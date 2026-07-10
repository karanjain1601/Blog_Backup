---
title: "IA3 — Learned Rescaling of Keys, Values, and FFN Activations"
slug: "ia3"
description: "IA3 (Liu et al., 2022) multiplies attention keys, values, and FFN intermediate activations by learned vectors — multiplicative rather than additive adaptation. Covers the three insertion points, trainable parameter count (~483K for LLaMA-7B), identity init, weight merging, and few-shot performance vs LoRA and adapters."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSUEzIChJbmZ1c2VkIEFkYXB0ZXIgYnkgSW5oaWJpdGluZyBhbmQgQW1wbGlmeWluZyBJbm5lciBBY3RpdmF0aW9ucywgTGl1IGV0IGFsLiwgMjAyMikgaXMgYSBwYXJhbWV0ZXItZWZmaWNpZW50IGZpbmUtdHVuaW5nIG1ldGhvZCB0aGF0IHNjYWxlcyBleGlzdGluZyBhY3RpdmF0aW9ucyBieSBsZWFybmVkIHZlY3RvcnMgcmF0aGVyIHRoYW4gYWRkaW5nIG5ldyBhY3RpdmF0aW9ucyBvciB3ZWlnaHQgb2Zmc2V0cy4gSW5zdGVhZCBvZiBpbnNlcnRpbmcgYm90dGxlbmVjayBsYXllcnMgb3IgZGVjb21wb3Npbmcgd2VpZ2h0IG1hdHJpY2VzLCBJQTMgcGxhY2VzIGVsZW1lbnQtd2lzZSBtdWx0aXBsaWNhdGlvbiBieSBhIGxlYXJuZWQgdmVjdG9yIGF0IHRocmVlIHN0cmF0ZWdpYyBwb2ludHMgaW4gZWFjaCB0cmFuc2Zvcm1lciBsYXllci4gVGhpcyBtdWx0aXBsaWNhdGl2ZSBkZXNpZ24gZ2l2ZXMgSUEzIGFuIGV4dHJlbWVseSBsb3cgcGFyYW1ldGVyIGNvdW50IHdoaWxlIHJldGFpbmluZyB0aGUgYWJpbGl0eSB0byBzZWxlY3RpdmVseSBhbXBsaWZ5IG9yIHN1cHByZXNzIHNwZWNpZmljIGFjdGl2YXRpb24gZGltZW5zaW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaHJlZSBJbnNlcnRpb24gUG9pbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJQTMgaW50cm9kdWNlcyB0aHJlZSBsZWFybmVkIHNjYWxlIHZlY3RvcnMgcGVyIHRyYW5zZm9ybWVyIGxheWVyOiAoMSkgbF9rIOKIiCDihJ1eKGRfaykgc2NhbGVzIHRoZSBhdHRlbnRpb24ga2V5czogSyDihpAgbF9rIOKKmSBLLCB3aGVyZSDiipkgaXMgZWxlbWVudC13aXNlIG11bHRpcGxpY2F0aW9uLiBUaGlzIG1vZHVsYXRlcyB3aGljaCBrZXkgZGltZW5zaW9ucyBhcmUgYW1wbGlmaWVkIG9yIHN1cHByZXNzZWQgZHVyaW5nIGF0dGVudGlvbiBzY29yZSBjb21wdXRhdGlvbi4gKDIpIGxfdiDiiIgg4oSdXihkX3YpIHNjYWxlcyB0aGUgYXR0ZW50aW9uIHZhbHVlczogViDihpAgbF92IOKKmSBWLiBUaGlzIGNvbnRyb2xzIHdoaWNoIHZhbHVlIGRpbWVuc2lvbnMgYXJlIHBhc3NlZCB0aHJvdWdoIHRvIHRoZSBvdXRwdXQuICgzKSBsX2ZmIOKIiCDihJ1eKGRfZmYpIHNjYWxlcyB0aGUgaW50ZXJtZWRpYXRlIEZGTiBhY3RpdmF0aW9uIChhZnRlciB0aGUgZmlyc3QgbGluZWFyICsgYWN0aXZhdGlvbik6IHgg4oaQIGxfZmYg4oqZIM+DKFdfMSB4KS4gQWxsIG90aGVyIGFjdGl2YXRpb25zIGFuZCBhbGwgd2VpZ2h0IG1hdHJpY2VzIHJlbWFpbiB1bmNoYW5nZWQuIEFsbCBzY2FsZSB2ZWN0b3JzIGFyZSBpbml0aWFsaXplZCB0byBvbmVzLCBlbnN1cmluZyBpZGVudGl0eSBiZWhhdmlvciBhdCB0aGUgc3RhcnQgb2YgdHJhaW5pbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQYXJhbWV0ZXIgY291bnQgZm9yIExMYU1BLTdCOiB3aXRoIDMyIGF0dGVudGlvbiBoZWFkcyBvZiBkaW1lbnNpb24gNjQsIGRfa190b3RhbCA9IGRfdl90b3RhbCA9IDMyw5c2NCA9IDIwNDguIEZGTiBpbnRlcm1lZGlhdGUgZF9mZiA9IDExMDA4LiBQZXIgbGF5ZXI6IDIwNDggKyAyMDQ4ICsgMTEwMDggPSAxNTEwNCBzY2FsYXJzLiBXaXRoIDMyIGxheWVyczogMzLDlzE1MTA0ID0gNDgzLDMyOCDiiYggMC40OE0gcGFyYW1ldGVycy4gVGhpcyBpcyByb3VnaGx5IDEwMMOXIGZld2VyIHBhcmFtZXRlcnMgdGhhbiBMb1JBIHdpdGggcj04IG9uIHRoZSBzYW1lIG1vZGVsICh3aGljaCBoYXMgYXBwcm94aW1hdGVseSA1ME0gdHJhaW5hYmxlIHBhcmFtcyBhY3Jvc3MgYWxsIFEsIEssIFYsIE8gcHJvamVjdGlvbnMpLiBBdCAxNi1iaXQgcHJlY2lzaW9uLCB0aGUgSUEzIHBhcmFtZXRlcnMgb2NjdXB5IGxlc3MgdGhhbiAxTUIgb2Ygc3RvcmFnZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJQTMgQXR0ZW50aW9uIEltcGxlbWVudGF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIElBM0F0dGVudGlvbihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlxuICAgIE11bHRpLWhlYWQgYXR0ZW50aW9uIHdpdGggSUEzIHNjYWxpbmcgb24ga2V5cyBhbmQgdmFsdWVzLlxuICAgIEJhY2tib25lIFEsIEssIFYgcHJvamVjdGlvbnMgYXJlIGZyb3plbjsgb25seSBsX2ssIGxfdiBhcmUgdHJhaW5lZC5cbiAgICBcIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsOiBpbnQsIG5faGVhZHM6IGludCwgZnJlZXplX2JhY2tib25lOiBib29sID0gVHJ1ZSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBhc3NlcnQgZF9tb2RlbCAlIG5faGVhZHMgPT0gMFxuICAgICAgICBzZWxmLm5faGVhZHMgPSBuX2hlYWRzXG4gICAgICAgIHNlbGYuaGVhZF9kaW0gPSBkX21vZGVsIC8vIG5faGVhZHNcbiAgICAgICAgc2VsZi5zY2FsZSA9IHNlbGYuaGVhZF9kaW0gKiogLTAuNVxuICAgICAgICBzZWxmLnFfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmtfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLnZfcHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLm91dF9wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIGlmIGZyZWV6ZV9iYWNrYm9uZTpcbiAgICAgICAgICAgIGZvciBtb2R1bGUgaW4gW3NlbGYucV9wcm9qLCBzZWxmLmtfcHJvaiwgc2VsZi52X3Byb2osIHNlbGYub3V0X3Byb2pdOlxuICAgICAgICAgICAgICAgIGZvciBwYXJhbSBpbiBtb2R1bGUucGFyYW1ldGVycygpOlxuICAgICAgICAgICAgICAgICAgICBwYXJhbS5yZXF1aXJlc19ncmFkID0gRmFsc2VcbiAgICAgICAgIyBJQTMgbGVhcm5lZCBzY2FsZXMgLS0gaW5pdCB0byAxIChpZGVudGl0eSBhdCBzdGFydClcbiAgICAgICAgc2VsZi5sX2sgPSBubi5QYXJhbWV0ZXIodG9yY2gub25lcyhkX21vZGVsKSlcbiAgICAgICAgc2VsZi5sX3YgPSBubi5QYXJhbWV0ZXIodG9yY2gub25lcyhkX21vZGVsKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIGJzeiwgc2VxLCBkID0geC5zaGFwZVxuICAgICAgICBRID0gc2VsZi5xX3Byb2ooeCkgICAgICAgICAgICAgICAgICMgbm8gc2NhbGluZyBvbiBRXG4gICAgICAgIEsgPSBzZWxmLmtfcHJvaih4KSAqIHNlbGYubF9rICAgICAjIElBMyBzY2FsZSBrZXlzXG4gICAgICAgIFYgPSBzZWxmLnZfcHJvaih4KSAqIHNlbGYubF92ICAgICAjIElBMyBzY2FsZSB2YWx1ZXNcbiAgICAgICAgZGVmIHNwbGl0KHQpOiByZXR1cm4gdC52aWV3KGJzeiwgc2VxLCBzZWxmLm5faGVhZHMsIHNlbGYuaGVhZF9kaW0pLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICBRLCBLLCBWID0gc3BsaXQoUSksIHNwbGl0KEspLCBzcGxpdChWKVxuICAgICAgICBhdHRuID0gRi5zb2Z0bWF4KChRIEAgSy50cmFuc3Bvc2UoLTIsIC0xKSkgKiBzZWxmLnNjYWxlLCBkaW09LTEpXG4gICAgICAgIG91dCA9IChhdHRuIEAgVikudHJhbnNwb3NlKDEsIDIpLmNvbnRpZ3VvdXMoKS52aWV3KGJzeiwgc2VxLCBkKVxuICAgICAgICByZXR1cm4gc2VsZi5vdXRfcHJvaihvdXQpXG5cbmF0dG4gPSBJQTNBdHRlbnRpb24oNTEyLCA4KVxudHJhaW5hYmxlID0gWyhuLCBwLnNoYXBlKSBmb3IgbiwgcCBpbiBhdHRuLm5hbWVkX3BhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWRdXG5wcmludChmXHUwMDI3VHJhaW5hYmxlIHBhcmFtczoge3RyYWluYWJsZX1cdTAwMjcpICAjIG9ubHkgbF9rLCBsX3YifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJQTMgRkZOIGFuZCBQYXJhbWV0ZXIgQ291bnQifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgSUEzRkZOKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiXG4gICAgRmVlZC1mb3J3YXJkIG5ldHdvcmsgd2l0aCBJQTMgc2NhbGluZyBvbiBpbnRlcm1lZGlhdGUgYWN0aXZhdGlvbi5cbiAgICBsX2ZmIHNjYWxlcyB0aGUgb3V0cHV0IG9mIHRoZSBmaXJzdCBsaW5lYXIgKyBhY3RpdmF0aW9uLlxuICAgIFwiXCJcIlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRfbW9kZWw6IGludCwgZF9mZjogaW50LCBmcmVlemVfYmFja2JvbmU6IGJvb2wgPSBUcnVlKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubGluZWFyMSA9IG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKVxuICAgICAgICBzZWxmLmxpbmVhcjIgPSBubi5MaW5lYXIoZF9mZiwgZF9tb2RlbClcbiAgICAgICAgc2VsZi5hY3QgPSBubi5HRUxVKClcbiAgICAgICAgaWYgZnJlZXplX2JhY2tib25lOlxuICAgICAgICAgICAgZm9yIHAgaW4gc2VsZi5wYXJhbWV0ZXJzKCk6XG4gICAgICAgICAgICAgICAgcC5yZXF1aXJlc19ncmFkID0gRmFsc2VcbiAgICAgICAgc2VsZi5sX2ZmID0gbm4uUGFyYW1ldGVyKHRvcmNoLm9uZXMoZF9mZikpICAjIGluaXQ9MSAoaWRlbnRpdHkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBoID0gc2VsZi5hY3Qoc2VsZi5saW5lYXIxKHgpKSAgIyAoYnN6LCBzZXEsIGRfZmYpXG4gICAgICAgIGggPSBoICogc2VsZi5sX2ZmICAgICAgICAgICAgICMgSUEzIHNjYWxlXG4gICAgICAgIHJldHVybiBzZWxmLmxpbmVhcjIoaClcblxuIyBQYXJhbWV0ZXIgY291bnQgYWNyb3NzIG1vZGVsIHNpemVzXG5jb25maWdzID0gW1xuICAgIChcdTAwMjdCRVJULWJhc2VcdTAwMjcsICA3NjgsICAzMDcyLCAxMiksXG4gICAgKFx1MDAyN1Q1LUxhcmdlXHUwMDI3LCAgMTAyNCwgIDQwOTYsIDI0KSxcbiAgICAoXHUwMDI3TExhTUEtN0JcdTAwMjcsICA0MDk2LCAxMTAwOCwgMzIpLFxuICAgIChcdTAwMjdMTGFNQS0xM0JcdTAwMjcsIDUxMjAsIDEzODI0LCA0MCksXG5dXG5wcmludChmXHUwMDI3e1wiTW9kZWxcIjpcdTAwM2MxNH0ge1wiZF9tb2RlbFwiOlx1MDAzZTh9IHtcImRfZmZcIjpcdTAwM2U3fSB7XCJMYXllcnNcIjpcdTAwM2U3fSB7XCJJQTMgUGFyYW1zXCI6XHUwMDNlMTJ9XHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDU1KVxuZm9yIG5hbWUsIGQsIGRmZiwgTCBpbiBjb25maWdzOlxuICAgIHBlcl9sYXllciA9IGQgKyBkICsgZGZmICAjIGxfayArIGxfdiArIGxfZmZcbiAgICB0b3RhbCA9IHBlcl9sYXllciAqIExcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMTR9IHtkOlx1MDAzZTh9IHtkZmY6XHUwMDNlN30ge0w6XHUwMDNlN30ge3RvdGFsOlx1MDAzZTEyLH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2VpZ2h0IE1lcmdpbmcgYXQgSW5mZXJlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJQTMgc2NhbGluZyB2ZWN0b3JzIGNhbiBiZSBmb2xkZWQgaW50byB0aGUgdW5kZXJseWluZyB3ZWlnaHQgbWF0cmljZXMgYmVmb3JlIGRlcGxveW1lbnQsIGVsaW1pbmF0aW5nIGFueSBpbmZlcmVuY2Ugb3ZlcmhlYWQuIFRoZSBrZXkgaW5zaWdodDogbXVsdGlwbHlpbmcgYWN0aXZhdGlvbnMgYnkgYSBsZWFybmVkIHZlY3RvciBpcyBlcXVpdmFsZW50IHRvIHNjYWxpbmcgdGhlIGNvcnJlc3BvbmRpbmcgcm93cyBvZiB0aGUgcHJvamVjdGlvbiBtYXRyaXggdGhhdCBwcm9kdWNlcyB0aG9zZSBhY3RpdmF0aW9ucy4gU3BlY2lmaWNhbGx5OiBLIOKGkCBsX2sg4oqZIFdfSyB4IGlzIGVxdWl2YWxlbnQgdG8gSyDihpAgKGRpYWcobF9rKSBXX0spIHguIFNvIFdfS19tZXJnZWQgPSBkaWFnKGxfaykgQCBXX0ssIGkuZS4sIG11bHRpcGx5IGVhY2ggcm93IGkgb2YgV19LIGJ5IGxfa1tpXS4gU2ltaWxhcmx5IGZvciBXX1YuIEZvciBsX2ZmIHNjYWxpbmcgdGhlIEZGTiBpbnRlcm1lZGlhdGUsIGl0IGlzIGVxdWl2YWxlbnQgdG8gc2NhbGluZyB0aGUgcm93cyBvZiBXXzIgKHRoZSBzZWNvbmQgbGluZWFyKTogV18yX21lcmdlZFtpLCA6XSA9IGxfZmZbaV0gw5cgV18yW2ksIDpdLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgbWVyZ2VfaWEzX2ludG9fd2VpZ2h0cyhrX3Byb2pfd2VpZ2h0OiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2X3Byb2pfd2VpZ2h0OiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBmZm4yX3dlaWdodDogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgbF9rOiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBsX3Y6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIGxfZmY6IHRvcmNoLlRlbnNvcik6XG4gICAgXCJcIlwiXG4gICAgRm9sZCBJQTMgc2NhbGluZyB2ZWN0b3JzIGludG8gcHJvamVjdGlvbiB3ZWlnaHQgbWF0cmljZXMuXG4gICAgQWZ0ZXIgbWVyZ2luZywgbW9kZWwgdXNlcyBzdGFuZGFyZCBsaW5lYXIgbGF5ZXJzIHdpdGggbm8gaW5mZXJlbmNlIG92ZXJoZWFkLlxuICAgIEtfbWVyZ2VkW2ksIDpdID0gbF9rW2ldICoga19wcm9qX3dlaWdodFtpLCA6XVxuICAgIFZfbWVyZ2VkW2ksIDpdID0gbF92W2ldICogdl9wcm9qX3dlaWdodFtpLCA6XVxuICAgIEZGTjJfbWVyZ2VkW2ksIDpdID0gbF9mZltpXSAqIGZmbjJfd2VpZ2h0W2ksIDpdICAgKGxpbmVhcjIgcm93cylcbiAgICBcIlwiXCJcbiAgICAjIFNjYWxlIG91dHB1dCByb3dzIG9mIEsgYW5kIFYgcHJvamVjdGlvbiB3ZWlnaHRzXG4gICAgS19tZXJnZWQgICA9IGtfcHJval93ZWlnaHQgKiBsX2sudW5zcXVlZXplKDEpICAgICMgKGRfbW9kZWwsIGRfbW9kZWwpXG4gICAgVl9tZXJnZWQgICA9IHZfcHJval93ZWlnaHQgKiBsX3YudW5zcXVlZXplKDEpICAgICMgKGRfbW9kZWwsIGRfbW9kZWwpXG4gICAgRkZOMl9tZXJnZWQgPSBmZm4yX3dlaWdodCAgKiBsX2ZmLnVuc3F1ZWV6ZSgxKSAgICMgKGRfbW9kZWwsIGRfZmYpXG4gICAgcHJpbnQoZlx1MDAyN0sgZGlmZiB2cyBvcmlnaW5hbDogeyhLX21lcmdlZCAtIGtfcHJval93ZWlnaHQpLmFicygpLm1lYW4oKTouNGZ9XHUwMDI3KVxuICAgIHJldHVybiBLX21lcmdlZCwgVl9tZXJnZWQsIEZGTjJfbWVyZ2VkXG5cbmRfbW9kZWwsIGRfZmYgPSA1MTIsIDIwNDhcbmtfdyA9IHRvcmNoLnJhbmRuKGRfbW9kZWwsIGRfbW9kZWwpXG52X3cgPSB0b3JjaC5yYW5kbihkX21vZGVsLCBkX21vZGVsKVxuZmZuMl93ID0gdG9yY2gucmFuZG4oZF9tb2RlbCwgZF9mZilcbmxfayAgPSB0b3JjaC5vbmVzKGRfbW9kZWwpICsgMC4xICogdG9yY2gucmFuZG4oZF9tb2RlbClcbmxfdiAgPSB0b3JjaC5vbmVzKGRfbW9kZWwpICsgMC4xICogdG9yY2gucmFuZG4oZF9tb2RlbClcbmxfZmYgPSB0b3JjaC5vbmVzKGRfZmYpICsgMC4xICogdG9yY2gucmFuZG4oZF9mZilcbktfbSwgVl9tLCBGRk5fbSA9IG1lcmdlX2lhM19pbnRvX3dlaWdodHMoa193LCB2X3csIGZmbjJfdywgbF9rLCBsX3YsIGxfZmYpXG5wcmludChmXHUwMDI3TWVyZ2VkIHNoYXBlczogSz17S19tLnNoYXBlfSwgVj17Vl9tLnNoYXBlfSwgRkZOMj17RkZOX20uc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZldy1TaG90IExlYXJuaW5nIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IklBMyB3YXMgZGVzaWduZWQgc3BlY2lmaWNhbGx5IGZvciBmZXctc2hvdCBmaW5lLXR1bmluZyBpbiB0aGUgVC1GZXcgcGFwZXIgKExpdSBldCBhbC4sIDIwMjIpLiBUaGUga2V5IGludHVpdGlvbjogd2l0aCB2ZXJ5IGZldyBsYWJlbGVkIGV4YW1wbGVzICgxMOKAkzUwKSwgbWV0aG9kcyB3aXRoIG1vcmUgdHJhaW5hYmxlIHBhcmFtZXRlcnMgb3ZlcmZpdCBtb3JlIGVhc2lseS4gSUEzXHUwMDI3cyDiiYg0ODBLIHBhcmFtZXRlcnMgZm9yIGEgN0IgbW9kZWwgcHJvdmlkZXMgYSBtdWNoIGxvd2VyLWNhcGFjaXR5IGxlYXJuZXIgdGhhbiBMb1JBXHUwMDI3cyDiiYg1ME0sIHJlZHVjaW5nIHRoZSByaXNrIG9mIG1lbW9yaXppbmcgdGhlIGZldyB0cmFpbmluZyBleGFtcGxlcyByYXRoZXIgdGhhbiBsZWFybmluZyBnZW5lcmFsaXphYmxlIHBhdHRlcm5zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBBcHByb3hpbWF0ZSBhY2N1cmFjeSBmcm9tIFQtRmV3IHBhcGVyIChMaXUgZXQgYWwuIDIwMjIpXG4jIFQ1LUxhcmdlICg3NzBNKSBiYWNrYm9uZSwgYXZlcmFnZWQgb3ZlciBTdXBlckdMVUUtc3R5bGUgdGFza3NcbnNob3RfY291bnRzID0gWzEwLCA1MCwgMTAwLCA1MDBdXG5pYTNfYWNjICAgICA9IFs2Ny4zLCA3NC44LCA3OC4yLCA4Mi4xXVxubG9yYV9hY2MgICAgPSBbNjMuMSwgNzIuNCwgNzcuMSwgODIuNV0gICMgTG9SQSByPThcbmFkYXB0ZXJfYWNjID0gWzYxLjQsIDcxLjgsIDc2LjgsIDgyLjBdICAjIFBmZWlmZmVyIGFkYXB0ZXJzIG09NjRcbmZ1bGxfZnRfYWNjID0gWzU4LjIsIDcwLjEsIDc2LjMsIDgzLjBdICAjIHByb25lIHRvIG92ZXJmaXR0aW5nIGF0IGxvdyBzaG90XG5cbnByaW50KGZcdTAwMjd7XCJTaG90c1wiOlx1MDAzZTh9IHwge1wiSUEzXCI6XHUwMDNlOH0gfCB7XCJMb1JBIHI9OFwiOlx1MDAzZTEwfSB8IHtcIkFkYXB0ZXJzXCI6XHUwMDNlMTB9IHwge1wiRnVsbCBGVFwiOlx1MDAzZTl9XHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDU1KVxuZm9yIHMsIGlhLCBsbywgYWQsIGZmdCBpbiB6aXAoc2hvdF9jb3VudHMsIGlhM19hY2MsIGxvcmFfYWNjLCBhZGFwdGVyX2FjYywgZnVsbF9mdF9hY2MpOlxuICAgIHByaW50KGZcdTAwMjd7czpcdTAwM2U4fSB8IHtpYTpcdTAwM2U4LjFmfSB8IHtsbzpcdTAwM2UxMC4xZn0gfCB7YWQ6XHUwMDNlMTAuMWZ9IHwge2ZmdDpcdTAwM2U5LjFmfVx1MDAyNylcblxucHJpbnQoKVxucHJpbnQoXHUwMDI3SUEzIGFkdmFudGFnZSBpcyBsYXJnZXN0IGF0IGxvdyBzaG90IGNvdW50cyAoMTAtNTApOlx1MDAyNylcbmZvciBzLCBpYSwgbG8gaW4gemlwKHNob3RfY291bnRzWzoyXSwgaWEzX2FjY1s6Ml0sIGxvcmFfYWNjWzoyXSk6XG4gICAgcHJpbnQoZlx1MDAyNyAge3N9LXNob3Q6IElBMyB7aWE6LjFmfSB2cyBMb1JBIHtsbzouMWZ9ICgre2lhLWxvOi4xZn0pXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IklBMyB2cyBPdGhlciBQRUZUIE1ldGhvZHMifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiVHJhaW5hYmxlIFBhcmFtcyAoN0IpIiwiSW5zZXJ0aW9uIFR5cGUiLCJNdWx0aXBsaWNhdGl2ZS9BZGRpdGl2ZSIsIk1lcmdlIGF0IEluZmVyZW5jZSIsIkZldy1TaG90IFN1aXRhYmlsaXR5Il0sInJvd3MiOltbIklBMyIsIn40ODNLICgzIHZlY3RvcnMvbGF5ZXIpIiwiSywgViwgRkZOIGludGVybWVkaWF0ZSBzY2FsaW5nIiwiTXVsdGlwbGljYXRpdmUiLCJZZXMg4oCUIGZvbGQgbCBpbnRvIHdlaWdodCByb3dzIiwiRXhjZWxsZW50IOKAlCBsb3dlc3Qgb3ZlcmZpdCByaXNrIl0sWyJMb1JBIChyPTgpIiwifjUwTSAoMiBtYXRyaWNlcy9sYXllcikiLCJXICs9IEJBIChsb3ctcmFuayBhZGRpdGl2ZSkiLCJBZGRpdGl2ZSIsIlllcyDigJQgV19tZXJnZWQgPSBXICsgQkEiLCJHb29kIOKAlCBtb2RlcmF0ZSBwYXJhbXMiXSxbIlZlUkEiLCJ+NjVLIChzaGFyZWQgcmFuZG9tIEIsIEEpIiwiVyArPSDOu19iIGRpYWcoYikgQiBkaWFnKGEpIEEiLCJBZGRpdGl2ZSB3aXRoIHNjYWxpbmciLCJZZXMg4oCUIG1lcmdlIGxpa2UgTG9SQSIsIlZlcnkgZ29vZCDigJQgdmVyeSBmZXcgcGFyYW1zIl0sWyJBZGFwdGVyIChQZmVpZmZlcikiLCJ+MjAwTSAoYm90dGxlbmVjayBGRk4pIiwiU2VyaWFsIEZGTiBhZnRlciBlYWNoIHN1Yi1sYXllciIsIkFkZGl0aXZlIiwiTm8g4oCUIGFkZHMgZXh0cmEgY29tcHV0ZSBwYXRoIiwiTW9kZXJhdGUg4oCUIG1vcmUgcGFyYW1zIHRvIG92ZXJmaXQiXSxbIlByb21wdCBUdW5pbmciLCJ+MTAwSyAoaW5wdXQgcHJlZml4IG9ubHkpIiwiSW5wdXQgZW1iZWRkaW5nIHByZWZpeCIsIk5laXRoZXIgKGlucHV0IG1vZGlmaWNhdGlvbikiLCJOL0Eg4oCUIHByZWZpeCBhbHdheXMgcHJlc2VudCIsIlBvb3IgYXQgXHUwMDNjMTBCIHNjYWxlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJULUZldzogSUEzIHdpdGggVGFzay1TcGVjaWZpYyBQcmV0cmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFQtRmV3IHBhcGVyIChMaXUgZXQgYWwuLCAyMDIyKSBkZW1vbnN0cmF0ZXMgdGhhdCBJQTMgY29tYmluZWQgd2l0aCBtdWx0aXRhc2sgcHJldHJhaW5pbmcgKFQwIG1vZGVsKSBhY2hpZXZlcyBzdGF0ZS1vZi10aGUtYXJ0IGZldy1zaG90IHBlcmZvcm1hbmNlIHdpdGggZmFyIGZld2VyIHRyYWluYWJsZSBwYXJhbWV0ZXJzIHRoYW4gR1BULTMgKDE3NUIpIGRlc3BpdGUgdXNpbmcgVDUtTGFyZ2UgKDc3ME0pLiBUaGUgVC1GZXcgcmVjaXBlOiAoMSkgc3RhcnQgZnJvbSBUMCwgYSBUNS1MYXJnZSBwcmV0cmFpbmVkIG9uIDM1IE5MUCBkYXRhc2V0cyB3aXRoIG5hdHVyYWwgbGFuZ3VhZ2UgcHJvbXB0czsgKDIpIGFwcGx5IElBMyBhbmQgdHJhaW4gb24gSyBleGFtcGxlcyBwZXIgdGFzazsgKDMpIHVzZSB1bmxpa2VsaWhvb2QgdHJhaW5pbmcgdG8gaW1wcm92ZSBjYWxpYnJhdGlvbi4gQXQgMTAtc2hvdCwgVC1GZXcgKDc3ME0gcGFyYW1zLCA0ODNLIElBMyBwYXJhbXMgZmluZS10dW5lZCkgb3V0cGVyZm9ybXMgR1BULTMgKDE3NUIsIHplcm8tc2hvdCkgb24gOSBvZiAxMSBiZW5jaG1hcmtzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVzaW5nIElBMyB3aXRoIHRoZSBQRUZUIExpYnJhcnkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBIdWdnaW5nRmFjZSBQRUZUIGxpYnJhcnkgcHJvdmlkZXMgbmF0aXZlIElBMyBzdXBwb3J0IHZpYSBJQTNDb25maWcuIFRoZSBrZXkgcGFyYW1ldGVycyBhcmUgdGFyZ2V0X21vZHVsZXMgKHdoaWNoIHByb2plY3Rpb24gbWF0cmljZXMgdG8gYXBwbHkgbF9rIGFuZCBsX3YgdG8sIHR5cGljYWxseSBbXHUwMDI3a19wcm9qXHUwMDI3LCBcdTAwMjd2X3Byb2pcdTAwMjddKSBhbmQgZmVlZGZvcndhcmRfbW9kdWxlcyAod2hpY2ggRkZOIGxheWVycyB0byBhcHBseSBsX2ZmIHRvLCB0eXBpY2FsbHkgW1x1MDAyN2Rvd25fcHJvalx1MDAyN10gZm9yIExMYU1BLXN0eWxlIG1vZGVscyBvciBbXHUwMDI3ZmMyXHUwMDI3XSBmb3IgQkVSVC1zdHlsZSkuIEFmdGVyIHRyYWluaW5nLCBjYWxsIG1vZGVsLm1lcmdlX2FkYXB0ZXIoKSB0byBmb2xkIHRoZSBzY2FsZSB2ZWN0b3JzIGludG8gdGhlIGJhc2Ugd2VpZ2h0cyBmb3IgemVyby1vdmVyaGVhZCBpbmZlcmVuY2UuIFRoZSBtZXJnZWQgbW9kZWwgaXMgaW5kaXN0aW5ndWlzaGFibGUgZnJvbSBhIHN0YW5kYXJkIG1vZGVsIGFuZCBjYW4gYmUgc2VydmVkIHdpdGhvdXQgdGhlIFBFRlQgbGlicmFyeS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6Ik11bHRpcGxpY2F0aXZlIHZzIEFkZGl0aXZlIiwiY29udGVudCI6IklBM1x1MDAyN3MgbXVsdGlwbGljYXRpdmUgc2NhbGluZyBwcmVzZXJ2ZXMgdGhlIHN1YnNwYWNlIHN0cnVjdHVyZSBvZiBwcmV0cmFpbmVkIGFjdGl2YXRpb25zIOKAlCB1bmxpa2UgYWRkaXRpdmUgYWRhcHRlcnMgKExvUkEsIGFkYXB0ZXJzKSwgSUEzIGNhbiBvbmx5IHNjYWxlIGV4aXN0aW5nIGZlYXR1cmVzLCBub3QgY3JlYXRlIG5ldyBvbmVzLiBUaGlzIG1ha2VzIGl0IGlkZWFsIGZvciB0YXNrLXNwZWNpZmljIGVtcGhhc2lzIGJ1dCB3ZWFrZXIgZm9yIHN0cnVjdHVyYWwgYWRhcHRhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgUmVjb21tZW5kYXRpb25zIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJJQTMgaW5pdDogbF9rID0gbF92ID0gbF9mZiA9IDEgKG9uZXMgdmVjdG9yKSDigJQgZW5zdXJlcyBpZGVudGl0eSBtYXBwaW5nIGF0IHRoZSBzdGFydCBvZiB0cmFpbmluZy4iLCJQYXJhbWV0ZXIgY291bnQ6IH4zNjDigJM0ODBLIGZvciA3QiBtb2RlbHMg4oCUIHJvdWdobHkgMTAww5cgZmV3ZXIgdGhhbiBMb1JBIHI9OC4iLCJXZWlnaHQgbWVyZ2luZzogZm9sZCBsX2sgaW50byBLIHByb2plY3Rpb24gcm93cywgbF92IGludG8gViBwcm9qZWN0aW9uIHJvd3MsIGxfZmYgaW50byBsaW5lYXIyIHJvd3MgYXQgaW5mZXJlbmNlLiIsIkZldy1zaG90IHJlZ2ltZTogSUEzIG91dHBlcmZvcm1zIExvUkEgYW5kIGFkYXB0ZXJzIGF0IDEw4oCTNTAgc2hvdHMgZHVlIHRvIGxvd2VyIHBhcmFtZXRlciBjb3VudCByZWR1Y2luZyBvdmVyZml0dGluZy4iLCJJQTMgY2Fubm90IGludHJvZHVjZSBuZXcgZmVhdHVyZSBkaXJlY3Rpb25zIOKAlCBpZiB0aGUgdGFzayByZXF1aXJlcyBuZXcgcmVwcmVzZW50YXRpb25zLCBMb1JBIG9yIGFkYXB0ZXJzIGFyZSBwcmVmZXJhYmxlLiIsIlVzZSBwZWZ0IGxpYnJhcnk6IElBM0NvbmZpZyB3aXRoIHRhcmdldF9tb2R1bGVzPVtcdTAwMjdrX3Byb2pcdTAwMjcsXHUwMDI3dl9wcm9qXHUwMDI3XSBhbmQgZmVlZGZvcndhcmRfbW9kdWxlcz1bXHUwMDI3ZG93bl9wcm9qXHUwMDI3XS4iLCJGb3IgaW5zdHJ1Y3Rpb24tZm9sbG93aW5nIGZpbmUtdHVuaW5nIGF0IDEwQisgc2NhbGUsIElBMyBpcyBjb21wZXRpdGl2ZSB3aXRoIExvUkEgYXQgMTAww5cgZmV3ZXIgcGFyYW1ldGVycy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# IA3 — Learned Rescaling of Keys, Values, and FFN Activations

