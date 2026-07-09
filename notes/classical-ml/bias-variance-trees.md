---
title: "Bias-Variance in Decision Trees"
slug: "bias-variance-trees"
description: "Explore how tree depth controls the bias-variance tradeoff, demonstrate tree instability as a symptom of high variance, and show how ensembles (bagging, boosting) address each component independently."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVjaXNpb24gdHJlZXMgcHJvdmlkZSBvbmUgb2YgdGhlIGNsZWFyZXN0IGlsbHVzdHJhdGlvbnMgb2YgdGhlIGJpYXMtdmFyaWFuY2UgdHJhZGVvZmYgaW4gbWFjaGluZSBsZWFybmluZy4gQSBmdWxseSBncm93biB0cmVlIG1lbW9yaXNlcyB0aGUgdHJhaW5pbmcgZGF0YSBwZXJmZWN0bHkgKHplcm8gYmlhcywgZXh0cmVtZSB2YXJpYW5jZSksIHdoaWxlIGEgc2hhbGxvdyB0cmVlIGNhbiBvbmx5IHJlcHJlc2VudCBjb2Fyc2UgZGVjaXNpb24gcnVsZXMgKGhpZ2ggYmlhcywgbG93IHZhcmlhbmNlKS4gVW5kZXJzdGFuZGluZyB0aGlzIHRyYWRlb2ZmIGluIHRyZWVzIOKAlCBhbmQgd2h5IGl0IG1vdGl2YXRlcyBlbnNlbWJsZSBtZXRob2RzIOKAlCBpcyBmb3VuZGF0aW9uYWwgdG8gdW5kZXJzdGFuZGluZyByYW5kb20gZm9yZXN0cywgZ3JhZGllbnQgYm9vc3RpbmcsIGFuZCBtb2Rlcm4gZW5zZW1ibGUgdGVjaG5pcXVlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGdWxseSBHcm93biBUcmVlcyDigJQgWmVybyBCaWFzLCBNYXhpbXVtIFZhcmlhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGRlY2lzaW9uIHRyZWUgZ3Jvd24gdG8gZnVsbCBkZXB0aCB3aWxsIGNyZWF0ZSBhIHVuaXF1ZSBsZWFmIGZvciBldmVyeSB0cmFpbmluZyBzYW1wbGUgKG9yIHNtYWxsIGdyb3VwIG9mIGlkZW50aWNhbCBzYW1wbGVzKS4gSXRzIHRyYWluaW5nIGVycm9yIGlzIHplcm8gb3IgbmVhci16ZXJvIOKAlCBpdCBoYXMgbWVtb3Jpc2VkIHRoZSBsYWJlbHMgcGVyZmVjdGx5LiBIb3dldmVyLCBhbnkgc21hbGwgcGVydHVyYmF0aW9uIHRvIHRoZSB0cmFpbmluZyBkYXRhIOKAlCBzd2FwcGluZyBhIGZldyBzYW1wbGVzLCBhZGRpbmcgbm9pc2UsIG9yIGRyYXdpbmcgYSBkaWZmZXJlbnQgYm9vdHN0cmFwIHNhbXBsZSDigJQgd2lsbCBwcm9kdWNlIGEgY29tcGxldGVseSBkaWZmZXJlbnQgdHJlZSBzdHJ1Y3R1cmUuIFRoaXMgZXh0cmVtZSBzZW5zaXRpdml0eSB0byB0aGUgdHJhaW5pbmcgZGF0YSBpcyB0aGUgZGVmaW5pdGlvbiBvZiBoaWdoIHZhcmlhbmNlLiBJbiB0aGUgYmlhcy12YXJpYW5jZSBkZWNvbXBvc2l0aW9uIEVbKHktxbcpwrJdID0gQmlhc8KyICsgVmFyICsgz4PCsiwgdGhlIHZhcmlhbmNlIHRlcm0gZG9taW5hdGVzIGZvciB1bnBydW5lZCB0cmVlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmVlIEluc3RhYmlsaXR5IOKAlCBIaWdoIFZhcmlhbmNlIGluIEFjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJlZSBpbnN0YWJpbGl0eSBpcyB0aGUgbW9zdCBpbnR1aXRpdmUgc3ltcHRvbSBvZiBoaWdoIHZhcmlhbmNlOiB0d28gdHJlZXMgdHJhaW5lZCBvbiBuZWFybHkgaWRlbnRpY2FsIGRhdGFzZXRzIGxvb2sgc3RydWN0dXJhbGx5IHZlcnkgZGlmZmVyZW50LiBUaGlzIGhhcHBlbnMgYmVjYXVzZSBzcGxpdHMgbmVhciB0aGUgdG9wIG9mIHRoZSB0cmVlIGFyZSBjaG9zZW4gZ3JlZWRpbHkg4oCUIGEgc21hbGwgZGlmZmVyZW5jZSBpbiB0aGUgdHJhaW5pbmcgc2FtcGxlIGNhbiBmbGlwIHRoZSBjaG9pY2Ugb2YgdGhlIHJvb3Qgc3BsaXQsIGNhc2NhZGluZyBpbnRvIGEgY29tcGxldGVseSBkaWZmZXJlbnQgdHJlZSBzdHJ1Y3R1cmUgYmVsb3cuIEluIGNvbnRyYXN0LCBsb2dpc3RpYyByZWdyZXNzaW9uIGNvZWZmaWNpZW50cyBjaGFuZ2Ugb25seSBzbGlnaHRseSB3aGVuIGEgZmV3IHNhbXBsZXMgYXJlIHBlcnR1cmJlZCDigJQgYSBzdGFibGUsIGxvdy12YXJpYW5jZSBtb2RlbC4gVGhpcyBpbnN0YWJpbGl0eSBpcyB3aGF0IG1ha2VzIHNpbmdsZSB0cmVlcyB1bnN1aXRhYmxlIGZvciBoaWdoLXN0YWtlcyBkZWNpc2lvbnMgYnV0IG1vdGl2YXRlcyBwb3dlcmZ1bCBlbnNlbWJsZSBtZXRob2RzIHRoYXQgYXZlcmFnZSBvdmVyIG1hbnkgdW5zdGFibGUgdHJlZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnRyZWUgaW1wb3J0IERlY2lzaW9uVHJlZUNsYXNzaWZpZXJcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKG5fc2FtcGxlcz0yMDAsIG5fZmVhdHVyZXM9OCwgbl9pbmZvcm1hdGl2ZT00LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5fcmVkdW5kYW50PTIsIHJhbmRvbV9zdGF0ZT00Milcblxucm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKDApXG5uID0gbGVuKFgpXG50cmVlcyA9IFtdXG5mb3IgdHJpYWwgaW4gcmFuZ2UoMik6XG4gICAgaWR4ID0gcm5nLmNob2ljZShuLCBuLCByZXBsYWNlPVRydWUpICAjIGJvb3RzdHJhcCByZXNhbXBsZVxuICAgIGR0ID0gRGVjaXNpb25UcmVlQ2xhc3NpZmllcihtYXhfZGVwdGg9NCwgcmFuZG9tX3N0YXRlPXRyaWFsKVxuICAgIGR0LmZpdChYW2lkeF0sIHlbaWR4XSlcbiAgICB0cmVlcy5hcHBlbmQoZHQpXG4gICAgcHJpbnQoZlx1MDAyN0Jvb3RzdHJhcCB7dHJpYWwrMX06IHJvb3RfZmVhdHVyZT17ZHQudHJlZV8uZmVhdHVyZVswXX0sIFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjd0aHJlc2hvbGQ9e2R0LnRyZWVfLnRocmVzaG9sZFswXTouM2Z9LCBsZWF2ZXM9e2R0LmdldF9uX2xlYXZlcygpfVx1MDAyNylcblxuIyBNZWFzdXJlIHByZWRpY3Rpb24gZGlzYWdyZWVtZW50IG9uIHVuc2VlbiBkYXRhXG5YX3Rlc3QgPSBybmcucmFuZG4oNTAwLCA4KVxuZGlzYWdyZWVtZW50ID0gbnAubWVhbih0cmVlc1swXS5wcmVkaWN0KFhfdGVzdCkgIT0gdHJlZXNbMV0ucHJlZGljdChYX3Rlc3QpKVxucHJpbnQoZlx1MDAyN1ByZWRpY3Rpb24gZGlzYWdyZWVtZW50IG9uIHVuc2VlbiBkYXRhOiB7ZGlzYWdyZWVtZW50Oi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVwdGggYXMgdGhlIFByaW1hcnkgQmlhcy1WYXJpYW5jZSBLbm9iIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmVlIGRlcHRoIGlzIHRoZSBzaW5nbGUgbW9zdCBpbXBvcnRhbnQgaHlwZXJwYXJhbWV0ZXIgY29udHJvbGxpbmcgdGhlIGJpYXMtdmFyaWFuY2UgdHJhZGVvZmYgaW4gZGVjaXNpb24gdHJlZXMuIFNoYWxsb3cgdHJlZXMgKGRlcHRoIDHigJMyKTogaGlnaCBiaWFzIGJlY2F1c2UgdGhleSBjYW4gb25seSBwYXJ0aXRpb24gdGhlIGZlYXR1cmUgc3BhY2UgaW50byAy4oCTNCByZWdpb25zIOKAlCB0aGV5IGNhbiBvbmx5IGNhcHR1cmUgdmVyeSBjb2Fyc2UgcGF0dGVybnMuIERlZXAgdHJlZXMgKGRlcHRoIFx1MDAzZSAxMCwgdW5saW1pdGVkKTogbG93IGJpYXMgYnV0IGV4dHJlbWUgdmFyaWFuY2UuIFRoZSBvcHRpbWFsIGRlcHRoIGRlcGVuZHMgb24gdGhlIHRydWUgY29tcGxleGl0eSBvZiB0aGUgZGVjaXNpb24gYm91bmRhcnkgYW5kIHRoZSBhbW91bnQgb2YgdHJhaW5pbmcgZGF0YSDigJQgbW9yZSBkYXRhIHRvbGVyYXRlcyBkZWVwZXIgdHJlZXMgYmVjYXVzZSB2YXJpYW5jZSBkZWNyZWFzZXMgd2l0aCBuLiBPdGhlciBoeXBlcnBhcmFtZXRlcnMgbGlrZSBtaW5fc2FtcGxlc19zcGxpdCBhbmQgbWluX3NhbXBsZXNfbGVhZiBhY3QgYXMgaW5kaXJlY3QgZGVwdGggbGltaXRlcnMgYnkgc3RvcHBpbmcgc3BsaXRzIGVhcmx5IHdoZW4gbm9kZXMgYXJlIHRvbyBzbWFsbCB0byBiZSByZWxpYWJsZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4udHJlZSBpbXBvcnQgRGVjaXNpb25UcmVlUmVncmVzc29yXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCBjcm9zc192YWxfc2NvcmVcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9yZWdyZXNzaW9uXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCwgeSA9IG1ha2VfcmVncmVzc2lvbihuX3NhbXBsZXM9MzAwLCBuX2ZlYXR1cmVzPTEwLCBuX2luZm9ybWF0aXZlPTUsXG4gICAgICAgICAgICAgICAgICAgICAgICBub2lzZT0xNS4wLCByYW5kb21fc3RhdGU9NDIpXG5cbmRlcHRocyA9IHJhbmdlKDEsIDIwKVxudHJhaW5fZXJyb3JzLCBjdl9lcnJvcnMgPSBbXSwgW11cbmZvciBkZXB0aCBpbiBkZXB0aHM6XG4gICAgZHQgPSBEZWNpc2lvblRyZWVSZWdyZXNzb3IobWF4X2RlcHRoPWRlcHRoLCByYW5kb21fc3RhdGU9NDIpXG4gICAgZHQuZml0KFgsIHkpXG4gICAgdHJhaW5fbXNlID0gbnAubWVhbigoeSAtIGR0LnByZWRpY3QoWCkpKioyKVxuICAgIGN2X21zZSA9IC1jcm9zc192YWxfc2NvcmUoZHQsIFgsIHksIGN2PTUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc2NvcmluZz1cdTAwMjduZWdfbWVhbl9zcXVhcmVkX2Vycm9yXHUwMDI3KS5tZWFuKClcbiAgICB0cmFpbl9lcnJvcnMuYXBwZW5kKHRyYWluX21zZSlcbiAgICBjdl9lcnJvcnMuYXBwZW5kKGN2X21zZSlcblxuYmVzdF9kZXB0aCA9IGxpc3QoZGVwdGhzKVtucC5hcmdtaW4oY3ZfZXJyb3JzKV1cbnByaW50KGZcdTAwMjd7XHUwMDI3RGVwdGhcdTAwMjc6XHUwMDNlNn0ge1x1MDAyN1RyYWluIE1TRVx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0NWIE1TRVx1MDAyNzpcdTAwM2UxMH1cdTAwMjcpXG5mb3IgZCwgdHIsIGN2IGluIHppcChkZXB0aHMsIHRyYWluX2Vycm9ycywgY3ZfZXJyb3JzKTpcbiAgICBtYXJrZXIgPSBcdTAwMjcgXHUwMDNjLS0gYmVzdCBDVlx1MDAyNyBpZiBkID09IGJlc3RfZGVwdGggZWxzZSBcdTAwMjdcdTAwMjdcbiAgICBwcmludChmXHUwMDI3e2Q6XHUwMDNlNn0ge3RyOlx1MDAzZTEwLjFmfSB7Y3Y6XHUwMDNlMTAuMWZ9e21hcmtlcn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmlhcy1WYXJpYW5jZSBEZWNvbXBvc2l0aW9uIHZpYSBCb290c3RyYXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIGVtcGlyaWNhbGx5IG1lYXN1cmUgYmlhcyBhbmQgdmFyaWFuY2UgZm9yIGEgdHJlZSBtb2RlbCwgd2UgcmVwZWF0ZWRseSBkcmF3IGJvb3RzdHJhcCB0cmFpbmluZyBzZXRzLCBmaXQgdGhlIG1vZGVsIG9uIGVhY2gsIGFuZCBjb2xsZWN0IHByZWRpY3Rpb25zIG9uIGEgZml4ZWQgdGVzdCBzZXQuIFRoZSBzcXVhcmVkIGJpYXMgYXQgZWFjaCB0ZXN0IHBvaW50IGlzIChtZWFuX3ByZWRpY3Rpb24gLSB0cnVlX3ZhbHVlKcKyLCBhbmQgdGhlIHZhcmlhbmNlIGlzIHRoZSB2YXJpYW5jZSBvZiBwcmVkaWN0aW9ucyBhY3Jvc3MgYm9vdHN0cmFwIHJ1bnMuIFRoaXMgZGVjb21wb3NpdGlvbiBjb25maXJtcyB0aGUgdGhlb3JldGljYWwgZXhwZWN0YXRpb246IGFzIGRlcHRoIGluY3JlYXNlcywgYmlhc8KyIGZhbGxzIGFuZCB2YXJpYW5jZSByaXNlcy4gVGhlIHRvdGFsIGV4cGVjdGVkIHRlc3QgZXJyb3IgaXMgYmlhc8KyICsgdmFyaWFuY2UgKyBpcnJlZHVjaWJsZSBub2lzZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4udHJlZSBpbXBvcnQgRGVjaXNpb25UcmVlUmVncmVzc29yXG5cbmRlZiBiaWFzX3ZhcmlhbmNlX3RyZWUobWF4X2RlcHRoLCBuX2Jvb3RzdHJhcHM9MjAwLCBuX3RyYWluPTEwMCxcbiAgICAgICAgICAgICAgICAgICAgICAgIG5fdGVzdD0zMDAsIG5vaXNlPTEuMCwgc2VlZD0wKTpcbiAgICBybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoc2VlZClcbiAgICBYX3Rlc3QgPSBucC5saW5zcGFjZSgwLCA2LCBuX3Rlc3QpLnJlc2hhcGUoLTEsIDEpXG4gICAgZl90cnVlID0gbnAuc2luKFhfdGVzdCkucmF2ZWwoKSArIDAuMyAqIFhfdGVzdC5yYXZlbCgpXG4gICAgcHJlZHMgPSBucC56ZXJvcygobl9ib290c3RyYXBzLCBuX3Rlc3QpKVxuICAgIGZvciBiIGluIHJhbmdlKG5fYm9vdHN0cmFwcyk6XG4gICAgICAgIFhfdHIgPSBybmcudW5pZm9ybSgwLCA2LCBuX3RyYWluKS5yZXNoYXBlKC0xLCAxKVxuICAgICAgICB5X3RyID0gbnAuc2luKFhfdHIpLnJhdmVsKCkgKyAwLjMgKiBYX3RyLnJhdmVsKCkgKyBybmcucmFuZG4obl90cmFpbikgKiBub2lzZVxuICAgICAgICBkdCA9IERlY2lzaW9uVHJlZVJlZ3Jlc3NvcihtYXhfZGVwdGg9bWF4X2RlcHRoKVxuICAgICAgICBkdC5maXQoWF90ciwgeV90cilcbiAgICAgICAgcHJlZHNbYl0gPSBkdC5wcmVkaWN0KFhfdGVzdClcbiAgICBiaWFzX3NxID0gbnAubWVhbigocHJlZHMubWVhbihheGlzPTApIC0gZl90cnVlKSoqMilcbiAgICB2YXJpYW5jZSA9IG5wLm1lYW4ocHJlZHMudmFyKGF4aXM9MCkpXG4gICAgcmV0dXJuIGJpYXNfc3EsIHZhcmlhbmNlLCBub2lzZSoqMlxuXG5wcmludChmXHUwMDI3e1x1MDAyN0RlcHRoXHUwMDI3Olx1MDAzZTh9IHtcdTAwMjdCaWFzXjJcdTAwMjc6XHUwMDNlMTB9IHtcdTAwMjdWYXJpYW5jZVx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN05vaXNlXHUwMDI3Olx1MDAzZTh9IHtcdTAwMjdUb3RhbFx1MDAyNzpcdTAwM2UxMH1cdTAwMjcpXG5mb3IgZCBpbiBbMSwgMiwgMywgNSwgOCwgMTUsIE5vbmVdOlxuICAgIGxhYmVsID0gc3RyKGQpIGlmIGQgZWxzZSBcdTAwMjdOb25lXHUwMDI3XG4gICAgYjIsIHYsIG56ID0gYmlhc192YXJpYW5jZV90cmVlKGQpXG4gICAgcHJpbnQoZlx1MDAyN3tsYWJlbDpcdTAwM2U4fSB7YjI6XHUwMDNlMTAuNGZ9IHt2Olx1MDAzZTEwLjRmfSB7bno6XHUwMDNlOC40Zn0ge2IyK3Yrbno6XHUwMDNlMTAuNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi50cmVlIGltcG9ydCBEZWNpc2lvblRyZWVDbGFzc2lmaWVyXG5mcm9tIHNrbGVhcm4uZW5zZW1ibGUgaW1wb3J0IFJhbmRvbUZvcmVzdENsYXNzaWZpZXJcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFjY3VyYWN5X3Njb3JlXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24obl9zYW1wbGVzPTUwMCwgbl9mZWF0dXJlcz0yMCwgbl9pbmZvcm1hdGl2ZT0xMCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX3JlZHVuZGFudD01LCByYW5kb21fc3RhdGU9NDIpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4zLCByYW5kb21fc3RhdGU9NDIpXG5cbiMgVW5wcnVuZWQgdHJlZVxuZHRfZnVsbCA9IERlY2lzaW9uVHJlZUNsYXNzaWZpZXIocmFuZG9tX3N0YXRlPTQyKVxuZHRfZnVsbC5maXQoWF90ciwgeV90cilcblxuIyBDb3N0LWNvbXBsZXhpdHkgcHJ1bmVkIHRyZWVcbnBhdGggPSBkdF9mdWxsLmNvc3RfY29tcGxleGl0eV9wcnVuaW5nX3BhdGgoWF90ciwgeV90cilcbmJlc3RfYWxwaGEgPSBwYXRoLmNjcF9hbHBoYXNbbGVuKHBhdGguY2NwX2FscGhhcykvLzJdXG5kdF9wcnVuZWQgPSBEZWNpc2lvblRyZWVDbGFzc2lmaWVyKGNjcF9hbHBoYT1iZXN0X2FscGhhLCByYW5kb21fc3RhdGU9NDIpXG5kdF9wcnVuZWQuZml0KFhfdHIsIHlfdHIpXG5cbnJmID0gUmFuZG9tRm9yZXN0Q2xhc3NpZmllcihuX2VzdGltYXRvcnM9MjAwLCByYW5kb21fc3RhdGU9NDIpXG5yZi5maXQoWF90ciwgeV90cilcblxucHJpbnQoZlx1MDAyN3tcdTAwMjdNb2RlbFx1MDAyNzoyMHN9IHtcdTAwMjdUcmFpbiBBY2NcdTAwMjc6XHUwMDNlMTB9IHtcdTAwMjdUZXN0IEFjY1x1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0xlYXZlc1x1MDAyNzpcdTAwM2U4fSB7XHUwMDI3R2FwXHUwMDI3Olx1MDAzZTh9XHUwMDI3KVxuZm9yIG5hbWUsIG1vZGVsIGluIFsoXHUwMDI3VW5wcnVuZWQgVHJlZVx1MDAyNywgZHRfZnVsbCksIChcdTAwMjdQcnVuZWQgVHJlZVx1MDAyNywgZHRfcHJ1bmVkKSwgKFx1MDAyN1JhbmRvbSBGb3Jlc3RcdTAwMjcsIHJmKV06XG4gICAgdHIgPSBhY2N1cmFjeV9zY29yZSh5X3RyLCBtb2RlbC5wcmVkaWN0KFhfdHIpKVxuICAgIHRlID0gYWNjdXJhY3lfc2NvcmUoeV90ZSwgbW9kZWwucHJlZGljdChYX3RlKSlcbiAgICBsZWF2ZXMgPSBtb2RlbC5nZXRfbl9sZWF2ZXMoKSBpZiBoYXNhdHRyKG1vZGVsLCBcdTAwMjdnZXRfbl9sZWF2ZXNcdTAwMjcpIGVsc2UgXHUwMDI3Ti9BXHUwMDI3XG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lOjIwc30ge3RyOlx1MDAzZTEwLjRmfSB7dGU6XHUwMDNlMTAuNGZ9IHtzdHIobGVhdmVzKTpcdTAwM2U4fSB7dHItdGU6XHUwMDNlOC40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJTaW5nbGUgVHJlZSBJbnRlcnByZXRhYmlsaXR5IHZzIEFjY3VyYWN5IFRyYWRlb2ZmIiwiY29udGVudCI6IkEgc2hhbGxvdyB0cmVlIChkZXB0aCDiiaQgMykgaXMgaGlnaGx5IGludGVycHJldGFibGUg4oCUIGEgYnVzaW5lc3MgYW5hbHlzdCBjYW4gdHJhY2UgYW55IHByZWRpY3Rpb24gdG8gYSBzZXF1ZW5jZSBvZiBhdCBtb3N0IDMgc2ltcGxlIHJ1bGVzLiBCdXQgYWNoaWV2aW5nIGNvbXBldGl0aXZlIGFjY3VyYWN5IG9mdGVuIHJlcXVpcmVzIGRlcHRoIFx1MDAzZSA2LCBhdCB3aGljaCBwb2ludCB0aGUgdHJlZSBpcyB0b28gbGFyZ2UgdG8gaW5zcGVjdCBtYW51YWxseS4gRW5zZW1ibGVzIChyYW5kb20gZm9yZXN0cywgZ3JhZGllbnQgYm9vc3RlZCB0cmVlcykgYWNoaWV2ZSBoaWdoIGFjY3VyYWN5IGJ1dCBzYWNyaWZpY2UgdGhpcyBpbnRlcnByZXRhYmlsaXR5LiBVc2Ugc2hhbGxvdyB0cmVlcyB3aGVuIHlvdSBuZWVkIGV4cGxhaW5hYmxlIHJ1bGVzOyB1c2UgZW5zZW1ibGVzIHdoZW4gYWNjdXJhY3kgaXMgcGFyYW1vdW50IGFuZCBpbnRlcnByZXRhYmlsaXR5IGNhbiBiZSBhcHByb3hpbWF0ZWQgd2l0aCBTSEFQLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhvdyBFbnNlbWJsZXMgRml4IHRoZSBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYWdnaW5nIChCb290c3RyYXAgQUdHcmVnYXRpbmcpIGFkZHJlc3NlcyB0aGUgdmFyaWFuY2UgcHJvYmxlbTogdHJhaW4gQiB0cmVlcyBvbiBkaWZmZXJlbnQgYm9vdHN0cmFwIHNhbXBsZXMgYW5kIGF2ZXJhZ2UgdGhlaXIgcHJlZGljdGlvbnMuIEJlY2F1c2UgZWFjaCB0cmVlIGhhcyBFW3ByZWRpY3Rpb25dIOKJiCBzYW1lIChsb3cgYmlhcyB1bmNoYW5nZWQpLCBidXQgVmFyKGF2ZXJhZ2UpID0gVmFyKHNpbmdsZSB0cmVlKS9CIGZvciB1bmNvcnJlbGF0ZWQgdHJlZXMsIGJhZ2dpbmcgZHJhbWF0aWNhbGx5IHJlZHVjZXMgdmFyaWFuY2UuIFJhbmRvbSBmb3Jlc3RzIGFkZCBmZWF0dXJlIHJhbmRvbWlzYXRpb24gYXQgZWFjaCBzcGxpdCAob25seSBhIHJhbmRvbSBzdWJzZXQgb2Ygc3FydChwKSBmZWF0dXJlcyBjb25zaWRlcmVkKSwgd2hpY2ggZGVjb3JyZWxhdGVzIHRoZSB0cmVlcyBmdXJ0aGVyIGFuZCByZWR1Y2VzIHZhcmlhbmNlIGV2ZW4gbW9yZS4gQm9vc3RpbmcgdGFrZXMgYSBkaWZmZXJlbnQgYXBwcm9hY2g6IGl0IHJlZHVjZXMgYmlhcyBieSBzZXF1ZW50aWFsbHkgZml0dGluZyB3ZWFrIGxlYXJuZXJzIHRvIHRoZSByZXNpZHVhbHMsIGF0IHNvbWUgY29zdCB0byB2YXJpYW5jZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBbHRlcm5hdGl2ZSBTdG9wcGluZyBDcml0ZXJpYSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmV5b25kIG1heF9kZXB0aCwgZGVjaXNpb24gdHJlZXMgb2ZmZXIgc2V2ZXJhbCBzdG9wcGluZyBjcml0ZXJpYSB0aGF0IGluZGlyZWN0bHkgY29udHJvbCB0aGUgYmlhcy12YXJpYW5jZSB0cmFkZW9mZi4gbWluX3NhbXBsZXNfc3BsaXQ6IGEgbm9kZSBtdXN0IGhhdmUgYXQgbGVhc3QgdGhpcyBtYW55IHNhbXBsZXMgdG8gYmUgc3BsaXQ7IHByZXZlbnRzIGZpdHRpbmcgdG8gdmVyeSBzbWFsbCwgbm9pc3kgc3Vic2V0cy4gbWluX3NhbXBsZXNfbGVhZjogZWFjaCBsZWFmIG11c3QgY29udGFpbiBhdCBsZWFzdCB0aGlzIG1hbnkgc2FtcGxlczsgbW9yZSBkaXJlY3RseSBjb250cm9scyBsZWFmIHNpemUgYW5kIHN0YWJpbGl0eS4gbWF4X2xlYWZfbm9kZXM6IGxpbWl0cyB0b3RhbCBsZWF2ZXMgcmF0aGVyIHRoYW4gZGVwdGgsIGFsbG93aW5nIGFzeW1tZXRyaWMgdHJlZXMgdG8gZ3JvdyBkZWVwZXIgd2hlcmUgZGF0YSBpcyBkZW5zZS4gbWluX2ltcHVyaXR5X2RlY3JlYXNlOiBvbmx5IHNwbGl0IGlmIHRoZSBpbXB1cml0eSByZWR1Y3Rpb24gZXhjZWVkcyBhIHRocmVzaG9sZCDigJQgYSBjb3N0LWJlbmVmaXQgc3RvcHBpbmcgcnVsZS4gSW4gcHJhY3RpY2UsIG1pbl9zYW1wbGVzX2xlYWY9MTDigJMzMCBpcyBhIHJvYnVzdCBhbHRlcm5hdGl2ZSB0byB0dW5pbmcgbWF4X2RlcHRoIGRpcmVjdGx5LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJEZXB0aCIsIkJpYXMiLCJWYXJpYW5jZSIsIkludGVycHJldGFiaWxpdHkiLCJOb3RlcyJdLCJyb3dzIjpbWyIx4oCTMiAoc3R1bXApIiwiVmVyeSBoaWdoIiwiVmVyeSBsb3ciLCJFeGNlbGxlbnQg4oCUIDLigJM0IHJ1bGVzIiwiT25seSBjYXB0dXJlcyBzaW1wbGUgbGluZWFyLWxpa2Ugc3BsaXRzIl0sWyIz4oCTNSAoc2hhbGxvdykiLCJNb2RlcmF0ZSIsIkxvdyIsIkdvb2Qg4oCUIGZpdHMgb24gb25lIHBhZ2UiLCJHb29kIGJhbGFuY2UgZm9yIHRhYnVsYXIgZGF0YSB3aXRoIG4gXHUwMDNjIDEwMDAiXSxbIjbigJMxMCAobWVkaXVtKSIsIkxvdyIsIk1vZGVyYXRlIiwiUG9vciDigJQgdG9vIG1hbnkgcGF0aHMiLCJUeXBpY2FsIG9wdGltYWwgcmFuZ2UgZm9yIHNpbmdsZSB0cmVlcyJdLFsiVW5saW1pdGVkIChmdWxsKSIsIk5lYXIgemVybyIsIlZlcnkgaGlnaCIsIlVudXNhYmxlIiwiTWVtb3Jpc2VzIHRyYWluaW5nIGRhdGE7IHVzZSBvbmx5IGluc2lkZSBlbnNlbWJsZXMiXSxbIlBydW5lZCAoQ0NQKSIsIk1vZGVyYXRlIiwiTG93LW1vZGVyYXRlIiwiQmV0dGVyIHRoYW4gZnVsbCIsIkNvc3QtY29tcGxleGl0eSBwcnVuaW5nIGZpbmRzIGdvb2QgYmlhcy12YXIgYmFsYW5jZSBhdXRvbWF0aWNhbGx5Il1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVzZSBtYXhfZGVwdGg9My01IGZvciBpbnRlcnByZXRhYmxlIHJ1bGVzOyB1c2UgZW5zZW1ibGVzIHdoZW4gYWNjdXJhY3kgbWF0dGVycyBtb3JlLiIsIm1pbl9zYW1wbGVzX2xlYWYgaXMgb2Z0ZW4gbW9yZSBzdGFibGUgdGhhbiBtYXhfZGVwdGggZm9yIGNvbnRyb2xsaW5nIG92ZXJmaXR0aW5nIGluIHByYWN0aWNlLiIsIlRyZWUgaW5zdGFiaWxpdHkgKGRpZmZlcmVudCBzdHJ1Y3R1cmUgZnJvbSBzbWFsbCBkYXRhIGNoYW5nZXMpIGlzIHRoZSBjbGVhcmVzdCBoaWdoLXZhcmlhbmNlIHNpZ25hbC4iLCJCYWdnaW5nIHJlZHVjZXMgdmFyaWFuY2UgcHJvcG9ydGlvbmFsbHkgdG8gdGhlIG51bWJlciBvZiB0cmVlcyBhbmQgdGhlaXIgZGVjb3JyZWxhdGlvbi4iLCJCb29zdGluZyByZWR1Y2VzIGJpYXMgYnkgZml0dGluZyByZXNpZHVhbHM7IHNocmlua2FnZSAoc21hbGwgbGVhcm5pbmcgcmF0ZSkgYWRkaXRpb25hbGx5IHJlZHVjZXMgdmFyaWFuY2UuIiwiRm9yIGZlYXR1cmUgaW1wb3J0YW5jZSBmcm9tIHRyZWVzLCBwcmVmZXIgcGVybXV0YXRpb24gaW1wb3J0YW5jZSBvdmVyIEdpbmkgaW1wb3J0YW5jZSAobGVzcyBiaWFzZWQgdG93YXJkIGhpZ2gtY2FyZGluYWxpdHkgZmVhdHVyZXMpLiIsIkNvc3QtY29tcGxleGl0eSBwcnVuaW5nIChjY3BfYWxwaGEpIGF1dG9tYXRpY2FsbHkgc2VsZWN0cyB0aGUgZGVwdGggdGhhdCBiYWxhbmNlcyB0cmFpbmluZyBmaXQgYW5kIGxlYWYgc2l6ZS4iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgYmlhcy12YXJpYW5jZSBsZW5zIG1ha2VzIGRlY2lzaW9uIHRyZWVzIHBhcnRpY3VsYXJseSBpbnN0cnVjdGl2ZTogdGhleSBhcmUgdGhlIHNpbXBsZXN0IG1vZGVsIHdoZXJlIHlvdSBjYW4gZGlyZWN0bHkgb2JzZXJ2ZSBib3RoIGZhaWx1cmUgbW9kZXMuIEEgc3R1bXAgY2xlYXJseSB1bmRlcmZpdHMgKGNhbm5vdCBjYXB0dXJlIG5vbmxpbmVhciBwYXR0ZXJucyk7IGFuIHVucHJ1bmVkIHRyZWUgY2xlYXJseSBvdmVyZml0cyAoY2Fubm90IGdlbmVyYWxpc2UgYmV5b25kIGl0cyB0cmFpbmluZyBzYW1wbGVzKS4gVGhlIGdhcCBiZXR3ZWVuIHRoZXNlIGV4dHJlbWVzIOKAlCBhbmQgd2h5IGF2ZXJhZ2luZyBvdmVyIG1hbnkgdW5zdGFibGUgdHJlZXMgcmVzb2x2ZXMgaXQg4oCUIGlzIHRoZSBjb3JlIGludHVpdGlvbiBiZWhpbmQgdGhlIG1vc3QgcG93ZXJmdWwgdGFidWxhciBNTCBtZXRob2RzIHRvZGF5LiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Bias-Variance in Decision Trees

