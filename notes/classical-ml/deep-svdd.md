---
title: "Deep SVDD — Deep One-Class Classification"
slug: "deep-svdd"
description: "Implement Deep Support Vector Data Description for one-class anomaly detection: the hypersphere objective that clusters normal representations around a center, center initialization, collapse prevention, autoencoder pretraining, and comparison with OCSVM and reconstruction-based methods."
tags: ["anomaly-detection", "density-estimation", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVlcCBTVkREIChSdWZmIGV0IGFsLiwgMjAxOCkgZXh0ZW5kcyB0aGUgY2xhc3NpY2FsIFN1cHBvcnQgVmVjdG9yIERhdGEgRGVzY3JpcHRpb24gdG8gZGVlcCBuZXR3b3Jrcy4gVGhlIGlkZWEgaXMgZWxlZ2FudDogdHJhaW4gYSBuZXVyYWwgbmV0d29yayDPhih4O1cpIHRvIG1hcCBhbGwgbm9ybWFsIHRyYWluaW5nIGRhdGEgdG8gYSBjb21wYWN0IGh5cGVyc3BoZXJlIHdpdGggY2VudGVyIGMgaW4gdGhlIGxhdGVudCBzcGFjZS4gQXQgdGVzdCB0aW1lLCBwb2ludHMgdGhhdCBtYXAgZmFyIGZyb20gYyBhcmUgYW5vbWFsaWVzLiBVbmxpa2UgYXV0b2VuY29kZXJzIHRoYXQgZGV0ZWN0IGFub21hbGllcyB2aWEgcmVjb25zdHJ1Y3Rpb24gZXJyb3IsIERlZXAgU1ZERCBkZXRlY3RzIGFub21hbGllcyBieSB0aGVpciBkaXN0YW5jZSBmcm9tIHRoZSBsZWFybmVkIG5vcm1hbCBtYW5pZm9sZCBpbiByZXByZXNlbnRhdGlvbiBzcGFjZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGcm9tIFNWREQgdG8gRGVlcCBTVkREIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFzc2ljYWwgU1ZERCBmaXRzIHRoZSBtaW5pbXVtLXZvbHVtZSBoeXBlcnNwaGVyZSBjb250YWluaW5nIGFsbCB0cmFpbmluZyBkYXRhIGluIGtlcm5lbCBmZWF0dXJlIHNwYWNlLCB3aXRoIHNvZnQtYm91bmRhcnkgdmFyaWFudCB1c2luZyBzbGFjayB2YXJpYWJsZXMuIFRoZSBrZXJuZWwgdmVyc2lvbiBpcyBlcXVpdmFsZW50IHRvIG9uZS1jbGFzcyBTVk0uIFRoZSBsaW1pdGF0aW9uOiB0aGUga2VybmVsIGlzIGZpeGVkIGFuZCB0aGUgcmVwcmVzZW50YXRpb24gaXMgbm90IGxlYXJuZWQgZnJvbSBkYXRhLiBEZWVwIFNWREQgYWRkcmVzc2VzIHRoaXMgYnkgam9pbnRseSBvcHRpbWlzaW5nIHRoZSBtYXBwaW5nIM+GIGFuZCB0aGUgY2VudGVyIGM6IG1pbl97VyxjfSAoMS9uKSDOo+G1oiDigJbPhih44bWiO1cpIOKIkiBj4oCWwrIuIFRoZSBuZXR3b3JrIGxlYXJucyBhIHJlcHJlc2VudGF0aW9uIHdoZXJlIG5vcm1hbCBkYXRhIGlzIGNvbXBhY3Q7IGFub21hbGllcywgaGF2aW5nIGEgZGlmZmVyZW50IHN0cnVjdHVyZSwgbWFwIHRvIGRpc3RhbnQgcmVnaW9ucy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIk9iamVjdGl2ZTogbWluaW1pc2Ugc3F1YXJlZCBkaXN0YW5jZXMgZnJvbSBsYXRlbnQgY29kZXMgdG8gY2VudGVyIGMg4oCUIGZvcmNlcyBub3JtYWwgZGF0YSBpbnRvIGEgdGlnaHQgY2x1c3Rlci4iLCJDZW50ZXIgYzogaW5pdGlhbGlzZWQgYXMgdGhlIG1lYW4gb2YgYSBmb3J3YXJkIHBhc3Mgb24gYWxsIHRyYWluaW5nIGRhdGE7IHRoZW4gZml4ZWQgZHVyaW5nIHRyYWluaW5nIHRvIHByZXZlbnQgdHJpdmlhbCBzb2x1dGlvbnMuIiwiQW5vbWFseSBzY29yZTog4oCWz4YoeDtXKeKIkmPigJbCsiDigJQgbGFyZ2VyIGRpc3RhbmNlIGZyb20gY2VudGVyIGluZGljYXRlcyBoaWdoZXIgYW5vbWFseSBsaWtlbGlob29kLiIsIkNvbGxhcHNlIHByZXZlbnRpb246IHJlbW92aW5nIGJpYXMgdGVybXMgaW4gdGhlIGxhc3QgbGF5ZXIgYW5kIGJvdW5kZWQgYWN0aXZhdGlvbnMgcHJldmVudHMgdGhlIG5ldHdvcmsgZnJvbSBtYXBwaW5nIGV2ZXJ5dGhpbmcgdG8gYy4iLCJTb2Z0LWJvdW5kYXJ5IHZhcmlhbnQ6IGFkZCBoeXBlcnNwaGVyZSByYWRpdXMgUiBhcyBhIHZhcmlhYmxlIHdpdGggcGVuYWx0eSBDwrfOoyBtYXgoMCzigJbPhih44bWiKeKIkmPigJbCsuKIklLCsikuIl19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIERlZXBTVkREKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfaW4sIGRfbGF0PTE2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgICMgTm8gYmlhcyBpbiBmaW5hbCBsYXllcjsgbm8gYm91bmRlZCBhY3RpdmF0aW9ucyDigJQgcHJldmVudHMgY29sbGFwc2VcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGRfaW4sIDY0LCBiaWFzPVRydWUpLCAgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDY0LCAzMiwgYmlhcz1UcnVlKSwgICAgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDMyLCBkX2xhdCwgYmlhcz1GYWxzZSkgICMgbm8gYmlhcyBoZXJlXG4gICAgICAgIClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeClcblxuZGVmIGluaXRfY2VudGVyKG1vZGVsLCBYX3RyYWluLCBlcHM9MC4xKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdDZW50ZXIgPSBtZWFuIG9mIGVuY29kZXIgb3V0cHV0cyBvbiB0cmFpbmluZyBkYXRhLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIG1vZGVsLmV2YWwoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICB6ID0gbW9kZWwoWF90cmFpbilcbiAgICBjID0gei5tZWFuKGRpbT0wKVxuICAgICMgQXZvaWQgbmVhci16ZXJvIGNlbnRlciAod291bGQgbWFrZSBjb2xsYXBzZSBlYXNpZXIpXG4gICAgY1soYy5hYnMoKSBcdTAwM2MgZXBzKSBcdTAwMjYgKGMgXHUwMDNlPSAwKV0gPSAgZXBzXG4gICAgY1soYy5hYnMoKSBcdTAwM2MgZXBzKSBcdTAwMjYgKGMgXHUwMDNjIDApXSAgPSAtZXBzXG4gICAgcmV0dXJuIGMuZGV0YWNoKClcblxuZGVmIHN2ZGRfbG9zcyhtb2RlbCwgeCwgY2VudGVyKTpcbiAgICB6ID0gbW9kZWwoeClcbiAgICByZXR1cm4gKCh6IC0gY2VudGVyKSAqKiAyKS5zdW0oZGltPS0xKS5tZWFuKClcblxudG9yY2gubWFudWFsX3NlZWQoMCk7IG5wLnJhbmRvbS5zZWVkKDApXG5YX3RyID0gdG9yY2gudGVuc29yKG5wLnJhbmRvbS5yYW5kbig2MDAsIDIwKSwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnN2ZGQgPSBEZWVwU1ZERChkX2luPTIwLCBkX2xhdD0xNilcbmNlbnRlciA9IGluaXRfY2VudGVyKHN2ZGQsIFhfdHIpXG5vcHQgPSB0b3JjaC5vcHRpbS5BZGFtKHN2ZGQucGFyYW1ldGVycygpLCBscj0xZS0zKVxuc3ZkZC50cmFpbigpXG5mb3IgZXAgaW4gcmFuZ2UoMzApOlxuICAgIGxvc3MgPSBzdmRkX2xvc3Moc3ZkZCwgWF90ciwgY2VudGVyKVxuICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgaWYgKGVwKzEpICUgMTAgPT0gMDpcbiAgICAgICAgcHJpbnQoZlx1MDAyN0Vwb2NoIHtlcCsxOjJkfSB8IFNWREQgbG9zczoge2xvc3MuaXRlbSgpOi42Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSHlwZXJzcGhlcmUgT2JqZWN0aXZlIGFuZCBDZW50ZXIgSW5pdGlhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjZW50ZXIgYyBpcyBjb21wdXRlZCBhcyB0aGUgbWVhbiBvZiDPhih44bWiO1cpIG9uIGFsbCB0cmFpbmluZyBkYXRhIHVzaW5nIGEgZm9yd2FyZCBwYXNzIGJlZm9yZSBvcHRpbWlzYXRpb24gYmVnaW5zLCB0aGVuIGhlbGQgZml4ZWQuIFRoaXMgdHdvLXBoYXNlIGFwcHJvYWNoIHByZXZlbnRzIHRoZSBuZXR3b3JrIGZyb20gdHJpdmlhbGx5IHNhdGlzZnlpbmcgdGhlIG9iamVjdGl2ZSBieSByb3RhdGluZyB0byBwbGFjZSBjIGF0IHRoZSBvcmlnaW4uIFRoZSBvYmplY3RpdmUgbWluIOKAls+GKHgp4oiSY+KAlsKyIGlzIGEgZm9ybSBvZiBkZWVwIGNsdXN0ZXJpbmcgd2l0aCBhIHNpbmdsZSBjZW50cm9pZCDigJQgcmVsYXRlZCB0byBrLW1lYW5zIHdpdGggaz0xLiBUaGUgdHJhaW5pbmcgZHluYW1pY3MgcHVsbCBhbGwgcmVwcmVzZW50YXRpb25zIHRvd2FyZCBjOiB0aGUgbmV0d29yayBtdXN0IGxlYXJuIGEgY29tcGFjdCByZXByZXNlbnRhdGlvbiBvZiB0aGUgbm9ybWFsIGNsYXNzIHRvIG1pbmltaXNlIHRoZSBvYmplY3RpdmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuXG5ucC5yYW5kb20uc2VlZCgxKTsgdG9yY2gubWFudWFsX3NlZWQoMSlcbiMgT25lLWNsYXNzIGNsYXNzaWZpY2F0aW9uOiBjbGFzcyAwID0gbm9ybWFsLCBldmVyeXRoaW5nIGVsc2UgPSBhbm9tYWx5XG5YX25vcm0gPSB0b3JjaC50ZW5zb3IobnAucmFuZG9tLnJhbmRuKDQwMCwgMjApLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuWF9hbm9tID0gdG9yY2gudGVuc29yKG5wLnJhbmRvbS5yYW5kbig4MCwgMjApICogMC4zICsgMywgZHR5cGU9dG9yY2guZmxvYXQzMilcblxuc3ZkZDIgPSBEZWVwU1ZERChkX2luPTIwLCBkX2xhdD0xNilcbmMyID0gaW5pdF9jZW50ZXIoc3ZkZDIsIFhfbm9ybSlcbm9wdDIgPSB0b3JjaC5vcHRpbS5BZGFtKHN2ZGQyLnBhcmFtZXRlcnMoKSwgbHI9NWUtNClcbnN2ZGQyLnRyYWluKClcbmZvciBlcCBpbiByYW5nZSg1MCk6XG4gICAgbG9zczIgPSBzdmRkX2xvc3Moc3ZkZDIsIFhfbm9ybSwgYzIpXG4gICAgb3B0Mi56ZXJvX2dyYWQoKTsgbG9zczIuYmFja3dhcmQoKTsgb3B0Mi5zdGVwKClcblxuc3ZkZDIuZXZhbCgpXG5YX2FsbCA9IHRvcmNoLmNhdChbWF9ub3JtWzoxMDBdLCBYX2Fub21dKVxueV9hbGwgPSBucC5hcnJheShbMF0qMTAwICsgWzFdKjgwKVxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgel9hbGwgPSBzdmRkMihYX2FsbClcbiAgICBzY29yZXMgPSAoKHpfYWxsIC0gYzIpICoqIDIpLnN1bShkaW09LTEpLm51bXB5KClcbmF1cm9jID0gcm9jX2F1Y19zY29yZSh5X2FsbCwgc2NvcmVzKVxucHJpbnQoZlx1MDAyN0RlZXAgU1ZERCBBVVJPQzoge2F1cm9jOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3Tm9ybWFsIG1lYW4gZGlzdGFuY2UgZnJvbSBjZW50ZXI6IHtzY29yZXNbOjEwMF0ubWVhbigpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3QW5vbWFseSBtZWFuIGRpc3RhbmNlIGZyb20gY2VudGVyOiB7c2NvcmVzWzEwMDpdLm1lYW4oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbGxhcHNlIFByZXZlbnRpb24gYW5kIFRyYWluaW5nIFRyaWNrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGh5cGVyc3BoZXJlIGNvbGxhcHNlIHByb2JsZW0gb2NjdXJzIHdoZW4gdGhlIG5ldHdvcmsgbWFwcyBldmVyeXRoaW5nIHRvIHRoZSBjZW50ZXIgYyBieSBzZXR0aW5nIGFsbCB3ZWlnaHRzIHRvIHplcm8gKHRyaXZpYWwgc29sdXRpb24pLiBUd28gYXJjaGl0ZWN0dXJhbCB0cmlja3MgcHJldmVudCB0aGlzOiAoMSkgUmVtb3ZlIGJpYXMgdGVybXMgaW4gdGhlIHBlbnVsdGltYXRlIGFuZCBmaW5hbCBsYXllcnMg4oCUIHRoZSBiaWFzIGNvdWxkIHNoaWZ0IHJlcHJlc2VudGF0aW9ucyB0byBjb2luY2lkZSB3aXRoIGMgcmVnYXJkbGVzcyBvZiBpbnB1dC4gKDIpIEF2b2lkIGJvdW5kZWQgYWN0aXZhdGlvbnMgbGlrZSBzaWdtb2lkIG9yIHRhbmggaW4gdGhlIG5ldHdvcmsg4oCUIHRoZXkgY2FuIHNhdHVyYXRlIGFuZCBwcm9kdWNlIGEgY29uc3RhbnQgb3V0cHV0LiBCYXRjaCBub3JtYWxpc2F0aW9uIGNhbiBhbHNvIGNhdXNlIGNvbGxhcHNlIGlmIHRoZSBub3JtYWxpc2VkIG1lYW4gZXF1YWxzIGMuIFVzZSBsYXllciBub3JtYWxpc2F0aW9uIG9yIGF2b2lkIG5vcm1hbGlzYXRpb24gaW4gdGhlIGxhc3QgbGF5ZXIuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJDb2xsYXBzZSBSaXNrIiwiY29udGVudCI6IklmIHlvdXIgRGVlcCBTVkREIGxvc3MgZ29lcyB0byB6ZXJvIHZlcnkgcXVpY2tseSAod2l0aGluIDUgZXBvY2hzKSwgc3VzcGVjdCBjb2xsYXBzZS4gRGlhZ25vc2UgYnkgY2hlY2tpbmcgaWYgYWxsIHRyYWluaW5nIGVtYmVkZGluZ3MgYXJlIGlkZW50aWNhbCAoc3RkIOKJiCAwKS4gRml4OiAoMSkgcmVtb3ZlIGJpYXMgaW4gdGhlIGxhc3QgbGluZWFyIGxheWVyLCAoMikgcmVwbGFjZSBzaWdtb2lkL3Rhbmggd2l0aCBSZUxVLCAoMykgZGlzYWJsZSBiYXRjaCBub3JtIGluIHRoZSBmaW5hbCBibG9jay4gQWxzbyBjaGVjayB0aGF0IHRoZSBjZW50ZXIgYyBpcyBub3QgbmVhciB6ZXJvIOKAlCBhIG5lYXItemVybyBjZW50ZXIgbWFrZXMgY29sbGFwc2UgZWFzaWVyLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIEF1dG9lbmNvZGVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfaW4sIGRfbGF0PTE2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9pbiwgNjQpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoNjQsIDMyKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDMyLCBkX2xhdCkpXG4gICAgICAgIHNlbGYuZGVjb2RlciA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9sYXQsIDMyKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDMyLCA2NCksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcig2NCwgZF9pbikpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLmRlY29kZXIoc2VsZi5lbmNvZGVyKHgpKVxuXG5ucC5yYW5kb20uc2VlZCgyKTsgdG9yY2gubWFudWFsX3NlZWQoMilcblhfdHJfYWUgPSB0b3JjaC50ZW5zb3IobnAucmFuZG9tLnJhbmRuKDUwMCwgMjApLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuYWUgPSBBdXRvZW5jb2RlcihkX2luPTIwLCBkX2xhdD0xNilcbm9wdF9hZSA9IHRvcmNoLm9wdGltLkFkYW0oYWUucGFyYW1ldGVycygpLCBscj0xZS0zKVxuZm9yIGVwIGluIHJhbmdlKDMwKTpcbiAgICBsb3NzX2FlID0gbm4uZnVuY3Rpb25hbC5tc2VfbG9zcyhhZShYX3RyX2FlKSwgWF90cl9hZSlcbiAgICBvcHRfYWUuemVyb19ncmFkKCk7IGxvc3NfYWUuYmFja3dhcmQoKTsgb3B0X2FlLnN0ZXAoKVxuICAgIGlmIChlcCsxKSAlIDEwID09IDA6XG4gICAgICAgIHByaW50KGZcdTAwMjdBRSBwcmV0cmFpbiBlcG9jaCB7ZXArMToyZH0gfCByZWNvbiBsb3NzOiB7bG9zc19hZS5pdGVtKCk6LjZmfVx1MDAyNylcbiMgVHJhbnNmZXIgZW5jb2RlciB3ZWlnaHRzIHRvIERlZXAgU1ZERFxuc3ZkZDMgPSBEZWVwU1ZERChkX2luPTIwLCBkX2xhdD0xNilcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIGZvciAobjEsIHAxKSwgKG4yLCBwMikgaW4gemlwKFxuICAgICAgICAgICAgYWUuZW5jb2Rlci5uYW1lZF9wYXJhbWV0ZXJzKCksXG4gICAgICAgICAgICBzdmRkMy5uZXQubmFtZWRfcGFyYW1ldGVycygpKTpcbiAgICAgICAgaWYgcDEuc2hhcGUgPT0gcDIuc2hhcGU6XG4gICAgICAgICAgICBwMi5jb3B5XyhwMSlcbnByaW50KFx1MDAyN0VuY29kZXIgd2VpZ2h0cyB0cmFuc2ZlcnJlZCB0byBTVkREIG5ldHdvcmsuXHUwMDI3KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJldHJhaW5pbmcgd2l0aCBhbiBhdXRvZW5jb2RlciBnaXZlcyB0aGUgU1ZERCBlbmNvZGVyIGEgaGVhZCBzdGFydDogdGhlIGVuY29kZXIgYWxyZWFkeSBrbm93cyBob3cgdG8gcmVwcmVzZW50IHRoZSBub3JtYWwgZGF0YSBtYW5pZm9sZCBiZWZvcmUgdGhlIGh5cGVyc3BoZXJlIG9iamVjdGl2ZSBiZWdpbnMgcHVsbGluZyByZXByZXNlbnRhdGlvbnMgdG93YXJkIGMuIFdpdGhvdXQgcHJldHJhaW5pbmcsIHRoZSByYW5kb20gaW5pdGlhbGlzYXRpb24gbWVhbnMgdGhlIGNlbnRlciBjIGlzIGluaXRpYWxpc2VkIGluIGFuIGFyYml0cmFyeSByZWdpb24gb2YgdGhlIGVtYmVkZGluZyBzcGFjZSwgYW5kIHRoZSBTVkREIG9iamVjdGl2ZSBtYXkgY29sbGFwc2Ugb3IgY29udmVyZ2UgdG8gYSBwb29yIGxvY2FsIG1pbmltdW0uIFdpdGggcHJldHJhaW5pbmcsIHRoZSBjZW50ZXIgaW5pdGlhbGlzYXRpb24gKG1lYW4gb2YgZW5jb2RlciBvdXRwdXRzKSBsYW5kcyBuZWFyIHRoZSB0cnVlIGRhdGEgbWVhbiBpbiBhIG1lYW5pbmdmdWwgcmVwcmVzZW50YXRpb24gc3BhY2UsIHNpZ25pZmljYW50bHkgaW1wcm92aW5nIGZpbmFsIGRldGVjdGlvbiBwZXJmb3JtYW5jZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTb2Z0LUJvdW5kYXJ5IERlZXAgU1ZERCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGhhcmQtYm91bmRhcnkgdmFyaWFudCBtaW5pbWlzZXMgdGhlIG1lYW4gc3F1YXJlZCBkaXN0YW5jZSB0byBjLCBpbXBsaWNpdGx5IGFzc3VtaW5nIGFsbCB0cmFpbmluZyBkYXRhIGlzIG5vcm1hbC4gSWYgdHJhaW5pbmcgZGF0YSBpcyBjb250YW1pbmF0ZWQgYnkgYSBzbWFsbCBmcmFjdGlvbiBvZiBhbm9tYWxpZXMsIGEgc29mdC1ib3VuZGFyeSBmb3JtdWxhdGlvbiBpcyBtb3JlIHJvYnVzdDogbWluX3tXLFIsY30gUsKyICsgQ8K3KDEvbinOoyBtYXgoMCwg4oCWz4YoeOG1oiniiJJj4oCWwrLiiJJSwrIpLiBUaGUgcmFkaXVzIFIgYWN0cyBhcyBhIHNsYWNrIHRocmVzaG9sZDogcG9pbnRzIG91dHNpZGUgdGhlIHNwaGVyZSBvZiByYWRpdXMgUiBpbmN1ciBhIHBlbmFsdHkgc2NhbGVkIGJ5IEMuIFNldHRpbmcgQz0xL+KImm4gaXMgYSBjb21tb24gcnVsZSBvZiB0aHVtYi4gVGhlIHJlc3VsdGluZyBtb2RlbCBpcyByb2J1c3QgdG8g4omkKDEvQ24pIGZyYWN0aW9uIG9mIHRyYWluaW5nIG91dGxpZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IHJvY19hdWNfc2NvcmVcblxuZGVmIHNvZnRfc3ZkZF9sb3NzKG1vZGVsLCB4LCBjZW50ZXIsIFIsIEM9MC4xKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdTb2Z0LWJvdW5kYXJ5IFNWREQ6IG9wdGltaXNlIFIgam9pbnRseSB3aXRoIG5ldHdvcmsgd2VpZ2h0cy5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICB6ID0gbW9kZWwoeClcbiAgICBkaXN0cyA9ICgoeiAtIGNlbnRlcikgKiogMikuc3VtKGRpbT0tMSlcbiAgICB2aW9sYXRpb25zID0gdG9yY2guY2xhbXAoZGlzdHMgLSBSICoqIDIsIG1pbj0wLjApXG4gICAgcmV0dXJuIFIgKiogMiArIEMgKiB2aW9sYXRpb25zLm1lYW4oKVxuXG5ucC5yYW5kb20uc2VlZCg0KTsgdG9yY2gubWFudWFsX3NlZWQoNClcbiMgQ29udGFtaW5hdGVkIHRyYWluaW5nIHNldDogNSUgYW5vbWFsaWVzIG1peGVkIGluXG5YX2NsZWFuID0gdG9yY2gudGVuc29yKG5wLnJhbmRvbS5yYW5kbig1NzAsIDIwKSwgZHR5cGU9dG9yY2guZmxvYXQzMilcblhfY29udGFtID0gdG9yY2gudGVuc29yKG5wLnJhbmRvbS5yYW5kbigzMCwgMjApICogMC4xICsgNCwgZHR5cGU9dG9yY2guZmxvYXQzMilcblhfbWl4ZWQgPSB0b3JjaC5jYXQoW1hfY2xlYW4sIFhfY29udGFtXSlcblxuc3ZkZF9zb2Z0ID0gRGVlcFNWREQoZF9pbj0yMCwgZF9sYXQ9MTYpXG5jX3NvZnQgPSBpbml0X2NlbnRlcihzdmRkX3NvZnQsIFhfY2xlYW4pXG5SX3BhcmFtID0gdG9yY2gubm4uUGFyYW1ldGVyKHRvcmNoLnRlbnNvcigxLjApKVxub3B0X3NvZnQgPSB0b3JjaC5vcHRpbS5BZGFtKFxuICAgIGxpc3Qoc3ZkZF9zb2Z0LnBhcmFtZXRlcnMoKSkgKyBbUl9wYXJhbV0sIGxyPTVlLTQpXG5mb3IgZXAgaW4gcmFuZ2UoNDApOlxuICAgIGxvc3NfcyA9IHNvZnRfc3ZkZF9sb3NzKHN2ZGRfc29mdCwgWF9taXhlZCwgY19zb2Z0LCBSX3BhcmFtKVxuICAgIG9wdF9zb2Z0Lnplcm9fZ3JhZCgpOyBsb3NzX3MuYmFja3dhcmQoKTsgb3B0X3NvZnQuc3RlcCgpXG4gICAgaWYgKGVwKzEpICUgMTAgPT0gMDpcbiAgICAgICAgcHJpbnQoZlx1MDAyN0Vwb2NoIHtlcCsxOjJkfSB8IGxvc3M9e2xvc3Nfcy5pdGVtKCk6LjZmfSAgUj17Ul9wYXJhbS5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNldCBDPTEvc3FydChuKSBhcyB0aGUgaW5pdGlhbCBjb250YW1pbmF0aW9uIHRvbGVyYW5jZSBoeXBlcnBhcmFtZXRlcjsgdHVuZSB1cCBpZiBmYWxzZS1hbGFybSByYXRlIGlzIHRvbyBoaWdoLiIsIkluaXRpYWxpc2UgUiBhcyB0aGUgbWVkaWFuIGRpc3RhbmNlIGZyb20gY2VudGVyIG9uIHRyYWluaW5nIGRhdGEg4oCUIGF2b2lkcyBzdGFydGluZyB3aXRoIFI9MCAoY29sbGFwc2VzIGFsbCBwb2ludHMpLiIsIk1vbml0b3IgUiBkdXJpbmcgdHJhaW5pbmc6IGlmIFIgZ3Jvd3MgdW5ib3VuZGVkbHksIGluY3JlYXNlIEMgb3IgcmVkdWNlIGxlYXJuaW5nIHJhdGUuIiwiSGFyZC1ib3VuZGFyeSBTVkREIGlzIGEgc3BlY2lhbCBjYXNlIG9mIHNvZnQtYm91bmRhcnkgd2l0aCBD4oaS4oieIGFuZCBSIGZpeGVkIOKAlCB1c2VmdWwgd2hlbiB0cmFpbmluZyBkYXRhIGlzIGNsZWFuLiIsIlRoZSBmcmFjdGlvbiBvZiB0cmFpbmluZyBzYW1wbGVzIG91dHNpZGUgdGhlIHNwaGVyZSB1cHBlci1ib3VuZHMgdGhlIGNvbnRhbWluYXRpb24gcmF0ZTogdXNlIHRoaXMgYXMgYSBzYW5pdHkgY2hlY2suIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWZ0ZXIgdHJhaW5pbmcgc29mdC1ib3VuZGFyeSBTVkRELCB0aGUgYW5vbWFseSBzY29yZSByZW1haW5zIOKAls+GKHgp4oiSY+KAlsKyIOKAlCB0aGUgcmFkaXVzIFIgYWZmZWN0cyB0cmFpbmluZyBidXQgbm90IGluZmVyZW5jZSBzY29yaW5nLiBUaGlzIG1lYW5zIHRoZSBzYW1lIHRocmVzaG9sZC1zZXR0aW5nIHByb2NlZHVyZSBhcHBsaWVzOiBjb21wdXRlIHNjb3JlcyBvbiBjbGVhbiB2YWxpZGF0aW9uIGRhdGEgYW5kIGZsYWcgdGVzdCBwb2ludHMgYWJvdmUgdGhlICgx4oiSzrEpIHF1YW50aWxlLiBUaGUgc29mdC1ib3VuZGFyeSBtb2RlbCBzaW1wbHkgcGxhY2VzIHRoZSBkZWNpc2lvbiBib3VuZGFyeSBtb3JlIHJvYnVzdGx5IHdoZW4gb3V0bGllcnMgYXJlIHByZXNlbnQgZHVyaW5nIHRyYWluaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gd2l0aCBSZWxhdGVkIE1ldGhvZHMifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiRmVhdHVyZSBMZWFybmluZyIsIkJvdW5kYXJ5IFR5cGUiLCJBbm9tYWx5IFNjb3JlIiwiQ29sbGFwc2UgUmlzayIsIlBlcmZvcm1hbmNlIl0sInJvd3MiOltbIkRlZXAgU1ZERCIsIlllcyDigJQgam9pbnQgZW5jb2RlciIsIkh5cGVyc3BoZXJlIiwi4oCWz4YoeCniiJJj4oCWwrIiLCJZZXMg4oCUIG5lZWRzIGNhcmVmdWwgZGVzaWduIiwiR29vZCB3aXRoIHByZXRyYWluaW5nIl0sWyJPQy1TVk0iLCJObyDigJQgZml4ZWQga2VybmVsIiwiS2VybmVsIGh5cGVycGxhbmUiLCJTaWduZWQgbWFyZ2luIGRpc3RhbmNlIiwiTm8iLCJNb2RlcmF0ZSwgcG9vciBzY2FsaW5nIl0sWyJBRSBSZWNvbnN0cnVjdGlvbiIsIlllcyDigJQgYXV0b2VuY29kZXIiLCJJbXBsaWNpdCB2aWEgcmVjb24gZXJyb3IiLCLigJZ44oiSeMyC4oCWwrIiLCJObyIsIkdvb2QgYmFzZWxpbmUsIGZsZXhpYmxlIl0sWyJEZWVwIFNWREQgKyBBRSBwcmV0cmFpbiIsIlllcyDigJQgdHdvIHBoYXNlcyIsIkh5cGVyc3BoZXJlIiwi4oCWz4YoeCniiJJj4oCWwrIiLCJSZWR1Y2VkIiwiQmVzdCBvdmVyYWxsIl0sWyJJc29sYXRpb24gRm9yZXN0IiwiTm8iLCJQYXJ0aXRpb24gdHJlZSIsIk1lYW4gcGF0aCBsZW5ndGgiLCJObyIsIkZhc3QsIGNvbXBldGl0aXZlIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF1dG9lbmNvZGVyIHByZXRyYWluaW5nIGZvbGxvd2VkIGJ5IFNWREQgZmluZS10dW5pbmcgY29uc2lzdGVudGx5IG91dHBlcmZvcm1zIGVpdGhlciBtZXRob2QgYWxvbmUuIFRoZSBhdXRvZW5jb2RlciBnaXZlcyB0aGUgZW5jb2RlciBhIG1lYW5pbmdmdWwgaW5pdGlhbGlzYXRpb24gdGhhdCBhdm9pZHMgY29sbGFwc2U7IHRoZSBTVkREIG9iamVjdGl2ZSB0aGVuIGNvbXByZXNzZXMgdGhlIG5vcm1hbCBjbGFzcyByZXByZXNlbnRhdGlvbiBpbnRvIGEgdGlnaHQgaHlwZXJzcGhlcmUuIFVzZSB0aGUgc29mdC1ib3VuZGFyeSB2YXJpYW50IHdoZW4gdGhlIHRyYWluaW5nIHNldCBtYXkgYmUgY29udGFtaW5hdGVkLCBhbmQgdHVuZSBDIHVzaW5nIGEgc21hbGwgbGFiZWxsZWQgdmFsaWRhdGlvbiBzZXQgaWYgYXZhaWxhYmxlLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Deep SVDD — Deep One-Class Classification

Deep SVDD (Ruff et al., 2018) extends the classical Support Vector Data Description to deep networks. The idea is elegant: train a neural network φ(x;W) to map all normal training data to a compact hypersphere with center c in the latent space. At test time, points that map far from c are anomalies. Unlike autoencoders that detect anomalies via reconstruction error, Deep SVDD detects anomalies by their distance from the learned normal manifold in representation space.

## From SVDD to Deep SVDD

Classical SVDD fits the minimum-volume hypersphere containing all training data in kernel feature space, with soft-boundary variant using slack variables. The kernel version is equivalent to one-class SVM. The limitation: the kernel is fixed and the representation is not learned from data. Deep SVDD addresses this by jointly optimising the mapping φ and the center c: min_{W,c} (1/n) Σᵢ ‖φ(xᵢ;W) − c‖². The network learns a representation where normal data is compact; anomalies, having a different structure, map to distant regions.

- Objective: minimise squared distances from latent codes to center c — forces normal data into a tight cluster.
- Center c: initialised as the mean of a forward pass on all training data; then fixed during training to prevent trivial solutions.
- Anomaly score: ‖φ(x;W)−c‖² — larger distance from center indicates higher anomaly likelihood.
- Collapse prevention: removing bias terms in the last layer and bounded activations prevents the network from mapping everything to c.
- Soft-boundary variant: add hypersphere radius R as a variable with penalty C·Σ max(0,‖φ(xᵢ)−c‖²−R²).

```python
import torch
import torch.nn as nn
import numpy as np

class DeepSVDD(nn.Module):
    def __init__(self, d_in, d_lat=16):
        super().__init__()
        # No bias in final layer; no bounded activations — prevents collapse
        self.net = nn.Sequential(
            nn.Linear(d_in, 64, bias=True),  nn.ReLU(),
            nn.Linear(64, 32, bias=True),    nn.ReLU(),
            nn.Linear(32, d_lat, bias=False)  # no bias here
        )

    def forward(self, x):
        return self.net(x)

def init_center(model, X_train, eps=0.1):
    '''Center = mean of encoder outputs on training data.'''
    model.eval()
    with torch.no_grad():
        z = model(X_train)
    c = z.mean(dim=0)
    # Avoid near-zero center (would make collapse easier)
    c[(c.abs() < eps) & (c >= 0)] =  eps
    c[(c.abs() < eps) & (c < 0)]  = -eps
    return c.detach()

def svdd_loss(model, x, center):
    z = model(x)
    return ((z - center) ** 2).sum(dim=-1).mean()

torch.manual_seed(0); np.random.seed(0)
X_tr = torch.tensor(np.random.randn(600, 20), dtype=torch.float32)
svdd = DeepSVDD(d_in=20, d_lat=16)
center = init_center(svdd, X_tr)
opt = torch.optim.Adam(svdd.parameters(), lr=1e-3)
svdd.train()
for ep in range(30):
    loss = svdd_loss(svdd, X_tr, center)
    opt.zero_grad(); loss.backward(); opt.step()
    if (ep+1) % 10 == 0:
        print(f'Epoch {ep+1:2d} | SVDD loss: {loss.item():.6f}')
```

## Hypersphere Objective and Center Initialization

The center c is computed as the mean of φ(xᵢ;W) on all training data using a forward pass before optimisation begins, then held fixed. This two-phase approach prevents the network from trivially satisfying the objective by rotating to place c at the origin. The objective min ‖φ(x)−c‖² is a form of deep clustering with a single centroid — related to k-means with k=1. The training dynamics pull all representations toward c: the network must learn a compact representation of the normal class to minimise the objective.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score

np.random.seed(1); torch.manual_seed(1)
# One-class classification: class 0 = normal, everything else = anomaly
X_norm = torch.tensor(np.random.randn(400, 20), dtype=torch.float32)
X_anom = torch.tensor(np.random.randn(80, 20) * 0.3 + 3, dtype=torch.float32)

svdd2 = DeepSVDD(d_in=20, d_lat=16)
c2 = init_center(svdd2, X_norm)
opt2 = torch.optim.Adam(svdd2.parameters(), lr=5e-4)
svdd2.train()
for ep in range(50):
    loss2 = svdd_loss(svdd2, X_norm, c2)
    opt2.zero_grad(); loss2.backward(); opt2.step()

svdd2.eval()
X_all = torch.cat([X_norm[:100], X_anom])
y_all = np.array([0]*100 + [1]*80)
with torch.no_grad():
    z_all = svdd2(X_all)
    scores = ((z_all - c2) ** 2).sum(dim=-1).numpy()
auroc = roc_auc_score(y_all, scores)
print(f'Deep SVDD AUROC: {auroc:.4f}')
print(f'Normal mean distance from center: {scores[:100].mean():.4f}')
print(f'Anomaly mean distance from center: {scores[100:].mean():.4f}')
```

## Collapse Prevention and Training Tricks

The hypersphere collapse problem occurs when the network maps everything to the center c by setting all weights to zero (trivial solution). Two architectural tricks prevent this: (1) Remove bias terms in the penultimate and final layers — the bias could shift representations to coincide with c regardless of input. (2) Avoid bounded activations like sigmoid or tanh in the network — they can saturate and produce a constant output. Batch normalisation can also cause collapse if the normalised mean equals c. Use layer normalisation or avoid normalisation in the last layer.

> **Collapse Risk**: If your Deep SVDD loss goes to zero very quickly (within 5 epochs), suspect collapse. Diagnose by checking if all training embeddings are identical (std ≈ 0). Fix: (1) remove bias in the last linear layer, (2) replace sigmoid/tanh with ReLU, (3) disable batch norm in the final block. Also check that the center c is not near zero — a near-zero center makes collapse easier.

```python
import torch
import torch.nn as nn
import numpy as np

class Autoencoder(nn.Module):
    def __init__(self, d_in, d_lat=16):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(d_in, 64), nn.ReLU(),
            nn.Linear(64, 32), nn.ReLU(),
            nn.Linear(32, d_lat))
        self.decoder = nn.Sequential(
            nn.Linear(d_lat, 32), nn.ReLU(),
            nn.Linear(32, 64), nn.ReLU(),
            nn.Linear(64, d_in))
    def forward(self, x):
        return self.decoder(self.encoder(x))

