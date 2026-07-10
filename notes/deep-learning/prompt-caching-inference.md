---
title: "Prompt Caching in LLM Inference"
slug: "prompt-caching-inference"
description: "Reusing KV cache computations for shared prompt prefixes across requests to eliminate redundant prefill computation for system prompts, RAG context, or repeated preambles."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJvbXB0IGNhY2hpbmcgKGFsc28gY2FsbGVkIHByZWZpeCBjYWNoaW5nIG9yIEtWIGNhY2hlIHJldXNlKSBpcyBhIHNlcnZlci1zaWRlIGluZmVyZW5jZSBvcHRpbWl6YXRpb24gdGhhdCBzdG9yZXMgdGhlIGtleS12YWx1ZSAoS1YpIHRlbnNvcnMgY29tcHV0ZWQgZHVyaW5nIHRoZSBwcmVmaWxsIHBoYXNlIGZvciBhIHByb21wdCBwcmVmaXggYW5kIHJldXNlcyB0aGVtIGFjcm9zcyBzdWJzZXF1ZW50IHJlcXVlc3RzIHRoYXQgc2hhcmUgdGhlIHNhbWUgcHJlZml4LiBXaXRob3V0IGNhY2hpbmcsIGV2ZXJ5IHJlcXVlc3Qg4oCUIGV2ZW4gaWYgaXQgc2hhcmVzIGEgMjAwMC10b2tlbiBzeXN0ZW0gcHJvbXB0IHdpdGggdGhlIHByZXZpb3VzIG9uZSDigJQgcmVjb21wdXRlcyBhbGwgMjAwMCB0b2tlbnMgZnJvbSBzY3JhdGNoLiBXaXRoIGNhY2hpbmcsIHRoZSBzZXJ2ZXIgZGV0ZWN0cyB0aGUgc2hhcmVkIHByZWZpeCwgbG9hZHMgaXRzIHByZWNvbXB1dGVkIEtWIHRlbnNvcnMgZnJvbSBtZW1vcnksIGFuZCBydW5zIHByZWZpbGwgb25seSBvbiB0aGUgdW5pcXVlIHN1ZmZpeC4gVGhpcyBlbGltaW5hdGVzIE8oTF9zaGFyZWQgKiBOX2xheWVycykgdHJhbnNmb3JtZXIgb3BlcmF0aW9ucyBwZXIgcmVxdWVzdCwgd2hlcmUgTF9zaGFyZWQgaXMgdGhlIHNoYXJlZCBwcmVmaXggbGVuZ3RoIGFuZCBOX2xheWVycyBpcyB0aGUgbnVtYmVyIG9mIHRyYW5zZm9ybWVyIGxheWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS1YgY2FjaGUgbWVtb3J5IGxheW91dDogZHVyaW5nIGEgZm9yd2FyZCBwYXNzIGZvciBhIHNlcXVlbmNlIG9mIFQgdG9rZW5zLCBlYWNoIHRyYW5zZm9ybWVyIGxheWVyIGwgcHJvZHVjZXMga2V5IG1hdHJpeCBLX2wg4oiIIOKEnV4oVMOXZF9rKSBhbmQgdmFsdWUgbWF0cml4IFZfbCDiiIgg4oSdXihUw5dkX3YpLiBUaGVzZSB0ZW5zb3JzIGFyZSByZXF1aXJlZCBieSBzdWJzZXF1ZW50IGxheWVycyBmb3IgYXR0ZW50aW9uIGNvbXB1dGF0aW9uLiBTdGFuZGFyZCBhdXRvcmVncmVzc2l2ZSBkZWNvZGluZyBjYWNoZXMgS1YgdGVuc29ycyBmb3IgcHJldmlvdXNseSBnZW5lcmF0ZWQgdG9rZW5zICh0aGUgZGVjb2RlLXBoYXNlIEtWIGNhY2hlKSB0byBhdm9pZCByZWNvbXB1dGluZyB0aGVtIGVhY2ggc3RlcC4gUHJlZml4IGNhY2hpbmcgZXh0ZW5kcyB0aGlzIGlkZWEgdG8gdGhlIHByZWZpbGwgcGhhc2U6IEtWIHRlbnNvcnMgZm9yIHRoZSBwcm9tcHQgcHJlZml4IGFyZSBzdG9yZWQgYWZ0ZXIgdGhlIGZpcnN0IHJlcXVlc3QgYW5kIHJlbG9hZGVkIGZvciBzdWJzZXF1ZW50IHJlcXVlc3RzLiBUaGUgbWVtb3J5IGNvc3Qgb2Ygc3RvcmluZyBhIHByZWZpeCBjYWNoZSBpcyAyIMOXIFRfcHJlZml4IMOXIE5fbGF5ZXJzIMOXIGRfayDDlyBieXRlc19wZXJfZWxlbWVudC4gRm9yIGEgN0IgbW9kZWwgd2l0aCAzMiBsYXllcnMsIGRfaz0xMjgsIGFuZCBUX3ByZWZpeD0yMDAwIHRva2VucyBpbiBmbG9hdDE2OiAyIMOXIDIwMDAgw5cgMzIgw5cgMTI4IMOXIDIgYnl0ZXMgPSAzMiBNQiDigJQgbW9kZXN0IHJlbGF0aXZlIHRvIHRoZSAxNCBHQiBtb2RlbCB3ZWlnaHRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZWZpeCBDYWNoaW5nIE1lY2hhbmljcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1lY2hhbmljcyBvZiBwcmVmaXggY2FjaGluZyByZXF1aXJlIHRocmVlIGNvbXBvbmVudHM6ICgxKSBhIGNhY2hlIHN0b3JlIG1hcHBpbmcgdG9rZW4gc2VxdWVuY2UgaGFzaGVzIHRvIEtWIHRlbnNvcnMsICgyKSBhIHByZWZpeCBtYXRjaGluZyBhbGdvcml0aG0gdGhhdCBmaW5kcyB0aGUgbG9uZ2VzdCBjYWNoZWQgcHJlZml4IG9mIGFueSBpbmNvbWluZyByZXF1ZXN0LCBhbmQgKDMpIGV2aWN0aW9uIGxvZ2ljIHRvIG1hbmFnZSBHUFUgbWVtb3J5IHdoZW4gdGhlIGNhY2hlIGZpbGxzLiBUaGUgY2FjaGUga2V5IGlzIHR5cGljYWxseSB0aGUgaGFzaCBvZiB0aGUgdG9rZW4gSUQgc2VxdWVuY2UgZm9yIHRoZSBwcmVmaXguIE9uIGEgbmV3IHJlcXVlc3QsIHRoZSBpbmZlcmVuY2Ugc2VydmVyIGhhc2hlcyBwcmVmaXhlcyBvZiBpbmNyZWFzaW5nIGxlbmd0aCBhbmQgbG9va3MgdXAgdGhlIGxvbmdlc3QgbWF0Y2guIENvbXB1dGF0aW9uIHRoZW4gcHJvY2VlZHMgb25seSBmb3IgdGhlIHVuY2FjaGVkIHN1ZmZpeC4gVGhlIGJvdW5kYXJ5IGJldHdlZW4gY2FjaGVkIGFuZCB1bmNhY2hlZCB0b2tlbnMgbXVzdCBhbGlnbiB3aXRoIGEgYmxvY2sgYm91bmRhcnkgKHR5cGljYWxseSAxNiBvciAzMiB0b2tlbnMpIGZvciBtZW1vcnkgbWFuYWdlbWVudCBlZmZpY2llbmN5LiBQYXJ0aWFsLWJsb2NrIGNhY2hpbmcgKGhhbmRsaW5nIHByZWZpeGVzIHRoYXQgZW5kIG1pZC1ibG9jaykgcmVxdWlyZXMgYWRkaXRpb25hbCBib29ra2VlcGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgaGFzaGxpYlxuZnJvbSB0eXBpbmcgaW1wb3J0IE9wdGlvbmFsLCBEaWN0LCBMaXN0LCBUdXBsZVxuZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzLCBmaWVsZFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBUcmllTm9kZTpcbiAgICBjaGlsZHJlbjogRGljdFtpbnQsIFwiVHJpZU5vZGVcIl0gPSBmaWVsZChkZWZhdWx0X2ZhY3Rvcnk9ZGljdClcbiAgICBrdl9jYWNoZTogT3B0aW9uYWxbdG9yY2guVGVuc29yXSA9IE5vbmVcblxuY2xhc3MgUmFkaXhQcmVmaXhDYWNoZTpcbiAgICBcIlwiXCJUcmllLWJhc2VkIEtWIHByZWZpeCBjYWNoZS4gRmluZHMgdGhlIGxvbmdlc3QgY2FjaGVkIHByZWZpeCBmb3IgYW55IHJlcXVlc3QuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLnJvb3QgPSBUcmllTm9kZSgpXG4gICAgICAgIHNlbGYuaGl0cyA9IDBcbiAgICAgICAgc2VsZi5taXNzZXMgPSAwXG5cbiAgICBkZWYgZmluZF9wcmVmaXgoc2VsZiwgdG9rZW5zOiBMaXN0W2ludF0pIC1cdTAwM2UgVHVwbGVbaW50LCBPcHRpb25hbFt0b3JjaC5UZW5zb3JdXTpcbiAgICAgICAgXCJcIlwiUmV0dXJuIChtYXRjaGVkX2xlbmd0aCwga3ZfdGVuc29ycykgZm9yIHRoZSBsb25nZXN0IGNhY2hlZCBwcmVmaXguXCJcIlwiXG4gICAgICAgIG5vZGUgPSBzZWxmLnJvb3RcbiAgICAgICAgbWF0Y2hlZCwgbGFzdF9rdiA9IDAsIE5vbmVcbiAgICAgICAgZm9yIHRvayBpbiB0b2tlbnM6XG4gICAgICAgICAgICBpZiB0b2sgbm90IGluIG5vZGUuY2hpbGRyZW46XG4gICAgICAgICAgICAgICAgc2VsZi5taXNzZXMgKz0gMVxuICAgICAgICAgICAgICAgIGJyZWFrXG4gICAgICAgICAgICBub2RlID0gbm9kZS5jaGlsZHJlblt0b2tdXG4gICAgICAgICAgICBtYXRjaGVkICs9IDFcbiAgICAgICAgICAgIGxhc3Rfa3YgPSBub2RlLmt2X2NhY2hlXG4gICAgICAgIGlmIG1hdGNoZWQgXHUwMDNlIDA6XG4gICAgICAgICAgICBzZWxmLmhpdHMgKz0gMVxuICAgICAgICByZXR1cm4gbWF0Y2hlZCwgbGFzdF9rdlxuXG4gICAgZGVmIHN0b3JlKHNlbGYsIHRva2VuczogTGlzdFtpbnRdLCBrdjogdG9yY2guVGVuc29yKSAtXHUwMDNlIE5vbmU6XG4gICAgICAgIFwiXCJcIkluc2VydCBhIHRva2VuIHNlcXVlbmNlIGFuZCBpdHMgS1YgdGVuc29ycyBpbnRvIHRoZSB0cmllLlwiXCJcIlxuICAgICAgICBub2RlID0gc2VsZi5yb290XG4gICAgICAgIGZvciB0b2sgaW4gdG9rZW5zOlxuICAgICAgICAgICAgaWYgdG9rIG5vdCBpbiBub2RlLmNoaWxkcmVuOlxuICAgICAgICAgICAgICAgIG5vZGUuY2hpbGRyZW5bdG9rXSA9IFRyaWVOb2RlKClcbiAgICAgICAgICAgIG5vZGUgPSBub2RlLmNoaWxkcmVuW3Rva11cbiAgICAgICAgbm9kZS5rdl9jYWNoZSA9IGt2XG5cbiAgICBkZWYgaGl0X3JhdGUoc2VsZikgLVx1MDAzZSBmbG9hdDpcbiAgICAgICAgdG90YWwgPSBzZWxmLmhpdHMgKyBzZWxmLm1pc3Nlc1xuICAgICAgICByZXR1cm4gc2VsZi5oaXRzIC8gdG90YWwgaWYgdG90YWwgXHUwMDNlIDAgZWxzZSAwLjBcblxuIyBEZW1vOiB0d28gcmVxdWVzdHMgc2hhcmluZyBhIHN5c3RlbSBwcm9tcHQgcHJlZml4XG5jYWNoZSA9IFJhZGl4UHJlZml4Q2FjaGUoKVxuc3lzdGVtX3Rva2VucyA9IGxpc3QocmFuZ2UoNTAwKSkgICMgNTAwLXRva2VuIHN5c3RlbSBwcm9tcHRcbmNhY2hlLnN0b3JlKHN5c3RlbV90b2tlbnMsIHRvcmNoLnplcm9zKDEsIDUwMCwgMzIsIDEyOCkpICAjIGZha2UgS1ZcbnJlcXVlc3RfdG9rZW5zID0gc3lzdGVtX3Rva2VucyArIFs2MDEsIDcwMiwgODAzXSAgICAgICAgICAjIHN5c3RlbSArIHVzZXIgcXVlcnlcbm1hdGNoZWQsIGt2ID0gY2FjaGUuZmluZF9wcmVmaXgocmVxdWVzdF90b2tlbnMpXG5wcmludChmXCJQcmVmaXggbWF0Y2hlZDoge21hdGNoZWR9IHRva2VucyAgS1YgcmV1c2VkOiB7a3YgaXMgbm90IE5vbmV9XCIpXG5wcmludChmXCJDYWNoZSBoaXQgcmF0ZToge2NhY2hlLmhpdF9yYXRlKCk6LjIlfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJhZGl4IEF0dGVudGlvbiBUcmVlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTR0xhbmdcdTAwMjdzIFJhZGl4QXR0ZW50aW9uIChaaGVuZyBldCBhbC4sIDIwMjMpIGdlbmVyYWxpemVzIHByZWZpeCBjYWNoaW5nIHRvIGEgcmFkaXggdHJlZSAoY29tcHJlc3NlZCB0cmllKSB0aGF0IHN0b3JlcyBLViBjYWNoZXMgZm9yIGFyYml0cmFyeSBzdWJ0cmVlcyBvZiByZXF1ZXN0IHNlcXVlbmNlcywgbm90IGp1c3QgbGluZWFyIHByZWZpeGVzLiBUaGlzIGhhbmRsZXMgbXVsdGktdHVybiBjb252ZXJzYXRpb25zIHdoZXJlIGVhY2ggdHVybiBzaGFyZXMgYSBncm93aW5nIHByZWZpeCB3aXRoIHByZXZpb3VzIHR1cm5zLCBhcyB3ZWxsIGFzIHRyZWUtc3RydWN0dXJlZCBnZW5lcmF0aW9uIChlLmcuLCBiZWFtIHNlYXJjaCBvciBwYXJhbGxlbCBjaGFpbi1vZi10aG91Z2h0IHNhbXBsaW5nKSB3aGVyZSBtdWx0aXBsZSBjb250aW51YXRpb25zIGJyYW5jaCBmcm9tIHRoZSBzYW1lIHJvb3QuIFRoZSByYWRpeCB0cmVlIG1haW50YWlucyBhIGxlYXN0LXJlY2VudGx5LXVzZWQgKExSVSkgZXZpY3Rpb24gcG9saWN5IGF0IHRoZSBub2RlIGxldmVsOiB3aGVuIEdQVSBtZW1vcnkgcnVucyBsb3csIHRoZSBzZXJ2ZXIgZXZpY3RzIHRoZSBkZWVwZXN0LCBsZWFzdC1yZWNlbnRseS1hY2Nlc3NlZCBub2RlcyBmaXJzdCwgcHJlc2VydmluZyB0aGUgbW9zdCBmcmVxdWVudGx5IHNoYXJlZCByb290cy4gUmFkaXhBdHRlbnRpb24gYWNoaWV2ZXMgY2FjaGUgaGl0IHJhdGVzIG9mIDg14oCTOTUlIGZvciBjaGF0Ym90IHdvcmtsb2FkcyB3aXRoIHNoYXJlZCBzeXN0ZW0gcHJvbXB0cywgY29tcGFyZWQgdG8gMzDigJM1MCUgZm9yIGhhc2gtYmFzZWQgbGluZWFyIHByZWZpeCBjYWNoZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2FjaGUgSGl0IFJhdGUgT3B0aW1pemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDYWNoZSBoaXQgcmF0ZSBkZXBlbmRzIGNyaXRpY2FsbHkgb24gcmVxdWVzdCBvcmRlcmluZyBhbmQgcHJvbXB0IHN0cnVjdHVyZS4gSWYgcmVxdWVzdHMgd2l0aCBpZGVudGljYWwgc3lzdGVtIHByb21wdHMgYXJyaXZlIGludGVybGVhdmVkIHdpdGggcmVxdWVzdHMgdXNpbmcgZGlmZmVyZW50IHN5c3RlbSBwcm9tcHRzLCBjYWNoZWQgS1YgdGVuc29ycyBtYXkgYmUgZXZpY3RlZCBiZWZvcmUgdGhleSBjYW4gYmUgcmV1c2VkLiBCYXRjaGluZyByZXF1ZXN0cyBieSBzaGFyZWQgcHJlZml4IG1heGltaXplcyBoaXQgcmF0ZTogc29ydCBpbmNvbWluZyByZXF1ZXN0cyBzbyB0aGF0IHJlcXVlc3RzIHNoYXJpbmcgYSBwcmVmaXggYXJlIHByb2Nlc3NlZCBjb25zZWN1dGl2ZWx5LiBBdCB0aGUgcHJvbXB0IGxldmVsLCBjb250ZW50IG9yZGVyaW5nIG1hdHRlcnM6IHRoZSBzaGFyZWQgcHJlZml4IG11c3QgYmUgaWRlbnRpY2FsIGF0IHRoZSBieXRlIGxldmVsIOKAlCBldmVuIHdoaXRlc3BhY2UgZGlmZmVyZW5jZXMgaW52YWxpZGF0ZSB0aGUgaGFzaCBtYXRjaC4gUGxhY2luZyBhbGwgc3RhYmxlIGNvbnRlbnQgKHN5c3RlbSBpbnN0cnVjdGlvbnMsIFJBRyBkb2N1bWVudHMsIGZldy1zaG90IGV4YW1wbGVzKSBiZWZvcmUgZHluYW1pYyBjb250ZW50ICh1c2VyIHF1ZXJ5LCBzZXNzaW9uIElEKSBlbnN1cmVzIHRoZSBsb25nZXN0IHBvc3NpYmxlIGNhY2hlZCBwcmVmaXguIEFudGhyb3BpY1x1MDAyN3MgcHJvbXB0IGNhY2hpbmcgQVBJIGZvcm1hbGl6ZXMgdGhpczogdGhlIGRldmVsb3BlciBleHBsaWNpdGx5IG1hcmtzIHN0YWJsZSBibG9ja3Mgd2l0aCBjYWNoZV9jb250cm9sLCBhbmQgdGhlIEFQSSBndWFyYW50ZWVzIGNhY2hpbmcgZm9yIHRob3NlIGJsb2Nrcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRpbWVcbmZyb20gdmxsbSBpbXBvcnQgTExNLCBTYW1wbGluZ1BhcmFtc1xuXG5kZWYgYmVuY2htYXJrX3ZsbG1fcHJlZml4X2NhY2hlKFxuICAgIG1vZGVsX25hbWU6IHN0ciA9IFwibWlzdHJhbGFpL01pc3RyYWwtN0ItdjAuMVwiLFxuICAgIG5fcmVxdWVzdHM6IGludCA9IDUwXG4pIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiQ29tcGFyZSBwcmVmaWxsIHRpbWUgd2l0aCBhbmQgd2l0aG91dCBwcmVmaXggY2FjaGluZyBpbiB2TExNLlwiXCJcIlxuICAgIHN5c3RlbV9wcm9tcHQgPSAoXG4gICAgICAgIFwiWW91IGFyZSBhIHdvcmxkLWNsYXNzIEFJIGFzc2lzdGFudCB3aXRoIGRlZXAgZXhwZXJ0aXNlIGluIG1hdGhlbWF0aWNzLCBcIlxuICAgICAgICBcInBoeXNpY3MsIGFuZCBjb21wdXRlciBzY2llbmNlLiBBbHdheXMgcmVhc29uIHN0ZXAgYnkgc3RlcCBhbmQgc2hvdyB5b3VyIHdvcmsuIFwiXG4gICAgICAgIFwiUHJvdmlkZSByaWdvcm91cyBwcm9vZnMgYW5kIG51bWVyaWNhbCBleGFtcGxlcyB3aGVyZSByZWxldmFudC4gXCJcbiAgICApICogMjUgICMgYXBwcm94IDYwMC10b2tlbiBzaGFyZWQgc3lzdGVtIHByb21wdFxuICAgIHVzZXJfcXVlcmllcyA9IFtmXCJFeHBsYWluIEZvdXJpZXIgdHJhbnNmb3JtIGFwcGxpY2F0aW9uICN7aX0uXCIgZm9yIGkgaW4gcmFuZ2Uobl9yZXF1ZXN0cyldXG4gICAgcHJvbXB0cyA9IFtzeXN0ZW1fcHJvbXB0ICsgXCIgVXNlcjogXCIgKyBxICsgXCIgQXNzaXN0YW50OlwiIGZvciBxIGluIHVzZXJfcXVlcmllc11cbiAgICBwYXJhbXMgPSBTYW1wbGluZ1BhcmFtcyh0ZW1wZXJhdHVyZT0wLjAsIG1heF90b2tlbnM9NjQpXG4gICAgIyBXaXRob3V0IHByZWZpeCBjYWNoaW5nXG4gICAgbGxtX25vID0gTExNKG1vZGVsPW1vZGVsX25hbWUsIGVuYWJsZV9wcmVmaXhfY2FjaGluZz1GYWxzZSwgZ3B1X21lbW9yeV91dGlsaXphdGlvbj0wLjgpXG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgb3V0X25vID0gbGxtX25vLmdlbmVyYXRlKHByb21wdHMsIHBhcmFtcylcbiAgICB0X25vID0gdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwXG4gICAgZGVsIGxsbV9ub1xuICAgICMgV2l0aCBwcmVmaXggY2FjaGluZyBlbmFibGVkXG4gICAgbGxtX3llcyA9IExMTShtb2RlbD1tb2RlbF9uYW1lLCBlbmFibGVfcHJlZml4X2NhY2hpbmc9VHJ1ZSwgZ3B1X21lbW9yeV91dGlsaXphdGlvbj0wLjgpXG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgb3V0X3llcyA9IGxsbV95ZXMuZ2VuZXJhdGUocHJvbXB0cywgcGFyYW1zKVxuICAgIHRfeWVzID0gdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwXG4gICAgZGVsIGxsbV95ZXNcbiAgICBwcmludChmXCJObyBjYWNoZTogICB7dF9ubzouMmZ9cyBmb3Ige25fcmVxdWVzdHN9IHJlcXVlc3RzXCIpXG4gICAgcHJpbnQoZlwiV2l0aCBjYWNoZToge3RfeWVzOi4yZn1zIGZvciB7bl9yZXF1ZXN0c30gcmVxdWVzdHNcIilcbiAgICBwcmludChmXCJQcmVmaWxsIHNwZWVkdXA6IHt0X25vIC8gdF95ZXM6LjJmfXhcIilcbiAgICAjIFZlcmlmeSBpZGVudGljYWwgb3V0cHV0c1xuICAgIGZvciBhLCBiIGluIHppcChvdXRfbm8sIG91dF95ZXMpOlxuICAgICAgICBhc3NlcnQgYS5vdXRwdXRzWzBdLnRleHQgPT0gYi5vdXRwdXRzWzBdLnRleHRcbiAgICByZXR1cm4gdF9ubyAvIHRfeWVzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQW50aHJvcGljIGFuZCBPcGVuQUkgUHJvbXB0IENhY2hpbmcgQVBJcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQm90aCBBbnRocm9waWMgYW5kIE9wZW5BSSBleHBvc2UgcHJvbXB0IGNhY2hpbmcgdGhyb3VnaCB0aGVpciBBUElzLCBhbGxvd2luZyBkZXZlbG9wZXJzIHRvIG1hcmsgc3BlY2lmaWMgY29udGVudCBibG9ja3MgYXMgY2FjaGVhYmxlLiBBbnRocm9waWNcdTAwMjdzIGltcGxlbWVudGF0aW9uIHVzZXMgY2FjaGVfY29udHJvbDoge3R5cGU6IGVwaGVtZXJhbH0gb24gbWVzc2FnZSBjb250ZW50IGJsb2NrczsgY2FjaGVkIGJsb2NrcyBhcmUgc3RvcmVkIGZvciA1IG1pbnV0ZXMgYnkgZGVmYXVsdC4gVXNhZ2Ugc3RhdGlzdGljcyBpbiB0aGUgcmVzcG9uc2UgaW5kaWNhdGUgY2FjaGVfY3JlYXRpb25faW5wdXRfdG9rZW5zICh0b2tlbnMgd3JpdHRlbiB0byBjYWNoZSBvbiBhIG1pc3MpIGFuZCBjYWNoZV9yZWFkX2lucHV0X3Rva2VucyAodG9rZW5zIHNlcnZlZCBmcm9tIGNhY2hlIG9uIGEgaGl0KS4gQ2FjaGUgcmVhZHMgYXJlIHByaWNlZCBhdCByb3VnaGx5IDEwJSBvZiBub3JtYWwgaW5wdXQgdG9rZW4gY29zdCwgbWFraW5nIGhlYXZ5IHN5c3RlbSBwcm9tcHRzICg0S+KAkzMySyB0b2tlbnMpIGV4dHJlbWVseSBlY29ub21pY2FsIHdoZW4gcmV1c2VkIGFjcm9zcyBtYW55IHR1cm5zLiBPcGVuQUlcdTAwMjdzIGltcGxlbWVudGF0aW9uIGlzIGF1dG9tYXRpYyBmb3IgcHJvbXB0cyBzaGFyaW5nIGEgY29tbW9uIHByZWZpeCBvZiBhdCBsZWFzdCAxMDI0IHRva2Vucywgd2l0aCBubyBleHBsaWNpdCBjYWNoZV9jb250cm9sIG1hcmtlcnMgcmVxdWlyZWQuIEJvdGggQVBJcyBndWFyYW50ZWUgdGhhdCBjYWNoZWQgY29tcHV0YXRpb24gZG9lcyBub3QgYWZmZWN0IG91dHB1dCBxdWFsaXR5IOKAlCB0aGUgc2FtZSBndWFyYW50ZWVzIGFzIHNlcnZlci1zaWRlIHByZWZpeCBjYWNoaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgYW50aHJvcGljXG5pbXBvcnQgdGltZVxuXG5kZWYgZGVtb19hbnRocm9waWNfcHJvbXB0X2NhY2hlKGRvY190ZXh0OiBzdHIpIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJTaG93IEFudGhyb3BpYyBwcm9tcHQgY2FjaGluZzogbWFyayBzdGFibGUgY29udGVudCB3aXRoIGNhY2hlX2NvbnRyb2wuXCJcIlwiXG4gICAgY2xpZW50ID0gYW50aHJvcGljLkFudGhyb3BpYygpXG4gICAgbWVzc2FnZXNfY2FjaGVkID0gW3tcInJvbGVcIjogXCJ1c2VyXCIsIFwiY29udGVudFwiOiBbXG4gICAgICAgIHtcInR5cGVcIjogXCJ0ZXh0XCIsIFwidGV4dFwiOiBkb2NfdGV4dCxcbiAgICAgICAgIFwiY2FjaGVfY29udHJvbFwiOiB7XCJ0eXBlXCI6IFwiZXBoZW1lcmFsXCJ9fSxcbiAgICAgICAge1widHlwZVwiOiBcInRleHRcIiwgXCJ0ZXh0XCI6IFwiU3VtbWFyaXplIHRoZSBrZXkgZmluZGluZ3MgaW4gMyBidWxsZXQgcG9pbnRzLlwifVxuICAgIF19XVxuICAgIG1lc3NhZ2VzX25vX2NhY2hlID0gW3tcInJvbGVcIjogXCJ1c2VyXCIsIFwiY29udGVudFwiOiBkb2NfdGV4dCArXG4gICAgICAgICAgICAgICAgICAgICAgICAgIFwiIFN1bW1hcml6ZSB0aGUga2V5IGZpbmRpbmdzIGluIDMgYnVsbGV0IHBvaW50cy5cIn1dXG4gICAgIyBGaXJzdCBjYWxsOiBjb2xkIGNhY2hlIG1pc3Mg4oCUIGZ1bGwgcHJlZmlsbCBiaWxsZWQgYXQgc3RhbmRhcmQgcmF0ZVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHIxID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShtb2RlbD1cImNsYXVkZS1vcHVzLTQtNVwiLCBtYXhfdG9rZW5zPTI1NixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VzPW1lc3NhZ2VzX2NhY2hlZClcbiAgICB0MSA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgICMgU2Vjb25kIGNhbGw6IGNhY2hlIGhpdCDigJQgb25seSBuZXcgdG9rZW5zIGJpbGxlZFxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHIyID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShtb2RlbD1cImNsYXVkZS1vcHVzLTQtNVwiLCBtYXhfdG9rZW5zPTI1NixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VzPW1lc3NhZ2VzX2NhY2hlZClcbiAgICB0MiA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgIHByaW50KGZcIkNhbGwgMSDigJQgY3JlYXRlZDoge3IxLnVzYWdlLmNhY2hlX2NyZWF0aW9uX2lucHV0X3Rva2Vuc30gY2FjaGUgdG9rZW5zLCByZWFkOiB7cjEudXNhZ2UuY2FjaGVfcmVhZF9pbnB1dF90b2tlbnN9LCB0aW1lOiB7dDE6LjJmfXNcIilcbiAgICBwcmludChmXCJDYWxsIDIg4oCUIGNyZWF0ZWQ6IHtyMi51c2FnZS5jYWNoZV9jcmVhdGlvbl9pbnB1dF90b2tlbnN9IGNhY2hlIHRva2VucywgcmVhZDoge3IyLnVzYWdlLmNhY2hlX3JlYWRfaW5wdXRfdG9rZW5zfSwgdGltZToge3QyOi4yZn1zXCIpXG4gICAgcHJpbnQoZlwiTGF0ZW5jeSByZWR1Y3Rpb246IHsodDEgLSB0MikgLyB0MSAqIDEwMDouMWZ9JVwiKVxuICAgIHJldHVybiB7XCJjb2xkX3RpbWVcIjogdDEsIFwid2FybV90aW1lXCI6IHQyLCBcInNwZWVkdXBcIjogdDEgLyB0Mn0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPbi1kZXZpY2UgUHJlZml4IENhY2hpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9uLWRldmljZSBpbmZlcmVuY2UgKGUuZy4sIG1vYmlsZSBvciBlZGdlIGRlcGxveW1lbnRzIHVzaW5nIGxsYW1hLmNwcCBvciBNTEMtTExNKSBjYW4gYWxzbyBiZW5lZml0IGZyb20gcHJlZml4IGNhY2hpbmcgd2hlbiB0aGUgc2FtZSBzeXN0ZW0gcHJvbXB0IG9yIGNvbnRleHQgaXMgcmV1c2VkIGFjcm9zcyBtdWx0aXBsZSB1c2VyIHNlc3Npb25zLiBsbGFtYS5jcHBcdTAwMjdzIHNlc3Npb24gZmlsZSBmZWF0dXJlIHNhdmVzIGFuZCBsb2FkcyB0aGUgS1YgY2FjaGUgc3RhdGUgZm9yIGEgZ2l2ZW4gcHJvbXB0IHByZWZpeCB0by9mcm9tIGRpc2ssIGFsbG93aW5nIHRoZSBuZXh0IGluZmVyZW5jZSBzZXNzaW9uIHRvIHNraXAgcHJlZmlsbCBlbnRpcmVseSBmb3IgdGhlIGNhY2hlZCBwb3J0aW9uLiBUaGUgY2hhbGxlbmdlIG9uIGRldmljZSBpcyBtZW1vcnk6IGEgNC1iaXQgcXVhbnRpemVkIDdCIG1vZGVsXHUwMDI3cyBLViBjYWNoZSBmb3IgMjAwMCB0b2tlbnMgaXMgYXBwcm94aW1hdGVseSAxNiBNQiwgd2hpY2ggaXMgZmVhc2libGUgb24gZGV2aWNlcyB3aXRoIDgrIEdCIFJBTS4gVGhlIGNhY2hlIG11c3QgYmUgaW52YWxpZGF0ZWQgd2hlbiB0aGUgbW9kZWwgd2VpZ2h0cyBjaGFuZ2UgKGUuZy4sIGFmdGVyIGFuIGFwcCB1cGRhdGUpLiBGb3IgY29udmVyc2F0aW9uYWwgYXNzaXN0YW50cyB3aGVyZSB0aGUgc3lzdGVtIHByb21wdCBpcyBmaXhlZCBhbmQgdGhlIHVzZXIgcXVlcnkgaXMgYWx3YXlzIGFwcGVuZGVkIGF0IHRoZSBlbmQsIGRpc2stYmFzZWQgS1YgY2FjaGUgcGVyc2lzdGVuY2UgY2FuIGVsaW1pbmF0ZSBzeXN0ZW0gcHJvbXB0IHByZWZpbGwgbGF0ZW5jeSBlbnRpcmVseSBvbiB0aGUgc2Vjb25kIGFuZCBzdWJzZXF1ZW50IHR1cm5zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgaGFzaGxpYlxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3QsIFR1cGxlXG5mcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBkZWZhdWx0ZGljdFxuXG5kZWYgb3B0aW1pemVfcmVxdWVzdF9vcmRlcmluZyhcbiAgICBwcm9tcHRzOiBMaXN0W3N0cl0sXG4gICAgcHJlZml4X2xlbmd0aHM6IExpc3RbaW50XSA9IFs2NCwgMTI4LCAyNTYsIDUxMl1cbikgLVx1MDAzZSBUdXBsZVtMaXN0W3N0cl0sIGZsb2F0XTpcbiAgICBcIlwiXCJTb3J0IHByb21wdHMgdG8gbWF4aW1pemUgcHJlZml4IGNhY2hlIGhpdHMgKGdyb3VwIGJ5IHNoYXJlZCBwcmVmaXhlcyBmaXJzdCkuXCJcIlwiXG4gICAgZGVmIHByZWZpeF9rZXkodGV4dDogc3RyLCBsZW5ndGg6IGludCkgLVx1MDAzZSBzdHI6XG4gICAgICAgIHJldHVybiBoYXNobGliLnNoYTI1Nih0ZXh0WzpsZW5ndGhdLmVuY29kZSgpKS5oZXhkaWdlc3QoKSBpZiBsZW4odGV4dCkgXHUwMDNlPSBsZW5ndGggZWxzZSBcIlwiXG4gICAgIyBTY29yZSBlYWNoIHByb21wdCBieSBob3cgbWFueSBvdGhlcnMgc2hhcmUgaXRzIHByZWZpeGVzXG4gICAgZnJlcTogZGVmYXVsdGRpY3QgPSBkZWZhdWx0ZGljdChpbnQpXG4gICAgZm9yIHAgaW4gcHJvbXB0czpcbiAgICAgICAgZm9yIEwgaW4gcHJlZml4X2xlbmd0aHM6XG4gICAgICAgICAgICBrID0gcHJlZml4X2tleShwLCBMKVxuICAgICAgICAgICAgaWYgazpcbiAgICAgICAgICAgICAgICBmcmVxW2tdICs9IDFcbiAgICBkZWYgc2NvcmUocDogc3RyKSAtXHUwMDNlIGludDpcbiAgICAgICAgcmV0dXJuIHN1bShmcmVxW3ByZWZpeF9rZXkocCwgTCldIGZvciBMIGluIHByZWZpeF9sZW5ndGhzIGlmIGxlbihwKSBcdTAwM2U9IEwpXG4gICAgc29ydGVkX3Byb21wdHMgPSBzb3J0ZWQocHJvbXB0cywga2V5PXNjb3JlLCByZXZlcnNlPVRydWUpXG4gICAgIyBFc3RpbWF0ZSBjYWNoZSBoaXQgcmF0ZSBhZnRlciBzb3J0aW5nXG4gICAgc2Vlbl9wcmVmaXhlczogc2V0ID0gc2V0KClcbiAgICBoaXRzID0gMFxuICAgIGZvciBwIGluIHNvcnRlZF9wcm9tcHRzOlxuICAgICAgICBrID0gcHJlZml4X2tleShwLCBwcmVmaXhfbGVuZ3Roc1stMV0pXG4gICAgICAgIGlmIGsgaW4gc2Vlbl9wcmVmaXhlczpcbiAgICAgICAgICAgIGhpdHMgKz0gMVxuICAgICAgICBzZWVuX3ByZWZpeGVzLmFkZChrKVxuICAgIGhpdF9yYXRlID0gaGl0cyAvIGxlbihwcm9tcHRzKSBpZiBwcm9tcHRzIGVsc2UgMC4wXG4gICAgcHJpbnQoZlwiRXN0aW1hdGVkIGNhY2hlIGhpdCByYXRlIGFmdGVyIG9yZGVyaW5nOiB7aGl0X3JhdGU6LjIlfVwiKVxuICAgIHJldHVybiBzb3J0ZWRfcHJvbXB0cywgaGl0X3JhdGUifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb3N0IFNhdmluZ3MgQW5hbHlzaXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBlY29ub21pYyBpbXBhY3Qgb2YgcHJvbXB0IGNhY2hpbmcgaXMgbGFyZ2VzdCBmb3Igd29ya2xvYWRzIHdpdGggbG9uZywgc2hhcmVkIHByZWZpeGVzIGFuZCBtYW55IHJlcXVlc3RzLiBBIFJBRyBhcHBsaWNhdGlvbiB3aXRoIGEgZml4ZWQgODAwMC10b2tlbiBrbm93bGVkZ2UgYmFzZSBwcmVmaXggc2VudCB3aXRoIGV2ZXJ5IHF1ZXJ5LCBzZXJ2aW5nIDEwMCwwMDAgZGFpbHkgcmVxdWVzdHMsIHdvdWxkIHdpdGhvdXQgY2FjaGluZyBwYXkgZm9yIDgwMDAgw5cgMTAwLDAwMCA9IDgwME0gaW5wdXQgdG9rZW5zIHBlciBkYXkuIFdpdGggOTAlIGNhY2hlIGhpdCByYXRlLCBvbmx5IDgwTSB0b2tlbnMgbmVlZCBmdWxsIHByZWZpbGwgY29tcHV0YXRpb24sIHdpdGggdGhlIHJlbWFpbmluZyA3MjBNIHNlcnZlZCBmcm9tIGNhY2hlIGF0IDEwJSBvZiBub3JtYWwgY29zdC4gVGhlIGVmZmVjdGl2ZSBpbnB1dCB0b2tlbiBjb3N0IGRyb3BzIHRvIDEwJSDDlyA3MjBNICsgMTAwJSDDlyA4ME0gPSAxNTJNIGVxdWl2YWxlbnQgdG9rZW5zIOKAlCBhbiA4MSUgcmVkdWN0aW9uIGluIGlucHV0LXNpZGUgY29tcHV0ZSBjb3N0cy4gVGhlIHNhdmluZ3MgYXJlIHByb3BvcnRpb25hbCB0byBwcmVmaXggbGVuZ3RoLCByZXF1ZXN0IHZvbHVtZSwgYW5kIGNhY2hlIGhpdCByYXRlLiBTaG9ydCBwcmVmaXhlcyBvciBsb3cgcmVxdWVzdCByYXRlcyBtYXkgbm90IGp1c3RpZnkgdGhlIGVuZ2luZWVyaW5nIG92ZXJoZWFkIG9mIGltcGxlbWVudGluZyBwcmVmaXggY2FjaGluZy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiU2NlbmFyaW8iLCJQcmVmaXggTGVuZ3RoICh0b2tlbnMpIiwiQ2FjaGUgSGl0IFJhdGUiLCJQcmVmaWxsIFNhdmluZ3MiLCJFZmZlY3RpdmUgQ29zdCBSZWR1Y3Rpb24iXSwicm93cyI6W1siU2hhcmVkIHN5c3RlbSBwcm9tcHQgKHNob3J0KSIsIjIwMCIsIjkwJSIsIjkwJSBvZiBwcmVmaXggcHJlZmlsbCBza2lwcGVkIiwiNDXigJM2MCUiXSxbIlJBRyB3aXRoIGZpeGVkIGRvY3VtZW50IHNldCIsIjQwMDDigJM4MDAwIiwiODUlIiwiODUlIG9mIHByZWZpeCBwcmVmaWxsIHNraXBwZWQiLCI3MOKAkzgwJSJdLFsiQ29kZSBjb250ZXh0IHdpbmRvdyIsIjIwMDDigJM0MDAwIiwiNzAlIiwiNzAlIG9mIHByZWZpeCBwcmVmaWxsIHNraXBwZWQiLCI1NeKAkzY1JSJdLFsiTXVsdGktdHVybiBjb252ZXJzYXRpb25hbCBoaXN0b3J5IiwiNTAw4oCTMjAwMCAoZ3Jvd2luZykiLCI2MCUiLCI2MCUgb2YgaGlzdG9yeSBwcmVmaWxsIHNraXBwZWQiLCI0MOKAkzU1JSJdLFsiTWl4ZWQgd29ya2xvYWQgKHZhcmllZCBwcmVmaXhlcykiLCIxMDAwIGF2ZyIsIjQwJSIsIjQwJSBvZiBwcmVmaXggcHJlZmlsbCBza2lwcGVkIiwiMjXigJMzNSUiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJTdHJ1Y3R1cmUgUHJvbXB0cyBmb3IgTWF4aW11bSBDYWNoZSBSZXVzZSIsImNvbnRlbnQiOiJQdXQgeW91ciBsb25nZXN0LCBtb3N0IHJldXNlZCBjb250ZW50IGF0IHRoZSBiZWdpbm5pbmcgb2YgdGhlIHByb21wdCAoc3lzdGVtIGluc3RydWN0aW9ucywgUkFHIGNvbnRleHQsIGV4YW1wbGVzKSBhbmQgZHluYW1pYyBjb250ZW50IGF0IHRoZSBlbmQg4oCUIHByZWZpeCBjYWNoZXMgb25seSBtYXRjaCBmcm9tIHRoZSBzdGFydCBvZiB0aGUgc2VxdWVuY2UuIEV2ZW4gYSBzaW5nbGUgY2hhcmFjdGVyIGRpZmZlcmVuY2UgYXQgcG9zaXRpb24gMSBpbnZhbGlkYXRlcyB0aGUgZW50aXJlIGNhY2hlIG1hdGNoIGZvciB0aGF0IHJlcXVlc3QuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUHJlZml4IGNhY2hpbmcgc3RvcmVzIEtWIHRlbnNvcnMgZm9yIHNoYXJlZCBwcm9tcHQgcHJlZml4ZXMgYW5kIHJldXNlcyB0aGVtIGFjcm9zcyByZXF1ZXN0cyDigJQgZWxpbWluYXRpbmcgcmVkdW5kYW50IHByZWZpbGwgY29tcHV0YXRpb24gZW50aXJlbHkgZm9yIGNhY2hlZCB0b2tlbnMuIiwiQSB0cmllIChyYWRpeCB0cmVlKSBzdHJ1Y3R1cmUgZW5hYmxlcyBlZmZpY2llbnQgbG9uZ2VzdC1wcmVmaXggbWF0Y2hpbmc6IGVhY2ggbm9kZSBzdG9yZXMgS1YgdGVuc29ycyBmb3IgYSB0b2tlbiBzZXF1ZW5jZSBwcmVmaXgsIHdpdGggTFJVIGV2aWN0aW9uIGZvciBtZW1vcnkgbWFuYWdlbWVudC4iLCJ2TExNIGVuYWJsZXMgcHJlZml4IGNhY2hpbmcgd2l0aCBhIHNpbmdsZSBmbGFnOiBMTE0oZW5hYmxlX3ByZWZpeF9jYWNoaW5nPVRydWUpOyBubyBvdGhlciBjb2RlIGNoYW5nZXMgYXJlIHJlcXVpcmVkLiIsIkFudGhyb3BpYyBhbmQgT3BlbkFJIEFQSXMgZXhwb3NlIHByb21wdCBjYWNoaW5nIGV4cGxpY2l0bHkg4oCUIG1hcmsgc3RhYmxlIGNvbnRlbnQgYmxvY2tzIHdpdGggY2FjaGVfY29udHJvbDsgY2FjaGVkIHRva2VucyBjb3N0IH4xMCUgb2Ygbm9ybWFsIGlucHV0IHRva2VuIHByaWNlLiIsIkZvciBtYXhpbXVtIGhpdCByYXRlLCBhbHdheXMgcGxhY2Ugc3RhYmxlIGNvbnRlbnQgKHN5c3RlbSBwcm9tcHQsIFJBRyBjb250ZXh0KSBiZWZvcmUgZHluYW1pYyBjb250ZW50ICh1c2VyIHF1ZXJ5KSBpbiB5b3VyIHByb21wdCBzdHJ1Y3R1cmUuIiwiT24tZGV2aWNlIGluZmVyZW5jZSBjYW4gcGVyc2lzdCBLViBjYWNoZXMgdG8gZGlzayBiZXR3ZWVuIHNlc3Npb25zIHVzaW5nIHNlc3Npb24gZmlsZXMgKGxsYW1hLmNwcCkgdG8gc2tpcCBzeXN0ZW0gcHJvbXB0IHByZWZpbGwgb24gd2FybSBzdGFydHMuIiwiQ2FjaGUgaGl0IHJhdGUgb2YgODDigJM5MCUgaXMgYWNoaWV2YWJsZSBmb3IgY2hhdGJvdCB3b3JrbG9hZHMgd2l0aCBhIGZpeGVkIHN5c3RlbSBwcm9tcHQ7IFJBRyB3aXRoIGEgZml4ZWQgZG9jdW1lbnQgc2V0IGNhbiBhY2hpZXZlIDg14oCTOTUlLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Prompt Caching in LLM Inference

