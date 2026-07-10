---
title: "Multi-Layer RNNs — Depth in Sequence Models"
slug: "multi-layer-rnns"
description: "Stacking RNN layers creates hierarchical temporal representations: lower layers capture fine-grained local patterns, higher layers integrate them into abstract structures. Covers 2-layer LSTM from scratch, PyTorch num_layers with variational dropout, layer-wise gradient analysis, residual stacked LSTM, and depth vs width trade-offs."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBzaW5nbGUtbGF5ZXIgUk5OIGxlYXJucyB0ZW1wb3JhbCBwYXR0ZXJucyBmcm9tIHJhdyBpbnB1dCwgYnV0IGRlZXAgbmV0d29ya3MgY2FuIGxlYXJuIGhpZXJhcmNoaWNhbCByZXByZXNlbnRhdGlvbnMg4oCUIGxvdyBsYXllcnMgZGV0ZWN0IGxvY2FsIHN0cnVjdHVyZSAobi1ncmFtcywgcGhvbmVtZXMsIGxvY2FsIHN5bnRheCkgd2hpbGUgaGlnaCBsYXllcnMgaW50ZWdyYXRlIHRoZXNlIGludG8gZ2xvYmFsIHBhdHRlcm5zIChzZW1hbnRpY3MsIGxvbmctcmFuZ2UgZGVwZW5kZW5jaWVzKS4gU3RhY2tlZCBSTk5zIGFwcGx5IHRoaXMgcHJpbmNpcGxlIHRvIHNlcXVlbmNlczogdGhlIG91dHB1dCBzZXF1ZW5jZSBvZiBsYXllciBsIGJlY29tZXMgdGhlIGlucHV0IHNlcXVlbmNlIG9mIGxheWVyIGwrMS4gRGVwdGggaW4gc2VxdWVuY2UgbW9kZWxzIHByb3ZpZGVzIHRoZSBzYW1lIGluZHVjdGl2ZSBiaWFzIGFzIGRlcHRoIGluIENOTnM6IGhpZXJhcmNoaWNhbCBmZWF0dXJlIGV4dHJhY3Rpb24gYXQgbXVsdGlwbGUgc2NhbGVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBTdGFjayBSTk4gTGF5ZXJzPyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gQ05OcywgZGVwdGggZW5hYmxlcyBoaWVyYXJjaGljYWwgZmVhdHVyZSBkZXRlY3Rpb246IGVkZ2VzIOKGkiB0ZXh0dXJlcyDihpIgcGFydHMg4oaSIG9iamVjdHMuIFRoZSBzYW1lIHByaW5jaXBsZSBhcHBsaWVzIHRvIHNlcXVlbmNlczogbGF5ZXIgMSBtaWdodCBkZXRlY3QgY2hhcmFjdGVyIG4tZ3JhbXMgb3IgbG9jYWwgZGVwZW5kZW5jeSBlZGdlcywgbGF5ZXIgMiBpbnRlZ3JhdGVzIHRoZXNlIGludG8gcGhyYXNlLWxldmVsIHBhdHRlcm5zLCBsYXllciAzIGNhcHR1cmVzIHNlbnRlbmNlLWxldmVsIHN0cnVjdHVyZS4gRW1waXJpY2FsbHksIHR3by1sYXllciBMU1RNcyBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybSBzaW5nbGUtbGF5ZXIgTFNUTXMgb24gbGFuZ3VhZ2UgbW9kZWxpbmcgYW5kIHRyYW5zbGF0aW9uIHRhc2tzLCB3aXRoIGRpbWluaXNoaW5nIHJldHVybnMgYmV5b25kIDQgbGF5ZXJzLiBUaGUga2V5IGNvbnN0cmFpbnQgaXMgdGhhdCBlYWNoIGxheWVyIGRvdWJsZXMgdGhlIGdyYWRpZW50IHBhdGggbGVuZ3RoLCBjb21wb3VuZGluZyB0aGUgdmFuaXNoaW5nIGdyYWRpZW50IHByb2JsZW0gYWNyb3NzIGJvdGggdGltZSBhbmQgZGVwdGguIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHdvLUxheWVyIExTVE0gZnJvbSBTY3JhdGNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBhIHN0YWNrZWQgTFNUTSwgbGF5ZXIgMSByZWNlaXZlcyB0aGUgaW5wdXQgc2VxdWVuY2UgeHQgYW5kIHByb2R1Y2VzIG91dHB1dCBzZXF1ZW5jZSBvdXQxdC4gTGF5ZXIgMiByZWNlaXZlcyBvdXQxdCBhcyBpdHMgaW5wdXQgYW5kIHByb2R1Y2VzIG91dDJ0LiBCZXR3ZWVuIGxheWVycywgZHJvcG91dCBpcyBhcHBsaWVkIHRvIHRoZSBvdXRwdXQgb2YgbGF5ZXIgMSBiZWZvcmUgZmVlZGluZyBpbnRvIGxheWVyIDIg4oCUIHRoaXMgaXMgc3RhbmRhcmQgaW50ZXItbGF5ZXIgZHJvcG91dC4gVGhlIGhpZGRlbiBhbmQgY2VsbCBzdGF0ZXMgb2YgZWFjaCBsYXllciBhcmUgbWFpbnRhaW5lZCBzZXBhcmF0ZWx5OiBbKGgxLCBjMSksIChoMiwgYzIpXS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgU3RhY2tlZExTVE0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJUd28tbGF5ZXIgTFNUTTogbGF5ZXItMSBvdXRwdXQgaXMgbGF5ZXItMiBpbnB1dCwgd2l0aCBpbnRlci1sYXllciBkcm9wb3V0LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSwgZHJvcG91dF9wPTAuMyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmxzdG0xID0gbm4uTFNUTShpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5sc3RtMiA9IG5uLkxTVE0oaGlkZGVuX3NpemUsIGhpZGRlbl9zaXplLCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLmRyb3AgID0gbm4uRHJvcG91dChkcm9wb3V0X3ApXG4gICAgICAgIHNlbGYuaGlkZGVuX3NpemUgPSBoaWRkZW5fc2l6ZVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgc3RhdGVzPU5vbmUpOlxuICAgICAgICBpZiBzdGF0ZXMgaXMgTm9uZTpcbiAgICAgICAgICAgIHN0YXRlcyA9IFtOb25lLCBOb25lXVxuICAgICAgICBvdXQxLCAoaDEsIGMxKSA9IHNlbGYubHN0bTEoeCwgc3RhdGVzWzBdKVxuICAgICAgICBvdXQxX2Ryb3BwZWQgPSBzZWxmLmRyb3Aob3V0MSkgICAgICAgICAgICAgICMgaW50ZXItbGF5ZXIgZHJvcG91dFxuICAgICAgICBvdXQyLCAoaDIsIGMyKSA9IHNlbGYubHN0bTIob3V0MV9kcm9wcGVkLCBzdGF0ZXNbMV0pXG4gICAgICAgIHJldHVybiBvdXQyLCBbKGgxLCBjMSksIChoMiwgYzIpXSwgb3V0MVxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbkIsIFQsIEksIEggPSA0LCAyMCwgOCwgMzJcbm1vZGVsID0gU3RhY2tlZExTVE0oaW5wdXRfc2l6ZT1JLCBoaWRkZW5fc2l6ZT1IKVxueCA9IHRvcmNoLnJhbmRuKEIsIFQsIEkpXG5vdXQyLCBzdGF0ZXMsIG91dDEgPSBtb2RlbCh4KVxuaDEsIGMxID0gc3RhdGVzWzBdXG5oMiwgYzIgPSBzdGF0ZXNbMV1cblxucHJpbnQoXHUwMDI3Mi1sYXllciBzdGFja2VkIExTVE06XHUwMDI3KVxucHJpbnQoXHUwMDI3ICBJbnB1dDogICAge31cdTAwMjcuZm9ybWF0KHR1cGxlKHguc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgTDEgb3V0OiAgIHt9ICAtXHUwMDNlIGRyb3BvdXQgLVx1MDAzZSBMMiBpbnB1dFx1MDAyNy5mb3JtYXQodHVwbGUob3V0MS5zaGFwZSkpKVxucHJpbnQoXHUwMDI3ICBMMiBvdXQ6ICAge31cdTAwMjcuZm9ybWF0KHR1cGxlKG91dDIuc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgaDE6IHt9ICBoMjoge31cdTAwMjcuZm9ybWF0KHR1cGxlKGgxLnNoYXBlKSwgdHVwbGUoaDIuc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgUGFyYW1zOiB7Oix9XHUwMDI3LmZvcm1hdChzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSkpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlB5VG9yY2ggbnVtX2xheWVycyB3aXRoIFZhcmlhdGlvbmFsIERyb3BvdXQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Im5uLkxTVE1cdTAwMjdzIG51bV9sYXllcnMgcGFyYW1ldGVyIHN0YWNrcyBsYXllcnMgYXV0b21hdGljYWxseS4gSXRzIGRyb3BvdXQgcGFyYW1ldGVyIGFwcGxpZXMgYmV0d2VlbiBsYXllcnMgKG5vdCB2YXJpYXRpb25hbCDigJQgYSBkaWZmZXJlbnQgbWFzayBhdCBlYWNoIHRpbWVzdGVwKS4gVmFyaWF0aW9uYWwgZHJvcG91dCAoR2FsIFx1MDAyNiBHaGFocmFtYW5pIDIwMTYpIHVzZXMgdGhlIHNhbWUgZHJvcG91dCBtYXNrIGFjcm9zcyBhbGwgVCB0aW1lc3RlcHMsIHdoaWNoIGlzIG1vcmUgY29uc2lzdGVudCB3aXRoIEJheWVzaWFuIGluZmVyZW5jZSBhbmQgZW1waXJpY2FsbHkgcGVyZm9ybXMgYmV0dGVyLiBJbXBsZW1lbnRpbmcgdmFyaWF0aW9uYWwgZHJvcG91dCByZXF1aXJlcyBtYW51YWxseSBtYXNraW5nIHRoZSBpbnB1dCBiZWZvcmUgcGFzc2luZyBpdCB0byB0aGUgTFNUTS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgVmFyRHJvcExTVE0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJNdWx0aS1sYXllciBMU1RNIHdpdGggdmFyaWF0aW9uYWwgZHJvcG91dCAoc2FtZSBtYXNrIGFjcm9zcyBhbGwgdGltZXN0ZXBzKS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfc2l6ZSwgaGlkZGVuX3NpemUsIG51bV9sYXllcnMsIGRyb3BvdXRfcD0wLjMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5sc3RtID0gbm4uTFNUTShpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSwgbnVtX2xheWVycz1udW1fbGF5ZXJzLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRyb3BvdXQ9ZHJvcG91dF9wIGlmIG51bV9sYXllcnMgXHUwMDNlIDEgZWxzZSAwLjAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5kcm9wb3V0X3AgPSBkcm9wb3V0X3BcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBpZiBzZWxmLnRyYWluaW5nIGFuZCBzZWxmLmRyb3BvdXRfcCBcdTAwM2UgMDpcbiAgICAgICAgICAgICMgU2FtcGxlIG9uZSBtYXNrOyBhcHBseSBhY3Jvc3MgYWxsIFQgdGltZXN0ZXBzICh2YXJpYXRpb25hbClcbiAgICAgICAgICAgIG1hc2sgPSAodG9yY2gucmFuZCh4LnNpemUoMCksIDEsIHguc2l6ZSgyKSkgXHUwMDNlIHNlbGYuZHJvcG91dF9wKS5mbG9hdCgpXG4gICAgICAgICAgICBtYXNrID0gbWFzayAvICgxLjAgLSBzZWxmLmRyb3BvdXRfcCkgICAjIHJlc2NhbGUgZm9yIGV4cGVjdGVkIHZhbHVlXG4gICAgICAgICAgICB4ID0geCAqIG1hc2tcbiAgICAgICAgcmV0dXJuIHNlbGYubHN0bSh4KVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuQiwgVCwgSSwgSCwgTCA9IDgsIDI1LCAxNiwgNjQsIDNcbm1vZGVsID0gVmFyRHJvcExTVE0oSSwgSCwgbnVtX2xheWVycz1MLCBkcm9wb3V0X3A9MC4zKVxubW9kZWwudHJhaW4oKVxueCA9IHRvcmNoLnJhbmRuKEIsIFQsIEkpXG5vdXQsIChoLCBjKSA9IG1vZGVsKHgpXG5cbnByaW50KFx1MDAyNzMtbGF5ZXIgTFNUTSB3aXRoIHZhcmlhdGlvbmFsIGRyb3BvdXQgKHRyYWluaW5nIG1vZGUpOlx1MDAyNylcbnByaW50KFx1MDAyNyAgSW5wdXQ6ICAge31cdTAwMjcuZm9ybWF0KHR1cGxlKHguc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgT3V0cHV0OiAge31cdTAwMjcuZm9ybWF0KHR1cGxlKG91dC5zaGFwZSkpKVxucHJpbnQoXHUwMDI3ICBoX246ICAgICB7fSAgIFx1MDAzYy0gKG51bV9sYXllcnMsIEIsIEgpXHUwMDI3LmZvcm1hdCh0dXBsZShoLnNoYXBlKSkpXG5wcmludChcdTAwMjcgIFBhcmFtczogIHs6LH1cdTAwMjcuZm9ybWF0KHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKSkpXG5wcmludChcdTAwMjcgIHZzIHN0YW5kYXJkIGRyb3BvdXQ6IGRpZmZlcmVudCBtYXNrIGVhY2ggc3RlcCAobm90IHZhcmlhdGlvbmFsKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXllci1XaXNlIEdyYWRpZW50IEFuYWx5c2lzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBhIHN0YWNrZWQgTFNUTSwgZ3JhZGllbnQgbXVzdCBmbG93IGJvdGggYmFja3dhcmQgdGhyb3VnaCB0aW1lIChCUFRUKSBhbmQgZG93bndhcmQgdGhyb3VnaCBsYXllcnMuIFRoZSBib3R0b20gbGF5ZXIgKGNsb3Nlc3QgdG8gaW5wdXQsIGZ1cnRoZXN0IGZyb20gbG9zcykgcmVjZWl2ZXMgdGhlIHdlYWtlc3QgZ3JhZGllbnQg4oCUIGl0IGlzIGNvbXBvdW5kZWQgYnkgYm90aCB2YW5pc2hpbmcgYWNyb3NzIHRpbWVzdGVwcyBhbmQgYXR0ZW51YXRpb24gYWNyb3NzIGxheWVycy4gTWVhc3VyaW5nIGdyYWRpZW50IG5vcm1zIHBlciBsYXllciByZXZlYWxzIHRoaXMgZWZmZWN0OiB0b3AgbGF5ZXJzIHR5cGljYWxseSBoYXZlIDXigJMyMHggbGFyZ2VyIGdyYWRpZW50IG5vcm1zIHRoYW4gYm90dG9tIGxheWVycyBpbiBhIDQtbGF5ZXIgc3RhY2suIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBsYXllcl9ncmFkaWVudF9ub3JtcyhudW1fbGF5ZXJzPTQsIEk9OCwgSD0zMiwgVD0yMCk6XG4gICAgXCJcIlwiTWVhc3VyZSB3ZWlnaHQgZ3JhZGllbnQgbm9ybSBpbiBlYWNoIGxheWVyIG9mIGEgc3RhY2tlZCBMU1RNLlwiXCJcIlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKDApXG4gICAgbHN0bSA9IG5uLkxTVE0oSSwgSCwgbnVtX2xheWVycz1udW1fbGF5ZXJzLCBiYXRjaF9maXJzdD1UcnVlKVxuICAgIHggPSB0b3JjaC5yYW5kbig0LCBULCBJKVxuICAgIG91dCwgXyA9IGxzdG0oeClcbiAgICBvdXRbOiwgLTEsIDpdLnN1bSgpLmJhY2t3YXJkKClcblxuICAgIHByaW50KFx1MDAyN0dyYWRpZW50IG5vcm1zIGZvciB7fS1sYXllciBMU1RNIChsb3NzIGF0IGZpbmFsIHRpbWVzdGVwKTpcdTAwMjcuZm9ybWF0KG51bV9sYXllcnMpKVxuICAgIHByaW50KFx1MDAyN3s6XHUwMDNlN30gezpcdTAwM2UxOH0gezpcdTAwM2UxOH1cdTAwMjcuZm9ybWF0KFx1MDAyN0xheWVyXHUwMDI3LCBcdTAwMjd3ZWlnaHRfaWggbm9ybVx1MDAyNywgXHUwMDI3d2VpZ2h0X2hoIG5vcm1cdTAwMjcpKVxuICAgIG5vcm1zX2hoID0gW11cbiAgICBmb3IgbCBpbiByYW5nZShudW1fbGF5ZXJzKTpcbiAgICAgICAgd2loID0gZ2V0YXR0cihsc3RtLCBcdTAwMjd3ZWlnaHRfaWhfbHt9XHUwMDI3LmZvcm1hdChsKSlcbiAgICAgICAgd2hoID0gZ2V0YXR0cihsc3RtLCBcdTAwMjd3ZWlnaHRfaGhfbHt9XHUwMDI3LmZvcm1hdChsKSlcbiAgICAgICAgZ19paCA9IHdpaC5ncmFkLm5vcm0oKS5pdGVtKCkgaWYgd2loLmdyYWQgaXMgbm90IE5vbmUgZWxzZSAwLjBcbiAgICAgICAgZ19oaCA9IHdoaC5ncmFkLm5vcm0oKS5pdGVtKCkgaWYgd2hoLmdyYWQgaXMgbm90IE5vbmUgZWxzZSAwLjBcbiAgICAgICAgbm9ybXNfaGguYXBwZW5kKGdfaGgpXG4gICAgICAgIHRhZyA9IFx1MDAyNyBcdTAwM2MtIGlucHV0IGxheWVyXHUwMDI3IGlmIGwgPT0gMCBlbHNlIChcdTAwMjcgXHUwMDNjLSBvdXRwdXQgbGF5ZXJcdTAwMjcgaWYgbCA9PSBudW1fbGF5ZXJzLTEgZWxzZSBcdTAwMjdcdTAwMjcpXG4gICAgICAgIHByaW50KFx1MDAyN3s6XHUwMDNlN30gezpcdTAwM2UxOC40Zn0gezpcdTAwM2UxOC40Zn17fVx1MDAyNy5mb3JtYXQobCwgZ19paCwgZ19oaCwgdGFnKSlcbiAgICByYXRpbyA9IG5vcm1zX2hoWy0xXSAvIG1heChub3Jtc19oaFswXSwgMWUtMjApXG4gICAgcHJpbnQoXHUwMDI3R3JhZGllbnQgcmF0aW8gKHRvcCAvIGJvdHRvbSBsYXllcik6IHs6LjJmfXhcdTAwMjcuZm9ybWF0KHJhdGlvKSlcblxubGF5ZXJfZ3JhZGllbnRfbm9ybXMobnVtX2xheWVycz00KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlc2lkdWFsIENvbm5lY3Rpb25zIGluIFN0YWNrZWQgTFNUTXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlc2lkdWFsIGNvbm5lY3Rpb25zIOKAlCBhZGRpbmcgdGhlIGlucHV0IG9mIGEgbGF5ZXIgdG8gaXRzIG91dHB1dCDigJQgYXJlIHN0YW5kYXJkIGluIGRlZXAgQ05OcyAoUmVzTmV0cykgYW5kIFRyYW5zZm9ybWVycyBidXQgbGVzcyBjb21tb24gaW4gc3RhY2tlZCBMU1RNcy4gVGhleSBwcm92aWRlIGFuIGFkZGl0aW9uYWwgZ3JhZGllbnQgaGlnaHdheSBieXBhc3NpbmcgZWFjaCBsYXllclx1MDAyN3MgY29tcHV0YXRpb24sIGhlbHBpbmcgd2l0aCB0cmFpbmluZyA0KyBsYXllciBzdGFja3MuIEZvciByZXNpZHVhbCBjb25uZWN0aW9ucyB0byB3b3JrIGluIHN0YWNrZWQgTFNUTXMsIHRoZSBpbnB1dCBkaW1lbnNpb24gYW5kIGhpZGRlbiBzaXplIG11c3QgbWF0Y2guIEEgbGluZWFyIHByb2plY3Rpb24gbGF5ZXIgaXMgdXNlZCBvdGhlcndpc2UuIExheWVyIG5vcm1hbGl6YXRpb24gaXMgdHlwaWNhbGx5IGFwcGxpZWQgYWZ0ZXIgdGhlIHJlc2lkdWFsIGFkZGl0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBSZXNMU1RNTGF5ZXIobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTaW5nbGUgTFNUTSBsYXllciB3aXRoIHJlc2lkdWFsIGNvbm5lY3Rpb24gKyBsYXllciBub3JtIChyZXF1aXJlcyBkX2luID09IGRfaGlkZGVuKS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaGlkZGVuX3NpemUsIGRyb3BvdXRfcD0wLjEpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5sc3RtID0gbm4uTFNUTShoaWRkZW5fc2l6ZSwgaGlkZGVuX3NpemUsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYubm9ybSA9IG5uLkxheWVyTm9ybShoaWRkZW5fc2l6ZSlcbiAgICAgICAgc2VsZi5kcm9wID0gbm4uRHJvcG91dChkcm9wb3V0X3ApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgb3V0LCBzdGF0ZSA9IHNlbGYubHN0bSh4KVxuICAgICAgICByZXR1cm4gc2VsZi5ub3JtKHggKyBzZWxmLmRyb3Aob3V0KSksIHN0YXRlICAgIyByZXNpZHVhbCArIGxheWVyIG5vcm1cblxuY2xhc3MgUmVzU3RhY2tlZExTVE0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJOLWxheWVyIHJlc2lkdWFsIHN0YWNrZWQgTFNUTSBmb3IgbGFuZ3VhZ2UgbW9kZWxpbmcuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHZvY2FiX3NpemUsIGVtYmVkX2RpbSwgaGlkZGVuX3NpemUsIG5fbGF5ZXJzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW1iZWQgICA9IG5uLkVtYmVkZGluZyh2b2NhYl9zaXplLCBlbWJlZF9kaW0pXG4gICAgICAgIHNlbGYucHJval9pbiA9IG5uLkxpbmVhcihlbWJlZF9kaW0sIGhpZGRlbl9zaXplKVxuICAgICAgICBzZWxmLmxheWVycyAgPSBubi5Nb2R1bGVMaXN0KFtSZXNMU1RNTGF5ZXIoaGlkZGVuX3NpemUpIGZvciBfIGluIHJhbmdlKG5fbGF5ZXJzKV0pXG4gICAgICAgIHNlbGYuZmMgICAgICA9IG5uLkxpbmVhcihoaWRkZW5fc2l6ZSwgdm9jYWJfc2l6ZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHRva2Vucyk6XG4gICAgICAgIHggPSBzZWxmLnByb2pfaW4oc2VsZi5lbWJlZCh0b2tlbnMpKVxuICAgICAgICBmb3IgbGF5ZXIgaW4gc2VsZi5sYXllcnM6XG4gICAgICAgICAgICB4LCBfID0gbGF5ZXIoeClcbiAgICAgICAgcmV0dXJuIHNlbGYuZmMoeClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbm1vZGVsID0gUmVzU3RhY2tlZExTVE0odm9jYWJfc2l6ZT0xMDAwLCBlbWJlZF9kaW09NjQsIGhpZGRlbl9zaXplPTY0LCBuX2xheWVycz00KVxudG9rZW5zID0gdG9yY2gucmFuZGludCgwLCAxMDAwLCAoNCwgMzApKVxubG9naXRzID0gbW9kZWwodG9rZW5zKVxucHJpbnQoXHUwMDI3NC1sYXllciBSZXNpZHVhbCBTdGFja2VkIExTVE06XHUwMDI3KVxucHJpbnQoXHUwMDI3ICBJbnB1dCB0b2tlbnM6IHt9XHUwMDI3LmZvcm1hdCh0dXBsZSh0b2tlbnMuc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgT3V0cHV0IGxvZ2l0czoge30gIChwZXItcG9zaXRpb24gdm9jYWIgc2NvcmVzKVx1MDAyNy5mb3JtYXQodHVwbGUobG9naXRzLnNoYXBlKSkpXG5wcmludChcdTAwMjcgIFBhcmFtczogezosfVx1MDAyNy5mb3JtYXQoc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpKSkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IjLigJM0IExheWVycyBVc3VhbGx5IFN1ZmZpY2llbnQgZm9yIFN0YWNrZWQgTFNUTXMiLCJjb250ZW50IjoiVW5saWtlIENOTnMgd2hpY2ggbWF5IHVzZSA1MOKAkzIwMCBsYXllcnMsIHN0YWNrZWQgTFNUTXMgcmFyZWx5IGJlbmVmaXQgYmV5b25kIDQgbGF5ZXJzLiBUaGUgY29tcG91bmRpbmcgdmFuaXNoaW5nIGdyYWRpZW50IChhY3Jvc3MgYm90aCB0aW1lIGFuZCBkZXB0aCkgbWFrZXMgdmVyeSBkZWVwIExTVE1zIGhhcmQgdG8gdHJhaW4gd2l0aG91dCByZXNpZHVhbCBjb25uZWN0aW9ucyBhbmQgY2FyZWZ1bCBpbml0aWFsaXphdGlvbi4gRW1waXJpY2FsbHksIDItbGF5ZXIgTFNUTXMgb3V0cGVyZm9ybSAxLWxheWVyIGJ5IDPigJM4IHBlcnBsZXhpdHkgcG9pbnRzIG9uIGxhbmd1YWdlIG1vZGVsaW5nOyAzLWxheWVyIGFkZHMgYW5vdGhlciAy4oCTNCBwb2ludHM7IDQtbGF5ZXIgbWFyZ2luYWwgaW1wcm92ZW1lbnQgd2l0aCBsb25nZXIgdHJhaW5pbmcgdGltZS4gU3BlbmQgY29tcHV0ZSBidWRnZXQgb24gd2lkZXIgaGlkZGVuIHNpemUgb3IgbG9uZ2VyIHRyYWluaW5nIGJlZm9yZSBhZGRpbmcgbW9yZSBsYXllcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVwdGggdnMgV2lkdGggVHJhZGUtb2ZmIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBmaXhlZCBwYXJhbWV0ZXIgYnVkZ2V0LCB0aGUgY2hvaWNlIGJldHdlZW4gYSBzaW5nbGUgd2lkZXIgbGF5ZXIgYW5kIG11bHRpcGxlIG5hcnJvd2VyIGxheWVycyBhZmZlY3RzIGJvdGggcXVhbGl0eSBhbmQgdHJhaW5pbmcgZHluYW1pY3MuIFdpZGVyIHNpbmdsZS1sYXllciBtb2RlbHMgaGF2ZSBtb3JlIGRpcmVjdCBjb25uZWN0aW9ucyBiZXR3ZWVuIGlucHV0IGFuZCBvdXRwdXQsIHdoaWxlIGRlZXBlciBtb2RlbHMgbGVhcm4gaGllcmFyY2hpY2FsIGZlYXR1cmVzLiBPbiBsYW5ndWFnZSBtb2RlbGluZyBiZW5jaG1hcmtzLCAyLTMgbGF5ZXIgTFNUTXMgY29uc2lzdGVudGx5IG91dHBlcmZvcm0gZXF1aXZhbGVudC1wYXJhbWV0ZXIgMS1sYXllciBtb2RlbHMsIHN1Z2dlc3RpbmcgdGhhdCBkZXB0aCBwcm92aWRlcyBhIHVzZWZ1bCBpbmR1Y3RpdmUgYmlhcyBiZXlvbmQgcmF3IHBhcmFtZXRlciBjb3VudC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQ29uZmlnIiwiUGFyYW1zIChJPTI1NikiLCJQVEIgUGVycGxleGl0eSIsIlRyYWluIHRpbWUgLyBlcG9jaCIsIkdyYWRpZW50IChib3R0b20gbGF5ZXIpIiwiRGVwdGggYmVuZWZpdCJdLCJyb3dzIjpbWyIxLWxheWVyIEg9NTEyIiwifjEuNk0iLCJ+OTAiLCIxeCAoYmFzZWxpbmUpIiwiU3Ryb25nIOKAlCBubyBkZXB0aCBkZWNheSIsIk5vbmUg4oCUIGZsYXQgZmVhdHVyZXMiXSxbIjItbGF5ZXIgSD0zNjQiLCJ+MS42TSIsIn43OCIsIn4xLjh4IiwiTW9kZXJhdGUg4oCUIDEgZXh0cmEgaG9wIiwiTG9jYWwgKyBtaWQtcmFuZ2UgcGF0dGVybnMiXSxbIjMtbGF5ZXIgSD0yOTciLCJ+MS42TSIsIn43NCIsIn4yLjV4IiwiV2VhayDigJQgMiBleHRyYSBob3BzIiwiSGllcmFyY2hpY2FsIGZlYXR1cmVzIl0sWyI0LWxheWVyIEg9MjU2IiwifjEuNk0iLCJ+NzMiLCJ+My4yeCIsIlZlcnkgd2VhayDigJQgbmVlZHMgcmVzaWR1YWwiLCJNYXJnaW5hbCBvdmVyIDMtbGF5ZXIiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhpZXJhcmNoaWNhbCBUZW1wb3JhbCBGZWF0dXJlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGhpZXJhcmNoaWNhbCBmZWF0dXJlIGh5cG90aGVzaXMgZm9yIHN0YWNrZWQgTFNUTXM6IGxvd2VyIGxheWVycyBkZXZlbG9wIHNlbnNpdGl2aXR5IHRvIGxvY2FsLCBmaW5lLWdyYWluZWQgcGF0dGVybnMgKGNoYXJhY3RlcnMsIG1vcnBoZW1lcywgc2hvcnQgbi1ncmFtcywgbG9jYWwgc3ludGFjdGljIGRlcGVuZGVuY2llcykgd2hpbGUgaGlnaGVyIGxheWVycyBkZXZlbG9wIHNlbnNpdGl2aXR5IHRvIGdsb2JhbCwgYWJzdHJhY3QgcGF0dGVybnMgKHBocmFzZXMsIGNsYXVzZXMsIHNlbWFudGljIHJlbGF0aW9uc2hpcHMpLiBUaGlzIGhhcyBiZWVuIGVtcGlyaWNhbGx5IGNvbmZpcm1lZCB0aHJvdWdoIHByb2JpbmcgdGFza3M6IGxheWVyIDEgb2YgYSAzLWxheWVyIExTVE0gYmVzdCBwcmVkaWN0cyBwYXJ0LW9mLXNwZWVjaCB0YWdzOyBsYXllciAzIGJlc3QgcHJlZGljdHMgc2VtYW50aWMgcm9sZXMgYW5kIGxvbmctcmFuZ2UgY29yZWZlcmVuY2UuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMYXllciAxIChjbG9zZXN0IHRvIGlucHV0KTogY2hhcmFjdGVyIHRyaWdyYW1zLCBtb3JwaG9sb2dpY2FsIHN1ZmZpeGVzLCBsb2NhbCBQT1MgcGF0dGVybnMuIiwiTGF5ZXIgMiAobWlkZGxlKTogcGhyYXNlIGJvdW5kYXJpZXMsIGxvY2FsIGRlcGVuZGVuY3kgZWRnZXMsIG5hbWVkIGVudGl0eSBzcGFucy4iLCJMYXllciAzIChjbG9zZXN0IHRvIG91dHB1dCk6IGNsYXVzZSBzdHJ1Y3R1cmUsIHNlbWFudGljIHJvbGVzLCBjb3JlZmVyZW5jZSwgdG9waWMuIiwiSW50ZXItbGF5ZXIgZHJvcG91dDogcHJldmVudHMgbGF5ZXIgMiBmcm9tIG92ZXJmaXR0aW5nIHRvIHJhdyBsYXllci0xIGFjdGl2YXRpb25zLiIsIlJlc2lkdWFsIGNvbm5lY3Rpb25zOiBhbGxvdyBncmFkaWVudCB0byBieXBhc3MgbGF5ZXJzIOKAlCBlbmFibGVzIGVmZmVjdGl2ZSBkZXB0aCBcdTAwM2UgNC4iLCJQcmFjdGljYWwgcmVjaXBlOiAyIGxheWVycyB3aXRoIEg9NTEyLTEwMjQgaXMgdGhlIG1vc3QgcmVsaWFibGUgYmFzZWxpbmUgZm9yIHByZS1UcmFuc2Zvcm1lciBOTFAuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhY2tlZCBMU1RNcyB3ZXJlIHRoZSBkb21pbmFudCBhcmNoaXRlY3R1cmUgZm9yIE5MUCBmcm9tIDIwMTXigJMyMDE4LCBhY2hpZXZpbmcgc3RhdGUtb2YtdGhlLWFydCBvbiBsYW5ndWFnZSBtb2RlbGluZyAoUGVubiBUcmVlYmFuayksIG1hY2hpbmUgdHJhbnNsYXRpb24gKFdNVCksIGFuZCBtYW55IGNsYXNzaWZpY2F0aW9uIHRhc2tzLiBUaGUgMi1sYXllciBCaUxTVE0gd2l0aCA2NTAgaGlkZGVuIHVuaXRzIGZyb20gTWVyaXR5IGV0IGFsLiAoQVdELUxTVE0sIDIwMTcpIHdpdGggd2VpZ2h0IGRyb3BvdXQsIGVtYmVkZGluZyBkcm9wb3V0LCBhbmQgRHJvcENvbm5lY3QgcmVtYWluZWQgY29tcGV0aXRpdmUgd2l0aCBlYXJseSBUcmFuc2Zvcm1lciBtb2RlbHMgb24gbGFuZ3VhZ2UgbW9kZWxpbmcgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Multi-Layer RNNs — Depth in Sequence Models

