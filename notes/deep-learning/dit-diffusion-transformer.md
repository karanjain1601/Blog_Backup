---
title: "DiT — Diffusion Transformer Replacing U-Net"
slug: "dit-diffusion-transformer"
description: "DiT replaces the U-Net backbone in latent diffusion with a scalable Vision Transformer, using patchified latent tokens, adaLN-Zero conditioning, and ViT-style scaling laws to achieve state-of-the-art FID on ImageNet while enabling the MM-DiT architectures used in SD3 and FLUX."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlmZnVzaW9uIFRyYW5zZm9ybWVycyAoRGlULCBQZWVibGVzIFx1MDAyNiBYaWUgMjAyMykgcmVwbGFjZSB0aGUgVS1OZXQgYmFja2JvbmUgdXNlZCBpbiBzdGFuZGFyZCBsYXRlbnQgZGlmZnVzaW9uIG1vZGVscyB3aXRoIGEgVmlzaW9uIFRyYW5zZm9ybWVyLCBwcm9jZXNzaW5nIHRoZSBpbWFnZSBsYXRlbnQgYXMgYSBzZXF1ZW5jZSBvZiBmbGF0dGVuZWQgcGF0Y2hlcy4gVGhpcyBhcmNoaXRlY3R1cmFsIHN3YXAgaXMgbW90aXZhdGVkIGJ5IHRoZSBvYnNlcnZhdGlvbiB0aGF0IFZpVCBwZXJmb3JtYW5jZSBzY2FsZXMgcmVsaWFibHkgd2l0aCBjb21wdXRlICh1bmxpa2UgVS1OZXRzIHdoaWNoIHNob3cgZGltaW5pc2hpbmcgcmV0dXJucyksIGFuZCB0aGF0IHRyYW5zZm9ybWVycyBoYW5kbGUgdmFyaWFibGUtbGVuZ3RoIGNvbmRpdGlvbmluZyBpbnB1dHMgbW9yZSBuYXR1cmFsbHkgdmlhIHNlbGYtYXR0ZW50aW9uLiBEaVQtWEwvMiBhY2hpZXZlcyBGSUQgMi4yNyBvbiBJbWFnZU5ldCAyNTbDlzI1Niwgc3VycGFzc2luZyB0aGUgVS1OZXQtYmFzZWQgQURNIG1vZGVsLCBhbmQgZm9ybXMgdGhlIGJhY2tib25lIG9mIFNEMyBhbmQgRkxVWC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGcm9tIFUtTmV0IHRvIFZpc2lvbiBUcmFuc2Zvcm1lciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFUtTmV0IHdhcyB0aGUgbmF0dXJhbCBjaG9pY2UgZm9yIGRpZmZ1c2lvbjogaXRzIGVuY29kZXItZGVjb2RlciB3aXRoIHNraXAgY29ubmVjdGlvbnMgbWlycm9ycyB0aGUgZGVub2lzaW5nIHByb2Nlc3Mgb2YgcmVmaW5pbmcgZmVhdHVyZXMgYXQgbXVsdGlwbGUgcmVzb2x1dGlvbnMuIEhvd2V2ZXIsIFUtTmV0cyBkbyBub3Qgc2NhbGUgYXMgY2xlYW5seSBhcyB0cmFuc2Zvcm1lcnMg4oCUIGFkZGluZyBsYXllcnMgb2Z0ZW4gcmVxdWlyZXMgaGFuZC1kZXNpZ25lZCBjaGFuZ2VzIHRvIHRoZSBhcmNoaXRlY3R1cmUuIERpVCB0cmVhdHMgdGhlIGxhdGVudCBncmlkIGFzIGEgdG9rZW4gc2VxdWVuY2UgKGxpa2UgVmlUKSwgYXBwbGllcyBzdGFuZGFyZCB0cmFuc2Zvcm1lciBibG9ja3MsIGFuZCByZWxpZXMgb24gdGhlIGF0dGVudGlvbiBtZWNoYW5pc21cdTAwMjdzIGdsb2JhbCByZWNlcHRpdmUgZmllbGQgcmF0aGVyIHRoYW4gaGllcmFyY2hpY2FsIGZlYXR1cmUgZXh0cmFjdGlvbi4gVGhlIGNvbmRpdGlvbmluZyBvbiB0aW1lc3RlcCB0IGFuZCBjbGFzcyBsYWJlbCAob3IgdGV4dCkgaXMgaW5qZWN0ZWQgcGVyLWJsb2NrIHZpYSBBZGFwdGl2ZSBMYXllck5vcm0uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGF0Y2hpZnkgTGF0ZW50IElucHV0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgVkFFIGxhdGVudCBvZiBzaGFwZSAoQywgSC84LCBXLzgpIOKAlCB0eXBpY2FsbHkgKDQsIDMyLCAzMikgZm9yIGEgMjU2w5cyNTYgaW1hZ2Ug4oCUIGlzIHNwbGl0IGludG8gbm9uLW92ZXJsYXBwaW5nIHBhdGNoZXMgb2Ygc2l6ZSBww5dwIChwPTIgb3IgcD00KS4gRWFjaCBwYXRjaCBpcyBmbGF0dGVuZWQgYW5kIGxpbmVhcmx5IHByb2plY3RlZCB0byBhIGQtZGltZW5zaW9uYWwgdG9rZW4gZW1iZWRkaW5nLiBGb3IgYSAzMsOXMzIgbGF0ZW50IHdpdGggcGF0Y2ggc2l6ZSAyLCB3ZSBnZXQgKDMyLzIpwrIgPSAyNTYgdG9rZW5zLiBTbWFsbGVyIHBhdGNoZXMgZ2l2ZSBtb3JlIHRva2VucyBhbmQgZmluZXIgc3BhdGlhbCByZXNvbHV0aW9uIGJ1dCBpbmNyZWFzZSBzZXF1ZW5jZSBsZW5ndGggcXVhZHJhdGljYWxseS4gQSBsZWFybmVkIHBvc2l0aW9uYWwgZW1iZWRkaW5nIGlzIGFkZGVkIGJlZm9yZSB0aGUgdHJhbnNmb3JtZXIgYmxvY2tzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBQYXRjaEVtYmVkKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiUGF0Y2hpZnkgaW1hZ2UgbGF0ZW50IGludG8gdG9rZW4gc2VxdWVuY2UgZm9yIERpVC5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2hhbm5lbHM9NCwgcGF0Y2hfc2l6ZT0yLCBlbWJlZF9kaW09MTE1Mik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBhdGNoX3NpemUgPSBwYXRjaF9zaXplXG4gICAgICAgIHNlbGYucHJvaiA9IG5uLkNvbnYyZChpbl9jaGFubmVscywgZW1iZWRfZGltLCBrZXJuZWxfc2l6ZT1wYXRjaF9zaXplLCBzdHJpZGU9cGF0Y2hfc2l6ZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICAjIHg6IChCLCBDLCBILCBXKSBsYXRlbnRcbiAgICAgICAgQiwgQywgSCwgVyA9IHguc2hhcGVcbiAgICAgICAgYXNzZXJ0IEggJSBzZWxmLnBhdGNoX3NpemUgPT0gMCBhbmQgVyAlIHNlbGYucGF0Y2hfc2l6ZSA9PSAwXG4gICAgICAgIHRva2VucyA9IHNlbGYucHJvaih4KSAgICAgICAgICAjIChCLCBlbWJlZF9kaW0sIEgvcCwgVy9wKVxuICAgICAgICB0b2tlbnMgPSB0b2tlbnMuZmxhdHRlbigyKSAgICAgIyAoQiwgZW1iZWRfZGltLCBOKSB3aGVyZSBOPShIL3ApKihXL3ApXG4gICAgICAgIHRva2VucyA9IHRva2Vucy50cmFuc3Bvc2UoMSwgMikgICMgKEIsIE4sIGVtYmVkX2RpbSlcbiAgICAgICAgcmV0dXJuIHRva2Vuc1xuXG5kZWYgYWRkX3Bvc2l0aW9uYWxfZW1iZWRkaW5nKHRva2VucywgcG9zX2VtYmVkKTpcbiAgICByZXR1cm4gdG9rZW5zICsgcG9zX2VtYmVkWzosIDp0b2tlbnMuc2hhcGVbMV0sIDpdXG5cbiMgRGVtbzogMjU2eDI1NiBpbWFnZSAtXHUwMDNlIDMyeDMyIFZBRSBsYXRlbnQgKDQgY2hhbm5lbHMpIC1cdTAwM2UgMjU2IHRva2Vuc1xucGF0Y2hfZW1iZWQgPSBQYXRjaEVtYmVkKGluX2NoYW5uZWxzPTQsIHBhdGNoX3NpemU9MiwgZW1iZWRfZGltPTExNTIpXG5sYXRlbnQgPSB0b3JjaC5yYW5kbigyLCA0LCAzMiwgMzIpICAjIGJhdGNoIG9mIDIgbGF0ZW50c1xudG9rZW5zID0gcGF0Y2hfZW1iZWQobGF0ZW50KVxucHJpbnQoZlx1MDAyN0xhdGVudDoge2xhdGVudC5zaGFwZX0gLVx1MDAzZSBUb2tlbnM6IHt0b2tlbnMuc2hhcGV9XHUwMDI3KSAgIyAoMiwgMjU2LCAxMTUyKVxuXG4jIEZvciA1MTJ4NTEyIGltYWdlOiA2NHg2NCBsYXRlbnQsIHBhdGNoPTIgLVx1MDAzZSAxMDI0IHRva2Vuc1xubGF0ZW50X2xnID0gdG9yY2gucmFuZG4oMSwgNCwgNjQsIDY0KVxudG9rZW5zX2xnID0gcGF0Y2hfZW1iZWQobGF0ZW50X2xnKVxucHJpbnQoZlx1MDAyNzY0eDY0IGxhdGVudCAtXHUwMDNlIHt0b2tlbnNfbGcuc2hhcGVbMV19IHRva2Vuc1x1MDAyNykgICMgMTAyNCB0b2tlbnMifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZGFwdGl2ZSBMYXllck5vcm0gWmVybyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlUIGNvbmRpdGlvbnMgZWFjaCB0cmFuc2Zvcm1lciBibG9jayBvbiBib3RoIHRoZSB0aW1lc3RlcCB0IGFuZCB0aGUgY2xhc3MgbGFiZWwgKG9yIHRleHQgZW1iZWRkaW5nKSB2aWEgQWRhcHRpdmUgTGF5ZXIgTm9ybWFsaXphdGlvbiAoYWRhTE4pLiBUaGUgY29uZGl0aW9uIGlzIGNvbXB1dGVkIGFzOiAozrEsIM6yLCDOsywgzrFcdTAwMjcsIM6yXHUwMDI3LCDOs1x1MDAyNykgPSBMaW5lYXIoU2lMVShjb25kKSksIHdoZXJlIGNvbmQgaXMgdGhlIHN1bSBvZiB0aW1lc3RlcCBhbmQgY2xhc3MgZW1iZWRkaW5ncy4gVGhlIExheWVyTm9ybSBvdXRwdXQgaXMgdGhlbiBtb2R1bGF0ZWQ6IGFkYUxOKHgpID0gzrPCt0xheWVyTm9ybSh4KSArIM6yLCBhbmQgdGhlIGF0dGVudGlvbi9GRk4gb3V0cHV0IGlzIHNjYWxlZCBieSDOsSBiZWZvcmUgdGhlIHJlc2lkdWFsIGFkZGl0aW9uLiBUaGUgWmVybyB2YXJpYW50IGluaXRpYWxpc2VzIHRoZSBmaW5hbCBsaW5lYXIgbGF5ZXIgb2YgZWFjaCBhZGFMTiB0byB6ZXJvLCBzbyBhdCB0cmFpbmluZyBzdGFydCBlYWNoIGJsb2NrIGFjdHMgYXMgdGhlIGlkZW50aXR5IOKAlCBjcml0aWNhbCBmb3IgdHJhaW5pbmcgc3RhYmlsaXR5IGF0IHNjYWxlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBBZGFMTlplcm8obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJBZGFwdGl2ZSBMYXllck5vcm0tWmVybzogY29uZGl0aW9uaW5nIHZpYSBzY2FsZStzaGlmdCwgemVyby1pbml0IG91dHB1dC5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaGlkZGVuX3NpemUsIGNvbmRfZGltKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubm9ybSA9IG5uLkxheWVyTm9ybShoaWRkZW5fc2l6ZSwgZWxlbWVudHdpc2VfYWZmaW5lPUZhbHNlKVxuICAgICAgICAjIDYgb3V0cHV0czogc2hpZnQsIHNjYWxlIGZvciBwcmUtYXR0bjsgZ2F0ZSBmb3IgYXR0bjsgc2hpZnQsIHNjYWxlLCBnYXRlIGZvciBGRk5cbiAgICAgICAgc2VsZi5hZGFMTl9tb2R1bGF0aW9uID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihjb25kX2RpbSwgNiAqIGhpZGRlbl9zaXplKVxuICAgICAgICApXG4gICAgICAgIG5uLmluaXQuemVyb3NfKHNlbGYuYWRhTE5fbW9kdWxhdGlvblstMV0ud2VpZ2h0KVxuICAgICAgICBubi5pbml0Lnplcm9zXyhzZWxmLmFkYUxOX21vZHVsYXRpb25bLTFdLmJpYXMpXG5cbiAgICBkZWYgbW9kdWxhdGUoc2VsZiwgeCwgc2hpZnQsIHNjYWxlKTpcbiAgICAgICAgcmV0dXJuIHggKiAoMSArIHNjYWxlLnVuc3F1ZWV6ZSgxKSkgKyBzaGlmdC51bnNxdWVlemUoMSlcblxuICAgIGRlZiBnZXRfbW9kdWxhdGlvbnMoc2VsZiwgY29uZCk6XG4gICAgICAgIG1vZHMgPSBzZWxmLmFkYUxOX21vZHVsYXRpb24oY29uZCkuY2h1bmsoNiwgZGltPTEpXG4gICAgICAgIHJldHVybiBtb2RzICAjIHNoaWZ0X2F0dG4sIHNjYWxlX2F0dG4sIGdhdGVfYXR0biwgc2hpZnRfZmYsIHNjYWxlX2ZmLCBnYXRlX2ZmXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5hZCA9IEFkYUxOWmVybyhoaWRkZW5fc2l6ZT0xMTUyLCBjb25kX2RpbT0xMTUyKVxuY29uZCA9IHRvcmNoLnJhbmRuKDQsIDExNTIpICAjIHRpbWVzdGVwICsgY2xhc3MgY29uZGl0aW9uXG5tb2RzID0gYWQuZ2V0X21vZHVsYXRpb25zKGNvbmQpXG5wcmludChmXHUwMDI3YWRhTE4tWmVybyBtb2R1bGF0aW9ucyBhdCBpbml0IChzaG91bGQgYmUgfjApOiB7W20uYWJzKCkubWF4KCkuaXRlbSgpOi40Zn0gZm9yIG0gaW4gbW9kc119XHUwMDI3LnJlcGxhY2UoXCJbXCIsIFwiW1wiKS5yZXBsYWNlKFwiXVwiLCBcIl1cIikpXG5wcmludChmXHUwMDI3QmxvY2tzIHN0YXJ0IGFzIGlkZW50aXR5IGF0IGluaXQg4oCUIHN0YWJsZSB0cmFpbmluZyBmcm9tIHNjcmF0Y2hcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGlUIEJsb2NrIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBEaVRCbG9jayhubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkRpVCB0cmFuc2Zvcm1lciBibG9jazogVmlUIGF0dGVudGlvbiArIEZGTiB3aXRoIGFkYUxOLVplcm8gY29uZGl0aW9uaW5nLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBoaWRkZW5fc2l6ZT0xMTUyLCBuX2hlYWRzPTE2LCBjb25kX2RpbT0xMTUyLCBtbHBfcmF0aW89NC4wKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubm9ybTEgPSBubi5MYXllck5vcm0oaGlkZGVuX3NpemUsIGVsZW1lbnR3aXNlX2FmZmluZT1GYWxzZSlcbiAgICAgICAgc2VsZi5ub3JtMiA9IG5uLkxheWVyTm9ybShoaWRkZW5fc2l6ZSwgZWxlbWVudHdpc2VfYWZmaW5lPUZhbHNlKVxuICAgICAgICBzZWxmLmF0dG4gPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oaGlkZGVuX3NpemUsIG5faGVhZHMsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIG1scF9kaW0gPSBpbnQoaGlkZGVuX3NpemUgKiBtbHBfcmF0aW8pXG4gICAgICAgIHNlbGYubWxwID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW5fc2l6ZSwgbWxwX2RpbSksIG5uLkdFTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihtbHBfZGltLCBoaWRkZW5fc2l6ZSlcbiAgICAgICAgKVxuICAgICAgICBzZWxmLmFkYUxOID0gbm4uU2VxdWVudGlhbChubi5TaUxVKCksIG5uLkxpbmVhcihjb25kX2RpbSwgNiAqIGhpZGRlbl9zaXplKSlcbiAgICAgICAgbm4uaW5pdC56ZXJvc18oc2VsZi5hZGFMTlstMV0ud2VpZ2h0KVxuICAgICAgICBubi5pbml0Lnplcm9zXyhzZWxmLmFkYUxOWy0xXS5iaWFzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgYyk6XG4gICAgICAgIG1vZHMgPSBzZWxmLmFkYUxOKGMpLmNodW5rKDYsIGRpbT0tMSkgICMgNiBtb2R1bGF0aW9uIHZlY3RvcnNcbiAgICAgICAgc2hpZnRfYSwgc2NhbGVfYSwgZ2F0ZV9hLCBzaGlmdF9tLCBzY2FsZV9tLCBnYXRlX20gPSBtb2RzXG4gICAgICAgICMgQXR0ZW50aW9uIHdpdGggYWRhTE4gY29uZGl0aW9uaW5nXG4gICAgICAgIGggPSBzZWxmLm5vcm0xKHgpICogKDEgKyBzY2FsZV9hWzosIE5vbmVdKSArIHNoaWZ0X2FbOiwgTm9uZV1cbiAgICAgICAgYXR0bl9vdXQsIF8gPSBzZWxmLmF0dG4oaCwgaCwgaClcbiAgICAgICAgeCA9IHggKyBnYXRlX2FbOiwgTm9uZV0gKiBhdHRuX291dFxuICAgICAgICAjIEZGTiB3aXRoIGFkYUxOIGNvbmRpdGlvbmluZ1xuICAgICAgICBoID0gc2VsZi5ub3JtMih4KSAqICgxICsgc2NhbGVfbVs6LCBOb25lXSkgKyBzaGlmdF9tWzosIE5vbmVdXG4gICAgICAgIHggPSB4ICsgZ2F0ZV9tWzosIE5vbmVdICogc2VsZi5tbHAoaClcbiAgICAgICAgcmV0dXJuIHhcblxuYmxvY2sgPSBEaVRCbG9jayhoaWRkZW5fc2l6ZT0xMTUyLCBuX2hlYWRzPTE2LCBjb25kX2RpbT0xMTUyKVxudG9rZW5zID0gdG9yY2gucmFuZG4oMiwgMjU2LCAxMTUyKSAgIyAoYmF0Y2gsIE5fdG9rZW5zLCBoaWRkZW4pXG5jb25kICAgPSB0b3JjaC5yYW5kbigyLCAxMTUyKSAgICAgICAgIyB0aW1lc3RlcCArIGNsYXNzIGNvbmRpdGlvblxub3V0ID0gYmxvY2sodG9rZW5zLCBjb25kKVxucHJpbnQoZlx1MDAyN0RpVCBibG9jazoge3Rva2Vucy5zaGFwZX0gLVx1MDAzZSB7b3V0LnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsaW5nIExhd3MgYW5kIEZMT1BzIHZzIEZJRCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGlUIGZvbGxvd3MgdGhlIHNhbWUgc2NhbGluZyBsYXdzIGFzIFZpVDogRklEIGRlY3JlYXNlcyBhcyBhIHBvd2VyIGxhdyBpbiBjb21wdXRlIChHRkxPUHMgcGVyIHNhbXBsZSkuIERpVC1YTC8yIHVzZXMgMjAwME0gR0ZMT1BzIHBlciBzYW1wbGUgYW5kIGFjaGlldmVzIEZJRCAyLjI3LCB3aGlsZSBEaVQtUy8yICgzM00gcGFyYW1zKSBhY2hpZXZlcyBGSUQgNjguNCDigJQgYSAzMMOXIGNvbXB1dGUgaW5jcmVhc2UgeWllbGRzIDMww5cgYmV0dGVyIEZJRC4gQ3J1Y2lhbGx5LCB0aGlzIHJlbGF0aW9uc2hpcCBpcyBzbW9vdGggYW5kIHByZWRpY3RhYmxlLCBtYWtpbmcgRGlUIGFtZW5hYmxlIHRvIGNvbXB1dGUtb3B0aW1hbCB0cmFpbmluZy4gVGhlIFUtTmV0IEFETSBtb2RlbCBhY2hpZXZlcyBGSUQgMTAuOTQgd2l0aCBjb21wYXJhYmxlIGNvbXB1dGUsIGNvbmZpcm1pbmcgdGhhdCBEaVRcdTAwMjdzIHRyYW5zZm9ybWVyIGJhY2tib25lIGlzIG1vcmUgY29tcHV0ZS1lZmZpY2llbnQgZm9yIGRpZmZ1c2lvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBEaVQgc2NhbGluZzogYXBwcm94aW1hdGUgRklEIHZzIEdGTE9QcyAoZnJvbSBQZWVibGVzIFx1MDAyNiBYaWUgMjAyMyBUYWJsZSAxKVxuZGl0X3Jlc3VsdHMgPSBbXG4gICAgKFx1MDAyN0RpVC1TLzJcdTAwMjcsICAzMywgICA2LCAgICA2OC40KSxcbiAgICAoXHUwMDI3RGlULUIvMlx1MDAyNywgIDEzMCwgIDIzLCAgIDQzLjUpLFxuICAgIChcdTAwMjdEaVQtTC8yXHUwMDI3LCAgNDU4LCAgODAsICAgMjMuNSksXG4gICAgKFx1MDAyN0RpVC1YTC8yXHUwMDI3LCA2NzUsICAxMTksICA5LjYyKSxcbiAgICAoXHUwMDI3QURNIChVLU5ldClcdTAwMjcsIDU1NCwgOTgsIDEwLjk0KSxcbl1cbnByaW50KGZcdTAwMjd7XCJNb2RlbFwiOlx1MDAzYzE1fSB7XCJQYXJhbXMgKE0pXCI6XHUwMDNlMTJ9IHtcIkdGTE9Qc1wiOlx1MDAzZTh9IHtcIkZJRFwiOlx1MDAzZTh9IHtcInZzIEFETVwiOlx1MDAzZTEwfVx1MDAyNylcbnByaW50KFx1MDAyNy1cdTAwMjcgKiA1OClcbmFkbV9maWQgPSAxMC45NFxuZm9yIG5hbWUsIHBhcmFtcywgZ2Zsb3BzLCBmaWQgaW4gZGl0X3Jlc3VsdHM6XG4gICAgZGVsdGEgPSBmXHUwMDI3e2ZpZCAtIGFkbV9maWQ6Ky4yZn1cdTAwMjcgaWYgbmFtZSAhPSBcdTAwMjdBRE0gKFUtTmV0KVx1MDAyNyBlbHNlIFx1MDAyNyhiYXNlbGluZSlcdTAwMjdcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMTV9IHtwYXJhbXM6XHUwMDNlMTJ9IHtnZmxvcHM6XHUwMDNlOH0ge2ZpZDpcdTAwM2U4LjJmfSB7ZGVsdGE6XHUwMDNlMTB9XHUwMDI3KVxuXG5wcmludCgpXG4jIFNjYWxpbmcgbGF3OiBsb2ctbG9nIHJlbGF0aW9uc2hpcFxuZ2Zsb3BzID0gbnAuYXJyYXkoWzYsIDIzLCA4MCwgMTE5XSlcbmZpZHMgPSBucC5hcnJheShbNjguNCwgNDMuNSwgMjMuNSwgOS42Ml0pXG5jb2VmID0gbnAucG9seWZpdChucC5sb2coZ2Zsb3BzKSwgbnAubG9nKGZpZHMpLCAxKVxucHJpbnQoZlx1MDAyN1Bvd2VyIGxhdyBmaXQ6IEZJRCB+IEdGTE9Qc157Y29lZlswXTouMmZ9IChleHBvbmVudCBcdTAwM2MgMCA9IGltcHJvdmVtZW50IHdpdGggc2NhbGUpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1NLURpVCBpbiBTRDMgYW5kIEZMVVgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNEMyBpbnRyb2R1Y2VzIE11bHRpLU1vZGFsIERpVCAoTU0tRGlUKSwgd2hlcmUgaW1hZ2UgdG9rZW5zIGFuZCB0ZXh0IHRva2VucyBhcmUgcHJvY2Vzc2VkIGpvaW50bHkgaW4gdGhlIHNhbWUgdHJhbnNmb3JtZXIgYmxvY2tzIHdpdGggc2VwYXJhdGUgd2VpZ2h0cyBmb3IgZWFjaCBtb2RhbGl0eS4gRWFjaCBNTS1EaVQgYmxvY2sgaGFzIHR3byBpbmRlcGVuZGVudCBzZXRzIG9mIGF0dGVudGlvbiBwcm9qZWN0aW9ucyDigJQgb25lIGZvciBpbWFnZSB0b2tlbnMgYW5kIG9uZSBmb3IgdGV4dCB0b2tlbnMg4oCUIGJ1dCB0aGUgYXR0ZW50aW9uIGl0c2VsZiBpcyBjb21wdXRlZCBvdmVyIHRoZSBjb25jYXRlbmF0ZWQgc2VxdWVuY2UsIGFsbG93aW5nIGZ1bGwgYmlkaXJlY3Rpb25hbCBjcm9zcy1tb2RhbCBhdHRlbnRpb24uIFRoaXMgaXMgbW9yZSBwb3dlcmZ1bCB0aGFuIHRoZSBjcm9zcy1hdHRlbnRpb24gbWVjaGFuaXNtIGluIFNEIDEueCBVLU5ldCBiZWNhdXNlIHRleHQgdG9rZW5zIGNhbiBhbHNvIGF0dGVuZCB0byBpbWFnZSB0b2tlbnMuIFNEMyB1c2VzIDE2LWNoYW5uZWwgbGF0ZW50cyAodnMgNCBpbiBTRCAxLngpLCB0cmlwbGluZyB0aGUgaW5mb3JtYXRpb24gY2FwYWNpdHkgb2YgdGhlIGNvbXByZXNzZWQgcmVwcmVzZW50YXRpb24uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJGTFVYOiBTb1RBIERpVCBUZXh0LXRvLUltYWdlIiwiY29udGVudCI6IkZMVVguMSAoQmxhY2sgRm9yZXN0IExhYnMsIDIwMjQpIGlzIGEgRGlULWJhc2VkIG1vZGVsIHRoYXQgYWNoaWV2ZXMgc3RhdGUtb2YtdGhlLWFydCB0ZXh0LXRvLWltYWdlIHF1YWxpdHkgb24gaHVtYW4gcHJlZmVyZW5jZSBiZW5jaG1hcmtzLiBGTFVYIHVzZXMgYSBoeWJyaWQgYXJjaGl0ZWN0dXJlIGNvbWJpbmluZyBNTS1EaVQgYmxvY2tzIChmb3Igam9pbnQgaW1hZ2UtdGV4dCBhdHRlbnRpb24pIGFuZCBzaW5nbGUtc3RyZWFtIERpVCBibG9ja3MgKGZvciBpbWFnZS1vbmx5IHJlZmluZW1lbnQpLCB3aXRoIGZsb3cgbWF0Y2hpbmcgYXMgdGhlIHRyYWluaW5nIG9iamVjdGl2ZS4gRkxVWC4xLWRldiAoMTJCIHBhcmFtZXRlcnMpIGlzIHB1YmxpY2x5IGF2YWlsYWJsZSBhbmQgb3V0cGVyZm9ybXMgTWlkam91cm5leSB2NiBvbiBwcm9tcHQgYWRoZXJlbmNlIHdoaWxlIEZMVVguMS1zY2huZWxsIHJlcXVpcmVzIG9ubHkgNCBORkUuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFyY2hpdGVjdHVyZSIsIlBhcmFtcyIsIkdGTE9Qcy9zYW1wbGUiLCJJbWFnZU5ldCAyNTYgRklEIiwiVHJhaW5pbmcgQ29tcHV0ZSIsIkFyY2hpdGVjdHVyZSBUeXBlIl0sInJvd3MiOltbIkFETSAoVS1OZXQsIGNsYXNzLWNvbmQpIiwiNTU0TSIsIn45OCIsIjEwLjk0IiwifjEwMDAgQTEwMCBHUFUtZGF5cyIsIlUtTmV0IHdpdGggc2VsZitjcm9zcy1hdHRuIl0sWyJEaVQtUy8yIiwiMzNNIiwiNiIsIjY4LjQiLCJ+NyBBMTAwIEdQVS1kYXlzIiwiU2hhbGxvdyBWaVQsIHBhdGNoPTIiXSxbIkRpVC1CLzIiLCIxMzBNIiwiMjMiLCI0My41IiwifjI4IEExMDAgR1BVLWRheXMiLCJCRVJULXNjYWxlIFZpVCwgcGF0Y2g9MiJdLFsiRGlULVhMLzIiLCI2NzVNIiwiMTE5IiwiMi4yNyAody8gQ0ZHKSIsIn4xMDAwIEExMDAgR1BVLWRheXMiLCJMYXJnZSBWaVQsIHBhdGNoPTIsIFNvVEEiXSxbIkZMVVguMSAoYXBwcm94KSIsIjEyQiIsIlx1MDAzZTEwMDAiLCJOL0EgKFQySSkiLCJcdTAwM2VcdTAwM2UxMGsgR1BVLWRheXMiLCJNTS1EaVQgKyBzaW5nbGUtc3RyZWFtIERpVCJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQYXRjaCBzaXplIHA9MiBnaXZlcyA0w5cgbW9yZSB0b2tlbnMgdGhhbiBwPTQgZm9yIHRoZSBzYW1lIGxhdGVudCDigJQgYmV0dGVyIHNwYXRpYWwgZGV0YWlsIGJ1dCA0w5cgbW9yZSBjb21wdXRlLiIsImFkYUxOLVplcm9cdTAwMjdzIHplcm8taW5pdCBlbnN1cmVzIGJsb2NrcyBzdGFydCBhcyBpZGVudGl0eSDigJQgd2l0aG91dCB0aGlzLCBkZWVwIERpVHMgZGl2ZXJnZSBhdCB0aGUgc3RhcnQgb2YgdHJhaW5pbmcuIiwiRGlULVhMLzIgdXNlcyAyOCB0cmFuc2Zvcm1lciBibG9ja3Mgd2l0aCBoaWRkZW4gc2l6ZSAxMTUyIGFuZCAxNiBhdHRlbnRpb24gaGVhZHMg4oCUIHRoZSBzYW1lIHNjYWxlIGFzIFZpVC1MLiIsIk1NLURpVCBlbmFibGVzIHRleHQgdG9rZW5zIHRvIGF0dGVuZCB0byBpbWFnZSB0b2tlbnMsIGdpdmluZyB0ZXh0IHN0cm9uZ2VyIGNvbnRyb2wgdGhhbiBjcm9zcy1hdHRlbnRpb24gYWxvbmUuIiwiRkxVWC4xLXNjaG5lbGwgYWNoaWV2ZXMgNC1zdGVwIGdlbmVyYXRpb24gdmlhIGd1aWRhbmNlIGRpc3RpbGxhdGlvbiDigJQgdGhlIERpVCBhcmNoaXRlY3R1cmUgaXMgY29tcGF0aWJsZSB3aXRoIGFsbCBkaXN0aWxsYXRpb24gbWV0aG9kcy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IERlc2lnbiBQcmluY2lwbGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaHJlZSBkZXNpZ24gZGVjaXNpb25zIGRlZmluZSBEaVRcdTAwMjdzIHN1Y2Nlc3M6ICgxKSBQYXRjaGlmeS10aGVuLXRyYW5zZm9ybWVyOiB0cmVhdGluZyB0aGUgbGF0ZW50IGFzIGEgdG9rZW4gc2VxdWVuY2UgZ2l2ZXMgZ2xvYmFsIHJlY2VwdGl2ZSBmaWVsZCBmcm9tIGxheWVyIDEsIHVubGlrZSBVLU5ldFx1MDAyN3MgbGltaXRlZCBrZXJuZWwgc2l6ZXMuICgyKSBhZGFMTi1aZXJvOiBjb25kaXRpb25pbmcgdmlhIHNjYWxlK3NoaWZ0K2dhdGUgd2l0aCB6ZXJvIGluaXRpYWxpc2F0aW9uIGlzIG1vcmUgZXhwcmVzc2l2ZSB0aGFuIGluLWNvbnRleHQgY29uZGl0aW9uaW5nIChwcmVwZW5kaW5nIGNvbmRpdGlvbiB0b2tlbnMpIGFuZCBtb3JlIHN0YWJsZSB0aGFuIGNyb3NzLWF0dGVudGlvbiBjb25kaXRpb25pbmcuICgzKSBQcmVkaWN0IM61IG9yIHY6IERpVCB1c2VzIHRoZSBzYW1lIG5vaXNlIHByZWRpY3Rpb24gb2JqZWN0aXZlIGFzIEREUE0gYnV0IGdhaW5zIGZyb20gdGhlIHRyYW5zZm9ybWVyXHUwMDI3cyBiZXR0ZXIgY2FwYWNpdHkuIFRoZSBrZXkgbGVzc29uIGlzIHRoYXQgYXJjaGl0ZWN0dXJhbCBpbXByb3ZlbWVudHMgY29tcG91bmQgd2l0aCBzY2FsZSDigJQgRGlUIGJlbmVmaXRzIG1vcmUgZnJvbSAxMMOXIG1vcmUgY29tcHV0ZSB0aGFuIFUtTmV0IGRvZXMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# DiT — Diffusion Transformer Replacing U-Net

