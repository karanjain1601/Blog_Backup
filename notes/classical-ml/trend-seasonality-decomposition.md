---
title: "Trend, Seasonality, and Residual — Additive vs Multiplicative"
slug: "trend-seasonality-decomposition"
description: "Decompose time series into trend, seasonal, and residual components using classical additive and multiplicative schemes, estimate trends via moving averages and the HP filter, and choose the right decomposition by analysing seasonal amplitude."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGltZS1zZXJpZXMgZGVjb21wb3NpdGlvbiBzZXBhcmF0ZXMgYW4gb2JzZXJ2ZWQgc2VxdWVuY2UgaW50byBpbnRlcnByZXRhYmxlIGNvbXBvbmVudHM6IGEgbG9uZy1ydW4gdHJlbmQsIGEgcmVwZWF0aW5nIHNlYXNvbmFsIHBhdHRlcm4sIGFuZCBhIHJlc2lkdWFsIHRoYXQgY2FwdHVyZXMgaXJyZWd1bGFyIHNob2Nrcy4gRGVjb21wb3NpdGlvbiBzZXJ2ZXMgdHdvIHB1cnBvc2VzOiBpdCBtYWtlcyBlYWNoIGNvbXBvbmVudCBlYXN5IHRvIG1vZGVsIHNlcGFyYXRlbHksIGFuZCBpdCBwcm92aWRlcyBkaWFnbm9zdGljcyBhYm91dCB0aGUgbmF0dXJlIG9mIHNlYXNvbmFsaXR5IChhZGRpdGl2ZSB2cyBtdWx0aXBsaWNhdGl2ZSkgdGhhdCBpbmZvcm0gdGhlIGNob2ljZSBvZiBmb3JlY2FzdGluZyBtb2RlbC4gQ2xhc3NpY2FsIGRlY29tcG9zaXRpb24gaXMgdGhlIHNpbXBsZXN0IGFwcHJvYWNoOyBtb2Rlcm4gbWV0aG9kcyBsaWtlIFNUTCBhbmQgWC0xM0FSSU1BLVNFQVRTIGV4dGVuZCBpdCBzdWJzdGFudGlhbGx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFkZGl0aXZlIGFuZCBNdWx0aXBsaWNhdGl2ZSBTY2hlbWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiB0aGUgYWRkaXRpdmUgbW9kZWwgeeKCnCA9IFTigpwgKyBT4oKcICsgUuKCnCwgdGhlIHNlYXNvbmFsIGFtcGxpdHVkZSBpcyBjb25zdGFudCByZWdhcmRsZXNzIG9mIHRoZSBsZXZlbC4gQSByZXRhaWxlciB3aG9zZSBDaHJpc3RtYXMgcGVhayBpcyBhbHdheXMgZXhhY3RseSAxMDAwIHVuaXRzIGFib3ZlIHRoZSB0cmVuZCBmb2xsb3dzIGFuIGFkZGl0aXZlIHBhdHRlcm4uIEluIHRoZSBtdWx0aXBsaWNhdGl2ZSBtb2RlbCB54oKcID0gVOKCnCDCtyBT4oKcIMK3IFLigpwsIHRoZSBzZWFzb25hbCBzd2luZyBzY2FsZXMgcHJvcG9ydGlvbmFsbHkgd2l0aCB0aGUgdHJlbmQgbGV2ZWwg4oCUIGEgc2VyaWVzIHRoYXQgZG91YmxlcyBpbiBsZXZlbCBhbHNvIGRvdWJsZXMgaXRzIHNlYXNvbmFsIHBlYWstdG8tdHJvdWdoIHJhbmdlLiBUYWtpbmcgbG9nYXJpdGhtcyBvZiBhIG11bHRpcGxpY2F0aXZlIHNlcmllcyBjb252ZXJ0cyBpdCB0byBhZGRpdGl2ZTogbG9nKHnigpwpID0gbG9nKFTigpwpICsgbG9nKFPigpwpICsgbG9nKFLigpwpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc3RhdHNtb2RlbHMudHNhLnNlYXNvbmFsIGltcG9ydCBzZWFzb25hbF9kZWNvbXBvc2VcblxubnAucmFuZG9tLnNlZWQoMClcbm4gPSAxMjAgICMgMTAgeWVhcnMgb2YgbW9udGhseSBkYXRhXG50ID0gbnAuYXJhbmdlKG4pXG5cbiMgQWRkaXRpdmU6IGNvbnN0YW50IHNlYXNvbmFsIGFtcGxpdHVkZVxudHJlbmRfYWRkID0gNTAgKyAwLjMgKiB0XG5zZWFzb25fYWRkID0gMTAgKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDEyKVxueV9hZGQgPSB0cmVuZF9hZGQgKyBzZWFzb25fYWRkICsgMiAqIG5wLnJhbmRvbS5yYW5kbihuKVxuXG4jIE11bHRpcGxpY2F0aXZlOiBzZWFzb25hbCBhbXBsaXR1ZGUgZ3Jvd3Mgd2l0aCB0cmVuZFxudHJlbmRfbXVsdCA9IDUwICsgMC40ICogdFxuc2Vhc29uX211bHQgPSAxICsgMC4zICogbnAuc2luKDIgKiBucC5waSAqIHQgLyAxMilcbnlfbXVsdCA9IHRyZW5kX211bHQgKiBzZWFzb25fbXVsdCAqIG5wLmV4cCgwLjA1ICogbnAucmFuZG9tLnJhbmRuKG4pKVxuXG5mb3IgbGFiZWwsIHksIG1vZGVsIGluIFsoXCJBZGRpdGl2ZVwiLCB5X2FkZCwgXCJhZGRpdGl2ZVwiKSwgKFwiTXVsdGlwbGljYXRpdmVcIiwgeV9tdWx0LCBcIm11bHRpcGxpY2F0aXZlXCIpXTpcbiAgICByZXN1bHQgPSBzZWFzb25hbF9kZWNvbXBvc2UoeSwgbW9kZWw9bW9kZWwsIHBlcmlvZD0xMilcbiAgICByZXNpZCA9IHJlc3VsdC5yZXNpZFt+bnAuaXNuYW4ocmVzdWx0LnJlc2lkKV1cbiAgICBwcmludChmXCJcXG57bGFiZWx9IGRlY29tcG9zaXRpb25cIilcbiAgICBwcmludChmXCIgIFRyZW5kIHJhbmdlOiAgICBbe3Jlc3VsdC50cmVuZFt+bnAuaXNuYW4ocmVzdWx0LnRyZW5kKV0ubWluKCk6LjFmfSwge3Jlc3VsdC50cmVuZFt+bnAuaXNuYW4ocmVzdWx0LnRyZW5kKV0ubWF4KCk6LjFmfV1cIilcbiAgICBwcmludChmXCIgIFNlYXNvbmFsIHJhbmdlOiBbe3Jlc3VsdC5zZWFzb25hbC5taW4oKTouM2Z9LCB7cmVzdWx0LnNlYXNvbmFsLm1heCgpOi4zZn1dXCIpXG4gICAgcHJpbnQoZlwiICBSZXNpZHVhbCBzdGQ6ICAge3Jlc2lkLnN0ZCgpOi4zZn0gIG1lYW46IHtyZXNpZC5tZWFuKCk6LjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyZW5kIEVzdGltYXRpb24gdmlhIENlbnRlcmVkIE1vdmluZyBBdmVyYWdlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2xhc3NpY2FsIG1ldGhvZCBlc3RpbWF0ZXMgdHJlbmQgdXNpbmcgYSBjZW50ZXJlZCBtb3ZpbmcgYXZlcmFnZSBvZiBsZW5ndGggZXF1YWwgdG8gdGhlIHNlYXNvbmFsIHBlcmlvZCBQLiBGb3IgZXZlbiBQIChlLmcuLCBtb250aGx5IFAgPSAxMiksIGEgMsOXMTIgTUEgaXMgdXNlZDogZmlyc3QgYSAxMi1NQSwgdGhlbiBhIDItTUEgb2YgdGhhdCwgcmVzdWx0aW5nIGluIGEgY2VudGVyZWQgZXN0aW1hdGUuIFRoZSBNQSB3ZWlnaHRzIG91dCB0aGUgc2Vhc29uYWwgZmx1Y3R1YXRpb25zLCBiZWNhdXNlIHN1bW1pbmcgZXhhY3RseSBvbmUgZnVsbCBzZWFzb25hbCBjeWNsZSBhdmVyYWdlcyB0aGVtIHRvIHplcm8uIFRoZSByZXN1bHRpbmcgdHJlbmQgZXN0aW1hdGUgaXMgc21vb3RoIGJ1dCBsb3NlcyBQLzIgb2JzZXJ2YXRpb25zIGF0IGVhY2ggZW5kIChib3VuZGFyeSBlZmZlY3QpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxubnAucmFuZG9tLnNlZWQoMSlcbm4gPSAxMjBcbnQgPSBucC5hcmFuZ2UobilcbnRyZW5kX3RydWUgPSA1MCArIDAuMyAqIHRcbnNlYXNvbiA9IDggKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDEyKVxueSA9IHRyZW5kX3RydWUgKyBzZWFzb24gKyAyICogbnAucmFuZG9tLnJhbmRuKG4pXG5cbmRlZiBjZW50ZXJlZF9tYSh4LCBwZXJpb2QpOlxuICAgIFwiXCJcIkNlbnRlcmVkIG1vdmluZyBhdmVyYWdlIGZvciB0cmVuZCBlc3RpbWF0aW9uLlwiXCJcIlxuICAgIGlmIHBlcmlvZCAlIDIgPT0gMTpcbiAgICAgICAgdyA9IG5wLm9uZXMocGVyaW9kKSAvIHBlcmlvZFxuICAgIGVsc2U6XG4gICAgICAgICMgMnhQIE1BIGZvciBldmVuIHBlcmlvZHNcbiAgICAgICAgdyA9IG5wLm9uZXMocGVyaW9kICsgMSkgLyBwZXJpb2RcbiAgICAgICAgd1swXSA9IDAuNSAvIHBlcmlvZFxuICAgICAgICB3Wy0xXSA9IDAuNSAvIHBlcmlvZFxuICAgIGhhbGYgPSBsZW4odykgLy8gMlxuICAgIHRyZW5kID0gbnAuY29udm9sdmUoeCwgd1s6Oi0xXSwgbW9kZT1cdTAwMjd2YWxpZFx1MDAyNylcbiAgICBwYWQgPSBucC5mdWxsKGhhbGYsIG5wLm5hbilcbiAgICByZXR1cm4gbnAuY29uY2F0ZW5hdGUoW3BhZCwgdHJlbmQsIHBhZF0pXG5cbnRyZW5kX21hID0gY2VudGVyZWRfbWEoeSwgcGVyaW9kPTEyKVxudmFsaWQgPSB+bnAuaXNuYW4odHJlbmRfbWEpXG5ybXNlID0gbnAuc3FydChucC5tZWFuKCh0cmVuZF9tYVt2YWxpZF0gLSB0cmVuZF90cnVlW3ZhbGlkXSkqKjIpKVxucHJpbnQoZlwiVHJlbmQgTUEgUk1TRSB2cyB0cnVlIHRyZW5kOiB7cm1zZTouNGZ9XCIpXG5wcmludChmXCJCb3JkZXIgTmFOcyBhdCBlYWNoIGVuZDogICAgIHsofnZhbGlkKS5zdW0oKSAvLyAyfSBvYnNlcnZhdGlvbnNcIilcbnByaW50KFwiQ2xhc3NpY2FsIE1BIHRyZW5kIGxvc2VzIGVuZHBvaW50cyAtLSB1c2UgU1RMIG9yIEhQIGZpbHRlciB0byBhdm9pZCB0aGlzLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlYXNvbmFsIENvbXBvbmVudCBhbmQgRGVzZWFzb25hbGlzYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFmdGVyIGV4dHJhY3RpbmcgdGhlIHRyZW5kLCB0aGUgZGV0cmVuZGVkIHNlcmllcyB54oKcIOKIkiBU4oKcIChhZGRpdGl2ZSkgb3IgeeKCnC9U4oKcIChtdWx0aXBsaWNhdGl2ZSkgaXMgYXZlcmFnZWQgYnkgcG9zaXRpb24gd2l0aGluIHRoZSBzZWFzb25hbCBjeWNsZSAoZS5nLiwgYWxsIEphbnVhcmllcywgYWxsIEZlYnJ1YXJpZXMpIHRvIG9idGFpbiByYXcgc2Vhc29uYWwgZmFjdG9ycy4gVGhlc2UgYXJlIHRoZW4gbm9ybWFsaXNlZCB0byBzdW0gdG8gemVybyAoYWRkaXRpdmUpIG9yIGF2ZXJhZ2UgdG8gb25lIChtdWx0aXBsaWNhdGl2ZSkgb3ZlciBhIGZ1bGwgcGVyaW9kLiBUaGUgcmVzdWx0aW5nIHNlYXNvbmFsIGNvbXBvbmVudCBoYXMgdGhlIHNhbWUgdmFsdWUgZm9yIGV2ZXJ5IEphbnVhcnksIGV2ZXJ5IEZlYnJ1YXJ5LCBldGMuLCBtYWtpbmcgaXQgYSBmaXhlZCBwYXR0ZXJuLiBSZXNpZHVhbHMgYXJlIHdoYXQgcmVtYWlucyBhZnRlciByZW1vdmluZyB0cmVuZCBhbmQgc2Vhc29uYWxpdHkuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTZWFzb25hbCBmYWN0b3JzIHN1bSB0byB6ZXJvIChhZGRpdGl2ZSkgb3IgYXZlcmFnZSB0byBvbmUgKG11bHRpcGxpY2F0aXZlKSBvdmVyIG9uZSBjb21wbGV0ZSBjeWNsZSDigJQgbm9ybWFsaXNhdGlvbiBlbmZvcmNlcyB0aGlzLiIsIkNsYXNzaWNhbCBkZWNvbXBvc2l0aW9uIGFzc3VtZXMgYSBzaW5nbGUgZml4ZWQgc2Vhc29uYWwgcGF0dGVybiBhY3Jvc3MgdGhlIGVudGlyZSBzZXJpZXMg4oCUIG5vIHllYXItdG8teWVhciBldm9sdXRpb24uIiwiVGhlIHNlYXNvbmFsbHkgYWRqdXN0ZWQgc2VyaWVzICh54oKcIOKIkiBT4oKcIG9yIHnigpwvU+KCnCkgaXNvbGF0ZXMgdGhlIHRyZW5kLWN5Y2xlIGFuZCBpcyB1c2VkIGluIG9mZmljaWFsIGVjb25vbWljIHN0YXRpc3RpY3MuIiwiT3Zlci1zbW9vdGhpbmcgdGhlIHRyZW5kICh0b28gd2lkZSBhIE1BIHdpbmRvdykgYWJzb3JicyBzZWFzb25hbCB2YXJpYXRpb24gaW50byB0aGUgcmVzaWR1YWwgcmF0aGVyIHRoYW4gdGhlIHNlYXNvbmFsIGNvbXBvbmVudC4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVzaWR1YWwgQUNGIOKAlCBDaGVja2luZyBEZWNvbXBvc2l0aW9uIFF1YWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgd2VsbC1zcGVjaWZpZWQgZGVjb21wb3NpdGlvbiBsZWF2ZXMgcmVzaWR1YWxzIHRoYXQgYmVoYXZlIGxpa2Ugd2hpdGUgbm9pc2U6IHplcm8gbWVhbiwgY29uc3RhbnQgdmFyaWFuY2UsIGFuZCBubyBzaWduaWZpY2FudCBhdXRvY29ycmVsYXRpb24uIFBsb3R0aW5nIHRoZSBBQ0Ygb2YgdGhlIHJlc2lkdWFscyByZXZlYWxzIHJlbWFpbmluZyBzdHJ1Y3R1cmUuIFNwaWtlcyBhdCB0aGUgc2Vhc29uYWwgbGFnIChrID0gUCwgMlAsIOKApikgaW5kaWNhdGUgdGhlIHNlYXNvbmFsIGNvbXBvbmVudCB3YXMgbm90IGZ1bGx5IGNhcHR1cmVkLiBTcGlrZXMgYXQgbG93IGxhZ3MgaW5kaWNhdGUgdGhlIHRyZW5kIHdhcyBpbnN1ZmZpY2llbnRseSBzbW9vdGhlZC4gVGhlIExqdW5nLUJveCB0ZXN0IHByb3ZpZGVzIGEgZm9ybWFsIHRlc3QgZm9yIHJlc2lkdWFsIGF1dG9jb3JyZWxhdGlvbiB1cCB0byBsYWcgaC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zZWFzb25hbCBpbXBvcnQgc2Vhc29uYWxfZGVjb21wb3NlXG5mcm9tIHN0YXRzbW9kZWxzLnN0YXRzLmRpYWdub3N0aWMgaW1wb3J0IGFjb3JyX2xqdW5nYm94XG5mcm9tIHN0YXRzbW9kZWxzLmdyYXBoaWNzLnRzYXBsb3RzIGltcG9ydCBwbG90X2FjZlxuXG5ucC5yYW5kb20uc2VlZCgyKVxubiA9IDEyMFxudCA9IG5wLmFyYW5nZShuKVxueSA9IDUwICsgMC4zKnQgKyA4Km5wLnNpbigyKm5wLnBpKnQvMTIpICsgMipucC5yYW5kb20ucmFuZG4obilcblxucmVzdWx0ID0gc2Vhc29uYWxfZGVjb21wb3NlKHksIG1vZGVsPVx1MDAyN2FkZGl0aXZlXHUwMDI3LCBwZXJpb2Q9MTIpXG5yZXNpZCA9IHJlc3VsdC5yZXNpZC5kcm9wbmEoKVxuXG4jIEFDRiBhdCBzZWFzb25hbCBsYWdzXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0dG9vbHMgaW1wb3J0IGFjZlxuYWNmX3ZhbHMgPSBhY2YocmVzaWQsIG5sYWdzPTI0KVxucHJpbnQoXCJSZXNpZHVhbCBBQ0YgYXQgc2Vhc29uYWwgbGFnczpcIilcbmZvciBsYWcgaW4gWzEyLCAyNF06XG4gICAgcHJpbnQoZlwiICBsYWcge2xhZzoyZH06IHthY2ZfdmFsc1tsYWddOi40Zn1cIilcblxuIyBManVuZy1Cb3ggdGVzdFxubGIgPSBhY29ycl9sanVuZ2JveChyZXNpZCwgbGFncz1bMTIsIDI0XSwgcmV0dXJuX2RmPVRydWUpXG5wcmludChcIlxcbkxqdW5nLUJveCB0ZXN0IG9uIHJlc2lkdWFsczpcIilcbnByaW50KGxiW1tcdTAwMjdsYl9zdGF0XHUwMDI3LCBcdTAwMjdsYl9wdmFsdWVcdTAwMjddXS50b19zdHJpbmcoKSlcbnByaW50KFwiXFxucCBcdTAwM2UgMC4wNTogcmVzaWR1YWxzIGNvbnNpc3RlbnQgd2l0aCB3aGl0ZSBub2lzZSAoZ29vZCBkZWNvbXBvc2l0aW9uKVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhQIEZpbHRlciBmb3IgVHJlbmQgRXh0cmFjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEhvZHJpY2stUHJlc2NvdHQgKEhQKSBmaWx0ZXIgZGVjb21wb3NlcyB54oKcIGludG8gdHJlbmQgz4TigpwgYW5kIGN5Y2xlIGPigpwgPSB54oKcIOKIkiDPhOKCnCBieSBtaW5pbWlzaW5nIHRoZSBsb3NzIGZ1bmN0aW9uIM6jKHnigpwg4oiSIM+E4oKcKcKyICsgzrvCt86jWyjPhOKCnOKCiuKCgSDiiJIgz4TigpwpIOKIkiAoz4Tigpwg4oiSIM+E4oKc4oKL4oKBKV3Csi4gVGhlIGZpcnN0IHRlcm0gZml0cyB0aGUgdHJlbmQgdG8gdGhlIGRhdGE7IHRoZSBzZWNvbmQgdGVybSBwZW5hbGlzZXMgY2hhbmdlcyBpbiB0aGUgdHJlbmQgZ3Jvd3RoIHJhdGUgKHNlY29uZCBkaWZmZXJlbmNlcykuIExhcmdlciDOuyBwcm9kdWNlcyBhIHNtb290aGVyLCBtb3JlIHNsb3dseSBjaGFuZ2luZyB0cmVuZC4gVGhlIHN0YW5kYXJkIM67IHZhbHVlcyBhcmUgMTYwMCBmb3IgcXVhcnRlcmx5IGRhdGEgYW5kIDEyOTYwMCBmb3IgbW9udGhseSBkYXRhLCBiYXNlZCBvbiB0aGUgYXNzdW1wdGlvbiB0aGF0IHRoZSBidXNpbmVzcyBjeWNsZSBoYXMgOMOXIHRoZSB2YXJpYW5jZSBvZiB0aGUgdHJlbmQgY29tcG9uZW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc3RhdHNtb2RlbHMudHNhLmZpbHRlcnMuaHBfZmlsdGVyIGltcG9ydCBocGZpbHRlclxuXG5ucC5yYW5kb20uc2VlZCgzKVxubiA9IDEyMFxudCA9IG5wLmFyYW5nZShuKVxueSA9IDUwICsgMC4yKnQgKyA1Km5wLnNpbigyKm5wLnBpKnQvMTIpICsgMypucC5yYW5kb20ucmFuZG4obilcblxucHJpbnQoZlwie1x1MDAyN0xhbWJkYVx1MDAyNzpcdTAwM2UxMHN9ICB7XHUwMDI3VHJlbmQgc3RkXHUwMDI3Olx1MDAzZTEwc30gIHtcdTAwMjdDeWNsZSBzdGRcdTAwMjc6XHUwMDNlMTBzfSAge1x1MDAyN0N5Y2xlL1RyZW5kIHZhciByYXRpb1x1MDAyNzpcdTAwM2UyMnN9XCIpXG5wcmludChcIi1cIiAqIDYwKVxuXG5mb3IgbGFtIGluIFsxMCwgMTAwLCAxNjAwLCAxMjk2MDBdOlxuICAgIGN5Y2xlLCB0cmVuZCA9IGhwZmlsdGVyKHksIGxhbWI9bGFtKVxuICAgIHJhdGlvID0gY3ljbGUudmFyKCkgLyB0cmVuZC52YXIoKVxuICAgIHByaW50KGZcIntsYW06MTAuMGZ9ICB7dHJlbmQuc3RkKCk6MTAuNGZ9ICB7Y3ljbGUuc3RkKCk6MTAuNGZ9ICB7cmF0aW86MjIuNGZ9XCIpXG5cbnByaW50KFwiXFxubGFtYmRhPTE2MDA6IHN0YW5kYXJkIHF1YXJ0ZXJseTsgbGFtYmRhPTEyOTYwMDogc3RhbmRhcmQgbW9udGhseVwiKVxucHJpbnQoXCJMYXJnZXIgbGFtYmRhID1cdTAwM2Ugc21vb3RoZXIgdHJlbmQgPVx1MDAzZSBtb3JlIHZhcmlhbmNlIGF0dHJpYnV0ZWQgdG8gY3ljbGVcIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkFkZGl0aXZlIHZzIE11bHRpcGxpY2F0aXZlOiBIb3cgdG8gQ2hvb3NlIiwiY29udGVudCI6IlBsb3QgdGhlIHNlcmllcy4gSWYgdGhlIHNlYXNvbmFsIHN3aW5ncyBncm93IHByb3BvcnRpb25hbGx5IHdpdGggdGhlIHRyZW5kIGxldmVsLCB1c2UgbXVsdGlwbGljYXRpdmUgZGVjb21wb3NpdGlvbiAob3IgbG9nLXRyYW5zZm9ybSB0byBhZGRpdGl2ZSkuIElmIHRoZSBzd2luZ3Mgc3RheSByb3VnaGx5IGNvbnN0YW50IHJlZ2FyZGxlc3Mgb2YgdGhlIGxldmVsLCB1c2UgYWRkaXRpdmUuIEEgcXVpY2sgZGlhZ25vc3RpYzogcGxvdCB0aGUgc2Vhc29uYWwgY29tcG9uZW50IGZyb20gYWRkaXRpdmUgZGVjb21wb3NpdGlvbiBhbmQgY2hlY2sgaWYgaXRzIGFtcGxpdHVkZSBncm93cyBvdmVyIHRpbWUg4oCUIGlmIGl0IGRvZXMsIHN3aXRjaCB0byBtdWx0aXBsaWNhdGl2ZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZWNvbXBvc2l0aW9uIE1ldGhvZHMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJTZWFzb25hbGl0eSBUeXBlIiwiTXVsdGlwbGUgU2Vhc29ucyIsIlJvYnVzdCB0byBPdXRsaWVycyIsIkhhbmRsZXMgQ2hhbmdpbmcgU2Vhc29uYWxpdHkiLCJJbXBsZW1lbnRhdGlvbiJdLCJyb3dzIjpbWyJDbGFzc2ljYWwgKE1BLWJhc2VkKSIsIkFkZGl0aXZlIG9yIG11bHRpcGxpY2F0aXZlIiwiTm8iLCJObyIsIk5vIOKAlCBmaXhlZCBzZWFzb25hbCBmYWN0b3JzIiwic3RhdHNtb2RlbHMgc2Vhc29uYWxfZGVjb21wb3NlIl0sWyJYLTEzQVJJTUEtU0VBVFMiLCJBZGRpdGl2ZSBvciBtdWx0aXBsaWNhdGl2ZSIsIk5vIiwiUGFydGlhbCAodmlhIEFSSU1BIG91dGxpZXIgZGV0ZWN0aW9uKSIsIlBhcnRpYWwgKGV2b2x2aW5nIHNlYXNvbmFsaXR5IHZpYSByZWdBUklNQSkiLCJzdGF0c21vZGVscyB4MTNfYXJpbWFfYW5hbHlzaXMiXSxbIlNUTCAoTE9FU1MtYmFzZWQpIiwiQWRkaXRpdmUgKGxvZyBmb3IgbXVsdGlwbGljYXRpdmUpIiwiTm8gKE1TVEwgZm9yIG11bHRpcGxlKSIsIlllcyDigJQgcm9idXN0IG9wdGlvbiIsIlllcyDigJQgTE9FU1Mgd2luZG93IGFkYXB0cyIsInN0YXRzbW9kZWxzIFNUTCJdLFsiU1RMICsgRVRTL0FSSU1BIiwiQWRkaXRpdmUiLCJZZXMgKHZpYSBNU1RMKSIsIlllcyIsIlllcyIsInN0YXRzZm9yZWNhc3QgKE5peHRsYSkiXSxbIlByb3BoZXQiLCJBZGRpdGl2ZSBvciBtdWx0aXBsaWNhdGl2ZSIsIlllcyAoZGFpbHkrd2Vla2x5K3llYXJseSkiLCJQYXJ0aWFsIChMYXBsYWNlIHByaW9yKSIsIlllcyDigJQgRm91cmllciBzZXJpZXMgc2Vhc29uYWxpdHkiLCJwcm9waGV0IChNZXRhKSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIFdvcmtmbG93IGZvciBEZWNvbXBvc2l0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHByYWN0aWNhbCB3b3JrZmxvdzogKDEpIHBsb3QgdGhlIHJhdyBzZXJpZXMgYW5kIGNoZWNrIHdoZXRoZXIgc2Vhc29uYWwgYW1wbGl0dWRlIGdyb3dzIHdpdGggdGhlIHRyZW5kIGxldmVsIChtdWx0aXBsaWNhdGl2ZSkgb3Igc3RheXMgY29uc3RhbnQgKGFkZGl0aXZlKTsgKDIpIGFwcGx5IFNUTCB3aXRoIHJvYnVzdD1UcnVlIGZvciBpbml0aWFsIGRlY29tcG9zaXRpb247ICgzKSBpbnNwZWN0IHJlc2lkdWFsIEFDRiDigJQgYWxsIGxhZ3MgaW5zaWRlIHRoZSDCsTEuOTYv4oiabiBiYW5kIGFuZCBManVuZy1Cb3ggcCBcdTAwM2UgMC4wNSBjb25maXJtIHdoaXRlIG5vaXNlOyAoNCkgZm9yIGZvcmVjYXN0aW5nLCBmaXQgRVRTIG9yIEFSSU1BIHRvIHRoZSB0cmVuZC1jeWNsZSArIHJlc2lkdWFsLCBwcm9qZWN0IHRoZSBzZWFzb25hbCBjb21wb25lbnQgZm9yd2FyZCwgYW5kIHJlY29tYmluZS4gVGhpcyBTVEwgKyBBUklNQS9FVFMgcGlwZWxpbmUgaXMgY29tcGV0aXRpdmUgb24gTTQtY29tcGV0aXRpb24gYmVuY2htYXJrcy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Trend, Seasonality, and Residual — Additive vs Multiplicative

