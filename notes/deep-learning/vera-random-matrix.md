---
title: "VeRA — Vector-Based Random Matrix Adaptation for Extreme Parameter Efficiency"
slug: "vera-random-matrix"
description: "VeRA (Kopiczko et al. 2024) shares a single frozen random matrix pair across all adapter layers and learns only per-layer scaling vectors, achieving ~32× fewer trainable parameters than LoRA r=16 while remaining competitive on language tasks."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9SQSByZWR1Y2VzIHRyYWluYWJsZSBwYXJhbWV0ZXJzIGJ5IHVzaW5nIGxvdy1yYW5rIG1hdHJpY2VzIHBlciBsYXllciwgYnV0IGVhY2ggbGF5ZXIgc3RpbGwgbWFpbnRhaW5zIGl0cyBvd24gcHJpdmF0ZSBBIGFuZCBCIG1hdHJpY2VzLiBGb3IgYSA3QiBwYXJhbWV0ZXIgbW9kZWwgd2l0aCBMb1JBIHJhbms9MTYgYXBwbGllZCB0byBhbGwgYXR0ZW50aW9uIHByb2plY3Rpb25zLCB0cmFpbmFibGUgcGFyYW1ldGVycyByZWFjaCB+ODRNLiBWZVJBIChWZWN0b3ItYmFzZWQgUmFuZG9tIG1hdHJpeCBBZGFwdGF0aW9uLCBLb3BpY3prbyBldCBhbC4sIDIwMjQpIHB1c2hlcyBwYXJhbWV0ZXIgZWZmaWNpZW5jeSBmdXJ0aGVyOiBhIHNpbmdsZSBwYWlyIG9mIHJhbmRvbSBtYXRyaWNlcyBpcyBzaGFyZWQgKGZyb3plbikgYWNyb3NzIGFsbCBsYXllcnMsIGFuZCBvbmx5IHNtYWxsIHBlci1sYXllciBzY2FsaW5nIHZlY3RvcnMgYXJlIGxlYXJuZWQuIFRoaXMgcmVkdWNlcyB0cmFpbmFibGUgcGFyYW1ldGVycyB0byBhcHByb3hpbWF0ZWx5IDEuNE0g4oCUIGEgNjDDlyByZWR1Y3Rpb24gb3ZlciBMb1JBIHI9MTYg4oCUIHdoaWxlIGFjaGlldmluZyBzdXJwcmlzaW5nbHkgY29tcGV0aXRpdmUgdGFzayBwZXJmb3JtYW5jZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWZVJBIEFyY2hpdGVjdHVyZSDigJQgU2hhcmVkIFJhbmRvbSBNYXRyaWNlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gVmVSQSwgYSBzaW5nbGUgcmFuZG9tIG1hdHJpeCBBIOKIiCDihJ1ee3LDl2RfaW59IGFuZCBhIHNpbmdsZSByYW5kb20gbWF0cml4IEIg4oiIIOKEnV57ZF9vdXTDl3J9IGFyZSBnZW5lcmF0ZWQgb25jZSAodXNpbmcgYSBmaXhlZCByYW5kb20gc2VlZCkgYW5kIGtlcHQgZnJvemVuIGFjcm9zcyBhbGwgbGF5ZXJzLiBGb3IgZWFjaCBsYXllciBsLCBWZVJBIGludHJvZHVjZXMgdHdvIGxlYXJuYWJsZSBzY2FsaW5nIHZlY3RvcnM6IGJfZF5sIOKIiCDihJ1ee2Rfb3V0fSAoc2NhbGVzIHJvd3Mgb2YgQikgYW5kIGRfcl5sIOKIiCDihJ1eciAoc2NhbGVzIHJvd3Mgb2YgQSkuIFRoZSBmb3J3YXJkIHBhc3MgZm9yIGxheWVyIGwgaXM6IGggKz0gQsK3ZGlhZyhiX2RebCnCt0HCt2RpYWcoZF9yXmwpwrd4LiBUaGUgZGlhZ29uYWwgc2NhbGluZyB2ZWN0b3JzIHNlbGVjdCB3aGljaCBkaXJlY3Rpb25zIGluIHRoZSBzaGFyZWQgcmFuZG9tIGJhc2lzIG1hdHRlciBmb3IgZWFjaCBzcGVjaWZpYyBsYXllci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWZVJBIExheWVyIEltcGxlbWVudGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgaW1wbGVtZW50YXRpb24gaW5zdGFudGlhdGVzIHRoZSBzaGFyZWQgcmFuZG9tIG1hdHJpY2VzIGFzIGJ1ZmZlcnMgKG5vdCBwYXJhbWV0ZXJzKSBhdCBtb2RlbCBpbml0aWFsaXphdGlvbi4gUGVyLWxheWVyIHRyYWluYWJsZSB2ZWN0b3JzIGFyZSByZWdpc3RlcmVkIGFzIHBhcmFtZXRlcnMuIFRoZSBmb3J3YXJkIHBhc3MgY29tcHV0ZXMgdGhlIHNjYWxlZCByYW5kb20gcHJvamVjdGlvbiB2aWEgZWxlbWVudC13aXNlIG11bHRpcGxpY2F0aW9uIOKAlCBlcXVpdmFsZW50IHRvIHJvdy1zY2FsaW5nIG9mIHRoZSBtYXRyaWNlcyDigJQgd2hpY2ggYXZvaWRzIG1hdGVyaWFsaXppbmcgZnVsbCBkaWFnb25hbCBtYXRyaWNlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBtYXRoXG5cbmNsYXNzIFZlUkFMaW5lYXIobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJWZVJBIGFkYXB0ZXI6IHNoYXJlZCBmcm96ZW4gKEEsQiksIGxlYXJuYWJsZSBwZXItbGF5ZXIgc2NhbGluZyB2ZWN0b3JzLlwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2ZlYXR1cmVzOiBpbnQsIG91dF9mZWF0dXJlczogaW50LFxuICAgICAgICAgICAgICAgICByYW5rOiBpbnQsIHNoYXJlZF9BOiB0b3JjaC5UZW5zb3IsIHNoYXJlZF9COiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgIGFscGhhOiBmbG9hdCA9IDEuMCwgZHJvcG91dDogZmxvYXQgPSAwLjApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5yYW5rID0gcmFua1xuICAgICAgICBzZWxmLnNjYWxpbmcgPSBhbHBoYSAvIHJhbmtcbiAgICAgICAgIyBCYXNlIHdlaWdodCAoZnJvemVuKVxuICAgICAgICBzZWxmLndlaWdodCA9IG5uLlBhcmFtZXRlcih0b3JjaC5yYW5kbihvdXRfZmVhdHVyZXMsIGluX2ZlYXR1cmVzKSwgcmVxdWlyZXNfZ3JhZD1GYWxzZSlcbiAgICAgICAgc2VsZi5iaWFzID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKG91dF9mZWF0dXJlcyksIHJlcXVpcmVzX2dyYWQ9RmFsc2UpXG4gICAgICAgICMgU2hhcmVkIHJhbmRvbSBtYXRyaWNlcyAoZnJvemVuIGJ1ZmZlcnMsIE5PVCB0cmFpbmFibGUpXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFx1MDAyN3NoYXJlZF9BXHUwMDI3LCBzaGFyZWRfQSkgICMgKHJhbmssIGluX2ZlYXR1cmVzKVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdzaGFyZWRfQlx1MDAyNywgc2hhcmVkX0IpICAjIChvdXRfZmVhdHVyZXMsIHJhbmspXG4gICAgICAgICMgUGVyLWxheWVyIHRyYWluYWJsZSBzY2FsaW5nIHZlY3RvcnNcbiAgICAgICAgc2VsZi52ZWNfZCA9IG5uLlBhcmFtZXRlcih0b3JjaC5vbmVzKHJhbmspKSAgICAgICAjIHNjYWxlcyBBIHJvd3NcbiAgICAgICAgc2VsZi52ZWNfYiA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcyhvdXRfZmVhdHVyZXMpKSAgIyBzY2FsZXMgQiByb3dzXG4gICAgICAgIHNlbGYuZHJvcG91dCA9IG5uLkRyb3BvdXQoZHJvcG91dClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIGJhc2UgPSBubi5mdW5jdGlvbmFsLmxpbmVhcih4LCBzZWxmLndlaWdodCwgc2VsZi5iaWFzKVxuICAgICAgICAjIGRpYWcoZF9yKSBAIEE6IHNjYWxlIGVhY2ggcm93IG9mIEEsIHNoYXBlIChyYW5rLCBpbl9mZWF0dXJlcylcbiAgICAgICAgc2NhbGVkX0EgPSBzZWxmLnNoYXJlZF9BICogc2VsZi52ZWNfZC51bnNxdWVlemUoMSlcbiAgICAgICAgIyBCIEAgZGlhZyhiX2QpOiBzY2FsZSBlYWNoIHJvdyBvZiBCLCBzaGFwZSAob3V0X2ZlYXR1cmVzLCByYW5rKVxuICAgICAgICBzY2FsZWRfQiA9IHNlbGYuc2hhcmVkX0IgKiBzZWxmLnZlY19iLnVuc3F1ZWV6ZSgxKVxuICAgICAgICBsb3JhX291dCA9IG5uLmZ1bmN0aW9uYWwubGluZWFyKFxuICAgICAgICAgICAgbm4uZnVuY3Rpb25hbC5saW5lYXIoc2VsZi5kcm9wb3V0KHgpLCBzY2FsZWRfQSksIHNjYWxlZF9CXG4gICAgICAgIClcbiAgICAgICAgcmV0dXJuIGJhc2UgKyBsb3JhX291dCAqIHNlbGYuc2NhbGluZ1xuXG5yYW5rLCBkX2luLCBkX291dCA9IDE2LCA3NjgsIDc2OFxuc2hhcmVkX0EgPSB0b3JjaC5yYW5kbihyYW5rLCBkX2luKVxuc2hhcmVkX0IgPSB0b3JjaC5yYW5kbihkX291dCwgcmFuaylcbmxheWVyID0gVmVSQUxpbmVhcihkX2luLCBkX291dCwgcmFuaywgc2hhcmVkX0EsIHNoYXJlZF9CKVxueCA9IHRvcmNoLnJhbmRuKDQsIGRfaW4pXG5wcmludChmXHUwMDI3T3V0cHV0OiB7bGF5ZXIoeCkuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1RyYWluYWJsZSBwYXJhbXM6IHZlY19kPXtsYXllci52ZWNfZC5udW1lbCgpfSwgdmVjX2I9e2xheWVyLnZlY19iLm51bWVsKCl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBhcmFtZXRlciBDb3VudCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBtb2RlbCB3aXRoIEwgYWRhcHRlciBsYXllcnMsIGRfaW4gYW5kIGRfb3V0LCBhbmQgcmFuayByOiBMb1JBIGNvbnRyaWJ1dGVzIDLDl0zDl3LDl2QgcGFyYW1zIHBlciBsYXllciBwYWlyLiBWZVJBIGNvbnRyaWJ1dGVzIEzDlyhyK2Rfb3V0KSBmb3IgdGhlIHNjYWxpbmcgdmVjdG9ycywgcGx1cyBvbmUgc2hhcmVkIHBhaXIgKHLDl2RfaW4gKyBkX291dMOXcikgdGhhdCBkb2VzIG5vdCBzY2FsZSB3aXRoIEwuIEZvciBhIDdCIExMYU1BLXN0eWxlIG1vZGVsIHdpdGggTD0zMiBhdHRlbnRpb24gbGF5ZXJzLCBkPTQwOTYsIHI9MTY6IExvUkEgaGFzIDMyw5cyw5cxNsOXNDA5NiA9IDQuMk0gdHJhaW5hYmxlIHBhcmFtcyBwZXIgcHJvamVjdGlvbi4gVmVSQSBoYXMgMzLDlygxNis0MDk2KSA9IDEzMUsgdHJhaW5hYmxlIHBhcmFtcyDigJQgYSAzMsOXIHJlZHVjdGlvbiBwZXIgcHJvamVjdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBjb21wYXJlX3BhcmFtX2NvdW50cyhtb2RlbF9kaW1zOiBkaWN0LCByYW5rczogbGlzdCA9ICg0LCA4LCAxNiwgMzIpKTpcbiAgICBcIlwiXCJDb21wYXJlIExvUkEgdnMgVmVSQSB0cmFpbmFibGUgcGFyYW1zIGZvciBhIHRyYW5zZm9ybWVyIG1vZGVsLlwiXCJcIlxuICAgIG5fbGF5ZXJzID0gbW9kZWxfZGltc1tcdTAwMjduX2xheWVyc1x1MDAyN10gICAgICMgZS5nLiwgMzJcbiAgICBkX21vZGVsID0gbW9kZWxfZGltc1tcdTAwMjdkX21vZGVsXHUwMDI3XSAgICAgICAjIGUuZy4sIDQwOTZcbiAgICBuX3Byb2ogPSBtb2RlbF9kaW1zW1x1MDAyN25fcHJvamVjdGlvbnNcdTAwMjddICAjIFEsIEssIFYsIE8gPSA0XG4gICAgcHJpbnQoZlx1MDAyN01vZGVsOiB7bl9sYXllcnN9IGxheWVycywgZD17ZF9tb2RlbH0sIHtuX3Byb2p9IHByb2plY3Rpb25zXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjd7XCJSYW5rXCI6XHUwMDNlNn0gIHtcIkxvUkEgcGFyYW1zXCI6XHUwMDNlMTR9ICB7XCJWZVJBIHBhcmFtc1wiOlx1MDAzZTE0fSAge1wiUmF0aW9cIjpcdTAwM2U4fVx1MDAyNylcbiAgICBwcmludChcdTAwMjctXHUwMDI3ICogNTApXG4gICAgZm9yIHIgaW4gcmFua3M6XG4gICAgICAgIGxvcmFfcGFyYW1zID0gbl9sYXllcnMgKiBuX3Byb2ogKiAyICogciAqIGRfbW9kZWxcbiAgICAgICAgIyBWZVJBOiBwZXItbGF5ZXIgdmVjdG9ycyArIG9uZSBzaGFyZWQgcGFpciAoY291bnRlZCBvbmNlKVxuICAgICAgICB2ZXJhX3Blcl9sYXllciA9IG5fbGF5ZXJzICogbl9wcm9qICogKHIgKyBkX21vZGVsKVxuICAgICAgICB2ZXJhX3NoYXJlZCA9IDIgKiByICogZF9tb2RlbCAgIyBzaGFyZWQgQSBhbmQgQlxuICAgICAgICB2ZXJhX3BhcmFtcyA9IHZlcmFfcGVyX2xheWVyICsgdmVyYV9zaGFyZWRcbiAgICAgICAgcmF0aW8gPSBsb3JhX3BhcmFtcyAvIHZlcmFfcGFyYW1zXG4gICAgICAgIHByaW50KGZcdTAwMjd7cjpcdTAwM2U2fSAge2xvcmFfcGFyYW1zLzFlNjpcdTAwM2UxMi4yZn1NICB7dmVyYV9wYXJhbXMvMWU2Olx1MDAzZTEyLjNmfU0gIHtyYXRpbzpcdTAwM2U3LjFmfXhcdTAwMjcpXG5cbmNvbXBhcmVfcGFyYW1fY291bnRzKHtcdTAwMjduX2xheWVyc1x1MDAyNzogMzIsIFx1MDAyN2RfbW9kZWxcdTAwMjc6IDQwOTYsIFx1MDAyN25fcHJvamVjdGlvbnNcdTAwMjc6IDR9KVxucHJpbnQoKVxuY29tcGFyZV9wYXJhbV9jb3VudHMoe1x1MDAyN25fbGF5ZXJzXHUwMDI3OiAzMiwgXHUwMDI3ZF9tb2RlbFx1MDAyNzogNDA5NiwgXHUwMDI3bl9wcm9qZWN0aW9uc1x1MDAyNzogNH0sXG4gICAgICAgICAgICAgICAgICAgICByYW5rcz1bNjQsIDEyOF0pIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVmVSQSBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhaW5pbmcgVmVSQSByZXF1aXJlcyBnZW5lcmF0aW5nIHRoZSBzaGFyZWQgcmFuZG9tIG1hdHJpY2VzIG9uY2Ugd2l0aCBhIGZpeGVkIHNlZWQgYW5kIHJlcGxpY2F0aW5nIHRoZW0gYWNyb3NzIGFsbCBsYXllcnMuIE9ubHkgdGhlIHNjYWxpbmcgdmVjdG9ycyBhcmUgcGFzc2VkIHRvIHRoZSBvcHRpbWl6ZXIuIFRoZSBzaGFyZWQgbWF0cmljZXMgYXJlIHJlZ2lzdGVyZWQgYXMgYnVmZmVycyBzbyB0aGV5IG1vdmUgdG8gdGhlIGNvcnJlY3QgZGV2aWNlIGF1dG9tYXRpY2FsbHkgYnV0IGRvIG5vdCBjb25zdW1lIG9wdGltaXplciBzdGF0ZSAobm8gQWRhbSBtL3Ygc3RhdGlzdGljcyBmb3IgdGhlbSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0XG5cbmRlZiBidWlsZF92ZXJhX21vZGVsKG5fbGF5ZXJzOiBpbnQsIGRfbW9kZWw6IGludCwgcmFuazogaW50ID0gMTYsXG4gICAgICAgICAgICAgICAgICAgICBzZWVkOiBpbnQgPSA0MikgLVx1MDAzZSBubi5Nb2R1bGVMaXN0OlxuICAgIFwiXCJcIkJ1aWxkIGEgc3RhY2sgb2YgVmVSQSBsYXllcnMgc2hhcmluZyBhIHNpbmdsZSByYW5kb20gbWF0cml4IHBhaXIuXCJcIlwiXG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICBzaGFyZWRfQSA9IHRvcmNoLnJhbmRuKHJhbmssIGRfbW9kZWwpIC8gKHJhbmsgKiogMC41KSAgIyBub3JtYWxpemVkIGluaXRcbiAgICBzaGFyZWRfQiA9IHRvcmNoLnJhbmRuKGRfbW9kZWwsIHJhbmspIC8gKHJhbmsgKiogMC41KVxuICAgIGxheWVycyA9IG5uLk1vZHVsZUxpc3QoW1xuICAgICAgICBWZVJBTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIHJhbmssIHNoYXJlZF9BLmNsb25lKCksIHNoYXJlZF9CLmNsb25lKCkpXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKVxuICAgIF0pXG4gICAgcmV0dXJuIGxheWVyc1xuXG5kZWYgZ2V0X3ZlcmFfb3B0aW1pemVyKG1vZGVsOiBubi5Nb2R1bGVMaXN0LCBscjogZmxvYXQgPSAxZS0zKSAtXHUwMDNlIG9wdGltLkFkYW1XOlxuICAgIFwiXCJcIk9ubHkgb3B0aW1pemUgc2NhbGluZyB2ZWN0b3JzOyBpZ25vcmUgZnJvemVuIHdlaWdodHMgYW5kIHNoYXJlZCBidWZmZXJzLlwiXCJcIlxuICAgIHRyYWluYWJsZSA9IFtwIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWRdXG4gICAgdG90YWwgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIHRyYWluYWJsZSlcbiAgICBwcmludChmXHUwMDI3VmVSQSB0cmFpbmFibGUgcGFyYW1ldGVyczoge3RvdGFsOix9XHUwMDI3KVxuICAgIHJldHVybiBvcHRpbS5BZGFtVyh0cmFpbmFibGUsIGxyPWxyLCB3ZWlnaHRfZGVjYXk9MC4wMSlcblxuIyBTaW11bGF0ZSB0cmFpbmluZ1xubGF5ZXJzID0gYnVpbGRfdmVyYV9tb2RlbChuX2xheWVycz00LCBkX21vZGVsPTI1NiwgcmFuaz0xNilcbm9wdGltaXplciA9IGdldF92ZXJhX29wdGltaXplcihsYXllcnMpXG54ID0gdG9yY2gucmFuZG4oOCwgMjU2KVxuZm9yIHN0ZXAgaW4gcmFuZ2UoNSk6XG4gICAgaCA9IHhcbiAgICBmb3IgbGF5ZXIgaW4gbGF5ZXJzOlxuICAgICAgICBoID0gbGF5ZXIoaCkgKyBoICAjIHJlc2lkdWFsXG4gICAgbG9zcyA9IGgucG93KDIpLm1lYW4oKVxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgIGxvc3MuYmFja3dhcmQoKVxuICAgIG9wdGltaXplci5zdGVwKClcbiAgICBpZiBzdGVwICUgMiA9PSAwOlxuICAgICAgICBwcmludChmXHUwMDI3U3RlcCB7c3RlcH06IGxvc3M9e2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUXVhbGl0eSB2cyBQYXJhbWV0ZXIgRWZmaWNpZW5jeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVuY2htYXJraW5nIFZlUkEgYWdhaW5zdCBMb1JBIGFuZCBmdWxsIGZpbmUtdHVuaW5nIHJldmVhbHMgdGhhdCBWZVJBIGFjaGlldmVzIHN1cnByaXNpbmdseSBjb21wZXRpdGl2ZSBhY2N1cmFjeSBvbiBsYW5ndWFnZSB1bmRlcnN0YW5kaW5nIHRhc2tzLiBUaGUgZ2FwIHdpZGVucyBvbiB0YXNrcyB0aGF0IHJlcXVpcmUgdmVyeSBkaWZmZXJlbnQgcmVwcmVzZW50YXRpb25zIGFjcm9zcyBsYXllcnMsIHdoZXJlIHRoZSBzaGFyZWQgcmFuZG9tIGJhc2lzIGJlY29tZXMgYSBib3R0bGVuZWNrLiBIb3dldmVyLCBmb3Igc3RhbmRhcmQgaW5zdHJ1Y3Rpb24gZm9sbG93aW5nIGFuZCBjb21tb25zZW5zZSByZWFzb25pbmcsIFZlUkEgd2l0aGluIH4x4oCTMyUgb2YgTG9SQSByPTE2IGRlc3BpdGUgMzLDlyBmZXdlciBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBtYXRoXG5cbiMgQXBwcm94aW1hdGUgYmVuY2htYXJrIHJlc3VsdHMgZnJvbSBWZVJBIHBhcGVyIChLb3BpY3prbyBldCBhbC4gMjAyNClcbiMgRXZhbHVhdGVkIG9uIExMYU1BLTdCIHdpdGggY29tbW9uc2Vuc2UgYW5kIEdMVUUgYmVuY2htYXJrc1xuYmVuY2htYXJrX2RhdGEgPSBbXG4gICAge1x1MDAyN21ldGhvZFx1MDAyNzogXHUwMDI3RnVsbCBGaW5lLVR1bmluZ1x1MDAyNywgXHUwMDI3cGFyYW1zX01cdTAwMjc6IDcwMDAuMCwgXHUwMDI3YWNjdXJhY3lcdTAwMjc6IDAuODkyfSxcbiAgICB7XHUwMDI3bWV0aG9kXHUwMDI3OiBcdTAwMjdMb1JBIHI9MTZcdTAwMjcsICAgICAgICBcdTAwMjdwYXJhbXNfTVx1MDAyNzogODMuOSwgICBcdTAwMjdhY2N1cmFjeVx1MDAyNzogMC44NzF9LFxuICAgIHtcdTAwMjdtZXRob2RcdTAwMjc6IFx1MDAyN0xvUkEgcj00XHUwMDI3LCAgICAgICAgIFx1MDAyN3BhcmFtc19NXHUwMDI3OiAyMC45LCAgIFx1MDAyN2FjY3VyYWN5XHUwMDI3OiAwLjg1OX0sXG4gICAge1x1MDAyN21ldGhvZFx1MDAyNzogXHUwMDI3RG9SQSByPTE2XHUwMDI3LCAgICAgICAgXHUwMDI3cGFyYW1zX01cdTAwMjc6IDgzLjksICAgXHUwMDI3YWNjdXJhY3lcdTAwMjc6IDAuODc4fSxcbiAgICB7XHUwMDI3bWV0aG9kXHUwMDI3OiBcdTAwMjdWZVJBIHI9MjU2XHUwMDI3LCAgICAgICBcdTAwMjdwYXJhbXNfTVx1MDAyNzogMS40LCAgICBcdTAwMjdhY2N1cmFjeVx1MDAyNzogMC44NjJ9LFxuICAgIHtcdTAwMjdtZXRob2RcdTAwMjc6IFx1MDAyN0lBM1x1MDAyNywgICAgICAgICAgICAgIFx1MDAyN3BhcmFtc19NXHUwMDI3OiAwLjAyLCAgIFx1MDAyN2FjY3VyYWN5XHUwMDI3OiAwLjgyOH0sXG5dXG5cbnByaW50KGZcdTAwMjd7XCJNZXRob2RcIjpcdTAwM2MyMH0gIHtcIlBhcmFtcyAoTSlcIjpcdTAwM2UxMn0gIHtcIkFjY3VyYWN5XCI6XHUwMDNlMTB9ICB7XCJQYXJhbXMvRnVsbEZUXCI6XHUwMDNlMTR9XHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDY1KVxuZm9yIGVudHJ5IGluIGJlbmNobWFya19kYXRhOlxuICAgIGZyYWMgPSBlbnRyeVtcdTAwMjdwYXJhbXNfTVx1MDAyN10gLyA3MDAwLjBcbiAgICBwcmludChmXCJ7ZW50cnlbXHUwMDI3bWV0aG9kXHUwMDI3XTpcdTAwM2MyMH0gIHtlbnRyeVtcdTAwMjdwYXJhbXNfTVx1MDAyN106XHUwMDNlMTIuMWZ9ICBcIlxuICAgICAgICAgIGZcIntlbnRyeVtcdTAwMjdhY2N1cmFjeVx1MDAyN106XHUwMDNlMTAuM2Z9ICB7ZnJhYzpcdTAwM2UxMy40JX1cIilcblxuIyBFZmZpY2llbmN5IHNjb3JlOiBhY2N1cmFjeSAvIGxvZzEwKHBhcmFtcylcbnByaW50KFx1MDAyN1xcbkVmZmljaWVuY3kgc2NvcmUgKGFjY3VyYWN5IC8gbG9nMTAocGFyYW1zKSk6XHUwMDI3KVxuZm9yIGVudHJ5IGluIGJlbmNobWFya19kYXRhOlxuICAgIHNjb3JlID0gZW50cnlbXHUwMDI3YWNjdXJhY3lcdTAwMjddIC8gbWF0aC5sb2cxMChlbnRyeVtcdTAwMjdwYXJhbXNfTVx1MDAyN10gKiAxZTYgKyAxKVxuICAgIHByaW50KGZcIiAge2VudHJ5W1x1MDAyN21ldGhvZFx1MDAyN106XHUwMDNjMjB9OiB7c2NvcmU6LjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBSYW5kb20gTWF0cmljZXMgV29yayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRoZW9yZXRpY2FsIGp1c3RpZmljYXRpb24gZm9yIFZlUkEgY29tZXMgZnJvbSByYW5kb20gZmVhdHVyZSB0aGVvcnkuIEEgcmFuZG9tIG1hdHJpeCBBIHdpdGggaS5pLmQuIEdhdXNzaWFuIGVudHJpZXMgc3BhbnMgdGhlIGVudGlyZSBpbnB1dCBzcGFjZSBpbiBleHBlY3RhdGlvbiDigJQgYW55IGRpcmVjdGlvbiBjYW4gYmUgYXBwcm94aW1hdGVseSByZWFjaGVkIGJ5IGEgc3VpdGFibGUgbGluZWFyIGNvbWJpbmF0aW9uIG9mIHRoZSByb3dzLiBUaGUgc2NhbGluZyB2ZWN0b3IgZF9yIHNlbGVjdHMgd2hpY2ggcmFuZG9tIGRpcmVjdGlvbnMgdG8gYW1wbGlmeSwgZWZmZWN0aXZlbHkgY29uc3RydWN0aW5nIGEgdGFzay1zcGVjaWZpYyBwcm9qZWN0aW9uIGZyb20gdGhlIHNoYXJlZCByYW5kb20gYmFzaXMuIFRoaXMgaXMgYW5hbG9nb3VzIHRvIHJhbmRvbSBraXRjaGVuIHNpbmtzIChSYWhpbWkgXHUwMDI2IFJlY2h0LCAyMDA3KTogcmFuZG9tIGZlYXR1cmVzIGFwcHJveGltYXRlIGEgcmljaCBrZXJuZWwgZnVuY3Rpb24sIGFuZCB0aGUgbGVhcm5lZCB3ZWlnaHRzIHNlbGVjdCB0aGUgcmVsZXZhbnQgZmVhdHVyZXMgZm9yIHRoZSB0YXNrLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBFRlQgUGFyYW1ldGVyIEVmZmljaWVuY3kgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJUcmFpbmFibGUgUGFyYW1zICg3QikiLCIlIG9mIFRvdGFsIiwiUXVhbGl0eSB2cyBGdWxsIEZUIiwiSW5mZXJlbmNlIE92ZXJoZWFkIiwiTWVtb3J5IFNhdmluZ3MiXSwicm93cyI6W1siRnVsbCBGaW5lLVR1bmluZyIsIjcsMDAwTSIsIjEwMCUiLCJCYXNlbGluZSIsIk5vbmUiLCJOb25lIl0sWyJMb1JBIHI9MTYiLCJ+ODRNIiwifjEuMiUiLCItMSB0byAtMiUiLCJNZXJnZTogbm9uZTsgc2VwYXJhdGU6IG1pbmltYWwiLCJIaWdoIl0sWyJMb1JBIHI9NCIsIn4yMU0iLCJ+MC4zJSIsIi0yIHRvIC00JSIsIk1lcmdlOiBub25lOyBzZXBhcmF0ZTogbWluaW1hbCIsIlZlcnkgaGlnaCJdLFsiVmVSQSAocj0yNTYpIiwifjEuNE0iLCJ+MC4wMiUiLCItMiB0byAtMyUiLCJTaGFyZWQgYnVmZmVyczsgbWluaW1hbCIsIkV4dHJlbWUiXSxbIlByZWZpeCBUdW5pbmcgKFA9MTAwKSIsIn41TSIsIn4wLjA3JSIsIi0zIHRvIC01JSIsIkV4dHJhIEtWIGNhY2hlIHBlciBsYXllciIsIkhpZ2giXSxbIklBMyIsIn4wLjAyTSIsIn4wLjAwMDMlIiwiLTYgdG8gLTEwJSIsIk5vbmUiLCJFeHRyZW1lIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoeSBzaGFyZWQgcmFuZG9tIG1hdHJpY2VzIHdvcmsiLCJjb250ZW50IjoiVmVSQVx1MDAyN3Mgc2hhcmVkIHJhbmRvbSBtYXRyaWNlcyB3b3JrIGJlY2F1c2UgcmFuZG9tIHByb2plY3Rpb24gbWF0cmljZXMgc3BhbiBhIHJpY2ggZnVuY3Rpb24gc3BhY2Ug4oCUIGFueSBkaXJlY3Rpb24gY2FuIGJlIGFwcHJveGltYXRlbHkgcmVhY2hlZCBieSBzY2FsaW5nIHJhbmRvbSB2ZWN0b3JzLCBzaW1pbGFyIHRvIGhvdyByYW5kb20gZmVhdHVyZXMgYXBwcm94aW1hdGUga2VybmVsIG1ldGhvZHMuIFRoZSBwZXItbGF5ZXIgc2NhbGluZyB2ZWN0b3JzIGxlYXJuIHdoaWNoIGRpcmVjdGlvbnMgaW4gdGhpcyBzaGFyZWQgcmFuZG9tIGJhc2lzIGFyZSBtb3N0IHVzZWZ1bCBmb3IgZWFjaCBsYXllclx1MDAyN3MgdGFzay4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNoYXJlZCByYW5kb20gc2VlZDogdXNlIHRoZSBzYW1lIHNlZWQgYWNyb3NzIHByb2Nlc3NlcyBhbmQgcnVucyBzbyBzaGFyZWRfQSBhbmQgc2hhcmVkX0IgYXJlIHJlcHJvZHVjaWJsZS4iLCJSYW5rIGNob2ljZTogVmVSQSB1c2VzIG11Y2ggbGFyZ2VyIHJhbmtzIChyPTY04oCTMjU2KSB0aGFuIExvUkEgYmVjYXVzZSB0aGUgbWF0cmljZXMgYXJlIG5vdCBsZWFybmVkIOKAlCBtb3JlIGNvbHVtbnMgZ2l2ZSByaWNoZXIgYmFzaXMgY292ZXJhZ2UuIiwiTGltaXRhdGlvbjogc2hhcmVkIG1hdHJpY2VzIGxpbWl0IGV4cHJlc3Npdml0eSB3aGVuIHRhc2tzIHJlcXVpcmUgaGlnaGx5IGRpdmVyc2UgbGF5ZXItd2lzZSBhZGFwdGF0aW9ucyAoZS5nLiwgbXVsdGltb2RhbCBtb2RlbHMpLiIsIk1lbW9yeTogVmVSQVx1MDAyN3Mgc2hhcmVkIGJ1ZmZlcnMgYXJlIHN0b3JlZCBvbmNlIGFuZCBicm9hZGNhc3Qg4oCUIHNhdmVzIG1lbW9yeSBvbiBtdWx0aS1HUFUgc2V0dXBzIHZzIHBlci1sYXllciBMb1JBIG1hdHJpY2VzLiIsIlN0YWNraW5nOiBWZVJBIHNjYWxpbmcgdmVjdG9ycyBjYW4gYmUgdGFzay1zcGVjaWZpYzsgbG9hZCBkaWZmZXJlbnQgdmVjX2QgYW5kIHZlY19iIGZvciBkaWZmZXJlbnQgdGFza3Mgd2l0aCB0aGUgc2FtZSBiYXNlICsgc2hhcmVkIHJhbmRvbSBtYXRyaWNlcy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# VeRA — Vector-Based Random Matrix Adaptation for Extreme Parameter Efficiency

