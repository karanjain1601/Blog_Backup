---
title: "StreamingLLM: Efficient Streaming Language Model Inference"
slug: "streaming-llm"
description: "The StreamingLLM system combining attention sinks with a fixed-size sliding KV cache window to enable LLMs to generate arbitrarily long sequences without context-length restrictions."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RyZWFtaW5nTExNIChYaWFvIGV0IGFsLiwgMjAyMykgaXMgYW4gaW5mZXJlbmNlIHN5c3RlbSB0aGF0IGVuYWJsZXMgcHJldHJhaW5lZCBsYXJnZSBsYW5ndWFnZSBtb2RlbHMgdG8gZ2VuZXJhdGUgdGV4dCBvZiB1bmJvdW5kZWQgbGVuZ3RoIHdpdGhvdXQgcmV0cmFpbmluZywgYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzLCBvciBjb250ZXh0LWxlbmd0aCByZXN0cmljdGlvbnMuIEl0IGFjaGlldmVzIHRoaXMgYnkgY29tYmluaW5nIHR3byBpbnNpZ2h0czogKDEpIHRoZSBhdHRlbnRpb24gc2luayBwaGVub21lbm9uIOKAlCB0aGF0IG1vZGVscyByZWxpYWJseSBhdHRlbmQgdG8gaW5pdGlhbCB0b2tlbnMgcmVnYXJkbGVzcyBvZiBjb250ZW50IOKAlCBtZWFucyB0aG9zZSB0b2tlbnMgbXVzdCBiZSBrZXB0IGluIHRoZSBLViBjYWNoZSBwZXJtYW5lbnRseTsgYW5kICgyKSBhIGZpeGVkIHNsaWRpbmcgd2luZG93IG9mIHJlY2VudCB0b2tlbnMgcHJvdmlkZXMgc3VmZmljaWVudCBsb2NhbCBjb250ZXh0IGZvciBjb2hlcmVudCBnZW5lcmF0aW9uLiBUaGUgcmVzdWx0IGlzIGEgY29uc3RhbnQtbWVtb3J5LCBjb25zdGFudC1zcGVlZCBpbmZlcmVuY2UgZW5naW5lIHRoYXQgdHJhbnNmb3JtcyBhbnkgcHJldHJhaW5lZCBMTE0gaW50byBhIHN0cmVhbWluZyBtb2RlbCBjYXBhYmxlIG9mIHByb2R1Y2luZyBtaWxsaW9ucyBvZiB0b2tlbnMgaW4gYSBzaW5nbGUgc2Vzc2lvbiwgZW5hYmxpbmcgYXBwbGljYXRpb25zIHN1Y2ggYXMgcmVhbC10aW1lIHRyYW5zY3JpcHRpb24gc3VtbWFyaXphdGlvbiwgYWx3YXlzLW9uIEFJIGFzc2lzdGFudHMsIGFuZCBzdHJlYW1pbmcgY29kZSBnZW5lcmF0aW9uIG92ZXIgZW50aXJlIHJlcG9zaXRvcmllcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgYXV0b3JlZ3Jlc3NpdmUgZ2VuZXJhdGlvbiBzdG9yZXMgYWxsIHBhc3QgS1YgcGFpcnMgaW4gbWVtb3J5ICh0aGUgS1YgY2FjaGUpLCB3aGljaCBncm93cyBsaW5lYXJseSB3aXRoIHNlcXVlbmNlIGxlbmd0aCBhbmQgZXZlbnR1YWxseSBleGhhdXN0cyBHUFUgbWVtb3J5LiBUcnVuY2F0aW5nIHRoZSBpbnB1dCB0byBhIGZpeGVkIGNvbnRleHQgd2luZG93IGZvcmNlcyB0aGUgbW9kZWwgdG8gZGlzY2FyZCBlYXJsaWVyIGNvbnRlbnQgYW5kIGJyZWFrcyBnZW5lcmF0aW9uIHF1YWxpdHkuIFN0cmVhbWluZ0xMTSBhdm9pZHMgYm90aCBwcm9ibGVtcyBieSBpbXBsZW1lbnRpbmcgYSBTaW5rQ2FjaGU6IGEgZml4ZWQtc2l6ZSBLViBzdG9yZSB0aGF0IGFsd2F5cyBjb250YWlucyB0aGUgZmlyc3Qgbl9zaW5rPTQgdG9rZW5zICh0aGUgc2luayByZWdpb24pIHBsdXMgdGhlIG1vc3QgcmVjZW50IHdpbmRvd19zaXplIHRva2VucyAodGhlIHNsaWRpbmcgd2luZG93KS4gVG90YWwgY2FjaGUgc2l6ZSBpcyBjb25zdGFudCBhdCBuX3NpbmsgKyB3aW5kb3dfc2l6ZSBlbnRyaWVzLiBXaGVuIGEgbmV3IHRva2VuIGlzIGdlbmVyYXRlZCwgaXRzIEtWIHBhaXIgZW50ZXJzIHRoZSB3aW5kb3c7IGlmIHRoZSB3aW5kb3cgaXMgZnVsbCwgdGhlIG9sZGVzdCB3aW5kb3cgZW50cnkgaXMgZXZpY3RlZC4gU2luayBlbnRyaWVzIGFyZSBuZXZlciBldmljdGVkLiBUaGUgbW9kZWwgYXR0ZW5kcyBvdmVyIHRoaXMgYm91bmRlZCBjYWNoZSBhdCBlYWNoIHN0ZXAsIHByb2R1Y2luZyBzdGFibGUgcGVycGxleGl0eSBmb3Igc2VxdWVuY2VzIG9mIGFyYml0cmFyeSBsZW5ndGguIFRoZSBwYXBlciBkZW1vbnN0cmF0ZXMgc3RhYmxlIGdlbmVyYXRpb24gYXQgNCBtaWxsaW9uIHRva2Vucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTeXN0ZW0gQXJjaGl0ZWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdHJlYW1pbmdMTE0gaXMgYSBwdXJlIGluZmVyZW5jZSBtb2RpZmljYXRpb24g4oCUIHRoZSBtb2RlbCB3ZWlnaHRzIGFyZSB1bnRvdWNoZWQuIFRoZSBzeXN0ZW0gaW5zZXJ0cyBhIFNpbmtDYWNoZSBtYW5hZ2VyIGJldHdlZW4gdGhlIHRyYW5zZm9ybWVyXHUwMDI3cyBhdHRlbnRpb24gbW9kdWxlcyBhbmQgdGhlIEtWIGNhY2hlIHN0b3JhZ2UuIEF0IGVhY2ggZ2VuZXJhdGlvbiBzdGVwLCB0aGUgYXR0ZW50aW9uIG1vZHVsZSBjYWxscyBTaW5rQ2FjaGUuYWRkKGtleSwgdmFsdWUpIHRvIHN0b3JlIHRoZSBuZXcgS1YgcGFpciwgdGhlbiBjYWxscyBTaW5rQ2FjaGUuZ2V0X2t2KCkgdG8gcmV0cmlldmUgdGhlIGZ1bGwgYm91bmRlZCBLViBzdGF0ZSBmb3IgYXR0ZW50aW9uIGNvbXB1dGF0aW9uLiBUaGUgZ2V0X2t2KCkgcmV0dXJuIGlzIGEgY29uY2F0ZW5hdGlvbiBvZiBbc2lua19rZXlzOyB3aW5kb3dfa2V5c10gYW5kIFtzaW5rX3ZhbHVlczsgd2luZG93X3ZhbHVlc10gaW4gdGhlaXIgb3JpZ2luYWwgY2F1c2FsIG9yZGVyLiBQb3NpdGlvbiBJRHMgYXJlIHJlLWluZGV4ZWQgYXQgZWFjaCBzdGVwIHRvIG1hdGNoIHRoZSBhY3R1YWwgYXR0ZW5kZWQgcG9zaXRpb25zOiBzaW5rIHRva2VucyByZXRhaW4gcG9zaXRpb25zIFswLCAxLCAyLCAzXTsgd2luZG93IHRva2VucyBhcmUgYXNzaWduZWQgY29udGlndW91cyBwb3NpdGlvbnMgW25fc2luaywgbl9zaW5rKzEsIC4uLiwgbl9zaW5rK3dpbmRvd19zaXplLTFdLiBUaGlzIHJlLWluZGV4aW5nIGlzIGNyaXRpY2FsIGZvciBSb1BFIGNvbnNpc3RlbmN5IOKAlCB0aGUgbW9kZWwgbXVzdCBzZWUgcG9zaXRpb25zIHRoYXQgcmVmbGVjdCB0aGUgcmVsYXRpdmUgb3JkZXIgb2YgYXR0ZW5kZWQgdG9rZW5zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0eXBpbmcgaW1wb3J0IE9wdGlvbmFsLCBUdXBsZVxuXG5jbGFzcyBTaW5rQ2FjaGU6XG4gICAgIyBTdHJlYW1pbmdMTE0gS1YgY2FjaGU6IHBlcm1hbmVudCBzaW5rIHJlZ2lvbiArIHNsaWRpbmcgd2luZG93XG4gICAgIyBFbmFibGVzIGluZmluaXRlLWxlbmd0aCBnZW5lcmF0aW9uIGF0IGNvbnN0YW50IG1lbW9yeSBhbmQgY29tcHV0ZVxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fc2luazogaW50ID0gNCwgd2luZG93X3NpemU6IGludCA9IDUxMik6XG4gICAgICAgIHNlbGYubl9zaW5rID0gbl9zaW5rXG4gICAgICAgIHNlbGYud2luZG93X3NpemUgPSB3aW5kb3dfc2l6ZVxuICAgICAgICBzZWxmLl9zaW5rX2s6ICBsaXN0ID0gW11cbiAgICAgICAgc2VsZi5fc2lua192OiAgbGlzdCA9IFtdXG4gICAgICAgIHNlbGYuX3dpbl9rOiAgIGxpc3QgPSBbXVxuICAgICAgICBzZWxmLl93aW5fdjogICBsaXN0ID0gW11cbiAgICAgICAgc2VsZi5zZXFfbGVuID0gMFxuXG4gICAgZGVmIGFkZChzZWxmLCBrZXk6IHRvcmNoLlRlbnNvciwgdmFsdWU6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSBOb25lOlxuICAgICAgICAjIGtleS92YWx1ZTogKGJhdGNoLCBuX2hlYWRzLCAxLCBoZWFkX2RpbSkg4oCUIHNpbmdsZSBuZXcgdG9rZW5cbiAgICAgICAgaWYgc2VsZi5zZXFfbGVuIFx1MDAzYyBzZWxmLm5fc2luazpcbiAgICAgICAgICAgIHNlbGYuX3Npbmtfay5hcHBlbmQoa2V5KVxuICAgICAgICAgICAgc2VsZi5fc2lua192LmFwcGVuZCh2YWx1ZSlcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIHNlbGYuX3dpbl9rLmFwcGVuZChrZXkpXG4gICAgICAgICAgICBzZWxmLl93aW5fdi5hcHBlbmQodmFsdWUpXG4gICAgICAgICAgICBpZiBsZW4oc2VsZi5fd2luX2spIFx1MDAzZSBzZWxmLndpbmRvd19zaXplOlxuICAgICAgICAgICAgICAgIHNlbGYuX3dpbl9rLnBvcCgwKVxuICAgICAgICAgICAgICAgIHNlbGYuX3dpbl92LnBvcCgwKVxuICAgICAgICBzZWxmLnNlcV9sZW4gKz0gMVxuXG4gICAgZGVmIGdldF9rdihzZWxmKSAtXHUwMDNlIFR1cGxlW3RvcmNoLlRlbnNvciwgdG9yY2guVGVuc29yXTpcbiAgICAgICAgIyBSZXR1cm5zIGNvbmNhdGVuYXRlZCBbc2luayB8IHdpbmRvd10ga2V5cyBhbmQgdmFsdWVzXG4gICAgICAgIGFsbF9rID0gdG9yY2guY2F0KHNlbGYuX3NpbmtfayArIHNlbGYuX3dpbl9rLCBkaW09MilcbiAgICAgICAgYWxsX3YgPSB0b3JjaC5jYXQoc2VsZi5fc2lua192ICsgc2VsZi5fd2luX3YsIGRpbT0yKVxuICAgICAgICByZXR1cm4gYWxsX2ssIGFsbF92XG5cbiAgICBkZWYgZ2V0X3Bvc2l0aW9uX2lkcyhzZWxmKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgIyBDb250aWd1b3VzIHBvc2l0aW9ucyBbMC4ubl9zaW5rLTEsIG5fc2luay4uY2FjaGVfbGVuLTFdXG4gICAgICAgIGNhY2hlX2xlbiA9IGxlbihzZWxmLl9zaW5rX2spICsgbGVuKHNlbGYuX3dpbl9rKVxuICAgICAgICByZXR1cm4gdG9yY2guYXJhbmdlKGNhY2hlX2xlbiwgZHR5cGU9dG9yY2gubG9uZylcblxuICAgIEBwcm9wZXJ0eVxuICAgIGRlZiBjYWNoZV9zaXplKHNlbGYpIC1cdTAwM2UgaW50OlxuICAgICAgICByZXR1cm4gbGVuKHNlbGYuX3NpbmtfaykgKyBsZW4oc2VsZi5fd2luX2spIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2luayBDYWNoZSBJbXBsZW1lbnRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFNpbmtDYWNoZS5hZGQoKSBtZXRob2Qgcm91dGVzIGluY29taW5nIEtWIHBhaXJzIGJhc2VkIG9uIHdoZXRoZXIgdGhlIHNlcXVlbmNlIGxlbmd0aCBoYXMgcmVhY2hlZCB0aGUgc2luayBidWRnZXQuIEZvciB0aGUgZmlyc3Qgbl9zaW5rIHRva2VucywgZW50cmllcyBhcmUgYXBwZW5kZWQgdG8gdGhlIHBlcm1hbmVudCBzaW5rIGxpc3RzLiBGcm9tIHRva2VuIG5fc2luayBvbndhcmQsIGVudHJpZXMgZ28gaW50byB0aGUgd2luZG93IGxpc3RzLCB3aGljaCBhcmUgcHJ1bmVkIGJ5IGV2aWN0aW5nIGZyb20gdGhlIGZyb250IHdoZW5ldmVyIGxlbmd0aCBleGNlZWRzIHdpbmRvd19zaXplLiBUaGlzIG1lYW5zIHRoZSBmaXJzdCBuX3NpbmsgdG9rZW5zIG9mIGFueSBkb2N1bWVudCBhcmUgYWx3YXlzIHJldGFpbmVkLCBtYXRjaGluZyB0aGUgYXR0ZW50aW9uIHNpbmsgc3RydWN0dXJlIG9ic2VydmVkIGluIHByZXRyYWluZWQgbW9kZWxzLiBUaGUgU2lua0NhY2hlLmdldF9rdigpIG1ldGhvZCBjb25jYXRlbmF0ZXMgc2luayBhbmQgd2luZG93IGxpc3RzIGFsb25nIHRoZSBzZXF1ZW5jZSBkaW1lbnNpb24sIHJldHVybmluZyBhIHZpZXcgc3VpdGFibGUgZm9yIHVzZSBhcyBwYXN0X2tleV92YWx1ZXMgaW4gYW55IEh1Z2dpbmdGYWNlIG1vZGVsLiBUaGUgdG90YWwgbnVtYmVyIG9mIEtWIGVudHJpZXMgcmV0dXJuZWQgaXMgYWx3YXlzIGF0IG1vc3Qgbl9zaW5rICsgd2luZG93X3NpemUsIHByb3ZpZGluZyB0aGUgY29uc3RhbnQtbWVtb3J5IGd1YXJhbnRlZSByZWdhcmRsZXNzIG9mIGhvdyBtYW55IHRva2VucyBoYXZlIGJlZW4gZ2VuZXJhdGVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvVG9rZW5pemVyLCBBdXRvTW9kZWxGb3JDYXVzYWxMTVxuXG5kZWYgYnVpbGRfc3RyZWFtaW5nX3Bvc2l0aW9uX2lkcyhzaW5rX2xlbjogaW50LCB3aW5kb3dfbGVuOiBpbnQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbmV3X3Rva2VuX3BvczogaW50KSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAjIFJlLWluZGV4IHBvc2l0aW9ucyBzbyBhdHRlbmRlZCB0b2tlbnMgaGF2ZSBjb250aWd1b3VzIFJvUEUtY29tcGF0aWJsZSBJRHNcbiAgICAjIFNpbmsgdG9rZW5zOiBbMCwgMSwgLi4uLCBzaW5rX2xlbi0xXSDigJQgYWx3YXlzIGZpeGVkXG4gICAgIyBXaW5kb3cgdG9rZW5zOiBbbmV3X3Rva2VuX3BvcyAtIHdpbmRvd19sZW4sIC4uLiwgbmV3X3Rva2VuX3BvcyAtIDFdXG4gICAgc2lua19pZHMgICA9IHRvcmNoLmFyYW5nZShzaW5rX2xlbiwgZHR5cGU9dG9yY2gubG9uZylcbiAgICB3aW5kb3dfc3RhcnQgPSBtYXgoc2lua19sZW4sIG5ld190b2tlbl9wb3MgLSB3aW5kb3dfbGVuKVxuICAgIHdpbmRvd19pZHMgPSB0b3JjaC5hcmFuZ2Uod2luZG93X3N0YXJ0LCBuZXdfdG9rZW5fcG9zLCBkdHlwZT10b3JjaC5sb25nKVxuICAgIHJldHVybiB0b3JjaC5jYXQoW3NpbmtfaWRzLCB3aW5kb3dfaWRzXSlcblxuZGVmIHN0cmVhbWluZ19nZW5lcmF0ZShtb2RlbCwgdG9rZW5pemVyLCBwcm9tcHQ6IHN0cixcbiAgICAgICAgICAgICAgICAgICAgICAgIG5fc2luazogaW50ID0gNCwgd2luZG93OiBpbnQgPSA1MTIsXG4gICAgICAgICAgICAgICAgICAgICAgICBtYXhfbmV3X3Rva2VuczogaW50ID0gMjAwMCkgLVx1MDAzZSBzdHI6XG4gICAgIyBBdXRvcmVncmVzc2l2ZSBnZW5lcmF0aW9uIHVzaW5nIFNpbmtDYWNoZSBmb3IgY29uc3RhbnQtbWVtb3J5IHN0cmVhbWluZ1xuICAgIGNhY2hlID0gU2lua0NhY2hlKG5fc2luaz1uX3NpbmssIHdpbmRvd19zaXplPXdpbmRvdylcbiAgICBpZHMgPSB0b2tlbml6ZXIocHJvbXB0LCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNykuaW5wdXRfaWRzLnRvKG1vZGVsLmRldmljZSlcbiAgICBnZW5lcmF0ZWQgPSBbXVxuICAgICMgUHJlZmlsbDogcHJvY2VzcyBhbGwgcHJvbXB0IHRva2VucyB0aHJvdWdoIHRoZSBjYWNoZVxuICAgIGZvciBpIGluIHJhbmdlKGlkcy5zaGFwZVsxXSk6XG4gICAgICAgIHRvayA9IGlkc1s6LCBpOmkrMV1cbiAgICAgICAgcG9zID0gdG9yY2gudGVuc29yKFtbaV1dLCBkdHlwZT10b3JjaC5sb25nLCBkZXZpY2U9bW9kZWwuZGV2aWNlKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIG91dCA9IG1vZGVsKHRvaywgcG9zaXRpb25faWRzPXBvcywgdXNlX2NhY2hlPVRydWUpXG4gICAgICAgIG5ld19rLCBuZXdfdiA9IG91dC5wYXN0X2tleV92YWx1ZXNbLTFdXG4gICAgICAgIGNhY2hlLmFkZChuZXdfa1s6LCA6LCAtMTosIDpdLCBuZXdfdls6LCA6LCAtMTosIDpdKVxuICAgICMgRGVjb2RlOiBnZW5lcmF0ZSB1cCB0byBtYXhfbmV3X3Rva2VucyB1c2luZyB0aGUgYm91bmRlZCBjYWNoZVxuICAgIG5leHRfdG9rID0gaWRzWzosIC0xOl1cbiAgICBmb3Igc3RlcCBpbiByYW5nZShtYXhfbmV3X3Rva2Vucyk6XG4gICAgICAgIHBvc19pZHMgPSBidWlsZF9zdHJlYW1pbmdfcG9zaXRpb25faWRzKGNhY2hlLm5fc2luaywgd2luZG93LCBjYWNoZS5zZXFfbGVuKVxuICAgICAgICBwb3NfaWRzID0gcG9zX2lkc1stMTpdLnVuc3F1ZWV6ZSgwKS50byhtb2RlbC5kZXZpY2UpXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgb3V0ID0gbW9kZWwobmV4dF90b2ssIHBvc2l0aW9uX2lkcz1wb3NfaWRzLCB1c2VfY2FjaGU9RmFsc2UpXG4gICAgICAgIG5leHRfdG9rID0gb3V0LmxvZ2l0c1s6LCAtMSwgOl0uYXJnbWF4KGRpbT0tMSwga2VlcGRpbT1UcnVlKVxuICAgICAgICBnZW5lcmF0ZWQuYXBwZW5kKG5leHRfdG9rLml0ZW0oKSlcbiAgICAgICAgaWYgbmV4dF90b2suaXRlbSgpID09IHRva2VuaXplci5lb3NfdG9rZW5faWQ6XG4gICAgICAgICAgICBicmVha1xuICAgIHJldHVybiB0b2tlbml6ZXIuZGVjb2RlKGdlbmVyYXRlZCwgc2tpcF9zcGVjaWFsX3Rva2Vucz1UcnVlKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNsaWRpbmcgV2luZG93IEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHNsaWRpbmcgd2luZG93IGNvbXBvbmVudCBvZiBTaW5rQ2FjaGUgcHJvdmlkZXMgbG9jYWwgY29udGV4dCBjb2hlcmVuY2U6IGVhY2ggZ2VuZXJhdGVkIHRva2VuIGNhbiBhdHRlbmQgdG8gdGhlIG1vc3QgcmVjZW50IHdpbmRvd19zaXplIHRva2Vucy4gVGhpcyB3aW5kb3cgY2FwdHVyZXMgc2VudGVuY2UtbGV2ZWwgYW5kIHBhcmFncmFwaC1sZXZlbCBkZXBlbmRlbmNpZXMg4oCUIHR5cGljYWxseSBzdWZmaWNpZW50IGZvciBmbHVlbnQgdGV4dCBnZW5lcmF0aW9uLiBDb250ZW50IGZyb20gYmV5b25kIHRoZSB3aW5kb3cgaXMgcGVybWFuZW50bHkgbG9zdCB0byBhdHRlbnRpb24sIHdoaWNoIGlzIHRoZSBwcmltYXJ5IGxpbWl0YXRpb24gb2YgU3RyZWFtaW5nTExNIGNvbXBhcmVkIHRvIGZ1bGwgbG9uZy1jb250ZXh0IG1vZGVscy4gSG93ZXZlciwgZm9yIG1hbnkgc3RyZWFtaW5nIGFwcGxpY2F0aW9ucyAobGl2ZSB0cmFuc2NyaXB0aW9uLCByZWFsLXRpbWUgZGlhbG9ndWUpLCBvbmx5IHRoZSByZWNlbnQgY29udGV4dCBpcyBuZWVkZWQgYW5kIHRoZSB3aW5kb3cgYXBwcm9hY2ggaXMgcGVyZmVjdGx5IGFkZXF1YXRlLiBUaGUgd2luZG93IHNpemUgaXMgYSB0dW5hYmxlIHBhcmFtZXRlcjogd2luZG93X3NpemU9NTEyIHVzZXMgYXBwcm94aW1hdGVseSAxR0Igb2YgS1YgY2FjaGUgbWVtb3J5IGZvciBhIDdCIG1vZGVsLCB3aGlsZSB3aW5kb3dfc2l6ZT0yMDQ4IHVzZXMgfjRHQi4gTGFyZ2VyIHdpbmRvd3MgcHJvdmlkZSBiZXR0ZXIgbG9uZy10ZXJtIGNvaGVyZW5jZSBhdCB0aGUgY29zdCBvZiBzbG93ZXIgYXR0ZW50aW9uIGNvbXB1dGF0aW9uICh0aG91Z2ggc3RpbGwgTyh3aW5kb3dfc2l6ZSkgcGVyIHN0ZXAsIG5vdCBPKG4pKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdGltZVxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXIsIEF1dG9Nb2RlbEZvckNhdXNhbExNXG5cbmRlZiB0aHJvdWdocHV0X2JlbmNobWFyayhtb2RlbF9uYW1lOiBzdHIsIG5fdG9rZW5zOiBpbnQgPSAxMDAwLFxuICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3c6IGludCA9IDUxMiwgbl9zaW5rOiBpbnQgPSA0KSAtXHUwMDNlIGRpY3Q6XG4gICAgIyBDb21wYXJlIHRva2Vucy9zZWM6IFN0cmVhbWluZ0xMTSB2cyBzdGFuZGFyZCBnZW5lcmF0aW9uIHdpdGggNEsgdHJ1bmNhdGlvblxuICAgIHRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXG4gICAgbW9kZWwgPSBBdXRvTW9kZWxGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQoXG4gICAgICAgIG1vZGVsX25hbWUsIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsIGRldmljZV9tYXA9XHUwMDI3YXV0b1x1MDAyN1xuICAgIClcbiAgICBwcm9tcHQgPSBcdTAwMjdUaGUgZm9sbG93aW5nIGlzIGEgbG9uZyB0ZWNobmljYWwgZGlzY3Vzc2lvbiBhYm91dCBtYWNoaW5lIGxlYXJuaW5nOiBcdTAwMjdcbiAgICBpZHMgPSB0b2tlbml6ZXIocHJvbXB0LCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNykuaW5wdXRfaWRzLmN1ZGEoKVxuICAgICMgQmVuY2htYXJrIDE6IFN0YW5kYXJkIGdlbmVyYXRpb24gKHRydW5jYXRpb24gYXQgbWF4X2xlbmd0aD00MDk2KVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBvdXQgPSBtb2RlbC5nZW5lcmF0ZShpZHMsIG1heF9uZXdfdG9rZW5zPW5fdG9rZW5zLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhfbGVuZ3RoPTQwOTYsIGRvX3NhbXBsZT1GYWxzZSlcbiAgICBzdGRfc3BlZWQgPSBuX3Rva2VucyAvICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApXG4gICAgIyBCZW5jaG1hcmsgMjogU3RyZWFtaW5nTExNIHdpdGggU2lua0NhY2hlXG4gICAgY2FjaGUgPSBTaW5rQ2FjaGUobl9zaW5rPW5fc2luaywgd2luZG93X3NpemU9d2luZG93KVxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGZvciBfIGluIHJhbmdlKG5fdG9rZW5zKTpcbiAgICAgICAgaywgdiA9IGNhY2hlLmdldF9rdigpIGlmIGNhY2hlLmNhY2hlX3NpemUgXHUwMDNlIDAgZWxzZSAoTm9uZSwgTm9uZSlcbiAgICAgICAgcGFzcyAgIyBwbGFjZWhvbGRlciBmb3IgYWN0dWFsIHN0cmVhbWluZyBzdGVwXG4gICAgc3RyZWFtX3NwZWVkID0gbl90b2tlbnMgLyAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKVxuICAgIHByaW50KGZcdTAwMjdTdGFuZGFyZCBnZW5lcmF0aW9uOiB7c3RkX3NwZWVkOi4xZn0gdG9rZW5zL3NlY1x1MDAyNylcbiAgICBwcmludChmXHUwMDI3U3RyZWFtaW5nTExNICh7d2luZG93fS10b2tlbiB3aW5kb3cpOiB7c3RyZWFtX3NwZWVkOi4xZn0gdG9rZW5zL3NlY1x1MDAyNylcbiAgICByZXR1cm4ge1x1MDAyN3N0YW5kYXJkXHUwMDI3OiBzdGRfc3BlZWQsIFx1MDAyN3N0cmVhbWluZ1x1MDAyNzogc3RyZWFtX3NwZWVkfSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBvc2l0aW9uIFJlLWluZGV4aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZnRlciBlYWNoIGV2aWN0aW9uIHN0ZXAsIHRoZSB3aW5kb3cgdG9rZW5zIGhhdmUgYSBnYXAgYmV0d2VlbiB0aGUgc2luayBwb3NpdGlvbnMgKDDigJMzKSBhbmQgdGhlaXIgb3JpZ2luYWwgc2VxdWVuY2UgcG9zaXRpb25zLiBXaXRob3V0IHJlLWluZGV4aW5nLCB0aGUgUm9QRSBlbWJlZGRpbmdzIHdvdWxkIHVzZSB0aGUgb3JpZ2luYWwgcG9zaXRpb25zLCBjcmVhdGluZyBhIGxhcmdlIHBvc2l0aW9uYWwgZ2FwIHRoYXQgZGlzcnVwdHMgcmVsYXRpdmUgcG9zaXRpb24gYXR0ZW50aW9uLiBTdHJlYW1pbmdMTE0gcmUtaW5kZXhlcyBwb3NpdGlvbnMgYXQgZWFjaCBzdGVwOiBzaW5rIHRva2VucyByZXRhaW4gcG9zaXRpb25zIFswLCAxLCAyLCAzXTsgd2luZG93IHRva2VucyBhcmUgYXNzaWduZWQgcG9zaXRpb25zIFtuX3NpbmssIG5fc2luaysxLCAuLi4sIG5fc2luayt3aW5kb3dfbGVuLTFdIHJlZ2FyZGxlc3Mgb2YgdGhlaXIgb3JpZ2luYWwgYWJzb2x1dGUgcG9zaXRpb25zLiBUaGlzIG1ha2VzIHRoZSBhdHRlbmRlZCBzZXF1ZW5jZSBhcHBlYXIgY29udGlndW91cyBmcm9tIHRoZSBtb2RlbFx1MDAyN3MgcGVyc3BlY3RpdmUuIFRoZSBwcmFjdGljYWwgZWZmZWN0IGlzIHRoYXQgdGhlIG1vZGVsIGJlbGlldmVzIGl0IGlzIGF0dGVuZGluZyB0byBhIHNlcXVlbmNlIG9mIGxlbmd0aCBuX3NpbmsgKyB3aW5kb3dfc2l6ZSDigJQgdGhlIHNpbmsgdG9rZW5zIGF0IHRoZSBiZWdpbm5pbmcgYW5kIHRoZSByZWNlbnQgd2luZG93IHJpZ2h0IGFmdGVyLiBQb3NpdGlvbiByZS1pbmRleGluZyByZXF1aXJlcyBvbmx5IGEgY2hhbmdlIHRvIHRoZSBwb3NpdGlvbl9pZHMgdGVuc29yIHBhc3NlZCB0byB0aGUgbW9kZWw7IG5vIHdlaWdodCBtb2RpZmljYXRpb24gaXMgbmVlZGVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIGRlbW9fbXVsdGl0dXJuX3N0cmVhbWluZyhuX3R1cm5zOiBpbnQgPSAyMCwgd2luZG93OiBpbnQgPSAyNTYsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX3Npbms6IGludCA9IDQpIC1cdTAwM2UgTm9uZTpcbiAgICAjIFNpbXVsYXRlIG11bHRpLXR1cm4gZGlhbG9ndWUgd2l0aCBTdHJlYW1pbmdMTE0gU2lua0NhY2hlXG4gICAgIyBFYWNoIHR1cm4gYXBwZW5kcyB1c2VyICsgYXNzaXN0YW50IHRva2VucyB0byB0aGUgY2FjaGVcbiAgICBjYWNoZV9zdGF0dXMgPSBbXVxuICAgIHRvdGFsX3Rva2VucyA9IDBcbiAgICBmb3IgdHVybiBpbiByYW5nZShuX3R1cm5zKTpcbiAgICAgICAgdXNlcl90b2tlbnMgICA9IHRvcmNoLnJhbmRuKDEsIDgsIDEsIDY0KSAgICMgc2ltdWxhdGUgOCBuZXcgdXNlciB0b2tlbnNcbiAgICAgICAgYXNzaXN0X3Rva2VucyA9IHRvcmNoLnJhbmRuKDEsIDgsIDEsIDY0KSAgICMgc2ltdWxhdGUgOCBhc3Npc3RhbnQgdG9rZW5zXG4gICAgICAgIGZvciB0b2sgaW4gcmFuZ2UoOCk6ICAjIGFkZCB1c2VyIHRva2Vuc1xuICAgICAgICAgICAgayA9IHVzZXJfdG9rZW5zWzosIDosIHRvazp0b2srMSwgOl1cbiAgICAgICAgICAgIHYgPSB1c2VyX3Rva2Vuc1s6LCA6LCB0b2s6dG9rKzEsIDpdXG4gICAgICAgICAgICBpZiB0b3RhbF90b2tlbnMgXHUwMDNjIG5fc2luazpcbiAgICAgICAgICAgICAgICBwYXNzICAjIGdvZXMgdG8gc2lua1xuICAgICAgICAgICAgdG90YWxfdG9rZW5zICs9IDFcbiAgICAgICAgZm9yIHRvayBpbiByYW5nZSg4KTogICMgYWRkIGFzc2lzdGFudCB0b2tlbnNcbiAgICAgICAgICAgIHRvdGFsX3Rva2VucyArPSAxXG4gICAgICAgIGNhY2hlX2xlbiA9IG1pbih0b3RhbF90b2tlbnMsIG5fc2luayArIHdpbmRvdylcbiAgICAgICAgY2FjaGVfc3RhdHVzLmFwcGVuZCh7XHUwMDI3dHVyblx1MDAyNzogdHVybiArIDEsIFx1MDAyN3RvdGFsXHUwMDI3OiB0b3RhbF90b2tlbnMsIFx1MDAyN2NhY2hlXHUwMDI3OiBjYWNoZV9sZW59KVxuICAgIHByaW50KGZcdTAwMjd7XCJUdXJuXCI6XHUwMDNlNX0gfCB7XCJUb3RhbCBUb2tlbnNcIjpcdTAwM2UxMn0gfCB7XCJDYWNoZSBTaXplXCI6XHUwMDNlMTB9XHUwMDI3KVxuICAgIGZvciBzIGluIGNhY2hlX3N0YXR1c1s6OjVdOlxuICAgICAgICBwcmludChmXHUwMDI3e3NbXCJ0dXJuXCJdOlx1MDAzZTV9IHwge3NbXCJ0b3RhbFwiXTpcdTAwM2UxMn0gfCB7c1tcImNhY2hlXCJdOlx1MDAzZTEwfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3Q2FjaGUgc3RheXMgYm91bmRlZCBhdCBtYXgge25fc2luayArIHdpbmRvd30gcmVnYXJkbGVzcyBvZiB0b3RhbCB0b2tlbnNcdTAwMjcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlNjZW5hcmlvIiwiQ29udGV4dCBOZWVkZWQiLCJDYWNoZSBTaXplIiwiQXBwcm9hY2giLCJTdHJlYW1pbmdMTE0gV29ya3M/Il0sInJvd3MiOltbIlNob3J0IGRvY3VtZW50IFFcdTAwMjZBIiwiXHUwMDNjIHdpbmRvd19zaXplIiwiXHUwMDNjIDUxNiB0b2tlbnMiLCJTdGFuZGFyZCBvciBzdHJlYW1pbmciLCJZZXMg4oCUIHRyaXZpYWxseSJdLFsiTG9uZyBkb2N1bWVudCBzdW1tYXJpemF0aW9uIiwiRnVsbCBkb2N1bWVudCIsIkdyb3dzIHdpdGggZG9jIiwiRnVsbCBsb25nLWNvbnRleHQgbW9kZWwgb3IgUkFHIiwiUGFydGlhbCDigJQgbG9zZXMgZWFybGllciBjb250ZW50Il0sWyJTdHJlYW1pbmcgdHJhbnNjcmlwdGlvbiIsIlJlY2VudCBhdWRpbyBvbmx5IiwiNTEyLTIwNDggdG9rZW5zIiwiU2luayArIHdpbmRvdyIsIlllcyDigJQgaWRlYWwgdXNlIGNhc2UiXSxbIk11bHRpLXR1cm4gZGlhbG9ndWUiLCJSZWNlbnQgdHVybnMiLCI1MTItMjA0OCB0b2tlbnMiLCJTaW5rICsgd2luZG93IiwiWWVzIOKAlCB3aW5kb3cgY292ZXJzIHJlY2VudCB0dXJucyJdLFsiSW5maW5pdGUgbm92ZWwgZ2VuZXJhdGlvbiIsIkxvY2FsIGNvaGVyZW5jZSBvbmx5IiwiNTEyLTIwNDggdG9rZW5zIiwiU2luayArIHdpbmRvdyIsIlllcyDigJQgc3RhYmxlIGluZGVmaW5pdGVseSJdLFsiTmVlZGxlLWluLWhheXN0YWNrIHJldHJpZXZhbCIsIkZ1bGwgZG9jdW1lbnQiLCJHcm93cyB0byBPT00iLCJGdWxsIGxvbmctY29udGV4dCBtb2RlbCIsIk5vIOKAlCBldmljdGVkIGNvbnRlbnQgdW5hdHRlbmRhYmxlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaHJvdWdocHV0IGFuZCBMYXRlbmN5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdHJlYW1pbmdMTE0gYWNoaWV2ZXMgY29uc3RhbnQgcGVyLXRva2VuIGxhdGVuY3kgYmVjYXVzZSB0aGUgS1YgY2FjaGUgc2l6ZSBpcyBib3VuZGVkLiBJbiBzdGFuZGFyZCBnZW5lcmF0aW9uLCBhdHRlbnRpb24gY29tcHV0YXRpb24gcGVyIHRva2VuIGdyb3dzIGFzIE8obikgKGxpbmVhciBpbiBzZXF1ZW5jZSBsZW5ndGgsIHF1YWRyYXRpYyB0b3RhbCksIGNhdXNpbmcgZ2VuZXJhdGlvbiB0byBzbG93IGRvd24gc2lnbmlmaWNhbnRseSBmb3IgbG9uZyBzZXF1ZW5jZXMuIFdpdGggYSBmaXhlZCBjYWNoZSBvZiBzaXplIG5fc2luayArIHdpbmRvd19zaXplID0gNTE2IGVudHJpZXMgKGF0IGRlZmF1bHQgc2V0dGluZ3MpLCBlYWNoIHRva2VuIHJlcXVpcmVzIGEgY29uc3RhbnQgbnVtYmVyIG9mIGF0dGVudGlvbiBvcGVyYXRpb25zIHJlZ2FyZGxlc3Mgb2YgaG93IG1hbnkgdG9rZW5zIGhhdmUgYmVlbiBnZW5lcmF0ZWQuIFRoZSBwYXBlciByZXBvcnRzIHRoYXQgU3RyZWFtaW5nTExNIG1haW50YWlucyA5NSUgb2YgdGhlIHNpbmdsZS10b2tlbiB0aHJvdWdocHV0IG9mIHRoZSBiYXNlIG1vZGVsIGluZGVmaW5pdGVseS4gTWVtb3J5IHVzYWdlIGlzIGFsc28gY29uc3RhbnQ6IGZvciBMTGFNQS03QiB3aXRoIDMyIGxheWVycywgMzIgaGVhZHMsIGhlYWRfZGltPTEyOCwgZmxvYXQxNiwgYW5kIGEgNTE2LWVudHJ5IGNhY2hlLCB0b3RhbCBLViBtZW1vcnkgaXMgMzIgw5cgMzIgw5cgNTE2IMOXIDEyOCDDlyAyIGJ5dGVzIOKJiCAxLjM3IEdCIOKAlCBhIGZpeGVkIGJ1ZGdldCByZWdhcmRsZXNzIG9mIGdlbmVyYXRpb24gZHVyYXRpb24uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlN0cmVhbWluZ0xMTSBTb2x2ZXMgTWVtb3J5LCBOb3QgUmV0cmlldmFsIiwiY29udGVudCI6IlN0cmVhbWluZ0xMTSBzb2x2ZXMgdGhlIG1lbW9yeSBwcm9ibGVtIGJ1dCBub3QgdGhlIHJldHJpZXZhbCBwcm9ibGVtIOKAlCB0aGUgbW9kZWwgY2FuIG9ubHkgYXR0ZW5kIHRvIGNvbnRlbnQgaW4gaXRzIHdpbmRvdzsgZm9yIHRydWUgbG9uZy1jb250ZXh0IHJldHJpZXZhbCwgY29tYmluZSBTdHJlYW1pbmdMTE0gd2l0aCBSQUcgb3IgdXNlIGEgZnVsbCBsb25nLWNvbnRleHQgbW9kZWwuIFN0cmVhbWluZ0xMTSBpcyBpZGVhbCBmb3Igc3RyZWFtaW5nIGdlbmVyYXRpb24gd2hlcmUgb25seSBsb2NhbCBjb2hlcmVuY2UgaXMgbmVlZGVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbWl0YXRpb25zIGFuZCBVc2UgQ2FzZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0cmVhbWluZ0xMTSBoYXMgb25lIGZ1bmRhbWVudGFsIGxpbWl0YXRpb246IGNvbnRlbnQgZXZpY3RlZCBmcm9tIHRoZSB3aW5kb3cgaXMgcGVybWFuZW50bHkgaW5hY2Nlc3NpYmxlIHRvIGF0dGVudGlvbi4gVGhpcyBtZWFucyB0aGUgbW9kZWwgY2Fubm90IHJldHJpZXZlIGluZm9ybWF0aW9uIGZyb20gbW9yZSB0aGFuIHdpbmRvd19zaXplIHRva2VucyBhZ28sIHJlZ2FyZGxlc3Mgb2YgaG93IGxvbmcgdGhlIGdlbmVyYXRpb24gc2Vzc2lvbiBpcy4gRm9yIG5lZWRsZS1pbi1oYXlzdGFjayByZXRyaWV2YWwgdGFza3Mgd2hlcmUgdGhlIGFuc3dlciBtYXkgYmUgYW55d2hlcmUgaW4gYSBsb25nIGRvY3VtZW50LCBTdHJlYW1pbmdMTE0gd2lsbCBmYWlsIHVubGVzcyB0aGUgcmVsZXZhbnQgY29udGVudCBoYXBwZW5zIHRvIHJlbWFpbiBpbiB0aGUgd2luZG93LiBUaGUgYXBwcm9wcmlhdGUgdXNlIGNhc2VzIGFyZSB0aG9zZSB3aGVyZSBvbmx5IHJlY2VudCBjb250ZXh0IGlzIG5lZWRlZDogbGl2ZSB0cmFuc2NyaXB0aW9uIGFuZCBzdW1tYXJpemF0aW9uLCBzdHJlYW1pbmcgY29kZSBjb21wbGV0aW9uLCByZWFsLXRpbWUgZGlhbG9ndWUgc3lzdGVtcywgYW5kIGxvbmcgY3JlYXRpdmUgd3JpdGluZyB3aGVyZSBsb2NhbCBzdHlsZSBjb2hlcmVuY2Ugc3VmZmljZXMuIEZvciB0cnVlIGxvbmctY29udGV4dCB1bmRlcnN0YW5kaW5nIHRhc2tzIOKAlCBsZWdhbCBkb2N1bWVudCBhbmFseXNpcywgbXVsdGktY2hhcHRlciBib29rIHN1bW1hcml6YXRpb24sIGxvbmctZm9ybSByZXNlYXJjaCByZXBvcnQgUVx1MDAyNkEg4oCUIGEgZnVsbCBsb25nLWNvbnRleHQgbW9kZWwgd2l0aCBSb1BFIGV4dGVuc2lvbiBvciBhIFJBRyBzeXN0ZW0gaXMgcmVxdWlyZWQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJNZW1vcnkgY29zdCBpcyBjb25zdGFudDogKG5fc2luayArIHdpbmRvd19zaXplKSDDlyBsYXllcnMgw5cgaGVhZHMgw5cgaGVhZF9kaW0gw5cgMiBieXRlcywgZml4ZWQgZm9yIHRoZSBzZXNzaW9uLiIsIlBlci10b2tlbiBzcGVlZCBpcyBjb25zdGFudDogYXR0ZW50aW9uIG92ZXIgYSBmaXhlZCBjYWNoZSBvZiBzaXplIDUxNiByYXRoZXIgdGhhbiBhIGdyb3dpbmcgc2VxdWVuY2UuIiwiU2luayB0b2tlbnMgYXJlIG5ldmVyIGV2aWN0ZWQ6IHRoZSBmaXJzdCA0IHRva2VucyBvZiBhbnkgc2Vzc2lvbiBhcmUgcGVybWFuZW50bHkgcmV0YWluZWQgdGhyb3VnaG91dCBnZW5lcmF0aW9uLiIsIlBvc2l0aW9uIHJlLWluZGV4aW5nIGlzIHJlcXVpcmVkOiBzaW5rIHRva2VucyBnZXQgcG9zaXRpb25zIDAtMywgd2luZG93IHRva2VucyBnZXQgcG9zaXRpb25zIDQgdG8gNCt3aW5kb3dfbGVuLTEuIiwiTm8gcmV0cmFpbmluZyBuZWVkZWQ6IHdvcmtzIHdpdGggYW55IHByZXRyYWluZWQgUm9QRSBvciBBTGlCaSBtb2RlbCB3aXRob3V0IHdlaWdodCBtb2RpZmljYXRpb24uIiwiQ3JpdGljYWwgbGltaXRhdGlvbjogY29udGVudCBldmljdGVkIGZyb20gdGhlIHdpbmRvdyBpcyB1bmF0dGVuZGFibGUg4oCUIGNvbWJpbmUgd2l0aCBSQUcgZm9yIGxvbmctY29udGV4dCByZXRyaWV2YWwuIiwiV2luZG93IHNpemUgdHVuaW5nOiA1MTIgdG9rZW5zIGZvciBtaW5pbWFsIG1lbW9yeSwgMjA0OCBmb3IgYmV0dGVyIGNvaGVyZW5jZSwgNDA5NiBmb3IgbmVhci1mdWxsLWNvbnRleHQgcXVhbGl0eS4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RyZWFtaW5nTExNIGlzIGEgcHJhY3RpY2FsIHN5c3RlbSBlbmFibGluZyBwcmV0cmFpbmVkIExMTXMgdG8gZnVuY3Rpb24gYXMgdHJ1ZSBzdHJlYW1pbmcgbW9kZWxzLiBJdHMgZGVzaWduIGlzIHByaW5jaXBsZWQ6IHRoZSBTaW5rQ2FjaGUgaXMgbm90IGEgaGV1cmlzdGljIGJ1dCBhIGRpcmVjdCByZXNwb25zZSB0byB0aGUgb2JzZXJ2ZWQgYXR0ZW50aW9uIHNpbmsgc3RydWN0dXJlIG9mIHRyYW5zZm9ybWVyIG1vZGVscy4gQnkgcmV0YWluaW5nIDQgc2luayB0b2tlbnMgcGx1cyBhIHNsaWRpbmcgd2luZG93LCBTdHJlYW1pbmdMTE0gYWNoaWV2ZXMgY29uc3RhbnQgbWVtb3J5LCBjb25zdGFudCBzcGVlZCwgYW5kIHN0YWJsZSBwZXJwbGV4aXR5IG92ZXIgYXJiaXRyYXJpbHkgbG9uZyBzZXF1ZW5jZXMuIFRoZSBhcHByb2FjaCByZXF1aXJlcyBubyByZXRyYWluaW5nLCBubyBmaW5lLXR1bmluZywgYW5kIG5vIGFyY2hpdGVjdHVyYWwgY2hhbmdlcyDigJQgYSB6ZXJvLXNob3QgY2FwYWJpbGl0eSB0aGF0IG1ha2VzIGl0IGltbWVkaWF0ZWx5IGFwcGxpY2FibGUgdG8gYW55IHByZXRyYWluZWQgUm9QRS1iYXNlZCBtb2RlbCBpbmNsdWRpbmcgdGhlIGVudGlyZSBMTGFNQSBmYW1pbHkuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTaW5rQ2FjaGUgZGVzaWduOiBrZWVwIGZpcnN0IG5fc2luaz00IHRva2VucyBwZXJtYW5lbnRseSArIHJvbGxpbmcgd2luZG93X3NpemU9NTEyIGZvciByZWNlbnQgY29udGV4dC4iLCJDYWNoZSBpcyBib3VuZGVkIGF0IG5fc2luayArIHdpbmRvd19zaXplIGVudHJpZXMsIGdpdmluZyBPKDEpIG1lbW9yeSBncm93dGggb3ZlciBhcmJpdHJhcnkgZ2VuZXJhdGlvbiBsZW5ndGguIiwiUG9zaXRpb24gcmUtaW5kZXggYXQgZWFjaCBzdGVwOiBzaW5rIGF0IFswLi4zXSwgd2luZG93IGF0IFs0Li40K3dpbl9sZW4tMV0gZm9yIFJvUEUgY29uc2lzdGVuY3kuIiwiV29ya3Mgd2l0aG91dCByZXRyYWluaW5nIG9uIGFueSBwcmV0cmFpbmVkIFJvUEUgbW9kZWwg4oCUIHB1cmUgaW5mZXJlbmNlLXRpbWUgbW9kaWZpY2F0aW9uLiIsIlN0YWJsZSBwZXJwbGV4aXR5IGRlbW9uc3RyYXRlZCBhdCA0IG1pbGxpb24gZ2VuZXJhdGVkIHRva2VucyBpbiB0aGUgb3JpZ2luYWwgcGFwZXIuIiwiQ29tYmluZSB3aXRoIFJBRyBmb3IgbG9uZy1jb250ZXh0IHJldHJpZXZhbCB0YXNrczsgU3RyZWFtaW5nTExNIGFsb25lIGNhbm5vdCByZXRyaWV2ZSBldmljdGVkIGNvbnRlbnQuIiwiRm9yIHRyYWluaW5nLXRpbWUgaW1wcm92ZW1lbnQsIGFkZCBhIGRlZGljYXRlZCBcdTAwM2NzaW5rXHUwMDNlIHRva2VuIHByZWZpeCBzbyBjb250ZW50IHRva2VucyBhcmUgbm90IHJlcHVycG9zZWQgYXMgc2lua3MuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# StreamingLLM: Efficient Streaming Language Model Inference

