---
title: "Transfer Learning — Feature Extraction vs Fine-Tuning Strategies"
slug: "transfer-learning-cnn"
description: "Transfer learning strategies for CNNs: feature extraction (frozen backbone) vs fine-tuning (unfrozen layers). Covers discriminative learning rates per layer group, progressive unfreezing, freezing BatchNorm statistics, and domain shift considerations for ImageNet-pretrained models."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhbnNmZXIgbGVhcm5pbmcgaXMgdGhlIHByYWN0aWNlIG9mIGluaXRpYWxpemluZyBhIG1vZGVsIHdpdGggd2VpZ2h0cyBwcmV0cmFpbmVkIG9uIGEgbGFyZ2UgZGF0YXNldCAodHlwaWNhbGx5IEltYWdlTmV0IHdpdGggMS4yOE0gaW1hZ2VzIGFuZCAxMDAwIGNsYXNzZXMpIGFuZCBhZGFwdGluZyBpdCB0byBhIG5ldyB0YXNrLiBCZWNhdXNlIGVhcmx5IENOTiBsYXllcnMgbGVhcm4gdW5pdmVyc2FsIGxvdy1sZXZlbCBmZWF0dXJlcyAoZWRnZXMsIHRleHR1cmVzLCBjb2xvcnMpIGFuZCBsYXRlciBsYXllcnMgbGVhcm4gaW5jcmVhc2luZ2x5IHRhc2stc3BlY2lmaWMgZmVhdHVyZXMsIHByZXRyYWluZWQgd2VpZ2h0cyBwcm92aWRlIGEgcG93ZXJmdWwgc3RhcnRpbmcgcG9pbnQgdGhhdCBkcmFtYXRpY2FsbHkgcmVkdWNlcyB0aGUgZGF0YSBhbmQgY29tcHV0ZSByZXF1aXJlZCBmb3IgdGhlIHRhcmdldCB0YXNrLiBUaGUgdHdvIHByaW1hcnkgdHJhbnNmZXIgc3RyYXRlZ2llcyDigJQgZmVhdHVyZSBleHRyYWN0aW9uIGFuZCBmaW5lLXR1bmluZyDigJQgZGlmZmVyIGluIHdoaWNoIGxheWVycyBhcmUgYWxsb3dlZCB0byB1cGRhdGUgZHVyaW5nIHRhcmdldCB0cmFpbmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGZWF0dXJlIEV4dHJhY3Rpb24g4oCUIEZyb3plbiBCYWNrYm9uZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gZmVhdHVyZSBleHRyYWN0aW9uLCBhbGwgY29udm9sdXRpb25hbCBsYXllcnMgYXJlIGZyb3plbiAocmVxdWlyZXNfZ3JhZD1GYWxzZSkgYW5kIG9ubHkgdGhlIGNsYXNzaWZpY2F0aW9uIGhlYWQgaXMgdHJhaW5lZC4gVGhlIGJhY2tib25lIGFjdHMgYXMgYSBmaXhlZCBmZWF0dXJlIGV4dHJhY3RvcjogZWFjaCBpbWFnZSBpcyBtYXBwZWQgdG8gYSBmZWF0dXJlIHZlY3RvciAoZS5nLiwgMjA0OC1kaW0gZm9yIFJlc05ldC01MCBhZnRlciBnbG9iYWwgYXZnIHBvb2wpLCBhbmQgYSBuZXcgbGluZWFyIGNsYXNzaWZpZXIgaXMgdHJhaW5lZCBvbiB0b3Agb2YgdGhlc2UgZnJvemVuIGZlYXR1cmVzLiBUaGlzIGlzIGZhc3QgKG9ubHkgaGVhZCBwYXJhbXMgYXJlIG9wdGltaXplZCksIG1lbW9yeS1lZmZpY2llbnQgKG5vIGdyYWRpZW50cyB0aHJvdWdoIHRoZSBiYWNrYm9uZSksIGFuZCB3b3JrcyB3ZWxsIHdoZW4gdGhlIHRhcmdldCBkb21haW4gaXMgdmlzdWFsbHkgc2ltaWxhciB0byBJbWFnZU5ldC4gRmVhdHVyZSBleHRyYWN0aW9uIGlzIHRoZSByaWdodCBjaG9pY2Ugd2hlbiB0cmFpbmluZyBkYXRhIGlzIHZlcnkgc21hbGwgKFx1MDAzYzEwMDAgZXhhbXBsZXMpIG9yIHdoZW4gdGhlIHRhcmdldCB0YXNrIGlzIHNpbWlsYXIgdG8gSW1hZ2VOZXQgY2xhc3NpZmljYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmluZS1UdW5pbmcg4oCUIFVuZnJlZXppbmcgTGF5ZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBmaW5lLXR1bmluZywgc29tZSBvciBhbGwgcHJldHJhaW5lZCBsYXllcnMgYXJlIHVuZnJvemVuIGFuZCBhbGxvd2VkIHRvIHVwZGF0ZSBkdXJpbmcgdGFyZ2V0IHRyYWluaW5nLiBUaGUga2V5IGh5cGVycGFyYW1ldGVyIGlzIHRoZSBsZWFybmluZyByYXRlOiBwcmV0cmFpbmVkIGxheWVycyBzaG91bGQgdXNlIGEgbXVjaCBsb3dlciBsZWFybmluZyByYXRlICgxZS01IHRvIDFlLTQpIHRoYW4gdGhlIG5ldyBoZWFkICgxZS0zKSwgdG8gcHJlc2VydmUgdGhlIGxlYXJuZWQgcmVwcmVzZW50YXRpb25zIHdoaWxlIGFsbG93aW5nIHRoZW0gdG8gc2hpZnQgc2xpZ2h0bHkgdG93YXJkIHRoZSB0YXJnZXQgZG9tYWluLiBGaW5lLXR1bmluZyBwcm92aWRlcyBoaWdoZXIgYWNjdXJhY3kgdGhhbiBmZWF0dXJlIGV4dHJhY3Rpb24gb24gbW9zdCB0YXNrcyBiZWNhdXNlIHRoZSBiYWNrYm9uZSBjYW4gYWRhcHQgaXRzIGhpZ2hlci1sZXZlbCBmZWF0dXJlcyB0byB0aGUgdGFyZ2V0IGRpc3RyaWJ1dGlvbi4gSXQgcmVxdWlyZXMgbW9yZSB0cmFpbmluZyBkYXRhICh0eXBpY2FsbHkgXHUwMDNlNTAwMCBleGFtcGxlcykgYW5kIGxvbmdlciB0cmFpbmluZyB0byBhdm9pZCBvdmVyZml0dGluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaGVuIHRvIFVzZSBXaGljaCBTdHJhdGVneSJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVmVyeSBzbWFsbCBkYXRhc2V0IChcdTAwM2MxMDAwIHNhbXBsZXMpLCBzaW1pbGFyIGRvbWFpbiAoZS5nLiwgcGV0cywgZmxvd2VycykgLVx1MDAzZSBmZWF0dXJlIGV4dHJhY3Rpb24gb25seS4iLCJTbWFsbCBkYXRhc2V0ICgxMDAwLTEwMDAwKSwgc2ltaWxhciBkb21haW4gLVx1MDAzZSBmaW5lLXR1bmUgdG9wIDEtMiBsYXllcnMgKyBoZWFkLiIsIk1lZGl1bSBkYXRhc2V0ICgxMDAwMCspLCBzaW1pbGFyIGRvbWFpbiAtXHUwMDNlIGZpbmUtdHVuZSBhbGwgbGF5ZXJzIHdpdGggc21hbGwgYmFja2JvbmUgTFIuIiwiTGFyZ2UgZGF0YXNldCAoMTAwMDAwKyksIGFueSBkb21haW4gLVx1MDAzZSBmaW5lLXR1bmUgYWxsIGxheWVycyBvciB0cmFpbiBmcm9tIHNjcmF0Y2guIiwiVmVyeSBkaWZmZXJlbnQgZG9tYWluIChlLmcuLCBtZWRpY2FsIGltYWdpbmcsIHNhdGVsbGl0ZSkgLVx1MDAzZSBmaW5lLXR1bmUgYWxsIGxheWVycyByZWdhcmRsZXNzIG9mIHNpemUuIiwiTG93IGNvbXB1dGUgYnVkZ2V0IC1cdTAwM2UgZmVhdHVyZSBleHRyYWN0aW9uIChubyBiYWNrYm9uZSBncmFkaWVudHMsIGZhc3RlciBwZXIgc3RlcCkuIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQWx3YXlzIEZyZWV6ZSBCYXRjaE5vcm0gRHVyaW5nIEZpbmUtVHVuaW5nIiwiY29udGVudCI6IkJhdGNoTm9ybSBsYXllcnMgbWFpbnRhaW4gcnVubmluZyBzdGF0aXN0aWNzIChtZWFuIGFuZCB2YXJpYW5jZSkgZXN0aW1hdGVkIGZyb20gdHJhaW5pbmcgYmF0Y2hlcy4gV2hlbiB5b3UgY2FsbCBtb2RlbC50cmFpbigpIGFuZCBmaW5lLXR1bmUgd2l0aCBzbWFsbCBiYXRjaGVzIG9uIGEgbmV3IGRvbWFpbiwgdGhlIHJ1bm5pbmcgc3RhdHMgYXJlIHVwZGF0ZWQgdG8gcmVmbGVjdCB0aGUgbmV3IGRpc3RyaWJ1dGlvbiDigJQgZGVzdHJveWluZyB0aGUgc3RhdGlzdGljcyBjYWxpYnJhdGVkIG9uIEltYWdlTmV0LiBBbHdheXMgY2FsbCBibl9tb2R1bGUuZXZhbCgpIGFmdGVyIG1vZGVsLnRyYWluKCkgdG8gZnJlZXplIHRoZSBCTiBydW5uaW5nIHN0YXRzLiBUaGUgYWZmaW5lIHBhcmFtZXRlcnMgKGdhbW1hLCBiZXRhKSBjYW4gc3RpbGwgYmUgdXBkYXRlZC4gRm9yZ2V0dGluZyB0aGlzIHN0ZXAgb2Z0ZW4gY2F1c2VzIGEgc2lnbmlmaWNhbnQgYWNjdXJhY3kgZHJvcCwgZXNwZWNpYWxseSB3aGVuIHRoZSB0YXJnZXQgYmF0Y2ggc2l6ZSBpcyBzbWFsbCBvciB0aGUgZG9tYWluIHNoaWZ0IGlzIGxhcmdlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpc2NyaW1pbmF0aXZlIExlYXJuaW5nIFJhdGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEaXNjcmltaW5hdGl2ZSBsZWFybmluZyByYXRlcyAoSG93YXJkIFx1MDAyNiBSdWRlciwgVUxNRmlUIDIwMTgpIGFzc2lnbiBkaWZmZXJlbnQgbGVhcm5pbmcgcmF0ZXMgdG8gZGlmZmVyZW50IGxheWVyIGdyb3VwczogZWFybGllciBsYXllcnMgKGNsb3NlciB0byB0aGUgaW5wdXQpIHVzZSBsb3dlciBsZWFybmluZyByYXRlcywgbGF0ZXIgbGF5ZXJzIHVzZSBoaWdoZXIgcmF0ZXMuIFRoZSByYXRpb25hbGU6IGVhcmx5IGxheWVycyBjb250YWluIG1vcmUgZ2VuZXJhbCwgdHJhbnNmZXJhYmxlIGZlYXR1cmVzIHRoYXQgc2hvdWxkIGNoYW5nZSBsaXR0bGU7IGxhdGVyIGxheWVycyBjb250YWluIG1vcmUgdGFzay1zcGVjaWZpYyBmZWF0dXJlcyB0aGF0IG5lZWQgdG8gYWRhcHQgbW9yZS4gRm9yIFJlc05ldC01MCwgYSB0eXBpY2FsIHNjaGVkdWxlIG1pZ2h0IGJlOiBsYXllcjEgTFIgPSAxZS01LCBsYXllcjIgTFIgPSAzZS01LCBsYXllcjMgTFIgPSAxZS00LCBsYXllcjQgTFIgPSAzZS00LCBmYyBMUiA9IDFlLTMgKGEgMTDDlyBzdGVwIHBlciBncm91cCkuIFRoaXMgYWNoaWV2ZXMgYmV0dGVyIGFjY3VyYWN5IHRoYW4gYSBzaW5nbGUgTFIgZm9yIGFsbCBsYXllcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSBFeGFtcGxlcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgbW9kZWxzXG5cbmRlZiBidWlsZF9mZWF0dXJlX2V4dHJhY3RvcihudW1fY2xhc3NlczogaW50KTpcbiAgICBcIlwiXCJGcmVlemUgYWxsIGJhY2tib25lIHBhcmFtczsgb25seSB0cmFpbiB0aGUgbmV3IGNsYXNzaWZpY2F0aW9uIGhlYWQuXCJcIlwiXG4gICAgbW9kZWwgPSBtb2RlbHMucmVzbmV0NTAod2VpZ2h0cz1tb2RlbHMuUmVzTmV0NTBfV2VpZ2h0cy5JTUFHRU5FVDFLX1YxKVxuICAgICMgRnJlZXplIGFsbCBwYXJhbWV0ZXJzXG4gICAgZm9yIHBhcmFtIGluIG1vZGVsLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgcGFyYW0ucmVxdWlyZXNfZ3JhZCA9IEZhbHNlXG4gICAgIyBSZXBsYWNlIGZpbmFsIGZ1bGx5LWNvbm5lY3RlZCBsYXllclxuICAgIG1vZGVsLmZjID0gbm4uTGluZWFyKG1vZGVsLmZjLmluX2ZlYXR1cmVzLCBudW1fY2xhc3NlcylcbiAgICAjIGZjIGlzIG5ld2x5IGNyZWF0ZWQgc28gcmVxdWlyZXNfZ3JhZD1UcnVlIGJ5IGRlZmF1bHRcbiAgICB0cmFpbmFibGUgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWQpXG4gICAgdG90YWwgICAgID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpXG4gICAgcHJpbnQoZlwiVHJhaW5hYmxlOiB7dHJhaW5hYmxlOix9IC8ge3RvdGFsOix9ICh7MTAwKnRyYWluYWJsZS90b3RhbDouM2Z9JSlcIilcbiAgICByZXR1cm4gbW9kZWxcblxubW9kZWwgPSBidWlsZF9mZWF0dXJlX2V4dHJhY3RvcihudW1fY2xhc3Nlcz0xMClcbm9wdGltaXplciA9IHRvcmNoLm9wdGltLkFkYW0oXG4gICAgZmlsdGVyKGxhbWJkYSBwOiBwLnJlcXVpcmVzX2dyYWQsIG1vZGVsLnBhcmFtZXRlcnMoKSksIGxyPTFlLTNcbilcbmNyaXRlcmlvbiA9IG5uLkNyb3NzRW50cm9weUxvc3MoKVxucHJpbnQoZlwiT3B0aW1pemVyIHBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIGcgaW4gb3B0aW1pemVyLnBhcmFtX2dyb3VwcyBmb3IgcCBpbiBnW1x1MDAyN3BhcmFtc1x1MDAyN10pOix9XCIpXG5wcmludChcIkZlYXR1cmUgZXh0cmFjdGlvbjogYmFja2JvbmUgaXMgYSBmaXhlZCB0cmFuc2Zvcm07IG9ubHkgaGVhZCBwYXJhbXMgb3B0aW1pemVkXCIpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNodmlzaW9uIGltcG9ydCBtb2RlbHNcblxuZGVmIG1ha2VfZGlzY3JpbWluYXRpdmVfZ3JvdXBzKG1vZGVsLCBiYXNlX2xyPTFlLTUsIGxyX211bHQ9My4wKTpcbiAgICBcIlwiXCJcbiAgICBEaXNjcmltaW5hdGl2ZSBMUnM6IGVhcmxpZXIgbGF5ZXJzIGdldCBsb3dlciBMUiB0byBwcmVzZXJ2ZSBwcmV0cmFpbmVkIGZlYXR1cmVzLlxuICAgIEVhY2ggZGVlcGVyIGxheWVyIGdyb3VwIHVzZXMgbHJfbXVsdCB4IGhpZ2hlciBMUiB0aGFuIHRoZSBwcmV2aW91cy5cbiAgICBcIlwiXCJcbiAgICBncm91cHMgPSBbXG4gICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IG1vZGVsLmxheWVyMS5wYXJhbWV0ZXJzKCksIFx1MDAyN2xyXHUwMDI3OiBiYXNlX2xyfSxcbiAgICAgICAge1x1MDAyN3BhcmFtc1x1MDAyNzogbW9kZWwubGF5ZXIyLnBhcmFtZXRlcnMoKSwgXHUwMDI3bHJcdTAwMjc6IGJhc2VfbHIgKiBscl9tdWx0fSxcbiAgICAgICAge1x1MDAyN3BhcmFtc1x1MDAyNzogbW9kZWwubGF5ZXIzLnBhcmFtZXRlcnMoKSwgXHUwMDI3bHJcdTAwMjc6IGJhc2VfbHIgKiBscl9tdWx0KioyfSxcbiAgICAgICAge1x1MDAyN3BhcmFtc1x1MDAyNzogbW9kZWwubGF5ZXI0LnBhcmFtZXRlcnMoKSwgXHUwMDI3bHJcdTAwMjc6IGJhc2VfbHIgKiBscl9tdWx0KiozfSxcbiAgICAgICAge1x1MDAyN3BhcmFtc1x1MDAyNzogbW9kZWwuZmMucGFyYW1ldGVycygpLCAgICAgXHUwMDI3bHJcdTAwMjc6IGJhc2VfbHIgKiBscl9tdWx0Kio0fSxcbiAgICBdXG4gICAgcmV0dXJuIGdyb3Vwc1xuXG5tb2RlbCA9IG1vZGVscy5yZXNuZXQ1MCh3ZWlnaHRzPW1vZGVscy5SZXNOZXQ1MF9XZWlnaHRzLklNQUdFTkVUMUtfVjEpXG5tb2RlbC5mYyA9IG5uLkxpbmVhcihtb2RlbC5mYy5pbl9mZWF0dXJlcywgMTApXG5cbmdyb3VwcyA9IG1ha2VfZGlzY3JpbWluYXRpdmVfZ3JvdXBzKG1vZGVsLCBiYXNlX2xyPTFlLTUsIGxyX211bHQ9My4wKVxub3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbShncm91cHMpXG5cbm5hbWVzID0gW1x1MDAyN2xheWVyMVx1MDAyNywgXHUwMDI3bGF5ZXIyXHUwMDI3LCBcdTAwMjdsYXllcjNcdTAwMjcsIFx1MDAyN2xheWVyNFx1MDAyNywgXHUwMDI3ZmNcdTAwMjddXG5wcmludChcdTAwMjdEaXNjcmltaW5hdGl2ZSBsZWFybmluZyByYXRlczpcdTAwMjcpXG5mb3IgbmFtZSwgZyBpbiB6aXAobmFtZXMsIGdyb3Vwcyk6XG4gICAgbiA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gZ1tcdTAwMjdwYXJhbXNcdTAwMjddKVxuICAgIHByaW50KGZcIiAge25hbWU6XHUwMDNjMTB9OiBscj17Z1tcdTAwMjdsclx1MDAyN106LjFlfSAgKHtuOix9IHBhcmFtcylcIilcbnByaW50KFx1MDAyN0VhcmxpZXIgbGF5ZXJzIHVzZSBsb3dlciBMUiAtLSBwcmV0cmFpbmVkIGZlYXR1cmVzIHByZXNlcnZlZCBtb3JlIHN0cm9uZ2x5XHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgbW9kZWxzXG5cbmRlZiBzZXRfcmVxdWlyZXNfZ3JhZF9mcm9tKG1vZGVsLCBsYXllcl9uYW1lOiBzdHIpOlxuICAgIFwiXCJcIkZyZWV6ZSBhbGwgbGF5ZXJzIGJlZm9yZSBsYXllcl9uYW1lOyB1bmZyZWV6ZSBmcm9tIGxheWVyX25hbWUgb253YXJkLlwiXCJcIlxuICAgIHVuZnJlZXppbmcgPSBGYWxzZVxuICAgIGZvciBuYW1lLCBwYXJhbSBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCk6XG4gICAgICAgIGlmIGxheWVyX25hbWUgaW4gbmFtZTpcbiAgICAgICAgICAgIHVuZnJlZXppbmcgPSBUcnVlXG4gICAgICAgIHBhcmFtLnJlcXVpcmVzX2dyYWQgPSB1bmZyZWV6aW5nXG4gICAgbiA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZClcbiAgICBwcmludChmXCIgIFVuZnJvemVuIGZyb20gXHUwMDI3e2xheWVyX25hbWV9XHUwMDI3OiB7bjosfSB0cmFpbmFibGUgcGFyYW1zXCIpXG5cbm1vZGVsID0gbW9kZWxzLnJlc25ldDUwKHdlaWdodHM9bW9kZWxzLlJlc05ldDUwX1dlaWdodHMuSU1BR0VORVQxS19WMSlcbm1vZGVsLmZjID0gbm4uTGluZWFyKG1vZGVsLmZjLmluX2ZlYXR1cmVzLCAxMClcblxuIyBFcG9jaCAxLTU6IGhlYWQgb25seSAoZmVhdHVyZSBleHRyYWN0aW9uIHdhcm11cClcbmZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKTogcC5yZXF1aXJlc19ncmFkID0gRmFsc2VcbmZvciBwIGluIG1vZGVsLmZjLnBhcmFtZXRlcnMoKTogcC5yZXF1aXJlc19ncmFkID0gVHJ1ZVxucHJpbnQoXCJFcG9jaCAxLTUgKGhlYWQgb25seSk6XCIpXG5wcmludChmXCIgIFRyYWluYWJsZToge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZCk6LH1cIilcblxuIyBFcG9jaCA2LTEwOiB1bmZyZWV6ZSBsYXllcjQgKGRlZXBlc3QgcmVzaWR1YWwgYmxvY2spXG5wcmludChcIkVwb2NoIDYtMTA6XCIpXG5zZXRfcmVxdWlyZXNfZ3JhZF9mcm9tKG1vZGVsLCBcdTAwMjdsYXllcjRcdTAwMjcpXG5cbiMgRXBvY2ggMTEtMTU6IHVuZnJlZXplIGxheWVyM1xucHJpbnQoXCJFcG9jaCAxMS0xNTpcIilcbnNldF9yZXF1aXJlc19ncmFkX2Zyb20obW9kZWwsIFx1MDAyN2xheWVyM1x1MDAyNylcblxuIyBFcG9jaCAxNis6IGZ1bGwgZmluZS10dW5pbmdcbmZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKTogcC5yZXF1aXJlc19ncmFkID0gVHJ1ZVxucHJpbnQoXCJFcG9jaCAxNisgKGZ1bGwpOlwiKVxucHJpbnQoZlwiICBUcmFpbmFibGU6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWQpOix9XCIpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNodmlzaW9uIGltcG9ydCBtb2RlbHNcblxuZGVmIGZyZWV6ZV9ibl9zdGF0cyhtb2RlbDogbm4uTW9kdWxlKTpcbiAgICBcIlwiXCJcbiAgICBLZWVwIEJOIGxheWVycyBpbiBldmFsIG1vZGUgdG8gZnJlZXplIHJ1bm5pbmdfbWVhbi9ydW5uaW5nX3Zhci5cbiAgICBBZmZpbmUgcGFyYW1zICh3ZWlnaHQ9Z2FtbWEsIGJpYXM9YmV0YSkgcmVtYWluIHRyYWluYWJsZS5cbiAgICBDYWxsIHRoaXMgQUZURVIgbW9kZWwudHJhaW4oKSBpbiBlYWNoIHRyYWluaW5nIGl0ZXJhdGlvbi5cbiAgICBcIlwiXCJcbiAgICBmb3IgbW9kdWxlIGluIG1vZGVsLm1vZHVsZXMoKTpcbiAgICAgICAgaWYgaXNpbnN0YW5jZShtb2R1bGUsIG5uLkJhdGNoTm9ybTJkKTpcbiAgICAgICAgICAgIG1vZHVsZS5ldmFsKCkgICAgICAgICAgICAgICAgICAgICAgICAjIGZyZWV6ZSBydW5uaW5nIHN0YXRzXG4gICAgICAgICAgICBtb2R1bGUud2VpZ2h0LnJlcXVpcmVzX2dyYWQgPSBUcnVlICAgIyBnYW1tYSBzdGlsbCBhZGFwdHNcbiAgICAgICAgICAgIG1vZHVsZS5iaWFzLnJlcXVpcmVzX2dyYWQgICA9IFRydWUgICAjIGJldGEgc3RpbGwgYWRhcHRzXG5cbm1vZGVsID0gbW9kZWxzLnJlc25ldDUwKHdlaWdodHM9bW9kZWxzLlJlc05ldDUwX1dlaWdodHMuSU1BR0VORVQxS19WMSlcbm1vZGVsLmZjID0gbm4uTGluZWFyKG1vZGVsLmZjLmluX2ZlYXR1cmVzLCA1KVxuXG5ibl9jb3VudCA9IHN1bSgxIGZvciBtIGluIG1vZGVsLm1vZHVsZXMoKSBpZiBpc2luc3RhbmNlKG0sIG5uLkJhdGNoTm9ybTJkKSlcbnByaW50KGZcIkJOIGxheWVycyBpbiBSZXNOZXQtNTA6IHtibl9jb3VudH1cIilcblxuIyBTaW11bGF0ZSB0cmFpbmluZyBsb29wIHN0ZXBcbm1vZGVsLnRyYWluKCkgICAgICAgICMgc2V0cyBhbGwgbGF5ZXJzIHRvIHRyYWluaW5nIG1vZGUgKEJOIHN0YXRzIHVwZGF0ZSlcbmZyZWV6ZV9ibl9zdGF0cyhtb2RlbCkgICMgaW1tZWRpYXRlbHkgZnJlZXplIEJOIHN0YXRzIGJhY2sgdG8gZXZhbCBtb2RlXG5cbmJuX2Zyb3plbiA9IHN1bSgxIGZvciBtIGluIG1vZGVsLm1vZHVsZXMoKVxuICAgICAgICAgICAgICAgIGlmIGlzaW5zdGFuY2UobSwgbm4uQmF0Y2hOb3JtMmQpIGFuZCBub3QgbS50cmFpbmluZylcbnByaW50KGZcIkFmdGVyIGZyZWV6ZV9ibl9zdGF0czoge2JuX2Zyb3plbn0ve2JuX2NvdW50fSBCTiBsYXllcnMgaW4gZXZhbCBtb2RlXCIpXG5wcmludChcIkJOIHJ1bm5pbmdfbWVhbi92YXIgcHJlc2VydmVkOyBnYW1tYS9iZXRhIHN0aWxsIGZpbmUtdHVuZWRcIilcbnByaW50KFwiV2l0aG91dCB0aGlzOiBJbWFnZU5ldCBCTiBzdGF0cyBhcmUgZGVzdHJveWVkIGJ5IHRhcmdldCBkaXN0cmlidXRpb25cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEb21haW4gQWRhcHRhdGlvbiBDb25zaWRlcmF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiB0aGUgc291cmNlIGRvbWFpbiAoSW1hZ2VOZXQpIGFuZCB0YXJnZXQgZG9tYWluIGRpZmZlciBzaWduaWZpY2FudGx5IOKAlCBlLmcuLCBncmF5c2NhbGUgbWVkaWNhbCBpbWFnZXMsIHNhdGVsbGl0ZSBpbWFnZXJ5LCBtaWNyb3Njb3B5IOKAlCBwcmV0cmFpbmVkIGZlYXR1cmVzIGFyZSBsZXNzIHRyYW5zZmVyYWJsZS4gSW4gdGhlc2UgY2FzZXM6ICgxKSBmaW5lLXR1bmUgYWxsIGxheWVycyB3aXRoIGEgc21hbGwgbGVhcm5pbmcgcmF0ZSAoMWUtNSkgZm9yIHRoZSBiYWNrYm9uZSBhbmQgYSBsYXJnZXIgcmF0ZSAoMWUtNCkgZm9yIHRoZSBoZWFkOyAoMikgdXNlIGxvbmdlciB0cmFpbmluZyAobW9yZSBlcG9jaHMpIHRvIGFsbG93IHRoZSBiYWNrYm9uZSB0byBhZGFwdDsgKDMpIGNvbnNpZGVyIGRvbWFpbi1zcGVjaWZpYyBwcmV0cmFpbmluZyBpZiBhdmFpbGFibGUgKGUuZy4sIFJhZEltYWdlTmV0IGZvciBtZWRpY2FsIGltYWdpbmcsIEdlb0FJIG1vZGVscyBmb3Igc2F0ZWxsaXRlIGRhdGEpOyAoNCkgYmF0Y2ggbm9ybWFsaXphdGlvbiBzdGF0aXN0aWNzIHNob3VsZCBkZWZpbml0ZWx5IGJlIGZyb3plbiBpbml0aWFsbHkgYW5kIHRoZW4gb3B0aW9uYWxseSBmaW5lLXR1bmVkIGluIGxhdGVyIGVwb2Nocy4gRm9yIGV4dHJlbWUgZG9tYWluIHNoaWZ0cyAoZS5nLiwgUkdCIHRvIGRlcHRoIGltYWdlcyksIHRyYWluaW5nIGZyb20gc2NyYXRjaCB3aXRoIGEgZ29vZCByYW5kb20gaW5pdGlhbGl6YXRpb24gKGUuZy4sIEthaW1pbmcpIG1heSBvdXRwZXJmb3JtIHRyYW5zZmVyIGxlYXJuaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYW5zZmVyIFN0cmF0ZWd5IFJlZmVyZW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJTdHJhdGVneSIsIkZyb3plbiBMYXllcnMiLCJUYXJnZXQgRGF0YXNldCBTaXplIiwiRG9tYWluIFNpbWlsYXJpdHkiLCJUcmFpbmluZyBTcGVlZCIsIlR5cGljYWwgQWNjdXJhY3kiXSwicm93cyI6W1siRmVhdHVyZSBleHRyYWN0aW9uIiwiQWxsIGNvbnYgbGF5ZXJzIiwiVmVyeSBzbWFsbCAoXHUwMDNjMUspIiwiSGlnaCAoc2ltaWxhciB0byBJbWFnZU5ldCkiLCJGYXN0ZXN0IiwiTW9kZXJhdGUiXSxbIkZpbmUtdHVuZSB0b3AgYmxvY2siLCJMYXllcnMgMeKAkzMiLCJTbWFsbCAoMUvigJMxMEspIiwiSGlnaCIsIkZhc3QiLCJHb29kIl0sWyJQcm9ncmVzc2l2ZSB1bmZyZWV6ZSIsIkxheWVyLWJ5LWxheWVyIGZyb20gdG9wIiwiTWVkaXVtICgxMEvigJMxMDBLKSIsIk1lZGl1bSIsIk1vZGVyYXRlIiwiVmVyeSBnb29kIl0sWyJGdWxsIGZpbmUtdHVuaW5nIiwiTm9uZSIsIkxhcmdlIChcdTAwM2UxMDBLKSIsIkFueSIsIlNsb3dlc3QiLCJCZXN0Il0sWyJUcmFpbiBmcm9tIHNjcmF0Y2giLCJOL0EgKHJhbmRvbSBpbml0KSIsIlZlcnkgbGFyZ2UgKFx1MDAzZTUwMEspIiwiTG93ICh2ZXJ5IGRpZmZlcmVudCkiLCJTbG93ZXN0IiwiQmVzdCBmb3IgZXh0cmVtZSBzaGlmdCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEd1aWRlbGluZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcmVsaWFibGUgdHJhbnNmZXIgbGVhcm5pbmcgd29ya2Zsb3c6ICgxKSBhbHdheXMgc3RhcnQgd2l0aCBmZWF0dXJlIGV4dHJhY3Rpb24gZm9yIGEgZmV3IGVwb2NocyB0byBzdGFiaWxpemUgdGhlIG5ldyBoZWFkIHdlaWdodHMgYmVmb3JlIHVuZnJlZXppbmcgYW55dGhpbmc7ICgyKSB1c2UgY29zaW5lIExSIHNjaGVkdWxlIHJhdGhlciB0aGFuIHN0ZXAgZGVjYXkg4oCUIGl0IHBhaXJzIGJldHRlciB3aXRoIGZpbmUtdHVuaW5nIGJlY2F1c2UgaXQgZG9lcyBub3QgYWJydXB0bHkgY2hhbmdlIHRoZSBMUjsgKDMpIGFwcGx5IGxhYmVsIHNtb290aGluZyAozrU9MC4xKSBhbmQgbW9kZXJhdGUgd2VpZ2h0IGRlY2F5ICgxZS00KSB0byBwcmV2ZW50IG92ZXJmaXR0aW5nIG9uIHNtYWxsIHRhcmdldCBkYXRhc2V0czsgKDQpIG1vbml0b3IgdmFsaWRhdGlvbiBsb3NzIGNhcmVmdWxseSDigJQgZmluZS10dW5pbmcgY2FuIG92ZXJmaXQgcXVpY2tseSB3aGVuIHRhcmdldCBkYXRhIGlzIHNtYWxsOyAoNSkgdXNlIG1peGVkIHByZWNpc2lvbiAodG9yY2guYXV0b2Nhc3QpIHRvIGZpdCBsYXJnZXIgYmF0Y2hlcywgd2hpY2ggc3RhYmlsaXplIEJOIHN0YXRpc3RpY3MgaWYgeW91IGNob29zZSB0byB1bmZyZWV6ZSBCTi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZlYXR1cmUgZXh0cmFjdGlvbjogZnJlZXplIGJhY2tib25lLCB0cmFpbiBoZWFkIG9ubHkg4oCUIGZhc3Rlc3QsIHdvcmtzIHdpdGggXHUwMDNjMTAwMCBzYW1wbGVzLiIsIkZpbmUtdHVuaW5nOiBsb3dlciBMUiBmb3IgYmFja2JvbmUgKDFlLTUpLCBoaWdoZXIgZm9yIGhlYWQgKDFlLTMpIOKAlCBiZXR0ZXIgYWNjdXJhY3kuIiwiUHJvZ3Jlc3NpdmUgdW5mcmVlemluZzogdW5mcmVlemUgdG9wLVx1MDAzZWJvdHRvbSwgb25lIGJsb2NrIHBlciBwaGFzZSDigJQgbW9zdCBzdGFibGUuIiwiRGlzY3JpbWluYXRpdmUgTFJzOiBlYXJsaWVyIGxheWVycyBnZXQgZXhwb25lbnRpYWxseSBsb3dlciBMUiAoM3ggc3RlcHMgcGVyIGdyb3VwKS4iLCJCYXRjaE5vcm06IGFsd2F5cyBjYWxsIGJuLmV2YWwoKSBhZnRlciBtb2RlbC50cmFpbigpIHRvIHByZXNlcnZlIEltYWdlTmV0IHN0YXRzLiIsIkRvbWFpbiBzaGlmdDogZXh0cmVtZSBzaGlmdCAobWVkaWNhbCwgc2F0ZWxsaXRlKSBvZnRlbiByZXF1aXJlcyBmdWxsIGZpbmUtdHVuaW5nIG9yIGRvbWFpbi1zcGVjaWZpYyBwcmV0cmFpbmluZy4iXX1d"
---
# Transfer Learning — Feature Extraction vs Fine-Tuning Strategies

