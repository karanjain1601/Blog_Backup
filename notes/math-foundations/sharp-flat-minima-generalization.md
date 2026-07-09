---
title: "Sharp vs Flat Minima and Generalization"
slug: "sharp-flat-minima-generalization"
description: "How the curvature of the loss minimum — measured by Hessian eigenvalues — predicts generalization, why SGD finds flat minima, and how SAM explicitly seeks them."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHdvIG1vZGVscyBjYW4gYWNoaWV2ZSBpZGVudGljYWwgdHJhaW5pbmcgbG9zcyB5ZXQgZGlmZmVyIGRyYW1hdGljYWxseSBpbiB0ZXN0IHBlcmZvcm1hbmNlLiBPbmUga2V5IGdlb21ldHJpYyBmYWN0b3I6IHRoZSBjdXJ2YXR1cmUgb2YgdGhlIGxvc3Mgc3VyZmFjZSBhdCB0aGUgbWluaW11bS4gQSBzaGFycCBtaW5pbXVtIGlzIHN1cnJvdW5kZWQgYnkgaGlnaC1jdXJ2YXR1cmUgd2FsbHMg4oCUIGEgdGlueSBwZXJ0dXJiYXRpb24gdG8gd2VpZ2h0cyBjYXVzZXMgYSBsYXJnZSBsb3NzIGluY3JlYXNlLCBhbmQgd2hlbiB0aGUgdHJhaW4vdGVzdCBkaXN0cmlidXRpb25zIGRpZmZlciBzbGlnaHRseSAoYXMgdGhleSBhbHdheXMgZG8pLCB0aGUgbW9kZWwgZ2VuZXJhbGl6ZXMgcG9vcmx5LiBBIGZsYXQgbWluaW11bSBpcyByb2J1c3QgdG8gcGVydHVyYmF0aW9ucyBhbmQgdGVuZHMgdG8gZ2VuZXJhbGl6ZSBiZXR0ZXIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVW5kZXJzdGFuZGluZyBTaGFycCBhbmQgRmxhdCBNaW5pbWEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNoYXJwbmVzcyBpcyBmb3JtYWxseSBxdWFudGlmaWVkIGJ5IHRoZSBIZXNzaWFuIOKIh8KyTCjOuCkgYXQgdGhlIG1pbmltdW0gzrgqLiBUaGUgbGFyZ2VzdCBlaWdlbnZhbHVlIM67X21heCjiiIfCskwpIGdpdmVzIHRoZSB3b3JzdC1jYXNlIGN1cnZhdHVyZTogYSBwZXJ0dXJiYXRpb24gzrUgaW4gdGhlIGRpcmVjdGlvbiBvZiB0aGUgdG9wIGVpZ2VudmVjdG9yIGluY3JlYXNlcyBsb3NzIGJ5IGFwcHJveGltYXRlbHkgKM67X21heC8yKeKAls614oCWwrIuIEZvciBhIGZsYXQgbWluaW11bSDOu19tYXggaXMgc21hbGw7IGZvciBhIHNoYXJwIG1pbmltdW0gaXQgY2FuIGJlIG1pbGxpb25zLiBQQUMtQmF5ZXMgYm91bmRzIGNvbm5lY3Qgc2hhcnBuZXNzIHRvIHRoZSBnZW5lcmFsaXphdGlvbiBnYXA6IGdlbmVyYWxpemF0aW9uX2dhcCDiiYggTyjiiJoozrtfbWF4L24pKSB3aGVyZSBuIGlzIHRyYWluaW5nIHNldCBzaXplLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSG9jaHJlaXRlciBcdTAwMjYgU2NobWlkaHViZXIgMTk5NyIsImNvbnRlbnQiOiJUaGUgb3JpZ2luYWwgZmxhdCBtaW5pbWEgcGFwZXIgYXJndWVkIGZyb20gYW4gTURMIHBlcnNwZWN0aXZlOiBhIGZsYXQgbWluaW11bSBjYW4gYmUgZGVzY3JpYmVkIHdpdGggZmV3ZXIgYml0cyB0aGFuIGEgc2hhcnAgb25lICh5b3UgY2FuIHF1YW50aXplIHRoZSB3ZWlnaHRzIG1vcmUgYWdncmVzc2l2ZWx5IHdpdGhvdXQgY2hhbmdpbmcgdGhlIGxvc3MpLiBMb3dlciBkZXNjcmlwdGlvbiBsZW5ndGggaW1wbGllcyBiZXR0ZXIgZ2VuZXJhbGl6YXRpb24gYnkgT2NjYW1cdTAwMjdzIHJhem9yIC8gTURMIHByaW5jaXBsZS4gTW9kZXJuIFBBQy1CYXllcyB0aGVvcnkgZm9ybWFsaXplcyB0aGlzIGludG8gcXVhbnRpdGF0aXZlIGdlbmVyYWxpemF0aW9uIGJvdW5kcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZWFzdXJpbmcgU2hhcnBuZXNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb21wdXRpbmcgdGhlIGZ1bGwgSGVzc2lhbiBvZiBhIG5ldXJhbCBuZXR3b3JrIGlzIE8obsKyKSBpbiBtZW1vcnkgYW5kIE8obsKzKSB0byBkaWFnb25hbGl6ZSDigJQgY29tcGxldGVseSBpbmZlYXNpYmxlIGZvciBsYXJnZSBtb2RlbHMuIFNldmVyYWwgZWZmaWNpZW50IHByb3hpZXMgZXhpc3Q6IHRoZSBsYXJnZXN0IEhlc3NpYW4gZWlnZW52YWx1ZSB2aWEgcG93ZXIgaXRlcmF0aW9uIChMYW5jem9zKSwgdGhlIEhlc3NpYW4gdHJhY2UgdmlhIEh1dGNoaW5zb25cdTAwMjdzIGVzdGltYXRvciwgYW5kIGV4cGVjdGVkIHNoYXJwbmVzcyAoYXZlcmFnZSBsb3NzIG92ZXIgR2F1c3NpYW4gd2VpZ2h0IHBlcnR1cmJhdGlvbnMpLiBFYWNoIGNhcHR1cmVzIGEgZGlmZmVyZW50IGFzcGVjdCBvZiB0aGUgY3VydmF0dXJlIGdlb21ldHJ5LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRyaWMiLCJGb3JtdWxhIiwiQ29tcHV0YXRpb25hbCBDb3N0IiwiSW50ZXJwcmV0YXRpb24iXSwicm93cyI6W1siTWF4IGVpZ2VudmFsdWUgzrtfbWF4IiwizrtfbWF4KOKIh8KyTCkiLCJPKG4pIHBlciBwb3dlciBpdGVyYXRpb24gc3RlcCIsIldvcnN0LWNhc2UgY3VydmF0dXJlIGRpcmVjdGlvbiJdLFsiSGVzc2lhbiB0cmFjZSIsIlRyKOKIh8KyTCkgPSDOo+G1os674bWiIiwiTyhrbikgdmlhIEh1dGNoaW5zb24gZXN0aW1hdG9yIiwiQXZlcmFnZSBjdXJ2YXR1cmUgYWNyb3NzIGFsbCBkaXJlY3Rpb25zIl0sWyJFeHBlY3RlZCBzaGFycG5lc3MiLCJFX860W0wozrgrzrQp4oiSTCjOuCldLCDOtH5OKDAsz4PCskkpIiwiTUMgc2FtcGxpbmcsIE8oa24pIHBlciBlc3RpbWF0ZSIsIkF2ZXJhZ2UgbG9zcyBpbmNyZWFzZSB1bmRlciByYW5kb20gcGVydHVyYmF0aW9uIl0sWyLPgS1zaGFycG5lc3MgKFNBTSkiLCJtYXhfe+KAls614oCW4omkz4F9IEwozrgrzrUp4oiSTCjOuCkiLCJPbmUgZ3JhZGllbnQgYXNjZW50IHN0ZXAgTyhuKSIsIldvcnN0LWNhc2UgcGVydHVyYmF0aW9uIGxvc3MgaW5jcmVhc2UgaW4gz4EtYmFsbCJdXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBsYXJnZXN0X2hlc3NpYW5fZWlnZW52YWx1ZShtb2RlbCwgbG9zc19mbiwgWCwgeSwgbl9pdGVycz00MCwgdG9sPTFlLTUpOlxuICAgIFwiXCJcIlBvd2VyIGl0ZXJhdGlvbiB0byBlc3RpbWF0ZSDOu19tYXgo4oiHwrJMKSDigJQgdGhlIHNoYXJwbmVzcyBtZXRyaWMuXCJcIlwiXG4gICAgcGFyYW1zID0gW3AgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZF1cblxuICAgICMgSW5pdGlhbGl6ZSByYW5kb20gdW5pdCB2ZWN0b3JcbiAgICB2ID0gW3RvcmNoLnJhbmRuX2xpa2UocCkgZm9yIHAgaW4gcGFyYW1zXVxuICAgIHZfbm9ybSA9IHRvcmNoLnNxcnQoc3VtKCh2aSoqMikuc3VtKCkgZm9yIHZpIGluIHYpKVxuICAgIHYgPSBbdmkgLyB2X25vcm0gZm9yIHZpIGluIHZdXG5cbiAgICBlaWdlbnZhbHVlID0gMC4wXG4gICAgZm9yIGl0IGluIHJhbmdlKG5faXRlcnMpOlxuICAgICAgICAjIEZvcndhcmQgcGFzc1xuICAgICAgICBsb3NzID0gbG9zc19mbihtb2RlbChYKSwgeSlcbiAgICAgICAgZ3JhZHMgPSB0b3JjaC5hdXRvZ3JhZC5ncmFkKGxvc3MsIHBhcmFtcywgY3JlYXRlX2dyYXBoPVRydWUpXG5cbiAgICAgICAgIyBIZXNzaWFuLXZlY3RvciBwcm9kdWN0OiBkL2TOuCAoZ3JhZHMgwrcgdilcbiAgICAgICAgZ3ZfZG90ID0gc3VtKChnICogdmkpLnN1bSgpIGZvciBnLCB2aSBpbiB6aXAoZ3JhZHMsIHYpKVxuICAgICAgICBIdiA9IHRvcmNoLmF1dG9ncmFkLmdyYWQoZ3ZfZG90LCBwYXJhbXMsIHJldGFpbl9ncmFwaD1GYWxzZSlcblxuICAgICAgICAjIFJheWxlaWdoIHF1b3RpZW50XG4gICAgICAgIG5ld19laWcgPSBzdW0oKGh2aSAqIHZpKS5zdW0oKSBmb3IgaHZpLCB2aSBpbiB6aXAoSHYsIHYpKS5pdGVtKClcblxuICAgICAgICAjIE5vcm1hbGl6ZSBmb3IgbmV4dCBpdGVyYXRpb25cbiAgICAgICAgSHZfbm9ybSA9IHRvcmNoLnNxcnQoc3VtKChodmkqKjIpLnN1bSgpIGZvciBodmkgaW4gSHYpKSArIDFlLTEyXG4gICAgICAgIHYgPSBbaHZpIC8gSHZfbm9ybSBmb3IgaHZpIGluIEh2XVxuXG4gICAgICAgIGlmIGFicyhuZXdfZWlnIC0gZWlnZW52YWx1ZSkgXHUwMDNjIHRvbDpcbiAgICAgICAgICAgIHByaW50KGZcIiAgQ29udmVyZ2VkIGF0IGl0ZXJhdGlvbiB7aXQrMX1cIilcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIGVpZ2VudmFsdWUgPSBuZXdfZWlnXG5cbiAgICByZXR1cm4gZWlnZW52YWx1ZVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubW9kZWwgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcig0LCAxNiksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDE2LCAxKSlcblgsIHkgPSB0b3JjaC5yYW5kbig2NCwgNCksIHRvcmNoLnJhbmRuKDY0LCAxKVxuc2hhcnBuZXNzID0gbGFyZ2VzdF9oZXNzaWFuX2VpZ2VudmFsdWUobW9kZWwsIG5uLk1TRUxvc3MoKSwgWCwgeSlcbnByaW50KGZcIs67X21heCAoc2hhcnBuZXNzKToge3NoYXJwbmVzczouNGZ9XCIpXG5wcmludChcIkhpZ2hlciDOu19tYXgg4oaSIHNoYXJwZXIgbWluaW11bSDihpIgZXhwZWN0ZWQgd29yc2UgZ2VuZXJhbGl6YXRpb24uXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlb3JldGljYWwgQ29ubmVjdGlvbnMgdG8gR2VuZXJhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBBQy1CYXllcyB0aGVvcnkgYm91bmRzIHRoZSBleHBlY3RlZCB0ZXN0IGxvc3MgaW4gdGVybXMgb2YgdGhlIEtMIGRpdmVyZ2VuY2UgYmV0d2VlbiBhIHBlcnR1cmJlZCBwb3N0ZXJpb3IgUSAod2VpZ2h0cyArIEdhdXNzaWFuIG5vaXNlKSBhbmQgYSBwcmlvciBQLiBNaW5pbWl6aW5nIHRoaXMgYm91bmQgZW5jb3VyYWdlcyBmaW5kaW5nIGZsYXQgcmVnaW9ucyB3aGVyZSBhZGRpbmcgbm9pc2UgZG9lc25cdTAwMjd0IGh1cnQgbG9zcy4gVGhlIGNvbm5lY3Rpb24gdG8gc2hhcnBuZXNzOiBLTChR4oCWUCkg4oidIM67X21heCB3aGVuIHRoZSBub2lzZSBjb3ZhcmlhbmNlIGlzIGlzb3Ryb3BpYy4gTGFyZ2UgYmF0Y2ggdHJhaW5pbmcgdGVuZHMgdG8gZmluZCBzaGFycCBtaW5pbWEgKEtlc2thciBldCBhbC4gMjAxNykgYmVjYXVzZSBsYXJnZSBiYXRjaGVzIHByb3ZpZGUgYWNjdXJhdGUgZ3JhZGllbnRzIHRoYXQgY29udmVyZ2UgdG8gdGhlIG5lYXJlc3QgbWluaW11bSByYXRoZXIgdGhhbiBleHBsb3Jpbmc7IHNtYWxsIGJhdGNoZXMgYWRkIG5vaXNlIHRoYXQgaGVscHMgZXNjYXBlIHNoYXJwIHJlZ2lvbnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMYXJnZSBiYXRjaCDihpIgbG93IGdyYWRpZW50IG5vaXNlIOKGkiBjb252ZXJnZXMgdG8gc2hhcnAgbWluaW1hIOKGkiBwb29yIGdlbmVyYWxpemF0aW9uIiwiU21hbGwgYmF0Y2gg4oaSIGhpZ2ggZ3JhZGllbnQgbm9pc2Ug4oaSIGJpYXNlcyB0b3dhcmQgZmxhdCBtaW5pbWEg4oaSIGJldHRlciBnZW5lcmFsaXphdGlvbiIsIkhpZ2ggbGVhcm5pbmcgcmF0ZSBhY3RzIHNpbWlsYXJseTogbm9pc3kgdXBkYXRlcyBwcmV2ZW50IHNldHRsaW5nIGluIHNoYXJwIG5hcnJvdyBiYXNpbnMiLCJTR0Qgbm9pc2Ugc2NhbGU6IOKInSDOt8K3z4PCsi9CIHdoZXJlIM63PWxlYXJuaW5nIHJhdGUsIM+DwrI9Z3JhZGllbnQgdmFyaWFuY2UsIEI9YmF0Y2ggc2l6ZSIsIkxpbmVhciBzY2FsaW5nIHJ1bGUgKEdveWFsIDIwMTcpOiBzY2FsZSBMUiBwcm9wb3J0aW9uYWwgdG8gYmF0Y2ggc2l6ZSB0byBtYWludGFpbiBub2lzZSBsZXZlbCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTQU06IFNoYXJwbmVzcy1Bd2FyZSBNaW5pbWl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNBTSAoRm9yZXQgZXQgYWwuIDIwMjEpIGV4cGxpY2l0bHkgbWluaW1pemVzIHRoZSB3b3JzdC1jYXNlIGxvc3MgaW4gYSDPgS1iYWxsIGFyb3VuZCBjdXJyZW50IHdlaWdodHMuIEluc3RlYWQgb2YgbWluaW1pemluZyBMKM64KSwgaXQgbWluaW1pemVzIG1heF974oCWzrXigJbiiaTPgX0gTCjOuCvOtSkuIEVhY2ggU0FNIHN0ZXAgaGFzIHR3byBncmFkaWVudCBjb21wdXRhdGlvbnM6ICgxKSBncmFkaWVudCBhc2NlbnQgdG8gZmluZCB0aGUgd29yc3QtY2FzZSBwZXJ0dXJiYXRpb24gzrXMgiA9IM+BwrfiiIdML+KAluKIh0zigJYsICgyKSBncmFkaWVudCBhdCB0aGUgcGVydHVyYmVkIHBvaW50IM64K861zIIgdXNlZCB0byB1cGRhdGUgzrguIFRoZSByZXN1bHQgaXMgYSBtb2RlbCB0aGF0IHNpdHMgaW4gYSBmbGF0IHJlZ2lvbiDigJQgYW55IHBlcnR1cmJhdGlvbiB3aXRoaW4gdGhlIM+BLWJhbGwgc3RpbGwgaGFzIGxvdyBsb3NzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjp0cnVlLCJpdGVtcyI6WyJDb21wdXRlIGdyYWRpZW50IOKIh0wozrgpIHdpdGggY3VycmVudCB3ZWlnaHRzIiwiQ29tcHV0ZSBwZXJ0dXJiYXRpb24gzrXMgiA9IM+BIMK3IOKIh0wozrgpIC8g4oCW4oiHTCjOuCnigJYgKG5vcm1hbGl6ZWQgZ3JhZGllbnQgc2NhbGVkIGJ5IM+BKSIsIkV2YWx1YXRlIGdyYWRpZW50IGF0IHBlcnR1cmJlZCB3ZWlnaHRzOiDiiIdMKM64ICsgzrXMgikiLCJVcGRhdGUgb3JpZ2luYWwgd2VpZ2h0czogzrgg4oaQIM64IOKIkiDOtyDCtyDiiIdMKM64ICsgzrXMgikiLCJDb3N0OiAyw5cgZm9yd2FyZC9iYWNrd2FyZCBwYXNzZXMgcGVyIHN0ZXAgdnMgU0dEXHUwMDI3cyAxw5ciXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5jbGFzcyBTQU0odG9yY2gub3B0aW0uT3B0aW1pemVyKTpcbiAgICBcIlwiXCJTaGFycG5lc3MtQXdhcmUgTWluaW1pemF0aW9uIChGb3JldCBldCBhbC4gMjAyMSkuXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgcGFyYW1zLCBiYXNlX29wdGltaXplcl9jbHMsIHJobz0wLjA1LCAqKmt3YXJncyk6XG4gICAgICAgIGRlZmF1bHRzID0gZGljdChyaG89cmhvLCAqKmt3YXJncylcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyhwYXJhbXMsIGRlZmF1bHRzKVxuICAgICAgICBzZWxmLmJhc2Vfb3B0aW1pemVyID0gYmFzZV9vcHRpbWl6ZXJfY2xzKHNlbGYucGFyYW1fZ3JvdXBzLCAqKmt3YXJncylcbiAgICAgICAgc2VsZi5wYXJhbV9ncm91cHMgPSBzZWxmLmJhc2Vfb3B0aW1pemVyLnBhcmFtX2dyb3Vwc1xuXG4gICAgQHRvcmNoLm5vX2dyYWQoKVxuICAgIGRlZiBmaXJzdF9zdGVwKHNlbGYsIHplcm9fZ3JhZD1GYWxzZSk6XG4gICAgICAgIFwiXCJcIkNsaW1iIHRvIHRoZSB3b3JzdC1jYXNlIHBlcnR1cmJhdGlvbiBwb2ludCDOuCArIM61zIIuXCJcIlwiXG4gICAgICAgIGdyYWRfbm9ybSA9IHNlbGYuX2dyYWRfbm9ybSgpXG4gICAgICAgIGZvciBncm91cCBpbiBzZWxmLnBhcmFtX2dyb3VwczpcbiAgICAgICAgICAgIHNjYWxlID0gZ3JvdXBbXCJyaG9cIl0gLyAoZ3JhZF9ub3JtICsgMWUtMTIpXG4gICAgICAgICAgICBmb3IgcCBpbiBncm91cFtcInBhcmFtc1wiXTpcbiAgICAgICAgICAgICAgICBpZiBwLmdyYWQgaXMgTm9uZTpcbiAgICAgICAgICAgICAgICAgICAgY29udGludWVcbiAgICAgICAgICAgICAgICBlX3cgPSBwLmdyYWQgKiBzY2FsZS50byhwKVxuICAgICAgICAgICAgICAgIHAuYWRkXyhlX3cpXG4gICAgICAgICAgICAgICAgc2VsZi5zdGF0ZVtwXVtcImVfd1wiXSA9IGVfd1xuICAgICAgICBpZiB6ZXJvX2dyYWQ6XG4gICAgICAgICAgICBzZWxmLnplcm9fZ3JhZCgpXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIHNlY29uZF9zdGVwKHNlbGYsIHplcm9fZ3JhZD1GYWxzZSk6XG4gICAgICAgIFwiXCJcIlJlc3RvcmUgzrgsIHRoZW4gYXBwbHkgYmFzZSBvcHRpbWl6ZXIgc3RlcCB1c2luZyBwZXJ0dXJiZWQgZ3JhZGllbnQuXCJcIlwiXG4gICAgICAgIGZvciBncm91cCBpbiBzZWxmLnBhcmFtX2dyb3VwczpcbiAgICAgICAgICAgIGZvciBwIGluIGdyb3VwW1wicGFyYW1zXCJdOlxuICAgICAgICAgICAgICAgIGlmIHAuZ3JhZCBpcyBOb25lOlxuICAgICAgICAgICAgICAgICAgICBjb250aW51ZVxuICAgICAgICAgICAgICAgIHAuc3ViXyhzZWxmLnN0YXRlW3BdW1wiZV93XCJdKVxuICAgICAgICBzZWxmLmJhc2Vfb3B0aW1pemVyLnN0ZXAoKVxuICAgICAgICBpZiB6ZXJvX2dyYWQ6XG4gICAgICAgICAgICBzZWxmLnplcm9fZ3JhZCgpXG5cbiAgICBkZWYgX2dyYWRfbm9ybShzZWxmKTpcbiAgICAgICAgZGV2aWNlID0gc2VsZi5wYXJhbV9ncm91cHNbMF1bXCJwYXJhbXNcIl1bMF0uZGV2aWNlXG4gICAgICAgIG5vcm1zID0gW3AuZ3JhZC5ub3JtKDIpLnRvKGRldmljZSlcbiAgICAgICAgICAgICAgICAgZm9yIGcgaW4gc2VsZi5wYXJhbV9ncm91cHMgZm9yIHAgaW4gZ1tcInBhcmFtc1wiXVxuICAgICAgICAgICAgICAgICBpZiBwLmdyYWQgaXMgbm90IE5vbmVdXG4gICAgICAgIHJldHVybiB0b3JjaC5zdGFjayhub3Jtcykubm9ybSgyKVxuXG4jIFF1aWNrIHVzYWdlIGRlbW9cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxubmV0ID0gdG9yY2gubm4uTGluZWFyKDQsIDEpXG5vcHQgPSBTQU0obmV0LnBhcmFtZXRlcnMoKSwgdG9yY2gub3B0aW0uU0dELCByaG89MC4wNSwgbHI9MC4wNSlcblgsIHkgPSB0b3JjaC5yYW5kbigzMiwgNCksIHRvcmNoLnJhbmRuKDMyLCAxKVxubG9zc19mbiA9IHRvcmNoLm5uLk1TRUxvc3MoKVxuZm9yIHN0ZXAgaW4gcmFuZ2UoNCk6XG4gICAgbG9zcyA9IGxvc3NfZm4obmV0KFgpLCB5KVxuICAgIGxvc3MuYmFja3dhcmQoKVxuICAgIG9wdC5maXJzdF9zdGVwKHplcm9fZ3JhZD1UcnVlKVxuICAgIGxvc3NfZm4obmV0KFgpLCB5KS5iYWNrd2FyZCgpXG4gICAgb3B0LnNlY29uZF9zdGVwKHplcm9fZ3JhZD1UcnVlKVxuICAgIHByaW50KGZcIlN0ZXAge3N0ZXArMX06IGxvc3M9e2xvc3MuaXRlbSgpOi40Zn1cIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiU0FNIEh5cGVycGFyYW1ldGVyIM+BIiwiY29udGVudCI6Is+BIGlzIHRoZSByYWRpdXMgb2YgdGhlIHBlcnR1cmJhdGlvbiBiYWxsLiBMYXJnZXIgz4Eg4oaSIHN0cm9uZ2VyIHNoYXJwbmVzcyByZWd1bGFyaXphdGlvbiBidXQgbW9yZSBhZ2dyZXNzaXZlIHBlcnR1cmJhdGlvbi4gRm9yIENJRkFSLTEwIC8gUmVzTmV0LCDPgT0wLjA1IHdvcmtzIHdlbGwuIEZvciB0cmFuc2Zvcm1lcnMsIM+BPTAuMDLigJMwLjEuIElmIM+BIGlzIHRvbyBsYXJnZSwgdGhlIHBlcnR1cmJhdGlvbiBvdmVyc2hvb3RzIGFuZCBTQU0gZGl2ZXJnZXMuIG1TQU0gdXNlcyBwZXItbWljcm8tYmF0Y2ggc2hhcnBuZXNzOyBBU0FNIHVzZXMgYWRhcHRpdmUgKHBlci1wYXJhbWV0ZXIpIG5vcm1hbGl6YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaW5nIFNBTSB2cyBTR0QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9uIGltYWdlIGNsYXNzaWZpY2F0aW9uIGJlbmNobWFya3MsIFNBTSBjb25zaXN0ZW50bHkgaW1wcm92ZXMgdGVzdCBhY2N1cmFjeSBieSAx4oCTMiUgb3ZlciBTR0Qgd2l0aCB0aGUgc2FtZSB0cmFpbmluZyBidWRnZXQuIFRoZSBpbXByb3ZlbWVudCBpcyBsYXJnZXN0IHdoZW4gdHJhaW5pbmcgZGF0YSBpcyBsaW1pdGVkIChoaWdoIGdlbmVyYWxpemF0aW9uIGdhcCkuIFNBTSBhbHNvIGltcHJvdmVzIHJvYnVzdG5lc3MgdG8gbGFiZWwgbm9pc2UgYW5kIGRpc3RyaWJ1dGlvbiBzaGlmdC4gVGhlIDLDlyBjb21wdXRlIGNvc3QgaXMgdGhlIG1haW4gZHJhd2JhY2s7IHNjaGVkdWxlZCBTQU0gKGFwcGx5IFNBTSBvbmx5IGluIGxhdGVyIGVwb2NocykgcmVjb3ZlcnMgbW9zdCBvZiB0aGUgYmVuZWZpdCBhdCBsb3dlciBjb3N0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiB0cmFpbl9tb2RlbChtb2RlbCwgb3B0aW1pemVyLCBYX3RyLCB5X3RyLCB1c2Vfc2FtPUZhbHNlLCBlcG9jaHM9NjApOlxuICAgIGxvc3NfZm4gPSBubi5NU0VMb3NzKClcbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgbW9kZWwudHJhaW4oKVxuICAgICAgICBmb3IgaSBpbiByYW5nZSgwLCBsZW4oWF90ciksIDE2KTpcbiAgICAgICAgICAgIHhiLCB5YiA9IFhfdHJbaTppKzE2XSwgeV90cltpOmkrMTZdXG4gICAgICAgICAgICBpZiB1c2Vfc2FtOlxuICAgICAgICAgICAgICAgIGxvc3MgPSBsb3NzX2ZuKG1vZGVsKHhiKSwgeWIpXG4gICAgICAgICAgICAgICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgICAgICAgICAgICAgb3B0aW1pemVyLmZpcnN0X3N0ZXAoemVyb19ncmFkPVRydWUpXG4gICAgICAgICAgICAgICAgbG9zc19mbihtb2RlbCh4YiksIHliKS5iYWNrd2FyZCgpXG4gICAgICAgICAgICAgICAgb3B0aW1pemVyLnNlY29uZF9zdGVwKHplcm9fZ3JhZD1UcnVlKVxuICAgICAgICAgICAgZWxzZTpcbiAgICAgICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgICAgICAgICBsb3NzID0gbG9zc19mbihtb2RlbCh4YiksIHliKVxuICAgICAgICAgICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICAgICAgICAgIG9wdGltaXplci5zdGVwKClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbm5wLnJhbmRvbS5zZWVkKDApXG5uX3RyLCBuX3RlID0gODAsIDQwXG5YX3RyID0gdG9yY2gucmFuZG4obl90ciwgMTApXG53X3RydWUgPSB0b3JjaC5yYW5kbigxMCwgMSlcbnlfdHIgPSBYX3RyIEAgd190cnVlICsgMC41ICogdG9yY2gucmFuZG4obl90ciwgMSlcblhfdGUgPSB0b3JjaC5yYW5kbihuX3RlLCAxMClcbnlfdGUgPSBYX3RlIEAgd190cnVlICsgMC41ICogdG9yY2gucmFuZG4obl90ZSwgMSlcblxucmVzdWx0cyA9IHt9XG5mb3IgbWV0aG9kLCB1c2Vfc2FtIGluIFsoXCJTR0RcIiwgRmFsc2UpLCAoXCJTQU1cIiwgVHJ1ZSldOlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKDEpXG4gICAgbW9kZWwgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcigxMCwgMzIpLCBubi5SZUxVKCksIG5uLkxpbmVhcigzMiwgMSkpXG4gICAgaWYgdXNlX3NhbTpcbiAgICAgICAgb3B0ID0gU0FNKG1vZGVsLnBhcmFtZXRlcnMoKSwgdG9yY2gub3B0aW0uU0dELCByaG89MC4wNSwgbHI9MC4wNSlcbiAgICBlbHNlOlxuICAgICAgICBvcHQgPSB0b3JjaC5vcHRpbS5TR0QobW9kZWwucGFyYW1ldGVycygpLCBscj0wLjA1KVxuICAgIHRyYWluX21vZGVsKG1vZGVsLCBvcHQsIFhfdHIsIHlfdHIsIHVzZV9zYW09dXNlX3NhbSlcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgdGVzdF9tc2UgPSBubi5NU0VMb3NzKCkobW9kZWwoWF90ZSksIHlfdGUpLml0ZW0oKVxuICAgIHJlc3VsdHNbbWV0aG9kXSA9IHRlc3RfbXNlXG4gICAgcHJpbnQoZlwie21ldGhvZH06IHRlc3QgTVNFID0ge3Rlc3RfbXNlOi40Zn1cIilcbnByaW50KGZcIlNBTSBpbXByb3ZlbWVudDogezEwMCoocmVzdWx0c1tcdTAwMjdTR0RcdTAwMjddLXJlc3VsdHNbXHUwMDI3U0FNXHUwMDI3XSkvcmVzdWx0c1tcdTAwMjdTR0RcdTAwMjddOi4xZn0lXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVmlzdWFsaXppbmcgdGhlIExvc3MgTGFuZHNjYXBlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXZSBjYW4gY29tcGFyZSB0aGUgbG9jYWwgbG9zcyBnZW9tZXRyeSBhcm91bmQgdHdvIG1pbmltYSBieSBzYW1wbGluZyBsb3NzIHZhbHVlcyB3aXRoaW4gYSBzbWFsbCBiYWxsLiBBIHNoYXJwIG1pbmltdW0gc2hvd3MgcmFwaWRseSBpbmNyZWFzaW5nIGxvc3MgZXZlbiBmb3Igc21hbGwgcGVydHVyYmF0aW9uczsgYSBmbGF0IG1pbmltdW0gbWFpbnRhaW5zIGxvdyBsb3NzIGFjcm9zcyB0aGUgZW50aXJlIGJhbGwuIFRoaXMgZGlyZWN0bHkgZXhwbGFpbnMgZ2VuZXJhbGl6YXRpb246IHRoZSB0cmFpbi10ZXN0IGRpc3RyaWJ1dGlvbiBzaGlmdCBhY3RzIGxpa2UgYSB3ZWlnaHQgcGVydHVyYmF0aW9uLCBzbyBzaGFycCBtaW5pbWEgc3VmZmVyIGEgbGFyZ2VyIHRlc3QgbG9zcyBpbmNyZWFzZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBzYW1wbGVfcGVydHVyYmF0aW9uX2xvc3NlcyhjZW50ZXJfd2VpZ2h0cywgbG9zc19mbiwgbl9zYW1wbGVzPTMwMCwgcmFkaWk9KDAuMSwgMC4zLCAwLjUpKTpcbiAgICBcIlwiXCJTYW1wbGUgbG9zcyBhdCByYW5kb20gcGVydHVyYmF0aW9ucyBvZiBkaWZmZXJlbnQgcmFkaWkgZnJvbSB0aGUgbWluaW11bS5cIlwiXCJcbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgciBpbiByYWRpaTpcbiAgICAgICAgcGVydHVyYmVkX2xvc3NlcyA9IFtdXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fc2FtcGxlcyk6XG4gICAgICAgICAgICBwZXJ0dXJiZWQgPSBbdyArIG5wLnJhbmRvbS5yYW5kbigqdy5zaGFwZSkgKiByIGZvciB3IGluIGNlbnRlcl93ZWlnaHRzXVxuICAgICAgICAgICAgcGVydHVyYmVkX2xvc3Nlcy5hcHBlbmQobG9zc19mbihwZXJ0dXJiZWQpKVxuICAgICAgICByZXN1bHRzW3JdID0gbnAuYXJyYXkocGVydHVyYmVkX2xvc3NlcylcbiAgICByZXR1cm4gcmVzdWx0c1xuXG5kZWYgc2hhcnBfbG9zcyh3cyk6ICAjIEhpZ2ggY3VydmF0dXJlOiAxMDAgKiB8fHd8fF4yXG4gICAgcmV0dXJuIHN1bSgxMDAuMCAqIG5wLnN1bSh3KioyKSBmb3IgdyBpbiB3cylcblxuZGVmIGZsYXRfbG9zcyh3cyk6ICAgIyBMb3cgY3VydmF0dXJlOiAxLjAgKiB8fHd8fF4yXG4gICAgcmV0dXJuIHN1bSgxLjAgKiBucC5zdW0odyoqMikgZm9yIHcgaW4gd3MpXG5cbm5wLnJhbmRvbS5zZWVkKDMpXG5jZW50ZXIgPSBbbnAuemVyb3MoKDYsKSksIG5wLnplcm9zKCg0LCkpXSAgIyBhdCB0aGUgZ2xvYmFsIG1pbmltdW1cblxuc2hhcnBfc3RhdHMgPSBzYW1wbGVfcGVydHVyYmF0aW9uX2xvc3NlcyhjZW50ZXIsIHNoYXJwX2xvc3MpXG5mbGF0X3N0YXRzICA9IHNhbXBsZV9wZXJ0dXJiYXRpb25fbG9zc2VzKGNlbnRlciwgZmxhdF9sb3NzKVxuXG5wcmludChmXCJ7XHUwMDI3UmFkaXVzXHUwMDI3Olx1MDAzYzh9IHtcdTAwMjdTaGFycCBNZWFuXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3U2hhcnAgU3RkXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3RmxhdCBNZWFuXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3RmxhdCBTdGRcdTAwMjc6XHUwMDNlMTB9XCIpXG5mb3IgciBpbiAoMC4xLCAwLjMsIDAuNSk6XG4gICAgc20sIHNzID0gc2hhcnBfc3RhdHNbcl0ubWVhbigpLCBzaGFycF9zdGF0c1tyXS5zdGQoKVxuICAgIGZtLCBmcyA9IGZsYXRfc3RhdHNbcl0ubWVhbigpLCAgZmxhdF9zdGF0c1tyXS5zdGQoKVxuICAgIHByaW50KGZcIntyOlx1MDAzYzguMWZ9IHtzbTpcdTAwM2UxMi40Zn0ge3NzOlx1MDAzZTEyLjRmfSB7Zm06XHUwMDNlMTIuNGZ9IHtmczpcdTAwM2UxMC40Zn1cIilcbnByaW50KFwiXFxuU2hhcnAgbWluaW11bTogbG9zcyBncm93cyByYXBpZGx5IHdpdGggcGVydHVyYmF0aW9uIHJhZGl1cy5cIilcbnByaW50KFwiRmxhdCBtaW5pbXVtOiBsb3NzIHN0YXlzIG5lYXIgemVybyBldmVuIGZvciBsYXJnZSBwZXJ0dXJiYXRpb25zLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4dGVuc2lvbnMgYW5kIFZhcmlhbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZXZlcmFsIFNBTSB2YXJpYW50cyBpbXByb3ZlIGVmZmljaWVuY3kgb3IgZWZmZWN0aXZlbmVzcy4gbS1TQU0gY29tcHV0ZXMgc2hhcnBuZXNzIG9uIGluZGl2aWR1YWwgbWljcm8tYmF0Y2hlcyByYXRoZXIgdGhhbiB0aGUgZnVsbCBiYXRjaCwgZmluZGluZyBzaGFycGVyIHBlci1zYW1wbGUgc2hhcnBuZXNzIGVzdGltYXRlcy4gQVNBTSAoQWRhcHRpdmUgU0FNKSBub3JtYWxpemVzIHRoZSBwZXJ0dXJiYXRpb24gcGVyIHBhcmFtZXRlciBieSBpdHMgbWFnbml0dWRlLCByZW1vdmluZyB0aGUgc2NhbGUgc2Vuc2l0aXZpdHkgb2YgZml4ZWQtz4EgU0FNLiBTY2hlZHVsZWQgz4EgYW5uZWFscyDPgSBkdXJpbmcgdHJhaW5pbmcg4oCUIGxhcmdlIM+BIGVhcmx5IGZvciBleHBsb3JhdGlvbiwgc21hbGwgz4EgbGF0ZXIgZm9yIHJlZmluZW1lbnQuIExvb2thaGVhZCArIFNBTSBjb21iaW5lcyBzbG93L2Zhc3Qgd2VpZ2h0IGF2ZXJhZ2luZyB3aXRoIHNoYXJwbmVzcyBhd2FyZW5lc3MuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJtU0FNIChtaWNyby1iYXRjaCBTQU0pOiBzaGFycG5lc3MgY29tcHV0ZWQgcGVyIG1pY3JvLWJhdGNoIOKAlCBmaW5kcyBzaGFycGVyLCBtb3JlIGhhcm1mdWwgbWluaW1hIiwiQVNBTTogYWRhcHRpdmUgcGVyLXBhcmFtZXRlciBub3JtYWxpemF0aW9uIM61zILhtaIgPSDPgXzOuOG1onzCt2fhtaIv4oCWfM64fMK3Z+KAliDigJQgc2NhbGUgaW52YXJpYW50IiwiR1NBTTogZ3JhZGllbnQgZGVjb21wb3NpdGlvbiBpbnRvIHNoYXJwbmVzcyBhbmQgdGFzayBkaXJlY3Rpb25zIGZvciBtb3JlIHN0YWJsZSB0cmFpbmluZyIsIlNXQSAoU3RvY2hhc3RpYyBXZWlnaHQgQXZlcmFnaW5nKTogYXZlcmFnZSB3ZWlnaHRzIGFsb25nIFNHRCB0cmFqZWN0b3J5IOKGkiBmbGF0IHJlZ2lvbiBpbXBsaWNpdGx5IiwiU0FNICsgbGFyZ2UgYmF0Y2g6IHBhcnRpYWxseSByZWNvdmVycyB0aGUgZmxhdG5lc3MgYmlhcyB0aGF0IHNtYWxsIGJhdGNoZXMgcHJvdmlkZSBuYXR1cmFsbHkiXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Sharp vs Flat Minima and Generalization

