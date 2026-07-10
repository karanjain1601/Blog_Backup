---
title: "DETR: End-to-End Detection with Transformers"
slug: "detr-transformer-detection"
description: "Detection as set prediction — DETR removes anchors and NMS using learned object queries, bipartite matching (Hungarian algorithm), and a transformer encoder-decoder over image features."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZXRlY3Rpb24gVHJhbnNmb3JtZXIgKERFVFIpIGVsaW1pbmF0ZXMgdHdvIGhhbmQtY3JhZnRlZCBjb21wb25lbnRzIHRoYXQgaGF2ZSBkZWZpbmVkIG9iamVjdCBkZXRlY3RvcnMgZm9yIGEgZGVjYWRlOiBhbmNob3IgYm94ZXMgYW5kIG5vbi1tYXhpbXVtIHN1cHByZXNzaW9uIChOTVMpLiBJbnN0ZWFkLCBERVRSIHRyZWF0cyBkZXRlY3Rpb24gYXMgZGlyZWN0IHNldCBwcmVkaWN0aW9uLiBBIGZpeGVkIHNldCBvZiBsZWFybmVkIHF1ZXJpZXMgYXR0ZW5kcyB0byBpbWFnZSBmZWF0dXJlcyB2aWEgYSB0cmFuc2Zvcm1lciBkZWNvZGVyLCBhbmQgZWFjaCBxdWVyeSBwcm9kdWNlcyBleGFjdGx5IG9uZSBvYmplY3QgcHJlZGljdGlvbi4gTm8gcG9zdC1wcm9jZXNzaW5nIHJlcXVpcmVkLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiREVUUiB3YXMgaW50cm9kdWNlZCBieSBDYXJpb24gZXQgYWwuIGF0IEZhY2Vib29rIEFJIFJlc2VhcmNoIGluIDIwMjAuIEl0cyBlbGVnYW5jZSBsaWVzIGluIHJlbW92aW5nIHRoZSBoZXVyaXN0aWMtaGVhdnkgY29tcG9uZW50cyBvZiBwcmlvciBkZXRlY3RvcnMuIFRoZSB0cmFkZW9mZiBpcyBzbG93IGNvbnZlcmdlbmNlIOKAlCBERVRSIG5lZWRzIDUwMCBlcG9jaHMgb24gQ09DTyB0byBtYXRjaCBGYXN0ZXIgUi1DTk4gdHJhaW5lZCBmb3IgMTIgZXBvY2hzLiBGb2xsb3ctdXAgd29yayAoRGVmb3JtYWJsZSBERVRSLCBEQUItREVUUiwgRE4tREVUUiwgUlQtREVUUikgaGFzIGxhcmdlbHkgY2xvc2VkIHRoaXMgZ2FwLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRldGVjdGlvbiBhcyBTZXQgUHJlZGljdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhZGl0aW9uYWwgZGV0ZWN0b3JzIHByb2R1Y2UgaHVuZHJlZHMgb2Ygb3ZlcmxhcHBpbmcgY2FuZGlkYXRlIGJveGVzIHRoZW4gdXNlIE5NUyB0byBzZWxlY3QgdGhlIGJlc3Qgb25lcy4gVGhpcyBjcmVhdGVzIGEgbm9uLWRpZmZlcmVudGlhYmxlIHBvc3QtcHJvY2Vzc2luZyBzdGVwIGFuZCByZXF1aXJlcyBjYXJlZnVsIHR1bmluZyBvZiBJb1UgdGhyZXNob2xkcy4gREVUUiBpbnN0ZWFkIG91dHB1dHMgZXhhY3RseSBOIHByZWRpY3Rpb25zICh0eXBpY2FsbHkgTj0xMDApIGFuZCB1c2VzIGJpcGFydGl0ZSBtYXRjaGluZyBkdXJpbmcgdHJhaW5pbmcgdG8gYXNzaWduIGVhY2ggcHJlZGljdGlvbiB0byBhdCBtb3N0IG9uZSBncm91bmQtdHJ1dGggb2JqZWN0LiBVbm1hdGNoZWQgcHJlZGljdGlvbnMgbGVhcm4gdG8gcHJlZGljdCBcdTAwMjdubyBvYmplY3RcdTAwMjcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2V0IHByZWRpY3Rpb24gZm9ybXVsYXRpb24gcmVxdWlyZXMgYSBsb3NzIHRoYXQgaXMgcGVybXV0YXRpb24taW52YXJpYW50OiB0aGUgc2FtZSBzZXQgb2YgZ3JvdW5kIHRydXRocyBtdXN0IHByb2R1Y2UgdGhlIHNhbWUgbG9zcyByZWdhcmRsZXNzIG9mIHRoZSBvcmRlciBvZiBwcmVkaWN0aW9ucy4gSHVuZ2FyaWFuIG1hdGNoaW5nIHByb3ZpZGVzIHRoaXMgYnkgZmluZGluZyB0aGUgb3B0aW1hbCBvbmUtdG8tb25lIGFzc2lnbm1lbnQgYmV0d2VlbiBwcmVkaWN0aW9ucyBhbmQgdGFyZ2V0cyB0aGF0IG1pbmltaXplcyBhIGNvbWJpbmVkIGNsYXNzaWZpY2F0aW9uICsgbG9jYWxpemF0aW9uIGNvc3QuIFRoaXMgbWFrZXMgdGhlIGxvc3MgYm90aCBwZXJtdXRhdGlvbi1pbnZhcmlhbnQgYW5kIGVuY291cmFnaW5nIG9mIGRpdmVyc2l0eSBhbW9uZyBxdWVyaWVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFyY2hpdGVjdHVyZTogRW5jb2RlciArIERlY29kZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRFVFJcdTAwMjdzIGFyY2hpdGVjdHVyZSBoYXMgdGhyZWUgc3RhZ2VzOiAoMSkgYSBDTk4gYmFja2JvbmUgKHR5cGljYWxseSBSZXNOZXQtNTApIGV4dHJhY3RzIGEgZmVhdHVyZSBtYXAgYXQgMS8zMiByZXNvbHV0aW9uOyAoMikgYSB0cmFuc2Zvcm1lciBlbmNvZGVyIHJlZmluZXMgdGhlc2UgZmVhdHVyZXMgd2l0aCBnbG9iYWwgc2VsZi1hdHRlbnRpb247ICgzKSBhIHRyYW5zZm9ybWVyIGRlY29kZXIgdGFrZXMgTiBsZWFybmVkIG9iamVjdCBxdWVyaWVzIGFuZCBhdHRlbmRzIHRvIGVuY29kZXIgb3V0cHV0cyB0byBwcm9kdWNlIE4gKGNsYXNzLCBib3gpIHByZWRpY3Rpb25zLiBUaGUgMkQgcG9zaXRpb25hbCBlbmNvZGluZyBhZGRlZCB0byBiYWNrYm9uZSBmZWF0dXJlcyBpcyBjcnVjaWFsIGZvciBzcGF0aWFsIGF3YXJlbmVzcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBtYXRoXG5cbmNsYXNzIERFVFJfRW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsPTI1NiwgbmhlYWQ9OCwgbnVtX2xheWVycz02KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuaW5wdXRfcHJvaiA9IG5uLkNvbnYyZCgyMDQ4LCBkX21vZGVsLCAxKSAgIyBSZXNOZXQgQzU6IDIwNDhjaFxuICAgICAgICBlbmNvZGVyX2xheWVyID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyTGF5ZXIoZF9tb2RlbCwgbmhlYWQsIGRpbV9mZWVkZm9yd2FyZD0yMDQ4KVxuICAgICAgICBzZWxmLmVuY29kZXIgPSBubi5UcmFuc2Zvcm1lckVuY29kZXIoZW5jb2Rlcl9sYXllciwgbnVtX2xheWVycylcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGJhY2tib25lX2ZlYXQsIHBvc19lbWJlZCk6XG4gICAgICAgIEIsIEMsIEgsIFcgPSBiYWNrYm9uZV9mZWF0LnNoYXBlXG4gICAgICAgIGZlYXQgPSBzZWxmLmlucHV0X3Byb2ooYmFja2JvbmVfZmVhdCkgICMgW0IsIDI1NiwgSCwgV11cbiAgICAgICAgZmVhdF9mbGF0ID0gZmVhdC5mbGF0dGVuKDIpLnBlcm11dGUoMiwgMCwgMSkgICAjIFtIVywgQiwgMjU2XVxuICAgICAgICBwb3NfZmxhdCA9IHBvc19lbWJlZC5mbGF0dGVuKDIpLnBlcm11dGUoMiwgMCwgMSlcbiAgICAgICAgbWVtb3J5ID0gc2VsZi5lbmNvZGVyKGZlYXRfZmxhdCArIHBvc19mbGF0KSAgICAjIFtIVywgQiwgMjU2XVxuICAgICAgICByZXR1cm4gbWVtb3J5In0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIERFVFJfRGVjb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsPTI1NiwgbmhlYWQ9OCwgbnVtX2xheWVycz02LCBudW1fcXVlcmllcz0xMDAsIG51bV9jbGFzc2VzPTkxKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucXVlcnlfZW1iZWQgPSBubi5FbWJlZGRpbmcobnVtX3F1ZXJpZXMsIGRfbW9kZWwpXG4gICAgICAgIGRlY29kZXJfbGF5ZXIgPSBubi5UcmFuc2Zvcm1lckRlY29kZXJMYXllcihkX21vZGVsLCBuaGVhZCwgZGltX2ZlZWRmb3J3YXJkPTIwNDgpXG4gICAgICAgIHNlbGYuZGVjb2RlciA9IG5uLlRyYW5zZm9ybWVyRGVjb2RlcihkZWNvZGVyX2xheWVyLCBudW1fbGF5ZXJzKVxuICAgICAgICBzZWxmLmNsYXNzX2hlYWQgPSBubi5MaW5lYXIoZF9tb2RlbCwgbnVtX2NsYXNzZXMgKyAxKSAgIyArMSBmb3Igbm8tb2JqZWN0XG4gICAgICAgIHNlbGYuYm94X2hlYWQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihkX21vZGVsLCA0KSwgbm4uU2lnbW9pZCgpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgbWVtb3J5LCBCKTpcbiAgICAgICAgcXVlcmllcyA9IHNlbGYucXVlcnlfZW1iZWQud2VpZ2h0LnVuc3F1ZWV6ZSgxKS5yZXBlYXQoMSwgQiwgMSkgICMgW04sIEIsIGRdXG4gICAgICAgIG91dCA9IHNlbGYuZGVjb2RlcihxdWVyaWVzLCBtZW1vcnkpICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBbTiwgQiwgZF1cbiAgICAgICAgcmV0dXJuIHNlbGYuY2xhc3NfaGVhZChvdXQpLCBzZWxmLmJveF9oZWFkKG91dCkgICAgICAgICAgICAgICAgICAjIGNsYXNzZXMsIGJveGVzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSHVuZ2FyaWFuIE1hdGNoaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEdXJpbmcgdHJhaW5pbmcsIERFVFIgdXNlcyB0aGUgSHVuZ2FyaWFuIGFsZ29yaXRobSB0byBmaW5kIHRoZSBtaW5pbXVtIGNvc3QgYmlwYXJ0aXRlIG1hdGNoaW5nIGJldHdlZW4gdGhlIE4gcHJlZGljdGVkIGJveGVzIGFuZCBNIGdyb3VuZC10cnV0aCBib3hlcyAoTSDiiaQgTikuIFRoZSBjb3N0IG1hdHJpeCBjb21iaW5lcyB0aHJlZSB0ZXJtczogKDEpIG5lZ2F0aXZlIGxvZy1wcm9iYWJpbGl0eSBvZiB0aGUgY29ycmVjdCBjbGFzcywgKDIpIEwxIGRpc3RhbmNlIGJldHdlZW4gcHJlZGljdGVkIGFuZCB0YXJnZXQgYm94IGNvb3JkaW5hdGVzLCBhbmQgKDMpIG5lZ2F0aXZlIGdlbmVyYWxpemVkIElvVSAoR0lvVSkgYmV0d2VlbiBib3hlcy4gR0lvVSBpcyBjcnVjaWFsIGZvciBoYW5kbGluZyBub24tb3ZlcmxhcHBpbmcgYm94ZXMgd2hlcmUgTDEgYW5kIElvVSBncmFkaWVudHMgdmFuaXNoLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5vcHRpbWl6ZSBpbXBvcnQgbGluZWFyX3N1bV9hc3NpZ25tZW50XG5cbmRlZiBodW5nYXJpYW5fbWF0Y2gocHJlZF9sb2dpdHMsIHByZWRfYm94ZXMsIGd0X2xhYmVscywgZ3RfYm94ZXMsIGNsc193ZWlnaHQ9MSwgbDFfd2VpZ2h0PTUsIGdpb3Vfd2VpZ2h0PTIpOlxuICAgIFwiXCJcIlxuICAgIHByZWRfbG9naXRzOiBbTiwgbnVtX2NsYXNzZXMrMV0sIHByZWRfYm94ZXM6IFtOLCA0XSAoY3gsY3ksdyxoIG5vcm1hbGl6ZWQpXG4gICAgZ3RfbGFiZWxzOiBbTV0sIGd0X2JveGVzOiBbTSwgNF1cbiAgICBSZXR1cm5zOiBtYXRjaGVkIChwcmVkX2lkeCwgZ3RfaWR4KSBwYWlyc1xuICAgIFwiXCJcIlxuICAgIE4sIE0gPSBsZW4ocHJlZF9sb2dpdHMpLCBsZW4oZ3RfbGFiZWxzKVxuICAgICMgQ2xhc3NpZmljYXRpb24gY29zdDogLWxvZ19zb2Z0bWF4IGZvciB0YXJnZXQgY2xhc3Nlc1xuICAgIGNsc19jb3N0ID0gLXByZWRfbG9naXRzLnNvZnRtYXgoLTEpWzosIGd0X2xhYmVsc10gICMgW04sIE1dXG4gICAgIyBMMSBjb3N0XG4gICAgbDFfY29zdCA9IHRvcmNoLmNkaXN0KHByZWRfYm94ZXMsIGd0X2JveGVzLCBwPTEpICAgIyBbTiwgTV1cbiAgICAjIENvbWJpbmUgKEdJb1Ugb21pdHRlZCBoZXJlIGZvciBicmV2aXR5KVxuICAgIGNvc3QgPSBjbHNfd2VpZ2h0ICogY2xzX2Nvc3QgKyBsMV93ZWlnaHQgKiBsMV9jb3N0XG4gICAgcm93X2lkeCwgY29sX2lkeCA9IGxpbmVhcl9zdW1fYXNzaWdubWVudChjb3N0LmRldGFjaCgpLmNwdSgpLm51bXB5KCkpXG4gICAgcmV0dXJuIHRvcmNoLmFzX3RlbnNvcihyb3dfaWR4KSwgdG9yY2guYXNfdGVuc29yKGNvbF9pZHgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiREVUUiBUcmFpbmluZyBhbmQgQ29udmVyZ2VuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRFVFJcdTAwMjdzIHNsb3cgY29udmVyZ2VuY2Ugc3RlbXMgZnJvbSB0aGUgY3Jvc3MtYXR0ZW50aW9uIG1lY2hhbmlzbSBpbiB0aGUgZGVjb2RlciDigJQgcXVlcmllcyBtdXN0IGxlYXJuIHRvIGF0dGVuZCB0byBzcGVjaWZpYyBpbWFnZSByZWdpb25zIGZyb20gcmFuZG9tIGluaXRpYWxpemF0aW9uLCB3aGljaCB0YWtlcyBtYW55IGVwb2Nocy4gVGhlIGVuY29kZXIgbXVzdCBhbHNvIGxlYXJuIHRvIHJlcHJlc2VudCBvYmplY3RzIGFzIGNvaGVyZW50IGVudGl0aWVzIGluIGl0cyBmZWF0dXJlIHNwYWNlLiBBbmFseXNpcyBzaG93cyB0aGF0IGF0dGVudGlvbiBtYXBzIG9ubHkgYmVjb21lIG9iamVjdC1zcGVjaWZpYyBhZnRlciB+MTUwIGVwb2NocywgZXhwbGFpbmluZyB0aGUgZ2FwIHZlcnN1cyBSUE4tYmFzZWQgdHdvLXN0YWdlIGRldGVjdG9ycy4ifSx7InR5cGUiOiJjYWxsb3V0IiwiY2FsbG91dF90eXBlIjoid2FybmluZyIsImNvbnRlbnQiOiJERVRSIHRyYWlucyBzbG93bHkg4oCUIGl0IG5lZWRzIDUwMCBlcG9jaHMgdnMgMTIgZm9yIEZhc3RlciBSLUNOTiB0byBjb252ZXJnZS4gRGVmb3JtYWJsZSBERVRSIGFuZCBSVC1ERVRSIGZpeCB0aGlzIHdpdGggZGVmb3JtYWJsZSBhdHRlbnRpb24gYW5kIGltcHJvdmVkIG1hdGNoaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgRGV0ckZvck9iamVjdERldGVjdGlvbiwgRGV0ckltYWdlUHJvY2Vzc29yXG5mcm9tIFBJTCBpbXBvcnQgSW1hZ2VcbmltcG9ydCByZXF1ZXN0c1xuaW1wb3J0IHRvcmNoXG5cbnByb2Nlc3NvciA9IERldHJJbWFnZVByb2Nlc3Nvci5mcm9tX3ByZXRyYWluZWQoXHUwMDI3ZmFjZWJvb2svZGV0ci1yZXNuZXQtNTBcdTAwMjcpXG5tb2RlbCA9IERldHJGb3JPYmplY3REZXRlY3Rpb24uZnJvbV9wcmV0cmFpbmVkKFx1MDAyN2ZhY2Vib29rL2RldHItcmVzbmV0LTUwXHUwMDI3KVxuXG5pbWFnZSA9IEltYWdlLm9wZW4oXHUwMDI3aW1hZ2UuanBnXHUwMDI3KVxuaW5wdXRzID0gcHJvY2Vzc29yKGltYWdlcz1pbWFnZSwgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcpXG5vdXRwdXRzID0gbW9kZWwoKippbnB1dHMpXG5cbiMgUG9zdC1wcm9jZXNzOiBmaWx0ZXIgMTAwIHF1ZXJ5IHByZWRpY3Rpb25zIGJ5IGNvbmZpZGVuY2VcbnJlc3VsdHMgPSBwcm9jZXNzb3IucG9zdF9wcm9jZXNzX29iamVjdF9kZXRlY3Rpb24oXG4gICAgb3V0cHV0cywgdGhyZXNob2xkPTAuNywgdGFyZ2V0X3NpemVzPVtpbWFnZS5zaXplWzo6LTFdXSlbMF1cblxuZm9yIHNjb3JlLCBsYWJlbCwgYm94IGluIHppcChyZXN1bHRzW1x1MDAyN3Njb3Jlc1x1MDAyN10sIHJlc3VsdHNbXHUwMDI3bGFiZWxzXHUwMDI3XSwgcmVzdWx0c1tcdTAwMjdib3hlc1x1MDAyN10pOlxuICAgIHByaW50KGZcdTAwMjd7bW9kZWwuY29uZmlnLmlkMmxhYmVsW2xhYmVsLml0ZW0oKV19OiB7c2NvcmU6LjJmfSBhdCB7Ym94LnRvbGlzdCgpfVx1MDAyNykifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRGV0ZWN0b3IiLCJBbmNob3JzIiwiTk1TIiwiQ29udmVyZ2VuY2UiLCJDT0NPIG1BUCIsIlNwZWVkIl0sInJvd3MiOltbIkZhc3RlciBSLUNOTiIsIlllcyAoUlBOKSIsIlllcyIsIjEyIGVwb2NocyIsIjQyLjAiLCJ+MjUgRlBTIl0sWyJSZXRpbmFOZXQiLCJZZXMgKGRlbnNlKSIsIlllcyIsIjEyIGVwb2NocyIsIjQwLjgiLCJ+MTggRlBTIl0sWyJERVRSIiwiTm8iLCJObyIsIjUwMCBlcG9jaHMiLCI0Mi4wIiwifjI4IEZQUyJdLFsiRGVmb3JtYWJsZSBERVRSIiwiTm8iLCJObyIsIjUwIGVwb2NocyIsIjQ2LjIiLCJ+MTkgRlBTIl0sWyJSVC1ERVRSIiwiTm8iLCJObyIsIjcyIGVwb2NocyIsIjUzLjEiLCJ+MTE0IEZQUyJdLFsiREFCLURFVFIiLCJObyIsIk5vIiwiNTAgZXBvY2hzIiwiNDUuNyIsIn4yMCBGUFMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRFVFJcdTAwMjdzIGFyY2hpdGVjdHVyYWwgY29udHJpYnV0aW9ucyBleHRlbmQgYmV5b25kIGRldGVjdGlvbi4gT2JqZWN0IHF1ZXJpZXMgYXMgYSBtZWNoYW5pc20gZm9yIHNldCBwcmVkaWN0aW9uIGhhdmUgYmVlbiBhZGFwdGVkIGZvciBwYW5vcHRpYyBzZWdtZW50YXRpb24gKE1hc2syRm9ybWVyKSwgM0Qgb2JqZWN0IGRldGVjdGlvbiAoREVUUjNEKSwgbXVsdGktb2JqZWN0IHRyYWNraW5nIChUcmFja0Zvcm1lciksIGFuZCB2aWRlbyB1bmRlcnN0YW5kaW5nLiBUaGUgSHVuZ2FyaWFuIG1hdGNoaW5nIHRyYWluaW5nIHBhcmFkaWdtIGlzIG5vdyB1c2VkIGluIG1hbnkgdGFza3MgcmVxdWlyaW5nIG9uZS10by1vbmUgcHJlZGljdGlvbiwgZnJvbSBrZXlwb2ludCBkZXRlY3Rpb24gdG8gY2FwdGlvbiBnZW5lcmF0aW9uLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIHByYWN0aXRpb25lcnM6IHVzZSBSVC1ERVRSIChmcm9tIEJhaWR1IC8gVWx0cmFseXRpY3MpIGlmIHlvdSBuZWVkIHRyYW5zZm9ybWVyLWJhc2VkIGRldGVjdGlvbiBpbiBwcm9kdWN0aW9uIOKAlCBpdCBtYXRjaGVzIERFVFJcdTAwMjdzIGVsZWdhbmNlIHdoaWxlIHRyYWluaW5nIGluIDcyIGVwb2NocyBhbmQgYWNoaWV2aW5nIDUzKyBtQVAgYXQgMTE0IEZQUy4gVXNlIERlZm9ybWFibGUgREVUUiBmb3IgcmVzZWFyY2ggYmFzZWxpbmVzLiBBdm9pZCB2YW5pbGxhIERFVFIgZm9yIG5ldyBwcm9qZWN0cyDigJQgaXRzIDUwMC1lcG9jaCB0cmFpbmluZyByZXF1aXJlbWVudCBtYWtlcyBpdGVyYXRpb24gZXhwZW5zaXZlLCBhbmQgaXRzIHN1Y2Nlc3NvcnMgYXJlIHN0cmljdGx5IHN1cGVyaW9yIG9uIGFsbCBtZXRyaWNzLiJ9XQ=="
---
# DETR: End-to-End Detection with Transformers