A single-layer RNN learns temporal patterns from raw input, but deep networks can learn hierarchical representations — low layers detect local structure (n-grams, phonemes, local syntax) while high layers integrate these into global patterns (semantics, long-range dependencies). Stacked RNNs apply this principle to sequences: the output sequence of layer l becomes the input sequence of layer l+1. Depth in sequence models provides the same inductive bias as depth in CNNs: hierarchical feature extraction at multiple scales.

## Why Stack RNN Layers?

In CNNs, depth enables hierarchical feature detection: edges → textures → parts → objects. The same principle applies to sequences: layer 1 might detect character n-grams or local dependency edges, layer 2 integrates these into phrase-level patterns, layer 3 captures sentence-level structure. Empirically, two-layer LSTMs consistently outperform single-layer LSTMs on language modeling and translation tasks, with diminishing returns beyond 4 layers. The key constraint is that each layer doubles the gradient path length, compounding the vanishing gradient problem across both time and depth.

## Two-Layer LSTM from Scratch

In a stacked LSTM, layer 1 receives the input sequence xt and produces output sequence out1t. Layer 2 receives out1t as its input and produces out2t. Between layers, dropout is applied to the output of layer 1 before feeding into layer 2 — this is standard inter-layer dropout. The hidden and cell states of each layer are maintained separately: [(h1, c1), (h2, c2)].