Decision trees provide one of the clearest illustrations of the bias-variance tradeoff in machine learning. A fully grown tree memorises the training data perfectly (zero bias, extreme variance), while a shallow tree can only represent coarse decision rules (high bias, low variance). Understanding this tradeoff in trees — and why it motivates ensemble methods — is foundational to understanding random forests, gradient boosting, and modern ensemble techniques.

## Fully Grown Trees — Zero Bias, Maximum Variance

A decision tree grown to full depth will create a unique leaf for every training sample (or small group of identical samples). Its training error is zero or near-zero — it has memorised the labels perfectly. However, any small perturbation to the training data — swapping a few samples, adding noise, or drawing a different bootstrap sample — will produce a completely different tree structure. This extreme sensitivity to the training data is the definition of high variance. In the bias-variance decomposition E[(y-ŷ)²] = Bias² + Var + σ², the variance term dominates for unpruned trees.

## Tree Instability — High Variance in Action

Tree instability is the most intuitive symptom of high variance: two trees trained on nearly identical datasets look structurally very different. This happens because splits near the top of the tree are chosen greedily — a small difference in the training sample can flip the choice of the root split, cascading into a completely different tree structure below. In contrast, logistic regression coefficients change only slightly when a few samples are perturbed — a stable, low-variance model. This instability is what makes single trees unsuitable for high-stakes decisions but motivates powerful ensemble methods that average over many unstable trees.

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

