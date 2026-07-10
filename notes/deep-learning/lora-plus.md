---
title: "LoRA+ — Different Learning Rates for A and B Matrices"
slug: "lora-plus"
description: "LoRA+ (Hayou et al. 2024) sets a higher learning rate for the B matrix than A, following maximal update parameterization theory. Achieves 1–2% benchmark improvement at zero extra compute by treating A and B as evolving at different timescales."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgTG9SQSBkZWNvbXBvc2VzIGEgd2VpZ2h0IHVwZGF0ZSBhcyDOlFcgPSBCwrdBIHdoZXJlIEEg4oiIIOKEnV57csOXZF9pbn0gYW5kIEIg4oiIIOKEnV57ZF9vdXTDl3J9LiBCeSBkZWZhdWx0LCBib3RoIG1hdHJpY2VzIGFyZSB0cmFpbmVkIHdpdGggdGhlIHNhbWUgbGVhcm5pbmcgcmF0ZSB1c2luZyBhIHNpbmdsZSBvcHRpbWl6ZXIgcGFyYW1ldGVyIGdyb3VwLiBMb1JBKyAoSGF5b3UgZXQgYWwuLCAyMDI0KSBpZGVudGlmaWVzIHRoaXMgYXMgYSBzdWJvcHRpbWFsIGNob2ljZTogQSBhbmQgQiBwbGF5IGZ1bmRhbWVudGFsbHkgZGlmZmVyZW50IHJvbGVzIGluIHRoZSBhZGFwdGVyIGFuZCBzaG91bGQgZXZvbHZlIGF0IGRpZmZlcmVudCB0aW1lc2NhbGVzLiBTZXR0aW5nIM63X0IgPSDOu8K3zrdfQSB3aXRoIM67PTE2IHlpZWxkcyBjb25zaXN0ZW50IDHigJMyJSBiZW5jaG1hcmsgZ2FpbnMgYXQgemVybyBhZGRpdGlvbmFsIGNvbXB1dGUgY29zdC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgUHJvYmxlbSB3aXRoIFN0YW5kYXJkIExvUkEgTGVhcm5pbmcgUmF0ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIExvUkEsIEEgaXMgaW5pdGlhbGl6ZWQgd2l0aCBhIEdhdXNzaWFuIGRpc3RyaWJ1dGlvbiAocmFuZG9tIHByb2plY3Rpb24sIGlucHV0LXNpZGUpIGFuZCBCIGlzIGluaXRpYWxpemVkIHRvIHplcm8gKG91dHB1dC1zaWRlLCBzdGFydHMgY29udHJpYnV0aW5nIG5vdGhpbmcpLiBEdXJpbmcgdHJhaW5pbmcsIEEgZnVuY3Rpb25zIGFzIGEgZmVhdHVyZSBleHRyYWN0b3IgdGhhdCBhZGFwdHMgdGhlIGRpcmVjdGlvbiBpbiB3aGljaCBpbnB1dHMgYXJlIHByb2plY3RlZCwgd2hpbGUgQiBzY2FsZXMgYW5kIGNvbWJpbmVzIHRob3NlIHByb2plY3RlZCBmZWF0dXJlcyBpbnRvIHRoZSBvdXRwdXQgc3BhY2UuIFRoZXNlIHR3byByb2xlcyByZXF1aXJlIGRpZmZlcmVudCBsZWFybmluZyBkeW5hbWljczogQiBtdXN0IG1vdmUgcXVpY2tseSBmcm9tIHplcm8gdG8gdXNlZnVsIHZhbHVlcyB3aGlsZSBBIHNob3VsZCB1cGRhdGUgbW9yZSBjYXJlZnVsbHkgdG8gcHJlc2VydmUgdGhlIGxlYXJuZWQgcHJvamVjdGlvbiBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmVhdHVyZSBMZWFybmluZyBUaGVvcnkgYW5kIE1heGltYWwgVXBkYXRlIFBhcmFtZXRlcml6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1heGltYWwgdXBkYXRlIHBhcmFtZXRlcml6YXRpb24gKG11UCwgWWFuZyBldCBhbC4sIDIwMjIpIHByb3ZpZGVzIGEgcHJpbmNpcGxlZCBmcmFtZXdvcmsgZm9yIHNldHRpbmcgcGVyLWxheWVyIGxlYXJuaW5nIHJhdGVzIGluIGluZmluaXRlLXdpZHRoIG5ldHdvcmtzLiBVbmRlciBtdVAsIFx1MDAyN2xhc3QtbGF5ZXJcdTAwMjcgcGFyYW1ldGVycyDigJQgdGhvc2UgY2xvc2VzdCB0byB0aGUgb3V0cHV0IOKAlCBzaG91bGQgcmVjZWl2ZSBhIGxhcmdlciBsZWFybmluZyByYXRlIHRvIGVuc3VyZSBmZWF0dXJlIGxlYXJuaW5nIChhcyBvcHBvc2VkIHRvIGxhenkgdHJhaW5pbmcpLiBJbiBMb1JBXHUwMDI3cyBjb250ZXh0LCBCIGlzIHRoZSBvdXRwdXQtcHJveGltYWwgbWF0cml4IGFuZCBzaG91bGQgaGF2ZSBhIGxhcmdlciBMUi4gQSBpcyB0aGUgaW5wdXQtcHJveGltYWwgbWF0cml4IGFuZCBiZW5lZml0cyBmcm9tIGEgc21hbGxlciBMUi4gTG9SQSsgZm9ybWFsaXplcyB0aGlzIHdpdGggdGhlIHJhdGlvIM63X0IvzrdfQSA9IM67LCB3aGVyZSDOuz0xNiBpcyB0aGUgZW1waXJpY2FsbHkgdmFsaWRhdGVkIGRlZmF1bHQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9SQSsgT3B0aW1pemVyIFNldHVwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2V5IGltcGxlbWVudGF0aW9uIGRldGFpbCBpcyBjcmVhdGluZyBzZXBhcmF0ZSBwYXJhbWV0ZXIgZ3JvdXBzIGZvciBBIGFuZCBCIG1hdHJpY2VzLiBQeVRvcmNoXHUwMDI3cyBBZGFtVyBvcHRpbWl6ZXIgYWNjZXB0cyBhIGxpc3Qgb2YgcGFyYW1ldGVyIGdyb3VwIGRpY3Rpb25hcmllcywgZWFjaCB3aXRoIGl0cyBvd24gbGVhcm5pbmcgcmF0ZS4gQnkgaXRlcmF0aW5nIG92ZXIgbmFtZWQgcGFyYW1ldGVycyBhbmQgcm91dGluZyBBLXN1ZmZpeCBwYXJhbWV0ZXJzIHRvIG9uZSBncm91cCBhbmQgQi1zdWZmaXggcGFyYW1ldGVycyB0byBhbm90aGVyLCBMb1JBKyByZXF1aXJlcyBvbmx5IGEgc21hbGwgd3JhcHBlciBhcm91bmQgc3RhbmRhcmQgb3B0aW1pemVyIGNvbnN0cnVjdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cbmZyb20gcGVmdCBpbXBvcnQgTG9yYUNvbmZpZywgZ2V0X3BlZnRfbW9kZWxcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTVxuXG5kZWYgY3JlYXRlX2xvcmFfcGx1c19vcHRpbWl6ZXIoXG4gICAgbW9kZWw6IHRvcmNoLm5uLk1vZHVsZSxcbiAgICBscl9BOiBmbG9hdCA9IDFlLTQsXG4gICAgbGFtYmRhX3JhdGlvOiBmbG9hdCA9IDE2LjAsXG4gICAgd2VpZ2h0X2RlY2F5OiBmbG9hdCA9IDAuMDEsXG4pIC1cdTAwM2Ugb3B0aW0uQWRhbVc6XG4gICAgXCJcIlwiQ3JlYXRlIEFkYW1XIHdpdGggc2VwYXJhdGUgTFJzIGZvciBMb1JBIEEgYW5kIEIgbWF0cmljZXMuXCJcIlwiXG4gICAgbHJfQiA9IGxyX0EgKiBsYW1iZGFfcmF0aW9cbiAgICBncm91cF9BLCBncm91cF9CLCBncm91cF9vdGhlciA9IFtdLCBbXSwgW11cbiAgICBmb3IgbmFtZSwgcGFyYW0gaW4gbW9kZWwubmFtZWRfcGFyYW1ldGVycygpOlxuICAgICAgICBpZiBub3QgcGFyYW0ucmVxdWlyZXNfZ3JhZDpcbiAgICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgIGlmIFx1MDAyN2xvcmFfQVx1MDAyNyBpbiBuYW1lOlxuICAgICAgICAgICAgZ3JvdXBfQS5hcHBlbmQocGFyYW0pXG4gICAgICAgIGVsaWYgXHUwMDI3bG9yYV9CXHUwMDI3IGluIG5hbWU6XG4gICAgICAgICAgICBncm91cF9CLmFwcGVuZChwYXJhbSlcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIGdyb3VwX290aGVyLmFwcGVuZChwYXJhbSlcbiAgICBwYXJhbV9ncm91cHMgPSBbXG4gICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IGdyb3VwX0EsIFx1MDAyN2xyXHUwMDI3OiBscl9BLCBcdTAwMjd3ZWlnaHRfZGVjYXlcdTAwMjc6IHdlaWdodF9kZWNheX0sXG4gICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IGdyb3VwX0IsIFx1MDAyN2xyXHUwMDI3OiBscl9CLCBcdTAwMjd3ZWlnaHRfZGVjYXlcdTAwMjc6IHdlaWdodF9kZWNheX0sXG4gICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IGdyb3VwX290aGVyLCBcdTAwMjdsclx1MDAyNzogbHJfQSwgXHUwMDI3d2VpZ2h0X2RlY2F5XHUwMDI3OiB3ZWlnaHRfZGVjYXl9LFxuICAgIF1cbiAgICBwcmludChmXHUwMDI3TG9SQSsgb3B0aW1pemVyOiBscl9BPXtscl9BOi4yZX0sIGxyX0I9e2xyX0I6LjJlfSAozrs9e2xhbWJkYV9yYXRpb30pXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIEEgcGFyYW1zOiB7bGVuKGdyb3VwX0EpfSwgQiBwYXJhbXM6IHtsZW4oZ3JvdXBfQil9LCBvdGhlcjoge2xlbihncm91cF9vdGhlcil9XHUwMDI3KVxuICAgIHJldHVybiBvcHRpbS5BZGFtVyhwYXJhbV9ncm91cHMpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9SQSsgTGF5ZXIgSW1wbGVtZW50YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc2VsZi1jb250YWluZWQgTG9SQSsgbW9kdWxlIHN0b3JlcyBBIGFuZCBCIGFzIHNlcGFyYXRlIG5hbWVkIGF0dHJpYnV0ZXMgbWF0Y2hpbmcgdGhlIHBlZnQgbGlicmFyeSBjb252ZW50aW9uIChsb3JhX0EsIGxvcmFfQikuIFRoZSBmb3J3YXJkIHBhc3MgaXMgaWRlbnRpY2FsIHRvIHN0YW5kYXJkIExvUkEg4oCUIHRoZSBkaWZmZXJlbmNlIGlzIGVudGlyZWx5IGluIHRoZSBvcHRpbWl6ZXIgY29uZmlndXJhdGlvbi4gVGhlIHNjYWxpbmcgZmFjdG9yIM6xL3IgaXMgYXBwbGllZCB0byB0aGUgQsK3QSBwcm9kdWN0IHRvIG5vcm1hbGl6ZSB0aGUgaW5pdGlhbGl6YXRpb24gdmFyaWFuY2UgcmVnYXJkbGVzcyBvZiByYW5rLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuY2xhc3MgTG9SQVBsdXNMaW5lYXIobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJMaW5lYXIgbGF5ZXIgd2l0aCBMb1JBKyBhZGFwdGVyIChzZXBhcmF0ZSBMUiBncm91cHMgZm9yIEEgYW5kIEIpLlwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2ZlYXR1cmVzOiBpbnQsIG91dF9mZWF0dXJlczogaW50LCByYW5rOiBpbnQgPSAxNixcbiAgICAgICAgICAgICAgICAgYWxwaGE6IGZsb2F0ID0gMTYuMCwgZHJvcG91dDogZmxvYXQgPSAwLjA1KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucmFuayA9IHJhbmtcbiAgICAgICAgc2VsZi5zY2FsaW5nID0gYWxwaGEgLyByYW5rXG4gICAgICAgICMgQmFzZSB3ZWlnaHQgZnJvemVuXG4gICAgICAgIHNlbGYud2VpZ2h0ID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKG91dF9mZWF0dXJlcywgaW5fZmVhdHVyZXMpLCByZXF1aXJlc19ncmFkPUZhbHNlKVxuICAgICAgICBzZWxmLmJpYXMgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2ZlYXR1cmVzKSwgcmVxdWlyZXNfZ3JhZD1GYWxzZSlcbiAgICAgICAgIyBMb1JBIGFkYXB0ZXJzOiBBPUdhdXNzaWFuIGluaXQsIEI9emVybyBpbml0XG4gICAgICAgIHNlbGYubG9yYV9BID0gbm4uUGFyYW1ldGVyKHRvcmNoLmVtcHR5KHJhbmssIGluX2ZlYXR1cmVzKSlcbiAgICAgICAgc2VsZi5sb3JhX0IgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2ZlYXR1cmVzLCByYW5rKSlcbiAgICAgICAgbm4uaW5pdC5rYWltaW5nX3VuaWZvcm1fKHNlbGYubG9yYV9BLCBhPW1hdGguc3FydCg1KSlcbiAgICAgICAgc2VsZi5kcm9wb3V0ID0gbm4uRHJvcG91dChkcm9wb3V0KVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgYmFzZV9vdXQgPSBubi5mdW5jdGlvbmFsLmxpbmVhcih4LCBzZWxmLndlaWdodCwgc2VsZi5iaWFzKVxuICAgICAgICBsb3JhX291dCA9IG5uLmZ1bmN0aW9uYWwubGluZWFyKFxuICAgICAgICAgICAgc2VsZi5kcm9wb3V0KHgpLCBzZWxmLmxvcmFfQVxuICAgICAgICApICAjIChiYXRjaCwgcmFuaylcbiAgICAgICAgbG9yYV9vdXQgPSBubi5mdW5jdGlvbmFsLmxpbmVhcihsb3JhX291dCwgc2VsZi5sb3JhX0IpICAjIChiYXRjaCwgb3V0KVxuICAgICAgICByZXR1cm4gYmFzZV9vdXQgKyBsb3JhX291dCAqIHNlbGYuc2NhbGluZ1xuXG4gICAgZGVmIGdldF9wYXJhbV9ncm91cHMoc2VsZiwgbHJfQTogZmxvYXQsIGxhbWJkYV9yYXRpbzogZmxvYXQgPSAxNi4wKTpcbiAgICAgICAgcmV0dXJuIFtcbiAgICAgICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IFtzZWxmLmxvcmFfQV0sIFx1MDAyN2xyXHUwMDI3OiBscl9BfSxcbiAgICAgICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IFtzZWxmLmxvcmFfQl0sIFx1MDAyN2xyXHUwMDI3OiBscl9BICogbGFtYmRhX3JhdGlvfSxcbiAgICAgICAgXVxuXG5sYXllciA9IExvUkFQbHVzTGluZWFyKDc2OCwgNzY4LCByYW5rPTE2KVxueCA9IHRvcmNoLnJhbmRuKDQsIDc2OClcbnByaW50KGZcdTAwMjdPdXRwdXQgc2hhcGU6IHtsYXllcih4KS5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3bG9yYV9BIHNoYXBlOiB7bGF5ZXIubG9yYV9BLnNoYXBlfSwgbG9yYV9CIHNoYXBlOiB7bGF5ZXIubG9yYV9CLnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYW1iZGEgU2Vuc2l0aXZpdHkgQW5hbHlzaXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjaG9pY2Ugb2YgzrsgZGV0ZXJtaW5lcyB0aGUgcmF0aW8gzrdfQi/Ot19BLiBIYXlvdSBldCBhbC4gcGVyZm9ybSBhIHN3ZWVwIGFjcm9zcyDOuyDiiIggezEsIDIsIDQsIDgsIDE2LCAzMn0gb24gY29tbW9uc2Vuc2UgcmVhc29uaW5nIGFuZCBtYXRoIGJlbmNobWFya3MuIM67PTEgaXMgZXF1aXZhbGVudCB0byBzdGFuZGFyZCBMb1JBLiBUaGUgcmVzdWx0cyBzaG93IGEgY2xlYXIgb3B0aW11bSBhcm91bmQgzrs9MTYgd2l0aCBkaW1pbmlzaGluZyByZXR1cm5zIGJleW9uZCwgYW5kIHNsaWdodCBkZWdyYWRhdGlvbiBhdCDOuz0zMiBkdWUgdG8gQiBtb3ZpbmcgdG9vIGZhc3QgYW5kIG92ZXJzaG9vdGluZyBnb29kIHNvbHV0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuZnJvbSB0b3JjaC51dGlscy5kYXRhIGltcG9ydCBEYXRhTG9hZGVyLCBUZW5zb3JEYXRhc2V0XG5cbmRlZiBscl9yYXRpb19zd2VlcChsYW1iZGFzPSgxLCAyLCA0LCA4LCAxNiwgMzIpLCBuX3N0ZXBzPTIwMCxcbiAgICAgICAgICAgICAgICAgICBpbl9kaW09MTI4LCBvdXRfZGltPTMyLCByYW5rPTgsIHNlZWQ9NDIpOlxuICAgIFwiXCJcIlN3ZWVwIExSIHJhdGlvIGxhbWJkYSBhbmQgbWVhc3VyZSBmaW5hbCB2YWxpZGF0aW9uIGxvc3MuXCJcIlwiXG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICBYID0gdG9yY2gucmFuZG4oNTEyLCBpbl9kaW0pXG4gICAgeSA9IHRvcmNoLnJhbmRpbnQoMCwgb3V0X2RpbSwgKDUxMiwpKVxuICAgIGxvYWRlciA9IERhdGFMb2FkZXIoVGVuc29yRGF0YXNldChYLCB5KSwgYmF0Y2hfc2l6ZT02NCwgc2h1ZmZsZT1UcnVlKVxuICAgIHJlc3VsdHMgPSB7fVxuICAgIGZvciBsYW0gaW4gbGFtYmRhczpcbiAgICAgICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICAgICAgbG9yYV9BID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKHJhbmssIGluX2RpbSkgKiAwLjAyKVxuICAgICAgICBsb3JhX0IgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Mob3V0X2RpbSwgcmFuaykpXG4gICAgICAgIGJhc2VfVyA9IHRvcmNoLnJhbmRuKG91dF9kaW0sIGluX2RpbSlcbiAgICAgICAgb3B0ID0gb3B0aW0uQWRhbVcoW1xuICAgICAgICAgICAge1x1MDAyN3BhcmFtc1x1MDAyNzogW2xvcmFfQV0sIFx1MDAyN2xyXHUwMDI3OiAxZS0zfSxcbiAgICAgICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IFtsb3JhX0JdLCBcdTAwMjdsclx1MDAyNzogMWUtMyAqIGxhbX0sXG4gICAgICAgIF0sIHdlaWdodF9kZWNheT0wLjAxKVxuICAgICAgICBjcml0ZXJpb24gPSBubi5Dcm9zc0VudHJvcHlMb3NzKClcbiAgICAgICAgZm9yIHN0ZXAsICh4YiwgeWIpIGluIHppcChyYW5nZShuX3N0ZXBzKSwgbG9hZGVyKTpcbiAgICAgICAgICAgIG9wdC56ZXJvX2dyYWQoKVxuICAgICAgICAgICAgb3V0ID0gKHhiIEAgYmFzZV9XLlQpICsgKHhiIEAgbG9yYV9BLlQpIEAgbG9yYV9CLlRcbiAgICAgICAgICAgIGxvc3MgPSBjcml0ZXJpb24ob3V0LCB5YilcbiAgICAgICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICAgICAgb3B0LnN0ZXAoKVxuICAgICAgICByZXN1bHRzW2xhbV0gPSBsb3NzLml0ZW0oKVxuICAgICAgICBwcmludChmXHUwMDI3ICBsYW1iZGE9e2xhbTpcdTAwM2UyfTogZmluYWwgbG9zcyA9IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KVxuICAgIGJlc3QgPSBtaW4ocmVzdWx0cywga2V5PXJlc3VsdHMuZ2V0KVxuICAgIHByaW50KGZcdTAwMjdCZXN0IGxhbWJkYToge2Jlc3R9IChsb3NzPXtyZXN1bHRzW2Jlc3RdOi40Zn0pXHUwMDI3KVxuICAgIHJldHVybiByZXN1bHRzXG5cbnByaW50KFx1MDAyN0xSIHJhdGlvIHN3ZWVwOlx1MDAyNylcbmxyX3JhdGlvX3N3ZWVwKCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBIHZzIEIgR3JhZGllbnQgQW5hbHlzaXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIHVuZGVyc3RhbmQgd2h5IGRpZmZlcmVudCBMUnMgaGVscCwgd2UgY2FuIHRyYWNrIGdyYWRpZW50IG5vcm1zIGFuZCBlZmZlY3RpdmUgdXBkYXRlIG1hZ25pdHVkZXMgZm9yIEEgYW5kIEIgdGhyb3VnaG91dCB0cmFpbmluZy4gV2l0aCB0aGUgc2FtZSBMUiwgQlx1MDAyN3MgZ3JhZGllbnQgbm9ybSBpcyB0eXBpY2FsbHkgbXVjaCBsYXJnZXIgaW4gZWFybHkgdHJhaW5pbmcgKGl0IHN0YXJ0cyBhdCB6ZXJvIGFuZCBuZWVkcyB0byBjYXRjaCB1cCksIHdoaWxlIEFcdTAwMjdzIGdyYWRpZW50IG5vcm0gaXMgbW9yZSBzdGFibGUuIExvUkErIGV4cGxpY2l0bHkgY29tcGVuc2F0ZXMgYnkgc2NhbGluZyB0aGUgQiB1cGRhdGUgdXB3YXJkLCBtYXRjaGluZyB3aGF0IHRoZSBuYXR1cmFsIGdyYWRpZW50IHdvdWxkIHN1Z2dlc3QuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cblxuZGVmIHRyYWNrX2FiX2dyYWRpZW50cyhuX3N0ZXBzPTEwMCwgcmFuaz0xNiwgaW5fZGltPTI1Niwgb3V0X2RpbT02NCwgbGFtYmRhX3JhdGlvPTE2KTpcbiAgICBcIlwiXCJUcmFjayBncmFkaWVudCBub3JtcyBhbmQgdXBkYXRlIG1hZ25pdHVkZXMgZm9yIEEgYW5kIEIgbWF0cmljZXMuXCJcIlwiXG4gICAgbG9yYV9BID0gbm4uUGFyYW1ldGVyKHRvcmNoLnJhbmRuKHJhbmssIGluX2RpbSkgKiAwLjAyKVxuICAgIGxvcmFfQiA9IG5uLlBhcmFtZXRlcih0b3JjaC56ZXJvcyhvdXRfZGltLCByYW5rKSlcbiAgICBvcHQgPSBvcHRpbS5BZGFtVyhbXG4gICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IFtsb3JhX0FdLCBcdTAwMjdsclx1MDAyNzogMWUtNH0sXG4gICAgICAgIHtcdTAwMjdwYXJhbXNcdTAwMjc6IFtsb3JhX0JdLCBcdTAwMjdsclx1MDAyNzogMWUtNCAqIGxhbWJkYV9yYXRpb30sXG4gICAgXSlcbiAgICBoaXN0b3J5ID0ge1x1MDAyN2dyYWRfQVx1MDAyNzogW10sIFx1MDAyN2dyYWRfQlx1MDAyNzogW10sIFx1MDAyN25vcm1fQVx1MDAyNzogW10sIFx1MDAyN25vcm1fQlx1MDAyNzogW119XG4gICAgZm9yIHN0ZXAgaW4gcmFuZ2Uobl9zdGVwcyk6XG4gICAgICAgIHggPSB0b3JjaC5yYW5kbigzMiwgaW5fZGltKVxuICAgICAgICBvdXQgPSB4IEAgbG9yYV9BLlQgQCBsb3JhX0IuVFxuICAgICAgICBsb3NzID0gb3V0LnBvdygyKS5tZWFuKClcbiAgICAgICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICBpZiBsb3JhX0EuZ3JhZCBpcyBub3QgTm9uZTpcbiAgICAgICAgICAgIGhpc3RvcnlbXHUwMDI3Z3JhZF9BXHUwMDI3XS5hcHBlbmQobG9yYV9BLmdyYWQubm9ybSgpLml0ZW0oKSlcbiAgICAgICAgICAgIGhpc3RvcnlbXHUwMDI3Z3JhZF9CXHUwMDI3XS5hcHBlbmQobG9yYV9CLmdyYWQubm9ybSgpLml0ZW0oKSlcbiAgICAgICAgaGlzdG9yeVtcdTAwMjdub3JtX0FcdTAwMjddLmFwcGVuZChsb3JhX0EuZGF0YS5ub3JtKCkuaXRlbSgpKVxuICAgICAgICBoaXN0b3J5W1x1MDAyN25vcm1fQlx1MDAyN10uYXBwZW5kKGxvcmFfQi5kYXRhLm5vcm0oKS5pdGVtKCkpXG4gICAgICAgIG9wdC5zdGVwKClcbiAgICBmaW5hbCA9IHtrOiByb3VuZCh2Wy0xXSwgNSkgZm9yIGssIHYgaW4gaGlzdG9yeS5pdGVtcygpfVxuICAgIHByaW50KGZcdTAwMjdGaW5hbCBncmFkIG5vcm1zICDigJQgQToge2ZpbmFsW1wiZ3JhZF9BXCJdOi41Zn0sIEI6IHtmaW5hbFtcImdyYWRfQlwiXTouNWZ9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdGaW5hbCBwYXJhbSBub3JtcyDigJQgQToge2ZpbmFsW1wibm9ybV9BXCJdOi40Zn0sIEI6IHtmaW5hbFtcIm5vcm1fQlwiXTouNGZ9XHUwMDI3KVxuICAgIHJldHVybiBoaXN0b3J5XG5cbnRyYWNrX2FiX2dyYWRpZW50cygpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9SQSBMZWFybmluZyBSYXRlIFN0cmF0ZWd5IENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiU3RyYXRlZ3kiLCJMUiBmb3IgQSIsIkxSIGZvciBCIiwiRXh0cmEgQ29tcHV0ZSIsIlR5cGljYWwgSW1wcm92ZW1lbnQiLCJOb3RlcyJdLCJyb3dzIjpbWyJTdGFuZGFyZCBMb1JBIiwizrciLCLOtyIsIk5vbmUiLCJCYXNlbGluZSIsIlNhbWUgTFIgZm9yIGJvdGg7IHNpbXBsZSBidXQgc3Vib3B0aW1hbCJdLFsiTG9SQSsgKM67PTE2KSIsIs63IiwiMTbCt863IiwiTm9uZSIsIisx4oCTMiUgb24gbW9zdCBiZW5jaG1hcmtzIiwiUmVjb21tZW5kZWQgZGVmYXVsdDsgZnJlZSBwZXJmb3JtYW5jZSBnYWluIl0sWyJMb1JBKyAozrs9NCkiLCLOtyIsIjTCt863IiwiTm9uZSIsIiswLjXigJMxJSIsIkNvbnNlcnZhdGl2ZSByYXRpbzsgbG93ZXIgcmlzayBvZiBCIGluc3RhYmlsaXR5Il0sWyJtdVAgTG9SQSIsIs63L2Zhbl9pbiIsIs63IChsYXN0LWxheWVyIHNjYWxlZCkiLCJOb25lIiwiKzHigJMyJSIsIkZ1bGwgbXVQIHRyYW5zZmVyOiBzZXQgTFIgdmlhIM68UCBjb29yZCBjaGVjayJdLFsiQWRhTG9SQSIsIkFkYXB0aXZlIChTVkQpIiwiQWRhcHRpdmUgKFNWRCkiLCJ+MjAlIG92ZXJoZWFkIiwiKzHigJMzJSIsIkltcG9ydGFuY2UtYXdhcmUgcmFuayBhbGxvY2F0aW9uOyBtb3JlIGNvbXBsZXgiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9SQSsgc3RhY2tzIG5hdHVyYWxseSB3aXRoIERvUkEgKHdlaWdodCBkZWNvbXBvc2l0aW9uIGludG8gbWFnbml0dWRlIGFuZCBkaXJlY3Rpb24pOiB0aGUgZGlyZWN0aW9uIGNvbXBvbmVudCBtYXBzIHRvIEFcdTAwMjdzIHJvbGUgYW5kIHRoZSBtYWduaXR1ZGUgY29tcG9uZW50IG1hcHMgdG8gQlx1MDAyN3Mgcm9sZS4gU2V0dGluZyBhIGhpZ2hlciBMUiBmb3IgdGhlIG1hZ25pdHVkZSB2ZWN0b3IgKERvUkFcdTAwMjdzIGVxdWl2YWxlbnQgb2YgQikgYW5kIGEgbG93ZXIgTFIgZm9yIHRoZSBkaXJlY3Rpb25hbCBMb1JBIG1hdHJpY2VzIGlzIGNvbnNpc3RlbnQgd2l0aCBMb1JBKyB0aGVvcnkuIFRoaXMgY29tYmluZWQgc2V0dXAgaGFzIGJlZW4gcmVwb3J0ZWQgdG8gb3V0cGVyZm9ybSBlaXRoZXIgbWV0aG9kIGFsb25lIG9uIHNldmVyYWwgaW5zdHJ1Y3Rpb24tZm9sbG93aW5nIGJlbmNobWFya3MuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkxvUkErIGlzIGEgZnJlZSBwZXJmb3JtYW5jZSB1cGdyYWRlIiwiY29udGVudCI6IkxvUkErIHdpdGggzrs9MTYgKM63X0IgPSAxNsK3zrdfQSkgcHJvdmlkZXMgMeKAkzIlIGNvbnNpc3RlbnQgaW1wcm92ZW1lbnQgYWNyb3NzIHRhc2tzIHdpdGggemVybyBhZGRpdGlvbmFsIGNvbXB1dGUg4oCUIGl0XHUwMDI3cyBhIGZyZWUgcGVyZm9ybWFuY2UgdXBncmFkZSB0aGF0IHNob3VsZCBiZSB0aGUgZGVmYXVsdCBvdmVyIHN0YW5kYXJkIExvUkEgaW4gbW9zdCBmaW5lLXR1bmluZyBzZXR1cHMuIFNpbXBseSBzcGxpdCB5b3VyIExvUkEgcGFyYW1ldGVycyBpbnRvIHR3byBvcHRpbWl6ZXIgZ3JvdXBzIGFuZCBzZXQgdGhlIEIgZ3JvdXBcdTAwMjdzIExSIDE2w5cgaGlnaGVyLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsizrs9MTYgaXMgdGhlIG1vc3Qgcm9idXN0IGRlZmF1bHQ7IHNlbnNpdGl2aXR5IGFuYWx5c2lzIHNob3dzIGxpdHRsZSBnYWluIGJleW9uZCDOuz0xNiBhbmQgcmlzayBvZiBpbnN0YWJpbGl0eSBhdCDOuz0zMi4iLCJBIGlzIGluaXRpYWxpemVkIHdpdGggR2F1c3NpYW4gbm9pc2UgYW5kIGFkYXB0cyBmZWF0dXJlIGRpcmVjdGlvbnM7IEIgc3RhcnRzIGF0IHplcm8gYW5kIGFkYXB0cyBvdXRwdXQgbWFnbml0dWRlcy4iLCJtdVAgdGhlb3J5IHByZWRpY3RzIHRoYXQgb3V0cHV0LXByb3hpbWFsIHBhcmFtZXRlcnMgc2hvdWxkIHJlY2VpdmUgbGFyZ2VyIExSIOKAlCBMb1JBKyBpcyBhIHByYWN0aWNhbCBhcHByb3hpbWF0aW9uLiIsIkxvUkErIGFkZHMgbm8gdHJhaW5hYmxlIHBhcmFtZXRlcnMsIG5vIGZvcndhcmQtcGFzcyBvdmVyaGVhZCwgYW5kIG5vIG1lbW9yeSBjb3N0IGJleW9uZCB0d28gb3B0aW1pemVyIHN0YXRlIHBhcnRpdGlvbnMuIiwiQ29tcGF0aWJsZSB3aXRoIHF1YW50aXphdGlvbiAoUUxvUkEpLCBEb1JBLCBhbmQgZ3JhZGllbnQgY2hlY2twb2ludGluZyDigJQgbm8gYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzIHJlcXVpcmVkLiIsIldoZW4gdXNpbmcgcGVmdCBsaWJyYXJ5LCBmaWx0ZXIgbmFtZWRfcGFyYW1ldGVycyBieSBcdTAwMjdsb3JhX0FcdTAwMjcgYW5kIFx1MDAyN2xvcmFfQlx1MDAyNyBzdWZmaXhlcyBmb3IgZ3JvdXAgc2VwYXJhdGlvbi4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# LoRA+ — Different Learning Rates for A and B Matrices