Time-series decomposition separates an observed sequence into interpretable components: a long-run trend, a repeating seasonal pattern, and a residual that captures irregular shocks. Decomposition serves two purposes: it makes each component easy to model separately, and it provides diagnostics about the nature of seasonality (additive vs multiplicative) that inform the choice of forecasting model. Classical decomposition is the simplest approach; modern methods like STL and X-13ARIMA-SEATS extend it substantially.

## Additive and Multiplicative Schemes

In the additive model yₜ = Tₜ + Sₜ + Rₜ, the seasonal amplitude is constant regardless of the level. A retailer whose Christmas peak is always exactly 1000 units above the trend follows an additive pattern. In the multiplicative model yₜ = Tₜ · Sₜ · Rₜ, the seasonal swing scales proportionally with the trend level — a series that doubles in level also doubles its seasonal peak-to-trough range. Taking logarithms of a multiplicative series converts it to additive: log(yₜ) = log(Tₜ) + log(Sₜ) + log(Rₜ).

```python
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

np.random.seed(0)
n = 120  # 10 years of monthly data
t = np.arange(n)

# Additive: constant seasonal amplitude
trend_add = 50 + 0.3 * t
season_add = 10 * np.sin(2 * np.pi * t / 12)
y_add = trend_add + season_add + 2 * np.random.randn(n)

# Multiplicative: seasonal amplitude grows with trend
trend_mult = 50 + 0.4 * t
season_mult = 1 + 0.3 * np.sin(2 * np.pi * t / 12)
y_mult = trend_mult * season_mult * np.exp(0.05 * np.random.randn(n))

for label, y, model in [("Additive", y_add, "additive"), ("Multiplicative", y_mult, "multiplicative")]:
    result = seasonal_decompose(y, model=model, period=12)
    resid = result.resid[~np.isnan(result.resid)]
    print(f"\n{label} decomposition")
    print(f"  Trend range:    [{result.trend[~np.isnan(result.trend)].min():.1f}, {result.trend[~np.isnan(result.trend)].max():.1f}]")
    print(f"  Seasonal range: [{result.seasonal.min():.3f}, {result.seasonal.max():.3f}]")
    print(f"  Residual std:   {resid.std():.3f}  mean: {resid.mean():.4f}")
```

