---
title: "Bidirectional RNNs — Forward and Backward Pass Concatenation"
slug: "bidirectional-rnns"
description: "Bidirectional LSTMs run a forward RNN left-to-right and a backward RNN right-to-left, concatenating hidden states at each position to give full-sequence context. Covers manual BiLSTM construction, PyTorch shape handling, pack_padded_sequence for variable-length batching, and BiLSTM for NER token classification."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSB1bmlkaXJlY3Rpb25hbCBSTk4gY29tcHV0ZXMgaHQgZnJvbSB4MSwgeDIsIC4uLiwgeHQg4oCUIGVhY2ggcG9zaXRpb24gc2VlcyBvbmx5IHBhc3QgY29udGV4dC4gTWFueSB0YXNrcyAobmFtZWQgZW50aXR5IHJlY29nbml0aW9uLCBtYWNoaW5lIHRyYW5zbGF0aW9uIGVuY29kaW5nLCBzZW50aW1lbnQgYW5hbHlzaXMpIGJlbmVmaXQgZnJvbSBrbm93aW5nIHRoZSBmdWxsIHNlcXVlbmNlIGF0IGV2ZXJ5IHBvc2l0aW9uLiBCaWRpcmVjdGlvbmFsIFJOTnMgcnVuIHR3byBSTk5zIG9uIHRoZSBzYW1lIHNlcXVlbmNlOiBvbmUgcHJvY2Vzc2VzIGxlZnQgdG8gcmlnaHQgKGZvcndhcmQpLCBvbmUgcmlnaHQgdG8gbGVmdCAoYmFja3dhcmQpLiBUaGVpciBoaWRkZW4gc3RhdGVzIGFyZSBjb25jYXRlbmF0ZWQgYXQgZWFjaCBzdGVwLCBnaXZpbmcgW2jihpJ0LCBo4oaQdF0g4oCUIGEgcmVwcmVzZW50YXRpb24gdGhhdCBoYXMgc2VlbiBib3RoIHBhc3QgYW5kIGZ1dHVyZSBjb250ZXh0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuaWRpcmVjdGlvbmFsIHZzIEJpZGlyZWN0aW9uYWwgQ29udGV4dCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gdGhlIGZvcndhcmQgZGlyZWN0aW9uIGjihpJ0IGRlcGVuZHMgb24geDEuLi54dDsgaW4gdGhlIGJhY2t3YXJkIGRpcmVjdGlvbiBo4oaQdCBkZXBlbmRzIG9uIHhULi4ueHQuIENvbmNhdGVuYXRpbmcgdGhlbSBhdCBlYWNoIHBvc2l0aW9uIGdpdmVzIGFjY2VzcyB0byB0aGUgZnVsbCBjb250ZXh0IHgxLi4ueFQgZnJvbSBib3RoIGVuZHMuIFRoaXMgaXMgY3J1Y2lhbCBmb3IgdGFza3Mgd2hlcmUgdGhlIG1lYW5pbmcgb2YgYSB3b3JkIGRlcGVuZHMgb24gd2hhdCBjb21lcyBhZnRlciBpdDogaW4gXHUwMDI3SSB3ZW50IHRvIHRoZSBiYW5rIHRvIHdpdGhkcmF3IGNhc2hcdTAwMjcgdnMgXHUwMDI3SSBzYXQgYnkgdGhlIHJpdmVyIGJhbmtcdTAwMjcsIHRoZSB3b3JkIFx1MDAyN2JhbmtcdTAwMjcgY2Fubm90IGJlIGNsYXNzaWZpZWQgd2l0aG91dCBzZWVpbmcgZG93bnN0cmVhbSBjb250ZXh0LiBCaWRpcmVjdGlvbmFsIHByb2Nlc3NpbmcgbWFrZXMgdGhpcyBpbmZvcm1hdGlvbiBhdmFpbGFibGUgYXQgZXZlcnkgcG9zaXRpb24gc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWFudWFsIEJpTFNUTSDigJQgRm9yd2FyZCBhbmQgQmFja3dhcmQgQ29uY2F0ZW5hdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW1wbGVtZW50aW5nIEJpTFNUTSBtYW51YWxseSBjbGFyaWZpZXMgZXhhY3RseSB3aGF0IGNvbmNhdGVuYXRpb24gaGFwcGVucyB3aGVyZS4gVGhlIGZvcndhcmQgTFNUTSBwcm9jZXNzZXMgdGhlIHNlcXVlbmNlIG5vcm1hbGx5LiBUaGUgYmFja3dhcmQgTFNUTSBwcm9jZXNzZXMgdGhlIHRpbWUtcmV2ZXJzZWQgc2VxdWVuY2UsIHRoZW4gaXRzIG91dHB1dHMgYXJlIHJlLWFsaWduZWQgdG8gdGhlIG9yaWdpbmFsIHRpbWUgYXhpcyBieSByZXZlcnNpbmcgYWdhaW4uIEF0IGVhY2ggcG9zaXRpb24gdCwgdGhlIG91dHB1dCBpcyBbZndkX291dHQsIGJ3ZF9vdXR0XSDiiIgg4oSdwrLhtLQuIFRoZSBmaW5hbCBoaWRkZW4gc3RhdGUgZm9yIGEgY2xhc3NpZmllciBpcyB0eXBpY2FsbHkgW2jihpJULCBo4oaQMV0g4oCUIHRoZSBmb3J3YXJkIGZpbmFsIHN0ZXAgYW5kIHRoZSBiYWNrd2FyZCBmaW5hbCBzdGVwICh3aGljaCBwcm9jZXNzZWQgeDEpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgbWFudWFsX2JpbHN0bSh4LCBpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSwgc2VlZD0wKTpcbiAgICBcIlwiXCJSdW4gZm9yd2FyZCArIGJhY2t3YXJkIExTVE1zIGFuZCBjb25jYXRlbmF0ZSBvdXRwdXRzIGF0IGVhY2ggc3RlcC5cIlwiXCJcbiAgICB0b3JjaC5tYW51YWxfc2VlZChzZWVkKVxuICAgIGZ3ZCA9IG5uLkxTVE0oaW5wdXRfc2l6ZSwgaGlkZGVuX3NpemUsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgYndkID0gbm4uTFNUTShpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcblxuICAgIGZ3ZF9vdXQsIChmd2RfaCwgXykgPSBmd2QoeCkgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIFQsIEgpIGxlZnQtdG8tcmlnaHRcbiAgICB4X3JldiA9IHRvcmNoLmZsaXAoeCwgZGltcz1bMV0pICAgICAgICAgICAgICAgICAgICAjIHJldmVyc2Ugc2VxdWVuY2VcbiAgICBid2Rfb3V0X3JldiwgKGJ3ZF9oLCBfKSA9IGJ3ZCh4X3JldikgICAgICAgICAgICAgICAjIChCLCBULCBIKSByaWdodC10by1sZWZ0XG4gICAgYndkX291dCA9IHRvcmNoLmZsaXAoYndkX291dF9yZXYsIGRpbXM9WzFdKSAgICAgICAgICMgcmUtYWxpZ24gdG8gb3JpZ2luYWwgdGltZSBheGlzXG5cbiAgICBjb21iaW5lZCA9IHRvcmNoLmNhdChbZndkX291dCwgYndkX291dF0sIGRpbT0yKSAgICAjIChCLCBULCAySClcbiAgICBmaW5hbF9oICA9IHRvcmNoLmNhdChbZndkX2gsIGJ3ZF9oXSwgZGltPTIpICAgICAgICAjICgxLCBCLCAySClcbiAgICByZXR1cm4gY29tYmluZWQsIGZpbmFsX2hcblxuQiwgVCwgSSwgSCA9IDQsIDEwLCA4LCAxNlxudG9yY2gubWFudWFsX3NlZWQoOTkpXG54ID0gdG9yY2gucmFuZG4oQiwgVCwgSSlcbm91dCwgaCA9IG1hbnVhbF9iaWxzdG0oeCwgSSwgSClcblxucHJpbnQoXHUwMDI3TWFudWFsIEJpTFNUTTpcdTAwMjcpXG5wcmludChcdTAwMjcgIElucHV0OiAgICAgICAge31cdTAwMjcuZm9ybWF0KHR1cGxlKHguc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgT3V0cHV0OiAgICAgICB7fSAgKGZ3ZCtid2QgY29udGV4dCBhdCBlYWNoIHBvc2l0aW9uKVx1MDAyNy5mb3JtYXQodHVwbGUob3V0LnNoYXBlKSkpXG5wcmludChcdTAwMjcgIEZpbmFsIGhpZGRlbjoge31cdTAwMjcuZm9ybWF0KHR1cGxlKGguc2hhcGUpKSlcbnByaW50KClcbnByaW50KFx1MDAyNyAgdD0wOiAgIGZvcndhcmQgaGFzIHNlZW4geFswXSBvbmx5OyBiYWNrd2FyZCBoYXMgc2VlbiBmdWxsIHNlcXVlbmNlXHUwMDI3KVxucHJpbnQoXHUwMDI3ICB0PVQvMjogYm90aCBkaXJlY3Rpb25zIGhhdmUgcGFydGlhbCBjb250ZXh0IC0tIHJpY2hlc3QgcmVwcmVzZW50YXRpb25cdTAwMjcpXG5wcmludChcdTAwMjcgIHQ9VC0xOiBmb3J3YXJkIGhhcyBzZWVuIGZ1bGwgc2VxdWVuY2U7IGJhY2t3YXJkIGhhcyBzZWVuIHhbVC0xXSBvbmx5XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlB5VG9yY2ggQnVpbHQtaW4g4oCUIFNoYXBlIEd1aWRlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQeVRvcmNoXHUwMDI3cyBubi5MU1RNIHdpdGggYmlkaXJlY3Rpb25hbD1UcnVlIGhhbmRsZXMgdGhlIGZvcndhcmQgYW5kIGJhY2t3YXJkIHBhc3NlcyBpbnRlcm5hbGx5LiBUaGUgb3V0cHV0IHRlbnNvciBoYXMgc2hhcGUgKEIsIFQsIDIqSCkgYW5kIGhfbiBoYXMgc2hhcGUgKDIqbnVtX2xheWVycywgQiwgSCkgd2hlcmUgZGlyZWN0aW9ucyBhcmUgaW50ZXJsZWF2ZWQ6IGhfblswXSBpcyB0aGUgZm9yd2FyZCBmaW5hbCBoaWRkZW4sIGhfblsxXSBpcyB0aGUgYmFja3dhcmQgZmluYWwgaGlkZGVuLiBVbmRlcnN0YW5kaW5nIHRoZXNlIHNoYXBlIGNvbnZlbnRpb25zIHByZXZlbnRzIHRoZSBjb21tb24gYnVnIG9mIGFjY2lkZW50YWxseSB1c2luZyBvbmx5IHRoZSBmb3J3YXJkIG9yIG9ubHkgdGhlIGJhY2t3YXJkIGhpZGRlbiBmb3IgZG93bnN0cmVhbSB0YXNrcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIFQsIEksIEggPSA0LCAxNSwgOCwgMTZcblxuYmlsc3RtID0gbm4uTFNUTShpbnB1dF9zaXplPUksIGhpZGRlbl9zaXplPUgsIG51bV9sYXllcnM9MSxcbiAgICAgICAgICAgICAgICAgYmlkaXJlY3Rpb25hbD1UcnVlLCBiYXRjaF9maXJzdD1UcnVlKVxuXG54ID0gdG9yY2gucmFuZG4oQiwgVCwgSSlcbm91dCwgKGhfbiwgY19uKSA9IGJpbHN0bSh4KVxuXG5wcmludChcdTAwMjdTaGFwZSBndWlkZSBmb3Igbm4uTFNUTShiaWRpcmVjdGlvbmFsPVRydWUsIGJhdGNoX2ZpcnN0PVRydWUpOlx1MDAyNylcbnByaW50KFx1MDAyNyAgeCAgIHt9XHUwMDI3LmZvcm1hdCh0dXBsZSh4LnNoYXBlKSkpXG5wcmludChcdTAwMjcgIG91dCB7fSAgXHUwMDNjLSAyKkggcGVyIHBvc2l0aW9uXHUwMDI3LmZvcm1hdCh0dXBsZShvdXQuc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgaF9uIHt9ICBcdTAwM2MtIFtmd2RfbGFzdCwgYndkX2xhc3RdIHN0YWNrZWQgb24gZGltIDBcdTAwMjcuZm9ybWF0KHR1cGxlKGhfbi5zaGFwZSkpKVxucHJpbnQoXHUwMDI3ICBjX24ge31cdTAwMjcuZm9ybWF0KHR1cGxlKGNfbi5zaGFwZSkpKVxucHJpbnQoKVxuaF9md2QgPSBoX25bMF0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIChCLCBIKSBsYXN0IGZvcndhcmQgaGlkZGVuXG5oX2J3ZCA9IGhfblsxXSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKEIsIEgpIGxhc3QgYmFja3dhcmQgaGlkZGVuXG5oX2NhdCA9IHRvcmNoLmNhdChbaF9md2QsIGhfYndkXSwgZGltPTEpICAgIyAoQiwgMkgpIGZvciBjbGFzc2lmaWVyXG5wcmludChcdTAwMjcgIGhfZndkIHt9ICBcdTAwM2MtIGZpbmFsIGZvcndhcmQgaGlkZGVuIChyZWFkcyBmcm9tIHhbVC0xXSlcdTAwMjcuZm9ybWF0KHR1cGxlKGhfZndkLnNoYXBlKSkpXG5wcmludChcdTAwMjcgIGhfYndkIHt9ICBcdTAwM2MtIGZpbmFsIGJhY2t3YXJkIGhpZGRlbiAocmVhZHMgZnJvbSB4WzBdKVx1MDAyNy5mb3JtYXQodHVwbGUoaF9id2Quc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgaF9jYXQge30gICBcdTAwM2MtIGNvbmNhdGVuYXRlZCBmb3Igc2VudGVuY2UtbGV2ZWwgY2xhc3NpZmllclx1MDAyNy5mb3JtYXQodHVwbGUoaF9jYXQuc2hhcGUpKSlcbm91dF9md2QgPSBvdXRbOiwgOiwgOkhdXG5vdXRfYndkID0gb3V0WzosIDosIEg6XVxucHJpbnQoXHUwMDI3ICBvdXRfZndkIHt9ICBwZXItc3RlcCBmb3J3YXJkIG91dHB1dHNcdTAwMjcuZm9ybWF0KHR1cGxlKG91dF9md2Quc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgb3V0X2J3ZCB7fSAgcGVyLXN0ZXAgYmFja3dhcmQgb3V0cHV0c1x1MDAyNy5mb3JtYXQodHVwbGUob3V0X2J3ZC5zaGFwZSkpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmljaWVudCBCYXRjaGluZyB3aXRoIHBhY2tfcGFkZGVkX3NlcXVlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWYXJpYWJsZS1sZW5ndGggc2VxdWVuY2VzIGluIGEgYmF0Y2ggbXVzdCBiZSBwYWRkZWQgdG8gdGhlIHNhbWUgbGVuZ3RoLCBjcmVhdGluZyB3YXN0ZWQgY29tcHV0YXRpb24gb24gcGFkZGluZyB0b2tlbnMuIFB5VG9yY2hcdTAwMjdzIHBhY2tfcGFkZGVkX3NlcXVlbmNlIHJlbW92ZXMgcGFkZGluZyBiZWZvcmUgdGhlIExTVE0sIHBhc3Npbmcgb25seSByZWFsIHRva2VucyB0aHJvdWdoIHRoZSByZWN1cnJlbnQgY29tcHV0YXRpb24uIFRoZSBMU1RNIHByb2Nlc3NlcyBhIGNvbXByZXNzZWQgcmVwcmVzZW50YXRpb24gYW5kIHBhZF9wYWNrZWRfc2VxdWVuY2UgcmVzdG9yZXMgdGhlIHBhZGRlZCBmb3JtIGFmdGVyd2FyZC4gRm9yIGJpZGlyZWN0aW9uYWwgTFNUTXMgd2l0aCB2YXJpYWJsZS1sZW5ndGggc2VxdWVuY2VzLCB0aGlzIG9wdGltaXphdGlvbiBpcyBlc3BlY2lhbGx5IGltcG9ydGFudCBzaW5jZSBib3RoIGRpcmVjdGlvbnMgcHJvY2VzcyB0aGUgc2FtZSBwYWRkaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaC5ubi51dGlscy5ybm4gaW1wb3J0IHBhY2tfcGFkZGVkX3NlcXVlbmNlLCBwYWRfcGFja2VkX3NlcXVlbmNlLCBwYWRfc2VxdWVuY2VcblxuZGVmIGJhdGNoX3ZhcmlhYmxlX2xlbmd0aChsZW5ndGhzLCBpbnB1dF9zaXplPTQsIGhpZGRlbl9zaXplPTE2KTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZCgxKVxuICAgIHNlcXMgPSBbdG9yY2gucmFuZG4obCwgaW5wdXRfc2l6ZSkgZm9yIGwgaW4gbGVuZ3Roc11cbiAgICBiaWxzdG0gPSBubi5MU1RNKGlucHV0X3NpemUsIGhpZGRlbl9zaXplLCBiaWRpcmVjdGlvbmFsPVRydWUsIGJhdGNoX2ZpcnN0PVRydWUpXG5cbiAgICBzZXFzX3NvcnRlZCA9IHNvcnRlZChzZXFzLCBrZXk9bGVuLCByZXZlcnNlPVRydWUpXG4gICAgbGVuX3NvcnRlZCAgPSBzb3J0ZWQobGVuZ3RocywgcmV2ZXJzZT1UcnVlKVxuICAgIGxlbl90ZW5zb3IgID0gdG9yY2gudGVuc29yKGxlbl9zb3J0ZWQpXG5cbiAgICBwYWRkZWQgPSBwYWRfc2VxdWVuY2Uoc2Vxc19zb3J0ZWQsIGJhdGNoX2ZpcnN0PVRydWUsIHBhZGRpbmdfdmFsdWU9MC4wKVxuICAgIHdhc3RlZCA9IHBhZGRlZC5udW1lbCgpIC0gc3VtKGwgKiBpbnB1dF9zaXplIGZvciBsIGluIGxlbl9zb3J0ZWQpXG4gICAgcHJpbnQoXHUwMDI3UGFkZGVkIGJhdGNoOiB7fSAgKHt9IHdhc3RlZCBlbGVtZW50cylcdTAwMjcuZm9ybWF0KHR1cGxlKHBhZGRlZC5zaGFwZSksIHdhc3RlZCkpXG5cbiAgICBwYWNrZWQgPSBwYWNrX3BhZGRlZF9zZXF1ZW5jZShwYWRkZWQsIGxlbl90ZW5zb3IsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgb3V0X3BhY2tlZCwgKGhfbiwgXykgPSBiaWxzdG0ocGFja2VkKVxuICAgIHByaW50KFx1MDAyN1BhY2tlZCBkYXRhOiAge30gIChubyB3YXN0ZWQgY29tcHV0YXRpb24pXHUwMDI3LmZvcm1hdCh0dXBsZShwYWNrZWQuZGF0YS5zaGFwZSkpKVxuXG4gICAgb3V0X3BhZCwgb3V0X2xlbnMgPSBwYWRfcGFja2VkX3NlcXVlbmNlKG91dF9wYWNrZWQsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgcHJpbnQoXHUwMDI3VW5wYWNrZWQgb3V0OiB7fSAgYWN0dWFsIGxlbmd0aHM6IHt9XHUwMDI3LmZvcm1hdChcbiAgICAgICAgdHVwbGUob3V0X3BhZC5zaGFwZSksIG91dF9sZW5zLnRvbGlzdCgpKSlcbiAgICBwcmludChcdTAwMjdoX24gc2hhcGU6ICAgIHt9ICBcdTAwM2MtIFtmd2RfZmluYWwsIGJ3ZF9maW5hbF0geCBiYXRjaFx1MDAyNy5mb3JtYXQodHVwbGUoaF9uLnNoYXBlKSkpXG5cbmJhdGNoX3ZhcmlhYmxlX2xlbmd0aChsZW5ndGhzPVsxMiwgOCwgNSwgM10pIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2VxdWVuY2UgTGFiZWxpbmcg4oCUIEJpTFNUTSBmb3IgTkVSIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOYW1lZCBlbnRpdHkgcmVjb2duaXRpb24gKE5FUikgcmVxdWlyZXMgdGFnZ2luZyBlYWNoIHRva2VuIHdpdGggYSBsYWJlbCAoZS5nLiBCLVBFUiwgSS1PUkcsIE8gdXNpbmcgQklPIG5vdGF0aW9uKS4gQmlMU1RNIGlzIHRoZSBjYW5vbmljYWwgcHJlLVRyYW5zZm9ybWVyIGFyY2hpdGVjdHVyZSBmb3IgTkVSOiBlYWNoIHRva2VuXHUwMDI3cyByZXByZXNlbnRhdGlvbiBiZW5lZml0cyBmcm9tIGJvdGggbGVmdCBhbmQgcmlnaHQgY29udGV4dC4gVHdvIHN0YWNrZWQgQmlMU1RNIGxheWVycyBhcmUgc3RhbmRhcmQg4oCUIHRoZSBmaXJzdCBjYXB0dXJlcyBsb2NhbCBzeW50YWN0aWMgcGF0dGVybnMsIHRoZSBzZWNvbmQgaW50ZWdyYXRlcyB0aGVtIGludG8gaGlnaGVyLWxldmVsIGVudGl0eSByZXByZXNlbnRhdGlvbnMuIEEgbGluZWFyIGNsYXNzaWZpZXIgb24gdG9wIG9mIGVhY2ggQmlMU1RNIG91dHB1dCBwb3NpdGlvbiBwcm9kdWNlcyBwZXItdG9rZW4gbG9naXRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBCaUxTVE1ORVIobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJCaWRpcmVjdGlvbmFsIDItbGF5ZXIgTFNUTSBmb3IgdG9rZW4tbGV2ZWwgTkVSIChzZXF1ZW5jZSBsYWJlbGluZykuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHZvY2FiX3NpemUsIGVtYmVkX2RpbSwgaGlkZGVuX3NpemUsIG5fdGFncywgcGFkX2lkeD0wKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW1iZWQgID0gbm4uRW1iZWRkaW5nKHZvY2FiX3NpemUsIGVtYmVkX2RpbSwgcGFkZGluZ19pZHg9cGFkX2lkeClcbiAgICAgICAgc2VsZi5iaWxzdG0gPSBubi5MU1RNKGVtYmVkX2RpbSwgaGlkZGVuX3NpemUsIG51bV9sYXllcnM9MixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJpZGlyZWN0aW9uYWw9VHJ1ZSwgYmF0Y2hfZmlyc3Q9VHJ1ZSwgZHJvcG91dD0wLjMpXG4gICAgICAgIHNlbGYuZHJvcCAgID0gbm4uRHJvcG91dCgwLjUpXG4gICAgICAgIHNlbGYuZmMgICAgID0gbm4uTGluZWFyKDIgKiBoaWRkZW5fc2l6ZSwgbl90YWdzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgdG9rZW5faWRzKTpcbiAgICAgICAgZW1iICAgID0gc2VsZi5kcm9wKHNlbGYuZW1iZWQodG9rZW5faWRzKSkgICAgIyAoQiwgVCwgRSlcbiAgICAgICAgb3V0LCBfID0gc2VsZi5iaWxzdG0oZW1iKSAgICAgICAgICAgICAgICAgICAgIyAoQiwgVCwgMkgpXG4gICAgICAgIG91dCAgICA9IHNlbGYuZHJvcChvdXQpXG4gICAgICAgIHJldHVybiBzZWxmLmZjKG91dCkgICAgICAgICAgICAgICAgICAgICAgICAgICAjIChCLCBULCBuX3RhZ3MpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuViwgRSwgSCwgVEFHUyA9IDUwMDAsIDY0LCAxMjgsIDkgICAjIDkgQklPIHRhZ3M6IE8gKyBCL0kgZm9yIDQgZW50aXR5IHR5cGVzXG5tb2RlbCA9IEJpTFNUTU5FUihWLCBFLCBILCBUQUdTKVxudG9rZW5zID0gdG9yY2gucmFuZGludCgxLCBWLCAoOCwgMjApKSAgICAgICMgYmF0Y2g9OCwgc2VxX2xlbj0yMFxubGFiZWxzID0gdG9yY2gucmFuZGludCgwLCBUQUdTLCAoOCwgMjApKVxuXG5sb2dpdHMgPSBtb2RlbCh0b2tlbnMpXG5sb3NzID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpKGxvZ2l0cy52aWV3KC0xLCBUQUdTKSwgbGFiZWxzLnZpZXcoLTEpKVxucHJpbnQoXHUwMDI3QmlMU1RNLU5FUiAoMi1sYXllciwgYmlkaXJlY3Rpb25hbCk6XHUwMDI3KVxucHJpbnQoXHUwMDI3ICBJbnB1dCB0b2tlbnM6IHt9XHUwMDI3LmZvcm1hdCh0dXBsZSh0b2tlbnMuc2hhcGUpKSlcbnByaW50KFx1MDAyNyAgT3V0cHV0IGxvZ2l0czoge30gIChwZXItdG9rZW4gdGFnIHNjb3JlcylcdTAwMjcuZm9ybWF0KHR1cGxlKGxvZ2l0cy5zaGFwZSkpKVxucHJpbnQoXHUwMDI3ICBMb3NzOiB7Oi40Zn1cdTAwMjcuZm9ybWF0KGxvc3MuaXRlbSgpKSlcbnByaW50KFx1MDAyNyAgUGFyYW1zOiB7Oix9XHUwMDI3LmZvcm1hdChzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSkpKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQmlSTk4gQ2Fubm90IEJlIFVzZWQgQXV0b3JlZ3Jlc3NpdmVseSIsImNvbnRlbnQiOiJCaWRpcmVjdGlvbmFsIFJOTnMgcmVxdWlyZSB0aGUgZnVsbCBpbnB1dCBzZXF1ZW5jZSB0byBiZSBhdmFpbGFibGUgYmVmb3JlIHByb2Nlc3Npbmcg4oCUIHRoZXkgY2Fubm90IGdlbmVyYXRlIG91dHB1dCB0b2tlbnMgb25lIGF0IGEgdGltZSBiZWNhdXNlIHRoZSBiYWNrd2FyZCBwYXNzIGhhcyBub3QgcnVuIHlldC4gVGhpcyBtYWtlcyB0aGVtIHVuc3VpdGFibGUgZm9yIGF1dG9yZWdyZXNzaXZlIGdlbmVyYXRpb24gKGxhbmd1YWdlIG1vZGVsaW5nLCBtYWNoaW5lIHRyYW5zbGF0aW9uIGRlY29kaW5nKS4gVGhleSBhcmUgYXBwcm9wcmlhdGUgb25seSBmb3IgZW5jb2RpbmcgdGFza3Mgd2hlcmUgdGhlIGZ1bGwgaW5wdXQgaXMga25vd246IGNsYXNzaWZpY2F0aW9uLCB0YWdnaW5nLCBuYW1lZCBlbnRpdHkgcmVjb2duaXRpb24sIG9yIGFzIHRoZSBlbmNvZGVyIGluIGVuY29kZXItZGVjb2RlciBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuaWRpcmVjdGlvbmFsIHZzIEJpZGlyZWN0aW9uYWwgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNob2ljZSBiZXR3ZWVuIHVuaWRpcmVjdGlvbmFsIGFuZCBiaWRpcmVjdGlvbmFsIGRlcGVuZHMgcHJpbWFyaWx5IG9uIHdoZXRoZXIgZnV0dXJlIGNvbnRleHQgaXMgYXZhaWxhYmxlIGF0IGluZmVyZW5jZSB0aW1lLiBGb3Igc2VxdWVuY2UgZW5jb2RpbmcgdGFza3MgKGNsYXNzaWZpY2F0aW9uLCB0YWdnaW5nLCB0cmFuc2xhdGlvbiBlbmNvZGluZykgYmlkaXJlY3Rpb25hbCBpcyBhbG1vc3QgYWx3YXlzIGJldHRlci4gRm9yIGdlbmVyYXRpb24gdGFza3MgaXQgaXMgaW1wb3NzaWJsZS4gTWVtb3J5IGRvdWJsZXMgYmVjYXVzZSB0aGVyZSBhcmUgdHdvIHNldHMgb2YgaGlkZGVuIHN0YXRlcywgYW5kIHRyYWluaW5nIGlzIHNsb3dlciBidXQgZ2VuZXJhbGx5IHByb2R1Y2VzIHNpZ25pZmljYW50bHkgYmV0dGVyIHJlcHJlc2VudGF0aW9ucyBmb3IgZml4ZWQtaW5wdXQgdGFza3MuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiVW5pZGlyZWN0aW9uYWwiLCJCaWRpcmVjdGlvbmFsIl0sInJvd3MiOltbIkNvbnRleHQgYXQgdCIsIngxLi4ueHQgKGNhdXNhbCBvbmx5KSIsIngxLi4ueFQgKGZ1bGwgc2VxdWVuY2UpIl0sWyJBdXRvcmVncmVzc2l2ZSBnZW5lcmF0aW9uIiwiWWVzIOKAlCBvdXRwdXRzIHRva2VuIGJ5IHRva2VuIiwiTm8g4oCUIG5lZWRzIGZ1bGwgaW5wdXQgZmlyc3QiXSxbIk1lbW9yeSAoSD0xMjgpIiwiMTI4IHBlciBzdGVwIiwiMjU2IHBlciBzdGVwICgyeCkiXSxbIlRyYWluaW5nIHNwZWVkIiwiRmFzdGVyICgxIExTVE0gcGFzcykiLCJ+Mnggc2xvd2VyICgyIExTVE0gcGFzc2VzKSJdLFsiTkVSIC8gdGFnZ2luZyIsIldlYWtlciDigJQgbm8gcmlnaHQgY29udGV4dCIsIlN0YW5kYXJkIGNob2ljZSDigJQgYm90aCBjb250ZXh0cyJdLFsiTGFuZ3VhZ2UgbW9kZWwiLCJTdGFuZGFyZCDigJQgY2F1c2FsIGNvbnN0cmFpbnQiLCJOb3QgYXBwbGljYWJsZSBmb3IgZ2VuZXJhdGlvbiJdLFsiRW5jb2RlciBpbiBzZXEyc2VxIiwiQ29tbW9uIiwiUHJlZmVycmVkIOKAlCByaWNoZXIgc291cmNlIHJlcHIiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFwcGxpY2F0aW9ucyBhbmQgQ29tbW9uIFBhdHRlcm5zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCaUxTVE0gaXMgdXNlZCBhcyB0aGUgZW5jb2RlciBpbiBtYW55IE5MUCBhcmNoaXRlY3R1cmVzOiBCaUxTVE0tQ1JGIGZvciBORVIgKGFkZCBhIENvbmRpdGlvbmFsIFJhbmRvbSBGaWVsZCBvbiB0b3Agb2YgQmlMU1RNIGxvZ2l0cyB0byBlbmZvcmNlIGxhYmVsIGNvbnNpc3RlbmN5KSwgQmlMU1RNICsgYXR0ZW50aW9uIGZvciB0ZXh0IGNsYXNzaWZpY2F0aW9uLCBhbmQgQmlMU1RNIGVuY29kZXIgKyB1bmlkaXJlY3Rpb25hbCBMU1RNIGRlY29kZXIgZm9yIHNlcXVlbmNlLXRvLXNlcXVlbmNlIHRhc2tzIChtYWNoaW5lIHRyYW5zbGF0aW9uIGJlZm9yZSBUcmFuc2Zvcm1lcnMpLiBCRVJUIHByZS10cmFpbnMgYmlkaXJlY3Rpb25hbCBUcmFuc2Zvcm1lciBlbmNvZGVycyByYXRoZXIgdGhhbiBCaUxTVE1zLCBidXQgdGhlIGNvcmUgaWRlYSDigJQgZnVsbCBjb250ZXh0IGF0IGV2ZXJ5IHBvc2l0aW9uIOKAlCBpcyB0aGUgc2FtZS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJpTFNUTS1DUkY6IGdvbGQgc3RhbmRhcmQgcHJlLVRyYW5zZm9ybWVyIE5FUiDigJQgQmlMU1RNIGZlYXR1cmVzICsgVml0ZXJiaSBkZWNvZGluZy4iLCJCaUxTVE0gZW5jb2RlciArIHVuaWRpcmVjdGlvbmFsIGRlY29kZXI6IHN0YW5kYXJkIHNlcTJzZXEgZm9yIHRyYW5zbGF0aW9uIChCYWhkYW5hdSAyMDE1KS4iLCJEZWVwU3BlZWNoOiBzdGFja2VkIEJpTFNUTXMgZm9yIGFjb3VzdGljIG1vZGVsaW5nIGluIHNwZWVjaCByZWNvZ25pdGlvbi4iLCJFTE1vOiBkZWVwIEJpTFNUTSBsYW5ndWFnZSBtb2RlbCB1c2VkIGFzIGNvbnRleHR1YWwgd29yZCBlbWJlZGRpbmdzIChQZXRlcnMgZXQgYWwuIDIwMTgpLiIsIlNlbnRpbWVudCBhbmFseXNpczogQmlMU1RNIG92ZXIgc2VudGVuY2Ugd2l0aCBtYXgtcG9vbCBvciBhdHRlbnRpb24gb3ZlciBhbGwgcG9zaXRpb25zLiIsIkRvY3VtZW50IGVuY29kaW5nOiBoaWVyYXJjaGljYWwgQmlMU1RNIOKAlCB3b3JkLWxldmVsIHRoZW4gc2VudGVuY2UtbGV2ZWwuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmlkaXJlY3Rpb25hbCBwcm9jZXNzaW5nIGlzIG9uZSBvZiB0aGUgbW9zdCByZWxpYWJsZSBpbXByb3ZlbWVudHMgYXZhaWxhYmxlIGZvciBhbnkgZml4ZWQtaW5wdXQgc2VxdWVuY2UgdGFzay4gVGhlIGVuZ2luZWVyaW5nIGNvc3QgaXMgbWluaW1hbCAob25lIGZsYWcgaW4gUHlUb3JjaCwgY2FyZWZ1bCBzaGFwZSBoYW5kbGluZyBmb3IgaF9uKSB3aGlsZSB0aGUgYWNjdXJhY3kgZ2FpbiBmcm9tIGZ1bGwgY29udGV4dCBjYW4gYmUgc3Vic3RhbnRpYWwuIE1vZGVybiBUcmFuc2Zvcm1lciBlbmNvZGVycyBhcmUgYWxzbyBiaWRpcmVjdGlvbmFsIGJ5IG5hdHVyZSDigJQgQkVSVFx1MDAyN3Mgc2VsZi1hdHRlbnRpb24gYXR0ZW5kcyB0byBhbGwgcG9zaXRpb25zIHNpbXVsdGFuZW91c2x5IOKAlCBtYWtpbmcgQmlMU1RNIHVuZGVyc3RhbmRpbmcgZGlyZWN0bHkgcmVsZXZhbnQgdG8gaW50ZXJwcmV0aW5nIHdoeSBlbmNvZGVyLW9ubHkgVHJhbnNmb3JtZXJzIHdvcmsgc28gd2VsbC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Bidirectional RNNs — Forward and Backward Pass Concatenation

