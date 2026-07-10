---
title: "β-VAE — Disentangled Representation Learning"
slug: "beta-vae"
description: "How β-VAE promotes disentangled representations by increasing the KL weight β>1, why higher β trades reconstruction quality for interpretable independent latent factors, and how FactorVAE and β-TCVAE isolate the total correlation penalty for better disentanglement-quality tradeoffs."
tags: ["deep-learning", "generative-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoizrItVkFFIChIaWdnaW5zIGV0IGFsLiAyMDE3KSBleHRlbmRzIHRoZSBzdGFuZGFyZCBWQUUgYnkgbXVsdGlwbHlpbmcgdGhlIEtMIHRlcm0gYnkgYSBzY2FsYXIgzrIgXHUwMDNlIDE6IEwgPSBFW2xvZyBwKHh8eildIC0gzrLCt0tMKHFfz4Yoenx4KSB8fCBwKHopKS4gV2hlbiDOsj0xIHRoZSBvYmplY3RpdmUgaXMgdGhlIHN0YW5kYXJkIEVMQk8uIEluY3JlYXNpbmcgzrIgaW1wb3NlcyBhIHN0cm9uZ2VyIGluZm9ybWF0aW9uIGJvdHRsZW5lY2sgb24gdGhlIGxhdGVudCBjb2RlLCBmb3JjaW5nIHRoZSBlbmNvZGVyIHRvIHVzZSBlYWNoIGxhdGVudCBkaW1lbnNpb24gc3BhcmluZ2x5IGFuZCBpbmRlcGVuZGVudGx5LiBUaGUgcmVzdWx0IGlzIGRpc2VudGFuZ2xlbWVudDogZWFjaCBsYXRlbnQgZGltZW5zaW9uIHRlbmRzIHRvIGVuY29kZSBvbmUgaW50ZXJwcmV0YWJsZSBnZW5lcmF0aXZlIGZhY3RvciAoZS5nLiwgcm90YXRpb24gYW5nbGUsIG9iamVjdCBzY2FsZSwgeC1wb3NpdGlvbikgaW5kZXBlbmRlbnRseSBvZiB0aGUgb3RoZXJzLiBUaGUgdHJhZGVvZmYgaXMgdGhhdCBoaWdoIM6yIGRlZ3JhZGVzIHJlY29uc3RydWN0aW9uIHF1YWxpdHkg4oCUIHRoZSBzdHJvbmdlciBib3R0bGVuZWNrIGxlYXZlcyBsZXNzIGNhcGFjaXR5IGZvciBwcmVjaXNlIHJlY29uc3RydWN0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSDOsiBcdTAwM2UgMSBQcm9tb3RlcyBEaXNlbnRhbmdsZW1lbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBLTCB0ZXJtIEtMKHFfz4Yoenx4KSB8fCBwKHopKSA9IEtMKHFfz4Yoenx4KSB8fCBOKDAsSSkpIGNhbiBiZSBkZWNvbXBvc2VkIGFzOiBpbmRleC1jb2RlIG11dHVhbCBpbmZvcm1hdGlvbiBJKHg7eikgKyB0b3RhbCBjb3JyZWxhdGlvbiBUQyh6KSArIGRpbWVuc2lvbi13aXNlIEtMLiBUb3RhbCBjb3JyZWxhdGlvbiBUQyh6KSA9IEtMKHEoeikgfHwg4oiP4rG8IHEoeuKxvCkpIG1lYXN1cmVzIHN0YXRpc3RpY2FsIGRlcGVuZGVuY2UgYW1vbmcgbGF0ZW50IGRpbWVuc2lvbnMg4oCUIGl0IGlzIHplcm8gb25seSB3aGVuIGFsbCBkaW1lbnNpb25zIGFyZSBtdXR1YWxseSBpbmRlcGVuZGVudC4gUGVuYWxpemluZyBLTCB3aXRoIM6yIFx1MDAzZSAxIGltcGxpY2l0bHkgcGVuYWxpemVzIFRDIG1vcmUgaGVhdmlseSwgcHVzaGluZyB0aGUgbWFyZ2luYWwgcG9zdGVyaW9yIHRvd2FyZCBhIGZhY3RvcmlhbCBkaXN0cmlidXRpb24uIEEgZmFjdG9yaWFsIG1hcmdpbmFsIHEoeikg4omIIOKIj+KxvCBxKHrisbwpIGlzIGEgbmVjZXNzYXJ5IChidXQgbm90IHN1ZmZpY2llbnQpIGNvbmRpdGlvbiBmb3IgZWFjaCB64rG8IHRvIGNhcHR1cmUgb25lIGluZGVwZW5kZW50IGdlbmVyYXRpdmUgZmFjdG9yLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Is6yLVZBRSBUcmFpbmluZyB3aXRoIENvbmZpZ3VyYWJsZSDOsiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuZnJvbSB0b3JjaC5vcHRpbSBpbXBvcnQgQWRhbVxuXG5jbGFzcyBCZXRhVkFFKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGxhdGVudF9kaW09MTAsIGJldGE9NC4wKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuYmV0YSA9IGJldGFcbiAgICAgICAgc2VsZi5sYXRlbnRfZGltID0gbGF0ZW50X2RpbVxuICAgICAgICBzZWxmLmVuY29kZXIgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKDEsIDMyLCA0LCAyLCAxKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uQ29udjJkKDMyLCA2NCwgNCwgMiwgMSksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkZsYXR0ZW4oKVxuICAgICAgICApXG4gICAgICAgIHNlbGYuZmNfbXUgICAgID0gbm4uTGluZWFyKDY0ICogNyAqIDcsIGxhdGVudF9kaW0pXG4gICAgICAgIHNlbGYuZmNfbG9ndmFyID0gbm4uTGluZWFyKDY0ICogNyAqIDcsIGxhdGVudF9kaW0pXG4gICAgICAgIHNlbGYuZGVjb2Rlcl9mYyA9IG5uLkxpbmVhcihsYXRlbnRfZGltLCA2NCAqIDcgKiA3KVxuICAgICAgICBzZWxmLmRlY29kZXIgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKDY0LCAzMiwgNCwgMiwgMSksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZCgzMiwgMSwgNCwgMiwgMSksIG5uLlNpZ21vaWQoKVxuICAgICAgICApXG5cbiAgICBkZWYgcmVwYXJhbWV0ZXJpemUoc2VsZiwgbXUsIGxvZ3Zhcik6XG4gICAgICAgIHJldHVybiBtdSArIHRvcmNoLmV4cCgwLjUgKiBsb2d2YXIpICogdG9yY2gucmFuZG5fbGlrZShtdSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBoID0gc2VsZi5lbmNvZGVyKHgpXG4gICAgICAgIG11LCBsb2d2YXIgPSBzZWxmLmZjX211KGgpLCBzZWxmLmZjX2xvZ3ZhcihoKVxuICAgICAgICB6ID0gc2VsZi5yZXBhcmFtZXRlcml6ZShtdSwgbG9ndmFyKVxuICAgICAgICBoMiA9IEYucmVsdShzZWxmLmRlY29kZXJfZmMoeikpLnZpZXcoLTEsIDY0LCA3LCA3KVxuICAgICAgICByZWNvbiA9IHNlbGYuZGVjb2RlcihoMilcbiAgICAgICAgcmV0dXJuIHJlY29uLCBtdSwgbG9ndmFyXG5cbiAgICBkZWYgbG9zcyhzZWxmLCB4KTpcbiAgICAgICAgcmVjb24sIG11LCBsb2d2YXIgPSBzZWxmKHgpXG4gICAgICAgIHJlY29uX2wgPSBGLmJpbmFyeV9jcm9zc19lbnRyb3B5KHJlY29uLCB4LCByZWR1Y3Rpb249XHUwMDI3c3VtXHUwMDI3KSAvIHguc2l6ZSgwKVxuICAgICAgICBrbCAgICAgID0gLTAuNSAqIHRvcmNoLnN1bSgxICsgbG9ndmFyIC0gbXUucG93KDIpIC0gbG9ndmFyLmV4cCgpLCBkaW09MSkubWVhbigpXG4gICAgICAgIHJldHVybiByZWNvbl9sICsgc2VsZi5iZXRhICoga2wsIHJlY29uX2wuaXRlbSgpLCBrbC5pdGVtKClcblxuZm9yIGJldGEgaW4gWzEsIDQsIDgsIDE2XTpcbiAgICBtID0gQmV0YVZBRShsYXRlbnRfZGltPTEwLCBiZXRhPWJldGEpXG4gICAgeCA9IHRvcmNoLnJhbmQoNCwgMSwgMjgsIDI4KVxuICAgIHRvdGFsLCByZWNvbiwga2wgPSBtLmxvc3MoeClcbiAgICBwcmludChmXHUwMDI3zrI9e2JldGE6MmR9OiB0b3RhbD17dG90YWw6LjJmfSAgcmVjb249e3JlY29uOi4yZn0gIEtMPXtrbDouMmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpc2VudGFuZ2xlbWVudCBWaXN1YWxpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc3RhbmRhcmQgd2F5IHRvIHZlcmlmeSBkaXNlbnRhbmdsZW1lbnQgdmlzdWFsbHkgaXMgbGF0ZW50IHRyYXZlcnNhbDogdGFrZSBhIHJlZmVyZW5jZSBpbWFnZSwgZW5jb2RlIGl0IHRvIGdldCB6LCB0aGVuIGZpeCBhbGwgbGF0ZW50IGRpbWVuc2lvbnMgZXhjZXB0IG9uZSBhbmQgdmFyeSB0aGF0IG9uZSBkaW1lbnNpb24gZnJvbSAtMyB0byArMyBpbiBzdGVwcy4gSWYgdGhlIG1vZGVsIGlzIGRpc2VudGFuZ2xlZCwgdmFyeWluZyB6X2ogc2hvdWxkIGNoYW5nZSBleGFjdGx5IG9uZSB2aXN1YWwgYXR0cmlidXRlIChlLmcuLCByb3RhdGlvbikgd2hpbGUgYWxsIG90aGVycyByZW1haW4gY29uc3RhbnQuIFdpdGggzrI9MSAodmFuaWxsYSBWQUUpLCB0cmF2ZXJzYWxzIG9mdGVuIGNoYW5nZSBtdWx0aXBsZSBhdHRyaWJ1dGVzIHNpbXVsdGFuZW91c2x5LiBXaXRoIM6yPTggb3IgzrI9MTYsIGluZGl2aWR1YWwgdHJhdmVyc2FscyB0eXBpY2FsbHkgaXNvbGF0ZSBzaW5nbGUgZmFjdG9ycywgYXQgdGhlIGNvc3Qgb2YgYmx1cnJpZXIgcmVjb25zdHJ1Y3Rpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWJcbm1hdHBsb3RsaWIudXNlKFx1MDAyN0FnZ1x1MDAyNylcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIGxhdGVudF90cmF2ZXJzYWwobW9kZWwsIHhfcmVmLCBkaW1faWR4LCBuX3N0ZXBzPTExLCB6X3JhbmdlPSgtMy4wLCAzLjApKTpcbiAgICBcIlwiXCJcbiAgICBGaXggYWxsIGxhdGVudCBkaW1zIGV4Y2VwdCBkaW1faWR4OyB0cmF2ZXJzZSBmcm9tIHpfcmFuZ2VbMF0gdG8gel9yYW5nZVsxXS5cbiAgICBSZXR1cm5zIGxpc3Qgb2YgZGVjb2RlZCBpbWFnZXMgc2hvd2luZyBob3cgdGhhdCBkaW0gY29udHJvbHMgZ2VuZXJhdGlvbi5cbiAgICBcIlwiXCJcbiAgICBtb2RlbC5ldmFsKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgbXUsIGxvZ3ZhciA9IG1vZGVsLmZjX211LCBtb2RlbC5mY19sb2d2YXJcbiAgICAgICAgaCA9IG1vZGVsLmVuY29kZXIoeF9yZWYudW5zcXVlZXplKDApKVxuICAgICAgICB6X2Jhc2UgPSBtb2RlbC5mY19tdShoKS5zcXVlZXplKDApICAjIHVzZSBtZWFuLCBubyBzYW1wbGluZ1xuICAgICAgICB6X3ZhbHMgPSB0b3JjaC5saW5zcGFjZSh6X3JhbmdlWzBdLCB6X3JhbmdlWzFdLCBuX3N0ZXBzKVxuICAgICAgICBpbWFnZXMgPSBbXVxuICAgICAgICBmb3IgdmFsIGluIHpfdmFsczpcbiAgICAgICAgICAgIHogPSB6X2Jhc2UuY2xvbmUoKVxuICAgICAgICAgICAgeltkaW1faWR4XSA9IHZhbFxuICAgICAgICAgICAgaDIgPSB0b3JjaC5yZWx1KG1vZGVsLmRlY29kZXJfZmMoei51bnNxdWVlemUoMCkpKS52aWV3KDEsIDY0LCA3LCA3KVxuICAgICAgICAgICAgaW1nID0gbW9kZWwuZGVjb2RlcihoMikuc3F1ZWV6ZSgpLmNwdSgpLm51bXB5KClcbiAgICAgICAgICAgIGltYWdlcy5hcHBlbmQoaW1nKVxuICAgIHJldHVybiBpbWFnZXNcblxuZGVmIHBsb3RfdHJhdmVyc2Fscyhtb2RlbCwgeF9yZWYsIG5fZGltcz01LCBzYXZlX3BhdGg9XHUwMDI3L3RtcC90cmF2ZXJzYWxzLnBuZ1x1MDAyNyk6XG4gICAgZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKG5fZGltcywgMTEsIGZpZ3NpemU9KDE1LCBuX2RpbXMgKiAxLjUpKVxuICAgIGZvciBkIGluIHJhbmdlKG5fZGltcyk6XG4gICAgICAgIGltZ3MgPSBsYXRlbnRfdHJhdmVyc2FsKG1vZGVsLCB4X3JlZiwgZGltX2lkeD1kKVxuICAgICAgICBmb3IgY29sLCBpbWcgaW4gZW51bWVyYXRlKGltZ3MpOlxuICAgICAgICAgICAgYXhlc1tkLCBjb2xdLmltc2hvdyhpbWcsIGNtYXA9XHUwMDI3Z3JheVx1MDAyNywgdm1pbj0wLCB2bWF4PTEpXG4gICAgICAgICAgICBheGVzW2QsIGNvbF0uYXhpcyhcdTAwMjdvZmZcdTAwMjcpXG4gICAgICAgIGF4ZXNbZCwgMF0uc2V0X3lsYWJlbChmXHUwMDI3el97ZH1cdTAwMjcsIHJvdGF0aW9uPTAsIGxhYmVscGFkPTIwLCBmb250c2l6ZT05KVxuICAgIHBsdC5zdXB0aXRsZShcdTAwMjfOsi1WQUUgTGF0ZW50IFRyYXZlcnNhbHNcdTAwMjcsIGZvbnRzaXplPTExKVxuICAgIHBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNhdmVmaWcoc2F2ZV9wYXRoLCBkcGk9MTAwKVxuICAgIHByaW50KGZcdTAwMjdUcmF2ZXJzYWwgZ3JpZCBzYXZlZCB0byB7c2F2ZV9wYXRofVx1MDAyNylcblxueF9yZWYgPSB0b3JjaC5yYW5kKDEsIDI4LCAyOClcbm1vZGVsID0gQmV0YVZBRShsYXRlbnRfZGltPTEwLCBiZXRhPTgpXG5wcmludChcdTAwMjdMYXRlbnQgdHJhdmVyc2FsOiB2YXJ5IG9uZSBkaW0sIGZpeCBvdGhlcnMgdG8gZGlhZ25vc2UgZGlzZW50YW5nbGVtZW50XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpc2VudGFuZ2xlbWVudCBNZXRyaWNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJRdWFsaXRhdGl2ZSB0cmF2ZXJzYWxzIGFyZSBpbnN1ZmZpY2llbnQgZm9yIHJpZ29yb3VzIGV2YWx1YXRpb24uIFRocmVlIHF1YW50aXRhdGl2ZSBtZXRyaWNzIGFyZSBjb21tb25seSB1c2VkLiBUaGUgQmV0YVZBRSBzY29yZSAoSGlnZ2lucyBldCBhbC4gMjAxNyk6IHNhbXBsZSBwYWlycyBvZiBpbWFnZXMgdGhhdCBkaWZmZXIgaW4gZXhhY3RseSBvbmUgZ3JvdW5kLXRydXRoIGZhY3RvcjsgZW5jb2RlIGJvdGg7IHRoZSBkaWZmZXJlbmNlIG9mIHRoZWlyIGxhdGVudCBjb2RlcyBzaG91bGQgcG9pbnQgYWxvbmcgdGhlIGF4aXMgZm9yIHRoYXQgZmFjdG9yOyBhIGxpbmVhciBjbGFzc2lmaWVyIHByZWRpY3RzIHdoaWNoIGZhY3RvciBjaGFuZ2VkIGZyb20gdGhlIGRpZmZlcmVuY2UgdmVjdG9yLiBGYWN0b3JWQUUgc2NvcmUgKEtpbSBcdTAwMjYgTW5paCAyMDE4KTogdXNlcyBhIG1ham9yaXR5IHZvdGUgY2xhc3NpZmllciBvbiB0aGUgbGF0ZW50IGRpbWVuc2lvbiB3aXRoIHNtYWxsZXN0IHZhcmlhbmNlIGFjcm9zcyBmaXhlZC1mYWN0b3IgYmF0Y2hlcy4gTUlHIChNdXR1YWwgSW5mb3JtYXRpb24gR2FwLCBDaGVuIGV0IGFsLiAyMDE4KTogZm9yIGVhY2ggZ3JvdW5kLXRydXRoIGZhY3RvciwgY29tcHV0ZSBub3JtYWxpemVkIG11dHVhbCBpbmZvcm1hdGlvbiB3aXRoIGVhY2ggbGF0ZW50IGRpbWVuc2lvbjsgdGhlIGdhcCBiZXR3ZWVuIHRoZSB0b3AtMSBhbmQgdG9wLTIgTUkgdmFsdWVzIG1lYXN1cmVzIGhvdyBleGNsdXNpdmVseSBvbmUgZGltZW5zaW9uIGVuY29kZXMgdGhhdCBmYWN0b3IuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBMb2dpc3RpY1JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcblxuZGVmIGJldGF2YWVfc2NvcmUobW9kZWwsIGdlbmVyYXRlX3BhaXJfZm4sIG5fcGFpcnM9MTAwMCwgbl9mYWN0b3JzPTYpOlxuICAgIFwiXCJcIlxuICAgIEJldGFWQUUgZGlzZW50YW5nbGVtZW50IHNjb3JlLlxuICAgIGdlbmVyYXRlX3BhaXJfZm4oZmFjdG9yX2lkeCkgLVx1MDAzZSAoaW1nMSwgaW1nMikgd2hlcmUgb25seSBmYWN0b3JfaWR4IGRpZmZlcnMuXG4gICAgU2NvcmUgPSBhY2N1cmFjeSBvZiBsaW5lYXIgY2xhc3NpZmllciBwcmVkaWN0aW5nIHdoaWNoIGZhY3RvciBjaGFuZ2VkLlxuICAgIFwiXCJcIlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIFhfdHJhaW4sIHlfdHJhaW4gPSBbXSwgW11cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9wYWlycyk6XG4gICAgICAgICAgICBmYWN0b3IgPSBucC5yYW5kb20ucmFuZGludChuX2ZhY3RvcnMpXG4gICAgICAgICAgICAjIGdlbmVyYXRlX3BhaXJfZm4gcmV0dXJucyAoaW1nMSwgaW1nMikgYXMgdGVuc29yc1xuICAgICAgICAgICAgaW1nMSwgaW1nMiA9IGdlbmVyYXRlX3BhaXJfZm4oZmFjdG9yKVxuICAgICAgICAgICAgbXUxLCBfID0gbW9kZWwuZmNfbXUobW9kZWwuZW5jb2RlcihpbWcxLnVuc3F1ZWV6ZSgwKSkpLCBOb25lXG4gICAgICAgICAgICBtdTIsIF8gPSBtb2RlbC5mY19tdShtb2RlbC5lbmNvZGVyKGltZzIudW5zcXVlZXplKDApKSksIE5vbmVcbiAgICAgICAgICAgIGgxID0gbW9kZWwuZW5jb2RlcihpbWcxLnVuc3F1ZWV6ZSgwKSlcbiAgICAgICAgICAgIGgyID0gbW9kZWwuZW5jb2RlcihpbWcyLnVuc3F1ZWV6ZSgwKSlcbiAgICAgICAgICAgIHoxLCB6MiA9IG1vZGVsLmZjX211KGgxKS5zcXVlZXplKCksIG1vZGVsLmZjX211KGgyKS5zcXVlZXplKClcbiAgICAgICAgICAgIGRpZmYgPSAoejEgLSB6MikuYWJzKCkuY3B1KCkubnVtcHkoKVxuICAgICAgICAgICAgWF90cmFpbi5hcHBlbmQoZGlmZilcbiAgICAgICAgICAgIHlfdHJhaW4uYXBwZW5kKGZhY3RvcilcbiAgICBYID0gbnAuYXJyYXkoWF90cmFpbilcbiAgICB5ID0gbnAuYXJyYXkoeV90cmFpbilcbiAgICBYX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4yLCByYW5kb21fc3RhdGU9MClcbiAgICBjbGYgPSBMb2dpc3RpY1JlZ3Jlc3Npb24obWF4X2l0ZXI9NTAwKS5maXQoWF90ciwgeV90cilcbiAgICBzY29yZSA9IGNsZi5zY29yZShYX3RlLCB5X3RlKVxuICAgIHByaW50KGZcdTAwMjdCZXRhVkFFIGRpc2VudGFuZ2xlbWVudCBzY29yZToge3Njb3JlOi4zZn0gKDEuMCA9IHBlcmZlY3QsIDEvbl9mYWN0b3JzID0gcmFuZG9tKVx1MDAyNylcbiAgICByZXR1cm4gc2NvcmVcblxuZGVmIG1pZ19zY29yZSh6X3NhbXBsZXMsIGZhY3Rvcl9zYW1wbGVzLCBiaW5zPTIwKTpcbiAgICBcIlwiXCJNdXR1YWwgSW5mb3JtYXRpb24gR2FwOiBnYXAgYmV0d2VlbiB0b3AtMSBhbmQgdG9wLTIgTUkgcGVyIGdyb3VuZC10cnV0aCBmYWN0b3IuXCJcIlwiXG4gICAgbl9mYWN0b3JzID0gZmFjdG9yX3NhbXBsZXMuc2hhcGVbMV1cbiAgICBuX2xhdGVudHMgID0gel9zYW1wbGVzLnNoYXBlWzFdXG4gICAgbWlfbWF0cml4ID0gbnAuemVyb3MoKG5fZmFjdG9ycywgbl9sYXRlbnRzKSlcbiAgICBmb3IgZiBpbiByYW5nZShuX2ZhY3RvcnMpOlxuICAgICAgICBmb3IgZCBpbiByYW5nZShuX2xhdGVudHMpOlxuICAgICAgICAgICAgIyBEaXNjcmV0aXplIGNvbnRpbnVvdXMgdmFsdWVzIGZvciBNSSBlc3RpbWF0aW9uXG4gICAgICAgICAgICBmX2Rpc2MgPSBucC5kaWdpdGl6ZShmYWN0b3Jfc2FtcGxlc1s6LCBmXSwgYmlucz1ucC5saW5zcGFjZShmYWN0b3Jfc2FtcGxlc1s6LCBmXS5taW4oKSwgZmFjdG9yX3NhbXBsZXNbOiwgZl0ubWF4KCksIGJpbnMpKVxuICAgICAgICAgICAgel9kaXNjID0gbnAuZGlnaXRpemUoel9zYW1wbGVzWzosIGRdLCBiaW5zPW5wLmxpbnNwYWNlKHpfc2FtcGxlc1s6LCBkXS5taW4oKSwgel9zYW1wbGVzWzosIGRdLm1heCgpLCBiaW5zKSlcbiAgICAgICAgICAgIG1pX21hdHJpeFtmLCBkXSA9IG5wLmNvcnJjb2VmKGZfZGlzYywgel9kaXNjKVswLCAxXSAqKiAyICAjIGFwcHJveCBNSSB2aWEgUl4yXG4gICAgbWlnID0gbnAubWVhbihucC5zb3J0KG1pX21hdHJpeCwgYXhpcz0xKVs6LCAtMV0gLSBucC5zb3J0KG1pX21hdHJpeCwgYXhpcz0xKVs6LCAtMl0pXG4gICAgcHJpbnQoZlx1MDAyN01JRyBzY29yZToge21pZzouM2Z9IChoaWdoZXIgPSBiZXR0ZXIsIG1heD0xLjApXHUwMDI3KVxuICAgIHJldHVybiBtaWdcblxucHJpbnQoXHUwMDI3RGlzZW50YW5nbGVtZW50IG1ldHJpYyBmdW5jdGlvbnMgcmVhZHlcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmFjdG9yVkFFIOKAlCBUb3RhbCBDb3JyZWxhdGlvbiBQZW5hbHR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGYWN0b3JWQUUgKEtpbSBcdTAwMjYgTW5paCAyMDE4KSBkZWNvbXBvc2VzIHRoZSDOsi1WQUUgb2JqZWN0aXZlIHRvIGlkZW50aWZ5IHRoZSB0b3RhbCBjb3JyZWxhdGlvbiBUQyh6KSA9IEtMKHEoeikgfHwg4oiP4rG8IHEoeuKxvCkpIGFzIHRoZSBrZXkgdGVybSBkcml2aW5nIGRpc2VudGFuZ2xlbWVudCwgYW5kIHBlbmFsaXplcyBUQyBkaXJlY3RseSByYXRoZXIgdGhhbiB0aGUgZnVsbCBLTC4gVEMgaXMgZXN0aW1hdGVkIHVzaW5nIGEgZGlzY3JpbWluYXRvciBEIHRyYWluZWQgdG8gZGlzdGluZ3Vpc2ggc2FtcGxlcyBmcm9tIHRoZSBhZ2dyZWdhdGVkIHBvc3RlcmlvciBxKHopID0g4oirIHEoenx4KXAoeClkeCBmcm9tIHNhbXBsZXMgZnJvbSB0aGUgZmFjdG9yaWFsIOKIj+KxvCBxKHrisbwpLiBUaGUgVEMgdGVybSBpcyBlc3RpbWF0ZWQgYXMgRV97cSh6KX1bbG9nIEQoeikgLSBsb2coMS1EKHopKV0uIEJ5IHBlbmFsaXppbmcgVEMgZGlyZWN0bHkgd2hpbGUga2VlcGluZyB0aGUgcmVjb25zdHJ1Y3Rpb24gYW5kIE1JIHRlcm1zIGZyb20gdGhlIHN0YW5kYXJkIEVMQk8sIEZhY3RvclZBRSBhY2hpZXZlcyBiZXR0ZXIgZGlzZW50YW5nbGVtZW50IGF0IHRoZSBzYW1lIHJlY29uc3RydWN0aW9uIHF1YWxpdHkgdGhhbiDOsi1WQUUgd2l0aCBlcXVpdmFsZW50IM6yLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBUQ0Rpc2NyaW1pbmF0b3Iobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJEaXNjcmltaW5hdG9yIGZvciBGYWN0b3JWQUU6IHNlcGFyYXRlcyBxKHopIGZyb20gcHJvZF9qIHEoel9qKS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbGF0ZW50X2RpbT0xMCwgaGlkZGVuPTI1Nik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIobGF0ZW50X2RpbSwgaGlkZGVuKSwgbm4uTGVha3lSZUxVKDAuMiksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCBoaWRkZW4pLCBubi5MZWFreVJlTFUoMC4yKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW4sIGhpZGRlbiksIG5uLkxlYWt5UmVMVSgwLjIpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgMikgICMgbG9naXRzIGZvciBbcmVhbCwgcGVybXV0ZWRdXG4gICAgICAgIClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHopOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeilcblxuZGVmIHBlcm11dGVfZGltcyh6KTpcbiAgICBcIlwiXCJQZXJtdXRlIGVhY2ggbGF0ZW50IGRpbSBpbmRlcGVuZGVudGx5IHRvIHNhbXBsZSBmcm9tIHByb2RfaiBxKHpfaikuXCJcIlwiXG4gICAgQiwgRCA9IHouc2hhcGVcbiAgICB6X3Blcm0gPSB0b3JjaC56ZXJvc19saWtlKHopXG4gICAgZm9yIGQgaW4gcmFuZ2UoRCk6XG4gICAgICAgIGlkeCA9IHRvcmNoLnJhbmRwZXJtKEIpXG4gICAgICAgIHpfcGVybVs6LCBkXSA9IHpbaWR4LCBkXVxuICAgIHJldHVybiB6X3Blcm1cblxuZGVmIGZhY3RvcnZhZV92YWVfbG9zcyhyZWNvbiwgeCwgbXUsIGxvZ3ZhciwgRF9uZXQsIGdhbW1hPTEwLjApOlxuICAgIFwiXCJcIlZBRSBsb3NzIGZvciBGYWN0b3JWQUU6IHJlY29uICsgTUkgKyBkaW1lbnNpb24td2lzZSBLTCArIGdhbW1hKlRDIGVzdGltYXRlLlwiXCJcIlxuICAgIHJlY29uX2xvc3MgPSBGLmJpbmFyeV9jcm9zc19lbnRyb3B5KHJlY29uLCB4LnZpZXcoeC5zaXplKDApLCAtMSksIHJlZHVjdGlvbj1cdTAwMjdzdW1cdTAwMjcpIC8geC5zaXplKDApXG4gICAga2wgPSAtMC41ICogdG9yY2guc3VtKDEgKyBsb2d2YXIgLSBtdS5wb3coMikgLSBsb2d2YXIuZXhwKCksIGRpbT0xKS5tZWFuKClcbiAgICAjIEVzdGltYXRlIFRDIHVzaW5nIGRpc2NyaW1pbmF0b3JcbiAgICBzdGQgPSB0b3JjaC5leHAoMC41ICogbG9ndmFyKVxuICAgIHogPSBtdSArIHN0ZCAqIHRvcmNoLnJhbmRuX2xpa2Uoc3RkKVxuICAgIGRfbG9naXRzID0gRF9uZXQoeikgICMgKEIsIDIpXG4gICAgdGNfZXN0aW1hdGUgPSAoZF9sb2dpdHNbOiwgMF0gLSBkX2xvZ2l0c1s6LCAxXSkubWVhbigpXG4gICAgcmV0dXJuIHJlY29uX2xvc3MgKyBrbCArIGdhbW1hICogdGNfZXN0aW1hdGVcblxuZGVmIGZhY3RvcnZhZV9kaXNjX2xvc3Moel9yZWFsLCBEX25ldCk6XG4gICAgXCJcIlwiRGlzY3JpbWluYXRvciBsb3NzOiBjbGFzc2lmeSBxKHopIGFzIHJlYWwsIHByb2RfaiBxKHpfaikgYXMgZmFrZS5cIlwiXCJcbiAgICB6X3Blcm0gPSBwZXJtdXRlX2RpbXMoel9yZWFsLmRldGFjaCgpKVxuICAgIHJlYWxfbG9naXRzID0gRF9uZXQoel9yZWFsLmRldGFjaCgpKVxuICAgIGZha2VfbG9naXRzID0gRF9uZXQoel9wZXJtKVxuICAgIHJlYWxfbG9zcyA9IEYuY3Jvc3NfZW50cm9weShyZWFsX2xvZ2l0cywgdG9yY2guemVyb3Moel9yZWFsLnNpemUoMCksIGR0eXBlPXRvcmNoLmxvbmcsIGRldmljZT16X3JlYWwuZGV2aWNlKSlcbiAgICBmYWtlX2xvc3MgPSBGLmNyb3NzX2VudHJvcHkoZmFrZV9sb2dpdHMsIHRvcmNoLm9uZXMoel9wZXJtLnNpemUoMCksIGR0eXBlPXRvcmNoLmxvbmcsIGRldmljZT16X3Blcm0uZGV2aWNlKSlcbiAgICByZXR1cm4gKHJlYWxfbG9zcyArIGZha2VfbG9zcykgLyAyXG5cbkQgPSBUQ0Rpc2NyaW1pbmF0b3IobGF0ZW50X2RpbT0xMClcbnpfc2FtcGxlID0gdG9yY2gucmFuZG4oMzIsIDEwKVxuel9wZXJtICAgPSBwZXJtdXRlX2RpbXMoel9zYW1wbGUpXG5wcmludChmXHUwMDI3RGlzY3JpbWluYXRvciBvbiBxKHopOiAgICAgICAgICB7RCh6X3NhbXBsZSkuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1Blcm11dGVkIGRpbXMgKHByb2RfaiBxKHpfaikpOiAge0Qoel9wZXJtKS5zaGFwZX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoizrItVENWQUUg4oCUIERlY29tcG9zaW5nIHRoZSBLTCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoizrItVENWQUUgKENoZW4gZXQgYWwuIDIwMTgpIHByb3ZpZGVzIHRoZSBtb3N0IHByaW5jaXBsZWQgZGVjb21wb3NpdGlvbiBvZiB0aGUgVkFFIG9iamVjdGl2ZS4gVGhlIGZ1bGwgS0wgdGVybSBLTChxX8+GKHp8eCkgfHwgcCh6KSkgY2FuIGJlIHdyaXR0ZW4gYXM6IEkoeDt6KSArIFRDKHopICsgzqPisbwgS0wocSh64rG8KSB8fCBwKHrisbwpKSwgd2hlcmUgSSh4O3opIGlzIHRoZSBpbmRleC1jb2RlIG11dHVhbCBpbmZvcm1hdGlvbiAoZW5jb2RpbmcgaW5mb3JtYXRpb24gY29udGVudCksIFRDKHopID0gS0wocSh6KSB8fCDiiI/isbwgcSh64rG8KSkgaXMgdGhlIHRvdGFsIGNvcnJlbGF0aW9uIChkZXBlbmRlbmN5IGJldHdlZW4gbGF0ZW50IGRpbWVuc2lvbnMpLCBhbmQgdGhlIGxhc3QgdGVybSBpcyBkaW1lbnNpb24td2lzZSBLTCAoZGlzdGFuY2Ugb2YgZWFjaCBtYXJnaW5hbCBmcm9tIHRoZSBwcmlvcikuIM6yLVRDVkFFIHBlbmFsaXplcyBvbmx5IFRDIHdpdGggYSBmYWN0b3IgzrEgKHR5cGljYWxseSDOsT3Osi0xKSwgbGVhdmluZyB0aGUgTUkgYW5kIGRpbWVuc2lvbi13aXNlIEtMIHRlcm1zIHdlaWdodGVkIGF0IDEuIFRoaXMgc3VyZ2ljYWwgcGVuYWx0eSBhY2hpZXZlcyB0aGUgc2FtZSBkaXNlbnRhbmdsZW1lbnQgZWZmZWN0IGFzIM6yLVZBRSB3aGlsZSBwcmVzZXJ2aW5nIG1vcmUgcmVjb25zdHJ1Y3Rpb24gcXVhbGl0eSwgYmVjYXVzZSBNSSBhbmQgZGltZW5zaW9uLXdpc2UgS0wgYXJlIG5vdCBpbmZsYXRlZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZ1bGwgS0wgPSBJKHg7eikgICsgIFRDKHopICArICDOo+KxvCBLTChxKHrisbwpfHxwKHrisbwpKSDigJQgdGhyZWUgZGlzdGluY3QgdGVybXMgd2l0aCBkaWZmZXJlbnQgcm9sZXMuIiwiSSh4O3opIHNob3VsZCBOT1QgYmUgcGVuYWxpemVkIGhlYXZpbHkg4oCUIGl0IHJlcHJlc2VudHMgdXNlZnVsIGluZm9ybWF0aW9uIGVuY29kZWQgaW4gei4iLCJUQyh6KSBpcyB0aGUgZGlzZW50YW5nbGVtZW50IHRlcm0g4oCUIHBlbmFsaXppbmcgaXQgZW5jb3VyYWdlcyBmYWN0b3JpYWwgbWFyZ2luYWwgcSh6KSDiiYgg4oiP4rG8IHEoeuKxvCkuIiwizrItVENWQUUgdXNlcyBtaW5pYmF0Y2gtc3RyYXRpZmllZCBzYW1wbGluZyB0byBlc3RpbWF0ZSBUQyB3aXRob3V0IGFuIGFkdmVyc2FyaWFsIGRpc2NyaW1pbmF0b3IuIiwiRmFjdG9yVkFFIGVzdGltYXRlcyBUQyBhZHZlcnNhcmlhbGx5OyDOsi1UQ1ZBRSBlc3RpbWF0ZXMgaXQgdmlhIGltcG9ydGFuY2Ugd2VpZ2h0aW5nIOKAlCBib3RoIHRhcmdldCB0aGUgc2FtZSB0ZXJtLiJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQ2hvb3NpbmcgzrIgaW4gUHJhY3RpY2UiLCJjb250ZW50IjoiU3RhcnQgd2l0aCDOsj00IGFuZCBpbmNyZWFzZSBpZiB0cmF2ZXJzYWxzIHNob3cgZW50YW5nbGVtZW50LiDOsj044oCTMTYgaXMgdGhlIHR5cGljYWwgc3dlZXQgc3BvdCBmb3IgZFNwcml0ZXMgYW5kIDNEIFNoYXBlcyBiZW5jaG1hcmtzLiBJZiByZWNvbnN0cnVjdGlvbnMgYmVjb21lIHRvbyBibHVycnkgYXQgaGlnaCDOsiwgdHJ5IEZhY3RvclZBRSAozrM9MTDigJM0MCkgb3IgzrItVENWQUUgaW5zdGVhZCDigJQgdGhleSBhY2hpZXZlIGVxdWl2YWxlbnQgZGlzZW50YW5nbGVtZW50IHdpdGggYmV0dGVyIHJlY29uc3RydWN0aW9uIGJ5IHBlbmFsaXppbmcgdG90YWwgY29ycmVsYXRpb24gbW9yZSBwcmVjaXNlbHkgcmF0aGVyIHRoYW4gdGhlIGZ1bGwgS0wuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiTG9zcyIsIs6yIC8gzrMiLCJEaXNlbnRhbmdsZW1lbnQgU2NvcmUiLCJSZWNvbnN0cnVjdGlvbiBRdWFsaXR5IiwiSW50ZXJwcmV0YWJpbGl0eSJdLCJyb3dzIjpbWyJWQUUgKM6yPTEpIiwiUmVjb24gKyAxwrdLTCIsIs6yPTEiLCJMb3cgKH4wLjUgQmV0YVZBRSkiLCJIaWdoIOKAlCBzaGFycCByZWNvbnN0cnVjdGlvbnMiLCJFbnRhbmdsZWQgZmFjdG9ycywgaGFyZCB0byBpbnRlcnByZXQiXSxbIs6yLVZBRSAozrI9NCkiLCJSZWNvbiArIDTCt0tMIiwizrI9NCIsIk1lZGl1bSAofjAuNykiLCJNb2RlcmF0ZSDigJQgc2xpZ2h0bHkgYmx1cnJ5IiwiU2V2ZXJhbCBmYWN0b3JzIGlzb2xhdGVkIl0sWyLOsi1WQUUgKM6yPTE2KSIsIlJlY29uICsgMTbCt0tMIiwizrI9MTYiLCJIaWdoICh+MC44NSkiLCJMb3cg4oCUIGJsdXJyeSByZWNvbnN0cnVjdGlvbnMiLCJNb3N0IGZhY3RvcnMgaXNvbGF0ZWQsIHNvbWUgbG9zdCJdLFsiRmFjdG9yVkFFIiwiUmVjb24gKyBNSSArIGRpbS1LTCArIM6zwrdUQyIsIs6zPTEw4oCTNDAiLCJIaWdoICh+MC44NeKAkzAuOSkiLCJCZXR0ZXIgdGhhbiDOsi1WQUUgYXQgc2FtZSBzY29yZSIsIkluZGVwZW5kZW50IFRDIHBlbmFsdHksIGNsZWFuZXIiXSxbIs6yLVRDVkFFIiwiUmVjb24gKyBNSSArIM6ywrdUQyArIGRpbS1LTCIsIs6yPTTigJM4IG9uIFRDIG9ubHkiLCJIaWdoICh+MC44NeKAkzAuOSkiLCJCZXR0ZXIgdGhhbiDOsi1WQUUiLCJFeHBsaWNpdCBUQyBkZWNvbXBvc2l0aW9uLCBwcmluY2lwbGVkIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIs6yPTEgaXMgdGhlIHN0YW5kYXJkIFZBRSDigJQgdGhlIEVMQk8gbG93ZXIgYm91bmQgb24gbG9nIHAoeCkgd2l0aCBubyBleHRyYSBkaXNlbnRhbmdsZW1lbnQgcHJlc3N1cmUuIiwiVG90YWwgY29ycmVsYXRpb24gVEMoeikgPSBLTChxKHopIHx8IOKIj+KxvCBxKHrisbwpKSBpcyB6ZXJvIGlmIGFuZCBvbmx5IGlmIGFsbCBsYXRlbnQgZGltZW5zaW9ucyBhcmUgbXV0dWFsbHkgaW5kZXBlbmRlbnQuIiwiVGhlIEJldGFWQUUgZGlzZW50YW5nbGVtZW50IHNjb3JlIHNhdHVyYXRlcyBhdCB+MC45IG9uIGRTcHJpdGVzOyBwZXJmZWN0IHNjb3JlcyBhcmUgdW5hY2hpZXZhYmxlIGJlY2F1c2Ugc3RvY2hhc3RpYyBlbmNvZGluZyBhZGRzIG5vaXNlIHRvIGRpZmZlcmVuY2UgdmVjdG9ycy4iLCJGYWN0b3JWQUVcdTAwMjdzIHBlcm11dGUtZGltcyB0cmljayBzaHVmZmxlcyBlYWNoIGxhdGVudCBkaW1lbnNpb24gaW5kZXBlbmRlbnRseSBhY3Jvc3MgdGhlIGJhdGNoIHRvIGFwcHJveGltYXRlIHNhbXBsZXMgZnJvbSB0aGUgZmFjdG9yaWFsIG1hcmdpbmFsIOKIj+KxvCBxKHrisbwpLiIsIs6yLVRDVkFFIChDaGVuIGV0IGFsLiAyMDE4KSBkZWNvbXBvc2VzIHRoZSBLTCBpbnRvIHRocmVlIHRlcm1zIOKAlCBpbmRleC1jb2RlIE1JIChJKHg7eikpLCBUQyh6KSwgYW5kIGRpbWVuc2lvbi13aXNlIEtMIOKAlCBhbmQgcGVuYWxpemVzIG9ubHkgVEMsIGdpdmluZyB0aGUgbW9zdCBwcmluY2lwbGVkIG9iamVjdGl2ZS4iLCJEaXNlbnRhbmdsZW1lbnQgaXMgZGF0YXNldC1kZXBlbmRlbnQ6IG1vZGVscyB3aXRoIGhpZ2ggQmV0YVZBRSBzY29yZXMgb24gZFNwcml0ZXMgbWF5IG5vdCBkaXNlbnRhbmdsZSBvbiBuYXR1cmFsIGltYWdlcyB3aGVyZSBmYWN0b3JzIGFyZSBjb3JyZWxhdGVkLiJdfSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiLOsi1WQUUgZXN0YWJsaXNoZXMgdGhhdCBhIHNpbmdsZSBzY2FsYXIgaHlwZXJwYXJhbWV0ZXIgY2FuIHNoaWZ0IHRoZSBWQUUgZnJvbSBhIHB1cmUgZ2VuZXJhdGl2ZSBtb2RlbCB0b3dhcmQgYSBkaXNlbnRhbmdsZWQgcmVwcmVzZW50YXRpb24gbGVhcm5lci4gRmFjdG9yVkFFIGFuZCDOsi1UQ1ZBRSByZWZpbmUgdGhpcyBpbnNpZ2h0IGJ5IGlzb2xhdGluZyB0b3RhbCBjb3JyZWxhdGlvbiBhcyB0aGUgb3BlcmF0aXZlIHRlcm0sIHlpZWxkaW5nIGJldHRlciBkaXNlbnRhbmdsZW1lbnQtcXVhbGl0eSB0cmFkZW9mZnMuIFRoZXNlIG1vZGVscyBmaW5kIHByYWN0aWNhbCB1c2UgaW4gY29udHJvbGxhYmxlIGdlbmVyYXRpb24sIHNjaWVudGlmaWMgZmFjdG9yIGRpc2NvdmVyeSwgYW5kIGRhdGEgYXVnbWVudGF0aW9uIOKAlCBhbnl3aGVyZSB0aGF0IGludGVycHJldGFibGUsIGluZGVwZW5kZW50IGxhdGVudCBmYWN0b3JzIGFyZSBtb3JlIHZhbHVhYmxlIHRoYW4gcGl4ZWwtcGVyZmVjdCByZWNvbnN0cnVjdGlvbi4ifV0="
---
# β-VAE — Disentangled Representation Learning

β-VAE (Higgins et al. 2017) extends the standard VAE by multiplying the KL term by a scalar β > 1: L = E[log p(x|z)] - β·KL(q_φ(z|x) || p(z)). When β=1 the objective is the standard ELBO. Increasing β imposes a stronger information bottleneck on the latent code, forcing the encoder to use each latent dimension sparingly and independently. The result is disentanglement: each latent dimension tends to encode one interpretable generative factor (e.g., rotation angle, object scale, x-position) independently of the others. The tradeoff is that high β degrades reconstruction quality — the stronger bottleneck leaves less capacity for precise reconstruction.

## Why β > 1 Promotes Disentanglement

The KL term KL(q_φ(z|x) || p(z)) = KL(q_φ(z|x) || N(0,I)) can be decomposed as: index-code mutual information I(x;z) + total correlation TC(z) + dimension-wise KL. Total correlation TC(z) = KL(q(z) || ∏ⱼ q(zⱼ)) measures statistical dependence among latent dimensions — it is zero only when all dimensions are mutually independent. Penalizing KL with β > 1 implicitly penalizes TC more heavily, pushing the marginal posterior toward a factorial distribution. A factorial marginal q(z) ≈ ∏ⱼ q(zⱼ) is a necessary (but not sufficient) condition for each zⱼ to capture one independent generative factor.

## β-VAE Training with Configurable β

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import Adam

class BetaVAE(nn.Module):
    def __init__(self, latent_dim=10, beta=4.0):
        super().__init__()
        self.beta = beta
        self.latent_dim = latent_dim
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(32, 64, 4, 2, 1), nn.ReLU(),
            nn.Flatten()
        )
        self.fc_mu     = nn.Linear(64 * 7 * 7, latent_dim)
        self.fc_logvar = nn.Linear(64 * 7 * 7, latent_dim)
        self.decoder_fc = nn.Linear(latent_dim, 64 * 7 * 7)
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(64, 32, 4, 2, 1), nn.ReLU(),
            nn.ConvTranspose2d(32, 1, 4, 2, 1), nn.Sigmoid()
        )

    def reparameterize(self, mu, logvar):
        return mu + torch.exp(0.5 * logvar) * torch.randn_like(mu)

    def forward(self, x):
        h = self.encoder(x)
        mu, logvar = self.fc_mu(h), self.fc_logvar(h)
        z = self.reparameterize(mu, logvar)
        h2 = F.relu(self.decoder_fc(z)).view(-1, 64, 7, 7)
        recon = self.decoder(h2)
        return recon, mu, logvar

    def loss(self, x):
        recon, mu, logvar = self(x)
        recon_l = F.binary_cross_entropy(recon, x, reduction='sum') / x.size(0)
        kl      = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=1).mean()
        return recon_l + self.beta * kl, recon_l.item(), kl.item()

