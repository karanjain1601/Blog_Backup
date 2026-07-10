---
title: "RoPE Linear Position Interpolation"
slug: "rope-linear-scaling"
description: "Extending LLM context length by linearly scaling RoPE position indices to fit within the original training range, enabling inference at 2–8x the pretrained context length with minimal fine-tuning."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUm90YXJ5IFBvc2l0aW9uIEVtYmVkZGluZyAoUm9QRSkgZW5jb2RlcyB0b2tlbiBwb3NpdGlvbnMgYnkgcm90YXRpbmcgcXVlcnkgYW5kIGtleSB2ZWN0b3JzIGluIHRoZSBhdHRlbnRpb24gbWVjaGFuaXNtLiBFYWNoIHRva2VuIGF0IHBvc2l0aW9uIG0gcmVjZWl2ZXMgYSB1bmlxdWUgcm90YXRpb24gbWF0cml4IHdob3NlIGFuZ2xlIGRlcGVuZHMgb24gYm90aCBtIGFuZCB0aGUgZW1iZWRkaW5nIGRpbWVuc2lvbi4gV2hlbiBhIG1vZGVsIHRyYWluZWQgb24gNDA5Ni10b2tlbiBzZXF1ZW5jZXMgbXVzdCBwcm9jZXNzIDE2Mzg0IHRva2VucywgcG9zaXRpb25zIDQwOTfigJMxNjM4NCBwcm9kdWNlIHJvdGF0aW9uIGFuZ2xlcyBmYXIgb3V0c2lkZSB3aGF0IHdhcyBzZWVuIGR1cmluZyB0cmFpbmluZyDigJQgdGhlIG1vZGVsIGhhcyBlZmZlY3RpdmVseSBuZXZlciBlbmNvdW50ZXJlZCB0aG9zZSBSb1BFIHZhbHVlcy4gTGluZWFyIHBvc2l0aW9uIGludGVycG9sYXRpb24gYWRkcmVzc2VzIHRoaXMgcHJvYmxlbSBieSBjb21wcmVzc2luZyBleHRlbmRlZCBwb3NpdGlvbiBpbmRpY2VzIGJhY2sgaW50byB0aGUgcHJldHJhaW5lZCByYW5nZSwgZW5hYmxpbmcgaW5mZXJlbmNlIGF0IDLigJM4eCB0aGUgb3JpZ2luYWwgY29udGV4dCBsZW5ndGggd2l0aG91dCBhbnkgYXJjaGl0ZWN0dXJhbCBjaGFuZ2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxpbmVhciBSb1BFIGludGVycG9sYXRpb24gKENoZW4gZXQgYWwuLCAyMDIzLCDigJhFeHRlbmRpbmcgQ29udGV4dCBXaW5kb3cgb2YgTGFyZ2UgTGFuZ3VhZ2UgTW9kZWxzIHZpYSBQb3NpdGlvbmFsIEludGVycG9sYXRpb27igJkpIHJlcGxhY2VzIGVhY2ggcG9zaXRpb24gaW5kZXggbSB3aXRoIG0vcyBpbiB0aGUgUm9QRSBjb21wdXRhdGlvbiwgd2hlcmUgcyA9IHRhcmdldF9sZW5ndGggLyB0cmFpbl9sZW5ndGguIEZvciBhIDQwOTYtdG9rZW4gbW9kZWwgdGFyZ2V0aW5nIDE2Mzg0LXRva2VuIGluZmVyZW5jZSwgcyA9IDQuIFBvc2l0aW9uIDE2MzgzIGJlY29tZXMgZWZmZWN0aXZlIHBvc2l0aW9uIDQwOTUuNzUg4oCUIHNhZmVseSBpbnNpZGUgdGhlIHRyYWluaW5nIGRpc3RyaWJ1dGlvbi4gTm8gYXJjaGl0ZWN0dXJhbCBjaGFuZ2UgaXMgcmVxdWlyZWQ6IG9ubHkgdGhlIGxpbmUgY29tcHV0aW5nIHBvc2l0aW9uIGluZGljZXMgbmVlZHMgYSBvbmUtY2hhcmFjdGVyIHBhdGNoLiBUaGUgbWV0aG9kIHdvcmtzIHplcm8tc2hvdCBmb3IgbW9kZXN0IHNjYWxlIGZhY3RvcnMgKHMg4omkIDIpIGFuZCB3aXRoIGJyaWVmIGZpbmUtdHVuaW5nIGZvciBsYXJnZXIgZmFjdG9ycyAocyDiiaQgOCkuIEl0IGlzIG5hdGl2ZWx5IHN1cHBvcnRlZCBpbiBIdWdnaW5nRmFjZSBUcmFuc2Zvcm1lcnMgdmlhIHJvcGVfc2NhbGluZz17XHUwMDI3dHlwZVx1MDAyNzogXHUwMDI3bGluZWFyXHUwMDI3LCBcdTAwMjdmYWN0b3JcdTAwMjc6IHN9IGFuZCBpcyB0aGUgYmFzZWxpbmUgYWdhaW5zdCB3aGljaCBhbGwgc3Vic2VxdWVudCBSb1BFIGV4dGVuc2lvbiBtZXRob2RzIGFyZSBjb21wYXJlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSb1BFIFJlZnJlc2hlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUm9QRSBkZWZpbmVzIHBvc2l0aW9uLWRlcGVuZGVudCByb3RhdGlvbiBtYXRyaWNlcy4gRm9yIGEgcXVlcnkgdmVjdG9yIHEgYXQgcG9zaXRpb24gbSwgdGhlIHJvdGF0ZWQgdmVyc2lvbiBpcyBxX20gPSBSX20gcSwgd2hlcmUgUl9tIGlzIGEgYmxvY2stZGlhZ29uYWwgbWF0cml4IHdob3NlIGktdGggMsOXMiBibG9jayBhcHBsaWVzIGEgcm90YXRpb24gYnkgYW5nbGUgdGhldGFfaSAqIG0uIFRoZSBpbnZlcnNlIGZyZXF1ZW5jaWVzIGFyZSB0aGV0YV9pID0gMSAvICgxMDAwMF4oMmkvZCkpLCBkZWNyZWFzaW5nIGdlb21ldHJpY2FsbHkgd2l0aCBkaW1lbnNpb24gaW5kZXggaS4gVGhlIGZpcnN0IGRpbWVuc2lvbiBwYWlyIChpPTApIHJvdGF0ZXMgYXQgdGhldGFfMCA9IDEvMTAwMDBeMCA9IDEgcmFkIHBlciBwb3NpdGlvbiDigJQgY2FwdHVyaW5nIGZpbmUtZ3JhaW5lZCBsb2NhbCBzeW50YXguIFRoZSBsYXN0IHBhaXIgKGk9ZC8yLTEpIHJvdGF0ZXMgYXQgdGhldGFfe2QvMi0xfSA9IDEvMTAwMDBeeyhkLTIpL2R9IOKJiCAxLzk3NzIgcmFkIHBlciBwb3NpdGlvbiwgY2FwdHVyaW5nIGNvYXJzZSBsb25nLXJhbmdlIHN0cnVjdHVyZS4gVGhlIGtleSBwcm9wZXJ0eSBpcyB0aGF0IHRoZSBkb3QgcHJvZHVjdCBxX21eVCBrX24gZGVwZW5kcyBvbmx5IG9uIHRoZSByZWxhdGl2ZSBvZmZzZXQgbS1uLCBnaXZpbmcgUm9QRSB0aGUgcmVsYXRpdmUtcG9zaXRpb24gYmVuZWZpdCBvZiBBTGlCaSB3aGlsZSByZW1haW5pbmcgY29tcGF0aWJsZSB3aXRoIEtWIGNhY2hpbmcuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJxX20gPSBSX21cXCwgcSwgXFxxdWFkIFJfbSA9IFxcbWF0aHJte2RpYWd9XFwhXFxsZWZ0KFIoXFx0aGV0YV8xIG0pLFxcLCBSKFxcdGhldGFfMiBtKSxcXCwgXFxsZG90cyxcXCwgUihcXHRoZXRhX3tkLzJ9XFwsIG0pXFxyaWdodCksIFxccXVhZCBcXHRoZXRhX2kgPSBcXGZyYWN7MX17MTAwMDBee1xcLDJpL2R9fSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGlubmVyIHByb2R1Y3QgYmV0d2VlbiByb3RhdGVkIHF1ZXJpZXMgYW5kIGtleXMgZmFjdG9yaXNlcyBhcyBxX21eVCBrX24gPSBxXlQgUl97bS1ufSBrLCBzbyBhdHRlbnRpb24gaXMgcHVyZWx5IGEgZnVuY3Rpb24gb2YgcmVsYXRpdmUgZGlzcGxhY2VtZW50IG0tbi4gVGhpcyBlbGVnYW50IHByb3BlcnR5IGlzIHdoeSBSb1BFIGJlY2FtZSB0aGUgZG9taW5hbnQgcG9zaXRpb24gZW5jb2RpbmcgaW4gTGxhbWEsIE1pc3RyYWwsIEZhbGNvbiwgR2VtbWEsIFF3ZW4sIGFuZCBtb3N0IG1vZGVybiBvcGVuLXdlaWdodCBMTE1zLiBUaGUgcm90YXRpb24gaXMgYXBwbGllZCBpbi1wbGFjZSB0byBxdWVyeSBhbmQga2V5IHZlY3RvcnMgYmVmb3JlIGNvbXB1dGluZyBhdHRlbnRpb24gc2NvcmVzOyB2YWx1ZSB2ZWN0b3JzIGFyZSBub3Qgcm90YXRlZC4gQmVjYXVzZSByb3RhdGlvbnMgYXJlIG9ydGhvZ29uYWwsIHRoZXkgcHJlc2VydmUgdmVjdG9yIG5vcm1zIGFuZCBkbyBub3QgZGlzdG9ydCB0aGUgbWFnbml0dWRlIG9mIGF0dGVudGlvbiBsb2dpdHMg4oCUIG9ubHkgdGhlaXIgZGlyZWN0aW9uYWwgc3RydWN0dXJlIGVuY29kZXMgcG9zaXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG1hdGhcblxuZGVmIHJvdGF0ZV9oYWxmKHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiTmVnYXRlIGFuZCBzd2FwIHRoZSB0d28gaGFsdmVzIG9mIHRoZSBsYXN0IGRpbWVuc2lvbiBmb3IgUm9QRSByb3RhdGlvbi5cIlwiXCJcbiAgICBoYWxmID0geC5zaGFwZVstMV0gLy8gMlxuICAgIHJldHVybiB0b3JjaC5jYXQoWy14Wy4uLiwgaGFsZjpdLCB4Wy4uLiwgOmhhbGZdXSwgZGltPS0xKVxuXG5kZWYgc3RhbmRhcmRfcm9wZShkaW06IGludCwgc2VxX2xlbjogaW50LCBiYXNlOiBpbnQgPSAxMDAwMCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiQnVpbGQgUm9QRSBlbWJlZGRpbmdzIGZvciBwb3NpdGlvbnMgMC4uc2VxX2xlbi0xLlwiXCJcIlxuICAgIGludl9mcmVxID0gMS4wIC8gKGJhc2UgKiogKHRvcmNoLmFyYW5nZSgwLCBkaW0sIDIpLmZsb2F0KCkgLyBkaW0pKVxuICAgIHQgPSB0b3JjaC5hcmFuZ2Uoc2VxX2xlbiwgZHR5cGU9dG9yY2guZmxvYXQzMilcbiAgICBmcmVxcyA9IHRvcmNoLm91dGVyKHQsIGludl9mcmVxKSAgICAgICAgICAjIChzZXFfbGVuLCBkaW0vMilcbiAgICByZXR1cm4gdG9yY2guY2F0KFtmcmVxcywgZnJlcXNdLCBkaW09LTEpICAjIChzZXFfbGVuLCBkaW0pXG5cbmRlZiBsaW5lYXJfc2NhbGVkX3JvcGUoZGltOiBpbnQsIHNlcV9sZW46IGludCwgc2NhbGU6IGZsb2F0LFxuICAgICAgICAgICAgICAgICAgICAgICBiYXNlOiBpbnQgPSAxMDAwMCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiTGluZWFyIHBvc2l0aW9uIGludGVycG9sYXRpb246IG1hcCBwb3NpdGlvbiBtIC1cdTAwM2UgbS9zLlxuICAgIEV4dGVuZGVkIHBvc2l0aW9ucyBhcmUgY29tcHJlc3NlZCBpbnRvIHRoZSBwcmV0cmFpbmVkIHJhbmdlIFswLCB0cmFpbl9sZW5dLlwiXCJcIlxuICAgIGludl9mcmVxID0gMS4wIC8gKGJhc2UgKiogKHRvcmNoLmFyYW5nZSgwLCBkaW0sIDIpLmZsb2F0KCkgLyBkaW0pKVxuICAgIHQgPSB0b3JjaC5hcmFuZ2Uoc2VxX2xlbiwgZHR5cGU9dG9yY2guZmxvYXQzMikgLyBzY2FsZSAgIyBcdTAwM2MtLSBpbnRlcnBvbGF0aW9uXG4gICAgZnJlcXMgPSB0b3JjaC5vdXRlcih0LCBpbnZfZnJlcSlcbiAgICByZXR1cm4gdG9yY2guY2F0KFtmcmVxcywgZnJlcXNdLCBkaW09LTEpXG5cbiMgVmVyaWZ5OiAxNksgY29udGV4dCB3aXRoIHM9NCBzdGF5cyB3aXRoaW4gdGhlIDRLIHRyYWluaW5nIGRpc3RyaWJ1dGlvblxudHJhaW5fbGVuLCBleHRfbGVuLCBzID0gNDA5NiwgMTYzODQsIDQuMFxuZW1iX29yaWcgICA9IHN0YW5kYXJkX3JvcGUoNjQsIHRyYWluX2xlbilcbmVtYl9zY2FsZWQgPSBsaW5lYXJfc2NhbGVkX3JvcGUoNjQsIGV4dF9sZW4sIHNjYWxlPXMpXG5wcmludChmXCJTdGFuZGFyZCBtYXggcm90YXRpb24gYW5nbGUgIDoge2VtYl9vcmlnLm1heCgpLml0ZW0oKTouNGZ9IHJhZFwiKVxucHJpbnQoZlwiU2NhbGVkLTR4IG1heCByb3RhdGlvbiBhbmdsZSA6IHtlbWJfc2NhbGVkLm1heCgpLml0ZW0oKTouNGZ9IHJhZFwiKVxuYWxpZ25lZCA9IHRvcmNoLmFsbGNsb3NlKGVtYl9zY2FsZWRbOnRyYWluX2xlbl0sIGVtYl9vcmlnLCBhdG9sPTFlLTUpXG5wcmludChmXCJGaXJzdCA0MDk2IHBvc2l0aW9ucyBtYXRjaCB0cmFpbmluZyBkaXN0cmlidXRpb246IHthbGlnbmVkfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik91dC1vZi1EaXN0cmlidXRpb24gUG9zaXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGEgbW9kZWwgdHJhaW5lZCBvbiA0MDk2IHRva2VucyByZWNlaXZlcyBhIDE2Mzg0LXRva2VuIHNlcXVlbmNlIHdpdGhvdXQgYW55IFJvUEUgbW9kaWZpY2F0aW9uLCBwb3NpdGlvbnMgNDA5N+KAkzE2Mzg0IHByb2R1Y2Ugcm90YXRpb24gYW5nbGVzIDR4IGxhcmdlciB0aGFuIGFueXRoaW5nIHNlZW4gZHVyaW5nIHRyYWluaW5nLiBUaGUgYXR0ZW50aW9uIGRvdCBwcm9kdWN0cyBkZXBlbmQgb24gc2luIGFuZCBjb3Mgb2YgdGhlc2UgYW5nbGVzLCBzbyB0aGUgYXR0ZW50aW9uIHBhdHRlcm4gaXMgY29tcGxldGVseSBkaXNydXB0ZWQuIEVtcGlyaWNhbGx5LCBwZXJwbGV4aXR5IHJpc2VzIGZyb20gcm91Z2hseSA2IGF0IDRLIHRvIG92ZXIgMTAwIGF0IDE2SyDigJQgdGhlIG1vZGVsIGVzc2VudGlhbGx5IGZhaWxzIHRvIHByb2Nlc3MgbG9uZyBkb2N1bWVudHMgY29oZXJlbnRseS4gVGhlIGVmZmVjdCBpcyBhc3ltbWV0cmljIGFjcm9zcyBSb1BFIGRpbWVuc2lvbnM6IGhpZ2gtZnJlcXVlbmN5IGRpbWVuc2lvbnMgKHBhaXJzIDDigJMxMCkgY29tcGxldGUgbWFueSBmdWxsIHJvdGF0aW9ucyBhbmQgbWF5IGFjY2lkZW50YWxseSBsYW5kIG5lYXIgYSB0cmFpbmVkIHZhbHVlIGJ5IHBlcmlvZGljaXR5LCBidXQgbG93LWZyZXF1ZW5jeSBkaW1lbnNpb25zIChwYWlycyBkLzItMTAgdG8gZC8yLTEpIHByb2R1Y2UgYW5nbGVzIHRoYXQgaGF2ZSBuZXZlciBiZWVuIHNlZW4gYW5kIGNhcnJ5IG5vIHNpZ25hbC4gVGhlIG1vZGVs4oCZcyBsb25nLXJhbmdlIGF0dGVudGlvbiBoZWFkcyBzaW1wbHkgc3RvcCBmdW5jdGlvbmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW5lYXIgSW50ZXJwb2xhdGlvbiBTY2FsaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZml4IGlzIHRvIHJlcGxhY2UgcG9zaXRpb24gaW5kZXggbSB3aXRoIG0vcyB0aHJvdWdob3V0IHRoZSBSb1BFIGNvbXB1dGF0aW9uLiBXaXRoIHM9NCBhbmQgYSAxNjM4NC10b2tlbiBzZXF1ZW5jZSwgcG9zaXRpb24gMTYzODMgYmVjb21lcyBlZmZlY3RpdmUgcG9zaXRpb24gNDA5NS43NS4gVGhlIG1vZGVsIG5ldmVyIHNlZXMgYSByb3RhdGlvbiBhbmdsZSBsYXJnZXIgdGhhbiB0aG9zZSBhdCBwb3NpdGlvbiA0MDk1LCBleGFjdGx5IGFzIGR1cmluZyB0cmFpbmluZy4gVGhlIGludGVycG9sYXRpb24gaXMgbWF0aGVtYXRpY2FsbHkgY2xlYW46IHRoZSBzZXQgb2YgZWZmZWN0aXZlIHBvc2l0aW9ucyBpcyB7MCwgMS9zLCAyL3MsIOKApiwgKE4tMSkvc30gd2hpY2ggZGVuc2VseSBjb3ZlcnMgWzAsIE4vc10gPSBbMCwgdHJhaW5fbGVuXS4gVW5saWtlIGV4dHJhcG9sYXRpb24gKHdoaWNoIGxlYXZlcyB0aGUgdHJhaW5lZCBkaXN0cmlidXRpb24pLCBpbnRlcnBvbGF0aW9uIHN0YXlzIHdpdGhpbiBpdC4gVGhlIGNvc3QgaXMgcmVzb2x1dGlvbjogd2l0aCBzPTQsIHR3byB0b2tlbnMgdGhhdCBhcmUgNCBwb3NpdGlvbnMgYXBhcnQgc2hhcmUgYW4gZWZmZWN0aXZlIHBvc2l0aW9uIGRpZmZlcmVuY2Ugb2Ygb25seSAxIOKAlCB0aGUgbW9kZWwgbXVzdCB1c2UgZmluZXItZ3JhaW5lZCBkaXN0aW5jdGlvbnMgdGhhbiBpdCB3YXMgdHJhaW5lZCBvbiBmb3IgbmVhcmJ5IHRva2Vucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgTGxhbWFDb25maWcsIExsYW1hRm9yQ2F1c2FsTE0sIEF1dG9Ub2tlbml6ZXJcblxuZGVmIGxvYWRfbGxhbWFfbGluZWFyX3NjYWxpbmcoXG4gICAgICAgIG1vZGVsX2lkOiBzdHIgPSBcIm1ldGEtbGxhbWEvTGxhbWEtMi03Yi1oZlwiLFxuICAgICAgICBzY2FsaW5nX2ZhY3RvcjogZmxvYXQgPSA0LjAsXG4gICAgICAgIHRhcmdldF9jdHg6IGludCA9IDE2Mzg0KSAtXHUwMDNlIHR1cGxlOlxuICAgIFwiXCJcIkFwcGx5IGxpbmVhciBSb1BFIGludGVycG9sYXRpb24gdG8gTGxhbWEtMi03QiBmb3IgMTZLLXRva2VuIGluZmVyZW5jZS5cIlwiXCJcbiAgICBjb25maWcgPSBMbGFtYUNvbmZpZy5mcm9tX3ByZXRyYWluZWQobW9kZWxfaWQpXG4gICAgIyBIdWdnaW5nRmFjZSBidWlsdC1pbiBsaW5lYXIgUm9QRSBzY2FsaW5nIHBhdGNoZXMgTGxhbWFSb3RhcnlFbWJlZGRpbmdcbiAgICBjb25maWcucm9wZV9zY2FsaW5nID0ge1widHlwZVwiOiBcImxpbmVhclwiLCBcImZhY3RvclwiOiBzY2FsaW5nX2ZhY3Rvcn1cbiAgICBjb25maWcubWF4X3Bvc2l0aW9uX2VtYmVkZGluZ3MgPSB0YXJnZXRfY3R4XG4gICAgbW9kZWwgPSBMbGFtYUZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcbiAgICAgICAgbW9kZWxfaWQsIGNvbmZpZz1jb25maWcsXG4gICAgICAgIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsIGRldmljZV9tYXA9XCJhdXRvXCJcbiAgICApXG4gICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQobW9kZWxfaWQpXG4gICAgbl9wYXJhbXMgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSkgLyAxZTlcbiAgICBwcmludChmXCJMb2FkZWQge25fcGFyYW1zOi4xZn1CIHBhcmFtcyB8IGNvbnRleHQgd2luZG93ID0ge3RhcmdldF9jdHh9IHRva2Vuc1wiKVxuICAgIHJldHVybiBtb2RlbCwgdG9rZW5pemVyXG5cbmRlZiBsb25nX2NvbnRleHRfZ2VuZXJhdGUobW9kZWwsIHRva2VuaXplciwgZG9jdW1lbnQ6IHN0cixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4X25ldzogaW50ID0gNjQpIC1cdTAwM2Ugc3RyOlxuICAgIFwiXCJcIlJ1biBjYXVzYWwgaW5mZXJlbmNlIG9uIGEgZG9jdW1lbnQgdXAgdG8gMTVLIHRva2Vucy5cIlwiXCJcbiAgICBpbnB1dHMgPSB0b2tlbml6ZXIoZG9jdW1lbnQsIHJldHVybl90ZW5zb3JzPVwicHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgdHJ1bmNhdGlvbj1UcnVlLCBtYXhfbGVuZ3RoPTE1MDAwKS50byhtb2RlbC5kZXZpY2UpXG4gICAgbl9pbiA9IGlucHV0c1tcImlucHV0X2lkc1wiXS5zaGFwZVstMV1cbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgb3V0ID0gbW9kZWwuZ2VuZXJhdGUoKippbnB1dHMsIG1heF9uZXdfdG9rZW5zPW1heF9uZXcsIGRvX3NhbXBsZT1GYWxzZSlcbiAgICBjb21wbGV0aW9uID0gdG9rZW5pemVyLmRlY29kZShvdXRbMCwgbl9pbjpdLCBza2lwX3NwZWNpYWxfdG9rZW5zPVRydWUpXG4gICAgcHJpbnQoZlwiSW5wdXQ6IHtuX2lufSB0b2tlbnMgfCBHZW5lcmF0ZWQ6IHtsZW4ob3V0WzBdKSAtIG5faW59IHRva2Vuc1wiKVxuICAgIHJldHVybiBjb21wbGV0aW9uXG5cbnByaW50KFwiVXNhZ2U6IG1vZGVsLCB0b2sgPSBsb2FkX2xsYW1hX2xpbmVhcl9zY2FsaW5nKCk7IGxvbmdfY29udGV4dF9nZW5lcmF0ZShtb2RlbCwgdG9rLCBkb2MpXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIFNjYWxpbmcgRmFjdG9yIHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzY2FsZSBmYWN0b3IgcyBpcyBzZXQgdG8gdGFyZ2V0X2xlbmd0aCAvIHRyYWluX2xlbmd0aC4gRm9yIGEgNEsgbW9kZWwgdGFyZ2V0aW5nIDE2Sywgcz00OyBmb3IgOEssIHM9Mi4gVGhlIHRyYWRlLW9mZiBiZXR3ZWVuIGV4dGVuc2lvbiByYXRpbyBhbmQgcXVhbGl0eSBpcyBzdGVlcDogYXQgcz0yLCBwZXJwbGV4aXR5IGRlZ3JhZGVzIGJ5IG9ubHkgMC4z4oCTMC41IFBQTCB6ZXJvLXNob3Q7IGF0IHM9NCwgZGVncmFkYXRpb24gaXMgMS414oCTMi41IFBQTCB3aXRob3V0IGZpbmUtdHVuaW5nOyBhdCBzPTgsIHRoZSBtb2RlbCByZXF1aXJlcyBtYW5kYXRvcnkgZmluZS10dW5pbmcgdG8gYmUgdXNlZnVsLiBUaGlzIGJlaGF2aW91ciBhcmlzZXMgYmVjYXVzZSBoaWdoZXIgcyB2YWx1ZXMgcGxhY2UgbW9yZSB0b2tlbnMgYXQgdGhlIHNhbWUgZWZmZWN0aXZlIHBvc2l0aW9uIGluZGV4LCBkZWdyYWRpbmcgdGhlIG1vZGVs4oCZcyBhYmlsaXR5IHRvIGRpc3Rpbmd1aXNoIHRva2VucyB0aGF0IGFyZSBjbG9zZSB0b2dldGhlciBpbiB0aGUgb3JpZ2luYWwgc2VxdWVuY2UuIFRoZSBvcmlnaW5hbCBwYXBlciAoQ2hlbiBldCBhbC4pIHJlY29tbWVuZHMgcyDiiaQgNCBmb3IgemVyby1zaG90IHVzZSBhbmQgdXAgdG8gcz04IHdpdGggZmluZS10dW5pbmcuIEluIHByYWN0aWNlLCBzPTIgKHRoZSBMb25nTG9SQSBjb25maWd1cmF0aW9uKSBhbmQgcz00ICh0aGUgTGxhbWEtMi1Mb25nIGNvbmZpZ3VyYXRpb24pIGFyZSB0aGUgbW9zdCBjb21tb24gZGVwbG95bWVudHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsRm9yQ2F1c2FsTE0sIEF1dG9Ub2tlbml6ZXJcblxuZGVmIGV2YWxfcHBsX2J5X2xlbmd0aChtb2RlbCwgdG9rZW5pemVyLCB0ZXh0OiBzdHIsXG4gICAgICAgICAgICAgICAgICAgICAgIGxlbmd0aHM6IGxpc3QsIGRldmljZTogc3RyID0gXCJjcHVcIikgLVx1MDAzZSBkaWN0OlxuICAgIFwiXCJcIkNvbXB1dGUgcGVyLXRva2VuIE5MTCBsb3NzIChwZXJwbGV4aXR5KSBhdCBpbmNyZWFzaW5nIHNlcXVlbmNlIGxlbmd0aHMuXCJcIlwiXG4gICAgdG9rZW5zID0gdG9rZW5pemVyKHRleHQsIHJldHVybl90ZW5zb3JzPVwicHRcIilbXCJpbnB1dF9pZHNcIl0udG8oZGV2aWNlKVxuICAgIG1vZGVsLmV2YWwoKVxuICAgIHJlc3VsdHMgPSB7fVxuICAgIGZvciBMIGluIGxlbmd0aHM6XG4gICAgICAgIGlmIHRva2Vucy5zaGFwZVsxXSBcdTAwM2MgTDpcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIGNodW5rID0gdG9rZW5zWzosIDpMXVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIGxvc3MgPSBtb2RlbChjaHVuaywgbGFiZWxzPWNodW5rKS5sb3NzLml0ZW0oKVxuICAgICAgICByZXN1bHRzW0xdID0gcm91bmQoMi43MTgyODE4MjggKiogbG9zcywgMilcbiAgICByZXR1cm4gcmVzdWx0c1xuXG4jIFJlcHJlc2VudGF0aXZlIFBQTCB2YWx1ZXMgc2hvd2luZyB0aGUgZWZmZWN0IG9mIGxpbmVhciBzY2FsaW5nXG5sZW5ndGhzICAgICAgPSBbNDA5NiwgNjE0NCwgODE5MiwgMTIyODgsIDE2Mzg0XVxucHBsX25vX3NjYWxlID0gWzYuMSwgIDkuOCwgIDE5LjQsICA1OC4xLCAgMTQ3LjNdICAgIyBkaXZlcmdlcyBPT0RcbnBwbF9zY2FsZWQgICA9IFs2LjEsICA2LjQsICAgNi45LCAgIDcuNSwgICAgOC4yXSAgICMgZ3JhY2VmdWwgd2l0aCBzPTRcblxucHJpbnQoZlwie1x1MDAyN0xlbmd0aFx1MDAyNzpcdTAwM2U4fSAge1x1MDAyN05vIFNjYWxpbmdcdTAwMjc6XHUwMDNlMTJ9ICB7XHUwMDI3TGluZWFyIHM9NFx1MDAyNzpcdTAwM2UxMn0gIHtcdTAwMjdSYXRpb1x1MDAyNzpcdTAwM2U4fVwiKVxuZm9yIEwsIG5zLCBzYyBpbiB6aXAobGVuZ3RocywgcHBsX25vX3NjYWxlLCBwcGxfc2NhbGVkKTpcbiAgICByYXRpbyA9IG5zIC8gc2NcbiAgICBmbGFnID0gXCIgISFcIiBpZiBucyBcdTAwM2UgMjAgZWxzZSBcIlwiXG4gICAgcHJpbnQoZlwie0w6XHUwMDNlOH0gIHtuczpcdTAwM2UxMi4xZn0gIHtzYzpcdTAwM2UxMi4xZn0gIHtyYXRpbzpcdTAwM2U3LjFmfXh7ZmxhZ31cIikifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiTWF4IHJlbGlhYmxlIGV4dGVuc2lvbiIsIkZpbmUtdHVuaW5nIG5lZWRlZCIsIlBQTCBhdCAyeCIsIlBQTCBhdCA0eCIsIk5vdGVzIl0sInJvd3MiOltbIk5vIHNjYWxpbmciLCIxeCAodHJhaW5pbmcgbGVuZ3RoKSIsIk4vQSIsIjE4KyAoT09EKSIsIjEwMCsgKE9PRCkiLCJDYXRhc3Ryb3BoaWMgYmV5b25kIHRyYWluIHdpbmRvdyJdLFsiTGluZWFyIGludGVycG9sYXRpb24iLCI04oCTOHgiLCJPcHRpb25hbCAocmVjb21tZW5kZWQgZm9yIHNcdTAwM2UyKSIsIjYuNCIsIjguMiIsIlVuaWZvcm0gcG9zaXRpb24gY29tcHJlc3Npb247IHNpbXBsZSAxLWxpbmUgcGF0Y2giXSxbIk5USy1hd2FyZSBzY2FsaW5nIiwiNOKAkzh4IiwiTm90IHJlcXVpcmVkIGZvciBz4omkNCIsIjYuMyIsIjcuNCIsIlByZXNlcnZlcyBoaWdoLWZyZXEgZGltczsgYmV0dGVyIHplcm8tc2hvdCB0aGFuIGxpbmVhciJdLFsiWWFSTiIsIjjigJMzMngiLCI0MDDigJMxMDAwIHN0ZXBzIGZvciBzXHUwMDNlNCIsIjYuMiIsIjYuOSIsIlBpZWNld2lzZSBwZXItZGltIHNjYWxpbmcgKyB0ZW1wZXJhdHVyZTsgc3RhdGUtb2YtdGhlLWFydCJdLFsiRnVsbCBmaW5lLXR1bmluZyIsIkFyYml0cmFyeSIsIlJlcXVpcmVkIChmdWxsIHRyYWluaW5nIGJ1ZGdldCkiLCI2LjEiLCI2LjEiLCJCZXN0IHF1YWxpdHkgYnV0IGV4cGVuc2l2ZTsgYmFzZWxpbmUgdXBwZXIgYm91bmQiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiUG9zaXRpb24gQ29tcHJlc3Npb24gVHJhZGUtb2ZmIiwiY29udGVudCI6IkxpbmVhciBpbnRlcnBvbGF0aW9uIGNvbXByZXNzZXMgYWxsIHBvc2l0aW9ucyB1bmlmb3JtbHkg4oCUIHRoZSBtb2RlbCBzZWVzIGVmZmVjdGl2ZSBwb3NpdGlvbiAwLjI1IHdoZXJlIGl0IHdhcyB0cmFpbmVkIG9uIHBvc2l0aW9uIDEuIEF0IHNjYWxlIGZhY3RvcnMgYWJvdmUgNHgsIGF0dGVudGlvbiBwYXR0ZXJucyBibHVyIGJlY2F1c2UgbmVhcmJ5IHRva2VucyBzaGFyZSBhbG1vc3QgaWRlbnRpY2FsIGVmZmVjdGl2ZSBwb3NpdGlvbnMuIFdpdGhvdXQgZmluZS10dW5pbmcsIHRoaXMgY2F1c2VzIHRoZSBtb2RlbCB0byBsb3NlIGZpbmUtZ3JhaW5lZCBsb2NhbCBzeW50YWN0aWMgZGlzdGluY3Rpb25zLiBBbHdheXMgcGFpciBzXHUwMDNlMiB3aXRoIGF0IGxlYXN0IDIwMCBmaW5lLXR1bmluZyBzdGVwcyBvbiBsb25nIGRvY3VtZW50cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGaW5lLXR1bmluZyBSZXF1aXJlbWVudHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxpbmVhciBzY2FsaW5nIHdvcmtzIHJlYXNvbmFibHkgemVyby1zaG90IGZvciBz4omkMiwgYnV0IGZvciBzPTTigJM4IGEgYnJpZWYgZmluZS10dW5pbmcgcGhhc2Ugb24gbG9uZyBkb2N1bWVudHMgZHJhbWF0aWNhbGx5IHJlY292ZXJzIHBlcmZvcm1hbmNlLiBDaGVuIGV0IGFsLiBzaG93IHRoYXQgMTAwMCBncmFkaWVudCBzdGVwcyBvbiBzZXF1ZW5jZXMgb2YgdGhlIHRhcmdldCBsZW5ndGggYnJpbmdzIHBlcnBsZXhpdHkgd2l0aGluIDAuNSBQUEwgb2YgYSBtb2RlbCBmdWxseSBwcmV0cmFpbmVkIGF0IHRoYXQgbGVuZ3RoLiBUaGUgZmluZS10dW5pbmcgc2V0dXAgaXM6IGEgZGF0YXNldCBvZiBsb25nIGRvY3VtZW50cyAoMTBL4oCTMTAwSyBleGFtcGxlcyksIGEgbGVhcm5pbmcgcmF0ZSAxMMOXIHNtYWxsZXIgdGhhbiBwcmV0cmFpbmluZyAoMWUtNSBmb3IgTGxhbWEtMiksIGFuZCBhIGNvc2luZSBvciBjb25zdGFudCBMUiBzY2hlZHVsZS4gVGhlIG1vZGVsIGFkYXB0cyBpdHMgYXR0ZW50aW9uIHBhdHRlcm5zIHRvIHRoZSBjb21wcmVzc2VkIHBvc2l0aW9uIHNwYWNlLCBsZWFybmluZyB3aGljaCBpbnRlcnBvbGF0ZWQgcG9zaXRpb25zIGNvcnJlc3BvbmQgdG8gbWVhbmluZ2Z1bCB0b2tlbiBkaXN0YW5jZXMuIEV2ZW4gMjAwIHN0ZXBzIHByb3ZpZGVzIGEgc2lnbmlmaWNhbnQgcmVjb3Zlcnkg4oCUIGEgcHJhY3RpY2FsIHRyYWRlLW9mZiB3aGVuIEdQVSB0aW1lIGlzIGNvbnN0cmFpbmVkLiBUaGUgTGxhbWEtMi1Mb25nIG1vZGVsIChNZXRhLCAyMDIzKSB3YXMgcHJvZHVjZWQgYnkgdGhpcyByZWNpcGUgYXQgcz00IGZvciAxNksgY29udGV4dC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgVHJhaW5lciwgVHJhaW5pbmdBcmd1bWVudHMsIERhdGFDb2xsYXRvckZvckxhbmd1YWdlTW9kZWxpbmdcblxuZGVmIHByaW50X3JlY292ZXJ5X3RhYmxlKCkgLVx1MDAzZSBOb25lOlxuICAgIFwiXCJcIlNob3cgcGVycGxleGl0eSBhdCAxNksgdG9rZW5zIGFzIGEgZnVuY3Rpb24gb2YgZmluZS10dW5pbmcgc3RlcHMuXG4gICAgRGVtb25zdHJhdGVzIHRoYXQgfjEwMDAgc3RlcHMgcmVjb3ZlcnMgbW9zdCBvZiB0aGUgUFBMIGdhcC5cIlwiXCJcbiAgICAjIChzdGVwcywgUFBMQDE2SykgYWZ0ZXIgbGluZWFyIHM9NCBzY2FsaW5nICsgZmluZS10dW5pbmcgb24gbG9uZyBkb2N1bWVudHNcbiAgICBjaGVja3BvaW50cyA9IFtcbiAgICAgICAgKDAsICAgIDguMiksICAgIyB6ZXJvLXNob3QgbGluZWFyIHNjYWxpbmcsIG5vIGZpbmUtdHVuaW5nXG4gICAgICAgICgyMDAsICA3LjYpLCAgICMgZWFybHkgZmluZS10dW5pbmdcbiAgICAgICAgKDUwMCwgIDcuMSksICAgIyBtaWQgZmluZS10dW5pbmdcbiAgICAgICAgKDEwMDAsIDYuNyksICAgIyBuZWFyLWNvbnZlcmdlZDogd2l0aGluIDAuNiBQUEwgb2YgNEsgYmFzZWxpbmVcbiAgICAgICAgKDIwMDAsIDYuNCksICAgIyBjb252ZXJnZWQ6IGluZGlzdGluZ3Vpc2hhYmxlIGZyb20gZnVsbCByZXRyYWluaW5nXG4gICAgXVxuICAgIGJhc2VsaW5lID0gNi4xICAgIyBQUEwgYXQgNEsgd2l0aCBzdGFuZGFyZCBSb1BFIChyZWZlcmVuY2UgbG93ZXIgYm91bmQpXG4gICAgcHJpbnQoZlwie1x1MDAyN1N0ZXBzXHUwMDI3Olx1MDAzZTh9ICB7XHUwMDI3UFBMQDE2S1x1MDAyNzpcdTAwM2UxMH0gIHtcdTAwMjdHYXAgdnMgNEtcdTAwMjc6XHUwMDNlMTJ9ICB7XHUwMDI3UmVjb3ZlcnklXHUwMDI3Olx1MDAzZTEyfVwiKVxuICAgIHByaW50KFwiLVwiICogNTApXG4gICAgZm9yIHN0ZXBzLCBwcGwgaW4gY2hlY2twb2ludHM6XG4gICAgICAgIGdhcCA9IHBwbCAtIGJhc2VsaW5lXG4gICAgICAgIHJlY292ZXJ5ID0gMTAwLjAgKiAoOC4yIC0gcHBsKSAvICg4LjIgLSBiYXNlbGluZSlcbiAgICAgICAgcHJpbnQoZlwie3N0ZXBzOlx1MDAzZTh9ICB7cHBsOlx1MDAzZTEwLjJmfSAge2dhcDpcdTAwM2UrMTIuMmZ9ICB7cmVjb3Zlcnk6XHUwMDNlMTEuMWZ9JVwiKVxuXG5wcmludF9yZWNvdmVyeV90YWJsZSgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGltaXRhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxpbmVhciBpbnRlcnBvbGF0aW9uIGhhcyB0d28gZnVuZGFtZW50YWwgbGltaXRhdGlvbnMuIEZpcnN0LCBpdCBhcHBsaWVzIHVuaWZvcm0gY29tcHJlc3Npb24gdG8gYWxsIFJvUEUgZGltZW5zaW9ucyByZWdhcmRsZXNzIG9mIHRoZWlyIGZyZXF1ZW5jeS4gSGlnaC1mcmVxdWVuY3kgZGltZW5zaW9ucyAod2hpY2ggZW5jb2RlIGxvY2FsIHN5bnRhY3RpYyBzdHJ1Y3R1cmUpIGFuZCBsb3ctZnJlcXVlbmN5IGRpbWVuc2lvbnMgKHdoaWNoIGVuY29kZSBsb25nLXJhbmdlIGRvY3VtZW50IHN0cnVjdHVyZSkgYm90aCBnZXQgdGhlaXIgcG9zaXRpb25zIGRpdmlkZWQgYnkgdGhlIHNhbWUgZmFjdG9yIHMuIEhpZ2gtZnJlcXVlbmN5IGRpbWVuc2lvbnMgYXJlIHBhcnRpY3VsYXJseSBzZW5zaXRpdmUgdG8gdGhpcyBjb21wcmVzc2lvbiBiZWNhdXNlIHRoZXkgcmVseSBvbiBmaW5lLWdyYWluZWQgcG9zaXRpb24gZGlmZmVyZW5jZXMgdG8gZGlzdGluZ3Vpc2ggdG9rZW5zIHdpdGhpbiBhIHNob3J0IHdpbmRvdy4gRGl2aWRpbmcgYWxsIHBvc2l0aW9ucyBieSBzIGJsdXJzIHRoZXNlIGxvY2FsIGRpc3RpbmN0aW9ucyBldmVuIGF0IHBvc2l0aW9ucyB0aGF0IGFyZSB3ZWxsIHdpdGhpbiB0aGUgb3JpZ2luYWwgdHJhaW5pbmcgcmFuZ2UuIFNlY29uZCwgdGhlIG1ldGhvZCBkb2VzIG5vdCBhZGRyZXNzIHRoZSBhbGlhc2luZyBwcm9ibGVtOiB3aXRoIHM9NCwgdG9rZW5zIGF0IGVmZmVjdGl2ZSBwb3NpdGlvbnMgMS4wLCAxLjI1LCAxLjUsIGFuZCAxLjc1IGFyZSBhbGwgY3JhbW1lZCBiZXR3ZWVuIHRyYWluaW5nIHBvc2l0aW9ucyAxIGFuZCAyLCBtYWtpbmcgaXQgaGFyZGVyIGZvciB0aGUgbW9kZWwgdG8gZGlzdGluZ3Vpc2ggdGhlbS4gTlRLLWF3YXJlIHNjYWxpbmcgYW5kIFlhUk4gYXJlIHNwZWNpZmljYWxseSBkZXNpZ25lZCB0byBhZGRyZXNzIHRoZXNlIGxpbWl0YXRpb25zLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVW5pZm9ybSBwb3NpdGlvbiBjb21wcmVzc2lvbiBkZWdyYWRlcyBoaWdoLWZyZXF1ZW5jeSBSb1BFIGRpbWVuc2lvbnMgdGhhdCBjYXB0dXJlIGxvY2FsIHN5bnRheCIsIlBlcnBsZXhpdHkgZGVncmFkZXMgcXVpY2tseSBhdCBzXHUwMDNlNCB3aXRob3V0IGZpbmUtdHVuaW5nIGR1ZSB0byBwb3NpdGlvbiBhbGlhc2luZyIsIkRvZXMgbm90IHByZXNlcnZlIHRoZSB3YXZlbGVuZ3RoIHNwZWN0cnVtIG9mIGRpZmZlcmVudCBSb1BFIGRpbWVuc2lvbiBwYWlycyIsIlBlcmZvcm1hbmNlIGRyb3BzIG1vcmUgZm9yIHRhc2tzIHJlcXVpcmluZyBwcmVjaXNlIGxvY2FsIHRva2VuIG9yZGVyaW5nIChlLmcuLCBjb2RlIGdlbmVyYXRpb24pIiwiTm90IHN1aXRhYmxlIGFzIGEgemVyby1zaG90IGRyb3AtaW4gZm9yIHNcdTAwM2U0OyBhbHdheXMgdmFsaWRhdGUgUFBMIGJlZm9yZSBkZXBsb3ltZW50IiwiRmluZS10dW5pbmcgaXMgcmVxdWlyZWQgdG8gY2xvc2UgdGhlIGdhcCBhdCBsYXJnZSBzY2FsZSBmYWN0b3JzLCBhZGRpbmcgdHJhaW5pbmcgY29zdCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMaW5lYXIgcG9zaXRpb24gaW50ZXJwb2xhdGlvbiBpcyB0aGUgc2ltcGxlc3QsIG1vc3Qgd2lkZWx5IGRlcGxveWVkIFJvUEUgY29udGV4dCBleHRlbnNpb24gbWV0aG9kIGFuZCB0aGUgYmFzZWxpbmUgYWdhaW5zdCB3aGljaCBhbGwgb3RoZXJzIGFyZSBtZWFzdXJlZC4gSXQgcmVxdWlyZXMgYSBvbmUtbGluZSBjaGFuZ2UgdG8gdGhlIFJvUEUgcG9zaXRpb24gaW5kZXggY29tcHV0YXRpb24sIG5vIGFyY2hpdGVjdHVyYWwgbW9kaWZpY2F0aW9uLCBhbmQgbm8gY2hhbmdlIHRvIG1vZGVsIHdlaWdodHMgZm9yIHplcm8tc2hvdCB1c2UuIEZvciBz4omkMiwgaXQgd29ya3Mgd2VsbCBvdXQtb2YtdGhlLWJveCB3aXRoIG5lZ2xpZ2libGUgUFBMIGNvc3QuIEZvciBzPTQsIGEgYnJpZWYgZmluZS10dW5pbmcgcGhhc2Ugb2YgNTAw4oCTMTAwMCBzdGVwcyBvbiBsb25nIGRvY3VtZW50cyByZWNvdmVycyBxdWFsaXR5IGNsb3NlIHRvIGZ1bGwgcmV0cmFpbmluZy4gVGhlIG1ldGhvZCBpcyBuYXRpdmVseSBzdXBwb3J0ZWQgaW4gSHVnZ2luZ0ZhY2UgVHJhbnNmb3JtZXJzIGFuZCBpcyB1c2VkIGluIHByb2R1Y3Rpb24gYnkgTGxhbWEtMi1Mb25nLCBDb2RlIExsYW1hICgxMDBLIGNvbnRleHQpLCBhbmQgbWFueSBvdGhlciBtb2RlbHMuIEZvciBleHRlbnNpb25zIGJleW9uZCBzPTQgb3IgemVyby1zaG90IHF1YWxpdHkgcmVxdWlyZW1lbnRzLCBOVEstYXdhcmUgc2NhbGluZyAod2hpY2ggbW9kaWZpZXMgdGhlIFJvUEUgYmFzZSBmcmVxdWVuY3kpIGFuZCBZYVJOICh3aGljaCBhcHBsaWVzIHBpZWNld2lzZSBzY2FsaW5nIHBlciBmcmVxdWVuY3kgYmFuZCkgb2ZmZXIgYmV0dGVyIHJlc3VsdHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTZXQgcm9wZV9zY2FsaW5nPXtcdTAwMjd0eXBlXHUwMDI3OiBcdTAwMjdsaW5lYXJcdTAwMjcsIFx1MDAyN2ZhY3Rvclx1MDAyNzogc30gaW4gSHVnZ2luZ0ZhY2UgY29uZmlnIOKAlCB6ZXJvIGNvZGUgY2hhbmdlcyIsInM9MiBpcyBzYWZlIHplcm8tc2hvdDsgcz00IGJlbmVmaXRzIGZyb20gNTAwKyBmaW5lLXR1bmluZyBzdGVwczsgcz04IHJlcXVpcmVzIGZpbmUtdHVuaW5nIiwiSW50ZXJwb2xhdGlvbiBzdGF5cyB3aXRoaW4gdGhlIHByZXRyYWluZWQgUm9QRSBkaXN0cmlidXRpb247IGV4dHJhcG9sYXRpb24gZG9lcyBub3QiLCJUaGUgbWV0aG9kIGlzIGEgb25lLWxpbmUgcGF0Y2g6IGRpdmlkZSBwb3NpdGlvbiBpbmRpY2VzIGJ5IHMgYmVmb3JlIGNvbXB1dGluZyBzaW4vY29zIiwiUFBMIGRlZ3JhZGF0aW9uIGlzIHJvdWdobHkgZXhwb25lbnRpYWwgaW4gcyB3aXRob3V0IGZpbmUtdHVuaW5nIiwiQmFzZWxpbmUgY29tcGFyaXNvbiBwb2ludCBmb3IgTlRLLWF3YXJlIHNjYWxpbmcgYW5kIFlhUk4iXX1d"
---
# RoPE Linear Position Interpolation

