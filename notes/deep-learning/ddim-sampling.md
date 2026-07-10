---
title: "DDIM — Deterministic Sampling for Diffusion Models"
slug: "ddim-sampling"
description: "Understand why DDPM requires 1000 steps and how DDIM achieves 10-50x speedup via a non-Markovian forward process, implement the DDIM update rule, deterministic vs stochastic sampling, DDIM inversion for real image encoding, and compare sampler quality-speed tradeoffs."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRERQTSBhY2hpZXZlcyBleGNlbGxlbnQgc2FtcGxlIHF1YWxpdHkgYnV0IHJlcXVpcmVzIFQ9MTAwMCBzZXF1ZW50aWFsIGRlbm9pc2luZyBzdGVwcyDigJQgZWFjaCBhIGZ1bGwgbmV1cmFsIG5ldHdvcmsgZm9yd2FyZCBwYXNzLiBBdCA1MTLDlzUxMiByZXNvbHV0aW9uLCB0aGlzIG1ha2VzIGdlbmVyYXRpb24gdGFrZSBzZWNvbmRzIHRvIG1pbnV0ZXMuIERESU0gKFNvbmcgZXQgYWwuIDIwMjApIHNvbHZlcyB0aGlzIHdpdGhvdXQgcmV0cmFpbmluZzogaXQgcmVpbnRlcnByZXRzIHRoZSBERFBNIGZvcndhcmQgcHJvY2VzcyBhcyBub24tTWFya292aWFuLCBkZXJpdmluZyBhbiBhbHRlcm5hdGl2ZSByZXZlcnNlIHByb2Nlc3MgdGhhdCBzaGFyZXMgdGhlIHNhbWUgdHJhaW5pbmcgb2JqZWN0aXZlIGJ1dCBjYW4gc2tpcCBzdGVwcy4gVGhlIHJlc3VsdDogNTAgRERJTSBzdGVwcyByb3V0aW5lbHkgbWF0Y2ggRERQTSBhdCAxMDAwIHN0ZXBzLCBnaXZpbmcgYSAyMMOXIHNwZWVkdXAgd2l0aCB0aGUgc2FtZSB0cmFpbmVkIG1vZGVsLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkREUE0gU2FtcGxpbmcgQm90dGxlbmVjayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRERQTVx1MDAyN3MgcmV2ZXJzZSBwcm9jZXNzIGlzIE1hcmtvdmlhbjogcF/OuCh4X3t0LTF9fHhfdCkgZGVwZW5kcyBvbmx5IG9uIHhfdC4gVGhlIGZ1bGwgY2hhaW4geF9UIOKGkiB4X3tULTF9IOKGkiAuLi4g4oaSIHhfMCByZXF1aXJlcyBhbGwgVD0xMDAwIHN0ZXBzIHRvIGJlIHRyYXZlcnNlZCBzZXF1ZW50aWFsbHkg4oCUIHNraXBwaW5nIHN0ZXBzIGJyZWFrcyB0aGUgTWFya292IGFzc3VtcHRpb24gYW5kIHByb2R1Y2VzIGxvdy1xdWFsaXR5IHNhbXBsZXMuIEVhY2ggc3RlcCByZXF1aXJlcyBvbmUgbmV1cmFsIG5ldHdvcmsgZXZhbHVhdGlvbiwgc28gZ2VuZXJhdGlvbiB0aW1lIHNjYWxlcyBsaW5lYXJseSB3aXRoIFQuIE9uIGFuIEExMDAgR1BVLCBnZW5lcmF0aW5nIGEgc2luZ2xlIDUxMsOXNTEyIGltYWdlIHRha2VzIH4zMCBzZWNvbmRzIGF0IFQ9MTAwMC4gQWNjZWxlcmF0aW5nIHNhbXBsaW5nIHdpdGhvdXQgZGVncmFkaW5nIHF1YWxpdHkgaXMgb25lIG9mIHRoZSBtb3N0IHByYWN0aWNhbGx5IGltcG9ydGFudCBwcm9ibGVtcyBpbiBkaWZmdXNpb24gbW9kZWwgcmVzZWFyY2guIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRERJTSDigJQgTm9uLU1hcmtvdmlhbiBGb3J3YXJkIFByb2Nlc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRESU0gZGVmaW5lcyBhIGZhbWlseSBvZiBub24tTWFya292aWFuIGZvcndhcmQgcHJvY2Vzc2VzIHFfz4MoeF97MTpUfXx4XzApIHBhcmFtZXRlcml6ZWQgYnkgz4MsIGFsbCBzaGFyaW5nIHRoZSBzYW1lIG1hcmdpbmFscyBxKHhfdHx4XzApID0gTih4X3Q7IOKImuG+sV90wrd4XzAsICgx4oiS4b6xX3QpSSkgYXMgRERQTS4gQmVjYXVzZSB0aGUgbWFyZ2luYWxzIGFyZSBpZGVudGljYWwsIHRoZSB0cmFpbmluZyBvYmplY3RpdmUg4oCWzrVfzrgoeF90LHQpIOKIkiDOteKAlsKyIGlzIHVuY2hhbmdlZCDigJQgYW55IEREUE0tdHJhaW5lZCBtb2RlbCBjYW4gYmUgdXNlZCBkaXJlY3RseSB3aXRoIERESU0gc2FtcGxpbmcuIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IHRoZSByZXZlcnNlIHByb2Nlc3MgY2FuIGJlIGRlcml2ZWQgZm9yIGFueSBzdWItc2VxdWVuY2Ugz4QgPSB7z4RfMSwgLi4uLCDPhF9TfSDiioIgezEsIC4uLiwgVH0sIGFsbG93aW5nIFMg4omqIFQgZGVub2lzaW5nIHN0ZXBzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRESU0gVXBkYXRlIFJ1bGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBERElNIHVwZGF0ZSBmcm9tIHhfdCB0byB4X3t0LTF9IGlzOiB4X3t0LTF9ID0g4oia4b6xX3t0LTF9wrd4zIJfMCArIOKImigx4oiS4b6xX3t0LTF94oiSz4NfdMKyKcK3zrVfzrgoeF90LHQpICsgz4NfdMK3zrUsIHdoZXJlIHjMgl8wID0gKHhfdCDiiJIg4oiaKDHiiJLhvrFfdCnCt861X864KHhfdCx0KSkv4oia4b6xX3QgaXMgdGhlIHByZWRpY3RlZCBjbGVhbiBpbWFnZS4gU2V0dGluZyDPg190PTAgeWllbGRzIGEgZnVsbHkgZGV0ZXJtaW5pc3RpYyB1cGRhdGUgKERESU0gcHJvcGVyKS4gU2V0dGluZyDPg190ID0g4oiaKCgx4oiS4b6xX3t0LTF9KS8oMeKIkuG+sV90KSnCt+KImigx4oiS4b6xX3Qv4b6xX3t0LTF9KSByZWNvdmVycyBERFBNLiBUaGUgcGFyYW1ldGVyIM+DX3QgaW50ZXJwb2xhdGVzIGJldHdlZW4gZGV0ZXJtaW5pc3RpYyBhbmQgZnVsbHkgc3RvY2hhc3RpYyBzYW1wbGluZywgZ2l2aW5nIGZpbmUtZ3JhaW5lZCBjb250cm9sIG92ZXIgdGhlIHNhbXBsZSBkaXZlcnNpdHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBtYWtlX3NjaGVkdWxlKFQ9MTAwMCwgYmV0YV9zdGFydD0xZS00LCBiZXRhX2VuZD0wLjAyKTpcbiAgICBiZXRhcyA9IHRvcmNoLmxpbnNwYWNlKGJldGFfc3RhcnQsIGJldGFfZW5kLCBUKVxuICAgIGFscGhhcyA9IDEuMCAtIGJldGFzXG4gICAgYWxwaGFfYmFyID0gdG9yY2guY3VtcHJvZChhbHBoYXMsIGRpbT0wKVxuICAgIHJldHVybiBhbHBoYV9iYXJcblxuZGVmIGRkaW1fc3RlcCh4X3QsIGVwc19wcmVkLCB0LCB0X3ByZXYsIGFscGhhX2JhciwgZXRhPTAuMCk6XG4gICAgXCJcIlwiU2luZ2xlIERESU0gdXBkYXRlOiB4X3QgLVx1MDAzZSB4X3t0X3ByZXZ9LiBldGE9MDogZGV0ZXJtaW5pc3RpYy5cIlwiXCJcbiAgICBhYl90ID0gYWxwaGFfYmFyW3RdXG4gICAgYWJfcCA9IGFscGhhX2Jhclt0X3ByZXZdIGlmIHRfcHJldiBcdTAwM2U9IDAgZWxzZSB0b3JjaC5vbmVzX2xpa2UoYWJfdClcbiAgICB4MF9wcmVkID0gKHhfdCAtIHRvcmNoLnNxcnQoMSAtIGFiX3QpICogZXBzX3ByZWQpIC8gdG9yY2guc3FydChhYl90KVxuICAgIHgwX3ByZWQgPSB4MF9wcmVkLmNsYW1wKC0xLjAsIDEuMClcbiAgICBzaWdtYSA9IGV0YSAqIHRvcmNoLnNxcnQoKDEgLSBhYl9wKSAvICgxIC0gYWJfdCkgKiAoMSAtIGFiX3QgLyBhYl9wKSlcbiAgICBkaXJfeHQgPSB0b3JjaC5zcXJ0KHRvcmNoLmNsYW1wKDEgLSBhYl9wIC0gc2lnbWEqKjIsIG1pbj0wKSkgKiBlcHNfcHJlZFxuICAgIG5vaXNlID0gc2lnbWEgKiB0b3JjaC5yYW5kbl9saWtlKHhfdCkgaWYgZXRhIFx1MDAzZSAwIGVsc2UgMC4wXG4gICAgcmV0dXJuIHRvcmNoLnNxcnQoYWJfcCkgKiB4MF9wcmVkICsgZGlyX3h0ICsgbm9pc2VcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmFscGhhX2JhciA9IG1ha2Vfc2NoZWR1bGUoVD0xMDAwKVxuIyBCdWlsZCA1MC1zdGVwIHN1Yi1zZXF1ZW5jZVxuZGRpbV9zdGVwcyA9IGxpc3QocmFuZ2UoMCwgMTAwMCwgMjApKVs6Oi0xXSAgIyBbOTgwLCA5NjAsIC4uLiwgMF1cbnByaW50KGZcdTAwMjdERElNIHVzZXMge2xlbihkZGltX3N0ZXBzKX0gc3RlcHMgdnMgRERQTSAxMDAwIHN0ZXBzXHUwMDI3KVxucHJpbnQoZlx1MDAyN1N1Yi1zZXF1ZW5jZSAoZmlyc3QgNSk6IHtkZGltX3N0ZXBzWzo1XX1cdTAwMjcpXG5wcmludChmXHUwMDI3U3BlZWR1cCBmYWN0b3I6IHsxMDAwIC8vIGxlbihkZGltX3N0ZXBzKX14XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRldGVybWluaXN0aWMgdnMgU3RvY2hhc3RpYyBERElNIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgzrcgcGFyYW1ldGVyIChldGEpIGNvbnRyb2xzIHN0b2NoYXN0aWNpdHkgaW4gRERJTS4gQXQgzrc9MCwgZWFjaCBkZW5vaXNpbmcgc3RlcCBpcyBkZXRlcm1pbmlzdGljIOKAlCB0aGUgc2FtZSBpbml0aWFsIG5vaXNlIHhfVCBhbHdheXMgcHJvZHVjZXMgdGhlIHNhbWUgZmluYWwgaW1hZ2UuIFRoaXMgZGV0ZXJtaW5pc20gaXMgYSBwb3dlcmZ1bCBwcm9wZXJ0eTogaXQgZW5hYmxlcyBpbWFnZSBlZGl0aW5nIChpbnRlcnBvbGF0ZSBpbiB4X1Qgc3BhY2UpLCBhbmQgaXQgbWVhbnMgRERJTSBpcyBhbiBpbXBsaWNpdCBnZW5lcmF0aXZlIG1vZGVsIHdpdGggYSBmaXhlZCBtYXBwaW5nIGZyb20gbm9pc2UgdG8gaW1hZ2VzLiBBdCDOtz0xLCB0aGUgdmFyaWFuY2UgbWF0Y2hlcyBERFBNIGV4YWN0bHkuIEludGVybWVkaWF0ZSDOtyB2YWx1ZXMgdHJhZGUgZGl2ZXJzaXR5IGZvciBkZXRlcm1pbmlzbS4gSW4gcHJhY3RpY2UsIM63PTAgKERESU0pIGdpdmVzIHRoZSBiZXN0IEZJRCBhdCBsb3cgc3RlcCBjb3VudHM7IM63PTEgKEREUE0pIG1heSBnaXZlIHNsaWdodGx5IGJldHRlciBkaXZlcnNpdHkgYXQgaGlnaCBzdGVwIGNvdW50cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGRkaW1fc2FtcGxpbmcoZXBzX21vZGVsLCBzaGFwZSwgYWxwaGFfYmFyLCB0aW1lc3RlcHMsIGV0YT0wLjAsIHNlZWQ9MCk6XG4gICAgXCJcIlwiRnVsbCBERElNIHNhbXBsaW5nIGxvb3AuIGV0YT0wOiBkZXRlcm1pbmlzdGljLCBldGE9MTogRERQTS1saWtlLlwiXCJcIlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgeCA9IHRvcmNoLnJhbmRuKHNoYXBlKVxuICAgIGZvciBpIGluIHJhbmdlKGxlbih0aW1lc3RlcHMpIC0gMSk6XG4gICAgICAgIHQgPSB0aW1lc3RlcHNbaV1cbiAgICAgICAgdF9wcmV2ID0gdGltZXN0ZXBzW2kgKyAxXVxuICAgICAgICBhYl90ID0gYWxwaGFfYmFyW3RdXG4gICAgICAgIGFiX3AgPSBhbHBoYV9iYXJbdF9wcmV2XVxuICAgICAgICB0X2JhdGNoID0gdG9yY2guZnVsbCgoc2hhcGVbMF0sKSwgdCwgZHR5cGU9dG9yY2gubG9uZylcbiAgICAgICAgZXBzID0gZXBzX21vZGVsKHgsIHRfYmF0Y2gpXG4gICAgICAgIHgwX3ByZWQgPSAoeCAtIHRvcmNoLnNxcnQoMSAtIGFiX3QpICogZXBzKSAvIHRvcmNoLnNxcnQoYWJfdClcbiAgICAgICAgeDBfcHJlZCA9IHgwX3ByZWQuY2xhbXAoLTEsIDEpXG4gICAgICAgIHNpZ21hID0gZXRhICogdG9yY2guc3FydCgoMSAtIGFiX3ApIC8gKDEgLSBhYl90KSAqICgxIC0gYWJfdCAvIGFiX3ApKVxuICAgICAgICBkaXJfeHQgPSB0b3JjaC5zcXJ0KHRvcmNoLmNsYW1wKDEgLSBhYl9wIC0gc2lnbWEqKjIsIG1pbj0wKSkgKiBlcHNcbiAgICAgICAgbm9pc2UgPSBzaWdtYSAqIHRvcmNoLnJhbmRuX2xpa2UoeCkgaWYgZXRhIFx1MDAzZSAwIGVsc2UgMC4wXG4gICAgICAgIHggPSB0b3JjaC5zcXJ0KGFiX3ApICogeDBfcHJlZCArIGRpcl94dCArIG5vaXNlXG4gICAgcmV0dXJuIHhcblxuY2xhc3MgVG95RXBzTW9kZWwodG9yY2gubm4uTW9kdWxlKTpcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCB0KTogcmV0dXJuIHggKiAwLjEgICMgbmVhci16ZXJvIGVwcyBmb3IgZGVtb1xuXG5lcHNfbW9kZWwgPSBUb3lFcHNNb2RlbCgpXG5hbHBoYV9iYXIgPSB0b3JjaC5jdW1wcm9kKDEgLSB0b3JjaC5saW5zcGFjZSgxZS00LCAwLjAyLCAxMDAwKSwgZGltPTApXG50aW1lc3RlcHMgPSBsaXN0KHJhbmdlKDAsIDEwMDAsIDIwKSlbOjotMV1cbmZvciBldGEgaW4gWzAuMCwgMC41LCAxLjBdOlxuICAgIHgxID0gZGRpbV9zYW1wbGluZyhlcHNfbW9kZWwsICg0LCA4KSwgYWxwaGFfYmFyLCB0aW1lc3RlcHMsIGV0YT1ldGEsIHNlZWQ9NDIpXG4gICAgeDIgPSBkZGltX3NhbXBsaW5nKGVwc19tb2RlbCwgKDQsIDgpLCBhbHBoYV9iYXIsIHRpbWVzdGVwcywgZXRhPWV0YSwgc2VlZD00MilcbiAgICBzYW1lID0gdG9yY2guYWxsY2xvc2UoeDEsIHgyLCBhdG9sPTFlLTUpXG4gICAgcHJpbnQoZlx1MDAyN2V0YT17ZXRhfTogZGV0ZXJtaW5pc3RpYz17c2FtZX0sIHNhbXBsZSBub3JtPXt4MS5ub3JtKCk6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdWItU2VxdWVuY2UgU2FtcGxpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRESU0gY2FuIHVzZSBhbnkgaW5jcmVhc2luZyBzdWItc2VxdWVuY2Ugz4Qg4oqGIHsxLC4uLixUfSBvZiB0aW1lc3RlcHMsIG5vdCBuZWNlc3NhcmlseSB1bmlmb3JtbHkgc3BhY2VkLiBVbmlmb3JtIHNwYWNpbmcgKGV2ZXJ5IFQvUyBzdGVwcykgd29ya3Mgd2VsbCBmb3IgbW9zdCBjYXNlcy4gRm9yIGltYWdlcyB3aXRoIGNvbXBsZXggaGlnaC1mcmVxdWVuY3kgc3RydWN0dXJlLCBmcm9udC1sb2FkaW5nIG1vcmUgc3RlcHMgbmVhciB0PVQgKHdoZXJlIG1vc3Qgbm9pc2UgaXMgcmVtb3ZlZCkgYW5kIGZld2VyIG5lYXIgdD0wIGNhbiBnaXZlIGJldHRlciBGSUQgYXQgdGhlIHNhbWUgYnVkZ2V0LiBUaGUgRERJTSB1cGRhdGUgaXMgdmFsaWQgZm9yIGFueSBjaG9pY2Ugb2Ygz4Qg4oCUIHRoZSBtYXJnaW5hbHMg4b6xX3vPhF9pfSBhcmUgYWxsIGRlZmluZWQgYnkgdGhlIHRyYWluaW5nIHNjaGVkdWxlLCBzbyBhbnkgc3ViLXNlcXVlbmNlIGluaGVyaXRzIHRoZSBjb3JyZWN0IHN0YXRpc3RpY2FsIHByb3BlcnRpZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRERJTSBJbnZlcnNpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJlY2F1c2Ugzrc9MCBERElNIGlzIGRldGVybWluaXN0aWMsIGl0cyByZXZlcnNlIGlzIGFsc28gKGFwcHJveGltYXRlbHkpIGRldGVybWluaXN0aWMuIERESU0gaW52ZXJzaW9uIGVuY29kZXMgYSByZWFsIGltYWdlIHhfMCBpbnRvIGEgbGF0ZW50IG5vaXNlIGNvZGUgeiDiiYggeF9UIGJ5IHJ1bm5pbmcgdGhlIHByb2Nlc3MgZm9yd2FyZDogeF97dCsxfSDiiYgg4oia4b6xX3t0KzF9wrd4zIJfMCArIOKImigx4oiS4b6xX3t0KzF9KcK3zrVfzrgoeF90LHQpLiBUaGlzIGlzIG9ubHkgYXBwcm94aW1hdGUgKHRoZSBlcHNpbG9uIG5ldHdvcmsgaXMgcXVlcmllZCBvbiBub2lzeSBpbnB1dHMgeF90IHJhdGhlciB0aGFuIHhfMCksIGJ1dCBpbiBwcmFjdGljZSBnaXZlcyBuZWFyLXBlcmZlY3QgcmVjb25zdHJ1Y3Rpb24gaW4gNTAgc3RlcHMuIERESU0gaW52ZXJzaW9uIGlzIHRoZSBjb3JlIG9mIG1vc3QgZGlmZnVzaW9uLWJhc2VkIGltYWdlIGVkaXRpbmcgbWV0aG9kczogaW52ZXJ0IHRvIGdldCB6LCBtYW5pcHVsYXRlIGluIHRoZSBub2lzZSBzcGFjZSBvciB2aWEgYXR0ZW50aW9uLCB0aGVuIHJlZ2VuZXJhdGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbkB0b3JjaC5ub19ncmFkKClcbmRlZiBkZGltX2ludmVyc2lvbihlcHNfbW9kZWwsIHgwLCBhbHBoYV9iYXIsIHRpbWVzdGVwcyk6XG4gICAgXCJcIlwiRW5jb2RlIHJlYWwgaW1hZ2UgeDAgdG8gYXBwcm94aW1hdGUgbm9pc2UgdmlhIHJldmVyc2UgRERJTS5cIlwiXCJcbiAgICAjIHRpbWVzdGVwcyBzaG91bGQgYmUgYXNjZW5kaW5nIGZvciBpbnZlcnNpb24gKHQ9MCAtXHUwMDNlIHQ9VClcbiAgICBmd2Rfc3RlcHMgPSBsaXN0KHJldmVyc2VkKHRpbWVzdGVwcykpICAjIFswLCAyMCwgNDAsIC4uLiwgOTgwXVxuICAgIHggPSB4MC5jbG9uZSgpXG4gICAgZm9yIGkgaW4gcmFuZ2UobGVuKGZ3ZF9zdGVwcykgLSAxKTpcbiAgICAgICAgdCA9IGZ3ZF9zdGVwc1tpXVxuICAgICAgICB0X25leHQgPSBmd2Rfc3RlcHNbaSArIDFdXG4gICAgICAgIGFiX3QgPSBhbHBoYV9iYXJbdF1cbiAgICAgICAgYWJfbmV4dCA9IGFscGhhX2Jhclt0X25leHRdXG4gICAgICAgIHRfYmF0Y2ggPSB0b3JjaC5mdWxsKCh4LnNoYXBlWzBdLCksIHQsIGR0eXBlPXRvcmNoLmxvbmcpXG4gICAgICAgIGVwcyA9IGVwc19tb2RlbCh4LCB0X2JhdGNoKVxuICAgICAgICAjIFByZWRpY3QgeDAsIHRoZW4gc3RlcCBmb3J3YXJkXG4gICAgICAgIHgwX3ByZWQgPSAoeCAtIHRvcmNoLnNxcnQoMSAtIGFiX3QpICogZXBzKSAvIHRvcmNoLnNxcnQoYWJfdClcbiAgICAgICAgeDBfcHJlZCA9IHgwX3ByZWQuY2xhbXAoLTEsIDEpXG4gICAgICAgIHggPSB0b3JjaC5zcXJ0KGFiX25leHQpICogeDBfcHJlZCArIHRvcmNoLnNxcnQoMSAtIGFiX25leHQpICogZXBzXG4gICAgcmV0dXJuIHggICMgYXBwcm94aW1hdGUgeF9UIChzaG91bGQgYmUgfk4oMCxJKSlcblxuYWxwaGFfYmFyID0gdG9yY2guY3VtcHJvZCgxIC0gdG9yY2gubGluc3BhY2UoMWUtNCwgMC4wMiwgMTAwMCksIGRpbT0wKVxudGltZXN0ZXBzID0gbGlzdChyYW5nZSgwLCAxMDAwLCAyMCkpWzo6LTFdXG5jbGFzcyBaZXJvRXBzKHRvcmNoLm5uLk1vZHVsZSk6XG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgdCk6IHJldHVybiB0b3JjaC56ZXJvc19saWtlKHgpXG54X3JlYWwgPSB0b3JjaC5yYW5kbigyLCA0KSAqIDAuMiAgIyBzaW11bGF0ZWQgaW1hZ2UgZmVhdHVyZXNcbnogPSBkZGltX2ludmVyc2lvbihaZXJvRXBzKCksIHhfcmVhbCwgYWxwaGFfYmFyLCB0aW1lc3RlcHMpXG5wcmludChmXHUwMDI3SW5wdXQgbm9ybToge3hfcmVhbC5ub3JtKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdJbnZlcnRlZCB6IG5vcm06IHt6Lm5vcm0oKTouNGZ9ICAoY2xvc2UgdG8gaW5wdXQgc2luY2UgZXBzfj0wKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpbmcgU2FtcGxlcnMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdGltZVxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBtZWFzdXJlX3NhbXBsaW5nX3RpbWUobl9zdGVwcywgRD02NCwgQj00LCBuX3RyaWFscz0zKTpcbiAgICBcIlwiXCJNZWFzdXJlIHdhbGwtY2xvY2sgdGltZSBmb3IgYSBnaXZlbiBudW1iZXIgb2YgZGVub2lzaW5nIHN0ZXBzLlwiXCJcIlxuICAgIGFscGhhX2JhciA9IHRvcmNoLmN1bXByb2QoMSAtIHRvcmNoLmxpbnNwYWNlKDFlLTQsIDAuMDIsIDEwMDApLCBkaW09MClcbiAgICB0aW1lc3RlcHMgPSBsaXN0KHJhbmdlKDAsIDEwMDAsIDEwMDAgLy8gbl9zdGVwcykpWzo6LTFdWzpuX3N0ZXBzXVxuXG4gICAgY2xhc3MgRXBzTmV0KHRvcmNoLm5uLk1vZHVsZSk6XG4gICAgICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICAgICAgc2VsZi5mYyA9IHRvcmNoLm5uLkxpbmVhcihELCBEKVxuICAgICAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCB0KTogcmV0dXJuIHNlbGYuZmMoeClcblxuICAgIG1vZGVsID0gRXBzTmV0KClcbiAgICB0aW1lcyA9IFtdXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl90cmlhbHMpOlxuICAgICAgICB0b3JjaC5tYW51YWxfc2VlZCgwKVxuICAgICAgICB4ID0gdG9yY2gucmFuZG4oQiwgRClcbiAgICAgICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKHRpbWVzdGVwcykgLSAxKTpcbiAgICAgICAgICAgICAgICB0LCB0X3AgPSB0aW1lc3RlcHNbaV0sIHRpbWVzdGVwc1tpKzFdXG4gICAgICAgICAgICAgICAgZXBzID0gbW9kZWwoeCwgdG9yY2guZnVsbCgoQiwpLCB0LCBkdHlwZT10b3JjaC5sb25nKSlcbiAgICAgICAgICAgICAgICBhYiA9IGFscGhhX2Jhclt0XTsgYWJfcCA9IGFscGhhX2Jhclt0X3BdXG4gICAgICAgICAgICAgICAgeDAgPSAoeCAtIHRvcmNoLnNxcnQoMS1hYikqZXBzKSAvIHRvcmNoLnNxcnQoYWIpXG4gICAgICAgICAgICAgICAgeCA9IHRvcmNoLnNxcnQoYWJfcCkqeDAgKyB0b3JjaC5zcXJ0KDEtYWJfcCkqZXBzXG4gICAgICAgIHRpbWVzLmFwcGVuZCh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApXG4gICAgcmV0dXJuIGZsb2F0KG5wLm1lYW4odGltZXMpKVxuXG5mb3Igbl9zdGVwcyBpbiBbMTAwMCwgMTAwLCA1MCwgMjBdOlxuICAgIHQgPSBtZWFzdXJlX3NhbXBsaW5nX3RpbWUobl9zdGVwcylcbiAgICBwcmludChmXHUwMDI3e25fc3RlcHM6NGR9IHN0ZXBzOiB7dCoxMDAwOi4xZn0gbXMgIChyZWxhdGl2ZToge3QvbWVhc3VyZV9zYW1wbGluZ190aW1lKDEwMDApKjEwMDouMWZ9JSlcdTAwMjcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlNhbXBsZXIiLCJTdGVwcyBuZWVkZWQiLCJEZXRlcm1pbmlzdGljIiwiSW52ZXJzaW9uIiwiRklEIGF0IE4gc3RlcHMiLCJLZXkgbGltaXRhdGlvbiJdLCJyb3dzIjpbWyJERFBNIChIbyBldCBhbC4gMjAyMCkiLCIxMDAwIChNYXJrb3ZpYW4gY2hhaW4pIiwiTm8g4oCUIHN0b2NoYXN0aWMgZWFjaCBzdGVwIiwiTm8iLCJ+My4yIGF0IDEwMDAgc3RlcHMiLCJWZXJ5IHNsb3c7IGNhbm5vdCBza2lwIHN0ZXBzIl0sWyJERElNIChTb25nIGV0IGFsLiAyMDIwKSIsIjUw4oCTMTAwIChhbnkgc3ViLXNlcSkiLCJZZXMgKM63PTApIiwiWWVzIOKAlCBuZWFyIGV4YWN0IiwifjQuMCBhdCA1MCBzdGVwcyIsIlNsaWdodGx5IGJsdXJyeSBhdCB2ZXJ5IGxvdyBzdGVwcyJdLFsiRFBNLVNvbHZlciAoTHUgZXQgYWwuIDIwMjIpIiwiMTDigJMyMCAoT0RFIHNvbHZlcikiLCJZZXMiLCJBcHByb3hpbWF0ZSIsIn4zLjUgYXQgMjAgc3RlcHMiLCJDb21wbGV4IGltcGxlbWVudGF0aW9uIl0sWyJQTkRNIChMaXUgZXQgYWwuIDIwMjIpIiwiNTAgKHBzZXVkby1saW5lYXIpIiwiWWVzIiwiTm8iLCJ+My4zIGF0IDUwIHN0ZXBzIiwiUmVxdWlyZXMgNCBwcmlvciBzdGVwcyB0byB3YXJtIHVwIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBtb3N0IHByb2R1Y3Rpb24gZGVwbG95bWVudHMsIERESU0gYXQgNTAgc3RlcHMgcHJvdmlkZXMgdGhlIGJlc3QgYmFsYW5jZSBvZiBzcGVlZCBhbmQgcXVhbGl0eS4gRFBNLVNvbHZlciBpcyBwcmVmZXJyZWQgd2hlbiBzdGVwIGNvdW50IG11c3QgZ28gYmVsb3cgMjAuIERESU0gaW52ZXJzaW9uIGlzIGVzc2VudGlhbCBmb3IgZWRpdGluZyB3b3JrZmxvd3MuIFRoZSBrZXkgdGFrZWF3YXkgaXMgdGhhdCBhbGwgdGhlc2Ugc2FtcGxlcnMgdXNlIHRoZSBzYW1lIHRyYWluZWQgZXBzaWxvbiBuZXR3b3JrIOKAlCBvbmx5IHRoZSB1cGRhdGUgcnVsZSBhbmQgc3RlcCBzY2hlZHVsZSBkaWZmZXIuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkRESU0gSW52ZXJzaW9uIGZvciBJbWFnZSBFZGl0aW5nIiwiY29udGVudCI6IlRvIGVkaXQgYSByZWFsIGltYWdlIHdpdGggYSBkaWZmdXNpb24gbW9kZWw6ICgxKSBJbnZlcnQgdGhlIGltYWdlIHdpdGggRERJTSBpbnZlcnNpb24gKDUwIHN0ZXBzLCDOtz0wKSB0byBvYnRhaW4gYSBub2lzZSBjb2RlIHouICgyKSBNb2RpZnkgdGhlIGdlbmVyYXRpb24gcHJvY2VzcyDigJQgc3dhcCB0ZXh0IHByb21wdHMsIGFkanVzdCBhdHRlbnRpb24gbWFwcywgb3IgYmxlbmQgbm9pc2UgY29kZXMuICgzKSBSZWdlbmVyYXRlIHdpdGggRERJTSBzYW1wbGluZyBmcm9tIHouIFRoZSBuZWFyLWRldGVybWluaXNtIG9mIERESU0gaW52ZXJzaW9uIGVuc3VyZXMgdGhlIHJlY29uc3RydWN0aW9uIGlzIGZhaXRoZnVsIGFuZCB0aGUgZWRpdCBpcyBsb2NhbGl6ZWQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJERElNIHNoYXJlcyB0aGUgRERQTSB0cmFpbmluZyBvYmplY3RpdmUg4oCUIGFueSBERFBNLXRyYWluZWQgbW9kZWwgd29ya3MgYXMgYSBERElNIHNhbXBsZXIgd2l0aCBubyByZXRyYWluaW5nLiIsIlRoZSBERElNIHVwZGF0ZSByZWZvcm11bGF0ZXMgZGVub2lzaW5nIGFzOiBwcmVkaWN0IHhfMCBmcm9tIHhfdCwgdGhlbiByZS1ub2lzZSB0byB4X3t0X3ByZXZ9LiIsIs63PTA6IGZ1bGx5IGRldGVybWluaXN0aWM7IM63PTE6IEREUE0tZXF1aXZhbGVudCBzdG9jaGFzdGljOyDOt+KIiCgwLDEpOiBpbnRlcnBvbGF0ZWQuIiwiU3ViLXNlcXVlbmNlIM+EIGNhbiBiZSBhbnkgaW5jcmVhc2luZyBzdWJzZXQgb2YgezEsLi4uLFR9IOKAlCB1bmlmb3JtIHNwYWNpbmcgd29ya3Mgd2VsbCBpbiBwcmFjdGljZS4iLCJERElNIGludmVyc2lvbiBlbmFibGVzIHJlYWwgaW1hZ2UgZW5jb2Rpbmc6IGludmVydCB4XzAg4oaSIHpfVCwgZWRpdCwgcmVnZW5lcmF0ZSDigJQgdGhlIGJhc2lzIG9mIG1vc3QgZWRpdGluZyBtZXRob2RzLiIsIkRQTS1Tb2x2ZXIgYW5kIFBORE0gaW1wcm92ZSBvbiBERElNIHVzaW5nIGhpZ2hlci1vcmRlciBPREUgc29sdmVycywgYWNoaWV2aW5nIHF1YWxpdHkgYXQgMTDigJMyMCBzdGVwcy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# DDIM — Deterministic Sampling for Diffusion Models