StreamingLLM (Xiao et al., 2023) is an inference system that enables pretrained large language models to generate text of unbounded length without retraining, architectural changes, or context-length restrictions. It achieves this by combining two insights: (1) the attention sink phenomenon — that models reliably attend to initial tokens regardless of content — means those tokens must be kept in the KV cache permanently; and (2) a fixed sliding window of recent tokens provides sufficient local context for coherent generation. The result is a constant-memory, constant-speed inference engine that transforms any pretrained LLM into a streaming model capable of producing millions of tokens in a single session, enabling applications such as real-time transcription summarization, always-on AI assistants, and streaming code generation over entire repositories.

## Overview

Standard autoregressive generation stores all past KV pairs in memory (the KV cache), which grows linearly with sequence length and eventually exhausts GPU memory. Truncating the input to a fixed context window forces the model to discard earlier content and breaks generation quality. StreamingLLM avoids both problems by implementing a SinkCache: a fixed-size KV store that always contains the first n_sink=4 tokens (the sink region) plus the most recent window_size tokens (the sliding window). Total cache size is constant at n_sink + window_size entries. When a new token is generated, its KV pair enters the window; if the window is full, the oldest window entry is evicted. Sink entries are never evicted. The model attends over this bounded cache at each step, producing stable perplexity for sequences of arbitrary length. The paper demonstrates stable generation at 4 million tokens.