Rotary Position Embedding (RoPE) encodes token positions by rotating query and key vectors in the attention mechanism. Each token at position m receives a unique rotation matrix whose angle depends on both m and the embedding dimension. When a model trained on 4096-token sequences must process 16384 tokens, positions 4097–16384 produce rotation angles far outside what was seen during training — the model has effectively never encountered those RoPE values. Linear position interpolation addresses this problem by compressing extended position indices back into the pretrained range, enabling inference at 2–8x the original context length without any architectural change.

## Overview

Linear RoPE interpolation (Chen et al., 2023, ‘Extending Context Window of Large Language Models via Positional Interpolation’) replaces each position index m with m/s in the RoPE computation, where s = target_length / train_length. For a 4096-token model targeting 16384-token inference, s = 4. Position 16383 becomes effective position 4095.75 — safely inside the training distribution. No architectural change is required: only the line computing position indices needs a one-character patch. The method works zero-shot for modest scale factors (s ≤ 2) and with brief fine-tuning for larger factors (s ≤ 8). It is natively supported in HuggingFace Transformers via rope_scaling={'type': 'linear', 'factor': s} and is the baseline against which all subsequent RoPE extension methods are compared.

## RoPE Refresher

RoPE defines position-dependent rotation matrices. For a query vector q at position m, the rotated version is q_m = R_m q, where R_m is a block-diagonal matrix whose i-th 2×2 block applies a rotation by angle theta_i * m. The inverse frequencies are theta_i = 1 / (10000^(2i/d)), decreasing geometrically with dimension index i. The first dimension pair (i=0) rotates at theta_0 = 1/10000^0 = 1 rad per position — capturing fine-grained local syntax. The last pair (i=d/2-1) rotates at theta_{d/2-1} = 1/10000^{(d-2)/d} ≈ 1/9772 rad per position, capturing coarse long-range structure. The key property is that the dot product q_m^T k_n depends only on the relative offset m-n, giving RoPE the relative-position benefit of ALiBi while remaining compatible with KV caching.

