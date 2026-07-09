---
title: "Transformer-Based Forecasting — Informer, Autoformer, PatchTST"
slug: "transformer-forecasting"
description: "Understand how vanilla Transformer attention fails for long sequences, how Informer, Autoformer, FEDformer, and PatchTST address the quadratic bottleneck, and how PatchTST enables transfer learning across time-series datasets."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHZhbmlsbGEgVHJhbnNmb3JtZXIgZW5jb2RlciBhcHBsaWVzIGZ1bGwgc2VsZi1hdHRlbnRpb24gb3ZlciBhbGwgTCBpbnB1dCB0b2tlbnMsIHJlcXVpcmluZyBPKEzCsikgbWVtb3J5IGFuZCBjb21wdXRlIOKAlCBwcm9oaWJpdGl2ZSBmb3IgbG9uZyB0aW1lIHNlcmllcyAoTD0xMDAwIG9yIG1vcmUpLiBBIHdhdmUgb2Ygc3BlY2lhbGlzZWQgYXJjaGl0ZWN0dXJlcyBhZGRyZXNzZWQgdGhpczogSW5mb3JtZXIgaW50cm9kdWNlZCBQcm9iU3BhcnNlIGF0dGVudGlvbiB3aXRoIE8oTCBsb2cgTCkgY29tcGxleGl0eTsgQXV0b2Zvcm1lciByZXBsYWNlZCBhdHRlbnRpb24gd2l0aCBhbiBhdXRvLWNvcnJlbGF0aW9uIG1lY2hhbmlzbTsgRkVEZm9ybWVyIG1vdmVkIHRvIGZyZXF1ZW5jeS1kb21haW4gbWl4aW5nOyBQYXRjaFRTVCB0b29rIGEgZGlmZmVyZW50IGFwcHJvYWNoLCBncm91cGluZyB0aW1lIHN0ZXBzIGludG8gcGF0Y2hlcyB0byByZWR1Y2Ugc2VxdWVuY2UgbGVuZ3RoIGRyYW1hdGljYWxseSBhbmQgZW5hYmxpbmcgbGFyZ2Utc2NhbGUgcHJldHJhaW5pbmcgYW5kIGZpbmUtdHVuaW5nIGFjcm9zcyBkYXRhc2V0cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWYW5pbGxhIFRyYW5zZm9ybWVyIGZvciBUaW1lIFNlcmllcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHN0YW5kYXJkIFRyYW5zZm9ybWVyIHNlbGYtYXR0ZW50aW9uIGlzIEF0dGVudGlvbihRLEssVikgPSBzb2Z0bWF4KFFL4bWAL+KImmQpVi4gRm9yIGEgc2VxdWVuY2Ugb2YgbGVuZ3RoIEwsIHRoZSBhdHRlbnRpb24gbWF0cml4IGlzIEzDl0wsIHJlcXVpcmluZyBPKEzCsikgdGltZSBhbmQgbWVtb3J5LiBQb3NpdGlvbmFsIGVuY29kaW5nIGlzIG5lZWRlZCBiZWNhdXNlIHNlbGYtYXR0ZW50aW9uIGlzIHBlcm11dGF0aW9uLWludmFyaWFudDogc2luKHBvcy8xMDAwMF4oMmkvZCkpIGFuZCBjb3MocG9zLzEwMDAwXigyaS9kKSkgYXJlIGNvbmNhdGVuYXRlZCB0byB0b2tlbiBlbWJlZGRpbmdzLiBUaGUgZW5jb2RlciBwcm9jZXNzZXMgdGhlIGlucHV0IHdpbmRvdzsgdGhlIGRlY29kZXIgdXNlcyBlbmNvZGVyLWRlY29kZXIgY3Jvc3MtYXR0ZW50aW9uIHRvIGdlbmVyYXRlIHRoZSBvdXRwdXQgc2VxdWVuY2UgYXV0b3JlZ3Jlc3NpdmVseS4gRm9yIEw9NzIwIChhIGNvbW1vbiBsb25nLWhvcml6b24gYmVuY2htYXJrKSwgdGhlIGF0dGVudGlvbiBtYXRyaXggaGFzIDUxOCw0MDAgZWxlbWVudHMgcGVyIGhlYWQg4oCUIGJhcmVseSB0cmFjdGFibGUgZXZlbiBvbiBHUFUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbWF0aFxuXG5jbGFzcyBQb3NpdGlvbmFsRW5jb2Rpbmcobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgbWF4X2xlbj01MDAwLCBkcm9wb3V0PTAuMSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmRyb3BvdXQgPSBubi5Ecm9wb3V0KGRyb3BvdXQpXG4gICAgICAgIHBlID0gdG9yY2guemVyb3MobWF4X2xlbiwgZF9tb2RlbClcbiAgICAgICAgcG9zID0gdG9yY2guYXJhbmdlKDAsIG1heF9sZW4pLnVuc3F1ZWV6ZSgxKS5mbG9hdCgpXG4gICAgICAgIGRpdiA9IHRvcmNoLmV4cCh0b3JjaC5hcmFuZ2UoMCwgZF9tb2RlbCwgMikuZmxvYXQoKSAqICgtbWF0aC5sb2coMTAwMDAuMCkgLyBkX21vZGVsKSlcbiAgICAgICAgcGVbOiwgMDo6Ml0gPSB0b3JjaC5zaW4ocG9zICogZGl2KVxuICAgICAgICBwZVs6LCAxOjoyXSA9IHRvcmNoLmNvcyhwb3MgKiBkaXYpXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFx1MDAyN3BlXHUwMDI3LCBwZS51bnNxdWVlemUoMCkpICAjICgxLCBtYXhfbGVuLCBkX21vZGVsKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLmRyb3BvdXQoeCArIHNlbGYucGVbOiwgOnguc2l6ZSgxKV0pXG5cbmNsYXNzIFRTVHJhbnNmb3JtZXJFbmNvZGVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGlucHV0X2RpbSwgZF9tb2RlbD02NCwgbmhlYWQ9NCwgbnVtX2xheWVycz0yLCBob3Jpem9uPTI0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW1iZWQgID0gbm4uTGluZWFyKGlucHV0X2RpbSwgZF9tb2RlbClcbiAgICAgICAgc2VsZi5wb3NfZW5jID0gUG9zaXRpb25hbEVuY29kaW5nKGRfbW9kZWwpXG4gICAgICAgIGVuY19sYXllciAgID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyTGF5ZXIoZF9tb2RlbCwgbmhlYWQsIGRpbV9mZWVkZm9yd2FyZD0xMjgsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IG5uLlRyYW5zZm9ybWVyRW5jb2RlcihlbmNfbGF5ZXIsIG51bV9sYXllcnM9bnVtX2xheWVycylcbiAgICAgICAgc2VsZi5oZWFkICAgID0gbm4uTGluZWFyKGRfbW9kZWwsIGhvcml6b24pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgIyB4OiAoYmF0Y2gsIHNlcV9sZW4sIGlucHV0X2RpbSlcbiAgICAgICAgeiA9IHNlbGYucG9zX2VuYyhzZWxmLmVtYmVkKHgpKSAgICMgKGJhdGNoLCBzZXFfbGVuLCBkX21vZGVsKVxuICAgICAgICB6ID0gc2VsZi5lbmNvZGVyKHopICAgICAgICAgICAgICAgIyAoYmF0Y2gsIHNlcV9sZW4sIGRfbW9kZWwpXG4gICAgICAgIHJldHVybiBzZWxmLmhlYWQoels6LCAtMSwgOl0pICAgICAjIChiYXRjaCwgaG9yaXpvbikg4oCUIHVzZSBsYXN0IHRva2VuXG5cbm1vZGVsID0gVFNUcmFuc2Zvcm1lckVuY29kZXIoaW5wdXRfZGltPTEsIGRfbW9kZWw9NjQsIG5oZWFkPTQsIG51bV9sYXllcnM9MiwgaG9yaXpvbj0yNClcbnggPSB0b3JjaC5yYW5kbig4LCA5NiwgMSkgICAgIyBiYXRjaD04LCBzZXE9OTYsIGZlYXR1cmVzPTFcbm91dCA9IG1vZGVsKHgpXG5wcmludChmXHUwMDI3SW5wdXQ6IHt4LnNoYXBlfSAgT3V0cHV0OiB7b3V0LnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbmZvcm1lcjogUHJvYlNwYXJzZSBBdHRlbnRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluZm9ybWVyIChaaG91IGV0IGFsLiwgMjAyMSkgaW50cm9kdWNlcyBQcm9iU3BhcnNlIHNlbGYtYXR0ZW50aW9uIHRvIHJlZHVjZSBjb21wbGV4aXR5IGZyb20gTyhMwrIpIHRvIE8oTCBsb2cgTCkuIFRoZSBrZXkgb2JzZXJ2YXRpb246IGluIGZ1bGwgYXR0ZW50aW9uLCBtb3N0IHF1ZXJ5IHZlY3RvcnMgaGF2ZSBuZWFybHkgdW5pZm9ybSBhdHRlbnRpb24gZGlzdHJpYnV0aW9ucyBhbmQgY29udHJpYnV0ZSBsaXR0bGUgaW5mb3JtYXRpb24uIEluZm9ybWVyIG1lYXN1cmVzIHF1ZXJ5IHNwYXJzaXR5IGFzIE0oceG1oiwgSykgPSBtYXhfaihx4bWia+KxvOG1gC/iiJpkKSAtIDEvTMK3zqPisbwoceG1omvisbzhtYAv4oiaZCksIHNlbGVjdHMgdGhlIHRvcC11PU8oTCBsb2cgTCkgcXVlcmllcyB3aXRoIGhpZ2hlc3QgTSAobW9zdCBub24tdW5pZm9ybSksIGFuZCBjb21wdXRlcyBmdWxsIGF0dGVudGlvbiBvbmx5IGZvciB0aG9zZSwgcmVwbGFjaW5nIHRoZSByZXN0IHdpdGggdGhlIGF2ZXJhZ2UgdmFsdWUgVsyELiBUaGUgZGlzdGlsbGluZyBlbmNvZGVyIGZ1cnRoZXIgaGFsdmVzIHRoZSBzZXF1ZW5jZSBsZW5ndGggYmV0d2VlbiBjb25zZWN1dGl2ZSBlbmNvZGVyIGxheWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGRURmb3JtZXI6IEZyZXF1ZW5jeS1FbmhhbmNlZCBEZWNvbXBvc2VkIFRyYW5zZm9ybWVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGRURmb3JtZXIgKFpob3UgZXQgYWwuLCAyMDIyKSBhcHBsaWVzIGRlY29tcG9zaXRpb24gKHNlYXNvbmFsLXRyZW5kKSBiZWZvcmUgZWFjaCBUcmFuc2Zvcm1lciBibG9jayBhbmQgcmVwbGFjZXMgdGhlIHNlbGYtYXR0ZW50aW9uIHdpdGggYSBmcmVxdWVuY3ktZW5oYW5jZWQgbWVjaGFuaXNtOiByYW5kb21seSBzZWxlY3QgYSBmaXhlZCBzdWJzZXQgb2YgRm91cmllciBvciB3YXZlbGV0IG1vZGVzLCBtaXggdGhlbSB3aXRoIGxlYXJuZWQgd2VpZ2h0cywgYW5kIHRyYW5zZm9ybSBiYWNrLiBUaGlzIGFjaGlldmVzIE8oTCkgY29tcGxleGl0eSBwZXIgbGF5ZXIg4oCUIGxpbmVhciBpbiBzZXF1ZW5jZSBsZW5ndGgg4oCUIHdoaWxlIGNhcHR1cmluZyBnbG9iYWwgcGVyaW9kaWMgc3RydWN0dXJlIHRoYXQgbG9jYWwgYXR0ZW50aW9uIG1pc3Nlcy4gVGhlIHJhbmRvbSBtb2RlIHNlbGVjdGlvbiBhY3RzIGFzIGEgZm9ybSBvZiByZWd1bGFyaXNhdGlvbiwgcHJldmVudGluZyB0aGUgbW9kZWwgZnJvbSBtZW1vcmlzaW5nIHNwZWNpZmljIGZyZXF1ZW5jeSBjb21wb25lbnRzLiBGRURmb3JtZXIgYWNoaWV2ZXMgY29tcGV0aXRpdmUgYmVuY2htYXJrIHBlcmZvcm1hbmNlIGF0IHNpZ25pZmljYW50bHkgbG93ZXIgY29tcHV0ZSB0aGFuIGZ1bGwtYXR0ZW50aW9uIHZhcmlhbnRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1dG9mb3JtZXI6IEF1dG8tQ29ycmVsYXRpb24gTWVjaGFuaXNtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdXRvZm9ybWVyIChXdSBldCBhbC4sIDIwMjEpIHJlcGxhY2VzIGF0dGVudGlvbiBlbnRpcmVseSB3aXRoIGFuIEF1dG8tQ29ycmVsYXRpb24gbWVjaGFuaXNtLiBUaGUgY29ycmVsYXRpb24gYmV0d2VlbiB0aGUgcXVlcnkgc2VxdWVuY2UgeOKCnCBhbmQgYSBsYWdnZWQgdmVyc2lvbiBvZiB0aGUga2V5IHNlcXVlbmNlIHjigpzigovPhCBpcyBjb21wdXRlZCB2aWEgRmFzdCBGb3VyaWVyIFRyYW5zZm9ybTogUijPhCkgPSBJRkZUKEZGVCh4KcK3RkZUKih4KSkuIFRoaXMgY2FwdHVyZXMgcGVyaW9kaWMgZGVwZW5kZW5jaWVzIGRpcmVjdGx5IGluIHRoZSBmcmVxdWVuY3kgZG9tYWluIGluIE8oTCBsb2cgTCkuIEluc3RlYWQgb2Ygc29mdG1heCBvdmVyIHBvc2l0aW9ucywgQXV0b2Zvcm1lciBhZ2dyZWdhdGVzIHRoZSB0b3AtayBtb3N0IGNvcnJlbGF0ZWQgbGFncywgcHJlc2VydmluZyB0aGUgc2VyaWVzIHN0cnVjdHVyZS4gU2VyaWVzIGRlY29tcG9zaXRpb24gKHRyZW5kLWN5Y2xpY2FsICsgcmVzaWR1YWwgYmxvY2tzKSBpcyBhcHBsaWVkIGJlZm9yZSBlYWNoIGF0dGVudGlvbiBhbmQgZmVlZGZvcndhcmQgbGF5ZXIgdG8gc3RhYmlsaXNlIGxlYXJuaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBhdGNoVFNUOiBQYXRjaGluZyBhbmQgQ2hhbm5lbCBJbmRlcGVuZGVuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBhdGNoVFNUIChOaWUgZXQgYWwuLCAyMDIzKSBkcmFtYXRpY2FsbHkgc2ltcGxpZmllcyBUcmFuc2Zvcm1lci1iYXNlZCBmb3JlY2FzdGluZyBieSBkaXZpZGluZyB0aGUgaW5wdXQgd2luZG93IGludG8gbm9uLW92ZXJsYXBwaW5nIChvciBzbGlnaHRseSBvdmVybGFwcGluZykgcGF0Y2hlcyBvZiBsZW5ndGggUC4gQSB3aW5kb3cgb2YgTCB0aW1lIHN0ZXBzIGJlY29tZXMgTC9QIHRva2VucywgcmVkdWNpbmcgdGhlIGF0dGVudGlvbiBjb21wdXRhdGlvbiBmcm9tIE8oTMKyKSB0byBPKChML1ApwrIpLiBXaXRoIEw9NTEyIGFuZCBQPTE2LCBzZXF1ZW5jZSBsZW5ndGggZHJvcHMgZnJvbSA1MTIgdG8gMzIg4oCUIGEgMjU2w5cgcmVkdWN0aW9uIGluIGF0dGVudGlvbiBjb3N0LiBFYWNoIHVuaXZhcmlhdGUgY2hhbm5lbCBpcyBwcm9jZXNzZWQgaW5kZXBlbmRlbnRseSAoY2hhbm5lbCBpbmRlcGVuZGVuY2UpLCBhbGxvd2luZyB0aGUgbW9kZWwgdG8gYmUgcHJldHJhaW5lZCBvbiBvbmUgc2V0IG9mIHNlcmllcyBhbmQgZmluZS10dW5lZCBvbiBhbm90aGVyIHdpdGggYSBkaWZmZXJlbnQgbnVtYmVyIG9mIGNoYW5uZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuY2xhc3MgUGF0Y2hFbWJlZGRpbmcobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgcGF0Y2hfbGVuLCBkX21vZGVsLCBzdHJpZGU9Tm9uZSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBhdGNoX2xlbiA9IHBhdGNoX2xlblxuICAgICAgICBzZWxmLnN0cmlkZSAgICA9IHN0cmlkZSBvciBwYXRjaF9sZW5cbiAgICAgICAgc2VsZi5wcm9qICAgICAgPSBubi5MaW5lYXIocGF0Y2hfbGVuLCBkX21vZGVsKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgICMgeDogKGJhdGNoLCB0aW1lKSDigJQgc2luZ2xlIGNoYW5uZWxcbiAgICAgICAgQiwgVCA9IHguc2hhcGVcbiAgICAgICAgIyBVbmZvbGQgaW50byBwYXRjaGVzXG4gICAgICAgIHBhdGNoZXMgPSB4LnVuZm9sZCgxLCBzZWxmLnBhdGNoX2xlbiwgc2VsZi5zdHJpZGUpICAjIChCLCBuX3BhdGNoZXMsIHBhdGNoX2xlbilcbiAgICAgICAgcmV0dXJuIHNlbGYucHJvaihwYXRjaGVzKSAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIChCLCBuX3BhdGNoZXMsIGRfbW9kZWwpXG5cbmNsYXNzIFBhdGNoVFNUKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHNlcV9sZW49NTEyLCBwYXRjaF9sZW49MTYsIGRfbW9kZWw9MTI4LCBuaGVhZD04LFxuICAgICAgICAgICAgICAgICBudW1fbGF5ZXJzPTMsIGhvcml6b249OTYsIGRyb3BvdXQ9MC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucGF0Y2hfZW1iZWQgPSBQYXRjaEVtYmVkZGluZyhwYXRjaF9sZW4sIGRfbW9kZWwpXG4gICAgICAgIG5fcGF0Y2hlcyA9IChzZXFfbGVuIC0gcGF0Y2hfbGVuKSAvLyBwYXRjaF9sZW4gKyAxXG4gICAgICAgIGVuY19sYXllciAgPSBubi5UcmFuc2Zvcm1lckVuY29kZXJMYXllcihcbiAgICAgICAgICAgIGRfbW9kZWwsIG5oZWFkLCBkaW1fZmVlZGZvcndhcmQ9ZF9tb2RlbCAqIDQsXG4gICAgICAgICAgICBkcm9wb3V0PWRyb3BvdXQsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IG5uLlRyYW5zZm9ybWVyRW5jb2RlcihlbmNfbGF5ZXIsIG51bV9sYXllcnMpXG4gICAgICAgIHNlbGYuaGVhZCAgICA9IG5uLkxpbmVhcihuX3BhdGNoZXMgKiBkX21vZGVsLCBob3Jpem9uKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgICMgeDogKGJhdGNoLCBjaGFubmVscywgdGltZSlcbiAgICAgICAgQiwgQywgVCA9IHguc2hhcGVcbiAgICAgICAgb3V0cyA9IFtdXG4gICAgICAgIGZvciBjIGluIHJhbmdlKEMpOiAgICAgICAgICAgIyBjaGFubmVsIGluZGVwZW5kZW5jZVxuICAgICAgICAgICAgeiA9IHNlbGYucGF0Y2hfZW1iZWQoeFs6LCBjLCA6XSkgICAjIChCLCBuX3BhdGNoZXMsIGRfbW9kZWwpXG4gICAgICAgICAgICB6ID0gc2VsZi5lbmNvZGVyKHopICAgICAgICAgICAgICAgICAjIChCLCBuX3BhdGNoZXMsIGRfbW9kZWwpXG4gICAgICAgICAgICBvdXRzLmFwcGVuZChzZWxmLmhlYWQoei5mbGF0dGVuKDEpKSkjIChCLCBob3Jpem9uKVxuICAgICAgICByZXR1cm4gdG9yY2guc3RhY2sob3V0cywgZGltPTEpICAgICAgICAgIyAoQiwgQywgaG9yaXpvbilcblxubW9kZWwgPSBQYXRjaFRTVChzZXFfbGVuPTUxMiwgcGF0Y2hfbGVuPTE2LCBkX21vZGVsPTEyOCwgbmhlYWQ9OCwgaG9yaXpvbj05NilcbnggPSB0b3JjaC5yYW5kbig0LCA3LCA1MTIpICAgIyBiYXRjaD00LCBjaGFubmVscz03LCB0aW1lPTUxMlxub3V0ID0gbW9kZWwoeClcbnByaW50KGZcdTAwMjdJbnB1dDoge3guc2hhcGV9ICBPdXRwdXQ6IHtvdXQuc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZXRyYWluaW5nIGFuZCBGaW5lLVR1bmluZyB3aXRoIFBhdGNoVFNUIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE1hc2tlZFBhdGNoVFNUKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiXG4gICAgUGF0Y2hUU1QgcHJldHJhaW5pbmcgdmlhIG1hc2tlZCBwYXRjaCBwcmVkaWN0aW9uIChhbmFsb2dvdXMgdG8gQkVSVCBNTE0pLlxuICAgIFJhbmRvbWx5IG1hc2tzIHNvbWUgcGF0Y2hlczsgcHJlZGljdHMgdGhlaXIgb3JpZ2luYWwgdmFsdWVzLlxuICAgIFwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBzZXFfbGVuPTUxMiwgcGF0Y2hfbGVuPTE2LCBkX21vZGVsPTEyOCwgbmhlYWQ9OCxcbiAgICAgICAgICAgICAgICAgbnVtX2xheWVycz0zLCBtYXNrX3JhdGlvPTAuNCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBhdGNoX2xlbiAgPSBwYXRjaF9sZW5cbiAgICAgICAgc2VsZi5tYXNrX3JhdGlvID0gbWFza19yYXRpb1xuICAgICAgICBzdHJpZGUgPSBwYXRjaF9sZW5cbiAgICAgICAgbl9wYXRjaGVzID0gKHNlcV9sZW4gLSBwYXRjaF9sZW4pIC8vIHN0cmlkZSArIDFcbiAgICAgICAgc2VsZi5wYXRjaF9wcm9qICA9IG5uLkxpbmVhcihwYXRjaF9sZW4sIGRfbW9kZWwpXG4gICAgICAgIHNlbGYubWFza190b2tlbiAgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3MoMSwgMSwgZF9tb2RlbCkpXG4gICAgICAgIGVuY19sYXllciA9IG5uLlRyYW5zZm9ybWVyRW5jb2RlckxheWVyKFxuICAgICAgICAgICAgZF9tb2RlbCwgbmhlYWQsIGRfbW9kZWwgKiA0LCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICBzZWxmLmVuY29kZXIgID0gbm4uVHJhbnNmb3JtZXJFbmNvZGVyKGVuY19sYXllciwgbnVtX2xheWVycylcbiAgICAgICAgc2VsZi5oZWFkICAgICA9IG5uLkxpbmVhcihkX21vZGVsLCBwYXRjaF9sZW4pICAjIHJlY29uc3RydWN0IHBhdGNoXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgQiwgVCA9IHguc2hhcGVcbiAgICAgICAgcGF0Y2hlcyA9IHgudW5mb2xkKDEsIHNlbGYucGF0Y2hfbGVuLCBzZWxmLnBhdGNoX2xlbikgICMgKEIsIE4sIFApXG4gICAgICAgIE4gPSBwYXRjaGVzLnNoYXBlWzFdXG4gICAgICAgIHogPSBzZWxmLnBhdGNoX3Byb2oocGF0Y2hlcykgICMgKEIsIE4sIGRfbW9kZWwpXG4gICAgICAgIG1hc2sgPSB0b3JjaC5yYW5kKEIsIE4pIFx1MDAzYyBzZWxmLm1hc2tfcmF0aW9cbiAgICAgICAgelttYXNrXSA9IHNlbGYubWFza190b2tlbi5leHBhbmQoQiwgTiwgLTEpW21hc2tdXG4gICAgICAgIHogPSBzZWxmLmVuY29kZXIoeilcbiAgICAgICAgcmVjb24gPSBzZWxmLmhlYWQoeikgICAgICAgICAgIyAoQiwgTiwgUClcbiAgICAgICAgbG9zcyAgPSAoKHJlY29uW21hc2tdIC0gcGF0Y2hlcy5kZXRhY2goKVttYXNrXSkgKiogMikubWVhbigpXG4gICAgICAgIHJldHVybiBsb3NzLCByZWNvblxuXG5tb2RlbCA9IE1hc2tlZFBhdGNoVFNUKHNlcV9sZW49NTEyLCBwYXRjaF9sZW49MTYsIGRfbW9kZWw9MTI4LCBuaGVhZD04LCBudW1fbGF5ZXJzPTMpXG54ID0gdG9yY2gucmFuZG4oNCwgNTEyKVxubG9zcywgcmVjb24gPSBtb2RlbCh4KVxucHJpbnQoZlx1MDAyN1ByZXRyYWluaW5nIHJlY29uc3RydWN0aW9uIGxvc3M6IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JlY29uc3RydWN0ZWQgcGF0Y2hlcyBzaGFwZToge3JlY29uLnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlBhdGNoVFNUIFByZXRyYWluaW5nIEVtcGlyaWNhbCBGaW5kaW5ncyIsImNvbnRlbnQiOiJQYXRjaFRTVCBwcmV0cmFpbmVkIG9uIEVUVGgxIGFuZCBmaW5lLXR1bmVkIG9uIEVUVGgyIGFjaGlldmVzIGxvd2VyIE1TRSB0aGFuIHRyYWluaW5nIGZyb20gc2NyYXRjaCBvbiBFVFRoMiBhbG9uZSwgZGVtb25zdHJhdGluZyBtZWFuaW5nZnVsIHRyYW5zZmVyIGFjcm9zcyBkYXRhc2V0cy4gVGhlIGNoYW5uZWwtaW5kZXBlbmRlbnQgZGVzaWduIG1lYW5zIHRoZSBwcmV0cmFpbmVkIGVuY29kZXIgY2FuIGJlIGFwcGxpZWQgdG8gYW55IHVuaXZhcmlhdGUgY2hhbm5lbCByZWdhcmRsZXNzIG9mIHRoZSBudW1iZXIgb2YgdmFyaWF0ZXMgaW4gdGhlIHRhcmdldCBkYXRhc2V0IOKAlCBvbmx5IHRoZSBsaW5lYXIgaGVhZCBuZWVkcyByZXBsYWNlbWVudCBhbmQgZmluZS10dW5pbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdHJhaW5pbmcgcmVjaXBlIGZvciBQYXRjaFRTVCBwcmV0cmFpbmluZzogKDEpIHVzZSBtYXNrZWQgcGF0Y2ggcmF0aW8gMC404oCTMC42OyAoMikgcHJldHJhaW4gZm9yIDEwMCBlcG9jaHMgd2l0aCBBZGFtVyAobHI9MWUtNCwgd2VpZ2h0X2RlY2F5PTFlLTIpIG9uIHRoZSBzb3VyY2UgZGF0YXNldDsgKDMpIHJlcGxhY2UgdGhlIHJlY29uc3RydWN0aW9uIGhlYWQgd2l0aCBhIGZvcmVjYXN0aW5nIGhlYWQgKGxpbmVhciBsYXllciBtYXBwaW5nIGZsYXR0ZW5lZCBwYXRjaCBlbWJlZGRpbmdzIHRvIEggb3V0cHV0cyk7ICg0KSBmaW5lLXR1bmUgdGhlIGZ1bGwgbW9kZWwgYXQgbHI9MWUtNSBmb3IgMjAgZXBvY2hzLiBBcHBseWluZyBpbnN0YW5jZSBub3JtYWxpc2F0aW9uIChSZXZJTikg4oCUIG5vcm1hbGlzZSBlYWNoIGlucHV0IHdpbmRvdyB0byB6ZXJvIG1lYW4gYW5kIHVuaXQgdmFyaWFuY2UsIHRoZW4gcmV2ZXJzZSBhdCBvdXRwdXQg4oCUIGlzIGNyaXRpY2FsIGZvciBzdGFiaWxpc2luZyB0cmFpbmluZyBhY3Jvc3Mgc2VyaWVzIHdpdGggZGlmZmVyZW50IHNjYWxlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wbGV4aXR5IGFuZCBBcmNoaXRlY3R1cmUgQ29tcGFyaXNvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBwYW5kYXMgYXMgcGRcblxuZGVmIGF0dGVudGlvbl9jb21wbGV4aXR5KEwsIGRfbW9kZWwsIG5faGVhZHMsIG1vZGVsPVx1MDAyN2Z1bGxcdTAwMjcpOlxuICAgIFwiXCJcIkFwcHJveGltYXRlIEZMT1BzIGZvciBvbmUgc2VsZi1hdHRlbnRpb24gbGF5ZXIuXCJcIlwiXG4gICAgaWYgbW9kZWwgPT0gXHUwMDI3ZnVsbFx1MDAyNzpcbiAgICAgICAgcmV0dXJuIEwgKiBMICogZF9tb2RlbCAgICAgICAgICAjIE8oTF4yICogZClcbiAgICBlbGlmIG1vZGVsID09IFx1MDAyN3Byb2JzcGFyc2VcdTAwMjc6XG4gICAgICAgIHUgPSBpbnQoTCAqIG5wLmxvZyhMKSkgICAgICAgICAgIyBzZWxlY3RlZCBxdWVyaWVzXG4gICAgICAgIHJldHVybiB1ICogTCAqIGRfbW9kZWwgICAgICAgICAgIyBPKEwgbG9nIEwgKiBkKVxuICAgIGVsaWYgbW9kZWwgPT0gXHUwMDI3YXV0b2NvcnJcdTAwMjc6XG4gICAgICAgIHJldHVybiBMICogbnAubG9nKEwpICogZF9tb2RlbCAgIyBGRlQtYmFzZWQgTyhMIGxvZyBMICogZClcbiAgICBlbGlmIG1vZGVsID09IFx1MDAyN3BhdGNoXHUwMDI3OlxuICAgICAgICBuX3BhdGNoZXMgPSBMIC8vIDE2ICAgICAgICAgICAgICMgcGF0Y2ggc2l6ZSBQPTE2XG4gICAgICAgIHJldHVybiBuX3BhdGNoZXMqKjIgKiBkX21vZGVsICAgIyBPKChML1ApXjIgKiBkKVxuICAgIGVsaWYgbW9kZWwgPT0gXHUwMDI3ZmVkXHUwMDI3OlxuICAgICAgICBtb2RlcyA9IG1pbihMIC8vIDIsIDY0KSAgICAgICAgICMgc2VsZWN0ZWQgZnJlcXVlbmN5IG1vZGVzXG4gICAgICAgIHJldHVybiBMICogbW9kZXMgKiBkX21vZGVsICAgICAgIyBPKEwgKiBtb2RlcyAqIGQpIOKJiCBPKEwpXG5cbkxfdmFsdWVzID0gWzk2LCAzMzYsIDcyMF1cbmRfbW9kZWwgPSA1MTJcbnJlc3VsdHMgPSBbXVxuZm9yIEwgaW4gTF92YWx1ZXM6XG4gICAgcm93ID0ge1x1MDAyN0xcdTAwMjc6IEx9XG4gICAgZm9yIG5hbWUgaW4gW1x1MDAyN2Z1bGxcdTAwMjcsIFx1MDAyN3Byb2JzcGFyc2VcdTAwMjcsIFx1MDAyN2F1dG9jb3JyXHUwMDI3LCBcdTAwMjdwYXRjaFx1MDAyNywgXHUwMDI3ZmVkXHUwMDI3XTpcbiAgICAgICAgcm93W25hbWVdID0gaW50KGF0dGVudGlvbl9jb21wbGV4aXR5KEwsIGRfbW9kZWwsIDgsIG5hbWUpKVxuICAgIHJlc3VsdHMuYXBwZW5kKHJvdylcblxuZGYgPSBwZC5EYXRhRnJhbWUocmVzdWx0cykuc2V0X2luZGV4KFx1MDAyN0xcdTAwMjcpXG5wcmludChcdTAwMjdTZWxmLWF0dGVudGlvbiBGTE9QcyAocmVsYXRpdmUgdG8gRnVsbCBhdCBMPTk2KTpcdTAwMjcpXG5iYXNlID0gZGYubG9jWzk2LCBcdTAwMjdmdWxsXHUwMDI3XVxucHJpbnQoKGRmIC8gYmFzZSkucm91bmQoMSkudG9fc3RyaW5nKCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9uZy1Ib3Jpem9uIEZvcmVjYXN0aW5nIEJlbmNobWFyayJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIkF0dGVudGlvbiBNZWNoYW5pc20iLCJDb21wbGV4aXR5IiwiS2V5IElubm92YXRpb24iLCJFVFRoMSBNU0UgKGg9NzIwKSIsIk5vdGVzIl0sInJvd3MiOltbIkluZm9ybWVyIiwiUHJvYlNwYXJzZSAodG9wLXUgcXVlcmllcykiLCJPKEwgbG9nIEwpIiwiU3BhcnNlIGF0dGVudGlvbiArIGRpc3RpbGxpbmcgZW5jb2RlciIsIn4wLjg2NSIsIkJlc3QgZm9yIHZlcnkgbG9uZyBpbnB1dHMgKEwgXHUwMDNlIDEwMDApIl0sWyJBdXRvZm9ybWVyIiwiQXV0by1Db3JyZWxhdGlvbiAoRkZUKSIsIk8oTCBsb2cgTCkiLCJGcmVxdWVuY3ktZG9tYWluIHNlcmllcyBkZWNvbXBvc2l0aW9uIiwifjAuNjgzIiwiU3Ryb25nIHNlYXNvbmFsIHBhdHRlcm4gY2FwdHVyZSJdLFsiRkVEZm9ybWVyIiwiRnJlcXVlbmN5LWVuaGFuY2VkIGRlY29tcC4iLCJPKEwpIiwiRm91cmllci9XYXZlbGV0IHJhbmRvbSBtb2RlIG1peGluZyIsIn4wLjYxMSIsIkVmZmljaWVudDsgZnJlcXVlbmN5IG1peGluZyBsYXllciJdLFsiUGF0Y2hUU1QiLCJGdWxsIGF0dGVudGlvbiBvbiBwYXRjaGVzIiwiTygoTC9QKcKyKSIsIlBhdGNoaW5nICsgY2hhbm5lbCBpbmRlcGVuZGVuY2UgKyBwcmV0cmFpbiIsIn4wLjQxMyIsIlN0YXRlLW9mLXRoZS1hcnQgYWNyb3NzIEVUVCBiZW5jaG1hcmtzIl0sWyJWYW5pbGxhIFRyYW5zZm9ybWVyIiwiRnVsbCBzZWxmLWF0dGVudGlvbiIsIk8oTMKyKSIsIkJhc2VsaW5lIOKAlCBxdWFkcmF0aWMgYm90dGxlbmVjayIsIn4wLjk0MSIsIk9ubHkgcHJhY3RpY2FsIGZvciBzaG9ydCBMIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlBhdGNoVFNUIHdpdGggcGF0Y2ggc2l6ZSBQPTE2IGFuZCBzdHJpZGUgUD0xNiByZWR1Y2VzIGF0dGVudGlvbiBjb3N0IGJ5IFDCsiA9IDI1NsOXIHZlcnN1cyBmdWxsLXNlcXVlbmNlIFRyYW5zZm9ybWVyLiIsIkNoYW5uZWwgaW5kZXBlbmRlbmNlIChzZXBhcmF0ZSBlbmNvZGVyIHBlciB2YXJpYXRlKSBvdXRwZXJmb3JtcyBjaGFubmVsIG1peGluZyBvbiBtb3N0IGxvbmctaG9yaXpvbiBiZW5jaG1hcmtzIOKAlCBtdWx0aXZhcmlhdGUgbWl4aW5nIGNhbiBpbnRyb2R1Y2Ugbm9pc2UuIiwiUHJldHJhaW5pbmcgd2l0aCBtYXNrZWQgcGF0Y2ggcmVjb25zdHJ1Y3Rpb24gKGFuYWxvZ291cyB0byBCRVJUIE1MTSkgcHJvdmlkZXMgYSB1c2VmdWwgaW5pdGlhbGlzYXRpb24gZXZlbiB3aXRoIGxpbWl0ZWQgbGFiZWxsZWQgZGF0YS4iLCJGRURmb3JtZXIgYW5kIEF1dG9mb3JtZXIgZGVjb21wb3NlIHNlcmllcyBpbnRvIHRyZW5kIGFuZCByZXNpZHVhbCBiZWZvcmUgZWFjaCBsYXllciwgbWFraW5nIHRoZW0gbW9yZSBpbnRlcnByZXRhYmxlIHRoYW4gZW5kLXRvLWVuZCBibGFjayBib3hlcy4iLCJGb3Igc2hvcnQtdG8tbWVkaXVtIGhvcml6b25zIChoIOKJpCA0OCksIExpZ2h0R0JNIHdpdGggbGFnIGZlYXR1cmVzIGFuZCBOSElUUyBvZnRlbiBvdXRwZXJmb3JtIGFsbCBUcmFuc2Zvcm1lciB2YXJpYW50cyBhdCBhIGZyYWN0aW9uIG9mIHRoZSBjb21wdXRlIGNvc3QuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFx1MDAyN0FyZSBUcmFuc2Zvcm1lcnMgRWZmZWN0aXZlIGZvciBUaW1lIFNlcmllcyBGb3JlY2FzdGluZz9cdTAwMjcgcGFwZXIgKFplbmcgZXQgYWwuLCAyMDIzKSBzaG93ZWQgdGhhdCBhIHNpbmdsZSBsaW5lYXIgbGF5ZXIgKERMaW5lYXIpIG1hdGNoZXMgb3Igb3V0cGVyZm9ybXMgYWxsIFRyYW5zZm9ybWVyLWJhc2VkIG1vZGVscyBvbiB0aGUgRVRUIGJlbmNobWFya3MsIHN1Z2dlc3RpbmcgdGhhdCB0ZW1wb3JhbCBkZXBlbmRlbmN5IOKAlCBub3QgY29tcGxleCBhdHRlbnRpb24g4oCUIGRyaXZlcyBtb3N0IG9mIHRoZSBzaWduYWwuIFBhdGNoVFNUXHUwMDI3cyBpbXByb3ZlbWVudCBpcyBwYXJ0bHkgYXR0cmlidXRlZCB0byBpdHMgbGFyZ2VyIGVmZmVjdGl2ZSBpbnB1dCB3aW5kb3cgKEw9NTEyIHZzIEw9OTYgZm9yIGVhcmxpZXIgbW9kZWxzKSByYXRoZXIgdGhhbiB0aGUgVHJhbnNmb3JtZXIgYXJjaGl0ZWN0dXJlIGl0c2VsZi4gVGhlIGxlc3NvbjogYWx3YXlzIGluY2x1ZGUgYSBsaW5lYXIgYmFzZWxpbmUgYW5kIGFuIE5ISVRTL05CRUFUUyBiYXNlbGluZSBiZWZvcmUgZGVwbG95aW5nIGEgVHJhbnNmb3JtZXIgZm9yIHRpbWUgc2VyaWVzLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Transformer-Based Forecasting — Informer, Autoformer, PatchTST

