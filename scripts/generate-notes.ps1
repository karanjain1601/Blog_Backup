# generate-notes.ps1
# Reads a JSON file of note definitions and writes markdown files with base64-encoded blocks_json.
#
# Usage:
#   .\scripts\generate-notes.ps1 -DataFile "scripts\notes-data.json" -OutputDir "notes\math-foundations"
#
# See docs/note-generation-workflow.md for the full JSON schema and workflow guide.

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
    Write-Host "Created directory: $OutputDir"
}

$written = 0

foreach ($note in $notes) {

    # 1. Encode blocks_json
    $blocksArray = $note.blocks | ConvertTo-Json -Depth 20 -Compress
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($blocksArray)
    $b64 = [Convert]::ToBase64String($bytes)

    # 2. Build YAML frontmatter
    $tagsYaml = '["' + ($note.tags -join '", "') + '"]'
    $frontmatter = @"
---
title: "$($note.title)"
slug: "$($note.slug)"
description: "$($note.description)"
tags: $tagsYaml
topic: "$($note.topic)"
status: "$($note.status)"
updated: "$($note.updated)"
blocks_json: "$b64"
---
"@

    # 3. Build human-readable markdown body from blocks
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
                $body += "``````$lang`n$($block.content)`n```````n`n"
            }
            "list" {
                if ($block.ordered) {
                    $idx = 1
                    foreach ($item in $block.items) {
                        $body += "$idx. $item`n"
                        $idx++
                    }
                } else {
                    foreach ($item in $block.items) {
                        $body += "- $item`n"
                    }
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
                $disp = if ($block.display -ne $false) { "`$`$$($block.content)`$`$" } else { "`$$($block.content)`$" }
                $body += "$disp`n`n"
            }
            "quote" {
                $body += "> $($block.content)"
                if ($block.cite) { $body += ("`n> -- " + $block.cite) }
                $body += "`n`n"
            }
        }
    }

    # 4. Write file (UTF-8 without BOM)
    $filePath = Join-Path $OutputDir "$($note.slug).md"
    $fullContent = $frontmatter + "`n" + $body
    $utf8NoBOM = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($filePath, $fullContent, $utf8NoBOM)

    $kb = [math]::Round((Get-Item $filePath).Length / 1KB, 1)
    $codeCount = ($note.blocks | Where-Object { $_.type -eq 'code' } | Measure-Object).Count
    Write-Host "  [OK] $($note.slug).md  ($($note.blocks.Count) blocks, $codeCount code, $kb KB)"
    $written++
}

Write-Host ""
Write-Host "Done. $written notes written to $OutputDir"
