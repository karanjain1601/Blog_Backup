---
title: "KV Cache in Transformer Inference"
slug: "kv-cache"
description: "Caching key and value projections from previous tokens to avoid recomputation during autoregressive decoding, reducing complexity from O(n^2) per step to O(n)."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEtWIGNhY2hlIGlzIHRoZSBwcmltYXJ5IG9wdGltaXphdGlvbiB0aGF0IG1ha2VzIGF1dG9yZWdyZXNzaXZlIHRyYW5zZm9ybWVyIGluZmVyZW5jZSBwcmFjdGljYWwgYXQgc2NhbGUuIER1cmluZyB0aGUgcHJlZmlsbCBwaGFzZSwgdGhlIG1vZGVsIGNvbXB1dGVzIGtleSAoSykgYW5kIHZhbHVlIChWKSBwcm9qZWN0aW9ucyBmb3IgZXZlcnkgaW5wdXQgdG9rZW4gaW4gb25lIHBhcmFsbGVsIGZvcndhcmQgcGFzcy4gV2l0aG91dCBjYWNoaW5nLCBlYWNoIHN1YnNlcXVlbnQgZGVjb2RlIHN0ZXAgd291bGQgcmVjb21wdXRlIHRoZXNlIHByb2plY3Rpb25zIGZvciBhbGwgcHJldmlvdXMgdG9rZW5zIOKAlCBhbiBPKG4pIG9wZXJhdGlvbiBwZXIgc3RlcCByZXBlYXRlZCBuIHRpbWVzLCBnaXZpbmcgTyhuXjIpIHRvdGFsIHdvcmsgb3ZlciBhbiBuLXRva2VuIGdlbmVyYXRpb24uIEJ5IHN0b3JpbmcgdGhlIEsgYW5kIFYgdGVuc29ycyBhZnRlciBwcmVmaWxsIGFuZCByZXVzaW5nIHRoZW0gaW4gYWxsIHN1YnNlcXVlbnQgZGVjb2RlIHN0ZXBzLCB0aGUgbW9kZWwgcmVkdWNlcyBlYWNoIGRlY29kZSBzdGVwIHRvIGNvbXB1dGluZyBvbmx5IG9uZSBuZXcgcGFpciBvZiBLLCBWIHByb2plY3Rpb25zIGZvciB0aGUgbmV3bHkgZ2VuZXJhdGVkIHRva2VuLCB0aGVuIGNvbmNhdGVuYXRpbmcgdGhlbSB3aXRoIHRoZSBjYWNoZS4gVGhpcyBkcm9wcyBwZXItc3RlcCBhdHRlbnRpb24gZnJvbSBPKG5eMikgdG8gTyhuKSBpbiBzZXF1ZW5jZSBsZW5ndGguIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRyYW5zZm9ybWVyIGF0dGVudGlvbiBjb21wdXRlcyBBdHRlbnRpb24oUSwgSywgVikgPSBzb2Z0bWF4KFFLXlQgLyBzcXJ0KGRfaykpIFYuIEluIGF1dG9yZWdyZXNzaXZlIGRlY29kaW5nLCBlYWNoIGdlbmVyYXRlZCB0b2tlbiB0IG11c3QgYXR0ZW5kIHRvIGFsbCB0LTEgcHJldmlvdXMgdG9rZW5zIHBsdXMgaXRzZWxmLiBXaXRob3V0IGNhY2hpbmcsIGdlbmVyYXRpbmcgdG9rZW4gdCByZXF1aXJlcyBjb21wdXRpbmcgS19pIGFuZCBWX2kgZm9yIGV2ZXJ5IHByaW9yIHRva2VuIGksIHdoaWNoIGlzIHdhc3RlZnVsIHNpbmNlIEtfaSBhbmQgVl9pIGFyZSBkZXRlcm1pbmlzdGljIGZ1bmN0aW9ucyBvZiBmaXhlZCBwcmV2aW91cyBpbnB1dCB0b2tlbnMgYW5kIG5ldmVyIGNoYW5nZS4gVGhlIEtWIGNhY2hlIHN0b3JlcyBLX2kgYW5kIFZfaSBhZnRlciB0aGVpciBmaXJzdCBjb21wdXRhdGlvbiBhbmQgcmV1c2VzIHRoZW0gaW5kZWZpbml0ZWx5LiBBdCBlYWNoIGRlY29kZSBzdGVwLCBvbmx5IHRoZSBuZXcgdG9rZW5cdTAwMjdzIFEsIEssIFYgYXJlIGNvbXB1dGVkIGZyb20gdGhlIG5ldyB0b2tlbiBlbWJlZGRpbmc7IHRoZSBuZXcgSyBhbmQgViBhcmUgYXBwZW5kZWQgdG8gdGhlIGNhY2hlLCBhbmQgYXR0ZW50aW9uIHJ1bnMgYWdhaW5zdCB0aGUgZnVsbCBjYWNoZWQgc2VxdWVuY2UuIFRoaXMgaXMgYSBwdXJlIGFsZ29yaXRobWljIG9wdGltaXphdGlvbiDigJQgY29ycmVjdG5lc3MgaXMgaWRlbnRpY2FsIHRvIHRoZSB1bmNhY2hlZCB2ZXJzaW9uLCB3aXRoIG5vIGFwcHJveGltYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJlZmlsbCB2cyBEZWNvZGUgUGhhc2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxMTSBpbmZlcmVuY2UgaGFzIHR3byBjb21wdXRhdGlvbmFsbHkgZGlzdGluY3QgcGhhc2VzLiBUaGUgcHJlZmlsbCBwaGFzZSBwcm9jZXNzZXMgdGhlIGVudGlyZSBwcm9tcHQgaW4gYSBzaW5nbGUgcGFyYWxsZWwgZm9yd2FyZCBwYXNzLiBBbGwgdG9rZW4gcG9zaXRpb25zIGFyZSBrbm93biwgc28gYXR0ZW50aW9uIGNhbiBiZSBjb21wdXRlZCBhcyBhIGRlbnNlIG1hdHJpeCBtdWx0aXBsaWNhdGlvbiBhY3Jvc3MgYWxsIHBvc2l0aW9ucyBzaW11bHRhbmVvdXNseS4gUHJlZmlsbCBpcyBjb21wdXRlLWJvdW5kOiBhcml0aG1ldGljIGludGVuc2l0eSAoRkxPUHMgcGVyIGJ5dGUgb2YgbWVtb3J5IGJhbmR3aWR0aCkgaXMgaGlnaCwgYW5kIG1vZGVybiBHUFVzIGFjaGlldmUgY2xvc2UgdG8gcGVhayBGTE9QIHV0aWxpemF0aW9uLiBUaGUgZGVjb2RlIHBoYXNlIGdlbmVyYXRlcyB0b2tlbnMgb25lIGF0IGEgdGltZSBhdXRvcmVncmVzc2l2ZWx5LiBFYWNoIHN0ZXAgaXMgbWVtb3J5LWJhbmR3aWR0aC1ib3VuZDogdGhlIEdQVSBtdXN0IHJlYWQgdGhlIGZ1bGwgbW9kZWwgd2VpZ2h0cyBhbmQgdGhlIGZ1bGwgS1YgY2FjaGUgZnJvbSBIQk0gKEhpZ2gtQmFuZHdpZHRoIE1lbW9yeSkgdG8gY29tcHV0ZSBhIHNpbmdsZSBvdXRwdXQgdG9rZW4uIE9uIGFuIEExMDAgODBHQiBHUFUgd2l0aCAyIFRCL3MgbWVtb3J5IGJhbmR3aWR0aCwgcmVhZGluZyBhIDcwQiBwYXJhbWV0ZXIgbW9kZWwgaW4gYmZsb2F0MTYgKH4xNDAgR0IpIHBsdXMgYSAzMiBHQiBLViBjYWNoZSB0YWtlcyB+ODZtcyBwZXIgc3RlcCDigJQgc2V0dGluZyBhIGhhcmQgZmxvb3Igb24gdG9rZW4gZ2VuZXJhdGlvbiBsYXRlbmN5LiBUaGlzIGZ1bmRhbWVudGFsIGFzeW1tZXRyeSBtb3RpdmF0ZXMgc2VwYXJhdGUgb3B0aW1pemF0aW9uIHN0cmF0ZWdpZXM6IG1heGltaXplIGJhdGNoIHNpemUgZHVyaW5nIHByZWZpbGwgKGhpZ2hlciBhcml0aG1ldGljIGludGVuc2l0eSksIG1pbmltaXplIEtWIGNhY2hlIHNpemUgYW5kIG1heGltaXplIGJhdGNoIHNpemUgZHVyaW5nIGRlY29kZSAoaGlnaGVyIGJhbmR3aWR0aCB1dGlsaXphdGlvbikuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS1YgQ2FjaGUgTWVjaGFuaWNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdCBlYWNoIHRyYW5zZm9ybWVyIGxheWVyLCB0aGUgS1YgY2FjaGUgbWFpbnRhaW5zIHR3byB0ZW5zb3JzOiBLX2NhY2hlIGFuZCBWX2NhY2hlLCBlYWNoIG9mIHNoYXBlIChiYXRjaF9zaXplLCBuX2t2X2hlYWRzLCBzZXFfbGVuLCBoZWFkX2RpbSkuIEF0IGRlY29kZSBzdGVwIHQsIHRoZSBuZXcgdG9rZW4gZW1iZWRkaW5nIHBhc3NlcyB0aHJvdWdoIHRoZSBRLCBLLCBWIHByb2plY3Rpb24gbWF0cmljZXMgdG8gcHJvZHVjZSBxX3QsIGtfdCwgdl90LCBlYWNoIG9mIHNoYXBlIChic3osIG5fa3ZfaGVhZHMsIDEsIGhlYWRfZGltKS4ga190IGFuZCB2X3QgYXJlIGFwcGVuZGVkIHRvIHRoZSBjYWNoZTogS19mdWxsID0gY2F0KFtLX2NhY2hlLCBrX3RdLCBkaW09MikuIEF0dGVudGlvbiB0aGVuIHJ1bnMgYWdhaW5zdCBLX2Z1bGwgYW5kIFZfZnVsbCB3aXRoIHRoZSBxdWVyeSBxX3QsIHByb2R1Y2luZyBvdXRwdXQgb2Ygc2hhcGUgKGJzeiwgbl9oZWFkcywgMSwgaGVhZF9kaW0pLiBUaGlzIG91dHB1dCBpcyBwcm9qZWN0ZWQgYW5kIGFkZGVkIHRvIHRoZSByZXNpZHVhbCBzdHJlYW0uIFRoZSB1cGRhdGVkIGNhY2hlLCBub3cgY29udGFpbmluZyBzZXFfbGVuICsgMSBlbnRyaWVzLCBpcyBwYXNzZWQgdG8gdGhlIG5leHQgZGVjb2RlIHN0ZXAuIEFjcm9zcyBhbGwgTCBsYXllcnMsIHRoaXMgbWVhbnMgdGhlIG1vZGVsIG1haW50YWlucyAyICogTCBLViBjYWNoZSB0ZW5zb3JzIHNpbXVsdGFuZW91c2x5LiBUaGUgdG90YWwgbWVtb3J5IGlzIHByb3BvcnRpb25hbCB0byBMICogbl9rdl9oZWFkcyAqIGhlYWRfZGltICogYmF0Y2hfc2l6ZSAqIHNlcV9sZW4gKiAyICogZHR5cGVfYnl0ZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcbmltcG9ydCB0aW1lXG5cbmRlZiBkZWNvZGVfc3RlcF93aXRoX2NhY2hlKHFfbmV3LCBrX25ldywgdl9uZXcsIGt2X2NhY2hlPU5vbmUpOlxuICAgIFwiXCJcIlxuICAgIFNpbmdsZSBhdXRvcmVncmVzc2l2ZSBkZWNvZGUgc3RlcCB1c2luZyBhIEtWIGNhY2hlIGRpY3QuXG4gICAgcV9uZXcsIGtfbmV3LCB2X25ldzogKGJzeiwgMSwgaGVhZF9kaW0pIHRlbnNvcnMgZm9yIHRoZSBuZXcgdG9rZW4uXG4gICAga3ZfY2FjaGU6IGRpY3Qge1x1MDAyN2tcdTAwMjc6IChic3osIHBhc3RfbGVuLCBkKSwgXHUwMDI3dlx1MDAyNzogKGJzeiwgcGFzdF9sZW4sIGQpfSBvciBOb25lLlxuICAgIFJldHVybnMgKG91dHB1dCwgdXBkYXRlZF9rdl9jYWNoZSkuIENhY2hlIGdyb3dzIGJ5IDEgcG9zaXRpb24gZWFjaCBzdGVwLlxuICAgIENvbXBsZXhpdHk6IE8obikgcGVyIHN0ZXAgd2l0aCBjYWNoZSB2cyBPKG5eMikgdG90YWwgd2l0aG91dC5cbiAgICBcIlwiXCJcbiAgICBpZiBrdl9jYWNoZSBpcyBub3QgTm9uZTpcbiAgICAgICAgayA9IHRvcmNoLmNhdChba3ZfY2FjaGVbXHUwMDI3a1x1MDAyN10sIGtfbmV3XSwgZGltPTEpICAjIChic3osIHBhc3QrMSwgaGVhZF9kaW0pXG4gICAgICAgIHYgPSB0b3JjaC5jYXQoW2t2X2NhY2hlW1x1MDAyN3ZcdTAwMjddLCB2X25ld10sIGRpbT0xKVxuICAgIGVsc2U6XG4gICAgICAgIGssIHYgPSBrX25ldywgdl9uZXdcbiAgICBuZXdfY2FjaGUgPSB7XHUwMDI3a1x1MDAyNzogaywgXHUwMDI3dlx1MDAyNzogdn1cbiAgICBzY2FsZSA9IG1hdGguc3FydChxX25ldy5zaGFwZVstMV0pXG4gICAgc2NvcmVzID0gdG9yY2guYm1tKHFfbmV3LCBrLnRyYW5zcG9zZSgxLCAyKSkgLyBzY2FsZSAgIyAoYnN6LCAxLCBzZXFfbGVuKVxuICAgIGF0dG4gPSBGLnNvZnRtYXgoc2NvcmVzLCBkaW09LTEpXG4gICAgb3V0cHV0ID0gdG9yY2guYm1tKGF0dG4sIHYpICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKGJzeiwgMSwgaGVhZF9kaW0pXG4gICAgcmV0dXJuIG91dHB1dCwgbmV3X2NhY2hlXG5cbiMgQmVuY2htYXJrIDIwMC1zdGVwIGRlY29kZSB3aXRoIEtWIGNhY2hlXG5ic3osIGhlYWRfZGltLCBuX3N0ZXBzID0gMSwgNjQsIDIwMFxuY2FjaGUgPSBOb25lXG50MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbmZvciBzdGVwIGluIHJhbmdlKG5fc3RlcHMpOlxuICAgIHEgPSB0b3JjaC5yYW5kbihic3osIDEsIGhlYWRfZGltKVxuICAgIG91dCwgY2FjaGUgPSBkZWNvZGVfc3RlcF93aXRoX2NhY2hlKHEsIHEuY2xvbmUoKSwgcS5jbG9uZSgpLCBjYWNoZSlcbmVsYXBzZWQgPSAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAqIDEwMDBcbnByaW50KGZcIkRlY29kZWQge25fc3RlcHN9IHRva2VucyB3aXRoIGNhY2hlIGluIHtlbGFwc2VkOi4xZn1tc1wiKVxucHJpbnQoZlwiRmluYWwgS1YgY2FjaGUgc2hhcGU6IHtjYWNoZVtcdTAwMjdrXHUwMDI3XS5zaGFwZX1cIikgICMgKDEsIDIwMCwgNjQpXG5wcmludChcIktWIGNhY2hlOiBPKG4pIHBlciBzdGVwIC0tIGVsaW1pbmF0ZXMgcmVkdW5kYW50IEssViByZWNvbXB1dGF0aW9uLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1lbW9yeSBGb290cHJpbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IktWIGNhY2hlIG1lbW9yeSBpcyB0aGUgcHJvZHVjdCBvZiBzaXggZmFjdG9yczogMiAoSyBhbmQgVikgw5cgbGF5ZXJzIMOXIEtWX2hlYWRzIMOXIGhlYWRfZGltIMOXIGJhdGNoX3NpemUgw5cgc2VxX2xlbiDDlyBkdHlwZV9ieXRlcy4gRm9yIExMYU1BLTMtOEIgKDMyIGxheWVycywgOCBHUUEgaGVhZHMsIGhlYWRfZGltPTEyOCkgaW4gYmZsb2F0MTYgYXQgYmF0Y2g9MSwgc2VxPTQwOTY6IDIgw5cgMzIgw5cgOCDDlyAxMjggw5cgMSDDlyA0MDk2IMOXIDIgPSA1MzYgTUIuIEF0IGJhdGNoPTMyLCBzZXE9ODE5MjogMiDDlyAzMiDDlyA4IMOXIDEyOCDDlyAzMiDDlyA4MTkyIMOXIDIgPSAzNC40IEdCLiBGb3IgTExhTUEtMy03MEIgKDgwIGxheWVycywgOCBHUUEgaGVhZHMsIGhlYWRfZGltPTEyOCkgYXQgYmF0Y2g9MzIsIHNlcT04MTkyOiA4NiBHQiDigJQgbW9yZSB0aGFuIHRoZSBtb2RlbCB3ZWlnaHRzIG9uIGEgc2luZ2xlIEExMDAuIEtWIGNhY2hlIGFsbG9jYXRpb24gbXVzdCBiZSBwbGFubmVkIGFzIHBhcnQgb2YgR1BVIG1lbW9yeSBidWRnZXRpbmc6IGEgdHlwaWNhbCBkZXBsb3ltZW50IGFsbG9jYXRlcyBtb2RlbCB3ZWlnaHRzIGZpcnN0LCB0aGVuIHJlc2VydmVzIHJlbWFpbmluZyBHUFUgbWVtb3J5IGZvciBLViBjYWNoZS4gVGhlIEtWIGNhY2hlIHNpemUgZGV0ZXJtaW5lcyB0aGUgbWF4aW11bSBhY2hpZXZhYmxlIGJhdGNoIHNpemUgYW5kIHNlcXVlbmNlIGxlbmd0aCBzaW11bHRhbmVvdXNseSDigJQgZW5naW5lZXJzIG11c3QgY2hvb3NlIGNhcmVmdWxseSBiYXNlZCBvbiBleHBlY3RlZCB3b3JrbG9hZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHR5cGluZyBpbXBvcnQgRGljdCwgVHVwbGVcblxuZGVmIGNvbXB1dGVfa3ZfY2FjaGVfYnl0ZXMoXG4gICAgbl9sYXllcnM6IGludCxcbiAgICBuX2t2X2hlYWRzOiBpbnQsXG4gICAgaGVhZF9kaW06IGludCxcbiAgICBiYXRjaF9zaXplOiBpbnQsXG4gICAgc2VxX2xlbjogaW50LFxuICAgIGR0eXBlX2J5dGVzOiBpbnQgPSAyLCAgIyAyID0gYmZsb2F0MTYvZmxvYXQxNiwgNCA9IGZsb2F0MzJcbikgLVx1MDAzZSBpbnQ6XG4gICAgXCJcIlwiXG4gICAgVG90YWwgS1YgY2FjaGUgbWVtb3J5IGluIGJ5dGVzLlxuICAgIEZvcm11bGE6IDIgKEsrVikgKiBsYXllcnMgKiBrdl9oZWFkcyAqIGhlYWRfZGltICogYmF0Y2ggKiBzZXEgKiBkdHlwZV9ieXRlcy5cbiAgICBcIlwiXCJcbiAgICByZXR1cm4gMiAqIG5fbGF5ZXJzICogbl9rdl9oZWFkcyAqIGhlYWRfZGltICogYmF0Y2hfc2l6ZSAqIHNlcV9sZW4gKiBkdHlwZV9ieXRlc1xuXG4jIE1vZGVsIGNvbmZpZ3MgKEdRQSByZWR1Y2VzIG5fa3ZfaGVhZHMgZmFyIGJlbG93IG5fcXVlcnlfaGVhZHMpXG5jb25maWdzID0ge1xuICAgIFwiTExhTUEtMy04QiAgKEdRQS04KVwiOiAgZGljdChuX2xheWVycz0zMiwgbl9rdl9oZWFkcz04LCAgaGVhZF9kaW09MTI4KSxcbiAgICBcIkxMYU1BLTMtNzBCIChHUUEtOClcIjogIGRpY3Qobl9sYXllcnM9ODAsIG5fa3ZfaGVhZHM9OCwgIGhlYWRfZGltPTEyOCksXG4gICAgXCJNaXN0cmFsLTdCICAoR1FBLTgpXCI6ICBkaWN0KG5fbGF5ZXJzPTMyLCBuX2t2X2hlYWRzPTgsICBoZWFkX2RpbT0xMjgpLFxuICAgIFwiR1BULTIgTGFyZ2UgKE1IQS0xNilcIjogZGljdChuX2xheWVycz0zNiwgbl9rdl9oZWFkcz0xNiwgaGVhZF9kaW09NjQpLFxufVxud2VpZ2h0X2J5dGVzID0ge1wiTExhTUEtMy04QiAgKEdRQS04KVwiOiA4ZTkqMiwgXCJMTGFNQS0zLTcwQiAoR1FBLTgpXCI6IDcwZTkqMixcbiAgICAgICAgICAgICAgICBcIk1pc3RyYWwtN0IgIChHUUEtOClcIjogN2U5KjIsIFwiR1BULTIgTGFyZ2UgKE1IQS0xNilcIjogMC43N2U5KjR9XG5cbnByaW50KGZcIntcdTAwMjdNb2RlbFx1MDAyNzpcdTAwM2MyNn0ge1x1MDAyN2Jzelx1MDAyNzpcdTAwM2U0fSB7XHUwMDI3c2VxXHUwMDI3Olx1MDAzZTZ9IHtcdTAwMjdLViBHQlx1MDAyNzpcdTAwM2U4fSB7XHUwMDI3JSBvZiB3ZWlnaHRzXHUwMDI3Olx1MDAzZTE0fVwiKVxucHJpbnQoXCItXCIgKiA2NClcbmZvciBuYW1lLCBjZmcgaW4gY29uZmlncy5pdGVtcygpOlxuICAgIGZvciBic3osIHNlcSBpbiBbKDEsIDQwOTYpLCAoOCwgNDA5NiksICgzMiwgODE5MildOlxuICAgICAgICBrdiA9IGNvbXB1dGVfa3ZfY2FjaGVfYnl0ZXMoKipjZmcsIGJhdGNoX3NpemU9YnN6LCBzZXFfbGVuPXNlcSlcbiAgICAgICAgcGN0ID0ga3YgLyB3ZWlnaHRfYnl0ZXNbbmFtZV0gKiAxMDBcbiAgICAgICAgcHJpbnQoZlwie25hbWU6XHUwMDNjMjZ9IHtic3o6XHUwMDNlNH0ge3NlcTpcdTAwM2U2fSB7a3YvMWU5Olx1MDAzZTcuMmZ9RyB7cGN0Olx1MDAzZTEzLjFmfSVcIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IktWIENhY2hlIE1lbW9yeSBXYXJuaW5nIiwiY29udGVudCI6IlRoZSBLViBjYWNoZSBncm93cyBsaW5lYXJseSB3aXRoIHNlcXVlbmNlIGxlbmd0aCBhbmQgYmF0Y2ggc2l6ZSDigJQgYSBiYXRjaCBvZiAzMiByZXF1ZXN0cyBhdCA4SyBjb250ZXh0IGNhbiBlYXNpbHkgcmVxdWlyZSA1MCsgR0Igb2YgS1YgY2FjaGUgYWxvbmUgZm9yIGEgNzBCIG1vZGVsLCBiZWZvcmUgZXZlbiBzdG9yaW5nIHRoZSB3ZWlnaHRzLiBPbiBhIHNpbmdsZSBBMTAwIDgwR0IsIHN0b3JpbmcgNzBCIHdlaWdodHMgaW4gYmZsb2F0MTYgY29uc3VtZXMgfjE0MCBHQiBhY3Jvc3MgbXVsdGlwbGUgR1BVczsgS1YgY2FjaGUgbXVzdCBiZSBidWRnZXRlZCBwZXItR1BVIGFjcm9zcyB0aGUgdGVuc29yLXBhcmFsbGVsIHNwbGl0LiBBbHdheXMgcHJvZmlsZSBLViBjYWNoZSBzaXplIGJlZm9yZSBkZXBsb3lpbmcgYXQgYmF0Y2ggc2l6ZXMgbGFyZ2VyIHRoYW4gNC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXR0ZW50aW9uIFR5cGUiLCJLViBIZWFkcyAoMzJMKSIsIkNhY2hlIFNpemUgKHNlcT00MDk2LCBic3o9MSwgZGltPTEyOCkiLCJ2cyBNSEEiLCJOb3RlcyJdLCJyb3dzIjpbWyJNSEEgIChIPTMyKSIsIjMyIiwifjIuMTUgR0IiLCIxLjB4IiwiRnVsbCBwZXItaGVhZCBLLFY7IEdQVC0yIC8gTExhTUEtMSJdLFsiTVFBICAoSD0xKSIsIjEiLCJ+MC4wNjcgR0IiLCIzMnggc21hbGxlciIsIlNoYXJlZCBzaW5nbGUgSyxWOyBQYUxNLCBGYWxjb24tN0IiXSxbIkdRQS04IChIPTgpIiwiOCIsIn4wLjUzNiBHQiIsIjR4IHNtYWxsZXIiLCJMTGFNQS0zIGFsbCBzaXplcywgTWlzdHJhbC03QiJdLFsiR1FBLTQgKEg9NCkiLCI0IiwifjAuMjY4IEdCIiwiOHggc21hbGxlciIsIkFnZ3Jlc3NpdmU7IHZpYWJsZSBhdCAxM0IrIHNjYWxlIl0sWyJHUUEtMiAoSD0yKSIsIjIiLCJ+MC4xMzQgR0IiLCIxNnggc21hbGxlciIsIkV4dHJlbWUgY29tcHJlc3Npb247IHF1YWxpdHkgdHJhZGVvZmYiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik11bHRpLVF1ZXJ5IGFuZCBHcm91cGVkLVF1ZXJ5IEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgTXVsdGktSGVhZCBBdHRlbnRpb24gKE1IQSkgYXNzaWducyBlYWNoIHF1ZXJ5IGhlYWQgaXRzIG93biBLLCBWIHByb2plY3Rpb24gbWF0cmljZXMsIGdpdmluZyBuX2hlYWRzIEtWIGhlYWRzLiBNdWx0aS1RdWVyeSBBdHRlbnRpb24gKE1RQSwgU2hhemVlciAyMDE5KSB1c2VzIGEgc2luZ2xlIHNoYXJlZCBLLCBWIGhlYWQgYWNyb3NzIGFsbCBxdWVyeSBoZWFkcywgcmVkdWNpbmcgS1YgY2FjaGUgYnkgYSBmYWN0b3Igb2Ygbl9oZWFkcy4gRm9yIGEgMzItaGVhZCBtb2RlbCwgTVFBIGN1dHMgS1YgY2FjaGUgMzJ4IGJ1dCBjYW4gZGVncmFkZSBxdWFsaXR5LCBwYXJ0aWN1bGFybHkgb24gdGFza3MgcmVxdWlyaW5nIGRpdmVyc2UgYXR0ZW50aW9uIHBhdHRlcm5zIHBlciBoZWFkLiBHcm91cGVkLVF1ZXJ5IEF0dGVudGlvbiAoR1FBLCBBaW5zbGllIGV0IGFsLiAyMDIzKSBnZW5lcmFsaXplcyBiZXR3ZWVuIE1IQSBhbmQgTVFBOiBHIGdyb3VwcyBvZiBxdWVyeSBoZWFkcyBzaGFyZSBvbmUgSyxWIGhlYWQgZWFjaCwgd2hlcmUgMSBcdTAwM2M9IEcgXHUwMDNjIG5faGVhZHMuIExMYU1BLTMgKDhCLCA3MEIpLCBMTGFNQS0zLjEsIE1pc3RyYWwtN0IsIE1peHRyYWwsIEdlbW1hLCBhbmQgbW9zdCBtb2Rlcm4gb3Blbi1zb3VyY2UgTExNcyB1c2UgR1FBIHdpdGggRz04IEtWIGhlYWRzLiBHUUEgd2l0aCBHPTggYWNoaWV2ZXMgNHggS1YgY2FjaGUgcmVkdWN0aW9uIHZzIE1IQSB3aGlsZSBtYWludGFpbmluZyBuZWFyLU1IQSBxdWFsaXR5IGF0IDdCKyBwYXJhbWV0ZXIgc2NhbGUuIFRoZSBxdWFsaXR5IGRlZ3JhZGF0aW9uIGZyb20gR1FBIGlzIG5lZ2xpZ2libGUgY29tcGFyZWQgdG8gdGhlIG1lbW9yeSBhbmQgdGhyb3VnaHB1dCBiZW5lZml0cywgbWFraW5nIEdRQSB0aGUgZGVmYXVsdCBmb3IgbmV3IGxhcmdlIExMTSBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBtYXRoXG5cbmRlZiBrdl9jYWNoZV9nYihcbiAgICBuX2xheWVyczogaW50LCBuX2t2X2hlYWRzOiBpbnQsIGhlYWRfZGltOiBpbnQsXG4gICAgYmF0Y2hfc2l6ZTogaW50LCBzZXFfbGVuOiBpbnQsIGR0eXBlX2J5dGVzOiBpbnQgPSAyLFxuKSAtXHUwMDNlIGZsb2F0OlxuICAgIFwiXCJcIktWIGNhY2hlIG1lbW9yeSBpbiBHQiAoZmxvYXQxNi9iZmxvYXQxNiBieSBkZWZhdWx0KS5cIlwiXCJcbiAgICByZXR1cm4gKDIgKiBuX2xheWVycyAqIG5fa3ZfaGVhZHMgKiBoZWFkX2RpbVxuICAgICAgICAgICAgKiBiYXRjaF9zaXplICogc2VxX2xlbiAqIGR0eXBlX2J5dGVzKSAvIDFlOVxuXG4jIENvbXBhcmUgTUhBLCBHUUEgdmFyaWFudHMsIGFuZCBNUUEgZm9yIDMyLWxheWVyIG1vZGVsLCBzZXE9NDA5NiwgYnN6PTFcbmJhc2UgPSBkaWN0KG5fbGF5ZXJzPTMyLCBoZWFkX2RpbT0xMjgsIGJhdGNoX3NpemU9MSwgc2VxX2xlbj00MDk2KVxuYXR0ZW50aW9uX3R5cGVzID0gW1xuICAgIChcIk1IQSAgKDMyIEtWIGhlYWRzKVwiLCAgMzIsICBcIkdQVC0yIC8gTGxhbWEtMSBzdHlsZVwiKSxcbiAgICAoXCJHUUEtOCAoOCBLViBoZWFkcylcIiwgICA4LCAgXCJMTGFNQS0zIC8gTWlzdHJhbC03QlwiKSxcbiAgICAoXCJHUUEtNCAoNCBLViBoZWFkcylcIiwgICA0LCAgXCJDdXN0b20gR1FBLTQgY29uZmlnXCIpLFxuICAgIChcIkdRQS0yICgyIEtWIGhlYWRzKVwiLCAgIDIsICBcIkFnZ3Jlc3NpdmUgY29tcHJlc3Npb25cIiksXG4gICAgKFwiTVFBICAgKDEgS1YgaGVhZClcIiwgICAgMSwgIFwiUGFMTSAvIEZhbGNvbi03QiBzdHlsZVwiKSxcbl1cbm1oYV9nYiA9IGt2X2NhY2hlX2diKCoqYmFzZSwgbl9rdl9oZWFkcz0zMilcbnByaW50KGZcIntcdTAwMjdBdHRlbnRpb24gVHlwZVx1MDAyNzpcdTAwM2MyNH0ge1x1MDAyN0tWIEhlYWRzXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3R0JcdTAwMjc6XHUwMDNlOH0ge1x1MDAyN3ZzIE1IQVx1MDAyNzpcdTAwM2UxMH0gIE5vdGVzXCIpXG5wcmludChcIi1cIiAqIDc1KVxuZm9yIGxhYmVsLCBuX2t2LCBub3RlcyBpbiBhdHRlbnRpb25fdHlwZXM6XG4gICAgZ2IgPSBrdl9jYWNoZV9nYigqKmJhc2UsIG5fa3ZfaGVhZHM9bl9rdilcbiAgICByZWR1Y3Rpb24gPSBtaGFfZ2IgLyBnYlxuICAgIHByaW50KGZcIntsYWJlbDpcdTAwM2MyNH0ge25fa3Y6XHUwMDNlMTB9IHtnYjpcdTAwM2U3LjNmfUcge3JlZHVjdGlvbjpcdTAwM2U5LjFmfXggIHtub3Rlc31cIilcbnByaW50KGZcIlxcbkJhc2UgKE1IQSk6IHttaGFfZ2I6LjNmfSBHQiBhdCBzZXE9NDA5NiwgYnN6PTEsIDMyTCwgZGltPTEyOCwgYmYxNlwiKVxucHJpbnQoXCJHUUEtOCByZWR1Y2VzIEtWIGNhY2hlIDR4IHZzIE1IQSB3aXRoIG1pbmltYWwgcXVhbGl0eSBsb3NzIGF0IDdCKyBzY2FsZS5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLViBDYWNoZSBFdmljdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGxvbmctY29udGV4dCBpbmZlcmVuY2Ugd2hlcmUgdGhlIEtWIGNhY2hlIHdvdWxkIGV4Y2VlZCBHUFUgbWVtb3J5LCBldmljdGlvbiBzdHJhdGVnaWVzIHNlbGVjdGl2ZWx5IGRpc2NhcmQgc3RvcmVkIEssIFYgZW50cmllcy4gU3RyZWFtaW5nTExNIChYaWFvIGV0IGFsLiwgMjAyMykga2VlcHMgdGhlIGZpcnN0IGZldyB0b2tlbnMgKGF0dGVudGlvbiBzaW5rcywgdHlwaWNhbGx5IDQpIHBsdXMgYSBzbGlkaW5nIHdpbmRvdyBvZiByZWNlbnQgdG9rZW5zLiBBdHRlbnRpb24gc2luayB0b2tlbnMgcmVjZWl2ZSBkaXNwcm9wb3J0aW9uYXRlIGF0dGVudGlvbiB3ZWlnaHQ7IGRpc2NhcmRpbmcgdGhlbSBjYXVzZXMgaW5zdGFiaWxpdHkuIEtlZXBpbmcgb25seSBzaW5rcyArIHJlY2VudCB0b2tlbnMgKHdpbmRvdyBzaXplIDUxMuKAkzIwNDgpIGVuYWJsZXMgdW5ib3VuZGVkIGNvbnRleHQgYXQgY29uc3RhbnQgbWVtb3J5LiBIMk8gKEhlYXZ5LUhpdHRlciBPcmFjbGUsIFpoYW5nIGV0IGFsLiwgMjAyMykgdHJhY2tzIGN1bXVsYXRpdmUgYXR0ZW50aW9uIHdlaWdodCBwZXIgdG9rZW4gYW5kIGV2aWN0cyB0aG9zZSB3aXRoIHRoZSBsb3dlc3QgYWNjdW11bGF0ZWQgc2NvcmUuIFRva2VucyB0aGF0IHJlcGVhdGVkbHkgcmVjZWl2ZSBoaWdoIGF0dGVudGlvbiAoaGVhdnkgaGl0dGVycykgYXJlIHByZXNlcnZlZDsgcmFyZWx5IGF0dGVuZGVkIHRva2VucyBhcmUgZXZpY3RlZC4gU2Npc3NvckhhbmRzIChMaXUgZXQgYWwuLCAyMDIzKSBtYWludGFpbnMgYSBmaXhlZCBzcGFyc2UgcGF0dGVybiBpZGVudGlmeWluZyBwZXJzaXN0ZW50IGhlYXZ5LWhpdHRlcnMgYWNyb3NzIGdlbmVyYXRpb24gc3RlcHMuIFNuYXBLViAoTGkgZXQgYWwuLCAyMDI0KSBjb21wcmVzc2VzIHRoZSBLViBjYWNoZSBieSBjbHVzdGVyaW5nIHNpbWlsYXIgSyxWIHZlY3RvcnMgd2l0aGluIGEgd2luZG93IGFuZCByZXRhaW5pbmcgcmVwcmVzZW50YXRpdmUgY2VudHJvaWRzLiBBbGwgZXZpY3Rpb24gc3RyYXRlZ2llcyB0cmFkZSBvZmYgcXVhbGl0eSAobG93ZXIgZXZpY3Rpb24gcmF0ZSDihpIgaGlnaGVyIHF1YWxpdHkpIHZzIG1lbW9yeSAoaGlnaGVyIGV2aWN0aW9uIHJhdGUg4oaSIHNtYWxsZXIgY2FjaGUpIHZzIGxhdGVuY3kgKGV2aWN0aW9uIG92ZXJoZWFkIHBlciBzdGVwKS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlN0cmVhbWluZ0xMTToga2VlcCBmaXJzdCA0IGF0dGVudGlvbi1zaW5rIHRva2VucyArIHNsaWRpbmcgd2luZG93ICg1MTItMjA0OCkuIENvbnN0YW50IG1lbW9yeSwgdW5ib3VuZGVkIGNvbnRleHQsIHNtYWxsIHF1YWxpdHkgbG9zcy4iLCJIMk86IHRyYWNrIGN1bXVsYXRpdmUgYXR0ZW50aW9uIG1hc3MgcGVyIHRva2VuLCBldmljdCBsb3dlc3Qtc2NvcmluZyBlbnRyaWVzLiBEeW5hbWljIGFuZCB0YXNrLWFkYXB0aXZlLCB+MS0yJSBxdWFsaXR5IGxvc3MgYXQgNTAlIGV2aWN0aW9uLiIsIlNjaXNzb3JIYW5kczogaWRlbnRpZnkgcGVyc2lzdGVudCBoZWF2eS1oaXR0ZXIgcG9zaXRpb25zOyBldmljdCBub24taGVhdnktaGl0dGVyIHRva2Vucy4gU2ltaWxhciBxdWFsaXR5IHRvIEgyTyB3aXRoIGxvd2VyIHBlci1zdGVwIG92ZXJoZWFkLiIsIlNuYXBLVjogY2x1c3RlciBzaW1pbGFyIEssViB2ZWN0b3JzLCByZXRhaW4gY2VudHJvaWRzLiBHb29kIGNvbXByZXNzaW9uIHJhdGlvICh+NHgpIHdpdGggc3Ryb25nIGxvbmctY29udGV4dCBwZXJmb3JtYW5jZS4iLCJRdWFudGl6ZWQgS1YgY2FjaGUgKElOVDgvSU5UNCk6IHJlZHVjZSBkdHlwZV9ieXRlcyBmcm9tIDIgdG8gMSBvciAwLjUsIGRvdWJsaW5nIGVmZmVjdGl2ZSBiYXRjaCBzaXplIG9yIHNlcXVlbmNlIGxlbmd0aCBhdCBtaW5pbWFsIHF1YWxpdHkgY29zdC4iLCJMYXllci13aXNlIGV2aWN0aW9uOiBkZWVwZXIgbGF5ZXJzIGhhdmUgbG93ZXIgYXR0ZW50aW9uIGVudHJvcHkgYW5kIHRvbGVyYXRlIG1vcmUgYWdncmVzc2l2ZSBldmljdGlvbiB0aGFuIGVhcmx5IGxheWVycy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS1YgQ2FjaGUgaW4gSHVnZ2luZ0ZhY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikh1Z2dpbmdGYWNlIFRyYW5zZm9ybWVycyBpbXBsZW1lbnRzIEtWIGNhY2hpbmcgdmlhIHRoZSBgdXNlX2NhY2hlPVRydWVgIHBhcmFtZXRlciAoZW5hYmxlZCBieSBkZWZhdWx0IGluIGBnZW5lcmF0ZSgpYCkuIFRoZSBtb2RlbCByZXR1cm5zIGBwYXN0X2tleV92YWx1ZXNgLCBhIHR1cGxlIG9mIChLLCBWKSB0dXBsZXMg4oCUIG9uZSBwZXIgbGF5ZXIg4oCUIGFmdGVyIGVhY2ggZm9yd2FyZCBwYXNzLiBJbiBgZ2VuZXJhdGUoKWAsIHBhc3Rfa2V5X3ZhbHVlcyBpcyBwYXNzZWQgYXV0b21hdGljYWxseSBiZXR3ZWVuIGRlY29kZSBzdGVwcy4gU2luY2UgVHJhbnNmb3JtZXJzIHY0LjM2LCB0aGUgYER5bmFtaWNDYWNoZWAgY2xhc3Mgd3JhcHMgcGFzdF9rZXlfdmFsdWVzIHdpdGggYW4gZXhwbGljaXQgYC51cGRhdGUoa2V5X3N0YXRlcywgdmFsdWVfc3RhdGVzLCBsYXllcl9pZHgpYCBBUEksIG1ha2luZyBjYWNoZSBpbnNwZWN0aW9uIGFuZCBtYW5pcHVsYXRpb24gc3RyYWlnaHRmb3J3YXJkLiBTdGF0aWMgY2FjaGVzIChgU3RhdGljQ2FjaGVgKSBwcmUtYWxsb2NhdGUgZml4ZWQtc2l6ZSB0ZW5zb3JzIHRvIGF2b2lkIGR5bmFtaWMgcmVzaXppbmcgb3ZlcmhlYWQgZHVyaW5nIGdlbmVyYXRpb24g4oCUIHVzZWZ1bCBmb3IgcHJvZHVjdGlvbiBzZXJ2aW5nIHdoZXJlIG1heCBzZXF1ZW5jZSBsZW5ndGggaXMga25vd24uIFF1YW50aXplZCBLViBjYWNoZXMgKGBRdWFudG9RdWFudGl6ZWRDYWNoZWApIHN0b3JlIEssViBpbiBJTlQ4IG9yIElOVDQsIGhhbHZpbmcgb3IgcXVhcnRlcmluZyBjYWNoZSBtZW1vcnkgYXQgdGhlIGNvc3Qgb2YgYSBxdWFudGl6YXRpb24vZGVxdWFudGl6YXRpb24gc3RlcCBwZXIgbGF5ZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRpbWVcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplclxuXG5kZWYgYmVuY2htYXJrX2hmX2t2X2NhY2hlKFxuICAgIG1vZGVsX25hbWU6IHN0ciA9IFwiZ3B0MlwiLFxuICAgIHByb21wdDogc3RyID0gXCJUaGUgS1YgY2FjaGUgaXMgYSBrZXkgb3B0aW1pemF0aW9uIGZvciB0cmFuc2Zvcm1lciBpbmZlcmVuY2UgYmVjYXVzZVwiLFxuICAgIG1heF9uZXdfdG9rZW5zOiBpbnQgPSA4MCxcbik6XG4gICAgXCJcIlwiQ29tcGFyZSBIdWdnaW5nRmFjZSBnZW5lcmF0aW9uIHNwZWVkIHdpdGggdnMgd2l0aG91dCBLViBjYWNoZS5cIlwiXCJcbiAgICB0b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgIG1vZGVsID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpLmV2YWwoKVxuICAgIGlucHV0cyA9IHRva2VuaXplcihwcm9tcHQsIHJldHVybl90ZW5zb3JzPVwicHRcIilcbiAgICBpbnB1dF9pZHMgPSBpbnB1dHNbXCJpbnB1dF9pZHNcIl1cblxuICAgICMgSW5zcGVjdCBwYXN0X2tleV92YWx1ZXMgZnJvbSBhIHNpbmdsZSBmb3J3YXJkIHBhc3NcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgZndkID0gbW9kZWwoaW5wdXRfaWRzLCB1c2VfY2FjaGU9VHJ1ZSlcbiAgICBwa3YgPSBmd2QucGFzdF9rZXlfdmFsdWVzICAjIHR1cGxlIG9mIChLLCBWKSBwZXIgbGF5ZXJcbiAgICBwcmludChmXCJNb2RlbDoge21vZGVsX25hbWV9ICB8ICBudW0gbGF5ZXJzIGluIEtWIGNhY2hlOiB7bGVuKHBrdil9XCIpXG4gICAgcHJpbnQoZlwiTGF5ZXItMCBLIHNoYXBlOiB7cGt2WzBdWzBdLnNoYXBlfVwiKSAgIyAoYnN6LCBuX2hlYWRzLCBzZXEsIGhlYWRfZGltKVxuXG4gICAgIyBXaXRoIEtWIGNhY2hlIChkZWZhdWx0IHVzZV9jYWNoZT1UcnVlKVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBvdXRfY2FjaGVkID0gbW9kZWwuZ2VuZXJhdGUoaW5wdXRfaWRzLCBtYXhfbmV3X3Rva2Vucz1tYXhfbmV3X3Rva2VucywgdXNlX2NhY2hlPVRydWUpXG4gICAgdF9jYWNoZWQgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gdDBcblxuICAgICMgV2l0aG91dCBLViBjYWNoZSAocmVjb21wdXRlcyBhbGwgSyxWIGF0IGV2ZXJ5IHN0ZXApXG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG91dF91bmNhY2hlZCA9IG1vZGVsLmdlbmVyYXRlKGlucHV0X2lkcywgbWF4X25ld190b2tlbnM9bWF4X25ld190b2tlbnMsIHVzZV9jYWNoZT1GYWxzZSlcbiAgICB0X3VuY2FjaGVkID0gdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwXG5cbiAgICBzcGVlZHVwID0gdF91bmNhY2hlZCAvIHRfY2FjaGVkXG4gICAgcHJpbnQoZlwidXNlX2NhY2hlPVRydWU6ICB7dF9jYWNoZWQ6LjJmfXNcIilcbiAgICBwcmludChmXCJ1c2VfY2FjaGU9RmFsc2U6IHt0X3VuY2FjaGVkOi4yZn1zXCIpXG4gICAgcHJpbnQoZlwiS1YgY2FjaGUgc3BlZWR1cDoge3NwZWVkdXA6LjFmfXggIChncm93cyB3aXRoIG1heF9uZXdfdG9rZW5zKVwiKVxuXG5iZW5jaG1hcmtfaGZfa3ZfY2FjaGUoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIktWIGNhY2hlIGNvbnZlcnRzIE8obl4yKSB0b3RhbCBkZWNvZGUgd29yayB0byBPKG4pOiBlc3NlbnRpYWwgZm9yIGFueSBnZW5lcmF0aW9uIGxvbmdlciB0aGFuIH4xMCB0b2tlbnMuIiwiTWVtb3J5ID0gMiAqIGxheWVycyAqIEtWX2hlYWRzICogaGVhZF9kaW0gKiBiYXRjaCAqIHNlcSAqIGR0eXBlX2J5dGVzOyBtb2RlbCB0aGUgYnVkZ2V0IGV4cGxpY2l0bHkgYmVmb3JlIGRlcGxveW1lbnQuIiwiR1FBIHdpdGggOCBLViBoZWFkcyBpcyBub3cgdGhlIHN0YW5kYXJkOiA0eCBLViBjYWNoZSByZWR1Y3Rpb24gdnMgTUhBIHdpdGggbmVnbGlnaWJsZSBxdWFsaXR5IGxvc3MgYXQgN0IrIHNjYWxlLiIsIk1RQSAoMSBLViBoZWFkKSBnaXZlcyBtYXhpbXVtIGNhY2hlIHJlZHVjdGlvbiAoMzJ4IGZvciAzMi1oZWFkIG1vZGVscykgYnV0IHJpc2tzIHF1YWxpdHkgZGVncmFkYXRpb247IHVzZWQgaW4gUGFMTSBhbmQgRmFsY29uLiIsIkRlY29kZSBwaGFzZSBpcyBtZW1vcnktYmFuZHdpZHRoLWJvdW5kOiBsYXJnZXIgYmF0Y2hlcyBpbXByb3ZlIEdQVSB1dGlsaXphdGlvbiBieSBhbW9ydGl6aW5nIHdlaWdodCByZWFkcyBhY3Jvc3MgbW9yZSB0b2tlbnMuIiwiS1YgY2FjaGUgZXZpY3Rpb24gKFN0cmVhbWluZ0xMTSwgSDJPLCBTbmFwS1YpIGVuYWJsZXMgbG9uZy1jb250ZXh0IGluZmVyZW5jZSBiZXlvbmQgYXZhaWxhYmxlIEdQVSBtZW1vcnkgYXQgbW9kZXN0IHF1YWxpdHkgY29zdC4iLCJIdWdnaW5nRmFjZSBEeW5hbWljQ2FjaGUgYW5kIFN0YXRpY0NhY2hlIHByb3ZpZGUgZmxleGlibGUgdnMgcHJlLWFsbG9jYXRlZCBLViBzdG9yYWdlOyBwcmVmZXIgU3RhdGljQ2FjaGUgZm9yIHByb2R1Y3Rpb24gZ2VuZXJhdGlvbiBsYXRlbmN5LiIsIlF1YW50aXplZCBLViBjYWNoZSAoSU5UOC9JTlQ0KSBwcm92aWRlcyAyLTR4IG1lbW9yeSByZWR1Y3Rpb247IGNvbWJpbmUgd2l0aCBHUUEgZm9yIG1heGltdW0gZWZmaWNpZW5jeS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# KV Cache in Transformer Inference

