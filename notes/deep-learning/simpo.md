---
title: "SimPO — Simple Preference Optimization with Length-Normalized Rewards"
slug: "simpo"
description: "SimPO (Meng et al., 2024) eliminates DPO's reference model and length bias by using average per-token log-probability as the implicit reward, combined with a target margin gamma that prevents preference collapse, consistently outperforming DPO on AlpacaEval 2 LC-WR."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2ltUE8gKFNpbXBsZSBQcmVmZXJlbmNlIE9wdGltaXphdGlvbiwgTWVuZyBldCBhbC4gMjAyNCkgYWRkcmVzc2VzIHR3byBpbmRlcGVuZGVudCBwcm9ibGVtcyB3aXRoIERQTyB0aGF0IGhhdmUgZGlmZmVyZW50IHJvb3RzIGJ1dCBpbnRlcmFjdCBoYXJtZnVsbHk6ICgxKSBEUE8gcmVxdWlyZXMgYSByZWZlcmVuY2UgbW9kZWwsIGRvdWJsaW5nIEdQVSBtZW1vcnk7ICgyKSBEUE9cdTAwMjdzIGltcGxpY2l0IHJld2FyZCDigJQgdGhlIHRvdGFsIGxvZy1wcm9iYWJpbGl0eSB1bmRlciB0aGUgcG9saWN5IOKAlCBpcyBiaWFzZWQgdG93YXJkIGxvbmdlciByZXNwb25zZXMgcmVnYXJkbGVzcyBvZiBxdWFsaXR5LiBTaW1QTyBmaXhlcyBib3RoIHByb2JsZW1zIGluIGEgc2luZ2xlIGRlc2lnbjogcmVwbGFjZSB0aGUgcmVmZXJlbmNlLW1vZGVsLXJlbGF0aXZlIHJld2FyZCB3aXRoIGEgbGVuZ3RoLW5vcm1hbGl6ZWQgYXZlcmFnZSBsb2ctcHJvYmFiaWxpdHksIGFuZCBhZGQgYSB0YXJnZXQgbWFyZ2luIGdhbW1hIHRoYXQgcHJldmVudHMgdGhlIG9wdGltaXphdGlvbiBmcm9tIGNvbGxhcHNpbmcgd2hlbiBjaG9zZW4gYW5kIHJlamVjdGVkIHJld2FyZHMgYXJlIHNpbWlsYXIuIFRoZSByZXN1bHQgaXMgYSBzaW1wbGVyLCBjaGVhcGVyLCBhbmQgZW1waXJpY2FsbHkgc3Ryb25nZXIgYWxpZ25tZW50IGFsZ29yaXRobS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEUE9cdTAwMjdzIExlbmd0aCBCaWFzOiBXaHkgVmVyYm9zZSBSZXNwb25zZXMgV2luIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEUE9cdTAwMjdzIGltcGxpY2l0IHJld2FyZCBmb3IgYSByZXNwb25zZSB5IGdpdmVuIHByb21wdCB4IGlzIHJfRFBPKHgseSkgPSBiZXRhICogbG9nIHBpX3RoZXRhKHl8eCkgLSBiZXRhICogbG9nIHBpX3JlZih5fHgpLiBUaGUgdGVybSBsb2cgcGlfdGhldGEoeXx4KSA9IHN1bV97dD0xfV57fHl8fSBsb2cgcGlfdGhldGEoeV90IHwgeCwgeV97XHUwMDNjdH0pIGlzIGEgU1VNIG92ZXIgdG9rZW5zIOKAlCBpdCBncm93cyBsaW5lYXJseSB3aXRoIHNlcXVlbmNlIGxlbmd0aCBldmVuIGlmIHBlci10b2tlbiBxdWFsaXR5IGlzIGlkZW50aWNhbC4gQ29uc2lkZXIgdHdvIHJlc3BvbnNlcyB3aXRoIHRoZSBzYW1lIHBlci10b2tlbiBsb2ctcHJvYmFiaWxpdHkgbXU6IGEgNTAtdG9rZW4gcmVzcG9uc2UgaGFzIHRvdGFsIGxvZy1wcm9iIDUwKm11LCB3aGlsZSBhIDIwMC10b2tlbiByZXNwb25zZSBoYXMgMjAwKm11LiBEUE8gd291bGQgcmFuayB0aGUgMjAwLXRva2VuIHJlc3BvbnNlIGFzIDTDlyBiZXR0ZXIuIFRoaXMgY3JlYXRlcyBhbiBpbmNlbnRpdmUgZm9yIG1vZGVscyB0byBwcm9kdWNlIHZlcmJvc2UgcmVzcG9uc2VzOiB0aGUgRFBPIHBvbGljeSBsZWFybnMgdGhhdCBhZGRpbmcgZmlsbGVyIHRleHQgKFx1MDAyN0dyZWF0IHF1ZXN0aW9uISBJIGFtIGhhcHB5IHRvIGV4cGxhaW4uLi5cdTAwMjcpIGluY3JlYXNlcyBpdHMgb3duIHJld2FyZCBldmVuIGlmIGl0IHJlZHVjZXMgcGVyLXRva2VuIHF1YWxpdHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2ltUE8gSW1wbGljaXQgUmV3YXJkOiBMZW5ndGgtTm9ybWFsaXplZCBMb2ctUHJvYnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNpbVBPIHJlcGxhY2VzIERQT1x1MDAyN3MgdG90YWwgbG9nLXByb2IgcmV3YXJkIHdpdGggYW4gYXZlcmFnZSBwZXItdG9rZW4gbG9nLXByb2JhYmlsaXR5OiByX1NpbVBPKHgseSkgPSAoYmV0YSAvIHx5fCkgKiBzdW1fe3Q9MX1ee3x5fH0gbG9nIHBpX3RoZXRhKHlfdCB8IHgsIHlfe1x1MDAzY3R9KS4gVGhpcyBpcyB0aGUgbWVhbiBjb25kaXRpb25hbCBsb2ctbGlrZWxpaG9vZCBvZiB0aGUgcmVzcG9uc2UgdG9rZW5zLCBzY2FsZWQgYnkgYmV0YS4gTGVuZ3RoIG5vcm1hbGl6YXRpb24gbWFrZXMgdGhlIHJld2FyZCBsZW5ndGgtYWdub3N0aWM6IGEgNTAtdG9rZW4gcmVzcG9uc2UgYW5kIGEgMjAwLXRva2VuIHJlc3BvbnNlIHdpdGggdGhlIHNhbWUgcGVyLXRva2VuIHF1YWxpdHkgcmVjZWl2ZSBpZGVudGljYWwgcmV3YXJkcy4gQ3J1Y2lhbGx5LCBTaW1QTyBoYXMgbm8gcmVmZXJlbmNlIG1vZGVsIOKAlCB0aGUgcmV3YXJkIGlzIHB1cmVseSBmcm9tIHRoZSBjdXJyZW50IHBvbGljeSDigJQgd2hpY2ggZWxpbWluYXRlcyB0aGUgbmVlZCB0byBzdG9yZSBwaV9yZWYgaW4gR1BVIG1lbW9yeS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaW1QTyBMb3NzIHdpdGggVGFyZ2V0IE1hcmdpbiBnYW1tYSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aG91dCBhIHJlZmVyZW5jZSBtb2RlbCwgdGhlIHByZWZlcmVuY2UgbWFyZ2luIGNhbiBjb2xsYXBzZSB0byB6ZXJvIGlmIHRoZSBwb2xpY3kgbGVhcm5zIHRvIGFzc2lnbiBzaW1pbGFyIHJld2FyZHMgdG8gY2hvc2VuIGFuZCByZWplY3RlZCByZXNwb25zZXMuIFNpbVBPIGFkZHMgYSB0YXJnZXQgbWFyZ2luIGdhbW1hOiBMX1NpbVBPID0gLUVbbG9nIHNpZ21hKHIoeCx5X3cpIC0gcih4LHlfbCkgLSBnYW1tYSldID0gLUVbbG9nIHNpZ21hKGJldGEqKGF2Z19sb2dwKHlfdykgLSBhdmdfbG9ncCh5X2wpKSAtIGdhbW1hKV0uIFRoZSBtYXJnaW4gZ2FtbWEgZW5mb3JjZXMgdGhhdCBjaG9zZW4gcmVzcG9uc2VzIG11c3QgYmUgcHJlZmVycmVkIGJ5IGF0IGxlYXN0IGdhbW1hIGluIHRoZSByZXdhcmQgc3BhY2Ug4oCUIHRoZSBvcHRpbWl6YXRpb24gaXMgbm9uLXRyaXZpYWxseSBzYXRpc2ZpZWQgd2hlbiB0aGUgbWFyZ2luIGV4YWN0bHkgZXF1YWxzIGdhbW1hLiBEZWZhdWx0IHZhbHVlcyBmcm9tIHRoZSBwYXBlcjogYmV0YT0yLjUsIGdhbW1hPTAuNS4gU2ltUE8gY29uc2lzdGVudGx5IG91dHBlcmZvcm1zIERQTyBvbiBBbHBhY2FFdmFsIDIgTEMtV1IgKGxlbmd0aC1jb250cm9sbGVkIHdpbiByYXRlKSB3aXRoIHRoZXNlIGh5cGVycGFyYW1ldGVycyBvbiBNaXN0cmFsIGFuZCBMbGFtYSBiYXNlIG1vZGVscy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaW1QTyBMb3NzIEltcGxlbWVudGF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgc2ltcG9fbG9zcyhcbiAgICBwb2xpY3lfY2hvc2VuX2xvZ3BzLCAgICAgICMgc3VtIG9mIGxvZy1wcm9icyBvdmVyIHJlc3BvbnNlIHRva2Vuc1xuICAgIHBvbGljeV9yZWplY3RlZF9sb2dwcyxcbiAgICBjaG9zZW5fbGVuZ3RocywgICAgICAgICAgICAjIHJlc3BvbnNlIHRva2VuIGNvdW50cyBmb3Igbm9ybWFsaXphdGlvblxuICAgIHJlamVjdGVkX2xlbmd0aHMsXG4gICAgYmV0YT0yLjUsXG4gICAgZ2FtbWE9MC41LFxuKTpcbiAgICAjIExlbmd0aC1ub3JtYWxpemVkIGF2ZXJhZ2UgbG9nLXByb2IgPSBTaW1QTyBpbXBsaWNpdCByZXdhcmQgcih4LHkpXG4gICAgcl9jaG9zZW4gICA9IHBvbGljeV9jaG9zZW5fbG9ncHMgICAvIGNob3Nlbl9sZW5ndGhzLmZsb2F0KClcbiAgICByX3JlamVjdGVkID0gcG9saWN5X3JlamVjdGVkX2xvZ3BzIC8gcmVqZWN0ZWRfbGVuZ3Rocy5mbG9hdCgpXG4gICAgIyBFbmZvcmNlIGJldGEqKHJfdyAtIHJfbCkgXHUwMDNlIGdhbW1hICh0YXJnZXQgbWFyZ2luIHByZXZlbnRzIGNvbGxhcHNlKVxuICAgIHJld2FyZF9kaWZmID0gYmV0YSAqIChyX2Nob3NlbiAtIHJfcmVqZWN0ZWQpIC0gZ2FtbWFcbiAgICBsb3NzID0gLUYubG9nc2lnbW9pZChyZXdhcmRfZGlmZikubWVhbigpXG4gICAgcmV0dXJuIGxvc3MsIHJfY2hvc2VuLmRldGFjaCgpLCByX3JlamVjdGVkLmRldGFjaCgpXG5cbmJzeiA9IDhcbmNob3Nlbl9sZW5zICAgPSB0b3JjaC5yYW5kaW50KDgwLCAxNTAsIChic3osKSlcbnJlamVjdGVkX2xlbnMgPSB0b3JjaC5yYW5kaW50KDUwLCAyNTAsIChic3osKSkgICMgcmVqZWN0ZWQgY2FuIGJlIGxvbmdlciBvciBzaG9ydGVyXG5jaG9zZW5fbG9ncHMgICA9IC1jaG9zZW5fbGVucy5mbG9hdCgpICogMC45ICAgICAgIyBzdW0gbG9ncCBwcm9wb3J0aW9uYWwgdG8gbGVuZ3RoXG5yZWplY3RlZF9sb2dwcyA9IC1yZWplY3RlZF9sZW5zLmZsb2F0KCkgKiAxLjEgICAgIyByZWplY3RlZCBoYXMgd29yc2UgcGVyLXRva2VuIGxvZ3Bcbmxvc3MsIHJ3LCByciA9IHNpbXBvX2xvc3MoY2hvc2VuX2xvZ3BzLCByZWplY3RlZF9sb2dwcywgY2hvc2VuX2xlbnMsIHJlamVjdGVkX2xlbnMpXG5wcmludChmXHUwMDI3U2ltUE8gbG9zczoge2xvc3M6LjRmfSAgYXZnIHJld2FyZCBjaG9zZW46IHtydy5tZWFuKCk6LjNmfSAgcmVqZWN0ZWQ6IHtyci5tZWFuKCk6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMZW5ndGggTm9ybWFsaXphdGlvbjogRFBPIHZzIFNpbVBPIFJld2FyZCBBc3NpZ25tZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2V5IGVtcGlyaWNhbCB0ZXN0IG9mIGxlbmd0aCBiaWFzIGlzOiBnaXZlbiB0d28gcmVzcG9uc2VzIHdpdGggaWRlbnRpY2FsIHBlci10b2tlbiBxdWFsaXR5IGJ1dCBkaWZmZXJlbnQgbGVuZ3Rocywgd2hpY2ggZG9lcyB0aGUgYWxnb3JpdGhtIHByZWZlcj8gRFBPLCB1c2luZyB0b3RhbCBsb2ctcHJvYiwgcHJlZmVycyB0aGUgbG9uZ2VyIG9uZSBpbiBwcm9wb3J0aW9uIHRvIGl0cyBsZW5ndGggYWR2YW50YWdlLiBTaW1QTywgdXNpbmcgYXZlcmFnZSBsb2ctcHJvYiwgYXNzaWducyBpZGVudGljYWwgcmV3YXJkcyB0byBib3RoLiBUaGlzIGlzIG5vdCBtZXJlbHkgYSB0aGVvcmV0aWNhbCBjb25jZXJuIOKAlCBvbiBBbHBhY2FFdmFsIDIsIERQTy10cmFpbmVkIG1vZGVscyBwcm9kdWNlIHJlc3BvbnNlcyB0aGF0IGFyZSBvbiBhdmVyYWdlIDMwLTUwJSBsb25nZXIgdGhhbiB0aGUgcmVmZXJlbmNlLCB3aGlsZSBTaW1QTy10cmFpbmVkIG1vZGVscyBtYXRjaCByZWZlcmVuY2UgbGVuZ3RoLCBleHBsYWluaW5nIFNpbVBPXHUwMDI3cyBzdXBlcmlvciBMQy1XUiAobGVuZ3RoLWNvbnRyb2xsZWQgd2luIHJhdGUpIGRlc3BpdGUgb2Z0ZW4gaGF2aW5nIGxvd2VyIHJhdyB3aW4gcmF0ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBkcG9fcmV3YXJkKGxvZ3BzX3N1bSwgcmVmX2xvZ3BzX3N1bSwgYmV0YT0wLjEpOlxuICAgICMgRFBPOiB1bm5vcm1hbGl6ZWQgdG90YWwgbG9nLXByb2IgZGlmZmVyZW5jZVxuICAgIHJldHVybiBiZXRhICogKGxvZ3BzX3N1bSAtIHJlZl9sb2dwc19zdW0pXG5cbmRlZiBzaW1wb19yZXdhcmQobG9ncHNfc3VtLCBsZW5ndGgsIGJldGE9Mi41KTpcbiAgICAjIFNpbVBPOiBhdmVyYWdlIHBlci10b2tlbiBsb2ctcHJvYiAobGVuZ3RoLW5vcm1hbGl6ZWQpXG4gICAgcmV0dXJuIGJldGEgKiBsb2dwc19zdW0gLyBsZW5ndGguZmxvYXQoKVxuXG4jIFR3byByZXNwb25zZXM6IHNhbWUgcGVyLXRva2VuIHF1YWxpdHksIDR4IGxlbmd0aCBkaWZmZXJlbmNlXG5wZXJfdG9rID0gLTEuMlxuc2hvcnRfbGVuLCBsb25nX2xlbiA9IHRvcmNoLnRlbnNvcig2MCksIHRvcmNoLnRlbnNvcigyNDApXG5zaG9ydF9sb2dwcyA9IHBlcl90b2sgKiBzaG9ydF9sZW4uZmxvYXQoKVxubG9uZ19sb2dwcyAgPSBwZXJfdG9rICogbG9uZ19sZW4uZmxvYXQoKVxucmVmX3Nob3J0ICAgPSBwZXJfdG9rICogMC45ICogc2hvcnRfbGVuLmZsb2F0KClcbnJlZl9sb25nICAgID0gcGVyX3RvayAqIDAuOSAqIGxvbmdfbGVuLmZsb2F0KClcblxuZHBvX3MgID0gZHBvX3Jld2FyZChzaG9ydF9sb2dwcywgcmVmX3Nob3J0KVxuZHBvX2wgID0gZHBvX3Jld2FyZChsb25nX2xvZ3BzLCAgcmVmX2xvbmcpXG5zaW1wb19zID0gc2ltcG9fcmV3YXJkKHNob3J0X2xvZ3BzLCBzaG9ydF9sZW4pXG5zaW1wb19sID0gc2ltcG9fcmV3YXJkKGxvbmdfbG9ncHMsICBsb25nX2xlbilcbnByaW50KGZcdTAwMjdFcXVhbCBwZXItdG9rZW4gcXVhbGl0eS4gRFBPOiBzaG9ydD17ZHBvX3M6LjFmfSwgbG9uZz17ZHBvX2w6LjFmfSAgLVx1MDAzZSBsb25nIHdpbnMgYnkge2Rwb19sL2Rwb19zOi4xZn14XHUwMDI3KVxucHJpbnQoZlx1MDAyN1NpbVBPOiAgICAgICAgICAgICAgICAgICAgICAgIHNob3J0PXtzaW1wb19zOi4zZn0sIGxvbmc9e3NpbXBvX2w6LjNmfSAtXHUwMDNlIGxlbmd0aC1uZXV0cmFsXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNpbVBPIFRyYWluaW5nIExvb3AgV2l0aG91dCBSZWZlcmVuY2UgTW9kZWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNpbVBPXHUwMDI3cyB0cmFpbmluZyBsb29wIGRpZmZlcnMgZnJvbSBEUE8gaW4gdHdvIGtleSB3YXlzOiBubyByZWZlcmVuY2UgbW9kZWwgZm9yd2FyZCBwYXNzLCBhbmQgZXhwbGljaXQgbGVuZ3RoIHRyYWNraW5nIGZvciB0aGUgbm9ybWFsaXphdGlvbi4gVGhlIHJlc3BvbnNlIGxlbmd0aCBpcyB0aGUgbnVtYmVyIG9mIG5vbi1wYWRkaW5nIHRva2VucyBpbiB0aGUgcmVzcG9uc2UgcG9ydGlvbiBvZiB0aGUgc2VxdWVuY2UgKG5vdCB0aGUgZnVsbCBwcm9tcHQrcmVzcG9uc2UgbGVuZ3RoKS4gSW4gcHJhY3RpY2UsIHRoaXMgcmVxdWlyZXMgYSByZXNwb25zZSBtYXNrIHRoYXQgbWFya3Mgd2hpY2ggdG9rZW5zIGFyZSBwYXJ0IG9mIHRoZSBhc3Npc3RhbnRcdTAwMjdzIHJlc3BvbnNlLCBzZXBhcmF0ZSBmcm9tIHRoZSBwcm9tcHQgdG9rZW5zLiBUaGlzIGlzIGltcG9ydGFudDogbm9ybWFsaXppbmcgYnkgdGhlIHRvdGFsIHNlcXVlbmNlIGxlbmd0aCAoaW5jbHVkaW5nIHByb21wdCkgd291bGQgcGVuYWxpemUgbG9uZyBwcm9tcHRzIHVuZmFpcmx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmZyb20gdG9yY2gub3B0aW0gaW1wb3J0IEFkYW1XXG5cbmRlZiBjb21wdXRlX3Jlc3BvbnNlX2xvZ3BzKG1vZGVsLCBpbnB1dF9pZHMsIGF0dGVudGlvbl9tYXNrLCByZXNwb25zZV9zdGFydCk6XG4gICAgIyBDb21wdXRlIHN1bSBhbmQgY291bnQgb2YgbG9nLXByb2JzIG92ZXIgcmVzcG9uc2UgdG9rZW5zIG9ubHkgKG5vdCBwcm9tcHQpXG4gICAgb3V0cHV0cyAgPSBtb2RlbChpbnB1dF9pZHM9aW5wdXRfaWRzLCBhdHRlbnRpb25fbWFzaz1hdHRlbnRpb25fbWFzaylcbiAgICBsb2dpdHMgICA9IG91dHB1dHMubG9naXRzWzosIDotMV0uY29udGlndW91cygpXG4gICAgbGFiZWxzICAgPSBpbnB1dF9pZHNbOiwgMTpdLmNvbnRpZ3VvdXMoKVxuICAgIGxwICAgICAgID0gRi5sb2dfc29mdG1heChsb2dpdHMsIGRpbT0tMSlcbiAgICB0b2tfbHAgICA9IGxwLmdhdGhlcigyLCBsYWJlbHMudW5zcXVlZXplKC0xKSkuc3F1ZWV6ZSgtMSlcbiAgICByZXNwX21hc2sgPSB0b3JjaC56ZXJvc19saWtlKHRva19scClcbiAgICByZXNwX21hc2tbOiwgcmVzcG9uc2Vfc3RhcnQ6XSA9IGF0dGVudGlvbl9tYXNrWzosIHJlc3BvbnNlX3N0YXJ0ICsgMTpdLmZsb2F0KClcbiAgICBzdW1fbHAgID0gKHRva19scCAqIHJlc3BfbWFzaykuc3VtKGRpbT0xKVxuICAgIGxlbmd0aHMgPSByZXNwX21hc2suc3VtKGRpbT0xKVxuICAgIHJldHVybiBzdW1fbHAsIGxlbmd0aHNcblxuZGVmIHNpbXBvX3RyYWluX3N0ZXAobW9kZWwsIG9wdGltaXplciwgY2hvc2VuX2lkcywgcmVqZWN0ZWRfaWRzLFxuICAgICAgICAgICAgICAgICAgICAgY19tYXNrLCByX21hc2ssIHJlc3Bfc3RhcnQsIGJldGE9Mi41LCBnYW1tYT0wLjUpOlxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgIGxvZ3BzX2MsIGxlbnNfYyA9IGNvbXB1dGVfcmVzcG9uc2VfbG9ncHMobW9kZWwsIGNob3Nlbl9pZHMsICAgY19tYXNrLCByZXNwX3N0YXJ0KVxuICAgIGxvZ3BzX3IsIGxlbnNfciA9IGNvbXB1dGVfcmVzcG9uc2VfbG9ncHMobW9kZWwsIHJlamVjdGVkX2lkcywgcl9tYXNrLCByZXNwX3N0YXJ0KVxuICAgIHJfYyAgID0gYmV0YSAqIGxvZ3BzX2MgLyBsZW5zX2NcbiAgICByX3IgICA9IGJldGEgKiBsb2dwc19yIC8gbGVuc19yXG4gICAgbG9zcyAgPSAtRi5sb2dzaWdtb2lkKHJfYyAtIHJfciAtIGdhbW1hKS5tZWFuKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgcmV0dXJuIGxvc3MuaXRlbSgpXG5cbnByaW50KFx1MDAyN1NpbVBPOiAxIG1vZGVsIGluIEdQVSwgcmVzcG9uc2Utb25seSBsZW5ndGggbm9ybWFsaXphdGlvbiwgbWFyZ2luIGdhbW1hPTAuNVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYXJnaW4gU2Vuc2l0aXZpdHkgQW5hbHlzaXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBnYW1tYSBtYXJnaW4gaW4gU2ltUE8gc2VydmVzIGFzIGEgbWluaW11bSBhY2NlcHRhYmxlIHByZWZlcmVuY2UgZ2FwLiBXaGVuIGdhbW1hPTAsIHRoZSBsb3NzIHJlZHVjZXMgdG8gYSBzaW1wbGUgY29udHJhc3RpdmUgbG9zcyB3aXRob3V0IGFuIGV4cGxpY2l0IHRhcmdldCDigJQgdGhlIG9wdGltaXphdGlvbiBpcyBzYXRpc2ZpZWQgd2hlbmV2ZXIgY2hvc2VuIHJld2FyZCBleGNlZWRzIHJlamVjdGVkIHJld2FyZCBieSBhbnkgYW1vdW50LCB3aGljaCBjYW4gbGVhZCB0byBzbWFsbCwgbm9pc3kgZ3JhZGllbnRzLiBBcyBnYW1tYSBpbmNyZWFzZXMsIHRoZSBlZmZlY3RpdmUgd2luLXJhdGUgdGhyZXNob2xkIHJpc2VzICh0aGUgbW9kZWwgbXVzdCBhY2hpZXZlIGEgc3Ryb25nZXIgcHJlZmVyZW5jZSB0byBzYXRpc2Z5IHRoZSBsb3NzKSwgd2hpY2ggcHJvdmlkZXMgbGFyZ2VyIGdyYWRpZW50cyB3aGVuIHRoZSBwb2xpY3kgaXMgbmVhciB0aGUgZGVjaXNpb24gYm91bmRhcnkgYnV0IGhhcmRlciBvcHRpbWl6YXRpb24gd2hlbiB0aGUgZGF0YSBpcyBub2lzeS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5iZXRhICA9IDIuNVxucl93ICAgPSB0b3JjaC5yYW5kbigxMDAwKSAqIDAuNCArIDAuOCAgICMgY2hvc2VuIGF2ZyBsb2ctcHJvYlxucl9sICAgPSB0b3JjaC5yYW5kbigxMDAwKSAqIDAuNCArIDAuMCAgICMgcmVqZWN0ZWQgYXZnIGxvZy1wcm9iXG5yZXdfZGlmZiA9IGJldGEgKiAocl93IC0gcl9sKVxuXG5nYW1tYXMgPSBbMC4wLCAwLjIsIDAuNSwgMS4wLCAyLjAsIDMuMF1cbnByaW50KGZcdTAwMjcgIGdhbW1hICAgd2luX3JhdGUgICBsb3NzICAgICAgIGdyYWRfbWFnbml0dWRlXHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDUwKVxuZm9yIGcgaW4gZ2FtbWFzOlxuICAgIHByb2JzID0gdG9yY2guc2lnbW9pZChyZXdfZGlmZiAtIGcpXG4gICAgbG9zcyAgPSAtRi5sb2dzaWdtb2lkKHJld19kaWZmIC0gZykubWVhbigpXG4gICAgZ3JhZCAgPSB0b3JjaC5zaWdtb2lkKC0ocmV3X2RpZmYgLSBnKSkubWVhbigpICAjIGdyYWRpZW50IHdlaWdodFxuICAgIHByaW50KGZcdTAwMjcgIHtnOi4xZn0gICAgIHtwcm9icy5tZWFuKCk6LjNmfSAgICB7bG9zcy5pdGVtKCk6LjRmfSAgICB7Z3JhZC5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KClcbnByaW50KFx1MDAyN0xhcmdlciBnYW1tYTogZmV3ZXIgc2F0aXNmaWVkIHBhaXJzLCBsYXJnZXIgZ3JhZGllbnRzIG9uIHVuc2F0aXNmaWVkIG9uZXNcdTAwMjcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlJlZmVyZW5jZSBNb2RlbCIsIkxlbmd0aCBOb3JtIiwiTWFyZ2luIFRlcm0iLCJNZW1vcnkgN0IiLCJBbHBhY2FFdmFsIDIgTEMtV1IiXSwicm93cyI6W1siRFBPIiwiWWVzIChmcm96ZW4pIiwiTm8gKHRvdGFsIGxvZ3ApIiwiTm8iLCJ+MjggR0IiLCJCYXNlbGluZSJdLFsiU2ltUE8iLCJObyIsIlllcyAoYXZnIGxvZ3ApIiwiWWVzIChnYW1tYSkiLCJ+MTQgR0IiLCIrMyB0byArNSBwdHMgdnMgRFBPIl0sWyJPUlBPIiwiTm8iLCJQYXJ0aWFsIChtZWFuIHRvaykiLCJObyIsIn4xNCBHQiIsIkNvbXBldGl0aXZlIHdpdGggRFBPIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlNpbVBPXHUwMDI3cyBMZW5ndGgtTm9ybWFsaXplZCBSZXdhcmQiLCJjb250ZW50IjoiU2ltUE9cdTAwMjdzIGxlbmd0aC1ub3JtYWxpemVkIHJld2FyZCBpcyB0aGVvcmV0aWNhbGx5IGVxdWl2YWxlbnQgdG8gbWF4aW1pemluZyBwZXItdG9rZW4gY29uZGl0aW9uYWwgbG9nLWxpa2VsaWhvb2Qgb2YgY2hvc2VuIG92ZXIgcmVqZWN0ZWQg4oCUIHRoaXMgZGlyZWN0bHkgcHJldmVudHMgdGhlIFx1MDAyN2FkZCBmaWxsZXIgdGV4dFx1MDAyNyBmYWlsdXJlIG1vZGUgd2hlcmUgRFBPIHBvbGljaWVzIGxlYXJuIHRvIGJlIHZlcmJvc2UgdG8gbWF4aW1pemUgdG90YWwgbG9nLXByb2IuIFRoZSBsZW5ndGgtY29udHJvbGxlZCB3aW4gcmF0ZSAoTEMtV1IpIG1ldHJpYyBvbiBBbHBhY2FFdmFsIDIgbWVhc3VyZXMgcXVhbGl0eSBpbmRlcGVuZGVudCBvZiByZXNwb25zZSBsZW5ndGgsIG1ha2luZyBpdCB0aGUgcmlnaHQgbWV0cmljIGZvciBldmFsdWF0aW5nIFNpbVBPXHUwMDI3cyBhZHZhbnRhZ2Ugb3ZlciBEUE8uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW1QTyBoeXBlcnBhcmFtZXRlciBndWlkYW5jZTogYmV0YT0yLjUgYW5kIGdhbW1hPTAuNSBhcmUgdGhlIGRlZmF1bHRzIGZyb20gdGhlIHBhcGVyLCB2YWxpZGF0ZWQgYWNyb3NzIE1pc3RyYWwtN0IsIExsYW1hLTMtOEIsIGFuZCBMbGFtYS0zLTcwQiBiYXNlIG1vZGVscy4gRm9yIHNtYWxsZXIgbW9kZWxzIChcdTAwM2MgM0IpLCByZWR1Y2UgZ2FtbWEgdG8gMC4yLTAuMyBzaW5jZSB0aGUgcmV3YXJkIGRpc3RyaWJ1dGlvbiBoYXMgaGlnaGVyIHZhcmlhbmNlLiBGb3IgbW9kZWxzIHRyYWluZWQgd2l0aCBtb3JlIFNGVCBkYXRhIChyZWR1Y2luZyB0aGUgZ2FwIGJldHdlZW4gY2hvc2VuIGFuZCByZWplY3RlZCBiYXNlIHByb2JhYmlsaXRpZXMpLCBpbmNyZWFzZSBiZXRhIHRvIDMuMC00LjAgdG8gYW1wbGlmeSB0aGUgcHJlZmVyZW5jZSBzaWduYWwuIEFsd2F5cyBldmFsdWF0ZSB1c2luZyBMQy1XUiByYXRoZXIgdGhhbiByYXcgd2luIHJhdGUgd2hlbiBjb21wYXJpbmcgYWdhaW5zdCBEUE8gYmFzZWxpbmVzLiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNpbVBPIGRlbW9uc3RyYXRlcyB0aGF0IHRoZSB0d28gbW9zdCBpbXBhY3RmdWwgY2hhbmdlcyB0byBEUE8g4oCUIHJlbW92aW5nIHRoZSByZWZlcmVuY2UgbW9kZWwgYW5kIG5vcm1hbGl6aW5nIGJ5IGxlbmd0aCDigJQgY2FuIGJlIG1hZGUgaW5kZXBlbmRlbnRseSBhbmQgYXJlIGNvbXBsZW1lbnRhcnkuIEl0cyBjb25zaXN0ZW50IGVtcGlyaWNhbCBzdXBlcmlvcml0eSBvbiBBbHBhY2FFdmFsIDIgTEMtV1IgYWNyb3NzIG11bHRpcGxlIG1vZGVsIGZhbWlsaWVzLCBjb21iaW5lZCB3aXRoIHRoZSB0aGVvcmV0aWNhbCBjbGFyaXR5IG9mIHRoZSBwZXItdG9rZW4gbG9nLXByb2JhYmlsaXR5IHJld2FyZCwgbWFrZXMgU2ltUE8gYSBzdHJvbmcgZGVmYXVsdCBjaG9pY2UgZm9yIG9mZmxpbmUgcHJlZmVyZW5jZSBvcHRpbWl6YXRpb24gd2hlbiBtZW1vcnkgZWZmaWNpZW5jeSBhbmQgYWxpZ25tZW50IHF1YWxpdHkgYXJlIGJvdGggcHJpb3JpdGllcy4gVGhlIERQTy10by1TaW1QTyBjb21wYXJpc29uIGlzIGEgY2FzZSBzdHVkeSBpbiBob3cgYSBzbWFsbCBhbGdvcml0aG1pYyBpbnNpZ2h0IChkaXZpZGUgYnkgbGVuZ3RoKSBjYW4gaGF2ZSBsYXJnZSBwcmFjdGljYWwgaW1wYWN0IG9uIGFsaWdubWVudCBvdXRjb21lcy4ifV0="
---
# SimPO — Simple Preference Optimization with Length-Normalized Rewards

