---
title: "GP Posterior — Conditioning on Observations"
slug: "gp-posterior-predictive"
description: "Deriving the GP posterior by conditioning a joint Gaussian on noisy observations: closed-form mean and covariance, uncertainty calibration, and GPyTorch implementation."
tags: ["gaussian-processes", "kernel-methods", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZyb20gUHJpb3IgdG8gUG9zdGVyaW9yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHaXZlbiB0cmFpbmluZyBvYnNlcnZhdGlvbnMgeSA9IGYoWCkgKyDOtSB3aGVyZSDOtSB+IE4oMCwgz4PCsl9uIEkpLCB0aGUgR1AgcG9zdGVyaW9yIG92ZXIgZnVuY3Rpb24gdmFsdWVzIGF0IHRlc3QgcG9pbnRzIFgqIGlzIGFnYWluIGEgR1AuIFRoaXMgaXMgdGhlIGtleSB0cmFjdGFiaWxpdHkgcHJvcGVydHkgb2YgR1BzOiBHYXVzc2lhbiBsaWtlbGlob29kcyBjb21iaW5lZCB3aXRoIGEgR1AgcHJpb3IgeWllbGQgYSBHUCBwb3N0ZXJpb3IuIFRoZSBwb3N0ZXJpb3IgbWVhbiBpcyB0aGUgYmVzdCBwb2ludCBlc3RpbWF0ZTsgdGhlIHBvc3RlcmlvciB2YXJpYW5jZSBxdWFudGlmaWVzIHByZWRpY3Rpb24gdW5jZXJ0YWludHkuIEJvdGggYXJlIGF2YWlsYWJsZSBpbiBjbG9zZWQgZm9ybSwgd2l0aCBubyBzYW1wbGluZyByZXF1aXJlZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdhdXNzaWFuIGxpa2VsaWhvb2QgcCh5fGYpID0gTih5fGYsIM+DwrJfbkkpIHByZXNlcnZlcyBHUCBjb25qdWdhY3kiLCJQb3N0ZXJpb3IgaXMgR1A6IGYqfFgseSxYKiB+IEdQKM68KiwgzqMqKSIsIlBvc3RlcmlvciBtZWFuIM68KjogYmVzdCBsaW5lYXIgdW5iaWFzZWQgcHJlZGljdG9yIG9mIGYoWCopIiwiUG9zdGVyaW9yIGNvdmFyaWFuY2UgzqMqOiBxdWFudGlmaWVzIHJlbWFpbmluZyB1bmNlcnRhaW50eSBhZnRlciBjb25kaXRpb25pbmciLCJDbG9zZWQtZm9ybSBzb2x1dGlvbiDigJQgbm8gTUNNQyBvciB2YXJpYXRpb25hbCBhcHByb3hpbWF0aW9uIG5lZWRlZCBmb3IgR2F1c3NpYW4gbGlrZWxpaG9vZCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQb3N0ZXJpb3IgRGVyaXZhdGlvbiB2aWEgSm9pbnQgR2F1c3NpYW4gQ29uZGl0aW9uaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgam9pbnQgZGlzdHJpYnV0aW9uIG9mIHRyYWluaW5nIG91dHB1dHMgeSBhbmQgdGVzdCBmdW5jdGlvbiB2YWx1ZXMgZiogaXMgR2F1c3NpYW46IFt5LCBmKl3htYAgfiBOKDAsIFtbSyArIM+DwrJfbiBJLCBLKuG1gF0sIFtLKiwgSyoqXV0pLiBBcHBseWluZyB0aGUgR2F1c3NpYW4gY29uZGl0aW9uaW5nIGZvcm11bGEgZ2l2ZXM6IHBvc3RlcmlvciBtZWFuIM68KiA9IEsq4bWAIChLICsgz4PCsl9uIEkp4oG7wrkgeSBhbmQgcG9zdGVyaW9yIGNvdmFyaWFuY2UgzqMqID0gSyoqIOKIkiBLKuG1gCAoSyArIM+DwrJfbiBJKeKBu8K5IEsqLiBIZXJlIEsgPSBrKFgsWCkgaXMgdGhlIG7Dl24gdHJhaW5pbmcga2VybmVsIG1hdHJpeCwgSyogPSBrKFgsWCopIGlzIG7Dl24qIGNyb3NzLWNvdmFyaWFuY2UsIGFuZCBLKiogPSBrKFgqLFgqKSBpcyB0aGUgbirDl24qIHRlc3Qga2VybmVsIG1hdHJpeC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgZWxsPTEuMCwgc2YyPTEuMCk6XG4gICAgWDEgPSBucC5hdGxlYXN0XzJkKFgxKS5yZXNoYXBlKC0xLDEpXG4gICAgWDIgPSBucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLDEpXG4gICAgcmV0dXJuIHNmMiAqIG5wLmV4cCgtMC41KihYMSAtIFgyLlQpKioyIC8gZWxsKioyKVxuXG5kZWYgZ3BfcG9zdGVyaW9yKFhfdHJhaW4sIHlfdHJhaW4sIFhfdGVzdCwgZWxsPTEuMCwgc2YyPTEuMCwgbm9pc2VfdmFyPTAuMSk6XG4gICAgbiA9IGxlbihYX3RyYWluKVxuICAgIEsgICAgPSByYmZfa2VybmVsKFhfdHJhaW4sIFhfdHJhaW4sIGVsbCwgc2YyKSArIG5vaXNlX3ZhcipucC5leWUobilcbiAgICBLX3MgID0gcmJmX2tlcm5lbChYX3RyYWluLCBYX3Rlc3QsICBlbGwsIHNmMikgICAjIG4geCBuKlxuICAgIEtfc3MgPSByYmZfa2VybmVsKFhfdGVzdCwgIFhfdGVzdCwgIGVsbCwgc2YyKSAgICMgbiogeCBuKlxuICAgIEwgICAgPSBucC5saW5hbGcuY2hvbGVza3koSylcbiAgICBhbHBoYSA9IG5wLmxpbmFsZy5zb2x2ZShMLlQsIG5wLmxpbmFsZy5zb2x2ZShMLCB5X3RyYWluKSkgICMgKEspXnstMX0geVxuICAgIG11ICAgPSBLX3MuVCBAIGFscGhhXG4gICAgdiAgICA9IG5wLmxpbmFsZy5zb2x2ZShMLCBLX3MpXG4gICAgY292ICA9IEtfc3MgLSB2LlQgQCB2XG4gICAgcmV0dXJuIG11LCBucC5kaWFnKGNvdilcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YX3RyYWluID0gbnAuYXJyYXkoWy00LCAtMiwgMCwgMiwgNF0sIGR0eXBlPWZsb2F0KVxueV90cmFpbiA9IG5wLnNpbihYX3RyYWluKSArIDAuMSpucC5yYW5kb20ucmFuZG4obGVuKFhfdHJhaW4pKVxuWF90ZXN0ICA9IG5wLmxpbnNwYWNlKC02LCA2LCAyMDApXG5tdSwgdmFyID0gZ3BfcG9zdGVyaW9yKFhfdHJhaW4sIHlfdHJhaW4sIFhfdGVzdCwgZWxsPTEuNSwgc2YyPTEuMCwgbm9pc2VfdmFyPTAuMDUpXG5zdGQgPSBucC5zcXJ0KHZhcilcblxucGx0LmZpZ3VyZShmaWdzaXplPSgxMCw0KSlcbnBsdC5maWxsX2JldHdlZW4oWF90ZXN0LCBtdS0yKnN0ZCwgbXUrMipzdGQsIGFscGhhPTAuMjUsIGxhYmVsPVx1MDAyN8KxMs+DXHUwMDI3KVxucGx0LnBsb3QoWF90ZXN0LCBtdSwgXHUwMDI3Yi1cdTAwMjcsIGx3PTIsIGxhYmVsPVx1MDAyN1Bvc3RlcmlvciBtZWFuXHUwMDI3KVxucGx0LnNjYXR0ZXIoWF90cmFpbiwgeV90cmFpbiwgYz1cdTAwMjdyXHUwMDI3LCB6b3JkZXI9NSwgcz02MCwgbGFiZWw9XHUwMDI3T2JzZXJ2YXRpb25zXHUwMDI3KVxucGx0LmxlZ2VuZCgpOyBwbHQudGl0bGUoXHUwMDI3R1AgUG9zdGVyaW9yIChSQkYsIOKEkz0xLjUpXHUwMDI3KVxucGx0LnhsYWJlbChcdTAwMjd4XHUwMDI3KTsgcGx0LnlsYWJlbChcdTAwMjdmKHgpXHUwMDI3KTsgcGx0LnRpZ2h0X2xheW91dCgpOyBwbHQuc2hvdygpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1hdHJpeCIsIlNoYXBlIiwiRm9ybXVsYSIsIkludGVycHJldGF0aW9uIl0sInJvd3MiOltbIksiLCJuIMOXIG4iLCJrKFgsWCkgKyDPg8KyX24gSSIsIk5vaXN5IHRyYWluaW5nIGNvdmFyaWFuY2Ug4oCUIGludmVydGVkIG9uY2UgYXQgY29zdCBPKG7CsykiXSxbIksqIiwibiDDlyBuKiIsImsoWCxYKikiLCJDcm9zcy1jb3ZhcmlhbmNlOiBob3cgdHJhaW5pbmcgcG9pbnRzIGluZm9ybSB0ZXN0IHBvaW50cyJdLFsiSyoqIiwibiogw5cgbioiLCJrKFgqLFgqKSIsIlByaW9yIHRlc3QgY292YXJpYW5jZSBiZWZvcmUgY29uZGl0aW9uaW5nIl0sWyJQb3N0ZXJpb3IgbWVhbiIsIm4qIMOXIDEiLCJLKuG1gCAoSyvPg8KyX25JKeKBu8K5IHkiLCJXZWlnaHRlZCBjb21iaW5hdGlvbiBvZiBrZXJuZWwgZXZhbHVhdGlvbnMgKHJlcHJlc2VudGVyIHRoZW9yZW0pIl0sWyJQb3N0ZXJpb3IgY292Iiwibiogw5cgbioiLCJLKiog4oiSIEsq4bWAIChLK8+DwrJfbkkp4oG7wrkgSyoiLCJQcmlvciB2YXJpYW5jZSBtaW51cyBpbmZvcm1hdGlvbiBnYWluZWQgZnJvbSBvYnNlcnZhdGlvbnMiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdQeVRvcmNoIEV4YWN0R1Agd2l0aCBDb25maWRlbmNlIEJhbmRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHUHlUb3JjaCBpbXBsZW1lbnRzIEdQIGluZmVyZW5jZSB1c2luZyBlZmZpY2llbnQgbGluZWFyIGFsZ2VicmEgKENvbmp1Z2F0ZSBHcmFkaWVudHMsIGxvdy1yYW5rIGFwcHJveGltYXRpb25zKS4gRXhhY3RHUCBpcyB0aGUgc3RhbmRhcmQgY2xhc3MgZm9yIGV4YWN0IGluZmVyZW5jZS4gQWZ0ZXIgdHJhaW5pbmcgKG9wdGltaXNpbmcgaHlwZXJwYXJhbWV0ZXJzIHZpYSBtYXJnaW5hbCBsaWtlbGlob29kKSwgY2FsbGluZyBtb2RlbChYX3Rlc3QpIHJldHVybnMgYSBNdWx0aXZhcmlhdGVOb3JtYWwgd2hvc2UgbWVhbiBhbmQgdmFyaWFuY2UgYXJlIHRoZSBwb3N0ZXJpb3IgcHJlZGljdGl2ZSBxdWFudGl0aWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBncHl0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmNsYXNzIEV4YWN0R1BNb2RlbChncHl0b3JjaC5tb2RlbHMuRXhhY3RHUCk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpXG4gICAgICAgIHNlbGYubWVhbl9tb2R1bGUgPSBncHl0b3JjaC5tZWFucy5Db25zdGFudE1lYW4oKVxuICAgICAgICBzZWxmLmNvdmFyX21vZHVsZSA9IGdweXRvcmNoLmtlcm5lbHMuU2NhbGVLZXJuZWwoXG4gICAgICAgICAgICBncHl0b3JjaC5rZXJuZWxzLlJCRktlcm5lbCgpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG1lYW5feCAgPSBzZWxmLm1lYW5fbW9kdWxlKHgpXG4gICAgICAgIGNvdmFyX3ggPSBzZWxmLmNvdmFyX21vZHVsZSh4KVxuICAgICAgICByZXR1cm4gZ3B5dG9yY2guZGlzdHJpYnV0aW9ucy5NdWx0aXZhcmlhdGVOb3JtYWwobWVhbl94LCBjb3Zhcl94KVxuXG50cmFpbl94ID0gdG9yY2gubGluc3BhY2UoLTQsIDQsIDIwKVxudHJhaW5feSA9IHRvcmNoLnNpbih0cmFpbl94KSArIDAuMSp0b3JjaC5yYW5kbl9saWtlKHRyYWluX3gpXG5cbmxpa2VsaWhvb2QgPSBncHl0b3JjaC5saWtlbGlob29kcy5HYXVzc2lhbkxpa2VsaWhvb2QoKVxubW9kZWwgPSBFeGFjdEdQTW9kZWwodHJhaW5feCwgdHJhaW5feSwgbGlrZWxpaG9vZClcblxubW9kZWwudHJhaW4oKTsgbGlrZWxpaG9vZC50cmFpbigpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MC4xKVxubWxsID0gZ3B5dG9yY2gubWxscy5FeGFjdE1hcmdpbmFsTG9nTGlrZWxpaG9vZChsaWtlbGlob29kLCBtb2RlbClcbmZvciBpIGluIHJhbmdlKDEwMCk6XG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgb3V0cHV0ID0gbW9kZWwodHJhaW5feClcbiAgICBsb3NzID0gLW1sbChvdXRwdXQsIHRyYWluX3kpXG4gICAgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG5cbm1vZGVsLmV2YWwoKTsgbGlrZWxpaG9vZC5ldmFsKClcbnRlc3RfeCA9IHRvcmNoLmxpbnNwYWNlKC02LCA2LCAyMDApXG53aXRoIHRvcmNoLm5vX2dyYWQoKSwgZ3B5dG9yY2guc2V0dGluZ3MuZmFzdF9wcmVkX3ZhcigpOlxuICAgIHByZWQgPSBsaWtlbGlob29kKG1vZGVsKHRlc3RfeCkpXG4gICAgbG93ZXIsIHVwcGVyID0gcHJlZC5jb25maWRlbmNlX3JlZ2lvbigpXG5cbnBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsNCkpXG5wbHQuZmlsbF9iZXR3ZWVuKHRlc3RfeC5udW1weSgpLCBsb3dlci5udW1weSgpLCB1cHBlci5udW1weSgpLCBhbHBoYT0wLjI1KVxucGx0LnBsb3QodGVzdF94Lm51bXB5KCksIHByZWQubWVhbi5udW1weSgpLCBsdz0yKVxucGx0LnNjYXR0ZXIodHJhaW5feC5udW1weSgpLCB0cmFpbl95Lm51bXB5KCksIGM9XHUwMDI3clx1MDAyNywgcz01MCwgem9yZGVyPTUpXG5wbHQudGl0bGUoXHUwMDI3R1B5VG9yY2ggRXhhY3RHUCBQb3N0ZXJpb3JcdTAwMjcpOyBwbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQb3N0ZXJpb3IgVmFyaWFuY2U6IE5lYXIgYW5kIEZhciBmcm9tIERhdGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEga2V5IEdQIHByb3BlcnR5IGlzIGF1dG9tYXRpYyB1bmNlcnRhaW50eSBjYWxpYnJhdGlvbi4gUG9zdGVyaW9yIHZhcmlhbmNlIGF0IGEgdGVzdCBwb2ludCB4KiBlcXVhbHMgSyh4Kix4KikgbWludXMgdGhlIGFtb3VudCBvZiB2YXJpYW5jZSBleHBsYWluZWQgYnkgdGhlIHRyYWluaW5nIG9ic2VydmF0aW9ucy4gTmVhciB0cmFpbmluZyBwb2ludHMsIHRoZSBzZWNvbmQgdGVybSBpcyBsYXJnZSDigJQgcG9zdGVyaW9yIHZhcmlhbmNlIGlzIHNtYWxsIChoaWdoIGNvbmZpZGVuY2UpLiBGYXIgZnJvbSBhbGwgdHJhaW5pbmcgcG9pbnRzLCB0aGUgc3VidHJhY3RlZCB0ZXJtIGFwcHJvYWNoZXMgMCBhbmQgdGhlIHBvc3RlcmlvciB2YXJpYW5jZSByZXR1cm5zIHRvIHRoZSBwcmlvciB2YXJpYW5jZSDPg8KyX2YuIFRoaXMgYmVoYXZpb3VyIHJlcXVpcmVzIG5vIG1hbnVhbCB0dW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcmJmX2tlcm5lbChYMSwgWDIsIGVsbD0xLjAsIHNmMj0xLjApOlxuICAgIFgxID0gbnAuYXRsZWFzdF8yZChYMSkucmVzaGFwZSgtMSwxKVxuICAgIFgyID0gbnAuYXRsZWFzdF8yZChYMikucmVzaGFwZSgtMSwxKVxuICAgIHJldHVybiBzZjIgKiBucC5leHAoLTAuNSooWDEtWDIuVCkqKjIvZWxsKioyKVxuXG5kZWYgZ3BfcG9zdGVyaW9yX3ZhcihYX3RyYWluLCBYX3Rlc3QsIGVsbCwgc2YyLCBub2lzZV92YXIpOlxuICAgIEsgICAgPSByYmZfa2VybmVsKFhfdHJhaW4sIFhfdHJhaW4sIGVsbCwgc2YyKSArIG5vaXNlX3ZhcipucC5leWUobGVuKFhfdHJhaW4pKVxuICAgIEtfcyAgPSByYmZfa2VybmVsKFhfdHJhaW4sIFhfdGVzdCwgZWxsLCBzZjIpXG4gICAgS19zcyA9IHJiZl9rZXJuZWwoWF90ZXN0LCAgWF90ZXN0LCBlbGwsIHNmMilcbiAgICBMICAgID0gbnAubGluYWxnLmNob2xlc2t5KEspXG4gICAgdiAgICA9IG5wLmxpbmFsZy5zb2x2ZShMLCBLX3MpXG4gICAgcmV0dXJuIG5wLmRpYWcoS19zcyAtIHYuVEB2KVxuXG5YX3RyYWluID0gbnAuYXJyYXkoWy0zLCAtMSwgMSwgM10sIGR0eXBlPWZsb2F0KVxuWF90ZXN0ICA9IG5wLmxpbnNwYWNlKC02LCA2LCAzMDApXG52YXIgPSBncF9wb3N0ZXJpb3JfdmFyKFhfdHJhaW4sIFhfdGVzdCwgZWxsPTEuMCwgc2YyPTEuMCwgbm9pc2VfdmFyPTAuMDEpXG5cbnBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsMykpXG5wbHQucGxvdChYX3Rlc3QsIHZhciwgbHc9MiwgY29sb3I9XHUwMDI3ZGFya29yYW5nZVx1MDAyNywgbGFiZWw9XHUwMDI3UG9zdGVyaW9yIHZhcmlhbmNlXHUwMDI3KVxucGx0LmF4aGxpbmUoMS4wLCBscz1cdTAwMjctLVx1MDAyNywgY29sb3I9XHUwMDI3Z3JheVx1MDAyNywgbGFiZWw9XHUwMDI3UHJpb3IgdmFyaWFuY2Ugz4PCsl9mPTFcdTAwMjcpXG5mb3IgeHAgaW4gWF90cmFpbjpcbiAgICBwbHQuYXh2bGluZSh4cCwgbHM9XHUwMDI3Olx1MDAyNywgY29sb3I9XHUwMDI3c3RlZWxibHVlXHUwMDI3LCBhbHBoYT0wLjYpXG5wbHQuZmlsbF9iZXR3ZWVuKFhfdGVzdCwgMCwgdmFyLCBhbHBoYT0wLjIsIGNvbG9yPVx1MDAyN2RhcmtvcmFuZ2VcdTAwMjcpXG5wbHQueGxhYmVsKFx1MDAyN3hcdTAwMjcpOyBwbHQueWxhYmVsKFx1MDAyN1Bvc3RlcmlvciBWYXIoZiopXHUwMDI3KVxucGx0LnRpdGxlKFx1MDAyN1Bvc3RlcmlvciBWYXJpYW5jZTogU2hyaW5rcyBOZWFyIERhdGEsIFJldHVybnMgdG8gUHJpb3IgRmFyIEF3YXlcdTAwMjcpXG5wbHQubGVnZW5kKCk7IHBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5vaXN5IHZzIE5vaXNlbGVzcyBPYnNlcnZhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gbm9pc2UgdmFyaWFuY2Ugz4PCsl9uID0gMCwgdGhlIEdQIGludGVycG9sYXRlcyBleGFjdGx5IHRocm91Z2ggYWxsIHRyYWluaW5nIHBvaW50cyDigJQgdGhlIHBvc3RlcmlvciBtZWFuIHBhc3NlcyB0aHJvdWdoIGV2ZXJ5IG9ic2VydmF0aW9uIGFuZCBwb3N0ZXJpb3IgdmFyaWFuY2UgaXMgZXhhY3RseSAwIGF0IHRyYWluaW5nIGlucHV0cy4gV2l0aCDPg8KyX24gXHUwMDNlIDAgKG5vaXN5IG9ic2VydmF0aW9ucyksIHRoZSBwb3N0ZXJpb3IgbWVhbiBzbW9vdGhzIHRocm91Z2ggdGhlIGRhdGEgcmF0aGVyIHRoYW4gaW50ZXJwb2xhdGluZywgYW5kIHRoZSBwb3N0ZXJpb3IgdmFyaWFuY2UgYXQgdHJhaW5pbmcgaW5wdXRzIGlzIM+DwrJfbiBcdTAwM2UgMC4gTm9pc2VsZXNzIEdQcyBhcmUgbnVtZXJpY2FsbHkgdW5zdGFibGUgKEsgaXMgb25seSBwb3NpdGl2ZSBzZW1pLWRlZmluaXRlKSBhbmQgc2hvdWxkIGFsd2F5cyBpbmNsdWRlIGF0IGxlYXN0IGEgc21hbGwgaml0dGVyIHRlcm0uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcmJmX2tlcm5lbChYMSwgWDIsIGVsbD0xLjAsIHNmMj0xLjApOlxuICAgIFgxID0gbnAuYXRsZWFzdF8yZChYMSkucmVzaGFwZSgtMSwxKVxuICAgIFgyID0gbnAuYXRsZWFzdF8yZChYMikucmVzaGFwZSgtMSwxKVxuICAgIHJldHVybiBzZjIgKiBucC5leHAoLTAuNSooWDEtWDIuVCkqKjIvZWxsKioyKVxuXG5kZWYgZ3BfcG9zdGVyaW9yKFhfdHIsIHlfdHIsIFhfdGUsIGVsbD0xLjAsIHNmMj0xLjAsIG5vaXNlX3Zhcj0wLjEpOlxuICAgIEsgICAgPSByYmZfa2VybmVsKFhfdHIsIFhfdHIsIGVsbCwgc2YyKSArIG5vaXNlX3ZhcipucC5leWUobGVuKFhfdHIpKVxuICAgIEtfcyAgPSByYmZfa2VybmVsKFhfdHIsIFhfdGUsIGVsbCwgc2YyKVxuICAgIEtfc3MgPSByYmZfa2VybmVsKFhfdGUsIFhfdGUsIGVsbCwgc2YyKVxuICAgIEwgICAgPSBucC5saW5hbGcuY2hvbGVza3koSylcbiAgICBhbHBoYSA9IG5wLmxpbmFsZy5zb2x2ZShMLlQsIG5wLmxpbmFsZy5zb2x2ZShMLCB5X3RyKSlcbiAgICBtdSAgID0gS19zLlQgQCBhbHBoYVxuICAgIHYgICAgPSBucC5saW5hbGcuc29sdmUoTCwgS19zKVxuICAgIHJldHVybiBtdSwgbnAuc3FydChucC5tYXhpbXVtKG5wLmRpYWcoS19zcyAtIHYuVEB2KSwgMCkpXG5cbm5wLnJhbmRvbS5zZWVkKDMpXG5YX3RyICA9IG5wLnNvcnQobnAucmFuZG9tLnVuaWZvcm0oLTQsIDQsIDgpKVxueV90ciAgPSBucC5zaW4oWF90cikgKyAwLjMqbnAucmFuZG9tLnJhbmRuKDgpXG5YX3RlICA9IG5wLmxpbnNwYWNlKC01LCA1LCAzMDApXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMyw0KSwgc2hhcmV5PVRydWUpXG5mb3IgYXgsIG5vaXNlLCB0aXRsZSBpbiB6aXAoYXhlcyxcbiAgICBbMWUtNiwgMC4zXSwgW1x1MDAyN05vaXNlbGVzcyAoz4PCsl9u4omIMCkg4oCUIGludGVycG9sYXRpb25cdTAwMjcsIFx1MDAyN05vaXN5ICjPg8KyX249MC4zKSDigJQgc21vb3RoaW5nXHUwMDI3XSk6XG4gICAgbXUsIHN0ZCA9IGdwX3Bvc3RlcmlvcihYX3RyLCB5X3RyLCBYX3RlLCBlbGw9MS4wLCBzZjI9MS4wLCBub2lzZV92YXI9bm9pc2UpXG4gICAgYXguZmlsbF9iZXR3ZWVuKFhfdGUsIG11LTIqc3RkLCBtdSsyKnN0ZCwgYWxwaGE9MC4yNSlcbiAgICBheC5wbG90KFhfdGUsIG11LCBsdz0yKVxuICAgIGF4LnNjYXR0ZXIoWF90ciwgeV90ciwgYz1cdTAwMjdyXHUwMDI3LCB6b3JkZXI9NSwgcz02MClcbiAgICBheC5zZXRfdGl0bGUodGl0bGUpOyBheC5zZXRfeGxhYmVsKFx1MDAyN3hcdTAwMjcpXG5heGVzWzBdLnNldF95bGFiZWwoXHUwMDI3Zih4KVx1MDAyNyk7IHBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQWx3YXlzIEluY2x1ZGUgSml0dGVyIEV2ZW4gZm9yIE5vaXNlbGVzcyBHUHMiLCJjb250ZW50IjoiU2V0dGluZyDPg8KyX24gPSAwIGV4YWN0bHkgY2F1c2VzIHRoZSBrZXJuZWwgbWF0cml4IEsgdG8gYmUgb25seSBwb3NpdGl2ZSBzZW1pLWRlZmluaXRlIHdoZW4gdHJhaW5pbmcgcG9pbnRzIHJlcGVhdCBvciBhcmUgdmVyeSBjbG9zZS4gQWx3YXlzIGFkZCBhIHNtYWxsIGppdHRlciAoMWUtNiB0byAxZS00KSB0byB0aGUgZGlhZ29uYWwgcmVnYXJkbGVzcyBvZiB0aGUgYXNzdW1lZCBub2lzZSBsZXZlbC4gVGhpcyB0aW55IHJlZ3VsYXJpc2F0aW9uIGRvZXMgbm90IGNoYW5nZSBwcmVkaWN0aW9ucyBtZWFuaW5nZnVsbHkgYnV0IHByZXZlbnRzIENob2xlc2t5IGZhaWx1cmVzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTyhuwrMpIEJvdHRsZW5lY2siLCJjb250ZW50IjoiVGhlIENob2xlc2t5IGZhY3RvcmlzYXRpb24gb2YgdGhlIG7Dl24gbWF0cml4IChLICsgz4PCsl9uIEkpIGNvc3RzIE8obsKzKSB0aW1lIGFuZCBPKG7CsikgbWVtb3J5LiBGb3IgbiBcdTAwM2UgNSwwMDAgdGhpcyBiZWNvbWVzIHRoZSBkb21pbmFudCBjb3N0LiBTcGFyc2UgR1AgYXBwcm94aW1hdGlvbnMgKGluZHVjaW5nIHBvaW50cywgRklUQywgU1ZHUCkgcmVkdWNlIHRoZSBjb3N0IHRvIE8obm3CsikgYW5kIE8obcKyKSByZXNwZWN0aXZlbHksIHdoZXJlIG0g4omqIG4gaXMgdGhlIG51bWJlciBvZiBpbmR1Y2luZyBwb2ludHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEdQIHBvc3RlcmlvciBpcyBhbmFseXRpY2FsbHkgdHJhY3RhYmxlIHdoZW4gdGhlIGxpa2VsaWhvb2QgaXMgR2F1c3NpYW46IGNvbmRpdGlvbmluZyB0aGUgam9pbnQgR2F1c3NpYW4gcCh5LCBmKikgb24gdGhlIG9ic2VydmF0aW9ucyB5IHlpZWxkcyBhIGNsb3NlZC1mb3JtIEdhdXNzaWFuIHBvc3RlcmlvciBvdmVyIGYqLiBQb3N0ZXJpb3IgbWVhbiDOvCogPSBLKuG1gChLK8+DwrJfbkkp4oG7wrl5IGlzIGEgd2VpZ2h0ZWQgc3VtIG9mIGtlcm5lbCBldmFsdWF0aW9ucy4gUG9zdGVyaW9yIHZhcmlhbmNlIM6jKiA9IEsqKiDiiJIgSyrhtYAoSyvPg8KyX25JKeKBu8K5Syogc2hyaW5rcyBuZWFyIG9ic2VydmF0aW9ucyBhbmQgcmV0dXJucyB0byBwcmlvciB2YXJpYW5jZSBmYXIgZnJvbSBkYXRhLiBUaGUgTyhuwrMpIGNvc3Qgb2YgaW52ZXJ0aW5nIEsrz4PCsl9uSSBpcyB0aGUgbWFpbiBjb21wdXRhdGlvbmFsIGJvdHRsZW5lY2sgb2YgZXhhY3QgR1AgaW5mZXJlbmNlLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUG9zdGVyaW9yIG1lYW46IHJlcHJlc2VudGVyIHRoZW9yZW0g4oCUIHdlaWdodGVkIGtlcm5lbCBldmFsdWF0aW9ucyBhdCB0cmFpbmluZyBwb2ludHMiLCJQb3N0ZXJpb3IgdmFyaWFuY2U6IHByaW9yIHZhcmlhbmNlIG1pbnVzIGluZm9ybWF0aW9uIGdhaW5lZCBmcm9tIGRhdGEiLCJVbmNlcnRhaW50eSBpcyBhdXRvbWF0aWNhbGx5IGNhbGlicmF0ZWQ6IGhpZ2ggbmVhciBkYXRhLCBsb3cgZmFyIGZyb20gZGF0YSIsIk8obsKzKSBDaG9sZXNreSBsaW1pdHMgZXhhY3QgR1BzIHRvIG4g4omyIDUsMDAwIOKAlCB1c2Ugc3BhcnNlIGFwcHJveGltYXRpb25zIGJleW9uZCB0aGlzIiwiTm9pc2VsZXNzIEdQICjPg8KyX249MCk6IGV4YWN0IGludGVycG9sYXRpb24sIG51bWVyaWNhbGx5IGZyYWdpbGUiLCJHUHlUb3JjaCB1c2VzIENvbmp1Z2F0ZSBHcmFkaWVudHMgdG8gYXZvaWQgZnVsbCBPKG7CsykgQ2hvbGVza3kgaW4gbWFueSByZWdpbWVzIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# GP Posterior — Conditioning on Observations

## From Prior to Posterior

Given training observations y = f(X) + ε where ε ~ N(0, σ²_n I), the GP posterior over function values at test points X* is again a GP. This is the key tractability property of GPs: Gaussian likelihoods combined with a GP prior yield a GP posterior. The posterior mean is the best point estimate; the posterior variance quantifies prediction uncertainty. Both are available in closed form, with no sampling required.

- Gaussian likelihood p(y|f) = N(y|f, σ²_nI) preserves GP conjugacy
- Posterior is GP: f*|X,y,X* ~ GP(μ*, Σ*)
- Posterior mean μ*: best linear unbiased predictor of f(X*)
- Posterior covariance Σ*: quantifies remaining uncertainty after conditioning
- Closed-form solution — no MCMC or variational approximation needed for Gaussian likelihood

## Posterior Derivation via Joint Gaussian Conditioning

The joint distribution of training outputs y and test function values f* is Gaussian: [y, f*]ᵀ ~ N(0, [[K + σ²_n I, K*ᵀ], [K*, K**]]). Applying the Gaussian conditioning formula gives: posterior mean μ* = K*ᵀ (K + σ²_n I)⁻¹ y and posterior covariance Σ* = K** − K*ᵀ (K + σ²_n I)⁻¹ K*. Here K = k(X,X) is the n×n training kernel matrix, K* = k(X,X*) is n×n* cross-covariance, and K** = k(X*,X*) is the n*×n* test kernel matrix.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1 - X2.T)**2 / ell**2)

