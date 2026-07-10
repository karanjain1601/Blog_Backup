---
title: "Shared Experts in MoE Architectures"
slug: "shared-experts-moe"
description: "Combining a set of always-active shared expert(s) with conditionally-routed sparse experts to handle common knowledge while sparse experts specialize — as in DeepSeek-MoE and DS-MoE."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgTW9FIHJvdXRlcyBldmVyeSB0b2tlbiB0byBhIHNtYWxsIHN1YnNldCBvZiBleHBlcnRzLCBsZWF2aW5nIGNvbW1vbiBsaW5ndWlzdGljIHBhdHRlcm5zIHRvIGJlIGxlYXJuZWQgcmVkdW5kYW50bHkgYWNyb3NzIG11bHRpcGxlIGV4cGVydHMuIFNoYXJlZCBleHBlcnRzIGFkZHJlc3MgdGhpcyBieSBpbnRyb2R1Y2luZyBhIGRlZGljYXRlZCBzZXQgb2YgYWx3YXlzLWFjdGl2ZSBleHBlcnRzIHRoYXQgcHJvY2VzcyBldmVyeSB0b2tlbiB1bmNvbmRpdGlvbmFsbHkg4oCUIHRoZXkgc2VydmUgYXMgYSBcdTAwMjdjb21tb24ga25vd2xlZGdlIHN0b3JlXHUwMDI3IGZvciBwYXR0ZXJucyB0aGF0IGFwcGVhciB1bml2ZXJzYWxseSBhY3Jvc3MgYWxsIGlucHV0cy4gVGhlIHJlbWFpbmluZyBleHBlcnRzIGFyZSBzcGFyc2UgYW5kIGNvbmRpdGlvbmFsbHkgcm91dGVkIGFzIGluIHN0YW5kYXJkIE1vRS4gVGhpcyBoeWJyaWQgZGVzaWduLCBpbnRyb2R1Y2VkIGluIERlZXBTZWVrLU1vRSAoRGFpIGV0IGFsLiwgMjAyNCkgYW5kIHVzZWQgaW4gRGVlcFNlZWstVjIsIGNsZWFubHkgc2VwYXJhdGVzIHVuaXZlcnNhbCBrbm93bGVkZ2UgKHNoYXJlZCBleHBlcnRzKSBmcm9tIHNwZWNpYWxpc2VkIGRvbWFpbiBrbm93bGVkZ2UgKHJvdXRlZCBleHBlcnRzKSwgaW1wcm92aW5nIG92ZXJhbGwgcGFyYW1ldGVyIGVmZmljaWVuY3kgYW5kIGFsbG93aW5nIHJvdXRlZCBleHBlcnRzIHRvIHNwZWNpYWxpc2UgbW9yZSBhZ2dyZXNzaXZlbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIGEgc2hhcmVkLWV4cGVydCBNb0UgbGF5ZXIsIHRoZSBvdXRwdXQgaXMgdGhlIHN1bSBvZiB0d28gY29tcG9uZW50czogKDEpIHRoZSBzdW0gb2Ygb3V0cHV0cyBmcm9tIE5fcyBzaGFyZWQgZXhwZXJ0cyB0aGF0IGFsd2F5cyBhY3RpdmF0ZSwgYW5kICgyKSB0aGUgd2VpZ2h0ZWQgc3VtIG9mIHRvcC1LX3Igc2VsZWN0ZWQgb3V0cHV0cyBmcm9tIE5fciByb3V0ZWQgZXhwZXJ0cy4gVGhlIHNoYXJlZCBleHBlcnRzIGNvbnRyaWJ1dGUgYSBmaXhlZCwgZ2VuZXJhbCB0cmFuc2Zvcm1hdGlvbiB0byBldmVyeSB0b2tlbjsgdGhlIHJvdXRlZCBleHBlcnRzIGNvbnRyaWJ1dGUgYSB0b2tlbi1zcGVjaWZpYywgc3BlY2lhbGlzZWQgdHJhbnNmb3JtYXRpb24uIFRoZSBsb2FkLWJhbGFuY2luZyBhdXhpbGlhcnkgbG9zcyBpcyBhcHBsaWVkIG9ubHkgdG8gdGhlIHJvdXRlZCBleHBlcnRzIOKAlCBzaW5jZSBzaGFyZWQgZXhwZXJ0cyBwcm9jZXNzIGFsbCB0b2tlbnMgZXF1YWxseSwgdGhleSBuZWVkIG5vIGJhbGFuY2luZy4gVGhlIG92ZXJhbGwgYWN0aXZlLXBhcmFtZXRlciBjb3VudCBwZXIgdG9rZW4gaXMgTl9zICsgS19yIGV4cGVydHMsIGNvbXBhcmVkIHRvIEtfciBpbiBhIHB1cmUgc3BhcnNlIE1vRS4gSW4gRGVlcFNlZWstVjIsIE5fcz0yIHNoYXJlZCBhbmQgS19yPTYgb2YgTl9yPTE2MCByb3V0ZWQgZXhwZXJ0cyBhY3RpdmF0ZSBwZXIgdG9rZW4sIGdpdmluZyA4IGFjdGl2ZSBleHBlcnQgdW5pdHMgcGVyIHRva2VuIHdpdGggMjM2QiB0b3RhbCBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vdGl2YXRpb24gZm9yIFNoYXJlZCBFeHBlcnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbW90aXZhdGlvbiBmb3Igc2hhcmVkIGV4cGVydHMgY29tZXMgZnJvbSBhbiBlbXBpcmljYWwgb2JzZXJ2YXRpb24gaW4gY29hcnNlIE1vRTogZXhwZXJ0IHdlaWdodCBtYXRyaWNlcyBzaG93IGhpZ2ggcGFpcndpc2UgY29zaW5lIHNpbWlsYXJpdHkgZm9yIGNlcnRhaW4gY29tcG9uZW50cy4gVGhpcyBzdWdnZXN0cyB0aGF0IG11bHRpcGxlIGV4cGVydHMgYXJlIGxlYXJuaW5nIHRoZSBzYW1lIHRyYW5zZm9ybWF0aW9uIOKAlCB3YXN0aW5nIHBhcmFtZXRlcnMgb24gcmVkdW5kYW50IGNvbW1vbiBrbm93bGVkZ2UgaW5zdGVhZCBvZiBkZXZlbG9waW5nIHVuaXF1ZSBzcGVjaWFsaXNhdGlvbnMuIFRoZSByZWR1bmRhbmN5IGFyaXNlcyBiZWNhdXNlLCBpbiBzdGFuZGFyZCBNb0UsIGV2ZW4gdGhvdWdoIGVhY2ggZXhwZXJ0IHByb2Nlc3NlcyBvbmx5IDEvTiB0b2tlbnMgb24gYXZlcmFnZSwgdGhvc2UgdG9rZW5zIHNwYW4gbWFueSBkaWZmZXJlbnQgbGluZ3Vpc3RpYyBwYXR0ZXJucy4gQW4gZXhwZXJ0IHRoYXQgcHJvY2Vzc2VzIGRpdmVyc2UgdG9rZW5zIG11c3QgbGVhcm4gZGl2ZXJzZSBmdW5jdGlvbnMsIGxlYWRpbmcgdG8gYSBcdTAwMjdqYWNrIG9mIGFsbCB0cmFkZXNcdTAwMjcgcmVwcmVzZW50YXRpb24gdGhhdCBvdmVybGFwcyB3aXRoIG90aGVyIGV4cGVydHMuIEJ5IG9mZmxvYWRpbmcgdGhlIG1vc3QgdW5pdmVyc2FsIHBhdHRlcm5zIHRvIGRlZGljYXRlZCBzaGFyZWQgZXhwZXJ0cywgcm91dGVkIGV4cGVydHMgYXJlIGZyZWUgdG8gc3BlY2lhbGlzZSBpbiBuYXJyb3dlciBhbmQgbW9yZSBkaXN0aW5jdCBkb21haW5zLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRXhwZXJ0IHdlaWdodCBjb3NpbmUgc2ltaWxhcml0eSBpbiBjb2Fyc2UgTW9FIGlzIGhpZ2hlciB0aGFuIGV4cGVjdGVkIOKAlCBleHBlcnRzIGxlYXJuIHJlZHVuZGFudCBmdW5jdGlvbnMiLCJDb21tb24gbGluZ3Vpc3RpYyBwYXR0ZXJucyAoZnVuY3Rpb24gd29yZHMsIHB1bmN0dWF0aW9uLCBiYXNpYyBncmFtbWFyKSBhcHBlYXIgaW4gYWxsIHRva2VuIGNvbnRleHRzIiwiU2hhcmVkIGV4cGVydHMgbGVhcm4gdGhlc2UgdW5pdmVyc2FsIHBhdHRlcm5zIG9uY2UsIG5vdCByZWR1bmRhbnRseSBhY3Jvc3MgbXVsdGlwbGUgcm91dGVkIGV4cGVydHMiLCJSb3V0ZWQgZXhwZXJ0IHNwZWNpYWxpc2F0aW9uIGltcHJvdmVzIGJlY2F1c2UgdGhleSBubyBsb25nZXIgbmVlZCB0byBjb3ZlciBjb21tb24gcGF0dGVybnMiLCJMb2FkLWJhbGFuY2luZyBwcmVzc3VyZSBvbiByb3V0ZWQgZXhwZXJ0cyBpcyByZWR1Y2VkIOKAlCB0aGV5IGhhbmRsZSBhIG1vcmUgc2VwYXJhYmxlIHRhc2siLCJBYmxhdGlvbnMgc2hvdyB0aGF0IHJlbW92aW5nIHNoYXJlZCBleHBlcnRzIHJlZHVjZXMgZG93bnN0cmVhbSBhY2N1cmFjeSBieSAwLjXigJMxLjUgcG9pbnRzIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFyY2hpdGVjdHVyZSBEZXNpZ24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzaGFyZWQtZXhwZXJ0IE1vRSBsYXllciBoYXMgdGhyZWUgY29tcG9uZW50czogYSByb3V0ZXIsIE5fcyBzaGFyZWQgZXhwZXJ0cywgYW5kIE5fciByb3V0ZWQgZXhwZXJ0cy4gVGhlIHJvdXRlciBpcyBpZGVudGljYWwgdG8gc3RhbmRhcmQgTW9FIOKAlCBhIGxpbmVhciBwcm9qZWN0aW9uIGZyb20gZF9tb2RlbCB0byBOX3IgKG5vdCBOX3IgKyBOX3MsIHNpbmNlIHNoYXJlZCBleHBlcnRzIG5lZWQgbm8gcm91dGluZykuIFNoYXJlZCBleHBlcnRzIGFyZSBzdGFuZGFyZCBGRk5zIChMaW5lYXIg4oaSIEdFTFUg4oaSIExpbmVhcikgd2l0aCB0aGUgc2FtZSBhcmNoaXRlY3R1cmUgYXMgcm91dGVkIGV4cGVydHMuIE9uIHRoZSBmb3J3YXJkIHBhc3MsIGlucHV0IHggaXMgcHJvY2Vzc2VkIGJ5IGFsbCBOX3Mgc2hhcmVkIGV4cGVydHMgaW4gcGFyYWxsZWwgKHN1bSB0aGVpciBvdXRwdXRzKSwgYW5kIGluZGVwZW5kZW50bHkgcHJvY2Vzc2VkIGJ5IHRoZSB0b3AtS19yIHNlbGVjdGVkIHJvdXRlZCBleHBlcnRzICh3ZWlnaHRlZCBzdW0pLiBUaGUgdHdvIGNvbXBvbmVudHMgYXJlIGFkZGVkIGVsZW1lbnQtd2lzZS4gU2luY2Ugc2hhcmVkIGV4cGVydCBvdXRwdXRzIGFyZSBub3QgZ2F0ZWQsIG5vIHJvdXRpbmcgd2VpZ2h0IGlzIGFwcGxpZWQg4oCUIGVhY2ggc2hhcmVkIGV4cGVydCBjb250cmlidXRlcyBpdHMgZnVsbCBvdXRwdXQuIEluIERlZXBTZWVrLU1vRSwgc2hhcmVkIGV4cGVydHMgaGF2ZSB0aGUgc2FtZSBoaWRkZW4gZGltZW5zaW9uIGFzIHJvdXRlZCBleHBlcnRzIChkX2ZmL20gZm9yIGZpbmUtZ3JhaW5lZCB2YXJpYW50cykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFNoYXJlZEV4cGVydE1vRUxheWVyKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTW9FIGxheWVyIHdpdGggYWx3YXlzLWFjdGl2ZSBzaGFyZWQgZXhwZXJ0cyArIHRvcC1LIHJvdXRlZCBleHBlcnRzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsOiBpbnQsIGRfZmY6IGludCxcbiAgICAgICAgICAgICAgICAgbl9zaGFyZWQ6IGludCwgbl9yb3V0ZWQ6IGludCwgdG9wX2s6IGludCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5fcm91dGVkLCBzZWxmLnRvcF9rID0gbl9yb3V0ZWQsIHRvcF9rXG4gICAgICAgIHNlbGYucm91dGVyID0gbm4uTGluZWFyKGRfbW9kZWwsIG5fcm91dGVkLCBiaWFzPUZhbHNlKVxuICAgICAgICAjIFNoYXJlZCBleHBlcnRzOiBhbHdheXMgYWN0aXZlLCBubyByb3V0aW5nIHdlaWdodFxuICAgICAgICBzZWxmLnNoYXJlZF9leHBlcnRzID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKSwgbm4uR0VMVSgpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICBubi5MaW5lYXIoZF9mZiwgZF9tb2RlbCkpIGZvciBfIGluIHJhbmdlKG5fc2hhcmVkKV0pXG4gICAgICAgICMgUm91dGVkIGV4cGVydHM6IHNwYXJzZSwgY29uZGl0aW9uYWxseSBhY3RpdmF0ZWRcbiAgICAgICAgc2VsZi5yb3V0ZWRfZXhwZXJ0cyA9IG5uLk1vZHVsZUxpc3QoW1xuICAgICAgICAgICAgbm4uU2VxdWVudGlhbChubi5MaW5lYXIoZF9tb2RlbCwgZF9mZiksIG5uLkdFTFUoKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgbm4uTGluZWFyKGRfZmYsIGRfbW9kZWwpKSBmb3IgXyBpbiByYW5nZShuX3JvdXRlZCldKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgIyAxLiBTaGFyZWQgZXhwZXJ0IHBhc3MgKGFsd2F5cyBhY3RpdmUsIG5vIGdhdGluZylcbiAgICAgICAgc2hhcmVkX291dCA9IHN1bShlKHgpIGZvciBlIGluIHNlbGYuc2hhcmVkX2V4cGVydHMpICAjIChCLCBULCBEKVxuICAgICAgICAjIDIuIFJvdXRlZCBleHBlcnQgcGFzcyAodG9wLUsgb2YgTl9yKVxuICAgICAgICBCLCBULCBEID0geC5zaGFwZVxuICAgICAgICB4ZiA9IHgudmlldyhCICogVCwgRClcbiAgICAgICAgcHJvYnMsIGlkeCA9IHRvcmNoLnRvcGsoRi5zb2Z0bWF4KHNlbGYucm91dGVyKHhmKSwgLTEpLCBzZWxmLnRvcF9rLCAtMSlcbiAgICAgICAgcHJvYnMgPSBwcm9icyAvIHByb2JzLnN1bSgtMSwga2VlcGRpbT1UcnVlKVxuICAgICAgICByb3V0ZWQgPSB0b3JjaC56ZXJvc19saWtlKHhmKVxuICAgICAgICBmb3IgayBpbiByYW5nZShzZWxmLnRvcF9rKTpcbiAgICAgICAgICAgIGZvciBlLCBleHBlcnQgaW4gZW51bWVyYXRlKHNlbGYucm91dGVkX2V4cGVydHMpOlxuICAgICAgICAgICAgICAgIG0gPSBpZHhbOiwga10gPT0gZVxuICAgICAgICAgICAgICAgIGlmIG0uYW55KCk6XG4gICAgICAgICAgICAgICAgICAgIHJvdXRlZFttXSArPSBwcm9ic1ttLCBrOmsrMV0gKiBleHBlcnQoeGZbbV0pXG4gICAgICAgIHJldHVybiBzaGFyZWRfb3V0ICsgcm91dGVkLnZpZXcoQiwgVCwgRClcblxubGF5ZXIgPSBTaGFyZWRFeHBlcnRNb0VMYXllcig1MTIsIDEwMjQsIG5fc2hhcmVkPTIsIG5fcm91dGVkPTMyLCB0b3Bfaz00KVxucHJpbnQoZlwiT3V0cHV0OiB7bGF5ZXIodG9yY2gucmFuZG4oMiwgOCwgNTEyKSkuc2hhcGV9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUm91dGluZyB3aXRoIFNoYXJlZCArIFJvdXRlZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJvdXRlciBpbiBhIHNoYXJlZC1leHBlcnQgTW9FIG9ubHkgbmVlZHMgdG8gc2NvcmUgdGhlIE5fciByb3V0ZWQgZXhwZXJ0cyDigJQgdGhlIE5fcyBzaGFyZWQgZXhwZXJ0cyBhcmUgYWx3YXlzIGFjdGl2ZSBhbmQgcmVxdWlyZSBubyBzY29yZS4gVGhpcyBrZWVwcyB0aGUgcm91dGVyIHNtYWxsZXIgdGhhbiBpdCB3b3VsZCBiZSBpZiBzaGFyZWQgZXhwZXJ0cyB3ZXJlIGluY2x1ZGVkIGluIHRoZSByb3V0aW5nIGRlY2lzaW9uLiBUaGUgcm91dGluZyBtZWNoYW5pc20gaXMgaWRlbnRpY2FsIHRvIHN0YW5kYXJkIHRvcC1LIHJvdXRpbmc6IHNvZnRtYXggb3ZlciBOX3IgbG9naXRzLCB0YWtlIHRvcC1LX3IsIHJlbm9ybWFsaXNlLCB3ZWlnaHRlZCBzdW0uIEJlY2F1c2UgdGhlIHNoYXJlZCBleHBlcnRzIGFscmVhZHkgcHJvdmlkZSBhIHVuaXZlcnNhbCBiYXNlIHRyYW5zZm9ybWF0aW9uLCB0aGUgcm91dGVkIGV4cGVydHMgbmVlZCBvbmx5IHByb2R1Y2UgYSByZXNpZHVhbCBzcGVjaWFsaXNlZCBjb3JyZWN0aW9uLiBUaGlzIG1lYW5zIHRoZSByb3V0aW5nIHdlaWdodHMgZG8gbm90IG5lZWQgdG8gYmUgYXMgc2hhcnAg4oCUIGEgbW9kZXJhdGUgcHJlZmVyZW5jZSBmb3IgY2VydGFpbiByb3V0ZWQgZXhwZXJ0cyBpcyBzdWZmaWNpZW50LiBJbiBwcmFjdGljZSwgdGhpcyBsZWFkcyB0byBtb3JlIHN0YWJsZSByb3V0aW5nIGFuZCBsZXNzIGNvbGxhcHNlIGNvbXBhcmVkIHRvIHB1cmUgc3BhcnNlIE1vRSB3aXRoIHRoZSBzYW1lIG51bWJlciBvZiByb3V0ZWQgZXhwZXJ0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBrbm93bGVkZ2VfZGVjb21wb3NpdGlvbl9hbmFseXNpcyhzaGFyZWRfd2VpZ2h0czogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJvdXRlZF93ZWlnaHRzOiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJNZWFzdXJlIGhvdyBkaWZmZXJlbnQgc2hhcmVkIHZzIHJvdXRlZCBleHBlcnQgd2VpZ2h0cyBhcmUuXG4gICAgc2hhcmVkX3dlaWdodHM6IChuX3NoYXJlZCwgZF9pbipkX291dCkgIHJvdXRlZF93ZWlnaHRzOiAobl9yb3V0ZWQsIGRfaW4qZF9vdXQpXG4gICAgSHlwb3RoZXNpczogc2hhcmVkIGV4cGVydHMgc2hvdWxkIGRpZmZlciBmcm9tIHJvdXRlZCBleHBlcnRzXG4gICAgKHRoZXkgY2FwdHVyZSBkaWZmZXJlbnQgcGF0dGVybnMpLCBhbmQgcm91dGVkIGV4cGVydHMgZGlmZmVyIGZyb20gZWFjaCBvdGhlci5cIlwiXCJcbiAgICBzaGFyZWRfbm9ybSA9IEYubm9ybWFsaXplKHNoYXJlZF93ZWlnaHRzLCBkaW09LTEpICAgICAgICMgKG5fcywgRClcbiAgICByb3V0ZWRfbm9ybSA9IEYubm9ybWFsaXplKHJvdXRlZF93ZWlnaHRzLCBkaW09LTEpICAgICAgICMgKG5fciwgRClcbiAgICAjIFNoYXJlZCB2cyByb3V0ZWQgc2ltaWxhcml0eSAoc2hvdWxkIGJlIGxvdyDigJQgZGlmZmVyZW50IGZ1bmN0aW9ucylcbiAgICBzcl9zaW0gPSAoc2hhcmVkX25vcm0udW5zcXVlZXplKDEpICogcm91dGVkX25vcm0udW5zcXVlZXplKDApKS5zdW0oLTEpICAjIChuX3MsIG5fcilcbiAgICAjIFJvdXRlZCB2cyByb3V0ZWQgc2ltaWxhcml0eSAoc2hvdWxkIGJlIGxvdyDigJQgZGl2ZXJzZSBzcGVjaWFsaXNhdGlvbilcbiAgICBycl9zaW0gPSByb3V0ZWRfbm9ybSBAIHJvdXRlZF9ub3JtLlQgICAgICAgICAgICAgICAgICAgICMgKG5fciwgbl9yKVxuICAgIG1hc2sgICA9IH50b3JjaC5leWUocm91dGVkX25vcm0uc2hhcGVbMF0sIGR0eXBlPXRvcmNoLmJvb2wpXG4gICAgcmV0dXJuIHtcbiAgICAgICAgXCJzaGFyZWRfdnNfcm91dGVkX21lYW5fc2ltXCI6IHNyX3NpbS5tZWFuKCkuaXRlbSgpLFxuICAgICAgICBcInJvdXRlZF92c19yb3V0ZWRfbWVhbl9zaW1cIjogcnJfc2ltW21hc2tdLm1lYW4oKS5pdGVtKCksXG4gICAgICAgIFwicm91dGVkX2RpdmVyc2l0eVwiOiAxIC0gcnJfc2ltW21hc2tdLm1lYW4oKS5pdGVtKCksXG4gICAgfVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuc2hhcmVkID0gdG9yY2gucmFuZG4oMiwgNTEyICogMjU2KVxucm91dGVkID0gdG9yY2gucmFuZG4oMzIsIDUxMiAqIDI1NilcbnN0YXRzICA9IGtub3dsZWRnZV9kZWNvbXBvc2l0aW9uX2FuYWx5c2lzKHNoYXJlZCwgcm91dGVkKVxuZm9yIGssIHYgaW4gc3RhdHMuaXRlbXMoKTpcbiAgICBwcmludChmXCJ7a306IHt2Oi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLbm93bGVkZ2UgRGVjb21wb3NpdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRoZW9yZXRpY2FsIG1vdGl2YXRpb24gZm9yIHNoYXJlZCBleHBlcnRzIGlzIHRoYXQgdGhlIGluZm9ybWF0aW9uIHByb2Nlc3NlZCBieSBhbiBNb0UgbGF5ZXIgY2FuIGJlIGRlY29tcG9zZWQgaW50byB0d28gb3J0aG9nb25hbCBjb21wb25lbnRzOiBnZW5lcmFsIGluZm9ybWF0aW9uIHRoYXQgaXMgY29udGV4dC1pbmRlcGVuZGVudCBhbmQgdW5pdmVyc2FsIChzdWNoIGFzIGJhc2ljIHRva2VuIHR5cGUgdHJhbnNmb3JtYXRpb25zLCBwb3NpdGlvbmFsIGNvbnRleHQsIGFuZCBncmFtbWF0aWNhbCBzdHJ1Y3R1cmUpLCBhbmQgc3BlY2lhbGlzZWQgaW5mb3JtYXRpb24gdGhhdCBkZXBlbmRzIG9uIHRoZSBzcGVjaWZpYyBkb21haW4sIHRvcGljLCBvciBsaW5ndWlzdGljIHJlZ2lzdGVyIG9mIHRoZSBpbnB1dC4gU2hhcmVkIGV4cGVydHMgYXJlIHJlc3BvbnNpYmxlIGZvciB0aGUgZ2VuZXJhbCBjb21wb25lbnQ7IHJvdXRlZCBleHBlcnRzIGhhbmRsZSB0aGUgc3BlY2lhbGlzZWQgY29tcG9uZW50LiBUaGlzIGRlY29tcG9zaXRpb24gaXMgbm90IGVuZm9yY2VkIGV4cGxpY2l0bHkg4oCUIHRoZXJlIGlzIG5vIGxvc3MgdGVybSB0aGF0IHNlcGFyYXRlcyB0aGVzZSByb2xlcy4gSW5zdGVhZCwgaXQgZW1lcmdlcyBmcm9tIHRoZSBncmFkaWVudCBkeW5hbWljczogc2hhcmVkIGV4cGVydCB3ZWlnaHRzIHJlY2VpdmUgZ3JhZGllbnRzIGZyb20gYWxsIHRva2VucyBhbmQgY29udmVyZ2UgdG93YXJkIHRoZSBtZWFuIHRyYW5zZm9ybWF0aW9uIGFjcm9zcyB0aGUgdG9rZW4gZGlzdHJpYnV0aW9uLCB3aGlsZSByb3V0ZWQgZXhwZXJ0IHdlaWdodHMgcmVjZWl2ZSBncmFkaWVudHMgb25seSBmcm9tIHRoZWlyIHNwZWNpZmljIHRva2VuIGNsdXN0ZXIgYW5kIGNvbnZlcmdlIHRvd2FyZCB0aGUgb3B0aW1hbCB0cmFuc2Zvcm1hdGlvbiBmb3IgdGhhdCBjbHVzdGVyLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJEZXNpZ24iLCJTaGFyZWQgZXhwZXJ0cyIsIlJvdXRlZCBleHBlcnRzIiwiVG9wLUsiLCJBbHdheXMtYWN0aXZlIEZMT1BzIiwiTm90ZXMiXSwicm93cyI6W1siU3RhbmRhcmQgTW9FIChubyBzaGFyZWQpIiwiMCIsIjgiLCIyIiwiMiBleHBlcnRzIiwiQmFzZWxpbmU7IGFsbCBleHBlcnRzIGNvbXBldGUgZm9yIHJvdXRpbmciXSxbIkRlZXBTZWVrLU1vRSIsIjIiLCI2NCIsIjYgcm91dGVkIiwiMiArIDYgPSA4IGV4cGVydCB1bml0cyIsIkZpbmUtZ3JhaW5lZDsgc2hhcmVkIGhhbmRsZSB1bml2ZXJzYWwgcGF0dGVybnMiXSxbIkRTLU1vRSB2YXJpYW50IiwiMSIsIjE2IiwiMiByb3V0ZWQiLCIxICsgMiA9IDMgZXhwZXJ0IHVuaXRzIiwiU2luZ2xlIHNoYXJlZCBleHBlcnQ7IGxpZ2h0ZXIgb3ZlcmhlYWQiXSxbIlByb3Bvc2VkIHNoYXJlZD0yIiwiMiIsIjMyIiwiNCByb3V0ZWQiLCIyICsgNCA9IDYgZXhwZXJ0IHVuaXRzIiwiQmFsYW5jZSBiZXR3ZWVuIHNoYXJlZCBjb3ZlcmFnZSBhbmQgcm91dGluZyJdLFsiT3Blbk1vRSIsIjAiLCIzMiIsIjIiLCIyIGV4cGVydHMiLCJObyBzaGFyZWQ7IHVzZXMgYXV4aWxpYXJ5IGxvc3Mgb25seSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVlcFNlZWstVjIgSW1wbGVtZW50YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZXBTZWVrLVYyIChEZWVwU2Vlay1BSSwgMjAyNCkgaXMgdGhlIGxhcmdlc3QgcHVibGljIGRlcGxveW1lbnQgb2Ygc2hhcmVkLWV4cGVydCBNb0UuIEl0IHVzZXMgMjM2QiB0b3RhbCBwYXJhbWV0ZXJzIHdpdGggMjFCIGFjdGl2ZSBwZXIgdG9rZW4sIGFjaGlldmVkIHRocm91Z2ggMTYwIGZpbmUtZ3JhaW5lZCByb3V0ZWQgZXhwZXJ0cyBwbHVzIDIgc2hhcmVkIGV4cGVydHMgcGVyIE1vRSBsYXllci4gRWFjaCBNb0UgbGF5ZXIgYWN0aXZhdGVzIDYgb2YgMTYwIHJvdXRlZCBleHBlcnRzIHBsdXMgYm90aCBzaGFyZWQgZXhwZXJ0cyBwZXIgdG9rZW4uIFRoZSBtb2RlbCB3YXMgdHJhaW5lZCBvbiA4LjFUIHRva2VucyB3aXRoIGEgY29zaW5lIGxlYXJuaW5nIHJhdGUgc2NoZWR1bGUuIFRoZSBsb2FkLWJhbGFuY2luZyBsb3NzIGFwcGxpZXMgdG8gdGhlIDE2MCByb3V0ZWQgZXhwZXJ0cyBvbmx5OyB0aGUgMiBzaGFyZWQgZXhwZXJ0cyBhcmUgZXhjbHVkZWQgc2luY2UgdGhleSBwcm9jZXNzIGFsbCB0b2tlbnMgZXF1YWxseS4gRGVlcFNlZWstVjIgZGVtb25zdHJhdGVzIHRoYXQgdGhpcyBhcmNoaXRlY3R1cmUgbWF0Y2hlcyBvciBleGNlZWRzIEdQVC00LWNsYXNzIHBlcmZvcm1hbmNlIG9uIG1vc3QgYmVuY2htYXJrcyB3aGlsZSBhY3RpdmF0aW5nIG9ubHkgfjklIG9mIHRvdGFsIHBhcmFtZXRlcnMgcGVyIHRva2VuLCBlbmFibGluZyBlZmZpY2llbnQgaW5mZXJlbmNlIG9uIGZld2VyIEdQVXMgdGhhbiBhIGNvbXBhcmFibGUgZGVuc2UgbW9kZWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBzaGFyZWRfbW9lX3RyYWluaW5nX2xvc3MobG1fbG9zczogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcm91dGVyX2xvZ2l0czogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcm91dGVkX2luZGljZXM6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5fcm91dGVkOiBpbnQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbHBoYTogZmxvYXQgPSAxZS0yKSAtXHUwMDNlIHR1cGxlOlxuICAgIFwiXCJcIlRyYWluaW5nIGxvc3MgZm9yIHNoYXJlZC1leHBlcnQgTW9FOiBMTSBsb3NzICsgYXV4IGxvc3Mgb24gcm91dGVkIG9ubHkuXG4gICAgU2hhcmVkIGV4cGVydHMgYXJlIG5vdCBpbmNsdWRlZCBpbiB0aGUgbG9hZC1iYWxhbmNpbmcgbG9zcy5cIlwiXCJcbiAgICBwcm9icyAgPSBGLnNvZnRtYXgocm91dGVyX2xvZ2l0cywgZGltPS0xKSAgICAgICAgICAgICAgICMgKE4sIEVfcm91dGVkKVxuICAgIG9uZWhvdCA9IEYub25lX2hvdChyb3V0ZWRfaW5kaWNlc1s6LCAwXSwgbl9yb3V0ZWQpLmZsb2F0KClcbiAgICBmX2kgICAgPSBvbmVob3QubWVhbigwKSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgZnJhY3Rpb24gZGlzcGF0Y2hlZFxuICAgIFBfaSAgICA9IHByb2JzLm1lYW4oMCkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBtZWFuIHJvdXRpbmcgcHJvYlxuICAgIGF1eCAgICA9IG5fcm91dGVkICogKGZfaSAqIFBfaSkuc3VtKCkgICAgICAgICAgICAgICAgICAjIGltYmFsYW5jZSBwZW5hbHR5XG4gICAgdG90YWwgID0gbG1fbG9zcyArIGFscGhhICogYXV4XG4gICAgcmV0dXJuIHRvdGFsLCB7XCJsbVwiOiBsbV9sb3NzLml0ZW0oKSwgXCJhdXhcIjogKGFscGhhICogYXV4KS5pdGVtKCl9XG5cbiMgU2ltdWxhdGUgYSB0cmFpbmluZyBzdGVwXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubG0gICA9IHRvcmNoLnRlbnNvcigyLjMpICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBjcm9zcy1lbnRyb3B5XG5sb2dpdHMgPSB0b3JjaC5yYW5kbigxMjgsIDMyKSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIDEyOCB0b2tlbnMsIDMyIHJvdXRlZFxuaWR4ICAgID0gdG9yY2gudG9wayhsb2dpdHMsIDQsIGRpbT0tMSkuaW5kaWNlcyAgICAgICAgICAgICAjIHRvcC00IHJvdXRpbmdcbnRvdGFsLCBicmVha2Rvd24gPSBzaGFyZWRfbW9lX3RyYWluaW5nX2xvc3MobG0sIGxvZ2l0cywgaWR4LCAzMilcbnByaW50KGZcIlRvdGFsOiB7dG90YWwuaXRlbSgpOi40Zn0gIExNOiB7YnJlYWtkb3duW1x1MDAyN2xtXHUwMDI3XTouNGZ9ICBBdXg6IHticmVha2Rvd25bXHUwMDI3YXV4XHUwMDI3XTouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHJhZGVvZmZzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaGFyZWQgZXhwZXJ0cyBpbXByb3ZlIHBhcmFtZXRlciBlZmZpY2llbmN5IGFuZCByb3V0ZWQgZXhwZXJ0IHNwZWNpYWxpc2F0aW9uIGJ1dCBpbnRyb2R1Y2UgYWRkaXRpb25hbCBhbHdheXMtYWN0aXZlIGNvbXB1dGUuIFdpdGggTl9zPTIgc2hhcmVkIGV4cGVydHMgYW5kIEtfcj02IHJvdXRlZCBleHBlcnRzLCBlYWNoIHRva2VuIGFjdGl2YXRlcyA4IGV4cGVydCB1bml0cyDigJQgZXF1aXZhbGVudCB0byB0b3AtOCByb3V0aW5nIGluIGEgcHVyZSBzcGFyc2UgTW9FLiBJZiB0aGUgZ29hbCBpcyB0byBtaW5pbWlzZSBhY3RpdmUgRkxPUHMsIHNoYXJlZCBleHBlcnRzIGNvbnN1bWUgYSBmaXhlZCBvdmVyaGVhZCB0aGF0IHNjYWxlcyB3aXRoIE5fcyBidXQgbm90IHdpdGggYmF0Y2ggc2l6ZSBvciByb3V0aW5nLiBBdCBpbmZlcmVuY2UgdGltZSwgdGhpcyBvdmVyaGVhZCBpcyBjb25zdGFudCBhbmQgcHJlZGljdGFibGUsIG1ha2luZyBsYXRlbmN5IG1vcmUgc3RhYmxlIHRoYW4gcHVyZSBzcGFyc2UgTW9FIHdoZXJlIHJvdXRpbmcgcGF0dGVybnMgdmFyeSBieSBpbnB1dC4gSG93ZXZlciwgc2hhcmVkIGV4cGVydHMgYWxzbyBpbmNyZWFzZSBtZW1vcnkgYmFuZHdpZHRoIHJlcXVpcmVtZW50cyBhdCBpbmZlcmVuY2Ugc2luY2UgdGhlaXIgd2VpZ2h0cyBtdXN0IGJlIHJlYWQgZm9yIGV2ZXJ5IHRva2VuLiBUaGUgb3B0aW1hbCBOX3MgZGVwZW5kcyBvbiBob3cgbXVjaCB1bml2ZXJzYWwga25vd2xlZGdlIGV4aXN0cyBpbiB0aGUgdHJhaW5pbmcgZGlzdHJpYnV0aW9uIOKAlCB0eXBpY2FsbHkgMeKAkzQgc2hhcmVkIGV4cGVydHMgaXMgc3VmZmljaWVudCwgd2l0aCBkaW1pbmlzaGluZyByZXR1cm5zIGJleW9uZCB0aGF0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgYWJsYXRpb25fc2hhcmVkX2V4cGVydHMobl9zaGFyZWRfbGlzdDogbGlzdCwgZF9tb2RlbDogaW50ID0gNTEyLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRfZmY6IGludCA9IDEwMjQsIG5fcm91dGVkOiBpbnQgPSAzMixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b3BfazogaW50ID0gNCkgLVx1MDAzZSBOb25lOlxuICAgIFwiXCJcIkFibGF0aW9uOiBtZWFzdXJlIHRvdGFsIGFjdGl2ZSBwYXJhbXMgcGVyIHRva2VuIGFzIG5fc2hhcmVkIHZhcmllcy5cIlwiXCJcbiAgICBwcmludChmXCJ7XHUwMDI3bl9zaGFyZWRcdTAwMjc6XHUwMDNlMTB9IHtcdTAwMjduX3JvdXRlZFx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN3RvcF9rXHUwMDI3Olx1MDAzZTh9IFwiXG4gICAgICAgICAgZlwie1x1MDAyN2FjdGl2ZV9wYXJhbXNfTVx1MDAyNzpcdTAwM2UxN30ge1x1MDAyN3NoYXJlZF9wY3RcdTAwMjc6XHUwMDNlMTJ9XCIpXG4gICAgZmZuX3BhcmFtcyA9IDIgKiBkX21vZGVsICogZF9mZiAgICAgICAgICAgICAgICAgICAgICAgICAjIHBhcmFtcyBwZXIgZXhwZXJ0XG4gICAgZm9yIG5zIGluIG5fc2hhcmVkX2xpc3Q6XG4gICAgICAgIGFjdGl2ZSA9IChucyArIHRvcF9rKSAqIGZmbl9wYXJhbXNcbiAgICAgICAgc2hhcmVkX2ZyYWMgPSBucyAvIChucyArIHRvcF9rKSAqIDEwMFxuICAgICAgICBwcmludChmXCJ7bnM6XHUwMDNlMTB9IHtuX3JvdXRlZDpcdTAwM2UxMH0ge3RvcF9rOlx1MDAzZTh9IFwiXG4gICAgICAgICAgICAgIGZcInthY3RpdmUvMWU2Olx1MDAzZTE3LjJmfSB7c2hhcmVkX2ZyYWM6XHUwMDNlMTEuMWZ9JVwiKVxuXG5hYmxhdGlvbl9zaGFyZWRfZXhwZXJ0cyhbMCwgMSwgMiwgNCwgOF0pXG5cbiMgRG93bnN0cmVhbSBhY2N1cmFjeSBwcm94eTogc2hhcmVkPTIgdHlwaWNhbGx5ICswLjUtMS41IHBvaW50cyB2cyBzaGFyZWQ9MFxuc2ltdWxhdGVkX2FjY3VyYWN5ID0gezA6IDY4LjIsIDE6IDY5LjEsIDI6IDY5LjgsIDQ6IDcwLjAsIDg6IDcwLjF9XG5wcmludChcIlxcblNpbXVsYXRlZCBkb3duc3RyZWFtIGFjY3VyYWN5IHZzIG5fc2hhcmVkOlwiKVxuZm9yIG5zLCBhY2MgaW4gc2ltdWxhdGVkX2FjY3VyYWN5Lml0ZW1zKCk6XG4gICAgYmFyID0gXHUwMDI3fFx1MDAyNyAqIGludCgoYWNjIC0gNjgpICogMjApXG4gICAgcHJpbnQoZlwiICBuX3NoYXJlZD17bnN9OiB7YWNjOi4xZn0gIHtiYXJ9XCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJDb21tb24gS25vd2xlZGdlIFN0b3JlIiwiY29udGVudCI6IlNoYXJlZCBleHBlcnRzIGFjdCBsaWtlIGEgXHUwMDI3Y29tbW9uIGtub3dsZWRnZVx1MDAyNyBzdG9yZSDigJQgdGhleSByZWR1Y2UgdGhlIHByZXNzdXJlIG9uIHJvdXRlZCBleHBlcnRzIHRvIGNvdmVyIHVuaXZlcnNhbCBsYW5ndWFnZSBwYXR0ZXJucywgYWxsb3dpbmcgcm91dGVkIGV4cGVydHMgdG8gc3BlY2lhbGl6ZSBtb3JlIGRlZXBseSBpbiBkb21haW4tc3BlY2lmaWMga25vd2xlZGdlLiBJbiBEZWVwU2Vlay1WMiwganVzdCAyIHNoYXJlZCBleHBlcnRzIChvdXQgb2YgMTYyIHRvdGFsKSBpbXByb3ZlIGJlbmNobWFyayBhY2N1cmFjeSBieSAwLjfigJMxLjIgcG9pbnRzIHZzIGEgYmFzZWxpbmUgd2l0aCAwIHNoYXJlZCBleHBlcnRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNoYXJlZCBleHBlcnRzIGFyZSBhIGxvdy1jb3N0IGFyY2hpdGVjdHVyYWwgYWRkaXRpb24gdGhhdCBtZWFuaW5nZnVsbHkgaW1wcm92ZSBNb0UgcXVhbGl0eS4gQnkgZGVkaWNhdGluZyBOX3MgYWx3YXlzLWFjdGl2ZSBleHBlcnRzIHRvIHVuaXZlcnNhbCBrbm93bGVkZ2UsIHJvdXRlZCBleHBlcnRzIGFyZSBmcmVlZCB0byBzcGVjaWFsaXNlIG1vcmUgbmFycm93bHksIHJlZHVjaW5nIGtub3dsZWRnZSByZWR1bmRhbmN5IGFuZCBpbXByb3ZpbmcgcGFyYW1ldGVyIGVmZmljaWVuY3kuIFRoZSBkZXNpZ24gaXMgY2xlYW46IHRoZSByb3V0ZXIgb25seSBzY29yZXMgTl9yIHJvdXRlZCBleHBlcnRzOyB0aGUgYXV4aWxpYXJ5IGxvYWQtYmFsYW5jaW5nIGxvc3MgYXBwbGllcyBvbmx5IHRvIHJvdXRlZCBleHBlcnRzOyBzaGFyZWQgZXhwZXJ0cyBhZGQgYSBmaXhlZCBwZXItdG9rZW4gY29tcHV0ZSBvdmVyaGVhZCBvZiBOX3MgZXhwZXJ0IGZvcndhcmQgcGFzc2VzLiBEZWVwU2Vlay1WMiBkZW1vbnN0cmF0ZXMgdGhhdCAyIHNoYXJlZCBleHBlcnRzIG91dCBvZiAxNjIgdG90YWwgaXMgc3VmZmljaWVudCB0byBtYXRlcmlhbGx5IGltcHJvdmUgcXVhbGl0eSBhdCB0aGUgMjM2QiB0b3RhbCBwYXJhbWV0ZXIgc2NhbGUuIEZvciBtb3N0IGFwcGxpY2F0aW9ucywgMeKAkzQgc2hhcmVkIGV4cGVydHMgaXMgdGhlIHByYWN0aWNhbCBzd2VldCBzcG90LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTl9zIHNoYXJlZCBleHBlcnRzIGFsd2F5cyBhY3RpdmF0ZSBmb3IgZXZlcnkgdG9rZW47IHRoZWlyIG91dHB1dCBpcyBzdW1tZWQgKG5vdCBnYXRlZCkiLCJSb3V0ZXIgb25seSBjb3ZlcnMgTl9yIHJvdXRlZCBleHBlcnRzOyBhdXhpbGlhcnkgbG9zcyBhcHBsaWVzIHRvIHJvdXRlZCBleHBlcnRzIG9ubHkiLCJTaGFyZWQgZXhwZXJ0cyBsZWFybiB1bml2ZXJzYWwgcGF0dGVybnM7IHJvdXRlZCBleHBlcnRzIGxlYXJuIGRvbWFpbi1zcGVjaWZpYyBzcGVjaWFsaXNhdGlvbnMiLCJBY3RpdmUgRkxPUHMgPSAoTl9zICsgS19yKSBleHBlcnQgZm9yd2FyZCBwYXNzZXMgcGVyIHRva2VuIOKAlCBmaXhlZCBvdmVyaGVhZCBmb3Igc2hhcmVkIiwiRGVlcFNlZWstVjI6IDIgc2hhcmVkICsgNi1vZi0xNjAgcm91dGVkID0gOCBhY3RpdmUgZXhwZXJ0IHVuaXRzIHBlciB0b2tlbiwgMjM2QiB0b3RhbCBwYXJhbXMiLCJPcHRpbWFsIE5fcyBpcyAx4oCTNDsgYmV5b25kIDQgc2hhcmVkIGV4cGVydHMsIHJldHVybnMgZGltaW5pc2ggYW5kIHJvdXRpbmcgYmVuZWZpdCBzaHJpbmtzIl19XQ=="
---
# Shared Experts in MoE Architectures