Standard LoRA decomposes a weight update as ΔW = B·A where A ∈ ℝ^{r×d_in} and B ∈ ℝ^{d_out×r}. By default, both matrices are trained with the same learning rate using a single optimizer parameter group. LoRA+ (Hayou et al., 2024) identifies this as a suboptimal choice: A and B play fundamentally different roles in the adapter and should evolve at different timescales. Setting η_B = λ·η_A with λ=16 yields consistent 1–2% benchmark gains at zero additional compute cost.

## The Problem with Standard LoRA Learning Rates

In LoRA, A is initialized with a Gaussian distribution (random projection, input-side) and B is initialized to zero (output-side, starts contributing nothing). During training, A functions as a feature extractor that adapts the direction in which inputs are projected, while B scales and combines those projected features into the output space. These two roles require different learning dynamics: B must move quickly from zero to useful values while A should update more carefully to preserve the learned projection structure.

## Feature Learning Theory and Maximal Update Parameterization

Maximal update parameterization (muP, Yang et al., 2022) provides a principled framework for setting per-layer learning rates in infinite-width networks. Under muP, 'last-layer' parameters — those closest to the output — should receive a larger learning rate to ensure feature learning (as opposed to lazy training). In LoRA's context, B is the output-proximal matrix and should have a larger LR. A is the input-proximal matrix and benefits from a smaller LR. LoRA+ formalizes this with the ratio η_B/η_A = λ, where λ=16 is the empirically validated default.