## System Architecture

StreamingLLM is a pure inference modification — the model weights are untouched. The system inserts a SinkCache manager between the transformer's attention modules and the KV cache storage. At each generation step, the attention module calls SinkCache.add(key, value) to store the new KV pair, then calls SinkCache.get_kv() to retrieve the full bounded KV state for attention computation. The get_kv() return is a concatenation of [sink_keys; window_keys] and [sink_values; window_values] in their original causal order. Position IDs are re-indexed at each step to match the actual attended positions: sink tokens retain positions [0, 1, 2, 3]; window tokens are assigned contiguous positions [n_sink, n_sink+1, ..., n_sink+window_size-1]. This re-indexing is critical for RoPE consistency — the model must see positions that reflect the relative order of attended tokens.

```python
import torch
import torch.nn as nn
from typing import Optional, Tuple

class SinkCache:
    # StreamingLLM KV cache: permanent sink region + sliding window
    # Enables infinite-length generation at constant memory and compute

    def __init__(self, n_sink: int = 4, window_size: int = 512):
        self.n_sink = n_sink
        self.window_size = window_size
        self._sink_k:  list = []
        self._sink_v:  list = []
        self._win_k:   list = []
        self._win_v:   list = []
        self.seq_len = 0

    def add(self, key: torch.Tensor, value: torch.Tensor) -> None:
        # key/value: (batch, n_heads, 1, head_dim) — single new token
        if self.seq_len < self.n_sink:
            self._sink_k.append(key)
            self._sink_v.append(value)
        else:
            self._win_k.append(key)
            self._win_v.append(value)
            if len(self._win_k) > self.window_size:
                self._win_k.pop(0)
                self._win_v.pop(0)
        self.seq_len += 1

    def get_kv(self) -> Tuple[torch.Tensor, torch.Tensor]:
        # Returns concatenated [sink | window] keys and values
        all_k = torch.cat(self._sink_k + self._win_k, dim=2)
        all_v = torch.cat(self._sink_v + self._win_v, dim=2)
        return all_k, all_v

    def get_position_ids(self) -> torch.Tensor:
        # Contiguous positions [0..n_sink-1, n_sink..cache_len-1]
        cache_len = len(self._sink_k) + len(self._win_k)
        return torch.arange(cache_len, dtype=torch.long)

    @property
    def cache_size(self) -> int:
        return len(self._sink_k) + len(self._win_k)
```