$$q_m = R_m\, q, \quad R_m = \mathrm{diag}\!\left(R(\theta_1 m),\, R(\theta_2 m),\, \ldots,\, R(\theta_{d/2}\, m)\right), \quad \theta_i = \frac{1}{10000^{\,2i/d}}$$

The inner product between rotated queries and keys factorises as q_m^T k_n = q^T R_{m-n} k, so attention is purely a function of relative displacement m-n. This elegant property is why RoPE became the dominant position encoding in Llama, Mistral, Falcon, Gemma, Qwen, and most modern open-weight LLMs. The rotation is applied in-place to query and key vectors before computing attention scores; value vectors are not rotated. Because rotations are orthogonal, they preserve vector norms and do not distort the magnitude of attention logits — only their directional structure encodes position.

```python
import torch
import math

def rotate_half(x: torch.Tensor) -> torch.Tensor:
    """Negate and swap the two halves of the last dimension for RoPE rotation."""
    half = x.shape[-1] // 2
    return torch.cat([-x[..., half:], x[..., :half]], dim=-1)

def standard_rope(dim: int, seq_len: int, base: int = 10000) -> torch.Tensor:
    """Build RoPE embeddings for positions 0..seq_len-1."""
    inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float() / dim))
    t = torch.arange(seq_len, dtype=torch.float32)
    freqs = torch.outer(t, inv_freq)          # (seq_len, dim/2)
    return torch.cat([freqs, freqs], dim=-1)  # (seq_len, dim)

def linear_scaled_rope(dim: int, seq_len: int, scale: float,
                       base: int = 10000) -> torch.Tensor:
    """Linear position interpolation: map position m -> m/s.
    Extended positions are compressed into the pretrained range [0, train_len]."""
    inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float() / dim))
    t = torch.arange(seq_len, dtype=torch.float32) / scale  # <-- interpolation
    freqs = torch.outer(t, inv_freq)
    return torch.cat([freqs, freqs], dim=-1)

# Verify: 16K context with s=4 stays within the 4K training distribution
train_len, ext_len, s = 4096, 16384, 4.0
emb_orig   = standard_rope(64, train_len)
emb_scaled = linear_scaled_rope(64, ext_len, scale=s)
print(f"Standard max rotation angle  : {emb_orig.max().item():.4f} rad")
print(f"Scaled-4x max rotation angle : {emb_scaled.max().item():.4f} rad")
aligned = torch.allclose(emb_scaled[:train_len], emb_orig, atol=1e-5)
print(f"First 4096 positions match training distribution: {aligned}")
```

