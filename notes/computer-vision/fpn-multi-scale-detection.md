---
title: "Feature Pyramid Networks for Multi-Scale Detection"
slug: "fpn-multi-scale-detection"
description: "FPN in detection — how P3–P7 levels handle small-to-large objects, lateral connections between backbone stages, and how RetinaNet and Faster R-CNN use FPN for scale-invariant detection."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGZWF0dXJlIFB5cmFtaWQgTmV0d29ya3MgKEZQTikgc29sdmUgYSBjb3JlIGNoYWxsZW5nZSBpbiBvYmplY3QgZGV0ZWN0aW9uOiBvYmplY3RzIGFwcGVhciBhdCB2YXN0bHkgZGlmZmVyZW50IHNjYWxlcy4gQSBzbWFsbCBwZWRlc3RyaWFuIG1pZ2h0IHNwYW4gMzLDlzMyIHBpeGVsczsgYSBuZWFyYnkgY2FyIG1pZ2h0IHNwYW4gNDAww5c0MDAuIFNpbmdsZS1zY2FsZSBkZXRlY3RvcnMgc3RydWdnbGUgd2l0aCB0aGlzIHJhbmdlLiBGUE4gYnVpbGRzIGEgbXVsdGktcmVzb2x1dGlvbiBweXJhbWlkIGZyb20gYSBzdGFuZGFyZCBiYWNrYm9uZSwgZ2l2aW5nIGRldGVjdG9ycyBzdHJvbmcgc2VtYW50aWMgZmVhdHVyZXMgYXQgZXZlcnkgc2NhbGUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZWZvcmUgRlBOLCBkZXRlY3RvcnMgZWl0aGVyIHJhbiBvbiBhIHNpbmdsZSBmZWF0dXJlIG1hcCAoZmFzdCBidXQgc2NhbGUtc2Vuc2l0aXZlKSBvciBvbiBhbiBpbWFnZSBweXJhbWlkIGF0IG11bHRpcGxlIHJlc29sdXRpb25zIChhY2N1cmF0ZSBidXQgc2xvdykuIEZQTiBhY2hpZXZlcyB0aGUgYmVzdCBvZiBib3RoOiBvbmUgZm9yd2FyZCBwYXNzIHRocm91Z2ggdGhlIGJhY2tib25lIHByb2R1Y2VzIGEgcmljaCBweXJhbWlkIG9mIGZlYXR1cmUgbWFwcyBhdCBtdWx0aXBsZSBzdHJpZGVzLCByZXVzaW5nIGNvbXB1dGF0aW9uIGVmZmljaWVudGx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZQTiBBcmNoaXRlY3R1cmUgZm9yIERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRlBOIGF0dGFjaGVzIHRvIGEgc3RhbmRhcmQgYmFja2JvbmUgKFJlc05ldCwgRWZmaWNpZW50TmV0KSBhbmQgZXh0cmFjdHMgZmVhdHVyZSBtYXBzIGF0IGZvdXIgb3IgZml2ZSBzdGFnZXMg4oCUIEMyIHRocm91Z2ggQzUg4oCUIHdoZXJlIGVhY2ggc3RhZ2UgaGFzIGhhbGYgdGhlIHNwYXRpYWwgcmVzb2x1dGlvbiBvZiB0aGUgcHJldmlvdXMuIFRoZXNlIGZvcm0gdGhlIGJvdHRvbS11cCBwYXRod2F5LiBGUE4gdGhlbiBidWlsZHMgYSB0b3AtZG93biBwYXRod2F5IHN0YXJ0aW5nIGZyb20gQzUsIHByb2dyZXNzaXZlbHkgdXBzYW1wbGluZyBhbmQgbWVyZ2luZyB3aXRoIHNoYWxsb3dlciwgaGlnaGVyLXJlc29sdXRpb24gZmVhdHVyZXMgdmlhIGxhdGVyYWwgY29ubmVjdGlvbnMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgb3V0cHV0IGlzIGZpdmUgcHlyYW1pZCBsZXZlbHMgUDPigJNQNyAoUDYgYW5kIFA3IGFyZSBvYnRhaW5lZCBieSBzdHJpZGVkIGNvbnZvbHV0aW9ucyBvbiBQNSkuIFAzIGhhcyBzdHJpZGUgOCBhbmQgY2FwdHVyZXMgZmluZSBzcGF0aWFsIGRldGFpbCBmb3Igc21hbGwgb2JqZWN0cy4gUDcgaGFzIHN0cmlkZSAxMjggYW5kIGNhcHR1cmVzIGNvYXJzZSBidXQgc2VtYW50aWNhbGx5IHJpY2ggZmVhdHVyZXMgZm9yIGxhcmdlIG9iamVjdHMuIEVhY2ggbGV2ZWwgb3V0cHV0cyAyNTYgY2hhbm5lbHMgYnkgY29udmVudGlvbiwgc2ltcGxpZnlpbmcgZG93bnN0cmVhbSBoZWFkcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgTGF0ZXJhbENvbm5lY3Rpb24obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2hhbm5lbHMsIG91dF9jaGFubmVscz0yNTYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5sYXRlcmFsX2NvbnYgPSBubi5Db252MmQoaW5fY2hhbm5lbHMsIG91dF9jaGFubmVscywgMSlcbiAgICAgICAgc2VsZi5vdXRwdXRfY29udiA9IG5uLkNvbnYyZChvdXRfY2hhbm5lbHMsIG91dF9jaGFubmVscywgMywgcGFkZGluZz0xKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgYm90dG9tX3VwLCB0b3BfZG93bik6XG4gICAgICAgIGxhdGVyYWwgPSBzZWxmLmxhdGVyYWxfY29udihib3R0b21fdXApXG4gICAgICAgIHVwc2FtcGxlZCA9IEYuaW50ZXJwb2xhdGUodG9wX2Rvd24sIHNpemU9bGF0ZXJhbC5zaGFwZVstMjpdLCBtb2RlPVx1MDAyN25lYXJlc3RcdTAwMjcpXG4gICAgICAgIG1lcmdlZCA9IGxhdGVyYWwgKyB1cHNhbXBsZWRcbiAgICAgICAgcmV0dXJuIHNlbGYub3V0cHV0X2NvbnYobWVyZ2VkKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxhdGVyYWwgQ29ubmVjdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsYXRlcmFsIGNvbm5lY3Rpb24gaXMgRlBOXHUwMDI3cyBrZXkgYnVpbGRpbmcgYmxvY2suIEF0IGVhY2ggbGV2ZWwsIGEgMcOXMSBjb252IHJlZHVjZXMgdGhlIGJvdHRvbS11cCBmZWF0dXJlIG1hcCB0byAyNTYgY2hhbm5lbHMuIFRoZSB0b3AtZG93biBtYXAgKGZyb20gdGhlIGxldmVsIGFib3ZlKSBpcyB1cHNhbXBsZWQgMsOXIHVzaW5nIG5lYXJlc3QtbmVpZ2hib3IgaW50ZXJwb2xhdGlvbiBhbmQgYWRkZWQgZWxlbWVudC13aXNlLiBBIGZpbmFsIDPDlzMgY29udiBzbW9vdGhzIGFsaWFzaW5nIGFydGlmYWN0cy4gVGhpcyBtZXJnaW5nIGVuc3VyZXMgdGhhdCBldmVyeSBsZXZlbCBjYXJyaWVzIGJvdGggc2VtYW50aWMgcmljaG5lc3MgKGZyb20gZGVwdGgpIGFuZCBzcGF0aWFsIHByZWNpc2lvbiAoZnJvbSByZXNvbHV0aW9uKS4ifSx7InR5cGUiOiJjYWxsb3V0IiwiY2FsbG91dF90eXBlIjoiaW5mbyIsImNvbnRlbnQiOiJGUE5cdTAwMjdzIGtleSBjb250cmlidXRpb246IHN0cm9uZyBzZW1hbnRpYyBmZWF0dXJlcyAoZnJvbSBkZWVwIGxheWVycykgYXQgaGlnaCByZXNvbHV0aW9uICh2aWEgdXBzYW1wbGluZykg4oCUIHdpdGhvdXQgRlBOLCBzaGFsbG93IGZlYXR1cmVzIGxhY2sgc2VtYW50aWNzIGFuZCBkZWVwIGZlYXR1cmVzIGxhY2sgcmVzb2x1dGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsZSBBc3NpZ25tZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaXRoIG11bHRpcGxlIEZQTiBsZXZlbHMgYXZhaWxhYmxlLCBkZXRlY3RvcnMgbXVzdCBhc3NpZ24gZWFjaCBncm91bmQtdHJ1dGggb2JqZWN0IHRvIGV4YWN0bHkgb25lIGxldmVsIGZvciB0cmFpbmluZy4gVGhlIGFzc2lnbm1lbnQgaXMgYmFzZWQgb24gb2JqZWN0IHNpemUuIFNtYWxsIG9iamVjdHMgKGUuZy4sIDMyw5czMiBwaXhlbHMpIGdvIHRvIFAzLCB3aGlsZSBsYXJnZSBvYmplY3RzIChlLmcuLCA1MTLDlzUxMiBwaXhlbHMpIGdvIHRvIFA3LiBUaGUgZm9ybXVsYSB1c2VzIGxvZzIgb2YgdGhlIG9iamVjdFx1MDAyN3Mgc2l6ZSByZWxhdGl2ZSB0byBhIGNhbm9uaWNhbCBzaXplIG9mIDIyNCBwaXhlbHMsIGdpdmluZyBhIGNvbnRpbnVvdXMgbWFwcGluZyB0aGF0IGlzIHRoZW4gY2xpcHBlZCB0byB2YWxpZCBsZXZlbCBpbmRpY2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbWF0aFxuXG5kZWYgYXNzaWduX2xldmVsKHcsIGgsIGswPTQsIGtfbWluPTMsIGtfbWF4PTUpOlxuICAgIFwiXCJcIlxuICAgIEFzc2lnbiBncm91bmQtdHJ1dGggYm94IG9mIHNpemUgKHcsIGgpIHRvIGFuIEZQTiBsZXZlbC5cbiAgICBrMD00IG1lYW5zIGEgMjI0eDIyNCBvYmplY3QgbWFwcyB0byBQNC5cbiAgICBcIlwiXCJcbiAgICBhcmVhID0gdyAqIGhcbiAgICBrID0gazAgKyBtYXRoLmxvZzIobWF0aC5zcXJ0KGFyZWEpIC8gMjI0LjApXG4gICAgayA9IGludChtYXRoLmZsb29yKGspKVxuICAgIGsgPSBtYXgoa19taW4sIG1pbihrX21heCwgaykpXG4gICAgcmV0dXJuIGtcblxuIyBTbWFsbCBvYmplY3Q6IDMyeDMyIC1cdTAwM2UgUDMsIExhcmdlOiA0NDh4NDQ4IC1cdTAwM2UgUDVcbnByaW50KGFzc2lnbl9sZXZlbCgzMiwgMzIpKSAgICMgLVx1MDAzZSAzXG5wcmludChhc3NpZ25fbGV2ZWwoMjI0LCAyMjQpKSAjIC1cdTAwM2UgNFxucHJpbnQoYXNzaWduX2xldmVsKDQ0OCwgNDQ4KSkgIyAtXHUwMDNlIDUifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRlBOIExldmVsIiwiU3RyaWRlIiwiQW5jaG9yIFNpemUgUmFuZ2UiLCJPYmplY3QgU2l6ZSBSYW5nZSIsIkJlc3QgTWF0Y2giXSwicm93cyI6W1siUDMiLCI4IiwiMTbigJM0OCBweCIsIlx1MDAzYyA2NCBweCIsIlNtYWxsIG9iamVjdHMgKHBlZGVzdHJpYW5zLCB0ZXh0KSJdLFsiUDQiLCIxNiIsIjQ44oCTOTYgcHgiLCI2NOKAkzEyOCBweCIsIk1lZGl1bSBvYmplY3RzIChjYXJzIGF0IGRpc3RhbmNlKSJdLFsiUDUiLCIzMiIsIjk24oCTMTkyIHB4IiwiMTI44oCTMjU2IHB4IiwiTWVkaXVtLWxhcmdlIG9iamVjdHMiXSxbIlA2IiwiNjQiLCIxOTLigJMzODQgcHgiLCIyNTbigJM1MTIgcHgiLCJMYXJnZSBvYmplY3RzIl0sWyJQNyIsIjEyOCIsIjM4NOKAkzc2OCBweCIsIlx1MDAzZSA1MTIgcHgiLCJWZXJ5IGxhcmdlIG9iamVjdHMgKHRydWNrcywgYnVzZXMpIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXRpbmFOZXQgd2l0aCBGUE4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJldGluYU5ldCBpcyB0aGUgY2Fub25pY2FsIEZQTi1iYXNlZCBkZXRlY3Rvci4gSXQgYXR0YWNoZXMgaWRlbnRpY2FsIGNsYXNzaWZpY2F0aW9uIGFuZCBib3ggcmVncmVzc2lvbiBoZWFkcyB0byBldmVyeSBGUE4gbGV2ZWwgKFAz4oCTUDcpLiBFYWNoIGhlYWQgaXMgYSBzdGFjayBvZiBmb3VyIDPDlzMgY29udm9sdXRpb25zIHdpdGggUmVMVSwgZm9sbG93ZWQgYnkgYSBmaW5hbCBwcmVkaWN0aW9uIGNvbnYuIEJlY2F1c2UgdGhlIHNhbWUgaGVhZCB3ZWlnaHRzIGFyZSBzaGFyZWQgYWNyb3NzIGxldmVscywgdGhlIG5ldHdvcmsgaXMgZm9yY2VkIHRvIGxlYXJuIHNjYWxlLWludmFyaWFudCBmZWF0dXJlcyDigJQgdGhlIEZQTiBsZXZlbHMgaGFuZGxlIHNjYWxlIHZhcmlhdGlvbiwgbm90IHRoZSBoZWFkcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJldGluYU5ldCBhbHNvIGludHJvZHVjZWQgRm9jYWwgTG9zcyB0byBhZGRyZXNzIHRoZSBleHRyZW1lIGZvcmVncm91bmQtYmFja2dyb3VuZCBpbWJhbGFuY2UgaW5oZXJlbnQgaW4gZGVuc2Ugc2luZ2xlLXN0YWdlIGRldGVjdGlvbi4gV2l0aCBGUE4gcHJvdmlkaW5nIG11bHRpLXNjYWxlIGFuY2hvcnMgYW5kIEZvY2FsIExvc3MgaGFuZGxpbmcgY2xhc3MgaW1iYWxhbmNlLCBSZXRpbmFOZXQgYWNoaWV2ZWQgc3RhdGUtb2YtdGhlLWFydCBhY2N1cmFjeSBhbW9uZyBzaW5nbGUtc3RhZ2UgZGV0ZWN0b3JzIGF0IHRoZSB0aW1lIG9mIGl0cyBpbnRyb2R1Y3Rpb24sIG1hdGNoaW5nIG9yIGV4Y2VlZGluZyB0d28tc3RhZ2UgRmFzdGVyIFItQ05OIHZhcmlhbnRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgUmV0aW5hTmV0SGVhZChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaGFubmVscz0yNTYsIG51bV9hbmNob3JzPTksIG51bV9jbGFzc2VzPTgwKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGNsc19sYXllcnMsIHJlZ19sYXllcnMgPSBbXSwgW11cbiAgICAgICAgZm9yIF8gaW4gcmFuZ2UoNCk6XG4gICAgICAgICAgICBjbHNfbGF5ZXJzICs9IFtubi5Db252MmQoaW5fY2hhbm5lbHMsIGluX2NoYW5uZWxzLCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKCldXG4gICAgICAgICAgICByZWdfbGF5ZXJzICs9IFtubi5Db252MmQoaW5fY2hhbm5lbHMsIGluX2NoYW5uZWxzLCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKCldXG4gICAgICAgIHNlbGYuY2xzX2hlYWQgPSBubi5TZXF1ZW50aWFsKCpjbHNfbGF5ZXJzLFxuICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoYW5uZWxzLCBudW1fYW5jaG9ycyAqIG51bV9jbGFzc2VzLCAzLCBwYWRkaW5nPTEpKVxuICAgICAgICBzZWxmLnJlZ19oZWFkID0gbm4uU2VxdWVudGlhbCgqcmVnX2xheWVycyxcbiAgICAgICAgICAgIG5uLkNvbnYyZChpbl9jaGFubmVscywgbnVtX2FuY2hvcnMgKiA0LCAzLCBwYWRkaW5nPTEpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgZnBuX2xldmVscyk6XG4gICAgICAgIHJldHVybiBbKHNlbGYuY2xzX2hlYWQocCksIHNlbGYucmVnX2hlYWQocCkpIGZvciBwIGluIGZwbl9sZXZlbHNdIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdCBpbmZlcmVuY2UsIFJldGluYU5ldCBhcHBsaWVzIHRoZSBoZWFkIHRvIGFsbCBmaXZlIEZQTiBsZXZlbHMgc2ltdWx0YW5lb3VzbHkuIEVhY2ggbGV2ZWwgcHJvZHVjZXMgYSBkZW5zZSBncmlkIG9mIGFuY2hvciBwcmVkaWN0aW9ucy4gQWZ0ZXIgc2lnbW9pZCBhY3RpdmF0aW9uIG9uIGNsYXNzIHNjb3JlcywgcHJlZGljdGlvbnMgYWNyb3NzIGFsbCBsZXZlbHMgYXJlIGNvbmNhdGVuYXRlZCBhbmQgZmlsdGVyZWQgdXNpbmcgYSBzY29yZSB0aHJlc2hvbGQsIHRoZW4gTm9uLU1heGltdW0gU3VwcHJlc3Npb24gKE5NUykgaXMgYXBwbGllZCB0byByZW1vdmUgZHVwbGljYXRlIGRldGVjdGlvbnMuIFRoZSB0b3RhbCBudW1iZXIgb2YgYW5jaG9ycyBpcyB0eXBpY2FsbHkgMTAwa+KAkzIwMGsgcGVyIGltYWdlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2h2aXNpb25cbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmltcG9ydCBtYXRwbG90bGliLnBhdGNoZXMgYXMgcGF0Y2hlc1xuXG4jIExvYWQgYSBwcmV0cmFpbmVkIFJldGluYU5ldCB3aXRoIEZQTiBiYWNrYm9uZVxubW9kZWwgPSB0b3JjaHZpc2lvbi5tb2RlbHMuZGV0ZWN0aW9uLnJldGluYW5ldF9yZXNuZXQ1MF9mcG4ocHJldHJhaW5lZD1UcnVlKVxubW9kZWwuZXZhbCgpXG5cbmRlZiB2aXN1YWxpemVfZnBuX2RldGVjdGlvbnMoaW1hZ2VfdGVuc29yLCBwcmVkaWN0aW9ucywgbGV2ZWxfY29sb3JzKTpcbiAgICBmaWcsIGF4ID0gcGx0LnN1YnBsb3RzKDEsIGZpZ3NpemU9KDEyLCA4KSlcbiAgICBheC5pbXNob3coaW1hZ2VfdGVuc29yLnBlcm11dGUoMSwgMiwgMCkpXG4gICAgZm9yIGJveCwgc2NvcmUsIGxldmVsIGluIHppcChwcmVkaWN0aW9uc1tcdTAwMjdib3hlc1x1MDAyN10sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJlZGljdGlvbnNbXHUwMDI3c2NvcmVzXHUwMDI3XSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmVkaWN0aW9ucy5nZXQoXHUwMDI3bGV2ZWxzXHUwMDI3LCBbXSkpOlxuICAgICAgICB4MSwgeTEsIHgyLCB5MiA9IGJveC50b2xpc3QoKVxuICAgICAgICBjb2xvciA9IGxldmVsX2NvbG9ycy5nZXQobGV2ZWwsIFx1MDAyN3doaXRlXHUwMDI3KVxuICAgICAgICByZWN0ID0gcGF0Y2hlcy5SZWN0YW5nbGUoKHgxLHkxKSwgeDIteDEsIHkyLXkxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaW5ld2lkdGg9MS41LCBlZGdlY29sb3I9Y29sb3IsIGZhY2Vjb2xvcj1cdTAwMjdub25lXHUwMDI3KVxuICAgICAgICBheC5hZGRfcGF0Y2gocmVjdClcbiAgICBwbHQuc2hvdygpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRlBOIGlzIG5vdyBhIHN0YW5kYXJkIGNvbXBvbmVudCBpbiBuZWFybHkgZXZlcnkgaGlnaC1wZXJmb3JtYW5jZSBkZXRlY3Rvci4gSXRzIGNvcmUgaW5zaWdodCDigJQgY29tYmluZSB0b3AtZG93biBzZW1hbnRpY3Mgd2l0aCBib3R0b20tdXAgcmVzb2x1dGlvbiDigJQgYXBwbGllcyBiZXlvbmQgYm91bmRpbmcgYm94ZXMgdG8gaW5zdGFuY2Ugc2VnbWVudGF0aW9uIChNYXNrIFItQ05OKSwga2V5cG9pbnQgZGV0ZWN0aW9uLCBhbmQgcGFub3B0aWMgc2VnbWVudGF0aW9uLiBVbmRlcnN0YW5kaW5nIEZQTiBpcyBwcmVyZXF1aXNpdGUga25vd2xlZGdlIGZvciByZWFkaW5nIHBhcGVycyBvbiBFZmZpY2llbnREZXQsIFlPTE9GLCBOQVNGUE4sIGFuZCBCaUZQTiwgYWxsIG9mIHdoaWNoIGJ1aWxkIG9uIG9yIG1vZGlmeSB0aGUgRlBOIGRlc2lnbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IktleSBwcmluY2lwbGVzIHRvIHJlbWVtYmVyOiAoMSkgbGF0ZXJhbCAxw5cxIGNvbnZzIHVuaWZ5IGNoYW5uZWwgZGltZW5zaW9ucywgKDIpIG5lYXJlc3QtbmVpZ2hib3IgdXBzYW1wbGUgYXZvaWRzIGxlYXJuZWQgdXBzYW1wbGluZyBhcnRpZmFjdHMsICgzKSBhIDPDlzMgY29udiBhZnRlciBtZXJnaW5nIGFsaWFzZXMgdGhlIHVwc2FtcGxlZCBtYXAsICg0KSBhbGwgbGV2ZWxzIG91dHB1dCAyNTYgY2hhbm5lbHMsIGFuZCAoNSkgbGV2ZWwgYXNzaWdubWVudCBkdXJpbmcgdHJhaW5pbmcgaXMgcnVsZS1iYXNlZCAobG9nMiBmb3JtdWxhKSByYXRoZXIgdGhhbiBsZWFybmVkLiBUaGVzZSBkZXNpZ24gY2hvaWNlcyBhcmUgc2ltcGxlIGJ1dCBlZmZlY3RpdmUgYWNyb3NzIGEgd2lkZSByYW5nZSBvZiBiYWNrYm9uZXMgYW5kIHRhc2tzLiJ9XQ=="
---
# Feature Pyramid Networks for Multi-Scale Detection

