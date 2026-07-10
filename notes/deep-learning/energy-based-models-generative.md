---
title: "Energy-Based Models — Contrastive Divergence and Langevin Sampling"
slug: "energy-based-models-generative"
description: "Energy-based models define unnormalized densities via a learned energy function and train via contrastive divergence with MCMC sampling, with Langevin dynamics providing a gradient-based sampler that connects EBMs to score-based models and enables out-of-distribution detection."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW5lcmd5LUJhc2VkIE1vZGVscyAoRUJNcykgZGVmaW5lIGEgcHJvYmFiaWxpdHkgZGlzdHJpYnV0aW9uIHZpYSBhbiBlbmVyZ3kgZnVuY3Rpb24gRV/OuCh4KTogcF/OuCh4KSA9IGV4cCgtRV/OuCh4KSkgLyBaKM64KSwgd2hlcmUgWijOuCkgPSDiiKtleHAoLUVfzrgoeCkpZHggaXMgdGhlIHBhcnRpdGlvbiBmdW5jdGlvbi4gTG93IGVuZXJneSBjb3JyZXNwb25kcyB0byBoaWdoIHByb2JhYmlsaXR5IOKAlCB0aGUgbW9kZWwgYXNzaWducyBsb3cgZW5lcmd5IHRvIGRhdGEtbGlrZSBzYW1wbGVzIGFuZCBoaWdoIGVuZXJneSB0byB1bmxpa2VseSBvbmVzLiBUaGUgY2VudHJhbCBjaGFsbGVuZ2UgaXMgdGhhdCBaKM64KSBpcyBpbnRyYWN0YWJsZSBmb3IgY29udGludW91cyBoaWdoLWRpbWVuc2lvbmFsIHgsIHNvIG1heGltdW0gbGlrZWxpaG9vZCB0cmFpbmluZyByZXF1aXJlcyBhcHByb3hpbWF0aW5nIHRoZSBncmFkaWVudCBvZiBsb2cgWiB3aXRoIE1DTUMgc2FtcGxpbmcuIEVCTXMgYXJlIGEgZmxleGlibGUgZnJhbWV3b3JrIHRoYXQgdW5pZmllcyBCb2x0em1hbm4gbWFjaGluZXMsIGRlbm9pc2luZyBhdXRvZW5jb2RlcnMsIGFuZCBzY29yZS1iYXNlZCBtb2RlbHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRW5lcmd5IEZ1bmN0aW9uIGFuZCBVbm5vcm1hbGl6ZWQgRGVuc2l0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGdyYWRpZW50IG9mIHRoZSBsb2ctbGlrZWxpaG9vZCBkZWNvbXBvc2VzIGludG8gdHdvIHRlcm1zOiDiiIdfzrggbG9nIHBfzrgoeCkgPSAt4oiHX864IEVfzrgoeCkgKyBFX3twX864fVviiIdfzrggRV/OuCh4KV0uIFRoZSBmaXJzdCB0ZXJtIChkYXRhIHRlcm0pIHB1c2hlcyBkb3duIGVuZXJneSBhdCByZWFsIGRhdGEgcG9pbnRzLiBUaGUgc2Vjb25kIHRlcm0gKG1vZGVsIHRlcm0pIHB1c2hlcyB1cCBlbmVyZ3kgYXQgbW9kZWwgc2FtcGxlcywgY29tcHV0ZWQgYnkgTUNNQy4gSWYgdGhlIG1vZGVsIHNhbXBsZXMgYXJlIGhpZ2ggcXVhbGl0eSwgdGhpcyBncmFkaWVudCBjb3JyZWN0bHkgc2hhcGVzIHRoZSBlbmVyZ3kgbGFuZHNjYXBlLiBUaGUgZGF0YSB0ZXJtIGlzIGV4YWN0OyB0aGUgbW9kZWwgdGVybSBpcyBlc3RpbWF0ZWQgdmlhIGsgc3RlcHMgb2YgTWFya292IGNoYWluIE1vbnRlIENhcmxvIGZyb20gdGhlIGN1cnJlbnQgbW9kZWwgZGlzdHJpYnV0aW9uLCBtYWtpbmcgRUJNIHRyYWluaW5nIGZ1bmRhbWVudGFsbHkgdGllZCB0byBNQ01DIHF1YWxpdHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEVuZXJneU5ldChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIk5ldXJhbCBuZXR3b3JrIGVuZXJneSBmdW5jdGlvbjogbWFwcyBpbnB1dCB0byBzY2FsYXIgZW5lcmd5IChsb3dlciA9IG1vcmUgbGlrZWx5KS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfZGltLCBoaWRkZW49MjU2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihpbnB1dF9kaW0sIGhpZGRlbiksIG5uLkxlYWt5UmVMVSgwLjIpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuKSwgbm4uTGVha3lSZUxVKDAuMiksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuLCAxKVxuICAgICAgICApXG5cbiAgICBkZWYgZW5lcmd5KHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeCkuc3F1ZWV6ZSgtMSkgICMgKEIsKVxuXG4gICAgZGVmIHVubm9ybV9sb2dfcHJvYihzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIC1zZWxmLmVuZXJneSh4KSAgICAgICAgICAjIGxvZyBwKih4KSB3aXRob3V0IFpcblxuIyBEZW1vOiBlbmVyZ3kgbGFuZHNjYXBlIG92ZXIgMkQgZ3JpZFxuZWJtID0gRW5lcmd5TmV0KGlucHV0X2RpbT0yKVxudG9yY2gubWFudWFsX3NlZWQoMClcbmdyaWQgPSB0b3JjaC5zdGFjayh0b3JjaC5tZXNoZ3JpZChcbiAgICB0b3JjaC5saW5zcGFjZSgtMywgMywgMzApLCB0b3JjaC5saW5zcGFjZSgtMywgMywgMzApLCBpbmRleGluZz1cdTAwMjdpalx1MDAyN1xuKSwgZGltPS0xKS5yZXNoYXBlKC0xLCAyKVxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgZW5lcmdpZXMgPSBlYm0uZW5lcmd5KGdyaWQpXG5wcmludChmXHUwMDI3R3JpZCBlbmVyZ3kgcmFuZ2U6IFt7ZW5lcmdpZXMubWluKCk6LjNmfSwge2VuZXJnaWVzLm1heCgpOi4zZn1dXHUwMDI3KVxucHJpbnQoZlx1MDAyN0VuZXJneSBhdCBvcmlnaW46IHtlYm0uZW5lcmd5KHRvcmNoLnplcm9zKDEsIDIpKS5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdVbm5vcm0gbG9nLXByb2IgYXQgb3JpZ2luOiB7ZWJtLnVubm9ybV9sb2dfcHJvYih0b3JjaC56ZXJvcygxLCAyKSkuaXRlbSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udHJhc3RpdmUgRGl2ZXJnZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udHJhc3RpdmUgRGl2ZXJnZW5jZSAoQ0QsIEhpbnRvbiAyMDAyKSBhcHByb3hpbWF0ZXMgdGhlIGludHJhY3RhYmxlIG1vZGVsIGV4cGVjdGF0aW9uIGJ5IHJ1bm5pbmcgYSBzaG9ydCBNYXJrb3YgY2hhaW4gc3RhcnRpbmcgZnJvbSBkYXRhIHBvaW50cyBpbnN0ZWFkIG9mIGZyb20gbm9pc2UuIENELWsgaW5pdGlhbGlzZXMgY2hhaW5zIGF0IGRhdGEgeCB+IHBfZGF0YSBhbmQgcnVucyBrIEdpYmJzIG9yIExhbmdldmluIHN0ZXBzIHRvIGdldCBcdTAwMjduZWdhdGl2ZVx1MDAyNyBzYW1wbGVzIHheLSB0aGF0IGFwcHJveGltYXRlIHBfzrguIFRoZSBncmFkaWVudCBlc3RpbWF0ZSBpczog4oiHX864IEwg4omIIEVfZGF0YVviiIdfzrggRV/OuCh4KV0gLSBFW+KIh1/OuCBFX864KHheLSldLiBXaXRoIGs9MSwgQ0QgaXMgYmlhc2VkIGJ1dCBjb21wdXRhdGlvbmFsbHkgY2hlYXAgYW5kIHdvcmtzIHdlbGwgZm9yIHNoYWxsb3cgbW9kZWxzIGxpa2UgUkJNcy4gVGhlIGJpYXMgY29tZXMgZnJvbSB0aGUgY2hhaW5zIG5vdCBtaXhpbmcgdG8gdGhlIHRydWUgbW9kZWwgZGlzdHJpYnV0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgbGFuZ2V2aW5fc3RlcChlYm0sIHgsIHN0ZXBfc2l6ZT0wLjAxLCBub2lzZV9zY2FsZT0wLjAwNSk6XG4gICAgXCJcIlwiU2luZ2xlIExhbmdldmluIE1DTUMgc3RlcCB0b3dhcmQgbG93ZXIgZW5lcmd5IHJlZ2lvbnMuXCJcIlwiXG4gICAgeCA9IHguZGV0YWNoKCkucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICBlbmVyZ3kgPSBlYm0uZW5lcmd5KHgpLnN1bSgpXG4gICAgZW5lcmd5LmJhY2t3YXJkKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgeF9uZXcgPSB4IC0gc3RlcF9zaXplICogeC5ncmFkICsgbm9pc2Vfc2NhbGUgKiB0b3JjaC5yYW5kbl9saWtlKHgpXG4gICAgcmV0dXJuIHhfbmV3LmRldGFjaCgpXG5cbmRlZiBjZF9rX3VwZGF0ZShlYm0sIHhfZGF0YSwgaz0xLCBscj0xZS0zLCBzdGVwX3NpemU9MC4wMSk6XG4gICAgXCJcIlwiQ0QtazogcnVuIGsgTGFuZ2V2aW4gc3RlcHMgZnJvbSBkYXRhLCBjb21wdXRlIGNvbnRyYXN0aXZlIGdyYWRpZW50LlwiXCJcIlxuICAgIG9wdGltaXplciA9IHRvcmNoLm9wdGltLkFkYW0oZWJtLnBhcmFtZXRlcnMoKSwgbHI9bHIpXG4gICAgeF9uZWcgPSB4X2RhdGEuY2xvbmUoKS5kZXRhY2goKVxuICAgIGZvciBfIGluIHJhbmdlKGspOlxuICAgICAgICB4X25lZyA9IGxhbmdldmluX3N0ZXAoZWJtLCB4X25lZywgc3RlcF9zaXplPXN0ZXBfc2l6ZSlcbiAgICBlbmVyZ3lfcG9zID0gZWJtLmVuZXJneSh4X2RhdGEpXG4gICAgZW5lcmd5X25lZyA9IGVibS5lbmVyZ3koeF9uZWcuZGV0YWNoKCkpXG4gICAgIyBNaW5pbWl6ZSBlbmVyZ3kgYXQgZGF0YSwgbWF4aW1pemUgYXQgbW9kZWwgc2FtcGxlc1xuICAgIGxvc3MgPSBlbmVyZ3lfcG9zLm1lYW4oKSAtIGVuZXJneV9uZWcubWVhbigpXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgb3B0aW1pemVyLnN0ZXAoKVxuICAgIHJldHVybiBsb3NzLml0ZW0oKSwgeF9uZWdcblxuZWJtID0gRW5lcmd5TmV0KGlucHV0X2RpbT0yKVxudG9yY2gubWFudWFsX3NlZWQoMClcbnhfZGF0YSA9IHRvcmNoLnJhbmRuKDY0LCAyKSAqIDAuNSArIDIuMCAgIyBkYXRhIGNsdXN0ZXIgYXQgKDIsMilcbmZvciBzdGVwIGluIHJhbmdlKDUwKTpcbiAgICBsb3NzLCB4X25lZyA9IGNkX2tfdXBkYXRlKGVibSwgeF9kYXRhLCBrPTUpXG4gICAgaWYgc3RlcCAlIDEwID09IDA6XG4gICAgICAgIHByaW50KGZcdTAwMjdTdGVwIHtzdGVwfTogQ0QgbG9zcz17bG9zczouNGZ9ICBFX2RhdGE9e2VibS5lbmVyZ3koeF9kYXRhKS5tZWFuKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQZXJzaXN0ZW50IENvbnRyYXN0aXZlIERpdmVyZ2VuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBlcnNpc3RlbnQgQ0QgKFBDRCwgVGllbGVtYW4gMjAwOCkgbWFpbnRhaW5zIGEgc2V0IG9mIHBlcnNpc3RlbnQgTWFya292IGNoYWlucyBhY3Jvc3MgcGFyYW1ldGVyIHVwZGF0ZXMgaW5zdGVhZCBvZiByZXN0YXJ0aW5nIGZyb20gZGF0YSBlYWNoIHN0ZXAuIFRoZSBjaGFpbnMgYWNjdW11bGF0ZSBtaXhpbmcgaGlzdG9yeSBhbmQgZXZlbnR1YWxseSBzYW1wbGUgZnJvbSB0aGUgdHJ1ZSBtb2RlbCBkaXN0cmlidXRpb24gKGdpdmVuIHNsb3cgZW5vdWdoIHBhcmFtZXRlciB1cGRhdGVzKS4gUENEIHByb2R1Y2VzIGJldHRlciBtb2RlbCBzYW1wbGVzIHRoYW4gQ0QtayBhdCB0aGUgY29zdCBvZiBtZW1vcnkgZm9yIHN0b3JpbmcgY2hhaW4gc3RhdGVzLiBUaGUgdHJhZGVvZmY6IGlmIGxlYXJuaW5nIHJhdGUgaXMgdG9vIGxhcmdlLCBwYXJhbWV0ZXJzIGNoYW5nZSBmYXN0ZXIgdGhhbiBjaGFpbnMgY2FuIG1peCwgY2F1c2luZyB0aGUgcGVyc2lzdGVudCBzYW1wbGVzIHRvIGxhZyBiZWhpbmQgdGhlIHRydWUgbW9kZWwgZGlzdHJpYnV0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxhbmdldmluIER5bmFtaWNzIE1DTUMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0b2NoYXN0aWMgR3JhZGllbnQgTGFuZ2V2aW4gRHluYW1pY3MgKFNHTEQpIHNhbXBsZXMgZnJvbSBwX864IHVzaW5nIHRoZSBncmFkaWVudCBvZiB0aGUgZW5lcmd5OiB4X3t0KzF9ID0geF90IC0gzrXCt+KIh194IEVfzrgoeF90KSArIOKImigyzrUpwrfOviB3aGVyZSDOviB+IE4oMCxJKS4gVGhpcyBpcyBncmFkaWVudCBkZXNjZW50IG9uIHRoZSBlbmVyZ3kgd2l0aCBpbmplY3RlZCBub2lzZSB0byBwcmV2ZW50IGNvbGxhcHNlIHRvIGEgc2luZ2xlIG1vZGUuIEluIHRoZSBsaW1pdCDOteKGkjAgd2l0aCBzdGVwIGNvdW50IFTihpLiiJ4sIFNHTEQgc2FtcGxlcyBleGFjdGx5IGZyb20gcF/OuC4gSW4gcHJhY3RpY2UsIGZpbml0ZSDOtSBpbnRyb2R1Y2VzIGJpYXMg4oCUIHRoaXMgaXMgdGhlIGZ1bmRhbWVudGFsIHRlbnNpb24gaW4gRUJNIHRyYWluaW5nLiBUaGUgZ3JhZGllbnQg4oiHX3ggRV/OuCh4KSBjb25uZWN0cyBFQk1zIGRpcmVjdGx5IHRvIHNjb3JlLWJhc2VkIG1vZGVsczogc2NvcmUgPSAt4oiHX3ggRV/OuCh4KSA9IOKIh194IGxvZyBwX864KHgpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgbGFuZ2V2aW5fc2FtcGxlKGVibSwgbl9zYW1wbGVzPTI1Niwgbl9zdGVwcz0xMDAsIHN0ZXBfc2l6ZT0wLjEsXG4gICAgICAgICAgICAgICAgICAgIG5vaXNlX3NjYWxlPTAuMDEsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpOlxuICAgIFwiXCJcIlNHTEQgc2FtcGxlcjogZ3JhZGllbnQgZGVzY2VudCBvbiBlbmVyZ3kgKyBHYXVzc2lhbiBub2lzZSBpbmplY3Rpb24uXCJcIlwiXG4gICAgeCA9IHRvcmNoLnJhbmRuKG5fc2FtcGxlcywgMiwgZGV2aWNlPWRldmljZSkgICMgc3RhcnQgZnJvbSBub2lzZVxuICAgIHRyYWplY3RvcnlfZW5lcmdpZXMgPSBbXVxuICAgIGZvciBzdGVwIGluIHJhbmdlKG5fc3RlcHMpOlxuICAgICAgICB4ID0geC5kZXRhY2goKS5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgICAgICBlbmVyZ3kgPSBlYm0uZW5lcmd5KHgpLnN1bSgpXG4gICAgICAgIGVuZXJneS5iYWNrd2FyZCgpXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgIyBHcmFkaWVudCBzdGVwIHRvd2FyZCBsb3ctZW5lcmd5IHJlZ2lvbnMgKyBMYW5nZXZpbiBub2lzZVxuICAgICAgICAgICAgeCA9IHggLSBzdGVwX3NpemUgKiB4LmdyYWQgKyAoMiAqIHN0ZXBfc2l6ZSkgKiogMC41ICogbm9pc2Vfc2NhbGUgKiB0b3JjaC5yYW5kbl9saWtlKHgpXG4gICAgICAgIGlmIHN0ZXAgJSAyMCA9PSAwOlxuICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICAgICAgZSA9IGVibS5lbmVyZ3koeC5kZXRhY2goKSkubWVhbigpLml0ZW0oKVxuICAgICAgICAgICAgdHJhamVjdG9yeV9lbmVyZ2llcy5hcHBlbmQoZSlcbiAgICByZXR1cm4geC5kZXRhY2goKSwgdHJhamVjdG9yeV9lbmVyZ2llc1xuXG5lYm0gPSBFbmVyZ3lOZXQoaW5wdXRfZGltPTIpXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbnNhbXBsZXMsIGVuZXJnaWVzID0gbGFuZ2V2aW5fc2FtcGxlKGVibSwgbl9zYW1wbGVzPTEyOCwgbl9zdGVwcz0xMDApXG5wcmludChmXHUwMDI3TGFuZ2V2aW4gTUNNQzoge2xlbihlbmVyZ2llcyl9IGNoZWNrcG9pbnRzXHUwMDI3KVxuZm9yIGksIGUgaW4gZW51bWVyYXRlKGVuZXJnaWVzKTpcbiAgICBwcmludChmXHUwMDI3ICBTdGVwIHtpKjIwOjNkfTogbWVhbiBlbmVyZ3kgPSB7ZTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbm5lY3Rpb24gdG8gU2NvcmUgTWF0Y2hpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzY29yZSBmdW5jdGlvbiBzKHgpID0g4oiHX3ggbG9nIHAoeCkgPSAt4oiHX3ggRV/OuCh4KSBkaXJlY3RseSBsaW5rcyBFQk1zIHRvIGRlbm9pc2luZyBzY29yZSBtYXRjaGluZyBhbmQgZGlmZnVzaW9uIG1vZGVscy4gU2NvcmUgbWF0Y2hpbmcgKEh5dsOkcmluZW4gMjAwNSkgYXZvaWRzIHRoZSBwYXJ0aXRpb24gZnVuY3Rpb24gZW50aXJlbHkgYnkgdHJhaW5pbmcgb24gdGhlIFN0ZWluIGlkZW50aXR5OiBFW3x84oiHX3ggbG9nIHBfzrgoeCkgLSDiiIdfeCBsb2cgcF9kYXRhKHgpfHzCsl0gY2FuIGJlIGNvbXB1dGVkIHdpdGhvdXQga25vd2luZyBaLiBEZW5vaXNpbmcgc2NvcmUgbWF0Y2hpbmcgZnVydGhlciBjb252ZXJ0cyB0aGlzIHRvIGEgcmVncmVzc2lvbiBwcm9ibGVtOiBwcmVkaWN0IHRoZSBzY29yZSBmcm9tIG5vaXN5IHNhbXBsZXMuIFRoaXMgaW5zaWdodCDigJQgdGhhdCB0cmFpbmluZyBFQk1zIGFuZCBzY29yZSBtb2RlbHMgYXJlIGVxdWl2YWxlbnQg4oCUIHVuZGVybGllcyB3aHkgZGlmZnVzaW9uIG1vZGVscyBjYW4gYmUgaW50ZXJwcmV0ZWQgYXMgaGllcmFyY2hpY2FsIEVCTXMgd2l0aCBkaWZmZXJlbnQgbm9pc2UgbGV2ZWxzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVCTXMgZm9yIE9PRCBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkVCTXMgcHJvdmlkZSBhIHByaW5jaXBsZWQgZnJhbWV3b3JrIGZvciBvdXQtb2YtZGlzdHJpYnV0aW9uIGRldGVjdGlvbjogaW4tZGlzdHJpYnV0aW9uIHNhbXBsZXMgc2hvdWxkIGhhdmUgbG93IGVuZXJneSAoaGlnaCBwcm9iYWJpbGl0eSkgYW5kIE9PRCBzYW1wbGVzIHNob3VsZCBoYXZlIGhpZ2ggZW5lcmd5LiBUaGlzIGlzIGluIGNvbnRyYXN0IHRvIGNsYXNzaWZpZXJzLCB3aGljaCBjYW4gYmUgYXJiaXRyYXJpbHkgY29uZmlkZW50IG9uIE9PRCBpbnB1dHMuIEdyYXRod29obCBldCBhbC4gKEpFTSwgMjAyMCkgc2hvd2VkIHRoYXQgdHJhaW5pbmcgYSBqb2ludCBlbmVyZ3ktYmFzZWQgbW9kZWwg4oCUIHdoZXJlIHRoZSBzYW1lIG5ldHdvcmsgc2VydmVzIGFzIGJvdGggY2xhc3NpZmllciBhbmQgZW5lcmd5IGZ1bmN0aW9uIOKAlCBhY2hpZXZlcyBzdHJvbmcgT09EIGRldGVjdGlvbiB3aGlsZSBtYWludGFpbmluZyBjbGFzc2lmaWNhdGlvbiBhY2N1cmFjeS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBudW1weSBhcyBucFxuXG5jbGFzcyBKRU1DbGFzc2lmaWVyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiSm9pbnQgRW5lcmd5IE1vZGVsOiBjbGFzc2lmaWVyIHRoYXQgYWxzbyBjb21wdXRlcyBmcmVlIGVuZXJneSBmb3IgT09EIGRldGVjdGlvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfZGltLCBuX2NsYXNzZXMsIGhpZGRlbj0xMjgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGlucHV0X2RpbSwgaGlkZGVuKSwgbm4uR0VMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgaGlkZGVuKSwgbm4uR0VMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbiwgbl9jbGFzc2VzKVxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldCh4KSAgIyBsb2dpdHNcbiAgICBkZWYgZnJlZV9lbmVyZ3koc2VsZiwgeCk6XG4gICAgICAgIGxvZ2l0cyA9IHNlbGYuZm9yd2FyZCh4KVxuICAgICAgICByZXR1cm4gLXRvcmNoLmxvZ3N1bWV4cChsb2dpdHMsIGRpbT0tMSkgICMgLWxvZyBzdW1fYyBleHAoZl9jKHgpKVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubW9kZWwgPSBKRU1DbGFzc2lmaWVyKGlucHV0X2RpbT0xMCwgbl9jbGFzc2VzPTQpXG5cbiMgSW4tZGlzdHJpYnV0aW9uIGRhdGEgKE1OSVNULWxpa2UsIGZlYXR1cmVzIGluIFstMSwgMV0pXG54X2luICA9IHRvcmNoLnJhbmRuKDEwMCwgMTApICogMC41XG4jIE9PRCBkYXRhICh2ZXJ5IGRpZmZlcmVudCBkaXN0cmlidXRpb24pXG54X29vZCA9IHRvcmNoLnJhbmRuKDEwMCwgMTApICogNS4wICsgMTAuMFxuXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBlX2luICA9IG1vZGVsLmZyZWVfZW5lcmd5KHhfaW4pXG4gICAgZV9vb2QgPSBtb2RlbC5mcmVlX2VuZXJneSh4X29vZClcbnByaW50KGZcdTAwMjdJbi1kaXN0cmlidXRpb24gZnJlZSBlbmVyZ3k6ICBtZWFuPXtlX2luLm1lYW4oKTouM2Z9IHN0ZD17ZV9pbi5zdGQoKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN09PRCBmcmVlIGVuZXJneTogICAgICAgICAgICAgIG1lYW49e2Vfb29kLm1lYW4oKTouM2Z9IHN0ZD17ZV9vb2Quc3RkKCk6LjNmfVx1MDAyNylcbmF1cm9jX3Byb3h5ID0gKGVfb29kIFx1MDAzZSBlX2luLm1lZGlhbigpKS5mbG9hdCgpLm1lYW4oKSAgIyBoaWdoZXIgZW5lcmd5ID0gT09EXG5wcmludChmXHUwMDI3QVVST0MgcHJveHkgKGhpZ2hlciBFID0gT09EKToge2F1cm9jX3Byb3h5Oi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIENvbnNpZGVyYXRpb25zIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJNQ01DIEluc3RhYmlsaXR5IGluIEVCTSBUcmFpbmluZyIsImNvbnRlbnQiOiJFQk0gdHJhaW5pbmcgaXMgbm90b3Jpb3VzbHkgdW5zdGFibGUgYmVjYXVzZSB0aGUgbW9kZWwgc2FtcGxlcyB1c2VkIGZvciB0aGUgY29udHJhc3RpdmUgZ3JhZGllbnQgYXJlIHRoZW1zZWx2ZXMgcHJvZHVjZWQgYnkgdGhlIGN1cnJlbnQgbW9kZWwuIElmIHRoZSBNQ01DIGNoYWlucyBkbyBub3QgbWl4IChlLmcuLCBzdGVwIHNpemUgdG9vIHNtYWxsLCB0b28gZmV3IHN0ZXBzKSwgdGhlIG1vZGVsIHNhbXBsZXMgY2x1c3RlciBuZWFyIGRhdGEgcG9pbnRzIGFuZCB0aGUgZW5lcmd5IGxhbmRzY2FwZSBkb2VzIG5vdCBsZWFybiB0byBwdXNoIHVwIGVuZXJneSBpbiBiZXR3ZWVuIG1vZGVzLiBNb25pdG9yIHRoZSBlbmVyZ3kgZ2FwIGJldHdlZW4gZGF0YSBhbmQgbW9kZWwgc2FtcGxlcyDigJQgYSBzaHJpbmtpbmcgZ2FwIGluZGljYXRlcyB0aGUgY2hhaW5zIGFyZSBub3QgZXhwbG9yaW5nLiBVc2Ugc3BlY3RyYWwgbm9ybWFsaXNhdGlvbiBvbiB0aGUgZW5lcmd5IG5ldHdvcmsgdG8gc3RhYmlsaXNlIHRyYWluaW5nLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIkxpa2VsaWhvb2QgVHJhY3RhYmxlIiwiU2FtcGxlIFF1YWxpdHkiLCJUcmFpbmluZyBTdGFiaWxpdHkiLCJNQ01DIE5lZWRlZCIsIk9PRCBEZXRlY3Rpb24iXSwicm93cyI6W1siVkFFIiwiWWVzIChFTEJPIGxvd2VyIGJvdW5kKSIsIk1vZGVyYXRlIOKAlCBibHVycnkiLCJIaWdoIOKAlCBzdGFibGUgS0wgb2JqZWN0aXZlIiwiTm8iLCJQb29yIOKAlCBkZWNvZGVyIHVuY2VydGFpbnR5Il0sWyJHQU4iLCJObyIsIkhpZ2gg4oCUIHNoYXJwIHNhbXBsZXMiLCJMb3cg4oCUIG1vZGUgY29sbGFwc2UsIG9zY2lsbGF0aW9uIiwiTm8iLCJQb3NzaWJsZSB2aWEgZGlzY3JpbWluYXRvciJdLFsiRUJNIiwiTm8gKGludHJhY3RhYmxlIFopIiwiTW9kZXJhdGUg4oCUIG1vZGUtc2Vla2luZyIsIkxvdyDigJQgTUNNQyBpbnN0YWJpbGl0eSIsIlllcyDigJQgYXQgdHJhaW4gYW5kIHRlc3QgdGltZSIsIkV4Y2VsbGVudCDigJQgZnJlZSBlbmVyZ3kgdGhyZXNob2xkIl0sWyJEaWZmdXNpb24iLCJBcHByb3hpbWF0ZSAoRUxCTykiLCJWZXJ5IGhpZ2gg4oCUIFNvVEEiLCJIaWdoIOKAlCBzdGFibGUgTVNFIG9iamVjdGl2ZSIsIk5vIChkZXRlcm1pbmlzdGljIGF0IHRlc3QpIiwiR29vZCB2aWEgbGlrZWxpaG9vZCBwcm94eSJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUaGUgcGFydGl0aW9uIGZ1bmN0aW9uIFogaXMgaW50cmFjdGFibGUg4oCUIG5ldmVyIGF0dGVtcHQgdG8gY29tcHV0ZSBpdCBleGFjdGx5OyB1c2UgTUNNQyBhcHByb3hpbWF0aW9ucy4iLCJDRC0xIGlzIGJpYXNlZCBidXQgZmFzdCBhbmQgd29ya3MgZm9yIHNoYWxsb3cgbW9kZWxzOyB1c2UgUENEIGZvciBkZWVwZXIgbmV0d29ya3Mgd2hlcmUgbWl4aW5nIGlzIHNsb3dlci4iLCJMYW5nZXZpbiBzdGVwIHNpemUgzrUgY29udHJvbHMgdGhlIGJpYXMtdmFyaWFuY2UgdHJhZGVvZmY6IHNtYWxsIM61ID0gbG93IGJpYXMsIG1hbnkgc3RlcHMgbmVlZGVkOyBsYXJnZSDOtSA9IGZhc3QgYnV0IGJpYXNlZC4iLCJTcGVjdHJhbCBub3JtYWxpc2F0aW9uIG9uIGVuZXJneSBuZXR3b3JrIHdlaWdodHMgYm91bmRzIHRoZSBMaXBzY2hpdHogY29uc3RhbnQgYW5kIHN0YWJpbGlzZXMgdHJhaW5pbmcuIiwiSkVNIGNvbWJpbmVzIEVCTSArIGNsYXNzaWZpZXIgaW4gb25lIG5ldHdvcmsg4oCUIHRoZSBmcmVlIGVuZXJneSBzZXJ2ZXMgYXMgYW4gT09EIHNjb3JlIGF0IG5lZ2xpZ2libGUgZXh0cmEgY29zdC4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Energy-Based Models — Contrastive Divergence and Langevin Sampling