## Trend Estimation via Centered Moving Average

The classical method estimates trend using a centered moving average of length equal to the seasonal period P. For even P (e.g., monthly P = 12), a 2×12 MA is used: first a 12-MA, then a 2-MA of that, resulting in a centered estimate. The MA weights out the seasonal fluctuations, because summing exactly one full seasonal cycle averages them to zero. The resulting trend estimate is smooth but loses P/2 observations at each end (boundary effect).

```python
import numpy as np

np.random.seed(1)
n = 120
t = np.arange(n)
trend_true = 50 + 0.3 * t
season = 8 * np.sin(2 * np.pi * t / 12)
y = trend_true + season + 2 * np.random.randn(n)

def centered_ma(x, period):
    """Centered moving average for trend estimation."""
    if period % 2 == 1:
        w = np.ones(period) / period
    else:
        # 2xP MA for even periods
        w = np.ones(period + 1) / period
        w[0] = 0.5 / period
        w[-1] = 0.5 / period
    half = len(w) // 2
    trend = np.convolve(x, w[::-1], mode='valid')
    pad = np.full(half, np.nan)
    return np.concatenate([pad, trend, pad])

trend_ma = centered_ma(y, period=12)
valid = ~np.isnan(trend_ma)
rmse = np.sqrt(np.mean((trend_ma[valid] - trend_true[valid])**2))
print(f"Trend MA RMSE vs true trend: {rmse:.4f}")
print(f"Border NaNs at each end:     {(~valid).sum() // 2} observations")
print("Classical MA trend loses endpoints -- use STL or HP filter to avoid this.")
```