for beta in [1, 4, 8, 16]:
    m = BetaVAE(latent_dim=10, beta=beta)
    x = torch.rand(4, 1, 28, 28)
    total, recon, kl = m.loss(x)
    print(f'β={beta:2d}: total={total:.2f}  recon={recon:.2f}  KL={kl:.2f}')
```

## Disentanglement Visualization

The standard way to verify disentanglement visually is latent traversal: take a reference image, encode it to get z, then fix all latent dimensions except one and vary that one dimension from -3 to +3 in steps. If the model is disentangled, varying z_j should change exactly one visual attribute (e.g., rotation) while all others remain constant. With β=1 (vanilla VAE), traversals often change multiple attributes simultaneously. With β=8 or β=16, individual traversals typically isolate single factors, at the cost of blurrier reconstructions.

```python
import torch
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def latent_traversal(model, x_ref, dim_idx, n_steps=11, z_range=(-3.0, 3.0)):
    """
    Fix all latent dims except dim_idx; traverse from z_range[0] to z_range[1].
    Returns list of decoded images showing how that dim controls generation.
    """
    model.eval()
    with torch.no_grad():
        mu, logvar = model.fc_mu, model.fc_logvar
        h = model.encoder(x_ref.unsqueeze(0))
        z_base = model.fc_mu(h).squeeze(0)  # use mean, no sampling
        z_vals = torch.linspace(z_range[0], z_range[1], n_steps)
        images = []
        for val in z_vals:
            z = z_base.clone()
            z[dim_idx] = val
            h2 = torch.relu(model.decoder_fc(z.unsqueeze(0))).view(1, 64, 7, 7)
            img = model.decoder(h2).squeeze().cpu().numpy()
            images.append(img)
    return images