DDPM achieves excellent sample quality but requires T=1000 sequential denoising steps — each a full neural network forward pass. At 512×512 resolution, this makes generation take seconds to minutes. DDIM (Song et al. 2020) solves this without retraining: it reinterprets the DDPM forward process as non-Markovian, deriving an alternative reverse process that shares the same training objective but can skip steps. The result: 50 DDIM steps routinely match DDPM at 1000 steps, giving a 20× speedup with the same trained model.

## DDPM Sampling Bottleneck

DDPM's reverse process is Markovian: p_θ(x_{t-1}|x_t) depends only on x_t. The full chain x_T → x_{T-1} → ... → x_0 requires all T=1000 steps to be traversed sequentially — skipping steps breaks the Markov assumption and produces low-quality samples. Each step requires one neural network evaluation, so generation time scales linearly with T. On an A100 GPU, generating a single 512×512 image takes ~30 seconds at T=1000. Accelerating sampling without degrading quality is one of the most practically important problems in diffusion model research.

## DDIM — Non-Markovian Forward Process

DDIM defines a family of non-Markovian forward processes q_σ(x_{1:T}|x_0) parameterized by σ, all sharing the same marginals q(x_t|x_0) = N(x_t; √ᾱ_t·x_0, (1−ᾱ_t)I) as DDPM. Because the marginals are identical, the training objective ‖ε_θ(x_t,t) − ε‖² is unchanged — any DDPM-trained model can be used directly with DDIM sampling. The key insight is that the reverse process can be derived for any sub-sequence τ = {τ_1, ..., τ_S} ⊂ {1, ..., T}, allowing S ≪ T denoising steps.