The vanilla Transformer encoder applies full self-attention over all L input tokens, requiring O(L²) memory and compute — prohibitive for long time series (L=1000 or more). A wave of specialised architectures addressed this: Informer introduced ProbSparse attention with O(L log L) complexity; Autoformer replaced attention with an auto-correlation mechanism; FEDformer moved to frequency-domain mixing; PatchTST took a different approach, grouping time steps into patches to reduce sequence length dramatically and enabling large-scale pretraining and fine-tuning across datasets.

## Vanilla Transformer for Time Series

The standard Transformer self-attention is Attention(Q,K,V) = softmax(QKᵀ/√d)V. For a sequence of length L, the attention matrix is L×L, requiring O(L²) time and memory. Positional encoding is needed because self-attention is permutation-invariant: sin(pos/10000^(2i/d)) and cos(pos/10000^(2i/d)) are concatenated to token embeddings. The encoder processes the input window; the decoder uses encoder-decoder cross-attention to generate the output sequence autoregressively. For L=720 (a common long-horizon benchmark), the attention matrix has 518,400 elements per head — barely tractable even on GPU.

```python
import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        pe = torch.zeros(max_len, d_model)
        pos = torch.arange(0, max_len).unsqueeze(1).float()
        div = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(pos * div)
        pe[:, 1::2] = torch.cos(pos * div)
        self.register_buffer('pe', pe.unsqueeze(0))  # (1, max_len, d_model)

    def forward(self, x):
        return self.dropout(x + self.pe[:, :x.size(1)])

class TSTransformerEncoder(nn.Module):
    def __init__(self, input_dim, d_model=64, nhead=4, num_layers=2, horizon=24):
        super().__init__()
        self.embed  = nn.Linear(input_dim, d_model)
        self.pos_enc = PositionalEncoding(d_model)
        enc_layer   = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward=128, batch_first=True)
        self.encoder = nn.TransformerEncoder(enc_layer, num_layers=num_layers)
        self.head    = nn.Linear(d_model, horizon)

    def forward(self, x):
        # x: (batch, seq_len, input_dim)
        z = self.pos_enc(self.embed(x))   # (batch, seq_len, d_model)
        z = self.encoder(z)               # (batch, seq_len, d_model)
        return self.head(z[:, -1, :])     # (batch, horizon) — use last token

model = TSTransformerEncoder(input_dim=1, d_model=64, nhead=4, num_layers=2, horizon=24)
x = torch.randn(8, 96, 1)    # batch=8, seq=96, features=1
out = model(x)
print(f'Input: {x.shape}  Output: {out.shape}')
```