Prompt caching (also called prefix caching or KV cache reuse) is a server-side inference optimization that stores the key-value (KV) tensors computed during the prefill phase for a prompt prefix and reuses them across subsequent requests that share the same prefix. Without caching, every request — even if it shares a 2000-token system prompt with the previous one — recomputes all 2000 tokens from scratch. With caching, the server detects the shared prefix, loads its precomputed KV tensors from memory, and runs prefill only on the unique suffix. This eliminates O(L_shared * N_layers) transformer operations per request, where L_shared is the shared prefix length and N_layers is the number of transformer layers.

## Overview

KV cache memory layout: during a forward pass for a sequence of T tokens, each transformer layer l produces key matrix K_l ∈ ℝ^(T×d_k) and value matrix V_l ∈ ℝ^(T×d_v). These tensors are required by subsequent layers for attention computation. Standard autoregressive decoding caches KV tensors for previously generated tokens (the decode-phase KV cache) to avoid recomputing them each step. Prefix caching extends this idea to the prefill phase: KV tensors for the prompt prefix are stored after the first request and reloaded for subsequent requests. The memory cost of storing a prefix cache is 2 × T_prefix × N_layers × d_k × bytes_per_element. For a 7B model with 32 layers, d_k=128, and T_prefix=2000 tokens in float16: 2 × 2000 × 32 × 128 × 2 bytes = 32 MB — modest relative to the 14 GB model weights.

