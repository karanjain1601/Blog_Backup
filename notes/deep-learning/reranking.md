---
title: "Reranking for RAG"
slug: "reranking"
description: "Using cross-encoder models to re-score an initial set of retrieved candidates for relevance, dramatically improving precision at the cost of additional latency — the most reliable RAG quality booster."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVyYW5raW5nIGlzIGEgc2Vjb25kLXN0YWdlIHJlbGV2YW5jZSBzY29yaW5nIHN0ZXAgYXBwbGllZCBhZnRlciBhbiBpbml0aWFsIHJldHJpZXZhbCBwaGFzZS4gVGhlIGluaXRpYWwgcmV0cmlldmFsIOKAlCB0eXBpY2FsbHkgYSBiaS1lbmNvZGVyIGRlbnNlIHNlYXJjaCBvciBCTTI1IOKAlCByZXR1cm5zIGEgYnJvYWQgY2FuZGlkYXRlIHNldCBvZiAyMOKAkzEwMCBkb2N1bWVudHMgcXVpY2tseSBidXQgaW1wcmVjaXNlbHksIGJlY2F1c2UgYmktZW5jb2RlcnMgY29tcHJlc3MgcXVlcnkgYW5kIGRvY3VtZW50IGludG8gZml4ZWQgdmVjdG9ycyBpbmRlcGVuZGVudGx5IGJlZm9yZSBjb21wYXJpbmcgdGhlbS4gQSByZXJhbmtlciB0aGVuIGpvaW50bHkgZW5jb2RlcyBlYWNoIHF1ZXJ5LWRvY3VtZW50IHBhaXIgdGhyb3VnaCBhIGNyb3NzLWVuY29kZXIsIHByb2R1Y2luZyBhIG11Y2ggbW9yZSBhY2N1cmF0ZSByZWxldmFuY2Ugc2NvcmUuIFRoZSB0b3AtayByZXJhbmtlZCBkb2N1bWVudHMgKHR5cGljYWxseSAz4oCTMTApIGFyZSBwYXNzZWQgdG8gdGhlIExMTS4gUmVyYW5raW5nIHR5cGljYWxseSBpbXByb3ZlcyBhbnN3ZXIgYWNjdXJhY3kgYnkgMTXigJMzMCUgb24gZG9tYWluLXNwZWNpZmljIFJBRyBiZW5jaG1hcmtzLCBtYWtpbmcgaXQgdGhlIHNpbmdsZSBoaWdoZXN0LVJPSSBpbXByb3ZlbWVudCBhdmFpbGFibGUgdG8gYSBiYXNpYyByZXRyaWV2YWwgcGlwZWxpbmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc3RhbmRhcmQgUkFHIHBpcGVsaW5lIHdpdGhvdXQgcmVyYW5raW5nIHN1ZmZlcnMgZnJvbSBhIHByZWNpc2lvbiBwcm9ibGVtOiB0aGUgdmVjdG9yIHNpbWlsYXJpdHkgYmV0d2VlbiBhIHF1ZXJ5IGVtYmVkZGluZyBhbmQgYSBkb2N1bWVudCBlbWJlZGRpbmcgaXMgYSBjb2Fyc2UgcmVsZXZhbmNlIHByb3h5LCBiZWNhdXNlIGJvdGggYXJlIGNvbXByZXNzZWQgaW50byBhIGZpeGVkLXNpemUgdmVjdG9yIGluZGVwZW5kZW50bHkgYmVmb3JlIGNvbXBhcmlzb24uIFRoZSBkb3QgcHJvZHVjdCBtZWFzdXJlcyBnZW9tZXRyaWMgcHJveGltaXR5IGluIGVtYmVkZGluZyBzcGFjZSwgbm90IHNlbWFudGljIGVudGFpbG1lbnQuIEEgZG9jdW1lbnQgdGhhdCBzaGFyZXMgdm9jYWJ1bGFyeSB3aXRoIHRoZSBxdWVyeSBidXQgZG9lcyBub3QgYWN0dWFsbHkgYW5zd2VyIGl0IGNhbiByYW5rIGhpZ2hlciB0aGFuIGEgZG9jdW1lbnQgdGhhdCBhbnN3ZXJzIHRoZSBxdWVyeSB1c2luZyBkaWZmZXJlbnQgd29yZHMuIFJlcmFua2luZyBhZGRyZXNzZXMgdGhpcyBieSBhcHBseWluZyBhIGNyb3NzLWVuY29kZXIgdGhhdCBhdHRlbmRzIG92ZXIgdGhlIGZ1bGwgcXVlcnktZG9jdW1lbnQgcGFpciBqb2ludGx5LCB1c2luZyBpdHMgZnVsbCBCRVJULXN0eWxlIGF0dGVudGlvbiB0byBkZXRlY3Qgd2hldGhlciB0aGUgZG9jdW1lbnQgYWN0dWFsbHkgY29udGFpbnMgdGhlIGFuc3dlciB0byB0aGUgcXVlcnkuIFRoZSBjb3N0IGlzIHF1YWRyYXRpYyBpbiB0aGUgbnVtYmVyIG9mIGNhbmRpZGF0ZXMgKGVhY2ggcXVlcnktZG9jdW1lbnQgcGFpciBpcyBzY29yZWQgaW5kZXBlbmRlbnRseSksIGJ1dCBzaW5jZSB0aGUgY2FuZGlkYXRlIHNldCBpcyBzbWFsbCAoMjDigJMxMDAgZG9jcyksIHRoZSBsYXRlbmN5IGlzIGFjY2VwdGFibGUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmktRW5jb2RlciB2cyBDcm9zcy1FbmNvZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCaS1lbmNvZGVycyAodXNlZCBpbiBkZW5zZSByZXRyaWV2YWwpIGVuY29kZSBxdWVyeSBhbmQgZG9jdW1lbnQgc2VwYXJhdGVseTogZW5jb2RlKHF1ZXJ5KSDihpIgcV92ZWN0b3IsIGVuY29kZShkb2MpIOKGkiBkX3ZlY3Rvciwgc2NvcmUgPSBkb3QocV92ZWN0b3IsIGRfdmVjdG9yKS4gVGhpcyBhbGxvd3MgZG9jdW1lbnRzIHRvIGJlIHByZS1lbmNvZGVkIG9mZmxpbmUgYW5kIGluZGV4ZWQgaW4gRkFJU1MsIGVuYWJsaW5nIHN1Yi1taWxsaXNlY29uZCByZXRyaWV2YWwgb3ZlciBtaWxsaW9ucyBvZiBkb2N1bWVudHMgYXQgcXVlcnkgdGltZS4gVGhlIHByaWNlIGlzIHRoZSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrOiB0aGUgZml4ZWQtc2l6ZSB2ZWN0b3IgY2Fubm90IGNhcHR1cmUgZmluZS1ncmFpbmVkIGludGVyYWN0aW9ucyBiZXR3ZWVuIHF1ZXJ5IHRva2VucyBhbmQgZG9jdW1lbnQgdG9rZW5zLiBDcm9zcy1lbmNvZGVycyBwcm9jZXNzIHRoZSBjb25jYXRlbmF0ZWQgcXVlcnkgYW5kIGRvY3VtZW50IGFzIGEgc2luZ2xlIGlucHV0IHNlcXVlbmNlOiBlbmNvZGUoW0NMU10gcXVlcnkgW1NFUF0gZG9jdW1lbnQgW1NFUF0pIOKGkiBzY2FsYXIgc2NvcmUuIFRoZSBmdWxsIHNlbGYtYXR0ZW50aW9uIG92ZXIgdGhlIGNvbWJpbmVkIHNlcXVlbmNlIGFsbG93cyBldmVyeSBxdWVyeSB0b2tlbiB0byBkaXJlY3RseSBhdHRlbmQgdG8gZXZlcnkgZG9jdW1lbnQgdG9rZW4sIHByb2R1Y2luZyBhIG11Y2ggbW9yZSBhY2N1cmF0ZSByZWxldmFuY2Ugc2NvcmUuIENyb3NzLWVuY29kZXJzIGNhbm5vdCBiZSBwcmUtaW5kZXhlZCBhbmQgc2NhbGUgbGluZWFybHkgd2l0aCB0aGUgbnVtYmVyIG9mIGNhbmRpZGF0ZXMgc2NvcmVkLCBzbyB0aGV5IGFyZSB1c2VkIG9ubHkgb24gdGhlIHNtYWxsIGNhbmRpZGF0ZSBzZXQgcmV0dXJuZWQgYnkgdGhlIGJpLWVuY29kZXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gc2VudGVuY2VfdHJhbnNmb3JtZXJzIGltcG9ydCBDcm9zc0VuY29kZXIsIFNlbnRlbmNlVHJhbnNmb3JtZXJcbmltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IGZhaXNzXG5cbmRlZiByZXRyaWV2ZV9jYW5kaWRhdGVzKHF1ZXJ5OiBzdHIsIGRvY3M6IGxpc3QsIGJpX21vZGVsX25hbWU6IHN0ciwgdG9wX246IGludCA9IDIwKSAtXHUwMDNlIGxpc3Q6XG4gICAgXCJcIlwiRmFzdCBiaS1lbmNvZGVyIHJldHJpZXZhbDogcmV0dXJuIGluZGljZXMgb2YgdG9wX24gY2FuZGlkYXRlIGRvY3VtZW50cy5cIlwiXCJcbiAgICBtb2RlbCAgPSBTZW50ZW5jZVRyYW5zZm9ybWVyKGJpX21vZGVsX25hbWUpXG4gICAgZF9lbWJzID0gbW9kZWwuZW5jb2RlKGRvY3MsIG5vcm1hbGl6ZV9lbWJlZGRpbmdzPVRydWUpLmFzdHlwZShucC5mbG9hdDMyKVxuICAgIHFfZW1iICA9IG1vZGVsLmVuY29kZShbcXVlcnldLCBub3JtYWxpemVfZW1iZWRkaW5ncz1UcnVlKS5hc3R5cGUobnAuZmxvYXQzMilcbiAgICBpbmRleCAgPSBmYWlzcy5JbmRleEZsYXRJUChkX2VtYnMuc2hhcGVbMV0pXG4gICAgaW5kZXguYWRkKGRfZW1icylcbiAgICBfLCBpZHhzID0gaW5kZXguc2VhcmNoKHFfZW1iLCBtaW4odG9wX24sIGxlbihkb2NzKSkpXG4gICAgcmV0dXJuIGlkeHNbMF0udG9saXN0KClcblxuZGVmIGNyb3NzX2VuY29kZXJfcmVyYW5rKHF1ZXJ5OiBzdHIsIGRvY3M6IGxpc3QsIGNhbmRpZGF0ZV9pZHhzOiBsaXN0LFxuICAgICAgICAgICAgICAgICAgICAgICAgICBjZV9tb2RlbDogc3RyID0gXCJjcm9zcy1lbmNvZGVyL21zLW1hcmNvLU1pbmlMTS1MLTYtdjJcIikgLVx1MDAzZSBsaXN0OlxuICAgIFwiXCJcIlNjb3JlIGVhY2ggcXVlcnktY2FuZGlkYXRlIHBhaXIgd2l0aCBhIGNyb3NzLWVuY29kZXI7IHJldHVybiBzb3J0ZWQgcmVzdWx0cy5cIlwiXCJcbiAgICByZXJhbmtlciAgPSBDcm9zc0VuY29kZXIoY2VfbW9kZWwsIG1heF9sZW5ndGg9NTEyKVxuICAgIHBhaXJzICAgICA9IFsocXVlcnksIGRvY3NbaV0pIGZvciBpIGluIGNhbmRpZGF0ZV9pZHhzXVxuICAgIHNjb3JlcyAgICA9IHJlcmFua2VyLnByZWRpY3QocGFpcnMpXG4gICAgcmFua2VkICAgID0gc29ydGVkKHppcChjYW5kaWRhdGVfaWR4cywgc2NvcmVzKSwga2V5PWxhbWJkYSB4OiB4WzFdLCByZXZlcnNlPVRydWUpXG4gICAgcmV0dXJuIFt7XCJkb2NfaWR4XCI6IGlkeCwgXCJjZV9zY29yZVwiOiBmbG9hdChzYyksIFwidGV4dFwiOiBkb2NzW2lkeF1bOjgwXX1cbiAgICAgICAgICAgIGZvciBpZHgsIHNjIGluIHJhbmtlZF1cblxuZG9jcyAgPSBbZlwiRG9jdW1lbnQge2l9OiB0b3BpYyBhYm91dCBOTFAgdGVjaG5pcXVlIHtpICUgOH0uXCIgZm9yIGkgaW4gcmFuZ2UoMzApXVxucXVlcnkgPSBcImhvdyBkb2VzIHJldHJpZXZhbCBhdWdtZW50ZWQgZ2VuZXJhdGlvbiBpbXByb3ZlIExMTSBhY2N1cmFjeVwiXG5jYW5kcyA9IHJldHJpZXZlX2NhbmRpZGF0ZXMocXVlcnksIGRvY3MsIFwiYWxsLU1pbmlMTS1MNi12MlwiLCB0b3Bfbj0yMClcbnByaW50KGZcIkJpLWVuY29kZXIgdG9wLTMgKG9yaWcgb3JkZXIpOiB7Y2FuZHNbOjNdfVwiKVxucmVzdWx0cyA9IGNyb3NzX2VuY29kZXJfcmVyYW5rKHF1ZXJ5LCBkb2NzLCBjYW5kcylcbnByaW50KGZcIkNyb3NzLWVuY29kZXIgdG9wLTM6IHtbcltcdTAwMjdkb2NfaWR4XHUwMDI3XSBmb3IgciBpbiByZXN1bHRzWzozXV19XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtRW5jb2RlciBBcmNoaXRlY3R1cmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgY3Jvc3MtZW5jb2RlciBmb3IgcmVyYW5raW5nIGlzIGEgc3RhbmRhcmQgQkVSVC1zdHlsZSB0cmFuc2Zvcm1lciB3aXRoIGEgbGluZWFyIGhlYWQgb24gdGhlIFtDTFNdIHRva2VuIHRoYXQgb3V0cHV0cyBhIHNpbmdsZSBzY2FsYXIgcmVsZXZhbmNlIHNjb3JlLiBUaGUgbW9kZWwgaXMgZmluZS10dW5lZCBvbiBNUy1NQVJDTyBvciBzaW1pbGFyIHBhc3NhZ2UtcmFua2luZyBkYXRhc2V0cyB1c2luZyBhIHBvaW50d2lzZSBvciBsaXN0d2lzZSBsb3NzOiBnaXZlbiBhIHF1ZXJ5LCBhIHJlbGV2YW50IHBhc3NhZ2UsIGFuZCBzZXZlcmFsIGlycmVsZXZhbnQgcGFzc2FnZXMsIHRoZSBtb2RlbCBsZWFybnMgdG8gYXNzaWduIGEgaGlnaGVyIHNjb3JlIHRvIHRoZSByZWxldmFudCBwYXNzYWdlLiBUaGUgbW9zdCBjb21tb25seSB1c2VkIGNyb3NzLWVuY29kZXJzIGFyZSB0aGUgbXMtbWFyY28tTWluaUxNIGZhbWlseSBmcm9tIHRoZSBzZW50ZW5jZS10cmFuc2Zvcm1lcnMgbGlicmFyeS4gTWluaUxNLUwtNi12MiBoYXMgNiBsYXllcnMgYW5kIH4yMk0gcGFyYW1ldGVycywgc2NvcmluZyAxMDAgcGFzc2FnZXMgaW4gYWJvdXQgNTBtcyBvbiBDUFUg4oCUIGEgcHJhY3RpY2FsIGxhdGVuY3kgZm9yIHJldHJpZXZhbCBwaXBlbGluZXMuIFRoZSBmdWxsIEJFUlQtbGFyZ2UgY3Jvc3MtZW5jb2RlciAobXMtbWFyY28tYmVydC1iYXNlKSBpcyBtb3JlIGFjY3VyYXRlIGJ1dCB0YWtlcyB+MjAwbXMgZm9yIDEwMCBwYXNzYWdlcy4gRm9yIGxhdGVuY3ktc2Vuc2l0aXZlIHBpcGVsaW5lcywgTWluaUxNLUwtNiBhdCB0b3AtNTAgY2FuZGlkYXRlcyBpcyB0aGUgcmVjb21tZW5kZWQgZGVmYXVsdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplciwgQXV0b01vZGVsXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBjb2xiZXJ0X2VuY29kZSh0ZXh0czogbGlzdCwgbW9kZWwsIHRva2VuaXplciwgZGV2aWNlOiBzdHIgPSBcImNwdVwiKSAtXHUwMDNlIHR1cGxlOlxuICAgIFwiXCJcIkVuY29kZSB0ZXh0cyB0byBwZXItdG9rZW4gZW1iZWRkaW5ncyAoYmF0Y2gsIHNlcV9sZW4sIGRpbSkgZm9yIENvbEJFUlQgc2NvcmluZy5cIlwiXCJcbiAgICBlbmMgPSB0b2tlbml6ZXIodGV4dHMsIHBhZGRpbmc9VHJ1ZSwgdHJ1bmNhdGlvbj1UcnVlLFxuICAgICAgICAgICAgICAgICAgICBtYXhfbGVuZ3RoPTEyOCwgcmV0dXJuX3RlbnNvcnM9XCJwdFwiKS50byhkZXZpY2UpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG91dCA9IG1vZGVsKCoqZW5jKVxuICAgICMgTm9ybWFsaXNlIGVhY2ggdG9rZW4gZW1iZWRkaW5nIHRvIHRoZSB1bml0IHNwaGVyZVxuICAgIHRva2VuX2VtYnMgPSBGLm5vcm1hbGl6ZShvdXQubGFzdF9oaWRkZW5fc3RhdGUsIHA9MiwgZGltPS0xKVxuICAgIHJldHVybiB0b2tlbl9lbWJzLCBlbmNbXCJhdHRlbnRpb25fbWFza1wiXVxuXG5kZWYgY29sYmVydF9tYXhzaW0ocV9lbWJzOiB0b3JjaC5UZW5zb3IsIGRfZW1iczogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICBxX21hc2s6IHRvcmNoLlRlbnNvciwgZF9tYXNrOiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiTWF4U2ltIHNjb3JlOiBzdW0gb3ZlciBxdWVyeSB0b2tlbnMgb2YgbWF4IGNvc2luZSBzaW1pbGFyaXR5IHRvIGFueSBkb2MgdG9rZW4uXCJcIlwiXG4gICAgc2ltcyA9IHRvcmNoLm1hdG11bChxX2VtYnNbMF0sIGRfZW1ic1swXS5UKSAgICMgKHFfbGVuLCBkX2xlbilcbiAgICBzaW1zWzosIGRfbWFza1swXSA9PSAwXSA9IC0xZTkgICAgICAgICAgICAgICAgICMgbWFzayBwYWRkaW5nIGluIGRvY1xuICAgIG1heF9zaW1zID0gc2ltcy5tYXgoZGltPS0xKS52YWx1ZXMgICAgICAgICAgICAgIyAocV9sZW4sKVxuICAgIG1heF9zaW1zW3FfbWFza1swXSA9PSAwXSA9IDAuMCAgICAgICAgICAgICAgICAjIG1hc2sgcGFkZGluZyBpbiBxdWVyeVxuICAgIHJldHVybiBtYXhfc2ltcy5zdW0oKS5pdGVtKClcblxubW9kZWxfbmFtZSA9IFwiYmVydC1iYXNlLXVuY2FzZWRcIlxudG9rICAgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxubW9kZWwgPSBBdXRvTW9kZWwuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG5xdWVyeSAgICA9IFwid2hhdCBpcyByZXRyaWV2YWwgYXVnbWVudGVkIGdlbmVyYXRpb25cIlxucGFzc2FnZXMgPSBbXCJSQUcgY29tYmluZXMgcmV0cmlldmFsIHdpdGggZ2VuZXJhdGlvbiB0byBncm91bmQgTExNIGFuc3dlcnMgaW4gcmVhbCBkb2N1bWVudHMuXCIsXG4gICAgICAgICAgICBcIkNvbnZvbHV0aW9uYWwgbmV0d29ya3MgcHJvY2VzcyBpbWFnZXMgdGhyb3VnaCBsb2NhbCBmaWx0ZXIgb3BlcmF0aW9ucy5cIl1cbnFfZW1icywgcV9tYXNrID0gY29sYmVydF9lbmNvZGUoW3F1ZXJ5XSwgbW9kZWwsIHRvaylcbmZvciBwIGluIHBhc3NhZ2VzOlxuICAgIGRfZW1icywgZF9tYXNrID0gY29sYmVydF9lbmNvZGUoW3BdLCBtb2RlbCwgdG9rKVxuICAgIHNjb3JlID0gY29sYmVydF9tYXhzaW0ocV9lbWJzLCBkX2VtYnMsIHFfbWFzaywgZF9tYXNrKVxuICAgIHByaW50KGZcIkNvbEJFUlQgc2NvcmUge3Njb3JlOi4zZn06IHtwWzo2MF19XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29sQkVSVCBMYXRlIEludGVyYWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb2xCRVJUIChDb250ZXh0dWFsaXplZCBMYXRlIEludGVyYWN0aW9uIG92ZXIgQkVSVCkgaXMgYSBoeWJyaWQgYmV0d2VlbiBiaS1lbmNvZGVycyBhbmQgY3Jvc3MtZW5jb2RlcnMuIEl0IGVuY29kZXMgcXVlcnkgYW5kIGRvY3VtZW50IHNlcGFyYXRlbHkgaW50byBwZXItdG9rZW4gZW1iZWRkaW5ncyByYXRoZXIgdGhhbiBwb29sZWQgdmVjdG9ycywgdGhlbiBjb21wdXRlcyBhIE1heFNpbSBpbnRlcmFjdGlvbiBzY29yZTogZm9yIGVhY2ggcXVlcnkgdG9rZW4sIGZpbmQgdGhlIG1heGltdW0gY29zaW5lIHNpbWlsYXJpdHkgdG8gYW55IGRvY3VtZW50IHRva2VuLCB0aGVuIHN1bSB0aGVzZSBwZXItdG9rZW4gbWF4aW11bXMuIFRoaXMgbGF0ZSBpbnRlcmFjdGlvbiBhbGxvd3MgZG9jdW1lbnQgdG9rZW4gZW1iZWRkaW5ncyB0byBiZSBwcmUtY29tcHV0ZWQgYW5kIHN0b3JlZCBvZmZsaW5lIChsaWtlIGEgYmktZW5jb2RlciksIHdoaWxlIHRoZSBNYXhTaW0gb3BlcmF0aW9uIGNhcHR1cmVzIGZpbmUtZ3JhaW5lZCB0b2tlbi1sZXZlbCByZWxldmFuY2Ugc2lnbmFscyAoYXBwcm9hY2hpbmcgY3Jvc3MtZW5jb2RlciBhY2N1cmFjeSkuIENvbEJFUlQgdjIgYWNoaWV2ZXMgbmVhci1jcm9zcy1lbmNvZGVyIGFjY3VyYWN5IG9uIE1TLU1BUkNPIHdoaWxlIHN1cHBvcnRpbmcgb2ZmbGluZSBpbmRleGluZyB0aHJvdWdoIGl0cyBjb21wcmVzc2VkIHRva2VuIGVtYmVkZGluZyBpbmRleC4gSXQgaXMgdGhlIHJlY29tbWVuZGVkIGNob2ljZSB3aGVuIGJvdGggcmV0cmlldmFsIGxhdGVuY3kgYW5kIHJhbmtpbmcgYWNjdXJhY3kgYXJlIGNyaXRpY2FsLCBhbmQgd2hlbiBpbmZyYXN0cnVjdHVyZSBjYW4gc3VwcG9ydCB0aGUgbGFyZ2VyIHBlci1kb2N1bWVudCBpbmRleCAoQ29sQkVSVCBzdG9yZXMgfjEwMCB2ZWN0b3JzIHBlciBkb2N1bWVudCByYXRoZXIgdGhhbiAxKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXJhbmtlciBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT2ZmLXRoZS1zaGVsZiBjcm9zcy1lbmNvZGVycyB0cmFpbmVkIG9uIE1TLU1BUkNPIGdlbmVyYWxpc2Ugd2VsbCB0byBtYW55IEVuZ2xpc2gtbGFuZ3VhZ2UgZG9tYWlucyBidXQgZGVncmFkZSBvbiBzcGVjaWFsaXNlZCBjb3Jwb3JhIChsZWdhbCwgYmlvbWVkaWNhbCwgZmluYW5jaWFsLCBjb2RlKS4gRmluZS10dW5pbmcgYSBjcm9zcy1lbmNvZGVyIG9uIGRvbWFpbi1zcGVjaWZpYyBkYXRhIHR5cGljYWxseSBpbXByb3ZlcyBNUlJAMTAgYnkgNeKAkzE1IHBlcmNlbnRhZ2UgcG9pbnRzLiBUaGUgdHJhaW5pbmcgZGF0YSBmb3JtYXQgaXMgdHJpcGxldHM6IChxdWVyeSwgcG9zaXRpdmUgcGFzc2FnZSwgbmVnYXRpdmUgcGFzc2FnZSkuIEhhcmQgbmVnYXRpdmVzIOKAlCBwYXNzYWdlcyB0aGF0IGFyZSByZXRyaWV2ZWQgYnkgYSBiaS1lbmNvZGVyIGJ1dCBhcmUgbm90IGFjdHVhbGx5IHJlbGV2YW50IOKAlCBhcmUgZmFyIG1vcmUgdmFsdWFibGUgdGhhbiByYW5kb20gbmVnYXRpdmVzIGZvciB0cmFpbmluZyBzdHJvbmcgcmVyYW5rZXJzLiBIYXJkIG5lZ2F0aXZlcyBjYW4gYmUgbWluZWQgdXNpbmcgYSB0cmFpbmVkIGJpLWVuY29kZXI6IHJldHJpZXZlIHRvcC0xMDAgZm9yIGVhY2ggdHJhaW5pbmcgcXVlcnksIGxhYmVsIHRoZSBpcnJlbGV2YW50IG9uZXMgYXMgaGFyZCBuZWdhdGl2ZXMsIGFuZCBpbmNsdWRlIHRoZW0gaW4gdGhlIHRyaXBsZXQgZGF0YXNldC4gVHJhaW5pbmcgdXNlcyBjcm9zcy1lbnRyb3B5IG9yIG1hcmdpbiByYW5raW5nIGxvc3MuIFN0YXJ0aW5nIGZyb20gYSBwcmUtdHJhaW5lZCBNUy1NQVJDTyBtb2RlbCBhbmQgZmluZS10dW5pbmcgZm9yIDHigJMzIGVwb2NocyBvbiAxMEvigJMxMDBLIGRvbWFpbiB0cmlwbGV0cyBpcyBhIHByYWN0aWNhbCByZWNpcGUgZm9yIG1vc3QgcHJvZHVjdGlvbiBkZXBsb3ltZW50cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGNvaGVyZVxuaW1wb3J0IHRpbWVcblxuZGVmIGNvaGVyZV9yZXJhbmsocXVlcnk6IHN0ciwgZG9jdW1lbnRzOiBsaXN0LCBhcGlfa2V5OiBzdHIsXG4gICAgICAgICAgICAgICAgICAgbW9kZWw6IHN0ciA9IFwicmVyYW5rLWVuZ2xpc2gtdjMuMFwiLCB0b3BfbjogaW50ID0gNSkgLVx1MDAzZSBsaXN0OlxuICAgIFwiXCJcIlJlcmFuayBkb2N1bWVudHMgd2l0aCBDb2hlcmUgcmVyYW5rIEFQSTsgbWVhc3VyZSBsYXRlbmN5IGFuZCByYW5rIGNoYW5nZXMuXCJcIlwiXG4gICAgY28gPSBjb2hlcmUuQ2xpZW50KGFwaV9rZXkpXG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgcmVzcG9uc2UgPSBjby5yZXJhbmsoXG4gICAgICAgIHF1ZXJ5PXF1ZXJ5LFxuICAgICAgICBkb2N1bWVudHM9ZG9jdW1lbnRzLFxuICAgICAgICBtb2RlbD1tb2RlbCxcbiAgICAgICAgdG9wX249dG9wX24sXG4gICAgICAgIHJldHVybl9kb2N1bWVudHM9VHJ1ZSxcbiAgICApXG4gICAgbGF0ZW5jeV9tcyA9ICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApICogMTAwMFxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciByIGluIHJlc3BvbnNlLnJlc3VsdHM6XG4gICAgICAgIG9yaWdfcmFuayA9IHIuaW5kZXggKyAxXG4gICAgICAgIG5ld19yYW5rICA9IGxlbihyZXN1bHRzKSArIDFcbiAgICAgICAgZGVsdGEgICAgID0gb3JpZ19yYW5rIC0gbmV3X3JhbmtcbiAgICAgICAgYXJyb3cgICAgID0gZlwiKCt7ZGVsdGF9KVwiIGlmIGRlbHRhIFx1MDAzZSAwIGVsc2UgZlwiKHtkZWx0YX0pXCIgaWYgZGVsdGEgXHUwMDNjIDAgZWxzZSBcIig9KVwiXG4gICAgICAgIHNuaXBwZXQgICA9IChyLmRvY3VtZW50LnRleHQgaWYgci5kb2N1bWVudCBlbHNlIGRvY3VtZW50c1tyLmluZGV4XSlbOjYwXVxuICAgICAgICByZXN1bHRzLmFwcGVuZCh7XCJvcmlnX3JhbmtcIjogb3JpZ19yYW5rLCBcIm5ld19yYW5rXCI6IG5ld19yYW5rLFxuICAgICAgICAgICAgICAgICAgICAgICAgIFwic2NvcmVcIjogci5yZWxldmFuY2Vfc2NvcmUsIFwic25pcHBldFwiOiBzbmlwcGV0fSlcbiAgICAgICAgcHJpbnQoZlwiT3JpZyB7b3JpZ19yYW5rOlx1MDAzZTJ9IC1cdTAwM2UgTmV3IHtuZXdfcmFuazpcdTAwM2UyfSB7YXJyb3c6XHUwMDNlNX0gIHNjb3JlPXtyLnJlbGV2YW5jZV9zY29yZTouNGZ9ICB7c25pcHBldH1cIilcbiAgICBwcmludChmXCJcXG5MYXRlbmN5OiB7bGF0ZW5jeV9tczouMGZ9bXMgIG1vZGVsPXttb2RlbH0gIGRvY3M9e2xlbihkb2N1bWVudHMpfVwiKVxuICAgIHJldHVybiByZXN1bHRzXG5cbmRvY3MgID0gW2ZcIlBhc3NhZ2Uge2l9OiBjb250ZW50IGFib3V0IG5hdHVyYWwgbGFuZ3VhZ2UgcHJvY2Vzc2luZyB0b3BpYyB7aX0uXCIgZm9yIGkgaW4gcmFuZ2UoMTApXVxucmVzdWx0ID0gY29oZXJlX3JlcmFuayhcImhvdyBkb2VzIE5MUCBwcm9jZXNzIGxhbmd1YWdlIHNlbWFudGljc1wiLCBkb2NzLCBcIllPVVJfQVBJX0tFWVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbW1lcmNpYWwgUmVyYW5rZXIgQVBJcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2V2ZXJhbCBwcm92aWRlcnMgb2ZmZXIgaG9zdGVkIHJlcmFua2luZyBBUElzIHRoYXQgcmVxdWlyZSBubyBtb2RlbCBkZXBsb3ltZW50LiBDb2hlcmVcdTAwMjdzIHJlcmFuay1lbmdsaXNoLXYzLjAgYW5kIHJlcmFuay1tdWx0aWxpbmd1YWwtdjMuMCBhcmUgdGhlIG1vc3Qgd2lkZWx5IHVzZWQsIHN1cHBvcnRpbmcgdXAgdG8gMTAsMDAwIGRvY3VtZW50cyBwZXIgY2FsbCB3aXRoIGxhdGVuY3kgb2YgMTAw4oCTNTAwbXMgZm9yIDUwIGNhbmRpZGF0ZXMuIFZveWFnZSBBSVx1MDAyN3MgcmVyYW5rLTEgYW5kIHJlcmFuay0yIG1vZGVscyBvZmZlciBjb21wZXRpdGl2ZSBhY2N1cmFjeSBvbiB0ZWNobmljYWwgYW5kIGNvZGUtaGVhdnkgY29ycG9yYS4gSmluYSBBSVx1MDAyN3MgamluYS1yZXJhbmtlci12MiBpcyBhdmFpbGFibGUgYm90aCBhcyBhbiBBUEkgYW5kIGFzIGFuIG9wZW4td2VpZ2h0IG1vZGVsLiBDb21tZXJjaWFsIEFQSXMgYXJlIHRoZSBmYXN0ZXN0IHBhdGggdG8gcHJvZHVjdGlvbiByZXJhbmtpbmc6IG5vIEdQVSBpbmZyYXN0cnVjdHVyZSwgcGF5LXBlci1yZXF1ZXN0IHByaWNpbmcgKH4kMC4wMDIgcGVyIDEwMDAgdG9rZW5zKSwgYW5kIG1hbmFnZWQgbW9kZWwgdXBkYXRlcy4gVGhlIHRyYWRlb2ZmIGlzIGRhdGEgcHJpdmFjeSAoYWxsIHF1ZXJpZXMgYW5kIGRvY3VtZW50cyBsZWF2ZSB5b3VyIGluZnJhc3RydWN0dXJlKSBhbmQgcGVyLXF1ZXJ5IGNvc3QgYXQgaGlnaCB2b2x1bWUuIEZvciBoaWdoLXZvbHVtZSBwcm9kdWN0aW9uIHdvcmtsb2FkcyAoXHUwMDNlMU0gZGFpbHkgcXVlcmllcyksIHNlbGYtaG9zdGVkIG9wZW4td2VpZ2h0IHJlcmFua2VycyBzdWNoIGFzIEJBQUkvYmdlLXJlcmFua2VyLXYyLW0zIG9mZmVyIGJldHRlciBlY29ub21pY3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0aW1lXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2VudGVuY2VfdHJhbnNmb3JtZXJzIGltcG9ydCBTZW50ZW5jZVRyYW5zZm9ybWVyLCBDcm9zc0VuY29kZXJcbmltcG9ydCBmYWlzc1xuXG5kZWYgZnVsbF9yYWdfcmVyYW5rX3BpcGVsaW5lKHF1ZXJ5OiBzdHIsIGRvY3M6IGxpc3QsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICByZXRyaWV2ZV90b3A6IGludCA9IDUwLCBmaW5hbF90b3A6IGludCA9IDUpIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJSZXRyaWV2ZSB0b3AtNTAgd2l0aCBkZW5zZSBiaS1lbmNvZGVyLCByZXJhbmsgd2l0aCBjcm9zcy1lbmNvZGVyLCByZXR1cm4gdG9wLTUuXCJcIlwiXG4gICAgYmlfbW9kZWwgPSBTZW50ZW5jZVRyYW5zZm9ybWVyKFwiYWxsLU1pbmlMTS1MNi12MlwiKVxuICAgIGNlX21vZGVsID0gQ3Jvc3NFbmNvZGVyKFwiY3Jvc3MtZW5jb2Rlci9tcy1tYXJjby1NaW5pTE0tTC02LXYyXCIsIG1heF9sZW5ndGg9NTEyKVxuICAgICMgU3RhZ2UgMTogZGVuc2UgcmV0cmlldmFsXG4gICAgZF9lbWJzID0gYmlfbW9kZWwuZW5jb2RlKGRvY3MsIG5vcm1hbGl6ZV9lbWJlZGRpbmdzPVRydWUpLmFzdHlwZShucC5mbG9hdDMyKVxuICAgIGluZGV4ICA9IGZhaXNzLkluZGV4RmxhdElQKGRfZW1icy5zaGFwZVsxXSlcbiAgICBpbmRleC5hZGQoZF9lbWJzKVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHFfZW1iID0gYmlfbW9kZWwuZW5jb2RlKFtxdWVyeV0sIG5vcm1hbGl6ZV9lbWJlZGRpbmdzPVRydWUpLmFzdHlwZShucC5mbG9hdDMyKVxuICAgIF8sIGhpdHMgPSBpbmRleC5zZWFyY2gocV9lbWIsIG1pbihyZXRyaWV2ZV90b3AsIGxlbihkb2NzKSkpXG4gICAgcmV0cmlldmFsX21zID0gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MCkgKiAxMDAwXG4gICAgIyBTdGFnZSAyOiBjcm9zcy1lbmNvZGVyIHJlcmFua2luZ1xuICAgIGNhbmRpZGF0ZXMgPSBbKGksIGRvY3NbaV0pIGZvciBpIGluIGhpdHNbMF0gaWYgaSBcdTAwM2MgbGVuKGRvY3MpXVxuICAgIHQxID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHNjb3JlcyA9IGNlX21vZGVsLnByZWRpY3QoWyhxdWVyeSwgZG9jKSBmb3IgXywgZG9jIGluIGNhbmRpZGF0ZXNdKVxuICAgIHJhbmtlZCA9IHNvcnRlZCh6aXAoY2FuZGlkYXRlcywgc2NvcmVzKSwga2V5PWxhbWJkYSB4OiB4WzFdLCByZXZlcnNlPVRydWUpXG4gICAgcmVyYW5rX21zID0gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MSkgKiAxMDAwXG4gICAgdG9wNSA9IFtkb2NzW2lkeF0gZm9yIChpZHgsIF8pLCBfIGluIHJhbmtlZFs6ZmluYWxfdG9wXV1cbiAgICBwcmludChmXCJTdGFnZSAxIChiaS1lbmNvZGVyKToge2xlbihjYW5kaWRhdGVzKX0gY2FuZGlkYXRlcyBpbiB7cmV0cmlldmFsX21zOi4wZn1tc1wiKVxuICAgIHByaW50KGZcIlN0YWdlIDIgKGNyb3NzLWVuYykgOiB0b3Ate2ZpbmFsX3RvcH0gZnJvbSB7bGVuKGNhbmRpZGF0ZXMpfSBpbiB7cmVyYW5rX21zOi4wZn1tc1wiKVxuICAgIHJldHVybiB7XCJ0b3BfZG9jc1wiOiB0b3A1LCBcInJldHJpZXZhbF9tc1wiOiByZXRyaWV2YWxfbXMsIFwicmVyYW5rX21zXCI6IHJlcmFua19tc31cblxuZG9jcyAgID0gW2ZcIkFydGljbGUge2l9OiBpbmZvcm1hdGlvbiBhYm91dCBkZWVwIGxlYXJuaW5nIGNvbmNlcHQge2kgJSAxMn0uXCIgZm9yIGkgaW4gcmFuZ2UoMTAwKV1cbnJlc3VsdCA9IGZ1bGxfcmFnX3JlcmFua19waXBlbGluZShcImV4cGxhaW4gaG93IG5ldXJhbCBuZXR3b3JrcyBsZWFybiByZXByZXNlbnRhdGlvbnNcIiwgZG9jcylcbmZvciBpLCBkIGluIGVudW1lcmF0ZShyZXN1bHRbXCJ0b3BfZG9jc1wiXSk6XG4gICAgcHJpbnQoZlwiICBGaW5hbCByYW5rIHtpKzF9OiB7ZH1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXRlbmN5IHZzIFF1YWxpdHkgVHJhZGVvZmYifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlcmFua2luZyBhZGRzIGxhdGVuY3kgcHJvcG9ydGlvbmFsIHRvIHRoZSBudW1iZXIgb2YgY2FuZGlkYXRlcyBzY29yZWQgYW5kIHRoZSBzaXplIG9mIHRoZSBjcm9zcy1lbmNvZGVyLiBNaW5pTE0tTC02LXYyIHNjb3JpbmcgNTAgY2FuZGlkYXRlcyB0YWtlcyA0MOKAkzgwbXMgb24gQ1BVLCB3aGljaCBpcyBhY2NlcHRhYmxlIGZvciBpbnRlcmFjdGl2ZSBhcHBsaWNhdGlvbnMuIFNjb3JpbmcgMjAwIGNhbmRpZGF0ZXMgd2l0aCB0aGUgc2FtZSBtb2RlbCB0YWtlcyAxNTDigJMzMDBtcy4gT24gR1BVLCB0aGVzZSB0aW1lcyBkcm9wIHRvIDXigJMyMG1zIGZvciA1MCBjYW5kaWRhdGVzLiBUaGUgcXVhbGl0eSB2cyBsYXRlbmN5IFBhcmV0byBmcm9udGllcjogc2NvcmUgMjDigJMzMCBjYW5kaWRhdGVzIHdpdGggTWluaUxNLUwtNiBmb3IgdGhlIGJlc3QgbGF0ZW5jeS1xdWFsaXR5IHRyYWRlb2ZmIGluIENQVS1vbmx5IGRlcGxveW1lbnRzOyBzY29yZSA1MOKAkzEwMCBjYW5kaWRhdGVzIHdpdGggYSBsYXJnZXIgbW9kZWwgKGJlcnQtYmFzZS11bmNhc2VkIGZpbmUtdHVuZWQgb24gTVMtTUFSQ08pIGZvciBtYXhpbXVtIGFjY3VyYWN5IHdoZW4gR1BVIGlzIGF2YWlsYWJsZS4gUmV0cmlldmluZyBtb3JlIGluaXRpYWwgY2FuZGlkYXRlcyBnZW5lcmFsbHkgaGVscHMgcmVyYW5raW5nIHVwIHRvIH4xMDA7IGJleW9uZCB0aGF0LCB0aGUgbWFyZ2luYWwgYmVuZWZpdCBkaW1pbmlzaGVzIGJlY2F1c2UgdGhlIGFkZGl0aW9uYWwgY2FuZGlkYXRlcyBhcmUgaW5jcmVhc2luZ2x5IGlycmVsZXZhbnQgYW5kIGEgZml4ZWQtY2FwYWNpdHkgcmVyYW5rZXIgY2FuIG9ubHkgZG8gc28gbXVjaC4gQWx3YXlzIGJlbmNobWFyayBlbmQtdG8tZW5kIHBpcGVsaW5lIGxhdGVuY3kgKHJldHJpZXZhbCArIHJlcmFua2luZykgdW5kZXIgcmVhbGlzdGljIGxvYWQgcmF0aGVyIHRoYW4gbWVhc3VyaW5nIGVhY2ggc3RhZ2UgaW4gaXNvbGF0aW9uLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJNUlJAMTAgaW1wcm92ZW1lbnQiLCJMYXRlbmN5ICg1MCBkb2NzLCBDUFUpIiwiQ29zdCIsIk5vdGVzIl0sInJvd3MiOltbIk5vIHJlcmFua2VyIiwiYmFzZWxpbmUgKDAlKSIsIjBtcyIsIkZyZWUiLCJCaS1lbmNvZGVyIG9yZGVyOyBmYXN0IGJ1dCBpbXByZWNpc2UiXSxbIk1pbmlMTSBjcm9zcy1lbmNvZGVyIiwiKzE44oCTMjIlIiwiNDDigJM4MG1zIiwiRnJlZSAoc2VsZi1ob3N0ZWQpIiwiQmVzdCBsYXRlbmN5LXF1YWxpdHkgZm9yIENQVTsgMjJNIHBhcmFtcyJdLFsiQkVSVC1iYXNlIGNyb3NzLWVuY29kZXIiLCIrMjLigJMyOCUiLCIxNTDigJMyNTBtcyIsIkZyZWUgKHNlbGYtaG9zdGVkKSIsIkhpZ2hlciBhY2N1cmFjeTsgbmVlZHMgR1BVIGZvciBsb3cgbGF0ZW5jeSJdLFsiQ29sQkVSVCBsYXRlIGludGVyYWN0aW9uIiwiKzIw4oCTMjUlIiwiMTDigJMzMG1zIChHUFUpIiwiRnJlZSAoc2VsZi1ob3N0ZWQpIiwiUHJlLWluZGV4YWJsZSB0b2tlbiBlbWJzOyBuZWVkcyBDb2xCRVJUIGluZnJhIl0sWyJDb2hlcmUgcmVyYW5rLXYzIiwiKzIy4oCTMjglIiwiMTAw4oCTMzAwbXMgKEFQSSkiLCJ+JDAuMDAyLzFLIHRva2VucyIsIk1hbmFnZWQ7IG5vIEdQVSBuZWVkZWQ7IGRhdGEgbGVhdmVzIGluZnJhIl0sWyJWb3lhZ2UgcmVyYW5rLTIiLCIrMjPigJMyOSUiLCIxMDDigJM0MDBtcyAoQVBJKSIsIn4kMC4wMDIvMUsgdG9rZW5zIiwiU3Ryb25nIG9uIHRlY2huaWNhbC9jb2RlIGNvcnBvcmEiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSGlnaGVzdCBST0kgU2luZ2xlIEltcHJvdmVtZW50IiwiY29udGVudCI6IlJlcmFua2luZyA1MCBjYW5kaWRhdGVzIHRvIDUgdHlwaWNhbGx5IGltcHJvdmVzIGFuc3dlciBhY2N1cmFjeSBieSAxNeKAkzI1JSBvbiBkb21haW4tc3BlY2lmaWMgUkFHIOKAlCBpdFx1MDAyN3MgdGhlIGhpZ2hlc3QgUk9JIHNpbmdsZSBpbXByb3ZlbWVudCB5b3UgY2FuIG1ha2UgdG8gYSBiYXNpYyBSQUcgcGlwZWxpbmUuIEJlZm9yZSBpbnZlc3RpbmcgaW4gYmV0dGVyIGVtYmVkZGluZ3MsIGh5YnJpZCBCTTI1K2RlbnNlIHJldHJpZXZhbCwgb3IgcXVlcnkgcmV3cml0aW5nLCBhZGQgYSBNaW5pTE0gY3Jvc3MtZW5jb2RlciByZXJhbmtlci4gVGhlIGxhdGVuY3kgY29zdCAoNDDigJM4MG1zIG9uIENQVSkgaXMgYWxtb3N0IGFsd2F5cyB3b3J0aCB0aGUgYWNjdXJhY3kgZ2Fpbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXJhbmtpbmcgaXMgdGhlIG1vc3QgcmVsaWFibGUsIGhpZ2hlc3QtUk9JIHVwZ3JhZGUgdG8gYW55IGJhc2ljIFJBRyBwaXBlbGluZS4gVGhlIHR3by1zdGFnZSBhcmNoaXRlY3R1cmUg4oCUIGZhc3QgYmktZW5jb2RlciByZXRyaWV2YWwgb2YgMjDigJMxMDAgY2FuZGlkYXRlcywgZm9sbG93ZWQgYnkgcHJlY2lzZSBjcm9zcy1lbmNvZGVyIHJlcmFua2luZyB0byAz4oCTMTAgcmVzdWx0cyDigJQgY29tYmluZXMgdGhlIHNjYWxhYmlsaXR5IG9mIGRlbnNlIHJldHJpZXZhbCB3aXRoIHRoZSBhY2N1cmFjeSBvZiBmdWxsLXNlcXVlbmNlIHNjb3JpbmcuIE1pbmlMTS1MLTYtdjIgaXMgdGhlIHByYWN0aWNhbCBkZWZhdWx0OiAyMk0gcGFyYW1ldGVycywgZnJlZSwgc2VsZi1ob3N0ZWQsIGFuZCBzY29yZXMgNTAgY2FuZGlkYXRlcyBpbiB1bmRlciA4MG1zIG9uIENQVS4gRm9yIG1heGltdW0gYWNjdXJhY3ksIGZpbmUtdHVuZSBhIGNyb3NzLWVuY29kZXIgb24gZG9tYWluLXNwZWNpZmljIGhhcmQgbmVnYXRpdmVzLiBGb3IgemVyby1pbmZyYXN0cnVjdHVyZSBkZXBsb3ltZW50cywgQ29oZXJlIG9yIFZveWFnZSByZXJhbmtlciBBUElzIGFyZSBleGNlbGxlbnQgZHJvcC1pbiBvcHRpb25zLiBDb2xCRVJUIGlzIHRoZSBiZXN0IGNob2ljZSB3aGVuIGJvdGggcHJlLWluZGV4aW5nIGFuZCBoaWdoIGFjY3VyYWN5IGFyZSByZXF1aXJlZC4gQWx3YXlzIHJldHJpZXZlIGF0IGxlYXN0IDIw4oCTNTAgY2FuZGlkYXRlcyBiZWZvcmUgcmVyYW5raW5nOyByZXJhbmtpbmcgNSBjYW5kaWRhdGVzIGhhcyBtaW5pbWFsIGJlbmVmaXQgb3ZlciB0aGUgb3JpZ2luYWwgcmV0cmlldmFsIG9yZGVyLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVHdvLXN0YWdlIHBpcGVsaW5lOiBiaS1lbmNvZGVyIHJldHJpZXZlcyB0b3AtNTAsIGNyb3NzLWVuY29kZXIgcmVyYW5rcyB0byB0b3AtNSIsIkNyb3NzLWVuY29kZXJzIGpvaW50bHkgYXR0ZW5kIG92ZXIgcXVlcnkrZG9jdW1lbnQ7IGZhciBtb3JlIGFjY3VyYXRlIHRoYW4gYmktZW5jb2RlciBzaW1pbGFyaXR5IiwiTWluaUxNLUwtNi12MiBpcyB0aGUgZGVmYXVsdDogZnJlZSwgMjJNIHBhcmFtcywgNDDigJM4MG1zIGZvciA1MCBjYW5kaWRhdGVzIG9uIENQVSIsIkZpbmUtdHVuZSBvbiBoYXJkIG5lZ2F0aXZlcyAoYmktZW5jb2RlciB0b3AtMTAwIG1pbnVzIGdyb3VuZCB0cnV0aCkgZm9yIGRvbWFpbiBhZGFwdGF0aW9uIiwiQ29oZXJlIHJlcmFuay12MyAvIFZveWFnZSByZXJhbmstMiBmb3IgemVyby1pbmZyYSBkZXBsb3ltZW50czsgfiQwLjAwMiBwZXIgMUsgdG9rZW5zIiwiQ29sQkVSVCBsYXRlIGludGVyYWN0aW9uOiBvZmZsaW5lLWluZGV4YWJsZSB0b2tlbiBlbWJlZGRpbmdzIHdpdGggbmVhciBjcm9zcy1lbmNvZGVyIGFjY3VyYWN5IiwiQWx3YXlzIHJldHJpZXZlIOKJpTIwIGNhbmRpZGF0ZXMgYmVmb3JlIHJlcmFua2luZzsgYmVuZWZpdCBwbGF0ZWF1cyBiZXlvbmQgfjEwMCBjYW5kaWRhdGVzIl19XQ=="
---
# Reranking for RAG

