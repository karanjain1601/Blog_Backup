---
title: "Causal Masking — Autoregressive Attention for Decoder"
slug: "causal-masking-transformer"
description: "How the causal look-ahead mask prevents decoders from seeing future tokens, plus KV cache mechanics for efficient inference and combined causal-plus-padding masks."
tags: ["deep-learning", "transformers"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhbnNmb3JtZXIgZGVjb2RlcnMgZ2VuZXJhdGUgdGV4dCBvbmUgdG9rZW4gYXQgYSB0aW1lLiBEdXJpbmcgdHJhaW5pbmcsIHRlYWNoZXIgZm9yY2luZyBwcmVzZW50cyB0aGUgZW50aXJlIHRhcmdldCBzZXF1ZW5jZSBhdCBvbmNlIOKAlCBidXQgYSBjcml0aWNhbCBpbnZhcmlhbnQgbXVzdCBiZSBwcmVzZXJ2ZWQ6IHBvc2l0aW9uIGkgbXVzdCBub3Qgc2VlIGFueSBpbmZvcm1hdGlvbiBmcm9tIHBvc2l0aW9ucyBpKzEsIGkrMiwg4oCmIChmdXR1cmUgdG9rZW5zKS4gV2l0aG91dCB0aGlzIGNvbnN0cmFpbnQgdGhlIG1vZGVsIHdvdWxkIHNpbXBseSBjb3B5IGZ1dHVyZSB0b2tlbnMgZnJvbSB0aGUgaW5wdXQgaW5zdGVhZCBvZiBsZWFybmluZyB0byBwcmVkaWN0IHRoZW0uIFRoZSBtZWNoYW5pc20gdGhhdCBlbmZvcmNlcyB0aGlzIGludmFyaWFudCBpcyB0aGUgKmNhdXNhbCBtYXNrKiwgYWxzbyBjYWxsZWQgdGhlIGxvb2stYWhlYWQgbWFzay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaHkgRGVjb2RlcnMgTmVlZCBDYXVzYWwgTWFza2luZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gc3RhbmRhcmQgc2NhbGVkIGRvdC1wcm9kdWN0IGF0dGVudGlvbiwgZXZlcnkgcXVlcnkgcG9zaXRpb24gYXR0ZW5kcyB0byBldmVyeSBrZXkgcG9zaXRpb24uIEZvciBlbmNvZGVyIHNlbGYtYXR0ZW50aW9uIHRoaXMgaXMgZGVzaXJhYmxlIOKAlCBhIHdvcmQgY2FuIHVzZSBjb250ZXh0IGZyb20gYm90aCBkaXJlY3Rpb25zLiBCdXQgZm9yIHRoZSBkZWNvZGVyLCB0aGlzIGlzIGNoZWF0aW5nOiBwb3NpdGlvbiAyIHNlZWluZyBwb3NpdGlvbiA1IG1lYW5zIHRoZSBtb2RlbCBoYXMgYmVlbiBnaXZlbiB0aGUgYW5zd2VyIGl0IGlzIHN1cHBvc2VkIHRvIHByZWRpY3QuIENhdXNhbCBtYXNraW5nIGJyZWFrcyB0aGVzZSBmb3J3YXJkLWxvb2tpbmcgYXR0ZW50aW9uIHBhdGhzLCByZXN0cmljdGluZyBlYWNoIHF1ZXJ5IHRvIGF0dGVuZCBvbmx5IHRvIGl0c2VsZiBhbmQgZWFybGllciBwb3NpdGlvbnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOnRydWUsIml0ZW1zIjpbIkNvbXB1dGUgcmF3IGF0dGVudGlvbiBzY29yZXM6IFMgPSBRS+G1gCAvIOKImmRfaywgc2hhcGUgKEwsIEwpIiwiQ3JlYXRlIGNhdXNhbCBtYXNrIE06IHVwcGVyLXRyaWFuZ3VsYXIgbWF0cml4IG9mIC3iiJ4gZm9yIHBvc2l0aW9ucyB3aGVyZSBqIFx1MDAzZSBpIiwiQWRkIG1hc2s6IFNfbWFza2VkID0gUyArIE0g4oCUIGZ1dHVyZSBwb3NpdGlvbnMgYmVjb21lIC3iiJ4iLCJBcHBseSBzb2Z0bWF4OiB3ZWlnaHRzID0gc29mdG1heChTX21hc2tlZCwgZGltPS0xKSDigJQgLeKIniBiZWNvbWVzIGV4YWN0bHkgMCIsIk91dHB1dDogTyA9IHdlaWdodHMgwrcgViDigJQgZnV0dXJlIHRva2VucyBjb250cmlidXRlIHplcm8gd2VpZ2h0Il19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IC3iiJ4gYW5kIE5vdCBaZXJvPyIsImNvbnRlbnQiOiJTZXR0aW5nIGxvZ2l0cyB0byAt4oieIGJlZm9yZSBzb2Z0bWF4IHlpZWxkcyBleGFjdGx5IHplcm8gaW4gdGhlIG91dHB1dCB3ZWlnaHRzIGJlY2F1c2UgZXhwKC3iiJ4pID0gMC4gU2V0dGluZyBsb2dpdHMgdG8gMCB3b3VsZCBub3QgbWFzayB0aGUgcG9zaXRpb24g4oCUIGl0IHdvdWxkIHJlY2VpdmUgYSBzb2Z0bWF4IHdlaWdodCBvZiAxL0wgaW5zdGVhZC4gVGhlIC3iiJ4gdHJpY2sgZXhwbG9pdHMgc29mdG1heCBub3JtYWxpc2F0aW9uIHRvIGNyZWF0ZSBwZXJmZWN0IG1hc2tpbmcgd2l0aCBubyBleHRyYSBjb21wdXRhdGlvbiBvdmVyaGVhZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgTG9vay1BaGVhZCBNYXNrIGFzIGFuIFVwcGVyIFRyaWFuZ3VsYXIgTWF0cml4In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2F1c2FsIG1hc2sgTSBpcyBhbiBMw5dMIG1hdHJpeCB3aGVyZSBNW2ksIGpdID0gLeKIniBpZiBqIFx1MDAzZSBpLCBlbHNlIDAuIEluIFB5VG9yY2ggdGhpcyBpcyBjcmVhdGVkIHdpdGggdG9yY2gudHJpdSh0b3JjaC5vbmVzKEwsIEwpLCBkaWFnb25hbD0xKSAqIC1mbG9hdChcdTAwMjdpbmZcdTAwMjcpLiBUaGUgZGlhZ29uYWw9MSBhcmd1bWVudCBzdGFydHMgdGhlIHVwcGVyIHRyaWFuZ2xlIG9uZSBzdGVwIGFib3ZlIHRoZSBtYWluIGRpYWdvbmFsLCBzbyBwb3NpdGlvbiBpIGNhbiBzdGlsbCBhdHRlbmQgdG8gaXRzZWxmIChqID0gaSkgYnV0IG5vdCB0byBhbnkgcG9zaXRpb24gaiBcdTAwM2UgaS4gVGhlIHJlc3VsdGluZyBhdHRlbnRpb24gd2VpZ2h0IG1hdHJpeCBpcyBsb3dlci10cmlhbmd1bGFyIGFmdGVyIHNvZnRtYXguIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS1YgQ2FjaGUg4oCUIFJlZHVjaW5nIE8oTMKyKSB0byBPKEwpIHBlciBTdGVwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdCBpbmZlcmVuY2UsIHRoZSBkZWNvZGVyIGdlbmVyYXRlcyB0b2tlbnMgc2VxdWVudGlhbGx5LiBXaXRob3V0IGEgS1YgY2FjaGUsIGNvbXB1dGluZyBhdHRlbnRpb24gYXQgc3RlcCB0IHJlcXVpcmVzIHJlcHJvY2Vzc2luZyBhbGwgdC0xIHByZXZpb3VzIHRva2VucyB0byBwcm9kdWNlIHRoZWlyIGtleXMgYW5kIHZhbHVlcyDigJQgTyh0KSB3b3JrIHBlciBzdGVwLCBPKEzCsikgdG90YWwgYWNyb3NzIGEgc2VxdWVuY2Ugb2YgbGVuZ3RoIEwuIFdpdGggYSBLViBjYWNoZSwgdGhlIGtleXMgYW5kIHZhbHVlcyBmb3IgcG9zaXRpb25zIDAgdGhyb3VnaCB0LTEgYXJlIHN0b3JlZCBhZnRlciB0aGVpciBmaXJzdCBjb21wdXRhdGlvbi4gU3RlcCB0IG9ubHkgY29tcHV0ZXMgUSwgSywgViBmb3IgdGhlIHNpbmdsZSBuZXcgdG9rZW4sIGFwcGVuZHMgSyBhbmQgViB0byB0aGUgY2FjaGUsIGFuZCBhdHRlbmRzIGFnYWluc3QgdGhlIGVudGlyZSBjYWNoZWQgSyBhbmQgVi4gVGhpcyByZWR1Y2VzIHBlci1zdGVwIGNvc3QgZnJvbSBPKEwpIHJlY29tcHV0ZSB0byBPKDEpIG5ldyBjb21wdXRhdGlvbiBwbHVzIE8oTCkgYXR0ZW50aW9uLCBhdCB0aGUgZXhwZW5zZSBvZiBtZW1vcnkgcHJvcG9ydGlvbmFsIHRvIEwgw5cgMiDDlyBuX2hlYWRzIMOXIGRfaGVhZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIENhdXNhbCBNYXNrIGZyb20gU2NyYXRjaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQnVpbGRpbmcgdGhlIHVwcGVyLXRyaWFuZ3VsYXIgLeKIniBtYXNrIGFuZCBhcHBseWluZyBpdCBpbnNpZGUgc2NhbGVkIGRvdC1wcm9kdWN0IGF0dGVudGlvbi4gUG9zaXRpb24gMCBhdHRlbmRzIG9ubHkgdG8gaXRzZWxmOyBwb3NpdGlvbiA1IGF0dGVuZHMgdG8gYWxsIDYgcG9zaXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBtYXRoXG5cbmRlZiBtYWtlX2NhdXNhbF9tYXNrKHNlcV9sZW46IGludCwgZGV2aWNlOiBzdHIgPSBcdTAwMjdjcHVcdTAwMjcpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlVwcGVyLXRyaWFuZ3VsYXIgbWF0cml4IG9mIC1pbmY7IHBvc2l0aW9ucyAoaSxqKSB3aXRoIGpcdTAwM2VpIGdldCAtaW5mLlwiXCJcIlxuICAgIG9uZXMgPSB0b3JjaC5vbmVzKHNlcV9sZW4sIHNlcV9sZW4sIGRldmljZT1kZXZpY2UpXG4gICAgbWFzayA9IHRvcmNoLnRyaXUob25lcywgZGlhZ29uYWw9MSkgICAgICAgIyAxIHdoZXJlIGogXHUwMDNlIGksIDAgb3RoZXJ3aXNlXG4gICAgcmV0dXJuIG1hc2sgKiBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSAgICAgICAgICAgICAgICMgc2hhcGUgKEwsIEwpXG5cbmRlZiBjYXVzYWxfYXR0ZW50aW9uKFE6IHRvcmNoLlRlbnNvciwgSzogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgVjogdG9yY2guVGVuc29yKSAtXHUwMDNlIHR1cGxlOlxuICAgIFwiXCJcIlNjYWxlZCBkb3QtcHJvZHVjdCBhdHRlbnRpb24gd2l0aCBjYXVzYWwgbWFzay4gUS9LL1Y6IChCLCBILCBMLCBkKS5cIlwiXCJcbiAgICBkX2sgID0gUS5zaXplKC0xKVxuICAgIEwgICAgPSBRLnNpemUoLTIpXG4gICAgc2NvcmVzID0gdG9yY2gubWF0bXVsKFEsIEsudHJhbnNwb3NlKC0yLCAtMSkpIC8gbWF0aC5zcXJ0KGRfaylcbiAgICBtYXNrICAgPSBtYWtlX2NhdXNhbF9tYXNrKEwsIGRldmljZT1RLmRldmljZSlcbiAgICBzY29yZXMgPSBzY29yZXMgKyBtYXNrICAgICAgICAgICAgICAgICAgICAjIGJyb2FkY2FzdCBvdmVyIGJhdGNoIGFuZCBoZWFkc1xuICAgIHdlaWdodHMgPSBGLnNvZnRtYXgoc2NvcmVzLCBkaW09LTEpXG4gICAgcmV0dXJuIHRvcmNoLm1hdG11bCh3ZWlnaHRzLCBWKSwgd2VpZ2h0c1xuXG4jIERlbW86IGJhdGNoPTIsIGhlYWRzPTQsIHNlcV9sZW49NiwgZF9rPTE2XG50b3JjaC5tYW51YWxfc2VlZCg0MilcbkIsIEgsIEwsIGQgPSAyLCA0LCA2LCAxNlxuUSA9IHRvcmNoLnJhbmRuKEIsIEgsIEwsIGQpXG5LID0gdG9yY2gucmFuZG4oQiwgSCwgTCwgZClcblYgPSB0b3JjaC5yYW5kbihCLCBILCBMLCBkKVxub3V0LCB3ZWlnaHRzID0gY2F1c2FsX2F0dGVudGlvbihRLCBLLCBWKVxucHJpbnQoXHUwMDI3T3V0cHV0IHNoYXBlOlx1MDAyNywgb3V0LnNoYXBlKSAgICAgICAgICAgICAjICgyLCA0LCA2LCAxNilcbnByaW50KFx1MDAyN1BvcyAwIHdlaWdodHMgKG9ubHkgc2VsZik6XHUwMDI3LCB3ZWlnaHRzWzAsIDAsIDBdLmRldGFjaCgpLm51bXB5KCkucm91bmQoMykpXG5wcmludChcdTAwMjdQb3MgNSB3ZWlnaHRzIChhbGwgc2l4KTogXHUwMDI3LCB3ZWlnaHRzWzAsIDAsIDVdLmRldGFjaCgpLm51bXB5KCkucm91bmQoMykpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSAyIOKAlCBWZXJpZnlpbmcgQ2F1c2FsIEF0dGVudGlvbiBDb3JyZWN0bmVzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBxdWFudGl0YXRpdmUgY2hlY2sgY29uZmlybWluZyB0aGF0IHRoZSBmdXR1cmUtYXR0ZW50aW9uIHdlaWdodCBzdW0gaXMgZWZmZWN0aXZlbHkgemVybyBmb3IgZXZlcnkgcXVlcnkgcG9zaXRpb24sIHByb3ZpbmcgdGhlIGNhdXNhbCBpbnZhcmlhbnQgaG9sZHMgbnVtZXJpY2FsbHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbWFrZV9jYXVzYWxfbWFzayhMLCBkZXZpY2U9XHUwMDI3Y3B1XHUwMDI3KTpcbiAgICByZXR1cm4gdG9yY2gudHJpdSh0b3JjaC5vbmVzKEwsIEwsIGRldmljZT1kZXZpY2UpLCBkaWFnb25hbD0xKSAqIGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpXG5cbmRlZiBjYXVzYWxfc2RwYShRLCBLLCBWKTpcbiAgICBkX2sgPSBRLnNpemUoLTEpXG4gICAgTCAgID0gUS5zaXplKC0yKVxuICAgIHNjb3JlcyAgPSBRIEAgSy50cmFuc3Bvc2UoLTIsIC0xKSAvIG1hdGguc3FydChkX2spXG4gICAgc2NvcmVzICs9IG1ha2VfY2F1c2FsX21hc2soTCwgUS5kZXZpY2UpXG4gICAgdyA9IEYuc29mdG1heChzY29yZXMsIGRpbT0tMSlcbiAgICByZXR1cm4gdyBAIFYsIHdcblxuIyBVc2UgTD01IGZvciByZWFkYWJsZSBvdXRwdXRcbnRvcmNoLm1hbnVhbF9zZWVkKDcpXG5MID0gNVxuUSA9IEsgPSBWID0gdG9yY2gucmFuZG4oMSwgMSwgTCwgOCkgICAjIHNoYXJlZCBRLCBLLCBWIGZvciBzaW1wbGljaXR5XG5fLCBhdHRuID0gY2F1c2FsX3NkcGEoUSwgSywgVilcbncgPSBhdHRuWzAsIDBdLmRldGFjaCgpXG5cbnByaW50KFx1MDAyN0F0dGVudGlvbiB3ZWlnaHQgbWF0cml4IChyb3dzPXF1ZXJpZXMsIGNvbHM9a2V5cyk6XHUwMDI3KVxucHJpbnQobnAuYXJyYXkyc3RyaW5nKHcubnVtcHkoKSwgcHJlY2lzaW9uPTMsIHN1cHByZXNzX3NtYWxsPVRydWUpKVxucHJpbnQoKVxuYWxsX29rID0gVHJ1ZVxuZm9yIGkgaW4gcmFuZ2UoTCk6XG4gICAgZnV0dXJlID0gd1tpLCBpKzE6XS5zdW0oKS5pdGVtKClcbiAgICBwYXN0ICAgPSB3W2ksIDppKzFdLnN1bSgpLml0ZW0oKVxuICAgIG9rID0gZnV0dXJlIFx1MDAzYyAxZS02XG4gICAgYWxsX29rID0gYWxsX29rIGFuZCBva1xuICAgIHByaW50KGZcdTAwMjcgIHBvcyB7aX06IHBhc3Rfc3VtPXtwYXN0Oi40Zn0gIGZ1dHVyZV9zdW09e2Z1dHVyZTouMmV9ICBvaz17b2t9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0NhdXNhbCBpbnZhcmlhbnQgaG9sZHM6IHthbGxfb2t9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMyDigJQgS1YgQ2FjaGUgZm9yIEF1dG9yZWdyZXNzaXZlIEluZmVyZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBtaW5pbWFsIGF0dGVudGlvbiBtb2R1bGUgdGhhdCBjYWNoZXMga2V5cyBhbmQgdmFsdWVzIGFjcm9zcyBnZW5lcmF0aW9uIHN0ZXBzLCBwcm9jZXNzaW5nIG9uZSBuZXcgdG9rZW4gcGVyIGZvcndhcmQgcGFzcyBpbnN0ZWFkIG9mIHJlY29tcHV0aW5nIGFsbCBwYXN0IHRva2Vucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBtYXRoXG5cbmNsYXNzIENhY2hlZFNlbGZBdHRlbnRpb24obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTaW5nbGUtaGVhZCBhdHRlbnRpb24gd2l0aCBLViBjYWNoZSBmb3Igc3RlcC1ieS1zdGVwIGluZmVyZW5jZS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbDogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZCAgPSBkX21vZGVsXG4gICAgICAgIHNlbGYuV3EgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XayA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLld2ID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuV28gPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5jYWNoZV9rID0gc2VsZi5jYWNoZV92ID0gTm9uZVxuXG4gICAgZGVmIHJlc2V0X2NhY2hlKHNlbGYpOlxuICAgICAgICBzZWxmLmNhY2hlX2sgPSBzZWxmLmNhY2hlX3YgPSBOb25lXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOiAgIyB4OiAoQiwgMSwgZClcbiAgICAgICAgcSwgaywgdiA9IHNlbGYuV3EoeCksIHNlbGYuV2soeCksIHNlbGYuV3YoeClcbiAgICAgICAgc2VsZi5jYWNoZV9rID0gayBpZiBzZWxmLmNhY2hlX2sgaXMgTm9uZSBlbHNlIHRvcmNoLmNhdChbc2VsZi5jYWNoZV9rLCBrXSwgMSlcbiAgICAgICAgc2VsZi5jYWNoZV92ID0gdiBpZiBzZWxmLmNhY2hlX3YgaXMgTm9uZSBlbHNlIHRvcmNoLmNhdChbc2VsZi5jYWNoZV92LCB2XSwgMSlcbiAgICAgICAgIyBBdHRlbmQ6IG5ldyBxdWVyeSB2cyBhbGwgY2FjaGVkIGtleXMgKG5vIGNhdXNhbCBtYXNrIG5lZWRlZDogc2luZ2xlIG5ldyBRKVxuICAgICAgICBzY29yZXMgID0gcSBAIHNlbGYuY2FjaGVfay50cmFuc3Bvc2UoLTIsIC0xKSAvIG1hdGguc3FydChzZWxmLmQpXG4gICAgICAgIHdlaWdodHMgPSB0b3JjaC5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKVxuICAgICAgICByZXR1cm4gc2VsZi5Xbyh3ZWlnaHRzIEAgc2VsZi5jYWNoZV92KVxuXG4jIFNpbXVsYXRlIDgtc3RlcCBhdXRvcmVncmVzc2l2ZSBkZWNvZGluZ1xubW9kZWwgPSBDYWNoZWRTZWxmQXR0ZW50aW9uKGRfbW9kZWw9NjQpXG5mb3Igc3RlcCBpbiByYW5nZSg4KTpcbiAgICB0b2sgPSB0b3JjaC5yYW5kbigxLCAxLCA2NCkgICAgICAgICAjIHNpbmdsZSBuZXcgdG9rZW4gZW1iZWRkaW5nXG4gICAgb3V0ID0gbW9kZWwodG9rKVxuICAgIExfY2FjaGUgPSBtb2RlbC5jYWNoZV9rLnNoYXBlWzFdXG4gICAgcHJpbnQoZlx1MDAyN1N0ZXAge3N0ZXArMX06IG91dD17dHVwbGUob3V0LnNoYXBlKX0sIEtWIGNhY2hlIGxlbmd0aD17TF9jYWNoZX1cdTAwMjcpXG5wcmludChcdTAwMjdGdWxsIHJlY29tcHV0ZSBjb3N0OiBPKExeMikgdG90YWw7IEtWIGNhY2hlIGNvc3Q6IE8oTCkgcGVyIHN0ZXBcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSA0IOKAlCBDb21iaW5lZCBDYXVzYWwgYW5kIFBhZGRpbmcgTWFzayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmF0Y2hlZCBkZWNvZGluZyBuZWVkcyBib3RoIGEgY2F1c2FsIG1hc2sgKG5vIGZ1dHVyZSB0b2tlbnMpIGFuZCBhIHBhZGRpbmcgbWFzayAobm8gUEFELWtleSBhdHRlbnRpb24pLiBCb3RoIHVzZSBhZGRpdGl2ZSAt4oieIG1hc2tpbmcsIHNvIHRoZXkgY2FuIGJlIHN1bW1lZCBkaXJlY3RseSBiZWZvcmUgc29mdG1heC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5kZWYgbWFrZV9jYXVzYWxfbWFzayhMOiBpbnQsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIHJldHVybiB0b3JjaC50cml1KHRvcmNoLm9uZXMoTCwgTCwgZGV2aWNlPWRldmljZSksIGRpYWdvbmFsPTEpICogZmxvYXQoXHUwMDI3LWluZlx1MDAyNylcblxuZGVmIG1ha2VfcGFkZGluZ19tYXNrKHNlcV9sZW5zLCBtYXhfbGVuOiBpbnQsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlJldHVybnMgKEIsIDEsIG1heF9sZW4pIGFkZGl0aXZlIG1hc2s6IC1pbmYgYXQgUEFEIHBvc2l0aW9ucy5cIlwiXCJcbiAgICBpZHMgICA9IHRvcmNoLmFyYW5nZShtYXhfbGVuLCBkZXZpY2U9ZGV2aWNlKS51bnNxdWVlemUoMCkgICAjICgxLCBMKVxuICAgIGxlbnMgID0gdG9yY2gudGVuc29yKHNlcV9sZW5zLCBkZXZpY2U9ZGV2aWNlKS51bnNxdWVlemUoMSkgICMgKEIsIDEpXG4gICAgaXNfcGFkID0gKGlkcyBcdTAwM2U9IGxlbnMpLmZsb2F0KCkgKiBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSAgICAgICAgICAgICAgICMgKEIsIEwpXG4gICAgcmV0dXJuIGlzX3BhZC51bnNxdWVlemUoMSkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIDEsIEwpXG5cbmRlZiBjb21iaW5lZF9tYXNrKHNlcV9sZW5zLCBtYXhfbGVuOiBpbnQsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlJldHVybnMgKEIsIG1heF9sZW4sIG1heF9sZW4pIGNvbWJpbmVkIGFkZGl0aXZlIG1hc2suXCJcIlwiXG4gICAgY2F1c2FsID0gbWFrZV9jYXVzYWxfbWFzayhtYXhfbGVuLCBkZXZpY2UpICAgICAgICAgICAgICAgICAgICMgKEwsIEwpXG4gICAgcGFkICAgID0gbWFrZV9wYWRkaW5nX21hc2soc2VxX2xlbnMsIG1heF9sZW4sIGRldmljZSkgICAgICAgICMgKEIsIDEsIEwpXG4gICAgcmV0dXJuIGNhdXNhbC51bnNxdWVlemUoMCkgKyBwYWQgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIEwsIEwpXG5cbiMgQmF0Y2g6IHNlcSAwIGxlbmd0aD01IChmdWxsKSwgc2VxIDEgbGVuZ3RoPTMgKHBhZGRlZCB0byA1KVxuc2VxX2xlbnMgPSBbNSwgM11cbm1hc2sgPSBjb21iaW5lZF9tYXNrKHNlcV9sZW5zLCBtYXhfbGVuPTUpXG5wcmludChcdTAwMjdNYXNrIHNoYXBlOlx1MDAyNywgbWFzay5zaGFwZSkgICAgICAgICAgICAgICMgKDIsIDUsIDUpXG5wcmludChcdTAwMjdcXG5TZXEgMCAobm8gcGFkZGluZywgb25seSBjYXVzYWwgLWluZiBhYm92ZSBkaWFnb25hbCk6XHUwMDI3KVxucHJpbnQobWFza1swXS5udW1weSgpKVxucHJpbnQoXHUwMDI3XFxuU2VxIDEgKGNvbHMgMyw0IGFyZSAtaW5mIGV2ZXJ5d2hlcmUg4oCUIHBhZGRpbmcgbWFzayArIGNhdXNhbCk6XHUwMDI3KVxucHJpbnQobWFza1sxXS5udW1weSgpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1hc2sgVmFyaWFudHMgYXQgYSBHbGFuY2UifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWFzayBUeXBlIiwiQXJjaGl0ZWN0dXJlIiwiUG9zaXRpb25zIFZpc2libGUgdG8gaSIsIlVzZSBDYXNlIiwiS1YgQ2FjaGUgYXQgSW5mZXJlbmNlIl0sInJvd3MiOltbIk5vIG1hc2siLCJFbmNvZGVyIiwiQWxsIHBvc2l0aW9ucyIsIkJFUlQsIHJlcHJlc2VudGF0aW9uIG1vZGVscyIsIk5vdCBhcHBsaWNhYmxlIl0sWyJDYXVzYWwgb25seSIsIkRlY29kZXIiLCJDdXJyZW50ICsgcGFzdCAoaiDiiaQgaSkiLCJHUFQsIGF1dG9yZWdyZXNzaXZlIExMTSIsIlllcyDigJQgY2FjaGUgSyBhbmQgViJdLFsiQmlkaXJlY3Rpb25hbCIsIkVuY29kZXIiLCJBbGwgcG9zaXRpb25zIChzYW1lIGFzIG5vIG1hc2spIiwiRW1iZWRkaW5nLCBjbGFzc2lmaWNhdGlvbiIsIk5vdCBhcHBsaWNhYmxlIl0sWyJDYXVzYWwgKyBwYWRkaW5nIiwiRGVjb2RlciAoYmF0Y2hlZCkiLCJQYXN0IG9ubHk7IFBBRCBrZXlzIGJsb2NrZWQiLCJCYXRjaGVkIHRleHQgZ2VuZXJhdGlvbiIsIlllcywgUEFELWF3YXJlIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNhdXNhbCBtYXNraW5nIGlzIHRoZSBtZWNoYW5pc20gdGhhdCBtYWtlcyBhdXRvcmVncmVzc2l2ZSBnZW5lcmF0aW9uIGNvcnJlY3QuIENvbWJpbmVkIHdpdGggYSBLViBjYWNoZSBpdCBlbmFibGVzIGVmZmljaWVudCBPKEwpIHBlci1zdGVwIGluZmVyZW5jZSByYXRoZXIgdGhhbiBuYWl2ZWx5IHJlY29tcHV0aW5nIGFsbCBwcmV2aW91cyBrZXlzIGFuZCB2YWx1ZXMgZWFjaCBzdGVwLiBGb3IgcHJvZHVjdGlvbiBkZXBsb3ltZW50cyBoYW5kbGluZyB2ZXJ5IGxvbmcgY29udGV4dHMsIEtWIGNhY2hlIG1lbW9yeSBtYW5hZ2VtZW50IOKAlCBxdWFudGl6YXRpb24sIGV2aWN0aW9uIHBvbGljaWVzLCBzbGlkaW5nLXdpbmRvdyBhdHRlbnRpb24g4oCUIGJlY29tZXMgdGhlIHByaW1hcnkgZW5naW5lZXJpbmcgY29uY2Vybi4ifV0="
---
# Causal Masking — Autoregressive Attention for Decoder

Transformer decoders generate text one token at a time. During training, teacher forcing presents the entire target sequence at once — but a critical invariant must be preserved: position i must not see any information from positions i+1, i+2, … (future tokens). Without this constraint the model would simply copy future tokens from the input instead of learning to predict them. The mechanism that enforces this invariant is the *causal mask*, also called the look-ahead mask.

## Why Decoders Need Causal Masking

In standard scaled dot-product attention, every query position attends to every key position. For encoder self-attention this is desirable — a word can use context from both directions. But for the decoder, this is cheating: position 2 seeing position 5 means the model has been given the answer it is supposed to predict. Causal masking breaks these forward-looking attention paths, restricting each query to attend only to itself and earlier positions.

1. Compute raw attention scores: S = QKᵀ / √d_k, shape (L, L)
2. Create causal mask M: upper-triangular matrix of -∞ for positions where j > i
3. Add mask: S_masked = S + M — future positions become -∞
4. Apply softmax: weights = softmax(S_masked, dim=-1) — -∞ becomes exactly 0
5. Output: O = weights · V — future tokens contribute zero weight

> **Why -∞ and Not Zero?**: Setting logits to -∞ before softmax yields exactly zero in the output weights because exp(-∞) = 0. Setting logits to 0 would not mask the position — it would receive a softmax weight of 1/L instead. The -∞ trick exploits softmax normalisation to create perfect masking with no extra computation overhead.

## The Look-Ahead Mask as an Upper Triangular Matrix

The causal mask M is an L×L matrix where M[i, j] = -∞ if j > i, else 0. In PyTorch this is created with torch.triu(torch.ones(L, L), diagonal=1) * -float('inf'). The diagonal=1 argument starts the upper triangle one step above the main diagonal, so position i can still attend to itself (j = i) but not to any position j > i. The resulting attention weight matrix is lower-triangular after softmax.

## KV Cache — Reducing O(L²) to O(L) per Step

At inference, the decoder generates tokens sequentially. Without a KV cache, computing attention at step t requires reprocessing all t-1 previous tokens to produce their keys and values — O(t) work per step, O(L²) total across a sequence of length L. With a KV cache, the keys and values for positions 0 through t-1 are stored after their first computation. Step t only computes Q, K, V for the single new token, appends K and V to the cache, and attends against the entire cached K and V. This reduces per-step cost from O(L) recompute to O(1) new computation plus O(L) attention, at the expense of memory proportional to L × 2 × n_heads × d_head.

## Code 1 — Causal Mask from Scratch

Building the upper-triangular -∞ mask and applying it inside scaled dot-product attention. Position 0 attends only to itself; position 5 attends to all 6 positions.

```python
import torch
import torch.nn.functional as F
import math

def make_causal_mask(seq_len: int, device: str = 'cpu') -> torch.Tensor:
    """Upper-triangular matrix of -inf; positions (i,j) with j>i get -inf."""
    ones = torch.ones(seq_len, seq_len, device=device)
    mask = torch.triu(ones, diagonal=1)       # 1 where j > i, 0 otherwise
    return mask * float('-inf')               # shape (L, L)

def causal_attention(Q: torch.Tensor, K: torch.Tensor,
                     V: torch.Tensor) -> tuple:
    """Scaled dot-product attention with causal mask. Q/K/V: (B, H, L, d)."""
    d_k  = Q.size(-1)
    L    = Q.size(-2)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
    mask   = make_causal_mask(L, device=Q.device)
    scores = scores + mask                    # broadcast over batch and heads
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V), weights

# Demo: batch=2, heads=4, seq_len=6, d_k=16
torch.manual_seed(42)
B, H, L, d = 2, 4, 6, 16
Q = torch.randn(B, H, L, d)
K = torch.randn(B, H, L, d)
V = torch.randn(B, H, L, d)
out, weights = causal_attention(Q, K, V)
print('Output shape:', out.shape)             # (2, 4, 6, 16)
print('Pos 0 weights (only self):', weights[0, 0, 0].detach().numpy().round(3))
print('Pos 5 weights (all six): ', weights[0, 0, 5].detach().numpy().round(3))
```

## Code 2 — Verifying Causal Attention Correctness

A quantitative check confirming that the future-attention weight sum is effectively zero for every query position, proving the causal invariant holds numerically.

```python
import torch
import torch.nn.functional as F
import math
import numpy as np

def make_causal_mask(L, device='cpu'):
    return torch.triu(torch.ones(L, L, device=device), diagonal=1) * float('-inf')

def causal_sdpa(Q, K, V):
    d_k = Q.size(-1)
    L   = Q.size(-2)
    scores  = Q @ K.transpose(-2, -1) / math.sqrt(d_k)
    scores += make_causal_mask(L, Q.device)
    w = F.softmax(scores, dim=-1)
    return w @ V, w

# Use L=5 for readable output
torch.manual_seed(7)
L = 5
Q = K = V = torch.randn(1, 1, L, 8)   # shared Q, K, V for simplicity
_, attn = causal_sdpa(Q, K, V)
w = attn[0, 0].detach()

print('Attention weight matrix (rows=queries, cols=keys):')
print(np.array2string(w.numpy(), precision=3, suppress_small=True))
print()
all_ok = True
for i in range(L):
    future = w[i, i+1:].sum().item()
    past   = w[i, :i+1].sum().item()
    ok = future < 1e-6
    all_ok = all_ok and ok
    print(f'  pos {i}: past_sum={past:.4f}  future_sum={future:.2e}  ok={ok}')
print(f'Causal invariant holds: {all_ok}')
```

## Code 3 — KV Cache for Autoregressive Inference

A minimal attention module that caches keys and values across generation steps, processing one new token per forward pass instead of recomputing all past tokens.

```python
import torch
import torch.nn as nn
import math

class CachedSelfAttention(nn.Module):
    """Single-head attention with KV cache for step-by-step inference."""
    def __init__(self, d_model: int):
        super().__init__()
        self.d  = d_model
        self.Wq = nn.Linear(d_model, d_model, bias=False)
        self.Wk = nn.Linear(d_model, d_model, bias=False)
        self.Wv = nn.Linear(d_model, d_model, bias=False)
        self.Wo = nn.Linear(d_model, d_model, bias=False)
        self.cache_k = self.cache_v = None

    def reset_cache(self):
        self.cache_k = self.cache_v = None

    def forward(self, x: torch.Tensor) -> torch.Tensor:  # x: (B, 1, d)
        q, k, v = self.Wq(x), self.Wk(x), self.Wv(x)
        self.cache_k = k if self.cache_k is None else torch.cat([self.cache_k, k], 1)
        self.cache_v = v if self.cache_v is None else torch.cat([self.cache_v, v], 1)
        # Attend: new query vs all cached keys (no causal mask needed: single new Q)
        scores  = q @ self.cache_k.transpose(-2, -1) / math.sqrt(self.d)
        weights = torch.softmax(scores, dim=-1)
        return self.Wo(weights @ self.cache_v)

# Simulate 8-step autoregressive decoding
model = CachedSelfAttention(d_model=64)
for step in range(8):
    tok = torch.randn(1, 1, 64)         # single new token embedding
    out = model(tok)
    L_cache = model.cache_k.shape[1]
    print(f'Step {step+1}: out={tuple(out.shape)}, KV cache length={L_cache}')
print('Full recompute cost: O(L^2) total; KV cache cost: O(L) per step')
```

## Code 4 — Combined Causal and Padding Mask

Batched decoding needs both a causal mask (no future tokens) and a padding mask (no PAD-key attention). Both use additive -∞ masking, so they can be summed directly before softmax.

```python
import torch
import torch.nn.functional as F
import math

def make_causal_mask(L: int, device='cpu') -> torch.Tensor:
    return torch.triu(torch.ones(L, L, device=device), diagonal=1) * float('-inf')

def make_padding_mask(seq_lens, max_len: int, device='cpu') -> torch.Tensor:
    """Returns (B, 1, max_len) additive mask: -inf at PAD positions."""
    ids   = torch.arange(max_len, device=device).unsqueeze(0)   # (1, L)
    lens  = torch.tensor(seq_lens, device=device).unsqueeze(1)  # (B, 1)
    is_pad = (ids >= lens).float() * float('-inf')               # (B, L)
    return is_pad.unsqueeze(1)                                   # (B, 1, L)

def combined_mask(seq_lens, max_len: int, device='cpu') -> torch.Tensor:
    """Returns (B, max_len, max_len) combined additive mask."""
    causal = make_causal_mask(max_len, device)                   # (L, L)
    pad    = make_padding_mask(seq_lens, max_len, device)        # (B, 1, L)
    return causal.unsqueeze(0) + pad                             # (B, L, L)

# Batch: seq 0 length=5 (full), seq 1 length=3 (padded to 5)
seq_lens = [5, 3]
mask = combined_mask(seq_lens, max_len=5)
print('Mask shape:', mask.shape)              # (2, 5, 5)
print('\nSeq 0 (no padding, only causal -inf above diagonal):')
print(mask[0].numpy())
print('\nSeq 1 (cols 3,4 are -inf everywhere — padding mask + causal):')
print(mask[1].numpy())
```

## Mask Variants at a Glance

| Mask Type | Architecture | Positions Visible to i | Use Case | KV Cache at Inference |
| --- | --- | --- | --- | --- |
| No mask | Encoder | All positions | BERT, representation models | Not applicable |
| Causal only | Decoder | Current + past (j ≤ i) | GPT, autoregressive LLM | Yes — cache K and V |
| Bidirectional | Encoder | All positions (same as no mask) | Embedding, classification | Not applicable |
| Causal + padding | Decoder (batched) | Past only; PAD keys blocked | Batched text generation | Yes, PAD-aware |

Causal masking is the mechanism that makes autoregressive generation correct. Combined with a KV cache it enables efficient O(L) per-step inference rather than naively recomputing all previous keys and values each step. For production deployments handling very long contexts, KV cache memory management — quantization, eviction policies, sliding-window attention — becomes the primary engineering concern.

