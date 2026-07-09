---
title: "Multi-Step Forecasting — Direct, Recursive, and MIMO"
slug: "multi-step-forecasting"
description: "Compare recursive (iterated one-step), direct (separate model per horizon), and MIMO (single model, all horizons) strategies for multi-step time-series forecasting, with analysis of error accumulation and horizon-accuracy trade-offs."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGktc3RlcCBmb3JlY2FzdGluZyByZXF1aXJlcyBwcm9kdWNpbmcgcHJlZGljdGlvbnMgZm9yIGhvcml6b25zIGg9MSwgMiwgLi4uLCBIIHJhdGhlciB0aGFuIGp1c3QgdGhlIG5leHQgc3RlcC4gVGhyZWUgbWFpbiBzdHJhdGVnaWVzIGV4aXN0OiByZWN1cnNpdmUgKHRyYWluIG9uZS1zdGVwIG1vZGVsLCBmZWVkIHByZWRpY3Rpb25zIGFzIGlucHV0cyBpdGVyYXRpdmVseSksIGRpcmVjdCAodHJhaW4gb25lIHNlcGFyYXRlIG1vZGVsIHBlciBob3Jpem9uKSwgYW5kIE1JTU8gKE11bHRpcGxlIElucHV0IE11bHRpcGxlIE91dHB1dCDigJQgdHJhaW4gb25lIG1vZGVsIHRoYXQgb3V0cHV0cyBhbGwgSCBob3Jpem9ucyBzaW11bHRhbmVvdXNseSkuIEVhY2ggc3RyYXRlZ3kgaGFzIGRpc3RpbmN0IGJpYXMtdmFyaWFuY2UgcHJvcGVydGllcywgYW5kIHRoZSBiZXN0IGNob2ljZSBkZXBlbmRzIG9uIHRoZSBmb3JlY2FzdCBob3Jpem9uLCBtb2RlbCBtaXNzcGVjaWZpY2F0aW9uLCBhbmQgdGhlIGludGVyLWhvcml6b24gZGVwZW5kZW5jeSBzdHJ1Y3R1cmUgb2YgdGhlIHRhcmdldCBzZXJpZXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJSZWN1cnNpdmU6IDEgbW9kZWwsIGVycm9yIGFjY3VtdWxhdGVzIGFjcm9zcyBob3Jpem9ucywgYmVzdCBmb3IgaCDiiaQgNS4iLCJEaXJlY3Q6IEggbW9kZWxzIChvbmUgcGVyIGhvcml6b24pLCBubyBlcnJvciBhY2N1bXVsYXRpb24sIGJlc3QgZm9yIGxvbmcgaG9yaXpvbnMgd2l0aCBtaXNzcGVjaWZpZWQgbW9kZWxzLiIsIk1JTU86IDEgbW9kZWwgb3V0cHV0dGluZyBhbGwgSCBob3Jpem9ucywgY2FwdHVyZXMgaW50ZXItaG9yaXpvbiBkZXBlbmRlbmNpZXMsIG5hdHVyYWwgZm9yIG5ldXJhbCBuZXRzLiIsIkRJUk1POiBHIG1vZGVscyAob25lIHBlciBncm91cCBvZiBob3Jpem9ucyksIGh5YnJpZCBiZXR3ZWVuIERpcmVjdCBhbmQgTUlNTy4iLCJBbHdheXMgZXZhbHVhdGUgUk1TRSBhdCBlYWNoIGluZGl2aWR1YWwgaG9yaXpvbiBoLCBub3QganVzdCB0aGUgYXZlcmFnZSDigJQgcHJvZmlsZXMgZGlmZmVyIGJ5IHN0cmF0ZWd5LiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZWN1cnNpdmUgKEl0ZXJhdGVkIE9uZS1TdGVwKSBGb3JlY2FzdGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVjdXJzaXZlIHN0cmF0ZWd5OiB0cmFpbiBhIG9uZS1zdGVwIG1vZGVsIMW34oKc4oKK4oKBID0gZih54oKcLCB54oKc4oKL4oKBLCAuLi4sIHnigpzigovigpopLiBBdCB0ZXN0IHRpbWUsIHRvIGZvcmVjYXN0IGggc3RlcHMgYWhlYWQsIGZlZWQgdGhlIHByZWRpY3RlZCDFt+KCnOKCiuKCgSBhcyBhbiBpbnB1dCB0byBwcm9kdWNlIMW34oKc4oKK4oKCLCBhbmQgc28gb24gaXRlcmF0aXZlbHkuIEFkdmFudGFnZXM6IG9ubHkgb25lIG1vZGVsIHRvIHRyYWluOyBzYW1wbGUtZWZmaWNpZW50LiBEaXNhZHZhbnRhZ2U6IGVycm9ycyBhY2N1bXVsYXRlIOKAlCBpZiDFt+KCnOKCiuKCgSBoYXMgZXJyb3IgZeKCnOKCiuKCgSwgdGhpcyBlcnJvciBwcm9wYWdhdGVzIGFzIGFuIGlucHV0IGVycm9yIHRvIMW34oKc4oKK4oKCLiBGb3Igd2VsbC1zcGVjaWZpZWQgbW9kZWxzLCBlcnJvciBhY2N1bXVsYXRpb24gaXMgc21hbGw7IGZvciBtaXNzcGVjaWZpZWQgbW9kZWxzLCBiaWFzIGNvbXBvdW5kcyBhY3Jvc3MgaG9yaXpvbnMuIFJlY3Vyc2l2ZSBwZXJmb3JtcyBiZXN0IGF0IHNob3J0IGhvcml6b25zIChoIOKJpCA1KS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBSaWRnZVxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IG1lYW5fc3F1YXJlZF9lcnJvclxuXG5kZWYgbWFrZV9sYWdfZmVhdHVyZXMoeSwgbl9sYWdzKTpcbiAgICBYLCB5X291dCA9IFtdLCBbXVxuICAgIGZvciB0IGluIHJhbmdlKG5fbGFncywgbGVuKHkpKTpcbiAgICAgICAgWC5hcHBlbmQoeVt0IC0gbl9sYWdzOnRdWzo6LTFdKSAgIyBsYWdfMSwgbGFnXzIsIC4uLiwgbGFnX3BcbiAgICAgICAgeV9vdXQuYXBwZW5kKHlbdF0pXG4gICAgcmV0dXJuIG5wLmFycmF5KFgpLCBucC5hcnJheSh5X291dClcblxuZGVmIHJlY3Vyc2l2ZV9mb3JlY2FzdChtb2RlbCwgbGFzdF9vYnMsIG5fbGFncywgaG9yaXpvbik6XG4gICAgXCJcIlwiUmVjdXJzaXZlbHkgZm9yZWNhc3QgSCBzdGVwcyBieSBmZWVkaW5nIHByZWRpY3Rpb25zIGFzIGlucHV0cy5cIlwiXCJcbiAgICBoaXN0b3J5ID0gbGlzdChsYXN0X29ic1stbl9sYWdzOl0pXG4gICAgZm9yZWNhc3RzID0gW11cbiAgICBmb3IgXyBpbiByYW5nZShob3Jpem9uKTpcbiAgICAgICAgeCA9IG5wLmFycmF5KGhpc3RvcnlbLW5fbGFnczpdWzo6LTFdKS5yZXNoYXBlKDEsIC0xKVxuICAgICAgICBuZXh0X3ZhbCA9IG1vZGVsLnByZWRpY3QoeClbMF1cbiAgICAgICAgZm9yZWNhc3RzLmFwcGVuZChuZXh0X3ZhbClcbiAgICAgICAgaGlzdG9yeS5hcHBlbmQobmV4dF92YWwpXG4gICAgcmV0dXJuIG5wLmFycmF5KGZvcmVjYXN0cylcblxubnAucmFuZG9tLnNlZWQoNDIpXG5UID0gMzAwXG55ID0gbnAuemVyb3MoVClcbmZvciB0IGluIHJhbmdlKDEsIFQpOlxuICAgIHlbdF0gPSAwLjcgKiB5W3QgLSAxXSArIG5wLnJhbmRvbS5yYW5kbigpXG5cbm5fbGFncywgSCA9IDEwLCAyMFxuWCwgeV90ID0gbWFrZV9sYWdfZmVhdHVyZXMoeSwgbl9sYWdzKVxudHJhaW5fZW5kID0gaW50KDAuOCAqIGxlbihYKSlcbm1vZGVsID0gUmlkZ2UoYWxwaGE9MS4wKS5maXQoWFs6dHJhaW5fZW5kXSwgeV90Wzp0cmFpbl9lbmRdKVxuXG5mb3JlY2FzdHMgPSByZWN1cnNpdmVfZm9yZWNhc3QobW9kZWwsIHlbOnRyYWluX2VuZCArIG5fbGFnc10sIG5fbGFncywgSClcbnRydWVfdmFscyA9IHlbdHJhaW5fZW5kICsgbl9sYWdzOiB0cmFpbl9lbmQgKyBuX2xhZ3MgKyBIXVxuZm9yIGggaW4gWzEsIDUsIDEwLCAyMF06XG4gICAgcm1zZSA9IG5wLnNxcnQobWVhbl9zcXVhcmVkX2Vycm9yKFt0cnVlX3ZhbHNbaC0xXV0sIFtmb3JlY2FzdHNbaC0xXV0pKVxuICAgIHByaW50KGZcdTAwMjdoPXtoOjJkfTogUk1TRSA9IHtybXNlOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGlyZWN0IChESVJFQ1QpIE11bHRpLVN0ZXAgRm9yZWNhc3RpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpcmVjdCBzdHJhdGVneTogZm9yIGVhY2ggaG9yaXpvbiBoIOKIiCB7MSwgMiwgLi4uLCBIfSwgdHJhaW4gYSBzZXBhcmF0ZSBtb2RlbCBm4oKVIG9uIHRyYWluaW5nIHBhaXJzICh44oKcLCB54oKc4oKK4oKVKSB1c2luZyBwYXN0IG9ic2VydmF0aW9ucyBvbmx5IGFzIGZlYXR1cmVzLiBBdCB0ZXN0IHRpbWUsIGVhY2ggbW9kZWwgZuKClSBwcm9kdWNlcyBpdHMgb3duIGgtc3RlcC1haGVhZCBmb3JlY2FzdCB3aXRob3V0IGl0ZXJhdGluZy4gQWR2YW50YWdlczogbm8gZXJyb3IgYWNjdW11bGF0aW9uIChlYWNoIG1vZGVsIGlzIHRyYWluZWQgZGlyZWN0bHkgZm9yIGl0cyBob3Jpem9uKTsgdGhlb3JldGljYWxseSBsb3dlciBiaWFzIGZvciBtaXNzcGVjaWZpZWQgbW9kZWxzLiBEaXNhZHZhbnRhZ2VzOiBIIHNlcGFyYXRlIG1vZGVscyB0byB0cmFpbiBhbmQgbWFpbnRhaW47IGVhY2ggbW9kZWwgdXNlcyBmZXdlciB0cmFpbmluZyBzYW1wbGVzIChzaW5jZSB0aGUgbGFzdCBIIG9ic2VydmF0aW9ucyBoYXZlIG5vIHRhcmdldCBmb3IgbG9uZ2VyIGhvcml6b25zKTsgaWdub3JlcyBpbnRlci1ob3Jpem9uIGRlcGVuZGVuY2llcyAoZm9yZWNhc3RzIGZvciBoPTMgYW5kIGg9NCBhcmUgaW5kZXBlbmRlbnQpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgbWVhbl9zcXVhcmVkX2Vycm9yXG5cbmRlZiBkaXJlY3RfZm9yZWNhc3QoeSwgbl9sYWdzLCBob3Jpem9uKTpcbiAgICBcIlwiXCJcbiAgICBUcmFpbiBvbmUgUmlkZ2UgbW9kZWwgcGVyIGhvcml6b24gaCBpbiBbMS4uaG9yaXpvbl0uXG4gICAgUmV0dXJucyBkaWN0IG9mIHtoOiAobW9kZWwsIHJtc2Vfb25fdGVzdCl9LlxuICAgIFwiXCJcIlxuICAgIFQgPSBsZW4oeSlcbiAgICBzcGxpdCA9IGludCgwLjggKiBUKVxuICAgIG1vZGVscyA9IHt9XG4gICAgZm9yIGggaW4gcmFuZ2UoMSwgaG9yaXpvbiArIDEpOlxuICAgICAgICBYX3Jvd3MsIHlfcm93cyA9IFtdLCBbXVxuICAgICAgICBmb3IgdCBpbiByYW5nZShuX2xhZ3MsIFQgLSBoKTpcbiAgICAgICAgICAgIFhfcm93cy5hcHBlbmQoeVt0IC0gbl9sYWdzOnRdWzo6LTFdKVxuICAgICAgICAgICAgeV9yb3dzLmFwcGVuZCh5W3QgKyBoXSlcbiAgICAgICAgWF9hbGwgPSBucC5hcnJheShYX3Jvd3MpXG4gICAgICAgIHlfYWxsID0gbnAuYXJyYXkoeV9yb3dzKVxuICAgICAgICBzcGxpdF9oID0gc3VtKDEgZm9yIHQgaW4gcmFuZ2Uobl9sYWdzLCBzcGxpdCkpXG4gICAgICAgIG0gPSBSaWRnZShhbHBoYT0xLjApLmZpdChYX2FsbFs6c3BsaXRfaF0sIHlfYWxsWzpzcGxpdF9oXSlcbiAgICAgICAgcHJlZCA9IG0ucHJlZGljdChYX2FsbFtzcGxpdF9oOl0pXG4gICAgICAgIHJtc2UgPSBucC5zcXJ0KG1lYW5fc3F1YXJlZF9lcnJvcih5X2FsbFtzcGxpdF9oOl0sIHByZWQpKVxuICAgICAgICBtb2RlbHNbaF0gPSAobSwgcm1zZSlcbiAgICByZXR1cm4gbW9kZWxzXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuVCA9IDMwMFxueSA9IG5wLnplcm9zKFQpXG5mb3IgdCBpbiByYW5nZSgxLCBUKTpcbiAgICB5W3RdID0gMC43ICogeVt0IC0gMV0gKyBucC5yYW5kb20ucmFuZG4oKVxuXG5tb2RlbHMgPSBkaXJlY3RfZm9yZWNhc3QoeSwgbl9sYWdzPTEwLCBob3Jpem9uPTIwKVxucHJpbnQoXHUwMDI3RGlyZWN0IGZvcmVjYXN0IFJNU0UgcGVyIGhvcml6b246XHUwMDI3KVxuZm9yIGggaW4gWzEsIDUsIDEwLCAyMF06XG4gICAgcHJpbnQoZlx1MDAyNyAgaD17aDoyZH06IFJNU0UgPSB7bW9kZWxzW2hdWzFdOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTUlNTyBNdWx0aS1TdGVwIEZvcmVjYXN0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNSU1PIChNdWx0aXBsZSBJbnB1dCBNdWx0aXBsZSBPdXRwdXQpOiBhIHNpbmdsZSBtb2RlbCBtYXBzIGlucHV0IHZlY3RvciB44oKcID0gW3nigpwsIHnigpzigovigoEsIC4uLiwgeeKCnOKCi+KCml0gdG8gdGhlIGZ1bGwgb3V0cHV0IHZlY3RvciBbxbfigpzigorigoEsIC4uLiwgxbfigpzigopIXSBzaW11bHRhbmVvdXNseS4gVGhlIG1vZGVsIGNhcHR1cmVzIGludGVyLWhvcml6b24gZGVwZW5kZW5jaWVzIOKAlCBrbm93aW5nIMW34oKc4oKK4oKBIGluZm9ybXMgxbfigpzigorigoIg4oCUIHdoaWNoIGRpcmVjdCBtb2RlbHMgaWdub3JlLiBNSU1PIGlzIG5hdHVyYWwgZm9yIG5ldXJhbCBuZXR3b3JrcyAob3V0cHV0IGxheWVyIGhhcyBIIHVuaXRzKSBhbmQgbXVsdGktb3V0cHV0IHJlZ3Jlc3NvcnMuIFRyYWluaW5nIHVzZXMgYWxsIHNhbXBsZXMgd2hlcmUgdGhlIGZ1bGwgSC1zdGVwIHRhcmdldCBpcyBhdmFpbGFibGUuIE1JTU8gb3V0cGVyZm9ybXMgZGlyZWN0IHdoZW4gc2VyaWVzIGhhdmUgc21vb3RoIHRyYWplY3RvcmllcyBhbmQgaW50ZXItaG9yaXpvbiBjb3JyZWxhdGlvbnM7IGl0IGlzIHRoZSBzdGFuZGFyZCBhcHByb2FjaCBmb3IgVHJhbnNmb3JtZXItYmFzZWQgZm9yZWNhc3RlcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRElSTU86IEdyb3VwZWQgSG9yaXpvbiBTdHJhdGVneSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRElSTU8gKERpcmVjdC1NSU1PKSBwYXJ0aXRpb25zIHRoZSBIIG91dHB1dCBob3Jpem9ucyBpbnRvIEcgZ3JvdXBzIG9mIHNpemUgZyA9IEgvRywgdGhlbiB0cmFpbnMgb25lIE1JTU8gbW9kZWwgcGVyIGdyb3VwLiBGb3IgSD0yNCwgRz02LCBlYWNoIE1JTU8gbW9kZWwgcHJvZHVjZXMgNC1zdGVwIG91dHB1dHM6IG9uZSBtb2RlbCBmb3IgaD0xLi40LCBhbm90aGVyIGZvciBoPTUuLjgsIGV0Yy4gVGhpcyByZWR1Y2VzIHRoZSBudW1iZXIgb2YgbW9kZWxzIGZyb20gSCAocHVyZSBkaXJlY3QpIHRvIEcgd2hpbGUgcHJlc2VydmluZyBpbnRlci1ob3Jpem9uIGNvbnNpc3RlbmN5IHdpdGhpbiBlYWNoIGdyb3VwLiBESVJNTyBpcyBhIHByYWN0aWNhbCBjb21wcm9taXNlOiBpdCBhdm9pZHMgbWFuYWdpbmcgSCBpbmRlcGVuZGVudCBtb2RlbHMgd2hpbGUga2VlcGluZyBlYWNoIE1JTU8gb3V0cHV0IGRpbWVuc2lvbiBzbWFsbCBlbm91Z2ggdG8gdHJhaW4gcmVsaWFibHkgb24gbGltaXRlZCBkYXRhLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlXG5mcm9tIHNrbGVhcm4ubXVsdGlvdXRwdXQgaW1wb3J0IE11bHRpT3V0cHV0UmVncmVzc29yXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgbWVhbl9zcXVhcmVkX2Vycm9yXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuVCA9IDQwMFxueSA9IG5wLnplcm9zKFQpXG5mb3IgdCBpbiByYW5nZSgxLCBUKTpcbiAgICB5W3RdID0gMC44ICogeVt0IC0gMV0gKyBucC5yYW5kb20ucmFuZG4oKVxuXG5uX2xhZ3MsIEggPSAxNSwgMjBcblhfcm93cywgeV9yb3dzID0gW10sIFtdXG5mb3IgdCBpbiByYW5nZShuX2xhZ3MsIFQgLSBIKTpcbiAgICBYX3Jvd3MuYXBwZW5kKHlbdCAtIG5fbGFnczp0XVs6Oi0xXSlcbiAgICB5X3Jvd3MuYXBwZW5kKHlbdDp0ICsgSF0pXG5YX2FsbCA9IG5wLmFycmF5KFhfcm93cylcbnlfYWxsID0gbnAuYXJyYXkoeV9yb3dzKSAgICMgc2hhcGUgKG5fc2FtcGxlcywgSClcblxuc3BsaXQgPSBpbnQoMC44ICogbGVuKFhfYWxsKSlcblhfdHJhaW4sIFhfdGVzdCA9IFhfYWxsWzpzcGxpdF0sIFhfYWxsW3NwbGl0Ol1cbnlfdHJhaW4sIHlfdGVzdCA9IHlfYWxsWzpzcGxpdF0sIHlfYWxsW3NwbGl0Ol1cblxubWltbyA9IE11bHRpT3V0cHV0UmVncmVzc29yKFJpZGdlKGFscGhhPTEuMCkpXG5taW1vLmZpdChYX3RyYWluLCB5X3RyYWluKVxucHJlZCA9IG1pbW8ucHJlZGljdChYX3Rlc3QpXG5cbnByaW50KFx1MDAyN01JTU8gUk1TRSBwZXIgaG9yaXpvbjpcdTAwMjcpXG5mb3IgaF9pZHggaW4gWzAsIDQsIDksIDE5XTpcbiAgICBybXNlID0gbnAuc3FydChtZWFuX3NxdWFyZWRfZXJyb3IoeV90ZXN0WzosIGhfaWR4XSwgcHJlZFs6LCBoX2lkeF0pKVxuICAgIHByaW50KGZcdTAwMjcgIGg9e2hfaWR4KzE6MmR9OiBSTVNFID0ge3Jtc2U6LjRmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkRJUk1POiBIeWJyaWQgb2YgRGlyZWN0IGFuZCBNSU1PIiwiY29udGVudCI6IkRJUk1PIGdyb3VwcyBob3Jpem9ucyBpbnRvIEcgYmxvY2tzIChlLmcuLCBIPTEyIOKGkiAzIGdyb3VwcyBvZiA0KSBhbmQgdHJhaW5zIG9uZSBNSU1PIG1vZGVsIHBlciBncm91cC4gVGhpcyByZWR1Y2VzIHRoZSBudW1iZXIgb2YgbW9kZWxzIHZlcnN1cyBwdXJlIERpcmVjdCAoRyBcdTAwM2MgSCkgd2hpbGUgcHJlc2VydmluZyBpbnRlci1ob3Jpem9uIGRlcGVuZGVuY3kgd2l0aGluIGVhY2ggZ3JvdXAuIERJUk1PIG9mdGVuIGFjaGlldmVzIHRoZSBiZXN0IG9mIGJvdGggd29ybGRzOiBsb3dlciBiaWFzIHRoYW4gcmVjdXJzaXZlLCBmZXdlciBtb2RlbHMgdGhhbiBkaXJlY3QsIGFuZCByaWNoZXIgb3V0cHV0IHN0cnVjdHVyZSB0aGFuIE1JTU8gd2l0aCBzbWFsbGVyIG91dHB1dCBkaW1lbnNpb24gcGVyIG1vZGVsLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlY3Vyc2l2ZSB2cyBEaXJlY3QgdnMgTUlNTyBBY2N1cmFjeSBDb21wYXJpc29uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUmlkZ2VcbmZyb20gc2tsZWFybi5tdWx0aW91dHB1dCBpbXBvcnQgTXVsdGlPdXRwdXRSZWdyZXNzb3JcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBtZWFuX3NxdWFyZWRfZXJyb3JcblxubnAucmFuZG9tLnNlZWQoNylcblQgPSA1MDBcbnkgPSBucC56ZXJvcyhUKVxuZm9yIHQgaW4gcmFuZ2UoMSwgVCk6XG4gICAgeVt0XSA9IDAuNzUgKiB5W3QgLSAxXSArIG5wLnJhbmRvbS5yYW5kbigpXG5cbm5fbGFncywgSCA9IDEwLCAxNVxuc3BsaXRfdCA9IDQwMFxuXG5kZWYgcm1zZShhLCBiKTpcbiAgICByZXR1cm4gbnAuc3FydChtZWFuX3NxdWFyZWRfZXJyb3IoYSwgYikpXG5cblhfYWxsID0gbnAuYXJyYXkoW3lbdCAtIG5fbGFnczp0XVs6Oi0xXSBmb3IgdCBpbiByYW5nZShuX2xhZ3MsIFQpXSlcbnlfc3RlcCA9IHlbbl9sYWdzOl1cblhfdHIsIFhfdGUgPSBYX2FsbFs6c3BsaXRfdCAtIG5fbGFnc10sIFhfYWxsW3NwbGl0X3QgLSBuX2xhZ3M6XVxueV90ciA9IHlfc3RlcFs6c3BsaXRfdCAtIG5fbGFnc11cblxub25lX3N0ZXAgPSBSaWRnZShhbHBoYT0xLjApLmZpdChYX3RyLCB5X3RyKVxuXG4jIE1JTU8gdGFyZ2V0c1xueV9taW1vID0gbnAuYXJyYXkoW3lbdDp0ICsgSF0gZm9yIHQgaW4gcmFuZ2Uobl9sYWdzLCBUIC0gSCldKVxuWF9taW1vID0gWF9hbGxbOmxlbih5X21pbW8pXVxuc3BsaXRfbSA9IHNwbGl0X3QgLSBuX2xhZ3Ncbm1pbW8gPSBNdWx0aU91dHB1dFJlZ3Jlc3NvcihSaWRnZShhbHBoYT0xLjApKS5maXQoWF9taW1vWzpzcGxpdF9tXSwgeV9taW1vWzpzcGxpdF9tXSlcbm1pbW9fcHJlZCA9IG1pbW8ucHJlZGljdChYX21pbW9bc3BsaXRfbTpdKVxuXG5wcmludChmXHUwMDI3e1wiSG9yaXpvblwiOlx1MDAzZTh9IHtcIlJlY3Vyc2l2ZVwiOlx1MDAzZTEyfSB7XCJNSU1PXCI6XHUwMDNlMTJ9XHUwMDI3KVxuZm9yIGggaW4gWzEsIDMsIDUsIDEwLCAxNV06XG4gICAgaGlzdCA9IGxpc3QoeVtzcGxpdF90IC0gbl9sYWdzOnNwbGl0X3RdKVxuICAgIHJlY19wcmVkcyA9IFtdXG4gICAgZm9yIHQgaW4gcmFuZ2UobGVuKFhfdGUpKTpcbiAgICAgICAgeGggPSBucC5hcnJheShoaXN0Wy1uX2xhZ3M6XVs6Oi0xXSkucmVzaGFwZSgxLCAtMSlcbiAgICAgICAgeWggPSBvbmVfc3RlcC5wcmVkaWN0KHhoKVswXTsgcmVjX3ByZWRzLmFwcGVuZCh5aCk7IGhpc3QuYXBwZW5kKHloKVxuICAgIHRydWVfaCA9IHlbc3BsaXRfdCArIGggLSAxOiBzcGxpdF90ICsgaF1cbiAgICBwcmludChmXHUwMDI3e2g6XHUwMDNlOH0gIHtyZWNfcHJlZHNbaC0xXSBpZiBoIFx1MDAzYz0gbGVuKHJlY19wcmVkcykgZWxzZSBcIk4vQVwiOlx1MDAzZTEyLjRmfSAge21pbW9fcHJlZFswLCBoLTFdOlx1MDAzZTEyLjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNdWx0aS1TdGVwIFN0cmF0ZWd5IFJlZmVyZW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJTdHJhdGVneSIsIkVycm9yIEFjY3VtdWxhdGlvbiIsIkludGVyLUhvcml6b24gRGVwZW5kZW5jeSIsIk1vZGVscyB0byBUcmFpbiIsIkJlc3QgSG9yaXpvbiIsIlR5cGljYWwgVXNlIENhc2UiXSwicm93cyI6W1siUmVjdXJzaXZlIiwiWWVzIOKAlCBjb21wb3VuZHMgd2l0aCBoIiwiSW1wbGljaXQgdmlhIHNoYXJlZCBtb2RlbCIsIjEiLCJTaG9ydCAoaCDiiaQgNSkiLCJXZWxsLXNwZWNpZmllZCBtb2RlbHMsIHNpbmdsZS1zdGVwIGRhdGEiXSxbIkRpcmVjdCIsIk5vIiwiTm9uZSAoaW5kZXBlbmRlbnQgcGVyIGgpIiwiSCIsIkxvbmcgKGggXHUwMDNlIDEwKSIsIk1pc3NwZWNpZmllZCBtb2RlbHMsIHRhYnVsYXIgTUwiXSxbIk1JTU8iLCJObyIsIkNhcHR1cmVkIGJ5IGpvaW50IG91dHB1dCIsIjEiLCJNZWRpdW3igJNsb25nIiwiTmV1cmFsIG5ldHMsIFRyYW5zZm9ybWVyIGZvcmVjYXN0ZXJzIl0sWyJESVJNTyIsIk5vIiwiV2l0aGluLWdyb3VwIG9ubHkiLCJHIChncm91cHMpIiwiQW55IiwiQ29tcHJvbWlzZTogZmV3ZXIgbW9kZWxzIHRoYW4gRGlyZWN0Il1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZvciBoIOKJpCA1LCByZWN1cnNpdmUgc3RyYXRlZ3kgaXMgdXN1YWxseSBjb21wZXRpdGl2ZSBhbmQgc2ltcGxlciB0byBpbXBsZW1lbnQgYW5kIG1haW50YWluLiIsIkZvciBoIFx1MDAzZSAxMCB3aXRoIHRhYnVsYXIgTUwgKExpZ2h0R0JNLCBYR0Jvb3N0KSwgZGlyZWN0IG91dHBlcmZvcm1zIHJlY3Vyc2l2ZSBkdWUgdG8gY29tcG91bmRpbmcgYmlhcy4iLCJNSU1PIGlzIHRoZSBuYXR1cmFsIGNob2ljZSBmb3IgbmV1cmFsIG5ldHdvcmsgYXJjaGl0ZWN0dXJlcyB0aGF0IG91dHB1dCBhIGZ1bGwgaG9yaXpvbiB2ZWN0b3IgaW4gb25lIGZvcndhcmQgcGFzcy4iLCJBbHdheXMgZXZhbHVhdGUgYWNjdXJhY3kgYXQgZWFjaCBpbmRpdmlkdWFsIGhvcml6b24gaCwgbm90IGp1c3QgYXMgYW4gYXZlcmFnZSDigJQgZXJyb3IgcHJvZmlsZXMgZGlmZmVyIGRyYW1hdGljYWxseSBieSBzdHJhdGVneS4iLCJDYWxpYnJhdGUgcHJlZGljdGlvbiBpbnRlcnZhbHMgc2VwYXJhdGVseSBwZXIgaG9yaXpvbjsgcmVjdXJzaXZlIGludGVydmFscyB1bmRlcmVzdGltYXRlIHdpZHRoIGJlY2F1c2UgdGhleSBpZ25vcmUgZXJyb3IgYWNjdW11bGF0aW9uLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBwcm9iYWJpbGlzdGljIG11bHRpLXN0ZXAgZm9yZWNhc3RpbmcsIGdlbmVyYXRlIHNhbXBsZSBwYXRocyByYXRoZXIgdGhhbiBwb2ludCBmb3JlY2FzdHM6IHNpbXVsYXRlIHRoZSByZWN1cnNpdmUgc3RyYXRlZ3kgTSB0aW1lcyBieSBhZGRpbmcgbm9pc2UgZHJhd24gZnJvbSB0aGUgcmVzaWR1YWwgZGlzdHJpYnV0aW9uIGF0IGVhY2ggc3RlcCwgdGhlbiBhZ2dyZWdhdGUgdGhlIE0gcGF0aHMgdG8gZ2V0IHF1YW50aWxlIGVzdGltYXRlcy4gVGhpcyBNb250ZSBDYXJsbyBhcHByb2FjaCBjYXB0dXJlcyBlcnJvciBhY2N1bXVsYXRpb24gaW4gdGhlIHRhaWxzIG5hdHVyYWxseSwgcHJvZHVjaW5nIHdpZGVyIGludGVydmFscyBmb3IgZGlzdGFudCBob3Jpem9ucyB3aXRob3V0IHJlcXVpcmluZyBwYXJhbWV0cmljIGFzc3VtcHRpb25zIGFib3V0IHRoZSBlcnJvciBkaXN0cmlidXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMaWJyYXJ5IHN1cHBvcnQgZm9yIG11bHRpLXN0ZXAgc3RyYXRlZ2llczogc2t0aW1lIHByb3ZpZGVzIERpcmVjdFRhYnVsYXJSZWdyZXNzaW9uRm9yZWNhc3RlciBhbmQgTXVsdGlPdXRwdXRUYWJ1bGFyUmVncmVzc2lvbkZvcmVjYXN0ZXIgKE1JTU8pLiBEYXJ0cyBzdXBwb3J0cyByZWN1cnNpdmUsIGRpcmVjdCwgYW5kIE1JTU8gd2l0aCBMaWdodEdCTS9YR0Jvb3N0IGJhY2tlbmRzLiBUaGUgbmV1cmFsZm9yZWNhc3QgbGlicmFyeSBwcm92aWRlcyBOSElUUyBhbmQgTkJFQVRTIGluIE1JTU8gbW9kZS4gRm9yIHF1aWNrIGJhc2VsaW5lcywgc2Npa2l0LWxlYXJuXHUwMDI3cyBNdWx0aU91dHB1dFJlZ3Jlc3NvciB3cmFwcyBhbnkgc2luZ2xlLW91dHB1dCBtb2RlbCBpbnRvIGEgZGlyZWN0IChwZXItaG9yaXpvbikgc3RyYXRlZ3kuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Multi-Step Forecasting — Direct, Recursive, and MIMO

