---
title: "Causal Language Modeling — Next-Token Prediction and Autoregressive Training"
slug: "causal-language-modeling"
description: "CLM trains decoder-only transformers (GPT, LLaMA, Mistral) to predict the next token from all prior tokens using cross-entropy loss over every sequence position simultaneously, making it the foundation of modern generative language models."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2F1c2FsIExhbmd1YWdlIE1vZGVsaW5nIChDTE0pIGlzIHRoZSBwcmV0cmFpbmluZyBvYmplY3RpdmUgdW5kZXJseWluZyB0aGUgR1BUIGZhbWlseSwgTExhTUEsIE1pc3RyYWwsIGFuZCB2aXJ0dWFsbHkgZXZlcnkgbW9kZXJuIGxhcmdlIGdlbmVyYXRpdmUgbW9kZWwuIFRoZSBvYmplY3RpdmUgaXMgZGVjZXB0aXZlbHkgc2ltcGxlOiBnaXZlbiBhIHNlcXVlbmNlIG9mIHRva2VucyB44oKBLCB44oKCLCDigKYsIHjigpksIGxlYXJuIHRoZSBwcm9iYWJpbGl0eSBQKHjigpwgfCB44oKBLCDigKYsIHjigpzigovigoEpIGZvciBldmVyeSBwb3NpdGlvbiB0IHNpbXVsdGFuZW91c2x5LiBBIHNpbmdsZSBmb3J3YXJkIHBhc3MgdGhyb3VnaCB0aGUgbmV0d29yayBjb21wdXRlcyBwcmVkaWN0aW9ucyBmb3IgYWxsIE4gcG9zaXRpb25zIGF0IG9uY2Ug4oCUIGVhY2ggcG9zaXRpb24gdCBzZWVzIG9ubHkgdGhlIHRva2VucyB0byBpdHMgbGVmdCwgZW5mb3JjZWQgYnkgYSBsb3dlci10cmlhbmd1bGFyIGNhdXNhbCBhdHRlbnRpb24gbWFzay4gVGhlIGNyb3NzLWVudHJvcHkgbG9zcyBpcyBhdmVyYWdlZCBvdmVyIGFsbCBOIHBvc2l0aW9ucywgbWFraW5nIENMTSByb3VnaGx5IDYuN8OXIG1vcmUgc2FtcGxlLWVmZmljaWVudCBwZXIgZm9yd2FyZCBwYXNzIHRoYW4gTWFza2VkIExhbmd1YWdlIE1vZGVsaW5nLCB3aGljaCBvbmx5IHN1cGVydmlzZXMgfjE1JSBvZiBwb3NpdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTmV4dC1Ub2tlbiBQcmVkaWN0aW9uIE9iamVjdGl2ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRyYWluaW5nIG9iamVjdGl2ZSBpcyB0byBtaW5pbWlzZSB0aGUgbmVnYXRpdmUgbG9nLWxpa2VsaWhvb2QgYXZlcmFnZWQgb3ZlciBldmVyeSB0b2tlbiBpbiB0aGUgc2VxdWVuY2U6IEwgPSAtKDEvTikgzqPigpwgbG9nIFAoeOKCnCB8IHhcdTAwM2PigpwpLiBUaGlzIGlzIGVxdWl2YWxlbnQgdG8gbWluaW1pc2luZyBjcm9zcy1lbnRyb3B5IGJldHdlZW4gdGhlIG1vZGVsXHUwMDI3cyBwcmVkaWN0ZWQgZGlzdHJpYnV0aW9uIGFuZCB0aGUgb25lLWhvdCB0cnVlIHRva2VuIGF0IGVhY2ggcG9zaXRpb24uIFRhcmdldHMgYXJlIHNpbXBseSB0aGUgaW5wdXRzIHNoaWZ0ZWQgYnkgb25lOiBnaXZlbiBpbnB1dCBbeOKCgSwg4oCmLCB44oKZXSwgdGhlIHRhcmdldCBpcyBbeOKCgiwg4oCmLCB44oKZ4oKK4oKBXS4gVGVhY2hlciBmb3JjaW5nIG1lYW5zIHRoZSB0cnVlIGNvbnRleHQgaXMgYWx3YXlzIGZlZCBkdXJpbmcgdHJhaW5pbmcsIG5vdCB0aGUgbW9kZWxcdTAwMjdzIG93biBwcmVkaWN0aW9ucyDigJQgdGhpcyBzdGFiaWxpc2VzIHRyYWluaW5nIGJ1dCBjcmVhdGVzIGFuIGV4cG9zdXJlIGJpYXMgYXQgaW5mZXJlbmNlIHRpbWUgd2hlcmUgZXJyb3JzIGNhbiBjb21wb3VuZCBhdXRvcmVncmVzc2l2ZWx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YXNldFxuZnJvbSB0b3JjaC5ubi51dGlscy5ybm4gaW1wb3J0IHBhZF9zZXF1ZW5jZVxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEdQVDJUb2tlbml6ZXJcblxuY2xhc3MgQ0xNRGF0YXNldChEYXRhc2V0KTpcbiAgICBcIlwiXCJEYXRhc2V0IGZvciBDTE06IHRva2VuaXNlIHRleHQgYW5kIGNyZWF0ZSBzaGlmdGVkIGlucHV0L3RhcmdldCBwYWlycy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGV4dHMsIHRva2VuaXplciwgbWF4X2xlbmd0aD01MTIpOlxuICAgICAgICBzZWxmLnRva2VuaXplciA9IHRva2VuaXplclxuICAgICAgICBzZWxmLm1heF9sZW5ndGggPSBtYXhfbGVuZ3RoXG4gICAgICAgIHNlbGYuZXhhbXBsZXMgPSBbXVxuICAgICAgICBmb3IgdGV4dCBpbiB0ZXh0czpcbiAgICAgICAgICAgIGlkcyA9IHRva2VuaXplci5lbmNvZGUodGV4dCwgYWRkX3NwZWNpYWxfdG9rZW5zPVRydWUpXG4gICAgICAgICAgICBmb3IgaSBpbiByYW5nZSgwLCBsZW4oaWRzKSAtIDEsIG1heF9sZW5ndGgpOlxuICAgICAgICAgICAgICAgIGNodW5rID0gaWRzW2k6IGkgKyBtYXhfbGVuZ3RoICsgMV1cbiAgICAgICAgICAgICAgICBpZiBsZW4oY2h1bmspIFx1MDAzZT0gMjpcbiAgICAgICAgICAgICAgICAgICAgc2VsZi5leGFtcGxlcy5hcHBlbmQoY2h1bmspXG5cbiAgICBkZWYgX19sZW5fXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIGxlbihzZWxmLmV4YW1wbGVzKVxuXG4gICAgZGVmIF9fZ2V0aXRlbV9fKHNlbGYsIGlkeCk6XG4gICAgICAgIGlkcyA9IHNlbGYuZXhhbXBsZXNbaWR4XVxuICAgICAgICBpbnB1dF9pZHMgPSB0b3JjaC50ZW5zb3IoaWRzWzotMV0sIGR0eXBlPXRvcmNoLmxvbmcpICAjIFt4MSwgLi4uLCB4Tl1cbiAgICAgICAgbGFiZWxzICAgID0gdG9yY2gudGVuc29yKGlkc1sxOl0sICBkdHlwZT10b3JjaC5sb25nKSAgIyBbeDIsIC4uLiwgeE4rMV1cbiAgICAgICAgcmV0dXJuIHtcImlucHV0X2lkc1wiOiBpbnB1dF9pZHMsIFwibGFiZWxzXCI6IGxhYmVscyxcbiAgICAgICAgICAgICAgICBcImF0dGVudGlvbl9tYXNrXCI6IHRvcmNoLm9uZXNfbGlrZShpbnB1dF9pZHMpfVxuXG5kZWYgY2xtX2NvbGxhdGVfZm4oYmF0Y2gsIHBhZF90b2tlbl9pZD01MDI1Nik6XG4gICAgaW5wdXRfaWRzICA9IHBhZF9zZXF1ZW5jZShbYltcImlucHV0X2lkc1wiXSAgZm9yIGIgaW4gYmF0Y2hdLCBiYXRjaF9maXJzdD1UcnVlLCBwYWRkaW5nX3ZhbHVlPXBhZF90b2tlbl9pZClcbiAgICBsYWJlbHMgICAgID0gcGFkX3NlcXVlbmNlKFtiW1wibGFiZWxzXCJdICAgICBmb3IgYiBpbiBiYXRjaF0sIGJhdGNoX2ZpcnN0PVRydWUsIHBhZGRpbmdfdmFsdWU9LTEwMClcbiAgICBhdHRuX21hc2tzID0gcGFkX3NlcXVlbmNlKFtiW1wiYXR0ZW50aW9uX21hc2tcIl0gZm9yIGIgaW4gYmF0Y2hdLCBiYXRjaF9maXJzdD1UcnVlLCBwYWRkaW5nX3ZhbHVlPTApXG4gICAgcmV0dXJuIHtcImlucHV0X2lkc1wiOiBpbnB1dF9pZHMsIFwibGFiZWxzXCI6IGxhYmVscywgXCJhdHRlbnRpb25fbWFza1wiOiBhdHRuX21hc2tzfSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNhdXNhbCBBdHRlbnRpb24gTWFzayBhbmQgRGVjb2Rlci1Pbmx5IEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNhdXNhbCAobG93ZXItdHJpYW5ndWxhcikgYXR0ZW50aW9uIG1hc2sgaXMgd2hhdCBtYWtlcyBDTE0gcG9zc2libGUgaW4gYSBzaW5nbGUgZm9yd2FyZCBwYXNzLiBQb3NpdGlvbiB0IG1heSBvbmx5IGF0dGVuZCB0byBwb3NpdGlvbnMgMSDigKYgdC4gSW4gUHlUb3JjaCB0aGlzIGlzIHR5cGljYWxseSBpbXBsZW1lbnRlZCBhcyBhIGJvb2xlYW4gbWFzayBmaWxsZWQgaW50byB0aGUgYXR0ZW50aW9uIHNjb3JlcyBiZWZvcmUgc29mdG1heDogcG9zaXRpb25zIHRoYXQgc2hvdWxkIGJlIGJsb2NrZWQgcmVjZWl2ZSAtaW5mLCBjb2xsYXBzaW5nIHRvIHplcm8gcHJvYmFiaWxpdHkgYWZ0ZXIgc29mdG1heC4gRGVjb2Rlci1vbmx5IHRyYW5zZm9ybWVycyAoR1BULCBMTGFNQSwgTWlzdHJhbCkgc3RhY2sgTiBzdWNoIG1hc2tlZCBzZWxmLWF0dGVudGlvbiBsYXllcnMuIFRoZXJlIGlzIG5vIGVuY29kZXIg4oCUIHRoZSBtb2RlbCByZWFkcywgcmVhc29ucywgYW5kIGdlbmVyYXRlcyBhbGwgaW4gb25lIHN0YWNrLCB1c2luZyB0aGUgS1YgY2FjaGUgYXQgaW5mZXJlbmNlIHRpbWUgdG8gYXZvaWQgcmVjb21wdXRpbmcga2V5cyBhbmQgdmFsdWVzIGZvciB0aGUgYWxyZWFkeS1nZW5lcmF0ZWQgcHJlZml4LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIHdpdGggVGVhY2hlciBGb3JjaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEdXJpbmcgdHJhaW5pbmcgdGhlIG1vZGVsIGFsd2F5cyByZWNlaXZlcyB0aGUgdHJ1ZSB0b2tlbiB44oKc4oKL4oKBIGFzIGlucHV0IHRvIHByZWRpY3QgeOKCnCwgcmVnYXJkbGVzcyBvZiB3aGV0aGVyIGl0IHdvdWxkIGhhdmUgcHJlZGljdGVkIHNvbWV0aGluZyBkaWZmZXJlbnQuIFRoaXMgaXMgY2FsbGVkIHRlYWNoZXIgZm9yY2luZy4gSXQga2VlcHMgdHJhaW5pbmcgc3RhYmxlIGFuZCBmYXN0IOKAlCB0aGUgbG9zcyBncmFkaWVudHMgZmxvdyB0aHJvdWdoIGV2ZXJ5IHBvc2l0aW9uIGluIGV2ZXJ5IGJhdGNoLiBUaGUgZG93bnNpZGUgaXMgZXhwb3N1cmUgYmlhczogYXQgaW5mZXJlbmNlIHRpbWUgdGhlIG1vZGVsIGF1dG9yZWdyZXNzaXZlbHkgZmVlZHMgaXRzIG93biBwcmVkaWN0aW9ucyBiYWNrIGFzIGlucHV0LCBzbyBhIHNpbmdsZSBlcnJvciBlYXJseSBpbiBnZW5lcmF0aW9uIGNhbiBjb3JydXB0IHRoZSByZXN0IG9mIHRoZSBzZXF1ZW5jZS4gU2NoZWR1bGVkIHNhbXBsaW5nIGFuZCBSTEhGIGZpbmUtdHVuaW5nIHBhcnRpYWxseSBhZGRyZXNzIHRoaXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgR1BUMkxNSGVhZE1vZGVsLCBHUFQyQ29uZmlnXG5cbmRlZiB0cmFpbl9jbG1fZXBvY2gobW9kZWwsIGRhdGFsb2FkZXIsIG9wdGltaXplciwgc2NoZWR1bGVyLCBkZXZpY2UsIGdyYWRfY2xpcD0xLjApOlxuICAgIFwiXCJcIk9uZSBlcG9jaCBvZiBDTE0gdHJhaW5pbmcgd2l0aCB0ZWFjaGVyIGZvcmNpbmcgYW5kIGNhdXNhbCBtYXNrLlwiXCJcIlxuICAgIG1vZGVsLnRyYWluKClcbiAgICB0b3RhbF9sb3NzLCB0b3RhbF90b2tlbnMgPSAwLjAsIDBcbiAgICBmb3IgYmF0Y2ggaW4gZGF0YWxvYWRlcjpcbiAgICAgICAgaW5wdXRfaWRzID0gYmF0Y2hbXCJpbnB1dF9pZHNcIl0udG8oZGV2aWNlKVxuICAgICAgICBsYWJlbHMgICAgPSBiYXRjaFtcImxhYmVsc1wiXS50byhkZXZpY2UpXG4gICAgICAgIGF0dG5fbWFzayA9IGJhdGNoW1wiYXR0ZW50aW9uX21hc2tcIl0udG8oZGV2aWNlKVxuICAgICAgICAjIEdQVDIgYXBwbGllcyBjYXVzYWwgbWFzayBpbnRlcm5hbGx5OyBsYWJlbHM9LTEwMCBwb3NpdGlvbnMgYXJlIGlnbm9yZWRcbiAgICAgICAgb3V0cHV0cyAgID0gbW9kZWwoaW5wdXRfaWRzPWlucHV0X2lkcywgYXR0ZW50aW9uX21hc2s9YXR0bl9tYXNrLCBsYWJlbHM9bGFiZWxzKVxuICAgICAgICBsb3NzICAgICAgPSBvdXRwdXRzLmxvc3NcbiAgICAgICAgbnVtX3Rva3MgID0gKGxhYmVscyAhPSAtMTAwKS5zdW0oKS5pdGVtKClcbiAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICB0b3JjaC5ubi51dGlscy5jbGlwX2dyYWRfbm9ybV8obW9kZWwucGFyYW1ldGVycygpLCBncmFkX2NsaXApXG4gICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgc2NoZWR1bGVyLnN0ZXAoKVxuICAgICAgICB0b3RhbF9sb3NzICAgKz0gbG9zcy5pdGVtKCkgKiBudW1fdG9rc1xuICAgICAgICB0b3RhbF90b2tlbnMgKz0gbnVtX3Rva3NcbiAgICByZXR1cm4gdG90YWxfbG9zcyAvIG1heCh0b3RhbF90b2tlbnMsIDEpXG5cbmNvbmZpZyA9IEdQVDJDb25maWcodm9jYWJfc2l6ZT01MDI1Nywgbl9sYXllcj0xMiwgbl9oZWFkPTEyLCBuX2VtYmQ9NzY4KVxubW9kZWwgID0gR1BUMkxNSGVhZE1vZGVsKGNvbmZpZylcbnByaW50KGZcIkdQVC0yIHNtYWxsIHBhcmFtZXRlcnM6IHtzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSkgLyAxZTY6LjFmfU1cIilcbnByaW50KFwiQ0xNIHRyYWlucyBvbiBldmVyeSB0b2tlbiBwb3NpdGlvbiDigJQgTiB0YXJnZXRzIHBlciBzZXF1ZW5jZSBvZiBsZW5ndGggTi5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQZXJwbGV4aXR5IGFuZCBFdmFsdWF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQZXJwbGV4aXR5IChQUEwpIGlzIHRoZSBzdGFuZGFyZCBDTE0gZXZhbHVhdGlvbiBtZXRyaWM6IFBQTCA9IGV4cChhdmVyYWdlIE5MTCBwZXIgdG9rZW4pLiBBIHBlcnBsZXhpdHkgb2YgMjAgbWVhbnMgdGhlIG1vZGVsIGlzIGFzIHN1cnByaXNlZCBieSBlYWNoIHRva2VuIGFzIGlmIGl0IGhhZCB0byBjaG9vc2UgdW5pZm9ybWx5IGZyb20gMjAgZXF1YWxseSBsaWtlbHkgb3B0aW9ucy4gTG93ZXIgcGVycGxleGl0eSBpbmRpY2F0ZXMgYSBiZXR0ZXIgbGFuZ3VhZ2UgbW9kZWwuIEZvciBsb25nIGRvY3VtZW50cywgYSBzbGlkaW5nLXdpbmRvdyBhcHByb2FjaCBpcyB1c2VkIHRvIGF2b2lkIHRoZSBtb2RlbCBoYXZpbmcgbm8gY29udGV4dCBhdCB0aGUgYmVnaW5uaW5nOiBhIHN0cmlkZSBvZiBoYWxmIHRoZSBjb250ZXh0IGxlbmd0aCBlbnN1cmVzIGVhY2ggdG9rZW4gaXMgZXZlbnR1YWxseSBwcmVkaWN0ZWQgd2l0aCBhIGZ1bGwgcHJlY2VkaW5nIGNvbnRleHQuIEdQVC0yIGFjaGlldmVzIFBQTCDiiYggMTguMyBvbiBXaWtpVGV4dC0xMDM7IExMYU1BLTIgNzBCIGFjaGlldmVzIFBQTCDiiYggMy4zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBtYXRoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgR1BUMkxNSGVhZE1vZGVsLCBHUFQyVG9rZW5pemVyXG5cbmRlZiBjb21wdXRlX3BlcnBsZXhpdHkobW9kZWwsIHRva2VuaXplciwgdGV4dCwgZGV2aWNlLCBtYXhfbGVuZ3RoPTEwMjQpOlxuICAgIFwiXCJcIlNsaWRpbmctd2luZG93IHBlcnBsZXhpdHk6IGV4cChhdmVyYWdlIE5MTCBwZXIgdG9rZW4pLlwiXCJcIlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIGlkcyAgICA9IHRva2VuaXplci5lbmNvZGUodGV4dClcbiAgICBzdHJpZGUgPSBtYXhfbGVuZ3RoIC8vIDJcbiAgICB0b3RhbF9ubGwsIHRvdGFsX3Rva2VucyA9IDAuMCwgMFxuICAgIGZvciBiZWdpbiBpbiByYW5nZSgwLCBsZW4oaWRzKSwgc3RyaWRlKTpcbiAgICAgICAgZW5kICAgPSBtaW4oYmVnaW4gKyBtYXhfbGVuZ3RoLCBsZW4oaWRzKSlcbiAgICAgICAgY2h1bmsgPSB0b3JjaC50ZW5zb3IoaWRzW2JlZ2luOmVuZF0sIGR0eXBlPXRvcmNoLmxvbmcpLnVuc3F1ZWV6ZSgwKS50byhkZXZpY2UpXG4gICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgbG9zcyA9IG1vZGVsKGNodW5rLCBsYWJlbHM9Y2h1bmspLmxvc3MuaXRlbSgpXG4gICAgICAgIHRvdGFsX25sbCAgICArPSBsb3NzICogY2h1bmsuc2l6ZSgxKVxuICAgICAgICB0b3RhbF90b2tlbnMgKz0gY2h1bmsuc2l6ZSgxKVxuICAgICAgICBpZiBlbmQgPT0gbGVuKGlkcyk6XG4gICAgICAgICAgICBicmVha1xuICAgIHJldHVybiBtYXRoLmV4cCh0b3RhbF9ubGwgLyB0b3RhbF90b2tlbnMpXG5cbm1vZGVsICAgICA9IEdQVDJMTUhlYWRNb2RlbC5mcm9tX3ByZXRyYWluZWQoXCJncHQyXCIpXG50b2tlbml6ZXIgPSBHUFQyVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChcImdwdDJcIilcbmRldmljZSAgICA9IFwiY3VkYVwiIGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcImNwdVwiXG5tb2RlbC50byhkZXZpY2UpXG5zYW1wbGUgICAgPSBcIkxhbmd1YWdlIG1vZGVscyBhc3NpZ24gcHJvYmFiaWxpdHkgdG8gc2VxdWVuY2VzIG9mIHRva2Vucy4gXCIgKiAxMFxucHBsICAgICAgID0gY29tcHV0ZV9wZXJwbGV4aXR5KG1vZGVsLCB0b2tlbml6ZXIsIHNhbXBsZSwgZGV2aWNlKVxucHJpbnQoZlwiUGVycGxleGl0eToge3BwbDouMmZ9ICAobG93ZXIgaXMgYmV0dGVyIOKAlCBleHAoYXZnIE5MTCBwZXIgdG9rZW4pKVwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiQ0xNIFNhbXBsZSBFZmZpY2llbmN5IHZzIE1MTSIsImNvbnRlbnQiOiJDTE0gdHJhaW5zIG9uIGV2ZXJ5IHRva2VuIHBvc2l0aW9uIHNpbXVsdGFuZW91c2x5IChub3QganVzdCBtYXNrZWQgcG9zaXRpb25zIGxpa2UgTUxNKSwgbWFraW5nIGl0IH42Ljd4IG1vcmUgc2FtcGxlLWVmZmljaWVudCBwZXIgZm9yd2FyZCBwYXNzIOKAlCBvbmUgZG9jdW1lbnQgZ2VuZXJhdGVzIE4gdHJhaW5pbmcgZXhhbXBsZXMgZm9yIGEgc2VxdWVuY2Ugb2YgbGVuZ3RoIE4uIE1MTSB3aXRoIDE1JSBtYXNraW5nIHlpZWxkcyBvbmx5IDAuMTVOIHN1cGVydmlzZWQgcHJlZGljdGlvbnMgcGVyIGZvcndhcmQgcGFzcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBdXRvcmVncmVzc2l2ZSBJbmZlcmVuY2UgYW5kIEtWIENhY2hlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdCBpbmZlcmVuY2UgdGltZSwgZ2VuZXJhdGlvbiBpcyBwdXJlbHkgYXV0b3JlZ3Jlc3NpdmU6IHNhbXBsZSBvciBhcmdtYXggb25lIHRva2VuLCBhcHBlbmQgaXQgdG8gdGhlIGNvbnRleHQsIGFuZCByZXBlYXQuIEdyZWVkeSBkZWNvZGluZyBwaWNrcyB0aGUgbW9zdCBwcm9iYWJsZSB0b2tlbiBhdCBlYWNoIHN0ZXA7IHRlbXBlcmF0dXJlIHNhbXBsaW5nIHJlc2NhbGVzIGxvZ2l0cyBiZWZvcmUgc29mdG1heDsgdG9wLWsgYW5kIG51Y2xldXMgKHRvcC1wKSBzYW1wbGluZyB0cnVuY2F0ZSB0aGUgZGlzdHJpYnV0aW9uIHRvIHRoZSBtb3N0IGxpa2VseSB0b2tlbnMuIFRoZSBLViBjYWNoZSBzdG9yZXMga2V5IGFuZCB2YWx1ZSB0ZW5zb3JzIGZyb20gcHJpb3IgcG9zaXRpb25zIHNvIHRoYXQgb25seSB0aGUgbmV3IHRva2VuIG5lZWRzIHRvIGJlIHByb2Nlc3NlZCBlYWNoIHN0ZXAsIHJlZHVjaW5nIHBlci1zdGVwIGNvbXB1dGUgZnJvbSBPKE7CsikgdG8gTyhOKSBhZnRlciB0aGUgZmlyc3QgZm9yd2FyZCBwYXNzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBHUFQyTE1IZWFkTW9kZWwsIEdQVDJUb2tlbml6ZXJcblxuZGVmIGdlbmVyYXRlX2F1dG9yZWdyZXNzaXZlKG1vZGVsLCB0b2tlbml6ZXIsIHByb21wdCwgbWF4X25ld190b2tlbnM9ODAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRlbXBlcmF0dXJlPTEuMCwgdG9wX2s9NTAsIGRldmljZT1cImNwdVwiKTpcbiAgICBcIlwiXCJBdXRvcmVncmVzc2l2ZSBnZW5lcmF0aW9uIHdpdGggdG9wLWsgc2FtcGxpbmcgYW5kIHRlbXBlcmF0dXJlIHNjYWxpbmcuXCJcIlwiXG4gICAgbW9kZWwuZXZhbCgpXG4gICAgaW5wdXRfaWRzID0gdG9rZW5pemVyLmVuY29kZShwcm9tcHQsIHJldHVybl90ZW5zb3JzPVwicHRcIikudG8oZGV2aWNlKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgXyBpbiByYW5nZShtYXhfbmV3X3Rva2Vucyk6XG4gICAgICAgICAgICBvdXRwdXRzID0gbW9kZWwoaW5wdXRfaWRzKVxuICAgICAgICAgICAgbG9naXRzICA9IG91dHB1dHMubG9naXRzWzosIC0xLCA6XSAvIHRlbXBlcmF0dXJlICAjIGxhc3QgcG9zaXRpb25cbiAgICAgICAgICAgIGlmIHRvcF9rIFx1MDAzZSAwOlxuICAgICAgICAgICAgICAgIHZhbHVlcywgXyA9IHRvcmNoLnRvcGsobG9naXRzLCB0b3BfaylcbiAgICAgICAgICAgICAgICBsb2dpdHMgICAgID0gbG9naXRzLm1hc2tlZF9maWxsKGxvZ2l0cyBcdTAwM2MgdmFsdWVzWzosIC0xOl0sIGZsb2F0KFwiLWluZlwiKSlcbiAgICAgICAgICAgIHByb2JzICAgICAgPSB0b3JjaC5zb2Z0bWF4KGxvZ2l0cywgZGltPS0xKVxuICAgICAgICAgICAgbmV4dF90b2tlbiA9IHRvcmNoLm11bHRpbm9taWFsKHByb2JzLCAxKVxuICAgICAgICAgICAgaW5wdXRfaWRzICA9IHRvcmNoLmNhdChbaW5wdXRfaWRzLCBuZXh0X3Rva2VuXSwgZGltPTEpXG4gICAgICAgICAgICBpZiBuZXh0X3Rva2VuLml0ZW0oKSA9PSB0b2tlbml6ZXIuZW9zX3Rva2VuX2lkOlxuICAgICAgICAgICAgICAgIGJyZWFrXG4gICAgcHJlZml4X2xlbiA9IGxlbih0b2tlbml6ZXIuZW5jb2RlKHByb21wdCkpXG4gICAgcmV0dXJuIHRva2VuaXplci5kZWNvZGUoaW5wdXRfaWRzWzAsIHByZWZpeF9sZW46XSwgc2tpcF9zcGVjaWFsX3Rva2Vucz1UcnVlKVxuXG5tb2RlbCAgICAgPSBHUFQyTE1IZWFkTW9kZWwuZnJvbV9wcmV0cmFpbmVkKFwiZ3B0MlwiKVxudG9rZW5pemVyID0gR1BUMlRva2VuaXplci5mcm9tX3ByZXRyYWluZWQoXCJncHQyXCIpXG5vdXRwdXQgICAgPSBnZW5lcmF0ZV9hdXRvcmVncmVzc2l2ZShtb2RlbCwgdG9rZW5pemVyLCBcIkNhdXNhbCBsYW5ndWFnZSBtb2RlbHNcIiwgbWF4X25ld190b2tlbnM9NDApXG5wcmludChcIkdlbmVyYXRlZDpcIiwgb3V0cHV0KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNMTSB2cyBNTE0gdnMgUHJlZml4IExNIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdGhyZWUgbWFqb3IgcHJldHJhaW5pbmcgcGFyYWRpZ21zIGRpZmZlciBpbiBob3cgbXVjaCBjb250ZXh0IGVhY2ggcG9zaXRpb24gY2FuIGF0dGVuZCB0byBhbmQgd2hhdCBmcmFjdGlvbiBvZiBwb3NpdGlvbnMgYXJlIHN1cGVydmlzZWQuIENMTSAoZGVjb2Rlci1vbmx5KSBwcmVkaWN0cyBldmVyeSB0b2tlbiBmcm9tIGxlZnQgY29udGV4dCBvbmx5IOKAlCBtYXhpbWFsbHkgc2FtcGxlLWVmZmljaWVudCBidXQgbGltaXRlZCB0byBvbmUtZGlyZWN0aW9uYWwgYXR0ZW50aW9uLiBNTE0gKGVuY29kZXItb25seSkgdXNlcyBiaWRpcmVjdGlvbmFsIGF0dGVudGlvbiBidXQgb25seSBzdXBlcnZpc2VzIH4xNSUgb2YgdG9rZW5zIHBlciBwYXNzLiBQcmVmaXggTE0gKGVuY29kZXItZGVjb2RlcikgdXNlcyBiaWRpcmVjdGlvbmFsIGF0dGVudGlvbiBvdmVyIGEgcHJlZml4IGFuZCBjYXVzYWwgYXR0ZW50aW9uIG92ZXIgdGhlIGNvbnRpbnVhdGlvbiwgZ2l2aW5nIGEgbWlkZGxlIGdyb3VuZCBzdWl0YWJsZSBmb3IgY29uZGl0aW9uYWwgZ2VuZXJhdGlvbiB0YXNrcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwgVHlwZSIsIkRpcmVjdGlvbmFsaXR5IiwiT2JqZWN0aXZlIiwiQXJjaGl0ZWN0dXJlIiwiU2FtcGxlIEVmZmljaWVuY3kiLCJQcmltYXJ5IFVzZSJdLCJyb3dzIjpbWyJDTE0iLCJMZWZ0LXRvLXJpZ2h0IChjYXVzYWwpIiwiTmV4dC10b2tlbiBwcmVkaWN0aW9uIChhbGwgTiBwb3NpdGlvbnMpIiwiRGVjb2Rlci1vbmx5IChHUFQsIExMYU1BLCBNaXN0cmFsKSIsIkhpZ2gg4oCUIE4gdGFyZ2V0cyBwZXIgc2VxdWVuY2UiLCJUZXh0IGdlbmVyYXRpb24sIGluLWNvbnRleHQgbGVhcm5pbmciXSxbIk1MTSIsIkJpZGlyZWN0aW9uYWwgKGZ1bGwpIiwiUHJlZGljdCB+MTUlIG1hc2tlZCB0b2tlbnMiLCJFbmNvZGVyLW9ubHkgKEJFUlQsIFJvQkVSVGEpIiwiTG93IOKAlCB+MC4xNU4gdGFyZ2V0cyBwZXIgc2VxdWVuY2UiLCJDbGFzc2lmaWNhdGlvbiwgTkVSLCB1bmRlcnN0YW5kaW5nIl0sWyJQcmVmaXggTE0iLCJCaWRpciBwcmVmaXggKyBjYXVzYWwgY29udC4iLCJTcGFuIHByZWRpY3Rpb24gLyB0ZXh0LXRvLXRleHQiLCJFbmNvZGVyLWRlY29kZXIgKFQ1LCBGTEFOLVQ1KSIsIk1lZGl1bSDigJQgZGVwZW5kcyBvbiBtYXNrIHJhdGUiLCJTZXEyc2VxLCBjb25kaXRpb25hbCBnZW5lcmF0aW9uIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbi1Db250ZXh0IExlYXJuaW5nIGFuZCBNdWx0aS1UYXNrIEZvcm1hdHRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9uZSBvZiB0aGUgbW9zdCBzdXJwcmlzaW5nIHByb3BlcnRpZXMgb2YgbGFyZ2UgQ0xNcyBpcyBpbi1jb250ZXh0IGxlYXJuaW5nIChJQ0wpOiB0aGUgbW9kZWwgY2FuIHNvbHZlIG5ldyB0YXNrcyBhdCBpbmZlcmVuY2UgdGltZSBzaW1wbHkgYnkgcHJlcGVuZGluZyBhIGZldyBleGFtcGxlcyB0byB0aGUgcHJvbXB0IOKAlCBubyBncmFkaWVudCB1cGRhdGUgcmVxdWlyZWQuIElDTCBlbWVyZ2VzIG5hdHVyYWxseSBmcm9tIENMTSBwcmV0cmFpbmluZyBiZWNhdXNlIHRoZSBtb2RlbCBoYXMgbGVhcm5lZCB0byBjb250aW51ZSBhbnkgcHJlZml4IGNvaGVyZW50bHksIGluY2x1ZGluZyB0YXNrIGRlbW9uc3RyYXRpb25zLiBNdWx0aS10YXNrIGxlYXJuaW5nIGlzIGVxdWFsbHkgbmF0dXJhbDogYW55IHRhc2sgY2FuIGJlIGV4cHJlc3NlZCBhcyBhIHRleHQgc2VxdWVuY2UgKHNlbnRpbWVudCBjbGFzc2lmaWNhdGlvbiDihpIgXHUwMDI3UmV2aWV3OiAuLi4gU2VudGltZW50OiBwb3NpdGl2ZVx1MDAyNyksIGFuZCBhIENMTSB0cmFpbmVkIG9uIGEgbWl4dHVyZSBvZiBzdWNoIHRhc2tzIGdlbmVyYWxpc2VzIGFjcm9zcyBhbGwgb2YgdGhlbSB3aXRoIG5vIHRhc2stc3BlY2lmaWMgaGVhZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdQVC0xICgxMTdNLCAyMDE4KTogZmlyc3QgQ0xNIHdpdGggdHJhbnNmb3JtZXIgZGVjb2RlciwgZGVtb25zdHJhdGVkIHRyYW5zZmVyIGxlYXJuaW5nLiIsIkdQVC0yICgxLjVCLCAyMDE5KTogemVyby1zaG90IHRhc2sgcGVyZm9ybWFuY2UgdmlhIHByb21wdCBlbmdpbmVlcmluZyDigJQgdGV4dCBjb21wbGV0aW9uIGFzIHRoZSB1bml2ZXJzYWwgaW50ZXJmYWNlLiIsIkdQVC0zICgxNzVCLCAyMDIwKTogZmV3LXNob3QgaW4tY29udGV4dCBsZWFybmluZyBhdCBzY2FsZTsgdGFzayBleGFtcGxlcyBpbiB0aGUgcHJvbXB0IHJlcGxhY2UgZmluZS10dW5pbmcuIiwiTExhTUEgKDdC4oCTNjVCLCAyMDIzKTogb3Blbi13ZWlnaHRzIENMTSB0cmFpbmVkIGxvbmdlciBvbiBtb3JlIGRhdGEg4oCUIG1hdGNoZXMgR1BULTMgYXQgYSBmcmFjdGlvbiBvZiB0aGUgc2l6ZS4iLCJNaXN0cmFsIDdCICgyMDIzKTogQ0xNIHdpdGggZ3JvdXBlZC1xdWVyeSBhdHRlbnRpb24gYW5kIHNsaWRpbmctd2luZG93IGF0dGVudGlvbiDigJQgZWZmaWNpZW50IGxvbmctY29udGV4dCBnZW5lcmF0aW9uLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHUFQgRmFtaWx5IGFuZCB0aGUgUm9hZCB0byBMTGFNQSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWxsIG1vZGVscyBpbiB0aGUgR1BUIGxpbmVhZ2Ugc2hhcmUgdGhlIHNhbWUgQ0xNIG9iamVjdGl2ZSDigJQgdGhlIGRpZmZlcmVuY2VzIGFyZSBzY2FsZSwgZGF0YSBxdWFsaXR5LCB0cmFpbmluZyBkdXJhdGlvbiwgYW5kIGFyY2hpdGVjdHVyYWwgbWljcm8tY2hvaWNlcy4gTExhTUEgaW50cm9kdWNlZCBSTVNOb3JtIChpbnN0ZWFkIG9mIExheWVyTm9ybSksIHJvdGFyeSBwb3NpdGlvbmFsIGVtYmVkZGluZ3MgKFJvUEUsIGluc3RlYWQgb2YgbGVhcm5lZCBhYnNvbHV0ZSBwb3NpdGlvbnMpLCBTd2lHTFUgYWN0aXZhdGlvbnMgKGluc3RlYWQgb2YgR0VMVSksIGFuZCBwcmUtbm9ybSBvcmRlciDigJQgYWxsIGNvbnRyaWJ1dGluZyB0byB0cmFpbmluZyBzdGFiaWxpdHkgYXQgc2NhbGUuIE1pc3RyYWwgYWRkZWQgZ3JvdXBlZC1xdWVyeSBhdHRlbnRpb24gKEdRQSkgdG8gcmVkdWNlIEtWIGNhY2hlIG1lbW9yeSBhbmQgc2xpZGluZy13aW5kb3cgYXR0ZW50aW9uIGZvciBlZmZpY2llbnQgbG9uZyBjb250ZXh0cy4gRGVzcGl0ZSB0aGVzZSBjaGFuZ2VzLCB0aGUgbG9zcyBmdW5jdGlvbiBpcyBpZGVudGljYWw6IGNyb3NzLWVudHJvcHkgb3ZlciBldmVyeSB0b2tlbiBwb3NpdGlvbiwgZXZlcnkgc3RlcC4ifV0="
---
# Causal Language Modeling — Next-Token Prediction and Autoregressive Training