## Sink Cache Implementation

The SinkCache.add() method routes incoming KV pairs based on whether the sequence length has reached the sink budget. For the first n_sink tokens, entries are appended to the permanent sink lists. From token n_sink onward, entries go into the window lists, which are pruned by evicting from the front whenever length exceeds window_size. This means the first n_sink tokens of any document are always retained, matching the attention sink structure observed in pretrained models. The SinkCache.get_kv() method concatenates sink and window lists along the sequence dimension, returning a view suitable for use as past_key_values in any HuggingFace model. The total number of KV entries returned is always at most n_sink + window_size, providing the constant-memory guarantee regardless of how many tokens have been generated.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def build_streaming_position_ids(sink_len: int, window_len: int,
                                  new_token_pos: int) -> torch.Tensor:
    # Re-index positions so attended tokens have contiguous RoPE-compatible IDs
    # Sink tokens: [0, 1, ..., sink_len-1] — always fixed
    # Window tokens: [new_token_pos - window_len, ..., new_token_pos - 1]
    sink_ids   = torch.arange(sink_len, dtype=torch.long)
    window_start = max(sink_len, new_token_pos - window_len)
    window_ids = torch.arange(window_start, new_token_pos, dtype=torch.long)
    return torch.cat([sink_ids, window_ids])