## Overview

Feature Pyramid Networks (FPN) solve a core challenge in object detection: objects appear at vastly different scales. A small pedestrian might span 32×32 pixels; a nearby car might span 400×400. Single-scale detectors struggle with this range. FPN builds a multi-resolution pyramid from a standard backbone, giving detectors strong semantic features at every scale.

Before FPN, detectors either ran on a single feature map (fast but scale-sensitive) or on an image pyramid at multiple resolutions (accurate but slow). FPN achieves the best of both: one forward pass through the backbone produces a rich pyramid of feature maps at multiple strides, reusing computation efficiently.

## FPN Architecture for Detection

FPN attaches to a standard backbone (ResNet, EfficientNet) and extracts feature maps at four or five stages — C2 through C5 — where each stage has half the spatial resolution of the previous. These form the bottom-up pathway. FPN then builds a top-down pathway starting from C5, progressively upsampling and merging with shallower, higher-resolution features via lateral connections.

The output is five pyramid levels P3–P7 (P6 and P7 are obtained by strided convolutions on P5). P3 has stride 8 and captures fine spatial detail for small objects. P7 has stride 128 and captures coarse but semantically rich features for large objects. Each level outputs 256 channels by convention, simplifying downstream heads.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LateralConnection(nn.Module):
    def __init__(self, in_channels, out_channels=256):
        super().__init__()
        self.lateral_conv = nn.Conv2d(in_channels, out_channels, 1)
        self.output_conv = nn.Conv2d(out_channels, out_channels, 3, padding=1)

    def forward(self, bottom_up, top_down):
        lateral = self.lateral_conv(bottom_up)
        upsampled = F.interpolate(top_down, size=lateral.shape[-2:], mode='nearest')
        merged = lateral + upsampled
        return self.output_conv(merged)