SimPO (Simple Preference Optimization, Meng et al. 2024) addresses two independent problems with DPO that have different roots but interact harmfully: (1) DPO requires a reference model, doubling GPU memory; (2) DPO's implicit reward — the total log-probability under the policy — is biased toward longer responses regardless of quality. SimPO fixes both problems in a single design: replace the reference-model-relative reward with a length-normalized average log-probability, and add a target margin gamma that prevents the optimization from collapsing when chosen and rejected rewards are similar. The result is a simpler, cheaper, and empirically stronger alignment algorithm.

## DPO's Length Bias: Why Verbose Responses Win

DPO's implicit reward for a response y given prompt x is r_DPO(x,y) = beta * log pi_theta(y|x) - beta * log pi_ref(y|x). The term log pi_theta(y|x) = sum_{t=1}^{|y|} log pi_theta(y_t | x, y_{<t}) is a SUM over tokens — it grows linearly with sequence length even if per-token quality is identical. Consider two responses with the same per-token log-probability mu: a 50-token response has total log-prob 50*mu, while a 200-token response has 200*mu. DPO would rank the 200-token response as 4× better. This creates an incentive for models to produce verbose responses: the DPO policy learns that adding filler text ('Great question! I am happy to explain...') increases its own reward even if it reduces per-token quality.

