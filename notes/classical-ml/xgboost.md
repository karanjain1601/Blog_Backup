---
title: "XGBoost — Second-Order Taylor Expansion and Regularization"
slug: "xgboost"
description: "XGBoost's principled objective function with L1/L2 regularization, second-order Taylor expansion for exact leaf weights, split gain formula, approximate histogram splits, and sparsity-aware training."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlhHQm9vc3QgT2JqZWN0aXZlIEZ1bmN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJYR0Jvb3N0IChDaGVuIFx1MDAyNiBHdWVzdHJpbiAyMDE2KSBmcmFtZXMgdHJlZSBib29zdGluZyBhcyBleHBsaWNpdCByZWd1bGFyaXNlZCBvYmplY3RpdmUgbWluaW1pc2F0aW9uOiBPYmogPSDOo+G1oiBsKHnhtaIsIMW34bWiKSArIM6j4oKWIM6pKGbigpYpIHdoZXJlIM6pKGYpID0gzrNUICsgKM67LzIpzqPisbwgd+KxvMKyIHBlbmFsaXNlcyB0cmVlIGNvbXBsZXhpdHkuIM6zIGlzIGEgbWluaW11bSBnYWluIHRocmVzaG9sZCBwZXIgbmV3IGxlYWYgKEwxLXN0eWxlIG9uIHRyZWUgc3RydWN0dXJlKTsgzrsgaXMgTDIgcmVndWxhcmlzYXRpb24gb24gbGVhZiB3ZWlnaHRzLiBUaGlzIGV4cGxpY2l0IHBlbmFsdHkgcHJldmVudHMgb3ZlcmZpdHRpbmcgYW5kIGlzIGtleSB0byBYR0Jvb3N0XHUwMDI3cyBzdXBlcmlvciBnZW5lcmFsaXNhdGlvbiBvdmVyIHZhbmlsbGEgZ3JhZGllbnQgYm9vc3RpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2Vjb25kLU9yZGVyIFRheWxvciBFeHBhbnNpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF0IHN0ZXAgbSwgWEdCb29zdCBhcHByb3hpbWF0ZXMgdGhlIGxvc3MgdXNpbmcgYSBzZWNvbmQtb3JkZXIgVGF5bG9yIGV4cGFuc2lvbiBhcm91bmQgdGhlIGN1cnJlbnQgcHJlZGljdGlvbiBGX3ttLTF9OiBMIOKJiCDOo+G1oiBbZ+G1oiBo4oKYKHjhtaIpICsgKDEvMikgaOG1oiBo4oKYKHjhtaIpwrJdICsgzqkoaOKCmCkgd2hlcmUgZ+G1oiA9IOKIgmwv4oiCRiAoZmlyc3QgZGVyaXZhdGl2ZSkgYW5kIGjhtaIgPSDiiILCsmwv4oiCRsKyIChzZWNvbmQgZGVyaXZhdGl2ZSAvIEhlc3NpYW4pLiBGb3IgYSBsZWFmIGogY29sbGVjdGluZyBpbnN0YW5jZXMgSV9qLCB0aGUgb3B0aW1hbCBsZWFmIHdlaWdodCBpcyB34rG8KiA9IOKIkkfisbwvKEjisbwrzrspIHdoZXJlIEfisbwgPSDOo+G1ouKIiElfaiBn4bWiIGFuZCBI4rG8ID0gzqPhtaLiiIhJX2ogaOG1oi4gVGhlIHNlY29uZC1vcmRlciBleHBhbnNpb24gZW5hYmxlcyBmYXN0ZXIsIG1vcmUgYWNjdXJhdGUgb3B0aW1pc2F0aW9uIHRoYW4gdGhlIGZpcnN0LW9yZGVyIGFwcHJvYWNoIHVzZWQgYnkgdmFuaWxsYSBHQi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHhnYm9vc3QgYXMgeGdiXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9yZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCB0cmFpbl90ZXN0X3NwbGl0XG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgbWVhbl9zcXVhcmVkX2Vycm9yXG5cbiMgQ3VzdG9tIG9iamVjdGl2ZTogTVNFIOKAlCBmaXJzdCBkZXJpdmF0aXZlID0gcHJlZCAtIHksIHNlY29uZCA9IDFcbmRlZiBtc2Vfb2JqKHlfcHJlZCwgZHRyYWluKTpcbiAgICB5X3RydWUgPSBkdHJhaW4uZ2V0X2xhYmVsKClcbiAgICBncmFkID0geV9wcmVkIC0geV90cnVlICAgICAgICAgICAjIGdfaSA9IGZpcnN0IGRlcml2YXRpdmUgb2YgTVNFXG4gICAgaGVzcyA9IG5wLm9uZXNfbGlrZSh5X3ByZWQpICAgICAgIyBoX2kgPSBzZWNvbmQgZGVyaXZhdGl2ZSA9IDEgKGNvbnN0YW50KVxuICAgIHJldHVybiBncmFkLCBoZXNzXG5cbmRlZiBybXNlX2V2YWwoeV9wcmVkLCBkdHJhaW4pOlxuICAgIHlfdHJ1ZSA9IGR0cmFpbi5nZXRfbGFiZWwoKVxuICAgIHJldHVybiBcdTAwMjdybXNlXHUwMDI3LCBmbG9hdChucC5zcXJ0KG1lYW5fc3F1YXJlZF9lcnJvcih5X3RydWUsIHlfcHJlZCkpKVxuXG5YLCB5ID0gbWFrZV9yZWdyZXNzaW9uKG5fc2FtcGxlcz0xMDAwLCBuX2ZlYXR1cmVzPTIwLCBub2lzZT0xNSwgcmFuZG9tX3N0YXRlPTQyKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxuXG5kdHJhaW4gPSB4Z2IuRE1hdHJpeChYX3RyLCBsYWJlbD15X3RyKVxuZHRlc3QgID0geGdiLkRNYXRyaXgoWF90ZSwgbGFiZWw9eV90ZSlcblxucGFyYW1zID0ge1x1MDAyN21heF9kZXB0aFx1MDAyNzogNCwgXHUwMDI3ZXRhXHUwMDI3OiAwLjEsIFx1MDAyN3NlZWRcdTAwMjc6IDQyLCBcdTAwMjd2ZXJib3NpdHlcdTAwMjc6IDB9XG5ldmFsc19yZXN1bHQgPSB7fVxubW9kZWwgPSB4Z2IudHJhaW4ocGFyYW1zLCBkdHJhaW4sIG51bV9ib29zdF9yb3VuZD0xNTAsXG4gICAgICAgICAgICAgICAgICBvYmo9bXNlX29iaiwgY3VzdG9tX21ldHJpYz1ybXNlX2V2YWwsXG4gICAgICAgICAgICAgICAgICBldmFscz1bKGR0cmFpbixcdTAwMjd0cmFpblx1MDAyNyksKGR0ZXN0LFx1MDAyN3Rlc3RcdTAwMjcpXSxcbiAgICAgICAgICAgICAgICAgIGV2YWxzX3Jlc3VsdD1ldmFsc19yZXN1bHQsIHZlcmJvc2VfZXZhbD0zMClcbnByZWRzID0gbW9kZWwucHJlZGljdChkdGVzdClcbnByaW50KGZcdTAwMjdGaW5hbCBSTVNFOiB7bnAuc3FydChtZWFuX3NxdWFyZWRfZXJyb3IoeV90ZSwgcHJlZHMpKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9wdGltYWwgU3BsaXQgR2FpbiBGb3JtdWxhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZ2FpbiBmcm9tIHNwbGl0dGluZyBub2RlIEkgaW50byBsZWZ0IElfTCBhbmQgcmlnaHQgSV9SIGlzOiBHYWluID0gKDEvMilbR19MwrIvKEhfTCvOuykgKyBHX1LCsi8oSF9SK867KSDiiJIgKEdfTCtHX1IpwrIvKEhfTCtIX1IrzrspXSDiiJIgzrMuIFRoZSDOsyB0ZXJtIG1lYW5zIGEgc3BsaXQgaXMgb25seSBtYWRlIGlmIHRoZSBnYWluIGV4Y2VlZHMgdGhlIG1pbmltdW0gdGhyZXNob2xkIOKAlCB0aGlzIGlzIFhHQm9vc3RcdTAwMjdzIGJ1aWx0LWluIHBydW5pbmcuIFRoZSBIZXNzaWFuIGluIHRoZSBkZW5vbWluYXRvciBhY3RzIGFzIGEgY29uZmlkZW5jZSB3ZWlnaHRpbmc6IGluc3RhbmNlcyB3aXRoIGxvdyBjdXJ2YXR1cmUgKGhpZ2ggY2VydGFpbnR5KSBoYXZlIGxlc3MgaW5mbHVlbmNlIG9uIHRoZSBzcGxpdC4gbWluX2NoaWxkX3dlaWdodCBjb250cm9scyB0aGUgbWluaW11bSBzdW0gb2YgSGVzc2lhbnMgYWxsb3dlZCBpbiBhIGxlYWYuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJXaHkgU2Vjb25kLU9yZGVyIE1hdHRlcnMiLCJjb250ZW50IjoiRmlyc3Qtb3JkZXIgbWV0aG9kcyAodmFuaWxsYSBHQikgdHJlYXQgZWFjaCBpbnN0YW5jZSBlcXVhbGx5IGluIHRoZSBncmFkaWVudC4gU2Vjb25kLW9yZGVyIG1ldGhvZHMgd2VpZ2h0IGluc3RhbmNlcyBieSB0aGVpciBIZXNzaWFuIOKAlCBpbnN0YW5jZXMgbmVhciB0aGUgZGVjaXNpb24gYm91bmRhcnkgKGhpZ2ggY3VydmF0dXJlLCB1bmNlcnRhaW4gcHJlZGljdGlvbnMpIGdldCBoaWdoZXIgd2VpZ2h0IHRoYW4gY29uZmlkZW50bHktY2xhc3NpZmllZCBpbnN0YW5jZXMuIFRoaXMgbGVhZHMgdG8gZmFzdGVyIGNvbnZlcmdlbmNlIGFuZCBiZXR0ZXIgbGVhZiB3ZWlnaHQgZXN0aW1hdGVzLCBlc3BlY2lhbGx5IHdpdGggbm9uLU1TRSBsb3NzZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiWEdCQ2xhc3NpZmllciB3aXRoIEVhcmx5IFN0b3BwaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJYR0Jvb3N0XHUwMDI3cyBQeXRob24gQVBJIHN1cHBvcnRzIGVhcmx5IHN0b3BwaW5nOiBpZiB0aGUgdmFsaWRhdGlvbiBtZXRyaWMgZG9lcyBub3QgaW1wcm92ZSBmb3IgZWFybHlfc3RvcHBpbmdfcm91bmRzIGNvbnNlY3V0aXZlIHJvdW5kcywgdHJhaW5pbmcgaGFsdHMgYW5kIGJlc3RfaXRlcmF0aW9uIGlzIHNhdmVkLiBUaGlzIGF1dG9tYXRpY2FsbHkgZmluZHMgdGhlIHJpZ2h0IG5fZXN0aW1hdG9ycyB3aXRob3V0IGdyaWQgc2VhcmNoLiBUaGUgZXZhbF9tZXRyaWMgcGFyYW1ldGVyIHNwZWNpZmllcyB0aGUgdmFsaWRhdGlvbiBtZXRyaWM7IGxvZ2xvc3MsIGF1YywgYW5kIGVycm9yIGFyZSBjb21tb24gY2hvaWNlcyBmb3IgY2xhc3NpZmljYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB4Z2Jvb3N0IGFzIHhnYlxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2JyZWFzdF9jYW5jZXJcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCByb2NfYXVjX3Njb3JlXG5cblgsIHkgPSBsb2FkX2JyZWFzdF9jYW5jZXIocmV0dXJuX1hfeT1UcnVlKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxuWF90cjIsIFhfdmFsLCB5X3RyMiwgeV92YWwgPSB0cmFpbl90ZXN0X3NwbGl0KFhfdHIsIHlfdHIsIHRlc3Rfc2l6ZT0wLjE1LCByYW5kb21fc3RhdGU9NDIpXG5cbmNsZiA9IHhnYi5YR0JDbGFzc2lmaWVyKFxuICAgIG5fZXN0aW1hdG9ycz0xMDAwLFxuICAgIGxlYXJuaW5nX3JhdGU9MC4wNSxcbiAgICBtYXhfZGVwdGg9NCxcbiAgICBtaW5fY2hpbGRfd2VpZ2h0PTUsICAgICAjIG1pbmltdW0gc3VtIG9mIGhlc3NpYW5zIHBlciBsZWFmXG4gICAgc3Vic2FtcGxlPTAuOCxcbiAgICBjb2xzYW1wbGVfYnl0cmVlPTAuOCxcbiAgICByZWdfYWxwaGE9MC4xLCAgICAgICAgICAjIEwxIG9uIGxlYWYgd2VpZ2h0c1xuICAgIHJlZ19sYW1iZGE9MS4wLCAgICAgICAgICMgTDIgb24gbGVhZiB3ZWlnaHRzXG4gICAgZXZhbF9tZXRyaWM9XHUwMDI3YXVjXHUwMDI3LFxuICAgIGVhcmx5X3N0b3BwaW5nX3JvdW5kcz0zMCxcbiAgICByYW5kb21fc3RhdGU9NDIsXG4gICAgdmVyYm9zaXR5PTBcbilcbmNsZi5maXQoWF90cjIsIHlfdHIyLCBldmFsX3NldD1bKFhfdmFsLCB5X3ZhbCldLCB2ZXJib3NlPUZhbHNlKVxucHJpbnQoZlx1MDAyN0Jlc3QgaXRlcmF0aW9uOiB7Y2xmLmJlc3RfaXRlcmF0aW9ufVx1MDAyNylcbmF1YyA9IHJvY19hdWNfc2NvcmUoeV90ZSwgY2xmLnByZWRpY3RfcHJvYmEoWF90ZSlbOiwgMV0pXG5wcmludChmXHUwMDI3VGVzdCBBVUM6IHthdWM6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTSEFQIEludGVncmF0aW9uIHdpdGggWEdCb29zdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiWEdCb29zdCBoYXMgbmF0aXZlIFNIQVAgc3VwcG9ydCB2aWEgdGhlIFRyZWVFeHBsYWluZXIsIGNvbXB1dGluZyBleGFjdCBTaGFwbGV5IHZhbHVlcyBpbiBPKFRMRMKyKSB0aW1lLiBtb2RlbC5wcmVkaWN0KGR0ZXN0LCBwcmVkX2NvbnRyaWJzPVRydWUpIHJldHVybnMgdGhlIFNIQVAgY29udHJpYnV0aW9uIG1hdHJpeCBkaXJlY3RseSBmcm9tIFhHQm9vc3Qgd2l0aG91dCB0aGUgc2VwYXJhdGUgc2hhcCBwYWNrYWdlLiBVc2luZyB0aGUgc2hhcCBwYWNrYWdlIG9uIFhHQm9vc3QgbW9kZWxzIGlzIGFsc28gc2VhbWxlc3MgYW5kIHByb3ZpZGVzIGFsbCBzdGFuZGFyZCB2aXN1YWxpc2F0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHhnYm9vc3QgYXMgeGdiXG5pbXBvcnQgc2hhcFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfYnJlYXN0X2NhbmNlclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuXG5kYXRhID0gbG9hZF9icmVhc3RfY2FuY2VyKClcblgsIHkgPSBkYXRhLmRhdGEsIGRhdGEudGFyZ2V0XG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4yLCByYW5kb21fc3RhdGU9NDIpXG5cbm1vZGVsID0geGdiLlhHQkNsYXNzaWZpZXIoXG4gICAgbl9lc3RpbWF0b3JzPTEwMCwgbWF4X2RlcHRoPTQsIGxlYXJuaW5nX3JhdGU9MC4xLFxuICAgIGV2YWxfbWV0cmljPVx1MDAyN2xvZ2xvc3NcdTAwMjcsIHJhbmRvbV9zdGF0ZT00MiwgdmVyYm9zaXR5PTApXG5tb2RlbC5maXQoWF90ciwgeV90cilcblxuIyBTSEFQIHZpYSBzaGFwIHBhY2thZ2VcbmV4cGxhaW5lciA9IHNoYXAuVHJlZUV4cGxhaW5lcihtb2RlbClcbnNoYXBfdmFsdWVzID0gZXhwbGFpbmVyLnNoYXBfdmFsdWVzKFhfdGUpXG5wcmludChcdTAwMjdTSEFQIHZhbHVlcyBzaGFwZTpcdTAwMjcsIHNoYXBfdmFsdWVzLnNoYXBlKVxuXG5tZWFuX2FicyA9IG5wLmFicyhzaGFwX3ZhbHVlcykubWVhbigwKVxudG9wNSA9IG5wLmFyZ3NvcnQobWVhbl9hYnMpWzo6LTFdWzo1XVxuZm9yIGkgaW4gdG9wNTpcbiAgICBwcmludChmXHUwMDI3ICB7ZGF0YS5mZWF0dXJlX25hbWVzW2ldOlx1MDAzYzM1c30ge21lYW5fYWJzW2ldOi40Zn1cdTAwMjcpXG5cbnNoYXAuc3VtbWFyeV9wbG90KHNoYXBfdmFsdWVzLCBYX3RlLFxuICAgICAgICAgICAgICAgICAgZmVhdHVyZV9uYW1lcz1kYXRhLmZlYXR1cmVfbmFtZXMsIHBsb3RfdHlwZT1cdTAwMjdiYXJcdTAwMjcsIHNob3c9VHJ1ZSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIeXBlcnBhcmFtZXRlciBUdW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlhHQm9vc3QgaGFzIG1hbnkgaHlwZXJwYXJhbWV0ZXJzIGJ1dCBtb3N0IHR1bmluZyBlZmZvcnQgeWllbGRzIGRpbWluaXNoaW5nIHJldHVybnMuIEZpeCBsZWFybmluZ19yYXRlPTAuMDUgYW5kIHVzZSBlYXJseSBzdG9wcGluZyB0byBmaW5kIG5fZXN0aW1hdG9ycy4gVGhlbiB0dW5lIG1heF9kZXB0aCBhbmQgbWluX2NoaWxkX3dlaWdodCAoY29udHJvbCB0cmVlIGNvbXBsZXhpdHkpLCBmb2xsb3dlZCBieSBzdWJzYW1wbGUgYW5kIGNvbHNhbXBsZV9ieXRyZWUgKGFkZCBzdG9jaGFzdGljaXR5KS4gRmluYWxseSBmaW5lLXR1bmUgcmVnX2FscGhhIGFuZCByZWdfbGFtYmRhLiBUaGlzIHNlcXVlbnRpYWwgYXBwcm9hY2ggYXZvaWRzIHRoZSBjdXJzZSBvZiBkaW1lbnNpb25hbGl0eSBpbiBncmlkIHNlYXJjaC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiSHlwZXJwYXJhbWV0ZXIiLCJUeXBpY2FsIFJhbmdlIiwiRWZmZWN0IiwiV2hlbiB0byBUdW5lIl0sInJvd3MiOltbImxlYXJuaW5nX3JhdGUiLCIwLjAx4oCTMC4zIiwiQ29udHJvbHMgc2hyaW5rYWdlIOKAlCBsb3dlciA9IG1vcmUgdHJlZXMgbmVlZGVkIiwiQWx3YXlzIOKAlCBzZXQgdG8gMC4wNSBmaXJzdCJdLFsibWF4X2RlcHRoIiwiM+KAkzgiLCJUcmVlIGNvbXBsZXhpdHkg4oCUIGRlZXBlciA9IG1vcmUgb3ZlcmZpdHRpbmcgcmlzayIsIkVhcmx5IGluIHR1bmluZyJdLFsibWluX2NoaWxkX3dlaWdodCIsIjHigJMyMCIsIk1pbiBIZXNzaWFuIHN1bSBwZXIgbGVhZiDigJQgaGlnaGVyID0gbW9yZSBjb25zZXJ2YXRpdmUiLCJBZnRlciBtYXhfZGVwdGgiXSxbInN1YnNhbXBsZSIsIjAuNeKAkzEuMCIsIkZyYWN0aW9uIG9mIHJvd3Mgc2FtcGxlZCBwZXIgdHJlZSAoc3RvY2hhc3RpYyBHQikiLCJBZnRlciB0cmVlIHBhcmFtcyJdLFsiY29sc2FtcGxlX2J5dHJlZSIsIjAuNeKAkzEuMCIsIkZyYWN0aW9uIG9mIGZlYXR1cmVzIHNhbXBsZWQgcGVyIHRyZWUiLCJBZnRlciBzdWJzYW1wbGUiXSxbInJlZ19hbHBoYSAoTDEpIiwiMOKAkzEiLCJTcGFyc2l0eSBpbiBsZWFmIHdlaWdodHMg4oCUIHVzZWZ1bCBmb3IgaGlnaC1kaW0gZGF0YSIsIkZpbmUtdHVuaW5nIHN0YWdlIl0sWyJyZWdfbGFtYmRhIChMMikiLCIw4oCTNSIsIlNtb290aCBzaHJpbmthZ2Ugb2YgbGVhZiB3ZWlnaHRzIiwiRmluZS10dW5pbmcgc3RhZ2UiXSxbImdhbW1hIiwiMOKAkzUiLCJNaW5pbXVtIGdhaW4gZm9yIGEgc3BsaXQg4oCUIGJ1aWx0LWluIHBydW5pbmciLCJGaW5lLXR1bmluZyBzdGFnZSJdXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB4Z2Jvb3N0IGFzIHhnYlxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfYnJlYXN0X2NhbmNlclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgUmFuZG9taXplZFNlYXJjaENWLCB0cmFpbl90ZXN0X3NwbGl0XG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCByYW5kaW50LCB1bmlmb3JtXG5cblgsIHkgPSBsb2FkX2JyZWFzdF9jYW5jZXIocmV0dXJuX1hfeT1UcnVlKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxuXG5wYXJhbV9kaXN0ID0ge1xuICAgIFx1MDAyN21heF9kZXB0aFx1MDAyNzogICAgICAgIHJhbmRpbnQoMywgOCksXG4gICAgXHUwMDI3bWluX2NoaWxkX3dlaWdodFx1MDAyNzogcmFuZGludCgxLCAxNSksXG4gICAgXHUwMDI3c3Vic2FtcGxlXHUwMDI3OiAgICAgICAgdW5pZm9ybSgwLjUsIDAuNSksXG4gICAgXHUwMDI3Y29sc2FtcGxlX2J5dHJlZVx1MDAyNzogdW5pZm9ybSgwLjUsIDAuNSksXG4gICAgXHUwMDI3cmVnX2FscGhhXHUwMDI3OiAgICAgICAgdW5pZm9ybSgwLCAxKSxcbn1cblxuYmFzZSA9IHhnYi5YR0JDbGFzc2lmaWVyKFxuICAgIG5fZXN0aW1hdG9ycz0xMDAsIGxlYXJuaW5nX3JhdGU9MC4xLFxuICAgIGV2YWxfbWV0cmljPVx1MDAyN2xvZ2xvc3NcdTAwMjcsIHJhbmRvbV9zdGF0ZT00MiwgdmVyYm9zaXR5PTApXG5ycyA9IFJhbmRvbWl6ZWRTZWFyY2hDVihiYXNlLCBwYXJhbV9kaXN0LCBuX2l0ZXI9NDAsIGN2PTUsXG4gICAgICAgICAgICAgICAgICAgICAgICBzY29yaW5nPVx1MDAyN3JvY19hdWNcdTAwMjcsIG5fam9icz0tMSwgcmFuZG9tX3N0YXRlPTQyKVxucnMuZml0KFhfdHIsIHlfdHIpXG5wcmludChcdTAwMjdCZXN0IHBhcmFtczpcdTAwMjcsIHJzLmJlc3RfcGFyYW1zXylcbnByaW50KGZcdTAwMjdDViBBVUM6ICAge3JzLmJlc3Rfc2NvcmVfOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3VGVzdCBBVUM6IHtycy5zY29yZShYX3RlLCB5X3RlKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiWEdCb29zdFx1MDAyN3MgZXhwbGljaXQgcmVndWxhcmlzYXRpb24gKM6zLCDOuykgaXMga2V5IHRvIGl0cyBnZW5lcmFsaXNhdGlvbiBhZHZhbnRhZ2Ugb3ZlciB2YW5pbGxhIEdCIiwiU2Vjb25kLW9yZGVyIFRheWxvciBleHBhbnNpb24gZ2l2ZXMgbW9yZSBhY2N1cmF0ZSBsZWFmIHdlaWdodHMgdGhhbiBmaXJzdC1vcmRlciBtZXRob2RzIiwibWluX2NoaWxkX3dlaWdodCBjb250cm9scyBsZWFmIGNvbmZpZGVuY2Ug4oCUIGhpZ2ggdmFsdWVzID0gbW9yZSBjb25zZXJ2YXRpdmUgc3BsaXRzIiwiZWFybHlfc3RvcHBpbmdfcm91bmRzIGF1dG9tYXRpY2FsbHkgZmluZHMgbl9lc3RpbWF0b3JzIOKAlCBhbHdheXMgdXNlIGl0IGluIHByYWN0aWNlIiwiU0hBUCBpcyBuYXRpdmVseSBpbnRlZ3JhdGVkIGludG8gWEdCb29zdCDigJQgdXNlIGl0IGZvciBhbGwgcHJvZHVjdGlvbiBleHBsYW5hdGlvbnMiLCJBcHByb3hpbWF0ZSBzcGxpdCBmaW5kaW5nIChoaXN0b2dyYW0pIGVuYWJsZXMgdHJhaW5pbmcgb24gZGF0YXNldHMgdGhhdCBkb25cdTAwMjd0IGZpdCBpbiBtZW1vcnkiXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlhHQm9vc3QgUXVpY2stU3RhcnQgQ29uZmlndXJhdGlvbiIsImNvbnRlbnQiOiJTZXQgbGVhcm5pbmdfcmF0ZT0wLjA1LCBtYXhfZGVwdGg9NSwgbl9lc3RpbWF0b3JzPTEwMDAgd2l0aCBlYXJseV9zdG9wcGluZ19yb3VuZHM9MzAgb24gYSB2YWxpZGF0aW9uIHNldC4gVGhpcyBzaW5nbGUgY29uZmlndXJhdGlvbiBiZWF0cyBtb3N0IGhhbmQtdHVuZWQgc2V0dXBzLiBUaGVuIGltcHJvdmUgZnVydGhlciB3aXRoIHN1YnNhbXBsZT0wLjggYW5kIGNvbHNhbXBsZV9ieXRyZWU9MC44LiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# XGBoost — Second-Order Taylor Expansion and Regularization