Two models can achieve identical training loss yet differ dramatically in test performance. One key geometric factor: the curvature of the loss surface at the minimum. A sharp minimum is surrounded by high-curvature walls — a tiny perturbation to weights causes a large loss increase, and when the train/test distributions differ slightly (as they always do), the model generalizes poorly. A flat minimum is robust to perturbations and tends to generalize better.

## Understanding Sharp and Flat Minima

Sharpness is formally quantified by the Hessian ∇²L(θ) at the minimum θ*. The largest eigenvalue λ_max(∇²L) gives the worst-case curvature: a perturbation ε in the direction of the top eigenvector increases loss by approximately (λ_max/2)‖ε‖². For a flat minimum λ_max is small; for a sharp minimum it can be millions. PAC-Bayes bounds connect sharpness to the generalization gap: generalization_gap ≈ O(√(λ_max/n)) where n is training set size.

> **Hochreiter & Schmidhuber 1997**: The original flat minima paper argued from an MDL perspective: a flat minimum can be described with fewer bits than a sharp one (you can quantize the weights more aggressively without changing the loss). Lower description length implies better generalization by Occam's razor / MDL principle. Modern PAC-Bayes theory formalizes this into quantitative generalization bounds.

## Measuring Sharpness

Computing the full Hessian of a neural network is O(n²) in memory and O(n³) to diagonalize — completely infeasible for large models. Several efficient proxies exist: the largest Hessian eigenvalue via power iteration (Lanczos), the Hessian trace via Hutchinson's estimator, and expected sharpness (average loss over Gaussian weight perturbations). Each captures a different aspect of the curvature geometry.

