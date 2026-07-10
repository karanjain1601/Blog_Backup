---
title: "Data Contamination — Benchmark Leakage and Decontamination in LLM Pretraining"
slug: "data-contamination-llm"
description: "How benchmark test data leaks into LLM pretraining corpora, contamination detection via n-gram overlap and MinHash, decontamination pipelines, and strategies for unbiased evaluation."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGF0YSBjb250YW1pbmF0aW9uIG9jY3VycyB3aGVuIHRlc3QgZXhhbXBsZXMgZnJvbSBldmFsdWF0aW9uIGJlbmNobWFya3MgYXBwZWFyIGluIHRoZSBwcmV0cmFpbmluZyBjb3JwdXMsIGNhdXNpbmcgaW5mbGF0ZWQgYmVuY2htYXJrIHNjb3JlcyB0aGF0IGRvIG5vdCByZWZsZWN0IGdlbnVpbmUgZ2VuZXJhbGl6YXRpb24uIEFzIExMTXMgYXJlIHRyYWluZWQgb24gaW5jcmVhc2luZ2x5IGxhcmdlIHdlYiBjcmF3bHMgKHRyaWxsaW9ucyBvZiB0b2tlbnMpLCB0aGUgcHJvYmFiaWxpdHkgdGhhdCBhbnkgZ2l2ZW4gcHVibGljIGJlbmNobWFyayBoYXMgYXQgbGVhc3Qgc29tZSBvdmVybGFwIHdpdGggdGhlIHRyYWluaW5nIGRhdGEgYXBwcm9hY2hlcyAxLiBDb250YW1pbmF0aW9uIHVuZGVybWluZXMgdGhlIHNjaWVudGlmaWMgdmFsdWUgb2YgYmVuY2htYXJrcyBhbmQgbWFrZXMgaXQgZGlmZmljdWx0IHRvIGNvbXBhcmUgbW9kZWxzIHRyYWluZWQgYXQgZGlmZmVyZW50IHRpbWVzIG9yIG9uIGRpZmZlcmVudCBkYXRhLiBHUFQtMyB3YXMgdGhlIGZpcnN0IG1ham9yIExMTSB0byBwdWJsaXNoIGEgY29udGFtaW5hdGlvbiBhbmFseXNpczsgc3Vic2VxdWVudCBtb2RlbHMgaGF2ZSBhZG9wdGVkIHZhcnlpbmcgbGV2ZWxzIG9mIHRyYW5zcGFyZW5jeSBhYm91dCBjb250YW1pbmF0aW9uIHJhdGVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlR5cGVzIG9mIEJlbmNobWFyayBDb250YW1pbmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb250YW1pbmF0aW9uIGV4aXN0cyBvbiBhIHNwZWN0cnVtIGZyb20gdmVyYmF0aW0gcmVwcm9kdWN0aW9uIHRvIHN1YnRsZSB0aGVtYXRpYyBvdmVybGFwLiBFeGFjdCBjb250YW1pbmF0aW9uIOKAlCB3aGVyZSB0aGUgdGVzdCBxdWVzdGlvbiBhbmQgYW5zd2VyIGFwcGVhciB2ZXJiYXRpbSBpbiB0cmFpbmluZyBkYXRhIOKAlCBpcyB0aGUgbW9zdCBzZXZlcmUgYW5kIGVhc2llc3QgdG8gZGV0ZWN0LiBQYXJ0aWFsIGNvbnRhbWluYXRpb24gY292ZXJzIGNhc2VzIHdoZXJlIG9ubHkgdGhlIHF1ZXN0aW9uIG9yIG9ubHkgdGhlIGFuc3dlciBhcHBlYXJzIHNlcGFyYXRlbHkgaW4gdHJhaW5pbmcgZGF0YS4gTmVhci1jb250YW1pbmF0aW9uIGludm9sdmVzIHBhcmFwaHJhc2VzIHdpdGhpbiBzbWFsbCBlZGl0IGRpc3RhbmNlIHRoYXQgYSBtb2RlbCB0cmFpbmVkIG9uIHRoZW0gd291bGQgc3RpbGwgaGF2ZSBhbiB1bmZhaXIgYWR2YW50YWdlLiBJbmRpcmVjdCBjb250YW1pbmF0aW9uIGlzIHRoZSBoYXJkZXN0IHRvIGhhbmRsZTogdHJhaW5pbmcgZXhhbXBsZXMgdGhhdCBhcmUgbm90IGZyb20gdGhlIGJlbmNobWFyayBidXQgYXJlIHNvIHNlbWFudGljYWxseSBzaW1pbGFyIHRoYXQgdGhleSBwcm92aWRlIHRoZSBhbnN3ZXIsIHN1Y2ggYXMgdGhlIG9yaWdpbmFsIHNvdXJjZSBkb2N1bWVudHMgZm9yIG11bHRpcGxlLWNob2ljZSBxdWVzdGlvbnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJFeGFjdDogdmVyYmF0aW0gcXVlc3Rpb24gKyBhbnN3ZXIgYXBwZWFyIHRvZ2V0aGVyIGluIHRyYWluaW5nIGRhdGEg4oCUIG1heGltdW0gYWR2YW50YWdlIiwiUGFydGlhbDogcXVlc3Rpb24gb3IgYW5zd2VyIGFsb25lIGluIHRyYWluaW5nIGRhdGEg4oCUIG1vZGVyYXRlIGFkdmFudGFnZSwgaGFyZCB0byBwcm92ZSBpbXBhY3QiLCJOZWFyOiBwYXJhcGhyYXNlZCB2ZXJzaW9uIHdpdGhpbiBzbWFsbCBlZGl0IGRpc3RhbmNlIChMZXZlbnNodGVpbiBcdTAwM2MyMCkg4oCUIGRldGVjdGFibGUgdmlhIE1pbkhhc2giLCJJbmRpcmVjdDogb3JpZ2luYWwgc291cmNlIG1hdGVyaWFsIChlLmcuLCBXaWtpcGVkaWEgYXJ0aWNsZXMgdW5kZXJseWluZyBNTUxVIHF1ZXN0aW9ucykg4oCUIG5lYXJseSB1bmRldGVjdGFibGUiLCJUZW1wb3JhbDogYmVuY2htYXJrIHJlbGVhc2VkIGJlZm9yZSBkYXRhIGN1dG9mZiwgY3Jhd2xlZCBsYXRlciDigJQgY29tbW9uIGZvciBuZXdlciBiZW5jaG1hcmtzIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik4tZ3JhbSBPdmVybGFwIERldGVjdGlvbiDigJQgVGhlIEdQVC0zIEFwcHJvYWNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHUFQtMyBpbnRyb2R1Y2VkIGEgc2ltcGxlIGJ1dCBlZmZlY3RpdmUgY29udGFtaW5hdGlvbiBkZXRlY3Rpb24gbWV0aG9kOiBidWlsZCBhIHNldCBvZiBhbGwgMTMtZ3JhbXMgKGNvbnRpZ3VvdXMgc2VxdWVuY2VzIG9mIDEzIHRva2VucykgZnJvbSBldmVyeSB0ZXN0IGV4YW1wbGUsIHRoZW4gc2NhbiB0aGUgdHJhaW5pbmcgY29ycHVzIGZvciBkb2N1bWVudHMgY29udGFpbmluZyBtb3JlIHRoYW4gYSB0aHJlc2hvbGQgbnVtYmVyIG9mIG1hdGNoaW5nIDEzLWdyYW1zLiBBIGRvY3VtZW50IGlzIGZsYWdnZWQgaWYgaXQgaGFzIDUgb3IgbW9yZSBvdmVybGFwcGluZyAxMy1ncmFtcyB3aXRoIGFueSBiZW5jaG1hcmsgZXhhbXBsZS4gMTMgdG9rZW5zIGlzIGNob3NlbiBiZWNhdXNlIGl0IGlzIGxvbmcgZW5vdWdoIHRvIGJlIGEgbWVhbmluZ2Z1bCBwaHJhc2UgdGhhdCB1bmlxdWVseSBpZGVudGlmaWVzIGEgYmVuY2htYXJrIGV4YW1wbGUsIHlldCBzaG9ydCBlbm91Z2ggdG8gY2F0Y2ggbmVhci1leGFjdCBjb3BpZXMuIFRoZSB0aHJlc2hvbGQgb2YgNSByZWR1Y2VzIGZhbHNlIHBvc2l0aXZlcyBmcm9tIGNvbW1vbmx5IG9jY3VycmluZyBwaHJhc2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IGRlZmF1bHRkaWN0XG5cbmRlZiBidWlsZF9uZ3JhbXModGV4dCwgbj0xMyk6XG4gICAgXCJcIlwiQnVpbGQgYSBzZXQgb2Ygbi1ncmFtIHR1cGxlcyBmcm9tIHdoaXRlc3BhY2UtdG9rZW5pemVkIHRleHQuXCJcIlwiXG4gICAgdG9rZW5zID0gcmUuc3ViKHJcdTAwMjdbXlxcd1xcc11cdTAwMjcsIFx1MDAyNyBcdTAwMjcsIHRleHQubG93ZXIoKSkuc3BsaXQoKVxuICAgIHJldHVybiBzZXQodHVwbGUodG9rZW5zW2k6aStuXSkgZm9yIGkgaW4gcmFuZ2UobGVuKHRva2VucykgLSBuICsgMSkpXG5cbmRlZiBzY2FuX2NvcnB1c19jb250YW1pbmF0aW9uKGJlbmNobWFya19leGFtcGxlcywgY29ycHVzX2RvY3MsIG49MTMsIHRocmVzaG9sZD01KTpcbiAgICBcIlwiXCJGbGFnIHRyYWluaW5nIGRvY3VtZW50cyB3aXRoIFx1MDAzZT0gdGhyZXNob2xkIG92ZXJsYXBwaW5nIG4tZ3JhbXMgd2l0aCBhbnkgYmVuY2htYXJrIGV4YW1wbGUuXCJcIlwiXG4gICAgYmVuY2hfbmdyYW1zID0gc2V0KClcbiAgICBmb3IgZXggaW4gYmVuY2htYXJrX2V4YW1wbGVzOlxuICAgICAgICB0ZXh0ID0gZXguZ2V0KFx1MDAyN3F1ZXN0aW9uXHUwMDI3LCBcdTAwMjdcdTAwMjcpICsgXHUwMDI3IFx1MDAyNyArIGV4LmdldChcdTAwMjdhbnN3ZXJcdTAwMjcsIFx1MDAyN1x1MDAyNylcbiAgICAgICAgYmVuY2hfbmdyYW1zLnVwZGF0ZShidWlsZF9uZ3JhbXModGV4dCwgbikpXG5cbiAgICBjb250YW1pbmF0ZWQgPSBbXVxuICAgIGZvciBkb2NfaWQsIGRvY190ZXh0IGluIGVudW1lcmF0ZShjb3JwdXNfZG9jcyk6XG4gICAgICAgIGRvY19uZ3JhbXMgPSBidWlsZF9uZ3JhbXMoZG9jX3RleHQsIG4pXG4gICAgICAgIG92ZXJsYXAgICAgPSBsZW4oZG9jX25ncmFtcyBcdTAwMjYgYmVuY2hfbmdyYW1zKVxuICAgICAgICBpZiBvdmVybGFwIFx1MDAzZT0gdGhyZXNob2xkOlxuICAgICAgICAgICAgY29udGFtaW5hdGVkLmFwcGVuZCh7XHUwMDI3ZG9jX2lkXHUwMDI3OiBkb2NfaWQsIFx1MDAyN292ZXJsYXBfY291bnRcdTAwMjc6IG92ZXJsYXAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcdTAwMjdwcmV2aWV3XHUwMDI3OiBkb2NfdGV4dFs6MTAwXX0pXG4gICAgcmV0dXJuIGNvbnRhbWluYXRlZFxuXG4jIE1pbmltYWwgcmVwcm9kdWNpYmxlIGV4YW1wbGVcbmJlbmNobWFyayA9IFtcbiAgICB7XHUwMDI3cXVlc3Rpb25cdTAwMjc6IFx1MDAyN1doYXQgbmV1cm90cmFuc21pdHRlciBpcyBwcmltYXJpbHkgYXNzb2NpYXRlZCB3aXRoIHJld2FyZCBwYXRod2F5cyBpbiB0aGUgYnJhaW5cdTAwMjcsXG4gICAgIFx1MDAyN2Fuc3dlclx1MDAyNzogXHUwMDI3ZG9wYW1pbmUgaXMgYXNzb2NpYXRlZCB3aXRoIHJld2FyZCBtb3RpdmF0aW9uIGFuZCBwbGVhc3VyZVx1MDAyN30sXG4gICAge1x1MDAyN3F1ZXN0aW9uXHUwMDI3OiBcdTAwMjdTb2x2ZSB0aGUgcmVjdXJyZW5jZSByZWxhdGlvbiBUIG9mIG4gZXF1YWxzIHR3byBUIG9mIG4gb3ZlciB0d28gcGx1cyBuXHUwMDI3LFxuICAgICBcdTAwMjdhbnN3ZXJcdTAwMjc6IFx1MDAyN0J5IG1hc3RlciB0aGVvcmVtIFQgb2YgbiBpcyB0aGV0YSBuIGxvZyBuXHUwMDI3fSxcbl1cbmNvcnB1cyA9IFtcbiAgICBcdTAwMjdkb3BhbWluZSBpcyBhc3NvY2lhdGVkIHdpdGggcmV3YXJkIG1vdGl2YXRpb24gYW5kIHBsZWFzdXJlIGluIHRoZSB2ZW50cmFsIHRlZ21lbnRhbCBhcmVhIG51Y2xldXMgYWNjdW1iZW5zXHUwMDI3LFxuICAgIFx1MDAyN3RyYW5zZm9ybWVycyB1c2Ugc2VsZi1hdHRlbnRpb24gdG8gcHJvY2VzcyBhbGwgdG9rZW5zIGluIHBhcmFsbGVsIHdpdGhvdXQgc2VxdWVudGlhbCBjb21wdXRhdGlvblx1MDAyNyxcbiAgICBcdTAwMjdCeSBtYXN0ZXIgdGhlb3JlbSBUIG9mIG4gaXMgdGhldGEgbiBsb2cgbiBmb3IgZGl2aWRlIGFuZCBjb25xdWVyIHJlY3VycmVuY2VzIHdpdGggYmFsYW5jZWQgc3BsaXRzXHUwMDI3LFxuXVxuZmxhZ2dlZCA9IHNjYW5fY29ycHVzX2NvbnRhbWluYXRpb24oYmVuY2htYXJrLCBjb3JwdXMsIG49NSwgdGhyZXNob2xkPTMpXG5wcmludChmXCJDb250YW1pbmF0ZWQgZG9jczoge2xlbihmbGFnZ2VkKX0ve2xlbihjb3JwdXMpfVwiKVxuZm9yIHIgaW4gZmxhZ2dlZDpcbiAgICBwcmludChmXCIgIERvYyB7cltcdTAwMjdkb2NfaWRcdTAwMjddfToge3JbXHUwMDI3b3ZlcmxhcF9jb3VudFx1MDAyN119IG92ZXJsYXBwaW5nIG4tZ3JhbXMg4oCUIHtyW1x1MDAyN3ByZXZpZXdcdTAwMjddIXI6LjYwfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1pbkhhc2ggTmVhci1EdXBsaWNhdGUgRGVjb250YW1pbmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOLWdyYW0gZXhhY3QgbWF0Y2hpbmcgbWlzc2VzIHBhcmFwaHJhc2VkIGNvbnRhbWluYXRpb24uIE1pbkhhc2ggcHJvdmlkZXMgYXBwcm94aW1hdGUgSmFjY2FyZCBzaW1pbGFyaXR5IGJldHdlZW4gZG9jdW1lbnRzIHdpdGhvdXQgY29tcGFyaW5nIGFsbCBuLWdyYW0gcGFpcnMuIEEgTWluSGFzaCBzaWduYXR1cmUgb2YgYSBkb2N1bWVudCBpcyBhIGZpeGVkLWxlbmd0aCB2ZWN0b3Igb2YgbWluaW11bSBoYXNoIHZhbHVlczsgdGhlIGZyYWN0aW9uIG9mIHNpZ25hdHVyZSBwb3NpdGlvbnMgd2hlcmUgdHdvIGRvY3VtZW50cyBhZ3JlZSBpcyBhbiB1bmJpYXNlZCBlc3RpbWF0b3Igb2YgSmFjY2FyZCBzaW1pbGFyaXR5LiBVc2luZyAxMjggaGFzaCBmdW5jdGlvbnMgZ2l2ZXMgYW4gZXN0aW1hdGlvbiB2YXJpYW5jZSBvZiB+MC4wMS4gRG9jdW1lbnRzIHdpdGggZXN0aW1hdGVkIEphY2NhcmQgc2ltaWxhcml0eSBhYm92ZSAwLjUgd2l0aCBhbnkgYmVuY2htYXJrIGV4YW1wbGUgYXJlIGZsYWdnZWQgYXMgbmVhci1jb250YW1pbmF0ZWQuIEluIHByYWN0aWNlLCBsb2NhbGl0eS1zZW5zaXRpdmUgaGFzaGluZyAoTFNIKSBhbGxvd3Mgc3ViLWxpbmVhciBsb29rdXAg4oCUIGVzc2VudGlhbCB3aGVuIHRoZSB0cmFpbmluZyBjb3JwdXMgaGFzIGJpbGxpb25zIG9mIGRvY3VtZW50cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHJlXG5pbXBvcnQgcmFuZG9tXG5mcm9tIHR5cGluZyBpbXBvcnQgTGlzdFxuXG5kZWYgc2hpbmdsZV9zZXQodGV4dCwgaz01KTpcbiAgICBcIlwiXCJCdWlsZCB3b3JkIGstc2hpbmdsZSAoay1ncmFtKSBzZXQgZnJvbSB0ZXh0IGZvciBKYWNjYXJkIGVzdGltYXRpb24uXCJcIlwiXG4gICAgdG9rZW5zID0gcmUuc3ViKHJcdTAwMjdbXlxcd1xcc11cdTAwMjcsIFx1MDAyNyBcdTAwMjcsIHRleHQubG93ZXIoKSkuc3BsaXQoKVxuICAgIHJldHVybiBzZXQodHVwbGUodG9rZW5zW2k6aStrXSkgZm9yIGkgaW4gcmFuZ2UobGVuKHRva2VucyktaysxKSlcblxuZGVmIG1pbmhhc2hfc2lnbmF0dXJlKHNoaW5nbGVzLCBudW1faGFzaGVzPTEyOCwgc2VlZD0wKTpcbiAgICBcIlwiXCJDb21wdXRlIE1pbkhhc2ggc2lnbmF0dXJlOiB2ZWN0b3Igb2YgbWluIGhhc2ggdmFsdWVzIG92ZXIgc2hpbmdsZXMuXCJcIlwiXG4gICAgcm5nID0gcmFuZG9tLlJhbmRvbShzZWVkKVxuICAgIHBhcmFtcyA9IFsocm5nLnJhbmRpbnQoMSwgMioqMzEtMSksIHJuZy5yYW5kaW50KDAsIDIqKjMxLTEpKSBmb3IgXyBpbiByYW5nZShudW1faGFzaGVzKV1cbiAgICBzaWcgPSBbXVxuICAgIGZvciBhLCBiIGluIHBhcmFtczpcbiAgICAgICAgbWluX3ZhbCA9IG1pbigoKGEgKiBoYXNoKHMpICsgYikgJSAoMioqMzEgLSAxKSkgZm9yIHMgaW4gc2hpbmdsZXMpIGlmIHNoaW5nbGVzIGVsc2UgMFxuICAgICAgICBzaWcuYXBwZW5kKG1pbl92YWwpXG4gICAgcmV0dXJuIHNpZ1xuXG5kZWYgamFjY2FyZF9mcm9tX3NpZ3Moc2lnMSwgc2lnMik6XG4gICAgcmV0dXJuIHN1bShhID09IGIgZm9yIGEsIGIgaW4gemlwKHNpZzEsIHNpZzIpKSAvIGxlbihzaWcxKVxuXG5kZWYgbWluaGFzaF9kZWNvbnRhbWluYXRlKGJlbmNobWFya19leGFtcGxlcywgdHJhaW5fZG9jcywgdGhyZXNob2xkPTAuNCwgbnVtX2hhc2hlcz0xMjgsIGs9NSk6XG4gICAgdGVzdF9zaWdzID0gW21pbmhhc2hfc2lnbmF0dXJlKHNoaW5nbGVfc2V0KGV4LmdldChcdTAwMjdxdWVzdGlvblx1MDAyNyxcdTAwMjdcdTAwMjcpICsgXHUwMDI3IFx1MDAyNyArIGV4LmdldChcdTAwMjdhbnN3ZXJcdTAwMjcsXHUwMDI3XHUwMDI3KSwgayksIG51bV9oYXNoZXMpXG4gICAgICAgICAgICAgICAgIGZvciBleCBpbiBiZW5jaG1hcmtfZXhhbXBsZXNdXG4gICAgZmxhZ2dlZCA9IFtdXG4gICAgZm9yIGksIGRvYyBpbiBlbnVtZXJhdGUodHJhaW5fZG9jcyk6XG4gICAgICAgIGRvY19zaWcgPSBtaW5oYXNoX3NpZ25hdHVyZShzaGluZ2xlX3NldChkb2MsIGspLCBudW1faGFzaGVzKVxuICAgICAgICBtYXhfc2ltICA9IG1heChqYWNjYXJkX2Zyb21fc2lncyhkb2Nfc2lnLCB0cykgZm9yIHRzIGluIHRlc3Rfc2lncylcbiAgICAgICAgaWYgbWF4X3NpbSBcdTAwM2U9IHRocmVzaG9sZDpcbiAgICAgICAgICAgIGZsYWdnZWQuYXBwZW5kKHtcdTAwMjd0cmFpbl9pZHhcdTAwMjc6IGksIFx1MDAyN21heF9qYWNjYXJkXHUwMDI3OiByb3VuZChtYXhfc2ltLCAzKX0pXG4gICAgcmV0dXJuIGZsYWdnZWRcblxudGVzdF9zZXQgPSBbe1x1MDAyN3F1ZXN0aW9uXHUwMDI3OiBcdTAwMjdXaGF0IGlzIHRoZSBib2lsaW5nIHBvaW50IG9mIHdhdGVyIGF0IHN0YW5kYXJkIHByZXNzdXJlXHUwMDI3LCBcdTAwMjdhbnN3ZXJcdTAwMjc6IFx1MDAyNzEwMCBkZWdyZWVzIENlbHNpdXMgYXQgb25lIGF0bW9zcGhlcmVcdTAwMjd9XVxudHJhaW4gICAgPSBbXG4gICAgXHUwMDI3VGhlIGJvaWxpbmcgcG9pbnQgb2Ygd2F0ZXIgYXQgc3RhbmRhcmQgcHJlc3N1cmUgb25lIGF0bW9zcGhlcmUgaXMgMTAwIGRlZ3JlZXMgQ2Vsc2l1cyBvciAyMTIgRmFocmVuaGVpdFx1MDAyNyxcbiAgICBcdTAwMjdOZXVyYWwgbmV0d29ya3MgbGVhcm4gZGF0YSByZXByZXNlbnRhdGlvbnMgdGhyb3VnaCBncmFkaWVudCBkZXNjZW50IGFuZCBiYWNrcHJvcGFnYXRpb25cdTAwMjcsXG4gICAgXHUwMDI3V2F0ZXIgYm9pbHMgYXQgMTAwIGRlZ3JlZXMgQ2Vsc2l1cyBhdCBvbmUgYXRtb3NwaGVyZSBwcmVzc3VyZSBzdGFuZGFyZCBjb25kaXRpb25zIHNlYSBsZXZlbFx1MDAyNyxcbl1cbnJlc3VsdHMgPSBtaW5oYXNoX2RlY29udGFtaW5hdGUodGVzdF9zZXQsIHRyYWluLCB0aHJlc2hvbGQ9MC4zKVxucHJpbnQoZlwiRmxhZ2dlZDoge2xlbihyZXN1bHRzKX0ve2xlbih0cmFpbil9IHRyYWluaW5nIGRvY3NcIilcbmZvciByIGluIHJlc3VsdHM6XG4gICAgcHJpbnQoZlwiICBUcmFpblt7cltcdTAwMjd0cmFpbl9pZHhcdTAwMjddfV06IEphY2NhcmQ9e3JbXHUwMDI3bWF4X2phY2NhcmRcdTAwMjddfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbnRhbWluYXRpb24gUmF0ZSBSZXBvcnRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlc3BvbnNpYmxlIGNvbnRhbWluYXRpb24gcmVwb3J0aW5nIHJlcXVpcmVzIHJ1bm5pbmcgZGV0ZWN0aW9uIG9uIGV2ZXJ5IGJlbmNobWFyayB1c2VkIGluIGV2YWx1YXRpb24sIHJlcG9ydGluZyBwZXItYmVuY2htYXJrIGNvbnRhbWluYXRpb24gcmF0ZXMsIGFuZCBzaG93aW5nIHRoYXQgY29udGFtaW5hdGVkIGV4YW1wbGVzIGRvIG5vdCBzaWduaWZpY2FudGx5IGNoYW5nZSBhZ2dyZWdhdGUgc2NvcmVzLiBUaGUgR1BULTQgdGVjaG5pY2FsIHJlcG9ydCByYW4gY29udGFtaW5hdGlvbiBhbmFseXNpcyBhY3Jvc3MgYWxsIG1ham9yIGJlbmNobWFya3MgYW5kIHJlcG9ydGVkIHRoYXQgY29udGFtaW5hdGlvbiByYXRlcyB3ZXJlIGxvdyBhbmQgZGlkIG5vdCBzdWJzdGFudGlhbGx5IGluZmxhdGUgc2NvcmVzLiBIb3dldmVyLCBjb250YW1pbmF0aW9uIGFuYWx5c2lzIG1ldGhvZG9sb2d5IHZhcmllcyB3aWRlbHkg4oCUIGRpZmZlcmVudCBuIHZhbHVlcywgdGhyZXNob2xkcywgYW5kIHRva2VuaXphdGlvbiBjaG9pY2VzIHByb2R1Y2UgdmVyeSBkaWZmZXJlbnQgY29udGFtaW5hdGlvbiByYXRlcyBmb3IgdGhlIHNhbWUgY29ycHVzIGFuZCBiZW5jaG1hcmsgY29tYmluYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCByZVxuXG5kZWYgbmdyYW1zX3NldCh0ZXh0LCBuKTpcbiAgICB0b2tlbnMgPSByZS5zdWIoclx1MDAyN1teXFx3XFxzXVx1MDAyNywgXHUwMDI3IFx1MDAyNywgdGV4dC5sb3dlcigpKS5zcGxpdCgpXG4gICAgcmV0dXJuIHNldCh0dXBsZSh0b2tlbnNbaTppK25dKSBmb3IgaSBpbiByYW5nZShsZW4odG9rZW5zKS1uKzEpKVxuXG5kZWYgY29udGFtaW5hdGlvbl9yYXRlKGJlbmNobWFya19leGFtcGxlcywgdHJhaW5fdGV4dCwgbj0xMywgbWluX292ZXJsYXA9NSk6XG4gICAgXCJcIlwiUmV0dXJuIGZyYWN0aW9uIG9mIGJlbmNobWFyayBleGFtcGxlcyB3aXRoIFx1MDAzZT1taW5fb3ZlcmxhcCBuLWdyYW0gbWF0Y2hlcyBpbiB0cmFpbi5cIlwiXCJcbiAgICB0cmFpbl9uZ3JhbXMgICAgPSBuZ3JhbXNfc2V0KHRyYWluX3RleHQsIG4pXG4gICAgY29udGFtaW5hdGVkICAgID0gMFxuICAgIGRldGFpbHMgICAgICAgICA9IFtdXG4gICAgZm9yIGV4IGluIGJlbmNobWFya19leGFtcGxlczpcbiAgICAgICAgdGV4dCAgICAgPSBleC5nZXQoXHUwMDI3cXVlc3Rpb25cdTAwMjcsXHUwMDI3XHUwMDI3KSArIFx1MDAyNyBcdTAwMjcgKyBleC5nZXQoXHUwMDI3YW5zd2VyXHUwMDI3LFx1MDAyN1x1MDAyNylcbiAgICAgICAgZXhfbmcgICAgPSBuZ3JhbXNfc2V0KHRleHQsIG4pXG4gICAgICAgIG92ZXJsYXAgID0gbGVuKGV4X25nIFx1MDAyNiB0cmFpbl9uZ3JhbXMpXG4gICAgICAgIGlzX2NvbnQgID0gb3ZlcmxhcCBcdTAwM2U9IG1pbl9vdmVybGFwXG4gICAgICAgIGNvbnRhbWluYXRlZCArPSBpbnQoaXNfY29udClcbiAgICAgICAgZGV0YWlscy5hcHBlbmQoe1x1MDAyN2NvbnRhbWluYXRlZFx1MDAyNzogaXNfY29udCwgXHUwMDI3b3ZlcmxhcFx1MDAyNzogb3ZlcmxhcH0pXG4gICAgcmF0ZSA9IGNvbnRhbWluYXRlZCAvIGxlbihiZW5jaG1hcmtfZXhhbXBsZXMpIGlmIGJlbmNobWFya19leGFtcGxlcyBlbHNlIDAuMFxuICAgIHJldHVybiB7XHUwMDI3dG90YWxcdTAwMjc6IGxlbihiZW5jaG1hcmtfZXhhbXBsZXMpLCBcdTAwMjdjb250YW1pbmF0ZWRcdTAwMjc6IGNvbnRhbWluYXRlZCxcbiAgICAgICAgICAgIFx1MDAyN3JhdGVcdTAwMjc6IHJvdW5kKHJhdGUsIDQpLCBcdTAwMjdkZXRhaWxzXHUwMDI3OiBkZXRhaWxzfVxuXG4jIFNpbXVsYXRlIGZvciB0aHJlZSBiZW5jaG1hcmsgc3Vic2V0c1xudHJhaW5fYmxvYiA9IChcdTAwMjdkb3BhbWluZSBpcyBhc3NvY2lhdGVkIHdpdGggcmV3YXJkIG1vdGl2YXRpb24gaW4gbnVjbGV1cyBhY2N1bWJlbnMgXHUwMDI3XG4gICAgICAgICAgICAgIFx1MDAyN3NvbHZlIHF1YWRyYXRpYyBieSBjb21wbGV0aW5nIHRoZSBzcXVhcmUgeCBzcXVhcmVkIHBsdXMgZml2ZSB4IHBsdXMgc2l4IFx1MDAyN1xuICAgICAgICAgICAgICBcdTAwMjd3YXRlciBib2lscyBhdCAxMDAgZGVncmVlcyBDZWxzaXVzIHN0YW5kYXJkIGNvbmRpdGlvbnMgc2VhIGxldmVsIHByZXNzdXJlXHUwMDI3KVxuYmVuY2htYXJrcyA9IHtcbiAgICBcdTAwMjdNTUxVXHUwMDI3OiAgW3tcdTAwMjdxdWVzdGlvblx1MDAyNzogXHUwMDI3ZG9wYW1pbmUgaXMgYXNzb2NpYXRlZCB3aXRoIHJld2FyZCBtb3RpdmF0aW9uIGluIG51Y2xldXMgYWNjdW1iZW5zXHUwMDI3LCBcdTAwMjdhbnN3ZXJcdTAwMjc6IFx1MDAyN2NvcnJlY3QgYW5zd2VyIEFcdTAwMjd9XSxcbiAgICBcdTAwMjdHU004S1x1MDAyNzogW3tcdTAwMjdxdWVzdGlvblx1MDAyNzogXHUwMDI3c29sdmUgcXVhZHJhdGljIGJ5IGNvbXBsZXRpbmcgdGhlIHNxdWFyZSBtZXRob2RcdTAwMjcsIFx1MDAyN2Fuc3dlclx1MDAyNzogXHUwMDI3eCBlcXVhbHMgcm9vdCB2YWx1ZXNcdTAwMjd9XSxcbiAgICBcdTAwMjdBUkNcdTAwMjc6ICAgW3tcdTAwMjdxdWVzdGlvblx1MDAyNzogXHUwMDI3d2hhdCBpcyB0aGUgbGFyZ2VzdCBwbGFuZXQgaW4gdGhlIHNvbGFyIHN5c3RlbVx1MDAyNywgXHUwMDI3YW5zd2VyXHUwMDI3OiBcdTAwMjdKdXBpdGVyIGhhcyBsYXJnZXN0IG1hc3NcdTAwMjd9XSxcbn1cbmZvciBuYW1lLCBleGFtcGxlcyBpbiBiZW5jaG1hcmtzLml0ZW1zKCk6XG4gICAgciA9IGNvbnRhbWluYXRpb25fcmF0ZShleGFtcGxlcywgdHJhaW5fYmxvYiwgbj00LCBtaW5fb3ZlcmxhcD0yKVxuICAgIHByaW50KGZcIntuYW1lfToge3JbXHUwMDI3Y29udGFtaW5hdGVkXHUwMDI3XX0ve3JbXHUwMDI3dG90YWxcdTAwMjddfSBjb250YW1pbmF0ZWQgKHtyW1x1MDAyN3JhdGVcdTAwMjddOi4xJX0pXCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJJbmZvIiwiY29udGVudCI6IkNvbnRhbWluYXRpb24gZGV0ZWN0aW9uIHdpdGggMTMtZ3JhbSBtYXRjaGluZyBoYXMgaGlnaCBmYWxzZSBwb3NpdGl2ZSByYXRlIGZvciBjb21tb24gcGhyYXNlcyDigJQgYWx3YXlzIG1hbnVhbGx5IHJldmlldyBmbGFnZ2VkIGV4YW1wbGVzIGJlZm9yZSByZW1vdmFsIHRvIGF2b2lkIGRlY29udGFtaW5hdGluZyB1bnJlbGF0ZWQgZG9jdW1lbnRzIHRoYXQgaGFwcGVuIHRvIHNoYXJlIGNvbW1vbiBwaHJhc2VzIHdpdGggYmVuY2htYXJrcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZWNvbnRhbWluYXRpb24gUGlwZWxpbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgZGVjb250YW1pbmF0aW9uIHBpcGVsaW5lIHJ1bnMgYmVmb3JlIHRoZSBmaW5hbCBkYXRhIG1peCBpcyBmcm96ZW46IGNvbGxlY3QgYWxsIGJlbmNobWFyayBleGFtcGxlcyBzY2hlZHVsZWQgZm9yIGV2YWx1YXRpb24sIGV4dHJhY3Qgbi1ncmFtcywgc2NhbiB0aGUgdHJhaW5pbmcgY29ycHVzLCByZW1vdmUgZmxhZ2dlZCBkb2N1bWVudHMsIGFuZCByZWdlbmVyYXRlIHRva2VuIGNvdW50IHN0YXRpc3RpY3MuIFRoZSBvcmRlciBtYXR0ZXJzIOKAlCBkZWNvbnRhbWluYXRpb24gc2hvdWxkIHJ1biBhZnRlciBvdGhlciBmaWx0ZXJpbmcgc3RlcHMgKHF1YWxpdHkgZmlsdGVyLCBkZWR1cGxpY2F0aW9uKSBidXQgYmVmb3JlIHRyYWluaW5nIGRhdGEgdG9rZW5pemF0aW9uLiBSZS1ydW5uaW5nIGRlY29udGFtaW5hdGlvbiB3aXRoIHRoZSBmaW5hbCBiZW5jaG1hcmsgc2V0IGF0IHRoZSBlbmQgb2YgZGF0YSBwcmVwYXJhdGlvbiBpcyBlc3NlbnRpYWwgYmVjYXVzZSBiZW5jaG1hcmsgc2VsZWN0aW9uIG9mdGVuIGNoYW5nZXMgZHVyaW5nIGRldmVsb3BtZW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmltcG9ydCBqc29uXG5cbmRlZiBuZ3JhbXNfc2V0KHRleHQsIG4pOlxuICAgIHRva2VucyA9IHJlLnN1YihyXHUwMDI3W15cXHdcXHNdXHUwMDI3LCBcdTAwMjcgXHUwMDI3LCB0ZXh0Lmxvd2VyKCkpLnNwbGl0KClcbiAgICByZXR1cm4gc2V0KHR1cGxlKHRva2Vuc1tpOmkrbl0pIGZvciBpIGluIHJhbmdlKGxlbih0b2tlbnMpLW4rMSkpXG5cbmRlZiBidWlsZF9iZW5jaG1hcmtfbmdyYW1zKGJlbmNobWFya19maWxlcywgbj0xMyk6XG4gICAgXCJcIlwiTG9hZCBiZW5jaG1hcmsgSlNPTiBmaWxlcyBhbmQgYnVpbGQgY29tYmluZWQgbi1ncmFtIHNldCBmcm9tIGFsbCBleGFtcGxlcy5cIlwiXCJcbiAgICBhbGxfbmdyYW1zID0gc2V0KClcbiAgICBmb3IgcGF0aCBpbiBiZW5jaG1hcmtfZmlsZXM6XG4gICAgICAgIHdpdGggb3BlbihwYXRoKSBhcyBmOlxuICAgICAgICAgICAgZXhhbXBsZXMgPSBqc29uLmxvYWQoZilcbiAgICAgICAgZm9yIGV4IGluIGV4YW1wbGVzOlxuICAgICAgICAgICAgdGV4dCA9IGV4LmdldChcdTAwMjdxdWVzdGlvblx1MDAyNyxcdTAwMjdcdTAwMjcpICsgXHUwMDI3IFx1MDAyNyArIGV4LmdldChcdTAwMjdjaG9pY2VzXHUwMDI3LFx1MDAyN1x1MDAyNykgKyBcdTAwMjcgXHUwMDI3ICsgZXguZ2V0KFx1MDAyN2Fuc3dlclx1MDAyNyxcdTAwMjdcdTAwMjcpXG4gICAgICAgICAgICBhbGxfbmdyYW1zLnVwZGF0ZShuZ3JhbXNfc2V0KHRleHQsIG4pKVxuICAgIHJldHVybiBhbGxfbmdyYW1zXG5cbmRlZiBkZWNvbnRhbWluYXRlX2NvcnB1cyh0cmFpbl9kb2NzLCBiZW5jaF9uZ3JhbXMsIG49MTMsIG92ZXJsYXBfdGhyZXNob2xkPTUpOlxuICAgIFwiXCJcIlJlbW92ZSB0cmFpbmluZyBkb2N1bWVudHMgd2l0aCBcdTAwM2U9IG92ZXJsYXBfdGhyZXNob2xkIG92ZXJsYXBwaW5nIG4tZ3JhbXMuXCJcIlwiXG4gICAgY2xlYW5fZG9jcywgcmVtb3ZlZCA9IFtdLCBbXVxuICAgIGZvciBpZHgsIGRvYyBpbiBlbnVtZXJhdGUodHJhaW5fZG9jcyk6XG4gICAgICAgIGRvY19uZyAgPSBuZ3JhbXNfc2V0KGRvY1tcdTAwMjd0ZXh0XHUwMDI3XSwgbilcbiAgICAgICAgb3ZlcmxhcCA9IGxlbihkb2NfbmcgXHUwMDI2IGJlbmNoX25ncmFtcylcbiAgICAgICAgaWYgb3ZlcmxhcCBcdTAwM2Mgb3ZlcmxhcF90aHJlc2hvbGQ6XG4gICAgICAgICAgICBjbGVhbl9kb2NzLmFwcGVuZChkb2MpXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICByZW1vdmVkLmFwcGVuZCh7XHUwMDI3aWR4XHUwMDI3OiBpZHgsIFx1MDAyN292ZXJsYXBcdTAwMjc6IG92ZXJsYXAsIFx1MDAyN3ByZXZpZXdcdTAwMjc6IGRvY1tcdTAwMjd0ZXh0XHUwMDI3XVs6ODBdfSlcbiAgICByZXR1cm4gY2xlYW5fZG9jcywgcmVtb3ZlZFxuXG4jIFNpbXVsYXRlIHdpdGggaW4tbWVtb3J5IGJlbmNobWFyayBuLWdyYW1zXG5iZW5jaF9uZ3JhbXMgPSBuZ3JhbXNfc2V0KFx1MDAyN2RvcGFtaW5lIHJld2FyZCBtb3RpdmF0aW9uIG51Y2xldXMgYWNjdW1iZW5zIHZlbnRyYWwgdGVnbWVudGFsXHUwMDI3LCBuPTQpXG50cmFpbl9jb3JwdXMgPSBbXG4gICAge1x1MDAyN2lkXHUwMDI3OiAwLCBcdTAwMjd0ZXh0XHUwMDI3OiBcdTAwMjdkb3BhbWluZSByZXdhcmQgbW90aXZhdGlvbiBudWNsZXVzIGFjY3VtYmVucyB2ZW50cmFsIHRlZ21lbnRhbCBhcmVhIGJhc2FsIGdhbmdsaWFcdTAwMjd9LFxuICAgIHtcdTAwMjdpZFx1MDAyNzogMSwgXHUwMDI3dGV4dFx1MDAyNzogXHUwMDI3dHJhbnNmb3JtZXIgYXR0ZW50aW9uIHNjYWxlcyBxdWFkcmF0aWNhbGx5IHdpdGggc2VxdWVuY2UgbGVuZ3RoIGluIHRoZSB3b3JzdCBjYXNlXHUwMDI3fSxcbiAgICB7XHUwMDI3aWRcdTAwMjc6IDIsIFx1MDAyN3RleHRcdTAwMjc6IFx1MDAyN3Jld2FyZCBtb3RpdmF0aW9uIG51Y2xldXMgYWNjdW1iZW5zIGlzIGtleSB0byB1bmRlcnN0YW5kaW5nIGFkZGljdGlvbiBhbmQgYmVoYXZpb3JcdTAwMjd9LFxuXVxuY2xlYW4sIHJlbW92ZWQgPSBkZWNvbnRhbWluYXRlX2NvcnB1cyh0cmFpbl9jb3JwdXMsIGJlbmNoX25ncmFtcywgbj00LCBvdmVybGFwX3RocmVzaG9sZD0zKVxucHJpbnQoZlwiT3JpZ2luYWw6IHtsZW4odHJhaW5fY29ycHVzKX0gIFJlbW92ZWQ6IHtsZW4ocmVtb3ZlZCl9ICBDbGVhbjoge2xlbihjbGVhbil9XCIpXG5mb3IgciBpbiByZW1vdmVkOlxuICAgIHByaW50KGZcIiAgUmVtb3ZlZCBkb2Mge3JbXHUwMDI3aWR4XHUwMDI3XX06IHtyW1x1MDAyN292ZXJsYXBcdTAwMjddfSBvdmVybGFwcGluZyBuLWdyYW1zXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmVuY2htYXJrIENvbnRhbWluYXRpb24gUmF0ZXMgaW4gTWFqb3IgTExNcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIk1NTFUgJSIsIkhlbGxhU3dhZyAlIiwiR1NNOEsgJSIsIkFSQyAlIiwiRGV0ZWN0aW9uIE1ldGhvZCJdLCJyb3dzIjpbWyJHUFQtMyAxNzVCIiwifjIuMiUiLCJ+My4xJSIsIk4vQSIsIn4yLjglIiwiMTMtZ3JhbSBvdmVybGFwLCB0aHJlc2hvbGQgNSJdLFsiR1BULTQiLCJcdTAwM2MxLjAlIiwiXHUwMDNjMS41JSIsIn4wLjglIiwiXHUwMDNjMS4wJSIsIkdQVC00IGNvbnRhbWluYXRpb24gYW5hbHlzaXMiXSxbIkxMYU1BLTIgNzBCIiwifjIuNCUiLCJ+MS44JSIsIn4zLjIlIiwifjIuMSUiLCJOLWdyYW0gKyBtYW51YWwgcmV2aWV3Il0sWyJNaXN0cmFsIDdCIiwifjEuMSUiLCJ+MC45JSIsIn4xLjQlIiwifjAuNyUiLCJQcm9wcmlldGFyeSAodW5kaXNjbG9zZWQgdGhyZXNob2xkKSJdLFsiRGVlcFNlZWstVjIiLCJcdTAwM2MwLjUlIiwiXHUwMDNjMC41JSIsIn4wLjYlIiwiXHUwMDNjMC41JSIsIlN1YnN0cmluZyBtYXRjaCBkZWR1cGxpY2F0aW9uIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcnVlIEV2YWx1YXRpb24g4oCUIEF2b2lkaW5nIENvbnRhbWluYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjbGVhbmVzdCBzb2x1dGlvbiB0byBiZW5jaG1hcmsgY29udGFtaW5hdGlvbiBpcyB0byBldmFsdWF0ZSBvbiB1bnB1Ymxpc2hlZCBiZW5jaG1hcmtzIHRoYXQgd2VyZSBuZXZlciBvbiB0aGUgcHVibGljIGludGVybmV0LiBTZXZlcmFsIHJlc2VhcmNoIGdyb3VwcyBtYWludGFpbiBwcml2YXRlIGV2YWx1YXRpb24gc2V0cyByZWxlYXNlZCBvbmx5IGFmdGVyIHRyYWluaW5nIGRhdGEgY3V0b2ZmLiBEeW5hbWljIGJlbmNobWFya2luZyDigJQgZ2VuZXJhdGluZyBuZXcgcHJvYmxlbXMgYXQgZXZhbHVhdGlvbiB0aW1lIHZpYSB0ZW1wbGF0ZXMgb3IgTExNLWdlbmVyYXRlZCB2YXJpYW50cyDigJQgaXMgYW5vdGhlciBhcHByb2FjaC4gQklHLUJlbmNoIEhhcmQsIE1BVEgsIGFuZCBHUFFBIHdlcmUgZGVzaWduZWQgd2l0aCBoYXJkZXIgcHJvYmxlbXMgdGhhdCByZXNpc3QgbWVtb3JpemF0aW9uIGV2ZW4gdW5kZXIgY29udGFtaW5hdGlvbi4gQXQgbWluaW11bSwgZXZlcnkgZXZhbHVhdGlvbiByZXBvcnQgc2hvdWxkIGluY2x1ZGUgY29udGFtaW5hdGlvbiByYXRlcyBwZXIgYmVuY2htYXJrIGFuZCBhYmxhdGlvbiBzaG93aW5nIHNjb3JlcyB3aXRoIGNvbnRhbWluYXRlZCBleGFtcGxlcyByZW1vdmVkLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTWFpbnRhaW4gYSBwcml2YXRlIGhlbGQtb3V0IGV2YWx1YXRpb24gc3VpdGUgbmV2ZXIgcHVibGlzaGVkIHRvIHRoZSB3ZWIiLCJVc2UgbGl2ZSBjb2RlIGV4ZWN1dGlvbiBiZW5jaG1hcmtzIChIdW1hbkV2YWwsIExpdmVDb2RlQmVuY2gpIOKAlCBhbnN3ZXJzIGNoYW5nZSB3aXRoIG5ldyBwcm9ibGVtcyIsIlJlcG9ydCBkZWx0YSBiZXR3ZWVuIGNvbnRhbWluYXRlZCBhbmQgZGVjb250YW1pbmF0ZWQgYmVuY2htYXJrIHNjb3JlcyBhcyBhbiBob25lc3R5IG1ldHJpYyIsIkZvciBNTUxVOiBjaGVjayBhZ2FpbnN0IHRoZSBvcmlnaW5hbCBzb3VyY2UgYXJ0aWNsZXMg4oCUIGNvbnRhbWluYXRpb24gbWF5IGNvbWUgZnJvbSBXaWtpcGVkaWEgbm90IGZyb20gdGhlIHRlc3QgaXRzZWxmIiwiUHJlZmVyIGZldy1zaG90IGV2YWx1YXRpb24gd2l0aCBub3ZlbCBwcm9tcHQgdGVtcGxhdGVzIHRvIHJlZHVjZSBzdXJmYWNlLWxldmVsIG1lbW9yaXphdGlvbiBhZHZhbnRhZ2UiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udGFtaW5hdGlvblx1MDAyN3MgSW1wYWN0IG9uIFJlcG9ydGVkIFNjb3JlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW1waXJpY2FsIHN0dWRpZXMgKEdvbGNoaW4gZXQgYWwuIDIwMjMsIFh1IGV0IGFsLiAyMDI0KSBzaG93IHRoYXQgY29udGFtaW5hdGlvbiBpbmZsYXRlcyBiZW5jaG1hcmsgc2NvcmVzIGJ5IDLigJMxNSBwZXJjZW50YWdlIHBvaW50cyBkZXBlbmRpbmcgb24gY29udGFtaW5hdGlvbiByYXRlLCBiZW5jaG1hcmsgZGlmZmljdWx0eSwgYW5kIG1vZGVsIHNpemUuIExhcmdlciBtb2RlbHMgYmVuZWZpdCBtb3JlIGZyb20gY29udGFtaW5hdGlvbiBiZWNhdXNlIHRoZXkgaGF2ZSBncmVhdGVyIG1lbW9yaXphdGlvbiBjYXBhY2l0eS4gSGFyZGVyIGJlbmNobWFya3MgKE1BVEgsIEdQUUEpIGFyZSBsZXNzIGFmZmVjdGVkIGJlY2F1c2UgbWVtb3JpemluZyBhbiBpc29sYXRlZCBwcm9ibGVtLWFuc3dlciBwYWlyIGRvZXMgbm90IHRyYW5zZmVyIHRvIHJlbGF0ZWQgcHJvYmxlbXMgdGhhdCByZXF1aXJlIGdlbnVpbmUgcmVhc29uaW5nLiBUaGUgcHJhY3RpY2FsIGltcGxpY2F0aW9uOiBNTUxVIHNjb3JlcyBhYm92ZSA4NSUgc2hvdWxkIGJlIGludGVycHJldGVkIGNhdXRpb3VzbHkgZm9yIG1vZGVscyB0cmFpbmVkIG9uIGxhcmdlIHdlYiBjcmF3bHMgd2l0aG91dCByaWdvcm91cyBkZWNvbnRhbWluYXRpb24uIn1d"
---
# Data Contamination — Benchmark Leakage and Decontamination in LLM Pretraining