Multi-step forecasting requires producing predictions for horizons h=1, 2, ..., H rather than just the next step. Three main strategies exist: recursive (train one-step model, feed predictions as inputs iteratively), direct (train one separate model per horizon), and MIMO (Multiple Input Multiple Output — train one model that outputs all H horizons simultaneously). Each strategy has distinct bias-variance properties, and the best choice depends on the forecast horizon, model misspecification, and the inter-horizon dependency structure of the target series.

- Recursive: 1 model, error accumulates across horizons, best for h ≤ 5.
- Direct: H models (one per horizon), no error accumulation, best for long horizons with misspecified models.
- MIMO: 1 model outputting all H horizons, captures inter-horizon dependencies, natural for neural nets.
- DIRMO: G models (one per group of horizons), hybrid between Direct and MIMO.
- Always evaluate RMSE at each individual horizon h, not just the average — profiles differ by strategy.

## Recursive (Iterated One-Step) Forecasting

Recursive strategy: train a one-step model ŷₜ₊₁ = f(yₜ, yₜ₋₁, ..., yₜ₋ₚ). At test time, to forecast h steps ahead, feed the predicted ŷₜ₊₁ as an input to produce ŷₜ₊₂, and so on iteratively. Advantages: only one model to train; sample-efficient. Disadvantage: errors accumulate — if ŷₜ₊₁ has error eₜ₊₁, this error propagates as an input error to ŷₜ₊₂. For well-specified models, error accumulation is small; for misspecified models, bias compounds across horizons. Recursive performs best at short horizons (h ≤ 5).

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def make_lag_features(y, n_lags):
    X, y_out = [], []
    for t in range(n_lags, len(y)):
        X.append(y[t - n_lags:t][::-1])  # lag_1, lag_2, ..., lag_p
        y_out.append(y[t])
    return np.array(X), np.array(y_out)