LoRA reduces trainable parameters by using low-rank matrices per layer, but each layer still maintains its own private A and B matrices. For a 7B parameter model with LoRA rank=16 applied to all attention projections, trainable parameters reach ~84M. VeRA (Vector-based Random matrix Adaptation, Kopiczko et al., 2024) pushes parameter efficiency further: a single pair of random matrices is shared (frozen) across all layers, and only small per-layer scaling vectors are learned. This reduces trainable parameters to approximately 1.4M — a 60× reduction over LoRA r=16 — while achieving surprisingly competitive task performance.

## VeRA Architecture — Shared Random Matrices

In VeRA, a single random matrix A ∈ ℝ^{r×d_in} and a single random matrix B ∈ ℝ^{d_out×r} are generated once (using a fixed random seed) and kept frozen across all layers. For each layer l, VeRA introduces two learnable scaling vectors: b_d^l ∈ ℝ^{d_out} (scales rows of B) and d_r^l ∈ ℝ^r (scales rows of A). The forward pass for layer l is: h += B·diag(b_d^l)·A·diag(d_r^l)·x. The diagonal scaling vectors select which directions in the shared random basis matter for each specific layer.

## VeRA Layer Implementation

The implementation instantiates the shared random matrices as buffers (not parameters) at model initialization. Per-layer trainable vectors are registered as parameters. The forward pass computes the scaled random projection via element-wise multiplication — equivalent to row-scaling of the matrices — which avoids materializing full diagonal matrices.