Reranking is a second-stage relevance scoring step applied after an initial retrieval phase. The initial retrieval — typically a bi-encoder dense search or BM25 — returns a broad candidate set of 20–100 documents quickly but imprecisely, because bi-encoders compress query and document into fixed vectors independently before comparing them. A reranker then jointly encodes each query-document pair through a cross-encoder, producing a much more accurate relevance score. The top-k reranked documents (typically 3–10) are passed to the LLM. Reranking typically improves answer accuracy by 15–30% on domain-specific RAG benchmarks, making it the single highest-ROI improvement available to a basic retrieval pipeline.

## Overview

A standard RAG pipeline without reranking suffers from a precision problem: the vector similarity between a query embedding and a document embedding is a coarse relevance proxy, because both are compressed into a fixed-size vector independently before comparison. The dot product measures geometric proximity in embedding space, not semantic entailment. A document that shares vocabulary with the query but does not actually answer it can rank higher than a document that answers the query using different words. Reranking addresses this by applying a cross-encoder that attends over the full query-document pair jointly, using its full BERT-style attention to detect whether the document actually contains the answer to the query. The cost is quadratic in the number of candidates (each query-document pair is scored independently), but since the candidate set is small (20–100 docs), the latency is acceptable.

## Bi-Encoder vs Cross-Encoder

