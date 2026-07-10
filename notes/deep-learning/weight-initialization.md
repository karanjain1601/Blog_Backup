---
title: "Weight Initialization — Xavier/Glorot and Kaiming/He"
slug: "weight-initialization"
description: "Derive variance-preserving weight initialization from first principles, implement Xavier and He initialization, compare their gradient flow with tanh vs ReLU, and visualise activation and gradient norms across depth."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2VpZ2h0IGluaXRpYWxpc2F0aW9uIGlzIHRoZSBzdGFydGluZyBwb2ludCBmb3IgYWxsIHRyYWluaW5nIGR5bmFtaWNzLiBJZiB3ZWlnaHRzIGFyZSB0b28gbGFyZ2UsIGFjdGl2YXRpb25zIGFuZCBncmFkaWVudHMgZXhwbG9kZTsgdG9vIHNtYWxsLCB0aGV5IHZhbmlzaC4gQm90aCBwYXRob2xvZ2llcyBwcmV2ZW50IGxlYXJuaW5nIGluIGRlZXAgbmV0d29ya3MuIFZhcmlhbmNlLXByZXNlcnZpbmcgaW5pdGlhbGlzYXRpb24gc2NoZW1lcyDigJQgWGF2aWVyL0dsb3JvdCBmb3IgdGFuaC9zaWdtb2lkIGFuZCBLYWltaW5nL0hlIGZvciBSZUxVIOKAlCBhcmUgZGVyaXZlZCBmcm9tIHRoZSByZXF1aXJlbWVudCB0aGF0IHRoZSB2YXJpYW5jZSBvZiBhY3RpdmF0aW9ucyBhbmQgZ3JhZGllbnRzIHN0YXkgYXBwcm94aW1hdGVseSBjb25zdGFudCBhcyBzaWduYWxzIHByb3BhZ2F0ZSB0aHJvdWdoIGRlcHRoLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBWYXJpYW5jZSBQcm9wYWdhdGlvbiBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBsaW5lYXIgbGF5ZXIgeiA9IFd4IChpZ25vcmluZyBiaWFzLCBwcmUtYWN0aXZhdGlvbiksIFZhcih64bWiKSA9IG7htaLigpkgwrcgVmFyKFcpIMK3IFZhcih4KSBpZiB3ZWlnaHRzIGFuZCBpbnB1dHMgYXJlIGkuaS5kLiBhbmQgemVyby1tZWFuLiBUbyBrZWVwIFZhcih6KSA9IFZhcih4KSAodmFyaWFuY2UgcHJlc2VydmF0aW9uKSwgd2UgbmVlZCBWYXIoVykgPSAxL27htaLigpkg4oCUIHRoZSBMZUN1biBpbml0aWFsaXNhdGlvbi4gRm9yIHRoZSBiYWNrd2FyZCBwYXNzOiBWYXIo4oiCTC/iiIJ4KSA9IG7igpLhtaTigpwgwrcgVmFyKFcpIMK3IFZhcijiiIJML+KIgnopLCByZXF1aXJpbmcgVmFyKFcpID0gMS9u4oKS4bWk4oKcLiBYYXZpZXIvR2xvcm90IGNvbXByb21pc2VzOiBWYXIoVykgPSAyLyhu4bWi4oKZICsgbuKCkuG1pOKCnCksIG1haW50YWluaW5nIHNpZ25hbCBpbiBib3RoIGRpcmVjdGlvbnMgZm9yIHplcm8tbWVhbiBzeW1tZXRyaWMgYWN0aXZhdGlvbnMgbGlrZSB0YW5oLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ilhhdmllci9HbG9yb3QgSW5pdGlhbGlzYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciB0YW5oIGFuZCBzaWdtb2lkIGFjdGl2YXRpb25zOiBXIH4gVSgt4oiaKDYvKG7htaLigpkgKyBu4oKS4bWk4oKcKSksICviiJooNi8obuG1ouKCmSArIG7igpLhtaTigpwpKSkgb3IgZXF1aXZhbGVudGx5IFcgfiBOKDAsIDIvKG7htaLigpkgKyBu4oKS4bWk4oKcKSkuIERlcml2ZWQgYnkgR2xvcm90IFx1MDAyNiBCZW5naW8gKDIwMTApIGFzc3VtaW5nIGxpbmVhciBhY3RpdmF0aW9ucyAodGFuaCDiiYggbGluZWFyIG5lYXIgb3JpZ2luKSBhbmQgcmVxdWlyaW5nIFZhcihmb3J3YXJkIHNpZ25hbCkg4omIIFZhcihiYWNrd2FyZCBzaWduYWwpLiBGb3Igc2lnbW9pZCwgdGhlIGVmZmVjdGl2ZSBncmFkaWVudCBhdCB6ZXJvIGlzIDAuMjUsIHNvIGEgZ2FpbiBvZiA0IGlzIGFwcGxpZWQ6IHN0ZCA9IGdhaW4gw5cg4oiaKDIvKG7htaLigpkgKyBu4oKS4bWk4oKcKSkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2FpbWluZy9IZSBJbml0aWFsaXNhdGlvbiBmb3IgUmVMVSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVMVSB6ZXJvcyBvdXQgaGFsZiBpdHMgaW5wdXRzLCBoYWx2aW5nIHRoZSBlZmZlY3RpdmUgdmFyaWFuY2UuIEhlIGV0IGFsLiAoMjAxNSkgYWNjb3VudCBmb3IgdGhpczogVmFyKFcpID0gMi9u4bWi4oKZIHNvIHRoYXQgYWZ0ZXIgUmVMVSwgdGhlIHZhcmlhbmNlIGlzIHByZXNlcnZlZC4gSW4gbm9ybWFsIGZvcm06IFcgfiBOKDAsIOKImigyL27htaLigpkpKS4gRm9yIExlYWt5IFJlTFUgd2l0aCBzbG9wZSDOsTogVmFyKFcpID0gMi8oKDErzrHCsinCt27htaLigpkpLiBUaGUgUHlUb3JjaCBmdW5jdGlvbiBubi5pbml0LmthaW1pbmdfbm9ybWFsXyBhY2NlcHRzIGEgbm9ubGluZWFyaXR5IGFyZ3VtZW50IGFuZCBjb21wdXRlcyB0aGUgY29ycmVjdCBnYWluIGF1dG9tYXRpY2FsbHkuIGZhbl9pbiBtb2RlIChkZWZhdWx0KSBwcmVzZXJ2ZXMgZm9yd2FyZCBzaWduYWw7IGZhbl9vdXQgbW9kZSBwcmVzZXJ2ZXMgYmFja3dhcmQgc2lnbmFsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBhY3RpdmF0aW9uX3ZhcmlhbmNlX3RyYWNlKGluaXRfc3RkX2ZuLCBhY3RpdmF0aW9uX2ZuLCBkZXB0aD0yMCwgd2lkdGg9NTEyLCBtPTI1Niwgc2VlZD0wKTpcbiAgICBcIlwiXCJUcmFjZSBhY3RpdmF0aW9uIHZhcmlhbmNlIGxheWVyIGJ5IGxheWVyIHdpdGggYSBnaXZlbiBpbml0IGFuZCBhY3RpdmF0aW9uLlwiXCJcIlxuICAgIG5wLnJhbmRvbS5zZWVkKHNlZWQpXG4gICAgeCA9IG5wLnJhbmRvbS5yYW5kbihtLCB3aWR0aClcbiAgICB2YXJpYW5jZXMgPSBbeC52YXIoKV1cbiAgICBmb3IgXyBpbiByYW5nZShkZXB0aCk6XG4gICAgICAgIG5faW4sIG5fb3V0ID0gd2lkdGgsIHdpZHRoXG4gICAgICAgIHN0ZCA9IGluaXRfc3RkX2ZuKG5faW4sIG5fb3V0KVxuICAgICAgICBXID0gbnAucmFuZG9tLnJhbmRuKG5fb3V0LCBuX2luKSAqIHN0ZFxuICAgICAgICBiID0gbnAuemVyb3Mobl9vdXQpXG4gICAgICAgIHogPSB4IEAgVy5UICsgYlxuICAgICAgICB4ID0gYWN0aXZhdGlvbl9mbih6KVxuICAgICAgICB2YXJpYW5jZXMuYXBwZW5kKHgudmFyKCkpXG4gICAgcmV0dXJuIHZhcmlhbmNlc1xuXG5kZWYgcmVsdSh6KTogcmV0dXJuIG5wLm1heGltdW0oMCwgeilcbmRlZiB0YW5oX2ZuKHopOiByZXR1cm4gbnAudGFuaCh6KVxuXG54YXZpZXJfc3RkID0gbGFtYmRhIG5faW4sIG5fb3V0OiBucC5zcXJ0KDIuMCAvIChuX2luICsgbl9vdXQpKVxuaGVfc3RkICAgICA9IGxhbWJkYSBuX2luLCBuX291dDogbnAuc3FydCgyLjAgLyBuX2luKVxubGVjdW5fc3RkICA9IGxhbWJkYSBuX2luLCBuX291dDogbnAuc3FydCgxLjAgLyBuX2luKVxuc21hbGxfc3RkICA9IGxhbWJkYSBuX2luLCBuX291dDogMC4wMVxuXG5wcmludChcdTAwMjdBY3RpdmF0aW9uIHZhcmlhbmNlIHRyYWNlIChkZXB0aD0yMCwgc2hvdWxkIHN0YXkgbmVhciAxLjApOlx1MDAyNylcbmZvciBsYWJlbCwgaW5pdF9mbiwgYWN0X2ZuIGluIFtcbiAgICAoXHUwMDI3WGF2aWVyK3RhbmhcdTAwMjcsIHhhdmllcl9zdGQsIHRhbmhfZm4pLFxuICAgIChcdTAwMjdIZStSZUxVXHUwMDI3LCAgICAgaGVfc3RkLCAgICAgcmVsdSksXG4gICAgKFx1MDAyN0xlQ3VuK3RhbmhcdTAwMjcsICBsZWN1bl9zdGQsICB0YW5oX2ZuKSxcbiAgICAoXHUwMDI3c21hbGwrUmVMVVx1MDAyNywgIHNtYWxsX3N0ZCwgIHJlbHUpLFxuXTpcbiAgICB2YXJzID0gYWN0aXZhdGlvbl92YXJpYW5jZV90cmFjZShpbml0X2ZuLCBhY3RfZm4pXG4gICAgcHJpbnQoZlx1MDAyNyAge2xhYmVsOlx1MDAzZTE0fTogbGF5ZXIwPXt2YXJzWzBdOi4zZn0gIGxheWVyNT17dmFyc1s1XTouM2Z9ICBcdTAwMjdcbiAgICAgICAgICBmXHUwMDI3bGF5ZXIxMD17dmFyc1sxMF06LjNmfSAgbGF5ZXIyMD17dmFyc1stMV06LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJYYXZpZXIgdnMgSGUg4oCUIEdyYWRpZW50IEZsb3cgQ29tcGFyaXNvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBidWlsZF9kZWVwX25ldChkZXB0aCwgd2lkdGgsIGluaXRfbmFtZSwgYWN0X25hbWUpOlxuICAgIGxheWVycyA9IFtdXG4gICAgZm9yIGkgaW4gcmFuZ2UoZGVwdGgpOlxuICAgICAgICBsaW4gPSBubi5MaW5lYXIod2lkdGgsIHdpZHRoLCBiaWFzPUZhbHNlKVxuICAgICAgICBpZiBpbml0X25hbWUgPT0gXHUwMDI3eGF2aWVyXHUwMDI3OlxuICAgICAgICAgICAgbm4uaW5pdC54YXZpZXJfbm9ybWFsXyhsaW4ud2VpZ2h0KVxuICAgICAgICBlbGlmIGluaXRfbmFtZSA9PSBcdTAwMjdoZVx1MDAyNzpcbiAgICAgICAgICAgIG5uLmluaXQua2FpbWluZ19ub3JtYWxfKGxpbi53ZWlnaHQsIG5vbmxpbmVhcml0eT1cdTAwMjdyZWx1XHUwMDI3KVxuICAgICAgICBlbGlmIGluaXRfbmFtZSA9PSBcdTAwMjdzbWFsbFx1MDAyNzpcbiAgICAgICAgICAgIG5uLmluaXQubm9ybWFsXyhsaW4ud2VpZ2h0LCAwLCAwLjAxKVxuICAgICAgICBsYXllcnMuYXBwZW5kKGxpbilcbiAgICAgICAgYWN0ID0gbm4uVGFuaCgpIGlmIGFjdF9uYW1lID09IFx1MDAyN3RhbmhcdTAwMjcgZWxzZSBubi5SZUxVKClcbiAgICAgICAgbGF5ZXJzLmFwcGVuZChhY3QpXG4gICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwoKmxheWVycylcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5kZXB0aCwgd2lkdGgsIG0gPSAxNSwgMTI4LCA2NFxuXG5mb3IgaW5pdF9uYW1lLCBhY3RfbmFtZSBpbiBbKFx1MDAyN3hhdmllclx1MDAyNywgXHUwMDI3dGFuaFx1MDAyNyksIChcdTAwMjdoZVx1MDAyNywgXHUwMDI3cmVsdVx1MDAyNyksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAoXHUwMDI3eGF2aWVyXHUwMDI3LCBcdTAwMjdyZWx1XHUwMDI3KSwgKFx1MDAyN3NtYWxsXHUwMDI3LCBcdTAwMjdyZWx1XHUwMDI3KV06XG4gICAgbW9kZWwgPSBidWlsZF9kZWVwX25ldChkZXB0aCwgd2lkdGgsIGluaXRfbmFtZSwgYWN0X25hbWUpXG4gICAgeCA9IHRvcmNoLnJhbmRuKG0sIHdpZHRoKVxuICAgIG91dCA9IG1vZGVsKHgpXG4gICAgb3V0LnN1bSgpLmJhY2t3YXJkKClcbiAgICBncmFkX25vcm1zID0gW21vZC53ZWlnaHQuZ3JhZC5ub3JtKCkuaXRlbSgpXG4gICAgICAgICAgICAgICAgICBmb3IgbW9kIGluIG1vZGVsLm1vZHVsZXMoKVxuICAgICAgICAgICAgICAgICAgaWYgaXNpbnN0YW5jZShtb2QsIG5uLkxpbmVhcikgYW5kIG1vZC53ZWlnaHQuZ3JhZCBpcyBub3QgTm9uZV1cbiAgICB2YW5pc2ggPSBncmFkX25vcm1zWzBdIFx1MDAzYyAxZS00XG4gICAgZXhwbG9kZSA9IGdyYWRfbm9ybXNbLTFdIFx1MDAzZSAxZTNcbiAgICBwcmludChmXHUwMDI3e2luaXRfbmFtZTpcdTAwM2U4fSt7YWN0X25hbWU6XHUwMDNjNX06IFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjdmaXJzdF9ncmFkPXtncmFkX25vcm1zWzBdOi4yZX0gIGxhc3RfZ3JhZD17Z3JhZF9ub3Jtc1stMV06LjJlfSAgXHUwMDI3XG4gICAgICAgICAgZlx1MDAyN3ZhbmlzaGluZz17dmFuaXNofSAgZXhwbG9kaW5nPXtleHBsb2RlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQeVRvcmNoIEluaXRpYWxpc2F0aW9uIEFQSSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBhcHBseV9pbml0KG1vZGVsLCBpbml0X25hbWUpOlxuICAgIGZvciBtIGluIG1vZGVsLm1vZHVsZXMoKTpcbiAgICAgICAgaWYgaXNpbnN0YW5jZShtLCBubi5MaW5lYXIpOlxuICAgICAgICAgICAgaWYgaW5pdF9uYW1lID09IFx1MDAyN3hhdmllcl91bmlmb3JtXHUwMDI3OlxuICAgICAgICAgICAgICAgIG5uLmluaXQueGF2aWVyX3VuaWZvcm1fKG0ud2VpZ2h0LCBnYWluPW5uLmluaXQuY2FsY3VsYXRlX2dhaW4oXHUwMDI3dGFuaFx1MDAyNykpXG4gICAgICAgICAgICBlbGlmIGluaXRfbmFtZSA9PSBcdTAwMjd4YXZpZXJfbm9ybWFsXHUwMDI3OlxuICAgICAgICAgICAgICAgIG5uLmluaXQueGF2aWVyX25vcm1hbF8obS53ZWlnaHQpXG4gICAgICAgICAgICBlbGlmIGluaXRfbmFtZSA9PSBcdTAwMjdrYWltaW5nX3VuaWZvcm1cdTAwMjc6XG4gICAgICAgICAgICAgICAgbm4uaW5pdC5rYWltaW5nX3VuaWZvcm1fKG0ud2VpZ2h0LCBub25saW5lYXJpdHk9XHUwMDI3cmVsdVx1MDAyNylcbiAgICAgICAgICAgIGVsaWYgaW5pdF9uYW1lID09IFx1MDAyN2thaW1pbmdfbm9ybWFsXHUwMDI3OlxuICAgICAgICAgICAgICAgIG5uLmluaXQua2FpbWluZ19ub3JtYWxfKG0ud2VpZ2h0LCBub25saW5lYXJpdHk9XHUwMDI3cmVsdVx1MDAyNylcbiAgICAgICAgICAgIGVsaWYgaW5pdF9uYW1lID09IFx1MDAyN29ydGhvZ29uYWxcdTAwMjc6XG4gICAgICAgICAgICAgICAgbm4uaW5pdC5vcnRob2dvbmFsXyhtLndlaWdodClcbiAgICAgICAgICAgIG5uLmluaXQuemVyb3NfKG0uYmlhcylcbiAgICByZXR1cm4gbW9kZWxcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmZvciBpbml0X25hbWUgaW4gW1x1MDAyN3hhdmllcl91bmlmb3JtXHUwMDI3LCBcdTAwMjd4YXZpZXJfbm9ybWFsXHUwMDI3LCBcdTAwMjdrYWltaW5nX3VuaWZvcm1cdTAwMjcsXG4gICAgICAgICAgICAgICAgICAgXHUwMDI3a2FpbWluZ19ub3JtYWxcdTAwMjcsIFx1MDAyN29ydGhvZ29uYWxcdTAwMjddOlxuICAgIG1vZGVsID0gYXBwbHlfaW5pdChubi5TZXF1ZW50aWFsKFxuICAgICAgICBubi5MaW5lYXIoMTI4LCAyNTYpLCBubi5SZUxVKCksXG4gICAgICAgIG5uLkxpbmVhcigyNTYsIDEyOCksIG5uLlJlTFUoKSxcbiAgICAgICAgbm4uTGluZWFyKDEyOCwgMTApXG4gICAgKSwgaW5pdF9uYW1lKVxuICAgIHdlaWdodHMgPSBbbS53ZWlnaHQgZm9yIG0gaW4gbW9kZWwubW9kdWxlcygpIGlmIGlzaW5zdGFuY2UobSwgbm4uTGluZWFyKV1cbiAgICBzdGRzID0gW3cuc3RkKCkuaXRlbSgpIGZvciB3IGluIHdlaWdodHNdXG4gICAgcHJpbnQoZlx1MDAyN3tpbml0X25hbWU6XHUwMDNlMTh9OiBsYXllciBzdGRzID0ge1tmXCJ7czouNGZ9XCIgZm9yIHMgaW4gc3Rkc119XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUnVsZSBvZiBUaHVtYiBmb3IgQ2hvb3NpbmcgSW5pdGlhbGlzYXRpb24iLCJjb250ZW50IjoiVXNlIEhlL0thaW1pbmcgZm9yIFJlTFUgYW5kIExlYWt5IFJlTFUg4oCUIGl0IGFjY291bnRzIGZvciB0aGUgNTAlIHplcm9pbmcuIFVzZSBYYXZpZXIvR2xvcm90IGZvciB0YW5oLCBzaWdtb2lkLCBhbmQgbGluZWFyIGFjdGl2YXRpb25zLiBVc2UgTGVDdW4gZm9yIFNFTFUgKHNlbGYtbm9ybWFsaXNpbmcgbmV0d29ya3MpLiBVc2UgT3J0aG9nb25hbCBmb3IgUk5OcyB0byBwcmVzZXJ2ZSBncmFkaWVudCBub3JtcyBhY3Jvc3MgdGltZSBzdGVwcy4gQWx3YXlzIGluaXRpYWxpc2UgYmlhc2VzIHRvIHplcm8gdW5sZXNzIHRoZXJlIGlzIGEgc3BlY2lmaWMgcmVhc29uIG90aGVyd2lzZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcmFkaWVudCBOb3JtIE1vbml0b3JpbmcgQWNyb3NzIExheWVycyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBncmFkX25vcm1fcGVyX2xheWVyKGluaXRfbmFtZSwgZGVwdGg9MTIsIHdpZHRoPTEyOCwgbT02NCwgc2VlZD0wKTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZChzZWVkKVxuICAgIGxheWVycyA9IFtdXG4gICAgZm9yIF8gaW4gcmFuZ2UoZGVwdGgpOlxuICAgICAgICBsaW4gPSBubi5MaW5lYXIod2lkdGgsIHdpZHRoLCBiaWFzPVRydWUpXG4gICAgICAgIGlmIGluaXRfbmFtZSA9PSBcdTAwMjdoZVx1MDAyNzpcbiAgICAgICAgICAgIG5uLmluaXQua2FpbWluZ19ub3JtYWxfKGxpbi53ZWlnaHQsIG5vbmxpbmVhcml0eT1cdTAwMjdyZWx1XHUwMDI3KVxuICAgICAgICBlbGlmIGluaXRfbmFtZSA9PSBcdTAwMjd4YXZpZXJcdTAwMjc6XG4gICAgICAgICAgICBubi5pbml0Lnhhdmllcl9ub3JtYWxfKGxpbi53ZWlnaHQpXG4gICAgICAgIGVsaWYgaW5pdF9uYW1lID09IFx1MDAyN3NtYWxsXHUwMDI3OlxuICAgICAgICAgICAgbm4uaW5pdC5ub3JtYWxfKGxpbi53ZWlnaHQsIDAsIDAuMDEpXG4gICAgICAgIG5uLmluaXQuemVyb3NfKGxpbi5iaWFzKVxuICAgICAgICBsYXllcnMuZXh0ZW5kKFtsaW4sIG5uLlJlTFUoKV0pXG4gICAgbW9kZWwgPSBubi5TZXF1ZW50aWFsKCpsYXllcnMpXG4gICAgeCA9IHRvcmNoLnJhbmRuKG0sIHdpZHRoKVxuICAgIG91dCA9IG1vZGVsKHgpXG4gICAgb3V0LnN1bSgpLmJhY2t3YXJkKClcbiAgICBub3JtcyA9IFtdXG4gICAgZm9yIG1vZCBpbiBtb2RlbC5tb2R1bGVzKCk6XG4gICAgICAgIGlmIGlzaW5zdGFuY2UobW9kLCBubi5MaW5lYXIpIGFuZCBtb2Qud2VpZ2h0LmdyYWQgaXMgbm90IE5vbmU6XG4gICAgICAgICAgICBub3Jtcy5hcHBlbmQobW9kLndlaWdodC5ncmFkLm5vcm0oKS5pdGVtKCkpXG4gICAgcmV0dXJuIG5vcm1zXG5cbmZvciBpbml0X25hbWUgaW4gW1x1MDAyN2hlXHUwMDI3LCBcdTAwMjd4YXZpZXJcdTAwMjcsIFx1MDAyN3NtYWxsXHUwMDI3XTpcbiAgICBub3JtcyA9IGdyYWRfbm9ybV9wZXJfbGF5ZXIoaW5pdF9uYW1lKVxuICAgIHByaW50KGZcdTAwMjd7aW5pdF9uYW1lOlx1MDAzZTh9OiBcdTAwMjcgKyBcdTAwMjcgIFx1MDAyNy5qb2luKGZcdTAwMjdMe2krMX09e246LjNmfVx1MDAyNyBmb3IgaSwgbiBpbiBlbnVtZXJhdGUobm9ybXMpKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbml0aWFsaXNhdGlvbiBNZXRob2QgUmVmZXJlbmNlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkFjdGl2YXRpb24iLCJGb3JtdWxhIChzdGQpIiwiVmFyaWFuY2UgVGFyZ2V0IiwiV2hlbiB0byBVc2UiXSwicm93cyI6W1siWGF2aWVyIFVuaWZvcm0iLCJ0YW5oLCBzaWdtb2lkLCBsaW5lYXIiLCLiiJooNi8obl9pbituX291dCkpIiwiVmFyKGZvcndhcmQp4omIVmFyKGJhY2t3YXJkKSIsIkRlZmF1bHQgZm9yIHRhbmgvc2lnbW9pZCBuZXR3b3JrcyJdLFsiWGF2aWVyIE5vcm1hbCIsInRhbmgsIHNpZ21vaWQsIGxpbmVhciIsIuKImigyLyhuX2luK25fb3V0KSkiLCJTYW1lIGFzIHVuaWZvcm0gKGRpZmZlcmVudCBkaXN0KSIsIk5vcm1hbCB2YXJpYW50IG9mIFhhdmllciDigJQgb2Z0ZW4gaW50ZXJjaGFuZ2VhYmxlIl0sWyJIZS9LYWltaW5nIE5vcm1hbCIsIlJlTFUsIExlYWt5IFJlTFUiLCLiiJooMi9uX2luKSIsIlZhciBwcmVzZXJ2ZWQgYWZ0ZXIgUmVMVSB6ZXJvaW5nIiwiRGVmYXVsdCBmb3IgUmVMVSBuZXR3b3JrcyDigJQgQ05OcywgTUxQcyJdLFsiTGVDdW4gTm9ybWFsIiwiU0VMVSIsIuKImigxL25faW4pIiwiVW5pdCB2YXJpYW5jZSBmb3Igc2VsZi1ub3JtYWxpc2luZyIsIlNlbGYtbm9ybWFsaXNpbmcgbmV0d29ya3Mgd2l0aCBTRUxVIGFjdGl2YXRpb24iXSxbIk9ydGhvZ29uYWwiLCJBbnkgKGVzcC4gUk5OcykiLCJSYW5kb20gb3J0aG9nb25hbCBtYXRyaXgiLCJQcmVzZXJ2ZXMgZ3JhZGllbnQgbm9ybXMgb3ZlciB0aW1lIiwiUk5Ocywgc2VxdWVuY2UgbW9kZWxzLCBhdm9pZCB2YW5pc2hpbmcgb3ZlciBzdGVwcyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3J0aG9nb25hbCBJbml0aWFsaXNhdGlvbiBmb3IgUmVjdXJyZW50IE5ldHdvcmtzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiByZWN1cnJlbnQgbmV0d29ya3MsIHRoZSB3ZWlnaHQgbWF0cml4IFdfaCBpcyBhcHBsaWVkIFQgdGltZXMgKG9uY2UgcGVyIHRpbWVzdGVwKTogaOKCnCA9IGYoV19oIGjigpzigovigoEgKyBXX3ggeOKCnCkuIElmIFdfaCBoYXMgc2luZ3VsYXIgdmFsdWVzIFx1MDAzZSAxLCBncmFkaWVudHMgZXhwbG9kZTsgXHUwMDNjIDEsIHRoZXkgdmFuaXNoLiBPcnRob2dvbmFsIG1hdHJpY2VzIGhhdmUgYWxsIHNpbmd1bGFyIHZhbHVlcyA9IDEsIHNvIOKAlldfaF5U4oCWID0gMSBmb3IgYWxsIFQg4oCUIGdyYWRpZW50cyBuZWl0aGVyIGV4cGxvZGUgbm9yIHZhbmlzaCB0aHJvdWdoIHRoZSByZWN1cnJlbmNlLiBJbiBwcmFjdGljZSwgb3J0aG9nb25hbCBpbml0IChubi5pbml0Lm9ydGhvZ29uYWxfKSBpcyB0aGUgcmVjb21tZW5kZWQgc3RhcnRpbmcgcG9pbnQgZm9yIFJOTnMgYW5kIGlzIHVzZWQgYXMgdGhlIGRlZmF1bHQgaW4gbWFueSBMU1RNIGltcGxlbWVudGF0aW9ucy4gSXQgaXMgYWxzbyBvY2Nhc2lvbmFsbHkgdXNlZCBpbiBmZWVkZm9yd2FyZCBuZXR3b3JrcyBhdCBsYXJnZSBkZXB0aCB0byBzdGFiaWxpc2Ugc2lnbmFsIHByb3BhZ2F0aW9uIGJlZm9yZSB0cmFpbmluZyBiZWdpbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEluaXRpYWxpc2F0aW9uIENoZWNrbGlzdCJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUmVMVSBoaWRkZW4gbGF5ZXJzOiBubi5pbml0LmthaW1pbmdfbm9ybWFsXyh3LCBub25saW5lYXJpdHk9XHUwMDI3cmVsdVx1MDAyNykg4oCUIEhlIGluaXQsIGZhbl9pbiBtb2RlLiIsIkxlYWt5IFJlTFU6IG5uLmluaXQua2FpbWluZ19ub3JtYWxfKHcsIGE9MC4wMSwgbm9ubGluZWFyaXR5PVx1MDAyN2xlYWt5X3JlbHVcdTAwMjcpLiIsIlRhbmgvc2lnbW9pZDogbm4uaW5pdC54YXZpZXJfbm9ybWFsXyh3KSBvciB4YXZpZXJfdW5pZm9ybV8gd2l0aCBnYWluPW5uLmluaXQuY2FsY3VsYXRlX2dhaW4oXHUwMDI3dGFuaFx1MDAyNykuIiwiU0VMVTogbm4uaW5pdC5rYWltaW5nX25vcm1hbF8odywgbW9kZT1cdTAwMjdmYW5faW5cdTAwMjcpIHdpdGggc3RkPTEv4oiabl9pbiAoTGVDdW4pLiIsIkFsbCBiaWFzZXM6IG5uLmluaXQuemVyb3NfKGIpIOKAlCBhbHdheXMgdW5sZXNzIHlvdSBoYXZlIGEgc3BlY2lmaWMgcmVhc29uIG90aGVyd2lzZS4iLCJSTk4gcmVjdXJyZW50IHdlaWdodHM6IG5uLmluaXQub3J0aG9nb25hbF8od19oKSB0byBzdGFiaWxpc2UgZ3JhZGllbnQgbm9ybXMgb3ZlciB0aW1lLiIsIlZlcmlmeTogbW9uaXRvciBhY3RpdmF0aW9uIHZhcmlhbmNlIGFuZCBncmFkaWVudCBub3JtcyBhY3Jvc3MgbGF5ZXJzIGluIHRoZSBmaXJzdCBmZXcgYmF0Y2hlcy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Weight Initialization — Xavier/Glorot and Kaiming/He