Standard MoE routes every token to a small subset of experts, leaving common linguistic patterns to be learned redundantly across multiple experts. Shared experts address this by introducing a dedicated set of always-active experts that process every token unconditionally — they serve as a 'common knowledge store' for patterns that appear universally across all inputs. The remaining experts are sparse and conditionally routed as in standard MoE. This hybrid design, introduced in DeepSeek-MoE (Dai et al., 2024) and used in DeepSeek-V2, cleanly separates universal knowledge (shared experts) from specialised domain knowledge (routed experts), improving overall parameter efficiency and allowing routed experts to specialise more aggressively.

## Overview

In a shared-expert MoE layer, the output is the sum of two components: (1) the sum of outputs from N_s shared experts that always activate, and (2) the weighted sum of top-K_r selected outputs from N_r routed experts. The shared experts contribute a fixed, general transformation to every token; the routed experts contribute a token-specific, specialised transformation. The load-balancing auxiliary loss is applied only to the routed experts — since shared experts process all tokens equally, they need no balancing. The overall active-parameter count per token is N_s + K_r experts, compared to K_r in a pure sparse MoE. In DeepSeek-V2, N_s=2 shared and K_r=6 of N_r=160 routed experts activate per token, giving 8 active expert units per token with 236B total parameters.

## Motivation for Shared Experts

