---
title: "GP Hyperparameter Learning — Type-II MLE and Marginal Likelihood"
slug: "gp-hyperparameter-learning"
description: "Optimising GP kernel hyperparameters by maximising the log marginal likelihood: derivation, gradient computation via Cholesky, Bayesian Occam's razor, and ARD for feature selection."
tags: ["gaussian-processes", "kernel-methods", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoYXQgQXJlIEdQIEh5cGVycGFyYW1ldGVycz8ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV2ZXJ5IEdQIGtlcm5lbCBoYXMgaHlwZXJwYXJhbWV0ZXJzIM64IHRoYXQgbXVzdCBiZSBzZXQgYmVmb3JlIGluZmVyZW5jZS4gRm9yIHRoZSBSQkYga2VybmVsOiBsZW5ndGgtc2NhbGUg4oSTIGNvbnRyb2xzIGNvcnJlbGF0aW9uIHJhbmdlLCBzaWduYWwgdmFyaWFuY2Ugz4PCsl9mIGNvbnRyb2xzIGZ1bmN0aW9uIGFtcGxpdHVkZSwgYW5kIG5vaXNlIHZhcmlhbmNlIM+DwrJfbiBzZXBhcmF0ZXMgb2JzZXJ2YXRpb24gbm9pc2UgZnJvbSBzaWduYWwuIFNldHRpbmcgdGhlc2UgYnkgaGFuZCAoY3Jvc3MtdmFsaWRhdGlvbiBncmlkIHNlYXJjaCkgaXMgZXhwZW5zaXZlIGFuZCBpZ25vcmVzIHRoZSBwcmluY2lwbGVkIEJheWVzaWFuIGFsdGVybmF0aXZlOiBtYXhpbWlzaW5nIHRoZSBsb2cgbWFyZ2luYWwgbGlrZWxpaG9vZCwgYWxzbyBjYWxsZWQgVHlwZS1JSSBNYXhpbXVtIExpa2VsaWhvb2QgKFR5cGUtSUkgTUxFKSBvciBldmlkZW5jZSBtYXhpbWlzYXRpb24uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMZW5ndGgtc2NhbGUg4oSTOiB0aGUgc2luZ2xlIG1vc3QgaW1wb3J0YW50IGh5cGVycGFyYW1ldGVyIOKAlCBjb250cm9scyBmdW5jdGlvbiBzbW9vdGhuZXNzIiwiU2lnbmFsIHZhcmlhbmNlIM+DwrJfZjogc2NhbGVzIEssIGNvbnRyb2xsaW5nIGZ1bmN0aW9uIGFtcGxpdHVkZSIsIk5vaXNlIHZhcmlhbmNlIM+DwrJfbjogYWRkZWQgdG8gZGlhZ29uYWwgb2YgSywgc2VwYXJhdGVzIHNpZ25hbCBmcm9tIG5vaXNlIiwiTWVhbiBmdW5jdGlvbiBwYXJhbXM6IGNvbnN0YW50LCBsaW5lYXIsIG9yIHBvbHlub21pYWwgdGVybXMgZm9yIGdsb2JhbCB0cmVuZCIsIkFSRCBsZW5ndGgtc2NhbGVzOiBvbmUg4oSTX2QgcGVyIGlucHV0IGRpbWVuc2lvbiBmb3IgYXV0b21hdGljIGZlYXR1cmUgcmVsZXZhbmNlIiwiVHlwZS1JSSBNTEUgKGV2aWRlbmNlIG1heGltaXNhdGlvbik6IG9wdGltaXNlIGFsbCDOuCBqb2ludGx5IHZpYSBtYXJnaW5hbCBsaWtlbGlob29kIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxvZyBNYXJnaW5hbCBMaWtlbGlob29kIERlcml2YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkludGVncmF0aW5nIG91dCB0aGUgbGF0ZW50IGZ1bmN0aW9uIGYgZ2l2ZXMgdGhlIG1hcmdpbmFsIGxpa2VsaWhvb2QgcCh5fFgszrgpID0g4oircCh5fGYpcChmfFgszrgpZGYgPSBOKHkgfCBtKFgpLCBLX864ICsgz4PCsl9uIEkpLiBUaGUgbG9nIG1hcmdpbmFsIGxpa2VsaWhvb2QgZGVjb21wb3NlcyBpbnRvIHRocmVlIGludGVycHJldGFibGUgdGVybXM6IGxvZyBwKHl8WCzOuCkgPSDiiJLCvSB54bWAKEsrz4PCsl9uSSnigbvCuXkg4oiSIMK9IGxvZ3xLK8+DwrJfbkl8IOKIkiBuLzIgbG9nKDLPgCkuIFRoZSBmaXJzdCB0ZXJtIGlzIGEgZGF0YS1maXQgdGVybSAobGFyZ2Ugd2hlbiB0aGUgbW9kZWwgZXhwbGFpbnMgeSB3ZWxsKS4gVGhlIHNlY29uZCBpcyBhIGNvbXBsZXhpdHkgcGVuYWx0eSAobGFyZ2Ugd2hlbiBLIGlzIGxhcmdlL2NvbXBsZXgpLiBUaGUgdGhpcmQgaXMgYSBjb25zdGFudC4gSm9pbnRseSB0aGV5IGltcGxlbWVudCBCYXllc2lhbiBPY2NhbVx1MDAyN3MgcmF6b3I6IHNpbXBsZXIgbW9kZWxzIHRoYXQgc3RpbGwgZXhwbGFpbiB0aGUgZGF0YSBhcmUgcHJlZmVycmVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgZWxsLCBzZjIpOlxuICAgIFgxID0gbnAuYXRsZWFzdF8yZChYMSkucmVzaGFwZSgtMSwxKVxuICAgIFgyID0gbnAuYXRsZWFzdF8yZChYMikucmVzaGFwZSgtMSwxKVxuICAgIHJldHVybiBzZjIgKiBucC5leHAoLTAuNSooWDEtWDIuVCkqKjIvZWxsKioyKVxuXG5kZWYgbG9nX21hcmdpbmFsX2xpa2VsaWhvb2QocGFyYW1zLCBYLCB5KTpcbiAgICBsb2dfZWxsLCBsb2dfc2YyLCBsb2dfc24yID0gcGFyYW1zXG4gICAgZWxsID0gbnAuZXhwKGxvZ19lbGwpOyBzZjIgPSBucC5leHAobG9nX3NmMik7IHNuMiA9IG5wLmV4cChsb2dfc24yKVxuICAgIG4gPSBsZW4oeSlcbiAgICBLID0gcmJmX2tlcm5lbChYLCBYLCBlbGwsIHNmMikgKyBzbjIqbnAuZXllKG4pXG4gICAgdHJ5OlxuICAgICAgICBMID0gbnAubGluYWxnLmNob2xlc2t5KEspXG4gICAgZXhjZXB0IG5wLmxpbmFsZy5MaW5BbGdFcnJvcjpcbiAgICAgICAgcmV0dXJuIDFlMTBcbiAgICBhbHBoYSA9IG5wLmxpbmFsZy5zb2x2ZShMLlQsIG5wLmxpbmFsZy5zb2x2ZShMLCB5KSlcbiAgICBsb2dfZGV0ID0gMipucC5zdW0obnAubG9nKG5wLmRpYWcoTCkpKVxuICAgIGxtbCA9IC0wLjUqKHkgQCBhbHBoYSkgLSAwLjUqbG9nX2RldCAtIDAuNSpuKm5wLmxvZygyKm5wLnBpKVxuICAgIHJldHVybiAtbG1sICAgIyByZXR1cm4gbmVnYXRpdmUgZm9yIG1pbmltaXNhdGlvblxuXG5ucC5yYW5kb20uc2VlZCg0MilcblggPSBucC5saW5zcGFjZSgtNSwgNSwgNDApXG55ID0gbnAuc2luKFgpICsgMC4yKm5wLnJhbmRvbS5yYW5kbig0MClcblxuIyBPcHRpbWlzZSBoeXBlcnBhcmFtZXRlcnMgZnJvbSBtdWx0aXBsZSByZXN0YXJ0c1xuYmVzdF92YWwsIGJlc3RfcGFyYW1zID0gbnAuaW5mLCBOb25lXG5mb3IgXyBpbiByYW5nZSg1KTpcbiAgICB4MCA9IG5wLmxvZyhucC5yYW5kb20udW5pZm9ybShbMC4xLCAwLjEsIDAuMDFdLCBbNS4wLCA1LjAsIDEuMF0pKVxuICAgIHJlcyA9IG1pbmltaXplKGxvZ19tYXJnaW5hbF9saWtlbGlob29kLCB4MCwgYXJncz0oWCwgeSksIG1ldGhvZD1cdTAwMjdMLUJGR1MtQlx1MDAyNylcbiAgICBpZiByZXMuZnVuIFx1MDAzYyBiZXN0X3ZhbDpcbiAgICAgICAgYmVzdF92YWwsIGJlc3RfcGFyYW1zID0gcmVzLmZ1biwgcmVzLnhcblxuZWxsX29wdCwgc2YyX29wdCwgc24yX29wdCA9IG5wLmV4cChiZXN0X3BhcmFtcylcbnByaW50KGZcdTAwMjdPcHRpbWlzZWQ6IOKEkz17ZWxsX29wdDouM2Z9LCDPg8KyX2Y9e3NmMl9vcHQ6LjNmfSwgz4PCsl9uPXtzbjJfb3B0Oi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkh5cGVycGFyYW1ldGVyIiwiUm9sZSIsIkRpYWdub3NpcyBXaGVuIFdyb25nIiwiVHlwaWNhbCBSYW5nZSJdLCJyb3dzIjpbWyJMZW5ndGgtc2NhbGUg4oSTIiwiQ29udHJvbHMgY29ycmVsYXRpb24gcmFuZ2UiLCJUb28gc21hbGwg4oaSIHdpZ2dseSwgb3ZlcmZpdDsgdG9vIGxhcmdlIOKGkiB1bmRlcmZpdCIsIjAuMSDDlyBkYXRhX3JhbmdlIOKAkyAyIMOXIGRhdGFfcmFuZ2UiXSxbIlNpZ25hbCB2YXJpYW5jZSDPg8KyX2YiLCJGdW5jdGlvbiBhbXBsaXR1ZGUiLCJUb28gc21hbGwg4oaSIG1lYW4gbmVhciB6ZXJvOyB0b28gbGFyZ2Ug4oaSIHdpbGQgZXh0cmFwb2xhdGlvbiIsIk1hdGNoZWQgdG8gb3V0cHV0IHN0ZDogMC4x4oCTMTAiXSxbIk5vaXNlIHZhcmlhbmNlIM+DwrJfbiIsIk9ic2VydmF0aW9uIG5vaXNlIiwiVG9vIHNtYWxsIOKGkiBpbnRlcnBvbGF0aW9uOyB0b28gbGFyZ2Ug4oaSIHNtb290aCBidXQgbWlzZml0IiwiMC4wMDHigJMxLjAgKGFzIGZyYWN0aW9uIG9mIG91dHB1dCB2YXJpYW5jZSkiXSxbIk1lYW4gcGFyYW1zIChpZiBsaW5lYXIvY29uc3QgbWVhbikiLCJDYXB0dXJlIGdsb2JhbCB0cmVuZCIsIklnbm9yZWQgYmFzZWxpbmUg4oaSIGJpYXNlZCBleHRyYXBvbGF0aW9uIiwiRml0IGZyb20gZGF0YTsgb2Z0ZW4gemVybyB3b3JrcyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR1B5VG9yY2ggTWFyZ2luYWwgTGlrZWxpaG9vZCBPcHRpbWlzYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdQeVRvcmNoIGNvbXB1dGVzIHRoZSBleGFjdCBtYXJnaW5hbCBsb2cgbGlrZWxpaG9vZCAoRXhhY3RNYXJnaW5hbExvZ0xpa2VsaWhvb2QpIGFuZCBpdHMgZ3JhZGllbnQgdGhyb3VnaCBhdXRvbWF0aWMgZGlmZmVyZW50aWF0aW9uLiBBIHN0YW5kYXJkIHRyYWluaW5nIGxvb3AgdXNlcyBBZGFtIG9yIEwtQkZHUyB3aXRoIDEwMOKAkzIwMCBpdGVyYXRpb25zLiBMb2ctcGFyYW1ldGVyaXNpbmcgaHlwZXJwYXJhbWV0ZXJzICh3b3JraW5nIGluIGxvZyBzcGFjZSkgZW5zdXJlcyBwb3NpdGl2aXR5IGFuZCBiZXR0ZXItY29uZGl0aW9uZWQgZ3JhZGllbnRzLiBHUHlUb3JjaFx1MDAyN3MgUGFyYW1ldGVyQ29uc3RyYWludCBzeXN0ZW0gaGFuZGxlcyB0aGlzIGF1dG9tYXRpY2FsbHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IGdweXRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuY2xhc3MgR1BNb2RlbChncHl0b3JjaC5tb2RlbHMuRXhhY3RHUCk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpXG4gICAgICAgIHNlbGYubWVhbl9tb2R1bGUgID0gZ3B5dG9yY2gubWVhbnMuWmVyb01lYW4oKVxuICAgICAgICBzZWxmLmNvdmFyX21vZHVsZSA9IGdweXRvcmNoLmtlcm5lbHMuU2NhbGVLZXJuZWwoZ3B5dG9yY2gua2VybmVscy5SQkZLZXJuZWwoKSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIGdweXRvcmNoLmRpc3RyaWJ1dGlvbnMuTXVsdGl2YXJpYXRlTm9ybWFsKFxuICAgICAgICAgICAgc2VsZi5tZWFuX21vZHVsZSh4KSwgc2VsZi5jb3Zhcl9tb2R1bGUoeCkpXG5cbm5wLnJhbmRvbS5zZWVkKDApXG5YX25wID0gbnAubGluc3BhY2UoLTUsIDUsIDUwKVxueV9ucCA9IG5wLnNpbihYX25wKSArIDAuMipucC5yYW5kb20ucmFuZG4oNTApXG50cmFpbl94ID0gdG9yY2gudGVuc29yKFhfbnAsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG50cmFpbl95ID0gdG9yY2gudGVuc29yKHlfbnAsIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG5cbmxpa2VsaWhvb2QgPSBncHl0b3JjaC5saWtlbGlob29kcy5HYXVzc2lhbkxpa2VsaWhvb2QoKVxubW9kZWwgPSBHUE1vZGVsKHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpXG5tb2RlbC50cmFpbigpOyBsaWtlbGlob29kLnRyYWluKClcbm1sbCA9IGdweXRvcmNoLm1sbHMuRXhhY3RNYXJnaW5hbExvZ0xpa2VsaWhvb2QobGlrZWxpaG9vZCwgbW9kZWwpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MC4xKVxuZm9yIGkgaW4gcmFuZ2UoMTUwKTpcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzID0gLW1sbChtb2RlbCh0cmFpbl94KSwgdHJhaW5feSlcbiAgICBsb3NzLmJhY2t3YXJkKCk7IG9wdGltaXplci5zdGVwKClcblxuZWxsID0gbW9kZWwuY292YXJfbW9kdWxlLmJhc2Vfa2VybmVsLmxlbmd0aHNjYWxlLml0ZW0oKVxuc2YyID0gbW9kZWwuY292YXJfbW9kdWxlLm91dHB1dHNjYWxlLml0ZW0oKVxuc24yID0gbGlrZWxpaG9vZC5ub2lzZS5pdGVtKClcbnByaW50KGZcdTAwMjdMZWFybmVkOiDihJM9e2VsbDouM2Z9LCDPg8KyX2Y9e3NmMjouM2Z9LCDPg8KyX249e3NuMjouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1hcmdpbmFsIExpa2VsaWhvb2QgTGFuZHNjYXBlIGFuZCBCYXllc2lhbiBPY2NhbVx1MDAyN3MgUmF6b3IifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBtYXJnaW5hbCBsaWtlbGlob29kIHN1cmZhY2Ugb3ZlciAo4oSTLCDPg8KyX2YpIGlzIHR5cGljYWxseSB1bmltb2RhbCBmb3Igc2ltcGxlIGRhdGFzZXRzIGJ1dCBjYW4gaGF2ZSBtdWx0aXBsZSBsb2NhbCBvcHRpbWEgZm9yIGNvbXBsZXggb3Igbm9pc3kgZGF0YS4gVGhlIGRhdGEtZml0IHRlcm0gZmF2b3VycyBjb21wbGV4IG1vZGVscyAobWFueSBwYXJhbWV0ZXJzLCBzbWFsbCDihJMpOyB0aGUgY29tcGxleGl0eSBwZW5hbHR5IGxvZ3xLK8+DwrJfbkl8IHBlbmFsaXNlcyB0aGVtLiBUaGVpciBzdW0g4oCUIHRoZSBtYXJnaW5hbCBsaWtlbGlob29kIOKAlCBwZWFrcyBhdCB0aGUgc2ltcGxlc3QgbW9kZWwgdGhhdCBzdGlsbCBleHBsYWlucyB0aGUgZGF0YS4gVGhpcyBhdXRvbWF0aWMgY29tcGxleGl0eSBjb250cm9sIGlzIHRoZSBCYXllc2lhbiBPY2NhbVx1MDAyN3MgcmF6b3IuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBzY2lweS5vcHRpbWl6ZSBpbXBvcnQgbWluaW1pemVcblxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBlbGwsIHNmMik6XG4gICAgWDEgPSBucC5hdGxlYXN0XzJkKFgxKS5yZXNoYXBlKC0xLDEpXG4gICAgWDIgPSBucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLDEpXG4gICAgcmV0dXJuIHNmMiAqIG5wLmV4cCgtMC41KihYMS1YMi5UKSoqMi9lbGwqKjIpXG5cbmRlZiBsbWxfZ3JpZChYLCB5LCBlbGwsIHNmMiwgc24yPTAuMDUpOlxuICAgIG4gPSBsZW4oeSlcbiAgICBLID0gcmJmX2tlcm5lbChYLCBYLCBlbGwsIHNmMikgKyBzbjIqbnAuZXllKG4pXG4gICAgdHJ5OlxuICAgICAgICBMID0gbnAubGluYWxnLmNob2xlc2t5KEspXG4gICAgICAgIGFscGhhID0gbnAubGluYWxnLnNvbHZlKEwuVCwgbnAubGluYWxnLnNvbHZlKEwsIHkpKVxuICAgICAgICBsb2dfZGV0ID0gMipucC5zdW0obnAubG9nKG5wLmRpYWcoTCkpKVxuICAgICAgICByZXR1cm4gLTAuNSooeUBhbHBoYSkgLSAwLjUqbG9nX2RldCAtIDAuNSpuKm5wLmxvZygyKm5wLnBpKVxuICAgIGV4Y2VwdCBFeGNlcHRpb246XG4gICAgICAgIHJldHVybiBucC5uYW5cblxubnAucmFuZG9tLnNlZWQoNSlcblggPSBucC5saW5zcGFjZSgtNSwgNSwgMzApXG55ID0gbnAuc2luKFgpICsgMC4xNSpucC5yYW5kb20ucmFuZG4oMzApXG5cbmVsbHMgID0gbnAubG9nc3BhY2UoLTEsIDEsIDQwKVxuc2YycyAgPSBucC5sb2dzcGFjZSgtMSwgMSwgNDApXG5aID0gbnAuYXJyYXkoW1tsbWxfZ3JpZChYLCB5LCBlLCBzKSBmb3IgZSBpbiBlbGxzXSBmb3IgcyBpbiBzZjJzXSlcblxucGx0LmZpZ3VyZShmaWdzaXplPSg4LDYpKVxucGx0LmNvbnRvdXJmKG5wLmxvZzEwKGVsbHMpLCBucC5sb2cxMChzZjJzKSwgWiwgbGV2ZWxzPTMwLCBjbWFwPVx1MDAyN3ZpcmlkaXNcdTAwMjcpXG5wbHQuY29sb3JiYXIobGFiZWw9XHUwMDI3TG9nIE1hcmdpbmFsIExpa2VsaWhvb2RcdTAwMjcpXG5wbHQueGxhYmVsKFx1MDAyN2xvZ+KCgeKCgCjihJMpXHUwMDI3KTsgcGx0LnlsYWJlbChcdTAwMjdsb2figoHigoAoz4PCsl9mKVx1MDAyNylcbnBsdC50aXRsZShcdTAwMjdNYXJnaW5hbCBMaWtlbGlob29kIExhbmRzY2FwZVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTXVsdGlwbGUgUmVzdGFydHMgQXZvaWQgTG9jYWwgT3B0aW1hIiwiY29udGVudCI6IlRoZSBtYXJnaW5hbCBsaWtlbGlob29kIG9iamVjdGl2ZSBpcyBub24tY29udmV4LiBSdW4gTC1CRkdTLUIgZnJvbSA14oCTMjAgcmFuZG9tIGluaXRpYWxpc2F0aW9ucyBpbiBsb2ctcGFyYW1ldGVyIHNwYWNlIGFuZCB0YWtlIHRoZSBvcHRpbXVtIHdpdGggdGhlIGhpZ2hlc3QgbG9nIG1hcmdpbmFsIGxpa2VsaWhvb2QuIFRoaXMgaXMgZXNwZWNpYWxseSBpbXBvcnRhbnQgZm9yIGhpZ2gtZGltZW5zaW9uYWwgb3IgY29tcG9zaXRpb25hbCBrZXJuZWxzIHdpdGggbWFueSBoeXBlcnBhcmFtZXRlcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQVJEIOKAlCBBdXRvbWF0aWMgUmVsZXZhbmNlIERldGVybWluYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF1dG9tYXRpYyBSZWxldmFuY2UgRGV0ZXJtaW5hdGlvbiAoQVJEKSBleHRlbmRzIHRoZSBzY2FsYXIgbGVuZ3RoLXNjYWxlIOKEkyB0byBhIHNlcGFyYXRlIOKEk19kIHBlciBpbnB1dCBkaW1lbnNpb24gZC4gVGhlIEFSRCBrZXJuZWwgaXMgayh4LHhcdTAwMjcpID0gz4PCsl9mIGV4cCjiiJLOo19kICh4ZOKIknhcdTAwMjdkKcKyLygy4oSTX2TCsikpLiBBZnRlciBtYXJnaW5hbCBsaWtlbGlob29kIG9wdGltaXNhdGlvbiwgc21hbGwg4oSTX2Qg4oaSIGRpbWVuc2lvbiBkIGlzIHJlbGV2YW50IChmdW5jdGlvbiB2YXJpZXMgc2hhcnBseSB3aXRoIGl0KTsgbGFyZ2Ug4oSTX2Qg4oaSIGRpbWVuc2lvbiBkIGlzIGlycmVsZXZhbnQgKGZ1bmN0aW9uIGlzIGZsYXQpLiBBUkQgcHJvdmlkZXMgYXV0b21hdGljLCBjb250aW51b3VzIGZlYXR1cmUgc2VsZWN0aW9uIGVtYmVkZGVkIGluIHRoZSBHUC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgZ3B5dG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5ucC5yYW5kb20uc2VlZCg0Milcbm4sIGQgPSAxMDAsIDZcblhfbnAgPSBucC5yYW5kb20ucmFuZG4obiwgZClcbiMgT25seSBmaXJzdCAyIGZlYXR1cmVzIG1hdHRlclxueV9ucCA9IG5wLnNpbihYX25wWzosMF0pICsgMC41KlhfbnBbOiwxXSArIDAuMSpucC5yYW5kb20ucmFuZG4obilcblxudHJhaW5feCA9IHRvcmNoLnRlbnNvcihYX25wLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxudHJhaW5feSA9IHRvcmNoLnRlbnNvcih5X25wLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuXG5saWtlbGlob29kID0gZ3B5dG9yY2gubGlrZWxpaG9vZHMuR2F1c3NpYW5MaWtlbGlob29kKClcbm1vZGVsX2FyZCA9IGdweXRvcmNoLm1vZGVscy5FeGFjdEdQKHRyYWluX3gsIHRyYWluX3ksIGxpa2VsaWhvb2QpXG5tb2RlbF9hcmQubWVhbl9tb2R1bGUgID0gZ3B5dG9yY2gubWVhbnMuWmVyb01lYW4oKVxubW9kZWxfYXJkLmNvdmFyX21vZHVsZSA9IGdweXRvcmNoLmtlcm5lbHMuU2NhbGVLZXJuZWwoXG4gICAgZ3B5dG9yY2gua2VybmVscy5SQkZLZXJuZWwoYXJkX251bV9kaW1zPWQpKVxubW9kZWxfYXJkLmZvcndhcmQgPSBsYW1iZGEgeDogZ3B5dG9yY2guZGlzdHJpYnV0aW9ucy5NdWx0aXZhcmlhdGVOb3JtYWwoXG4gICAgbW9kZWxfYXJkLm1lYW5fbW9kdWxlKHgpLCBtb2RlbF9hcmQuY292YXJfbW9kdWxlKHgpKVxuXG5tb2RlbF9hcmQudHJhaW4oKTsgbGlrZWxpaG9vZC50cmFpbigpXG5tbGwgPSBncHl0b3JjaC5tbGxzLkV4YWN0TWFyZ2luYWxMb2dMaWtlbGlob29kKGxpa2VsaWhvb2QsIG1vZGVsX2FyZClcbm9wdCA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWxfYXJkLnBhcmFtZXRlcnMoKSwgbHI9MC4xKVxuZm9yIF8gaW4gcmFuZ2UoMjAwKTpcbiAgICBvcHQuemVyb19ncmFkKCk7ICgtbWxsKG1vZGVsX2FyZCh0cmFpbl94KSwgdHJhaW5feSkpLmJhY2t3YXJkKCk7IG9wdC5zdGVwKClcblxuZWxscyA9IG1vZGVsX2FyZC5jb3Zhcl9tb2R1bGUuYmFzZV9rZXJuZWwubGVuZ3Roc2NhbGUuZGV0YWNoKCkubnVtcHkoKVswXVxuZm9yIGksIGwgaW4gZW51bWVyYXRlKGVsbHMpOlxuICAgIHByaW50KGZcdTAwMjdGZWF0dXJlIHtpfTog4oSTID0ge2w6LjNmfSAge1wiXHUwMDNjLS0gcmVsZXZhbnRcIiBpZiBsIFx1MDAzYyAxLjAgZWxzZSBcImlycmVsZXZhbnRcIn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHlwZS1JSSBNTEUgb3B0aW1pc2VzIEdQIGh5cGVycGFyYW1ldGVycyBieSBtYXhpbWlzaW5nIHRoZSBsb2cgbWFyZ2luYWwgbGlrZWxpaG9vZCBsb2cgcCh5fFgszrgpLiBUaGUgb2JqZWN0aXZlIGJhbGFuY2VzIGRhdGEtZml0IGFnYWluc3QgbW9kZWwgY29tcGxleGl0eSAoQmF5ZXNpYW4gT2NjYW1cdTAwMjdzIHJhem9yKSB3aXRob3V0IGEgaGVsZC1vdXQgdmFsaWRhdGlvbiBzZXQuIE9wdGltaXNhdGlvbiB1c2VzIGdyYWRpZW50LWJhc2VkIG1ldGhvZHMgKEwtQkZHUy1CIG9yIEFkYW0pIGluIGxvZy1wYXJhbWV0ZXIgc3BhY2Ugd2l0aCBtdWx0aXBsZSByZXN0YXJ0cy4gQVJEIGV4dGVuZHMgc2NhbGFyIGxlbmd0aC1zY2FsZXMgdG8gcGVyLWRpbWVuc2lvbiB2YWx1ZXMsIHByb3ZpZGluZyBhdXRvbWF0aWMgZmVhdHVyZSBzZWxlY3Rpb24uIEZvciBsYXJnZSBuLCBncmFkaWVudCBjb21wdXRhdGlvbiB0aHJvdWdoIENob2xlc2t5IHJlbWFpbnMgdGhlIHN0YW5kYXJkIGFwcHJvYWNoLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiTWFyZ2luYWwgTGlrZWxpaG9vZCDiiaAgUHJlZGljdGl2ZSBBY2N1cmFjeSIsImNvbnRlbnQiOiJNYXhpbWlzaW5nIHRoZSBtYXJnaW5hbCBsaWtlbGlob29kIGlzIG5vdCB0aGUgc2FtZSBhcyBtaW5pbWlzaW5nIHByZWRpY3Rpb24gZXJyb3IuIFRoZSBjb21wbGV4aXR5IHBlbmFsdHkgY2FuIGNhdXNlIHRoZSBvcHRpbWlzZXIgdG8gY2hvb3NlIGEgc2ltcGxlciBtb2RlbCB0aGFuIHdoYXQgZ2l2ZXMgYmVzdCB0ZXN0IFJNU0UsIGVzcGVjaWFsbHkgZm9yIHNtYWxsIGRhdGFzZXRzLiBXaGVuIHB1cmUgcHJlZGljdGl2ZSBhY2N1cmFjeSBtYXR0ZXJzLCBjb21wYXJlIHdpdGggY3Jvc3MtdmFsaWRhdGVkIGh5cGVycGFyYW1ldGVyIHNlbGVjdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkxvZyBtYXJnaW5hbCBsaWtlbGlob29kID0gZGF0YSBmaXQg4oiSIGNvbXBsZXhpdHkgcGVuYWx0eSDiiJIgY29uc3RhbnQiLCJUaHJlZSB0ZXJtczog4oiSwr154bWAKEsrz4PCskkp4oG7wrl5LCDiiJLCvWxvZ3xLK8+DwrJJfCwg4oiSbi8yIGxvZygyz4ApIiwiR3JhZGllbnQgdGhyb3VnaCBDaG9sZXNreTog4oiCTE1ML+KIgs64IHZpYSBtYXRyaXggZGVyaXZhdGl2ZXMg4oCUIGF1dG9tYXRpYyBpbiBHUHlUb3JjaCIsIkwtQkZHUy1CIHdpdGggNeKAkzIwIHJhbmRvbSByZXN0YXJ0cyBhdm9pZHMgbG9jYWwgb3B0aW1hIiwiQVJEOiBzZXBhcmF0ZSDihJNfZCBwZXIgZGltZW5zaW9uIGdpdmVzIGF1dG9tYXRpYyByZWxldmFuY2UgZGV0ZXJtaW5hdGlvbiIsIkJheWVzaWFuIE9jY2FtXHUwMDI3cyByYXpvcjogbWFyZ2luYWwgbGlrZWxpaG9vZCBwcmVmZXJzIHNpbXBsZXIgbW9kZWxzIHRoYXQgZml0IHRoZSBkYXRhIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# GP Hyperparameter Learning — Type-II MLE and Marginal Likelihood

## What Are GP Hyperparameters?

Every GP kernel has hyperparameters θ that must be set before inference. For the RBF kernel: length-scale ℓ controls correlation range, signal variance σ²_f controls function amplitude, and noise variance σ²_n separates observation noise from signal. Setting these by hand (cross-validation grid search) is expensive and ignores the principled Bayesian alternative: maximising the log marginal likelihood, also called Type-II Maximum Likelihood (Type-II MLE) or evidence maximisation.

- Length-scale ℓ: the single most important hyperparameter — controls function smoothness
- Signal variance σ²_f: scales K, controlling function amplitude
- Noise variance σ²_n: added to diagonal of K, separates signal from noise
- Mean function params: constant, linear, or polynomial terms for global trend
- ARD length-scales: one ℓ_d per input dimension for automatic feature relevance
- Type-II MLE (evidence maximisation): optimise all θ jointly via marginal likelihood

## Log Marginal Likelihood Derivation

Integrating out the latent function f gives the marginal likelihood p(y|X,θ) = ∫p(y|f)p(f|X,θ)df = N(y | m(X), K_θ + σ²_n I). The log marginal likelihood decomposes into three interpretable terms: log p(y|X,θ) = −½ yᵀ(K+σ²_nI)⁻¹y − ½ log|K+σ²_nI| − n/2 log(2π). The first term is a data-fit term (large when the model explains y well). The second is a complexity penalty (large when K is large/complex). The third is a constant. Jointly they implement Bayesian Occam's razor: simpler models that still explain the data are preferred.

```python
import numpy as np
from scipy.optimize import minimize

def rbf_kernel(X1, X2, ell, sf2):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1-X2.T)**2/ell**2)

def log_marginal_likelihood(params, X, y):
    log_ell, log_sf2, log_sn2 = params
    ell = np.exp(log_ell); sf2 = np.exp(log_sf2); sn2 = np.exp(log_sn2)
    n = len(y)
    K = rbf_kernel(X, X, ell, sf2) + sn2*np.eye(n)
    try:
        L = np.linalg.cholesky(K)
    except np.linalg.LinAlgError:
        return 1e10
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, y))
    log_det = 2*np.sum(np.log(np.diag(L)))
    lml = -0.5*(y @ alpha) - 0.5*log_det - 0.5*n*np.log(2*np.pi)
    return -lml   # return negative for minimisation

np.random.seed(42)
X = np.linspace(-5, 5, 40)
y = np.sin(X) + 0.2*np.random.randn(40)

# Optimise hyperparameters from multiple restarts
best_val, best_params = np.inf, None
for _ in range(5):
    x0 = np.log(np.random.uniform([0.1, 0.1, 0.01], [5.0, 5.0, 1.0]))
    res = minimize(log_marginal_likelihood, x0, args=(X, y), method='L-BFGS-B')
    if res.fun < best_val:
        best_val, best_params = res.fun, res.x

ell_opt, sf2_opt, sn2_opt = np.exp(best_params)
print(f'Optimised: ℓ={ell_opt:.3f}, σ²_f={sf2_opt:.3f}, σ²_n={sn2_opt:.4f}')
```

| Hyperparameter | Role | Diagnosis When Wrong | Typical Range |
| --- | --- | --- | --- |
| Length-scale ℓ | Controls correlation range | Too small → wiggly, overfit; too large → underfit | 0.1 × data_range – 2 × data_range |
| Signal variance σ²_f | Function amplitude | Too small → mean near zero; too large → wild extrapolation | Matched to output std: 0.1–10 |
| Noise variance σ²_n | Observation noise | Too small → interpolation; too large → smooth but misfit | 0.001–1.0 (as fraction of output variance) |
| Mean params (if linear/const mean) | Capture global trend | Ignored baseline → biased extrapolation | Fit from data; often zero works |

## GPyTorch Marginal Likelihood Optimisation

GPyTorch computes the exact marginal log likelihood (ExactMarginalLogLikelihood) and its gradient through automatic differentiation. A standard training loop uses Adam or L-BFGS with 100–200 iterations. Log-parameterising hyperparameters (working in log space) ensures positivity and better-conditioned gradients. GPyTorch's ParameterConstraint system handles this automatically.

```python
import torch
import gpytorch
import numpy as np
import matplotlib.pyplot as plt

class GPModel(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood):
        super().__init__(train_x, train_y, likelihood)
        self.mean_module  = gpytorch.means.ZeroMean()
        self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())
    def forward(self, x):
        return gpytorch.distributions.MultivariateNormal(
            self.mean_module(x), self.covar_module(x))

np.random.seed(0)
X_np = np.linspace(-5, 5, 50)
y_np = np.sin(X_np) + 0.2*np.random.randn(50)
train_x = torch.tensor(X_np, dtype=torch.float32)
train_y = torch.tensor(y_np, dtype=torch.float32)

likelihood = gpytorch.likelihoods.GaussianLikelihood()
model = GPModel(train_x, train_y, likelihood)
model.train(); likelihood.train()
mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
for i in range(150):
    optimizer.zero_grad()
    loss = -mll(model(train_x), train_y)
    loss.backward(); optimizer.step()

ell = model.covar_module.base_kernel.lengthscale.item()
sf2 = model.covar_module.outputscale.item()
sn2 = likelihood.noise.item()
print(f'Learned: ℓ={ell:.3f}, σ²_f={sf2:.3f}, σ²_n={sn2:.4f}')
```

## Marginal Likelihood Landscape and Bayesian Occam's Razor

The marginal likelihood surface over (ℓ, σ²_f) is typically unimodal for simple datasets but can have multiple local optima for complex or noisy data. The data-fit term favours complex models (many parameters, small ℓ); the complexity penalty log|K+σ²_nI| penalises them. Their sum — the marginal likelihood — peaks at the simplest model that still explains the data. This automatic complexity control is the Bayesian Occam's razor.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def rbf_kernel(X1, X2, ell, sf2):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1-X2.T)**2/ell**2)

def lml_grid(X, y, ell, sf2, sn2=0.05):
    n = len(y)
    K = rbf_kernel(X, X, ell, sf2) + sn2*np.eye(n)
    try:
        L = np.linalg.cholesky(K)
        alpha = np.linalg.solve(L.T, np.linalg.solve(L, y))
        log_det = 2*np.sum(np.log(np.diag(L)))
        return -0.5*(y@alpha) - 0.5*log_det - 0.5*n*np.log(2*np.pi)
    except Exception:
        return np.nan

np.random.seed(5)
X = np.linspace(-5, 5, 30)
y = np.sin(X) + 0.15*np.random.randn(30)

ells  = np.logspace(-1, 1, 40)
sf2s  = np.logspace(-1, 1, 40)
Z = np.array([[lml_grid(X, y, e, s) for e in ells] for s in sf2s])

plt.figure(figsize=(8,6))
plt.contourf(np.log10(ells), np.log10(sf2s), Z, levels=30, cmap='viridis')
plt.colorbar(label='Log Marginal Likelihood')
plt.xlabel('log₁₀(ℓ)'); plt.ylabel('log₁₀(σ²_f)')
plt.title('Marginal Likelihood Landscape')
plt.tight_layout(); plt.show()
```

> **Multiple Restarts Avoid Local Optima**: The marginal likelihood objective is non-convex. Run L-BFGS-B from 5–20 random initialisations in log-parameter space and take the optimum with the highest log marginal likelihood. This is especially important for high-dimensional or compositional kernels with many hyperparameters.

## ARD — Automatic Relevance Determination

Automatic Relevance Determination (ARD) extends the scalar length-scale ℓ to a separate ℓ_d per input dimension d. The ARD kernel is k(x,x') = σ²_f exp(−Σ_d (xd−x'd)²/(2ℓ_d²)). After marginal likelihood optimisation, small ℓ_d → dimension d is relevant (function varies sharply with it); large ℓ_d → dimension d is irrelevant (function is flat). ARD provides automatic, continuous feature selection embedded in the GP.

```python
import torch
import gpytorch
import numpy as np

np.random.seed(42)
n, d = 100, 6
X_np = np.random.randn(n, d)
# Only first 2 features matter
y_np = np.sin(X_np[:,0]) + 0.5*X_np[:,1] + 0.1*np.random.randn(n)

train_x = torch.tensor(X_np, dtype=torch.float32)
train_y = torch.tensor(y_np, dtype=torch.float32)

likelihood = gpytorch.likelihoods.GaussianLikelihood()
model_ard = gpytorch.models.ExactGP(train_x, train_y, likelihood)
model_ard.mean_module  = gpytorch.means.ZeroMean()
model_ard.covar_module = gpytorch.kernels.ScaleKernel(
    gpytorch.kernels.RBFKernel(ard_num_dims=d))
model_ard.forward = lambda x: gpytorch.distributions.MultivariateNormal(
    model_ard.mean_module(x), model_ard.covar_module(x))

model_ard.train(); likelihood.train()
mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model_ard)
opt = torch.optim.Adam(model_ard.parameters(), lr=0.1)
for _ in range(200):
    opt.zero_grad(); (-mll(model_ard(train_x), train_y)).backward(); opt.step()

