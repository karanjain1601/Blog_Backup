---
title: "Sparse GPs — Inducing Points, FITC, and VFE"
slug: "sparse-gps-inducing-points"
description: "How inducing-point methods (FITC, VFE, SVGP) reduce exact GP training from O(n³) to O(nm²), the overconfidence problem with FITC versus the variational correction in VFE, and mini-batch training with SVGP for massive datasets."
tags: ["gaussian-processes", "kernel-methods", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBPKG7CsykgQm90dGxlbmVjayBvZiBFeGFjdCBHUHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV4YWN0IEdQIHJlZ3Jlc3Npb24gcmVxdWlyZXMgaW52ZXJ0aW5nIHRoZSBuw5duIGtlcm5lbCBtYXRyaXggSyArIM+DwrJfbiBJLCB3aGljaCBjb3N0cyBPKG7CsykgdGltZSBhbmQgTyhuwrIpIG1lbW9yeS4gRm9yIG4gPSAxLDAwMCB0aGlzIGlzIGZhc3Q7IGZvciBuID0gMTAsMDAwIGl0IHRha2VzIG1pbnV0ZXM7IGZvciBuID0gMTAwLDAwMCBpdCBiZWNvbWVzIGludHJhY3RhYmxlIG9uIGEgc3RhbmRhcmQgd29ya3N0YXRpb24uIFRoZSBjb3JlIGlzc3VlIGlzIHRoYXQgZXZlcnkgdHJhaW5pbmcgcG9pbnQgY29udHJpYnV0ZXMgdG8gZXZlcnkgcHJlZGljdGlvbiDigJQgc3RvcmluZyBhbmQgaW52ZXJ0aW5nIHRoZSBmdWxsIG7Dl24gbWF0cml4IGlzIHVuYXZvaWRhYmxlIGluIHRoZSBleGFjdCBmb3JtdWxhdGlvbi4gU3BhcnNlIEdQIGFwcHJveGltYXRpb25zIGF0dGFjayB0aGlzIGJ5IGludHJvZHVjaW5nIGEgbXVjaCBzbWFsbGVyIHNldCBvZiBtIOKJqiBuIHJlcHJlc2VudGF0aXZlIHBvaW50cyB0aGF0IHN1bW1hcmlzZSB0aGUgZW50aXJlIGRhdGFzZXQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW5kdWNpbmcgUG9pbnRzIOKAlCBSZWR1Y2luZyBuIHRvIG0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBpbmR1Y2luZy1wb2ludCBmcmFtZXdvcmsgaW50cm9kdWNlcyBhIHNldCBvZiBtIHBzZXVkby1pbnB1dHMgWiA9IHt64oKBLCDigKYsIHrigph9IHdpdGggY29ycmVzcG9uZGluZyBmdW5jdGlvbiB2YWx1ZXMgdSA9IGYoWikuIFRoZXNlIGluZHVjaW5nIHBvaW50cyBhcmUgbm90IG9ic2VydmVkIGRhdGEg4oCUIHRoZXkgYXJlIGF1eGlsaWFyeSB2YXJpYWJsZXMgY2hvc2VuIHRvIHN1bW1hcmlzZSB0aGUgR1AuIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IGlmIHdlIGNhbiBleHByZXNzIHRoZSBHUCBwb3N0ZXJpb3IgaW4gdGVybXMgb2YgdSByYXRoZXIgdGhhbiBmKFgpLCB3ZSBjYW4gd29yayB3aXRoIGFuIG3Dl20gc3lzdGVtIGluc3RlYWQgb2YgbsOXbiwgcmVkdWNpbmcgdHJhaW5pbmcgY29zdCBmcm9tIE8obsKzKSB0byBPKG5twrIpIGFuZCBtZW1vcnkgZnJvbSBPKG7CsikgdG8gTyhubSkuIERpZmZlcmVudCBzcGFyc2UgR1AgbWV0aG9kcyBkaWZmZXIgaW4gaG93IHRoZXkgYXBwcm94aW1hdGUgdGhlIGpvaW50IGRpc3RyaWJ1dGlvbiBwKGYsIHUpLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsibSDiiaogbiBpbmR1Y2luZyBwb2ludHMgWiBwbGFjZWQgaW4gdGhlIGlucHV0IGRvbWFpbiDigJQgbm90IG9ic2VydmVkIGRhdGEgcG9pbnRzIiwidSA9IGYoWikgYXJlIGZ1bmN0aW9uIHZhbHVlcyBhdCBpbmR1Y2luZyBwb2ludHMg4oCUIGtleSBsYXRlbnQgdmFyaWFibGVzIiwiQWxsIGFwcHJveGltYXRpb25zIHNoYXJlIE8obm3CsikgdHJhaW5pbmcgY29zdCBhbmQgTyhtwrIpIG1lbW9yeSBmb3IgdGhlIG3Dl20gc3lzdGVtIiwiSW5kdWNpbmcgcG9pbnQgbG9jYXRpb25zIFogY2FuIGJlIGZpeGVkIChncmlkL2stbWVhbnMpIG9yIGxlYXJuZWQgYnkgZ3JhZGllbnQgZGVzY2VudCBvbiB0aGUgRUxCTyIsIlF1YWxpdHkgaW1wcm92ZXMgYXMgbSBpbmNyZWFzZXM7IG0gPSBuIHJlY292ZXJzIGV4YWN0IEdQIGF0IGZ1bGwgTyhuwrMpIGNvc3QiLCJHUHlUb3JjaCwgR1BmbG93LCBhbmQgc2Npa2l0LWxlYXJuIHN1cHBvcnQgc3BhcnNlIEdQcyBvdXQgb2YgdGhlIGJveCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGSVRDOiBGdWxseSBJbmRlcGVuZGVudCBUcmFpbmluZyBDb25kaXRpb25hbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRklUQyAoRnVsbHkgSW5kZXBlbmRlbnQgVHJhaW5pbmcgQ29uZGl0aW9uYWwsIFNuZWxzb24gXHUwMDI2IEdoYWhyYW1hbmkgMjAwNikgYXBwcm94aW1hdGVzIHRoZSB0cnVlIGpvaW50IG92ZXIgdHJhaW5pbmcgb3V0cHV0cyBhcyBhIHByb2R1Y3Q6IHEoZnx1KSA9IM6g4bWiIHAoZuG1onx1KS4gRWFjaCB0cmFpbmluZyBvdXRwdXQgZuG1oiBpcyBhc3N1bWVkIGluZGVwZW5kZW50IG9mIGFsbCBvdGhlcnMgZ2l2ZW4gdGhlIGluZHVjaW5nIHZhbHVlcyB1LiBUaGlzIGZhY3RvcmlzYXRpb24gbWFrZXMgdGhlIG7Dl24gdHJhaW5pbmcgY292YXJpYW5jZSBibG9jay1kaWFnb25hbCB3aXRoIGEgcmFuay1tIHVwZGF0ZSBzdHJ1Y3R1cmUuIFRoZSBkaWFnb25hbCBjb3JyZWN0aW9uIHRlcm0gzpsgPSBkaWFnKEtmZiDiiJIgUWZmKSArIM+DwrJfbiBJIGNhcHR1cmVzIHRoZSByZXNpZHVhbCB2YXJpYW5jZSBub3QgZXhwbGFpbmVkIGJ5IHRoZSBpbmR1Y2luZyBwb2ludHMuIEZJVEMgcHJlZGljdGlvbiBpcyBPKG5twrIpIGZvciB0cmFpbmluZyBhbmQgTyhtwrMpIGZvciB0aGUgaW5kdWNpbmctcG9pbnQgaW52ZXJzaW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBlbGw9MS4wLCBzZjI9MS4wKTpcbiAgICBYMSA9IG5wLmF0bGVhc3RfMmQoWDEpLnJlc2hhcGUoLTEsIDEpXG4gICAgWDIgPSBucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLCAxKVxuICAgIHJldHVybiBzZjIgKiBucC5leHAoLTAuNSAqIChYMSAtIFgyLlQpKioyIC8gZWxsKioyKVxuXG5kZWYgZml0Y19wcmVkaWN0KFhfdHJhaW4sIHlfdHJhaW4sIFhfdGVzdCwgWF9pbmQsIGVsbD0xLjAsIHNmMj0xLjAsIG5vaXNlX3Zhcj0wLjEpOlxuICAgIG4sIG0gPSBsZW4oWF90cmFpbiksIGxlbihYX2luZClcbiAgICBLdXUgPSByYmZfa2VybmVsKFhfaW5kLCBYX2luZCwgZWxsLCBzZjIpICsgMWUtNiAqIG5wLmV5ZShtKSAgIyBtIHggbVxuICAgIEt1ZiA9IHJiZl9rZXJuZWwoWF9pbmQsIFhfdHJhaW4sIGVsbCwgc2YyKSAgICAjIG0geCBuXG4gICAgS3VzID0gcmJmX2tlcm5lbChYX2luZCwgWF90ZXN0LCBlbGwsIHNmMikgICAgICMgbSB4IG5fdGVzdFxuICAgIEx1dSA9IG5wLmxpbmFsZy5jaG9sZXNreShLdXUpXG4gICAgViA9IG5wLmxpbmFsZy5zb2x2ZShMdXUsIEt1ZikgICAgICAgICAgICAgICAgICMgbSB4IG4sIEx1dV57LTF9IEt1ZlxuICAgIFFmZl9kaWFnID0gbnAuc3VtKFYqKjIsIGF4aXM9MCkgICAgICAgICAgICAgICAjIGRpYWcgb2YgS3VmXlQgS3V1XnstMX0gS3VmXG4gICAgbGFtID0gc2YyIC0gUWZmX2RpYWcgKyBub2lzZV92YXIgICAgICAgICAgICAgICMgRklUQyBkaWFnb25hbCBjb3JyZWN0aW9uIChsZW5ndGggbilcbiAgICBBID0gViBAIChWIC8gbGFtKS5UICsgbnAuZXllKG0pICAgICAgICAgICAgICAjIG0geCBtXG4gICAgTEEgPSBucC5saW5hbGcuY2hvbGVza3koQSlcbiAgICBiID0gbnAubGluYWxnLnNvbHZlKExBLCBWIEAgKHlfdHJhaW4gLyBsYW0pKSAgIyBtXG4gICAgVyA9IG5wLmxpbmFsZy5zb2x2ZShMdXUsIEt1cykgICAgICAgICAgICAgICAgICMgbSB4IG5fdGVzdFxuICAgIG11ID0gVy5UIEAgbnAubGluYWxnLnNvbHZlKExBLlQsIGIpXG4gICAgdmFyID0gc2YyIC0gbnAuc3VtKFcqKjIsIGF4aXM9MCkgKyBucC5zdW0obnAubGluYWxnLnNvbHZlKExBLCBXKSoqMiwgYXhpcz0wKVxuICAgIHJldHVybiBtdSwgbnAuc3FydChucC5tYXhpbXVtKHZhciwgMCkpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWF90ciA9IG5wLnJhbmRvbS51bmlmb3JtKC01LCA1LCA1MDApXG55X3RyID0gbnAuc2luKFhfdHIpICsgMC4yICogbnAucmFuZG9tLnJhbmRuKDUwMClcblhfaW5kID0gbnAubGluc3BhY2UoLTUsIDUsIDIwKVxuWF90ZSA9IG5wLmxpbnNwYWNlKC02LCA2LCAyMDApXG5tdSwgc3RkID0gZml0Y19wcmVkaWN0KFhfdHIsIHlfdHIsIFhfdGUsIFhfaW5kKVxucGx0LmZpZ3VyZShmaWdzaXplPSgxMCwgNCkpXG5wbHQuZmlsbF9iZXR3ZWVuKFhfdGUsIG11IC0gMipzdGQsIG11ICsgMipzdGQsIGFscGhhPTAuMjUsIGxhYmVsPVx1MDAyN8KxMs+DXHUwMDI3KVxucGx0LnBsb3QoWF90ZSwgbXUsIFx1MDAyN2ItXHUwMDI3LCBsdz0yLCBsYWJlbD1cdTAwMjdGSVRDIG1lYW5cdTAwMjcpXG5wbHQuc2NhdHRlcihYX2luZCwgbnAuemVyb3MoMjApLCBtYXJrZXI9XHUwMDI3fFx1MDAyNywgcz0xMDAsIGM9XHUwMDI3clx1MDAyNywgem9yZGVyPTUsIGxhYmVsPVx1MDAyN0luZHVjaW5nIHB0c1x1MDAyNylcbnBsdC50aXRsZShcdTAwMjdGSVRDIFNwYXJzZSBHUDogbj01MDAgdHJhaW5pbmcgcG9pbnRzLCBtPTIwIGluZHVjaW5nIChjb3N0IE8obm3CsikpXHUwMDI3KVxucGx0LnhsYWJlbChcdTAwMjd4XHUwMDI3KTsgcGx0LnlsYWJlbChcdTAwMjdmKHgpXHUwMDI3KTsgcGx0LmxlZ2VuZCgpOyBwbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zaG93KCkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkZJVEMgQ2FuIEdpdmUgT3ZlcmNvbmZpZGVudCBQcmVkaWN0aW9ucyIsImNvbnRlbnQiOiJCZWNhdXNlIEZJVEMgdHJlYXRzIHRyYWluaW5nIG91dHB1dHMgYXMgaW5kZXBlbmRlbnQgZ2l2ZW4gdSwgaXQgY2FuIHVuZGVyZXN0aW1hdGUgcG9zdGVyaW9yIHVuY2VydGFpbnR5IOKAlCBlc3BlY2lhbGx5IGluIHJlZ2lvbnMgYmV0d2VlbiBpbmR1Y2luZyBwb2ludHMgdGhhdCBzdGlsbCBoYXZlIHRyYWluaW5nIGRhdGEuIElmIHlvdXIgaW5kdWNpbmcgcG9pbnRzIGFyZSB0b28gc3BhcnNlLCBGSVRDIG1heSByZXBvcnQgbG93IHZhcmlhbmNlIChoaWdoIGNvbmZpZGVuY2UpIGluIGdhcHMgd2hlcmUgdGhlIGFwcHJveGltYXRpb24gaXMgYWN0dWFsbHkgcG9vci4gVkZFIGNvcnJlY3RzIHRoaXMgYnkgYm91bmRpbmcgdGhlIHRydWUgcG9zdGVyaW9yIGZyb20gYmVsb3cuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVkZFOiBWYXJpYXRpb25hbCBGcmVlIEVuZXJneSAoVGl0c2lhcyAyMDA5KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVkZFIChWYXJpYXRpb25hbCBGcmVlIEVuZXJneSwgVGl0c2lhcyAyMDA5KSBmcmFtZXMgc3BhcnNlIEdQIGluZmVyZW5jZSBhcyB2YXJpYXRpb25hbCBpbmZlcmVuY2UuIEluc3RlYWQgb2YgbWFraW5nIGEgY29uZGl0aW9uYWwtaW5kZXBlbmRlbmNlIGFwcHJveGltYXRpb24gbGlrZSBGSVRDLCBWRkUgbWluaW1pc2VzIHRoZSBLTCBkaXZlcmdlbmNlIEtMW3EoZix1KSB8fCBwKGYsdXx5KV0gYnkgb3B0aW1pc2luZyBhIGxvd2VyIGJvdW5kIChFTEJPKSB0byB0aGUgbG9nIG1hcmdpbmFsIGxpa2VsaWhvb2QuIFRoZSBFTEJPIGhhcyB0aGUgZm9ybTogbG9nIHAoeSkg4omlIGxvZyBOKHkgfCAwLCBRbm4gKyDPg8KyX25JKSDiiJIgKDEvMs+DwrJfbikgdHIoS2ZmIOKIkiBRbm4pIHdoZXJlIFFubiA9IEtubSBLbW3igbvCuSBLbW4uIFRoZSB0cmFjZSB0ZXJtIGlzIGEgcGVuYWx0eSB0aGF0IGdyb3dzIHdoZW4gdGhlIGluZHVjaW5nIHBvaW50cyBmYWlsIHRvIGV4cGxhaW4gdGhlIGRhdGEgdmFyaWFuY2Ug4oCUIHRoaXMgcHJldmVudHMgb3ZlcmNvbmZpZGVuY2UuIFZGRSBpcyB0aGUgcHJpbmNpcGxlZCBzcGFyc2UgR1A6IEZJVEMgY2FuIGJlIHNlZW4gYXMgVkZFIHdpdGhvdXQgdGhlIHRyYWNlIGNvcnJlY3Rpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IGdweXRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuY2xhc3MgU0dQUk1vZGVsKGdweXRvcmNoLm1vZGVscy5FeGFjdEdQKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdHJhaW5feCwgdHJhaW5feSwgbGlrZWxpaG9vZCwgaW5kdWNpbmdfcG9pbnRzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyh0cmFpbl94LCB0cmFpbl95LCBsaWtlbGlob29kKVxuICAgICAgICBzZWxmLm1lYW5fbW9kdWxlID0gZ3B5dG9yY2gubWVhbnMuWmVyb01lYW4oKVxuICAgICAgICBzZWxmLmNvdmFyX21vZHVsZSA9IGdweXRvcmNoLmtlcm5lbHMuSW5kdWNpbmdQb2ludEtlcm5lbChcbiAgICAgICAgICAgIGdweXRvcmNoLmtlcm5lbHMuU2NhbGVLZXJuZWwoZ3B5dG9yY2gua2VybmVscy5SQkZLZXJuZWwoKSksXG4gICAgICAgICAgICBpbmR1Y2luZ19wb2ludHM9aW5kdWNpbmdfcG9pbnRzLCBsaWtlbGlob29kPWxpa2VsaWhvb2QpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgbWVhbl94ID0gc2VsZi5tZWFuX21vZHVsZSh4KVxuICAgICAgICBjb3Zhcl94ID0gc2VsZi5jb3Zhcl9tb2R1bGUoeClcbiAgICAgICAgcmV0dXJuIGdweXRvcmNoLmRpc3RyaWJ1dGlvbnMuTXVsdGl2YXJpYXRlTm9ybWFsKG1lYW5feCwgY292YXJfeClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbm4gPSAyMDAwXG50cmFpbl94ID0gdG9yY2gucmFuZG4obilcbnRyYWluX3kgPSB0b3JjaC5zaW4odHJhaW5feCAqIDMpICsgMC4yICogdG9yY2gucmFuZG4obilcbmluZHVjaW5nX3B0cyA9IHRvcmNoLmxpbnNwYWNlKC0zLCAzLCA1MClcbmxpa2VsaWhvb2QgPSBncHl0b3JjaC5saWtlbGlob29kcy5HYXVzc2lhbkxpa2VsaWhvb2QoKVxubW9kZWwgPSBTR1BSTW9kZWwodHJhaW5feCwgdHJhaW5feSwgbGlrZWxpaG9vZCwgaW5kdWNpbmdfcHRzKVxubW9kZWwudHJhaW4oKTsgbGlrZWxpaG9vZC50cmFpbigpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MC4wNSlcbm1sbCA9IGdweXRvcmNoLm1sbHMuRXhhY3RNYXJnaW5hbExvZ0xpa2VsaWhvb2QobGlrZWxpaG9vZCwgbW9kZWwpXG5mb3IgaSBpbiByYW5nZSgyMDApOlxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgIGxvc3MgPSAtbWxsKG1vZGVsKHRyYWluX3gpLCB0cmFpbl95KVxuICAgIGxvc3MuYmFja3dhcmQoKTsgb3B0aW1pemVyLnN0ZXAoKVxuICAgIGlmIChpICsgMSkgJSA1MCA9PSAwOlxuICAgICAgICBscyA9IG1vZGVsLmNvdmFyX21vZHVsZS5iYXNlX2tlcm5lbC5iYXNlX2tlcm5lbC5sZW5ndGhzY2FsZS5pdGVtKClcbiAgICAgICAgcHJpbnQoZlx1MDAyN0l0ZXIge2krMX06IGxvc3M9e2xvc3MuaXRlbSgpOi40Zn0sIGxlbmd0aHNjYWxlPXtsczouM2Z9XHUwMDI3KVxucHJpbnQoXHUwMDI3VkZFL1NHUFIgdHJhaW5lZCBvbiBuPTIwMDAgcG9pbnRzIHVzaW5nIG09NTAgbGVhcm5lZCBpbmR1Y2luZyBwb2ludHNcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRklUQyB2cyBWRkUg4oCUIE92ZXJjb25maWRlbmNlIElzc3VlIFZpc3VhbGlzZWQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBwcmFjdGljYWwgZGlmZmVyZW5jZSBiZXR3ZWVuIEZJVEMgYW5kIFZGRSBiZWNvbWVzIHZpc2libGUgaW4gZXh0cmFwb2xhdGlvbiByZWdpb25zIGFuZCBiZXR3ZWVuIHNwYXJzZSBpbmR1Y2luZyBwb2ludHMuIFdpdGggdG9vIGZldyBpbmR1Y2luZyBwb2ludHMsIEZJVEMgbWF5IHJlcG9ydCBuZWFyLXplcm8gdmFyaWFuY2UgaW4gcmVnaW9ucyB3aGVyZSB0aGUgYXBwcm94aW1hdGlvbiBxdWFsaXR5IGlzIHBvb3IsIGJlY2F1c2UgaXQgZG9lcyBub3QgaW5jbHVkZSB0aGUgdHJhY2UgcGVuYWx0eS4gVkZFIGluY2x1ZGVzIHRoaXMgdHJhY2UgdGVybSBpbiBpdHMgRUxCTywgd2hpY2ggYWN0cyBhcyBhIHJlZ3VsYXJpc2VyIHRoYXQgd2lkZW5zIHVuY2VydGFpbnR5IHdoZXJlIHRoZSBpbmR1Y2luZyBwb2ludHMgZG8gbm90IHByb3ZpZGUgZ29vZCBjb3ZlcmFnZS4gSW4gcHJhY3RpY2UsIFZGRSBpcyBwcmVmZXJyZWQgd2hlbiB1bmNlcnRhaW50eSBjYWxpYnJhdGlvbiBtYXR0ZXJzOyBGSVRDIGlzIHNvbWV0aW1lcyBwcmVmZXJyZWQgZm9yIHNwZWVkIGluIGxvdy1zdGFrZXMgcmVncmVzc2lvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZ2F1c3NpYW5fcHJvY2VzcyBpbXBvcnQgR2F1c3NpYW5Qcm9jZXNzUmVncmVzc29yXG5mcm9tIHNrbGVhcm4uZ2F1c3NpYW5fcHJvY2Vzcy5rZXJuZWxzIGltcG9ydCBSQkYsIFdoaXRlS2VybmVsXG5cbm5wLnJhbmRvbS5zZWVkKDcpXG5uID0gMzAwXG5YX3RyID0gbnAuc29ydChucC5yYW5kb20udW5pZm9ybSgtNCwgNCwgbikpLnJlc2hhcGUoLTEsIDEpXG55X3RyID0gbnAuc2luKFhfdHIucmF2ZWwoKSkgKyAwLjE1ICogbnAucmFuZG9tLnJhbmRuKG4pXG5YX3RlID0gbnAubGluc3BhY2UoLTYsIDYsIDMwMCkucmVzaGFwZSgtMSwgMSlcblxuIyBFeGFjdCBHUCBvbiBzbWFsbCBzdWJzZXQgKGdyb3VuZCB0cnV0aCByZWZlcmVuY2UpXG5pZHggPSBucC5yYW5kb20uY2hvaWNlKG4sIDgwLCByZXBsYWNlPUZhbHNlKVxua2VybmVsID0gUkJGKGxlbmd0aF9zY2FsZT0xLjApICsgV2hpdGVLZXJuZWwobm9pc2VfbGV2ZWw9MC4wMilcbmdwX2V4YWN0ID0gR2F1c3NpYW5Qcm9jZXNzUmVncmVzc29yKGtlcm5lbD1rZXJuZWwsIG5fcmVzdGFydHNfb3B0aW1pemVyPTIpXG5ncF9leGFjdC5maXQoWF90cltpZHhdLCB5X3RyW2lkeF0pXG5tdV9leGFjdCwgc3RkX2V4YWN0ID0gZ3BfZXhhY3QucHJlZGljdChYX3RlLCByZXR1cm5fc3RkPVRydWUpXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMywgNCksIHNoYXJleT1UcnVlKVxuZm9yIGF4LCBtLCBsYWJlbCBpbiB6aXAoYXhlcywgWzQsIDIwXSxcbiAgICBbXHUwMDI3RklUQy1saWtlIChtPTQsIG92ZXJjb25maWRlbnQgaW4gZ2FwcylcdTAwMjcsIFx1MDAyN1ZGRS1saWtlIChtPTIwLCBiZXR0ZXIgY2FsaWJyYXRlZClcdTAwMjddKTpcbiAgICBpbmQgPSBucC5saW5zcGFjZSgtNCwgNCwgbSkucmVzaGFwZSgtMSwgMSlcbiAgICBncF9zcGFyc2UgPSBHYXVzc2lhblByb2Nlc3NSZWdyZXNzb3Ioa2VybmVsPVJCRigpICsgV2hpdGVLZXJuZWwoKSwgbl9yZXN0YXJ0c19vcHRpbWl6ZXI9MSlcbiAgICBncF9zcGFyc2UuZml0KG5wLnZzdGFjayhbaW5kLCBYX3RyWzo0MF1dKSwgbnAuaHN0YWNrKFtucC5zaW4oaW5kLnJhdmVsKCkpLCB5X3RyWzo0MF1dKSlcbiAgICBtdSwgc3RkID0gZ3Bfc3BhcnNlLnByZWRpY3QoWF90ZSwgcmV0dXJuX3N0ZD1UcnVlKVxuICAgIGF4LmZpbGxfYmV0d2VlbihYX3RlLnJhdmVsKCksIG11IC0gMipzdGQsIG11ICsgMipzdGQsIGFscGhhPTAuMjUpXG4gICAgYXgucGxvdChYX3RlLnJhdmVsKCksIG11LCBsdz0yLCBsYWJlbD1cdTAwMjdTcGFyc2UgbWVhblx1MDAyNylcbiAgICBheC5wbG90KFhfdGUucmF2ZWwoKSwgbXVfZXhhY3QsIFx1MDAyN2stLVx1MDAyNywgbHc9MSwgYWxwaGE9MC42LCBsYWJlbD1cdTAwMjdFeGFjdCBHUCByZWZcdTAwMjcpXG4gICAgYXguc2NhdHRlcihpbmQucmF2ZWwoKSwgbnAuemVyb3MobSksIG1hcmtlcj1cdTAwMjd8XHUwMDI3LCBzPTgwLCBjPVx1MDAyN3JcdTAwMjcsIHpvcmRlcj01LCBsYWJlbD1mXHUwMDI3bT17bX0gcHRzXHUwMDI3KVxuICAgIGF4LnNldF90aXRsZShsYWJlbCk7IGF4LnNldF94bGFiZWwoXHUwMDI3eFx1MDAyNylcbmF4ZXNbMF0uc2V0X3lsYWJlbChcdTAwMjdmKHgpXHUwMDI3KTsgcGx0LnN1cHRpdGxlKFx1MDAyN0luZHVjaW5nLVBvaW50IENvdW50IHZzIFVuY2VydGFpbnR5IFdpZHRoXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpOyBwbHQubGVnZW5kKCk7IHBsdC5zaG93KCkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiVHJhaW5pbmcgQ29zdCIsIk1lbW9yeSIsIkVMQk8gQm91bmQiLCJPdmVyY29uZmlkZW5jZSBSaXNrIiwiV2hlbiB0byBVc2UiLCJBY2N1cmFjeSB2cyBFeGFjdCJdLCJyb3dzIjpbWyJFeGFjdCBHUCIsIk8obsKzKSIsIk8obsKyKSIsIkV4YWN0IiwiTm9uZSIsIm4gXHUwMDNjIDUsMDAwLCBhbnkgZG9tYWluIiwiUmVmZXJlbmNlIl0sWyJGSVRDIiwiTyhubcKyKSIsIk8obm0pIiwiTm8gKG5vdCBhIHZhbGlkIGJvdW5kKSIsIkhpZ2gg4oCUIG5vIHRyYWNlIHBlbmFsdHkiLCJGYXN0IHNwYXJzZSBiYXNlbGluZSwgbG93LXN0YWtlcyByZWdyZXNzaW9uIiwiR29vZCBmb3IgbeKJpTAuMW4iXSxbIlZGRSAoU0dQUikiLCJPKG5twrIpIiwiTyhubSkiLCJZZXMgKHZhbGlkIGxvd2VyIGJvdW5kKSIsIkxvdyDigJQgdHJhY2UgcGVuYWx0eSBjb3JyZWN0cyIsIkRlZmF1bHQgc3BhcnNlIEdQOyBVUSBtYXR0ZXJzIiwiQmV0dGVyIGNhbGlicmF0ZWQgdGhhbiBGSVRDIl0sWyJTVkdQIiwiTyhibcKyKSBwZXIgYmF0Y2giLCJPKG3CsikiLCJZZXMgKHN0b2NoYXN0aWMgRUxCTykiLCJMb3cg4oCUIHZhcmlhdGlvbmFsIiwibiBcdTAwM2UgMTAwLDAwMDsgc3RyZWFtaW5nIGRhdGEiLCJTY2FsZXMgdG8gbWlsbGlvbnMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBsYWNpbmcgSW5kdWNpbmcgUG9pbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbG9jYXRpb24gb2YgaW5kdWNpbmcgcG9pbnRzIFogaGFzIGEgbGFyZ2UgZWZmZWN0IG9uIGFwcHJveGltYXRpb24gcXVhbGl0eS4gUG9vciBwbGFjZW1lbnQg4oCUIGUuZy4sIGFsbCBwb2ludHMgY2x1c3RlcmVkIGluIG9uZSByZWdpb24g4oCUIGxlYXZlcyBsYXJnZSBhcmVhcyBvZiB0aGUgaW5wdXQgc3BhY2UgdW5jb3ZlcmVkIGFuZCBkZWdyYWRlcyBwcmVkaWN0aW9ucyBlbHNld2hlcmUuIFRocmVlIHN0cmF0ZWdpZXMgYXJlIGNvbW1vbmx5IHVzZWQ6ICgxKSBmaXhlZCBncmlkIG92ZXIgdGhlIGlucHV0IGRvbWFpbiAod29ya3MgZm9yIGxvdy1kaW1lbnNpb25hbCBpbnB1dHMpLCAoMikgay1tZWFucyBjbHVzdGVyaW5nIG9uIHRoZSB0cmFpbmluZyBpbnB1dHMgWCAoY2FwdHVyZXMgdGhlIGRlbnNpdHkgb2YgdGhlIGRhdGEpLCBhbmQgKDMpIGdyYWRpZW50LWJhc2VkIG9wdGltaXNhdGlvbiBieSB0cmVhdGluZyBaIGFzIHBhcmFtZXRlcnMgaW4gdGhlIEVMQk8gKGxlYXJuZWQgaW5kdWNpbmcgcG9pbnRzLCB1c2VkIGluIEdQeVRvcmNoKS4gTGVhcm5lZCBwbGFjZW1lbnQgaXMgbW9zdCBmbGV4aWJsZSBidXQgYWRkcyBwYXJhbWV0ZXJzIHRvIHRoZSBvcHRpbWlzYXRpb24uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHcmlkIHBsYWNlbWVudDogZXZlbmx5IHNwYWNlZCBvdmVyIHRoZSBib3VuZGluZyBib3gg4oCUIHNpbXBsZSBidXQgcG9vciBmb3Igbm9uLXVuaWZvcm0gdHJhaW5pbmcgZGlzdHJpYnV0aW9ucyIsImstbWVhbnMgb24gWDogaW5pdGlhbGlzZSBaIGF0IGstbWVhbnMgY2VudHJvaWRzIG9mIHRyYWluaW5nIGlucHV0cyDigJQgZ29vZCBwcmFjdGljYWwgZGVmYXVsdCIsIkxlYXJuZWQgWjogaW5jbHVkZSBaIGluIGdyYWRpZW50IG9wdGltaXNhdGlvbiBvZiBFTEJPIOKAlCBiZXN0IHF1YWxpdHksIGhpZ2hlciBjb21wdXRlIiwiUmFuZG9tIHN1YnNldCBvZiB0cmFpbmluZyBwb2ludHM6IGZhc3QgaGV1cmlzdGljLCBubyBhZGRpdGlvbmFsIGNvbXB1dGF0aW9uIiwiRm9yIGQgXHUwMDNlIDMgaW5wdXQgZGltZW5zaW9ucywgZ3JpZCBhbmQgcmFuZG9tIHN1YnNldHMgZGVncmFkZSDigJQgay1tZWFucyBvciBsZWFybmVkIGFyZSBwcmVmZXJyZWQiLCJNb3JlIGluZHVjaW5nIHBvaW50cyBhbHdheXMgaGVscCBidXQgaW5jcmVhc2UgTyhtwrMpIGludmVyc2lvbiBjb3N0IOKAlCA1MOKAkzUwMCBpcyB0eXBpY2FsIHJhbmdlIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNWR1A6IFN0b2NoYXN0aWMgVmFyaWF0aW9uYWwgR1AgZm9yIE1hc3NpdmUgRGF0YXNldHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNWR1AgKFN0b2NoYXN0aWMgVmFyaWF0aW9uYWwgR1AsIEhlbnNtYW4gZXQgYWwuIDIwMTMpIGV4dGVuZHMgVkZFIHRvIG1pbmktYmF0Y2ggdHJhaW5pbmcuIFRoZSBFTEJPIGRlY29tcG9zZXMgYXMgYSBzdW0gb3ZlciBkYXRhIHBvaW50cywgc28gZWFjaCBtaW5pLWJhdGNoIGdpdmVzIGFuIHVuYmlhc2VkIGVzdGltYXRlIG9mIHRoZSBncmFkaWVudC4gVGhpcyBhbGxvd3MgdHJhaW5pbmcgb24gbWlsbGlvbnMgb2YgcG9pbnRzIHdpdGggYSBmaXhlZCBtZW1vcnkgZm9vdHByaW50IG9mIE8obcKyKS4gVGhlIHZhcmlhdGlvbmFsIHBhcmFtZXRlcnMgKG1lYW4gYW5kIGNvdmFyaWFuY2Ugb2YgcSh1KSkgYXJlIG1haW50YWluZWQgZ2xvYmFsbHkgYW5kIHVwZGF0ZWQgdmlhIHN0b2NoYXN0aWMgZ3JhZGllbnQgZGVzY2VudC4gVGhlIGtleSBkaWZmZXJlbmNlIGZyb20gVkZFL1NHUFIgaXMgdGhhdCBTVkdQIHN0b3JlcyB0aGUgdmFyaWF0aW9uYWwgZGlzdHJpYnV0aW9uIHEodSkgZXhwbGljaXRseSBhcyBwYXJhbWV0ZXJzIHJhdGhlciB0aGFuIGNvbXB1dGluZyBpdCBhbmFseXRpY2FsbHkgZnJvbSB0aGUgdHJhaW5pbmcgZGF0YSBpbiBvbmUgcGFzcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgZ3B5dG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5jbGFzcyBTVkdQTW9kZWwoZ3B5dG9yY2gubW9kZWxzLkFwcHJveGltYXRlR1ApOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbmR1Y2luZ19wb2ludHMpOlxuICAgICAgICB2ZCA9IGdweXRvcmNoLnZhcmlhdGlvbmFsLkNob2xlc2t5VmFyaWF0aW9uYWxEaXN0cmlidXRpb24oaW5kdWNpbmdfcG9pbnRzLnNpemUoMCkpXG4gICAgICAgIHZzID0gZ3B5dG9yY2gudmFyaWF0aW9uYWwuVmFyaWF0aW9uYWxTdHJhdGVneShcbiAgICAgICAgICAgIHNlbGYsIGluZHVjaW5nX3BvaW50cywgdmQsIGxlYXJuX2luZHVjaW5nX2xvY2F0aW9ucz1UcnVlKVxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHZzKVxuICAgICAgICBzZWxmLm1lYW5fbW9kdWxlID0gZ3B5dG9yY2gubWVhbnMuQ29uc3RhbnRNZWFuKClcbiAgICAgICAgc2VsZi5jb3Zhcl9tb2R1bGUgPSBncHl0b3JjaC5rZXJuZWxzLlNjYWxlS2VybmVsKGdweXRvcmNoLmtlcm5lbHMuUkJGS2VybmVsKCkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIGdweXRvcmNoLmRpc3RyaWJ1dGlvbnMuTXVsdGl2YXJpYXRlTm9ybWFsKFxuICAgICAgICAgICAgc2VsZi5tZWFuX21vZHVsZSh4KSwgc2VsZi5jb3Zhcl9tb2R1bGUoeCkpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuTiA9IDEwMDAwXG50cmFpbl94ID0gdG9yY2gucmFuZG4oTilcbnRyYWluX3kgPSB0b3JjaC5zaW4odHJhaW5feCAqIDIpICsgMC4zICogdG9yY2gucmFuZG4oTilcbmluZHVjaW5nX3B0cyA9IHRvcmNoLnJhbmRuKDEwMClcbm1vZGVsID0gU1ZHUE1vZGVsKGluZHVjaW5nX3B0cylcbmxpa2VsaWhvb2QgPSBncHl0b3JjaC5saWtlbGlob29kcy5HYXVzc2lhbkxpa2VsaWhvb2QoKVxubW9kZWwudHJhaW4oKTsgbGlrZWxpaG9vZC50cmFpbigpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKFxuICAgIFt7XHUwMDI3cGFyYW1zXHUwMDI3OiBtb2RlbC5wYXJhbWV0ZXJzKCl9LCB7XHUwMDI3cGFyYW1zXHUwMDI3OiBsaWtlbGlob29kLnBhcmFtZXRlcnMoKX1dLCBscj0wLjAxKVxuZWxibyA9IGdweXRvcmNoLm1sbHMuVmFyaWF0aW9uYWxFTEJPKGxpa2VsaWhvb2QsIG1vZGVsLCBudW1fZGF0YT1OKVxuZGF0YXNldCA9IHRvcmNoLnV0aWxzLmRhdGEuVGVuc29yRGF0YXNldCh0cmFpbl94LCB0cmFpbl95KVxubG9hZGVyID0gdG9yY2gudXRpbHMuZGF0YS5EYXRhTG9hZGVyKGRhdGFzZXQsIGJhdGNoX3NpemU9MjU2LCBzaHVmZmxlPVRydWUpXG5mb3IgZXBvY2ggaW4gcmFuZ2UoMyk6XG4gICAgZXBvY2hfbG9zcyA9IDAuMFxuICAgIGZvciB4X2JhdGNoLCB5X2JhdGNoIGluIGxvYWRlcjpcbiAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgIGxvc3MgPSAtZWxibyhtb2RlbCh4X2JhdGNoKSwgeV9iYXRjaClcbiAgICAgICAgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgIGVwb2NoX2xvc3MgKz0gbG9zcy5pdGVtKClcbiAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NoKzF9OiBhdmcgbG9zcz17ZXBvY2hfbG9zcy9sZW4obG9hZGVyKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1NWR1AgdHJhaW5lZCBvbiBOPXtOfSBwb2ludHMgd2l0aCBtPTEwMCBpbmR1Y2luZyAobWluaS1iYXRjaCBzaXplPTI1NilcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXhhY3QgR1BzIHNjYWxlIGFzIE8obsKzKSDigJQgaW1wcmFjdGljYWwgYmV5b25kIHJvdWdobHkgNSwwMDAgcG9pbnRzLiBTcGFyc2UgR1AgbWV0aG9kcyBpbnRyb2R1Y2UgbSDiiaogbiBpbmR1Y2luZyBwb2ludHMgWiB0byByZWR1Y2UgY29zdCB0byBPKG5twrIpLiBGSVRDIG1ha2VzIGEgY29uZGl0aW9uYWwtaW5kZXBlbmRlbmNlIGFwcHJveGltYXRpb24gdGhhdCBjYW4geWllbGQgb3ZlcmNvbmZpZGVudCBwcmVkaWN0aW9ucyBiZWNhdXNlIGl0IGxhY2tzIGEgdHJhY2UgcGVuYWx0eS4gVkZFIGlzIHRoZSBwcmluY2lwbGVkIGFsdGVybmF0aXZlOiBpdCBtYXhpbWlzZXMgYSB2YWxpZCBFTEJPIHRoYXQgaW5jbHVkZXMgYSB0cmFjZSBjb3JyZWN0aW9uLCBtYWtpbmcgdW5jZXJ0YWludHkgZXN0aW1hdGVzIGJldHRlciBjYWxpYnJhdGVkLiBTVkdQIGV4dGVuZHMgVkZFIHRvIG1pbmktYmF0Y2ggdHJhaW5pbmcsIGVuYWJsaW5nIE8oYm3CsikgcGVyLXN0ZXAgY29zdCBhbmQgbWFraW5nIEdQIHJlZ3Jlc3Npb24gZmVhc2libGUgZm9yIG1pbGxpb25zIG9mIG9ic2VydmF0aW9ucy4gSW5kdWNpbmcgcG9pbnQgcGxhY2VtZW50IG1hdHRlcnM6IGxlYXJuZWQgbG9jYXRpb25zIHZpYSBncmFkaWVudCBvcHRpbWlzYXRpb24gZ2l2ZSB0aGUgYmVzdCBxdWFsaXR5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRXhhY3QgR1A6IE8obsKzKSDigJQgdXNlIG9ubHkgZm9yIG4gXHUwMDNjIDUsMDAwIiwiSW5kdWNpbmcgcG9pbnRzIFo6IG0g4omqIG4gcHNldWRvLWlucHV0cyB0aGF0IHN1bW1hcmlzZSB0aGUgZGF0YXNldCwgY29zdCBPKG5twrIpIiwiRklUQzogY29uZGl0aW9uYWwgaW5kZXBlbmRlbmNlIGFwcHJveGltYXRpb24g4oCUIGZhc3QgYnV0IGNhbiBiZSBvdmVyY29uZmlkZW50IiwiVkZFIChUaXRzaWFzIDIwMDkpOiB2YWxpZCB2YXJpYXRpb25hbCBsb3dlciBib3VuZCDigJQgaW5jbHVkZXMgdHJhY2UgcGVuYWx0eSwgYmV0dGVyIGNhbGlicmF0ZWQiLCJTVkdQOiBtaW5pLWJhdGNoIEVMQk8g4oCUIHNjYWxlcyB0byBtaWxsaW9ucywgbWVtb3J5IE8obcKyKSBmaXhlZCIsIkxlYXJuZWQgaW5kdWNpbmcgcG9pbnRzOiB0cmVhdCBaIGFzIHBhcmFtZXRlcnMgaW4gRUxCTyBvcHRpbWlzYXRpb24gZm9yIGJlc3QgcXVhbGl0eSIsIkdQeVRvcmNoOiBTcGFyc2VHUFJlZ3Jlc3Npb24gKFNHUFIvVkZFKSBmb3IgbW9kZXJhdGUgbiwgU1ZHUCBmb3IgdmVyeSBsYXJnZSBuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Sparse GPs — Inducing Points, FITC, and VFE

## The O(n³) Bottleneck of Exact GPs

Exact GP regression requires inverting the n×n kernel matrix K + σ²_n I, which costs O(n³) time and O(n²) memory. For n = 1,000 this is fast; for n = 10,000 it takes minutes; for n = 100,000 it becomes intractable on a standard workstation. The core issue is that every training point contributes to every prediction — storing and inverting the full n×n matrix is unavoidable in the exact formulation. Sparse GP approximations attack this by introducing a much smaller set of m ≪ n representative points that summarise the entire dataset.

## Inducing Points — Reducing n to m

The inducing-point framework introduces a set of m pseudo-inputs Z = {z₁, …, zₘ} with corresponding function values u = f(Z). These inducing points are not observed data — they are auxiliary variables chosen to summarise the GP. The key insight is that if we can express the GP posterior in terms of u rather than f(X), we can work with an m×m system instead of n×n, reducing training cost from O(n³) to O(nm²) and memory from O(n²) to O(nm). Different sparse GP methods differ in how they approximate the joint distribution p(f, u).

- m ≪ n inducing points Z placed in the input domain — not observed data points
- u = f(Z) are function values at inducing points — key latent variables
- All approximations share O(nm²) training cost and O(m²) memory for the m×m system
- Inducing point locations Z can be fixed (grid/k-means) or learned by gradient descent on the ELBO
- Quality improves as m increases; m = n recovers exact GP at full O(n³) cost
- GPyTorch, GPflow, and scikit-learn support sparse GPs out of the box

## FITC: Fully Independent Training Conditional

FITC (Fully Independent Training Conditional, Snelson & Ghahramani 2006) approximates the true joint over training outputs as a product: q(f|u) = Πᵢ p(fᵢ|u). Each training output fᵢ is assumed independent of all others given the inducing values u. This factorisation makes the n×n training covariance block-diagonal with a rank-m update structure. The diagonal correction term Λ = diag(Kff − Qff) + σ²_n I captures the residual variance not explained by the inducing points. FITC prediction is O(nm²) for training and O(m³) for the inducing-point inversion.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1, 1)
    X2 = np.atleast_2d(X2).reshape(-1, 1)
    return sf2 * np.exp(-0.5 * (X1 - X2.T)**2 / ell**2)