Weight initialisation is the starting point for all training dynamics. If weights are too large, activations and gradients explode; too small, they vanish. Both pathologies prevent learning in deep networks. Variance-preserving initialisation schemes — Xavier/Glorot for tanh/sigmoid and Kaiming/He for ReLU — are derived from the requirement that the variance of activations and gradients stay approximately constant as signals propagate through depth.

## The Variance Propagation Problem

For a linear layer z = Wx (ignoring bias, pre-activation), Var(zᵢ) = nᵢₙ · Var(W) · Var(x) if weights and inputs are i.i.d. and zero-mean. To keep Var(z) = Var(x) (variance preservation), we need Var(W) = 1/nᵢₙ — the LeCun initialisation. For the backward pass: Var(∂L/∂x) = nₒᵤₜ · Var(W) · Var(∂L/∂z), requiring Var(W) = 1/nₒᵤₜ. Xavier/Glorot compromises: Var(W) = 2/(nᵢₙ + nₒᵤₜ), maintaining signal in both directions for zero-mean symmetric activations like tanh.

## Xavier/Glorot Initialisation

For tanh and sigmoid activations: W ~ U(-√(6/(nᵢₙ + nₒᵤₜ)), +√(6/(nᵢₙ + nₒᵤₜ))) or equivalently W ~ N(0, 2/(nᵢₙ + nₒᵤₜ)). Derived by Glorot & Bengio (2010) assuming linear activations (tanh ≈ linear near origin) and requiring Var(forward signal) ≈ Var(backward signal). For sigmoid, the effective gradient at zero is 0.25, so a gain of 4 is applied: std = gain × √(2/(nᵢₙ + nₒᵤₜ)).

