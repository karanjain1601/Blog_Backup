---
title: "Prefix Language Modeling — T5 Span Corruption and Mixed Training Objectives"
slug: "prefix-language-modeling"
description: "Prefix LM combines bidirectional attention over a prefix with causal autoregressive generation for the continuation; T5 implements this via span corruption with sentinel tokens and a unified text-to-text format that casts every NLP task as sequence-to-sequence generation."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJlZml4IExhbmd1YWdlIE1vZGVsaW5nIHNpdHMgYmV0d2VlbiBDTE0gYW5kIE1MTTogYSBwcmVmaXggKGlucHV0IHByb21wdCkgaXMgcHJvY2Vzc2VkIHdpdGggZnVsbCBiaWRpcmVjdGlvbmFsIGF0dGVudGlvbiBzbyBldmVyeSBwcmVmaXggdG9rZW4gY2FuIGF0dGVuZCB0byBldmVyeSBvdGhlciBwcmVmaXggdG9rZW4sIHRoZW4gdGhlIGNvbnRpbnVhdGlvbiBpcyBnZW5lcmF0ZWQgYXV0b3JlZ3Jlc3NpdmVseSB3aXRoIGNhdXNhbCBhdHRlbnRpb24uIFRoaXMgYXJjaGl0ZWN0dXJlIG5hdHVyYWxseSBzdWl0cyBjb25kaXRpb25hbCBnZW5lcmF0aW9uIOKAlCB0aGUgZW5jb2Rlci1saWtlIHByZWZpeCB1bmRlcnN0YW5kaW5nIGVuYWJsZXMgcmljaCBjb25kaXRpb25pbmcsIHdoaWxlIHRoZSBkZWNvZGVyLWxpa2UgY29udGludWF0aW9uIGVuYWJsZXMgZ2VuZXJhdGl2ZSBmbGV4aWJpbGl0eS4gVDUgKFJhZmZlbCBldCBhbC4sIDIwMjApIG9wZXJhdGlvbmFsaXNlcyB0aGlzIHdpdGggc3BhbiBjb3JydXB0aW9uOiByZXBsYWNlIHJhbmRvbSAxNSUgdGV4dCBzcGFucyB3aXRoIHNlbnRpbmVsIHRva2VucyAoXHUwMDNjZXh0cmFfaWRfMFx1MDAzZSwgXHUwMDNjZXh0cmFfaWRfMVx1MDAzZSwg4oCmKSBhbmQgdHJhaW4gdGhlIG1vZGVsIHRvIHByZWRpY3QgdGhlIGRyb3BwZWQgc3BhbnMuIEFsbCB0YXNrcyDigJQgY2xhc3NpZmljYXRpb24sIHN1bW1hcmlzYXRpb24sIHRyYW5zbGF0aW9uLCBRQSDigJQgYXJlIGNhc3QgYXMgdGV4dC10by10ZXh0IHBhaXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlQ1IFNwYW4gQ29ycnVwdGlvbiBPYmplY3RpdmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlQ1XHUwMDI3cyBwcmV0cmFpbmluZyBvYmplY3RpdmUgY29ycnVwdHMgdGhlIGlucHV0IGJ5IHJlbW92aW5nIGNvbnRpZ3VvdXMgc3BhbnMgb2YgdG9rZW5zIGFuZCByZXBsYWNpbmcgZWFjaCBzcGFuIHdpdGggYSB1bmlxdWUgc2VudGluZWwgdG9rZW4uIFRoZSB0YXJnZXQgc2VxdWVuY2UgY29uc2lzdHMgb2YgdGhvc2Ugc2VudGluZWxzIGVhY2ggZm9sbG93ZWQgYnkgdGhlIG9yaWdpbmFsIHRva2VucyBvZiB0aGUgY29ycmVzcG9uZGluZyBzcGFuLCB0ZXJtaW5hdGVkIGJ5IGEgZmluYWwgc2VudGluZWwgYW5kIEVPUy4gU3BhbiBsZW5ndGhzIGFyZSBzYW1wbGVkIGZyb20gYSBnZW9tZXRyaWMgZGlzdHJpYnV0aW9uIHdpdGggYSBtZWFuIG9mIDMgdG9rZW5zLCBnaXZpbmcgYSBtaXggb2Ygc2hvcnQgKDHigJMyIHRva2VuKSBhbmQgb2NjYXNpb25hbGx5IGxvbmcgKDXigJMxMCB0b2tlbikgc3BhbnMuIEJlY2F1c2Ugc3BhbnMgdHlwaWNhbGx5IGNvbnRhaW4gMyB0b2tlbnMgYnV0IGFyZSByZXBsYWNlZCBieSBhIHNpbmdsZSBzZW50aW5lbCwgdGhlIGlucHV0IHNlcXVlbmNlIGlzIH4xMCUgc2hvcnRlciB0aGFuIHRoZSBvcmlnaW5hbCBhbmQgdGhlIHRhcmdldCBpcyB+M+KAkzTDlyBzaG9ydGVyIHRoYW4gdGhlIG9yaWdpbmFsIGRyb3BwZWQgdG9rZW5zIOKAlCBtYWtpbmcgYm90aCBlbmNvZGVyIGFuZCBkZWNvZGVyIHBhc3NlcyBjb21wdXRhdGlvbmFsbHkgY2hlYXAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHJhbmRvbVxuaW1wb3J0IG1hdGhcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBUNVRva2VuaXplclxuXG5kZWYgdDVfc3Bhbl9jb3JydXB0aW9uKHRva2VucywgdG9rZW5pemVyLCBub2lzZV9kZW5zaXR5PTAuMTUsIG1lYW5fc3Bhbj0zLjApOlxuICAgIFwiXCJcIlQ1IHNwYW4gY29ycnVwdGlvbjogcmVwbGFjZSByYW5kb20gc3BhbnMgd2l0aCBcdTAwM2NleHRyYV9pZF9OXHUwMDNlIHNlbnRpbmVsIHRva2Vucy5cIlwiXCJcbiAgICBuICAgICAgICAgPSBsZW4odG9rZW5zKVxuICAgIG51bV9ub2lzZSA9IG1heCgxLCBpbnQobiAqIG5vaXNlX2RlbnNpdHkpKVxuICAgIHNwYW5zLCB0b3RhbCA9IFtdLCAwXG4gICAgd2hpbGUgdG90YWwgXHUwMDNjIG51bV9ub2lzZTpcbiAgICAgICAgbGVuZ3RoID0gbWF4KDEsIG1pbihpbnQoLW1lYW5fc3BhbiAqIG1hdGgubG9nKG1heChyYW5kb20ucmFuZG9tKCksIDFlLTkpKSksIG4gLy8gNCkpXG4gICAgICAgIHNwYW5zLmFwcGVuZChsZW5ndGgpXG4gICAgICAgIHRvdGFsICs9IGxlbmd0aFxuICAgIG1heF9zdGFydCA9IG1heCgxLCBuIC0gbWF4KHNwYW5zKSlcbiAgICBzdGFydHMgICAgPSBzb3J0ZWQocmFuZG9tLnNhbXBsZShyYW5nZShtYXhfc3RhcnQpLCBtaW4obGVuKHNwYW5zKSwgbWF4X3N0YXJ0KSkpXG4gICAgc2VudGluZWxfYmFzZSA9IHRva2VuaXplci5jb252ZXJ0X3Rva2Vuc190b19pZHMoXCJcdTAwM2NleHRyYV9pZF8wXHUwMDNlXCIpXG4gICAgaW5wLCB0Z3QsIHBvcyA9IFtdLCBbXSwgMFxuICAgIGZvciBpZHgsIChzdGFydCwgbGVuZ3RoKSBpbiBlbnVtZXJhdGUoemlwKHN0YXJ0cywgc3BhbnMpKTpcbiAgICAgICAgZW5kID0gbWluKHN0YXJ0ICsgbGVuZ3RoLCBuKVxuICAgICAgICBpbnAuZXh0ZW5kKHRva2Vuc1twb3M6c3RhcnRdKSAgICAgICAgICAjIGtlZXAgbm9uLWNvcnJ1cHRlZCB0b2tlbnNcbiAgICAgICAgaW5wLmFwcGVuZChzZW50aW5lbF9iYXNlIC0gaWR4KSAgICAgICAgIyBcdTAwM2NleHRyYV9pZF9pZHhcdTAwM2UgcmVwbGFjZXMgc3BhblxuICAgICAgICB0Z3QuYXBwZW5kKHNlbnRpbmVsX2Jhc2UgLSBpZHgpICAgICAgICAjIHRhcmdldDogc2VudGluZWwgdGhlbiBvcmlnaW5hbCB0b2tlbnNcbiAgICAgICAgdGd0LmV4dGVuZCh0b2tlbnNbc3RhcnQ6ZW5kXSlcbiAgICAgICAgcG9zID0gZW5kXG4gICAgaW5wLmV4dGVuZCh0b2tlbnNbcG9zOl0pXG4gICAgdGd0LmFwcGVuZCh0b2tlbml6ZXIuZW9zX3Rva2VuX2lkKVxuICAgIHJldHVybiB0b3JjaC50ZW5zb3IoaW5wLCBkdHlwZT10b3JjaC5sb25nKSwgdG9yY2gudGVuc29yKHRndCwgZHR5cGU9dG9yY2gubG9uZylcblxudG9rZW5pemVyID0gVDVUb2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFwidDUtc21hbGxcIilcbnRleHQgICA9IFwiUHJldHJhaW5pbmcgb2JqZWN0aXZlcyBkZXRlcm1pbmUgaG93IHdlbGwgYSBsYW5ndWFnZSBtb2RlbCBnZW5lcmFsaXplcyB0byBuZXcgdGFza3NcIlxudG9rZW5zID0gdG9rZW5pemVyLmVuY29kZSh0ZXh0KVs6LTFdXG5pbnAsIHRndCA9IHQ1X3NwYW5fY29ycnVwdGlvbih0b2tlbnMsIHRva2VuaXplcilcbnByaW50KGZcIk9yaWdpbmFsOiB7bGVuKHRva2Vucyl9IHwgSW5wdXQ6IHtsZW4oaW5wKX0gfCBUYXJnZXQ6IHtsZW4odGd0KX1cIilcbnByaW50KFwiSW5wdXQgOlwiLCB0b2tlbml6ZXIuZGVjb2RlKGlucCkpXG5wcmludChcIlRhcmdldDpcIiwgdG9rZW5pemVyLmRlY29kZSh0Z3QpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZWZpeCBMTSBBdHRlbnRpb24gTWFzayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHByZWZpeCBMTSBhdHRlbnRpb24gcGF0dGVybiBpcyBhIGh5YnJpZDogcHJlZml4IHRva2VucyBmb3JtIGEgZnVsbHkgY29ubmVjdGVkIChiaWRpcmVjdGlvbmFsKSBibG9jayDigJQgZXZlcnkgcHJlZml4IHRva2VuIGNhbiBhdHRlbmQgdG8gZXZlcnkgb3RoZXIgcHJlZml4IHRva2VuIGluIGJvdGggZGlyZWN0aW9ucy4gQ29udGludWF0aW9uIHRva2VucyBmb3JtIGEgY2F1c2FsIGJsb2NrIOKAlCBlYWNoIGNvbnRpbnVhdGlvbiB0b2tlbiBjYW4gYXR0ZW5kIHRvIGFsbCBwcmVmaXggdG9rZW5zIGFuZCBhbGwgcHJpb3IgY29udGludWF0aW9uIHRva2VucyBidXQgbm90IGZ1dHVyZSBvbmVzLiBJbiBhbiBlbmNvZGVyLWRlY29kZXIgbW9kZWwgbGlrZSBUNSB0aGlzIGlzIGltcGxlbWVudGVkIG5hdHVyYWxseSBieSB0aGUgY3Jvc3MtYXR0ZW50aW9uIG1lY2hhbmlzbTogdGhlIGVuY29kZXIgY29tcHV0ZXMgZnVsbHkgYmlkaXJlY3Rpb25hbCByZXByZXNlbnRhdGlvbnMgb2YgdGhlIGNvcnJ1cHRlZCBpbnB1dCAodGhlIHByZWZpeCksIGFuZCB0aGUgZGVjb2RlciBhdHRlbmRzIHRvIHRob3NlIHJlcHJlc2VudGF0aW9ucyB2aWEgY3Jvc3MtYXR0ZW50aW9uIHdoaWxlIGFwcGx5aW5nIGEgY2F1c2FsIHNlbGYtYXR0ZW50aW9uIG1hc2sgb3ZlciB0aGUgZ2VuZXJhdGVkIHRva2VucyBzbyBmYXIuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG1hdGhcblxuZGVmIGJ1aWxkX3ByZWZpeF9sbV9tYXNrKHNlcV9sZW4sIHByZWZpeF9sZW4sIGRldmljZT1cImNwdVwiKTpcbiAgICBcIlwiXCJQcmVmaXggTE0gbWFzazogcHJlZml4IGJpZGlyZWN0aW9uYWwsIGNvbnRpbnVhdGlvbiBjYXVzYWwuXG4gICAgUmV0dXJucyAoc2VxX2xlbiwgc2VxX2xlbikgYm9vbCB0ZW5zb3I7IFRydWUgPSBhbGxvd2VkIHRvIGF0dGVuZC5cIlwiXCJcbiAgICBtYXNrID0gdG9yY2guemVyb3Moc2VxX2xlbiwgc2VxX2xlbiwgZHR5cGU9dG9yY2guYm9vbCwgZGV2aWNlPWRldmljZSlcbiAgICBtYXNrWzpwcmVmaXhfbGVuLCA6cHJlZml4X2xlbl0gPSBUcnVlICAgIyBwcmVmaXggYXR0ZW5kcyB0byBhbGwgcHJlZml4XG4gICAgZm9yIGkgaW4gcmFuZ2UocHJlZml4X2xlbiwgc2VxX2xlbik6XG4gICAgICAgIG1hc2tbaSwgOmkgKyAxXSA9IFRydWUgICAgICAgICAgICAgIyBjb250aW51YXRpb246IGNhdXNhbCB3aW5kb3dcbiAgICByZXR1cm4gbWFza1xuXG5kZWYgc2NhbGVkX2RvdF9wcm9kdWN0X3ByZWZpeF9sbShRLCBLLCBWLCBwcmVmaXhfbGVuKTpcbiAgICBcIlwiXCJBdHRlbnRpb24gd2l0aCBwcmVmaXggTE0gbWFzayBhcHBsaWVkIGluIGEgc2luZ2xlIGNhbGwuXCJcIlwiXG4gICAgc2VxX2xlbiA9IFEuc2l6ZSgtMilcbiAgICBkX2sgICAgID0gUS5zaXplKC0xKVxuICAgIHNjb3JlcyAgPSB0b3JjaC5tYXRtdWwoUSwgSy50cmFuc3Bvc2UoLTIsIC0xKSkgLyBtYXRoLnNxcnQoZF9rKVxuICAgIG1hc2sgICAgPSBidWlsZF9wcmVmaXhfbG1fbWFzayhzZXFfbGVuLCBwcmVmaXhfbGVuLCBRLmRldmljZSlcbiAgICBzY29yZXMgID0gc2NvcmVzLm1hc2tlZF9maWxsKH5tYXNrLCBmbG9hdChcIi1pbmZcIikpXG4gICAgd2VpZ2h0cyA9IHRvcmNoLnNvZnRtYXgoc2NvcmVzLCBkaW09LTEpXG4gICAgcmV0dXJuIHRvcmNoLm1hdG11bCh3ZWlnaHRzLCBWKSwgd2VpZ2h0c1xuXG5zZXFfbGVuLCBwcmVmaXhfbGVuLCBkX2sgPSAxMiwgNSwgNjRcblEgPSB0b3JjaC5yYW5kbigxLCBzZXFfbGVuLCBkX2spXG5LID0gdG9yY2gucmFuZG4oMSwgc2VxX2xlbiwgZF9rKVxuViA9IHRvcmNoLnJhbmRuKDEsIHNlcV9sZW4sIGRfaylcbm91dCwgYXR0biA9IHNjYWxlZF9kb3RfcHJvZHVjdF9wcmVmaXhfbG0oUSwgSywgViwgcHJlZml4X2xlbilcbm1hc2sgPSBidWlsZF9wcmVmaXhfbG1fbWFzayhzZXFfbGVuLCBwcmVmaXhfbGVuKVxucHJpbnQoZlwiUHJlZml4ICh7cHJlZml4X2xlbn0gdG9rZW5zKTogYXR0ZW5kIHRvIHttYXNrWzpwcmVmaXhfbGVuLDpwcmVmaXhfbGVuXS5zdW0oMSkuZmxvYXQoKS5tZWFuKCk6LjBmfSB0b2tlbnMgYXZnIChmdWxsIHByZWZpeClcIilcbnByaW50KGZcIkNvbnRpbnVhdGlvbiAoe3NlcV9sZW4tcHJlZml4X2xlbn0gdG9rZW5zKTogY2F1c2FsIOKAlCBwcmVmaXggKyBwcmlvciB0b2tlbnMgb25seVwiKVxucHJpbnQoZlwiT3V0cHV0IHNoYXBlOiB7b3V0LnNoYXBlfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRleHQtdG8tVGV4dCBUYXNrIEZvcm1hdHRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlQ1XHUwMDI3cyBtb3N0IGluZmx1ZW50aWFsIGRlc2lnbiBkZWNpc2lvbiBpcyB0aGUgdGV4dC10by10ZXh0IGZvcm1hdDogZXZlcnkgTkxQIHRhc2sgaXMgZXhwcmVzc2VkIGFzIGEgbWFwcGluZyBmcm9tIGFuIGlucHV0IHRleHQgc3RyaW5nIHRvIGFuIG91dHB1dCB0ZXh0IHN0cmluZy4gQ2xhc3NpZmljYXRpb24gYmVjb21lcyBzdHJpbmcgb3V0cHV0IChcdTAwMjdwb3NpdGl2ZVx1MDAyNywgXHUwMDI3bmVnYXRpdmVcdTAwMjcsIFx1MDAyN25ldXRyYWxcdTAwMjcpOyByZWdyZXNzaW9uIGJlY29tZXMgYSBudW1lcmljIHN0cmluZzsgdHJhbnNsYXRpb24gaXMgc2VsZi1ldmlkZW50OyBRQSBtYXBzIFx1MDAyN3F1ZXN0aW9uOiAuLi4gY29udGV4dDogLi4uXHUwMDI3IHRvIGFuIGFuc3dlciBzdHJpbmcuIEEgdGFzay1zcGVjaWZpYyBwcmVmaXggKGUuZy4gXHUwMDI3c3N0MiBzZW50ZW5jZTpcdTAwMjcsIFx1MDAyN3N1bW1hcml6ZTpcdTAwMjcsIFx1MDAyN3RyYW5zbGF0ZSBFbmdsaXNoIHRvIEdlcm1hbjpcdTAwMjcpIHJvdXRlcyB0aGUgbW9kZWwgdG8gdGhlIGFwcHJvcHJpYXRlIGJlaGF2aW91ci4gVGhpcyB1bmlmaWNhdGlvbiBtZWFucyBhIHNpbmdsZSBtb2RlbCBjYW4gaGFuZGxlIGRvemVucyBvZiB0YXNrcyB3aXRoIG5vIGFyY2hpdGVjdHVyZSBjaGFuZ2VzLCBvbmx5IHByb21wdCBjaGFuZ2VzIOKAlCB0aGUgcHJlY3Vyc29yIHRvIG1vZGVybiBpbnN0cnVjdGlvbi10dW5lZCBtb2RlbHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBUNVRva2VuaXplclxuXG5UQVNLX1RFTVBMQVRFUyA9IHtcbiAgICBcImNsYXNzaWZpY2F0aW9uXCI6IChcInNzdDIgc2VudGVuY2U6IHt0ZXh0fVwiLCBcIntsYWJlbH1cIiksXG4gICAgXCJzdW1tYXJpemF0aW9uXCI6ICAoXCJzdW1tYXJpemU6IHt0ZXh0fVwiLCBcIntzdW1tYXJ5fVwiKSxcbiAgICBcInRyYW5zbGF0aW9uXCI6ICAgIChcInRyYW5zbGF0ZSBFbmdsaXNoIHRvIEdlcm1hbjoge3RleHR9XCIsIFwie3RyYW5zbGF0aW9ufVwiKSxcbiAgICBcIm5saVwiOiAgICAgICAgICAgIChcIm1ubGkgaHlwb3RoZXNpczoge2h5cG90aGVzaXN9IHByZW1pc2U6IHtwcmVtaXNlfVwiLCBcIntsYWJlbH1cIiksXG4gICAgXCJxYVwiOiAgICAgICAgICAgICAoXCJxdWVzdGlvbjoge3F1ZXN0aW9ufSBjb250ZXh0OiB7Y29udGV4dH1cIiwgXCJ7YW5zd2VyfVwiKSxcbn1cblxuZGVmIGZvcm1hdF90ZXh0X3RvX3RleHQodGFzaywgKiprd2FyZ3MpOlxuICAgIHRtcGxfaW4sIHRtcGxfb3V0ID0gVEFTS19URU1QTEFURVNbdGFza11cbiAgICByZXR1cm4gdG1wbF9pbi5mb3JtYXQoKiprd2FyZ3MpLCB0bXBsX291dC5mb3JtYXQoKiprd2FyZ3MpXG5cbnRva2VuaXplciA9IFQ1VG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcInQ1LXNtYWxsXCIpXG5leGFtcGxlcyAgPSBbXG4gICAgZm9ybWF0X3RleHRfdG9fdGV4dChcImNsYXNzaWZpY2F0aW9uXCIsIHRleHQ9XCJUaGUgZmlsbSB3YXMgYnJlYXRodGFraW5nLlwiLCBsYWJlbD1cInBvc2l0aXZlXCIpLFxuICAgIGZvcm1hdF90ZXh0X3RvX3RleHQoXCJ0cmFuc2xhdGlvblwiLCB0ZXh0PVwiRGVlcCBsZWFybmluZyBpcyBwb3dlcmZ1bC5cIiwgdHJhbnNsYXRpb249XCJEZWVwIExlYXJuaW5nIGlzdCBtYWNodHZvbGwuXCIpLFxuICAgIGZvcm1hdF90ZXh0X3RvX3RleHQoXCJxYVwiLCBxdWVzdGlvbj1cIldoYXQgaXMgVDU/XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICBjb250ZXh0PVwiVDUgaXMgYSB0ZXh0LXRvLXRleHQgdHJhbnNmZXIgdHJhbnNmb3JtZXIuXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICBhbnN3ZXI9XCJ0ZXh0LXRvLXRleHQgdHJhbnNmZXIgdHJhbnNmb3JtZXJcIiksXG4gICAgZm9ybWF0X3RleHRfdG9fdGV4dChcInN1bW1hcml6YXRpb25cIixcbiAgICAgICAgICAgICAgICAgICAgICAgIHRleHQ9XCJUNSBjb252ZXJ0cyBldmVyeSBOTFAgdGFzayBpbnRvIHRleHQtdG8tdGV4dCBmb3JtYXQgdXNpbmcgYW4gZW5jb2Rlci1kZWNvZGVyLlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgc3VtbWFyeT1cIlQ1IHVuaWZpZXMgTkxQIHRhc2tzIGFzIHRleHQtdG8tdGV4dC5cIiksXG5dXG5mb3IgaW5wLCB0Z3QgaW4gZXhhbXBsZXM6XG4gICAgZW5jX2luICA9IHRva2VuaXplci5lbmNvZGUoaW5wKVxuICAgIGVuY190Z3QgPSB0b2tlbml6ZXIuZW5jb2RlKHRndClcbiAgICBwcmludChmXCJbe2xlbihlbmNfaW4pOjNkfSBpbiB8IHtsZW4oZW5jX3RndCk6MmR9IHRndF0ge2lucFs6NTVdfS4uLlwiKVxuICAgIHByaW50KGZcIiAgVGFyZ2V0OiB7dGd0fVxcblwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJUNSBTcGFuIENvcnJ1cHRpb24gdnMgV29yZC1MZXZlbCBNYXNraW5nIiwiY29udGVudCI6IlQ1XHUwMDI3cyBzcGFuIGNvcnJ1cHRpb24gY3JlYXRlcyAzLjR4IHNob3J0ZXIgdGFyZ2V0IHNlcXVlbmNlcyB0aGFuIFNwYW5CRVJUXHUwMDI3cyB3b3JkLWxldmVsIG1hc2tpbmcgZm9yIHRoZSBzYW1lIDE1JSBtYXNraW5nIHJhdGUg4oCUIHRoaXMgc2lnbmlmaWNhbnRseSByZWR1Y2VzIGRlY29kZXIgY29tcHV0ZSBkdXJpbmcgcHJldHJhaW5pbmcgd2hpbGUgbWFpbnRhaW5pbmcgc3Bhbi1sZXZlbCBjb250ZXh0IHJlY292ZXJ5LiBBIG1lYW4gc3BhbiBvZiAzIHRva2VucyBtZWFucyBvbmUgc2VudGluZWwgcmVwbGFjZXMgMyB0b2tlbnMgaW4gdGhlIGlucHV0LCBjb21wcmVzc2luZyB0aGUgdGFyZ2V0IHRvIHJvdWdobHkgMS8zIG9mIHRoZSBkcm9wcGVkLXRva2VuIGNvdW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZMQU4tVDUgWmVyby1TaG90IEluZmVyZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRkxBTi1UNSAoV2VpIGV0IGFsLiAyMDIyLCBDaHVuZyBldCBhbC4gMjAyMikgZmluZS10dW5lcyBUNSBvbiBhIG1hc3NpdmUgbWl4dHVyZSBvZiBpbnN0cnVjdGlvbi1mb3JtYXR0ZWQgdGFza3Mg4oCUIG92ZXIgMTgwMCB0YXNrcyBwaHJhc2VkIGFzIG5hdHVyYWwgbGFuZ3VhZ2UgaW5zdHJ1Y3Rpb25zIGFjcm9zcyBtdWx0aXBsZSBiZW5jaG1hcmtzLiBUaGlzIGluc3RydWN0aW9uIHR1bmluZyBkcmFtYXRpY2FsbHkgaW1wcm92ZXMgemVyby1zaG90IGFuZCBmZXctc2hvdCBwZXJmb3JtYW5jZTogdGhlIG1vZGVsIGxlYXJucyB0byBmb2xsb3cgZnJlZS1mb3JtIGluc3RydWN0aW9ucyByYXRoZXIgdGhhbiBvbmx5IHRhc2stc3BlY2lmaWMgcHJlZml4ZXMuIEZMQU4tVDUtWFhMICgxMUIgcGFyYW1ldGVycykgbWF0Y2hlcyBvciBleGNlZWRzIEdQVC0zICgxNzVCKSBvbiBtYW55IGJlbmNobWFya3MsIGRlbW9uc3RyYXRpbmcgdGhhdCBpbnN0cnVjdGlvbiBkaXZlcnNpdHkgbWF0dGVycyBtb3JlIHRoYW4gcmF3IHNjYWxlIGZvciB6ZXJvLXNob3QgZ2VuZXJhbGlzYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IFQ1Rm9yQ29uZGl0aW9uYWxHZW5lcmF0aW9uLCBUNVRva2VuaXplclxuXG5kZXZpY2UgICAgPSBcImN1ZGFcIiBpZiB0b3JjaC5jdWRhLmlzX2F2YWlsYWJsZSgpIGVsc2UgXCJjcHVcIlxubW9kZWwgICAgID0gVDVGb3JDb25kaXRpb25hbEdlbmVyYXRpb24uZnJvbV9wcmV0cmFpbmVkKFwiZ29vZ2xlL2ZsYW4tdDUtYmFzZVwiKS50byhkZXZpY2UpXG50b2tlbml6ZXIgPSBUNVRva2VuaXplci5mcm9tX3ByZXRyYWluZWQoXCJnb29nbGUvZmxhbi10NS1iYXNlXCIpXG5tb2RlbC5ldmFsKClcblxuZGVmIGZsYW5fdDVfcHJlZGljdChwcm9tcHQsIG1heF9uZXdfdG9rZW5zPTY0LCBudW1fYmVhbXM9NCk6XG4gICAgXCJcIlwiWmVyby1zaG90IEZMQU4tVDUgaW5mZXJlbmNlIGZvciBhcmJpdHJhcnkgaW5zdHJ1Y3Rpb24tZm9ybWF0dGVkIHRhc2tzLlwiXCJcIlxuICAgIGlucHV0cyA9IHRva2VuaXplcihwcm9tcHQsIHJldHVybl90ZW5zb3JzPVwicHRcIiwgdHJ1bmNhdGlvbj1UcnVlLFxuICAgICAgICAgICAgICAgICAgICAgICBtYXhfbGVuZ3RoPTUxMikudG8oZGV2aWNlKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBvdXQgPSBtb2RlbC5nZW5lcmF0ZSgqKmlucHV0cywgbWF4X25ld190b2tlbnM9bWF4X25ld190b2tlbnMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIG51bV9iZWFtcz1udW1fYmVhbXMsIGVhcmx5X3N0b3BwaW5nPVRydWUpXG4gICAgcmV0dXJuIHRva2VuaXplci5kZWNvZGUob3V0WzBdLCBza2lwX3NwZWNpYWxfdG9rZW5zPVRydWUpXG5cbnByb21wdHMgPSBbXG4gICAgXCJDbGFzc2lmeSBzZW50aW1lbnQgKHBvc2l0aXZlL25lZ2F0aXZlKTogXHUwMDI3VGhpcyBsZWN0dXJlIG9uIHRyYW5zZm9ybWVycyB3YXMgb3V0c3RhbmRpbmchXHUwMDI3XCIsXG4gICAgXCJUcmFuc2xhdGUgdG8gRnJlbmNoOiBcdTAwMjdUaGUgcXVpY2sgYnJvd24gZm94IGp1bXBzIG92ZXIgdGhlIGxhenkgZG9nLlx1MDAyN1wiLFxuICAgIFwiQW5zd2VyOiBXaGF0IHByZXRyYWluaW5nIG9iamVjdGl2ZSBkb2VzIFQ1IHVzZT8gQ29udGV4dDogVDUgdXNlcyBzcGFuIGNvcnJ1cHRpb24uXCIsXG5dXG5mb3IgcHJvbXB0IGluIHByb21wdHM6XG4gICAgYW5zd2VyID0gZmxhbl90NV9wcmVkaWN0KHByb21wdClcbiAgICBwcmludChmXCJROiB7cHJvbXB0Wzo2MF19Li4uXCIpXG4gICAgcHJpbnQoZlwiQToge2Fuc3dlcn1cXG5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIG9mIFByZXRyYWluaW5nIE9iamVjdGl2ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0aHJlZSBwYXJhZGlnbXMg4oCUIENMTSwgTUxNLCBhbmQgUHJlZml4IExNIC8gRW5jb2Rlci1EZWNvZGVyIOKAlCByZXByZXNlbnQgZnVuZGFtZW50YWwgdHJhZGUtb2ZmcyBiZXR3ZWVuIGdlbmVyYXRpb24gY2FwYWJpbGl0eSwgcmVwcmVzZW50YXRpb24gcmljaG5lc3MsIGFuZCBjb21wdXRlIGVmZmljaWVuY3kuIENMTSBpcyB0aGUgc2ltcGxlc3QgYW5kIG1vc3Qgc2FtcGxlLWVmZmljaWVudCwgbWFraW5nIGl0IGRvbWluYW50IGZvciBsYXJnZS1zY2FsZSBwcmV0cmFpbmluZy4gTUxNIHByb2R1Y2VzIHRoZSByaWNoZXN0IHRva2VuLWxldmVsIHJlcHJlc2VudGF0aW9ucyBmb3IgdW5kZXJzdGFuZGluZyBidXQgY2Fubm90IGdlbmVyYXRlLiBQcmVmaXggTE0gLyBFbmNvZGVyLURlY29kZXIgaXMgdGhlIG1vc3QgcG93ZXJmdWwgZm9yIGNvbmRpdGlvbmFsIGdlbmVyYXRpb24gdGFza3MgYnV0IHJlcXVpcmVzIHBhaXJlZCBpbnB1dC1vdXRwdXQgZGF0YSBmb3IgdGFzayBmb3JtYXR0aW5nIGFuZCBpcyBtb3JlIGV4cGVuc2l2ZSB0byB0cmFpbiAodHdvIGNvbXBvbmVudHMpLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJBc3BlY3QiLCJDTE0iLCJNTE0iLCJQcmVmaXggTE0iLCJFbmNvZGVyLURlY29kZXIiXSwicm93cyI6W1siQXR0ZW50aW9uIHR5cGUiLCJDYXVzYWwgKGxlZnQtdG8tcmlnaHQpIiwiQmlkaXJlY3Rpb25hbCAoZnVsbCkiLCJCaWRpciBwcmVmaXggKyBjYXVzYWwgY29udGludWF0aW9uIiwiRW5jb2RlcjogZnVsbDsgRGVjb2RlcjogY2F1c2FsIl0sWyJUcmFpbmluZyB0YXJnZXQiLCJBbGwgTiB0b2tlbnMgKHNoaWZ0ZWQpIiwifjE1JSBtYXNrZWQgdG9rZW5zIiwiRHJvcHBlZCBzcGFuIHRva2VucyArIHNlbnRpbmVscyIsIlRhcmdldCBzZXF1ZW5jZSB0b2tlbnMiXSxbIkdlbmVyYXRpb24iLCJOYXRpdmUgYXV0b3JlZ3Jlc3NpdmUiLCJOb3QgbmF0aXZlIOKAlCBuZWVkcyBzZXBhcmF0ZSBkZWNvZGVyIiwiTmF0aXZlIGNvbnRpbnVhdGlvbiBvZiBwcmVmaXgiLCJOYXRpdmUgdmlhIGNyb3NzLWF0dGVudGlvbiBkZWNvZGluZyJdLFsiU2FtcGxlIGVmZmljaWVuY3kiLCJIaWdoIOKAlCBOIHRhcmdldHMvc2VxIiwiTG93IOKAlCB+MC4xNU4gdGFyZ2V0cy9zZXEiLCJNZWRpdW0g4oCUIGRlcGVuZHMgb24gc3BhbiBkZW5zaXR5IiwiRGVwZW5kcyBvbiBwYWlyZWQgZGF0YSBxdWFsaXR5Il0sWyJLZXkgbW9kZWxzIiwiR1BULCBMTGFNQSwgTWlzdHJhbCIsIkJFUlQsIFJvQkVSVGEsIERlQkVSVGEiLCJQYUxNIChzdWZmaXggcHJlZGljdGlvbikiLCJUNSwgRkxBTi1UNSwgQkFSVCwgbVQ1Il1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVTDIg4oCUIE1peHR1cmUgb2YgT2JqZWN0aXZlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVUwyIChUYXkgZXQgYWwuIDIwMjIpIHByb3Bvc2VzIHRyYWluaW5nIGEgc2luZ2xlIG1vZGVsIHdpdGggYSBtaXh0dXJlIG9mIGRlbm9pc2luZyBvYmplY3RpdmVzLCBjYWxsaW5nIGl0IE1peHR1cmUtb2YtRGVub2lzZXJzIChNb0QpLiBUaHJlZSBvYmplY3RpdmUgZmFtaWxpZXMgYXJlIG1peGVkOiBSLWRlbm9pc2VycyAoQ0xNLWxpa2U6IHByZWRpY3QgYSBzdWZmaXgpLCBTLWRlbm9pc2VycyAoc3BhbiBjb3JydXB0aW9uIGxpa2UgVDUgd2l0aCBzaG9ydCBzcGFucyksIGFuZCBYLWRlbm9pc2VycyAoZXh0cmVtZSBzcGFuIGNvcnJ1cHRpb24gd2l0aCB2ZXJ5IGxvbmcgc3BhbnMgb3IgaGlnaCBtYXNraW5nIHJhdGVzKS4gQSBtb2RlIHRva2VuIChbUl0sIFtTXSwgW1hdKSBwcmVwZW5kZWQgdG8gdGhlIGlucHV0IHRlbGxzIHRoZSBtb2RlbCB3aGljaCBkZW5vaXNpbmcgcmVnaW1lIGFwcGxpZXMuIFVMMi0yMEIgb3V0cGVyZm9ybXMgR1BULTMgMTc1QiBvbiBtYW55IGJlbmNobWFya3MsIHNob3dpbmcgdGhhdCBvYmplY3RpdmUgZGl2ZXJzaXR5IGR1cmluZyBwcmV0cmFpbmluZyBpcyBhIG1vcmUgZWZmaWNpZW50IHVzZSBvZiBjb21wdXRlIHRoYW4gc2NhbGluZyBhIHNpbmdsZSBvYmplY3RpdmUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJSLWRlbm9pc2VyOiBwcmVkaWN0IHN1ZmZpeCBmcm9tIHByZWZpeCDigJQgaWRlbnRpY2FsIHRvIENMTSwgZW5jb3VyYWdlcyBsZWZ0LXRvLXJpZ2h0IGdlbmVyYXRpb24uIiwiUy1kZW5vaXNlcjogVDUtc3R5bGUgc3BhbiBjb3JydXB0aW9uIHdpdGggc2hvcnQgc3BhbnMgKG1lYW4gMyB0b2tlbnMsIDE1JSByYXRlKSDigJQgc3RhbmRhcmQgc2VxMnNlcS4iLCJYLWRlbm9pc2VyOiBleHRyZW1lIGNvcnJ1cHRpb24g4oCUIHZlcnkgbG9uZyBzcGFucyAobWVhbiAzMiB0b2tlbnMpIG9yIGhpZ2ggcmF0ZSAoNTAlKSDigJQgZm9yY2VzIGZ1bGwgZG9jdW1lbnQgcmVjb25zdHJ1Y3Rpb24uIiwiTW9kZSB0b2tlbiAoW1JdLCBbU10sIFtYXSkgcHJlcGVuZGVkIHRvIGlucHV0IHJvdXRlcyB0aGUgbW9kZWwgdG8gdGhlIGNvcnJlY3QgZGVub2lzaW5nIGJlaGF2aW91ci4iLCJVTDIgdW5pZmllcyBHUFQtc3R5bGUgZ2VuZXJhdGlvbiBhbmQgVDUtc3R5bGUgc2VxMnNlcSBpbiBvbmUgbW9kZWwgd2l0aG91dCBhcmNoaXRlY3R1cmFsIGNoYW5nZXMuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXB1dGUgRWZmaWNpZW5jeSBvZiBQcmVmaXggTE0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcHJhY3RpY2FsIGFkdmFudGFnZSBvZiB0aGUgZW5jb2Rlci1kZWNvZGVyIGFyY2hpdGVjdHVyZSBpcyB0aGF0IHRoZSBlbmNvZGVyIGNvbXB1dGVzIHByZWZpeCByZXByZXNlbnRhdGlvbnMgb25seSBvbmNlIHBlciBnZW5lcmF0aW9uIHJlcXVlc3QuIEluIENMTSwgcmUtcHJvY2Vzc2luZyB0aGUgZW50aXJlIHByb21wdCBpcyByZXF1aXJlZCBmb3IgZWFjaCBuZXcgdG9rZW4gKG1pdGlnYXRlZCBieSBLViBjYWNoZSksIGFuZCB0aGUgcHJlZml4IHRva2VucyBjb21wZXRlIGZvciBjb250ZXh0IGxlbmd0aCB3aXRoIGdlbmVyYXRlZCB0b2tlbnMuIEluIGVuY29kZXItZGVjb2RlciBtb2RlbHMsIHRoZSBwcmVmaXggaXMgcHJvY2Vzc2VkIGJ5IHRoZSBlbmNvZGVyIGF0IGZ1bGwgYXR0ZW50aW9uIGNvbXBsZXhpdHkgb25jZSwgdGhlbiBpdHMga2V5LXZhbHVlIHJlcHJlc2VudGF0aW9ucyBhcmUgcGFzc2VkIHRvIHRoZSBkZWNvZGVyIHZpYSBjcm9zcy1hdHRlbnRpb24gZm9yIGFsbCBnZW5lcmF0aW9uIHN0ZXBzLiBUaGlzIHNlcGFyYXRpb24gbWVhbnMgdGhlIGVuY29kZXIgY2FuIHByb2Nlc3MgdmVyeSBsb25nIGNvbnRleHRzIHdpdGhvdXQgYnVyZGVuaW5nIHRoZSBkZWNvZGVyLiBUNSAxMUIgYWNoaWV2ZXMgc3Ryb25nIHBlcmZvcm1hbmNlIGFjcm9zcyBkaXZlcnNlIHRhc2tzIHdoaWxlIHJlbWFpbmluZyBtb3JlIGludGVycHJldGFibGUgdGhhbiBzYW1lLXNpemUgQ0xNIG1vZGVscyBkdWUgdG8gdGhpcyBleHBsaWNpdCBpbnB1dC1vdXRwdXQgc2VwYXJhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYUxNIGFuZCBQcmVmaXggUHJlZGljdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGFMTSAoQ2hvd2RoZXJ5IGV0IGFsLiwgMjAyMiksIGEgNTQwQiBwYXJhbWV0ZXIgZGVjb2Rlci1vbmx5IG1vZGVsLCBhbHNvIGluY29ycG9yYXRlcyBhIHByZWZpeC1zdHlsZSB0cmFpbmluZyB2YXJpYW50IGNhbGxlZCBzdWZmaXggcHJlZGljdGlvbjogYSBmcmFjdGlvbiBvZiB0cmFpbmluZyBleGFtcGxlcyBhcmUgZm9ybWF0dGVkIHNvIHRoYXQgYSByYW5kb20gc3VmZml4IG9mIHRoZSBkb2N1bWVudCBpcyBtb3ZlZCB0byB0aGUgYmVnaW5uaW5nLCBhbmQgdGhlIG1vZGVsIGxlYXJucyB0byBjb21wbGV0ZSB0aGUgZG9jdW1lbnQgZnJvbSBhIHBvc2l0aW9uIGluIHRoZSBtaWRkbGUuIFRoaXMgZXhwb3NlcyB0aGUgQ0xNLW9ubHkgbW9kZWwgdG8gYmlkaXJlY3Rpb25hbCBjb250ZXh0IGR1cmluZyBwcmV0cmFpbmluZyB3aXRob3V0IHJlcXVpcmluZyBhbiBlbmNvZGVyLiBDb21iaW5lZCB3aXRoIGNoYWluLW9mLXRob3VnaHQgcHJvbXB0aW5nLCBQYUxNIGFjaGlldmVzIGh1bWFuLWxldmVsIHBlcmZvcm1hbmNlIG9uIGEgd2lkZSByYW5nZSBvZiBtdWx0aS1zdGVwIHJlYXNvbmluZyB0YXNrcywgc3VnZ2VzdGluZyB0aGF0IHByZXRyYWluaW5nIG9iamVjdGl2ZSBkaXZlcnNpdHkg4oCUIGV2ZW4gd2l0aGluIGEgZGVjb2Rlci1vbmx5IGZyYW1ld29yayDigJQgc2lnbmlmaWNhbnRseSBpbXByb3ZlcyBnZW5lcmFsaXNhdGlvbi4ifV0="
---
# Prefix Language Modeling — T5 Span Corruption and Mixed Training Objectives