| Metric | Formula | Computational Cost | Interpretation |
| --- | --- | --- | --- |
| Max eigenvalue λ_max | λ_max(∇²L) | O(n) per power iteration step | Worst-case curvature direction |
| Hessian trace | Tr(∇²L) = Σᵢλᵢ | O(kn) via Hutchinson estimator | Average curvature across all directions |
| Expected sharpness | E_δ[L(θ+δ)−L(θ)], δ~N(0,σ²I) | MC sampling, O(kn) per estimate | Average loss increase under random perturbation |
| ρ-sharpness (SAM) | max_{‖ε‖≤ρ} L(θ+ε)−L(θ) | One gradient ascent step O(n) | Worst-case perturbation loss increase in ρ-ball |

```python
import torch
import torch.nn as nn

def largest_hessian_eigenvalue(model, loss_fn, X, y, n_iters=40, tol=1e-5):
    """Power iteration to estimate λ_max(∇²L) — the sharpness metric."""
    params = [p for p in model.parameters() if p.requires_grad]

    # Initialize random unit vector
    v = [torch.randn_like(p) for p in params]
    v_norm = torch.sqrt(sum((vi**2).sum() for vi in v))
    v = [vi / v_norm for vi in v]

    eigenvalue = 0.0
    for it in range(n_iters):
        # Forward pass
        loss = loss_fn(model(X), y)
        grads = torch.autograd.grad(loss, params, create_graph=True)

        # Hessian-vector product: d/dθ (grads · v)
        gv_dot = sum((g * vi).sum() for g, vi in zip(grads, v))
        Hv = torch.autograd.grad(gv_dot, params, retain_graph=False)

        # Rayleigh quotient
        new_eig = sum((hvi * vi).sum() for hvi, vi in zip(Hv, v)).item()

        # Normalize for next iteration
        Hv_norm = torch.sqrt(sum((hvi**2).sum() for hvi in Hv)) + 1e-12
        v = [hvi / Hv_norm for hvi in Hv]

        if abs(new_eig - eigenvalue) < tol:
            print(f"  Converged at iteration {it+1}")
            break
        eigenvalue = new_eig

    return eigenvalue

torch.manual_seed(0)
model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
X, y = torch.randn(64, 4), torch.randn(64, 1)
sharpness = largest_hessian_eigenvalue(model, nn.MSELoss(), X, y)
print(f"λ_max (sharpness): {sharpness:.4f}")
print("Higher λ_max → sharper minimum → expected worse generalization.")
```

