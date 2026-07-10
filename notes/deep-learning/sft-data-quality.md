---
title: "SFT Data Quality — Filtering, Diversity, and Instruction Complexity"
slug: "sft-data-quality"
description: "Covers SFT data quality dimensions — correctness, instruction following, format, diversity, and complexity — plus practical techniques: AI judge scoring, IFD score filtering, instruction clustering for diversity analysis, complexity bucketing via Evol-Instruct, deduplication, and comparative analysis of Alpaca, FLAN, WizardLM, LIMA, ShareGPT, and OpenHermes datasets."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHF1YWxpdHkgb2YgU0ZUIGRhdGEgaXMgdGhlIGRvbWluYW50IGZhY3RvciBpbiBpbnN0cnVjdGlvbi1mb2xsb3dpbmcgY2FwYWJpbGl0eSwgb3V0d2VpZ2hpbmcgZGF0YXNldCBzaXplIGJ5IGEgd2lkZSBtYXJnaW4uIEZpdmUgb3J0aG9nb25hbCBxdWFsaXR5IGRpbWVuc2lvbnMgbXVzdCBhbGwgYmUgc2F0aXNmaWVkOiBjb3JyZWN0bmVzcyAodGhlIHJlc3BvbnNlIGlzIGZhY3R1YWxseSBhY2N1cmF0ZSksIGluc3RydWN0aW9uIGZvbGxvd2luZyAodGhlIHJlc3BvbnNlIGFjdHVhbGx5IGFkZHJlc3NlcyB3aGF0IHdhcyBhc2tlZCksIGZvcm1hdCBxdWFsaXR5IChhcHByb3ByaWF0ZSBsZW5ndGgsIHN0cnVjdHVyZSwgYW5kIHN0eWxlIGZvciB0aGUgdGFzayksIGRpdmVyc2l0eSAoYnJvYWQgdGFzay10eXBlIGFuZCBkb21haW4gY292ZXJhZ2UpLCBhbmQgY29tcGxleGl0eSAoYSBzcGVjdHJ1bSBmcm9tIHNpbXBsZSB0byBkaWZmaWN1bHQgaW5zdHJ1Y3Rpb25zKS4gUHJhY3RpY2FsIGRhdGEgcGlwZWxpbmVzIGNvbWJpbmUgYXV0b21hdGVkIHNjb3JpbmcsIEFJIGp1ZGdlcywgY2x1c3RlcmluZywgYW5kIGRlZHVwbGljYXRpb24gdG8gc2VsZWN0IGEgY29tcGFjdCwgaGlnaC1xdWFsaXR5IHN1YnNldCBmcm9tIGEgbGFyZ2VyIHJhdyBwb29sLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRhdGEgUXVhbGl0eSBEaW1lbnNpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJRdWFsaXR5IGlzIG11bHRpZGltZW5zaW9uYWwg4oCUIGEgcmVzcG9uc2UgY2FuIGJlIGZhY3R1YWxseSBjb3JyZWN0IGJ1dCBmYWlsIHRvIGZvbGxvdyB0aGUgaW5zdHJ1Y3Rpb24gKGFuc3dlcmluZyBhIGRpZmZlcmVudCBxdWVzdGlvbiksIG9yIGZvbGxvdyBpbnN0cnVjdGlvbnMgcHJlY2lzZWx5IGJ1dCBwcm9kdWNlIGFuIGlsbC1mb3JtYXR0ZWQgd2FsbCBvZiB0ZXh0LiBFYWNoIGRpbWVuc2lvbiBtdXN0IGJlIGFzc2Vzc2VkIHNlcGFyYXRlbHkuIEh1bWFuIExpa2VydC1zY2FsZSBhbm5vdGF0aW9uICgx4oCTNSkgb24gaGVscGZ1bG5lc3MsIGFjY3VyYWN5LCBhbmQgZm9ybWF0IGlzIHRoZSBnb2xkIHN0YW5kYXJkIGJ1dCBleHBlbnNpdmUuIEFJIGp1ZGdlcyAoR1BULTQgb3IgYSBjYWxpYnJhdGVkIG9wZW4tc291cmNlIGp1ZGdlIG1vZGVsKSBjYW4gcHJveHkgaHVtYW4gcmF0aW5ncyBhdCBzY2FsZSB3aXRoIH44MOKAkzg1JSBTcGVhcm1hbiBjb3JyZWxhdGlvbiB0byBodW1hbiBsYWJlbHMuIEF1dG9tYXRlZCBtZXRyaWNzIGxpa2UgUk9VR0UsIEJMRVVSVCwgb3IgQkVSVFNjb3JlIGFyZSB1c2VmdWwgb25seSB3aGVuIGEgcmVmZXJlbmNlIGFuc3dlciBleGlzdHMgKGNsb3NlZCB0YXNrcyksIGFuZCBmYWlsIG9uIG9wZW4tZW5kZWQgZ2VuZXJhdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNvcnJlY3RuZXNzOiByZXNwb25zZSBpcyBmYWN0dWFsbHkgYWNjdXJhdGUg4oCUIGNoZWNrIGFnYWluc3QgcmVmZXJlbmNlIGFuc3dlcnMsIHJldHJpZXZhbCwgb3Iga25vd2xlZGdlIGJhc2UgdmVyaWZpY2F0aW9uLiIsIkluc3RydWN0aW9uIGZvbGxvd2luZzogcmVzcG9uc2UgYWRkcmVzc2VzIHRoZSBpbnN0cnVjdGlvbiDigJQgbWlzbWF0Y2hlcyBpbmNsdWRlIHRvcGljIGRyaWZ0LCBwYXJ0aWFsIGNvbXBsZXRpb24sIGFuZCBpZ25vcmluZyBjb25zdHJhaW50cy4iLCJGb3JtYXQgcXVhbGl0eTogbGVuZ3RoIGlzIGFwcHJvcHJpYXRlIChub3QgdHJ1bmNhdGVkLCBub3QgcGFkZGVkIHdpdGggZmlsbGVyKSwgc3RydWN0dXJlIG1hdGNoZXMgdGhlIHRhc2sgKGNvZGUgYmxvY2sgZm9yIGNvZGUsIHByb3NlIGZvciBleHBsYW5hdGlvbikuIiwiRGl2ZXJzaXR5OiBkaXN0cmlidXRpb24gYWNyb3NzIHRhc2sgdHlwZXMgKFFBLCBzdW1tYXJpc2F0aW9uLCBjb2RlLCBjcmVhdGl2ZSwgcmVhc29uaW5nKSwgZG9tYWlucywgbGFuZ3VhZ2VzLCBhbmQgZGlmZmljdWx0eSBsZXZlbHMuIiwiQ29tcGxleGl0eTogZWFzeS1tZWRpdW0taGFyZCBkaXN0cmlidXRpb24g4oCUIGEgZGF0YXNldCBvZiBvbmx5IGVhc3kgZXhhbXBsZXMgcHJvZHVjZXMgYSBtb2RlbCB0aGF0IGZhaWxzIG9uIGhhcmQgcmVhbC13b3JsZCBxdWVyaWVzLiIsIkRlZHVwbGljYXRpb246IG5lYXItZHVwbGljYXRlIGluc3RydWN0aW9ucyBiaWFzIGdyYWRpZW50IHVwZGF0ZXMgYW5kIGluZmxhdGUgYXBwYXJlbnQgZGF0YXNldCBzaXplIOKAlCB1c2UgTWluSGFzaCBvciBlbWJlZGRpbmctc2ltaWxhcml0eSBkZWR1cC4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQUktQmFzZWQgUXVhbGl0eSBTY29yaW5nIHdpdGggTExNIEp1ZGdlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVc2luZyBhIHN0cm9uZyBMTE0gYXMgYSBqdWRnZSAoR1BULTQsIENsYXVkZSwgb3IgYSBmaW5lLXR1bmVkIHJld2FyZCBtb2RlbCkgdG8gc2NvcmUgaW5zdHJ1Y3Rpb24tcmVzcG9uc2UgcGFpcnMgaXMgdGhlIG1vc3Qgc2NhbGFibGUgcXVhbGl0eSBzaWduYWwgZm9yIG9wZW4tZW5kZWQgZ2VuZXJhdGlvbi4gVGhlIGp1ZGdlIHJlY2VpdmVzIHRoZSBpbnN0cnVjdGlvbiwgdGhlIHJlc3BvbnNlLCBhbmQgYW4gZXZhbHVhdGlvbiBydWJyaWMsIHRoZW4gcmV0dXJucyBzdHJ1Y3R1cmVkIHNjb3Jlcy4gS2V5IGNvbnNpZGVyYXRpb25zOiB1c2UgYSBjb25zaXN0ZW50IHByb21wdCB0ZW1wbGF0ZSB0byBtaW5pbWlzZSBwb3NpdGlvbmFsIGJpYXMsIGNhbGlicmF0ZSB0aGUganVkZ2UgYWdhaW5zdCBodW1hbiBhbm5vdGF0aW9ucyBvbiBhIGhlbGQtb3V0IHNldCwgYW5kIHVzZSB0ZW1wZXJhdHVyZT0wIGZvciByZXByb2R1Y2liaWxpdHkuIEp1ZGdlIGFncmVlbWVudCB3aXRoIGh1bWFucyBpcyB0eXBpY2FsbHkgfjgw4oCTODUlIOKAlCBzdWZmaWNpZW50IGZvciBidWxrIGZpbHRlcmluZyBidXQgbm90IGZvciBmaW5lLWdyYWluZWQgcmFua2luZy4gUnVubmluZyB0aGUganVkZ2UgaW4gYmF0Y2ggd2l0aCBKU09OIG91dHB1dCBhbmQgc2NoZW1hIHZhbGlkYXRpb24gYXZvaWRzIHBhcnNpbmcgZXJyb3JzIGF0IHNjYWxlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQganNvblxuZnJvbSBvcGVuYWkgaW1wb3J0IE9wZW5BSVxuXG5jbGllbnQgPSBPcGVuQUkoKVxuXG5KVURHRV9QUk9NUFQgPSBcIlwiXCJFdmFsdWF0ZSB0aGlzIGluc3RydWN0aW9uLXJlc3BvbnNlIHBhaXIuIFJldHVybiBKU09OIG9ubHkuXG5cbkluc3RydWN0aW9uOiB7aW5zdHJ1Y3Rpb259XG5SZXNwb25zZToge3Jlc3BvbnNlfVxuXG5TY29yZSBlYWNoIGRpbWVuc2lvbiAxLTUgKDU9YmVzdCk6XG4tIGhlbHBmdWxuZXNzOiBEb2VzIHRoZSByZXNwb25zZSBmdWxseSBhZGRyZXNzIHRoZSBpbnN0cnVjdGlvbj9cbi0gYWNjdXJhY3k6IElzIHRoZSByZXNwb25zZSBmYWN0dWFsbHkgY29ycmVjdD9cbi0gZm9ybWF0OiBJcyB0aGUgcmVzcG9uc2UgYXBwcm9wcmlhdGVseSBzdHJ1Y3R1cmVkIGFuZCBzaXplZD9cbi0gb3ZlcmFsbDogV2VpZ2h0ZWQgYXZlcmFnZSAoaGVscGZ1bG5lc3MgMC40LCBhY2N1cmFjeSAwLjQsIGZvcm1hdCAwLjIpXG5cblJldHVybjoge3tcImhlbHBmdWxuZXNzXCI6IGludCwgXCJhY2N1cmFjeVwiOiBpbnQsIFwiZm9ybWF0XCI6IGludCwgXCJvdmVyYWxsXCI6IGZsb2F0LCBcInJlYXNvblwiOiBzdHJ9fVwiXCJcIlxuXG5kZWYgc2NvcmVfcGFpcihpbnN0cnVjdGlvbiwgcmVzcG9uc2UsIGp1ZGdlX21vZGVsPVwiZ3B0LTRvLW1pbmlcIik6XG4gICAgcHJvbXB0ID0gSlVER0VfUFJPTVBULmZvcm1hdChpbnN0cnVjdGlvbj1pbnN0cnVjdGlvbiwgcmVzcG9uc2U9cmVzcG9uc2UpXG4gICAgcmVzdWx0ID0gY2xpZW50LmNoYXQuY29tcGxldGlvbnMuY3JlYXRlKFxuICAgICAgICBtb2RlbD1qdWRnZV9tb2RlbCxcbiAgICAgICAgbWVzc2FnZXM9W3tcInJvbGVcIjogXCJ1c2VyXCIsIFwiY29udGVudFwiOiBwcm9tcHR9XSxcbiAgICAgICAgcmVzcG9uc2VfZm9ybWF0PXtcInR5cGVcIjogXCJqc29uX29iamVjdFwifSxcbiAgICAgICAgdGVtcGVyYXR1cmU9MCxcbiAgICApXG4gICAgcmV0dXJuIGpzb24ubG9hZHMocmVzdWx0LmNob2ljZXNbMF0ubWVzc2FnZS5jb250ZW50KVxuXG5kZWYgZmlsdGVyX2J5X3F1YWxpdHkocGFpcnMsIG1pbl9vdmVyYWxsPTMuNSwganVkZ2VfbW9kZWw9XCJncHQtNG8tbWluaVwiKTpcbiAgICBcIlwiXCJGaWx0ZXIgaW5zdHJ1Y3Rpb24tcmVzcG9uc2UgcGFpcnM7IHJldGFpbiB0aG9zZSBzY29yaW5nIFx1MDAzZT0gbWluX292ZXJhbGwuXCJcIlwiXG4gICAga2VwdCA9IFtdXG4gICAgZm9yIHBhaXIgaW4gcGFpcnM6XG4gICAgICAgIHNjb3JlcyA9IHNjb3JlX3BhaXIocGFpcltcImluc3RydWN0aW9uXCJdLCBwYWlyW1wicmVzcG9uc2VcIl0sIGp1ZGdlX21vZGVsKVxuICAgICAgICBpZiBzY29yZXNbXCJvdmVyYWxsXCJdIFx1MDAzZT0gbWluX292ZXJhbGw6XG4gICAgICAgICAgICBrZXB0LmFwcGVuZCh7KipwYWlyLCBcInF1YWxpdHlfc2NvcmVzXCI6IHNjb3Jlc30pXG4gICAgcHJpbnQoZlwiUmV0YWluZWQge2xlbihrZXB0KX0ve2xlbihwYWlycyl9IHBhaXJzICh0aHJlc2hvbGQ9e21pbl9vdmVyYWxsfSlcIilcbiAgICByZXR1cm4ga2VwdCJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikluc3RydWN0aW9uIEZvbGxvd2luZyBEaWZmaWN1bHR5IChJRkQpIFNjb3JlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgSUZEIHNjb3JlIG1lYXN1cmVzIGhvdyBtdWNoIGEgZ2l2ZW4gaW5zdHJ1Y3Rpb24gY29uc3RyYWlucyB0aGUgcmVzcG9uc2U6IElGRCA9IGxvZyBQKHJlc3BvbnNlIHwgaW5zdHJ1Y3Rpb24pIOKIkiBsb2cgUChyZXNwb25zZSkuIEEgaGlnaCBJRkQgbWVhbnMgdGhlIGluc3RydWN0aW9uIGlzIGluZm9ybWF0aXZlIOKAlCB0aGUgbW9kZWxcdTAwMjdzIHByb2JhYmlsaXR5IG9mIGdlbmVyYXRpbmcgdGhlIHJlc3BvbnNlIGluY3JlYXNlcyBzdWJzdGFudGlhbGx5IHdoZW4gaXQgc2VlcyB0aGUgaW5zdHJ1Y3Rpb24uIExvdy1JRkQgZXhhbXBsZXMgaGF2ZSBnZW5lcmljIHJlc3BvbnNlcyB0aGF0IGNvdWxkIGZvbGxvdyBhbG1vc3QgYW55IGluc3RydWN0aW9uIChlLmcuLCBcdTAwMjdTdXJlLCBJIGNhbiBoZWxwIHdpdGggdGhhdC5cdTAwMjcpIGFuZCBjb250cmlidXRlIGxpdHRsZSBncmFkaWVudCBzaWduYWwuIEZpbHRlcmluZyBmb3IgaGlnaC1JRkQgc2VsZWN0cyBleGFtcGxlcyB3aGVyZSB0aGUgaW5zdHJ1Y3Rpb24gbWVhbmluZ2Z1bGx5IGNvbnN0cmFpbnMgdGhlIGNvbXBsZXRpb24sIGltcHJvdmluZyB0cmFpbmluZyBlZmZpY2llbmN5LiBUaGUgc2NvcmUgcmVxdWlyZXMgZm9yd2FyZCBwYXNzZXMgdGhyb3VnaCBhIHJlZmVyZW5jZSBMTE0gKG9mdGVuIHRoZSBzYW1lIGJhc2UgbW9kZWwgYmVpbmcgZmluZS10dW5lZCkgdG8gY29tcHV0ZSBjb25kaXRpb25hbCBhbmQgdW5jb25kaXRpb25hbCBsb2ctcHJvYmFiaWxpdGllcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvVG9rZW5pemVyLCBBdXRvTW9kZWxGb3JDYXVzYWxMTVxuXG5kZWYgY29tcHV0ZV9pZmQobW9kZWwsIHRva2VuaXplciwgaW5zdHJ1Y3Rpb24sIHJlc3BvbnNlLCBkZXZpY2U9XCJjdWRhXCIpOlxuICAgIFwiXCJcIklGRCA9IGxvZyBQKHJlc3BvbnNlfGluc3RydWN0aW9uKSAtIGxvZyBQKHJlc3BvbnNlIGFsb25lKS4gSGlnaGVyID0gbW9yZSBjb25zdHJhaW5lZC5cIlwiXCJcbiAgICBtb2RlbC5ldmFsKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgIyBDb25kaXRpb25hbDogUChyZXNwb25zZSB8IGluc3RydWN0aW9uKVxuICAgICAgICBmdWxsX3RleHQgPSBpbnN0cnVjdGlvbiArIHJlc3BvbnNlXG4gICAgICAgIGZ1bGxfaWRzICA9IHRva2VuaXplcihmdWxsX3RleHQsIHJldHVybl90ZW5zb3JzPVwicHRcIikuaW5wdXRfaWRzLnRvKGRldmljZSlcbiAgICAgICAgaW5zdHJfaWRzID0gdG9rZW5pemVyKGluc3RydWN0aW9uLCByZXR1cm5fdGVuc29ycz1cInB0XCIpLmlucHV0X2lkcy50byhkZXZpY2UpXG4gICAgICAgIHJlc3Bfc3RhcnQgPSBpbnN0cl9pZHMuc2hhcGVbMV1cbiAgICAgICAgbGFiZWxzX2NvbmQgPSBmdWxsX2lkcy5jbG9uZSgpXG4gICAgICAgIGxhYmVsc19jb25kWzosIDpyZXNwX3N0YXJ0XSA9IC0xMDAgICMgbWFzayBpbnN0cnVjdGlvblxuICAgICAgICBsb3NzX2NvbmQgPSBtb2RlbChmdWxsX2lkcywgbGFiZWxzPWxhYmVsc19jb25kKS5sb3NzLml0ZW0oKVxuICAgICAgICAjIFVuY29uZGl0aW9uYWw6IFAocmVzcG9uc2UpXG4gICAgICAgIHJlc3BfaWRzID0gdG9rZW5pemVyKHJlc3BvbnNlLCByZXR1cm5fdGVuc29ycz1cInB0XCIpLmlucHV0X2lkcy50byhkZXZpY2UpXG4gICAgICAgIGxvc3NfdW5jb25kID0gbW9kZWwocmVzcF9pZHMsIGxhYmVscz1yZXNwX2lkcykubG9zcy5pdGVtKClcbiAgICBpZmQgPSBsb3NzX3VuY29uZCAtIGxvc3NfY29uZCAgIyBwb3NpdGl2ZSA9IGluc3RydWN0aW9uIGhlbHBzIHByZWRpY3QgcmVzcG9uc2VcbiAgICByZXR1cm4gcm91bmQoaWZkLCA0KVxuXG5kZWYgZmlsdGVyX2J5X2lmZChtb2RlbCwgdG9rZW5pemVyLCBkYXRhc2V0LCBtaW5faWZkPTAuMSwgZGV2aWNlPVwiY3VkYVwiKTpcbiAgICBcIlwiXCJLZWVwIGV4YW1wbGVzIHdoZXJlIGluc3RydWN0aW9uIG1lYW5pbmdmdWxseSBjb25zdHJhaW5zIHRoZSByZXNwb25zZS5cIlwiXCJcbiAgICBzY29yZWQgPSBbXVxuICAgIGZvciBleCBpbiBkYXRhc2V0OlxuICAgICAgICBzY29yZSA9IGNvbXB1dGVfaWZkKG1vZGVsLCB0b2tlbml6ZXIsIGV4W1wiaW5zdHJ1Y3Rpb25cIl0sIGV4W1wicmVzcG9uc2VcIl0sIGRldmljZSlcbiAgICAgICAgaWYgc2NvcmUgXHUwMDNlPSBtaW5faWZkOlxuICAgICAgICAgICAgc2NvcmVkLmFwcGVuZCh7KipleCwgXCJpZmRcIjogc2NvcmV9KVxuICAgIHJldHVybiBzb3J0ZWQoc2NvcmVkLCBrZXk9bGFtYmRhIHg6IHhbXCJpZmRcIl0sIHJldmVyc2U9VHJ1ZSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnN0cnVjdGlvbiBEaXZlcnNpdHkgQW5hbHlzaXMgdmlhIENsdXN0ZXJpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpdmVyc2l0eSBpcyBhc3Nlc3NlZCBieSBlbWJlZGRpbmcgYWxsIGluc3RydWN0aW9ucyB3aXRoIGEgc2VudGVuY2UgZW5jb2RlciwgY2x1c3RlcmluZyBpbiBlbWJlZGRpbmcgc3BhY2UsIGFuZCBleGFtaW5pbmcgdGhlIGRpc3RyaWJ1dGlvbiBhY3Jvc3MgY2x1c3RlcnMuIEEgaGVhbHRoeSBkYXRhc2V0IGhhcyBldmVuIGNsdXN0ZXIgc2l6ZXMgYW5kIGhpZ2ggZW50cm9weSBvdmVyIHRoZSBjbHVzdGVyIGRpc3RyaWJ1dGlvbi4gU2tld2VkIGRpc3RyaWJ1dGlvbnMgKGEgZmV3IGRvbWluYW50IGNsdXN0ZXJzKSBpbmRpY2F0ZSB0b3BpYyBvciBmb3JtYXQgYmlhcyB0aGF0IHdpbGwgY2F1c2UgdGhlIFNGVCBtb2RlbCB0byB1bmRlcmZpdCB1bmRlcnJlcHJlc2VudGVkIHRhc2sgdHlwZXMuIEFmdGVyIGNsdXN0ZXJpbmcsIHVuZGVycmVwcmVzZW50ZWQgY2x1c3RlcnMgY2FuIGJlIHVwc2FtcGxlZCBvciB1c2VkIGFzIGEgdGFyZ2V0IGRpc3RyaWJ1dGlvbiBmb3IgZnVydGhlciBkYXRhIGNvbGxlY3Rpb24uIFRoZSBudW1iZXIgb2YgY2x1c3RlcnMgaXMgYSBoeXBlcnBhcmFtZXRlciDigJQgMjDigJM1MCBjbHVzdGVycyBpcyB0eXBpY2FsIGZvciBkYXRhc2V0cyBvZiAxMEvigJMxMDBLIGV4YW1wbGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBLTWVhbnNcbmZyb20gc2VudGVuY2VfdHJhbnNmb3JtZXJzIGltcG9ydCBTZW50ZW5jZVRyYW5zZm9ybWVyXG5cbmRlZiBhbmFseXplX2RpdmVyc2l0eShpbnN0cnVjdGlvbnMsIG5fY2x1c3RlcnM9MzAsIHNlZWQ9NDIpOlxuICAgIFwiXCJcIkNsdXN0ZXIgaW5zdHJ1Y3Rpb25zLCBjb21wdXRlIGVudHJvcHkgb3ZlciBjbHVzdGVyIGRpc3RyaWJ1dGlvbi5cIlwiXCJcbiAgICBlbmNvZGVyID0gU2VudGVuY2VUcmFuc2Zvcm1lcihcImFsbC1NaW5pTE0tTDYtdjJcIilcbiAgICBlbWJlZGRpbmdzID0gZW5jb2Rlci5lbmNvZGUoaW5zdHJ1Y3Rpb25zLCBiYXRjaF9zaXplPTY0LCBzaG93X3Byb2dyZXNzX2Jhcj1UcnVlKVxuICAgIGttZWFucyA9IEtNZWFucyhuX2NsdXN0ZXJzPW5fY2x1c3RlcnMsIHJhbmRvbV9zdGF0ZT1zZWVkLCBuX2luaXQ9MTApXG4gICAgbGFiZWxzID0ga21lYW5zLmZpdF9wcmVkaWN0KGVtYmVkZGluZ3MpXG4gICAgY291bnRzID0gbnAuYmluY291bnQobGFiZWxzKVxuICAgIHByb2JzID0gY291bnRzIC8gbGVuKGluc3RydWN0aW9ucylcbiAgICBlbnRyb3B5ID0gLW5wLnN1bShwcm9icyAqIG5wLmxvZyhwcm9icyArIDFlLTEyKSlcbiAgICBtYXhfZW50cm9weSA9IG5wLmxvZyhuX2NsdXN0ZXJzKVxuICAgIHByaW50KGZcIkRpdmVyc2l0eSBlbnRyb3B5OiB7ZW50cm9weTouM2Z9IC8ge21heF9lbnRyb3B5Oi4zZn0gKHtlbnRyb3B5L21heF9lbnRyb3B5Oi4xJX0gb2YgbWF4KVwiKVxuICAgIHByaW50KGZcIkNsdXN0ZXIgc2l6ZXMg4oCUIG1pbjoge2NvdW50cy5taW4oKX0sIG1heDoge2NvdW50cy5tYXgoKX0sIHN0ZDoge2NvdW50cy5zdGQoKTouMWZ9XCIpXG4gICAgcmV0dXJuIGxhYmVscywgZW1iZWRkaW5ncywgZW50cm9weVxuXG5kZWYgcmVzYW1wbGVfZm9yX2RpdmVyc2l0eShpbnN0cnVjdGlvbnMsIGxhYmVscywgbl9jbHVzdGVycywgdGFyZ2V0X3Blcl9jbHVzdGVyPTIwMCk6XG4gICAgXCJcIlwiVXBzYW1wbGUgdW5kZXJyZXByZXNlbnRlZCBjbHVzdGVycyB0byBlbnN1cmUgZXZlbiB0YXNrLXR5cGUgY292ZXJhZ2UuXCJcIlwiXG4gICAgZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVmYXVsdGRpY3RcbiAgICBidWNrZXRzID0gZGVmYXVsdGRpY3QobGlzdClcbiAgICBmb3IgaSwgbGJsIGluIGVudW1lcmF0ZShsYWJlbHMpOlxuICAgICAgICBidWNrZXRzW2ludChsYmwpXS5hcHBlbmQoaSlcbiAgICBzZWxlY3RlZCA9IFtdXG4gICAgZm9yIGxibCBpbiByYW5nZShuX2NsdXN0ZXJzKTpcbiAgICAgICAgaWR4cyA9IGJ1Y2tldHNbbGJsXVxuICAgICAgICBuID0gbWluKGxlbihpZHhzKSwgdGFyZ2V0X3Blcl9jbHVzdGVyKVxuICAgICAgICBzZWxlY3RlZC5leHRlbmQobnAucmFuZG9tLmNob2ljZShpZHhzLCBuLCByZXBsYWNlPUZhbHNlKS50b2xpc3QoKSlcbiAgICBwcmludChmXCJSZXNhbXBsZWQ6IHtsZW4oc2VsZWN0ZWQpfSBleGFtcGxlcyBmcm9tIHtsZW4oaW5zdHJ1Y3Rpb25zKX0gKHRhcmdldCB7dGFyZ2V0X3Blcl9jbHVzdGVyfS9jbHVzdGVyKVwiKVxuICAgIHJldHVybiBzZWxlY3RlZCJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBsZXhpdHkgU2NvcmluZyBhbmQgRXZvbC1JbnN0cnVjdCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW5zdHJ1Y3Rpb24gY29tcGxleGl0eSBjYW4gYmUgbWVhc3VyZWQgdmlhIGxleGljYWwgZmVhdHVyZXMgKGluc3RydWN0aW9uIGxlbmd0aCwgdm9jYWJ1bGFyeSByaWNobmVzcywgZGVwZW5kZW5jeSBkZXB0aCkgb3IgTExNLWJhc2VkIHNjb3JpbmcuIFdpemFyZExNXHUwMDI3cyBFdm9sLUluc3RydWN0IG1ldGhvZCBhdXRvbWF0aWNhbGx5IGV2b2x2ZXMgc2ltcGxlIGluc3RydWN0aW9ucyBpbnRvIG1vcmUgY29tcGxleCB2YXJpYW50cyB1c2luZyBhbiBMTE06IGFkZCBjb25zdHJhaW50cywgaW5jcmVhc2Ugc2NvcGUsIGFkZCByZWFzb25pbmcgc3RlcHMsIG9yIGNvbWJpbmUgbXVsdGlwbGUgdGFza3MuIFRoaXMgcHJvZHVjZXMgYSBjb21wbGV4aXR5IHNwZWN0cnVtIGZyb20gYSBzbWFsbCBzZWVkIHNldCB3aXRob3V0IG1hbnVhbCBhbm5vdGF0aW9uLiBEZWl0YSBleHRlbmRzIHRoaXMgYnkgam9pbnRseSBzY29yaW5nIGNvbXBsZXhpdHkgKGhvdyBkaWZmaWN1bHQgaXMgdGhlIGluc3RydWN0aW9uPykgYW5kIHF1YWxpdHkgKGhvdyBnb29kIGlzIHRoZSByZXNwb25zZT8pIHRvIHNlbGVjdCBhIGNvbXBhY3QsIGhpZ2gtZGl2ZXJzaXR5IHN1YnNldC4gQSBiYWxhbmNlZCBlYXN5L21lZGl1bS9oYXJkIGRpc3RyaWJ1dGlvbiAocm91Z2hseSAyNS81MC8yNSkgcHJvZHVjZXMgdGhlIGJlc3QgZ2VuZXJhbGlzYXRpb24gYWNyb3NzIHF1ZXJ5IGRpZmZpY3VsdHkgbGV2ZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgcmVcbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlclxuXG5kZWYgc2NvcmVfY29tcGxleGl0eShpbnN0cnVjdGlvbik6XG4gICAgXCJcIlwiSGV1cmlzdGljIGNvbXBsZXhpdHkgc2NvcmU6IDAuMCAodHJpdmlhbCkgdG8gMS4wIChoaWdobHkgY29tcGxleCkuXCJcIlwiXG4gICAgd29yZHMgPSBpbnN0cnVjdGlvbi5zcGxpdCgpXG4gICAgaWYgbm90IHdvcmRzOlxuICAgICAgICByZXR1cm4gMC4wXG4gICAgdW5pcXVlX3dvcmRzICAgPSBsZW4oc2V0KHcubG93ZXIoKSBmb3IgdyBpbiB3b3JkcykpXG4gICAgdm9jYWJfcmljaG5lc3MgPSB1bmlxdWVfd29yZHMgLyBsZW4od29yZHMpXG4gICAgbGVuZ3RoX3Njb3JlICAgPSBtaW4obGVuKHdvcmRzKSAvIDYwLjAsIDEuMCkgICMgc2F0dXJhdGVzIGF0IDYwIHdvcmRzXG4gICAgbnVtX2NsYXVzZXMgICAgPSBpbnN0cnVjdGlvbi5jb3VudChcdTAwMjcsXHUwMDI3KSArIGluc3RydWN0aW9uLmNvdW50KFx1MDAyNztcdTAwMjcpXG4gICAgY2xhdXNlX3Njb3JlICAgPSBtaW4obnVtX2NsYXVzZXMgLyA2LjAsIDEuMClcbiAgICBjb25zdHJhaW50X2t3cyA9IFtcIm11c3RcIiwgXCJzaG91bGRcIiwgXCJvbmx5XCIsIFwiZG8gbm90XCIsIFwid2l0aG91dFwiLCBcImdpdmVuIHRoYXRcIiwgXCJhc3N1bWluZ1wiXVxuICAgIGhhc19jb25zdHJhaW50ID0gaW50KGFueShrdyBpbiBpbnN0cnVjdGlvbi5sb3dlcigpIGZvciBrdyBpbiBjb25zdHJhaW50X2t3cykpXG4gICAgbXVsdGlzdGVwX2t3cyAgPSBbXCJmaXJzdFwiLCBcInRoZW5cIiwgXCJmaW5hbGx5XCIsIFwic3RlcFwiLCBcIm5leHRcIiwgXCJhZnRlciB0aGF0XCJdXG4gICAgaGFzX211bHRpc3RlcCAgPSBpbnQoYW55KGt3IGluIGluc3RydWN0aW9uLmxvd2VyKCkgZm9yIGt3IGluIG11bHRpc3RlcF9rd3MpKVxuICAgIHNjb3JlID0gKDAuMjUgKiBsZW5ndGhfc2NvcmUgKyAwLjIwICogdm9jYWJfcmljaG5lc3MgK1xuICAgICAgICAgICAgIDAuMjAgKiBjbGF1c2Vfc2NvcmUgKyAwLjIwICogaGFzX2NvbnN0cmFpbnQgKyAwLjE1ICogaGFzX211bHRpc3RlcClcbiAgICByZXR1cm4gcm91bmQoc2NvcmUsIDMpXG5cbmRlZiBidWNrZXRfYnlfY29tcGxleGl0eShpbnN0cnVjdGlvbnMsIHRocmVzaG9sZHM9KDAuMzMsIDAuNjcpKTpcbiAgICBzY29yZXMgPSBbKGksIHNjb3JlX2NvbXBsZXhpdHkoaW5zdCkpIGZvciBpLCBpbnN0IGluIGVudW1lcmF0ZShpbnN0cnVjdGlvbnMpXVxuICAgIGJ1Y2tldHMgPSB7XCJlYXN5XCI6IFtdLCBcIm1lZGl1bVwiOiBbXSwgXCJoYXJkXCI6IFtdfVxuICAgIGZvciBpLCBzIGluIHNjb3JlczpcbiAgICAgICAgaWYgICBzIFx1MDAzYyB0aHJlc2hvbGRzWzBdOiBidWNrZXRzW1wiZWFzeVwiXS5hcHBlbmQoaSlcbiAgICAgICAgZWxpZiBzIFx1MDAzYyB0aHJlc2hvbGRzWzFdOiBidWNrZXRzW1wibWVkaXVtXCJdLmFwcGVuZChpKVxuICAgICAgICBlbHNlOiAgICAgICAgICAgICAgICAgICBidWNrZXRzW1wiaGFyZFwiXS5hcHBlbmQoaSlcbiAgICBmb3IgaywgdiBpbiBidWNrZXRzLml0ZW1zKCk6XG4gICAgICAgIHByaW50KGZcIiAge2t9OiB7bGVuKHYpfSAoe2xlbih2KS9sZW4oaW5zdHJ1Y3Rpb25zKTouMSV9KVwiKVxuICAgIHJldHVybiBidWNrZXRzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVkdXBsaWNhdGlvbiBhbmQgRm9ybWF0IFF1YWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5lYXItZHVwbGljYXRlIGluc3RydWN0aW9ucyBiaWFzIHRoZSBncmFkaWVudCDigJQgdGhlIG1vZGVsIGVmZmVjdGl2ZWx5IHNlZXMgdGhlIHNhbWUgZXhhbXBsZSBtdWx0aXBsZSB0aW1lcyBwZXIgZXBvY2gsIGNhdXNpbmcgb3ZlcmZpdHRpbmcgb24gdGhlIGR1cGxpY2F0ZWQgdGVtcGxhdGUuIE1pbkhhc2ggTFNIIGRlZHVwbGljYXRpb24gKEphY2NhcmQgc2ltaWxhcml0eSB0aHJlc2hvbGQgfjAuODUgb24gaW5zdHJ1Y3Rpb24gbi1ncmFtcykgaXMgZWZmaWNpZW50IGF0IHNjYWxlLiBGb3JtYXQgcXVhbGl0eSBpc3N1ZXMgaW5jbHVkZTogcmVzcG9uc2VzIHRoYXQgYXJlIHRydW5jYXRlZCBtaWQtc2VudGVuY2UgKHRva2VuIGxpbWl0IGR1cmluZyBnZW5lcmF0aW9uKSwgcmVzcG9uc2VzIHRoYXQgaGFsbHVjaW5hdGUgdGhlbiBjb3JyZWN0IHRoZW1zZWx2ZXMsIGV4Y2Vzc2l2ZSBoZWRnaW5nIGxhbmd1YWdlIChcdTAwMjdBcyBhbiBBSSBsYW5ndWFnZSBtb2RlbC4uLlx1MDAyNyksIGFuZCB1bm5lY2Vzc2FyeSByZXBldGl0aW9uIG9mIHRoZSBpbnN0cnVjdGlvbi4gQXV0b21hdGVkIHJ1bGVzIChtaW5pbXVtIHJlc3BvbnNlIGxlbmd0aCwgbm8gYmxhY2tsaXN0ZWQgcGhyYXNlcywgc2VudGVuY2UgY29tcGxldGVuZXNzIGNoZWNrKSBjYW4gZmlsdGVyIHRoZXNlLiBGb3IgcmVzcG9uc2VzIGdlbmVyYXRlZCBieSBHUFQtNCwgY2hlY2tpbmcgdGhhdCB0aGUgcmVzcG9uc2UgaXMgaW4gdGhlIHNhbWUgbGFuZ3VhZ2UgYXMgdGhlIGluc3RydWN0aW9uIGNhdGNoZXMgYSBjb21tb24gZGF0YSBwaXBlbGluZSBlcnJvci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTRlQgRGF0YXNldCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRhdGFzZXQiLCJTaXplIiwiU291cmNlIiwiUXVhbGl0eSBDb250cm9sIiwiRGl2ZXJzaXR5IiwiS2V5IFN0cmVuZ3RoIl0sInJvd3MiOltbIkFscGFjYSIsIjUySyIsIkdQVC0zLjUgc2VsZi1pbnN0cnVjdCIsIk5vbmUiLCJNZWRpdW0g4oCUIHNlbGYtaW5zdHJ1Y3QgYmlhc2VkIHRvIGNvbW1vbiB0ZW1wbGF0ZXMiLCJQaW9uZWVyZWQgdGhlIHN5bnRoZXRpYyBpbnN0cnVjdGlvbiBwYXJhZGlnbSJdLFsiRkxBTiIsIjEuOE0gKG11bHRpLXRhc2spIiwiMTAwMCsgTkxQIHRhc2tzIHJlZm9ybWF0dGVkIiwiSHVtYW4tY3VyYXRlZCB0YXNrIHNlbGVjdGlvbiIsIlZlcnkgaGlnaCDigJQgMTAwMCsgdGFzayB0eXBlcyIsIkJlc3QgemVyby1zaG90IGdlbmVyYWxpc2F0aW9uIGZyb20gZGl2ZXJzaXR5Il0sWyJTaGFyZUdQVCIsIjcwSyIsIlJlYWwgQ2hhdEdQVCBjb252ZXJzYXRpb25zIiwiTm9uZSAodXNlci1zaGFyZWQpIiwiSGlnaCDigJQgcmVhbCB1c2VyIHF1ZXJ5IGRpc3RyaWJ1dGlvbiIsIk11bHRpLXR1cm4gZGlhbG9ndWUgYW5kIGZvcm1hdCByZWFsaXNtIl0sWyJXaXphcmRMTSAoRXZvbCkiLCIyNTBLIiwiRXZvbC1JbnN0cnVjdCBmcm9tIEdQVC00IiwiQXV0b21hdGljIGNvbXBsZXhpdHkgc2NvcmluZyIsIkhpZ2gg4oCUIGNvdmVycyBicmVhZHRoIGFuZCBkZXB0aCIsIlN0cm9uZyBvbiBjb21wbGV4IGFuZCBtdWx0aS1zdGVwIGluc3RydWN0aW9ucyJdLFsiTElNQSIsIjFLIiwiRXhwZXJ0LWN1cmF0ZWQgbWl4IiwiSHVtYW4gZXhwZXJ0IHJldmlldyBvZiBldmVyeSBleGFtcGxlIiwiQ2FyZWZ1bGx5IGJhbGFuY2VkIHRhc2sgdHlwZXMiLCJQcm92ZXMgMUsgcXVhbGl0eSBiZWF0cyA1Mksgbm9pc3kgZGF0YSJdLFsiT3Blbkhlcm1lcy0yLjUiLCIxTSIsIk11bHRpcGxlIG9wZW4tc291cmNlIG1peGVzIiwiQXV0b21hdGVkIGRlZHVwICsgcXVhbGl0eSBmaWx0ZXIiLCJWZXJ5IGhpZ2gg4oCUIG11bHRpbGluZ3VhbCwgbXVsdGktZG9tYWluIiwiQmVzdCBvcGVuLXNvdXJjZSBzaW5nbGUtZGF0YXNldCBmb3IgZ2VuZXJhbCBTRlQiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJRdWFsaXR5IEZpbHRlcmluZyBCZWF0cyBWb2x1bWUiLCJjb250ZW50IjoiRmlsdGVyaW5nIDUySyBBbHBhY2EgZXhhbXBsZXMgZG93biB0byA5SyBoaWdoLXF1YWxpdHkgZXhhbXBsZXMgKEFscGFnYXN1cykgcHJvZHVjZXMgYmV0dGVyIFNGVCBtb2RlbHMgdGhhbiB0cmFpbmluZyBvbiBhbGwgNTJLIOKAlCBwcmlvcml0aXNlIHF1YWxpdHkgZmlsdGVyaW5nIG92ZXIgZGF0YSB2b2x1bWUgZm9yIFNGVCwgdW5saWtlIHByZXRyYWluaW5nLiBSdW4geW91ciByYXcgZGF0YXNldCB0aHJvdWdoIGFuIEFJIGp1ZGdlIGF0IG1pbl9vdmVyYWxsPTMuNSwgdGhlbiBhcHBseSBJRkQgZmlsdGVyaW5nIGFuZCBkaXZlcnNpdHkgcmVzYW1wbGluZy4gQSAxMEsgY2FyZWZ1bGx5IGN1cmF0ZWQgc2V0IHdpbGwgb3V0cGVyZm9ybSAxMDBLIHVuZmlsdGVyZWQgZGF0YS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcHJhY3RpY2FsIFNGVCBkYXRhIHBpcGVsaW5lIGNvbWJpbmVzIGZvdXIgc3RlcHM6ICgxKSBjb2xsZWN0IGEgbGFyZ2UgcmF3IHBvb2wgZnJvbSBtdWx0aXBsZSBzb3VyY2VzIChTaGFyZUdQVCwgb3Blbi1zb3VyY2UgZGF0YXNldHMsIHN5bnRoZXRpYyBnZW5lcmF0aW9uKTsgKDIpIGRlZHVwbGljYXRlIHdpdGggTWluSGFzaDsgKDMpIHNjb3JlIHdpdGggYW4gQUkganVkZ2UgYW5kIElGRCBmaWx0ZXI7ICg0KSByZXNhbXBsZSBmb3IgZGl2ZXJzaXR5IGFuZCBjb21wbGV4aXR5IGJhbGFuY2UuIFRoZSByZXN1bHRpbmcgZmlsdGVyZWQgZGF0YXNldCBpcyB0eXBpY2FsbHkgMTDigJMyMCUgb2YgdGhlIHJhdyBwb29sIHNpemUuIFRoaXMgaW52ZXN0bWVudCBpbiBkYXRhIHF1YWxpdHkgcGF5cyBjb21wb3VuZCBkaXZpZGVuZHM6IG1vZGVscyB0cmFpbmVkIG9uIGhpZ2gtcXVhbGl0eSBTRlQgZGF0YSByZWFjaCBiZXR0ZXIgcHJlZmVyZW5jZSBsZWFybmluZyBiYXNlbGluZXMsIHJlc3BvbmQgYmV0dGVyIHRvIFJMSEYvRFBPLCBhbmQgcmVxdWlyZSBsZXNzIGNvbXB1dGUgb3ZlcmFsbC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# SFT Data Quality — Filtering, Diversity, and Instruction Complexity