def gp_posterior(X_train, y_train, X_test, ell=1.0, sf2=1.0, noise_var=0.1):
    n = len(X_train)
    K    = rbf_kernel(X_train, X_train, ell, sf2) + noise_var*np.eye(n)
    K_s  = rbf_kernel(X_train, X_test,  ell, sf2)   # n x n*
    K_ss = rbf_kernel(X_test,  X_test,  ell, sf2)   # n* x n*
    L    = np.linalg.cholesky(K)
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, y_train))  # (K)^{-1} y
    mu   = K_s.T @ alpha
    v    = np.linalg.solve(L, K_s)
    cov  = K_ss - v.T @ v
    return mu, np.diag(cov)

np.random.seed(42)
X_train = np.array([-4, -2, 0, 2, 4], dtype=float)
y_train = np.sin(X_train) + 0.1*np.random.randn(len(X_train))
X_test  = np.linspace(-6, 6, 200)
mu, var = gp_posterior(X_train, y_train, X_test, ell=1.5, sf2=1.0, noise_var=0.05)
std = np.sqrt(var)

plt.figure(figsize=(10,4))
plt.fill_between(X_test, mu-2*std, mu+2*std, alpha=0.25, label='±2σ')
plt.plot(X_test, mu, 'b-', lw=2, label='Posterior mean')
plt.scatter(X_train, y_train, c='r', zorder=5, s=60, label='Observations')
plt.legend(); plt.title('GP Posterior (RBF, ℓ=1.5)')
plt.xlabel('x'); plt.ylabel('f(x)'); plt.tight_layout(); plt.show()
```

| Matrix | Shape | Formula | Interpretation |
| --- | --- | --- | --- |
| K | n × n | k(X,X) + σ²_n I | Noisy training covariance — inverted once at cost O(n³) |
| K* | n × n* | k(X,X*) | Cross-covariance: how training points inform test points |
| K** | n* × n* | k(X*,X*) | Prior test covariance before conditioning |
| Posterior mean | n* × 1 | K*ᵀ (K+σ²_nI)⁻¹ y | Weighted combination of kernel evaluations (representer theorem) |
| Posterior cov | n* × n* | K** − K*ᵀ (K+σ²_nI)⁻¹ K* | Prior variance minus information gained from observations |

## GPyTorch ExactGP with Confidence Bands

GPyTorch implements GP inference using efficient linear algebra (Conjugate Gradients, low-rank approximations). ExactGP is the standard class for exact inference. After training (optimising hyperparameters via marginal likelihood), calling model(X_test) returns a MultivariateNormal whose mean and variance are the posterior predictive quantities.

```python
import torch
import gpytorch
import numpy as np
import matplotlib.pyplot as plt

