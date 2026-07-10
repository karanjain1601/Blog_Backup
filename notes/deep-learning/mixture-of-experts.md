---
title: "Mixture of Experts (MoE) in LLMs"
slug: "mixture-of-experts"
description: "Scaling LLM capacity by replacing dense FFN layers with a bank of expert networks, routing each token to top-K experts to achieve high parameter count at low compute cost per token."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWl4dHVyZSBvZiBFeHBlcnRzIChNb0UpIGlzIGFuIGFyY2hpdGVjdHVyYWwgcGF0dGVybiB0aGF0IHJlcGxhY2VzIGVhY2ggZGVuc2UgZmVlZC1mb3J3YXJkIG5ldHdvcmsgKEZGTikgbGF5ZXIgaW4gYSB0cmFuc2Zvcm1lciB3aXRoIGEgYmFuayBvZiBOIGV4cGVydCBuZXR3b3JrcyBwbHVzIGEgbGVhcm5lZCByb3V0ZXIuIEZvciBlYWNoIHRva2VuLCB0aGUgcm91dGVyIHNlbGVjdHMgdGhlIHRvcC1LIGV4cGVydHMgYW5kIHNlbmRzIHRoZSB0b2tlbiBvbmx5IHRvIHRob3NlIGV4cGVydHM7IHRoZSBvdXRwdXRzIGFyZSBjb21iaW5lZCB3aXRoIHRoZSByb3V0aW5nIHdlaWdodHMuIEJlY2F1c2Ugb25seSBLIG91dCBvZiBOIGV4cGVydHMgYWN0aXZhdGUgcGVyIHRva2VuLCB0b3RhbCBwYXJhbWV0ZXIgY291bnQgZ3Jvd3Mgd2l0aCBOIHdoaWxlIGNvbXB1dGUgcGVyIHRva2VuIGdyb3dzIG9ubHkgd2l0aCBLIOKAlCBkZWNvdXBsaW5nIG1vZGVsIGNhcGFjaXR5IGZyb20gaW5mZXJlbmNlIGNvc3QuIE1vRSBoYXMgYmVjb21lIGNlbnRyYWwgdG8gc3RhdGUtb2YtdGhlLWFydCBMTE1zOiBNaXh0cmFsLCBEZWVwU2Vlay1WMiwgYW5kIHRoZSBlc3RpbWF0ZWQgYXJjaGl0ZWN0dXJlIG9mIEdQVC00IGFsbCB1c2UgTW9FIGxheWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGlkZWEgb2YgdXNpbmcgbXVsdGlwbGUgc3BlY2lhbGlzZWQgc3ViLW5ldHdvcmtzIGRhdGVzIHRvIEphY29icyBldCBhbC4gKDE5OTEpLCBidXQgbW9kZXJuIHNwYXJzZSBNb0UgZm9yIHRyYW5zZm9ybWVycyB3YXMgZXN0YWJsaXNoZWQgYnkgU2hhemVlciBldCBhbC4gKDIwMTcpIGluIFx1MDAyN091dHJhZ2VvdXNseSBMYXJnZSBOZXVyYWwgTmV0d29ya3M6IFRoZSBTcGFyc2VseS1HYXRlZCBNaXh0dXJlLW9mLUV4cGVydHMgTGF5ZXJcdTAwMjcuIFRoZSBhcmNoaXRlY3R1cmUgaW5zZXJ0cyBNb0UgbGF5ZXJzIGluIHBsYWNlIG9mIEZGTiBzdWJsYXllcnM7IGF0dGVudGlvbiBsYXllcnMgcmVtYWluIGRlbnNlIGFuZCBhcmUgc2hhcmVkIGFjcm9zcyBhbGwgdG9rZW5zLiBBIGxpbmVhciByb3V0ZXIgbWFwcyBlYWNoIHRva2VuIGVtYmVkZGluZyB0byBOIGV4cGVydCBsb2dpdHM7IHNvZnRtYXggZm9sbG93ZWQgYnkgdG9wLUsgc2VsZWN0aW9uIGRldGVybWluZXMgd2hpY2ggZXhwZXJ0cyBwcm9jZXNzIHRoZSB0b2tlbi4gR1NoYXJkIChMZXBpa2hpbiBldCBhbC4sIDIwMjEpIHNjYWxlZCB0aGlzIHRvIDYwMEIgcGFyYW1ldGVycyBvbiBUUFVzOyBTd2l0Y2ggVHJhbnNmb3JtZXIgKEZlZHVzIGV0IGFsLiwgMjAyMikgc2ltcGxpZmllZCB0aGUgZGVzaWduIHRvIHRvcC0xIHJvdXRpbmcgYW5kIHNob3dlZCB0aGF0IE1vRSBtb2RlbHMgbWF0Y2ggZGVuc2UgbW9kZWxzIGF0IDd4IGZld2VyIEZMT1BzLiBNaXh0cmFsLTh4N0IgKE1pc3RyYWwsIDIwMjMpIGJyb3VnaHQgb3Blbi13ZWlnaHQgTW9FIHRvIDQ3QiBwYXJhbWV0ZXJzIHdpdGggdG9wLTIgcm91dGluZywgbWF0Y2hpbmcgR1BULTMuNSBxdWFsaXR5IGF0IDEzQiBhY3RpdmUgcGFyYW1ldGVycyBwZXIgdG9rZW4uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9FIExheWVyIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gYSBzdGFuZGFyZCB0cmFuc2Zvcm1lciwgZWFjaCBsYXllciBhcHBsaWVzIG11bHRpLWhlYWQgYXR0ZW50aW9uIGZvbGxvd2VkIGJ5IGEgcG9zaXRpb24td2lzZSBGRk46IEZGTih4KSA9IFcyICogR0VMVShXMSAqIHgpLiBUaGUgRkZOIG9wZXJhdGVzIGlkZW50aWNhbGx5IG9uIGV2ZXJ5IHRva2VuLiBJbiBhbiBNb0UgbGF5ZXIsIHRoZSBzaW5nbGUgRkZOIGlzIHJlcGxhY2VkIGJ5IE4gZXhwZXJ0IEZGTnMge0VfMCwgLi4uLCBFX3tOLTF9fSBhbmQgYSByb3V0ZXIgRy4gRm9yIHRva2VuIHgsIHRoZSByb3V0ZXIgY29tcHV0ZXMgbG9naXRzIGggPSBXX3IgKiB4LCBjb252ZXJ0cyB0byBwcm9iYWJpbGl0aWVzIHAgPSBzb2Z0bWF4KGgpLCBzZWxlY3RzIHRoZSB0b3AtSyBpbmRpY2VzLCBhbmQgcHJvZHVjZXMgdGhlIG91dHB1dCBhcyBhIHdlaWdodGVkIHN1bSBvZiBzZWxlY3RlZCBleHBlcnQgb3V0cHV0czogTW9FKHgpID0gc3VtX3trIGluIHRvcC1LfSBwX2sgKiBFX2soeCkuIFRoZSByb3V0ZXIgYW5kIGFsbCBleHBlcnRzIHNoYXJlIHRoZSBzYW1lIGlucHV0IGRpbWVuc2lvbiBkX21vZGVsOyBleHBlcnQgaGlkZGVuIGRpbWVuc2lvbnMgYXJlIG9mdGVuIGlkZW50aWNhbCB0byB0aGUgZGVuc2UgRkZOXHUwMDI3cyBoaWRkZW4gZGltZW5zaW9uLCB0aG91Z2ggaW4gZmluZS1ncmFpbmVkIE1vRSB0aGV5IG1heSBiZSBzbWFsbGVyLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBNb0VMYXllcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsOiBpbnQsIGRfZmY6IGludCwgbl9leHBlcnRzOiBpbnQsIHRvcF9rOiBpbnQgPSAyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubl9leHBlcnRzLCBzZWxmLnRvcF9rID0gbl9leHBlcnRzLCB0b3Bfa1xuICAgICAgICBzZWxmLnJvdXRlciA9IG5uLkxpbmVhcihkX21vZGVsLCBuX2V4cGVydHMsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuZXhwZXJ0cyA9IG5uLk1vZHVsZUxpc3QoW1xuICAgICAgICAgICAgbm4uU2VxdWVudGlhbChubi5MaW5lYXIoZF9tb2RlbCwgZF9mZiksIG5uLkdFTFUoKSwgbm4uTGluZWFyKGRfZmYsIGRfbW9kZWwpKVxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9leHBlcnRzKV0pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBCLCBULCBEID0geC5zaGFwZVxuICAgICAgICB4ZiA9IHgudmlldygtMSwgRCkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyAoTiwgRClcbiAgICAgICAgbG9naXRzID0gc2VsZi5yb3V0ZXIoeGYpICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKE4sIEUpXG4gICAgICAgIHByb2JzLCBpbmRpY2VzID0gdG9yY2gudG9wayhGLnNvZnRtYXgobG9naXRzLCAtMSksIHNlbGYudG9wX2ssIGRpbT0tMSlcbiAgICAgICAgcHJvYnMgPSBwcm9icyAvIHByb2JzLnN1bSgtMSwga2VlcGRpbT1UcnVlKSAgICAgICAgICMgcmVub3JtYWxpc2UgdG9wLUtcbiAgICAgICAgb3V0ID0gdG9yY2guemVyb3NfbGlrZSh4ZilcbiAgICAgICAgZm9yIGsgaW4gcmFuZ2Uoc2VsZi50b3Bfayk6XG4gICAgICAgICAgICBmb3IgZSBpbiByYW5nZShzZWxmLm5fZXhwZXJ0cyk6XG4gICAgICAgICAgICAgICAgbWFzayA9IGluZGljZXNbOiwga10gPT0gZVxuICAgICAgICAgICAgICAgIGlmIG1hc2suYW55KCk6XG4gICAgICAgICAgICAgICAgICAgIG91dFttYXNrXSArPSBwcm9ic1ttYXNrLCBrOmsrMV0gKiBzZWxmLmV4cGVydHNbZV0oeGZbbWFza10pXG4gICAgICAgIHJldHVybiBvdXQudmlldyhCLCBULCBEKVxuXG5sYXllciA9IE1vRUxheWVyKGRfbW9kZWw9NTEyLCBkX2ZmPTIwNDgsIG5fZXhwZXJ0cz04LCB0b3Bfaz0yKVxucHJpbnQobGF5ZXIodG9yY2gucmFuZG4oMiwgMTYsIDUxMikpLnNoYXBlKSAgIyAoMiwgMTYsIDUxMikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUb3AtSyBSb3V0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcm91dGVyIGlzIGEgc2luZ2xlIGxpbmVhciBsYXllciB0aGF0IG1hcHMgZF9tb2RlbCDihpIgbl9leHBlcnRzLiBBZnRlciBzb2Z0bWF4LCB0aGUgdG9wLUsgdmFsdWVzIGRldGVybWluZSBib3RoIHdoaWNoIGV4cGVydHMgcmVjZWl2ZSB0aGUgdG9rZW4gYW5kIHdpdGggd2hhdCB3ZWlnaHQuIFRoZSBjaG9pY2Ugb2YgSyBjcmVhdGVzIGEgZnVuZGFtZW50YWwgdHJhZGUtb2ZmOiBLPTEgKFN3aXRjaCBUcmFuc2Zvcm1lcikgbWluaW1pc2VzIGNvbXB1dGUgYW5kIGNvbW11bmljYXRpb24gYnV0IGxvc2VzIHRoZSBhdmVyYWdpbmcgYmVuZWZpdCBvZiBtdWx0aXBsZSBleHBlcnRzOyBLPTIgKE1peHRyYWwsIEdTaGFyZCkgaXMgdGhlIG1vc3QgY29tbW9uIGNob2ljZSBhbmQgcHJvdmlkZXMgYmV0dGVyIGdyYWRpZW50IGZsb3cgYW5kIHN0YWJpbGl0eTsgS1x1MDAzZTIgc3RhcnRzIHRvIGJsdXIgdGhlIHNwYXJzaXR5IGJlbmVmaXQuIFRoZSBzb2Z0bWF4IGlzIGNvbXB1dGVkIG92ZXIgYWxsIE4gZXhwZXJ0cyBldmVuIHRob3VnaCBvbmx5IEsgYXJlIHNlbGVjdGVkLCBzbyB0aGUgcm91dGVyIGl0c2VsZiBpcyBPKE4pIOKAlCB0aG91Z2ggTiBpcyB0eXBpY2FsbHkgOOKAkzY0IHNvIHRoaXMgY29zdCBpcyBuZWdsaWdpYmxlLiBTb21lIGRlc2lnbnMgdXNlIGEgc2lnbW9pZCBpbnN0ZWFkIG9mIHNvZnRtYXggZm9yIHJvdXRpbmcgKHVzZWQgaW4gRGVlcFNlZWstVjIpIHRvIGFsbG93IGluZGVwZW5kZW50IHBlci1leHBlcnQgc2NvcmVzIHJhdGhlciB0aGFuIGEgemVyby1zdW0gY29tcGV0aXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgdG9wX2tfcm91dGVyKHg6IHRvcmNoLlRlbnNvciwgV19yb3V0ZXI6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgdG9wX2s6IGludCwgbm9pc2Vfc3RkOiBmbG9hdCA9IDAuMCkgLVx1MDAzZSB0dXBsZTpcbiAgICBcIlwiXCJUb2tlbi1jaG9pY2UgdG9wLUsgcm91dGluZyB3aXRoIG9wdGlvbmFsIGppdHRlciBub2lzZSAoU2hhemVlciAyMDE3KS5cbiAgICB4OiAoYmF0Y2gqc2VxLCBkX21vZGVsKSAgIFdfcm91dGVyOiAoZF9tb2RlbCwgbl9leHBlcnRzKVxuICAgIFJldHVybnM6IHdlaWdodHMgKE4sIEspIGFuZCBleHBlcnQgaW5kaWNlcyAoTiwgSykuXCJcIlwiXG4gICAgbG9naXRzID0geCBAIFdfcm91dGVyICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIChOLCBFKVxuICAgIGlmIG5vaXNlX3N0ZCBcdTAwM2UgMCBhbmQgdG9yY2guaXNfZ3JhZF9lbmFibGVkKCk6XG4gICAgICAgIGxvZ2l0cyA9IGxvZ2l0cyArIHRvcmNoLnJhbmRuX2xpa2UobG9naXRzKSAqIG5vaXNlX3N0ZFxuICAgIHByb2JzID0gRi5zb2Z0bWF4KGxvZ2l0cywgZGltPS0xKSAgICAgICAgICAgICAgICAgICAgICAgIyAoTiwgRSlcbiAgICB3ZWlnaHRzLCBpbmRpY2VzID0gdG9yY2gudG9wayhwcm9icywgdG9wX2ssIGRpbT0tMSkgICAgICMgKE4sIEspIGVhY2hcbiAgICB3ZWlnaHRzID0gd2VpZ2h0cyAvIHdlaWdodHMuc3VtKC0xLCBrZWVwZGltPVRydWUpICAgICAgICMgcmVub3JtYWxpc2VcbiAgICByZXR1cm4gd2VpZ2h0cywgaW5kaWNlc1xuXG4jIERlbW86IDggZXhwZXJ0cywgdG9wLTIsIGJhdGNoIG9mIDQgdG9rZW5zXG5kX21vZGVsLCBuX2V4cGVydHMsIHRvcF9rID0gMjU2LCA4LCAyXG5XID0gdG9yY2gucmFuZG4oZF9tb2RlbCwgbl9leHBlcnRzKSAqIDAuMDJcbnggPSB0b3JjaC5yYW5kbig0LCBkX21vZGVsKVxudywgaWR4ID0gdG9wX2tfcm91dGVyKHgsIFcsIHRvcF9rKVxucHJpbnQoZlwiU2VsZWN0ZWQgZXhwZXJ0cyBwZXIgdG9rZW46IHtpZHgudG9saXN0KCl9XCIpXG5wcmludChmXCJSb3V0aW5nIHdlaWdodHM6ICAgICAgICAgICAge3cucm91bmQoZGVjaW1hbHM9MykudG9saXN0KCl9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9hZCBCYWxhbmNpbmcgTG9zcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aG91dCBleHBsaWNpdCByZWd1bGFyaXNhdGlvbiwgdGhlIHJvdXRlciBxdWlja2x5IGNvbGxhcHNlczogYSBmZXcgZXhwZXJ0cyBjb25zaXN0ZW50bHkgcmVjZWl2ZSB0aGUgaGlnaGVzdCBsb2dpdHMsIGFyZSBzZWxlY3RlZCBieSBtb3N0IHRva2VucywgYW5kIHRodXMgcmVjZWl2ZSB0aGUgbW9zdCBncmFkaWVudCBzaWduYWwsIHJlaW5mb3JjaW5nIHRoZWlyIGRvbWluYW5jZS4gVGhpcyBleHBlcnQgY29sbGFwc2UgbGVhdmVzIG1vc3QgZXhwZXJ0cyB1bmRlcnRyYWluZWQuIFN3aXRjaCBUcmFuc2Zvcm1lciBhbmQgR1NoYXJkIGFkZHJlc3MgdGhpcyB3aXRoIGFuIGF1eGlsaWFyeSBsb2FkLWJhbGFuY2luZyBsb3NzIHRoYXQgcGVuYWxpc2VzIGRldmlhdGlvbiBmcm9tIHVuaWZvcm0gZXhwZXJ0IHV0aWxpc2F0aW9uLiBUaGUgbG9zcyBpcyBhZGRlZCB0byB0aGUgbGFuZ3VhZ2UtbW9kZWxsaW5nIGxvc3Mgd2l0aCBhIHNtYWxsIGNvZWZmaWNpZW50IGFscGhhICh0eXBpY2FsbHkgMWUtMikuIFRoZSBzdGFuZGFyZCBmb3JtdWxhdGlvbiBjb21wdXRlcyBmX2kgKGZyYWN0aW9uIG9mIHRva2VucyBkaXNwYXRjaGVkIHRvIGV4cGVydCBpKSBhbmQgUF9pIChtZWFuIHJvdXRpbmcgcHJvYmFiaWxpdHkgZm9yIGV4cGVydCBpKSwgdGhlbiBwZW5hbGlzZXMgdGhlaXIgaW5uZXIgcHJvZHVjdCBzY2FsZWQgYnkgTjogYXV4X2xvc3MgPSBOICogc3VtKGZfaSAqIFBfaSkuIEEgcGVyZmVjdGx5IGJhbGFuY2VkIHJvdXRlciBnaXZlcyBhdXhfbG9zcyA9IDEgcmVnYXJkbGVzcyBvZiBOLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGF1eGlsaWFyeV9sb2FkX2JhbGFuY2VfbG9zcyhyb3V0ZXJfbG9naXRzOiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBleHBlcnRfaW5kaWNlczogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9leHBlcnRzOiBpbnQsIGFscGhhOiBmbG9hdCA9IDFlLTIpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlN3aXRjaCBUcmFuc2Zvcm1lciAvIEdTaGFyZCBhdXhpbGlhcnkgbG9hZC1iYWxhbmNpbmcgbG9zcy5cbiAgICByb3V0ZXJfbG9naXRzOiAoTiwgRSkgIGV4cGVydF9pbmRpY2VzOiAoTiwgdG9wX2spIExvbmdUZW5zb3IuXCJcIlwiXG4gICAgcHJvYnMgPSBGLnNvZnRtYXgocm91dGVyX2xvZ2l0cywgZGltPS0xKSAgICAgICAgICAgICAgICAjIChOLCBFKVxuICAgICMgRnJhY3Rpb24gb2YgdG9rZW5zIHJvdXRlZCB0byBlYWNoIGV4cGVydCAodXNlIHRvcC0xIGZvciBkaXNwYXRjaCBmcmFjdGlvbilcbiAgICBvbmVob3QgPSBGLm9uZV9ob3QoZXhwZXJ0X2luZGljZXNbOiwgMF0sIG5fZXhwZXJ0cykuZmxvYXQoKSAgIyAoTiwgRSlcbiAgICBmX2kgPSBvbmVob3QubWVhbihkaW09MCkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgKEUsKVxuICAgIFBfaSA9IHByb2JzLm1lYW4oZGltPTApICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIyAoRSwpXG4gICAgYXV4X2xvc3MgPSBuX2V4cGVydHMgKiAoZl9pICogUF9pKS5zdW0oKVxuICAgIHJldHVybiBhbHBoYSAqIGF1eF9sb3NzXG5cbmRlZiBjb21iaW5lZF9sb3NzKGxtX2xvc3MsIHJvdXRlcl9sb2dpdHMsIGV4cGVydF9pbmRpY2VzLCBuX2V4cGVydHMpOlxuICAgIFwiXCJcIlRvdGFsIHRyYWluaW5nIGxvc3M6IGxhbmd1YWdlLW1vZGVsIGxvc3MgKyBsb2FkLWJhbGFuY2luZyBhdXhpbGlhcnkgbG9zcy5cIlwiXCJcbiAgICBsYiA9IGF1eGlsaWFyeV9sb2FkX2JhbGFuY2VfbG9zcyhyb3V0ZXJfbG9naXRzLCBleHBlcnRfaW5kaWNlcywgbl9leHBlcnRzKVxuICAgIHJldHVybiBsbV9sb3NzICsgbGIsIGxiLml0ZW0oKVxuXG4jIFNpbXVsYXRlIGEgYmFsYW5jZWQgdnMgY29sbGFwc2VkIHJvdXRlclxuYmFsYW5jZWQgID0gdG9yY2guemVyb3MoMzIsIDgpOyBiYWxhbmNlZC5zY2F0dGVyXygxLCB0b3JjaC5yYW5kaW50KDAsOCwoMzIsMSkpLCA1LjApXG5jb2xsYXBzZWQgPSB0b3JjaC56ZXJvcygzMiwgOCk7IGNvbGxhcHNlZFs6LCAwXSA9IDUuMFxuZm9yIG5hbWUsIGxvZ2l0cyBpbiBbKFwiYmFsYW5jZWRcIiwgYmFsYW5jZWQpLCAoXCJjb2xsYXBzZWRcIiwgY29sbGFwc2VkKV06XG4gICAgaWR4ID0gdG9yY2gudG9wayhsb2dpdHMsIDIsIGRpbT0tMSkuaW5kaWNlc1xuICAgIGxiICA9IGF1eGlsaWFyeV9sb2FkX2JhbGFuY2VfbG9zcyhsb2dpdHMsIGlkeCwgbl9leHBlcnRzPTgsIGFscGhhPTEuMClcbiAgICBwcmludChmXCJ7bmFtZTpcdTAwM2UxMH06IGF1eF9sb3NzID0ge2xiLml0ZW0oKTouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXhwZXJ0IFNwZWNpYWxpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZXNwaXRlIHRoZSB1bnN1cGVydmlzZWQgbmF0dXJlIG9mIHRoZSByb3V0ZXIsIE1vRSBleHBlcnRzIHNwb250YW5lb3VzbHkgc3BlY2lhbGlzZSBkdXJpbmcgdHJhaW5pbmcuIEFuYWx5c2VzIG9mIE1peHRyYWwtOHg3QiBhbmQgU3dpdGNoIFRyYW5zZm9ybWVyIHNob3cgdGhhdCBleHBlcnRzIHNwZWNpYWxpc2UgYWNyb3NzIGRvbWFpbnMgKGNvZGUsIG1hdGgsIG5hdHVyYWwgbGFuZ3VhZ2UpLCBzeW50YWN0aWMgcm9sZXMgKHZlcmJzLCBwdW5jdHVhdGlvbiwgbmFtZWQgZW50aXRpZXMpLCBhbmQgZnJlcXVlbmN5IGJhbmRzIChjb21tb24gdnMgcmFyZSB0b2tlbnMpLiBUaGlzIHNwZWNpYWxpc2F0aW9uIGVtZXJnZXMgZnJvbSB0aGUgdHJhaW5pbmcgZHluYW1pY3M6IGlmIGV4cGVydCBBIGlzIGJldHRlciBhdCBjb2RlIHRva2VucywgaXQgcmVjZWl2ZXMgbW9yZSBncmFkaWVudCBzaWduYWwgZnJvbSBjb2RlIHNlcXVlbmNlcywgZnVydGhlciBpbXByb3ZpbmcgaXRzIGNvZGUgY2FwYWJpbGl0eS4gVGhlIHJvdXRlciBsZWFybnMgdG8gcm91dGUgY29kZSB0b2tlbnMgdG8gZXhwZXJ0IEEsIHdoaWNoIGluIHR1cm4gc3BlY2lhbGlzZXMgZnVydGhlciDigJQgYSBwb3NpdGl2ZSBmZWVkYmFjayBsb29wLiBUaGlzIHNlbGYtb3JnYW5pc2F0aW9uIGlzIHdoeSBsb2FkIGJhbGFuY2luZyBtYXR0ZXJzOiBpZiBleHBlcnQgQSBtb25vcG9saXNlcyBhbGwgdG9rZW5zLCBvdGhlciBleHBlcnRzIG5ldmVyIGRldmVsb3Agc3BlY2lhbGlzYXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5jbGFzcyBFeHBlcnRVdGlsaXphdGlvblRyYWNrZXI6XG4gICAgXCJcIlwiVHJhY2sgcGVyLWV4cGVydCB0b2tlbiBjb3VudHMgYW5kIGNvbXB1dGUgbG9hZCBzdGF0aXN0aWNzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2V4cGVydHM6IGludCk6XG4gICAgICAgIHNlbGYuY291bnRzID0gdG9yY2guemVyb3Mobl9leHBlcnRzKVxuICAgICAgICBzZWxmLm5fZXhwZXJ0cyA9IG5fZXhwZXJ0c1xuXG4gICAgZGVmIHVwZGF0ZShzZWxmLCBpbmRpY2VzOiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgTm9uZTpcbiAgICAgICAgXCJcIlwiaW5kaWNlczogKE4sIHRvcF9rKSBMb25nVGVuc29yIG9mIHNlbGVjdGVkIGV4cGVydCBpZHMuXCJcIlwiXG4gICAgICAgIGZvciBlIGluIHJhbmdlKHNlbGYubl9leHBlcnRzKTpcbiAgICAgICAgICAgIHNlbGYuY291bnRzW2VdICs9IChpbmRpY2VzID09IGUpLnN1bSgpLmZsb2F0KClcblxuICAgIGRlZiBzdGF0cyhzZWxmKSAtXHUwMDNlIGRpY3Q6XG4gICAgICAgIGxvYWQgPSBzZWxmLmNvdW50cyAvIHNlbGYuY291bnRzLnN1bSgpXG4gICAgICAgIGlkZWFsID0gMS4wIC8gc2VsZi5uX2V4cGVydHNcbiAgICAgICAgZW50cm9weSA9IC0obG9hZCAqIChsb2FkICsgMWUtOSkubG9nKCkpLnN1bSgpLml0ZW0oKVxuICAgICAgICBtYXhfZSAgID0gbnAubG9nKHNlbGYubl9leHBlcnRzKVxuICAgICAgICBjdiAgICAgID0gKGxvYWQuc3RkKCkgLyBsb2FkLm1lYW4oKSkuaXRlbSgpXG4gICAgICAgIHJldHVybiB7XCJub3JtYWxpc2VkX2VudHJvcHlcIjogZW50cm9weSAvIG1heF9lLCBcImN2XCI6IGN2LFxuICAgICAgICAgICAgICAgIFwibWF4X2xvYWRcIjogbG9hZC5tYXgoKS5pdGVtKCksIFwibWluX2xvYWRcIjogbG9hZC5taW4oKS5pdGVtKCl9XG5cbnRyYWNrZXIgPSBFeHBlcnRVdGlsaXphdGlvblRyYWNrZXIoOClcbiMgU2ltdWxhdGUgMTAwIGJhdGNoZXMgb2YgMzIgdG9rZW5zLCB0b3AtMiByb3V0aW5nXG5mb3IgXyBpbiByYW5nZSgxMDApOlxuICAgIHRyYWNrZXIudXBkYXRlKHRvcmNoLnJhbmRpbnQoMCwgOCwgKDMyLCAyKSkpXG5wcmludCh0cmFja2VyLnN0YXRzKCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR1NoYXJkIGFuZCBTd2l0Y2ggVHJhbnNmb3JtZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdTaGFyZCAoTGVwaWtoaW4gZXQgYWwuLCAyMDIxKSB3YXMgdGhlIGZpcnN0IGRlbW9uc3RyYXRpb24gb2YgdHJpbGxpb24tcGFyYW1ldGVyLXNjYWxlIE1vRSB0cmFpbmluZywgcmVhY2hpbmcgNjAwQiBwYXJhbWV0ZXJzIHdpdGggdG9wLTIgcm91dGluZyBhY3Jvc3MgMjA0OCBUUFUgY29yZXMuIEl0IGludHJvZHVjZWQgY2FwYWNpdHkgZmFjdG9yIOKAlCBhIHBlci1leHBlcnQgYnVmZmVyIHRoYXQgbGltaXRzIGhvdyBtYW55IHRva2VucyBjYW4gYmUgcHJvY2Vzc2VkIHBlciBleHBlcnQgcGVyIGJhdGNoLCBkcm9wcGluZyBvdmVyZmxvdyB0b2tlbnMuIFN3aXRjaCBUcmFuc2Zvcm1lciAoRmVkdXMgZXQgYWwuLCAyMDIyKSBzaW1wbGlmaWVkIHRoZSBhcmNoaXRlY3R1cmUgdG8gdG9wLTEgcm91dGluZyBhbmQgc2hvd2VkIHRoYXQgdGhlIGNvbXBsZXhpdHkgb2YgdG9wLUsgKEtcdTAwM2UxKSBpcyB1bm5lY2Vzc2FyeTogd2l0aCBnb29kIGxvYWQgYmFsYW5jaW5nLCB0b3AtMSBtYXRjaGVzIHRvcC0yIHF1YWxpdHkgYXQgbG93ZXIgcm91dGluZyBjb3N0LiBCb3RoIHBhcGVycyBlc3RhYmxpc2hlZCB0aGUga2V5IE1vRSB0cmFpbmluZyBwcmluY2lwbGVzOiBhdXhpbGlhcnkgYmFsYW5jaW5nIGxvc3MsIGNhcGFjaXR5IGZhY3RvcnMgZm9yIGhhcmR3YXJlIGVmZmljaWVuY3ksIGFuZCB0aGUgRkxPUHMvcXVhbGl0eSBzY2FsaW5nIGxhd3MgdGhhdCBmYXZvdXIgc3BhcnNlIG92ZXIgZGVuc2UgYXQgZml4ZWQgY29tcHV0ZSBidWRnZXQuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiVG90YWwgcGFyYW1zIiwiQWN0aXZlIHBhcmFtcyIsIkV4cGVydHMiLCJUb3AtSyIsIkZMT1BzL3Rva2VuIl0sInJvd3MiOltbIlN3aXRjaC1DIiwiMS42VCIsIn43QiIsIjIwNDgiLCIxIiwifjdCIGVxdWl2LiJdLFsiTWl4dHJhbC04eDdCIiwiNDdCIiwiMTNCIiwiOCIsIjIiLCIxM0IgZXF1aXYuIl0sWyJNaXh0cmFsLTh4MjJCIiwiMTQxQiIsIjM5QiIsIjgiLCIyIiwiMzlCIGVxdWl2LiJdLFsiRGVlcFNlZWstVjIiLCIyMzZCIiwiMjFCIiwiMTYwIiwiNiIsIjIxQiBlcXVpdi4iXSxbIkdQVC00IChlc3QuKSIsIn4xLjhUIiwifjExMEIiLCJ+MTYiLCJ+MiIsIn4xMTBCIGVxdWl2LiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3BhcnNlIHZzIERlbnNlIFRyYWRlb2ZmcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTW9FIG1vZGVscyBvZmZlciBoaWdoIGNhcGFjaXR5IGF0IGxvdyBwZXItdG9rZW4gRkxPUHMgYnV0IGludHJvZHVjZSBjb3N0czogKDEpIE1lbW9yeSDigJQgYWxsIGV4cGVydHMgbXVzdCByZXNpZGUgaW4gR1BVIG1lbW9yeSBldmVuIHRob3VnaCBvbmx5IEsgYXJlIGFjdGl2ZSBwZXIgdG9rZW47IE1peHRyYWwtOHg3QiByZXF1aXJlcyB+OTBHQiB0byBsb2FkIGFsbCB3ZWlnaHRzIGluIGJmMTYuICgyKSBDb21tdW5pY2F0aW9uIOKAlCBpbiBkaXN0cmlidXRlZCB0cmFpbmluZywgdG9rZW5zIG11c3QgYmUgcm91dGVkIHRvIHRoZSBjb3JyZWN0IGV4cGVydFx1MDAyN3MgZGV2aWNlIChhbGwtdG8tYWxsIGNvbGxlY3RpdmUpLCBhZGRpbmcgaW50ZXItZGV2aWNlIGxhdGVuY3kgdGhhdCBjYW4gYm90dGxlbmVjayB0cmFpbmluZyB0aHJvdWdocHV0LiAoMykgQmF0Y2gtc2l6ZSBzZW5zaXRpdml0eSDigJQgTW9FIGVmZmljaWVuY3kgaW1wcm92ZXMgYXQgbGFyZ2UgYmF0Y2ggc2l6ZXMgc2luY2UgbWFueSB0b2tlbnMgY2FuIGJlIHByb2Nlc3NlZCBieSBlYWNoIGV4cGVydCBpbiBwYXJhbGxlbDsgYXQgc21hbGwgYmF0Y2hlcyAoaW5mZXJlbmNlKSwgZXhwZXJ0IHV0aWxpc2F0aW9uIGRyb3BzIGFuZCBoYXJkd2FyZSB1dGlsaXNhdGlvbiBzdWZmZXJzLiAoNCkgTG9hZCBpbWJhbGFuY2Ug4oCUIHVuZGVyIGRpc3RyaWJ1dGlvbiBzaGlmdCAoZGlmZmVyZW50IGluZmVyZW5jZSBkb21haW4gZnJvbSB0cmFpbmluZyksIGxvYWQgY2FuIGJlY29tZSB1bmV2ZW4sIHRyaWdnZXJpbmcgdG9rZW4gZHJvcHBpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgZXN0aW1hdGVfbW9lX2Nvc3QoZF9tb2RlbDogaW50LCBkX2ZmOiBpbnQsIG5fZXhwZXJ0czogaW50LFxuICAgICAgICAgICAgICAgICAgICAgdG9wX2s6IGludCwgbl9sYXllcnM6IGludCwgc2VxX2xlbjogaW50KSAtXHUwMDNlIGRpY3Q6XG4gICAgXCJcIlwiRXN0aW1hdGUgcGVyLWZvcndhcmQtcGFzcyBGTE9QcyBhbmQgcGFyYW1ldGVyIGNvdW50cyBmb3IgTW9FIHZzIGRlbnNlLlwiXCJcIlxuICAgICMgRGVuc2UgRkZOOiB0d28gbGluZWFyIGxheWVycyAoZF9tb2RlbC1cdTAwM2VkX2ZmLVx1MDAzZWRfbW9kZWwpIHBlciB0b2tlbiBwZXIgbGF5ZXJcbiAgICBkZW5zZV9mbG9wcyAgPSAyICogZF9tb2RlbCAqIGRfZmYgKiAyICogc2VxX2xlbiAqIG5fbGF5ZXJzICAgICAjIDIgZm9yIGZ3ZFxuICAgIGRlbnNlX3BhcmFtcyA9IDIgKiBkX21vZGVsICogZF9mZiAqIG5fbGF5ZXJzXG4gICAgIyBNb0UgRkZOOiB0b3BfayBhY3RpdmUgZXhwZXJ0cyBwZXIgdG9rZW47IHRvdGFsIHBhcmFtcyBzY2FsZSB3aXRoIG5fZXhwZXJ0c1xuICAgIG1vZV9mbG9wcyAgICA9IDIgKiBkX21vZGVsICogZF9mZiAqIHRvcF9rICogMiAqIHNlcV9sZW4gKiBuX2xheWVyc1xuICAgIG1vZV9wYXJhbXNfYWN0aXZlID0gMiAqIGRfbW9kZWwgKiBkX2ZmICogdG9wX2sgKiBuX2xheWVycyAgICAgICMgYWN0aXZlIG9ubHlcbiAgICBtb2VfcGFyYW1zX3RvdGFsICA9IDIgKiBkX21vZGVsICogZF9mZiAqIG5fZXhwZXJ0cyAqIG5fbGF5ZXJzICAgIyBhbGwgZXhwZXJ0c1xuICAgIHJldHVybiB7XG4gICAgICAgIFwiZGVuc2VfZmxvcHNfR1wiOiBkZW5zZV9mbG9wcyAvIDFlOSxcbiAgICAgICAgXCJtb2VfZmxvcHNfR1wiOiAgIG1vZV9mbG9wcyAgIC8gMWU5LFxuICAgICAgICBcImRlbnNlX3BhcmFtc19CXCI6ICAgICAgZGVuc2VfcGFyYW1zIC8gMWU5LFxuICAgICAgICBcIm1vZV9hY3RpdmVfcGFyYW1zX0JcIjogbW9lX3BhcmFtc19hY3RpdmUgLyAxZTksXG4gICAgICAgIFwibW9lX3RvdGFsX3BhcmFtc19CXCI6ICBtb2VfcGFyYW1zX3RvdGFsIC8gMWU5LFxuICAgICAgICBcImZsb3BfcmF0aW9cIjogbW9lX2Zsb3BzIC8gZGVuc2VfZmxvcHMsXG4gICAgfVxuXG5mb3IgbmUgaW4gWzEsIDgsIDY0XTpcbiAgICByID0gZXN0aW1hdGVfbW9lX2Nvc3QoNDA5NiwgMTQzMzYsIG5lLCBtaW4obmUsMiksIDMyLCAyMDQ4KVxuICAgIHByaW50KGZcIkU9e25lOlx1MDAzZTN9OiBkZW5zZT17cltcdTAwMjdkZW5zZV9mbG9wc19HXHUwMDI3XTouMGZ9RyAgbW9lPXtyW1x1MDAyN21vZV9mbG9wc19HXHUwMDI3XTouMGZ9RyAgXCJcbiAgICAgICAgICBmXCJ0b3RhbF9wYXJhbXM9e3JbXHUwMDI3bW9lX3RvdGFsX3BhcmFtc19CXHUwMDI3XTouMWZ9QiAgYWN0aXZlPXtyW1x1MDAyN21vZV9hY3RpdmVfcGFyYW1zX0JcdTAwMjddOi4xZn1CXCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJTcGFyc2UgYnV0IFBvd2VyZnVsIiwiY29udGVudCI6Ik1vRSBtb2RlbHMgYXJlIFx1MDAyN3NwYXJzZVx1MDAyNyDigJQgTWl4dHJhbCA4eDdCIGhhcyA0N0IgdG90YWwgcGFyYW1ldGVycyBidXQgb25seSAxM0IgYWN0aXZhdGUgcGVyIHRva2VuLCBnaXZpbmcgfkdQVC0zLjUtbGV2ZWwgY29tcHV0ZSBhdCB+R1BULTQtbGV2ZWwgY2FwYWNpdHkuIFRoZSBrZXkgaW5zaWdodDogcGFyYW1ldGVyIGNvdW50IGNvbnRyb2xzIG1vZGVsIGtub3dsZWRnZSwgd2hpbGUgYWN0aXZlIHBhcmFtZXRlcnMgY29udHJvbCBpbmZlcmVuY2UgY29zdC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb0UgaXMgdGhlIGRvbWluYW50IGFyY2hpdGVjdHVyZSBmb3Igc2NhbGluZyBMTE0gY2FwYWNpdHkgYmV5b25kIHRoZSBsaW1pdHMgb2YgZGVuc2UgdHJhaW5pbmcgY29tcHV0ZS4gQnkgY29uZGl0aW9uYWxseSBhY3RpdmF0aW5nIG9ubHkgSyBvZiBOIGV4cGVydHMgcGVyIHRva2VuLCBNb0UgZGVjb3VwbGVzIHRvdGFsIHBhcmFtZXRlciBjb3VudCAod2hpY2ggZGV0ZXJtaW5lcyBtb2RlbCBxdWFsaXR5KSBmcm9tIHBlci10b2tlbiBGTE9QcyAod2hpY2ggZGV0ZXJtaW5lIHRyYWluaW5nIGFuZCBpbmZlcmVuY2UgY29zdCkuIFRoZSBwcmltYXJ5IGNoYWxsZW5nZXMgYXJlIGV4cGVydCBjb2xsYXBzZSAoc29sdmVkIHdpdGggYXV4aWxpYXJ5IGxvYWQtYmFsYW5jaW5nIGxvc3MpLCBtZW1vcnkgY29zdCAoYWxsIGV4cGVydHMgbXVzdCBiZSBsb2FkZWQpLCBhbmQgY29tbXVuaWNhdGlvbiBvdmVyaGVhZCBpbiBkaXN0cmlidXRlZCB0cmFpbmluZy4gVG9wLTIgcm91dGluZyB3aXRoIGFuIGF1eGlsaWFyeSBsb3NzIGNvZWZmaWNpZW50IG9mIDFlLTIgaXMgdGhlIG1vc3QgY29tbW9uIHJlY2lwZSwgYXMgdXNlZCBpbiBNaXh0cmFsIGFuZCBEZWVwU2Vlay1WMi4gRmluZS1ncmFpbmVkIHZhcmlhbnRzIChtYW55IHNtYWxsIGV4cGVydHMpIGFuZCBzaGFyZWQgZXhwZXJ0cyBhcmUgYWN0aXZlIHJlc2VhcmNoIGRpcmVjdGlvbnMgdGhhdCBpbXByb3ZlIHNwZWNpYWxpc2F0aW9uIGFuZCBrbm93bGVkZ2UgY292ZXJhZ2UuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJSZXBsYWNlIGRlbnNlIEZGTiB3aXRoIE4gZXhwZXJ0IEZGTnMgYW5kIGEgbGluZWFyIHJvdXRlcjsgYWN0aXZhdGUgb25seSB0b3AtSyBwZXIgdG9rZW4iLCJUb3AtSz0yIGlzIHRoZSBzdGFuZGFyZCBjaG9pY2U7IHRvcC0xIChTd2l0Y2ggVHJhbnNmb3JtZXIpIGlzIHNpbXBsZXIgYnV0IHNsaWdodGx5IHdlYWtlciIsIkF1eGlsaWFyeSBsb2FkLWJhbGFuY2luZyBsb3NzIChhbHBoYX4xZS0yKSBpcyBtYW5kYXRvcnkgdG8gcHJldmVudCBleHBlcnQgY29sbGFwc2UiLCJUb3RhbCBwYXJhbXMgc2NhbGUgd2l0aCBOOyBhY3RpdmUgcGFyYW1zIHNjYWxlIHdpdGggSyDigJQgbWVtb3J5IGNvc3QgaXMgTiwgY29tcHV0ZSBjb3N0IGlzIEsiLCJFeHBlcnRzIHNwb250YW5lb3VzbHkgc3BlY2lhbGlzZSBieSBkb21haW4sIHN5bnRheCwgYW5kIHRva2VuIGZyZXF1ZW5jeSIsIk1vRSBpcyB1c2VkIGluIE1peHRyYWwsIERlZXBTZWVrLVYyLCBHUFQtNCAoZXN0aW1hdGVkKSwgYW5kIFN3aXRjaCBUcmFuc2Zvcm1lciJdfV0="
---
# Mixture of Experts (MoE) in LLMs

