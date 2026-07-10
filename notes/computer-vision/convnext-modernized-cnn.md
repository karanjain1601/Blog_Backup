---
title: "ConvNeXt: Modernizing CNNs to Match Vision Transformers"
slug: "convnext-modernized-cnn"
description: "How ConvNeXt incrementally modernizes ResNet-50 by adopting ViT training techniques — depthwise 7×7 convolutions, inverted bottleneck, GELU, and layer scale — achieving accuracy parity with Swin Transformer."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb252TmVYdCAoMjAyMiwgTGl1IGV0IGFsLiwgTWV0YSBBSSkgYXNrcyBhIHNpbXBsZSBxdWVzdGlvbjogY2FuIGEgcGxhaW4gQ05OIG1hdGNoIFN3aW4gVHJhbnNmb3JtZXIgd2hlbiB0cmFpbmVkIHdpdGggdGhlIHNhbWUgcmVjaXBlPyBTdGFydGluZyBmcm9tIFJlc05ldC01MCwgdGhlIGF1dGhvcnMgYXBwbHkgVmlULWVyYSBpbXByb3ZlbWVudHMgb25lIGF0IGEgdGltZSDigJQgbWFjcm8gZGVzaWduLCBkZXB0aHdpc2UgY29udm9sdXRpb25zLCBpbnZlcnRlZCBib3R0bGVuZWNrLCBsYXJnZXIga2VybmVscywgR0VMVSwgZmV3ZXIgYWN0aXZhdGlvbnMg4oCUIG1lYXN1cmluZyBhY2N1cmFjeSBhdCBlYWNoIHN0ZXAgdG8gaXNvbGF0ZSBlYWNoIGNvbnRyaWJ1dGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSByZXN1bHRpbmcgQ29udk5lWHQgZmFtaWx5IChUL1MvQi9ML1hMKSBzcGFucyAyOeKAkzM1MCBNIHBhcmFtZXRlcnMuIENvbnZOZVh0LVQgbWF0Y2hlcyBTd2luLVQgYXQgODIuMSUgSW1hZ2VOZXQtMUsgdG9wLTEgd2l0aCB+MjclIGhpZ2hlciB0aHJvdWdocHV0LCB3aGlsZSBDb252TmVYdC1MIHJlYWNoZXMgODQuMyUuIFRoZSBhcmNoaXRlY3R1cmUgaXMgcHVyZWx5IGNvbnZvbHV0aW9uYWwg4oCUIG5vIHNlbGYtYXR0ZW50aW9uIOKAlCB5ZXQgY29tcGV0ZXMgb24gY2xhc3NpZmljYXRpb24sIG9iamVjdCBkZXRlY3Rpb24sIGFuZCBzZW1hbnRpYyBzZWdtZW50YXRpb24gYmVuY2htYXJrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlB1Ymxpc2hlZCBhcyBcdTAwMjdBIENvbnZOZXQgZm9yIHRoZSAyMDIwc1x1MDAyNyBhdCBDVlBSIDIwMjIsIENvbnZOZVh0IGNoYWxsZW5nZXMgdGhlIG5hcnJhdGl2ZSB0aGF0IHRyYW5zZm9ybWVycyBhcmUgaW5oZXJlbnRseSBzdXBlcmlvciB0byBDTk5zLiBJdCBzaG93cyB0aGF0IHdpdGggZXF1YWxpemVkIHRyYWluaW5nIGNvbmRpdGlvbnMg4oCUIEFkYW1XLCBjb3NpbmUgZGVjYXksIGV4dGVuZGVkIHNjaGVkdWxlcywgYW5kIG1vZGVybiBhdWdtZW50YXRpb24g4oCUIGEgd2VsbC1kZXNpZ25lZCBjb252b2x1dGlvbmFsIG5ldHdvcmsgY2FuIG1hdGNoIG9yIGV4Y2VlZCBoaWVyYXJjaGljYWwgdmlzaW9uIHRyYW5zZm9ybWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb2Rlcm5pemF0aW9uIFJvYWRtYXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBhdXRob3JzIGJlZ2luIHdpdGggUmVzTmV0LTUwIGF0IDc2LjElIHRvcC0xIGFuZCBhcHBseSB0aGUgVmlUIHRyYWluaW5nIHJlY2lwZTogQWRhbVcgb3B0aW1pemVyLCBjb3NpbmUgc2NoZWR1bGUgd2l0aCB3YXJtdXAsIDMwMCB0cmFpbmluZyBlcG9jaHMsIE1peHVwLCBDdXRNaXgsIFJhbmRBdWdtZW50LCBhbmQgTGFiZWwgU21vb3RoaW5nLiBUaGlzIGFsb25lIHJhaXNlcyBhY2N1cmFjeSB0byA3OC44JSDigJQgYSAyLjctcG9pbnQgZ2FpbiB3aXRoIG5vIGFyY2hpdGVjdHVyYWwgY2hhbmdlLCByZXZlYWxpbmcgdGhhdCBtdWNoIG9mIHRoZSBDTk4tdnMtdHJhbnNmb3JtZXIgZ2FwIHN0ZW1zIGZyb20gdHJhaW5pbmcgcHJvY2VkdXJlcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFyY2hpdGVjdHVyYWwgY2hhbmdlcyBhcHBsaWVkIHNlcXVlbnRpYWxseTogc3RhZ2UgcmF0aW8gKDMsNCw2LDMp4oaSKDMsMyw5LDMpIOKGkiA3OS40JTsgcGF0Y2hpZnkgc3RlbSDihpIgNzkuNSU7IGRlcHRod2lzZSBzZXBhcmFibGUgbGF5ZXJzIOKGkiA4MC41JTsgaW52ZXJ0ZWQgYm90dGxlbmVjayAoNMOXIGV4cGFuZCkg4oaSIDgwLjYlOyA3w5c3IGRlcHRod2lzZSBrZXJuZWwg4oaSIDgwLjYlOyBHRUxVICsgc2luZ2xlIGFjdGl2YXRpb24gcGVyIGJsb2NrIOKGkiA4MS4zJTsgc2VwYXJhdGUgZG93bnNhbXBsaW5nIGxheWVycyDihpIgODIuMCUuIEVhY2ggc3RlcCBpcyBzbWFsbDsgY29tcG91bmRlZCB0aGV5IGNsb3NlIHRoZSBnYXAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udk5lWHQgQmxvY2sgRGVzaWduIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQ29udk5lWHQgYmxvY2sgbWlycm9ycyBhIHRyYW5zZm9ybWVyIGJsb2NrOiBkZXB0aHdpc2UgN8OXNyBjb252IGZvciBsYXJnZS1rZXJuZWwgc3BhdGlhbCBtaXhpbmcsIHRoZW4gYSBwb2ludHdpc2UgZXhwYW5kLTTDlyBsaW5lYXIgbGF5ZXIsIEdFTFUsIGFuZCBhIHBvaW50d2lzZSBwcm9qZWN0aW9uIGJhY2suIFVubGlrZSBSZXNOZXRcdTAwMjdzIGJvdHRsZW5lY2ssIHRoZSBkZXB0aHdpc2UgY29udiBydW5zIGF0IGZ1bGwgY2hhbm5lbCB3aWR0aCBiZWZvcmUgZXhwYW5zaW9uLiBCYXRjaCBOb3JtIGlzIHN3YXBwZWQgZm9yIExheWVyIE5vcm0sIGFuZCBhIHNpbmdsZSBhY3RpdmF0aW9uIHBlciBibG9jayBtYXRjaGVzIHRyYW5zZm9ybWVyIGNvbnZlbnRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaCwgdG9yY2gubm4gYXMgbm5cbmNsYXNzIENvbnZOZVh0QmxvY2sobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltLCBsc19pbml0PTFlLTYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5kdyA9IG5uLkNvbnYyZChkaW0sIGRpbSwgNywgcGFkZGluZz0zLCBncm91cHM9ZGltKVxuICAgICAgICBzZWxmLm5vcm0gPSBubi5MYXllck5vcm0oZGltKVxuICAgICAgICBzZWxmLnB3MSA9IG5uLkxpbmVhcihkaW0sIDQgKiBkaW0pXG4gICAgICAgIHNlbGYuYWN0ID0gbm4uR0VMVSgpXG4gICAgICAgIHNlbGYucHcyID0gbm4uTGluZWFyKDQgKiBkaW0sIGRpbSlcbiAgICAgICAgc2VsZi5nYW1tYSA9IG5uLlBhcmFtZXRlcihsc19pbml0ICogdG9yY2gub25lcyhkaW0pKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByID0geFxuICAgICAgICB4ID0gc2VsZi5kdyh4KS5wZXJtdXRlKDAsIDIsIDMsIDEpICAjIE5DSFctXHUwMDNlTkhXQ1xuICAgICAgICB4ID0gc2VsZi5wdzIoc2VsZi5hY3Qoc2VsZi5wdzEoc2VsZi5ub3JtKHgpKSkpXG4gICAgICAgIHJldHVybiByICsgKHNlbGYuZ2FtbWEgKiB4KS5wZXJtdXRlKDAsIDMsIDEsIDIpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMYXllciBzY2FsZSBpcyBhIHBlci1jaGFubmVsIGxlYXJuYWJsZSBzY2FsYXIgzrMgaW5pdGlhbGl6ZWQgdG8gYSB0aW55IHZhbHVlICgxZS02KS4gSXQgbXVsdGlwbGllcyB0aGUgYmxvY2sgb3V0cHV0IGJlZm9yZSBhZGRpbmcgdGhlIHJlc2lkdWFsLCB6ZXJvaW5nIG5ldyBibG9ja3MgYXQgaW5pdGlhbGl6YXRpb24gc28gdHJhaW5pbmcgc3RhcnRzIGFzIGlmIHRoZSBuZXR3b3JrIHdlcmUgc2hhbGxvdy4gVGhpcyBwcmV2ZW50cyBncmFkaWVudCBleHBsb3Npb24gaW4gbGFyZ2UgQ29udk5lWHQgbW9kZWxzIGFuZCBpcyBjcml0aWNhbCBmb3Igc3RhYmxlIHRyYWluaW5nIGF0IENvbnZOZVh0LUIgc2NhbGUgYW5kIGFib3ZlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2gsIHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIExheWVyU2NhbGUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltLCBpbml0PTFlLTYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5nYW1tYSA9IG5uLlBhcmFtZXRlcihpbml0ICogdG9yY2gub25lcyhkaW0pKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICAjIHg6IChCLCBILCBXLCBDKSAtLSBOSFdDIGxheW91dFxuICAgICAgICByZXR1cm4gc2VsZi5nYW1tYSAqIHggICMgYnJvYWRjYXN0cyBvdmVyIEIsIEgsIFdcblxuIyBHcmFkaWVudCBlZmZlY3Q6IGdyYWQgdy5yLnQuIGJsb2NrIHBhcmFtcyBzY2FsZWQgYnkgZ2FtbWFcbiMgZ2FtbWEgfj0gMCBhdCBpbml0IC1cdTAwM2UgbmV3IGJsb2NrcyBjb250cmlidXRlIG5lYXItemVyb1xuIyAtXHUwMDNlIG5ldHdvcmsgYmVoYXZlcyBsaWtlIGEgc2hhbGxvd2VyIG1vZGVsIGF0IHN0YXJ0IG9mIHRyYWluaW5nIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaC5ubiBhcyBublxuXG4jIFBhdGNoaWZ5IHN0ZW06IHJlcGxhY2VzIFJlc05ldFx1MDAyN3MgN3g3IGNvbnYgKyBNYXhQb29sXG4jIFByb2R1Y2VzIG5vbi1vdmVybGFwcGluZyA0eDQgcGF0Y2hlcyAoc3RyaWRlID0ga2VybmVsX3NpemUpXG5zdGVtID0gbm4uU2VxdWVudGlhbChcbiAgICBubi5Db252MmQoMywgOTYsIGtlcm5lbF9zaXplPTQsIHN0cmlkZT00KSwgICMgQ19vdXQ9OTYgZm9yIENvbnZOZVh0LVRcbiAgICBubi5MYXllck5vcm0oOTYsIGVwcz0xZS02KSxcbilcbiMgSW5wdXQgOiAoQiwgMywgMjI0LCAyMjQpXG4jIE91dHB1dDogKEIsIDk2LCA1NiwgNTYpXG4jIE5vIG92ZXJsYXAgYmV0d2VlbiBwYXRjaGVzOyBzdHJpZGUgPT0ga2VybmVsX3NpemVcbiMgTGF5ZXJOb3JtIG5vcm1hbGlzZXMgb3ZlciBjaGFubmVsIGRpbSAoYXBwbGllZCBhZnRlciBOSFdDIHBlcm11dGUpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWFjcm8gQXJjaGl0ZWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb252TmVYdCB1c2VzIGEgNC1zdGFnZSBoaWVyYXJjaHk6IHNwYXRpYWwgcmVzb2x1dGlvbiBoYWx2ZXMgYW5kIGNoYW5uZWxzIGRvdWJsZSBhdCBlYWNoIHN0YWdlIGJvdW5kYXJ5LiBDaGFubmVsIGNvdW50cyBhcmUgKDk2LCAxOTIsIDM4NCwgNzY4KSBmb3IgQ29udk5lWHQtVC4gRG93bnNhbXBsaW5nIGJldHdlZW4gc3RhZ2VzIHVzZXMgYSBzZXBhcmF0ZSBMYXllck5vcm0gKyAyw5cyIHN0cmlkZS0yIGNvbnYsIGRlY291cGxpbmcgc3BhdGlhbCByZWR1Y3Rpb24gZnJvbSBmZWF0dXJlIHRyYW5zZm9ybWF0aW9uLiBUaGUgc3RhZ2UgcmF0aW8gc2hpZnRzIHRvICgzLDMsOSwzKSwgY29uY2VudHJhdGluZyBjb21wdXRlIGluIHN0YWdlIDMgbGlrZSBTd2luLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJBcmNoaXRlY3R1cmUiLCJUb3AtMSAlIiwiUGFyYW1zIChNKSIsIkZMT1BzIChHKSIsIlRocm91Z2hwdXQgKGltZy9zKSJdLCJyb3dzIjpbWyJSZXNOZXQtNTAiLCI3Ni4xIiwiMjUiLCI0LjEiLCIxMjI2Il0sWyJTd2luLVQiLCI4MS4zIiwiMjgiLCI0LjUiLCI3NTUiXSxbIkNvbnZOZVh0LVQiLCI4Mi4xIiwiMjkiLCI0LjUiLCI5NjAiXSxbIkNvbnZOZVh0LVMiLCI4My4xIiwiNTAiLCI4LjciLCI1OTIiXSxbIkNvbnZOZVh0LUIiLCI4My44IiwiODkiLCIxNS40IiwiMzczIl0sWyJDb252TmVYdC1MIiwiODQuMyIsIjE5OCIsIjM0LjQiLCIyMDUiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udk5lWHRcdTAwMjdzIHNlcGFyYXRlIGRvd25zYW1wbGluZyBsYXllcnMgY29udHJhc3Qgd2l0aCBSZXNOZXQsIHdoZXJlIHRoZSBmaXJzdCBibG9jayBpbiBlYWNoIHN0YWdlIHNpbXVsdGFuZW91c2x5IGhhbHZlcyByZXNvbHV0aW9uIGFuZCBkb3VibGVzIGNoYW5uZWxzLiBUaGlzIGNsZWFuIHNlcGFyYXRpb24gbWFrZXMgZWFjaCBjb21wb25lbnRcdTAwMjdzIHJvbGUgZXhwbGljaXQuIFRoZSA0LXN0YWdlIGZlYXR1cmUgbWFwcyBhdCBzdHJpZGVzICg0LCA4LCAxNiwgMzIpIHBsdWcgZGlyZWN0bHkgaW50byBGUE4gZm9yIGRldGVjdGlvbiBhbmQgVVBlck5ldCBmb3Igc2VnbWVudGF0aW9uIHdpdGhvdXQgYXJjaGl0ZWN0dXJhbCBtb2RpZmljYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udk5lWHQgdnMgU3dpbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udk5lWHQtVCBhbmQgU3dpbi1UIGFyZSBhIGZhaXIgY29tcGFyaXNvbiBhdCB+MjkgTSBwYXJhbWV0ZXJzIGFuZCB+NC41IEdGTE9Qcy4gQ29udk5lWHQtVCBhY2hpZXZlcyA4Mi4xJSB2cyBTd2luLVRcdTAwMjdzIDgxLjMlIG9uIEltYWdlTmV0LTFLLCB3aXRoIH4yNyUgaGlnaGVyIHRocm91Z2hwdXQgKDk2MCB2cyA3NTUgaW1nL3Mgb24gQTEwMCkuIENvbnZOZVh0IGF2b2lkcyBzaGlmdGVkIHdpbmRvdyBvcGVyYXRpb25zIGFuZCByZWxhdGl2ZSBwb3NpdGlvbiBiaWFzZXMsIGdpdmluZyBpdCBzaW1wbGVyIENVREEga2VybmVscyBhbmQgYmV0dGVyIGNvbXBhdGliaWxpdHkgd2l0aCBkZWVwIGxlYXJuaW5nIGNvbXBpbGVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRpbW0sIHRvcmNoLCB0aW1lXG5cbmRldmljZSA9IHRvcmNoLmRldmljZShcImN1ZGFcIiBpZiB0b3JjaC5jdWRhLmlzX2F2YWlsYWJsZSgpIGVsc2UgXCJjcHVcIilcbnBhaXJzID0gWyhcImNvbnZuZXh0X3RpbnlcIiwgODIuMSksIChcInN3aW5fdGlueV9wYXRjaDRfd2luZG93N18yMjRcIiwgODEuMyldXG5mb3IgbmFtZSwgdG9wMSBpbiBwYWlyczpcbiAgICBtID0gdGltbS5jcmVhdGVfbW9kZWwobmFtZSwgcHJldHJhaW5lZD1GYWxzZSkuZXZhbCgpLnRvKGRldmljZSlcbiAgICB4ID0gdG9yY2gucmFuZG4oMzIsIDMsIDIyNCwgMjI0LCBkZXZpY2U9ZGV2aWNlKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgXyBpbiByYW5nZSgzKTogbSh4KSAgICAgICAgICAjIHdhcm11cFxuICAgICAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2UoMjApOiBtKHgpXG4gICAgICAgIGZwcyA9IDMyICogMjAgLyAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKVxuICAgIHByaW50KGZcIntuYW1lfTogdG9wLTE9e3RvcDF9JSAgdGhyb3VnaHB1dD17ZnBzOi4wZn0gaW1nL3NcIikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJleW9uZCB0aHJvdWdocHV0LCBDb252TmVYdCBzdXBwb3J0cyBhcmJpdHJhcnkgaW5wdXQgcmVzb2x1dGlvbnMgd2l0aG91dCByZXRyYWluaW5nLCBpbnRlZ3JhdGVzIGNsZWFubHkgd2l0aCB0b3JjaHZpc2lvbiBhbmQgdGltbSwgYW5kIHJlcXVpcmVzIG5vIHNwZWNpYWxpemVkIENVREEgZXh0ZW5zaW9ucy4gT24gZG93bnN0cmVhbSB0YXNrcywgQ29udk5lWHQtQiB3aXRoIENhc2NhZGUgTWFzayBSLUNOTiBhY2hpZXZlcyA1NC4wIGJveCBBUCBvbiBDT0NPIHZzIFN3aW4tQiA1MS45LCBhbmQgd2l0aCBVUGVyTmV0IG9uIEFERTIwSyByZWFjaGVzIDUyLjEgbUlvVSB2cyBTd2luLUIgNTEuNi4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJjb250ZW50IjoiQ29udk5lWHQgc2hvd3MgdGhlIGFjY3VyYWN5IGdhcCBiZXR3ZWVuIENOTnMgYW5kIHRyYW5zZm9ybWVycyB3YXMgbGFyZ2VseSBhIHRyYWluaW5nIHJlY2lwZSBnYXAg4oCUIHdpdGggQWRhbVcsIGNvc2luZSBzY2hlZHVsZSwgTWl4dXAsIEN1dE1peCwgYW5kIFJhbmRBdWdtZW50LCBhIHB1cmUgQ05OIG1hdGNoZXMgU3dpbiBUcmFuc2Zvcm1lci4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF0IHNjYWxlLCBDb252TmVYdC1YTCBmaW5lLXR1bmVkIG9uIEltYWdlTmV0LTIySyByZWFjaGVzIDg3LjglIHRvcC0xIGF0IDM4NMKyIHJlc29sdXRpb24uIENvbnZOZVh0LUwgcHJlLXRyYWluZWQgb24gSW1hZ2VOZXQtMjJLIHNjb3JlcyA4Ni42JSBhdCAyMjTCsi4gVGhlc2UgcmVzdWx0cyBjb25maXJtIHRoYXQgdGhlIGFyY2hpdGVjdHVyYWwgaW1wcm92ZW1lbnRzIHRyYW5zZmVyIGFjcm9zcyBzY2FsZXMgYW5kIHByZXRyYWluaW5nIGRhdGFzZXRzLCBtYWtpbmcgQ29udk5lWHQgYSBzdHJvbmcgYmFja2JvbmUgZm9yIHZpc3VhbCByZWNvZ25pdGlvbiB0YXNrcyByZXF1aXJpbmcgbGFyZ2Utc2NhbGUgcHJldHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udk5lWHQgcHJvdmVzIHRoYXQgbG9jYWxpdHkgYW5kIHRyYW5zbGF0aW9uIGVxdWl2YXJpYW5jZSwgY29tYmluZWQgd2l0aCBWaVQgdHJhaW5pbmcgcmVjaXBlcywgY2FuIG1hdGNoIGF0dGVudGlvbi1iYXNlZCBtb2RlbHMuIEtleSBjaGFuZ2VzOiBkZXB0aHdpc2UgN8OXNyBjb252IGZvciBsYXJnZSByZWNlcHRpdmUgZmllbGQsIGludmVydGVkIGJvdHRsZW5lY2sgKDTDlyBleHBhbnNpb24pLCBHRUxVICsgc2luZ2xlIGFjdGl2YXRpb24gcGVyIGJsb2NrLCBMYXllciBOb3JtIHJlcGxhY2luZyBCYXRjaCBOb3JtLCBzZXBhcmF0ZSBkb3duc2FtcGxpbmcgbGF5ZXJzLCBhbmQgbGF5ZXIgc2NhbGUgZm9yIGRlZXAgbW9kZWwgc3RhYmlsaXR5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIHByYWN0aXRpb25lcnMsIENvbnZOZVh0LVQgaXMgdGhlIGRlZmF1bHQgZHJvcC1pbiBmb3IgUmVzTmV0LTUwLCBvZmZlcmluZyArNiBwb2ludHMgdG9wLTEgYWNjdXJhY3kgYXQgc2ltaWxhciBGTE9Qcy4gQ29udk5lWHQtQi9MIHN1aXQgaGlnaGVyLWNvbXB1dGUgc2NlbmFyaW9zLiBPbiBtb2JpbGUgb3IgZWRnZSBoYXJkd2FyZSwgZGVwdGh3aXNlIGNvbnZvbHV0aW9ucyBtYXkgdW5kZXJwZXJmb3JtIG9uIHNvbWUgYWNjZWxlcmF0b3JzIOKAlCBiZW5jaG1hcmsgYm90aCBiZWZvcmUgY29tbWl0dGluZy4gVXNlIHRpbW0gZm9yIHByZXRyYWluZWQgd2VpZ2h0cyBhbmQgcmVsaWFibGUgZmluZS10dW5pbmcgYmFzZWxpbmVzLiJ9XQ=="
---
# ConvNeXt: Modernizing CNNs to Match Vision Transformers

