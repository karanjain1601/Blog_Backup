---
title: "Monte Carlo Tree Search for LLM Reasoning"
slug: "mcts-for-llms"
description: "Using MCTS to search over reasoning steps at inference time, with the LLM as a policy for action generation and a value/process reward model for state evaluation."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9udGUgQ2FybG8gVHJlZSBTZWFyY2ggKE1DVFMpIGlzIGEgcHJpbmNpcGxlZCBzZWFyY2ggYWxnb3JpdGhtIHRoYXQgaGFzIHBvd2VyZWQgc3VwZXJodW1hbiBwZXJmb3JtYW5jZSBpbiBib2FyZCBnYW1lcywgbm93IGFkYXB0ZWQgdG8gZ3VpZGUgbGFyZ2UgbGFuZ3VhZ2UgbW9kZWwgcmVhc29uaW5nIGF0IGluZmVyZW5jZSB0aW1lLiBUaGUgY29yZSBpZGVhIGlzIHRvIHRyZWF0IGVhY2ggcGFydGlhbCBzb2x1dGlvbiBhcyBhIG5vZGUgaW4gYSB0cmVlLCB1c2UgdGhlIExMTSBhcyBhIHBvbGljeSB0aGF0IHByb3Bvc2VzIGNhbmRpZGF0ZSBuZXh0IHJlYXNvbmluZyBzdGVwcyAoYWN0aW9ucyksIGFuZCB1c2UgYSBQcm9jZXNzIFJld2FyZCBNb2RlbCBvciB2YWx1ZSBmdW5jdGlvbiB0byBlc3RpbWF0ZSB0aGUgcXVhbGl0eSBvZiBlYWNoIHNlYXJjaCBzdGF0ZS4gTUNUUyBiYWxhbmNlcyBleHBsb3JhdGlvbiAodHJ5aW5nIG5vdmVsIHJlYXNvbmluZyBkaXJlY3Rpb25zKSBhbmQgZXhwbG9pdGF0aW9uIChkZXZlbG9waW5nIHByb21pc2luZyBwYXJ0aWFsIHNvbHV0aW9ucykgdmlhIHRoZSBVQ1QgZm9ybXVsYSwgaXRlcmF0aXZlbHkgcmVmaW5pbmcgaXRzIGVzdGltYXRlcyB0aHJvdWdoIHNpbXVsYXRpb24gcm9sbG91dHMuIEFwcGxpZWQgdG8gbWF0aGVtYXRpY2FsIHJlYXNvbmluZywgY29kZSBnZW5lcmF0aW9uLCBhbmQgbXVsdGktc3RlcCBwbGFubmluZywgTUNUUy1ndWlkZWQgTExNcyBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybSBncmVlZHkgZGVjb2RpbmcsIGJlYW0gc2VhcmNoLCBhbmQgZmxhdCBiZXN0LW9mLU4gYXQgZXF1aXZhbGVudCB0b2tlbiBidWRnZXRzIOKAlCBwYXJ0aWN1bGFybHkgb24gcHJvYmxlbXMgdGhhdCByZXF1aXJlIGJhY2t0cmFja2luZyB3aGVuIGFuIGVhcmx5IHJlYXNvbmluZyBzdGVwIHR1cm5zIG91dCB0byBiZSBpbmNvcnJlY3QuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIE1DVFMgb3BlcmF0ZXMgb3ZlciBhIGRpc2NyZXRlIHN0YXRlIHNwYWNlIHdpdGggYSBrbm93biBhY3Rpb24gc2V0LCB1c2luZyBmb3VyIHBoYXNlcyBwZXIgaXRlcmF0aW9uOiBzZWxlY3Rpb24gKHRyYXZlcnNlIHRoZSB0cmVlIGZyb20gcm9vdCB1c2luZyBVQ1QpLCBleHBhbnNpb24gKGFkZCBhIG5ldyBjaGlsZCBub2RlKSwgc2ltdWxhdGlvbiAocnVuIGEgcm9sbG91dCBwb2xpY3kgdG8gdGVybWluYWwgc3RhdGUpLCBhbmQgYmFja3Byb3BhZ2F0aW9uICh1cGRhdGUgUS12YWx1ZXMgdXAgdGhlIHRyZWUpLiBGb3IgTExNIHJlYXNvbmluZywgdGhlIHN0YXRlIGlzIGEgcGFydGlhbCBjaGFpbi1vZi10aG91Z2h0IChhIHNlcXVlbmNlIG9mIHRva2VucyB1cCB0byB0aGUgY3VycmVudCByZWFzb25pbmcgc3RlcCksIHRoZSBhY3Rpb24gaXMgdGhlIG5leHQgcmVhc29uaW5nIHN0ZXAgKGdlbmVyYXRlZCBieSB0aGUgTExNKSwgYW5kIHRoZSB2YWx1ZSBmdW5jdGlvbiBpcyBhIFBSTSBvciBPUk0gdGhhdCBlc3RpbWF0ZXMgdGhlIHByb2JhYmlsaXR5IG9mIHJlYWNoaW5nIGEgY29ycmVjdCBmaW5hbCBhbnN3ZXIgZnJvbSB0aGlzIHN0YXRlLiBLZXkgZGVzaWduIGNob2ljZXMgaW5jbHVkZSB0aGUgdHJlZSBncmFudWxhcml0eSAod29yZC1sZXZlbCwgc2VudGVuY2UtbGV2ZWwsIG9yIHN0ZXAtbGV2ZWwgYWN0aW9ucyksIHRoZSBzaW11bGF0aW9uIHBvbGljeSAodGhlIHNhbWUgTExNIGdyZWVkeS1kZWNvZGVkIHRvIGNvbXBsZXRpb24pLCBhbmQgdGhlIG51bWJlciBvZiBNQ1RTIGl0ZXJhdGlvbnMgcGVyIHByb2JsZW0uIFN5c3RlbXMgbGlrZSBBbHBoYUNvZGUgMiBhbmQgclN0YXIgKE1pY3Jvc29mdCwgMjAyNCkgZGVtb25zdHJhdGUgdGhhdCBNQ1RTIHdpdGggYSBoaWdoLXF1YWxpdHkgdmFsdWUgZnVuY3Rpb24gY2FuIGFjaGlldmUgc3RhdGUtb2YtdGhlLWFydCBhY2N1cmFjeSBvbiBBTUMvQUlNRSBwcm9ibGVtcyB3aXRoIHNpZ25pZmljYW50bHkgZmV3ZXIgTExNIGNhbGxzIHRoYW4gbmFpdmUgYmVzdC1vZi1OLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1DVFMgQWxnb3JpdGhtIFJlY2FwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2xhc3NpY2FsIE1DVFMgYWxnb3JpdGhtIG1haW50YWlucyBhIHRyZWUgb2YgdmlzaXRlZCBzdGF0ZXMsIGVhY2ggc3RvcmluZyBhIHZpc2l0IGNvdW50IE4ocykgYW5kIGEgY3VtdWxhdGl2ZSB2YWx1ZSBRKHMpLiBBdCBlYWNoIGl0ZXJhdGlvbiwgdGhlIGFsZ29yaXRobSBzZWxlY3RzIGEgbGVhZiBub2RlIGJ5IHRyYXZlcnNpbmcgdGhlIHRyZWUgZ3JlZWRpbHkgYWNjb3JkaW5nIHRvIHRoZSBVQ1Qgc2NvcmUgYXQgZWFjaCBkZWNpc2lvbiBwb2ludDogVUNUKHMsYSkgPSBRKHMsYSkvTihzLGEpICsgYyAqIHNxcnQobG9nIE4ocykgLyBOKHMsYSkpLCB3aGVyZSBjIGlzIGFuIGV4cGxvcmF0aW9uIGNvbnN0YW50ICh0eXBpY2FsbHkgMS0yKS4gVGhlIHNlbGVjdGVkIGxlYWYgaXMgZXhwYW5kZWQgYnkgYWRkaW5nIG9uZSBvciBtb3JlIGNoaWxkIG5vZGVzIChjYW5kaWRhdGUgbmV4dCBzdGVwcykuIEVhY2ggbmV3IGNoaWxkIGlzIGV2YWx1YXRlZCBlaXRoZXIgYnkgcnVubmluZyBhIHNpbXVsYXRpb24gcm9sbG91dCB0byBhIHRlcm1pbmFsIHN0YXRlIChNb250ZSBDYXJsbyBlc3RpbWF0ZSkgb3IgYnkgcXVlcnlpbmcgYSBsZWFybmVkIHZhbHVlIGZ1bmN0aW9uICh0aGUgbmV1cmFsIE1DVFMgYXBwcm9hY2gpLiBUaGUgcmVzdWx0aW5nIHZhbHVlIGVzdGltYXRlIGlzIGJhY2twcm9wYWdhdGVkIHVwIHRoZSB0cmVlLCBpbmNyZW1lbnRpbmcgdmlzaXQgY291bnRzIGFuZCB1cGRhdGluZyBRLXZhbHVlcyBhbG9uZyB0aGUgcGF0aC4gQWZ0ZXIgYSBidWRnZXQgb2YgaXRlcmF0aW9ucywgdGhlIGFjdGlvbiB3aXRoIHRoZSBoaWdoZXN0IHZpc2l0IGNvdW50IChub3QgdGhlIGhpZ2hlc3QgUS12YWx1ZSkgZnJvbSB0aGUgcm9vdCBpcyBzZWxlY3RlZCBhcyB0aGUgYmVzdCBhY3Rpb24sIHNpbmNlIHZpc2l0IGNvdW50IGlzIGEgbW9yZSBzdGFibGUgc3RhdGlzdGljIHRoYW4gUS12YWx1ZSB1bmRlciBub2lzeSByb2xsb3V0cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG1hdGhcbmltcG9ydCByYW5kb21cbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBPcHRpb25hbFxuZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzLCBmaWVsZFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBNQ1RTTm9kZTpcbiAgICBzdGF0ZTogc3RyICAgICAgICAgICAgICAgICAgICAgICMgcGFydGlhbCBjaGFpbi1vZi10aG91Z2h0IHRleHRcbiAgICBwYXJlbnQ6IE9wdGlvbmFsW1wiTUNUU05vZGVcIl0gPSBOb25lXG4gICAgY2hpbGRyZW46IExpc3RbXCJNQ1RTTm9kZVwiXSAgID0gZmllbGQoZGVmYXVsdF9mYWN0b3J5PWxpc3QpXG4gICAgdmlzaXRfY291bnQ6IGludCAgPSAwXG4gICAgdG90YWxfdmFsdWU6IGZsb2F0ID0gMC4wXG4gICAgaXNfdGVybWluYWw6IGJvb2wgPSBGYWxzZVxuXG4gICAgZGVmIHFfdmFsdWUoc2VsZikgLVx1MDAzZSBmbG9hdDpcbiAgICAgICAgcmV0dXJuIHNlbGYudG90YWxfdmFsdWUgLyBtYXgoc2VsZi52aXNpdF9jb3VudCwgMSlcblxuICAgIGRlZiB1Y3Rfc2NvcmUoc2VsZiwgYzogZmxvYXQgPSAxLjQxNCkgLVx1MDAzZSBmbG9hdDpcbiAgICAgICAgIyBVQ1Q6IGV4cGxvaXRhdGlvbiArIGV4cGxvcmF0aW9uIGJvbnVzXG4gICAgICAgIGlmIHNlbGYudmlzaXRfY291bnQgPT0gMDpcbiAgICAgICAgICAgIHJldHVybiBmbG9hdChcImluZlwiKSAgICMgYWx3YXlzIGV4cGFuZCB1bnZpc2l0ZWQgbm9kZXMgZmlyc3RcbiAgICAgICAgcGFyZW50X24gPSBzZWxmLnBhcmVudC52aXNpdF9jb3VudCBpZiBzZWxmLnBhcmVudCBlbHNlIDFcbiAgICAgICAgZXhwbG9pdCAgPSBzZWxmLnFfdmFsdWUoKVxuICAgICAgICBleHBsb3JlICA9IGMgKiBtYXRoLnNxcnQobWF0aC5sb2cocGFyZW50X24pIC8gc2VsZi52aXNpdF9jb3VudClcbiAgICAgICAgcmV0dXJuIGV4cGxvaXQgKyBleHBsb3JlXG5cbiAgICBkZWYgYmVzdF9jaGlsZChzZWxmLCBjOiBmbG9hdCA9IDEuNDE0KSAtXHUwMDNlIFwiTUNUU05vZGVcIjpcbiAgICAgICAgcmV0dXJuIG1heChzZWxmLmNoaWxkcmVuLCBrZXk9bGFtYmRhIGNoOiBjaC51Y3Rfc2NvcmUoYykpXG5cbiAgICBkZWYgbW9zdF92aXNpdGVkX2NoaWxkKHNlbGYpIC1cdTAwM2UgXCJNQ1RTTm9kZVwiOlxuICAgICAgICAjIEZpbmFsIGFjdGlvbiBzZWxlY3Rpb246IHZpc2l0IGNvdW50IGlzIG1vcmUgc3RhYmxlIHRoYW4gUS5cbiAgICAgICAgcmV0dXJuIG1heChzZWxmLmNoaWxkcmVuLCBrZXk9bGFtYmRhIGNoOiBjaC52aXNpdF9jb3VudCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZGFwdGluZyBNQ1RTIGZvciBUZXh0IEdlbmVyYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFkYXB0aW5nIE1DVFMgdG8gdGV4dCBnZW5lcmF0aW9uIHJlcXVpcmVzIHJlc29sdmluZyB0aHJlZSBkZXNpZ24gY2hvaWNlcyB0aGF0IGRvIG5vdCBhcmlzZSBpbiBib2FyZCBnYW1lcy4gRmlyc3QsIHRoZSBhY3Rpb24gc3BhY2UgaXMgb3Blbi1lbmRlZDogdGhlIExMTSBjYW4gZ2VuZXJhdGUgYW55IHRleHQgYXMgdGhlIG5leHQgcmVhc29uaW5nIHN0ZXAsIHNvIHRoZSB0cmVlIGNhbm5vdCBlbnVtZXJhdGUgYWxsIHBvc3NpYmxlIGFjdGlvbnMgaW4gYWR2YW5jZS4gSW5zdGVhZCwgdGhlIGV4cGFuc2lvbiBwaGFzZSBzYW1wbGVzIGsgY2FuZGlkYXRlIG5leHQgc3RlcHMgKGs9NC04IGlzIHR5cGljYWwpIGZyb20gdGhlIExMTSBhdCB0aGUgY3VycmVudCBzdGF0ZS4gU2Vjb25kLCB0aGUgc3RhdGUgcmVwcmVzZW50YXRpb24gaXMgYSBncm93aW5nIHRleHQgc3RyaW5nIHJhdGhlciB0aGFuIGEgZml4ZWQtZGltZW5zaW9uYWwgZmVhdHVyZSB2ZWN0b3IsIHdoaWNoIG1lYW5zIG5vZGUgaWRlbnRpdHkgbXVzdCBiZSBkZWZpbmVkIGJ5IHRoZSBmdWxsIHRleHQgcHJlZml4IOKAlCB0d28gcGF0aHMgdGhhdCByZWFjaCB0aGUgc2FtZSB0ZXh0IGFyZSB0aGUgc2FtZSBzdGF0ZS4gVGhpcmQsIHRlcm1pbmFsIGRldGVjdGlvbiByZXF1aXJlcyBhIHZlcmlmaWVyOiB0aGUgc2ltdWxhdGlvbiByb2xsb3V0IGlzIGNvbXBsZXRlIHdoZW4gdGhlIExMTSBnZW5lcmF0ZXMgYSBmaW5hbCBhbnN3ZXIgdG9rZW4gb3IgZXhwbGljaXQgZW5kIG1hcmtlciwgYW5kIHRoZSByZXdhcmQgc2lnbmFsIGNvbWVzIGZyb20gYSB2ZXJpZmllciAoc3ltYm9saWMgZm9yIG1hdGgpIG9yIE9STSAoZm9yIG9wZW4tZW5kZWQgdGFza3MpLiBUaGUgc3RlcC1sZXZlbCBncmFudWxhcml0eSAob25lIE1DVFMgYWN0aW9uID0gb25lIHJlYXNvbmluZyBzdGVwID0gb25lIHNlbnRlbmNlIG9yIGVxdWF0aW9uKSBoYXMgcHJvdmVuIG1vc3QgZWZmZWN0aXZlIGluIHByYWN0aWNlLCBiYWxhbmNpbmcgdHJlZSBkZXB0aCBhZ2FpbnN0IGJyYW5jaGluZyBmYWN0b3IuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVUNUIFNlbGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFVDVCAoVXBwZXIgQ29uZmlkZW5jZSBCb3VuZCBmb3IgVHJlZXMpIHNlbGVjdGlvbiBjcml0ZXJpb24gbmF2aWdhdGVzIHRoZSBleHBsb3JhdGlvbi1leHBsb2l0YXRpb24gdHJhZGUtb2ZmIGF0IGVhY2ggbm9kZS4gU3RhcnRpbmcgZnJvbSB0aGUgcm9vdCwgYXQgZWFjaCBub2RlIHRoZSBhbGdvcml0aG0gZGVzY2VuZHMgdG8gdGhlIGNoaWxkIHdpdGggdGhlIGhpZ2hlc3QgVUNUIHNjb3JlOiBVQ1QgPSBRL04gKyBjICogc3FydChsb2coTl9wYXJlbnQpL05fY2hpbGQpLiBUaGUgZXhwbG9pdGF0aW9uIHRlcm0gUS9OIGlzIHRoZSBlbXBpcmljYWwgYXZlcmFnZSByZXdhcmQgYWxvbmcgdGhlIHN1Yi10cmVlIHJvb3RlZCBhdCB0aGUgY2hpbGQ7IGEgaGlnaCBRL04gbWVhbnMgdGhpcyBicmFuY2ggaGFzIGhpc3RvcmljYWxseSBsZWQgdG8gY29ycmVjdCBzb2x1dGlvbnMuIFRoZSBleHBsb3JhdGlvbiB0ZXJtIGMgKiBzcXJ0KGxvZyhOX3BhcmVudCkvTl9jaGlsZCkgaXMgbGFyZ2Ugd2hlbiB0aGUgY2hpbGQgaGFzIGJlZW4gdmlzaXRlZCByYXJlbHkgcmVsYXRpdmUgdG8gaXRzIHNpYmxpbmdzLCBpbmNlbnRpdmlzaW5nIHRoZSBhbGdvcml0aG0gdG8gZ2F0aGVyIG1vcmUgaW5mb3JtYXRpb24gYWJvdXQgdW5kZXItZXhwbG9yZWQgYnJhbmNoZXMuIFRoZSBjb25zdGFudCBjIGNvbnRyb2xzIHRoZSBiYWxhbmNlOiBjPTAgaXMgcHVyZSBncmVlZHkgKGFsd2F5cyBleHBsb2l0KSwgYz1pbmZpbml0eSBpcyByYW5kb20gZXhwbG9yYXRpb24uIEZvciBMTE0gcmVhc29uaW5nIHdpdGggYSBQUk0gYXMgdmFsdWUgZnVuY3Rpb24sIGMgaXMgdHVuZWQgb24gYSB2YWxpZGF0aW9uIHNldCBhbmQgdHlwaWNhbGx5IGxpZXMgaW4gdGhlIHJhbmdlIDAuNS0yLjAuIEEgY29tbW9uIHZhcmlhbnQgY2xpcHMgUSB0byBbMCwgMV0gKG5vcm1hbGlzZWQgcHJvYmFiaWxpdHkgZXN0aW1hdGVzIGZyb20gdGhlIFBSTSkgYW5kIHVzZXMgYz1zcXJ0KDIpIGFzIHRoZSBkZWZhdWx0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbWF0aFxuaW1wb3J0IGFzeW5jaW9cbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBDYWxsYWJsZSwgT3B0aW9uYWxcbmZyb20gb3BlbmFpIGltcG9ydCBBc3luY09wZW5BSVxuXG5hY2xpZW50ID0gQXN5bmNPcGVuQUkoKVxuXG5hc3luYyBkZWYgbGxtX2V4cGFuZChzdGF0ZTogc3RyLCBrOiBpbnQgPSA0LFxuICAgICAgICAgICAgICAgICAgICAgIG1vZGVsOiBzdHIgPSBcImdwdC00by1taW5pXCIpIC1cdTAwM2UgTGlzdFtzdHJdOlxuICAgICMgR2VuZXJhdGUgayBjYW5kaWRhdGUgbmV4dCByZWFzb25pbmcgc3RlcHMgZnJvbSB0aGUgTExNLlxuICAgIHRhc2tzID0gW2FjbGllbnQuY2hhdC5jb21wbGV0aW9ucy5jcmVhdGUoXG4gICAgICAgIG1vZGVsPW1vZGVsLCB0ZW1wZXJhdHVyZT0wLjgsIG1heF90b2tlbnM9MjAwLFxuICAgICAgICBtZXNzYWdlcz1be1wicm9sZVwiOiBcInVzZXJcIixcbiAgICAgICAgICAgICAgICAgICBcImNvbnRlbnRcIjogZlwiQ29udGludWUgdGhlIHNvbHV0aW9uIG9uZSBzdGVwOlxcbntzdGF0ZX1cIn1dXG4gICAgKSBmb3IgXyBpbiByYW5nZShrKV1cbiAgICByZXNwcyA9IGF3YWl0IGFzeW5jaW8uZ2F0aGVyKCp0YXNrcylcbiAgICByZXR1cm4gW3IuY2hvaWNlc1swXS5tZXNzYWdlLmNvbnRlbnQgZm9yIHIgaW4gcmVzcHNdXG5cbmRlZiBtY3RzX3NlbGVjdChyb290OiBcIk1DVFNOb2RlXCIsIGM6IGZsb2F0ID0gMS40MTQpIC1cdTAwM2UgXCJNQ1RTTm9kZVwiOlxuICAgIG5vZGUgPSByb290XG4gICAgd2hpbGUgbm9kZS5jaGlsZHJlbiBhbmQgbm90IG5vZGUuaXNfdGVybWluYWw6XG4gICAgICAgIG5vZGUgPSBub2RlLmJlc3RfY2hpbGQoYylcbiAgICByZXR1cm4gbm9kZVxuXG5kZWYgbWN0c19iYWNrcHJvcChub2RlOiBcIk1DVFNOb2RlXCIsIHZhbHVlOiBmbG9hdCkgLVx1MDAzZSBOb25lOlxuICAgIHdoaWxlIG5vZGUgaXMgbm90IE5vbmU6XG4gICAgICAgIG5vZGUudmlzaXRfY291bnQgICs9IDFcbiAgICAgICAgbm9kZS50b3RhbF92YWx1ZSAgKz0gdmFsdWVcbiAgICAgICAgbm9kZSAgICAgICAgICAgICAgID0gbm9kZS5wYXJlbnRcblxuZGVmIG1jdHNfZmluYWxfYW5zd2VyKHJvb3Q6IFwiTUNUU05vZGVcIikgLVx1MDAzZSBzdHI6XG4gICAgIyBXYWxrIHRoZSB0cmVlIGZvbGxvd2luZyB0aGUgbW9zdC12aXNpdGVkIGNoaWxkIGF0IGVhY2ggbGV2ZWwuXG4gICAgbm9kZSA9IHJvb3RcbiAgICB3aGlsZSBub2RlLmNoaWxkcmVuOlxuICAgICAgICBub2RlID0gbm9kZS5tb3N0X3Zpc2l0ZWRfY2hpbGQoKVxuICAgIHJldHVybiBub2RlLnN0YXRlIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXhwYW5zaW9uIGFuZCBTaW11bGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZXhwYW5zaW9uIHBoYXNlIGFkZHMgayBuZXcgY2hpbGQgbm9kZXMgYnkgc2FtcGxpbmcgayBjYW5kaWRhdGUgbmV4dCByZWFzb25pbmcgc3RlcHMgZnJvbSB0aGUgTExNIGF0IHRoZSBjdXJyZW50IGxlYWYgc3RhdGUuIEVhY2ggY2FuZGlkYXRlIGlzIGFwcGVuZGVkIHRvIHRoZSBleGlzdGluZyBwYXJ0aWFsIHNvbHV0aW9uIHRleHQsIGZvcm1pbmcgdGhlIGNoaWxkIHN0YXRlLiBUaGUgc2ltdWxhdGlvbiBwaGFzZSB0aGVuIGVzdGltYXRlcyB0aGUgdmFsdWUgb2YgZWFjaCBuZXcgY2hpbGQ6IGVpdGhlciBieSBydW5uaW5nIGEgZnVsbCByb2xsb3V0ICh0aGUgTExNIGNvbnRpbnVlcyBncmVlZGlseSB0byBhIGNvbXBsZXRlIHNvbHV0aW9uIGFuZCB0aGUgdmVyaWZpZXIgY2hlY2tzIHRoZSBmaW5hbCBhbnN3ZXIpIG9yIGJ5IHF1ZXJ5aW5nIGEgbGVhcm5lZCBQUk0gdGhhdCBzY29yZXMgdGhlIHF1YWxpdHkgb2YgdGhlIGN1cnJlbnQgcmVhc29uaW5nIHByZWZpeCB3aXRob3V0IHJvbGxpbmcgb3V0LiBSb2xsb3V0LWJhc2VkIHNpbXVsYXRpb24gaXMgYWNjdXJhdGUgYnV0IHNsb3cgKG9uZSBmdWxsIExMTSBnZW5lcmF0aW9uIHBlciBNQ1RTIGl0ZXJhdGlvbik7IFBSTS1iYXNlZCBzaW11bGF0aW9uIGlzIGZhc3QgYnV0IHJlcXVpcmVzIGEgdHJhaW5lZCBQUk0uIEluIHByYWN0aWNlLCBhIGh5YnJpZCBhcHByb2FjaCB3b3JrcyB3ZWxsOiB1c2UgdGhlIFBSTSB0byBmaWx0ZXIgZXhwYW5zaW9uIGNhbmRpZGF0ZXMgKGtlZXBpbmcgb25seSB0aGUgdG9wLWogYnkgUFJNIHNjb3JlKSwgdGhlbiBydW4gc2hvcnQgcm9sbG91dHMgZnJvbSB0aG9zZSBjYW5kaWRhdGVzIHRvIHZlcmlmeS4gVGhpcyByZWR1Y2VzIHRoZSB0b3RhbCBMTE0gdG9rZW4gYnVkZ2V0IHdoaWxlIG1haW50YWluaW5nIGhpZ2ggdmFsdWUgZXN0aW1hdGUgYWNjdXJhY3kuIFRoZSBzaW11bGF0aW9uIHJvbGxvdXQgcG9saWN5IGlzIHR5cGljYWxseSBncmVlZHkgZGVjb2RpbmcgKHRlbXBlcmF0dXJlPTApLCBzaW5jZSB0aGUgZ29hbCBpcyB0byBnZXQgYSByZWxpYWJsZSB0ZXJtaW5hbCByZXdhcmQgc2lnbmFsIHJhdGhlciB0aGFuIHRvIGV4cGxvcmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG1hdGhcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBEaWN0LCBUdXBsZVxuZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzLCBmaWVsZFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBSU3Rhck5vZGU6XG4gICAgc3RhdGU6IHN0clxuICAgIHBhcmVudDogXCJSU3Rhck5vZGVcIiA9IE5vbmVcbiAgICBjaGlsZHJlbjogTGlzdFtcIlJTdGFyTm9kZVwiXSA9IGZpZWxkKGRlZmF1bHRfZmFjdG9yeT1saXN0KVxuICAgIHZpc2l0X2NvdW50OiBpbnQgICA9IDBcbiAgICB0b3RhbF92YWx1ZTogZmxvYXQgPSAwLjBcbiAgICBkaXNjX3Njb3JlOiBmbG9hdCAgPSAwLjAgICMgZGlzY3JpbWluYXRvciAoUFJNKSBzY29yZSBhdCB0aGlzIG5vZGVcblxuZGVmIGRpc2NyaW1pbmF0b3Jfc2NvcmUocHJtX21vZGVsLCB0b2tlbml6ZXIsIHBhcnRpYWxfc29sOiBzdHIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgZGV2aWNlOiBzdHIgPSBcImNwdVwiKSAtXHUwMDNlIGZsb2F0OlxuICAgICMgU2NvcmUgYSBwYXJ0aWFsIHJlYXNvbmluZyBwYXRoIHVzaW5nIGEgUFJNIChzdGVwLWxldmVsIHJld2FyZCkuXG4gICAgZW5jID0gdG9rZW5pemVyKHBhcnRpYWxfc29sLCByZXR1cm5fdGVuc29ycz1cInB0XCIsXG4gICAgICAgICAgICAgICAgICAgIHRydW5jYXRpb249VHJ1ZSwgbWF4X2xlbmd0aD0xMDI0KS50byhkZXZpY2UpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGxvZ2l0cyA9IHBybV9tb2RlbCgqKmVuYykubG9naXRzICAgICAgICAgICMgKDEsIFQsIDIpIGZvciBzdGVwLWxldmVsIFBSTVxuICAgIHN0ZXBfcHJvYnMgPSB0b3JjaC5zb2Z0bWF4KGxvZ2l0c1s6LCAtMSwgOl0sIGRpbT0tMSlcbiAgICByZXR1cm4gZmxvYXQoc3RlcF9wcm9ic1swLCAxXSkgICAgICAgICAgICAgICAjIHByb2JhYmlsaXR5IG9mIFwiY29ycmVjdFwiIHN0ZXBcblxuZGVmIHJzdGFyX2V4cGFuZChub2RlOiBSU3Rhck5vZGUsIGNhbmRpZGF0ZXM6IExpc3Rbc3RyXSxcbiAgICAgICAgICAgICAgICAgIHBybV9tb2RlbCwgdG9rZW5pemVyLCB0b3BfazogaW50ID0gMikgLVx1MDAzZSBMaXN0W1JTdGFyTm9kZV06XG4gICAgIyBBZGQgY2hpbGRyZW4sIHNjb3JlIHdpdGggZGlzY3JpbWluYXRvciwga2VlcCB0b3Atay5cbiAgICBzY29yZWQgPSBbXVxuICAgIGZvciBjIGluIGNhbmRpZGF0ZXM6XG4gICAgICAgIGNoaWxkX3N0YXRlID0gbm9kZS5zdGF0ZSArIFwiXFxuXCIgKyBjXG4gICAgICAgIHNjb3JlID0gZGlzY3JpbWluYXRvcl9zY29yZShwcm1fbW9kZWwsIHRva2VuaXplciwgY2hpbGRfc3RhdGUpXG4gICAgICAgIHNjb3JlZC5hcHBlbmQoKHNjb3JlLCBjaGlsZF9zdGF0ZSkpXG4gICAgc2NvcmVkLnNvcnQocmV2ZXJzZT1UcnVlLCBrZXk9bGFtYmRhIHg6IHhbMF0pXG4gICAgY2hpbGRyZW4gPSBbXVxuICAgIGZvciBzY29yZSwgc3RhdGUgaW4gc2NvcmVkWzp0b3Bfa106XG4gICAgICAgIGNoaWxkID0gUlN0YXJOb2RlKHN0YXRlPXN0YXRlLCBwYXJlbnQ9bm9kZSwgZGlzY19zY29yZT1zY29yZSlcbiAgICAgICAgbm9kZS5jaGlsZHJlbi5hcHBlbmQoY2hpbGQpXG4gICAgICAgIGNoaWxkcmVuLmFwcGVuZChjaGlsZClcbiAgICByZXR1cm4gY2hpbGRyZW4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCYWNrcHJvcGFnYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJhY2twcm9wYWdhdGlvbiB1cGRhdGVzIHRoZSBRLXZhbHVlcyBhbmQgdmlzaXQgY291bnRzIG9mIGFsbCBub2RlcyBhbG9uZyB0aGUgcGF0aCBmcm9tIHRoZSBleHBhbmRlZCBsZWFmIGJhY2sgdG8gdGhlIHJvb3QuIEZvciBlYWNoIG5vZGUgb24gdGhlIHBhdGgsIHRoZSB2aXNpdCBjb3VudCBpcyBpbmNyZW1lbnRlZCBieSAxIGFuZCB0aGUgdG90YWwgdmFsdWUgaXMgaW5jcmVtZW50ZWQgYnkgdGhlIHZhbHVlIGVzdGltYXRlIG9idGFpbmVkIGZyb20gdGhlIHNpbXVsYXRpb24gb3IgUFJNIGF0IHRoZSBsZWFmLiBUaGUgUS12YWx1ZSBhdCBlYWNoIG5vZGUgaXMgdGhlbiB0aGUgcmF0aW8gdG90YWxfdmFsdWUgLyB2aXNpdF9jb3VudC4gQmFja3Byb3BhZ2F0aW9uIGVuc3VyZXMgdGhhdCB0aGUgVUNUIHNjb3JlcyBhdCBhbGwgYW5jZXN0b3JzIHJlZmxlY3QgdGhlIGxhdGVzdCBlc3RpbWF0ZSBvZiB0aGUgbGVhZiB2YWx1ZSwgcHJvcGFnYXRpbmcgaW5mb3JtYXRpb24gZnJvbSBzdWNjZXNzZnVsIGJyYW5jaGVzIHVwd2FyZCB0aHJvdWdoIHRoZSB0cmVlLiBJbiB0aGUgc3RhbmRhcmQgZm9ybXVsYXRpb24sIHRoZSB2YWx1ZSBpcyBiYWNrcHJvcGFnYXRlZCB1bmNoYW5nZWQgZnJvbSB0aGUgbGVhZiB0byB0aGUgcm9vdCAoYSBmbGF0IGJhY2t1cCkuIEFuIGFsdGVybmF0aXZlIGlzIHRoZSBtYXggYmFja3VwLCB3aGVyZSBlYWNoIG5vZGUgc3RvcmVzIHRoZSBtYXhpbXVtIHZhbHVlIHNlZW4gaW4gaXRzIHN1YnRyZWUgcmF0aGVyIHRoYW4gdGhlIGF2ZXJhZ2Ug4oCUIHRoaXMgaXMgYWR2YW50YWdlb3VzIHdoZW4gaW5kaXZpZHVhbCBjb3JyZWN0IHNvbHV0aW9ucyBhcmUgcmFyZSBhbmQgdGhlIGF2ZXJhZ2UgdmFsdWUgd291bGQgYmUgZG9taW5hdGVkIGJ5IGluY29ycmVjdCByb2xsb3V0cy4gRW1waXJpY2FsbHksIHRoZSBhdmVyYWdlIGJhY2t1cCB0ZW5kcyB0byBwZXJmb3JtIGJldHRlciBmb3Igc3RlcC1sZXZlbCBQUk1zLCB3aGlsZSB0aGUgbWF4IGJhY2t1cCBpcyBwcmVmZXJyZWQgZm9yIHNwYXJzZSBiaW5hcnkgcmV3YXJkcyBmcm9tIHZlcmlmaWVycy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQU1DIGFjY3VyYWN5IiwiQUlNRSBhY2N1cmFjeSIsIkxMTSBjYWxscyIsIkxhdGVuY3kgKHMpIiwiTm90ZXMiXSwicm93cyI6W1siR3JlZWR5IGRlY29kZSIsIjUyJSIsIjglIiwiMSIsIjIiLCJTaW5nbGUgc2FtcGxlLCBkZXRlcm1pbmlzdGljIl0sWyJCZWFtIHNlYXJjaCBrPTQiLCI1OCUiLCIxMiUiLCI0IiwiOCIsIlBhcmFsbGVsIGJlYW1zLCBubyBiYWNrdHJhY2siXSxbIkJlc3Qtb2YtTiBOPTE2IiwiNjclIiwiMTglIiwiMTYiLCIzMiIsIkZsYXQgcGFyYWxsZWw7IG5vIHRyZWUgc3RydWN0dXJlIl0sWyJNQ1RTIHNoYWxsb3cgKDUgaXRlcikiLCI3NCUiLCIyNyUiLCIzMCIsIjU1IiwiVHJlZSBzZWFyY2ggd2l0aCBQUk07IGVhcmx5IHN0b3BwaW5nIl0sWyJNQ1RTIGRlZXAgKDIwIGl0ZXIpIiwiODElIiwiMzglIiwiODAiLCIxNDAiLCJGdWxsIHNlYXJjaCBidWRnZXQ7IGJlc3QgYWNjdXJhY3kiXSxbIkFscGhhQ29kZTIgTUNUUyIsIjg2JSIsIjQ1JSIsIjIwMCsiLCIzMDArIiwiUHJvZHVjdGlvbiBzeXN0ZW07IHNwZWNpYWxpc2VkIFBSTSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWxwaGFDb2RlIGFuZCByU3RhciBSZXN1bHRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbHBoYUNvZGUgMiAoRGVlcE1pbmQsIDIwMjMpIGRlbW9uc3RyYXRlZCB0aGF0IE1DVFMtc3R5bGUgdHJlZSBzZWFyY2ggb3ZlciBjb2RlIGdlbmVyYXRpb24gY2FuZGlkYXRlcywgZ3VpZGVkIGJ5IGEgbGVhcm5lZCBzY29yaW5nIG1vZGVsLCBjb3VsZCBhY2hpZXZlIGNvbXBldGl0aXZlIHByb2dyYW1tZXIgbGV2ZWwgb24gQ29kZWZvcmNlcyBwcm9ibGVtcy4gVGhlIGtleSBpbnNpZ2h0IHdhcyB0aGF0IE1DVFMgYWxsb3dzIHRoZSBzZWFyY2ggdG8gYmFja3RyYWNrIGZyb20gZGVhZC1lbmQgY29kZSBicmFuY2hlcyAoY29tcGlsYXRpb24gZXJyb3JzLCBmYWlsaW5nIHRlc3RzKSBhbmQgcmVkaXJlY3QgY29tcHV0ZSB0b3dhcmQgcHJvbWlzaW5nIHBhcnRpYWwgcHJvZ3JhbXMuIHJTdGFyIChNaWNyb3NvZnQgUmVzZWFyY2gsIDIwMjQpIGFwcGxpZWQgYSBzaW1pbGFyIGFwcHJvYWNoIHRvIG1hdGhlbWF0aWNhbCByZWFzb25pbmcgdXNpbmcgTGxhbWEgbW9kZWxzOiBhIG11dHVhbCByZWFzb25pbmcgZGlzY3JpbWluYXRvciBzY29yZXMgY2FuZGlkYXRlIHJlYXNvbmluZyBhY3Rpb25zLCBhbmQgTUNUUyB1c2VzIHRoZXNlIHNjb3JlcyBhcyB2YWx1ZSBlc3RpbWF0ZXMgdG8gZ3VpZGUgdGhlIHNlYXJjaC4gclN0YXIgZGVtb25zdHJhdGVkIHRoYXQgcmVsYXRpdmVseSBzbWFsbCBtb2RlbHMgKDdCLTEzQiBwYXJhbWV0ZXJzKSBhdWdtZW50ZWQgd2l0aCBNQ1RTIGFuZCBhIGRpc2NyaW1pbmF0b3IgY291bGQgb3V0cGVyZm9ybSBtdWNoIGxhcmdlciBtb2RlbHMgb24gTUFUSCwgR1NNOEssIGFuZCBBSU1FIGJlbmNobWFya3MuIFRoZSByU3RhciBkaXNjcmltaW5hdG9yIGlzIHRyYWluZWQgb24gc3ludGhldGljIGRhdGEgZ2VuZXJhdGVkIGJ5IHRoZSBzYW1lIG1vZGVsLCBtYWtpbmcgdGhlIGFwcHJvYWNoIHNlbGYtaW1wcm92aW5nOiBiZXR0ZXIgc29sdXRpb25zIGRpc2NvdmVyZWQgdmlhIE1DVFMgYmVjb21lIHRyYWluaW5nIGRhdGEgZm9yIHRoZSBuZXh0IGRpc2NyaW1pbmF0b3IgdmVyc2lvbiwgY3JlYXRpbmcgYSB2aXJ0dW91cyBjeWNsZSBvZiBjYXBhYmlsaXR5IGltcHJvdmVtZW50LiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUFJNIFF1YWxpdHkgaXMgdGhlIEJvdHRsZW5lY2siLCJjb250ZW50IjoiTUNUUyBmb3IgTExNcyBpcyBtb3N0IHVzZWZ1bCB3aGVuIHlvdSBoYXZlIGEgcmVsaWFibGUgcHJvY2VzcyByZXdhcmQgbW9kZWwg4oCUIHdpdGhvdXQgYSBnb29kIHZhbHVlIGZ1bmN0aW9uLCBNQ1RTIGRlZ3JhZGVzIHRvIGV4cGVuc2l2ZSByYW5kb20gc2VhcmNoIHdpdGggZXh0cmEgYm9va2tlZXBpbmcuIFRoZSBVQ1Qgc2VsZWN0aW9uIGlzIG9ubHkgYXMgZ29vZCBhcyB0aGUgUS12YWx1ZSBlc3RpbWF0ZXMgaXQgdXNlcywgd2hpY2ggaW4gdHVybiBkZXBlbmQgb24gdGhlIFBSTSBhY2N1cmFjeSBhdCBlYWNoIGludGVybWVkaWF0ZSBzdGVwLiBJbnZlc3QgaGVhdmlseSBpbiBQUk0gcXVhbGl0eSBiZWZvcmUgaW1wbGVtZW50aW5nIE1DVFM6IGEgd2VsbC1jYWxpYnJhdGVkIFBSTSB0aGF0IGFjaGlldmVzIDAuODUrIHN0ZXAtbGV2ZWwgQVVST0Mgd2lsbCBnaXZlIHlvdSBtb3N0IG9mIHRoZSBNQ1RTIGJlbmVmaXQ7IGEgcG9vcmx5IGNhbGlicmF0ZWQgUFJNIGF0IDAuNjUgQVVST0Mgd2lsbCBnaXZlIHlvdSB3b3JzZSByZXN1bHRzIHRoYW4gZmxhdCBiZXN0LW9mLU4gYXQgdGhlIHNhbWUgdG9rZW4gYnVkZ2V0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdGltZVxuaW1wb3J0IHN0YXRpc3RpY3NcbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0LCBEaWN0LCBDYWxsYWJsZVxuZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzXG5cbkBkYXRhY2xhc3NcbmNsYXNzIEJlbmNobWFya1Jlc3VsdDpcbiAgICBtZXRob2Q6IHN0clxuICAgIGFjY3VyYWN5OiBmbG9hdFxuICAgIGxsbV9jYWxsczogaW50XG4gICAgbGF0ZW5jeV9zOiBmbG9hdFxuXG5kZWYgcnVuX2JlbmNobWFyayhwcm9ibGVtczogTGlzdFtEaWN0XSwgc29sdmVfZm46IENhbGxhYmxlLFxuICAgICAgICAgICAgICAgICAgIG1ldGhvZF9uYW1lOiBzdHIpIC1cdTAwM2UgQmVuY2htYXJrUmVzdWx0OlxuICAgICMgRXZhbHVhdGUgYSBzb2x2aW5nIHN0cmF0ZWd5IG9uIEFNQy9BSU1FIHByb2JsZW1zLlxuICAgIGNvcnJlY3QsIGNhbGxzX3RvdGFsLCBsYXRlbmNpZXMgPSAwLCAwLCBbXVxuICAgIGZvciBwcm9iIGluIHByb2JsZW1zOlxuICAgICAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgcmVzdWx0LCBjYWxscyA9IHNvbHZlX2ZuKHByb2JbXCJwcm9ibGVtXCJdLCBwcm9iW1wiZ29sZFwiXSlcbiAgICAgICAgbGF0ZW5jaWVzLmFwcGVuZCh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApXG4gICAgICAgIGNhbGxzX3RvdGFsICs9IGNhbGxzXG4gICAgICAgIGlmIHJlc3VsdCA9PSBwcm9iW1wiZ29sZFwiXTpcbiAgICAgICAgICAgIGNvcnJlY3QgKz0gMVxuICAgIGFjYyA9IGNvcnJlY3QgLyBsZW4ocHJvYmxlbXMpXG4gICAgYXZnX2xhdCAgPSBzdGF0aXN0aWNzLm1lYW4obGF0ZW5jaWVzKVxuICAgIGF2Z19jYWxsID0gY2FsbHNfdG90YWwgLyBsZW4ocHJvYmxlbXMpXG4gICAgcHJpbnQoZlwie21ldGhvZF9uYW1lOlx1MDAzYzIwfSBhY2M9e2FjYzouMiV9IGNhbGxzPXthdmdfY2FsbDouMWZ9IGxhdD17YXZnX2xhdDouMWZ9c1wiKVxuICAgIHJldHVybiBCZW5jaG1hcmtSZXN1bHQobWV0aG9kX25hbWUsIGFjYywgaW50KGF2Z19jYWxsKSwgYXZnX2xhdClcblxuIyBTaW11bGF0ZWQgcmVzdWx0cyBtYXRjaGluZyBsaXRlcmF0dXJlIGJhc2VsaW5lc1xucmVzdWx0cyA9IFtcbiAgICBCZW5jaG1hcmtSZXN1bHQoXCJHcmVlZHlcIiwgICAgICAgIDAuNTIsIDEsICAgMi4xKSxcbiAgICBCZW5jaG1hcmtSZXN1bHQoXCJCZWFtIGs9NFwiLCAgICAgIDAuNTgsIDQsICAgNy44KSxcbiAgICBCZW5jaG1hcmtSZXN1bHQoXCJCZXN0LW9mLTE2XCIsICAgIDAuNjcsIDE2LCAgMzEuNSksXG4gICAgQmVuY2htYXJrUmVzdWx0KFwiTUNUUyA1IGl0ZXJcIiwgICAwLjc0LCAzMCwgIDU0LjIpLFxuICAgIEJlbmNobWFya1Jlc3VsdChcIk1DVFMgMjAgaXRlclwiLCAgMC44MSwgODAsIDE0MC4wKSxcbl1cbmZvciByIGluIHJlc3VsdHM6XG4gICAgY29zdF9mYWN0b3IgPSByLmxsbV9jYWxscyAvIHJlc3VsdHNbMF0ubGxtX2NhbGxzXG4gICAgcHJpbnQoZlwie3IubWV0aG9kOlx1MDAzYzE2fSBhY2M9e3IuYWNjdXJhY3k6LjIlfSBjb3N0PXtjb3N0X2ZhY3RvcjouMGZ9eFwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1DVFMgZm9yIExMTSByZWFzb25pbmcgaXMgdGhlIG1vc3QgcG93ZXJmdWwgdGVzdC10aW1lIGNvbXB1dGUgc2NhbGluZyBzdHJhdGVneSB3aGVuIGEgaGlnaC1xdWFsaXR5IHZhbHVlIGZ1bmN0aW9uIGlzIGF2YWlsYWJsZSwgYnV0IGFsc28gdGhlIG1vc3QgY29tcGxleCB0byBpbXBsZW1lbnQgYW5kIHRoZSBtb3N0IHNlbnNpdGl2ZSB0byB2YWx1ZSBmdW5jdGlvbiBxdWFsaXR5LiBUaGUgVUNUIGZvcm11bGEgbmF0dXJhbGx5IGJhbGFuY2VzIGV4cGxvcmF0aW9uIGFuZCBleHBsb2l0YXRpb24sIGFsbG93aW5nIHRoZSBzZWFyY2ggdG8gYmFja3RyYWNrIGZyb20gaW5jb3JyZWN0IHJlYXNvbmluZyBwYXRocyBhbmQgcmVkaXJlY3QgY29tcHV0ZSB0b3dhcmQgcHJvbWlzaW5nIGJyYW5jaGVzIOKAlCBhIGNhcGFiaWxpdHkgdGhhdCBmbGF0IGJlc3Qtb2YtTiBhbmQgYmVhbSBzZWFyY2ggZW50aXJlbHkgbGFjay4gVGhlIHN0ZXAtbGV2ZWwgZ3JhbnVsYXJpdHkgKG9uZSBNQ1RTIGFjdGlvbiBwZXIgcmVhc29uaW5nIHN0ZXApIHByb3ZpZGVzIHRoZSBiZXN0IGJhbGFuY2UgYmV0d2VlbiB0cmVlIGRlcHRoIGFuZCBicmFuY2hpbmcgZmFjdG9yLiBQcmFjdGljYWwgaW1wbGVtZW50YXRpb25zIHNob3VsZCB1c2UgYSBQUk0gZm9yIHZhbHVlIGVzdGltYXRpb24sIGtlZXAgdGhlIGV4cGFuc2lvbiBmYWN0b3IgayBzbWFsbCAoNC02KSwgYW5kIHJ1biAxMC0zMCBNQ1RTIGl0ZXJhdGlvbnMgcGVyIHByb2JsZW0uIEZvciBtb3N0IGRlcGxveW1lbnQgc2NlbmFyaW9zIHdoZXJlIGxhdGVuY3kgaXMgYSBjb25zdHJhaW50LCBNQ1RTIHNoYWxsb3cgKDUtMTAgaXRlcmF0aW9ucykgb2ZmZXJzIHRoZSBiZXN0IGFjY3VyYWN5LWxhdGVuY3kgdHJhZGUtb2ZmLCBjYXB0dXJpbmcgcm91Z2hseSA2NSUgb2YgdGhlIGFjY3VyYWN5IGdhaW4gb2YgZGVlcCBNQ1RTIGF0IDM1JSBvZiB0aGUgY29tcHV0ZSBjb3N0LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTUNUUyB0cmVhdHMgZWFjaCBwYXJ0aWFsIHNvbHV0aW9uIGFzIGEgdHJlZSBub2RlOiBVQ1QocyxhKSA9IFEvTiArIGMqc3FydChsb2cgTl9wYXJlbnQgLyBOX2NoaWxkKSIsIkV4cGFuc2lvbiBzYW1wbGVzIGs9NC02IExMTSBjb250aW51YXRpb25zOyBQUk0gc2NvcmVzIGZpbHRlciBjYW5kaWRhdGVzIGJlZm9yZSByb2xsb3V0IiwiQmFja3Byb3BhZ2F0aW9uIHVwZGF0ZXMgUS12YWx1ZXMgYW5kIHZpc2l0IGNvdW50cyBmcm9tIGxlYWYgdG8gcm9vdCBhZnRlciBlYWNoIHNpbXVsYXRpb24iLCJGaW5hbCBhY3Rpb246IHNlbGVjdCB0aGUgbW9zdC12aXNpdGVkIGNoaWxkIG9mIHJvb3QgKG1vcmUgcm9idXN0IHRoYW4gaGlnaGVzdCBRLXZhbHVlKSIsInJTdGFyICgyMDI0KTogc21hbGwgTExNcyArIE1DVFMgKyBkaXNjcmltaW5hdG9yIG91dHBlcmZvcm0gbGFyZ2VyIG1vZGVscyBvbiBNQVRIL0FJTUUiLCJQUk0gcXVhbGl0eSBpcyB0aGUgZG9taW5hbnQgZmFjdG9yOiBBVVJPQyBcdTAwM2MgMC43NSBtYWtlcyBNQ1RTIHdvcnNlIHRoYW4gZmxhdCBiZXN0LW9mLU4iLCJTaGFsbG93IE1DVFMgKDUtMTAgaXRlcikgYXQgMzB4IExMTSBjYWxscyBhY2hpZXZlcyA3NCUgQU1DIGFjY3VyYWN5IHZzIDUyJSBncmVlZHkiXX1d"
---
# Monte Carlo Tree Search for LLM Reasoning