Mixture of Experts (MoE) is an architectural pattern that replaces each dense feed-forward network (FFN) layer in a transformer with a bank of N expert networks plus a learned router. For each token, the router selects the top-K experts and sends the token only to those experts; the outputs are combined with the routing weights. Because only K out of N experts activate per token, total parameter count grows with N while compute per token grows only with K — decoupling model capacity from inference cost. MoE has become central to state-of-the-art LLMs: Mixtral, DeepSeek-V2, and the estimated architecture of GPT-4 all use MoE layers.

## Overview

The idea of using multiple specialised sub-networks dates to Jacobs et al. (1991), but modern sparse MoE for transformers was established by Shazeer et al. (2017) in 'Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer'. The architecture inserts MoE layers in place of FFN sublayers; attention layers remain dense and are shared across all tokens. A linear router maps each token embedding to N expert logits; softmax followed by top-K selection determines which experts process the token. GShard (Lepikhin et al., 2021) scaled this to 600B parameters on TPUs; Switch Transformer (Fedus et al., 2022) simplified the design to top-1 routing and showed that MoE models match dense models at 7x fewer FLOPs. Mixtral-8x7B (Mistral, 2023) brought open-weight MoE to 47B parameters with top-2 routing, matching GPT-3.5 quality at 13B active parameters per token.