np.random.seed(42)
X, y = make_classification(n_samples=200, n_features=8, n_informative=4,
                            n_redundant=2, random_state=42)

rng = np.random.RandomState(0)
n = len(X)
trees = []
for trial in range(2):
    idx = rng.choice(n, n, replace=True)  # bootstrap resample
    dt = DecisionTreeClassifier(max_depth=4, random_state=trial)
    dt.fit(X[idx], y[idx])
    trees.append(dt)
    print(f'Bootstrap {trial+1}: root_feature={dt.tree_.feature[0]}, '
          f'threshold={dt.tree_.threshold[0]:.3f}, leaves={dt.get_n_leaves()}')

# Measure prediction disagreement on unseen data
X_test = rng.randn(500, 8)
disagreement = np.mean(trees[0].predict(X_test) != trees[1].predict(X_test))
print(f'Prediction disagreement on unseen data: {disagreement:.3f}')
```

## Depth as the Primary Bias-Variance Knob

Tree depth is the single most important hyperparameter controlling the bias-variance tradeoff in decision trees. Shallow trees (depth 1–2): high bias because they can only partition the feature space into 2–4 regions — they can only capture very coarse patterns. Deep trees (depth > 10, unlimited): low bias but extreme variance. The optimal depth depends on the true complexity of the decision boundary and the amount of training data — more data tolerates deeper trees because variance decreases with n. Other hyperparameters like min_samples_split and min_samples_leaf act as indirect depth limiters by stopping splits early when nodes are too small to be reliable.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_regression

np.random.seed(42)
X, y = make_regression(n_samples=300, n_features=10, n_informative=5,
                        noise=15.0, random_state=42)

depths = range(1, 20)
train_errors, cv_errors = [], []
for depth in depths:
    dt = DecisionTreeRegressor(max_depth=depth, random_state=42)
    dt.fit(X, y)
    train_mse = np.mean((y - dt.predict(X))**2)
    cv_mse = -cross_val_score(dt, X, y, cv=5,
                               scoring='neg_mean_squared_error').mean()
    train_errors.append(train_mse)
    cv_errors.append(cv_mse)

best_depth = list(depths)[np.argmin(cv_errors)]
print(f'{'Depth':>6} {'Train MSE':>10} {'CV MSE':>10}')
for d, tr, cv in zip(depths, train_errors, cv_errors):
    marker = ' <-- best CV' if d == best_depth else ''
    print(f'{d:>6} {tr:>10.1f} {cv:>10.1f}{marker}')
```