The KV cache is the primary optimization that makes autoregressive transformer inference practical at scale. During the prefill phase, the model computes key (K) and value (V) projections for every input token in one parallel forward pass. Without caching, each subsequent decode step would recompute these projections for all previous tokens — an O(n) operation per step repeated n times, giving O(n^2) total work over an n-token generation. By storing the K and V tensors after prefill and reusing them in all subsequent decode steps, the model reduces each decode step to computing only one new pair of K, V projections for the newly generated token, then concatenating them with the cache. This drops per-step attention from O(n^2) to O(n) in sequence length.

## Overview

Transformer attention computes Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V. In autoregressive decoding, each generated token t must attend to all t-1 previous tokens plus itself. Without caching, generating token t requires computing K_i and V_i for every prior token i, which is wasteful since K_i and V_i are deterministic functions of fixed previous input tokens and never change. The KV cache stores K_i and V_i after their first computation and reuses them indefinitely. At each decode step, only the new token's Q, K, V are computed from the new token embedding; the new K and V are appended to the cache, and attention runs against the full cached sequence. This is a pure algorithmic optimization — correctness is identical to the uncached version, with no approximation.

## Prefill vs Decode Phase

LLM inference has two computationally distinct phases. The prefill phase processes the entire prompt in a single parallel forward pass. All token positions are known, so attention can be computed as a dense matrix multiplication across all positions simultaneously. Prefill is compute-bound: arithmetic intensity (FLOPs per byte of memory bandwidth) is high, and modern GPUs achieve close to peak FLOP utilization. The decode phase generates tokens one at a time autoregressively. Each step is memory-bandwidth-bound: the GPU must read the full model weights and the full KV cache from HBM (High-Bandwidth Memory) to compute a single output token. On an A100 80GB GPU with 2 TB/s memory bandwidth, reading a 70B parameter model in bfloat16 (~140 GB) plus a 32 GB KV cache takes ~86ms per step — setting a hard floor on token generation latency. This fundamental asymmetry motivates separate optimization strategies: maximize batch size during prefill (higher arithmetic intensity), minimize KV cache size and maximize batch size during decode (higher bandwidth utilization).