## MoE Layer Architecture

In a standard transformer, each layer applies multi-head attention followed by a position-wise FFN: FFN(x) = W2 * GELU(W1 * x). The FFN operates identically on every token. In an MoE layer, the single FFN is replaced by N expert FFNs {E_0, ..., E_{N-1}} and a router G. For token x, the router computes logits h = W_r * x, converts to probabilities p = softmax(h), selects the top-K indices, and produces the output as a weighted sum of selected expert outputs: MoE(x) = sum_{k in top-K} p_k * E_k(x). The router and all experts share the same input dimension d_model; expert hidden dimensions are often identical to the dense FFN's hidden dimension, though in fine-grained MoE they may be smaller.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MoELayer(nn.Module):
    def __init__(self, d_model: int, d_ff: int, n_experts: int, top_k: int = 2):
        super().__init__()
        self.n_experts, self.top_k = n_experts, top_k
        self.router = nn.Linear(d_model, n_experts, bias=False)
        self.experts = nn.ModuleList([
            nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(), nn.Linear(d_ff, d_model))
            for _ in range(n_experts)])

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, D = x.shape
        xf = x.view(-1, D)                                  # (N, D)
        logits = self.router(xf)                            # (N, E)
        probs, indices = torch.topk(F.softmax(logits, -1), self.top_k, dim=-1)
        probs = probs / probs.sum(-1, keepdim=True)         # renormalise top-K
        out = torch.zeros_like(xf)
        for k in range(self.top_k):
            for e in range(self.n_experts):
                mask = indices[:, k] == e
                if mask.any():
                    out[mask] += probs[mask, k:k+1] * self.experts[e](xf[mask])
        return out.view(B, T, D)