Prefix Language Modeling sits between CLM and MLM: a prefix (input prompt) is processed with full bidirectional attention so every prefix token can attend to every other prefix token, then the continuation is generated autoregressively with causal attention. This architecture naturally suits conditional generation — the encoder-like prefix understanding enables rich conditioning, while the decoder-like continuation enables generative flexibility. T5 (Raffel et al., 2020) operationalises this with span corruption: replace random 15% text spans with sentinel tokens (<extra_id_0>, <extra_id_1>, …) and train the model to predict the dropped spans. All tasks — classification, summarisation, translation, QA — are cast as text-to-text pairs.

## T5 Span Corruption Objective

T5's pretraining objective corrupts the input by removing contiguous spans of tokens and replacing each span with a unique sentinel token. The target sequence consists of those sentinels each followed by the original tokens of the corresponding span, terminated by a final sentinel and EOS. Span lengths are sampled from a geometric distribution with a mean of 3 tokens, giving a mix of short (1–2 token) and occasionally long (5–10 token) spans. Because spans typically contain 3 tokens but are replaced by a single sentinel, the input sequence is ~10% shorter than the original and the target is ~3–4× shorter than the original dropped tokens — making both encoder and decoder passes computationally cheap.

```python
import torch
import random
import math
from transformers import T5Tokenizer

def t5_span_corruption(tokens, tokenizer, noise_density=0.15, mean_span=3.0):
    """T5 span corruption: replace random spans with <extra_id_N> sentinel tokens."""
    n         = len(tokens)
    num_noise = max(1, int(n * noise_density))
    spans, total = [], 0
    while total < num_noise:
        length = max(1, min(int(-mean_span * math.log(max(random.random(), 1e-9))), n // 4))
        spans.append(length)
        total += length
    max_start = max(1, n - max(spans))
    starts    = sorted(random.sample(range(max_start), min(len(spans), max_start)))
    sentinel_base = tokenizer.convert_tokens_to_ids("<extra_id_0>")
    inp, tgt, pos = [], [], 0
    for idx, (start, length) in enumerate(zip(starts, spans)):
        end = min(start + length, n)
        inp.extend(tokens[pos:start])          # keep non-corrupted tokens
        inp.append(sentinel_base - idx)        # <extra_id_idx> replaces span
        tgt.append(sentinel_base - idx)        # target: sentinel then original tokens
        tgt.extend(tokens[start:end])
        pos = end
    inp.extend(tokens[pos:])
    tgt.append(tokenizer.eos_token_id)
    return torch.tensor(inp, dtype=torch.long), torch.tensor(tgt, dtype=torch.long)

tokenizer = T5Tokenizer.from_pretrained("t5-small")
text   = "Pretraining objectives determine how well a language model generalizes to new tasks"
tokens = tokenizer.encode(text)[:-1]
inp, tgt = t5_span_corruption(tokens, tokenizer)
print(f"Original: {len(tokens)} | Input: {len(inp)} | Target: {len(tgt)}")
print("Input :", tokenizer.decode(inp))
print("Target:", tokenizer.decode(tgt))
```