The quality of SFT data is the dominant factor in instruction-following capability, outweighing dataset size by a wide margin. Five orthogonal quality dimensions must all be satisfied: correctness (the response is factually accurate), instruction following (the response actually addresses what was asked), format quality (appropriate length, structure, and style for the task), diversity (broad task-type and domain coverage), and complexity (a spectrum from simple to difficult instructions). Practical data pipelines combine automated scoring, AI judges, clustering, and deduplication to select a compact, high-quality subset from a larger raw pool.

## Data Quality Dimensions

Quality is multidimensional — a response can be factually correct but fail to follow the instruction (answering a different question), or follow instructions precisely but produce an ill-formatted wall of text. Each dimension must be assessed separately. Human Likert-scale annotation (1–5) on helpfulness, accuracy, and format is the gold standard but expensive. AI judges (GPT-4 or a calibrated open-source judge model) can proxy human ratings at scale with ~80–85% Spearman correlation to human labels. Automated metrics like ROUGE, BLEURT, or BERTScore are useful only when a reference answer exists (closed tasks), and fail on open-ended generation.

- Correctness: response is factually accurate — check against reference answers, retrieval, or knowledge base verification.
- Instruction following: response addresses the instruction — mismatches include topic drift, partial completion, and ignoring constraints.
- Format quality: length is appropriate (not truncated, not padded with filler), structure matches the task (code block for code, prose for explanation).
- Diversity: distribution across task types (QA, summarisation, code, creative, reasoning), domains, languages, and difficulty levels.
- Complexity: easy-medium-hard distribution — a dataset of only easy examples produces a model that fails on hard real-world queries.
- Deduplication: near-duplicate instructions bias gradient updates and inflate apparent dataset size — use MinHash or embedding-similarity dedup.