class ExactGPModel(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood):
        super().__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ConstantMean()
        self.covar_module = gpytorch.kernels.ScaleKernel(
            gpytorch.kernels.RBFKernel())

    def forward(self, x):
        mean_x  = self.mean_module(x)
        covar_x = self.covar_module(x)
        return gpytorch.distributions.MultivariateNormal(mean_x, covar_x)

train_x = torch.linspace(-4, 4, 20)
train_y = torch.sin(train_x) + 0.1*torch.randn_like(train_x)

likelihood = gpytorch.likelihoods.GaussianLikelihood()
model = ExactGPModel(train_x, train_y, likelihood)

model.train(); likelihood.train()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
for i in range(100):
    optimizer.zero_grad()
    output = model(train_x)
    loss = -mll(output, train_y)
    loss.backward(); optimizer.step()

model.eval(); likelihood.eval()
test_x = torch.linspace(-6, 6, 200)
with torch.no_grad(), gpytorch.settings.fast_pred_var():
    pred = likelihood(model(test_x))
    lower, upper = pred.confidence_region()

plt.figure(figsize=(10,4))
plt.fill_between(test_x.numpy(), lower.numpy(), upper.numpy(), alpha=0.25)
plt.plot(test_x.numpy(), pred.mean.numpy(), lw=2)
plt.scatter(train_x.numpy(), train_y.numpy(), c='r', s=50, zorder=5)
plt.title('GPyTorch ExactGP Posterior'); plt.tight_layout(); plt.show()
```

## Posterior Variance: Near and Far from Data

A key GP property is automatic uncertainty calibration. Posterior variance at a test point x* equals K(x*,x*) minus the amount of variance explained by the training observations. Near training points, the second term is large — posterior variance is small (high confidence). Far from all training points, the subtracted term approaches 0 and the posterior variance returns to the prior variance σ²_f. This behaviour requires no manual tuning.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1-X2.T)**2/ell**2)

def gp_posterior_var(X_train, X_test, ell, sf2, noise_var):
    K    = rbf_kernel(X_train, X_train, ell, sf2) + noise_var*np.eye(len(X_train))
    K_s  = rbf_kernel(X_train, X_test, ell, sf2)
    K_ss = rbf_kernel(X_test,  X_test, ell, sf2)
    L    = np.linalg.cholesky(K)
    v    = np.linalg.solve(L, K_s)
    return np.diag(K_ss - v.T@v)

X_train = np.array([-3, -1, 1, 3], dtype=float)
X_test  = np.linspace(-6, 6, 300)
var = gp_posterior_var(X_train, X_test, ell=1.0, sf2=1.0, noise_var=0.01)

plt.figure(figsize=(10,3))
plt.plot(X_test, var, lw=2, color='darkorange', label='Posterior variance')
plt.axhline(1.0, ls='--', color='gray', label='Prior variance σ²_f=1')
for xp in X_train:
    plt.axvline(xp, ls=':', color='steelblue', alpha=0.6)
plt.fill_between(X_test, 0, var, alpha=0.2, color='darkorange')
plt.xlabel('x'); plt.ylabel('Posterior Var(f*)')
plt.title('Posterior Variance: Shrinks Near Data, Returns to Prior Far Away')
plt.legend(); plt.tight_layout(); plt.show()
```