## Kaiming/He Initialisation for ReLU

ReLU zeros out half its inputs, halving the effective variance. He et al. (2015) account for this: Var(W) = 2/nᵢₙ so that after ReLU, the variance is preserved. In normal form: W ~ N(0, √(2/nᵢₙ)). For Leaky ReLU with slope α: Var(W) = 2/((1+α²)·nᵢₙ). The PyTorch function nn.init.kaiming_normal_ accepts a nonlinearity argument and computes the correct gain automatically. fan_in mode (default) preserves forward signal; fan_out mode preserves backward signal.

```python
import numpy as np
import torch
import torch.nn as nn

def activation_variance_trace(init_std_fn, activation_fn, depth=20, width=512, m=256, seed=0):
    """Trace activation variance layer by layer with a given init and activation."""
    np.random.seed(seed)
    x = np.random.randn(m, width)
    variances = [x.var()]
    for _ in range(depth):
        n_in, n_out = width, width
        std = init_std_fn(n_in, n_out)
        W = np.random.randn(n_out, n_in) * std
        b = np.zeros(n_out)
        z = x @ W.T + b
        x = activation_fn(z)
        variances.append(x.var())
    return variances

def relu(z): return np.maximum(0, z)
def tanh_fn(z): return np.tanh(z)

xavier_std = lambda n_in, n_out: np.sqrt(2.0 / (n_in + n_out))
he_std     = lambda n_in, n_out: np.sqrt(2.0 / n_in)
lecun_std  = lambda n_in, n_out: np.sqrt(1.0 / n_in)
small_std  = lambda n_in, n_out: 0.01

print('Activation variance trace (depth=20, should stay near 1.0):')
for label, init_fn, act_fn in [
    ('Xavier+tanh', xavier_std, tanh_fn),
    ('He+ReLU',     he_std,     relu),
    ('LeCun+tanh',  lecun_std,  tanh_fn),
    ('small+ReLU',  small_std,  relu),
]:
    vars = activation_variance_trace(init_fn, act_fn)
    print(f'  {label:>14}: layer0={vars[0]:.3f}  layer5={vars[5]:.3f}  '
          f'layer10={vars[10]:.3f}  layer20={vars[-1]:.4f}')
```