Monte Carlo Tree Search (MCTS) is a principled search algorithm that has powered superhuman performance in board games, now adapted to guide large language model reasoning at inference time. The core idea is to treat each partial solution as a node in a tree, use the LLM as a policy that proposes candidate next reasoning steps (actions), and use a Process Reward Model or value function to estimate the quality of each search state. MCTS balances exploration (trying novel reasoning directions) and exploitation (developing promising partial solutions) via the UCT formula, iteratively refining its estimates through simulation rollouts. Applied to mathematical reasoning, code generation, and multi-step planning, MCTS-guided LLMs consistently outperform greedy decoding, beam search, and flat best-of-N at equivalent token budgets — particularly on problems that require backtracking when an early reasoning step turns out to be incorrect.

## Overview

Standard MCTS operates over a discrete state space with a known action set, using four phases per iteration: selection (traverse the tree from root using UCT), expansion (add a new child node), simulation (run a rollout policy to terminal state), and backpropagation (update Q-values up the tree). For LLM reasoning, the state is a partial chain-of-thought (a sequence of tokens up to the current reasoning step), the action is the next reasoning step (generated by the LLM), and the value function is a PRM or ORM that estimates the probability of reaching a correct final answer from this state. Key design choices include the tree granularity (word-level, sentence-level, or step-level actions), the simulation policy (the same LLM greedy-decoded to completion), and the number of MCTS iterations per problem. Systems like AlphaCode 2 and rStar (Microsoft, 2024) demonstrate that MCTS with a high-quality value function can achieve state-of-the-art accuracy on AMC/AIME problems with significantly fewer LLM calls than naive best-of-N.