def plot_traversals(model, x_ref, n_dims=5, save_path='/tmp/traversals.png'):
    fig, axes = plt.subplots(n_dims, 11, figsize=(15, n_dims * 1.5))
    for d in range(n_dims):
        imgs = latent_traversal(model, x_ref, dim_idx=d)
        for col, img in enumerate(imgs):
            axes[d, col].imshow(img, cmap='gray', vmin=0, vmax=1)
            axes[d, col].axis('off')
        axes[d, 0].set_ylabel(f'z_{d}', rotation=0, labelpad=20, fontsize=9)
    plt.suptitle('β-VAE Latent Traversals', fontsize=11)
    plt.tight_layout(); plt.savefig(save_path, dpi=100)
    print(f'Traversal grid saved to {save_path}')

x_ref = torch.rand(1, 28, 28)
model = BetaVAE(latent_dim=10, beta=8)
print('Latent traversal: vary one dim, fix others to diagnose disentanglement')
```

## Disentanglement Metrics

Qualitative traversals are insufficient for rigorous evaluation. Three quantitative metrics are commonly used. The BetaVAE score (Higgins et al. 2017): sample pairs of images that differ in exactly one ground-truth factor; encode both; the difference of their latent codes should point along the axis for that factor; a linear classifier predicts which factor changed from the difference vector. FactorVAE score (Kim & Mnih 2018): uses a majority vote classifier on the latent dimension with smallest variance across fixed-factor batches. MIG (Mutual Information Gap, Chen et al. 2018): for each ground-truth factor, compute normalized mutual information with each latent dimension; the gap between the top-1 and top-2 MI values measures how exclusively one dimension encodes that factor.

```python
import torch
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def betavae_score(model, generate_pair_fn, n_pairs=1000, n_factors=6):
    """
    BetaVAE disentanglement score.
    generate_pair_fn(factor_idx) -> (img1, img2) where only factor_idx differs.
    Score = accuracy of linear classifier predicting which factor changed.
    """
    model.eval()
    X_train, y_train = [], []
    with torch.no_grad():
        for _ in range(n_pairs):
            factor = np.random.randint(n_factors)
            # generate_pair_fn returns (img1, img2) as tensors
            img1, img2 = generate_pair_fn(factor)
            mu1, _ = model.fc_mu(model.encoder(img1.unsqueeze(0))), None
            mu2, _ = model.fc_mu(model.encoder(img2.unsqueeze(0))), None
            h1 = model.encoder(img1.unsqueeze(0))
            h2 = model.encoder(img2.unsqueeze(0))
            z1, z2 = model.fc_mu(h1).squeeze(), model.fc_mu(h2).squeeze()
            diff = (z1 - z2).abs().cpu().numpy()
            X_train.append(diff)
            y_train.append(factor)
    X = np.array(X_train)
    y = np.array(y_train)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)
    clf = LogisticRegression(max_iter=500).fit(X_tr, y_tr)
    score = clf.score(X_te, y_te)
    print(f'BetaVAE disentanglement score: {score:.3f} (1.0 = perfect, 1/n_factors = random)')
    return score