A unidirectional RNN computes ht from x1, x2, ..., xt — each position sees only past context. Many tasks (named entity recognition, machine translation encoding, sentiment analysis) benefit from knowing the full sequence at every position. Bidirectional RNNs run two RNNs on the same sequence: one processes left to right (forward), one right to left (backward). Their hidden states are concatenated at each step, giving [h→t, h←t] — a representation that has seen both past and future context.

## Unidirectional vs Bidirectional Context

In the forward direction h→t depends on x1...xt; in the backward direction h←t depends on xT...xt. Concatenating them at each position gives access to the full context x1...xT from both ends. This is crucial for tasks where the meaning of a word depends on what comes after it: in 'I went to the bank to withdraw cash' vs 'I sat by the river bank', the word 'bank' cannot be classified without seeing downstream context. Bidirectional processing makes this information available at every position simultaneously.

## Manual BiLSTM — Forward and Backward Concatenation

Implementing BiLSTM manually clarifies exactly what concatenation happens where. The forward LSTM processes the sequence normally. The backward LSTM processes the time-reversed sequence, then its outputs are re-aligned to the original time axis by reversing again. At each position t, the output is [fwd_outt, bwd_outt] ∈ ℝ²ᴴ. The final hidden state for a classifier is typically [h→T, h←1] — the forward final step and the backward final step (which processed x1).