## XGBoost Objective Function

XGBoost (Chen & Guestrin 2016) frames tree boosting as explicit regularised objective minimisation: Obj = Σᵢ l(yᵢ, ŷᵢ) + Σₖ Ω(fₖ) where Ω(f) = γT + (λ/2)Σⱼ wⱼ² penalises tree complexity. γ is a minimum gain threshold per new leaf (L1-style on tree structure); λ is L2 regularisation on leaf weights. This explicit penalty prevents overfitting and is key to XGBoost's superior generalisation over vanilla gradient boosting.

## Second-Order Taylor Expansion

At step m, XGBoost approximates the loss using a second-order Taylor expansion around the current prediction F_{m-1}: L ≈ Σᵢ [gᵢ hₘ(xᵢ) + (1/2) hᵢ hₘ(xᵢ)²] + Ω(hₘ) where gᵢ = ∂l/∂F (first derivative) and hᵢ = ∂²l/∂F² (second derivative / Hessian). For a leaf j collecting instances I_j, the optimal leaf weight is wⱼ* = −Gⱼ/(Hⱼ+λ) where Gⱼ = Σᵢ∈I_j gᵢ and Hⱼ = Σᵢ∈I_j hᵢ. The second-order expansion enables faster, more accurate optimisation than the first-order approach used by vanilla GB.

