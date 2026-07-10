---
title: "GoogLeNet / Inception — Parallel Branches and Auxiliary Classifiers"
slug: "googlenet-inception"
description: "GoogLeNet introduces the Inception module — parallel 1×1, 3×3, 5×5, and max-pool branches concatenated to capture multi-scale features — achieving 5M parameters (vs AlexNet's 60M) through 1×1 bottlenecks. Inception-v3 adds factorization; Xception pushes to depthwise separable convolutions."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR29vZ0xlTmV0IChTemVnZWR5IGV0IGFsLiwgMjAxNCwgYWxzbyBJbmNlcHRpb24tdjEpIGFza3MgYSBkaWZmZXJlbnQgcXVlc3Rpb24gZnJvbSBWR0c6IGluc3RlYWQgb2YgZ29pbmcgZGVlcGVyIHVuaWZvcm1seSwgd2hhdCBpZiBhIHNpbmdsZSBsYXllciBjYXB0dXJlcyBmZWF0dXJlcyBhdCBtdWx0aXBsZSBzY2FsZXMgc2ltdWx0YW5lb3VzbHk/IFRoZSBJbmNlcHRpb24gbW9kdWxlIGFwcGxpZXMgcGFyYWxsZWwgY29udm9sdXRpb25zIG9mIGRpZmZlcmVudCBrZXJuZWwgc2l6ZXMgYW5kIGNvbmNhdGVuYXRlcyB0aGVpciBvdXRwdXRzLiBUaGlzIG11bHRpLXNjYWxlIHByb2Nlc3Npbmcg4oCUIDHDlzEgZm9yIGNyb3NzLWNoYW5uZWwgcHJvamVjdGlvbiwgM8OXMyBmb3IgbG9jYWwgZmVhdHVyZXMsIDXDlzUgZm9yIGJyb2FkZXIgY29udGV4dCwgcGx1cyBtYXggcG9vbGluZyBmb3Igc3BhdGlhbCBpbnZhcmlhbmNlIOKAlCBjYXB0dXJlcyBhIHJpY2hlciBmZWF0dXJlIHJlcHJlc2VudGF0aW9uIHRoYW4gYW55IHNpbmdsZSBrZXJuZWwgc2l6ZSwgd2hpbGUgMcOXMSBib3R0bGVuZWNrcyBrZWVwIGNvbXB1dGF0aW9uIHRyYWN0YWJsZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb3RpdmF0aW9uOiBFZmZpY2llbmN5IFRocm91Z2ggQXJjaGl0ZWN0dXJhbCBXaWR0aCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGFyZ2VyIG5ldHdvcmtzIG1lYW4gbW9yZSBwYXJhbWV0ZXJzIGFuZCBtb3JlIGNvbXB1dGF0aW9uIOKAlCB0d28gcmVzb3VyY2VzIHRoYXQgc2NhbGUgcG9vcmx5IHdpdGggZGVwdGggYWxvbmUuIEdvb2dMZU5ldFx1MDAyN3Mgc29sdXRpb24gaXMgYXJjaGl0ZWN0dXJhbCB3aWR0aDogd2l0aGluIGEgc2luZ2xlIGxheWVyLCBhcHBseSBtdWx0aXBsZSBmaWx0ZXIgc2l6ZXMgaW4gcGFyYWxsZWwgYW5kIGxldCB0aGUgbmV0d29yayBsZWFybiB3aGljaCBzY2FsZXMgYXJlIG1vc3QgaW5mb3JtYXRpdmUuIFRoZSAxw5cxIGNvbnZvbHV0aW9uIGlzIGtleTogYXBwbGllZCBiZWZvcmUgZXhwZW5zaXZlIDPDlzMgYW5kIDXDlzUgY29udm9sdXRpb25zLCBpdCBhY3RzIGFzIGEgY2hhbm5lbC1yZWR1Y3Rpb24gYm90dGxlbmVjay4gV2l0aG91dCAxw5cxIHJlZHVjdGlvbiwgYSBzaW5nbGUgSW5jZXB0aW9uIG1vZHVsZSBvbiAyNTYtY2hhbm5lbCBpbnB1dCB3aXRoIDY0IGZpbHRlcnMgb2YgNcOXNSBjb3N0cyAyNTbDlzY0w5cyNcOXSMOXVyA9IDQwOSw2MDDDl0jDl1cgbXVsdGlwbHktYWRkcy4gV2l0aCBhIDHDlzEgcmVkdWN0aW9uIHRvIDMyIGNoYW5uZWxzIGZpcnN0OiAyNTbDlzMyICsgMzLDlzY0w5cyNSA9IDU5LDM5MiDigJQgYSA3w5cgcmVkdWN0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBJbmNlcHRpb24gTW9kdWxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgSW5jZXB0aW9uLXYxIG1vZHVsZSBoYXMgZm91ciBwYXJhbGxlbCBicmFuY2hlczogKDEpIDHDlzEgY29udiBmb3IgZGlyZWN0IGNoYW5uZWwgcHJvamVjdGlvbjsgKDIpIDHDlzEgY29udiByZWR1Y2luZyBjaGFubmVscywgZm9sbG93ZWQgYnkgM8OXMyBjb252OyAoMykgMcOXMSBjb252IHJlZHVjaW5nIGNoYW5uZWxzLCBmb2xsb3dlZCBieSA1w5c1IGNvbnY7ICg0KSAzw5czIG1heCBwb29saW5nIGZvbGxvd2VkIGJ5IDHDlzEgY29udi4gQWxsIGJyYW5jaGVzIHByZXNlcnZlIHNwYXRpYWwgZGltZW5zaW9ucyAodmlhIGFwcHJvcHJpYXRlIHBhZGRpbmcpIGFuZCB0aGVpciBvdXRwdXRzIGFyZSBjb25jYXRlbmF0ZWQgYWxvbmcgdGhlIGNoYW5uZWwgZGltZW5zaW9uLiBUaGUgbmV0d29yayBsZWFybnMgdG8gd2VpZ2h0IHRoZXNlIHBhdGh3YXlzIHRocm91Z2ggYmFja3Byb3BhZ2F0aW9uIOKAlCBlZmZlY3RpdmVseSBwZXJmb3JtaW5nIHNwYXJzZSwgbXVsdGktc2NhbGUgZmVhdHVyZSBleHRyYWN0aW9uIGF0IGVhY2ggbGF5ZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIEluY2VwdGlvbk1vZHVsZShubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0luY2VwdGlvbi12MSBtb2R1bGU6IHBhcmFsbGVsIGJyYW5jaGVzIGF0IDF4MSwgM3gzLCA1eDUsIG1heC1wb29sLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgY2gxeDEsIGNoM3gzX3IsIGNoM3gzLCBjaDV4NV9yLCBjaDV4NSwgY2hfcG9vbCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmJyYW5jaDEgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoLCBjaDF4MSwgMSksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSlcbiAgICAgICAgc2VsZi5icmFuY2gyID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChpbl9jaCwgY2gzeDNfciwgMSksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChjaDN4M19yLCBjaDN4MywgMywgcGFkZGluZz0xKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpKVxuICAgICAgICBzZWxmLmJyYW5jaDMgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoLCBjaDV4NV9yLCAxKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uQ29udjJkKGNoNXg1X3IsIGNoNXg1LCA1LCBwYWRkaW5nPTIpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSkpXG4gICAgICAgIHNlbGYuYnJhbmNoNCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5NYXhQb29sMmQoMywgc3RyaWRlPTEsIHBhZGRpbmc9MSksXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2gsIGNoX3Bvb2wsIDEpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHRvcmNoLmNhdChbc2VsZi5icmFuY2gxKHgpLCBzZWxmLmJyYW5jaDIoeCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYuYnJhbmNoMyh4KSwgc2VsZi5icmFuY2g0KHgpXSwgZGltPTEpXG5cbiMgSW5jZXB0aW9uLTNhIGZyb20gR29vZ0xlTmV0IHBhcGVyOiBpbj0xOTIsIG91dD02NCsxMjgrMzIrMzI9MjU2XG5tb2R1bGUgPSBJbmNlcHRpb25Nb2R1bGUoMTkyLCA2NCwgOTYsIDEyOCwgMTYsIDMyLCAzMilcbnggPSB0b3JjaC5yYW5kbigyLCAxOTIsIDI4LCAyOClcbm91dCA9IG1vZHVsZSh4KVxucGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2R1bGUucGFyYW1ldGVycygpKVxucHJpbnQoXHUwMDI3SW5jZXB0aW9uLTNhOiB7fSAtXHUwMDNlIHt9XHUwMDI3LmZvcm1hdCh4LnNoYXBlLCBvdXQuc2hhcGUpKVxucHJpbnQoXHUwMDI3T3V0cHV0IGNoYW5uZWxzOiA2NCsxMjgrMzIrMzIgPSB7fVx1MDAyNy5mb3JtYXQoNjQrMTI4KzMyKzMyKSlcbnByaW50KFx1MDAyN1BhcmFtZXRlcnM6IHs6LH1cdTAwMjcuZm9ybWF0KHBhcmFtcykpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiMXgxIENvbnZvbHV0aW9ucyBhcyBDaGFubmVsIEJvdHRsZW5lY2tzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgMcOXMSBjb252b2x1dGlvbiAoYWxzbyBjYWxsZWQgYSBwb2ludHdpc2UgY29udm9sdXRpb24gb3IgbmV0d29yay1pbi1uZXR3b3JrIHByb2plY3Rpb24pIG9wZXJhdGVzIGlkZW50aWNhbGx5IHRvIGEgbGluZWFyIGNvbWJpbmF0aW9uIGFjcm9zcyBjaGFubmVscyBhdCBlYWNoIHNwYXRpYWwgbG9jYXRpb24uIEl0IHJlZHVjZXMgY2hhbm5lbHMgYmVmb3JlIGV4cGVuc2l2ZSBjb252b2x1dGlvbnMg4oCUIGZvciBleGFtcGxlLCByZWR1Y2luZyAyNTYgY2hhbm5lbHMgdG8gMzIgYmVmb3JlIGEgNcOXNSBjb252IGN1dHMgdGhlIDXDlzUgY29tcHV0YXRpb24gYnkgOMOXIOKAlCBhbmQgZXhwYW5kcyBjaGFubmVscyBhZnRlciBkZXB0aHdpc2UgY29udm9sdXRpb25zIGluIG1vZGVybiBhcmNoaXRlY3R1cmVzLiBCZXlvbmQgY2hhbm5lbCByZWR1Y3Rpb24sIDHDlzEgY29udnMgYWRkIG5vbmxpbmVhcml0eSAocGFpcmVkIHdpdGggUmVMVSkgYW5kIG1peCBpbmZvcm1hdGlvbiBhY3Jvc3MgY2hhbm5lbHMgd2l0aG91dCBhbnkgc3BhdGlhbCBtaXhpbmcuIExpbiBldCBhbC4gKDIwMTQpIHNob3dlZCB0aGF0IDHDlzEgY29udiBsYXllcnMgYWN0IGFzIFx1MDAyN21pY3JvLW5ldHdvcmtzXHUwMDI3IHdpdGhpbiBlYWNoIHNwYXRpYWwgbG9jYXRpb24sIGdyZWF0bHkgaW5jcmVhc2luZyByZXByZXNlbnRhdGlvbmFsIGNhcGFjaXR5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgY291bnRfcGFyYW1zKG0pOiByZXR1cm4gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtLnBhcmFtZXRlcnMoKSlcbmRlZiBjb3VudF9mbG9wc19jb252KGluX2NoLCBvdXRfY2gsIGssIGgsIHcpOlxuICAgIHJldHVybiAyICogaW5fY2ggKiBvdXRfY2ggKiBrICogayAqIGggKiB3XG5cbmluX2NoLCBvdXRfY2gsIEgsIFcgPSAyNTYsIDEyOCwgMTQsIDE0XG5cbiMgRGlyZWN0IDV4NSBjb252XG5kaXJlY3QgPSBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgNSwgcGFkZGluZz0yKVxuXG4jIDF4MSBib3R0bGVuZWNrICsgNXg1IGNvbnZcbmJvdHRsZW5lY2sgPSBubi5TZXF1ZW50aWFsKFxuICAgIG5uLkNvbnYyZChpbl9jaCwgMzIsIDEpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgbm4uQ29udjJkKDMyLCBvdXRfY2gsIDUsIHBhZGRpbmc9MikpXG5cbmRpcmVjdF9wYXJhbXMgPSBjb3VudF9wYXJhbXMoZGlyZWN0KVxuYm90dGxlX3BhcmFtcyA9IGNvdW50X3BhcmFtcyhib3R0bGVuZWNrKVxuZGlyZWN0X2Zsb3BzICA9IGNvdW50X2Zsb3BzX2NvbnYoaW5fY2gsIG91dF9jaCwgNSwgSCwgVylcbmJvdHRsZV9mbG9wcyAgPSAoY291bnRfZmxvcHNfY29udihpbl9jaCwgMzIsIDEsIEgsIFcpICtcbiAgICAgICAgICAgICAgICAgY291bnRfZmxvcHNfY29udigzMiwgb3V0X2NoLCA1LCBILCBXKSlcblxucHJpbnQoXHUwMDI3ezpcdTAwM2MyMH0gezpcdTAwM2UxMn0gezpcdTAwM2UxNH1cdTAwMjcuZm9ybWF0KFx1MDAyN0NvbmZpZ1x1MDAyNywgXHUwMDI3UGFyYW1zXHUwMDI3LCBcdTAwMjdGTE9Qc1x1MDAyNykpXG5wcmludChcdTAwMjd7Olx1MDAzYzIwfSB7Olx1MDAzZTEyLH0gezpcdTAwM2UxNCx9XHUwMDI3LmZvcm1hdChcdTAwMjdEaXJlY3QgNXg1XHUwMDI3LCBkaXJlY3RfcGFyYW1zLCBkaXJlY3RfZmxvcHMpKVxucHJpbnQoXHUwMDI3ezpcdTAwM2MyMH0gezpcdTAwM2UxMix9IHs6XHUwMDNlMTQsfVx1MDAyNy5mb3JtYXQoXHUwMDI3MXgxKzV4NSBib3R0bGVuZWNrXHUwMDI3LCBib3R0bGVfcGFyYW1zLCBib3R0bGVfZmxvcHMpKVxucHJpbnQoXHUwMDI3UGFyYW0gcmVkdWN0aW9uOiB7Oi4xZn14XHUwMDI3LmZvcm1hdChkaXJlY3RfcGFyYW1zIC8gYm90dGxlX3BhcmFtcykpXG5wcmludChcdTAwMjdGTE9QIHJlZHVjdGlvbjogIHs6LjFmfXhcdTAwMjcuZm9ybWF0KGRpcmVjdF9mbG9wcyAvIGJvdHRsZV9mbG9wcykpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXV4aWxpYXJ5IENsYXNzaWZpZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHb29nTGVOZXQgaW5zZXJ0cyB0d28gYXV4aWxpYXJ5IGNsYXNzaWZpY2F0aW9uIGhlYWRzIGF0IGludGVybWVkaWF0ZSBkZXB0aHMgKGFmdGVyIEluY2VwdGlvbi00YSBhbmQgSW5jZXB0aW9uLTRkKS4gRHVyaW5nIHRyYWluaW5nLCB0aGVzZSBhdXhpbGlhcnkgb3V0cHV0cyBjb21wdXRlIHNvZnRtYXggbG9zc2VzICh3ZWlnaHRlZCBieSAwLjMpIHRoYXQgYXJlIGFkZGVkIHRvIHRoZSBtYWluIGxvc3MuIEdyYWRpZW50cyBmcm9tIHRoZXNlIGludGVybWVkaWF0ZSBsb3NzZXMgZmxvdyBiYWNrd2FyZCBpbnRvIHRoZSBsb3dlciBsYXllcnMsIHByb3ZpZGluZyBhbiBhZGRpdGlvbmFsIHRyYWluaW5nIHNpZ25hbCBhbmQgY29tYmF0aW5nIHZhbmlzaGluZyBncmFkaWVudHMgaW4gdGhlIDIyLWxheWVyIG5ldHdvcmsuIEF0IGluZmVyZW5jZSB0aW1lLCBhdXhpbGlhcnkgY2xhc3NpZmllcnMgYXJlIHJlbW92ZWQuIFRoZSBJbmNlcHRpb24gYXV0aG9ycyBsYXRlciBhY2tub3dsZWRnZWQgdGhhdCB0aGUgcmVndWxhcmlzYXRpb24gZWZmZWN0IChkcm9wb3V0IGJlZm9yZSBhdXhpbGlhcnkgY2xhc3NpZmllcnMpIGNvbnRyaWJ1dGVkIG1vcmUgdGhhbiB0aGUgZ3JhZGllbnQgc2lnbmFsIOKAlCBJbmNlcHRpb24tdjMgcmV0YWluZWQgb25seSBvbmUgYXV4aWxpYXJ5IGNsYXNzaWZpZXIuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJBdXhpbGlhcnkgQ2xhc3NpZmllcnMgdnMgUmVzaWR1YWxzIiwiY29udGVudCI6IkF1eGlsaWFyeSBjbGFzc2lmaWVycyBzb2x2ZSB0aGUgdmFuaXNoaW5nIGdyYWRpZW50IHByb2JsZW0gYnkgaW5qZWN0aW5nIGxvc3Mgc2lnbmFsIGF0IGludGVybWVkaWF0ZSBsYXllcnMg4oCUIGFuIGVuZ2luZWVyaW5nIHdvcmthcm91bmQuIFJlc05ldCAoMjAxNSkgc29sdmVkIHRoZSBzYW1lIHByb2JsZW0gbW9yZSBlbGVnYW50bHkgd2l0aCBza2lwIGNvbm5lY3Rpb25zIHRoYXQgcHJvdmlkZSBhIGRpcmVjdCBncmFkaWVudCBwYXRoLiBXaXRoIHNraXAgY29ubmVjdGlvbnMsIGF1eGlsaWFyeSBjbGFzc2lmaWVycyBiZWNvbWUgdW5uZWNlc3NhcnkuIEluY2VwdGlvbi12NCBhbmQgSW5jZXB0aW9uLVJlc05ldCBjb21iaW5lIGJvdGggYXBwcm9hY2hlcywgYnV0IHRoZSByZXNpZHVhbCBwYXRoIGRvbWluYXRlcy4gTW9kZXJuIGFyY2hpdGVjdHVyZXMgdW5pdmVyc2FsbHkgcHJlZmVyIHJlc2lkdWFscyBvdmVyIGF1eGlsaWFyeSBjbGFzc2lmaWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbmNlcHRpb24tdjM6IEZhY3Rvcml6YXRpb24gYW5kIEFzeW1tZXRyaWMgQ29udm9sdXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbmNlcHRpb24tdjMgKFN6ZWdlZHkgZXQgYWwuLCAyMDE2KSBpbnRyb2R1Y2VzIHRocmVlIGtleSBpbXByb3ZlbWVudHM6ICgxKSBmYWN0b3JpemUgNcOXNSBjb252b2x1dGlvbnMgaW50byB0d28gc3RhY2tlZCAzw5czIGNvbnZvbHV0aW9ucyAoc2FtZSBSRiwgZmV3ZXIgcGFyYW1ldGVycyk7ICgyKSBmYWN0b3JpemUgbsOXbiBjb252b2x1dGlvbnMgaW50byBhc3ltbWV0cmljIDHDl24gKyBuw5cxIGNvbnZvbHV0aW9ucyDigJQgZm9yIG49NywgdGhpcyByZWR1Y2VzIHBhcmFtZXRlcnMgZnJvbSA0OUPCsiB0byAxNEPCsiAoMy41w5cgc2F2aW5nKTsgKDMpIGxhYmVsIHNtb290aGluZyBhcyBhIHJlZ3VsYXJpc2VyICh0YXJnZXQgZGlzdHJpYnV0aW9uOiAwLjkgZm9yIHRydWUgY2xhc3MsIDAuMS8oSy0xKSBmb3Igb3RoZXJzKTsgKDQpIEJhdGNoTm9ybSBhcHBsaWVkIHRocm91Z2hvdXQgdGhlIGF1eGlsaWFyeSBjbGFzc2lmaWVyLiBUaGVzZSBjaGFuZ2VzIHJlZHVjZWQgY29tcHV0YXRpb24gYnkgYSBmYWN0b3Igb2YgNCB3aGlsZSBpbXByb3ZpbmcgYWNjdXJhY3kgdG8gNzguOCUgdG9wLTEgb24gSW1hZ2VOZXQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBjb3VudF9wYXJhbXMobSk6IHJldHVybiBzdW0ocC5udW1lbCgpIGZvciBwIGluIG0ucGFyYW1ldGVycygpKVxuXG5pbl9jaCwgb3V0X2NoLCBuID0gMjU2LCAyNTYsIDdcblxuIyBTdGFuZGFyZCBueG4gY29udlxuc3RhbmRhcmQgPSBubi5TZXF1ZW50aWFsKFxuICAgIG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCBuLCBwYWRkaW5nPW4vLzIsIGJpYXM9RmFsc2UpLFxuICAgIG5uLkJhdGNoTm9ybTJkKG91dF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSlcblxuIyBGYWN0b3JlZCBpbnRvIHR3byAzeDMgY29udnMgKGZvciBuPTUgY2FzZSlcbmZhY3RvcmVkXzV4NSA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uQ29udjJkKGluX2NoLCBvdXRfY2gsIDMsIHBhZGRpbmc9MSwgYmlhcz1GYWxzZSksXG4gICAgbm4uQmF0Y2hOb3JtMmQob3V0X2NoKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgIG5uLkNvbnYyZChvdXRfY2gsIG91dF9jaCwgMywgcGFkZGluZz0xLCBiaWFzPUZhbHNlKSxcbiAgICBubi5CYXRjaE5vcm0yZChvdXRfY2gpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSkpXG5cbiMgQXN5bW1ldHJpYyBmYWN0b3JpemF0aW9uOiAxeG4gKyBueDFcbmFzeW1tZXRyaWMgPSBubi5TZXF1ZW50aWFsKFxuICAgIG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAoMSwgbiksIHBhZGRpbmc9KDAsIG4vLzIpLCBiaWFzPUZhbHNlKSxcbiAgICBubi5CYXRjaE5vcm0yZChvdXRfY2gpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgbm4uQ29udjJkKG91dF9jaCwgb3V0X2NoLCAobiwgMSksIHBhZGRpbmc9KG4vLzIsIDApLCBiaWFzPUZhbHNlKSxcbiAgICBubi5CYXRjaE5vcm0yZChvdXRfY2gpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSkpXG5cbnggPSB0b3JjaC5yYW5kbigyLCBpbl9jaCwgMTcsIDE3KVxuZm9yIG5hbWUsIG0gaW4gWyhcdTAwMjd7fXh7fSBzdGFuZGFyZFx1MDAyNy5mb3JtYXQobixuKSwgc3RhbmRhcmQpLFxuICAgICAgICAgICAgICAgIChcdTAwMjd0d28gM3gzXHUwMDI3LCBmYWN0b3JlZF81eDUpLFxuICAgICAgICAgICAgICAgIChcdTAwMjcxeHt9K3t9eDFcdTAwMjcuZm9ybWF0KG4sbiksIGFzeW1tZXRyaWMpXTpcbiAgICBwcmludChcdTAwMjd7Olx1MDAzYzE4fSBwYXJhbXM9ezpcdTAwM2U4LH0gIG91dD17fVx1MDAyNy5mb3JtYXQobmFtZSwgY291bnRfcGFyYW1zKG0pLCBtKHgpLnNoYXBlKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJYY2VwdGlvbjogRXh0cmVtZSBJbmNlcHRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlhjZXB0aW9uIChDaG9sbGV0LCAyMDE3KSB0YWtlcyBJbmNlcHRpb24gdG8gaXRzIGxvZ2ljYWwgZXh0cmVtZTogaWYgSW5jZXB0aW9uIG1vZHVsZXMgYXJlIGVzc2VudGlhbGx5IGRlcHRod2lzZSBzZXBhcmFibGUgY29udm9sdXRpb25zIChzcGF0aWFsIGZpbHRlcmluZyBwZXIgY2hhbm5lbCwgZm9sbG93ZWQgYnkgY3Jvc3MtY2hhbm5lbCBtaXhpbmcpLCB3aHkgbm90IHJlcGxhY2UgYWxsIGNvbnZvbHV0aW9ucyB3aXRoIGRlcHRod2lzZSBzZXBhcmFibGUgb3BlcmF0aW9ucz8gWGNlcHRpb24gdXNlcyAzNiBkZXB0aHdpc2Ugc2VwYXJhYmxlIGNvbnYgbGF5ZXJzIGluIGEgbGluZWFyIHN0YWNrIHdpdGggcmVzaWR1YWwgY29ubmVjdGlvbnMuIEEgZGVwdGh3aXNlIHNlcGFyYWJsZSBjb252IGFwcGxpZXMgYSBzcGF0aWFsIDPDlzMgZmlsdGVyIHRvIGVhY2ggaW5wdXQgY2hhbm5lbCBpbmRlcGVuZGVudGx5IChkZXB0aHdpc2UpLCB0aGVuIG1peGVzIGNoYW5uZWxzIHdpdGggYSAxw5cxIGNvbnYgKHBvaW50d2lzZSkuIEZvciBDIGlucHV0IGFuZCBvdXRwdXQgY2hhbm5lbHMsIHRoaXMgY29zdHMgQ8OXOSArIEPCsiBwYXJhbWV0ZXJzIHZzIEPCssOXOSBmb3IgYSBzdGFuZGFyZCBjb252IOKAlCByb3VnaGx5IGEgMS85ICsgMS9DIHNhdmluZywgdHlwaWNhbGx5IDjigJM5w5cgZmV3ZXIgcGFyYW1ldGVycy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGNvdW50X3BhcmFtcyhtKTogcmV0dXJuIHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbS5wYXJhbWV0ZXJzKCkpXG5cbmNsYXNzIERlcHRod2lzZVNlcGFyYWJsZShubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN1hjZXB0aW9uLXN0eWxlIGRlcHRod2lzZSBzZXBhcmFibGUgY29udm9sdXRpb24gYmxvY2suXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBvdXRfY2gpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5kdyA9IG5uLkNvbnYyZChpbl9jaCwgaW5fY2gsIDMsIHBhZGRpbmc9MSwgZ3JvdXBzPWluX2NoLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnB3ID0gbm4uQ29udjJkKGluX2NoLCBvdXRfY2gsIDEsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuYm4gPSBubi5CYXRjaE5vcm0yZChvdXRfY2gpXG4gICAgICAgIHNlbGYucmVsdSA9IG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiByZXR1cm4gc2VsZi5yZWx1KHNlbGYuYm4oc2VsZi5wdyhzZWxmLmR3KHgpKSkpXG5cbmNsYXNzIFN0YW5kYXJkQ29udkJsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBvdXRfY2gpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5jb252ID0gbm4uQ29udjJkKGluX2NoLCBvdXRfY2gsIDMsIHBhZGRpbmc9MSwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5ibiAgID0gbm4uQmF0Y2hOb3JtMmQob3V0X2NoKVxuICAgICAgICBzZWxmLnJlbHUgPSBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYucmVsdShzZWxmLmJuKHNlbGYuY29udih4KSkpXG5cbmluX2NoLCBvdXRfY2ggPSAyNTYsIDI1Nlxuc3RkID0gU3RhbmRhcmRDb252QmxvY2soaW5fY2gsIG91dF9jaClcbmR3cyA9IERlcHRod2lzZVNlcGFyYWJsZShpbl9jaCwgb3V0X2NoKVxueCA9IHRvcmNoLnJhbmRuKDIsIGluX2NoLCAyOCwgMjgpXG5cbnJhdGlvID0gY291bnRfcGFyYW1zKHN0ZCkgLyBjb3VudF9wYXJhbXMoZHdzKVxudGhlb3J5ID0gMS85ICsgMS9vdXRfY2hcbnByaW50KFx1MDAyN1N0YW5kYXJkIGNvbnY6ICAgezpcdTAwM2U4LH0gcGFyYW1zICBvdXRwdXQge31cdTAwMjcuZm9ybWF0KGNvdW50X3BhcmFtcyhzdGQpLCBzdGQoeCkuc2hhcGUpKVxucHJpbnQoXHUwMDI3RFcgU2VwYXJhYmxlOiAgICB7Olx1MDAzZTgsfSBwYXJhbXMgIG91dHB1dCB7fVx1MDAyNy5mb3JtYXQoY291bnRfcGFyYW1zKGR3cyksIGR3cyh4KS5zaGFwZSkpXG5wcmludChcdTAwMjdSZWR1Y3Rpb246IHs6LjJmfXggICh0aGVvcnk6IDEvOSsxL0MgPSB7Oi40Zn0pXHUwMDI3LmZvcm1hdChyYXRpbywgdGhlb3J5KSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbmNlcHRpb24gVmVyc2lvbnMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWFjaCBJbmNlcHRpb24gdmVyc2lvbiBhZGRyZXNzZXMgYSBzcGVjaWZpYyBsaW1pdGF0aW9uIG9mIGl0cyBwcmVkZWNlc3NvcjogdjEgaW50cm9kdWNlZCBtdWx0aS1zY2FsZSBwYXJhbGxlbCBicmFuY2hlczsgdjMgZmFjdG9yaXNlZCBvcGVyYXRpb25zIGZvciBlZmZpY2llbmN5OyB2NCBhZGRlZCByZXNpZHVhbCBjb25uZWN0aW9ucyBmb3IgZWFzaWVyIHRyYWluaW5nOyBYY2VwdGlvbiByZXBsYWNlZCBpbmNlcHRpb24gYmxvY2tzIHdpdGggZGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbnMgZW50aXJlbHkuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiWWVhciIsIlBhcmFtcyIsIkdGTE9QcyIsIlRvcC0xIEFjYyIsIktleSBJbm5vdmF0aW9uIl0sInJvd3MiOltbIkdvb2dMZU5ldCAodjEpIiwiMjAxNCIsIjVNIiwiMS41IiwiNjkuOCUiLCJJbmNlcHRpb24gbW9kdWxlICsgYXV4aWxpYXJ5IGNsYXNzaWZpZXJzIl0sWyJJbmNlcHRpb24tdjMiLCIyMDE2IiwiMjNNIiwiNS43IiwiNzguOCUiLCJGYWN0b3JpemVkIDXDlzUgKyBhc3ltbWV0cmljIDHDl24sIGxhYmVsIHNtb290aGluZyJdLFsiSW5jZXB0aW9uLXY0IiwiMjAxNiIsIjQyTSIsIjEyLjMiLCI4MC4wJSIsIkRlZXBlciBpbmNlcHRpb24gd2l0aCB1bmlmb3JtIHN0ZW0gYmxvY2siXSxbIkluY2VwdGlvbi1SZXNOZXQtdjIiLCIyMDE2IiwiNTVNIiwiMTMuMiIsIjgwLjQlIiwiSW5jZXB0aW9uIG1vZHVsZXMgKyByZXNpZHVhbCBzaG9ydGN1dHMiXSxbIlhjZXB0aW9uIiwiMjAxNyIsIjIyTSIsIjguNCIsIjc5LjAlIiwiQWxsIGNvbnZvbHV0aW9ucyByZXBsYWNlZCBieSBkZXB0aHdpc2Ugc2VwYXJhYmxlIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdvb2dMZU5ldCBhY2hpZXZlZCBBbGV4TmV0LWxldmVsIGFjY3VyYWN5IHdpdGggMTJ4IGZld2VyIHBhcmFtZXRlcnMg4oCUIGRlbW9uc3RyYXRpbmcgdGhhdCBhcmNoaXRlY3R1cmFsIGRlc2lnbiBtYXR0ZXJzIG1vcmUgdGhhbiByYXcgc2NhbGUuIiwiMXgxIGNvbnZvbHV0aW9ucyBhcmUgbm93IHVuaXZlcnNhbDogdGhleSBhcHBlYXIgaW4gUmVzTmV0IGJvdHRsZW5lY2tzLCBNb2JpbGVOZXQsIEVmZmljaWVudE5ldCwgYW5kIHRyYW5zZm9ybWVyIHByb2plY3Rpb24gbGF5ZXJzLiIsIkFzeW1tZXRyaWMgZmFjdG9yaXNhdGlvbiAoMXhuICsgbngxKSBpbnNwaXJlZCB0aGUgdXNlIG9mIGRlcHRod2lzZSBzZXBhcmFibGUgY29udm9sdXRpb25zIGluIE1vYmlsZU5ldCBhbmQgU2h1ZmZsZU5ldC4iLCJBdXhpbGlhcnkgY2xhc3NpZmllcnMgd2VyZSBsYXJnZWx5IGFiYW5kb25lZCBhZnRlciByZXNpZHVhbCBjb25uZWN0aW9ucyBwcm92aWRlZCBhIGNsZWFuZXIgc29sdXRpb24gdG8gdGhlIHZhbmlzaGluZyBncmFkaWVudCBwcm9ibGVtLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# GoogLeNet / Inception — Parallel Branches and Auxiliary Classifiers

