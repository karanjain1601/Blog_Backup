---
title: "Padding Mask — Variable-Length Sequences in Batches"
slug: "padding-mask-transformer"
description: "Handling variable-length sequences in batched Transformer training and inference by masking PAD tokens from attention, covering PyTorch and HuggingFace conventions plus sequence packing."
tags: ["deep-learning", "transformers"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR1BVcyBwcm9jZXNzIGV4YW1wbGVzIGluIHBhcmFsbGVsIGJhdGNoZXMsIGJ1dCBuYXR1cmFsIGxhbmd1YWdlIHNlcXVlbmNlcyB2YXJ5IHdpbGRseSBpbiBsZW5ndGguIEEgYmF0Y2ggb2Ygc2VudGVuY2VzIHdpdGggbGVuZ3RocyBbMywgNywgMTJdIG11c3QgYmUgcGFkZGVkIHRvIGEgY29tbW9uIGxlbmd0aCBvZiAxMiBiZWZvcmUgYmVpbmcgc3RhY2tlZCBpbnRvIGEgdGVuc29yLiBUaGUgcGFkZGluZyB0b2tlbnMgKFBBRCkgYXJlIG1lYW5pbmdsZXNzIOKAlCB0aGV5IGNhcnJ5IG5vIGluZm9ybWF0aW9uIOKAlCBidXQgd2l0aG91dCBleHBsaWNpdCBoYW5kbGluZywgdGhlIGF0dGVudGlvbiBtZWNoYW5pc20gd2lsbCBoYXBwaWx5IGF0dGVuZCB0byB0aGVtLCBjb3JydXB0aW5nIHRoZSBjb21wdXRhdGlvbiBhbmQgZGVncmFkaW5nIG1vZGVsIHF1YWxpdHkgZXNwZWNpYWxseSBhdCB0aGUgZW5kIG9mIHNob3J0ZXIgc2VxdWVuY2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZhcmlhYmxlLUxlbmd0aCBTZXF1ZW5jZXMgYW5kIHRoZSBQYWRkaW5nIFByb2JsZW0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlR3byBzZXBhcmF0ZSBtYXNraW5nIG5lZWRzIGFyaXNlIHdoZW4gcGFkZGluZyBpcyBwcmVzZW50LiBGaXJzdCwgbm8gcXVlcnkgdG9rZW4gc2hvdWxkIGF0dGVuZCB0byBQQUQga2V5IHBvc2l0aW9ucyDigJQgYSByZWFsIHRva2VuIGF0IHBvc2l0aW9uIDIgYXR0ZW5kaW5nIHRvIGEgUEFEIHRva2VuIGF0IHBvc2l0aW9uIDkgd291bGQgcHVsbCBtZWFuaW5nbGVzcyBpbmZvcm1hdGlvbiBpbnRvIGl0cyByZXByZXNlbnRhdGlvbi4gU2Vjb25kLCBQQUQgdG9rZW4gcXVlcmllcyB0aGVtc2VsdmVzIHByb2R1Y2UgbWVhbmluZ2xlc3Mgb3V0cHV0cywgd2hpY2ggbXVzdCBiZSB6ZXJvZWQgb3V0IG9yIGlnbm9yZWQgaW4gdGhlIGxvc3MgY29tcHV0YXRpb24uIFRoZSBwYWRkaW5nIG1hc2sgYWRkcmVzc2VzIHRoZSBmaXJzdCBjb25jZXJuIGJ5IGFkZGluZyAt4oieIHRvIGF0dGVudGlvbiBzY29yZXMgYXQgUEFEIGtleSBwb3NpdGlvbnMgYmVmb3JlIHNvZnRtYXgsIHByb2R1Y2luZyB6ZXJvIGF0dGVudGlvbiB3ZWlnaHQgb24gdGhvc2UgcG9zaXRpb25zLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsic2VxX2xlbnMgPSBbMywgNywgMTJdIOKGkiBwYWQgYWxsIHNlcXVlbmNlcyB0byBtYXhfbGVuID0gMTIiLCJQQUQgdG9rZW4gaWQgKHR5cGljYWxseSAwKSBhZGRlZCBhdCBwb3NpdGlvbnMgYmV5b25kIHRoZSByZWFsIHNlcXVlbmNlIGxlbmd0aCIsIkNyZWF0ZSBrZXlfcGFkZGluZ19tYXNrOiBUcnVlIGF0IFBBRCBwb3NpdGlvbnMgKFB5VG9yY2gpIG9yIDAgYXQgUEFEIHBvc2l0aW9ucyAoSHVnZ2luZ0ZhY2UpIiwiTWFzayBtYXBzIHRvIGFkZGl0aXZlIC3iiJ4gb24gUEFEIGtleSBjb2x1bW5zIGJlZm9yZSBzb2Z0bWF4IiwiTG9zczogaWdub3JlIFBBRCBwb3NpdGlvbnMgdmlhIGxhYmVsID0gLTEwMCBpbiBDcm9zc0VudHJvcHlMb3NzIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQ29udmVudGlvbiBNaXNtYXRjaDogUHlUb3JjaCB2cyBIdWdnaW5nRmFjZSIsImNvbnRlbnQiOiJQeVRvcmNoIG5uLk11bHRpaGVhZEF0dGVudGlvbiB1c2VzIGtleV9wYWRkaW5nX21hc2sgd2hlcmUgVHJ1ZSBtZWFucyBcdTAwMjdpZ25vcmUgdGhpcyBwb3NpdGlvblx1MDAyNyAoaWdub3JlPVRydWUpLiBIdWdnaW5nRmFjZSB0cmFuc2Zvcm1lcnMgdXNlcyBhdHRlbnRpb25fbWFzayB3aGVyZSAxIG1lYW5zIFx1MDAyN2F0dGVuZFx1MDAyNyBhbmQgMCBtZWFucyBcdTAwMjdpZ25vcmVcdTAwMjcgKGF0dGVuZD0xKS4gVGhlc2UgYXJlIG9wcG9zaXRlIGNvbnZlbnRpb25zIOKAlCBjb252ZXJ0aW5nIGJldHdlZW4gdGhlbSBpcyBhIGNvbW1vbiBzb3VyY2Ugb2YgYnVncyB3aGVuIG1peGluZyBQeVRvcmNoIGF0dGVudGlvbiBsYXllcnMgd2l0aCBIdWdnaW5nRmFjZSB0b2tlbml6ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbnN0cnVjdGluZyBhIFBhZGRpbmcgTWFzayBmcm9tIFNlcXVlbmNlIExlbmd0aHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdpdmVuIGEgbGlzdCBvZiBhY3R1YWwgc2VxdWVuY2UgbGVuZ3RocywgdGhlIHBhZGRpbmcgbWFzayBpcyBjb21wdXRlZCBieSBicm9hZGNhc3Rpbmc6IGNyZWF0ZSBhICgxLCBtYXhfbGVuKSByYW5nZSB0ZW5zb3Igb2YgcG9zaXRpb24gaW5kaWNlcyBhbmQgY29tcGFyZSBpdCBhZ2FpbnN0IGEgKEIsIDEpIHRlbnNvciBvZiBsZW5ndGhzLiBQb3NpdGlvbnMgd2hlcmUgaW5kZXggXHUwMDNlPSBsZW5ndGggYXJlIFBBRC4gVGhpcyB2ZWN0b3Jpc2VkIGNvbXBhcmlzb24gYXZvaWRzIGxvb3Bpbmcgb3ZlciB0aGUgYmF0Y2ggYW5kIGlzIGZ1bGx5IEdQVS1jb21wYXRpYmxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlB5VG9yY2ggdnMgSHVnZ2luZ0ZhY2UgQ29udmVudGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0d28gbWFqb3IgbGlicmFyaWVzIHVzZSBvcHBvc2l0ZSBzaWduIGNvbnZlbnRpb25zLiBQeVRvcmNoXHUwMDI3cyBubi5NdWx0aWhlYWRBdHRlbnRpb24gYWNjZXB0cyBrZXlfcGFkZGluZ19tYXNrIGFzIGEgQm9vbGVhbiB0ZW5zb3Igd2hlcmUgVHJ1ZSBmbGFncyBwb3NpdGlvbnMgdG8gaWdub3JlLCB3aGljaCBpdCBpbnRlcm5hbGx5IGNvbnZlcnRzIHRvIC3iiJ4gYWRkaXRpdmUgdmFsdWVzLiBIdWdnaW5nRmFjZSBtb2RlbHMgYWNjZXB0IGF0dGVudGlvbl9tYXNrIGFzIGEgZmxvYXQgb3IgaW50IHRlbnNvciB3aGVyZSAxIGZsYWdzIHJlYWwgdG9rZW5zIGFuZCAwIGZsYWdzIFBBRCDigJQgdGhlIG1vZGVsIGNvbnZlcnRzIDBzIHRvIC3iiJ4gYWRkaXRpdmUgdmFsdWVzLiBCb3RoIGFjaGlldmUgdGhlIHNhbWUgcmVzdWx0IGJ1dCByZXF1aXJlIGRpZmZlcmVudCBpbnB1dCBwcmVwYXJhdGlvbi4gV2hlbiB1c2luZyBhIEh1Z2dpbmdGYWNlIHRva2VuaXplciB3aXRoIGEgY3VzdG9tIFB5VG9yY2ggYXR0ZW50aW9uIGxheWVyLCBhbHdheXMgY2hlY2sgYW5kIGNvbnZlcnQgdGhlIGNvbnZlbnRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAxIOKAlCBQYWRkaW5nIE1hc2sgZnJvbSBTZXF1ZW5jZSBMZW5ndGhzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWZWN0b3Jpc2VkIGNvbnN0cnVjdGlvbiBvZiB0aGUgYWRkaXRpdmUgcGFkZGluZyBtYXNrIGZyb20gYSBsaXN0IG9mIHJlYWwgc2VxdWVuY2UgbGVuZ3RocywgcmV0dXJuaW5nIHNoYXBlIChCLCAxLCAxLCBtYXhfbGVuKSByZWFkeSB0byBicm9hZGNhc3Qgb3ZlciBhdHRlbnRpb24gc2NvcmUgdGVuc29ycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBtYWtlX3BhZGRpbmdfbWFzayhzZXFfbGVuczogbGlzdCwgbWF4X2xlbjogaW50LFxuICAgICAgICAgICAgICAgICAgICAgIGRldmljZTogc3RyID0gXHUwMDI3Y3B1XHUwMDI3KSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJcbiAgICBBZGRpdGl2ZSBwYWRkaW5nIG1hc2sgb2Ygc2hhcGUgKEIsIDEsIDEsIG1heF9sZW4pLlxuICAgIFZhbHVlOiAwLjAgYXQgcmVhbCB0b2tlbiBwb3NpdGlvbnMsIC1pbmYgYXQgUEFEIHBvc2l0aW9ucy5cbiAgICBCcm9hZGNhc3Qtc2FmZSB3aXRoIGF0dGVudGlvbiBzY29yZXMgb2Ygc2hhcGUgKEIsIEgsIExfcSwgTF9rKS5cbiAgICBcIlwiXCJcbiAgICBCICAgID0gbGVuKHNlcV9sZW5zKVxuICAgIGlkcyAgPSB0b3JjaC5hcmFuZ2UobWF4X2xlbiwgZGV2aWNlPWRldmljZSkudW5zcXVlZXplKDApICAjICgxLCBtYXhfbGVuKVxuICAgIGxlbnMgPSB0b3JjaC50ZW5zb3Ioc2VxX2xlbnMsIGRldmljZT1kZXZpY2UpLnVuc3F1ZWV6ZSgxKSAjIChCLCAxKVxuICAgIGlzX3BhZCA9IChpZHMgXHUwMDNlPSBsZW5zKS5mbG9hdCgpICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIChCLCBtYXhfbGVuKVxuICAgIG1hc2sgICA9IGlzX3BhZCAqIGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgMCBvciAtaW5mXG4gICAgcmV0dXJuIG1hc2sudmlldyhCLCAxLCAxLCBtYXhfbGVuKSAgICAgICAgICAgICAgICAgICAgICAgICAjIChCLDEsMSxtYXhfbGVuKVxuXG4jIERlbW8gd2l0aCB0aHJlZSBzZXF1ZW5jZXMgb2YgZGlmZmVyZW50IGxlbmd0aHNcbnNlcV9sZW5zID0gWzYsIDQsIDJdXG5tYXNrID0gbWFrZV9wYWRkaW5nX21hc2soc2VxX2xlbnMsIG1heF9sZW49NilcbnByaW50KFx1MDAyN01hc2sgc2hhcGU6XHUwMDI3LCBtYXNrLnNoYXBlKSAgIyAoMywgMSwgMSwgNilcbmZvciBpLCBsZW5ndGggaW4gZW51bWVyYXRlKHNlcV9sZW5zKTpcbiAgICByb3cgPSBtYXNrW2ksIDAsIDBdLnRvbGlzdCgpXG4gICAgbGFiZWxzID0gW1x1MDAyN29rXHUwMDI3IGlmIHYgPT0gMC4wIGVsc2UgXHUwMDI3LWluZlx1MDAyNyBmb3IgdiBpbiByb3ddXG4gICAgcHJpbnQoZlx1MDAyNyAgc2VxIHtpfSAobGVuPXtsZW5ndGh9KToge2xhYmVsc31cdTAwMjcpXG4jIEFkZGluZyB0aGlzIG1hc2sgdG8gKEIsIEgsIEwsIEwpIHNjb3JlcyBibG9ja3MgYWxsIFBBRCBrZXkgY29sdW1ucyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMiDigJQgbm4uTXVsdGloZWFkQXR0ZW50aW9uIHdpdGgga2V5X3BhZGRpbmdfbWFzayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVXNpbmcgUHlUb3JjaFx1MDAyN3MgYnVpbHQtaW4gTXVsdGloZWFkQXR0ZW50aW9uIHdpdGggdGhlIGtleV9wYWRkaW5nX21hc2sgcGFyYW1ldGVyLCB2ZXJpZnlpbmcgdGhhdCBhdHRlbnRpb24gd2VpZ2h0cyBvbiBQQUQga2V5IHBvc2l0aW9ucyBhcmUgZWZmZWN0aXZlbHkgemVyby4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIEwsIGRfbW9kZWwsIG5faGVhZHMgPSAzLCA2LCA2NCwgNFxuXG5taGEgPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oZW1iZWRfZGltPWRfbW9kZWwsIG51bV9oZWFkcz1uX2hlYWRzLCBiYXRjaF9maXJzdD1UcnVlKVxuXG4jIElucHV0IHNlcXVlbmNlczsgcGFkZGluZyBhbHJlYWR5IGFwcGxpZWQgKHplcm9zIGF0IFBBRCBwb3NpdGlvbnMpXG54ID0gdG9yY2gucmFuZG4oQiwgTCwgZF9tb2RlbClcbnNlcV9sZW5zID0gWzYsIDQsIDJdXG5cbiMgUHlUb3JjaCBrZXlfcGFkZGluZ19tYXNrOiBUcnVlID0gaWdub3JlIChQQUQpLCBGYWxzZSA9IGF0dGVuZCAocmVhbCB0b2tlbilcbmlkcyAgPSB0b3JjaC5hcmFuZ2UoTCkudW5zcXVlZXplKDApICAgICAgICAgICAgICAjICgxLCBMKVxubGVucyA9IHRvcmNoLnRlbnNvcihzZXFfbGVucykudW5zcXVlZXplKDEpICAgICAgICAjIChCLCAxKVxua2V5X3BhZGRpbmdfbWFzayA9IChpZHMgXHUwMDNlPSBsZW5zKSAgICAgICAgICAgICAgICAgICMgKEIsIEwpIGJvb2wsIFRydWUgYXQgUEFEXG5cbm91dCwgYXR0bl93ZWlnaHRzID0gbWhhKFxuICAgIHF1ZXJ5PXgsIGtleT14LCB2YWx1ZT14LFxuICAgIGtleV9wYWRkaW5nX21hc2s9a2V5X3BhZGRpbmdfbWFzayxcbiAgICBuZWVkX3dlaWdodHM9VHJ1ZSxcbiAgICBhdmVyYWdlX2F0dG5fd2VpZ2h0cz1GYWxzZSxcbilcbnByaW50KFx1MDAyN091dHB1dCBzaGFwZTogICAgICAgXHUwMDI3LCBvdXQuc2hhcGUpICAgICAgICAgICAjICgzLCA2LCA2NClcbnByaW50KFx1MDAyN0F0dG4gd2VpZ2h0cyBzaGFwZTogXHUwMDI3LCBhdHRuX3dlaWdodHMuc2hhcGUpICAjICgzLCA0LCA2LCA2KVxuXG4jIFZlcmlmeTogd2VpZ2h0cyBvbiBQQUQga2V5IGNvbHVtbnMgc2hvdWxkIGJlIG5lYXIgemVyb1xuZm9yIGksIGxlbmd0aCBpbiBlbnVtZXJhdGUoc2VxX2xlbnMpOlxuICAgIGlmIGxlbmd0aCBcdTAwM2MgTDpcbiAgICAgICAgcGFkX3cgPSBhdHRuX3dlaWdodHNbaSwgOiwgOmxlbmd0aCwgbGVuZ3RoOl0uYWJzKCkubWF4KCkuaXRlbSgpXG4gICAgICAgIHByaW50KGZcdTAwMjcgIHNlcSB7aX0gKGxlbj17bGVuZ3RofSk6IG1heCB3ZWlnaHQgb24gUEFEIGtleXMgPSB7cGFkX3c6LjJlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDMg4oCUIEh1Z2dpbmdGYWNlIEF0dGVudGlvbiBNYXNrIENvbnZlbnRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbnZlcnRpbmcgYmV0d2VlbiB0aGUgSHVnZ2luZ0ZhY2UgYXR0ZW50aW9uX21hc2sgKDE9YXR0ZW5kLCAwPVBBRCkgYW5kIHRoZSBhZGRpdGl2ZSAt4oieIGZvcm1hdCBleHBlY3RlZCBieSByYXcgYXR0ZW50aW9uIHNjb3JlIHRlbnNvcnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgaGZfdG9fYWRkaXRpdmVfbWFzayhhdHRlbnRpb25fbWFzazogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJcbiAgICBIdWdnaW5nRmFjZSBjb252ZW50aW9uOiBhdHRlbnRpb25fbWFza1tiLCBwb3NdID0gMSBhdHRlbmQsIDAgaWdub3JlLlxuICAgIENvbnZlcnQgdG8gYWRkaXRpdmUgbWFzazogMCBhdCByZWFsIHBvc2l0aW9ucywgLWluZiBhdCBQQUQgcG9zaXRpb25zLlxuICAgIElucHV0OiAoQiwgTCkgIC1cdTAwM2UgIE91dHB1dDogKEIsIDEsIDEsIEwpIGZvciBicm9hZGNhc3Rpbmcgb3ZlciAoQiwgSCwgTCwgTCkuXG4gICAgXCJcIlwiXG4gICAgaW52ZXJ0ZWQgPSAoMS4wIC0gYXR0ZW50aW9uX21hc2suZmxvYXQoKSkgKiBmbG9hdChcdTAwMjctaW5mXHUwMDI3KVxuICAgIHJldHVybiBpbnZlcnRlZC51bnNxdWVlemUoMSkudW5zcXVlZXplKDIpICAgICAgIyAoQiwgMSwgMSwgTClcblxuZGVmIGFkZGl0aXZlX3RvX2hmKG1hc2s6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiUmV2ZXJzZTogYWRkaXRpdmUgKEIsMSwxLEwpIC1cdTAwM2UgSEYgYXR0ZW50aW9uX21hc2sgKEIsIEwpLlwiXCJcIlxuICAgIGZsYXQgPSBtYXNrLnNxdWVlemUoMSkuc3F1ZWV6ZSgxKSAgICAgICAgICAgICAgIyAoQiwgTClcbiAgICByZXR1cm4gKGZsYXQgPT0gMC4wKS5sb25nKCkgICAgICAgICAgICAgICAgICAgICMgMSB3aGVyZSByZWFsLCAwIHdoZXJlIC1pbmZcblxuIyBTaW11bGF0ZSBIdWdnaW5nRmFjZSB0b2tlbml6ZXIgb3V0cHV0IChQQUQgaWQgPSAwKVxuaW5wdXRfaWRzID0gdG9yY2gudGVuc29yKFtcbiAgICBbMTAxLCAxMjM0LCA1Njc4LCA5MDEyLCAzNDU2LCAgMTAyXSwgICMgbGVuZ3RoIDZcbiAgICBbMTAxLCAyNDY4LCAxMzU3LCAgMTAyLCAgICAwLCAgICAwXSwgICMgbGVuZ3RoIDQsIHBhZHMgYXQgNCw1XG4gICAgWzEwMSwgIDk5OSwgIDEwMiwgICAgMCwgICAgMCwgICAgMF0sICAjIGxlbmd0aCAzLCBwYWRzIGF0IDMsNCw1XG5dKVxuaGZfbWFzayAgID0gKGlucHV0X2lkcyAhPSAwKS5sb25nKCkgICAgICAgIyAxPXJlYWwsIDA9UEFEICAoSHVnZ2luZ0ZhY2UpXG5wcmludChcdTAwMjdIRiBhdHRlbnRpb25fbWFzazpcdTAwMjcpXG5wcmludChoZl9tYXNrKVxuYWRkX21hc2sgPSBoZl90b19hZGRpdGl2ZV9tYXNrKGhmX21hc2spXG5wcmludChcdTAwMjdBZGRpdGl2ZSBtYXNrIChzZXEgMSk6XHUwMDI3LCBhZGRfbWFza1sxLCAwLCAwXS50b2xpc3QoKSlcbiMgWzAuMCwgMC4wLCAwLjAsIDAuMCwgLWluZiwgLWluZl0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDQg4oCUIFNlcXVlbmNlIFBhY2tpbmcgV2l0aG91dCBQYWRkaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgdHJhaW5pbmcgZWZmaWNpZW5jeSwgc2VxdWVuY2VzIGNhbiBiZSBwYWNrZWQgZW5kLXRvLWVuZCB3aXRob3V0IFBBRCB0b2tlbnMsIGVsaW1pbmF0aW5nIHdhc3RlZCBjb21wdXRlLiBQeVRvcmNoXHUwMDI3cyBwYWNrX3BhZGRlZF9zZXF1ZW5jZSAvIHBhZF9wYWNrZWRfc2VxdWVuY2UgaW1wbGVtZW50cyB0aGlzIGZvciBSTk4tc3R5bGUgbGF5ZXJzOyBmb3IgVHJhbnNmb3JtZXJzIHRoZSBzYW1lIGlkZWEgYXBwbGllcyB3aXRoIGN1c3RvbSBwb3NpdGlvbiBpZHMgYW5kIHNlZ21lbnQgYXR0ZW50aW9uIG1hc2tzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdG9yY2gubm4udXRpbHMucm5uIGltcG9ydCBwYWNrX3BhZGRlZF9zZXF1ZW5jZSwgcGFkX3BhY2tlZF9zZXF1ZW5jZVxuXG50b3JjaC5tYW51YWxfc2VlZCgxKVxuZF9tb2RlbCAgPSAzMlxuc2VxX2xlbnMgPSBbOCwgNSwgM10gICAgICAgIyBtdXN0IGJlIHNvcnRlZCBkZXNjZW5kaW5nIGZvciBwYWNrX3BhZGRlZF9zZXF1ZW5jZVxubWF4X2xlbiAgPSBtYXgoc2VxX2xlbnMpXG5CICAgICAgICA9IGxlbihzZXFfbGVucylcblxuIyBQYWRkZWQgaW5wdXQ6IChCLCBtYXhfbGVuLCBkX21vZGVsKVxueF9wYWRkZWQgPSB0b3JjaC5yYW5kbihCLCBtYXhfbGVuLCBkX21vZGVsKVxuZm9yIGksIGwgaW4gZW51bWVyYXRlKHNlcV9sZW5zKTpcbiAgICB4X3BhZGRlZFtpLCBsOl0gPSAwLjAgICMgemVyby1maWxsIFBBRCBwb3NpdGlvbnMgZm9yIGNsYXJpdHlcblxucHJpbnQoXHUwMDI3UGFkZGVkIHRlbnNvciBzaGFwZTpcdTAwMjcsIHhfcGFkZGVkLnNoYXBlKSAgICAgICAgICAjICgzLCA4LCAzMilcbnByaW50KFx1MDAyN1RvdGFsIGVsZW1lbnRzICh3aXRoIFBBRCk6XHUwMDI3LCBCICogbWF4X2xlbilcbnByaW50KFx1MDAyN1JlYWwgdG9rZW4gY291bnQ6ICAgICAgICAgXHUwMDI3LCBzdW0oc2VxX2xlbnMpKVxud2FzdGUgPSAxMDAgKiAoMSAtIHN1bShzZXFfbGVucykgLyAoQiAqIG1heF9sZW4pKVxucHJpbnQoZlx1MDAyN1dhc3RlZCBjb21wdXRlIChQQUQgZnJhY3Rpb24pOiB7d2FzdGU6LjFmfSVcdTAwMjcpXG5cbiMgUGFjazogcmVtb3ZlIFBBRCB0b2tlbnMsIGNvbmNhdGVuYXRlIG9ubHkgcmVhbCB0b2tlbnNcbmxlbmd0aHNfdCA9IHRvcmNoLnRlbnNvcihzZXFfbGVucylcbnBhY2tlZCA9IHBhY2tfcGFkZGVkX3NlcXVlbmNlKHhfcGFkZGVkLCBsZW5ndGhzX3QsIGJhdGNoX2ZpcnN0PVRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZW5mb3JjZV9zb3J0ZWQ9VHJ1ZSlcbnByaW50KFx1MDAyN1xcblBhY2tlZCBkYXRhIHNoYXBlOlx1MDAyNywgcGFja2VkLmRhdGEuc2hhcGUpICAgICAgICMgKDE2LCAzMikgcmVhbCB0b2tlbnMgb25seVxuXG4jIFVucGFjayBiYWNrIHRvIHBhZGRlZCBmb3IgbG9zcyBjb21wdXRhdGlvblxudW5wYWNrZWQsIG91dF9sZW5zID0gcGFkX3BhY2tlZF9zZXF1ZW5jZShwYWNrZWQsIGJhdGNoX2ZpcnN0PVRydWUpXG5wcmludChcdTAwMjdVbnBhY2tlZCBzaGFwZTpcdTAwMjcsIHVucGFja2VkLnNoYXBlKVxucHJpbnQoXHUwMDI3UmVjb3ZlcmVkIGxlbmd0aHM6XHUwMDI3LCBvdXRfbGVucy50b2xpc3QoKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYWRkaW5nIFN0cmF0ZWdpZXMgQ29tcGFyZWQifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiU3RyYXRlZ3kiLCJNb2RlbCBUeXBlIiwiUG9zaXRpb25zIE1hc2tlZCIsIkltcGxlbWVudGF0aW9uIiwiSEYgQ29udmVudGlvbiJdLCJyb3dzIjpbWyJObyBtYXNrIiwiQW55IiwiTm9uZSAoYXR0ZW5kIHRvIGFsbCkiLCJPbWl0IG1hc2sgcGFyYW1ldGVyIiwiYXR0ZW50aW9uX21hc2s6IGFsbCAxcyJdLFsiUGFkZGluZyBvbmx5IiwiRW5jb2RlciAoQkVSVCkiLCJQQUQga2V5IHBvc2l0aW9ucyIsImtleV9wYWRkaW5nX21hc2s9VHJ1ZSBhdCBQQUQiLCJhdHRlbnRpb25fbWFzazogMCBhdCBQQUQiXSxbIkNhdXNhbCBvbmx5IiwiRGVjb2RlciAoR1BUKSIsIkZ1dHVyZSBwb3NpdGlvbnMgKGogXHUwMDNlIGkpIiwiYXR0bl9tYXNrIHVwcGVyLXRyaSAtaW5mIiwiTm90IGEgc3RhbmRhcmQgSEYgcGFyYW0iXSxbIkNhdXNhbCArIHBhZGRpbmciLCJEZWNvZGVyIChiYXRjaGVkKSIsIkZ1dHVyZSArIFBBRCBrZXlzIiwiU3VtIGNhdXNhbCArIHBhZCBhZGRpdGl2ZSBtYXNrcyIsImF0dGVudGlvbl9tYXNrICsgY2F1c2FsIl0sWyJTZXF1ZW5jZSBwYWNraW5nIiwiQW55ICh0cmFpbmluZykiLCJObyBQQUQgdG9rZW5zIGF0IGFsbCIsInBhY2tfcGFkZGVkX3NlcXVlbmNlIG9yIGN1c3RvbSIsIlZhcmlhYmxlIHBvc2l0aW9uX2lkcyJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQYWRkaW5nIG1hc2tzIGFyZSBjb25jZXB0dWFsbHkgc2ltcGxlIGJ1dCBvcGVyYXRpb25hbGx5IGltcG9ydGFudDogdW5tYXNrZWQgUEFEIHRva2VucyBpbnRyb2R1Y2Ugc3B1cmlvdXMgc2lnbmFsLCBlc3BlY2lhbGx5IGluIHNob3J0IHNlcXVlbmNlcyB3aGVyZSBQQUQgdG9rZW5zIGZvcm0gYSBsYXJnZSBmcmFjdGlvbiBvZiB0aGUgYmF0Y2guIFNlcXVlbmNlIHBhY2tpbmcgZWxpbWluYXRlcyB0aGlzIG92ZXJoZWFkIGVudGlyZWx5IGR1cmluZyB0cmFpbmluZy4gQXQgaW5mZXJlbmNlLCBwYWRkaW5nIG1hc2tzIHJlbWFpbiBuZWNlc3Nhcnkgd2hlbiBwcm9jZXNzaW5nIHZhcmlhYmxlLWxlbmd0aCBiYXRjaGVzIGJlY2F1c2UgbW9zdCBzZXJ2aW5nIGZyYW1ld29ya3MgcGFkIHRvIGEgZml4ZWQgYnVja2V0IHNpemUgZm9yIG1lbW9yeSBsYXlvdXQgZWZmaWNpZW5jeS4ifV0="
---
# Padding Mask — Variable-Length Sequences in Batches

GPUs process examples in parallel batches, but natural language sequences vary wildly in length. A batch of sentences with lengths [3, 7, 12] must be padded to a common length of 12 before being stacked into a tensor. The padding tokens (PAD) are meaningless — they carry no information — but without explicit handling, the attention mechanism will happily attend to them, corrupting the computation and degrading model quality especially at the end of shorter sequences.

## Variable-Length Sequences and the Padding Problem

Two separate masking needs arise when padding is present. First, no query token should attend to PAD key positions — a real token at position 2 attending to a PAD token at position 9 would pull meaningless information into its representation. Second, PAD token queries themselves produce meaningless outputs, which must be zeroed out or ignored in the loss computation. The padding mask addresses the first concern by adding -∞ to attention scores at PAD key positions before softmax, producing zero attention weight on those positions.

- seq_lens = [3, 7, 12] → pad all sequences to max_len = 12
- PAD token id (typically 0) added at positions beyond the real sequence length
- Create key_padding_mask: True at PAD positions (PyTorch) or 0 at PAD positions (HuggingFace)
- Mask maps to additive -∞ on PAD key columns before softmax
- Loss: ignore PAD positions via label = -100 in CrossEntropyLoss

> **Convention Mismatch: PyTorch vs HuggingFace**: PyTorch nn.MultiheadAttention uses key_padding_mask where True means 'ignore this position' (ignore=True). HuggingFace transformers uses attention_mask where 1 means 'attend' and 0 means 'ignore' (attend=1). These are opposite conventions — converting between them is a common source of bugs when mixing PyTorch attention layers with HuggingFace tokenizers.

## Constructing a Padding Mask from Sequence Lengths

Given a list of actual sequence lengths, the padding mask is computed by broadcasting: create a (1, max_len) range tensor of position indices and compare it against a (B, 1) tensor of lengths. Positions where index >= length are PAD. This vectorised comparison avoids looping over the batch and is fully GPU-compatible.

## PyTorch vs HuggingFace Conventions

The two major libraries use opposite sign conventions. PyTorch's nn.MultiheadAttention accepts key_padding_mask as a Boolean tensor where True flags positions to ignore, which it internally converts to -∞ additive values. HuggingFace models accept attention_mask as a float or int tensor where 1 flags real tokens and 0 flags PAD — the model converts 0s to -∞ additive values. Both achieve the same result but require different input preparation. When using a HuggingFace tokenizer with a custom PyTorch attention layer, always check and convert the convention.

## Code 1 — Padding Mask from Sequence Lengths

Vectorised construction of the additive padding mask from a list of real sequence lengths, returning shape (B, 1, 1, max_len) ready to broadcast over attention score tensors.

```python
import torch

def make_padding_mask(seq_lens: list, max_len: int,
                      device: str = 'cpu') -> torch.Tensor:
    """
    Additive padding mask of shape (B, 1, 1, max_len).
    Value: 0.0 at real token positions, -inf at PAD positions.
    Broadcast-safe with attention scores of shape (B, H, L_q, L_k).
    """
    B    = len(seq_lens)
    ids  = torch.arange(max_len, device=device).unsqueeze(0)  # (1, max_len)
    lens = torch.tensor(seq_lens, device=device).unsqueeze(1) # (B, 1)
    is_pad = (ids >= lens).float()                             # (B, max_len)
    mask   = is_pad * float('-inf')                            # 0 or -inf
    return mask.view(B, 1, 1, max_len)                         # (B,1,1,max_len)

# Demo with three sequences of different lengths
seq_lens = [6, 4, 2]
mask = make_padding_mask(seq_lens, max_len=6)
print('Mask shape:', mask.shape)  # (3, 1, 1, 6)
for i, length in enumerate(seq_lens):
    row = mask[i, 0, 0].tolist()
    labels = ['ok' if v == 0.0 else '-inf' for v in row]
    print(f'  seq {i} (len={length}): {labels}')
# Adding this mask to (B, H, L, L) scores blocks all PAD key columns
```

## Code 2 — nn.MultiheadAttention with key_padding_mask

Using PyTorch's built-in MultiheadAttention with the key_padding_mask parameter, verifying that attention weights on PAD key positions are effectively zero.

```python
import torch
import torch.nn as nn

torch.manual_seed(0)
B, L, d_model, n_heads = 3, 6, 64, 4

mha = nn.MultiheadAttention(embed_dim=d_model, num_heads=n_heads, batch_first=True)

# Input sequences; padding already applied (zeros at PAD positions)
x = torch.randn(B, L, d_model)
seq_lens = [6, 4, 2]

# PyTorch key_padding_mask: True = ignore (PAD), False = attend (real token)
ids  = torch.arange(L).unsqueeze(0)              # (1, L)
lens = torch.tensor(seq_lens).unsqueeze(1)        # (B, 1)
key_padding_mask = (ids >= lens)                  # (B, L) bool, True at PAD

out, attn_weights = mha(
    query=x, key=x, value=x,
    key_padding_mask=key_padding_mask,
    need_weights=True,
    average_attn_weights=False,
)
print('Output shape:       ', out.shape)           # (3, 6, 64)
print('Attn weights shape: ', attn_weights.shape)  # (3, 4, 6, 6)

# Verify: weights on PAD key columns should be near zero
for i, length in enumerate(seq_lens):
    if length < L:
        pad_w = attn_weights[i, :, :length, length:].abs().max().item()
        print(f'  seq {i} (len={length}): max weight on PAD keys = {pad_w:.2e}')
```

## Code 3 — HuggingFace Attention Mask Convention

Converting between the HuggingFace attention_mask (1=attend, 0=PAD) and the additive -∞ format expected by raw attention score tensors.

```python
import torch

def hf_to_additive_mask(attention_mask: torch.Tensor) -> torch.Tensor:
    """
    HuggingFace convention: attention_mask[b, pos] = 1 attend, 0 ignore.
    Convert to additive mask: 0 at real positions, -inf at PAD positions.
    Input: (B, L)  ->  Output: (B, 1, 1, L) for broadcasting over (B, H, L, L).
    """
    inverted = (1.0 - attention_mask.float()) * float('-inf')
    return inverted.unsqueeze(1).unsqueeze(2)      # (B, 1, 1, L)

def additive_to_hf(mask: torch.Tensor) -> torch.Tensor:
    """Reverse: additive (B,1,1,L) -> HF attention_mask (B, L)."""
    flat = mask.squeeze(1).squeeze(1)              # (B, L)
    return (flat == 0.0).long()                    # 1 where real, 0 where -inf

# Simulate HuggingFace tokenizer output (PAD id = 0)
input_ids = torch.tensor([
    [101, 1234, 5678, 9012, 3456,  102],  # length 6
    [101, 2468, 1357,  102,    0,    0],  # length 4, pads at 4,5
    [101,  999,  102,    0,    0,    0],  # length 3, pads at 3,4,5
])
hf_mask   = (input_ids != 0).long()       # 1=real, 0=PAD  (HuggingFace)
print('HF attention_mask:')
print(hf_mask)
add_mask = hf_to_additive_mask(hf_mask)
print('Additive mask (seq 1):', add_mask[1, 0, 0].tolist())
# [0.0, 0.0, 0.0, 0.0, -inf, -inf]
```

## Code 4 — Sequence Packing Without Padding

For training efficiency, sequences can be packed end-to-end without PAD tokens, eliminating wasted compute. PyTorch's pack_padded_sequence / pad_packed_sequence implements this for RNN-style layers; for Transformers the same idea applies with custom position ids and segment attention masks.

```python
import torch
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

torch.manual_seed(1)
d_model  = 32
seq_lens = [8, 5, 3]       # must be sorted descending for pack_padded_sequence
max_len  = max(seq_lens)
B        = len(seq_lens)

# Padded input: (B, max_len, d_model)
x_padded = torch.randn(B, max_len, d_model)
for i, l in enumerate(seq_lens):
    x_padded[i, l:] = 0.0  # zero-fill PAD positions for clarity

print('Padded tensor shape:', x_padded.shape)          # (3, 8, 32)
print('Total elements (with PAD):', B * max_len)
print('Real token count:         ', sum(seq_lens))
waste = 100 * (1 - sum(seq_lens) / (B * max_len))
print(f'Wasted compute (PAD fraction): {waste:.1f}%')

# Pack: remove PAD tokens, concatenate only real tokens
lengths_t = torch.tensor(seq_lens)
packed = pack_padded_sequence(x_padded, lengths_t, batch_first=True,
                               enforce_sorted=True)
print('\nPacked data shape:', packed.data.shape)       # (16, 32) real tokens only

# Unpack back to padded for loss computation
unpacked, out_lens = pad_packed_sequence(packed, batch_first=True)
print('Unpacked shape:', unpacked.shape)
print('Recovered lengths:', out_lens.tolist())
```

## Padding Strategies Compared

| Strategy | Model Type | Positions Masked | Implementation | HF Convention |
| --- | --- | --- | --- | --- |
| No mask | Any | None (attend to all) | Omit mask parameter | attention_mask: all 1s |
| Padding only | Encoder (BERT) | PAD key positions | key_padding_mask=True at PAD | attention_mask: 0 at PAD |
| Causal only | Decoder (GPT) | Future positions (j > i) | attn_mask upper-tri -inf | Not a standard HF param |
| Causal + padding | Decoder (batched) | Future + PAD keys | Sum causal + pad additive masks | attention_mask + causal |
| Sequence packing | Any (training) | No PAD tokens at all | pack_padded_sequence or custom | Variable position_ids |

Padding masks are conceptually simple but operationally important: unmasked PAD tokens introduce spurious signal, especially in short sequences where PAD tokens form a large fraction of the batch. Sequence packing eliminates this overhead entirely during training. At inference, padding masks remain necessary when processing variable-length batches because most serving frameworks pad to a fixed bucket size for memory layout efficiency.