## AI-Based Quality Scoring with LLM Judge

Using a strong LLM as a judge (GPT-4, Claude, or a fine-tuned reward model) to score instruction-response pairs is the most scalable quality signal for open-ended generation. The judge receives the instruction, the response, and an evaluation rubric, then returns structured scores. Key considerations: use a consistent prompt template to minimise positional bias, calibrate the judge against human annotations on a held-out set, and use temperature=0 for reproducibility. Judge agreement with humans is typically ~80–85% — sufficient for bulk filtering but not for fine-grained ranking. Running the judge in batch with JSON output and schema validation avoids parsing errors at scale.

```python
import json
from openai import OpenAI

client = OpenAI()

JUDGE_PROMPT = """Evaluate this instruction-response pair. Return JSON only.

Instruction: {instruction}
Response: {response}

Score each dimension 1-5 (5=best):
- helpfulness: Does the response fully address the instruction?
- accuracy: Is the response factually correct?
- format: Is the response appropriately structured and sized?
- overall: Weighted average (helpfulness 0.4, accuracy 0.4, format 0.2)

Return: {{"helpfulness": int, "accuracy": int, "format": int, "overall": float, "reason": str}}"""

def score_pair(instruction, response, judge_model="gpt-4o-mini"):
    prompt = JUDGE_PROMPT.format(instruction=instruction, response=response)
    result = client.chat.completions.create(
        model=judge_model,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0,
    )
    return json.loads(result.choices[0].message.content)

def filter_by_quality(pairs, min_overall=3.5, judge_model="gpt-4o-mini"):
    """Filter instruction-response pairs; retain those scoring >= min_overall."""
    kept = []
    for pair in pairs:
        scores = score_pair(pair["instruction"], pair["response"], judge_model)
        if scores["overall"] >= min_overall:
            kept.append({**pair, "quality_scores": scores})
    print(f"Retained {len(kept)}/{len(pairs)} pairs (threshold={min_overall})")
    return kept
```