```python
import torch
import torch.nn as nn

class StackedLSTM(nn.Module):
    """Two-layer LSTM: layer-1 output is layer-2 input, with inter-layer dropout."""
    def __init__(self, input_size, hidden_size, dropout_p=0.3):
        super().__init__()
        self.lstm1 = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.lstm2 = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.drop  = nn.Dropout(dropout_p)
        self.hidden_size = hidden_size

    def forward(self, x, states=None):
        if states is None:
            states = [None, None]
        out1, (h1, c1) = self.lstm1(x, states[0])
        out1_dropped = self.drop(out1)              # inter-layer dropout
        out2, (h2, c2) = self.lstm2(out1_dropped, states[1])
        return out2, [(h1, c1), (h2, c2)], out1

torch.manual_seed(42)
B, T, I, H = 4, 20, 8, 32
model = StackedLSTM(input_size=I, hidden_size=H)
x = torch.randn(B, T, I)
out2, states, out1 = model(x)
h1, c1 = states[0]
h2, c2 = states[1]

print('2-layer stacked LSTM:')
print('  Input:    {}'.format(tuple(x.shape)))
print('  L1 out:   {}  -> dropout -> L2 input'.format(tuple(out1.shape)))
print('  L2 out:   {}'.format(tuple(out2.shape)))
print('  h1: {}  h2: {}'.format(tuple(h1.shape), tuple(h2.shape)))
print('  Params: {:,}'.format(sum(p.numel() for p in model.parameters())))
```