## Informer: ProbSparse Attention

Informer (Zhou et al., 2021) introduces ProbSparse self-attention to reduce complexity from O(L²) to O(L log L). The key observation: in full attention, most query vectors have nearly uniform attention distributions and contribute little information. Informer measures query sparsity as M(qᵢ, K) = max_j(qᵢkⱼᵀ/√d) - 1/L·Σⱼ(qᵢkⱼᵀ/√d), selects the top-u=O(L log L) queries with highest M (most non-uniform), and computes full attention only for those, replacing the rest with the average value V̄. The distilling encoder further halves the sequence length between consecutive encoder layers.

## FEDformer: Frequency-Enhanced Decomposed Transformer

FEDformer (Zhou et al., 2022) applies decomposition (seasonal-trend) before each Transformer block and replaces the self-attention with a frequency-enhanced mechanism: randomly select a fixed subset of Fourier or wavelet modes, mix them with learned weights, and transform back. This achieves O(L) complexity per layer — linear in sequence length — while capturing global periodic structure that local attention misses. The random mode selection acts as a form of regularisation, preventing the model from memorising specific frequency components. FEDformer achieves competitive benchmark performance at significantly lower compute than full-attention variants.

## Autoformer: Auto-Correlation Mechanism

Autoformer (Wu et al., 2021) replaces attention entirely with an Auto-Correlation mechanism. The correlation between the query sequence xₜ and a lagged version of the key sequence xₜ₋τ is computed via Fast Fourier Transform: R(τ) = IFFT(FFT(x)·FFT*(x)). This captures periodic dependencies directly in the frequency domain in O(L log L). Instead of softmax over positions, Autoformer aggregates the top-k most correlated lags, preserving the series structure. Series decomposition (trend-cyclical + residual blocks) is applied before each attention and feedforward layer to stabilise learning.