## Overview

ConvNeXt (2022, Liu et al., Meta AI) asks a simple question: can a plain CNN match Swin Transformer when trained with the same recipe? Starting from ResNet-50, the authors apply ViT-era improvements one at a time — macro design, depthwise convolutions, inverted bottleneck, larger kernels, GELU, fewer activations — measuring accuracy at each step to isolate each contribution.

The resulting ConvNeXt family (T/S/B/L/XL) spans 29–350 M parameters. ConvNeXt-T matches Swin-T at 82.1% ImageNet-1K top-1 with ~27% higher throughput, while ConvNeXt-L reaches 84.3%. The architecture is purely convolutional — no self-attention — yet competes on classification, object detection, and semantic segmentation benchmarks.

Published as 'A ConvNet for the 2020s' at CVPR 2022, ConvNeXt challenges the narrative that transformers are inherently superior to CNNs. It shows that with equalized training conditions — AdamW, cosine decay, extended schedules, and modern augmentation — a well-designed convolutional network can match or exceed hierarchical vision transformers.

## Modernization Roadmap

The authors begin with ResNet-50 at 76.1% top-1 and apply the ViT training recipe: AdamW optimizer, cosine schedule with warmup, 300 training epochs, Mixup, CutMix, RandAugment, and Label Smoothing. This alone raises accuracy to 78.8% — a 2.7-point gain with no architectural change, revealing that much of the CNN-vs-transformer gap stems from training procedures.