layer = MoELayer(d_model=512, d_ff=2048, n_experts=8, top_k=2)
print(layer(torch.randn(2, 16, 512)).shape)  # (2, 16, 512)
```

## Top-K Routing

The router is a single linear layer that maps d_model → n_experts. After softmax, the top-K values determine both which experts receive the token and with what weight. The choice of K creates a fundamental trade-off: K=1 (Switch Transformer) minimises compute and communication but loses the averaging benefit of multiple experts; K=2 (Mixtral, GShard) is the most common choice and provides better gradient flow and stability; K>2 starts to blur the sparsity benefit. The softmax is computed over all N experts even though only K are selected, so the router itself is O(N) — though N is typically 8–64 so this cost is negligible. Some designs use a sigmoid instead of softmax for routing (used in DeepSeek-V2) to allow independent per-expert scores rather than a zero-sum competition.

```python
import torch
import torch.nn.functional as F

def top_k_router(x: torch.Tensor, W_router: torch.Tensor,
                 top_k: int, noise_std: float = 0.0) -> tuple:
    """Token-choice top-K routing with optional jitter noise (Shazeer 2017).
    x: (batch*seq, d_model)   W_router: (d_model, n_experts)
    Returns: weights (N, K) and expert indices (N, K)."""
    logits = x @ W_router                                   # (N, E)
    if noise_std > 0 and torch.is_grad_enabled():
        logits = logits + torch.randn_like(logits) * noise_std
    probs = F.softmax(logits, dim=-1)                       # (N, E)
    weights, indices = torch.topk(probs, top_k, dim=-1)     # (N, K) each
    weights = weights / weights.sum(-1, keepdim=True)       # renormalise
    return weights, indices