IA3 (Infused Adapter by Inhibiting and Amplifying Inner Activations, Liu et al., 2022) is a parameter-efficient fine-tuning method that scales existing activations by learned vectors rather than adding new activations or weight offsets. Instead of inserting bottleneck layers or decomposing weight matrices, IA3 places element-wise multiplication by a learned vector at three strategic points in each transformer layer. This multiplicative design gives IA3 an extremely low parameter count while retaining the ability to selectively amplify or suppress specific activation dimensions.

## Three Insertion Points

IA3 introduces three learned scale vectors per transformer layer: (1) l_k ∈ ℝ^(d_k) scales the attention keys: K ← l_k ⊙ K, where ⊙ is element-wise multiplication. This modulates which key dimensions are amplified or suppressed during attention score computation. (2) l_v ∈ ℝ^(d_v) scales the attention values: V ← l_v ⊙ V. This controls which value dimensions are passed through to the output. (3) l_ff ∈ ℝ^(d_ff) scales the intermediate FFN activation (after the first linear + activation): x ← l_ff ⊙ σ(W_1 x). All other activations and all weight matrices remain unchanged. All scale vectors are initialized to ones, ensuring identity behavior at the start of training.

Parameter count for LLaMA-7B: with 32 attention heads of dimension 64, d_k_total = d_v_total = 32×64 = 2048. FFN intermediate d_ff = 11008. Per layer: 2048 + 2048 + 11008 = 15104 scalars. With 32 layers: 32×15104 = 483,328 ≈ 0.48M parameters. This is roughly 100× fewer parameters than LoRA with r=8 on the same model (which has approximately 50M trainable params across all Q, K, V, O projections). At 16-bit precision, the IA3 parameters occupy less than 1MB of storage.