## Prefix LM Attention Mask

The prefix LM attention pattern is a hybrid: prefix tokens form a fully connected (bidirectional) block — every prefix token can attend to every other prefix token in both directions. Continuation tokens form a causal block — each continuation token can attend to all prefix tokens and all prior continuation tokens but not future ones. In an encoder-decoder model like T5 this is implemented naturally by the cross-attention mechanism: the encoder computes fully bidirectional representations of the corrupted input (the prefix), and the decoder attends to those representations via cross-attention while applying a causal self-attention mask over the generated tokens so far.

```python
import torch
import math

def build_prefix_lm_mask(seq_len, prefix_len, device="cpu"):
    """Prefix LM mask: prefix bidirectional, continuation causal.
    Returns (seq_len, seq_len) bool tensor; True = allowed to attend."""
    mask = torch.zeros(seq_len, seq_len, dtype=torch.bool, device=device)
    mask[:prefix_len, :prefix_len] = True   # prefix attends to all prefix
    for i in range(prefix_len, seq_len):
        mask[i, :i + 1] = True             # continuation: causal window
    return mask

def scaled_dot_product_prefix_lm(Q, K, V, prefix_len):
    """Attention with prefix LM mask applied in a single call."""
    seq_len = Q.size(-2)
    d_k     = Q.size(-1)
    scores  = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
    mask    = build_prefix_lm_mask(seq_len, prefix_len, Q.device)
    scores  = scores.masked_fill(~mask, float("-inf"))
    weights = torch.softmax(scores, dim=-1)
    return torch.matmul(weights, V), weights

seq_len, prefix_len, d_k = 12, 5, 64
Q = torch.randn(1, seq_len, d_k)
K = torch.randn(1, seq_len, d_k)
V = torch.randn(1, seq_len, d_k)
out, attn = scaled_dot_product_prefix_lm(Q, K, V, prefix_len)
mask = build_prefix_lm_mask(seq_len, prefix_len)
print(f"Prefix ({prefix_len} tokens): attend to {mask[:prefix_len,:prefix_len].sum(1).float().mean():.0f} tokens avg (full prefix)")
print(f"Continuation ({seq_len-prefix_len} tokens): causal — prefix + prior tokens only")
print(f"Output shape: {out.shape}")
```

