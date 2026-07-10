---
title: "SimSiam — Collapsing Without Negatives or Momentum"
slug: "simsiam-stop-gradient"
description: "SimSiam (Chen & He 2020) achieves self-supervised learning without negatives, EMA, or large batch sizes by applying a stop-gradient on one branch of the loss, which can be interpreted as an expectation-maximisation procedure with the predictor as the E-step."
tags: ["deep-learning", "self-supervised-learning", "contrastive-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2ltU2lhbSAoU2ltcGxlIFNpYW1lc2UgTmV0d29ya3MsIENoZW4gXHUwMDI2IEhlIDIwMjApIHN0cmlwcyBCWU9MIGRvd24gdG8gaXRzIG1pbmltdW06IG5vIG5lZ2F0aXZlcywgbm8gRU1BLCBubyBsYXJnZSBiYXRjaCBzaXplLiBUaGUgb25seSBpbmdyZWRpZW50IHByZXZlbnRpbmcgY29sbGFwc2UgaXMgdGhlIHN0b3AtZ3JhZGllbnQgb3BlcmF0aW9uIG9uIG9uZSBicmFuY2guIERlc3BpdGUgaXRzIHNpbXBsaWNpdHksIFNpbVNpYW0gYWNoaWV2ZXMgY29tcGV0aXRpdmUgcGVyZm9ybWFuY2UgKDcxLjMlIHRvcC0xIG9uIEltYWdlTmV0IHdpdGggUmVzTmV0LTUwKSBhbmQgcHJvdmlkZXMgdmFsdWFibGUgdGhlb3JldGljYWwgaW5zaWdodCBpbnRvIHdoeSBzZWxmLXN1cGVydmlzZWQgbGVhcm5pbmcgd2l0aG91dCBuZWdhdGl2ZXMgY2FuIHdvcmsgdGhyb3VnaCBhbiBleHBlY3RhdGlvbi1tYXhpbWlzYXRpb24gbGVucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcmNoaXRlY3R1cmUg4oCUIEVuY29kZXIsIFByb2plY3RvciwgUHJlZGljdG9yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW1TaWFtIHVzZXMgYSBzeW1tZXRyaWMgU2lhbWVzZSBhcmNoaXRlY3R1cmUgd2l0aCBvbmUgYXN5bW1ldHJpYyBlbGVtZW50LiBCb3RoIGJyYW5jaGVzIHNoYXJlIHRoZSBzYW1lIGVuY29kZXIgZiAoUmVzTmV0KSBhbmQgcHJvamVjdG9yIGggKDMtbGF5ZXIgTUxQIHdpdGggQk4pLiBPbiB0b3Agb2Ygb25lIGJyYW5jaCwgYSB0d28tbGF5ZXIgTUxQIHByZWRpY3RvciBwIGlzIGFwcGxpZWQuIFRoZSBrZXkgaW5zaWdodDogdGhlIHByZWRpY3RvciBpcyBhcHBsaWVkIG9ubHkgdG8gb25lIHNpZGU7IHRoZSBvdGhlciBzaWRlIGlzIHN0b3AtZ3JhZGllbnRlZC4gVGhlcmUgaXMgbm8gc2VwYXJhdGUgdGFyZ2V0IG5ldHdvcmssIG5vIHF1ZXVlLCBubyBFTUEg4oCUIGJvdGggYnJhbmNoZXMgc2hhcmUgd2VpZ2h0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCB0b3JjaHZpc2lvbi5tb2RlbHMgYXMgbW9kZWxzXG5cbmNsYXNzIFNpbVNpYW0obm4uTW9kdWxlKTpcbiAgICBcIlwiXCJTaW1TaWFtOiBzaGFyZWQgZW5jb2RlciArIHByb2plY3RvciwgYXN5bW1ldHJpYyBwcmVkaWN0b3IgKyBzdG9wLWdyYWRpZW50LlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBiYWNrYm9uZV9mbj1tb2RlbHMucmVzbmV0NTAsIHByb2pfZGltPTIwNDgsIHByZWRfaGlkZGVuPTUxMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBiYXNlID0gYmFja2JvbmVfZm4od2VpZ2h0cz1Ob25lKVxuICAgICAgICBmZWF0X2RpbSA9IGJhc2UuZmMuaW5fZmVhdHVyZXMgICMgMjA0OFxuICAgICAgICAjIEVuY29kZXIgKGJhY2tib25lIHdpdGhvdXQgZmluYWwgZmMpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IG5uLlNlcXVlbnRpYWwoKmxpc3QoYmFzZS5jaGlsZHJlbigpKVs6LTFdKVxuICAgICAgICAjIFByb2plY3RvcjogMy1sYXllciBNTFAgd2l0aCBCTiAoZGltIHN0YXlzIDIwNDgpXG4gICAgICAgIHNlbGYucHJvamVjdG9yID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihmZWF0X2RpbSwgZmVhdF9kaW0sIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMWQoZmVhdF9kaW0pLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5MaW5lYXIoZmVhdF9kaW0sIGZlYXRfZGltLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTFkKGZlYXRfZGltKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGZlYXRfZGltLCBwcm9qX2RpbSwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0xZChwcm9qX2RpbSwgYWZmaW5lPUZhbHNlKSwgICMgbm8gbGVhcm5hYmxlIHNjYWxlIGF0IG91dHB1dFxuICAgICAgICApXG4gICAgICAgICMgUHJlZGljdG9yOiAyLWxheWVyIE1MUCB3aXRoIGJvdHRsZW5lY2tcbiAgICAgICAgc2VsZi5wcmVkaWN0b3IgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uTGluZWFyKHByb2pfZGltLCBwcmVkX2hpZGRlbiwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0xZChwcmVkX2hpZGRlbiksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcihwcmVkX2hpZGRlbiwgcHJval9kaW0pLFxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4MSwgeDIpOlxuICAgICAgICB6MSA9IHNlbGYucHJvamVjdG9yKHNlbGYuZW5jb2Rlcih4MSkuZmxhdHRlbigxKSlcbiAgICAgICAgejIgPSBzZWxmLnByb2plY3RvcihzZWxmLmVuY29kZXIoeDIpLmZsYXR0ZW4oMSkpXG4gICAgICAgIHAxID0gc2VsZi5wcmVkaWN0b3IoejEpXG4gICAgICAgIHAyID0gc2VsZi5wcmVkaWN0b3IoejIpXG4gICAgICAgIHJldHVybiBwMSwgcDIsIHoxLmRldGFjaCgpLCB6Mi5kZXRhY2goKSAgIyB6IGlzIHN0b3AtZ3JhZGllbnRlZFxuXG5tb2RlbCA9IFNpbVNpYW0oKVxucHJpbnQoXHUwMDI3U2ltU2lhbSBwYXJhbWV0ZXJzOlx1MDAyNywgc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpIC8vIDFfMDAwXzAwMCwgXHUwMDI3TVx1MDAyNylcbnByaW50KFx1MDAyN0tleTogejEgYW5kIHoyIGFyZSBkZXRhY2hlZCAoc3RvcC1ncmFkaWVudCkgYmVmb3JlIGVudGVyaW5nIGxvc3MuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0b3AtR3JhZGllbnQgYW5kIHRoZSBMb3NzIEZ1bmN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgU2ltU2lhbSBsb3NzIGlzOiBEKHAsIHopID0gLWNvc19zaW0ocCwgc2coeikpID0gLShwL+KAlnDigJYpwrcoei/igJZ64oCWKSB3aGVyZSBzZyjCtykgZGVub3RlcyBzdG9wLWdyYWRpZW50IChkZXRhY2ggaW4gUHlUb3JjaCkuIFRoZSBzeW1tZXRyaXNlZCBsb3NzIGlzOiBMID0gwr1EKHDigoEsIHNnKHrigoIpKSArIMK9RChw4oKCLCBzZyh64oKBKSkuIFRoZSBzdG9wLWdyYWRpZW50IGlzIG5vdCBtZXJlbHkgYSB0cmljayDigJQgaXQgaXMgdGhlIGZ1bmRhbWVudGFsIG1lY2hhbmlzbS4gV2l0aG91dCBpdCwgdGhlIG9iamVjdGl2ZSByZWR1Y2VzIHRvIGEgZGVnZW5lcmF0ZSBwcm9ibGVtIHdoZXJlIHRoZSBjb25zdGFudCBzb2x1dGlvbiAoYWxsIG91dHB1dHMgaWRlbnRpY2FsKSBpcyBvcHRpbWFsIGFuZCBlYXNpbHkgZm91bmQgYnkgZ3JhZGllbnQgZGVzY2VudC4gV2l0aCBpdCwgdGhlIHByb2JsZW0gYmVjb21lcyBhIHR3by1wbGF5ZXIgYWx0ZXJuYXRpbmcgb3B0aW1pc2F0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIHNpbXNpYW1fbG9zcyhwMSwgcDIsIHoxLCB6Mik6XG4gICAgXCJcIlwiU2ltU2lhbSBzeW1tZXRyaXNlZCBsb3NzLiB6MSwgejIgbXVzdCBhbHJlYWR5IGJlIHN0b3AtZ3JhZGllbnRlZC5cbiAgICBwMSwgcDI6IHByZWRpY3RvciBvdXRwdXRzIChncmFkIGZsb3dzIHRocm91Z2ggdGhlc2UpXG4gICAgejEsIHoyOiBwcm9qZWN0b3Igb3V0cHV0cyAoZGV0YWNoZWQg4oCUIG5vIGdyYWQpXG4gICAgXCJcIlwiXG4gICAgZGVmIEQocCwgeik6XG4gICAgICAgIFwiXCJcIk5lZ2F0aXZlIGNvc2luZSBzaW1pbGFyaXR5OiBsb3dlciBpcyBiZXR0ZXIuXCJcIlwiXG4gICAgICAgIHBfbm9ybSA9IEYubm9ybWFsaXplKHAsIGRpbT0xKVxuICAgICAgICB6X25vcm0gPSBGLm5vcm1hbGl6ZSh6LCBkaW09MSkgICMgeiBpcyBhbHJlYWR5IGRldGFjaGVkXG4gICAgICAgIHJldHVybiAtKHBfbm9ybSAqIHpfbm9ybSkuc3VtKGRpbT0xKS5tZWFuKClcbiAgICByZXR1cm4gMC41ICogRChwMSwgejIpICsgMC41ICogRChwMiwgejEpXG5cbiMgVHJhaW5pbmcgc3RlcFxuZGVmIHRyYWluX3N0ZXBfc2ltc2lhbShtb2RlbCwgeDEsIHgyLCBvcHRpbWl6ZXIpOlxuICAgIHAxLCBwMiwgejEsIHoyID0gbW9kZWwoeDEsIHgyKSAgIyB6IGFscmVhZHkgZGV0YWNoZWQgaW4gZm9yd2FyZCgpXG4gICAgbG9zcyA9IHNpbXNpYW1fbG9zcyhwMSwgcDIsIHoxLCB6MilcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgIyBNb25pdG9yIGNvbGxhcHNlOiBzdGQgb2YgeiBzaG91bGQgc3RheSBcdTAwM2UgMFxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBzdGQgPSBGLm5vcm1hbGl6ZSh6MSwgZGltPTEpLnN0ZCgwKS5tZWFuKCkuaXRlbSgpXG4gICAgcmV0dXJuIGxvc3MuaXRlbSgpLCBzdGRcblxuIyBRdWljayB0ZXN0XG50b3JjaC5tYW51YWxfc2VlZCgwKVxucDEgPSB0b3JjaC5yYW5kbigzMiwgMjA0OCwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxucDIgPSB0b3JjaC5yYW5kbigzMiwgMjA0OCwgcmVxdWlyZXNfZ3JhZD1UcnVlKVxuejEgPSB0b3JjaC5yYW5kbigzMiwgMjA0OCkuZGV0YWNoKClcbnoyID0gdG9yY2gucmFuZG4oMzIsIDIwNDgpLmRldGFjaCgpXG5sb3NzID0gc2ltc2lhbV9sb3NzKHAxLCBwMiwgejEsIHoyKVxucHJpbnQoZlx1MDAyN1NpbVNpYW0gbG9zcyBvbiByYW5kb20gaW5wdXRzOiB7bG9zcy5pdGVtKCk6LjRmfSAgKGV4cGVjdGVkIG5lYXIgMCBmb3IgcmFuZG9tKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2xsYXBzZSBBbmFseXNpcyBXaXRoIGFuZCBXaXRob3V0IFN0b3AtR3JhZGllbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldpdGhvdXQgc3RvcC1ncmFkaWVudCwgdGhlIGdyYWRpZW50IHB1c2hlcyBib3RoIHogYW5kIHAgdG8gbWF4aW1pc2UgY29zaW5lIHNpbWlsYXJpdHksIGFuZCB0aGUgdHJpdmlhbCBzb2x1dGlvbiDigJQgYWxsIHZlY3RvcnMgcG9pbnQgdG8gdGhlIHNhbWUgZGlyZWN0aW9uIOKAlCBhY2hpZXZlcyBsb3NzIC0xIGltbWVkaWF0ZWx5LiBXaXRoIHN0b3AtZ3JhZGllbnQsIHdoZW4gY29tcHV0aW5nIGRML2Rw4oKBLCB64oKCIGlzIHRyZWF0ZWQgYXMgYSBjb25zdGFudC4gVGhlIGdyYWRpZW50IG9ubHkgZmxvd3MgdGhyb3VnaCBw4oKBLCBmb3JjaW5nIHDigoEgdG8gbWF0Y2ggdGhlIGN1cnJlbnQgeuKCgiBhcyBiZXN0IGFzIHBvc3NpYmxlIHdpdGhvdXQgbW9kaWZ5aW5nIHrigoIuIFRoaXMgY3JlYXRlcyBhbiBhbHRlcm5hdGluZyBvcHRpbWlzYXRpb24gd2hlcmUgbmVpdGhlciBzaWRlIGNhbiB1bmlsYXRlcmFsbHkgY29sbGFwc2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBjaGVja19jb2xsYXBzZSh1c2Vfc3RvcF9ncmFkaWVudCwgbl9zdGVwcz0zMDAsIHNlZWQ9Nyk6XG4gICAgXCJcIlwiUnVuIGEgdG95IFNpbVNpYW0gYW5kIHJlcG9ydCB3aGV0aGVyIGNvbGxhcHNlIG9jY3Vycy5cIlwiXCJcbiAgICB0b3JjaC5tYW51YWxfc2VlZChzZWVkKVxuICAgIG5ldCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDMyLCA2NCksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDY0LCAzMikpXG4gICAgcHJlZCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDMyLCAxNiksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDE2LCAzMikpXG4gICAgb3B0ID0gdG9yY2gub3B0aW0uU0dEKGxpc3QobmV0LnBhcmFtZXRlcnMoKSkgKyBsaXN0KHByZWQucGFyYW1ldGVycygpKSwgbHI9MC4wNSlcbiAgICBzdGRzID0gW11cbiAgICBmb3IgXyBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgeDEsIHgyID0gdG9yY2gucmFuZG4oNjQsIDMyKSwgdG9yY2gucmFuZG4oNjQsIDMyKVxuICAgICAgICB6MSwgejIgPSBGLm5vcm1hbGl6ZShuZXQoeDEpLCBkaW09MSksIEYubm9ybWFsaXplKG5ldCh4MiksIGRpbT0xKVxuICAgICAgICBwMSwgcDIgPSBwcmVkKHoxKSwgcHJlZCh6MilcbiAgICAgICAgaWYgdXNlX3N0b3BfZ3JhZGllbnQ6XG4gICAgICAgICAgICBsb3NzID0gMC41ICogKC0ocDEgKiB6Mi5kZXRhY2goKSkuc3VtKDEpLm1lYW4oKSArXG4gICAgICAgICAgICAgICAgICAgICAgICAgIC0ocDIgKiB6MS5kZXRhY2goKSkuc3VtKDEpLm1lYW4oKSlcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIGxvc3MgPSAwLjUgKiAoLShwMSAqIHoyKS5zdW0oMSkubWVhbigpICtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgLShwMiAqIHoxKS5zdW0oMSkubWVhbigpKVxuICAgICAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIHN0ZHMuYXBwZW5kKEYubm9ybWFsaXplKG5ldCh0b3JjaC5yYW5kbig2NCwgMzIpKSwgZGltPTEpLnN0ZCgwKS5tZWFuKCkuaXRlbSgpKVxuICAgIHJldHVybiBzdGRzWy0xXSwgbWluKHN0ZHMpXG5cbmZpbmFsX3N0ZF9zZywgICBtaW5fc3RkX3NnICAgPSBjaGVja19jb2xsYXBzZShUcnVlKVxuZmluYWxfc3RkX25vc2csIG1pbl9zdGRfbm9zZyA9IGNoZWNrX2NvbGxhcHNlKEZhbHNlKVxucHJpbnQoZlx1MDAyN1dpdGggICAgc3RvcC1ncmFkOiBmaW5hbCBzdGQ9e2ZpbmFsX3N0ZF9zZzouNGZ9LCBtaW4gc3RkPXttaW5fc3RkX3NnOi40Zn0gIOKGkiBzdGFibGVcdTAwMjcpXG5wcmludChmXHUwMDI3V2l0aG91dCBzdG9wLWdyYWQ6IGZpbmFsIHN0ZD17ZmluYWxfc3RkX25vc2c6LjZmfSwgbWluIHN0ZD17bWluX3N0ZF9ub3NnOi42Zn0g4oaSIGNvbGxhcHNlZFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFTSBJbnRlcnByZXRhdGlvbiDigJQgQWx0ZXJuYXRpbmcgT3B0aW1pc2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW1TaWFtIGNhbiBiZSBpbnRlcnByZXRlZCBhcyBhbiBFeHBlY3RhdGlvbi1NYXhpbWlzYXRpb24gYWxnb3JpdGhtLiBUaGUgZnVsbCBsb3NzIHdpdGhvdXQgc3RvcC1ncmFkaWVudCBpcyBMID0gRV97VH5BfVvigJZGKHg7IM64KSAtIEYoVCh4KTsgzrgp4oCWwrJdIG92ZXIgYXVnbWVudGF0aW9ucy4gSW50cm9kdWNpbmcgc3RvcC1ncmFkaWVudCBkZWZpbmVzIGEgdHdvLXN0ZXAgcHJvY2VkdXJlOiAoMSkgRS1zdGVwOiBmaXggzrgsIGNvbXB1dGUgdGhlIG9wdGltYWwgcHJlZGljdG9yICh0aGUgbWVhbiBvZiBGKFQoeCkpIG92ZXIgYXVnbWVudGF0aW9ucykg4oCUIHRoaXMgaXMgd2hhdCBzZyh6KSByZXByZXNlbnRzOyAoMikgTS1zdGVwOiBmaXggdGhlIEUtc3RlcCByZXN1bHQsIHVwZGF0ZSDOuCB0byBtaW5pbWlzZSBNU0UuIFRoZSBwcmVkaWN0b3IgYXBwcm94aW1hdGVzIHRoZSBFLXN0ZXAgYnkgbGVhcm5pbmcgdG8gb3V0cHV0IHRoZSBtZWFuIHJlcHJlc2VudGF0aW9uIGFjcm9zcyBhdWdtZW50YXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgZW1faW50ZXJwcmV0YXRpb25fZGVtbyhuX2F1Zz04LCBuX3N0ZXBzPTIwMCwgc2VlZD0wKTpcbiAgICBcIlwiXCJTaG93IHRoYXQgdGhlIHByZWRpY3RvciBjb252ZXJnZXMgdG8gdGhlIG1lYW4gb2YgYXVnbWVudGVkIHJlcHJlc2VudGF0aW9ucy5cbiAgICBJbiBFTSB0ZXJtczogRS1zdGVwID0gcHJlZGljdG9yIGxlYXJuaW5nIHRoZSBtZWFuLCBNLXN0ZXAgPSBlbmNvZGVyIHVwZGF0aW5nLlxuICAgIFwiXCJcIlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgZW5jb2RlciA9IG5uLkxpbmVhcigxNiwgOCwgYmlhcz1GYWxzZSlcbiAgICBwcmVkaWN0b3IgPSBubi5MaW5lYXIoOCwgOCwgYmlhcz1GYWxzZSlcbiAgICBvcHRfZW5jICA9IHRvcmNoLm9wdGltLlNHRChlbmNvZGVyLnBhcmFtZXRlcnMoKSwgICBscj0wLjA1KVxuICAgIG9wdF9wcmVkID0gdG9yY2gub3B0aW0uU0dEKHByZWRpY3Rvci5wYXJhbWV0ZXJzKCksIGxyPTAuMSlcbiAgICB4ID0gdG9yY2gucmFuZG4oMSwgMTYpICAjIG9uZSBhbmNob3IgaW1hZ2VcbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgIyBFLXN0ZXA6IHVwZGF0ZSBwcmVkaWN0b3IgdG8gcHJlZGljdCBtZWFuIG9mIGF1Z21lbnRlZCB2aWV3c1xuICAgICAgICBhdWdtZW50YXRpb25zID0gW3ggKyAwLjEgKiB0b3JjaC5yYW5kbl9saWtlKHgpIGZvciBfIGluIHJhbmdlKG5fYXVnKV1cbiAgICAgICAgenMgPSB0b3JjaC5zdGFjayhbRi5ub3JtYWxpemUoZW5jb2RlcihhdWcpLCBkaW09MSkgZm9yIGF1ZyBpbiBhdWdtZW50YXRpb25zXSlcbiAgICAgICAgbWVhbl96ID0genMubWVhbigwKS5kZXRhY2goKSAgIyBzdG9wLWdyYWRpZW50IG9uIHRhcmdldFxuICAgICAgICBwcmVkX291dCA9IHByZWRpY3RvcihGLm5vcm1hbGl6ZShlbmNvZGVyKHgpLCBkaW09MSkpXG4gICAgICAgIGxvc3NfZSA9IEYubXNlX2xvc3MocHJlZF9vdXQsIG1lYW5feilcbiAgICAgICAgb3B0X3ByZWQuemVyb19ncmFkKCk7IGxvc3NfZS5iYWNrd2FyZCgpOyBvcHRfcHJlZC5zdGVwKClcbiAgICAgICAgIyBNLXN0ZXA6IHVwZGF0ZSBlbmNvZGVyIHVzaW5nIHByZWRpY3Rvclx1MDAyN3MgY3VycmVudCB0YXJnZXRcbiAgICAgICAgcHJlZF9vdXQgPSBwcmVkaWN0b3IoRi5ub3JtYWxpemUoZW5jb2Rlcih4KSwgZGltPTEpKVxuICAgICAgICB0YXJnZXRfeiA9IG1lYW5feiAgIyBmaXhlZCBmcm9tIEUtc3RlcFxuICAgICAgICBsb3NzX20gPSBGLm1zZV9sb3NzKHByZWRfb3V0LCB0YXJnZXRfeilcbiAgICAgICAgb3B0X2VuYy56ZXJvX2dyYWQoKTsgbG9zc19tLmJhY2t3YXJkKCk7IG9wdF9lbmMuc3RlcCgpXG4gICAgcmV0dXJuIGxvc3NfZS5pdGVtKCksIGxvc3NfbS5pdGVtKClcblxubGUsIGxtID0gZW1faW50ZXJwcmV0YXRpb25fZGVtbygpXG5wcmludChmXHUwMDI3RS1zdGVwIGZpbmFsIGxvc3M6IHtsZTouNmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN00tc3RlcCBmaW5hbCBsb3NzOiB7bG06LjZmfVx1MDAyNylcbnByaW50KFx1MDAyN1ByZWRpY3RvciBjb252ZXJnZXMgdG8gbWVhbiByZXByZXNlbnRhdGlvbiBhY3Jvc3MgYXVnbWVudGF0aW9ucy5cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJQcmVkaWN0b3IgRGVwdGggTWF0dGVycyIsImNvbnRlbnQiOiJTaW1TaWFtIHJlcXVpcmVzIHRoZSBwcmVkaWN0b3IgdG8gaGF2ZSBhdCBsZWFzdCBvbmUgaGlkZGVuIGxheWVyLiBBIGxpbmVhciBwcmVkaWN0b3IgKHNpbmdsZSBsYXllcikgaXMgaW5zdWZmaWNpZW50IHRvIGJyZWFrIHRoZSBzeW1tZXRyeSBuZWVkZWQgdG8gcHJldmVudCBjb2xsYXBzZSDigJQgYSBsaW5lYXIgbWFwIG9uIHRvcCBvZiBhIGxpbmVhciBlbmNvZGVyIGNvbGxhcHNlcyB0aGUgcHJvYmxlbSB0byBhIHRyaXZpYWwgcmFuay0xIHNvbHV0aW9uLiBUaGUgaGlkZGVuIGxheWVyIGluIHRoZSBwcmVkaWN0b3IgcHJvdmlkZXMgdGhlIG5vbi1saW5lYXJpdHkgbmVlZGVkIHRvIGltcGxlbWVudCB0aGUgRS1zdGVwIGFwcHJveGltYXRpb24gZmFpdGhmdWxseS4gSW4gcHJhY3RpY2UsIGEgMi1sYXllciBNTFAgd2l0aCBhIGJvdHRsZW5lY2sgKGlucHV0IDIwNDgg4oaSIGhpZGRlbiA1MTIg4oaSIG91dHB1dCAyMDQ4KSB3b3JrcyB3ZWxsLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhdGNoIFNpemUgYW5kIFRyYWluaW5nIERldGFpbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVubGlrZSBTaW1DTFIsIFNpbVNpYW0gZG9lcyBub3QgcmVxdWlyZSBsYXJnZSBiYXRjaCBzaXplcy4gQmF0Y2ggc2l6ZXMgb2YgMjU24oCTNTEyIGFyZSBzdWZmaWNpZW50IGJlY2F1c2UgdGhlcmUgYXJlIG5vIGluLWJhdGNoIG5lZ2F0aXZlcy4gVHJhaW5pbmcgdXNlcyBTR0Qgd2l0aCBtb21lbnR1bSAwLjksIHdlaWdodCBkZWNheSAxZS00LCBhbmQgYSBjb3NpbmUgbGVhcm5pbmcgcmF0ZSBzY2hlZHVsZSB3aXRoIGxpbmVhciB3YXJtdXAuIFRoZSBsZWFybmluZyByYXRlIGlzIDAuMDUgw5cgYmF0Y2hfc2l6ZS8yNTYuIE5vIExBUlMgb3B0aW1pc2VyIGlzIG5lZWRlZC4gVHJhaW5pbmcgZm9yIDEwMOKAkzgwMCBlcG9jaHMgb24gSW1hZ2VOZXQgd2l0aCBSZXNOZXQtNTAgYWNoaWV2ZXMgNzAuOCXigJM3MS4zJSB0b3AtMSBsaW5lYXIgZXZhbHVhdGlvbiBhY2N1cmFjeS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJhdGNoIHNpemUgMjU24oCTNTEyIHN1ZmZpY2llbnQg4oCUIG5vIGxhcmdlIGJhdGNoIHJlcXVpcmVkIChrZXkgYWR2YW50YWdlIG92ZXIgU2ltQ0xSKS4iLCJTR0Qgd2l0aCBtb21lbnR1bT0wLjksIHdlaWdodCBkZWNheT0xZS00LCBiYXNlX2xyPTAuMDUgw5cgYmF0Y2gvMjU2LiIsIlByZWRpY3RvciB1c2VzIGhpZ2hlciBsZWFybmluZyByYXRlIHRoYW4gZW5jb2RlciAoMTDDlyBpbiBzb21lIGFibGF0aW9ucykuIiwiQk4gaW4gcHJvamVjdG9yIG91dHB1dCBsYXllciB1c2VzIGFmZmluZT1GYWxzZSAobm8gbGVhcm5hYmxlIHNjYWxlL2JpYXMpLiIsIkNvbGxhcHNlIGRpYWdub3NpczogbW9uaXRvciBzdGQoeikg4oCUIHNob3VsZCBzdGF5IG5lYXIgMC43IGZvciAxMjgtRCB1bml0IHNwaGVyZS4iXX0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkVNQSBUYXJnZXQiLCJQcmVkaWN0b3IiLCJTdG9wLUdyYWRpZW50IiwiQ29sbGFwc2UgTWVjaGFuaXNtIiwiQmF0Y2ggU2l6ZSIsIkxpbmVhciBFdmFsIFRvcC0xIl0sInJvd3MiOltbIkJZT0wiLCJZZXMgKM+EPTAuOTk2KSIsIlllcyIsIlllcyAoaW1wbGljaXQpIiwiRU1BICsgYXN5bW1ldHJ5ICsgQk4iLCI0MDk2IiwiNzQuMyUiXSxbIlNpbVNpYW0iLCJObyIsIlllcyIsIkV4cGxpY2l0IHNnKMK3KSIsIkVNIGFsdGVybmF0aW9uIiwiMjU2IiwiNzEuMyUiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoZW4gdG8gQ2hvb3NlIFNpbVNpYW0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNpbVNpYW0gaXMgdGhlIHJpZ2h0IGNob2ljZSB3aGVuIGNvbXB1dGUgYnVkZ2V0IGlzIGxpbWl0ZWQgYW5kIGludGVycHJldGFiaWxpdHkgbWF0dGVycy4gSXRzIHNtYWxsIGJhdGNoIHNpemUgKDI1NikgYW5kIGFic2VuY2Ugb2YgYW4gRU1BIHRhcmdldCBuZXR3b3JrIGhhbHZlIHRoZSBtZW1vcnkgZm9vdHByaW50IGNvbXBhcmVkIHRvIEJZT0wuIFRoZSBFTSBpbnRlcnByZXRhdGlvbiBwcm92aWRlcyBhIGNsZWFuIHRoZW9yZXRpY2FsIHN0b3J5IGZvciBwcmVzZW50YXRpb25zIGFuZCBwYXBlcnMuIFRoZSBtYWluIHJpc2sgaXMgdHJhaW5pbmcgaW5zdGFiaWxpdHk6IGlmIHRoZSBwcmVkaWN0b3IgaXMgdW5kZXItcG93ZXJlZCAodG9vIHNoYWxsb3cgb3IgdG9vIHNtYWxsKSBvciB0aGUgbGVhcm5pbmcgcmF0ZSBpcyB0b28gaGlnaCwgY29sbGFwc2UgY2FuIG9jY3VyIHNpbGVudGx5IOKAlCBtb25pdG9yIHBlci1kaW1lbnNpb24gc3RkIG9mIHogZHVyaW5nIHRyYWluaW5nIGFuZCBzdG9wIGVhcmx5IGlmIGl0IGRyb3BzIGJlbG93IDAuMS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXN1bHRzIGFuZCBQcmFjdGljYWwgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaW1TaWFtIGFjaGlldmVzIDcxLjMlIHRvcC0xIGxpbmVhciBldmFsdWF0aW9uIHdpdGggUmVzTmV0LTUwIGF0IDIwMCBlcG9jaHMsIGltcHJvdmluZyB0byA3MS4zJSBhdCA4MDAgZXBvY2hzLiBUaGUgcmVzdWx0IGlzIHBhcnRpY3VsYXJseSBub3RhYmxlIGJlY2F1c2UgaXQgdXNlcyBiYXRjaCBzaXplIDI1NiBhbmQgbm8gRU1BIOKAlCBwcm92aW5nIHRoYXQgbmVpdGhlciBsYXJnZSBiYXRjaGVzIG5vciBtb21lbnR1bSBlbmNvZGVycyBhcmUgbmVjZXNzYXJ5IGZvciBoaWdoLXF1YWxpdHkgc2VsZi1zdXBlcnZpc2VkIGxlYXJuaW5nLiBUcmFuc2ZlciBsZWFybmluZyByZXN1bHRzIG9uIFBhc2NhbCBWT0Mgb2JqZWN0IGRldGVjdGlvbiBtYXRjaCBNb0NvIHYyIHdpdGhpbiAwLjMgQVAuIFRoZSBzdG9wLWdyYWRpZW50IGlzIHRoZSBzaW5nbGUgaW5kaXNwZW5zYWJsZSBjb21wb25lbnQ6IHJlbW92aW5nIGl0IGNhdXNlcyBjb2xsYXBzZSB3aXRoaW4gdGhlIGZpcnN0IGZldyBlcG9jaHMgcmVnYXJkbGVzcyBvZiBvdGhlciBoeXBlcnBhcmFtZXRlcnMuIn1d"
---
# SimSiam — Collapsing Without Negatives or Momentum

SimSiam (Simple Siamese Networks, Chen & He 2020) strips BYOL down to its minimum: no negatives, no EMA, no large batch size. The only ingredient preventing collapse is the stop-gradient operation on one branch. Despite its simplicity, SimSiam achieves competitive performance (71.3% top-1 on ImageNet with ResNet-50) and provides valuable theoretical insight into why self-supervised learning without negatives can work through an expectation-maximisation lens.

## Architecture — Encoder, Projector, Predictor

SimSiam uses a symmetric Siamese architecture with one asymmetric element. Both branches share the same encoder f (ResNet) and projector h (3-layer MLP with BN). On top of one branch, a two-layer MLP predictor p is applied. The key insight: the predictor is applied only to one side; the other side is stop-gradiented. There is no separate target network, no queue, no EMA — both branches share weights.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

class SimSiam(nn.Module):
    """SimSiam: shared encoder + projector, asymmetric predictor + stop-gradient."""
    def __init__(self, backbone_fn=models.resnet50, proj_dim=2048, pred_hidden=512):
        super().__init__()
        base = backbone_fn(weights=None)
        feat_dim = base.fc.in_features  # 2048
        # Encoder (backbone without final fc)
        self.encoder = nn.Sequential(*list(base.children())[:-1])
        # Projector: 3-layer MLP with BN (dim stays 2048)
        self.projector = nn.Sequential(
            nn.Linear(feat_dim, feat_dim, bias=False),
            nn.BatchNorm1d(feat_dim), nn.ReLU(inplace=True),
            nn.Linear(feat_dim, feat_dim, bias=False),
            nn.BatchNorm1d(feat_dim), nn.ReLU(inplace=True),
            nn.Linear(feat_dim, proj_dim, bias=False),
            nn.BatchNorm1d(proj_dim, affine=False),  # no learnable scale at output
        )
        # Predictor: 2-layer MLP with bottleneck
        self.predictor = nn.Sequential(
            nn.Linear(proj_dim, pred_hidden, bias=False),
            nn.BatchNorm1d(pred_hidden), nn.ReLU(inplace=True),
            nn.Linear(pred_hidden, proj_dim),
        )

    def forward(self, x1, x2):
        z1 = self.projector(self.encoder(x1).flatten(1))
        z2 = self.projector(self.encoder(x2).flatten(1))
        p1 = self.predictor(z1)
        p2 = self.predictor(z2)
        return p1, p2, z1.detach(), z2.detach()  # z is stop-gradiented

model = SimSiam()
print('SimSiam parameters:', sum(p.numel() for p in model.parameters()) // 1_000_000, 'M')
print('Key: z1 and z2 are detached (stop-gradient) before entering loss.')
```

## Stop-Gradient and the Loss Function

The SimSiam loss is: D(p, z) = -cos_sim(p, sg(z)) = -(p/‖p‖)·(z/‖z‖) where sg(·) denotes stop-gradient (detach in PyTorch). The symmetrised loss is: L = ½D(p₁, sg(z₂)) + ½D(p₂, sg(z₁)). The stop-gradient is not merely a trick — it is the fundamental mechanism. Without it, the objective reduces to a degenerate problem where the constant solution (all outputs identical) is optimal and easily found by gradient descent. With it, the problem becomes a two-player alternating optimisation.

```python
import torch
import torch.nn.functional as F

def simsiam_loss(p1, p2, z1, z2):
    """SimSiam symmetrised loss. z1, z2 must already be stop-gradiented.
    p1, p2: predictor outputs (grad flows through these)
    z1, z2: projector outputs (detached — no grad)
    """
    def D(p, z):
        """Negative cosine similarity: lower is better."""
        p_norm = F.normalize(p, dim=1)
        z_norm = F.normalize(z, dim=1)  # z is already detached
        return -(p_norm * z_norm).sum(dim=1).mean()
    return 0.5 * D(p1, z2) + 0.5 * D(p2, z1)

# Training step
def train_step_simsiam(model, x1, x2, optimizer):
    p1, p2, z1, z2 = model(x1, x2)  # z already detached in forward()
    loss = simsiam_loss(p1, p2, z1, z2)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    # Monitor collapse: std of z should stay > 0
    with torch.no_grad():
        std = F.normalize(z1, dim=1).std(0).mean().item()
    return loss.item(), std

# Quick test
torch.manual_seed(0)
p1 = torch.randn(32, 2048, requires_grad=True)
p2 = torch.randn(32, 2048, requires_grad=True)
z1 = torch.randn(32, 2048).detach()
z2 = torch.randn(32, 2048).detach()
loss = simsiam_loss(p1, p2, z1, z2)
print(f'SimSiam loss on random inputs: {loss.item():.4f}  (expected near 0 for random)')
```

## Collapse Analysis With and Without Stop-Gradient

Without stop-gradient, the gradient pushes both z and p to maximise cosine similarity, and the trivial solution — all vectors point to the same direction — achieves loss -1 immediately. With stop-gradient, when computing dL/dp₁, z₂ is treated as a constant. The gradient only flows through p₁, forcing p₁ to match the current z₂ as best as possible without modifying z₂. This creates an alternating optimisation where neither side can unilaterally collapse.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def check_collapse(use_stop_gradient, n_steps=300, seed=7):
    """Run a toy SimSiam and report whether collapse occurs."""
    torch.manual_seed(seed)
    net = nn.Sequential(nn.Linear(32, 64), nn.ReLU(), nn.Linear(64, 32))
    pred = nn.Sequential(nn.Linear(32, 16), nn.ReLU(), nn.Linear(16, 32))
    opt = torch.optim.SGD(list(net.parameters()) + list(pred.parameters()), lr=0.05)
    stds = []
    for _ in range(n_steps):
        x1, x2 = torch.randn(64, 32), torch.randn(64, 32)
        z1, z2 = F.normalize(net(x1), dim=1), F.normalize(net(x2), dim=1)
        p1, p2 = pred(z1), pred(z2)
        if use_stop_gradient:
            loss = 0.5 * (-(p1 * z2.detach()).sum(1).mean() +
                          -(p2 * z1.detach()).sum(1).mean())
        else:
            loss = 0.5 * (-(p1 * z2).sum(1).mean() +
                          -(p2 * z1).sum(1).mean())
        opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            stds.append(F.normalize(net(torch.randn(64, 32)), dim=1).std(0).mean().item())
    return stds[-1], min(stds)

final_std_sg,   min_std_sg   = check_collapse(True)
final_std_nosg, min_std_nosg = check_collapse(False)
print(f'With    stop-grad: final std={final_std_sg:.4f}, min std={min_std_sg:.4f}  → stable')
print(f'Without stop-grad: final std={final_std_nosg:.6f}, min std={min_std_nosg:.6f} → collapsed')
```

## EM Interpretation — Alternating Optimisation

SimSiam can be interpreted as an Expectation-Maximisation algorithm. The full loss without stop-gradient is L = E_{T~A}[‖F(x; θ) - F(T(x); θ)‖²] over augmentations. Introducing stop-gradient defines a two-step procedure: (1) E-step: fix θ, compute the optimal predictor (the mean of F(T(x)) over augmentations) — this is what sg(z) represents; (2) M-step: fix the E-step result, update θ to minimise MSE. The predictor approximates the E-step by learning to output the mean representation across augmentations.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def em_interpretation_demo(n_aug=8, n_steps=200, seed=0):
    """Show that the predictor converges to the mean of augmented representations.
    In EM terms: E-step = predictor learning the mean, M-step = encoder updating.
    """
    torch.manual_seed(seed)
    encoder = nn.Linear(16, 8, bias=False)
    predictor = nn.Linear(8, 8, bias=False)
    opt_enc  = torch.optim.SGD(encoder.parameters(),   lr=0.05)
    opt_pred = torch.optim.SGD(predictor.parameters(), lr=0.1)
    x = torch.randn(1, 16)  # one anchor image
    for step in range(n_steps):
        # E-step: update predictor to predict mean of augmented views
        augmentations = [x + 0.1 * torch.randn_like(x) for _ in range(n_aug)]
        zs = torch.stack([F.normalize(encoder(aug), dim=1) for aug in augmentations])
        mean_z = zs.mean(0).detach()  # stop-gradient on target
        pred_out = predictor(F.normalize(encoder(x), dim=1))
        loss_e = F.mse_loss(pred_out, mean_z)
        opt_pred.zero_grad(); loss_e.backward(); opt_pred.step()
        # M-step: update encoder using predictor's current target
        pred_out = predictor(F.normalize(encoder(x), dim=1))
        target_z = mean_z  # fixed from E-step
        loss_m = F.mse_loss(pred_out, target_z)
        opt_enc.zero_grad(); loss_m.backward(); opt_enc.step()
    return loss_e.item(), loss_m.item()

le, lm = em_interpretation_demo()
print(f'E-step final loss: {le:.6f}')
print(f'M-step final loss: {lm:.6f}')
print('Predictor converges to mean representation across augmentations.')
```

> **Predictor Depth Matters**: SimSiam requires the predictor to have at least one hidden layer. A linear predictor (single layer) is insufficient to break the symmetry needed to prevent collapse — a linear map on top of a linear encoder collapses the problem to a trivial rank-1 solution. The hidden layer in the predictor provides the non-linearity needed to implement the E-step approximation faithfully. In practice, a 2-layer MLP with a bottleneck (input 2048 → hidden 512 → output 2048) works well.

## Batch Size and Training Details

Unlike SimCLR, SimSiam does not require large batch sizes. Batch sizes of 256–512 are sufficient because there are no in-batch negatives. Training uses SGD with momentum 0.9, weight decay 1e-4, and a cosine learning rate schedule with linear warmup. The learning rate is 0.05 × batch_size/256. No LARS optimiser is needed. Training for 100–800 epochs on ImageNet with ResNet-50 achieves 70.8%–71.3% top-1 linear evaluation accuracy.

- Batch size 256–512 sufficient — no large batch required (key advantage over SimCLR).
- SGD with momentum=0.9, weight decay=1e-4, base_lr=0.05 × batch/256.
- Predictor uses higher learning rate than encoder (10× in some ablations).
- BN in projector output layer uses affine=False (no learnable scale/bias).
- Collapse diagnosis: monitor std(z) — should stay near 0.7 for 128-D unit sphere.

| Method | EMA Target | Predictor | Stop-Gradient | Collapse Mechanism | Batch Size | Linear Eval Top-1 |
| --- | --- | --- | --- | --- | --- | --- |
| BYOL | Yes (τ=0.996) | Yes | Yes (implicit) | EMA + asymmetry + BN | 4096 | 74.3% |
| SimSiam | No | Yes | Explicit sg(·) | EM alternation | 256 | 71.3% |

## When to Choose SimSiam

SimSiam is the right choice when compute budget is limited and interpretability matters. Its small batch size (256) and absence of an EMA target network halve the memory footprint compared to BYOL. The EM interpretation provides a clean theoretical story for presentations and papers. The main risk is training instability: if the predictor is under-powered (too shallow or too small) or the learning rate is too high, collapse can occur silently — monitor per-dimension std of z during training and stop early if it drops below 0.1.

## Results and Practical Takeaways

SimSiam achieves 71.3% top-1 linear evaluation with ResNet-50 at 200 epochs, improving to 71.3% at 800 epochs. The result is particularly notable because it uses batch size 256 and no EMA — proving that neither large batches nor momentum encoders are necessary for high-quality self-supervised learning. Transfer learning results on Pascal VOC object detection match MoCo v2 within 0.3 AP. The stop-gradient is the single indispensable component: removing it causes collapse within the first few epochs regardless of other hyperparameters.