## Xavier vs He — Gradient Flow Comparison

```python
import torch
import torch.nn as nn
import numpy as np

def build_deep_net(depth, width, init_name, act_name):
    layers = []
    for i in range(depth):
        lin = nn.Linear(width, width, bias=False)
        if init_name == 'xavier':
            nn.init.xavier_normal_(lin.weight)
        elif init_name == 'he':
            nn.init.kaiming_normal_(lin.weight, nonlinearity='relu')
        elif init_name == 'small':
            nn.init.normal_(lin.weight, 0, 0.01)
        layers.append(lin)
        act = nn.Tanh() if act_name == 'tanh' else nn.ReLU()
        layers.append(act)
    return nn.Sequential(*layers)

torch.manual_seed(42)
depth, width, m = 15, 128, 64

for init_name, act_name in [('xavier', 'tanh'), ('he', 'relu'),
                              ('xavier', 'relu'), ('small', 'relu')]:
    model = build_deep_net(depth, width, init_name, act_name)
    x = torch.randn(m, width)
    out = model(x)
    out.sum().backward()
    grad_norms = [mod.weight.grad.norm().item()
                  for mod in model.modules()
                  if isinstance(mod, nn.Linear) and mod.weight.grad is not None]
    vanish = grad_norms[0] < 1e-4
    explode = grad_norms[-1] > 1e3
    print(f'{init_name:>8}+{act_name:<5}: '
          f'first_grad={grad_norms[0]:.2e}  last_grad={grad_norms[-1]:.2e}  '
          f'vanishing={vanish}  exploding={explode}')
```