Bi-encoders (used in dense retrieval) encode query and document separately: encode(query) → q_vector, encode(doc) → d_vector, score = dot(q_vector, d_vector). This allows documents to be pre-encoded offline and indexed in FAISS, enabling sub-millisecond retrieval over millions of documents at query time. The price is the information bottleneck: the fixed-size vector cannot capture fine-grained interactions between query tokens and document tokens. Cross-encoders process the concatenated query and document as a single input sequence: encode([CLS] query [SEP] document [SEP]) → scalar score. The full self-attention over the combined sequence allows every query token to directly attend to every document token, producing a much more accurate relevance score. Cross-encoders cannot be pre-indexed and scale linearly with the number of candidates scored, so they are used only on the small candidate set returned by the bi-encoder.

```python
from sentence_transformers import CrossEncoder, SentenceTransformer
import numpy as np
import faiss

def retrieve_candidates(query: str, docs: list, bi_model_name: str, top_n: int = 20) -> list:
    """Fast bi-encoder retrieval: return indices of top_n candidate documents."""
    model  = SentenceTransformer(bi_model_name)
    d_embs = model.encode(docs, normalize_embeddings=True).astype(np.float32)
    q_emb  = model.encode([query], normalize_embeddings=True).astype(np.float32)
    index  = faiss.IndexFlatIP(d_embs.shape[1])
    index.add(d_embs)
    _, idxs = index.search(q_emb, min(top_n, len(docs)))
    return idxs[0].tolist()

def cross_encoder_rerank(query: str, docs: list, candidate_idxs: list,
                          ce_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2") -> list:
    """Score each query-candidate pair with a cross-encoder; return sorted results."""
    reranker  = CrossEncoder(ce_model, max_length=512)
    pairs     = [(query, docs[i]) for i in candidate_idxs]
    scores    = reranker.predict(pairs)
    ranked    = sorted(zip(candidate_idxs, scores), key=lambda x: x[1], reverse=True)
    return [{"doc_idx": idx, "ce_score": float(sc), "text": docs[idx][:80]}
            for idx, sc in ranked]

docs  = [f"Document {i}: topic about NLP technique {i % 8}." for i in range(30)]
query = "how does retrieval augmented generation improve LLM accuracy"
cands = retrieve_candidates(query, docs, "all-MiniLM-L6-v2", top_n=20)
print(f"Bi-encoder top-3 (orig order): {cands[:3]}")
results = cross_encoder_rerank(query, docs, cands)
print(f"Cross-encoder top-3: {[r['doc_idx'] for r in results[:3]]}")
```

