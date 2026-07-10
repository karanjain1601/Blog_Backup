# Notes Backup

> Last synced: 2026-07-09

**6 notes** across **4 topics**

| Title | Status | Topic | Updated |
| ----- | ------ | ----- | ------- |
| [Next.js App Router Patterns](notes/web-dev/nextjs-app-router-patterns.md) | published | web-dev | 2026-07-09 |
| [React Server Components Deep Dive](notes/web-dev/react-server-components-deep-dive.md) | published | web-dev | 2026-07-09 |
| [Prompt Engineering Fundamentals](notes/ai-ml/prompt-engineering-fundamentals.md) | evergreen | ai-ml | 2026-07-09 |
| [Understanding Transformers](notes/ai-ml/understanding-transformers.md) | published | ai-ml | 2026-07-09 |
| [Building a Second Brain](notes/productivity/building-a-second-brain.md) | evergreen | productivity | 2026-07-09 |
| [Raw Thoughts on AI Agents](notes/_uncategorized/raw-thoughts-on-ai-agents.md) | draft | — | 2026-07-09 |

## GitHub Pages deployment

A workflow in [.github/workflows/deploy-pages.yml](.github/workflows/deploy-pages.yml) converts the markdown notes into static HTML and publishes the generated site from the gh-pages branch.

To enable GitHub Pages for the repository:

1. Open the repository Settings → Pages.
2. Choose Deploy from a branch.
3. Select the gh-pages branch and the / (root) folder.

The build step runs automatically on pushes to main and can also be triggered manually from the Actions tab.