## KV Cache Mechanics

At each transformer layer, the KV cache maintains two tensors: K_cache and V_cache, each of shape (batch_size, n_kv_heads, seq_len, head_dim). At decode step t, the new token embedding passes through the Q, K, V projection matrices to produce q_t, k_t, v_t, each of shape (bsz, n_kv_heads, 1, head_dim). k_t and v_t are appended to the cache: K_full = cat([K_cache, k_t], dim=2). Attention then runs against K_full and V_full with the query q_t, producing output of shape (bsz, n_heads, 1, head_dim). This output is projected and added to the residual stream. The updated cache, now containing seq_len + 1 entries, is passed to the next decode step. Across all L layers, this means the model maintains 2 * L KV cache tensors simultaneously. The total memory is proportional to L * n_kv_heads * head_dim * batch_size * seq_len * 2 * dtype_bytes.

```python
import torch
import torch.nn.functional as F
import math
import time

def decode_step_with_cache(q_new, k_new, v_new, kv_cache=None):
    """
    Single autoregressive decode step using a KV cache dict.
    q_new, k_new, v_new: (bsz, 1, head_dim) tensors for the new token.
    kv_cache: dict {'k': (bsz, past_len, d), 'v': (bsz, past_len, d)} or None.
    Returns (output, updated_kv_cache). Cache grows by 1 position each step.
    Complexity: O(n) per step with cache vs O(n^2) total without.
    """
    if kv_cache is not None:
        k = torch.cat([kv_cache['k'], k_new], dim=1)  # (bsz, past+1, head_dim)
        v = torch.cat([kv_cache['v'], v_new], dim=1)
    else:
        k, v = k_new, v_new
    new_cache = {'k': k, 'v': v}
    scale = math.sqrt(q_new.shape[-1])
    scores = torch.bmm(q_new, k.transpose(1, 2)) / scale  # (bsz, 1, seq_len)
    attn = F.softmax(scores, dim=-1)
    output = torch.bmm(attn, v)                            # (bsz, 1, head_dim)
    return output, new_cache

# Benchmark 200-step decode with KV cache
bsz, head_dim, n_steps = 1, 64, 200
cache = None
t0 = time.perf_counter()
for step in range(n_steps):
    q = torch.randn(bsz, 1, head_dim)
    out, cache = decode_step_with_cache(q, q.clone(), q.clone(), cache)
elapsed = (time.perf_counter() - t0) * 1000
print(f"Decoded {n_steps} tokens with cache in {elapsed:.1f}ms")
print(f"Final KV cache shape: {cache['k'].shape}")  # (1, 200, 64)
print("KV cache: O(n) per step -- eliminates redundant K,V recomputation.")
```

