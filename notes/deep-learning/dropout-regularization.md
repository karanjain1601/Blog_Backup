---
title: "Dropout — Inverted Dropout, Variational, and Structured"
slug: "dropout-regularization"
description: "Implement inverted dropout from scratch, apply MC-Dropout for uncertainty estimation, implement DropBlock for CNNs, and use variational dropout for consistent RNN regularization."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRHJvcG91dCAoU3JpdmFzdGF2YSBldCBhbC4gMjAxNCkgcmFuZG9tbHkgc2V0cyBhY3RpdmF0aW9ucyB0byB6ZXJvIHdpdGggcHJvYmFiaWxpdHkgcCBkdXJpbmcgdHJhaW5pbmcsIHByZXZlbnRpbmcgbmV1cm9ucyBmcm9tIGNvLWFkYXB0aW5nIGFuZCBhY3RpbmcgYXMgYW4gaW1wbGljaXQgZW5zZW1ibGUgb2YgMuKBvyBzdWItbmV0d29ya3MgKHdoZXJlIG4gaXMgdGhlIG51bWJlciBvZiB1bml0cykuIEVhY2ggZm9yd2FyZCBwYXNzIHNhbXBsZXMgYSBkaWZmZXJlbnQgYmluYXJ5IG1hc2ssIHRyYWluaW5nIGEgZGlmZmVyZW50IHRoaW5uZWQgbmV0d29yay4gQXQgdGVzdCB0aW1lLCBhbGwgbmV1cm9ucyBhcmUgdXNlZCBhbmQgb3V0cHV0cyBhcmUgc2NhbGVkIHRvIG1hdGNoIHRoZSBleHBlY3RlZCB2YWx1ZSBkdXJpbmcgdHJhaW5pbmcuIFRoaXMgZW5zZW1ibGUgaW50ZXJwcmV0YXRpb24gZXhwbGFpbnMgd2h5IGRyb3BvdXQgaW1wcm92ZXMgZ2VuZXJhbGl6YXRpb246IGl0IHByZXZlbnRzIGFueSBzaW5nbGUgbmV1cm9uIGZyb20gYmVpbmcgZXNzZW50aWFsIGZvciBhIHByZWRpY3Rpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RhbmRhcmQgRHJvcG91dCBhbmQgSW52ZXJ0ZWQgRHJvcG91dCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHdvIGVxdWl2YWxlbnQgZm9ybXVsYXRpb25zIGV4aXN0LiBTdGFuZGFyZCBkcm9wb3V0OiB6ZXJvIG91dCB3aXRoIHByb2JhYmlsaXR5IHAsIHNjYWxlIGJ5IDEvKDEtcCkgYXQgdGVzdCB0aW1lLiBJbnZlcnRlZCBkcm9wb3V0ICh0aGUgbW9kZXJuIGRlZmF1bHQgaW4gUHlUb3JjaCBhbmQgVGVuc29yRmxvdyk6IHNjYWxlIGtlcHQgYWN0aXZhdGlvbnMgYnkgMS8oMS1wKSBkdXJpbmcgdHJhaW5pbmcsIG5vIHNjYWxpbmcgYXQgdGVzdCB0aW1lLiBJbnZlcnRlZCBkcm9wb3V0IGlzIHByZWZlcnJlZCBiZWNhdXNlIHRoZSB0ZXN0LXRpbWUgbmV0d29yayBpcyBhIHNpbXBsZSBmZWVkLWZvcndhcmQgcGFzcyB3aXRoIG5vIG1vZGlmaWNhdGlvbiDigJQgbW9kZWwuZXZhbCgpIGF1dG9tYXRpY2FsbHkgZGlzYWJsZXMgZHJvcG91dCB3aXRob3V0IHJlcXVpcmluZyBhbnkgd2VpZ2h0IHJlc2NhbGluZy4gUHlUb3JjaFx1MDAyN3Mgbm4uRHJvcG91dCB1c2VzIGludmVydGVkIGRyb3BvdXQgaW50ZXJuYWxseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgaW52ZXJ0ZWRfZHJvcG91dCh4LCBwLCB0cmFpbmluZz1UcnVlKTpcbiAgICBpZiBub3QgdHJhaW5pbmcgb3IgcCA9PSAwLjA6XG4gICAgICAgIHJldHVybiB4XG4gICAgIyBTYW1wbGUgYmluYXJ5IG1hc2s6IGtlZXAgZWFjaCB1bml0IHdpdGggcHJvYmFiaWxpdHkgKDEtcClcbiAgICBtYXNrID0gKG5wLnJhbmRvbS5yYW5kKCp4LnNoYXBlKSBcdTAwM2UgcCkuYXN0eXBlKG5wLmZsb2F0MzIpXG4gICAgIyBTY2FsZSBieSAxLygxLXApIHNvIGV4cGVjdGVkIHZhbHVlIG1hdGNoZXMgeFxuICAgIHJldHVybiB4ICogbWFzayAvICgxLjAgLSBwKVxuXG5ucC5yYW5kb20uc2VlZCg0MilcbnggPSBucC5vbmVzKCg0LCA4KSkgICMgYWxsLW9uZXMgdG8gc2VlIHNjYWxpbmcgY2xlYXJseVxucCA9IDAuNVxuXG4jIFRyYWluaW5nIG1vZGU6IHNvbWUgdW5pdHMgemVyb2VkLCBzdXJ2aXZvcnMgc2NhbGVkIHVwXG5vdXRfdHJhaW4gPSBpbnZlcnRlZF9kcm9wb3V0KHgsIHAsIHRyYWluaW5nPVRydWUpXG5wcmludChmXHUwMDI3VHJhaW46IG1lYW49e291dF90cmFpbi5tZWFuKCk6LjNmfSAoc2hvdWxkIH4xLjApLCB6ZXJvcz17KCBvdXRfdHJhaW49PTApLnN1bSgpfVx1MDAyNylcblxuIyBFdmFsIG1vZGU6IGFsbCB1bml0cyBhY3RpdmUsIG5vIHNjYWxpbmcgbmVlZGVkXG5vdXRfZXZhbCA9IGludmVydGVkX2Ryb3BvdXQoeCwgcCwgdHJhaW5pbmc9RmFsc2UpXG5wcmludChmXHUwMDI3RXZhbDogIG1lYW49e291dF9ldmFsLm1lYW4oKTouM2Z9IChzaG91bGQgMS4wKSwgemVyb3M9eyhvdXRfZXZhbD09MCkuc3VtKCl9XHUwMDI3KVxuXG4jIFB5VG9yY2ggZXF1aXZhbGVudFxudG9yY2hfZG8gPSBubi5Ecm9wb3V0KHA9cClcbnhfdCA9IHRvcmNoLm9uZXMoNCwgOClcbnRvcmNoX2RvLnRyYWluKClcbm91dF9wdF90cmFpbiA9IHRvcmNoX2RvKHhfdClcbnByaW50KGZcdTAwMjdQeVRvcmNoIHRyYWluIG1lYW46IHtvdXRfcHRfdHJhaW4ubWVhbigpOi4zZn1cdTAwMjcpXG50b3JjaF9kby5ldmFsKClcbm91dF9wdF9ldmFsID0gdG9yY2hfZG8oeF90KVxucHJpbnQoZlx1MDAyN1B5VG9yY2ggZXZhbCAgbWVhbjoge291dF9wdF9ldmFsLm1lYW4oKTouM2Z9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRyb3BvdXQgUGxhY2VtZW50IEd1aWRlbGluZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvcnJlY3QgZHJvcG91dCBwbGFjZW1lbnQgbWF0dGVycyBzaWduaWZpY2FudGx5LiBTdGFuZGFyZCBydWxlczogKDEpIGFwcGx5IGRyb3BvdXQgYWZ0ZXIgYWN0aXZhdGlvbiBmdW5jdGlvbnMgKFJlTFUsIEdFTFUpLCBub3QgYmVmb3JlOyAoMikgZG8gbm90IGFwcGx5IGRyb3BvdXQgaW1tZWRpYXRlbHkgYmVmb3JlIHRoZSBvdXRwdXQgbGF5ZXIg4oCUIGl0IGNyZWF0ZXMgdG9vIG11Y2ggbm9pc2UgaW4gdGhlIGZpbmFsIHByZWRpY3Rpb25zOyAoMykgZG8gbm90IGFwcGx5IGRyb3BvdXQgYmV0d2VlbiBhIG5vcm1hbGl6YXRpb24gbGF5ZXIgYW5kIGl0cyBuZXh0IGxpbmVhciBsYXllciwgYXMgdGhlIGRyb3BwZWQgemVyb3MgY29ycnVwdCB0aGUgbm9ybWFsaXphdGlvbiBzdGF0aXN0aWNzOyAoNCkgaW4gVHJhbnNmb3JtZXJzLCBkcm9wb3V0IGlzIGFwcGxpZWQgYWZ0ZXIgYXR0ZW50aW9uIHdlaWdodHMsIGFmdGVyIHRoZSBhdHRlbnRpb24gb3V0cHV0IHByb2plY3Rpb24sIGFuZCBhZnRlciBlYWNoIEZGTiBsYXllci4gT3B0aW1hbCBwOiAwLjUgZm9yIGZ1bGx5LWNvbm5lY3RlZCBoaWRkZW4gbGF5ZXJzLCAwLjHigJMwLjIgZm9yIGNvbnZvbHV0aW9uYWwgbGF5ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZhcmlhdGlvbmFsIERyb3BvdXQgZm9yIFJOTnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIGRyb3BvdXQgYXBwbGllZCB0byBSTk4gaW5wdXRzIGF0IGVhY2ggdGltZXN0ZXAgdXNlcyBhIGRpZmZlcmVudCBtYXNrIHBlciBzdGVwLCB3aGljaCBkb2VzIG5vdCBlZmZlY3RpdmVseSByZWd1bGFyaXplIHRlbXBvcmFsIGRlcGVuZGVuY2llcy4gVmFyaWF0aW9uYWwgZHJvcG91dCAoR2FsIFx1MDAyNiBHaGFocmFtYW5pIDIwMTYpIHNhbXBsZXMgb25lIG1hc2sgcGVyIHNlcXVlbmNlIGFuZCBhcHBsaWVzIGl0IGNvbnNpc3RlbnRseSBhY3Jvc3MgYWxsIHRpbWVzdGVwcyDigJQgdGhlIHNhbWUgdW5pdHMgYXJlIGRyb3BwZWQgYXQgZXZlcnkgc3RlcC4gVGhpcyBwcm9wZXJseSByZWd1bGFyaXplcyB0aGUgcmVjdXJyZW50IHdlaWdodHMgYW5kIGVtcGlyaWNhbGx5IHJlZHVjZXMgcGVycGxleGl0eSBpbiBsYW5ndWFnZSBtb2RlbGluZyB0YXNrcyBieSAxMOKAkzE1JSBjb21wYXJlZCB0byBzdGFuZGFyZCBwZXItc3RlcCBkcm9wb3V0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBWYXJpYXRpb25hbERyb3BvdXRMU1RNKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGlucHV0X3NpemUsIGhpZGRlbl9zaXplLCBkcm9wb3V0X3A9MC41KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubHN0bSA9IG5uLkxTVE0oaW5wdXRfc2l6ZSwgaGlkZGVuX3NpemUsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZHJvcG91dF9wID0gZHJvcG91dF9wXG4gICAgICAgIHNlbGYuaGlkZGVuX3NpemUgPSBoaWRkZW5fc2l6ZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgICMgeDogKGJhdGNoLCBzZXFfbGVuLCBpbnB1dF9zaXplKVxuICAgICAgICBiYXRjaCwgc2VxX2xlbiwgXyA9IHguc2hhcGVcbiAgICAgICAgIyBTYW1wbGUgT05FIG1hc2sgZm9yIHRoZSBlbnRpcmUgc2VxdWVuY2UgKHZhcmlhdGlvbmFsKVxuICAgICAgICBpZiBzZWxmLnRyYWluaW5nIGFuZCBzZWxmLmRyb3BvdXRfcCBcdTAwM2UgMDpcbiAgICAgICAgICAgIG1hc2sgPSB4Lm5ld19vbmVzKGJhdGNoLCAxLCB4LnNpemUoLTEpKVxuICAgICAgICAgICAgbWFzayA9IHRvcmNoLmJlcm5vdWxsaShtYXNrICogKDEgLSBzZWxmLmRyb3BvdXRfcCkpXG4gICAgICAgICAgICBtYXNrID0gbWFzayAvICgxIC0gc2VsZi5kcm9wb3V0X3ApXG4gICAgICAgICAgICB4ID0geCAqIG1hc2suZXhwYW5kX2FzKHgpICAjIHNhbWUgbWFzayBhcHBsaWVkIGF0IGV2ZXJ5IHRpbWVzdGVwXG4gICAgICAgIG91dCwgKGgsIGMpID0gc2VsZi5sc3RtKHgpXG4gICAgICAgIHJldHVybiBvdXQsIChoLCBjKVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubW9kZWwgPSBWYXJpYXRpb25hbERyb3BvdXRMU1RNKDMyLCA2NCwgZHJvcG91dF9wPTAuMylcbm1vZGVsLnRyYWluKClcbnggPSB0b3JjaC5yYW5kbig0LCAyMCwgMzIpXG5vdXQsIF8gPSBtb2RlbCh4KVxucHJpbnQoZlx1MDAyN091dHB1dCBzaGFwZToge291dC5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3Tm9uLXplcm8gaW5wdXQgZnJhY3Rpb246IHsoeCAhPSAwKS5mbG9hdCgpLm1lYW4oKTouM2Z9XHUwMDI3KVxucHJpbnQoXHUwMDI3U2FtZSBkcm9wb3V0IG1hc2sgYXBwbGllZCBhY3Jvc3MgYWxsIDIwIHRpbWVzdGVwcyBpbiB2YXJpYXRpb25hbCBtb2RlLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEcm9wQmxvY2sgZm9yIENvbnZvbHV0aW9uYWwgTmV0d29ya3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIGRyb3BvdXQgYXBwbGllZCB0byBjb252b2x1dGlvbmFsIGZlYXR1cmUgbWFwcyBkcm9wcyBpbmRpdmlkdWFsIHBpeGVscywgYnV0IHNwYXRpYWxseSBhZGphY2VudCBhY3RpdmF0aW9ucyBhcmUgaGlnaGx5IGNvcnJlbGF0ZWQg4oCUIGRyb3BwaW5nIG9uZSBwaXhlbCBiYXJlbHkgYWZmZWN0cyBuZWFyYnkgb25lcy4gRHJvcEJsb2NrIChHaGlhc2kgZXQgYWwuIDIwMTgpIGRyb3BzIGNvbnRpZ3VvdXMgc3F1YXJlIHJlZ2lvbnMgKGJsb2NrX3NpemUgw5cgYmxvY2tfc2l6ZSkgb2YgdGhlIGZlYXR1cmUgbWFwLCBmb3JjaW5nIHRoZSBuZXR3b3JrIHRvIHNwcmVhZCBmZWF0dXJlcyBhY3Jvc3MgdGhlIHNwYXRpYWwgZXh0ZW50LiBEcm9wQmxvY2sgaXMgbW9yZSBlZmZlY3RpdmUgdGhhbiBzdGFuZGFyZCBkcm9wb3V0IGZvciBDTk4gcmVndWxhcml6YXRpb24gYW5kIGFjaGlldmVzICsx4oCTMiUgdG9wLTEgYWNjdXJhY3kgb24gSW1hZ2VOZXQgZm9yIFJlc05ldCBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBEcm9wQmxvY2syRChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkcm9wX3Byb2I9MC4xLCBibG9ja19zaXplPTcpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5kcm9wX3Byb2IgPSBkcm9wX3Byb2JcbiAgICAgICAgc2VsZi5ibG9ja19zaXplID0gYmxvY2tfc2l6ZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGlmIG5vdCBzZWxmLnRyYWluaW5nIG9yIHNlbGYuZHJvcF9wcm9iID09IDA6XG4gICAgICAgICAgICByZXR1cm4geFxuICAgICAgICBCLCBDLCBILCBXID0geC5zaGFwZVxuICAgICAgICAjIEFkanVzdCBkcm9wIHByb2JhYmlsaXR5IGZvciBjZW50ZXIgc2VlZCBwb2ludHNcbiAgICAgICAgZ2FtbWEgPSBzZWxmLmRyb3BfcHJvYiAvIChzZWxmLmJsb2NrX3NpemUgKiogMilcbiAgICAgICAgZ2FtbWEgKj0gKEggKiBXKSAvICgoSCAtIHNlbGYuYmxvY2tfc2l6ZSArIDEpICogKFcgLSBzZWxmLmJsb2NrX3NpemUgKyAxKSlcbiAgICAgICAgIyBTYW1wbGUgc2VlZCBtYXNrIHRoZW4gZGlsYXRlIHRvIGJsb2NrIHNpemVcbiAgICAgICAgbWFza19zZWVkID0gdG9yY2guYmVybm91bGxpKHRvcmNoLm9uZXMoQiwgQywgSCwgVywgZGV2aWNlPXguZGV2aWNlKSAqIGdhbW1hKVxuICAgICAgICAjIE1heC1wb29sIHRvIGV4cGFuZCBzZWVkcyBpbnRvIGJsb2Nrc1xuICAgICAgICBtYXNrID0gRi5tYXhfcG9vbDJkKFxuICAgICAgICAgICAgbWFza19zZWVkLFxuICAgICAgICAgICAga2VybmVsX3NpemU9KHNlbGYuYmxvY2tfc2l6ZSwgc2VsZi5ibG9ja19zaXplKSxcbiAgICAgICAgICAgIHN0cmlkZT0xLFxuICAgICAgICAgICAgcGFkZGluZz1zZWxmLmJsb2NrX3NpemUgLy8gMlxuICAgICAgICApXG4gICAgICAgIG1hc2sgPSAxIC0gbWFzayAgIyBpbnZlcnQ6IDE9a2VlcCwgMD1kcm9wXG4gICAgICAgICMgUmVzY2FsZSB0byBtYWludGFpbiBleHBlY3RlZCB2YWx1ZVxuICAgICAgICB4ID0geCAqIG1hc2sgKiBtYXNrLm51bWVsKCkgLyBtYXNrLnN1bSgpLmNsYW1wKG1pbj0xKVxuICAgICAgICByZXR1cm4geFxuXG5CLCBDLCBILCBXID0gMiwgMTYsIDMyLCAzMlxueCA9IHRvcmNoLnJhbmRuKEIsIEMsIEgsIFcpXG5kYiA9IERyb3BCbG9jazJEKGRyb3BfcHJvYj0wLjEsIGJsb2NrX3NpemU9NSlcbmRiLnRyYWluKClcbm91dCA9IGRiKHgpXG56ZXJvX2ZyYWMgPSAob3V0ID09IDApLmZsb2F0KCkubWVhbigpLml0ZW0oKVxucHJpbnQoZlx1MDAyN0Ryb3BCbG9jayB6ZXJvIGZyYWN0aW9uOiB7emVyb19mcmFjOi4zZn0gKGNvbnRpZ3VvdXMgYmxvY2tzIHplcm9lZClcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJNQy1Ecm9wb3V0IGZvciBVbmNlcnRhaW50eSBFc3RpbWF0aW9uIiwiY29udGVudCI6IkdhbCBcdTAwMjYgR2hhaHJhbWFuaSAoMjAxNikgc2hvd2VkIHRoYXQgYSBuZXVyYWwgbmV0d29yayB3aXRoIGRyb3BvdXQgaXMgZXF1aXZhbGVudCB0byBhIGRlZXAgR2F1c3NpYW4gUHJvY2VzcyBhcHByb3hpbWF0aW9uLiBBdCBpbmZlcmVuY2UsIGtlZXBpbmcgZHJvcG91dCBhY3RpdmUgYW5kIHJ1bm5pbmcgbXVsdGlwbGUgZm9yd2FyZCBwYXNzZXMgKE1DLURyb3BvdXQpIHByb2R1Y2VzIGEgZGlzdHJpYnV0aW9uIG9mIHByZWRpY3Rpb25zLiBUaGUgbWVhbiBnaXZlcyB0aGUgcG9pbnQgZXN0aW1hdGU7IHRoZSB2YXJpYW5jZSBlc3RpbWF0ZXMgZXBpc3RlbWljIHVuY2VydGFpbnR5LiBUaGlzIHJlcXVpcmVzIG5vIGFyY2hpdGVjdHVyZSBjaGFuZ2VzIOKAlCBqdXN0IGtlZXAgbW9kZWwudHJhaW4oKSBhdCBpbmZlcmVuY2UgdGltZSBhbmQgc2FtcGxlIE4gZm9yd2FyZCBwYXNzZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTUMtRHJvcG91dCBmb3IgVW5jZXJ0YWludHkgRXN0aW1hdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIE1DRHJvcG91dE5ldChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbnB1dF9kaW0sIGhpZGRlbl9kaW0sIG91dHB1dF9kaW0sIHA9MC4zKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihpbnB1dF9kaW0sIGhpZGRlbl9kaW0pLFxuICAgICAgICAgICAgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uRHJvcG91dChwKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihoaWRkZW5fZGltLCBoaWRkZW5fZGltKSxcbiAgICAgICAgICAgIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkRyb3BvdXQocCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuX2RpbSwgb3V0cHV0X2RpbSlcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeClcblxubW9kZWwgPSBNQ0Ryb3BvdXROZXQoMTAsIDY0LCAxLCBwPTAuMylcbnhfdGVzdCA9IHRvcmNoLnJhbmRuKDIwLCAxMClcbiMgTUMtRHJvcG91dDoga2VlcCBtb2RlbCBpbiB0cmFpbiBtb2RlLCBydW4gTiBmb3J3YXJkIHBhc3Nlc1xubW9kZWwudHJhaW4oKSAgIyBkcm9wb3V0IHN0YXlzIGFjdGl2ZVxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgc2FtcGxlcyA9IHRvcmNoLnN0YWNrKFttb2RlbCh4X3Rlc3QpIGZvciBfIGluIHJhbmdlKDEwMCldLCBkaW09MClcblxucHJlZF9tZWFuID0gc2FtcGxlcy5tZWFuKGRpbT0wKVxucHJlZF9zdGQgID0gc2FtcGxlcy5zdGQoZGltPTApXG5wcmludChmXHUwMDI3UHJlZGljdGlvbiBtZWFuOiB7cHJlZF9tZWFuLnNxdWVlemUoKVs6NV0udG9saXN0KCl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1VuY2VydGFpbnR5IHN0ZDoge3ByZWRfc3RkLnNxdWVlemUoKVs6NV0udG9saXN0KCl9XHUwMDI3KVxucHJpbnQoXHUwMDI3SGlnaCBzdGQgPVx1MDAzZSBoaWdoIGVwaXN0ZW1pYyB1bmNlcnRhaW50eSBmb3IgdGhhdCBpbnB1dC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3B0aW1hbCBEcm9wb3V0IFJhdGUgYnkgQXJjaGl0ZWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFbXBpcmljYWwgZ3VpZGVsaW5lcyBmb3IgZHJvcG91dCBwcm9iYWJpbGl0eSBwOiBGdWxseS1jb25uZWN0ZWQgbGF5ZXJzIGluIGNsYXNzaWZpZXJzIOKAlCBwPTAuNSAoU3JpdmFzdGF2YSBldCBhbC4gb3JpZ2luYWwgcmVjb21tZW5kYXRpb24pLiBDb252b2x1dGlvbmFsIGxheWVycyDigJQgcD0wLjEgdG8gMC4yIChzcGF0aWFsIGNvcnJlbGF0aW9uIG1ha2VzIHN0YW5kYXJkIGRyb3BvdXQgbGVzcyBlZmZlY3RpdmU7IHByZWZlciBEcm9wQmxvY2spLiBUcmFuc2Zvcm1lciBhdHRlbnRpb24gZHJvcG91dCDigJQgcD0wLjEgKHRvbyBtdWNoIGRyb3BvdXQgaHVydHMgYXR0ZW50aW9uIHBhdHRlcm4gZm9ybWF0aW9uKS4gVHJhbnNmb3JtZXIgRkZOIGRyb3BvdXQg4oCUIHA9MC4xIHRvIDAuMyBkZXBlbmRpbmcgb24gbW9kZWwgc2l6ZSBhbmQgZGF0YXNldC4gTGFyZ2UgcHJlLXRyYWluZWQgbW9kZWxzIChCRVJULCBHUFQpIOKAlCBwPTAuMS4gVmVyeSBzbWFsbCBkYXRhc2V0cyDigJQgcD0wLjUgdG8gMC43IGZvciBhZ2dyZXNzaXZlIHJlZ3VsYXJpemF0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQXBwbHkgZHJvcG91dCBhZnRlciBhY3RpdmF0aW9uLCBub3QgYmVmb3JlOiBkcm9wb3V0IGFmdGVyIFJlTFUgYXZvaWRzIHplcm9pbmcgdW5pdHMgdGhhdCBhcmUgYWxyZWFkeSBpbmFjdGl2ZS4iLCJTa2lwIGRyb3BvdXQgb24gdGhlIG91dHB1dCBsYXllcjogZGlyZWN0bHkgYXBwbHlpbmcgZHJvcG91dCB0byBsb2dpdHMgYWRkcyBpbnN0YWJpbGl0eSB0byB0aGUgZmluYWwgcHJlZGljdGlvbi4iLCJJbmNyZWFzZSBwIGZvciBsYXJnZXIgbW9kZWxzIHRyYWluZWQgb24gc21hbGxlciBkYXRhc2V0czogYmlnZ2VyIG1vZGVscyBoYXZlIGhpZ2hlciB2YXJpYW5jZSBhbmQgbmVlZCBtb3JlIHJlZ3VsYXJpemF0aW9uLiIsIkRpc2FibGUgZHJvcG91dCBhdCBldmFsIHRpbWU6IGFsd2F5cyBjYWxsIG1vZGVsLmV2YWwoKSBiZWZvcmUgaW5mZXJlbmNlIOKAlCBQeVRvcmNoIGhhbmRsZXMgdGhpcyBhdXRvbWF0aWNhbGx5LiIsIkRyb3BDb25uZWN0OiBkcm9wIGluZGl2aWR1YWwgd2VpZ2h0cyByYXRoZXIgdGhhbiBhY3RpdmF0aW9ucyDigJQgYSBnZW5lcmFsaXphdGlvbiBvZiBkcm9wb3V0IGxlc3MgY29tbW9ubHkgdXNlZCBpbiBwcmFjdGljZS4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRHJvcG91dCBWYXJpYW50cyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlZhcmlhbnQiLCJXaGF0IGlzIERyb3BwZWQiLCJNYXNrIFNjb3BlIiwiSW5mZXJlbmNlIEJlaGF2aW9yIiwiQmVzdCBGb3IiXSwicm93cyI6W1siU3RhbmRhcmQgRHJvcG91dCIsIkluZGl2aWR1YWwgYWN0aXZhdGlvbnMiLCJOZXcgbWFzayBwZXIgZm9yd2FyZCBwYXNzIiwiRGlzYWJsZWQgKHNjYWxpbmcgaGFuZGxlZCBieSBpbnZlcnRlZCBkcm9wb3V0KSIsIkZDIGxheWVycyBpbiBjbGFzc2lmaWVycyJdLFsiSW52ZXJ0ZWQgRHJvcG91dCIsIkluZGl2aWR1YWwgYWN0aXZhdGlvbnMgKHNjYWxlZCBkdXJpbmcgdHJhaW4pIiwiTmV3IG1hc2sgcGVyIGZvcndhcmQgcGFzcyIsIk5vIG1vZGlmaWNhdGlvbiBuZWVkZWQiLCJEZWZhdWx0IGV2ZXJ5d2hlcmUg4oCUIHNhbWUgYXMgc3RhbmRhcmQgaW4gUHlUb3JjaCJdLFsiVmFyaWF0aW9uYWwgRHJvcG91dCIsIkluZGl2aWR1YWwgYWN0aXZhdGlvbnMiLCJTYW1lIG1hc2sgYWNyb3NzIGFsbCB0aW1lc3RlcHMiLCJEaXNhYmxlZCIsIlJOTnMsIExTVE1zIOKAlCBjb25zaXN0ZW50IHRlbXBvcmFsIHJlZ3VsYXJpemF0aW9uIl0sWyJEcm9wQmxvY2siLCJDb250aWd1b3VzIHNwYXRpYWwgYmxvY2tzIGluIGZlYXR1cmUgbWFwcyIsIk5ldyBibG9jayBtYXNrIHBlciBmb3J3YXJkIHBhc3MiLCJEaXNhYmxlZCIsIkNOTiBmZWF0dXJlIG1hcHMg4oCUIGJldHRlciB0aGFuIHBlci1waXhlbCBkcm9wb3V0Il0sWyJNQy1Ecm9wb3V0IiwiSW5kaXZpZHVhbCBhY3RpdmF0aW9ucyAoa2VwdCBhY3RpdmUgYXQgdGVzdCkiLCJOZXcgbWFzayBwZXIgZm9yd2FyZCBwYXNzIiwiQUNUSVZFIOKAlCBOIHBhc3NlcyBmb3IgdW5jZXJ0YWludHkiLCJCYXllc2lhbiB1bmNlcnRhaW50eSBlc3RpbWF0aW9uIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkludmVydGVkIGRyb3BvdXQgKFB5VG9yY2hcdTAwMjdzIG5uLkRyb3BvdXQpIGlzIHRoZSBkZWZhdWx0IGZvciBtb3N0IGFyY2hpdGVjdHVyZXMuIFN3aXRjaCB0byB2YXJpYXRpb25hbCBkcm9wb3V0IGZvciBzZXF1ZW5jZSBtb2RlbHMgKFJOTnMsIExTVE1zKSB3aGVyZSB0ZW1wb3JhbCBjb25zaXN0ZW5jeSBtYXR0ZXJzLiBVc2UgRHJvcEJsb2NrIGZvciBDTk4gYmFja2JvbmVzIHdoZW4gZHJvcG91dCBpcyBub3QgcHJvdmlkaW5nIGVub3VnaCByZWd1bGFyaXphdGlvbi4gQXBwbHkgTUMtRHJvcG91dCBmb3IgYW55IHNhZmV0eS1jcml0aWNhbCBhcHBsaWNhdGlvbiB0aGF0IHJlcXVpcmVzIGNhbGlicmF0ZWQgdW5jZXJ0YWludHkgZXN0aW1hdGVzIHdpdGhvdXQgYWRkaW5nIGEgc2VwYXJhdGUgdW5jZXJ0YWludHkgaGVhZC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Dropout — Inverted Dropout, Variational, and Structured

