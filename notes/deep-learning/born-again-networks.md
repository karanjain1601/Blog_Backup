---
title: "Born-Again Networks — Sequential Self-Distillation"
slug: "born-again-networks"
description: "Born-again networks (Furlanello et al. 2018) distil from a teacher into a same-capacity student, yielding accuracy gains despite no compression. Covers BAN training chains, the GESD ensemble, dark knowledge, calibration, and the connection to snapshot ensembles."
tags: ["deep-learning", "model-compression", "knowledge-distillation", "pruning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQm9ybi1hZ2FpbiBuZXR3b3JrcyAoQkFOcyksIGludHJvZHVjZWQgYnkgRnVybGFuZWxsbyBldCBhbC4gKDIwMTgpLCBhcHBseSBrbm93bGVkZ2UgZGlzdGlsbGF0aW9uIGluIGFuIHVuZXhwZWN0ZWQgZGlyZWN0aW9uOiBpbnN0ZWFkIG9mIGNvbXByZXNzaW5nIGEgbGFyZ2UgdGVhY2hlciBpbnRvIGEgc21hbGxlciBzdHVkZW50LCB0aGV5IGRpc3RpbCBhIG1vZGVsIGludG8gYW4gaWRlbnRpY2FsLWNhcGFjaXR5IGNvcHkuIFRoZSByZXN1bHQgaXMgYSBzdHVkZW50IHRoYXQgY29uc2lzdGVudGx5IG91dHBlcmZvcm1zIHRoZSB0ZWFjaGVyIG9uIHRoZSBzYW1lIHRhc2sgZGVzcGl0ZSBoYXZpbmcgdGhlIHNhbWUgbnVtYmVyIG9mIHBhcmFtZXRlcnMuIFRoaXMgdmlvbGF0ZXMgdGhlIG5haXZlIGludHVpdGlvbiB0aGF0IGRpc3RpbGxhdGlvbiBvbmx5IGhlbHBzIHdoZW4gdGhlIHN0dWRlbnQgaXMgc21hbGxlciDigJQgdGhlIGJlbmVmaXQgY29tZXMgbm90IGZyb20gY29tcHJlc3Npb24gYnV0IGZyb20gdGhlIHJpY2hlciBzdXBlcnZpc2lvbiBzaWduYWwgZW5jb2RlZCBpbiB0aGUgdGVhY2hlclx1MDAyN3Mgc29mdCBwcm9iYWJpbGl0eSBvdXRwdXRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoYXQgQXJlIEJvcm4tQWdhaW4gTmV0d29ya3M/In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGJvcm4tYWdhaW4gbmV0d29yayBpcyBhIG1vZGVsIHRyYWluZWQgYnkgbWluaW1pc2luZyB0aGUgS0wgZGl2ZXJnZW5jZSBiZXR3ZWVuIGl0cyBvdXRwdXQgZGlzdHJpYnV0aW9uIGFuZCB0aGUgc29mdCBwcm9iYWJpbGl0aWVzIG9mIGEgdGVhY2hlciB3aXRoIGlkZW50aWNhbCBhcmNoaXRlY3R1cmUuIEJlY2F1c2UgdGVhY2hlciBhbmQgc3R1ZGVudCBoYXZlIHRoZSBzYW1lIGNhcGFjaXR5LCB0aGUgc3R1ZGVudCBjYW5ub3QgZXhwbG9pdCB0aGUgdGVhY2hlclx1MDAyN3Mga25vd2xlZGdlIHRocm91Z2ggY29tcHJlc3Npb24uIEluc3RlYWQsIGl0IGxlYXJucyBhIHNtb290aGVyIGRlY2lzaW9uIGJvdW5kYXJ5IHNoYXBlZCBieSBpbnRlci1jbGFzcyBzaW1pbGFyaXR5IGluZm9ybWF0aW9uIGluIHRoZSB0ZWFjaGVyXHUwMDI3cyBzb2Z0IGxhYmVscy4gVGhlIHRlYWNoZXJcdTAwMjdzIG5vbi1hcmdtYXggcHJvYmFiaWxpdGllcyDigJQgZm9yIGV4YW1wbGUsIGFzc2lnbmluZyBwcm9iYWJpbGl0eSAwLjAzIHRvIFx1MDAyN2F1dG9tb2JpbGVcdTAwMjcgd2hlbiBjbGFzc2lmeWluZyBhIFx1MDAyN3RydWNrXHUwMDI3IOKAlCBlbmNvZGUgc2VtYW50aWMgcmVsYXRpb25zaGlwcyB0aGF0IGFjdCBhcyByZWd1bGFyaXNhdGlvbiwgcmVkdWNpbmcgZWZmZWN0aXZlIGxhYmVsIG5vaXNlIG9uIGFtYmlndW91cyBleGFtcGxlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgQkFOIFRyYWluaW5nIENoYWluIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCQU5zIGFyZSBhcHBsaWVkIHNlcXVlbnRpYWxseTogR+KCgSBpcyB0aGUgYmFzZWxpbmUgbW9kZWwgdHJhaW5lZCBvbiBoYXJkIGxhYmVscy4gR+KCgiAoQkFOLTEpIGlzIHRyYWluZWQgdXNpbmcgR+KCgVx1MDAyN3Mgc29mdCB0YXJnZXRzIGF0IHRlbXBlcmF0dXJlIFQuIEfigoMgKEJBTi0yKSB1c2VzIEfigoJcdTAwMjdzIHNvZnQgdGFyZ2V0cywgYW5kIHNvIG9uLiBVbmxpa2UgdHJhZGl0aW9uYWwgS0Qgd2hlcmUgdGhlIHRlYWNoZXIgaXMgYSBmaXhlZCBsYXJnZXIgbW9kZWwsIHRoZSBCQU4gdGVhY2hlciBpbXByb3ZlcyB3aXRoIGVhY2ggZ2VuZXJhdGlvbiwgcHJvdmlkaW5nIHByb2dyZXNzaXZlbHkgcmljaGVyIHN1cGVydmlzaW9uLiBUZW1wZXJhdHVyZSBUIGNvbnRyb2xzIHNvZnRuZXNzIOKAlCBoaWdoZXIgVCBzcHJlYWRzIHByb2JhYmlsaXR5IG1hc3MgbW9yZSBldmVubHkgYWNyb3NzIGNsYXNzZXMsIHJldmVhbGluZyBtb3JlIGludGVyLWNsYXNzIHN0cnVjdHVyZS4gQSBjb21iaW5lZCBsb3NzIGJsZW5kcyBoYXJkIGxhYmVscyAoY3Jvc3MtZW50cm9weSkgYW5kIHNvZnQgdGFyZ2V0cyAoS0wgZGl2ZXJnZW5jZSksIHdlaWdodGVkIGJ5IGFscGhhLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5cbmRlZiB0cmFpbl9iYW5fZ2VuZXJhdGlvbih0ZWFjaGVyLCBzdHVkZW50LCB0cmFpbl9sb2FkZXIsIGRldmljZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICB0ZW1wZXJhdHVyZT00LjAsIGFscGhhPTAuNSwgZXBvY2hzPTEwLCBscj0xZS0zKTpcbiAgICBcIlwiXCJUcmFpbiBzdHVkZW50IGFzIGEgQkFOIG9mIHRlYWNoZXIgdXNpbmcgc29mdCB0YXJnZXQgZGlzdGlsbGF0aW9uLlwiXCJcIlxuICAgIHRlYWNoZXIuZXZhbCgpXG4gICAgc3R1ZGVudC50cmFpbigpXG4gICAgb3B0aW1pemVyID0gb3B0aW0uQWRhbShzdHVkZW50LnBhcmFtZXRlcnMoKSwgbHI9bHIpXG4gICAgY3JpdGVyaW9uID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpXG4gICAgZm9yIGVwb2NoIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIHRvdGFsX2xvc3MgPSAwLjBcbiAgICAgICAgZm9yIFgsIHkgaW4gdHJhaW5fbG9hZGVyOlxuICAgICAgICAgICAgWCwgeSA9IFgudG8oZGV2aWNlKSwgeS50byhkZXZpY2UpXG4gICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIHRlYWNoZXJfbG9naXRzID0gdGVhY2hlcihYKVxuICAgICAgICAgICAgICAgIHNvZnRfdGFyZ2V0cyA9IEYuc29mdG1heCh0ZWFjaGVyX2xvZ2l0cyAvIHRlbXBlcmF0dXJlLCBkaW09LTEpXG4gICAgICAgICAgICBzdHVkZW50X2xvZ2l0cyA9IHN0dWRlbnQoWClcbiAgICAgICAgICAgIGhhcmRfbG9zcyA9IGNyaXRlcmlvbihzdHVkZW50X2xvZ2l0cywgeSlcbiAgICAgICAgICAgIHNvZnRfbG9zcyA9IEYua2xfZGl2KFxuICAgICAgICAgICAgICAgIEYubG9nX3NvZnRtYXgoc3R1ZGVudF9sb2dpdHMgLyB0ZW1wZXJhdHVyZSwgZGltPS0xKSxcbiAgICAgICAgICAgICAgICBzb2Z0X3RhcmdldHMsIHJlZHVjdGlvbj1cdTAwMjdiYXRjaG1lYW5cdTAwMjdcbiAgICAgICAgICAgICkgKiAodGVtcGVyYXR1cmUgKiogMilcbiAgICAgICAgICAgIGxvc3MgPSAoMSAtIGFscGhhKSAqIGhhcmRfbG9zcyArIGFscGhhICogc29mdF9sb3NzXG4gICAgICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgICAgIHRvdGFsX2xvc3MgKz0gbG9zcy5pdGVtKClcbiAgICAgICAgcHJpbnQoZlx1MDAyN0Vwb2NoIHtlcG9jaCsxfS97ZXBvY2hzfTogbG9zcz17dG90YWxfbG9zcy9sZW4odHJhaW5fbG9hZGVyKTouNGZ9XHUwMDI3KVxuICAgIHJldHVybiBzdHVkZW50XG5cbiMgQkFOIGNoYWluOiBHMSAoYmFzZWxpbmUpIC1cdTAwM2UgRzIgKEJBTi0xKSAtXHUwMDNlIEczIChCQU4tMilcbnByaW50KFx1MDAyN0JBTiBjaGFpbjogRzEgLVx1MDAzZSBHMiB2aWEgRzEgc29mdCB0YXJnZXRzLCBHMiAtXHUwMDNlIEczIHZpYSBHMiBzb2Z0IHRhcmdldHNcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR0VTRCDigJQgR2VuZXJhdGluZyBFbnNlbWJsZSBieSBTZXF1ZW50aWFsIERpc3RpbGxhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWZ0ZXIgdHJhaW5pbmcgbXVsdGlwbGUgQkFOIGdlbmVyYXRpb25zIEfigoEsIEfigoIsIC4uLiwgR+KCmSwgRnVybGFuZWxsbyBldCBhbC4gcHJvcG9zZSBHRVNEIChHZW5lcmF0aW5nIEVuc2VtYmxlIGJ5IFNlcXVlbnRpYWwgRGlzdGlsbGF0aW9uKTogY29tYmluZSBhbGwgZ2VuZXJhdGlvbnMgYnkgYXZlcmFnaW5nIHRoZWlyIHNvZnRtYXggcHJlZGljdGlvbnMuIFRoaXMgZW5zZW1ibGUgZXhwbG9pdHMgdGhlIGRpdmVyc2l0eSBpbnRyb2R1Y2VkIGJ5IHNlcXVlbnRpYWwgZGlzdGlsbGF0aW9uIOKAlCBlYWNoIGdlbmVyYXRpb24gbWFrZXMgZGlmZmVyZW50IHR5cGVzIG9mIGVycm9ycyBiZWNhdXNlIGl0IHdhcyB0cmFpbmVkIG9uIGEgZGlmZmVyZW50IHN1cGVydmlzaW9uIHNpZ25hbC4gR0VTRCBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybXMgYm90aCBhIHN0YW5kYXJkIGVuc2VtYmxlIG9mIGluZGVwZW5kZW50bHkgdHJhaW5lZCBtb2RlbHMgYW5kIGFueSBzaW5nbGUgQkFOIGdlbmVyYXRpb24sIGF0IG5vIGFkZGl0aW9uYWwgdHJhaW5pbmcgY29zdCBvbmNlIGFsbCBnZW5lcmF0aW9ucyBleGlzdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHR5cGluZyBpbXBvcnQgTGlzdFxuXG5kZWYgZ2VzZF9lbnNlbWJsZV9wcmVkaWN0KG1vZGVsczogTGlzdFt0b3JjaC5ubi5Nb2R1bGVdLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeDogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdGVtcGVyYXR1cmU6IGZsb2F0ID0gMS4wKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJHRVNEOiBhdmVyYWdlIHNvZnRtYXggcHJvYmFiaWxpdGllcyBmcm9tIGFsbCBCQU4gZ2VuZXJhdGlvbnMgRzEuLi5Hbi5cIlwiXCJcbiAgICBhbGxfcHJvYnMgPSBbXVxuICAgIGZvciBtb2RlbCBpbiBtb2RlbHM6XG4gICAgICAgIG1vZGVsLmV2YWwoKVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIGxvZ2l0cyA9IG1vZGVsKHgpXG4gICAgICAgICAgICBwcm9icyA9IEYuc29mdG1heChsb2dpdHMgLyB0ZW1wZXJhdHVyZSwgZGltPS0xKVxuICAgICAgICAgICAgYWxsX3Byb2JzLmFwcGVuZChwcm9icylcbiAgICByZXR1cm4gdG9yY2guc3RhY2soYWxsX3Byb2JzLCBkaW09MCkubWVhbihkaW09MClcblxuZGVmIGV2YWx1YXRlX2dlc2QobW9kZWxzLCB0ZXN0X2xvYWRlciwgZGV2aWNlKTpcbiAgICBcIlwiXCJFdmFsdWF0ZSBHRVNEIGVuc2VtYmxlIGFjY3VyYWN5IG9uIHRlc3Qgc2V0LlwiXCJcIlxuICAgIGNvcnJlY3QsIHRvdGFsID0gMCwgMFxuICAgIGZvciBYLCB5IGluIHRlc3RfbG9hZGVyOlxuICAgICAgICBYLCB5ID0gWC50byhkZXZpY2UpLCB5LnRvKGRldmljZSlcbiAgICAgICAgYXZnX3Byb2JzID0gZ2VzZF9lbnNlbWJsZV9wcmVkaWN0KG1vZGVscywgWClcbiAgICAgICAgcHJlZHMgPSBhdmdfcHJvYnMuYXJnbWF4KGRpbT0tMSlcbiAgICAgICAgY29ycmVjdCArPSAocHJlZHMgPT0geSkuc3VtKCkuaXRlbSgpXG4gICAgICAgIHRvdGFsICs9IHkuc2l6ZSgwKVxuICAgIHJldHVybiBjb3JyZWN0IC8gdG90YWxcblxuIyBHRVNEIG91dHBlcmZvcm1zIGFueSBzaW5nbGUgQkFOIGR1ZSB0byBjb21wbGVtZW50YXJ5IGVycm9yIHBhdHRlcm5zXG5wcmludChcdTAwMjdHRVNEOiBHMSwgRzIsIEczIGVhY2ggdHJhaW5lZCBvbiB0aGUgcHJldmlvdXMgZ2VuZXJhdGlvbiBzb2Z0IHRhcmdldHMuXHUwMDI3KVxucHJpbnQoXHUwMDI3RW5zZW1ibGUgb2Ygc2VxdWVudGlhbGx5IGRpc3RpbGxlZCBtb2RlbHMgY2FwdHVyZXMgY29tcGxlbWVudGFyeSBlcnJvcnMuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBTYW1lLUNhcGFjaXR5IERpc3RpbGxhdGlvbiBJbXByb3ZlcyBBY2N1cmFjeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhyZWUgbWVjaGFuaXNtcyBleHBsYWluIHdoeSBhIHNhbWUtY2FwYWNpdHkgc3R1ZGVudCBvdXRwZXJmb3JtcyBpdHMgdGVhY2hlci4gRmlyc3QsIHNvZnQgdGFyZ2V0cyBwcm92aWRlIGEgcmljaGVyIGdyYWRpZW50IHNpZ25hbDogdGhlIEtMIGRpdmVyZ2VuY2UgbG9zcyBjYXJyaWVzIGluZm9ybWF0aW9uIGFib3V0IGV2ZXJ5IGNsYXNzIHByb2JhYmlsaXR5LCBub3QganVzdCB0aGUgY29ycmVjdCBjbGFzcy4gU2Vjb25kLCB0aGUgdGVhY2hlclx1MDAyN3Mgc29mdCBsYWJlbHMgcmVkdWNlIGVmZmVjdGl2ZSBsYWJlbCBub2lzZSDigJQgbWlzY2xhc3NpZmllZCB0cmFpbmluZyBleGFtcGxlcyByZWNlaXZlIHNvZnRlciBzdXBlcnZpc2lvbiwgZGFtcGVuaW5nIGdyYWRpZW50IHNwaWtlcyBmcm9tIGhhcmQgbGFiZWxzLiBUaGlyZCwgdGhlIGRpc3RpbGxhdGlvbiBsb3NzIGFjdHMgYXMgaW1wbGljaXQgcmVndWxhcmlzYXRpb24sIGVuY291cmFnaW5nIHRoZSBzdHVkZW50IHRvIHByb2R1Y2UgY2FsaWJyYXRlZCwgc21vb3RoIGRpc3RyaWJ1dGlvbnMgcmF0aGVyIHRoYW4gc2hhcnBseSBwZWFrZWQgb25lcy4gVGhpcyBzbW9vdGhlciBkaXN0cmlidXRpb24gZ2VuZXJhbGlzZXMgYmV0dGVyLiBEYXJrIGtub3dsZWRnZSDigJQgdGhlIHNpZ25hbCBlbWJlZGRlZCBpbiBzbWFsbCBub24tbWF4aW11bSBjbGFzcyBwcm9iYWJpbGl0aWVzIOKAlCBpcyB0aGUgbWVjaGFuaXNtIHVuZGVybHlpbmcgYWxsIHRocmVlIGVmZmVjdHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWNjdXJhY3kgUGVyIEdlbmVyYXRpb24g4oCUIEVtcGlyaWNhbCBSZXN1bHRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGdXJsYW5lbGxvIGV0IGFsLiBldmFsdWF0ZWQgQkFOcyBvbiBEZW5zZU5ldC00MCBvbiBDSUZBUi0xMCBhbmQgQ0lGQVItMTAwLiBUaGUgYmFzZWxpbmUgYWNoaWV2ZXMgOTMuMTIlIG9uIENJRkFSLTEwLiBCQU4tMSBpbXByb3ZlcyB0byA5My44NSUgKCswLjczJSksIEJBTi0yIHRvIDk0LjEwJSAoKzAuMjUlIG92ZXIgQkFOLTEpLCBhbmQgQkFOLTMgdG8gOTQuMjElICgrMC4xMSUgb3ZlciBCQU4tMikuIEdhaW5zIGRpbWluaXNoIHdpdGggZWFjaCBnZW5lcmF0aW9uIGFzIHRoZSB0ZWFjaGVyLXN0dWRlbnQgcXVhbGl0eSBnYXAgbmFycm93cy4gVGhlIEdFU0QgZW5zZW1ibGUgb2YgYWxsIGZvdXIgZ2VuZXJhdGlvbnMgYWNoaWV2ZXMgOTQuNzElLCBzdXJwYXNzaW5nIGFueSBzaW5nbGUgZ2VuZXJhdGlvbiBhbmQgb3V0cGVyZm9ybWluZyBhbiBpbmRlcGVuZGVudGx5IHRyYWluZWQgZW5zZW1ibGUgb2YgZm91ciBtb2RlbHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG4jIEVtcGlyaWNhbCByZXN1bHRzOiBEZW5zZU5ldC00MCBvbiBDSUZBUi0xMCBhbmQgQ0lGQVItMTAwIChGdXJsYW5lbGxvIGV0IGFsLiAyMDE4KVxuZ2VuZXJhdGlvbnMgID0gW1x1MDAyN0cxIChCYXNlbGluZSlcdTAwMjcsIFx1MDAyN0cyIChCQU4tMSlcdTAwMjcsIFx1MDAyN0czIChCQU4tMilcdTAwMjcsIFx1MDAyN0c0IChCQU4tMylcdTAwMjddXG5jaWZhcjEwX2FjYyAgPSBbOTMuMTIsIDkzLjg1LCA5NC4xMCwgOTQuMjFdXG5jaWZhcjEwMF9hY2MgPSBbNzAuNDgsIDcxLjE0LCA3MS42MiwgNzEuODldXG5cbnByaW50KFx1MDAyN0RlbnNlTmV0LTQwIEJvcm4tQWdhaW4gTmV0d29yayBHZW5lcmF0aW9uczpcdTAwMjcpXG5wcmludChmXHUwMDI3e1wiR2VuZXJhdGlvblwiOlx1MDAzYzIwfSB7XCJDSUZBUi0xMFwiOlx1MDAzZTEwfSB7XCJDSUZBUi0xMDBcIjpcdTAwM2UxMH0ge1wiRGVsdGExMFwiOlx1MDAzZTl9IHtcIkRlbHRhMTAwXCI6XHUwMDNlMTB9XHUwMDI3KVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDYzKVxuZm9yIGksIChnLCBjMTAsIGMxMDApIGluIGVudW1lcmF0ZSh6aXAoZ2VuZXJhdGlvbnMsIGNpZmFyMTBfYWNjLCBjaWZhcjEwMF9hY2MpKTpcbiAgICBkMTAgID0gYzEwICAtIGNpZmFyMTBfYWNjWzBdICBpZiBpIFx1MDAzZSAwIGVsc2UgMC4wXG4gICAgZDEwMCA9IGMxMDAgLSBjaWZhcjEwMF9hY2NbMF0gaWYgaSBcdTAwM2UgMCBlbHNlIDAuMFxuICAgIHByaW50KGZcdTAwMjd7ZzpcdTAwM2MyMH0ge2MxMDpcdTAwM2UxMC4yZn0ge2MxMDA6XHUwMDNlMTAuMmZ9IHtkMTA6XHUwMDNlKzkuMmZ9IHtkMTAwOlx1MDAzZSsxMC4yZn1cdTAwMjcpXG5cbiMgR0VTRCBlbnNlbWJsZSByZXN1bHRzXG5nZXNkX2MxMCwgZ2VzZF9jMTAwID0gOTQuNzEsIDcyLjg5XG5wcmludChmXHUwMDI3XFxue1wiR0VTRCAoZW5zZW1ibGUpXCI6XHUwMDNjMjB9IHtnZXNkX2MxMDpcdTAwM2UxMC4yZn0ge2dlc2RfYzEwMDpcdTAwM2UxMC4yZn1cdTAwMjcsIGVuZD1cdTAwMjdcdTAwMjcpXG5wcmludChmXHUwMDI3IHtnZXNkX2MxMC1jaWZhcjEwX2FjY1swXTpcdTAwM2UrOS4yZn0ge2dlc2RfYzEwMC1jaWZhcjEwMF9hY2NbMF06XHUwMDNlKzEwLjJmfVx1MDAyNylcbnByaW50KGZcdTAwMjdcXG5CQU4gY2hhaW4gKyBHRVNEIGdhaW46IENJRkFSLTEwPXtnZXNkX2MxMC1jaWZhcjEwX2FjY1swXTorLjJmfSUsIENJRkFSLTEwMD17Z2VzZF9jMTAwLWNpZmFyMTAwX2FjY1swXTorLjJmfSVcdTAwMjcpXG5wcmludChcdTAwMjdLZXkgaW5zaWdodDogQkFOLTEgYWxyZWFkeSBpbXByb3ZlcyBvdmVyIEcxIGRlc3BpdGUgaWRlbnRpY2FsIGNhcGFjaXR5Llx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEYXJrIEtub3dsZWRnZSBhbmQgU29mdCBUYXJnZXQgUXVhbGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSGludG9uIGV0IGFsLiAoMjAxNSkgY29pbmVkIFx1MDAyN2Rhcmsga25vd2xlZGdlXHUwMDI3IHRvIGRlc2NyaWJlIGluZm9ybWF0aW9uIGVtYmVkZGVkIGluIGEgbW9kZWxcdTAwMjdzIG5vbi1tYXhpbXVtIGNsYXNzIHByb2JhYmlsaXRpZXMuIEEgd2VsbC10cmFpbmVkIGNsYXNzaWZpZXIgYXNzaWducyBub24tbmVnbGlnaWJsZSBwcm9iYWJpbGl0eSB0byB2aXN1YWxseSBzaW1pbGFyIGNsYXNzZXM6IGEgY2F0IGltYWdlIG1heSByZWNlaXZlIHByb2JhYmlsaXR5IDAuMDQgb24gXHUwMDI3dGlnZXJcdTAwMjcgYW5kIDAuMDIgb24gXHUwMDI3ZG9nXHUwMDI3LCBidXQgbmVhci16ZXJvIG9uIFx1MDAyN3RydWNrXHUwMDI3LiBUaGlzIGludGVyLWNsYXNzIHNpbWlsYXJpdHkgaXMgYWJzZW50IGluIG9uZS1ob3QgbGFiZWxzLiBFeHBlY3RlZCBDYWxpYnJhdGlvbiBFcnJvciAoRUNFKSBtZWFzdXJlcyBob3cgd2VsbCBjb25maWRlbmNlIGFsaWducyB3aXRoIGFjY3VyYWN5LiBTb2Z0IHRhcmdldHMgZnJvbSBhIGNhbGlicmF0ZWQgdGVhY2hlciBoYXZlIGxvd2VyIEVDRSB0aGFuIGhhcmQgb25lLWhvdCBsYWJlbHMsIGluZGljYXRpbmcgdGhleSBjb252ZXkgbW9yZSBob25lc3QgdW5jZXJ0YWludHkgYW5kIHJpY2hlciBpbmZvcm1hdGlvbiBwZXIgdHJhaW5pbmcgZXhhbXBsZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBleHBlY3RlZF9jYWxpYnJhdGlvbl9lcnJvcihwcm9iczogdG9yY2guVGVuc29yLCBsYWJlbHM6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9iaW5zOiBpbnQgPSAxMCkgLVx1MDAzZSBmbG9hdDpcbiAgICBcIlwiXCJDb21wdXRlIEVDRTogfGFjY3VyYWN5IC0gY29uZmlkZW5jZXwgd2VpZ2h0ZWQgYnkgYmluIGZyYWN0aW9uLlwiXCJcIlxuICAgIGNvbmZpZGVuY2VzLCBwcmVkaWN0aW9ucyA9IHByb2JzLm1heChkaW09LTEpXG4gICAgYWNjdXJhY2llcyA9IHByZWRpY3Rpb25zLmVxKGxhYmVscylcbiAgICBlY2UgPSAwLjBcbiAgICBlZGdlcyA9IHRvcmNoLmxpbnNwYWNlKDAsIDEsIG5fYmlucyArIDEpXG4gICAgZm9yIGkgaW4gcmFuZ2Uobl9iaW5zKTpcbiAgICAgICAgbG8sIGhpID0gZWRnZXNbaV0uaXRlbSgpLCBlZGdlc1tpICsgMV0uaXRlbSgpXG4gICAgICAgIGluX2JpbiA9IChjb25maWRlbmNlcyBcdTAwM2U9IGxvKSBcdTAwMjYgKGNvbmZpZGVuY2VzIFx1MDAzYyBoaSlcbiAgICAgICAgaWYgaW5fYmluLnN1bSgpID09IDA6XG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICBiaW5fYWNjICA9IGFjY3VyYWNpZXNbaW5fYmluXS5mbG9hdCgpLm1lYW4oKS5pdGVtKClcbiAgICAgICAgYmluX2NvbmYgPSBjb25maWRlbmNlc1tpbl9iaW5dLm1lYW4oKS5pdGVtKClcbiAgICAgICAgYmluX2ZyYWMgPSBpbl9iaW4uZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG4gICAgICAgIGVjZSArPSBiaW5fZnJhYyAqIGFicyhiaW5fYWNjIC0gYmluX2NvbmYpXG4gICAgcmV0dXJuIGVjZVxuXG50b3JjaC5tYW51YWxfc2VlZCg0Milcbm4sIEMgPSAxMDAwLCAxMFxudGVhY2hlcl9sb2dpdHMgPSB0b3JjaC5yYW5kbihuLCBDKVxudGVhY2hlcl9wcm9icyAgPSBGLnNvZnRtYXgodGVhY2hlcl9sb2dpdHMsIGRpbT0tMSlcbmxhYmVscyA9IHRlYWNoZXJfbG9naXRzLmFyZ21heChkaW09LTEpXG5oYXJkX3Byb2JzID0gRi5vbmVfaG90KGxhYmVscywgQykuZmxvYXQoKVxuXG5lY2Vfc29mdCA9IGV4cGVjdGVkX2NhbGlicmF0aW9uX2Vycm9yKHRlYWNoZXJfcHJvYnMsIGxhYmVscylcbmVjZV9oYXJkID0gZXhwZWN0ZWRfY2FsaWJyYXRpb25fZXJyb3IoaGFyZF9wcm9icywgbGFiZWxzKVxucHJpbnQoZlx1MDAyN1NvZnQgdGFyZ2V0IEVDRToge2VjZV9zb2Z0Oi40Zn0gICAodGVhY2hlciBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb24pXHUwMDI3KVxucHJpbnQoZlx1MDAyN0hhcmQgbGFiZWwgRUNFOiAge2VjZV9oYXJkOi40Zn0gIChvbmUtaG90OiAxMDAlIGNvbmZpZGVudClcdTAwMjcpXG5wcmludChmXHUwMDI3RUNFIHJlZHVjdGlvbiBmcm9tIHNvZnQgdGFyZ2V0czoge2VjZV9oYXJkIC0gZWNlX3NvZnQ6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN1NvZnQgdGFyZ2V0cyBlbmNvZGUgaW50ZXItY2xhc3Mgc2ltaWxhcml0eTogY2F0cyBzaW1pbGFyIHRvIHRpZ2Vycywgbm90IHRydWNrcy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29ubmVjdGlvbiB0byBTbmFwc2hvdCBFbnNlbWJsZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikh1YW5nIGV0IGFsLiAoMjAxNykgcHJvcG9zZWQgU25hcHNob3QgRW5zZW1ibGVzOiB1c2UgYSBjeWNsaWNhbCBsZWFybmluZyByYXRlIHNjaGVkdWxlIHRvIGNvbnZlcmdlIHRvIG11bHRpcGxlIGxvY2FsIG1pbmltYSBpbiBhIHNpbmdsZSB0cmFpbmluZyBydW4sIHNhdmluZyBjaGVja3BvaW50cyBhdCBlYWNoIHRyb3VnaC4gVGhlIGVuc2VtYmxlIG91dHBlcmZvcm1zIGFueSBpbmRpdmlkdWFsIHNuYXBzaG90LiBCQU5zIGFjaGlldmUgZGl2ZXJzaXR5IGJ5IGEgZGlmZmVyZW50IG1lY2hhbmlzbSDigJQgc2VxdWVudGlhbCBkaXN0aWxsYXRpb24gY2hhbmdlcyB0aGUgZWZmZWN0aXZlIGxvc3MgbGFuZHNjYXBlIHNlZW4gYnkgZWFjaCBnZW5lcmF0aW9uIOKAlCBidXQgYm90aCBhcHByb2FjaGVzIHByb2R1Y2UgZW5zZW1ibGVzIG9mIG1vZGVscyB3aXRoIGNvbXBsZW1lbnRhcnkgZXJyb3IgcGF0dGVybnMuIFRoZSBrZXkgZGlmZmVyZW5jZSBpcyB0aGF0IEdFU0QgbWVtYmVycyBhcmUgZnVsbHkgaW5kZXBlbmRlbnRseSB0cmFpbmVkLCB3aGlsZSBzbmFwc2hvdCBtZW1iZXJzIHNoYXJlIGFsbCB0cmFpbmluZyBoaXN0b3J5IHVwIHRvIGVhY2ggTFIgY3ljbGUuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IldoZW4gdG8gVXNlIEJBTnMgSW5zdGVhZCBvZiBMYXJnZXIgTW9kZWxzIiwiY29udGVudCI6IklmIHlvdSBhcmUgYXQgYSBjb21wdXRlIGJ1ZGdldCBsaW1pdCBhbmQgY2Fubm90IHRyYWluIGEgbGFyZ2VyIGFyY2hpdGVjdHVyZSwgcnVuIDItMyBCQU4gZ2VuZXJhdGlvbnMgb24geW91ciBleGlzdGluZyBhcmNoaXRlY3R1cmUuIEVhY2ggZ2VuZXJhdGlvbiBhZGRzIHRoZSBzYW1lIHRyYWluaW5nIGNvc3QgYXMgdGhlIG9yaWdpbmFsIHJ1biwgYnV0IGNvbnNpc3RlbnRseSBpbXByb3ZlcyBhY2N1cmFjeSBieSAwLjUtMS4wJSBvbiBjbGFzc2lmaWNhdGlvbiBiZW5jaG1hcmtzIHdpdGhvdXQgY2hhbmdpbmcgbW9kZWwgc2l6ZSBvciBpbmZlcmVuY2UgY29zdC4gVGhpcyBpcyBwYXJ0aWN1bGFybHkgZWZmZWN0aXZlIHdoZW4geW91IGhhdmUgYWxyZWFkeSB0dW5lZCBoeXBlcnBhcmFtZXRlcnMgZm9yIHRoZSBiYXNlIGFyY2hpdGVjdHVyZSBhbmQgd2FudCBmdXJ0aGVyIGdhaW5zIGF0IHplcm8gbW9kZWwtc2l6ZSBjb3N0LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIlBhcmFtcyIsIkNJRkFSLTEwIEFjYyIsIkluZmVyZW5jZSBDb3N0IiwiVHJhaW5pbmcgQ29zdCIsIkRpdmVyc2l0eSBNZWNoYW5pc20iXSwicm93cyI6W1siRzEgKEJhc2VsaW5lKSIsIjF4IiwiOTMuMTIlIiwiMXgiLCIxeCIsIlJhbmRvbSBpbml0ICsgU0dEIl0sWyJHMiAoQkFOLTEpIiwiMXgiLCI5My44NSUiLCIxeCIsIjJ4IiwiRzEgc29mdCB0YXJnZXRzIl0sWyJHMyAoQkFOLTIpIiwiMXgiLCI5NC4xMCUiLCIxeCIsIjN4IiwiRzIgc29mdCB0YXJnZXRzIl0sWyJHNCAoQkFOLTMpIiwiMXgiLCI5NC4yMSUiLCIxeCIsIjR4IiwiRzMgc29mdCB0YXJnZXRzIl0sWyJHRVNEIChHMS1HNCkiLCI0eCAoY29tYmluZWQpIiwiOTQuNzElIiwiNHgiLCI0eCIsIlNlcXVlbnRpYWwgZGlzdGlsbGF0aW9uIl0sWyJTdGFuZGFyZCBlbnNlbWJsZSAoNHgpIiwiNHgiLCI5NC40MSUiLCI0eCIsIjR4IiwiSW5kZXBlbmRlbnQgcmFuZG9tIGluaXRzIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJBTiB0cmFpbmluZyB1c2VzIEtMIGRpdmVyZ2VuY2UgbG9zcyBhdCB0ZW1wZXJhdHVyZSBUPTQsIGNvbWJpbmVkIHdpdGggaGFyZCBjcm9zcy1lbnRyb3B5IGF0IHdlaWdodCBhbHBoYS4iLCJHYWlucyBwZXIgZ2VuZXJhdGlvbiBkaW1pbmlzaDogQkFOLTEgKzAuNzMlLCBCQU4tMiArMC4yNSUsIEJBTi0zICswLjExJSBvbiBDSUZBUi0xMC4iLCJHRVNEIGF2ZXJhZ2VzIHNvZnRtYXggcHJvYmFiaWxpdGllcyAobm90IGxvZ2l0cykgYWNyb3NzIGFsbCBnZW5lcmF0aW9ucyBHMS4uLkduLiIsIlRlbXBlcmF0dXJlIFQgY29udHJvbHMgZGFyayBrbm93bGVkZ2UgdmlzaWJpbGl0eTogVD00IGlzIHN0YW5kYXJkOyBUPTEgZGVncmFkZXMgdG8gaGFyZCBkaXN0aWxsYXRpb24uIiwiQkFOcyB3b3JrIGZvciBhbnkgYXJjaGl0ZWN0dXJlIOKAlCBDTk5zLCB0cmFuc2Zvcm1lcnMsIE1MUHMg4oCUIGFuZCBhbnkgY2xhc3NpZmljYXRpb24gZGF0YXNldC4iLCJHRVNEIGJlYXRzIGEgc3RhbmRhcmQgZW5zZW1ibGUgb2YgNCBpbmRlcGVuZGVudGx5IHRyYWluZWQgbW9kZWxzIGJ5IH4wLjMlIG9uIENJRkFSLTEwLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Born-Again Networks — Sequential Self-Distillation

Born-again networks (BANs), introduced by Furlanello et al. (2018), apply knowledge distillation in an unexpected direction: instead of compressing a large teacher into a smaller student, they distil a model into an identical-capacity copy. The result is a student that consistently outperforms the teacher on the same task despite having the same number of parameters. This violates the naive intuition that distillation only helps when the student is smaller — the benefit comes not from compression but from the richer supervision signal encoded in the teacher's soft probability outputs.

## What Are Born-Again Networks?

A born-again network is a model trained by minimising the KL divergence between its output distribution and the soft probabilities of a teacher with identical architecture. Because teacher and student have the same capacity, the student cannot exploit the teacher's knowledge through compression. Instead, it learns a smoother decision boundary shaped by inter-class similarity information in the teacher's soft labels. The teacher's non-argmax probabilities — for example, assigning probability 0.03 to 'automobile' when classifying a 'truck' — encode semantic relationships that act as regularisation, reducing effective label noise on ambiguous examples.

## The BAN Training Chain

BANs are applied sequentially: G₁ is the baseline model trained on hard labels. G₂ (BAN-1) is trained using G₁'s soft targets at temperature T. G₃ (BAN-2) uses G₂'s soft targets, and so on. Unlike traditional KD where the teacher is a fixed larger model, the BAN teacher improves with each generation, providing progressively richer supervision. Temperature T controls softness — higher T spreads probability mass more evenly across classes, revealing more inter-class structure. A combined loss blends hard labels (cross-entropy) and soft targets (KL divergence), weighted by alpha.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

def train_ban_generation(teacher, student, train_loader, device,
                         temperature=4.0, alpha=0.5, epochs=10, lr=1e-3):
    """Train student as a BAN of teacher using soft target distillation."""
    teacher.eval()
    student.train()
    optimizer = optim.Adam(student.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    for epoch in range(epochs):
        total_loss = 0.0
        for X, y in train_loader:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            with torch.no_grad():
                teacher_logits = teacher(X)
                soft_targets = F.softmax(teacher_logits / temperature, dim=-1)
            student_logits = student(X)
            hard_loss = criterion(student_logits, y)
            soft_loss = F.kl_div(
                F.log_softmax(student_logits / temperature, dim=-1),
                soft_targets, reduction='batchmean'
            ) * (temperature ** 2)
            loss = (1 - alpha) * hard_loss + alpha * soft_loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f'Epoch {epoch+1}/{epochs}: loss={total_loss/len(train_loader):.4f}')
    return student

# BAN chain: G1 (baseline) -> G2 (BAN-1) -> G3 (BAN-2)
print('BAN chain: G1 -> G2 via G1 soft targets, G2 -> G3 via G2 soft targets')
```

## GESD — Generating Ensemble by Sequential Distillation

After training multiple BAN generations G₁, G₂, ..., Gₙ, Furlanello et al. propose GESD (Generating Ensemble by Sequential Distillation): combine all generations by averaging their softmax predictions. This ensemble exploits the diversity introduced by sequential distillation — each generation makes different types of errors because it was trained on a different supervision signal. GESD consistently outperforms both a standard ensemble of independently trained models and any single BAN generation, at no additional training cost once all generations exist.

```python
import torch
import torch.nn.functional as F
from typing import List

def gesd_ensemble_predict(models: List[torch.nn.Module],
                           x: torch.Tensor,
                           temperature: float = 1.0) -> torch.Tensor:
    """GESD: average softmax probabilities from all BAN generations G1...Gn."""
    all_probs = []
    for model in models:
        model.eval()
        with torch.no_grad():
            logits = model(x)
            probs = F.softmax(logits / temperature, dim=-1)
            all_probs.append(probs)
    return torch.stack(all_probs, dim=0).mean(dim=0)

def evaluate_gesd(models, test_loader, device):
    """Evaluate GESD ensemble accuracy on test set."""
    correct, total = 0, 0
    for X, y in test_loader:
        X, y = X.to(device), y.to(device)
        avg_probs = gesd_ensemble_predict(models, X)
        preds = avg_probs.argmax(dim=-1)
        correct += (preds == y).sum().item()
        total += y.size(0)
    return correct / total

# GESD outperforms any single BAN due to complementary error patterns
print('GESD: G1, G2, G3 each trained on the previous generation soft targets.')
print('Ensemble of sequentially distilled models captures complementary errors.')
```

## Why Same-Capacity Distillation Improves Accuracy

Three mechanisms explain why a same-capacity student outperforms its teacher. First, soft targets provide a richer gradient signal: the KL divergence loss carries information about every class probability, not just the correct class. Second, the teacher's soft labels reduce effective label noise — misclassified training examples receive softer supervision, dampening gradient spikes from hard labels. Third, the distillation loss acts as implicit regularisation, encouraging the student to produce calibrated, smooth distributions rather than sharply peaked ones. This smoother distribution generalises better. Dark knowledge — the signal embedded in small non-maximum class probabilities — is the mechanism underlying all three effects.

## Accuracy Per Generation — Empirical Results

Furlanello et al. evaluated BANs on DenseNet-40 on CIFAR-10 and CIFAR-100. The baseline achieves 93.12% on CIFAR-10. BAN-1 improves to 93.85% (+0.73%), BAN-2 to 94.10% (+0.25% over BAN-1), and BAN-3 to 94.21% (+0.11% over BAN-2). Gains diminish with each generation as the teacher-student quality gap narrows. The GESD ensemble of all four generations achieves 94.71%, surpassing any single generation and outperforming an independently trained ensemble of four models.

```python
import numpy as np

# Empirical results: DenseNet-40 on CIFAR-10 and CIFAR-100 (Furlanello et al. 2018)
generations  = ['G1 (Baseline)', 'G2 (BAN-1)', 'G3 (BAN-2)', 'G4 (BAN-3)']
cifar10_acc  = [93.12, 93.85, 94.10, 94.21]
cifar100_acc = [70.48, 71.14, 71.62, 71.89]

print('DenseNet-40 Born-Again Network Generations:')
print(f'{"Generation":<20} {"CIFAR-10":>10} {"CIFAR-100":>10} {"Delta10":>9} {"Delta100":>10}')
print('-' * 63)
for i, (g, c10, c100) in enumerate(zip(generations, cifar10_acc, cifar100_acc)):
    d10  = c10  - cifar10_acc[0]  if i > 0 else 0.0
    d100 = c100 - cifar100_acc[0] if i > 0 else 0.0
    print(f'{g:<20} {c10:>10.2f} {c100:>10.2f} {d10:>+9.2f} {d100:>+10.2f}')

# GESD ensemble results
gesd_c10, gesd_c100 = 94.71, 72.89
print(f'\n{"GESD (ensemble)":<20} {gesd_c10:>10.2f} {gesd_c100:>10.2f}', end='')
print(f' {gesd_c10-cifar10_acc[0]:>+9.2f} {gesd_c100-cifar100_acc[0]:>+10.2f}')
print(f'\nBAN chain + GESD gain: CIFAR-10={gesd_c10-cifar10_acc[0]:+.2f}%, CIFAR-100={gesd_c100-cifar100_acc[0]:+.2f}%')
print('Key insight: BAN-1 already improves over G1 despite identical capacity.')
```

## Dark Knowledge and Soft Target Quality

Hinton et al. (2015) coined 'dark knowledge' to describe information embedded in a model's non-maximum class probabilities. A well-trained classifier assigns non-negligible probability to visually similar classes: a cat image may receive probability 0.04 on 'tiger' and 0.02 on 'dog', but near-zero on 'truck'. This inter-class similarity is absent in one-hot labels. Expected Calibration Error (ECE) measures how well confidence aligns with accuracy. Soft targets from a calibrated teacher have lower ECE than hard one-hot labels, indicating they convey more honest uncertainty and richer information per training example.

```python
import torch
import torch.nn.functional as F

def expected_calibration_error(probs: torch.Tensor, labels: torch.Tensor,
                                n_bins: int = 10) -> float:
    """Compute ECE: |accuracy - confidence| weighted by bin fraction."""
    confidences, predictions = probs.max(dim=-1)
    accuracies = predictions.eq(labels)
    ece = 0.0
    edges = torch.linspace(0, 1, n_bins + 1)
    for i in range(n_bins):
        lo, hi = edges[i].item(), edges[i + 1].item()
        in_bin = (confidences >= lo) & (confidences < hi)
        if in_bin.sum() == 0:
            continue
        bin_acc  = accuracies[in_bin].float().mean().item()
        bin_conf = confidences[in_bin].mean().item()
        bin_frac = in_bin.float().mean().item()
        ece += bin_frac * abs(bin_acc - bin_conf)
    return ece

torch.manual_seed(42)
n, C = 1000, 10
teacher_logits = torch.randn(n, C)
teacher_probs  = F.softmax(teacher_logits, dim=-1)
labels = teacher_logits.argmax(dim=-1)
hard_probs = F.one_hot(labels, C).float()

ece_soft = expected_calibration_error(teacher_probs, labels)
ece_hard = expected_calibration_error(hard_probs, labels)
print(f'Soft target ECE: {ece_soft:.4f}   (teacher probability distribution)')
print(f'Hard label ECE:  {ece_hard:.4f}  (one-hot: 100% confident)')
print(f'ECE reduction from soft targets: {ece_hard - ece_soft:.4f}')
print('Soft targets encode inter-class similarity: cats similar to tigers, not trucks.')
```

## Connection to Snapshot Ensembles

Huang et al. (2017) proposed Snapshot Ensembles: use a cyclical learning rate schedule to converge to multiple local minima in a single training run, saving checkpoints at each trough. The ensemble outperforms any individual snapshot. BANs achieve diversity by a different mechanism — sequential distillation changes the effective loss landscape seen by each generation — but both approaches produce ensembles of models with complementary error patterns. The key difference is that GESD members are fully independently trained, while snapshot members share all training history up to each LR cycle.

> **When to Use BANs Instead of Larger Models**: If you are at a compute budget limit and cannot train a larger architecture, run 2-3 BAN generations on your existing architecture. Each generation adds the same training cost as the original run, but consistently improves accuracy by 0.5-1.0% on classification benchmarks without changing model size or inference cost. This is particularly effective when you have already tuned hyperparameters for the base architecture and want further gains at zero model-size cost.

| Model | Params | CIFAR-10 Acc | Inference Cost | Training Cost | Diversity Mechanism |
| --- | --- | --- | --- | --- | --- |
| G1 (Baseline) | 1x | 93.12% | 1x | 1x | Random init + SGD |
| G2 (BAN-1) | 1x | 93.85% | 1x | 2x | G1 soft targets |
| G3 (BAN-2) | 1x | 94.10% | 1x | 3x | G2 soft targets |
| G4 (BAN-3) | 1x | 94.21% | 1x | 4x | G3 soft targets |
| GESD (G1-G4) | 4x (combined) | 94.71% | 4x | 4x | Sequential distillation |
| Standard ensemble (4x) | 4x | 94.41% | 4x | 4x | Independent random inits |

- BAN training uses KL divergence loss at temperature T=4, combined with hard cross-entropy at weight alpha.
- Gains per generation diminish: BAN-1 +0.73%, BAN-2 +0.25%, BAN-3 +0.11% on CIFAR-10.
- GESD averages softmax probabilities (not logits) across all generations G1...Gn.
- Temperature T controls dark knowledge visibility: T=4 is standard; T=1 degrades to hard distillation.
- BANs work for any architecture — CNNs, transformers, MLPs — and any classification dataset.
- GESD beats a standard ensemble of 4 independently trained models by ~0.3% on CIFAR-10.

---

