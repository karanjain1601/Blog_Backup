---
title: "SAINT — Self-Attention and Intersample Attention for Tabular Data"
slug: "saint-tabular"
description: "SAINT alternates between row-wise self-attention (over features) and intersample attention (over other training rows) to combine feature interaction modeling with instance-based learning."
tags: ["tabular", "deep-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU0FJTlQgKFNlbGYtQXR0ZW50aW9uIGFuZCBJbnRlcnNhbXBsZSBBdHRlbnRpb24gVHJhbnNmb3JtZXIsIFNvbWVwYWxsaSBldCBhbC4gMjAyMSkgYWRkcmVzc2VzIGEga2V5IGxpbWl0YXRpb24gb2YgRlQtVHJhbnNmb3JtZXI6IGF0dGVudGlvbiBpcyBjb21wdXRlZCBvbmx5IGFjcm9zcyBmZWF0dXJlcyBvZiBhIHNpbmdsZSByb3csIGlnbm9yaW5nIHJlbGF0aW9uc2hpcHMgYmV0d2VlbiB0cmFpbmluZyBzYW1wbGVzLiBTQUlOVCBhZGRzIGEgc2Vjb25kIGF0dGVudGlvbiBheGlzIOKAlCBhY3Jvc3Mgcm93cyDigJQgZWZmZWN0aXZlbHkgY29tYmluaW5nIGEgZmVhdHVyZS1pbnRlcmFjdGlvbiBUcmFuc2Zvcm1lciB3aXRoIGEgbGVhcm5lZCBrLU5OIGluIGVtYmVkZGluZyBzcGFjZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUd28gVHlwZXMgb2YgQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFYWNoIFNBSU5UIGJsb2NrIGNvbnRhaW5zIHR3byBzZXF1ZW50aWFsIHN1Yi1ibG9ja3MuIFJvdyBhdHRlbnRpb24gKGlkZW50aWNhbCB0byBGVC1UcmFuc2Zvcm1lcikgcHJvY2Vzc2VzIGZlYXR1cmVzIHdpdGhpbiBhIHNpbmdsZSBzYW1wbGUuIEludGVyc2FtcGxlIGF0dGVudGlvbiBwcm9jZXNzZXMgdGhlIHJlcHJlc2VudGF0aW9uIG9mIHRoZSBzYW1lIGZlYXR1cmUgYWNyb3NzIGEgYmF0Y2ggb2Ygc2FtcGxlcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlJvdyBhdHRlbnRpb246IGZvciBvbmUgc2FtcGxlLCBhdHRlbmQgb3ZlciBGIGZlYXR1cmUgdG9rZW5zIOKAlCBjYXB0dXJlcyBmZWF0dXJlIGludGVyYWN0aW9ucyB3aXRoaW4gYSByb3ciLCJJbnRlcnNhbXBsZSBhdHRlbnRpb246IGZvciBhIG1pbmktYmF0Y2ggb2YgQiBzYW1wbGVzLCBhdHRlbmQgb3ZlciBCIHNhbXBsZSByZXByZXNlbnRhdGlvbnMgb2YgdGhlIHNhbWUgZmVhdHVyZSBwb3NpdGlvbiIsIkFsdGVybmF0aW5nIHBhdHRlcm46IFtSb3cgQXR0biDihpIgSW50ZXJzYW1wbGUgQXR0bl0gw5cgTl9sYXllcnMiLCJJbnRlcnNhbXBsZSBhdHRlbnRpb24gbGV0cyB0aGUgbW9kZWwgYXNrOiB3aGljaCBvdGhlciB0cmFpbmluZyBzYW1wbGVzIGFyZSBtb3N0IGluZm9ybWF0aXZlIGZvciBwcmVkaWN0aW5nIHRoZSBjdXJyZW50IHNhbXBsZT8iLCJDb21wdXRhdGlvbmFsIGNvc3Q6IE8oQsKyKSBwZXIgaW50ZXJzYW1wbGUgYXR0ZW50aW9uIOKAlCBxdWFkcmF0aWMgaW4gYmF0Y2ggc2l6ZSwgbm90IGRhdGFzZXQgc2l6ZSIsIkF0IGluZmVyZW5jZSB0aW1lLCB0aGUgYmF0Y2ggYWN0cyBhcyB0aGUgY29udGV4dCDigJQgc2ltaWxhciBzYW1wbGVzIGluIHRoZSBiYXRjaCByZWluZm9yY2UgcHJlZGljdGlvbnMiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUm93IEF0dGVudGlvbiBCbG9jayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJvdyBhdHRlbnRpb24gYmxvY2sgaXMgYSBzdGFuZGFyZCBUcmFuc2Zvcm1lciBlbmNvZGVyIGxheWVyIGFwcGxpZWQgdG8gdGhlIEYgZmVhdHVyZSB0b2tlbnMgb2YgYSBzaW5nbGUgc2FtcGxlLiBJdCBpcyBpZGVudGljYWwgaW4gZGVzaWduIHRvIG9uZSBGVC1UcmFuc2Zvcm1lciBsYXllci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2ggaW1wb3J0IFRlbnNvclxuXG5jbGFzcyBSb3dBdHRlbnRpb25CbG9jayhubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlNlbGYtYXR0ZW50aW9uIG92ZXIgZmVhdHVyZXMgd2l0aGluIGVhY2ggcm93IChpZGVudGljYWwgdG8gRlQtVHJhbnNmb3JtZXIgbGF5ZXIpLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX3Rva2VuOiBpbnQsIG5faGVhZHM6IGludCwgZF9mZm46IGludCwgZHJvcG91dDogZmxvYXQgPSAwLjEpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5hdHRuID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKFxuICAgICAgICAgICAgZW1iZWRfZGltPWRfdG9rZW4sIG51bV9oZWFkcz1uX2hlYWRzLFxuICAgICAgICAgICAgZHJvcG91dD1kcm9wb3V0LCBiYXRjaF9maXJzdD1UcnVlXG4gICAgICAgIClcbiAgICAgICAgc2VsZi5mZiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MYXllck5vcm0oZF90b2tlbiksXG4gICAgICAgICAgICBubi5MaW5lYXIoZF90b2tlbiwgZF9mZm4pLFxuICAgICAgICAgICAgbm4uR0VMVSgpLFxuICAgICAgICAgICAgbm4uRHJvcG91dChkcm9wb3V0KSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihkX2ZmbiwgZF90b2tlbiksXG4gICAgICAgICAgICBubi5Ecm9wb3V0KGRyb3BvdXQpXG4gICAgICAgIClcbiAgICAgICAgc2VsZi5ub3JtMSA9IG5uLkxheWVyTm9ybShkX3Rva2VuKVxuICAgICAgICBzZWxmLm5vcm0yID0gbm4uTGF5ZXJOb3JtKGRfdG9rZW4pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiBUZW5zb3IpIC1cdTAwM2UgVGVuc29yOiAgIyB4OiAoQiwgRiwgZClcbiAgICAgICAgIyBTZWxmLWF0dGVudGlvbiBvdmVyIGZlYXR1cmVzIChGIHRva2VucylcbiAgICAgICAgYXR0bl9vdXQsIF8gPSBzZWxmLmF0dG4oeCwgeCwgeClcbiAgICAgICAgeCA9IHNlbGYubm9ybTEoeCArIGF0dG5fb3V0KVxuICAgICAgICAjIEZlZWQtZm9yd2FyZFxuICAgICAgICB4ID0gc2VsZi5ub3JtMih4ICsgc2VsZi5mZih4KSlcbiAgICAgICAgcmV0dXJuIHggICMgKEIsIEYsIGQpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW50ZXJzYW1wbGUgQXR0ZW50aW9uIEJsb2NrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbnRlcnNhbXBsZSBhdHRlbnRpb24gdHJhbnNwb3NlcyB0aGUgYmF0Y2ggYW5kIGZlYXR1cmUgZGltZW5zaW9uczogZm9yIGVhY2ggZmVhdHVyZSBwb3NpdGlvbiwgYWxsIEIgc2FtcGxlIHJlcHJlc2VudGF0aW9ucyBhdHRlbmQgdG8gZWFjaCBvdGhlci4gVGhpcyBwcm9kdWNlcyBhIELDl0IgYXR0ZW50aW9uIG1hdHJpeCBwZXIgZmVhdHVyZSDigJQgdGhlIG1vZGVsIGxlYXJucyB3aGljaCBzYW1wbGVzIGFyZSByZWxldmFudCBmb3IgcHJlZGljdGluZyBlYWNoIG90aGVyLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaCBpbXBvcnQgVGVuc29yXG5cbmNsYXNzIEludGVyc2FtcGxlQXR0ZW50aW9uQmxvY2sobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTZWxmLWF0dGVudGlvbiBvdmVyIHNhbXBsZXMgZm9yIGVhY2ggZmVhdHVyZSBwb3NpdGlvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF90b2tlbjogaW50LCBuX2hlYWRzOiBpbnQsIGRfZmZuOiBpbnQsIGRyb3BvdXQ6IGZsb2F0ID0gMC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYXR0biAgPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oXG4gICAgICAgICAgICBlbWJlZF9kaW09ZF90b2tlbiwgbnVtX2hlYWRzPW5faGVhZHMsXG4gICAgICAgICAgICBkcm9wb3V0PWRyb3BvdXQsIGJhdGNoX2ZpcnN0PVRydWVcbiAgICAgICAgKVxuICAgICAgICBzZWxmLm5vcm0xID0gbm4uTGF5ZXJOb3JtKGRfdG9rZW4pXG4gICAgICAgIHNlbGYubm9ybTIgPSBubi5MYXllck5vcm0oZF90b2tlbilcbiAgICAgICAgc2VsZi5mZiAgICA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZF90b2tlbiwgZF9mZm4pLCBubi5HRUxVKCksXG4gICAgICAgICAgICBubi5Ecm9wb3V0KGRyb3BvdXQpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGRfZmZuLCBkX3Rva2VuKSwgbm4uRHJvcG91dChkcm9wb3V0KVxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiBUZW5zb3IpIC1cdTAwM2UgVGVuc29yOiAgIyB4OiAoQiwgRiwgZClcbiAgICAgICAgQiwgRiwgZCA9IHguc2hhcGVcbiAgICAgICAgIyBUcmFuc3Bvc2U6IHRyZWF0IGVhY2ggZmVhdHVyZSBwb3NpdGlvbiBhcyBhIHNlcXVlbmNlIG9mIEIgc2FtcGxlc1xuICAgICAgICB4X3QgPSB4LnBlcm11dGUoMSwgMCwgMikgICAgICAgICAgIyAoRiwgQiwgZClcbiAgICAgICAgYXR0bl9vdXQsIF8gPSBzZWxmLmF0dG4oeF90LCB4X3QsIHhfdCkgICMgYXR0ZW5kIG92ZXIgQiBzYW1wbGVzXG4gICAgICAgIHhfdCA9IHNlbGYubm9ybTEoeF90ICsgYXR0bl9vdXQpXG4gICAgICAgIHhfdCA9IHNlbGYubm9ybTIoeF90ICsgc2VsZi5mZih4X3QpKVxuICAgICAgICByZXR1cm4geF90LnBlcm11dGUoMSwgMCwgMikgICAgICAgICMgYmFjayB0byAoQiwgRiwgZCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTQUlOVCBGdWxsIEZvcndhcmQgUGFzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU0FJTlQgc3RhY2tzIGFsdGVybmF0aW5nIHJvdyBhbmQgaW50ZXJzYW1wbGUgYXR0ZW50aW9uIGJsb2Nrcy4gVGhlIFtDTFNdIHRva2VuIChwcmVwZW5kZWQgdG8gdGhlIGZlYXR1cmUgc2VxdWVuY2UpIGFnZ3JlZ2F0ZXMgZ2xvYmFsIGluZm9ybWF0aW9uIGFuZCBkcml2ZXMgdGhlIHByZWRpY3Rpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoIGltcG9ydCBUZW5zb3JcblxuY2xhc3MgU0FJTlQobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl9mZWF0dXJlczogaW50LCBkX3Rva2VuOiBpbnQsIG5faGVhZHM6IGludCxcbiAgICAgICAgICAgICAgICAgZF9mZm46IGludCwgbl9sYXllcnM6IGludCwgbl9jbGFzc2VzOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgIyBGZWF0dXJlIHRva2VuaXphdGlvbiAobnVtZXJpY2FsLCBzYW1lIGFzIEZULVRyYW5zZm9ybWVyKVxuICAgICAgICBzZWxmLnRva2VuaXplciA9IG5uLkxpbmVhcigxLCBkX3Rva2VuKSAgIyBzaW1wbGlmaWVkOiBzaGFyZWQgcHJvamVjdGlvblxuICAgICAgICBzZWxmLmNsc190b2tlbiAgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3MoMSwgMSwgZF90b2tlbikpXG5cbiAgICAgICAgc2VsZi5yb3dfYmxvY2tzID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBSb3dBdHRlbnRpb25CbG9jayhkX3Rva2VuLCBuX2hlYWRzLCBkX2ZmbikgZm9yIF8gaW4gcmFuZ2Uobl9sYXllcnMpXG4gICAgICAgIF0pXG4gICAgICAgIHNlbGYuaXNhbXBsZV9ibG9ja3MgPSBubi5Nb2R1bGVMaXN0KFtcbiAgICAgICAgICAgIEludGVyc2FtcGxlQXR0ZW50aW9uQmxvY2soZF90b2tlbiwgbl9oZWFkcywgZF9mZm4pIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKVxuICAgICAgICBdKVxuICAgICAgICBzZWxmLmhlYWQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGF5ZXJOb3JtKGRfdG9rZW4pLFxuICAgICAgICAgICAgbm4uTGluZWFyKGRfdG9rZW4sIG5fY2xhc3NlcylcbiAgICAgICAgKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogVGVuc29yKSAtXHUwMDNlIFRlbnNvcjogICMgeDogKEIsIEYpXG4gICAgICAgICMgVG9rZW5pemUgZWFjaCBmZWF0dXJlIGluZGVwZW5kZW50bHlcbiAgICAgICAgdG9rZW5zID0gc2VsZi50b2tlbml6ZXIoeC51bnNxdWVlemUoLTEpKSAgICAgICAgICAgIyAoQiwgRiwgZClcbiAgICAgICAgY2xzICAgID0gc2VsZi5jbHNfdG9rZW4uZXhwYW5kKHguc2l6ZSgwKSwgLTEsIC0xKSAgIyAoQiwgMSwgZClcbiAgICAgICAgdG9rZW5zID0gdG9yY2guY2F0KFtjbHMsIHRva2Vuc10sIGRpbT0xKSAgICAgICAgICAgICMgKEIsIEYrMSwgZClcblxuICAgICAgICAjIEFsdGVybmF0ZSByb3cgYW5kIGludGVyc2FtcGxlIGF0dGVudGlvblxuICAgICAgICBmb3Igcm93X2JsaywgaXNhbXBsZV9ibGsgaW4gemlwKHNlbGYucm93X2Jsb2Nrcywgc2VsZi5pc2FtcGxlX2Jsb2Nrcyk6XG4gICAgICAgICAgICB0b2tlbnMgPSByb3dfYmxrKHRva2VucylcbiAgICAgICAgICAgIHRva2VucyA9IGlzYW1wbGVfYmxrKHRva2VucylcblxuICAgICAgICByZXR1cm4gc2VsZi5oZWFkKHRva2Vuc1s6LCAwXSkgICMgQ0xTIHRva2VuIOKGkiBwcmVkaWN0aW9uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU0NBUkYtU3R5bGUgUHJldHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNBSU5UIHVzZXMgU0NBUkYgKFNlbGYtc3VwZXJ2aXNlZCBDb250cmFzdGl2ZSBsZWFybmluZyB1c2luZyByYW5kb20gRmVhdHVyZSBDb3JydXB0aW9uKSBmb3IgcHJldHJhaW5pbmc6IHJhbmRvbWx5IHJlcGxhY2UgZWFjaCBmZWF0dXJlIHZhbHVlIHdpdGggYSB2YWx1ZSBzYW1wbGVkIGZyb20gdGhlIGVtcGlyaWNhbCBtYXJnaW5hbCBkaXN0cmlidXRpb24gb2YgdGhhdCBmZWF0dXJlLiBUaGUgbW9kZWwgbGVhcm5zIHRvIHByb2R1Y2Ugc2ltaWxhciByZXByZXNlbnRhdGlvbnMgZm9yIGNsZWFuIGFuZCBjb3JydXB0ZWQgdmlld3Mgb2YgdGhlIHNhbWUgcm93IChjb250cmFzdGl2ZSBsb3NzKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmZyb20gdG9yY2ggaW1wb3J0IFRlbnNvclxuXG5kZWYgc2NhcmZfY29ycnVwdCh4OiBUZW5zb3IsIGNvcnJ1cHRpb25fcmF0ZTogZmxvYXQgPSAwLjYpIC1cdTAwM2UgVGVuc29yOlxuICAgIFwiXCJcIlJlcGxhY2UgZWFjaCBmZWF0dXJlIHdpdGggYSByYW5kb20gdmFsdWUgZnJvbSBpdHMgZW1waXJpY2FsIG1hcmdpbmFsLlwiXCJcIlxuICAgIEIsIEYgPSB4LnNoYXBlXG4gICAgbWFzayA9IHRvcmNoLmJlcm5vdWxsaSh0b3JjaC5mdWxsKChCLCBGKSwgY29ycnVwdGlvbl9yYXRlKSkuYm9vbCgpXG4gICAgIyBTYW1wbGUgcmFuZG9tIHJvdyBpbmRpY2VzIGZvciBlYWNoIHBvc2l0aW9uIHRvIHVzZSBhcyByZXBsYWNlbWVudFxuICAgIHJhbmRvbV9yb3dzID0gdG9yY2gucmFuZGludCgwLCBCLCAoQiwgRikpXG4gICAgeF9jb3JydXB0ICAgPSB4LmNsb25lKClcbiAgICBmb3IgaiBpbiByYW5nZShGKTpcbiAgICAgICAgeF9jb3JydXB0W21hc2tbOiwgal0sIGpdID0geFtyYW5kb21fcm93c1ttYXNrWzosIGpdLCBqXSwgal1cbiAgICByZXR1cm4geF9jb3JydXB0XG5cbmNsYXNzIFNDQVJGTG9zcyhubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0ZW1wZXJhdHVyZTogZmxvYXQgPSAwLjA3KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYudGVtcGVyYXR1cmUgPSB0ZW1wZXJhdHVyZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgel9jbGVhbjogVGVuc29yLCB6X2NvcnJ1cHQ6IFRlbnNvcikgLVx1MDAzZSBUZW5zb3I6XG4gICAgICAgIHoxID0gRi5ub3JtYWxpemUoel9jbGVhbiwgICBkaW09LTEpICAjIChCLCBkKVxuICAgICAgICB6MiA9IEYubm9ybWFsaXplKHpfY29ycnVwdCwgZGltPS0xKSAgIyAoQiwgZClcbiAgICAgICAgbG9naXRzID0gejEgQCB6Mi5UIC8gc2VsZi50ZW1wZXJhdHVyZSAgIyAoQiwgQilcbiAgICAgICAgbGFiZWxzID0gdG9yY2guYXJhbmdlKHoxLnNpemUoMCksIGRldmljZT16MS5kZXZpY2UpXG4gICAgICAgIHJldHVybiBGLmNyb3NzX2VudHJvcHkobG9naXRzLCBsYWJlbHMpICAjIEluZm9OQ0UgbG9zcyJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTQUlOVCB2cyBPdGhlciBUYWJ1bGFyIE1vZGVscyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIkF0dGVudGlvbiBUeXBlIiwiUHJldHJhaW5pbmciLCJDb21wbGV4aXR5IiwiQmVuY2htYXJrIFBlcmZvcm1hbmNlIl0sInJvd3MiOltbIkZULVRyYW5zZm9ybWVyIiwiUm93IG9ubHkgKGZlYXR1cmUgw5cgZmVhdHVyZSkiLCJNTE0tc3R5bGUgb3B0aW9uYWwiLCJPKEbCsikgcGVyIGxheWVyIiwiQ29tcGV0aXRpdmUgd2l0aCBYR0Jvb3N0IG9uIGxhcmdlIGRhdGFzZXRzIl0sWyJTQUlOVCIsIlJvdyArIEludGVyc2FtcGxlIiwiU0NBUkYgY29udHJhc3RpdmUiLCJPKEbCsikgKyBPKELCsikgcGVyIGxheWVyIiwiR2VuZXJhbGx5IG91dHBlcmZvcm1zIEZULVRyYW5zZm9ybWVyIl0sWyJUYWJOZXQiLCJTZXF1ZW50aWFsIHNwYXJzZSBmZWF0dXJlIHNlbGVjdGlvbiIsIlJlY29uc3RydWN0aW9uIHByZXRyYWluaW5nIiwiTyhOX3N0ZXBzIMOXIEYpIiwiT2Z0ZW4gYmVoaW5kIEZULVRyYW5zZm9ybWVyIGFuZCBTQUlOVCJdLFsiWEdCb29zdCIsIk5vbmUgKGdyZWVkeSBzcGxpdHMpIiwiTm9uZSIsIk8obiBsb2cgbikgcGVyIHRyZWUiLCJTdGF0ZS1vZi10aGUtYXJ0IG9uIG1vc3QgdGFidWxhciBiZW5jaG1hcmtzIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkludGVyc2FtcGxlIEF0dGVudGlvbiBDb3N0IiwiY29udGVudCI6IkludGVyc2FtcGxlIGF0dGVudGlvbiBpcyBxdWFkcmF0aWMgaW4gYmF0Y2ggc2l6ZSBPKELCsikuIEZvciBCPTUxMiwgdGhpcyBtZWFucyAyNjIsMTQ0IGF0dGVudGlvbiBzY29yZSBjb21wdXRhdGlvbnMgcGVyIGZlYXR1cmUgcG9zaXRpb24gcGVyIGxheWVyLiBLZWVwIGJhdGNoIHNpemVzIG1vZGVyYXRlICgxMjjigJM1MTIpIGFuZCBtb25pdG9yIEdQVSBtZW1vcnkuIEF0IGluZmVyZW5jZSwgcHJlZGljdGlvbnMgaW1wcm92ZSB3aGVuIHRoZSBiYXRjaCBjb250YWlucyBkaXZlcnNlLCByZXByZXNlbnRhdGl2ZSBzYW1wbGVzIGZyb20gdGhlIHRyYWluaW5nIGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTQUlOVCBjb21iaW5lcyByb3cgYXR0ZW50aW9uIChmZWF0dXJlIGludGVyYWN0aW9ucykgd2l0aCBpbnRlcnNhbXBsZSBhdHRlbnRpb24gKHNhbXBsZSBzaW1pbGFyaXR5KSBpbiBhbHRlcm5hdGluZyBibG9ja3MiLCJJbnRlcnNhbXBsZSBhdHRlbnRpb24gaXMgYW5hbG9nb3VzIHRvIGEgbGVhcm5lZCBzb2Z0IGstTk46IHNpbWlsYXIgdHJhaW5pbmcgc2FtcGxlcyBhdHRlbmQgdG8gZWFjaCBvdGhlciIsIlNDQVJGIHByZXRyYWluaW5nIHVzZXMgbWFyZ2luYWwtZGlzdHJpYnV0aW9uIGZlYXR1cmUgY29ycnVwdGlvbiB3aXRoIGNvbnRyYXN0aXZlIEluZm9OQ0UgbG9zcyIsIlNBSU5UIGdlbmVyYWxseSBvdXRwZXJmb3JtcyBGVC1UcmFuc2Zvcm1lciBhbmQgVGFiTmV0IGJ1dCBhdCBoaWdoZXIgY29tcHV0YXRpb25hbCBjb3N0IiwiTyhCwrIpIGludGVyc2FtcGxlIGF0dGVudGlvbiBjb3N0IHJlcXVpcmVzIGNhcmVmdWwgYmF0Y2ggc2l6ZSBzZWxlY3Rpb24gdG8gYXZvaWQgbWVtb3J5IGlzc3VlcyJdfV0="
---
# SAINT — Self-Attention and Intersample Attention for Tabular Data

SAINT (Self-Attention and Intersample Attention Transformer, Somepalli et al. 2021) addresses a key limitation of FT-Transformer: attention is computed only across features of a single row, ignoring relationships between training samples. SAINT adds a second attention axis — across rows — effectively combining a feature-interaction Transformer with a learned k-NN in embedding space.

## Two Types of Attention

Each SAINT block contains two sequential sub-blocks. Row attention (identical to FT-Transformer) processes features within a single sample. Intersample attention processes the representation of the same feature across a batch of samples.

- Row attention: for one sample, attend over F feature tokens — captures feature interactions within a row
- Intersample attention: for a mini-batch of B samples, attend over B sample representations of the same feature position
- Alternating pattern: [Row Attn → Intersample Attn] × N_layers
- Intersample attention lets the model ask: which other training samples are most informative for predicting the current sample?
- Computational cost: O(B²) per intersample attention — quadratic in batch size, not dataset size
- At inference time, the batch acts as the context — similar samples in the batch reinforce predictions

## Row Attention Block

The row attention block is a standard Transformer encoder layer applied to the F feature tokens of a single sample. It is identical in design to one FT-Transformer layer.

```python
import torch
import torch.nn as nn
from torch import Tensor

class RowAttentionBlock(nn.Module):
    """Self-attention over features within each row (identical to FT-Transformer layer)."""
    def __init__(self, d_token: int, n_heads: int, d_ffn: int, dropout: float = 0.1):
        super().__init__()
        self.attn = nn.MultiheadAttention(
            embed_dim=d_token, num_heads=n_heads,
            dropout=dropout, batch_first=True
        )
        self.ff = nn.Sequential(
            nn.LayerNorm(d_token),
            nn.Linear(d_token, d_ffn),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ffn, d_token),
            nn.Dropout(dropout)
        )
        self.norm1 = nn.LayerNorm(d_token)
        self.norm2 = nn.LayerNorm(d_token)

    def forward(self, x: Tensor) -> Tensor:  # x: (B, F, d)
        # Self-attention over features (F tokens)
        attn_out, _ = self.attn(x, x, x)
        x = self.norm1(x + attn_out)
        # Feed-forward
        x = self.norm2(x + self.ff(x))
        return x  # (B, F, d)
```

## Intersample Attention Block

Intersample attention transposes the batch and feature dimensions: for each feature position, all B sample representations attend to each other. This produces a B×B attention matrix per feature — the model learns which samples are relevant for predicting each other.

```python
import torch
import torch.nn as nn
from torch import Tensor

class IntersampleAttentionBlock(nn.Module):
    """Self-attention over samples for each feature position."""
    def __init__(self, d_token: int, n_heads: int, d_ffn: int, dropout: float = 0.1):
        super().__init__()
        self.attn  = nn.MultiheadAttention(
            embed_dim=d_token, num_heads=n_heads,
            dropout=dropout, batch_first=True
        )
        self.norm1 = nn.LayerNorm(d_token)
        self.norm2 = nn.LayerNorm(d_token)
        self.ff    = nn.Sequential(
            nn.Linear(d_token, d_ffn), nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ffn, d_token), nn.Dropout(dropout)
        )

    def forward(self, x: Tensor) -> Tensor:  # x: (B, F, d)
        B, F, d = x.shape
        # Transpose: treat each feature position as a sequence of B samples
        x_t = x.permute(1, 0, 2)          # (F, B, d)
        attn_out, _ = self.attn(x_t, x_t, x_t)  # attend over B samples
        x_t = self.norm1(x_t + attn_out)
        x_t = self.norm2(x_t + self.ff(x_t))
        return x_t.permute(1, 0, 2)        # back to (B, F, d)
```

## SAINT Full Forward Pass

SAINT stacks alternating row and intersample attention blocks. The [CLS] token (prepended to the feature sequence) aggregates global information and drives the prediction.

```python
import torch
import torch.nn as nn
from torch import Tensor

class SAINT(nn.Module):
    def __init__(self, n_features: int, d_token: int, n_heads: int,
                 d_ffn: int, n_layers: int, n_classes: int):
        super().__init__()
        # Feature tokenization (numerical, same as FT-Transformer)
        self.tokenizer = nn.Linear(1, d_token)  # simplified: shared projection
        self.cls_token  = nn.Parameter(torch.zeros(1, 1, d_token))

        self.row_blocks = nn.ModuleList([
            RowAttentionBlock(d_token, n_heads, d_ffn) for _ in range(n_layers)
        ])
        self.isample_blocks = nn.ModuleList([
            IntersampleAttentionBlock(d_token, n_heads, d_ffn) for _ in range(n_layers)
        ])
        self.head = nn.Sequential(
            nn.LayerNorm(d_token),
            nn.Linear(d_token, n_classes)
        )

    def forward(self, x: Tensor) -> Tensor:  # x: (B, F)
        # Tokenize each feature independently
        tokens = self.tokenizer(x.unsqueeze(-1))           # (B, F, d)
        cls    = self.cls_token.expand(x.size(0), -1, -1)  # (B, 1, d)
        tokens = torch.cat([cls, tokens], dim=1)            # (B, F+1, d)

        # Alternate row and intersample attention
        for row_blk, isample_blk in zip(self.row_blocks, self.isample_blocks):
            tokens = row_blk(tokens)
            tokens = isample_blk(tokens)

        return self.head(tokens[:, 0])  # CLS token → prediction
```

## SCARF-Style Pretraining

SAINT uses SCARF (Self-supervised Contrastive learning using random Feature Corruption) for pretraining: randomly replace each feature value with a value sampled from the empirical marginal distribution of that feature. The model learns to produce similar representations for clean and corrupted views of the same row (contrastive loss).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor

def scarf_corrupt(x: Tensor, corruption_rate: float = 0.6) -> Tensor:
    """Replace each feature with a random value from its empirical marginal."""
    B, F = x.shape
    mask = torch.bernoulli(torch.full((B, F), corruption_rate)).bool()
    # Sample random row indices for each position to use as replacement
    random_rows = torch.randint(0, B, (B, F))
    x_corrupt   = x.clone()
    for j in range(F):
        x_corrupt[mask[:, j], j] = x[random_rows[mask[:, j], j], j]
    return x_corrupt

class SCARFLoss(nn.Module):
    def __init__(self, temperature: float = 0.07):
        super().__init__()
        self.temperature = temperature

    def forward(self, z_clean: Tensor, z_corrupt: Tensor) -> Tensor:
        z1 = F.normalize(z_clean,   dim=-1)  # (B, d)
        z2 = F.normalize(z_corrupt, dim=-1)  # (B, d)
        logits = z1 @ z2.T / self.temperature  # (B, B)
        labels = torch.arange(z1.size(0), device=z1.device)
        return F.cross_entropy(logits, labels)  # InfoNCE loss
```

---

## SAINT vs Other Tabular Models

| Model | Attention Type | Pretraining | Complexity | Benchmark Performance |
| --- | --- | --- | --- | --- |
| FT-Transformer | Row only (feature × feature) | MLM-style optional | O(F²) per layer | Competitive with XGBoost on large datasets |
| SAINT | Row + Intersample | SCARF contrastive | O(F²) + O(B²) per layer | Generally outperforms FT-Transformer |
| TabNet | Sequential sparse feature selection | Reconstruction pretraining | O(N_steps × F) | Often behind FT-Transformer and SAINT |
| XGBoost | None (greedy splits) | None | O(n log n) per tree | State-of-the-art on most tabular benchmarks |

> **Intersample Attention Cost**: Intersample attention is quadratic in batch size O(B²). For B=512, this means 262,144 attention score computations per feature position per layer. Keep batch sizes moderate (128–512) and monitor GPU memory. At inference, predictions improve when the batch contains diverse, representative samples from the training distribution.

## Key Takeaways

- SAINT combines row attention (feature interactions) with intersample attention (sample similarity) in alternating blocks
- Intersample attention is analogous to a learned soft k-NN: similar training samples attend to each other
- SCARF pretraining uses marginal-distribution feature corruption with contrastive InfoNCE loss
- SAINT generally outperforms FT-Transformer and TabNet but at higher computational cost
- O(B²) intersample attention cost requires careful batch size selection to avoid memory issues