Dropout (Srivastava et al. 2014) randomly sets activations to zero with probability p during training, preventing neurons from co-adapting and acting as an implicit ensemble of 2ⁿ sub-networks (where n is the number of units). Each forward pass samples a different binary mask, training a different thinned network. At test time, all neurons are used and outputs are scaled to match the expected value during training. This ensemble interpretation explains why dropout improves generalization: it prevents any single neuron from being essential for a prediction.

## Standard Dropout and Inverted Dropout

Two equivalent formulations exist. Standard dropout: zero out with probability p, scale by 1/(1-p) at test time. Inverted dropout (the modern default in PyTorch and TensorFlow): scale kept activations by 1/(1-p) during training, no scaling at test time. Inverted dropout is preferred because the test-time network is a simple feed-forward pass with no modification — model.eval() automatically disables dropout without requiring any weight rescaling. PyTorch's nn.Dropout uses inverted dropout internally.

```python
import numpy as np
import torch
import torch.nn as nn

def inverted_dropout(x, p, training=True):
    if not training or p == 0.0:
        return x
    # Sample binary mask: keep each unit with probability (1-p)
    mask = (np.random.rand(*x.shape) > p).astype(np.float32)
    # Scale by 1/(1-p) so expected value matches x
    return x * mask / (1.0 - p)

np.random.seed(42)
x = np.ones((4, 8))  # all-ones to see scaling clearly
p = 0.5

# Training mode: some units zeroed, survivors scaled up
out_train = inverted_dropout(x, p, training=True)
print(f'Train: mean={out_train.mean():.3f} (should ~1.0), zeros={( out_train==0).sum()}')

# Eval mode: all units active, no scaling needed
out_eval = inverted_dropout(x, p, training=False)
print(f'Eval:  mean={out_eval.mean():.3f} (should 1.0), zeros={(out_eval==0).sum()}')

# PyTorch equivalent
torch_do = nn.Dropout(p=p)
x_t = torch.ones(4, 8)
torch_do.train()
out_pt_train = torch_do(x_t)
print(f'PyTorch train mean: {out_pt_train.mean():.3f}')
torch_do.eval()
out_pt_eval = torch_do(x_t)
print(f'PyTorch eval  mean: {out_pt_eval.mean():.3f}')
```