def recursive_forecast(model, last_obs, n_lags, horizon):
    """Recursively forecast H steps by feeding predictions as inputs."""
    history = list(last_obs[-n_lags:])
    forecasts = []
    for _ in range(horizon):
        x = np.array(history[-n_lags:][::-1]).reshape(1, -1)
        next_val = model.predict(x)[0]
        forecasts.append(next_val)
        history.append(next_val)
    return np.array(forecasts)

np.random.seed(42)
T = 300
y = np.zeros(T)
for t in range(1, T):
    y[t] = 0.7 * y[t - 1] + np.random.randn()

n_lags, H = 10, 20
X, y_t = make_lag_features(y, n_lags)
train_end = int(0.8 * len(X))
model = Ridge(alpha=1.0).fit(X[:train_end], y_t[:train_end])

forecasts = recursive_forecast(model, y[:train_end + n_lags], n_lags, H)
true_vals = y[train_end + n_lags: train_end + n_lags + H]
for h in [1, 5, 10, 20]:
    rmse = np.sqrt(mean_squared_error([true_vals[h-1]], [forecasts[h-1]]))
    print(f'h={h:2d}: RMSE = {rmse:.4f}')
```

## Direct (DIRECT) Multi-Step Forecasting

Direct strategy: for each horizon h ∈ {1, 2, ..., H}, train a separate model fₕ on training pairs (xₜ, yₜ₊ₕ) using past observations only as features. At test time, each model fₕ produces its own h-step-ahead forecast without iterating. Advantages: no error accumulation (each model is trained directly for its horizon); theoretically lower bias for misspecified models. Disadvantages: H separate models to train and maintain; each model uses fewer training samples (since the last H observations have no target for longer horizons); ignores inter-horizon dependencies (forecasts for h=3 and h=4 are independent).

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def direct_forecast(y, n_lags, horizon):
    """
    Train one Ridge model per horizon h in [1..horizon].
    Returns dict of {h: (model, rmse_on_test)}.
    """
    T = len(y)
    split = int(0.8 * T)
    models = {}
    for h in range(1, horizon + 1):
        X_rows, y_rows = [], []
        for t in range(n_lags, T - h):
            X_rows.append(y[t - n_lags:t][::-1])
            y_rows.append(y[t + h])
        X_all = np.array(X_rows)
        y_all = np.array(y_rows)
        split_h = sum(1 for t in range(n_lags, split))
        m = Ridge(alpha=1.0).fit(X_all[:split_h], y_all[:split_h])
        pred = m.predict(X_all[split_h:])
        rmse = np.sqrt(mean_squared_error(y_all[split_h:], pred))
        models[h] = (m, rmse)
    return models

np.random.seed(42)
T = 300
y = np.zeros(T)
for t in range(1, T):
    y[t] = 0.7 * y[t - 1] + np.random.randn()

models = direct_forecast(y, n_lags=10, horizon=20)
print('Direct forecast RMSE per horizon:')
for h in [1, 5, 10, 20]:
    print(f'  h={h:2d}: RMSE = {models[h][1]:.4f}')
```