## Cross-Encoder Architecture

A cross-encoder for reranking is a standard BERT-style transformer with a linear head on the [CLS] token that outputs a single scalar relevance score. The model is fine-tuned on MS-MARCO or similar passage-ranking datasets using a pointwise or listwise loss: given a query, a relevant passage, and several irrelevant passages, the model learns to assign a higher score to the relevant passage. The most commonly used cross-encoders are the ms-marco-MiniLM family from the sentence-transformers library. MiniLM-L-6-v2 has 6 layers and ~22M parameters, scoring 100 passages in about 50ms on CPU — a practical latency for retrieval pipelines. The full BERT-large cross-encoder (ms-marco-bert-base) is more accurate but takes ~200ms for 100 passages. For latency-sensitive pipelines, MiniLM-L-6 at top-50 candidates is the recommended default.

```python
import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F

def colbert_encode(texts: list, model, tokenizer, device: str = "cpu") -> tuple:
    """Encode texts to per-token embeddings (batch, seq_len, dim) for ColBERT scoring."""
    enc = tokenizer(texts, padding=True, truncation=True,
                    max_length=128, return_tensors="pt").to(device)
    with torch.no_grad():
        out = model(**enc)
    # Normalise each token embedding to the unit sphere
    token_embs = F.normalize(out.last_hidden_state, p=2, dim=-1)
    return token_embs, enc["attention_mask"]

def colbert_maxsim(q_embs: torch.Tensor, d_embs: torch.Tensor,
                    q_mask: torch.Tensor, d_mask: torch.Tensor) -> float:
    """MaxSim score: sum over query tokens of max cosine similarity to any doc token."""
    sims = torch.matmul(q_embs[0], d_embs[0].T)   # (q_len, d_len)
    sims[:, d_mask[0] == 0] = -1e9                 # mask padding in doc
    max_sims = sims.max(dim=-1).values             # (q_len,)
    max_sims[q_mask[0] == 0] = 0.0                # mask padding in query
    return max_sims.sum().item()

model_name = "bert-base-uncased"
tok   = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
query    = "what is retrieval augmented generation"
passages = ["RAG combines retrieval with generation to ground LLM answers in real documents.",
            "Convolutional networks process images through local filter operations."]
q_embs, q_mask = colbert_encode([query], model, tok)
for p in passages:
    d_embs, d_mask = colbert_encode([p], model, tok)
    score = colbert_maxsim(q_embs, d_embs, q_mask, d_mask)
    print(f"ColBERT score {score:.3f}: {p[:60]}")
```