```

## Lateral Connections

The lateral connection is FPN's key building block. At each level, a 1×1 conv reduces the bottom-up feature map to 256 channels. The top-down map (from the level above) is upsampled 2× using nearest-neighbor interpolation and added element-wise. A final 3×3 conv smooths aliasing artifacts. This merging ensures that every level carries both semantic richness (from depth) and spatial precision (from resolution).

> ****: FPN's key contribution: strong semantic features (from deep layers) at high resolution (via upsampling) — without FPN, shallow features lack semantics and deep features lack resolution.

## Scale Assignment

With multiple FPN levels available, detectors must assign each ground-truth object to exactly one level for training. The assignment is based on object size. Small objects (e.g., 32×32 pixels) go to P3, while large objects (e.g., 512×512 pixels) go to P7. The formula uses log2 of the object's size relative to a canonical size of 224 pixels, giving a continuous mapping that is then clipped to valid level indices.

```python
import math

def assign_level(w, h, k0=4, k_min=3, k_max=5):
    """
    Assign ground-truth box of size (w, h) to an FPN level.
    k0=4 means a 224x224 object maps to P4.
    """
    area = w * h
    k = k0 + math.log2(math.sqrt(area) / 224.0)
    k = int(math.floor(k))
    k = max(k_min, min(k_max, k))
    return k