## PyTorch Initialisation API

```python
import torch
import torch.nn as nn
import numpy as np

def apply_init(model, init_name):
    for m in model.modules():
        if isinstance(m, nn.Linear):
            if init_name == 'xavier_uniform':
                nn.init.xavier_uniform_(m.weight, gain=nn.init.calculate_gain('tanh'))
            elif init_name == 'xavier_normal':
                nn.init.xavier_normal_(m.weight)
            elif init_name == 'kaiming_uniform':
                nn.init.kaiming_uniform_(m.weight, nonlinearity='relu')
            elif init_name == 'kaiming_normal':
                nn.init.kaiming_normal_(m.weight, nonlinearity='relu')
            elif init_name == 'orthogonal':
                nn.init.orthogonal_(m.weight)
            nn.init.zeros_(m.bias)
    return model

torch.manual_seed(0)
for init_name in ['xavier_uniform', 'xavier_normal', 'kaiming_uniform',
                   'kaiming_normal', 'orthogonal']:
    model = apply_init(nn.Sequential(
        nn.Linear(128, 256), nn.ReLU(),
        nn.Linear(256, 128), nn.ReLU(),
        nn.Linear(128, 10)
    ), init_name)
    weights = [m.weight for m in model.modules() if isinstance(m, nn.Linear)]
    stds = [w.std().item() for w in weights]
    print(f'{init_name:>18}: layer stds = {[f"{s:.4f}" for s in stds]}')
```