## Memory Footprint

KV cache memory is the product of six factors: 2 (K and V) × layers × KV_heads × head_dim × batch_size × seq_len × dtype_bytes. For LLaMA-3-8B (32 layers, 8 GQA heads, head_dim=128) in bfloat16 at batch=1, seq=4096: 2 × 32 × 8 × 128 × 1 × 4096 × 2 = 536 MB. At batch=32, seq=8192: 2 × 32 × 8 × 128 × 32 × 8192 × 2 = 34.4 GB. For LLaMA-3-70B (80 layers, 8 GQA heads, head_dim=128) at batch=32, seq=8192: 86 GB — more than the model weights on a single A100. KV cache allocation must be planned as part of GPU memory budgeting: a typical deployment allocates model weights first, then reserves remaining GPU memory for KV cache. The KV cache size determines the maximum achievable batch size and sequence length simultaneously — engineers must choose carefully based on expected workload.

```python
import torch
from typing import Dict, Tuple

def compute_kv_cache_bytes(
    n_layers: int,
    n_kv_heads: int,
    head_dim: int,
    batch_size: int,
    seq_len: int,
    dtype_bytes: int = 2,  # 2 = bfloat16/float16, 4 = float32
) -> int:
    """
    Total KV cache memory in bytes.
    Formula: 2 (K+V) * layers * kv_heads * head_dim * batch * seq * dtype_bytes.
    """
    return 2 * n_layers * n_kv_heads * head_dim * batch_size * seq_len * dtype_bytes

# Model configs (GQA reduces n_kv_heads far below n_query_heads)
configs = {
    "LLaMA-3-8B  (GQA-8)":  dict(n_layers=32, n_kv_heads=8,  head_dim=128),
    "LLaMA-3-70B (GQA-8)":  dict(n_layers=80, n_kv_heads=8,  head_dim=128),
    "Mistral-7B  (GQA-8)":  dict(n_layers=32, n_kv_heads=8,  head_dim=128),
    "GPT-2 Large (MHA-16)": dict(n_layers=36, n_kv_heads=16, head_dim=64),
}
weight_bytes = {"LLaMA-3-8B  (GQA-8)": 8e9*2, "LLaMA-3-70B (GQA-8)": 70e9*2,
                "Mistral-7B  (GQA-8)": 7e9*2, "GPT-2 Large (MHA-16)": 0.77e9*4}

print(f"{'Model':<26} {'bsz':>4} {'seq':>6} {'KV GB':>8} {'% of weights':>14}")
print("-" * 64)
for name, cfg in configs.items():
    for bsz, seq in [(1, 4096), (8, 4096), (32, 8192)]:
        kv = compute_kv_cache_bytes(**cfg, batch_size=bsz, seq_len=seq)
        pct = kv / weight_bytes[name] * 100
        print(f"{name:<26} {bsz:>4} {seq:>6} {kv/1e9:>7.2f}G {pct:>13.1f}%")
```