## Overview

Detection Transformer (DETR) eliminates two hand-crafted components that have defined object detectors for a decade: anchor boxes and non-maximum suppression (NMS). Instead, DETR treats detection as direct set prediction. A fixed set of learned queries attends to image features via a transformer decoder, and each query produces exactly one object prediction. No post-processing required.

DETR was introduced by Carion et al. at Facebook AI Research in 2020. Its elegance lies in removing the heuristic-heavy components of prior detectors. The tradeoff is slow convergence — DETR needs 500 epochs on COCO to match Faster R-CNN trained for 12 epochs. Follow-up work (Deformable DETR, DAB-DETR, DN-DETR, RT-DETR) has largely closed this gap.

## Detection as Set Prediction

Traditional detectors produce hundreds of overlapping candidate boxes then use NMS to select the best ones. This creates a non-differentiable post-processing step and requires careful tuning of IoU thresholds. DETR instead outputs exactly N predictions (typically N=100) and uses bipartite matching during training to assign each prediction to at most one ground-truth object. Unmatched predictions learn to predict 'no object'.

The set prediction formulation requires a loss that is permutation-invariant: the same set of ground truths must produce the same loss regardless of the order of predictions. Hungarian matching provides this by finding the optimal one-to-one assignment between predictions and targets that minimizes a combined classification + localization cost. This makes the loss both permutation-invariant and encouraging of diversity among queries.