## Prefix Caching Mechanics

The mechanics of prefix caching require three components: (1) a cache store mapping token sequence hashes to KV tensors, (2) a prefix matching algorithm that finds the longest cached prefix of any incoming request, and (3) eviction logic to manage GPU memory when the cache fills. The cache key is typically the hash of the token ID sequence for the prefix. On a new request, the inference server hashes prefixes of increasing length and looks up the longest match. Computation then proceeds only for the uncached suffix. The boundary between cached and uncached tokens must align with a block boundary (typically 16 or 32 tokens) for memory management efficiency. Partial-block caching (handling prefixes that end mid-block) requires additional bookkeeping.

```python
import torch
import hashlib
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: Dict[int, "TrieNode"] = field(default_factory=dict)
    kv_cache: Optional[torch.Tensor] = None

class RadixPrefixCache:
    """Trie-based KV prefix cache. Finds the longest cached prefix for any request."""
    def __init__(self):
        self.root = TrieNode()
        self.hits = 0
        self.misses = 0

    def find_prefix(self, tokens: List[int]) -> Tuple[int, Optional[torch.Tensor]]:
        """Return (matched_length, kv_tensors) for the longest cached prefix."""
        node = self.root
        matched, last_kv = 0, None
        for tok in tokens:
            if tok not in node.children:
                self.misses += 1
                break
            node = node.children[tok]
            matched += 1
            last_kv = node.kv_cache
        if matched > 0:
            self.hits += 1
        return matched, last_kv

    def store(self, tokens: List[int], kv: torch.Tensor) -> None:
        """Insert a token sequence and its KV tensors into the trie."""
        node = self.root
        for tok in tokens:
            if tok not in node.children:
                node.children[tok] = TrieNode()
            node = node.children[tok]
        node.kv_cache = kv

    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0

# Demo: two requests sharing a system prompt prefix
cache = RadixPrefixCache()
system_tokens = list(range(500))  # 500-token system prompt
cache.store(system_tokens, torch.zeros(1, 500, 32, 128))  # fake KV
request_tokens = system_tokens + [601, 702, 803]          # system + user query
matched, kv = cache.find_prefix(request_tokens)
print(f"Prefix matched: {matched} tokens  KV reused: {kv is not None}")
print(f"Cache hit rate: {cache.hit_rate():.2%}")
```

