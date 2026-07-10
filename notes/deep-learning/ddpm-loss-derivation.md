---
title: "DDPM Loss — VLB, Simplified Objective, and x₀ vs ε Prediction"
slug: "ddpm-loss-derivation"
description: "Derives the DDPM training objective from the ELBO: each KL term is a Gaussian-vs-Gaussian comparison with tractable posterior. Ho et al. simplify to predict noise epsilon. Covers x0- vs eps- vs v-prediction, SNR weighting, and min-SNR-gamma for stable training."
tags: ["deep-learning", "generative-models", "diffusion-models", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEREUE0gdHJhaW5pbmcgb2JqZWN0aXZlIGlzIGRlcml2ZWQgZnJvbSB0aGUgZXZpZGVuY2UgbG93ZXIgYm91bmQgKEVMQk8pIG9uIGxvZyBwKHhfMCkuIEJlY2F1c2UgdGhlIGZvcndhcmQgcHJvY2VzcyBpcyBhIGZpeGVkIE1hcmtvdiBjaGFpbiB3aXRoIEdhdXNzaWFuIGNvbmRpdGlvbmFscywgZXZlcnkgdGVybSBpbiB0aGUgRUxCTyByZWR1Y2VzIHRvIGEgS0wgZGl2ZXJnZW5jZSBiZXR3ZWVuIEdhdXNzaWFucywgd2hpY2ggaGFzIGEgY2xvc2VkLWZvcm0gZXhwcmVzc2lvbi4gSG8gZXQgYWwuIGZ1cnRoZXIgc2ltcGxpZnkgYnkgZHJvcHBpbmcgcmV3ZWlnaHRpbmcgYW5kIHByZWRpY3Rpbmcgbm9pc2UgzrUgaW5zdGVhZCBvZiB0aGUgbWVhbiwgYXJyaXZpbmcgYXQgYSBzdGFuZGFyZCBNU0UgbG9zcy4gVW5kZXJzdGFuZGluZyB0aGUgZnVsbCBkZXJpdmF0aW9uIGlsbHVtaW5hdGVzIHdoeSDOtS1wcmVkaWN0aW9uIHdvcmtzLCBob3cgU05SIHNoYXBlcyB0aGUgbG9zcyBsYW5kc2NhcGUsIGFuZCBob3cgbWluLVNOUiB3ZWlnaHRpbmcgaW1wcm92ZXMgdHJhaW5pbmcgc3RhYmlsaXR5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV2aWRlbmNlIExvd2VyIEJvdW5kIChWTEIpIGZvciBEaWZmdXNpb24gTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbG9nLWxpa2VsaWhvb2QgbG9nIHBfzrgoeF8wKSBpcyBpbnRyYWN0YWJsZS4gSW5zdGVhZCB3ZSBtYXhpbWl6ZSB0aGUgRUxCTzogTCA9IEVfcVtsb2cgcF/OuCh4XzB8eF8xKV0gLSBLTFtxKHhfVHx4XzApIHx8IHAoeF9UKV0gLSDOo197dD0yfV57VH0gRV9xW0tMW3EoeF97dC0xfXx4X3QsIHhfMCkgfHwgcF/OuCh4X3t0LTF9fHhfdCldXS4gVGhlIGZpcnN0IHRlcm0gaXMgdGhlIHJlY29uc3RydWN0aW9uIGxvc3MsIHRoZSBzZWNvbmQgaXMgYSBib3VuZGFyeSB0ZXJtIChmaXhlZCwgc2luY2UgcCh4X1QpID0gTigwLEkpIGFuZCBxKHhfVHx4XzApIOKJiCBOKDAsSSkgZm9yIGxhcmdlIFQpLCBhbmQgdGhlIHN1bSBvZiBLTCB0ZXJtcyBpcyB0aGUgbWFpbiB0cmFpbmluZyBzaWduYWwuIEVhY2ggS0wgaXMgYmV0d2VlbiB0d28gR2F1c3NpYW5zOiB0aGUgdHJhY3RhYmxlIHBvc3RlcmlvciBxKHhfe3QtMX18eF90LCB4XzApIGFuZCB0aGUgbGVhcm5lZCBwX864KHhfe3QtMX18eF90KS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGtsX2dhdXNzaWFuKG11MSwgbG9nX3ZhcjEsIG11MiwgbG9nX3ZhcjIpOlxuICAgIFwiXCJcIktMKE4obXUxLGV4cChsdjEpKSB8fCBOKG11MixleHAobHYyKSkpIC0tIGNsb3NlZCBmb3JtLlwiXCJcIlxuICAgIHJldHVybiAwLjUgKiAobG9nX3ZhcjIgLSBsb2dfdmFyMVxuICAgICAgICAgICAgICAgICAgKyAobG9nX3ZhcjEuZXhwKCkgKyAobXUxIC0gbXUyKSoqMikgLyBsb2dfdmFyMi5leHAoKSAtIDEpXG5cbmRlZiBxX3Bvc3Rlcmlvcih4MCwgeHQsIHQsIGFscGhhX2JhciwgYmV0YSk6XG4gICAgXCJcIlwiVHJhY3RhYmxlIHBvc3RlcmlvciBxKHhfe3QtMX18eF90LHhfMCk6IG1lYW4gYW5kIGxvZy12YXJpYW5jZS5cIlwiXCJcbiAgICBhbHBoYSAgPSAxLjAgLSBiZXRhXG4gICAgYWJfdCAgID0gYWxwaGFfYmFyW3RdXG4gICAgYWJfcCAgID0gYWxwaGFfYmFyW3QgLSAxXSBpZiB0IFx1MDAzZSAwIGVsc2UgdG9yY2gub25lc19saWtlKGFiX3QpXG4gICAgYzEgPSBhYl9wLnNxcnQoKSAqIGJldGFbdF0gLyAoMSAtIGFiX3QpXG4gICAgYzIgPSBhbHBoYVt0XS5zcXJ0KCkgKiAoMSAtIGFiX3ApIC8gKDEgLSBhYl90KVxuICAgIG11X3EgICA9IGMxICogeDAgKyBjMiAqIHh0XG4gICAgdmFyX3EgID0gYmV0YVt0XSAqICgxIC0gYWJfcCkgLyAoMSAtIGFiX3QpXG4gICAgcmV0dXJuIG11X3EsIHZhcl9xLmxvZygpXG5cbmRlZiB2bGJfdGVybShtb2RlbCwgeDAsIHQsIGFscGhhX2JhciwgYmV0YSk6XG4gICAgXCJcIlwiU2luZ2xlIFZMQiB0ZXJtIExfdCA9IEVbS0wocSh4X3t0LTF9fHhfdCx4MCkgfHwgcF90aGV0YSh4X3t0LTF9fHhfdCkpXS5cIlwiXCJcbiAgICBub2lzZSA9IHRvcmNoLnJhbmRuX2xpa2UoeDApXG4gICAgYWJfdCAgPSBhbHBoYV9iYXJbdF1cbiAgICB4dCAgICA9IGFiX3Quc3FydCgpICogeDAgKyAoMSAtIGFiX3QpLnNxcnQoKSAqIG5vaXNlXG4gICAgbXVfcSwgbHZfcSA9IHFfcG9zdGVyaW9yKHgwLCB4dCwgdCwgYWxwaGFfYmFyLCBiZXRhKVxuICAgIHRfYiAgID0gdG9yY2guZnVsbCgoeDAuc2hhcGVbMF0sKSwgdCwgZHR5cGU9dG9yY2gubG9uZylcbiAgICBlcHNfcCA9IG1vZGVsKHh0LCB0X2IpXG4gICAgeDBfcCAgPSAoeHQgLSAoMSAtIGFiX3QpLnNxcnQoKSAqIGVwc19wKSAvIGFiX3Quc3FydCgpXG4gICAgbXVfcCwgXyA9IHFfcG9zdGVyaW9yKHgwX3AuZGV0YWNoKCksIHh0LCB0LCBhbHBoYV9iYXIsIGJldGEpXG4gICAga2wgPSBrbF9nYXVzc2lhbihtdV9xLCBsdl9xLCBtdV9wLCBsdl9xKVxuICAgIHJldHVybiBrbC5tZWFuKClcblxucHJpbnQoXCJWTEIgPSBFW2xvZyBwKHgwfHgxKV0gLSBLTFtxKHhUfHgwKXx8cCh4VCldXCIpXG5wcmludChcIiAgICAtIHN1bV97dD0yfV57VH0gRVtLTFtxKHhfe3QtMX18eF90LHgwKSB8fCBwX3RoZXRhKHhfe3QtMX18eF90KV1dXCIpXG5wcmludChcIkVhY2ggS0wgaXMgR2F1c3NpYW4tdnMtR2F1c3NpYW4gLS0gY2xvc2VkIGZvcm0sIG5vIE1DIG5lZWRlZFwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWN0YWJsZSBQb3N0ZXJpb3IgcSh4X3t0LTF9IHwgeF90LCB4XzApIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb25kaXRpb25pbmcgb24geF8wIG1ha2VzIHRoZSByZXZlcnNlIHBvc3RlcmlvciB0cmFjdGFibGUuIEJ5IEJheWVzXHUwMDI3IHJ1bGUgYW5kIHRoZSBNYXJrb3YgcHJvcGVydHk6IHEoeF97dC0xfSB8IHhfdCwgeF8wKSDiiJ0gcSh4X3QgfCB4X3t0LTF9KSBxKHhfe3QtMX0gfCB4XzApLiBCb3RoIGZhY3RvcnMgYXJlIEdhdXNzaWFuLCBzbyB0aGVpciBwcm9kdWN0IGlzIGFsc28gR2F1c3NpYW4uIFRoZSByZXN1bHRpbmcgcG9zdGVyaW9yIGhhcyBtZWFuIM68zINfdCA9ICjiiJrOscyFX3t0LTF9IM6yX3QgeF8wICsg4oiazrFfdCAoMS3OscyFX3t0LTF9KSB4X3QpIC8gKDEtzrHMhV90KSBhbmQgdmFyaWFuY2UgzrLMg190ID0gzrJfdCAoMS3OscyFX3t0LTF9KSAvICgxLc6xzIVfdCkuIENydWNpYWxseSwgzrLMg190IGRlcGVuZHMgb25seSBvbiB0aGUgZml4ZWQgc2NoZWR1bGUsIG5vdCBvbiB0aGUgZGF0YS4gVGhpcyBtZWFucyB0aGUgS0wgdGVybSBzaW1wbGlmaWVzIHRvIGEgY29tcGFyaXNvbiBvZiBtZWFucyBvbmx5ICh0aGUgdmFyaWFuY2VzIG1hdGNoKSwgcmVkdWNpbmcgZWFjaCBMX3QgdG8gYSB3ZWlnaHRlZCBNU0UgYmV0d2VlbiDOvMyDX3QgYW5kIM68X864LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNpbXBsaWZpZWQgzrUtUHJlZGljdGlvbiBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXBhcmFtZXRlcml6aW5nIM68X864IGluIHRlcm1zIG9mIHRoZSBwcmVkaWN0ZWQgbm9pc2UgzrVfzrg6IM68X864KHhfdCwgdCkgPSAoeF90IC0gzrJfdCAvIOKImigxLc6xzIVfdCkgzrVfzrgoeF90LCB0KSkgLyDiiJrOsV90LiBTdWJzdGl0dXRpbmcgaW50byB0aGUgS0wsIGVhY2ggTF90IGJlY29tZXMgcHJvcG9ydGlvbmFsIHRvIHx8zrUgLSDOtV/OuCh4X3QsIHQpfHxeMiB3aXRoIGEgd2VpZ2h0IM6yX3TCsiAvICgyzrFfdCgxLc6xzIVfdCkpLiBIbyBldCBhbC4gZHJvcCB0aGlzIHBlci10aW1lc3RlcCB3ZWlnaHQgKHNldCBhbGwgd2VpZ2h0cyB0byAxKSBhbmQgZmluZCB0aGF0IHRoZSB1bndlaWdodGVkIGxvc3M6IExfe3NpbXBsZX0gPSBFX3t0LHhfMCzOtX1bfHzOtSAtIM61X864KOKIms6xzIVfdCB4XzAgKyDiiJooMS3OscyFX3QpzrUsIHQpfHxeMl0gYWNoaWV2ZXMgYmV0dGVyIHNhbXBsZSBxdWFsaXR5LiBUaGUgd2VpZ2h0IGRyb3BwaW5nIGltcGxpY2l0bHkgdXAtd2VpZ2h0cyBoaWdoLW5vaXNlIHRpbWVzdGVwcyAobGFyZ2UgdCwgc21hbGwgU05SKSByZWxhdGl2ZSB0byB0aGUgVkxCLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGRkcG1fbG9zc19zaW1wbGUobW9kZWwsIHgwLCBhbHBoYV9iYXIsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpOlxuICAgIFwiXCJcIlxuICAgIFNpbXBsaWZpZWQgRERQTSBsb3NzIChIbyBldCBhbC4gMjAyMCwgRXEuIDE0KS5cbiAgICBMX3NpbXBsZSA9IEVbfHxlcHMgLSBlcHNfdGhldGEoc3FydChhYl90KSp4MCArIHNxcnQoMS1hYl90KSplcHMsIHQpfHxeMl1cbiAgICBVbmlmb3JtIHdlaWdodGluZyBvdmVyIHQgLS0gZHJvcHMgVkxCIHdlaWdodHMsIGVtcGlyaWNhbGx5IGJldHRlci5cbiAgICBcIlwiXCJcbiAgICBCICAgPSB4MC5zaGFwZVswXVxuICAgIHQgICA9IHRvcmNoLnJhbmRpbnQoMCwgbGVuKGFscGhhX2JhciksIChCLCksIGRldmljZT1kZXZpY2UpXG4gICAgZXBzID0gdG9yY2gucmFuZG5fbGlrZSh4MClcbiAgICBhYiAgPSBhbHBoYV9iYXJbdF0udmlldygtMSwgMSwgMSwgMSlcbiAgICB4dCAgPSBhYi5zcXJ0KCkgKiB4MCArICgxIC0gYWIpLnNxcnQoKSAqIGVwc1xuICAgIGVwc19oYXQgPSBtb2RlbCh4dCwgdClcbiAgICByZXR1cm4gRi5tc2VfbG9zcyhlcHNfaGF0LCBlcHMpXG5cbmltcG9ydCB0b3JjaFxuVCAgICAgICAgID0gMTAwMFxuYmV0YSAgICAgID0gdG9yY2gubGluc3BhY2UoMWUtNCwgMC4wMiwgVClcbmFscGhhX2JhciA9IHRvcmNoLmN1bXByb2QoMSAtIGJldGEsIGRpbT0wKVxubW9kZWwgICAgID0gU2ltcGxlVU5ldCgpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MmUtNClcblxuZm9yIHN0ZXAgaW4gcmFuZ2UoMyk6XG4gICAgeDAgICA9IHRvcmNoLnJhbmRuKDQsIDMsIDMyLCAzMilcbiAgICBsb3NzID0gZGRwbV9sb3NzX3NpbXBsZShtb2RlbCwgeDAsIGFscGhhX2JhcilcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgcHJpbnQoZlwiU3RlcCB7c3RlcH06IExfc2ltcGxlPXtsb3NzLml0ZW0oKTouNGZ9XCIpXG5wcmludChcIlVuaWZvcm0gdCB3ZWlnaHRpbmc6IGltcGxpY2l0bHkgdXAtd2VpZ2h0cyBoaWdoLW5vaXNlIChsYXJnZSB0KSB0ZXJtc1wiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6InjigoAgdnMgzrUgdnMgdiBQcmVkaWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaHJlZSBwYXJhbWV0ZXJpemF0aW9ucyBhcmUgZXF1aXZhbGVudCBhdCBpbmZpbml0ZSBjYXBhY2l0eSBidXQgZGlmZmVyIGluIGJpYXMgYW5kIGdyYWRpZW50IHNjYWxpbmcgaW4gcHJhY3RpY2UuIM61LXByZWRpY3Rpb24gcHJlZGljdHMgdGhlIG5vaXNlOiB0YXJnZXQgzrUgaGFzIHVuaXQgc2NhbGUsIHN0YWJsZSBhdCBoaWdoIG5vaXNlIChsYXJnZSB0KSwgYnV0IGF0IGxvdyBub2lzZSAoc21hbGwgdCwgaGlnaCBTTlIpIHRoZSBsb3NzIGlzIGRvbWluYXRlZCBieSBmaW5lIGRldGFpbHMuIHhfMC1wcmVkaWN0aW9uIHByZWRpY3RzIHRoZSBjbGVhbiBpbWFnZSBkaXJlY3RseTogbmF0dXJhbCBhdCBsb3cgbm9pc2UsIGJ1dCBub2lzeSBhdCBoaWdoIG5vaXNlIHdoZXJlIHhfMCBpcyBiYXJlbHkgcmVjb3ZlcmFibGUuIHYtcHJlZGljdGlvbiAoU2FsaW1hbnMgXHUwMDI2IEhvLCAyMDIyKSBwcmVkaWN0cyB2ID0g4oiazrHMhV90IM61IC0g4oiaKDEtzrHMhV90KSB4XzAsIGFuIGludGVycG9sYXRpb24gdGhhdCBiYWxhbmNlcyB3ZWxsIGFjcm9zcyBhbGwgbm9pc2UgbGV2ZWxzLiBJbWFnZW4gYW5kIGxhdGVudCBkaWZmdXNpb24gbW9kZWxzIG9mdGVuIHVzZSB2LXByZWRpY3Rpb24gZm9yIGhpZ2ggcmVzb2x1dGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBsb3NzX2Vwcyhtb2RlbCwgeDAsIGFscGhhX2Jhcik6XG4gICAgXCJcIlwiZXBzLXByZWRpY3Rpb246IHByZWRpY3QgdGhlIGFkZGVkIG5vaXNlLlwiXCJcIlxuICAgIEIsIHQgID0geDAuc2hhcGVbMF0sIHRvcmNoLnJhbmRpbnQoMCwgbGVuKGFscGhhX2JhciksICh4MC5zaGFwZVswXSwpKVxuICAgIGVwcyAgID0gdG9yY2gucmFuZG5fbGlrZSh4MClcbiAgICBhYiAgICA9IGFscGhhX2Jhclt0XS52aWV3KC0xLCAxLCAxLCAxKVxuICAgIHh0ICAgID0gYWIuc3FydCgpICogeDAgKyAoMSAtIGFiKS5zcXJ0KCkgKiBlcHNcbiAgICByZXR1cm4gRi5tc2VfbG9zcyhtb2RlbCh4dCwgdCksIGVwcylcblxuZGVmIGxvc3NfeDAobW9kZWwsIHgwLCBhbHBoYV9iYXIpOlxuICAgIFwiXCJcIngwLXByZWRpY3Rpb246IHByZWRpY3QgdGhlIG9yaWdpbmFsIGNsZWFuIGltYWdlLlwiXCJcIlxuICAgIEIsIHQgID0geDAuc2hhcGVbMF0sIHRvcmNoLnJhbmRpbnQoMCwgbGVuKGFscGhhX2JhciksICh4MC5zaGFwZVswXSwpKVxuICAgIGVwcyAgID0gdG9yY2gucmFuZG5fbGlrZSh4MClcbiAgICBhYiAgICA9IGFscGhhX2Jhclt0XS52aWV3KC0xLCAxLCAxLCAxKVxuICAgIHh0ICAgID0gYWIuc3FydCgpICogeDAgKyAoMSAtIGFiKS5zcXJ0KCkgKiBlcHNcbiAgICByZXR1cm4gRi5tc2VfbG9zcyhtb2RlbCh4dCwgdCksIHgwKVxuXG5kZWYgbG9zc192KG1vZGVsLCB4MCwgYWxwaGFfYmFyKTpcbiAgICBcIlwiXCJ2LXByZWRpY3Rpb246IHYgPSBzcXJ0KGFiX3QpKmVwcyAtIHNxcnQoMS1hYl90KSp4MC5cIlwiXCJcbiAgICBCLCB0ICA9IHgwLnNoYXBlWzBdLCB0b3JjaC5yYW5kaW50KDAsIGxlbihhbHBoYV9iYXIpLCAoeDAuc2hhcGVbMF0sKSlcbiAgICBlcHMgICA9IHRvcmNoLnJhbmRuX2xpa2UoeDApXG4gICAgYWIgICAgPSBhbHBoYV9iYXJbdF0udmlldygtMSwgMSwgMSwgMSlcbiAgICB4dCAgICA9IGFiLnNxcnQoKSAqIHgwICsgKDEgLSBhYikuc3FydCgpICogZXBzXG4gICAgdl90Z3QgPSBhYi5zcXJ0KCkgKiBlcHMgLSAoMSAtIGFiKS5zcXJ0KCkgKiB4MFxuICAgIHJldHVybiBGLm1zZV9sb3NzKG1vZGVsKHh0LCB0KSwgdl90Z3QpXG5cblQgPSAxMDAwXG5iZXRhID0gdG9yY2gubGluc3BhY2UoMWUtNCwgMC4wMiwgVClcbmFscGhhX2JhciA9IHRvcmNoLmN1bXByb2QoMSAtIGJldGEsIGRpbT0wKVxubW9kZWwgPSBTaW1wbGVVTmV0KClcblxuZm9yIG5hbWUsIGZuIGluIFsoXHUwMDI3ZXBzLXByZWRcdTAwMjcsIGxvc3NfZXBzKSwgKFx1MDAyN3gwLXByZWQgXHUwMDI3LCBsb3NzX3gwKSwgKFx1MDAyN3YtcHJlZCAgXHUwMDI3LCBsb3NzX3YpXTpcbiAgICBsb3NzZXMgPSBbZm4obW9kZWwsIHRvcmNoLnJhbmRuKDQsIDMsIDMyLCAzMiksIGFscGhhX2JhcikuaXRlbSgpIGZvciBfIGluIHJhbmdlKDQpXVxuICAgIHByaW50KGZcIntuYW1lfTogbWVhbiBsb3NzID0ge3N1bShsb3NzZXMpL2xlbihsb3NzZXMpOi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaWduYWwtdG8tTm9pc2UgUmF0aW8gUGVyc3BlY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBTTlIgYXQgdGltZXN0ZXAgdCBpcyBTTlJfdCA9IM6xzIVfdCAvICgxIC0gzrHMhV90KS4gVGhlIGZ1bGwgVkxCIHdlaWdodHMgZWFjaCBMX3QgYnkgU05SX3QgLSBTTlJfe3QtMX0g4omIIOKIglNOUi/iiIJ0LiBVbmRlciDOtS1wcmVkaWN0aW9uLCBMX3tzaW1wbGV9IGltcGxpY2l0bHkgYXNzaWducyB3ZWlnaHQgMSB0byBhbGwgdGltZXN0ZXBzLCB3aGljaCBtZWFucyBoaWdoLVNOUiAobG93LW5vaXNlKSB0aW1lc3RlcHMgYXJlIHVuZGVyLXdlaWdodGVkIGNvbXBhcmVkIHRvIHRoZSBWTEIgYW5kIGxvdy1TTlIgKGhpZ2gtbm9pc2UpIHRpbWVzdGVwcyBhcmUgb3Zlci13ZWlnaHRlZC4gVW5kZXIgeF8wLXByZWRpY3Rpb24sIHRoZSBpbXBsaWNpdCB3ZWlnaHQgaXMgcHJvcG9ydGlvbmFsIHRvIFNOUl90LCBzZXZlcmVseSB1cC13ZWlnaHRpbmcgbG93LW5vaXNlIHN0ZXBzLiBUaGUgVkxCIGFuZCBzaW1wbGlmaWVkIGxvc3NlcyBoYXZlIGRpZmZlcmVudCBlbXBpcmljYWwgYmVoYXZpb3IgYmVjYXVzZSB0aGV5IHB1dCBkaWZmZXJlbnQgaW1wb3J0YW5jZSBvbiBkaWZmZXJlbnQgbm9pc2UgbGV2ZWxzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiU05SIFdlaWdodGluZyBpbiBEaWZmdXNpb24gTG9zcyIsImNvbnRlbnQiOiJWTEIgd2VpZ2h0IGZvciBMX3QgdW5kZXIgeF8wLXByZWRpY3Rpb24gaXMgcHJvcG9ydGlvbmFsIHRvIFNOUl90LCB3aGljaCBzcGFucyBtYW55IG9yZGVycyBvZiBtYWduaXR1ZGU6IFNOUiBhdCB0PTEgKG5lYXItY2xlYW4pIGNhbiBiZSB+MTAsMDAwIHdoaWxlIFNOUiBhdCB0PTk5OSAobmVhci1ub2lzZSkgaXMgfjAuMDAwMS4gVGhpcyAxMF44IGR5bmFtaWMgcmFuZ2UgbWFrZXMgdGhlIFZMQiBleHRyZW1lbHkgc2Vuc2l0aXZlIHRvIGxvdy1ub2lzZSB0ZXJtcyBhbmQgbnVtZXJpY2FsbHkgdW5zdGFibGUuIFRoZSBzaW1wbGlmaWVkIGxvc3Mgd2l0aCB1bmlmb3JtIHdlaWdodHMgYXZvaWRzIHRoaXMgYnV0IGxvc2VzIHRoZSB0aGVvcmV0aWNhbCBncm91bmRpbmcgb2YgdGhlIEVMQk8uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWluLVNOUiBXZWlnaHRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1pbi1TTlItzrMgKEhhbmcgZXQgYWwuLCAyMDIzKSBwcm9wb3NlcyBhIHByaW5jaXBsZWQgY29tcHJvbWlzZTogd2VpZ2h0IGVhY2ggTF90IGJ5IG1pbihTTlJfdCwgzrMpIC8gU05SX3QuIFRoaXMgY2FwcyB0aGUgY29udHJpYnV0aW9uIG9mIGxvdy1ub2lzZSAoaGlnaC1TTlIpIHRpbWVzdGVwcyB0byBhdCBtb3N0IM6zIHRpbWVzIHRoZSB3ZWlnaHQgb2YgaGlnaC1ub2lzZSBzdGVwcy4gV2l0aCDOsz01LCB0aGUgbG9zcyBiZWNvbWVzIG1vcmUgdW5pZm9ybSB0aGFuIHhfMC1wcmVkaWN0aW9uIHdoaWxlIHN0aWxsIHJlc3BlY3RpbmcgdGhlIFNOUiBzdHJ1Y3R1cmUuIEVtcGlyaWNhbGx5IHRoaXMgcmVkdWNlcyB0aGUgZ2FwIGJldHdlZW4gVkxCIGFuZCBzaW1wbGlmaWVkIG9iamVjdGl2ZXMgYW5kIHN0YWJpbGl6ZXMgdHJhaW5pbmcsIGVzcGVjaWFsbHkgZm9yIGxhcmdlIG1vZGVscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBjb21wdXRlX3NucihhbHBoYV9iYXIpOlxuICAgIFwiXCJcIlNOUl90ID0gYWxwaGFfYmFyX3QgLyAoMSAtIGFscGhhX2Jhcl90KS5cIlwiXCJcbiAgICByZXR1cm4gYWxwaGFfYmFyIC8gKDEuMCAtIGFscGhhX2JhcilcblxuZGVmIG1pbl9zbnJfbG9zcyhtb2RlbCwgeDAsIGFscGhhX2JhciwgZ2FtbWE9NS4wKTpcbiAgICBcIlwiXCJcbiAgICBNaW4tU05SLWdhbW1hIGxvc3MgKEhhbmcgZXQgYWwuIDIwMjMpLlxuICAgIHdlaWdodF90ID0gbWluKFNOUl90LCBnYW1tYSkgLyBTTlJfdFxuICAgIENhcHMgaW5mbHVlbmNlIG9mIGhpZ2gtU05SIChsb3ctbm9pc2UpIHRpbWVzdGVwcy5cbiAgICBcIlwiXCJcbiAgICBCICAgPSB4MC5zaGFwZVswXVxuICAgIHQgICA9IHRvcmNoLnJhbmRpbnQoMCwgbGVuKGFscGhhX2JhciksIChCLCkpXG4gICAgZXBzID0gdG9yY2gucmFuZG5fbGlrZSh4MClcbiAgICBhYiAgPSBhbHBoYV9iYXJbdF0udmlldygtMSwgMSwgMSwgMSlcbiAgICB4dCAgPSBhYi5zcXJ0KCkgKiB4MCArICgxIC0gYWIpLnNxcnQoKSAqIGVwc1xuICAgIGVwc19oYXQgPSBtb2RlbCh4dCwgdClcbiAgICBtc2UgID0gRi5tc2VfbG9zcyhlcHNfaGF0LCBlcHMsIHJlZHVjdGlvbj1cdTAwMjdub25lXHUwMDI3KS5tZWFuKGRpbT1bMSwgMiwgM10pXG4gICAgc25yICA9IGNvbXB1dGVfc25yKGFscGhhX2Jhclt0XSlcbiAgICB3ICAgID0gdG9yY2gubWluaW11bShzbnIsIHRvcmNoLmZ1bGxfbGlrZShzbnIsIGdhbW1hKSkgLyBzbnJcbiAgICByZXR1cm4gKHcgKiBtc2UpLm1lYW4oKVxuXG5UICAgID0gMTAwMFxuYmV0YSA9IHRvcmNoLmxpbnNwYWNlKDFlLTQsIDAuMDIsIFQpXG5hYiAgID0gdG9yY2guY3VtcHJvZCgxIC0gYmV0YSwgZGltPTApXG5zbnIgID0gY29tcHV0ZV9zbnIoYWIpXG5tb2RlbCA9IFNpbXBsZVVOZXQoKVxueDAgICAgPSB0b3JjaC5yYW5kbig4LCAzLCAzMiwgMzIpXG5cbmxfc2ltcGxlICA9IEYubXNlX2xvc3MobW9kZWwoYWJbNTAwXS5zcXJ0KCkqeDAsIHRvcmNoLmZ1bGwoKDgsKSw1MDAsZHR5cGU9dG9yY2gubG9uZykpLCB0b3JjaC5yYW5kbl9saWtlKHgwKSlcbmxfbWluc25yICA9IG1pbl9zbnJfbG9zcyhtb2RlbCwgeDAsIGFiLCBnYW1tYT01LjApXG5wcmludChmXCJTaW1wbGUgbG9zczogICAge2xfc2ltcGxlLml0ZW0oKTouNGZ9XCIpXG5wcmludChmXCJNaW4tU05SLTUgbG9zczoge2xfbWluc25yLml0ZW0oKTouNGZ9XCIpXG5wcmludChmXCJTTlIgcmFuZ2U6IHtzbnIubWluKCk6LjVmfSAodD17VC0xfSkgdG8ge3Nuci5tYXgoKTouMWZ9ICh0PTApXCIpXG5wcmludChcIk1pbi1TTlItNTogd2VpZ2h0cyBjYXBwZWQgYXQgZ2FtbWE9NSAtLSByZWR1Y2VzIDEwXjggZHluYW1pYyByYW5nZVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9iamVjdGl2ZSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk9iamVjdGl2ZSIsIk5ldHdvcmsgb3V0cHV0IiwiSW1wbGljaXQgd2VpZ2h0IiwiSGlnaC1ub2lzZSBiZWhhdmlvciIsIkxvdy1ub2lzZSBiZWhhdmlvciIsIlVzZWQgaW4iXSwicm93cyI6W1siRnVsbCBWTEIgKGVwcy1wcmVkKSIsIk5vaXNlIGVwcyIsIlNOUl90IC0gU05SX3t0LTF9IiwiQWNjdXJhdGUsIGhpZ2ggdmFyaWFuY2UiLCJBY2N1cmF0ZSwgaGlnaCB3ZWlnaHQiLCJERFBNIHRoZW9yZXRpY2FsIGFuYWx5c2lzIl0sWyJMX3NpbXBsZSAoZXBzLXByZWQpIiwiTm9pc2UgZXBzIiwiVW5pZm9ybSAoMSBwZXIgdCkiLCJTdGFibGUgdW5pdC1zY2FsZSB0YXJnZXRzIiwiVW5kZXItd2VpZ2h0ZWQgdnMgVkxCIiwiRERQTSwgRERQTSsrLCBtb3N0IG1vZGVscyJdLFsieDAtcHJlZGljdGlvbiIsIkNsZWFuIGltYWdlIHgwIiwiUHJvcG9ydGlvbmFsIHRvIFNOUl90IiwiTm9pc3kgLS0gbG93IFNOUiBtYWtlcyB4MCBoYXJkIiwiTmF0dXJhbCBhbmQgc3RhYmxlIiwiU29tZSBpbXByb3ZlZCBERFBNcyJdLFsidi1wcmVkaWN0aW9uIiwidiA9IHNxcnQoYWIpIGVwcyAtIHNxcnQoMS1hYikgeDAiLCJCYWxhbmNlZCBhY3Jvc3MgU05SIiwiSGFuZGxlcyB3ZWxsICh2IH4gZXBzKSIsIkhhbmRsZXMgd2VsbCAodiB+IC14MCkiLCJJbWFnZW4sIGxhdGVudCBkaWZmdXNpb24iXSxbIk1pbi1TTlItZ2FtbWEiLCJOb2lzZSBlcHMiLCJtaW4oU05SX3QsIGdhbW1hKS9TTlJfdCIsIlNpbWlsYXIgdG8gc2ltcGxlIiwiQ2FwcGVkIGNvbnRyaWJ1dGlvbiIsIlNEMywgaW1wcm92ZWQgdHJhaW5pbmciXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNob2ljZSBvZiBwcmVkaWN0aW9uIHRhcmdldCBhbmQgbG9zcyB3ZWlnaHRpbmcgc2lnbmlmaWNhbnRseSBhZmZlY3RzIHRyYWluaW5nIGR5bmFtaWNzLCBmaW5hbCBzYW1wbGUgcXVhbGl0eSwgYW5kIHRoZSBkaWZmaWN1bHR5IG9mIHRoZSBvcHRpbWl6YXRpb24gbGFuZHNjYXBlLiDOtS1wcmVkaWN0aW9uIHdpdGggTF97c2ltcGxlfSBpcyB0aGUgZG9taW5hbnQgY2hvaWNlIGZvciBpdHMgc2ltcGxpY2l0eSBhbmQgZW1waXJpY2FsIHBlcmZvcm1hbmNlLiB2LXByZWRpY3Rpb24gaXMgcHJlZmVycmVkIGZvciBoaWdoLXJlc29sdXRpb24gc3ludGhlc2lzIGFuZCBjYXNjYWRlZCBkaWZmdXNpb24gbW9kZWxzIHdoZXJlIFNOUiBzcGFucyBhIHZlcnkgd2lkZSByYW5nZS4gTWluLVNOUiB3ZWlnaHRpbmcgaXMgYSBkcm9wLWluIGltcHJvdmVtZW50IGFwcGxpY2FibGUgdG8gYW55IHByZWRpY3Rpb24gdGFyZ2V0LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVkxCOiBwcmluY2lwbGVkIEVMQk8gd2l0aCBwZXItdCB3ZWlnaHRzIC0tIHRoZW9yZXRpY2FsbHkgZ3JvdW5kZWQgYnV0IGhpZ2ggdmFyaWFuY2UgaW4gcHJhY3RpY2UuIiwiTF9zaW1wbGU6IGRyb3AgVkxCIHdlaWdodHMsIHVuaWZvcm0gd2VpZ2h0aW5nIC0tIHNpbXBsZXIgYW5kIGVtcGlyaWNhbGx5IGJldHRlciAoSG8gZXQgYWwuKS4iLCJlcHMgdnMgeDA6IG1hdGhlbWF0aWNhbGx5IGVxdWl2YWxlbnQsIGRpZmZlciBpbiBpbXBsaWNpdCBTTlIgd2VpZ2h0aW5nIGFuZCB0cmFpbmluZyBzdGFiaWxpdHkuIiwidi1wcmVkaWN0aW9uOiBpbnRlcnBvbGF0ZXMgZXBzIGFuZCB4MCwgYmFsYW5jZWQgYXQgYWxsIG5vaXNlIGxldmVscywgcHJlZmVycmVkIGZvciBoaWdoLXJlcy4iLCJNaW4tU05SLWdhbW1hOiBjYXBzIFNOUiB3ZWlnaHQgYXQgZ2FtbWEgLS0gcmVkdWNlcyAxMF44IGR5bmFtaWMgcmFuZ2UgdG8gTyhnYW1tYSkgcmFuZ2UuIiwiS2V5IGluc2lnaHQ6IHRoZSBjaG9pY2Ugb2YgcGFyYW1ldGVyaXphdGlvbiBlbmNvZGVzIGFuIGltcGxpY2l0IHByaW9yIG9uIHdoaWNoIG5vaXNlIGxldmVscyBtYXR0ZXIgbW9zdC4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# DDPM Loss — VLB, Simplified Objective, and x₀ vs ε Prediction

The DDPM training objective is derived from the evidence lower bound (ELBO) on log p(x_0). Because the forward process is a fixed Markov chain with Gaussian conditionals, every term in the ELBO reduces to a KL divergence between Gaussians, which has a closed-form expression. Ho et al. further simplify by dropping reweighting and predicting noise ε instead of the mean, arriving at a standard MSE loss. Understanding the full derivation illuminates why ε-prediction works, how SNR shapes the loss landscape, and how min-SNR weighting improves training stability.

## Evidence Lower Bound (VLB) for Diffusion Models

The log-likelihood log p_θ(x_0) is intractable. Instead we maximize the ELBO: L = E_q[log p_θ(x_0|x_1)] - KL[q(x_T|x_0) || p(x_T)] - Σ_{t=2}^{T} E_q[KL[q(x_{t-1}|x_t, x_0) || p_θ(x_{t-1}|x_t)]]. The first term is the reconstruction loss, the second is a boundary term (fixed, since p(x_T) = N(0,I) and q(x_T|x_0) ≈ N(0,I) for large T), and the sum of KL terms is the main training signal. Each KL is between two Gaussians: the tractable posterior q(x_{t-1}|x_t, x_0) and the learned p_θ(x_{t-1}|x_t).

```python
import torch
import torch.nn as nn

def kl_gaussian(mu1, log_var1, mu2, log_var2):
    """KL(N(mu1,exp(lv1)) || N(mu2,exp(lv2))) -- closed form."""
    return 0.5 * (log_var2 - log_var1
                  + (log_var1.exp() + (mu1 - mu2)**2) / log_var2.exp() - 1)

def q_posterior(x0, xt, t, alpha_bar, beta):
    """Tractable posterior q(x_{t-1}|x_t,x_0): mean and log-variance."""
    alpha  = 1.0 - beta
    ab_t   = alpha_bar[t]
    ab_p   = alpha_bar[t - 1] if t > 0 else torch.ones_like(ab_t)
    c1 = ab_p.sqrt() * beta[t] / (1 - ab_t)
    c2 = alpha[t].sqrt() * (1 - ab_p) / (1 - ab_t)
    mu_q   = c1 * x0 + c2 * xt
    var_q  = beta[t] * (1 - ab_p) / (1 - ab_t)
    return mu_q, var_q.log()

def vlb_term(model, x0, t, alpha_bar, beta):
    """Single VLB term L_t = E[KL(q(x_{t-1}|x_t,x0) || p_theta(x_{t-1}|x_t))]."""
    noise = torch.randn_like(x0)
    ab_t  = alpha_bar[t]
    xt    = ab_t.sqrt() * x0 + (1 - ab_t).sqrt() * noise
    mu_q, lv_q = q_posterior(x0, xt, t, alpha_bar, beta)
    t_b   = torch.full((x0.shape[0],), t, dtype=torch.long)
    eps_p = model(xt, t_b)
    x0_p  = (xt - (1 - ab_t).sqrt() * eps_p) / ab_t.sqrt()
    mu_p, _ = q_posterior(x0_p.detach(), xt, t, alpha_bar, beta)
    kl = kl_gaussian(mu_q, lv_q, mu_p, lv_q)
    return kl.mean()

print("VLB = E[log p(x0|x1)] - KL[q(xT|x0)||p(xT)]")
print("    - sum_{t=2}^{T} E[KL[q(x_{t-1}|x_t,x0) || p_theta(x_{t-1}|x_t)]]")
print("Each KL is Gaussian-vs-Gaussian -- closed form, no MC needed")
```

## Tractable Posterior q(x_{t-1} | x_t, x_0)

Conditioning on x_0 makes the reverse posterior tractable. By Bayes' rule and the Markov property: q(x_{t-1} | x_t, x_0) ∝ q(x_t | x_{t-1}) q(x_{t-1} | x_0). Both factors are Gaussian, so their product is also Gaussian. The resulting posterior has mean μ̃_t = (√α̅_{t-1} β_t x_0 + √α_t (1-α̅_{t-1}) x_t) / (1-α̅_t) and variance β̃_t = β_t (1-α̅_{t-1}) / (1-α̅_t). Crucially, β̃_t depends only on the fixed schedule, not on the data. This means the KL term simplifies to a comparison of means only (the variances match), reducing each L_t to a weighted MSE between μ̃_t and μ_θ.

## Simplified ε-Prediction Loss

Reparameterizing μ_θ in terms of the predicted noise ε_θ: μ_θ(x_t, t) = (x_t - β_t / √(1-α̅_t) ε_θ(x_t, t)) / √α_t. Substituting into the KL, each L_t becomes proportional to ||ε - ε_θ(x_t, t)||^2 with a weight β_t² / (2α_t(1-α̅_t)). Ho et al. drop this per-timestep weight (set all weights to 1) and find that the unweighted loss: L_{simple} = E_{t,x_0,ε}[||ε - ε_θ(√α̅_t x_0 + √(1-α̅_t)ε, t)||^2] achieves better sample quality. The weight dropping implicitly up-weights high-noise timesteps (large t, small SNR) relative to the VLB.

```python
import torch
import torch.nn.functional as F

def ddpm_loss_simple(model, x0, alpha_bar, device='cpu'):
    """
    Simplified DDPM loss (Ho et al. 2020, Eq. 14).
    L_simple = E[||eps - eps_theta(sqrt(ab_t)*x0 + sqrt(1-ab_t)*eps, t)||^2]
    Uniform weighting over t -- drops VLB weights, empirically better.
    """
    B   = x0.shape[0]
    t   = torch.randint(0, len(alpha_bar), (B,), device=device)
    eps = torch.randn_like(x0)
    ab  = alpha_bar[t].view(-1, 1, 1, 1)
    xt  = ab.sqrt() * x0 + (1 - ab).sqrt() * eps
    eps_hat = model(xt, t)
    return F.mse_loss(eps_hat, eps)

import torch
T         = 1000
beta      = torch.linspace(1e-4, 0.02, T)
alpha_bar = torch.cumprod(1 - beta, dim=0)
model     = SimpleUNet()
optimizer = torch.optim.Adam(model.parameters(), lr=2e-4)

for step in range(3):
    x0   = torch.randn(4, 3, 32, 32)
    loss = ddpm_loss_simple(model, x0, alpha_bar)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(f"Step {step}: L_simple={loss.item():.4f}")
print("Uniform t weighting: implicitly up-weights high-noise (large t) terms")
```

## x₀ vs ε vs v Prediction

Three parameterizations are equivalent at infinite capacity but differ in bias and gradient scaling in practice. ε-prediction predicts the noise: target ε has unit scale, stable at high noise (large t), but at low noise (small t, high SNR) the loss is dominated by fine details. x_0-prediction predicts the clean image directly: natural at low noise, but noisy at high noise where x_0 is barely recoverable. v-prediction (Salimans & Ho, 2022) predicts v = √α̅_t ε - √(1-α̅_t) x_0, an interpolation that balances well across all noise levels. Imagen and latent diffusion models often use v-prediction for high resolution.

```python
import torch
import torch.nn.functional as F

def loss_eps(model, x0, alpha_bar):
    """eps-prediction: predict the added noise."""
    B, t  = x0.shape[0], torch.randint(0, len(alpha_bar), (x0.shape[0],))
    eps   = torch.randn_like(x0)
    ab    = alpha_bar[t].view(-1, 1, 1, 1)
    xt    = ab.sqrt() * x0 + (1 - ab).sqrt() * eps
    return F.mse_loss(model(xt, t), eps)

def loss_x0(model, x0, alpha_bar):
    """x0-prediction: predict the original clean image."""
    B, t  = x0.shape[0], torch.randint(0, len(alpha_bar), (x0.shape[0],))
    eps   = torch.randn_like(x0)
    ab    = alpha_bar[t].view(-1, 1, 1, 1)
    xt    = ab.sqrt() * x0 + (1 - ab).sqrt() * eps
    return F.mse_loss(model(xt, t), x0)

def loss_v(model, x0, alpha_bar):
    """v-prediction: v = sqrt(ab_t)*eps - sqrt(1-ab_t)*x0."""
    B, t  = x0.shape[0], torch.randint(0, len(alpha_bar), (x0.shape[0],))
    eps   = torch.randn_like(x0)
    ab    = alpha_bar[t].view(-1, 1, 1, 1)
    xt    = ab.sqrt() * x0 + (1 - ab).sqrt() * eps
    v_tgt = ab.sqrt() * eps - (1 - ab).sqrt() * x0
    return F.mse_loss(model(xt, t), v_tgt)

T = 1000
beta = torch.linspace(1e-4, 0.02, T)
alpha_bar = torch.cumprod(1 - beta, dim=0)
model = SimpleUNet()

for name, fn in [('eps-pred', loss_eps), ('x0-pred ', loss_x0), ('v-pred  ', loss_v)]:
    losses = [fn(model, torch.randn(4, 3, 32, 32), alpha_bar).item() for _ in range(4)]
    print(f"{name}: mean loss = {sum(losses)/len(losses):.4f}")
```

## Signal-to-Noise Ratio Perspective

The SNR at timestep t is SNR_t = α̅_t / (1 - α̅_t). The full VLB weights each L_t by SNR_t - SNR_{t-1} ≈ ∂SNR/∂t. Under ε-prediction, L_{simple} implicitly assigns weight 1 to all timesteps, which means high-SNR (low-noise) timesteps are under-weighted compared to the VLB and low-SNR (high-noise) timesteps are over-weighted. Under x_0-prediction, the implicit weight is proportional to SNR_t, severely up-weighting low-noise steps. The VLB and simplified losses have different empirical behavior because they put different importance on different noise levels.

> **SNR Weighting in Diffusion Loss**: VLB weight for L_t under x_0-prediction is proportional to SNR_t, which spans many orders of magnitude: SNR at t=1 (near-clean) can be ~10,000 while SNR at t=999 (near-noise) is ~0.0001. This 10^8 dynamic range makes the VLB extremely sensitive to low-noise terms and numerically unstable. The simplified loss with uniform weights avoids this but loses the theoretical grounding of the ELBO.

## Min-SNR Weighting

Min-SNR-γ (Hang et al., 2023) proposes a principled compromise: weight each L_t by min(SNR_t, γ) / SNR_t. This caps the contribution of low-noise (high-SNR) timesteps to at most γ times the weight of high-noise steps. With γ=5, the loss becomes more uniform than x_0-prediction while still respecting the SNR structure. Empirically this reduces the gap between VLB and simplified objectives and stabilizes training, especially for large models.

```python
import torch
import torch.nn.functional as F

def compute_snr(alpha_bar):
    """SNR_t = alpha_bar_t / (1 - alpha_bar_t)."""
    return alpha_bar / (1.0 - alpha_bar)

def min_snr_loss(model, x0, alpha_bar, gamma=5.0):
    """
    Min-SNR-gamma loss (Hang et al. 2023).
    weight_t = min(SNR_t, gamma) / SNR_t
    Caps influence of high-SNR (low-noise) timesteps.
    """
    B   = x0.shape[0]
    t   = torch.randint(0, len(alpha_bar), (B,))
    eps = torch.randn_like(x0)
    ab  = alpha_bar[t].view(-1, 1, 1, 1)
    xt  = ab.sqrt() * x0 + (1 - ab).sqrt() * eps
    eps_hat = model(xt, t)
    mse  = F.mse_loss(eps_hat, eps, reduction='none').mean(dim=[1, 2, 3])
    snr  = compute_snr(alpha_bar[t])
    w    = torch.minimum(snr, torch.full_like(snr, gamma)) / snr
    return (w * mse).mean()

T    = 1000
beta = torch.linspace(1e-4, 0.02, T)
ab   = torch.cumprod(1 - beta, dim=0)
snr  = compute_snr(ab)
model = SimpleUNet()
x0    = torch.randn(8, 3, 32, 32)

l_simple  = F.mse_loss(model(ab[500].sqrt()*x0, torch.full((8,),500,dtype=torch.long)), torch.randn_like(x0))
l_minsnr  = min_snr_loss(model, x0, ab, gamma=5.0)
print(f"Simple loss:    {l_simple.item():.4f}")
print(f"Min-SNR-5 loss: {l_minsnr.item():.4f}")
print(f"SNR range: {snr.min():.5f} (t={T-1}) to {snr.max():.1f} (t=0)")
print("Min-SNR-5: weights capped at gamma=5 -- reduces 10^8 dynamic range")
```

## Objective Comparison

| Objective | Network output | Implicit weight | High-noise behavior | Low-noise behavior | Used in |
| --- | --- | --- | --- | --- | --- |
| Full VLB (eps-pred) | Noise eps | SNR_t - SNR_{t-1} | Accurate, high variance | Accurate, high weight | DDPM theoretical analysis |
| L_simple (eps-pred) | Noise eps | Uniform (1 per t) | Stable unit-scale targets | Under-weighted vs VLB | DDPM, DDPM++, most models |
| x0-prediction | Clean image x0 | Proportional to SNR_t | Noisy -- low SNR makes x0 hard | Natural and stable | Some improved DDPMs |
| v-prediction | v = sqrt(ab) eps - sqrt(1-ab) x0 | Balanced across SNR | Handles well (v ~ eps) | Handles well (v ~ -x0) | Imagen, latent diffusion |
| Min-SNR-gamma | Noise eps | min(SNR_t, gamma)/SNR_t | Similar to simple | Capped contribution | SD3, improved training |

The choice of prediction target and loss weighting significantly affects training dynamics, final sample quality, and the difficulty of the optimization landscape. ε-prediction with L_{simple} is the dominant choice for its simplicity and empirical performance. v-prediction is preferred for high-resolution synthesis and cascaded diffusion models where SNR spans a very wide range. Min-SNR weighting is a drop-in improvement applicable to any prediction target.

- VLB: principled ELBO with per-t weights -- theoretically grounded but high variance in practice.
- L_simple: drop VLB weights, uniform weighting -- simpler and empirically better (Ho et al.).
- eps vs x0: mathematically equivalent, differ in implicit SNR weighting and training stability.
- v-prediction: interpolates eps and x0, balanced at all noise levels, preferred for high-res.
- Min-SNR-gamma: caps SNR weight at gamma -- reduces 10^8 dynamic range to O(gamma) range.
- Key insight: the choice of parameterization encodes an implicit prior on which noise levels matter most.

---