# Small object: 32x32 -> P3, Large: 448x448 -> P5
print(assign_level(32, 32))   # -> 3
print(assign_level(224, 224)) # -> 4
print(assign_level(448, 448)) # -> 5
```

| FPN Level | Stride | Anchor Size Range | Object Size Range | Best Match |
| --- | --- | --- | --- | --- |
| P3 | 8 | 16–48 px | < 64 px | Small objects (pedestrians, text) |
| P4 | 16 | 48–96 px | 64–128 px | Medium objects (cars at distance) |
| P5 | 32 | 96–192 px | 128–256 px | Medium-large objects |
| P6 | 64 | 192–384 px | 256–512 px | Large objects |
| P7 | 128 | 384–768 px | > 512 px | Very large objects (trucks, buses) |

## RetinaNet with FPN

RetinaNet is the canonical FPN-based detector. It attaches identical classification and box regression heads to every FPN level (P3–P7). Each head is a stack of four 3×3 convolutions with ReLU, followed by a final prediction conv. Because the same head weights are shared across levels, the network is forced to learn scale-invariant features — the FPN levels handle scale variation, not the heads.

RetinaNet also introduced Focal Loss to address the extreme foreground-background imbalance inherent in dense single-stage detection. With FPN providing multi-scale anchors and Focal Loss handling class imbalance, RetinaNet achieved state-of-the-art accuracy among single-stage detectors at the time of its introduction, matching or exceeding two-stage Faster R-CNN variants.

```python
import torch.nn as nn