## Noisy vs Noiseless Observations

When noise variance σ²_n = 0, the GP interpolates exactly through all training points — the posterior mean passes through every observation and posterior variance is exactly 0 at training inputs. With σ²_n > 0 (noisy observations), the posterior mean smooths through the data rather than interpolating, and the posterior variance at training inputs is σ²_n > 0. Noiseless GPs are numerically unstable (K is only positive semi-definite) and should always include at least a small jitter term.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1-X2.T)**2/ell**2)

def gp_posterior(X_tr, y_tr, X_te, ell=1.0, sf2=1.0, noise_var=0.1):
    K    = rbf_kernel(X_tr, X_tr, ell, sf2) + noise_var*np.eye(len(X_tr))
    K_s  = rbf_kernel(X_tr, X_te, ell, sf2)
    K_ss = rbf_kernel(X_te, X_te, ell, sf2)
    L    = np.linalg.cholesky(K)
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, y_tr))
    mu   = K_s.T @ alpha
    v    = np.linalg.solve(L, K_s)
    return mu, np.sqrt(np.maximum(np.diag(K_ss - v.T@v), 0))

np.random.seed(3)
X_tr  = np.sort(np.random.uniform(-4, 4, 8))
y_tr  = np.sin(X_tr) + 0.3*np.random.randn(8)
X_te  = np.linspace(-5, 5, 300)

