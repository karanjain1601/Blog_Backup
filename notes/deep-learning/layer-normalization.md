---
title: "Layer Normalization — Sequence Models and Pre/Post-Norm"
slug: "layer-normalization"
description: "Derive LN from first principles, contrast pre-norm vs post-norm Transformer architectures, compare BN vs LN vs RMSNorm vs GroupNorm, and analyze gradient flow across normalization methods."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGF5ZXIgTm9ybWFsaXphdGlvbiAoQmEgZXQgYWwuIDIwMTYpIG5vcm1hbGl6ZXMgYWN0aXZhdGlvbnMgYWNyb3NzIHRoZSBmZWF0dXJlIGRpbWVuc2lvbiBvZiBlYWNoIGluZGl2aWR1YWwgc2FtcGxlLCBtYWtpbmcgaXQgYmF0Y2gtc2l6ZSBpbmRlcGVuZGVudCBhbmQgY29uc2lzdGVudCBiZXR3ZWVuIHRyYWluaW5nIGFuZCBpbmZlcmVuY2UuIFVubGlrZSBCYXRjaCBOb3JtYWxpemF0aW9uIHdoaWNoIG5vcm1hbGl6ZXMgYWNyb3NzIHRoZSBiYXRjaCBkaW1lbnNpb24sIExOIG9wZXJhdGVzIG9uIGVhY2ggdG9rZW5cdTAwMjdzIGZlYXR1cmUgdmVjdG9yIGluIGlzb2xhdGlvbiDigJQgYSBwcm9wZXJ0eSB0aGF0IG1ha2VzIGl0IHRoZSBzdGFuZGFyZCBub3JtYWxpemF0aW9uIGNob2ljZSBmb3IgVHJhbnNmb3JtZXJzLCBSTk5zLCBhbmQgYW55IGFyY2hpdGVjdHVyZSBwcm9jZXNzaW5nIHZhcmlhYmxlLWxlbmd0aCBzZXF1ZW5jZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGF5ZXIgTm9ybWFsaXphdGlvbiBGb3JtdWxhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYW4gaW5wdXQgdmVjdG9yIHgg4oiIIOKEneG1iCwgTGF5ZXIgTm9ybWFsaXphdGlvbiBjb21wdXRlczogzrwgPSAoMS9kKSDOo+G1oiB44bWiIChtZWFuIG92ZXIgZmVhdHVyZSBkaW0pLCDPg8KyID0gKDEvZCkgzqPhtaIgKHjhtaIg4oiSIM68KcKyICh2YXJpYW5jZSBvdmVyIGZlYXR1cmUgZGltKSwgeMyC4bWiID0gKHjhtaIg4oiSIM68KSAvIOKImijPg8KyICsgzrUpIChub3JtYWxpemUpLCB54bWiID0gzrPhtaIgeMyC4bWiICsgzrLhtaIgKHNjYWxlIGFuZCBzaGlmdCkuIFRoZSBsZWFybmVkIHBhcmFtZXRlcnMgzrMgKHNjYWxlKSBhbmQgzrIgKHNoaWZ0KSBoYXZlIHRoZSBzYW1lIGRpbWVuc2lvbiBhcyB0aGUgZmVhdHVyZSB2ZWN0b3IsIGdpdmluZyB0aGUgbW9kZWwgZnJlZWRvbSB0byB1bmRvIHRoZSBub3JtYWxpemF0aW9uIGlmIGJlbmVmaWNpYWwuIM61IGlzIGEgc21hbGwgY29uc3RhbnQgKHR5cGljYWxseSAxZS01KSBmb3IgbnVtZXJpY2FsIHN0YWJpbGl0eS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgbGF5ZXJfbm9ybV9udW1weSh4LCBnYW1tYSwgYmV0YSwgZXBzPTFlLTUpOlxuICAgICMgeDogKC4uLiwgZmVhdHVyZXMpIOKAlCBub3JtYWxpemUgb3ZlciBsYXN0IGRpbWVuc2lvblxuICAgIG1lYW4gPSB4Lm1lYW4oYXhpcz0tMSwga2VlcGRpbXM9VHJ1ZSlcbiAgICB2YXIgPSB4LnZhcihheGlzPS0xLCBrZWVwZGltcz1UcnVlLCBkZG9mPTApXG4gICAgeF9oYXQgPSAoeCAtIG1lYW4pIC8gbnAuc3FydCh2YXIgKyBlcHMpXG4gICAgcmV0dXJuIGdhbW1hICogeF9oYXQgKyBiZXRhXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuYmF0Y2gsIHNlcSwgZmVhdHVyZXMgPSAyLCAxMCwgNjRcbnhfbnAgPSBucC5yYW5kb20ucmFuZG4oYmF0Y2gsIHNlcSwgZmVhdHVyZXMpLmFzdHlwZShucC5mbG9hdDMyKVxuZ2FtbWFfbnAgPSBucC5vbmVzKGZlYXR1cmVzLCBkdHlwZT1ucC5mbG9hdDMyKVxuYmV0YV9ucCA9IG5wLnplcm9zKGZlYXR1cmVzLCBkdHlwZT1ucC5mbG9hdDMyKVxub3V0X3NjcmF0Y2ggPSBsYXllcl9ub3JtX251bXB5KHhfbnAsIGdhbW1hX25wLCBiZXRhX25wKVxuXG54X3RvcmNoID0gdG9yY2gudGVuc29yKHhfbnApXG5sbiA9IG5uLkxheWVyTm9ybShmZWF0dXJlcylcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIGxuLndlaWdodC5maWxsXygxLjApXG4gICAgbG4uYmlhcy5maWxsXygwLjApXG5vdXRfdG9yY2ggPSBsbih4X3RvcmNoKS5kZXRhY2goKS5udW1weSgpXG5cbnByaW50KGZcdTAwMjdNYXggZGlmZiBzY3JhdGNoIHZzIFB5VG9yY2g6IHtucC5hYnMob3V0X3NjcmF0Y2ggLSBvdXRfdG9yY2gpLm1heCgpOi4yZX1cdTAwMjcpXG5wcmludChmXHUwMDI3UGVyLXRva2VuIG1lYW4gYWZ0ZXIgTE4gKHNob3VsZCB+MCk6IHtvdXRfc2NyYXRjaC5tZWFuKGF4aXM9LTEpLm1lYW4oKTouNmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1Blci10b2tlbiBzdGQgIGFmdGVyIExOIChzaG91bGQgfjEpOiB7b3V0X3NjcmF0Y2guc3RkKGF4aXM9LTEpLm1lYW4oKTouNmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhdGNoIE5vcm1hbGl6YXRpb24gdnMgTGF5ZXIgTm9ybWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmF0Y2ggTm9ybWFsaXphdGlvbiBub3JtYWxpemVzIGFjcm9zcyB0aGUgYmF0Y2ggZGltZW5zaW9uOiBmb3IgZWFjaCBmZWF0dXJlIGosIEJOIGNvbXB1dGVzIHRoZSBtZWFuIGFuZCB2YXJpYW5jZSBvdmVyIGFsbCBzYW1wbGVzIGluIHRoZSBiYXRjaC4gVGhpcyBjcmVhdGVzIHRocmVlIHByb2JsZW1zIGluIHNlcXVlbmNlIG1vZGVsaW5nOiAoMSkgc3RhdGlzdGljcyBkZXBlbmQgb24gYmF0Y2ggc2l6ZSDigJQgbm9pc3kgYXQgc21hbGwgYmF0Y2hlczsgKDIpIGRpZmZlcmVudCBjb21wdXRhdGlvbiBhdCB0cmFpbiAoYmF0Y2ggc3RhdHMpIHZzIGV2YWwgKHJ1bm5pbmcgc3RhdHMpIGNhdXNpbmcgYSB0cmFpbi9ldmFsIGdhcDsgKDMpIHZhcmlhYmxlLWxlbmd0aCBzZXF1ZW5jZXMgY2Fubm90IGJlIGJhdGNoZWQgY2xlYW5seSBzaW5jZSBwYWRkaW5nIHRva2VucyBjb3JydXB0IGJhdGNoIHN0YXRpc3RpY3MuIExOIGNvbXB1dGVzIHN0YXRpc3RpY3MgcGVyLXNhbXBsZSBvdmVyIHRoZSBmZWF0dXJlIGRpbWVuc2lvbiwgZWxpbWluYXRpbmcgYWxsIHRocmVlIHByb2JsZW1zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgY29tcGFyZV9ub3JtcyhiYXRjaF9zaXplLCBzZXFfbGVuPTEwLCBmZWF0dXJlcz0zMik6XG4gICAgeCA9IHRvcmNoLnJhbmRuKGJhdGNoX3NpemUsIHNlcV9sZW4sIGZlYXR1cmVzKVxuXG4gICAgbG4gPSBubi5MYXllck5vcm0oZmVhdHVyZXMpXG4gICAgb3V0X2xuID0gbG4oeClcbiAgICBsbl9pbmZvID0gZlx1MDAyN21lYW49e291dF9sbi5tZWFuKCk6LjNmfSwgc3RkPXtvdXRfbG4uc3RkKCk6LjNmfVx1MDAyN1xuXG4gICAgYm4gPSBubi5CYXRjaE5vcm0xZChmZWF0dXJlcylcbiAgICB4X2ZsYXQgPSB4LnJlc2hhcGUoYmF0Y2hfc2l6ZSAqIHNlcV9sZW4sIGZlYXR1cmVzKVxuICAgIHRyeTpcbiAgICAgICAgb3V0X2JuID0gYm4oeF9mbGF0KVxuICAgICAgICBibl9pbmZvID0gZlx1MDAyN21lYW49e291dF9ibi5tZWFuKCk6LjNmfSwgc3RkPXtvdXRfYm4uc3RkKCk6LjNmfVx1MDAyN1xuICAgIGV4Y2VwdCBSdW50aW1lRXJyb3IgYXMgZTpcbiAgICAgICAgYm5faW5mbyA9IGZcdTAwMjdFUlJPUjoge3N0cihlKVs6NjBdfVx1MDAyN1xuXG4gICAgcHJpbnQoZlx1MDAyNyAgYmF0Y2hfc2l6ZT17YmF0Y2hfc2l6ZX06XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgICAgTGF5ZXJOb3JtICA6IHtsbl9pbmZvfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICAgIEJhdGNoTm9ybTFkOiB7Ym5faW5mb31cdTAwMjcpXG5cbnByaW50KFx1MDAyNz09PSBOb3JtYWxpemF0aW9uIGF0IGRpZmZlcmVudCBiYXRjaCBzaXplcyA9PT1cdTAwMjcpXG5mb3IgYnMgaW4gWzgsIDQsIDIsIDFdOlxuICAgIGNvbXBhcmVfbm9ybXMoYnMpXG5wcmludChcdTAwMjdcXG5MTiBpcyBiYXRjaC1zaXplIGluZGVwZW5kZW50LiBCTiBkZWdyYWRlcyBzaGFycGx5IGF0IGJhdGNoX3NpemU9MS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJlLU5vcm0gYW5kIFBvc3QtTm9ybSBUcmFuc2Zvcm1lciBBcmNoaXRlY3R1cmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgb3JpZ2luYWwgVHJhbnNmb3JtZXIgKFZhc3dhbmkgZXQgYWwuIDIwMTcpIHVzZWQgUG9zdC1MTjogeSA9IExOKHggKyBTdWJsYXllcih4KSkuIE5vcm1hbGl6YXRpb24gaXMgYXBwbGllZCBhZnRlciB0aGUgcmVzaWR1YWwgYWRkaXRpb24uIFByZS1MTiAoR1BULTIsIExMYU1BLCBQYUxNKTogeSA9IHggKyBTdWJsYXllcihMTih4KSkuIE5vcm1hbGl6YXRpb24gaXMgYXBwbGllZCBiZWZvcmUgZWFjaCBzdWJsYXllcjsgdGhlIHJlc2lkdWFsIHN0cmVhbSBncm93cyB3aXRob3V0IGJlaW5nIGJvdW5kZWQgYnkgbm9ybWFsaXphdGlvbiwgZ2l2aW5nIG1vcmUgc3RhYmxlIGdyYWRpZW50IGZsb3cuIFByZS1MTiB0eXBpY2FsbHkgcmVxdWlyZXMgbm8gbGVhcm5pbmcgcmF0ZSB3YXJtdXAgYW5kIHRyYWlucyBtb3JlIHJlbGlhYmx5IGF0IGRlcHRoIOKJpSAyNCBsYXllcnMuIFBvc3QtTE4gY2FuIGFjaGlldmUgbWFyZ2luYWxseSBiZXR0ZXIgZmluYWwgcGVycGxleGl0eSBidXQgcmVxdWlyZXMgY2FyZWZ1bCB0dW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFByZU5vcm1CbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsLCBuaGVhZCwgZGltX2ZmKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYXR0biA9IG5uLk11bHRpaGVhZEF0dGVudGlvbihkX21vZGVsLCBuaGVhZCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5mZiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9tb2RlbCwgZGltX2ZmKSwgbm4uR0VMVSgpLCBubi5MaW5lYXIoZGltX2ZmLCBkX21vZGVsKSlcbiAgICAgICAgc2VsZi5sbjEgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5sbjIgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgbiA9IHNlbGYubG4xKHgpXG4gICAgICAgIHggPSB4ICsgc2VsZi5hdHRuKG4sIG4sIG4pWzBdXG4gICAgICAgIHggPSB4ICsgc2VsZi5mZihzZWxmLmxuMih4KSlcbiAgICAgICAgcmV0dXJuIHhcblxuY2xhc3MgUG9zdE5vcm1CbG9jayhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsLCBuaGVhZCwgZGltX2ZmKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYXR0biA9IG5uLk11bHRpaGVhZEF0dGVudGlvbihkX21vZGVsLCBuaGVhZCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5mZiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9tb2RlbCwgZGltX2ZmKSwgbm4uR0VMVSgpLCBubi5MaW5lYXIoZGltX2ZmLCBkX21vZGVsKSlcbiAgICAgICAgc2VsZi5sbjEgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICAgICAgc2VsZi5sbjIgPSBubi5MYXllck5vcm0oZF9tb2RlbClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgeCA9IHNlbGYubG4xKHggKyBzZWxmLmF0dG4oeCwgeCwgeClbMF0pXG4gICAgICAgIHggPSBzZWxmLmxuMih4ICsgc2VsZi5mZih4KSlcbiAgICAgICAgcmV0dXJuIHhcblxuZF9tb2RlbCwgbmhlYWQsIGRpbV9mZiA9IDY0LCA0LCAxMjhcbnggPSB0b3JjaC5yYW5kbigyLCAxNiwgZF9tb2RlbClcbnByZSA9IFByZU5vcm1CbG9jayhkX21vZGVsLCBuaGVhZCwgZGltX2ZmKVxucG9zdCA9IFBvc3ROb3JtQmxvY2soZF9tb2RlbCwgbmhlYWQsIGRpbV9mZilcbnByaW50KGZcdTAwMjdQcmVOb3JtICBvdXRwdXQgbm9ybToge3ByZSh4KS5ub3JtKCkuaXRlbSgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3UG9zdE5vcm0gb3V0cHV0IG5vcm06IHtwb3N0KHgpLm5vcm0oKS5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN1ByZU5vcm0gcmVzaWR1YWwgZ3Jvd3MgZnJlZWx5OyBQb3N0Tm9ybSBib3VuZGVkIGJ5IExOIGF0IGVhY2ggc3VibGF5ZXIgb3V0cHV0Llx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlByZS1Ob3JtIGlzIHRoZSBNb2Rlcm4gRGVmYXVsdCIsImNvbnRlbnQiOiJBbGwgbWFqb3IgTExNcyDigJQgR1BULTIsIEdQVC0zLCBMTGFNQSAxLzIvMywgUGFMTSwgRmFsY29uLCBNaXN0cmFsIOKAlCB1c2UgUHJlLUxOLiBQb3N0LUxOIChvcmlnaW5hbCBUcmFuc2Zvcm1lcikgY2FuIGFjaGlldmUgc2xpZ2h0bHkgYmV0dGVyIGZpbmFsIHBlcnBsZXhpdHkgYnV0IHJlcXVpcmVzIGNhcmVmdWwgd2FybXVwIHNjaGVkdWxlcyBhbmQgb2Z0ZW4gZGl2ZXJnZXMgaW4gbW9kZWxzIGRlZXBlciB0aGFuIDI0IGxheWVycy4gRm9yIG5ldyBhcmNoaXRlY3R1cmVzLCBzdGFydCB3aXRoIFByZS1MTi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaHkgTGF5ZXIgTm9ybSBSZXBsYWNlZCBCYXRjaCBOb3JtIGluIFNlcXVlbmNlIE1vZGVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhyZWUgcHJvcGVydGllcyBtYWtlIExOIHVuaXF1ZWx5IHN1aXRlZCB0byBzZXF1ZW5jZSBtb2RlbGluZzogQmF0Y2ggaW5kZXBlbmRlbmNlIOKAlCBMTiBzdGF0aXN0aWNzIGFyZSBjb21wdXRlZCBwZXItc2FtcGxlLCBzbyBub3JtYWxpemF0aW9uIGlzIGlkZW50aWNhbCBhdCBiYXRjaF9zaXplPTEgYW5kIGJhdGNoX3NpemU9NTEyLiBWYXJpYWJsZS1sZW5ndGggY29tcGF0aWJpbGl0eSDigJQgZWFjaCB0b2tlbiBpcyBub3JtYWxpemVkIHVzaW5nIG9ubHkgaXRzIG93biBmZWF0dXJlIHZlY3Rvciwgc28gc2VxdWVuY2VzIG9mIGRpZmZlcmVudCBsZW5ndGhzIGNhbiBiZSBwcm9jZXNzZWQgd2l0aG91dCBhbnkgc3BlY2lhbCBoYW5kbGluZy4gVHJhaW4vZXZhbCBjb25zaXN0ZW5jeSDigJQgTE4gdXNlcyB0aGUgc2FtZSBmb3JtdWxhIGF0IHRyYWluaW5nIGFuZCBpbmZlcmVuY2Ugd2l0aCBubyBydW5uaW5nLW1lYW4gYWNjdW11bGF0aW9uIGFuZCBubyBiZWhhdmlvcmFsIHNoaWZ0IGJldHdlZW4gbW9kZWwudHJhaW4oKSBhbmQgbW9kZWwuZXZhbCgpLiBCTiB2aW9sYXRlcyBhbGwgdGhyZWUgcHJvcGVydGllcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJhdGNoIGluZGVwZW5kZW5jZTogTE4gY29tcHV0ZXMgbWVhbi92YXIgb3ZlciB0aGUgZmVhdHVyZSBkaW0gb2YgZWFjaCBzYW1wbGUg4oCUIG5vIGJhdGNoIGNvdXBsaW5nLiIsIlZhcmlhYmxlIHNlcXVlbmNlczogcGFkZGluZyB0b2tlbnMgd291bGQgY29ycnVwdCBCTiBiYXRjaCBzdGF0aXN0aWNzOyBMTiBwcm9jZXNzZXMgZWFjaCBwb3NpdGlvbiBpbmRlcGVuZGVudGx5LiIsIk5vIHRyYWluL2V2YWwgZ2FwOiBCTiB1c2VzIGJhdGNoIHN0YXRzIGF0IHRyYWluIGFuZCBydW5uaW5nIHN0YXRzIGF0IGV2YWw7IExOIGJlaGF2aW9yIGlzIGlkZW50aWNhbCBpbiBib3RoIG1vZGVzLiIsIkNvbnNpc3RlbnQgZ3JhZGllbnQ6IExOIGdyYWRpZW50IGRlcGVuZHMgb25seSBvbiB0aGUgbG9jYWwgc2FtcGxlIOKAlCBubyBjcm9zcy1iYXRjaCBncmFkaWVudCBjb3VwbGluZyBpbiBiYWNrd2FyZCBwYXNzLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcmFkaWVudCBGbG93IFRocm91Z2ggTGF5ZXIgTm9ybSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGdyYWRpZW50IG9mIHRoZSBMTiBvdXRwdXQgd2l0aCByZXNwZWN0IHRvIHRoZSBpbnB1dCBoYXMgYSBjZW50ZXJpbmcgY29tcG9uZW50OiDiiIJML+KIgngg4oidIFviiIJML+KIgnjMgiDiiJIgbWVhbijiiIJML+KIgnjMgikg4oiSIHjMgiDCtyBtZWFuKOKIgkwv4oiCeMyCIMK3IHjMgildIC8gz4MuIFRoZSBtZWFuIHN1YnRyYWN0aW9uIHRlcm1zIHByZXZlbnQgY29uc3RhbnQgZ3JhZGllbnQgY29tcG9uZW50cyBmcm9tIGZsb3dpbmcgYmFjaywgYWN0aW5nIGFzIGFuIGltcGxpY2l0IGdyYWRpZW50IHJlZ3VsYXJpemVyLiBGb3IgQk4sIGdyYWRpZW50cyBhcmUgY291cGxlZCBhY3Jvc3MgdGhlIGJhdGNoIOKAlCBlYWNoIHNhbXBsZVx1MDAyN3MgZ3JhZGllbnQgZGVwZW5kcyBvbiBhbGwgb3RoZXJzLCB3aGljaCBjYW4gY2F1c2UgaW5zdGFiaWxpdHkgd2hlbiBiYXRjaCBzaXplIGNoYW5nZXMgYmV0d2VlbiB0cmFpbmluZyBhbmQgaW5mZXJlbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBtZWFzdXJlX2dyYWRfZmxvdyhub3JtX2NsYXNzLCBpbnB1dF9zaGFwZSwgKiprd2FyZ3MpOlxuICAgIHggPSB0b3JjaC5yYW5kbigqaW5wdXRfc2hhcGUsIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbiAgICBsYXllciA9IG5vcm1fY2xhc3MoKiprd2FyZ3MpXG4gICAgb3V0ID0gbGF5ZXIoeClcbiAgICBsb3NzID0gb3V0LnBvdygyKS5tZWFuKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICByZXR1cm4geC5ncmFkLmFicygpLm1lYW4oKS5pdGVtKCksIHguZ3JhZC5zdGQoKS5pdGVtKClcblxuQiwgVCwgQyA9IDQsIDIwLCA2NFxubG5fbWVhbiwgbG5fc3RkID0gbWVhc3VyZV9ncmFkX2Zsb3cobm4uTGF5ZXJOb3JtLCAoQiwgVCwgQyksIG5vcm1hbGl6ZWRfc2hhcGU9QylcblxuY2xhc3MgQk5TZXEobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbnVtX2ZlYXR1cmVzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYm4gPSBubi5CYXRjaE5vcm0xZChudW1fZmVhdHVyZXMpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIEIsIFQsIEMgPSB4LnNoYXBlXG4gICAgICAgIHJldHVybiBzZWxmLmJuKHgucmVzaGFwZShCICogVCwgQykpLnJlc2hhcGUoQiwgVCwgQylcblxuYm5fbWVhbiwgYm5fc3RkID0gbWVhc3VyZV9ncmFkX2Zsb3coQk5TZXEsIChCLCBULCBDKSwgbnVtX2ZlYXR1cmVzPUMpXG5cbnByaW50KGZcdTAwMjdMYXllck5vcm0gZ3JhZDogbWVhbj17bG5fbWVhbjouNmZ9LCBzdGQ9e2xuX3N0ZDouNmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0JhdGNoTm9ybSBncmFkOiBtZWFuPXtibl9tZWFuOi42Zn0sIHN0ZD17Ym5fc3RkOi42Zn1cdTAwMjcpXG5wcmludChcdTAwMjdMTiBncmFkaWVudCBpcyBwZXItc2FtcGxlIOKAlCBubyBjcm9zcy1iYXRjaCBjb3VwbGluZyBpbiB0aGUgYmFja3dhcmQgcGFzcy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRW1iZWRkaW5nIExheWVyIE5vcm1hbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vZGVybiBMTE1zIGFwcGx5IExOIHRvIHRoZSBlbWJlZGRpbmcgb3V0cHV0cyBiZWZvcmUgZmVlZGluZyB0aGVtIGludG8gdGhlIGZpcnN0IHRyYW5zZm9ybWVyIGJsb2NrLiBUaGlzIGJvdW5kcyB0aGUgc2NhbGUgb2YgdGhlIGluaXRpYWwgcmVzaWR1YWwgc3RyZWFtIGFuZCBwcmV2ZW50cyBlYXJseSBsYXllcnMgZnJvbSBzcGVuZGluZyBjYXBhY2l0eSBvbiBub3JtYWxpemF0aW9uLiBCRVJUIGFuZCBSb0JFUlRhIGFwcGx5IExOIGFmdGVyIHN1bW1pbmcgdG9rZW4gYW5kIHBvc2l0aW9uYWwgZW1iZWRkaW5ncy4gR1BULU5lb1ggdXNlcyBhIHNlcGFyYXRlIGVtYmVkZGluZyBub3JtYWxpemF0aW9uIGJlZm9yZSBhbmQgYWZ0ZXIgdGhlIGVtYmVkZGluZyBsb29rdXAuIFRoZSBMTiBwYXJhbWV0ZXJzIGF0IHRoZSBlbWJlZGRpbmcgbGF5ZXIgYXJlIGxlYXJuZWQgaW5kZXBlbmRlbnRseSBmcm9tIHRoZSBMTiBpbnNpZGUgZWFjaCB0cmFuc2Zvcm1lciBibG9jay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOb3JtYWxpemF0aW9uIE1ldGhvZHMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJOb3JtYWxpemVzIE92ZXIiLCJCYXRjaCBEZXBlbmRlbnQiLCJUcmFpbi9FdmFsIEdhcCIsIkxlYXJuYWJsZSBQYXJhbXMiLCJTdGFuZGFyZCBVc2UiXSwicm93cyI6W1siQmF0Y2hOb3JtIiwiQmF0Y2ggZGltIHBlciBjaGFubmVsIiwiWWVzIiwiWWVzIOKAlCBydW5uaW5nIHN0YXRzIGF0IGV2YWwiLCLOsywgzrIgcGVyIGNoYW5uZWwiLCJJbWFnZSBjbGFzc2lmaWNhdGlvbiAobGFyZ2UgYmF0Y2gpIl0sWyJMYXllck5vcm0iLCJGZWF0dXJlIGRpbSBwZXIgc2FtcGxlIiwiTm8iLCJObyIsIs6zLCDOsiBwZXIgZmVhdHVyZSIsIlRyYW5zZm9ybWVycywgUk5OcywgTkxQIl0sWyJSTVNOb3JtIiwiRmVhdHVyZSBkaW0gcGVyIHNhbXBsZSAobm8gbWVhbikiLCJObyIsIk5vIiwizrMgcGVyIGZlYXR1cmUgb25seSIsIkxMYU1BLCBHZW1tYSwgTWlzdHJhbCwgRmFsY29uIl0sWyJHcm91cE5vcm0iLCJXaXRoaW4gZWFjaCBjaGFubmVsIGdyb3VwIHBlciBzYW1wbGUiLCJObyIsIk5vIiwizrMsIM6yIHBlciBjaGFubmVsIiwiT2JqZWN0IGRldGVjdGlvbiwgc2VnbWVudGF0aW9uIl0sWyJJbnN0YW5jZU5vcm0iLCJTcGF0aWFsIGRpbXMgcGVyIHNhbXBsZSBwZXIgY2hhbm5lbCIsIk5vIiwiTm8iLCLOsywgzrIgcGVyIGNoYW5uZWwgKG9wdGlvbmFsKSIsIlN0eWxlIHRyYW5zZmVyLCBDeWNsZUdBTiJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDaG9vc2UgTGF5ZXJOb3JtIGZvciBhbnkgVHJhbnNmb3JtZXItYmFzZWQgYXJjaGl0ZWN0dXJlLiBVc2UgUk1TTm9ybSB3aGVuIHRyYWluaW5nIGVmZmljaWVuY3kgbWF0dGVycyBhbmQgbWVhbi1jZW50ZXJpbmcgaXMgbm90IGNyaXRpY2FsLiBVc2UgR3JvdXBOb3JtIHdoZW4gYmF0Y2ggc2l6ZXMgYXJlIHNtYWxsICjiiaQ0KSBhbmQgc3BhdGlhbCBzdHJ1Y3R1cmUgZXhpc3RzLiBVc2UgSW5zdGFuY2VOb3JtIHNwZWNpZmljYWxseSBmb3Igc3R5bGUgdHJhbnNmZXIgd2hlcmUgcmVtb3ZpbmcgcGVyLWNoYW5uZWwgc3RhdGlzdGljcyBub3JtYWxpemVzIHN0eWxlIGluZm9ybWF0aW9uLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Layer Normalization — Sequence Models and Pre/Post-Norm

