---
title: "Spectral Clustering — Graph Laplacian and Normalized Cut"
slug: "spectral-clustering"
description: "Understand spectral clustering from first principles: similarity graph construction, unnormalized and normalized graph Laplacians, spectral embedding via the k smallest eigenvectors, the normalized cut objective, connection to Markov chains, and comparison with k-means on non-convex benchmarks."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BlY3RyYWwgY2x1c3RlcmluZyBzb2x2ZXMgdGhlIHByb2JsZW0gay1tZWFucyBjYW5ub3Q6IGNsdXN0ZXJpbmcgZGF0YSB3aXRoIG5vbi1jb252ZXgsIG5vbi1zcGhlcmljYWwgc3RydWN0dXJlLiBUaGUgY29yZSBpbnNpZ2h0IGlzIHRvIHJlcHJlc2VudCB0aGUgZGF0YSBhcyBhIHNpbWlsYXJpdHkgZ3JhcGgsIHRoZW4gY2x1c3RlciBpbiB0aGUgZ3JhcGhcdTAwMjdzIHNwZWN0cmFsIChMYXBsYWNpYW4gZWlnZW52ZWN0b3IpIHNwYWNlIHJhdGhlciB0aGFuIHRoZSBvcmlnaW5hbCBmZWF0dXJlIHNwYWNlLiBJbiB0aGUgc3BlY3RyYWwgZW1iZWRkaW5nLCBub24tY29udmV4IHNoYXBlcyBpbiBpbnB1dCBzcGFjZSBiZWNvbWUgbGluZWFybHkgc2VwYXJhYmxlIOKAlCBhIHNpbXBsZSBrLW1lYW5zIGluIHRoZSBlbWJlZGRpbmcgdGhlbiByZWNvdmVycyB0aGUgdHJ1ZSBjbHVzdGVycy4gVGhlIG1ldGhvZCBpcyBncm91bmRlZCBpbiBncmFwaCBwYXJ0aXRpb25pbmcgdGhlb3J5IGFuZCBjb25uZWN0cyB0byByYW5kb20gd2Fsa3Mgb24gZ3JhcGhzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNpbWlsYXJpdHkgR3JhcGggQ29uc3RydWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHaXZlbiBuIHBvaW50cywgY29uc3RydWN0IGEgd2VpZ2h0ZWQgZ3JhcGggd2hlcmUgbm9kZXMgYXJlIHBvaW50cyBhbmQgZWRnZSB3ZWlnaHRzIGVuY29kZSBzaW1pbGFyaXR5LiBUd28gY29tbW9uIGNob2ljZXM6ICgxKSDOtS1uZWlnaGJvcmhvb2QgZ3JhcGg6IGNvbm5lY3QgcG9pbnRzIHdpdGggZGlzdCh44bWiLHjisbwpIOKJpCDOtSwgd2l0aCBiaW5hcnkgb3IgUkJGLXdlaWdodGVkIGVkZ2VzOyAoMikgay1OTiBncmFwaDogY29ubmVjdCBlYWNoIHBvaW50IHRvIGl0cyBrIG5lYXJlc3QgbmVpZ2hib3JzLCB3aXRoIHdlaWdodHMgdyh44bWiLHjisbwpID0gZXhwKOKIkuKAlnjhtaLiiJJ44rG84oCWwrIvKDLPg8KyKSkuIFRoZSBSQkYgKEdhdXNzaWFuKSBrZXJuZWwgz4MgY29udHJvbHMgdGhlIG5laWdoYm9yaG9vZCBzY2FsZSDigJQgc21hbGxlciDPgyBtZWFucyBvbmx5IHZlcnkgbmVhcmJ5IHBvaW50cyBhcmUgY29ubmVjdGVkLiBUaGUgcmVzdWx0aW5nIHdlaWdodCBtYXRyaXggVyDiiIgg4oSd4oG/y6Pigb8gaXMgc3ltbWV0cmljIHdpdGggd+G1ouKxvCDiiaUgMC4gVGhlIGRlZ3JlZSBtYXRyaXggRCBpcyBkaWFnb25hbCB3aXRoIEThtaLhtaIgPSDOo+KxvCB34bWi4rG8LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYXBoIExhcGxhY2lhbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHVubm9ybWFsaXplZCBncmFwaCBMYXBsYWNpYW4gaXMgTCA9IEQg4oiSIFcuIEwgaXMgc3ltbWV0cmljIHBvc2l0aXZlIHNlbWktZGVmaW5pdGU6IGZvciBhbnkgdmVjdG9yIGYsIGbhtYBMZiA9ICgxLzIpIM6j4bWi4rG8IHfhtaLisbwoZuG1ouKIkmbisbwpwrIg4omlIDAuIFRoZSBzbWFsbGVzdCBlaWdlbnZhbHVlIGlzIGFsd2F5cyAwIChlaWdlbnZlY3RvciA9IGNvbnN0YW50IDEpLiBUaGUgbXVsdGlwbGljaXR5IG9mIGVpZ2VudmFsdWUgMCBlcXVhbHMgdGhlIG51bWJlciBvZiBjb25uZWN0ZWQgY29tcG9uZW50cyDigJQgYSBrZXkgdGhlb3JlbSBsaW5raW5nIHNwZWN0cmFsIHByb3BlcnRpZXMgdG8gZ3JhcGggc3RydWN0dXJlLiBGb3IgYSBjb25uZWN0ZWQgZ3JhcGgsIHRoZSBzZWNvbmQtc21hbGxlc3QgZWlnZW52YWx1ZSDOu+KCgiAoRmllZGxlciB2YWx1ZSkgbWVhc3VyZXMgdGhlIGdyYXBoXHUwMDI3cyBhbGdlYnJhaWMgY29ubmVjdGl2aXR5OyBpdHMgZWlnZW52ZWN0b3IgKEZpZWRsZXIgdmVjdG9yKSByZXZlYWxzIHRoZSBtb3N0IG5hdHVyYWwgYmlwYXJ0aXRpb24uIFRoZSBub3JtYWxpemVkIExhcGxhY2lhbiBMX3N5bSA9IERee+KIkjEvMn1MRF574oiSMS8yfSA9IEkg4oiSIERee+KIkjEvMn1XRF574oiSMS8yfSBpcyBwcmVmZXJyZWQgZm9yIHNwZWN0cmFsIGNsdXN0ZXJpbmcgYXMgaXQgYWNjb3VudHMgZm9yIGRlZ3JlZSBoZXRlcm9nZW5laXR5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBLTWVhbnNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9tb29uc1xuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWRqdXN0ZWRfcmFuZF9zY29yZVxuXG5kZWYgc3BlY3RyYWxfY2x1c3RlcmluZ19zY3JhdGNoKFgsIGssIHNpZ21hPTAuNSwgbl9uZWlnaGJvcnM9MTApOlxuICAgIFwiXCJcIlNwZWN0cmFsIGNsdXN0ZXJpbmc6IGFmZmluaXR5IC1cdTAwM2UgTGFwbGFjaWFuIC1cdTAwM2UgZWlnZW52ZWN0b3JzIC1cdTAwM2Ugay1tZWFucy5cIlwiXCJcbiAgICBuID0gWC5zaGFwZVswXVxuICAgICMgQnVpbGQgUkJGIGFmZmluaXR5IG1hdHJpeCAoZnVsbCwgbm90IGtOTiBmb3Igc2ltcGxpY2l0eSlcbiAgICBkaXN0c19zcSA9ICgoWFs6LCBOb25lLCA6XSAtIFhbTm9uZSwgOiwgOl0pICoqIDIpLnN1bShheGlzPTIpXG4gICAgVyA9IG5wLmV4cCgtZGlzdHNfc3EgLyAoMiAqIHNpZ21hICoqIDIpKVxuICAgIG5wLmZpbGxfZGlhZ29uYWwoVywgMCkgICMgbm8gc2VsZi1sb29wc1xuICAgICMgRGVncmVlIG1hdHJpeCBhbmQgbm9ybWFsaXplZCBMYXBsYWNpYW5cbiAgICBkID0gVy5zdW0oYXhpcz0xKVxuICAgIERfaW52X3NxcnQgPSBucC5kaWFnKDEuMCAvIG5wLnNxcnQoZCArIDFlLTEwKSlcbiAgICBMX3N5bSA9IG5wLmV5ZShuKSAtIERfaW52X3NxcnQgQCBXIEAgRF9pbnZfc3FydFxuICAgICMgRWlnZW5kZWNvbXBvc2l0aW9uIOKAlCBrIHNtYWxsZXN0IGVpZ2VudmVjdG9yc1xuICAgIGVpZ3ZhbHMsIGVpZ3ZlY3MgPSBucC5saW5hbGcuZWlnaChMX3N5bSlcbiAgICBVID0gZWlndmVjc1s6LCA6a10gICMgcm93cyA9IGVtYmVkZGluZ3MgZm9yIGVhY2ggcG9pbnRcbiAgICAjIE5vcm1hbGl6ZSByb3dzIHRvIHVuaXQgbm9ybSAoc3RhbmRhcmQgcHJhY3RpY2UpXG4gICAgbm9ybXMgPSBucC5saW5hbGcubm9ybShVLCBheGlzPTEsIGtlZXBkaW1zPVRydWUpXG4gICAgVV9ub3JtID0gVSAvIChub3JtcyArIDFlLTEwKVxuICAgICMgSy1NZWFucyBpbiBzcGVjdHJhbCBzcGFjZVxuICAgIGttID0gS01lYW5zKG5fY2x1c3RlcnM9aywgbl9pbml0PTEwLCByYW5kb21fc3RhdGU9NDIpXG4gICAgbGFiZWxzID0ga20uZml0X3ByZWRpY3QoVV9ub3JtKVxuICAgIHJldHVybiBsYWJlbHMsIGVpZ3ZhbHNbOmsrMl1cblxuWCwgeV90cnVlID0gbWFrZV9tb29ucyhuX3NhbXBsZXM9MzAwLCBub2lzZT0wLjA3LCByYW5kb21fc3RhdGU9NDIpXG5YID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG5sYWJlbHMsIGVpZ3ZhbHMgPSBzcGVjdHJhbF9jbHVzdGVyaW5nX3NjcmF0Y2goWCwgaz0yLCBzaWdtYT0wLjMpXG5wcmludChmXCJTcGVjdHJhbCBBUkk6IHthZGp1c3RlZF9yYW5kX3Njb3JlKHlfdHJ1ZSwgbGFiZWxzKTouNGZ9XCIpXG5rbV9sYWJlbHMgPSBLTWVhbnMobl9jbHVzdGVycz0yLCBuX2luaXQ9MTAsIHJhbmRvbV9zdGF0ZT00MikuZml0X3ByZWRpY3QoWClcbnByaW50KGZcIkstTWVhbnMgQVJJOiB7YWRqdXN0ZWRfcmFuZF9zY29yZSh5X3RydWUsIGttX2xhYmVscyk6LjRmfVwiKVxucHJpbnQoZlwiRmlyc3QgNCBlaWdlbnZhbHVlczoge2VpZ3ZhbHNbOjRdLnJvdW5kKDYpfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVpZ2VudmFsdWUgQW5hbHlzaXMgYW5kIENsdXN0ZXIgU3RydWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbnVtYmVyIG9mIHplcm8gKG9yIG5lYXItemVybykgZWlnZW52YWx1ZXMgb2YgTCByZXZlYWxzIHRoZSBudW1iZXIgb2YgY29ubmVjdGVkIGNvbXBvbmVudHMg4oCUIGFuZCBieSBleHRlbnNpb24sIHRoZSBudW1iZXIgb2YgbmF0dXJhbCBjbHVzdGVycy4gQW4gXHUwMDI3ZWlnZW5nYXBcdTAwMjcgaGV1cmlzdGljOiBjaG9vc2UgayB3aGVyZSB0aGVyZSBpcyBhIGxhcmdlIGdhcCBiZXR3ZWVuIM674oKWIGFuZCDOu+KCluKCiuKCgS4gVGhlIGZpcnN0IGsgZWlnZW52ZWN0b3JzIFUg4oiIIOKEneKBv8uj4bWPIGdpdmUgYSBrLWRpbWVuc2lvbmFsIHNwZWN0cmFsIGVtYmVkZGluZyB3aGVyZSBwb2ludHMgZnJvbSB0aGUgc2FtZSB3ZWxsLXNlcGFyYXRlZCBjbHVzdGVyIGFyZSBjbG9zZSB0b2dldGhlciAobmVhcmx5IGVxdWFsIHJvd3MpIGFuZCBwb2ludHMgZnJvbSBkaWZmZXJlbnQgY2x1c3RlcnMgYXJlIGZhciBhcGFydC4gVGhlIEZpZWRsZXIgdmVjdG9yIHXigoIgKHNlY29uZCBlaWdlbnZlY3RvcikgYmlwYXJ0aXRpb25zIHRoZSBncmFwaCBhbG9uZyBpdHMgd2Vha2VzdCBib3R0bGVuZWNrIOKAlCB0aGlzIGlzIHRoZSBzcGVjdHJhbCByZWxheGF0aW9uIG9mIHRoZSBub3JtYWxpemVkIGN1dCBwcm9ibGVtLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9tb29ucywgbWFrZV9jaXJjbGVzXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuZGVmIGJ1aWxkX2xhcGxhY2lhbihYLCBzaWdtYT0wLjUpOlxuICAgIGRpc3RzX3NxID0gKChYWzosIE5vbmUsIDpdIC0gWFtOb25lLCA6LCA6XSkgKiogMikuc3VtKGF4aXM9MilcbiAgICBXID0gbnAuZXhwKC1kaXN0c19zcSAvICgyICogc2lnbWEgKiogMikpXG4gICAgbnAuZmlsbF9kaWFnb25hbChXLCAwKVxuICAgIGQgPSBXLnN1bShheGlzPTEpXG4gICAgRF9pbnZfc3FydCA9IG5wLmRpYWcoMS4wIC8gbnAuc3FydChkICsgMWUtMTApKVxuICAgIHJldHVybiBucC5leWUobGVuKFgpKSAtIERfaW52X3NxcnQgQCBXIEAgRF9pbnZfc3FydCwgV1xuXG5mb3IgbmFtZSwgKFgsIHlfdHJ1ZSkgaW4gWyhcdTAwMjdNb29uc1x1MDAyNywgbWFrZV9tb29ucygyMDAsIG5vaXNlPTAuMDYsIHJhbmRvbV9zdGF0ZT0wKSksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgKFx1MDAyN0NpcmNsZXNcdTAwMjcsIG1ha2VfY2lyY2xlcygyMDAsIG5vaXNlPTAuMDQsIGZhY3Rvcj0wLjUsIHJhbmRvbV9zdGF0ZT0wKSldOlxuICAgIFggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcbiAgICBMLCBXID0gYnVpbGRfbGFwbGFjaWFuKFgsIHNpZ21hPTAuMylcbiAgICBlaWd2YWxzID0gbnAubGluYWxnLmVpZ3ZhbHNoKEwpXG4gICAgZWlndmFsc19zb3J0ZWQgPSBucC5zb3J0KGVpZ3ZhbHMpWzo4XVxuICAgIGdhcHMgPSBucC5kaWZmKGVpZ3ZhbHNfc29ydGVkKVxuICAgIGJlc3RfayA9IG5wLmFyZ21heChnYXBzKSArIDFcbiAgICBwcmludChmXCJ7bmFtZX06IGZpcnN0IDggZWlnZW52YWx1ZXM6IHtlaWd2YWxzX3NvcnRlZC5yb3VuZCg0KX1cIilcbiAgICBwcmludChmXCIgIEVpZ2VuZ2FwIGhldXJpc3RpYyBzdWdnZXN0cyBrPXtiZXN0X2t9IChnYXA9e2dhcHNbYmVzdF9rLTFdOi40Zn0pXCIpXG4gICAgcHJpbnQoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6InNrbGVhcm4gU3BlY3RyYWxDbHVzdGVyaW5nIOKAlCBQcmFjdGljYWwgVXNhZ2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6InNrbGVhcm5cdTAwMjdzIFNwZWN0cmFsQ2x1c3RlcmluZyBoYW5kbGVzIHRoZSBmdWxsIHBpcGVsaW5lOiBhZmZpbml0eSBtYXRyaXggY29uc3RydWN0aW9uIChSQkYga2VybmVsIG9yIHByZWNvbXB1dGVkKSwgbm9ybWFsaXplZCBMYXBsYWNpYW4gY29tcHV0YXRpb24sIGVpZ2VuZGVjb21wb3NpdGlvbiAoQVJQQUNLIGZvciBzcGFyc2UgbWF0cmljZXMpLCBhbmQgay1tZWFucyBpbiB0aGUgc3BlY3RyYWwgZW1iZWRkaW5nLiBLZXkgcGFyYW1ldGVyczogbl9jbHVzdGVycyAoayksIGFmZmluaXR5IChcdTAwMjdyYmZcdTAwMjcsIFx1MDAyN25lYXJlc3RfbmVpZ2hib3JzXHUwMDI3LCBvciBcdTAwMjdwcmVjb21wdXRlZFx1MDAyNyksIGdhbW1hICg9MS8yz4PCsiBmb3IgUkJGKSwgYW5kIG5fbmVpZ2hib3JzIChmb3Igay1OTiBhZmZpbml0eSkuIFRoZSBcdTAwMjduZWFyZXN0X25laWdoYm9yc1x1MDAyNyBhZmZpbml0eSBidWlsZHMgYSBzcGFyc2Ugay1OTiBncmFwaCBhbmQgaXMgcmVjb21tZW5kZWQgZm9yIGxhcmdlIG4gYXMgaXQgYXZvaWRzIHRoZSBPKG7CsikgZGVuc2UgYWZmaW5pdHkgbWF0cml4LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBTcGVjdHJhbENsdXN0ZXJpbmdcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9tb29ucywgbWFrZV9jaXJjbGVzXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWRqdXN0ZWRfcmFuZF9zY29yZVxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbmRhdGFzZXRzID0gW1xuICAgIChcdTAwMjdNb29uc1x1MDAyNywgICAqbWFrZV9tb29ucyhuX3NhbXBsZXM9MzAwLCBub2lzZT0wLjA3LCByYW5kb21fc3RhdGU9NDIpKSxcbiAgICAoXHUwMDI3Q2lyY2xlc1x1MDAyNywgKm1ha2VfY2lyY2xlcyhuX3NhbXBsZXM9MzAwLCBub2lzZT0wLjA1LCBmYWN0b3I9MC41LCByYW5kb21fc3RhdGU9NDIpKSxcbl1cblxuZm9yIG5hbWUsIFgsIHlfdHJ1ZSBpbiBkYXRhc2V0czpcbiAgICBYID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG4gICAgIyBSQkYgYWZmaW5pdHlcbiAgICBzY19yYmYgPSBTcGVjdHJhbENsdXN0ZXJpbmcobl9jbHVzdGVycz0yLCBhZmZpbml0eT1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTEwLjAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9pbml0PTEwLCByYW5kb21fc3RhdGU9NDIpXG4gICAgbGFiZWxzX3JiZiA9IHNjX3JiZi5maXRfcHJlZGljdChYKVxuICAgICMgay1OTiBhZmZpbml0eSAoc3BhcnNlIOKAlCBiZXR0ZXIgZm9yIGxhcmdlciBuKVxuICAgIHNjX2tubiA9IFNwZWN0cmFsQ2x1c3RlcmluZyhuX2NsdXN0ZXJzPTIsIGFmZmluaXR5PVx1MDAyN25lYXJlc3RfbmVpZ2hib3JzXHUwMDI3LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5fbmVpZ2hib3JzPTE1LCBuX2luaXQ9MTAsIHJhbmRvbV9zdGF0ZT00MilcbiAgICBsYWJlbHNfa25uID0gc2Nfa25uLmZpdF9wcmVkaWN0KFgpXG4gICAgYXJpX3JiZiA9IGFkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCBsYWJlbHNfcmJmKVxuICAgIGFyaV9rbm4gPSBhZGp1c3RlZF9yYW5kX3Njb3JlKHlfdHJ1ZSwgbGFiZWxzX2tubilcbiAgICBwcmludChmXCJ7bmFtZX06XCIpXG4gICAgcHJpbnQoZlwiICBSQkYgYWZmaW5pdHkgKGdhbW1hPTEwKTogQVJJPXthcmlfcmJmOi40Zn1cIilcbiAgICBwcmludChmXCIgIGstTk4gYWZmaW5pdHkgKGs9MTUpOiAgIEFSST17YXJpX2tubjouNGZ9XCIpXG4gICAgcHJpbnQoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5vcm1hbGl6ZWQgQ3V0IE9iamVjdGl2ZSBhbmQgTWFya292IENoYWluIENvbm5lY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNwZWN0cmFsIGNsdXN0ZXJpbmcgbWluaW1pemVzIHRoZSBOb3JtYWxpemVkIEN1dDogTmN1dChBLEIpID0gY3V0KEEsQikvdm9sKEEpICsgY3V0KEEsQikvdm9sKEIpIHdoZXJlIGN1dChBLEIpID0gzqNfe2niiIhBLGriiIhCfSB34bWi4rG8IGFuZCB2b2woQSkgPSDOo197aeKIiEF9IGThtaIuIE5jdXQgcGVuYWxpemVzIGN1dHMgdGhhdCBpc29sYXRlIHNtYWxsIGNsdXN0ZXJzIChsb3cgdm9sdW1lKSwgYmFsYW5jaW5nIHBhcnRpdGlvbiBzaXplcy4gVGhlIG5vcm1hbGl6ZWQgTGFwbGFjaWFuIGVpZ2VudmVjdG9ycyBwcm92aWRlIHRoZSBjb250aW51b3VzIHJlbGF4YXRpb24gb2YgdGhpcyBjb21iaW5hdG9yaWFsIHByb2JsZW0uIFRoZSBNYXJrb3YgY2hhaW4gY29ubmVjdGlvbjogROKBu8K5VyBpcyB0aGUgdHJhbnNpdGlvbiBtYXRyaXggb2YgYSByYW5kb20gd2FsayBvbiB0aGUgZ3JhcGguIFRoZSBzcGVjdHJhbCBlbWJlZGRpbmcgZ3JvdXBzIHBvaW50cyB0aGF0IGEgcmFuZG9tIHdhbGtlciB2aXNpdHMgdG9nZXRoZXIg4oCUIGludHVpdGl2ZWx5LCBjbHVzdGVycyBhcmUgc2V0cyBvZiBub2RlcyB0aGUgd2FsayByYXJlbHkgZXNjYXBlcyBmcm9tLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBTcGVjdHJhbENsdXN0ZXJpbmcsIEtNZWFuc1xuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX21vb25zLCBtYWtlX2NpcmNsZXMsIG1ha2VfYmxvYnNcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBhZGp1c3RlZF9yYW5kX3Njb3JlXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuZGF0YXNldHMgPSBbXG4gICAgKFx1MDAyN01vb25zXHUwMDI3LCAgICptYWtlX21vb25zKG5fc2FtcGxlcz00MDAsIG5vaXNlPTAuMDcsIHJhbmRvbV9zdGF0ZT00MikpLFxuICAgIChcdTAwMjdDaXJjbGVzXHUwMDI3LCAqbWFrZV9jaXJjbGVzKG5fc2FtcGxlcz00MDAsIG5vaXNlPTAuMDUsIGZhY3Rvcj0wLjUsIHJhbmRvbV9zdGF0ZT00MikpLFxuICAgIChcdTAwMjdCbG9ic1x1MDAyNywgICAqbWFrZV9ibG9icyhuX3NhbXBsZXM9NDAwLCBjZW50ZXJzPTMsIGNsdXN0ZXJfc3RkPTAuOCwgcmFuZG9tX3N0YXRlPTQyKSksXG5dXG5cbnByaW50KGZcIntcdTAwMjdEYXRhc2V0XHUwMDI3OjEwc30ge1x1MDAyN1NwZWN0cmFsIEFSSVx1MDAyNzpcdTAwM2UxNH0ge1x1MDAyN0tNZWFucyBBUklcdTAwMjc6XHUwMDNlMTJ9XCIpXG5mb3IgbmFtZSwgWCwgeV90cnVlIGluIGRhdGFzZXRzOlxuICAgIFggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcbiAgICBrID0gbGVuKG5wLnVuaXF1ZSh5X3RydWUpKVxuICAgIHNjID0gU3BlY3RyYWxDbHVzdGVyaW5nKG5fY2x1c3RlcnM9aywgYWZmaW5pdHk9XHUwMDI3cmJmXHUwMDI3LCBnYW1tYT04LjAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5faW5pdD0xMCwgcmFuZG9tX3N0YXRlPTQyKVxuICAgIGttID0gS01lYW5zKG5fY2x1c3RlcnM9aywgbl9pbml0PTEwLCByYW5kb21fc3RhdGU9NDIpXG4gICAgc3BfbGFiZWxzID0gc2MuZml0X3ByZWRpY3QoWClcbiAgICBrbV9sYWJlbHMgPSBrbS5maXRfcHJlZGljdChYKVxuICAgIGFyaV9zcCA9IGFkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCBzcF9sYWJlbHMpXG4gICAgYXJpX2ttID0gYWRqdXN0ZWRfcmFuZF9zY29yZSh5X3RydWUsIGttX2xhYmVscylcbiAgICBwcmludChmXCJ7bmFtZToxMHN9IHthcmlfc3A6XHUwMDNlMTQuNGZ9IHthcmlfa206XHUwMDNlMTIuNGZ9XCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJTY2FsYWJpbGl0eSBMaW1pdGF0aW9uIiwiY29udGVudCI6Ik5haXZlIHNwZWN0cmFsIGNsdXN0ZXJpbmcgcmVxdWlyZXMgYW4gTyhuwrIpIGRlbnNlIGFmZmluaXR5IG1hdHJpeCBhbmQgTyhuwrMpIGVpZ2VuZGVjb21wb3NpdGlvbiwgbGltaXRpbmcgaXQgdG8gbiBcdTAwM2MgNSwwMDDigJMxMCwwMDAuIEZvciBsYXJnZXIgZGF0YXNldHM6ICgxKSB1c2UgbmVhcmVzdF9uZWlnaGJvcnMgYWZmaW5pdHkgaW4gc2tsZWFybiB0byBidWlsZCBhIHNwYXJzZSBncmFwaDsgKDIpIHVzZSBOeXN0csO2bSBhcHByb3hpbWF0aW9uIHRvIHN1YnNhbXBsZSBsYW5kbWFyayBwb2ludHM7ICgzKSB1c2Ugc2tsZWFyblx1MDAyN3MgU3BlY3RyYWxDbHVzdGVyaW5nIHdpdGggZWlnZW5fc29sdmVyPVx1MDAyN2FycGFja1x1MDAyNyBmb3IgdGhlIHNwYXJzZSBlaWdlbnZhbHVlIHNvbHZlci4gREJTQ0FOIG9yIEhEQlNDQU4gYXJlIG9mdGVuIGJldHRlciBjaG9pY2VzIGZvciB2ZXJ5IGxhcmdlIGRhdGFzZXRzIHdpdGggbm9uLWNvbnZleCBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHVuaW5nIHRoZSBBZmZpbml0eSDigJQgU2lnbWEgYW5kIGstTk4gR3JhcGgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBhZmZpbml0eSBwYXJhbWV0ZXIgz4MgKG9yIGVxdWl2YWxlbnRseSBnYW1tYSA9IDEvMs+DwrIpIGNvbnRyb2xzIHdoYXQgY291bnRzIGFzIFx1MDAyN25lYXJieS5cdTAwMjcgVG9vIHNtYWxsIM+DIGRpc2Nvbm5lY3RzIHRoZSBncmFwaCDigJQgZWFjaCBwb2ludCBpcyBpc29sYXRlZCBhbmQgdGhlIHNwZWN0cmFsIGVtYmVkZGluZyBpcyBkZWdlbmVyYXRlLiBUb28gbGFyZ2Ugz4MgY29ubmVjdHMgZXZlcnl0aGluZyBhbmQgZWxpbWluYXRlcyB0aGUgY2x1c3RlciBzdHJ1Y3R1cmUuIFRoZSBrLU5OIGFmZmluaXR5IGF2b2lkcyB0aGlzIHNlbnNpdGl2aXR5OiBjb25uZWN0aW5nIGVhY2ggcG9pbnQgdG8gaXRzIGsgbmVhcmVzdCBuZWlnaGJvcnMgY3JlYXRlcyBhIHNwYXJzZSBncmFwaCB0aGF0IHByZXNlcnZlcyBsb2NhbCB0b3BvbG9neSB3aXRob3V0IHJlcXVpcmluZyDPgyB0byBiZSBzZXQuIEZvciBtb3N0IGRhdGFzZXRzLCBrLU5OIGFmZmluaXR5IHdpdGggaz0xMOKAkzMwIG91dHBlcmZvcm1zIFJCRiBhZmZpbml0eSBhbmQgc2NhbGVzIGJldHRlciB2aWEgc3BhcnNlIGxpbmVhciBhbGdlYnJhLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNsdXN0ZXJpbmcgQWxnb3JpdGhtIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJLLU1lYW5zIiwiREJTQ0FOIiwiU3BlY3RyYWwiLCJHTU0iXSwicm93cyI6W1siTm9uLWNvbnZleCBjbHVzdGVycyIsIk5vIiwiWWVzIiwiWWVzIiwiUGFydGlhbCAoZWxsaXB0aWNhbCkiXSxbIlVzZXMgZ3JhcGggc3RydWN0dXJlIiwiTm8iLCJMb2NhbCBkZW5zaXR5IiwiWWVzIOKAlCBnbG9iYWwgZ3JhcGgiLCJObyJdLFsiT3V0bGllciBoYW5kbGluZyIsIk5vbmUiLCJFeHBsaWNpdCBub2lzZSIsIk5vbmUgKGFsbCBhc3NpZ25lZCkiLCJTb2Z0IGxvdy1kZW5zaXR5Il0sWyJTY2FsYWJsZSB0byBuXHUwMDNlMTAwSyIsIlllcyAobWluaS1iYXRjaCkiLCJZZXMgKHNwYXRpYWwgaW5kZXgpIiwiTm8gKE8obsKzKSBuYWl2ZSkiLCJZZXMgKG1pbmktYmF0Y2ggRU0pIl0sWyJrIHJlcXVpcmVkIiwiWWVzIiwiTm8iLCJZZXMiLCJZZXMiXSxbIk1haW4gaHlwZXJwYXJhbWV0ZXIiLCJrIiwizrUsIG1pblB0cyIsImssIM+DIChvciBrLU5OKSIsImssIGNvdmFyaWFuY2UgdHlwZSJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJDaG9vc2luZyBhZmZpbml0eTogUkJGIGtlcm5lbCB3aXRoIGdhbW1hIHR1bmVkIHZpYSBrLWRpc3RhbmNlIHBsb3Q7IGFsdGVybmF0aXZlbHkgbmVhcmVzdF9uZWlnaGJvcnMgd2l0aCBrPTEw4oCTMzAgZm9yIGxhcmdlIG4uIiwiQ2hvb3Npbmcgc2lnbWEgZm9yIFJCRjogc2V0IM+DIHRvIHRoZSBtZWRpYW4gcGFpcndpc2UgZGlzdGFuY2Ugb3IgdXNlIHNpZ21hID0ga3RoLU5OIGRpc3RhbmNlOyB0b28gc21hbGwgZGlzY29ubmVjdHMgdGhlIGdyYXBoLCB0b28gbGFyZ2UgY29ubmVjdHMgZXZlcnl0aGluZy4iLCJFaWdlbmdhcCBoZXVyaXN0aWMgZm9yIGs6IGNvbXB1dGUgTF9zeW0gZWlnZW52YWx1ZXMgYW5kIGxvb2sgZm9yIGEgbGFyZ2UgZ2FwIOKAlCB0aGUgbmF0dXJhbCBrIGNvcnJlc3BvbmRzIHRvIHRoZSBnYXAgcG9zaXRpb24uIiwiay1OTiBhZmZpbml0eSBpcyBmYXN0ZXIgYW5kIG1vcmUgaW50ZXJwcmV0YWJsZSBmb3IgaGlnaC1kaW1lbnNpb25hbCBkYXRhOyBSQkYgaXMgc21vb3RoZXIgZm9yIGxvdy1kaW1lbnNpb25hbCBkYXRhLiIsIk5vcm1hbGl6ZSByb3dzIG9mIHRoZSBlbWJlZGRpbmcgVSB0byB1bml0IG5vcm0gYmVmb3JlIGstbWVhbnMg4oCUIHRoaXMgaXMgc3RhbmRhcmQgcHJhY3RpY2UgaW4gbm9ybWFsaXplZCBzcGVjdHJhbCBjbHVzdGVyaW5nLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Spectral Clustering — Graph Laplacian and Normalized Cut