def mig_score(z_samples, factor_samples, bins=20):
    """Mutual Information Gap: gap between top-1 and top-2 MI per ground-truth factor."""
    n_factors = factor_samples.shape[1]
    n_latents  = z_samples.shape[1]
    mi_matrix = np.zeros((n_factors, n_latents))
    for f in range(n_factors):
        for d in range(n_latents):
            # Discretize continuous values for MI estimation
            f_disc = np.digitize(factor_samples[:, f], bins=np.linspace(factor_samples[:, f].min(), factor_samples[:, f].max(), bins))
            z_disc = np.digitize(z_samples[:, d], bins=np.linspace(z_samples[:, d].min(), z_samples[:, d].max(), bins))
            mi_matrix[f, d] = np.corrcoef(f_disc, z_disc)[0, 1] ** 2  # approx MI via R^2
    mig = np.mean(np.sort(mi_matrix, axis=1)[:, -1] - np.sort(mi_matrix, axis=1)[:, -2])
    print(f'MIG score: {mig:.3f} (higher = better, max=1.0)')
    return mig

print('Disentanglement metric functions ready')
```

## FactorVAE — Total Correlation Penalty

FactorVAE (Kim & Mnih 2018) decomposes the β-VAE objective to identify the total correlation TC(z) = KL(q(z) || ∏ⱼ q(zⱼ)) as the key term driving disentanglement, and penalizes TC directly rather than the full KL. TC is estimated using a discriminator D trained to distinguish samples from the aggregated posterior q(z) = ∫ q(z|x)p(x)dx from samples from the factorial ∏ⱼ q(zⱼ). The TC term is estimated as E_{q(z)}[log D(z) - log(1-D(z))]. By penalizing TC directly while keeping the reconstruction and MI terms from the standard ELBO, FactorVAE achieves better disentanglement at the same reconstruction quality than β-VAE with equivalent β.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TCDiscriminator(nn.Module):
    """Discriminator for FactorVAE: separates q(z) from prod_j q(z_j)."""
    def __init__(self, latent_dim=10, hidden=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, hidden), nn.LeakyReLU(0.2),
            nn.Linear(hidden, hidden), nn.LeakyReLU(0.2),
            nn.Linear(hidden, hidden), nn.LeakyReLU(0.2),
            nn.Linear(hidden, 2)  # logits for [real, permuted]
        )

    def forward(self, z):
        return self.net(z)

def permute_dims(z):
    """Permute each latent dim independently to sample from prod_j q(z_j)."""
    B, D = z.shape
    z_perm = torch.zeros_like(z)
    for d in range(D):
        idx = torch.randperm(B)
        z_perm[:, d] = z[idx, d]
    return z_perm

def factorvae_vae_loss(recon, x, mu, logvar, D_net, gamma=10.0):
    """VAE loss for FactorVAE: recon + MI + dimension-wise KL + gamma*TC estimate."""
    recon_loss = F.binary_cross_entropy(recon, x.view(x.size(0), -1), reduction='sum') / x.size(0)
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=1).mean()
    # Estimate TC using discriminator
    std = torch.exp(0.5 * logvar)
    z = mu + std * torch.randn_like(std)
    d_logits = D_net(z)  # (B, 2)
    tc_estimate = (d_logits[:, 0] - d_logits[:, 1]).mean()
    return recon_loss + kl + gamma * tc_estimate

def factorvae_disc_loss(z_real, D_net):
    """Discriminator loss: classify q(z) as real, prod_j q(z_j) as fake."""
    z_perm = permute_dims(z_real.detach())
    real_logits = D_net(z_real.detach())
    fake_logits = D_net(z_perm)
    real_loss = F.cross_entropy(real_logits, torch.zeros(z_real.size(0), dtype=torch.long, device=z_real.device))
    fake_loss = F.cross_entropy(fake_logits, torch.ones(z_perm.size(0), dtype=torch.long, device=z_perm.device))
    return (real_loss + fake_loss) / 2

D = TCDiscriminator(latent_dim=10)
z_sample = torch.randn(32, 10)
z_perm   = permute_dims(z_sample)
print(f'Discriminator on q(z):          {D(z_sample).shape}')
print(f'Permuted dims (prod_j q(z_j)):  {D(z_perm).shape}')
```