## Text-to-Text Task Formatting

T5's most influential design decision is the text-to-text format: every NLP task is expressed as a mapping from an input text string to an output text string. Classification becomes string output ('positive', 'negative', 'neutral'); regression becomes a numeric string; translation is self-evident; QA maps 'question: ... context: ...' to an answer string. A task-specific prefix (e.g. 'sst2 sentence:', 'summarize:', 'translate English to German:') routes the model to the appropriate behaviour. This unification means a single model can handle dozens of tasks with no architecture changes, only prompt changes — the precursor to modern instruction-tuned models.

```python
from transformers import T5Tokenizer

TASK_TEMPLATES = {
    "classification": ("sst2 sentence: {text}", "{label}"),
    "summarization":  ("summarize: {text}", "{summary}"),
    "translation":    ("translate English to German: {text}", "{translation}"),
    "nli":            ("mnli hypothesis: {hypothesis} premise: {premise}", "{label}"),
    "qa":             ("question: {question} context: {context}", "{answer}"),
}

def format_text_to_text(task, **kwargs):
    tmpl_in, tmpl_out = TASK_TEMPLATES[task]
    return tmpl_in.format(**kwargs), tmpl_out.format(**kwargs)

tokenizer = T5Tokenizer.from_pretrained("t5-small")
examples  = [
    format_text_to_text("classification", text="The film was breathtaking.", label="positive"),
    format_text_to_text("translation", text="Deep learning is powerful.", translation="Deep Learning ist machtvoll."),
    format_text_to_text("qa", question="What is T5?",
                        context="T5 is a text-to-text transfer transformer.",
                        answer="text-to-text transfer transformer"),
    format_text_to_text("summarization",
                        text="T5 converts every NLP task into text-to-text format using an encoder-decoder.",
                        summary="T5 unifies NLP tasks as text-to-text."),
]
for inp, tgt in examples:
    enc_in  = tokenizer.encode(inp)
    enc_tgt = tokenizer.encode(tgt)
    print(f"[{len(enc_in):3d} in | {len(enc_tgt):2d} tgt] {inp[:55]}...")
    print(f"  Target: {tgt}\n")
```