Energy-Based Models (EBMs) define a probability distribution via an energy function E_θ(x): p_θ(x) = exp(-E_θ(x)) / Z(θ), where Z(θ) = ∫exp(-E_θ(x))dx is the partition function. Low energy corresponds to high probability — the model assigns low energy to data-like samples and high energy to unlikely ones. The central challenge is that Z(θ) is intractable for continuous high-dimensional x, so maximum likelihood training requires approximating the gradient of log Z with MCMC sampling. EBMs are a flexible framework that unifies Boltzmann machines, denoising autoencoders, and score-based models.

## Energy Function and Unnormalized Density

The gradient of the log-likelihood decomposes into two terms: ∇_θ log p_θ(x) = -∇_θ E_θ(x) + E_{p_θ}[∇_θ E_θ(x)]. The first term (data term) pushes down energy at real data points. The second term (model term) pushes up energy at model samples, computed by MCMC. If the model samples are high quality, this gradient correctly shapes the energy landscape. The data term is exact; the model term is estimated via k steps of Markov chain Monte Carlo from the current model distribution, making EBM training fundamentally tied to MCMC quality.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class EnergyNet(nn.Module):
    """Neural network energy function: maps input to scalar energy (lower = more likely)."""
    def __init__(self, input_dim, hidden=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden), nn.LeakyReLU(0.2),
            nn.Linear(hidden, hidden), nn.LeakyReLU(0.2),
            nn.Linear(hidden, 1)
        )

    def energy(self, x):
        return self.net(x).squeeze(-1)  # (B,)

    def unnorm_log_prob(self, x):
        return -self.energy(x)          # log p*(x) without Z