## β-TCVAE — Decomposing the KL

β-TCVAE (Chen et al. 2018) provides the most principled decomposition of the VAE objective. The full KL term KL(q_φ(z|x) || p(z)) can be written as: I(x;z) + TC(z) + Σⱼ KL(q(zⱼ) || p(zⱼ)), where I(x;z) is the index-code mutual information (encoding information content), TC(z) = KL(q(z) || ∏ⱼ q(zⱼ)) is the total correlation (dependency between latent dimensions), and the last term is dimension-wise KL (distance of each marginal from the prior). β-TCVAE penalizes only TC with a factor α (typically α=β-1), leaving the MI and dimension-wise KL terms weighted at 1. This surgical penalty achieves the same disentanglement effect as β-VAE while preserving more reconstruction quality, because MI and dimension-wise KL are not inflated.

- Full KL = I(x;z)  +  TC(z)  +  Σⱼ KL(q(zⱼ)||p(zⱼ)) — three distinct terms with different roles.
- I(x;z) should NOT be penalized heavily — it represents useful information encoded in z.
- TC(z) is the disentanglement term — penalizing it encourages factorial marginal q(z) ≈ ∏ⱼ q(zⱼ).
- β-TCVAE uses minibatch-stratified sampling to estimate TC without an adversarial discriminator.
- FactorVAE estimates TC adversarially; β-TCVAE estimates it via importance weighting — both target the same term.

