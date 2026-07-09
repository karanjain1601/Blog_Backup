---
title: "Gradient Clipping — Norm and Value Clipping"
slug: "gradient-clipping"
description: "Why gradients explode in deep and recurrent networks, global norm clipping vs value clipping, PyTorch implementation, monitoring gradient health, and interactions with gradient accumulation."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR3JhZGllbnQgY2xpcHBpbmcgaXMgYSBzaW1wbGUgYnV0IGVzc2VudGlhbCB0cmFpbmluZyBzdGFiaWxpemF0aW9uIHRlY2huaXF1ZSwgZXNwZWNpYWxseSBmb3IgcmVjdXJyZW50IG5ldHdvcmtzIGFuZCBsYXJnZSBsYW5ndWFnZSBtb2RlbHMuIFdpdGhvdXQgaXQsIG9jY2FzaW9uYWwgbGFyZ2UgZ3JhZGllbnRzIGNhbiBjYXVzZSB3ZWlnaHQgdXBkYXRlcyB0aGF0IGNvbXBsZXRlbHkgZGVzdGFiaWxpemUgdHJhaW5pbmcg4oCUIHRoZSBcdTAwMjdleHBsb2RpbmcgZ3JhZGllbnRcdTAwMjcgcHJvYmxlbS4gQ2xpcHBpbmcgYm91bmRzIHRoZSBpbmZsdWVuY2Ugb2YgYW55IHNpbmdsZSBncmFkaWVudCBzaWduYWwgd2hpbGUgcHJlc2VydmluZyB0aGUgdXBkYXRlIGRpcmVjdGlvbiwgYWN0aW5nIGFzIGFuIGFkYXB0aXZlIGxlYXJuaW5nIHJhdGUgdGhhdCBzY2FsZXMgZG93biBvbmx5IHdoZW4gbmVlZGVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4cGxvZGluZyBHcmFkaWVudHMgaW4gRGVlcCBOZXR3b3JrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRHVyaW5nIGJhY2twcm9wYWdhdGlvbiB0aHJvdWdoIHRpbWUgKEJQVFQpIGluIFJOTnMsIHRoZSBncmFkaWVudCBmbG93cyB0aHJvdWdoIGEgY2hhaW4gb2YgSmFjb2JpYW5zOiDiiIJML+KIgmjigoAgPSAo4oiCaF9UL+KIgmjigoAp4bWAIOKIgkwv4oiCaF9UID0gKOKIj+KCnCBXX2howrdkaWFnKM+DXHUwMDI3KGjigpwpKSnhtYAg4oiCTC/iiIJoX1QuIElmIHRoZSBzcGVjdHJhbCByYWRpdXMgz4EoV19oaCkgXHUwMDNlIDEsIHRoZSBwcm9kdWN0IG9mIEphY29iaWFucyBncm93cyBleHBvbmVudGlhbGx5IHdpdGggc2VxdWVuY2UgbGVuZ3RoIFQ6IOKAluKIj0rigpzigJYg4omIIM+B4bWALiBGb3Igz4E9MS4xIGFuZCBUPTEwMCwgdGhlIGdyYWRpZW50IGFtcGxpZmljYXRpb24gaXMgMS4xwrnigbDigbAg4omIIDEw4oG0LiBEZWVwIGZlZWRmb3J3YXJkIG5ldHdvcmtzIGZhY2UgdGhlIHNhbWUgaXNzdWU6IGVhY2ggbGF5ZXIgbXVsdGlwbGllcyBieSBhIHdlaWdodCBtYXRyaXgsIGFuZCBpZiB0aGUgc2luZ3VsYXIgdmFsdWVzIGV4Y2VlZCAxIHRoZSBwcm9kdWN0IGV4cGxvZGVzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQlBUVCBhbmQgRXhwb25lbnRpYWwgR3JhZGllbnQgR3Jvd3RoIiwiY29udGVudCI6IlRoZSBwcm9kdWN0IG9mIFQgSmFjb2JpYW5zIOKIj+KCnErigpwgaGFzIG5vcm0gdGhhdCBncm93cyBhcyDPgShKKeG1gCB3aGVyZSDPgSBpcyB0aGUgc3BlY3RyYWwgcmFkaXVzLiBGb3Igz4FcdTAwM2UxOiBleHBvbmVudGlhbCBleHBsb3Npb24uIEZvciDPgVx1MDAzYzE6IGV4cG9uZW50aWFsIHZhbmlzaGluZy4gVGhlIDEuMCBib3VuZGFyeSBpcyB1bnN0YWJsZSDigJQgdHlwaWNhbCBSTk5zIGluaXRpYWxpemVkIHdpdGggz4HiiYgxIHF1aWNrbHkgZHJpZnQuIEdyYWRpZW50IGNsaXBwaW5nIGhhbmRsZXMgdGhlIGV4cGxvc2lvbiBzaWRlOyBnYXRpbmcgbWVjaGFuaXNtcyAoTFNUTSwgR1JVKSBhbmQgY2FyZWZ1bCBpbml0aWFsaXphdGlvbiBoYW5kbGUgdmFuaXNoaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgcm5uX3N0ZXAoaCwgeCwgV19oaCwgV194aCwgYik6XG4gICAgXCJcIlwiU2luZ2xlIFJOTiBzdGVwOiBoX3QgPSB0YW5oKFdfaGggQCBoX3t0LTF9ICsgV194aCBAIHhfdCArIGIpLlwiXCJcIlxuICAgIHJldHVybiB0b3JjaC50YW5oKFdfaGggQCBoICsgV194aCBAIHggKyBiKVxuXG5kZWYgdHJhY2tfYnB0dF9ncmFkaWVudF9ub3JtcyhzZXFfbGVuPTgwLCBoaWRkZW49MTYsIHNwZWN0cmFsX3JhZGl1cz0xLjEsIHNlZWQ9MCk6XG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICAjIEluaXRpYWxpemUgV19oaCB3aXRoIGdpdmVuIHNwZWN0cmFsIHJhZGl1c1xuICAgIFdfcmF3ID0gdG9yY2gucmFuZG4oaGlkZGVuLCBoaWRkZW4pXG4gICAgVSwgUywgVmggPSB0b3JjaC5saW5hbGcuc3ZkKFdfcmF3KVxuICAgIFdfaGggPSAoVSBAIFZoKSAqIHNwZWN0cmFsX3JhZGl1cyAgIyBzcGVjdHJhbCByYWRpdXMgZXhhY3RseSA9IDEuMVxuICAgIFdfaGgucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcblxuICAgIFdfeGggPSB0b3JjaC5yYW5kbihoaWRkZW4sIDQpICogMC4xXG4gICAgYiA9IHRvcmNoLnplcm9zKGhpZGRlbilcbiAgICB4X3NlcSA9IHRvcmNoLnJhbmRuKHNlcV9sZW4sIDQpXG5cbiAgICBwcmludChmXCJCUFRUIGdyYWRpZW50IG5vcm1zIChoaWRkZW49e2hpZGRlbn0sIHNwZWN0cmFsIHJhZGl1cz17c3BlY3RyYWxfcmFkaXVzfSlcIilcbiAgICBwcmludChmXCJ7XHUwMDI3VGltZSBzdGVwXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3fHxkTC9kV19oaHx8XHUwMDI3Olx1MDAzZTE2fSB7XHUwMDI3U3RhdHVzXHUwMDI3Olx1MDAzZTEyfVwiKVxuXG4gICAgbm9ybXMgPSBbXVxuICAgIGZvciB0IGluIHJhbmdlKHNlcV9sZW4pOlxuICAgICAgICBoID0gdG9yY2guemVyb3MoaGlkZGVuKVxuICAgICAgICBmb3IgcyBpbiByYW5nZSh0ICsgMSk6XG4gICAgICAgICAgICBoID0gcm5uX3N0ZXAoaCwgeF9zZXFbc10sIFdfaGgsIFdfeGgsIGIpXG4gICAgICAgIGxvc3MgPSBoLnN1bSgpXG4gICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICBpZiBXX2hoLmdyYWQgaXMgbm90IE5vbmUgYW5kIHQgJSAxNSA9PSAwOlxuICAgICAgICAgICAgZ24gPSBXX2hoLmdyYWQubm9ybSgpLml0ZW0oKVxuICAgICAgICAgICAgbm9ybXMuYXBwZW5kKCh0LCBnbikpXG4gICAgICAgICAgICBzdGF0dXMgPSBcIkVYUExPRElOR1wiIGlmIGduIFx1MDAzZSA1MCBlbHNlIChcIndhcm5pbmdcIiBpZiBnbiBcdTAwM2UgNSBlbHNlIFwic3RhYmxlXCIpXG4gICAgICAgICAgICBwcmludChmXCJ7dDpcdTAwM2UxMH0ge2duOlx1MDAzZTE2LjJmfSB7c3RhdHVzOlx1MDAzZTEyfVwiKVxuICAgICAgICAgICAgV19oaC5ncmFkLnplcm9fKClcbiAgICByZXR1cm4gbm9ybXNcblxubm9ybXMgPSB0cmFja19icHR0X2dyYWRpZW50X25vcm1zKHNlcV9sZW49NzUsIGhpZGRlbj0xMiwgc3BlY3RyYWxfcmFkaXVzPTEuMDgpXG5wcmludChcIlxcbkdyYWRpZW50IGdyb3dzIGV4cG9uZW50aWFsbHkgd2l0aCBzZXF1ZW5jZSBsZW5ndGgg4oCUIGNsaXBwaW5nIGlzIGVzc2VudGlhbC5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHbG9iYWwgTm9ybSBDbGlwcGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2xvYmFsIG5vcm0gY2xpcHBpbmcgY29tcHV0ZXMgdGhlIG5vcm0gYWNyb3NzIEFMTCBwYXJhbWV0ZXJzIHNpbXVsdGFuZW91c2x5OiBnX25vcm0gPSDiiJoozqPhtaLigJbiiIfOuOG1ouKAlsKyKS4gSWYgZ19ub3JtIGV4Y2VlZHMgdGhlIHRocmVzaG9sZCBjLCBldmVyeSBncmFkaWVudCBpcyBzY2FsZWQgYnkgdGhlIHNhbWUgZmFjdG9yIGMvZ19ub3JtLiBUaGlzIGlzIHRoZSBjcml0aWNhbCBwcm9wZXJ0eTogYWxsIGdyYWRpZW50cyBhcmUgc2NhbGVkIHVuaWZvcm1seSwgc28gdGhlaXIgcmVsYXRpdmUgbWFnbml0dWRlcyBhbmQgdGh1cyB0aGUgZ3JhZGllbnQgZGlyZWN0aW9uIGlzIHByZXNlcnZlZC4gVGhlIG9wdGltaXplciB0YWtlcyBhIHN0ZXAgaW4gdGhlIHNhbWUgZGlyZWN0aW9uIGFzIHRoZSB0cnVlIGdyYWRpZW50LCBqdXN0IHNob3J0ZXIuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOnRydWUsIml0ZW1zIjpbIkNvbXB1dGUgZ2xvYmFsIGdyYWRpZW50IG5vcm06IGdfbm9ybSA9IHNxcnQoc3VtIG92ZXIgYWxsIHBhcmFtcyBvZiB8fGdyYWRfaXx8wrIpIiwiSWYgZ19ub3JtIFx1MDAzZSB0aHJlc2hvbGQ6IHNjYWxlID0gdGhyZXNob2xkIC8gZ19ub3JtOyBlbHNlIHNjYWxlID0gMS4wIiwiQXBwbHk6IGdyYWRfaSDihpAgZ3JhZF9pICogc2NhbGUgZm9yIEFMTCBwYXJhbWV0ZXIgZ3JvdXBzIHNpbXVsdGFuZW91c2x5IiwiUGFzcyBzY2FsZWQgZ3JhZGllbnRzIHRvIG9wdGltaXplci5zdGVwKCkg4oCUIGRpcmVjdGlvbiBwcmVzZXJ2ZWQsIG1hZ25pdHVkZSBib3VuZGVkIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZhbHVlIENsaXBwaW5nIGFuZCBXaHkgSXQgSXMgSW5mZXJpb3IifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZhbHVlIGNsaXBwaW5nIGNsaXBzIGVhY2ggZ3JhZGllbnQgY29tcG9uZW50IGluZGVwZW5kZW50bHk6IGfhtaIg4oaQIGNsaXAoZ+G1oiwg4oiSYywgYykuIFRoaXMgaXMgc2ltcGxlciBidXQgY2hhbmdlcyB0aGUgZ3JhZGllbnQgZGlyZWN0aW9uOiBpZiBvbmUgcGFyYW1ldGVyIGhhcyBhIGxhcmdlIGdyYWRpZW50IHRoYXQgZ2V0cyBjbGlwcGVkIHdoaWxlIG90aGVycyBhcmUgc21hbGwsIHRoZSByZWxhdGl2ZSBtYWduaXR1ZGVzIGFyZSBkaXN0b3J0ZWQuIFRoZSByZXN1bHRpbmcgdXBkYXRlIHBvaW50cyBpbiBhIGRpZmZlcmVudCBkaXJlY3Rpb24gdGhhbiB0aGUgdHJ1ZSBncmFkaWVudC4gVGhpcyBjYW4gc2xvdyBjb252ZXJnZW5jZSBhbmQgaW50cm9kdWNlIHN5c3RlbWF0aWMgYmlhcywgcGFydGljdWxhcmx5IHByb2JsZW1hdGljIGZvciBjb3JyZWxhdGVkIHBhcmFtZXRlcnMuIFZhbHVlIGNsaXBwaW5nIGlzIHNvbWV0aW1lcyB1c2VkIGluIERRTi1zdHlsZSBSTCBidXQgaXMgZ2VuZXJhbGx5IG5vdCByZWNvbW1lbmRlZC4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoeSBEaXJlY3Rpb24gTWF0dGVycyIsImNvbnRlbnQiOiJHcmFkaWVudCBkZXNjZW50IHdvcmtzIGJlY2F1c2Ug4oiS4oiHZiBwb2ludHMgaW4gdGhlIHN0ZWVwZXN0IGRlc2NlbnQgZGlyZWN0aW9uLiBBbnkgcG9zaXRpdmUgc2NhbGluZyBvZiB0aGUgZ3JhZGllbnQgc3RpbGwgcG9pbnRzIGRvd25oaWxsLiBCdXQgZWxlbWVudHdpc2UgY2xpcHBpbmcgY3JlYXRlcyBhIGdyYWRpZW50IHRoYXQgaXMgbm8gbG9uZ2VyIHByb3BvcnRpb25hbCB0byDiiIdmIOKAlCBzb21lIGNvbXBvbmVudHMgYXJlIHN1cHByZXNzZWQgcmVsYXRpdmUgdG8gb3RoZXJzLCBlZmZlY3RpdmVseSBjaGFuZ2luZyB0aGUgcHJlY29uZGl0aW9uaW5nLiBUaGUgcmVzdWx0aW5nIHVwZGF0ZSBkaXJlY3Rpb24gbWF5IG5vdCBiZSBhIGRlc2NlbnQgZGlyZWN0aW9uIGF0IGFsbCBmb3Igbm9uLXNlcGFyYWJsZSBvYmplY3RpdmVzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJGb3JtdWxhIiwiRGlyZWN0aW9uIFByZXNlcnZlZCIsIlJlY29tbWVuZGVkIl0sInJvd3MiOltbIkdsb2JhbCBOb3JtIENsaXAiLCJnIOKGkCBnwrdtaW4oMSwgYy/igJZn4oCWX2dsb2JhbCkiLCJZZXMg4oCUIGFsbCBwYXJhbXMgc2NhbGVkIHVuaWZvcm1seSIsIlllcyDigJQgZGVmYXVsdCBmb3IgdHJhbnNmb3JtZXJzLCBSTk5zLCBMTE1zIl0sWyJWYWx1ZSBDbGlwIiwiZ+G1oiDihpAgY2xpcChn4bWiLCDiiJJjLCBjKSBwZXIgZWxlbWVudCIsIk5vIOKAlCBjaGFuZ2VzIHJlbGF0aXZlIG1hZ25pdHVkZXMiLCJSYXJlbHkg4oCUIHNvbWUgUkwgKERRTiksIG5vdCByZWNvbW1lbmRlZCBmb3Igc3VwZXJ2aXNlZCJdLFsiUGVyLWxheWVyIE5vcm0gQ2xpcCIsImfigpcg4oaQIGfigpfCt21pbigxLCBjL+KAlmfigpfigJYpIHBlciBsYXllciBsIiwiWWVzIOKAlCB3aXRoaW4gZWFjaCBsYXllciIsIlNvbWV0aW1lcyDigJQgbGF5ZXItc2Vuc2l0aXZlIGFyY2hpdGVjdHVyZXMiXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZ2xvYmFsX25vcm1fY2xpcChncmFkcywgdGhyZXNob2xkKTpcbiAgICBcIlwiXCJDbGlwIGJ5IGdsb2JhbCBub3JtIOKAlCBwcmVzZXJ2ZXMgZ3JhZGllbnQgZGlyZWN0aW9uLlwiXCJcIlxuICAgIGdsb2JhbF9ub3JtID0gdG9yY2guc3FydChzdW0oZy5ub3JtKCkqKjIgZm9yIGcgaW4gZ3JhZHMpKVxuICAgIGlmIGdsb2JhbF9ub3JtIFx1MDAzZSB0aHJlc2hvbGQ6XG4gICAgICAgIHNjYWxlID0gdGhyZXNob2xkIC8gKGdsb2JhbF9ub3JtICsgMWUtMTIpXG4gICAgICAgIHJldHVybiBbZyAqIHNjYWxlIGZvciBnIGluIGdyYWRzXSwgZ2xvYmFsX25vcm0uaXRlbSgpLCBUcnVlXG4gICAgcmV0dXJuIGxpc3QoZ3JhZHMpLCBnbG9iYWxfbm9ybS5pdGVtKCksIEZhbHNlXG5cbmRlZiB2YWx1ZV9jbGlwKGdyYWRzLCB0aHJlc2hvbGQpOlxuICAgIFwiXCJcIkNsaXAgZWFjaCBlbGVtZW50IGluZGVwZW5kZW50bHkg4oCUIGNoYW5nZXMgZ3JhZGllbnQgZGlyZWN0aW9uLlwiXCJcIlxuICAgIGNsaXBwZWQgPSBbdG9yY2guY2xhbXAoZywgLXRocmVzaG9sZCwgdGhyZXNob2xkKSBmb3IgZyBpbiBncmFkc11cbiAgICBvcmlnX25vcm0gPSB0b3JjaC5zcXJ0KHN1bShnLm5vcm0oKSoqMiBmb3IgZyBpbiBncmFkcykpLml0ZW0oKVxuICAgIGNsaXBfbm9ybSA9IHRvcmNoLnNxcnQoc3VtKGcubm9ybSgpKioyIGZvciBnIGluIGNsaXBwZWQpKS5pdGVtKClcbiAgICByZXR1cm4gY2xpcHBlZCwgb3JpZ19ub3JtLCBjbGlwX25vcm1cblxudG9yY2gubWFudWFsX3NlZWQoNSlcbmdyYWRzID0gW3RvcmNoLnJhbmRuKDQsIDYpICogNC4wLCB0b3JjaC5yYW5kbig0KSAqIDguMF1cbnRocmVzaG9sZCA9IDEuMFxuXG5ub3JtX2csIGdfbm9ybSwgd2FzX2NsaXBwZWQgPSBnbG9iYWxfbm9ybV9jbGlwKGdyYWRzLCB0aHJlc2hvbGQpXG52YWxfZywgb3JpZ19ub3JtLCB2YWxfbm9ybSA9IHZhbHVlX2NsaXAoZ3JhZHMsIHRocmVzaG9sZClcblxuZGlyX29yaWcgPSB0b3JjaC5jYXQoW2cuZmxhdHRlbigpIGZvciBnIGluIGdyYWRzXSkuZmxvYXQoKVxuZGlyX25vcm0gPSB0b3JjaC5jYXQoW2cuZmxhdHRlbigpIGZvciBnIGluIG5vcm1fZ10pLmZsb2F0KClcbmRpcl92YWwgID0gdG9yY2guY2F0KFtnLmZsYXR0ZW4oKSBmb3IgZyBpbiB2YWxfZ10pLmZsb2F0KClcblxuY29zX25vcm0gPSB0b3JjaC5kb3QoZGlyX29yaWcvZGlyX29yaWcubm9ybSgpLCBkaXJfbm9ybS9kaXJfbm9ybS5ub3JtKCkpLml0ZW0oKVxuY29zX3ZhbCAgPSB0b3JjaC5kb3QoZGlyX29yaWcvZGlyX29yaWcubm9ybSgpLCBkaXJfdmFsL2Rpcl92YWwubm9ybSgpKS5pdGVtKClcblxucHJpbnQoZlwiT3JpZ2luYWwgZ2xvYmFsIG5vcm06IHtnX25vcm06LjRmfVwiKVxucHJpbnQoZlwiXFxuR2xvYmFsIE5vcm0gQ2xpcCAodGhyZXNob2xkPXt0aHJlc2hvbGR9KTpcIilcbnByaW50KGZcIiAgUmVzdWx0IG5vcm06IHt0b3JjaC5zcXJ0KHN1bShnLm5vcm0oKSoqMiBmb3IgZyBpbiBub3JtX2cpKS5pdGVtKCk6LjRmfVwiKVxucHJpbnQoZlwiICBDb3NpbmUgc2ltaWxhcml0eSB3aXRoIG9yaWdpbmFsOiB7Y29zX25vcm06LjZmfSAoMS4wID0gc2FtZSBkaXJlY3Rpb24pXCIpXG5wcmludChmXCJcXG5WYWx1ZSBDbGlwICh0aHJlc2hvbGQ9e3RocmVzaG9sZH0pOlwiKVxucHJpbnQoZlwiICBSZXN1bHQgbm9ybToge3ZhbF9ub3JtOi40Zn1cIilcbnByaW50KGZcIiAgQ29zaW5lIHNpbWlsYXJpdHkgd2l0aCBvcmlnaW5hbDoge2Nvc192YWw6LjRmfSAgXHUwMDNjLSBkaXJlY3Rpb24gY2hhbmdlZCFcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQeVRvcmNoIEltcGxlbWVudGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJ0b3JjaC5ubi51dGlscy5jbGlwX2dyYWRfbm9ybV8gaXMgdGhlIHN0YW5kYXJkIFB5VG9yY2ggZnVuY3Rpb24gZm9yIGdsb2JhbCBub3JtIGNsaXBwaW5nLiBJdCByZXR1cm5zIHRoZSBwcmUtY2xpcHBpbmcgZ3JhZGllbnQgbm9ybSwgd2hpY2ggaXMgaW52YWx1YWJsZSBmb3IgbW9uaXRvcmluZyB0cmFpbmluZyBoZWFsdGguIFRoZSBmdW5jdGlvbiBtb2RpZmllcyBncmFkaWVudHMgaW4tcGxhY2UgYmVmb3JlIHRoZSBvcHRpbWl6ZXIgc3RlcC4gSXQgbXVzdCBiZSBjYWxsZWQgQUZURVIgbG9zcy5iYWNrd2FyZCgpIGFuZCBCRUZPUkUgb3B0aW1pemVyLnN0ZXAoKS4gV2hlbiB1c2luZyBncmFkaWVudCBhY2N1bXVsYXRpb24sIGNsaXAgYWZ0ZXIgdGhlIGZ1bGwgYWNjdW11bGF0aW9uIGlzIGNvbXBsZXRlIOKAlCBub3QgYWZ0ZXIgZWFjaCBtaWNyby1iYXRjaCBiYWNrd2FyZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IGRlcXVlXG5cbmNsYXNzIEdyYWROb3JtVHJhY2tlcjpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgd2luZG93PTEwMCk6XG4gICAgICAgIHNlbGYud2luZG93ID0gZGVxdWUobWF4bGVuPXdpbmRvdylcbiAgICAgICAgc2VsZi50b3RhbCA9IDBcbiAgICAgICAgc2VsZi5jbGlwcGVkID0gMFxuXG4gICAgZGVmIHVwZGF0ZShzZWxmLCBub3JtLCB0aHJlc2hvbGQpOlxuICAgICAgICBzZWxmLndpbmRvdy5hcHBlbmQobm9ybSlcbiAgICAgICAgc2VsZi50b3RhbCArPSAxXG4gICAgICAgIGlmIG5vcm0gXHUwMDNlIHRocmVzaG9sZDpcbiAgICAgICAgICAgIHNlbGYuY2xpcHBlZCArPSAxXG5cbiAgICBAcHJvcGVydHlcbiAgICBkZWYgY2xpcF9yYXRlKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5jbGlwcGVkIC8gbWF4KHNlbGYudG90YWwsIDEpXG5cbmRlZiB0cmFpbl9sb29wKG1vZGVsLCBYLCB5LCBjbGlwX3RocmVzaG9sZD0xLjAsIG5fc3RlcHM9MTAwKTpcbiAgICBsb3NzX2ZuID0gbm4uTVNFTG9zcygpXG4gICAgb3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG4gICAgdHJhY2tlciA9IEdyYWROb3JtVHJhY2tlcigpXG5cbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgIGxvc3MgPSBsb3NzX2ZuKG1vZGVsKFgpLCB5KVxuICAgICAgICBsb3NzLmJhY2t3YXJkKClcblxuICAgICAgICAjIGNsaXBfZ3JhZF9ub3JtXyByZXR1cm5zIHByZS1jbGlwIG5vcm0gYW5kIGNsaXBzIGluLXBsYWNlXG4gICAgICAgIHByZV9jbGlwX25vcm0gPSBubi51dGlscy5jbGlwX2dyYWRfbm9ybV8obW9kZWwucGFyYW1ldGVycygpLCBjbGlwX3RocmVzaG9sZClcbiAgICAgICAgdHJhY2tlci51cGRhdGUocHJlX2NsaXBfbm9ybS5pdGVtKCksIGNsaXBfdGhyZXNob2xkKVxuXG4gICAgICAgIG9wdGltaXplci5zdGVwKClcblxuICAgICAgICBpZiBzdGVwICUgMjUgPT0gMDpcbiAgICAgICAgICAgIHByaW50KGZcIlN0ZXAge3N0ZXA6M2R9OiBsb3NzPXtsb3NzLml0ZW0oKTouNGZ9ICBcIlxuICAgICAgICAgICAgICAgICAgZlwiZ3JhZF9ub3JtPXtwcmVfY2xpcF9ub3JtLml0ZW0oKTouNGZ9ICBcIlxuICAgICAgICAgICAgICAgICAgZlwiY2xpcF9yYXRlPXt0cmFja2VyLmNsaXBfcmF0ZTouMSV9XCIpXG5cbiAgICByZXR1cm4gdHJhY2tlclxuXG50b3JjaC5tYW51YWxfc2VlZCg0Milcbm1vZGVsID0gbm4uU2VxdWVudGlhbChcbiAgICBubi5MaW5lYXIoOCwgMzIpLCBubi5SZUxVKCksXG4gICAgbm4uTGluZWFyKDMyLCAxNiksIG5uLlJlTFUoKSxcbiAgICBubi5MaW5lYXIoMTYsIDEpXG4pXG5YID0gdG9yY2gucmFuZG4oNjQsIDgpXG55ID0gdG9yY2gucmFuZG4oNjQsIDEpXG5cbnByaW50KFwiVHJhaW5pbmcgd2l0aCBnbG9iYWwgbm9ybSBjbGlwcGluZyAodGhyZXNob2xkPTEuMCk6XCIpXG50cmFja2VyID0gdHJhaW5fbG9vcChtb2RlbCwgWCwgeSwgY2xpcF90aHJlc2hvbGQ9MS4wLCBuX3N0ZXBzPTgwKVxucHJpbnQoZlwiXFxuT3ZlcmFsbCBjbGlwIHJhdGU6IHt0cmFja2VyLmNsaXBfcmF0ZTouMSV9XCIpXG5wcmludChmXCJSZWNlbnQgbm9ybSB3aW5kb3c6IG1lYW49e3N1bSh0cmFja2VyLndpbmRvdykvbGVuKHRyYWNrZXIud2luZG93KTouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgTm9ybSBNb25pdG9yaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcHJlLWNsaXBwaW5nIGdyYWRpZW50IG5vcm0gaXMgb25lIG9mIHRoZSBtb3N0IGluZm9ybWF0aXZlIHRyYWluaW5nIHNpZ25hbHMgYXZhaWxhYmxlLiBEdXJpbmcgYSBoZWFsdGh5IHRyYWluaW5nIHJ1biB0aGUgbm9ybSBzaG91bGQgYmUgcm91Z2hseSBzdGFibGUgKG9yIHNsb3dseSBkZWNyZWFzaW5nKS4gU3VkZGVuIHNwaWtlcyBpbmRpY2F0ZSBhIGJhZCBiYXRjaCwgbnVtZXJpY2FsIGluc3RhYmlsaXR5LCBvciBhIGxlYXJuaW5nIHJhdGUgdGhhdCBpcyB0b28gaGlnaC4gQSBwZXJzaXN0ZW50bHkgaGlnaCBjbGlwIHJhdGUgKFx1MDAzZTUwJSkgc3VnZ2VzdHMgdGhlIHRocmVzaG9sZCBpcyB0b28gbG93IG9yIHRoZSBsZWFybmluZyByYXRlIG5lZWRzIHJlZHVjaW5nLiBQZXItbGF5ZXIgbm9ybSB0cmFja2luZyByZXZlYWxzIHdoaWNoIGxheWVycyBhcmUgbW9zdCBhY3RpdmUg4oCUIHZlcnkgZGlmZmVyZW50IG5vcm1zIGFjcm9zcyBsYXllcnMgY2FuIGluZGljYXRlIGluaXRpYWxpemF0aW9uIGlzc3Vlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVmYXVsdGRpY3RcblxuZGVmIG1vbml0b3JfZ3JhZGllbnRfbm9ybXMobW9kZWwsIFgsIHksIG9wdGltaXplciwgY2xpcF90aHJlc2g9MS4wLCBuX3N0ZXBzPTYwKTpcbiAgICBcIlwiXCJUcmFjayBwZXItbGF5ZXIgYW5kIGdsb2JhbCBncmFkaWVudCBub3JtcyBhY3Jvc3MgdHJhaW5pbmcuXCJcIlwiXG4gICAgbG9zc19mbiA9IG5uLk1TRUxvc3MoKVxuICAgIGhpc3RvcnkgPSBkZWZhdWx0ZGljdChsaXN0KVxuXG4gICAgZm9yIHN0ZXAgaW4gcmFuZ2Uobl9zdGVwcyk6XG4gICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgICAgICBsb3NzID0gbG9zc19mbihtb2RlbChYKSwgeSlcbiAgICAgICAgbG9zcy5iYWNrd2FyZCgpXG5cbiAgICAgICAgIyBSZWNvcmQgcGVyLWxheWVyIG5vcm1zIGJlZm9yZSBjbGlwcGluZ1xuICAgICAgICBmb3IgbmFtZSwgcCBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCk6XG4gICAgICAgICAgICBpZiBwLmdyYWQgaXMgbm90IE5vbmU6XG4gICAgICAgICAgICAgICAgaGlzdG9yeVtuYW1lXS5hcHBlbmQocC5ncmFkLm5vcm0oKS5pdGVtKCkpXG5cbiAgICAgICAgZ2xvYmFsX25vcm0gPSBubi51dGlscy5jbGlwX2dyYWRfbm9ybV8obW9kZWwucGFyYW1ldGVycygpLCBjbGlwX3RocmVzaClcbiAgICAgICAgaGlzdG9yeVtcdTAwMjdfZ2xvYmFsXHUwMDI3XS5hcHBlbmQoZ2xvYmFsX25vcm0uaXRlbSgpKVxuICAgICAgICBvcHRpbWl6ZXIuc3RlcCgpXG5cbiAgICBwcmludChmXCJcXG5HcmFkaWVudCBOb3JtIFJlcG9ydCAoe25fc3RlcHN9IHN0ZXBzLCBjbGlwPXtjbGlwX3RocmVzaH0pXCIpXG4gICAgcHJpbnQoZlwie1x1MDAyN1BhcmFtZXRlclx1MDAyNzpcdTAwM2MyOH0ge1x1MDAyN01lYW5cdTAwMjc6XHUwMDNlOH0ge1x1MDAyN1N0ZFx1MDAyNzpcdTAwM2U4fSB7XHUwMDI3TWF4XHUwMDI3Olx1MDAzZTh9IHtcdTAwMjdDbGlwJVx1MDAyNzpcdTAwM2U3fVwiKVxuICAgIHByaW50KFwiLVwiICogNjIpXG4gICAgZm9yIG5hbWUsIHZhbHMgaW4gc29ydGVkKGhpc3RvcnkuaXRlbXMoKSk6XG4gICAgICAgIGFyciA9IG5wLmFycmF5KHZhbHMpXG4gICAgICAgIGNsaXBfcGN0ID0gMTAwKihhcnIgXHUwMDNlIGNsaXBfdGhyZXNoKS5tZWFuKCkgaWYgbmFtZSA9PSBcdTAwMjdfZ2xvYmFsXHUwMDI3IGVsc2UgMC4wXG4gICAgICAgIGxhYmVsID0gXHUwMDI3W0dMT0JBTF1cdTAwMjcgaWYgbmFtZSA9PSBcdTAwMjdfZ2xvYmFsXHUwMDI3IGVsc2UgbmFtZVxuICAgICAgICBwcmludChmXCJ7bGFiZWw6XHUwMDNjMjh9IHthcnIubWVhbigpOlx1MDAzZTguNGZ9IHthcnIuc3RkKCk6XHUwMDNlOC40Zn0ge2Fyci5tYXgoKTpcdTAwM2U4LjRmfSBcIlxuICAgICAgICAgICAgICBmXCJ7Y2xpcF9wY3Q6XHUwMDNlNi4xZn0lXCIpXG4gICAgcmV0dXJuIGhpc3RvcnlcblxudG9yY2gubWFudWFsX3NlZWQoMylcbm1vZGVsID0gbm4uU2VxdWVudGlhbChcbiAgICBubi5MaW5lYXIoOCwgMjQpLCBubi5SZUxVKCksXG4gICAgbm4uTGluZWFyKDI0LCAxMiksIG5uLlJlTFUoKSxcbiAgICBubi5MaW5lYXIoMTIsIDEpXG4pXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5TR0QobW9kZWwucGFyYW1ldGVycygpLCBscj0wLjA1LCBtb21lbnR1bT0wLjkpXG5YLCB5ID0gdG9yY2gucmFuZG4oOTYsIDgpLCB0b3JjaC5yYW5kbig5NiwgMSlcbmhpc3RvcnkgPSBtb25pdG9yX2dyYWRpZW50X25vcm1zKG1vZGVsLCBYLCB5LCBvcHRpbWl6ZXIsIG5fc3RlcHM9NTApXG5wcmludChcIlxcblNwaWtlcyBpbiBbR0xPQkFMXSBub3JtIGluZGljYXRlIHRyYWluaW5nIGluc3RhYmlsaXR5LlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkludGVyYWN0aW9uIHdpdGggT3RoZXIgVHJhaW5pbmcgVGVjaG5pcXVlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR3JhZGllbnQgY2xpcHBpbmcgaW50ZXJhY3RzIHdpdGggc2V2ZXJhbCBvdGhlciB0cmFpbmluZyBjb21wb25lbnRzIGluIHdheXMgdGhhdCByZXF1aXJlIGNhcmVmdWwgb3JkZXJpbmcuIFdpdGggZ3JhZGllbnQgYWNjdW11bGF0aW9uLCBiYWNrd2FyZCBpcyBjYWxsZWQgb24gbXVsdGlwbGUgbWljcm8tYmF0Y2hlcyBiZWZvcmUgc3RlcC4gQ2xpcHBpbmcgbXVzdCBoYXBwZW4gYWZ0ZXIgYWxsIG1pY3JvLWJhdGNoIGdyYWRpZW50cyBhcmUgYWNjdW11bGF0ZWQg4oCUIGNsaXBwaW5nIHBlciBtaWNyby1iYXRjaCBhbmQgdGhlbiBzdW1taW5nIGdpdmVzIGEgZGlmZmVyZW50IChpbmNvcnJlY3QpIGVmZmVjdGl2ZSB0aHJlc2hvbGQuIFdpdGggbWl4ZWQgcHJlY2lzaW9uIChBTVApLCB1bnNjYWxlIHRoZSBncmFkaWVudHMgZmlyc3QgKHNjYWxlci51bnNjYWxlXyhvcHRpbWl6ZXIpKSBiZWZvcmUgY2xpcHBpbmcsIHRoZW4gY2FsbCBzY2FsZXIuc3RlcChvcHRpbWl6ZXIpIOKAlCBQeVRvcmNoXHUwMDI3cyBHcmFkU2NhbGVyIGhhbmRsZXMgdGhpcyBhdXRvbWF0aWNhbGx5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiR3JhZGllbnQgYWNjdW11bGF0aW9uOiBjYWxsIGNsaXBfZ3JhZF9ub3JtXyBvbmNlIEFGVEVSIGFsbCBtaWNyby1iYXRjaCBiYWNrd2FyZCBwYXNzZXMsIG5vdCBwZXIgbWljcm8tYmF0Y2giLCJNaXhlZCBwcmVjaXNpb24gKEFNUCk6IHNjYWxlci51bnNjYWxlXyhvcHRpbWl6ZXIpIGJlZm9yZSBjbGlwX2dyYWRfbm9ybV8g4oCUIEdyYWRTY2FsZXIgZG9lcyB0aGlzIGlmIHVzZWQgY29ycmVjdGx5IiwiRGlzdHJpYnV0ZWQgdHJhaW5pbmc6IGdyYWRpZW50cyBhcmUgYWxyZWFkeSBhbGwtcmVkdWNlZCBhY3Jvc3MgZGV2aWNlcyBiZWZvcmUgY2xpcHBpbmcg4oCUIGNsaXAgb25jZSBvbiBlYWNoIHJlcGxpY2EiLCJHcmFkaWVudCBjaGVja3BvaW50aW5nOiBubyBpbnRlcmFjdGlvbiwgcmVjb21wdXRhdGlvbiBoYXBwZW5zIGluc2lkZSBiYWNrd2FyZCDigJQgY2xpcCBvbiBmaW5hbCBhY2N1bXVsYXRlZCBncmFkcyIsIk9wdGltaXplciBpbnRlcmFjdGlvbjogY2xpcCBiZWZvcmUgb3B0aW1pemVyLnN0ZXAoKSBhbHdheXM7IHNvbWUgb3B0aW1pemVycyAoQWRhR3JhZCwgQWRhbSkgbWFpbnRhaW4gc2Vjb25kIG1vbWVudHMgb2YgcmF3IChwcmUtY2xpcCkgZ3JhZGllbnRzIGludGVybmFsbHkiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2V0dGluZyB0aGUgQ2xpcHBpbmcgVGhyZXNob2xkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2xpcHBpbmcgdGhyZXNob2xkIGlzIGEgaHlwZXJwYXJhbWV0ZXIgdGhhdCBzaG91bGQgYmUgc2V0IGJ5IG1vbml0b3JpbmcgdGhlIGdyYWRpZW50IG5vcm0gaGlzdG9ncmFtIGR1cmluZyB0aGUgZmlyc3QgZmV3IGh1bmRyZWQgc3RlcHMgb2YgdHJhaW5pbmcgKGJlZm9yZSBhbnkgY2xpcHBpbmcpLiBBIGdvb2QgdGhyZXNob2xkIGlzIHJvdWdobHkgdGhlIDk1dGjigJM5OXRoIHBlcmNlbnRpbGUgb2YgdGhlIG5hdHVyYWwgZ3JhZGllbnQgbm9ybSBkaXN0cmlidXRpb24g4oCUIGhpZ2ggZW5vdWdoIHRoYXQgaXQgcmFyZWx5IGNsaXBzIGR1cmluZyBzdGFibGUgdHJhaW5pbmcgYnV0IGNhdGNoZXMgcGF0aG9sb2dpY2FsIHNwaWtlcy4gRm9yIHRyYW5zZm9ybWVyIGxhbmd1YWdlIG1vZGVscyB0aGUgY29tbXVuaXR5IGRlZmF1bHQgaXMgMS4wOyBmb3IgUk5OcyAxLjDigJM1LjA7IGZvciBDTk5zIGNsaXBwaW5nIGlzIG9mdGVuIG5vdCBuZWVkZWQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUcmFuc2Zvcm1lciBMTE1zOiB0aHJlc2hvbGQ9MS4wIGlzIHRoZSBuZWFyLXVuaXZlcnNhbCBkZWZhdWx0IChHUFQtMiwgR1BULTMsIExMYU1BIGFsbCB1c2UgMS4wKSIsIlJOTnMgLyBMU1RNczogdGhyZXNob2xkPTEuMOKAkzUuMCBkZXBlbmRpbmcgb24gc2VxdWVuY2UgbGVuZ3RoIGFuZCBoaWRkZW4gc2l6ZSIsIkNOTnM6IG9mdGVuIG5vIGNsaXBwaW5nIG5lZWRlZDsgZ3JhZGllbnRzIGFyZSB1c3VhbGx5IHdlbGwtYmVoYXZlZCB3aXRoIEJOIiwiTW9uaXRvciBjbGlwIHJhdGU6IGlmIFx1MDAzZTEwJSBvZiBzdGVwcyBjbGlwLCBjb25zaWRlciByZWR1Y2luZyBMUiBvciBpbmNyZWFzaW5nIHRocmVzaG9sZCIsIldhdGNoIGZvciBwZXJzaXN0ZW50IGhpZ2ggbm9ybXMgYXQgaW5pdGlhbGl6YXRpb246IG1heSBpbmRpY2F0ZSBiYWQgd2VpZ2h0IGluaXQgb3IgdmVyeSBoaWdoIExSIiwiTG9nIGdyYWRpZW50IG5vcm0gYXMgYSBXXHUwMDI2QiAvIFRlbnNvckJvYXJkIG1ldHJpYyDigJQgaXRcdTAwMjdzIG9uZSBvZiB0aGUgYmVzdCBlYXJseSB3YXJuaW5nIHNpZ25hbHMiXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Gradient Clipping — Norm and Value Clipping