```python
import xgboost as xgb
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Custom objective: MSE — first derivative = pred - y, second = 1
def mse_obj(y_pred, dtrain):
    y_true = dtrain.get_label()
    grad = y_pred - y_true           # g_i = first derivative of MSE
    hess = np.ones_like(y_pred)      # h_i = second derivative = 1 (constant)
    return grad, hess

def rmse_eval(y_pred, dtrain):
    y_true = dtrain.get_label()
    return 'rmse', float(np.sqrt(mean_squared_error(y_true, y_pred)))

X, y = make_regression(n_samples=1000, n_features=20, noise=15, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

dtrain = xgb.DMatrix(X_tr, label=y_tr)
dtest  = xgb.DMatrix(X_te, label=y_te)

params = {'max_depth': 4, 'eta': 0.1, 'seed': 42, 'verbosity': 0}
evals_result = {}
model = xgb.train(params, dtrain, num_boost_round=150,
                  obj=mse_obj, custom_metric=rmse_eval,
                  evals=[(dtrain,'train'),(dtest,'test')],
                  evals_result=evals_result, verbose_eval=30)
preds = model.predict(dtest)
print(f'Final RMSE: {np.sqrt(mean_squared_error(y_te, preds)):.4f}')
```

## Optimal Split Gain Formula