## ColBERT Late Interaction

ColBERT (Contextualized Late Interaction over BERT) is a hybrid between bi-encoders and cross-encoders. It encodes query and document separately into per-token embeddings rather than pooled vectors, then computes a MaxSim interaction score: for each query token, find the maximum cosine similarity to any document token, then sum these per-token maximums. This late interaction allows document token embeddings to be pre-computed and stored offline (like a bi-encoder), while the MaxSim operation captures fine-grained token-level relevance signals (approaching cross-encoder accuracy). ColBERT v2 achieves near-cross-encoder accuracy on MS-MARCO while supporting offline indexing through its compressed token embedding index. It is the recommended choice when both retrieval latency and ranking accuracy are critical, and when infrastructure can support the larger per-document index (ColBERT stores ~100 vectors per document rather than 1).

## Reranker Training

Off-the-shelf cross-encoders trained on MS-MARCO generalise well to many English-language domains but degrade on specialised corpora (legal, biomedical, financial, code). Fine-tuning a cross-encoder on domain-specific data typically improves MRR@10 by 5–15 percentage points. The training data format is triplets: (query, positive passage, negative passage). Hard negatives — passages that are retrieved by a bi-encoder but are not actually relevant — are far more valuable than random negatives for training strong rerankers. Hard negatives can be mined using a trained bi-encoder: retrieve top-100 for each training query, label the irrelevant ones as hard negatives, and include them in the triplet dataset. Training uses cross-entropy or margin ranking loss. Starting from a pre-trained MS-MARCO model and fine-tuning for 1–3 epochs on 10K–100K domain triplets is a practical recipe for most production deployments.