## PatchTST: Patching and Channel Independence

PatchTST (Nie et al., 2023) dramatically simplifies Transformer-based forecasting by dividing the input window into non-overlapping (or slightly overlapping) patches of length P. A window of L time steps becomes L/P tokens, reducing the attention computation from O(L²) to O((L/P)²). With L=512 and P=16, sequence length drops from 512 to 32 — a 256× reduction in attention cost. Each univariate channel is processed independently (channel independence), allowing the model to be pretrained on one set of series and fine-tuned on another with a different number of channels.

```python
import torch
import torch.nn as nn
import math

class PatchEmbedding(nn.Module):
    def __init__(self, patch_len, d_model, stride=None):
        super().__init__()
        self.patch_len = patch_len
        self.stride    = stride or patch_len
        self.proj      = nn.Linear(patch_len, d_model)

    def forward(self, x):
        # x: (batch, time) — single channel
        B, T = x.shape
        # Unfold into patches
        patches = x.unfold(1, self.patch_len, self.stride)  # (B, n_patches, patch_len)
        return self.proj(patches)                            # (B, n_patches, d_model)

class PatchTST(nn.Module):
    def __init__(self, seq_len=512, patch_len=16, d_model=128, nhead=8,
                 num_layers=3, horizon=96, dropout=0.1):
        super().__init__()
        self.patch_embed = PatchEmbedding(patch_len, d_model)
        n_patches = (seq_len - patch_len) // patch_len + 1
        enc_layer  = nn.TransformerEncoderLayer(
            d_model, nhead, dim_feedforward=d_model * 4,
            dropout=dropout, batch_first=True)
        self.encoder = nn.TransformerEncoder(enc_layer, num_layers)
        self.head    = nn.Linear(n_patches * d_model, horizon)

    def forward(self, x):
        # x: (batch, channels, time)
        B, C, T = x.shape
        outs = []
        for c in range(C):           # channel independence
            z = self.patch_embed(x[:, c, :])   # (B, n_patches, d_model)
            z = self.encoder(z)                 # (B, n_patches, d_model)
            outs.append(self.head(z.flatten(1)))# (B, horizon)
        return torch.stack(outs, dim=1)         # (B, C, horizon)

model = PatchTST(seq_len=512, patch_len=16, d_model=128, nhead=8, horizon=96)
x = torch.randn(4, 7, 512)   # batch=4, channels=7, time=512
out = model(x)
print(f'Input: {x.shape}  Output: {out.shape}')
```

