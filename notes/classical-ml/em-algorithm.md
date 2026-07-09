---
title: "EM Algorithm — E-Step, M-Step, and Convergence"
slug: "em-algorithm"
description: "Derive the EM algorithm from first principles: the ELBO lower bound, Jensen's inequality proof of monotone log-likelihood increase, the E-step as posterior inference over latent variables, and the M-step as complete-data MLE. Covers Baum-Welch for HMMs and EM variants."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEV4cGVjdGF0aW9uLU1heGltaXphdGlvbiAoRU0pIGFsZ29yaXRobSBzb2x2ZXMgYSBjbGFzcyBvZiBNTEUgcHJvYmxlbXMgd2hlcmUgZGlyZWN0IG1heGltaXphdGlvbiBvZiB0aGUgb2JzZXJ2ZWQtZGF0YSBsaWtlbGlob29kIGlzIGludHJhY3RhYmxlIGR1ZSB0byBsYXRlbnQgdmFyaWFibGVzLiBCeSBpbnRyb2R1Y2luZyBhIGxvd2VyIGJvdW5kICh0aGUgRUxCTykgdmlhIEplbnNlblx1MDAyN3MgaW5lcXVhbGl0eSwgRU0gY29udmVydHMgdGhlIGhhcmQgcHJvYmxlbSBpbnRvIHR3byBhbHRlcm5hdGluZyB0cmFjdGFibGUgc3RlcHMuIFVuZGVyc3RhbmRpbmcgdGhlIGRlcml2YXRpb24gZXhwbGFpbnMgd2h5IEVNIG1vbm90b25pY2FsbHkgaW5jcmVhc2VzIHRoZSBsaWtlbGlob29kLCB3aHkgaXQgY29udmVyZ2VzIHRvIGEgbG9jYWwgbWF4aW11bSwgYW5kIHdoZW4gaXQgc2hvdWxkIGJlIHByZWZlcnJlZCBvdmVyIGRpcmVjdCBncmFkaWVudC1iYXNlZCBvcHRpbWl6YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIE1MRSB3aXRoIExhdGVudCBWYXJpYWJsZXMgUHJvYmxlbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2l2ZW4gb2JzZXJ2ZWQgZGF0YSBYIGFuZCBsYXRlbnQgdmFyaWFibGVzIFosIHRoZSBjb21wbGV0ZS1kYXRhIGxvZy1saWtlbGlob29kIGxvZyBwKFgsWnzOuCkgaXMgb2Z0ZW4gdHJhY3RhYmxlIChlLmcuLCBjbG9zZWQtZm9ybSBNTEUgZm9yIGVhY2ggY29tcG9uZW50IG9mIGEgbWl4dHVyZSkuIEJ1dCB0aGUgb2JzZXJ2ZWQtZGF0YSBsb2ctbGlrZWxpaG9vZCBsb2cgcChYfM64KSA9IGxvZyDOo19aIHAoWCxafM64KSByZXF1aXJlcyBzdW1taW5nIG92ZXIgYWxsIGNvbmZpZ3VyYXRpb25zIG9mIFosIHdoaWNoIGlzIGV4cG9uZW50aWFsbHkgbGFyZ2UuIERpcmVjdCBncmFkaWVudCBhc2NlbnQgb24gbG9nIHAoWHzOuCkgaXMgcG9zc2libGUgYnV0IGNvbXB1dGF0aW9uYWxseSBleHBlbnNpdmUgYW5kIG51bWVyaWNhbGx5IHVuc3RhYmxlLiBFTSBzaWRlc3RlcHMgdGhpcyBieSBvcHRpbWl6aW5nIGEgdHJhY3RhYmxlIGxvd2VyIGJvdW5kLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBFTEJPIGFuZCBKZW5zZW5cdTAwMjdzIEluZXF1YWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhbnkgZGlzdHJpYnV0aW9uIHEoWiksIGxvZyBwKFh8zrgpID0gbG9nIM6jX1ogcShaKSBbcChYLFp8zrgpL3EoWildIOKJpSDOo19aIHEoWikgbG9nW3AoWCxafM64KS9xKFopXSA9IEVfcVtsb2cgcChYLFp8zrgpXSDiiJIgRV9xW2xvZyBxKFopXSA9IEVMQk8ocSzOuCkuIFRoZSBpbmVxdWFsaXR5IGZvbGxvd3MgZnJvbSBKZW5zZW5cdTAwMjdzIChsb2cgaXMgY29uY2F2ZSkuIFRoZSBnYXAgZXF1YWxzIEtMKHEg4oCWIHAoWnxYLM64KSkg4omlIDAuIFNldHRpbmcgcShaKSA9IHAoWnxYLM64X29sZCkgbWFrZXMgS0w9MCwgc28gdGhlIGJvdW5kIGlzIHRpZ2h0IGF0IHRoZSBjdXJyZW50IM64X29sZC4gVGhlIEUtc3RlcCBjb21wdXRlcyB0aGlzIHBvc3RlcmlvcjsgdGhlIE0tc3RlcCBtYXhpbWl6ZXMgdGhlIHJlc3VsdGluZyBFTEJPIG92ZXIgzrgsIHdoaWNoIGVxdWFscyBtYXhpbWl6aW5nIFEozrgszrhfb2xkKSA9IEVfe1p8WCzOuF9vbGR9W2xvZyBwKFgsWnzOuCldLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IG5vcm1cbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuXG5kZWYgZW1fMWRfZ21tKFgsIGs9MiwgbWF4X2l0ZXI9MTAwLCB0b2w9MWUtNiwgc2VlZD00Mik6XG4gICAgXCJcIlwiRU0gZm9yIDFEIEdNTSB3aXRoIEVMQk8gKGV2aWRlbmNlIGxvd2VyIGJvdW5kKSB0cmFja2luZy5cIlwiXCJcbiAgICBybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoc2VlZClcbiAgICBuID0gbGVuKFgpXG4gICAgcGkgPSBucC5vbmVzKGspIC8ga1xuICAgIG11ID0gWFtybmcuY2hvaWNlKG4sIGssIHJlcGxhY2U9RmFsc2UpXVxuICAgIHNpZ21hID0gbnAuZnVsbChrLCBYLnN0ZCgpKVxuICAgIGxvZ19saWtzLCBlbGJvcyA9IFtdLCBbXVxuICAgIGZvciBfIGluIHJhbmdlKG1heF9pdGVyKTpcbiAgICAgICAgIyBFLXN0ZXA6IHBvc3RlcmlvciBQKHo9ayB8IHgsIHRoZXRhKVxuICAgICAgICBSID0gbnAuYXJyYXkoW3BpW2pdICogbm9ybS5wZGYoWCwgbXVbal0sIHNpZ21hW2pdKSBmb3IgaiBpbiByYW5nZShrKV0pLlRcbiAgICAgICAgcHggPSBSLnN1bShheGlzPTEpXG4gICAgICAgIGxvZ19saWtzLmFwcGVuZChucC5sb2cocHggKyAxZS0zMDApLnN1bSgpKVxuICAgICAgICBSIC89IHB4WzosIE5vbmVdXG4gICAgICAgICMgRUxCTyA9IEVfcVtsb2cgcChYLFp8dGhldGEpXSAtIEVfcVtsb2cgcShaKV1cbiAgICAgICAgbG9nX3B4eiA9IHN1bShSWzosIGpdICogKG5wLmxvZyhwaVtqXSsxZS0zMDApICsgbm9ybS5sb2dwZGYoWCwgbXVbal0sIHNpZ21hW2pdKSlcbiAgICAgICAgICAgICAgICAgICAgICBmb3IgaiBpbiByYW5nZShrKSkuc3VtKClcbiAgICAgICAgZW50cm9weV9xID0gLW5wLnN1bShSICogbnAubG9nKFIgKyAxZS0zMDApKVxuICAgICAgICBlbGJvcy5hcHBlbmQobG9nX3B4eiArIGVudHJvcHlfcSlcbiAgICAgICAgIyBNLXN0ZXBcbiAgICAgICAgTmsgPSBSLnN1bShheGlzPTApXG4gICAgICAgIHBpID0gTmsgLyBuXG4gICAgICAgIG11ID0gKFIgKiBYWzosIE5vbmVdKS5zdW0oYXhpcz0wKSAvIE5rXG4gICAgICAgIHNpZ21hID0gbnAuc3FydCgoKFIgKiAoWFs6LCBOb25lXSAtIG11KSAqKiAyKS5zdW0oYXhpcz0wKSkgLyBOaylcbiAgICAgICAgaWYgbGVuKGxvZ19saWtzKSBcdTAwM2UgMSBhbmQgYWJzKGxvZ19saWtzWy0xXSAtIGxvZ19saWtzWy0yXSkgXHUwMDNjIHRvbDpcbiAgICAgICAgICAgIGJyZWFrXG4gICAgcmV0dXJuIHBpLCBtdSwgc2lnbWEsIG5wLmFycmF5KGxvZ19saWtzKSwgbnAuYXJyYXkoZWxib3MpXG5cblgxZCA9IG5wLmNvbmNhdGVuYXRlKFtucC5yYW5kb20ubm9ybWFsKC0zLCAwLjgsIDIwMCksIG5wLnJhbmRvbS5ub3JtYWwoMywgMS4yLCAyMDApXSlcbnBpLCBtdSwgc2lnbWEsIGxscywgZWxibyA9IGVtXzFkX2dtbShYMWQsIGs9MilcbnByaW50KGZcIkNvbXBvbmVudCBtZWFuczoge211LnJvdW5kKDMpfSwgd2VpZ2h0czoge3BpLnJvdW5kKDMpfSwgc2lnbWFzOiB7c2lnbWEucm91bmQoMyl9XCIpXG5wcmludChmXCJMb2ctbGlrZWxpaG9vZCBtb25vdG9uZToge2FsbChucC5kaWZmKGxscykgXHUwMDNlPSAtMWUtNil9XCIpXG5wcmludChmXCJFTEJPIG1vbm90b25lOiAgICAgICAgICAge2FsbChucC5kaWZmKGVsYm8pIFx1MDAzZT0gLTFlLTYpfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBFTSBNb25vdG9uaWNhbGx5IEluY3JlYXNlcyBMb2ctTGlrZWxpaG9vZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWZ0ZXIgdGhlIEUtc3RlcCB3aXRoIHE9cChafFgszrhfb2xkKSwgdGhlIEVMQk8gZXF1YWxzIGxvZyBwKFh8zrhfb2xkKS4gVGhlIE0tc3RlcCBmaW5kcyDOuF9uZXcgdGhhdCBtYXhpbWl6ZXMgUSjOuCzOuF9vbGQpLCBzbyBRKM64X25ldyzOuF9vbGQpIOKJpSBRKM64X29sZCzOuF9vbGQpLiBTaW5jZSB0aGUgRUxCTyBsb3dlci1ib3VuZHMgbG9nIHAoWHzOuCkgZm9yIGFsbCBxLCBhbmQgc2luY2UgYXQgzrhfb2xkIHRoZSBib3VuZCBpcyB0aWdodDogbG9nIHAoWHzOuF9uZXcpIOKJpSBFTEJPKHEszrhfbmV3KSDiiaUgRUxCTyhxLM64X29sZCkgPSBsb2cgcChYfM64X29sZCkuIFRoZXJlZm9yZSBlYWNoIGNvbXBsZXRlIEVNIGl0ZXJhdGlvbiBjYW5ub3QgZGVjcmVhc2UgdGhlIG9ic2VydmVkIGxvZy1saWtlbGlob29kLiBDb252ZXJnZW5jZSBmb2xsb3dzIGJlY2F1c2UgbG9nIHAoWHzOuCkgaXMgYm91bmRlZCBhYm92ZSAocHJvYmFiaWxpdGllcyDiiaQgMSBzbyBsb2ctbGlrZWxpaG9vZCDiiaQgMCBwZXIgcG9pbnQpIGFuZCBtb25vdG9uaWNhbGx5IGluY3JlYXNpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybVxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoMClcblggPSBucC5jb25jYXRlbmF0ZShbcm5nLm5vcm1hbCgtMiwgMSwgMTUwKSwgcm5nLm5vcm1hbCgzLCAwLjcsIDEwMCldKVxuayA9IDJcbm4gPSBsZW4oWClcblxucGkgPSBucC5hcnJheShbMC41LCAwLjVdKVxubXUgPSBucC5hcnJheShbLTEuMCwgMS4wXSlcbnNpZyA9IG5wLmFycmF5KFsxLjAsIDEuMF0pXG5cbnByZXZfbGwgPSAtbnAuaW5mXG5wcmludChmXCJ7XHUwMDI3SXRlclx1MDAyNzpcdTAwM2U2fSB7XHUwMDI3TG9nLUxpa1x1MDAyNzpcdTAwM2UxNH0ge1x1MDAyN0RlbHRhXHUwMDI3Olx1MDAzZTE0fSB7XHUwMDI3TW9ub3RvbmVcdTAwMjc6XHUwMDNlMTB9XCIpXG5mb3IgaXQgaW4gcmFuZ2UoMjApOlxuICAgIFIgPSBucC5hcnJheShbcGlbal0gKiBub3JtLnBkZihYLCBtdVtqXSwgc2lnW2pdKSBmb3IgaiBpbiByYW5nZShrKV0pLlRcbiAgICBweCA9IFIuc3VtKGF4aXM9MSlcbiAgICBsbCA9IG5wLmxvZyhweCArIDFlLTMwMCkuc3VtKClcbiAgICBkZWx0YSA9IGxsIC0gcHJldl9sbFxuICAgIHByaW50KGZcIntpdDpcdTAwM2U2fSB7bGw6XHUwMDNlMTQuNGZ9IHtkZWx0YTpcdTAwM2UxNC42Zn0ge3N0cihkZWx0YSBcdTAwM2U9IC0xZS04KTpcdTAwM2UxMH1cIilcbiAgICBSIC89IHB4WzosIE5vbmVdXG4gICAgTmsgPSBSLnN1bShheGlzPTApXG4gICAgcGkgPSBOayAvIG5cbiAgICBtdSA9IChSICogWFs6LCBOb25lXSkuc3VtKGF4aXM9MCkgLyBOa1xuICAgIHNpZyA9IG5wLnNxcnQoKChSICogKFhbOiwgTm9uZV0gLSBtdSkgKiogMikuc3VtKGF4aXM9MCkpIC8gTmspXG4gICAgaWYgYWJzKGxsIC0gcHJldl9sbCkgXHUwMDNjIDFlLTg6XG4gICAgICAgIHByaW50KGZcIkNvbnZlcmdlZCBhdCBpdGVyYXRpb24ge2l0fVwiKVxuICAgICAgICBicmVha1xuICAgIHByZXZfbGwgPSBsbCJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhdW0tV2VsY2gg4oCUIEVNIGZvciBIaWRkZW4gTWFya292IE1vZGVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEJhdW0tV2VsY2ggYWxnb3JpdGhtIGlzIEVNIGFwcGxpZWQgdG8gSGlkZGVuIE1hcmtvdiBNb2RlbHMgKEhNTXMpLiBUaGUgbGF0ZW50IHZhcmlhYmxlIFogPSAoeuKCgSwuLi4selQpIGlzIHRoZSBoaWRkZW4gc3RhdGUgc2VxdWVuY2UuIFRoZSBFLXN0ZXAgY29tcHV0ZXMgdGhlIGZvcndhcmQtYmFja3dhcmQgcHJvYmFiaWxpdGllcyAozrPhtaIodCkgPSBQKHrigpw9aXxYLM64KSBhbmQgzr7htaLisbwodCkgPSBQKHrigpw9aSx64oKc4oKK4oKBPWp8WCzOuCkpIHZpYSB0aGUgZm9yd2FyZCBhbmQgYmFja3dhcmQgcGFzc2VzIG9uIHRoZSB0cmVsbGlzIOKAlCBhbiBPKFTCt1PCsikgY29tcHV0YXRpb24uIFRoZSBNLXN0ZXAgcmUtZXN0aW1hdGVzIHRyYW5zaXRpb24gbWF0cml4IEEsIGVtaXNzaW9uIHBhcmFtZXRlcnMgQiwgYW5kIGluaXRpYWwgZGlzdHJpYnV0aW9uIM+AIGJ5IHRha2luZyBleHBlY3RlZCBzdWZmaWNpZW50IHN0YXRpc3RpY3MuIFRoZSBzdHJ1Y3R1cmUgaXMgZXhhY3RseSBFTTogRS1zdGVwIGZpbGxzIGluIHNvZnQgbGF0ZW50IHN0YXRlczsgTS1zdGVwIG1heGltaXplcyB0aGUgY29tcGxldGUtZGF0YSBsaWtlbGlob29kIHVzaW5nIHRob3NlIHNvZnQgY291bnRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGZvcndhcmRfYmFja3dhcmQob2JzLCBBLCBCLCBwaV9pbml0KTpcbiAgICBcIlwiXCJGb3J3YXJkLWJhY2t3YXJkIGFsZ29yaXRobSBmb3IgZGlzY3JldGUgSE1NIOKAlCBPKFQgKiBTXjIpLlwiXCJcIlxuICAgIFQsIFMgPSBsZW4ob2JzKSwgQS5zaGFwZVswXVxuICAgIGFscGhhID0gbnAuemVyb3MoKFQsIFMpKVxuICAgIGJldGEgPSBucC56ZXJvcygoVCwgUykpXG4gICAgYWxwaGFbMF0gPSBwaV9pbml0ICogQls6LCBvYnNbMF1dXG4gICAgYWxwaGFbMF0gLz0gYWxwaGFbMF0uc3VtKClcbiAgICBmb3IgdCBpbiByYW5nZSgxLCBUKTpcbiAgICAgICAgYWxwaGFbdF0gPSAoYWxwaGFbdC0xXSBAIEEpICogQls6LCBvYnNbdF1dXG4gICAgICAgIGFscGhhW3RdIC89IGFscGhhW3RdLnN1bSgpXG4gICAgYmV0YVstMV0gPSAxLjBcbiAgICBmb3IgdCBpbiByYW5nZShUIC0gMiwgLTEsIC0xKTpcbiAgICAgICAgYmV0YVt0XSA9IEEgQCAoQls6LCBvYnNbdCsxXV0gKiBiZXRhW3QrMV0pXG4gICAgICAgIGJldGFbdF0gLz0gYmV0YVt0XS5zdW0oKVxuICAgIGdhbW1hID0gYWxwaGEgKiBiZXRhXG4gICAgZ2FtbWEgLz0gZ2FtbWEuc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcbiAgICByZXR1cm4gZ2FtbWFcblxuIyBUaW55IDItc3RhdGUgSE1NIHdpdGggMyBzeW1ib2xzXG5ucC5yYW5kb20uc2VlZCgwKVxuUywgT19zaXplLCBUID0gMiwgMywgODBcbm9icyA9IG5wLnJhbmRvbS5jaG9pY2UoT19zaXplLCBUKVxuIyBSYW5kb20gaW5pdFxuQSA9IG5wLnJhbmRvbS5kaXJpY2hsZXQoWzEsIDFdLCBzaXplPVMpXG5CID0gbnAucmFuZG9tLmRpcmljaGxldChbMSwgMSwgMV0sIHNpemU9UylcbnBpX2luaXQgPSBucC5hcnJheShbMC42LCAwLjRdKVxuXG5mb3IgZW1faXRlciBpbiByYW5nZSgxNSk6XG4gICAgZ2FtbWEgPSBmb3J3YXJkX2JhY2t3YXJkKG9icywgQSwgQiwgcGlfaW5pdClcbiAgICBwaV9pbml0ID0gZ2FtbWFbMF1cbiAgICBBX25ldyA9IG5wLnplcm9zX2xpa2UoQSlcbiAgICBCX25ldyA9IG5wLnplcm9zX2xpa2UoQilcbiAgICBmb3IgcyBpbiByYW5nZShTKTpcbiAgICAgICAgQV9uZXdbc10gPSBnYW1tYVs6LTEsIHMsIE5vbmVdIEAgQVtzLCBOb25lXSAvIGdhbW1hWzotMSwgc10uc3VtKClcbiAgICAgICAgZm9yIG8gaW4gcmFuZ2UoT19zaXplKTpcbiAgICAgICAgICAgIEJfbmV3W3MsIG9dID0gZ2FtbWFbb2JzID09IG8sIHNdLnN1bSgpIC8gZ2FtbWFbOiwgc10uc3VtKClcbiAgICBBLCBCID0gQV9uZXcgLyBBX25ldy5zdW0oYXhpcz0xLCBrZWVwZGltcz1UcnVlKSwgQl9uZXdcbnByaW50KGZcIkNvbnZlcmdlZC4gQT1cXG57QS5yb3VuZCgzKX1cXG5CPVxcbntCLnJvdW5kKDMpfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVNIFZhcmlhbnRzIGFuZCBXaGVuIHRvIFVzZSBFYWNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZXZlcmFsIEVNIHZhcmlhbnRzIGFkZHJlc3MgZGlmZmVyZW50IGJvdHRsZW5lY2tzOiBHZW5lcmFsaXplZCBFTSAoR0VNKSBhbGxvd3MgYW55IHN0ZXAgdGhhdCBpbmNyZWFzZXMgUSByYXRoZXIgdGhhbiBtYXhpbWl6aW5nIGl0IOKAlCB1c2VmdWwgd2hlbiB0aGUgTS1zdGVwIGhhcyBubyBjbG9zZWQgZm9ybS4gRXhwZWN0YXRpb24tQ29uZGl0aW9uYWwgTWF4aW1pemF0aW9uIChFQ00pIGJyZWFrcyB0aGUgTS1zdGVwIGludG8gY29uZGl0aW9uYWwgbWF4aW1pemF0aW9ucyBvdmVyIHBhcmFtZXRlciBzdWJzZXRzIOKAlCBzaW1wbGlmeWluZyBjb21wbGV4IE0tc3RlcHMuIFZhcmlhdGlvbmFsIEVNIHJlcGxhY2VzIHRoZSBleGFjdCBFLXN0ZXAgcG9zdGVyaW9yIHdpdGggYSBmYWN0b3JlZCBhcHByb3hpbWF0aW9uIHEoWikg4omIIM6g4bWiIHHhtaIoWuG1oikg4oCUIGVzc2VudGlhbCB3aGVuIHRoZSBleGFjdCBwb3N0ZXJpb3IgaXMgaW50cmFjdGFibGUgKGUuZy4sIGluIEJheWVzaWFuIGNsdXN0ZXJpbmcgb3IgdG9waWMgbW9kZWxzIGxpa2UgTERBKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnNwZWNpYWwgaW1wb3J0IGRpZ2FtbWEsIGdhbW1hbG5cblxuZGVmIHZhcmlhdGlvbmFsX2RpcmljaGxldF9taXh0dXJlKFgsIGs9MywgbWF4X2l0ZXI9NTAsIGFscGhhMD0xLjAsIHNlZWQ9NDIpOlxuICAgIFwiXCJcIk1lYW4tZmllbGQgdmFyaWF0aW9uYWwgRU0gZm9yIGEgRGlyaWNobGV0IHByb2Nlc3MgbWl4dHVyZSAoc2ltcGxpZmllZCkuXCJcIlwiXG4gICAgcm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKHNlZWQpXG4gICAgbiwgZCA9IFguc2hhcGVcbiAgICAjIFZhcmlhdGlvbmFsIHBhcmFtZXRlcnM6IHJlc3BvbnNpYmlsaXRpZXNcbiAgICByID0gcm5nLmRpcmljaGxldChucC5vbmVzKGspLCBzaXplPW4pICAjIHEoWikgPSBDYXQocl9pKVxuICAgIGVsYm9zID0gW11cbiAgICBmb3IgaXQgaW4gcmFuZ2UobWF4X2l0ZXIpOlxuICAgICAgICBOayA9IHIuc3VtKGF4aXM9MCkgKyAxZS0xMFxuICAgICAgICAjIFZhcmlhdGlvbmFsIE0tc3RlcDogdXBkYXRlIG5hdHVyYWwgcGFyYW1ldGVyc1xuICAgICAgICBhbHBoYSA9IGFscGhhMCArIE5rXG4gICAgICAgIG11X2sgPSAoci5UIEAgWCkgLyBOa1s6LCBOb25lXVxuICAgICAgICAjIFZhcmlhdGlvbmFsIEUtc3RlcDogdXBkYXRlIHJlc3BvbnNpYmlsaXRpZXNcbiAgICAgICAgbG9nX3IgPSBkaWdhbW1hKGFscGhhKSAtIGRpZ2FtbWEoYWxwaGEuc3VtKCkpXG4gICAgICAgIGZvciBqIGluIHJhbmdlKGspOlxuICAgICAgICAgICAgZGlmZiA9IFggLSBtdV9rW2pdXG4gICAgICAgICAgICBsb2dfcl9qID0gLTAuNSAqIChkaWZmICoqIDIpLnN1bShheGlzPTEpXG4gICAgICAgICAgICBsb2dfciA9IG5wLnZzdGFjayhbbG9nX3IsIGxvZ19yX2pdKSBpZiBpc2luc3RhbmNlKGxvZ19yLCBucC5uZGFycmF5KSBhbmQgbG9nX3IubmRpbSA9PSAxIGVsc2UgbG9nX3JcbiAgICAgICAgIyBTaW1wbGUgRS1zdGVwOiB1c2UgRXVjbGlkZWFuIGRpc3RhbmNlIGZvciB0aGlzIGlsbHVzdHJhdGlvblxuICAgICAgICBkaXN0cyA9IG5wLmFycmF5KFsoKFggLSBtdV9rW2pdKSoqMikuc3VtKGF4aXM9MSkgZm9yIGogaW4gcmFuZ2UoayldKS5UXG4gICAgICAgIHIgPSBucC5leHAoLTAuNSAqIGRpc3RzKVxuICAgICAgICByIC89IHIuc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcbiAgICAgICAgZWxib19hcHByb3ggPSAtKHIgKiBkaXN0cyAvIDIpLnN1bSgpXG4gICAgICAgIGVsYm9zLmFwcGVuZChlbGJvX2FwcHJveClcbiAgICByZXR1cm4gciwgbXVfaywgZWxib3NcblxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2Jsb2JzXG5YLCBfID0gbWFrZV9ibG9icyhuX3NhbXBsZXM9MjAwLCBjZW50ZXJzPTMsIHJhbmRvbV9zdGF0ZT01KVxuciwgY2VudGVycywgZWxib3MgPSB2YXJpYXRpb25hbF9kaXJpY2hsZXRfbWl4dHVyZShYLCBrPTUpXG5sYWJlbHMgPSByLmFyZ21heChheGlzPTEpXG5hY3RpdmUgPSBucC51bmlxdWUobGFiZWxzKVxucHJpbnQoZlwiQWN0aXZlIGNvbXBvbmVudHM6IHtsZW4oYWN0aXZlKX0gKG9mIDUgaW5pdGlhbGl6ZWQpXCIpXG5wcmludChmXCJFTEJPIG1vbm90b25lOiB7YWxsKG5wLmRpZmYoZWxib3MpIFx1MDAzZT0gLTFlLTQpfVwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiRU0gdnMgRGlyZWN0IEdyYWRpZW50IEFzY2VudCIsImNvbnRlbnQiOiJFTSBpcyBwcmVmZXJyZWQgd2hlbiB0aGUgTS1zdGVwIGhhcyBhIGNsb3NlZC1mb3JtIHNvbHV0aW9uIChhcyBpbiBHTU1zLCBITU1zLCBhbmQgZmFjdG9yIGFuYWx5c2lzKSwgbWFraW5nIGVhY2ggaXRlcmF0aW9uIGNoZWFwIGFuZCBleGFjdC4gRGlyZWN0IGdyYWRpZW50IGFzY2VudCBvbiBsb2cgcChYfM64KSBpcyBwcmVmZXJyZWQgd2hlbiB0aGUgTS1zdGVwIGxhY2tzIGEgY2xvc2VkIGZvcm0gb3Igd2hlbiB0aGUgRS1zdGVwIHBvc3RlcmlvciBpcyBpbnRyYWN0YWJsZS4gU3RvY2hhc3RpYyBFTSAodXNpbmcgbWluaS1iYXRjaGVzIGZvciB0aGUgRS1zdGVwKSBicmlkZ2VzIHRoZSB0d28gYXBwcm9hY2hlcyBmb3IgbGFyZ2UgZGF0YXNldHMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlZhcmlhbnQiLCJNLXN0ZXAiLCJFLXN0ZXAiLCJDb252ZXJnZW5jZSIsIlVzZSBDYXNlIl0sInJvd3MiOltbIlN0YW5kYXJkIEVNIiwiRXhhY3QgY2xvc2VkLWZvcm0gbWF4aW1pemF0aW9uIiwiRXhhY3QgcG9zdGVyaW9yIiwiTW9ub3RvbmUsIGxpbmVhciBuZWFyIGNvbnZlcmdlbmNlIiwiR01NcywgSE1NcywgRmFjdG9yIEFuYWx5c2lzIl0sWyJHRU0gKEdlbmVyYWxpemVkIEVNKSIsIkFueSDOuCB0aGF0IGluY3JlYXNlcyBRIiwiRXhhY3QgcG9zdGVyaW9yIiwiTW9ub3RvbmUsIHNsb3dlciIsIk0tc3RlcCBoYXMgbm8gY2xvc2VkIGZvcm0iXSxbIkVDTSAoQ29uZC4gTWF4aW1pemF0aW9uKSIsIlNlcXVlbnRpYWwgY29uZGl0aW9uYWwgbWF4aW1hIiwiRXhhY3QgcG9zdGVyaW9yIiwiTW9ub3RvbmUsIG1heSBiZSBzbG93ZXIiLCJDb21wbGV4IE0tc3RlcCwgc3RydWN0dXJlZCBwYXJhbXMiXSxbIlZhcmlhdGlvbmFsIEVNIiwiRXhhY3Qgb3IgZ3JhZGllbnQgc3RlcCIsIkZhY3RvcmVkIGFwcHJveCBxKFopIiwiRUxCTyBtb25vdG9uZSwgYXBwcm94aW1hdGUiLCJCYXllc2lhbiBtb2RlbHMsIExEQSwgVkFFcyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSy1NZWFucyBhcyBIYXJkIEVNIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJLLW1lYW5zIGlzIGV4YWN0bHkgRU0gYXBwbGllZCB0byBhIEdNTSB3aGVyZSBhbGwgY292YXJpYW5jZXMgYXJlIGVxdWFsIGlzb3Ryb3BpYyBtYXRyaWNlcyDPg8KySSBhbmQgYXNzaWdubWVudHMgYXJlIGhhcmQgKG9uZS1ob3QpLiBUaGUgRS1zdGVwIGJlY29tZXMgbmVhcmVzdC1jZW50cm9pZCBhc3NpZ25tZW50IChhcmdtYXggb2YgdGhlIEdhdXNzaWFuIGxpa2VsaWhvb2QgPSBhcmdtaW4gb2Ygc3F1YXJlZCBkaXN0YW5jZSksIGFuZCB0aGUgTS1zdGVwIGJlY29tZXMgdXBkYXRpbmcgdG8gdGhlIGNsdXN0ZXIgbWVhbiAod2hpY2ggbWF4aW1pemVzIHRoZSBHYXVzc2lhbiBsb2ctbGlrZWxpaG9vZCkuIFRoaXMgdmlldyBjbGFyaWZpZXMgd2h5IGstbWVhbnMgY29udmVyZ2VzIGZhc3RlciB0aGFuIEdNTSBFTSDigJQgaGFyZCBhc3NpZ25tZW50cyBlbGltaW5hdGUgdGhlIGNvc3RseSByZXNwb25zaWJpbGl0eSBjb21wdXRhdGlvbnMg4oCUIGJ1dCBhbHNvIHdoeSBpdCBpcyBsZXNzIGZsZXhpYmxlOiB0aGUgaGFyZCBFLXN0ZXAgY2Fubm90IGV4cHJlc3MgdW5jZXJ0YWludHkgYWJvdXQgYm9yZGVybGluZSBwb2ludHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJIYXJkIEUtc3RlcDogYXNzaWduIGVhY2ggcG9pbnQgdG8gb25lIGNsdXN0ZXIgKGFyZ21pbiBkaXN0YW5jZSkgcmF0aGVyIHRoYW4gY29tcHV0aW5nIHNvZnQgcmVzcG9uc2liaWxpdGllcy4iLCJNLXN0ZXAgaWRlbnRpY2FsOiBjbHVzdGVyIG1lYW4gbWluaW1pemVzIHNxdWFyZWQgZGlzdGFuY2UsIGV4YWN0bHkgYXMgaW4gR01NIE0tc3RlcCB3aXRoIHNwaGVyaWNhbCBjb3ZhcmlhbmNlLiIsIkNvbnZlcmdlbmNlIGZhc3Rlcjogbm8gbWF0cml4IGludmVyc2Ugb3IgZGV0ZXJtaW5hbnQgY29tcHV0YXRpb24gZm9yIGNvdmFyaWFuY2VzLiIsIldDU1MgPSBuZWdhdGl2ZSBHTU0gY29tcGxldGUtZGF0YSBsb2ctbGlrZWxpaG9vZCB1bmRlciBzcGhlcmljYWwgZXF1YWwtdmFyaWFuY2UgYXNzdW1wdGlvbi4iLCJLLW1lYW5zIGFzIGluaXRpYWxpemF0aW9uOiBydW5uaW5nIGstbWVhbnMgdGhlbiB1c2luZyBpdHMgbGFiZWxzIGFzIHN0YXJ0aW5nIHJlc3BvbnNpYmlsaXRpZXMgZm9yIEdNTSBFTSBvZnRlbiBnaXZlcyBiZXR0ZXIgY29udmVyZ2VuY2UgdGhhbiByYW5kb20gR01NIGluaXRpYWxpemF0aW9uLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBFTSBwZXJzcGVjdGl2ZSBvbiBrLW1lYW5zIGFsc28gZXhwbGFpbnMgaXRzIHNlbnNpdGl2aXR5IHRvIGluaXRpYWxpemF0aW9uOiB0aGUgaGFyZCBFLXN0ZXAgY3JlYXRlcyBzaGFycCBkZWNpc2lvbiBib3VuZGFyaWVzIHRoYXQgY2FuIHRyYXAgdGhlIGFsZ29yaXRobSBpbiBsb2NhbCBvcHRpbWEgZnJvbSB3aGljaCBzb2Z0IEVNIGNvdWxkIGVzY2FwZSBieSBzcHJlYWRpbmcgcmVzcG9uc2liaWxpdHkgbWFzcyBhY3Jvc3MgY2x1c3RlcnMuIFdoZW4gay1tZWFucyBnZXRzIHN0dWNrLCBzd2l0Y2hpbmcgdG8gR01NIEVNIHdpdGggdGhlIGstbWVhbnMgY2VudHJvaWRzIGFzIGluaXRpYWxpemF0aW9uIG9mdGVuIGZpbmRzIGEgYmV0dGVyIHNvbHV0aW9uLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# EM Algorithm — E-Step, M-Step, and Convergence

