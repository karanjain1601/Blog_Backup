---
title: "Autoencoders — Undercomplete, Denoising, Sparse, Contractive"
slug: "autoencoders"
description: "A comprehensive guide to autoencoder variants: undercomplete bottlenecks, denoising autoencoders as score function estimators, sparse autoencoders with L1 and KL penalties, contractive autoencoders with Jacobian regularisation, and the connection to PCA and VAEs."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW4gYXV0b2VuY29kZXIgaXMgYSBuZXVyYWwgbmV0d29yayB0cmFpbmVkIHRvIHJlY29uc3RydWN0IGl0cyBpbnB1dCB0aHJvdWdoIGEgY29tcHJlc3NlZCBib3R0bGVuZWNrLiBUaGUgZW5jb2RlciBmOiBY4oaSWiBtYXBzIGlucHV0IHRvIGEgbGF0ZW50IGNvZGUsIHRoZSBkZWNvZGVyIGc6IFrihpJYzIIgbWFwcyBiYWNrIHRvIGlucHV0IHNwYWNlLCBhbmQgdHJhaW5pbmcgbWluaW1pc2VzIHRoZSByZWNvbnN0cnVjdGlvbiBsb3NzIOKAlnggLSBnKGYoeCkp4oCWwrIuIERpZmZlcmVudCByZWd1bGFyaXNhdGlvbiBzdHJhdGVnaWVzIHByb2R1Y2UgcXVhbGl0YXRpdmVseSBkaWZmZXJlbnQgbGF0ZW50IHJlcHJlc2VudGF0aW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcmNoaXRlY3R1cmUgYW5kIFJlY29uc3RydWN0aW9uIExvc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzaW1wbGVzdCBhdXRvZW5jb2RlciB1c2VzIGEgc2luZ2xlIGJvdHRsZW5lY2sgaGlkZGVuIGxheWVyOiB4IOKGkiBoIChlbmNvZGVyKSDihpIgeMyCIChkZWNvZGVyKSwgd2l0aCBNU0UgbG9zcyDigJZ4LXjMguKAlsKyIGZvciBjb250aW51b3VzIGlucHV0cyBvciBiaW5hcnkgY3Jvc3MtZW50cm9weSBmb3IgYmluYXJ5IGlucHV0cy4gVGhlIGJvdHRsZW5lY2sgZGltZW5zaW9uIGRfeiBcdTAwM2MgZF94IGZvcmNlcyBjb21wcmVzc2lvbi4gVGhlIGtleSBpbnNpZ2h0OiBhIGxpbmVhciBhdXRvZW5jb2RlciB3aXRoIE1TRSBsb3NzIHJlY292ZXJzIGV4YWN0bHkgdGhlIFBDQSBzdWJzcGFjZSDigJQgaXQgZmluZHMgdGhlIHNhbWUgZGlyZWN0aW9ucyBvZiBtYXhpbXVtIHZhcmlhbmNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuZGVyY29tcGxldGUgQXV0b2VuY29kZXIgdnMgUENBIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9kaWdpdHNcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBQQ0FcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5YLCB5ID0gbG9hZF9kaWdpdHMocmV0dXJuX1hfeT1UcnVlKVxuWCA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKS5hc3R5cGUobnAuZmxvYXQzMilcblhfdCA9IHRvcmNoLnRlbnNvcihYKVxuXG5jbGFzcyBBdXRvZW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbnB1dF9kaW09NjQsIGxhdGVudF9kaW09Mik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVuY29kZXIgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGlucHV0X2RpbSwgMzIpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoMzIsIGxhdGVudF9kaW0pXG4gICAgICAgIClcbiAgICAgICAgc2VsZi5kZWNvZGVyID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihsYXRlbnRfZGltLCAzMiksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcigzMiwgaW5wdXRfZGltKVxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLmRlY29kZXIoc2VsZi5lbmNvZGVyKHgpKVxuXG5tb2RlbCA9IEF1dG9lbmNvZGVyKGxhdGVudF9kaW09Milcbm9wdCA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0zKVxuZm9yIGVwb2NoIGluIHJhbmdlKDMwMCk6XG4gICAgbG9zcyA9IG5uLk1TRUxvc3MoKShtb2RlbChYX3QpLCBYX3QpXG4gICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbiAgICBpZiBlcG9jaCAlIDEwMCA9PSAwOlxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NofTogbG9zcz17bG9zcy5pdGVtKCk6LjRmfVx1MDAyNylcblxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgWl9hZSA9IG1vZGVsLmVuY29kZXIoWF90KS5udW1weSgpXG5aX3BjYSA9IFBDQShuX2NvbXBvbmVudHM9MikuZml0X3RyYW5zZm9ybShYKVxucHJpbnQoZlx1MDAyN0FFIGxhdGVudCBzaGFwZToge1pfYWUuc2hhcGV9LCAgUENBIHNoYXBlOiB7Wl9wY2Euc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlbm9pc2luZyBBdXRvZW5jb2RlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBkZW5vaXNpbmcgYXV0b2VuY29kZXIgKERBRSkgdHJhaW5zIG9uIGNvcnJ1cHRlZCBpbnB1dHMgeMyDIGFuZCByZWNvbnN0cnVjdHMgdGhlIGNsZWFuIHguIFRoZSBjb3JydXB0aW9uIGNhbiBiZSBHYXVzc2lhbiBub2lzZSwgbWFza2luZyAoZHJvcG91dCksIG9yIHNhbHQtYW5kLXBlcHBlciBub2lzZS4gVGhlIGtleSBpbnNpZ2h0IChWaW5jZW50IGV0IGFsLiAyMDExKTogdGhlIERBRSBsZWFybnMgdG8gZXN0aW1hdGUgdGhlIGdyYWRpZW50IG9mIHRoZSBsb2cgZGF0YSBkZW5zaXR5IOKIgmxvZyBwKHgpL+KIgngg4oCUIGEgc2NvcmUgZnVuY3Rpb24uIFRoaXMgZm9yY2VzIHRoZSBtb2RlbCB0byB1bmRlcnN0YW5kIHRoZSBkYXRhIG1hbmlmb2xkIHJhdGhlciB0aGFuIGp1c3QgbWVtb3Jpc2luZyBpbnB1dHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9kaWdpdHNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBNaW5NYXhTY2FsZXJcblxuWCwgeSA9IGxvYWRfZGlnaXRzKHJldHVybl9YX3k9VHJ1ZSlcblggPSBNaW5NYXhTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpLmFzdHlwZShucC5mbG9hdDMyKVxuWF90ID0gdG9yY2gudGVuc29yKFgpXG5ub2lzZV9zdGQgPSAwLjNcblxuY2xhc3MgRGVub2lzaW5nQUUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltPTY0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkaW0sIDEyOCksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcigxMjgsIDMyKSwgbm4uUmVMVSgpXG4gICAgICAgIClcbiAgICAgICAgc2VsZi5kZWMgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKDMyLCAxMjgpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoMTI4LCBkaW0pLCBubi5TaWdtb2lkKClcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5kZWMoc2VsZi5lbmMoeCkpXG5cbm1vZGVsID0gRGVub2lzaW5nQUUoKVxub3B0ID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5cbmZvciBlcG9jaCBpbiByYW5nZSgzMDApOlxuICAgIG5vaXNlID0gdG9yY2gucmFuZG5fbGlrZShYX3QpICogbm9pc2Vfc3RkXG4gICAgWF9ub2lzeSA9IHRvcmNoLmNsYW1wKFhfdCArIG5vaXNlLCAwLjAsIDEuMCkgICMgY29ycnVwdFxuICAgIFhfcmVjb24gPSBtb2RlbChYX25vaXN5KSAgICAgICAgICAgICAgICAgICAgICAgICMgcmVjb25zdHJ1Y3RcbiAgICBsb3NzID0gbm4uTVNFTG9zcygpKFhfcmVjb24sIFhfdCkgICAgICAgICAgICAgICAjIHRhcmdldDogY2xlYW4hXG4gICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbiAgICBpZiBlcG9jaCAlIDEwMCA9PSAwOlxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NofTogbG9zcz17bG9zcy5pdGVtKCk6LjRmfVx1MDAyNylcblxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgbm9pc2UgPSB0b3JjaC5yYW5kbl9saWtlKFhfdFs6OF0pICogbm9pc2Vfc3RkXG4gICAgWF9ub2lzeV90ZXN0ID0gdG9yY2guY2xhbXAoWF90Wzo4XSArIG5vaXNlLCAwLCAxKVxuICAgIFhfY2xlYW4gPSBtb2RlbChYX25vaXN5X3Rlc3QpXG5wcmludChmXHUwMDI3RGVub2lzaW5nIE1TRToge25uLk1TRUxvc3MoKShYX2NsZWFuLCBYX3RbOjhdKS5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkRlbm9pc2luZyBBRSBhbmQgU2NvcmUgTWF0Y2hpbmciLCJjb250ZW50IjoiVGhlIG9wdGltYWwgREFFIG91dHB1dCBzYXRpc2ZpZXMgRVt4IHwgeMyDXSDiiYggeMyDICsgz4PCsiDiiIJsb2cgcCh4zIMpL+KIgnjMgy4gVGhpcyBtZWFucyB0aGUgREFFIGltcGxpY2l0bHkgZXN0aW1hdGVzIHRoZSBzY29yZSBmdW5jdGlvbiBvZiB0aGUgZGF0YSBkaXN0cmlidXRpb24g4oCUIHRoZSBzYW1lIHF1YW50aXR5IHVzZWQgaW4gc2NvcmUtYmFzZWQgZ2VuZXJhdGl2ZSBtb2RlbHMgYW5kIGRpZmZ1c2lvbiBtb2RlbHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3BhcnNlIEF1dG9lbmNvZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHNwYXJzZSBhdXRvZW5jb2RlciB1c2VzIGFuIG92ZXJjb21wbGV0ZSByZXByZXNlbnRhdGlvbiAoZF96IFx1MDAzZSBkX3gpIGJ1dCBmb3JjZXMgc3BhcnNlIGFjdGl2YXRpb25zIHZpYSBhbiBMMSBwZW5hbHR5IG9yIGEgS0wgZGl2ZXJnZW5jZSBiZXR3ZWVuIHRoZSBhdmVyYWdlIGFjdGl2YXRpb24gYW5kIGEgdGFyZ2V0IHNwYXJzaXR5IM+BLiBVbmxpa2UgdW5kZXJjb21wbGV0ZSBBRXMsIHNwYXJzaXR5IChub3QgYm90dGxlbmVjayBzaXplKSBwcm92aWRlcyB0aGUgY29tcHJlc3Npb24gcHJlc3N1cmUuIFNwYXJzZSBmZWF0dXJlcyB0ZW5kIHRvIGJlIG1vcmUgaW50ZXJwcmV0YWJsZSBhbmQgZGlzZW50YW5nbGVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfZGlnaXRzXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgTWluTWF4U2NhbGVyXG5cblgsIHkgPSBsb2FkX2RpZ2l0cyhyZXR1cm5fWF95PVRydWUpXG5YID0gTWluTWF4U2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKS5hc3R5cGUobnAuZmxvYXQzMilcblhfdCA9IHRvcmNoLnRlbnNvcihYKVxuXG5jbGFzcyBTcGFyc2VBRShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbnB1dF9kaW09NjQsIGhpZGRlbl9kaW09MjU2KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgICMgT3ZlcmNvbXBsZXRlOiBoaWRkZW5fZGltIFx1MDAzZSBpbnB1dF9kaW1cbiAgICAgICAgc2VsZi5lbmNvZGVyID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoaW5wdXRfZGltLCBoaWRkZW5fZGltKSwgbm4uUmVMVSgpKVxuICAgICAgICBzZWxmLmRlY29kZXIgPSBubi5MaW5lYXIoaGlkZGVuX2RpbSwgaW5wdXRfZGltKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBoID0gc2VsZi5lbmNvZGVyKHgpXG4gICAgICAgIHJldHVybiBzZWxmLmRlY29kZXIoaCksIGhcblxubW9kZWwgPSBTcGFyc2VBRShoaWRkZW5fZGltPTI1Nilcbm9wdCA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0zKVxubGFtYmRhX2wxID0gMWUtNFxuXG5mb3IgZXBvY2ggaW4gcmFuZ2UoMzAwKTpcbiAgICB4X3JlY29uLCBoID0gbW9kZWwoWF90KVxuICAgIHJlY29uX2xvc3MgPSBubi5NU0VMb3NzKCkoeF9yZWNvbiwgWF90KVxuICAgIHNwYXJzZV9sb3NzID0gbGFtYmRhX2wxICogaC5hYnMoKS5tZWFuKCkgICMgTDEgc3BhcnNpdHkgb24gYWN0aXZhdGlvbnNcbiAgICBsb3NzID0gcmVjb25fbG9zcyArIHNwYXJzZV9sb3NzXG4gICAgb3B0Lnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcbiAgICBpZiBlcG9jaCAlIDEwMCA9PSAwOlxuICAgICAgICBhY3RpdmVfZnJhYyA9IChoLmRldGFjaCgpIFx1MDAzZSAwLjEpLmZsb2F0KCkubWVhbigpLml0ZW0oKVxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NofTogcmVjb249e3JlY29uX2xvc3M6LjRmfSwgYWN0aXZlPXthY3RpdmVfZnJhYzouMSV9XHUwMDI3KVxuXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBfLCBoID0gbW9kZWwoWF90KVxuICAgIHByaW50KGZcdTAwMjdBdmVyYWdlIGFjdGl2ZSB1bml0czogeyhoIFx1MDAzZSAwLjEpLmZsb2F0KCkubWVhbigpOi4xJX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udHJhY3RpdmUgQXV0b2VuY29kZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgY29udHJhY3RpdmUgYXV0b2VuY29kZXIgKENBRSkgcGVuYWxpc2VzIHRoZSBGcm9iZW5pdXMgbm9ybSBvZiB0aGUgZW5jb2RlciBKYWNvYmlhbiDigJbiiIJoL+KIgnjigJZfRsKyLiBUaGlzIGZvcmNlcyB0aGUgZW5jb2RlciB0byBiZSBpbnNlbnNpdGl2ZSB0byBzbWFsbCBwZXJ0dXJiYXRpb25zIG9mIHRoZSBpbnB1dCDigJQgdGhlIGxhdGVudCBjb2RlIGNoYW5nZXMgc2xvd2x5IGFzIHggbW92ZXMgc2xpZ2h0bHkuIEZvciBhIHNpZ21vaWQgZW5jb2RlciwgdGhlIEphY29iaWFuIHBlbmFsdHkgc2ltcGxpZmllcyB0byDOo+KxvCBoX2rCsigxLWhfainCsiDOo+G1oiBXX2ppwrIsIHdoaWNoIGlzIGNoZWFwIHRvIGNvbXB1dGUgYW5hbHl0aWNhbGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfZGlnaXRzXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgTWluTWF4U2NhbGVyXG5cblgsIHkgPSBsb2FkX2RpZ2l0cyhyZXR1cm5fWF95PVRydWUpXG5YID0gTWluTWF4U2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKS5hc3R5cGUobnAuZmxvYXQzMilcblhfdCA9IHRvcmNoLnRlbnNvcihYKVxuZF9pbiwgZF9oID0gNjQsIDMyXG5cbmNsYXNzIENvbnRyYWN0aXZlQUUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVuY19sYXllciA9IG5uLkxpbmVhcihkX2luLCBkX2gpXG4gICAgICAgIHNlbGYuZGVjID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoZF9oLCBkX2luKSwgbm4uU2lnbW9pZCgpKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBoID0gdG9yY2guc2lnbW9pZChzZWxmLmVuY19sYXllcih4KSlcbiAgICAgICAgcmV0dXJuIHNlbGYuZGVjKGgpLCBoXG5cbmRlZiBqYWNvYmlhbl9mcm9iKGgsIFcpOlxuICAgICMgQW5hbHl0aWMgRnJvYmVuaXVzIG5vcm0gZm9yIHNpZ21vaWQgZW5jb2RlclxuICAgIHMgPSBoICogKDEuMCAtIGgpICAgICAgICAgICAgICAgIyAobiwgZF9oKSDigJQgc2lnbW9pZCBkZXJpdmF0aXZlXG4gICAgcmV0dXJuIChzKioyIEAgKFcqKjIpLnN1bShkaW09MSkpLm1lYW4oKVxuXG5tb2RlbCA9IENvbnRyYWN0aXZlQUUoKVxub3B0ID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5sYW1iZGFfYyA9IDFlLTRcblxuZm9yIGVwb2NoIGluIHJhbmdlKDMwMCk6XG4gICAgeF9yZWNvbiwgaCA9IG1vZGVsKFhfdClcbiAgICByZWNvbiA9IG5uLk1TRUxvc3MoKSh4X3JlY29uLCBYX3QpXG4gICAgY29udHJhY3QgPSBsYW1iZGFfYyAqIGphY29iaWFuX2Zyb2IoaCwgbW9kZWwuZW5jX2xheWVyLndlaWdodClcbiAgICBsb3NzID0gcmVjb24gKyBjb250cmFjdFxuICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG4gICAgaWYgZXBvY2ggJSAxMDAgPT0gMDpcbiAgICAgICAgcHJpbnQoZlx1MDAyN0Vwb2NoIHtlcG9jaH06IHJlY29uPXtyZWNvbjouNGZ9LCBjb250cmFjdD17Y29udHJhY3Q6LjZmfVx1MDAyNylcbnByaW50KFx1MDAyN1RyYWluaW5nIGNvbXBsZXRlXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbmVhciBBRSA9IFBDQSwgYW5kIFZBRSBQcmV2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGxpbmVhciBhdXRvZW5jb2RlciB3aXRoIE1TRSBsb3NzIChubyBub25saW5lYXJpdGllcykgc3BhbnMgdGhlIHNhbWUgc3Vic3BhY2UgYXMgUENBOiB0aGUgbGVhcm5lZCBlbmNvZGVyIGRpcmVjdGlvbnMgYXJlIHRoZSB0b3AgayBlaWdlbnZlY3RvcnMgb2YgWOG1gFguIFRoZXkgbWF5IGJlIHJvdGF0ZWQgcmVsYXRpdmUgdG8gdGhlIHRydWUgUENzLCBidXQgdGhlIHN1YnNwYWNlIGlzIGlkZW50aWNhbC4gVGhlIFZBRSAoVmFyaWF0aW9uYWwgQXV0b2VuY29kZXIpIGV4dGVuZHMgdGhpcyBmcmFtZXdvcmsgcHJvYmFiaWxpc3RpY2FsbHk6IHRoZSBlbmNvZGVyIG91dHB1dHMgYSBkaXN0cmlidXRpb24gcSh6fHgpID0gTijOvCh4KSwgz4PCsih4KSkgYW5kIHRoZSBsb3NzIGFkZHMgYSBLTCB0ZXJtIHRvIGVuZm9yY2UgYSBzbW9vdGgsIGNvbnRpbnVvdXMgbGF0ZW50IHNwYWNlIOKAlCBlbmFibGluZyBnZW5lcmF0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVW5kZXJjb21wbGV0ZSBBRTogY29tcHJlc3Npb24gdmlhIGJvdHRsZW5lY2s7IGVxdWl2YWxlbnQgdG8gUENBIHdoZW4gbGluZWFyIiwiRGVub2lzaW5nIEFFOiBjb3JydXB0aW9uICsgcmVjb25zdHJ1Y3Rpb247IGxlYXJucyBkYXRhIG1hbmlmb2xkIGFuZCBzY29yZSBmdW5jdGlvbiIsIlNwYXJzZSBBRTogb3ZlcmNvbXBsZXRlICsgTDEgb3IgS0wgcGVuYWx0eTsgZGlzZW50YW5nbGVkLCBpbnRlcnByZXRhYmxlIGZlYXR1cmVzIiwiQ29udHJhY3RpdmUgQUU6IEphY29iaWFuIHBlbmFsdHk7IHN0YWJsZSBsYXRlbnQgY29kZSBpbnZhcmlhbnQgdG8gcGVydHVyYmF0aW9ucyIsIlZBRTogcHJvYmFiaWxpc3RpYyBlbmNvZGVyOyBjb250aW51b3VzLCBnZW5lcmF0aXZlIGxhdGVudCBzcGFjZSJdfSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmFyaWFudCIsIlJlZ3VsYXJpc2F0aW9uIiwiTGF0ZW50IFN0cnVjdHVyZSIsIkJlc3QgRm9yIl0sInJvd3MiOltbIlVuZGVyY29tcGxldGUiLCJCb3R0bGVuZWNrIHNpemUiLCJDb21wYWN0LCBkZW5zZSIsIkRpbWVuc2lvbmFsaXR5IHJlZHVjdGlvbiJdLFsiRGVub2lzaW5nIiwiSW5wdXQgY29ycnVwdGlvbiIsIk1hbmlmb2xkLWFsaWduZWQiLCJSb2J1c3QgZmVhdHVyZXMsIGltYWdlIHJlc3RvcmF0aW9uIl0sWyJTcGFyc2UiLCJMMSBvciBLTCBvbiBhY3RpdmF0aW9ucyIsIlNwYXJzZSwgb3ZlcmNvbXBsZXRlIiwiSW50ZXJwcmV0YWJsZSBmZWF0dXJlcywgZGljdGlvbmFyeSBsZWFybmluZyJdLFsiQ29udHJhY3RpdmUiLCJKYWNvYmlhbiBGcm9iZW5pdXMiLCJTbW9vdGgsIHN0YWJsZSIsIk5vaXNlLXJvYnVzdCByZXByZXNlbnRhdGlvbnMiXSxbIlZBRSIsIktMKHEoenx4KXx8cCh6KSkiLCJDb250aW51b3VzLCBnZW5lcmF0aXZlIiwiR2VuZXJhdGlvbiwgaW50ZXJwb2xhdGlvbiJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGwgYXV0b2VuY29kZXIgdmFyaWFudHMgc2hhcmUgdGhlIGVuY29kZXItZGVjb2RlciBza2VsZXRvbiBidXQgZGlmZmVyIGluIHdoYXQgdGhleSByZWd1bGFyaXNlLiBUaGUgY2hvaWNlIG9mIHJlZ3VsYXJpc2F0aW9uIGRldGVybWluZXMgdGhlIGdlb21ldHJ5IG9mIHRoZSBsYXRlbnQgc3BhY2U6IGEgYm90dGxlbmVjayBwcm9kdWNlcyBhIGNvbXBhY3Qgc3Vic3BhY2UgKGxpa2UgUENBKSwgY29ycnVwdGlvbiBwcmVzc3VyZSBwcm9kdWNlcyBhIG1hbmlmb2xkLWFsaWduZWQgY29kZSwgTDEgcGVuYWx0eSBwcm9kdWNlcyBhIHNwYXJzZSBkaWN0aW9uYXJ5LCBhbmQgSmFjb2JpYW4gcGVuYWx0eSBwcm9kdWNlcyBhIGZsYXQsIGxvY2FsbHktbGluZWFyIG1hcHBpbmcuIEVhY2ggcmVndWxhcmlzYXRpb24gc3RyYXRlZ3kgaXMgc3VpdGVkIHRvIGEgZGlmZmVyZW50IGRvd25zdHJlYW0gZ29hbC4ifSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkNob29zaW5nIGFuIEF1dG9lbmNvZGVyIFZhcmlhbnQiLCJjb250ZW50IjoiRm9yIGRpbWVuc2lvbmFsaXR5IHJlZHVjdGlvbiBjb21wYXJhYmxlIHRvIFBDQTogdW5kZXJjb21wbGV0ZSBBRS4gRm9yIGxlYXJuaW5nIHJlcHJlc2VudGF0aW9ucyB0aGF0IGdlbmVyYWxpc2UgdW5kZXIgbm9pc2U6IGRlbm9pc2luZyBBRS4gRm9yIGh1bWFuLWludGVycHJldGFibGUgZmVhdHVyZXM6IHNwYXJzZSBBRS4gRm9yIHNtb290aCBsYXRlbnQgc3BhY2VzIG5lZWRlZCBmb3IgaW50ZXJwb2xhdGlvbiBvciBnZW5lcmF0aW9uOiBWQUUuIEZvciBwcm9kdWN0aW9uIGZlYXR1cmUgZXh0cmFjdG9ycyB0aGF0IGFyZSBzdGFibGUgdW5kZXIgaW5wdXQgcGVydHVyYmF0aW9uczogY29udHJhY3RpdmUgQUUuIn1d"
---
# Autoencoders — Undercomplete, Denoising, Sparse, Contractive