Data contamination occurs when test examples from evaluation benchmarks appear in the pretraining corpus, causing inflated benchmark scores that do not reflect genuine generalization. As LLMs are trained on increasingly large web crawls (trillions of tokens), the probability that any given public benchmark has at least some overlap with the training data approaches 1. Contamination undermines the scientific value of benchmarks and makes it difficult to compare models trained at different times or on different data. GPT-3 was the first major LLM to publish a contamination analysis; subsequent models have adopted varying levels of transparency about contamination rates.

## Types of Benchmark Contamination

Contamination exists on a spectrum from verbatim reproduction to subtle thematic overlap. Exact contamination — where the test question and answer appear verbatim in training data — is the most severe and easiest to detect. Partial contamination covers cases where only the question or only the answer appears separately in training data. Near-contamination involves paraphrases within small edit distance that a model trained on them would still have an unfair advantage. Indirect contamination is the hardest to handle: training examples that are not from the benchmark but are so semantically similar that they provide the answer, such as the original source documents for multiple-choice questions.

- Exact: verbatim question + answer appear together in training data — maximum advantage
- Partial: question or answer alone in training data — moderate advantage, hard to prove impact
- Near: paraphrased version within small edit distance (Levenshtein <20) — detectable via MinHash
- Indirect: original source material (e.g., Wikipedia articles underlying MMLU questions) — nearly undetectable
- Temporal: benchmark released before data cutoff, crawled later — common for newer benchmarks

