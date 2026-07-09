---
title: "KL Divergence — Asymmetry and Forward vs Reverse"
slug: "kl-divergence"
description: "KL divergence KL(P‖Q) measures the information cost of using model Q to encode data from P. Covers non-negativity via Jensen's inequality, the critical asymmetry, forward (inclusive) vs reverse (mode-seeking) KL, applications in VAEs, MLE, RLHF, and variational inference."
tags: ["information-theory", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiS3VsbGJhY2stTGVpYmxlciBkaXZlcmdlbmNlIGlzIG9uZSBvZiB0aGUgbW9zdCBpbXBvcnRhbnQgcXVhbnRpdGllcyBpbiBzdGF0aXN0aWNzLCBpbmZvcm1hdGlvbiB0aGVvcnksIGFuZCBtYWNoaW5lIGxlYXJuaW5nLiBJdCBtZWFzdXJlcyBob3cgbXVjaCBvbmUgcHJvYmFiaWxpdHkgZGlzdHJpYnV0aW9uIGRpZmZlcnMgZnJvbSBhbm90aGVyLCBhbmQgaXRzIGFzeW1tZXRyeSDigJQgS0woUOKAllEpIOKJoCBLTChR4oCWUCkgaW4gZ2VuZXJhbCDigJQgaXMgbm90IGEgYnVnIGJ1dCBhIGZlYXR1cmU6IGVhY2ggZGlyZWN0aW9uIGNhcHR1cmVzIGZ1bmRhbWVudGFsbHkgZGlmZmVyZW50IGJlaGF2aW91ciB3aGVuIGFwcHJveGltYXRpbmcgZGlzdHJpYnV0aW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZWZpbml0aW9uIGFuZCBOb24tTmVnYXRpdml0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGRpc2NyZXRlIGRpc3RyaWJ1dGlvbnMgUCBhbmQgUSBvdmVyIHRoZSBzYW1lIHN1cHBvcnQsIEtMKFDigJZRKSA9IM6jX3ggcCh4KSBsb2cocCh4KS9xKHgpKS4gVGhpcyBjYW4gYmUgcmVhZCBhcyB0aGUgZXh0cmEgYml0cyBwZXIgc3ltYm9sIHdoZW4gZW5jb2RpbmcgZGF0YSBmcm9tIFAgdXNpbmcgYSBjb2RlIG9wdGltaXplZCBmb3IgUSwgcmF0aGVyIHRoYW4gdGhlIG9wdGltYWwgY29kZSBmb3IgUC4gS0woUOKAllEpIOKJpSAwIGFsd2F5cyAoR2liYnNcdTAwMjcgaW5lcXVhbGl0eSksIHdpdGggZXF1YWxpdHkgaWZmIFAgPSBRIGV2ZXJ5d2hlcmUuIFByb29mOiBieSBKZW5zZW5cdTAwMjdzIGluZXF1YWxpdHkgYXBwbGllZCB0byB0aGUgY29udmV4IGZ1bmN0aW9uIC1sb2csIC1LTChQ4oCWUSkgPSDOoyBwKHgpIGxvZyhxKHgpL3AoeCkpIOKJpCBsb2cgzqMgcCh4KcK3KHEoeCkvcCh4KSkgPSBsb2cgMSA9IDAuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJLTCBJcyBOb3QgYSBEaXN0YW5jZSIsImNvbnRlbnQiOiJLTCBkaXZlcmdlbmNlIGlzIG5vdCBhIG1ldHJpYy4gSXQgdmlvbGF0ZXMgc3ltbWV0cnkgKEtMKFDigJZRKSDiiaAgS0woUeKAllApIGluIGdlbmVyYWwpIGFuZCB0aGUgdHJpYW5nbGUgaW5lcXVhbGl0eS4gSXQgaXMgdW5kZWZpbmVkIHdoZW4gUSh4KT0wIGJ1dCBQKHgpXHUwMDNlMCAodGhlIGNvbnZlbnRpb24gaXMgS0wgPSAr4oieIGluIHRoaXMgY2FzZSkuIFVzZSBKZW5zZW4tU2hhbm5vbiBkaXZlcmdlbmNlIHdoZW4gYSBzeW1tZXRyaWMsIGJvdW5kZWQgbWVhc3VyZSBpcyBuZWVkZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zcGVjaWFsIGltcG9ydCBrbF9kaXZcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IGVudHJvcHkgYXMgc2NpcHlfZW50cm9weVxuXG5kZWYga2xfZGl2ZXJnZW5jZShwLCBxLCBlcHM9MWUtMTIpOlxuICAgIFwiXCJcIlxuICAgIEtMKFDigJZRKSA9IM6jIHAoeCkgbG9nKHAoeCkvcSh4KSkuXG4gICAgUmV0dXJucyAraW5mIGlmIHEoeCk9MCBhbmQgcCh4KVx1MDAzZTAuXG4gICAgXCJcIlwiXG4gICAgcCA9IG5wLmFzYXJyYXkocCwgZHR5cGU9ZmxvYXQpXG4gICAgcSA9IG5wLmFzYXJyYXkocSwgZHR5cGU9ZmxvYXQpXG4gICAgIyBGaW5kIHN1cHBvcnQgd2hlcmUgcCBcdTAwM2UgMFxuICAgIG1hc2sgPSBwIFx1MDAzZSAwXG4gICAgaWYgbnAuYW55KHFbbWFza10gPT0gMCk6XG4gICAgICAgIHJldHVybiBucC5pbmZcbiAgICByZXR1cm4gbnAuc3VtKHBbbWFza10gKiBucC5sb2cocFttYXNrXSAvIChxW21hc2tdICsgZXBzKSkpXG5cbiMgRGVtb25zdHJhdGUgYXN5bW1ldHJ5XG5wID0gbnAuYXJyYXkoWzAuNiwgMC4zLCAwLjFdKVxucSA9IG5wLmFycmF5KFswLjIsIDAuNSwgMC4zXSlcblxua2xfcHEgPSBrbF9kaXZlcmdlbmNlKHAsIHEpXG5rbF9xcCA9IGtsX2RpdmVyZ2VuY2UocSwgcClcblxucHJpbnQoZlwiS0woUOKAllEpID0ge2tsX3BxOi40Zn0gbmF0c1wiKVxucHJpbnQoZlwiS0woUeKAllApID0ge2tsX3FwOi40Zn0gbmF0c1wiKVxucHJpbnQoZlwiQXN5bW1ldHJpYzoge25vdCBucC5pc2Nsb3NlKGtsX3BxLCBrbF9xcCl9XCIpXG5cbiMgVmVyaWZ5IHdpdGggc2NpcHlcbnByaW50KGZcIlNjaXB5IEtMKFDigJZRKSA9IHtzY2lweV9lbnRyb3B5KHAsIHEpOi40Zn0gbmF0cyAgKG1hdGNoZXM6IHtucC5pc2Nsb3NlKGtsX3BxLCBzY2lweV9lbnRyb3B5KHAsIHEpKX0pXCIpXG5cbiMgS0wgPSAwIGlmZiBQID0gUVxucHJpbnQoZlwiXFxuS0woUOKAllApID0ge2tsX2RpdmVyZ2VuY2UocCwgcCk6LjZmfSAgKHNob3VsZCBiZSAwKVwiKVxuXG4jIEtMIGJsb3dzIHVwIHdoZW4gUSBoYXMgemVybyB3aGVyZSBQIGhhcyBtYXNzXG5xX3plcm8gPSBucC5hcnJheShbMC41LCAwLjUsIDAuMF0pXG5wcmludChmXCJLTChQ4oCWUSkgd2hlbiBRIGhhcyB6ZXJvIHdoZXJlIFBcdTAwM2UwOiB7a2xfZGl2ZXJnZW5jZShwLCBxX3plcm8pfVwiKSAgIyBpbmYifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGb3J3YXJkIEtMIHZzIFJldmVyc2UgS0wg4oCUIFRoZSBDcml0aWNhbCBEaWZmZXJlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3J3YXJkIEtMIChhbHNvIGNhbGxlZCBcdTAwMjdpbmNsdXNpdmVcdTAwMjcgb3IgXHUwMDI3SS1wcm9qZWN0aW9uXHUwMDI3KTogbWluaW1pemUgS0wocF90cnVlIOKAliBxX2FwcHJveCkgb3ZlciBxLiBCZWNhdXNlIGxvZyhwL3EpIOKGkiAt4oieIHdoZW4gcSDihpIgMCBidXQgcCBcdTAwM2UgMCwgdGhlIGxvc3MgaXMgaW5maW5pdGUgdW5sZXNzIHEgY292ZXJzIGFsbCBtb2RlcyBvZiBwLiBUaGlzIGZvcmNlcyBxIHRvIGJlIGJyb2FkIOKAlCBpdCBtdXN0IHBsYWNlIG1hc3MgZXZlcnl3aGVyZSB0aGF0IHAgZG9lcywgZXZlbiBpZiBwIGlzIG11bHRpbW9kYWwuIFRoZSByZXN1bHQgaXMgb2Z0ZW4gYSBzbWVhcmVkLW91dCwgbWVhbi1zZWVraW5nIGFwcHJveGltYXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXZlcnNlIEtMIChhbHNvIGNhbGxlZCBcdTAwMjdleGNsdXNpdmVcdTAwMjcgb3IgXHUwMDI3TS1wcm9qZWN0aW9uXHUwMDI3KTogbWluaW1pemUgS0wocV9hcHByb3gg4oCWIHBfdHJ1ZSkgb3ZlciBxLiBCZWNhdXNlIHdlIHdlaWdodCBieSBxLCB3aGVuIHEoeCkg4oaSIDAgdGhlcmUgaXMgbm8gcGVuYWx0eSBldmVuIGlmIHAoeCkgXHUwMDNlIDAuIFRoaXMgYWxsb3dzIHEgdG8gaWdub3JlIG1vZGVzIG9mIHAgZW50aXJlbHkuIFRoZSBvcHRpbWl6ZXIgY29uY2VudHJhdGVzIHEgb24gb25lIG1vZGUgb2YgcCAobW9kZS1zZWVraW5nIGJlaGF2aW91ciksIGZpdHRpbmcgdGhhdCBtb2RlIHdlbGwgd2hpbGUgaWdub3Jpbmcgb3RoZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbiMgVGFyZ2V0OiBiaW1vZGFsIGRpc3RyaWJ1dGlvbiAobWl4dHVyZSBvZiB0d28gR2F1c3NpYW5zIG9uIGRpc2NyZXRlIGdyaWQpXG54ID0gbnAubGluc3BhY2UoLTUsIDUsIDMwMClcbmR4ID0geFsxXSAtIHhbMF1cblxuZGVmIGdhdXNzaWFuKHgsIG11LCBzaWdtYSk6XG4gICAgcmV0dXJuIG5wLmV4cCgtMC41ICogKCh4IC0gbXUpIC8gc2lnbWEpICoqIDIpIC8gKHNpZ21hICogbnAuc3FydCgyICogbnAucGkpKVxuXG4jIFRydWUgZGlzdHJpYnV0aW9uOiBiaW1vZGFsXG5wID0gMC41ICogZ2F1c3NpYW4oeCwgLTIsIDAuNSkgKyAwLjUgKiBnYXVzc2lhbih4LCAyLCAwLjUpXG5wID0gcCAvIChwLnN1bSgpICogZHgpICAjIG5vcm1hbGl6ZVxucF9kaXNjcmV0ZSA9IHAgKiBkeCAgICAjIGRpc2NyZXRlIHByb2JhYmlsaXRpZXNcblxuZGVmIGZpdF9nYXVzc2lhbl9hcHByb3godGFyZ2V0X2tsKTpcbiAgICBcIlwiXCJGaXQgTihtdSwgc2lnbWEpIHRvIGJpbW9kYWwgcCBieSBtaW5pbWl6aW5nIGZvcndhcmQgb3IgcmV2ZXJzZSBLTC5cIlwiXCJcbiAgICBkZWYgZm9yd2FyZF9rbChwYXJhbXMpOiAgIyBLTChwX3RydWUgfHwgcSlcbiAgICAgICAgbXUsIGxvZ19zaWdtYSA9IHBhcmFtc1xuICAgICAgICBzaWdtYSA9IG5wLmV4cChsb2dfc2lnbWEpXG4gICAgICAgIHEgPSBnYXVzc2lhbih4LCBtdSwgc2lnbWEpXG4gICAgICAgIHEgPSBxIC8gKHEuc3VtKCkgKiBkeClcbiAgICAgICAgcV9kID0gcSAqIGR4XG4gICAgICAgIHFfZCA9IG5wLmNsaXAocV9kLCAxZS0xMiwgTm9uZSlcbiAgICAgICAgcmV0dXJuIG5wLnN1bShwX2Rpc2NyZXRlICogbnAubG9nKG5wLmNsaXAocF9kaXNjcmV0ZSwgMWUtMTIsIE5vbmUpIC8gcV9kKSlcblxuICAgIGRlZiByZXZlcnNlX2tsKHBhcmFtcyk6ICAjIEtMKHEgfHwgcF90cnVlKVxuICAgICAgICBtdSwgbG9nX3NpZ21hID0gcGFyYW1zXG4gICAgICAgIHNpZ21hID0gbnAuZXhwKGxvZ19zaWdtYSlcbiAgICAgICAgcSA9IGdhdXNzaWFuKHgsIG11LCBzaWdtYSlcbiAgICAgICAgcSA9IHEgLyAocS5zdW0oKSAqIGR4KVxuICAgICAgICBxX2QgPSBucC5jbGlwKHEgKiBkeCwgMWUtMTIsIE5vbmUpXG4gICAgICAgIHBfZCA9IG5wLmNsaXAocF9kaXNjcmV0ZSwgMWUtMTIsIE5vbmUpXG4gICAgICAgIHJldHVybiBucC5zdW0ocV9kICogbnAubG9nKHFfZCAvIHBfZCkpXG5cbiAgICBvYmogPSBmb3J3YXJkX2tsIGlmIHRhcmdldF9rbCA9PSBcdTAwMjdmb3J3YXJkXHUwMDI3IGVsc2UgcmV2ZXJzZV9rbFxuICAgIHJlc3VsdCA9IG1pbmltaXplKG9iaiwgWzAuMCwgMC4wXSwgbWV0aG9kPVx1MDAyN05lbGRlci1NZWFkXHUwMDI3KVxuICAgIG11LCBsb2dfc2lnbWEgPSByZXN1bHQueFxuICAgIHJldHVybiBtdSwgbnAuZXhwKGxvZ19zaWdtYSlcblxubXVfZndkLCBzaWdfZndkID0gZml0X2dhdXNzaWFuX2FwcHJveChcdTAwMjdmb3J3YXJkXHUwMDI3KVxubXVfcmV2LCBzaWdfcmV2ID0gZml0X2dhdXNzaWFuX2FwcHJveChcdTAwMjdyZXZlcnNlXHUwMDI3KVxuXG5wcmludChmXCJGb3J3YXJkIEtMIGZpdDogIG11PXttdV9md2Q6LjNmfSwgc2lnbWE9e3NpZ19md2Q6LjNmfSAgKG1lYW4tc2Vla2luZywgd2lkZSlcIilcbnByaW50KGZcIlJldmVyc2UgS0wgZml0OiAgbXU9e211X3JldjouM2Z9LCBzaWdtYT17c2lnX3JldjouM2Z9ICAobW9kZS1zZWVraW5nLCBuYXJyb3cpXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS0wgaW4gVmFyaWF0aW9uYWwgSW5mZXJlbmNlIGFuZCBWQUVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWYXJpYXRpb25hbCBBdXRvZW5jb2RlcnMgKFZBRXMpIG1pbmltaXplIHRoZSBuZWdhdGl2ZSBFTEJPOiBMID0gRV9xW2xvZyBwKHh8eildIC0gS0wocSh6fHgpIOKAliBwKHopKS4gVGhlIEtMIHRlcm0gaXMgYmV0d2VlbiB0aGUgYXBwcm94aW1hdGUgcG9zdGVyaW9yIHEoenx4KSAoZW5jb2RlcikgYW5kIHRoZSBwcmlvciBwKHopICh0eXBpY2FsbHkgTigwLEkpKS4gVGhpcyBpcyB0aGUgcmV2ZXJzZSBLTCBLTChx4oCWcCksIHdoaWNoIGVuY291cmFnZXMgbW9kZS1zZWVraW5nIGJlaGF2aW91ciDigJQgdGhlIGVuY29kZXIgbGVhcm5zIHRvIGNvbmNlbnRyYXRlIG9uIHNwZWNpZmljIHJlZ2lvbnMgb2YgbGF0ZW50IHNwYWNlIHJhdGhlciB0aGFuIHNwcmVhZGluZyBwcm9iYWJpbGl0eSBtYXNzIGV2ZXJ5d2hlcmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuIyBLTCBkaXZlcmdlbmNlIGJldHdlZW4gdHdvIEdhdXNzaWFuczogY2xvc2VkIGZvcm1cbiMgS0woTihtdTEsIHNpZ21hMV4yKSB8fCBOKG11Miwgc2lnbWEyXjIpKVxuZGVmIGtsX2dhdXNzaWFucyhtdTEsIGxvZ3ZhcjEsIG11Mj0wLjAsIGxvZ3ZhcjI9MC4wKTpcbiAgICBcIlwiXCJcbiAgICBDbG9zZWQtZm9ybSBLTCBiZXR3ZWVuIHR3byBkaWFnb25hbCBHYXVzc2lhbnMuXG4gICAgRGVmYXVsdDogS0wocSB8fCBOKDAsSSkpIHVzZWQgaW4gVkFFIEVMQk8uXG4gICAgXCJcIlwiXG4gICAgdmFyMSA9IHRvcmNoLmV4cChsb2d2YXIxKVxuICAgIHZhcjIgPSB0b3JjaC5leHAodG9yY2gudGVuc29yKGxvZ3ZhcjIpKVxuICAgIGtsID0gMC41ICogKGxvZ3ZhcjIgLSBsb2d2YXIxICsgdmFyMSAvIHZhcjJcbiAgICAgICAgICAgICAgICArIChtdTEgLSBtdTIpICoqIDIgLyB2YXIyIC0gMSlcbiAgICByZXR1cm4ga2wuc3VtKGRpbT0tMSkubWVhbigpXG5cbiMgU2ltdWxhdGUgVkFFIGVuY29kZXIgb3V0cHV0IGZvciBhIGJhdGNoXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbmJhdGNoX3NpemUsIGxhdGVudF9kaW0gPSAzMiwgOFxubXUgICAgID0gdG9yY2gucmFuZG4oYmF0Y2hfc2l6ZSwgbGF0ZW50X2RpbSkgKiAwLjVcbmxvZ3ZhciA9IHRvcmNoLnJhbmRuKGJhdGNoX3NpemUsIGxhdGVudF9kaW0pICogMC4zIC0gMSAgIyBsb2ctdmFyaWFuY2Vcblxua2xfbG9zcyA9IGtsX2dhdXNzaWFucyhtdSwgbG9ndmFyKVxuXG4jIFZBRSByZXBhcmFtZXRlcml6YXRpb24gdHJpY2tcbmVwcyA9IHRvcmNoLnJhbmRuX2xpa2UobXUpXG56ICAgPSBtdSArIHRvcmNoLmV4cCgwLjUgKiBsb2d2YXIpICogZXBzXG5cbiMgUmVjb25zdHJ1Y3Rpb24gbG9zcyBwbGFjZWhvbGRlciAoYXNzdW1lIGJpbmFyeSBpbnB1dClcbnJlY29uX2xvc3MgPSBubi5CQ0VMb3NzKCkodG9yY2guc2lnbW9pZCh6KSwgdG9yY2gucmFuZF9saWtlKHopKVxuXG5lbGJvID0gcmVjb25fbG9zcyArIGtsX2xvc3NcbnByaW50KGZcIlZBRSBFTEJPIGNvbXBvbmVudHMgKGJhdGNoIG9mIHtiYXRjaF9zaXplfSk6XCIpXG5wcmludChmXCIgIFJlY29uc3RydWN0aW9uIGxvc3M6IHtyZWNvbl9sb3NzLml0ZW0oKTouNGZ9XCIpXG5wcmludChmXCIgIEtMKHHigJZwKSBsb3NzOiAgICAgICAge2tsX2xvc3MuaXRlbSgpOi40Zn1cIilcbnByaW50KGZcIiAgVG90YWwgLUVMQk86ICAgICAgICAgIHtlbGJvLml0ZW0oKTouNGZ9XCIpXG5wcmludChmXCIgIFJlcGFyYW1ldGVyaXplZCB6IHNoYXBlOiB7ei5zaGFwZX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLTCBpbiBSTEhGIGFuZCBMYW5ndWFnZSBNb2RlbCBBbGlnbm1lbnQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBIdW1hbiBGZWVkYmFjayAoUkxIRikgdXNlcyBhIEtMIHBlbmFsdHkgdG8ga2VlcCB0aGUgcG9saWN5IM+AX864IGNsb3NlIHRvIGEgcmVmZXJlbmNlIHBvbGljeSDPgF9yZWY6IEwgPSAtRVtyKHgpXSArIM6ywrdLTCjPgF/OuCDigJYgz4BfcmVmKS4gVGhlIEtMIHRlcm0gcHJldmVudHMgdGhlIHBvbGljeSBmcm9tIGRldmlhdGluZyB0b28gZmFyIGZyb20gdGhlIHByZXRyYWluZWQgbW9kZWwgKHJld2FyZCBoYWNraW5nLCBtb2RlIGNvbGxhcHNlKS4gVGhpcyBpcyBhIHJldmVyc2UgS0w6IEtMKM+AX864IOKAliDPgF9yZWYpLCBwZW5hbGl6aW5nIHRoZSBwb2xpY3kgZm9yIHBsYWNpbmcgbWFzcyB3aGVyZSB0aGUgcmVmZXJlbmNlIGhhcyBsb3cgcHJvYmFiaWxpdHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBrbF9wZW5hbHR5X3JsaGYobG9naXRzX3BvbGljeSwgbG9naXRzX3JlZiwgYmV0YT0wLjAxKTpcbiAgICBcIlwiXCJcbiAgICBLTCBwZW5hbHR5IHVzZWQgaW4gUkxIRjogYmV0YSAqIEtMKHBpX3RoZXRhIHx8IHBpX3JlZikuXG4gICAgbG9naXRzX3BvbGljeSwgbG9naXRzX3JlZjogKGJhdGNoLCB2b2NhYl9zaXplKVxuICAgIFwiXCJcIlxuICAgIGxvZ19wID0gRi5sb2dfc29mdG1heChsb2dpdHNfcG9saWN5LCBkaW09LTEpXG4gICAgbG9nX3IgPSBGLmxvZ19zb2Z0bWF4KGxvZ2l0c19yZWYsICAgIGRpbT0tMSlcbiAgICAjIEtMKHBvbGljeSB8fCByZWYpID0gzqMgcCAqIChsb2cgcCAtIGxvZyByKVxuICAgIGtsID0gKGxvZ19wLmV4cCgpICogKGxvZ19wIC0gbG9nX3IpKS5zdW0oZGltPS0xKSAgIyAoYmF0Y2gsKVxuICAgIHJldHVybiBiZXRhICoga2wubWVhbigpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDEpXG5iYXRjaCwgdm9jYWIgPSAxNiwgNTAyNTcgICMgR1BULTIgdm9jYWIgc2l6ZVxuXG4jIFJlZmVyZW5jZSBtb2RlbCAoZnJvemVuKVxubG9naXRzX3JlZiAgICA9IHRvcmNoLnJhbmRuKGJhdGNoLCB2b2NhYilcbiMgUG9saWN5IHNsaWdodGx5IHNoaWZ0ZWQgZnJvbSByZWZlcmVuY2VcbmxvZ2l0c19wb2xpY3kgPSBsb2dpdHNfcmVmICsgdG9yY2gucmFuZG4oYmF0Y2gsIHZvY2FiKSAqIDAuNVxuIyBTdHJvbmdseSBzaGlmdGVkIHBvbGljeSAod291bGQgZ2V0IGxhcmdlIEtMIHBlbmFsdHkpXG5sb2dpdHNfZHJpZnRlZCA9IGxvZ2l0c19yZWYgKyB0b3JjaC5yYW5kbihiYXRjaCwgdm9jYWIpICogMy4wXG5cbmZvciBuYW1lLCBsb2dpdHMgaW4gWyhcImFsaWduZWQgcG9saWN5XCIsIGxvZ2l0c19wb2xpY3kpLFxuICAgICAgICAgICAgICAgICAgICAgKFwiZHJpZnRlZCBwb2xpY3lcIiwgbG9naXRzX2RyaWZ0ZWQpXTpcbiAgICBrbF9wZW4gPSBrbF9wZW5hbHR5X3JsaGYobG9naXRzLCBsb2dpdHNfcmVmLCBiZXRhPTAuMDEpXG4gICAga2xfcmF3ID0ga2xfcGVuYWx0eV9ybGhmKGxvZ2l0cywgbG9naXRzX3JlZiwgYmV0YT0xLjApXG4gICAgcHJpbnQoZlwie25hbWV9OiBLTCA9IHtrbF9yYXcuaXRlbSgpOi40Zn0gbmF0cywgIHBlbmFsdHkgKM6yPTAuMDEpID0ge2tsX3Blbi5pdGVtKCk6LjRmfVwiKSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIktMKFDigJZRKSDigJQgRm9yd2FyZCBLTCIsIktMKFHigJZQKSDigJQgUmV2ZXJzZSBLTCJdLCJyb3dzIjpbWyJBbHNvIGNhbGxlZCIsIkktcHJvamVjdGlvbiwgaW5jbHVzaXZlLCBtZWFuLXNlZWtpbmciLCJNLXByb2plY3Rpb24sIGV4Y2x1c2l2ZSwgbW9kZS1zZWVraW5nIl0sWyJXaGVuIFEoeCk9MCwgUCh4KVx1MDAzZTAiLCJLTCA9ICviiJ4g4oCUIGZvcmNlcyBRIHRvIGNvdmVyIFBcdTAwMjdzIHN1cHBvcnQiLCJObyBwZW5hbHR5IOKAlCBRIGNhbiBpZ25vcmUgbW9kZXMgb2YgUCJdLFsiV2hlbiBQKHgpPTAsIFEoeClcdTAwM2UwIiwiTm8gcGVuYWx0eSDigJQgUSBjYW4gYmUgbm9uemVybyB3aGVyZSBQPTAiLCJLTCA9ICviiJ4gKGlmIGxvZyAwID0gLeKIniBjb252ZW50aW9uKSJdLFsiT3B0aW1pemVyIGJlaGF2aW91ciIsIlEgc3ByZWFkcyB0byBjb3ZlciBhbGwgbW9kZXMgb2YgUCIsIlEgY29uY2VudHJhdGVzIG9uIG9uZSBtb2RlIG9mIFAiXSxbIlVzZWQgaW4iLCJNTEUsIGNyb3NzLWVudHJvcHkgbWluaW1pemF0aW9uIiwiVkFFIGVuY29kZXIsIHZhcmlhdGlvbmFsIGluZmVyZW5jZSwgUkxIRiBLTCBwZW5hbHR5Il0sWyJTdXBwb3J0cyBtdXN0IG1hdGNoPyIsIlllczogUSBtdXN0IGNvdmVyIFBcdTAwMjdzIHN1cHBvcnQiLCJObzogUSBjYW4gaGF2ZSBzbWFsbGVyIHN1cHBvcnQgdGhhbiBQIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJKUyBEaXZlcmdlbmNlIGFuZCBmLURpdmVyZ2VuY2VzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgSmVuc2VuLVNoYW5ub24gZGl2ZXJnZW5jZSBKU0QoUCxRKSA9ICgxLzIpS0woUOKAlk0pICsgKDEvMilLTChR4oCWTSkgd2hlcmUgTT0oUCtRKS8yIGlzIGEgc3ltbWV0cml6ZWQsIGJvdW5kZWQgdmFyaWFudC4gQm90aCBLTCBhbmQgSlNEIGJlbG9uZyB0byB0aGUgZmFtaWx5IG9mIGYtZGl2ZXJnZW5jZXM6IERfZihQ4oCWUSkgPSDOoyBxKHgpIGYocCh4KS9xKHgpKSBmb3IgYSBjb252ZXggZnVuY3Rpb24gZiB3aXRoIGYoMSk9MC4gS0wgdXNlcyBmKHQpID0gdCBsb2cgdDsgcmV2ZXJzZSBLTCB1c2VzIGYodCkgPSAtbG9nIHQ7IEpTRCB1c2VzIGYodCkgPSB0IGxvZygydC8odCsxKSkgKyBsb2coMi8odCsxKSkuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6Ik1MRSA9IE1pbmltaXppbmcgRm9yd2FyZCBLTCIsImNvbnRlbnQiOiJhcmcgbWF4X864IM6j4bWiIGxvZyBxX864KHjhtaIpID0gYXJnIG1pbl/OuCBLTChwX2RhdGEg4oCWIHFfzrgpLiBNYXhpbXVtIGxpa2VsaWhvb2QgZXN0aW1hdGlvbiBpcyBmb3J3YXJkIEtMIG1pbmltaXphdGlvbiDigJQgaXQgZm9yY2VzIHRoZSBtb2RlbCB0byBjb3ZlciBhbGwgdGhlIGRhdGEsIG5vdCBqdXN0IGZpdCBvbmUgY2x1c3Rlci4gVGhpcyBpcyB3aHkgTUxFIHdpdGggZmxleGlibGUgbW9kZWxzIHRlbmRzIHRvIHByb2R1Y2UgYnJvYWQsIGNhbGlicmF0ZWQgZGlzdHJpYnV0aW9ucy4ifSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJLTCBkaXZlcmdlbmNlIGlzIHRoZSBmdW5kYW1lbnRhbCBtZWFzdXJlIG9mIGRpc2NyZXBhbmN5IGJldHdlZW4gcHJvYmFiaWxpdHkgZGlzdHJpYnV0aW9ucy4gSXRzIGFzeW1tZXRyeSBlbmNvZGVzIHR3byBjb21wbGV0ZWx5IGRpZmZlcmVudCBvcHRpbWl6YXRpb24gb2JqZWN0aXZlcyDigJQgZm9yd2FyZCBLTCBmb3IgaW5jbHVzaXZlIGNvdmVyYWdlIChNTEUsIGNyb3NzLWVudHJvcHkgdHJhaW5pbmcpIGFuZCByZXZlcnNlIEtMIGZvciBtb2RlIGNvbmNlbnRyYXRpb24gKFZBRXMsIHZhcmlhdGlvbmFsIGluZmVyZW5jZSwgUkxIRikuIENob29zaW5nIHRoZSB3cm9uZyBkaXJlY3Rpb24gbGVhZHMgdG8gcGF0aG9sb2dpY2FsIGJlaGF2aW91cjogbW9kZSBhdmVyYWdpbmcgb3IgbW9kZSBkcm9wcGluZy4ifV0="
---
# KL Divergence — Asymmetry and Forward vs Reverse

Kullback-Leibler divergence is one of the most important quantities in statistics, information theory, and machine learning. It measures how much one probability distribution differs from another, and its asymmetry — KL(P‖Q) ≠ KL(Q‖P) in general — is not a bug but a feature: each direction captures fundamentally different behaviour when approximating distributions.

## Definition and Non-Negativity

For discrete distributions P and Q over the same support, KL(P‖Q) = Σ_x p(x) log(p(x)/q(x)). This can be read as the extra bits per symbol when encoding data from P using a code optimized for Q, rather than the optimal code for P. KL(P‖Q) ≥ 0 always (Gibbs' inequality), with equality iff P = Q everywhere. Proof: by Jensen's inequality applied to the convex function -log, -KL(P‖Q) = Σ p(x) log(q(x)/p(x)) ≤ log Σ p(x)·(q(x)/p(x)) = log 1 = 0.

> **KL Is Not a Distance**: KL divergence is not a metric. It violates symmetry (KL(P‖Q) ≠ KL(Q‖P) in general) and the triangle inequality. It is undefined when Q(x)=0 but P(x)>0 (the convention is KL = +∞ in this case). Use Jensen-Shannon divergence when a symmetric, bounded measure is needed.

```python
import numpy as np
from scipy.special import kl_div
from scipy.stats import entropy as scipy_entropy

def kl_divergence(p, q, eps=1e-12):
    """
    KL(P‖Q) = Σ p(x) log(p(x)/q(x)).
    Returns +inf if q(x)=0 and p(x)>0.
    """
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    # Find support where p > 0
    mask = p > 0
    if np.any(q[mask] == 0):
        return np.inf
    return np.sum(p[mask] * np.log(p[mask] / (q[mask] + eps)))

# Demonstrate asymmetry
p = np.array([0.6, 0.3, 0.1])
q = np.array([0.2, 0.5, 0.3])

kl_pq = kl_divergence(p, q)
kl_qp = kl_divergence(q, p)

print(f"KL(P‖Q) = {kl_pq:.4f} nats")
print(f"KL(Q‖P) = {kl_qp:.4f} nats")
print(f"Asymmetric: {not np.isclose(kl_pq, kl_qp)}")

# Verify with scipy
print(f"Scipy KL(P‖Q) = {scipy_entropy(p, q):.4f} nats  (matches: {np.isclose(kl_pq, scipy_entropy(p, q))})")

# KL = 0 iff P = Q
print(f"\nKL(P‖P) = {kl_divergence(p, p):.6f}  (should be 0)")

# KL blows up when Q has zero where P has mass
q_zero = np.array([0.5, 0.5, 0.0])
print(f"KL(P‖Q) when Q has zero where P>0: {kl_divergence(p, q_zero)}")  # inf
```

## Forward KL vs Reverse KL — The Critical Difference

Forward KL (also called 'inclusive' or 'I-projection'): minimize KL(p_true ‖ q_approx) over q. Because log(p/q) → -∞ when q → 0 but p > 0, the loss is infinite unless q covers all modes of p. This forces q to be broad — it must place mass everywhere that p does, even if p is multimodal. The result is often a smeared-out, mean-seeking approximation.

Reverse KL (also called 'exclusive' or 'M-projection'): minimize KL(q_approx ‖ p_true) over q. Because we weight by q, when q(x) → 0 there is no penalty even if p(x) > 0. This allows q to ignore modes of p entirely. The optimizer concentrates q on one mode of p (mode-seeking behaviour), fitting that mode well while ignoring others.

```python
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Target: bimodal distribution (mixture of two Gaussians on discrete grid)
x = np.linspace(-5, 5, 300)
dx = x[1] - x[0]

def gaussian(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

# True distribution: bimodal
p = 0.5 * gaussian(x, -2, 0.5) + 0.5 * gaussian(x, 2, 0.5)
p = p / (p.sum() * dx)  # normalize
p_discrete = p * dx    # discrete probabilities

def fit_gaussian_approx(target_kl):
    """Fit N(mu, sigma) to bimodal p by minimizing forward or reverse KL."""
    def forward_kl(params):  # KL(p_true || q)
        mu, log_sigma = params
        sigma = np.exp(log_sigma)
        q = gaussian(x, mu, sigma)
        q = q / (q.sum() * dx)
        q_d = q * dx
        q_d = np.clip(q_d, 1e-12, None)
        return np.sum(p_discrete * np.log(np.clip(p_discrete, 1e-12, None) / q_d))

    def reverse_kl(params):  # KL(q || p_true)
        mu, log_sigma = params
        sigma = np.exp(log_sigma)
        q = gaussian(x, mu, sigma)
        q = q / (q.sum() * dx)
        q_d = np.clip(q * dx, 1e-12, None)
        p_d = np.clip(p_discrete, 1e-12, None)
        return np.sum(q_d * np.log(q_d / p_d))

    obj = forward_kl if target_kl == 'forward' else reverse_kl
    result = minimize(obj, [0.0, 0.0], method='Nelder-Mead')
    mu, log_sigma = result.x
    return mu, np.exp(log_sigma)

mu_fwd, sig_fwd = fit_gaussian_approx('forward')
mu_rev, sig_rev = fit_gaussian_approx('reverse')

print(f"Forward KL fit:  mu={mu_fwd:.3f}, sigma={sig_fwd:.3f}  (mean-seeking, wide)")
print(f"Reverse KL fit:  mu={mu_rev:.3f}, sigma={sig_rev:.3f}  (mode-seeking, narrow)")
```

## KL in Variational Inference and VAEs

Variational Autoencoders (VAEs) minimize the negative ELBO: L = E_q[log p(x|z)] - KL(q(z|x) ‖ p(z)). The KL term is between the approximate posterior q(z|x) (encoder) and the prior p(z) (typically N(0,I)). This is the reverse KL KL(q‖p), which encourages mode-seeking behaviour — the encoder learns to concentrate on specific regions of latent space rather than spreading probability mass everywhere.

```python
import numpy as np
import torch
import torch.nn as nn

# KL divergence between two Gaussians: closed form
# KL(N(mu1, sigma1^2) || N(mu2, sigma2^2))
def kl_gaussians(mu1, logvar1, mu2=0.0, logvar2=0.0):
    """
    Closed-form KL between two diagonal Gaussians.
    Default: KL(q || N(0,I)) used in VAE ELBO.
    """
    var1 = torch.exp(logvar1)
    var2 = torch.exp(torch.tensor(logvar2))
    kl = 0.5 * (logvar2 - logvar1 + var1 / var2
                + (mu1 - mu2) ** 2 / var2 - 1)
    return kl.sum(dim=-1).mean()

# Simulate VAE encoder output for a batch
torch.manual_seed(42)
batch_size, latent_dim = 32, 8
mu     = torch.randn(batch_size, latent_dim) * 0.5
logvar = torch.randn(batch_size, latent_dim) * 0.3 - 1  # log-variance

kl_loss = kl_gaussians(mu, logvar)

# VAE reparameterization trick
eps = torch.randn_like(mu)
z   = mu + torch.exp(0.5 * logvar) * eps

# Reconstruction loss placeholder (assume binary input)
recon_loss = nn.BCELoss()(torch.sigmoid(z), torch.rand_like(z))

elbo = recon_loss + kl_loss
print(f"VAE ELBO components (batch of {batch_size}):")
print(f"  Reconstruction loss: {recon_loss.item():.4f}")
print(f"  KL(q‖p) loss:        {kl_loss.item():.4f}")
print(f"  Total -ELBO:          {elbo.item():.4f}")
print(f"  Reparameterized z shape: {z.shape}")
```

## KL in RLHF and Language Model Alignment

Reinforcement Learning from Human Feedback (RLHF) uses a KL penalty to keep the policy π_θ close to a reference policy π_ref: L = -E[r(x)] + β·KL(π_θ ‖ π_ref). The KL term prevents the policy from deviating too far from the pretrained model (reward hacking, mode collapse). This is a reverse KL: KL(π_θ ‖ π_ref), penalizing the policy for placing mass where the reference has low probability.

```python
import numpy as np
import torch
import torch.nn.functional as F

def kl_penalty_rlhf(logits_policy, logits_ref, beta=0.01):
    """
    KL penalty used in RLHF: beta * KL(pi_theta || pi_ref).
    logits_policy, logits_ref: (batch, vocab_size)
    """
    log_p = F.log_softmax(logits_policy, dim=-1)
    log_r = F.log_softmax(logits_ref,    dim=-1)
    # KL(policy || ref) = Σ p * (log p - log r)
    kl = (log_p.exp() * (log_p - log_r)).sum(dim=-1)  # (batch,)
    return beta * kl.mean()

torch.manual_seed(1)
batch, vocab = 16, 50257  # GPT-2 vocab size

# Reference model (frozen)
logits_ref    = torch.randn(batch, vocab)
# Policy slightly shifted from reference
logits_policy = logits_ref + torch.randn(batch, vocab) * 0.5
# Strongly shifted policy (would get large KL penalty)
logits_drifted = logits_ref + torch.randn(batch, vocab) * 3.0

for name, logits in [("aligned policy", logits_policy),
                     ("drifted policy", logits_drifted)]:
    kl_pen = kl_penalty_rlhf(logits, logits_ref, beta=0.01)
    kl_raw = kl_penalty_rlhf(logits, logits_ref, beta=1.0)
    print(f"{name}: KL = {kl_raw.item():.4f} nats,  penalty (β=0.01) = {kl_pen.item():.4f}")
```

| Property | KL(P‖Q) — Forward KL | KL(Q‖P) — Reverse KL |
| --- | --- | --- |
| Also called | I-projection, inclusive, mean-seeking | M-projection, exclusive, mode-seeking |
| When Q(x)=0, P(x)>0 | KL = +∞ — forces Q to cover P's support | No penalty — Q can ignore modes of P |
| When P(x)=0, Q(x)>0 | No penalty — Q can be nonzero where P=0 | KL = +∞ (if log 0 = -∞ convention) |
| Optimizer behaviour | Q spreads to cover all modes of P | Q concentrates on one mode of P |
| Used in | MLE, cross-entropy minimization | VAE encoder, variational inference, RLHF KL penalty |
| Supports must match? | Yes: Q must cover P's support | No: Q can have smaller support than P |

## JS Divergence and f-Divergences

The Jensen-Shannon divergence JSD(P,Q) = (1/2)KL(P‖M) + (1/2)KL(Q‖M) where M=(P+Q)/2 is a symmetrized, bounded variant. Both KL and JSD belong to the family of f-divergences: D_f(P‖Q) = Σ q(x) f(p(x)/q(x)) for a convex function f with f(1)=0. KL uses f(t) = t log t; reverse KL uses f(t) = -log t; JSD uses f(t) = t log(2t/(t+1)) + log(2/(t+1)).

> **MLE = Minimizing Forward KL**: arg max_θ Σᵢ log q_θ(xᵢ) = arg min_θ KL(p_data ‖ q_θ). Maximum likelihood estimation is forward KL minimization — it forces the model to cover all the data, not just fit one cluster. This is why MLE with flexible models tends to produce broad, calibrated distributions.

---

KL divergence is the fundamental measure of discrepancy between probability distributions. Its asymmetry encodes two completely different optimization objectives — forward KL for inclusive coverage (MLE, cross-entropy training) and reverse KL for mode concentration (VAEs, variational inference, RLHF). Choosing the wrong direction leads to pathological behaviour: mode averaging or mode dropping.