```python
import torch
import torch.nn as nn

def manual_bilstm(x, input_size, hidden_size, seed=0):
    """Run forward + backward LSTMs and concatenate outputs at each step."""
    torch.manual_seed(seed)
    fwd = nn.LSTM(input_size, hidden_size, batch_first=True)
    bwd = nn.LSTM(input_size, hidden_size, batch_first=True)

    fwd_out, (fwd_h, _) = fwd(x)                       # (B, T, H) left-to-right
    x_rev = torch.flip(x, dims=[1])                    # reverse sequence
    bwd_out_rev, (bwd_h, _) = bwd(x_rev)               # (B, T, H) right-to-left
    bwd_out = torch.flip(bwd_out_rev, dims=[1])         # re-align to original time axis

    combined = torch.cat([fwd_out, bwd_out], dim=2)    # (B, T, 2H)
    final_h  = torch.cat([fwd_h, bwd_h], dim=2)        # (1, B, 2H)
    return combined, final_h

B, T, I, H = 4, 10, 8, 16
torch.manual_seed(99)
x = torch.randn(B, T, I)
out, h = manual_bilstm(x, I, H)

print('Manual BiLSTM:')
print('  Input:        {}'.format(tuple(x.shape)))
print('  Output:       {}  (fwd+bwd context at each position)'.format(tuple(out.shape)))
print('  Final hidden: {}'.format(tuple(h.shape)))
print()
print('  t=0:   forward has seen x[0] only; backward has seen full sequence')
print('  t=T/2: both directions have partial context -- richest representation')
print('  t=T-1: forward has seen full sequence; backward has seen x[T-1] only')
```