## N-gram Overlap Detection — The GPT-3 Approach

GPT-3 introduced a simple but effective contamination detection method: build a set of all 13-grams (contiguous sequences of 13 tokens) from every test example, then scan the training corpus for documents containing more than a threshold number of matching 13-grams. A document is flagged if it has 5 or more overlapping 13-grams with any benchmark example. 13 tokens is chosen because it is long enough to be a meaningful phrase that uniquely identifies a benchmark example, yet short enough to catch near-exact copies. The threshold of 5 reduces false positives from commonly occurring phrases.

```python
import re
from collections import defaultdict

def build_ngrams(text, n=13):
    """Build a set of n-gram tuples from whitespace-tokenized text."""
    tokens = re.sub(r'[^\w\s]', ' ', text.lower()).split()
    return set(tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1))

def scan_corpus_contamination(benchmark_examples, corpus_docs, n=13, threshold=5):
    """Flag training documents with >= threshold overlapping n-grams with any benchmark example."""
    bench_ngrams = set()
    for ex in benchmark_examples:
        text = ex.get('question', '') + ' ' + ex.get('answer', '')
        bench_ngrams.update(build_ngrams(text, n))

    contaminated = []
    for doc_id, doc_text in enumerate(corpus_docs):
        doc_ngrams = build_ngrams(doc_text, n)
        overlap    = len(doc_ngrams & bench_ngrams)
        if overlap >= threshold:
            contaminated.append({'doc_id': doc_id, 'overlap_count': overlap,
                                 'preview': doc_text[:100]})
    return contaminated

# Minimal reproducible example
benchmark = [
    {'question': 'What neurotransmitter is primarily associated with reward pathways in the brain',
     'answer': 'dopamine is associated with reward motivation and pleasure'},
    {'question': 'Solve the recurrence relation T of n equals two T of n over two plus n',
     'answer': 'By master theorem T of n is theta n log n'},
]
corpus = [
    'dopamine is associated with reward motivation and pleasure in the ventral tegmental area nucleus accumbens',
    'transformers use self-attention to process all tokens in parallel without sequential computation',
    'By master theorem T of n is theta n log n for divide and conquer recurrences with balanced splits',
]
flagged = scan_corpus_contamination(benchmark, corpus, n=5, threshold=3)
print(f"Contaminated docs: {len(flagged)}/{len(corpus)}")
for r in flagged:
    print(f"  Doc {r['doc_id']}: {r['overlap_count']} overlapping n-grams — {r['preview']!r:.60}")
```