```python
import torch
import torch.nn as nn
import math

class VeRALinear(nn.Module):
    """VeRA adapter: shared frozen (A,B), learnable per-layer scaling vectors."""

    def __init__(self, in_features: int, out_features: int,
                 rank: int, shared_A: torch.Tensor, shared_B: torch.Tensor,
                 alpha: float = 1.0, dropout: float = 0.0):
        super().__init__()
        self.rank = rank
        self.scaling = alpha / rank
        # Base weight (frozen)
        self.weight = nn.Parameter(torch.randn(out_features, in_features), requires_grad=False)
        self.bias = nn.Parameter(torch.zeros(out_features), requires_grad=False)
        # Shared random matrices (frozen buffers, NOT trainable)
        self.register_buffer('shared_A', shared_A)  # (rank, in_features)
        self.register_buffer('shared_B', shared_B)  # (out_features, rank)
        # Per-layer trainable scaling vectors
        self.vec_d = nn.Parameter(torch.ones(rank))       # scales A rows
        self.vec_b = nn.Parameter(torch.zeros(out_features))  # scales B rows
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        base = nn.functional.linear(x, self.weight, self.bias)
        # diag(d_r) @ A: scale each row of A, shape (rank, in_features)
        scaled_A = self.shared_A * self.vec_d.unsqueeze(1)
        # B @ diag(b_d): scale each row of B, shape (out_features, rank)
        scaled_B = self.shared_B * self.vec_b.unsqueeze(1)
        lora_out = nn.functional.linear(
            nn.functional.linear(self.dropout(x), scaled_A), scaled_B
        )
        return base + lora_out * self.scaling

rank, d_in, d_out = 16, 768, 768
shared_A = torch.randn(rank, d_in)
shared_B = torch.randn(d_out, rank)
layer = VeRALinear(d_in, d_out, rank, shared_A, shared_B)
x = torch.randn(4, d_in)
print(f'Output: {layer(x).shape}')
print(f'Trainable params: vec_d={layer.vec_d.numel()}, vec_b={layer.vec_b.numel()}')
```