The gain from splitting node I into left I_L and right I_R is: Gain = (1/2)[G_L²/(H_L+λ) + G_R²/(H_R+λ) − (G_L+G_R)²/(H_L+H_R+λ)] − γ. The γ term means a split is only made if the gain exceeds the minimum threshold — this is XGBoost's built-in pruning. The Hessian in the denominator acts as a confidence weighting: instances with low curvature (high certainty) have less influence on the split. min_child_weight controls the minimum sum of Hessians allowed in a leaf.

> **Why Second-Order Matters**: First-order methods (vanilla GB) treat each instance equally in the gradient. Second-order methods weight instances by their Hessian — instances near the decision boundary (high curvature, uncertain predictions) get higher weight than confidently-classified instances. This leads to faster convergence and better leaf weight estimates, especially with non-MSE losses.

## XGBClassifier with Early Stopping

XGBoost's Python API supports early stopping: if the validation metric does not improve for early_stopping_rounds consecutive rounds, training halts and best_iteration is saved. This automatically finds the right n_estimators without grid search. The eval_metric parameter specifies the validation metric; logloss, auc, and error are common choices for classification.

```python
import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
X_tr2, X_val, y_tr2, y_val = train_test_split(X_tr, y_tr, test_size=0.15, random_state=42)

clf = xgb.XGBClassifier(
    n_estimators=1000,
    learning_rate=0.05,
    max_depth=4,
    min_child_weight=5,     # minimum sum of hessians per leaf
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,          # L1 on leaf weights
    reg_lambda=1.0,         # L2 on leaf weights
    eval_metric='auc',
    early_stopping_rounds=30,
    random_state=42,
    verbosity=0
)
clf.fit(X_tr2, y_tr2, eval_set=[(X_val, y_val)], verbose=False)
print(f'Best iteration: {clf.best_iteration}')
auc = roc_auc_score(y_te, clf.predict_proba(X_te)[:, 1])
print(f'Test AUC: {auc:.4f}')
```