> **T5 Span Corruption vs Word-Level Masking**: T5's span corruption creates 3.4x shorter target sequences than SpanBERT's word-level masking for the same 15% masking rate — this significantly reduces decoder compute during pretraining while maintaining span-level context recovery. A mean span of 3 tokens means one sentinel replaces 3 tokens in the input, compressing the target to roughly 1/3 of the dropped-token count.

## FLAN-T5 Zero-Shot Inference

FLAN-T5 (Wei et al. 2022, Chung et al. 2022) fine-tunes T5 on a massive mixture of instruction-formatted tasks — over 1800 tasks phrased as natural language instructions across multiple benchmarks. This instruction tuning dramatically improves zero-shot and few-shot performance: the model learns to follow free-form instructions rather than only task-specific prefixes. FLAN-T5-XXL (11B parameters) matches or exceeds GPT-3 (175B) on many benchmarks, demonstrating that instruction diversity matters more than raw scale for zero-shot generalisation.

```python
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

device    = "cuda" if torch.cuda.is_available() else "cpu"
model     = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base").to(device)
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model.eval()

def flan_t5_predict(prompt, max_new_tokens=64, num_beams=4):
    """Zero-shot FLAN-T5 inference for arbitrary instruction-formatted tasks."""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
                       max_length=512).to(device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new_tokens,
                             num_beams=num_beams, early_stopping=True)
    return tokenizer.decode(out[0], skip_special_tokens=True)

prompts = [
    "Classify sentiment (positive/negative): 'This lecture on transformers was outstanding!'",
    "Translate to French: 'The quick brown fox jumps over the lazy dog.'",
    "Answer: What pretraining objective does T5 use? Context: T5 uses span corruption.",
]
for prompt in prompts:
    answer = flan_t5_predict(prompt)
    print(f"Q: {prompt[:60]}...")
    print(f"A: {answer}\n")
```