## Architecture: Encoder + Decoder

DETR's architecture has three stages: (1) a CNN backbone (typically ResNet-50) extracts a feature map at 1/32 resolution; (2) a transformer encoder refines these features with global self-attention; (3) a transformer decoder takes N learned object queries and attends to encoder outputs to produce N (class, box) predictions. The 2D positional encoding added to backbone features is crucial for spatial awareness.

```python
import torch
import torch.nn as nn
import math

class DETR_Encoder(nn.Module):
    def __init__(self, d_model=256, nhead=8, num_layers=6):
        super().__init__()
        self.input_proj = nn.Conv2d(2048, d_model, 1)  # ResNet C5: 2048ch
        encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward=2048)
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers)

    def forward(self, backbone_feat, pos_embed):
        B, C, H, W = backbone_feat.shape
        feat = self.input_proj(backbone_feat)  # [B, 256, H, W]
        feat_flat = feat.flatten(2).permute(2, 0, 1)   # [HW, B, 256]
        pos_flat = pos_embed.flatten(2).permute(2, 0, 1)
        memory = self.encoder(feat_flat + pos_flat)    # [HW, B, 256]
        return memory
```

```python
import torch
import torch.nn as nn

class DETR_Decoder(nn.Module):
    def __init__(self, d_model=256, nhead=8, num_layers=6, num_queries=100, num_classes=91):
        super().__init__()
        self.query_embed = nn.Embedding(num_queries, d_model)
        decoder_layer = nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward=2048)
        self.decoder = nn.TransformerDecoder(decoder_layer, num_layers)
        self.class_head = nn.Linear(d_model, num_classes + 1)  # +1 for no-object
        self.box_head = nn.Sequential(
            nn.Linear(d_model, d_model), nn.ReLU(),
            nn.Linear(d_model, d_model), nn.ReLU(),
            nn.Linear(d_model, 4), nn.Sigmoid())

    def forward(self, memory, B):
        queries = self.query_embed.weight.unsqueeze(1).repeat(1, B, 1)  # [N, B, d]
        out = self.decoder(queries, memory)                              # [N, B, d]
        return self.class_head(out), self.box_head(out)                  # classes, boxes
```