## Radix Attention Tree

SGLang's RadixAttention (Zheng et al., 2023) generalizes prefix caching to a radix tree (compressed trie) that stores KV caches for arbitrary subtrees of request sequences, not just linear prefixes. This handles multi-turn conversations where each turn shares a growing prefix with previous turns, as well as tree-structured generation (e.g., beam search or parallel chain-of-thought sampling) where multiple continuations branch from the same root. The radix tree maintains a least-recently-used (LRU) eviction policy at the node level: when GPU memory runs low, the server evicts the deepest, least-recently-accessed nodes first, preserving the most frequently shared roots. RadixAttention achieves cache hit rates of 85–95% for chatbot workloads with shared system prompts, compared to 30–50% for hash-based linear prefix caches.

## Cache Hit Rate Optimization

Cache hit rate depends critically on request ordering and prompt structure. If requests with identical system prompts arrive interleaved with requests using different system prompts, cached KV tensors may be evicted before they can be reused. Batching requests by shared prefix maximizes hit rate: sort incoming requests so that requests sharing a prefix are processed consecutively. At the prompt level, content ordering matters: the shared prefix must be identical at the byte level — even whitespace differences invalidate the hash match. Placing all stable content (system instructions, RAG documents, few-shot examples) before dynamic content (user query, session ID) ensures the longest possible cached prefix. Anthropic's prompt caching API formalizes this: the developer explicitly marks stable blocks with cache_control, and the API guarantees caching for those blocks.