## LoRA+ Optimizer Setup

The key implementation detail is creating separate parameter groups for A and B matrices. PyTorch's AdamW optimizer accepts a list of parameter group dictionaries, each with its own learning rate. By iterating over named parameters and routing A-suffix parameters to one group and B-suffix parameters to another, LoRA+ requires only a small wrapper around standard optimizer construction.

```python
import torch
import torch.optim as optim
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM

def create_lora_plus_optimizer(
    model: torch.nn.Module,
    lr_A: float = 1e-4,
    lambda_ratio: float = 16.0,
    weight_decay: float = 0.01,
) -> optim.AdamW:
    """Create AdamW with separate LRs for LoRA A and B matrices."""
    lr_B = lr_A * lambda_ratio
    group_A, group_B, group_other = [], [], []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        if 'lora_A' in name:
            group_A.append(param)
        elif 'lora_B' in name:
            group_B.append(param)
        else:
            group_other.append(param)
    param_groups = [
        {'params': group_A, 'lr': lr_A, 'weight_decay': weight_decay},
        {'params': group_B, 'lr': lr_B, 'weight_decay': weight_decay},
        {'params': group_other, 'lr': lr_A, 'weight_decay': weight_decay},
    ]
    print(f'LoRA+ optimizer: lr_A={lr_A:.2e}, lr_B={lr_B:.2e} (λ={lambda_ratio})')
    print(f'  A params: {len(group_A)}, B params: {len(group_B)}, other: {len(group_other)}')
    return optim.AdamW(param_groups)
```