> **Choosing β in Practice**: Start with β=4 and increase if traversals show entanglement. β=8–16 is the typical sweet spot for dSprites and 3D Shapes benchmarks. If reconstructions become too blurry at high β, try FactorVAE (γ=10–40) or β-TCVAE instead — they achieve equivalent disentanglement with better reconstruction by penalizing total correlation more precisely rather than the full KL.

| Model | Loss | β / γ | Disentanglement Score | Reconstruction Quality | Interpretability |
| --- | --- | --- | --- | --- | --- |
| VAE (β=1) | Recon + 1·KL | β=1 | Low (~0.5 BetaVAE) | High — sharp reconstructions | Entangled factors, hard to interpret |
| β-VAE (β=4) | Recon + 4·KL | β=4 | Medium (~0.7) | Moderate — slightly blurry | Several factors isolated |
| β-VAE (β=16) | Recon + 16·KL | β=16 | High (~0.85) | Low — blurry reconstructions | Most factors isolated, some lost |
| FactorVAE | Recon + MI + dim-KL + γ·TC | γ=10–40 | High (~0.85–0.9) | Better than β-VAE at same score | Independent TC penalty, cleaner |
| β-TCVAE | Recon + MI + β·TC + dim-KL | β=4–8 on TC only | High (~0.85–0.9) | Better than β-VAE | Explicit TC decomposition, principled |