## MIMO Multi-Step Forecasting

MIMO (Multiple Input Multiple Output): a single model maps input vector xₜ = [yₜ, yₜ₋₁, ..., yₜ₋ₚ] to the full output vector [ŷₜ₊₁, ..., ŷₜ₊H] simultaneously. The model captures inter-horizon dependencies — knowing ŷₜ₊₁ informs ŷₜ₊₂ — which direct models ignore. MIMO is natural for neural networks (output layer has H units) and multi-output regressors. Training uses all samples where the full H-step target is available. MIMO outperforms direct when series have smooth trajectories and inter-horizon correlations; it is the standard approach for Transformer-based forecasters.

## DIRMO: Grouped Horizon Strategy

DIRMO (Direct-MIMO) partitions the H output horizons into G groups of size g = H/G, then trains one MIMO model per group. For H=24, G=6, each MIMO model produces 4-step outputs: one model for h=1..4, another for h=5..8, etc. This reduces the number of models from H (pure direct) to G while preserving inter-horizon consistency within each group. DIRMO is a practical compromise: it avoids managing H independent models while keeping each MIMO output dimension small enough to train reliably on limited data.

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error

np.random.seed(42)
T = 400
y = np.zeros(T)
for t in range(1, T):
    y[t] = 0.8 * y[t - 1] + np.random.randn()