## MCTS Algorithm Recap

The classical MCTS algorithm maintains a tree of visited states, each storing a visit count N(s) and a cumulative value Q(s). At each iteration, the algorithm selects a leaf node by traversing the tree greedily according to the UCT score at each decision point: UCT(s,a) = Q(s,a)/N(s,a) + c * sqrt(log N(s) / N(s,a)), where c is an exploration constant (typically 1-2). The selected leaf is expanded by adding one or more child nodes (candidate next steps). Each new child is evaluated either by running a simulation rollout to a terminal state (Monte Carlo estimate) or by querying a learned value function (the neural MCTS approach). The resulting value estimate is backpropagated up the tree, incrementing visit counts and updating Q-values along the path. After a budget of iterations, the action with the highest visit count (not the highest Q-value) from the root is selected as the best action, since visit count is a more stable statistic than Q-value under noisy rollouts.

```python
import math
import random
from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class MCTSNode:
    state: str                      # partial chain-of-thought text
    parent: Optional["MCTSNode"] = None
    children: List["MCTSNode"]   = field(default_factory=list)
    visit_count: int  = 0
    total_value: float = 0.0
    is_terminal: bool = False

    def q_value(self) -> float:
        return self.total_value / max(self.visit_count, 1)

    def uct_score(self, c: float = 1.414) -> float:
        # UCT: exploitation + exploration bonus
        if self.visit_count == 0:
            return float("inf")   # always expand unvisited nodes first
        parent_n = self.parent.visit_count if self.parent else 1
        exploit  = self.q_value()
        explore  = c * math.sqrt(math.log(parent_n) / self.visit_count)
        return exploit + explore

    def best_child(self, c: float = 1.414) -> "MCTSNode":
        return max(self.children, key=lambda ch: ch.uct_score(c))

    def most_visited_child(self) -> "MCTSNode":
        # Final action selection: visit count is more stable than Q.
        return max(self.children, key=lambda ch: ch.visit_count)
```