```python
import cohere
import time

def cohere_rerank(query: str, documents: list, api_key: str,
                   model: str = "rerank-english-v3.0", top_n: int = 5) -> list:
    """Rerank documents with Cohere rerank API; measure latency and rank changes."""
    co = cohere.Client(api_key)
    t0 = time.perf_counter()
    response = co.rerank(
        query=query,
        documents=documents,
        model=model,
        top_n=top_n,
        return_documents=True,
    )
    latency_ms = (time.perf_counter() - t0) * 1000
    results = []
    for r in response.results:
        orig_rank = r.index + 1
        new_rank  = len(results) + 1
        delta     = orig_rank - new_rank
        arrow     = f"(+{delta})" if delta > 0 else f"({delta})" if delta < 0 else "(=)"
        snippet   = (r.document.text if r.document else documents[r.index])[:60]
        results.append({"orig_rank": orig_rank, "new_rank": new_rank,
                         "score": r.relevance_score, "snippet": snippet})
        print(f"Orig {orig_rank:>2} -> New {new_rank:>2} {arrow:>5}  score={r.relevance_score:.4f}  {snippet}")
    print(f"\nLatency: {latency_ms:.0f}ms  model={model}  docs={len(documents)}")
    return results

docs  = [f"Passage {i}: content about natural language processing topic {i}." for i in range(10)]
result = cohere_rerank("how does NLP process language semantics", docs, "YOUR_API_KEY")
```