## PyTorch num_layers with Variational Dropout

nn.LSTM's num_layers parameter stacks layers automatically. Its dropout parameter applies between layers (not variational — a different mask at each timestep). Variational dropout (Gal & Ghahramani 2016) uses the same dropout mask across all T timesteps, which is more consistent with Bayesian inference and empirically performs better. Implementing variational dropout requires manually masking the input before passing it to the LSTM.

```python
import torch
import torch.nn as nn

class VarDropLSTM(nn.Module):
    """Multi-layer LSTM with variational dropout (same mask across all timesteps)."""
    def __init__(self, input_size, hidden_size, num_layers, dropout_p=0.3):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers=num_layers,
                            dropout=dropout_p if num_layers > 1 else 0.0,
                            batch_first=True)
        self.dropout_p = dropout_p

    def forward(self, x):
        if self.training and self.dropout_p > 0:
            # Sample one mask; apply across all T timesteps (variational)
            mask = (torch.rand(x.size(0), 1, x.size(2)) > self.dropout_p).float()
            mask = mask / (1.0 - self.dropout_p)   # rescale for expected value
            x = x * mask
        return self.lstm(x)

torch.manual_seed(0)
B, T, I, H, L = 8, 25, 16, 64, 3
model = VarDropLSTM(I, H, num_layers=L, dropout_p=0.3)
model.train()
x = torch.randn(B, T, I)
out, (h, c) = model(x)

print('3-layer LSTM with variational dropout (training mode):')
print('  Input:   {}'.format(tuple(x.shape)))
print('  Output:  {}'.format(tuple(out.shape)))
print('  h_n:     {}   <- (num_layers, B, H)'.format(tuple(h.shape)))
print('  Params:  {:,}'.format(sum(p.numel() for p in model.parameters())))
print('  vs standard dropout: different mask each step (not variational)')
```