> **KV Cache Memory Warning**: The KV cache grows linearly with sequence length and batch size — a batch of 32 requests at 8K context can easily require 50+ GB of KV cache alone for a 70B model, before even storing the weights. On a single A100 80GB, storing 70B weights in bfloat16 consumes ~140 GB across multiple GPUs; KV cache must be budgeted per-GPU across the tensor-parallel split. Always profile KV cache size before deploying at batch sizes larger than 4.

| Attention Type | KV Heads (32L) | Cache Size (seq=4096, bsz=1, dim=128) | vs MHA | Notes |
| --- | --- | --- | --- | --- |
| MHA  (H=32) | 32 | ~2.15 GB | 1.0x | Full per-head K,V; GPT-2 / LLaMA-1 |
| MQA  (H=1) | 1 | ~0.067 GB | 32x smaller | Shared single K,V; PaLM, Falcon-7B |
| GQA-8 (H=8) | 8 | ~0.536 GB | 4x smaller | LLaMA-3 all sizes, Mistral-7B |
| GQA-4 (H=4) | 4 | ~0.268 GB | 8x smaller | Aggressive; viable at 13B+ scale |
| GQA-2 (H=2) | 2 | ~0.134 GB | 16x smaller | Extreme compression; quality tradeoff |

## Multi-Query and Grouped-Query Attention