def fitc_predict(X_train, y_train, X_test, X_ind, ell=1.0, sf2=1.0, noise_var=0.1):
    n, m = len(X_train), len(X_ind)
    Kuu = rbf_kernel(X_ind, X_ind, ell, sf2) + 1e-6 * np.eye(m)  # m x m
    Kuf = rbf_kernel(X_ind, X_train, ell, sf2)    # m x n
    Kus = rbf_kernel(X_ind, X_test, ell, sf2)     # m x n_test
    Luu = np.linalg.cholesky(Kuu)
    V = np.linalg.solve(Luu, Kuf)                 # m x n, Luu^{-1} Kuf
    Qff_diag = np.sum(V**2, axis=0)               # diag of Kuf^T Kuu^{-1} Kuf
    lam = sf2 - Qff_diag + noise_var              # FITC diagonal correction (length n)
    A = V @ (V / lam).T + np.eye(m)              # m x m
    LA = np.linalg.cholesky(A)
    b = np.linalg.solve(LA, V @ (y_train / lam))  # m
    W = np.linalg.solve(Luu, Kus)                 # m x n_test
    mu = W.T @ np.linalg.solve(LA.T, b)
    var = sf2 - np.sum(W**2, axis=0) + np.sum(np.linalg.solve(LA, W)**2, axis=0)
    return mu, np.sqrt(np.maximum(var, 0))