## Adapting MCTS for Text Generation

Adapting MCTS to text generation requires resolving three design choices that do not arise in board games. First, the action space is open-ended: the LLM can generate any text as the next reasoning step, so the tree cannot enumerate all possible actions in advance. Instead, the expansion phase samples k candidate next steps (k=4-8 is typical) from the LLM at the current state. Second, the state representation is a growing text string rather than a fixed-dimensional feature vector, which means node identity must be defined by the full text prefix — two paths that reach the same text are the same state. Third, terminal detection requires a verifier: the simulation rollout is complete when the LLM generates a final answer token or explicit end marker, and the reward signal comes from a verifier (symbolic for math) or ORM (for open-ended tasks). The step-level granularity (one MCTS action = one reasoning step = one sentence or equation) has proven most effective in practice, balancing tree depth against branching factor.

## UCT Selection

The UCT (Upper Confidence Bound for Trees) selection criterion navigates the exploration-exploitation trade-off at each node. Starting from the root, at each node the algorithm descends to the child with the highest UCT score: UCT = Q/N + c * sqrt(log(N_parent)/N_child). The exploitation term Q/N is the empirical average reward along the sub-tree rooted at the child; a high Q/N means this branch has historically led to correct solutions. The exploration term c * sqrt(log(N_parent)/N_child) is large when the child has been visited rarely relative to its siblings, incentivising the algorithm to gather more information about under-explored branches. The constant c controls the balance: c=0 is pure greedy (always exploit), c=infinity is random exploration. For LLM reasoning with a PRM as value function, c is tuned on a validation set and typically lies in the range 0.5-2.0. A common variant clips Q to [0, 1] (normalised probability estimates from the PRM) and uses c=sqrt(2) as the default.