## IA3 Attention Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class IA3Attention(nn.Module):
    """
    Multi-head attention with IA3 scaling on keys and values.
    Backbone Q, K, V projections are frozen; only l_k, l_v are trained.
    """

    def __init__(self, d_model: int, n_heads: int, freeze_backbone: bool = True):
        super().__init__()
        assert d_model % n_heads == 0
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads
        self.scale = self.head_dim ** -0.5
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)
        if freeze_backbone:
            for module in [self.q_proj, self.k_proj, self.v_proj, self.out_proj]:
                for param in module.parameters():
                    param.requires_grad = False
        # IA3 learned scales -- init to 1 (identity at start)
        self.l_k = nn.Parameter(torch.ones(d_model))
        self.l_v = nn.Parameter(torch.ones(d_model))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        bsz, seq, d = x.shape
        Q = self.q_proj(x)                 # no scaling on Q
        K = self.k_proj(x) * self.l_k     # IA3 scale keys
        V = self.v_proj(x) * self.l_v     # IA3 scale values
        def split(t): return t.view(bsz, seq, self.n_heads, self.head_dim).transpose(1, 2)
        Q, K, V = split(Q), split(K), split(V)
        attn = F.softmax((Q @ K.transpose(-2, -1)) * self.scale, dim=-1)
        out = (attn @ V).transpose(1, 2).contiguous().view(bsz, seq, d)
        return self.out_proj(out)