Causal Language Modeling (CLM) is the pretraining objective underlying the GPT family, LLaMA, Mistral, and virtually every modern large generative model. The objective is deceptively simple: given a sequence of tokens x₁, x₂, …, xₙ, learn the probability P(xₜ | x₁, …, xₜ₋₁) for every position t simultaneously. A single forward pass through the network computes predictions for all N positions at once — each position t sees only the tokens to its left, enforced by a lower-triangular causal attention mask. The cross-entropy loss is averaged over all N positions, making CLM roughly 6.7× more sample-efficient per forward pass than Masked Language Modeling, which only supervises ~15% of positions.

## Next-Token Prediction Objective

The training objective is to minimise the negative log-likelihood averaged over every token in the sequence: L = -(1/N) Σₜ log P(xₜ | x<ₜ). This is equivalent to minimising cross-entropy between the model's predicted distribution and the one-hot true token at each position. Targets are simply the inputs shifted by one: given input [x₁, …, xₙ], the target is [x₂, …, xₙ₊₁]. Teacher forcing means the true context is always fed during training, not the model's own predictions — this stabilises training but creates an exposure bias at inference time where errors can compound autoregressively.

```python
import torch
from torch.utils.data import Dataset
from torch.nn.utils.rnn import pad_sequence
from transformers import GPT2Tokenizer

class CLMDataset(Dataset):
    """Dataset for CLM: tokenise text and create shifted input/target pairs."""
    def __init__(self, texts, tokenizer, max_length=512):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.examples = []
        for text in texts:
            ids = tokenizer.encode(text, add_special_tokens=True)
            for i in range(0, len(ids) - 1, max_length):
                chunk = ids[i: i + max_length + 1]
                if len(chunk) >= 2:
                    self.examples.append(chunk)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        ids = self.examples[idx]
        input_ids = torch.tensor(ids[:-1], dtype=torch.long)  # [x1, ..., xN]
        labels    = torch.tensor(ids[1:],  dtype=torch.long)  # [x2, ..., xN+1]
        return {"input_ids": input_ids, "labels": labels,
                "attention_mask": torch.ones_like(input_ids)}

def clm_collate_fn(batch, pad_token_id=50256):
    input_ids  = pad_sequence([b["input_ids"]  for b in batch], batch_first=True, padding_value=pad_token_id)
    labels     = pad_sequence([b["labels"]     for b in batch], batch_first=True, padding_value=-100)
    attn_masks = pad_sequence([b["attention_mask"] for b in batch], batch_first=True, padding_value=0)
    return {"input_ids": input_ids, "labels": labels, "attention_mask": attn_masks}
```

