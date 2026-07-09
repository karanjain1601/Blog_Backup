---
title: "Next.js App Router Patterns"
slug: "nextjs-app-router-patterns"
description: "Practical patterns for the Next.js App Router — layouts, loading states, and data fetching."
tags: ["nextjs", "react", "web-dev", "app-router"]
topic: "web-dev"
status: "published"
updated: "2026-07-05"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIE5leHQuanMgQXBwIFJvdXRlciBpbnRyb2R1Y2VkIGEgcGFyYWRpZ20gc2hpZnQgd2l0aCBSZWFjdCBTZXJ2ZXIgQ29tcG9uZW50cyBhcyB0aGUgZGVmYXVsdC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXlvdXRzIGFuZCBMb2FkaW5nIFN0YXRlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmVzdGVkIGxheW91dHMgZW5hYmxlIHBlcnNpc3RlbnQgVUkgYWNyb3NzIHJvdXRlIGNoYW5nZXMgd2l0aG91dCByZS1tb3VudGluZyBzaGFyZWQgY29tcG9uZW50cy4ifV0="
---

# Next.js App Router Patterns

The Next.js App Router introduced a paradigm shift with React Server Components as the default.

## Layouts and Loading States

Nested layouts enable persistent UI across route changes without re-mounting shared components.
