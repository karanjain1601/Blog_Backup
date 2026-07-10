---
title: "ALiBi — Attention with Linear Biases for Length Generalization"
slug: "alibi-attention-bias"
description: "How ALiBi (Press et al. 2022) replaces positional embeddings with per-head linear distance penalties on attention logits, enabling train-short-test-long generalisation used in BLOOM-176B and MPT."
tags: ["deep-learning", "transformers", "positional-encoding"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQUxpQmkgKEF0dGVudGlvbiB3aXRoIExpbmVhciBCaWFzZXMpLCBpbnRyb2R1Y2VkIGJ5IFByZXNzIGV0IGFsLiAoMjAyMiksIHRha2VzIGEgcmFkaWNhbGx5IHNpbXBsZSBhcHByb2FjaCB0byBwb3NpdGlvbmFsIGVuY29kaW5nOiAqZG8gbm90IGFkZCBhbnkgcG9zaXRpb25hbCBpbmZvcm1hdGlvbiB0byB0aGUgdG9rZW4gZW1iZWRkaW5ncyBhdCBhbGwqLiBJbnN0ZWFkLCBzdWJ0cmFjdCBhIGxpbmVhciBiaWFzIGZyb20gdGhlIHJhdyBhdHRlbnRpb24gbG9naXRzIGF0IGV2ZXJ5IGxheWVyIGFuZCBldmVyeSBoZWFkLiBUaGUgYmlhcyBwZW5hbGlzZXMgYXR0ZW50aW9uIHRvIGRpc3RhbnQgdG9rZW5zIGluIHByb3BvcnRpb24gdG8gdGhlaXIgZGlzdGFuY2UsIGdpdmluZyBlYWNoIGhlYWQgYSBidWlsdC1pbiByZWNlbmN5IHByZWZlcmVuY2Ug4oCUIHplcm8gbGVhcm5lZCBwb3NpdGlvbmFsIHBhcmFtZXRlcnMsIHplcm8gZW1iZWRkaW5nIGxvb2t1cCwgYW5kIGEgZm9ybXVsYSB0aGF0IHJlbWFpbnMgdmFsaWQgYXQgYW55IHNlcXVlbmNlIGxlbmd0aC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgQUxpQmkgTWVjaGFuaXNtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBzdGFuZGFyZCBzY2FsZWQgZG90LXByb2R1Y3QgYXR0ZW50aW9uIHRoZSBsb2dpdCBmb3IgcXVlcnkgcG9zaXRpb24gaSBhdHRlbmRpbmcgdG8ga2V5IHBvc2l0aW9uIGogaXMgUeG1okvisbzhtYAgLyDiiJpkX2suIEFMaUJpIG1vZGlmaWVzIHRoaXMgdG86IHNjb3JlX2FsaWJpKGksIGopID0gUeG1okvisbzhtYAgLyDiiJpkX2sg4oiSIG3Ct3xpIOKIkiBqfCwgd2hlcmUgbSBpcyBhIGhlYWQtc3BlY2lmaWMgc2xvcGUuIFRoZSBiaWFzIHRlcm0gZGVwZW5kcyBvbmx5IG9uIHRoZSAqcmVsYXRpdmUqIGRpc3RhbmNlIHxpIOKIkiBqfCwgbm90IG9uIGFic29sdXRlIHBvc2l0aW9uIHZhbHVlcy4gQ3J1Y2lhbGx5LCB0aGlzIG1lYW5zIHRoZSBiaWFzIGlzIHZhbGlkIGF0IGFueSBhYnNvbHV0ZSBwb3NpdGlvbiDigJQgaW5jbHVkaW5nIHBvc2l0aW9ucyAxMDI1LCAyMDQ4LCBvciA4MTkyIHRoYXQgd2VyZSBuZXZlciBzZWVuIGR1cmluZyB0cmFpbmluZyBvbiAxMDI0LXRva2VuIHNlcXVlbmNlcy4gTm8gbmV3IGVtYmVkZGluZyByb3dzIGFyZSBuZWVkZWQgZm9yIHVuc2VlbiBwb3NpdGlvbnM7IHRoZSBkaXN0YW5jZSBmb3JtdWxhIGV4dHJhcG9sYXRlcyBhdXRvbWF0aWNhbGx5LiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50IjoiXFx0ZXh0e3Njb3JlXFxfYWxpYml9KGksaikgPSBcXGZyYWN7UV9pIEtfal57XFx0b3B9fXtcXHNxcnR7ZF9rfX0gLSBtIFxcY2RvdCB8aSAtIGp8In0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR2VvbWV0cmljIFNsb3BlcyBwZXIgSGVhZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWFjaCBhdHRlbnRpb24gaGVhZCB1c2VzIGEgZGlmZmVyZW50IHNsb3BlIG0gZHJhd24gZnJvbSBhIGdlb21ldHJpYyBzZXF1ZW5jZS4gRm9yIGggaGVhZHMsIHRoZSBzbG9wZXMgYXJlOiBtX2sgPSAyXnviiJI4ay9ofSBmb3IgayA9IDEsIOKApiwgaC4gVGhpcyBnaXZlcyBhIHNlcXVlbmNlIGZyb20gMl574oiSOC9ofSAoc2hhbGxvd2VzdCwgZ2xvYmFsIGhlYWQpIGRvd24gdG8gMl574oiSOH0gKHN0ZWVwZXN0LCBsb2NhbCBoZWFkKSDigJQgdGhlIHBhcGVyIHJldmVyc2VzIHRoZSBpbmRleGluZyBzbyBoZWFkIDEgaXMgc3RlZXBlc3QgYW5kIHRoZSBsYXN0IGhlYWQgaXMgc2hhbGxvd2VzdC4gSGVhZCAxIHNoYXJwbHkgcGVuYWxpc2VzIGRpc3RhbmNlOyBhIHRva2VuIGF0IGRpc3RhbmNlIDEwIHJlY2VpdmVzIGEgYmlhcyBvZiDiiJIxMG3igoEgd2hpY2ggaXMgdmVyeSBuZWdhdGl2ZS4gVGhlIGxhc3QgaGVhZFx1MDAyN3Mgc2hhbGxvdyBzbG9wZSBtZWFucyBkaXN0YW50IHRva2VucyBzdGlsbCByZWNlaXZlIG5lYXItemVybyBiaWFzIGFuZCBjYW4gY29udHJpYnV0ZSBtZWFuaW5nZnVsbHkuIFRoaXMgZGl2ZXJzaXR5IGxldHMgdGhlIG1vZGVsIGNhcHR1cmUgYm90aCBsb2NhbCBzeW50YWN0aWMgY3VlcyBhbmQgbG9uZy1yYW5nZSBzZW1hbnRpYyBkZXBlbmRlbmNpZXMgc2ltdWx0YW5lb3VzbHkgYWNyb3NzIGhlYWRzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiSGVhZCAxIChzdGVlcGVzdCBzbG9wZSBtID0gMl57LTh9KTogZWZmZWN0aXZlbHkgYSBsb2NhbCBhdHRlbnRpb24gd2luZG93IG9mIGEgZmV3IHRva2VucyIsIkhlYWQgaCAoc2hhbGxvd2VzdCBzbG9wZSBtID0gMl57LTgvaH0pOiBjYW4gYXR0ZW5kIGdsb2JhbGx5IHdpdGggc21hbGwgZGlzdGFuY2UgcGVuYWx0eSIsIlNsb3BlcyBhcmUgZml4ZWQgYXQgaW5pdGlhbGlzYXRpb24g4oCUIG5ldmVyIHVwZGF0ZWQgYnkgZ3JhZGllbnQgZGVzY2VudCIsIkJpYXMgaXMgYSBsb3dlci10cmlhbmd1bGFyIG1hdHJpeCBjb21iaW5lZCB3aXRoIHRoZSBjYXVzYWwgbWFzayBhdCBlYWNoIGxheWVyIiwiVGhlIGJpYXMgdGVuc29yIGlzIGNvbXB1dGVkIG9uLXRoZS1mbHkgZm9yIGVhY2ggc2VxdWVuY2UgbGVuZ3RoIOKAlCBubyBtYXgtbGVuZ3RoIGNhcCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIEFMaUJpIEJpYXMgQ29tcHV0YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbXB1dGluZyB0aGUgZ2VvbWV0cmljIHNsb3BlIHNlcXVlbmNlIGFuZCBidWlsZGluZyB0aGUgZnVsbCAobl9oZWFkcyDDlyBzZXFfbGVuIMOXIHNlcV9sZW4pIGJpYXMgdGVuc29yLiBUaGUgaW1wbGVtZW50YXRpb24gaGFuZGxlcyBub24tcG93ZXItb2YtMiBoZWFkIGNvdW50cyBieSBpbnRlcnBvbGF0aW5nIGV4dHJhIGludGVybWVkaWF0ZSBzbG9wZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG1hdGhcblxuXG5kZWYgZ2V0X2FsaWJpX3Nsb3BlcyhuX2hlYWRzOiBpbnQpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIkdlb21ldHJpYyBzZXF1ZW5jZTogezJeey04L2h9LCAyXnstOCoyL2h9LCAuLi4sIDJeey04fX0gZm9yIGggaGVhZHMuXCJcIlwiXG4gICAgIyBVc2UgbGFyZ2VzdCBwb3dlciBvZiAyIFx1MDAzYz0gbl9oZWFkcyBhcyB0aGUgYmFzZSBjb3VudFxuICAgIG4gPSAyICoqIG1hdGguZmxvb3IobWF0aC5sb2cyKG5faGVhZHMpKVxuICAgIG0wID0gMiAqKiAoLTggLyBuKSAgICAgICAgICAgICAgICAgICAgICAgICAgICMgYmFzZSBzdGVwIHJhdGlvXG4gICAgc2xvcGVzID0gdG9yY2gudGVuc29yKFttMCAqKiBpIGZvciBpIGluIHJhbmdlKDEsIG4gKyAxKV0sIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgaWYgbiBcdTAwM2Mgbl9oZWFkczogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBub24tcG93ZXItb2YtMjogaW50ZXJwb2xhdGUgZXh0cmFzXG4gICAgICAgIGV4dHJhID0gdG9yY2gudGVuc29yKFxuICAgICAgICAgICAgW20wICoqIChpIC8gMikgZm9yIGkgaW4gcmFuZ2UoMSwgMiAqIChuX2hlYWRzIC0gbikgKyAxLCAyKV0sXG4gICAgICAgICAgICBkdHlwZT10b3JjaC5mbG9hdDMyLFxuICAgICAgICApXG4gICAgICAgIHNsb3BlcyA9IHRvcmNoLmNhdChbc2xvcGVzLCBleHRyYV0sIGRpbT0wKVxuICAgIHJldHVybiBzbG9wZXMgICMgc2hhcGUgKG5faGVhZHMsKVxuXG5cbmRlZiBjb21wdXRlX2FsaWJpX2JpYXMobl9oZWFkczogaW50LCBzZXFfbGVuOiBpbnQpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlJldHVybiBBTGlCaSBiaWFzIHRlbnNvciBvZiBzaGFwZSAobl9oZWFkcywgc2VxX2xlbiwgc2VxX2xlbikuXCJcIlwiXG4gICAgc2xvcGVzID0gZ2V0X2FsaWJpX3Nsb3BlcyhuX2hlYWRzKSAgICAgICAgICAgICMgKEgsKVxuICAgIHBvcyAgICA9IHRvcmNoLmFyYW5nZShzZXFfbGVuLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgIGRpc3QgICA9IChwb3MudW5zcXVlZXplKDApIC0gcG9zLnVuc3F1ZWV6ZSgxKSkuYWJzKCkgICAjIHxpLWp8IG1hdHJpeCAoTCwgTClcbiAgICAjIChILCAxLCAxKSAqICgxLCBMLCBMKSA9XHUwMDNlIChILCBMLCBMKVxuICAgIHJldHVybiAtc2xvcGVzLnZpZXcobl9oZWFkcywgMSwgMSkgKiBkaXN0LnVuc3F1ZWV6ZSgwKVxuXG5cbiMgRXhhbXBsZTogOCBoZWFkcywgc2VxdWVuY2UgbGVuZ3RoIDE2XG5iaWFzICAgPSBjb21wdXRlX2FsaWJpX2JpYXMoOCwgMTYpXG5zbG9wZXMgPSBnZXRfYWxpYmlfc2xvcGVzKDgpXG5wcmludChcIkJpYXMgc2hhcGU6XCIsIGJpYXMuc2hhcGUpICAgICAgICAgICAgICAgICAgIyAoOCwgMTYsIDE2KVxucHJpbnQoXCJTbG9wZXM6XCIsIHNsb3Blcy5udW1weSgpLnJvdW5kKDUpKVxucHJpbnQoXCJIZWFkIDAgYmlhcyBhdCBkaXN0PTggKHN0ZWVwZXN0KTpcIiwgIGJpYXNbMCwgOCwgMF0uaXRlbSgpKVxucHJpbnQoXCJIZWFkIDcgYmlhcyBhdCBkaXN0PTggKHNoYWxsb3dlc3QpOlwiLCBiaWFzWzcsIDgsIDBdLml0ZW0oKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIEFMaUJpIEluc2lkZSBNdWx0aS1IZWFkIEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW50ZWdyYXRpbmcgdGhlIEFMaUJpIGJpYXMgdGVuc29yIGludG8gYSBmdWxsIG11bHRpLWhlYWQgYXR0ZW50aW9uIG1vZHVsZS4gVGhlIGJpYXMgaXMgYWRkZWQgdG8gcmF3IGF0dGVudGlvbiBsb2dpdHMgKmJlZm9yZSogc29mdG1heC4gTm8gbW9kaWZpY2F0aW9uIHRvIFEsIEssIG9yIFYgcHJvamVjdGlvbnMgaXMgbmVlZGVkIOKAlCB0aGUgdG9rZW4gZW1iZWRkaW5ncyByZW1haW4gcG9zaXRpb24tZnJlZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBtYXRoXG5cblxuY2xhc3MgQUxpQmlNdWx0aUhlYWRBdHRlbnRpb24obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJNdWx0aS1oZWFkIGF0dGVudGlvbiB0aGF0IHVzZXMgQUxpQmkgbG9naXQgYmlhc2VzIGluc3RlYWQgb2YgcG9zaXRpb25hbCBlbWJlZGRpbmdzLlwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgbl9oZWFkczogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGFzc2VydCBkX21vZGVsICUgbl9oZWFkcyA9PSAwXG4gICAgICAgIHNlbGYubl9oZWFkcyA9IG5faGVhZHNcbiAgICAgICAgc2VsZi5kX2sgID0gZF9tb2RlbCAvLyBuX2hlYWRzXG4gICAgICAgIHNlbGYucWt2ICA9IG5uLkxpbmVhcihkX21vZGVsLCAzICogZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNsb3BlcyA9IHNlbGYuX21ha2Vfc2xvcGVzKG5faGVhZHMpXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFwic2xvcGVzXCIsIHNsb3BlcykgICAjIGZpeGVkLCBuZXZlciB0cmFpbmVkXG5cbiAgICBAc3RhdGljbWV0aG9kXG4gICAgZGVmIF9tYWtlX3Nsb3BlcyhuOiBpbnQpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBiYXNlID0gMiAqKiAoLTggLyAoMiAqKiBtYXRoLmZsb29yKG1hdGgubG9nMihuKSkpKVxuICAgICAgICByZXR1cm4gdG9yY2gudGVuc29yKFtiYXNlICoqIGkgZm9yIGkgaW4gcmFuZ2UoMSwgbiArIDEpXSwgZHR5cGU9dG9yY2guZmxvYXQzMilcblxuICAgIGRlZiBfYWxpYmlfYmlhcyhzZWxmLCBzZXFfbGVuOiBpbnQpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBwb3MgID0gdG9yY2guYXJhbmdlKHNlcV9sZW4sIGRldmljZT1zZWxmLnNsb3Blcy5kZXZpY2UsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgICAgIGRpc3QgPSAocG9zLnVuc3F1ZWV6ZSgwKSAtIHBvcy51bnNxdWVlemUoMSkpLmFicygpICAgICAgICAgICMgKEwsIEwpXG4gICAgICAgIHJldHVybiAtc2VsZi5zbG9wZXMudmlldygtMSwgMSwgMSkgKiBkaXN0LnVuc3F1ZWV6ZSgwKSAgICAgICMgKEgsIEwsIEwpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IsIGNhdXNhbDogYm9vbCA9IFRydWUpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBCLCBMLCBfID0geC5zaGFwZVxuICAgICAgICBxa3YgPSBzZWxmLnFrdih4KS5yZXNoYXBlKEIsIEwsIDMsIHNlbGYubl9oZWFkcywgc2VsZi5kX2spLnBlcm11dGUoMiwgMCwgMywgMSwgNClcbiAgICAgICAgUSwgSywgViA9IHFrdlswXSwgcWt2WzFdLCBxa3ZbMl1cbiAgICAgICAgc2NvcmVzID0gdG9yY2gubWF0bXVsKFEsIEsudHJhbnNwb3NlKC0yLCAtMSkpIC8gbWF0aC5zcXJ0KHNlbGYuZF9rKVxuICAgICAgICBzY29yZXMgPSBzY29yZXMgKyBzZWxmLl9hbGliaV9iaWFzKEwpICAgICMgXHUwMDNjLS0gQUxpQmkgYmlhcyBpbmplY3RlZCBoZXJlXG4gICAgICAgIGlmIGNhdXNhbDpcbiAgICAgICAgICAgIG1hc2sgPSB0b3JjaC50cml1KHRvcmNoLm9uZXMoTCwgTCwgZGV2aWNlPXguZGV2aWNlKSwgZGlhZ29uYWw9MSkuYm9vbCgpXG4gICAgICAgICAgICBzY29yZXMgPSBzY29yZXMubWFza2VkX2ZpbGwobWFzaywgZmxvYXQoXCItaW5mXCIpKVxuICAgICAgICBvdXQgPSB0b3JjaC5tYXRtdWwoRi5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKSwgVilcbiAgICAgICAgcmV0dXJuIHNlbGYucHJvaihvdXQudHJhbnNwb3NlKDEsIDIpLnJlc2hhcGUoQiwgTCwgLTEpKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUmVjZW5jeSBCaWFzIElzIEJ1aWx0IEluIiwiY29udGVudCI6IkFMaUJpXHUwMDI3cyBsaW5lYXIgcGVuYWx0eSBjcmVhdGVzIGEgZml4ZWQgcmVjZW5jeSBhZHZhbnRhZ2U6IHRoZSBpbW1lZGlhdGVseSBwcmVjZWRpbmcgdG9rZW4gKGRpc3RhbmNlIDEpIHJlY2VpdmVzIGEgYmlhcyBvZiDiiJJtLCB3aGlsZSBhIHRva2VuIGF0IGRpc3RhbmNlIDEwMCByZWNlaXZlcyDiiJIxMDBtLiBUaGlzIGlzIGEgaGFyZGNvZGVkIGluZHVjdGl2ZSBiaWFzIOKAlCB0aGUgbW9kZWwgY2Fubm90IGxlYXJuIHRvIGF0dGVuZCB1bmlmb3JtbHkgYXQgYWxsIGRpc3RhbmNlcy4gRm9yIHJldHJpZXZhbC1zdHlsZSB0YXNrcyB3aGVyZSBhIHJlbGV2YW50IHRva2VuIG1heSBiZSBmYXIgYXdheSBhbmQgbmVlZHMgaGlnaCBhdHRlbnRpb24gd2VpZ2h0IHJlZ2FyZGxlc3Mgb2YgcG9zaXRpb24sIHRoaXMgbW9ub3RvbmljIGRlY2F5IGlzIGEgbWVhbmluZ2Z1bCBsaW1pdGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluIFNob3J0LCBUZXN0IExvbmcg4oCUIEV4dHJhcG9sYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjcml0aWNhbCBhZHZhbnRhZ2Ugb2YgQUxpQmkgb3ZlciBzaW51c29pZGFsIGFuZCBsZWFybmVkIHBvc2l0aW9uYWwgZW1iZWRkaW5ncyBpcyBpdHMgYmVoYXZpb3VyIGF0IHNlcXVlbmNlIGxlbmd0aHMgYmV5b25kIHRoZSB0cmFpbmluZyB3aW5kb3cuIFNpbnVzb2lkYWwgUEUgaXMgdGhlb3JldGljYWxseSB1bmJvdW5kZWQgYnV0IGludHJvZHVjZXMgYSBkaXN0cmlidXRpb24gc2hpZnQgYXQgaW5mZXJlbmNlIGJlY2F1c2UgdGhlIG1vZGVsIHJhcmVseSBzZWVzIHRoZSBsb25nZXN0LXJhbmdlIHNpbnVzb2lkYWwgcGF0dGVybnMgZHVyaW5nIHRyYWluaW5nLiBMZWFybmVkIFBFIGNhbm5vdCBnZW5lcmFsaXNlIGF0IGFsbCB0byBwb3NpdGlvbnMgYmV5b25kIG1heF90cmFpbl9sZW4uIEFMaUJpXHUwMDI3cyBiaWFzIGRlcGVuZHMgb25seSBvbiByZWxhdGl2ZSBkaXN0YW5jZSwgc28gZXZhbHVhdGluZyBhdCBsZW5ndGggMjA0OCB3aGVuIHRyYWluZWQgb24gMTAyNCB0b2tlbnMgaXMgaGFuZGxlZCBzZWFtbGVzc2x5OiB0aGUgbWF4aW11bSBkaXN0YW5jZSBpbmNyZWFzZXMsIGJ1dCB0aGUgZm9ybXVsYSBpcyB1bmNoYW5nZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBtYXRoXG5cbiMgQXBwcm94aW1hdGUgcGVycGxleGl0eSByZXN1bHRzIGZyb20gUHJlc3MgZXQgYWwuICgyMDIyKSBUYWJsZSAxXG4jIEFsbCBtb2RlbHMgdHJhaW5lZCBvbiBzZXF1ZW5jZXMgb2YgbGVuZ3RoIDEwMjQgKFdpa2lUZXh0LTEwMylcblxudHJhaW5fbGVuID0gMTAyNFxudGVzdF9sZW5zICA9IFs1MTIsIDEwMjQsIDIwNDgsIDQwOTYsIDgxOTJdXG5cbnJlc3VsdHMgPSB7XG4gICAgXCJTaW51c29pZGFsIFBFXCI6IHs1MTI6IDE3LjUsIDEwMjQ6IDE3LjgsIDIwNDg6IDIzLjksIDQwOTY6IDM4LjQsIDgxOTI6IGZsb2F0KFwiaW5mXCIpfSxcbiAgICBcIkxlYXJuZWQgUEVcIjogICAgezUxMjogMTcuMywgMTAyNDogMTcuNiwgMjA0ODogZmxvYXQoXCJpbmZcIiksIDQwOTY6IGZsb2F0KFwiaW5mXCIpLCA4MTkyOiBmbG9hdChcImluZlwiKX0sXG4gICAgXCJBTGlCaVwiOiAgICAgICAgIHs1MTI6IDE3LjYsIDEwMjQ6IDE3LjksIDIwNDg6IDE4LjMsIDQwOTY6IDE5LjAsIDgxOTI6IDIwLjV9LFxufVxuXG5wcmludChmXCJQZXJwbGV4aXR5IGF0IFZhcmlvdXMgTGVuZ3RocyAodHJhaW5lZCBvbiB7dHJhaW5fbGVufSB0b2tlbnMpXCIpXG5wcmludChmXCJ7XHUwMDI3TGVuZ3RoXHUwMDI3Olx1MDAzYzEwfVwiLCBlbmQ9XCJcIilcbmZvciBuYW1lIGluIHJlc3VsdHM6XG4gICAgcHJpbnQoZlwie25hbWU6XHUwMDNjMjB9XCIsIGVuZD1cIlwiKVxucHJpbnQoKVxucHJpbnQoXCItXCIgKiA3MClcblxuZm9yIEwgaW4gdGVzdF9sZW5zOlxuICAgIHRhZyA9IFwiICAodHJhaW4pXCIgaWYgTCA9PSB0cmFpbl9sZW4gZWxzZSBcIiAgT09EXCIgaWYgTCBcdTAwM2UgdHJhaW5fbGVuIGVsc2UgXCJcIlxuICAgIHByaW50KGZcIntMOlx1MDAzYzEwfVwiLCBlbmQ9XCJcIilcbiAgICBmb3IgbmFtZSwgcHBsX21hcCBpbiByZXN1bHRzLml0ZW1zKCk6XG4gICAgICAgIHZhbCA9IHBwbF9tYXAuZ2V0KEwsIGZsb2F0KFwibmFuXCIpKVxuICAgICAgICBzICAgPSBcImluZlwiIGlmIG1hdGguaXNpbmYodmFsKSBlbHNlIGZcInt2YWw6LjFmfVwiXG4gICAgICAgIHByaW50KGZcIntzOlx1MDAzYzIwfVwiLCBlbmQ9XCJcIilcbiAgICBwcmludCh0YWcpXG5cbnByaW50KClcbnByaW50KFwiQUxpQmkgZGVncmFkZXMgZ3JhY2VmdWxseS4gTGVhcm5lZCBQRSBmYWlscyBjb21wbGV0ZWx5IGF0IE9PRCBsZW5ndGhzLlwiKVxucHJpbnQoXCJTaW51c29pZGFsIFBFIGRlZ3JhZGVzIHNoYXJwbHkgYmV5b25kIDJ4IHRyYWluaW5nIGxlbmd0aC5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDQg4oCUIFBlci1IZWFkIFNsb3BlIFZpc3VhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZpc3VhbGlzaW5nIGhvdyBlYWNoIGhlYWRcdTAwMjdzIHNsb3BlIGNvbnRyb2xzIHRoZSBlZmZlY3RpdmUgYXR0ZW50aW9uIHdpbmRvdyBzaXplLiBBIHN0ZWVwIHNsb3BlIG1ha2VzIHRoZSBtb2RlbCB0aWdodGx5IGxvY2FsbHkgZm9jdXNlZDsgYSBzaGFsbG93IHNsb3BlIGFsbG93cyBnbG9iYWxseSBkaXN0cmlidXRlZCBhdHRlbnRpb24gb3ZlciBodW5kcmVkcyBvZiB0b2tlbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBtYXRoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuXG5kZWYgZ2V0X2FsaWJpX3Nsb3BlcyhuX2hlYWRzOiBpbnQpIC1cdTAwM2UgbGlzdDpcbiAgICBuICA9IDIgKiogbWF0aC5mbG9vcihtYXRoLmxvZzIobl9oZWFkcykpXG4gICAgbTAgPSAyICoqICgtOCAvIG4pXG4gICAgc2xvcGVzID0gW20wICoqIGkgZm9yIGkgaW4gcmFuZ2UoMSwgbiArIDEpXVxuICAgIGlmIG4gXHUwMDNjIG5faGVhZHM6XG4gICAgICAgIHNsb3BlcyArPSBbbTAgKiogKGkgLyAyKSBmb3IgaSBpbiByYW5nZSgxLCAyICogKG5faGVhZHMgLSBuKSArIDEsIDIpXVxuICAgIHJldHVybiBzbG9wZXNcblxuXG5uX2hlYWRzICAgPSA4XG5tYXhfZGlzdCAgPSA2NFxuc2xvcGVzICAgID0gZ2V0X2FsaWJpX3Nsb3BlcyhuX2hlYWRzKVxuZGlzdGFuY2VzID0gbnAuYXJhbmdlKG1heF9kaXN0KVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMiwgNCwgZmlnc2l6ZT0oMTQsIDUpLCBzaGFyZXk9VHJ1ZSlcbmF4ZXMgPSBheGVzLmZsYXR0ZW4oKVxuZm9yIGgsIChheCwgbSkgaW4gZW51bWVyYXRlKHppcChheGVzLCBzbG9wZXMpKTpcbiAgICBiaWFzID0gLW0gKiBkaXN0YW5jZXNcbiAgICBheC5wbG90KGRpc3RhbmNlcywgYmlhcywgY29sb3I9ZlwiQ3tofVwiLCBsaW5ld2lkdGg9MilcbiAgICBheC5zZXRfdGl0bGUoZlwiSGVhZCB7aCsxfSAgbT17bTouNWZ9XCIsIGZvbnRzaXplPTkpXG4gICAgYXguc2V0X3hsYWJlbChcInxpIC0ganwgZGlzdGFuY2VcIilcbiAgICBpZiBoICUgNCA9PSAwOlxuICAgICAgICBheC5zZXRfeWxhYmVsKFwibG9naXQgYmlhc1wiKVxucGx0LnN1cHRpdGxlKFwiQUxpQmkgUGVyLUhlYWQgTGluZWFyIERlY2F5ICg4IGhlYWRzKVwiLCBmb250c2l6ZT0xMiwgeT0xLjAxKVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcImFsaWJpX3Nsb3Blcy5wbmdcIiwgZHBpPTEyMCwgYmJveF9pbmNoZXM9XCJ0aWdodFwiKVxuXG5wcmludChmXCJ7XHUwMDI3SGVhZFx1MDAyNzpcdTAwM2M4fXtcdTAwMjdTbG9wZSBtXHUwMDI3Olx1MDAzYzE1fXtcdTAwMjdiaWFzIGF0IGRpc3Q9MTBcdTAwMjc6XHUwMDNjMjB9e1x1MDAyN0F0dGVudGlvbiBjaGFyYWN0ZXJcdTAwMjd9XCIpXG5wcmludChcIi1cIiAqIDU4KVxuY2hhcnMgPSBbXCJWZXJ5IGxvY2FsXCIsIFwiTG9jYWxcIiwgXCJMb2NhbFwiLCBcIk1vZGVyYXRlXCIsXG4gICAgICAgICBcIk1vZGVyYXRlXCIsIFwiU2VtaS1nbG9iYWxcIiwgXCJTZW1pLWdsb2JhbFwiLCBcIkdsb2JhbFwiXVxuZm9yIGgsIChtLCBjKSBpbiBlbnVtZXJhdGUoemlwKHNsb3BlcywgY2hhcnMpKTpcbiAgICBwcmludChmXCJ7aCsxOlx1MDAzYzh9e206XHUwMDNjMTUuNmZ9ey1tKjEwOlx1MDAzYzIwLjRmfXtjfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gb2YgUG9zaXRpb25hbCBFbmNvZGluZyBNZXRob2RzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBTGlCaSBvY2N1cGllcyBhIHVuaXF1ZSBuaWNoZTogemVybyB0cmFpbmFibGUgcGFyYW1ldGVycywgbm8gZW1iZWRkaW5nIGxvb2t1cCwgYW5kIGdyYWNlZnVsIGV4dHJhcG9sYXRpb24gYmV5b25kIHRoZSB0cmFpbmluZyBsZW5ndGguIFRoZSB0cmFkZW9mZiBpcyBhIGhhcmRjb2RlZCBtb25vdG9uaWMgZGVjYXkgdGhhdCBjYW5ub3QgbGVhcm4gbm9uLW1vbm90b25pYyBhdHRlbnRpb24gcGF0dGVybnMuIFRoZSB0YWJsZSBiZWxvdyBjb21wYXJlcyBmaXZlIGFwcHJvYWNoZXMgYWNyb3NzIHByb3BlcnRpZXMgcmVsZXZhbnQgdG8gZGVwbG95bWVudC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiVHJhaW4tc2hvcnQgdGVzdC1sb25nIiwiUGFyYW1zIiwiSW1wbGVtZW50YXRpb24iLCJNb25vdG9uaWMgZGVjYXkiLCJVc2VkIGluIl0sInJvd3MiOltbIlNpbnVzb2lkYWwiLCJQb29yIOKAlCBkaXN0cmlidXRpb24gc2hpZnQiLCIwIiwiTG93IiwiTm8iLCJPcmlnaW5hbCBUcmFuc2Zvcm1lciwgQkFSVCJdLFsiTGVhcm5lZCBBYnNvbHV0ZSIsIk5vbmUg4oCUIGhhcmQgT09EIGZhaWx1cmUiLCJtYXhfbGVuIMOXIGRfbW9kZWwiLCJMb3ciLCJObyIsIkJFUlQsIEdQVC0yLCBlYXJseSBHUFQtMyJdLFsiUm9QRSIsIkdvb2Qg4oCUIHJvdGFyeSByZWxhdGl2ZSBQRSIsIjAiLCJNZWRpdW0iLCJObyAocm90YXJ5KSIsIkxMYU1BIDEvMi8zLCBNaXN0cmFsLCBGYWxjb24iXSxbIkFMaUJpIiwiVmVyeSBnb29kIOKAlCBsaW5lYXIgZGVjYXkiLCIwIiwiTG93IiwiWWVzIChoYXJkY29kZWQpIiwiQkxPT00tMTc2QiwgTVBULTdCLCBPUFQgdmFyaWFudHMiXSxbIk5vUEUiLCJNb2RlcmF0ZSDigJQgaW1wbGljaXQgY2F1c2FsIiwiMCIsIlRyaXZpYWwgKHJlbW92ZSBQRSkiLCJOL0EiLCJSZXNlYXJjaCBhYmxhdGlvbnMsIGRlY29kZXIgc3R1ZGllcyJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBTGlCaSB3YXMgYWRvcHRlZCBpbiBCTE9PTS0xNzZCICh0aGUgZmlyc3Qgb3BlbiBtdWx0aWxpbmd1YWwgMTAwQisgbW9kZWwpLCB0aGUgTW9zYWljIE1QVCBmYW1pbHksIGFuZCBzZXZlcmFsIE9QVCB2YXJpYW50cy4gSXRzIHplcm8tcGFyYW1ldGVyIG92ZXJoZWFkIGFuZCBtaW5pbWFsIGltcGxlbWVudGF0aW9uIGNoYW5nZXMgbWFkZSBpdCBhdHRyYWN0aXZlIGF0IHNjYWxlLiBBcyBvZiAyMDI0LCBSb1BFIGhhcyBsYXJnZWx5IGRpc3BsYWNlZCBBTGlCaSBpbiBuZXcgbGFyZ2UgbW9kZWxzIGR1ZSB0byBSb1BFXHUwMDI3cyBzdXBlcmlvciBsb25nLWNvbnRleHQgcGVyZm9ybWFuY2Ugd2hlbiBjb21iaW5lZCB3aXRoIHBvc2l0aW9uYWwgaW50ZXJwb2xhdGlvbiB0ZWNobmlxdWVzIGxpa2UgWWFSTiBvciBMb25nUm9QRS4gQUxpQmlcdTAwMjdzIHByaW1hcnkgbGltaXRhdGlvbiDigJQgaGFyZGNvZGVkIG1vbm90b25pYyBkZWNheSDigJQgYmVjb21lcyBzaWduaWZpY2FudCBpbiByZXRyaWV2YWwtYXVnbWVudGVkIHRhc2tzIHdoZXJlIHRoZSByZWxldmFudCBwYXNzYWdlIGlzIGZhciBmcm9tIHRoZSBjdXJyZW50IGdlbmVyYXRpb24gcG9zaXRpb24gYW5kIG11c3QgcmVjZWl2ZSBoaWdoIGF0dGVudGlvbiB3ZWlnaHQgcmVnYXJkbGVzcyBvZiBkaXN0YW5jZS4ifV0="
---
# ALiBi — Attention with Linear Biases for Length Generalization

ALiBi (Attention with Linear Biases), introduced by Press et al. (2022), takes a radically simple approach to positional encoding: *do not add any positional information to the token embeddings at all*. Instead, subtract a linear bias from the raw attention logits at every layer and every head. The bias penalises attention to distant tokens in proportion to their distance, giving each head a built-in recency preference — zero learned positional parameters, zero embedding lookup, and a formula that remains valid at any sequence length.

## The ALiBi Mechanism

In standard scaled dot-product attention the logit for query position i attending to key position j is QᵢKⱼᵀ / √d_k. ALiBi modifies this to: score_alibi(i, j) = QᵢKⱼᵀ / √d_k − m·|i − j|, where m is a head-specific slope. The bias term depends only on the *relative* distance |i − j|, not on absolute position values. Crucially, this means the bias is valid at any absolute position — including positions 1025, 2048, or 8192 that were never seen during training on 1024-token sequences. No new embedding rows are needed for unseen positions; the distance formula extrapolates automatically.

$$\text{score\_alibi}(i,j) = \frac{Q_i K_j^{\top}}{\sqrt{d_k}} - m \cdot |i - j|$$

## Geometric Slopes per Head

Each attention head uses a different slope m drawn from a geometric sequence. For h heads, the slopes are: m_k = 2^{−8k/h} for k = 1, …, h. This gives a sequence from 2^{−8/h} (shallowest, global head) down to 2^{−8} (steepest, local head) — the paper reverses the indexing so head 1 is steepest and the last head is shallowest. Head 1 sharply penalises distance; a token at distance 10 receives a bias of −10m₁ which is very negative. The last head's shallow slope means distant tokens still receive near-zero bias and can contribute meaningfully. This diversity lets the model capture both local syntactic cues and long-range semantic dependencies simultaneously across heads.

- Head 1 (steepest slope m = 2^{-8}): effectively a local attention window of a few tokens
- Head h (shallowest slope m = 2^{-8/h}): can attend globally with small distance penalty
- Slopes are fixed at initialisation — never updated by gradient descent
- Bias is a lower-triangular matrix combined with the causal mask at each layer
- The bias tensor is computed on-the-fly for each sequence length — no max-length cap

## Code 1 — ALiBi Bias Computation

Computing the geometric slope sequence and building the full (n_heads × seq_len × seq_len) bias tensor. The implementation handles non-power-of-2 head counts by interpolating extra intermediate slopes.

```python
import torch
import math


def get_alibi_slopes(n_heads: int) -> torch.Tensor:
    """Geometric sequence: {2^{-8/h}, 2^{-8*2/h}, ..., 2^{-8}} for h heads."""
    # Use largest power of 2 <= n_heads as the base count
    n = 2 ** math.floor(math.log2(n_heads))
    m0 = 2 ** (-8 / n)                           # base step ratio
    slopes = torch.tensor([m0 ** i for i in range(1, n + 1)], dtype=torch.float32)
    if n < n_heads:                               # non-power-of-2: interpolate extras
        extra = torch.tensor(
            [m0 ** (i / 2) for i in range(1, 2 * (n_heads - n) + 1, 2)],
            dtype=torch.float32,
        )
        slopes = torch.cat([slopes, extra], dim=0)
    return slopes  # shape (n_heads,)


def compute_alibi_bias(n_heads: int, seq_len: int) -> torch.Tensor:
    """Return ALiBi bias tensor of shape (n_heads, seq_len, seq_len)."""
    slopes = get_alibi_slopes(n_heads)            # (H,)
    pos    = torch.arange(seq_len, dtype=torch.float32)
    dist   = (pos.unsqueeze(0) - pos.unsqueeze(1)).abs()   # |i-j| matrix (L, L)
    # (H, 1, 1) * (1, L, L) => (H, L, L)
    return -slopes.view(n_heads, 1, 1) * dist.unsqueeze(0)


# Example: 8 heads, sequence length 16
bias   = compute_alibi_bias(8, 16)
slopes = get_alibi_slopes(8)
print("Bias shape:", bias.shape)                  # (8, 16, 16)
print("Slopes:", slopes.numpy().round(5))
print("Head 0 bias at dist=8 (steepest):",  bias[0, 8, 0].item())
print("Head 7 bias at dist=8 (shallowest):", bias[7, 8, 0].item())
```

## Code 2 — ALiBi Inside Multi-Head Attention

Integrating the ALiBi bias tensor into a full multi-head attention module. The bias is added to raw attention logits *before* softmax. No modification to Q, K, or V projections is needed — the token embeddings remain position-free.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class ALiBiMultiHeadAttention(nn.Module):
    """Multi-head attention that uses ALiBi logit biases instead of positional embeddings."""

    def __init__(self, d_model: int, n_heads: int):
        super().__init__()
        assert d_model % n_heads == 0
        self.n_heads = n_heads
        self.d_k  = d_model // n_heads
        self.qkv  = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        slopes = self._make_slopes(n_heads)
        self.register_buffer("slopes", slopes)   # fixed, never trained

    @staticmethod
    def _make_slopes(n: int) -> torch.Tensor:
        base = 2 ** (-8 / (2 ** math.floor(math.log2(n))))
        return torch.tensor([base ** i for i in range(1, n + 1)], dtype=torch.float32)

    def _alibi_bias(self, seq_len: int) -> torch.Tensor:
        pos  = torch.arange(seq_len, device=self.slopes.device, dtype=torch.float32)
        dist = (pos.unsqueeze(0) - pos.unsqueeze(1)).abs()          # (L, L)
        return -self.slopes.view(-1, 1, 1) * dist.unsqueeze(0)      # (H, L, L)

    def forward(self, x: torch.Tensor, causal: bool = True) -> torch.Tensor:
        B, L, _ = x.shape
        qkv = self.qkv(x).reshape(B, L, 3, self.n_heads, self.d_k).permute(2, 0, 3, 1, 4)
        Q, K, V = qkv[0], qkv[1], qkv[2]
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)
        scores = scores + self._alibi_bias(L)    # <-- ALiBi bias injected here
        if causal:
            mask = torch.triu(torch.ones(L, L, device=x.device), diagonal=1).bool()
            scores = scores.masked_fill(mask, float("-inf"))
        out = torch.matmul(F.softmax(scores, dim=-1), V)
        return self.proj(out.transpose(1, 2).reshape(B, L, -1))