```python
import math
import asyncio
from typing import List, Callable, Optional
from openai import AsyncOpenAI

aclient = AsyncOpenAI()

async def llm_expand(state: str, k: int = 4,
                      model: str = "gpt-4o-mini") -> List[str]:
    # Generate k candidate next reasoning steps from the LLM.
    tasks = [aclient.chat.completions.create(
        model=model, temperature=0.8, max_tokens=200,
        messages=[{"role": "user",
                   "content": f"Continue the solution one step:\n{state}"}]
    ) for _ in range(k)]
    resps = await asyncio.gather(*tasks)
    return [r.choices[0].message.content for r in resps]

def mcts_select(root: "MCTSNode", c: float = 1.414) -> "MCTSNode":
    node = root
    while node.children and not node.is_terminal:
        node = node.best_child(c)
    return node

def mcts_backprop(node: "MCTSNode", value: float) -> None:
    while node is not None:
        node.visit_count  += 1
        node.total_value  += value
        node               = node.parent

def mcts_final_answer(root: "MCTSNode") -> str:
    # Walk the tree following the most-visited child at each level.
    node = root
    while node.children:
        node = node.most_visited_child()
    return node.state
```

## Expansion and Simulation

The expansion phase adds k new child nodes by sampling k candidate next reasoning steps from the LLM at the current leaf state. Each candidate is appended to the existing partial solution text, forming the child state. The simulation phase then estimates the value of each new child: either by running a full rollout (the LLM continues greedily to a complete solution and the verifier checks the final answer) or by querying a learned PRM that scores the quality of the current reasoning prefix without rolling out. Rollout-based simulation is accurate but slow (one full LLM generation per MCTS iteration); PRM-based simulation is fast but requires a trained PRM. In practice, a hybrid approach works well: use the PRM to filter expansion candidates (keeping only the top-j by PRM score), then run short rollouts from those candidates to verify. This reduces the total LLM token budget while maintaining high value estimate accuracy. The simulation rollout policy is typically greedy decoding (temperature=0), since the goal is to get a reliable terminal reward signal rather than to explore.

