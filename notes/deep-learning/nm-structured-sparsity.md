---
title: "N:M Sparsity — Hardware-Accelerated Structured Sparsity"
slug: "nm-structured-sparsity"
description: "N:M sparsity (e.g., 2:4) requires exactly N nonzeros per M consecutive weights, enabling 2× throughput via NVIDIA Sparse Tensor Cores. Covers mask generation, training-time enforcement, compression format, and accuracy vs hardware trade-offs."
tags: ["deep-learning", "model-compression", "pruning", "quantization"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTjpNIHNwYXJzaXR5IGlzIGEgc3RydWN0dXJlZCBzcGFyc2l0eSBwYXR0ZXJuIHdoZXJlLCB3aXRoaW4gZXZlcnkgY29uc2VjdXRpdmUgZ3JvdXAgb2YgTSB3ZWlnaHRzLCBleGFjdGx5IE4gYXJlIG5vbnplcm8uIFRoZSAyOjQgcGF0dGVybiAoMiBub256ZXJvcyBwZXIgNCB3ZWlnaHRzLCA1MCUgc3BhcnNpdHkpIGlzIG5hdGl2ZWx5IHN1cHBvcnRlZCBieSBOVklESUEgQTEwMCBhbmQgbGF0ZXIgR1BVcyB2aWEgU3BhcnNlIFRlbnNvciBDb3JlcywgZGVsaXZlcmluZyB1cCB0byAyw5cgdGhyb3VnaHB1dCBmb3IgbGluZWFyIGxheWVycyB3aXRoIG1pbmltYWwgYWNjdXJhY3kgbG9zcy4gVW5saWtlIHVuc3RydWN0dXJlZCBzcGFyc2l0eSwgMjo0IHJlcXVpcmVzIG5vIHNwZWNpYWxpemVkIHNwYXJzZSBzb2x2ZXIg4oCUIHRoZSBoYXJkd2FyZSBoYW5kbGVzIGl0IHRyYW5zcGFyZW50bHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSG93IFNwYXJzZSBUZW5zb3IgQ29yZXMgV29yayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gdGhlIGNvbXByZXNzZWQgMjo0IHJlcHJlc2VudGF0aW9uLCBlYWNoIGdyb3VwIG9mIDQgY29uc2VjdXRpdmUgd2VpZ2h0cyBzdG9yZXMgb25seSAyIHZhbHVlcyBwbHVzIGEgMi1iaXQgaW5kZXggcGFpciBpbmRpY2F0aW5nIHRoZWlyIHBvc2l0aW9ucyAoMDAsIDAxLCAxMCwgb3IgMTEpLiBUaGUgd2VpZ2h0IG1hdHJpeCBpcyBjb21wcmVzc2VkIHRvIDUwJSBzdG9yYWdlLiBEdXJpbmcgbWF0cml4IG11bHRpcGxpY2F0aW9uLCB0aGUgaGFyZHdhcmUgdW5wYWNrcyB0aGUgaW5kaWNlcyBhbmQgbXVsdGlwbGllcyBvbmx5IHRoZSBub256ZXJvIHZhbHVlcyB3aXRoIHRoZSBjb3JyZXNwb25kaW5nIGFjdGl2YXRpb25zIOKAlCBlZmZlY3RpdmVseSBjb21wdXRpbmcgYSBzcGFyc2UgR0VNTSB3aXRoIG5vIHdhc3RlZCBtdWx0aXBsaWNhdGlvbnMuIFRoaXMgaXMgb25seSBhdmFpbGFibGUgZm9yIGxpbmVhciAoZGVuc2UgbWF0bXVsKSBsYXllcnM7IGJhdGNoIG5vcm0sIGVtYmVkZGluZ3MsIGFuZCBkZXB0aHdpc2UgY29udm9sdXRpb25zIHNlZSBubyBiZW5lZml0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IjI6NCBNYXNrIEdlbmVyYXRpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGdlbmVyYXRlXzJfNF9tYXNrKHdlaWdodDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJcbiAgICBHZW5lcmF0ZSBhIDI6NCBzcGFyc2l0eSBtYXNrOiBrZWVwIDIgbGFyZ2VzdC1tYWduaXR1ZGUgd2VpZ2h0cyBwZXIgZ3JvdXAgb2YgNC5cbiAgICB3ZWlnaHQ6IGFueSBzaGFwZTsgbGFzdCBkaW0gaXMgZ3JvdXBlZCBpbnRvIGJsb2NrcyBvZiA0LlxuICAgIFJldHVybnMgYSBib29sZWFuIG1hc2sgb2Ygc2FtZSBzaGFwZS5cbiAgICBcIlwiXCJcbiAgICBvcmlnaW5hbF9zaGFwZSA9IHdlaWdodC5zaGFwZVxuICAgICMgRmxhdHRlbiB0byAyRDogKHJvd3MsIGNvbHMpIHdoZXJlIGNvbHMgbXVzdCBiZSBkaXZpc2libGUgYnkgNFxuICAgIHcyZCA9IHdlaWdodC52aWV3KC0xLCB3ZWlnaHQuc2hhcGVbLTFdKSAgIyAoLi4uLCBDKSAtXHUwMDNlIChOLCBDKVxuICAgIE4sIEMgPSB3MmQuc2hhcGVcbiAgICBhc3NlcnQgQyAlIDQgPT0gMCwgZlx1MDAyN0xhc3QgZGltIHtDfSBtdXN0IGJlIGRpdmlzaWJsZSBieSA0IGZvciAyOjQgc3BhcnNpdHlcdTAwMjdcblxuICAgICMgR3JvdXAgaW50byBibG9ja3Mgb2YgNFxuICAgIHdfZ3JvdXBlZCA9IHcyZC52aWV3KE4sIEMgLy8gNCwgNCkgICMgKE4sIEMvLzQsIDQpXG4gICAgIyBGaW5kIHRvcC0yIG1hZ25pdHVkZXMgd2l0aGluIGVhY2ggZ3JvdXBcbiAgICBfLCB0b3BfaWR4ID0gd19ncm91cGVkLmFicygpLnRvcGsoMiwgZGltPS0xKSAgIyAoTiwgQy8vNCwgMilcbiAgICAjIEJ1aWxkIG1hc2tcbiAgICBtYXNrID0gdG9yY2guemVyb3NfbGlrZSh3X2dyb3VwZWQsIGR0eXBlPXRvcmNoLmJvb2wpXG4gICAgbWFzay5zY2F0dGVyXygtMSwgdG9wX2lkeCwgVHJ1ZSlcbiAgICByZXR1cm4gbWFzay52aWV3KG9yaWdpbmFsX3NoYXBlKVxuXG4jIERlbW9uc3RyYXRlXG50b3JjaC5tYW51YWxfc2VlZCg0MilcblcgPSB0b3JjaC5yYW5kbig0LCA4KSAgIyA0IG91dHB1dCBuZXVyb25zLCA4IGlucHV0c1xubWFzayA9IGdlbmVyYXRlXzJfNF9tYXNrKFcpXG5wcmludChcdTAwMjdXZWlnaHQgbWF0cml4Olx1MDAyNylcbnByaW50KFcucm91bmQoZGVjaW1hbHM9MikpXG5wcmludChcdTAwMjdcXG4yOjQgTWFzayAoMT1rZWVwLCAwPXBydW5lKTpcdTAwMjcpXG5wcmludChtYXNrLmludCgpKVxucHJpbnQoXHUwMDI3XFxuU3BhcnNlIHdlaWdodDpcdTAwMjcpXG5wcmludCgoVyAqIG1hc2spLnJvdW5kKGRlY2ltYWxzPTIpKVxucHJpbnQoZlx1MDAyN1xcblNwYXJzaXR5OiB7KH5tYXNrKS5mbG9hdCgpLm1lYW4oKS5pdGVtKCk6LjElfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyB3aXRoIDI6NCBDb25zdHJhaW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgMjo0IGNvbnN0cmFpbnQgY2FuIGJlIGFwcGxpZWQgcG9zdC10cmFpbmluZyAocHJ1bmUgKyBzaG9ydCBmaW5lLXR1bmUpIG9yIGVuZm9yY2VkIGR1cmluZyB0cmFpbmluZyBieSByZS1hcHBseWluZyB0aGUgbWFzayBldmVyeSBOIGdyYWRpZW50IHN0ZXBzLiBEdXJpbmcgdHJhaW5pbmcsIHRoZSBtYXNrIGlzIHJlY29tcHV0ZWQgcGVyaW9kaWNhbGx5IGZyb20gdGhlIGN1cnJlbnQgd2VpZ2h0IG1hZ25pdHVkZXMsIGFuZCB3ZWlnaHRzIG91dHNpZGUgdGhlIG1hc2sgYXJlIHplcm9lZC4gR3JhZGllbnRzIHN0aWxsIGZsb3cgdGhyb3VnaCBhbGwgcG9zaXRpb25zLCBidXQgdGhlIHplcm9lZCB3ZWlnaHRzIGFyZSByZS16ZXJvZWQgYmVmb3JlIGVhY2ggZm9yd2FyZCBwYXNzLiBUaGlzIGFsbG93cyB0aGUgbmV0d29yayB0byByZS1hbGxvY2F0ZSB0aGUgMiBrZXB0IHBvc2l0aW9ucyB3aXRoaW4gZWFjaCBncm91cCBhcyB0cmFpbmluZyBwcm9ncmVzc2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5cbmNsYXNzIFNwYXJzZUxpbmVhcjI0KG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTGluZWFyIGxheWVyIHRoYXQgZW5mb3JjZXMgMjo0IHNwYXJzaXR5IG9uIGl0cyB3ZWlnaHQgbWF0cml4LlwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2ZlYXR1cmVzOiBpbnQsIG91dF9mZWF0dXJlczogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGFzc2VydCBpbl9mZWF0dXJlcyAlIDQgPT0gMCwgXHUwMDI3aW5fZmVhdHVyZXMgbXVzdCBiZSBkaXZpc2libGUgYnkgNFx1MDAyN1xuICAgICAgICBzZWxmLmxpbmVhciA9IG5uLkxpbmVhcihpbl9mZWF0dXJlcywgb3V0X2ZlYXR1cmVzKVxuICAgICAgICBzZWxmLm1hc2sgPSBzZWxmLl9jb21wdXRlX21hc2soKVxuXG4gICAgZGVmIF9jb21wdXRlX21hc2soc2VsZikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIFcgPSBzZWxmLmxpbmVhci53ZWlnaHQuZGF0YSAgIyAob3V0LCBpbilcbiAgICAgICAgd19ncm91cGVkID0gVy52aWV3KFcuc2hhcGVbMF0sIFcuc2hhcGVbMV0gLy8gNCwgNClcbiAgICAgICAgXywgaWR4ID0gd19ncm91cGVkLmFicygpLnRvcGsoMiwgZGltPS0xKVxuICAgICAgICBtYXNrID0gdG9yY2guemVyb3NfbGlrZSh3X2dyb3VwZWQsIGR0eXBlPXRvcmNoLmJvb2wpXG4gICAgICAgIG1hc2suc2NhdHRlcl8oLTEsIGlkeCwgVHJ1ZSlcbiAgICAgICAgcmV0dXJuIG1hc2sudmlldyhXLnNoYXBlKVxuXG4gICAgZGVmIGFwcGx5X21hc2soc2VsZik6XG4gICAgICAgIFwiXCJcIlJlLXBydW5lIGFuZCByZS16ZXJvIHdlaWdodHMgb3V0c2lkZSB0aGUgY3VycmVudCBtYXNrLlwiXCJcIlxuICAgICAgICBzZWxmLm1hc2sgPSBzZWxmLl9jb21wdXRlX21hc2soKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIHNlbGYubGluZWFyLndlaWdodC5kYXRhICo9IHNlbGYubWFzay5mbG9hdCgpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICByZXR1cm4gc2VsZi5saW5lYXIoeClcblxuIyBTaW11bGF0ZSAyOjQgdHJhaW5pbmcgbG9vcFxubW9kZWwgPSBTcGFyc2VMaW5lYXIyNCg2NCwgMzIpXG5vcHRpbWl6ZXIgPSBvcHRpbS5TR0QobW9kZWwucGFyYW1ldGVycygpLCBscj0wLjAxKVxucmVtYXNrX2V2ZXJ5ID0gMTAgICMgcmUtYXBwbHkgMjo0IG1hc2sgZXZlcnkgMTAgc3RlcHNcblxuZm9yIHN0ZXAgaW4gcmFuZ2UoMzApOlxuICAgIHggPSB0b3JjaC5yYW5kbigxNiwgNjQpXG4gICAgbG9zcyA9IG1vZGVsKHgpLnBvdygyKS5tZWFuKClcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgaWYgKHN0ZXAgKyAxKSAlIHJlbWFza19ldmVyeSA9PSAwOlxuICAgICAgICBtb2RlbC5hcHBseV9tYXNrKClcbiAgICAgICAgZGVuc2l0eSA9IG1vZGVsLm1hc2suZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG4gICAgICAgIHByaW50KGZcdTAwMjdTdGVwIHtzdGVwKzF9OiBsb3NzPXtsb3NzLml0ZW0oKTouNGZ9ICBkZW5zaXR5PXtkZW5zaXR5Oi4yZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcHJlc3NlZCBTdG9yYWdlIEZvcm1hdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gdGhlIDI6NCBjb21wcmVzc2VkIGZvcm1hdCwgYSB3ZWlnaHQgbWF0cml4IG9mIHNoYXBlIChNLCBLKSBpcyBzdG9yZWQgYXM6ICgxKSBhIHZhbHVlIHRlbnNvciBvZiBzaGFwZSAoTSwgSy8yKSBjb250YWluaW5nIHRoZSAyIG5vbnplcm8gdmFsdWVzIHBlciBncm91cCBhbmQgKDIpIGEgbWV0YWRhdGEgdGVuc29yIG9mIHNoYXBlIChNLCBLLzgpIGNvbnRhaW5pbmcgMi1iaXQgaW5kaWNlcyAoNCBiaXRzIHBlciBncm91cCBvZiA0KS4gVG90YWwgc3RvcmFnZTogSy8yIHZhbHVlcyDDlyBlbGVtZW50X3NpemUgKyBLLzggbWV0YWRhdGEgYnl0ZXMuIEZvciBGUDE2IHdlaWdodHMsIHRoaXMgaXMgKEsvMiDDlyAyKSArIChLLzgpID0gNUsvOCBieXRlcyB2cyBLIMOXIDIgPSAySyBieXRlcyB1bmNvbXByZXNzZWQg4oCUIGEgMy4yw5cgcmVkdWN0aW9uIGluIHN0b3JhZ2UgcGVyIHJvdy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGNvbXByZXNzXzJfNCh3ZWlnaHQ6IHRvcmNoLlRlbnNvcik6XG4gICAgXCJcIlwiXG4gICAgU2ltdWxhdGUgMjo0IGNvbXByZXNzaW9uOiByZXR1cm5zICh2YWx1ZXMsIG1ldGFkYXRhKSB0ZW5zb3JzLlxuICAgIHZhbHVlczogbm9uemVybyBlbGVtZW50cywgc2hhcGUgKHJvd3MsIGNvbHMvLzIpXG4gICAgbWV0YWRhdGE6IDQtYml0IGluZGljZXMgcGFja2VkIGFzIHVpbnQ4LCBzaGFwZSAocm93cywgY29scy8vOClcbiAgICBcIlwiXCJcbiAgICBXID0gd2VpZ2h0LnZpZXcoLTEsIHdlaWdodC5zaGFwZVstMV0pICAjIChOLCBDKVxuICAgIE4sIEMgPSBXLnNoYXBlXG4gICAgYXNzZXJ0IEMgJSA0ID09IDBcbiAgICB3X2dyb3VwZWQgPSBXLnZpZXcoTiwgQyAvLyA0LCA0KSAgIyAoTiwgRywgNCkgd2hlcmUgRyA9IEMvLzRcbiAgICBzY29yZXMsIGluZGljZXMgPSB3X2dyb3VwZWQuYWJzKCkudG9waygyLCBkaW09LTEpICAjIChOLCBHLCAyKVxuICAgICMgR2F0aGVyIG5vbnplcm8gdmFsdWVzXG4gICAgdmFsdWVzID0gd19ncm91cGVkLmdhdGhlcigtMSwgaW5kaWNlcykgICMgKE4sIEcsIDIpXG4gICAgdmFsdWVzX2ZsYXQgPSB2YWx1ZXMucmVzaGFwZShOLCBDIC8vIDIpICAjIChOLCBDLy8yKVxuICAgICMgUGFjayBpbmRpY2VzIGFzIDQgYml0cyBwZXIgZ3JvdXAgKDIgcG9zaXRpb25zIGluIHswLDEsMiwzfSlcbiAgICAjIEVhY2ggaW5kZXggZml0cyBpbiAyIGJpdHM7IDQgYml0cyBwZXIgZ3JvdXAgb2YgNFxuICAgIGlkeF9zb3J0ZWQgPSBpbmRpY2VzLnNvcnQoZGltPS0xKS52YWx1ZXMgICMgZW5zdXJlIGFzY2VuZGluZyBvcmRlclxuICAgIG1ldGEgPSAoaWR4X3NvcnRlZFsuLi4sIDBdICogNCArIGlkeF9zb3J0ZWRbLi4uLCAxXSkudG8odG9yY2gudWludDgpICAjIChOLCBHKVxuICAgIHJldHVybiB2YWx1ZXNfZmxhdCwgbWV0YVxuXG5XID0gdG9yY2gucmFuZG4oOCwgMTYpXG52YWxzLCBtZXRhID0gY29tcHJlc3NfMl80KFcpXG5cbnVuY29tcHJlc3NlZF9ieXRlcyA9IFcubnVtZWwoKSAqIDQgICMgZmxvYXQzMlxuY29tcHJlc3NlZF9ieXRlcyA9IHZhbHMubnVtZWwoKSAqIDQgKyBtZXRhLm51bWVsKCkgICMgZmxvYXQzMiB2YWxzICsgdWludDggbWV0YVxucHJpbnQoZlx1MDAyN09yaWdpbmFsOiB7Vy5zaGFwZX0gIC1cdTAwM2UgIHt1bmNvbXByZXNzZWRfYnl0ZXN9IGJ5dGVzXHUwMDI3KVxucHJpbnQoZlx1MDAyN1ZhbHVlczogICB7dmFscy5zaGFwZX0sICBNZXRhZGF0YToge21ldGEuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0NvbXByZXNzZWQ6IHtjb21wcmVzc2VkX2J5dGVzfSBieXRlcyAgKHJhdGlvIHt1bmNvbXByZXNzZWRfYnl0ZXMvY29tcHJlc3NlZF9ieXRlczouMmZ9eClcdTAwMjcpXG5wcmludChmXHUwMDI3RGVuc2l0eSBjaGVjazoge3ZhbHMubnVtZWwoKX0ve1cubnVtZWwoKX0gPSB7dmFscy5udW1lbCgpL1cubnVtZWwoKTouMCV9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiMjo0IE9ubHkgSGVscHMgb24gQTEwMCsgZm9yIExpbmVhciBMYXllcnMiLCJjb250ZW50IjoiU3BhcnNlIFRlbnNvciBDb3JlIGFjY2VsZXJhdGlvbiBpcyBvbmx5IGF2YWlsYWJsZSBvbiBOVklESUEgQW1wZXJlIChBMTAwKSBhbmQgbGF0ZXIgR1BVcy4gT24gZWFybGllciBHUFVzIChWMTAwLCBUNCkgb3Igb24gQ1BVLCAyOjQgc3BhcnNpdHkgcHJvdmlkZXMgbm8gc3BlZWR1cCDigJQgdGhlIHNwYXJzZSB6ZXJvcyBzdGlsbCBwYXJ0aWNpcGF0ZSBpbiBjb21wdXRhdGlvbi4gQWRkaXRpb25hbGx5LCBvbmx5IGxpbmVhciAobWF0bXVsKSBsYXllcnMgYmVuZWZpdDsgZGVwdGh3aXNlIGNvbnZvbHV0aW9ucywgYmF0Y2ggbm9ybSwgYW5kIGVtYmVkZGluZ3MgcmVtYWluIGRlbnNlLiBGb3IgQ1BVIGRlcGxveW1lbnQsIHVuc3RydWN0dXJlZCBzcGFyc2l0eSB3aXRoIFNwTU0gb3IgZnVsbCBzdHJ1Y3R1cmVkIHBydW5pbmcgYXJlIGJldHRlciBjaG9pY2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFjY3VyYWN5IHZzIERlbnNlIEJhc2VsaW5lIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOVklESUFcdTAwMjdzIGV4cGVyaW1lbnRzIG9uIFJlc05ldC01MCBhbmQgQkVSVCBzaG93IHRoYXQgMjo0IHNwYXJzaXR5IHdpdGggMTDigJMyMCBlcG9jaHMgb2YgZmluZS10dW5pbmcgcmVjb3ZlcnMgdG8gd2l0aGluIDAuMeKAkzAuNSUgb2YgdGhlIGRlbnNlIGJhc2VsaW5lLiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCB3aXRoaW4gZWFjaCBncm91cCBvZiA0LCB0aGUgMiBzdXJ2aXZpbmcgd2VpZ2h0cyBjYW4gYmUgYW55IHBhaXIg4oCUIHRoaXMgZ2l2ZXMgdGhlIG5ldHdvcmsgZW5vdWdoIGZsZXhpYmlsaXR5IHRvIHJlcHJlc2VudCB0aGUgc2FtZSBmdW5jdGlvbnMgYXMgdGhlIGRlbnNlIG1vZGVsLiBMYXJnZXIgbW9kZWxzIChHUFQtMyBzY2FsZSkgc2hvdyBldmVuIHNtYWxsZXIgYWNjdXJhY3kgZ2FwcywgYXMgdGhlIHJlZHVuZGFuY3kgaW4gbGFyZ2UgbW9kZWxzIG1ha2VzIGl0IGVhc2llciB0byBwcnVuZSBoYWxmIHRoZSB3ZWlnaHRzIHdpdGhvdXQgbG9zaW5nIGZ1bmN0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gb2YgU3BhcnNpdHkgRm9ybWF0cyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJGb3JtYXQiLCJTcGFyc2l0eSIsIkExMDAgU3BlZWR1cCIsIkFjY3VyYWN5IHZzIERlbnNlIiwiSGFyZHdhcmUgU3VwcG9ydCIsIkltcGxlbWVudGF0aW9uIERpZmZpY3VsdHkiXSwicm93cyI6W1siRGVuc2UgKGJhc2VsaW5lKSIsIjAlIiwiMcOXIiwiQmFzZWxpbmUiLCJBbGwgaGFyZHdhcmUiLCJUcml2aWFsIl0sWyIyOjQgKE49MiwgTT00KSIsIjUwJSIsIn4yw5ciLCItMC4xIHRvIC0wLjUlIiwiQTEwMCsgb25seSAoQW1wZXJlKSIsIkxvdyDigJQgdG9yY2gubm4udXRpbHMucHJ1bmUgb3IgYXBleCJdLFsiMTo0IChOPTEsIE09NCkiLCI3NSUiLCJ+MsOXIChzYW1lIEhXIHBhdGgpIiwiLTIgdG8gLTUlIiwiQTEwMCsgb25seSIsIkxvdyDigJQgc2FtZSB0b29saW5nIl0sWyJVbnN0cnVjdHVyZWQgNTAlIiwiNTAlIiwifjHDlyAobm8gSFcgc3VwcG9ydCkiLCItMC41IHRvIC0yJSIsIk5vbmUgKHN0YW5kYXJkIEdQVSkiLCJMb3cg4oCUIHRocmVzaG9sZCBtYXNrIl0sWyJTdHJ1Y3R1cmVkIGZpbHRlciA1MCUiLCI1MCUgb2YgZmlsdGVycyIsIn4xLjXigJMyw5cgKGFueSBHUFUpIiwiLTEgdG8gLTMlIiwiQWxsIGhhcmR3YXJlIiwiSGlnaCDigJQgcmVzaGFwZSBkZXBlbmRlbnQgbGF5ZXJzIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcHBseWluZyAyOjQgU3BhcnNpdHkgd2l0aCBQeVRvcmNoIFNlbWktU3RydWN0dXJlZCBQcnVuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQeVRvcmNoIDIuMSsgaW5jbHVkZXMgdG9yY2guc3BhcnNlLlNwYXJzZVNlbWlTdHJ1Y3R1cmVkVGVuc29yIHdoaWNoIHdyYXBzIHRoZSAyOjQgY29tcHJlc3NlZCBmb3JtYXQuIENhbGxpbmcgdG9fc3BhcnNlX3NlbWlfc3RydWN0dXJlZCh3ZWlnaHQpIHJldHVybnMgYSB0ZW5zb3IgdGhhdCBwYXJ0aWNpcGF0ZXMgdHJhbnNwYXJlbnRseSBpbiBubi5MaW5lYXIgZm9yd2FyZCBhbmQgYmFja3dhcmQgcGFzc2VzLCB1c2luZyBjdVNQQVJTRUx0IHVuZGVyIHRoZSBob29kIG9uIEExMDAgR1BVcy4gTm8gY2hhbmdlcyB0byB0aGUgbW9kZWxcdTAwMjdzIGZvcndhcmQgbWV0aG9kIGFyZSByZXF1aXJlZCDigJQgc2ltcGx5IGNvbnZlcnQgdGhlIHdlaWdodCB0ZW5zb3IgYWZ0ZXIgcHJ1bmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbiMgUmVxdWlyZXMgUHlUb3JjaCBcdTAwM2U9IDIuMSBhbmQgQ1VEQSBBMTAwK1xuIyBmcm9tIHRvcmNoLnNwYXJzZSBpbXBvcnQgdG9fc3BhcnNlX3NlbWlfc3RydWN0dXJlZCwgU3BhcnNlU2VtaVN0cnVjdHVyZWRUZW5zb3JcblxuZGVmIGFwcGx5XzJfNF90b19tb2RlbChtb2RlbDogbm4uTW9kdWxlLCB2ZXJib3NlOiBib29sID0gVHJ1ZSk6XG4gICAgXCJcIlwiXG4gICAgQXBwbHkgMjo0IHN0cnVjdHVyZWQgc3BhcnNpdHkgdG8gYWxsIExpbmVhciBsYXllcnMuXG4gICAgUHJ1bmUgaW4tcGxhY2UgdXNpbmcgbWFnbml0dWRlIGNyaXRlcmlvbiwgdGhlbiBjb252ZXJ0IHRvIHNlbWktc3RydWN0dXJlZCBmb3JtYXQuXG4gICAgXCJcIlwiXG4gICAgbl9jb252ZXJ0ZWQgPSAwXG4gICAgZm9yIG5hbWUsIG1vZHVsZSBpbiBtb2RlbC5uYW1lZF9tb2R1bGVzKCk6XG4gICAgICAgIGlmIG5vdCBpc2luc3RhbmNlKG1vZHVsZSwgbm4uTGluZWFyKTpcbiAgICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgIFcgPSBtb2R1bGUud2VpZ2h0LmRhdGFcbiAgICAgICAgaWYgVy5zaGFwZVsxXSAlIDQgIT0gMDpcbiAgICAgICAgICAgIGlmIHZlcmJvc2U6XG4gICAgICAgICAgICAgICAgcHJpbnQoZlx1MDAyNyAgU2tpcCB7bmFtZX06IGluX2ZlYXR1cmVzPXtXLnNoYXBlWzFdfSBub3QgZGl2aXNpYmxlIGJ5IDRcdTAwMjcpXG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICAjIEdlbmVyYXRlIDI6NCBtYXNrIGFuZCBhcHBseVxuICAgICAgICB3X2dyb3VwZWQgPSBXLnZpZXcoVy5zaGFwZVswXSwgVy5zaGFwZVsxXSAvLyA0LCA0KVxuICAgICAgICBfLCBpZHggPSB3X2dyb3VwZWQuYWJzKCkudG9waygyLCBkaW09LTEpXG4gICAgICAgIG1hc2sgPSB0b3JjaC56ZXJvc19saWtlKHdfZ3JvdXBlZCwgZHR5cGU9dG9yY2guYm9vbClcbiAgICAgICAgbWFzay5zY2F0dGVyXygtMSwgaWR4LCBUcnVlKVxuICAgICAgICBtb2R1bGUud2VpZ2h0LmRhdGEgPSBXICogbWFzay52aWV3KFcuc2hhcGUpLmZsb2F0KClcbiAgICAgICAgbl9jb252ZXJ0ZWQgKz0gMVxuICAgICAgICBpZiB2ZXJib3NlOlxuICAgICAgICAgICAgZGVuc2l0eSA9IG1hc2suZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG4gICAgICAgICAgICBwcmludChmXHUwMDI3ICB7bmFtZX06IHtXLnNoYXBlfSBwcnVuZWQsIGRlbnNpdHk9e2RlbnNpdHk6LjJmfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3QXBwbGllZCAyOjQgc3BhcnNpdHkgdG8ge25fY29udmVydGVkfSBMaW5lYXIgbGF5ZXJzLlx1MDAyNylcblxubW9kZWwgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcig2NCwgMTI4KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoMTI4LCAzMikpXG5hcHBseV8yXzRfdG9fbW9kZWwobW9kZWwpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZnRlciBhcHBseWluZyAyOjQgc3BhcnNpdHksIHJlLXRyYWluaW5nIChmaW5lLXR1bmluZykgZm9yIDEw4oCTMjAgZXBvY2hzIHdpdGggYSBzbWFsbCBsZWFybmluZyByYXRlICgxMCUgb2Ygb3JpZ2luYWwpIGlzIHN1ZmZpY2llbnQgdG8gcmVjb3ZlciBiYXNlbGluZSBhY2N1cmFjeSBvbiBtb3N0IHRhc2tzLiBUcmFpbmluZy10aW1lIDI6NCAoZW5mb3JjaW5nIHRoZSBjb25zdHJhaW50IHRocm91Z2hvdXQgdHJhaW5pbmcpIGdpdmVzIHNsaWdodGx5IGJldHRlciBhY2N1cmFjeSB0aGFuIHBvc3QtdHJhaW5pbmcgcHJ1bmluZyBidXQgcmVxdWlyZXMgbW9kaWZ5aW5nIHRoZSB0cmFpbmluZyBsb29wIHRvIHJlLW1hc2sgZXZlcnkgZmV3IHN0ZXBzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiMjo0IGlzIHRoZSBzd2VldCBzcG90OiA1MCUgc3BhcnNpdHkgd2l0aCAyw5cgaGFyZHdhcmUgc3BlZWR1cCBhdCBuZWFyLXplcm8gYWNjdXJhY3kgY29zdC4iLCJNZXRhZGF0YSBvdmVyaGVhZDogMi1iaXQgaW5kZXggcGVyIHBvc2l0aW9uIGFkZHMgNi4yNSUgc3RvcmFnZSBvdmVyaGVhZCBvdmVyIHRoZSBkZW5zZSB2YWx1ZXMtb25seSBzdG9yYWdlLiIsIk9ubHkgbWF0bXVsIGxheWVycyBiZW5lZml0OiBza2lwIDI6NCBmb3IgZGVwdGh3aXNlIGNvbnYsIGJhdGNoIG5vcm0sIGFuZCBlbWJlZGRpbmcgbGF5ZXJzLiIsIlJlLW1hc2tpbmcgZnJlcXVlbmN5IGR1cmluZyB0cmFpbmluZzogZXZlcnkgMTAw4oCTMTAwMCBzdGVwczsgdG9vIGZyZXF1ZW50IHNsb3dzIHRyYWluaW5nLCB0b28gcmFyZSB3YXN0ZXMgY2FwYWNpdHkuIiwiRm9yIElOVDggKyAyOjQ6IEExMDAgc3VwcG9ydHMgSU5UOCBTcGFyc2UgVGVuc29yIENvcmVzIGdpdmluZyB1cCB0byA0w5cgdGhyb3VnaHB1dCB2cyBGUDE2IGRlbnNlLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# N:M Sparsity — Hardware-Accelerated Structured Sparsity

N:M sparsity is a structured sparsity pattern where, within every consecutive group of M weights, exactly N are nonzero. The 2:4 pattern (2 nonzeros per 4 weights, 50% sparsity) is natively supported by NVIDIA A100 and later GPUs via Sparse Tensor Cores, delivering up to 2× throughput for linear layers with minimal accuracy loss. Unlike unstructured sparsity, 2:4 requires no specialized sparse solver — the hardware handles it transparently.

## How Sparse Tensor Cores Work

In the compressed 2:4 representation, each group of 4 consecutive weights stores only 2 values plus a 2-bit index pair indicating their positions (00, 01, 10, or 11). The weight matrix is compressed to 50% storage. During matrix multiplication, the hardware unpacks the indices and multiplies only the nonzero values with the corresponding activations — effectively computing a sparse GEMM with no wasted multiplications. This is only available for linear (dense matmul) layers; batch norm, embeddings, and depthwise convolutions see no benefit.

## 2:4 Mask Generation

```python
import torch
import torch.nn as nn

def generate_2_4_mask(weight: torch.Tensor) -> torch.Tensor:
    """
    Generate a 2:4 sparsity mask: keep 2 largest-magnitude weights per group of 4.
    weight: any shape; last dim is grouped into blocks of 4.
    Returns a boolean mask of same shape.
    """
    original_shape = weight.shape
    # Flatten to 2D: (rows, cols) where cols must be divisible by 4
    w2d = weight.view(-1, weight.shape[-1])  # (..., C) -> (N, C)
    N, C = w2d.shape
    assert C % 4 == 0, f'Last dim {C} must be divisible by 4 for 2:4 sparsity'

    # Group into blocks of 4
    w_grouped = w2d.view(N, C // 4, 4)  # (N, C//4, 4)
    # Find top-2 magnitudes within each group
    _, top_idx = w_grouped.abs().topk(2, dim=-1)  # (N, C//4, 2)
    # Build mask
    mask = torch.zeros_like(w_grouped, dtype=torch.bool)
    mask.scatter_(-1, top_idx, True)
    return mask.view(original_shape)

# Demonstrate
torch.manual_seed(42)
W = torch.randn(4, 8)  # 4 output neurons, 8 inputs
mask = generate_2_4_mask(W)
print('Weight matrix:')
print(W.round(decimals=2))
print('\n2:4 Mask (1=keep, 0=prune):')
print(mask.int())
print('\nSparse weight:')
print((W * mask).round(decimals=2))
print(f'\nSparsity: {(~mask).float().mean().item():.1%}')
```

## Training with 2:4 Constraint

The 2:4 constraint can be applied post-training (prune + short fine-tune) or enforced during training by re-applying the mask every N gradient steps. During training, the mask is recomputed periodically from the current weight magnitudes, and weights outside the mask are zeroed. Gradients still flow through all positions, but the zeroed weights are re-zeroed before each forward pass. This allows the network to re-allocate the 2 kept positions within each group as training progresses.

```python
import torch
import torch.nn as nn
import torch.optim as optim

class SparseLinear24(nn.Module):
    """Linear layer that enforces 2:4 sparsity on its weight matrix."""

    def __init__(self, in_features: int, out_features: int):
        super().__init__()
        assert in_features % 4 == 0, 'in_features must be divisible by 4'
        self.linear = nn.Linear(in_features, out_features)
        self.mask = self._compute_mask()

    def _compute_mask(self) -> torch.Tensor:
        W = self.linear.weight.data  # (out, in)
        w_grouped = W.view(W.shape[0], W.shape[1] // 4, 4)
        _, idx = w_grouped.abs().topk(2, dim=-1)
        mask = torch.zeros_like(w_grouped, dtype=torch.bool)
        mask.scatter_(-1, idx, True)
        return mask.view(W.shape)

    def apply_mask(self):
        """Re-prune and re-zero weights outside the current mask."""
        self.mask = self._compute_mask()
        with torch.no_grad():
            self.linear.weight.data *= self.mask.float()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)

# Simulate 2:4 training loop
model = SparseLinear24(64, 32)
optimizer = optim.SGD(model.parameters(), lr=0.01)
remask_every = 10  # re-apply 2:4 mask every 10 steps

for step in range(30):
    x = torch.randn(16, 64)
    loss = model(x).pow(2).mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (step + 1) % remask_every == 0:
        model.apply_mask()
        density = model.mask.float().mean().item()
        print(f'Step {step+1}: loss={loss.item():.4f}  density={density:.2f}')
```

## Compressed Storage Format

In the 2:4 compressed format, a weight matrix of shape (M, K) is stored as: (1) a value tensor of shape (M, K/2) containing the 2 nonzero values per group and (2) a metadata tensor of shape (M, K/8) containing 2-bit indices (4 bits per group of 4). Total storage: K/2 values × element_size + K/8 metadata bytes. For FP16 weights, this is (K/2 × 2) + (K/8) = 5K/8 bytes vs K × 2 = 2K bytes uncompressed — a 3.2× reduction in storage per row.

```python
import torch
import numpy as np

def compress_2_4(weight: torch.Tensor):
    """
    Simulate 2:4 compression: returns (values, metadata) tensors.
    values: nonzero elements, shape (rows, cols//2)
    metadata: 4-bit indices packed as uint8, shape (rows, cols//8)
    """
    W = weight.view(-1, weight.shape[-1])  # (N, C)
    N, C = W.shape
    assert C % 4 == 0
    w_grouped = W.view(N, C // 4, 4)  # (N, G, 4) where G = C//4
    scores, indices = w_grouped.abs().topk(2, dim=-1)  # (N, G, 2)
    # Gather nonzero values
    values = w_grouped.gather(-1, indices)  # (N, G, 2)
    values_flat = values.reshape(N, C // 2)  # (N, C//2)
    # Pack indices as 4 bits per group (2 positions in {0,1,2,3})
    # Each index fits in 2 bits; 4 bits per group of 4
    idx_sorted = indices.sort(dim=-1).values  # ensure ascending order
    meta = (idx_sorted[..., 0] * 4 + idx_sorted[..., 1]).to(torch.uint8)  # (N, G)
    return values_flat, meta

W = torch.randn(8, 16)
vals, meta = compress_2_4(W)

uncompressed_bytes = W.numel() * 4  # float32
compressed_bytes = vals.numel() * 4 + meta.numel()  # float32 vals + uint8 meta
print(f'Original: {W.shape}  ->  {uncompressed_bytes} bytes')
print(f'Values:   {vals.shape},  Metadata: {meta.shape}')
print(f'Compressed: {compressed_bytes} bytes  (ratio {uncompressed_bytes/compressed_bytes:.2f}x)')
print(f'Density check: {vals.numel()}/{W.numel()} = {vals.numel()/W.numel():.0%}')
```

> **2:4 Only Helps on A100+ for Linear Layers**: Sparse Tensor Core acceleration is only available on NVIDIA Ampere (A100) and later GPUs. On earlier GPUs (V100, T4) or on CPU, 2:4 sparsity provides no speedup — the sparse zeros still participate in computation. Additionally, only linear (matmul) layers benefit; depthwise convolutions, batch norm, and embeddings remain dense. For CPU deployment, unstructured sparsity with SpMM or full structured pruning are better choices.

## Accuracy vs Dense Baseline

NVIDIA's experiments on ResNet-50 and BERT show that 2:4 sparsity with 10–20 epochs of fine-tuning recovers to within 0.1–0.5% of the dense baseline. The key insight is that within each group of 4, the 2 surviving weights can be any pair — this gives the network enough flexibility to represent the same functions as the dense model. Larger models (GPT-3 scale) show even smaller accuracy gaps, as the redundancy in large models makes it easier to prune half the weights without losing function.

## Comparison of Sparsity Formats

| Format | Sparsity | A100 Speedup | Accuracy vs Dense | Hardware Support | Implementation Difficulty |
| --- | --- | --- | --- | --- | --- |
| Dense (baseline) | 0% | 1× | Baseline | All hardware | Trivial |
| 2:4 (N=2, M=4) | 50% | ~2× | -0.1 to -0.5% | A100+ only (Ampere) | Low — torch.nn.utils.prune or apex |
| 1:4 (N=1, M=4) | 75% | ~2× (same HW path) | -2 to -5% | A100+ only | Low — same tooling |
| Unstructured 50% | 50% | ~1× (no HW support) | -0.5 to -2% | None (standard GPU) | Low — threshold mask |
| Structured filter 50% | 50% of filters | ~1.5–2× (any GPU) | -1 to -3% | All hardware | High — reshape dependent layers |

## Applying 2:4 Sparsity with PyTorch Semi-Structured Pruning

PyTorch 2.1+ includes torch.sparse.SparseSemiStructuredTensor which wraps the 2:4 compressed format. Calling to_sparse_semi_structured(weight) returns a tensor that participates transparently in nn.Linear forward and backward passes, using cuSPARSELt under the hood on A100 GPUs. No changes to the model's forward method are required — simply convert the weight tensor after pruning.

```python
import torch
import torch.nn as nn
# Requires PyTorch >= 2.1 and CUDA A100+
# from torch.sparse import to_sparse_semi_structured, SparseSemiStructuredTensor

def apply_2_4_to_model(model: nn.Module, verbose: bool = True):
    """
    Apply 2:4 structured sparsity to all Linear layers.
    Prune in-place using magnitude criterion, then convert to semi-structured format.
    """
    n_converted = 0
    for name, module in model.named_modules():
        if not isinstance(module, nn.Linear):
            continue
        W = module.weight.data
        if W.shape[1] % 4 != 0:
            if verbose:
                print(f'  Skip {name}: in_features={W.shape[1]} not divisible by 4')
            continue
        # Generate 2:4 mask and apply
        w_grouped = W.view(W.shape[0], W.shape[1] // 4, 4)
        _, idx = w_grouped.abs().topk(2, dim=-1)
        mask = torch.zeros_like(w_grouped, dtype=torch.bool)
        mask.scatter_(-1, idx, True)
        module.weight.data = W * mask.view(W.shape).float()
        n_converted += 1
        if verbose:
            density = mask.float().mean().item()
            print(f'  {name}: {W.shape} pruned, density={density:.2f}')
    print(f'Applied 2:4 sparsity to {n_converted} Linear layers.')

model = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 32))
apply_2_4_to_model(model)
```

After applying 2:4 sparsity, re-training (fine-tuning) for 10–20 epochs with a small learning rate (10% of original) is sufficient to recover baseline accuracy on most tasks. Training-time 2:4 (enforcing the constraint throughout training) gives slightly better accuracy than post-training pruning but requires modifying the training loop to re-mask every few steps.

- 2:4 is the sweet spot: 50% sparsity with 2× hardware speedup at near-zero accuracy cost.
- Metadata overhead: 2-bit index per position adds 6.25% storage overhead over the dense values-only storage.
- Only matmul layers benefit: skip 2:4 for depthwise conv, batch norm, and embedding layers.
- Re-masking frequency during training: every 100–1000 steps; too frequent slows training, too rare wastes capacity.
- For INT8 + 2:4: A100 supports INT8 Sparse Tensor Cores giving up to 4× throughput vs FP16 dense.

---