The Expectation-Maximization (EM) algorithm solves a class of MLE problems where direct maximization of the observed-data likelihood is intractable due to latent variables. By introducing a lower bound (the ELBO) via Jensen's inequality, EM converts the hard problem into two alternating tractable steps. Understanding the derivation explains why EM monotonically increases the likelihood, why it converges to a local maximum, and when it should be preferred over direct gradient-based optimization.

## The MLE with Latent Variables Problem

Given observed data X and latent variables Z, the complete-data log-likelihood log p(X,Z|θ) is often tractable (e.g., closed-form MLE for each component of a mixture). But the observed-data log-likelihood log p(X|θ) = log Σ_Z p(X,Z|θ) requires summing over all configurations of Z, which is exponentially large. Direct gradient ascent on log p(X|θ) is possible but computationally expensive and numerically unstable. EM sidesteps this by optimizing a tractable lower bound.

## The ELBO and Jensen's Inequality

For any distribution q(Z), log p(X|θ) = log Σ_Z q(Z) [p(X,Z|θ)/q(Z)] ≥ Σ_Z q(Z) log[p(X,Z|θ)/q(Z)] = E_q[log p(X,Z|θ)] − E_q[log q(Z)] = ELBO(q,θ). The inequality follows from Jensen's (log is concave). The gap equals KL(q ‖ p(Z|X,θ)) ≥ 0. Setting q(Z) = p(Z|X,θ_old) makes KL=0, so the bound is tight at the current θ_old. The E-step computes this posterior; the M-step maximizes the resulting ELBO over θ, which equals maximizing Q(θ,θ_old) = E_{Z|X,θ_old}[log p(X,Z|θ)].