The motivation for shared experts comes from an empirical observation in coarse MoE: expert weight matrices show high pairwise cosine similarity for certain components. This suggests that multiple experts are learning the same transformation — wasting parameters on redundant common knowledge instead of developing unique specialisations. The redundancy arises because, in standard MoE, even though each expert processes only 1/N tokens on average, those tokens span many different linguistic patterns. An expert that processes diverse tokens must learn diverse functions, leading to a 'jack of all trades' representation that overlaps with other experts. By offloading the most universal patterns to dedicated shared experts, routed experts are free to specialise in narrower and more distinct domains.

- Expert weight cosine similarity in coarse MoE is higher than expected — experts learn redundant functions
- Common linguistic patterns (function words, punctuation, basic grammar) appear in all token contexts
- Shared experts learn these universal patterns once, not redundantly across multiple routed experts
- Routed expert specialisation improves because they no longer need to cover common patterns
- Load-balancing pressure on routed experts is reduced — they handle a more separable task
- Ablations show that removing shared experts reduces downstream accuracy by 0.5–1.5 points

## Architecture Design

The shared-expert MoE layer has three components: a router, N_s shared experts, and N_r routed experts. The router is identical to standard MoE — a linear projection from d_model to N_r (not N_r + N_s, since shared experts need no routing). Shared experts are standard FFNs (Linear → GELU → Linear) with the same architecture as routed experts. On the forward pass, input x is processed by all N_s shared experts in parallel (sum their outputs), and independently processed by the top-K_r selected routed experts (weighted sum). The two components are added element-wise. Since shared expert outputs are not gated, no routing weight is applied — each shared expert contributes its full output. In DeepSeek-MoE, shared experts have the same hidden dimension as routed experts (d_ff/m for fine-grained variants).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SharedExpertMoELayer(nn.Module):
    """MoE layer with always-active shared experts + top-K routed experts."""
    def __init__(self, d_model: int, d_ff: int,
                 n_shared: int, n_routed: int, top_k: int):
        super().__init__()
        self.n_routed, self.top_k = n_routed, top_k
        self.router = nn.Linear(d_model, n_routed, bias=False)
        # Shared experts: always active, no routing weight
        self.shared_experts = nn.ModuleList([
            nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(),
                          nn.Linear(d_ff, d_model)) for _ in range(n_shared)])
        # Routed experts: sparse, conditionally activated
        self.routed_experts = nn.ModuleList([
            nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(),
                          nn.Linear(d_ff, d_model)) for _ in range(n_routed)])

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 1. Shared expert pass (always active, no gating)
        shared_out = sum(e(x) for e in self.shared_experts)  # (B, T, D)
        # 2. Routed expert pass (top-K of N_r)
        B, T, D = x.shape
        xf = x.view(B * T, D)
        probs, idx = torch.topk(F.softmax(self.router(xf), -1), self.top_k, -1)
        probs = probs / probs.sum(-1, keepdim=True)
        routed = torch.zeros_like(xf)
        for k in range(self.top_k):
            for e, expert in enumerate(self.routed_experts):
                m = idx[:, k] == e
                if m.any():
                    routed[m] += probs[m, k:k+1] * expert(xf[m])
        return shared_out + routed.view(B, T, D)