## SHAP Integration with XGBoost

XGBoost has native SHAP support via the TreeExplainer, computing exact Shapley values in O(TLD²) time. model.predict(dtest, pred_contribs=True) returns the SHAP contribution matrix directly from XGBoost without the separate shap package. Using the shap package on XGBoost models is also seamless and provides all standard visualisations.

```python
import xgboost as xgb
import shap
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X, y = data.data, data.target
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBClassifier(
    n_estimators=100, max_depth=4, learning_rate=0.1,
    eval_metric='logloss', random_state=42, verbosity=0)
model.fit(X_tr, y_tr)

# SHAP via shap package
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_te)
print('SHAP values shape:', shap_values.shape)

mean_abs = np.abs(shap_values).mean(0)
top5 = np.argsort(mean_abs)[::-1][:5]
for i in top5:
    print(f'  {data.feature_names[i]:<35s} {mean_abs[i]:.4f}')

shap.summary_plot(shap_values, X_te,
                  feature_names=data.feature_names, plot_type='bar', show=True)
```

## Hyperparameter Tuning

XGBoost has many hyperparameters but most tuning effort yields diminishing returns. Fix learning_rate=0.05 and use early stopping to find n_estimators. Then tune max_depth and min_child_weight (control tree complexity), followed by subsample and colsample_bytree (add stochasticity). Finally fine-tune reg_alpha and reg_lambda. This sequential approach avoids the curse of dimensionality in grid search.