## Instruction Following Difficulty (IFD) Score

The IFD score measures how much a given instruction constrains the response: IFD = log P(response | instruction) − log P(response). A high IFD means the instruction is informative — the model's probability of generating the response increases substantially when it sees the instruction. Low-IFD examples have generic responses that could follow almost any instruction (e.g., 'Sure, I can help with that.') and contribute little gradient signal. Filtering for high-IFD selects examples where the instruction meaningfully constrains the completion, improving training efficiency. The score requires forward passes through a reference LLM (often the same base model being fine-tuned) to compute conditional and unconditional log-probabilities.

```python
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM

def compute_ifd(model, tokenizer, instruction, response, device="cuda"):
    """IFD = log P(response|instruction) - log P(response alone). Higher = more constrained."""
    model.eval()
    with torch.no_grad():
        # Conditional: P(response | instruction)
        full_text = instruction + response
        full_ids  = tokenizer(full_text, return_tensors="pt").input_ids.to(device)
        instr_ids = tokenizer(instruction, return_tensors="pt").input_ids.to(device)
        resp_start = instr_ids.shape[1]
        labels_cond = full_ids.clone()
        labels_cond[:, :resp_start] = -100  # mask instruction
        loss_cond = model(full_ids, labels=labels_cond).loss.item()
        # Unconditional: P(response)
        resp_ids = tokenizer(response, return_tensors="pt").input_ids.to(device)
        loss_uncond = model(resp_ids, labels=resp_ids).loss.item()
    ifd = loss_uncond - loss_cond  # positive = instruction helps predict response
    return round(ifd, 4)

def filter_by_ifd(model, tokenizer, dataset, min_ifd=0.1, device="cuda"):
    """Keep examples where instruction meaningfully constrains the response."""
    scored = []
    for ex in dataset:
        score = compute_ifd(model, tokenizer, ex["instruction"], ex["response"], device)
        if score >= min_ifd:
            scored.append({**ex, "ifd": score})
    return sorted(scored, key=lambda x: x["ifd"], reverse=True)
```