# Demo: 8 experts, top-2, batch of 4 tokens
d_model, n_experts, top_k = 256, 8, 2
W = torch.randn(d_model, n_experts) * 0.02
x = torch.randn(4, d_model)
w, idx = top_k_router(x, W, top_k)
print(f"Selected experts per token: {idx.tolist()}")
print(f"Routing weights:            {w.round(decimals=3).tolist()}")
```

## Load Balancing Loss

Without explicit regularisation, the router quickly collapses: a few experts consistently receive the highest logits, are selected by most tokens, and thus receive the most gradient signal, reinforcing their dominance. This expert collapse leaves most experts undertrained. Switch Transformer and GShard address this with an auxiliary load-balancing loss that penalises deviation from uniform expert utilisation. The loss is added to the language-modelling loss with a small coefficient alpha (typically 1e-2). The standard formulation computes f_i (fraction of tokens dispatched to expert i) and P_i (mean routing probability for expert i), then penalises their inner product scaled by N: aux_loss = N * sum(f_i * P_i). A perfectly balanced router gives aux_loss = 1 regardless of N.

```python
import torch
import torch.nn.functional as F

def auxiliary_load_balance_loss(router_logits: torch.Tensor,
                                 expert_indices: torch.Tensor,
                                 n_experts: int, alpha: float = 1e-2) -> torch.Tensor:
    """Switch Transformer / GShard auxiliary load-balancing loss.
    router_logits: (N, E)  expert_indices: (N, top_k) LongTensor."""
    probs = F.softmax(router_logits, dim=-1)                # (N, E)
    # Fraction of tokens routed to each expert (use top-1 for dispatch fraction)
    onehot = F.one_hot(expert_indices[:, 0], n_experts).float()  # (N, E)
    f_i = onehot.mean(dim=0)                                # (E,)
    P_i = probs.mean(dim=0)                                 # (E,)
    aux_loss = n_experts * (f_i * P_i).sum()
    return alpha * aux_loss