Transfer learning is the practice of initializing a model with weights pretrained on a large dataset (typically ImageNet with 1.28M images and 1000 classes) and adapting it to a new task. Because early CNN layers learn universal low-level features (edges, textures, colors) and later layers learn increasingly task-specific features, pretrained weights provide a powerful starting point that dramatically reduces the data and compute required for the target task. The two primary transfer strategies — feature extraction and fine-tuning — differ in which layers are allowed to update during target training.

## Feature Extraction — Frozen Backbone

In feature extraction, all convolutional layers are frozen (requires_grad=False) and only the classification head is trained. The backbone acts as a fixed feature extractor: each image is mapped to a feature vector (e.g., 2048-dim for ResNet-50 after global avg pool), and a new linear classifier is trained on top of these frozen features. This is fast (only head params are optimized), memory-efficient (no gradients through the backbone), and works well when the target domain is visually similar to ImageNet. Feature extraction is the right choice when training data is very small (<1000 examples) or when the target task is similar to ImageNet classification.

## Fine-Tuning — Unfreezing Layers

In fine-tuning, some or all pretrained layers are unfrozen and allowed to update during target training. The key hyperparameter is the learning rate: pretrained layers should use a much lower learning rate (1e-5 to 1e-4) than the new head (1e-3), to preserve the learned representations while allowing them to shift slightly toward the target domain. Fine-tuning provides higher accuracy than feature extraction on most tasks because the backbone can adapt its higher-level features to the target distribution. It requires more training data (typically >5000 examples) and longer training to avoid overfitting.