Architectural changes applied sequentially: stage ratio (3,4,6,3)→(3,3,9,3) → 79.4%; patchify stem → 79.5%; depthwise separable layers → 80.5%; inverted bottleneck (4× expand) → 80.6%; 7×7 depthwise kernel → 80.6%; GELU + single activation per block → 81.3%; separate downsampling layers → 82.0%. Each step is small; compounded they close the gap.

## ConvNeXt Block Design

The ConvNeXt block mirrors a transformer block: depthwise 7×7 conv for large-kernel spatial mixing, then a pointwise expand-4× linear layer, GELU, and a pointwise projection back. Unlike ResNet's bottleneck, the depthwise conv runs at full channel width before expansion. Batch Norm is swapped for Layer Norm, and a single activation per block matches transformer convention.

```python
import torch, torch.nn as nn
class ConvNeXtBlock(nn.Module):
    def __init__(self, dim, ls_init=1e-6):
        super().__init__()
        self.dw = nn.Conv2d(dim, dim, 7, padding=3, groups=dim)
        self.norm = nn.LayerNorm(dim)
        self.pw1 = nn.Linear(dim, 4 * dim)
        self.act = nn.GELU()
        self.pw2 = nn.Linear(4 * dim, dim)
        self.gamma = nn.Parameter(ls_init * torch.ones(dim))
    def forward(self, x):
        r = x
        x = self.dw(x).permute(0, 2, 3, 1)  # NCHW->NHWC
        x = self.pw2(self.act(self.pw1(self.norm(x))))
        return r + (self.gamma * x).permute(0, 3, 1, 2)
```