## Layer-Wise Gradient Analysis

In a stacked LSTM, gradient must flow both backward through time (BPTT) and downward through layers. The bottom layer (closest to input, furthest from loss) receives the weakest gradient — it is compounded by both vanishing across timesteps and attenuation across layers. Measuring gradient norms per layer reveals this effect: top layers typically have 5–20x larger gradient norms than bottom layers in a 4-layer stack.

```python
import torch
import torch.nn as nn

def layer_gradient_norms(num_layers=4, I=8, H=32, T=20):
    """Measure weight gradient norm in each layer of a stacked LSTM."""
    torch.manual_seed(0)
    lstm = nn.LSTM(I, H, num_layers=num_layers, batch_first=True)
    x = torch.randn(4, T, I)
    out, _ = lstm(x)
    out[:, -1, :].sum().backward()

    print('Gradient norms for {}-layer LSTM (loss at final timestep):'.format(num_layers))
    print('{:>7} {:>18} {:>18}'.format('Layer', 'weight_ih norm', 'weight_hh norm'))
    norms_hh = []
    for l in range(num_layers):
        wih = getattr(lstm, 'weight_ih_l{}'.format(l))
        whh = getattr(lstm, 'weight_hh_l{}'.format(l))
        g_ih = wih.grad.norm().item() if wih.grad is not None else 0.0
        g_hh = whh.grad.norm().item() if whh.grad is not None else 0.0
        norms_hh.append(g_hh)
        tag = ' <- input layer' if l == 0 else (' <- output layer' if l == num_layers-1 else '')
        print('{:>7} {:>18.4f} {:>18.4f}{}'.format(l, g_ih, g_hh, tag))
    ratio = norms_hh[-1] / max(norms_hh[0], 1e-20)
    print('Gradient ratio (top / bottom layer): {:.2f}x'.format(ratio))

layer_gradient_norms(num_layers=4)
```