An autoencoder is a neural network trained to reconstruct its input through a compressed bottleneck. The encoder f: X→Z maps input to a latent code, the decoder g: Z→X̂ maps back to input space, and training minimises the reconstruction loss ‖x - g(f(x))‖². Different regularisation strategies produce qualitatively different latent representations.

## Architecture and Reconstruction Loss

The simplest autoencoder uses a single bottleneck hidden layer: x → h (encoder) → x̂ (decoder), with MSE loss ‖x-x̂‖² for continuous inputs or binary cross-entropy for binary inputs. The bottleneck dimension d_z < d_x forces compression. The key insight: a linear autoencoder with MSE loss recovers exactly the PCA subspace — it finds the same directions of maximum variance.

## Undercomplete Autoencoder vs PCA

```python
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X, y = load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X).astype(np.float32)
X_t = torch.tensor(X)

class Autoencoder(nn.Module):
    def __init__(self, input_dim=64, latent_dim=2):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32), nn.ReLU(),
            nn.Linear(32, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32), nn.ReLU(),
            nn.Linear(32, input_dim)
        )
    def forward(self, x):
        return self.decoder(self.encoder(x))

model = Autoencoder(latent_dim=2)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
for epoch in range(300):
    loss = nn.MSELoss()(model(X_t), X_t)
    opt.zero_grad(); loss.backward(); opt.step()
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: loss={loss.item():.4f}')

with torch.no_grad():
    Z_ae = model.encoder(X_t).numpy()
Z_pca = PCA(n_components=2).fit_transform(X)
print(f'AE latent shape: {Z_ae.shape},  PCA shape: {Z_pca.shape}')
```