## LoRA+ Layer Implementation

A self-contained LoRA+ module stores A and B as separate named attributes matching the peft library convention (lora_A, lora_B). The forward pass is identical to standard LoRA — the difference is entirely in the optimizer configuration. The scaling factor α/r is applied to the B·A product to normalize the initialization variance regardless of rank.

```python
import torch
import torch.nn as nn
import math

class LoRAPlusLinear(nn.Module):
    """Linear layer with LoRA+ adapter (separate LR groups for A and B)."""

    def __init__(self, in_features: int, out_features: int, rank: int = 16,
                 alpha: float = 16.0, dropout: float = 0.05):
        super().__init__()
        self.rank = rank
        self.scaling = alpha / rank
        # Base weight frozen
        self.weight = nn.Parameter(torch.randn(out_features, in_features), requires_grad=False)
        self.bias = nn.Parameter(torch.zeros(out_features), requires_grad=False)
        # LoRA adapters: A=Gaussian init, B=zero init
        self.lora_A = nn.Parameter(torch.empty(rank, in_features))
        self.lora_B = nn.Parameter(torch.zeros(out_features, rank))
        nn.init.kaiming_uniform_(self.lora_A, a=math.sqrt(5))
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        base_out = nn.functional.linear(x, self.weight, self.bias)
        lora_out = nn.functional.linear(
            self.dropout(x), self.lora_A
        )  # (batch, rank)
        lora_out = nn.functional.linear(lora_out, self.lora_B)  # (batch, out)
        return base_out + lora_out * self.scaling

    def get_param_groups(self, lr_A: float, lambda_ratio: float = 16.0):
        return [
            {'params': [self.lora_A], 'lr': lr_A},
            {'params': [self.lora_B], 'lr': lr_A * lambda_ratio},
        ]

layer = LoRAPlusLinear(768, 768, rank=16)
x = torch.randn(4, 768)
print(f'Output shape: {layer(x).shape}')
print(f'lora_A shape: {layer.lora_A.shape}, lora_B shape: {layer.lora_B.shape}')
```