## PyTorch Built-in — Shape Guide

PyTorch's nn.LSTM with bidirectional=True handles the forward and backward passes internally. The output tensor has shape (B, T, 2*H) and h_n has shape (2*num_layers, B, H) where directions are interleaved: h_n[0] is the forward final hidden, h_n[1] is the backward final hidden. Understanding these shape conventions prevents the common bug of accidentally using only the forward or only the backward hidden for downstream tasks.

```python
import torch
import torch.nn as nn

torch.manual_seed(0)
B, T, I, H = 4, 15, 8, 16

bilstm = nn.LSTM(input_size=I, hidden_size=H, num_layers=1,
                 bidirectional=True, batch_first=True)

x = torch.randn(B, T, I)
out, (h_n, c_n) = bilstm(x)

print('Shape guide for nn.LSTM(bidirectional=True, batch_first=True):')
print('  x   {}'.format(tuple(x.shape)))
print('  out {}  <- 2*H per position'.format(tuple(out.shape)))
print('  h_n {}  <- [fwd_last, bwd_last] stacked on dim 0'.format(tuple(h_n.shape)))
print('  c_n {}'.format(tuple(c_n.shape)))
print()
h_fwd = h_n[0]                              # (B, H) last forward hidden
h_bwd = h_n[1]                              # (B, H) last backward hidden
h_cat = torch.cat([h_fwd, h_bwd], dim=1)   # (B, 2H) for classifier
print('  h_fwd {}  <- final forward hidden (reads from x[T-1])'.format(tuple(h_fwd.shape)))
print('  h_bwd {}  <- final backward hidden (reads from x[0])'.format(tuple(h_bwd.shape)))
print('  h_cat {}   <- concatenated for sentence-level classifier'.format(tuple(h_cat.shape)))
out_fwd = out[:, :, :H]
out_bwd = out[:, :, H:]
print('  out_fwd {}  per-step forward outputs'.format(tuple(out_fwd.shape)))
print('  out_bwd {}  per-step backward outputs'.format(tuple(out_bwd.shape)))
```