## Denoising Autoencoder

A denoising autoencoder (DAE) trains on corrupted inputs x̃ and reconstructs the clean x. The corruption can be Gaussian noise, masking (dropout), or salt-and-pepper noise. The key insight (Vincent et al. 2011): the DAE learns to estimate the gradient of the log data density ∂log p(x)/∂x — a score function. This forces the model to understand the data manifold rather than just memorising inputs.

```python
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.preprocessing import MinMaxScaler

X, y = load_digits(return_X_y=True)
X = MinMaxScaler().fit_transform(X).astype(np.float32)
X_t = torch.tensor(X)
noise_std = 0.3

class DenoisingAE(nn.Module):
    def __init__(self, dim=64):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(dim, 128), nn.ReLU(),
            nn.Linear(128, 32), nn.ReLU()
        )
        self.dec = nn.Sequential(
            nn.Linear(32, 128), nn.ReLU(),
            nn.Linear(128, dim), nn.Sigmoid()
        )
    def forward(self, x):
        return self.dec(self.enc(x))

model = DenoisingAE()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(300):
    noise = torch.randn_like(X_t) * noise_std
    X_noisy = torch.clamp(X_t + noise, 0.0, 1.0)  # corrupt
    X_recon = model(X_noisy)                        # reconstruct
    loss = nn.MSELoss()(X_recon, X_t)               # target: clean!
    opt.zero_grad(); loss.backward(); opt.step()
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: loss={loss.item():.4f}')

with torch.no_grad():
    noise = torch.randn_like(X_t[:8]) * noise_std
    X_noisy_test = torch.clamp(X_t[:8] + noise, 0, 1)
    X_clean = model(X_noisy_test)
print(f'Denoising MSE: {nn.MSELoss()(X_clean, X_t[:8]).item():.4f}')
```