Standard Multi-Head Attention (MHA) assigns each query head its own K, V projection matrices, giving n_heads KV heads. Multi-Query Attention (MQA, Shazeer 2019) uses a single shared K, V head across all query heads, reducing KV cache by a factor of n_heads. For a 32-head model, MQA cuts KV cache 32x but can degrade quality, particularly on tasks requiring diverse attention patterns per head. Grouped-Query Attention (GQA, Ainslie et al. 2023) generalizes between MHA and MQA: G groups of query heads share one K,V head each, where 1 <= G < n_heads. LLaMA-3 (8B, 70B), LLaMA-3.1, Mistral-7B, Mixtral, Gemma, and most modern open-source LLMs use GQA with G=8 KV heads. GQA with G=8 achieves 4x KV cache reduction vs MHA while maintaining near-MHA quality at 7B+ parameter scale. The quality degradation from GQA is negligible compared to the memory and throughput benefits, making GQA the default for new large LLM architectures.

```python
import torch
import math

def kv_cache_gb(
    n_layers: int, n_kv_heads: int, head_dim: int,
    batch_size: int, seq_len: int, dtype_bytes: int = 2,
) -> float:
    """KV cache memory in GB (float16/bfloat16 by default)."""
    return (2 * n_layers * n_kv_heads * head_dim
            * batch_size * seq_len * dtype_bytes) / 1e9

# Compare MHA, GQA variants, and MQA for 32-layer model, seq=4096, bsz=1
base = dict(n_layers=32, head_dim=128, batch_size=1, seq_len=4096)
attention_types = [
    ("MHA  (32 KV heads)",  32,  "GPT-2 / Llama-1 style"),
    ("GQA-8 (8 KV heads)",   8,  "LLaMA-3 / Mistral-7B"),
    ("GQA-4 (4 KV heads)",   4,  "Custom GQA-4 config"),
    ("GQA-2 (2 KV heads)",   2,  "Aggressive compression"),
    ("MQA   (1 KV head)",    1,  "PaLM / Falcon-7B style"),
]
mha_gb = kv_cache_gb(**base, n_kv_heads=32)
print(f"{'Attention Type':<24} {'KV Heads':>10} {'GB':>8} {'vs MHA':>10}  Notes")
print("-" * 75)
for label, n_kv, notes in attention_types:
    gb = kv_cache_gb(**base, n_kv_heads=n_kv)
    reduction = mha_gb / gb
    print(f"{label:<24} {n_kv:>10} {gb:>7.3f}G {reduction:>9.1f}x  {notes}")
print(f"\nBase (MHA): {mha_gb:.3f} GB at seq=4096, bsz=1, 32L, dim=128, bf16")
print("GQA-8 reduces KV cache 4x vs MHA with minimal quality loss at 7B+ scale.")
```