## Dropout Placement Guidelines

Correct dropout placement matters significantly. Standard rules: (1) apply dropout after activation functions (ReLU, GELU), not before; (2) do not apply dropout immediately before the output layer — it creates too much noise in the final predictions; (3) do not apply dropout between a normalization layer and its next linear layer, as the dropped zeros corrupt the normalization statistics; (4) in Transformers, dropout is applied after attention weights, after the attention output projection, and after each FFN layer. Optimal p: 0.5 for fully-connected hidden layers, 0.1–0.2 for convolutional layers.

## Variational Dropout for RNNs

Standard dropout applied to RNN inputs at each timestep uses a different mask per step, which does not effectively regularize temporal dependencies. Variational dropout (Gal & Ghahramani 2016) samples one mask per sequence and applies it consistently across all timesteps — the same units are dropped at every step. This properly regularizes the recurrent weights and empirically reduces perplexity in language modeling tasks by 10–15% compared to standard per-step dropout.

```python
import torch
import torch.nn as nn

class VariationalDropoutLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, dropout_p=0.5):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.dropout_p = dropout_p
        self.hidden_size = hidden_size

    def forward(self, x):
        # x: (batch, seq_len, input_size)
        batch, seq_len, _ = x.shape
        # Sample ONE mask for the entire sequence (variational)
        if self.training and self.dropout_p > 0:
            mask = x.new_ones(batch, 1, x.size(-1))
            mask = torch.bernoulli(mask * (1 - self.dropout_p))
            mask = mask / (1 - self.dropout_p)
            x = x * mask.expand_as(x)  # same mask applied at every timestep
        out, (h, c) = self.lstm(x)
        return out, (h, c)

torch.manual_seed(0)
model = VariationalDropoutLSTM(32, 64, dropout_p=0.3)
model.train()
x = torch.randn(4, 20, 32)
out, _ = model(x)
print(f'Output shape: {out.shape}')
print(f'Non-zero input fraction: {(x != 0).float().mean():.3f}')
print('Same dropout mask applied across all 20 timesteps in variational mode.')
```