## Residual Connections in Stacked LSTMs

Residual connections — adding the input of a layer to its output — are standard in deep CNNs (ResNets) and Transformers but less common in stacked LSTMs. They provide an additional gradient highway bypassing each layer's computation, helping with training 4+ layer stacks. For residual connections to work in stacked LSTMs, the input dimension and hidden size must match. A linear projection layer is used otherwise. Layer normalization is typically applied after the residual addition.

```python
import torch
import torch.nn as nn

class ResLSTMLayer(nn.Module):
    """Single LSTM layer with residual connection + layer norm (requires d_in == d_hidden)."""
    def __init__(self, hidden_size, dropout_p=0.1):
        super().__init__()
        self.lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.norm = nn.LayerNorm(hidden_size)
        self.drop = nn.Dropout(dropout_p)

    def forward(self, x):
        out, state = self.lstm(x)
        return self.norm(x + self.drop(out)), state   # residual + layer norm

class ResStackedLSTM(nn.Module):
    """N-layer residual stacked LSTM for language modeling."""
    def __init__(self, vocab_size, embed_dim, hidden_size, n_layers):
        super().__init__()
        self.embed   = nn.Embedding(vocab_size, embed_dim)
        self.proj_in = nn.Linear(embed_dim, hidden_size)
        self.layers  = nn.ModuleList([ResLSTMLayer(hidden_size) for _ in range(n_layers)])
        self.fc      = nn.Linear(hidden_size, vocab_size)

    def forward(self, tokens):
        x = self.proj_in(self.embed(tokens))
        for layer in self.layers:
            x, _ = layer(x)
        return self.fc(x)

torch.manual_seed(0)
model = ResStackedLSTM(vocab_size=1000, embed_dim=64, hidden_size=64, n_layers=4)
tokens = torch.randint(0, 1000, (4, 30))
logits = model(tokens)
print('4-layer Residual Stacked LSTM:')
print('  Input tokens: {}'.format(tuple(tokens.shape)))
print('  Output logits: {}  (per-position vocab scores)'.format(tuple(logits.shape)))
print('  Params: {:,}'.format(sum(p.numel() for p in model.parameters())))
```

