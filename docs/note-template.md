---
title: "Note Title"
slug: "note-slug"
description: "One-sentence summary of what this note covers."
tags: ["tag-one", "tag-two"]
topic: "topic-slug"
status: "draft"
updated: "2026-07-09"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiV3JpdGUgeW91ciBpbnRyb2R1Y3Rpb24gaGVyZS4gU3VtbWFyaXNlIHdoYXQgdGhpcyBub3RlIGNvdmVycyBhbmQgd2h5IGl0IG1hdHRlcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VjdGlvbiBPbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJvZHkgY29udGVudCBmb3Igc2VjdGlvbiBvbmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VjdGlvbiBUd28ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJvZHkgY29udGVudCBmb3Igc2VjdGlvbiB0d28uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRmlyc3QgdGFrZWF3YXkiLCJTZWNvbmQgdGFrZWF3YXkiLCJUaGlyZCB0YWtlYXdheSJdfV0="
---

# Note Title

Write your introduction here. Summarise what this note covers and why it matters.

## Section One

Body content for section one.

## Section Two

Body content for section two.

## Key Takeaways

- First takeaway
- Second takeaway
- Third takeaway

---

<!--
FRONTMATTER FIELDS
==================
title       — Display title (required)
slug        — URL-safe identifier, must be unique (required)
description — One-line summary shown in listings (optional)
tags        — Array of tag strings (optional)
topic       — Topic slug for grouping; omit for _uncategorized (optional)
status      — "draft" | "published" | "evergreen"
              draft     → admin-only, not backed up by cron
              published → live on web, backed up by cron
              evergreen → live on web, backed up by cron, marked as long-lasting
updated     — ISO date YYYY-MM-DD
blocks_json — Base64-encoded JSON array of Block objects (see docs/blocks-reference.md)
              This is the source of truth for the note's content.
              The markdown body below the frontmatter is human-readable only.

ADDING BLOCKS
=============
1. Build the JSON array using the types in docs/blocks-reference.md
2. Base64-encode it:
   Node:       Buffer.from(JSON.stringify(blocks)).toString("base64")
   PowerShell: [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($json))
   Python:     import base64, json; base64.b64encode(json.dumps(blocks).encode()).decode()
3. Paste the result into the blocks_json frontmatter field

RESTORE
=======
The admin UI at /backup can restore notes from this repo into the database.
Restore uses slug as the conflict key — existing notes are upserted.
Missing topics referenced in `topic` are created automatically.
-->