## DropBlock for Convolutional Networks

Standard dropout applied to convolutional feature maps drops individual pixels, but spatially adjacent activations are highly correlated — dropping one pixel barely affects nearby ones. DropBlock (Ghiasi et al. 2018) drops contiguous square regions (block_size × block_size) of the feature map, forcing the network to spread features across the spatial extent. DropBlock is more effective than standard dropout for CNN regularization and achieves +1–2% top-1 accuracy on ImageNet for ResNet architectures.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DropBlock2D(nn.Module):
    def __init__(self, drop_prob=0.1, block_size=7):
        super().__init__()
        self.drop_prob = drop_prob
        self.block_size = block_size

    def forward(self, x):
        if not self.training or self.drop_prob == 0:
            return x
        B, C, H, W = x.shape
        # Adjust drop probability for center seed points
        gamma = self.drop_prob / (self.block_size ** 2)
        gamma *= (H * W) / ((H - self.block_size + 1) * (W - self.block_size + 1))
        # Sample seed mask then dilate to block size
        mask_seed = torch.bernoulli(torch.ones(B, C, H, W, device=x.device) * gamma)
        # Max-pool to expand seeds into blocks
        mask = F.max_pool2d(
            mask_seed,
            kernel_size=(self.block_size, self.block_size),
            stride=1,
            padding=self.block_size // 2
        )
        mask = 1 - mask  # invert: 1=keep, 0=drop
        # Rescale to maintain expected value
        x = x * mask * mask.numel() / mask.sum().clamp(min=1)
        return x