def combined_loss(lm_loss, router_logits, expert_indices, n_experts):
    """Total training loss: language-model loss + load-balancing auxiliary loss."""
    lb = auxiliary_load_balance_loss(router_logits, expert_indices, n_experts)
    return lm_loss + lb, lb.item()

# Simulate a balanced vs collapsed router
balanced  = torch.zeros(32, 8); balanced.scatter_(1, torch.randint(0,8,(32,1)), 5.0)
collapsed = torch.zeros(32, 8); collapsed[:, 0] = 5.0
for name, logits in [("balanced", balanced), ("collapsed", collapsed)]:
    idx = torch.topk(logits, 2, dim=-1).indices
    lb  = auxiliary_load_balance_loss(logits, idx, n_experts=8, alpha=1.0)
    print(f"{name:>10}: aux_loss = {lb.item():.4f}")
```

## Expert Specialization

Despite the unsupervised nature of the router, MoE experts spontaneously specialise during training. Analyses of Mixtral-8x7B and Switch Transformer show that experts specialise across domains (code, math, natural language), syntactic roles (verbs, punctuation, named entities), and frequency bands (common vs rare tokens). This specialisation emerges from the training dynamics: if expert A is better at code tokens, it receives more gradient signal from code sequences, further improving its code capability. The router learns to route code tokens to expert A, which in turn specialises further — a positive feedback loop. This self-organisation is why load balancing matters: if expert A monopolises all tokens, other experts never develop specialisations.

```python
import torch
import numpy as np