Layer scale is a per-channel learnable scalar γ initialized to a tiny value (1e-6). It multiplies the block output before adding the residual, zeroing new blocks at initialization so training starts as if the network were shallow. This prevents gradient explosion in large ConvNeXt models and is critical for stable training at ConvNeXt-B scale and above.

```python
import torch, torch.nn as nn

class LayerScale(nn.Module):
    def __init__(self, dim, init=1e-6):
        super().__init__()
        self.gamma = nn.Parameter(init * torch.ones(dim))
    def forward(self, x):
        # x: (B, H, W, C) -- NHWC layout
        return self.gamma * x  # broadcasts over B, H, W

# Gradient effect: grad w.r.t. block params scaled by gamma
# gamma ~= 0 at init -> new blocks contribute near-zero
# -> network behaves like a shallower model at start of training
```

```python
import torch.nn as nn

# Patchify stem: replaces ResNet's 7x7 conv + MaxPool
# Produces non-overlapping 4x4 patches (stride = kernel_size)
stem = nn.Sequential(
    nn.Conv2d(3, 96, kernel_size=4, stride=4),  # C_out=96 for ConvNeXt-T
    nn.LayerNorm(96, eps=1e-6),
)
# Input : (B, 3, 224, 224)
# Output: (B, 96, 56, 56)
# No overlap between patches; stride == kernel_size
# LayerNorm normalises over channel dim (applied after NHWC permute)
```