## Hungarian Matching

During training, DETR uses the Hungarian algorithm to find the minimum cost bipartite matching between the N predicted boxes and M ground-truth boxes (M ≤ N). The cost matrix combines three terms: (1) negative log-probability of the correct class, (2) L1 distance between predicted and target box coordinates, and (3) negative generalized IoU (GIoU) between boxes. GIoU is crucial for handling non-overlapping boxes where L1 and IoU gradients vanish.

```python
import torch
import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_match(pred_logits, pred_boxes, gt_labels, gt_boxes, cls_weight=1, l1_weight=5, giou_weight=2):
    """
    pred_logits: [N, num_classes+1], pred_boxes: [N, 4] (cx,cy,w,h normalized)
    gt_labels: [M], gt_boxes: [M, 4]
    Returns: matched (pred_idx, gt_idx) pairs
    """
    N, M = len(pred_logits), len(gt_labels)
    # Classification cost: -log_softmax for target classes
    cls_cost = -pred_logits.softmax(-1)[:, gt_labels]  # [N, M]
    # L1 cost
    l1_cost = torch.cdist(pred_boxes, gt_boxes, p=1)   # [N, M]
    # Combine (GIoU omitted here for brevity)
    cost = cls_weight * cls_cost + l1_weight * l1_cost
    row_idx, col_idx = linear_sum_assignment(cost.detach().cpu().numpy())
    return torch.as_tensor(row_idx), torch.as_tensor(col_idx)
```

