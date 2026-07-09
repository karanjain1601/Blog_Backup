# Block Types Reference

All 22 block types supported by the Notes KB schema. Every block may carry an optional `id` string for deep-linking.

---

## Leaf Blocks

### `text`
A paragraph of content. Markdown is supported in `content`.

```json
{ "type": "text", "content": "Your paragraph here. **Bold**, _italic_, `code`." }
```

| Field | Type | Required |
| --- | --- | --- |
| `content` | string | yes |

---

### `heading`
A section heading, levels 1–6.

```json
{ "type": "heading", "level": 2, "content": "Section Title" }
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `level` | integer 1–6 | yes | 1 = h1, 2 = h2, … |
| `content` | string | yes | |

---

### `code`
A syntax-highlighted code block.

```json
{
  "type": "code",
  "language": "typescript",
  "filename": "example.ts",
  "highlight": [3, 4],
  "content": "function greet(name: string) {\n  return `Hello, ${name}!`;\n}"
}
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `language` | string | no | defaults to `"text"` |
| `filename` | string | no | shown in code block header |
| `highlight` | integer[] | no | 1-indexed line numbers to highlight |
| `content` | string | yes | |

---

### `math`
A LaTeX math expression.

```json
{ "type": "math", "content": "E = mc^2", "display": true }
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `content` | string | yes | LaTeX expression |
| `display` | boolean | no | `true` = block math, `false` = inline; defaults to `true` |

---

### `callout`
A highlighted callout box. Five variants available.

```json
{
  "type": "callout",
  "variant": "info",
  "title": "Optional title",
  "content": "Callout body text."
}
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `variant` | string | no | `"info"` `"warning"` `"error"` `"tip"` `"note"` — defaults to `"note"` |
| `title` | string | no | if omitted, variant name is used |
| `content` | string | yes | |

---

### `quote`
A blockquote with optional attribution.

```json
{
  "type": "quote",
  "content": "The best way to predict the future is to invent it.",
  "cite": "Alan Kay"
}
```

| Field | Type | Required |
| --- | --- | --- |
| `content` | string | yes |
| `cite` | string | no |

---

### `list`
An ordered or unordered list.

```json
{ "type": "list", "ordered": false, "items": ["Item one", "Item two", "Item three"] }
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `ordered` | boolean | no | defaults to `false` |
| `items` | string[] | yes | |

---

### `todo`
A checklist.

```json
{
  "type": "todo",
  "items": [
    { "text": "Completed task", "checked": true },
    { "text": "Pending task", "checked": false }
  ]
}
```

| Field | Type | Required |
| --- | --- | --- |
| `items` | `{ text: string, checked: boolean }[]` | yes |

---

### `table`
A data table with headers and rows.

```json
{
  "type": "table",
  "headers": ["Name", "Type", "Required"],
  "rows": [
    ["content", "string", "yes"],
    ["language", "string", "no"]
  ]
}
```

| Field | Type | Required |
| --- | --- | --- |
| `headers` | string[] | yes |
| `rows` | string[][] | yes |

---

### `divider`
A horizontal rule. No extra fields.

```json
{ "type": "divider" }
```

---

### `image`
An image with alt text and optional caption.

```json
{
  "type": "image",
  "src": "https://example.com/image.png",
  "alt": "Descriptive alt text",
  "caption": "Optional caption shown below"
}
```

| Field | Type | Required |
| --- | --- | --- |
| `src` | URL string | yes |
| `alt` | string | yes |
| `caption` | string | no |

---

### `gallery`
A grid of images.

```json
{
  "type": "gallery",
  "images": [
    { "src": "https://example.com/a.png", "alt": "Image A" },
    { "src": "https://example.com/b.png", "alt": "Image B" }
  ]
}
```

| Field | Type | Required |
| --- | --- | --- |
| `images` | `{ src: URL, alt: string }[]` | yes |

---

### `video`
A native video player.

```json
{
  "type": "video",
  "src": "https://example.com/video.mp4",
  "poster": "https://example.com/thumb.jpg",
  "caption": "Optional caption"
}
```

| Field | Type | Required |
| --- | --- | --- |
| `src` | URL string | yes |
| `poster` | URL string | no |
| `caption` | string | no |

---

### `file`
A downloadable file link.

```json
{
  "type": "file",
  "src": "https://example.com/document.pdf",
  "name": "document.pdf",
  "size": "1.4 MB"
}
```

| Field | Type | Required |
| --- | --- | --- |
| `src` | URL string | yes |
| `name` | string | yes |
| `size` | string | no |

---

### `embed`
An embedded third-party resource (YouTube, Vimeo, tweet, CodePen, or generic iframe).

```json
{ "type": "embed", "provider": "youtube", "url": "https://www.youtube.com/watch?v=..." }
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `provider` | string | no | `"youtube"` `"vimeo"` `"tweet"` `"codepen"` `"generic"` — defaults to `"generic"` |
| `url` | URL string | yes | |