class RetinaNetHead(nn.Module):
    def __init__(self, in_channels=256, num_anchors=9, num_classes=80):
        super().__init__()
        cls_layers, reg_layers = [], []
        for _ in range(4):
            cls_layers += [nn.Conv2d(in_channels, in_channels, 3, padding=1), nn.ReLU()]
            reg_layers += [nn.Conv2d(in_channels, in_channels, 3, padding=1), nn.ReLU()]
        self.cls_head = nn.Sequential(*cls_layers,
            nn.Conv2d(in_channels, num_anchors * num_classes, 3, padding=1))
        self.reg_head = nn.Sequential(*reg_layers,
            nn.Conv2d(in_channels, num_anchors * 4, 3, padding=1))

    def forward(self, fpn_levels):
        return [(self.cls_head(p), self.reg_head(p)) for p in fpn_levels]
```

At inference, RetinaNet applies the head to all five FPN levels simultaneously. Each level produces a dense grid of anchor predictions. After sigmoid activation on class scores, predictions across all levels are concatenated and filtered using a score threshold, then Non-Maximum Suppression (NMS) is applied to remove duplicate detections. The total number of anchors is typically 100k–200k per image.

```python
import torchvision
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load a pretrained RetinaNet with FPN backbone
model = torchvision.models.detection.retinanet_resnet50_fpn(pretrained=True)
model.eval()

