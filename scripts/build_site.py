#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

import markdown

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NOTES_DIR = ROOT / "notes"
DEFAULT_OUTPUT_DIR = ROOT / "site"


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    if not text.startswith("---"):
        return {}, text

    match = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n?(.*)$", text, re.S)
    if not match:
        return {}, text

    metadata: Dict[str, object] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
            value = value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            items = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
            value = items

        metadata[key] = value

    return metadata, match.group(2).strip()


def render_note_page(title: str, metadata: Dict[str, object], body: str, relative_index_path: str) -> str:
    body_html = markdown.markdown(body, extensions=["extra"])
    meta_items = []
    for key in ["description", "topic", "status", "updated"]:
        if metadata.get(key):
            meta_items.append(f"<li><strong>{html.escape(key)}:</strong> {html.escape(str(metadata[key]))}</li>")

    meta_html = "".join(meta_items)
    if meta_html:
        meta_html = f"<ul class='note-meta'>{meta_html}</ul>"

    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{html.escape(title)} | Notes Backup</title>
  <meta name=\"description\" content=\"{html.escape(str(metadata.get('description', '')))}\" />
  <style>
    :root {{ color-scheme: light dark; font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
    body {{ margin: 0; background: #0f172a; color: #e2e8f0; }}
    main {{ max-width: 860px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; }}
    a {{ color: #7dd3fc; }}
    .back-link {{ display: inline-block; margin-bottom: 1.5rem; }}
    article {{ background: #111827; border: 1px solid #334155; border-radius: 14px; padding: 2rem; box-shadow: 0 20px 45px rgba(15, 23, 42, 0.2); }}
    .note-meta {{ padding-left: 1rem; color: #cbd5e1; }}
    code {{ background: rgba(255,255,255,0.08); padding: 0.1rem 0.25rem; border-radius: 4px; }}
    pre {{ background: #020617; padding: 1rem; border-radius: 8px; overflow-x: auto; }}
  </style>
</head>
<body>
  <main>
    <a class=\"back-link\" href=\"{relative_index_path}\">← Back to notes index</a>
    <article>
      <h1>{html.escape(title)}</h1>
      {meta_html}
      {body_html}
    </article>
  </main>
</body>
</html>
"""


def render_index_page(entries: List[Dict[str, str]], output_dir: Path) -> str:
    items = []
    for entry in entries:
        items.append(
            f"<li><a href=\"{entry['href']}\">{html.escape(entry['title'])}</a> — {html.escape(entry['description'])}</li>"
        )

    list_html = "\n".join(items) if items else "<li>No notes found.</li>"
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Notes Backup</title>
  <meta name=\"description\" content=\"Static HTML export of the notes repository\" />
  <style>
    :root {{ color-scheme: light dark; font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
    body {{ margin: 0; background: #0f172a; color: #e2e8f0; }}
    main {{ max-width: 860px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; }}
    a {{ color: #7dd3fc; }}
    ul {{ line-height: 1.75; }}
  </style>
</head>
<body>
  <main>
    <h1>Notes Backup</h1>
    <p>This static site is generated from the markdown notes in the repository.</p>
    <ul>
      {list_html}
    </ul>
  </main>
</body>
</html>
"""


def build_site(notes_dir: Path, output_dir: Path) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    notes = sorted(notes_dir.rglob("*.md"))
    entries: List[Dict[str, str]] = []

    for source_path in notes:
        metadata, body = parse_frontmatter(source_path.read_text(encoding="utf-8"))
        title = str(metadata.get("title") or source_path.stem.replace("-", " ").title())
        description = str(metadata.get("description") or "")

        relative_output_path = source_path.relative_to(notes_dir).with_suffix(".html")
        output_path = output_dir / relative_output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        relative_index_path = os.path.relpath(output_dir / "index.html", output_path.parent).replace(os.sep, "/")
        output_path.write_text(
            render_note_page(title, metadata, body, relative_index_path),
            encoding="utf-8",
        )

        entries.append(
            {
                "title": title,
                "description": description,
                "href": relative_output_path.as_posix(),
            }
        )

    (output_dir / "index.html").write_text(render_index_page(entries, output_dir), encoding="utf-8")
    (output_dir / "404.html").write_text(
        """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Page not found</title>
</head>
<body>
  <h1>Page not found</h1>
  <p>The requested page could not be found.</p>
</body>
</html>
""",
        encoding="utf-8",
    )
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")

    return [output_dir / entry["href"] for entry in entries]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a static HTML site from the markdown notes")
    parser.add_argument("--notes-dir", type=Path, default=DEFAULT_NOTES_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    output_files = build_site(args.notes_dir.resolve(), args.output_dir.resolve())
    print(f"Generated {len(output_files)} HTML pages in {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
