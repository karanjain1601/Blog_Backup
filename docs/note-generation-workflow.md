# Note Generation Workflow

The recommended way to batch-generate notes is:

1. **Write all note content into a JSON file** (`notes-data.json`)
2. **Run a single PowerShell script** (`generate-notes.ps1`) that encodes and writes all markdown files

This approach lets the author focus entirely on content quality during JSON authoring, without context-switching to encoding between each note. It's also repeatable — re-run the script to regenerate any notes after editing the JSON.

---

## Step 1 — Create the JSON data file

Create a file like `scripts/notes-data.json` with this structure:

```json
[
  {
    "slug": "example-topic",
    "title": "Example Topic",
    "description": "One sentence summary of what this note covers.",
    "tags": ["tag1", "tag2", "math", "foundations"],
    "topic": "math-foundations",
    "status": "published",
    "updated": "2026-07-10",
    "blocks": [
      {
        "type": "text",
        "content": "Introduction paragraph explaining what this note covers and why it matters for ML/AI."
      },
      {
        "type": "heading",
        "level": 2,
        "content": "Core Definition"
      },
      {
        "type": "text",
        "content": "Detailed definition with math notation inline: f(x) = Σ wᵢxᵢ + b."
      },
      {
        "type": "code",
        "language": "python",
        "content": "import numpy as np\n\n# Working example\nA = np.array([[1, 2], [3, 4]])\neigenvalues, eigenvectors = np.linalg.eig(A)\nprint('Eigenvalues:', eigenvalues)"
      },
      {
        "type": "heading",
        "level": 2,
        "content": "Key Properties"
      },
      {
        "type": "text",
        "content": "..."
      },
      {
        "type": "code",
        "language": "python",
        "content": "import torch\n\n# Second code example\n..."
      },
      {
        "type": "callout",
        "variant": "warning",
        "title": "Common Pitfall",
        "content": "Description of what goes wrong."
      },
      {
        "type": "table",
        "headers": ["Method", "Pros", "Cons"],
        "rows": [
          ["Option A", "Fast", "Less accurate"],
          ["Option B", "Accurate", "Slower"]
        ]
      },
      {
        "type": "divider"
      },
      {
        "type": "heading",
        "level": 2,
        "content": "Key Takeaways"
      },
      {
        "type": "list",
        "ordered": false,
        "items": [
          "First takeaway",
          "Second takeaway"
        ]
      }
    ]
  }
]
```

See `docs/blocks-reference.md` for all 22 block types and their fields.
See `docs/note-quality-guide.md` for quality targets (block count, code block depth, etc.).

---

## Step 2 — Run the generation script

Save the script below as `scripts/generate-notes.ps1`, then run:

```powershell
cd "c:\Users\karan.e.jain\Projects_Self\Blog_Backup"
.\scripts\generate-notes.ps1 -DataFile "scripts\notes-data.json" -OutputDir "notes\math-foundations"
```

---

## The Generation Script

```powershell
# generate-notes.ps1
# Usage: .\generate-notes.ps1 -DataFile <path-to-json> -OutputDir <output-folder>

param(
    [Parameter(Mandatory=$true)]
    [string]$DataFile,

    [Parameter(Mandatory=$true)]
    [string]$OutputDir
)

# Load note definitions
$notes = Get-Content $DataFile -Raw -Encoding UTF8 | ConvertFrom-Json

# Ensure output directory exists
if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

$written = 0
$skipped = 0

foreach ($note in $notes) {
    # --- 1. Encode blocks_json ---
    $blocksArray = $note.blocks | ConvertTo-Json -Depth 20 -Compress
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($blocksArray)
    $b64 = [Convert]::ToBase64String($bytes)

    # --- 2. Build YAML frontmatter ---
    $tagsYaml = '["' + ($note.tags -join '", "') + '"]'
    $frontmatter = "---`ntitle: `"$($note.title)`"`nslug: `"$($note.slug)`"`ndescription: `"$($note.description)`"`ntags: $tagsYaml`ntopic: `"$($note.topic)`"`nstatus: `"$($note.status)`"`nupdated: `"$($note.updated)`"`nblocks_json: `"$b64`"`n---`n"

    # --- 3. Build human-readable markdown body from blocks ---
    $body = "# $($note.title)`n`n"

    foreach ($block in $note.blocks) {
        switch ($block.type) {
            "text" {
                $body += "$($block.content)`n`n"
            }
            "heading" {
                $hashes = "#" * $block.level
                $body += "$hashes $($block.content)`n`n"
            }
            "code" {
                $lang = if ($block.language) { $block.language } else { "" }
                $body += "``````$lang`n$($block.content)`n``````"`n`n"
            }
            "list" {
                if ($block.ordered) {
                    $idx = 1
                    foreach ($item in $block.items) { $body += "$idx. $item`n"; $idx++ }
                } else {
                    foreach ($item in $block.items) { $body += "- $item`n" }
                }
                $body += "`n"
            }
            "callout" {
                $t = if ($block.title) { $block.title } else { $block.variant }
                $body += "> **$t**: $($block.content)`n`n"
            }
            "table" {
                $body += "| " + ($block.headers -join " | ") + " |`n"
                $body += "| " + (($block.headers | ForEach-Object { "---" }) -join " | ") + " |`n"
                foreach ($row in $block.rows) {
                    $body += "| " + ($row -join " | ") + " |`n"
                }
                $body += "`n"
            }
            "divider" {
                $body += "---`n`n"
            }
            "math" {
                $body += "`$`$$($block.content)`$`$`n`n"
            }
            "quote" {
                $body += "> $($block.content)"
                if ($block.cite) { $body += "`n> — $($block.cite)" }
                $body += "`n`n"
            }
        }
    }

    # --- 4. Write file ---
    $filePath = Join-Path $OutputDir "$($note.slug).md"
    $fullContent = $frontmatter + "`n" + $body
    [System.IO.File]::WriteAllText($filePath, $fullContent, [System.Text.Encoding]::UTF8)

    Write-Host "  [OK] $($note.slug).md"
    $written++
}

Write-Host ""
Write-Host "Done. Written: $written, Skipped: $skipped"
```

---

## Why this approach produces better notes

When an agent writes all JSON content first (without encoding each block), it can:

- Think about the **full narrative** across all 20+ blocks before committing to any text
- Write **richer code examples** (with imports, comments, realistic data) because it's not context-switching between content and encoding
- Achieve **consistent structure** across all notes in one pass
- **Batch-encode** all notes with a single script run (no per-note PowerShell calls)

### Agent prompt pattern that works well

Tell the agent:

> 1. Write all note definitions into a JSON file at `scripts/notes-data.json`
> 2. Run `generate-notes.ps1` to produce all markdown files

This lets the agent spend its entire reasoning budget on content quality, not on encoding mechanics.

---

## Validating the output

After generation, check quality:

```powershell
cd "c:\Users\karan.e.jain\Projects_Self\Blog_Backup\notes\math-foundations"

foreach ($file in Get-ChildItem *.md) {
    $b64 = [regex]::Match((Get-Content $file.FullName -Raw), 'blocks_json:\s+"([^"]+)"').Groups[1].Value
    $json = [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($b64))
    $blocks = $json | ConvertFrom-Json
    $codeBlocks = ($blocks | Where-Object {$_.type -eq 'code'} | Measure-Object).Count
    $kb = [math]::Round($file.Length / 1KB, 1)
    Write-Host "$($file.BaseName): $($blocks.Count) blocks, $codeBlocks code, $kb KB"
}
```

Target per note: **≥20 blocks, ≥3 code blocks, ≥18 KB**.