## DDIM Update Rule

The DDIM update from x_t to x_{t-1} is: x_{t-1} = √ᾱ_{t-1}·x̂_0 + √(1−ᾱ_{t-1}−σ_t²)·ε_θ(x_t,t) + σ_t·ε, where x̂_0 = (x_t − √(1−ᾱ_t)·ε_θ(x_t,t))/√ᾱ_t is the predicted clean image. Setting σ_t=0 yields a fully deterministic update (DDIM proper). Setting σ_t = √((1−ᾱ_{t-1})/(1−ᾱ_t))·√(1−ᾱ_t/ᾱ_{t-1}) recovers DDPM. The parameter σ_t interpolates between deterministic and fully stochastic sampling, giving fine-grained control over the sample diversity.

```python
import torch
import numpy as np

def make_schedule(T=1000, beta_start=1e-4, beta_end=0.02):
    betas = torch.linspace(beta_start, beta_end, T)
    alphas = 1.0 - betas
    alpha_bar = torch.cumprod(alphas, dim=0)
    return alpha_bar

def ddim_step(x_t, eps_pred, t, t_prev, alpha_bar, eta=0.0):
    """Single DDIM update: x_t -> x_{t_prev}. eta=0: deterministic."""
    ab_t = alpha_bar[t]
    ab_p = alpha_bar[t_prev] if t_prev >= 0 else torch.ones_like(ab_t)
    x0_pred = (x_t - torch.sqrt(1 - ab_t) * eps_pred) / torch.sqrt(ab_t)
    x0_pred = x0_pred.clamp(-1.0, 1.0)
    sigma = eta * torch.sqrt((1 - ab_p) / (1 - ab_t) * (1 - ab_t / ab_p))
    dir_xt = torch.sqrt(torch.clamp(1 - ab_p - sigma**2, min=0)) * eps_pred
    noise = sigma * torch.randn_like(x_t) if eta > 0 else 0.0
    return torch.sqrt(ab_p) * x0_pred + dir_xt + noise

torch.manual_seed(0)
alpha_bar = make_schedule(T=1000)
# Build 50-step sub-sequence
ddim_steps = list(range(0, 1000, 20))[::-1]  # [980, 960, ..., 0]
print(f'DDIM uses {len(ddim_steps)} steps vs DDPM 1000 steps')
print(f'Sub-sequence (first 5): {ddim_steps[:5]}')
print(f'Speedup factor: {1000 // len(ddim_steps)}x')
```