n_lags, H = 15, 20
X_rows, y_rows = [], []
for t in range(n_lags, T - H):
    X_rows.append(y[t - n_lags:t][::-1])
    y_rows.append(y[t:t + H])
X_all = np.array(X_rows)
y_all = np.array(y_rows)   # shape (n_samples, H)

split = int(0.8 * len(X_all))
X_train, X_test = X_all[:split], X_all[split:]
y_train, y_test = y_all[:split], y_all[split:]

mimo = MultiOutputRegressor(Ridge(alpha=1.0))
mimo.fit(X_train, y_train)
pred = mimo.predict(X_test)

print('MIMO RMSE per horizon:')
for h_idx in [0, 4, 9, 19]:
    rmse = np.sqrt(mean_squared_error(y_test[:, h_idx], pred[:, h_idx]))
    print(f'  h={h_idx+1:2d}: RMSE = {rmse:.4f}')
```

> **DIRMO: Hybrid of Direct and MIMO**: DIRMO groups horizons into G blocks (e.g., H=12 → 3 groups of 4) and trains one MIMO model per group. This reduces the number of models versus pure Direct (G < H) while preserving inter-horizon dependency within each group. DIRMO often achieves the best of both worlds: lower bias than recursive, fewer models than direct, and richer output structure than MIMO with smaller output dimension per model.

## Recursive vs Direct vs MIMO Accuracy Comparison

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error

np.random.seed(7)
T = 500
y = np.zeros(T)
for t in range(1, T):
    y[t] = 0.75 * y[t - 1] + np.random.randn()

n_lags, H = 10, 15
split_t = 400

def rmse(a, b):
    return np.sqrt(mean_squared_error(a, b))

X_all = np.array([y[t - n_lags:t][::-1] for t in range(n_lags, T)])
y_step = y[n_lags:]
X_tr, X_te = X_all[:split_t - n_lags], X_all[split_t - n_lags:]
y_tr = y_step[:split_t - n_lags]

one_step = Ridge(alpha=1.0).fit(X_tr, y_tr)

# MIMO targets
y_mimo = np.array([y[t:t + H] for t in range(n_lags, T - H)])
X_mimo = X_all[:len(y_mimo)]
split_m = split_t - n_lags
mimo = MultiOutputRegressor(Ridge(alpha=1.0)).fit(X_mimo[:split_m], y_mimo[:split_m])
mimo_pred = mimo.predict(X_mimo[split_m:])

print(f'{"Horizon":>8} {"Recursive":>12} {"MIMO":>12}')
for h in [1, 3, 5, 10, 15]:
    hist = list(y[split_t - n_lags:split_t])
    rec_preds = []
    for t in range(len(X_te)):
        xh = np.array(hist[-n_lags:][::-1]).reshape(1, -1)
        yh = one_step.predict(xh)[0]; rec_preds.append(yh); hist.append(yh)
    true_h = y[split_t + h - 1: split_t + h]
    print(f'{h:>8}  {rec_preds[h-1] if h <= len(rec_preds) else "N/A":>12.4f}  {mimo_pred[0, h-1]:>12.4f}')
```