Layer Normalization (Ba et al. 2016) normalizes activations across the feature dimension of each individual sample, making it batch-size independent and consistent between training and inference. Unlike Batch Normalization which normalizes across the batch dimension, LN operates on each token's feature vector in isolation — a property that makes it the standard normalization choice for Transformers, RNNs, and any architecture processing variable-length sequences.

## Layer Normalization Formula

For an input vector x ∈ ℝᵈ, Layer Normalization computes: μ = (1/d) Σᵢ xᵢ (mean over feature dim), σ² = (1/d) Σᵢ (xᵢ − μ)² (variance over feature dim), x̂ᵢ = (xᵢ − μ) / √(σ² + ε) (normalize), yᵢ = γᵢ x̂ᵢ + βᵢ (scale and shift). The learned parameters γ (scale) and β (shift) have the same dimension as the feature vector, giving the model freedom to undo the normalization if beneficial. ε is a small constant (typically 1e-5) for numerical stability.

```python
import numpy as np
import torch
import torch.nn as nn

def layer_norm_numpy(x, gamma, beta, eps=1e-5):
    # x: (..., features) — normalize over last dimension
    mean = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True, ddof=0)
    x_hat = (x - mean) / np.sqrt(var + eps)
    return gamma * x_hat + beta

np.random.seed(42)
batch, seq, features = 2, 10, 64
x_np = np.random.randn(batch, seq, features).astype(np.float32)
gamma_np = np.ones(features, dtype=np.float32)
beta_np = np.zeros(features, dtype=np.float32)
out_scratch = layer_norm_numpy(x_np, gamma_np, beta_np)

x_torch = torch.tensor(x_np)
ln = nn.LayerNorm(features)
with torch.no_grad():
    ln.weight.fill_(1.0)
    ln.bias.fill_(0.0)
out_torch = ln(x_torch).detach().numpy()

print(f'Max diff scratch vs PyTorch: {np.abs(out_scratch - out_torch).max():.2e}')
print(f'Per-token mean after LN (should ~0): {out_scratch.mean(axis=-1).mean():.6f}')
print(f'Per-token std  after LN (should ~1): {out_scratch.std(axis=-1).mean():.6f}')
```