## Pretraining and Fine-Tuning with PatchTST

```python
import torch
import torch.nn as nn

class MaskedPatchTST(nn.Module):
    """
    PatchTST pretraining via masked patch prediction (analogous to BERT MLM).
    Randomly masks some patches; predicts their original values.
    """
    def __init__(self, seq_len=512, patch_len=16, d_model=128, nhead=8,
                 num_layers=3, mask_ratio=0.4):
        super().__init__()
        self.patch_len  = patch_len
        self.mask_ratio = mask_ratio
        stride = patch_len
        n_patches = (seq_len - patch_len) // stride + 1
        self.patch_proj  = nn.Linear(patch_len, d_model)
        self.mask_token  = nn.Parameter(torch.zeros(1, 1, d_model))
        enc_layer = nn.TransformerEncoderLayer(
            d_model, nhead, d_model * 4, batch_first=True)
        self.encoder  = nn.TransformerEncoder(enc_layer, num_layers)
        self.head     = nn.Linear(d_model, patch_len)  # reconstruct patch

    def forward(self, x):
        B, T = x.shape
        patches = x.unfold(1, self.patch_len, self.patch_len)  # (B, N, P)
        N = patches.shape[1]
        z = self.patch_proj(patches)  # (B, N, d_model)
        mask = torch.rand(B, N) < self.mask_ratio
        z[mask] = self.mask_token.expand(B, N, -1)[mask]
        z = self.encoder(z)
        recon = self.head(z)          # (B, N, P)
        loss  = ((recon[mask] - patches.detach()[mask]) ** 2).mean()
        return loss, recon

model = MaskedPatchTST(seq_len=512, patch_len=16, d_model=128, nhead=8, num_layers=3)
x = torch.randn(4, 512)
loss, recon = model(x)
print(f'Pretraining reconstruction loss: {loss.item():.4f}')
print(f'Reconstructed patches shape: {recon.shape}')
```