# Demo: energy landscape over 2D grid
ebm = EnergyNet(input_dim=2)
torch.manual_seed(0)
grid = torch.stack(torch.meshgrid(
    torch.linspace(-3, 3, 30), torch.linspace(-3, 3, 30), indexing='ij'
), dim=-1).reshape(-1, 2)
with torch.no_grad():
    energies = ebm.energy(grid)
print(f'Grid energy range: [{energies.min():.3f}, {energies.max():.3f}]')
print(f'Energy at origin: {ebm.energy(torch.zeros(1, 2)).item():.4f}')
print(f'Unnorm log-prob at origin: {ebm.unnorm_log_prob(torch.zeros(1, 2)).item():.4f}')
```

## Contrastive Divergence

Contrastive Divergence (CD, Hinton 2002) approximates the intractable model expectation by running a short Markov chain starting from data points instead of from noise. CD-k initialises chains at data x ~ p_data and runs k Gibbs or Langevin steps to get 'negative' samples x^- that approximate p_θ. The gradient estimate is: ∇_θ L ≈ E_data[∇_θ E_θ(x)] - E[∇_θ E_θ(x^-)]. With k=1, CD is biased but computationally cheap and works well for shallow models like RBMs. The bias comes from the chains not mixing to the true model distribution.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def langevin_step(ebm, x, step_size=0.01, noise_scale=0.005):
    """Single Langevin MCMC step toward lower energy regions."""
    x = x.detach().requires_grad_(True)
    energy = ebm.energy(x).sum()
    energy.backward()
    with torch.no_grad():
        x_new = x - step_size * x.grad + noise_scale * torch.randn_like(x)
    return x_new.detach()

def cd_k_update(ebm, x_data, k=1, lr=1e-3, step_size=0.01):
    """CD-k: run k Langevin steps from data, compute contrastive gradient."""
    optimizer = torch.optim.Adam(ebm.parameters(), lr=lr)
    x_neg = x_data.clone().detach()
    for _ in range(k):
        x_neg = langevin_step(ebm, x_neg, step_size=step_size)
    energy_pos = ebm.energy(x_data)
    energy_neg = ebm.energy(x_neg.detach())
    # Minimize energy at data, maximize at model samples
    loss = energy_pos.mean() - energy_neg.mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss.item(), x_neg

ebm = EnergyNet(input_dim=2)
torch.manual_seed(0)
x_data = torch.randn(64, 2) * 0.5 + 2.0  # data cluster at (2,2)
for step in range(50):
    loss, x_neg = cd_k_update(ebm, x_data, k=5)
    if step % 10 == 0:
        print(f'Step {step}: CD loss={loss:.4f}  E_data={ebm.energy(x_data).mean():.4f}')
```