Diffusion Transformers (DiT, Peebles & Xie 2023) replace the U-Net backbone used in standard latent diffusion models with a Vision Transformer, processing the image latent as a sequence of flattened patches. This architectural swap is motivated by the observation that ViT performance scales reliably with compute (unlike U-Nets which show diminishing returns), and that transformers handle variable-length conditioning inputs more naturally via self-attention. DiT-XL/2 achieves FID 2.27 on ImageNet 256×256, surpassing the U-Net-based ADM model, and forms the backbone of SD3 and FLUX.

## From U-Net to Vision Transformer

The U-Net was the natural choice for diffusion: its encoder-decoder with skip connections mirrors the denoising process of refining features at multiple resolutions. However, U-Nets do not scale as cleanly as transformers — adding layers often requires hand-designed changes to the architecture. DiT treats the latent grid as a token sequence (like ViT), applies standard transformer blocks, and relies on the attention mechanism's global receptive field rather than hierarchical feature extraction. The conditioning on timestep t and class label (or text) is injected per-block via Adaptive LayerNorm.

## Patchify Latent Input

The VAE latent of shape (C, H/8, W/8) — typically (4, 32, 32) for a 256×256 image — is split into non-overlapping patches of size p×p (p=2 or p=4). Each patch is flattened and linearly projected to a d-dimensional token embedding. For a 32×32 latent with patch size 2, we get (32/2)² = 256 tokens. Smaller patches give more tokens and finer spatial resolution but increase sequence length quadratically. A learned positional embedding is added before the transformer blocks.