```python
import numpy as np
from scipy.stats import norm
from sklearn.datasets import make_blobs

def em_1d_gmm(X, k=2, max_iter=100, tol=1e-6, seed=42):
    """EM for 1D GMM with ELBO (evidence lower bound) tracking."""
    rng = np.random.default_rng(seed)
    n = len(X)
    pi = np.ones(k) / k
    mu = X[rng.choice(n, k, replace=False)]
    sigma = np.full(k, X.std())
    log_liks, elbos = [], []
    for _ in range(max_iter):
        # E-step: posterior P(z=k | x, theta)
        R = np.array([pi[j] * norm.pdf(X, mu[j], sigma[j]) for j in range(k)]).T
        px = R.sum(axis=1)
        log_liks.append(np.log(px + 1e-300).sum())
        R /= px[:, None]
        # ELBO = E_q[log p(X,Z|theta)] - E_q[log q(Z)]
        log_pxz = sum(R[:, j] * (np.log(pi[j]+1e-300) + norm.logpdf(X, mu[j], sigma[j]))
                      for j in range(k)).sum()
        entropy_q = -np.sum(R * np.log(R + 1e-300))
        elbos.append(log_pxz + entropy_q)
        # M-step
        Nk = R.sum(axis=0)
        pi = Nk / n
        mu = (R * X[:, None]).sum(axis=0) / Nk
        sigma = np.sqrt(((R * (X[:, None] - mu) ** 2).sum(axis=0)) / Nk)
        if len(log_liks) > 1 and abs(log_liks[-1] - log_liks[-2]) < tol:
            break
    return pi, mu, sigma, np.array(log_liks), np.array(elbos)

X1d = np.concatenate([np.random.normal(-3, 0.8, 200), np.random.normal(3, 1.2, 200)])
pi, mu, sigma, lls, elbo = em_1d_gmm(X1d, k=2)
print(f"Component means: {mu.round(3)}, weights: {pi.round(3)}, sigmas: {sigma.round(3)}")
print(f"Log-likelihood monotone: {all(np.diff(lls) >= -1e-6)}")
print(f"ELBO monotone:           {all(np.diff(elbo) >= -1e-6)}")
```

