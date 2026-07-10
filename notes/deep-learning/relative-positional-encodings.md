---
title: "Relative Positional Encodings — T5 Bias and Shaw et al."
slug: "relative-positional-encodings"
description: "Understand how relative positional encodings replace absolute position indices with inter-token distances: Shaw et al. (2018) query-relative embeddings modifying attention scores, T5 log-spaced bucket bias, DeBERTa disentangled attention, and empirical length generalisation beyond training sequence length."
tags: ["deep-learning", "transformers", "positional-encoding"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWJzb2x1dGUgcG9zaXRpb25hbCBlbmNvZGluZ3MgKHNpbnVzb2lkYWwgb3IgbGVhcm5lZCkgYXNzaWduIGEgdW5pcXVlIHZlY3RvciB0byBlYWNoIGFic29sdXRlIHBvc2l0aW9uIDEsIDIsIOKApiwgTC4gVGhpcyB3b3JrcyB3ZWxsIHdpdGhpbiB0aGUgdHJhaW5pbmcgbGVuZ3RoIGJ1dCBmYWlscyB0byBnZW5lcmFsaXNlOiBwb3NpdGlvbiA1MTIgZHVyaW5nIHRyYWluaW5nIGFuZCBwb3NpdGlvbiA1MTIgYXQgdGVzdCB0aW1lIG1lYW4gdGhlIHNhbWUgdGhpbmcgb25seSBpZiB0aGUgc2VxdWVuY2UgY29udGV4dCBpcyBpZGVudGljYWwuIFJlbGF0aXZlIHBvc2l0aW9uYWwgZW5jb2RpbmdzIHRha2UgYSBkaWZmZXJlbnQgYXBwcm9hY2gg4oCUIHRoZXkgZW5jb2RlIHRoZSBkaXN0YW5jZSBiZXR3ZWVuIHRva2VuIHBhaXJzIHJhdGhlciB0aGFuIHRoZWlyIGFic29sdXRlIGluZGljZXMuIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IGluIGxhbmd1YWdlLCB3aGF0IG1hdHRlcnMgaXMgb2Z0ZW4gaG93IGZhciBhcGFydCB0d28gdG9rZW5zIGFyZSAoYWRqYWNlbnQgbW9kaWZpZXIsIGNsYXVzZSBib3VuZGFyeSwgc2VudGVuY2UgZW5kKSByYXRoZXIgdGhhbiB0aGVpciBhYnNvbHV0ZSBpbmRleCBpbiBhIGRvY3VtZW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFic29sdXRlIHZzIFJlbGF0aXZlIFBvc2l0aW9uIOKAlCBUaGUgQ29yZSBEaXN0aW5jdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gc3RhbmRhcmQgYXR0ZW50aW9uLCB0aGUgc2NvcmUgYmV0d2VlbiBxdWVyeSBhdCBwb3NpdGlvbiBpIGFuZCBrZXkgYXQgcG9zaXRpb24gaiBpczogc197aWp9ID0gcV9pIMK3IGtfaiAvIHNxcnQoZF9rKS4gQWZ0ZXIgYWRkaW5nIGFic29sdXRlIFBFLCBxX2kgYW5kIGtfaiBlYWNoIGNhcnJ5IHRoZWlyIG93biBwb3NpdGlvbiwgYnV0IHRoZSBzY29yZSBzdGlsbCBjb25mbGF0ZXMgY29udGVudCBhbmQgcG9zaXRpb24gaW4gYSBmaXhlZCB3YXkuIFJlbGF0aXZlIFBFIGFwcHJvYWNoZXMgaW5zdGVhZCBtb2RpZnkgdGhlIHNjb3JlIGRpcmVjdGx5IHVzaW5nIHRoZSBkaXN0YW5jZSAoaiAtIGkpOiBzX3tpan0gPSAocV9pICsgcl97ai1pfSkgwrcga19qIHdoZXJlIHJfe2otaX0gaXMgYSBsZWFybmVkIG9yIGNvbXB1dGVkIHZlY3RvciBmb3IgdGhlIHJlbGF0aXZlIG9mZnNldC4gVGhpcyBtYWtlcyB0aGUgc2NvcmUgZXhwbGljaXRseSBzZW5zaXRpdmUgdG8gdGhlIHJlbGF0aW9uc2hpcCBiZXR3ZWVuIHBvc2l0aW9ucyByYXRoZXIgdGhhbiBlYWNoIHBvc2l0aW9uXHUwMDI3cyBhYnNvbHV0ZSBpbmRleCwgZW5hYmxpbmcgdGhlIG1vZGVsIHRvIGdlbmVyYWxpc2UgdGhlIHBhdHRlcm4gXHUwMDI3YXR0ZW5kIHRvIHRoZSB0b2tlbiAzIHBvc2l0aW9ucyBiYWNrXHUwMDI3IGFjcm9zcyBhbnkgYWJzb2x1dGUgbG9jYXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZWxhdGl2ZSBQRSBhbHNvIGVuYWJsZXMgYmV0dGVyIGxlbmd0aCBnZW5lcmFsaXNhdGlvbjogYSBtb2RlbCB0cmFpbmVkIG9uIHNlcXVlbmNlcyBvZiBsZW5ndGggMTI4IGNhbiBoYW5kbGUgbGVuZ3RoIDI1NiBiZWNhdXNlIHRoZSBwb3NpdGlvbiBzaWduYWxzIGl0IHdhcyB0cmFpbmVkIG9uIChkaXN0YW5jZXMgMCwgMSwgMiwg4oCmLCAxMjcpIHN0aWxsIGFwcGVhciB3aXRoaW4gdGhlIGxvbmdlciBzZXF1ZW5jZS4gQWJzb2x1dGUgUEUgbW9kZWxzIG11c3Qgc2VlIHBvc2l0aW9uIGluZGV4IDIwMCBkdXJpbmcgdHJhaW5pbmcgdG8gaGFuZGxlIGl0IOKAlCByZWxhdGl2ZSBtb2RlbHMgb25seSBuZWVkIHRvIGhhdmUgc2VlbiBkaXN0YW5jZSAyMDAgYmV0d2VlbiBzb21lIHBhaXIgb2YgdG9rZW5zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNoYXcgZXQgYWwuIDIwMTgg4oCUIFJlbGF0aXZlIFBFIGluIEF0dGVudGlvbiBTY29yZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNoYXcgZXQgYWwuICgyMDE4KSBpbnRyb2R1Y2VkIHRoZSBmaXJzdCB3aWRlbHktdXNlZCByZWxhdGl2ZSBQRTogbW9kaWZ5IGVhY2ggYXR0ZW50aW9uIHNjb3JlIGJ5IGEgbGVhcm5lZCBlbWJlZGRpbmcgZm9yIHRoZSByZWxhdGl2ZSBkaXN0YW5jZSBjbGlwcGVkIHRvIGEgbWF4aW11bSByYW5nZS4gVGhlIHNjb3JlIGJlY29tZXMgYV97aWp9ID0gKHFfaSArIHJfe2otaX0pIMK3IGtfaiAvIHNxcnQoZF9rKSB3aGVyZSByX2QgaXMgYSBsZWFybmVkIGRfbW9kZWwtZGltZW5zaW9uYWwgdmVjdG9yIGZvciBkaXN0YW5jZSBkLiBEaXN0YW5jZXMgYmV5b25kIGEgdGhyZXNob2xkIChlLmcuIMKxMTYpIHNoYXJlIHRoZSBib3VuZGFyeSBlbWJlZGRpbmcg4oCUIHRoZSBhc3N1bXB0aW9uIGJlaW5nIHRoYXQgdmVyeSBkaXN0YW50IHBvc2l0aW9ucyBjYXJyeSBsaW1pdGVkIGFkZGl0aW9uYWwgc2VxdWVudGlhbCBpbmZvcm1hdGlvbi4gVGhlIHZhbHVlIHNpZGUgY2FuIG9wdGlvbmFsbHkgYmUgc2ltaWxhcmx5IGF1Z21lbnRlZC4gVGhpcyBhcHByb2FjaCByZXF1aXJlcyBPKG4pIGFkZGl0aW9uYWwgZW1iZWRkaW5ncyAobm90IE8obsKyKSkgYmVjYXVzZSBkaXN0YW5jZXMgYXJlIHNoYXJlZCBhY3Jvc3MgYWxsIChpLCBqKSBwYWlycyB3aXRoIHRoZSBzYW1lIG9mZnNldC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgU2hhd1JlbGF0aXZlUEUobm4uTW9kdWxlKTpcbiAgICAjIFNoYXcgZXQgYWwuICgyMDE4KTogbGVhcm5lZCByZWxhdGl2ZSBwb3NpdGlvbiBlbWJlZGRpbmdzIGluIGF0dGVudGlvbi5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgbWF4X3JlbGF0aXZlPTE2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubWF4X3JlbCA9IG1heF9yZWxhdGl2ZVxuICAgICAgICBzZWxmLnJlbF9rICAgPSBubi5FbWJlZGRpbmcoMiAqIG1heF9yZWxhdGl2ZSArIDEsIGRfbW9kZWwpXG5cbiAgICBkZWYgX2NsaXAoc2VsZiwgZGlzdCk6XG4gICAgICAgIHJldHVybiBkaXN0LmNsYW1wKC1zZWxmLm1heF9yZWwsIHNlbGYubWF4X3JlbCkgKyBzZWxmLm1heF9yZWxcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIFEsIEspOlxuICAgICAgICAjIFEsIEs6IChiYXRjaCwgc2VxLCBkX21vZGVsKVxuICAgICAgICBzZXEsIGRrID0gUS5zaGFwZVsxXSwgUS5zaGFwZVstMV1cbiAgICAgICAgY29udGVudCA9IHRvcmNoLmJtbShRLCBLLnRyYW5zcG9zZSgxLCAyKSkgLyBkayAqKiAwLjVcbiAgICAgICAgaSA9IHRvcmNoLmFyYW5nZShzZXEpLnVuc3F1ZWV6ZSgxKVxuICAgICAgICBqID0gdG9yY2guYXJhbmdlKHNlcSkudW5zcXVlZXplKDApXG4gICAgICAgIGRpc3QgPSBzZWxmLl9jbGlwKGogLSBpKSAgICAgICAgICAgICAgIyAoc2VxLCBzZXEpIGNsaXBwZWQgZGlzdGFuY2VzXG4gICAgICAgIFIgICAgPSBzZWxmLnJlbF9rKGRpc3QpICAgICAgICAgICAgICAgIyAoc2VxLCBzZXEsIGRfbW9kZWwpXG4gICAgICAgIHJlbCAgPSB0b3JjaC5laW5zdW0oXHUwMDI3YnFkLHFrZC1cdTAwM2VicWtcdTAwMjcsIFEsIFIpIC8gZGsgKiogMC41XG4gICAgICAgIHJldHVybiBGLnNvZnRtYXgoY29udGVudCArIHJlbCwgZGltPS0xKVxuXG50b3JjaC5tYW51YWxfc2VlZCg3KVxubW9kZWwgPSBTaGF3UmVsYXRpdmVQRShkX21vZGVsPTY0LCBtYXhfcmVsYXRpdmU9OClcblEgPSB0b3JjaC5yYW5kbigyLCAxMiwgNjQpXG5LID0gdG9yY2gucmFuZG4oMiwgMTIsIDY0KVxuYXR0biA9IG1vZGVsKFEsIEspXG5wcmludChcdTAwMjdBdHRlbnRpb24gc2hhcGU6XHUwMDI3LCBhdHRuLnNoYXBlKVxucHJpbnQoXHUwMDI3Um93IHN1bXMgKHNob3VsZCBiZSAxKTpcdTAwMjcsIGF0dG5bMF0uc3VtKGRpbT0tMSkuZGV0YWNoKCkucm91bmQoZGVjaW1hbHM9MykpXG5wcmludChcdTAwMjdDb250ZW50IHNjb3JlICsgcmVsYXRpdmUgZW1iZWRkaW5nIHNjb3JlID0gZmluYWwgbG9naXQuXHUwMDI3KVxucHJpbnQoXHUwMDI3RGlzdGFuY2VzIFx1MDAzZT1cdTAwMjcgKyBzdHIobW9kZWwubWF4X3JlbCkgKyBcdTAwMjcgc2hhcmUgb25lIGVtYmVkZGluZyAoY2xpcHBlZCkuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlQ1IFJlbGF0aXZlIEJpYXMg4oCUIExvZy1TcGFjZWQgQnVja2V0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmFmZmVsIGV0IGFsLiAoMjAyMCkgaW50cm9kdWNlZCBhIHNpbXBsZXIgcmVsYXRpdmUgUEUgaW4gVDU6IGEgbGVhcm5lZCBzY2FsYXIgYmlhcyBiX3tqLWl9IGFkZGVkIHRvIGVhY2ggYXR0ZW50aW9uIGxvZ2l0LCBzaGFyZWQgYWNyb3NzIGFsbCBwb3NpdGlvbiBwYWlycyB3aXRoIHRoZSBzYW1lIHJlbGF0aXZlIG9mZnNldC4gSW5zdGVhZCBvZiBhIGZ1bGwgZF9tb2RlbC1kaW1lbnNpb25hbCB2ZWN0b3IgcGVyIGRpc3RhbmNlIChTaGF3IGV0IGFsLiksIFQ1IHVzZXMgYSBzaW5nbGUgc2NhbGFyIHBlciBoZWFkIHBlciBkaXN0YW5jZSBidWNrZXQuIERpc3RhbmNlcyBhcmUgZ3JvdXBlZCBpbnRvIDMyIGJ1Y2tldHMgd2l0aCBsb2ctc3BhY2luZzogbWFueSBmaW5lLWdyYWluZWQgYnVja2V0cyBmb3Igc21hbGwgZGlzdGFuY2VzICh3aGVyZSBwcmVjaXNlIHBvc2l0aW9uIG1hdHRlcnMpIGFuZCBmZXcgY29hcnNlIGJ1Y2tldHMgZm9yIGxhcmdlIGRpc3RhbmNlcyAod2hlcmUgZXhhY3Qgb2Zmc2V0IG1hdHRlcnMgbGVzcykuIFRoZSBiaWFzIHRhYmxlIGhhcyBzaGFwZSAobnVtX2J1Y2tldHMsIG51bV9oZWFkcykgPSAoMzIsIG51bV9oZWFkcykg4oCUIGEgdmVyeSBzbWFsbCBhZGRpdGlvbi4gQ3J1Y2lhbGx5LCB0aGUgYmlhcyBpcyBzaGFyZWQgYWNyb3NzIGFsbCBsYXllcnMsIGRyYW1hdGljYWxseSByZWR1Y2luZyBwYXJhbWV0ZXJzIGNvbXBhcmVkIHRvIHBlci1sYXllciByZWxhdGl2ZSBlbWJlZGRpbmdzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuY2xhc3MgVDVSZWxhdGl2ZUJpYXMobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbnVtX2hlYWRzLCBudW1fYnVja2V0cz0zMiwgbWF4X2Rpc3RhbmNlPTEyOCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm51bV9idWNrZXRzICA9IG51bV9idWNrZXRzXG4gICAgICAgIHNlbGYubWF4X2Rpc3RhbmNlID0gbWF4X2Rpc3RhbmNlXG4gICAgICAgIHNlbGYuYmlhcyA9IG5uLkVtYmVkZGluZyhudW1fYnVja2V0cywgbnVtX2hlYWRzKVxuXG4gICAgZGVmIF9idWNrZXQoc2VsZiwgcmVsX3Bvcyk6XG4gICAgICAgIGhhbGYgPSBzZWxmLm51bV9idWNrZXRzIC8vIDJcbiAgICAgICAgbiAgICA9IHJlbF9wb3MuYWJzKClcbiAgICAgICAgaXNfc21hbGwgPSBuIFx1MDAzYyBoYWxmXG4gICAgICAgIGxhcmdlX3ZhbCA9IGhhbGYgKyAoXG4gICAgICAgICAgICB0b3JjaC5sb2cobi5mbG9hdCgpLmNsYW1wKG1pbj0xKSAvIGhhbGYpIC9cbiAgICAgICAgICAgIG1hdGgubG9nKHNlbGYubWF4X2Rpc3RhbmNlIC8gaGFsZikgKiAoc2VsZi5udW1fYnVja2V0cyAtIGhhbGYpXG4gICAgICAgICkubG9uZygpLmNsYW1wKDAsIHNlbGYubnVtX2J1Y2tldHMgLSBoYWxmIC0gMSlcbiAgICAgICAgcmV0dXJuIHRvcmNoLndoZXJlKGlzX3NtYWxsLCBuLCBsYXJnZV92YWwpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBzZXFfcSwgc2VxX2spOlxuICAgICAgICBxX3BvcyA9IHRvcmNoLmFyYW5nZShzZXFfcSkudW5zcXVlZXplKDEpXG4gICAgICAgIGtfcG9zID0gdG9yY2guYXJhbmdlKHNlcV9rKS51bnNxdWVlemUoMClcbiAgICAgICAgcmVsICAgPSBrX3BvcyAtIHFfcG9zICAgICAgICAgICAgICAgICAjIChzZXFfcSwgc2VxX2spXG4gICAgICAgIGJrdCAgID0gc2VsZi5fYnVja2V0KHJlbClcbiAgICAgICAgYmlhcyAgPSBzZWxmLmJpYXMoYmt0KSAgICAgICAgICAgICAgICAjIChzZXFfcSwgc2VxX2ssIG51bV9oZWFkcylcbiAgICAgICAgcmV0dXJuIGJpYXMucGVybXV0ZSgyLCAwLCAxKSAgICAgICAgICAjIChudW1faGVhZHMsIHNlcV9xLCBzZXFfaylcblxudDUgPSBUNVJlbGF0aXZlQmlhcyhudW1faGVhZHM9OClcbmJpYXMgPSB0NShzZXFfcT0xMiwgc2VxX2s9MTIpXG5wcmludChcdTAwMjdCaWFzIHNoYXBlOlx1MDAyNywgYmlhcy5zaGFwZSlcbnByaW50KFx1MDAyN1BhcmFtZXRlcnM6XHUwMDI3LCBzdW0ocC5udW1lbCgpIGZvciBwIGluIHQ1LnBhcmFtZXRlcnMoKSkpXG5idWNrZXRzID0gW3Q1Ll9idWNrZXQodG9yY2gudGVuc29yKGQpKS5pdGVtKCkgZm9yIGQgaW4gcmFuZ2UoMTApXVxucHJpbnQoXHUwMDI3QnVja2V0cyBmb3IgZGlzdGFuY2VzIDAtOTpcdTAwMjcsIGJ1Y2tldHMpXG5wcmludChcdTAwMjdMb2ctc3BhY2luZzogbWFueSBidWNrZXRzIGZvciBzbWFsbCBkaXN0YW5jZXMsIGZld2VyIGZvciBsYXJnZS5cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlQ1IEJpYXMgdnMgU2hhdyBFbWJlZGRpbmc6IEtleSBUcmFkZS1vZmZzIiwiY29udGVudCI6IlNoYXcgZXQgYWwuIHVzZSBhIGZ1bGwgZF9tb2RlbC1kaW1lbnNpb25hbCB2ZWN0b3IgcGVyIGRpc3RhbmNlIChoaWdoIGV4cHJlc3NpdmVuZXNzLCBoaWdoIGNvc3QpOyBUNSB1c2VzIGEgc2luZ2xlIHNjYWxhciBwZXIgaGVhZCBwZXIgYnVja2V0IChsb3cgY29zdCwgZ29vZCBnZW5lcmFsaXNhdGlvbikuIFQ1IGJ1Y2tldHMgYXJlIGxvZy1zcGFjZWQg4oCUIDE2IGV4YWN0IGJ1Y2tldHMgZm9yIGRpc3RhbmNlcyAwLTE1LCB0aGVuIDE2IGxvZy1zcGFjZWQgYnVja2V0cyBmb3IgMTYtMTI4Ky4gVGhpcyBjaG9pY2UgcmVmbGVjdHMgdGhlIGxpbmd1aXN0aWMgcHJpb3IgdGhhdCBsb2NhbCBjb250ZXh0IChuZWFyYnkgdG9rZW5zKSBpcyBtb3JlIGRpc3RhbmNlLXNlbnNpdGl2ZSB0aGFuIGRpc3RhbnQgY29udGV4dC4gVDUgcmVsYXRpdmUgYmlhcyBpcyBhZGRlZCB0byBldmVyeSBhdHRlbnRpb24gbGF5ZXJcdTAwMjdzIGxvZ2l0cyB1c2luZyB0aGUgc2FtZSBzaGFyZWQgd2VpZ2h0IHRhYmxlLCBub3Qgc2VwYXJhdGUgdGFibGVzIHBlciBsYXllci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZUJFUlRhIOKAlCBEaXNlbnRhbmdsZWQgQXR0ZW50aW9uIE1lY2hhbmlzbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSGUgZXQgYWwuICgyMDIxKSBpbnRyb2R1Y2VkIERlQkVSVGEgd2l0aCBkaXNlbnRhbmdsZWQgYXR0ZW50aW9uOiBlYWNoIHRva2VuIGlzIHJlcHJlc2VudGVkIGJ5IHR3byB2ZWN0b3JzIOKAlCBhIGNvbnRlbnQgdmVjdG9yIGFuZCBhIHBvc2l0aW9uIHZlY3RvciDigJQgYW5kIHRoZSBhdHRlbnRpb24gc2NvcmUgaXMgZGVjb21wb3NlZCBpbnRvIHRocmVlIHRlcm1zOiBjb250ZW50LXRvLWNvbnRlbnQgKHN0YW5kYXJkIGRvdCBwcm9kdWN0KSwgY29udGVudC10by1wb3NpdGlvbiAocXVlcnkgY29udGVudCBhdHRlbmRpbmcgdG8ga2V5IHBvc2l0aW9ucyksIGFuZCBwb3NpdGlvbi10by1jb250ZW50IChxdWVyeSBwb3NpdGlvbnMgYXR0ZW5kaW5nIHRvIGtleSBjb250ZW50KS4gVGhpcyByaWNoZXIgaW50ZXJhY3Rpb24gYWxsb3dzIHRoZSBtb2RlbCB0byBzZXBhcmF0ZWx5IGxlYXJuIHdoYXQgYSB0b2tlbiBtZWFucyBhbmQgd2hlcmUgaXQgaXMuIFRoZSBwb3NpdGlvbiBlbWJlZGRpbmdzIGFyZSByZWxhdGl2ZTogdG9rZW4gYXQgcG9zaXRpb24gaSB1c2VzIHRoZSBlbWJlZGRpbmcgZm9yIGRpc3RhbmNlIChqIC0gaSkgd2hlbiBjb21wdXRpbmcgaXRzIHNjb3JlIGFnYWluc3QgcG9zaXRpb24gaiwgbWFraW5nIHRoZSBzY2hlbWUgbmF0dXJhbGx5IHJlbGF0aXZlIGFuZCBlbmFibGluZyBsZW5ndGggZ2VuZXJhbGlzYXRpb24uIERlQkVSVGEgb21pdHMgdGhlIHBvc2l0aW9uLXRvLXBvc2l0aW9uIHRlcm0gYXMgZW1waXJpY2FsbHkgbGVzcyB1c2VmdWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIERpc2VudGFuZ2xlZEF0dGVudGlvbihubi5Nb2R1bGUpOlxuICAgICMgRGVCRVJUYSAoSGUgZXQgYWwuIDIwMjEpOiBjb250ZW50LXRvLWNvbnRlbnQgKyBjb250ZW50LXRvLXBvc2l0aW9uLlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsLCBudW1faGVhZHMsIG1heF9yZWw9MTI4KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZGsgICAgICA9IGRfbW9kZWwgLy8gbnVtX2hlYWRzXG4gICAgICAgIHNlbGYuaCAgICAgICA9IG51bV9oZWFkc1xuICAgICAgICBzZWxmLldxICAgICAgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XayAgICAgID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuV3AgICAgICA9IG5uLkVtYmVkZGluZygyICogbWF4X3JlbCArIDEsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYubWF4X3JlbCA9IG1heF9yZWxcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBiLCBuLCBkID0geC5zaGFwZVxuICAgICAgICBRID0gc2VsZi5XcSh4KS52aWV3KGIsIG4sIHNlbGYuaCwgc2VsZi5kaykudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIEsgPSBzZWxmLldrKHgpLnZpZXcoYiwgbiwgc2VsZi5oLCBzZWxmLmRrKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgYzJjID0gUSBAIEsudHJhbnNwb3NlKC0yLCAtMSkgLyBzZWxmLmRrICoqIDAuNVxuICAgICAgICBpICAgPSB0b3JjaC5hcmFuZ2UobikudW5zcXVlZXplKDEpXG4gICAgICAgIGogICA9IHRvcmNoLmFyYW5nZShuKS51bnNxdWVlemUoMClcbiAgICAgICAgaWR4ID0gKGogLSBpKS5jbGFtcCgtc2VsZi5tYXhfcmVsLCBzZWxmLm1heF9yZWwpICsgc2VsZi5tYXhfcmVsXG4gICAgICAgIFAgICA9IHNlbGYuV3AoaWR4KSAgICAgICAgICAgICAgICAgICAgICAgICAjIChuLCBuLCBkX21vZGVsKVxuICAgICAgICBQICAgPSBQLnZpZXcobiwgbiwgc2VsZi5oLCBzZWxmLmRrKS5wZXJtdXRlKDIsIDAsIDEsIDMpXG4gICAgICAgIGMycCA9IChRLnVuc3F1ZWV6ZSgtMikgKiBQKS5zdW0oLTEpIC8gc2VsZi5kayAqKiAwLjVcbiAgICAgICAgcmV0dXJuIEYuc29mdG1heChjMmMgKyBjMnAsIGRpbT0tMSlcblxudG9yY2gubWFudWFsX3NlZWQoMylcbmRhICAgPSBEaXNlbnRhbmdsZWRBdHRlbnRpb24oZF9tb2RlbD02NCwgbnVtX2hlYWRzPTQsIG1heF9yZWw9MTYpXG54ICAgID0gdG9yY2gucmFuZG4oMiwgOCwgNjQpXG5hdHRuID0gZGEoeClcbnByaW50KFx1MDAyN0F0dGVudGlvbiBzaGFwZTpcdTAwMjcsIGF0dG4uc2hhcGUpXG5wcmludChcdTAwMjdjMmMgPSBjb250ZW50LXRvLWNvbnRlbnQ7IGMycCA9IGNvbnRlbnQtdG8tcG9zaXRpb24uXHUwMDI3KVxucHJpbnQoXHUwMDI3RGVCRVJUYSB1c2VzIG9ubHkgYzJjICsgYzJwIChub3QgcDJjKSBpbiB0aGlzIHNpbXBsaWZpZWQgdmVyc2lvbi5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGVuZ3RoIEdlbmVyYWxpc2F0aW9uIOKAlCBSZWxhdGl2ZSB2cyBBYnNvbHV0ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVsYXRpdmUgUEUgc2NoZW1lcyBnZW5lcmFsaXNlIGJldHRlciB0byBzZXF1ZW5jZXMgbG9uZ2VyIHRoYW4gdGhlIHRyYWluaW5nIG1heGltdW0gYmVjYXVzZSB0aGUgZGlzdGFuY2Ugdm9jYWJ1bGFyeSAoMCwgMSwg4oCmLCBtYXhfZGlzdCkgYXBwZWFycyB0aHJvdWdob3V0IHRyYWluaW5nIHJlZ2FyZGxlc3Mgb2YgYWJzb2x1dGUgcG9zaXRpb24uIEEgbW9kZWwgdHJhaW5lZCBvbiA2NC10b2tlbiBzZXF1ZW5jZXMgc2VlcyBkaXN0YW5jZXMgMOKAkzYzOyB0ZXN0aW5nIG9uIDEyOC10b2tlbiBzZXF1ZW5jZXMgaW50cm9kdWNlcyBuZXcgZGlzdGFuY2VzICg2NOKAkzEyNykgYnV0IHRoZSBleGlzdGluZyBkaXN0YW5jZXMgc3RpbGwgb3BlcmF0ZSBjb3JyZWN0bHkuIEluIGNvbnRyYXN0LCBhYnNvbHV0ZSBQRSBtb2RlbHMgaGF2ZSBubyBlbWJlZGRpbmcgZm9yIHBvc2l0aW9uIDEyOCBpZiB0aGV5IHdlcmUgdHJhaW5lZCB3aXRoIG1heF9zZXFfbGVuPTY0LiBUaGUgZm9sbG93aW5nIGNvZGUgbWVhc3VyZXMgaG93IGNvbnNpc3RlbnRseSBQRSBzY2hlbWVzIGRpc3Rpbmd1aXNoIGNvbnNlY3V0aXZlIHBvc2l0aW9ucyBhY3Jvc3MgZGlmZmVyZW50IHRlc3QgbGVuZ3Rocy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBtYXRoXG5cbmRlZiBzaW51c29pZGFsX3BlKHNlcV9sZW4sIGRfbW9kZWwpOlxuICAgIHBlICA9IHRvcmNoLnplcm9zKHNlcV9sZW4sIGRfbW9kZWwpXG4gICAgcG9zID0gdG9yY2guYXJhbmdlKHNlcV9sZW4pLmZsb2F0KCkudW5zcXVlZXplKDEpXG4gICAgZGl2ID0gdG9yY2guZXhwKHRvcmNoLmFyYW5nZSgwLCBkX21vZGVsLCAyKS5mbG9hdCgpICogKC1tYXRoLmxvZygxMDAwMC4wKSAvIGRfbW9kZWwpKVxuICAgIHBlWzosIDA6OjJdID0gdG9yY2guc2luKHBvcyAqIGRpdilcbiAgICBwZVs6LCAxOjoyXSA9IHRvcmNoLmNvcyhwb3MgKiBkaXYpXG4gICAgcmV0dXJuIHBlXG5cbmRlZiBhdmdfY29uc2VjdXRpdmVfZGlzdGFuY2UocGUpOlxuICAgIHJldHVybiAocGVbMTpdIC0gcGVbOi0xXSkubm9ybShkaW09LTEpLm1lYW4oKS5pdGVtKClcblxudHJhaW5fbGVuLCBkX21vZGVsID0gNjQsIDEyOFxuc2luX3RyYWluID0gc2ludXNvaWRhbF9wZSh0cmFpbl9sZW4sIGRfbW9kZWwpXG5sZWFybmVkICAgPSBubi5FbWJlZGRpbmcodHJhaW5fbGVuLCBkX21vZGVsKVxubm4uaW5pdC5ub3JtYWxfKGxlYXJuZWQud2VpZ2h0LCBzdGQ9MC4wMilcblxucHJpbnQoXHUwMDI3RXh0cmFwb2xhdGlvbiBjb21wYXJpc29uICh0cmFpbl9sZW49NjQpXHUwMDI3KVxucHJpbnQoXHUwMDI3ezpcdTAwM2UxMH0gezpcdTAwM2UxNH0gezpcdTAwM2UxNH1cdTAwMjcuZm9ybWF0KFx1MDAyN3Rlc3RfbGVuXHUwMDI3LCBcdTAwMjdzaW51c29pZGFsXHUwMDI3LCBcdTAwMjdsZWFybmVkXHUwMDI3KSlcbmZvciB0ZXN0X2xlbiBpbiBbMzIsIDY0LCA5NiwgMTI4LCAxOTJdOlxuICAgIHNpbl90ZXN0ID0gc2ludXNvaWRhbF9wZSh0ZXN0X2xlbiwgZF9tb2RlbClcbiAgICBzaW5fZGlzdCA9IGF2Z19jb25zZWN1dGl2ZV9kaXN0YW5jZShzaW5fdGVzdClcbiAgICBpZHMgICAgICA9IHRvcmNoLmFyYW5nZSh0ZXN0X2xlbikuY2xhbXAoMCwgdHJhaW5fbGVuIC0gMSlcbiAgICBscm5fcGUgICA9IGxlYXJuZWQoaWRzKS5kZXRhY2goKVxuICAgIGxybl9kaXN0ID0gYXZnX2NvbnNlY3V0aXZlX2Rpc3RhbmNlKGxybl9wZSlcbiAgICBwcmludChcdTAwMjd7Olx1MDAzZTEwfSB7Olx1MDAzZTE0LjRmfSB7Olx1MDAzZTE0LjRmfVx1MDAyNy5mb3JtYXQodGVzdF9sZW4sIHNpbl9kaXN0LCBscm5fZGlzdCkpXG5wcmludChcdTAwMjdMZWFybmVkIGRpc3QgY29sbGFwc2VzIGF0IHBvc2l0aW9ucyBcdTAwM2UgdHJhaW5fbGVuOyBzaW51c29pZGFsIHN0YXlzIHN0YWJsZS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhbnNmb3JtZXItWEwgYW5kIFNlZ21lbnQgUmVjdXJyZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGFpIGV0IGFsLiAoMjAxOSkgaW50cm9kdWNlZCBUcmFuc2Zvcm1lci1YTCB3aXRoIGEgcmVsYXRpdmUgUEUgdmFyaWFudCBkZXNpZ25lZCBmb3Igc2VnbWVudCByZWN1cnJlbmNlOiBkdXJpbmcgdHJhaW5pbmcsIGNhY2hlZCBoaWRkZW4gc3RhdGVzIGZyb20gcHJldmlvdXMgc2VnbWVudHMgYXJlIGFwcGVuZGVkIGFzIGFkZGl0aW9uYWwga2V5cyBhbmQgdmFsdWVzLiBBYnNvbHV0ZSBwb3NpdGlvbiBlbWJlZGRpbmdzIGJyZWFrIGhlcmUgYmVjYXVzZSBhIHRva2VuIGF0IGFic29sdXRlIHBvc2l0aW9uIDUgaW4gc2VnbWVudCB0IGhhcyBhIGRpZmZlcmVudCBwb3NpdGlvbmFsIHJlbGF0aW9uc2hpcCB0byBzZWdtZW50IHQtMSB0b2tlbnMgdGhhbiB0byBpdHMgb3duIHNlZ21lbnQuIFRyYW5zZm9ybWVyLVhMXHUwMDI3cyByZWxhdGl2ZSBQRSBkaXJlY3RseSBjb21wdXRlcyBzaW51c29pZGFsbHktZGVyaXZlZCBkaXN0YW5jZSB2ZWN0b3JzIGF0IGF0dGVudGlvbiB0aW1lLCBhbGxvd2luZyB0aGUgbW9kZWwgdG8gY29ycmVjdGx5IGVuY29kZSBcdTAwMjd0aGlzIHRva2VuIGlzIDE1MCBwb3NpdGlvbnMgYmVmb3JlIG1lIGluIHRoZSBjb250ZXh0XHUwMDI3IGV2ZW4gd2hlbiB0aGUgY29udGV4dCBzcGFucyBtdWx0aXBsZSBjYWNoZWQgc2VnbWVudHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUcmFuc2Zvcm1lci1YTDogc2ludXNvaWRhbC1kZXJpdmVkIHJlbGF0aXZlIFBFIGNvbXB1dGVkIGF0IGF0dGVudGlvbiB0aW1lLCBlbmFibGVzIHJlY3VycmVudCBtZW1vcnkiLCJTaGF3IGV0IGFsLjogbGVhcm5lZCB2ZWN0b3Igcl97ai1pfSBhZGRlZCB0byBxdWVyeSBpbiBhdHRlbnRpb24gc2NvcmUsIG1heCBkaXN0YW5jZSBjbGlwcGVkIiwiVDU6IHNjYWxhciBiaWFzIGJfe2otaX0gcGVyIGhlYWQsIGxvZy1zcGFjZWQgYnVja2V0cywgc2hhcmVkIGFjcm9zcyBhbGwgbGF5ZXJzIiwiRGVCRVJUYTogZGlzZW50YW5nbGVkIGNvbnRlbnQgKyBwb3NpdGlvbiB2ZWN0b3JzLCBjMmMgKyBjMnAgaW50ZXJhY3Rpb24gdGVybXMiLCJBbGwgcmVsYXRpdmUgbWV0aG9kcyBzaGFyZSBhIGtleSBwcm9wZXJ0eTogdGhlIHBvc2l0aW9uIHNpZ25hbCBkZXBlbmRzIG9uIChqLWkpIG5vdCBvbiBqIG9yIGkgaW5kaXZpZHVhbGx5Il19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gYW5kIFByYWN0aWNhbCBHdWlkYW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJFeHRyYXBvbGF0aW9uIiwiUGFyYW1ldGVycyIsIlNoYXJlZCBXZWlnaHRzIiwiQ29tcGxleGl0eSIsIlVzZWQgSW4iXSwicm93cyI6W1siQWJzb2x1dGUgUEUiLCJQb29yIOKAlCBoYXJkIGxpbWl0IGF0IG1heF9zZXFfbGVuIiwibWF4X2xlbsOXZF9tb2RlbCBvciAwIiwiTi9BIiwiTyhuKSIsIkJFUlQsIEdQVC0yIChoaXN0b3JpY2FsKSJdLFsiU2hhdyBldCBhbC4iLCJCZXR0ZXIg4oCUIGRpc3RhbmNlcyBnZW5lcmFsaXNlIiwiKDLDl21heF9yZWwrMSnDl2RfbW9kZWwiLCJDbGlwcGVkIGRpc3RhbmNlcyBzaGFyZSBib3VuZGFyeSIsIk8obsKyZCkiLCJNdXNpYyBUcmFuc2Zvcm1lciwgc29tZSBCRVJUIHZhcmlhbnRzIl0sWyJUNSBSZWxhdGl2ZSBCaWFzIiwiR29vZCDigJQgYnVja2V0cyBjb3ZlciBsYXJnZSBkaXN0IiwibnVtX2J1Y2tldHPDl251bV9oZWFkcyAodGlueSkiLCJMb2ctc3BhY2VkIGJ1Y2tldHMgc2hhcmVkIHBlciBsYXllciIsIk8obsKyKSIsIlQ1LCBVTDIsIEZsYW4tVDUiXSxbIkRlQkVSVGEiLCJHb29kIOKAlCByZWxhdGl2ZSBieSBkZXNpZ24iLCIoMsOXbWF4X3JlbCsxKcOXZF9tb2RlbCIsIlBvc2l0aW9uIGVtYmVkZGluZ3Mgc2hhcmVkIiwiTyhuwrJkKSIsIkRlQkVSVGEtdjEvdjIvdjMsIG1EZUJFUlRhIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBlbmNvZGVyLW9ubHkgbW9kZWxzIChjbGFzc2lmaWNhdGlvbiwgTkxVKSB3aGVyZSBzZXF1ZW5jZXMgc3RheSB3aXRoaW4gYSBtb2RlcmF0ZSBsZW5ndGgsIFQ1LXN0eWxlIHJlbGF0aXZlIGJpYXMgb2ZmZXJzIGFuIGV4Y2VsbGVudCBjb3N0LXF1YWxpdHkgYmFsYW5jZSDigJQgbWluaW1hbCBwYXJhbWV0ZXJzIGFuZCBzdHJvbmcgZ2VuZXJhbGlzYXRpb24uIEZvciBsYXJnZSBhdXRvcmVncmVzc2l2ZSBkZWNvZGVycywgUm9QRSAobm90IGluIHRoaXMgdGFibGUpIGlzIHRoZSBjdXJyZW50IHN0YW5kYXJkIGJlY2F1c2UgaXQgb3BlcmF0ZXMgb24gcm90YXRlZCBxdWVyeS1rZXkgdmVjdG9ycyB3aXRoIHplcm8gZXh0cmEgcGFyYW1ldGVycy4gRGVCRVJUYSBpcyB0aGUgc3Ryb25nZXN0IHBlcmZvcm1lciBmb3IgQkVSVC1zdHlsZSBwcmUtdHJhaW5pbmcgYXQgbW9kZXJhdGUgc2VxdWVuY2UgbGVuZ3Rocy4gU2hhdyBldCBhbC4gaXMgbGFyZ2VseSBzdXBlcnNlZGVkIGJ5IHRoZSBzaW1wbGVyIFQ1IGJpYXMgYW5kIHRoZSBtb3JlIHBvd2VyZnVsIERlQkVSVGEgYXBwcm9hY2guIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Relative Positional Encodings — T5 Bias and Shaw et al.

Absolute positional encodings (sinusoidal or learned) assign a unique vector to each absolute position 1, 2, …, L. This works well within the training length but fails to generalise: position 512 during training and position 512 at test time mean the same thing only if the sequence context is identical. Relative positional encodings take a different approach — they encode the distance between token pairs rather than their absolute indices. The key insight is that in language, what matters is often how far apart two tokens are (adjacent modifier, clause boundary, sentence end) rather than their absolute index in a document.

## Absolute vs Relative Position — The Core Distinction

In standard attention, the score between query at position i and key at position j is: s_{ij} = q_i · k_j / sqrt(d_k). After adding absolute PE, q_i and k_j each carry their own position, but the score still conflates content and position in a fixed way. Relative PE approaches instead modify the score directly using the distance (j - i): s_{ij} = (q_i + r_{j-i}) · k_j where r_{j-i} is a learned or computed vector for the relative offset. This makes the score explicitly sensitive to the relationship between positions rather than each position's absolute index, enabling the model to generalise the pattern 'attend to the token 3 positions back' across any absolute location.

Relative PE also enables better length generalisation: a model trained on sequences of length 128 can handle length 256 because the position signals it was trained on (distances 0, 1, 2, …, 127) still appear within the longer sequence. Absolute PE models must see position index 200 during training to handle it — relative models only need to have seen distance 200 between some pair of tokens.

## Shaw et al. 2018 — Relative PE in Attention Scores

Shaw et al. (2018) introduced the first widely-used relative PE: modify each attention score by a learned embedding for the relative distance clipped to a maximum range. The score becomes a_{ij} = (q_i + r_{j-i}) · k_j / sqrt(d_k) where r_d is a learned d_model-dimensional vector for distance d. Distances beyond a threshold (e.g. ±16) share the boundary embedding — the assumption being that very distant positions carry limited additional sequential information. The value side can optionally be similarly augmented. This approach requires O(n) additional embeddings (not O(n²)) because distances are shared across all (i, j) pairs with the same offset.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ShawRelativePE(nn.Module):
    # Shaw et al. (2018): learned relative position embeddings in attention.
    def __init__(self, d_model, max_relative=16):
        super().__init__()
        self.max_rel = max_relative
        self.rel_k   = nn.Embedding(2 * max_relative + 1, d_model)

    def _clip(self, dist):
        return dist.clamp(-self.max_rel, self.max_rel) + self.max_rel

    def forward(self, Q, K):
        # Q, K: (batch, seq, d_model)
        seq, dk = Q.shape[1], Q.shape[-1]
        content = torch.bmm(Q, K.transpose(1, 2)) / dk ** 0.5
        i = torch.arange(seq).unsqueeze(1)
        j = torch.arange(seq).unsqueeze(0)
        dist = self._clip(j - i)              # (seq, seq) clipped distances
        R    = self.rel_k(dist)               # (seq, seq, d_model)
        rel  = torch.einsum('bqd,qkd->bqk', Q, R) / dk ** 0.5
        return F.softmax(content + rel, dim=-1)

torch.manual_seed(7)
model = ShawRelativePE(d_model=64, max_relative=8)
Q = torch.randn(2, 12, 64)
K = torch.randn(2, 12, 64)
attn = model(Q, K)
print('Attention shape:', attn.shape)
print('Row sums (should be 1):', attn[0].sum(dim=-1).detach().round(decimals=3))
print('Content score + relative embedding score = final logit.')
print('Distances >=' + str(model.max_rel) + ' share one embedding (clipped).')
```

## T5 Relative Bias — Log-Spaced Buckets

Raffel et al. (2020) introduced a simpler relative PE in T5: a learned scalar bias b_{j-i} added to each attention logit, shared across all position pairs with the same relative offset. Instead of a full d_model-dimensional vector per distance (Shaw et al.), T5 uses a single scalar per head per distance bucket. Distances are grouped into 32 buckets with log-spacing: many fine-grained buckets for small distances (where precise position matters) and few coarse buckets for large distances (where exact offset matters less). The bias table has shape (num_buckets, num_heads) = (32, num_heads) — a very small addition. Crucially, the bias is shared across all layers, dramatically reducing parameters compared to per-layer relative embeddings.

```python
import torch
import torch.nn as nn
import math

class T5RelativeBias(nn.Module):
    def __init__(self, num_heads, num_buckets=32, max_distance=128):
        super().__init__()
        self.num_buckets  = num_buckets
        self.max_distance = max_distance
        self.bias = nn.Embedding(num_buckets, num_heads)

    def _bucket(self, rel_pos):
        half = self.num_buckets // 2
        n    = rel_pos.abs()
        is_small = n < half
        large_val = half + (
            torch.log(n.float().clamp(min=1) / half) /
            math.log(self.max_distance / half) * (self.num_buckets - half)
        ).long().clamp(0, self.num_buckets - half - 1)
        return torch.where(is_small, n, large_val)

    def forward(self, seq_q, seq_k):
        q_pos = torch.arange(seq_q).unsqueeze(1)
        k_pos = torch.arange(seq_k).unsqueeze(0)
        rel   = k_pos - q_pos                 # (seq_q, seq_k)
        bkt   = self._bucket(rel)
        bias  = self.bias(bkt)                # (seq_q, seq_k, num_heads)
        return bias.permute(2, 0, 1)          # (num_heads, seq_q, seq_k)

t5 = T5RelativeBias(num_heads=8)
bias = t5(seq_q=12, seq_k=12)
print('Bias shape:', bias.shape)
print('Parameters:', sum(p.numel() for p in t5.parameters()))
buckets = [t5._bucket(torch.tensor(d)).item() for d in range(10)]
print('Buckets for distances 0-9:', buckets)
print('Log-spacing: many buckets for small distances, fewer for large.')
```

> **T5 Bias vs Shaw Embedding: Key Trade-offs**: Shaw et al. use a full d_model-dimensional vector per distance (high expressiveness, high cost); T5 uses a single scalar per head per bucket (low cost, good generalisation). T5 buckets are log-spaced — 16 exact buckets for distances 0-15, then 16 log-spaced buckets for 16-128+. This choice reflects the linguistic prior that local context (nearby tokens) is more distance-sensitive than distant context. T5 relative bias is added to every attention layer's logits using the same shared weight table, not separate tables per layer.

## DeBERTa — Disentangled Attention Mechanism

He et al. (2021) introduced DeBERTa with disentangled attention: each token is represented by two vectors — a content vector and a position vector — and the attention score is decomposed into three terms: content-to-content (standard dot product), content-to-position (query content attending to key positions), and position-to-content (query positions attending to key content). This richer interaction allows the model to separately learn what a token means and where it is. The position embeddings are relative: token at position i uses the embedding for distance (j - i) when computing its score against position j, making the scheme naturally relative and enabling length generalisation. DeBERTa omits the position-to-position term as empirically less useful.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DisentangledAttention(nn.Module):
    # DeBERTa (He et al. 2021): content-to-content + content-to-position.
    def __init__(self, d_model, num_heads, max_rel=128):
        super().__init__()
        self.dk      = d_model // num_heads
        self.h       = num_heads
        self.Wq      = nn.Linear(d_model, d_model, bias=False)
        self.Wk      = nn.Linear(d_model, d_model, bias=False)
        self.Wp      = nn.Embedding(2 * max_rel + 1, d_model)
        self.max_rel = max_rel

    def forward(self, x):
        b, n, d = x.shape
        Q = self.Wq(x).view(b, n, self.h, self.dk).transpose(1, 2)
        K = self.Wk(x).view(b, n, self.h, self.dk).transpose(1, 2)
        c2c = Q @ K.transpose(-2, -1) / self.dk ** 0.5
        i   = torch.arange(n).unsqueeze(1)
        j   = torch.arange(n).unsqueeze(0)
        idx = (j - i).clamp(-self.max_rel, self.max_rel) + self.max_rel
        P   = self.Wp(idx)                         # (n, n, d_model)
        P   = P.view(n, n, self.h, self.dk).permute(2, 0, 1, 3)
        c2p = (Q.unsqueeze(-2) * P).sum(-1) / self.dk ** 0.5
        return F.softmax(c2c + c2p, dim=-1)

torch.manual_seed(3)
da   = DisentangledAttention(d_model=64, num_heads=4, max_rel=16)
x    = torch.randn(2, 8, 64)
attn = da(x)
print('Attention shape:', attn.shape)
print('c2c = content-to-content; c2p = content-to-position.')
print('DeBERTa uses only c2c + c2p (not p2c) in this simplified version.')
```

## Length Generalisation — Relative vs Absolute

Relative PE schemes generalise better to sequences longer than the training maximum because the distance vocabulary (0, 1, …, max_dist) appears throughout training regardless of absolute position. A model trained on 64-token sequences sees distances 0–63; testing on 128-token sequences introduces new distances (64–127) but the existing distances still operate correctly. In contrast, absolute PE models have no embedding for position 128 if they were trained with max_seq_len=64. The following code measures how consistently PE schemes distinguish consecutive positions across different test lengths.

```python
import torch
import torch.nn as nn
import math

def sinusoidal_pe(seq_len, d_model):
    pe  = torch.zeros(seq_len, d_model)
    pos = torch.arange(seq_len).float().unsqueeze(1)
    div = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(pos * div)
    pe[:, 1::2] = torch.cos(pos * div)
    return pe

def avg_consecutive_distance(pe):
    return (pe[1:] - pe[:-1]).norm(dim=-1).mean().item()

train_len, d_model = 64, 128
sin_train = sinusoidal_pe(train_len, d_model)
learned   = nn.Embedding(train_len, d_model)
nn.init.normal_(learned.weight, std=0.02)

print('Extrapolation comparison (train_len=64)')
print('{:>10} {:>14} {:>14}'.format('test_len', 'sinusoidal', 'learned'))
for test_len in [32, 64, 96, 128, 192]:
    sin_test = sinusoidal_pe(test_len, d_model)
    sin_dist = avg_consecutive_distance(sin_test)
    ids      = torch.arange(test_len).clamp(0, train_len - 1)
    lrn_pe   = learned(ids).detach()
    lrn_dist = avg_consecutive_distance(lrn_pe)
    print('{:>10} {:>14.4f} {:>14.4f}'.format(test_len, sin_dist, lrn_dist))
print('Learned dist collapses at positions > train_len; sinusoidal stays stable.')
```

## Transformer-XL and Segment Recurrence

Dai et al. (2019) introduced Transformer-XL with a relative PE variant designed for segment recurrence: during training, cached hidden states from previous segments are appended as additional keys and values. Absolute position embeddings break here because a token at absolute position 5 in segment t has a different positional relationship to segment t-1 tokens than to its own segment. Transformer-XL's relative PE directly computes sinusoidally-derived distance vectors at attention time, allowing the model to correctly encode 'this token is 150 positions before me in the context' even when the context spans multiple cached segments.

- Transformer-XL: sinusoidal-derived relative PE computed at attention time, enables recurrent memory
- Shaw et al.: learned vector r_{j-i} added to query in attention score, max distance clipped
- T5: scalar bias b_{j-i} per head, log-spaced buckets, shared across all layers
- DeBERTa: disentangled content + position vectors, c2c + c2p interaction terms
- All relative methods share a key property: the position signal depends on (j-i) not on j or i individually

## Comparison and Practical Guidance

| Method | Extrapolation | Parameters | Shared Weights | Complexity | Used In |
| --- | --- | --- | --- | --- | --- |
| Absolute PE | Poor — hard limit at max_seq_len | max_len×d_model or 0 | N/A | O(n) | BERT, GPT-2 (historical) |
| Shaw et al. | Better — distances generalise | (2×max_rel+1)×d_model | Clipped distances share boundary | O(n²d) | Music Transformer, some BERT variants |
| T5 Relative Bias | Good — buckets cover large dist | num_buckets×num_heads (tiny) | Log-spaced buckets shared per layer | O(n²) | T5, UL2, Flan-T5 |
| DeBERTa | Good — relative by design | (2×max_rel+1)×d_model | Position embeddings shared | O(n²d) | DeBERTa-v1/v2/v3, mDeBERTa |

For encoder-only models (classification, NLU) where sequences stay within a moderate length, T5-style relative bias offers an excellent cost-quality balance — minimal parameters and strong generalisation. For large autoregressive decoders, RoPE (not in this table) is the current standard because it operates on rotated query-key vectors with zero extra parameters. DeBERTa is the strongest performer for BERT-style pre-training at moderate sequence lengths. Shaw et al. is largely superseded by the simpler T5 bias and the more powerful DeBERTa approach.

---