## Efficient Batching with pack_padded_sequence

Variable-length sequences in a batch must be padded to the same length, creating wasted computation on padding tokens. PyTorch's pack_padded_sequence removes padding before the LSTM, passing only real tokens through the recurrent computation. The LSTM processes a compressed representation and pad_packed_sequence restores the padded form afterward. For bidirectional LSTMs with variable-length sequences, this optimization is especially important since both directions process the same padding.

```python
import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence, pad_sequence

def batch_variable_length(lengths, input_size=4, hidden_size=16):
    torch.manual_seed(1)
    seqs = [torch.randn(l, input_size) for l in lengths]
    bilstm = nn.LSTM(input_size, hidden_size, bidirectional=True, batch_first=True)

    seqs_sorted = sorted(seqs, key=len, reverse=True)
    len_sorted  = sorted(lengths, reverse=True)
    len_tensor  = torch.tensor(len_sorted)

    padded = pad_sequence(seqs_sorted, batch_first=True, padding_value=0.0)
    wasted = padded.numel() - sum(l * input_size for l in len_sorted)
    print('Padded batch: {}  ({} wasted elements)'.format(tuple(padded.shape), wasted))

    packed = pack_padded_sequence(padded, len_tensor, batch_first=True)
    out_packed, (h_n, _) = bilstm(packed)
    print('Packed data:  {}  (no wasted computation)'.format(tuple(packed.data.shape)))

    out_pad, out_lens = pad_packed_sequence(out_packed, batch_first=True)
    print('Unpacked out: {}  actual lengths: {}'.format(
        tuple(out_pad.shape), out_lens.tolist()))
    print('h_n shape:    {}  <- [fwd_final, bwd_final] x batch'.format(tuple(h_n.shape)))

batch_variable_length(lengths=[12, 8, 5, 3])
```