B, C, H, W = 2, 16, 32, 32
x = torch.randn(B, C, H, W)
db = DropBlock2D(drop_prob=0.1, block_size=5)
db.train()
out = db(x)
zero_frac = (out == 0).float().mean().item()
print(f'DropBlock zero fraction: {zero_frac:.3f} (contiguous blocks zeroed)')
```

> **MC-Dropout for Uncertainty Estimation**: Gal & Ghahramani (2016) showed that a neural network with dropout is equivalent to a deep Gaussian Process approximation. At inference, keeping dropout active and running multiple forward passes (MC-Dropout) produces a distribution of predictions. The mean gives the point estimate; the variance estimates epistemic uncertainty. This requires no architecture changes — just keep model.train() at inference time and sample N forward passes.

## MC-Dropout for Uncertainty Estimation

```python
import torch
import torch.nn as nn
import numpy as np

class MCDropoutNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, p=0.3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(p),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(p),
            nn.Linear(hidden_dim, output_dim)
        )
    def forward(self, x):
        return self.net(x)

model = MCDropoutNet(10, 64, 1, p=0.3)
x_test = torch.randn(20, 10)
# MC-Dropout: keep model in train mode, run N forward passes
model.train()  # dropout stays active
with torch.no_grad():
    samples = torch.stack([model(x_test) for _ in range(100)], dim=0)