## Causal Attention Mask and Decoder-Only Architecture

The causal (lower-triangular) attention mask is what makes CLM possible in a single forward pass. Position t may only attend to positions 1 … t. In PyTorch this is typically implemented as a boolean mask filled into the attention scores before softmax: positions that should be blocked receive -inf, collapsing to zero probability after softmax. Decoder-only transformers (GPT, LLaMA, Mistral) stack N such masked self-attention layers. There is no encoder — the model reads, reasons, and generates all in one stack, using the KV cache at inference time to avoid recomputing keys and values for the already-generated prefix.

## Training with Teacher Forcing

During training the model always receives the true token xₜ₋₁ as input to predict xₜ, regardless of whether it would have predicted something different. This is called teacher forcing. It keeps training stable and fast — the loss gradients flow through every position in every batch. The downside is exposure bias: at inference time the model autoregressively feeds its own predictions back as input, so a single error early in generation can corrupt the rest of the sequence. Scheduled sampling and RLHF fine-tuning partially address this.

```python
import torch
import torch.nn as nn
from transformers import GPT2LMHeadModel, GPT2Config

def train_clm_epoch(model, dataloader, optimizer, scheduler, device, grad_clip=1.0):
    """One epoch of CLM training with teacher forcing and causal mask."""
    model.train()
    total_loss, total_tokens = 0.0, 0
    for batch in dataloader:
        input_ids = batch["input_ids"].to(device)
        labels    = batch["labels"].to(device)
        attn_mask = batch["attention_mask"].to(device)
        # GPT2 applies causal mask internally; labels=-100 positions are ignored
        outputs   = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels)
        loss      = outputs.loss
        num_toks  = (labels != -100).sum().item()
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
        optimizer.step()
        scheduler.step()
        total_loss   += loss.item() * num_toks
        total_tokens += num_toks
    return total_loss / max(total_tokens, 1)

config = GPT2Config(vocab_size=50257, n_layer=12, n_head=12, n_embd=768)
model  = GPT2LMHeadModel(config)
print(f"GPT-2 small parameters: {sum(p.numel() for p in model.parameters()) / 1e6:.1f}M")
print("CLM trains on every token position — N targets per sequence of length N.")
```