- β=1 is the standard VAE — the ELBO lower bound on log p(x) with no extra disentanglement pressure.
- Total correlation TC(z) = KL(q(z) || ∏ⱼ q(zⱼ)) is zero if and only if all latent dimensions are mutually independent.
- The BetaVAE disentanglement score saturates at ~0.9 on dSprites; perfect scores are unachievable because stochastic encoding adds noise to difference vectors.
- FactorVAE's permute-dims trick shuffles each latent dimension independently across the batch to approximate samples from the factorial marginal ∏ⱼ q(zⱼ).
- β-TCVAE (Chen et al. 2018) decomposes the KL into three terms — index-code MI (I(x;z)), TC(z), and dimension-wise KL — and penalizes only TC, giving the most principled objective.
- Disentanglement is dataset-dependent: models with high BetaVAE scores on dSprites may not disentangle on natural images where factors are correlated.

---

β-VAE establishes that a single scalar hyperparameter can shift the VAE from a pure generative model toward a disentangled representation learner. FactorVAE and β-TCVAE refine this insight by isolating total correlation as the operative term, yielding better disentanglement-quality tradeoffs. These models find practical use in controllable generation, scientific factor discovery, and data augmentation — anywhere that interpretable, independent latent factors are more valuable than pixel-perfect reconstruction.