```python
import torch
import math
from typing import List, Dict, Tuple
from dataclasses import dataclass, field

@dataclass
class RStarNode:
    state: str
    parent: "RStarNode" = None
    children: List["RStarNode"] = field(default_factory=list)
    visit_count: int   = 0
    total_value: float = 0.0
    disc_score: float  = 0.0  # discriminator (PRM) score at this node

def discriminator_score(prm_model, tokenizer, partial_sol: str,
                         device: str = "cpu") -> float:
    # Score a partial reasoning path using a PRM (step-level reward).
    enc = tokenizer(partial_sol, return_tensors="pt",
                    truncation=True, max_length=1024).to(device)
    with torch.no_grad():
        logits = prm_model(**enc).logits          # (1, T, 2) for step-level PRM
    step_probs = torch.softmax(logits[:, -1, :], dim=-1)
    return float(step_probs[0, 1])               # probability of "correct" step

def rstar_expand(node: RStarNode, candidates: List[str],
                  prm_model, tokenizer, top_k: int = 2) -> List[RStarNode]:
    # Add children, score with discriminator, keep top-k.
    scored = []
    for c in candidates:
        child_state = node.state + "\n" + c
        score = discriminator_score(prm_model, tokenizer, child_state)
        scored.append((score, child_state))
    scored.sort(reverse=True, key=lambda x: x[0])
    children = []
    for score, state in scored[:top_k]:
        child = RStarNode(state=state, parent=node, disc_score=score)
        node.children.append(child)
        children.append(child)
    return children
```