## Deterministic vs Stochastic DDIM

The η parameter (eta) controls stochasticity in DDIM. At η=0, each denoising step is deterministic — the same initial noise x_T always produces the same final image. This determinism is a powerful property: it enables image editing (interpolate in x_T space), and it means DDIM is an implicit generative model with a fixed mapping from noise to images. At η=1, the variance matches DDPM exactly. Intermediate η values trade diversity for determinism. In practice, η=0 (DDIM) gives the best FID at low step counts; η=1 (DDPM) may give slightly better diversity at high step counts.

```python
import torch
import numpy as np

def ddim_sampling(eps_model, shape, alpha_bar, timesteps, eta=0.0, seed=0):
    """Full DDIM sampling loop. eta=0: deterministic, eta=1: DDPM-like."""
    torch.manual_seed(seed)
    x = torch.randn(shape)
    for i in range(len(timesteps) - 1):
        t = timesteps[i]
        t_prev = timesteps[i + 1]
        ab_t = alpha_bar[t]
        ab_p = alpha_bar[t_prev]
        t_batch = torch.full((shape[0],), t, dtype=torch.long)
        eps = eps_model(x, t_batch)
        x0_pred = (x - torch.sqrt(1 - ab_t) * eps) / torch.sqrt(ab_t)
        x0_pred = x0_pred.clamp(-1, 1)
        sigma = eta * torch.sqrt((1 - ab_p) / (1 - ab_t) * (1 - ab_t / ab_p))
        dir_xt = torch.sqrt(torch.clamp(1 - ab_p - sigma**2, min=0)) * eps
        noise = sigma * torch.randn_like(x) if eta > 0 else 0.0
        x = torch.sqrt(ab_p) * x0_pred + dir_xt + noise
    return x

class ToyEpsModel(torch.nn.Module):
    def forward(self, x, t): return x * 0.1  # near-zero eps for demo

eps_model = ToyEpsModel()
alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
timesteps = list(range(0, 1000, 20))[::-1]
for eta in [0.0, 0.5, 1.0]:
    x1 = ddim_sampling(eps_model, (4, 8), alpha_bar, timesteps, eta=eta, seed=42)
    x2 = ddim_sampling(eps_model, (4, 8), alpha_bar, timesteps, eta=eta, seed=42)
    same = torch.allclose(x1, x2, atol=1e-5)
    print(f'eta={eta}: deterministic={same}, sample norm={x1.norm():.3f}')
```