np.random.seed(2); torch.manual_seed(2)
X_tr_ae = torch.tensor(np.random.randn(500, 20), dtype=torch.float32)
ae = Autoencoder(d_in=20, d_lat=16)
opt_ae = torch.optim.Adam(ae.parameters(), lr=1e-3)
for ep in range(30):
    loss_ae = nn.functional.mse_loss(ae(X_tr_ae), X_tr_ae)
    opt_ae.zero_grad(); loss_ae.backward(); opt_ae.step()
    if (ep+1) % 10 == 0:
        print(f'AE pretrain epoch {ep+1:2d} | recon loss: {loss_ae.item():.6f}')
# Transfer encoder weights to Deep SVDD
svdd3 = DeepSVDD(d_in=20, d_lat=16)
with torch.no_grad():
    for (n1, p1), (n2, p2) in zip(
            ae.encoder.named_parameters(),
            svdd3.net.named_parameters()):
        if p1.shape == p2.shape:
            p2.copy_(p1)
print('Encoder weights transferred to SVDD network.')
```

Pretraining with an autoencoder gives the SVDD encoder a head start: the encoder already knows how to represent the normal data manifold before the hypersphere objective begins pulling representations toward c. Without pretraining, the random initialisation means the center c is initialised in an arbitrary region of the embedding space, and the SVDD objective may collapse or converge to a poor local minimum. With pretraining, the center initialisation (mean of encoder outputs) lands near the true data mean in a meaningful representation space, significantly improving final detection performance.

## Soft-Boundary Deep SVDD

The hard-boundary variant minimises the mean squared distance to c, implicitly assuming all training data is normal. If training data is contaminated by a small fraction of anomalies, a soft-boundary formulation is more robust: min_{W,R,c} R² + C·(1/n)Σ max(0, ‖φ(xᵢ)−c‖²−R²). The radius R acts as a slack threshold: points outside the sphere of radius R incur a penalty scaled by C. Setting C=1/√n is a common rule of thumb. The resulting model is robust to ≤(1/Cn) fraction of training outliers.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score

def soft_svdd_loss(model, x, center, R, C=0.1):
    '''Soft-boundary SVDD: optimise R jointly with network weights.'''
    z = model(x)
    dists = ((z - center) ** 2).sum(dim=-1)
    violations = torch.clamp(dists - R ** 2, min=0.0)
    return R ** 2 + C * violations.mean()

np.random.seed(4); torch.manual_seed(4)
# Contaminated training set: 5% anomalies mixed in
X_clean = torch.tensor(np.random.randn(570, 20), dtype=torch.float32)
X_contam = torch.tensor(np.random.randn(30, 20) * 0.1 + 4, dtype=torch.float32)
X_mixed = torch.cat([X_clean, X_contam])

svdd_soft = DeepSVDD(d_in=20, d_lat=16)
c_soft = init_center(svdd_soft, X_clean)
R_param = torch.nn.Parameter(torch.tensor(1.0))
opt_soft = torch.optim.Adam(
    list(svdd_soft.parameters()) + [R_param], lr=5e-4)
for ep in range(40):
    loss_s = soft_svdd_loss(svdd_soft, X_mixed, c_soft, R_param)
    opt_soft.zero_grad(); loss_s.backward(); opt_soft.step()
    if (ep+1) % 10 == 0:
        print(f'Epoch {ep+1:2d} | loss={loss_s.item():.6f}  R={R_param.item():.4f}')
```