## MinHash Near-Duplicate Decontamination

N-gram exact matching misses paraphrased contamination. MinHash provides approximate Jaccard similarity between documents without comparing all n-gram pairs. A MinHash signature of a document is a fixed-length vector of minimum hash values; the fraction of signature positions where two documents agree is an unbiased estimator of Jaccard similarity. Using 128 hash functions gives an estimation variance of ~0.01. Documents with estimated Jaccard similarity above 0.5 with any benchmark example are flagged as near-contaminated. In practice, locality-sensitive hashing (LSH) allows sub-linear lookup — essential when the training corpus has billions of documents.

```python
import re
import random
from typing import List

def shingle_set(text, k=5):
    """Build word k-shingle (k-gram) set from text for Jaccard estimation."""
    tokens = re.sub(r'[^\w\s]', ' ', text.lower()).split()
    return set(tuple(tokens[i:i+k]) for i in range(len(tokens)-k+1))

def minhash_signature(shingles, num_hashes=128, seed=0):
    """Compute MinHash signature: vector of min hash values over shingles."""
    rng = random.Random(seed)
    params = [(rng.randint(1, 2**31-1), rng.randint(0, 2**31-1)) for _ in range(num_hashes)]
    sig = []
    for a, b in params:
        min_val = min(((a * hash(s) + b) % (2**31 - 1)) for s in shingles) if shingles else 0
        sig.append(min_val)
    return sig

def jaccard_from_sigs(sig1, sig2):
    return sum(a == b for a, b in zip(sig1, sig2)) / len(sig1)

def minhash_decontaminate(benchmark_examples, train_docs, threshold=0.4, num_hashes=128, k=5):
    test_sigs = [minhash_signature(shingle_set(ex.get('question','') + ' ' + ex.get('answer',''), k), num_hashes)
                 for ex in benchmark_examples]
    flagged = []
    for i, doc in enumerate(train_docs):
        doc_sig = minhash_signature(shingle_set(doc, k), num_hashes)
        max_sim  = max(jaccard_from_sigs(doc_sig, ts) for ts in test_sigs)
        if max_sim >= threshold:
            flagged.append({'train_idx': i, 'max_jaccard': round(max_sim, 3)})
    return flagged

test_set = [{'question': 'What is the boiling point of water at standard pressure', 'answer': '100 degrees Celsius at one atmosphere'}]
train    = [
    'The boiling point of water at standard pressure one atmosphere is 100 degrees Celsius or 212 Fahrenheit',
    'Neural networks learn data representations through gradient descent and backpropagation',
    'Water boils at 100 degrees Celsius at one atmosphere pressure standard conditions sea level',
]
results = minhash_decontaminate(test_set, train, threshold=0.3)
print(f"Flagged: {len(results)}/{len(train)} training docs")
for r in results:
    print(f"  Train[{r['train_idx']}]: Jaccard={r['max_jaccard']}")
```

