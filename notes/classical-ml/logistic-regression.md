---
title: "Logistic Regression"
slug: "logistic-regression"
description: "Derive logistic regression via Bernoulli MLE, implement gradient descent and Newton-Raphson (IRLS), interpret coefficients as log-odds ratios, calibrate probabilities with Platt scaling, and extend to multinomial via softmax."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9naXN0aWMgcmVncmVzc2lvbiBtb2RlbHMgdGhlIHByb2JhYmlsaXR5IG9mIGEgYmluYXJ5IG91dGNvbWUgYnkgcGFzc2luZyBhIGxpbmVhciBmdW5jdGlvbiB0aHJvdWdoIHRoZSBzaWdtb2lkOiBQKHk9MXx4KSA9IM+DKM644bWAeCkgPSAxLygxK2Vee+KIks644bWAeH0pLiBVbmxpa2UgbGluZWFyIHJlZ3Jlc3Npb24sIGl0IG91dHB1dHMgdmFsaWQgcHJvYmFiaWxpdGllcyBpbiBbMCwxXSBhbmQgaXRzIGRlY2lzaW9uIGJvdW5kYXJ5IGlzIGxpbmVhciBpbiBmZWF0dXJlIHNwYWNlLiBEZXNwaXRlIGl0cyBzaW1wbGljaXR5LCBsb2dpc3RpYyByZWdyZXNzaW9uIHJlbWFpbnMgb25lIG9mIHRoZSBtb3N0IHdpZGVseSBkZXBsb3llZCBjbGFzc2lmaWVycyBpbiBtZWRpY2luZSwgZmluYW5jZSwgYW5kIGluZHVzdHJ5IGJlY2F1c2UgaXRzIGNvZWZmaWNpZW50cyBhcmUgZGlyZWN0bHkgaW50ZXJwcmV0YWJsZSBhcyBsb2ctb2RkcyByYXRpb3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIFNpZ21vaWQgRnVuY3Rpb24gYW5kIExvZ2l0IExpbmsifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzaWdtb2lkIM+DKHopID0gMS8oMStlXnviiJJ6fSkgbWFwcyDihJ0g4oaSICgwLDEpIHdpdGggz4MoMCk9MC41IGFuZCBncmFkaWVudCDPg1x1MDAyNyh6KSA9IM+DKHopKDHiiJLPgyh6KSkuIFRoZSBsb2dpdCAobG9nLW9kZHMpIGlzIGl0cyBpbnZlcnNlOiBsb2dpdChwKSA9IGxvZyhwLygx4oiScCkpID0gzrjhtYB4LiBUaGlzIGlzIHRoZSBjYW5vbmljYWwgbGluayBmdW5jdGlvbiBmb3IgdGhlIEJlcm5vdWxsaSBHTE0uIFRoZSBvZGRzIHJhdGlvIFAoeT0xKS9QKHk9MCkgPSBlXnvOuOG1gHh9LCBzbyBlYWNoIHVuaXQgaW5jcmVhc2UgaW4gZmVhdHVyZSBqIG11bHRpcGxpZXMgdGhlIG9kZHMgYnkgZV57zrjisbx9LiBUaGUgZGVjaXNpb24gYm91bmRhcnkgUCh5PTF8eCkgPSAwLjUg4p+6IM644bWAeCA9IDAsIHdoaWNoIGlzIGEgaHlwZXJwbGFuZSBpbiBmZWF0dXJlIHNwYWNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1heGltdW0gTGlrZWxpaG9vZCBFc3RpbWF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBc3N1bWluZyB5X2kgfiBCZXJub3VsbGkoz4MozrjhtYB44bWiKSksIHRoZSBsb2ctbGlrZWxpaG9vZCBpcyDihJMozrgpID0gzqMgW3nhtaIgbG9nIM+DKM644bWAeOG1oikgKyAoMeKIknnhtaIpIGxvZygx4oiSz4MozrjhtYB44bWiKSldLiBUaGlzIGVxdWFscyB0aGUgbmVnYXRpdmUgY3Jvc3MtZW50cm9weSBsb3NzLiDihJMozrgpIGlzIGNvbmNhdmUgaW4gzrgsIHNvIGFueSBsb2NhbCBtYXhpbXVtIGlzIGdsb2JhbC4gVGhlIGdyYWRpZW50IGlzIOKIguKEky/iiILOuCA9IFjhtYAoeSDiiJIgxbcpIHdoZXJlIMW34bWiID0gz4MozrjhtYB44bWiKS4gVGhlcmUgaXMgbm8gY2xvc2VkIGZvcm0gZm9yIHRoZSBNTEUgYmVjYXVzZSDPgyBpcyBub25saW5lYXIg4oCUIGl0ZXJhdGl2ZSBtZXRob2RzIChncmFkaWVudCBhc2NlbnQsIE5ld3Rvbi1SYXBoc29uKSBhcmUgcmVxdWlyZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5cbmRlZiBzaWdtb2lkKHopOlxuICAgIHJldHVybiAxLjAgLyAoMS4wICsgbnAuZXhwKC1ucC5jbGlwKHosIC0yNTAsIDI1MCkpKVxuXG5kZWYgbG9naXN0aWNfZ2QoWCwgeSwgbHI9MC4xLCBuX2l0ZXI9MTAwMCwgdG9sPTFlLTYpOlxuICAgIG4sIHAgPSBYLnNoYXBlXG4gICAgWF9iID0gbnAuaHN0YWNrKFtucC5vbmVzKChuLCAxKSksIFhdKVxuICAgIHRoZXRhID0gbnAuemVyb3MoWF9iLnNoYXBlWzFdKVxuICAgIGZvciBpIGluIHJhbmdlKG5faXRlcik6XG4gICAgICAgIHlfaGF0ID0gc2lnbW9pZChYX2IgQCB0aGV0YSlcbiAgICAgICAgZ3JhZCA9IFhfYi5UIEAgKHkgLSB5X2hhdCkgICAgICMgZ3JhZGllbnQgb2YgbG9nLWxpa2VsaWhvb2RcbiAgICAgICAgdGhldGEgKz0gbHIgKiBncmFkXG4gICAgICAgIGlmIG5wLmxpbmFsZy5ub3JtKGdyYWQpIFx1MDAzYyB0b2w6XG4gICAgICAgICAgICBwcmludChmXHUwMDI3Q29udmVyZ2VkIGF0IGl0ZXJhdGlvbiB7aX1cdTAwMjcpXG4gICAgICAgICAgICBicmVha1xuICAgIHJldHVybiB0aGV0YVxuXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKG5fc2FtcGxlcz0zMDAsIG5fZmVhdHVyZXM9NCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9pbmZvcm1hdGl2ZT0zLCByYW5kb21fc3RhdGU9NDIpXG50aGV0YSA9IGxvZ2lzdGljX2dkKFgsIHksIGxyPTAuMDUsIG5faXRlcj0yMDAwKVxuXG5YX2IgPSBucC5oc3RhY2soW25wLm9uZXMoKGxlbihYKSwgMSkpLCBYXSlcbmFjYyA9ICgoc2lnbW9pZChYX2IgQCB0aGV0YSkgXHUwMDNlPSAwLjUpID09IHkpLm1lYW4oKVxucHJpbnQoZlx1MDAyN0ludGVyY2VwdDoge3RoZXRhWzBdOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3Q29lZmZpY2llbnRzOiB7bnAucm91bmQodGhldGFbMTpdLCA0KX1cdTAwMjcpXG5wcmludChmXHUwMDI3VHJhaW5pbmcgYWNjdXJhY3k6IHthY2M6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOZXd0b24tUmFwaHNvbiBhbmQgSVJMUyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmV3dG9uLVJhcGhzb24gdXBkYXRlcyDOuCB1c2luZyB0aGUgSGVzc2lhbjogzrgg4oaQIM64IOKIkiBI4oG7wrniiIfihJMuIEZvciBsb2dpc3RpYyByZWdyZXNzaW9uLCB0aGUgSGVzc2lhbiBpcyBIID0g4oiSWOG1gFdYIHdoZXJlIFcgPSBkaWFnKMW34bWiKDHiiJLFt+G1oikpIGlzIHRoZSB3ZWlnaHQgbWF0cml4LiBUaGlzIGlzIHRoZSBJdGVyYXRpdmVseSBSZXdlaWdodGVkIExlYXN0IFNxdWFyZXMgKElSTFMpIGFsZ29yaXRobTogYXQgZWFjaCBzdGVwLCBzb2x2ZSBhIHdlaWdodGVkIGxlYXN0LXNxdWFyZXMgcHJvYmxlbS4gTmV3dG9uLVJhcGhzb24gY29udmVyZ2VzIHF1YWRyYXRpY2FsbHkgbmVhciB0aGUgb3B0aW11bSAodHlwaWNhbGx5IDXigJMxMCBpdGVyYXRpb25zIHZzIGh1bmRyZWRzIGZvciBncmFkaWVudCBkZXNjZW50KSBidXQgcmVxdWlyZXMgTyhwwrMpIHBlciBzdGVwIGZvciB0aGUgbWF0cml4IGludmVyc2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBMb2dpc3RpY1JlZ3Jlc3Npb25cblxuZGVmIHNpZ21vaWQoeik6XG4gICAgcmV0dXJuIDEuMCAvICgxLjAgKyBucC5leHAoLW5wLmNsaXAoeiwgLTI1MCwgMjUwKSkpXG5cbmRlZiBpcmxzKFgsIHksIG5faXRlcj0yMCwgdG9sPTFlLTgpOlxuICAgIG4sIHAgPSBYLnNoYXBlXG4gICAgWF9iID0gbnAuaHN0YWNrKFtucC5vbmVzKChuLCAxKSksIFhdKVxuICAgIHRoZXRhID0gbnAuemVyb3MoWF9iLnNoYXBlWzFdKVxuICAgIGZvciBpIGluIHJhbmdlKG5faXRlcik6XG4gICAgICAgIHlfaGF0ID0gc2lnbW9pZChYX2IgQCB0aGV0YSlcbiAgICAgICAgVyA9IHlfaGF0ICogKDEgLSB5X2hhdCkgICAgICAgICAgICAgICAgICAjIEJlcm5vdWxsaSB3ZWlnaHRzXG4gICAgICAgIGdyYWQgPSBYX2IuVCBAICh5IC0geV9oYXQpICAgICAgICAgICAgICAgIyBncmFkaWVudFxuICAgICAgICBIID0gLShYX2IuVCAqIFcpIEAgWF9iICAgICAgICAgICAgICAgICAgICMgSGVzc2lhblxuICAgICAgICBzdGVwID0gbnAubGluYWxnLnNvbHZlKC1ILCBncmFkKSAgICAgICAgICAjIE5ld3RvbiBzdGVwXG4gICAgICAgIHRoZXRhICs9IHN0ZXBcbiAgICAgICAgaWYgbnAubGluYWxnLm5vcm0oZ3JhZCkgXHUwMDNjIHRvbDpcbiAgICAgICAgICAgIHByaW50KGZcdTAwMjdJUkxTIGNvbnZlcmdlZCBhdCBzdGVwIHtpKzF9XHUwMDI3KVxuICAgICAgICAgICAgYnJlYWtcbiAgICByZXR1cm4gdGhldGFcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihuX3NhbXBsZXM9MzAwLCBuX2ZlYXR1cmVzPTQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5faW5mb3JtYXRpdmU9MywgcmFuZG9tX3N0YXRlPTQyKVxudGhldGFfaXJscyA9IGlybHMoWCwgeSlcbmxyX3JlZiA9IExvZ2lzdGljUmVncmVzc2lvbihDPTFlNiwgc29sdmVyPVx1MDAyN2xiZmdzXHUwMDI3LCBtYXhfaXRlcj0xMDAwKS5maXQoWCwgeSlcbnByaW50KFx1MDAyN0lSTFMgY29lZnM6ICAgXHUwMDI3LCBucC5yb3VuZCh0aGV0YV9pcmxzWzE6XSwgNCkpXG5wcmludChcdTAwMjdza2xlYXJuIGNvZWZzOlx1MDAyNywgbnAucm91bmQobHJfcmVmLmNvZWZfWzBdLCA0KSlcbnByaW50KFx1MDAyN01heCBkaWZmOiB7Oi4yZX1cdTAwMjcuZm9ybWF0KG5wLmFicyh0aGV0YV9pcmxzWzE6XSAtIGxyX3JlZi5jb2VmX1swXSkubWF4KCkpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZWZmaWNpZW50IEludGVycHJldGF0aW9uIGFuZCBDb25maWRlbmNlIEludGVydmFscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvZWZmaWNpZW50IM644rG8IHJlcHJlc2VudHMgdGhlIGNoYW5nZSBpbiBsb2ctb2RkcyBwZXIgdW5pdCBpbmNyZWFzZSBpbiBmZWF0dXJlIGosIGhvbGRpbmcgYWxsIG90aGVycyBmaXhlZC4gVGhlIG9kZHMgcmF0aW8gZm9yIGZlYXR1cmUgaiBpcyBlXnvOuOKxvH06IGlmIM644rG8ID0gMC41LCBhIG9uZS11bml0IGluY3JlYXNlIG11bHRpcGxpZXMgdGhlIG9kZHMgb2YgdGhlIHBvc2l0aXZlIGNsYXNzIGJ5IGVeezAuNX0g4omIIDEuNjUuIEFwcHJveGltYXRlIDk1JSBjb25maWRlbmNlIGludGVydmFscyBmb3IgzrjisbwgdXNlIHRoZSBkaWFnb25hbCBvZiB0aGUgaW52ZXJzZSBGaXNoZXIgaW5mb3JtYXRpb24gbWF0cml4ICjiiJJIKeKBu8K5LCBnaXZpbmcgzrjisbwgwrEgMS45NiDDlyBTRV9qLCB3aGljaCBtYXBzIHRvIENJIG9uIHRoZSBvZGRzIHJhdGlvIGJ5IGV4cG9uZW50aWF0aW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9icmVhc3RfY2FuY2VyXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBMb2dpc3RpY1JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5kYXRhID0gbG9hZF9icmVhc3RfY2FuY2VyKClcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oZGF0YS5kYXRhWzosIDo2XSlcbnkgPSBkYXRhLnRhcmdldFxuZmVhdHVyZV9uYW1lcyA9IGRhdGEuZmVhdHVyZV9uYW1lc1s6Nl1cblxubHIgPSBMb2dpc3RpY1JlZ3Jlc3Npb24oQz0xLjAsIHNvbHZlcj1cdTAwMjdsYmZnc1x1MDAyNywgbWF4X2l0ZXI9MTAwMCkuZml0KFgsIHkpXG5jb2VmcyA9IGxyLmNvZWZfWzBdXG5cbiMgRmlzaGVyIGluZm9ybWF0aW9uLWJhc2VkIFNFc1xuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgTG9naXN0aWNSZWdyZXNzaW9uXG5YX2IgPSBucC5oc3RhY2soW25wLm9uZXMoKGxlbihYKSwgMSkpLCBYXSlcbnlfaGF0ID0gbHIucHJlZGljdF9wcm9iYShYKVs6LCAxXVxuVyA9IHlfaGF0ICogKDEgLSB5X2hhdClcbkhfaW52ID0gbnAubGluYWxnLmludigoWF9iLlQgKiBXKSBAIFhfYilcblNFcyA9IG5wLnNxcnQobnAuZGlhZyhIX2ludikpWzE6XSAgIyBza2lwIGludGVyY2VwdCBTRVxuXG5wcmludChmXHUwMDI3e1wiRmVhdHVyZVwiOlx1MDAzZTMwfSB7XCJDb2VmXCI6XHUwMDNlOH0ge1wiT1JcIjpcdTAwM2U4fSB7XCI5NSUgQ0lcIn1cdTAwMjcgKVxuZm9yIG5hbWUsIGNvZWYsIHNlIGluIHppcChmZWF0dXJlX25hbWVzLCBjb2VmcywgU0VzKTpcbiAgICBsbyA9IG5wLmV4cChjb2VmIC0gMS45NiAqIHNlKVxuICAgIGhpID0gbnAuZXhwKGNvZWYgKyAxLjk2ICogc2UpXG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lOlx1MDAzZTMwfSB7Y29lZjpcdTAwM2U4LjNmfSB7bnAuZXhwKGNvZWYpOlx1MDAzZTguM2Z9ICBbe2xvOi4zZn0sIHtoaTouM2Z9XVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDYWxpYnJhdGlvbiBhbmQgUGxhdHQgU2NhbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBtb2RlbCBpcyB3ZWxsLWNhbGlicmF0ZWQgaWYgYW1vbmcgYWxsIHByZWRpY3Rpb25zIMW3IOKJiCAwLjcsIHJvdWdobHkgNzAlIG9mIHRydWUgbGFiZWxzIGFyZSBwb3NpdGl2ZS4gUmVsaWFiaWxpdHkgZGlhZ3JhbXMgKGNhbGlicmF0aW9uIGN1cnZlcykgcGxvdCBtZWFuIHByZWRpY3RlZCBwcm9iYWJpbGl0eSBhZ2FpbnN0IG9ic2VydmVkIHBvc2l0aXZlIHJhdGUgYWNyb3NzIGJpbnMuIExvZ2lzdGljIHJlZ3Jlc3Npb24gaXMgZ2VuZXJhbGx5IHdlbGwtY2FsaWJyYXRlZCBmb3IgaW4tZGlzdHJpYnV0aW9uIGRhdGEuIFBsYXR0IHNjYWxpbmcgcG9zdC1ob2MgZml0cyBhIGxvZ2lzdGljIHJlZ3Jlc3Npb24gb24gdGhlIG1vZGVsXHUwMDI3cyByYXcgc2NvcmVzIHVzaW5nIGEgaGVsZC1vdXQgY2FsaWJyYXRpb24gc2V0LCBtYXBwaW5nIHVuY2FsaWJyYXRlZCBwcm9iYWJpbGl0aWVzIHRvIGNhbGlicmF0ZWQgb25lcy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkNhbGlicmF0aW9uIE1hdHRlcnMgaW4gUHJvZHVjdGlvbiIsImNvbnRlbnQiOiJFdmVuIGlmIGEgbW9kZWwgaGFzIGhpZ2ggQVVDLCBwb29ybHkgY2FsaWJyYXRlZCBwcm9iYWJpbGl0aWVzIGNhdXNlIGRvd25zdHJlYW0gZmFpbHVyZXM6IHJpc2sgc2NvcmVzLCBleHBlY3RlZC12YWx1ZSBkZWNpc2lvbnMsIGFuZCB0aHJlc2hvbGQgdHVuaW5nIGFsbCByZXF1aXJlIHJlbGlhYmxlIHByb2JhYmlsaXR5IGVzdGltYXRlcy4gQWx3YXlzIHBsb3QgYSByZWxpYWJpbGl0eSBkaWFncmFtIGJlZm9yZSBkZXBsb3lpbmcgYW55IHByb2JhYmlsaXR5LW91dHB1dHRpbmcgbW9kZWwuIFVzZSBpc290b25pYyByZWdyZXNzaW9uIChub25wYXJhbWV0cmljKSBvciBQbGF0dCBzY2FsaW5nIChwYXJhbWV0cmljKSB0byByZWNhbGlicmF0ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExvZ2lzdGljUmVncmVzc2lvblxuZnJvbSBza2xlYXJuLmNhbGlicmF0aW9uIGltcG9ydCBDYWxpYnJhdGVkQ2xhc3NpZmllckNWLCBjYWxpYnJhdGlvbl9jdXJ2ZVxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgU1ZDXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24obl9zYW1wbGVzPTIwMDAsIG5fZmVhdHVyZXM9MTAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5faW5mb3JtYXRpdmU9NSwgcmFuZG9tX3N0YXRlPTQyKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuNCwgcmFuZG9tX3N0YXRlPTQyKVxuXG4jIFVuY2FsaWJyYXRlZCBTVk0gKGRlY2lzaW9uLWZ1bmN0aW9uIHNjb3Jlcywgbm90IHByb2JhYmlsaXRpZXMpXG5zdm0gPSBTVkMoa2VybmVsPVx1MDAyN3JiZlx1MDAyNywgcHJvYmFiaWxpdHk9RmFsc2UpLmZpdChYX3RyLCB5X3RyKVxuXG4jIFBsYXR0IHNjYWxpbmcgdmlhIENhbGlicmF0ZWRDbGFzc2lmaWVyQ1ZcbnBsYXR0X3N2bSA9IENhbGlicmF0ZWRDbGFzc2lmaWVyQ1YoU1ZDKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcpLCBtZXRob2Q9XHUwMDI3c2lnbW9pZFx1MDAyNywgY3Y9NSlcbnBsYXR0X3N2bS5maXQoWF90ciwgeV90cilcblxubHJfY2FsID0gTG9naXN0aWNSZWdyZXNzaW9uKG1heF9pdGVyPTEwMDApLmZpdChYX3RyLCB5X3RyKVxuXG5mb3IgbmFtZSwgcHJvYmFfZm4gaW4gWyhcdTAwMjdMUiAocmVmZXJlbmNlKVx1MDAyNywgbHJfY2FsLnByZWRpY3RfcHJvYmEoWF90ZSlbOiwgMV0pLFxuICAgICAgICAgICAgICAgICAgICAgICAgKFx1MDAyN1NWTStQbGF0dFx1MDAyNywgcGxhdHRfc3ZtLnByZWRpY3RfcHJvYmEoWF90ZSlbOiwgMV0pXTpcbiAgICBmcmFjX3BvcywgbWVhbl9wcmVkID0gY2FsaWJyYXRpb25fY3VydmUoeV90ZSwgcHJvYmFfZm4sIG5fYmlucz0xMClcbiAgICBjYWxfZXJyID0gbnAubWVhbihucC5hYnMoZnJhY19wb3MgLSBtZWFuX3ByZWQpKVxuICAgIHByaW50KGZcdTAwMjd7bmFtZX06IG1lYW4gY2FsaWJyYXRpb24gZXJyb3IgPSB7Y2FsX2VycjouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik11bHRpbm9taWFsIExvZ2lzdGljIFJlZ3Jlc3Npb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBLIFx1MDAzZSAyIGNsYXNzZXMsIHRoZSBzb2Z0bWF4IGZ1bmN0aW9uIGdlbmVyYWxpc2VzIHRoZSBzaWdtb2lkOiBQKHk9a3x4KSA9IGVee8644oKW4bWAeH0gLyDOo+KxvCBlXnvOuOKxvOG1gHh9LiBPbmUgY2xhc3MgaXMgdHlwaWNhbGx5IGNob3NlbiBhcyB0aGUgcmVmZXJlbmNlIChpdHMgd2VpZ2h0cyBhcmUgemVybykgZm9yIGlkZW50aWZpYWJpbGl0eSwgcmVkdWNpbmcgdG8gS+KIkjEgaW5kZXBlbmRlbnQgc2V0cyBvZiBwYXJhbWV0ZXJzLiBUaGUgbG9nLWxpa2VsaWhvb2QgaXMgdGhlIG5lZ2F0aXZlIGNhdGVnb3JpY2FsIGNyb3NzLWVudHJvcHkuIEdyYWRpZW50IGFuZCBOZXd0b24gdXBkYXRlcyBleHRlbmQgYW5hbG9nb3VzbHkuIE11bHRpLWxhYmVsIGNsYXNzaWZpY2F0aW9uIChtdWx0aXBsZSBiaW5hcnkgbGFiZWxzIHNpbXVsdGFuZW91c2x5KSBpcyBzb2x2ZWQgYnkgSyBpbmRlcGVuZGVudCBiaW5hcnkgbG9naXN0aWMgbW9kZWxzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJMaW5rIEZ1bmN0aW9uIiwiRGlzdHJpYnV0aW9uIiwiUmFuZ2UiLCJVc2UgQ2FzZSJdLCJyb3dzIjpbWyJTaWdtb2lkOiAxLygxK2Veey16fSkiLCJCZXJub3VsbGkiLCIoMCwxKSIsIkJpbmFyeSBjbGFzc2lmaWNhdGlvbiJdLFsiU29mdG1heDogZV57emt9L86jZV57emp9IiwiQ2F0ZWdvcmljYWwvTXVsdGlub21pYWwiLCIoMCwxKSBzdW1taW5nIHRvIDEiLCJNdWx0aWNsYXNzIGNsYXNzaWZpY2F0aW9uIl0sWyJJZGVudGl0eTogeiIsIkdhdXNzaWFuIiwiKC3iiJ4sK+KInikiLCJSZWdyZXNzaW9uIChPTFMpIl0sWyJMb2c6IGVeeiAob3IgbG9nIGxpbmspIiwiUG9pc3NvbiIsIigwLCviiJ4pIiwiQ291bnQgZGF0YSwgUG9pc3NvbiByZWdyZXNzaW9uIl0sWyJQcm9iaXQ6IM6mKHopIiwiQmVybm91bGxpIiwiKDAsMSkiLCJCaW5hcnksIEdhdXNzaWFuIGxhdGVudCB2YXJpYWJsZSBpbnRlcnByZXRhdGlvbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVndWxhcmlzYXRpb24gaW4gTG9naXN0aWMgUmVncmVzc2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aG91dCByZWd1bGFyaXNhdGlvbiwgbG9naXN0aWMgcmVncmVzc2lvbiBjYW4gb3ZlcmZpdCAoZXNwZWNpYWxseSB3aXRoIG1hbnkgZmVhdHVyZXMgb3IgcGVyZmVjdGx5IHNlcGFyYWJsZSBkYXRhIOKAlCB0aGUgTUxFIGlzIHVuZGVmaW5lZCBmb3Igc2VwYXJhYmxlIGRhdGEgc2luY2UgbG9zcyBhcHByb2FjaGVzIHplcm8gb25seSBhdCDigJbOuOKAluKGkuKInikuIEwyIHJlZ3VsYXJpc2F0aW9uIChDPTEvzrsgaW4gc2tsZWFybikgYWRkcyDiiJLOu+KAls644oCWwrIgdG8gdGhlIGxvZy1saWtlbGlob29kLCBzaHJpbmtpbmcgYWxsIGNvZWZmaWNpZW50cy4gTDEgcmVndWxhcmlzYXRpb24gcHJvbW90ZXMgc3BhcnNpdHkg4oCUIHVzZWZ1bCBmb3IgZmVhdHVyZSBzZWxlY3Rpb24gd2l0aCBoaWdoLWRpbWVuc2lvbmFsIGRhdGEuIHNrbGVhcm4gdXNlcyB0aGUgXHUwMDI3c2FnYVx1MDAyNyBzb2x2ZXIgZm9yIGJvdGggTDEgYW5kIEVsYXN0aWNOZXQgcmVndWxhcmlzZWQgbG9naXN0aWMgcmVncmVzc2lvbiBhdCBzY2FsZS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkwyIChSaWRnZSwgZGVmYXVsdCk6IGFkZHMg4oiSzrvigJbOuOKAlsKyIHRlcm07IGFsbCBjb2VmZmljaWVudHMgc2hyaW5rIGJ1dCByZW1haW4gbm9uemVybzsgYWx3YXlzIGNvbnZlcmdlcy4iLCJMMSAoTGFzc28pOiBwcm9tb3RlcyBleGFjdCB6ZXJvczsgdXNlZnVsIGZvciBoaWdoLWRpbWVuc2lvbmFsIGRhdGEgd2l0aCBtYW55IGlycmVsZXZhbnQgZmVhdHVyZXMuIiwiRWxhc3RpY05ldDogTDErTDIgY29tYmluYXRpb247IGhhbmRsZXMgY29ycmVsYXRlZCBmZWF0dXJlcyBiZXR0ZXIgdGhhbiBwdXJlIEwxLiIsIlBlcmZlY3RseSBzZXBhcmFibGUgZGF0YTogTDIvTDEgcmVndWxhcmlzYXRpb24gaXMgcmVxdWlyZWQgdG8gcHJldmVudCBkaXZlcmdlbmNlIG9mIE1MRS4iLCJNdWx0aWNsYXNzOiB1c2UgXHUwMDI3bXVsdGlub21pYWxcdTAwMjcgd2l0aCBcdTAwMjdsYmZnc1x1MDAyNyBvciBcdTAwMjdzYWdhXHUwMDI3IHNvbHZlcjsgYXZvaWRzIG9uZS12cy1yZXN0IGFwcHJveGltYXRpb24uIiwiQ2FsaWJyYXRpb246IGxvZ2lzdGljIHJlZ3Jlc3Npb24gaXMgd2VsbC1jYWxpYnJhdGVkIGJ5IGRlZmF1bHQ7IFNWTXMgYW5kIHRyZWUgbW9kZWxzIHR5cGljYWxseSBuZWVkIFBsYXR0IHNjYWxpbmcuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Logistic Regression

