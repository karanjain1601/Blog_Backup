---
title: "Feed-Forward Sublayer — Position-Wise MLP in Transformers"
slug: "feed-forward-sublayer"
description: "The position-wise FFN sub-layer: dimensions, parameter budget, the FFN-as-associative-memory interpretation, and the activation function evolution from ReLU to SwiGLU."
tags: ["deep-learning", "transformers"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXZlcnkgVHJhbnNmb3JtZXIgYmxvY2sgY29udGFpbnMgdHdvIHN1Yi1sYXllcnM6IG11bHRpLWhlYWQgYXR0ZW50aW9uIGFuZCBhIHBvc2l0aW9uLXdpc2UgZmVlZC1mb3J3YXJkIG5ldHdvcmsgKEZGTikuIFdoaWxlIGF0dGVudGlvbiBtaXhlcyBpbmZvcm1hdGlvbiBhY3Jvc3MgdG9rZW4gcG9zaXRpb25zLCB0aGUgRkZOIHByb2Nlc3NlcyBlYWNoIHBvc2l0aW9uIGluZGVwZW5kZW50bHkgd2l0aCB0aGUgc2FtZSB0d28tbGF5ZXIgTUxQIGFwcGxpZWQgaWRlbnRpY2FsbHkgdG8gYWxsIHBvc2l0aW9ucy4gRGVzcGl0ZSBpdHMgc2ltcGxpY2l0eSwgdGhlIEZGTiB0eXBpY2FsbHkgYWNjb3VudHMgZm9yIHR3by10aGlyZHMgb2YgYSBsYXJnZSBUcmFuc2Zvcm1lclx1MDAyN3MgcGFyYW1ldGVycyBhbmQgYSBzdWJzdGFudGlhbCBmcmFjdGlvbiBvZiBpdHMgaW5mZXJlbmNlIGNvbXB1dGUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUG9zaXRpb24tV2lzZSBGRk4g4oCUIFNhbWUgTUxQIGF0IEV2ZXJ5IFBvc2l0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc3RhbmRhcmQgRkZOIGlzIGRlZmluZWQgYXMgRkZOKHgpID0gQWN0aXZhdGlvbih4IFfigoEgKyBi4oKBKSBX4oKCICsgYuKCgi4gSGVyZSB4IGhhcyBzaGFwZSAoQiwgTCwgZF9tb2RlbCksIGFuZCB0aGUgRkZOIGlzIGFwcGxpZWQgaWRlbnRpY2FsbHkgYXQgZXZlcnkgdG9rZW4gcG9zaXRpb24g4oCUIHRoZSBNTFAgd2VpZ2h0cyBhcmUgc2hhcmVkIGFjcm9zcyBwb3NpdGlvbnMsIG5vdCBhY3Jvc3MgbGF5ZXJzLiBUaGUgaW5uZXIgZGltZW5zaW9uIGRfZmYgaXMgdHlwaWNhbGx5IHNldCB0byA0IMOXIGRfbW9kZWwsIGdpdmluZyBhIGJvdHRsZW5lY2sgc3RydWN0dXJlOiB0aGUgaGlkZGVuIHN0YXRlIGV4cGFuZHMgZnJvbSBkX21vZGVsIHRvIGRfZmYsIHBhc3NlcyB0aHJvdWdoIHRoZSBub24tbGluZWFyaXR5LCB0aGVuIGNvbnRyYWN0cyBiYWNrIHRvIGRfbW9kZWwuIFRoaXMgNMOXIHJhdGlvIGlzIGFuIGVtcGlyaWNhbCBjaG9pY2UgZnJvbSBWYXN3YW5pIDIwMTcgdGhhdCBoYXMgcmVtYWluZWQgc3VycHJpc2luZ2x5IGR1cmFibGUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJkX21vZGVsID0gNTEyIOKGkiBkX2ZmID0gMjA0OCAoNMOXKSDigJQgc3RhbmRhcmQgVHJhbnNmb3JtZXIgb3JpZ2luYWwiLCJkX21vZGVsID0gNzY4IOKGkiBkX2ZmID0gMzA3MiAoNMOXKSDigJQgQkVSVC1iYXNlIiwiZF9tb2RlbCA9IDEwMjQg4oaSIGRfZmYgPSA0MDk2ICg0w5cpIOKAlCBCRVJULWxhcmdlLCBHUFQtMiBtZWRpdW0iLCJQYXJhbWV0ZXIgY291bnQ6IFfigoEgaXMgZF9tb2RlbCDDlyBkX2ZmLCBX4oKCIGlzIGRfZmYgw5cgZF9tb2RlbCDihpIgMiDCtyBkX21vZGVsIMK3IGRfZmYgdG90YWwiLCJGb3IgZF9tb2RlbD01MTIsIGRfZmY9MjA0ODogRkZOIGhhcyAyLDA5NywxNTIgcGFyYW1zIHZzIH43ODYsNDMyIGZvciBhdHRlbnRpb24iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJGRk4gUGFyYW1ldGVycyBEb21pbmF0ZSBpbiBMYXJnZSBNb2RlbHMiLCJjb250ZW50IjoiSW4gYSBzdGFuZGFyZCBUcmFuc2Zvcm1lciB3aXRoIGRfbW9kZWw9NTEyIGFuZCBkX2ZmPTIwNDgsIGVhY2ggRkZOIGJsb2NrIGhhcyB+Mk0gcGFyYW1ldGVycyB3aGlsZSBlYWNoIGF0dGVudGlvbiBibG9jayBoYXMgfjc4NksgcGFyYW1ldGVycyDigJQgYWJvdXQgMi43w5cgbW9yZSBpbiB0aGUgRkZOLiBBY3Jvc3MgYWxsIGxheWVycywgdGhlIEZGTiBhY2NvdW50cyBmb3Igcm91Z2hseSB0d28tdGhpcmRzIG9mIHRvdGFsIG5vbi1lbWJlZGRpbmcgcGFyYW1ldGVycy4gVGhpcyByYXRpbyB3b3JzZW5zIGFzIG1vZGVscyBncm93OiBHUFQtM1x1MDAyN3MgMTc1QiBwYXJhbWV0ZXJzIGFyZSBwcmVkb21pbmFudGx5IGluIEZGTiBsYXllcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRkZOIGFzIEFzc29jaWF0aXZlIE1lbW9yeSAoR2V2YSBldCBhbC4gMjAyMSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdldmEgZXQgYWwuICgyMDIxKSBwcm9wb3NlZCBhIGNvbXBlbGxpbmcgaW50ZXJwcmV0YXRpb246IHRoZSByb3dzIG9mIFfigoEgYWN0IGFzIFx1MDAyN2tleXNcdTAwMjcgYW5kIHRoZSByb3dzIG9mIFfigoLhtYAgYWN0IGFzIFx1MDAyN3ZhbHVlc1x1MDAyNy4gVGhlIGlucHV0IHggaXMgY29tcGFyZWQgYWdhaW5zdCBhbGwga2V5cyB2aWEgdGhlIGxpbmVhciBwcm9qZWN0aW9uIHhX4oKBOyBwb3NpdGlvbnMgd2l0aCBoaWdoIGRvdC1wcm9kdWN0IGFjdGl2YXRlIGFmdGVyIHRoZSBSZUxVIChvciBHRUxVKSBub24tbGluZWFyaXR5LiBUaGUgYWN0aXZhdGVkIGhpZGRlbiB1bml0cyB0aGVuIHNlbGVjdCBjb3JyZXNwb25kaW5nIHZhbHVlIHZlY3RvcnMgZnJvbSBX4oKCLCBibGVuZGluZyB0aGVtIGludG8gdGhlIG91dHB1dC4gVGhpcyBpcyBhIGNvbnRpbnVvdXMsIHNvZnQga2V5LXZhbHVlIGxvb2t1cCDigJQgdGhlIEZGTiByZXRyaWV2ZXMgZmFjdHVhbCBhc3NvY2lhdGlvbnMgKGUuZy4sIGNhcGl0YWwgY2l0aWVzLCBjb21tb24gY29sbG9jYXRpb25zKSBzdG9yZWQgaW4gaXRzIHdlaWdodHMgZHVyaW5nIHByZXRyYWluaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFjdGl2YXRpb24gRnVuY3Rpb25zIOKAlCBGcm9tIFJlTFUgdG8gU3dpR0xVIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgb3JpZ2luYWwgVHJhbnNmb3JtZXIgdXNlZCBSZUxVLiBHUFQtMiBzd2l0Y2hlZCB0byBHRUxVLCB3aGljaCBpcyBzbW9vdGhlciBhbmQgYXZvaWRzIHRoZSBkZWFkLW5ldXJvbiBwcm9ibGVtIG9mIFJlTFUuIE1vcmUgcmVjZW50bHksIGdhdGVkIHZhcmlhbnRzIChTd2lHTFUsIEdFR0xVLCBSZUdMVSkgaGF2ZSBiZWNvbWUgc3RhbmRhcmQgaW4gZnJvbnRpZXIgTExNcy4gVGhlc2UgdXNlIHRocmVlIG1hdHJpY2VzIGluc3RlYWQgb2YgdHdvLCB3aGVyZSBvbmUgYnJhbmNoIGFjdHMgYXMgYSBtdWx0aXBsaWNhdGl2ZSBnYXRlIGNvbnRyb2xsaW5nIGluZm9ybWF0aW9uIGZsb3cuIFNoYXplZXIgKDIwMjApIHNob3dlZCB0aGF0IGdhdGVkIHZhcmlhbnRzIGNvbnNpc3RlbnRseSBvdXRwZXJmb3JtIFJlTFUgYW5kIEdFTFUgYXQgdGhlIHNhbWUgcGFyYW1ldGVyIGFuZCBjb21wdXRlIGJ1ZGdldC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIEZGTiBCbG9jayBmcm9tIFNjcmF0Y2gifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgY2xlYW4gcG9zaXRpb24td2lzZSBGRk4gaW1wbGVtZW50YXRpb24gd2l0aCBjb25maWd1cmFibGUgYWN0aXZhdGlvbiwgc2hvd2luZyBob3cgRkZOIHBhcmFtZXRlciBjb3VudCBjb21wYXJlcyB0byBhdHRlbnRpb24gcGFyYW1ldGVyIGNvdW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBGZWVkRm9yd2FyZEJsb2NrKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiUG9zaXRpb24td2lzZSBGRk46IEZGTih4KSA9IERyb3BvdXQoQWN0KHggVzEgKyBiMSkgVzIgKyBiMikuXG4gICAgU2FtZSBNTFAgYXBwbGllZCBpbmRlcGVuZGVudGx5IHRvIGV2ZXJ5IHRva2VuIHBvc2l0aW9uLlxuICAgIGRfZmYgZGVmYXVsdHMgdG8gNCAqIGRfbW9kZWwgKHRoZSBzdGFuZGFyZCByYXRpbyBmcm9tIFZhc3dhbmkgMjAxNykuXG4gICAgXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgZF9mZjogaW50ID0gTm9uZSxcbiAgICAgICAgICAgICAgICAgZHJvcG91dDogZmxvYXQgPSAwLjEsIGFjdGl2YXRpb246IHN0ciA9IFx1MDAyN2dlbHVcdTAwMjcpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgZF9mZiAgICAgICA9IGRfZmYgb3IgNCAqIGRfbW9kZWxcbiAgICAgICAgc2VsZi5mYzEgICA9IG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKVxuICAgICAgICBzZWxmLmZjMiAgID0gbm4uTGluZWFyKGRfZmYsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYuZHJvcCAgPSBubi5Ecm9wb3V0KGRyb3BvdXQpXG4gICAgICAgIHNlbGYuYWN0ICAgPSB7XHUwMDI3cmVsdVx1MDAyNzogRi5yZWx1LCBcdTAwMjdnZWx1XHUwMDI3OiBGLmdlbHV9W2FjdGl2YXRpb25dXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICByZXR1cm4gc2VsZi5mYzIoc2VsZi5kcm9wKHNlbGYuYWN0KHNlbGYuZmMxKHgpKSkpXG5cbiMgQ29tcGFyZSBwYXJhbWV0ZXIgY291bnRzOiBGRk4gdnMgYXR0ZW50aW9uXG5kX21vZGVsLCBkX2ZmID0gNTEyLCAyMDQ4XG5mZm4gICA9IEZlZWRGb3J3YXJkQmxvY2soZF9tb2RlbCwgZF9mZilcbmF0dG4gID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRfbW9kZWwsIG51bV9oZWFkcz04LCBiYXRjaF9maXJzdD1UcnVlKVxucF9mZm4gID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBmZm4ucGFyYW1ldGVycygpKVxucF9hdHRuID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBhdHRuLnBhcmFtZXRlcnMoKSlcbnByaW50KGZcdTAwMjdkX21vZGVsPXtkX21vZGVsfSwgZF9mZj17ZF9mZn1cdTAwMjcpXG5wcmludChmXHUwMDI3RkZOIHBhcmFtczogIHtwX2ZmbjosfSAgKHtwX2Zmbi8ocF9mZm4rcF9hdHRuKSoxMDA6LjFmfSUgb2YgRkZOK0F0dG4pXHUwMDI3KVxucHJpbnQoZlx1MDAyN0F0dG4gcGFyYW1zOiB7cF9hdHRuOix9ICh7cF9hdHRuLyhwX2ZmbitwX2F0dG4pKjEwMDouMWZ9JSBvZiBGRk4rQXR0bilcdTAwMjcpXG54ICAgPSB0b3JjaC5yYW5kbigyLCAxMCwgZF9tb2RlbClcbm91dCA9IGZmbih4KVxucHJpbnQoZlx1MDAyN091dHB1dCBzaGFwZToge291dC5zaGFwZX0gIChwb3NpdGlvbi13aXNlOiBzYW1lIGFzIGlucHV0KVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIEdhdGVkIEZGTiAoU3dpR0xVIFZhcmlhbnQpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTd2lHTFUgdXNlcyB0aHJlZSB3ZWlnaHQgbWF0cmljZXM6IGEgZ2F0ZSBicmFuY2ggKFfigoEsIHRocm91Z2ggU2lMVSksIGEgdmFsdWUgYnJhbmNoIChX4oKCLCBsaW5lYXIpLCBhbmQgYSBkb3duLXByb2plY3Rpb24gKFfigoMpLiBUaGUgaGlkZGVuIGRpbWVuc2lvbiBpcyByZWR1Y2VkIHRvIDIvMyBvZiB0aGUgc3RhbmRhcmQgZF9mZiB0byBrZWVwIHBhcmFtZXRlciBjb3VudHMgZXF1aXZhbGVudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgU3dpR0xVRkZOKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiU3dpR0xVIChTaGF6ZWVyIDIwMjApOiBGRk4oeCkgPSAoU2lMVSh4IFcxKSAqIHggVzIpIFczLlxuICAgIFRocmVlIG1hdHJpY2VzOyBkX2ZmIGFkanVzdGVkIHRvIDIvMyBvZiBzdGFuZGFyZCB0byBtYXRjaCBwYXJhbSBjb3VudC5cbiAgICBTaUxVKHgpID0geCAqIHNpZ21vaWQoeCkgIChhbHNvIGNhbGxlZCBTd2lzaCkuXG4gICAgVXNlZCBpbjogTExhTUEgMS8yLzMsIE1pc3RyYWwsIFBhTE0sIEdlbW1hLlxuICAgIFwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsOiBpbnQsIGRfZmY6IGludCA9IE5vbmUsIGRyb3BvdXQ6IGZsb2F0ID0gMC4wKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGRfZmYgICAgICAgPSBkX2ZmIG9yIGludCg0ICogZF9tb2RlbCAqIDIgLyAzKVxuICAgICAgICBzZWxmLlcxICAgID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfZmYsIGJpYXM9RmFsc2UpICAgIyBnYXRlXG4gICAgICAgIHNlbGYuVzIgICAgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9mZiwgYmlhcz1GYWxzZSkgICAjIHZhbHVlXG4gICAgICAgIHNlbGYuVzMgICAgPSBubi5MaW5lYXIoZF9mZiwgICBkX21vZGVsLCBiaWFzPUZhbHNlKSAjIGRvd25cbiAgICAgICAgc2VsZi5kcm9wICA9IG5uLkRyb3BvdXQoZHJvcG91dClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIGdhdGUgID0gRi5zaWx1KHNlbGYuVzEoeCkpICAgICAgICMgU2lMVSBnYXRlIGJyYW5jaFxuICAgICAgICB2YWx1ZSA9IHNlbGYuVzIoeCkgICAgICAgICAgICAgICAjIGxpbmVhciB2YWx1ZSBicmFuY2hcbiAgICAgICAgcmV0dXJuIHNlbGYuVzMoc2VsZi5kcm9wKGdhdGUgKiB2YWx1ZSkpXG5cbiMgVmVyaWZ5IHNoYXBlcyBhbmQgcGFyYW1ldGVyIGNvdW50IHZzIHN0YW5kYXJkIEZGTlxuZF9tb2RlbCA9IDUxMlxuc3dpICAgICA9IFN3aUdMVUZGTihkX21vZGVsKVxuc3RkX3AgICA9IDIgKiBkX21vZGVsICogKDQgKiBkX21vZGVsKSAgICMgc3RhbmRhcmQgMi1tYXRyaXggRkZOXG5zd2lfcCAgID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBzd2kucGFyYW1ldGVycygpKVxucHJpbnQoZlx1MDAyN1N0YW5kYXJkIEZGTiBwYXJhbXMgKDIgbWF0cywgZF9mZj17NCpkX21vZGVsfSk6ICB7c3RkX3A6LH1cdTAwMjcpXG5wcmludChmXHUwMDI3U3dpR0xVIEZGTiAgcGFyYW1zICgzIG1hdHMsIGRfZmY9e2ludCg0KmRfbW9kZWwqMi8zKX0pOiB7c3dpX3A6LH1cdTAwMjcpXG5wcmludChmXHUwMDI3UmF0aW86IHtzd2lfcCAvIHN0ZF9wOi4zZn0gICh0YXJnZXQgY2xvc2UgdG8gMS4wMDApXHUwMDI3KVxueCAgID0gdG9yY2gucmFuZG4oMiwgMTAsIGRfbW9kZWwpXG5vdXQgPSBzd2koeClcbnByaW50KGZcdTAwMjdPdXRwdXQgc2hhcGU6IHtvdXQuc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMyDigJQgRkZOIGFzIEFzc29jaWF0aXZlIE1lbW9yeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVtb25zdHJhdGluZyB0aGUgR2V2YSBldCBhbC4gKDIwMjEpIGtleS12YWx1ZSBtZW1vcnkgaW50ZXJwcmV0YXRpb246IGEga25vd24ga2V5IHBhdHRlcm4gc3RvcmVkIGluIFfigoEgcm93IDMgY2F1c2VzIGhpZ2ggYWN0aXZhdGlvbiB0aGVyZSwgYW5kIHRoZSBjb3JyZXNwb25kaW5nIFfigoIgY29sdW1uIGlzIHJldHJpZXZlZCBhcyB0aGUgb3V0cHV0IHZhbHVlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG4jIEdldmEgZXQgYWwuICgyMDIxKTogRkZOIHJvd3Mgb2YgVzEgPSBrZXlzLCBjb2x1bW5zIG9mIFcyID0gdmFsdWVzXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbmRfaW4sIGRfZmYsIGRfb3V0ID0gOCwgMTYsIDhcblxuVzEgPSBubi5MaW5lYXIoZF9pbiwgZF9mZiwgYmlhcz1GYWxzZSkgICAgIyBrZXkgbWF0cml4ICAoZF9mZiB4IGRfaW4gcm93cylcblcyID0gbm4uTGluZWFyKGRfZmYsIGRfb3V0LCBiaWFzPUZhbHNlKSAgICMgdmFsdWUgbWF0cml4XG5cbiMgUGxhbnQgYSBtZW1vcnk6IGtleSAzIC1cdTAwM2UgdmFsdWUgdmVjdG9yXG50YXJnZXRfa2V5ICAgPSB0b3JjaC5yYW5kbihkX2luKVxudGFyZ2V0X3ZhbHVlID0gdG9yY2gucmFuZG4oZF9vdXQpXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBXMS53ZWlnaHRbM10gICAgPSB0YXJnZXRfa2V5ICAgICAgICAgICMgcm93IDMgb2YgVzEgPSB0aGUga2V5XG4gICAgVzIud2VpZ2h0WzosIDNdID0gdGFyZ2V0X3ZhbHVlICAgICAgICMgY29sdW1uIDMgb2YgVzIgPSB0aGUgdmFsdWVcblxuIyBRdWVyeSB3aXRoIHRoZSBwbGFudGVkIGtleSBwYXR0ZXJuXG54X3F1ZXJ5ICAgICA9IHRhcmdldF9rZXkudW5zcXVlZXplKDApICAgICMgKDEsIGRfaW4pXG5hY3RpdmF0aW9ucyA9IEYucmVsdShXMSh4X3F1ZXJ5KSkgICAgICAgICMga2V5IHBhdHRlcm4gYWN0aXZhdGVzIGtleSAzIHN0cm9uZ2x5XG5wcmludChcdTAwMjdBY3RpdmF0aW9ucyAoc2hvdWxkIGJlIGhpZ2hlc3QgYXQgaW5kZXggMyk6XHUwMDI3KVxucHJpbnQoYWN0aXZhdGlvbnMuZGV0YWNoKCkubnVtcHkoKS5yb3VuZCgzKSlcbnByaW50KFx1MDAyN01heCBhY3RpdmF0aW9uIGF0IGluZGV4Olx1MDAyNywgYWN0aXZhdGlvbnMuYXJnbWF4KCkuaXRlbSgpKVxuXG5yZXRyaWV2ZWQgPSBXMihhY3RpdmF0aW9ucylcbnByaW50KFx1MDAyN1xcblJldHJpZXZlZDpcdTAwMjcsIHJldHJpZXZlZC5kZXRhY2goKS5udW1weSgpLnJvdW5kKDMpKVxucHJpbnQoXHUwMDI3VGFyZ2V0OiAgIFx1MDAyNywgdGFyZ2V0X3ZhbHVlLm51bXB5KCkucm91bmQoMykpXG5jb3MgPSBGLmNvc2luZV9zaW1pbGFyaXR5KHJldHJpZXZlZCwgdGFyZ2V0X3ZhbHVlLnVuc3F1ZWV6ZSgwKSlcbnByaW50KGZcdTAwMjdDb3NpbmUgc2ltaWxhcml0eToge2Nvcy5pdGVtKCk6LjRmfSAgKGhpZ2ggPSBzdWNjZXNzZnVsIHJldHJpZXZhbClcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSA0IOKAlCBQcm9maWxpbmcgRkZOIHZzIEF0dGVudGlvbiBDb21wdXRlIEJ1ZGdldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW1waXJpY2FsbHkgdGltaW5nIEZGTiBhbmQgc2VsZi1hdHRlbnRpb24gb24gdGhlIHNhbWUgYmF0Y2ggdG8gcXVhbnRpZnkgdGhlaXIgcmVsYXRpdmUgY29tcHV0ZSBjb3N0cywgc2hvd2luZyB0aGUgRkZOIGRvbWluYXRlcyBhdCBsYXJnZSBkX2ZmLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRpbWVcblxuZGVmIHRpbWVfbW9kdWxlKG1vZHVsZTogbm4uTW9kdWxlLCB4OiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgbl9ydW5zOiBpbnQgPSAxMDAsIGxhYmVsOiBzdHIgPSBcdTAwMjdcdTAwMjcpIC1cdTAwM2UgZmxvYXQ6XG4gICAgbW9kdWxlLmV2YWwoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgXyBpbiByYW5nZSgxMCk6ICAgICAgIyB3YXJtLXVwXG4gICAgICAgICAgICBfID0gbW9kdWxlKHgpXG4gICAgICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgICAgICBmb3IgXyBpbiByYW5nZShuX3J1bnMpOlxuICAgICAgICAgICAgXyA9IG1vZHVsZSh4KVxuICAgICAgICBtcyA9ICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApIC8gbl9ydW5zICogMTAwMFxuICAgIHByaW50KGZcdTAwMjd7bGFiZWw6XHUwMDNjMjh9OiB7bXM6LjNmfSBtcy9wYXNzXHUwMDI3KVxuICAgIHJldHVybiBtc1xuXG5kX21vZGVsLCBuX2hlYWRzLCBkX2ZmID0gNTEyLCA4LCAyMDQ4XG5CLCBMID0gNCwgMTI4XG5cbmZmbiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uTGluZWFyKGRfbW9kZWwsIGRfZmYpLCBubi5HRUxVKCksIG5uLkxpbmVhcihkX2ZmLCBkX21vZGVsKVxuKVxuXG5jbGFzcyBBdHRuV3JhcHBlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkLCBoKTogc3VwZXIoKS5fX2luaXRfXygpOyBzZWxmLmEgPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oZCwgaCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYuYSh4LCB4LCB4KVswXVxuXG54X2ZmbiAgPSB0b3JjaC5yYW5kbihCLCBMLCBkX21vZGVsKVxueF9hdHRuID0gdG9yY2gucmFuZG4oQiwgTCwgZF9tb2RlbClcblxudF9mZm4gID0gdGltZV9tb2R1bGUoZmZuLCB4X2ZmbiwgbGFiZWw9Zlx1MDAyN0ZGTiAoZF9mZj17ZF9mZn0pXHUwMDI3KVxudF9hdHRuID0gdGltZV9tb2R1bGUoQXR0bldyYXBwZXIoZF9tb2RlbCwgbl9oZWFkcyksIHhfYXR0biwgbGFiZWw9XHUwMDI3U2VsZi1BdHRlbnRpb25cdTAwMjcpXG5wcmludChmXHUwMDI3RkZOIC8gQXR0biB0aW1lIHJhdGlvOiB7dF9mZm4vdF9hdHRuOi4yZn14ICAoZF9tb2RlbD17ZF9tb2RlbH0sIEw9e0x9KVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGRk4gVmFyaWFudHMgQ29tcGFyZWQifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmFyaWFudCIsIkFjdGl2YXRpb24iLCJNYXRyaWNlcyIsImRfZmYgUmF0aW8iLCJVc2VkIEluIl0sInJvd3MiOltbIlN0YW5kYXJkIFJlTFUiLCJSZUxVIiwiMiIsIjTDlyBkX21vZGVsIiwiT3JpZ2luYWwgVHJhbnNmb3JtZXIsIGVhcmx5IEJFUlQiXSxbIlN0YW5kYXJkIEdFTFUiLCJHRUxVIiwiMiIsIjTDlyBkX21vZGVsIiwiR1BULTIsIEJFUlQsIFJvQkVSVGEiXSxbIlN3aUdMVSIsIlNpTFUgKFN3aXNoKSBnYXRlIiwiMyIsIn44LzPDlyBkX21vZGVsIiwiTExhTUEgMS8yLzMsIE1pc3RyYWwsIFBhTE0sIEdlbW1hIl0sWyJSZUdMVSIsIlJlTFUgZ2F0ZSIsIjMiLCLiiaQ0w5cgZF9tb2RlbCIsIlJlc2VhcmNoIG1vZGVscyAoU2hhemVlciAyMDIwKSJdLFsiR0VHTFUiLCJHRUxVIGdhdGUiLCIzIiwi4omkNMOXIGRfbW9kZWwiLCJUNSB2YXJpYW50cywgc29tZSBCRVJUIHN1Y2Nlc3NvcnMiXSxbIlNwYXJzZSBNb0UiLCJBbnkgKHBlciBleHBlcnQpIiwiMiBwZXIgZXhwZXJ0IiwiayBhY3RpdmUgb2YgbiBleHBlcnRzIiwiTWl4dHJhbCwgU3dpdGNoIFRyYW5zZm9ybWVyIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBGRk4gc3ViLWxheWVyIGlzIGRlY2VwdGl2ZWx5IHNpbXBsZSBidXQgcGxheXMgYSBjZW50cmFsIHJvbGU6IGl0IHByb3ZpZGVzIHBlci10b2tlbiBub24tbGluZWFyIHRyYW5zZm9ybWF0aW9uIGFmdGVyIGVhY2ggYXR0ZW50aW9uIG9wZXJhdGlvbiwgc3RvcmluZyBmYWN0dWFsIGtub3dsZWRnZSBpbiBpdHMgd2VpZ2h0cyBhbmQgYWN0aW5nIGFzIHRoZSBtb2RlbFx1MDAyN3MgbWVtb3J5LiBUaGUgZXZvbHV0aW9uIGZyb20gUmVMVSB0byBHRUxVIHRvIGdhdGVkIHZhcmlhbnRzIChTd2lHTFUpIHJlcHJlc2VudHMgY29uc2lzdGVudCBlbXBpcmljYWwgd2lucyBhdCB0aGUgc2FtZSBjb21wdXRlIGJ1ZGdldCDigJQgYSByYXJlIGNhc2Ugd2hlcmUgYSBkcm9wLWluIGNoYW5nZSByZWxpYWJseSBpbXByb3ZlcyBxdWFsaXR5IHdpdGhvdXQgaW5jcmVhc2luZyBGTE9Qcy4ifV0="
---
# Feed-Forward Sublayer — Position-Wise MLP in Transformers

Every Transformer block contains two sub-layers: multi-head attention and a position-wise feed-forward network (FFN). While attention mixes information across token positions, the FFN processes each position independently with the same two-layer MLP applied identically to all positions. Despite its simplicity, the FFN typically accounts for two-thirds of a large Transformer's parameters and a substantial fraction of its inference compute.

## Position-Wise FFN — Same MLP at Every Position

The standard FFN is defined as FFN(x) = Activation(x W₁ + b₁) W₂ + b₂. Here x has shape (B, L, d_model), and the FFN is applied identically at every token position — the MLP weights are shared across positions, not across layers. The inner dimension d_ff is typically set to 4 × d_model, giving a bottleneck structure: the hidden state expands from d_model to d_ff, passes through the non-linearity, then contracts back to d_model. This 4× ratio is an empirical choice from Vaswani 2017 that has remained surprisingly durable.

- d_model = 512 → d_ff = 2048 (4×) — standard Transformer original
- d_model = 768 → d_ff = 3072 (4×) — BERT-base
- d_model = 1024 → d_ff = 4096 (4×) — BERT-large, GPT-2 medium
- Parameter count: W₁ is d_model × d_ff, W₂ is d_ff × d_model → 2 · d_model · d_ff total
- For d_model=512, d_ff=2048: FFN has 2,097,152 params vs ~786,432 for attention

> **FFN Parameters Dominate in Large Models**: In a standard Transformer with d_model=512 and d_ff=2048, each FFN block has ~2M parameters while each attention block has ~786K parameters — about 2.7× more in the FFN. Across all layers, the FFN accounts for roughly two-thirds of total non-embedding parameters. This ratio worsens as models grow: GPT-3's 175B parameters are predominantly in FFN layers.

## FFN as Associative Memory (Geva et al. 2021)

Geva et al. (2021) proposed a compelling interpretation: the rows of W₁ act as 'keys' and the rows of W₂ᵀ act as 'values'. The input x is compared against all keys via the linear projection xW₁; positions with high dot-product activate after the ReLU (or GELU) non-linearity. The activated hidden units then select corresponding value vectors from W₂, blending them into the output. This is a continuous, soft key-value lookup — the FFN retrieves factual associations (e.g., capital cities, common collocations) stored in its weights during pretraining.

## Activation Functions — From ReLU to SwiGLU

The original Transformer used ReLU. GPT-2 switched to GELU, which is smoother and avoids the dead-neuron problem of ReLU. More recently, gated variants (SwiGLU, GEGLU, ReGLU) have become standard in frontier LLMs. These use three matrices instead of two, where one branch acts as a multiplicative gate controlling information flow. Shazeer (2020) showed that gated variants consistently outperform ReLU and GELU at the same parameter and compute budget.

## Code 1 — FFN Block from Scratch

A clean position-wise FFN implementation with configurable activation, showing how FFN parameter count compares to attention parameter count.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class FeedForwardBlock(nn.Module):
    """Position-wise FFN: FFN(x) = Dropout(Act(x W1 + b1) W2 + b2).
    Same MLP applied independently to every token position.
    d_ff defaults to 4 * d_model (the standard ratio from Vaswani 2017).
    """
    def __init__(self, d_model: int, d_ff: int = None,
                 dropout: float = 0.1, activation: str = 'gelu'):
        super().__init__()
        d_ff       = d_ff or 4 * d_model
        self.fc1   = nn.Linear(d_model, d_ff)
        self.fc2   = nn.Linear(d_ff, d_model)
        self.drop  = nn.Dropout(dropout)
        self.act   = {'relu': F.relu, 'gelu': F.gelu}[activation]

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.fc2(self.drop(self.act(self.fc1(x))))

# Compare parameter counts: FFN vs attention
d_model, d_ff = 512, 2048
ffn   = FeedForwardBlock(d_model, d_ff)
attn  = nn.MultiheadAttention(d_model, num_heads=8, batch_first=True)
p_ffn  = sum(p.numel() for p in ffn.parameters())
p_attn = sum(p.numel() for p in attn.parameters())
print(f'd_model={d_model}, d_ff={d_ff}')
print(f'FFN params:  {p_ffn:,}  ({p_ffn/(p_ffn+p_attn)*100:.1f}% of FFN+Attn)')
print(f'Attn params: {p_attn:,} ({p_attn/(p_ffn+p_attn)*100:.1f}% of FFN+Attn)')
x   = torch.randn(2, 10, d_model)
out = ffn(x)
print(f'Output shape: {out.shape}  (position-wise: same as input)')
```

## Code 2 — Gated FFN (SwiGLU Variant)

SwiGLU uses three weight matrices: a gate branch (W₁, through SiLU), a value branch (W₂, linear), and a down-projection (W₃). The hidden dimension is reduced to 2/3 of the standard d_ff to keep parameter counts equivalent.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SwiGLUFFN(nn.Module):
    """SwiGLU (Shazeer 2020): FFN(x) = (SiLU(x W1) * x W2) W3.
    Three matrices; d_ff adjusted to 2/3 of standard to match param count.
    SiLU(x) = x * sigmoid(x)  (also called Swish).
    Used in: LLaMA 1/2/3, Mistral, PaLM, Gemma.
    """
    def __init__(self, d_model: int, d_ff: int = None, dropout: float = 0.0):
        super().__init__()
        d_ff       = d_ff or int(4 * d_model * 2 / 3)
        self.W1    = nn.Linear(d_model, d_ff, bias=False)   # gate
        self.W2    = nn.Linear(d_model, d_ff, bias=False)   # value
        self.W3    = nn.Linear(d_ff,   d_model, bias=False) # down
        self.drop  = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        gate  = F.silu(self.W1(x))       # SiLU gate branch
        value = self.W2(x)               # linear value branch
        return self.W3(self.drop(gate * value))

# Verify shapes and parameter count vs standard FFN
d_model = 512
swi     = SwiGLUFFN(d_model)
std_p   = 2 * d_model * (4 * d_model)   # standard 2-matrix FFN
swi_p   = sum(p.numel() for p in swi.parameters())
print(f'Standard FFN params (2 mats, d_ff={4*d_model}):  {std_p:,}')
print(f'SwiGLU FFN  params (3 mats, d_ff={int(4*d_model*2/3)}): {swi_p:,}')
print(f'Ratio: {swi_p / std_p:.3f}  (target close to 1.000)')
x   = torch.randn(2, 10, d_model)
out = swi(x)
print(f'Output shape: {out.shape}')
```

## Code 3 — FFN as Associative Memory

Demonstrating the Geva et al. (2021) key-value memory interpretation: a known key pattern stored in W₁ row 3 causes high activation there, and the corresponding W₂ column is retrieved as the output value.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# Geva et al. (2021): FFN rows of W1 = keys, columns of W2 = values
torch.manual_seed(42)
d_in, d_ff, d_out = 8, 16, 8

W1 = nn.Linear(d_in, d_ff, bias=False)    # key matrix  (d_ff x d_in rows)
W2 = nn.Linear(d_ff, d_out, bias=False)   # value matrix

# Plant a memory: key 3 -> value vector
target_key   = torch.randn(d_in)
target_value = torch.randn(d_out)
with torch.no_grad():
    W1.weight[3]    = target_key          # row 3 of W1 = the key
    W2.weight[:, 3] = target_value       # column 3 of W2 = the value

# Query with the planted key pattern
x_query     = target_key.unsqueeze(0)    # (1, d_in)
activations = F.relu(W1(x_query))        # key pattern activates key 3 strongly
print('Activations (should be highest at index 3):')
print(activations.detach().numpy().round(3))
print('Max activation at index:', activations.argmax().item())

retrieved = W2(activations)
print('\nRetrieved:', retrieved.detach().numpy().round(3))
print('Target:   ', target_value.numpy().round(3))
cos = F.cosine_similarity(retrieved, target_value.unsqueeze(0))
print(f'Cosine similarity: {cos.item():.4f}  (high = successful retrieval)')
```

## Code 4 — Profiling FFN vs Attention Compute Budget

Empirically timing FFN and self-attention on the same batch to quantify their relative compute costs, showing the FFN dominates at large d_ff.

```python
import torch
import torch.nn as nn
import time

def time_module(module: nn.Module, x: torch.Tensor,
                n_runs: int = 100, label: str = '') -> float:
    module.eval()
    with torch.no_grad():
        for _ in range(10):      # warm-up
            _ = module(x)
        t0 = time.perf_counter()
        for _ in range(n_runs):
            _ = module(x)
        ms = (time.perf_counter() - t0) / n_runs * 1000
    print(f'{label:<28}: {ms:.3f} ms/pass')
    return ms

d_model, n_heads, d_ff = 512, 8, 2048
B, L = 4, 128

ffn = nn.Sequential(
    nn.Linear(d_model, d_ff), nn.GELU(), nn.Linear(d_ff, d_model)
)

class AttnWrapper(nn.Module):
    def __init__(self, d, h): super().__init__(); self.a = nn.MultiheadAttention(d, h, batch_first=True)
    def forward(self, x): return self.a(x, x, x)[0]

x_ffn  = torch.randn(B, L, d_model)
x_attn = torch.randn(B, L, d_model)

t_ffn  = time_module(ffn, x_ffn, label=f'FFN (d_ff={d_ff})')
t_attn = time_module(AttnWrapper(d_model, n_heads), x_attn, label='Self-Attention')
print(f'FFN / Attn time ratio: {t_ffn/t_attn:.2f}x  (d_model={d_model}, L={L})')
```

## FFN Variants Compared

| Variant | Activation | Matrices | d_ff Ratio | Used In |
| --- | --- | --- | --- | --- |
| Standard ReLU | ReLU | 2 | 4× d_model | Original Transformer, early BERT |
| Standard GELU | GELU | 2 | 4× d_model | GPT-2, BERT, RoBERTa |
| SwiGLU | SiLU (Swish) gate | 3 | ~8/3× d_model | LLaMA 1/2/3, Mistral, PaLM, Gemma |
| ReGLU | ReLU gate | 3 | ≤4× d_model | Research models (Shazeer 2020) |
| GEGLU | GELU gate | 3 | ≤4× d_model | T5 variants, some BERT successors |
| Sparse MoE | Any (per expert) | 2 per expert | k active of n experts | Mixtral, Switch Transformer |

The FFN sub-layer is deceptively simple but plays a central role: it provides per-token non-linear transformation after each attention operation, storing factual knowledge in its weights and acting as the model's memory. The evolution from ReLU to GELU to gated variants (SwiGLU) represents consistent empirical wins at the same compute budget — a rare case where a drop-in change reliably improves quality without increasing FLOPs.