## Lambda Sensitivity Analysis

The choice of λ determines the ratio η_B/η_A. Hayou et al. perform a sweep across λ ∈ {1, 2, 4, 8, 16, 32} on commonsense reasoning and math benchmarks. λ=1 is equivalent to standard LoRA. The results show a clear optimum around λ=16 with diminishing returns beyond, and slight degradation at λ=32 due to B moving too fast and overshooting good solutions.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

def lr_ratio_sweep(lambdas=(1, 2, 4, 8, 16, 32), n_steps=200,
                   in_dim=128, out_dim=32, rank=8, seed=42):
    """Sweep LR ratio lambda and measure final validation loss."""
    torch.manual_seed(seed)
    X = torch.randn(512, in_dim)
    y = torch.randint(0, out_dim, (512,))
    loader = DataLoader(TensorDataset(X, y), batch_size=64, shuffle=True)
    results = {}
    for lam in lambdas:
        torch.manual_seed(seed)
        lora_A = nn.Parameter(torch.randn(rank, in_dim) * 0.02)
        lora_B = nn.Parameter(torch.zeros(out_dim, rank))
        base_W = torch.randn(out_dim, in_dim)
        opt = optim.AdamW([
            {'params': [lora_A], 'lr': 1e-3},
            {'params': [lora_B], 'lr': 1e-3 * lam},
        ], weight_decay=0.01)
        criterion = nn.CrossEntropyLoss()
        for step, (xb, yb) in zip(range(n_steps), loader):
            opt.zero_grad()
            out = (xb @ base_W.T) + (xb @ lora_A.T) @ lora_B.T
            loss = criterion(out, yb)
            loss.backward()
            opt.step()
        results[lam] = loss.item()
        print(f'  lambda={lam:>2}: final loss = {loss.item():.4f}')
    best = min(results, key=results.get)
    print(f'Best lambda: {best} (loss={results[best]:.4f})')
    return results