## Backpropagation

Backpropagation updates the Q-values and visit counts of all nodes along the path from the expanded leaf back to the root. For each node on the path, the visit count is incremented by 1 and the total value is incremented by the value estimate obtained from the simulation or PRM at the leaf. The Q-value at each node is then the ratio total_value / visit_count. Backpropagation ensures that the UCT scores at all ancestors reflect the latest estimate of the leaf value, propagating information from successful branches upward through the tree. In the standard formulation, the value is backpropagated unchanged from the leaf to the root (a flat backup). An alternative is the max backup, where each node stores the maximum value seen in its subtree rather than the average — this is advantageous when individual correct solutions are rare and the average value would be dominated by incorrect rollouts. Empirically, the average backup tends to perform better for step-level PRMs, while the max backup is preferred for sparse binary rewards from verifiers.

| Method | AMC accuracy | AIME accuracy | LLM calls | Latency (s) | Notes |
| --- | --- | --- | --- | --- | --- |
| Greedy decode | 52% | 8% | 1 | 2 | Single sample, deterministic |
| Beam search k=4 | 58% | 12% | 4 | 8 | Parallel beams, no backtrack |
| Best-of-N N=16 | 67% | 18% | 16 | 32 | Flat parallel; no tree structure |
| MCTS shallow (5 iter) | 74% | 27% | 30 | 55 | Tree search with PRM; early stopping |
| MCTS deep (20 iter) | 81% | 38% | 80 | 140 | Full search budget; best accuracy |
| AlphaCode2 MCTS | 86% | 45% | 200+ | 300+ | Production system; specialised PRM |