## Bias-Variance Decomposition via Bootstrap

To empirically measure bias and variance for a tree model, we repeatedly draw bootstrap training sets, fit the model on each, and collect predictions on a fixed test set. The squared bias at each test point is (mean_prediction - true_value)², and the variance is the variance of predictions across bootstrap runs. This decomposition confirms the theoretical expectation: as depth increases, bias² falls and variance rises. The total expected test error is bias² + variance + irreducible noise.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

def bias_variance_tree(max_depth, n_bootstraps=200, n_train=100,
                        n_test=300, noise=1.0, seed=0):
    rng = np.random.RandomState(seed)
    X_test = np.linspace(0, 6, n_test).reshape(-1, 1)
    f_true = np.sin(X_test).ravel() + 0.3 * X_test.ravel()
    preds = np.zeros((n_bootstraps, n_test))
    for b in range(n_bootstraps):
        X_tr = rng.uniform(0, 6, n_train).reshape(-1, 1)
        y_tr = np.sin(X_tr).ravel() + 0.3 * X_tr.ravel() + rng.randn(n_train) * noise
        dt = DecisionTreeRegressor(max_depth=max_depth)
        dt.fit(X_tr, y_tr)
        preds[b] = dt.predict(X_test)
    bias_sq = np.mean((preds.mean(axis=0) - f_true)**2)
    variance = np.mean(preds.var(axis=0))
    return bias_sq, variance, noise**2

