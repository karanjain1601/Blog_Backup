---
title: "Exploding Gradients — Clipping Strategies"
slug: "exploding-gradients-clipping"
description: "Understand why gradients explode in RNNs and deep networks, compare value vs norm clipping empirically, monitor gradient health during training, and apply correct clipping with gradient accumulation."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXhwbG9kaW5nIGdyYWRpZW50cyBhcmUgdGhlIG9wcG9zaXRlIG9mIHZhbmlzaGluZzogd2hlbiB0aGUgc3BlY3RyYWwgcmFkaXVzIG9mIGVhY2ggSmFjb2JpYW4gZXhjZWVkcyAxLCB0aGUgcHJvZHVjdCBvZiBKYWNvYmlhbnMgZ3Jvd3MgZXhwb25lbnRpYWxseSB3aXRoIGRlcHRoIG9yIHNlcXVlbmNlIGxlbmd0aC4gUk5OcyBhcmUgZXNwZWNpYWxseSB2dWxuZXJhYmxlIGJlY2F1c2UgdGhlIHNhbWUgd2VpZ2h0IG1hdHJpeCBXIGlzIG11bHRpcGxpZWQgYXQgZXZlcnkgdGltZSBzdGVwIOKAlCB0aGUgZWZmZWN0aXZlIGRlcHRoIGVxdWFscyB0aGUgc2VxdWVuY2UgbGVuZ3RoLCB3aGljaCBjYW4gYmUgaHVuZHJlZHMgb3IgdGhvdXNhbmRzLiBTeW1wdG9tcyBpbmNsdWRlIE5hTiBsb3NzLCBkaXZlcmdpbmcgdHJhaW5pbmcgY3VydmVzLCBhbmQgc3VkZGVuIGdyYWRpZW50IG5vcm0gc3Bpa2VzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHdvIG1haW4gY2xpcHBpbmcgc3RyYXRlZ2llcyBleGlzdDogdmFsdWUgY2xpcHBpbmcgKHBlci1lbGVtZW50KSBhbmQgbm9ybSBjbGlwcGluZyAoZ2xvYmFsIHNjYWxlKS4gTm9ybSBjbGlwcGluZyBpcyB0aGUgc3RhbmRhcmQgZm9yIGxhcmdlIGxhbmd1YWdlIG1vZGVscy4gRXhwbG9kaW5nIGdyYWRpZW50cyBhcmUgZGlzdGluY3QgZnJvbSB2YW5pc2hpbmcg4oCUIGJvdGggY2FuIGNvZXhpc3QgaW4gdGhlIHNhbWUgbmV0d29yayB3aGVuIGVhcmx5IGxheWVycyB2YW5pc2ggYW5kIGxhdGUgbGF5ZXJzIGV4cGxvZGUsIGEgY29tbW9uIHBhdGhvbG9neSBpbiB2ZXJ5IGRlZXAgbmV0d29ya3Mgd2l0aG91dCByZXNpZHVhbCBjb25uZWN0aW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYXRoZW1hdGljYWwgQ2F1c2Ug4oCUIFJOTiBHcmFkaWVudCBFeHBsb3Npb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIGFuIFJOTiwgaOKCnCA9IHRhbmgoV2jigpzigovigoEgKyBVeOKCnCkuIEJ5IHRoZSBjaGFpbiBydWxlLCDiiIJo4oKcL+KIgmjigoAgPSDOoOKCluKCjOKCgeG1lyBkaWFnKHRhbmhcdTAwMjcowrcpKSDCtyBXLiBJZiDPgShXKSBcdTAwM2UgMSwgdGhlbiDigJbiiIJo4oKcL+KIgmjigoDigJYgZ3Jvd3MgYXMgz4EoVynhtYAuIEZvciDPgShXKSA9IDEuMSBhbmQgVD0xMDAsIGdyYWRpZW50IG1hZ25pdHVkZSByZWFjaGVzIDEuMcK54oGw4oGwIOKJiCAxMyw3ODAuIEV2ZW4gbW9kZXN0IHNwZWN0cmFsIHJhZGlpIGFib3ZlIDEgcHJvZHVjZSBjYXRhc3Ryb3BoaWMgZXhwbG9zaW9uIG92ZXIgbG9uZyBzZXF1ZW5jZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBzaW11bGF0ZV9leHBsb3Npb24oc2VxX2xlbj01MCwgaGlkZGVuPTMyLCBzcGVjdHJhbF9yYWRpdXM9MS4xLCBzZWVkPTApOlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgcm5uID0gbm4uUk5OQ2VsbChoaWRkZW4sIGhpZGRlbiwgbm9ubGluZWFyaXR5PVx1MDAyN3RhbmhcdTAwMjcpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIFUsIFMsIFYgPSB0b3JjaC5saW5hbGcuc3ZkKHJubi53ZWlnaHRfaGgpXG4gICAgICAgIHJubi53ZWlnaHRfaGguZGF0YSA9IChVICogKFMgKiBzcGVjdHJhbF9yYWRpdXMgLyBTWzBdKS51bnNxdWVlemUoMCkpIEAgVlxuICAgIGggPSB0b3JjaC56ZXJvcygxLCBoaWRkZW4sIHJlcXVpcmVzX2dyYWQ9VHJ1ZSlcbiAgICBoX2N1cnIgPSBoXG4gICAgZm9yIHQgaW4gcmFuZ2Uoc2VxX2xlbik6XG4gICAgICAgIGhfY3VyciA9IHJubih0b3JjaC5yYW5kbigxLCBoaWRkZW4pLCBoX2N1cnIpXG4gICAgaF9jdXJyLm1lYW4oKS5iYWNrd2FyZCgpXG4gICAgcHJpbnQoZlx1MDAyN3Jobz17c3BlY3RyYWxfcmFkaXVzfSwgVD17c2VxX2xlbn06IGdyYWQgbm9ybT17aC5ncmFkLm5vcm0oKTouM2V9LCBleHBlY3RlZH57c3BlY3RyYWxfcmFkaXVzKipzZXFfbGVuOi4zZX1cdTAwMjcpXG5cbnNpbXVsYXRlX2V4cGxvc2lvbihzZXFfbGVuPTMwLCBzcGVjdHJhbF9yYWRpdXM9MS4wNSlcbnNpbXVsYXRlX2V4cGxvc2lvbihzZXFfbGVuPTMwLCBzcGVjdHJhbF9yYWRpdXM9MS4yMCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWYWx1ZSBDbGlwcGluZyB2cyBOb3JtIENsaXBwaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWYWx1ZSBjbGlwcGluZyBjbGlwcyBlYWNoIGdyYWRpZW50IGVsZW1lbnQgaW5kZXBlbmRlbnRseTogZ+G1oiDihpAgY2xpcChn4bWiLCDiiJJjLCBjKS4gVGhpcyBjaGFuZ2VzIHRoZSBncmFkaWVudCBkaXJlY3Rpb24g4oCUIHJlbGF0aXZlIG1hZ25pdHVkZXMgYWNyb3NzIHBhcmFtZXRlcnMgYXJlIGFsdGVyZWQuIE5vcm0gY2xpcHBpbmcgcmVzY2FsZXMgdGhlIGVudGlyZSBncmFkaWVudDogaWYg4oCWZ+KAliBcdTAwM2UgYywgdGhlbiBnIOKGkCBnIMK3IGMv4oCWZ+KAli4gVGhpcyBwcmVzZXJ2ZXMgZGlyZWN0aW9uIHdoaWxlIGJvdW5kaW5nIG1hZ25pdHVkZS4gTm9ybSBjbGlwcGluZyBpcyB0aGUgc3RhbmRhcmQgaW4gTExNIHRyYWluaW5nIOKAlCBHUFQsIFQ1LCBMTGFNQSBhbGwgdXNlIG1heF9ub3JtPTEuMC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGNvbXBhcmVfY2xpcHBpbmcoY2xpcF92YWw9MS4wKTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZCg3KVxuICAgIG1vZGVsID0gbm4uTGluZWFyKDEwLCAxMClcbiAgICAobW9kZWwodG9yY2gucmFuZG4oNCwgMTApKSAqIDEwMCkubWVhbigpLmJhY2t3YXJkKClcbiAgICBnX29yaWcgPSBtb2RlbC53ZWlnaHQuZ3JhZC5jbG9uZSgpXG4gICAgb3JpZ19kaXIgPSBGLm5vcm1hbGl6ZShnX29yaWcuZmxhdHRlbigpLCBkaW09MClcblxuICAgIG1vZGVsLndlaWdodC5ncmFkLmRhdGEgPSBnX29yaWcuY2xvbmUoKVxuICAgIHRvcmNoLm5uLnV0aWxzLmNsaXBfZ3JhZF92YWx1ZV8obW9kZWwucGFyYW1ldGVycygpLCBjbGlwX3ZhbHVlPWNsaXBfdmFsKVxuICAgIGNvc192YWx1ZSA9IChvcmlnX2RpciAqIEYubm9ybWFsaXplKG1vZGVsLndlaWdodC5ncmFkLmZsYXR0ZW4oKSwgZGltPTApKS5zdW0oKS5pdGVtKClcblxuICAgIG1vZGVsLndlaWdodC5ncmFkLmRhdGEgPSBnX29yaWcuY2xvbmUoKVxuICAgIHRvcmNoLm5uLnV0aWxzLmNsaXBfZ3JhZF9ub3JtXyhtb2RlbC5wYXJhbWV0ZXJzKCksIG1heF9ub3JtPWNsaXBfdmFsKVxuICAgIGNvc19ub3JtICA9IChvcmlnX2RpciAqIEYubm9ybWFsaXplKG1vZGVsLndlaWdodC5ncmFkLmZsYXR0ZW4oKSwgZGltPTApKS5zdW0oKS5pdGVtKClcblxuICAgIHByaW50KGZcdTAwMjdPcmlnaW5hbCBub3JtOiB7Z19vcmlnLm5vcm0oKTouNGZ9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdWYWx1ZSBjbGlwIGNvc2luZSBzaW06IHtjb3NfdmFsdWU6LjZmfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3Tm9ybSAgY2xpcCBjb3NpbmUgc2ltOiB7Y29zX25vcm06LjZmfVx1MDAyNylcbiAgICBwcmludChcdTAwMjdOb3JtIGNsaXBwaW5nIHByZXNlcnZlcyBkaXJlY3Rpb24gKGNvc+KJiDEpOyB2YWx1ZSBjbGlwcGluZyBkaXN0b3J0cyBpdC5cdTAwMjcpXG5cbmNvbXBhcmVfY2xpcHBpbmcoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IE5vcm0gTW9uaXRvcmluZyBEdXJpbmcgVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxvZ2dpbmcgdGhlIHByZS1jbGlwIGdyYWRpZW50IG5vcm0gZXZlcnkgc3RlcCBpcyB0aGUgcHJpbWFyeSBoZWFsdGggbWV0cmljIGZvciBkZWVwIG5ldHdvcmsgdHJhaW5pbmcuIEEgaGVhbHRoeSBub3JtIHN0YXlzIGluIGEgc3RhYmxlIHJhbmdlOyBzcGlrZXMgaW5kaWNhdGUgaW5zdGFiaWxpdHkuIElmIG1vcmUgdGhhbiAzMCUgb2Ygc3RlcHMgcmVxdWlyZSBjbGlwcGluZywgdGhlIGxlYXJuaW5nIHJhdGUgaXMgdG9vIGhpZ2guIElmIGdyYWRpZW50IG5vcm1zIGFyZSBjb25zaXN0ZW50bHkgbmVhciB6ZXJvIGluIGVhcmx5IGxheWVycywgdmFuaXNoaW5nIGlzIHRoZSBpc3N1ZSDigJQgY2xpcHBpbmcgY2Fubm90IGZpeCB2YW5pc2hpbmcgZ3JhZGllbnRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiB0cmFpbl93aXRoX2dyYWRfbW9uaXRvcmluZyhuX3N0ZXBzPTIwMCwgY2xpcD0xLjAsIHNlZWQ9MCk6XG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICBtb2RlbCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgIG5uLkxpbmVhcig2NCwgMjU2KSwgbm4uVGFuaCgpLFxuICAgICAgICBubi5MaW5lYXIoMjU2LCAyNTYpLCBubi5UYW5oKCksXG4gICAgICAgIG5uLkxpbmVhcigyNTYsIDEwKVxuICAgIClcbiAgICBvcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBncmFkX25vcm1zLCBjbGlwcGVkID0gW10sIDBcbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX3N0ZXBzKTpcbiAgICAgICAgeCwgeSA9IHRvcmNoLnJhbmRuKDMyLCA2NCksIHRvcmNoLnJhbmRpbnQoMCwgMTAsICgzMiwpKVxuICAgICAgICBubi5Dcm9zc0VudHJvcHlMb3NzKCkobW9kZWwoeCksIHkpLmJhY2t3YXJkKClcbiAgICAgICAgdG90YWxfbm9ybSA9IHRvcmNoLm5uLnV0aWxzLmNsaXBfZ3JhZF9ub3JtXyhtb2RlbC5wYXJhbWV0ZXJzKCksIG1heF9ub3JtPWNsaXApXG4gICAgICAgIGdyYWRfbm9ybXMuYXBwZW5kKHRvdGFsX25vcm0uaXRlbSgpKVxuICAgICAgICBpZiB0b3RhbF9ub3JtLml0ZW0oKSBcdTAwM2UgY2xpcDogY2xpcHBlZCArPSAxXG4gICAgICAgIG9wdGltaXplci5zdGVwKCk7IG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgIHByaW50KGZcdTAwMjdDbGlwPXtjbGlwfToge2NsaXBwZWR9L3tuX3N0ZXBzfSBzdGVwcyBjbGlwcGVkICh7MTAwKmNsaXBwZWQvbl9zdGVwczouMWZ9JSlcdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN0dyYWQgbm9ybTogbWVhbj17bnAubWVhbihncmFkX25vcm1zKTouNGZ9IG1heD17bnAubWF4KGdyYWRfbm9ybXMpOi40Zn1cdTAwMjcpXG5cbnRyYWluX3dpdGhfZ3JhZF9tb25pdG9yaW5nKGNsaXA9MS4wKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IEFjY3VtdWxhdGlvbiB3aXRoIENvcnJlY3QgQ2xpcHBpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdyYWRpZW50IGFjY3VtdWxhdGlvbiBzaW11bGF0ZXMgYSBsYXJnZXIgZWZmZWN0aXZlIGJhdGNoIHNpemUgYnkgYWNjdW11bGF0aW5nIGdyYWRpZW50cyBvdmVyIG11bHRpcGxlIG1pY3JvLXN0ZXBzIGJlZm9yZSBjYWxsaW5nIG9wdGltaXplci5zdGVwKCkuIFRoZSBjcml0aWNhbCBydWxlOiBjbGlwIGFmdGVyIGFsbCBtaWNyby1zdGVwcywgbmV2ZXIgYmVmb3JlLiBDbGlwcGluZyBlYWNoIG1pY3JvLWJhdGNoIGluZGVwZW5kZW50bHkgYXBwbGllcyBtdWx0aXBsZSBjbGlwcGluZyBvcGVyYXRpb25zIGFuZCB0aGUgZmluYWwgZ3JhZGllbnQgZG9lcyBub3QgY29ycmVzcG9uZCB0byBhIHNpbmdsZSBjbGlwcGVkIGdsb2JhbCBncmFkaWVudC4gU2NhbGUgdGhlIGxvc3MgYnkgMS9hY2N1bV9zdGVwcyBiZWZvcmUgYmFja3dhcmQgdG8gbm9ybWFsaXplIHRoZSBhY2N1bXVsYXRlZCBncmFkaWVudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIHRyYWluX3dpdGhfYWNjdW11bGF0aW9uKGFjY3VtX3N0ZXBzPTQsIGNsaXA9MS4wLCBuX2l0ZXJzPTUwKTpcbiAgICB0b3JjaC5tYW51YWxfc2VlZCgwKVxuICAgIG1vZGVsID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMzIsIDY0KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoNjQsIDQpKVxuICAgIG9wdGltaXplciA9IHRvcmNoLm9wdGltLkFkYW1XKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBjcml0ZXJpb24gPSBubi5Dcm9zc0VudHJvcHlMb3NzKClcbiAgICBmb3Igc3RlcCBpbiByYW5nZShuX2l0ZXJzKTpcbiAgICAgICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgICAgIHRvdGFsX2xvc3MgPSAwLjBcbiAgICAgICAgZm9yIF8gaW4gcmFuZ2UoYWNjdW1fc3RlcHMpOlxuICAgICAgICAgICAgeCA9IHRvcmNoLnJhbmRuKDgsIDMyKVxuICAgICAgICAgICAgeSA9IHRvcmNoLnJhbmRpbnQoMCwgNCwgKDgsKSlcbiAgICAgICAgICAgIGxvc3MgPSBjcml0ZXJpb24obW9kZWwoeCksIHkpIC8gYWNjdW1fc3RlcHNcbiAgICAgICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICAgICAgdG90YWxfbG9zcyArPSBsb3NzLml0ZW0oKVxuICAgICAgICBncmFkX25vcm0gPSB0b3JjaC5ubi51dGlscy5jbGlwX2dyYWRfbm9ybV8obW9kZWwucGFyYW1ldGVycygpLCBtYXhfbm9ybT1jbGlwKVxuICAgICAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgIGlmIHN0ZXAgJSAxMCA9PSAwOlxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyN1N0ZXAge3N0ZXA6M2R9OiBsb3NzPXt0b3RhbF9sb3NzOi40Zn0gZ3JhZF9ub3JtPXtncmFkX25vcm06LjRmfVx1MDAyNylcblxudHJhaW5fd2l0aF9hY2N1bXVsYXRpb24oKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxSIFdhcm11cCBhbmQgU3BlY3RyYWwgTm9ybWFsaXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGVhcm5pbmcgcmF0ZSB3YXJtdXAgbGluZWFybHkgaW5jcmVhc2VzIExSIGZyb20gMCB0byB0aGUgdGFyZ2V0IG92ZXIgdGhlIGZpcnN0IGZldyBodW5kcmVkIHN0ZXBzLiBBdCB0aGUgc3RhcnQgb2YgdHJhaW5pbmcsIHBhcmFtZXRlcnMgYXJlIHJhbmRvbWx5IGluaXRpYWxpemVkIGFuZCBncmFkaWVudHMgY2FuIGJlIGxhcmdlIGFuZCBpbmNvbnNpc3RlbnQuIEEgc21hbGwgaW5pdGlhbCBMUiBwcmV2ZW50cyBlYXJseSBncmFkaWVudCBleHBsb3Npb25zIGJlZm9yZSB0aGUgb3B0aW1pemVyIGFjY3VtdWxhdGVzIHN0YWJsZSBtb21lbnR1bSBlc3RpbWF0ZXMuIExSIHdhcm11cCBpcyBjb21wbGVtZW50YXJ5IHRvIGNsaXBwaW5nIOKAlCBjbGlwcGluZyBpcyBhIHNhZmV0eSBuZXQgd2hpbGUgd2FybXVwIHByZXZlbnRzIHRoZSBwcm9ibGVtIGZyb20gb2NjdXJyaW5nLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BlY3RyYWwgbm9ybWFsaXphdGlvbiAoTWl5YXRvIDIwMTgpIGNvbnN0cmFpbnMgdGhlIHNwZWN0cmFsIHJhZGl1cyBvZiBlYWNoIHdlaWdodCBtYXRyaXggdG8gYmUg4omkIDEgYnkgZGl2aWRpbmcgYnkgdGhlIHRvcCBzaW5ndWxhciB2YWx1ZTogV19zbiA9IFcvz4PigoEoVykuIFRoaXMgZWxpbWluYXRlcyBncmFkaWVudCBleHBsb3Npb24gYXQgdGhlIHNvdXJjZS4gVXNlZCBpbiBHQU5zIChkaXNjcmltaW5hdG9yIHN0YWJpbGl6YXRpb24pIGFuZCBzb21lIHRyYW5zZm9ybWVyIHZhcmlhbnRzIGFzIGFuIGFsdGVybmF0aXZlIHRvIGNsaXBwaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0cmF0ZWd5IENvbXBhcmlzb24ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkxMTSBUcmFpbmluZyBTdGFuZGFyZCIsImNvbnRlbnQiOiJBbGwgbWFqb3IgTExNIHRyYWluaW5nIHJlY2lwZXMgKEdQVC0zLCBMTGFNQSwgTWlzdHJhbCkgdXNlIGdsb2JhbCBub3JtIGNsaXBwaW5nIHdpdGggbWF4X25vcm09MS4wLCBhcHBsaWVkIGFmdGVyIGdyYWRpZW50IGFjY3VtdWxhdGlvbiBhbmQgYmVmb3JlIG9wdGltaXplci5zdGVwKCkuIExvZyB0aGUgcHJlLWNsaXAgbm9ybSB0byBXXHUwMDI2QiBldmVyeSBzdGVwIOKAlCBzdXN0YWluZWQgbm9ybXMgYWJvdmUgNcOXIHRoZSBjbGlwIHRocmVzaG9sZCBpbmRpY2F0ZSBhcmNoaXRlY3R1cmUgb3IgTFIgaXNzdWVzIHRoYXQgY2xpcHBpbmcgYWxvbmUgY2Fubm90IGZpeC4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiU3RyYXRlZ3kiLCJEaXJlY3Rpb24gcHJlc2VydmVkIiwiTExNIHN0YW5kYXJkIiwiV2hlbiB0byB1c2UiXSwicm93cyI6W1siVmFsdWUgY2xpcHBpbmcgKGNsaXBfZ3JhZF92YWx1ZV8pIiwiTm8g4oCUIGRpc3RvcnRlZCIsIk5vIiwiU2ltcGxlIFJOTnMsIGxlZ2FjeSBjb2RlIl0sWyJOb3JtIGNsaXBwaW5nIChjbGlwX2dyYWRfbm9ybV8pIiwiWWVzIOKAlCBvbmx5IHNjYWxlIGNoYW5nZXMiLCJZZXMgKG1heF9ub3JtPTEuMCkiLCJEZWZhdWx0IGZvciBhbGwgbW9kZXJuIGRlZXAgbmV0d29ya3MiXSxbIkFkYXB0aXZlIHBlci1sYXllciBub3JtIGNsaXBwaW5nIiwiWWVzIiwiUmFyZSIsIkhldGVyb2dlbmVvdXMgYXJjaGl0ZWN0dXJlcyJdLFsiU3BlY3RyYWwgbm9ybWFsaXphdGlvbiIsIk4vQSDigJQgcHJldmVudHMgZXhwbG9zaW9uIiwiTm8iLCJHQU5zLCB3aGVuIHN0YWJpbGl0eSBpcyBjcml0aWNhbCJdLFsiTm8gY2xpcHBpbmciLCJOL0EiLCJObyIsIk9ubHkgd2hlbiBzcGVjdHJhbCBub3JtIGd1YXJhbnRlZXMgYm91bmRlZCBncmFkaWVudHMiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTG9nIGdyYWRfbm9ybSBiZWZvcmUgY2xpcHBpbmcgZXZlcnkgc3RlcCDigJQgc3VkZGVuIHNwaWtlcyBhcmUgZWFybHkgd2FybmluZyBvZiBpbnN0YWJpbGl0eS4iLCJMUiB3YXJtdXAgY29tcGxlbWVudHMgY2xpcHBpbmc6IHNtYWxsIGluaXRpYWwgTFIgcmVkdWNlcyBlYXJseSBncmFkaWVudCBleHBsb3Npb24gcmlzay4iLCJJZiBcdTAwM2UzMCUgb2Ygc3RlcHMgYXJlIGNsaXBwZWQsIHJlZHVjZSBsZWFybmluZyByYXRlIOKAlCBjbGlwcGluZyBpcyBhIHNhZmV0eSBuZXQsIG5vdCBhIHN1YnN0aXR1dGUgZm9yIExSIHR1bmluZy4iLCJXaXRoIGdyYWRpZW50IGFjY3VtdWxhdGlvbiwgY2xpcCBvbmNlIGFmdGVyIGFsbCBtaWNyby1zdGVwcywgbm90IHBlciBtaWNyby1zdGVwLiIsIlNwZWN0cmFsIG5vcm1hbGl6YXRpb24gb24gd2VpZ2h0IG1hdHJpY2VzIGJvdW5kcyDPgShXKSDiiaQgMSwgZWxpbWluYXRpbmcgZXhwbG9zaW9uIGF0IHRoZSBzb3VyY2UuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Exploding Gradients — Clipping Strategies