- Set C=1/sqrt(n) as the initial contamination tolerance hyperparameter; tune up if false-alarm rate is too high.
- Initialise R as the median distance from center on training data — avoids starting with R=0 (collapses all points).
- Monitor R during training: if R grows unboundedly, increase C or reduce learning rate.
- Hard-boundary SVDD is a special case of soft-boundary with C→∞ and R fixed — useful when training data is clean.
- The fraction of training samples outside the sphere upper-bounds the contamination rate: use this as a sanity check.

After training soft-boundary SVDD, the anomaly score remains ‖φ(x)−c‖² — the radius R affects training but not inference scoring. This means the same threshold-setting procedure applies: compute scores on clean validation data and flag test points above the (1−α) quantile. The soft-boundary model simply places the decision boundary more robustly when outliers are present during training.

## Comparison with Related Methods

| Method | Feature Learning | Boundary Type | Anomaly Score | Collapse Risk | Performance |
| --- | --- | --- | --- | --- | --- |
| Deep SVDD | Yes — joint encoder | Hypersphere | ‖φ(x)−c‖² | Yes — needs careful design | Good with pretraining |
| OC-SVM | No — fixed kernel | Kernel hyperplane | Signed margin distance | No | Moderate, poor scaling |
| AE Reconstruction | Yes — autoencoder | Implicit via recon error | ‖x−x̂‖² | No | Good baseline, flexible |
| Deep SVDD + AE pretrain | Yes — two phases | Hypersphere | ‖φ(x)−c‖² | Reduced | Best overall |
| Isolation Forest | No | Partition tree | Mean path length | No | Fast, competitive |

Autoencoder pretraining followed by SVDD fine-tuning consistently outperforms either method alone. The autoencoder gives the encoder a meaningful initialisation that avoids collapse; the SVDD objective then compresses the normal class representation into a tight hypersphere. Use the soft-boundary variant when the training set may be contaminated, and tune C using a small labelled validation set if available.

---