## Commercial Reranker APIs

Several providers offer hosted reranking APIs that require no model deployment. Cohere's rerank-english-v3.0 and rerank-multilingual-v3.0 are the most widely used, supporting up to 10,000 documents per call with latency of 100–500ms for 50 candidates. Voyage AI's rerank-1 and rerank-2 models offer competitive accuracy on technical and code-heavy corpora. Jina AI's jina-reranker-v2 is available both as an API and as an open-weight model. Commercial APIs are the fastest path to production reranking: no GPU infrastructure, pay-per-request pricing (~$0.002 per 1000 tokens), and managed model updates. The tradeoff is data privacy (all queries and documents leave your infrastructure) and per-query cost at high volume. For high-volume production workloads (>1M daily queries), self-hosted open-weight rerankers such as BAAI/bge-reranker-v2-m3 offer better economics.

```python
import time
import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder
import faiss

def full_rag_rerank_pipeline(query: str, docs: list,
                              retrieve_top: int = 50, final_top: int = 5) -> dict:
    """Retrieve top-50 with dense bi-encoder, rerank with cross-encoder, return top-5."""
    bi_model = SentenceTransformer("all-MiniLM-L6-v2")
    ce_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2", max_length=512)
    # Stage 1: dense retrieval
    d_embs = bi_model.encode(docs, normalize_embeddings=True).astype(np.float32)
    index  = faiss.IndexFlatIP(d_embs.shape[1])
    index.add(d_embs)
    t0 = time.perf_counter()
    q_emb = bi_model.encode([query], normalize_embeddings=True).astype(np.float32)
    _, hits = index.search(q_emb, min(retrieve_top, len(docs)))
    retrieval_ms = (time.perf_counter() - t0) * 1000
    # Stage 2: cross-encoder reranking
    candidates = [(i, docs[i]) for i in hits[0] if i < len(docs)]
    t1 = time.perf_counter()
    scores = ce_model.predict([(query, doc) for _, doc in candidates])
    ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)
    rerank_ms = (time.perf_counter() - t1) * 1000
    top5 = [docs[idx] for (idx, _), _ in ranked[:final_top]]
    print(f"Stage 1 (bi-encoder): {len(candidates)} candidates in {retrieval_ms:.0f}ms")
    print(f"Stage 2 (cross-enc) : top-{final_top} from {len(candidates)} in {rerank_ms:.0f}ms")
    return {"top_docs": top5, "retrieval_ms": retrieval_ms, "rerank_ms": rerank_ms}

docs   = [f"Article {i}: information about deep learning concept {i % 12}." for i in range(100)]
result = full_rag_rerank_pipeline("explain how neural networks learn representations", docs)
for i, d in enumerate(result["top_docs"]):
    print(f"  Final rank {i+1}: {d}")
```