print(f'{'Depth':>8} {'Bias^2':>10} {'Variance':>10} {'Noise':>8} {'Total':>10}')
for d in [1, 2, 3, 5, 8, 15, None]:
    label = str(d) if d else 'None'
    b2, v, nz = bias_variance_tree(d)
    print(f'{label:>8} {b2:>10.4f} {v:>10.4f} {nz:>8.4f} {b2+v+nz:>10.4f}')
```

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)
X, y = make_classification(n_samples=500, n_features=20, n_informative=10,
                            n_redundant=5, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)

# Unpruned tree
dt_full = DecisionTreeClassifier(random_state=42)
dt_full.fit(X_tr, y_tr)

# Cost-complexity pruned tree
path = dt_full.cost_complexity_pruning_path(X_tr, y_tr)
best_alpha = path.ccp_alphas[len(path.ccp_alphas)//2]
dt_pruned = DecisionTreeClassifier(ccp_alpha=best_alpha, random_state=42)
dt_pruned.fit(X_tr, y_tr)

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_tr, y_tr)

print(f'{'Model':20s} {'Train Acc':>10} {'Test Acc':>10} {'Leaves':>8} {'Gap':>8}')
for name, model in [('Unpruned Tree', dt_full), ('Pruned Tree', dt_pruned), ('Random Forest', rf)]:
    tr = accuracy_score(y_tr, model.predict(X_tr))
    te = accuracy_score(y_te, model.predict(X_te))
    leaves = model.get_n_leaves() if hasattr(model, 'get_n_leaves') else 'N/A'
    print(f'{name:20s} {tr:>10.4f} {te:>10.4f} {str(leaves):>8} {tr-te:>8.4f}')
```