## Theoretical Connections to Generalization

PAC-Bayes theory bounds the expected test loss in terms of the KL divergence between a perturbed posterior Q (weights + Gaussian noise) and a prior P. Minimizing this bound encourages finding flat regions where adding noise doesn't hurt loss. The connection to sharpness: KL(Q‖P) ∝ λ_max when the noise covariance is isotropic. Large batch training tends to find sharp minima (Keskar et al. 2017) because large batches provide accurate gradients that converge to the nearest minimum rather than exploring; small batches add noise that helps escape sharp regions.

- Large batch → low gradient noise → converges to sharp minima → poor generalization
- Small batch → high gradient noise → biases toward flat minima → better generalization
- High learning rate acts similarly: noisy updates prevent settling in sharp narrow basins
- SGD noise scale: ∝ η·σ²/B where η=learning rate, σ²=gradient variance, B=batch size
- Linear scaling rule (Goyal 2017): scale LR proportional to batch size to maintain noise level

## SAM: Sharpness-Aware Minimization

SAM (Foret et al. 2021) explicitly minimizes the worst-case loss in a ρ-ball around current weights. Instead of minimizing L(θ), it minimizes max_{‖ε‖≤ρ} L(θ+ε). Each SAM step has two gradient computations: (1) gradient ascent to find the worst-case perturbation ε̂ = ρ·∇L/‖∇L‖, (2) gradient at the perturbed point θ+ε̂ used to update θ. The result is a model that sits in a flat region — any perturbation within the ρ-ball still has low loss.

