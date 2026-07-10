import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_site.py"


class BuildSiteTests(unittest.TestCase):
    def test_build_creates_index_and_note_pages(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "site"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--output-dir", str(output_dir)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("Generated", result.stdout)
            self.assertTrue((output_dir / "index.html").exists())
            self.assertTrue((output_dir / ".nojekyll").exists())
            self.assertTrue((output_dir / "ai-ml" / "prompt-engineering-fundamentals.html").exists())

            html_text = (output_dir / "ai-ml" / "prompt-engineering-fundamentals.html").read_text(encoding="utf-8")
            self.assertIn("Prompt Engineering Fundamentals", html_text)
            self.assertIn("Core Techniques", html_text)

            index_html = (output_dir / "index.html").read_text(encoding="utf-8")
            self.assertIn("<h2>ai-ml</h2>", index_html)


if __name__ == "__main__":
    unittest.main()
