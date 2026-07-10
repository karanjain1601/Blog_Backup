---
title: "Variational Autoencoders: Continuous Latent Space and ELBO"
slug: "vae-continuous-latent"
description: ""
tags: ["vae", "generative-models", "elbo", "latent-space", "computer-vision"]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImgyIiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWYXJpYXRpb25hbCBBdXRvZW5jb2RlcnMgKFZBRXMpIGNvbWJpbmUgYSBwcm9iYWJpbGlzdGljIGVuY29kZXIgcSh6fHgpIHdpdGggYSBnZW5lcmF0aXZlIGRlY29kZXIgcCh4fHopIHRyYWluZWQgam9pbnRseSB2aWEgYSBwcmluY2lwbGVkIHZhcmlhdGlvbmFsIGxvd2VyIGJvdW5kLiBVbmxpa2UgcGxhaW4gYXV0b2VuY29kZXJzLCBWQUVzIGltcG9zZSBhIHByaW9yIHAoeikgPSBOKDAsIEkpIG9uIHRoZSBsYXRlbnQgc3BhY2UsIGZvcmNpbmcgaXQgdG8gYmUgc21vb3RoIGFuZCBjb250aW51b3Vz4oCUZW5hYmxpbmcgZ2VuZXJhdGlvbiBieSBzYW1wbGluZyB6IGRpcmVjdGx5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVkFFcyBhcmUgdGhlb3JldGljYWxseSBncm91bmRlZCBpbiB2YXJpYXRpb25hbCBpbmZlcmVuY2UgYW5kIG9mZmVyIGV4cGxpY2l0IGxpa2VsaWhvb2QgZXN0aW1hdGlvbiwgc3RhYmxlIHRyYWluaW5nLCBhbmQgbmF0dXJhbCBzdXBwb3J0IGZvciBkaXNlbnRhbmdsZW1lbnQgZXh0ZW5zaW9ucyBsaWtlIM6yLVZBRS4gVGhleSB0cmFkZSBvZmYgc2FtcGxlIHNoYXJwbmVzcyBmb3IgYSBzdHJ1Y3R1cmVkIGxhdGVudCBzcGFjZSwgbWFraW5nIHRoZW0gY29tcGxlbWVudGFyeSB0byBHQU5zIGZvciBjb250cm9sbGVkIGdlbmVyYXRpdmUgbW9kZWxpbmcuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiRUxCTyBEZXJpdmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNYXhpbWl6aW5nIGxvZyBwKHgpIGRpcmVjdGx5IGlzIGludHJhY3RhYmxlIGJlY2F1c2UgaXQgcmVxdWlyZXMgaW50ZWdyYXRpbmcgb3ZlciBhbGwgei4gSW5zdGVhZCwgd2UgbWF4aW1pemUgdGhlIEV2aWRlbmNlIExvd2VyIEJPdW5kIChFTEJPKTogbG9nIHAoeCkg4omlIEVfcVtsb2cgcCh4fHopXSAtIEtMKHEoenx4KSB8fCBwKHopKS4gVGhlIGZpcnN0IHRlcm0gaXMgcmVjb25zdHJ1Y3Rpb24gbGlrZWxpaG9vZDsgdGhlIHNlY29uZCBpcyBhIHJlZ3VsYXJpemF0aW9uIHRlcm0gcHVsbGluZyBxIHRvd2FyZCB0aGUgcHJpb3IuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgS0wgZGl2ZXJnZW5jZSBLTChOKM68LCDPg8KyKSB8fCBOKDAsIEkpKSBoYXMgYSBjbG9zZWQgZm9ybTogLTAuNSAqIM6jKDEgKyBsb2cgz4PCsiAtIM68wrIgLSDPg8KyKS4gVGhpcyBtZWFucyB3ZSBuZXZlciBuZWVkIHRvIHNhbXBsZSB0byBjb21wdXRlIHRoZSByZWd1bGFyaXphdGlvbiB0ZXJt4oCUb25seSB0aGUgcmVjb25zdHJ1Y3Rpb24gdGVybSByZXF1aXJlcyBzYW1wbGluZyB0aHJvdWdoIHRoZSByZXBhcmFtZXRlcml6YXRpb24gdHJpY2suIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiUmVwYXJhbWV0ZXJpemF0aW9uIFRyaWNrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTYW1wbGluZyB6IH4gcSh6fHgpID0gTijOvCwgz4PCsikgaXMgbm9uLWRpZmZlcmVudGlhYmxlLCBibG9ja2luZyBncmFkaWVudCBmbG93IHRvIHRoZSBlbmNvZGVyLiBUaGUgcmVwYXJhbWV0ZXJpemF0aW9uIHRyaWNrIHJld3JpdGVzIHogPSDOvCArIM61ICogz4Mgd2hlcmUgzrUgfiBOKDAsIEkpLiBOb3cgZ3JhZGllbnRzIGZsb3cgdGhyb3VnaCDOvCBhbmQgz4MgKGVuY29kZXIgb3V0cHV0cykgd2hpbGUgzrUgaXMgdHJlYXRlZCBhcyBhIGZpeGVkIHJhbmRvbSB2YXJpYWJsZSwgZW5hYmxpbmcgZW5kLXRvLWVuZCBiYWNrcHJvcGFnYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgVkFFRW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaD0zLCBsYXRlbnRfZGltPTEyOCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmNvbnYgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoLCAzMiwgNCwgMiwgMSksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZCgzMiwgNjQsIDQsIDIsIDEpLCAgIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZCg2NCwgMTI4LCA0LCAyLCAxKSwgIG5uLlJlTFUoKSxcbiAgICAgICAgKVxuICAgICAgICBzZWxmLmZjX211ICA9IG5uLkxpbmVhcigxMjggKiA0ICogNCwgbGF0ZW50X2RpbSlcbiAgICAgICAgc2VsZi5mY19sdiAgPSBubi5MaW5lYXIoMTI4ICogNCAqIDQsIGxhdGVudF9kaW0pXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGggPSBzZWxmLmNvbnYoeCkuZmxhdHRlbigxKVxuICAgICAgICBtdSwgbHYgPSBzZWxmLmZjX211KGgpLCBzZWxmLmZjX2x2KGgpXG4gICAgICAgIHogPSBtdSArIHRvcmNoLnJhbmRuX2xpa2UobXUpICogKDAuNSAqIGx2KS5leHAoKVxuICAgICAgICByZXR1cm4geiwgbXUsIGx2In0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiRGVjb2RlciBhbmQgUmVjb25zdHJ1Y3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBkZWNvZGVyIHAoeHx6KSBtYXBzIGEgbGF0ZW50IHZlY3RvciBiYWNrIHRvIHBpeGVsIHNwYWNlLiBGb3IgYmluYXJ5IG9yIG5vcm1hbGl6ZWQgaW1hZ2VzLCBhIEJlcm5vdWxsaSBkZWNvZGVyIHdpdGggYmluYXJ5IGNyb3NzLWVudHJvcHkgcmVjb25zdHJ1Y3Rpb24gbG9zcyBpcyBjb21tb24uIEZvciBjb250aW51b3VzIGltYWdlIHZhbHVlcywgYSBHYXVzc2lhbiBkZWNvZGVyIHdpdGggTVNFIGxvc3MgaXMgdXNlZC4gVGhlIGNob2ljZSBhZmZlY3RzIHRoZSB0cmFkZW9mZiBiZXR3ZWVuIHNoYXJwbmVzcyBhbmQgYmx1cnJpbmVzcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGtsX2xvc3MobXUsIGxvZ192YXIpOlxuICAgIFwiXCJcIkFuYWx5dGljYWwgS0wgZGl2ZXJnZW5jZSBmcm9tIE4obXUsIHNpZ21hXjIpIHRvIE4oMCxJKS5cIlwiXCJcbiAgICByZXR1cm4gLTAuNSAqIHRvcmNoLnN1bShcbiAgICAgICAgMSArIGxvZ192YXIgLSBtdS5wb3coMikgLSBsb2dfdmFyLmV4cCgpXG4gICAgKSAvIG11LnNpemUoMCkgICAjIG1lYW4gb3ZlciBiYXRjaCJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIHZhZV9sb3NzKHhfaGF0LCB4LCBtdSwgbG9nX3ZhciwgYmV0YT0xLjApOlxuICAgIFwiXCJcIkZ1bGwgVkFFIEVMQk8gbG9zczogcmVjb25zdHJ1Y3Rpb24gKyBiZXRhICogS0wuXG4gICAgeF9oYXQsIHg6IChCLCBDLCBILCBXKSDigJQgcHJlZGljdGVkIGFuZCB0YXJnZXQgaW1hZ2VzIGluIFswLCAxXVxuICAgIGJldGE6IDEuMCBmb3Igc3RhbmRhcmQgVkFFLCBcdTAwM2UxIGZvciBiZXRhLVZBRVxuICAgIFwiXCJcIlxuICAgIHJlY29uID0gRi5iaW5hcnlfY3Jvc3NfZW50cm9weShcbiAgICAgICAgeF9oYXQsIHgsIHJlZHVjdGlvbj1cdTAwMjdzdW1cdTAwMjdcbiAgICApIC8geC5zaXplKDApXG4gICAga2wgPSAtMC41ICogdG9yY2guc3VtKFxuICAgICAgICAxICsgbG9nX3ZhciAtIG11LnBvdygyKSAtIGxvZ192YXIuZXhwKClcbiAgICApIC8geC5zaXplKDApXG4gICAgcmV0dXJuIHJlY29uICsgYmV0YSAqIGtsLCByZWNvbiwga2wifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZBRSBkZWNvZGVycyB0ZW5kIHRvIHByb2R1Y2UgYmx1cnJ5IGltYWdlcyBiZWNhdXNlIHRoZSBHYXVzc2lhbiBvciBCZXJub3VsbGkgYXNzdW1wdGlvbnMgZW5jb3VyYWdlIGF2ZXJhZ2luZyBvdmVyIHBvc3NpYmxlIHJlY29uc3RydWN0aW9ucy4gVGhpcyBibHVycmluZXNzIGlzIHRoZSBtYWluIHF1YWxpdHkgZ2FwIHJlbGF0aXZlIHRvIEdBTnMuIEhpZXJhcmNoaWNhbCBWQUVzIChWRFZBRSwgTlZBRSkgYW5kIFZRLVZBRSBhZGRyZXNzIHRoaXMgd2l0aCBzdHJvbmdlciBkZWNvZGVycyBhbmQgZGlzY3JldGUgbGF0ZW50IHNwYWNlcyByZXNwZWN0aXZlbHkuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoizrItVkFFIGFuZCBEaXNlbnRhbmdsZW1lbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Is6yLVZBRSBtdWx0aXBsaWVzIHRoZSBLTCB0ZXJtIGJ5IM6yIFx1MDAzZSAxLCBhcHBseWluZyBzdHJvbmdlciBwcmVzc3VyZSBmb3IgdGhlIHBvc3RlcmlvciBxKHp8eCkgdG8gbWF0Y2ggdGhlIGlzb3Ryb3BpYyBHYXVzc2lhbiBwcmlvci4gVGhpcyBlbmNvdXJhZ2VzIGVhY2ggbGF0ZW50IGRpbWVuc2lvbiB0byBlbmNvZGUgZXhhY3RseSBvbmUgaW5kZXBlbmRlbnQgZ2VuZXJhdGl2ZSBmYWN0b3IgKHBvc2UsIGxpZ2h0aW5nLCBjb2xvcikgYXQgdGhlIGNvc3Qgb2YgbG93ZXIgcmVjb25zdHJ1Y3Rpb24gZmlkZWxpdHkuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJjb250ZW50IjoiVGhlIM6yIGNvZWZmaWNpZW50IGluIM6yLVZBRSB0cmFkZXMgb2ZmIHJlY29uc3RydWN0aW9uIGZpZGVsaXR5IGFnYWluc3QgbGF0ZW50IGRpc2VudGFuZ2xlbWVudC4gzrI9MSBpcyBzdGFuZGFyZCBWQUUuIM6yPTTigJMxMCBlbmNvdXJhZ2VzIGVhY2ggbGF0ZW50IGRpbWVuc2lvbiB0byBlbmNvZGUgb25lIGluZGVwZW5kZW50IGZhY3RvciDigJQgdXNlZnVsIGZvciBjb250cm9sbGFibGUgZ2VuZXJhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5AdG9yY2gubm9fZ3JhZCgpXG5kZWYgbGF0ZW50X3RyYXZlcnNhbChkZWNvZGVyLCB6X2Jhc2UsIGRpbSwgbG89LTMuMCwgaGk9My4wLCBzdGVwcz0xMCwgZGV2aWNlPVx1MDAyN2N1ZGFcdTAwMjcpOlxuICAgIFwiXCJcIlN3ZWVwIG9uZSBsYXRlbnQgZGltZW5zaW9uIHdoaWxlIGhvbGRpbmcgb3RoZXJzIGZpeGVkLlxuICAgIFJldHVybnMgYSB0ZW5zb3Igb2Ygc2hhcGUgKHN0ZXBzLCBDLCBILCBXKSBmb3IgdmlzdWFsaXphdGlvbi5cbiAgICBcIlwiXCJcbiAgICB2YWxzID0gdG9yY2gubGluc3BhY2UobG8sIGhpLCBzdGVwcywgZGV2aWNlPWRldmljZSlcbiAgICBpbWdzID0gW11cbiAgICBmb3IgdiBpbiB2YWxzOlxuICAgICAgICB6ID0gel9iYXNlLmNsb25lKCkudG8oZGV2aWNlKSAgICMgKDEsIGxhdGVudF9kaW0pXG4gICAgICAgIHpbMCwgZGltXSA9IHZcbiAgICAgICAgaW1ncy5hcHBlbmQoZGVjb2Rlcih6KSkgICAgICAgICAgIyAoMSwgQywgSCwgVylcbiAgICByZXR1cm4gdG9yY2guY2F0KGltZ3MsIGRpbT0wKSAgICAgICAgIyAoc3RlcHMsIEMsIEgsIFcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwizrIgVmFsdWUiLCJSZWNvbnN0cnVjdGlvbiBRdWFsaXR5IiwiRGlzZW50YW5nbGVtZW50IiwiRklEIl0sInJvd3MiOltbIlZBRSIsIjEiLCJIaWdoIiwiTG93IiwifjYwIl0sWyLOsi1WQUUiLCI0IiwiTWVkaXVtLUhpZ2giLCJNZWRpdW0iLCJ+NzUiXSxbIs6yLVZBRSIsIjEwIiwiTWVkaXVtIiwiSGlnaCIsIn45MCJdLFsiVlEtVkFFIiwiTi9BIiwiSGlnaCIsIk1lZGl1bSIsIn40NSJdLFsiVlEtVkFFLTIiLCJOL0EiLCJWZXJ5IEhpZ2giLCJNZWRpdW0iLCJ+MzEiXV19LHsidHlwZSI6ImgyIiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBFTEJPIHByb3ZpZGVzIGEgcHJpbmNpcGxlZCBvYmplY3RpdmUgd2l0aCB0d28gY29tcGV0aW5nIGZvcmNlczogcmVjb25zdHJ1Y3Rpb24gZmlkZWxpdHkgKGxpa2VsaWhvb2QgdGVybSkgYW5kIHJlZ3VsYXJpemF0aW9uIHRvd2FyZCB0aGUgcHJpb3IgKEtMIHRlcm0pLiBUaGUgcmVwYXJhbWV0ZXJpemF0aW9uIHRyaWNrIGlzIHRoZSBrZXkgaW5zaWdodCB0aGF0IG1ha2VzIGdyYWRpZW50LWJhc2VkIHRyYWluaW5nIHBvc3NpYmxlIGRlc3BpdGUgc3RvY2hhc3RpYyBzYW1wbGluZyBpbiB0aGUgZm9yd2FyZCBwYXNzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoizrItVkFFIGRlbW9uc3RyYXRlcyB0aGF0IHNpbXBsZSBjb2VmZmljaWVudCBzY2FsaW5nIG1lYW5pbmdmdWxseSBjaGFuZ2VzIHRoZSBpbmR1Y3RpdmUgYmlhcyBvZiB0aGUgbW9kZWwgdG93YXJkIGRpc2VudGFuZ2xlbWVudC4gV2hlbiBjb250cm9sbGFibGUgZ2VuZXJhdGlvbiBpcyB0aGUgZ29hbCAoZS5nLiwgdmFyeWluZyBvbmx5IG9uZSBhdHRyaWJ1dGUpLCBzdGFydCB3aXRoIM6yPTQgYW5kIHN3ZWVwIHVwd2FyZCwgbW9uaXRvcmluZyBib3RoIEZJRCBhbmQgYSBkaXNlbnRhbmdsZW1lbnQgbWV0cmljIGxpa2UgTUlHIG9yIERDSS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZRLVZBRSBhbmQgVlEtVkFFLTIgYnlwYXNzIHRoZSBibHVycmluZXNzIHByb2JsZW0gYnkgcXVhbnRpemluZyB0aGUgbGF0ZW50IHNwYWNlIGludG8gYSBsZWFybmVkIGRpc2NyZXRlIGNvZGVib29rLCB0aGVuIHRyYWluaW5nIGFuIGF1dG9yZWdyZXNzaXZlIHByaW9yIG92ZXIgY29kZWJvb2sgaW5kaWNlcy4gVGhpcyBjb21iaW5hdGlvbiBvZiBWQUUgY29tcHJlc3Npb24gd2l0aCBBUiBtb2RlbGluZyBwcm9kdWNlcyBzaGFycCwgaGlnaC1yZXNvbHV0aW9uIGltYWdlcyBhbmQgdW5kZXJwaW5zIG1vZGVscyBsaWtlIERBTEwtRSBhbmQgUlEtVkFFLVRyYW5zZm9ybWVyLiJ9XQ=="
---
# Variational Autoencoders: Continuous Latent Space and ELBO