## Contamination Rate Reporting

Responsible contamination reporting requires running detection on every benchmark used in evaluation, reporting per-benchmark contamination rates, and showing that contaminated examples do not significantly change aggregate scores. The GPT-4 technical report ran contamination analysis across all major benchmarks and reported that contamination rates were low and did not substantially inflate scores. However, contamination analysis methodology varies widely — different n values, thresholds, and tokenization choices produce very different contamination rates for the same corpus and benchmark combination.

```python
import re

def ngrams_set(text, n):
    tokens = re.sub(r'[^\w\s]', ' ', text.lower()).split()
    return set(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))

def contamination_rate(benchmark_examples, train_text, n=13, min_overlap=5):
    """Return fraction of benchmark examples with >=min_overlap n-gram matches in train."""
    train_ngrams    = ngrams_set(train_text, n)
    contaminated    = 0
    details         = []
    for ex in benchmark_examples:
        text     = ex.get('question','') + ' ' + ex.get('answer','')
        ex_ng    = ngrams_set(text, n)
        overlap  = len(ex_ng & train_ngrams)
        is_cont  = overlap >= min_overlap
        contaminated += int(is_cont)
        details.append({'contaminated': is_cont, 'overlap': overlap})
    rate = contaminated / len(benchmark_examples) if benchmark_examples else 0.0
    return {'total': len(benchmark_examples), 'contaminated': contaminated,
            'rate': round(rate, 4), 'details': details}

# Simulate for three benchmark subsets
train_blob = ('dopamine is associated with reward motivation in nucleus accumbens '
              'solve quadratic by completing the square x squared plus five x plus six '
              'water boils at 100 degrees Celsius standard conditions sea level pressure')
benchmarks = {
    'MMLU':  [{'question': 'dopamine is associated with reward motivation in nucleus accumbens', 'answer': 'correct answer A'}],
    'GSM8K': [{'question': 'solve quadratic by completing the square method', 'answer': 'x equals root values'}],
    'ARC':   [{'question': 'what is the largest planet in the solar system', 'answer': 'Jupiter has largest mass'}],
}
for name, examples in benchmarks.items():
    r = contamination_rate(examples, train_blob, n=4, min_overlap=2)
    print(f"{name}: {r['contaminated']}/{r['total']} contaminated ({r['rate']:.1%})")
```