## Perplexity and Evaluation

Perplexity (PPL) is the standard CLM evaluation metric: PPL = exp(average NLL per token). A perplexity of 20 means the model is as surprised by each token as if it had to choose uniformly from 20 equally likely options. Lower perplexity indicates a better language model. For long documents, a sliding-window approach is used to avoid the model having no context at the beginning: a stride of half the context length ensures each token is eventually predicted with a full preceding context. GPT-2 achieves PPL ≈ 18.3 on WikiText-103; LLaMA-2 70B achieves PPL ≈ 3.3.

```python
import torch
import math
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def compute_perplexity(model, tokenizer, text, device, max_length=1024):
    """Sliding-window perplexity: exp(average NLL per token)."""
    model.eval()
    ids    = tokenizer.encode(text)
    stride = max_length // 2
    total_nll, total_tokens = 0.0, 0
    for begin in range(0, len(ids), stride):
        end   = min(begin + max_length, len(ids))
        chunk = torch.tensor(ids[begin:end], dtype=torch.long).unsqueeze(0).to(device)
        with torch.no_grad():
            loss = model(chunk, labels=chunk).loss.item()
        total_nll    += loss * chunk.size(1)
        total_tokens += chunk.size(1)
        if end == len(ids):
            break
    return math.exp(total_nll / total_tokens)

model     = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
device    = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
sample    = "Language models assign probability to sequences of tokens. " * 10
ppl       = compute_perplexity(model, tokenizer, sample, device)
print(f"Perplexity: {ppl:.2f}  (lower is better — exp(avg NLL per token))")
```