```python
import torch
import torch.nn as nn

class PatchEmbed(nn.Module):
    """Patchify image latent into token sequence for DiT."""
    def __init__(self, in_channels=4, patch_size=2, embed_dim=1152):
        super().__init__()
        self.patch_size = patch_size
        self.proj = nn.Conv2d(in_channels, embed_dim, kernel_size=patch_size, stride=patch_size)

    def forward(self, x):
        # x: (B, C, H, W) latent
        B, C, H, W = x.shape
        assert H % self.patch_size == 0 and W % self.patch_size == 0
        tokens = self.proj(x)          # (B, embed_dim, H/p, W/p)
        tokens = tokens.flatten(2)     # (B, embed_dim, N) where N=(H/p)*(W/p)
        tokens = tokens.transpose(1, 2)  # (B, N, embed_dim)
        return tokens

def add_positional_embedding(tokens, pos_embed):
    return tokens + pos_embed[:, :tokens.shape[1], :]

# Demo: 256x256 image -> 32x32 VAE latent (4 channels) -> 256 tokens
patch_embed = PatchEmbed(in_channels=4, patch_size=2, embed_dim=1152)
latent = torch.randn(2, 4, 32, 32)  # batch of 2 latents
tokens = patch_embed(latent)
print(f'Latent: {latent.shape} -> Tokens: {tokens.shape}')  # (2, 256, 1152)

# For 512x512 image: 64x64 latent, patch=2 -> 1024 tokens
latent_lg = torch.randn(1, 4, 64, 64)
tokens_lg = patch_embed(latent_lg)
print(f'64x64 latent -> {tokens_lg.shape[1]} tokens')  # 1024 tokens
```

