---
title: "React Server Components Deep Dive"
slug: "react-server-components-deep-dive"
description: "How RSCs work under the hood and when to reach for them vs client components."
tags: ["react", "rsc", "web-dev", "performance"]
topic: "web-dev"
status: "published"
updated: "2026-06-28"
blocks_json: "W3siaWQiOiJiMSIsInR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJSZWFjdCBTZXJ2ZXIgQ29tcG9uZW50cyByZW5kZXIgb24gdGhlIHNlcnZlciBhbmQgc2VuZCBzZXJpYWxpemVkIG91dHB1dCB0byB0aGUgY2xpZW50LCBlbGltaW5hdGluZyBjbGllbnQtc2lkZSBkYXRhIGZldGNoaW5nIGZvciBtYW55IHVzZSBjYXNlcy4ifV19LHsiaWQiOiJiMiIsInR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJUaGUgbWVudGFsIG1vZGVsIHNoaWZ0OiBjb21wb25lbnRzIGFyZSBzZXJ2ZXItZmlyc3QgYnkgZGVmYXVsdCwgb3B0IGluIHRvIGNsaWVudCBpbnRlcmFjdGl2aXR5IHdpdGggdXNlIGNsaWVudC4ifV19XQ=="
---

# React Server Components Deep Dive

React Server Components render on the server and send serialized output to the client, eliminating client-side data fetching for many use cases.

The mental model shift: components are server-first by default, opt in to client interactivity with use client.