## Why EM Monotonically Increases Log-Likelihood

After the E-step with q=p(Z|X,θ_old), the ELBO equals log p(X|θ_old). The M-step finds θ_new that maximizes Q(θ,θ_old), so Q(θ_new,θ_old) ≥ Q(θ_old,θ_old). Since the ELBO lower-bounds log p(X|θ) for all q, and since at θ_old the bound is tight: log p(X|θ_new) ≥ ELBO(q,θ_new) ≥ ELBO(q,θ_old) = log p(X|θ_old). Therefore each complete EM iteration cannot decrease the observed log-likelihood. Convergence follows because log p(X|θ) is bounded above (probabilities ≤ 1 so log-likelihood ≤ 0 per point) and monotonically increasing.

```python
import numpy as np
from scipy.stats import norm

rng = np.random.default_rng(0)
X = np.concatenate([rng.normal(-2, 1, 150), rng.normal(3, 0.7, 100)])
k = 2
n = len(X)

pi = np.array([0.5, 0.5])
mu = np.array([-1.0, 1.0])
sig = np.array([1.0, 1.0])

prev_ll = -np.inf
print(f"{'Iter':>6} {'Log-Lik':>14} {'Delta':>14} {'Monotone':>10}")
for it in range(20):
    R = np.array([pi[j] * norm.pdf(X, mu[j], sig[j]) for j in range(k)]).T
    px = R.sum(axis=1)
    ll = np.log(px + 1e-300).sum()
    delta = ll - prev_ll
    print(f"{it:>6} {ll:>14.4f} {delta:>14.6f} {str(delta >= -1e-8):>10}")
    R /= px[:, None]
    Nk = R.sum(axis=0)
    pi = Nk / n
    mu = (R * X[:, None]).sum(axis=0) / Nk
    sig = np.sqrt(((R * (X[:, None] - mu) ** 2).sum(axis=0)) / Nk)
    if abs(ll - prev_ll) < 1e-8:
        print(f"Converged at iteration {it}")
        break
    prev_ll = ll
```