Variational Autoencoders (VAEs) combine a probabilistic encoder q(z|x) with a generative decoder p(x|z) trained jointly via a principled variational lower bound. Unlike plain autoencoders, VAEs impose a prior p(z) = N(0, I) on the latent space, forcing it to be smooth and continuous—enabling generation by sampling z directly.

VAEs are theoretically grounded in variational inference and offer explicit likelihood estimation, stable training, and natural support for disentanglement extensions like β-VAE. They trade off sample sharpness for a structured latent space, making them complementary to GANs for controlled generative modeling.

Maximizing log p(x) directly is intractable because it requires integrating over all z. Instead, we maximize the Evidence Lower BOund (ELBO): log p(x) ≥ E_q[log p(x|z)] - KL(q(z|x) || p(z)). The first term is reconstruction likelihood; the second is a regularization term pulling q toward the prior.

The KL divergence KL(N(μ, σ²) || N(0, I)) has a closed form: -0.5 * Σ(1 + log σ² - μ² - σ²). This means we never need to sample to compute the regularization term—only the reconstruction term requires sampling through the reparameterization trick.

Sampling z ~ q(z|x) = N(μ, σ²) is non-differentiable, blocking gradient flow to the encoder. The reparameterization trick rewrites z = μ + ε * σ where ε ~ N(0, I). Now gradients flow through μ and σ (encoder outputs) while ε is treated as a fixed random variable, enabling end-to-end backpropagation.