> **Rule of Thumb for Choosing Initialisation**: Use He/Kaiming for ReLU and Leaky ReLU — it accounts for the 50% zeroing. Use Xavier/Glorot for tanh, sigmoid, and linear activations. Use LeCun for SELU (self-normalising networks). Use Orthogonal for RNNs to preserve gradient norms across time steps. Always initialise biases to zero unless there is a specific reason otherwise.

## Gradient Norm Monitoring Across Layers

```python
import torch
import torch.nn as nn
import numpy as np

def grad_norm_per_layer(init_name, depth=12, width=128, m=64, seed=0):
    torch.manual_seed(seed)
    layers = []
    for _ in range(depth):
        lin = nn.Linear(width, width, bias=True)
        if init_name == 'he':
            nn.init.kaiming_normal_(lin.weight, nonlinearity='relu')
        elif init_name == 'xavier':
            nn.init.xavier_normal_(lin.weight)
        elif init_name == 'small':
            nn.init.normal_(lin.weight, 0, 0.01)
        nn.init.zeros_(lin.bias)
        layers.extend([lin, nn.ReLU()])
    model = nn.Sequential(*layers)
    x = torch.randn(m, width)
    out = model(x)
    out.sum().backward()
    norms = []
    for mod in model.modules():
        if isinstance(mod, nn.Linear) and mod.weight.grad is not None:
            norms.append(mod.weight.grad.norm().item())
    return norms

for init_name in ['he', 'xavier', 'small']:
    norms = grad_norm_per_layer(init_name)
    print(f'{init_name:>8}: ' + '  '.join(f'L{i+1}={n:.3f}' for i, n in enumerate(norms)))
```