Spectral clustering solves the problem k-means cannot: clustering data with non-convex, non-spherical structure. The core insight is to represent the data as a similarity graph, then cluster in the graph's spectral (Laplacian eigenvector) space rather than the original feature space. In the spectral embedding, non-convex shapes in input space become linearly separable — a simple k-means in the embedding then recovers the true clusters. The method is grounded in graph partitioning theory and connects to random walks on graphs.

## Similarity Graph Construction

Given n points, construct a weighted graph where nodes are points and edge weights encode similarity. Two common choices: (1) ε-neighborhood graph: connect points with dist(xᵢ,xⱼ) ≤ ε, with binary or RBF-weighted edges; (2) k-NN graph: connect each point to its k nearest neighbors, with weights w(xᵢ,xⱼ) = exp(−‖xᵢ−xⱼ‖²/(2σ²)). The RBF (Gaussian) kernel σ controls the neighborhood scale — smaller σ means only very nearby points are connected. The resulting weight matrix W ∈ ℝⁿˣⁿ is symmetric with wᵢⱼ ≥ 0. The degree matrix D is diagonal with Dᵢᵢ = Σⱼ wᵢⱼ.

## Graph Laplacian

The unnormalized graph Laplacian is L = D − W. L is symmetric positive semi-definite: for any vector f, fᵀLf = (1/2) Σᵢⱼ wᵢⱼ(fᵢ−fⱼ)² ≥ 0. The smallest eigenvalue is always 0 (eigenvector = constant 1). The multiplicity of eigenvalue 0 equals the number of connected components — a key theorem linking spectral properties to graph structure. For a connected graph, the second-smallest eigenvalue λ₂ (Fiedler value) measures the graph's algebraic connectivity; its eigenvector (Fiedler vector) reveals the most natural bipartition. The normalized Laplacian L_sym = D^{−1/2}LD^{−1/2} = I − D^{−1/2}WD^{−1/2} is preferred for spectral clustering as it accounts for degree heterogeneity.

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score