> **Denoising AE and Score Matching**: The optimal DAE output satisfies E[x | x̃] ≈ x̃ + σ² ∂log p(x̃)/∂x̃. This means the DAE implicitly estimates the score function of the data distribution — the same quantity used in score-based generative models and diffusion models.

## Sparse Autoencoder

A sparse autoencoder uses an overcomplete representation (d_z > d_x) but forces sparse activations via an L1 penalty or a KL divergence between the average activation and a target sparsity ρ. Unlike undercomplete AEs, sparsity (not bottleneck size) provides the compression pressure. Sparse features tend to be more interpretable and disentangled.

```python
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.preprocessing import MinMaxScaler

X, y = load_digits(return_X_y=True)
X = MinMaxScaler().fit_transform(X).astype(np.float32)
X_t = torch.tensor(X)

class SparseAE(nn.Module):
    def __init__(self, input_dim=64, hidden_dim=256):
        super().__init__()
        # Overcomplete: hidden_dim > input_dim
        self.encoder = nn.Sequential(nn.Linear(input_dim, hidden_dim), nn.ReLU())
        self.decoder = nn.Linear(hidden_dim, input_dim)
    def forward(self, x):
        h = self.encoder(x)
        return self.decoder(h), h

model = SparseAE(hidden_dim=256)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
lambda_l1 = 1e-4

for epoch in range(300):
    x_recon, h = model(X_t)
    recon_loss = nn.MSELoss()(x_recon, X_t)
    sparse_loss = lambda_l1 * h.abs().mean()  # L1 sparsity on activations
    loss = recon_loss + sparse_loss
    opt.zero_grad(); loss.backward(); opt.step()
    if epoch % 100 == 0:
        active_frac = (h.detach() > 0.1).float().mean().item()
        print(f'Epoch {epoch}: recon={recon_loss:.4f}, active={active_frac:.1%}')

with torch.no_grad():
    _, h = model(X_t)
    print(f'Average active units: {(h > 0.1).float().mean():.1%}')
```