```python
import time
from vllm import LLM, SamplingParams

def benchmark_vllm_prefix_cache(
    model_name: str = "mistralai/Mistral-7B-v0.1",
    n_requests: int = 50
) -> float:
    """Compare prefill time with and without prefix caching in vLLM."""
    system_prompt = (
        "You are a world-class AI assistant with deep expertise in mathematics, "
        "physics, and computer science. Always reason step by step and show your work. "
        "Provide rigorous proofs and numerical examples where relevant. "
    ) * 25  # approx 600-token shared system prompt
    user_queries = [f"Explain Fourier transform application #{i}." for i in range(n_requests)]
    prompts = [system_prompt + " User: " + q + " Assistant:" for q in user_queries]
    params = SamplingParams(temperature=0.0, max_tokens=64)
    # Without prefix caching
    llm_no = LLM(model=model_name, enable_prefix_caching=False, gpu_memory_utilization=0.8)
    t0 = time.perf_counter()
    out_no = llm_no.generate(prompts, params)
    t_no = time.perf_counter() - t0
    del llm_no
    # With prefix caching enabled
    llm_yes = LLM(model=model_name, enable_prefix_caching=True, gpu_memory_utilization=0.8)
    t0 = time.perf_counter()
    out_yes = llm_yes.generate(prompts, params)
    t_yes = time.perf_counter() - t0
    del llm_yes
    print(f"No cache:   {t_no:.2f}s for {n_requests} requests")
    print(f"With cache: {t_yes:.2f}s for {n_requests} requests")
    print(f"Prefill speedup: {t_no / t_yes:.2f}x")
    # Verify identical outputs
    for a, b in zip(out_no, out_yes):
        assert a.outputs[0].text == b.outputs[0].text
    return t_no / t_yes
```