## Initialisation Method Reference

| Method | Activation | Formula (std) | Variance Target | When to Use |
| --- | --- | --- | --- | --- |
| Xavier Uniform | tanh, sigmoid, linear | √(6/(n_in+n_out)) | Var(forward)≈Var(backward) | Default for tanh/sigmoid networks |
| Xavier Normal | tanh, sigmoid, linear | √(2/(n_in+n_out)) | Same as uniform (different dist) | Normal variant of Xavier — often interchangeable |
| He/Kaiming Normal | ReLU, Leaky ReLU | √(2/n_in) | Var preserved after ReLU zeroing | Default for ReLU networks — CNNs, MLPs |
| LeCun Normal | SELU | √(1/n_in) | Unit variance for self-normalising | Self-normalising networks with SELU activation |
| Orthogonal | Any (esp. RNNs) | Random orthogonal matrix | Preserves gradient norms over time | RNNs, sequence models, avoid vanishing over steps |

## Orthogonal Initialisation for Recurrent Networks

In recurrent networks, the weight matrix W_h is applied T times (once per timestep): hₜ = f(W_h hₜ₋₁ + W_x xₜ). If W_h has singular values > 1, gradients explode; < 1, they vanish. Orthogonal matrices have all singular values = 1, so ‖W_h^T‖ = 1 for all T — gradients neither explode nor vanish through the recurrence. In practice, orthogonal init (nn.init.orthogonal_) is the recommended starting point for RNNs and is used as the default in many LSTM implementations. It is also occasionally used in feedforward networks at large depth to stabilise signal propagation before training begins.

## Practical Initialisation Checklist

- ReLU hidden layers: nn.init.kaiming_normal_(w, nonlinearity='relu') — He init, fan_in mode.
- Leaky ReLU: nn.init.kaiming_normal_(w, a=0.01, nonlinearity='leaky_relu').
- Tanh/sigmoid: nn.init.xavier_normal_(w) or xavier_uniform_ with gain=nn.init.calculate_gain('tanh').
- SELU: nn.init.kaiming_normal_(w, mode='fan_in') with std=1/√n_in (LeCun).
- All biases: nn.init.zeros_(b) — always unless you have a specific reason otherwise.
- RNN recurrent weights: nn.init.orthogonal_(w_h) to stabilise gradient norms over time.
- Verify: monitor activation variance and gradient norms across layers in the first few batches.

---