## Out-of-Distribution Positions

When a model trained on 4096 tokens receives a 16384-token sequence without any RoPE modification, positions 4097–16384 produce rotation angles 4x larger than anything seen during training. The attention dot products depend on sin and cos of these angles, so the attention pattern is completely disrupted. Empirically, perplexity rises from roughly 6 at 4K to over 100 at 16K — the model essentially fails to process long documents coherently. The effect is asymmetric across RoPE dimensions: high-frequency dimensions (pairs 0–10) complete many full rotations and may accidentally land near a trained value by periodicity, but low-frequency dimensions (pairs d/2-10 to d/2-1) produce angles that have never been seen and carry no signal. The model’s long-range attention heads simply stop functioning.

## Linear Interpolation Scaling

The fix is to replace position index m with m/s throughout the RoPE computation. With s=4 and a 16384-token sequence, position 16383 becomes effective position 4095.75. The model never sees a rotation angle larger than those at position 4095, exactly as during training. The interpolation is mathematically clean: the set of effective positions is {0, 1/s, 2/s, …, (N-1)/s} which densely covers [0, N/s] = [0, train_len]. Unlike extrapolation (which leaves the trained distribution), interpolation stays within it. The cost is resolution: with s=4, two tokens that are 4 positions apart share an effective position difference of only 1 — the model must use finer-grained distinctions than it was trained on for nearby tokens.

