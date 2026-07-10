---
title: "Wasserstein GAN — Earth Mover Distance and Gradient Penalty"
slug: "wasserstein-gan"
description: "WGAN replaces the JS divergence objective with the Wasserstein-1 (Earth Mover) distance, enforced via weight clipping or gradient penalty, providing a meaningful loss that correlates with sample quality and solving vanishing-gradient and mode collapse problems of standard GANs."
tags: ["deep-learning", "generative-models", "gans"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFdhc3NlcnN0ZWluIEdBTiAoQXJqb3Zza3kgZXQgYWwuLCAyMDE3KSBpZGVudGlmaWVzIGEgZnVuZGFtZW50YWwgZmxhdyBpbiB0aGUgc3RhbmRhcmQgR0FOIHRyYWluaW5nIG9iamVjdGl2ZSBhbmQgcmVwbGFjZXMgaXQgd2l0aCBhIHRoZW9yZXRpY2FsbHkgbW90aXZhdGVkIGFsdGVybmF0aXZlLiBTdGFuZGFyZCBHQU5zIG1pbmltaXNlIHRoZSBKZW5zZW4tU2hhbm5vbiBkaXZlcmdlbmNlIGJldHdlZW4gcF9kYXRhIGFuZCBwX2csIGJ1dCBKUyBkaXZlcmdlbmNlIGlzIHVuZGVmaW5lZCAob3Igc2F0dXJhdGVkKSB3aGVuIHRoZSB0d28gZGlzdHJpYnV0aW9ucyBoYXZlIGRpc2pvaW50IHN1cHBvcnQg4oCUIHdoaWNoIGlzIG5lYXJseSBhbHdheXMgdGhlIGNhc2UgaW4gaGlnaC1kaW1lbnNpb25hbCBzcGFjZXMgZWFybHkgaW4gdHJhaW5pbmcuIFdHQU4gcmVwbGFjZXMgSlMgd2l0aCB0aGUgV2Fzc2Vyc3RlaW4tMSBkaXN0YW5jZSwgd2hpY2ggaXMgYWx3YXlzIGRlZmluZWQgYW5kIHByb3ZpZGVzIG1lYW5pbmdmdWwgZ3JhZGllbnRzIGV2ZW4gd2hlbiB0aGUgZGlzdHJpYnV0aW9ucyBkbyBub3Qgb3ZlcmxhcC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgSlMgRGl2ZXJnZW5jZSBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBoaWdoLWRpbWVuc2lvbmFsIHNwYWNlcywgdGhlIHJlYWwgZGF0YSBkaXN0cmlidXRpb24gcF9kYXRhIGFuZCB0aGUgZ2VuZXJhdGVkIGRpc3RyaWJ1dGlvbiBwX2cgY29uY2VudHJhdGUgb24gbG93LWRpbWVuc2lvbmFsIG1hbmlmb2xkcyB0aGF0IGhhdmUgbWVhc3VyZSB6ZXJvIHJlbGF0aXZlIHRvIHRoZSBhbWJpZW50IHNwYWNlLiBXaGVuIHRoZXNlIG1hbmlmb2xkcyBhcmUgZGlzam9pbnQgKHdoaWNoIGhhcHBlbnMgYWxtb3N0IGNlcnRhaW5seSBlYXJseSBpbiB0cmFpbmluZyksIHRoZSBKUyBkaXZlcmdlbmNlIGlzIGV4YWN0bHkgbG9nKDIpIOKAlCBhIGNvbnN0YW50IHdpdGggZ3JhZGllbnQgemVyby4gVGhpcyBtZWFucyB0aGUgZGlzY3JpbWluYXRvciBzYXR1cmF0ZXMsIHByb3ZpZGluZyBubyBncmFkaWVudCB0byB0aGUgZ2VuZXJhdG9yLiBUaGUgR0FOIHRoZW4gb3NjaWxsYXRlcyBvciBzdGFsbHMgcmF0aGVyIHRoYW4gaW1wcm92aW5nLiJ9LHsidHlwZSI6Im1hdGgiLCJjb250ZW50IjoiXFx0ZXh0e0pTfShwIFxcfCBxKSA9IFxcZnJhY3sxfXsyfSBLTFxcIVxcbGVmdChwIFxcLFxcQmlnXFx8XFwsIFxcZnJhY3twK3F9ezJ9XFxyaWdodCkgKyBcXGZyYWN7MX17Mn0gS0xcXCFcXGxlZnQocSBcXCxcXEJpZ1xcfFxcLCBcXGZyYWN7cCtxfXsyfVxccmlnaHQpIiwiZGlzcGxheSI6dHJ1ZX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2Fzc2Vyc3RlaW4tMSBEaXN0YW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFdhc3NlcnN0ZWluLTEgKEVhcnRoIE1vdmVyKSBkaXN0YW5jZSBXKHAsIHEpIG1lYXN1cmVzIHRoZSBtaW5pbXVtIGNvc3Qgb2YgdHJhbnNwb3J0aW5nIG1hc3MgZnJvbSBkaXN0cmlidXRpb24gcCB0byBkaXN0cmlidXRpb24gcSwgd2hlcmUgY29zdCBpcyB0aGUgZGlzdGFuY2UgbW92ZWQgdGltZXMgdGhlIG1hc3MgbW92ZWQuIFVubGlrZSBKUyBkaXZlcmdlbmNlLCBXKHAscSkgaXMgZGVmaW5lZCBhbmQgY29udGludW91cyBldmVuIHdoZW4gcCBhbmQgcSBoYXZlIGRpc2pvaW50IHN1cHBvcnRzIOKAlCBpdCByZXR1cm5zIHRoZSBwaHlzaWNhbCBkaXN0YW5jZSBiZXR3ZWVuIHRoZSB0d28gZGlzdHJpYnV0aW9uIG1hc3Nlcy4gQXMgcF9nIG1vdmVzIHRvd2FyZCBwX2RhdGEgZHVyaW5nIHRyYWluaW5nLCBXKHBfZywgcF9kYXRhKSBkZWNyZWFzZXMgbW9ub3RvbmljYWxseSBhbmQgcHJvdmlkZXMgdXNlZnVsIGdyYWRpZW50IGluZm9ybWF0aW9uIHRocm91Z2hvdXQuIn0seyJ0eXBlIjoibWF0aCIsImNvbnRlbnQiOiJXKHAsIHEpID0gXFxpbmZfe1xcZ2FtbWEgXFxpbiBcXFBpKHAscSl9IFxcbWF0aGJie0V9X3soeCx5KSBcXHNpbSBcXGdhbW1hfVtcXHx4IC0geVxcfF0iLCJkaXNwbGF5Ijp0cnVlfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLYW50b3JvdmljaC1SdWJpbnN0ZWluIER1YWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbXB1dGluZyBXKHAscSkgZGlyZWN0bHkgaXMgaW50cmFjdGFibGUgZm9yIGhpZ2gtZGltZW5zaW9uYWwgZGlzdHJpYnV0aW9ucy4gVGhlIEthbnRvcm92aWNoLVJ1Ymluc3RlaW4gZHVhbGl0eSBwcm92aWRlcyBhIHRyYWN0YWJsZSBkdWFsIGZvcm11bGF0aW9uOiBXKHAscSkgPSBzdXBfe3x8Znx8X0wg4omkIDF9IChFX3BbZih4KV0gLSBFX3FbZih4KV0pLCB3aGVyZSB0aGUgc3VwcmVtdW0gaXMgb3ZlciBhbGwgMS1MaXBzY2hpdHogZnVuY3Rpb25zIGYuIEluIFdHQU4sIHRoZSBjcml0aWMgKHJlcGxhY2luZyB0aGUgZGlzY3JpbWluYXRvcikgcGFyYW1ldGVyaXNlcyBmLiBUcmFpbmluZyBtYXhpbWlzZXMgRVtmKHJlYWwpXSAtIEVbZihmYWtlKV0gb3ZlciB0aGUgY3JpdGljIHdoaWxlIGVuZm9yY2luZyB0aGUgMS1MaXBzY2hpdHogY29uc3RyYWludC4gVGhlIGNyaXRpYyBpcyBub3QgYSBjbGFzc2lmaWVyIOKAlCBpdCBvdXRwdXRzIHVuYm91bmRlZCByZWFsLXZhbHVlZCBzY29yZXMsIG5vdCBwcm9iYWJpbGl0aWVzLiJ9LHsidHlwZSI6Im1hdGgiLCJjb250ZW50IjoiVyhwLCBxKSA9IFxcc3VwX3tcXHxmXFx8X0wgXFxsZXEgMX0gXFxsZWZ0KCBcXG1hdGhiYntFfV97eCBcXHNpbSBwfVtmKHgpXSAtIFxcbWF0aGJie0V9X3t4IFxcc2ltIHF9W2YoeCldIFxccmlnaHQpIiwiZGlzcGxheSI6dHJ1ZX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV0dBTiBUcmFpbmluZyB3aXRoIFdlaWdodCBDbGlwcGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV0dBTiBlbmZvcmNlcyB0aGUgMS1MaXBzY2hpdHogY29uc3RyYWludCBvbiB0aGUgY3JpdGljIGJ5IGNsaXBwaW5nIGFsbCBjcml0aWMgd2VpZ2h0cyB0byB0aGUgaW50ZXJ2YWwgWy1jLCBjXSBhZnRlciBlYWNoIGdyYWRpZW50IHN0ZXAgKHR5cGljYWxseSBjPTAuMDEpLiBUaGUgY3JpdGljIGlzIHRyYWluZWQgdG8gbmVhci1jb252ZXJnZW5jZSAobl9jcml0aWM9NSBzdGVwcykgYmVmb3JlIGVhY2ggZ2VuZXJhdG9yIHVwZGF0ZS4gVW5saWtlIHN0YW5kYXJkIEdBTiwgV0dBTiB1c2VzIFJNU3Byb3AgcmF0aGVyIHRoYW4gQWRhbSDigJQgdGhlIGF1dGhvcnMgZm91bmQgQWRhbVx1MDAyN3MgbW9tZW50dW0gZGVzdGFiaWxpc2VzIFdHQU4gdHJhaW5pbmcuIFRoZSBnZW5lcmF0b3IgbG9zcyBpcyBzaW1wbHkgLUVbZihHKHopKV0sIGFuZCB0aGUgY3JpdGljIGxvc3MgaXMgLShFW2YocmVhbCldIC0gRVtmKGZha2UpXSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cblxuZGVmIHRyYWluX3dnYW4oZ2VuZXJhdG9yLCBjcml0aWMsIGRhdGFsb2FkZXIsXG4gICAgICAgICAgICAgICBudW1fZXBvY2hzPTEwMCwgbl9jcml0aWM9NSwgY2xpcF9jPTAuMDEsIGxhdGVudF9kaW09MTAwKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdXR0FOIHRyYWluaW5nIHdpdGggd2VpZ2h0IGNsaXBwaW5nLiBDcml0aWMgb3V0cHV0cyB1bmJvdW5kZWQgc2NhbGFycy5cbiAgICBVc2UgUk1TcHJvcCBub3QgQWRhbTsgY2xpcCBjcml0aWMgd2VpZ2h0cyB0byBbLWMsIGNdIGFmdGVyIGVhY2ggc3RlcC5cbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBvcHRfRyA9IG9wdGltLlJNU3Byb3AoZ2VuZXJhdG9yLnBhcmFtZXRlcnMoKSwgbHI9NWUtNSlcbiAgICBvcHRfQyA9IG9wdGltLlJNU3Byb3AoY3JpdGljLnBhcmFtZXRlcnMoKSwgbHI9NWUtNSlcbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2UobnVtX2Vwb2Nocyk6XG4gICAgICAgIGZvciByZWFsX2ltZ3MsIF8gaW4gZGF0YWxvYWRlcjpcbiAgICAgICAgICAgIGJzID0gcmVhbF9pbWdzLnNpemUoMClcbiAgICAgICAgICAgICMgLS0tIENyaXRpYzogbl9jcml0aWMgc3RlcHMgcGVyIGdlbmVyYXRvciBzdGVwIC0tLVxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9jcml0aWMpOlxuICAgICAgICAgICAgICAgIG9wdF9DLnplcm9fZ3JhZCgpXG4gICAgICAgICAgICAgICAgeiA9IHRvcmNoLnJhbmRuKGJzLCBsYXRlbnRfZGltKVxuICAgICAgICAgICAgICAgIGZha2VfaW1ncyA9IGdlbmVyYXRvcih6KS5kZXRhY2goKVxuICAgICAgICAgICAgICAgICMgTWF4aW1pemUgRVtmKHJlYWwpXSAtIEVbZihmYWtlKV0sIGkuZS4gbWluaW1pc2UgbmVnYXRpb25cbiAgICAgICAgICAgICAgICBjX3JlYWwgPSBjcml0aWMocmVhbF9pbWdzKS5tZWFuKClcbiAgICAgICAgICAgICAgICBjX2Zha2UgPSBjcml0aWMoZmFrZV9pbWdzKS5tZWFuKClcbiAgICAgICAgICAgICAgICBjX2xvc3MgPSAtKGNfcmVhbCAtIGNfZmFrZSlcbiAgICAgICAgICAgICAgICBjX2xvc3MuYmFja3dhcmQoKVxuICAgICAgICAgICAgICAgIG9wdF9DLnN0ZXAoKVxuICAgICAgICAgICAgICAgICMgRW5mb3JjZSAxLUxpcHNjaGl0eiBjb25zdHJhaW50IHZpYSB3ZWlnaHQgY2xpcHBpbmdcbiAgICAgICAgICAgICAgICBmb3IgcCBpbiBjcml0aWMucGFyYW1ldGVycygpOlxuICAgICAgICAgICAgICAgICAgICBwLmRhdGEuY2xhbXBfKC1jbGlwX2MsIGNsaXBfYylcbiAgICAgICAgICAgICMgLS0tIEdlbmVyYXRvcjogbWF4aW1pemUgRVtmKEcoeikpXSAtLS1cbiAgICAgICAgICAgIG9wdF9HLnplcm9fZ3JhZCgpXG4gICAgICAgICAgICB6ID0gdG9yY2gucmFuZG4oYnMsIGxhdGVudF9kaW0pXG4gICAgICAgICAgICBnX2xvc3MgPSAtY3JpdGljKGdlbmVyYXRvcih6KSkubWVhbigpXG4gICAgICAgICAgICBnX2xvc3MuYmFja3dhcmQoKVxuICAgICAgICAgICAgb3B0X0cuc3RlcCgpXG4gICAgICAgIHdfZGlzdCA9IChjX3JlYWwgLSBjX2Zha2UpLml0ZW0oKVxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NofTogV19kaXN0PXt3X2Rpc3Q6LjRmfSAgR19sb3NzPXtnX2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgd2Fzc2Vyc3RlaW5fZGlzdGFuY2UsIGdhdXNzaWFuX2tkZVxuXG5kZWYgY29tcGFyZV93MV92c19qcyhtZWFuMT0wLjAsIHN0ZDE9MS4wLCBtZWFuMj0yLjAsIHN0ZDI9MS4wLCBuPTIwMDAwKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdDb21wYXJlIFdhc3NlcnN0ZWluLTEgYW5kIEpTIGRpdmVyZ2VuY2Ugb24gMUQgR2F1c3NpYW5zLlxuICAgIEpTIHNhdHVyYXRlcyBhdCBsb2coMikgZm9yIGRpc2pvaW50IGRpc3RyaWJ1dGlvbnM7IFcxIHN0YXlzIG1lYW5pbmdmdWwuXG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgcCA9IG5wLnJhbmRvbS5ub3JtYWwobWVhbjEsIHN0ZDEsIG4pXG4gICAgcSA9IG5wLnJhbmRvbS5ub3JtYWwobWVhbjIsIHN0ZDIsIG4pXG4gICAgdzEgPSB3YXNzZXJzdGVpbl9kaXN0YW5jZShwLCBxKVxuICAgIGtkZV9wLCBrZGVfcSA9IGdhdXNzaWFuX2tkZShwKSwgZ2F1c3NpYW5fa2RlKHEpXG4gICAgeCA9IG5wLmxpbnNwYWNlKG1pbihwLm1pbigpLCBxLm1pbigpKSwgbWF4KHAubWF4KCksIHEubWF4KCkpLCA1MDApXG4gICAgcHgsIHF4ID0ga2RlX3AoeCkgKyAxZS0xMCwga2RlX3EoeCkgKyAxZS0xMFxuICAgIG14ID0gMC41ICogKHB4ICsgcXgpXG4gICAganMgPSAwLjUgKiAobnAudHJhcHoocHggKiBucC5sb2cocHggLyBteCksIHgpICtcbiAgICAgICAgICAgICAgICBucC50cmFweihxeCAqIG5wLmxvZyhxeCAvIG14KSwgeCkpXG4gICAgcmV0dXJuIHcxLCBqc1xuXG5wcmludChmXHUwMDI3e1wiU2VwYXJhdGlvblwiOlx1MDAzYzEyfSB7XCJXMS1kaXN0YW5jZVwiOlx1MDAzYzE0fSB7XCJKUy1kaXZlcmdlbmNlXCI6XHUwMDNjMTZ9IHtcIkpTIHNhdHVyYXRlZD9cIn1cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNTgpXG5mb3Igc2VwIGluIFswLjUsIDIuMCwgNS4wLCAxMC4wLCAyMC4wXTpcbiAgICB3MSwganMgPSBjb21wYXJlX3cxX3ZzX2pzKG1lYW4xPTAuMCwgbWVhbjI9c2VwKVxuICAgIHNhdHVyYXRlZCA9IFx1MDAyN1lFUyAobm8gZ3JhZGllbnQhKVx1MDAyNyBpZiBqcyBcdTAwM2UgMC42NSBlbHNlIFx1MDAyN25vXHUwMDI3XG4gICAgcHJpbnQoZlx1MDAyN3tzZXA6XHUwMDNjMTIuMWZ9IHt3MTpcdTAwM2MxNC40Zn0ge2pzOlx1MDAzYzE2LjRmfSB7c2F0dXJhdGVkfVx1MDAyNylcbnByaW50KGZcdTAwMjdKUyBzYXR1cmF0ZXMgYXQgbG9nKDIpID0ge25wLmxvZygyKTouNGZ9IGZvciBkaXNqb2ludCBkaXN0cmlidXRpb25zLlx1MDAyNylcbnByaW50KFx1MDAyN1cxIGNvbnRpbnVlcyBzY2FsaW5nIGxpbmVhcmx5IHdpdGggc2VwYXJhdGlvbiDigJQgYWx3YXlzIGEgdXNlZnVsIGdyYWRpZW50IHNpZ25hbC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2VpZ2h0IENsaXBwaW5nIFByb2JsZW1zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXZWlnaHQgY2xpcHBpbmcgZW5mb3JjZXMgdGhlIExpcHNjaGl0eiBjb25zdHJhaW50LCBidXQgaXQgaXMgY3J1ZGUuIEFsbCB3ZWlnaHRzIGFyZSBmb3JjZWQgaW50byBbLWMsIGNdLCB3aGljaCBiaWFzZXMgdGhlIGNyaXRpYyB0b3dhcmQgbGluZWFyIGZ1bmN0aW9ucyDigJQgdGhlIHNpbXBsZXN0IGZ1bmN0aW9ucyB0aGF0IHJlc3BlY3QgdGhlIGJvdW5kIHdoaWxlIHVzaW5nIGFsbCBhdmFpbGFibGUgd2VpZ2h0IGNhcGFjaXR5LiBUaGlzIGRyYW1hdGljYWxseSByZWR1Y2VzIHRoZSBjcml0aWNcdTAwMjdzIGV4cHJlc3NpdmUgcG93ZXIuIFdpdGggYyB0b28gc21hbGwsIGdyYWRpZW50cyB2YW5pc2ggaW4gZGVlcCBjcml0aWNzOyB3aXRoIGMgdG9vIGxhcmdlLCB0aGUgTGlwc2NoaXR6IGNvbnN0cmFpbnQgaXMgbm90IG1lYW5pbmdmdWxseSBlbmZvcmNlZC4gVGhlIFdHQU4gYXV0aG9ycyB0aGVtc2VsdmVzIGFja25vd2xlZGdlZCBjbGlwcGluZyBhcyBhIHN0b3BnYXAgbWVhc3VyZS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IldlaWdodCBDbGlwcGluZyBMaW1pdGF0aW9ucyIsImNvbnRlbnQiOiJXZWlnaHQgY2xpcHBpbmcgYmlhc2VzIHRoZSBjcml0aWMgdG93YXJkIGxpbmVhciBmdW5jdGlvbnMgYmVjYXVzZSBjbGlwcGluZyBhbGwgd2VpZ2h0cyB1bmlmb3JtbHkgc3VwcHJlc3NlcyBkZWVwIGNvbXBvc2l0aW9uYWwgZmVhdHVyZXMuIFRoaXMgY2FwYWNpdHkgdW5kZXJ1c2UgbWVhbnMgdGhlIGNyaXRpYyBjYW5ub3QgZml0IHRoZSB0cnVlIFdhc3NlcnN0ZWluIGRpc3RhbmNlIHdlbGwuIFRoZSBzb2x1dGlvbiBpcyBXR0FOLUdQIChHdWxyYWphbmkgMjAxNyksIHdoaWNoIHJlcGxhY2VzIGNsaXBwaW5nIHdpdGggYSBncmFkaWVudCBwZW5hbHR5IHRlcm06IGxhbWJkYSAqIEVbKHx8Z3JhZF94IEQoeF9oYXQpfHxfMiAtIDEpXjJdIGV2YWx1YXRlZCBhdCBpbnRlcnBvbGF0ZWQgcG9pbnRzIHhfaGF0IGJldHdlZW4gcmVhbCBhbmQgZmFrZSBzYW1wbGVzLiBXR0FOLUdQIGlzIHRoZSBwcmVmZXJyZWQgbWV0aG9kIGluIHByYWN0aWNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIFN0YWJpbGl0eSBhbmQgTG9zcyBhcyBhIFF1YWxpdHkgTWV0cmljIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIG1ham9yIGFkdmFudGFnZSBvZiBXR0FOIG92ZXIgc3RhbmRhcmQgR0FOIGlzIHRoYXQgdGhlIGNyaXRpYyBsb3NzIGlzIGEgbWVhbmluZ2Z1bCBwcm94eSBmb3Igc2FtcGxlIHF1YWxpdHkuIFRoZSBjcml0aWMgbG9zcyAobmVnYXRpdmUgVyBlc3RpbWF0ZSkgZGVjcmVhc2VzIGFzIHRoZSBnZW5lcmF0b3IgaW1wcm92ZXMsIGFuZCB0aGlzIGRlY3JlYXNlIGNvcnJlbGF0ZXMgd2l0aCB2aXN1YWwgcXVhbGl0eSBpbXByb3ZlbWVudHMgYW5kIEZJRCByZWR1Y3Rpb24uIEluIHN0YW5kYXJkIEdBTiwgbmVpdGhlciB0aGUgZ2VuZXJhdG9yIG5vciB0aGUgZGlzY3JpbWluYXRvciBsb3NzIGlzIGEgcmVsaWFibGUgcXVhbGl0eSBzaWduYWwg4oCUIEQgbG9zcyBjYW4gZHJvcCB0byB6ZXJvIHdoaWxlIEcgcHJvZHVjZXMgZ2FyYmFnZSwgYW5kIEcgbG9zcyBjYW4gYmUgaGlnaCBldmVuIHdoZW4gaW1hZ2VzIGxvb2sgZ29vZC4gV0dBTiBlbGltaW5hdGVzIHRoaXMgcHJvYmxlbSBieSBjb25zdHJ1Y3Rpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiB0b3lfdHJhaW5pbmcobW9kZT1cdTAwMjd3Z2FuXHUwMDI3LCBuX3N0ZXBzPTQwMCwgc2VlZD00Mik6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3VHJhaW4gR0FOIG9yIFdHQU4gb24gYSB0b3kgMkQgR2F1c3NpYW4uIFJldHVybnMgbG9zcyBoaXN0b3JpZXMgZm9yIGNvbXBhcmlzb24uXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICB0YXJnZXQgPSB0b3JjaC50ZW5zb3IoWzMuMCwgMy4wXSlcbiAgICBHID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMiwgNjQpLCBubi5SZUxVKCksIG5uLkxpbmVhcig2NCwgMikpXG4gICAgRCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDIsIDY0KSwgbm4uTGVha3lSZUxVKDAuMiksIG5uLkxpbmVhcig2NCwgMSkpXG4gICAgaWYgbW9kZSA9PSBcdTAwMjd3Z2FuXHUwMDI3OlxuICAgICAgICBvcHRfRyA9IHRvcmNoLm9wdGltLlJNU3Byb3AoRy5wYXJhbWV0ZXJzKCksIGxyPTVlLTUpXG4gICAgICAgIG9wdF9EID0gdG9yY2gub3B0aW0uUk1TcHJvcChELnBhcmFtZXRlcnMoKSwgbHI9NWUtNSlcbiAgICBlbHNlOlxuICAgICAgICBELmFkZF9tb2R1bGUoXHUwMDI3c2lnXHUwMDI3LCBubi5TaWdtb2lkKCkpXG4gICAgICAgIG9wdF9HID0gdG9yY2gub3B0aW0uQWRhbShHLnBhcmFtZXRlcnMoKSwgbHI9MmUtNCwgYmV0YXM9KDAuNSwgMC45OTkpKVxuICAgICAgICBvcHRfRCA9IHRvcmNoLm9wdGltLkFkYW0oRC5wYXJhbWV0ZXJzKCksIGxyPTJlLTQsIGJldGFzPSgwLjUsIDAuOTk5KSlcbiAgICBsb3NzZXNfRywgbG9zc2VzX0QgPSBbXSwgW11cbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgcmVhbCA9IHRhcmdldCArIHRvcmNoLnJhbmRuKDY0LCAyKSAqIDAuNVxuICAgICAgICB6ID0gdG9yY2gucmFuZG4oNjQsIDIpXG4gICAgICAgIGZha2UgPSBHKHopXG4gICAgICAgIGlmIG1vZGUgPT0gXHUwMDI3d2dhblx1MDAyNzpcbiAgICAgICAgICAgIGRfbG9zcyA9IC0oRChyZWFsKS5tZWFuKCkgLSBEKGZha2UuZGV0YWNoKCkpLm1lYW4oKSlcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIGJjZSA9IG5uLkJDRUxvc3MoKVxuICAgICAgICAgICAgZF9sb3NzID0gYmNlKEQocmVhbCksIHRvcmNoLm9uZXMoNjQsIDEpKSArIGJjZShEKGZha2UuZGV0YWNoKCkpLCB0b3JjaC56ZXJvcyg2NCwgMSkpXG4gICAgICAgIG9wdF9ELnplcm9fZ3JhZCgpOyBkX2xvc3MuYmFja3dhcmQoKTsgb3B0X0Quc3RlcCgpXG4gICAgICAgIGlmIG1vZGUgPT0gXHUwMDI3d2dhblx1MDAyNzpcbiAgICAgICAgICAgIGZvciBwIGluIEQucGFyYW1ldGVycygpOiBwLmRhdGEuY2xhbXBfKC0wLjAxLCAwLjAxKVxuICAgICAgICAgICAgZ19sb3NzID0gLUQoRyh6KSkubWVhbigpXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICBnX2xvc3MgPSBiY2UoRChHKHopKSwgdG9yY2gub25lcyg2NCwgMSkpXG4gICAgICAgIG9wdF9HLnplcm9fZ3JhZCgpOyBnX2xvc3MuYmFja3dhcmQoKTsgb3B0X0cuc3RlcCgpXG4gICAgICAgIGxvc3Nlc19HLmFwcGVuZChnX2xvc3MuaXRlbSgpKTsgbG9zc2VzX0QuYXBwZW5kKGRfbG9zcy5pdGVtKCkpXG4gICAgcmV0dXJuIGxvc3Nlc19HLCBsb3NzZXNfRFxuXG5nYW5fRywgZ2FuX0QgPSB0b3lfdHJhaW5pbmcoXHUwMDI3Z2FuXHUwMDI3KVxud2dhbl9HLCB3Z2FuX0QgPSB0b3lfdHJhaW5pbmcoXHUwMDI3d2dhblx1MDAyNylcbnByaW50KGZcdTAwMjdHQU4gIGZpbmFsIEdfbG9zcz17Z2FuX0dbLTFdOi40Zn0gIERfbG9zcz17Z2FuX0RbLTFdOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3V0dBTiBmaW5hbCBHX2xvc3M9e3dnYW5fR1stMV06LjRmfSAgV19kaXN0PXstd2dhbl9EWy0xXTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgdHJhY2tfd19kaXN0YW5jZV92c19xdWFsaXR5KGdlbmVyYXRvciwgY3JpdGljLCBkYXRhbG9hZGVyLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZmlkX2ZuPU5vbmUsIGV2YWxfaW50ZXJ2YWw9MTAwKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdUcmFjayBXR0FOIGNyaXRpYyBXLWRpc3RhbmNlIGVzdGltYXRlIGFsb25nc2lkZSBGSUQuXG4gICAgQSBkZWNyZWFzaW5nIFcgZXN0aW1hdGUgc2hvdWxkIGNvcnJlbGF0ZSB3aXRoIGltcHJvdmluZyAobG93ZXIpIEZJRCBzY29yZXMuXG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZ2VuZXJhdG9yLmV2YWwoKTsgY3JpdGljLmV2YWwoKVxuICAgIHdfZXN0aW1hdGVzLCBmaWRfc2NvcmVzLCBzdGVwcyA9IFtdLCBbXSwgW11cbiAgICBzdGVwID0gMFxuICAgIGZvciByZWFsX2ltZ3MsIF8gaW4gZGF0YWxvYWRlcjpcbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICB6ID0gdG9yY2gucmFuZG4ocmVhbF9pbWdzLnNpemUoMCksIDEwMClcbiAgICAgICAgICAgIGZha2VfaW1ncyA9IGdlbmVyYXRvcih6KVxuICAgICAgICAgICAgY19yZWFsID0gY3JpdGljKHJlYWxfaW1ncykubWVhbigpLml0ZW0oKVxuICAgICAgICAgICAgY19mYWtlID0gY3JpdGljKGZha2VfaW1ncykubWVhbigpLml0ZW0oKVxuICAgICAgICAgICAgd19lc3QgPSBjX3JlYWwgLSBjX2Zha2VcbiAgICAgICAgd19lc3RpbWF0ZXMuYXBwZW5kKHdfZXN0KVxuICAgICAgICBpZiBmaWRfZm4gaXMgbm90IE5vbmUgYW5kIHN0ZXAgJSBldmFsX2ludGVydmFsID09IDA6XG4gICAgICAgICAgICBmaWQgPSBmaWRfZm4oZ2VuZXJhdG9yKVxuICAgICAgICAgICAgZmlkX3Njb3Jlcy5hcHBlbmQoZmlkKVxuICAgICAgICAgICAgc3RlcHMuYXBwZW5kKHN0ZXApXG4gICAgICAgICAgICBwcmludChmXHUwMDI3U3RlcCB7c3RlcDo1ZH06IFdfZXN0aW1hdGU9e3dfZXN0Oi40Zn0gIEZJRD17ZmlkOi4yZn1cdTAwMjcpXG4gICAgICAgIHN0ZXAgKz0gMVxuICAgIGlmIGxlbihmaWRfc2NvcmVzKSBcdTAwM2UgMTpcbiAgICAgICAgY29yciA9IG5wLmNvcnJjb2VmKHdfZXN0aW1hdGVzWzpsZW4oZmlkX3Njb3JlcyldLCBmaWRfc2NvcmVzKVswLCAxXVxuICAgICAgICBwcmludChmXHUwMDI3Q29ycmVsYXRpb24oV19lc3RpbWF0ZSwgRklEKSA9IHtjb3JyOi40Zn1cdTAwMjcpXG4gICAgICAgIHByaW50KFx1MDAyN0V4cGVjdGVkOiBuZWdhdGl2ZSAoaGlnaGVyIFdfZGlzdCBlc3RpbWF0ZSAtXHUwMDNlIGJldHRlci9sb3dlciBGSUQpXHUwMDI3KVxuICAgIHJldHVybiB3X2VzdGltYXRlcywgZmlkX3Njb3JlcyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdBTiBWYXJpYW50cyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkxpcHNjaGl0eiBFbmZvcmNlbWVudCIsIkxvc3MgTWVhbmluZ2Z1bD8iLCJTdGFiaWxpdHkiLCJCYXRjaE5vcm0gaW4gQ3JpdGljIiwiUmVsYXRpdmUgUXVhbGl0eSJdLCJyb3dzIjpbWyJTdGFuZGFyZCBHQU4iLCJOb25lIChKUyBkaXZlcmdlbmNlKSIsIk5vIOKAlCBvc2NpbGxhdGVzLCBub3QgY29ycmVsYXRlZCB3aXRoIHF1YWxpdHkiLCJMb3c6IG1vZGUgY29sbGFwc2UsIHZhbmlzaGluZyBncmFkaWVudHMiLCJBbGxvd2VkIChhdm9pZCBpbiBwcmFjdGljZSkiLCJCYXNlbGluZSJdLFsiV0dBTiIsIldlaWdodCBjbGlwcGluZyB0byBbLWMsIGNdIiwiWWVzIOKAlCBXIGRpc3RhbmNlIGRlY3JlYXNlcyBhcyBxdWFsaXR5IGltcHJvdmVzIiwiTW9kZXJhdGU6IGNsaXBwaW5nIGJpYXNlcyB0b3dhcmQgbGluZWFyIGNyaXRpY3MiLCJOb3QgcmVjb21tZW5kZWQiLCJCZXR0ZXIgdGhhbiBHQU4iXSxbIldHQU4tR1AiLCJHcmFkaWVudCBwZW5hbHR5IG9uIGludGVycG9sYXRlZCBwb2ludHMiLCJZZXMg4oCUIG1vcmUgYWNjdXJhdGUgVyBlc3RpbWF0ZSB0aGFuIGNsaXBwaW5nIiwiSGlnaDogc3RhYmxlIGFjcm9zcyBhcmNoaXRlY3R1cmVzIGFuZCBkYXRhc2V0cyIsIk5vdCBhbGxvd2VkICh1c2UgTGF5ZXJOb3JtKSIsIlN0cm9uZyBiYXNlbGluZSJdLFsiU04tR0FOIiwiU3BlY3RyYWwgbm9ybSBvbiBhbGwgY3JpdGljIHdlaWdodCBtYXRyaWNlcyIsIlBhcnRpYWwg4oCUIGhpbmdlIGxvc3MsIG5vdCB0cnVlIFcgZGlzdGFuY2UiLCJIaWdoOiBubyBleHRyYSBiYWNrd2FyZCBwYXNzLCBmYXN0IiwiQWxsb3dlZCIsIkNvbXBldGl0aXZlIEZJRCJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXR0FOLUdQIGlzIHRoZSBtb3N0IHdpZGVseSBhZG9wdGVkIHZhcmlhbnQgZm9yIHJlc2VhcmNoIGFuZCBwcm9kdWN0aW9uIEdBTiB0cmFpbmluZyBiZWNhdXNlIGl0IHByb3ZpZGVzIHRoZSBzdHJvbmdlc3QgdGhlb3JldGljYWwgZ3VhcmFudGVlcyAoZ3JhZGllbnQgcGVuYWx0eSBkaXJlY3RseSBlbmZvcmNlcyB0aGUgZHVhbCBjb25zdHJhaW50KSwgd29ya3Mgd2l0aCBtb3N0IGFyY2hpdGVjdHVyZXMsIGFuZCBwcm9kdWNlcyByZWxpYWJseSBpbnRlcnByZXRhYmxlIHRyYWluaW5nIGN1cnZlcy4gU04tR0FOIGlzIHByZWZlcnJlZCB3aGVuIGNvbXB1dGF0aW9uYWwgZWZmaWNpZW5jeSBtYXR0ZXJzLCBhcyBzcGVjdHJhbCBub3JtYWxpc2F0aW9uIGFkZHMgbWluaW1hbCBvdmVyaGVhZCAob25lIHBvd2VyIGl0ZXJhdGlvbiBwZXIgbGF5ZXIgcGVyIHN0ZXApIGNvbXBhcmVkIHRvIFdHQU4tR1BcdTAwMjdzIGV4dHJhIGJhY2t3YXJkIHBhc3MgdGhyb3VnaCBjcmVhdGVfZ3JhcGguIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJVc2UgUk1TcHJvcCAobm90IEFkYW0pIGZvciBXR0FOIHdpdGggd2VpZ2h0IGNsaXBwaW5nIOKAlCBBZGFtXHUwMDI3cyBtb21lbnR1bSBkZXN0YWJpbGlzZXMgV2Fzc2Vyc3RlaW4gdHJhaW5pbmcgd2l0aCBjbGlwcGluZyIsIldHQU4tR1AgdXNlcyBBZGFtIHdpdGggYmV0YXM9KDAuMCwgMC45KSDigJQgemVybyBmaXJzdCBtb21lbnQgYXZvaWRzIG1vbWVudHVtIGlzc3VlcyB3aGlsZSBzZWNvbmQgbW9tZW50IGhlbHBzIGFkYXB0YXRpb24iLCJUaGUgY3JpdGljIGxvc3MgaW4gV0dBTiBpcyBhIGxvd2VyIGJvdW5kIG9uIHRoZSB0cnVlIFcgZGlzdGFuY2U7IGEgbW9ub3RvbmljYWxseSBkZWNyZWFzaW5nIGNyaXRpYyBsb3NzIG1lYW5zIHRoZSBnZW5lcmF0b3IgaXMgaW1wcm92aW5nIiwiV2VpZ2h0IGNsaXBwaW5nIGNvbnN0YW50IGM9MC4wMSBpcyB0aGUgc3RhbmRhcmQgc3RhcnRpbmcgcG9pbnQg4oCUIGlmIHRyYWluaW5nIGlzIHNsb3cgdHJ5IGM9MC4wNTsgaWYgdW5zdGFibGUgdHJ5IGM9MC4wMDUiLCJXR0FOLUdQIGVsaW1pbmF0ZXMgdGhlIG5lZWQgZm9yIGJhdGNoIG5vcm1hbGlzYXRpb24gaW4gdGhlIGNyaXRpYyBlbnRpcmVseSDigJQgdXNlIExheWVyTm9ybSBvciBHcm91cE5vcm0gaW5zdGVhZCBmb3Igc3RhYmxlIGFjdGl2YXRpb25zIl19XQ=="
---
# Wasserstein GAN — Earth Mover Distance and Gradient Penalty

The Wasserstein GAN (Arjovsky et al., 2017) identifies a fundamental flaw in the standard GAN training objective and replaces it with a theoretically motivated alternative. Standard GANs minimise the Jensen-Shannon divergence between p_data and p_g, but JS divergence is undefined (or saturated) when the two distributions have disjoint support — which is nearly always the case in high-dimensional spaces early in training. WGAN replaces JS with the Wasserstein-1 distance, which is always defined and provides meaningful gradients even when the distributions do not overlap.

## The JS Divergence Problem

In high-dimensional spaces, the real data distribution p_data and the generated distribution p_g concentrate on low-dimensional manifolds that have measure zero relative to the ambient space. When these manifolds are disjoint (which happens almost certainly early in training), the JS divergence is exactly log(2) — a constant with gradient zero. This means the discriminator saturates, providing no gradient to the generator. The GAN then oscillates or stalls rather than improving.

$$\text{JS}(p \| q) = \frac{1}{2} KL\!\left(p \,\Big\|\, \frac{p+q}{2}\right) + \frac{1}{2} KL\!\left(q \,\Big\|\, \frac{p+q}{2}\right)$$

## Wasserstein-1 Distance

The Wasserstein-1 (Earth Mover) distance W(p, q) measures the minimum cost of transporting mass from distribution p to distribution q, where cost is the distance moved times the mass moved. Unlike JS divergence, W(p,q) is defined and continuous even when p and q have disjoint supports — it returns the physical distance between the two distribution masses. As p_g moves toward p_data during training, W(p_g, p_data) decreases monotonically and provides useful gradient information throughout.

$$W(p, q) = \inf_{\gamma \in \Pi(p,q)} \mathbb{E}_{(x,y) \sim \gamma}[\|x - y\|]$$

## Kantorovich-Rubinstein Duality

Computing W(p,q) directly is intractable for high-dimensional distributions. The Kantorovich-Rubinstein duality provides a tractable dual formulation: W(p,q) = sup_{||f||_L ≤ 1} (E_p[f(x)] - E_q[f(x)]), where the supremum is over all 1-Lipschitz functions f. In WGAN, the critic (replacing the discriminator) parameterises f. Training maximises E[f(real)] - E[f(fake)] over the critic while enforcing the 1-Lipschitz constraint. The critic is not a classifier — it outputs unbounded real-valued scores, not probabilities.

$$W(p, q) = \sup_{\|f\|_L \leq 1} \left( \mathbb{E}_{x \sim p}[f(x)] - \mathbb{E}_{x \sim q}[f(x)] \right)$$

## WGAN Training with Weight Clipping

WGAN enforces the 1-Lipschitz constraint on the critic by clipping all critic weights to the interval [-c, c] after each gradient step (typically c=0.01). The critic is trained to near-convergence (n_critic=5 steps) before each generator update. Unlike standard GAN, WGAN uses RMSprop rather than Adam — the authors found Adam's momentum destabilises WGAN training. The generator loss is simply -E[f(G(z))], and the critic loss is -(E[f(real)] - E[f(fake)]).

```python
import torch
import torch.nn as nn
import torch.optim as optim

def train_wgan(generator, critic, dataloader,
               num_epochs=100, n_critic=5, clip_c=0.01, latent_dim=100):
    '''WGAN training with weight clipping. Critic outputs unbounded scalars.
    Use RMSprop not Adam; clip critic weights to [-c, c] after each step.
    '''
    opt_G = optim.RMSprop(generator.parameters(), lr=5e-5)
    opt_C = optim.RMSprop(critic.parameters(), lr=5e-5)
    for epoch in range(num_epochs):
        for real_imgs, _ in dataloader:
            bs = real_imgs.size(0)
            # --- Critic: n_critic steps per generator step ---
            for _ in range(n_critic):
                opt_C.zero_grad()
                z = torch.randn(bs, latent_dim)
                fake_imgs = generator(z).detach()
                # Maximize E[f(real)] - E[f(fake)], i.e. minimise negation
                c_real = critic(real_imgs).mean()
                c_fake = critic(fake_imgs).mean()
                c_loss = -(c_real - c_fake)
                c_loss.backward()
                opt_C.step()
                # Enforce 1-Lipschitz constraint via weight clipping
                for p in critic.parameters():
                    p.data.clamp_(-clip_c, clip_c)
            # --- Generator: maximize E[f(G(z))] ---
            opt_G.zero_grad()
            z = torch.randn(bs, latent_dim)
            g_loss = -critic(generator(z)).mean()
            g_loss.backward()
            opt_G.step()
        w_dist = (c_real - c_fake).item()
        print(f'Epoch {epoch}: W_dist={w_dist:.4f}  G_loss={g_loss.item():.4f}')
```

```python
import numpy as np
from scipy.stats import wasserstein_distance, gaussian_kde

def compare_w1_vs_js(mean1=0.0, std1=1.0, mean2=2.0, std2=1.0, n=20000):
    '''Compare Wasserstein-1 and JS divergence on 1D Gaussians.
    JS saturates at log(2) for disjoint distributions; W1 stays meaningful.
    '''
    p = np.random.normal(mean1, std1, n)
    q = np.random.normal(mean2, std2, n)
    w1 = wasserstein_distance(p, q)
    kde_p, kde_q = gaussian_kde(p), gaussian_kde(q)
    x = np.linspace(min(p.min(), q.min()), max(p.max(), q.max()), 500)
    px, qx = kde_p(x) + 1e-10, kde_q(x) + 1e-10
    mx = 0.5 * (px + qx)
    js = 0.5 * (np.trapz(px * np.log(px / mx), x) +
                np.trapz(qx * np.log(qx / mx), x))
    return w1, js

print(f'{"Separation":<12} {"W1-distance":<14} {"JS-divergence":<16} {"JS saturated?"}')
print('-' * 58)
for sep in [0.5, 2.0, 5.0, 10.0, 20.0]:
    w1, js = compare_w1_vs_js(mean1=0.0, mean2=sep)
    saturated = 'YES (no gradient!)' if js > 0.65 else 'no'
    print(f'{sep:<12.1f} {w1:<14.4f} {js:<16.4f} {saturated}')
print(f'JS saturates at log(2) = {np.log(2):.4f} for disjoint distributions.')
print('W1 continues scaling linearly with separation — always a useful gradient signal.')
```

## Weight Clipping Problems

Weight clipping enforces the Lipschitz constraint, but it is crude. All weights are forced into [-c, c], which biases the critic toward linear functions — the simplest functions that respect the bound while using all available weight capacity. This dramatically reduces the critic's expressive power. With c too small, gradients vanish in deep critics; with c too large, the Lipschitz constraint is not meaningfully enforced. The WGAN authors themselves acknowledged clipping as a stopgap measure.

> **Weight Clipping Limitations**: Weight clipping biases the critic toward linear functions because clipping all weights uniformly suppresses deep compositional features. This capacity underuse means the critic cannot fit the true Wasserstein distance well. The solution is WGAN-GP (Gulrajani 2017), which replaces clipping with a gradient penalty term: lambda * E[(||grad_x D(x_hat)||_2 - 1)^2] evaluated at interpolated points x_hat between real and fake samples. WGAN-GP is the preferred method in practice.

## Training Stability and Loss as a Quality Metric

A major advantage of WGAN over standard GAN is that the critic loss is a meaningful proxy for sample quality. The critic loss (negative W estimate) decreases as the generator improves, and this decrease correlates with visual quality improvements and FID reduction. In standard GAN, neither the generator nor the discriminator loss is a reliable quality signal — D loss can drop to zero while G produces garbage, and G loss can be high even when images look good. WGAN eliminates this problem by construction.

```python
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def toy_training(mode='wgan', n_steps=400, seed=42):
    '''Train GAN or WGAN on a toy 2D Gaussian. Returns loss histories for comparison.'''
    torch.manual_seed(seed)
    target = torch.tensor([3.0, 3.0])
    G = nn.Sequential(nn.Linear(2, 64), nn.ReLU(), nn.Linear(64, 2))
    D = nn.Sequential(nn.Linear(2, 64), nn.LeakyReLU(0.2), nn.Linear(64, 1))
    if mode == 'wgan':
        opt_G = torch.optim.RMSprop(G.parameters(), lr=5e-5)
        opt_D = torch.optim.RMSprop(D.parameters(), lr=5e-5)
    else:
        D.add_module('sig', nn.Sigmoid())
        opt_G = torch.optim.Adam(G.parameters(), lr=2e-4, betas=(0.5, 0.999))
        opt_D = torch.optim.Adam(D.parameters(), lr=2e-4, betas=(0.5, 0.999))
    losses_G, losses_D = [], []
    for step in range(n_steps):
        real = target + torch.randn(64, 2) * 0.5
        z = torch.randn(64, 2)
        fake = G(z)
        if mode == 'wgan':
            d_loss = -(D(real).mean() - D(fake.detach()).mean())
        else:
            bce = nn.BCELoss()
            d_loss = bce(D(real), torch.ones(64, 1)) + bce(D(fake.detach()), torch.zeros(64, 1))
        opt_D.zero_grad(); d_loss.backward(); opt_D.step()
        if mode == 'wgan':
            for p in D.parameters(): p.data.clamp_(-0.01, 0.01)
            g_loss = -D(G(z)).mean()
        else:
            g_loss = bce(D(G(z)), torch.ones(64, 1))
        opt_G.zero_grad(); g_loss.backward(); opt_G.step()
        losses_G.append(g_loss.item()); losses_D.append(d_loss.item())
    return losses_G, losses_D

gan_G, gan_D = toy_training('gan')
wgan_G, wgan_D = toy_training('wgan')
print(f'GAN  final G_loss={gan_G[-1]:.4f}  D_loss={gan_D[-1]:.4f}')
print(f'WGAN final G_loss={wgan_G[-1]:.4f}  W_dist={-wgan_D[-1]:.4f}')
```

```python
import torch
import numpy as np

def track_w_distance_vs_quality(generator, critic, dataloader,
                                 fid_fn=None, eval_interval=100):
    '''Track WGAN critic W-distance estimate alongside FID.
    A decreasing W estimate should correlate with improving (lower) FID scores.
    '''
    generator.eval(); critic.eval()
    w_estimates, fid_scores, steps = [], [], []
    step = 0
    for real_imgs, _ in dataloader:
        with torch.no_grad():
            z = torch.randn(real_imgs.size(0), 100)
            fake_imgs = generator(z)
            c_real = critic(real_imgs).mean().item()
            c_fake = critic(fake_imgs).mean().item()
            w_est = c_real - c_fake
        w_estimates.append(w_est)
        if fid_fn is not None and step % eval_interval == 0:
            fid = fid_fn(generator)
            fid_scores.append(fid)
            steps.append(step)
            print(f'Step {step:5d}: W_estimate={w_est:.4f}  FID={fid:.2f}')
        step += 1
    if len(fid_scores) > 1:
        corr = np.corrcoef(w_estimates[:len(fid_scores)], fid_scores)[0, 1]
        print(f'Correlation(W_estimate, FID) = {corr:.4f}')
        print('Expected: negative (higher W_dist estimate -> better/lower FID)')
    return w_estimates, fid_scores
```

## GAN Variants Comparison

| Method | Lipschitz Enforcement | Loss Meaningful? | Stability | BatchNorm in Critic | Relative Quality |
| --- | --- | --- | --- | --- | --- |
| Standard GAN | None (JS divergence) | No — oscillates, not correlated with quality | Low: mode collapse, vanishing gradients | Allowed (avoid in practice) | Baseline |
| WGAN | Weight clipping to [-c, c] | Yes — W distance decreases as quality improves | Moderate: clipping biases toward linear critics | Not recommended | Better than GAN |
| WGAN-GP | Gradient penalty on interpolated points | Yes — more accurate W estimate than clipping | High: stable across architectures and datasets | Not allowed (use LayerNorm) | Strong baseline |
| SN-GAN | Spectral norm on all critic weight matrices | Partial — hinge loss, not true W distance | High: no extra backward pass, fast | Allowed | Competitive FID |

WGAN-GP is the most widely adopted variant for research and production GAN training because it provides the strongest theoretical guarantees (gradient penalty directly enforces the dual constraint), works with most architectures, and produces reliably interpretable training curves. SN-GAN is preferred when computational efficiency matters, as spectral normalisation adds minimal overhead (one power iteration per layer per step) compared to WGAN-GP's extra backward pass through create_graph.

- Use RMSprop (not Adam) for WGAN with weight clipping — Adam's momentum destabilises Wasserstein training with clipping
- WGAN-GP uses Adam with betas=(0.0, 0.9) — zero first moment avoids momentum issues while second moment helps adaptation
- The critic loss in WGAN is a lower bound on the true W distance; a monotonically decreasing critic loss means the generator is improving
- Weight clipping constant c=0.01 is the standard starting point — if training is slow try c=0.05; if unstable try c=0.005
- WGAN-GP eliminates the need for batch normalisation in the critic entirely — use LayerNorm or GroupNorm instead for stable activations