print('LR ratio sweep:')
lr_ratio_sweep()
```

## A vs B Gradient Analysis

To understand why different LRs help, we can track gradient norms and effective update magnitudes for A and B throughout training. With the same LR, B's gradient norm is typically much larger in early training (it starts at zero and needs to catch up), while A's gradient norm is more stable. LoRA+ explicitly compensates by scaling the B update upward, matching what the natural gradient would suggest.

```python
import torch
import torch.nn as nn
import torch.optim as optim

def track_ab_gradients(n_steps=100, rank=16, in_dim=256, out_dim=64, lambda_ratio=16):
    """Track gradient norms and update magnitudes for A and B matrices."""
    lora_A = nn.Parameter(torch.randn(rank, in_dim) * 0.02)
    lora_B = nn.Parameter(torch.zeros(out_dim, rank))
    opt = optim.AdamW([
        {'params': [lora_A], 'lr': 1e-4},
        {'params': [lora_B], 'lr': 1e-4 * lambda_ratio},
    ])
    history = {'grad_A': [], 'grad_B': [], 'norm_A': [], 'norm_B': []}
    for step in range(n_steps):
        x = torch.randn(32, in_dim)
        out = x @ lora_A.T @ lora_B.T
        loss = out.pow(2).mean()
        opt.zero_grad()
        loss.backward()
        if lora_A.grad is not None:
            history['grad_A'].append(lora_A.grad.norm().item())
            history['grad_B'].append(lora_B.grad.norm().item())
        history['norm_A'].append(lora_A.data.norm().item())
        history['norm_B'].append(lora_B.data.norm().item())
        opt.step()
    final = {k: round(v[-1], 5) for k, v in history.items()}
    print(f'Final grad norms  — A: {final["grad_A"]:.5f}, B: {final["grad_B"]:.5f}')
    print(f'Final param norms — A: {final["norm_A"]:.4f}, B: {final["norm_B"]:.4f}')
    return history