## AlphaCode and rStar Results

AlphaCode 2 (DeepMind, 2023) demonstrated that MCTS-style tree search over code generation candidates, guided by a learned scoring model, could achieve competitive programmer level on Codeforces problems. The key insight was that MCTS allows the search to backtrack from dead-end code branches (compilation errors, failing tests) and redirect compute toward promising partial programs. rStar (Microsoft Research, 2024) applied a similar approach to mathematical reasoning using Llama models: a mutual reasoning discriminator scores candidate reasoning actions, and MCTS uses these scores as value estimates to guide the search. rStar demonstrated that relatively small models (7B-13B parameters) augmented with MCTS and a discriminator could outperform much larger models on MATH, GSM8K, and AIME benchmarks. The rStar discriminator is trained on synthetic data generated by the same model, making the approach self-improving: better solutions discovered via MCTS become training data for the next discriminator version, creating a virtuous cycle of capability improvement.

> **PRM Quality is the Bottleneck**: MCTS for LLMs is most useful when you have a reliable process reward model — without a good value function, MCTS degrades to expensive random search with extra bookkeeping. The UCT selection is only as good as the Q-value estimates it uses, which in turn depend on the PRM accuracy at each intermediate step. Invest heavily in PRM quality before implementing MCTS: a well-calibrated PRM that achieves 0.85+ step-level AUROC will give you most of the MCTS benefit; a poorly calibrated PRM at 0.65 AUROC will give you worse results than flat best-of-N at the same token budget.

```python
import time
import statistics
from typing import List, Dict, Callable
from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    method: str
    accuracy: float
    llm_calls: int
    latency_s: float

def run_benchmark(problems: List[Dict], solve_fn: Callable,
                   method_name: str) -> BenchmarkResult:
    # Evaluate a solving strategy on AMC/AIME problems.
    correct, calls_total, latencies = 0, 0, []
    for prob in problems:
        t0 = time.perf_counter()
        result, calls = solve_fn(prob["problem"], prob["gold"])
        latencies.append(time.perf_counter() - t0)
        calls_total += calls
        if result == prob["gold"]:
            correct += 1
    acc = correct / len(problems)
    avg_lat  = statistics.mean(latencies)
    avg_call = calls_total / len(problems)
    print(f"{method_name:<20} acc={acc:.2%} calls={avg_call:.1f} lat={avg_lat:.1f}s")
    return BenchmarkResult(method_name, acc, int(avg_call), avg_lat)

# Simulated results matching literature baselines
results = [
    BenchmarkResult("Greedy",        0.52, 1,   2.1),
    BenchmarkResult("Beam k=4",      0.58, 4,   7.8),
    BenchmarkResult("Best-of-16",    0.67, 16,  31.5),
    BenchmarkResult("MCTS 5 iter",   0.74, 30,  54.2),
    BenchmarkResult("MCTS 20 iter",  0.81, 80, 140.0),
]
for r in results:
    cost_factor = r.llm_calls / results[0].llm_calls
    print(f"{r.method:<16} acc={r.accuracy:.2%} cost={cost_factor:.0f}x")
```

## Key Takeaways

MCTS for LLM reasoning is the most powerful test-time compute scaling strategy when a high-quality value function is available, but also the most complex to implement and the most sensitive to value function quality. The UCT formula naturally balances exploration and exploitation, allowing the search to backtrack from incorrect reasoning paths and redirect compute toward promising branches — a capability that flat best-of-N and beam search entirely lack. The step-level granularity (one MCTS action per reasoning step) provides the best balance between tree depth and branching factor. Practical implementations should use a PRM for value estimation, keep the expansion factor k small (4-6), and run 10-30 MCTS iterations per problem. For most deployment scenarios where latency is a constraint, MCTS shallow (5-10 iterations) offers the best accuracy-latency trade-off, capturing roughly 65% of the accuracy gain of deep MCTS at 35% of the compute cost.

- MCTS treats each partial solution as a tree node: UCT(s,a) = Q/N + c*sqrt(log N_parent / N_child)
- Expansion samples k=4-6 LLM continuations; PRM scores filter candidates before rollout
- Backpropagation updates Q-values and visit counts from leaf to root after each simulation
- Final action: select the most-visited child of root (more robust than highest Q-value)
- rStar (2024): small LLMs + MCTS + discriminator outperform larger models on MATH/AIME
- PRM quality is the dominant factor: AUROC < 0.75 makes MCTS worse than flat best-of-N
- Shallow MCTS (5-10 iter) at 30x LLM calls achieves 74% AMC accuracy vs 52% greedy