layer = SharedExpertMoELayer(512, 1024, n_shared=2, n_routed=32, top_k=4)
print(f"Output: {layer(torch.randn(2, 8, 512)).shape}")
```

## Routing with Shared + Routed

The router in a shared-expert MoE only needs to score the N_r routed experts — the N_s shared experts are always active and require no score. This keeps the router smaller than it would be if shared experts were included in the routing decision. The routing mechanism is identical to standard top-K routing: softmax over N_r logits, take top-K_r, renormalise, weighted sum. Because the shared experts already provide a universal base transformation, the routed experts need only produce a residual specialised correction. This means the routing weights do not need to be as sharp — a moderate preference for certain routed experts is sufficient. In practice, this leads to more stable routing and less collapse compared to pure sparse MoE with the same number of routed experts.

```python
import torch
import torch.nn.functional as F

def knowledge_decomposition_analysis(shared_weights: torch.Tensor,
                                     routed_weights: torch.Tensor) -> dict:
    """Measure how different shared vs routed expert weights are.
    shared_weights: (n_shared, d_in*d_out)  routed_weights: (n_routed, d_in*d_out)
    Hypothesis: shared experts should differ from routed experts
    (they capture different patterns), and routed experts differ from each other."""
    shared_norm = F.normalize(shared_weights, dim=-1)       # (n_s, D)
    routed_norm = F.normalize(routed_weights, dim=-1)       # (n_r, D)
    # Shared vs routed similarity (should be low — different functions)
    sr_sim = (shared_norm.unsqueeze(1) * routed_norm.unsqueeze(0)).sum(-1)  # (n_s, n_r)
    # Routed vs routed similarity (should be low — diverse specialisation)
    rr_sim = routed_norm @ routed_norm.T                    # (n_r, n_r)
    mask   = ~torch.eye(routed_norm.shape[0], dtype=torch.bool)
    return {
        "shared_vs_routed_mean_sim": sr_sim.mean().item(),
        "routed_vs_routed_mean_sim": rr_sim[mask].mean().item(),
        "routed_diversity": 1 - rr_sim[mask].mean().item(),
    }