## Anthropic and OpenAI Prompt Caching APIs

Both Anthropic and OpenAI expose prompt caching through their APIs, allowing developers to mark specific content blocks as cacheable. Anthropic's implementation uses cache_control: {type: ephemeral} on message content blocks; cached blocks are stored for 5 minutes by default. Usage statistics in the response indicate cache_creation_input_tokens (tokens written to cache on a miss) and cache_read_input_tokens (tokens served from cache on a hit). Cache reads are priced at roughly 10% of normal input token cost, making heavy system prompts (4K–32K tokens) extremely economical when reused across many turns. OpenAI's implementation is automatic for prompts sharing a common prefix of at least 1024 tokens, with no explicit cache_control markers required. Both APIs guarantee that cached computation does not affect output quality — the same guarantees as server-side prefix caching.

```python
import anthropic
import time

def demo_anthropic_prompt_cache(doc_text: str) -> dict:
    """Show Anthropic prompt caching: mark stable content with cache_control."""
    client = anthropic.Anthropic()
    messages_cached = [{"role": "user", "content": [
        {"type": "text", "text": doc_text,
         "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": "Summarize the key findings in 3 bullet points."}
    ]}]
    messages_no_cache = [{"role": "user", "content": doc_text +
                          " Summarize the key findings in 3 bullet points."}]
    # First call: cold cache miss — full prefill billed at standard rate
    t0 = time.perf_counter()
    r1 = client.messages.create(model="claude-opus-4-5", max_tokens=256,
                                 messages=messages_cached)
    t1 = time.perf_counter() - t0
    # Second call: cache hit — only new tokens billed
    t0 = time.perf_counter()
    r2 = client.messages.create(model="claude-opus-4-5", max_tokens=256,
                                 messages=messages_cached)
    t2 = time.perf_counter() - t0
    print(f"Call 1 — created: {r1.usage.cache_creation_input_tokens} cache tokens, read: {r1.usage.cache_read_input_tokens}, time: {t1:.2f}s")
    print(f"Call 2 — created: {r2.usage.cache_creation_input_tokens} cache tokens, read: {r2.usage.cache_read_input_tokens}, time: {t2:.2f}s")
    print(f"Latency reduction: {(t1 - t2) / t1 * 100:.1f}%")
    return {"cold_time": t1, "warm_time": t2, "speedup": t1 / t2}
```