## Adaptive LayerNorm Zero

DiT conditions each transformer block on both the timestep t and the class label (or text embedding) via Adaptive Layer Normalization (adaLN). The condition is computed as: (α, β, γ, α', β', γ') = Linear(SiLU(cond)), where cond is the sum of timestep and class embeddings. The LayerNorm output is then modulated: adaLN(x) = γ·LayerNorm(x) + β, and the attention/FFN output is scaled by α before the residual addition. The Zero variant initialises the final linear layer of each adaLN to zero, so at training start each block acts as the identity — critical for training stability at scale.

```python
import torch
import torch.nn as nn

class AdaLNZero(nn.Module):
    """Adaptive LayerNorm-Zero: conditioning via scale+shift, zero-init output."""
    def __init__(self, hidden_size, cond_dim):
        super().__init__()
        self.norm = nn.LayerNorm(hidden_size, elementwise_affine=False)
        # 6 outputs: shift, scale for pre-attn; gate for attn; shift, scale, gate for FFN
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(),
            nn.Linear(cond_dim, 6 * hidden_size)
        )
        nn.init.zeros_(self.adaLN_modulation[-1].weight)
        nn.init.zeros_(self.adaLN_modulation[-1].bias)

    def modulate(self, x, shift, scale):
        return x * (1 + scale.unsqueeze(1)) + shift.unsqueeze(1)

    def get_modulations(self, cond):
        mods = self.adaLN_modulation(cond).chunk(6, dim=1)
        return mods  # shift_attn, scale_attn, gate_attn, shift_ff, scale_ff, gate_ff

torch.manual_seed(0)
ad = AdaLNZero(hidden_size=1152, cond_dim=1152)
cond = torch.randn(4, 1152)  # timestep + class condition
mods = ad.get_modulations(cond)
print(f'adaLN-Zero modulations at init (should be ~0): {[m.abs().max().item():.4f} for m in mods]}'.replace("[", "[").replace("]", "]"))
print(f'Blocks start as identity at init — stable training from scratch')
```

## DiT Block Architecture

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DiTBlock(nn.Module):
    """DiT transformer block: ViT attention + FFN with adaLN-Zero conditioning."""
    def __init__(self, hidden_size=1152, n_heads=16, cond_dim=1152, mlp_ratio=4.0):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_size, elementwise_affine=False)
        self.norm2 = nn.LayerNorm(hidden_size, elementwise_affine=False)
        self.attn = nn.MultiheadAttention(hidden_size, n_heads, batch_first=True)
        mlp_dim = int(hidden_size * mlp_ratio)
        self.mlp = nn.Sequential(
            nn.Linear(hidden_size, mlp_dim), nn.GELU(),
            nn.Linear(mlp_dim, hidden_size)
        )
        self.adaLN = nn.Sequential(nn.SiLU(), nn.Linear(cond_dim, 6 * hidden_size))
        nn.init.zeros_(self.adaLN[-1].weight)
        nn.init.zeros_(self.adaLN[-1].bias)

    def forward(self, x, c):
        mods = self.adaLN(c).chunk(6, dim=-1)  # 6 modulation vectors
        shift_a, scale_a, gate_a, shift_m, scale_m, gate_m = mods
        # Attention with adaLN conditioning
        h = self.norm1(x) * (1 + scale_a[:, None]) + shift_a[:, None]
        attn_out, _ = self.attn(h, h, h)
        x = x + gate_a[:, None] * attn_out
        # FFN with adaLN conditioning
        h = self.norm2(x) * (1 + scale_m[:, None]) + shift_m[:, None]
        x = x + gate_m[:, None] * self.mlp(h)
        return x