1. Compute gradient ∇L(θ) with current weights
2. Compute perturbation ε̂ = ρ · ∇L(θ) / ‖∇L(θ)‖ (normalized gradient scaled by ρ)
3. Evaluate gradient at perturbed weights: ∇L(θ + ε̂)
4. Update original weights: θ ← θ − η · ∇L(θ + ε̂)
5. Cost: 2× forward/backward passes per step vs SGD's 1×

```python
import torch

class SAM(torch.optim.Optimizer):
    """Sharpness-Aware Minimization (Foret et al. 2021)."""

    def __init__(self, params, base_optimizer_cls, rho=0.05, **kwargs):
        defaults = dict(rho=rho, **kwargs)
        super().__init__(params, defaults)
        self.base_optimizer = base_optimizer_cls(self.param_groups, **kwargs)
        self.param_groups = self.base_optimizer.param_groups

    @torch.no_grad()
    def first_step(self, zero_grad=False):
        """Climb to the worst-case perturbation point θ + ε̂."""
        grad_norm = self._grad_norm()
        for group in self.param_groups:
            scale = group["rho"] / (grad_norm + 1e-12)
            for p in group["params"]:
                if p.grad is None:
                    continue
                e_w = p.grad * scale.to(p)
                p.add_(e_w)
                self.state[p]["e_w"] = e_w
        if zero_grad:
            self.zero_grad()

    @torch.no_grad()
    def second_step(self, zero_grad=False):
        """Restore θ, then apply base optimizer step using perturbed gradient."""
        for group in self.param_groups:
            for p in group["params"]:
                if p.grad is None:
                    continue
                p.sub_(self.state[p]["e_w"])
        self.base_optimizer.step()
        if zero_grad:
            self.zero_grad()

    def _grad_norm(self):
        device = self.param_groups[0]["params"][0].device
        norms = [p.grad.norm(2).to(device)
                 for g in self.param_groups for p in g["params"]
                 if p.grad is not None]
        return torch.stack(norms).norm(2)

# Quick usage demo
torch.manual_seed(42)
net = torch.nn.Linear(4, 1)
opt = SAM(net.parameters(), torch.optim.SGD, rho=0.05, lr=0.05)
X, y = torch.randn(32, 4), torch.randn(32, 1)
loss_fn = torch.nn.MSELoss()
for step in range(4):
    loss = loss_fn(net(X), y)
    loss.backward()
    opt.first_step(zero_grad=True)
    loss_fn(net(X), y).backward()
    opt.second_step(zero_grad=True)
    print(f"Step {step+1}: loss={loss.item():.4f}")
```