## Persistent Contrastive Divergence

Persistent CD (PCD, Tieleman 2008) maintains a set of persistent Markov chains across parameter updates instead of restarting from data each step. The chains accumulate mixing history and eventually sample from the true model distribution (given slow enough parameter updates). PCD produces better model samples than CD-k at the cost of memory for storing chain states. The tradeoff: if learning rate is too large, parameters change faster than chains can mix, causing the persistent samples to lag behind the true model distribution.

## Langevin Dynamics MCMC

Stochastic Gradient Langevin Dynamics (SGLD) samples from p_θ using the gradient of the energy: x_{t+1} = x_t - ε·∇_x E_θ(x_t) + √(2ε)·ξ where ξ ~ N(0,I). This is gradient descent on the energy with injected noise to prevent collapse to a single mode. In the limit ε→0 with step count T→∞, SGLD samples exactly from p_θ. In practice, finite ε introduces bias — this is the fundamental tension in EBM training. The gradient ∇_x E_θ(x) connects EBMs directly to score-based models: score = -∇_x E_θ(x) = ∇_x log p_θ(x).

```python
import torch
import torch.nn as nn

def langevin_sample(ebm, n_samples=256, n_steps=100, step_size=0.1,
                    noise_scale=0.01, device='cpu'):
    """SGLD sampler: gradient descent on energy + Gaussian noise injection."""
    x = torch.randn(n_samples, 2, device=device)  # start from noise
    trajectory_energies = []
    for step in range(n_steps):
        x = x.detach().requires_grad_(True)
        energy = ebm.energy(x).sum()
        energy.backward()
        with torch.no_grad():
            # Gradient step toward low-energy regions + Langevin noise
            x = x - step_size * x.grad + (2 * step_size) ** 0.5 * noise_scale * torch.randn_like(x)
        if step % 20 == 0:
            with torch.no_grad():
                e = ebm.energy(x.detach()).mean().item()
            trajectory_energies.append(e)
    return x.detach(), trajectory_energies

ebm = EnergyNet(input_dim=2)
torch.manual_seed(42)
samples, energies = langevin_sample(ebm, n_samples=128, n_steps=100)
print(f'Langevin MCMC: {len(energies)} checkpoints')
for i, e in enumerate(energies):
    print(f'  Step {i*20:3d}: mean energy = {e:.4f}')
```