Logistic regression models the probability of a binary outcome by passing a linear function through the sigmoid: P(y=1|x) = σ(θᵀx) = 1/(1+e^{−θᵀx}). Unlike linear regression, it outputs valid probabilities in [0,1] and its decision boundary is linear in feature space. Despite its simplicity, logistic regression remains one of the most widely deployed classifiers in medicine, finance, and industry because its coefficients are directly interpretable as log-odds ratios.

## The Sigmoid Function and Logit Link

The sigmoid σ(z) = 1/(1+e^{−z}) maps ℝ → (0,1) with σ(0)=0.5 and gradient σ'(z) = σ(z)(1−σ(z)). The logit (log-odds) is its inverse: logit(p) = log(p/(1−p)) = θᵀx. This is the canonical link function for the Bernoulli GLM. The odds ratio P(y=1)/P(y=0) = e^{θᵀx}, so each unit increase in feature j multiplies the odds by e^{θⱼ}. The decision boundary P(y=1|x) = 0.5 ⟺ θᵀx = 0, which is a hyperplane in feature space.

## Maximum Likelihood Estimation

Assuming y_i ~ Bernoulli(σ(θᵀxᵢ)), the log-likelihood is ℓ(θ) = Σ [yᵢ log σ(θᵀxᵢ) + (1−yᵢ) log(1−σ(θᵀxᵢ))]. This equals the negative cross-entropy loss. ℓ(θ) is concave in θ, so any local maximum is global. The gradient is ∂ℓ/∂θ = Xᵀ(y − ŷ) where ŷᵢ = σ(θᵀxᵢ). There is no closed form for the MLE because σ is nonlinear — iterative methods (gradient ascent, Newton-Raphson) are required.