## Batch Normalization vs Layer Normalization

Batch Normalization normalizes across the batch dimension: for each feature j, BN computes the mean and variance over all samples in the batch. This creates three problems in sequence modeling: (1) statistics depend on batch size — noisy at small batches; (2) different computation at train (batch stats) vs eval (running stats) causing a train/eval gap; (3) variable-length sequences cannot be batched cleanly since padding tokens corrupt batch statistics. LN computes statistics per-sample over the feature dimension, eliminating all three problems.

```python
import torch
import torch.nn as nn

def compare_norms(batch_size, seq_len=10, features=32):
    x = torch.randn(batch_size, seq_len, features)

    ln = nn.LayerNorm(features)
    out_ln = ln(x)
    ln_info = f'mean={out_ln.mean():.3f}, std={out_ln.std():.3f}'

    bn = nn.BatchNorm1d(features)
    x_flat = x.reshape(batch_size * seq_len, features)
    try:
        out_bn = bn(x_flat)
        bn_info = f'mean={out_bn.mean():.3f}, std={out_bn.std():.3f}'
    except RuntimeError as e:
        bn_info = f'ERROR: {str(e)[:60]}'

    print(f'  batch_size={batch_size}:')
    print(f'    LayerNorm  : {ln_info}')
    print(f'    BatchNorm1d: {bn_info}')

print('=== Normalization at different batch sizes ===')
for bs in [8, 4, 2, 1]:
    compare_norms(bs)
print('\nLN is batch-size independent. BN degrades sharply at batch_size=1.')
```