GoogLeNet (Szegedy et al., 2014, also Inception-v1) asks a different question from VGG: instead of going deeper uniformly, what if a single layer captures features at multiple scales simultaneously? The Inception module applies parallel convolutions of different kernel sizes and concatenates their outputs. This multi-scale processing — 1×1 for cross-channel projection, 3×3 for local features, 5×5 for broader context, plus max pooling for spatial invariance — captures a richer feature representation than any single kernel size, while 1×1 bottlenecks keep computation tractable.

## Motivation: Efficiency Through Architectural Width

Larger networks mean more parameters and more computation — two resources that scale poorly with depth alone. GoogLeNet's solution is architectural width: within a single layer, apply multiple filter sizes in parallel and let the network learn which scales are most informative. The 1×1 convolution is key: applied before expensive 3×3 and 5×5 convolutions, it acts as a channel-reduction bottleneck. Without 1×1 reduction, a single Inception module on 256-channel input with 64 filters of 5×5 costs 256×64×25×H×W = 409,600×H×W multiply-adds. With a 1×1 reduction to 32 channels first: 256×32 + 32×64×25 = 59,392 — a 7× reduction.

## The Inception Module

The Inception-v1 module has four parallel branches: (1) 1×1 conv for direct channel projection; (2) 1×1 conv reducing channels, followed by 3×3 conv; (3) 1×1 conv reducing channels, followed by 5×5 conv; (4) 3×3 max pooling followed by 1×1 conv. All branches preserve spatial dimensions (via appropriate padding) and their outputs are concatenated along the channel dimension. The network learns to weight these pathways through backpropagation — effectively performing sparse, multi-scale feature extraction at each layer.