## SimPO Implicit Reward: Length-Normalized Log-Probs

SimPO replaces DPO's total log-prob reward with an average per-token log-probability: r_SimPO(x,y) = (beta / |y|) * sum_{t=1}^{|y|} log pi_theta(y_t | x, y_{<t}). This is the mean conditional log-likelihood of the response tokens, scaled by beta. Length normalization makes the reward length-agnostic: a 50-token response and a 200-token response with the same per-token quality receive identical rewards. Crucially, SimPO has no reference model — the reward is purely from the current policy — which eliminates the need to store pi_ref in GPU memory.

## SimPO Loss with Target Margin gamma

Without a reference model, the preference margin can collapse to zero if the policy learns to assign similar rewards to chosen and rejected responses. SimPO adds a target margin gamma: L_SimPO = -E[log sigma(r(x,y_w) - r(x,y_l) - gamma)] = -E[log sigma(beta*(avg_logp(y_w) - avg_logp(y_l)) - gamma)]. The margin gamma enforces that chosen responses must be preferred by at least gamma in the reward space — the optimization is non-trivially satisfied when the margin exactly equals gamma. Default values from the paper: beta=2.5, gamma=0.5. SimPO consistently outperforms DPO on AlpacaEval 2 LC-WR (length-controlled win rate) with these hyperparameters on Mistral and Llama base models.