## Parameter Count Comparison

For a model with L adapter layers, d_in and d_out, and rank r: LoRA contributes 2×L×r×d params per layer pair. VeRA contributes L×(r+d_out) for the scaling vectors, plus one shared pair (r×d_in + d_out×r) that does not scale with L. For a 7B LLaMA-style model with L=32 attention layers, d=4096, r=16: LoRA has 32×2×16×4096 = 4.2M trainable params per projection. VeRA has 32×(16+4096) = 131K trainable params — a 32× reduction per projection.

```python
import torch

def compare_param_counts(model_dims: dict, ranks: list = (4, 8, 16, 32)):
    """Compare LoRA vs VeRA trainable params for a transformer model."""
    n_layers = model_dims['n_layers']     # e.g., 32
    d_model = model_dims['d_model']       # e.g., 4096
    n_proj = model_dims['n_projections']  # Q, K, V, O = 4
    print(f'Model: {n_layers} layers, d={d_model}, {n_proj} projections')
    print(f'{"Rank":>6}  {"LoRA params":>14}  {"VeRA params":>14}  {"Ratio":>8}')
    print('-' * 50)
    for r in ranks:
        lora_params = n_layers * n_proj * 2 * r * d_model
        # VeRA: per-layer vectors + one shared pair (counted once)
        vera_per_layer = n_layers * n_proj * (r + d_model)
        vera_shared = 2 * r * d_model  # shared A and B
        vera_params = vera_per_layer + vera_shared
        ratio = lora_params / vera_params
        print(f'{r:>6}  {lora_params/1e6:>12.2f}M  {vera_params/1e6:>12.3f}M  {ratio:>7.1f}x')

compare_param_counts({'n_layers': 32, 'd_model': 4096, 'n_projections': 4})
print()
compare_param_counts({'n_layers': 32, 'd_model': 4096, 'n_projections': 4},
                     ranks=[64, 128])
```