np.random.seed(42)
X_tr = np.random.uniform(-5, 5, 500)
y_tr = np.sin(X_tr) + 0.2 * np.random.randn(500)
X_ind = np.linspace(-5, 5, 20)
X_te = np.linspace(-6, 6, 200)
mu, std = fitc_predict(X_tr, y_tr, X_te, X_ind)
plt.figure(figsize=(10, 4))
plt.fill_between(X_te, mu - 2*std, mu + 2*std, alpha=0.25, label='±2σ')
plt.plot(X_te, mu, 'b-', lw=2, label='FITC mean')
plt.scatter(X_ind, np.zeros(20), marker='|', s=100, c='r', zorder=5, label='Inducing pts')
plt.title('FITC Sparse GP: n=500 training points, m=20 inducing (cost O(nm²))')
plt.xlabel('x'); plt.ylabel('f(x)'); plt.legend(); plt.tight_layout(); plt.show()
```

> **FITC Can Give Overconfident Predictions**: Because FITC treats training outputs as independent given u, it can underestimate posterior uncertainty — especially in regions between inducing points that still have training data. If your inducing points are too sparse, FITC may report low variance (high confidence) in gaps where the approximation is actually poor. VFE corrects this by bounding the true posterior from below.

## VFE: Variational Free Energy (Titsias 2009)

VFE (Variational Free Energy, Titsias 2009) frames sparse GP inference as variational inference. Instead of making a conditional-independence approximation like FITC, VFE minimises the KL divergence KL[q(f,u) || p(f,u|y)] by optimising a lower bound (ELBO) to the log marginal likelihood. The ELBO has the form: log p(y) ≥ log N(y | 0, Qnn + σ²_nI) − (1/2σ²_n) tr(Kff − Qnn) where Qnn = Knm Kmm⁻¹ Kmn. The trace term is a penalty that grows when the inducing points fail to explain the data variance — this prevents overconfidence. VFE is the principled sparse GP: FITC can be seen as VFE without the trace correction.

```python
import torch
import gpytorch
import numpy as np
import matplotlib.pyplot as plt