## Sub-Sequence Sampling

DDIM can use any increasing sub-sequence τ ⊆ {1,...,T} of timesteps, not necessarily uniformly spaced. Uniform spacing (every T/S steps) works well for most cases. For images with complex high-frequency structure, front-loading more steps near t=T (where most noise is removed) and fewer near t=0 can give better FID at the same budget. The DDIM update is valid for any choice of τ — the marginals ᾱ_{τ_i} are all defined by the training schedule, so any sub-sequence inherits the correct statistical properties.

## DDIM Inversion

Because η=0 DDIM is deterministic, its reverse is also (approximately) deterministic. DDIM inversion encodes a real image x_0 into a latent noise code z ≈ x_T by running the process forward: x_{t+1} ≈ √ᾱ_{t+1}·x̂_0 + √(1−ᾱ_{t+1})·ε_θ(x_t,t). This is only approximate (the epsilon network is queried on noisy inputs x_t rather than x_0), but in practice gives near-perfect reconstruction in 50 steps. DDIM inversion is the core of most diffusion-based image editing methods: invert to get z, manipulate in the noise space or via attention, then regenerate.

```python
import torch
import numpy as np

@torch.no_grad()
def ddim_inversion(eps_model, x0, alpha_bar, timesteps):
    """Encode real image x0 to approximate noise via reverse DDIM."""
    # timesteps should be ascending for inversion (t=0 -> t=T)
    fwd_steps = list(reversed(timesteps))  # [0, 20, 40, ..., 980]
    x = x0.clone()
    for i in range(len(fwd_steps) - 1):
        t = fwd_steps[i]
        t_next = fwd_steps[i + 1]
        ab_t = alpha_bar[t]
        ab_next = alpha_bar[t_next]
        t_batch = torch.full((x.shape[0],), t, dtype=torch.long)
        eps = eps_model(x, t_batch)
        # Predict x0, then step forward
        x0_pred = (x - torch.sqrt(1 - ab_t) * eps) / torch.sqrt(ab_t)
        x0_pred = x0_pred.clamp(-1, 1)
        x = torch.sqrt(ab_next) * x0_pred + torch.sqrt(1 - ab_next) * eps
    return x  # approximate x_T (should be ~N(0,I))

alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
timesteps = list(range(0, 1000, 20))[::-1]
class ZeroEps(torch.nn.Module):
    def forward(self, x, t): return torch.zeros_like(x)
x_real = torch.randn(2, 4) * 0.2  # simulated image features
z = ddim_inversion(ZeroEps(), x_real, alpha_bar, timesteps)
print(f'Input norm: {x_real.norm():.4f}')
print(f'Inverted z norm: {z.norm():.4f}  (close to input since eps~=0)')
```