```python
import torch
from transformers import LlamaConfig, LlamaForCausalLM, AutoTokenizer

def load_llama_linear_scaling(
        model_id: str = "meta-llama/Llama-2-7b-hf",
        scaling_factor: float = 4.0,
        target_ctx: int = 16384) -> tuple:
    """Apply linear RoPE interpolation to Llama-2-7B for 16K-token inference."""
    config = LlamaConfig.from_pretrained(model_id)
    # HuggingFace built-in linear RoPE scaling patches LlamaRotaryEmbedding
    config.rope_scaling = {"type": "linear", "factor": scaling_factor}
    config.max_position_embeddings = target_ctx
    model = LlamaForCausalLM.from_pretrained(
        model_id, config=config,
        torch_dtype=torch.float16, device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    n_params = sum(p.numel() for p in model.parameters()) / 1e9
    print(f"Loaded {n_params:.1f}B params | context window = {target_ctx} tokens")
    return model, tokenizer

def long_context_generate(model, tokenizer, document: str,
                          max_new: int = 64) -> str:
    """Run causal inference on a document up to 15K tokens."""
    inputs = tokenizer(document, return_tensors="pt",
                       truncation=True, max_length=15000).to(model.device)
    n_in = inputs["input_ids"].shape[-1]
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new, do_sample=False)
    completion = tokenizer.decode(out[0, n_in:], skip_special_tokens=True)
    print(f"Input: {n_in} tokens | Generated: {len(out[0]) - n_in} tokens")
    return completion

print("Usage: model, tok = load_llama_linear_scaling(); long_context_generate(model, tok, doc)")
```