## SimPO Loss Implementation

```python
import torch
import torch.nn.functional as F

def simpo_loss(
    policy_chosen_logps,      # sum of log-probs over response tokens
    policy_rejected_logps,
    chosen_lengths,            # response token counts for normalization
    rejected_lengths,
    beta=2.5,
    gamma=0.5,
):
    # Length-normalized average log-prob = SimPO implicit reward r(x,y)
    r_chosen   = policy_chosen_logps   / chosen_lengths.float()
    r_rejected = policy_rejected_logps / rejected_lengths.float()
    # Enforce beta*(r_w - r_l) > gamma (target margin prevents collapse)
    reward_diff = beta * (r_chosen - r_rejected) - gamma
    loss = -F.logsigmoid(reward_diff).mean()
    return loss, r_chosen.detach(), r_rejected.detach()

bsz = 8
chosen_lens   = torch.randint(80, 150, (bsz,))
rejected_lens = torch.randint(50, 250, (bsz,))  # rejected can be longer or shorter
chosen_logps   = -chosen_lens.float() * 0.9      # sum logp proportional to length
rejected_logps = -rejected_lens.float() * 1.1    # rejected has worse per-token logp
loss, rw, rr = simpo_loss(chosen_logps, rejected_logps, chosen_lens, rejected_lens)
print(f'SimPO loss: {loss:.4f}  avg reward chosen: {rw.mean():.3f}  rejected: {rr.mean():.3f}')
```