> **SAM Hyperparameter ρ**: ρ is the radius of the perturbation ball. Larger ρ → stronger sharpness regularization but more aggressive perturbation. For CIFAR-10 / ResNet, ρ=0.05 works well. For transformers, ρ=0.02–0.1. If ρ is too large, the perturbation overshoots and SAM diverges. mSAM uses per-micro-batch sharpness; ASAM uses adaptive (per-parameter) normalization.

## Comparing SAM vs SGD

On image classification benchmarks, SAM consistently improves test accuracy by 1–2% over SGD with the same training budget. The improvement is largest when training data is limited (high generalization gap). SAM also improves robustness to label noise and distribution shift. The 2× compute cost is the main drawback; scheduled SAM (apply SAM only in later epochs) recovers most of the benefit at lower cost.

```python
import torch
import torch.nn as nn
import numpy as np

def train_model(model, optimizer, X_tr, y_tr, use_sam=False, epochs=60):
    loss_fn = nn.MSELoss()
    for epoch in range(epochs):
        model.train()
        for i in range(0, len(X_tr), 16):
            xb, yb = X_tr[i:i+16], y_tr[i:i+16]
            if use_sam:
                loss = loss_fn(model(xb), yb)
                loss.backward()
                optimizer.first_step(zero_grad=True)
                loss_fn(model(xb), yb).backward()
                optimizer.second_step(zero_grad=True)
            else:
                optimizer.zero_grad()
                loss = loss_fn(model(xb), yb)
                loss.backward()
                optimizer.step()

torch.manual_seed(0)
np.random.seed(0)
n_tr, n_te = 80, 40
X_tr = torch.randn(n_tr, 10)
w_true = torch.randn(10, 1)
y_tr = X_tr @ w_true + 0.5 * torch.randn(n_tr, 1)
X_te = torch.randn(n_te, 10)
y_te = X_te @ w_true + 0.5 * torch.randn(n_te, 1)

results = {}
for method, use_sam in [("SGD", False), ("SAM", True)]:
    torch.manual_seed(1)
    model = nn.Sequential(nn.Linear(10, 32), nn.ReLU(), nn.Linear(32, 1))
    if use_sam:
        opt = SAM(model.parameters(), torch.optim.SGD, rho=0.05, lr=0.05)
    else:
        opt = torch.optim.SGD(model.parameters(), lr=0.05)
    train_model(model, opt, X_tr, y_tr, use_sam=use_sam)
    with torch.no_grad():
        test_mse = nn.MSELoss()(model(X_te), y_te).item()
    results[method] = test_mse
    print(f"{method}: test MSE = {test_mse:.4f}")
print(f"SAM improvement: {100*(results['SGD']-results['SAM'])/results['SGD']:.1f}%")
```