## Contractive Autoencoder

A contractive autoencoder (CAE) penalises the Frobenius norm of the encoder Jacobian ‖∂h/∂x‖_F². This forces the encoder to be insensitive to small perturbations of the input — the latent code changes slowly as x moves slightly. For a sigmoid encoder, the Jacobian penalty simplifies to Σⱼ h_j²(1-h_j)² Σᵢ W_ji², which is cheap to compute analytically.

```python
import numpy as np
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.preprocessing import MinMaxScaler

X, y = load_digits(return_X_y=True)
X = MinMaxScaler().fit_transform(X).astype(np.float32)
X_t = torch.tensor(X)
d_in, d_h = 64, 32

class ContractiveAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.enc_layer = nn.Linear(d_in, d_h)
        self.dec = nn.Sequential(nn.Linear(d_h, d_in), nn.Sigmoid())
    def forward(self, x):
        h = torch.sigmoid(self.enc_layer(x))
        return self.dec(h), h

def jacobian_frob(h, W):
    # Analytic Frobenius norm for sigmoid encoder
    s = h * (1.0 - h)               # (n, d_h) — sigmoid derivative
    return (s**2 @ (W**2).sum(dim=1)).mean()

model = ContractiveAE()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
lambda_c = 1e-4

for epoch in range(300):
    x_recon, h = model(X_t)
    recon = nn.MSELoss()(x_recon, X_t)
    contract = lambda_c * jacobian_frob(h, model.enc_layer.weight)
    loss = recon + contract
    opt.zero_grad(); loss.backward(); opt.step()
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: recon={recon:.4f}, contract={contract:.6f}')
print('Training complete')
```