def visualize_fpn_detections(image_tensor, predictions, level_colors):
    fig, ax = plt.subplots(1, figsize=(12, 8))
    ax.imshow(image_tensor.permute(1, 2, 0))
    for box, score, level in zip(predictions['boxes'],
                                  predictions['scores'],
                                  predictions.get('levels', [])):
        x1, y1, x2, y2 = box.tolist()
        color = level_colors.get(level, 'white')
        rect = patches.Rectangle((x1,y1), x2-x1, y2-y1,
                                   linewidth=1.5, edgecolor=color, facecolor='none')
        ax.add_patch(rect)
    plt.show()
```

## Key Takeaways

FPN is now a standard component in nearly every high-performance detector. Its core insight — combine top-down semantics with bottom-up resolution — applies beyond bounding boxes to instance segmentation (Mask R-CNN), keypoint detection, and panoptic segmentation. Understanding FPN is prerequisite knowledge for reading papers on EfficientDet, YOLOF, NASFPN, and BiFPN, all of which build on or modify the FPN design.

Key principles to remember: (1) lateral 1×1 convs unify channel dimensions, (2) nearest-neighbor upsample avoids learned upsampling artifacts, (3) a 3×3 conv after merging aliases the upsampled map, (4) all levels output 256 channels, and (5) level assignment during training is rule-based (log2 formula) rather than learned. These design choices are simple but effective across a wide range of backbones and tasks.