## On-device Prefix Caching

On-device inference (e.g., mobile or edge deployments using llama.cpp or MLC-LLM) can also benefit from prefix caching when the same system prompt or context is reused across multiple user sessions. llama.cpp's session file feature saves and loads the KV cache state for a given prompt prefix to/from disk, allowing the next inference session to skip prefill entirely for the cached portion. The challenge on device is memory: a 4-bit quantized 7B model's KV cache for 2000 tokens is approximately 16 MB, which is feasible on devices with 8+ GB RAM. The cache must be invalidated when the model weights change (e.g., after an app update). For conversational assistants where the system prompt is fixed and the user query is always appended at the end, disk-based KV cache persistence can eliminate system prompt prefill latency entirely on the second and subsequent turns.

```python
import hashlib
from typing import List, Tuple
from collections import defaultdict

def optimize_request_ordering(
    prompts: List[str],
    prefix_lengths: List[int] = [64, 128, 256, 512]
) -> Tuple[List[str], float]:
    """Sort prompts to maximize prefix cache hits (group by shared prefixes first)."""
    def prefix_key(text: str, length: int) -> str:
        return hashlib.sha256(text[:length].encode()).hexdigest() if len(text) >= length else ""
    # Score each prompt by how many others share its prefixes
    freq: defaultdict = defaultdict(int)
    for p in prompts:
        for L in prefix_lengths:
            k = prefix_key(p, L)
            if k:
                freq[k] += 1
    def score(p: str) -> int:
        return sum(freq[prefix_key(p, L)] for L in prefix_lengths if len(p) >= L)
    sorted_prompts = sorted(prompts, key=score, reverse=True)
    # Estimate cache hit rate after sorting
    seen_prefixes: set = set()
    hits = 0
    for p in sorted_prompts:
        k = prefix_key(p, prefix_lengths[-1])
        if k in seen_prefixes:
            hits += 1
        seen_prefixes.add(k)
    hit_rate = hits / len(prompts) if prompts else 0.0
    print(f"Estimated cache hit rate after ordering: {hit_rate:.2%}")
    return sorted_prompts, hit_rate
```