## Multi-Step Strategy Reference

| Strategy | Error Accumulation | Inter-Horizon Dependency | Models to Train | Best Horizon | Typical Use Case |
| --- | --- | --- | --- | --- | --- |
| Recursive | Yes — compounds with h | Implicit via shared model | 1 | Short (h ≤ 5) | Well-specified models, single-step data |
| Direct | No | None (independent per h) | H | Long (h > 10) | Misspecified models, tabular ML |
| MIMO | No | Captured by joint output | 1 | Medium–long | Neural nets, Transformer forecasters |
| DIRMO | No | Within-group only | G (groups) | Any | Compromise: fewer models than Direct |

- For h ≤ 5, recursive strategy is usually competitive and simpler to implement and maintain.
- For h > 10 with tabular ML (LightGBM, XGBoost), direct outperforms recursive due to compounding bias.
- MIMO is the natural choice for neural network architectures that output a full horizon vector in one forward pass.
- Always evaluate accuracy at each individual horizon h, not just as an average — error profiles differ dramatically by strategy.
- Calibrate prediction intervals separately per horizon; recursive intervals underestimate width because they ignore error accumulation.

For probabilistic multi-step forecasting, generate sample paths rather than point forecasts: simulate the recursive strategy M times by adding noise drawn from the residual distribution at each step, then aggregate the M paths to get quantile estimates. This Monte Carlo approach captures error accumulation in the tails naturally, producing wider intervals for distant horizons without requiring parametric assumptions about the error distribution.

Library support for multi-step strategies: sktime provides DirectTabularRegressionForecaster and MultiOutputTabularRegressionForecaster (MIMO). Darts supports recursive, direct, and MIMO with LightGBM/XGBoost backends. The neuralforecast library provides NHITS and NBEATS in MIMO mode. For quick baselines, scikit-learn's MultiOutputRegressor wraps any single-output model into a direct (per-horizon) strategy.

---