pred_mean = samples.mean(dim=0)
pred_std  = samples.std(dim=0)
print(f'Prediction mean: {pred_mean.squeeze()[:5].tolist()}')
print(f'Uncertainty std: {pred_std.squeeze()[:5].tolist()}')
print('High std => high epistemic uncertainty for that input.')
```

## Optimal Dropout Rate by Architecture

Empirical guidelines for dropout probability p: Fully-connected layers in classifiers — p=0.5 (Srivastava et al. original recommendation). Convolutional layers — p=0.1 to 0.2 (spatial correlation makes standard dropout less effective; prefer DropBlock). Transformer attention dropout — p=0.1 (too much dropout hurts attention pattern formation). Transformer FFN dropout — p=0.1 to 0.3 depending on model size and dataset. Large pre-trained models (BERT, GPT) — p=0.1. Very small datasets — p=0.5 to 0.7 for aggressive regularization.

- Apply dropout after activation, not before: dropout after ReLU avoids zeroing units that are already inactive.
- Skip dropout on the output layer: directly applying dropout to logits adds instability to the final prediction.
- Increase p for larger models trained on smaller datasets: bigger models have higher variance and need more regularization.
- Disable dropout at eval time: always call model.eval() before inference — PyTorch handles this automatically.
- DropConnect: drop individual weights rather than activations — a generalization of dropout less commonly used in practice.

## Dropout Variants Comparison

| Variant | What is Dropped | Mask Scope | Inference Behavior | Best For |
| --- | --- | --- | --- | --- |
| Standard Dropout | Individual activations | New mask per forward pass | Disabled (scaling handled by inverted dropout) | FC layers in classifiers |
| Inverted Dropout | Individual activations (scaled during train) | New mask per forward pass | No modification needed | Default everywhere — same as standard in PyTorch |
| Variational Dropout | Individual activations | Same mask across all timesteps | Disabled | RNNs, LSTMs — consistent temporal regularization |
| DropBlock | Contiguous spatial blocks in feature maps | New block mask per forward pass | Disabled | CNN feature maps — better than per-pixel dropout |
| MC-Dropout | Individual activations (kept active at test) | New mask per forward pass | ACTIVE — N passes for uncertainty | Bayesian uncertainty estimation |

Inverted dropout (PyTorch's nn.Dropout) is the default for most architectures. Switch to variational dropout for sequence models (RNNs, LSTMs) where temporal consistency matters. Use DropBlock for CNN backbones when dropout is not providing enough regularization. Apply MC-Dropout for any safety-critical application that requires calibrated uncertainty estimates without adding a separate uncertainty head.

---