## VeRA Training

Training VeRA requires generating the shared random matrices once with a fixed seed and replicating them across all layers. Only the scaling vectors are passed to the optimizer. The shared matrices are registered as buffers so they move to the correct device automatically but do not consume optimizer state (no Adam m/v statistics for them).

```python
import torch
import torch.nn as nn
import torch.optim as optim
from typing import List

def build_vera_model(n_layers: int, d_model: int, rank: int = 16,
                     seed: int = 42) -> nn.ModuleList:
    """Build a stack of VeRA layers sharing a single random matrix pair."""
    torch.manual_seed(seed)
    shared_A = torch.randn(rank, d_model) / (rank ** 0.5)  # normalized init
    shared_B = torch.randn(d_model, rank) / (rank ** 0.5)
    layers = nn.ModuleList([
        VeRALinear(d_model, d_model, rank, shared_A.clone(), shared_B.clone())
        for _ in range(n_layers)
    ])
    return layers

def get_vera_optimizer(model: nn.ModuleList, lr: float = 1e-3) -> optim.AdamW:
    """Only optimize scaling vectors; ignore frozen weights and shared buffers."""
    trainable = [p for p in model.parameters() if p.requires_grad]
    total = sum(p.numel() for p in trainable)
    print(f'VeRA trainable parameters: {total:,}')
    return optim.AdamW(trainable, lr=lr, weight_decay=0.01)

# Simulate training
layers = build_vera_model(n_layers=4, d_model=256, rank=16)
optimizer = get_vera_optimizer(layers)
x = torch.randn(8, 256)
for step in range(5):
    h = x
    for layer in layers:
        h = layer(h) + h  # residual
    loss = h.pow(2).mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if step % 2 == 0:
        print(f'Step {step}: loss={loss.item():.4f}')
```