> **Single Tree Interpretability vs Accuracy Tradeoff**: A shallow tree (depth ≤ 3) is highly interpretable — a business analyst can trace any prediction to a sequence of at most 3 simple rules. But achieving competitive accuracy often requires depth > 6, at which point the tree is too large to inspect manually. Ensembles (random forests, gradient boosted trees) achieve high accuracy but sacrifice this interpretability. Use shallow trees when you need explainable rules; use ensembles when accuracy is paramount and interpretability can be approximated with SHAP.

## How Ensembles Fix the Problem

Bagging (Bootstrap AGGregating) addresses the variance problem: train B trees on different bootstrap samples and average their predictions. Because each tree has E[prediction] ≈ same (low bias unchanged), but Var(average) = Var(single tree)/B for uncorrelated trees, bagging dramatically reduces variance. Random forests add feature randomisation at each split (only a random subset of sqrt(p) features considered), which decorrelates the trees further and reduces variance even more. Boosting takes a different approach: it reduces bias by sequentially fitting weak learners to the residuals, at some cost to variance.

## Alternative Stopping Criteria

Beyond max_depth, decision trees offer several stopping criteria that indirectly control the bias-variance tradeoff. min_samples_split: a node must have at least this many samples to be split; prevents fitting to very small, noisy subsets. min_samples_leaf: each leaf must contain at least this many samples; more directly controls leaf size and stability. max_leaf_nodes: limits total leaves rather than depth, allowing asymmetric trees to grow deeper where data is dense. min_impurity_decrease: only split if the impurity reduction exceeds a threshold — a cost-benefit stopping rule. In practice, min_samples_leaf=10–30 is a robust alternative to tuning max_depth directly.