> **PatchTST Pretraining Empirical Findings**: PatchTST pretrained on ETTh1 and fine-tuned on ETTh2 achieves lower MSE than training from scratch on ETTh2 alone, demonstrating meaningful transfer across datasets. The channel-independent design means the pretrained encoder can be applied to any univariate channel regardless of the number of variates in the target dataset — only the linear head needs replacement and fine-tuning.

The training recipe for PatchTST pretraining: (1) use masked patch ratio 0.4–0.6; (2) pretrain for 100 epochs with AdamW (lr=1e-4, weight_decay=1e-2) on the source dataset; (3) replace the reconstruction head with a forecasting head (linear layer mapping flattened patch embeddings to H outputs); (4) fine-tune the full model at lr=1e-5 for 20 epochs. Applying instance normalisation (RevIN) — normalise each input window to zero mean and unit variance, then reverse at output — is critical for stabilising training across series with different scales.

## Complexity and Architecture Comparison

```python
import numpy as np
import pandas as pd

def attention_complexity(L, d_model, n_heads, model='full'):
    """Approximate FLOPs for one self-attention layer."""
    if model == 'full':
        return L * L * d_model          # O(L^2 * d)
    elif model == 'probsparse':
        u = int(L * np.log(L))          # selected queries
        return u * L * d_model          # O(L log L * d)
    elif model == 'autocorr':
        return L * np.log(L) * d_model  # FFT-based O(L log L * d)
    elif model == 'patch':
        n_patches = L // 16             # patch size P=16
        return n_patches**2 * d_model   # O((L/P)^2 * d)
    elif model == 'fed':
        modes = min(L // 2, 64)         # selected frequency modes
        return L * modes * d_model      # O(L * modes * d) ≈ O(L)

L_values = [96, 336, 720]
d_model = 512
results = []
for L in L_values:
    row = {'L': L}
    for name in ['full', 'probsparse', 'autocorr', 'patch', 'fed']:
        row[name] = int(attention_complexity(L, d_model, 8, name))
    results.append(row)

df = pd.DataFrame(results).set_index('L')
print('Self-attention FLOPs (relative to Full at L=96):')
base = df.loc[96, 'full']
print((df / base).round(1).to_string())
```