attn = IA3Attention(512, 8)
trainable = [(n, p.shape) for n, p in attn.named_parameters() if p.requires_grad]
print(f'Trainable params: {trainable}')  # only l_k, l_v
```

## IA3 FFN and Parameter Count

```python
import torch
import torch.nn as nn

class IA3FFN(nn.Module):
    """
    Feed-forward network with IA3 scaling on intermediate activation.
    l_ff scales the output of the first linear + activation.
    """

    def __init__(self, d_model: int, d_ff: int, freeze_backbone: bool = True):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.act = nn.GELU()
        if freeze_backbone:
            for p in self.parameters():
                p.requires_grad = False
        self.l_ff = nn.Parameter(torch.ones(d_ff))  # init=1 (identity)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.act(self.linear1(x))  # (bsz, seq, d_ff)
        h = h * self.l_ff             # IA3 scale
        return self.linear2(h)

# Parameter count across model sizes
configs = [
    ('BERT-base',  768,  3072, 12),
    ('T5-Large',  1024,  4096, 24),
    ('LLaMA-7B',  4096, 11008, 32),
    ('LLaMA-13B', 5120, 13824, 40),
]
print(f'{"Model":<14} {"d_model":>8} {"d_ff":>7} {"Layers":>7} {"IA3 Params":>12}')
print('-' * 55)
for name, d, dff, L in configs:
    per_layer = d + d + dff  # l_k + l_v + l_ff
    total = per_layer * L
    print(f'{name:<14} {d:>8} {dff:>7} {L:>7} {total:>12,}')