## Comparing Samplers

```python
import torch
import time
import numpy as np

def measure_sampling_time(n_steps, D=64, B=4, n_trials=3):
    """Measure wall-clock time for a given number of denoising steps."""
    alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
    timesteps = list(range(0, 1000, 1000 // n_steps))[::-1][:n_steps]

    class EpsNet(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.fc = torch.nn.Linear(D, D)
        def forward(self, x, t): return self.fc(x)

    model = EpsNet()
    times = []
    for _ in range(n_trials):
        torch.manual_seed(0)
        x = torch.randn(B, D)
        t0 = time.perf_counter()
        with torch.no_grad():
            for i in range(len(timesteps) - 1):
                t, t_p = timesteps[i], timesteps[i+1]
                eps = model(x, torch.full((B,), t, dtype=torch.long))
                ab = alpha_bar[t]; ab_p = alpha_bar[t_p]
                x0 = (x - torch.sqrt(1-ab)*eps) / torch.sqrt(ab)
                x = torch.sqrt(ab_p)*x0 + torch.sqrt(1-ab_p)*eps
        times.append(time.perf_counter() - t0)
    return float(np.mean(times))

for n_steps in [1000, 100, 50, 20]:
    t = measure_sampling_time(n_steps)
    print(f'{n_steps:4d} steps: {t*1000:.1f} ms  (relative: {t/measure_sampling_time(1000)*100:.1f}%)')
```