## Sequence Labeling — BiLSTM for NER

Named entity recognition (NER) requires tagging each token with a label (e.g. B-PER, I-ORG, O using BIO notation). BiLSTM is the canonical pre-Transformer architecture for NER: each token's representation benefits from both left and right context. Two stacked BiLSTM layers are standard — the first captures local syntactic patterns, the second integrates them into higher-level entity representations. A linear classifier on top of each BiLSTM output position produces per-token logits.

```python
import torch
import torch.nn as nn

class BiLSTMNER(nn.Module):
    """Bidirectional 2-layer LSTM for token-level NER (sequence labeling)."""
    def __init__(self, vocab_size, embed_dim, hidden_size, n_tags, pad_idx=0):
        super().__init__()
        self.embed  = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_idx)
        self.bilstm = nn.LSTM(embed_dim, hidden_size, num_layers=2,
                              bidirectional=True, batch_first=True, dropout=0.3)
        self.drop   = nn.Dropout(0.5)
        self.fc     = nn.Linear(2 * hidden_size, n_tags)

    def forward(self, token_ids):
        emb    = self.drop(self.embed(token_ids))    # (B, T, E)
        out, _ = self.bilstm(emb)                    # (B, T, 2H)
        out    = self.drop(out)
        return self.fc(out)                           # (B, T, n_tags)

torch.manual_seed(42)
V, E, H, TAGS = 5000, 64, 128, 9   # 9 BIO tags: O + B/I for 4 entity types
model = BiLSTMNER(V, E, H, TAGS)
tokens = torch.randint(1, V, (8, 20))      # batch=8, seq_len=20
labels = torch.randint(0, TAGS, (8, 20))

logits = model(tokens)
loss = nn.CrossEntropyLoss()(logits.view(-1, TAGS), labels.view(-1))
print('BiLSTM-NER (2-layer, bidirectional):')
print('  Input tokens: {}'.format(tuple(tokens.shape)))
print('  Output logits: {}  (per-token tag scores)'.format(tuple(logits.shape)))
print('  Loss: {:.4f}'.format(loss.item()))
print('  Params: {:,}'.format(sum(p.numel() for p in model.parameters())))
```