## KV Cache Eviction

For long-context inference where the KV cache would exceed GPU memory, eviction strategies selectively discard stored K, V entries. StreamingLLM (Xiao et al., 2023) keeps the first few tokens (attention sinks, typically 4) plus a sliding window of recent tokens. Attention sink tokens receive disproportionate attention weight; discarding them causes instability. Keeping only sinks + recent tokens (window size 512–2048) enables unbounded context at constant memory. H2O (Heavy-Hitter Oracle, Zhang et al., 2023) tracks cumulative attention weight per token and evicts those with the lowest accumulated score. Tokens that repeatedly receive high attention (heavy hitters) are preserved; rarely attended tokens are evicted. ScissorHands (Liu et al., 2023) maintains a fixed sparse pattern identifying persistent heavy-hitters across generation steps. SnapKV (Li et al., 2024) compresses the KV cache by clustering similar K,V vectors within a window and retaining representative centroids. All eviction strategies trade off quality (lower eviction rate → higher quality) vs memory (higher eviction rate → smaller cache) vs latency (eviction overhead per step).

- StreamingLLM: keep first 4 attention-sink tokens + sliding window (512-2048). Constant memory, unbounded context, small quality loss.
- H2O: track cumulative attention mass per token, evict lowest-scoring entries. Dynamic and task-adaptive, ~1-2% quality loss at 50% eviction.
- ScissorHands: identify persistent heavy-hitter positions; evict non-heavy-hitter tokens. Similar quality to H2O with lower per-step overhead.
- SnapKV: cluster similar K,V vectors, retain centroids. Good compression ratio (~4x) with strong long-context performance.
- Quantized KV cache (INT8/INT4): reduce dtype_bytes from 2 to 1 or 0.5, doubling effective batch size or sequence length at minimal quality cost.
- Layer-wise eviction: deeper layers have lower attention entropy and tolerate more aggressive eviction than early layers.

