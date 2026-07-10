---
title: "MAE — Masked Autoencoders for Vision"
slug: "mae-masked-autoencoder"
description: "Deep dive into MAE (He et al. 2022): masking 75% of image patches, asymmetric encoder-decoder design, normalized pixel reconstruction targets, and comparison with SimMIM, BEiT, and MaskFeat."
tags: ["deep-learning", "self-supervised-learning", "masked-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWFza2VkIEF1dG9lbmNvZGVycyAoTUFFKSBieSBIZSBldCBhbC4gKDIwMjIpIGRlbW9uc3RyYXRlZCB0aGF0IGEgc3VycHJpc2luZ2x5IHNpbXBsZSBpZGVhIOKAlCBtYXNrIG1vc3Qgb2YgYW4gaW1hZ2UgYW5kIHJlY29uc3RydWN0IHRoZSBtaXNzaW5nIHBhcnRzIOKAlCBzY2FsZXMgcmVtYXJrYWJseSB3ZWxsIGZvciB2aXN1YWwgcHJlLXRyYWluaW5nLiBCeSBtYXNraW5nIDc1JSBvZiBwYXRjaGVzIGFuZCB1c2luZyBhbiBhc3ltbWV0cmljIGVuY29kZXItZGVjb2RlciwgTUFFIGFjaGlldmVzIHN0cm9uZyByZXByZXNlbnRhdGlvbnMgd2l0aG91dCBjb250cmFzdGl2ZSBwYWlycywgbmVnYXRpdmUgc2FtcGxlcywgb3IgbW9tZW50dW0gbmV0d29ya3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2hhdCBpcyBNQUU/In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNQUUgaXMgYSBzZWxmLXN1cGVydmlzZWQgcHJlLXRyYWluaW5nIG1ldGhvZCBmb3IgdmlzaW9uIHRyYW5zZm9ybWVycyAoVmlUKS4gVGhlIGNvcmUgaWRlYSBtaXJyb3JzIEJFUlQgaW4gTkxQOiByYW5kb21seSBtYXNrIGEgc3Vic2V0IG9mIGlucHV0IHRva2VucyAocGF0Y2hlcykgYW5kIHRyYWluIHRoZSBtb2RlbCB0byByZWNvbnN0cnVjdCB0aGUgb3JpZ2luYWxzLiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCB2aXNpb24gZGF0YSBpcyBmYXIgbW9yZSByZWR1bmRhbnQgdGhhbiBsYW5ndWFnZSDigJQgYSBoaWdoIG1hc2tpbmcgcmF0aW8gKDc1JSB2cyBCRVJUXHUwMDI3cyAxNSUpIGZvcmNlcyB0aGUgbW9kZWwgdG8gbGVhcm4gaG9saXN0aWMgc2NlbmUgdW5kZXJzdGFuZGluZyByYXRoZXIgdGhhbiBpbnRlcnBvbGF0aW5nIGZyb20gbmVhcmJ5IHZpc2libGUgcGl4ZWxzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBhdGNoIE1hc2tpbmcgU3RyYXRlZ3kifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1BRSBkaXZpZGVzIHRoZSBpbnB1dCBpbWFnZSBpbnRvIG5vbi1vdmVybGFwcGluZyBwYXRjaGVzICh0eXBpY2FsbHkgMTZ4MTYgcGl4ZWxzKS4gQSByYW5kb20gNzUlIG9mIHBhdGNoZXMgYXJlIG1hc2tlZC4gQ3J1Y2lhbGx5LCB0aGUgZW5jb2RlciBzZWVzIG9ubHkgdGhlIHJlbWFpbmluZyAyNSUg4oCUIG1hc2sgdG9rZW5zIGFyZSBuZXZlciBwYXNzZWQgdG8gdGhlIGVuY29kZXIuIFRoaXMgYXN5bW1ldHJpYyBkZXNpZ24gaXMgdGhlIGtleSBlZmZpY2llbmN5IHdpbjogdGhlIGVuY29kZXIgcHJvY2Vzc2VzIG9ubHkgYSBxdWFydGVyIG9mIHRoZSBwYXRjaGVzLCB5aWVsZGluZyBhIDPigJM0eCBzcGVlZHVwIG92ZXIgcHJvY2Vzc2luZyBhbGwgcGF0Y2hlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIHJhbmRvbV9tYXNraW5nKHgsIG1hc2tfcmF0aW89MC43NSk6XG4gICAgIyB4OiBbQiwgTiwgRF0gcGF0Y2ggZW1iZWRkaW5nc1xuICAgICMgUmV0dXJuczogdmlzaWJsZSB0b2tlbnMsIGJpbmFyeSBtYXNrICgxPW1hc2tlZCksIHJlc3RvcmUgaW5kaWNlc1xuICAgIEIsIE4sIEQgPSB4LnNoYXBlXG4gICAga2VlcCA9IGludChOICogKDEgLSBtYXNrX3JhdGlvKSkgICMgbnVtYmVyIG9mIHBhdGNoZXMgdG8ga2VlcFxuXG4gICAgIyBHZW5lcmF0ZSBwZXItc2FtcGxlIHJhbmRvbSBub2lzZSBmb3IgaW5kZXBlbmRlbnQgc2h1ZmZsaW5nXG4gICAgbm9pc2UgPSB0b3JjaC5yYW5kKEIsIE4sIGRldmljZT14LmRldmljZSlcblxuICAgICMgU29ydCBwYXRjaGVzIGJ5IG5vaXNlIHRvIGdldCBhIHJhbmRvbSBwZXJtdXRhdGlvblxuICAgIGlkc19zaHVmZmxlID0gdG9yY2guYXJnc29ydChub2lzZSwgZGltPTEpICAgICAgICAjIGFzY2VuZGluZ1xuICAgIGlkc19yZXN0b3JlID0gdG9yY2guYXJnc29ydChpZHNfc2h1ZmZsZSwgZGltPTEpICAjIGludmVyc2UgcGVybXV0YXRpb25cblxuICAgICMgS2VlcCBvbmx5IHRoZSBmaXJzdCBga2VlcGAgcGF0Y2hlcyAobG93ZXN0IG5vaXNlIHZhbHVlcylcbiAgICBpZHNfa2VlcCA9IGlkc19zaHVmZmxlWzosIDprZWVwXVxuICAgIHhfdmlzaWJsZSA9IHRvcmNoLmdhdGhlcihcbiAgICAgICAgeCwgZGltPTEsXG4gICAgICAgIGluZGV4PWlkc19rZWVwLnVuc3F1ZWV6ZSgtMSkuZXhwYW5kKC0xLCAtMSwgRClcbiAgICApXG5cbiAgICAjIEJpbmFyeSBtYXNrOiAwID0ga2VwdCwgMSA9IG1hc2tlZCAoYWxpZ25lZCB3aXRoIGlkc19yZXN0b3JlIG9yZGVyKVxuICAgIG1hc2sgPSB0b3JjaC5vbmVzKEIsIE4sIGRldmljZT14LmRldmljZSlcbiAgICBtYXNrWzosIDprZWVwXSA9IDBcbiAgICBtYXNrID0gdG9yY2guZ2F0aGVyKG1hc2ssIGRpbT0xLCBpbmRleD1pZHNfcmVzdG9yZSlcblxuICAgIHJldHVybiB4X3Zpc2libGUsIG1hc2ssIGlkc19yZXN0b3JlXG5cbiMgRXhhbXBsZSB1c2FnZTogMTk2IHBhdGNoZXMgKDE0eDE0IGdyaWQgZm9yIDIyNHB4IGltYWdlIHdpdGggMTZweCBwYXRjaGVzKVxuIyB4ID0gdG9yY2gucmFuZG4oOCwgMTk2LCA3NjgpICAjIGJhdGNoIG9mIDgsIDE5NiBwYXRjaGVzLCA3NjgtZGltXG4jIHhfdmlzLCBtYXNrLCBpZHNfcmVzdG9yZSA9IHJhbmRvbV9tYXNraW5nKHgsIG1hc2tfcmF0aW89MC43NSlcbiMgeF92aXMuc2hhcGUgIC1cdTAwM2UgWzgsIDQ5LCA3NjhdICAob25seSAyNSUgdmlzaWJsZSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgTUFFIEVuY29kZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBlbmNvZGVyIGlzIGEgc3RhbmRhcmQgVmlUIChlLmcuLCBWaVQtTCB3aXRoIDI0IGJsb2NrcyBhbmQgMTAyNC1kaW0gZW1iZWRkaW5ncykgdGhhdCBvcGVyYXRlcyBleGNsdXNpdmVseSBvbiB2aXNpYmxlIHBhdGNoZXMuIFBvc2l0aW9uYWwgZW1iZWRkaW5ncyBhcmUgYWRkZWQgYmVmb3JlIG1hc2tpbmcgc28gdGhlIGVuY29kZXIga25vd3Mgc3BhdGlhbCBwb3NpdGlvbnMuIE5vIG1hc2sgdG9rZW5zIGVudGVyIHRoZSBlbmNvZGVyIOKAlCB0aGlzIGlzIHdoYXQgbWFrZXMgaXQgY29tcHV0YXRpb25hbGx5IGVmZmljaWVudC4gVGhlIGVuY29kZXIgcHJvZHVjZXMgcmljaCByZXByZXNlbnRhdGlvbnMgZm9yIG9ubHkgdGhlIHZpc2libGUgMjUlIG9mIHBhdGNoZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIGVpbm9wcyBpbXBvcnQgcmVhcnJhbmdlXG5cbmNsYXNzIFRyYW5zZm9ybWVyQmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltLCBoZWFkcywgbWxwX3JhdGlvPTQuMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5vcm0xID0gbm4uTGF5ZXJOb3JtKGRpbSlcbiAgICAgICAgc2VsZi5hdHRuID0gbm4uTXVsdGloZWFkQXR0ZW50aW9uKGRpbSwgaGVhZHMsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYubm9ybTIgPSBubi5MYXllck5vcm0oZGltKVxuICAgICAgICBzZWxmLm1scCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZGltLCBpbnQoZGltICogbWxwX3JhdGlvKSksIG5uLkdFTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihpbnQoZGltICogbWxwX3JhdGlvKSwgZGltKVxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHggPSB4ICsgc2VsZi5hdHRuKHNlbGYubm9ybTEoeCksIHNlbGYubm9ybTEoeCksIHNlbGYubm9ybTEoeCkpWzBdXG4gICAgICAgIHJldHVybiB4ICsgc2VsZi5tbHAoc2VsZi5ub3JtMih4KSlcblxuY2xhc3MgTUFFRW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbWdfc2l6ZT0yMjQsIHBhdGNoX3NpemU9MTYsIGVtYmVkX2RpbT03NjgsIGRlcHRoPTEyLCBudW1faGVhZHM9MTIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5wYXRjaF9lbWJlZCA9IG5uLkNvbnYyZCgzLCBlbWJlZF9kaW0sIHBhdGNoX3NpemUsIHN0cmlkZT1wYXRjaF9zaXplKVxuICAgICAgICBudW1fcGF0Y2hlcyA9IChpbWdfc2l6ZSAvLyBwYXRjaF9zaXplKSAqKiAyXG4gICAgICAgIHNlbGYucG9zX2VtYmVkID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKDEsIG51bV9wYXRjaGVzICsgMSwgZW1iZWRfZGltKSlcbiAgICAgICAgc2VsZi5jbHNfdG9rZW4gID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKDEsIDEsIGVtYmVkX2RpbSkpXG4gICAgICAgIHNlbGYuYmxvY2tzID0gbm4uTW9kdWxlTGlzdChbVHJhbnNmb3JtZXJCbG9jayhlbWJlZF9kaW0sIG51bV9oZWFkcykgZm9yIF8gaW4gcmFuZ2UoZGVwdGgpXSlcbiAgICAgICAgc2VsZi5ub3JtID0gbm4uTGF5ZXJOb3JtKGVtYmVkX2RpbSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIGlkc19rZWVwKTpcbiAgICAgICAgQiA9IHguc2hhcGVbMF1cbiAgICAgICAgeCA9IHJlYXJyYW5nZShzZWxmLnBhdGNoX2VtYmVkKHgpLCBcdTAwMjdiIGQgaCB3IC1cdTAwM2UgYiAoaCB3KSBkXHUwMDI3KVxuICAgICAgICB4ID0geCArIHNlbGYucG9zX2VtYmVkWzosIDE6LCA6XSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIHNwYXRpYWwgcG9zLWVtYmVkXG4gICAgICAgIEQgPSB4LnNoYXBlWy0xXVxuICAgICAgICB4ID0gdG9yY2guZ2F0aGVyKHgsIDEsIGlkc19rZWVwLnVuc3F1ZWV6ZSgtMSkuZXhwYW5kKC0xLCAtMSwgRCkpICMga2VlcCB2aXNpYmxlIG9ubHlcbiAgICAgICAgY2xzID0gc2VsZi5jbHNfdG9rZW4uZXhwYW5kKEIsIC0xLCAtMSlcbiAgICAgICAgeCA9IHRvcmNoLmNhdChbY2xzLCB4XSwgZGltPTEpXG4gICAgICAgIGZvciBibG9jayBpbiBzZWxmLmJsb2NrczpcbiAgICAgICAgICAgIHggPSBibG9jayh4KVxuICAgICAgICByZXR1cm4gc2VsZi5ub3JtKHgpICAjIFtCLCAxK2tlZXAsIERdIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIE1BRSBEZWNvZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZGVjb2RlciBpcyBpbnRlbnRpb25hbGx5IGxpZ2h0d2VpZ2h0IOKAlCBvbmx5IDQgdHJhbnNmb3JtZXIgYmxvY2tzICh2cyAxMisgaW4gdGhlIGVuY29kZXIpIGFuZCBhIHNtYWxsZXIgZW1iZWRkaW5nIGRpbWVuc2lvbiAoNTEyIHZzIDc2OCkuIEl0IHJlY2VpdmVzIGVuY29kZWQgdmlzaWJsZSB0b2tlbnMgcGx1cyBsZWFybmFibGUgbWFzayB0b2tlbnMgaW5zZXJ0ZWQgYXQgbWFza2VkIHBvc2l0aW9ucy4gUG9zaXRpb25hbCBlbWJlZGRpbmdzIGFyZSBhZGRlZCBzbyB0aGUgZGVjb2RlciBrbm93cyB3aGljaCBwYXRjaGVzIHRvIHJlY29uc3RydWN0LiBUaGUgb3V0cHV0IGhlYWQgcHJvamVjdHMgdG8gcGl4ZWwgdmFsdWVzIGZvciBlYWNoIHBhdGNoLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBNQUVEZWNvZGVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG51bV9wYXRjaGVzPTE5NiwgZW5jb2Rlcl9kaW09NzY4LCBkZWNvZGVyX2RpbT01MTIsXG4gICAgICAgICAgICAgICAgIGRlcHRoPTQsIG51bV9oZWFkcz04LCBwYXRjaF9zaXplPTE2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZGVjb2Rlcl9lbWJlZCA9IG5uLkxpbmVhcihlbmNvZGVyX2RpbSwgZGVjb2Rlcl9kaW0pXG4gICAgICAgIHNlbGYubWFza190b2tlbiA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcygxLCAxLCBkZWNvZGVyX2RpbSkpXG4gICAgICAgIHNlbGYucG9zX2VtYmVkICA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcygxLCBudW1fcGF0Y2hlcyArIDEsIGRlY29kZXJfZGltKSlcbiAgICAgICAgc2VsZi5ibG9ja3MgPSBubi5Nb2R1bGVMaXN0KFtUcmFuc2Zvcm1lckJsb2NrKGRlY29kZXJfZGltLCBudW1faGVhZHMpIGZvciBfIGluIHJhbmdlKGRlcHRoKV0pXG4gICAgICAgIHNlbGYubm9ybSA9IG5uLkxheWVyTm9ybShkZWNvZGVyX2RpbSlcbiAgICAgICAgc2VsZi5wcmVkID0gbm4uTGluZWFyKGRlY29kZXJfZGltLCBwYXRjaF9zaXplICogcGF0Y2hfc2l6ZSAqIDMpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4X2VuY29kZWQsIGlkc19yZXN0b3JlKTpcbiAgICAgICAgeCA9IHNlbGYuZGVjb2Rlcl9lbWJlZCh4X2VuY29kZWQpICAgIyBwcm9qZWN0IGVuY29kZXIgZGltIC1cdTAwM2UgZGVjb2RlciBkaW1cbiAgICAgICAgeF92aXMgPSB4WzosIDE6LCA6XSAgICAgICAgICAgICAgICAgIyBzdHJpcCBjbHMgdG9rZW5cbiAgICAgICAgQiwgbl92aXMsIEQgPSB4X3Zpcy5zaGFwZVxuICAgICAgICBuX21hc2sgPSBpZHNfcmVzdG9yZS5zaGFwZVsxXSAtIG5fdmlzXG5cbiAgICAgICAgIyBFeHBhbmQgbWFzayB0b2tlbnMgdG8gZmlsbCBtYXNrZWQgcG9zaXRpb25zXG4gICAgICAgIG1hc2tfdG9rZW5zID0gc2VsZi5tYXNrX3Rva2VuLmV4cGFuZChCLCBuX21hc2ssIC0xKVxuICAgICAgICB4X2Z1bGwgPSB0b3JjaC5jYXQoW3hfdmlzLCBtYXNrX3Rva2Vuc10sIGRpbT0xKSAgICMgW0IsIE4sIERdXG5cbiAgICAgICAgIyBVbnNodWZmbGU6IHJlc3RvcmUgb3JpZ2luYWwgcGF0Y2ggb3JkZXIgdXNpbmcgaW52ZXJzZSBwZXJtdXRhdGlvblxuICAgICAgICB4X2Z1bGwgPSB0b3JjaC5nYXRoZXIoXG4gICAgICAgICAgICB4X2Z1bGwsIDEsIGlkc19yZXN0b3JlLnVuc3F1ZWV6ZSgtMSkuZXhwYW5kKC0xLCAtMSwgRClcbiAgICAgICAgKVxuICAgICAgICAjIEFkZCBwb3NpdGlvbmFsIGVtYmVkZGluZyAoZnVsbCBzZXF1ZW5jZSkgYW5kIHByZXBlbmQgY2xzIHRva2VuXG4gICAgICAgIHhfZnVsbCA9IHhfZnVsbCArIHNlbGYucG9zX2VtYmVkWzosIDE6LCA6XVxuICAgICAgICB4ID0gdG9yY2guY2F0KFt4WzosIDoxLCA6XSwgeF9mdWxsXSwgZGltPTEpXG4gICAgICAgIGZvciBibG9jayBpbiBzZWxmLmJsb2NrczpcbiAgICAgICAgICAgIHggPSBibG9jayh4KVxuICAgICAgICB4ID0gc2VsZi5ub3JtKHgpXG4gICAgICAgIHJldHVybiBzZWxmLnByZWQoeFs6LCAxOiwgOl0pICAgIyBbQiwgTiwgcGF0Y2hfc2l6ZV4yICogM10ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZWNvbnN0cnVjdGlvbiBUYXJnZXQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJhdGhlciB0aGFuIHJhdyBwaXhlbCB2YWx1ZXMsIE1BRSBub3JtYWxpemVzIGVhY2ggcGF0Y2hcdTAwMjdzIHBpeGVscyB0byB6ZXJvIG1lYW4gYW5kIHVuaXQgdmFyaWFuY2UgYmVmb3JlIGNvbXB1dGluZyB0aGUgbG9zcy4gVGhpcyBwZXItcGF0Y2ggbm9ybWFsaXphdGlvbiBpbXByb3ZlcyB0cmFpbmluZyBzdGFiaWxpdHkgYW5kIGZpbmFsIHJlcHJlc2VudGF0aW9uIHF1YWxpdHkuIFRoZSBsb3NzIGlzIG9ubHkgY29tcHV0ZWQgb24gbWFza2VkIHBhdGNoZXMg4oCUIHZpc2libGUgcGF0Y2hlcyBhcmUgaWdub3JlZC4gQXQgaW5mZXJlbmNlIHRpbWUsIHByZWRpY3Rpb25zIGNhbiBiZSB1bm5vcm1hbGl6ZWQgYmFjayB0byBSR0IgZm9yIHZpc3VhbGl6YXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiBwYXRjaGlmeShpbWdzLCBwYXRjaF9zaXplPTE2KTpcbiAgICAjIENvbnZlcnQgW0IsIDMsIEgsIFddIGltYWdlcyB0byBbQiwgTiwgcGF0Y2hfc2l6ZV4yICogM10gcGF0Y2ggdG9rZW5zXG4gICAgcCA9IHBhdGNoX3NpemVcbiAgICBoID0gdyA9IGltZ3Muc2hhcGVbLTFdIC8vIHBcbiAgICB4ID0gaW1ncy5yZXNoYXBlKGltZ3Muc2hhcGVbMF0sIDMsIGgsIHAsIHcsIHApXG4gICAgeCA9IHRvcmNoLmVpbnN1bShcdTAwMjduY2hwd3EtXHUwMDNlbmh3cHFjXHUwMDI3LCB4KVxuICAgIHJldHVybiB4LnJlc2hhcGUoaW1ncy5zaGFwZVswXSwgaCAqIHcsIHAgKiBwICogMylcblxuZGVmIGNvbXB1dGVfcmVjb25zdHJ1Y3Rpb25fdGFyZ2V0KGltZ3MsIHBhdGNoX3NpemU9MTYpOlxuICAgICMgUGVyLXBhdGNoIG1lYW4vc3RkIG5vcm1hbGl6YXRpb24g4oCUIHRoZSBNQUUgcmVjb25zdHJ1Y3Rpb24gdGFyZ2V0XG4gICAgdGFyZ2V0ID0gcGF0Y2hpZnkoaW1ncywgcGF0Y2hfc2l6ZSlcbiAgICBtZWFuID0gdGFyZ2V0Lm1lYW4oZGltPS0xLCBrZWVwZGltPVRydWUpXG4gICAgc3RkICA9IHRhcmdldC52YXIoZGltPS0xLCBrZWVwZGltPVRydWUpLnNxcnQoKS5jbGFtcChtaW49MWUtNilcbiAgICByZXR1cm4gKHRhcmdldCAtIG1lYW4pIC8gc3RkXG5cbmRlZiB1bm5vcm1hbGl6ZV9mb3Jfdml6KHByZWQsIG9yaWdfaW1ncywgcGF0Y2hfc2l6ZT0xNik6XG4gICAgIyBSZXZlcnNlIHBhdGNoIG5vcm1hbGl6YXRpb24gZm9yIHZpc3VhbGl6YXRpb25cbiAgICB0YXJnZXQgPSBwYXRjaGlmeShvcmlnX2ltZ3MsIHBhdGNoX3NpemUpXG4gICAgbWVhbiA9IHRhcmdldC5tZWFuKGRpbT0tMSwga2VlcGRpbT1UcnVlKVxuICAgIHN0ZCAgPSB0YXJnZXQudmFyKGRpbT0tMSwga2VlcGRpbT1UcnVlKS5zcXJ0KCkuY2xhbXAobWluPTFlLTYpXG4gICAgcmV0dXJuIHByZWQgKiBzdGQgKyBtZWFuXG5cbmRlZiBtYWVfbG9zcyhwcmVkLCBpbWdzLCBtYXNrLCBwYXRjaF9zaXplPTE2KTpcbiAgICAjIE1TRSBsb3NzIGNvbXB1dGVkIG9ubHkgb24gbWFza2VkIHBhdGNoZXNcbiAgICB0YXJnZXQgPSBjb21wdXRlX3JlY29uc3RydWN0aW9uX3RhcmdldChpbWdzLCBwYXRjaF9zaXplKSAgIyBbQiwgTiwgcF4yKjNdXG4gICAgbG9zcyA9ICgocHJlZCAtIHRhcmdldCkgKiogMikubWVhbihkaW09LTEpICAgICAgICAgICAgICAgIyBbQiwgTl0gcGVyLXBhdGNoXG4gICAgcmV0dXJuIChsb3NzICogbWFzaykuc3VtKCkgLyBtYXNrLnN1bSgpICAgICAgICAgICAgICAgICAgICMgbWVhbiBvdmVyIG1hc2tlZCJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5zaWdodCIsInRpdGxlIjoiV2h5IDc1JSBhbmQgTm90IDE1JT8iLCJjb250ZW50IjoiQkVSVCBtYXNrcyBvbmx5IDE1JSBvZiB0b2tlbnMgYmVjYXVzZSBsYW5ndWFnZSBpcyBpbmZvcm1hdGlvbi1kZW5zZSDigJQgcmVtb3ZpbmcgbW9yZSBkZXN0cm95cyBtb3N0IGNvbnRleHQuIEltYWdlcyBhcmUgZmFyIG1vcmUgc3BhdGlhbGx5IHJlZHVuZGFudDogYWRqYWNlbnQgcGl4ZWxzIGFyZSBoaWdobHkgY29ycmVsYXRlZCwgc28gbG93IG1hc2sgcmF0aW9zIGFsbG93IHRyaXZpYWwgdGV4dHVyZSBpbnRlcnBvbGF0aW9uLiBUaGUgNzUlIHJhdGlvIGZvcmNlcyB0aGUgbW9kZWwgdG8gcmVhc29uIGdsb2JhbGx5IGFib3V0IG9iamVjdCBzdHJ1Y3R1cmUsIHlpZWxkaW5nIHNlbWFudGljYWxseSByaWNoZXIgZmVhdHVyZXMuIEFibGF0aW9ucyBzaG93IHBlcmZvcm1hbmNlIGRyb3BzIHNoYXJwbHkgYXQgbWFzayByYXRpb3MgYmVsb3cgNjAlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhpZ2ggTWFzayBSYXRpbyBhbmQgV2h5IEl0IFdvcmtzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgaGlnaCBtYXNrIHJhdGlvIGlzIHNpbXVsdGFuZW91c2x5IHRoZSBlZmZpY2llbmN5IG1lY2hhbmlzbSBhbmQgdGhlIHJlcHJlc2VudGF0aW9uLXF1YWxpdHkgbWVjaGFuaXNtLiBXaXRoIG9ubHkgMjUlIG9mIHBhdGNoZXMgdmlzaWJsZSwgdGhlIGVuY29kZXIgY2Fubm90IHJlbHkgb24gbmVhcmJ5IHBpeGVsIGludGVycG9sYXRpb24g4oCUIGl0IG11c3QgbGVhcm4gb2JqZWN0LWxldmVsIHNlbWFudGljcy4gQWJsYXRpb25zIGluIHRoZSBvcmlnaW5hbCBwYXBlciBjb25maXJtIHRoYXQgcGVyZm9ybWFuY2UgZGVncmFkZXMgc2lnbmlmaWNhbnRseSBhdCBsb3dlciBtYXNrIHJhdGlvcyAoNDDigJM1MCUpLCB2YWxpZGF0aW5nIHRoYXQgdGFzayBkaWZmaWN1bHR5IGRyaXZlcyByZXByZXNlbnRhdGlvbiBxdWFsaXR5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiNzUlIG1hc2sgcmF0aW86IGVuY29kZXIgcHJvY2Vzc2VzIDPigJM0eCBmZXdlciB0b2tlbnMsIGdpdmluZyBhIHNpZ25pZmljYW50IHRyYWluaW5nIHNwZWVkdXAiLCJIaWdoIG1hc2tpbmcgZm9yY2VzIGhvbGlzdGljIHVuZGVyc3RhbmRpbmcgb2Ygc2hhcGUsIHRleHR1cmUsIGFuZCBvYmplY3Qgc3RydWN0dXJlIiwiTm8gbWFzayB0b2tlbnMgaW4gdGhlIGVuY29kZXIgcHJldmVudHMgZXhwbG9pdGF0aW9uIG9mIHRyaXZpYWwgbG9jYWwgY29ycmVsYXRpb25zIiwiTGlnaHR3ZWlnaHQgZGVjb2RlciAoNCBibG9ja3MpIGNhbiByZWNvbnN0cnVjdCBmcm9tIHN0cm9uZyBlbmNvZGVyIHJlcHJlc2VudGF0aW9ucyIsIk5vcm1hbGl6ZWQgcGl4ZWwgdGFyZ2V0cyAocGVyLXBhdGNoIG1lYW4vc3RkKSBpbXByb3ZlIHRyYWluaW5nIHN0YWJpbGl0eSB2cyByYXcgUkdCIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gd2l0aCBSZWxhdGVkIE1ldGhvZHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1BRSBzaXRzIGluIGEgZmFtaWx5IG9mIG1hc2tlZCBpbWFnZSBtb2RlbGluZyAoTUlNKSBhcHByb2FjaGVzIHRoYXQgZGlmZmVyIGluIHJlY29uc3RydWN0aW9uIHRhcmdldHMsIG1hc2tpbmcgc3RyYXRlZ2llcywgYW5kIGFyY2hpdGVjdHVyZXMuIFNpbU1JTSB1c2VzIGEgc2ltaWxhciBwaXhlbC1wcmVkaWN0aW9uIHRhcmdldCBidXQgcGFzc2VzIGFsbCB0b2tlbnMgKGluY2x1ZGluZyBtYXNrIHRva2VucykgdG8gdGhlIGVuY29kZXIuIEJFaVQgcHJlZGljdHMgZGlzY3JldGUgdmlzdWFsIHRva2VucyBmcm9tIGEgcHJldHJhaW5lZCB0b2tlbml6ZXIuIE1hc2tGZWF0IHByZWRpY3RzIEhPRyAoSGlzdG9ncmFtcyBvZiBPcmllbnRlZCBHcmFkaWVudHMpIGZlYXR1cmVzLCBhIGhhbmQtY3JhZnRlZCBkZXNjcmlwdG9yLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJNYXNrIFJhdGlvIiwiUmVjb25zdHJ1Y3Rpb24gVGFyZ2V0IiwiRW5jb2RlciBJbnB1dCIsIklOLTFLIEZpbmUtdHVuZSBUb3AtMSJdLCJyb3dzIjpbWyJNQUUiLCI3NSUiLCJOb3JtYWxpemVkIHBpeGVsIHZhbHVlcyIsIlZpc2libGUgcGF0Y2hlcyBvbmx5IiwiODcuOCUgKFZpVC1IKSJdLFsiU2ltTUlNIiwiNjAlIiwiUmF3IHBpeGVsIHZhbHVlcyIsIkFsbCBwYXRjaGVzICsgbWFzayB0b2tlbnMiLCI4NC4wJSAoU3dpblYyLUgpIl0sWyJCRWlUIiwiNDAlIiwiRGlzY3JldGUgdmlzdWFsIHRva2VucyAoZFZBRSkiLCJBbGwgcGF0Y2hlcyArIG1hc2sgdG9rZW5zIiwiODYuMyUgKFZpVC1MKSJdLFsiTWFza0ZlYXQiLCI0MCUiLCJIT0cgZmVhdHVyZXMiLCJBbGwgcGF0Y2hlcyArIG1hc2sgdG9rZW5zIiwiODQuMCUgKFZpVC1MKSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmluZS10dW5pbmcgYW5kIFNjYWxhYmlsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZnRlciBwcmUtdHJhaW5pbmcsIHRoZSBkZWNvZGVyIGlzIGRpc2NhcmRlZCBhbmQgb25seSB0aGUgZW5jb2RlciBpcyBmaW5lLXR1bmVkIG9uIGRvd25zdHJlYW0gdGFza3MuIE1BRSBhY2hpZXZlcyA4Ny44JSB0b3AtMSBvbiBJbWFnZU5ldCB3aXRoIFZpVC1ILCBzdXJwYXNzaW5nIHN1cGVydmlzZWQgcHJlLXRyYWluaW5nIGJhc2VsaW5lcy4gQ3J1Y2lhbGx5LCBsYXJnZXIgVmlUIG1vZGVscyBiZW5lZml0IG1vcmUgZnJvbSBNQUUgcHJlLXRyYWluaW5nIOKAlCBWaVQtTCBhbmQgVmlULUggc2hvdyBsYXJnZXIgcmVsYXRpdmUgZ2FpbnMgdGhhbiBWaVQtQiwgc3VnZ2VzdGluZyBNQUUgaXMgZXNwZWNpYWxseSB3ZWxsLXN1aXRlZCB0byBsYXJnZS1zY2FsZSBzZWxmLXN1cGVydmlzZWQgbGVhcm5pbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBkYXRhLWxpbWl0ZWQgZmluZS10dW5pbmcgcmVnaW1lcyB3aXRoIG9ubHkgMSUgb2YgSW1hZ2VOZXQgbGFiZWxzICh+MTIsODAwIGltYWdlcyksIE1BRSBwcmUtdHJhaW5lZCBWaVQtTCBhY2hpZXZlcyB+NzMlIHRvcC0xIGFjY3VyYWN5LCBkcmFtYXRpY2FsbHkgb3V0cGVyZm9ybWluZyB0cmFpbmluZyBmcm9tIHNjcmF0Y2guIFRoaXMgY29uZmlybXMgdGhhdCBNQUUgbGVhcm5zIGdlbnVpbmUgdmlzdWFsIHNlbWFudGljcyByYXRoZXIgdGhhbiBkYXRhc2V0LXNwZWNpZmljIHNob3J0Y3V0cywgbWFraW5nIGl0IGEgcG93ZXJmdWwgZm91bmRhdGlvbiBmb3IgdHJhbnNmZXIgbGVhcm5pbmcuIn1d"
---
# MAE — Masked Autoencoders for Vision

Masked Autoencoders (MAE) by He et al. (2022) demonstrated that a surprisingly simple idea — mask most of an image and reconstruct the missing parts — scales remarkably well for visual pre-training. By masking 75% of patches and using an asymmetric encoder-decoder, MAE achieves strong representations without contrastive pairs, negative samples, or momentum networks.

## What is MAE?

MAE is a self-supervised pre-training method for vision transformers (ViT). The core idea mirrors BERT in NLP: randomly mask a subset of input tokens (patches) and train the model to reconstruct the originals. The key insight is that vision data is far more redundant than language — a high masking ratio (75% vs BERT's 15%) forces the model to learn holistic scene understanding rather than interpolating from nearby visible pixels.

## Patch Masking Strategy

MAE divides the input image into non-overlapping patches (typically 16x16 pixels). A random 75% of patches are masked. Crucially, the encoder sees only the remaining 25% — mask tokens are never passed to the encoder. This asymmetric design is the key efficiency win: the encoder processes only a quarter of the patches, yielding a 3–4x speedup over processing all patches.

```python
import torch
import torch.nn as nn

def random_masking(x, mask_ratio=0.75):
    # x: [B, N, D] patch embeddings
    # Returns: visible tokens, binary mask (1=masked), restore indices
    B, N, D = x.shape
    keep = int(N * (1 - mask_ratio))  # number of patches to keep

    # Generate per-sample random noise for independent shuffling
    noise = torch.rand(B, N, device=x.device)

    # Sort patches by noise to get a random permutation
    ids_shuffle = torch.argsort(noise, dim=1)        # ascending
    ids_restore = torch.argsort(ids_shuffle, dim=1)  # inverse permutation

    # Keep only the first `keep` patches (lowest noise values)
    ids_keep = ids_shuffle[:, :keep]
    x_visible = torch.gather(
        x, dim=1,
        index=ids_keep.unsqueeze(-1).expand(-1, -1, D)
    )

    # Binary mask: 0 = kept, 1 = masked (aligned with ids_restore order)
    mask = torch.ones(B, N, device=x.device)
    mask[:, :keep] = 0
    mask = torch.gather(mask, dim=1, index=ids_restore)

    return x_visible, mask, ids_restore

# Example usage: 196 patches (14x14 grid for 224px image with 16px patches)
# x = torch.randn(8, 196, 768)  # batch of 8, 196 patches, 768-dim
# x_vis, mask, ids_restore = random_masking(x, mask_ratio=0.75)
# x_vis.shape  -> [8, 49, 768]  (only 25% visible)
```

## The MAE Encoder

The encoder is a standard ViT (e.g., ViT-L with 24 blocks and 1024-dim embeddings) that operates exclusively on visible patches. Positional embeddings are added before masking so the encoder knows spatial positions. No mask tokens enter the encoder — this is what makes it computationally efficient. The encoder produces rich representations for only the visible 25% of patches.

```python
import torch
import torch.nn as nn
from einops import rearrange

class TransformerBlock(nn.Module):
    def __init__(self, dim, heads, mlp_ratio=4.0):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)
        self.attn = nn.MultiheadAttention(dim, heads, batch_first=True)
        self.norm2 = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, int(dim * mlp_ratio)), nn.GELU(),
            nn.Linear(int(dim * mlp_ratio), dim)
        )
    def forward(self, x):
        x = x + self.attn(self.norm1(x), self.norm1(x), self.norm1(x))[0]
        return x + self.mlp(self.norm2(x))

class MAEEncoder(nn.Module):
    def __init__(self, img_size=224, patch_size=16, embed_dim=768, depth=12, num_heads=12):
        super().__init__()
        self.patch_embed = nn.Conv2d(3, embed_dim, patch_size, stride=patch_size)
        num_patches = (img_size // patch_size) ** 2
        self.pos_embed = nn.Parameter(torch.zeros(1, num_patches + 1, embed_dim))
        self.cls_token  = nn.Parameter(torch.zeros(1, 1, embed_dim))
        self.blocks = nn.ModuleList([TransformerBlock(embed_dim, num_heads) for _ in range(depth)])
        self.norm = nn.LayerNorm(embed_dim)

    def forward(self, x, ids_keep):
        B = x.shape[0]
        x = rearrange(self.patch_embed(x), 'b d h w -> b (h w) d')
        x = x + self.pos_embed[:, 1:, :]                                  # spatial pos-embed
        D = x.shape[-1]
        x = torch.gather(x, 1, ids_keep.unsqueeze(-1).expand(-1, -1, D)) # keep visible only
        cls = self.cls_token.expand(B, -1, -1)
        x = torch.cat([cls, x], dim=1)
        for block in self.blocks:
            x = block(x)
        return self.norm(x)  # [B, 1+keep, D]
```

## The MAE Decoder

The decoder is intentionally lightweight — only 4 transformer blocks (vs 12+ in the encoder) and a smaller embedding dimension (512 vs 768). It receives encoded visible tokens plus learnable mask tokens inserted at masked positions. Positional embeddings are added so the decoder knows which patches to reconstruct. The output head projects to pixel values for each patch.

```python
import torch
import torch.nn as nn

class MAEDecoder(nn.Module):
    def __init__(self, num_patches=196, encoder_dim=768, decoder_dim=512,
                 depth=4, num_heads=8, patch_size=16):
        super().__init__()
        self.decoder_embed = nn.Linear(encoder_dim, decoder_dim)
        self.mask_token = nn.Parameter(torch.zeros(1, 1, decoder_dim))
        self.pos_embed  = nn.Parameter(torch.zeros(1, num_patches + 1, decoder_dim))
        self.blocks = nn.ModuleList([TransformerBlock(decoder_dim, num_heads) for _ in range(depth)])
        self.norm = nn.LayerNorm(decoder_dim)
        self.pred = nn.Linear(decoder_dim, patch_size * patch_size * 3)

    def forward(self, x_encoded, ids_restore):
        x = self.decoder_embed(x_encoded)   # project encoder dim -> decoder dim
        x_vis = x[:, 1:, :]                 # strip cls token
        B, n_vis, D = x_vis.shape
        n_mask = ids_restore.shape[1] - n_vis

        # Expand mask tokens to fill masked positions
        mask_tokens = self.mask_token.expand(B, n_mask, -1)
        x_full = torch.cat([x_vis, mask_tokens], dim=1)   # [B, N, D]

        # Unshuffle: restore original patch order using inverse permutation
        x_full = torch.gather(
            x_full, 1, ids_restore.unsqueeze(-1).expand(-1, -1, D)
        )
        # Add positional embedding (full sequence) and prepend cls token
        x_full = x_full + self.pos_embed[:, 1:, :]
        x = torch.cat([x[:, :1, :], x_full], dim=1)
        for block in self.blocks:
            x = block(x)
        x = self.norm(x)
        return self.pred(x[:, 1:, :])   # [B, N, patch_size^2 * 3]
```

## Reconstruction Target

Rather than raw pixel values, MAE normalizes each patch's pixels to zero mean and unit variance before computing the loss. This per-patch normalization improves training stability and final representation quality. The loss is only computed on masked patches — visible patches are ignored. At inference time, predictions can be unnormalized back to RGB for visualization.

```python
import torch
import numpy as np
import matplotlib.pyplot as plt

def patchify(imgs, patch_size=16):
    # Convert [B, 3, H, W] images to [B, N, patch_size^2 * 3] patch tokens
    p = patch_size
    h = w = imgs.shape[-1] // p
    x = imgs.reshape(imgs.shape[0], 3, h, p, w, p)
    x = torch.einsum('nchpwq->nhwpqc', x)
    return x.reshape(imgs.shape[0], h * w, p * p * 3)

def compute_reconstruction_target(imgs, patch_size=16):
    # Per-patch mean/std normalization — the MAE reconstruction target
    target = patchify(imgs, patch_size)
    mean = target.mean(dim=-1, keepdim=True)
    std  = target.var(dim=-1, keepdim=True).sqrt().clamp(min=1e-6)
    return (target - mean) / std

def unnormalize_for_viz(pred, orig_imgs, patch_size=16):
    # Reverse patch normalization for visualization
    target = patchify(orig_imgs, patch_size)
    mean = target.mean(dim=-1, keepdim=True)
    std  = target.var(dim=-1, keepdim=True).sqrt().clamp(min=1e-6)
    return pred * std + mean

def mae_loss(pred, imgs, mask, patch_size=16):
    # MSE loss computed only on masked patches
    target = compute_reconstruction_target(imgs, patch_size)  # [B, N, p^2*3]
    loss = ((pred - target) ** 2).mean(dim=-1)               # [B, N] per-patch
    return (loss * mask).sum() / mask.sum()                   # mean over masked
```

> **Why 75% and Not 15%?**: BERT masks only 15% of tokens because language is information-dense — removing more destroys most context. Images are far more spatially redundant: adjacent pixels are highly correlated, so low mask ratios allow trivial texture interpolation. The 75% ratio forces the model to reason globally about object structure, yielding semantically richer features. Ablations show performance drops sharply at mask ratios below 60%.

## High Mask Ratio and Why It Works

The high mask ratio is simultaneously the efficiency mechanism and the representation-quality mechanism. With only 25% of patches visible, the encoder cannot rely on nearby pixel interpolation — it must learn object-level semantics. Ablations in the original paper confirm that performance degrades significantly at lower mask ratios (40–50%), validating that task difficulty drives representation quality.

- 75% mask ratio: encoder processes 3–4x fewer tokens, giving a significant training speedup
- High masking forces holistic understanding of shape, texture, and object structure
- No mask tokens in the encoder prevents exploitation of trivial local correlations
- Lightweight decoder (4 blocks) can reconstruct from strong encoder representations
- Normalized pixel targets (per-patch mean/std) improve training stability vs raw RGB

## Comparison with Related Methods

MAE sits in a family of masked image modeling (MIM) approaches that differ in reconstruction targets, masking strategies, and architectures. SimMIM uses a similar pixel-prediction target but passes all tokens (including mask tokens) to the encoder. BEiT predicts discrete visual tokens from a pretrained tokenizer. MaskFeat predicts HOG (Histograms of Oriented Gradients) features, a hand-crafted descriptor.

| Method | Mask Ratio | Reconstruction Target | Encoder Input | IN-1K Fine-tune Top-1 |
| --- | --- | --- | --- | --- |
| MAE | 75% | Normalized pixel values | Visible patches only | 87.8% (ViT-H) |
| SimMIM | 60% | Raw pixel values | All patches + mask tokens | 84.0% (SwinV2-H) |
| BEiT | 40% | Discrete visual tokens (dVAE) | All patches + mask tokens | 86.3% (ViT-L) |
| MaskFeat | 40% | HOG features | All patches + mask tokens | 84.0% (ViT-L) |

## Fine-tuning and Scalability

After pre-training, the decoder is discarded and only the encoder is fine-tuned on downstream tasks. MAE achieves 87.8% top-1 on ImageNet with ViT-H, surpassing supervised pre-training baselines. Crucially, larger ViT models benefit more from MAE pre-training — ViT-L and ViT-H show larger relative gains than ViT-B, suggesting MAE is especially well-suited to large-scale self-supervised learning.

In data-limited fine-tuning regimes with only 1% of ImageNet labels (~12,800 images), MAE pre-trained ViT-L achieves ~73% top-1 accuracy, dramatically outperforming training from scratch. This confirms that MAE learns genuine visual semantics rather than dataset-specific shortcuts, making it a powerful foundation for transfer learning.