> **BiRNN Cannot Be Used Autoregressively**: Bidirectional RNNs require the full input sequence to be available before processing — they cannot generate output tokens one at a time because the backward pass has not run yet. This makes them unsuitable for autoregressive generation (language modeling, machine translation decoding). They are appropriate only for encoding tasks where the full input is known: classification, tagging, named entity recognition, or as the encoder in encoder-decoder architectures.

## Unidirectional vs Bidirectional Comparison

The choice between unidirectional and bidirectional depends primarily on whether future context is available at inference time. For sequence encoding tasks (classification, tagging, translation encoding) bidirectional is almost always better. For generation tasks it is impossible. Memory doubles because there are two sets of hidden states, and training is slower but generally produces significantly better representations for fixed-input tasks.

| Property | Unidirectional | Bidirectional |
| --- | --- | --- |
| Context at t | x1...xt (causal only) | x1...xT (full sequence) |
| Autoregressive generation | Yes — outputs token by token | No — needs full input first |
| Memory (H=128) | 128 per step | 256 per step (2x) |
| Training speed | Faster (1 LSTM pass) | ~2x slower (2 LSTM passes) |
| NER / tagging | Weaker — no right context | Standard choice — both contexts |
| Language model | Standard — causal constraint | Not applicable for generation |
| Encoder in seq2seq | Common | Preferred — richer source repr |