```python
import torch
import torch.nn as nn

class InceptionModule(nn.Module):
    '''Inception-v1 module: parallel branches at 1x1, 3x3, 5x5, max-pool.'''
    def __init__(self, in_ch, ch1x1, ch3x3_r, ch3x3, ch5x5_r, ch5x5, ch_pool):
        super().__init__()
        self.branch1 = nn.Sequential(
            nn.Conv2d(in_ch, ch1x1, 1), nn.ReLU(inplace=True))
        self.branch2 = nn.Sequential(
            nn.Conv2d(in_ch, ch3x3_r, 1), nn.ReLU(inplace=True),
            nn.Conv2d(ch3x3_r, ch3x3, 3, padding=1), nn.ReLU(inplace=True))
        self.branch3 = nn.Sequential(
            nn.Conv2d(in_ch, ch5x5_r, 1), nn.ReLU(inplace=True),
            nn.Conv2d(ch5x5_r, ch5x5, 5, padding=2), nn.ReLU(inplace=True))
        self.branch4 = nn.Sequential(
            nn.MaxPool2d(3, stride=1, padding=1),
            nn.Conv2d(in_ch, ch_pool, 1), nn.ReLU(inplace=True))

    def forward(self, x):
        return torch.cat([self.branch1(x), self.branch2(x),
                          self.branch3(x), self.branch4(x)], dim=1)

# Inception-3a from GoogLeNet paper: in=192, out=64+128+32+32=256
module = InceptionModule(192, 64, 96, 128, 16, 32, 32)
x = torch.randn(2, 192, 28, 28)
out = module(x)
params = sum(p.numel() for p in module.parameters())
print('Inception-3a: {} -> {}'.format(x.shape, out.shape))
print('Output channels: 64+128+32+32 = {}'.format(64+128+32+32))
print('Parameters: {:,}'.format(params))
```