## KV Cache in HuggingFace

HuggingFace Transformers implements KV caching via the `use_cache=True` parameter (enabled by default in `generate()`). The model returns `past_key_values`, a tuple of (K, V) tuples — one per layer — after each forward pass. In `generate()`, past_key_values is passed automatically between decode steps. Since Transformers v4.36, the `DynamicCache` class wraps past_key_values with an explicit `.update(key_states, value_states, layer_idx)` API, making cache inspection and manipulation straightforward. Static caches (`StaticCache`) pre-allocate fixed-size tensors to avoid dynamic resizing overhead during generation — useful for production serving where max sequence length is known. Quantized KV caches (`QuantoQuantizedCache`) store K,V in INT8 or INT4, halving or quartering cache memory at the cost of a quantization/dequantization step per layer.

```python
import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer

def benchmark_hf_kv_cache(
    model_name: str = "gpt2",
    prompt: str = "The KV cache is a key optimization for transformer inference because",
    max_new_tokens: int = 80,
):
    """Compare HuggingFace generation speed with vs without KV cache."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).eval()
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]

    # Inspect past_key_values from a single forward pass
    with torch.no_grad():
        fwd = model(input_ids, use_cache=True)
    pkv = fwd.past_key_values  # tuple of (K, V) per layer
    print(f"Model: {model_name}  |  num layers in KV cache: {len(pkv)}")
    print(f"Layer-0 K shape: {pkv[0][0].shape}")  # (bsz, n_heads, seq, head_dim)

    # With KV cache (default use_cache=True)
    t0 = time.perf_counter()
    with torch.no_grad():
        out_cached = model.generate(input_ids, max_new_tokens=max_new_tokens, use_cache=True)
    t_cached = time.perf_counter() - t0

    # Without KV cache (recomputes all K,V at every step)
    t0 = time.perf_counter()
    with torch.no_grad():
        out_uncached = model.generate(input_ids, max_new_tokens=max_new_tokens, use_cache=False)
    t_uncached = time.perf_counter() - t0

    speedup = t_uncached / t_cached
    print(f"use_cache=True:  {t_cached:.2f}s")
    print(f"use_cache=False: {t_uncached:.2f}s")
    print(f"KV cache speedup: {speedup:.1f}x  (grows with max_new_tokens)")

benchmark_hf_kv_cache()
```

## Key Takeaways

- KV cache converts O(n^2) total decode work to O(n): essential for any generation longer than ~10 tokens.
- Memory = 2 * layers * KV_heads * head_dim * batch * seq * dtype_bytes; model the budget explicitly before deployment.
- GQA with 8 KV heads is now the standard: 4x KV cache reduction vs MHA with negligible quality loss at 7B+ scale.
- MQA (1 KV head) gives maximum cache reduction (32x for 32-head models) but risks quality degradation; used in PaLM and Falcon.
- Decode phase is memory-bandwidth-bound: larger batches improve GPU utilization by amortizing weight reads across more tokens.
- KV cache eviction (StreamingLLM, H2O, SnapKV) enables long-context inference beyond available GPU memory at modest quality cost.
- HuggingFace DynamicCache and StaticCache provide flexible vs pre-allocated KV storage; prefer StaticCache for production generation latency.
- Quantized KV cache (INT8/INT4) provides 2-4x memory reduction; combine with GQA for maximum efficiency.

---