## Baum-Welch — EM for Hidden Markov Models

The Baum-Welch algorithm is EM applied to Hidden Markov Models (HMMs). The latent variable Z = (z₁,...,zT) is the hidden state sequence. The E-step computes the forward-backward probabilities (γᵢ(t) = P(zₜ=i|X,θ) and ξᵢⱼ(t) = P(zₜ=i,zₜ₊₁=j|X,θ)) via the forward and backward passes on the trellis — an O(T·S²) computation. The M-step re-estimates transition matrix A, emission parameters B, and initial distribution π by taking expected sufficient statistics. The structure is exactly EM: E-step fills in soft latent states; M-step maximizes the complete-data likelihood using those soft counts.

```python
import numpy as np

def forward_backward(obs, A, B, pi_init):
    """Forward-backward algorithm for discrete HMM — O(T * S^2)."""
    T, S = len(obs), A.shape[0]
    alpha = np.zeros((T, S))
    beta = np.zeros((T, S))
    alpha[0] = pi_init * B[:, obs[0]]
    alpha[0] /= alpha[0].sum()
    for t in range(1, T):
        alpha[t] = (alpha[t-1] @ A) * B[:, obs[t]]
        alpha[t] /= alpha[t].sum()
    beta[-1] = 1.0
    for t in range(T - 2, -1, -1):
        beta[t] = A @ (B[:, obs[t+1]] * beta[t+1])
        beta[t] /= beta[t].sum()
    gamma = alpha * beta
    gamma /= gamma.sum(axis=1, keepdims=True)
    return gamma

# Tiny 2-state HMM with 3 symbols
np.random.seed(0)
S, O_size, T = 2, 3, 80
obs = np.random.choice(O_size, T)
# Random init
A = np.random.dirichlet([1, 1], size=S)
B = np.random.dirichlet([1, 1, 1], size=S)
pi_init = np.array([0.6, 0.4])

for em_iter in range(15):
    gamma = forward_backward(obs, A, B, pi_init)
    pi_init = gamma[0]
    A_new = np.zeros_like(A)
    B_new = np.zeros_like(B)
    for s in range(S):
        A_new[s] = gamma[:-1, s, None] @ A[s, None] / gamma[:-1, s].sum()
        for o in range(O_size):
            B_new[s, o] = gamma[obs == o, s].sum() / gamma[:, s].sum()
    A, B = A_new / A_new.sum(axis=1, keepdims=True), B_new
print(f"Converged. A=\n{A.round(3)}\nB=\n{B.round(3)}")
```