class SGPRModel(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood, inducing_points):
        super().__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ZeroMean()
        self.covar_module = gpytorch.kernels.InducingPointKernel(
            gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel()),
            inducing_points=inducing_points, likelihood=likelihood)

    def forward(self, x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        return gpytorch.distributions.MultivariateNormal(mean_x, covar_x)

torch.manual_seed(0)
n = 2000
train_x = torch.randn(n)
train_y = torch.sin(train_x * 3) + 0.2 * torch.randn(n)
inducing_pts = torch.linspace(-3, 3, 50)
likelihood = gpytorch.likelihoods.GaussianLikelihood()
model = SGPRModel(train_x, train_y, likelihood, inducing_pts)
model.train(); likelihood.train()
optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
for i in range(200):
    optimizer.zero_grad()
    loss = -mll(model(train_x), train_y)
    loss.backward(); optimizer.step()
    if (i + 1) % 50 == 0:
        ls = model.covar_module.base_kernel.base_kernel.lengthscale.item()
        print(f'Iter {i+1}: loss={loss.item():.4f}, lengthscale={ls:.3f}')
print('VFE/SGPR trained on n=2000 points using m=50 learned inducing points')
```

## FITC vs VFE — Overconfidence Issue Visualised

The practical difference between FITC and VFE becomes visible in extrapolation regions and between sparse inducing points. With too few inducing points, FITC may report near-zero variance in regions where the approximation quality is poor, because it does not include the trace penalty. VFE includes this trace term in its ELBO, which acts as a regulariser that widens uncertainty where the inducing points do not provide good coverage. In practice, VFE is preferred when uncertainty calibration matters; FITC is sometimes preferred for speed in low-stakes regression.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

np.random.seed(7)
n = 300
X_tr = np.sort(np.random.uniform(-4, 4, n)).reshape(-1, 1)
y_tr = np.sin(X_tr.ravel()) + 0.15 * np.random.randn(n)
X_te = np.linspace(-6, 6, 300).reshape(-1, 1)

# Exact GP on small subset (ground truth reference)
idx = np.random.choice(n, 80, replace=False)
kernel = RBF(length_scale=1.0) + WhiteKernel(noise_level=0.02)
gp_exact = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=2)
gp_exact.fit(X_tr[idx], y_tr[idx])
mu_exact, std_exact = gp_exact.predict(X_te, return_std=True)

fig, axes = plt.subplots(1, 2, figsize=(13, 4), sharey=True)
for ax, m, label in zip(axes, [4, 20],
    ['FITC-like (m=4, overconfident in gaps)', 'VFE-like (m=20, better calibrated)']):
    ind = np.linspace(-4, 4, m).reshape(-1, 1)
    gp_sparse = GaussianProcessRegressor(kernel=RBF() + WhiteKernel(), n_restarts_optimizer=1)
    gp_sparse.fit(np.vstack([ind, X_tr[:40]]), np.hstack([np.sin(ind.ravel()), y_tr[:40]]))
    mu, std = gp_sparse.predict(X_te, return_std=True)
    ax.fill_between(X_te.ravel(), mu - 2*std, mu + 2*std, alpha=0.25)
    ax.plot(X_te.ravel(), mu, lw=2, label='Sparse mean')
    ax.plot(X_te.ravel(), mu_exact, 'k--', lw=1, alpha=0.6, label='Exact GP ref')
    ax.scatter(ind.ravel(), np.zeros(m), marker='|', s=80, c='r', zorder=5, label=f'm={m} pts')
    ax.set_title(label); ax.set_xlabel('x')
axes[0].set_ylabel('f(x)'); plt.suptitle('Inducing-Point Count vs Uncertainty Width')
plt.tight_layout(); plt.legend(); plt.show()
```

| Method | Training Cost | Memory | ELBO Bound | Overconfidence Risk | When to Use | Accuracy vs Exact |
| --- | --- | --- | --- | --- | --- | --- |
| Exact GP | O(n³) | O(n²) | Exact | None | n < 5,000, any domain | Reference |
| FITC | O(nm²) | O(nm) | No (not a valid bound) | High — no trace penalty | Fast sparse baseline, low-stakes regression | Good for m≥0.1n |
| VFE (SGPR) | O(nm²) | O(nm) | Yes (valid lower bound) | Low — trace penalty corrects | Default sparse GP; UQ matters | Better calibrated than FITC |
| SVGP | O(bm²) per batch | O(m²) | Yes (stochastic ELBO) | Low — variational | n > 100,000; streaming data | Scales to millions |

## Placing Inducing Points

The location of inducing points Z has a large effect on approximation quality. Poor placement — e.g., all points clustered in one region — leaves large areas of the input space uncovered and degrades predictions elsewhere. Three strategies are commonly used: (1) fixed grid over the input domain (works for low-dimensional inputs), (2) k-means clustering on the training inputs X (captures the density of the data), and (3) gradient-based optimisation by treating Z as parameters in the ELBO (learned inducing points, used in GPyTorch). Learned placement is most flexible but adds parameters to the optimisation.

- Grid placement: evenly spaced over the bounding box — simple but poor for non-uniform training distributions
- k-means on X: initialise Z at k-means centroids of training inputs — good practical default
- Learned Z: include Z in gradient optimisation of ELBO — best quality, higher compute
- Random subset of training points: fast heuristic, no additional computation
- For d > 3 input dimensions, grid and random subsets degrade — k-means or learned are preferred
- More inducing points always help but increase O(m³) inversion cost — 50–500 is typical range

## SVGP: Stochastic Variational GP for Massive Datasets

SVGP (Stochastic Variational GP, Hensman et al. 2013) extends VFE to mini-batch training. The ELBO decomposes as a sum over data points, so each mini-batch gives an unbiased estimate of the gradient. This allows training on millions of points with a fixed memory footprint of O(m²). The variational parameters (mean and covariance of q(u)) are maintained globally and updated via stochastic gradient descent. The key difference from VFE/SGPR is that SVGP stores the variational distribution q(u) explicitly as parameters rather than computing it analytically from the training data in one pass.

```python
import torch
import gpytorch
import numpy as np

class SVGPModel(gpytorch.models.ApproximateGP):
    def __init__(self, inducing_points):
        vd = gpytorch.variational.CholeskyVariationalDistribution(inducing_points.size(0))
        vs = gpytorch.variational.VariationalStrategy(
            self, inducing_points, vd, learn_inducing_locations=True)
        super().__init__(vs)
        self.mean_module = gpytorch.means.ConstantMean()
        self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())

    def forward(self, x):
        return gpytorch.distributions.MultivariateNormal(
            self.mean_module(x), self.covar_module(x))

torch.manual_seed(42)
N = 10000
train_x = torch.randn(N)
train_y = torch.sin(train_x * 2) + 0.3 * torch.randn(N)
inducing_pts = torch.randn(100)
model = SVGPModel(inducing_pts)
likelihood = gpytorch.likelihoods.GaussianLikelihood()
model.train(); likelihood.train()
optimizer = torch.optim.Adam(
    [{'params': model.parameters()}, {'params': likelihood.parameters()}], lr=0.01)
elbo = gpytorch.mlls.VariationalELBO(likelihood, model, num_data=N)
dataset = torch.utils.data.TensorDataset(train_x, train_y)
loader = torch.utils.data.DataLoader(dataset, batch_size=256, shuffle=True)
for epoch in range(3):
    epoch_loss = 0.0
    for x_batch, y_batch in loader:
        optimizer.zero_grad()
        loss = -elbo(model(x_batch), y_batch)
        loss.backward(); optimizer.step()
        epoch_loss += loss.item()
    print(f'Epoch {epoch+1}: avg loss={epoch_loss/len(loader):.4f}')
print(f'SVGP trained on N={N} points with m=100 inducing (mini-batch size=256)')
```

## Key Takeaways

Exact GPs scale as O(n³) — impractical beyond roughly 5,000 points. Sparse GP methods introduce m ≪ n inducing points Z to reduce cost to O(nm²). FITC makes a conditional-independence approximation that can yield overconfident predictions because it lacks a trace penalty. VFE is the principled alternative: it maximises a valid ELBO that includes a trace correction, making uncertainty estimates better calibrated. SVGP extends VFE to mini-batch training, enabling O(bm²) per-step cost and making GP regression feasible for millions of observations. Inducing point placement matters: learned locations via gradient optimisation give the best quality.

- Exact GP: O(n³) — use only for n < 5,000
- Inducing points Z: m ≪ n pseudo-inputs that summarise the dataset, cost O(nm²)
- FITC: conditional independence approximation — fast but can be overconfident
- VFE (Titsias 2009): valid variational lower bound — includes trace penalty, better calibrated
- SVGP: mini-batch ELBO — scales to millions, memory O(m²) fixed
- Learned inducing points: treat Z as parameters in ELBO optimisation for best quality
- GPyTorch: SparseGPRegression (SGPR/VFE) for moderate n, SVGP for very large n

---