```

## Weight Merging at Inference

IA3 scaling vectors can be folded into the underlying weight matrices before deployment, eliminating any inference overhead. The key insight: multiplying activations by a learned vector is equivalent to scaling the corresponding rows of the projection matrix that produces those activations. Specifically: K ← l_k ⊙ W_K x is equivalent to K ← (diag(l_k) W_K) x. So W_K_merged = diag(l_k) @ W_K, i.e., multiply each row i of W_K by l_k[i]. Similarly for W_V. For l_ff scaling the FFN intermediate, it is equivalent to scaling the rows of W_2 (the second linear): W_2_merged[i, :] = l_ff[i] × W_2[i, :].

```python
import torch
import torch.nn as nn

def merge_ia3_into_weights(k_proj_weight: torch.Tensor,
                           v_proj_weight: torch.Tensor,
                           ffn2_weight: torch.Tensor,
                           l_k: torch.Tensor,
                           l_v: torch.Tensor,
                           l_ff: torch.Tensor):
    """
    Fold IA3 scaling vectors into projection weight matrices.
    After merging, model uses standard linear layers with no inference overhead.
    K_merged[i, :] = l_k[i] * k_proj_weight[i, :]
    V_merged[i, :] = l_v[i] * v_proj_weight[i, :]
    FFN2_merged[i, :] = l_ff[i] * ffn2_weight[i, :]   (linear2 rows)
    """
    # Scale output rows of K and V projection weights
    K_merged   = k_proj_weight * l_k.unsqueeze(1)    # (d_model, d_model)
    V_merged   = v_proj_weight * l_v.unsqueeze(1)    # (d_model, d_model)
    FFN2_merged = ffn2_weight  * l_ff.unsqueeze(1)   # (d_model, d_ff)
    print(f'K diff vs original: {(K_merged - k_proj_weight).abs().mean():.4f}')
    return K_merged, V_merged, FFN2_merged