## When to Use Which Strategy

- Very small dataset (<1000 samples), similar domain (e.g., pets, flowers) -> feature extraction only.
- Small dataset (1000-10000), similar domain -> fine-tune top 1-2 layers + head.
- Medium dataset (10000+), similar domain -> fine-tune all layers with small backbone LR.
- Large dataset (100000+), any domain -> fine-tune all layers or train from scratch.
- Very different domain (e.g., medical imaging, satellite) -> fine-tune all layers regardless of size.
- Low compute budget -> feature extraction (no backbone gradients, faster per step).

> **Always Freeze BatchNorm During Fine-Tuning**: BatchNorm layers maintain running statistics (mean and variance) estimated from training batches. When you call model.train() and fine-tune with small batches on a new domain, the running stats are updated to reflect the new distribution — destroying the statistics calibrated on ImageNet. Always call bn_module.eval() after model.train() to freeze the BN running stats. The affine parameters (gamma, beta) can still be updated. Forgetting this step often causes a significant accuracy drop, especially when the target batch size is small or the domain shift is large.

## Discriminative Learning Rates

Discriminative learning rates (Howard & Ruder, ULMFiT 2018) assign different learning rates to different layer groups: earlier layers (closer to the input) use lower learning rates, later layers use higher rates. The rationale: early layers contain more general, transferable features that should change little; later layers contain more task-specific features that need to adapt more. For ResNet-50, a typical schedule might be: layer1 LR = 1e-5, layer2 LR = 3e-5, layer3 LR = 1e-4, layer4 LR = 3e-4, fc LR = 1e-3 (a 10× step per group). This achieves better accuracy than a single LR for all layers.