## Macro Architecture

ConvNeXt uses a 4-stage hierarchy: spatial resolution halves and channels double at each stage boundary. Channel counts are (96, 192, 384, 768) for ConvNeXt-T. Downsampling between stages uses a separate LayerNorm + 2×2 stride-2 conv, decoupling spatial reduction from feature transformation. The stage ratio shifts to (3,3,9,3), concentrating compute in stage 3 like Swin.

| Architecture | Top-1 % | Params (M) | FLOPs (G) | Throughput (img/s) |
| --- | --- | --- | --- | --- |
| ResNet-50 | 76.1 | 25 | 4.1 | 1226 |
| Swin-T | 81.3 | 28 | 4.5 | 755 |
| ConvNeXt-T | 82.1 | 29 | 4.5 | 960 |
| ConvNeXt-S | 83.1 | 50 | 8.7 | 592 |
| ConvNeXt-B | 83.8 | 89 | 15.4 | 373 |
| ConvNeXt-L | 84.3 | 198 | 34.4 | 205 |

ConvNeXt's separate downsampling layers contrast with ResNet, where the first block in each stage simultaneously halves resolution and doubles channels. This clean separation makes each component's role explicit. The 4-stage feature maps at strides (4, 8, 16, 32) plug directly into FPN for detection and UPerNet for segmentation without architectural modification.