Exploding gradients are the opposite of vanishing: when the spectral radius of each Jacobian exceeds 1, the product of Jacobians grows exponentially with depth or sequence length. RNNs are especially vulnerable because the same weight matrix W is multiplied at every time step — the effective depth equals the sequence length, which can be hundreds or thousands. Symptoms include NaN loss, diverging training curves, and sudden gradient norm spikes.

Two main clipping strategies exist: value clipping (per-element) and norm clipping (global scale). Norm clipping is the standard for large language models. Exploding gradients are distinct from vanishing — both can coexist in the same network when early layers vanish and late layers explode, a common pathology in very deep networks without residual connections.

## Mathematical Cause — RNN Gradient Explosion

In an RNN, hₜ = tanh(Whₜ₋₁ + Uxₜ). By the chain rule, ∂hₜ/∂h₀ = Πₖ₌₁ᵗ diag(tanh'(·)) · W. If ρ(W) > 1, then ‖∂hₜ/∂h₀‖ grows as ρ(W)ᵀ. For ρ(W) = 1.1 and T=100, gradient magnitude reaches 1.1¹⁰⁰ ≈ 13,780. Even modest spectral radii above 1 produce catastrophic explosion over long sequences.

```python
import torch
import torch.nn as nn

def simulate_explosion(seq_len=50, hidden=32, spectral_radius=1.1, seed=0):
    torch.manual_seed(seed)
    rnn = nn.RNNCell(hidden, hidden, nonlinearity='tanh')
    with torch.no_grad():
        U, S, V = torch.linalg.svd(rnn.weight_hh)
        rnn.weight_hh.data = (U * (S * spectral_radius / S[0]).unsqueeze(0)) @ V
    h = torch.zeros(1, hidden, requires_grad=True)
    h_curr = h
    for t in range(seq_len):
        h_curr = rnn(torch.randn(1, hidden), h_curr)
    h_curr.mean().backward()
    print(f'rho={spectral_radius}, T={seq_len}: grad norm={h.grad.norm():.3e}, expected~{spectral_radius**seq_len:.3e}')

simulate_explosion(seq_len=30, spectral_radius=1.05)
simulate_explosion(seq_len=30, spectral_radius=1.20)
```

## Value Clipping vs Norm Clipping

Value clipping clips each gradient element independently: gᵢ ← clip(gᵢ, −c, c). This changes the gradient direction — relative magnitudes across parameters are altered. Norm clipping rescales the entire gradient: if ‖g‖ > c, then g ← g · c/‖g‖. This preserves direction while bounding magnitude. Norm clipping is the standard in LLM training — GPT, T5, LLaMA all use max_norm=1.0.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def compare_clipping(clip_val=1.0):
    torch.manual_seed(7)
    model = nn.Linear(10, 10)
    (model(torch.randn(4, 10)) * 100).mean().backward()
    g_orig = model.weight.grad.clone()
    orig_dir = F.normalize(g_orig.flatten(), dim=0)

    model.weight.grad.data = g_orig.clone()
    torch.nn.utils.clip_grad_value_(model.parameters(), clip_value=clip_val)
    cos_value = (orig_dir * F.normalize(model.weight.grad.flatten(), dim=0)).sum().item()

    model.weight.grad.data = g_orig.clone()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=clip_val)
    cos_norm  = (orig_dir * F.normalize(model.weight.grad.flatten(), dim=0)).sum().item()

    print(f'Original norm: {g_orig.norm():.4f}')
    print(f'Value clip cosine sim: {cos_value:.6f}')
    print(f'Norm  clip cosine sim: {cos_norm:.6f}')
    print('Norm clipping preserves direction (cos≈1); value clipping distorts it.')