## Pre-Norm and Post-Norm Transformer Architectures

The original Transformer (Vaswani et al. 2017) used Post-LN: y = LN(x + Sublayer(x)). Normalization is applied after the residual addition. Pre-LN (GPT-2, LLaMA, PaLM): y = x + Sublayer(LN(x)). Normalization is applied before each sublayer; the residual stream grows without being bounded by normalization, giving more stable gradient flow. Pre-LN typically requires no learning rate warmup and trains more reliably at depth ≥ 24 layers. Post-LN can achieve marginally better final perplexity but requires careful tuning.

```python
import torch
import torch.nn as nn

class PreNormBlock(nn.Module):
    def __init__(self, d_model, nhead, dim_ff):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, nhead, batch_first=True)
        self.ff = nn.Sequential(
            nn.Linear(d_model, dim_ff), nn.GELU(), nn.Linear(dim_ff, d_model))
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)
    def forward(self, x):
        n = self.ln1(x)
        x = x + self.attn(n, n, n)[0]
        x = x + self.ff(self.ln2(x))
        return x

class PostNormBlock(nn.Module):
    def __init__(self, d_model, nhead, dim_ff):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, nhead, batch_first=True)
        self.ff = nn.Sequential(
            nn.Linear(d_model, dim_ff), nn.GELU(), nn.Linear(dim_ff, d_model))
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)
    def forward(self, x):
        x = self.ln1(x + self.attn(x, x, x)[0])
        x = self.ln2(x + self.ff(x))
        return x

d_model, nhead, dim_ff = 64, 4, 128
x = torch.randn(2, 16, d_model)
pre = PreNormBlock(d_model, nhead, dim_ff)
post = PostNormBlock(d_model, nhead, dim_ff)
print(f'PreNorm  output norm: {pre(x).norm().item():.4f}')
print(f'PostNorm output norm: {post(x).norm().item():.4f}')
print('PreNorm residual grows freely; PostNorm bounded by LN at each sublayer output.')
```