```
import torch
import torch.nn as nn

class VAEEncoder(nn.Module):
    def __init__(self, in_ch=3, latent_dim=128):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch, 32, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(32, 64, 4, 2, 1),   nn.ReLU(),
            nn.Conv2d(64, 128, 4, 2, 1),  nn.ReLU(),
        )
        self.fc_mu  = nn.Linear(128 * 4 * 4, latent_dim)
        self.fc_lv  = nn.Linear(128 * 4 * 4, latent_dim)
    def forward(self, x):
        h = self.conv(x).flatten(1)
        mu, lv = self.fc_mu(h), self.fc_lv(h)
        z = mu + torch.randn_like(mu) * (0.5 * lv).exp()
        return z, mu, lv
```

The decoder p(x|z) maps a latent vector back to pixel space. For binary or normalized images, a Bernoulli decoder with binary cross-entropy reconstruction loss is common. For continuous image values, a Gaussian decoder with MSE loss is used. The choice affects the tradeoff between sharpness and blurriness.

```
import torch
import torch.nn.functional as F

def kl_loss(mu, log_var):
    """Analytical KL divergence from N(mu, sigma^2) to N(0,I)."""
    return -0.5 * torch.sum(
        1 + log_var - mu.pow(2) - log_var.exp()
    ) / mu.size(0)   # mean over batch
```