## The Scaling Factor s

The scale factor s is set to target_length / train_length. For a 4K model targeting 16K, s=4; for 8K, s=2. The trade-off between extension ratio and quality is steep: at s=2, perplexity degrades by only 0.3–0.5 PPL zero-shot; at s=4, degradation is 1.5–2.5 PPL without fine-tuning; at s=8, the model requires mandatory fine-tuning to be useful. This behaviour arises because higher s values place more tokens at the same effective position index, degrading the model’s ability to distinguish tokens that are close together in the original sequence. The original paper (Chen et al.) recommends s ≤ 4 for zero-shot use and up to s=8 with fine-tuning. In practice, s=2 (the LongLoRA configuration) and s=4 (the Llama-2-Long configuration) are the most common deployments.

```python
import torch
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

def eval_ppl_by_length(model, tokenizer, text: str,
                       lengths: list, device: str = "cpu") -> dict:
    """Compute per-token NLL loss (perplexity) at increasing sequence lengths."""
    tokens = tokenizer(text, return_tensors="pt")["input_ids"].to(device)
    model.eval()
    results = {}
    for L in lengths:
        if tokens.shape[1] < L:
            break
        chunk = tokens[:, :L]
        with torch.no_grad():
            loss = model(chunk, labels=chunk).loss.item()
        results[L] = round(2.718281828 ** loss, 2)
    return results

# Representative PPL values showing the effect of linear scaling
lengths      = [4096, 6144, 8192, 12288, 16384]
ppl_no_scale = [6.1,  9.8,  19.4,  58.1,  147.3]   # diverges OOD
ppl_scaled   = [6.1,  6.4,   6.9,   7.5,    8.2]   # graceful with s=4

print(f"{'Length':>8}  {'No Scaling':>12}  {'Linear s=4':>12}  {'Ratio':>8}")
for L, ns, sc in zip(lengths, ppl_no_scale, ppl_scaled):
    ratio = ns / sc
    flag = " !!" if ns > 20 else ""
    print(f"{L:>8}  {ns:>12.1f}  {sc:>12.1f}  {ratio:>7.1f}x{flag}")
```

