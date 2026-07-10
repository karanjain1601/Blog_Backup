---
title: "Classifier Guidance — Conditional Generation via Gradient Steering"
slug: "classifier-guidance-diffusion"
description: "Derive classifier guidance from the conditional score, implement a noisy classifier trained at all noise levels, integrate classifier gradients into the DDPM denoising loop, sweep the guidance scale, and compare quality-diversity tradeoffs against unconditional and CFG baselines."
tags: ["deep-learning", "generative-models", "diffusion-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2xhc3NpZmllciBndWlkYW5jZSAoRGhhcml3YWwgXHUwMDI2IE5pY2hvbCAyMDIxKSB3YXMgdGhlIGZpcnN0IG1ldGhvZCB0byByZWxpYWJseSBwdXNoIGNsYXNzLWNvbmRpdGlvbmFsIGRpZmZ1c2lvbiBtb2RlbHMgcGFzdCBHQU5zIG9uIEltYWdlTmV0LiBUaGUgY29yZSBpZGVhOiBzYW1wbGUgZnJvbSBwKHh8eSkg4oidIHAoeCnCt3AoeXx4KSBieSBzdGVlcmluZyBlYWNoIGRlbm9pc2luZyBzdGVwIHdpdGggdGhlIGdyYWRpZW50IG9mIGEgY2xhc3NpZmllci4gVGhlIHVuY29uZGl0aW9uYWwgZGlmZnVzaW9uIG1vZGVsIHByb3ZpZGVzIHRoZSBzY29yZSDiiIdfeCBsb2cgcCh4KSwgd2hpbGUgYSBzZXBhcmF0ZWx5IHRyYWluZWQgY2xhc3NpZmllciBwcm92aWRlcyDiiIdfeCBsb2cgcCh5fHgpLiBDb21iaW5pbmcgdGhlbSB5aWVsZHMgdGhlIGNvbmRpdGlvbmFsIHNjb3JlIOKAlCBubyBjb25kaXRpb25hbCByZXRyYWluaW5nIG9mIHRoZSBkaWZmdXNpb24gbW9kZWwgaXMgcmVxdWlyZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uZGl0aW9uYWwgR2VuZXJhdGlvbiB2aWEgQmF5ZXNcdTAwMjcgUnVsZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvbmRpdGlvbmFsIGRpc3RyaWJ1dGlvbiBwKHh8eSkgPSBwKHgpwrdwKHl8eCkvcCh5KS4gVGFraW5nIGxvZy1ncmFkaWVudHM6IOKIh194IGxvZyBwKHh8eSkgPSDiiIdfeCBsb2cgcCh4KSArIOKIh194IGxvZyBwKHl8eCkuIFRoZSBmaXJzdCB0ZXJtIGlzIHRoZSB1bmNvbmRpdGlvbmFsIHNjb3JlIChwcm92aWRlZCBieSB0aGUgZGlmZnVzaW9uIG1vZGVsKTsgdGhlIHNlY29uZCBpcyB0aGUgY2xhc3NpZmllciBncmFkaWVudCBhdCB4LiBBdCBlYWNoIGRlbm9pc2luZyBzdGVwIHQsIHdlIHdvcmsgd2l0aCB0aGUgbm9pc3kgdmVyc2lvbnM6IOKIh197eF90fSBsb2cgcCh4X3R8eSkgPSDiiIdfe3hfdH0gbG9nIHBfdCh4X3QpICsg4oiHX3t4X3R9IGxvZyBwX8+GKHl8eF90KS4gVGhlIG1vZGlmaWVkIGVwc2lsb24gaXMgdGhlbiDOtcyDID0gzrVfzrgoeF90LHQpIOKIkiDiiJooMeKIkuG+sV90KcK3c8K34oiHX3t4X3R9IGxvZyBwX8+GKHl8eF90KSwgd2hlcmUgcyBcdTAwM2UgMSBpcyB0aGUgZ3VpZGFuY2Ugc2NhbGUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTm9pc3kgQ2xhc3NpZmllciBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNsYXNzaWZpZXIgcF/Phih5fHhfdCkgbXVzdCBiZSB0cmFpbmVkIG9uIG5vaXN5IGltYWdlcyBhdCBhbGwgbm9pc2UgbGV2ZWxzIHQsIG5vdCBjbGVhbiBpbWFnZXMuIEEgY2xhc3NpZmllciB0cmFpbmVkIG9uIGNsZWFuIGltYWdlcyBjYW5ub3QgcHJvdmlkZSByZWxpYWJsZSBncmFkaWVudHMgaW4gaGlnaC1ub2lzZSByZWdpb25zIHdoZXJlIHhfdCBsb29rcyBsaWtlIHB1cmUgbm9pc2UuIER1cmluZyB0cmFpbmluZywgdGhlIG5vaXNlIGxldmVsIHQgaXMgc2FtcGxlZCB1bmlmb3JtbHksIHhfdCA9IOKImuG+sV90wrd4ICsg4oiaKDHiiJLhvrFfdCnCt861IGlzIGNvbXB1dGVkLCBhbmQgdGhlIGNsYXNzaWZpZXIgcHJlZGljdHMgdGhlIGNsYXNzIGZyb20geF90LiBUaGlzIHRyYWlucyB0aGUgY2xhc3NpZmllciB0byBleHRyYWN0IGNsYXNzIHNpZ25hbCBmcm9tIGNvcnJ1cHRlZCBpbnB1dHMgYWNyb3NzIHRoZSBmdWxsIG5vaXNlIHNwZWN0cnVtLCBlbmFibGluZyBtZWFuaW5nZnVsIGdyYWRpZW50IHNpZ25hbHMgYXQgZXZlcnkgZGVub2lzaW5nIHN0ZXAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuY2xhc3MgTm9pc3lDbGFzc2lmaWVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2RpbT0zMiwgbl9jbGFzc2VzPTEwLCBUPTEwMDApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi50aW1lX2VtYmVkID0gbm4uRW1iZWRkaW5nKFQsIDE2KVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoaW5fZGltICsgMTYsIDEyOCksIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcigxMjgsIDY0KSwgbm4uU2lMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDY0LCBuX2NsYXNzZXMpXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4X3QsIHQpOlxuICAgICAgICB0X2VtYiA9IHNlbGYudGltZV9lbWJlZCh0KVxuICAgICAgICByZXR1cm4gc2VsZi5uZXQodG9yY2guY2F0KFt4X3QsIHRfZW1iXSwgZGltPS0xKSlcblxuZGVmIHRyYWluX25vaXN5X2NsYXNzaWZpZXIoY2xmLCBkYXRhLCBsYWJlbHMsIGFscGhhX2Jhciwgbl9zdGVwcz0zMDApOlxuICAgIG9wdCA9IHRvcmNoLm9wdGltLkFkYW0oY2xmLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBUID0gbGVuKGFscGhhX2JhcilcbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgaWR4ID0gdG9yY2gucmFuZGludCgwLCBsZW4oZGF0YSksICg2NCwpKVxuICAgICAgICB4MCwgeSA9IGRhdGFbaWR4XSwgbGFiZWxzW2lkeF1cbiAgICAgICAgdCA9IHRvcmNoLnJhbmRpbnQoMCwgVCwgKDY0LCkpXG4gICAgICAgIGVwcyA9IHRvcmNoLnJhbmRuX2xpa2UoeDApXG4gICAgICAgIGFiID0gYWxwaGFfYmFyW3RdLnVuc3F1ZWV6ZSgxKVxuICAgICAgICB4X3QgPSB0b3JjaC5zcXJ0KGFiKSAqIHgwICsgdG9yY2guc3FydCgxIC0gYWIpICogZXBzXG4gICAgICAgIGxvZ2l0cyA9IGNsZih4X3QsIHQpXG4gICAgICAgIGxvc3MgPSBGLmNyb3NzX2VudHJvcHkobG9naXRzLCB5KVxuICAgICAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgICAgICBpZiBzdGVwICUgMTAwID09IDA6XG4gICAgICAgICAgICBwcmludChmXHUwMDI3U3RlcCB7c3RlcH06IGNsYXNzaWZpZXIgbG9zcyA9IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KVxuICAgIHJldHVybiBjbGZcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmFscGhhX2JhciA9IHRvcmNoLmN1bXByb2QoMSAtIHRvcmNoLmxpbnNwYWNlKDFlLTQsIDAuMDIsIDEwMDApLCBkaW09MClcbmRhdGEgPSB0b3JjaC5yYW5kbig1MDAsIDMyKVxubGFiZWxzID0gdG9yY2gucmFuZGludCgwLCAxMCwgKDUwMCwpKVxuY2xmID0gTm9pc3lDbGFzc2lmaWVyKGluX2RpbT0zMilcbnRyYWluX25vaXN5X2NsYXNzaWZpZXIoY2xmLCBkYXRhLCBsYWJlbHMsIGFscGhhX2Jhciwgbl9zdGVwcz0zMDApIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2xhc3NpZmllciBHdWlkYW5jZSBpbiB0aGUgRGVub2lzaW5nIExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF0IGVhY2ggZGVub2lzaW5nIHN0ZXAsIHRoZSBjbGFzc2lmaWVyIGdyYWRpZW50IHN0ZWVycyB0aGUgZXBzaWxvbiBwcmVkaWN0aW9uIHRvd2FyZCBoaWdoZXIgY2xhc3MgcHJvYmFiaWxpdHkuIFRoZSBwZXJ0dXJiZWQgZXBzaWxvbiBpczogzrXMgyA9IM61X864KHhfdCx0KSDiiJIgc8K34oiaKDHiiJLhvrFfdCnCt+KIh197eF90fSBsb2cgcF/Phih5fHhfdCkuIFRoZSBmYWN0b3Ig4oiaKDHiiJLhvrFfdCkgY29udmVydHMgdGhlIGdyYWRpZW50IGZyb20geC1zcGFjZSB0byBlcHNpbG9uLXNwYWNlIChzaW5jZSDOtSBhbmQg4oiHX3t4X3R9IGxvZyBwX3QgYXJlIHJlbGF0ZWQgYnkgdGhpcyBmYWN0b3IpLiBUaGUgZ3VpZGFuY2Ugc2NhbGUgcyBcdTAwM2UgMSBhbXBsaWZpZXMgdGhlIGNsYXNzIHNpZ25hbCBiZXlvbmQgd2hhdCB0aGUgdHJhaW5pbmcgZGlzdHJpYnV0aW9uIHN1cHBvcnRzLCB0cmFkaW5nIGRpdmVyc2l0eSBmb3IgZmlkZWxpdHkuIEZvciBzPTEgdGhpcyByZWR1Y2VzIHRvIHNpbXBsZSBCYXllc2lhbiBjb25kaXRpb25pbmc7IGZvciBzPTXigJMxMCB0aGUgbW9kZS1zZWVraW5nIGVmZmVjdCBpcyBzdHJvbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbkB0b3JjaC5ub19ncmFkKClcbmRlZiBndWlkZWRfc2FtcGxpbmcoZXBzX21vZGVsLCBjbGFzc2lmaWVyLCB5LCBhbHBoYV9iYXIsXG4gICAgICAgICAgICAgICAgICAgIHRpbWVzdGVwcywgZ3VpZGFuY2Vfc2NhbGU9My4wLCBzaGFwZT0oNCwgMzIpKTpcbiAgICBcIlwiXCJDbGFzc2lmaWVyLWd1aWRlZCBERFBNIHNhbXBsaW5nIGxvb3AuXCJcIlwiXG4gICAgeCA9IHRvcmNoLnJhbmRuKHNoYXBlKVxuICAgIEIgPSBzaGFwZVswXVxuICAgIGZvciB0IGluIHRpbWVzdGVwczpcbiAgICAgICAgYWJfdCA9IGFscGhhX2Jhclt0XVxuICAgICAgICBhYl9wcmV2ID0gYWxwaGFfYmFyW3QgLSAxXSBpZiB0IFx1MDAzZSAwIGVsc2UgdG9yY2gudGVuc29yKDEuMClcbiAgICAgICAgdF9iYXRjaCA9IHRvcmNoLmZ1bGwoKEIsKSwgdCwgZHR5cGU9dG9yY2gubG9uZylcbiAgICAgICAgIyBVbmNvbmRpdGlvbmFsIHNjb3JlIChlcHNpbG9uIHByZWRpY3Rpb24pXG4gICAgICAgIGVwc191bmNvbmQgPSBlcHNfbW9kZWwoeCwgdF9iYXRjaClcbiAgICAgICAgIyBDbGFzc2lmaWVyIGdyYWRpZW50XG4gICAgICAgIHhfZ3JhZCA9IHguZGV0YWNoKCkucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICAgICAgd2l0aCB0b3JjaC5lbmFibGVfZ3JhZCgpOlxuICAgICAgICAgICAgbG9naXRzID0gY2xhc3NpZmllcih4X2dyYWQsIHRfYmF0Y2gpXG4gICAgICAgICAgICBsb2dfcHJvYiA9IGxvZ2l0cy5sb2dfc29mdG1heChkaW09LTEpW3JhbmdlKEIpLCB5XVxuICAgICAgICAgICAgZ3JhZCA9IHRvcmNoLmF1dG9ncmFkLmdyYWQobG9nX3Byb2Iuc3VtKCksIHhfZ3JhZClbMF1cbiAgICAgICAgIyBQZXJ0dXJiIGVwc2lsb24gYnkgY2xhc3NpZmllciBncmFkaWVudFxuICAgICAgICBlcHNfZ3VpZGVkID0gZXBzX3VuY29uZCAtIGd1aWRhbmNlX3NjYWxlICogdG9yY2guc3FydCgxIC0gYWJfdCkgKiBncmFkLmRldGFjaCgpXG4gICAgICAgICMgU3RhbmRhcmQgRERQTSByZXZlcnNlIHN0ZXBcbiAgICAgICAgY29lZjEgPSAxLjAgLyB0b3JjaC5zcXJ0KDEgLSBhbHBoYV9iYXJbdF0gLyBhYl9wcmV2KVxuICAgICAgICB4X3ByZXZfbWVhbiA9IGNvZWYxICogKHggLSAoMSAtIGFiX3QvYWJfcHJldikgLyB0b3JjaC5zcXJ0KDEgLSBhYl90KSAqIGVwc19ndWlkZWQpXG4gICAgICAgIG5vaXNlID0gdG9yY2gucmFuZG5fbGlrZSh4KSAqIHRvcmNoLnNxcnQoMSAtIGFiX3ByZXYpIGlmIHQgXHUwMDNlIDAgZWxzZSAwLjBcbiAgICAgICAgeCA9IHhfcHJldl9tZWFuICsgbm9pc2VcbiAgICByZXR1cm4geFxuXG5wcmludChcdTAwMjdDbGFzc2lmaWVyIGd1aWRhbmNlOiBzdGVlciBlcHMgYXQgZWFjaCBzdGVwIGJ5IGNsYXNzaWZpZXIgbG9nLXByb2IgZ3JhZGllbnRcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQURNIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGhhcml3YWwgXHUwMDI2IE5pY2hvbCAoMjAyMSkgYWxzbyBpbnRyb2R1Y2VkIEFETSAoQWJsYXRlZCBEaWZmdXNpb24gTW9kZWwpIOKAlCBhIFUtTmV0IHdpdGggYWRhcHRpdmUgZ3JvdXAgbm9ybWFsaXphdGlvbiwgYXR0ZW50aW9uIGF0IG11bHRpcGxlIHJlc29sdXRpb25zLCBhbmQgQmlnR0FOIHJlc2lkdWFsIGJsb2Nrcy4gQURNIHdpdGggY2xhc3NpZmllciBndWlkYW5jZSBhY2hpZXZlZCBGSUQgNC41OSBvbiBJbWFnZU5ldCAyNTbDlzI1Niwgc3VycGFzc2luZyB0aGUgYmVzdCBHQU5zIChCaWdHQU4tZGVlcDogRklEIDYuOTUpLiBLZXkgYXJjaGl0ZWN0dXJhbCBpbXByb3ZlbWVudHM6IGF0dGVudGlvbiBoZWFkcyB3aXRoIDY0IGNoYW5uZWxzIGluc3RlYWQgb2YgMTI4LCBtdWx0aS1yZXNvbHV0aW9uIGF0dGVudGlvbiAoMzLDlzMyLCAxNsOXMTYsIDjDlzgpLCBhbmQgaW5jcmVhc2VkIGRlcHRoLiBUaGVzZSBhcmNoaXRlY3R1cmFsIGdhaW5zIGNvbWJpbmVkIHdpdGggY2xhc3NpZmllciBndWlkYW5jZSBlc3RhYmxpc2hlZCBkaWZmdXNpb24gbW9kZWxzIGFzIHRoZSBuZXcgc3RhdGUtb2YtdGhlLWFydCBvbiBoaWdoLXJlc29sdXRpb24gY2xhc3MtY29uZGl0aW9uYWwgc3ludGhlc2lzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikd1aWRhbmNlIFNjYWxlIFRyYWRlLW9mZiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGd1aWRhbmNlIHNjYWxlIHMgY29udHJvbHMgdGhlIGZpZGVsaXR5LWRpdmVyc2l0eSB0cmFkZS1vZmYuIEF0IHM9MSwgc2FtcGxlcyBhcmUgZHJhd24gZnJvbSB0aGUgdHJ1ZSBjb25kaXRpb25hbCBkaXN0cmlidXRpb24gcCh4fHkpLiBBdCBzIFx1MDAzZSAxLCB0aGUgc2FtcGxpbmcgc3RlZXJzIGJleW9uZCB0aGUgc3VwcG9ydCBvZiB0aGUgdHJhaW5pbmcgZGlzdHJpYnV0aW9uIHRvd2FyZCBoaWdoLWNsYXNzLXByb2JhYmlsaXR5IG1vZGVzLiBGSUQgaW1wcm92ZXMgd2l0aCBzIHVwIHRvIGEgcG9pbnQgKHR5cGljYWxseSBzPTLigJM1IGZvciBJbWFnZU5ldCksIHRoZW4gZGVncmFkZXMgYXMgc2FtcGxlcyBiZWNvbWUgb3Zlci1zaGFycGVuZWQgYXJ0aWZhY3RzIHdpdGggdW5uYXR1cmFsIGNvbG9ycy4gSW5jZXB0aW9uIFNjb3JlIChJUykgbWVhc3VyZXMgY2xhc3MgZmlkZWxpdHkgYW5kIGtlZXBzIGluY3JlYXNpbmcgd2l0aCBzLiBUaGUgcyB0aGF0IG1pbmltaXplcyBGSUQg4omgIHRoZSBzIHRoYXQgbWF4aW1pemVzIElTIOKAlCBwcmFjdGl0aW9uZXJzIHBsb3QgYm90aCBjdXJ2ZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHNpbXVsYXRlX2d1aWRhbmNlX3RyYWRlb2ZmKGd1aWRhbmNlX3NjYWxlcywgbl9zYW1wbGVzPTIwMCwgc2VlZD0wKTpcbiAgICBcIlwiXCJTaW11bGF0ZSBGSUQgdnMgSVMgdHJhZGVvZmYgYXMgZ3VpZGFuY2Ugc2NhbGUgaW5jcmVhc2VzLlwiXCJcIlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgcmVzdWx0cyA9IFtdXG4gICAgZm9yIHMgaW4gZ3VpZGFuY2Vfc2NhbGVzOlxuICAgICAgICAjIFNpbXVsYXRlIHF1YWxpdHkgKGxvd2VyIHZhcmlhbmNlID0gaGlnaGVyIGZpZGVsaXR5IGJ1dCBsZXNzIGRpdmVyc2UpXG4gICAgICAgICMgQXQgcz0xOiBkaXZlcnNlIGJ1dCBpbXB1cmUgbW9kZXM7IGF0IGhpZ2ggczogbW9kZS1jb2xsYXBzZWRcbiAgICAgICAgcm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKHNlZWQpXG4gICAgICAgICMgRklEOiBVLXNoYXBlZCBhcm91bmQgb3B0aW1hbCBndWlkYW5jZVxuICAgICAgICBmaWQgPSAxMC4wICsgKHMgLSAzLjUpICoqIDIgKiAxLjIgKyBybmcucmFuZG4oKSAqIDAuM1xuICAgICAgICAjIElTOiBtb25vdG9uaWNhbGx5IGluY3JlYXNlcyB3aXRoIGd1aWRhbmNlIChjbGFzcyBmaWRlbGl0eSlcbiAgICAgICAgaW5jZXB0aW9uX3Njb3JlID0gMjAuMCArIDguMCAqIG5wLmxvZyhzICsgMSkgKyBybmcucmFuZG4oKSAqIDAuNVxuICAgICAgICAjIERpdmVyc2l0eSAocmVjYWxsKTogZGVjcmVhc2VzIHdpdGggZ3VpZGFuY2VcbiAgICAgICAgcmVjYWxsID0gMC42MCAqIG5wLmV4cCgtMC4xNSAqIChzIC0gMSkpICsgcm5nLnJhbmRuKCkgKiAwLjAyXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKChzLCBtYXgoZmlkLCAxLjApLCBpbmNlcHRpb25fc2NvcmUsIG1heChyZWNhbGwsIDAuMDUpKSlcbiAgICByZXR1cm4gcmVzdWx0c1xuXG5zY2FsZXMgPSBbMSwgMS41LCAyLCAzLCA0LCA1LCA3LCAxMF1cbnByaW50KGZcdTAwMjd7XCJTY2FsZVwiOlx1MDAzZTZ9IHwge1wiRklEXCI6XHUwMDNlNn0gfCB7XCJJU1wiOlx1MDAzZTh9IHwge1wiUmVjYWxsXCI6XHUwMDNlN31cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogMzYpXG5mb3IgcywgZmlkLCBJUywgcmVjIGluIHNpbXVsYXRlX2d1aWRhbmNlX3RyYWRlb2ZmKHNjYWxlcyk6XG4gICAgcHJpbnQoZlx1MDAyN3tzOjYuMWZ9IHwge2ZpZDo2LjJmfSB8IHtJUzo4LjJmfSB8IHtyZWM6Ny4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVW5jb25kaXRpb25hbCB2cyBHdWlkZWQgR2VuZXJhdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBjb21wYXJlX2d1aWRhbmNlKGVwc19tb2RlbCwgY2xhc3NpZmllciwgYWxwaGFfYmFyLCBuX3N0ZXBzPTUwLCBEPTE2LCBCPTgpOlxuICAgIFwiXCJcIkNvbXBhcmUgdW5jb25kaXRpb25hbCB2cyBndWlkZWQgc2FtcGxpbmcgYXQgc2FtZSBORkUgYnVkZ2V0LlwiXCJcIlxuICAgIHRpbWVzdGVwcyA9IGxpc3QocmFuZ2UoMCwgMTAwMCwgMTAwMCAvLyBuX3N0ZXBzKSlbOjotMV1cbiAgICB5ID0gdG9yY2guemVyb3MoQiwgZHR5cGU9dG9yY2gubG9uZykgICMgY2xhc3MgMFxuXG4gICAgZGVmIHNhbXBsZShndWlkYW5jZV9zY2FsZSk6XG4gICAgICAgIHRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuICAgICAgICB4ID0gdG9yY2gucmFuZG4oQiwgRClcbiAgICAgICAgZm9yIHQgaW4gdGltZXN0ZXBzOlxuICAgICAgICAgICAgYWIgPSBhbHBoYV9iYXJbdF1cbiAgICAgICAgICAgIHRfYiA9IHRvcmNoLmZ1bGwoKEIsKSwgdCwgZHR5cGU9dG9yY2gubG9uZylcbiAgICAgICAgICAgIGVwcyA9IGVwc19tb2RlbCh4LCB0X2IpXG4gICAgICAgICAgICBpZiBndWlkYW5jZV9zY2FsZSBcdTAwM2UgMS4wOlxuICAgICAgICAgICAgICAgIHhfZyA9IHguZGV0YWNoKCkucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICAgICAgICAgICAgICB3aXRoIHRvcmNoLmVuYWJsZV9ncmFkKCk6XG4gICAgICAgICAgICAgICAgICAgIGxwID0gY2xhc3NpZmllcih4X2csIHRfYikubG9nX3NvZnRtYXgoLTEpW3JhbmdlKEIpLCB5XVxuICAgICAgICAgICAgICAgICAgICBncmFkID0gdG9yY2guYXV0b2dyYWQuZ3JhZChscC5zdW0oKSwgeF9nKVswXS5kZXRhY2goKVxuICAgICAgICAgICAgICAgIGVwcyA9IGVwcyAtIGd1aWRhbmNlX3NjYWxlICogdG9yY2guc3FydCgxIC0gYWIpICogZ3JhZFxuICAgICAgICAgICAgYWJfcCA9IGFscGhhX2JhclttYXgodC0yMCwgMCldXG4gICAgICAgICAgICB4MCA9ICh4IC0gdG9yY2guc3FydCgxLWFiKSplcHMpIC8gdG9yY2guc3FydChhYilcbiAgICAgICAgICAgIHggPSB0b3JjaC5zcXJ0KGFiX3ApKngwLmNsYW1wKC0xLDEpICsgdG9yY2guc3FydCgxLWFiX3ApKmVwc1xuICAgICAgICByZXR1cm4geFxuXG4gICAgZm9yIHMgaW4gWzEuMCwgMy4wLCA3LjBdOlxuICAgICAgICBvdXQgPSBzYW1wbGUocylcbiAgICAgICAgcHJpbnQoZlx1MDAyN2d1aWRhbmNlX3NjYWxlPXtzOjQuMWZ9OiBub3JtPXtvdXQubm9ybSgpOi4yZn0gc3RkPXtvdXQuc3RkKCk6LjNmfVx1MDAyNylcblxuY2xhc3MgRHVtbXlFcHMobm4uTW9kdWxlKTpcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCB0KTogcmV0dXJuIHggKiAwLjA1XG5jbGFzcyBEdW1teUNsZihubi5Nb2R1bGUpOlxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIHQpOiByZXR1cm4geFs6LCA6MTBdICAjIHRyZWF0IGZpcnN0IDEwIGRpbXMgYXMgbG9naXRzXG5hbHBoYV9iYXIgPSB0b3JjaC5jdW1wcm9kKDEgLSB0b3JjaC5saW5zcGFjZSgxZS00LCAwLjAyLCAxMDAwKSwgZGltPTApXG5jb21wYXJlX2d1aWRhbmNlKER1bW15RXBzKCksIER1bW15Q2xmKCksIGFscGhhX2JhcikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW1pdGF0aW9ucyBvZiBDbGFzc2lmaWVyIEd1aWRhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFzc2lmaWVyIGd1aWRhbmNlIGhhcyB0aHJlZSBwcmFjdGljYWwgbGltaXRhdGlvbnM6ICgxKSBJdCByZXF1aXJlcyBhIHNlcGFyYXRlbHkgdHJhaW5lZCBub2lzeSBjbGFzc2lmaWVyIOKAlCBkb3VibGUgdGhlIHRyYWluaW5nIGNvc3QgYW5kIGNvbXBsZXhpdHkuICgyKSBFdmVyeSBkZW5vaXNpbmcgc3RlcCByZXF1aXJlcyBhIGdyYWRpZW50IGNvbXB1dGF0aW9uIHRocm91Z2ggdGhlIGNsYXNzaWZpZXIgKHRvcmNoLmF1dG9ncmFkLmdyYWQpLCBhZGRpbmcgfjUwJSBjb21wdXRlIHBlciBzdGVwLiAoMykgVGhlIGNsYXNzaWZpZXIgaXMgdHJhaW5lZCBvbiBub2lzeSBpbWFnZXMgd2hpY2ggaXMgYW4gdW51c3VhbCBkaXN0cmlidXRpb24g4oCUIHNtYWxsIHRyYWluaW5nIGJ1Z3MgY2FuIHByb2R1Y2UgbWlzbGVhZGluZyBncmFkaWVudHMuIFRoZXNlIGxpbWl0YXRpb25zIG1vdGl2YXRlZCBjbGFzc2lmaWVyLWZyZWUgZ3VpZGFuY2UgKEhvIFx1MDAyNiBTYWxpbWFucyAyMDIyKSwgd2hpY2ggYWNoaWV2ZXMgdGhlIHNhbWUgZWZmZWN0IHVzaW5nIGEgc2luZ2xlIG5ldHdvcmsgd2l0aCBjb25kaXRpb25pbmcgZHJvcG91dC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiUmVxdWlyZXMgY2xhc3NpZmllciIsIkd1aWRhbmNlIGZvcm11bGEiLCJGSUQgKEltYWdlTmV0IDI1NikiLCJEaXZlcnNpdHkiLCJQcmFjdGljYWwgY29tcGxleGl0eSJdLCJyb3dzIjpbWyJVbmNvbmRpdGlvbmFsIEREUE0iLCJObyIsIs61X864KHhfdCwgdCkgb25seSIsIn4yNiAoY2xhc3MtYWdub3N0aWMpIiwiSGlnaCIsIkxvdyDigJQgb25lIG5ldHdvcmsiXSxbIkNsYXNzaWZpZXIgR3VpZGFuY2UgKHM9MykiLCJZZXMg4oCUIG5vaXN5IGNsYXNzaWZpZXIiLCLOtV/OuCDiiJIgc8K34oiaKDHiiJLhvrEpwrfiiIcgbG9nIHAoeXx4X3QpIiwifjQuNiAoQURNK2d1aWRhbmNlKSIsIk1lZGl1bSIsIkhpZ2gg4oCUIHR3byBuZXR3b3JrcywgZ3JhZCBhdCBlYWNoIHN0ZXAiXSxbIkNGRyAodz03KSIsIk5vIOKAlCBqb2ludCBtb2RlbCIsIs61X3VuY29uZCArIHfCtyjOtV9jb25kIOKIkiDOtV91bmNvbmQpIiwifjMuOCAoTERNKSIsIk1lZGl1bSIsIkxvdyDigJQgb25lIG5ldHdvcmssIHR3byBmb3J3YXJkIHBhc3NlcyJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJHcmFkaWVudCBRdWFsaXR5IERlZ3JhZGVzIGF0IEhpZ2ggTm9pc2UiLCJjb250ZW50IjoiQ2xhc3NpZmllciBncmFkaWVudHMg4oiHX3t4X3R9IGxvZyBwX8+GKHl8eF90KSBiZWNvbWUgdW5yZWxpYWJsZSBhdCBoaWdoIG5vaXNlIGxldmVscyAodCBjbG9zZSB0byBUKSB3aGVyZSB4X3QgaXMgbmVhcmx5IHB1cmUgbm9pc2UuIElmIHlvdSBzZWUgZGl2ZXJnaW5nIHNhbXBsZXMgb3IgTmFOIG91dHB1dHMsIGNoZWNrIHRoZSBncmFkaWVudCBtYWduaXR1ZGUgYXQgaGlnaCB0IOKAlCBjb25zaWRlciBjbGlwcGluZyB0aGUgZ3VpZGFuY2Ugc2lnbmFsIChlLmcuIGNsYW1wIGdyYWRpZW50IG5vcm0gdG8gMS4wKSBmb3IgdGhlIGZpcnN0IDIwJSBvZiBkZW5vaXNpbmcgc3RlcHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJDbGFzc2lmaWVyIGd1aWRhbmNlIHNhbXBsZXMgZnJvbSBwKHh8eSkg4oidIHAoeCnCt3AoeXx4KSDigJQgdGhlb3JldGljYWxseSBncm91bmRlZCBCYXllc2lhbiBjb25kaXRpb25pbmcuIiwiVGhlIG5vaXN5IGNsYXNzaWZpZXIgbXVzdCBiZSB0cmFpbmVkIG9uIHt4X3QsIHR9IHBhaXJzIGFjcm9zcyBhbGwgdCDigJQgdHJhaW5pbmcgb24gb25seSBjbGVhbiBpbWFnZXMgZmFpbHMuIiwiR3VpZGFuY2Ugc2NhbGUgcyBcdTAwM2UgMSBhbXBsaWZpZXMgY2xhc3Mgc2lnbmFsIGJleW9uZCB0aGUgdHJhaW5pbmcgZGlzdHJpYnV0aW9uLCB0cmFkaW5nIHJlY2FsbCBmb3IgcHJlY2lzaW9uLiIsIkFETSArIGNsYXNzaWZpZXIgZ3VpZGFuY2UgZmlyc3QgYmVhdCBHQU5zIG9uIEltYWdlTmV0IDI1NsOXMjU2IChGSUQgNC41OSB2cyBCaWdHQU4tZGVlcCA2Ljk1KS4iLCJFdmVyeSBzdGVwIHJlcXVpcmVzIGF1dG9ncmFkIHRocm91Z2ggdGhlIGNsYXNzaWZpZXIg4oCUIGFkZHMgfjUwJSBjb21wdXRlIHZzIHVuY29uZGl0aW9uYWwgc2FtcGxpbmcuIiwiQ2xhc3NpZmllci1mcmVlIGd1aWRhbmNlIChDRkcpIGFjaGlldmVzIHNpbWlsYXIgb3IgYmV0dGVyIHF1YWxpdHkgd2l0aG91dCBhIHNlcGFyYXRlIGNsYXNzaWZpZXIuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Classifier Guidance — Conditional Generation via Gradient Steering

Classifier guidance (Dhariwal & Nichol 2021) was the first method to reliably push class-conditional diffusion models past GANs on ImageNet. The core idea: sample from p(x|y) ∝ p(x)·p(y|x) by steering each denoising step with the gradient of a classifier. The unconditional diffusion model provides the score ∇_x log p(x), while a separately trained classifier provides ∇_x log p(y|x). Combining them yields the conditional score — no conditional retraining of the diffusion model is required.

## Conditional Generation via Bayes' Rule

The conditional distribution p(x|y) = p(x)·p(y|x)/p(y). Taking log-gradients: ∇_x log p(x|y) = ∇_x log p(x) + ∇_x log p(y|x). The first term is the unconditional score (provided by the diffusion model); the second is the classifier gradient at x. At each denoising step t, we work with the noisy versions: ∇_{x_t} log p(x_t|y) = ∇_{x_t} log p_t(x_t) + ∇_{x_t} log p_φ(y|x_t). The modified epsilon is then ε̃ = ε_θ(x_t,t) − √(1−ᾱ_t)·s·∇_{x_t} log p_φ(y|x_t), where s > 1 is the guidance scale.

## Noisy Classifier Training

The classifier p_φ(y|x_t) must be trained on noisy images at all noise levels t, not clean images. A classifier trained on clean images cannot provide reliable gradients in high-noise regions where x_t looks like pure noise. During training, the noise level t is sampled uniformly, x_t = √ᾱ_t·x + √(1−ᾱ_t)·ε is computed, and the classifier predicts the class from x_t. This trains the classifier to extract class signal from corrupted inputs across the full noise spectrum, enabling meaningful gradient signals at every denoising step.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class NoisyClassifier(nn.Module):
    def __init__(self, in_dim=32, n_classes=10, T=1000):
        super().__init__()
        self.time_embed = nn.Embedding(T, 16)
        self.net = nn.Sequential(
            nn.Linear(in_dim + 16, 128), nn.SiLU(),
            nn.Linear(128, 64), nn.SiLU(),
            nn.Linear(64, n_classes)
        )
    def forward(self, x_t, t):
        t_emb = self.time_embed(t)
        return self.net(torch.cat([x_t, t_emb], dim=-1))

def train_noisy_classifier(clf, data, labels, alpha_bar, n_steps=300):
    opt = torch.optim.Adam(clf.parameters(), lr=1e-3)
    T = len(alpha_bar)
    for step in range(n_steps):
        idx = torch.randint(0, len(data), (64,))
        x0, y = data[idx], labels[idx]
        t = torch.randint(0, T, (64,))
        eps = torch.randn_like(x0)
        ab = alpha_bar[t].unsqueeze(1)
        x_t = torch.sqrt(ab) * x0 + torch.sqrt(1 - ab) * eps
        logits = clf(x_t, t)
        loss = F.cross_entropy(logits, y)
        opt.zero_grad(); loss.backward(); opt.step()
        if step % 100 == 0:
            print(f'Step {step}: classifier loss = {loss.item():.4f}')
    return clf

torch.manual_seed(0)
alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
data = torch.randn(500, 32)
labels = torch.randint(0, 10, (500,))
clf = NoisyClassifier(in_dim=32)
train_noisy_classifier(clf, data, labels, alpha_bar, n_steps=300)
```

## Classifier Guidance in the Denoising Loop

At each denoising step, the classifier gradient steers the epsilon prediction toward higher class probability. The perturbed epsilon is: ε̃ = ε_θ(x_t,t) − s·√(1−ᾱ_t)·∇_{x_t} log p_φ(y|x_t). The factor √(1−ᾱ_t) converts the gradient from x-space to epsilon-space (since ε and ∇_{x_t} log p_t are related by this factor). The guidance scale s > 1 amplifies the class signal beyond what the training distribution supports, trading diversity for fidelity. For s=1 this reduces to simple Bayesian conditioning; for s=5–10 the mode-seeking effect is strong.

```python
import torch
import torch.nn as nn

@torch.no_grad()
def guided_sampling(eps_model, classifier, y, alpha_bar,
                    timesteps, guidance_scale=3.0, shape=(4, 32)):
    """Classifier-guided DDPM sampling loop."""
    x = torch.randn(shape)
    B = shape[0]
    for t in timesteps:
        ab_t = alpha_bar[t]
        ab_prev = alpha_bar[t - 1] if t > 0 else torch.tensor(1.0)
        t_batch = torch.full((B,), t, dtype=torch.long)
        # Unconditional score (epsilon prediction)
        eps_uncond = eps_model(x, t_batch)
        # Classifier gradient
        x_grad = x.detach().requires_grad_(True)
        with torch.enable_grad():
            logits = classifier(x_grad, t_batch)
            log_prob = logits.log_softmax(dim=-1)[range(B), y]
            grad = torch.autograd.grad(log_prob.sum(), x_grad)[0]
        # Perturb epsilon by classifier gradient
        eps_guided = eps_uncond - guidance_scale * torch.sqrt(1 - ab_t) * grad.detach()
        # Standard DDPM reverse step
        coef1 = 1.0 / torch.sqrt(1 - alpha_bar[t] / ab_prev)
        x_prev_mean = coef1 * (x - (1 - ab_t/ab_prev) / torch.sqrt(1 - ab_t) * eps_guided)
        noise = torch.randn_like(x) * torch.sqrt(1 - ab_prev) if t > 0 else 0.0
        x = x_prev_mean + noise
    return x

print('Classifier guidance: steer eps at each step by classifier log-prob gradient')
```

## ADM Architecture

Dhariwal & Nichol (2021) also introduced ADM (Ablated Diffusion Model) — a U-Net with adaptive group normalization, attention at multiple resolutions, and BigGAN residual blocks. ADM with classifier guidance achieved FID 4.59 on ImageNet 256×256, surpassing the best GANs (BigGAN-deep: FID 6.95). Key architectural improvements: attention heads with 64 channels instead of 128, multi-resolution attention (32×32, 16×16, 8×8), and increased depth. These architectural gains combined with classifier guidance established diffusion models as the new state-of-the-art on high-resolution class-conditional synthesis.

## Guidance Scale Trade-off

The guidance scale s controls the fidelity-diversity trade-off. At s=1, samples are drawn from the true conditional distribution p(x|y). At s > 1, the sampling steers beyond the support of the training distribution toward high-class-probability modes. FID improves with s up to a point (typically s=2–5 for ImageNet), then degrades as samples become over-sharpened artifacts with unnatural colors. Inception Score (IS) measures class fidelity and keeps increasing with s. The s that minimizes FID ≠ the s that maximizes IS — practitioners plot both curves.

```python
import torch
import torch.nn as nn
import numpy as np

def simulate_guidance_tradeoff(guidance_scales, n_samples=200, seed=0):
    """Simulate FID vs IS tradeoff as guidance scale increases."""
    torch.manual_seed(seed)
    results = []
    for s in guidance_scales:
        # Simulate quality (lower variance = higher fidelity but less diverse)
        # At s=1: diverse but impure modes; at high s: mode-collapsed
        rng = np.random.RandomState(seed)
        # FID: U-shaped around optimal guidance
        fid = 10.0 + (s - 3.5) ** 2 * 1.2 + rng.randn() * 0.3
        # IS: monotonically increases with guidance (class fidelity)
        inception_score = 20.0 + 8.0 * np.log(s + 1) + rng.randn() * 0.5
        # Diversity (recall): decreases with guidance
        recall = 0.60 * np.exp(-0.15 * (s - 1)) + rng.randn() * 0.02
        results.append((s, max(fid, 1.0), inception_score, max(recall, 0.05)))
    return results

scales = [1, 1.5, 2, 3, 4, 5, 7, 10]
print(f'{"Scale":>6} | {"FID":>6} | {"IS":>8} | {"Recall":>7}')
print('-' * 36)
for s, fid, IS, rec in simulate_guidance_tradeoff(scales):
    print(f'{s:6.1f} | {fid:6.2f} | {IS:8.2f} | {rec:7.3f}')
```

## Unconditional vs Guided Generation

```python
import torch
import torch.nn as nn
import numpy as np

def compare_guidance(eps_model, classifier, alpha_bar, n_steps=50, D=16, B=8):
    """Compare unconditional vs guided sampling at same NFE budget."""
    timesteps = list(range(0, 1000, 1000 // n_steps))[::-1]
    y = torch.zeros(B, dtype=torch.long)  # class 0

    def sample(guidance_scale):
        torch.manual_seed(42)
        x = torch.randn(B, D)
        for t in timesteps:
            ab = alpha_bar[t]
            t_b = torch.full((B,), t, dtype=torch.long)
            eps = eps_model(x, t_b)
            if guidance_scale > 1.0:
                x_g = x.detach().requires_grad_(True)
                with torch.enable_grad():
                    lp = classifier(x_g, t_b).log_softmax(-1)[range(B), y]
                    grad = torch.autograd.grad(lp.sum(), x_g)[0].detach()
                eps = eps - guidance_scale * torch.sqrt(1 - ab) * grad
            ab_p = alpha_bar[max(t-20, 0)]
            x0 = (x - torch.sqrt(1-ab)*eps) / torch.sqrt(ab)
            x = torch.sqrt(ab_p)*x0.clamp(-1,1) + torch.sqrt(1-ab_p)*eps
        return x

    for s in [1.0, 3.0, 7.0]:
        out = sample(s)
        print(f'guidance_scale={s:4.1f}: norm={out.norm():.2f} std={out.std():.3f}')

class DummyEps(nn.Module):
    def forward(self, x, t): return x * 0.05
class DummyClf(nn.Module):
    def forward(self, x, t): return x[:, :10]  # treat first 10 dims as logits
alpha_bar = torch.cumprod(1 - torch.linspace(1e-4, 0.02, 1000), dim=0)
compare_guidance(DummyEps(), DummyClf(), alpha_bar)
```

## Limitations of Classifier Guidance

Classifier guidance has three practical limitations: (1) It requires a separately trained noisy classifier — double the training cost and complexity. (2) Every denoising step requires a gradient computation through the classifier (torch.autograd.grad), adding ~50% compute per step. (3) The classifier is trained on noisy images which is an unusual distribution — small training bugs can produce misleading gradients. These limitations motivated classifier-free guidance (Ho & Salimans 2022), which achieves the same effect using a single network with conditioning dropout.

| Method | Requires classifier | Guidance formula | FID (ImageNet 256) | Diversity | Practical complexity |
| --- | --- | --- | --- | --- | --- |
| Unconditional DDPM | No | ε_θ(x_t, t) only | ~26 (class-agnostic) | High | Low — one network |
| Classifier Guidance (s=3) | Yes — noisy classifier | ε_θ − s·√(1−ᾱ)·∇ log p(y|x_t) | ~4.6 (ADM+guidance) | Medium | High — two networks, grad at each step |
| CFG (w=7) | No — joint model | ε_uncond + w·(ε_cond − ε_uncond) | ~3.8 (LDM) | Medium | Low — one network, two forward passes |

> **Gradient Quality Degrades at High Noise**: Classifier gradients ∇_{x_t} log p_φ(y|x_t) become unreliable at high noise levels (t close to T) where x_t is nearly pure noise. If you see diverging samples or NaN outputs, check the gradient magnitude at high t — consider clipping the guidance signal (e.g. clamp gradient norm to 1.0) for the first 20% of denoising steps.

- Classifier guidance samples from p(x|y) ∝ p(x)·p(y|x) — theoretically grounded Bayesian conditioning.
- The noisy classifier must be trained on {x_t, t} pairs across all t — training on only clean images fails.
- Guidance scale s > 1 amplifies class signal beyond the training distribution, trading recall for precision.
- ADM + classifier guidance first beat GANs on ImageNet 256×256 (FID 4.59 vs BigGAN-deep 6.95).
- Every step requires autograd through the classifier — adds ~50% compute vs unconditional sampling.
- Classifier-free guidance (CFG) achieves similar or better quality without a separate classifier.

---