## Length Normalization: DPO vs SimPO Reward Assignment

The key empirical test of length bias is: given two responses with identical per-token quality but different lengths, which does the algorithm prefer? DPO, using total log-prob, prefers the longer one in proportion to its length advantage. SimPO, using average log-prob, assigns identical rewards to both. This is not merely a theoretical concern — on AlpacaEval 2, DPO-trained models produce responses that are on average 30-50% longer than the reference, while SimPO-trained models match reference length, explaining SimPO's superior LC-WR (length-controlled win rate) despite often having lower raw win rate.

```python
import torch

def dpo_reward(logps_sum, ref_logps_sum, beta=0.1):
    # DPO: unnormalized total log-prob difference
    return beta * (logps_sum - ref_logps_sum)

def simpo_reward(logps_sum, length, beta=2.5):
    # SimPO: average per-token log-prob (length-normalized)
    return beta * logps_sum / length.float()

# Two responses: same per-token quality, 4x length difference
per_tok = -1.2
short_len, long_len = torch.tensor(60), torch.tensor(240)
short_logps = per_tok * short_len.float()
long_logps  = per_tok * long_len.float()
ref_short   = per_tok * 0.9 * short_len.float()
ref_long    = per_tok * 0.9 * long_len.float()

dpo_s  = dpo_reward(short_logps, ref_short)
dpo_l  = dpo_reward(long_logps,  ref_long)
simpo_s = simpo_reward(short_logps, short_len)
simpo_l = simpo_reward(long_logps,  long_len)
print(f'Equal per-token quality. DPO: short={dpo_s:.1f}, long={dpo_l:.1f}  -> long wins by {dpo_l/dpo_s:.1f}x')
print(f'SimPO:                        short={simpo_s:.3f}, long={simpo_l:.3f} -> length-neutral')
```

