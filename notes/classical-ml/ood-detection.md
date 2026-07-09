---
title: "OOD Detection — Energy Score, Mahalanobis, and MaxSoftmax"
slug: "ood-detection"
description: "Compare OOD detection methods for neural classifiers: MaxSoftmax baseline, ODIN with temperature scaling and input perturbation, Mahalanobis distance in feature space, and the energy score — with AUROC benchmarks and post-hoc implementation guidance."
tags: ["anomaly-detection", "density-estimation", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT3V0LW9mLWRpc3RyaWJ1dGlvbiAoT09EKSBkZXRlY3Rpb24gYXNrczogZ2l2ZW4gYSBtb2RlbCB0cmFpbmVkIG9uIGluLWRpc3RyaWJ1dGlvbiAoSUQpIGRhdGEsIGNhbiB3ZSBkZXRlY3QgaW5wdXRzIGZyb20gYSBkaWZmZXJlbnQgZGlzdHJpYnV0aW9uIGF0IHRlc3QgdGltZSB3aXRob3V0IHJldHJhaW5pbmc/IFVubGlrZSBhbm9tYWx5IGRldGVjdGlvbiBpbiB1bnN1cGVydmlzZWQgc2V0dGluZ3MsIE9PRCBkZXRlY3Rpb24gZXhwbG9pdHMgdGhlIHN0cnVjdHVyZSBvZiBhIHByZXRyYWluZWQgY2xhc3NpZmllciDigJQgaXRzIHNvZnRtYXggb3V0cHV0cywgaW50ZXJuYWwgZmVhdHVyZSByZXByZXNlbnRhdGlvbnMsIGFuZCBsb2dpdHMg4oCUIHRvIGRlcml2ZSBhIHNlcGFyYXRpb24gc2NvcmUuIFRoZSBrZXkgY2hhbGxlbmdlIGlzIHRoYXQgbmV1cmFsIG5ldHdvcmtzIGFyZSBvZnRlbiBvdmVyY29uZmlkZW50IG9uIE9PRCBpbnB1dHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJNYXhTb2Z0bWF4IChIZW5kcnlja3MgXHUwMDI2IEdpbXBlbCAyMDE3KTogc2ltcGxlc3QgYmFzZWxpbmUg4oCUIG1heCBjbGFzcyBwcm9iYWJpbGl0eSBpcyBsb3cgZm9yIE9PRDsgd29ya3MgcG9vcmx5IGR1ZSB0byBvdmVyY29uZmlkZW5jZS4iLCJPRElOIChMaWFuZyBldCBhbC4gMjAxOCk6IHRlbXBlcmF0dXJlIHNjYWxpbmcgKyBhZHZlcnNhcmlhbCBwZXJ0dXJiYXRpb247IGxhcmdlIEFVUk9DIGltcHJvdmVtZW50IG92ZXIgTWF4U29mdG1heC4iLCJNYWhhbGFub2JpcyAoTGVlIGV0IGFsLiAyMDE4KTogY2xhc3MtY29uZGl0aW9uYWwgR2F1c3NpYW5zIGluIGZlYXR1cmUgc3BhY2U7IHN0cm9uZ2VzdCBmZWF0dXJlLWJhc2VkIHBvc3QtaG9jIG1ldGhvZC4iLCJFbmVyZ3kgc2NvcmUgKExpdSBldCBhbC4gMjAyMCk6IOKIklTCt2xvZyDOoyBleHAoZuKCli9UKTsgdGhlb3JldGljYWxseSBncm91bmRlZCBhbmQgZWFzeSB0byBjb21wdXRlLiIsIlZpTSAoV2FuZyBldCBhbC4gMjAyMik6IHZpcnR1YWwtbWF0Y2hlZCBsb2dpdHMgdmlhIG51bGwtc3BhY2UgcHJvamVjdGlvbjsgdG9wIHBlcmZvcm1lciBvbiBJbWFnZU5ldC1zY2FsZSBiZW5jaG1hcmtzLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbi1EaXN0cmlidXRpb24gdnMgT3V0LW9mLURpc3RyaWJ1dGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBtb2RlbCB0cmFpbmVkIG9uIENJRkFSLTEwIChuYXR1cmFsIGltYWdlcykgc2VlcyBzZW1hbnRpY2FsbHkgZGlmZmVyZW50IGlucHV0cyBhdCBkZXBsb3ltZW50OiBtZWRpY2FsIGltYWdlcywgc2F0ZWxsaXRlIGltYWdlcywgYWR2ZXJzYXJpYWwgZXhhbXBsZXMuIE9PRCBkZXRlY3Rpb24gbXVzdCBmbGFnIHRoZXNlIGJlZm9yZSB0aGUgbW9kZWwgbWFrZXMgYSBkYW5nZXJvdXNseSBjb25maWRlbnQgd3JvbmcgcHJlZGljdGlvbi4gRXZhbHVhdGlvbiB1c2VzIHR3byBtZXRyaWNzOiBBVVJPQyAoYXJlYSB1bmRlciB0aGUgUk9DIGN1cnZlIGZvciBJRCB2cyBPT0QgYmluYXJ5IGNsYXNzaWZpY2F0aW9uKSBhbmQgRlBSOTUgKGZhbHNlLXBvc2l0aXZlIHJhdGUgd2hlbiBUUFI9OTUlKS4gVGhlIGJlbmNobWFyayBpbnZvbHZlcyB0aGUgbW9kZWwgcHJlZGljdGluZyBJRCBjb3JyZWN0bHkgb24gaXRzIHRlc3Qgc2V0IHdoaWxlIGJlaW5nIGV4cG9zZWQgdG8gYSBzZXBhcmF0ZSBPT0QgZGF0YXNldC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IHJvY19hdWNfc2NvcmVcblxuY2xhc3MgU2ltcGxlQ2xhc3NpZmllcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX2luLCBuX2NsYXNzZXMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5mZWF0dXJlcyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoZF9pbiwgMTI4KSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDEyOCwgNjQpLCBubi5SZUxVKCkpXG4gICAgICAgIHNlbGYuaGVhZCA9IG5uLkxpbmVhcig2NCwgbl9jbGFzc2VzKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5oZWFkKHNlbGYuZmVhdHVyZXMoeCkpXG4gICAgZGVmIGZlYXR1cmVfbWFwKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5mZWF0dXJlcyh4KVxuXG5kZWYgbWF4c29mdG1heF9zY29yZShtb2RlbCwgeCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3QmFzZWxpbmUgT09EOiAxIC0gbWF4IHNvZnRtYXggcHJvYmFiaWxpdHkuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgbW9kZWwuZXZhbCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGxvZ2l0cyA9IG1vZGVsKHgpXG4gICAgICAgIHByb2JzID0gdG9yY2guc29mdG1heChsb2dpdHMsIGRpbT0tMSlcbiAgICByZXR1cm4gMS4wIC0gcHJvYnMubWF4KGRpbT0tMSkudmFsdWVzLm51bXB5KClcblxudG9yY2gubWFudWFsX3NlZWQoMCk7IG5wLnJhbmRvbS5zZWVkKDApXG5uX2NscywgZCA9IDUsIDIwXG5tb2RlbCA9IFNpbXBsZUNsYXNzaWZpZXIoZCwgbl9jbHMpXG5YX2lkICA9IHRvcmNoLnJhbmRuKDEwMCwgZClcblhfb29kID0gdG9yY2gucmFuZG4oMzAsIGQpICogMyArIDVcbnkgPSBucC5hcnJheShbMF0qMTAwICsgWzFdKjMwKVxuWF9hbGwgPSB0b3JjaC5jYXQoW1hfaWQsIFhfb29kXSlcbnNjb3JlcyA9IG1heHNvZnRtYXhfc2NvcmUobW9kZWwsIFhfYWxsKVxucHJpbnQoZlx1MDAyN01heFNvZnRtYXggQVVST0M6IHtyb2NfYXVjX3Njb3JlKHksIHNjb3Jlcyk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN01heFNvZnRtYXggaXMgb3ZlcmNvbmZpZGVudCDigJQgc29mdG1heCBjYW4gYmUgaGlnaCBldmVuIGZvciBPT0QgaW5wdXRzLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPRElOOiBUZW1wZXJhdHVyZSBTY2FsaW5nIGFuZCBJbnB1dCBQZXJ0dXJiYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9ESU4gKExpYW5nIGV0IGFsLiwgMjAxOCkgaW1wcm92ZXMgT09EIHNlcGFyYXRpb24gdmlhIHR3byBvcGVyYXRpb25zIGFwcGxpZWQgdG8gdGhlIHByZXRyYWluZWQgY2xhc3NpZmllci4gVGVtcGVyYXR1cmUgc2NhbGluZzogcmVwbGFjZSBzb2Z0bWF4KGYoeCkvMSkgd2l0aCBzb2Z0bWF4KGYoeCkvVCkgd2hlcmUgVFx1MDAzZTEg4oCUIHRoaXMgYnJvYWRlbnMgdGhlIHNvZnRtYXggZGlzdHJpYnV0aW9uLCBhbXBsaWZ5aW5nIHRoZSBnYXAgYmV0d2VlbiBJRCAoaGlnaCBjb25maWRlbmNlKSBhbmQgT09EIChsb3cgY29uZmlkZW5jZSkgc2NvcmVzLiBJbnB1dCBwZXJ0dXJiYXRpb246IGFkZCBhIHNtYWxsIGFkdmVyc2FyaWFsIHBlcnR1cmJhdGlvbiDOtCBpbiB0aGUgZGlyZWN0aW9uIHRoYXQgaW5jcmVhc2VzIHRoZSBtYXggc29mdG1heCBwcm9iYWJpbGl0eTogeFx1MDAyNyA9IHggKyDOtcK3c2lnbijiiIdfeCBtYXggcF9UKHgpKS4gQm90aCBvcGVyYXRpb25zIGFyZSBwb3N0LWhvYyDigJQgbm8gcmV0cmFpbmluZyBuZWVkZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuXG5kZWYgb2Rpbl9zY29yZShtb2RlbCwgeCwgVD0xMDAuMCwgZXBzPTAuMDAyKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdPRElOOiB0ZW1wZXJhdHVyZSBzY2FsaW5nICsgaW5wdXQgcGVydHVyYmF0aW9uIE9PRCBzY29yZS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBtb2RlbC5ldmFsKClcbiAgICB4X3ZhciA9IHguY2xvbmUoKS5kZXRhY2goKS5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgIGxvZ2l0cyA9IG1vZGVsKHhfdmFyKVxuICAgIG1heF9sb2dpdF9pZHggPSBsb2dpdHMuYXJnbWF4KGRpbT0tMSlcbiAgICAjIElucHV0IHBlcnR1cmJhdGlvbjogbWF4aW1pc2UgY29uZmlkZW5jZSBpbiBwcmVkaWN0ZWQgY2xhc3NcbiAgICBzY29yZV9mb3JfZ3JhZCA9IHRvcmNoLnNvZnRtYXgobG9naXRzIC8gVCwgZGltPS0xKVxuICAgIHNjb3JlX2Zvcl9ncmFkW3JhbmdlKGxlbih4KSksIG1heF9sb2dpdF9pZHhdLnN1bSgpLmJhY2t3YXJkKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgcGVydHVyYmF0aW9uID0gZXBzICogeF92YXIuZ3JhZC5zaWduKClcbiAgICAgICAgeF9wZXJ0dXJiZWQgPSB4X3ZhciArIHBlcnR1cmJhdGlvblxuICAgICAgICBsb2dpdHNfcCA9IG1vZGVsKHhfcGVydHVyYmVkKVxuICAgICAgICBwcm9ic19wID0gdG9yY2guc29mdG1heChsb2dpdHNfcCAvIFQsIGRpbT0tMSlcbiAgICAgICAgb29kX3Njb3JlID0gMS4wIC0gcHJvYnNfcC5tYXgoZGltPS0xKS52YWx1ZXNcbiAgICByZXR1cm4gb29kX3Njb3JlLm51bXB5KClcblxub2Rpbl9zY29yZXMgPSBvZGluX3Njb3JlKG1vZGVsLCBYX2FsbCwgVD0xMDAuMCwgZXBzPTAuMDAyKVxucHJpbnQoZlx1MDAyN09ESU4gQVVST0MgKFQ9MTAwLCBlcHM9MC4wMDIpOiB7cm9jX2F1Y19zY29yZSh5LCBvZGluX3Njb3Jlcyk6LjRmfVx1MDAyNylcbmJhc2Vfc2NvcmVzID0gbWF4c29mdG1heF9zY29yZShtb2RlbCwgWF9hbGwpXG5wcmludChmXHUwMDI3TWF4U29mdG1heCBBVVJPQyBiYXNlbGluZTogICAgIHtyb2NfYXVjX3Njb3JlKHksIGJhc2Vfc2NvcmVzKTouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3T0RJTiBpbXByb3ZlbWVudCBjb21lcyBmcm9tIGNhbGlicmF0aW9uICsgYWR2ZXJzYXJpYWwgYW1wbGlmaWNhdGlvbi5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWFoYWxhbm9iaXMgRGlzdGFuY2UgaW4gRmVhdHVyZSBTcGFjZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGVlIGV0IGFsLiAoMjAxOCkgZml0IGNsYXNzLWNvbmRpdGlvbmFsIEdhdXNzaWFucyBOKM684oKWLCDOoykgaW4gdGhlIHBlbnVsdGltYXRlIGZlYXR1cmUgc3BhY2Ugb2YgdGhlIGNsYXNzaWZpZXIsIHVzaW5nIGEgc2hhcmVkIHRpZWQgY292YXJpYW5jZSDOoyBlc3RpbWF0ZWQgZnJvbSBhbGwgdHJhaW5pbmcgZmVhdHVyZXMuIFRoZSBPT0Qgc2NvcmUgZm9yIGEgdGVzdCBwb2ludCB4IGlzIHRoZSBNYWhhbGFub2JpcyBkaXN0YW5jZSB0byB0aGUgbmVhcmVzdCBjbGFzcyBjZW50cm9pZDogTSh4KSA9IG1pbl9rIChmKHgp4oiSzrzigpYp4bWAIM6j4oG7wrkgKGYoeCniiJLOvOKClikuIFRoaXMgc2NvcmUgY2FwdHVyZXMgcHJveGltaXR5IHRvIHRoZSBsZWFybmVkIGNsYXNzIG1hbmlmb2xkcyBpbiBmZWF0dXJlIHNwYWNlIHJhdGhlciB0aGFuIGluIGlucHV0IHNwYWNlLCBvZnRlbiBvdXRwZXJmb3JtaW5nIGxvZ2l0LWJhc2VkIG1ldGhvZHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuZnJvbSBza2xlYXJuLmNvdmFyaWFuY2UgaW1wb3J0IEVtcGlyaWNhbENvdmFyaWFuY2VcblxuZGVmIGZpdF9tYWhhbGFub2Jpcyhtb2RlbCwgWF90cmFpbiwgeV90cmFpbiwgbl9jbGFzc2VzKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdGaXQgY2xhc3MtY29uZGl0aW9uYWwgR2F1c3NpYW5zIGluIGZlYXR1cmUgc3BhY2UuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgbW9kZWwuZXZhbCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZlYXRzID0gbW9kZWwuZmVhdHVyZV9tYXAoWF90cmFpbikubnVtcHkoKVxuICAgIGNsYXNzX21lYW5zLCBjbGFzc19mZWF0cyA9IFtdLCBbXVxuICAgIGZvciBjIGluIHJhbmdlKG5fY2xhc3Nlcyk6XG4gICAgICAgIGlkeCA9ICh5X3RyYWluID09IGMpXG4gICAgICAgIGNmID0gZmVhdHNbaWR4XVxuICAgICAgICBjbGFzc19tZWFucy5hcHBlbmQoY2YubWVhbihheGlzPTApKVxuICAgICAgICBjbGFzc19mZWF0cy5hcHBlbmQoY2YpXG4gICAgYWxsX2ZlYXRzID0gbnAudnN0YWNrKGNsYXNzX2ZlYXRzKVxuICAgIGNvdiA9IEVtcGlyaWNhbENvdmFyaWFuY2UoKS5maXQoYWxsX2ZlYXRzKVxuICAgIHByZWMgPSBjb3YucHJlY2lzaW9uX1xuICAgIHJldHVybiBucC5hcnJheShjbGFzc19tZWFucyksIHByZWNcblxuZGVmIG1haGFsYW5vYmlzX3Njb3JlKG1vZGVsLCBYX3Rlc3QsIGNsYXNzX21lYW5zLCBwcmVjaXNpb24pOlxuICAgIG1vZGVsLmV2YWwoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmZWF0cyA9IG1vZGVsLmZlYXR1cmVfbWFwKFhfdGVzdCkubnVtcHkoKVxuICAgIHNjb3JlcyA9IG5wLnplcm9zKGxlbihmZWF0cykpXG4gICAgZm9yIGksIGYgaW4gZW51bWVyYXRlKGZlYXRzKTpcbiAgICAgICAgZGlzdHMgPSBbZmxvYXQoKGYgLSBtdSkgQCBwcmVjaXNpb24gQCAoZiAtIG11KSkgZm9yIG11IGluIGNsYXNzX21lYW5zXVxuICAgICAgICBzY29yZXNbaV0gPSBtaW4oZGlzdHMpXG4gICAgcmV0dXJuIHNjb3Jlc1xuXG5uX2NsczIgPSA1XG55X3RyID0gbnAucmFuZG9tLnJhbmRpbnQoMCwgbl9jbHMyLCBzaXplPTEwMClcblhfdHJfdCA9IHRvcmNoLnJhbmRuKDEwMCwgZClcbm11X2FyciwgcHJlY19tYXQgPSBmaXRfbWFoYWxhbm9iaXMobW9kZWwsIFhfdHJfdCwgeV90ciwgbl9jbHMyKVxubWFoX3Njb3JlcyA9IG1haGFsYW5vYmlzX3Njb3JlKG1vZGVsLCBYX2FsbCwgbXVfYXJyLCBwcmVjX21hdClcbnByaW50KGZcdTAwMjdNYWhhbGFub2JpcyBBVVJPQzoge3JvY19hdWNfc2NvcmUoeSwgbWFoX3Njb3Jlcyk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFbmVyZ3kgU2NvcmUgZm9yIE9PRCBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxpdSBldCBhbC4gKDIwMjApIHByb3Bvc2VkIHRoZSBlbmVyZ3kgc2NvcmU6IEUoeDtmKSA9IOKIklTCt2xvZyDOo+KCliBleHAoZuKClih4KS9UKSB3aGVyZSBm4oKWIGFyZSB0aGUgY2xhc3MgbG9naXRzLiBVbmxpa2UgTWF4U29mdG1heCwgdGhlIGVuZXJneSBzY29yZSBpbnRlZ3JhdGVzIGluZm9ybWF0aW9uIGZyb20gYWxsIGNsYXNzIGxvZ2l0cyByYXRoZXIgdGhhbiBqdXN0IHRoZSBtYXhpbXVtIOKAlCBpdCBpcyB0aGUgbG9nLXN1bS1leHAgb2YgbG9naXRzLCByZWxhdGVkIHRvIHRoZSBmcmVlIGVuZXJneSBpbiBzdGF0aXN0aWNhbCBtZWNoYW5pY3MuIFRoZW9yZXRpY2FsbHksIGFsaWduZWQgZW5lcmd5IHNjb3JlcyBjb3JyZXNwb25kIHRvIGxvZyBwKHgpIHVwIHRvIGEgY29uc3RhbnQgd2hlbiB0aGUgbW9kZWwgaXMgY2FsaWJyYXRlZC4gSW4gcHJhY3RpY2UsIGVuZXJneSBzY29yZXMgY29uc2lzdGVudGx5IG91dHBlcmZvcm0gTWF4U29mdG1heCBhbmQgYXJlIGNvbXBldGl0aXZlIHdpdGggTWFoYWxhbm9iaXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuXG5kZWYgZW5lcmd5X3Njb3JlKG1vZGVsLCB4LCBUPTEuMCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3RW5lcmd5IHNjb3JlOiAtVCAqIGxvZ3N1bWV4cChsb2dpdHMgLyBUKS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBtb2RlbC5ldmFsKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgbG9naXRzID0gbW9kZWwoeClcbiAgICAgICAgcmV0dXJuICgtVCAqIHRvcmNoLmxvZ3N1bWV4cChsb2dpdHMgLyBULCBkaW09LTEpKS5udW1weSgpXG5cbmVuZXJneV9zY29yZXMgPSBlbmVyZ3lfc2NvcmUobW9kZWwsIFhfYWxsLCBUPTEuMClcbmJhc2Vfc2NvcmVzICA9IG1heHNvZnRtYXhfc2NvcmUobW9kZWwsIFhfYWxsKVxub2Rpbl9zYyAgICAgID0gb2Rpbl9zY29yZShtb2RlbCwgWF9hbGwsIFQ9MTAwLjAsIGVwcz0wLjAwMilcbm1haF9zYyAgICAgICA9IG1haGFsYW5vYmlzX3Njb3JlKG1vZGVsLCBYX2FsbCwgbXVfYXJyLCBwcmVjX21hdClcblxucHJpbnQoXHUwMDI3T09EIGRldGVjdG9yIGNvbXBhcmlzb24gKGhpZ2hlciBBVVJPQyA9IGJldHRlcik6XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgTWF4U29mdG1heDogICAgICAge3JvY19hdWNfc2NvcmUoeSwgYmFzZV9zY29yZXMpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3ICBPRElOIChUPTEwMCk6ICAgICB7cm9jX2F1Y19zY29yZSh5LCBvZGluX3NjKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgTWFoYWxhbm9iaXM6ICAgICAge3JvY19hdWNfc2NvcmUoeSwgbWFoX3NjKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgRW5lcmd5IChUPTEuMCk6ICAge3JvY19hdWNfc2NvcmUoeSwgZW5lcmd5X3Njb3Jlcyk6LjRmfVx1MDAyNylcbnByaW50KClcbnByaW50KFx1MDAyN0VuZXJneSBzY29yZSBhZHZhbnRhZ2VzOiBubyBmZWF0dXJlIGZpdHRpbmcsIG5vIHBlcnR1cmJhdGlvbiwgc2luZ2xlIGZvcndhcmQgcGFzcy5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT09EIEV2YWx1YXRpb24gYW5kIEJlbmNobWFyayBSZXN1bHRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBldmFsdWF0aW9uIGNvbXBhcmVzIGEgbW9kZWxcdTAwMjdzIGFiaWxpdHkgdG8gc2VwYXJhdGUgSUQgdGVzdCBkYXRhIGZyb20gT09EIHRlc3QgZGF0YSB1c2luZyBBVVJPQyBhbmQgRlBSOTUuIENvbW1vbiBJRCBkYXRhc2V0czogQ0lGQVItMTAsIENJRkFSLTEwMCwgSW1hZ2VOZXQuIENvbW1vbiBPT0QgZGF0YXNldHM6IFNWSE4sIExTVU4sIGlTVU4sIFRleHR1cmVzLiBOZWFyLU9PRCAoc2ltaWxhciBkb21haW4sIGUuZy4sIENJRkFSLTEwIHZzIENJRkFSLTEwMCkgaXMgaGFyZGVyIHRoYW4gZmFyLU9PRCAoZS5nLiwgQ0lGQVItMTAgdnMgU1ZITikuIE1vZGVybiBiYXNlbGluZXMgbGlrZSBWaU0gKFZpcnR1YWwgTWF0Y2hlZCBMb2dpdCkgYW5kIEtOTi1iYXNlZCBtZXRob2RzIGFjaGlldmUgQVVST0NcdTAwM2U5NSUgb24gc3RhbmRhcmQgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZQUjk1IOKAlCB0aGUgZmFsc2UtcG9zaXRpdmUgcmF0ZSB3aGVuIHRoZSB0cnVlLXBvc2l0aXZlIHJhdGUgaXMgZml4ZWQgYXQgOTUlIOKAlCBpcyBvZnRlbiBtb3JlIGluZm9ybWF0aXZlIHRoYW4gQVVST0MgYWxvbmUuIEEgbG93IEFVUk9DIG1vZGVsIG1pZ2h0IHN0aWxsIGJlIGRlcGxveWFibGUgaWYgRlBSOTUgaXMgbG93IChmZXcgZmFsc2UgYWxhcm1zIHdoZW4gY2F0Y2hpbmcgbW9zdCBhbm9tYWxpZXMpLiBDb252ZXJzZWx5LCBhIGhpZ2ggQVVST0MgbW9kZWwgd2l0aCBoaWdoIEZQUjk1IGdlbmVyYXRlcyB0b28gbWFueSBmYWxzZSBhbGFybXMgaW4gcHJvZHVjdGlvbi4gUmVwb3J0IGJvdGggbWV0cmljcyB0b2dldGhlcjsgb3B0aW1pc2UgdGhyZXNob2xkIG9uIGEgdmFsaWRhdGlvbiBzZXQgdG8gbWF0Y2ggb3BlcmF0aW9uYWwgdG9sZXJhbmNlIGZvciBmYWxzZSBwb3NpdGl2ZXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJOZWFyLU9PRDogc2VtYW50aWNhbGx5IHNpbWlsYXIgYnV0IGRpZmZlcmVudCBjbGFzcyAoQ0lGQVItMTAgdnMgQ0lGQVItMTAwKSDigJQgcmVxdWlyZXMgc3Ryb25nIGZlYXR1cmUtc3BhY2UgbWV0aG9kcyBsaWtlIE1haGFsYW5vYmlzIG9yIFZpTS4iLCJGYXItT09EOiB2aXN1YWxseSB2ZXJ5IGRpZmZlcmVudCBkb21haW4gKENJRkFSLTEwIHZzIFNWSE4gZGlnaXRzKSDigJQgTWF4U29mdG1heCBhbHJlYWR5IGFjaGlldmVzIGhpZ2ggQVVST0MuIiwiRlBSOTU6IGxvd2VyIGlzIGJldHRlcjsgdGFyZ2V0IFx1MDAzYzIwJSBmb3IgcHJvZHVjdGlvbiBkZXBsb3ltZW50IHRvIGtlZXAgZmFsc2UtYWxhcm0gcmF0ZSBhY2NlcHRhYmxlLiIsIkFVUk9DOiB0aHJlc2hvbGQtaW5kZXBlbmRlbnQgbWVhc3VyZTsgYSBzY29yZSBvZiAxLjAgbWVhbnMgcGVyZmVjdCBzZXBhcmF0aW9uOyByYW5kb20gYmFzZWxpbmUgPSAwLjUuIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJQb3N0LUhvYyBPT0QgV2l0aG91dCBSZXRyYWluaW5nIiwiY29udGVudCI6IkFsbCBtZXRob2RzIGFib3ZlIChNYXhTb2Z0bWF4LCBPRElOLCBNYWhhbGFub2JpcywgZW5lcmd5IHNjb3JlKSBhcmUgcG9zdC1ob2M6IHRoZXkgdXNlIGEgcHJldHJhaW5lZCBjbGFzc2lmaWVyIHdpdGhvdXQgbW9kaWZpY2F0aW9uLiBGb3IgcHJvZHVjdGlvbiBkZXBsb3ltZW50LCBlbmVyZ3kgc2NvcmUgaXMgdGhlIGVhc2llc3QgdG8gaW1wbGVtZW50IOKAlCBvbmUgbGluZSBvZiBjb2RlIHVzaW5nIGV4aXN0aW5nIGxvZ2l0cy4gTWFoYWxhbm9iaXMgcmVxdWlyZXMgZml0dGluZyBjbGFzcy1jb25kaXRpb25hbCBHYXVzc2lhbnMgKGluZXhwZW5zaXZlKSBidXQgbmVlZHMgYWNjZXNzIHRvIHRyYWluaW5nIHNldCBmZWF0dXJlcy4gT0RJTiByZXF1aXJlcyBncmFkaWVudCBjb21wdXRhdGlvbiBhdCBpbmZlcmVuY2Ugd2hpY2ggYWRkcyBsYXRlbmN5LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJBVVJPQyAobmVhci1PT0QpIiwiQVVST0MgKGZhci1PT0QpIiwiUmVxdWlyZXMgUmV0cmFpbmluZyIsIkZlYXR1cmUgTGF5ZXIiLCJJbmZlcmVuY2UgQ29zdCJdLCJyb3dzIjpbWyJNYXhTb2Z0bWF4IiwiNzDigJM4MCUiLCI4NeKAkzkwJSIsIk5vIiwiTm9uZSAobG9naXRzKSIsIjHDlyBmb3J3YXJkIHBhc3MiXSxbIk9ESU4iLCI4MOKAkzg4JSIsIjky4oCTOTYlIiwiTm8iLCJOb25lIChsb2dpdHMpIiwiMsOXIGZvcndhcmQgKyBncmFkIl0sWyJNYWhhbGFub2JpcyIsIjg14oCTOTIlIiwiOTTigJM5NyUiLCJObyIsIlBlbnVsdGltYXRlIiwiMcOXIGZvcndhcmQgKyBkaXN0YW5jZSJdLFsiRW5lcmd5IFNjb3JlIiwiODPigJM5MCUiLCI5M+KAkzk3JSIsIk5vIiwiTm9uZSAobG9naXRzKSIsIjHDlyBmb3J3YXJkIHBhc3MiXSxbIlZpTSAoVmlydHVhbCBNYXRjaGVkKSIsIjkw4oCTOTUlIiwiOTbigJM5OSUiLCJObyIsIlBlbnVsdGltYXRlIiwiMcOXIGZvcndhcmQgKyBwcm9qZWN0aW9uIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIHByYWN0aWNlOiBzdGFydCB3aXRoIHRoZSBlbmVyZ3kgc2NvcmUgYXMgaXQgcmVxdWlyZXMgbm8gYWRkaXRpb25hbCBmaXR0aW5nIGFuZCBpcyBvbmUgbGluZSBvZiBjb2RlLiBJZiBwZXJmb3JtYW5jZSBpcyBpbnN1ZmZpY2llbnQsIGFkZCB0aGUgTWFoYWxhbm9iaXMgZGlzdGFuY2UgYXMgYSBjb21wbGVtZW50YXJ5IHNjb3JlIOKAlCBib3RoIGNhbiBiZSBsaW5lYXJseSBjb21iaW5lZC4gVXNlIE9ESU4gd2hlbiB5b3UgaGF2ZSB0aW1lIGJ1ZGdldCBmb3IgZ3JhZGllbnQgY29tcHV0YXRpb24gYW5kIG5lZWQgdG8gbWF4aW1pc2UgQVVST0Mgb24gbmVhci1PT0QgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# OOD Detection — Energy Score, Mahalanobis, and MaxSoftmax

Out-of-distribution (OOD) detection asks: given a model trained on in-distribution (ID) data, can we detect inputs from a different distribution at test time without retraining? Unlike anomaly detection in unsupervised settings, OOD detection exploits the structure of a pretrained classifier — its softmax outputs, internal feature representations, and logits — to derive a separation score. The key challenge is that neural networks are often overconfident on OOD inputs.

- MaxSoftmax (Hendrycks & Gimpel 2017): simplest baseline — max class probability is low for OOD; works poorly due to overconfidence.
- ODIN (Liang et al. 2018): temperature scaling + adversarial perturbation; large AUROC improvement over MaxSoftmax.
- Mahalanobis (Lee et al. 2018): class-conditional Gaussians in feature space; strongest feature-based post-hoc method.
- Energy score (Liu et al. 2020): −T·log Σ exp(fₖ/T); theoretically grounded and easy to compute.
- ViM (Wang et al. 2022): virtual-matched logits via null-space projection; top performer on ImageNet-scale benchmarks.

## In-Distribution vs Out-of-Distribution

A model trained on CIFAR-10 (natural images) sees semantically different inputs at deployment: medical images, satellite images, adversarial examples. OOD detection must flag these before the model makes a dangerously confident wrong prediction. Evaluation uses two metrics: AUROC (area under the ROC curve for ID vs OOD binary classification) and FPR95 (false-positive rate when TPR=95%). The benchmark involves the model predicting ID correctly on its test set while being exposed to a separate OOD dataset.

```python
import torch
import torch.nn as nn
import numpy as np
from sklearn.metrics import roc_auc_score

class SimpleClassifier(nn.Module):
    def __init__(self, d_in, n_classes):
        super().__init__()
        self.features = nn.Sequential(
            nn.Linear(d_in, 128), nn.ReLU(),
            nn.Linear(128, 64), nn.ReLU())
        self.head = nn.Linear(64, n_classes)
    def forward(self, x):
        return self.head(self.features(x))
    def feature_map(self, x):
        return self.features(x)

def maxsoftmax_score(model, x):
    '''Baseline OOD: 1 - max softmax probability.'''
    model.eval()
    with torch.no_grad():
        logits = model(x)
        probs = torch.softmax(logits, dim=-1)
    return 1.0 - probs.max(dim=-1).values.numpy()

torch.manual_seed(0); np.random.seed(0)
n_cls, d = 5, 20
model = SimpleClassifier(d, n_cls)
X_id  = torch.randn(100, d)
X_ood = torch.randn(30, d) * 3 + 5
y = np.array([0]*100 + [1]*30)
X_all = torch.cat([X_id, X_ood])
scores = maxsoftmax_score(model, X_all)
print(f'MaxSoftmax AUROC: {roc_auc_score(y, scores):.4f}')
print('MaxSoftmax is overconfident — softmax can be high even for OOD inputs.')
```

## ODIN: Temperature Scaling and Input Perturbation

ODIN (Liang et al., 2018) improves OOD separation via two operations applied to the pretrained classifier. Temperature scaling: replace softmax(f(x)/1) with softmax(f(x)/T) where T>1 — this broadens the softmax distribution, amplifying the gap between ID (high confidence) and OOD (low confidence) scores. Input perturbation: add a small adversarial perturbation δ in the direction that increases the max softmax probability: x' = x + ε·sign(∇_x max p_T(x)). Both operations are post-hoc — no retraining needed.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score

def odin_score(model, x, T=100.0, eps=0.002):
    '''ODIN: temperature scaling + input perturbation OOD score.'''
    model.eval()
    x_var = x.clone().detach().requires_grad_(True)
    logits = model(x_var)
    max_logit_idx = logits.argmax(dim=-1)
    # Input perturbation: maximise confidence in predicted class
    score_for_grad = torch.softmax(logits / T, dim=-1)
    score_for_grad[range(len(x)), max_logit_idx].sum().backward()
    with torch.no_grad():
        perturbation = eps * x_var.grad.sign()
        x_perturbed = x_var + perturbation
        logits_p = model(x_perturbed)
        probs_p = torch.softmax(logits_p / T, dim=-1)
        ood_score = 1.0 - probs_p.max(dim=-1).values
    return ood_score.numpy()

odin_scores = odin_score(model, X_all, T=100.0, eps=0.002)
print(f'ODIN AUROC (T=100, eps=0.002): {roc_auc_score(y, odin_scores):.4f}')
base_scores = maxsoftmax_score(model, X_all)
print(f'MaxSoftmax AUROC baseline:     {roc_auc_score(y, base_scores):.4f}')
print('ODIN improvement comes from calibration + adversarial amplification.')
```

## Mahalanobis Distance in Feature Space

Lee et al. (2018) fit class-conditional Gaussians N(μₖ, Σ) in the penultimate feature space of the classifier, using a shared tied covariance Σ estimated from all training features. The OOD score for a test point x is the Mahalanobis distance to the nearest class centroid: M(x) = min_k (f(x)−μₖ)ᵀ Σ⁻¹ (f(x)−μₖ). This score captures proximity to the learned class manifolds in feature space rather than in input space, often outperforming logit-based methods.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.covariance import EmpiricalCovariance

def fit_mahalanobis(model, X_train, y_train, n_classes):
    '''Fit class-conditional Gaussians in feature space.'''
    model.eval()
    with torch.no_grad():
        feats = model.feature_map(X_train).numpy()
    class_means, class_feats = [], []
    for c in range(n_classes):
        idx = (y_train == c)
        cf = feats[idx]
        class_means.append(cf.mean(axis=0))
        class_feats.append(cf)
    all_feats = np.vstack(class_feats)
    cov = EmpiricalCovariance().fit(all_feats)
    prec = cov.precision_
    return np.array(class_means), prec

def mahalanobis_score(model, X_test, class_means, precision):
    model.eval()
    with torch.no_grad():
        feats = model.feature_map(X_test).numpy()
    scores = np.zeros(len(feats))
    for i, f in enumerate(feats):
        dists = [float((f - mu) @ precision @ (f - mu)) for mu in class_means]
        scores[i] = min(dists)
    return scores

n_cls2 = 5
y_tr = np.random.randint(0, n_cls2, size=100)
X_tr_t = torch.randn(100, d)
mu_arr, prec_mat = fit_mahalanobis(model, X_tr_t, y_tr, n_cls2)
mah_scores = mahalanobis_score(model, X_all, mu_arr, prec_mat)
print(f'Mahalanobis AUROC: {roc_auc_score(y, mah_scores):.4f}')
```

## Energy Score for OOD Detection

Liu et al. (2020) proposed the energy score: E(x;f) = −T·log Σₖ exp(fₖ(x)/T) where fₖ are the class logits. Unlike MaxSoftmax, the energy score integrates information from all class logits rather than just the maximum — it is the log-sum-exp of logits, related to the free energy in statistical mechanics. Theoretically, aligned energy scores correspond to log p(x) up to a constant when the model is calibrated. In practice, energy scores consistently outperform MaxSoftmax and are competitive with Mahalanobis.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score

def energy_score(model, x, T=1.0):
    '''Energy score: -T * logsumexp(logits / T).'''
    model.eval()
    with torch.no_grad():
        logits = model(x)
        return (-T * torch.logsumexp(logits / T, dim=-1)).numpy()

energy_scores = energy_score(model, X_all, T=1.0)
base_scores  = maxsoftmax_score(model, X_all)
odin_sc      = odin_score(model, X_all, T=100.0, eps=0.002)
mah_sc       = mahalanobis_score(model, X_all, mu_arr, prec_mat)

print('OOD detector comparison (higher AUROC = better):')
print(f'  MaxSoftmax:       {roc_auc_score(y, base_scores):.4f}')
print(f'  ODIN (T=100):     {roc_auc_score(y, odin_sc):.4f}')
print(f'  Mahalanobis:      {roc_auc_score(y, mah_sc):.4f}')
print(f'  Energy (T=1.0):   {roc_auc_score(y, energy_scores):.4f}')
print()
print('Energy score advantages: no feature fitting, no perturbation, single forward pass.')
```

## OOD Evaluation and Benchmark Results

Standard evaluation compares a model's ability to separate ID test data from OOD test data using AUROC and FPR95. Common ID datasets: CIFAR-10, CIFAR-100, ImageNet. Common OOD datasets: SVHN, LSUN, iSUN, Textures. Near-OOD (similar domain, e.g., CIFAR-10 vs CIFAR-100) is harder than far-OOD (e.g., CIFAR-10 vs SVHN). Modern baselines like ViM (Virtual Matched Logit) and KNN-based methods achieve AUROC>95% on standard benchmarks.

FPR95 — the false-positive rate when the true-positive rate is fixed at 95% — is often more informative than AUROC alone. A low AUROC model might still be deployable if FPR95 is low (few false alarms when catching most anomalies). Conversely, a high AUROC model with high FPR95 generates too many false alarms in production. Report both metrics together; optimise threshold on a validation set to match operational tolerance for false positives.

- Near-OOD: semantically similar but different class (CIFAR-10 vs CIFAR-100) — requires strong feature-space methods like Mahalanobis or ViM.
- Far-OOD: visually very different domain (CIFAR-10 vs SVHN digits) — MaxSoftmax already achieves high AUROC.
- FPR95: lower is better; target <20% for production deployment to keep false-alarm rate acceptable.
- AUROC: threshold-independent measure; a score of 1.0 means perfect separation; random baseline = 0.5.

> **Post-Hoc OOD Without Retraining**: All methods above (MaxSoftmax, ODIN, Mahalanobis, energy score) are post-hoc: they use a pretrained classifier without modification. For production deployment, energy score is the easiest to implement — one line of code using existing logits. Mahalanobis requires fitting class-conditional Gaussians (inexpensive) but needs access to training set features. ODIN requires gradient computation at inference which adds latency.

| Method | AUROC (near-OOD) | AUROC (far-OOD) | Requires Retraining | Feature Layer | Inference Cost |
| --- | --- | --- | --- | --- | --- |
| MaxSoftmax | 70–80% | 85–90% | No | None (logits) | 1× forward pass |
| ODIN | 80–88% | 92–96% | No | None (logits) | 2× forward + grad |
| Mahalanobis | 85–92% | 94–97% | No | Penultimate | 1× forward + distance |
| Energy Score | 83–90% | 93–97% | No | None (logits) | 1× forward pass |
| ViM (Virtual Matched) | 90–95% | 96–99% | No | Penultimate | 1× forward + projection |

In practice: start with the energy score as it requires no additional fitting and is one line of code. If performance is insufficient, add the Mahalanobis distance as a complementary score — both can be linearly combined. Use ODIN when you have time budget for gradient computation and need to maximise AUROC on near-OOD benchmarks.

---