```python
import numpy as np
from sklearn.datasets import make_classification

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -250, 250)))

def logistic_gd(X, y, lr=0.1, n_iter=1000, tol=1e-6):
    n, p = X.shape
    X_b = np.hstack([np.ones((n, 1)), X])
    theta = np.zeros(X_b.shape[1])
    for i in range(n_iter):
        y_hat = sigmoid(X_b @ theta)
        grad = X_b.T @ (y - y_hat)     # gradient of log-likelihood
        theta += lr * grad
        if np.linalg.norm(grad) < tol:
            print(f'Converged at iteration {i}')
            break
    return theta

np.random.seed(42)
X, y = make_classification(n_samples=300, n_features=4,
                             n_informative=3, random_state=42)
theta = logistic_gd(X, y, lr=0.05, n_iter=2000)

X_b = np.hstack([np.ones((len(X), 1)), X])
acc = ((sigmoid(X_b @ theta) >= 0.5) == y).mean()
print(f'Intercept: {theta[0]:.4f}')
print(f'Coefficients: {np.round(theta[1:], 4)}')
print(f'Training accuracy: {acc:.4f}')
```

## Newton-Raphson and IRLS

Newton-Raphson updates θ using the Hessian: θ ← θ − H⁻¹∇ℓ. For logistic regression, the Hessian is H = −XᵀWX where W = diag(ŷᵢ(1−ŷᵢ)) is the weight matrix. This is the Iteratively Reweighted Least Squares (IRLS) algorithm: at each step, solve a weighted least-squares problem. Newton-Raphson converges quadratically near the optimum (typically 5–10 iterations vs hundreds for gradient descent) but requires O(p³) per step for the matrix inverse.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -250, 250)))