## Instruction Diversity Analysis via Clustering

Diversity is assessed by embedding all instructions with a sentence encoder, clustering in embedding space, and examining the distribution across clusters. A healthy dataset has even cluster sizes and high entropy over the cluster distribution. Skewed distributions (a few dominant clusters) indicate topic or format bias that will cause the SFT model to underfit underrepresented task types. After clustering, underrepresented clusters can be upsampled or used as a target distribution for further data collection. The number of clusters is a hyperparameter — 20–50 clusters is typical for datasets of 10K–100K examples.

```python
import numpy as np
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

def analyze_diversity(instructions, n_clusters=30, seed=42):
    """Cluster instructions, compute entropy over cluster distribution."""
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = encoder.encode(instructions, batch_size=64, show_progress_bar=True)
    kmeans = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    labels = kmeans.fit_predict(embeddings)
    counts = np.bincount(labels)
    probs = counts / len(instructions)
    entropy = -np.sum(probs * np.log(probs + 1e-12))
    max_entropy = np.log(n_clusters)
    print(f"Diversity entropy: {entropy:.3f} / {max_entropy:.3f} ({entropy/max_entropy:.1%} of max)")
    print(f"Cluster sizes — min: {counts.min()}, max: {counts.max()}, std: {counts.std():.1f}")
    return labels, embeddings, entropy

def resample_for_diversity(instructions, labels, n_clusters, target_per_cluster=200):
    """Upsample underrepresented clusters to ensure even task-type coverage."""
    from collections import defaultdict
    buckets = defaultdict(list)
    for i, lbl in enumerate(labels):
        buckets[int(lbl)].append(i)
    selected = []
    for lbl in range(n_clusters):
        idxs = buckets[lbl]
        n = min(len(idxs), target_per_cluster)
        selected.extend(np.random.choice(idxs, n, replace=False).tolist())
    print(f"Resampled: {len(selected)} examples from {len(instructions)} (target {target_per_cluster}/cluster)")
    return selected
```