## Applications and Common Patterns

BiLSTM is used as the encoder in many NLP architectures: BiLSTM-CRF for NER (add a Conditional Random Field on top of BiLSTM logits to enforce label consistency), BiLSTM + attention for text classification, and BiLSTM encoder + unidirectional LSTM decoder for sequence-to-sequence tasks (machine translation before Transformers). BERT pre-trains bidirectional Transformer encoders rather than BiLSTMs, but the core idea — full context at every position — is the same.

- BiLSTM-CRF: gold standard pre-Transformer NER — BiLSTM features + Viterbi decoding.
- BiLSTM encoder + unidirectional decoder: standard seq2seq for translation (Bahdanau 2015).
- DeepSpeech: stacked BiLSTMs for acoustic modeling in speech recognition.
- ELMo: deep BiLSTM language model used as contextual word embeddings (Peters et al. 2018).
- Sentiment analysis: BiLSTM over sentence with max-pool or attention over all positions.
- Document encoding: hierarchical BiLSTM — word-level then sentence-level.

Bidirectional processing is one of the most reliable improvements available for any fixed-input sequence task. The engineering cost is minimal (one flag in PyTorch, careful shape handling for h_n) while the accuracy gain from full context can be substantial. Modern Transformer encoders are also bidirectional by nature — BERT's self-attention attends to all positions simultaneously — making BiLSTM understanding directly relevant to interpreting why encoder-only Transformers work so well.

---