## Code Examples

```python
import torch
import torch.nn as nn
from torchvision import models

def build_feature_extractor(num_classes: int):
    """Freeze all backbone params; only train the new classification head."""
    model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
    # Freeze all parameters
    for param in model.parameters():
        param.requires_grad = False
    # Replace final fully-connected layer
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    # fc is newly created so requires_grad=True by default
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total     = sum(p.numel() for p in model.parameters())
    print(f"Trainable: {trainable:,} / {total:,} ({100*trainable/total:.3f}%)")
    return model

model = build_feature_extractor(num_classes=10)
optimizer = torch.optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()), lr=1e-3
)
criterion = nn.CrossEntropyLoss()
print(f"Optimizer params: {sum(p.numel() for g in optimizer.param_groups for p in g['params']):,}")
print("Feature extraction: backbone is a fixed transform; only head params optimized")
```

```python
import torch
import torch.nn as nn
from torchvision import models

def make_discriminative_groups(model, base_lr=1e-5, lr_mult=3.0):
    """
    Discriminative LRs: earlier layers get lower LR to preserve pretrained features.
    Each deeper layer group uses lr_mult x higher LR than the previous.
    """
    groups = [
        {'params': model.layer1.parameters(), 'lr': base_lr},
        {'params': model.layer2.parameters(), 'lr': base_lr * lr_mult},
        {'params': model.layer3.parameters(), 'lr': base_lr * lr_mult**2},
        {'params': model.layer4.parameters(), 'lr': base_lr * lr_mult**3},
        {'params': model.fc.parameters(),     'lr': base_lr * lr_mult**4},
    ]
    return groups

model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
model.fc = nn.Linear(model.fc.in_features, 10)

groups = make_discriminative_groups(model, base_lr=1e-5, lr_mult=3.0)
optimizer = torch.optim.Adam(groups)

names = ['layer1', 'layer2', 'layer3', 'layer4', 'fc']
print('Discriminative learning rates:')
for name, g in zip(names, groups):
    n = sum(p.numel() for p in g['params'])
    print(f"  {name:<10}: lr={g['lr']:.1e}  ({n:,} params)")
print('Earlier layers use lower LR -- pretrained features preserved more strongly')
```