| Depth | Bias | Variance | Interpretability | Notes |
| --- | --- | --- | --- | --- |
| 1–2 (stump) | Very high | Very low | Excellent — 2–4 rules | Only captures simple linear-like splits |
| 3–5 (shallow) | Moderate | Low | Good — fits on one page | Good balance for tabular data with n < 1000 |
| 6–10 (medium) | Low | Moderate | Poor — too many paths | Typical optimal range for single trees |
| Unlimited (full) | Near zero | Very high | Unusable | Memorises training data; use only inside ensembles |
| Pruned (CCP) | Moderate | Low-moderate | Better than full | Cost-complexity pruning finds good bias-var balance automatically |

- Use max_depth=3-5 for interpretable rules; use ensembles when accuracy matters more.
- min_samples_leaf is often more stable than max_depth for controlling overfitting in practice.
- Tree instability (different structure from small data changes) is the clearest high-variance signal.
- Bagging reduces variance proportionally to the number of trees and their decorrelation.
- Boosting reduces bias by fitting residuals; shrinkage (small learning rate) additionally reduces variance.
- For feature importance from trees, prefer permutation importance over Gini importance (less biased toward high-cardinality features).
- Cost-complexity pruning (ccp_alpha) automatically selects the depth that balances training fit and leaf size.

The bias-variance lens makes decision trees particularly instructive: they are the simplest model where you can directly observe both failure modes. A stump clearly underfits (cannot capture nonlinear patterns); an unpruned tree clearly overfits (cannot generalise beyond its training samples). The gap between these extremes — and why averaging over many unstable trees resolves it — is the core intuition behind the most powerful tabular ML methods today.

---