def spectral_clustering_scratch(X, k, sigma=0.5, n_neighbors=10):
    """Spectral clustering: affinity -> Laplacian -> eigenvectors -> k-means."""
    n = X.shape[0]
    # Build RBF affinity matrix (full, not kNN for simplicity)
    dists_sq = ((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2)
    W = np.exp(-dists_sq / (2 * sigma ** 2))
    np.fill_diagonal(W, 0)  # no self-loops
    # Degree matrix and normalized Laplacian
    d = W.sum(axis=1)
    D_inv_sqrt = np.diag(1.0 / np.sqrt(d + 1e-10))
    L_sym = np.eye(n) - D_inv_sqrt @ W @ D_inv_sqrt
    # Eigendecomposition — k smallest eigenvectors
    eigvals, eigvecs = np.linalg.eigh(L_sym)
    U = eigvecs[:, :k]  # rows = embeddings for each point
    # Normalize rows to unit norm (standard practice)
    norms = np.linalg.norm(U, axis=1, keepdims=True)
    U_norm = U / (norms + 1e-10)
    # K-Means in spectral space
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(U_norm)
    return labels, eigvals[:k+2]

X, y_true = make_moons(n_samples=300, noise=0.07, random_state=42)
X = StandardScaler().fit_transform(X)
labels, eigvals = spectral_clustering_scratch(X, k=2, sigma=0.3)
print(f"Spectral ARI: {adjusted_rand_score(y_true, labels):.4f}")
km_labels = KMeans(n_clusters=2, n_init=10, random_state=42).fit_predict(X)
print(f"K-Means ARI: {adjusted_rand_score(y_true, km_labels):.4f}")
print(f"First 4 eigenvalues: {eigvals[:4].round(6)}")
```

## Eigenvalue Analysis and Cluster Structure

The number of zero (or near-zero) eigenvalues of L reveals the number of connected components — and by extension, the number of natural clusters. An 'eigengap' heuristic: choose k where there is a large gap between λₖ and λₖ₊₁. The first k eigenvectors U ∈ ℝⁿˣᵏ give a k-dimensional spectral embedding where points from the same well-separated cluster are close together (nearly equal rows) and points from different clusters are far apart. The Fiedler vector u₂ (second eigenvector) bipartitions the graph along its weakest bottleneck — this is the spectral relaxation of the normalized cut problem.

```python
import numpy as np
from sklearn.datasets import make_moons, make_circles
from sklearn.preprocessing import StandardScaler

def build_laplacian(X, sigma=0.5):
    dists_sq = ((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2)
    W = np.exp(-dists_sq / (2 * sigma ** 2))
    np.fill_diagonal(W, 0)
    d = W.sum(axis=1)
    D_inv_sqrt = np.diag(1.0 / np.sqrt(d + 1e-10))
    return np.eye(len(X)) - D_inv_sqrt @ W @ D_inv_sqrt, W

for name, (X, y_true) in [('Moons', make_moons(200, noise=0.06, random_state=0)),
                            ('Circles', make_circles(200, noise=0.04, factor=0.5, random_state=0))]:
    X = StandardScaler().fit_transform(X)
    L, W = build_laplacian(X, sigma=0.3)
    eigvals = np.linalg.eigvalsh(L)
    eigvals_sorted = np.sort(eigvals)[:8]
    gaps = np.diff(eigvals_sorted)
    best_k = np.argmax(gaps) + 1
    print(f"{name}: first 8 eigenvalues: {eigvals_sorted.round(4)}")
    print(f"  Eigengap heuristic suggests k={best_k} (gap={gaps[best_k-1]:.4f})")
    print()
```

## sklearn SpectralClustering — Practical Usage

sklearn's SpectralClustering handles the full pipeline: affinity matrix construction (RBF kernel or precomputed), normalized Laplacian computation, eigendecomposition (ARPACK for sparse matrices), and k-means in the spectral embedding. Key parameters: n_clusters (k), affinity ('rbf', 'nearest_neighbors', or 'precomputed'), gamma (=1/2σ² for RBF), and n_neighbors (for k-NN affinity). The 'nearest_neighbors' affinity builds a sparse k-NN graph and is recommended for large n as it avoids the O(n²) dense affinity matrix.

```python
import numpy as np
from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_moons, make_circles
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

datasets = [
    ('Moons',   *make_moons(n_samples=300, noise=0.07, random_state=42)),
    ('Circles', *make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=42)),
]

for name, X, y_true in datasets:
    X = StandardScaler().fit_transform(X)
    # RBF affinity
    sc_rbf = SpectralClustering(n_clusters=2, affinity='rbf', gamma=10.0,
                                  n_init=10, random_state=42)
    labels_rbf = sc_rbf.fit_predict(X)
    # k-NN affinity (sparse — better for larger n)
    sc_knn = SpectralClustering(n_clusters=2, affinity='nearest_neighbors',
                                  n_neighbors=15, n_init=10, random_state=42)
    labels_knn = sc_knn.fit_predict(X)
    ari_rbf = adjusted_rand_score(y_true, labels_rbf)
    ari_knn = adjusted_rand_score(y_true, labels_knn)
    print(f"{name}:")
    print(f"  RBF affinity (gamma=10): ARI={ari_rbf:.4f}")
    print(f"  k-NN affinity (k=15):   ARI={ari_knn:.4f}")
    print()
```

## Normalized Cut Objective and Markov Chain Connection

Spectral clustering minimizes the Normalized Cut: Ncut(A,B) = cut(A,B)/vol(A) + cut(A,B)/vol(B) where cut(A,B) = Σ_{i∈A,j∈B} wᵢⱼ and vol(A) = Σ_{i∈A} dᵢ. Ncut penalizes cuts that isolate small clusters (low volume), balancing partition sizes. The normalized Laplacian eigenvectors provide the continuous relaxation of this combinatorial problem. The Markov chain connection: D⁻¹W is the transition matrix of a random walk on the graph. The spectral embedding groups points that a random walker visits together — intuitively, clusters are sets of nodes the walk rarely escapes from.

```python
import numpy as np
from sklearn.cluster import SpectralClustering, KMeans
from sklearn.datasets import make_moons, make_circles, make_blobs
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

datasets = [
    ('Moons',   *make_moons(n_samples=400, noise=0.07, random_state=42)),
    ('Circles', *make_circles(n_samples=400, noise=0.05, factor=0.5, random_state=42)),
    ('Blobs',   *make_blobs(n_samples=400, centers=3, cluster_std=0.8, random_state=42)),
]

print(f"{'Dataset':10s} {'Spectral ARI':>14} {'KMeans ARI':>12}")
for name, X, y_true in datasets:
    X = StandardScaler().fit_transform(X)
    k = len(np.unique(y_true))
    sc = SpectralClustering(n_clusters=k, affinity='rbf', gamma=8.0,
                             n_init=10, random_state=42)
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    sp_labels = sc.fit_predict(X)
    km_labels = km.fit_predict(X)
    ari_sp = adjusted_rand_score(y_true, sp_labels)
    ari_km = adjusted_rand_score(y_true, km_labels)
    print(f"{name:10s} {ari_sp:>14.4f} {ari_km:>12.4f}")
```

> **Scalability Limitation**: Naive spectral clustering requires an O(n²) dense affinity matrix and O(n³) eigendecomposition, limiting it to n < 5,000–10,000. For larger datasets: (1) use nearest_neighbors affinity in sklearn to build a sparse graph; (2) use Nyström approximation to subsample landmark points; (3) use sklearn's SpectralClustering with eigen_solver='arpack' for the sparse eigenvalue solver. DBSCAN or HDBSCAN are often better choices for very large datasets with non-convex structure.

## Tuning the Affinity — Sigma and k-NN Graph

The affinity parameter σ (or equivalently gamma = 1/2σ²) controls what counts as 'nearby.' Too small σ disconnects the graph — each point is isolated and the spectral embedding is degenerate. Too large σ connects everything and eliminates the cluster structure. The k-NN affinity avoids this sensitivity: connecting each point to its k nearest neighbors creates a sparse graph that preserves local topology without requiring σ to be set. For most datasets, k-NN affinity with k=10–30 outperforms RBF affinity and scales better via sparse linear algebra.

## Clustering Algorithm Comparison

| Property | K-Means | DBSCAN | Spectral | GMM |
| --- | --- | --- | --- | --- |
| Non-convex clusters | No | Yes | Yes | Partial (elliptical) |
| Uses graph structure | No | Local density | Yes — global graph | No |
| Outlier handling | None | Explicit noise | None (all assigned) | Soft low-density |
| Scalable to n>100K | Yes (mini-batch) | Yes (spatial index) | No (O(n³) naive) | Yes (mini-batch EM) |
| k required | Yes | No | Yes | Yes |
| Main hyperparameter | k | ε, minPts | k, σ (or k-NN) | k, covariance type |

- Choosing affinity: RBF kernel with gamma tuned via k-distance plot; alternatively nearest_neighbors with k=10–30 for large n.
- Choosing sigma for RBF: set σ to the median pairwise distance or use sigma = kth-NN distance; too small disconnects the graph, too large connects everything.
- Eigengap heuristic for k: compute L_sym eigenvalues and look for a large gap — the natural k corresponds to the gap position.
- k-NN affinity is faster and more interpretable for high-dimensional data; RBF is smoother for low-dimensional data.
- Normalize rows of the embedding U to unit norm before k-means — this is standard practice in normalized spectral clustering.

---