```

> **Recency Bias Is Built In**: ALiBi's linear penalty creates a fixed recency advantage: the immediately preceding token (distance 1) receives a bias of −m, while a token at distance 100 receives −100m. This is a hardcoded inductive bias — the model cannot learn to attend uniformly at all distances. For retrieval-style tasks where a relevant token may be far away and needs high attention weight regardless of position, this monotonic decay is a meaningful limitation.

## Train Short, Test Long — Extrapolation

The critical advantage of ALiBi over sinusoidal and learned positional embeddings is its behaviour at sequence lengths beyond the training window. Sinusoidal PE is theoretically unbounded but introduces a distribution shift at inference because the model rarely sees the longest-range sinusoidal patterns during training. Learned PE cannot generalise at all to positions beyond max_train_len. ALiBi's bias depends only on relative distance, so evaluating at length 2048 when trained on 1024 tokens is handled seamlessly: the maximum distance increases, but the formula is unchanged.

```python
import math

# Approximate perplexity results from Press et al. (2022) Table 1
# All models trained on sequences of length 1024 (WikiText-103)

train_len = 1024
test_lens  = [512, 1024, 2048, 4096, 8192]

results = {
    "Sinusoidal PE": {512: 17.5, 1024: 17.8, 2048: 23.9, 4096: 38.4, 8192: float("inf")},
    "Learned PE":    {512: 17.3, 1024: 17.6, 2048: float("inf"), 4096: float("inf"), 8192: float("inf")},
    "ALiBi":         {512: 17.6, 1024: 17.9, 2048: 18.3, 4096: 19.0, 8192: 20.5},
}