d_model, d_ff = 512, 2048
k_w = torch.randn(d_model, d_model)
v_w = torch.randn(d_model, d_model)
ffn2_w = torch.randn(d_model, d_ff)
l_k  = torch.ones(d_model) + 0.1 * torch.randn(d_model)
l_v  = torch.ones(d_model) + 0.1 * torch.randn(d_model)
l_ff = torch.ones(d_ff) + 0.1 * torch.randn(d_ff)
K_m, V_m, FFN_m = merge_ia3_into_weights(k_w, v_w, ffn2_w, l_k, l_v, l_ff)
print(f'Merged shapes: K={K_m.shape}, V={V_m.shape}, FFN2={FFN_m.shape}')
```

## Few-Shot Learning Comparison

IA3 was designed specifically for few-shot fine-tuning in the T-Few paper (Liu et al., 2022). The key intuition: with very few labeled examples (10–50), methods with more trainable parameters overfit more easily. IA3's ≈480K parameters for a 7B model provides a much lower-capacity learner than LoRA's ≈50M, reducing the risk of memorizing the few training examples rather than learning generalizable patterns.

```python
import numpy as np

# Approximate accuracy from T-Few paper (Liu et al. 2022)
# T5-Large (770M) backbone, averaged over SuperGLUE-style tasks
shot_counts = [10, 50, 100, 500]
ia3_acc     = [67.3, 74.8, 78.2, 82.1]
lora_acc    = [63.1, 72.4, 77.1, 82.5]  # LoRA r=8
adapter_acc = [61.4, 71.8, 76.8, 82.0]  # Pfeiffer adapters m=64
full_ft_acc = [58.2, 70.1, 76.3, 83.0]  # prone to overfitting at low shot