## Comparison of Pretraining Objectives

The three paradigms — CLM, MLM, and Prefix LM / Encoder-Decoder — represent fundamental trade-offs between generation capability, representation richness, and compute efficiency. CLM is the simplest and most sample-efficient, making it dominant for large-scale pretraining. MLM produces the richest token-level representations for understanding but cannot generate. Prefix LM / Encoder-Decoder is the most powerful for conditional generation tasks but requires paired input-output data for task formatting and is more expensive to train (two components).

| Aspect | CLM | MLM | Prefix LM | Encoder-Decoder |
| --- | --- | --- | --- | --- |
| Attention type | Causal (left-to-right) | Bidirectional (full) | Bidir prefix + causal continuation | Encoder: full; Decoder: causal |
| Training target | All N tokens (shifted) | ~15% masked tokens | Dropped span tokens + sentinels | Target sequence tokens |
| Generation | Native autoregressive | Not native — needs separate decoder | Native continuation of prefix | Native via cross-attention decoding |
| Sample efficiency | High — N targets/seq | Low — ~0.15N targets/seq | Medium — depends on span density | Depends on paired data quality |
| Key models | GPT, LLaMA, Mistral | BERT, RoBERTa, DeBERTa | PaLM (suffix prediction) | T5, FLAN-T5, BART, mT5 |