fig, axes = plt.subplots(1, 2, figsize=(13,4), sharey=True)
for ax, noise, title in zip(axes,
    [1e-6, 0.3], ['Noiseless (σ²_n≈0) — interpolation', 'Noisy (σ²_n=0.3) — smoothing']):
    mu, std = gp_posterior(X_tr, y_tr, X_te, ell=1.0, sf2=1.0, noise_var=noise)
    ax.fill_between(X_te, mu-2*std, mu+2*std, alpha=0.25)
    ax.plot(X_te, mu, lw=2)
    ax.scatter(X_tr, y_tr, c='r', zorder=5, s=60)
    ax.set_title(title); ax.set_xlabel('x')
axes[0].set_ylabel('f(x)'); plt.tight_layout(); plt.show()
```

> **Always Include Jitter Even for Noiseless GPs**: Setting σ²_n = 0 exactly causes the kernel matrix K to be only positive semi-definite when training points repeat or are very close. Always add a small jitter (1e-6 to 1e-4) to the diagonal regardless of the assumed noise level. This tiny regularisation does not change predictions meaningfully but prevents Cholesky failures.

> **O(n³) Bottleneck**: The Cholesky factorisation of the n×n matrix (K + σ²_n I) costs O(n³) time and O(n²) memory. For n > 5,000 this becomes the dominant cost. Sparse GP approximations (inducing points, FITC, SVGP) reduce the cost to O(nm²) and O(m²) respectively, where m ≪ n is the number of inducing points.

## Key Takeaways

The GP posterior is analytically tractable when the likelihood is Gaussian: conditioning the joint Gaussian p(y, f*) on the observations y yields a closed-form Gaussian posterior over f*. Posterior mean μ* = K*ᵀ(K+σ²_nI)⁻¹y is a weighted sum of kernel evaluations. Posterior variance Σ* = K** − K*ᵀ(K+σ²_nI)⁻¹K* shrinks near observations and returns to prior variance far from data. The O(n³) cost of inverting K+σ²_nI is the main computational bottleneck of exact GP inference.

- Posterior mean: representer theorem — weighted kernel evaluations at training points
- Posterior variance: prior variance minus information gained from data
- Uncertainty is automatically calibrated: high near data, low far from data
- O(n³) Cholesky limits exact GPs to n ≲ 5,000 — use sparse approximations beyond this
- Noiseless GP (σ²_n=0): exact interpolation, numerically fragile
- GPyTorch uses Conjugate Gradients to avoid full O(n³) Cholesky in many regimes

---