print(f'{"Shots":>8} | {"IA3":>8} | {"LoRA r=8":>10} | {"Adapters":>10} | {"Full FT":>9}')
print('-' * 55)
for s, ia, lo, ad, fft in zip(shot_counts, ia3_acc, lora_acc, adapter_acc, full_ft_acc):
    print(f'{s:>8} | {ia:>8.1f} | {lo:>10.1f} | {ad:>10.1f} | {fft:>9.1f}')

print()
print('IA3 advantage is largest at low shot counts (10-50):')
for s, ia, lo in zip(shot_counts[:2], ia3_acc[:2], lora_acc[:2]):
    print(f'  {s}-shot: IA3 {ia:.1f} vs LoRA {lo:.1f} (+{ia-lo:.1f})')
```

## IA3 vs Other PEFT Methods

| Method | Trainable Params (7B) | Insertion Type | Multiplicative/Additive | Merge at Inference | Few-Shot Suitability |
| --- | --- | --- | --- | --- | --- |
| IA3 | ~483K (3 vectors/layer) | K, V, FFN intermediate scaling | Multiplicative | Yes — fold l into weight rows | Excellent — lowest overfit risk |
| LoRA (r=8) | ~50M (2 matrices/layer) | W += BA (low-rank additive) | Additive | Yes — W_merged = W + BA | Good — moderate params |
| VeRA | ~65K (shared random B, A) | W += λ_b diag(b) B diag(a) A | Additive with scaling | Yes — merge like LoRA | Very good — very few params |
| Adapter (Pfeiffer) | ~200M (bottleneck FFN) | Serial FFN after each sub-layer | Additive | No — adds extra compute path | Moderate — more params to overfit |
| Prompt Tuning | ~100K (input prefix only) | Input embedding prefix | Neither (input modification) | N/A — prefix always present | Poor at <10B scale |

## T-Few: IA3 with Task-Specific Pretraining

The T-Few paper (Liu et al., 2022) demonstrates that IA3 combined with multitask pretraining (T0 model) achieves state-of-the-art few-shot performance with far fewer trainable parameters than GPT-3 (175B) despite using T5-Large (770M). The T-Few recipe: (1) start from T0, a T5-Large pretrained on 35 NLP datasets with natural language prompts; (2) apply IA3 and train on K examples per task; (3) use unlikelihood training to improve calibration. At 10-shot, T-Few (770M params, 483K IA3 params fine-tuned) outperforms GPT-3 (175B, zero-shot) on 9 of 11 benchmarks.

## Using IA3 with the PEFT Library

The HuggingFace PEFT library provides native IA3 support via IA3Config. The key parameters are target_modules (which projection matrices to apply l_k and l_v to, typically ['k_proj', 'v_proj']) and feedforward_modules (which FFN layers to apply l_ff to, typically ['down_proj'] for LLaMA-style models or ['fc2'] for BERT-style). After training, call model.merge_adapter() to fold the scale vectors into the base weights for zero-overhead inference. The merged model is indistinguishable from a standard model and can be served without the PEFT library.

> **Multiplicative vs Additive**: IA3's multiplicative scaling preserves the subspace structure of pretrained activations — unlike additive adapters (LoRA, adapters), IA3 can only scale existing features, not create new ones. This makes it ideal for task-specific emphasis but weaker for structural adaptation.

## Practical Recommendations

- IA3 init: l_k = l_v = l_ff = 1 (ones vector) — ensures identity mapping at the start of training.
- Parameter count: ~360–480K for 7B models — roughly 100× fewer than LoRA r=8.
- Weight merging: fold l_k into K projection rows, l_v into V projection rows, l_ff into linear2 rows at inference.
- Few-shot regime: IA3 outperforms LoRA and adapters at 10–50 shots due to lower parameter count reducing overfitting.
- IA3 cannot introduce new feature directions — if the task requires new representations, LoRA or adapters are preferable.
- Use peft library: IA3Config with target_modules=['k_proj','v_proj'] and feedforward_modules=['down_proj'].
- For instruction-following fine-tuning at 10B+ scale, IA3 is competitive with LoRA at 100× fewer parameters.

---