## Complexity Scoring and Evol-Instruct

Instruction complexity can be measured via lexical features (instruction length, vocabulary richness, dependency depth) or LLM-based scoring. WizardLM's Evol-Instruct method automatically evolves simple instructions into more complex variants using an LLM: add constraints, increase scope, add reasoning steps, or combine multiple tasks. This produces a complexity spectrum from a small seed set without manual annotation. Deita extends this by jointly scoring complexity (how difficult is the instruction?) and quality (how good is the response?) to select a compact, high-diversity subset. A balanced easy/medium/hard distribution (roughly 25/50/25) produces the best generalisation across query difficulty levels.

```python
import re
import numpy as np
from collections import Counter

def score_complexity(instruction):
    """Heuristic complexity score: 0.0 (trivial) to 1.0 (highly complex)."""
    words = instruction.split()
    if not words:
        return 0.0
    unique_words   = len(set(w.lower() for w in words))
    vocab_richness = unique_words / len(words)
    length_score   = min(len(words) / 60.0, 1.0)  # saturates at 60 words
    num_clauses    = instruction.count(',') + instruction.count(';')
    clause_score   = min(num_clauses / 6.0, 1.0)
    constraint_kws = ["must", "should", "only", "do not", "without", "given that", "assuming"]
    has_constraint = int(any(kw in instruction.lower() for kw in constraint_kws))
    multistep_kws  = ["first", "then", "finally", "step", "next", "after that"]
    has_multistep  = int(any(kw in instruction.lower() for kw in multistep_kws))
    score = (0.25 * length_score + 0.20 * vocab_richness +
             0.20 * clause_score + 0.20 * has_constraint + 0.15 * has_multistep)
    return round(score, 3)

def bucket_by_complexity(instructions, thresholds=(0.33, 0.67)):
    scores = [(i, score_complexity(inst)) for i, inst in enumerate(instructions)]
    buckets = {"easy": [], "medium": [], "hard": []}
    for i, s in scores:
        if   s < thresholds[0]: buckets["easy"].append(i)
        elif s < thresholds[1]: buckets["medium"].append(i)
        else:                   buckets["hard"].append(i)
    for k, v in buckets.items():
        print(f"  {k}: {len(v)} ({len(v)/len(instructions):.1%})")
    return buckets
```