torch.manual_seed(0)
shared = torch.randn(2, 512 * 256)
routed = torch.randn(32, 512 * 256)
stats  = knowledge_decomposition_analysis(shared, routed)
for k, v in stats.items():
    print(f"{k}: {v:.4f}")
```

## Knowledge Decomposition

The theoretical motivation for shared experts is that the information processed by an MoE layer can be decomposed into two orthogonal components: general information that is context-independent and universal (such as basic token type transformations, positional context, and grammatical structure), and specialised information that depends on the specific domain, topic, or linguistic register of the input. Shared experts are responsible for the general component; routed experts handle the specialised component. This decomposition is not enforced explicitly — there is no loss term that separates these roles. Instead, it emerges from the gradient dynamics: shared expert weights receive gradients from all tokens and converge toward the mean transformation across the token distribution, while routed expert weights receive gradients only from their specific token cluster and converge toward the optimal transformation for that cluster.

| Design | Shared experts | Routed experts | Top-K | Always-active FLOPs | Notes |
| --- | --- | --- | --- | --- | --- |
| Standard MoE (no shared) | 0 | 8 | 2 | 2 experts | Baseline; all experts compete for routing |
| DeepSeek-MoE | 2 | 64 | 6 routed | 2 + 6 = 8 expert units | Fine-grained; shared handle universal patterns |
| DS-MoE variant | 1 | 16 | 2 routed | 1 + 2 = 3 expert units | Single shared expert; lighter overhead |
| Proposed shared=2 | 2 | 32 | 4 routed | 2 + 4 = 6 expert units | Balance between shared coverage and routing |
| OpenMoE | 0 | 32 | 2 | 2 experts | No shared; uses auxiliary loss only |

## DeepSeek-V2 Implementation

DeepSeek-V2 (DeepSeek-AI, 2024) is the largest public deployment of shared-expert MoE. It uses 236B total parameters with 21B active per token, achieved through 160 fine-grained routed experts plus 2 shared experts per MoE layer. Each MoE layer activates 6 of 160 routed experts plus both shared experts per token. The model was trained on 8.1T tokens with a cosine learning rate schedule. The load-balancing loss applies to the 160 routed experts only; the 2 shared experts are excluded since they process all tokens equally. DeepSeek-V2 demonstrates that this architecture matches or exceeds GPT-4-class performance on most benchmarks while activating only ~9% of total parameters per token, enabling efficient inference on fewer GPUs than a comparable dense model.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def shared_moe_training_loss(lm_loss: torch.Tensor,
                              router_logits: torch.Tensor,
                              routed_indices: torch.Tensor,
                              n_routed: int,
                              alpha: float = 1e-2) -> tuple:
    """Training loss for shared-expert MoE: LM loss + aux loss on routed only.
    Shared experts are not included in the load-balancing loss."""
    probs  = F.softmax(router_logits, dim=-1)               # (N, E_routed)
    onehot = F.one_hot(routed_indices[:, 0], n_routed).float()
    f_i    = onehot.mean(0)                                 # fraction dispatched
    P_i    = probs.mean(0)                                  # mean routing prob
    aux    = n_routed * (f_i * P_i).sum()                  # imbalance penalty
    total  = lm_loss + alpha * aux
    return total, {"lm": lm_loss.item(), "aux": (alpha * aux).item()}

# Simulate a training step
torch.manual_seed(0)
lm   = torch.tensor(2.3)                                    # cross-entropy
logits = torch.randn(128, 32)                               # 128 tokens, 32 routed
idx    = torch.topk(logits, 4, dim=-1).indices             # top-4 routing
total, breakdown = shared_moe_training_loss(lm, logits, idx, 32)
print(f"Total: {total.item():.4f}  LM: {breakdown['lm']:.4f}  Aux: {breakdown['aux']:.4f}")
```