## Connection to Score Matching

The score function s(x) = ∇_x log p(x) = -∇_x E_θ(x) directly links EBMs to denoising score matching and diffusion models. Score matching (Hyvärinen 2005) avoids the partition function entirely by training on the Stein identity: E[||∇_x log p_θ(x) - ∇_x log p_data(x)||²] can be computed without knowing Z. Denoising score matching further converts this to a regression problem: predict the score from noisy samples. This insight — that training EBMs and score models are equivalent — underlies why diffusion models can be interpreted as hierarchical EBMs with different noise levels.

## EBMs for OOD Detection

EBMs provide a principled framework for out-of-distribution detection: in-distribution samples should have low energy (high probability) and OOD samples should have high energy. This is in contrast to classifiers, which can be arbitrarily confident on OOD inputs. Grathwohl et al. (JEM, 2020) showed that training a joint energy-based model — where the same network serves as both classifier and energy function — achieves strong OOD detection while maintaining classification accuracy.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class JEMClassifier(nn.Module):
    """Joint Energy Model: classifier that also computes free energy for OOD detection."""
    def __init__(self, input_dim, n_classes, hidden=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden), nn.GELU(),
            nn.Linear(hidden, hidden), nn.GELU(),
            nn.Linear(hidden, n_classes)
        )
    def forward(self, x):
        return self.net(x)  # logits
    def free_energy(self, x):
        logits = self.forward(x)
        return -torch.logsumexp(logits, dim=-1)  # -log sum_c exp(f_c(x))