## Visualizing the Loss Landscape

We can compare the local loss geometry around two minima by sampling loss values within a small ball. A sharp minimum shows rapidly increasing loss even for small perturbations; a flat minimum maintains low loss across the entire ball. This directly explains generalization: the train-test distribution shift acts like a weight perturbation, so sharp minima suffer a larger test loss increase.

```python
import numpy as np

def sample_perturbation_losses(center_weights, loss_fn, n_samples=300, radii=(0.1, 0.3, 0.5)):
    """Sample loss at random perturbations of different radii from the minimum."""
    results = {}
    for r in radii:
        perturbed_losses = []
        for _ in range(n_samples):
            perturbed = [w + np.random.randn(*w.shape) * r for w in center_weights]
            perturbed_losses.append(loss_fn(perturbed))
        results[r] = np.array(perturbed_losses)
    return results

def sharp_loss(ws):  # High curvature: 100 * ||w||^2
    return sum(100.0 * np.sum(w**2) for w in ws)

def flat_loss(ws):   # Low curvature: 1.0 * ||w||^2
    return sum(1.0 * np.sum(w**2) for w in ws)

np.random.seed(3)
center = [np.zeros((6,)), np.zeros((4,))]  # at the global minimum

sharp_stats = sample_perturbation_losses(center, sharp_loss)
flat_stats  = sample_perturbation_losses(center, flat_loss)

print(f"{'Radius':<8} {'Sharp Mean':>12} {'Sharp Std':>12} {'Flat Mean':>12} {'Flat Std':>10}")
for r in (0.1, 0.3, 0.5):
    sm, ss = sharp_stats[r].mean(), sharp_stats[r].std()
    fm, fs = flat_stats[r].mean(),  flat_stats[r].std()
    print(f"{r:<8.1f} {sm:>12.4f} {ss:>12.4f} {fm:>12.4f} {fs:>10.4f}")
print("\nSharp minimum: loss grows rapidly with perturbation radius.")
print("Flat minimum: loss stays near zero even for large perturbations.")
```

## Extensions and Variants

Several SAM variants improve efficiency or effectiveness. m-SAM computes sharpness on individual micro-batches rather than the full batch, finding sharper per-sample sharpness estimates. ASAM (Adaptive SAM) normalizes the perturbation per parameter by its magnitude, removing the scale sensitivity of fixed-ρ SAM. Scheduled ρ anneals ρ during training — large ρ early for exploration, small ρ later for refinement. Lookahead + SAM combines slow/fast weight averaging with sharpness awareness.

- mSAM (micro-batch SAM): sharpness computed per micro-batch — finds sharper, more harmful minima
- ASAM: adaptive per-parameter normalization ε̂ᵢ = ρ|θᵢ|·gᵢ/‖|θ|·g‖ — scale invariant
- GSAM: gradient decomposition into sharpness and task directions for more stable training
- SWA (Stochastic Weight Averaging): average weights along SGD trajectory → flat region implicitly
- SAM + large batch: partially recovers the flatness bias that small batches provide naturally

---