track_ab_gradients()
```

## LoRA Learning Rate Strategy Comparison

| Strategy | LR for A | LR for B | Extra Compute | Typical Improvement | Notes |
| --- | --- | --- | --- | --- | --- |
| Standard LoRA | η | η | None | Baseline | Same LR for both; simple but suboptimal |
| LoRA+ (λ=16) | η | 16·η | None | +1–2% on most benchmarks | Recommended default; free performance gain |
| LoRA+ (λ=4) | η | 4·η | None | +0.5–1% | Conservative ratio; lower risk of B instability |
| muP LoRA | η/fan_in | η (last-layer scaled) | None | +1–2% | Full muP transfer: set LR via μP coord check |
| AdaLoRA | Adaptive (SVD) | Adaptive (SVD) | ~20% overhead | +1–3% | Importance-aware rank allocation; more complex |

LoRA+ stacks naturally with DoRA (weight decomposition into magnitude and direction): the direction component maps to A's role and the magnitude component maps to B's role. Setting a higher LR for the magnitude vector (DoRA's equivalent of B) and a lower LR for the directional LoRA matrices is consistent with LoRA+ theory. This combined setup has been reported to outperform either method alone on several instruction-following benchmarks.

> **LoRA+ is a free performance upgrade**: LoRA+ with λ=16 (η_B = 16·η_A) provides 1–2% consistent improvement across tasks with zero additional compute — it's a free performance upgrade that should be the default over standard LoRA in most fine-tuning setups. Simply split your LoRA parameters into two optimizer groups and set the B group's LR 16× higher.

- λ=16 is the most robust default; sensitivity analysis shows little gain beyond λ=16 and risk of instability at λ=32.
- A is initialized with Gaussian noise and adapts feature directions; B starts at zero and adapts output magnitudes.
- muP theory predicts that output-proximal parameters should receive larger LR — LoRA+ is a practical approximation.
- LoRA+ adds no trainable parameters, no forward-pass overhead, and no memory cost beyond two optimizer state partitions.
- Compatible with quantization (QLoRA), DoRA, and gradient checkpointing — no architectural changes required.
- When using peft library, filter named_parameters by 'lora_A' and 'lora_B' suffixes for group separation.

---