## ConvNeXt vs Swin

ConvNeXt-T and Swin-T are a fair comparison at ~29 M parameters and ~4.5 GFLOPs. ConvNeXt-T achieves 82.1% vs Swin-T's 81.3% on ImageNet-1K, with ~27% higher throughput (960 vs 755 img/s on A100). ConvNeXt avoids shifted window operations and relative position biases, giving it simpler CUDA kernels and better compatibility with deep learning compilers.

```python
import timm, torch, time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
pairs = [("convnext_tiny", 82.1), ("swin_tiny_patch4_window7_224", 81.3)]
for name, top1 in pairs:
    m = timm.create_model(name, pretrained=False).eval().to(device)
    x = torch.randn(32, 3, 224, 224, device=device)
    with torch.no_grad():
        for _ in range(3): m(x)          # warmup
        t0 = time.perf_counter()
        for _ in range(20): m(x)
        fps = 32 * 20 / (time.perf_counter() - t0)
    print(f"{name}: top-1={top1}%  throughput={fps:.0f} img/s")
```

Beyond throughput, ConvNeXt supports arbitrary input resolutions without retraining, integrates cleanly with torchvision and timm, and requires no specialized CUDA extensions. On downstream tasks, ConvNeXt-B with Cascade Mask R-CNN achieves 54.0 box AP on COCO vs Swin-B 51.9, and with UPerNet on ADE20K reaches 52.1 mIoU vs Swin-B 51.6.

> **info**: ConvNeXt shows the accuracy gap between CNNs and transformers was largely a training recipe gap — with AdamW, cosine schedule, Mixup, CutMix, and RandAugment, a pure CNN matches Swin Transformer.

At scale, ConvNeXt-XL fine-tuned on ImageNet-22K reaches 87.8% top-1 at 384² resolution. ConvNeXt-L pre-trained on ImageNet-22K scores 86.6% at 224². These results confirm that the architectural improvements transfer across scales and pretraining datasets, making ConvNeXt a strong backbone for visual recognition tasks requiring large-scale pretraining.

## Key Takeaways

ConvNeXt proves that locality and translation equivariance, combined with ViT training recipes, can match attention-based models. Key changes: depthwise 7×7 conv for large receptive field, inverted bottleneck (4× expansion), GELU + single activation per block, Layer Norm replacing Batch Norm, separate downsampling layers, and layer scale for deep model stability.

For practitioners, ConvNeXt-T is the default drop-in for ResNet-50, offering +6 points top-1 accuracy at similar FLOPs. ConvNeXt-B/L suit higher-compute scenarios. On mobile or edge hardware, depthwise convolutions may underperform on some accelerators — benchmark both before committing. Use timm for pretrained weights and reliable fine-tuning baselines.