> **2–4 Layers Usually Sufficient for Stacked LSTMs**: Unlike CNNs which may use 50–200 layers, stacked LSTMs rarely benefit beyond 4 layers. The compounding vanishing gradient (across both time and depth) makes very deep LSTMs hard to train without residual connections and careful initialization. Empirically, 2-layer LSTMs outperform 1-layer by 3–8 perplexity points on language modeling; 3-layer adds another 2–4 points; 4-layer marginal improvement with longer training time. Spend compute budget on wider hidden size or longer training before adding more layers.

## Depth vs Width Trade-off

For a fixed parameter budget, the choice between a single wider layer and multiple narrower layers affects both quality and training dynamics. Wider single-layer models have more direct connections between input and output, while deeper models learn hierarchical features. On language modeling benchmarks, 2-3 layer LSTMs consistently outperform equivalent-parameter 1-layer models, suggesting that depth provides a useful inductive bias beyond raw parameter count.

| Config | Params (I=256) | PTB Perplexity | Train time / epoch | Gradient (bottom layer) | Depth benefit |
| --- | --- | --- | --- | --- | --- |
| 1-layer H=512 | ~1.6M | ~90 | 1x (baseline) | Strong — no depth decay | None — flat features |
| 2-layer H=364 | ~1.6M | ~78 | ~1.8x | Moderate — 1 extra hop | Local + mid-range patterns |
| 3-layer H=297 | ~1.6M | ~74 | ~2.5x | Weak — 2 extra hops | Hierarchical features |
| 4-layer H=256 | ~1.6M | ~73 | ~3.2x | Very weak — needs residual | Marginal over 3-layer |