ells = model_ard.covar_module.base_kernel.lengthscale.detach().numpy()[0]
for i, l in enumerate(ells):
    print(f'Feature {i}: ℓ = {l:.3f}  {"<-- relevant" if l < 1.0 else "irrelevant"}')
```

## Key Takeaways

Type-II MLE optimises GP hyperparameters by maximising the log marginal likelihood log p(y|X,θ). The objective balances data-fit against model complexity (Bayesian Occam's razor) without a held-out validation set. Optimisation uses gradient-based methods (L-BFGS-B or Adam) in log-parameter space with multiple restarts. ARD extends scalar length-scales to per-dimension values, providing automatic feature selection. For large n, gradient computation through Cholesky remains the standard approach.

> **Marginal Likelihood ≠ Predictive Accuracy**: Maximising the marginal likelihood is not the same as minimising prediction error. The complexity penalty can cause the optimiser to choose a simpler model than what gives best test RMSE, especially for small datasets. When pure predictive accuracy matters, compare with cross-validated hyperparameter selection.

- Log marginal likelihood = data fit − complexity penalty − constant
- Three terms: −½yᵀ(K+σ²I)⁻¹y, −½log|K+σ²I|, −n/2 log(2π)
- Gradient through Cholesky: ∂LML/∂θ via matrix derivatives — automatic in GPyTorch
- L-BFGS-B with 5–20 random restarts avoids local optima
- ARD: separate ℓ_d per dimension gives automatic relevance determination
- Bayesian Occam's razor: marginal likelihood prefers simpler models that fit the data

---