| Method | Max reliable extension | Fine-tuning needed | PPL at 2x | PPL at 4x | Notes |
| --- | --- | --- | --- | --- | --- |
| No scaling | 1x (training length) | N/A | 18+ (OOD) | 100+ (OOD) | Catastrophic beyond train window |
| Linear interpolation | 4–8x | Optional (recommended for s>2) | 6.4 | 8.2 | Uniform position compression; simple 1-line patch |
| NTK-aware scaling | 4–8x | Not required for s≤4 | 6.3 | 7.4 | Preserves high-freq dims; better zero-shot than linear |
| YaRN | 8–32x | 400–1000 steps for s>4 | 6.2 | 6.9 | Piecewise per-dim scaling + temperature; state-of-the-art |
| Full fine-tuning | Arbitrary | Required (full training budget) | 6.1 | 6.1 | Best quality but expensive; baseline upper bound |

> **Position Compression Trade-off**: Linear interpolation compresses all positions uniformly — the model sees effective position 0.25 where it was trained on position 1. At scale factors above 4x, attention patterns blur because nearby tokens share almost identical effective positions. Without fine-tuning, this causes the model to lose fine-grained local syntactic distinctions. Always pair s>2 with at least 200 fine-tuning steps on long documents.

## Fine-tuning Requirements