## Hierarchical Temporal Features

The hierarchical feature hypothesis for stacked LSTMs: lower layers develop sensitivity to local, fine-grained patterns (characters, morphemes, short n-grams, local syntactic dependencies) while higher layers develop sensitivity to global, abstract patterns (phrases, clauses, semantic relationships). This has been empirically confirmed through probing tasks: layer 1 of a 3-layer LSTM best predicts part-of-speech tags; layer 3 best predicts semantic roles and long-range coreference.

- Layer 1 (closest to input): character trigrams, morphological suffixes, local POS patterns.
- Layer 2 (middle): phrase boundaries, local dependency edges, named entity spans.
- Layer 3 (closest to output): clause structure, semantic roles, coreference, topic.
- Inter-layer dropout: prevents layer 2 from overfitting to raw layer-1 activations.
- Residual connections: allow gradient to bypass layers — enables effective depth > 4.
- Practical recipe: 2 layers with H=512-1024 is the most reliable baseline for pre-Transformer NLP.

Stacked LSTMs were the dominant architecture for NLP from 2015–2018, achieving state-of-the-art on language modeling (Penn Treebank), machine translation (WMT), and many classification tasks. The 2-layer BiLSTM with 650 hidden units from Merity et al. (AWD-LSTM, 2017) with weight dropout, embedding dropout, and DropConnect remained competitive with early Transformer models on language modeling benchmarks.

---