| Hyperparameter | Typical Range | Effect | When to Tune |
| --- | --- | --- | --- |
| learning_rate | 0.01–0.3 | Controls shrinkage — lower = more trees needed | Always — set to 0.05 first |
| max_depth | 3–8 | Tree complexity — deeper = more overfitting risk | Early in tuning |
| min_child_weight | 1–20 | Min Hessian sum per leaf — higher = more conservative | After max_depth |
| subsample | 0.5–1.0 | Fraction of rows sampled per tree (stochastic GB) | After tree params |
| colsample_bytree | 0.5–1.0 | Fraction of features sampled per tree | After subsample |
| reg_alpha (L1) | 0–1 | Sparsity in leaf weights — useful for high-dim data | Fine-tuning stage |
| reg_lambda (L2) | 0–5 | Smooth shrinkage of leaf weights | Fine-tuning stage |
| gamma | 0–5 | Minimum gain for a split — built-in pruning | Fine-tuning stage |

```python
import xgboost as xgb
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint, uniform

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

param_dist = {
    'max_depth':        randint(3, 8),
    'min_child_weight': randint(1, 15),
    'subsample':        uniform(0.5, 0.5),
    'colsample_bytree': uniform(0.5, 0.5),
    'reg_alpha':        uniform(0, 1),
}

base = xgb.XGBClassifier(
    n_estimators=100, learning_rate=0.1,
    eval_metric='logloss', random_state=42, verbosity=0)
rs = RandomizedSearchCV(base, param_dist, n_iter=40, cv=5,
                        scoring='roc_auc', n_jobs=-1, random_state=42)
rs.fit(X_tr, y_tr)
print('Best params:', rs.best_params_)
print(f'CV AUC:   {rs.best_score_:.4f}')
print(f'Test AUC: {rs.score(X_te, y_te):.4f}')
```

- XGBoost's explicit regularisation (γ, λ) is key to its generalisation advantage over vanilla GB
- Second-order Taylor expansion gives more accurate leaf weights than first-order methods
- min_child_weight controls leaf confidence — high values = more conservative splits
- early_stopping_rounds automatically finds n_estimators — always use it in practice
- SHAP is natively integrated into XGBoost — use it for all production explanations
- Approximate split finding (histogram) enables training on datasets that don't fit in memory

> **XGBoost Quick-Start Configuration**: Set learning_rate=0.05, max_depth=5, n_estimators=1000 with early_stopping_rounds=30 on a validation set. This single configuration beats most hand-tuned setups. Then improve further with subsample=0.8 and colsample_bytree=0.8.

---