## Seasonal Component and Deseasonalisation

After extracting the trend, the detrended series yₜ − Tₜ (additive) or yₜ/Tₜ (multiplicative) is averaged by position within the seasonal cycle (e.g., all Januaries, all Februaries) to obtain raw seasonal factors. These are then normalised to sum to zero (additive) or average to one (multiplicative) over a full period. The resulting seasonal component has the same value for every January, every February, etc., making it a fixed pattern. Residuals are what remains after removing trend and seasonality.

- Seasonal factors sum to zero (additive) or average to one (multiplicative) over one complete cycle — normalisation enforces this.
- Classical decomposition assumes a single fixed seasonal pattern across the entire series — no year-to-year evolution.
- The seasonally adjusted series (yₜ − Sₜ or yₜ/Sₜ) isolates the trend-cycle and is used in official economic statistics.
- Over-smoothing the trend (too wide a MA window) absorbs seasonal variation into the residual rather than the seasonal component.

## Residual ACF — Checking Decomposition Quality

A well-specified decomposition leaves residuals that behave like white noise: zero mean, constant variance, and no significant autocorrelation. Plotting the ACF of the residuals reveals remaining structure. Spikes at the seasonal lag (k = P, 2P, …) indicate the seasonal component was not fully captured. Spikes at low lags indicate the trend was insufficiently smoothed. The Ljung-Box test provides a formal test for residual autocorrelation up to lag h.