Gradient clipping is a simple but essential training stabilization technique, especially for recurrent networks and large language models. Without it, occasional large gradients can cause weight updates that completely destabilize training — the 'exploding gradient' problem. Clipping bounds the influence of any single gradient signal while preserving the update direction, acting as an adaptive learning rate that scales down only when needed.

## Exploding Gradients in Deep Networks

During backpropagation through time (BPTT) in RNNs, the gradient flows through a chain of Jacobians: ∂L/∂h₀ = (∂h_T/∂h₀)ᵀ ∂L/∂h_T = (∏ₜ W_hh·diag(σ'(hₜ)))ᵀ ∂L/∂h_T. If the spectral radius ρ(W_hh) > 1, the product of Jacobians grows exponentially with sequence length T: ‖∏Jₜ‖ ≈ ρᵀ. For ρ=1.1 and T=100, the gradient amplification is 1.1¹⁰⁰ ≈ 10⁴. Deep feedforward networks face the same issue: each layer multiplies by a weight matrix, and if the singular values exceed 1 the product explodes.

> **BPTT and Exponential Gradient Growth**: The product of T Jacobians ∏ₜJₜ has norm that grows as ρ(J)ᵀ where ρ is the spectral radius. For ρ>1: exponential explosion. For ρ<1: exponential vanishing. The 1.0 boundary is unstable — typical RNNs initialized with ρ≈1 quickly drift. Gradient clipping handles the explosion side; gating mechanisms (LSTM, GRU) and careful initialization handle vanishing.

```python
import torch
import numpy as np

def rnn_step(h, x, W_hh, W_xh, b):
    """Single RNN step: h_t = tanh(W_hh @ h_{t-1} + W_xh @ x_t + b)."""
    return torch.tanh(W_hh @ h + W_xh @ x + b)

def track_bptt_gradient_norms(seq_len=80, hidden=16, spectral_radius=1.1, seed=0):
    torch.manual_seed(seed)
    # Initialize W_hh with given spectral radius
    W_raw = torch.randn(hidden, hidden)
    U, S, Vh = torch.linalg.svd(W_raw)
    W_hh = (U @ Vh) * spectral_radius  # spectral radius exactly = 1.1
    W_hh.requires_grad_(True)

    W_xh = torch.randn(hidden, 4) * 0.1
    b = torch.zeros(hidden)
    x_seq = torch.randn(seq_len, 4)

    print(f"BPTT gradient norms (hidden={hidden}, spectral radius={spectral_radius})")
    print(f"{'Time step':>10} {'||dL/dW_hh||':>16} {'Status':>12}")

    norms = []
    for t in range(seq_len):
        h = torch.zeros(hidden)
        for s in range(t + 1):
            h = rnn_step(h, x_seq[s], W_hh, W_xh, b)
        loss = h.sum()
        loss.backward()
        if W_hh.grad is not None and t % 15 == 0:
            gn = W_hh.grad.norm().item()
            norms.append((t, gn))
            status = "EXPLODING" if gn > 50 else ("warning" if gn > 5 else "stable")
            print(f"{t:>10} {gn:>16.2f} {status:>12}")
            W_hh.grad.zero_()
    return norms

norms = track_bptt_gradient_norms(seq_len=75, hidden=12, spectral_radius=1.08)
print("\nGradient grows exponentially with sequence length — clipping is essential.")
```

## Global Norm Clipping

Global norm clipping computes the norm across ALL parameters simultaneously: g_norm = √(Σᵢ‖∇θᵢ‖²). If g_norm exceeds the threshold c, every gradient is scaled by the same factor c/g_norm. This is the critical property: all gradients are scaled uniformly, so their relative magnitudes and thus the gradient direction is preserved. The optimizer takes a step in the same direction as the true gradient, just shorter.

1. Compute global gradient norm: g_norm = sqrt(sum over all params of ||grad_i||²)
2. If g_norm > threshold: scale = threshold / g_norm; else scale = 1.0
3. Apply: grad_i ← grad_i * scale for ALL parameter groups simultaneously
4. Pass scaled gradients to optimizer.step() — direction preserved, magnitude bounded

## Value Clipping and Why It Is Inferior

Value clipping clips each gradient component independently: gᵢ ← clip(gᵢ, −c, c). This is simpler but changes the gradient direction: if one parameter has a large gradient that gets clipped while others are small, the relative magnitudes are distorted. The resulting update points in a different direction than the true gradient. This can slow convergence and introduce systematic bias, particularly problematic for correlated parameters. Value clipping is sometimes used in DQN-style RL but is generally not recommended.

> **Why Direction Matters**: Gradient descent works because −∇f points in the steepest descent direction. Any positive scaling of the gradient still points downhill. But elementwise clipping creates a gradient that is no longer proportional to ∇f — some components are suppressed relative to others, effectively changing the preconditioning. The resulting update direction may not be a descent direction at all for non-separable objectives.

| Method | Formula | Direction Preserved | Recommended |
| --- | --- | --- | --- |
| Global Norm Clip | g ← g·min(1, c/‖g‖_global) | Yes — all params scaled uniformly | Yes — default for transformers, RNNs, LLMs |
| Value Clip | gᵢ ← clip(gᵢ, −c, c) per element | No — changes relative magnitudes | Rarely — some RL (DQN), not recommended for supervised |
| Per-layer Norm Clip | gₗ ← gₗ·min(1, c/‖gₗ‖) per layer l | Yes — within each layer | Sometimes — layer-sensitive architectures |

```python
import torch
import numpy as np

def global_norm_clip(grads, threshold):
    """Clip by global norm — preserves gradient direction."""
    global_norm = torch.sqrt(sum(g.norm()**2 for g in grads))
    if global_norm > threshold:
        scale = threshold / (global_norm + 1e-12)
        return [g * scale for g in grads], global_norm.item(), True
    return list(grads), global_norm.item(), False

def value_clip(grads, threshold):
    """Clip each element independently — changes gradient direction."""
    clipped = [torch.clamp(g, -threshold, threshold) for g in grads]
    orig_norm = torch.sqrt(sum(g.norm()**2 for g in grads)).item()
    clip_norm = torch.sqrt(sum(g.norm()**2 for g in clipped)).item()
    return clipped, orig_norm, clip_norm

torch.manual_seed(5)
grads = [torch.randn(4, 6) * 4.0, torch.randn(4) * 8.0]
threshold = 1.0

norm_g, g_norm, was_clipped = global_norm_clip(grads, threshold)
val_g, orig_norm, val_norm = value_clip(grads, threshold)

dir_orig = torch.cat([g.flatten() for g in grads]).float()
dir_norm = torch.cat([g.flatten() for g in norm_g]).float()
dir_val  = torch.cat([g.flatten() for g in val_g]).float()

cos_norm = torch.dot(dir_orig/dir_orig.norm(), dir_norm/dir_norm.norm()).item()
cos_val  = torch.dot(dir_orig/dir_orig.norm(), dir_val/dir_val.norm()).item()

print(f"Original global norm: {g_norm:.4f}")
print(f"\nGlobal Norm Clip (threshold={threshold}):")
print(f"  Result norm: {torch.sqrt(sum(g.norm()**2 for g in norm_g)).item():.4f}")
print(f"  Cosine similarity with original: {cos_norm:.6f} (1.0 = same direction)")
print(f"\nValue Clip (threshold={threshold}):")
print(f"  Result norm: {val_norm:.4f}")
print(f"  Cosine similarity with original: {cos_val:.4f}  <- direction changed!")
```

## PyTorch Implementation

torch.nn.utils.clip_grad_norm_ is the standard PyTorch function for global norm clipping. It returns the pre-clipping gradient norm, which is invaluable for monitoring training health. The function modifies gradients in-place before the optimizer step. It must be called AFTER loss.backward() and BEFORE optimizer.step(). When using gradient accumulation, clip after the full accumulation is complete — not after each micro-batch backward.

```python
import torch
import torch.nn as nn
from collections import deque

class GradNormTracker:
    def __init__(self, window=100):
        self.window = deque(maxlen=window)
        self.total = 0
        self.clipped = 0

    def update(self, norm, threshold):
        self.window.append(norm)
        self.total += 1
        if norm > threshold:
            self.clipped += 1

    @property
    def clip_rate(self):
        return self.clipped / max(self.total, 1)

def train_loop(model, X, y, clip_threshold=1.0, n_steps=100):
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    tracker = GradNormTracker()

    for step in range(n_steps):
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()

        # clip_grad_norm_ returns pre-clip norm and clips in-place
        pre_clip_norm = nn.utils.clip_grad_norm_(model.parameters(), clip_threshold)
        tracker.update(pre_clip_norm.item(), clip_threshold)

        optimizer.step()

        if step % 25 == 0:
            print(f"Step {step:3d}: loss={loss.item():.4f}  "
                  f"grad_norm={pre_clip_norm.item():.4f}  "
                  f"clip_rate={tracker.clip_rate:.1%}")

    return tracker

torch.manual_seed(42)
model = nn.Sequential(
    nn.Linear(8, 32), nn.ReLU(),
    nn.Linear(32, 16), nn.ReLU(),
    nn.Linear(16, 1)
)
X = torch.randn(64, 8)
y = torch.randn(64, 1)

print("Training with global norm clipping (threshold=1.0):")
tracker = train_loop(model, X, y, clip_threshold=1.0, n_steps=80)
print(f"\nOverall clip rate: {tracker.clip_rate:.1%}")
print(f"Recent norm window: mean={sum(tracker.window)/len(tracker.window):.4f}")
```

## Gradient Norm Monitoring

The pre-clipping gradient norm is one of the most informative training signals available. During a healthy training run the norm should be roughly stable (or slowly decreasing). Sudden spikes indicate a bad batch, numerical instability, or a learning rate that is too high. A persistently high clip rate (>50%) suggests the threshold is too low or the learning rate needs reducing. Per-layer norm tracking reveals which layers are most active — very different norms across layers can indicate initialization issues.

```python
import torch
import torch.nn as nn
import numpy as np
from collections import defaultdict

def monitor_gradient_norms(model, X, y, optimizer, clip_thresh=1.0, n_steps=60):
    """Track per-layer and global gradient norms across training."""
    loss_fn = nn.MSELoss()
    history = defaultdict(list)

    for step in range(n_steps):
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()

        # Record per-layer norms before clipping
        for name, p in model.named_parameters():
            if p.grad is not None:
                history[name].append(p.grad.norm().item())

        global_norm = nn.utils.clip_grad_norm_(model.parameters(), clip_thresh)
        history['_global'].append(global_norm.item())
        optimizer.step()

    print(f"\nGradient Norm Report ({n_steps} steps, clip={clip_thresh})")
    print(f"{'Parameter':<28} {'Mean':>8} {'Std':>8} {'Max':>8} {'Clip%':>7}")
    print("-" * 62)
    for name, vals in sorted(history.items()):
        arr = np.array(vals)
        clip_pct = 100*(arr > clip_thresh).mean() if name == '_global' else 0.0
        label = '[GLOBAL]' if name == '_global' else name
        print(f"{label:<28} {arr.mean():>8.4f} {arr.std():>8.4f} {arr.max():>8.4f} "
              f"{clip_pct:>6.1f}%")
    return history

torch.manual_seed(3)
model = nn.Sequential(
    nn.Linear(8, 24), nn.ReLU(),
    nn.Linear(24, 12), nn.ReLU(),
    nn.Linear(12, 1)
)
optimizer = torch.optim.SGD(model.parameters(), lr=0.05, momentum=0.9)
X, y = torch.randn(96, 8), torch.randn(96, 1)
history = monitor_gradient_norms(model, X, y, optimizer, n_steps=50)
print("\nSpikes in [GLOBAL] norm indicate training instability.")
```

## Interaction with Other Training Techniques

Gradient clipping interacts with several other training components in ways that require careful ordering. With gradient accumulation, backward is called on multiple micro-batches before step. Clipping must happen after all micro-batch gradients are accumulated — clipping per micro-batch and then summing gives a different (incorrect) effective threshold. With mixed precision (AMP), unscale the gradients first (scaler.unscale_(optimizer)) before clipping, then call scaler.step(optimizer) — PyTorch's GradScaler handles this automatically.

- Gradient accumulation: call clip_grad_norm_ once AFTER all micro-batch backward passes, not per micro-batch
- Mixed precision (AMP): scaler.unscale_(optimizer) before clip_grad_norm_ — GradScaler does this if used correctly
- Distributed training: gradients are already all-reduced across devices before clipping — clip once on each replica
- Gradient checkpointing: no interaction, recomputation happens inside backward — clip on final accumulated grads
- Optimizer interaction: clip before optimizer.step() always; some optimizers (AdaGrad, Adam) maintain second moments of raw (pre-clip) gradients internally

## Setting the Clipping Threshold

The clipping threshold is a hyperparameter that should be set by monitoring the gradient norm histogram during the first few hundred steps of training (before any clipping). A good threshold is roughly the 95th–99th percentile of the natural gradient norm distribution — high enough that it rarely clips during stable training but catches pathological spikes. For transformer language models the community default is 1.0; for RNNs 1.0–5.0; for CNNs clipping is often not needed.

- Transformer LLMs: threshold=1.0 is the near-universal default (GPT-2, GPT-3, LLaMA all use 1.0)
- RNNs / LSTMs: threshold=1.0–5.0 depending on sequence length and hidden size
- CNNs: often no clipping needed; gradients are usually well-behaved with BN
- Monitor clip rate: if >10% of steps clip, consider reducing LR or increasing threshold
- Watch for persistent high norms at initialization: may indicate bad weight init or very high LR
- Log gradient norm as a W&B / TensorBoard metric — it's one of the best early warning signals

---