```
import torch.nn.functional as F

def vae_loss(x_hat, x, mu, log_var, beta=1.0):
    """Full VAE ELBO loss: reconstruction + beta * KL.
    x_hat, x: (B, C, H, W) — predicted and target images in [0, 1]
    beta: 1.0 for standard VAE, >1 for beta-VAE
    """
    recon = F.binary_cross_entropy(
        x_hat, x, reduction='sum'
    ) / x.size(0)
    kl = -0.5 * torch.sum(
        1 + log_var - mu.pow(2) - log_var.exp()
    ) / x.size(0)
    return recon + beta * kl, recon, kl
```

VAE decoders tend to produce blurry images because the Gaussian or Bernoulli assumptions encourage averaging over possible reconstructions. This blurriness is the main quality gap relative to GANs. Hierarchical VAEs (VDVAE, NVAE) and VQ-VAE address this with stronger decoders and discrete latent spaces respectively.

β-VAE multiplies the KL term by β > 1, applying stronger pressure for the posterior q(z|x) to match the isotropic Gaussian prior. This encourages each latent dimension to encode exactly one independent generative factor (pose, lighting, color) at the cost of lower reconstruction fidelity.

> **tip**: The β coefficient in β-VAE trades off reconstruction fidelity against latent disentanglement. β=1 is standard VAE. β=4–10 encourages each latent dimension to encode one independent factor — useful for controllable generation.