print(f"Perplexity at Various Lengths (trained on {train_len} tokens)")
print(f"{'Length':<10}", end="")
for name in results:
    print(f"{name:<20}", end="")
print()
print("-" * 70)

for L in test_lens:
    tag = "  (train)" if L == train_len else "  OOD" if L > train_len else ""
    print(f"{L:<10}", end="")
    for name, ppl_map in results.items():
        val = ppl_map.get(L, float("nan"))
        s   = "inf" if math.isinf(val) else f"{val:.1f}"
        print(f"{s:<20}", end="")
    print(tag)

print()
print("ALiBi degrades gracefully. Learned PE fails completely at OOD lengths.")
print("Sinusoidal PE degrades sharply beyond 2x training length.")
```

## Code 4 — Per-Head Slope Visualization

Visualising how each head's slope controls the effective attention window size. A steep slope makes the model tightly locally focused; a shallow slope allows globally distributed attention over hundreds of tokens.

```python
import math
import numpy as np
import matplotlib.pyplot as plt


def get_alibi_slopes(n_heads: int) -> list:
    n  = 2 ** math.floor(math.log2(n_heads))
    m0 = 2 ** (-8 / n)
    slopes = [m0 ** i for i in range(1, n + 1)]
    if n < n_heads:
        slopes += [m0 ** (i / 2) for i in range(1, 2 * (n_heads - n) + 1, 2)]
    return slopes