block = DiTBlock(hidden_size=1152, n_heads=16, cond_dim=1152)
tokens = torch.randn(2, 256, 1152)  # (batch, N_tokens, hidden)
cond   = torch.randn(2, 1152)        # timestep + class condition
out = block(tokens, cond)
print(f'DiT block: {tokens.shape} -> {out.shape}')
```

## Scaling Laws and FLOPs vs FID

DiT follows the same scaling laws as ViT: FID decreases as a power law in compute (GFLOPs per sample). DiT-XL/2 uses 2000M GFLOPs per sample and achieves FID 2.27, while DiT-S/2 (33M params) achieves FID 68.4 — a 30× compute increase yields 30× better FID. Crucially, this relationship is smooth and predictable, making DiT amenable to compute-optimal training. The U-Net ADM model achieves FID 10.94 with comparable compute, confirming that DiT's transformer backbone is more compute-efficient for diffusion.

```python
import torch
import numpy as np

# DiT scaling: approximate FID vs GFLOPs (from Peebles & Xie 2023 Table 1)
dit_results = [
    ('DiT-S/2',  33,   6,    68.4),
    ('DiT-B/2',  130,  23,   43.5),
    ('DiT-L/2',  458,  80,   23.5),
    ('DiT-XL/2', 675,  119,  9.62),
    ('ADM (U-Net)', 554, 98, 10.94),
]
print(f'{"Model":<15} {"Params (M)":>12} {"GFLOPs":>8} {"FID":>8} {"vs ADM":>10}')
print('-' * 58)
adm_fid = 10.94
for name, params, gflops, fid in dit_results:
    delta = f'{fid - adm_fid:+.2f}' if name != 'ADM (U-Net)' else '(baseline)'
    print(f'{name:<15} {params:>12} {gflops:>8} {fid:>8.2f} {delta:>10}')