## 1x1 Convolutions as Channel Bottlenecks

The 1×1 convolution (also called a pointwise convolution or network-in-network projection) operates identically to a linear combination across channels at each spatial location. It reduces channels before expensive convolutions — for example, reducing 256 channels to 32 before a 5×5 conv cuts the 5×5 computation by 8× — and expands channels after depthwise convolutions in modern architectures. Beyond channel reduction, 1×1 convs add nonlinearity (paired with ReLU) and mix information across channels without any spatial mixing. Lin et al. (2014) showed that 1×1 conv layers act as 'micro-networks' within each spatial location, greatly increasing representational capacity.

```python
import torch
import torch.nn as nn

def count_params(m): return sum(p.numel() for p in m.parameters())
def count_flops_conv(in_ch, out_ch, k, h, w):
    return 2 * in_ch * out_ch * k * k * h * w

in_ch, out_ch, H, W = 256, 128, 14, 14

# Direct 5x5 conv
direct = nn.Conv2d(in_ch, out_ch, 5, padding=2)

# 1x1 bottleneck + 5x5 conv
bottleneck = nn.Sequential(
    nn.Conv2d(in_ch, 32, 1), nn.ReLU(inplace=True),
    nn.Conv2d(32, out_ch, 5, padding=2))

direct_params = count_params(direct)
bottle_params = count_params(bottleneck)
direct_flops  = count_flops_conv(in_ch, out_ch, 5, H, W)
bottle_flops  = (count_flops_conv(in_ch, 32, 1, H, W) +
                 count_flops_conv(32, out_ch, 5, H, W))

print('{:<20} {:>12} {:>14}'.format('Config', 'Params', 'FLOPs'))
print('{:<20} {:>12,} {:>14,}'.format('Direct 5x5', direct_params, direct_flops))
print('{:<20} {:>12,} {:>14,}'.format('1x1+5x5 bottleneck', bottle_params, bottle_flops))
print('Param reduction: {:.1f}x'.format(direct_params / bottle_params))
print('FLOP reduction:  {:.1f}x'.format(direct_flops / bottle_flops))
```