## DETR Training and Convergence

DETR's slow convergence stems from the cross-attention mechanism in the decoder — queries must learn to attend to specific image regions from random initialization, which takes many epochs. The encoder must also learn to represent objects as coherent entities in its feature space. Analysis shows that attention maps only become object-specific after ~150 epochs, explaining the gap versus RPN-based two-stage detectors.

> ****: DETR trains slowly — it needs 500 epochs vs 12 for Faster R-CNN to converge. Deformable DETR and RT-DETR fix this with deformable attention and improved matching.

```python
from transformers import DetrForObjectDetection, DetrImageProcessor
from PIL import Image
import requests
import torch

processor = DetrImageProcessor.from_pretrained('facebook/detr-resnet-50')
model = DetrForObjectDetection.from_pretrained('facebook/detr-resnet-50')

image = Image.open('image.jpg')
inputs = processor(images=image, return_tensors='pt')
outputs = model(**inputs)

# Post-process: filter 100 query predictions by confidence
results = processor.post_process_object_detection(
    outputs, threshold=0.7, target_sizes=[image.size[::-1]])[0]

for score, label, box in zip(results['scores'], results['labels'], results['boxes']):
    print(f'{model.config.id2label[label.item()]}: {score:.2f} at {box.tolist()}')
```

| Detector | Anchors | NMS | Convergence | COCO mAP | Speed |
| --- | --- | --- | --- | --- | --- |
| Faster R-CNN | Yes (RPN) | Yes | 12 epochs | 42.0 | ~25 FPS |
| RetinaNet | Yes (dense) | Yes | 12 epochs | 40.8 | ~18 FPS |
| DETR | No | No | 500 epochs | 42.0 | ~28 FPS |
| Deformable DETR | No | No | 50 epochs | 46.2 | ~19 FPS |
| RT-DETR | No | No | 72 epochs | 53.1 | ~114 FPS |
| DAB-DETR | No | No | 50 epochs | 45.7 | ~20 FPS |

## Key Takeaways

DETR's architectural contributions extend beyond detection. Object queries as a mechanism for set prediction have been adapted for panoptic segmentation (Mask2Former), 3D object detection (DETR3D), multi-object tracking (TrackFormer), and video understanding. The Hungarian matching training paradigm is now used in many tasks requiring one-to-one prediction, from keypoint detection to caption generation.

For practitioners: use RT-DETR (from Baidu / Ultralytics) if you need transformer-based detection in production — it matches DETR's elegance while training in 72 epochs and achieving 53+ mAP at 114 FPS. Use Deformable DETR for research baselines. Avoid vanilla DETR for new projects — its 500-epoch training requirement makes iteration expensive, and its successors are strictly superior on all metrics.