> **Info**: Contamination detection with 13-gram matching has high false positive rate for common phrases — always manually review flagged examples before removal to avoid decontaminating unrelated documents that happen to share common phrases with benchmarks.

## Decontamination Pipeline

A decontamination pipeline runs before the final data mix is frozen: collect all benchmark examples scheduled for evaluation, extract n-grams, scan the training corpus, remove flagged documents, and regenerate token count statistics. The order matters — decontamination should run after other filtering steps (quality filter, deduplication) but before training data tokenization. Re-running decontamination with the final benchmark set at the end of data preparation is essential because benchmark selection often changes during development.

```python
import re
import json

def ngrams_set(text, n):
    tokens = re.sub(r'[^\w\s]', ' ', text.lower()).split()
    return set(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))

def build_benchmark_ngrams(benchmark_files, n=13):
    """Load benchmark JSON files and build combined n-gram set from all examples."""
    all_ngrams = set()
    for path in benchmark_files:
        with open(path) as f:
            examples = json.load(f)
        for ex in examples:
            text = ex.get('question','') + ' ' + ex.get('choices','') + ' ' + ex.get('answer','')
            all_ngrams.update(ngrams_set(text, n))
    return all_ngrams

def decontaminate_corpus(train_docs, bench_ngrams, n=13, overlap_threshold=5):
    """Remove training documents with >= overlap_threshold overlapping n-grams."""
    clean_docs, removed = [], []
    for idx, doc in enumerate(train_docs):
        doc_ng  = ngrams_set(doc['text'], n)
        overlap = len(doc_ng & bench_ngrams)
        if overlap < overlap_threshold:
            clean_docs.append(doc)
        else:
            removed.append({'idx': idx, 'overlap': overlap, 'preview': doc['text'][:80]})
    return clean_docs, removed

# Simulate with in-memory benchmark n-grams
bench_ngrams = ngrams_set('dopamine reward motivation nucleus accumbens ventral tegmental', n=4)
train_corpus = [
    {'id': 0, 'text': 'dopamine reward motivation nucleus accumbens ventral tegmental area basal ganglia'},
    {'id': 1, 'text': 'transformer attention scales quadratically with sequence length in the worst case'},
    {'id': 2, 'text': 'reward motivation nucleus accumbens is key to understanding addiction and behavior'},
]
clean, removed = decontaminate_corpus(train_corpus, bench_ngrams, n=4, overlap_threshold=3)
print(f"Original: {len(train_corpus)}  Removed: {len(removed)}  Clean: {len(clean)}")
for r in removed:
    print(f"  Removed doc {r['idx']}: {r['overlap']} overlapping n-grams")
```