## Auxiliary Classifiers

GoogLeNet inserts two auxiliary classification heads at intermediate depths (after Inception-4a and Inception-4d). During training, these auxiliary outputs compute softmax losses (weighted by 0.3) that are added to the main loss. Gradients from these intermediate losses flow backward into the lower layers, providing an additional training signal and combating vanishing gradients in the 22-layer network. At inference time, auxiliary classifiers are removed. The Inception authors later acknowledged that the regularisation effect (dropout before auxiliary classifiers) contributed more than the gradient signal — Inception-v3 retained only one auxiliary classifier.

> **Auxiliary Classifiers vs Residuals**: Auxiliary classifiers solve the vanishing gradient problem by injecting loss signal at intermediate layers — an engineering workaround. ResNet (2015) solved the same problem more elegantly with skip connections that provide a direct gradient path. With skip connections, auxiliary classifiers become unnecessary. Inception-v4 and Inception-ResNet combine both approaches, but the residual path dominates. Modern architectures universally prefer residuals over auxiliary classifiers.

## Inception-v3: Factorization and Asymmetric Convolutions

Inception-v3 (Szegedy et al., 2016) introduces three key improvements: (1) factorize 5×5 convolutions into two stacked 3×3 convolutions (same RF, fewer parameters); (2) factorize n×n convolutions into asymmetric 1×n + n×1 convolutions — for n=7, this reduces parameters from 49C² to 14C² (3.5× saving); (3) label smoothing as a regulariser (target distribution: 0.9 for true class, 0.1/(K-1) for others); (4) BatchNorm applied throughout the auxiliary classifier. These changes reduced computation by a factor of 4 while improving accuracy to 78.8% top-1 on ImageNet.