## UL2 — Mixture of Objectives

UL2 (Tay et al. 2022) proposes training a single model with a mixture of denoising objectives, calling it Mixture-of-Denoisers (MoD). Three objective families are mixed: R-denoisers (CLM-like: predict a suffix), S-denoisers (span corruption like T5 with short spans), and X-denoisers (extreme span corruption with very long spans or high masking rates). A mode token ([R], [S], [X]) prepended to the input tells the model which denoising regime applies. UL2-20B outperforms GPT-3 175B on many benchmarks, showing that objective diversity during pretraining is a more efficient use of compute than scaling a single objective.

- R-denoiser: predict suffix from prefix — identical to CLM, encourages left-to-right generation.
- S-denoiser: T5-style span corruption with short spans (mean 3 tokens, 15% rate) — standard seq2seq.
- X-denoiser: extreme corruption — very long spans (mean 32 tokens) or high rate (50%) — forces full document reconstruction.
- Mode token ([R], [S], [X]) prepended to input routes the model to the correct denoising behaviour.
- UL2 unifies GPT-style generation and T5-style seq2seq in one model without architectural changes.

## Compute Efficiency of Prefix LM

A practical advantage of the encoder-decoder architecture is that the encoder computes prefix representations only once per generation request. In CLM, re-processing the entire prompt is required for each new token (mitigated by KV cache), and the prefix tokens compete for context length with generated tokens. In encoder-decoder models, the prefix is processed by the encoder at full attention complexity once, then its key-value representations are passed to the decoder via cross-attention for all generation steps. This separation means the encoder can process very long contexts without burdening the decoder. T5 11B achieves strong performance across diverse tasks while remaining more interpretable than same-size CLM models due to this explicit input-output separation.

## PaLM and Prefix Prediction

PaLM (Chowdhery et al., 2022), a 540B parameter decoder-only model, also incorporates a prefix-style training variant called suffix prediction: a fraction of training examples are formatted so that a random suffix of the document is moved to the beginning, and the model learns to complete the document from a position in the middle. This exposes the CLM-only model to bidirectional context during pretraining without requiring an encoder. Combined with chain-of-thought prompting, PaLM achieves human-level performance on a wide range of multi-step reasoning tasks, suggesting that pretraining objective diversity — even within a decoder-only framework — significantly improves generalisation.