class ExpertUtilizationTracker:
    """Track per-expert token counts and compute load statistics."""
    def __init__(self, n_experts: int):
        self.counts = torch.zeros(n_experts)
        self.n_experts = n_experts

    def update(self, indices: torch.Tensor) -> None:
        """indices: (N, top_k) LongTensor of selected expert ids."""
        for e in range(self.n_experts):
            self.counts[e] += (indices == e).sum().float()

    def stats(self) -> dict:
        load = self.counts / self.counts.sum()
        ideal = 1.0 / self.n_experts
        entropy = -(load * (load + 1e-9).log()).sum().item()
        max_e   = np.log(self.n_experts)
        cv      = (load.std() / load.mean()).item()
        return {"normalised_entropy": entropy / max_e, "cv": cv,
                "max_load": load.max().item(), "min_load": load.min().item()}

tracker = ExpertUtilizationTracker(8)
# Simulate 100 batches of 32 tokens, top-2 routing
for _ in range(100):
    tracker.update(torch.randint(0, 8, (32, 2)))
print(tracker.stats())
```

## GShard and Switch Transformer

GShard (Lepikhin et al., 2021) was the first demonstration of trillion-parameter-scale MoE training, reaching 600B parameters with top-2 routing across 2048 TPU cores. It introduced capacity factor — a per-expert buffer that limits how many tokens can be processed per expert per batch, dropping overflow tokens. Switch Transformer (Fedus et al., 2022) simplified the architecture to top-1 routing and showed that the complexity of top-K (K>1) is unnecessary: with good load balancing, top-1 matches top-2 quality at lower routing cost. Both papers established the key MoE training principles: auxiliary balancing loss, capacity factors for hardware efficiency, and the FLOPs/quality scaling laws that favour sparse over dense at fixed compute budget.

| Model | Total params | Active params | Experts | Top-K | FLOPs/token |
| --- | --- | --- | --- | --- | --- |
| Switch-C | 1.6T | ~7B | 2048 | 1 | ~7B equiv. |
| Mixtral-8x7B | 47B | 13B | 8 | 2 | 13B equiv. |
| Mixtral-8x22B | 141B | 39B | 8 | 2 | 39B equiv. |
| DeepSeek-V2 | 236B | 21B | 160 | 6 | 21B equiv. |
| GPT-4 (est.) | ~1.8T | ~110B | ~16 | ~2 | ~110B equiv. |

## Sparse vs Dense Tradeoffs

MoE models offer high capacity at low per-token FLOPs but introduce costs: (1) Memory — all experts must reside in GPU memory even though only K are active per token; Mixtral-8x7B requires ~90GB to load all weights in bf16. (2) Communication — in distributed training, tokens must be routed to the correct expert's device (all-to-all collective), adding inter-device latency that can bottleneck training throughput. (3) Batch-size sensitivity — MoE efficiency improves at large batch sizes since many tokens can be processed by each expert in parallel; at small batches (inference), expert utilisation drops and hardware utilisation suffers. (4) Load imbalance — under distribution shift (different inference domain from training), load can become uneven, triggering token dropping.

```python
import torch