```python
import torch
import torch.nn as nn

def count_params(m): return sum(p.numel() for p in m.parameters())

in_ch, out_ch, n = 256, 256, 7

# Standard nxn conv
standard = nn.Sequential(
    nn.Conv2d(in_ch, out_ch, n, padding=n//2, bias=False),
    nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True))

# Factored into two 3x3 convs (for n=5 case)
factored_5x5 = nn.Sequential(
    nn.Conv2d(in_ch, out_ch, 3, padding=1, bias=False),
    nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True),
    nn.Conv2d(out_ch, out_ch, 3, padding=1, bias=False),
    nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True))

# Asymmetric factorization: 1xn + nx1
asymmetric = nn.Sequential(
    nn.Conv2d(in_ch, out_ch, (1, n), padding=(0, n//2), bias=False),
    nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True),
    nn.Conv2d(out_ch, out_ch, (n, 1), padding=(n//2, 0), bias=False),
    nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True))

x = torch.randn(2, in_ch, 17, 17)
for name, m in [('{}x{} standard'.format(n,n), standard),
                ('two 3x3', factored_5x5),
                ('1x{}+{}x1'.format(n,n), asymmetric)]:
    print('{:<18} params={:>8,}  out={}'.format(name, count_params(m), m(x).shape))
```