torch.manual_seed(0)
model = JEMClassifier(input_dim=10, n_classes=4)

# In-distribution data (MNIST-like, features in [-1, 1])
x_in  = torch.randn(100, 10) * 0.5
# OOD data (very different distribution)
x_ood = torch.randn(100, 10) * 5.0 + 10.0

with torch.no_grad():
    e_in  = model.free_energy(x_in)
    e_ood = model.free_energy(x_ood)
print(f'In-distribution free energy:  mean={e_in.mean():.3f} std={e_in.std():.3f}')
print(f'OOD free energy:              mean={e_ood.mean():.3f} std={e_ood.std():.3f}')
auroc_proxy = (e_ood > e_in.median()).float().mean()  # higher energy = OOD
print(f'AUROC proxy (higher E = OOD): {auroc_proxy:.3f}')
```

## Practical Considerations

> **MCMC Instability in EBM Training**: EBM training is notoriously unstable because the model samples used for the contrastive gradient are themselves produced by the current model. If the MCMC chains do not mix (e.g., step size too small, too few steps), the model samples cluster near data points and the energy landscape does not learn to push up energy in between modes. Monitor the energy gap between data and model samples — a shrinking gap indicates the chains are not exploring. Use spectral normalisation on the energy network to stabilise training.

| Model | Likelihood Tractable | Sample Quality | Training Stability | MCMC Needed | OOD Detection |
| --- | --- | --- | --- | --- | --- |
| VAE | Yes (ELBO lower bound) | Moderate — blurry | High — stable KL objective | No | Poor — decoder uncertainty |
| GAN | No | High — sharp samples | Low — mode collapse, oscillation | No | Possible via discriminator |
| EBM | No (intractable Z) | Moderate — mode-seeking | Low — MCMC instability | Yes — at train and test time | Excellent — free energy threshold |
| Diffusion | Approximate (ELBO) | Very high — SoTA | High — stable MSE objective | No (deterministic at test) | Good via likelihood proxy |

- The partition function Z is intractable — never attempt to compute it exactly; use MCMC approximations.
- CD-1 is biased but fast and works for shallow models; use PCD for deeper networks where mixing is slower.
- Langevin step size ε controls the bias-variance tradeoff: small ε = low bias, many steps needed; large ε = fast but biased.
- Spectral normalisation on energy network weights bounds the Lipschitz constant and stabilises training.
- JEM combines EBM + classifier in one network — the free energy serves as an OOD score at negligible extra cost.

---