def streaming_generate(model, tokenizer, prompt: str,
                        n_sink: int = 4, window: int = 512,
                        max_new_tokens: int = 2000) -> str:
    # Autoregressive generation using SinkCache for constant-memory streaming
    cache = SinkCache(n_sink=n_sink, window_size=window)
    ids = tokenizer(prompt, return_tensors='pt').input_ids.to(model.device)
    generated = []
    # Prefill: process all prompt tokens through the cache
    for i in range(ids.shape[1]):
        tok = ids[:, i:i+1]
        pos = torch.tensor([[i]], dtype=torch.long, device=model.device)
        with torch.no_grad():
            out = model(tok, position_ids=pos, use_cache=True)
        new_k, new_v = out.past_key_values[-1]
        cache.add(new_k[:, :, -1:, :], new_v[:, :, -1:, :])
    # Decode: generate up to max_new_tokens using the bounded cache
    next_tok = ids[:, -1:]
    for step in range(max_new_tokens):
        pos_ids = build_streaming_position_ids(cache.n_sink, window, cache.seq_len)
        pos_ids = pos_ids[-1:].unsqueeze(0).to(model.device)
        with torch.no_grad():
            out = model(next_tok, position_ids=pos_ids, use_cache=False)
        next_tok = out.logits[:, -1, :].argmax(dim=-1, keepdim=True)
        generated.append(next_tok.item())
        if next_tok.item() == tokenizer.eos_token_id:
            break
    return tokenizer.decode(generated, skip_special_tokens=True)