```
import torch
import numpy as np

@torch.no_grad()
def latent_traversal(decoder, z_base, dim, lo=-3.0, hi=3.0, steps=10, device='cuda'):
    """Sweep one latent dimension while holding others fixed.
    Returns a tensor of shape (steps, C, H, W) for visualization.
    """
    vals = torch.linspace(lo, hi, steps, device=device)
    imgs = []
    for v in vals:
        z = z_base.clone().to(device)   # (1, latent_dim)
        z[0, dim] = v
        imgs.append(decoder(z))          # (1, C, H, W)
    return torch.cat(imgs, dim=0)        # (steps, C, H, W)
```

| Model | β Value | Reconstruction Quality | Disentanglement | FID |
| --- | --- | --- | --- | --- |
| VAE | 1 | High | Low | ~60 |
| β-VAE | 4 | Medium-High | Medium | ~75 |
| β-VAE | 10 | Medium | High | ~90 |
| VQ-VAE | N/A | High | Medium | ~45 |
| VQ-VAE-2 | N/A | Very High | Medium | ~31 |

The ELBO provides a principled objective with two competing forces: reconstruction fidelity (likelihood term) and regularization toward the prior (KL term). The reparameterization trick is the key insight that makes gradient-based training possible despite stochastic sampling in the forward pass.

β-VAE demonstrates that simple coefficient scaling meaningfully changes the inductive bias of the model toward disentanglement. When controllable generation is the goal (e.g., varying only one attribute), start with β=4 and sweep upward, monitoring both FID and a disentanglement metric like MIG or DCI.

VQ-VAE and VQ-VAE-2 bypass the blurriness problem by quantizing the latent space into a learned discrete codebook, then training an autoregressive prior over codebook indices. This combination of VAE compression with AR modeling produces sharp, high-resolution images and underpins models like DALL-E and RQ-VAE-Transformer.