## Quality vs Parameter Efficiency

Benchmarking VeRA against LoRA and full fine-tuning reveals that VeRA achieves surprisingly competitive accuracy on language understanding tasks. The gap widens on tasks that require very different representations across layers, where the shared random basis becomes a bottleneck. However, for standard instruction following and commonsense reasoning, VeRA within ~1–3% of LoRA r=16 despite 32× fewer parameters.

```python
import torch
import math

# Approximate benchmark results from VeRA paper (Kopiczko et al. 2024)
# Evaluated on LLaMA-7B with commonsense and GLUE benchmarks
benchmark_data = [
    {'method': 'Full Fine-Tuning', 'params_M': 7000.0, 'accuracy': 0.892},
    {'method': 'LoRA r=16',        'params_M': 83.9,   'accuracy': 0.871},
    {'method': 'LoRA r=4',         'params_M': 20.9,   'accuracy': 0.859},
    {'method': 'DoRA r=16',        'params_M': 83.9,   'accuracy': 0.878},
    {'method': 'VeRA r=256',       'params_M': 1.4,    'accuracy': 0.862},
    {'method': 'IA3',              'params_M': 0.02,   'accuracy': 0.828},
]

print(f'{"Method":<20}  {"Params (M)":>12}  {"Accuracy":>10}  {"Params/FullFT":>14}')
print('-' * 65)
for entry in benchmark_data:
    frac = entry['params_M'] / 7000.0
    print(f"{entry['method']:<20}  {entry['params_M']:>12.1f}  "
          f"{entry['accuracy']:>10.3f}  {frac:>13.4%}")

# Efficiency score: accuracy / log10(params)
print('\nEfficiency score (accuracy / log10(params)):')
for entry in benchmark_data:
    score = entry['accuracy'] / math.log10(entry['params_M'] * 1e6 + 1)
    print(f"  {entry['method']:<20}: {score:.4f}")
```