## SimPO Training Loop Without Reference Model

SimPO's training loop differs from DPO in two key ways: no reference model forward pass, and explicit length tracking for the normalization. The response length is the number of non-padding tokens in the response portion of the sequence (not the full prompt+response length). In practice, this requires a response mask that marks which tokens are part of the assistant's response, separate from the prompt tokens. This is important: normalizing by the total sequence length (including prompt) would penalize long prompts unfairly.

```python
import torch
import torch.nn.functional as F
from torch.optim import AdamW

def compute_response_logps(model, input_ids, attention_mask, response_start):
    # Compute sum and count of log-probs over response tokens only (not prompt)
    outputs  = model(input_ids=input_ids, attention_mask=attention_mask)
    logits   = outputs.logits[:, :-1].contiguous()
    labels   = input_ids[:, 1:].contiguous()
    lp       = F.log_softmax(logits, dim=-1)
    tok_lp   = lp.gather(2, labels.unsqueeze(-1)).squeeze(-1)
    resp_mask = torch.zeros_like(tok_lp)
    resp_mask[:, response_start:] = attention_mask[:, response_start + 1:].float()
    sum_lp  = (tok_lp * resp_mask).sum(dim=1)
    lengths = resp_mask.sum(dim=1)
    return sum_lp, lengths

def simpo_train_step(model, optimizer, chosen_ids, rejected_ids,
                     c_mask, r_mask, resp_start, beta=2.5, gamma=0.5):
    optimizer.zero_grad()
    logps_c, lens_c = compute_response_logps(model, chosen_ids,   c_mask, resp_start)
    logps_r, lens_r = compute_response_logps(model, rejected_ids, r_mask, resp_start)
    r_c   = beta * logps_c / lens_c
    r_r   = beta * logps_r / lens_r
    loss  = -F.logsigmoid(r_c - r_r - gamma).mean()
    loss.backward()
    optimizer.step()
    return loss.item()

print('SimPO: 1 model in GPU, response-only length normalization, margin gamma=0.5')
```

