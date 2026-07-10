---
title: "RoPE — Rotary Position Embeddings and Long-Context Extension"
slug: "rope-rotary-embeddings"
description: "Master RoPE (Rotary Position Embeddings): rotating query and key vectors by position-dependent angles to encode relative distance directly in the attention dot product, with zero extra parameters, used in LLaMA 1/2/3, Mistral, Falcon, and Qwen, plus YaRN for long-context extension."
tags: ["deep-learning", "transformers", "positional-encoding"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUm9QRSAoUm90YXJ5IFBvc2l0aW9uIEVtYmVkZGluZ3MpLCBpbnRyb2R1Y2VkIGJ5IFN1IGV0IGFsLiAoMjAyMSkgaW4gUm9Gb3JtZXIsIGVuY29kZXMgcG9zaXRpb24gaW5mb3JtYXRpb24gYnkgcm90YXRpbmcgdGhlIHF1ZXJ5IGFuZCBrZXkgdmVjdG9ycyBiZWZvcmUgY29tcHV0aW5nIHRoZSBkb3QgcHJvZHVjdC4gVGhlIGtleSBtYXRoZW1hdGljYWwgaW5zaWdodCBpcyB0aGF0IGlmIHlvdSByb3RhdGUgYSB2ZWN0b3IgYXQgcG9zaXRpb24gbSBieSBhbmdsZSBtwrfOuCBhbmQgYSB2ZWN0b3IgYXQgcG9zaXRpb24gbiBieSBhbmdsZSBuwrfOuCwgdGhlaXIgZG90IHByb2R1Y3QgaW52b2x2ZXMgb25seSB0aGUgcmVsYXRpdmUgYW5nbGUgKG3iiJJuKcK3zrgg4oCUIHRoZSBhYnNvbHV0ZSBwb3NpdGlvbnMgY2FuY2VsIG91dC4gVGhpcyBnaXZlcyBSb1BFIHRoZSBiZXN0IG9mIGJvdGggd29ybGRzOiBpdCBlbmNvZGVzIHJlbGF0aXZlIHBvc2l0aW9uIGRpcmVjdGx5IGluIHRoZSBhdHRlbnRpb24gc2NvcmUgKGxpa2UgcmVsYXRpdmUgUEUgc2NoZW1lcykgd2hpbGUgYmVpbmcgY29tcHV0ZWQgYXMgYSBzaW1wbGUgbXVsdGlwbGljYXRpdmUgb3BlcmF0aW9uIG9uIGV4aXN0aW5nIFEvSyB2ZWN0b3JzIChsaWtlIGFic29sdXRlIFBFKSwgd2l0aCB6ZXJvIGFkZGl0aW9uYWwgcGFyYW1ldGVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSb1BFIE1hdGhlbWF0aWNhbCBGb3VuZGF0aW9uIOKAlCBSb3RhdGlvbiBpbiAyRCBTdWJzcGFjZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJvUEUgc3BsaXRzIHRoZSBkX21vZGVsIGRpbWVuc2lvbiBpbnRvIGQvMiBwYWlycy4gRm9yIHBhaXIgaywgdGhlIHJvdGF0aW9uIGFuZ2xlIGlzIM64X2sgPSAxMDAwMF57LTJrL2R9LCBtYXRjaGluZyB0aGUgZnJlcXVlbmN5IHNjaGVkdWxlIG9mIHNpbnVzb2lkYWwgUEUuIEZvciBhIHZlY3RvciBhdCBwb3NpdGlvbiBtLCBwYWlyIGsgaXMgcm90YXRlZCBieSBtwrfOuF9rOiB0aGUgMkQgcm90YXRpb24gW3gxLCB4Ml0g4oaSIFt4McK3Y29zKG3OuF9rKSDiiJIgeDLCt3NpbihtzrhfayksIHgxwrdzaW4obc64X2spICsgeDLCt2NvcyhtzrhfayldLiBXaGVuIGNvbXB1dGluZyB0aGUgZG90IHByb2R1Y3Qgb2Ygcm90YXRlZCBxdWVyeSBxX20gYW5kIHJvdGF0ZWQga2V5IGtfbjogKFJfbcK3cSleVCDCtyAoUl9uwrdrKSA9IHFeVCDCtyBSX3tuLW19IMK3IGsg4oCUIG9ubHkgdGhlIHJlbGF0aXZlIHBvc2l0aW9uIChu4oiSbSkgYXBwZWFycy4gVGhpcyBob2xkcyBleGFjdGx5IGZvciBhbnkgY2hvaWNlIG9mIHEgYW5kIGsgdmVjdG9ycywgbWFraW5nIFJvUEUgYSBwYXJhbWV0ZXItZnJlZSBtZWNoYW5pc20gdGhhdCBwcm92YWJseSBlbmNvZGVzIHJlbGF0aXZlIGRpc3RhbmNlIHdpdGhvdXQgYW55IGFwcHJveGltYXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZnJlcXVlbmN5IHNjaGVkdWxlIM64X2sgPSAxMDAwMF57LTJrL2R9IG1lYW5zIGxvdy1pbmRleCBwYWlycyAoaz0wKSByb3RhdGUgZmFzdCAozrhfMCA9IDEpIHdoaWxlIGhpZ2gtaW5kZXggcGFpcnMgKGs9ZC8y4oiSMSkgcm90YXRlIHNsb3dseSAozrhfe2QvMi0xfSDiiYggMTAwMDBeey0xfSA9IDAuMDAwMSkuIFNob3J0LXJhbmdlIGRlcGVuZGVuY2llcyBhcmUgY2FwdHVyZWQgYnkgZmFzdC1yb3RhdGluZyBwYWlyczsgbG9uZy1yYW5nZSBkZXBlbmRlbmNpZXMgYnkgc2xvdy1yb3RhdGluZyBwYWlycy4gVGhpcyBtYXRjaGVzIHRoZSBmcmVxdWVuY3kgc3BlY3RydW0gb2Ygc2ludXNvaWRhbCBQRSBhbmQgaXMgdGhlIHNhbWUgc2NoZWR1bGUgdXNlZCBpbiB0aGUgb3JpZ2luYWwgVHJhbnNmb3JtZXIuIFRoZSBiYXNlIDEwMDAwIGNhbiBiZSBjaGFuZ2VkOiBsYXJnZXIgYmFzZSA9IHNsb3dlciByb3RhdGlvbiA9IGJldHRlciBsb25nLWNvbnRleHQgKHVzZWQgaW4gQ29kZSBMbGFtYSwgTGxhbWEtMyB3aXRoIGJhc2U9NTAwMDAwKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbXBsZW1lbnRpbmcgUm9QRSBmcm9tIFNjcmF0Y2gifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzdGFuZGFyZCBpbXBsZW1lbnRhdGlvbiBwcmVjb21wdXRlcyBhIChtYXhfc2VxX2xlbiwgZC8yKSB0YWJsZSBvZiBjb3MobcK3zrhfaykgYW5kIHNpbihtwrfOuF9rKSB2YWx1ZXMuIEF0IGZvcndhcmQgdGltZSwgdGhlc2UgYXJlIHVzZWQgdG8gcm90YXRlIGVhY2ggUSBhbmQgSyB2ZWN0b3I6IHRoZSBmaXJzdCBoYWxmIG9mIHRoZSB2ZWN0b3IgaXMgW3gxwrdjb3Mg4oiSIHgywrdzaW5dIGFuZCB0aGUgc2Vjb25kIGhhbGYgaXMgW3gxwrdzaW4gKyB4MsK3Y29zXS4gVGhpcyBpcyBlcXVpdmFsZW50IHRvIGNvbXBsZXggbXVsdGlwbGljYXRpb246IHRyZWF0aW5nIGVhY2ggcGFpciAoeDEsIHgyKSBhcyBhIGNvbXBsZXggbnVtYmVyIHgxICsgacK3eDIgYW5kIG11bHRpcGx5aW5nIGJ5IGVee2nCt23Ct864X2t9LiBUaGUgcm90YXRlX2hhbGYgdHJpY2sgYXZvaWRzIG1hdGVyaWFsaXNpbmcgdGhlIGZ1bGwgcm90YXRpb24gbWF0cml4IGFuZCBvcGVyYXRlcyB3aXRoIGVsZW1lbnQtd2lzZSBtdWx0aXBsaWNhdGlvbnMgb24gaGFsZi1zaGlmdGVkIHNsaWNlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbWF0aFxuXG5kZWYgYnVpbGRfcm9wZV9jYWNoZShzZXFfbGVuLCBkX21vZGVsLCBiYXNlPTEwMDAwKTpcbiAgICAjIFByZWNvbXB1dGUgY29zL3NpbiB0YWJsZXMgZm9yIFJvUEUuIGRfbW9kZWwgbXVzdCBiZSBldmVuLlxuICAgIGFzc2VydCBkX21vZGVsICUgMiA9PSAwXG4gICAgaGFsZiAgPSBkX21vZGVsIC8vIDJcbiAgICBrICAgICA9IHRvcmNoLmFyYW5nZShoYWxmLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgIHRoZXRhID0gYmFzZSAqKiAoLTIgKiBrIC8gZF9tb2RlbCkgICAgICAgICAgICAjIChoYWxmLCkgZnJlcXVlbmNpZXNcbiAgICBwb3MgICA9IHRvcmNoLmFyYW5nZShzZXFfbGVuLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgIGZyZXFzID0gdG9yY2gub3V0ZXIocG9zLCB0aGV0YSkgICAgICAgICAgICAgICAjIChzZXFfbGVuLCBoYWxmKVxuICAgIHJldHVybiB0b3JjaC5jb3MoZnJlcXMpLCB0b3JjaC5zaW4oZnJlcXMpXG5cbmRlZiBhcHBseV9yb3BlKHgsIGNvcywgc2luKTpcbiAgICAjIEFwcGx5IFJvUEUgdG8geDogKGJhdGNoLCBzZXFfbGVuLCBkX21vZGVsKVxuICAgIHgxLCB4MiA9IHhbLi4uLCA6eC5zaGFwZVstMV0vLzJdLCB4Wy4uLiwgeC5zaGFwZVstMV0vLzI6XVxuICAgIGNvcyA9IGNvc1s6eC5zaGFwZVsxXV0udW5zcXVlZXplKDApICAgICAgICAgICAjICgxLCBzZXFfbGVuLCBoYWxmKVxuICAgIHNpbiA9IHNpbls6eC5zaGFwZVsxXV0udW5zcXVlZXplKDApXG4gICAgeF9yb3QgPSB0b3JjaC5jYXQoW3gxICogY29zIC0geDIgKiBzaW4sIHgxICogc2luICsgeDIgKiBjb3NdLCBkaW09LTEpXG4gICAgcmV0dXJuIHhfcm90XG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuc2VxX2xlbiwgZF9tb2RlbCA9IDE2LCA2NFxuY29zX2NhY2hlLCBzaW5fY2FjaGUgPSBidWlsZF9yb3BlX2NhY2hlKHNlcV9sZW4sIGRfbW9kZWwpXG5wcmludChcdTAwMjdjb3MgY2FjaGUgc2hhcGU6XHUwMDI3LCBjb3NfY2FjaGUuc2hhcGUsIFx1MDAyNyBzaW4gY2FjaGUgc2hhcGU6XHUwMDI3LCBzaW5fY2FjaGUuc2hhcGUpXG5cblEgPSB0b3JjaC5yYW5kbigxLCBzZXFfbGVuLCBkX21vZGVsKVxuSyA9IHRvcmNoLnJhbmRuKDEsIHNlcV9sZW4sIGRfbW9kZWwpXG5RX3JvdCA9IGFwcGx5X3JvcGUoUSwgY29zX2NhY2hlLCBzaW5fY2FjaGUpXG5LX3JvdCA9IGFwcGx5X3JvcGUoSywgY29zX2NhY2hlLCBzaW5fY2FjaGUpXG5wcmludChcdTAwMjdROlx1MDAyNywgUS5zaGFwZSwgXHUwMDI3LVx1MDAzZSBRX3JvdDpcdTAwMjcsIFFfcm90LnNoYXBlKVxuc2NvcmVzID0gKFFfcm90IEAgS19yb3QudHJhbnNwb3NlKC0yLCAtMSkpIC8gZF9tb2RlbCAqKiAwLjVcbnByaW50KFx1MDAyN1Njb3JlIG1hdHJpeCBzaGFwZTpcdTAwMjcsIHNjb3Jlcy5zaGFwZSlcbnByaW50KFx1MDAyN1Njb3JlcyBlbmNvZGUgb25seSByZWxhdGl2ZSBwb3NpdGlvbiDigJQgbm8gYWJzb2x1dGUgaW5kZXggbmVlZGVkLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWZXJpZnlpbmcgdGhlIFJlbGF0aXZlIERpc3RhbmNlIFByb3BlcnR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZGVmaW5pbmcgcHJvcGVydHkgb2YgUm9QRSBpcyB0aGF0IHRoZSBhdHRlbnRpb24gc2NvcmUgYmV0d2VlbiBhIHJvdGF0ZWQgcXVlcnkgYXQgcG9zaXRpb24gcF9xIGFuZCBhIHJvdGF0ZWQga2V5IGF0IHBvc2l0aW9uIHBfayBkZXBlbmRzIG9ubHkgb24gKHBfcSDiiJIgcF9rKSwgbm90IG9uIHRoZSBhYnNvbHV0ZSB2YWx1ZXMgb2YgcF9xIG9yIHBfayBpbmRpdmlkdWFsbHkuIFdlIGNhbiB2ZXJpZnkgdGhpcyBudW1lcmljYWxseTogZml4IHEgYW5kIGsgdmVjdG9ycywgcm90YXRlIHRoZW0gYXQgZGlmZmVyZW50IGFic29sdXRlIHBvc2l0aW9uIHBhaXJzIHRoYXQgc2hhcmUgdGhlIHNhbWUgcmVsYXRpdmUgZGlzdGFuY2UsIGFuZCBjb25maXJtIHRoZSBkb3QgcHJvZHVjdHMgYXJlIGlkZW50aWNhbC4gRm9yIGV4YW1wbGUsIChwb3NfcT0wLCBwb3Nfaz0yKSBhbmQgKHBvc19xPTEsIHBvc19rPTMpIGJvdGggaGF2ZSByZWxhdGl2ZSBkaXN0YW5jZSDiiJIyIGFuZCBzaG91bGQgeWllbGQgdGhlIHNhbWUgZG90IHByb2R1Y3QuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG1hdGhcblxuZGVmIGJ1aWxkX3JvcGUoc2VxX2xlbiwgZF9tb2RlbCwgYmFzZT0xMDAwMCk6XG4gICAgaGFsZiAgPSBkX21vZGVsIC8vIDJcbiAgICB0aGV0YSA9IHRvcmNoLnRlbnNvcihbYmFzZSAqKiAoLTIqay9kX21vZGVsKSBmb3IgayBpbiByYW5nZShoYWxmKV0pXG4gICAgZnJlcXMgPSB0b3JjaC5vdXRlcih0b3JjaC5hcmFuZ2Uoc2VxX2xlbiwgZHR5cGU9dG9yY2guZmxvYXQzMiksIHRoZXRhKVxuICAgIHJldHVybiB0b3JjaC5jb3MoZnJlcXMpLCB0b3JjaC5zaW4oZnJlcXMpXG5cbmRlZiByb3RhdGVfdmVjKHYsIHBvcywgY29zLCBzaW4pOlxuICAgIGMsIHMgPSBjb3NbcG9zXSwgc2luW3Bvc11cbiAgICB2MSwgdjIgPSB2WzpsZW4odikvLzJdLCB2W2xlbih2KS8vMjpdXG4gICAgcmV0dXJuIHRvcmNoLmNhdChbdjEqYyAtIHYyKnMsIHYxKnMgKyB2MipjXSlcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmRfbW9kZWwgPSAxNlxuY29zLCBzaW4gPSBidWlsZF9yb3BlKDIwLCBkX21vZGVsKVxucSA9IHRvcmNoLnJhbmRuKGRfbW9kZWwpXG5rID0gdG9yY2gucmFuZG4oZF9tb2RlbClcblxucHJpbnQoXHUwMDI3VmVyaWZ5aW5nOiBkb3QocV9yb3RAcHEsIGtfcm90QHBrKSBkZXBlbmRzIG9ubHkgb24gKHBxIC0gcGspXHUwMDI3KVxucHJpbnQoXHUwMDI3ezpcdTAwM2U2fSB7Olx1MDAzZTZ9IHs6XHUwMDNlMTB9IHs6XHUwMDNlMTR9XHUwMDI3LmZvcm1hdChcdTAwMjdwb3NfcVx1MDAyNywgXHUwMDI3cG9zX2tcdTAwMjcsIFx1MDAyN3JlbGF0aXZlXHUwMDI3LCBcdTAwMjdkb3Rfc2NvcmVcdTAwMjcpKVxuZm9yIHBxLCBwayBpbiBbKDAsMCksKDEsMSksKDUsNSksKDAsMiksKDEsMyksKDUsNyksKDAsNCksKDEsNSldOlxuICAgIHFfciA9IHJvdGF0ZV92ZWMocSwgcHEsIGNvcywgc2luKVxuICAgIGtfciA9IHJvdGF0ZV92ZWMoaywgcGssIGNvcywgc2luKVxuICAgIGRvdCA9IChxX3IgKiBrX3IpLnN1bSgpLml0ZW0oKVxuICAgIHByaW50KFx1MDAyN3s6XHUwMDNlNn0gezpcdTAwM2U2fSB7Olx1MDAzZTEwfSB7Olx1MDAzZTE0LjZmfVx1MDAyNy5mb3JtYXQocHEsIHBrLCBwcS1waywgZG90KSlcbnByaW50KFx1MDAyN1BhaXJzICgwLC0yKSwgKDEsLTIpLCAoNSwtMikgc2hvdWxkIGdpdmUgaWRlbnRpY2FsIGRvdCBzY29yZXMuXHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW1wb3J0YW50IiwidGl0bGUiOiJSb1BFIEhhcyBaZXJvIFRyYWluYWJsZSBQYXJhbWV0ZXJzIiwiY29udGVudCI6IlVubGlrZSBsZWFybmVkIFBFICh3aGljaCBoYXMgbWF4X2xlbiDDlyBkX21vZGVsIHBhcmFtZXRlcnMpIG9yIFNoYXctc3R5bGUgcmVsYXRpdmUgUEUgKHdoaWNoIGhhcyAoMsOXbWF4X3JlbCsxKSDDlyBkX21vZGVsIHBhcmFtZXRlcnMpLCBSb1BFIGFkZHMgZXhhY3RseSB6ZXJvIHRyYWluYWJsZSBwYXJhbWV0ZXJzLiBUaGUgY29zL3NpbiB0YWJsZXMgYXJlIGNvbXB1dGVkIGZyb20gYSBmaXhlZCBmb3JtdWxhIGFuZCBzdG9yZWQgYXMgbm9uLWdyYWRpZW50IGJ1ZmZlcnMuIFRoaXMgbWVhbnMgUm9QRVx1MDAyN3MgcG9zaXRpb24gZW5jb2RpbmcgY2FwYWNpdHkgY29tZXMgZW50aXJlbHkgZnJvbSB0aGUgbW9kZWwgbGVhcm5pbmcgdG8gdXNlIHJvdGF0ZWQgUS9LIHZlY3RvcnMg4oCUIHRoZSByb3RhdGlvbiBzY2hlZHVsZSBpdHNlbGYgaXMgYSBoeXBlcnBhcmFtZXRlciwgbm90IGEgbGVhcm5lZCBvbmUuIENoYW5naW5nIHRoZSBiYXNlIGZyb20gMTAwMDAgdG8gNTAwMDAwIChhcyBpbiBMTGFNQS0zKSBzaGlmdHMgdGhlIGZyZXF1ZW5jeSBzcGVjdHJ1bSB3aXRob3V0IGFkZGluZyBhbnkgcGFyYW1ldGVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFZmZpY2llbnQgUm9QRSB3aXRoIFByZWNvbXB1dGVkIGNvcy9zaW4gQ2FjaGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByb2R1Y3Rpb24gaW1wbGVtZW50YXRpb25zIHJlZ2lzdGVyIHRoZSBjb3Mvc2luIHRhYmxlcyBhcyBub24tdHJhaW5hYmxlIGJ1ZmZlcnMgdXNpbmcgcmVnaXN0ZXJfYnVmZmVyLCBlbnN1cmluZyB0aGV5IGFyZSBtb3ZlZCB0byB0aGUgY29ycmVjdCBkZXZpY2Ugd2l0aCB0aGUgbW9kZWwgd2l0aG91dCBhcHBlYXJpbmcgaW4gbW9kZWwucGFyYW1ldGVycygpLiBUaGUgdGFibGVzIGFyZSBwcmVjb21wdXRlZCBmb3IgdGhlIG1heGltdW0gZXhwZWN0ZWQgc2VxdWVuY2UgbGVuZ3RoIGF0IGluaXRpYWxpc2F0aW9uLiBBdCBmb3J3YXJkIHRpbWUsIHRoZSBmaXJzdCBUIHJvd3MgYXJlIHNsaWNlZCBmb3IgdGhlIGFjdHVhbCBzZXF1ZW5jZS4gVGhlIHJvdGF0ZV9oYWxmIG9wZXJhdGlvbiDigJQgbmVnYXRpbmcgdGhlIHNlY29uZCBoYWxmIGFuZCBzd2FwcGluZyDigJQgZW5hYmxlcyB0aGUgcm90YXRpb24gdXNpbmcgb25seSBlbGVtZW50LXdpc2UgbXVsdGlwbGljYXRpb24gYW5kIGFkZGl0aW9uLCBhdm9pZGluZyBhbnkgZXhwbGljaXQgcm90YXRpb24gbWF0cml4LiBUaGlzIGlzIHRoZSBpbXBsZW1lbnRhdGlvbiB1c2VkIGluIEh1Z2dpbmdGYWNlIHRyYW5zZm9ybWVycyBmb3IgTExhTUEsIE1pc3RyYWwsIGFuZCBzaW1pbGFyIG1vZGVscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgUm90YXJ5RW1iZWRkaW5nKG5uLk1vZHVsZSk6XG4gICAgIyBQcm9kdWN0aW9uIFJvUEU6IHByZWNvbXB1dGVkIGNvcy9zaW4gY2FjaGUsIG5vIGxlYXJuZWQgcGFyYW1ldGVycy5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGltLCBtYXhfc2VxX2xlbj00MDk2LCBiYXNlPTEwMDAwKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGludl9mcmVxID0gMS4wIC8gKGJhc2UgKiogKHRvcmNoLmFyYW5nZSgwLCBkaW0sIDIpLmZsb2F0KCkgLyBkaW0pKVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdpbnZfZnJlcVx1MDAyNywgaW52X2ZyZXEpXG4gICAgICAgIHQgICAgID0gdG9yY2guYXJhbmdlKG1heF9zZXFfbGVuKS5mbG9hdCgpXG4gICAgICAgIGZyZXFzID0gdG9yY2gub3V0ZXIodCwgaW52X2ZyZXEpXG4gICAgICAgIGVtYiAgID0gdG9yY2guY2F0KFtmcmVxcywgZnJlcXNdLCBkaW09LTEpICAgIyAobWF4X3NlcV9sZW4sIGRpbSlcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3Y29zX2NhY2hlZFx1MDAyNywgZW1iLmNvcygpKVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdzaW5fY2FjaGVkXHUwMDI3LCBlbWIuc2luKCkpXG5cbiAgICBAc3RhdGljbWV0aG9kXG4gICAgZGVmIHJvdGF0ZV9oYWxmKHgpOlxuICAgICAgICB4MSwgeDIgPSB4Wy4uLiwgOnguc2hhcGVbLTFdLy8yXSwgeFsuLi4sIHguc2hhcGVbLTFdLy8yOl1cbiAgICAgICAgcmV0dXJuIHRvcmNoLmNhdChbLXgyLCB4MV0sIGRpbT0tMSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHEsIGspOlxuICAgICAgICBUICAgPSBxLnNoYXBlWy0yXVxuICAgICAgICBjb3MgPSBzZWxmLmNvc19jYWNoZWRbOlRdLnVuc3F1ZWV6ZSgwKS51bnNxdWVlemUoMClcbiAgICAgICAgc2luID0gc2VsZi5zaW5fY2FjaGVkWzpUXS51bnNxdWVlemUoMCkudW5zcXVlZXplKDApXG4gICAgICAgIHJldHVybiAocSAqIGNvcyArIHNlbGYucm90YXRlX2hhbGYocSkgKiBzaW4sXG4gICAgICAgICAgICAgICAgayAqIGNvcyArIHNlbGYucm90YXRlX2hhbGYoaykgKiBzaW4pXG5cbnJvcGUgPSBSb3RhcnlFbWJlZGRpbmcoZGltPTY0LCBtYXhfc2VxX2xlbj0yMDQ4KVxuYiwgaCwgcywgZCA9IDIsIDgsIDEyOCwgNjRcbnEgPSB0b3JjaC5yYW5kbihiLCBoLCBzLCBkKVxuayA9IHRvcmNoLnJhbmRuKGIsIGgsIHMsIGQpXG5xX3JvdCwga19yb3QgPSByb3BlKHEsIGspXG5wcmludChcdTAwMjdJbnB1dCBxOlx1MDAyNywgcS5zaGFwZSwgXHUwMDI3LVx1MDAzZSBxX3JvdDpcdTAwMjcsIHFfcm90LnNoYXBlKVxucHJpbnQoXHUwMDI3VHJhaW5hYmxlIHBhcmFtZXRlcnM6XHUwMDI3LCBzdW0ocC5udW1lbCgpIGZvciBwIGluIHJvcGUucGFyYW1ldGVycygpKSlcbnByaW50KFx1MDAyN0J1ZmZlcnMgKG5vdCB0cmFpbmVkKTpcdTAwMjcsIFtuYW1lIGZvciBuYW1lLCBfIGluIHJvcGUubmFtZWRfYnVmZmVycygpXSlcbnByaW50KFx1MDAyN1JvUEUgYWRkcyB6ZXJvIHRyYWluYWJsZSBwYXJhbWV0ZXJzIHRvIHRoZSBtb2RlbC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiWWFSTiDigJQgTG9uZy1Db250ZXh0IEV4dGVuc2lvbiBCZXlvbmQgVHJhaW5pbmcgTGVuZ3RoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOYWl2ZSBSb1BFIGV4dHJhcG9sYXRpb24gKHVzaW5nIHBvc2l0aW9uIGluZGljZXMgYmV5b25kIHRoZSB0cmFpbmluZyBtYXhpbXVtKSBjYXVzZXMgdGhlIGF0dGVudGlvbiBzY29yZXMgdG8gaW52b2x2ZSByb3RhdGlvbiBhbmdsZXMgdGhlIG1vZGVsIG5ldmVyIHNhdyBkdXJpbmcgdHJhaW5pbmcsIGRlZ3JhZGluZyBxdWFsaXR5LiBZYVJOIChQZW5nIGV0IGFsLiAyMDIzKSBhZGRyZXNzZXMgdGhpcyBieSBzZWxlY3RpdmVseSBzY2FsaW5nIHRoZSDOuCBmcmVxdWVuY2llczogaGlnaC1mcmVxdWVuY3kgZGltZW5zaW9ucyAoc21hbGwgd2F2ZWxlbmd0aCkgYXJlIGxlZnQgdW5jaGFuZ2VkIGJlY2F1c2UgdGhleSBhbHJlYWR5IHNlZSBkaXZlcnNlIHJlbGF0aXZlIGRpc3RhbmNlcyB3aXRoaW4gdGhlIHRyYWluaW5nIGxlbmd0aDsgbG93LWZyZXF1ZW5jeSBkaW1lbnNpb25zIChsYXJnZSB3YXZlbGVuZ3RoKSBhcmUgc2NhbGVkIGRvd24gYnkgYSBmYWN0b3IgZXF1YWwgdG8gdGhlIGNvbnRleHQgZXh0ZW5zaW9uIHJhdGlvLiBUaGlzIHNlbGVjdGl2ZSBzY2FsaW5nIGtlZXBzIHRoZSBwZXItZGltZW5zaW9uIHJvdGF0aW9uIHJhdGVzIHdpdGhpbiB0aGUgZGlzdHJpYnV0aW9uIHNlZW4gZHVyaW5nIHRyYWluaW5nIHdoaWxlIHBoeXNpY2FsbHkgYWNjb21tb2RhdGluZyBsb25nZXIgc2VxdWVuY2VzLiBZYVJOIGFsc28gYWRqdXN0cyB0aGUgc29mdG1heCB0ZW1wZXJhdHVyZSB0byBjb21wZW5zYXRlIGZvciBzY29yZSBtYWduaXR1ZGUgY2hhbmdlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbWF0aFxuXG5kZWYgcm9wZV9jYWNoZShzZXFfbGVuLCBkX21vZGVsLCBzY2FsZT0xLjAsIGJhc2U9MTAwMDApOlxuICAgICMgU3RhbmRhcmQgUm9QRSB3aXRoIG9wdGlvbmFsIHVuaWZvcm0gZnJlcXVlbmN5IHNjYWxpbmcuXG4gICAgaGFsZiAgPSBkX21vZGVsIC8vIDJcbiAgICBrICAgICA9IHRvcmNoLmFyYW5nZShoYWxmLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgIHRoZXRhID0gYmFzZSAqKiAoLTIgKiBrIC8gZF9tb2RlbCkgLyBzY2FsZVxuICAgIGZyZXFzID0gdG9yY2gub3V0ZXIodG9yY2guYXJhbmdlKHNlcV9sZW4sIGR0eXBlPXRvcmNoLmZsb2F0MzIpLCB0aGV0YSlcbiAgICByZXR1cm4gdG9yY2guY29zKGZyZXFzKSwgdG9yY2guc2luKGZyZXFzKVxuXG5kZWYgeWFybl9jYWNoZShzZXFfbGVuLCBkX21vZGVsLCBzY2FsZSwgYmFzZT0xMDAwMCwgYmV0YV9mYXN0PTMyLCBiZXRhX3Nsb3c9MSk6XG4gICAgIyBZYVJOOiBzZWxlY3RpdmUgc2NhbGluZyDigJQgaGlnaC1mcmVxIGRpbXMgdW5jaGFuZ2VkLCBsb3ctZnJlcSBzY2FsZWQuXG4gICAgaGFsZiAgICA9IGRfbW9kZWwgLy8gMlxuICAgIGsgICAgICAgPSB0b3JjaC5hcmFuZ2UoaGFsZiwgZHR5cGU9dG9yY2guZmxvYXQzMilcbiAgICB0aGV0YSAgID0gYmFzZSAqKiAoLTIgKiBrIC8gZF9tb2RlbClcbiAgICB3YXZlbGVuID0gMiAqIG1hdGgucGkgLyAodGhldGEgKyAxZS05KVxuICAgIHNjYWxlZCAgICAgICAgPSB0aGV0YS5jbG9uZSgpXG4gICAgbG93X21hc2sgICAgICA9IHdhdmVsZW4gXHUwMDNlIHNjYWxlICogYmV0YV9zbG93XG4gICAgc2NhbGVkW2xvd19tYXNrXSAvPSBzY2FsZVxuICAgIGZyZXFzID0gdG9yY2gub3V0ZXIodG9yY2guYXJhbmdlKHNlcV9sZW4sIGR0eXBlPXRvcmNoLmZsb2F0MzIpLCBzY2FsZWQpXG4gICAgcmV0dXJuIHRvcmNoLmNvcyhmcmVxcyksIHRvcmNoLnNpbihmcmVxcylcblxuZF9tb2RlbCA9IDY0XG5wcmludChcdTAwMjd7Olx1MDAzZTh9IHs6XHUwMDNlOH0gezpcdTAwM2UxNH0gezpcdTAwM2UxNH1cdTAwMjcuZm9ybWF0KFx1MDAyN3NlcV9sZW5cdTAwMjcsIFx1MDAyN3NjYWxlXHUwMDI3LCBcdTAwMjdyb3BlX3NwcmVhZFx1MDAyNywgXHUwMDI3eWFybl9zcHJlYWRcdTAwMjcpKVxuZm9yIHRlc3RfbGVuLCBzY2FsZSBpbiBbKDIwNDgsIDEuMCksICg0MDk2LCAyLjApLCAoODE5MiwgNC4wKSwgKDE2Mzg0LCA4LjApXTpcbiAgICBjX3N0ZCwgIF8gPSByb3BlX2NhY2hlKHRlc3RfbGVuLCBkX21vZGVsLCBzY2FsZT0xLjApXG4gICAgY195YXJuLCBfID0geWFybl9jYWNoZSh0ZXN0X2xlbiwgZF9tb2RlbCwgc2NhbGU9c2NhbGUpXG4gICAgc3RkX3NwICAgPSBjX3N0ZC5zdGQoZGltPTApLm1lYW4oKS5pdGVtKClcbiAgICB5YXJuX3NwICA9IGNfeWFybi5zdGQoZGltPTApLm1lYW4oKS5pdGVtKClcbiAgICBwcmludChcdTAwMjd7Olx1MDAzZTh9IHs6XHUwMDNlOC4xZn0gezpcdTAwM2UxNC40Zn0gezpcdTAwM2UxNC40Zn1cdTAwMjcuZm9ybWF0KHRlc3RfbGVuLCBzY2FsZSwgc3RkX3NwLCB5YXJuX3NwKSlcbnByaW50KFx1MDAyN1lhUk4gbWFpbnRhaW5zIGNvcy9zaW4gc3ByZWFkOyBuYWl2ZSB1bmlmb3JtIHNjYWxpbmcgY29sbGFwc2VzIGl0Llx1MDAyNykifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzcHJlYWQgbWV0cmljIGFib3ZlIG1lYXN1cmVzIGhvdyB3ZWxsIHRoZSBjb3Mvc2luIGNhY2hlIGRpc3Rpbmd1aXNoZXMgZGlmZmVyZW50IHBvc2l0aW9uczogYSBoaWdoIHNwcmVhZCBtZWFucyBtYW55IGRpc3RpbmN0IHJvdGF0aW9uIHN0YXRlcyAoZ29vZCksIHdoaWxlIGEgbG93IHNwcmVhZCBtZWFucyBtYW55IHBvc2l0aW9ucyBjb2xsYXBzZSB0byBzaW1pbGFyIGFuZ2xlcyAoYmFkKS4gQXQgMTYzODQgdG9rZW5zIHdpdGggbmFpdmUgUm9QRSAoc2NhbGU9MS4wKSwgbWFueSBoaWdoLWZyZXF1ZW5jeSBkaW1lbnNpb25zIGhhdmUgY29tcGxldGVkIG1hbnkgZnVsbCByb3RhdGlvbnMgKDLPgCBjeWNsZXMpIGFuZCBhbGlhcyB0byBwcmV2aW91c2x5IHNlZW4gYW5nbGVzIOKAlCB0aGUgbW9kZWwgY2Fubm90IGRpc3Rpbmd1aXNoIHBvc2l0aW9ucyAwIGFuZCA4MTkyIGluIHRob3NlIGRpbWVuc2lvbnMuIFlhUk5cdTAwMjdzIHNlbGVjdGl2ZSBzY2FsaW5nIHNsb3dzIGRvd24gdGhlIHJvdGF0aW9uIHJhdGVzIHNwZWNpZmljYWxseSBpbiB0aGUgZGltZW5zaW9ucyB3aGVyZSBhbGlhc2luZyB3b3VsZCBvY2N1ciwgbWFpbnRhaW5pbmcgZGlzdGluZ3Vpc2hhYmlsaXR5IGFjcm9zcyB0aGUgbG9uZ2VyIGNvbnRleHQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUm9QRSBpbiBQcm9kdWN0aW9uIExMTXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJvUEUgaGFzIGJlY29tZSB0aGUgZGUtZmFjdG8gcG9zaXRpb25hbCBlbmNvZGluZyBmb3IgZGVjb2Rlci1vbmx5IExMTXMgc2luY2UgMjAyMy4gSXRzIGNvbWJpbmF0aW9uIG9mIHJlbGF0aXZlLWluLXNjb3JlIGVuY29kaW5nLCB6ZXJvIGV4dHJhIHBhcmFtZXRlcnMsIGFuZCBzdXBwb3J0IGZvciBjb250ZXh0IGV4dGVuc2lvbiBoYXMgbWFkZSBpdCBkb21pbmFudC4gS2V5IGRlcGxveW1lbnQgbm90ZXM6IFJvUEUgaXMgYXBwbGllZCBpbmRlcGVuZGVudGx5IHRvIGVhY2ggYXR0ZW50aW9uIGhlYWQgKGVhY2ggaGVhZCBnZXRzIGl0cyBvd24gUSBhbmQgSyByb3RhdGVkIGJ5IHRoZSBzYW1lIHBvc2l0aW9uIGFuZ2xlcyk7IHRoZSBiYXNlIGZyZXF1ZW5jeSAoZGVmYXVsdCAxMDAwMCkgY2FuIGJlIGluY3JlYXNlZCB0byBzaGlmdCB0aGUgdXNlZnVsIHJhbmdlIHRvIGxvbmdlciBzZXF1ZW5jZXM7IFlhUk4gb3IgbGluZWFyIHNjYWxpbmcgd2l0aCBjb250aW51ZWQgcHJlLXRyYWluaW5nIGlzIHRoZSBzdGFuZGFyZCByZWNpcGUgZm9yIGV4dGVuZGluZyBhIDRLLWNvbnRleHQgbW9kZWwgdG8gMzJLIG9yIDEyOEsgY29udGV4dHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMTGFNQSAxLzI6IFJvUEUgd2l0aCBiYXNlPTEwMDAwLCBtYXhfc2VxX2xlbj00MDk2IChMTGFNQS0yKSIsIkxMYU1BLTM6IFJvUEUgd2l0aCBiYXNlPTUwMDAwMCwgZXh0ZW5kZWQgdG8gMTI4SyB2aWEgbG9uZy1jb250ZXh0IGZpbmUtdHVuaW5nIiwiTWlzdHJhbCA3QjogUm9QRSBiYXNlPTEwMDAwLCBzbGlkaW5nIHdpbmRvdyBhdHRlbnRpb24gZm9yIGVmZmljaWVudCAzMksgY29udGV4dCIsIkZhbGNvbjogUm9QRSB3aXRoIGJhc2U9MTAwMDAgYWNyb3NzIDdCLCA0MEIsIDE4MEIgbW9kZWwgc2l6ZXMiLCJRd2VuIDEvMjogUm9QRSB3aXRoIGR5bmFtaWMgTlRLIHNjYWxpbmcgZm9yIDhLLTMySyBjb250ZXh0IiwiR1BULU5lb1ggLyBQeXRoaWE6IFJvUEUgYXMgdGhlIGRlZmF1bHQgUEUgZm9yIG9wZW4gcmVwcm9kdWN0aW9uIG9mIEdQVC1jbGFzcyBtb2RlbHMiLCJDb2RlIExsYW1hOiBSb1BFIGJhc2U9MTAwMDAwMCAoMU0pIGZvciBsb25nIGNvZGUgY29udGV4dHMgdXAgdG8gMTAwSyB0b2tlbnMiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiDigJQgU2ludXNvaWRhbCB2cyBMZWFybmVkIHZzIFJvUEUgdnMgQUxpQmkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiUmVsYXRpdmUgaW4gU2NvcmUiLCJObyBQYXJhbXMiLCJFeHRyYXBvbGF0aW9uIiwiTExNIEFkb3B0aW9uIiwiU2NvcmUgQ29tcGxleGl0eSJdLCJyb3dzIjpbWyJTaW51c29pZGFsIFBFIiwiTm8g4oCUIGFic29sdXRlIG9ubHkiLCJZZXMiLCJXZWFrIOKAlCBwZXJpb2RpYyBhbGlhc2luZyIsIkxvdyDigJQgbGVnYWN5IG9ubHkiLCJPKG5kKSBwcmVjb21wdXRlIl0sWyJMZWFybmVkIFBFIiwiTm8g4oCUIGFic29sdXRlIG9ubHkiLCJObyDigJQgbWF4X2xlbsOXZF9tb2RlbCIsIk5vbmUg4oCUIGhhcmQgZmFpbHVyZSIsIk1lZGl1bSDigJQgQkVSVCwgR1BULTIiLCJPKG5kKSBsb29rdXAiXSxbIlJvUEUiLCJZZXMg4oCUIHJvdGF0aW9uIGVuY29kZXMgZGlzdGFuY2UiLCJZZXMg4oCUIHplcm8gcGFyYW1zIiwiR29vZCDigJQgWWFSTi9OVEsgZXh0ZW5kcyB0byAxMDBLKyIsIlZlcnkgaGlnaCDigJQgTExhTUEsIE1pc3RyYWwsIFF3ZW4iLCJPKG5kKSBwZXIgbGF5ZXIiXSxbIkFMaUJpIiwiWWVzIOKAlCBhZGRpdGl2ZSBsaW5lYXIgYmlhcyIsIlllcyDigJQgaCBzbG9wZXMgb25seSIsIlN0cm9uZyDigJQgbGluZWFyIGV4dHJhcG9sYXRlcyBuYXR1cmFsbHkiLCJNZWRpdW0g4oCUIE1QVCwgQkxPT00iLCJPKG7CsikgYmlhcyBhZGQiXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# RoPE — Rotary Position Embeddings and Long-Context Extension

RoPE (Rotary Position Embeddings), introduced by Su et al. (2021) in RoFormer, encodes position information by rotating the query and key vectors before computing the dot product. The key mathematical insight is that if you rotate a vector at position m by angle m·θ and a vector at position n by angle n·θ, their dot product involves only the relative angle (m−n)·θ — the absolute positions cancel out. This gives RoPE the best of both worlds: it encodes relative position directly in the attention score (like relative PE schemes) while being computed as a simple multiplicative operation on existing Q/K vectors (like absolute PE), with zero additional parameters.

## RoPE Mathematical Foundation — Rotation in 2D Subspaces

RoPE splits the d_model dimension into d/2 pairs. For pair k, the rotation angle is θ_k = 10000^{-2k/d}, matching the frequency schedule of sinusoidal PE. For a vector at position m, pair k is rotated by m·θ_k: the 2D rotation [x1, x2] → [x1·cos(mθ_k) − x2·sin(mθ_k), x1·sin(mθ_k) + x2·cos(mθ_k)]. When computing the dot product of rotated query q_m and rotated key k_n: (R_m·q)^T · (R_n·k) = q^T · R_{n-m} · k — only the relative position (n−m) appears. This holds exactly for any choice of q and k vectors, making RoPE a parameter-free mechanism that provably encodes relative distance without any approximation.

The frequency schedule θ_k = 10000^{-2k/d} means low-index pairs (k=0) rotate fast (θ_0 = 1) while high-index pairs (k=d/2−1) rotate slowly (θ_{d/2-1} ≈ 10000^{-1} = 0.0001). Short-range dependencies are captured by fast-rotating pairs; long-range dependencies by slow-rotating pairs. This matches the frequency spectrum of sinusoidal PE and is the same schedule used in the original Transformer. The base 10000 can be changed: larger base = slower rotation = better long-context (used in Code Llama, Llama-3 with base=500000).

## Implementing RoPE from Scratch

The standard implementation precomputes a (max_seq_len, d/2) table of cos(m·θ_k) and sin(m·θ_k) values. At forward time, these are used to rotate each Q and K vector: the first half of the vector is [x1·cos − x2·sin] and the second half is [x1·sin + x2·cos]. This is equivalent to complex multiplication: treating each pair (x1, x2) as a complex number x1 + i·x2 and multiplying by e^{i·m·θ_k}. The rotate_half trick avoids materialising the full rotation matrix and operates with element-wise multiplications on half-shifted slices.

```python
import torch
import math

def build_rope_cache(seq_len, d_model, base=10000):
    # Precompute cos/sin tables for RoPE. d_model must be even.
    assert d_model % 2 == 0
    half  = d_model // 2
    k     = torch.arange(half, dtype=torch.float32)
    theta = base ** (-2 * k / d_model)            # (half,) frequencies
    pos   = torch.arange(seq_len, dtype=torch.float32)
    freqs = torch.outer(pos, theta)               # (seq_len, half)
    return torch.cos(freqs), torch.sin(freqs)

def apply_rope(x, cos, sin):
    # Apply RoPE to x: (batch, seq_len, d_model)
    x1, x2 = x[..., :x.shape[-1]//2], x[..., x.shape[-1]//2:]
    cos = cos[:x.shape[1]].unsqueeze(0)           # (1, seq_len, half)
    sin = sin[:x.shape[1]].unsqueeze(0)
    x_rot = torch.cat([x1 * cos - x2 * sin, x1 * sin + x2 * cos], dim=-1)
    return x_rot

torch.manual_seed(42)
seq_len, d_model = 16, 64
cos_cache, sin_cache = build_rope_cache(seq_len, d_model)
print('cos cache shape:', cos_cache.shape, ' sin cache shape:', sin_cache.shape)

Q = torch.randn(1, seq_len, d_model)
K = torch.randn(1, seq_len, d_model)
Q_rot = apply_rope(Q, cos_cache, sin_cache)
K_rot = apply_rope(K, cos_cache, sin_cache)
print('Q:', Q.shape, '-> Q_rot:', Q_rot.shape)
scores = (Q_rot @ K_rot.transpose(-2, -1)) / d_model ** 0.5
print('Score matrix shape:', scores.shape)
print('Scores encode only relative position — no absolute index needed.')
```

## Verifying the Relative Distance Property

The defining property of RoPE is that the attention score between a rotated query at position p_q and a rotated key at position p_k depends only on (p_q − p_k), not on the absolute values of p_q or p_k individually. We can verify this numerically: fix q and k vectors, rotate them at different absolute position pairs that share the same relative distance, and confirm the dot products are identical. For example, (pos_q=0, pos_k=2) and (pos_q=1, pos_k=3) both have relative distance −2 and should yield the same dot product.

```python
import torch
import math

def build_rope(seq_len, d_model, base=10000):
    half  = d_model // 2
    theta = torch.tensor([base ** (-2*k/d_model) for k in range(half)])
    freqs = torch.outer(torch.arange(seq_len, dtype=torch.float32), theta)
    return torch.cos(freqs), torch.sin(freqs)

def rotate_vec(v, pos, cos, sin):
    c, s = cos[pos], sin[pos]
    v1, v2 = v[:len(v)//2], v[len(v)//2:]
    return torch.cat([v1*c - v2*s, v1*s + v2*c])

torch.manual_seed(0)
d_model = 16
cos, sin = build_rope(20, d_model)
q = torch.randn(d_model)
k = torch.randn(d_model)

print('Verifying: dot(q_rot@pq, k_rot@pk) depends only on (pq - pk)')
print('{:>6} {:>6} {:>10} {:>14}'.format('pos_q', 'pos_k', 'relative', 'dot_score'))
for pq, pk in [(0,0),(1,1),(5,5),(0,2),(1,3),(5,7),(0,4),(1,5)]:
    q_r = rotate_vec(q, pq, cos, sin)
    k_r = rotate_vec(k, pk, cos, sin)
    dot = (q_r * k_r).sum().item()
    print('{:>6} {:>6} {:>10} {:>14.6f}'.format(pq, pk, pq-pk, dot))
print('Pairs (0,-2), (1,-2), (5,-2) should give identical dot scores.')
```

> **RoPE Has Zero Trainable Parameters**: Unlike learned PE (which has max_len × d_model parameters) or Shaw-style relative PE (which has (2×max_rel+1) × d_model parameters), RoPE adds exactly zero trainable parameters. The cos/sin tables are computed from a fixed formula and stored as non-gradient buffers. This means RoPE's position encoding capacity comes entirely from the model learning to use rotated Q/K vectors — the rotation schedule itself is a hyperparameter, not a learned one. Changing the base from 10000 to 500000 (as in LLaMA-3) shifts the frequency spectrum without adding any parameters.

## Efficient RoPE with Precomputed cos/sin Cache

Production implementations register the cos/sin tables as non-trainable buffers using register_buffer, ensuring they are moved to the correct device with the model without appearing in model.parameters(). The tables are precomputed for the maximum expected sequence length at initialisation. At forward time, the first T rows are sliced for the actual sequence. The rotate_half operation — negating the second half and swapping — enables the rotation using only element-wise multiplication and addition, avoiding any explicit rotation matrix. This is the implementation used in HuggingFace transformers for LLaMA, Mistral, and similar models.

```python
import torch
import torch.nn as nn

class RotaryEmbedding(nn.Module):
    # Production RoPE: precomputed cos/sin cache, no learned parameters.
    def __init__(self, dim, max_seq_len=4096, base=10000):
        super().__init__()
        inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer('inv_freq', inv_freq)
        t     = torch.arange(max_seq_len).float()
        freqs = torch.outer(t, inv_freq)
        emb   = torch.cat([freqs, freqs], dim=-1)   # (max_seq_len, dim)
        self.register_buffer('cos_cached', emb.cos())
        self.register_buffer('sin_cached', emb.sin())

    @staticmethod
    def rotate_half(x):
        x1, x2 = x[..., :x.shape[-1]//2], x[..., x.shape[-1]//2:]
        return torch.cat([-x2, x1], dim=-1)

    def forward(self, q, k):
        T   = q.shape[-2]
        cos = self.cos_cached[:T].unsqueeze(0).unsqueeze(0)
        sin = self.sin_cached[:T].unsqueeze(0).unsqueeze(0)
        return (q * cos + self.rotate_half(q) * sin,
                k * cos + self.rotate_half(k) * sin)

rope = RotaryEmbedding(dim=64, max_seq_len=2048)
b, h, s, d = 2, 8, 128, 64
q = torch.randn(b, h, s, d)
k = torch.randn(b, h, s, d)
q_rot, k_rot = rope(q, k)
print('Input q:', q.shape, '-> q_rot:', q_rot.shape)
print('Trainable parameters:', sum(p.numel() for p in rope.parameters()))
print('Buffers (not trained):', [name for name, _ in rope.named_buffers()])
print('RoPE adds zero trainable parameters to the model.')
```

## YaRN — Long-Context Extension Beyond Training Length

Naive RoPE extrapolation (using position indices beyond the training maximum) causes the attention scores to involve rotation angles the model never saw during training, degrading quality. YaRN (Peng et al. 2023) addresses this by selectively scaling the θ frequencies: high-frequency dimensions (small wavelength) are left unchanged because they already see diverse relative distances within the training length; low-frequency dimensions (large wavelength) are scaled down by a factor equal to the context extension ratio. This selective scaling keeps the per-dimension rotation rates within the distribution seen during training while physically accommodating longer sequences. YaRN also adjusts the softmax temperature to compensate for score magnitude changes.

```python
import torch
import math

def rope_cache(seq_len, d_model, scale=1.0, base=10000):
    # Standard RoPE with optional uniform frequency scaling.
    half  = d_model // 2
    k     = torch.arange(half, dtype=torch.float32)
    theta = base ** (-2 * k / d_model) / scale
    freqs = torch.outer(torch.arange(seq_len, dtype=torch.float32), theta)
    return torch.cos(freqs), torch.sin(freqs)

def yarn_cache(seq_len, d_model, scale, base=10000, beta_fast=32, beta_slow=1):
    # YaRN: selective scaling — high-freq dims unchanged, low-freq scaled.
    half    = d_model // 2
    k       = torch.arange(half, dtype=torch.float32)
    theta   = base ** (-2 * k / d_model)
    wavelen = 2 * math.pi / (theta + 1e-9)
    scaled        = theta.clone()
    low_mask      = wavelen > scale * beta_slow
    scaled[low_mask] /= scale
    freqs = torch.outer(torch.arange(seq_len, dtype=torch.float32), scaled)
    return torch.cos(freqs), torch.sin(freqs)

d_model = 64
print('{:>8} {:>8} {:>14} {:>14}'.format('seq_len', 'scale', 'rope_spread', 'yarn_spread'))
for test_len, scale in [(2048, 1.0), (4096, 2.0), (8192, 4.0), (16384, 8.0)]:
    c_std,  _ = rope_cache(test_len, d_model, scale=1.0)
    c_yarn, _ = yarn_cache(test_len, d_model, scale=scale)
    std_sp   = c_std.std(dim=0).mean().item()
    yarn_sp  = c_yarn.std(dim=0).mean().item()
    print('{:>8} {:>8.1f} {:>14.4f} {:>14.4f}'.format(test_len, scale, std_sp, yarn_sp))
print('YaRN maintains cos/sin spread; naive uniform scaling collapses it.')
```

The spread metric above measures how well the cos/sin cache distinguishes different positions: a high spread means many distinct rotation states (good), while a low spread means many positions collapse to similar angles (bad). At 16384 tokens with naive RoPE (scale=1.0), many high-frequency dimensions have completed many full rotations (2π cycles) and alias to previously seen angles — the model cannot distinguish positions 0 and 8192 in those dimensions. YaRN's selective scaling slows down the rotation rates specifically in the dimensions where aliasing would occur, maintaining distinguishability across the longer context.

## RoPE in Production LLMs

RoPE has become the de-facto positional encoding for decoder-only LLMs since 2023. Its combination of relative-in-score encoding, zero extra parameters, and support for context extension has made it dominant. Key deployment notes: RoPE is applied independently to each attention head (each head gets its own Q and K rotated by the same position angles); the base frequency (default 10000) can be increased to shift the useful range to longer sequences; YaRN or linear scaling with continued pre-training is the standard recipe for extending a 4K-context model to 32K or 128K contexts.

- LLaMA 1/2: RoPE with base=10000, max_seq_len=4096 (LLaMA-2)
- LLaMA-3: RoPE with base=500000, extended to 128K via long-context fine-tuning
- Mistral 7B: RoPE base=10000, sliding window attention for efficient 32K context
- Falcon: RoPE with base=10000 across 7B, 40B, 180B model sizes
- Qwen 1/2: RoPE with dynamic NTK scaling for 8K-32K context
- GPT-NeoX / Pythia: RoPE as the default PE for open reproduction of GPT-class models
- Code Llama: RoPE base=1000000 (1M) for long code contexts up to 100K tokens

## Comparison — Sinusoidal vs Learned vs RoPE vs ALiBi

| Method | Relative in Score | No Params | Extrapolation | LLM Adoption | Score Complexity |
| --- | --- | --- | --- | --- | --- |
| Sinusoidal PE | No — absolute only | Yes | Weak — periodic aliasing | Low — legacy only | O(nd) precompute |
| Learned PE | No — absolute only | No — max_len×d_model | None — hard failure | Medium — BERT, GPT-2 | O(nd) lookup |
| RoPE | Yes — rotation encodes distance | Yes — zero params | Good — YaRN/NTK extends to 100K+ | Very high — LLaMA, Mistral, Qwen | O(nd) per layer |
| ALiBi | Yes — additive linear bias | Yes — h slopes only | Strong — linear extrapolates naturally | Medium — MPT, BLOOM | O(n²) bias add |

---