## Long-Horizon Forecasting Benchmark

| Model | Attention Mechanism | Complexity | Key Innovation | ETTh1 MSE (h=720) | Notes |
| --- | --- | --- | --- | --- | --- |
| Informer | ProbSparse (top-u queries) | O(L log L) | Sparse attention + distilling encoder | ~0.865 | Best for very long inputs (L > 1000) |
| Autoformer | Auto-Correlation (FFT) | O(L log L) | Frequency-domain series decomposition | ~0.683 | Strong seasonal pattern capture |
| FEDformer | Frequency-enhanced decomp. | O(L) | Fourier/Wavelet random mode mixing | ~0.611 | Efficient; frequency mixing layer |
| PatchTST | Full attention on patches | O((L/P)²) | Patching + channel independence + pretrain | ~0.413 | State-of-the-art across ETT benchmarks |
| Vanilla Transformer | Full self-attention | O(L²) | Baseline — quadratic bottleneck | ~0.941 | Only practical for short L |

- PatchTST with patch size P=16 and stride P=16 reduces attention cost by P² = 256× versus full-sequence Transformer.
- Channel independence (separate encoder per variate) outperforms channel mixing on most long-horizon benchmarks — multivariate mixing can introduce noise.
- Pretraining with masked patch reconstruction (analogous to BERT MLM) provides a useful initialisation even with limited labelled data.
- FEDformer and Autoformer decompose series into trend and residual before each layer, making them more interpretable than end-to-end black boxes.
- For short-to-medium horizons (h ≤ 48), LightGBM with lag features and NHITS often outperform all Transformer variants at a fraction of the compute cost.

The 'Are Transformers Effective for Time Series Forecasting?' paper (Zeng et al., 2023) showed that a single linear layer (DLinear) matches or outperforms all Transformer-based models on the ETT benchmarks, suggesting that temporal dependency — not complex attention — drives most of the signal. PatchTST's improvement is partly attributed to its larger effective input window (L=512 vs L=96 for earlier models) rather than the Transformer architecture itself. The lesson: always include a linear baseline and an NHITS/NBEATS baseline before deploying a Transformer for time series.

---

