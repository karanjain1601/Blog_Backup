---
title: "Next.js App Router Patterns"
slug: "nextjs-app-router-patterns"
description: "Practical patterns for the Next.js App Router — layouts, loading states, and data fetching."
tags: ["nextjs", "react", "web-dev", "app-router"]
topic: "web-dev"
status: "published"
updated: "2026-07-05"
blocks_json: "W3siaWQiOiJiMSIsInR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJUaGUgTmV4dC5qcyBBcHAgUm91dGVyIGludHJvZHVjZWQgYSBwYXJhZGlnbSBzaGlmdCB3aXRoIFJlYWN0IFNlcnZlciBDb21wb25lbnRzIGFzIHRoZSBkZWZhdWx0LiJ9XX0seyJpZCI6ImIyIiwidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6W3sidHlwZSI6InRleHQiLCJ0ZXh0IjoiTGF5b3V0cyBhbmQgTG9hZGluZyBTdGF0ZXMifV19LHsiaWQiOiJiMyIsInR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJOZXN0ZWQgbGF5b3V0cyBlbmFibGUgcGVyc2lzdGVudCBVSSBhY3Jvc3Mgcm91dGUgY2hhbmdlcyB3aXRob3V0IHJlLW1vdW50aW5nIHNoYXJlZCBjb21wb25lbnRzLiJ9XX1d"
---

# Next.js App Router Patterns

The Next.js App Router introduced a paradigm shift with React Server Components as the default.

## Layouts and Loading States

Nested layouts enable persistent UI across route changes without re-mounting shared components.