> **CLM Sample Efficiency vs MLM**: CLM trains on every token position simultaneously (not just masked positions like MLM), making it ~6.7x more sample-efficient per forward pass — one document generates N training examples for a sequence of length N. MLM with 15% masking yields only 0.15N supervised predictions per forward pass.

## Autoregressive Inference and KV Cache

At inference time, generation is purely autoregressive: sample or argmax one token, append it to the context, and repeat. Greedy decoding picks the most probable token at each step; temperature sampling rescales logits before softmax; top-k and nucleus (top-p) sampling truncate the distribution to the most likely tokens. The KV cache stores key and value tensors from prior positions so that only the new token needs to be processed each step, reducing per-step compute from O(N²) to O(N) after the first forward pass.

```python
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_autoregressive(model, tokenizer, prompt, max_new_tokens=80,
                             temperature=1.0, top_k=50, device="cpu"):
    """Autoregressive generation with top-k sampling and temperature scaling."""
    model.eval()
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        for _ in range(max_new_tokens):
            outputs = model(input_ids)
            logits  = outputs.logits[:, -1, :] / temperature  # last position
            if top_k > 0:
                values, _ = torch.topk(logits, top_k)
                logits     = logits.masked_fill(logits < values[:, -1:], float("-inf"))
            probs      = torch.softmax(logits, dim=-1)
            next_token = torch.multinomial(probs, 1)
            input_ids  = torch.cat([input_ids, next_token], dim=1)
            if next_token.item() == tokenizer.eos_token_id:
                break
    prefix_len = len(tokenizer.encode(prompt))
    return tokenizer.decode(input_ids[0, prefix_len:], skip_special_tokens=True)

model     = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
output    = generate_autoregressive(model, tokenizer, "Causal language models", max_new_tokens=40)
print("Generated:", output)
```