def irls(X, y, n_iter=20, tol=1e-8):
    n, p = X.shape
    X_b = np.hstack([np.ones((n, 1)), X])
    theta = np.zeros(X_b.shape[1])
    for i in range(n_iter):
        y_hat = sigmoid(X_b @ theta)
        W = y_hat * (1 - y_hat)                  # Bernoulli weights
        grad = X_b.T @ (y - y_hat)               # gradient
        H = -(X_b.T * W) @ X_b                   # Hessian
        step = np.linalg.solve(-H, grad)          # Newton step
        theta += step
        if np.linalg.norm(grad) < tol:
            print(f'IRLS converged at step {i+1}')
            break
    return theta

np.random.seed(42)
X, y = make_classification(n_samples=300, n_features=4,
                             n_informative=3, random_state=42)
theta_irls = irls(X, y)
lr_ref = LogisticRegression(C=1e6, solver='lbfgs', max_iter=1000).fit(X, y)
print('IRLS coefs:   ', np.round(theta_irls[1:], 4))
print('sklearn coefs:', np.round(lr_ref.coef_[0], 4))
print('Max diff: {:.2e}'.format(np.abs(theta_irls[1:] - lr_ref.coef_[0]).max()))
```

## Coefficient Interpretation and Confidence Intervals

The coefficient θⱼ represents the change in log-odds per unit increase in feature j, holding all others fixed. The odds ratio for feature j is e^{θⱼ}: if θⱼ = 0.5, a one-unit increase multiplies the odds of the positive class by e^{0.5} ≈ 1.65. Approximate 95% confidence intervals for θⱼ use the diagonal of the inverse Fisher information matrix (−H)⁻¹, giving θⱼ ± 1.96 × SE_j, which maps to CI on the odds ratio by exponentiating.

```python
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X = StandardScaler().fit_transform(data.data[:, :6])
y = data.target
feature_names = data.feature_names[:6]