compare_clipping()
```

## Gradient Norm Monitoring During Training

Logging the pre-clip gradient norm every step is the primary health metric for deep network training. A healthy norm stays in a stable range; spikes indicate instability. If more than 30% of steps require clipping, the learning rate is too high. If gradient norms are consistently near zero in early layers, vanishing is the issue — clipping cannot fix vanishing gradients.

```python
import torch
import torch.nn as nn
import numpy as np

def train_with_grad_monitoring(n_steps=200, clip=1.0, seed=0):
    torch.manual_seed(seed)
    model = nn.Sequential(
        nn.Linear(64, 256), nn.Tanh(),
        nn.Linear(256, 256), nn.Tanh(),
        nn.Linear(256, 10)
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    grad_norms, clipped = [], 0
    for step in range(n_steps):
        x, y = torch.randn(32, 64), torch.randint(0, 10, (32,))
        nn.CrossEntropyLoss()(model(x), y).backward()
        total_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=clip)
        grad_norms.append(total_norm.item())
        if total_norm.item() > clip: clipped += 1
        optimizer.step(); optimizer.zero_grad()
    print(f'Clip={clip}: {clipped}/{n_steps} steps clipped ({100*clipped/n_steps:.1f}%)')
    print(f'Grad norm: mean={np.mean(grad_norms):.4f} max={np.max(grad_norms):.4f}')