> **Pre-Norm is the Modern Default**: All major LLMs — GPT-2, GPT-3, LLaMA 1/2/3, PaLM, Falcon, Mistral — use Pre-LN. Post-LN (original Transformer) can achieve slightly better final perplexity but requires careful warmup schedules and often diverges in models deeper than 24 layers. For new architectures, start with Pre-LN.

## Why Layer Norm Replaced Batch Norm in Sequence Models

Three properties make LN uniquely suited to sequence modeling: Batch independence — LN statistics are computed per-sample, so normalization is identical at batch_size=1 and batch_size=512. Variable-length compatibility — each token is normalized using only its own feature vector, so sequences of different lengths can be processed without any special handling. Train/eval consistency — LN uses the same formula at training and inference with no running-mean accumulation and no behavioral shift between model.train() and model.eval(). BN violates all three properties.

- Batch independence: LN computes mean/var over the feature dim of each sample — no batch coupling.
- Variable sequences: padding tokens would corrupt BN batch statistics; LN processes each position independently.
- No train/eval gap: BN uses batch stats at train and running stats at eval; LN behavior is identical in both modes.
- Consistent gradient: LN gradient depends only on the local sample — no cross-batch gradient coupling in backward pass.

## Gradient Flow Through Layer Norm

The gradient of the LN output with respect to the input has a centering component: ∂L/∂x ∝ [∂L/∂x̂ − mean(∂L/∂x̂) − x̂ · mean(∂L/∂x̂ · x̂)] / σ. The mean subtraction terms prevent constant gradient components from flowing back, acting as an implicit gradient regularizer. For BN, gradients are coupled across the batch — each sample's gradient depends on all others, which can cause instability when batch size changes between training and inference.

