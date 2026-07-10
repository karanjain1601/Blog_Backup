---
title: "Why Multiple Attention Heads — Different Subspace Specialisation"
slug: "why-multiple-attention-heads"
description: "Examine single-head limitations, the subspace specialisation argument, Clark et al. 2019 empirical evidence, gradient-based head importance scoring, and head pruning experiments."
tags: ["deep-learning", "transformers", "attention"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBUcmFuc2Zvcm1lciB3aXRoIGEgc2luZ2xlIGF0dGVudGlvbiBoZWFkIHBlciBsYXllciBsZWFybnMgb25lIGdsb2JhbCBhdHRlbnRpb24gcGF0dGVybiBwZXIgbGF5ZXIg4oCUIGEgc2luZ2xlIGxlYXJuZWQgc2ltaWxhcml0eSBmdW5jdGlvbiBhcHBsaWVkIHVuaWZvcm1seSB0byBhbGwgcXVlcmllcy4gTXVsdGlwbGUgaGVhZHMgYWxsb3cgdGhlIG1vZGVsIHRvIHNpbXVsdGFuZW91c2x5IHJvdXRlIGluZm9ybWF0aW9uIHRocm91Z2ggaCBkaWZmZXJlbnQgbGVhcm5lZCByb3V0aW5nIGZ1bmN0aW9ucywgZWFjaCBvcGVyYXRpbmcgb24gYSBkaWZmZXJlbnQgbGluZWFyIHByb2plY3Rpb24gb2YgdGhlIHNhbWUgaW5wdXQuIFRoaXMgaXMgbm90IG1lcmVseSByZWR1bmRhbmN5OiBkaWZmZXJlbnQgaGVhZHMgdGVuZCB0byBzcGVjaWFsaXNlIG9uIHN5bnRhY3RpYyBkZXBlbmRlbmNpZXMsIGNvcmVmZXJlbmNlLCBwb3NpdGlvbmFsIHN0cnVjdHVyZSwgYW5kIHNlbWFudGljIHNpbWlsYXJpdHkgc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2luZ2xlLUhlYWQgTGltaXRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aCBhIHNpbmdsZSBhdHRlbnRpb24gaGVhZCBvZiBkaW1lbnNpb24gZF9tb2RlbCwgZXZlcnkgcG9zaXRpb24gY29tcHV0ZXMgYSBzaW5nbGUgcXVlcnkgYW5kIGNvbXBhcmVzIGl0IHRvIGEgc2luZ2xlIHNldCBvZiBrZXlzLiBUaGUgb3V0cHV0IGlzIG9uZSB3ZWlnaHRlZCBjb21iaW5hdGlvbiBvZiB2YWx1ZSB2ZWN0b3JzIOKAlCBhIHJhbmstMSByb3V0aW5nLiBJZiB0aGUgdGFzayByZXF1aXJlcyBzaW11bHRhbmVvdXNseSBhdHRlbmRpbmcgdG8gbXVsdGlwbGUgdW5yZWxhdGVkIHBvc2l0aW9ucyAoZS5nLiwgdGhlIHN1YmplY3Qgb2YgYSBzZW50ZW5jZSBhbmQgYSBkaXN0YW50IHByb25vdW4gdGhhdCByZWZlcnMgdG8gaXQpLCBhIHNpbmdsZSBoZWFkIG11c3QgdHJhZGUgb2ZmIGJldHdlZW4gdGhlbSwgYWNoaWV2aW5nIG5laXRoZXIgcmVsaWFibHkuIE11bHRpcGxlIGhlYWRzIGNpcmN1bXZlbnQgdGhpcyBieSBwYXJ0aXRpb25pbmcgdGhlIGNhcGFjaXR5IOKAlCBoZWFkIDEgY2FuIGF0dGVuZCB0byBzeW50YWN0aWMgZGVwZW5kZW5jaWVzIHdoaWxlIGhlYWQgMiBoYW5kbGVzIGNvcmVmZXJlbmNlIHdpdGhvdXQgZWl0aGVyIGludGVyZmVyaW5nIHdpdGggdGhlIG90aGVyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1hdGhlbWF0aWNhbCBKdXN0aWZpY2F0aW9uIOKAlCBTdWJzcGFjZSBSZXByZXNlbnRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHByb2plY3Rpb24gbWF0cmljZXMgV+G1olEgYW5kIFfhtaJLIG1hcCB0aGUgZnVsbCBkX21vZGVsLWRpbWVuc2lvbmFsIGlucHV0IGludG8gYSBk4oKWLWRpbWVuc2lvbmFsIHN1YnNwYWNlLiBEaWZmZXJlbnQgaGVhZHMgcHJvamVjdCBpbnRvIGRpZmZlcmVudCBzdWJzcGFjZXMsIHNvIHRoZXkgbWVhc3VyZSBzaW1pbGFyaXR5IGFsb25nIGRpZmZlcmVudCBkaXJlY3Rpb25zLiBGb3JtYWxseSwgaCBoZWFkcyBwcm9kdWNlIGggaW5kZXBlbmRlbnQgYXR0ZW50aW9uLXdlaWdodGVkIHN1bXMgb2YgdmFsdWUgcHJvamVjdGlvbnM7IGNvbmNhdGVuYXRpbmcgdGhlbSBiZWZvcmUgV+G0vCBhbGxvd3MgdGhlIG91dHB1dCBwcm9qZWN0aW9uIHRvIG1peCBpbmZvcm1hdGlvbiBmcm9tIGFsbCBoIHN1YnNwYWNlcy4gVGhlIHJhbmsgb2YgdGhlIGNvbWJpbmVkIG91dHB1dCBpcyBib3VuZGVkIGJ5IG1pbihowrdkdiwgZF9tb2RlbCkg4oCUIHBvdGVudGlhbGx5IGZhciBoaWdoZXIgdGhhbiB0aGUgcmFuayBhY2hpZXZhYmxlIHdpdGggYSBzaW5nbGUgaGVhZCBvZiBkaW1lbnNpb24gZF9tb2RlbC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN1cGVycG9zaXRpb24gdGhlb3J5IChFbGhhZ2UgZXQgYWwuIDIwMjIpIHByb3ZpZGVzIGEgY29tcGxlbWVudGFyeSB2aWV3OiB3aXRoIGVub3VnaCBoZWFkcywgYSBUcmFuc2Zvcm1lciBsYXllciBjYW4gc3RvcmUgYW5kIHJldHJpZXZlIG11bHRpcGxlIGFwcHJveGltYXRlbHktb3J0aG9nb25hbCBcdTAwMjdmZWF0dXJlc1x1MDAyNyBzaW11bHRhbmVvdXNseS4gRWFjaCBoZWFkIGFjdHMgb24gYSBkaWZmZXJlbnQgc3Vic3BhY2UgaW4gd2hpY2ggZGlzdGluY3QgZmVhdHVyZXMgYXJlIG5lYXJseSBvcnRob2dvbmFsOyBpbnRlcmZlcmVuY2UgYmV0d2VlbiBmZWF0dXJlcyBpcyBzdXBwcmVzc2VkIGFjcm9zcyBoZWFkcyBldmVuIHdoZW4gaXQgY2Fubm90IGJlIGF2b2lkZWQgd2l0aGluIGEgc2luZ2xlIGhlYWQuIFRoaXMgYWxsb3dzIHRoZSBtb2RlbCB0byBtYWludGFpbiBtb3JlIGluZGVwZW5kZW50IFx1MDAyN3Rob3VnaHRzXHUwMDI3IHBlciBsYXllciB0aGFuIGl0cyByYXcgZGltZW5zaW9uIHdvdWxkIHN1Z2dlc3QuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5kX21vZGVsLCBoID0gMjU2LCA4XG5taGEgPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oZF9tb2RlbCwgaCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbldRLCBXSywgXyA9IG1oYS5pbl9wcm9qX3dlaWdodC5jaHVuaygzLCBkaW09MClcbmRrID0gZF9tb2RlbCAvLyBoXG5cbnRva2VucyA9IFtcdTAwMjdbQ0xTXVx1MDAyNywgXHUwMDI3dGhlXHUwMDI3LCBcdTAwMjdjYXRcdTAwMjcsIFx1MDAyN3NhdFx1MDAyNywgXHUwMDI3b25cdTAwMjcsIFx1MDAyN21hdFx1MDAyNywgXHUwMDI3W1NFUF1cdTAwMjcsIFx1MDAyNy5cdTAwMjddXG5zZXFfbGVuID0gbGVuKHRva2VucylcbnggPSB0b3JjaC5yYW5kbigxLCBzZXFfbGVuLCBkX21vZGVsKVxueF9mbGF0ID0geC5zcXVlZXplKDApXG5cbmRlZiBoZWFkX2F0dG4oeF9mbGF0LCBpKTpcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgUSA9ICh4X2ZsYXQgQCBXUS5UKVs6LCBpKmRrOihpKzEpKmRrXVxuICAgICAgICBLID0gKHhfZmxhdCBAIFdLLlQpWzosIGkqZGs6KGkrMSkqZGtdXG4gICAgICAgIFMgPSAoUSBAIEsuVCAvIGRrKiowLjUpLm51bXB5KClcbiAgICBTIC09IFMubWF4KDEsIGtlZXBkaW1zPVRydWUpXG4gICAgQSA9IG5wLmV4cChTKTsgQSAvPSBBLnN1bSgxLCBrZWVwZGltcz1UcnVlKVxuICAgIHJldHVybiBBXG5cbnByaW50KFx1MDAyN0hlYWQgfCBcdTAwMjcgKyBcdTAwMjcgfCBcdTAwMjcuam9pbihcdTAwMjd7Olx1MDAzZTV9XHUwMDI3LmZvcm1hdCh0Wzo1XSkgZm9yIHQgaW4gdG9rZW5zKSlcbnByaW50KFx1MDAyNy1cdTAwMjcgKiAoNyArIDggKiBzZXFfbGVuKSlcbmZvciBpIGluIHJhbmdlKGgpOlxuICAgIEEgPSBoZWFkX2F0dG4oeF9mbGF0LCBpKVxuICAgIHBlYWtzID0gW3Rva2Vuc1tqXVs6NV0gZm9yIGogaW4gQS5hcmdtYXgoYXhpcz0xKV1cbiAgICBlbnQgPSAtKEEgKiBucC5sb2coQSArIDFlLTkpKS5zdW0oMSkubWVhbigpXG4gICAgcm93ID0gXHUwMDI3IHwgXHUwMDI3LmpvaW4oXHUwMDI3ezpcdTAwM2U1fVx1MDAyNy5mb3JtYXQocCkgZm9yIHAgaW4gcGVha3MpXG4gICAgcHJpbnQoXHUwMDI3SHs6XHUwMDNlMn0gIHwge30gIGVudD17Oi4yZn1cdTAwMjcuZm9ybWF0KGksIHJvdywgZW50KSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFbXBpcmljYWwgRXZpZGVuY2Ug4oCUIENsYXJrIGV0IGFsLiAyMDE5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFyayBldCBhbC4gKDIwMTkpIHN5c3RlbWF0aWNhbGx5IGFuYWx5c2VkIGF0dGVudGlvbiBwYXR0ZXJucyBhY3Jvc3MgYWxsIDE0NCBoZWFkcyBpbiBCRVJULWJhc2UuIFRoZXkgZm91bmQgY2xlYXIgZnVuY3Rpb25hbCBzcGVjaWFsaXNhdGlvbjogY2VydGFpbiBoZWFkcyB0cmFjayBkaXJlY3Qgb2JqZWN0IHJlbGF0aW9uc2hpcHMsIG90aGVycyBhdHRlbmQgdG8gY29yZWZlcmVudCBtZW50aW9ucywgYW5kIGEgZGlzdGluY3QgY2xhc3MgYXR0ZW5kcyB0byB0aGUgaW1tZWRpYXRlbHkgcHJlY2VkaW5nIG9yIGZvbGxvd2luZyB0b2tlbi4gQ3J1Y2lhbGx5LCBzb21lIGhlYWRzIGNhcHR1cmUgaW5mb3JtYXRpb24gaGlnaGx5IGNvcnJlbGF0ZWQgd2l0aCB0aGUgb3V0cHV0IG9mIHN1cGVydmlzZWQgZGVwZW5kZW5jeSBwYXJzZXJzIOKAlCB3aXRob3V0IGFueSBleHBsaWNpdCBzdXBlcnZpc2lvbiBvbiBzeW50YXguIFRoaXMgcHJvdmlkZXMgc3Ryb25nIGVtcGlyaWNhbCBldmlkZW5jZSB0aGF0IG11bHRpLWhlYWQgYXR0ZW50aW9uIHNwb250YW5lb3VzbHkgbGVhcm5zIGRpdmVyc2UsIGxpbmd1aXN0aWNhbGx5IG1lYW5pbmdmdWwgcm91dGluZyBmdW5jdGlvbnMgYWNyb3NzIGhlYWRzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiQ2xhcmsgZXQgYWwuIDIwMTkgS2V5IEZpbmRpbmdzIiwiY29udGVudCI6IkluIEJFUlQtYmFzZSAoMTIgbGF5ZXJzIMOXIDEyIGhlYWRzID0gMTQ0IGhlYWRzIHRvdGFsKTogKDEpIEhlYWRzIGluIGxheWVycyA24oCTMTAgc2hvdyB0aGUgc3Ryb25nZXN0IHN5bnRhY3RpYyBiZWhhdmlvdXIuICgyKSBBIHNpbmdsZSBoZWFkIGluIGxheWVyIDggYWNoaWV2ZXMgNzYuMSUgYWNjdXJhY3kgb24gYSBjb3JlZmVyZW5jZSB0YXNrIHdpdGggbm8gZmluZS10dW5pbmcuICgzKSBDZXJ0YWluIGhlYWRzIGF0dGVuZCBhbG1vc3QgZXhjbHVzaXZlbHkgdG8gW1NFUF0gb3IgW0NMU10gdG9rZW5zIOKAlCBhY3RpbmcgYXMgXHUwMDI3bm8tb3BcdTAwMjcgYXR0ZW50aW9uIHNpbmtzLiAoNCkgUmVtb3ZpbmcgYW55IHNpbmdsZSBoZWFkIGNhdXNlcyBcdTAwM2MxJSBwZXJmb3JtYW5jZSBkcm9wOyByZW1vdmluZyB0aGUgdG9wLTUgbW9zdCBpbXBvcnRhbnQgaGVhZHMgY2F1c2VzIH4zJSBkcm9wLiBBdHRlbnRpb24gcGF0dGVybnMgYXJlIHNwYXJzZSBhbmQgaW50ZXJwcmV0YWJsZSBhdCB0aGUgaGVhZCBsZXZlbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxudG9yY2gubWFudWFsX3NlZWQoNylcbmRfbW9kZWwsIGgsIHNlcV9sZW4sIGJhdGNoID0gMTI4LCA4LCAyMCwgMTZcblxuY2xhc3MgVGlueVRyYW5zZm9ybWVyTGF5ZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmF0dG4gPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oZF9tb2RlbCwgaCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5ub3JtID0gbm4uTGF5ZXJOb3JtKGRfbW9kZWwpXG4gICAgICAgIHNlbGYucHJvaiA9IG5uLkxpbmVhcihkX21vZGVsLCAxKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGEsIF8gPSBzZWxmLmF0dG4oeCwgeCwgeClcbiAgICAgICAgeCA9IHNlbGYubm9ybSh4ICsgYSlcbiAgICAgICAgcmV0dXJuIHNlbGYucHJvaih4Lm1lYW4oZGltPTEpKVxuXG5tb2RlbCA9IFRpbnlUcmFuc2Zvcm1lckxheWVyKClcbnggPSB0b3JjaC5yYW5kbihiYXRjaCwgc2VxX2xlbiwgZF9tb2RlbClcbnkgPSB4Lm1lYW4oZGltPSgxLCAyKSkudW5zcXVlZXplKC0xKVxubG9zcyA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MobW9kZWwoeCksIHkpXG5sb3NzLmJhY2t3YXJkKClcblxuV1FfZywgV0tfZywgV1ZfZyA9IG1vZGVsLmF0dG4uaW5fcHJval93ZWlnaHQuZ3JhZC5jaHVuaygzLCBkaW09MClcbmRrID0gZF9tb2RlbCAvLyBoXG5wcmludChcdTAwMjd7Olx1MDAzZTZ9IHs6XHUwMDNlMTB9IHs6XHUwMDNlMTB9IHs6XHUwMDNlMTB9IHs6XHUwMDNlMTJ9XHUwMDI3LmZvcm1hdChcdTAwMjdIZWFkXHUwMDI3LCBcdTAwMjdRX2dyYWRcdTAwMjcsIFx1MDAyN0tfZ3JhZFx1MDAyNywgXHUwMDI3Vl9ncmFkXHUwMDI3LCBcdTAwMjdJbXBvcnRhbmNlXHUwMDI3KSlcbmZvciBpIGluIHJhbmdlKGgpOlxuICAgIHFnID0gV1FfZ1tpKmRrOihpKzEpKmRrXS5ub3JtKCkuaXRlbSgpXG4gICAga2cgPSBXS19nW2kqZGs6KGkrMSkqZGtdLm5vcm0oKS5pdGVtKClcbiAgICB2ZyA9IFdWX2dbaSpkazooaSsxKSpka10ubm9ybSgpLml0ZW0oKVxuICAgIGltcCA9IChxZyArIGtnICsgdmcpIC8gM1xuICAgIHByaW50KFx1MDAyN3s6XHUwMDNlNn0gezpcdTAwM2UxMC40Zn0gezpcdTAwM2UxMC40Zn0gezpcdTAwM2UxMC40Zn0gezpcdTAwM2UxMi40Zn1cdTAwMjcuZm9ybWF0KGksIHFnLCBrZywgdmcsIGltcCkpXG5wcmludChcdTAwMjdIaWdoZXIgZ3JhZGllbnQgbm9ybSAtXHUwMDNlIGhlYWQgY29udHJpYnV0ZXMgbW9yZSB0byB0aGlzIHRhc2suXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhlYWQgUHJ1bmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWljaGVsIGV0IGFsLiAoMjAxOSkgc2hvd2VkIHRoYXQgbW9zdCBhdHRlbnRpb24gaGVhZHMgaW4gQkVSVCBjYW4gYmUgcHJ1bmVkIGF0IHRlc3QgdGltZSB3aXRoIG1pbmltYWwgYWNjdXJhY3kgbG9zcyDigJQgZm9yIEJFUlQtYmFzZSBvbiBNTkxJLCBvbmx5IDE2IG9mIDE0NCBoZWFkcyBhcmUgbmVlZGVkIHRvIHJldGFpbiA5MCUgb2YgcGVyZm9ybWFuY2UuIFZvaXRhIGV0IGFsLiAoMjAxOSkgaWRlbnRpZmllZCBmb3VyIGhlYWQgcm9sZXMgdGhhdCBhcmUgY29uc2lzdGVudGx5IHByZXNlcnZlZDogcG9zaXRpb25hbCAoYXR0ZW5kIHRvIGFkamFjZW50IHRva2VuKSwgc3ludGFjdGljIChhdHRlbmQgdG8gc3ludGFjdGljIGRlcGVuZGVudHMpLCByYXJlLXdvcmQgKGF0dGVuZCB0byBsb3ctZnJlcXVlbmN5IHRva2VucyksIGFuZCBjb3JlZmVyZW5jZS4gVW5pbXBvcnRhbnQgaGVhZHMg4oCUIHRob3NlIHdob3NlIHJlbW92YWwgY2F1c2VzIHRoZSBzbWFsbGVzdCBhY2N1cmFjeSBkcm9wIOKAlCBjYW4gYmUgemVyb2VkIG91dCBieSBzZXR0aW5nIHRoZSBjb3JyZXNwb25kaW5nIGNvbHVtbnMgb2YgV+G0vCB0byB6ZXJvLCB3aGljaCBpcyBlcXVpdmFsZW50IHRvIHJlbW92aW5nIHRoZWlyIGNvbnRyaWJ1dGlvbiB0byB0aGUgb3V0cHV0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5kX21vZGVsLCBoLCBuID0gMTI4LCA4LCAxNVxuXG5taGEgPSBubi5NdWx0aWhlYWRBdHRlbnRpb24oZF9tb2RlbCwgaCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbnggPSB0b3JjaC5yYW5kbig0LCBuLCBkX21vZGVsKVxuXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBiYXNlbGluZSwgXyA9IG1oYSh4LCB4LCB4KVxuXG4jIENvbXB1dGUgcGVyLWhlYWQgaW1wb3J0YW5jZTogZ3JhZGllbnQgb2Ygb3V0cHV0IEwyIG5vcm0gdy5yLnQuIFdWIHNsaWNlXG5pbXBvcnRhbmNlcyA9IFtdXG5mb3IgaSBpbiByYW5nZShoKTpcbiAgICB4X3JlcSA9IHguY2xvbmUoKS5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgIG91dCwgXyA9IG1oYSh4X3JlcSwgeF9yZXEsIHhfcmVxKVxuICAgIG91dC5ub3JtKCkuYmFja3dhcmQoKVxuICAgIFdRX2csIFdLX2csIFdWX2cgPSBtaGEuaW5fcHJval93ZWlnaHQuZ3JhZC5jaHVuaygzLCBkaW09MCkgaWYgbWhhLmluX3Byb2pfd2VpZ2h0LmdyYWQgaXMgbm90IE5vbmUgZWxzZSAodG9yY2guemVyb3MoZF9tb2RlbCxkX21vZGVsKSwpKjNcbiAgICBkayA9IGRfbW9kZWwgLy8gaFxuICAgIGltcG9ydGFuY2VzLmFwcGVuZChmbG9hdChXVl9nW2kqZGs6KGkrMSkqZGtdLm5vcm0oKSkgaWYgV1ZfZyBpcyBub3QgTm9uZSBlbHNlIDAuMClcbiAgICBtaGEuemVyb19ncmFkKClcblxuaW1wb3J0YW5jZXMgPSBucC5hcnJheShpbXBvcnRhbmNlcylcbnJhbmtlZCA9IG5wLmFyZ3NvcnQoaW1wb3J0YW5jZXMpXG5wcmludChcdTAwMjdIZWFkIGltcG9ydGFuY2UgcmFua2luZyAobGVhc3QgdG8gbW9zdCk6XHUwMDI3LCByYW5rZWQudG9saXN0KCkpXG5wcmludChcdTAwMjdMZWFzdCBpbXBvcnRhbnQgaGVhZCAocHJ1bmUgZmlyc3QpOiBoZWFkXHUwMDI3LCByYW5rZWRbMF0pXG5cbiMgWmVybyBvdXQgdGhlIGxlYXN0IGltcG9ydGFudCBoZWFkIGluIFdPXG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBkayA9IGRfbW9kZWwgLy8gaFxuICAgIG1oYS5vdXRfcHJvai53ZWlnaHRbOiwgcmFua2VkWzBdKmRrOihyYW5rZWRbMF0rMSkqZGtdID0gMFxuICAgIHBydW5lZCwgXyA9IG1oYSh4LCB4LCB4KVxuXG5kaWZmID0gKGJhc2VsaW5lIC0gcHJ1bmVkKS5hYnMoKS5tZWFuKCkuaXRlbSgpXG5wcmludChcdTAwMjdPdXRwdXQgY2hhbmdlIGFmdGVyIHBydW5pbmcgaGVhZCB7fTogezouNGZ9XHUwMDI3LmZvcm1hdChyYW5rZWRbMF0sIGRpZmYpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNpbmdsZS1IZWFkIHZzIE11bHRpLUhlYWQgVGFzayBDb21wYXJpc29uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHNpbmdsZSBhdHRlbnRpb24gaGVhZCBjYW4gcmVwcmVzZW50IGF0IG1vc3Qgb25lIHJvdXRpbmcgcGF0dGVybiBwZXIgbGF5ZXIg4oCUIGl0IGlzIGxpbWl0ZWQgdG8gYSByYW5rLTEgd2VpZ2h0aW5nIG9mIHZhbHVlIHZlY3RvcnMgZnJvbSBhIHNpbmdsZSBzdWJzcGFjZS4gVGFza3MgcmVxdWlyaW5nIHNpbXVsdGFuZW91cyBhdHRlbnRpb24gdG8gbXVsdGlwbGUgZGl2ZXJzZSBwb3NpdGlvbnMgKHN1YmplY3QrdmVyYitvYmplY3QsIG9yIHRva2VuK2l0cyBjb3JlZmVyZW5jZSBhbnRlY2VkZW50K3NlbnRlbmNlIGVuZCkgZm9yY2UgYSBzaW5nbGUgaGVhZCB0byBjb21wcm9taXNlLiBNdWx0aS1oZWFkIGF0dGVudGlvbiBhY2hpZXZlcyBhIGhpZ2hlciBlZmZlY3RpdmUgcmFuayBpbiBpdHMgb3V0cHV0IHRyYW5zZm9ybWF0aW9uLCBlbmFibGluZyBpdCB0byByb3V0ZSB0aHJvdWdoIG11bHRpcGxlIGluZGVwZW5kZW50IHBhdGh3YXlzIGFuZCBjb21iaW5lIHRoZW0gaW4gdGhlIG91dHB1dCBwcm9qZWN0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHNvZnRtYXgoUyk6XG4gICAgUyA9IFMgLSBTLm1heChheGlzPS0xLCBrZWVwZGltcz1UcnVlKVxuICAgIGUgPSBucC5leHAoUyk7IHJldHVybiBlIC8gZS5zdW0oYXhpcz0tMSwga2VlcGRpbXM9VHJ1ZSlcblxuZGVmIHNpbmdsZV9oZWFkKFEsIEssIFYsIFdxLCBXaywgV3YsIFdvKTpcbiAgICBBID0gc29mdG1heCgoUSBAIFdxKSBAIChLIEAgV2spLlQgLyBucC5zcXJ0KFdxLnNoYXBlWzFdKSlcbiAgICByZXR1cm4gKEEgQCAoViBAIFd2KSkgQCBXb1xuXG5kZWYgbXVsdGlfaGVhZChRLCBLLCBWLCBXUXMsIFdLcywgV1ZzLCBXbyk6XG4gICAgaGVhZHMgPSBbKHNvZnRtYXgoKFFAV3EpQChLQFdrKS5UL25wLnNxcnQoV3Euc2hhcGVbMV0pKSlAKFZAV3YpXG4gICAgICAgICAgICAgZm9yIFdxLCBXaywgV3YgaW4gemlwKFdRcywgV0tzLCBXVnMpXVxuICAgIHJldHVybiBucC5jb25jYXRlbmF0ZShoZWFkcywgYXhpcz0tMSkgQCBXb1xuXG5ucC5yYW5kb20uc2VlZCgxKVxubiwgZCwgaCA9IDEyLCA2NCwgOFxuZGsgPSBkIC8vIGhcblEgPSBLID0gViA9IG5wLnJhbmRvbS5yYW5kbihuLCBkKVxuXG5XcTEgPSBucC5yYW5kb20ucmFuZG4oZCwgZCkgKiAwLjFcbldrMSA9IG5wLnJhbmRvbS5yYW5kbihkLCBkKSAqIDAuMVxuV3YxID0gbnAuZXllKGQpOyBXbzEgPSBucC5leWUoZClcbnNoX291dCA9IHNpbmdsZV9oZWFkKFEsIEssIFYsIFdxMSwgV2sxLCBXdjEsIFdvMSlcblxuV1FzID0gW25wLnJhbmRvbS5yYW5kbihkLCBkaykqMC4xIGZvciBfIGluIHJhbmdlKGgpXVxuV0tzID0gW25wLnJhbmRvbS5yYW5kbihkLCBkaykqMC4xIGZvciBfIGluIHJhbmdlKGgpXVxuV1ZzID0gW25wLmV5ZShkKVs6LCBpKmRrOihpKzEpKmRrXSBmb3IgaSBpbiByYW5nZShoKV1cbldPbSA9IG5wLnJhbmRvbS5yYW5kbihkLCBkKSAqIDAuMVxubWhfb3V0ID0gbXVsdGlfaGVhZChRLCBLLCBWLCBXUXMsIFdLcywgV1ZzLCBXT20pXG5cbnByaW50KFx1MDAyN1NpbmdsZS1oZWFkIG91dHB1dCBtYXRyaXggcmFuazpcdTAwMjcsIG5wLmxpbmFsZy5tYXRyaXhfcmFuayhzaF9vdXQpKVxucHJpbnQoXHUwMDI3TXVsdGktaGVhZCBvdXRwdXQgbWF0cml4IHJhbms6IFx1MDAyNywgbnAubGluYWxnLm1hdHJpeF9yYW5rKG1oX291dCkpXG5wcmludChcdTAwMjdNdWx0aS1oZWFkIGFjaGlldmVzIGhpZ2hlciByYW5rIC1cdTAwM2UgcmljaGVyIHJlcHJlc2VudGF0aW9uYWwgY2FwYWNpdHkuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpbWluaXNoaW5nIFJldHVybnMgYW5kIFByYWN0aWNhbCBHdWlkYW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW1waXJpY2FsIHJlc3VsdHMgc2hvdyBkaW1pbmlzaGluZyByZXR1cm5zIGJleW9uZCA44oCTMTYgaGVhZHMgZm9yIG1vc3QgTkxQIHRhc2tzIGF0IHN0YW5kYXJkIG1vZGVsIHNpemVzLiBCZXlvbmQgdGhhdCwgYWRkaXRpb25hbCBoZWFkcyBvZnRlbiBjb252ZXJnZSB0byBzaW1pbGFyIHBhdHRlcm5zIG9yIGFjdCBhcyBhdHRlbnRpb24gc2lua3MuIFRoZSBvcHRpbWFsIGggYmFsYW5jZXMgcmVwcmVzZW50YXRpb25hbCBkaXZlcnNpdHkgKGZhdm91cmluZyBtb3JlIGhlYWRzKSBhZ2FpbnN0IHBlci1oZWFkIGNhcGFjaXR5IChmYXZvdXJpbmcgZmV3ZXIsIHdpZGVyIGhlYWRzKS4gRm9yIHZlcnkgbGFyZ2UgbW9kZWxzIChkX21vZGVsIOKJpSA0MDk2KSBtb3JlIGhlYWRzIGhlbHAgYnkgc3BsaXR0aW5nIHRoZSBlbm9ybW91cyBrZXkgc3BhY2U7IGZvciBzbWFsbCBtb2RlbHMgKGRfbW9kZWwg4omkIDI1NikgZmV3ZXIgaGVhZHMgd2l0aCBsYXJnZXIgZOKCliB0eXBpY2FsbHkgd29yayBiZXR0ZXIuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkhlYWQgVHlwZSIsIldoYXQgSXQgQXR0ZW5kcyBUbyIsIkV4YW1wbGUgaW4gQkVSVCIsIlNhZmVseSBQcnVuYWJsZT8iXSwicm93cyI6W1siTG9jYWwgLyBwb3NpdGlvbmFsIiwiQWRqYWNlbnQgdG9rZW5zIChwcmV2IG9yIG5leHQgcG9zaXRpb24pIiwiRWFjaCB3b3JkIGF0dGVuZGluZyB0byBpdHMgaW1tZWRpYXRlIG5laWdoYm91ciIsIk9mdGVuIHllcyDigJQgbG93IHRhc2sgcmVsZXZhbmNlIl0sWyJTeW50YWN0aWMgZGVwZW5kZW5jeSIsIkhlYWQgbm91biDihpIgbW9kaWZpZXI7IHN1YmplY3Qg4oaSIHZlcmIiLCJOb3VuIGF0dGVuZGluZyB0byBpdHMgZ292ZXJuaW5nIHZlcmIiLCJObyDigJQgdGFzay1jcml0aWNhbCJdLFsiQ29yZWZlcmVuY2UiLCJQcm9ub3VuIOKGkiBpdHMgYW50ZWNlZGVudCBub3VuIiwiXHUwMDI3aXRcdTAwMjcgYXR0ZW5kaW5nIHRvIHRoZSBlbnRpdHkgaXQgcmVmZXJzIHRvIiwiTm8g4oCUIHRhc2stY3JpdGljYWwiXSxbIkF0dGVudGlvbiBzaW5rIChbU0VQXS9bQ0xTXSkiLCJNYW55IHRva2VucyBhdHRlbmQgdG8gc3BlY2lhbCB0b2tlbnMiLCJbU0VQXSBhY3RpbmcgYXMgbm8tb3AgaW5mb3JtYXRpb24gZHVtcCIsIlllcyDigJQgbWluaW1hbCBpbmZvcm1hdGlvbiB0cmFuc2ZlciJdLFsiU2VtYW50aWMgc2ltaWxhcml0eSIsIlNlbWFudGljYWxseSByZWxhdGVkIHRva2VucyBhY3Jvc3MgdGhlIHNlbnRlbmNlIiwiU3lub255bXMgYW5kIGNvLWh5cG9ueW1zIiwiUGFydGlhbGx5IOKAlCBkZXBlbmRzIG9uIHRhc2siXSxbIlJhcmUtd29yZCIsIkxvdy1mcmVxdWVuY3kgdG9rZW5zIGF0dGVuZCBnbG9iYWxseSIsIlVua25vd24gd29yZHMgZ2F0aGVyIGJyb2FkIGNvbnRleHQiLCJQYXJ0aWFsbHkiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3RhcnQgd2l0aCBoID0gZF9tb2RlbCAvIDY0IGFzIHRoZSBkZWZhdWx0IChk4oKWID0gNjQgcGVyIGhlYWQpOiB3b3JrcyB3ZWxsIGZvciBkX21vZGVsIOKIiCB7MjU2LCA1MTIsIDc2OCwgMTAyNH0iLCJHcm91cGVkIFF1ZXJ5IEF0dGVudGlvbiAoR1FBKTogdXNlIGZld2VyIEtWIGhlYWRzIHRoYW4gUSBoZWFkcyB0byByZWR1Y2UgS1YgY2FjaGUgYXQgaW5mZXJlbmNlIHdpdGhvdXQgbXVjaCBxdWFsaXR5IGxvc3MiLCJIZWFkIHBydW5pbmcgYnVkZ2V0OiBmb3IgQkVSVC1zY2FsZSBtb2RlbHMsIHBydW5pbmcgNTAlIG9mIGhlYWRzIHR5cGljYWxseSBjb3N0cyBcdTAwM2MgMSUgYWNjdXJhY3kiLCJEaWFnbm9zdGljOiBtZWFzdXJlIHBlci1oZWFkIGVudHJvcHkgb24gYSBoZWxkLW91dCBzZXQg4oCUIGhlYWRzIHdpdGggbmVhci1tYXhpbXVtIGVudHJvcHkgYXJlIGNhbmRpZGF0ZXMgZm9yIHBydW5pbmciLCJBdHRlbnRpb24gaGVhZCBhbmFseXNpcyBpcyBtb3N0IGludGVycHJldGFibGUgaW4gdGhlIGZpcnN0IGZldyBsYXllcnM7IGRlZXAgbGF5ZXJzIGV4aGliaXQgbGVzcyBzdHJ1Y3R1cmVkIHBhdHRlcm5zIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Why Multiple Attention Heads — Different Subspace Specialisation

A Transformer with a single attention head per layer learns one global attention pattern per layer — a single learned similarity function applied uniformly to all queries. Multiple heads allow the model to simultaneously route information through h different learned routing functions, each operating on a different linear projection of the same input. This is not merely redundancy: different heads tend to specialise on syntactic dependencies, coreference, positional structure, and semantic similarity simultaneously.

## Single-Head Limitation

With a single attention head of dimension d_model, every position computes a single query and compares it to a single set of keys. The output is one weighted combination of value vectors — a rank-1 routing. If the task requires simultaneously attending to multiple unrelated positions (e.g., the subject of a sentence and a distant pronoun that refers to it), a single head must trade off between them, achieving neither reliably. Multiple heads circumvent this by partitioning the capacity — head 1 can attend to syntactic dependencies while head 2 handles coreference without either interfering with the other.

## Mathematical Justification — Subspace Representation

The projection matrices WᵢQ and WᵢK map the full d_model-dimensional input into a dₖ-dimensional subspace. Different heads project into different subspaces, so they measure similarity along different directions. Formally, h heads produce h independent attention-weighted sums of value projections; concatenating them before Wᴼ allows the output projection to mix information from all h subspaces. The rank of the combined output is bounded by min(h·dv, d_model) — potentially far higher than the rank achievable with a single head of dimension d_model.

Superposition theory (Elhage et al. 2022) provides a complementary view: with enough heads, a Transformer layer can store and retrieve multiple approximately-orthogonal 'features' simultaneously. Each head acts on a different subspace in which distinct features are nearly orthogonal; interference between features is suppressed across heads even when it cannot be avoided within a single head. This allows the model to maintain more independent 'thoughts' per layer than its raw dimension would suggest.

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(42)
d_model, h = 256, 8
mha = nn.MultiheadAttention(d_model, h, batch_first=True)
WQ, WK, _ = mha.in_proj_weight.chunk(3, dim=0)
dk = d_model // h

tokens = ['[CLS]', 'the', 'cat', 'sat', 'on', 'mat', '[SEP]', '.']
seq_len = len(tokens)
x = torch.randn(1, seq_len, d_model)
x_flat = x.squeeze(0)

def head_attn(x_flat, i):
    with torch.no_grad():
        Q = (x_flat @ WQ.T)[:, i*dk:(i+1)*dk]
        K = (x_flat @ WK.T)[:, i*dk:(i+1)*dk]
        S = (Q @ K.T / dk**0.5).numpy()
    S -= S.max(1, keepdims=True)
    A = np.exp(S); A /= A.sum(1, keepdims=True)
    return A

print('Head | ' + ' | '.join('{:>5}'.format(t[:5]) for t in tokens))
print('-' * (7 + 8 * seq_len))
for i in range(h):
    A = head_attn(x_flat, i)
    peaks = [tokens[j][:5] for j in A.argmax(axis=1)]
    ent = -(A * np.log(A + 1e-9)).sum(1).mean()
    row = ' | '.join('{:>5}'.format(p) for p in peaks)
    print('H{:>2}  | {}  ent={:.2f}'.format(i, row, ent))
```

## Empirical Evidence — Clark et al. 2019

Clark et al. (2019) systematically analysed attention patterns across all 144 heads in BERT-base. They found clear functional specialisation: certain heads track direct object relationships, others attend to coreferent mentions, and a distinct class attends to the immediately preceding or following token. Crucially, some heads capture information highly correlated with the output of supervised dependency parsers — without any explicit supervision on syntax. This provides strong empirical evidence that multi-head attention spontaneously learns diverse, linguistically meaningful routing functions across heads.

> **Clark et al. 2019 Key Findings**: In BERT-base (12 layers × 12 heads = 144 heads total): (1) Heads in layers 6–10 show the strongest syntactic behaviour. (2) A single head in layer 8 achieves 76.1% accuracy on a coreference task with no fine-tuning. (3) Certain heads attend almost exclusively to [SEP] or [CLS] tokens — acting as 'no-op' attention sinks. (4) Removing any single head causes <1% performance drop; removing the top-5 most important heads causes ~3% drop. Attention patterns are sparse and interpretable at the head level.

```python
import torch
import torch.nn as nn

torch.manual_seed(7)
d_model, h, seq_len, batch = 128, 8, 20, 16

class TinyTransformerLayer(nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, h, batch_first=True)
        self.norm = nn.LayerNorm(d_model)
        self.proj = nn.Linear(d_model, 1)

    def forward(self, x):
        a, _ = self.attn(x, x, x)
        x = self.norm(x + a)
        return self.proj(x.mean(dim=1))

model = TinyTransformerLayer()
x = torch.randn(batch, seq_len, d_model)
y = x.mean(dim=(1, 2)).unsqueeze(-1)
loss = nn.functional.mse_loss(model(x), y)
loss.backward()

WQ_g, WK_g, WV_g = model.attn.in_proj_weight.grad.chunk(3, dim=0)
dk = d_model // h
print('{:>6} {:>10} {:>10} {:>10} {:>12}'.format('Head', 'Q_grad', 'K_grad', 'V_grad', 'Importance'))
for i in range(h):
    qg = WQ_g[i*dk:(i+1)*dk].norm().item()
    kg = WK_g[i*dk:(i+1)*dk].norm().item()
    vg = WV_g[i*dk:(i+1)*dk].norm().item()
    imp = (qg + kg + vg) / 3
    print('{:>6} {:>10.4f} {:>10.4f} {:>10.4f} {:>12.4f}'.format(i, qg, kg, vg, imp))
print('Higher gradient norm -> head contributes more to this task.')
```

## Head Pruning

Michel et al. (2019) showed that most attention heads in BERT can be pruned at test time with minimal accuracy loss — for BERT-base on MNLI, only 16 of 144 heads are needed to retain 90% of performance. Voita et al. (2019) identified four head roles that are consistently preserved: positional (attend to adjacent token), syntactic (attend to syntactic dependents), rare-word (attend to low-frequency tokens), and coreference. Unimportant heads — those whose removal causes the smallest accuracy drop — can be zeroed out by setting the corresponding columns of Wᴼ to zero, which is equivalent to removing their contribution to the output.

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(0)
d_model, h, n = 128, 8, 15

mha = nn.MultiheadAttention(d_model, h, batch_first=True)
x = torch.randn(4, n, d_model)

with torch.no_grad():
    baseline, _ = mha(x, x, x)

# Compute per-head importance: gradient of output L2 norm w.r.t. WV slice
importances = []
for i in range(h):
    x_req = x.clone().requires_grad_(True)
    out, _ = mha(x_req, x_req, x_req)
    out.norm().backward()
    WQ_g, WK_g, WV_g = mha.in_proj_weight.grad.chunk(3, dim=0) if mha.in_proj_weight.grad is not None else (torch.zeros(d_model,d_model),)*3
    dk = d_model // h
    importances.append(float(WV_g[i*dk:(i+1)*dk].norm()) if WV_g is not None else 0.0)
    mha.zero_grad()

importances = np.array(importances)
ranked = np.argsort(importances)
print('Head importance ranking (least to most):', ranked.tolist())
print('Least important head (prune first): head', ranked[0])

# Zero out the least important head in WO
with torch.no_grad():
    dk = d_model // h
    mha.out_proj.weight[:, ranked[0]*dk:(ranked[0]+1)*dk] = 0
    pruned, _ = mha(x, x, x)

diff = (baseline - pruned).abs().mean().item()
print('Output change after pruning head {}: {:.4f}'.format(ranked[0], diff))
```

## Single-Head vs Multi-Head Task Comparison

A single attention head can represent at most one routing pattern per layer — it is limited to a rank-1 weighting of value vectors from a single subspace. Tasks requiring simultaneous attention to multiple diverse positions (subject+verb+object, or token+its coreference antecedent+sentence end) force a single head to compromise. Multi-head attention achieves a higher effective rank in its output transformation, enabling it to route through multiple independent pathways and combine them in the output projection.

```python
import numpy as np

def softmax(S):
    S = S - S.max(axis=-1, keepdims=True)
    e = np.exp(S); return e / e.sum(axis=-1, keepdims=True)

def single_head(Q, K, V, Wq, Wk, Wv, Wo):
    A = softmax((Q @ Wq) @ (K @ Wk).T / np.sqrt(Wq.shape[1]))
    return (A @ (V @ Wv)) @ Wo

def multi_head(Q, K, V, WQs, WKs, WVs, Wo):
    heads = [(softmax((Q@Wq)@(K@Wk).T/np.sqrt(Wq.shape[1])))@(V@Wv)
             for Wq, Wk, Wv in zip(WQs, WKs, WVs)]
    return np.concatenate(heads, axis=-1) @ Wo

np.random.seed(1)
n, d, h = 12, 64, 8
dk = d // h
Q = K = V = np.random.randn(n, d)

Wq1 = np.random.randn(d, d) * 0.1
Wk1 = np.random.randn(d, d) * 0.1
Wv1 = np.eye(d); Wo1 = np.eye(d)
sh_out = single_head(Q, K, V, Wq1, Wk1, Wv1, Wo1)

WQs = [np.random.randn(d, dk)*0.1 for _ in range(h)]
WKs = [np.random.randn(d, dk)*0.1 for _ in range(h)]
WVs = [np.eye(d)[:, i*dk:(i+1)*dk] for i in range(h)]
WOm = np.random.randn(d, d) * 0.1
mh_out = multi_head(Q, K, V, WQs, WKs, WVs, WOm)

print('Single-head output matrix rank:', np.linalg.matrix_rank(sh_out))
print('Multi-head output matrix rank: ', np.linalg.matrix_rank(mh_out))
print('Multi-head achieves higher rank -> richer representational capacity.')
```

## Diminishing Returns and Practical Guidance

Empirical results show diminishing returns beyond 8–16 heads for most NLP tasks at standard model sizes. Beyond that, additional heads often converge to similar patterns or act as attention sinks. The optimal h balances representational diversity (favouring more heads) against per-head capacity (favouring fewer, wider heads). For very large models (d_model ≥ 4096) more heads help by splitting the enormous key space; for small models (d_model ≤ 256) fewer heads with larger dₖ typically work better.

| Head Type | What It Attends To | Example in BERT | Safely Prunable? |
| --- | --- | --- | --- |
| Local / positional | Adjacent tokens (prev or next position) | Each word attending to its immediate neighbour | Often yes — low task relevance |
| Syntactic dependency | Head noun → modifier; subject → verb | Noun attending to its governing verb | No — task-critical |
| Coreference | Pronoun → its antecedent noun | 'it' attending to the entity it refers to | No — task-critical |
| Attention sink ([SEP]/[CLS]) | Many tokens attend to special tokens | [SEP] acting as no-op information dump | Yes — minimal information transfer |
| Semantic similarity | Semantically related tokens across the sentence | Synonyms and co-hyponyms | Partially — depends on task |
| Rare-word | Low-frequency tokens attend globally | Unknown words gather broad context | Partially |

- Start with h = d_model / 64 as the default (dₖ = 64 per head): works well for d_model ∈ {256, 512, 768, 1024}
- Grouped Query Attention (GQA): use fewer KV heads than Q heads to reduce KV cache at inference without much quality loss
- Head pruning budget: for BERT-scale models, pruning 50% of heads typically costs < 1% accuracy
- Diagnostic: measure per-head entropy on a held-out set — heads with near-maximum entropy are candidates for pruning
- Attention head analysis is most interpretable in the first few layers; deep layers exhibit less structured patterns

---