```python
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_acf

np.random.seed(2)
n = 120
t = np.arange(n)
y = 50 + 0.3*t + 8*np.sin(2*np.pi*t/12) + 2*np.random.randn(n)

result = seasonal_decompose(y, model='additive', period=12)
resid = result.resid.dropna()

# ACF at seasonal lags
from statsmodels.tsa.stattools import acf
acf_vals = acf(resid, nlags=24)
print("Residual ACF at seasonal lags:")
for lag in [12, 24]:
    print(f"  lag {lag:2d}: {acf_vals[lag]:.4f}")

# Ljung-Box test
lb = acorr_ljungbox(resid, lags=[12, 24], return_df=True)
print("\nLjung-Box test on residuals:")
print(lb[['lb_stat', 'lb_pvalue']].to_string())
print("\np > 0.05: residuals consistent with white noise (good decomposition)")
```

## HP Filter for Trend Extraction

The Hodrick-Prescott (HP) filter decomposes yₜ into trend τₜ and cycle cₜ = yₜ − τₜ by minimising the loss function Σ(yₜ − τₜ)² + λ·Σ[(τₜ₊₁ − τₜ) − (τₜ − τₜ₋₁)]². The first term fits the trend to the data; the second term penalises changes in the trend growth rate (second differences). Larger λ produces a smoother, more slowly changing trend. The standard λ values are 1600 for quarterly data and 129600 for monthly data, based on the assumption that the business cycle has 8× the variance of the trend component.

