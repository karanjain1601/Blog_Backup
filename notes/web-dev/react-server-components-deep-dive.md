---
title: "React Server Components Deep Dive"
slug: "react-server-components-deep-dive"
description: "How RSCs work under the hood and when to reach for them vs client components."
tags: ["react", "rsc", "web-dev", "performance"]
topic: "web-dev"
status: "published"
updated: "2026-06-28"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVhY3QgU2VydmVyIENvbXBvbmVudHMgcmVuZGVyIG9uIHRoZSBzZXJ2ZXIgYW5kIHNlbmQgc2VyaWFsaXplZCBvdXRwdXQgdG8gdGhlIGNsaWVudCwgZWxpbWluYXRpbmcgY2xpZW50LXNpZGUgZGF0YSBmZXRjaGluZyBmb3IgbWFueSB1c2UgY2FzZXMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbWVudGFsIG1vZGVsIHNoaWZ0OiBjb21wb25lbnRzIGFyZSBzZXJ2ZXItZmlyc3QgYnkgZGVmYXVsdCwgb3B0IGluIHRvIGNsaWVudCBpbnRlcmFjdGl2aXR5IHdpdGggYHVzZSBjbGllbnRgLiJ9XQ=="
---

# React Server Components Deep Dive

React Server Components render on the server and send serialized output to the client, eliminating client-side data fetching for many use cases.

The mental model shift: components are server-first by default, opt in to client interactivity with `use client`.