## Deduplication and Format Quality

Near-duplicate instructions bias the gradient — the model effectively sees the same example multiple times per epoch, causing overfitting on the duplicated template. MinHash LSH deduplication (Jaccard similarity threshold ~0.85 on instruction n-grams) is efficient at scale. Format quality issues include: responses that are truncated mid-sentence (token limit during generation), responses that hallucinate then correct themselves, excessive hedging language ('As an AI language model...'), and unnecessary repetition of the instruction. Automated rules (minimum response length, no blacklisted phrases, sentence completeness check) can filter these. For responses generated by GPT-4, checking that the response is in the same language as the instruction catches a common data pipeline error.

## SFT Dataset Comparison

| Dataset | Size | Source | Quality Control | Diversity | Key Strength |
| --- | --- | --- | --- | --- | --- |
| Alpaca | 52K | GPT-3.5 self-instruct | None | Medium — self-instruct biased to common templates | Pioneered the synthetic instruction paradigm |
| FLAN | 1.8M (multi-task) | 1000+ NLP tasks reformatted | Human-curated task selection | Very high — 1000+ task types | Best zero-shot generalisation from diversity |
| ShareGPT | 70K | Real ChatGPT conversations | None (user-shared) | High — real user query distribution | Multi-turn dialogue and format realism |
| WizardLM (Evol) | 250K | Evol-Instruct from GPT-4 | Automatic complexity scoring | High — covers breadth and depth | Strong on complex and multi-step instructions |
| LIMA | 1K | Expert-curated mix | Human expert review of every example | Carefully balanced task types | Proves 1K quality beats 52K noisy data |
| OpenHermes-2.5 | 1M | Multiple open-source mixes | Automated dedup + quality filter | Very high — multilingual, multi-domain | Best open-source single-dataset for general SFT |

> **Quality Filtering Beats Volume**: Filtering 52K Alpaca examples down to 9K high-quality examples (Alpagasus) produces better SFT models than training on all 52K — prioritise quality filtering over data volume for SFT, unlike pretraining. Run your raw dataset through an AI judge at min_overall=3.5, then apply IFD filtering and diversity resampling. A 10K carefully curated set will outperform 100K unfiltered data.

A practical SFT data pipeline combines four steps: (1) collect a large raw pool from multiple sources (ShareGPT, open-source datasets, synthetic generation); (2) deduplicate with MinHash; (3) score with an AI judge and IFD filter; (4) resample for diversity and complexity balance. The resulting filtered dataset is typically 10–20% of the raw pool size. This investment in data quality pays compound dividends: models trained on high-quality SFT data reach better preference learning baselines, respond better to RLHF/DPO, and require less compute overall.

---