---

### `embed-note`
Transclude (embed) another note by slug — Obsidian-style `![[...]]`.

```json
{ "type": "embed-note", "target": "other-note-slug", "anchor": "#section-heading" }
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `target` | string | yes | slug of the note to embed |
| `anchor` | string | no | `#heading` or `^blockId` within the target |

---

### `mermaid`
A Mermaid diagram with optional tabs/stacked/split layout.

```json
{
  "type": "mermaid",
  "content": "graph TD\n  A --> B --> C",
  "title": "Optional caption",
  "layout": "tabs",
  "defaultTab": "diagram"
}
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `content` | string | yes | Mermaid syntax |
| `title` | string | no | |
| `layout` | string | no | `"tabs"` `"stacked"` `"split"` — defaults to `"tabs"` |
| `defaultTab` | string | no | `"diagram"` or `"source"` — defaults to `"diagram"` |

---

### `collection`
A live filtered view over notes (like a Notion linked database).

```json
{
  "type": "collection",
  "view": "list",
  "filter": { "topic": "ai-ml" },
  "groupBy": "status",
  "sort": "updated_at"
}
```

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `view` | string | no | `"table"` `"board"` `"gallery"` `"list"` — defaults to `"list"` |
| `filter` | object | no | key-value filter criteria |
| `groupBy` | string | no | field to group by |
| `sort` | string | no | field to sort by |

---

### `toc`
Auto-generated table of contents from the note's headings. Rendered as a page-level aside, not inline.

```json
{ "type": "toc" }
```

No additional fields.

---

## Container Blocks

These blocks nest other blocks inside them. Children follow the same schema recursively.

---

### `details`
A disclosure element — collapsed by default, expandable on click.

```json
{
  "type": "details",
  "summary": "Click to expand",
  "blocks": [
    { "type": "text", "content": "Hidden content revealed on expand." }
  ]
}
```

| Field | Type | Required |
| --- | --- | --- |
| `summary` | string | yes |
| `blocks` | Block[] | yes |

---

### `tabs`
Tabbed content — each tab has a label and its own block list.

```json
{
  "type": "tabs",
  "tabs": [
    { "label": "Python", "blocks": [{ "type": "code", "language": "python", "content": "print('hello')" }] },
    { "label": "TypeScript", "blocks": [{ "type": "code", "language": "typescript", "content": "console.log('hello')" }] }
  ]
}
```

| Field | Type | Required |
| --- | --- | --- |
| `tabs` | `{ label: string, blocks: Block[] }[]` | yes |

---

### `columns`
A multi-column layout. Each column holds its own block list.

```json
{
  "type": "columns",
  "columns": [
    { "blocks": [{ "type": "text", "content": "Left column." }] },
    { "blocks": [{ "type": "text", "content": "Right column." }] }
  ]
}
```

| Field | Type | Required |
| --- | --- | --- |
| `columns` | `{ blocks: Block[] }[]` | yes |

---

## Quick Reference

| Type | Category | Key Fields |
| --- | --- | --- |
| `text` | leaf | `content` |
| `heading` | leaf | `level`, `content` |
| `code` | leaf | `content`, `language?`, `filename?`, `highlight?` |
| `math` | leaf | `content`, `display?` |
| `callout` | leaf | `content`, `variant?`, `title?` |
| `quote` | leaf | `content`, `cite?` |
| `list` | leaf | `items`, `ordered?` |
| `todo` | leaf | `items[]` with `text` + `checked` |
| `table` | leaf | `headers`, `rows` |
| `divider` | leaf | — |
| `image` | leaf | `src`, `alt`, `caption?` |
| `gallery` | leaf | `images[]` with `src` + `alt` |
| `video` | leaf | `src`, `poster?`, `caption?` |
| `file` | leaf | `src`, `name`, `size?` |
| `embed` | leaf | `url`, `provider?` |
| `embed-note` | leaf | `target`, `anchor?` |
| `mermaid` | leaf | `content`, `title?`, `layout?`, `defaultTab?` |
| `collection` | leaf | `view?`, `filter?`, `groupBy?`, `sort?` |
| `toc` | leaf | — |
| `details` | container | `summary`, `blocks[]` |
| `tabs` | container | `tabs[]` with `label` + `blocks[]` |
| `columns` | container | `columns[]` with `blocks[]` |