train_with_grad_monitoring(clip=1.0)
```

## Gradient Accumulation with Correct Clipping

Gradient accumulation simulates a larger effective batch size by accumulating gradients over multiple micro-steps before calling optimizer.step(). The critical rule: clip after all micro-steps, never before. Clipping each micro-batch independently applies multiple clipping operations and the final gradient does not correspond to a single clipped global gradient. Scale the loss by 1/accum_steps before backward to normalize the accumulated gradient.

```python
import torch
import torch.nn as nn

def train_with_accumulation(accum_steps=4, clip=1.0, n_iters=50):
    torch.manual_seed(0)
    model = nn.Sequential(nn.Linear(32, 64), nn.ReLU(), nn.Linear(64, 4))
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    for step in range(n_iters):
        optimizer.zero_grad()
        total_loss = 0.0
        for _ in range(accum_steps):
            x = torch.randn(8, 32)
            y = torch.randint(0, 4, (8,))
            loss = criterion(model(x), y) / accum_steps
            loss.backward()
            total_loss += loss.item()
        grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=clip)
        optimizer.step()
        if step % 10 == 0:
            print(f'Step {step:3d}: loss={total_loss:.4f} grad_norm={grad_norm:.4f}')

train_with_accumulation()
```

## LR Warmup and Spectral Normalization

Learning rate warmup linearly increases LR from 0 to the target over the first few hundred steps. At the start of training, parameters are randomly initialized and gradients can be large and inconsistent. A small initial LR prevents early gradient explosions before the optimizer accumulates stable momentum estimates. LR warmup is complementary to clipping — clipping is a safety net while warmup prevents the problem from occurring.

Spectral normalization (Miyato 2018) constrains the spectral radius of each weight matrix to be ≤ 1 by dividing by the top singular value: W_sn = W/σ₁(W). This eliminates gradient explosion at the source. Used in GANs (discriminator stabilization) and some transformer variants as an alternative to clipping.

## Strategy Comparison

> **LLM Training Standard**: All major LLM training recipes (GPT-3, LLaMA, Mistral) use global norm clipping with max_norm=1.0, applied after gradient accumulation and before optimizer.step(). Log the pre-clip norm to W&B every step — sustained norms above 5× the clip threshold indicate architecture or LR issues that clipping alone cannot fix.

| Strategy | Direction preserved | LLM standard | When to use |
| --- | --- | --- | --- |
| Value clipping (clip_grad_value_) | No — distorted | No | Simple RNNs, legacy code |
| Norm clipping (clip_grad_norm_) | Yes — only scale changes | Yes (max_norm=1.0) | Default for all modern deep networks |
| Adaptive per-layer norm clipping | Yes | Rare | Heterogeneous architectures |
| Spectral normalization | N/A — prevents explosion | No | GANs, when stability is critical |
| No clipping | N/A | No | Only when spectral norm guarantees bounded gradients |

- Log grad_norm before clipping every step — sudden spikes are early warning of instability.
- LR warmup complements clipping: small initial LR reduces early gradient explosion risk.
- If >30% of steps are clipped, reduce learning rate — clipping is a safety net, not a substitute for LR tuning.
- With gradient accumulation, clip once after all micro-steps, not per micro-step.
- Spectral normalization on weight matrices bounds ρ(W) ≤ 1, eliminating explosion at the source.

---