print()
# Scaling law: log-log relationship
gflops = np.array([6, 23, 80, 119])
fids = np.array([68.4, 43.5, 23.5, 9.62])
coef = np.polyfit(np.log(gflops), np.log(fids), 1)
print(f'Power law fit: FID ~ GFLOPs^{coef[0]:.2f} (exponent < 0 = improvement with scale)')
```

## MM-DiT in SD3 and FLUX

SD3 introduces Multi-Modal DiT (MM-DiT), where image tokens and text tokens are processed jointly in the same transformer blocks with separate weights for each modality. Each MM-DiT block has two independent sets of attention projections — one for image tokens and one for text tokens — but the attention itself is computed over the concatenated sequence, allowing full bidirectional cross-modal attention. This is more powerful than the cross-attention mechanism in SD 1.x U-Net because text tokens can also attend to image tokens. SD3 uses 16-channel latents (vs 4 in SD 1.x), tripling the information capacity of the compressed representation.

> **FLUX: SoTA DiT Text-to-Image**: FLUX.1 (Black Forest Labs, 2024) is a DiT-based model that achieves state-of-the-art text-to-image quality on human preference benchmarks. FLUX uses a hybrid architecture combining MM-DiT blocks (for joint image-text attention) and single-stream DiT blocks (for image-only refinement), with flow matching as the training objective. FLUX.1-dev (12B parameters) is publicly available and outperforms Midjourney v6 on prompt adherence while FLUX.1-schnell requires only 4 NFE.

| Architecture | Params | GFLOPs/sample | ImageNet 256 FID | Training Compute | Architecture Type |
| --- | --- | --- | --- | --- | --- |
| ADM (U-Net, class-cond) | 554M | ~98 | 10.94 | ~1000 A100 GPU-days | U-Net with self+cross-attn |
| DiT-S/2 | 33M | 6 | 68.4 | ~7 A100 GPU-days | Shallow ViT, patch=2 |
| DiT-B/2 | 130M | 23 | 43.5 | ~28 A100 GPU-days | BERT-scale ViT, patch=2 |
| DiT-XL/2 | 675M | 119 | 2.27 (w/ CFG) | ~1000 A100 GPU-days | Large ViT, patch=2, SoTA |
| FLUX.1 (approx) | 12B | >1000 | N/A (T2I) | >>10k GPU-days | MM-DiT + single-stream DiT |

- Patch size p=2 gives 4× more tokens than p=4 for the same latent — better spatial detail but 4× more compute.
- adaLN-Zero's zero-init ensures blocks start as identity — without this, deep DiTs diverge at the start of training.
- DiT-XL/2 uses 28 transformer blocks with hidden size 1152 and 16 attention heads — the same scale as ViT-L.
- MM-DiT enables text tokens to attend to image tokens, giving text stronger control than cross-attention alone.
- FLUX.1-schnell achieves 4-step generation via guidance distillation — the DiT architecture is compatible with all distillation methods.

## Key Design Principles

Three design decisions define DiT's success: (1) Patchify-then-transformer: treating the latent as a token sequence gives global receptive field from layer 1, unlike U-Net's limited kernel sizes. (2) adaLN-Zero: conditioning via scale+shift+gate with zero initialisation is more expressive than in-context conditioning (prepending condition tokens) and more stable than cross-attention conditioning. (3) Predict ε or v: DiT uses the same noise prediction objective as DDPM but gains from the transformer's better capacity. The key lesson is that architectural improvements compound with scale — DiT benefits more from 10× more compute than U-Net does.

---