## Tradeoffs

Shared experts improve parameter efficiency and routed expert specialisation but introduce additional always-active compute. With N_s=2 shared experts and K_r=6 routed experts, each token activates 8 expert units — equivalent to top-8 routing in a pure sparse MoE. If the goal is to minimise active FLOPs, shared experts consume a fixed overhead that scales with N_s but not with batch size or routing. At inference time, this overhead is constant and predictable, making latency more stable than pure sparse MoE where routing patterns vary by input. However, shared experts also increase memory bandwidth requirements at inference since their weights must be read for every token. The optimal N_s depends on how much universal knowledge exists in the training distribution — typically 1–4 shared experts is sufficient, with diminishing returns beyond that.

```python
import torch
import torch.nn as nn

def ablation_shared_experts(n_shared_list: list, d_model: int = 512,
                            d_ff: int = 1024, n_routed: int = 32,
                            top_k: int = 4) -> None:
    """Ablation: measure total active params per token as n_shared varies."""
    print(f"{'n_shared':>10} {'n_routed':>10} {'top_k':>8} "
          f"{'active_params_M':>17} {'shared_pct':>12}")
    ffn_params = 2 * d_model * d_ff                         # params per expert
    for ns in n_shared_list:
        active = (ns + top_k) * ffn_params
        shared_frac = ns / (ns + top_k) * 100
        print(f"{ns:>10} {n_routed:>10} {top_k:>8} "
              f"{active/1e6:>17.2f} {shared_frac:>11.1f}%")

ablation_shared_experts([0, 1, 2, 4, 8])

# Downstream accuracy proxy: shared=2 typically +0.5-1.5 points vs shared=0
simulated_accuracy = {0: 68.2, 1: 69.1, 2: 69.8, 4: 70.0, 8: 70.1}
print("\nSimulated downstream accuracy vs n_shared:")
for ns, acc in simulated_accuracy.items():
    bar = '|' * int((acc - 68) * 20)
    print(f"  n_shared={ns}: {acc:.1f}  {bar}")
```