def estimate_moe_cost(d_model: int, d_ff: int, n_experts: int,
                     top_k: int, n_layers: int, seq_len: int) -> dict:
    """Estimate per-forward-pass FLOPs and parameter counts for MoE vs dense."""
    # Dense FFN: two linear layers (d_model->d_ff->d_model) per token per layer
    dense_flops  = 2 * d_model * d_ff * 2 * seq_len * n_layers     # 2 for fwd
    dense_params = 2 * d_model * d_ff * n_layers
    # MoE FFN: top_k active experts per token; total params scale with n_experts
    moe_flops    = 2 * d_model * d_ff * top_k * 2 * seq_len * n_layers
    moe_params_active = 2 * d_model * d_ff * top_k * n_layers      # active only
    moe_params_total  = 2 * d_model * d_ff * n_experts * n_layers   # all experts
    return {
        "dense_flops_G": dense_flops / 1e9,
        "moe_flops_G":   moe_flops   / 1e9,
        "dense_params_B":      dense_params / 1e9,
        "moe_active_params_B": moe_params_active / 1e9,
        "moe_total_params_B":  moe_params_total / 1e9,
        "flop_ratio": moe_flops / dense_flops,
    }

for ne in [1, 8, 64]:
    r = estimate_moe_cost(4096, 14336, ne, min(ne,2), 32, 2048)
    print(f"E={ne:>3}: dense={r['dense_flops_G']:.0f}G  moe={r['moe_flops_G']:.0f}G  "
          f"total_params={r['moe_total_params_B']:.1f}B  active={r['moe_active_params_B']:.1f}B")
```

> **Sparse but Powerful**: MoE models are 'sparse' — Mixtral 8x7B has 47B total parameters but only 13B activate per token, giving ~GPT-3.5-level compute at ~GPT-4-level capacity. The key insight: parameter count controls model knowledge, while active parameters control inference cost.

## Key Takeaways

MoE is the dominant architecture for scaling LLM capacity beyond the limits of dense training compute. By conditionally activating only K of N experts per token, MoE decouples total parameter count (which determines model quality) from per-token FLOPs (which determine training and inference cost). The primary challenges are expert collapse (solved with auxiliary load-balancing loss), memory cost (all experts must be loaded), and communication overhead in distributed training. Top-2 routing with an auxiliary loss coefficient of 1e-2 is the most common recipe, as used in Mixtral and DeepSeek-V2. Fine-grained variants (many small experts) and shared experts are active research directions that improve specialisation and knowledge coverage.

- Replace dense FFN with N expert FFNs and a linear router; activate only top-K per token
- Top-K=2 is the standard choice; top-1 (Switch Transformer) is simpler but slightly weaker
- Auxiliary load-balancing loss (alpha~1e-2) is mandatory to prevent expert collapse
- Total params scale with N; active params scale with K — memory cost is N, compute cost is K
- Experts spontaneously specialise by domain, syntax, and token frequency
- MoE is used in Mixtral, DeepSeek-V2, GPT-4 (estimated), and Switch Transformer