lr = LogisticRegression(C=1.0, solver='lbfgs', max_iter=1000).fit(X, y)
coefs = lr.coef_[0]

# Fisher information-based SEs
from sklearn.linear_model import LogisticRegression
X_b = np.hstack([np.ones((len(X), 1)), X])
y_hat = lr.predict_proba(X)[:, 1]
W = y_hat * (1 - y_hat)
H_inv = np.linalg.inv((X_b.T * W) @ X_b)
SEs = np.sqrt(np.diag(H_inv))[1:]  # skip intercept SE

print(f'{"Feature":>30} {"Coef":>8} {"OR":>8} {"95% CI"}' )
for name, coef, se in zip(feature_names, coefs, SEs):
    lo = np.exp(coef - 1.96 * se)
    hi = np.exp(coef + 1.96 * se)
    print(f'{name:>30} {coef:>8.3f} {np.exp(coef):>8.3f}  [{lo:.3f}, {hi:.3f}]')
```

## Calibration and Platt Scaling

A model is well-calibrated if among all predictions ŷ ≈ 0.7, roughly 70% of true labels are positive. Reliability diagrams (calibration curves) plot mean predicted probability against observed positive rate across bins. Logistic regression is generally well-calibrated for in-distribution data. Platt scaling post-hoc fits a logistic regression on the model's raw scores using a held-out calibration set, mapping uncalibrated probabilities to calibrated ones.

> **Calibration Matters in Production**: Even if a model has high AUC, poorly calibrated probabilities cause downstream failures: risk scores, expected-value decisions, and threshold tuning all require reliable probability estimates. Always plot a reliability diagram before deploying any probability-outputting model. Use isotonic regression (nonparametric) or Platt scaling (parametric) to recalibrate.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

np.random.seed(42)
X, y = make_classification(n_samples=2000, n_features=10,
                             n_informative=5, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.4, random_state=42)

# Uncalibrated SVM (decision-function scores, not probabilities)
svm = SVC(kernel='rbf', probability=False).fit(X_tr, y_tr)

# Platt scaling via CalibratedClassifierCV
platt_svm = CalibratedClassifierCV(SVC(kernel='rbf'), method='sigmoid', cv=5)
platt_svm.fit(X_tr, y_tr)

lr_cal = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)

for name, proba_fn in [('LR (reference)', lr_cal.predict_proba(X_te)[:, 1]),
                        ('SVM+Platt', platt_svm.predict_proba(X_te)[:, 1])]:
    frac_pos, mean_pred = calibration_curve(y_te, proba_fn, n_bins=10)
    cal_err = np.mean(np.abs(frac_pos - mean_pred))
    print(f'{name}: mean calibration error = {cal_err:.4f}')
```