Linear scaling works reasonably zero-shot for s≤2, but for s=4–8 a brief fine-tuning phase on long documents dramatically recovers performance. Chen et al. show that 1000 gradient steps on sequences of the target length brings perplexity within 0.5 PPL of a model fully pretrained at that length. The fine-tuning setup is: a dataset of long documents (10K–100K examples), a learning rate 10× smaller than pretraining (1e-5 for Llama-2), and a cosine or constant LR schedule. The model adapts its attention patterns to the compressed position space, learning which interpolated positions correspond to meaningful token distances. Even 200 steps provides a significant recovery — a practical trade-off when GPU time is constrained. The Llama-2-Long model (Meta, 2023) was produced by this recipe at s=4 for 16K context.

```python
import torch
from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling

def print_recovery_table() -> None:
    """Show perplexity at 16K tokens as a function of fine-tuning steps.
    Demonstrates that ~1000 steps recovers most of the PPL gap."""
    # (steps, PPL@16K) after linear s=4 scaling + fine-tuning on long documents
    checkpoints = [
        (0,    8.2),   # zero-shot linear scaling, no fine-tuning
        (200,  7.6),   # early fine-tuning
        (500,  7.1),   # mid fine-tuning
        (1000, 6.7),   # near-converged: within 0.6 PPL of 4K baseline
        (2000, 6.4),   # converged: indistinguishable from full retraining
    ]
    baseline = 6.1   # PPL at 4K with standard RoPE (reference lower bound)
    print(f"{'Steps':>8}  {'PPL@16K':>10}  {'Gap vs 4K':>12}  {'Recovery%':>12}")
    print("-" * 50)
    for steps, ppl in checkpoints:
        gap = ppl - baseline
        recovery = 100.0 * (8.2 - ppl) / (8.2 - baseline)
        print(f"{steps:>8}  {ppl:>10.2f}  {gap:>+12.2f}  {recovery:>11.1f}%")

print_recovery_table()
```

## Limitations

Linear interpolation has two fundamental limitations. First, it applies uniform compression to all RoPE dimensions regardless of their frequency. High-frequency dimensions (which encode local syntactic structure) and low-frequency dimensions (which encode long-range document structure) both get their positions divided by the same factor s. High-frequency dimensions are particularly sensitive to this compression because they rely on fine-grained position differences to distinguish tokens within a short window. Dividing all positions by s blurs these local distinctions even at positions that are well within the original training range. Second, the method does not address the aliasing problem: with s=4, tokens at effective positions 1.0, 1.25, 1.5, and 1.75 are all crammed between training positions 1 and 2, making it harder for the model to distinguish them. NTK-aware scaling and YaRN are specifically designed to address these limitations.

- Uniform position compression degrades high-frequency RoPE dimensions that capture local syntax
- Perplexity degrades quickly at s>4 without fine-tuning due to position aliasing
- Does not preserve the wavelength spectrum of different RoPE dimension pairs
- Performance drops more for tasks requiring precise local token ordering (e.g., code generation)
- Not suitable as a zero-shot drop-in for s>4; always validate PPL before deployment
- Fine-tuning is required to close the gap at large scale factors, adding training cost

## Key Takeaways

Linear position interpolation is the simplest, most widely deployed RoPE context extension method and the baseline against which all others are measured. It requires a one-line change to the RoPE position index computation, no architectural modification, and no change to model weights for zero-shot use. For s≤2, it works well out-of-the-box with negligible PPL cost. For s=4, a brief fine-tuning phase of 500–1000 steps on long documents recovers quality close to full retraining. The method is natively supported in HuggingFace Transformers and is used in production by Llama-2-Long, Code Llama (100K context), and many other models. For extensions beyond s=4 or zero-shot quality requirements, NTK-aware scaling (which modifies the RoPE base frequency) and YaRN (which applies piecewise scaling per frequency band) offer better results.

- Set rope_scaling={'type': 'linear', 'factor': s} in HuggingFace config — zero code changes
- s=2 is safe zero-shot; s=4 benefits from 500+ fine-tuning steps; s=8 requires fine-tuning
- Interpolation stays within the pretrained RoPE distribution; extrapolation does not
- The method is a one-line patch: divide position indices by s before computing sin/cos
- PPL degradation is roughly exponential in s without fine-tuning
- Baseline comparison point for NTK-aware scaling and YaRN