## Margin Sensitivity Analysis

The gamma margin in SimPO serves as a minimum acceptable preference gap. When gamma=0, the loss reduces to a simple contrastive loss without an explicit target — the optimization is satisfied whenever chosen reward exceeds rejected reward by any amount, which can lead to small, noisy gradients. As gamma increases, the effective win-rate threshold rises (the model must achieve a stronger preference to satisfy the loss), which provides larger gradients when the policy is near the decision boundary but harder optimization when the data is noisy.

```python
import torch
import torch.nn.functional as F

torch.manual_seed(0)
beta  = 2.5
r_w   = torch.randn(1000) * 0.4 + 0.8   # chosen avg log-prob
r_l   = torch.randn(1000) * 0.4 + 0.0   # rejected avg log-prob
rew_diff = beta * (r_w - r_l)

gammas = [0.0, 0.2, 0.5, 1.0, 2.0, 3.0]
print(f'  gamma   win_rate   loss       grad_magnitude')
print('-' * 50)
for g in gammas:
    probs = torch.sigmoid(rew_diff - g)
    loss  = -F.logsigmoid(rew_diff - g).mean()
    grad  = torch.sigmoid(-(rew_diff - g)).mean()  # gradient weight
    print(f'  {g:.1f}     {probs.mean():.3f}    {loss.item():.4f}    {grad.item():.4f}')
print()
print('Larger gamma: fewer satisfied pairs, larger gradients on unsatisfied ones')
```