```python
import numpy as np
from statsmodels.tsa.filters.hp_filter import hpfilter

np.random.seed(3)
n = 120
t = np.arange(n)
y = 50 + 0.2*t + 5*np.sin(2*np.pi*t/12) + 3*np.random.randn(n)

print(f"{'Lambda':>10s}  {'Trend std':>10s}  {'Cycle std':>10s}  {'Cycle/Trend var ratio':>22s}")
print("-" * 60)

for lam in [10, 100, 1600, 129600]:
    cycle, trend = hpfilter(y, lamb=lam)
    ratio = cycle.var() / trend.var()
    print(f"{lam:10.0f}  {trend.std():10.4f}  {cycle.std():10.4f}  {ratio:22.4f}")

print("\nlambda=1600: standard quarterly; lambda=129600: standard monthly")
print("Larger lambda => smoother trend => more variance attributed to cycle")
```

> **Additive vs Multiplicative: How to Choose**: Plot the series. If the seasonal swings grow proportionally with the trend level, use multiplicative decomposition (or log-transform to additive). If the swings stay roughly constant regardless of the level, use additive. A quick diagnostic: plot the seasonal component from additive decomposition and check if its amplitude grows over time — if it does, switch to multiplicative.

## Decomposition Methods Comparison

| Method | Seasonality Type | Multiple Seasons | Robust to Outliers | Handles Changing Seasonality | Implementation |
| --- | --- | --- | --- | --- | --- |
| Classical (MA-based) | Additive or multiplicative | No | No | No — fixed seasonal factors | statsmodels seasonal_decompose |
| X-13ARIMA-SEATS | Additive or multiplicative | No | Partial (via ARIMA outlier detection) | Partial (evolving seasonality via regARIMA) | statsmodels x13_arima_analysis |
| STL (LOESS-based) | Additive (log for multiplicative) | No (MSTL for multiple) | Yes — robust option | Yes — LOESS window adapts | statsmodels STL |
| STL + ETS/ARIMA | Additive | Yes (via MSTL) | Yes | Yes | statsforecast (Nixtla) |
| Prophet | Additive or multiplicative | Yes (daily+weekly+yearly) | Partial (Laplace prior) | Yes — Fourier series seasonality | prophet (Meta) |

## Practical Workflow for Decomposition

A practical workflow: (1) plot the raw series and check whether seasonal amplitude grows with the trend level (multiplicative) or stays constant (additive); (2) apply STL with robust=True for initial decomposition; (3) inspect residual ACF — all lags inside the ±1.96/√n band and Ljung-Box p > 0.05 confirm white noise; (4) for forecasting, fit ETS or ARIMA to the trend-cycle + residual, project the seasonal component forward, and recombine. This STL + ARIMA/ETS pipeline is competitive on M4-competition benchmarks.

---