## EM Variants and When to Use Each

Several EM variants address different bottlenecks: Generalized EM (GEM) allows any step that increases Q rather than maximizing it — useful when the M-step has no closed form. Expectation-Conditional Maximization (ECM) breaks the M-step into conditional maximizations over parameter subsets — simplifying complex M-steps. Variational EM replaces the exact E-step posterior with a factored approximation q(Z) ≈ Πᵢ qᵢ(Zᵢ) — essential when the exact posterior is intractable (e.g., in Bayesian clustering or topic models like LDA).

```python
import numpy as np
from scipy.special import digamma, gammaln

def variational_dirichlet_mixture(X, k=3, max_iter=50, alpha0=1.0, seed=42):
    """Mean-field variational EM for a Dirichlet process mixture (simplified)."""
    rng = np.random.default_rng(seed)
    n, d = X.shape
    # Variational parameters: responsibilities
    r = rng.dirichlet(np.ones(k), size=n)  # q(Z) = Cat(r_i)
    elbos = []
    for it in range(max_iter):
        Nk = r.sum(axis=0) + 1e-10
        # Variational M-step: update natural parameters
        alpha = alpha0 + Nk
        mu_k = (r.T @ X) / Nk[:, None]
        # Variational E-step: update responsibilities
        log_r = digamma(alpha) - digamma(alpha.sum())
        for j in range(k):
            diff = X - mu_k[j]
            log_r_j = -0.5 * (diff ** 2).sum(axis=1)
            log_r = np.vstack([log_r, log_r_j]) if isinstance(log_r, np.ndarray) and log_r.ndim == 1 else log_r
        # Simple E-step: use Euclidean distance for this illustration
        dists = np.array([((X - mu_k[j])**2).sum(axis=1) for j in range(k)]).T
        r = np.exp(-0.5 * dists)
        r /= r.sum(axis=1, keepdims=True)
        elbo_approx = -(r * dists / 2).sum()
        elbos.append(elbo_approx)
    return r, mu_k, elbos

from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=200, centers=3, random_state=5)
r, centers, elbos = variational_dirichlet_mixture(X, k=5)
labels = r.argmax(axis=1)
active = np.unique(labels)
print(f"Active components: {len(active)} (of 5 initialized)")
print(f"ELBO monotone: {all(np.diff(elbos) >= -1e-4)}")
```