## Linear AE = PCA, and VAE Preview

A linear autoencoder with MSE loss (no nonlinearities) spans the same subspace as PCA: the learned encoder directions are the top k eigenvectors of XᵀX. They may be rotated relative to the true PCs, but the subspace is identical. The VAE (Variational Autoencoder) extends this framework probabilistically: the encoder outputs a distribution q(z|x) = N(μ(x), σ²(x)) and the loss adds a KL term to enforce a smooth, continuous latent space — enabling generation.

- Undercomplete AE: compression via bottleneck; equivalent to PCA when linear
- Denoising AE: corruption + reconstruction; learns data manifold and score function
- Sparse AE: overcomplete + L1 or KL penalty; disentangled, interpretable features
- Contractive AE: Jacobian penalty; stable latent code invariant to perturbations
- VAE: probabilistic encoder; continuous, generative latent space

| Variant | Regularisation | Latent Structure | Best For |
| --- | --- | --- | --- |
| Undercomplete | Bottleneck size | Compact, dense | Dimensionality reduction |
| Denoising | Input corruption | Manifold-aligned | Robust features, image restoration |
| Sparse | L1 or KL on activations | Sparse, overcomplete | Interpretable features, dictionary learning |
| Contractive | Jacobian Frobenius | Smooth, stable | Noise-robust representations |
| VAE | KL(q(z|x)||p(z)) | Continuous, generative | Generation, interpolation |

All autoencoder variants share the encoder-decoder skeleton but differ in what they regularise. The choice of regularisation determines the geometry of the latent space: a bottleneck produces a compact subspace (like PCA), corruption pressure produces a manifold-aligned code, L1 penalty produces a sparse dictionary, and Jacobian penalty produces a flat, locally-linear mapping. Each regularisation strategy is suited to a different downstream goal.

---

> **Choosing an Autoencoder Variant**: For dimensionality reduction comparable to PCA: undercomplete AE. For learning representations that generalise under noise: denoising AE. For human-interpretable features: sparse AE. For smooth latent spaces needed for interpolation or generation: VAE. For production feature extractors that are stable under input perturbations: contractive AE.