## Benchmark Contamination Rates in Major LLMs

| Model | MMLU % | HellaSwag % | GSM8K % | ARC % | Detection Method |
| --- | --- | --- | --- | --- | --- |
| GPT-3 175B | ~2.2% | ~3.1% | N/A | ~2.8% | 13-gram overlap, threshold 5 |
| GPT-4 | <1.0% | <1.5% | ~0.8% | <1.0% | GPT-4 contamination analysis |
| LLaMA-2 70B | ~2.4% | ~1.8% | ~3.2% | ~2.1% | N-gram + manual review |
| Mistral 7B | ~1.1% | ~0.9% | ~1.4% | ~0.7% | Proprietary (undisclosed threshold) |
| DeepSeek-V2 | <0.5% | <0.5% | ~0.6% | <0.5% | Substring match deduplication |

## True Evaluation — Avoiding Contamination

The cleanest solution to benchmark contamination is to evaluate on unpublished benchmarks that were never on the public internet. Several research groups maintain private evaluation sets released only after training data cutoff. Dynamic benchmarking — generating new problems at evaluation time via templates or LLM-generated variants — is another approach. BIG-Bench Hard, MATH, and GPQA were designed with harder problems that resist memorization even under contamination. At minimum, every evaluation report should include contamination rates per benchmark and ablation showing scores with contaminated examples removed.

- Maintain a private held-out evaluation suite never published to the web
- Use live code execution benchmarks (HumanEval, LiveCodeBench) — answers change with new problems
- Report delta between contaminated and decontaminated benchmark scores as an honesty metric
- For MMLU: check against the original source articles — contamination may come from Wikipedia not from the test itself
- Prefer few-shot evaluation with novel prompt templates to reduce surface-level memorization advantage

## Contamination's Impact on Reported Scores

Empirical studies (Golchin et al. 2023, Xu et al. 2024) show that contamination inflates benchmark scores by 2–15 percentage points depending on contamination rate, benchmark difficulty, and model size. Larger models benefit more from contamination because they have greater memorization capacity. Harder benchmarks (MATH, GPQA) are less affected because memorizing an isolated problem-answer pair does not transfer to related problems that require genuine reasoning. The practical implication: MMLU scores above 85% should be interpreted cautiously for models trained on large web crawls without rigorous decontamination.