| Sampler | Steps needed | Deterministic | Inversion | FID at N steps | Key limitation |
| --- | --- | --- | --- | --- | --- |
| DDPM (Ho et al. 2020) | 1000 (Markovian chain) | No — stochastic each step | No | ~3.2 at 1000 steps | Very slow; cannot skip steps |
| DDIM (Song et al. 2020) | 50–100 (any sub-seq) | Yes (η=0) | Yes — near exact | ~4.0 at 50 steps | Slightly blurry at very low steps |
| DPM-Solver (Lu et al. 2022) | 10–20 (ODE solver) | Yes | Approximate | ~3.5 at 20 steps | Complex implementation |
| PNDM (Liu et al. 2022) | 50 (pseudo-linear) | Yes | No | ~3.3 at 50 steps | Requires 4 prior steps to warm up |

For most production deployments, DDIM at 50 steps provides the best balance of speed and quality. DPM-Solver is preferred when step count must go below 20. DDIM inversion is essential for editing workflows. The key takeaway is that all these samplers use the same trained epsilon network — only the update rule and step schedule differ.

> **DDIM Inversion for Image Editing**: To edit a real image with a diffusion model: (1) Invert the image with DDIM inversion (50 steps, η=0) to obtain a noise code z. (2) Modify the generation process — swap text prompts, adjust attention maps, or blend noise codes. (3) Regenerate with DDIM sampling from z. The near-determinism of DDIM inversion ensures the reconstruction is faithful and the edit is localized.

- DDIM shares the DDPM training objective — any DDPM-trained model works as a DDIM sampler with no retraining.
- The DDIM update reformulates denoising as: predict x_0 from x_t, then re-noise to x_{t_prev}.
- η=0: fully deterministic; η=1: DDPM-equivalent stochastic; η∈(0,1): interpolated.
- Sub-sequence τ can be any increasing subset of {1,...,T} — uniform spacing works well in practice.
- DDIM inversion enables real image encoding: invert x_0 → z_T, edit, regenerate — the basis of most editing methods.
- DPM-Solver and PNDM improve on DDIM using higher-order ODE solvers, achieving quality at 10–20 steps.

---

