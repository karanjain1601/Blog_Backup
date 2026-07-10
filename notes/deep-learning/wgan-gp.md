---
title: "WGAN-GP — Gradient Penalty for Lipschitz Constraint"
slug: "wgan-gp"
description: "WGAN-GP (Gulrajani 2017) replaces WGAN weight clipping with a gradient penalty that enforces the 1-Lipschitz constraint on the critic, dramatically improving training stability and enabling conditional GAN architectures that require LayerNorm instead of BatchNorm."
tags: ["deep-learning", "generative-models", "gans"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2Fzc2Vyc3RlaW4gR0FOIChBcmpvdnNreSBldCBhbC4gMjAxNykgcmVwbGFjZWQgdGhlIEpTLWRpdmVyZ2VuY2Ugb2JqZWN0aXZlIG9mIHN0YW5kYXJkIEdBTnMgd2l0aCB0aGUgRWFydGggTW92ZXIgKFdhc3NlcnN0ZWluLTEpIGRpc3RhbmNlLCB3aGljaCBwcm92aWRlcyBtZWFuaW5nZnVsIGdyYWRpZW50cyBldmVuIHdoZW4gZ2VuZXJhdG9yIGFuZCByZWFsIGRpc3RyaWJ1dGlvbnMgZG8gbm90IG92ZXJsYXAuIFRoZSBjcml0aWMgZl93IG11c3QgYmUgMS1MaXBzY2hpdHo6IHxmX3coeCkgLSBmX3coeSl8IOKJpCB8fHggLSB5fHwgZm9yIGFsbCB4LCB5LiBUaGUgb3JpZ2luYWwgV0dBTiBlbmZvcmNlZCB0aGlzIGJ5IGNsaXBwaW5nIGFsbCBjcml0aWMgd2VpZ2h0cyB0byBbLWMsIGNdLiBXR0FOLUdQIChHdWxyYWphbmkgZXQgYWwuIDIwMTcpIGRpc2NhcmRzIGNsaXBwaW5nIGFuZCBkaXJlY3RseSBwZW5hbGlzZXMgdGhlIGdyYWRpZW50IG5vcm0gb2YgdGhlIGNyaXRpYyBhdCBpbnRlcnBvbGF0ZWQgcG9pbnRzIGJldHdlZW4gcmVhbCBhbmQgZmFrZSBzYW1wbGVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByb2JsZW1zIHdpdGggV2VpZ2h0IENsaXBwaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXZWlnaHQgY2xpcHBpbmcgZW5mb3JjZXMgdGhlIExpcHNjaGl0eiBjb25zdHJhaW50IGJ1dCBpbnRyb2R1Y2VzIHNpZ25pZmljYW50IHNpZGUgZWZmZWN0cy4gV2hlbiB0aGUgY2xpcHBpbmcgcmFuZ2UgYyBpcyB0b28gc21hbGwsIGdyYWRpZW50cyB2YW5pc2ggaW4gZGVlcGVyIGNyaXRpY3MgYmVjYXVzZSB0aGUgd2VpZ2h0IG1hZ25pdHVkZSBsaW1pdHMgdGhlIGZ1bmN0aW9uXHUwMDI3cyBzZW5zaXRpdml0eS4gV2hlbiBjIGlzIHRvbyBsYXJnZSwgdGhlIGNvbnN0cmFpbnQgaXMgdG9vIGxvb3NlIGFuZCB0aGUgV2Fzc2Vyc3RlaW4gZXN0aW1hdGUgYmVjb21lcyB1bnJlbGlhYmxlLiBNb3N0IGNyaXRpY2FsbHksIGNsaXBwaW5nIGJpYXNlcyB0aGUgY3JpdGljIHRvd2FyZCBzaW1wbGUgZnVuY3Rpb25zOiB3aXRoIGNsaXBwZWQgd2VpZ2h0cywgdGhlIG9wdGltYWwgY3JpdGljIGZvciBtYW55IGRpc3RyaWJ1dGlvbnMgaXMgYSBuZWFyLWJpbmFyeSBzdGVwIGZ1bmN0aW9uIHRoYXQgc2F0dXJhdGVzIHF1aWNrbHksIGxpbWl0aW5nIHRoZSBxdWFsaXR5IG9mIHRoZSBncmFkaWVudCBzaWduYWwgcHJvdmlkZWQgdG8gdGhlIGdlbmVyYXRvci4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIldlaWdodCBjbGlwcGluZyB0byBbLWMsIGNdIGZvcmNlcyBjcml0aWMgd2VpZ2h0cyB0b3dhcmQgZXh0cmVtZXMgKMKxYyksIHByb2R1Y2luZyBuZWFyLWJpbmFyeSBhY3RpdmF0aW9ucy4iLCJTbWFsbCBjIGNhdXNlcyB2YW5pc2hpbmcgZ3JhZGllbnRzIGluIGRlZXBlciBjcml0aWNzOyBsYXJnZSBjIHdlYWtlbnMgdGhlIExpcHNjaGl0eiBjb25zdHJhaW50LiIsIkNsaXBwZWQgY3JpdGljcyBwcmVmZXIgZGVnZW5lcmF0ZSBzb2x1dGlvbnMgdGhhdCBhcmUgaGFyZCB0byBkaWFnbm9zZSBmcm9tIHRyYWluaW5nIGxvc3MgYWxvbmUuIiwiV0dBTi1HUCBkaXJlY3RseSBwZW5hbGlzZXMgdGhlIGdyYWRpZW50IG5vcm0sIGF2b2lkaW5nIGFsbCBvZiB0aGVzZSBpc3N1ZXMgd2l0aCBhIHNpbmdsZSBhZGRlZCBsb3NzIHRlcm0uIiwiVGhlIGludGVycG9sYXRpb24gc2NoZW1lIHNhbXBsZXMgdW5pZm9ybWx5IGFsb25nIHN0cmFpZ2h0IGxpbmVzIGJldHdlZW4gcmVhbCBhbmQgZmFrZSDigJQgbm90IGp1c3QgaW4gZW1wdHkgc3BhY2UuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBHcmFkaWVudCBQZW5hbHR5IEZvcm11bGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgb3B0aW1hbCBjcml0aWMgdW5kZXIgdGhlIFdhc3NlcnN0ZWluIG9iamVjdGl2ZSBzYXRpc2ZpZXMgfHziiIdfeCBEKHgpfHzigoIgPSAxIGFsbW9zdCBldmVyeXdoZXJlIG9uIHRoZSBzdXBwb3J0IG9mIHBfZGF0YSBhbmQgcF9nLCBhbmQgYWxvbmcgc3RyYWlnaHQgbGluZXMgY29ubmVjdGluZyB0aGVtLiBXR0FOLUdQIGVuZm9yY2VzIHRoaXMgYnkgYWRkaW5nIGEgcGVuYWx0eSB0ZXJtIHRvIHRoZSBjcml0aWMgbG9zczogTF9HUCA9IM67IMK3IEVfe3jMgn1bKHx84oiHX3t4zIJ9IEQoeMyCKXx84oKCIC0gMSnCsl0uIFRoZSBpbnRlcnBvbGF0ZWQgcG9pbnRzIHjMgiA9IM61IMK3IHhfcmVhbCArICgxIC0gzrUpIMK3IHhfZmFrZSB3aGVyZSDOtSB+IFVbMCwgMV0gc2FtcGxlIHVuaWZvcm1seSBhbG9uZyB0aGUgc3RyYWlnaHQgbGluZSBiZXR3ZWVuIHJlYWwgYW5kIGZha2UgZGF0YSBwYWlycy4gVGhlIHBlbmFsdHkgY29lZmZpY2llbnQgzrsgPSAxMCBpcyB0aGUgc3RhbmRhcmQgdmFsdWUuIEJlY2F1c2UgdGhlIHBlbmFsdHkgb3BlcmF0ZXMgb24gaW5kaXZpZHVhbCBzYW1wbGVzIHJhdGhlciB0aGFuIGJhdGNoIHN0YXRpc3RpY3MsIEJhdGNoTm9ybSBjYW5ub3QgYmUgdXNlZCBpbiB0aGUgY3JpdGljLiBVc2UgTGF5ZXJOb3JtIG9yIG5vIG5vcm1hbGlzYXRpb24gaW4gdGhlIGNyaXRpYyBpbnN0ZWFkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IFBlbmFsdHkgSW1wbGVtZW50YXRpb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5hdXRvZ3JhZCBhcyBhdXRvZ3JhZFxuXG5kZWYgY29tcHV0ZV9ncmFkaWVudF9wZW5hbHR5KGNyaXRpYywgcmVhbF9zYW1wbGVzLCBmYWtlX3NhbXBsZXMsIGRldmljZSwgbGFtYmRhX2dwPTEwLjApOlxuICAgIFwiXCJcIldHQU4tR1AgZ3JhZGllbnQgcGVuYWx0eTogaW50ZXJwb2xhdGUgcmVhbC9mYWtlLCBwZW5hbGlzZSBncmFkaWVudCBub3JtLlwiXCJcIlxuICAgIEIgPSByZWFsX3NhbXBsZXMuc2l6ZSgwKVxuICAgICMgU2FtcGxlIGVwc2lsb24gdW5pZm9ybWx5IGZvciBpbnRlcnBvbGF0aW9uXG4gICAgZXBzID0gdG9yY2gucmFuZChCLCAxLCAxLCAxLCBkZXZpY2U9ZGV2aWNlKSAgIyAoQiwxLDEsMSkgZm9yIGltYWdlIGRhdGFcbiAgICBlcHMgPSBlcHMuZXhwYW5kX2FzKHJlYWxfc2FtcGxlcylcbiAgICAjIEludGVycG9sYXRlIGJldHdlZW4gcmVhbCBhbmQgZmFrZVxuICAgIHhfaGF0ID0gKGVwcyAqIHJlYWxfc2FtcGxlcyArICgxIC0gZXBzKSAqIGZha2Vfc2FtcGxlcykucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICAjIENyaXRpYyBzY29yZSBhdCBpbnRlcnBvbGF0ZWQgcG9pbnRzXG4gICAgZF9oYXQgPSBjcml0aWMoeF9oYXQpXG4gICAgIyBDb21wdXRlIGdyYWRpZW50IG9mIGNyaXRpYyBvdXRwdXQgdy5yLnQuIGludGVycG9sYXRlZCBpbnB1dFxuICAgIGdyYWRpZW50cyA9IGF1dG9ncmFkLmdyYWQoXG4gICAgICAgIG91dHB1dHM9ZF9oYXQsXG4gICAgICAgIGlucHV0cz14X2hhdCxcbiAgICAgICAgZ3JhZF9vdXRwdXRzPXRvcmNoLm9uZXNfbGlrZShkX2hhdCksXG4gICAgICAgIGNyZWF0ZV9ncmFwaD1UcnVlLCAgICMgbmVlZGVkIHRvIGRpZmZlcmVudGlhdGUgdGhyb3VnaCBwZW5hbHR5IGZvciBjcml0aWMgdXBkYXRlXG4gICAgICAgIHJldGFpbl9ncmFwaD1UcnVlLFxuICAgICAgICBvbmx5X2lucHV0cz1UcnVlXG4gICAgKVswXVxuICAgICMgRmxhdHRlbiBncmFkaWVudHMgYW5kIGNvbXB1dGUgTDIgbm9ybSBwZXIgc2FtcGxlXG4gICAgZ3JhZGllbnRzID0gZ3JhZGllbnRzLnZpZXcoQiwgLTEpICAgICAgICAgICAgICAgICAgICAgICAjIChCLCBDKkgqVylcbiAgICBncmFkX25vcm0gPSBncmFkaWVudHMubm9ybSgyLCBkaW09MSkgICAgICAgICAgICAgICAgICAgICMgKEIsKVxuICAgIGdyYWRpZW50X3BlbmFsdHkgPSBsYW1iZGFfZ3AgKiAoKGdyYWRfbm9ybSAtIDEpICoqIDIpLm1lYW4oKVxuICAgIHJldHVybiBncmFkaWVudF9wZW5hbHR5XG5cbiMgTWluaW1hbCBjcml0aWMgKG5vIEJhdGNoTm9ybSDigJQgdXNlIExheWVyTm9ybSBvciBubyBub3JtKVxuY2xhc3MgQ3JpdGljKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNoYW5uZWxzPTEsIGltZ19zaXplPTI4KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChjaGFubmVscywgNjQsIDQsIDIsIDEpLCBubi5MZWFreVJlTFUoMC4yKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZCg2NCwgMTI4LCA0LCAyLCAxKSwgbm4uTGVha3lSZUxVKDAuMiksXG4gICAgICAgICAgICBubi5GbGF0dGVuKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoMTI4ICogKGltZ19zaXplIC8vIDQpICoqIDIsIDEpXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYubmV0KHgpXG5cbmNyaXRpYyA9IENyaXRpYygpXG5yZWFsID0gdG9yY2gucmFuZG4oOCwgMSwgMjgsIDI4KVxuZmFrZSA9IHRvcmNoLnJhbmRuKDgsIDEsIDI4LCAyOClcbmdwID0gY29tcHV0ZV9ncmFkaWVudF9wZW5hbHR5KGNyaXRpYywgcmVhbCwgZmFrZSwgZGV2aWNlPVx1MDAyN2NwdVx1MDAyNylcbnByaW50KGZcdTAwMjdHcmFkaWVudCBwZW5hbHR5OiB7Z3AuaXRlbSgpOi40Zn0gIChzaG91bGQgc2hyaW5rIHRvd2FyZCAwIGFzIGNyaXRpYyB0cmFpbnMpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBsZXRlIFdHQU4tR1AgVHJhaW5pbmcgTG9vcCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNyaXRpYyBpcyB1cGRhdGVkIG5fY3JpdGljID0gNSB0aW1lcyBwZXIgZ2VuZXJhdG9yIHN0ZXAuIFRoaXMgYXN5bW1ldHJ5IGV4aXN0cyBiZWNhdXNlIHRoZSBXYXNzZXJzdGVpbiBkaXN0YW5jZSBlc3RpbWF0ZSByZXF1aXJlcyB0aGUgY3JpdGljIHRvIGJlIG5lYXItb3B0aW1hbCBiZWZvcmUgdGhlIGdlbmVyYXRvciBncmFkaWVudCBpcyBtZWFuaW5nZnVsLiBNb3JlIGNyaXRpYyBzdGVwcyBnaXZlIGEgYmV0dGVyIFdhc3NlcnN0ZWluIGVzdGltYXRlIGJ1dCBzbG93IG92ZXJhbGwgdHJhaW5pbmcuIFRoZSBvcHRpbWl6ZXIgZm9yIGJvdGggY3JpdGljIGFuZCBnZW5lcmF0b3IgdXNlcyBBZGFtIHdpdGggzrLigoEgPSAwLjAg4oCUIHplcm8gZmlyc3QgbW9tZW50IGlzIGltcG9ydGFudCBiZWNhdXNlIG1vbWVudHVtIGNhbiBjYXVzZSB0aGUgV2Fzc2Vyc3RlaW4gZXN0aW1hdGUgdG8gb3NjaWxsYXRlIHdoZW4gdGhlIGdlbmVyYXRvciBkaXN0cmlidXRpb24gY2hhbmdlcyByYXBpZGx5LiDOsuKCgiA9IDAuOSBpcyBrZXB0IGZvciBzZWNvbmQgbW9tZW50IHNtb290aGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5hdXRvZ3JhZCBhcyBhdXRvZ3JhZFxuXG5jbGFzcyBHZW5lcmF0b3Iobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbGF0ZW50X2RpbT0xMDAsIGltZ19jaGFubmVscz0xLCBiYXNlPTY0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZChsYXRlbnRfZGltLCBiYXNlICogNCwgNCwgMSwgMCksIG5uLkJhdGNoTm9ybTJkKGJhc2UgKiA0KSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKGJhc2UgKiA0LCBiYXNlICogMiwgNCwgMiwgMSksIG5uLkJhdGNoTm9ybTJkKGJhc2UgKiAyKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKGJhc2UgKiAyLCBiYXNlLCA0LCAyLCAxKSwgbm4uQmF0Y2hOb3JtMmQoYmFzZSksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZChiYXNlLCBpbWdfY2hhbm5lbHMsIDQsIDIsIDEpLCBubi5UYW5oKClcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHopOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoei52aWV3KCp6LnNoYXBlLCAxLCAxKSlcblxuY2xhc3MgV0dBTkdQQ3JpdGljKG5uLk1vZHVsZSk6ICAjIE5PIEJhdGNoTm9ybSBpbiBjcml0aWNcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW1nX2NoYW5uZWxzPTEsIGJhc2U9NjQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGltZ19jaGFubmVscywgYmFzZSwgNCwgMiwgMSksIG5uLkxlYWt5UmVMVSgwLjIpLFxuICAgICAgICAgICAgbm4uQ29udjJkKGJhc2UsIGJhc2UgKiAyLCA0LCAyLCAxKSwgbm4uTGF5ZXJOb3JtKFtiYXNlICogMiwgOCwgOF0pLCBubi5MZWFreVJlTFUoMC4yKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChiYXNlICogMiwgYmFzZSAqIDQsIDQsIDIsIDEpLCBubi5MYXllck5vcm0oW2Jhc2UgKiA0LCA0LCA0XSksIG5uLkxlYWt5UmVMVSgwLjIpLFxuICAgICAgICAgICAgbm4uRmxhdHRlbigpLCBubi5MaW5lYXIoYmFzZSAqIDQgKiA0ICogNCwgMSlcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeClcblxuZGVmIHRyYWluX3dnYW5fZ3AoRywgQywgZGF0YWxvYWRlciwgbl9lcG9jaHM9NSwgbl9jcml0aWM9NSwgbGFtPTEwLjAsIGxyPTFlLTQpOlxuICAgIGRldmljZSA9IG5leHQoRy5wYXJhbWV0ZXJzKCkpLmRldmljZVxuICAgIG9wdF9HID0gdG9yY2gub3B0aW0uQWRhbShHLnBhcmFtZXRlcnMoKSwgbHI9bHIsIGJldGFzPSgwLjAsIDAuOSkpXG4gICAgb3B0X0MgPSB0b3JjaC5vcHRpbS5BZGFtKEMucGFyYW1ldGVycygpLCBscj1sciwgYmV0YXM9KDAuMCwgMC45KSlcbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2Uobl9lcG9jaHMpOlxuICAgICAgICBmb3IgcmVhbF9iYXRjaCwgXyBpbiBkYXRhbG9hZGVyOlxuICAgICAgICAgICAgcmVhbCA9IHJlYWxfYmF0Y2gudG8oZGV2aWNlKVxuICAgICAgICAgICAgQiA9IHJlYWwuc2l6ZSgwKVxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9jcml0aWMpOlxuICAgICAgICAgICAgICAgIHogPSB0b3JjaC5yYW5kbihCLCAxMDAsIGRldmljZT1kZXZpY2UpXG4gICAgICAgICAgICAgICAgZmFrZSA9IEcoeikuZGV0YWNoKClcbiAgICAgICAgICAgICAgICBlcHMgPSB0b3JjaC5yYW5kKEIsIDEsIDEsIDEsIGRldmljZT1kZXZpY2UpLmV4cGFuZF9hcyhyZWFsKVxuICAgICAgICAgICAgICAgIHhfaGF0ID0gKGVwcyAqIHJlYWwgKyAoMSAtIGVwcykgKiBmYWtlKS5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgICAgICAgICAgICAgIGRfaGF0ID0gQyh4X2hhdClcbiAgICAgICAgICAgICAgICBncmFkcyA9IGF1dG9ncmFkLmdyYWQoZF9oYXQsIHhfaGF0LCB0b3JjaC5vbmVzX2xpa2UoZF9oYXQpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcmVhdGVfZ3JhcGg9VHJ1ZSwgcmV0YWluX2dyYXBoPVRydWUpWzBdXG4gICAgICAgICAgICAgICAgZ3AgPSBsYW0gKiAoKGdyYWRzLnZpZXcoQiwgLTEpLm5vcm0oMiwgZGltPTEpIC0gMSkgKiogMikubWVhbigpXG4gICAgICAgICAgICAgICAgbG9zc19DID0gQyhmYWtlKS5tZWFuKCkgLSBDKHJlYWwpLm1lYW4oKSArIGdwXG4gICAgICAgICAgICAgICAgb3B0X0MuemVyb19ncmFkKCk7IGxvc3NfQy5iYWNrd2FyZCgpOyBvcHRfQy5zdGVwKClcbiAgICAgICAgICAgIHogPSB0b3JjaC5yYW5kbihCLCAxMDAsIGRldmljZT1kZXZpY2UpXG4gICAgICAgICAgICBsb3NzX0cgPSAtQyhHKHopKS5tZWFuKClcbiAgICAgICAgICAgIG9wdF9HLnplcm9fZ3JhZCgpOyBsb3NzX0cuYmFja3dhcmQoKTsgb3B0X0cuc3RlcCgpXG4gICAgICAgIHByaW50KGZcdTAwMjdFcG9jaCB7ZXBvY2grMX06IExfQz17bG9zc19DLml0ZW0oKTouNGZ9ICBMX0c9e2xvc3NfRy5pdGVtKCk6LjRmfVx1MDAyNylcblxucHJpbnQoXHUwMDI3V0dBTi1HUDogY3JpdGljIHVwZGF0ZWQgNXggcGVyIGdlbmVyYXRvciBzdGVwLCBBZGFtIHdpdGggYmV0YXM9KDAuMCwgMC45KVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSMSBHcmFkaWVudCBQZW5hbHR5IOKAlCBTaW1wbGVyIEFsdGVybmF0aXZlIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2guYXV0b2dyYWQgYXMgYXV0b2dyYWRcblxuZGVmIHIxX2dyYWRpZW50X3BlbmFsdHkoY3JpdGljLCByZWFsX3NhbXBsZXMsIGdhbW1hPTEwLjApOlxuICAgIFwiXCJcIlIxIHJlZ3VsYXJpc2F0aW9uOiBwZW5hbGlzZSBncmFkaWVudCBub3JtIGF0IHJlYWwgZGF0YSBvbmx5IChNZXNjaGVkZXIgMjAxOCkuXG5cbiAgICBTaW1wbGVyIHRoYW4gV0dBTi1HUDogbm8gaW50ZXJwb2xhdGlvbiBuZWVkZWQsIG9ubHkgcmVhbCBzYW1wbGVzIHVzZWQuXG4gICAgU3RhYmxlIGZvciBzdGFuZGFyZCBHQU4gKG5vbi1zYXR1cmF0aW5nKSBsb3NzIHdpdGggZ3JhZGllbnQgcGVuYWx0eS5cbiAgICBMID0gRVtzb2Z0cGx1cygtRChyZWFsKSldICsgRVtzb2Z0cGx1cyhEKGZha2UpKV0gKyBnYW1tYS8yICogRVt8fGdyYWRfRChyZWFsKXx8XjJdXG4gICAgXCJcIlwiXG4gICAgcmVhbCA9IHJlYWxfc2FtcGxlcy5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgIGRfcmVhbCA9IGNyaXRpYyhyZWFsKVxuICAgIGdyYWRzID0gYXV0b2dyYWQuZ3JhZChcbiAgICAgICAgb3V0cHV0cz1kX3JlYWwuc3VtKCksXG4gICAgICAgIGlucHV0cz1yZWFsLFxuICAgICAgICBjcmVhdGVfZ3JhcGg9VHJ1ZSxcbiAgICAgICAgb25seV9pbnB1dHM9VHJ1ZVxuICAgIClbMF1cbiAgICByMV9wZW5hbHR5ID0gKGdhbW1hIC8gMi4wKSAqIChncmFkcy52aWV3KGdyYWRzLnNpemUoMCksIC0xKS5ub3JtKDIsIGRpbT0xKSAqKiAyKS5tZWFuKClcbiAgICByZXR1cm4gcjFfcGVuYWx0eVxuXG5jbGFzcyBTaW1wbGVEaXNjcmltaW5hdG9yKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uRmxhdHRlbigpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDI4ICogMjgsIDI1NiksIG5uLkxlYWt5UmVMVSgwLjIpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDI1NiwgMTI4KSwgbm4uTGVha3lSZUxVKDAuMiksXG4gICAgICAgICAgICBubi5MaW5lYXIoMTI4LCAxKVxuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldCh4KVxuXG5EID0gU2ltcGxlRGlzY3JpbWluYXRvcigpXG5yZWFsX2RhdGEgPSB0b3JjaC5yYW5kbigxNiwgMSwgMjgsIDI4KVxucjEgPSByMV9ncmFkaWVudF9wZW5hbHR5KEQsIHJlYWxfZGF0YSwgZ2FtbWE9MTAuMClcbnByaW50KGZcdTAwMjdSMSBwZW5hbHR5OiB7cjEuaXRlbSgpOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdSMSBhZHZhbnRhZ2U6IG5vIGZha2Utc2FtcGxlIGludGVycG9sYXRpb24sIGxvd2VyIGNvbXB1dGUsIHVzZWQgaW4gU3R5bGVHQU4yXHUwMDI3KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUjEgcmVndWxhcmlzYXRpb24gZGlmZmVycyBmcm9tIFdHQU4tR1AgaW4gYSBrZXkgd2F5OiBpdCBvbmx5IHBlbmFsaXNlcyBncmFkaWVudHMgYXQgcmVhbCBkYXRhIHBvaW50cywgbm90IGF0IGludGVycG9sYXRlZCBwb2ludHMgYmV0d2VlbiByZWFsIGFuZCBmYWtlLiBUaGlzIG1ha2VzIFIxIHNpbXBsZXIgdG8gaW1wbGVtZW50IChubyBpbnRlcnBvbGF0aW9uIHN0ZXApIGFuZCBzbGlnaHRseSBjaGVhcGVyIChvbmUgZmV3ZXIgYmFja3dhcmQgcGFzcykuIEl0IGlzIHVzZWQgYXMgdGhlIGRlZmF1bHQgaW4gU3R5bGVHQU4sIFN0eWxlR0FOMiwgYW5kIFN0eWxlR0FOLVhMLiBXR0FOLUdQIGlzIHByZWZlcnJlZCB3aGVuIHRoZSBnZW5lcmF0b3IgaXMgZmFyIGZyb20gdGhlIGRhdGEgZGlzdHJpYnV0aW9uIChlYXJseSB0cmFpbmluZykgYmVjYXVzZSBwZW5hbGlzaW5nIGludGVycG9sYW50cyBwcm92aWRlcyBncmFkaWVudCBpbmZvcm1hdGlvbiBpbiByZWdpb25zIGJldHdlZW4gcmVhbCBhbmQgZmFrZS4gRm9yIG1vc3QgcHJhY3RpY2FsIGFwcGxpY2F0aW9ucyB3aGVyZSB0cmFpbmluZyBpcyB3ZWxsLWluaXRpYWxpc2VkLCBSMSBpcyB0aGUgcmVjb21tZW5kZWQgZGVmYXVsdC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXR0FOIENsaXBwaW5nIHZzIFdHQU4tR1A6IExvc3MgQ3VydmVzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbWF0cGxvdGxpYlxubWF0cGxvdGxpYi51c2UoXHUwMDI3QWdnXHUwMDI3KVxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcnVuX3RveV93Z2FuKHVzZV9ncD1UcnVlLCBuX3N0ZXBzPTMwMCwgc2VlZD0wKTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZChzZWVkKVxuICAgIEcgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcigxLCAzMiksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDMyLCAxKSlcbiAgICBDID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMSwgMzIpLCBubi5MZWFreVJlTFUoMC4yKSwgbm4uTGluZWFyKDMyLCAxKSlcbiAgICBvcHRfRyA9IHRvcmNoLm9wdGltLkFkYW0oRy5wYXJhbWV0ZXJzKCksIGxyPTFlLTMsIGJldGFzPSgwLjAsIDAuOSkpXG4gICAgb3B0X0MgPSB0b3JjaC5vcHRpbS5BZGFtKEMucGFyYW1ldGVycygpLCBscj0xZS0zLCBiZXRhcz0oMC4wLCAwLjkpKVxuICAgIHdfZGlzdHMgPSBbXVxuICAgIGZvciBzdGVwIGluIHJhbmdlKG5fc3RlcHMpOlxuICAgICAgICByZWFsID0gdG9yY2gucmFuZG4oNjQsIDEpICogMC41ICsgMi4wXG4gICAgICAgIGZvciBfIGluIHJhbmdlKDUpOlxuICAgICAgICAgICAgeiA9IHRvcmNoLnJhbmRuKDY0LCAxKVxuICAgICAgICAgICAgZmFrZSA9IEcoeikuZGV0YWNoKClcbiAgICAgICAgICAgIGlmIHVzZV9ncDpcbiAgICAgICAgICAgICAgICBlcHMgPSB0b3JjaC5yYW5kKDY0LCAxKVxuICAgICAgICAgICAgICAgIHhoYXQgPSAoZXBzICogcmVhbCArICgxIC0gZXBzKSAqIGZha2UpLnJlcXVpcmVzX2dyYWRfKFRydWUpXG4gICAgICAgICAgICAgICAgZF94aGF0ID0gQyh4aGF0KVxuICAgICAgICAgICAgICAgIGdyYWRzID0gdG9yY2guYXV0b2dyYWQuZ3JhZChkX3hoYXQuc3VtKCksIHhoYXQsIGNyZWF0ZV9ncmFwaD1UcnVlKVswXVxuICAgICAgICAgICAgICAgIGdwID0gMTAuMCAqICgoZ3JhZHMubm9ybSgyLCBkaW09MSkgLSAxKSAqKiAyKS5tZWFuKClcbiAgICAgICAgICAgICAgICBsb3NzX0MgPSBDKGZha2UpLm1lYW4oKSAtIEMocmVhbCkubWVhbigpICsgZ3BcbiAgICAgICAgICAgIGVsc2U6XG4gICAgICAgICAgICAgICAgbG9zc19DID0gQyhmYWtlKS5tZWFuKCkgLSBDKHJlYWwpLm1lYW4oKVxuICAgICAgICAgICAgb3B0X0MuemVyb19ncmFkKCk7IGxvc3NfQy5iYWNrd2FyZCgpOyBvcHRfQy5zdGVwKClcbiAgICAgICAgICAgIGlmIG5vdCB1c2VfZ3A6XG4gICAgICAgICAgICAgICAgZm9yIHAgaW4gQy5wYXJhbWV0ZXJzKCk6XG4gICAgICAgICAgICAgICAgICAgIHAuZGF0YS5jbGFtcF8oLTAuMDEsIDAuMDEpXG4gICAgICAgIHogPSB0b3JjaC5yYW5kbig2NCwgMSlcbiAgICAgICAgbG9zc19HID0gLUMoRyh6KSkubWVhbigpXG4gICAgICAgIG9wdF9HLnplcm9fZ3JhZCgpOyBsb3NzX0cuYmFja3dhcmQoKTsgb3B0X0cuc3RlcCgpXG4gICAgICAgIGlmIHN0ZXAgJSAxMCA9PSAwOlxuICAgICAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICAgICAgd19kaXN0cy5hcHBlbmQoYWJzKGxvc3NfQy5pdGVtKCkpKVxuICAgIHJldHVybiB3X2Rpc3RzXG5cbmdwX2N1cnZlICAgPSBydW5fdG95X3dnYW4odXNlX2dwPVRydWUpXG5jbGlwX2N1cnZlID0gcnVuX3RveV93Z2FuKHVzZV9ncD1GYWxzZSlcbnByaW50KGZcdTAwMjdXR0FOLUdQICAgZmluYWwgVy1kaXN0IHByb3h5OiB7Z3BfY3VydmVbLTFdOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3V0dBTi1jbGlwIGZpbmFsIFctZGlzdCBwcm94eToge2NsaXBfY3VydmVbLTFdOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdXR0FOLUdQIGNvbnZlcmdlcyBtb3JlIHNtb290aGx5OyBjbGlwcGluZyBjYXVzZXMgb3NjaWxsYXRpb24vc2xvdyBjb252ZXJnZW5jZVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZW1vdmluZyBCYXRjaE5vcm0gZnJvbSB0aGUgQ3JpdGljIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXRjaE5vcm0gbm9ybWFsaXNlcyBhY3RpdmF0aW9ucyBhY3Jvc3MgdGhlIGJhdGNoLCBtYWtpbmcgZWFjaCBzYW1wbGVcdTAwMjdzIGdyYWRpZW50IGRlcGVuZCBvbiBldmVyeSBvdGhlciBzYW1wbGUgaW4gdGhlIGJhdGNoLiBUaGlzIHZpb2xhdGVzIHRoZSBwZXItc2FtcGxlIExpcHNjaGl0eiBjb25zdHJhaW50IHRoYXQgV0dBTi1HUCBlbmZvcmNlcyDigJQgdGhlIGdyYWRpZW50IHBlbmFsdHkgdGFyZ2V0cyB0aGUgZ3JhZGllbnQgYXQgaW5kaXZpZHVhbCBpbnRlcnBvbGF0ZWQgcG9pbnRzLCBidXQgQmF0Y2hOb3JtIGNvdXBsaW5nIG1lYW5zIHRoZSBncmFkaWVudCBkZXBlbmRzIG9uIHdoYXQgb3RoZXIgc2FtcGxlcyBhcmUgaW4gdGhlIGJhdGNoLiBUaGUgZml4IGlzIHNpbXBsZTogcmVwbGFjZSBCYXRjaE5vcm0gaW4gdGhlIGNyaXRpYyB3aXRoIExheWVyTm9ybSAobm9ybWFsaXNlcyBwZXIgc2FtcGxlIGFjcm9zcyBjaGFubmVscykgb3IgSW5zdGFuY2VOb3JtIChub3JtYWxpc2VzIHBlciBzYW1wbGUgcGVyIGNoYW5uZWwpLCBvciBvbWl0IG5vcm1hbGlzYXRpb24gZW50aXJlbHkgaW4gdGhlIGNyaXRpYy4gVGhlIGdlbmVyYXRvciBjYW4gc3RpbGwgdXNlIEJhdGNoTm9ybSBub3JtYWxseS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkJhdGNoTm9ybSBCcmVha3MgR3JhZGllbnQgUGVuYWx0eSIsImNvbnRlbnQiOiJOZXZlciB1c2UgQmF0Y2hOb3JtIGluIHRoZSBXR0FOLUdQIGNyaXRpYy4gVGhlIHBlci1zYW1wbGUgZ3JhZGllbnQgYXQgeF9oYXQgbXVzdCBiZSBpbmRlcGVuZGVudCBvZiBvdGhlciBiYXRjaCBtZW1iZXJzLCBidXQgQmF0Y2hOb3JtIG5vcm1hbGlzZXMgYWNyb3NzIHRoZSBiYXRjaCwgY291cGxpbmcgYWxsIGdyYWRpZW50cy4gVXNlIExheWVyTm9ybSwgSW5zdGFuY2VOb3JtLCBvciBubyBub3JtYWxpc2F0aW9uIGluIHRoZSBjcml0aWMuIFRoZSBnZW5lcmF0b3IgaXMgdW5hZmZlY3RlZCBhbmQgY2FuIHVzZSBCYXRjaE5vcm0gYXMgdXN1YWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSHlwZXJwYXJhbWV0ZXJzIGFuZCBQcmFjdGljYWwgVGlwcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHN0YW5kYXJkIFdHQU4tR1AgcmVjaXBlIGZyb20gR3VscmFqYW5pIGV0IGFsLiBpczogzrsgPSAxMCwgbl9jcml0aWMgPSA1IChjcml0aWMgc3RlcHMgcGVyIGdlbmVyYXRvciBzdGVwKSwgQWRhbSB3aXRoIGxyID0gMWUtNCBhbmQgYmV0YXMgPSAoMC4wLCAwLjkpLiBUaGUgemVybyBmaXJzdCBtb21lbnQgKM6y4oKBID0gMCkgaXMgaW1wb3J0YW50IOKAlCBtb21lbnR1bSBjYW4gZGVzdGFiaWxpc2UgV2Fzc2Vyc3RlaW4gdHJhaW5pbmcuIFRoZSBjcml0aWMgaXMgdHJhaW5lZCB0byBjb252ZXJnZW5jZSBiZWZvcmUgZWFjaCBnZW5lcmF0b3IgdXBkYXRlLCBhcHByb3hpbWF0ZWQgYnkgbl9jcml0aWMgc3RlcHMuIEluY3JlYXNpbmcgbl9jcml0aWMgaW1wcm92ZXMgY3JpdGljIHF1YWxpdHkgYnV0IHNsb3dzIHRyYWluaW5nLiBUaGUgZ3JhZGllbnQgcGVuYWx0eSBhZGRzIG9uZSBhZGRpdGlvbmFsIGJhY2t3YXJkIHBhc3MgcGVyIGNyaXRpYyBzdGVwICh0aHJvdWdoIGNyZWF0ZV9ncmFwaD1UcnVlKSB3aGljaCByb3VnaGx5IGRvdWJsZXMgY3JpdGljIGNvbXB1dGF0aW9uLiBPbiBjb25kaXRpb25hbCBHQU5zLCBXR0FOLUdQIGlzIHRoZSBzdGFuZGFyZCBjaG9pY2UgYmVjYXVzZSBpdCBhbGxvd3MgYXJiaXRyYXJ5IGNyaXRpYyBhcmNoaXRlY3R1cmVzIHdpdGhvdXQgbm9ybWFsaXNhdGlvbiBjb25zdHJhaW50cy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiTGlwc2NoaXR6IEVuZm9yY2VtZW50IiwiQmF0Y2hOb3JtIGluIENyaXRpYyIsIlN0YWJpbGl0eSIsIkNvbXB1dGUgT3ZlcmhlYWQiLCJGSUQgKHR5cGljYWwpIl0sInJvd3MiOltbIlN0YW5kYXJkIEdBTiIsIk5vbmUgKEpTIGRpdmVyZ2VuY2UpIiwiQWxsb3dlZCIsIkxvdyDigJQgbW9kZSBjb2xsYXBzZSwgdmFuaXNoaW5nIGdyYWRzIiwiTm9uZSIsIlZhcmllcyB3aWRlbHkiXSxbIldHQU4gKGNsaXBwaW5nKSIsIldlaWdodCBjbGlwcGluZyB0byBbLWMsIGNdIiwiTm90IHJlY29tbWVuZGVkIiwiTW9kZXJhdGUg4oCUIGJpYXNlcyB0b3dhcmQgc2ltcGxlIGZ1bmN0aW9ucyIsIk1pbmltYWwiLCJCZXR0ZXIgdGhhbiBHQU4iXSxbIldHQU4tR1AiLCJHcmFkaWVudCBwZW5hbHR5IG9uIGludGVycG9sYW50cyIsIk5vdCBhbGxvd2VkICh1c2UgTGF5ZXJOb3JtKSIsIkhpZ2gg4oCUIHN0YWJsZSBhY3Jvc3MgYXJjaGl0ZWN0dXJlcyIsIn4yeCBjcml0aWMgYmFja3dhcmQiLCJTdHJvbmcgYmFzZWxpbmUiXSxbIlIxLUdBTiIsIkdyYWRpZW50IHBlbmFsdHkgYXQgcmVhbCBkYXRhIG9ubHkiLCJBbGxvd2VkIGluIGdlbmVyYXRvciIsIkhpZ2gg4oCUIHNpbXBsZXIsIGxlc3MgY29tcHV0ZSIsIn4xLjV4IGNyaXRpYyBiYWNrd2FyZCIsIkNvbXBhcmFibGUgdG8gV0dBTi1HUCJdLFsiU04tR0FOIiwiU3BlY3RyYWwgbm9ybSBvbiBhbGwgY3JpdGljIHdlaWdodHMiLCJBbGxvd2VkIiwiSGlnaCDigJQgbm8gZXh0cmEgYmFja3dhcmQgcGFzcyIsIk1pbmltYWwgKFNWRCBwZXIgbGF5ZXIpIiwiQ29tcGV0aXRpdmUgRklEIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVzZSB0b3JjaC5hdXRvZ3JhZC5ncmFkIHdpdGggY3JlYXRlX2dyYXBoPVRydWUgdG8gY29tcHV0ZSB0aGUgZ3JhZGllbnQgcGVuYWx0eSDigJQgc3RhbmRhcmQgYmFja3dhcmQoKSBjYW5ub3QgYmUgdXNlZCBiZWNhdXNlIHlvdSBuZWVkIGdyYWRpZW50cyBvZiBncmFkaWVudHMuIiwibGFtYmRhPTEwIGlzIHJvYnVzdCBhY3Jvc3MgaW1hZ2UgcmVzb2x1dGlvbnM7IHR1bmluZyBpcyByYXJlbHkgbmVlZGVkLiBMb3dlciBsYW1iZGEgKH4xKSBtYXkgaGVscCBpZiB0aGUgcGVuYWx0eSBkb21pbmF0ZXMgZWFybHkgdHJhaW5pbmcuIiwiUjEgcmVndWxhcmlzYXRpb24gKHBlbmFsaXNlIGdyYWRpZW50IGF0IHJlYWwgZGF0YSBvbmx5KSBpcyBzaW1wbGVyLCBjb21wdXRhdGlvbmFsbHkgY2hlYXBlciwgYW5kIHVzZWQgaW4gU3R5bGVHQU4yIOKAlCBwcmVmZXIgaXQgZm9yIG5ldyBwcm9qZWN0cy4iLCJXR0FOLUdQIGNyaXRpYyBsb3NzIHNob3VsZCBkZWNyZWFzZSBhbmQgZXZlbnR1YWxseSBwbGF0ZWF1IG5lYXIgYSBzbWFsbCBwb3NpdGl2ZSB2YWx1ZSDigJQgaWYgaXQgb3NjaWxsYXRlcyBvciBncm93cywgcmVkdWNlIHRoZSBsZWFybmluZyByYXRlLiIsIlRoZSBXYXNzZXJzdGVpbiBkaXN0YW5jZSBlc3RpbWF0ZSAobmVnYXRpdmUgY3JpdGljIGxvc3MpIGlzIGEgbWVhbmluZ2Z1bCB0cmFpbmluZyBzaWduYWw6IGRlY3JlYXNpbmcgVy1kaXN0YW5jZSBjb3JyZXNwb25kcyB0byBpbXByb3ZpbmcgZ2VuZXJhdGlvbiBxdWFsaXR5LiIsIk1vbml0b3IgZ3JhZGllbnQgbm9ybXMgYXQgaW50ZXJwb2xhdGVkIHBvaW50czogdGhleSBzaG91bGQgaG92ZXIgbmVhciAxIGFmdGVyIGEgZmV3IGh1bmRyZWQgdHJhaW5pbmcgc3RlcHMgaWYgdGhlIHBlbmFsdHkgaXMgd29ya2luZyBjb3JyZWN0bHkuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# WGAN-GP — Gradient Penalty for Lipschitz Constraint

Wasserstein GAN (Arjovsky et al. 2017) replaced the JS-divergence objective of standard GANs with the Earth Mover (Wasserstein-1) distance, which provides meaningful gradients even when generator and real distributions do not overlap. The critic f_w must be 1-Lipschitz: |f_w(x) - f_w(y)| ≤ ||x - y|| for all x, y. The original WGAN enforced this by clipping all critic weights to [-c, c]. WGAN-GP (Gulrajani et al. 2017) discards clipping and directly penalises the gradient norm of the critic at interpolated points between real and fake samples.

## Problems with Weight Clipping

Weight clipping enforces the Lipschitz constraint but introduces significant side effects. When the clipping range c is too small, gradients vanish in deeper critics because the weight magnitude limits the function's sensitivity. When c is too large, the constraint is too loose and the Wasserstein estimate becomes unreliable. Most critically, clipping biases the critic toward simple functions: with clipped weights, the optimal critic for many distributions is a near-binary step function that saturates quickly, limiting the quality of the gradient signal provided to the generator.

- Weight clipping to [-c, c] forces critic weights toward extremes (±c), producing near-binary activations.
- Small c causes vanishing gradients in deeper critics; large c weakens the Lipschitz constraint.
- Clipped critics prefer degenerate solutions that are hard to diagnose from training loss alone.
- WGAN-GP directly penalises the gradient norm, avoiding all of these issues with a single added loss term.
- The interpolation scheme samples uniformly along straight lines between real and fake — not just in empty space.

## The Gradient Penalty Formulation

The optimal critic under the Wasserstein objective satisfies ||∇_x D(x)||₂ = 1 almost everywhere on the support of p_data and p_g, and along straight lines connecting them. WGAN-GP enforces this by adding a penalty term to the critic loss: L_GP = λ · E_{x̂}[(||∇_{x̂} D(x̂)||₂ - 1)²]. The interpolated points x̂ = ε · x_real + (1 - ε) · x_fake where ε ~ U[0, 1] sample uniformly along the straight line between real and fake data pairs. The penalty coefficient λ = 10 is the standard value. Because the penalty operates on individual samples rather than batch statistics, BatchNorm cannot be used in the critic. Use LayerNorm or no normalisation in the critic instead.

## Gradient Penalty Implementation

```python
import torch
import torch.nn as nn
import torch.autograd as autograd

def compute_gradient_penalty(critic, real_samples, fake_samples, device, lambda_gp=10.0):
    """WGAN-GP gradient penalty: interpolate real/fake, penalise gradient norm."""
    B = real_samples.size(0)
    # Sample epsilon uniformly for interpolation
    eps = torch.rand(B, 1, 1, 1, device=device)  # (B,1,1,1) for image data
    eps = eps.expand_as(real_samples)
    # Interpolate between real and fake
    x_hat = (eps * real_samples + (1 - eps) * fake_samples).requires_grad_(True)
    # Critic score at interpolated points
    d_hat = critic(x_hat)
    # Compute gradient of critic output w.r.t. interpolated input
    gradients = autograd.grad(
        outputs=d_hat,
        inputs=x_hat,
        grad_outputs=torch.ones_like(d_hat),
        create_graph=True,   # needed to differentiate through penalty for critic update
        retain_graph=True,
        only_inputs=True
    )[0]
    # Flatten gradients and compute L2 norm per sample
    gradients = gradients.view(B, -1)                       # (B, C*H*W)
    grad_norm = gradients.norm(2, dim=1)                    # (B,)
    gradient_penalty = lambda_gp * ((grad_norm - 1) ** 2).mean()
    return gradient_penalty

# Minimal critic (no BatchNorm — use LayerNorm or no norm)
class Critic(nn.Module):
    def __init__(self, channels=1, img_size=28):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(channels, 64, 4, 2, 1), nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, 4, 2, 1), nn.LeakyReLU(0.2),
            nn.Flatten(),
            nn.Linear(128 * (img_size // 4) ** 2, 1)
        )
    def forward(self, x):
        return self.net(x)

critic = Critic()
real = torch.randn(8, 1, 28, 28)
fake = torch.randn(8, 1, 28, 28)
gp = compute_gradient_penalty(critic, real, fake, device='cpu')
print(f'Gradient penalty: {gp.item():.4f}  (should shrink toward 0 as critic trains)')
```

## Complete WGAN-GP Training Loop

The critic is updated n_critic = 5 times per generator step. This asymmetry exists because the Wasserstein distance estimate requires the critic to be near-optimal before the generator gradient is meaningful. More critic steps give a better Wasserstein estimate but slow overall training. The optimizer for both critic and generator uses Adam with β₁ = 0.0 — zero first moment is important because momentum can cause the Wasserstein estimate to oscillate when the generator distribution changes rapidly. β₂ = 0.9 is kept for second moment smoothing.

```python
import torch
import torch.nn as nn
import torch.autograd as autograd

class Generator(nn.Module):
    def __init__(self, latent_dim=100, img_channels=1, base=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, base * 4, 4, 1, 0), nn.BatchNorm2d(base * 4), nn.ReLU(),
            nn.ConvTranspose2d(base * 4, base * 2, 4, 2, 1), nn.BatchNorm2d(base * 2), nn.ReLU(),
            nn.ConvTranspose2d(base * 2, base, 4, 2, 1), nn.BatchNorm2d(base), nn.ReLU(),
            nn.ConvTranspose2d(base, img_channels, 4, 2, 1), nn.Tanh()
        )
    def forward(self, z):
        return self.net(z.view(*z.shape, 1, 1))

class WGANGPCritic(nn.Module):  # NO BatchNorm in critic
    def __init__(self, img_channels=1, base=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(img_channels, base, 4, 2, 1), nn.LeakyReLU(0.2),
            nn.Conv2d(base, base * 2, 4, 2, 1), nn.LayerNorm([base * 2, 8, 8]), nn.LeakyReLU(0.2),
            nn.Conv2d(base * 2, base * 4, 4, 2, 1), nn.LayerNorm([base * 4, 4, 4]), nn.LeakyReLU(0.2),
            nn.Flatten(), nn.Linear(base * 4 * 4 * 4, 1)
        )
    def forward(self, x):
        return self.net(x)

def train_wgan_gp(G, C, dataloader, n_epochs=5, n_critic=5, lam=10.0, lr=1e-4):
    device = next(G.parameters()).device
    opt_G = torch.optim.Adam(G.parameters(), lr=lr, betas=(0.0, 0.9))
    opt_C = torch.optim.Adam(C.parameters(), lr=lr, betas=(0.0, 0.9))
    for epoch in range(n_epochs):
        for real_batch, _ in dataloader:
            real = real_batch.to(device)
            B = real.size(0)
            for _ in range(n_critic):
                z = torch.randn(B, 100, device=device)
                fake = G(z).detach()
                eps = torch.rand(B, 1, 1, 1, device=device).expand_as(real)
                x_hat = (eps * real + (1 - eps) * fake).requires_grad_(True)
                d_hat = C(x_hat)
                grads = autograd.grad(d_hat, x_hat, torch.ones_like(d_hat),
                                      create_graph=True, retain_graph=True)[0]
                gp = lam * ((grads.view(B, -1).norm(2, dim=1) - 1) ** 2).mean()
                loss_C = C(fake).mean() - C(real).mean() + gp
                opt_C.zero_grad(); loss_C.backward(); opt_C.step()
            z = torch.randn(B, 100, device=device)
            loss_G = -C(G(z)).mean()
            opt_G.zero_grad(); loss_G.backward(); opt_G.step()
        print(f'Epoch {epoch+1}: L_C={loss_C.item():.4f}  L_G={loss_G.item():.4f}')

print('WGAN-GP: critic updated 5x per generator step, Adam with betas=(0.0, 0.9)')
```

## R1 Gradient Penalty — Simpler Alternative

```python
import torch
import torch.nn as nn
import torch.autograd as autograd

def r1_gradient_penalty(critic, real_samples, gamma=10.0):
    """R1 regularisation: penalise gradient norm at real data only (Mescheder 2018).

    Simpler than WGAN-GP: no interpolation needed, only real samples used.
    Stable for standard GAN (non-saturating) loss with gradient penalty.
    L = E[softplus(-D(real))] + E[softplus(D(fake))] + gamma/2 * E[||grad_D(real)||^2]
    """
    real = real_samples.requires_grad_(True)
    d_real = critic(real)
    grads = autograd.grad(
        outputs=d_real.sum(),
        inputs=real,
        create_graph=True,
        only_inputs=True
    )[0]
    r1_penalty = (gamma / 2.0) * (grads.view(grads.size(0), -1).norm(2, dim=1) ** 2).mean()
    return r1_penalty

class SimpleDiscriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 256), nn.LeakyReLU(0.2),
            nn.Linear(256, 128), nn.LeakyReLU(0.2),
            nn.Linear(128, 1)
        )
    def forward(self, x):
        return self.net(x)

D = SimpleDiscriminator()
real_data = torch.randn(16, 1, 28, 28)
r1 = r1_gradient_penalty(D, real_data, gamma=10.0)
print(f'R1 penalty: {r1.item():.4f}')
print('R1 advantage: no fake-sample interpolation, lower compute, used in StyleGAN2')
```

R1 regularisation differs from WGAN-GP in a key way: it only penalises gradients at real data points, not at interpolated points between real and fake. This makes R1 simpler to implement (no interpolation step) and slightly cheaper (one fewer backward pass). It is used as the default in StyleGAN, StyleGAN2, and StyleGAN-XL. WGAN-GP is preferred when the generator is far from the data distribution (early training) because penalising interpolants provides gradient information in regions between real and fake. For most practical applications where training is well-initialised, R1 is the recommended default.

## WGAN Clipping vs WGAN-GP: Loss Curves

```python
import torch
import torch.nn as nn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run_toy_wgan(use_gp=True, n_steps=300, seed=0):
    torch.manual_seed(seed)
    G = nn.Sequential(nn.Linear(1, 32), nn.ReLU(), nn.Linear(32, 1))
    C = nn.Sequential(nn.Linear(1, 32), nn.LeakyReLU(0.2), nn.Linear(32, 1))
    opt_G = torch.optim.Adam(G.parameters(), lr=1e-3, betas=(0.0, 0.9))
    opt_C = torch.optim.Adam(C.parameters(), lr=1e-3, betas=(0.0, 0.9))
    w_dists = []
    for step in range(n_steps):
        real = torch.randn(64, 1) * 0.5 + 2.0
        for _ in range(5):
            z = torch.randn(64, 1)
            fake = G(z).detach()
            if use_gp:
                eps = torch.rand(64, 1)
                xhat = (eps * real + (1 - eps) * fake).requires_grad_(True)
                d_xhat = C(xhat)
                grads = torch.autograd.grad(d_xhat.sum(), xhat, create_graph=True)[0]
                gp = 10.0 * ((grads.norm(2, dim=1) - 1) ** 2).mean()
                loss_C = C(fake).mean() - C(real).mean() + gp
            else:
                loss_C = C(fake).mean() - C(real).mean()
            opt_C.zero_grad(); loss_C.backward(); opt_C.step()
            if not use_gp:
                for p in C.parameters():
                    p.data.clamp_(-0.01, 0.01)
        z = torch.randn(64, 1)
        loss_G = -C(G(z)).mean()
        opt_G.zero_grad(); loss_G.backward(); opt_G.step()
        if step % 10 == 0:
            with torch.no_grad():
                w_dists.append(abs(loss_C.item()))
    return w_dists

gp_curve   = run_toy_wgan(use_gp=True)
clip_curve = run_toy_wgan(use_gp=False)
print(f'WGAN-GP   final W-dist proxy: {gp_curve[-1]:.4f}')
print(f'WGAN-clip final W-dist proxy: {clip_curve[-1]:.4f}')
print('WGAN-GP converges more smoothly; clipping causes oscillation/slow convergence')
```

## Removing BatchNorm from the Critic

BatchNorm normalises activations across the batch, making each sample's gradient depend on every other sample in the batch. This violates the per-sample Lipschitz constraint that WGAN-GP enforces — the gradient penalty targets the gradient at individual interpolated points, but BatchNorm coupling means the gradient depends on what other samples are in the batch. The fix is simple: replace BatchNorm in the critic with LayerNorm (normalises per sample across channels) or InstanceNorm (normalises per sample per channel), or omit normalisation entirely in the critic. The generator can still use BatchNorm normally.

> **BatchNorm Breaks Gradient Penalty**: Never use BatchNorm in the WGAN-GP critic. The per-sample gradient at x_hat must be independent of other batch members, but BatchNorm normalises across the batch, coupling all gradients. Use LayerNorm, InstanceNorm, or no normalisation in the critic. The generator is unaffected and can use BatchNorm as usual.

## Hyperparameters and Practical Tips

The standard WGAN-GP recipe from Gulrajani et al. is: λ = 10, n_critic = 5 (critic steps per generator step), Adam with lr = 1e-4 and betas = (0.0, 0.9). The zero first moment (β₁ = 0) is important — momentum can destabilise Wasserstein training. The critic is trained to convergence before each generator update, approximated by n_critic steps. Increasing n_critic improves critic quality but slows training. The gradient penalty adds one additional backward pass per critic step (through create_graph=True) which roughly doubles critic computation. On conditional GANs, WGAN-GP is the standard choice because it allows arbitrary critic architectures without normalisation constraints.

| Method | Lipschitz Enforcement | BatchNorm in Critic | Stability | Compute Overhead | FID (typical) |
| --- | --- | --- | --- | --- | --- |
| Standard GAN | None (JS divergence) | Allowed | Low — mode collapse, vanishing grads | None | Varies widely |
| WGAN (clipping) | Weight clipping to [-c, c] | Not recommended | Moderate — biases toward simple functions | Minimal | Better than GAN |
| WGAN-GP | Gradient penalty on interpolants | Not allowed (use LayerNorm) | High — stable across architectures | ~2x critic backward | Strong baseline |
| R1-GAN | Gradient penalty at real data only | Allowed in generator | High — simpler, less compute | ~1.5x critic backward | Comparable to WGAN-GP |
| SN-GAN | Spectral norm on all critic weights | Allowed | High — no extra backward pass | Minimal (SVD per layer) | Competitive FID |

- Use torch.autograd.grad with create_graph=True to compute the gradient penalty — standard backward() cannot be used because you need gradients of gradients.
- lambda=10 is robust across image resolutions; tuning is rarely needed. Lower lambda (~1) may help if the penalty dominates early training.
- R1 regularisation (penalise gradient at real data only) is simpler, computationally cheaper, and used in StyleGAN2 — prefer it for new projects.
- WGAN-GP critic loss should decrease and eventually plateau near a small positive value — if it oscillates or grows, reduce the learning rate.
- The Wasserstein distance estimate (negative critic loss) is a meaningful training signal: decreasing W-distance corresponds to improving generation quality.
- Monitor gradient norms at interpolated points: they should hover near 1 after a few hundred training steps if the penalty is working correctly.

---