## Why Random Matrices Work

The theoretical justification for VeRA comes from random feature theory. A random matrix A with i.i.d. Gaussian entries spans the entire input space in expectation — any direction can be approximately reached by a suitable linear combination of the rows. The scaling vector d_r selects which random directions to amplify, effectively constructing a task-specific projection from the shared random basis. This is analogous to random kitchen sinks (Rahimi & Recht, 2007): random features approximate a rich kernel function, and the learned weights select the relevant features for the task.

## PEFT Parameter Efficiency Comparison

| Method | Trainable Params (7B) | % of Total | Quality vs Full FT | Inference Overhead | Memory Savings |
| --- | --- | --- | --- | --- | --- |
| Full Fine-Tuning | 7,000M | 100% | Baseline | None | None |
| LoRA r=16 | ~84M | ~1.2% | -1 to -2% | Merge: none; separate: minimal | High |
| LoRA r=4 | ~21M | ~0.3% | -2 to -4% | Merge: none; separate: minimal | Very high |
| VeRA (r=256) | ~1.4M | ~0.02% | -2 to -3% | Shared buffers; minimal | Extreme |
| Prefix Tuning (P=100) | ~5M | ~0.07% | -3 to -5% | Extra KV cache per layer | High |
| IA3 | ~0.02M | ~0.0003% | -6 to -10% | None | Extreme |

> **Why shared random matrices work**: VeRA's shared random matrices work because random projection matrices span a rich function space — any direction can be approximately reached by scaling random vectors, similar to how random features approximate kernel methods. The per-layer scaling vectors learn which directions in this shared random basis are most useful for each layer's task.

- Shared random seed: use the same seed across processes and runs so shared_A and shared_B are reproducible.
- Rank choice: VeRA uses much larger ranks (r=64–256) than LoRA because the matrices are not learned — more columns give richer basis coverage.
- Limitation: shared matrices limit expressivity when tasks require highly diverse layer-wise adaptations (e.g., multimodal models).
- Memory: VeRA's shared buffers are stored once and broadcast — saves memory on multi-GPU setups vs per-layer LoRA matrices.
- Stacking: VeRA scaling vectors can be task-specific; load different vec_d and vec_b for different tasks with the same base + shared random matrices.

---