## Cost Savings Analysis

The economic impact of prompt caching is largest for workloads with long, shared prefixes and many requests. A RAG application with a fixed 8000-token knowledge base prefix sent with every query, serving 100,000 daily requests, would without caching pay for 8000 × 100,000 = 800M input tokens per day. With 90% cache hit rate, only 80M tokens need full prefill computation, with the remaining 720M served from cache at 10% of normal cost. The effective input token cost drops to 10% × 720M + 100% × 80M = 152M equivalent tokens — an 81% reduction in input-side compute costs. The savings are proportional to prefix length, request volume, and cache hit rate. Short prefixes or low request rates may not justify the engineering overhead of implementing prefix caching.

| Scenario | Prefix Length (tokens) | Cache Hit Rate | Prefill Savings | Effective Cost Reduction |
| --- | --- | --- | --- | --- |
| Shared system prompt (short) | 200 | 90% | 90% of prefix prefill skipped | 45–60% |
| RAG with fixed document set | 4000–8000 | 85% | 85% of prefix prefill skipped | 70–80% |
| Code context window | 2000–4000 | 70% | 70% of prefix prefill skipped | 55–65% |
| Multi-turn conversational history | 500–2000 (growing) | 60% | 60% of history prefill skipped | 40–55% |
| Mixed workload (varied prefixes) | 1000 avg | 40% | 40% of prefix prefill skipped | 25–35% |

> **Structure Prompts for Maximum Cache Reuse**: Put your longest, most reused content at the beginning of the prompt (system instructions, RAG context, examples) and dynamic content at the end — prefix caches only match from the start of the sequence. Even a single character difference at position 1 invalidates the entire cache match for that request.

## Key Takeaways

- Prefix caching stores KV tensors for shared prompt prefixes and reuses them across requests — eliminating redundant prefill computation entirely for cached tokens.
- A trie (radix tree) structure enables efficient longest-prefix matching: each node stores KV tensors for a token sequence prefix, with LRU eviction for memory management.
- vLLM enables prefix caching with a single flag: LLM(enable_prefix_caching=True); no other code changes are required.
- Anthropic and OpenAI APIs expose prompt caching explicitly — mark stable content blocks with cache_control; cached tokens cost ~10% of normal input token price.
- For maximum hit rate, always place stable content (system prompt, RAG context) before dynamic content (user query) in your prompt structure.
- On-device inference can persist KV caches to disk between sessions using session files (llama.cpp) to skip system prompt prefill on warm starts.
- Cache hit rate of 80–90% is achievable for chatbot workloads with a fixed system prompt; RAG with a fixed document set can achieve 85–95%.

---