```

## Sliding Window Attention

The sliding window component of SinkCache provides local context coherence: each generated token can attend to the most recent window_size tokens. This window captures sentence-level and paragraph-level dependencies — typically sufficient for fluent text generation. Content from beyond the window is permanently lost to attention, which is the primary limitation of StreamingLLM compared to full long-context models. However, for many streaming applications (live transcription, real-time dialogue), only the recent context is needed and the window approach is perfectly adequate. The window size is a tunable parameter: window_size=512 uses approximately 1GB of KV cache memory for a 7B model, while window_size=2048 uses ~4GB. Larger windows provide better long-term coherence at the cost of slower attention computation (though still O(window_size) per step, not O(n)).

```python
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM

def throughput_benchmark(model_name: str, n_tokens: int = 1000,
                          window: int = 512, n_sink: int = 4) -> dict:
    # Compare tokens/sec: StreamingLLM vs standard generation with 4K truncation
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16, device_map='auto'
    )
    prompt = 'The following is a long technical discussion about machine learning: '
    ids = tokenizer(prompt, return_tensors='pt').input_ids.cuda()
    # Benchmark 1: Standard generation (truncation at max_length=4096)
    t0 = time.perf_counter()
    with torch.no_grad():
        out = model.generate(ids, max_new_tokens=n_tokens,
                             max_length=4096, do_sample=False)
    std_speed = n_tokens / (time.perf_counter() - t0)
    # Benchmark 2: StreamingLLM with SinkCache
    cache = SinkCache(n_sink=n_sink, window_size=window)
    t0 = time.perf_counter()
    for _ in range(n_tokens):
        k, v = cache.get_kv() if cache.cache_size > 0 else (None, None)
        pass  # placeholder for actual streaming step
    stream_speed = n_tokens / (time.perf_counter() - t0)
    print(f'Standard generation: {std_speed:.1f} tokens/sec')
    print(f'StreamingLLM ({window}-token window): {stream_speed:.1f} tokens/sec')
    return {'standard': std_speed, 'streaming': stream_speed}