> **Common Knowledge Store**: Shared experts act like a 'common knowledge' store — they reduce the pressure on routed experts to cover universal language patterns, allowing routed experts to specialize more deeply in domain-specific knowledge. In DeepSeek-V2, just 2 shared experts (out of 162 total) improve benchmark accuracy by 0.7–1.2 points vs a baseline with 0 shared experts.

## Key Takeaways

Shared experts are a low-cost architectural addition that meaningfully improve MoE quality. By dedicating N_s always-active experts to universal knowledge, routed experts are freed to specialise more narrowly, reducing knowledge redundancy and improving parameter efficiency. The design is clean: the router only scores N_r routed experts; the auxiliary load-balancing loss applies only to routed experts; shared experts add a fixed per-token compute overhead of N_s expert forward passes. DeepSeek-V2 demonstrates that 2 shared experts out of 162 total is sufficient to materially improve quality at the 236B total parameter scale. For most applications, 1–4 shared experts is the practical sweet spot.

- N_s shared experts always activate for every token; their output is summed (not gated)
- Router only covers N_r routed experts; auxiliary loss applies to routed experts only
- Shared experts learn universal patterns; routed experts learn domain-specific specialisations
- Active FLOPs = (N_s + K_r) expert forward passes per token — fixed overhead for shared
- DeepSeek-V2: 2 shared + 6-of-160 routed = 8 active expert units per token, 236B total params
- Optimal N_s is 1–4; beyond 4 shared experts, returns diminish and routing benefit shrinks