n_heads   = 8
max_dist  = 64
slopes    = get_alibi_slopes(n_heads)
distances = np.arange(max_dist)

fig, axes = plt.subplots(2, 4, figsize=(14, 5), sharey=True)
axes = axes.flatten()
for h, (ax, m) in enumerate(zip(axes, slopes)):
    bias = -m * distances
    ax.plot(distances, bias, color=f"C{h}", linewidth=2)
    ax.set_title(f"Head {h+1}  m={m:.5f}", fontsize=9)
    ax.set_xlabel("|i - j| distance")
    if h % 4 == 0:
        ax.set_ylabel("logit bias")
plt.suptitle("ALiBi Per-Head Linear Decay (8 heads)", fontsize=12, y=1.01)
plt.tight_layout()
plt.savefig("alibi_slopes.png", dpi=120, bbox_inches="tight")

print(f"{'Head':<8}{'Slope m':<15}{'bias at dist=10':<20}{'Attention character'}")
print("-" * 58)
chars = ["Very local", "Local", "Local", "Moderate",
         "Moderate", "Semi-global", "Semi-global", "Global"]
for h, (m, c) in enumerate(zip(slopes, chars)):
    print(f"{h+1:<8}{m:<15.6f}{-m*10:<20.4f}{c}")
```

## Comparison of Positional Encoding Methods

ALiBi occupies a unique niche: zero trainable parameters, no embedding lookup, and graceful extrapolation beyond the training length. The tradeoff is a hardcoded monotonic decay that cannot learn non-monotonic attention patterns. The table below compares five approaches across properties relevant to deployment.

| Method | Train-short test-long | Params | Implementation | Monotonic decay | Used in |
| --- | --- | --- | --- | --- | --- |
| Sinusoidal | Poor — distribution shift | 0 | Low | No | Original Transformer, BART |
| Learned Absolute | None — hard OOD failure | max_len × d_model | Low | No | BERT, GPT-2, early GPT-3 |
| RoPE | Good — rotary relative PE | 0 | Medium | No (rotary) | LLaMA 1/2/3, Mistral, Falcon |
| ALiBi | Very good — linear decay | 0 | Low | Yes (hardcoded) | BLOOM-176B, MPT-7B, OPT variants |
| NoPE | Moderate — implicit causal | 0 | Trivial (remove PE) | N/A | Research ablations, decoder studies |

ALiBi was adopted in BLOOM-176B (the first open multilingual 100B+ model), the Mosaic MPT family, and several OPT variants. Its zero-parameter overhead and minimal implementation changes made it attractive at scale. As of 2024, RoPE has largely displaced ALiBi in new large models due to RoPE's superior long-context performance when combined with positional interpolation techniques like YaRN or LongRoPE. ALiBi's primary limitation — hardcoded monotonic decay — becomes significant in retrieval-augmented tasks where the relevant passage is far from the current generation position and must receive high attention weight regardless of distance.