## Latency vs Quality Tradeoff

Reranking adds latency proportional to the number of candidates scored and the size of the cross-encoder. MiniLM-L-6-v2 scoring 50 candidates takes 40–80ms on CPU, which is acceptable for interactive applications. Scoring 200 candidates with the same model takes 150–300ms. On GPU, these times drop to 5–20ms for 50 candidates. The quality vs latency Pareto frontier: score 20–30 candidates with MiniLM-L-6 for the best latency-quality tradeoff in CPU-only deployments; score 50–100 candidates with a larger model (bert-base-uncased fine-tuned on MS-MARCO) for maximum accuracy when GPU is available. Retrieving more initial candidates generally helps reranking up to ~100; beyond that, the marginal benefit diminishes because the additional candidates are increasingly irrelevant and a fixed-capacity reranker can only do so much. Always benchmark end-to-end pipeline latency (retrieval + reranking) under realistic load rather than measuring each stage in isolation.

| Method | MRR@10 improvement | Latency (50 docs, CPU) | Cost | Notes |
| --- | --- | --- | --- | --- |
| No reranker | baseline (0%) | 0ms | Free | Bi-encoder order; fast but imprecise |
| MiniLM cross-encoder | +18–22% | 40–80ms | Free (self-hosted) | Best latency-quality for CPU; 22M params |
| BERT-base cross-encoder | +22–28% | 150–250ms | Free (self-hosted) | Higher accuracy; needs GPU for low latency |
| ColBERT late interaction | +20–25% | 10–30ms (GPU) | Free (self-hosted) | Pre-indexable token embs; needs ColBERT infra |
| Cohere rerank-v3 | +22–28% | 100–300ms (API) | ~$0.002/1K tokens | Managed; no GPU needed; data leaves infra |
| Voyage rerank-2 | +23–29% | 100–400ms (API) | ~$0.002/1K tokens | Strong on technical/code corpora |

> **Highest ROI Single Improvement**: Reranking 50 candidates to 5 typically improves answer accuracy by 15–25% on domain-specific RAG — it's the highest ROI single improvement you can make to a basic RAG pipeline. Before investing in better embeddings, hybrid BM25+dense retrieval, or query rewriting, add a MiniLM cross-encoder reranker. The latency cost (40–80ms on CPU) is almost always worth the accuracy gain.

## Key Takeaways

Reranking is the most reliable, highest-ROI upgrade to any basic RAG pipeline. The two-stage architecture — fast bi-encoder retrieval of 20–100 candidates, followed by precise cross-encoder reranking to 3–10 results — combines the scalability of dense retrieval with the accuracy of full-sequence scoring. MiniLM-L-6-v2 is the practical default: 22M parameters, free, self-hosted, and scores 50 candidates in under 80ms on CPU. For maximum accuracy, fine-tune a cross-encoder on domain-specific hard negatives. For zero-infrastructure deployments, Cohere or Voyage reranker APIs are excellent drop-in options. ColBERT is the best choice when both pre-indexing and high accuracy are required. Always retrieve at least 20–50 candidates before reranking; reranking 5 candidates has minimal benefit over the original retrieval order.

- Two-stage pipeline: bi-encoder retrieves top-50, cross-encoder reranks to top-5
- Cross-encoders jointly attend over query+document; far more accurate than bi-encoder similarity
- MiniLM-L-6-v2 is the default: free, 22M params, 40–80ms for 50 candidates on CPU
- Fine-tune on hard negatives (bi-encoder top-100 minus ground truth) for domain adaptation
- Cohere rerank-v3 / Voyage rerank-2 for zero-infra deployments; ~$0.002 per 1K tokens
- ColBERT late interaction: offline-indexable token embeddings with near cross-encoder accuracy
- Always retrieve ≥20 candidates before reranking; benefit plateaus beyond ~100 candidates