## Xception: Extreme Inception

Xception (Chollet, 2017) takes Inception to its logical extreme: if Inception modules are essentially depthwise separable convolutions (spatial filtering per channel, followed by cross-channel mixing), why not replace all convolutions with depthwise separable operations? Xception uses 36 depthwise separable conv layers in a linear stack with residual connections. A depthwise separable conv applies a spatial 3×3 filter to each input channel independently (depthwise), then mixes channels with a 1×1 conv (pointwise). For C input and output channels, this costs C×9 + C² parameters vs C²×9 for a standard conv — roughly a 1/9 + 1/C saving, typically 8–9× fewer parameters.

```python
import torch
import torch.nn as nn

def count_params(m): return sum(p.numel() for p in m.parameters())

class DepthwiseSeparable(nn.Module):
    '''Xception-style depthwise separable convolution block.'''
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.dw = nn.Conv2d(in_ch, in_ch, 3, padding=1, groups=in_ch, bias=False)
        self.pw = nn.Conv2d(in_ch, out_ch, 1, bias=False)
        self.bn = nn.BatchNorm2d(out_ch)
        self.relu = nn.ReLU(inplace=True)
    def forward(self, x): return self.relu(self.bn(self.pw(self.dw(x))))

class StandardConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.conv = nn.Conv2d(in_ch, out_ch, 3, padding=1, bias=False)
        self.bn   = nn.BatchNorm2d(out_ch)
        self.relu = nn.ReLU(inplace=True)
    def forward(self, x): return self.relu(self.bn(self.conv(x)))

in_ch, out_ch = 256, 256
std = StandardConvBlock(in_ch, out_ch)
dws = DepthwiseSeparable(in_ch, out_ch)
x = torch.randn(2, in_ch, 28, 28)

ratio = count_params(std) / count_params(dws)
theory = 1/9 + 1/out_ch
print('Standard conv:   {:>8,} params  output {}'.format(count_params(std), std(x).shape))
print('DW Separable:    {:>8,} params  output {}'.format(count_params(dws), dws(x).shape))
print('Reduction: {:.2f}x  (theory: 1/9+1/C = {:.4f})'.format(ratio, theory))
```