```python
import torch
import torch.nn as nn
from torchvision import models

def set_requires_grad_from(model, layer_name: str):
    """Freeze all layers before layer_name; unfreeze from layer_name onward."""
    unfreezing = False
    for name, param in model.named_parameters():
        if layer_name in name:
            unfreezing = True
        param.requires_grad = unfreezing
    n = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"  Unfrozen from '{layer_name}': {n:,} trainable params")

model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
model.fc = nn.Linear(model.fc.in_features, 10)

# Epoch 1-5: head only (feature extraction warmup)
for p in model.parameters(): p.requires_grad = False
for p in model.fc.parameters(): p.requires_grad = True
print("Epoch 1-5 (head only):")
print(f"  Trainable: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")

# Epoch 6-10: unfreeze layer4 (deepest residual block)
print("Epoch 6-10:")
set_requires_grad_from(model, 'layer4')

# Epoch 11-15: unfreeze layer3
print("Epoch 11-15:")
set_requires_grad_from(model, 'layer3')

# Epoch 16+: full fine-tuning
for p in model.parameters(): p.requires_grad = True
print("Epoch 16+ (full):")
print(f"  Trainable: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")
```

```python
import torch
import torch.nn as nn
from torchvision import models

def freeze_bn_stats(model: nn.Module):
    """
    Keep BN layers in eval mode to freeze running_mean/running_var.
    Affine params (weight=gamma, bias=beta) remain trainable.
    Call this AFTER model.train() in each training iteration.
    """
    for module in model.modules():
        if isinstance(module, nn.BatchNorm2d):
            module.eval()                        # freeze running stats
            module.weight.requires_grad = True   # gamma still adapts
            module.bias.requires_grad   = True   # beta still adapts

model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
model.fc = nn.Linear(model.fc.in_features, 5)

bn_count = sum(1 for m in model.modules() if isinstance(m, nn.BatchNorm2d))
print(f"BN layers in ResNet-50: {bn_count}")

# Simulate training loop step
model.train()        # sets all layers to training mode (BN stats update)
freeze_bn_stats(model)  # immediately freeze BN stats back to eval mode

bn_frozen = sum(1 for m in model.modules()
                if isinstance(m, nn.BatchNorm2d) and not m.training)
print(f"After freeze_bn_stats: {bn_frozen}/{bn_count} BN layers in eval mode")
print("BN running_mean/var preserved; gamma/beta still fine-tuned")
print("Without this: ImageNet BN stats are destroyed by target distribution")
```