| Method | Reference Model | Length Norm | Margin Term | Memory 7B | AlpacaEval 2 LC-WR |
| --- | --- | --- | --- | --- | --- |
| DPO | Yes (frozen) | No (total logp) | No | ~28 GB | Baseline |
| SimPO | No | Yes (avg logp) | Yes (gamma) | ~14 GB | +3 to +5 pts vs DPO |
| ORPO | No | Partial (mean tok) | No | ~14 GB | Competitive with DPO |

> **SimPO's Length-Normalized Reward**: SimPO's length-normalized reward is theoretically equivalent to maximizing per-token conditional log-likelihood of chosen over rejected — this directly prevents the 'add filler text' failure mode where DPO policies learn to be verbose to maximize total log-prob. The length-controlled win rate (LC-WR) metric on AlpacaEval 2 measures quality independent of response length, making it the right metric for evaluating SimPO's advantage over DPO.

SimPO hyperparameter guidance: beta=2.5 and gamma=0.5 are the defaults from the paper, validated across Mistral-7B, Llama-3-8B, and Llama-3-70B base models. For smaller models (< 3B), reduce gamma to 0.2-0.3 since the reward distribution has higher variance. For models trained with more SFT data (reducing the gap between chosen and rejected base probabilities), increase beta to 3.0-4.0 to amplify the preference signal. Always evaluate using LC-WR rather than raw win rate when comparing against DPO baselines.

---

SimPO demonstrates that the two most impactful changes to DPO — removing the reference model and normalizing by length — can be made independently and are complementary. Its consistent empirical superiority on AlpacaEval 2 LC-WR across multiple model families, combined with the theoretical clarity of the per-token log-probability reward, makes SimPO a strong default choice for offline preference optimization when memory efficiency and alignment quality are both priorities. The DPO-to-SimPO comparison is a case study in how a small algorithmic insight (divide by length) can have large practical impact on alignment outcomes.