## Multinomial Logistic Regression

For K > 2 classes, the softmax function generalises the sigmoid: P(y=k|x) = e^{θₖᵀx} / Σⱼ e^{θⱼᵀx}. One class is typically chosen as the reference (its weights are zero) for identifiability, reducing to K−1 independent sets of parameters. The log-likelihood is the negative categorical cross-entropy. Gradient and Newton updates extend analogously. Multi-label classification (multiple binary labels simultaneously) is solved by K independent binary logistic models.

| Link Function | Distribution | Range | Use Case |
| --- | --- | --- | --- |
| Sigmoid: 1/(1+e^{-z}) | Bernoulli | (0,1) | Binary classification |
| Softmax: e^{zk}/Σe^{zj} | Categorical/Multinomial | (0,1) summing to 1 | Multiclass classification |
| Identity: z | Gaussian | (-∞,+∞) | Regression (OLS) |
| Log: e^z (or log link) | Poisson | (0,+∞) | Count data, Poisson regression |
| Probit: Φ(z) | Bernoulli | (0,1) | Binary, Gaussian latent variable interpretation |

## Regularisation in Logistic Regression

Without regularisation, logistic regression can overfit (especially with many features or perfectly separable data — the MLE is undefined for separable data since loss approaches zero only at ‖θ‖→∞). L2 regularisation (C=1/λ in sklearn) adds −λ‖θ‖² to the log-likelihood, shrinking all coefficients. L1 regularisation promotes sparsity — useful for feature selection with high-dimensional data. sklearn uses the 'saga' solver for both L1 and ElasticNet regularised logistic regression at scale.

- L2 (Ridge, default): adds −λ‖θ‖² term; all coefficients shrink but remain nonzero; always converges.
- L1 (Lasso): promotes exact zeros; useful for high-dimensional data with many irrelevant features.
- ElasticNet: L1+L2 combination; handles correlated features better than pure L1.
- Perfectly separable data: L2/L1 regularisation is required to prevent divergence of MLE.
- Multiclass: use 'multinomial' with 'lbfgs' or 'saga' solver; avoids one-vs-rest approximation.
- Calibration: logistic regression is well-calibrated by default; SVMs and tree models typically need Platt scaling.

---