## Inception Versions Comparison

Each Inception version addresses a specific limitation of its predecessor: v1 introduced multi-scale parallel branches; v3 factorised operations for efficiency; v4 added residual connections for easier training; Xception replaced inception blocks with depthwise separable convolutions entirely.

| Model | Year | Params | GFLOPs | Top-1 Acc | Key Innovation |
| --- | --- | --- | --- | --- | --- |
| GoogLeNet (v1) | 2014 | 5M | 1.5 | 69.8% | Inception module + auxiliary classifiers |
| Inception-v3 | 2016 | 23M | 5.7 | 78.8% | Factorized 5×5 + asymmetric 1×n, label smoothing |
| Inception-v4 | 2016 | 42M | 12.3 | 80.0% | Deeper inception with uniform stem block |
| Inception-ResNet-v2 | 2016 | 55M | 13.2 | 80.4% | Inception modules + residual shortcuts |
| Xception | 2017 | 22M | 8.4 | 79.0% | All convolutions replaced by depthwise separable |

- GoogLeNet achieved AlexNet-level accuracy with 12x fewer parameters — demonstrating that architectural design matters more than raw scale.
- 1x1 convolutions are now universal: they appear in ResNet bottlenecks, MobileNet, EfficientNet, and transformer projection layers.
- Asymmetric factorisation (1xn + nx1) inspired the use of depthwise separable convolutions in MobileNet and ShuffleNet.
- Auxiliary classifiers were largely abandoned after residual connections provided a cleaner solution to the vanishing gradient problem.

---