## CLM vs MLM vs Prefix LM

The three major pretraining paradigms differ in how much context each position can attend to and what fraction of positions are supervised. CLM (decoder-only) predicts every token from left context only — maximally sample-efficient but limited to one-directional attention. MLM (encoder-only) uses bidirectional attention but only supervises ~15% of tokens per pass. Prefix LM (encoder-decoder) uses bidirectional attention over a prefix and causal attention over the continuation, giving a middle ground suitable for conditional generation tasks.

| Model Type | Directionality | Objective | Architecture | Sample Efficiency | Primary Use |
| --- | --- | --- | --- | --- | --- |
| CLM | Left-to-right (causal) | Next-token prediction (all N positions) | Decoder-only (GPT, LLaMA, Mistral) | High — N targets per sequence | Text generation, in-context learning |
| MLM | Bidirectional (full) | Predict ~15% masked tokens | Encoder-only (BERT, RoBERTa) | Low — ~0.15N targets per sequence | Classification, NER, understanding |
| Prefix LM | Bidir prefix + causal cont. | Span prediction / text-to-text | Encoder-decoder (T5, FLAN-T5) | Medium — depends on mask rate | Seq2seq, conditional generation |

## In-Context Learning and Multi-Task Formatting

One of the most surprising properties of large CLMs is in-context learning (ICL): the model can solve new tasks at inference time simply by prepending a few examples to the prompt — no gradient update required. ICL emerges naturally from CLM pretraining because the model has learned to continue any prefix coherently, including task demonstrations. Multi-task learning is equally natural: any task can be expressed as a text sequence (sentiment classification → 'Review: ... Sentiment: positive'), and a CLM trained on a mixture of such tasks generalises across all of them with no task-specific head.

- GPT-1 (117M, 2018): first CLM with transformer decoder, demonstrated transfer learning.
- GPT-2 (1.5B, 2019): zero-shot task performance via prompt engineering — text completion as the universal interface.
- GPT-3 (175B, 2020): few-shot in-context learning at scale; task examples in the prompt replace fine-tuning.
- LLaMA (7B–65B, 2023): open-weights CLM trained longer on more data — matches GPT-3 at a fraction of the size.
- Mistral 7B (2023): CLM with grouped-query attention and sliding-window attention — efficient long-context generation.

## GPT Family and the Road to LLaMA

All models in the GPT lineage share the same CLM objective — the differences are scale, data quality, training duration, and architectural micro-choices. LLaMA introduced RMSNorm (instead of LayerNorm), rotary positional embeddings (RoPE, instead of learned absolute positions), SwiGLU activations (instead of GELU), and pre-norm order — all contributing to training stability at scale. Mistral added grouped-query attention (GQA) to reduce KV cache memory and sliding-window attention for efficient long contexts. Despite these changes, the loss function is identical: cross-entropy over every token position, every step.