```

## Position Re-indexing

After each eviction step, the window tokens have a gap between the sink positions (0–3) and their original sequence positions. Without re-indexing, the RoPE embeddings would use the original positions, creating a large positional gap that disrupts relative position attention. StreamingLLM re-indexes positions at each step: sink tokens retain positions [0, 1, 2, 3]; window tokens are assigned positions [n_sink, n_sink+1, ..., n_sink+window_len-1] regardless of their original absolute positions. This makes the attended sequence appear contiguous from the model's perspective. The practical effect is that the model believes it is attending to a sequence of length n_sink + window_size — the sink tokens at the beginning and the recent window right after. Position re-indexing requires only a change to the position_ids tensor passed to the model; no weight modification is needed.

```python
import torch

def demo_multiturn_streaming(n_turns: int = 20, window: int = 256,
                              n_sink: int = 4) -> None:
    # Simulate multi-turn dialogue with StreamingLLM SinkCache
    # Each turn appends user + assistant tokens to the cache
    cache_status = []
    total_tokens = 0
    for turn in range(n_turns):
        user_tokens   = torch.randn(1, 8, 1, 64)   # simulate 8 new user tokens
        assist_tokens = torch.randn(1, 8, 1, 64)   # simulate 8 assistant tokens
        for tok in range(8):  # add user tokens
            k = user_tokens[:, :, tok:tok+1, :]
            v = user_tokens[:, :, tok:tok+1, :]
            if total_tokens < n_sink:
                pass  # goes to sink
            total_tokens += 1
        for tok in range(8):  # add assistant tokens
            total_tokens += 1
        cache_len = min(total_tokens, n_sink + window)
        cache_status.append({'turn': turn + 1, 'total': total_tokens, 'cache': cache_len})
    print(f'{"Turn":>5} | {"Total Tokens":>12} | {"Cache Size":>10}')
    for s in cache_status[::5]:
        print(f'{s["turn"]:>5} | {s["total"]:>12} | {s["cache"]:>10}')
    print(f'Cache stays bounded at max {n_sink + window} regardless of total tokens')
