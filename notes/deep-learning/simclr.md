---
title: "SimCLR — Simple Contrastive Learning of Representations"
slug: "simclr"
description: "SimCLR (Chen et al. 2020) learns visual representations by maximizing agreement between two augmented views of the same image via the NT-Xent contrastive loss, a 2-layer MLP projection head, and large batch sizes that supply enough in-batch negatives."
tags: ["deep-learning", "self-supervised-learning", "contrastive-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2ltQ0xSIChTaW1wbGUgRnJhbWV3b3JrIGZvciBDb250cmFzdGl2ZSBMZWFybmluZyBvZiBWaXN1YWwgUmVwcmVzZW50YXRpb25zLCBDaGVuIGV0IGFsLiAyMDIwKSBzaG93ZWQgdGhhdCBzZWxmLXN1cGVydmlzZWQgY29udHJhc3RpdmUgbGVhcm5pbmcgY291bGQgcml2YWwgc3VwZXJ2aXNlZCBJbWFnZU5ldCBwcmUtdHJhaW5pbmcuIFRoZSBrZXkgaW5zaWdodCBpcyBlbGVnYW50OiBhdWdtZW50IGVhY2ggaW1hZ2UgdHdpY2UsIGVuY29kZSBib3RoIHZpZXdzIHdpdGggYSBzaGFyZWQgUmVzTmV0LCBwcm9qZWN0IHRoZSByZXByZXNlbnRhdGlvbnMgd2l0aCBhIHNtYWxsIE1MUCwgYW5kIHRoZW4gdHJhaW4gdGhlIGVuY29kZXIgdG8gbWF4aW1pc2UgYWdyZWVtZW50IGJldHdlZW4gdGhlIHR3byB2aWV3cyB3aGlsZSB0cmVhdGluZyBhbGwgb3RoZXIgaW1hZ2VzIGluIHRoZSBiYXRjaCBhcyBuZWdhdGl2ZXMuIE5vIGxhYmVscyByZXF1aXJlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb250cmFzdGl2ZSBMZWFybmluZyBGcmFtZXdvcmsifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIG1pbmktYmF0Y2ggb2YgTiBpbWFnZXMsIFNpbUNMUiBnZW5lcmF0ZXMgMk4gYXVnbWVudGVkIHZpZXdzIGJ5IGFwcGx5aW5nIHR3byBpbmRlcGVuZGVudCBzdG9jaGFzdGljIGF1Z21lbnRhdGlvbiBzZXF1ZW5jZXMgdG8gZWFjaCBpbWFnZS4gVGhlIGVuY29kZXIgZiAoYSBSZXNOZXQpIG1hcHMgZWFjaCB2aWV3IHjhtaIgdG8gYSByZXByZXNlbnRhdGlvbiBo4bWiID0gZih44bWiKS4gQSB0d28tbGF5ZXIgTUxQIHByb2plY3Rpb24gaGVhZCBnIG1hcHMgaOG1oiB0byB64bWiID0gZyho4bWiKSwgd2hpY2ggaXMgTDItbm9ybWFsaXNlZCBiZWZvcmUgdGhlIGxvc3MgaXMgY29tcHV0ZWQuIFRoZSBjb250cmFzdGl2ZSBsb3NzIGlzIGNvbXB1dGVkIGluIHRoZSB6LXNwYWNlOyBpbXBvcnRhbnRseSwgZG93bnN0cmVhbSB0YXNrcyB1c2UgaOG1oiAodGhlIGVuY29kZXIgb3V0cHV0IGJlZm9yZSBwcm9qZWN0aW9uKSwgbm90IHrhtaIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTlQtWGVudCBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgTlQtWGVudCAoTm9ybWFsaXNlZCBUZW1wZXJhdHVyZS1zY2FsZWQgQ3Jvc3MgRW50cm9weSkgbG9zcyBmb3IgYSBwb3NpdGl2ZSBwYWlyIChpLCBqKSBmcm9tIHRoZSBzYW1lIGltYWdlIGlzOiBMX3tpLGp9ID0gLWxvZ1sgZXhwKHNpbSh64bWiLHrisbwpL8+EKSAvIM6jX3tr4omgaX0gZXhwKHNpbSh64bWiLHrigpYpL8+EKSBdIHdoZXJlIHNpbSh1LHYpID0gdeG1gHYvKOKAlnXigJbigJZ24oCWKSBpcyBjb3NpbmUgc2ltaWxhcml0eSBhbmQgz4QgaXMgYSB0ZW1wZXJhdHVyZSBoeXBlcnBhcmFtZXRlciAoZGVmYXVsdCAwLjA3KS4gVGhlIGRlbm9taW5hdG9yIHN1bXMgb3ZlciBhbGwgMihOLTEpIG90aGVyIHZpZXdzIGluIHRoZSBiYXRjaCDigJQgYm90aCBhdWdtZW50YXRpb25zIG9mIG90aGVyIGltYWdlcyDigJQgbWFraW5nIHRoZW0gdGhlIG5lZ2F0aXZlcy4gVGhlIGZpbmFsIGxvc3MgaXMgdGhlIG1lYW4gb3ZlciBhbGwgMk4gb3JkZXJlZCBwYWlycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBudF94ZW50X2xvc3MoejEsIHoyLCB0ZW1wZXJhdHVyZT0wLjA3KTpcbiAgICBcIlwiXCJOVC1YZW50IGxvc3MgZm9yIFNpbUNMUi5cbiAgICB6MSwgejI6IChOLCBEKSBMMi1ub3JtYWxpc2VkIGVtYmVkZGluZ3MgZnJvbSB0d28gYXVnbWVudGVkIHZpZXdzLlxuICAgIFJldHVybnMgc2NhbGFyIGxvc3MuXG4gICAgXCJcIlwiXG4gICAgTiA9IHoxLnNpemUoMClcbiAgICAjIENvbmNhdGVuYXRlIHJlcHJlc2VudGF0aW9uczogW3oxXzAsIHoxXzEsIC4uLiwgejJfMCwgejJfMSwgLi4uXVxuICAgIHogPSB0b3JjaC5jYXQoW3oxLCB6Ml0sIGRpbT0wKSAgICAgICAgICAjICgyTiwgRClcbiAgICAjIENvc2luZSBzaW1pbGFyaXR5IG1hdHJpeCBmb3IgYWxsIHBhaXJzXG4gICAgc2ltID0gRi5jb3NpbmVfc2ltaWxhcml0eSh6LnVuc3F1ZWV6ZSgxKSwgei51bnNxdWVlemUoMCksIGRpbT0yKSAgIyAoMk4sIDJOKVxuICAgIHNpbSA9IHNpbSAvIHRlbXBlcmF0dXJlXG4gICAgIyBNYXNrIG91dCBzZWxmLXNpbWlsYXJpdHkgb24gdGhlIGRpYWdvbmFsXG4gICAgbWFza19zZWxmID0gdG9yY2guZXllKDIgKiBOLCBkdHlwZT10b3JjaC5ib29sLCBkZXZpY2U9ei5kZXZpY2UpXG4gICAgc2ltLm1hc2tlZF9maWxsXyhtYXNrX3NlbGYsIGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpKVxuICAgICMgUG9zaXRpdmUgcGFpcnM6IChpLCBpK04pIGFuZCAoaStOLCBpKVxuICAgIGxhYmVscyA9IHRvcmNoLmNhdChbdG9yY2guYXJhbmdlKE4sIDIqTiksIHRvcmNoLmFyYW5nZShOKV0pLnRvKHouZGV2aWNlKVxuICAgIGxvc3MgPSBGLmNyb3NzX2VudHJvcHkoc2ltLCBsYWJlbHMpXG4gICAgcmV0dXJuIGxvc3NcblxuIyBRdWljayBzYW5pdHkgY2hlY2tcbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuejEgPSBGLm5vcm1hbGl6ZSh0b3JjaC5yYW5kbigzMiwgMTI4KSwgZGltPTEpXG56MiA9IEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKDMyLCAxMjgpLCBkaW09MSlcbnByaW50KFx1MDAyN05ULVhlbnQgbG9zcyAocmFuZG9tLCBzaG91bGQgYmUgfmxvZyg2MykpOlx1MDAyNywgbnRfeGVudF9sb3NzKHoxLCB6MikuaXRlbSgpKVxuIyBQZXJmZWN0IGFncmVlbWVudCBzaG91bGQgZ2l2ZSBsb3NzIG5lYXIgemVyb1xuejJfcGVyZmVjdCA9IHoxLmNsb25lKClcbnByaW50KFx1MDAyN05ULVhlbnQgbG9zcyAocGVyZmVjdCBhZ3JlZW1lbnQpOlx1MDAyNywgbnRfeGVudF9sb3NzKHoxLCB6Ml9wZXJmZWN0KS5pdGVtKCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGF0YSBBdWdtZW50YXRpb24gUGlwZWxpbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBhdWdtZW50YXRpb24gc3RyYXRlZ3kgaXMgb25lIG9mIHRoZSBtb3N0IGNyaXRpY2FsIGNvbXBvbmVudHMgb2YgU2ltQ0xSLiBBbiBhYmxhdGlvbiBzdHVkeSBpbiB0aGUgcGFwZXIgc2hvd2VkIHRoYXQgcmFuZG9tIGNyb3BwaW5nIChyZXNpemVkIGNyb3ApIGFsb25lIHByb3ZpZGVzIHRoZSBtb3N0IGJlbmVmaXQsIGZvbGxvd2VkIGJ5IGNvbG9yIGppdHRlci4gVGhlIGludHVpdGlvbiBpcyB0aGF0IGEgY3JvcCBmb3JjZXMgdGhlIG5ldHdvcmsgdG8gbGVhcm4gY29udGVudCByYXRoZXIgdGhhbiBwb3NpdGlvbiBvciBzcGF0aWFsIGxheW91dC4gQ29sb3Igaml0dGVyIHByZXZlbnRzIHRoZSBuZXR3b3JrIGZyb20gdXNpbmcgY29sb3Igc3RhdGlzdGljcyBhcyBhIHNob3J0Y3V0LiBHYXVzc2lhbiBibHVyIChhcHBsaWVkIHdpdGggNTAlIHByb2JhYmlsaXR5KSBlbmNvdXJhZ2VzIHJvYnVzdG5lc3MgdG8gZnJlcXVlbmN5IGNvbnRlbnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgdHJhbnNmb3Jtc1xuXG5jbGFzcyBTaW1DTFJBdWdtZW50YXRpb246XG4gICAgXCJcIlwiVHdvLXZpZXcgYXVnbWVudGF0aW9uIGZvciBTaW1DTFIuIFJldHVybnMgYSBwYWlyICh2aWV3MSwgdmlldzIpIHBlciBpbWFnZS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW1hZ2Vfc2l6ZT0yMjQsIHM9MS4wKTpcbiAgICAgICAgY29sb3Jfaml0dGVyID0gdHJhbnNmb3Jtcy5Db2xvckppdHRlcihcbiAgICAgICAgICAgIGJyaWdodG5lc3M9MC44ICogcyxcbiAgICAgICAgICAgIGNvbnRyYXN0PTAuOCAqIHMsXG4gICAgICAgICAgICBzYXR1cmF0aW9uPTAuOCAqIHMsXG4gICAgICAgICAgICBodWU9MC4yICogc1xuICAgICAgICApXG4gICAgICAgIHNlbGYudHJhbnNmb3JtID0gdHJhbnNmb3Jtcy5Db21wb3NlKFtcbiAgICAgICAgICAgIHRyYW5zZm9ybXMuUmFuZG9tUmVzaXplZENyb3AoaW1hZ2Vfc2l6ZSwgc2NhbGU9KDAuMiwgMS4wKSksICAjIG1vc3QgaW1wb3J0YW50XG4gICAgICAgICAgICB0cmFuc2Zvcm1zLlJhbmRvbUhvcml6b250YWxGbGlwKHA9MC41KSxcbiAgICAgICAgICAgIHRyYW5zZm9ybXMuUmFuZG9tQXBwbHkoW2NvbG9yX2ppdHRlcl0sIHA9MC44KSxcbiAgICAgICAgICAgIHRyYW5zZm9ybXMuUmFuZG9tR3JheXNjYWxlKHA9MC4yKSxcbiAgICAgICAgICAgIHRyYW5zZm9ybXMuUmFuZG9tQXBwbHkoW3RyYW5zZm9ybXMuR2F1c3NpYW5CbHVyKGtlcm5lbF9zaXplPTIzKV0sIHA9MC41KSxcbiAgICAgICAgICAgIHRyYW5zZm9ybXMuVG9UZW5zb3IoKSxcbiAgICAgICAgICAgIHRyYW5zZm9ybXMuTm9ybWFsaXplKG1lYW49WzAuNDg1LCAwLjQ1NiwgMC40MDZdLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RkPVswLjIyOSwgMC4yMjQsIDAuMjI1XSksXG4gICAgICAgIF0pXG5cbiAgICBkZWYgX19jYWxsX18oc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLnRyYW5zZm9ybSh4KSwgc2VsZi50cmFuc2Zvcm0oeClcblxuIyBVc2FnZSB3aXRoIERhdGFMb2FkZXJcbiMgZGF0YXNldCA9IEltYWdlRm9sZGVyKHJvb3QsIHRyYW5zZm9ybT1TaW1DTFJBdWdtZW50YXRpb24oMjI0KSlcbiMgRWFjaCBiYXRjaCBnaXZlczogKHZpZXcxX2JhdGNoLCB2aWV3Ml9iYXRjaCksIGxhYmVsc1xucHJpbnQoXHUwMDI3U2ltQ0xSIGF1Z21lbnRhdGlvbiBwaXBlbGluZSBkZWZpbmVkLlx1MDAyNylcbnByaW50KFx1MDAyN0tleTogUmFuZG9tUmVzaXplZENyb3Aoc2NhbGU9MC4yLTEuMCkgaXMgdGhlIG1vc3QgaW1wb3J0YW50IGF1Z21lbnRhdGlvbi5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2ltQ0xSIFRyYWluaW5nIExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNpbUNMUiByZXF1aXJlcyBubyBzcGVjaWFsIGFyY2hpdGVjdHVyZSBiZXlvbmQgYSBzdGFuZGFyZCBSZXNOZXQgZW5jb2RlciBhbmQgYSBzbWFsbCBNTFAgcHJvamVjdGlvbiBoZWFkLiBUaGUgcHJvamVjdGlvbiBoZWFkICh0d28gbGluZWFyIGxheWVycyB3aXRoIEJhdGNoTm9ybSBhbmQgUmVMVSkgaXMgb25seSB1c2VkIGR1cmluZyBwcmUtdHJhaW5pbmc7IGl0IGlzIGRpc2NhcmRlZCBmb3IgZG93bnN0cmVhbSB0YXNrcy4gQSBsYXJnZSBiYXRjaCBzaXplICg0MDk24oCTODE5MikgaXMgY3JpdGljYWwgYmVjYXVzZSB0aGUgbnVtYmVyIG9mIGluLWJhdGNoIG5lZ2F0aXZlcyBkZXRlcm1pbmVzIGhvdyBpbmZvcm1hdGl2ZSB0aGUgbG9zcyBzaWduYWwgaXMuIExBUlMgb3B0aW1pc2VyIGlzIHJlY29tbWVuZGVkIGF0IHRoZXNlIGJhdGNoIHNpemVzIGR1ZSB0byBpdHMgbGF5ZXItd2lzZSBhZGFwdGl2ZSBsZWFybmluZyByYXRlIHNjYWxpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgdG9yY2h2aXNpb24ubW9kZWxzIGFzIG1vZGVsc1xuXG5jbGFzcyBTaW1DTFIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmFja2JvbmU9XHUwMDI3cmVzbmV0NTBcdTAwMjcsIHByb2pfZGltPTEyOCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBiYXNlID0gbW9kZWxzLnJlc25ldDUwKHdlaWdodHM9Tm9uZSlcbiAgICAgICAgc2VsZi5lbmNvZGVyID0gbm4uU2VxdWVudGlhbCgqbGlzdChiYXNlLmNoaWxkcmVuKCkpWzotMV0pICAjIHJlbW92ZSBmY1xuICAgICAgICBmZWF0X2RpbSA9IGJhc2UuZmMuaW5fZmVhdHVyZXMgICMgMjA0OCBmb3IgUmVzTmV0LTUwXG4gICAgICAgIHNlbGYucHJvamVjdG9yID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihmZWF0X2RpbSwgZmVhdF9kaW0pLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMWQoZmVhdF9kaW0pLFxuICAgICAgICAgICAgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGZlYXRfZGltLCBwcm9qX2RpbSksXG4gICAgICAgIClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgxLCB4Mik6XG4gICAgICAgIGgxID0gc2VsZi5lbmNvZGVyKHgxKS5mbGF0dGVuKDEpICAjIChOLCAyMDQ4KVxuICAgICAgICBoMiA9IHNlbGYuZW5jb2Rlcih4MikuZmxhdHRlbigxKVxuICAgICAgICB6MSA9IEYubm9ybWFsaXplKHNlbGYucHJvamVjdG9yKGgxKSwgZGltPTEpICAjIChOLCAxMjgpXG4gICAgICAgIHoyID0gRi5ub3JtYWxpemUoc2VsZi5wcm9qZWN0b3IoaDIpLCBkaW09MSlcbiAgICAgICAgcmV0dXJuIHoxLCB6MiwgaDEsIGgyICAjIHJldHVybiBoIGZvciBkb3duc3RyZWFtIHVzZVxuXG4jIFRyYWluaW5nIHN0ZXAgKGluc2lkZSBlcG9jaCBsb29wKVxuZGVmIHRyYWluX3N0ZXAobW9kZWwsIGJhdGNoLCBvcHRpbWl6ZXIsIHRlbXBlcmF0dXJlPTAuMDcpOlxuICAgICh2aWV3MSwgdmlldzIpLCBfID0gYmF0Y2hcbiAgICB2aWV3MSwgdmlldzIgPSB2aWV3MS5jdWRhKCksIHZpZXcyLmN1ZGEoKVxuICAgIHoxLCB6MiwgXywgXyA9IG1vZGVsKHZpZXcxLCB2aWV3MilcbiAgICBsb3NzID0gbnRfeGVudF9sb3NzKHoxLCB6MiwgdGVtcGVyYXR1cmUpXG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgb3B0aW1pemVyLnN0ZXAoKVxuICAgIHJldHVybiBsb3NzLml0ZW0oKVxuXG5tb2RlbCA9IFNpbUNMUigpLmN1ZGEoKVxucHJpbnQoXHUwMDI3RW5jb2RlciBvdXRwdXQgZGltOlx1MDAyNywgMjA0OClcbnByaW50KFx1MDAyN1Byb2plY3RvciBvdXRwdXQgZGltOlx1MDAyNywgMTI4KVxucHJpbnQoXHUwMDI3UGFyYW1ldGVyczpcdTAwMjcsIHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKSAvLyAxXzAwMF8wMDAsIFx1MDAyN01cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGluZWFyIEV2YWx1YXRpb24gUHJvdG9jb2wifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIGV2YWx1YXRlIHJlcHJlc2VudGF0aW9uIHF1YWxpdHksIFNpbUNMUiB1c2VzIGxpbmVhciBldmFsdWF0aW9uOiBmcmVlemUgdGhlIHByZS10cmFpbmVkIGVuY29kZXIgYW5kIHRyYWluIGEgc2luZ2xlIGxpbmVhciBjbGFzc2lmaWVyIG9uIHRvcCBvZiB0aGUgZnJvemVuIHJlcHJlc2VudGF0aW9ucy4gVGhpcyBpc29sYXRlcyB0aGUgcmVwcmVzZW50YXRpb24gcXVhbGl0eSBmcm9tIHRoZSBsaW5lYXIgaGVhZFx1MDAyN3MgY2FwYWNpdHkuIEEgaGlnaCBsaW5lYXIgZXZhbHVhdGlvbiBhY2N1cmFjeSBpbmRpY2F0ZXMgdGhlIGVuY29kZXIgaGFzIGxlYXJuZWQgc2VtYW50aWNhbGx5IG1lYW5pbmdmdWwgZmVhdHVyZXMuIFRoZSBlbmNvZGVyXHUwMDI3cyBvdXRwdXQgKGJlZm9yZSBwcm9qZWN0aW9uKSBpcyB1c2VkOyB0aGlzIGlzIHdoeSB0aGUgcHJvamVjdGlvbiBoZWFkIG11c3QgYmUgZGlzY2FyZGVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaC51dGlscy5kYXRhIGltcG9ydCBEYXRhTG9hZGVyXG5mcm9tIHRvcmNodmlzaW9uIGltcG9ydCBkYXRhc2V0cywgdHJhbnNmb3Jtc1xuXG5kZWYgbGluZWFyX2V2YWx1YXRpb24oZW5jb2RlciwgdHJhaW5fbG9hZGVyLCB2YWxfbG9hZGVyLCBudW1fY2xhc3Nlcz0xMDAwLFxuICAgICAgICAgICAgICAgICAgICAgICBlcG9jaHM9MTAwLCBscj0wLjEsIGRldmljZT1cdTAwMjdjdWRhXHUwMDI3KTpcbiAgICBcIlwiXCJGcmVlemUgZW5jb2RlciwgdHJhaW4gYW5kIGV2YWx1YXRlIGEgbGluZWFyIGNsYXNzaWZpZXIuXCJcIlwiXG4gICAgZW5jb2Rlci5ldmFsKClcbiAgICBmb3IgcCBpbiBlbmNvZGVyLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgcC5yZXF1aXJlc19ncmFkXyhGYWxzZSlcblxuICAgICMgRGV0ZXJtaW5lIGZlYXR1cmUgZGltZW5zaW9uIGZyb20gYSBkdW1teSBmb3J3YXJkIHBhc3NcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZHVtbXkgPSB0b3JjaC5yYW5kbigyLCAzLCAyMjQsIDIyNCkudG8oZGV2aWNlKVxuICAgICAgICBmZWF0X2RpbSA9IGVuY29kZXIoZHVtbXkpLmZsYXR0ZW4oMSkuc2l6ZSgxKVxuXG4gICAgY2xhc3NpZmllciA9IG5uLkxpbmVhcihmZWF0X2RpbSwgbnVtX2NsYXNzZXMpLnRvKGRldmljZSlcbiAgICBvcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5TR0QoY2xhc3NpZmllci5wYXJhbWV0ZXJzKCksIGxyPWxyLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtb21lbnR1bT0wLjksIHdlaWdodF9kZWNheT0wLjApXG4gICAgc2NoZWR1bGVyID0gdG9yY2gub3B0aW0ubHJfc2NoZWR1bGVyLkNvc2luZUFubmVhbGluZ0xSKG9wdGltaXplciwgZXBvY2hzKVxuICAgIGNyaXRlcmlvbiA9IG5uLkNyb3NzRW50cm9weUxvc3MoKVxuXG4gICAgZm9yIGVwb2NoIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIGNsYXNzaWZpZXIudHJhaW4oKVxuICAgICAgICBmb3IgaW1ncywgbGFiZWxzIGluIHRyYWluX2xvYWRlcjpcbiAgICAgICAgICAgIGltZ3MsIGxhYmVscyA9IGltZ3MudG8oZGV2aWNlKSwgbGFiZWxzLnRvKGRldmljZSlcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIGZlYXRzID0gZW5jb2RlcihpbWdzKS5mbGF0dGVuKDEpXG4gICAgICAgICAgICBsb2dpdHMgPSBjbGFzc2lmaWVyKGZlYXRzKVxuICAgICAgICAgICAgbG9zcyA9IGNyaXRlcmlvbihsb2dpdHMsIGxhYmVscylcbiAgICAgICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgIHNjaGVkdWxlci5zdGVwKClcblxuICAgICMgVmFsaWRhdGlvbiBhY2N1cmFjeVxuICAgIGNsYXNzaWZpZXIuZXZhbCgpXG4gICAgY29ycmVjdCA9IHRvdGFsID0gMFxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgaW1ncywgbGFiZWxzIGluIHZhbF9sb2FkZXI6XG4gICAgICAgICAgICBpbWdzLCBsYWJlbHMgPSBpbWdzLnRvKGRldmljZSksIGxhYmVscy50byhkZXZpY2UpXG4gICAgICAgICAgICBmZWF0cyA9IGVuY29kZXIoaW1ncykuZmxhdHRlbigxKVxuICAgICAgICAgICAgcHJlZHMgPSBjbGFzc2lmaWVyKGZlYXRzKS5hcmdtYXgoMSlcbiAgICAgICAgICAgIGNvcnJlY3QgKz0gKHByZWRzID09IGxhYmVscykuc3VtKCkuaXRlbSgpXG4gICAgICAgICAgICB0b3RhbCArPSBsYWJlbHMuc2l6ZSgwKVxuICAgIHJldHVybiBjb3JyZWN0IC8gdG90YWxcblxucHJpbnQoXHUwMDI3TGluZWFyIGV2YWx1YXRpb24gcHJvdG9jb2w6IGZyZWV6ZSBlbmNvZGVyLCB0cmFpbiBsaW5lYXIgaGVhZCBvbmx5Llx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IlByb2plY3Rpb24gSGVhZCBNYXR0ZXJzIOKAlCBVc2UgRW5jb2RlciBPdXRwdXQgRG93bnN0cmVhbSIsImNvbnRlbnQiOiJBIGNyaXRpY2FsIGZpbmRpbmcgb2YgU2ltQ0xSIGlzIHRoYXQgdGhlIHByb2plY3Rpb24gaGVhZCAoZykgaW1wcm92ZXMgY29udHJhc3RpdmUgbGVhcm5pbmcgYnV0IHRoZSByZXByZXNlbnRhdGlvbiBiZWZvcmUgdGhlIHByb2plY3Rpb24gaGVhZCAoaCkgaXMgYmV0dGVyIGZvciBkb3duc3RyZWFtIHRhc2tzLiBUaGUgcHJvamVjdGlvbiBoZWFkIGNvbGxhcHNlcyBpbmZvcm1hdGlvbiB0aGF0IGlzIHVzZWZ1bCBmb3IgY2xhc3NpZmljYXRpb24gYnV0IG5vdCBmb3IgY29udHJhc3RpdmUgbG9zcy4gQWx3YXlzIGZyZWV6ZSB0aGUgZW5jb2RlciBhbmQgZGlzY2FyZCB0aGUgcHJvamVjdGlvbiBoZWFkIHdoZW4gcGVyZm9ybWluZyBsaW5lYXIgZXZhbHVhdGlvbiBvciBmaW5lLXR1bmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW1wZXJhdHVyZSBhbmQgQmF0Y2ggU2l6ZSBTZW5zaXRpdml0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGVtcGVyYXR1cmUgz4QgY29udHJvbHMgdGhlIGNvbmNlbnRyYXRpb24gb2YgdGhlIGRpc3RyaWJ1dGlvbi4gTG93IM+EIChlLmcuLCAwLjA3KSBjcmVhdGVzIGEgc2hhcnBlciBkaXN0cmlidXRpb24sIHBlbmFsaXNpbmcgaGFyZCBuZWdhdGl2ZXMgbW9yZS4gSGlnaCDPhCB0cmVhdHMgbmVnYXRpdmVzIG1vcmUgdW5pZm9ybWx5LiBCYXRjaCBzaXplIGlzIGEgcHJveHkgZm9yIHRoZSBudW1iZXIgb2YgbmVnYXRpdmVzOiBhdCBiYXRjaCBzaXplIE4sIHRoZXJlIGFyZSAyKE4tMSkgbmVnYXRpdmVzIHBlciBhbmNob3IuIFNpbUNMUiBuZWVkcyA0MDk24oCTODE5MiBpbWFnZXMgcGVyIGJhdGNoIHRvIGFjY3VtdWxhdGUgZW5vdWdoIG5lZ2F0aXZlcy4gVGhpcyByZXF1aXJlcyBlaXRoZXIgbWFueSBHUFVzIG9yIGdyYWRpZW50IGFjY3VtdWxhdGlvbiwgbWFraW5nIGl0IGV4cGVuc2l2ZSBjb21wYXJlZCB0byBxdWV1ZS1iYXNlZCBtZXRob2RzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiz4QgPSAwLjA3IG9wdGltYWwgYWNyb3NzIGV4cGVyaW1lbnRzIOKAlCB0b28gbG93IGNhdXNlcyBpbnN0YWJpbGl0eSwgdG9vIGhpZ2ggZGVncmFkZXMgcXVhbGl0eS4iLCJCYXRjaCBzaXplIDQwOTYgd2l0aCBMQVJTIG9wdGltaXplciBhbmQgY29zaW5lIGRlY2F5IG92ZXIgMTAw4oCTMTAwMCBlcG9jaHMuIiwiUmFuZG9tIHJlc2l6ZWQgY3JvcCBpcyB0aGUgc2luZ2xlIG1vc3QgaW1wb3J0YW50IGF1Z21lbnRhdGlvbiAoXHUwMDNlMTAlIHRvcC0xIGRpZmZlcmVuY2UpLiIsIkNvbG9yIGppdHRlciArIHJhbmRvbSBncmF5c2NhbGUgcHJldmVudHMgcmVsaWFuY2Ugb24gY29sb3Igc3RhdGlzdGljcyBhcyBhIGNoZWF0IGNvZGUuIiwiUmVtb3ZpbmcgR2F1c3NpYW4gYmx1ciBmcm9tIHRoZSBwaXBlbGluZSBjYXVzZXMgfjHigJMyJSB0b3AtMSByZWdyZXNzaW9uLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaW1DTFIgdjIgYW5kIEV4dGVuc2lvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNpbUNMUiB2MiAoQ2hlbiBldCBhbC4gMjAyMGIpIGludHJvZHVjZWQgdGhyZWUgaW1wcm92ZW1lbnRzOiAoMSkgYSBsYXJnZXIgYmFja2JvbmUgKFJlc05ldC0xNTIgd2l0aCBzZWxlY3RpdmUga2VybmVscyksICgyKSBhIGRlZXBlciBwcm9qZWN0aW9uIGhlYWQgKDMtbGF5ZXIgTUxQIGluc3RlYWQgb2YgMi1sYXllciksIGFuZCAoMykgc2VtaS1zdXBlcnZpc2VkIGxlYXJuaW5nIHdpdGggZGlzdGlsbGF0aW9uIOKAlCB1c2UgdGhlIHNlbGYtc3VwZXJ2aXNlZCBtb2RlbCB0byBnZW5lcmF0ZSBwc2V1ZG8tbGFiZWxzIG9uIHVubGFiZWxsZWQgZGF0YSBhbmQgZGlzdGlsIGludG8gYSBzbWFsbGVyIHN0dWRlbnQuIFRoZXNlIGltcHJvdmVtZW50cyBwdXNoZWQgdG9wLTEgYWNjdXJhY3kgYmV5b25kIDc5JSBvbiBJbWFnZU5ldCB3aXRoIG9ubHkgMSUgb2YgbGFiZWxzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJCYXRjaCBTaXplIiwiTmVnYXRpdmVzIE5lZWRlZCIsIlByb2plY3Rpb24gTGF5ZXJzIiwiTGluZWFyIEV2YWwgVG9wLTEiXSwicm93cyI6W1siU2ltQ0xSIHYxIiwiNDA5NiIsIlllcyAoaW4tYmF0Y2gpIiwiMi1sYXllciBNTFAiLCI2OS4zJSJdLFsiU2ltQ0xSIHYyIiwiNDA5NiIsIlllcyAoaW4tYmF0Y2gpIiwiMy1sYXllciBNTFAiLCI3NC4yJSJdLFsiQllPTCIsIjQwOTYiLCJObyIsIjItbGF5ZXIgTUxQIiwiNzQuMyUiXSxbIk1vQ28gdjMiLCI0MDk2IiwiTm8gKGxhcmdlIGJhdGNoIFZpVCkiLCIyLWxheWVyIE1MUCIsIjgzLjIlIChWaVQtQi8xNikiXV19XQ=="
---
# SimCLR — Simple Contrastive Learning of Representations

SimCLR (Simple Framework for Contrastive Learning of Visual Representations, Chen et al. 2020) showed that self-supervised contrastive learning could rival supervised ImageNet pre-training. The key insight is elegant: augment each image twice, encode both views with a shared ResNet, project the representations with a small MLP, and then train the encoder to maximise agreement between the two views while treating all other images in the batch as negatives. No labels required.

## Contrastive Learning Framework

For a mini-batch of N images, SimCLR generates 2N augmented views by applying two independent stochastic augmentation sequences to each image. The encoder f (a ResNet) maps each view xᵢ to a representation hᵢ = f(xᵢ). A two-layer MLP projection head g maps hᵢ to zᵢ = g(hᵢ), which is L2-normalised before the loss is computed. The contrastive loss is computed in the z-space; importantly, downstream tasks use hᵢ (the encoder output before projection), not zᵢ.

## NT-Xent Loss

The NT-Xent (Normalised Temperature-scaled Cross Entropy) loss for a positive pair (i, j) from the same image is: L_{i,j} = -log[ exp(sim(zᵢ,zⱼ)/τ) / Σ_{k≠i} exp(sim(zᵢ,zₖ)/τ) ] where sim(u,v) = uᵀv/(‖u‖‖v‖) is cosine similarity and τ is a temperature hyperparameter (default 0.07). The denominator sums over all 2(N-1) other views in the batch — both augmentations of other images — making them the negatives. The final loss is the mean over all 2N ordered pairs.

```python
import torch
import torch.nn.functional as F

def nt_xent_loss(z1, z2, temperature=0.07):
    """NT-Xent loss for SimCLR.
    z1, z2: (N, D) L2-normalised embeddings from two augmented views.
    Returns scalar loss.
    """
    N = z1.size(0)
    # Concatenate representations: [z1_0, z1_1, ..., z2_0, z2_1, ...]
    z = torch.cat([z1, z2], dim=0)          # (2N, D)
    # Cosine similarity matrix for all pairs
    sim = F.cosine_similarity(z.unsqueeze(1), z.unsqueeze(0), dim=2)  # (2N, 2N)
    sim = sim / temperature
    # Mask out self-similarity on the diagonal
    mask_self = torch.eye(2 * N, dtype=torch.bool, device=z.device)
    sim.masked_fill_(mask_self, float('-inf'))
    # Positive pairs: (i, i+N) and (i+N, i)
    labels = torch.cat([torch.arange(N, 2*N), torch.arange(N)]).to(z.device)
    loss = F.cross_entropy(sim, labels)
    return loss

# Quick sanity check
torch.manual_seed(42)
z1 = F.normalize(torch.randn(32, 128), dim=1)
z2 = F.normalize(torch.randn(32, 128), dim=1)
print('NT-Xent loss (random, should be ~log(63)):', nt_xent_loss(z1, z2).item())
# Perfect agreement should give loss near zero
z2_perfect = z1.clone()
print('NT-Xent loss (perfect agreement):', nt_xent_loss(z1, z2_perfect).item())
```

## Data Augmentation Pipeline

The augmentation strategy is one of the most critical components of SimCLR. An ablation study in the paper showed that random cropping (resized crop) alone provides the most benefit, followed by color jitter. The intuition is that a crop forces the network to learn content rather than position or spatial layout. Color jitter prevents the network from using color statistics as a shortcut. Gaussian blur (applied with 50% probability) encourages robustness to frequency content.

```python
import torch
from torchvision import transforms

class SimCLRAugmentation:
    """Two-view augmentation for SimCLR. Returns a pair (view1, view2) per image."""
    def __init__(self, image_size=224, s=1.0):
        color_jitter = transforms.ColorJitter(
            brightness=0.8 * s,
            contrast=0.8 * s,
            saturation=0.8 * s,
            hue=0.2 * s
        )
        self.transform = transforms.Compose([
            transforms.RandomResizedCrop(image_size, scale=(0.2, 1.0)),  # most important
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomApply([color_jitter], p=0.8),
            transforms.RandomGrayscale(p=0.2),
            transforms.RandomApply([transforms.GaussianBlur(kernel_size=23)], p=0.5),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225]),
        ])

    def __call__(self, x):
        return self.transform(x), self.transform(x)

# Usage with DataLoader
# dataset = ImageFolder(root, transform=SimCLRAugmentation(224))
# Each batch gives: (view1_batch, view2_batch), labels
print('SimCLR augmentation pipeline defined.')
print('Key: RandomResizedCrop(scale=0.2-1.0) is the most important augmentation.')
```

## SimCLR Training Loop

SimCLR requires no special architecture beyond a standard ResNet encoder and a small MLP projection head. The projection head (two linear layers with BatchNorm and ReLU) is only used during pre-training; it is discarded for downstream tasks. A large batch size (4096–8192) is critical because the number of in-batch negatives determines how informative the loss signal is. LARS optimiser is recommended at these batch sizes due to its layer-wise adaptive learning rate scaling.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

class SimCLR(nn.Module):
    def __init__(self, backbone='resnet50', proj_dim=128):
        super().__init__()
        base = models.resnet50(weights=None)
        self.encoder = nn.Sequential(*list(base.children())[:-1])  # remove fc
        feat_dim = base.fc.in_features  # 2048 for ResNet-50
        self.projector = nn.Sequential(
            nn.Linear(feat_dim, feat_dim),
            nn.BatchNorm1d(feat_dim),
            nn.ReLU(inplace=True),
            nn.Linear(feat_dim, proj_dim),
        )

    def forward(self, x1, x2):
        h1 = self.encoder(x1).flatten(1)  # (N, 2048)
        h2 = self.encoder(x2).flatten(1)
        z1 = F.normalize(self.projector(h1), dim=1)  # (N, 128)
        z2 = F.normalize(self.projector(h2), dim=1)
        return z1, z2, h1, h2  # return h for downstream use

# Training step (inside epoch loop)
def train_step(model, batch, optimizer, temperature=0.07):
    (view1, view2), _ = batch
    view1, view2 = view1.cuda(), view2.cuda()
    z1, z2, _, _ = model(view1, view2)
    loss = nt_xent_loss(z1, z2, temperature)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss.item()

model = SimCLR().cuda()
print('Encoder output dim:', 2048)
print('Projector output dim:', 128)
print('Parameters:', sum(p.numel() for p in model.parameters()) // 1_000_000, 'M')
```

## Linear Evaluation Protocol

To evaluate representation quality, SimCLR uses linear evaluation: freeze the pre-trained encoder and train a single linear classifier on top of the frozen representations. This isolates the representation quality from the linear head's capacity. A high linear evaluation accuracy indicates the encoder has learned semantically meaningful features. The encoder's output (before projection) is used; this is why the projection head must be discarded.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def linear_evaluation(encoder, train_loader, val_loader, num_classes=1000,
                       epochs=100, lr=0.1, device='cuda'):
    """Freeze encoder, train and evaluate a linear classifier."""
    encoder.eval()
    for p in encoder.parameters():
        p.requires_grad_(False)

    # Determine feature dimension from a dummy forward pass
    with torch.no_grad():
        dummy = torch.randn(2, 3, 224, 224).to(device)
        feat_dim = encoder(dummy).flatten(1).size(1)

    classifier = nn.Linear(feat_dim, num_classes).to(device)
    optimizer = torch.optim.SGD(classifier.parameters(), lr=lr,
                                momentum=0.9, weight_decay=0.0)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, epochs)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        classifier.train()
        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            with torch.no_grad():
                feats = encoder(imgs).flatten(1)
            logits = classifier(feats)
            loss = criterion(logits, labels)
            optimizer.zero_grad(); loss.backward(); optimizer.step()
        scheduler.step()

    # Validation accuracy
    classifier.eval()
    correct = total = 0
    with torch.no_grad():
        for imgs, labels in val_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            feats = encoder(imgs).flatten(1)
            preds = classifier(feats).argmax(1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    return correct / total

print('Linear evaluation protocol: freeze encoder, train linear head only.')
```

> **Projection Head Matters — Use Encoder Output Downstream**: A critical finding of SimCLR is that the projection head (g) improves contrastive learning but the representation before the projection head (h) is better for downstream tasks. The projection head collapses information that is useful for classification but not for contrastive loss. Always freeze the encoder and discard the projection head when performing linear evaluation or fine-tuning.

## Temperature and Batch Size Sensitivity

Temperature τ controls the concentration of the distribution. Low τ (e.g., 0.07) creates a sharper distribution, penalising hard negatives more. High τ treats negatives more uniformly. Batch size is a proxy for the number of negatives: at batch size N, there are 2(N-1) negatives per anchor. SimCLR needs 4096–8192 images per batch to accumulate enough negatives. This requires either many GPUs or gradient accumulation, making it expensive compared to queue-based methods.

- τ = 0.07 optimal across experiments — too low causes instability, too high degrades quality.
- Batch size 4096 with LARS optimizer and cosine decay over 100–1000 epochs.
- Random resized crop is the single most important augmentation (>10% top-1 difference).
- Color jitter + random grayscale prevents reliance on color statistics as a cheat code.
- Removing Gaussian blur from the pipeline causes ~1–2% top-1 regression.

## SimCLR v2 and Extensions

SimCLR v2 (Chen et al. 2020b) introduced three improvements: (1) a larger backbone (ResNet-152 with selective kernels), (2) a deeper projection head (3-layer MLP instead of 2-layer), and (3) semi-supervised learning with distillation — use the self-supervised model to generate pseudo-labels on unlabelled data and distil into a smaller student. These improvements pushed top-1 accuracy beyond 79% on ImageNet with only 1% of labels.

| Method | Batch Size | Negatives Needed | Projection Layers | Linear Eval Top-1 |
| --- | --- | --- | --- | --- |
| SimCLR v1 | 4096 | Yes (in-batch) | 2-layer MLP | 69.3% |
| SimCLR v2 | 4096 | Yes (in-batch) | 3-layer MLP | 74.2% |
| BYOL | 4096 | No | 2-layer MLP | 74.3% |
| MoCo v3 | 4096 | No (large batch ViT) | 2-layer MLP | 83.2% (ViT-B/16) |