## Domain Adaptation Considerations

When the source domain (ImageNet) and target domain differ significantly — e.g., grayscale medical images, satellite imagery, microscopy — pretrained features are less transferable. In these cases: (1) fine-tune all layers with a small learning rate (1e-5) for the backbone and a larger rate (1e-4) for the head; (2) use longer training (more epochs) to allow the backbone to adapt; (3) consider domain-specific pretraining if available (e.g., RadImageNet for medical imaging, GeoAI models for satellite data); (4) batch normalization statistics should definitely be frozen initially and then optionally fine-tuned in later epochs. For extreme domain shifts (e.g., RGB to depth images), training from scratch with a good random initialization (e.g., Kaiming) may outperform transfer learning.

## Transfer Strategy Reference

| Strategy | Frozen Layers | Target Dataset Size | Domain Similarity | Training Speed | Typical Accuracy |
| --- | --- | --- | --- | --- | --- |
| Feature extraction | All conv layers | Very small (<1K) | High (similar to ImageNet) | Fastest | Moderate |
| Fine-tune top block | Layers 1–3 | Small (1K–10K) | High | Fast | Good |
| Progressive unfreeze | Layer-by-layer from top | Medium (10K–100K) | Medium | Moderate | Very good |
| Full fine-tuning | None | Large (>100K) | Any | Slowest | Best |
| Train from scratch | N/A (random init) | Very large (>500K) | Low (very different) | Slowest | Best for extreme shift |

## Practical Guidelines

A reliable transfer learning workflow: (1) always start with feature extraction for a few epochs to stabilize the new head weights before unfreezing anything; (2) use cosine LR schedule rather than step decay — it pairs better with fine-tuning because it does not abruptly change the LR; (3) apply label smoothing (ε=0.1) and moderate weight decay (1e-4) to prevent overfitting on small target datasets; (4) monitor validation loss carefully — fine-tuning can overfit quickly when target data is small; (5) use mixed precision (torch.autocast) to fit larger batches, which stabilize BN statistics if you choose to unfreeze BN.

- Feature extraction: freeze backbone, train head only — fastest, works with <1000 samples.
- Fine-tuning: lower LR for backbone (1e-5), higher for head (1e-3) — better accuracy.
- Progressive unfreezing: unfreeze top->bottom, one block per phase — most stable.
- Discriminative LRs: earlier layers get exponentially lower LR (3x steps per group).
- BatchNorm: always call bn.eval() after model.train() to preserve ImageNet stats.
- Domain shift: extreme shift (medical, satellite) often requires full fine-tuning or domain-specific pretraining.