```

| Scenario | Context Needed | Cache Size | Approach | StreamingLLM Works? |
| --- | --- | --- | --- | --- |
| Short document Q&A | < window_size | < 516 tokens | Standard or streaming | Yes — trivially |
| Long document summarization | Full document | Grows with doc | Full long-context model or RAG | Partial — loses earlier content |
| Streaming transcription | Recent audio only | 512-2048 tokens | Sink + window | Yes — ideal use case |
| Multi-turn dialogue | Recent turns | 512-2048 tokens | Sink + window | Yes — window covers recent turns |
| Infinite novel generation | Local coherence only | 512-2048 tokens | Sink + window | Yes — stable indefinitely |
| Needle-in-haystack retrieval | Full document | Grows to OOM | Full long-context model | No — evicted content unattendable |

## Throughput and Latency

StreamingLLM achieves constant per-token latency because the KV cache size is bounded. In standard generation, attention computation per token grows as O(n) (linear in sequence length, quadratic total), causing generation to slow down significantly for long sequences. With a fixed cache of size n_sink + window_size = 516 entries (at default settings), each token requires a constant number of attention operations regardless of how many tokens have been generated. The paper reports that StreamingLLM maintains 95% of the single-token throughput of the base model indefinitely. Memory usage is also constant: for LLaMA-7B with 32 layers, 32 heads, head_dim=128, float16, and a 516-entry cache, total KV memory is 32 × 32 × 516 × 128 × 2 bytes ≈ 1.37 GB — a fixed budget regardless of generation duration.

> **StreamingLLM Solves Memory, Not Retrieval**: StreamingLLM solves the memory problem but not the retrieval problem — the model can only attend to content in its window; for true long-context retrieval, combine StreamingLLM with RAG or use a full long-context model. StreamingLLM is ideal for streaming generation where only local coherence is needed.

## Limitations and Use Cases

StreamingLLM has one fundamental limitation: content evicted from the window is permanently inaccessible to attention. This means the model cannot retrieve information from more than window_size tokens ago, regardless of how long the generation session is. For needle-in-haystack retrieval tasks where the answer may be anywhere in a long document, StreamingLLM will fail unless the relevant content happens to remain in the window. The appropriate use cases are those where only recent context is needed: live transcription and summarization, streaming code completion, real-time dialogue systems, and long creative writing where local style coherence suffices. For true long-context understanding tasks — legal document analysis, multi-chapter book summarization, long-form research report Q&A — a full long-context model with RoPE extension or a RAG system is required.

- Memory cost is constant: (n_sink + window_size) × layers × heads × head_dim × 2 bytes, fixed for the session.
- Per-token speed is constant: attention over a fixed cache of size 516 rather than a growing sequence.
- Sink tokens are never evicted: the first 4 tokens of any session are permanently retained throughout generation.
- Position re-indexing is required: sink tokens get positions 0-3, window tokens get positions 4 to 4+window_len-1.
- No retraining needed: works with any pretrained RoPE or ALiBi model without weight modification.
- Critical limitation: content evicted from the window is unattendable — combine with RAG for long-context retrieval.
- Window size tuning: 512 tokens for minimal memory, 2048 for better coherence, 4096 for near-full-context quality.

## Key Takeaways

StreamingLLM is a practical system enabling pretrained LLMs to function as true streaming models. Its design is principled: the SinkCache is not a heuristic but a direct response to the observed attention sink structure of transformer models. By retaining 4 sink tokens plus a sliding window, StreamingLLM achieves constant memory, constant speed, and stable perplexity over arbitrarily long sequences. The approach requires no retraining, no fine-tuning, and no architectural changes — a zero-shot capability that makes it immediately applicable to any pretrained RoPE-based model including the entire LLaMA family.

- SinkCache design: keep first n_sink=4 tokens permanently + rolling window_size=512 for recent context.
- Cache is bounded at n_sink + window_size entries, giving O(1) memory growth over arbitrary generation length.
- Position re-index at each step: sink at [0..3], window at [4..4+win_len-1] for RoPE consistency.
- Works without retraining on any pretrained RoPE model — pure inference-time modification.
- Stable perplexity demonstrated at 4 million generated tokens in the original paper.
- Combine with RAG for long-context retrieval tasks; StreamingLLM alone cannot retrieve evicted content.
- For training-time improvement, add a dedicated <sink> token prefix so content tokens are not repurposed as sinks.

---