```python
import torch
import torch.nn as nn
import numpy as np

def measure_grad_flow(norm_class, input_shape, **kwargs):
    x = torch.randn(*input_shape, requires_grad=True)
    layer = norm_class(**kwargs)
    out = layer(x)
    loss = out.pow(2).mean()
    loss.backward()
    return x.grad.abs().mean().item(), x.grad.std().item()

B, T, C = 4, 20, 64
ln_mean, ln_std = measure_grad_flow(nn.LayerNorm, (B, T, C), normalized_shape=C)

class BNSeq(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.bn = nn.BatchNorm1d(num_features)
    def forward(self, x):
        B, T, C = x.shape
        return self.bn(x.reshape(B * T, C)).reshape(B, T, C)

bn_mean, bn_std = measure_grad_flow(BNSeq, (B, T, C), num_features=C)

print(f'LayerNorm grad: mean={ln_mean:.6f}, std={ln_std:.6f}')
print(f'BatchNorm grad: mean={bn_mean:.6f}, std={bn_std:.6f}')
print('LN gradient is per-sample — no cross-batch coupling in the backward pass.')
```

## Embedding Layer Normalization

Modern LLMs apply LN to the embedding outputs before feeding them into the first transformer block. This bounds the scale of the initial residual stream and prevents early layers from spending capacity on normalization. BERT and RoBERTa apply LN after summing token and positional embeddings. GPT-NeoX uses a separate embedding normalization before and after the embedding lookup. The LN parameters at the embedding layer are learned independently from the LN inside each transformer block.

## Normalization Methods Comparison

| Method | Normalizes Over | Batch Dependent | Train/Eval Gap | Learnable Params | Standard Use |
| --- | --- | --- | --- | --- | --- |
| BatchNorm | Batch dim per channel | Yes | Yes — running stats at eval | γ, β per channel | Image classification (large batch) |
| LayerNorm | Feature dim per sample | No | No | γ, β per feature | Transformers, RNNs, NLP |
| RMSNorm | Feature dim per sample (no mean) | No | No | γ per feature only | LLaMA, Gemma, Mistral, Falcon |
| GroupNorm | Within each channel group per sample | No | No | γ, β per channel | Object detection, segmentation |
| InstanceNorm | Spatial dims per sample per channel | No | No | γ, β per channel (optional) | Style transfer, CycleGAN |

Choose LayerNorm for any Transformer-based architecture. Use RMSNorm when training efficiency matters and mean-centering is not critical. Use GroupNorm when batch sizes are small (≤4) and spatial structure exists. Use InstanceNorm specifically for style transfer where removing per-channel statistics normalizes style information.

---