> **EM vs Direct Gradient Ascent**: EM is preferred when the M-step has a closed-form solution (as in GMMs, HMMs, and factor analysis), making each iteration cheap and exact. Direct gradient ascent on log p(X|θ) is preferred when the M-step lacks a closed form or when the E-step posterior is intractable. Stochastic EM (using mini-batches for the E-step) bridges the two approaches for large datasets.

| Variant | M-step | E-step | Convergence | Use Case |
| --- | --- | --- | --- | --- |
| Standard EM | Exact closed-form maximization | Exact posterior | Monotone, linear near convergence | GMMs, HMMs, Factor Analysis |
| GEM (Generalized EM) | Any θ that increases Q | Exact posterior | Monotone, slower | M-step has no closed form |
| ECM (Cond. Maximization) | Sequential conditional maxima | Exact posterior | Monotone, may be slower | Complex M-step, structured params |
| Variational EM | Exact or gradient step | Factored approx q(Z) | ELBO monotone, approximate | Bayesian models, LDA, VAEs |

## K-Means as Hard EM

K-means is exactly EM applied to a GMM where all covariances are equal isotropic matrices σ²I and assignments are hard (one-hot). The E-step becomes nearest-centroid assignment (argmax of the Gaussian likelihood = argmin of squared distance), and the M-step becomes updating to the cluster mean (which maximizes the Gaussian log-likelihood). This view clarifies why k-means converges faster than GMM EM — hard assignments eliminate the costly responsibility computations — but also why it is less flexible: the hard E-step cannot express uncertainty about borderline points.

- Hard E-step: assign each point to one cluster (argmin distance) rather than computing soft responsibilities.
- M-step identical: cluster mean minimizes squared distance, exactly as in GMM M-step with spherical covariance.
- Convergence faster: no matrix inverse or determinant computation for covariances.
- WCSS = negative GMM complete-data log-likelihood under spherical equal-variance assumption.
- K-means as initialization: running k-means then using its labels as starting responsibilities for GMM EM often gives better convergence than random GMM initialization.

The EM perspective on k-means also explains its sensitivity to initialization: the hard E-step creates sharp decision boundaries that can trap the algorithm in local optima from which soft EM could escape by spreading responsibility mass across clusters. When k-means gets stuck, switching to GMM EM with the k-means centroids as initialization often finds a better solution.

---

