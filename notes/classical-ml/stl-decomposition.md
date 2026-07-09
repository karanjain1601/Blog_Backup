---
title: "STL Decomposition — Seasonal-Trend via LOESS"
slug: "stl-decomposition"
description: "Understand STL's inner and outer loop algorithm using LOESS smoothing, tune the key parameters (seasonal, trend, robust), extend to multiple seasonal periods with MSTL, and validate decomposition quality via residual analysis."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU1RMIChTZWFzb25hbC1UcmVuZCBkZWNvbXBvc2l0aW9uIHVzaW5nIExPRVNTKSBvdmVyY29tZXMgdGhyZWUgY3JpdGljYWwgbGltaXRhdGlvbnMgb2YgY2xhc3NpY2FsIGRlY29tcG9zaXRpb246IGl0IGhhbmRsZXMgYW55IHNlYXNvbmFsIHBlcmlvZCAobm90IGp1c3QgaW50ZWdlciBtdWx0aXBsZXMgb2YgMTIpLCBpdCBjYW4gdXNlIGEgcm9idXN0IG9wdGlvbiB0aGF0IGRvd24td2VpZ2h0cyBvdXRsaWVycywgYW5kIGl0IGFsbG93cyB0aGUgc2Vhc29uYWwgY29tcG9uZW50IHRvIGV2b2x2ZSBzbG93bHkgb3ZlciB0aW1lLiBQdWJsaXNoZWQgYnkgQ2xldmVsYW5kIGV0IGFsLiAoMTk5MCksIFNUTCByZW1haW5zIHRoZSBnb2xkIHN0YW5kYXJkIGZvciBleHBsb3JhdG9yeSBkZWNvbXBvc2l0aW9uIGFuZCBpcyB0aGUgYmFja2JvbmUgb2Ygc2V2ZXJhbCBwcm9kdWN0aW9uIGZvcmVjYXN0aW5nIGZyYW1ld29ya3MgaW5jbHVkaW5nIEZhY2Vib29rIFByb3BoZXQgYW5kIHRoZSBOaXh0bGEgc3RhY2suIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTE9FU1Mg4oCUIExvY2FsbHkgRXN0aW1hdGVkIFNjYXR0ZXJwbG90IFNtb290aGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTE9FU1MgZml0cyBhIHdlaWdodGVkIGxvY2FsIHBvbHlub21pYWwgcmVncmVzc2lvbiBhdCBlYWNoIHBvaW50IHjigpwuIE9ic2VydmF0aW9ucyBjbG9zZXIgdG8geOKCnCByZWNlaXZlIGhpZ2hlciB3ZWlnaHRzICh0eXBpY2FsbHkgdXNpbmcgYSB0cmljdWJpYyBrZXJuZWwpLiBUaGUgYmFuZHdpZHRoIHBhcmFtZXRlciBjb250cm9scyB0aGUgZnJhY3Rpb24gb2YgZGF0YSB1c2VkIGluIGVhY2ggbG9jYWwgZml0OiBzbWFsbGVyIGJhbmR3aWR0aCBnaXZlcyBtb3JlIGZsZXhpYmxlLCB3aWdnbHkgc21vb3RoaW5nOyBsYXJnZXIgYmFuZHdpZHRoIGdpdmVzIHNtb290aGVyLCBtb3JlIGdsb2JhbCBlc3RpbWF0ZXMuIFNUTCB1c2VzIExPRVNTIGFzIGEgYnVpbGRpbmcgYmxvY2sgZm9yIGJvdGggdGhlIHNlYXNvbmFsIGFuZCB0cmVuZCBzbW9vdGhlcnMsIHdpdGggc2VwYXJhdGUgYmFuZHdpZHRoIHBhcmFtZXRlcnMgZm9yIGVhY2ggY29tcG9uZW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNUTCBBbGdvcml0aG0g4oCUIElubmVyIGFuZCBPdXRlciBMb29wcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU1RMIGFsdGVybmF0ZXMgYmV0d2VlbiBhbiBpbm5lciBsb29wIGFuZCBhbiBvdXRlciBsb29wLiBUaGUgaW5uZXIgbG9vcCBpdGVyYXRlcyBzZXZlcmFsIHRpbWVzLCB1cGRhdGluZyBzZWFzb25hbCBhbmQgdHJlbmQgZXN0aW1hdGVzOiAoMSkgZGV0cmVuZCB0aGUgc2VyaWVzIChzdWJ0cmFjdCBjdXJyZW50IHRyZW5kIGVzdGltYXRlKSwgKDIpIHNtb290aCBlYWNoIHNlYXNvbmFsIHN1Yi1zZXJpZXMgKGFsbCBKYW51YXJ5IHZhbHVlcywgYWxsIEZlYnJ1YXJ5IHZhbHVlcywgZXRjLikgd2l0aCBhIExPRVNTIG9mIHdpbmRvdyBu4oKbIHRvIGdldCBhIHJhdyBzZWFzb25hbCBlc3RpbWF0ZSwgKDMpIGFwcGx5IGEgbG93LXBhc3MgZmlsdGVyIChNQSB0aGVuIExPRVNTKSB0byByZW1vdmUgbG93LWZyZXF1ZW5jeSBjb250YW1pbmF0aW9uIGZyb20gdGhlIHNlYXNvbmFsIGVzdGltYXRlLCAoNCkgc3VidHJhY3QgdGhlIHNlYXNvbmFsIGVzdGltYXRlIGFuZCBzbW9vdGggdGhlIGRlc2Vhc29uYWxpc2VkIHNlcmllcyB3aXRoIExPRVNTIG9mIHdpbmRvdyBu4oKcIHRvIHVwZGF0ZSB0aGUgdHJlbmQuIFRoZSBvdXRlciBsb29wIGNvbXB1dGVzIHJvYnVzdG5lc3Mgd2VpZ2h0cyBiYXNlZCBvbiByZXNpZHVhbCBtYWduaXR1ZGUgKGJpc3F1YXJlIHdlaWdodHMpLCByZWR1Y2luZyB0aGUgaW5mbHVlbmNlIG9mIG91dGxpZXJzIGluIHN1YnNlcXVlbnQgaW5uZXIgbG9vcCBpdGVyYXRpb25zLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjp0cnVlLCJpdGVtcyI6WyJPdXRlciBsb29wIGluaXRpYWxpc2VzOiB0cmVuZCA9IDAsIHNlYXNvbmFsID0gMCwgcm9idXN0bmVzcyB3ZWlnaHRzID0gMS4iLCJJbm5lciBsb29wIChyZXBlYXRlZCBuX2lubmVyIHRpbWVzKTogdXBkYXRlIHNlYXNvbmFsIHZpYSBMT0VTUyBvbiBzdWItc2VyaWVzLCBhcHBseSBsb3ctcGFzcyBmaWx0ZXIsIHVwZGF0ZSB0cmVuZCB2aWEgTE9FU1Mgb24gZGVzZWFzb25hbGlzZWQgZGF0YS4iLCJPdXRlciBsb29wIChpZiByb2J1c3Q9VHJ1ZSk6IGNvbXB1dGUgcmVzaWR1YWxzLCBhc3NpZ24gYmlzcXVhcmUgcm9idXN0bmVzcyB3ZWlnaHRzLCByZXBlYXQgaW5uZXIgbG9vcCB3aXRoIHdlaWdodGVkIExPRVNTLiIsIkZpbmFsIGRlY29tcG9zaXRpb246IFTigpwgKHRyZW5kKSwgU+KCnCAoc2Vhc29uYWwpLCBS4oKcID0geeKCnCDiiJIgVOKCnCDiiJIgU+KCnCAocmVtYWluZGVyKS4iLCJUaGUgc2Vhc29uYWwgY29tcG9uZW50IHN1bSBvdmVyIG9uZSBwZXJpb2Qg4omIIDAgYnV0IGlzIG5vdCBmb3JjZWQgdG8gYmUgZXhhY3RseSB6ZXJvIOKAlCBpdCBjYW4gZHJpZnQgc2xvd2x5LiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSdW5uaW5nIFNUTCB3aXRoIHN0YXRzbW9kZWxzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2Euc2Vhc29uYWwgaW1wb3J0IFNUTFxuXG5ucC5yYW5kb20uc2VlZCgwKVxubiA9IDE1NiAgIyAzIHllYXJzIG9mIHdlZWtseSBkYXRhXG50ID0gbnAuYXJhbmdlKG4pXG5cbiMgQ29uc3RydWN0IHNlcmllczogdHJlbmQgKyB3ZWVrbHkgc2Vhc29uICsgbm9pc2VcbnRyZW5kX3RydWUgPSAxMDAgKyAwLjUgKiB0XG5zZWFzb24gPSAxNSAqIG5wLnNpbigyICogbnAucGkgKiB0IC8gNTIpXG55ID0gdHJlbmRfdHJ1ZSArIHNlYXNvbiArIDMgKiBucC5yYW5kb20ucmFuZG4obilcblxuIyBGaXQgU1RMIHdpdGggcGVyaW9kPTUyICh3ZWVrbHkgd2l0aCB5ZWFybHkgc2Vhc29uYWxpdHkpXG5zdGwgPSBTVEwoeSwgcGVyaW9kPTUyLCBzZWFzb25hbD0xMywgdHJlbmQ9Tm9uZSwgcm9idXN0PVRydWUpXG5yZXN1bHQgPSBzdGwuZml0KClcblxuIyBJbnNwZWN0IGNvbXBvbmVudHNcbnZhbGlkID0gfm5wLmlzbmFuKHJlc3VsdC50cmVuZClcbnByaW50KGZcIlRyZW5kICByYW5nZTogW3tyZXN1bHQudHJlbmRbdmFsaWRdLm1pbigpOi4xZn0sIHtyZXN1bHQudHJlbmRbdmFsaWRdLm1heCgpOi4xZn1dXCIpXG5wcmludChmXCJTZWFzb25hbCByYW5nZTogW3tyZXN1bHQuc2Vhc29uYWwubWluKCk6LjJmfSwge3Jlc3VsdC5zZWFzb25hbC5tYXgoKTouMmZ9XVwiKVxucHJpbnQoZlwiUmVzaWQgIHN0ZDogIHtyZXN1bHQucmVzaWQuc3RkKCk6LjRmfVwiKVxucHJpbnQoZlwiU2Vhc29uYWwgc3RyZW5ndGg6IHttYXgoMCwgMSAtIHJlc3VsdC5yZXNpZC52YXIoKSAvIChyZXN1bHQuc2Vhc29uYWwgKyByZXN1bHQucmVzaWQpLnZhcigpKTouNGZ9XCIpXG5wcmludChmXCJUcmVuZCBzdHJlbmd0aDogICAge21heCgwLCAxIC0gcmVzdWx0LnJlc2lkLnZhcigpIC8gKHJlc3VsdC50cmVuZCArIHJlc3VsdC5yZXNpZCkudmFyKCkpOi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSb2J1c3QgU1RMIOKAlCBIYW5kbGluZyBPdXRsaWVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gbm9uLXJvYnVzdCBTVEwgYWxsIHJlc2lkdWFscyBoYXZlIGVxdWFsIHdlaWdodC4gSWYgdGhlIHNlcmllcyBjb250YWlucyBvdXRsaWVycyAoZGF0YSBlbnRyeSBlcnJvcnMsIHN0cmlrZXMsIG5hdHVyYWwgZGlzYXN0ZXJzKSwgdGhleSBwdWxsIHRoZSBMT0VTUyBzbW9vdGhlciBhbmQgY29udGFtaW5hdGUgdGhlIHNlYXNvbmFsIGFuZCB0cmVuZCBlc3RpbWF0ZXMuIFJvYnVzdCBTVEwgYWRkcyBhbiBvdXRlciBsb29wIHRoYXQgY29tcHV0ZXMgYmlzcXVhcmUgd2VpZ2h0czogd+KCnCA9ICgxIOKIkiAofFLigpx8Lyg2wrdtZWRpYW4ofFJ8KSkpwrIpwrIgZm9yIHxS4oKcfCBcdTAwM2MgNsK3bWVkaWFuKHxSfCksIGFuZCAwIG90aGVyd2lzZS4gT2JzZXJ2YXRpb25zIHdpdGggdmVyeSBsYXJnZSByZXNpZHVhbHMgcmVjZWl2ZSBuZWFyLXplcm8gd2VpZ2h0cyBhbmQgaGF2ZSBuZWdsaWdpYmxlIGluZmx1ZW5jZSBvbiBzdWJzZXF1ZW50IExPRVNTIGZpdHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2Euc2Vhc29uYWwgaW1wb3J0IFNUTFxuXG5ucC5yYW5kb20uc2VlZCg1KVxubiA9IDEyMFxudCA9IG5wLmFyYW5nZShuKVxueV9jbGVhbiA9IDUwICsgMC4zKnQgKyAxMCpucC5zaW4oMipucC5waSp0LzEyKSArIDIqbnAucmFuZG9tLnJhbmRuKG4pXG5cbiMgSW5qZWN0IG91dGxpZXJzIGF0IGEgZmV3IHBvc2l0aW9uc1xueV9kaXJ0eSA9IHlfY2xlYW4uY29weSgpXG5vdXRsaWVyX2lkeCA9IFszMCwgNjAsIDkwXVxuZm9yIGlkeCBpbiBvdXRsaWVyX2lkeDpcbiAgICB5X2RpcnR5W2lkeF0gKz0gNjAgICMgbGFyZ2UgcG9zaXRpdmUgc3Bpa2VcblxucHJpbnQoZlwie1x1MDAyN01ldGhvZFx1MDAyNzoyMHN9ICB7XHUwMDI3VHJlbmQgUk1TRVx1MDAyNzoxMnN9ICB7XHUwMDI3U2Vhc29uIFJNU0VcdTAwMjc6MTJzfSAge1x1MDAyN1Jlc2lkIHN0ZFx1MDAyNzoxMHN9XCIpXG5wcmludChcIi1cIiAqIDYwKVxuXG50cnVlX3RyZW5kICA9IDUwICsgMC4zKnRcbnRydWVfc2Vhc29uID0gMTAqbnAuc2luKDIqbnAucGkqdC8xMilcblxuZm9yIHJvYnVzdCBpbiBbRmFsc2UsIFRydWVdOlxuICAgIHN0bCA9IFNUTCh5X2RpcnR5LCBwZXJpb2Q9MTIsIHNlYXNvbmFsPTcsIHJvYnVzdD1yb2J1c3QpXG4gICAgciA9IHN0bC5maXQoKVxuICAgIHRyZW5kX3Jtc2UgID0gbnAuc3FydChucC5tZWFuKChyLnRyZW5kICAtIHRydWVfdHJlbmQpKioyKSlcbiAgICBzZWFzb25fcm1zZSA9IG5wLnNxcnQobnAubWVhbigoci5zZWFzb25hbCAtIHRydWVfc2Vhc29uKSoqMikpXG4gICAgbGFiZWwgPSBcIlJvYnVzdCBTVExcIiBpZiByb2J1c3QgZWxzZSBcIlN0YW5kYXJkIFNUTFwiXG4gICAgcHJpbnQoZlwie2xhYmVsOjIwc30gIHt0cmVuZF9ybXNlOjEyLjRmfSAge3NlYXNvbl9ybXNlOjEyLjRmfSAge3IucmVzaWQuc3RkKCk6MTAuNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTVNUTCBmb3IgTXVsdGlwbGUgU2Vhc29uYWwgUGVyaW9kcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSG91cmx5IGVsZWN0cmljaXR5IGRlbWFuZCBzaG93cyBib3RoIGEgZGFpbHkgY3ljbGUgKHBlcmlvZCAyNCkgYW5kIGEgd2Vla2x5IGN5Y2xlIChwZXJpb2QgMTY4KS4gTVNUTCAoTXVsdGlwbGUgU1RMKSBoYW5kbGVzIHRoaXMgYnkgaXRlcmF0aW5nOiBzdGFydGluZyB3aXRoIHRoZSBsb25nZXN0IHNlYXNvbmFsIHBlcmlvZCwgYXBwbHlpbmcgU1RMIGFuZCBrZWVwaW5nIGl0cyBzZWFzb25hbCBjb21wb25lbnQsIGRlc2Vhc29uYWxpc2luZywgdGhlbiByZXBlYXRpbmcgZm9yIHRoZSBuZXh0IHBlcmlvZC4gVGhlIGZpbmFsIGRlY29tcG9zaXRpb24gaGFzIG9uZSB0cmVuZCBjb21wb25lbnQgYW5kIG9uZSBzZWFzb25hbCBjb21wb25lbnQgcGVyIHNwZWNpZmllZCBwZXJpb2QuIFRoaXMgaXMgYXZhaWxhYmxlIGluIHRoZSBzdGF0c2ZvcmVjYXN0IGxpYnJhcnkgKE5peHRsYSkgYW5kIGNhbiBhbHNvIGJlIGFwcHJveGltYXRlZCBieSBzZXF1ZW50aWFsIFNUTCBjYWxscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zZWFzb25hbCBpbXBvcnQgU1RMXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubiA9IDMzNiAgIyAyIHdlZWtzIG9mIGhvdXJseSBkYXRhXG50ID0gbnAuYXJhbmdlKG4pXG5cbiMgSG91cmx5IGRhdGE6IGRhaWx5ICgyNGgpICsgd2Vla2x5ICgxNjhoKSBzZWFzb25hbGl0eVxuc2Vhc29uX2RhaWx5ICA9IDUuMCAqIG5wLnNpbigyICogbnAucGkgKiB0IC8gMjQpXG5zZWFzb25fd2Vla2x5ID0gMy4wICogbnAuc2luKDIgKiBucC5waSAqIHQgLyAxNjgpXG50cmVuZF9jb21wICAgID0gMjAgKyAwLjAyICogdFxueSA9IHRyZW5kX2NvbXAgKyBzZWFzb25fZGFpbHkgKyBzZWFzb25fd2Vla2x5ICsgbnAucmFuZG9tLnJhbmRuKG4pXG5cbiMgU2VxdWVudGlhbCBTVEwgYXBwcm94aW1hdGlvbjogcmVtb3ZlIHdlZWtseSBmaXJzdCwgdGhlbiBkYWlseVxuc3RsX3dlZWtseSA9IFNUTCh5LCBwZXJpb2Q9MTY4LCBzZWFzb25hbD0xMywgcm9idXN0PVRydWUpXG5yX3dlZWtseSA9IHN0bF93ZWVrbHkuZml0KClcbnlfZGV3ZWVrbHkgPSB5IC0gcl93ZWVrbHkuc2Vhc29uYWxcblxuc3RsX2RhaWx5ID0gU1RMKHlfZGV3ZWVrbHksIHBlcmlvZD0yNCwgc2Vhc29uYWw9Nywgcm9idXN0PVRydWUpXG5yX2RhaWx5ID0gc3RsX2RhaWx5LmZpdCgpXG5cbnJlc2lkX2NvbWJpbmVkID0geSAtIHJfd2Vla2x5LnNlYXNvbmFsIC0gcl9kYWlseS5zZWFzb25hbCAtIHJfZGFpbHkudHJlbmRcbnByaW50KGZcIldlZWtseSBzZWFzb25hbCByYW5nZTogW3tyX3dlZWtseS5zZWFzb25hbC5taW4oKTouMmZ9LCB7cl93ZWVrbHkuc2Vhc29uYWwubWF4KCk6LjJmfV1cIilcbnByaW50KGZcIkRhaWx5ICBzZWFzb25hbCByYW5nZTogW3tyX2RhaWx5LnNlYXNvbmFsLm1pbigpOi4yZn0sICB7cl9kYWlseS5zZWFzb25hbC5tYXgoKTouMmZ9XVwiKVxucHJpbnQoZlwiQ29tYmluZWQgcmVzaWR1YWwgc3RkOiB7cmVzaWRfY29tYmluZWQuc3RkKCk6LjRmfVwiKVxucHJpbnQoZlwiVHJ1ZSBub2lzZSBzdGQ6ICAgICAgICAxLjAwMDAgIChyZXNpZHVhbCBzaG91bGQgYmUgY2xvc2UgdG8gMSlcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTVEwgUGFyYW1ldGVycyBSZWZlcmVuY2UifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUGFyYW1ldGVyIiwiRGVzY3JpcHRpb24iLCJFZmZlY3Qgb2YgSW5jcmVhc2luZyIsIlR5cGljYWwgVmFsdWVzIl0sInJvd3MiOltbInBlcmlvZCIsIkxlbmd0aCBvZiBzZWFzb25hbCBjeWNsZSAoUCkiLCJOL0Eg4oCUIG11c3QgbWF0Y2ggZGF0YSBmcmVxdWVuY3kiLCIxMiAobW9udGhseSksIDUyICh3ZWVrbHkpLCAyNCAoaG91cmx5KSJdLFsic2Vhc29uYWwgKG7igpspIiwiTE9FU1Mgd2luZG93IGZvciBzZWFzb25hbCBzdWItc2VyaWVzIiwiU21vb3RoZXIgc2Vhc29uYWwg4oCUIGxlc3MgeWVhci10by15ZWFyIHZhcmlhdGlvbiIsIk9kZCwg4omlIDc7IHRyeSA3LCAxMSwgMTMsIDE1Il0sWyJ0cmVuZCAobuKCnCkiLCJMT0VTUyB3aW5kb3cgZm9yIHRyZW5kIHNtb290aGVyIiwiU21vb3RoZXIgdHJlbmQg4oCUIHNsb3dlciBhZGFwdGF0aW9uIiwiT2RkLCDiiaUgUDsgcnVsZSBvZiB0aHVtYjogY2VpbCgxLjXCt1AvKDHiiJIxLjUvbuKCmykpIl0sWyJyb2J1c3QiLCJCb29sZWFuOiB1c2UgYmlzcXVhcmUgb3V0ZXItbG9vcCB3ZWlnaHRzIiwiTi9BIOKAlCBib29sZWFuIGZsYWciLCJUcnVlIHdoZW4gc2VyaWVzIGhhcyBvdXRsaWVycyBvciBpcnJlZ3VsYXIgc2hvY2tzIl0sWyJsb3dfcGFzcyAobuKClykiLCJMb3ctcGFzcyBmaWx0ZXIgd2luZG93IGZvciBzZWFzb25hbCBzdGVwIiwiU21vb3RoZXIgc2Vhc29uYWwgZXh0cmFjdGlvbiIsIlNtYWxsZXN0IG9kZCBpbnRlZ2VyIFx1MDAzZSBQIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXNpZHVhbCBBbmFseXNpcyBhbmQgRGlhZ25vc3RpY3MifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zZWFzb25hbCBpbXBvcnQgU1RMXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0dG9vbHMgaW1wb3J0IGFjZlxuZnJvbSBzdGF0c21vZGVscy5zdGF0cy5kaWFnbm9zdGljIGltcG9ydCBhY29ycl9sanVuZ2JveFxuXG5ucC5yYW5kb20uc2VlZCg5KVxubiA9IDEyMFxudCA9IG5wLmFyYW5nZShuKVxueSA9IDYwICsgMC40KnQgKyAxMipucC5zaW4oMipucC5waSp0LzEyKSArIDIuNSpucC5yYW5kb20ucmFuZG4obilcblxuc3RsID0gU1RMKHksIHBlcmlvZD0xMiwgc2Vhc29uYWw9MTEsIHJvYnVzdD1UcnVlKVxucmVzdWx0ID0gc3RsLmZpdCgpXG5yZXNpZCA9IHJlc3VsdC5yZXNpZFxuXG5hY2ZfciA9IGFjZihyZXNpZCwgbmxhZ3M9MjQsIGFscGhhPTAuMDUpXG5wcmludChcIlJlc2lkdWFsIEFDRiBhdCBrZXkgbGFncyAoc2hvdWxkIGJlIG5lYXIgemVybyk6XCIpXG5mb3IgbGFnIGluIFsxLCA2LCAxMiwgMjRdOlxuICAgIHByaW50KGZcIiAgbGFnIHtsYWc6MmR9OiBBQ0Y9e2FjZl9yWzBdW2xhZ106LjRmfSAgOTUlQ0k9W3thY2ZfclsxXVtsYWddWzBdOi4zZn0sIHthY2ZfclsxXVtsYWddWzFdOi4zZn1dXCIpXG5cbmxiID0gYWNvcnJfbGp1bmdib3gocmVzaWQsIGxhZ3M9WzEyLCAyNF0sIHJldHVybl9kZj1UcnVlKVxucHJpbnQoXCJcXG5ManVuZy1Cb3ggdGVzdDpcIilcbnByaW50KGxiW1tcdTAwMjdsYl9zdGF0XHUwMDI3LCBcdTAwMjdsYl9wdmFsdWVcdTAwMjddXS50b19zdHJpbmcoKSlcblxuc3RyZW5ndGhfcyA9IG1heCgwLCAxIC0gcmVzaWQudmFyKCkgLyAocmVzdWx0LnNlYXNvbmFsICsgcmVzaWQpLnZhcigpKVxuc3RyZW5ndGhfdCA9IG1heCgwLCAxIC0gcmVzaWQudmFyKCkgLyAocmVzdWx0LnRyZW5kICAgKyByZXNpZCkudmFyKCkpXG5wcmludChmXCJcXG5TZWFzb25hbCBzdHJlbmd0aDoge3N0cmVuZ3RoX3M6LjRmfSAgKFx1MDAzZTAuNiA9IHN0cm9uZyBzZWFzb25hbGl0eSlcIilcbnByaW50KGZcIlRyZW5kIHN0cmVuZ3RoOiAgICB7c3RyZW5ndGhfdDouNGZ9ICAoXHUwMDNlMC42ID0gc3Ryb25nIHRyZW5kKVwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJTZWFzb25hbCBTdHJlbmd0aCBNZXRyaWMiLCJjb250ZW50IjoiVGhlIHNlYXNvbmFsIHN0cmVuZ3RoIEZzID0gbWF4KDAsIDEg4oiSIFZhcihS4oKcKS9WYXIoU+KCnCArIFLigpwpKSBtZWFzdXJlcyBob3cgbXVjaCBvZiB0aGUgc2Vhc29uYWwrcmVzaWR1YWwgdmFyaWFuY2UgaXMgZXhwbGFpbmVkIGJ5IHRoZSBzZWFzb25hbCBjb21wb25lbnQuIFZhbHVlcyBhYm92ZSAwLjYgaW5kaWNhdGUgc3Ryb25nLCBmb3JlY2FzdGFibGUgc2Vhc29uYWxpdHkuIFRoZSBjb3JyZXNwb25kaW5nIHRyZW5kIHN0cmVuZ3RoIEZ0ID0gbWF4KDAsIDEg4oiSIFZhcihS4oKcKS9WYXIoVOKCnCArIFLigpwpKSBzaW1pbGFybHkgcXVhbnRpZmllcyB0aGUgdHJlbmQuIEJvdGggbWV0cmljcyBhcmUgdXNlZCBpbiB0aGUgVGhldGEgbWV0aG9kIGFuZCBNNC9NNSBjb21wZXRpdGlvbiBmZWF0dXJlIGVuZ2luZWVyaW5nIHBpcGVsaW5lcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTVEwgdnMgQ2xhc3NpY2FsIERlY29tcG9zaXRpb24ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNUTCB3b3JrcyBmb3IgYW55IHNlYXNvbmFsIHBlcmlvZCBQOyBjbGFzc2ljYWwgcmVxdWlyZXMgUCB0byBkaXZpZGUgZXZlbmx5IGludG8gdGhlIHNlcmllcyBsZW5ndGguIiwiU1RMIGFsbG93cyB0aGUgc2Vhc29uYWwgY29tcG9uZW50IHRvIGNoYW5nZSBzbG93bHkgb3ZlciB0aW1lOyBjbGFzc2ljYWwgdXNlcyBmaXhlZCBzZWFzb25hbCBmYWN0b3JzLiIsIlJvYnVzdCBTVEwgZG93bi13ZWlnaHRzIG91dGxpZXJzOyBjbGFzc2ljYWwgZGVjb21wb3NpdGlvbiBoYXMgbm8gb3V0bGllciBwcm90ZWN0aW9uLiIsIkNsYXNzaWNhbCBkZWNvbXBvc2l0aW9uIGxvc2VzIFAvMiBvYnNlcnZhdGlvbnMgYXQgZWFjaCBlbmQgKGJvcmRlciBlZmZlY3QpOyBTVEwgdXNlcyBMT0VTUyB3aGljaCBhbHNvIHN0cnVnZ2xlcyBhdCBib3VuZGFyaWVzIGJ1dCBsZXNzIHNldmVyZWx5LiIsIlNUTCBpcyBhZGRpdGl2ZSBvbmx5OyBhcHBseSBsb2cgdHJhbnNmb3JtIGJlZm9yZSBTVEwgZm9yIG11bHRpcGxpY2F0aXZlIHNlcmllcy4iLCJTVEwgaXMgY29tcHV0YXRpb25hbGx5IG1vcmUgZXhwZW5zaXZlIHRoYW4gY2xhc3NpY2FsIGRlY29tcG9zaXRpb24gYnV0IHN0aWxsIHZlcnkgZmFzdCBpbiBwcmFjdGljZS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# STL Decomposition — Seasonal-Trend via LOESS

STL (Seasonal-Trend decomposition using LOESS) overcomes three critical limitations of classical decomposition: it handles any seasonal period (not just integer multiples of 12), it can use a robust option that down-weights outliers, and it allows the seasonal component to evolve slowly over time. Published by Cleveland et al. (1990), STL remains the gold standard for exploratory decomposition and is the backbone of several production forecasting frameworks including Facebook Prophet and the Nixtla stack.

## LOESS — Locally Estimated Scatterplot Smoothing

LOESS fits a weighted local polynomial regression at each point xₜ. Observations closer to xₜ receive higher weights (typically using a tricubic kernel). The bandwidth parameter controls the fraction of data used in each local fit: smaller bandwidth gives more flexible, wiggly smoothing; larger bandwidth gives smoother, more global estimates. STL uses LOESS as a building block for both the seasonal and trend smoothers, with separate bandwidth parameters for each component.

## STL Algorithm — Inner and Outer Loops

STL alternates between an inner loop and an outer loop. The inner loop iterates several times, updating seasonal and trend estimates: (1) detrend the series (subtract current trend estimate), (2) smooth each seasonal sub-series (all January values, all February values, etc.) with a LOESS of window nₛ to get a raw seasonal estimate, (3) apply a low-pass filter (MA then LOESS) to remove low-frequency contamination from the seasonal estimate, (4) subtract the seasonal estimate and smooth the deseasonalised series with LOESS of window nₜ to update the trend. The outer loop computes robustness weights based on residual magnitude (bisquare weights), reducing the influence of outliers in subsequent inner loop iterations.

1. Outer loop initialises: trend = 0, seasonal = 0, robustness weights = 1.
2. Inner loop (repeated n_inner times): update seasonal via LOESS on sub-series, apply low-pass filter, update trend via LOESS on deseasonalised data.
3. Outer loop (if robust=True): compute residuals, assign bisquare robustness weights, repeat inner loop with weighted LOESS.
4. Final decomposition: Tₜ (trend), Sₜ (seasonal), Rₜ = yₜ − Tₜ − Sₜ (remainder).
5. The seasonal component sum over one period ≈ 0 but is not forced to be exactly zero — it can drift slowly.

## Running STL with statsmodels

```python
import numpy as np
from statsmodels.tsa.seasonal import STL

np.random.seed(0)
n = 156  # 3 years of weekly data
t = np.arange(n)

# Construct series: trend + weekly season + noise
trend_true = 100 + 0.5 * t
season = 15 * np.sin(2 * np.pi * t / 52)
y = trend_true + season + 3 * np.random.randn(n)

# Fit STL with period=52 (weekly with yearly seasonality)
stl = STL(y, period=52, seasonal=13, trend=None, robust=True)
result = stl.fit()

# Inspect components
valid = ~np.isnan(result.trend)
print(f"Trend  range: [{result.trend[valid].min():.1f}, {result.trend[valid].max():.1f}]")
print(f"Seasonal range: [{result.seasonal.min():.2f}, {result.seasonal.max():.2f}]")
print(f"Resid  std:  {result.resid.std():.4f}")
print(f"Seasonal strength: {max(0, 1 - result.resid.var() / (result.seasonal + result.resid).var()):.4f}")
print(f"Trend strength:    {max(0, 1 - result.resid.var() / (result.trend + result.resid).var()):.4f}")
```

## Robust STL — Handling Outliers

In non-robust STL all residuals have equal weight. If the series contains outliers (data entry errors, strikes, natural disasters), they pull the LOESS smoother and contaminate the seasonal and trend estimates. Robust STL adds an outer loop that computes bisquare weights: wₜ = (1 − (|Rₜ|/(6·median(|R|)))²)² for |Rₜ| < 6·median(|R|), and 0 otherwise. Observations with very large residuals receive near-zero weights and have negligible influence on subsequent LOESS fits.

```python
import numpy as np
from statsmodels.tsa.seasonal import STL

np.random.seed(5)
n = 120
t = np.arange(n)
y_clean = 50 + 0.3*t + 10*np.sin(2*np.pi*t/12) + 2*np.random.randn(n)

# Inject outliers at a few positions
y_dirty = y_clean.copy()
outlier_idx = [30, 60, 90]
for idx in outlier_idx:
    y_dirty[idx] += 60  # large positive spike

print(f"{'Method':20s}  {'Trend RMSE':12s}  {'Season RMSE':12s}  {'Resid std':10s}")
print("-" * 60)

true_trend  = 50 + 0.3*t
true_season = 10*np.sin(2*np.pi*t/12)

for robust in [False, True]:
    stl = STL(y_dirty, period=12, seasonal=7, robust=robust)
    r = stl.fit()
    trend_rmse  = np.sqrt(np.mean((r.trend  - true_trend)**2))
    season_rmse = np.sqrt(np.mean((r.seasonal - true_season)**2))
    label = "Robust STL" if robust else "Standard STL"
    print(f"{label:20s}  {trend_rmse:12.4f}  {season_rmse:12.4f}  {r.resid.std():10.4f}")
```

## MSTL for Multiple Seasonal Periods

Hourly electricity demand shows both a daily cycle (period 24) and a weekly cycle (period 168). MSTL (Multiple STL) handles this by iterating: starting with the longest seasonal period, applying STL and keeping its seasonal component, deseasonalising, then repeating for the next period. The final decomposition has one trend component and one seasonal component per specified period. This is available in the statsforecast library (Nixtla) and can also be approximated by sequential STL calls.

```python
import numpy as np
from statsmodels.tsa.seasonal import STL

np.random.seed(42)
n = 336  # 2 weeks of hourly data
t = np.arange(n)

# Hourly data: daily (24h) + weekly (168h) seasonality
season_daily  = 5.0 * np.sin(2 * np.pi * t / 24)
season_weekly = 3.0 * np.sin(2 * np.pi * t / 168)
trend_comp    = 20 + 0.02 * t
y = trend_comp + season_daily + season_weekly + np.random.randn(n)

# Sequential STL approximation: remove weekly first, then daily
stl_weekly = STL(y, period=168, seasonal=13, robust=True)
r_weekly = stl_weekly.fit()
y_deweekly = y - r_weekly.seasonal

stl_daily = STL(y_deweekly, period=24, seasonal=7, robust=True)
r_daily = stl_daily.fit()

resid_combined = y - r_weekly.seasonal - r_daily.seasonal - r_daily.trend
print(f"Weekly seasonal range: [{r_weekly.seasonal.min():.2f}, {r_weekly.seasonal.max():.2f}]")
print(f"Daily  seasonal range: [{r_daily.seasonal.min():.2f},  {r_daily.seasonal.max():.2f}]")
print(f"Combined residual std: {resid_combined.std():.4f}")
print(f"True noise std:        1.0000  (residual should be close to 1)")
```

## STL Parameters Reference

| Parameter | Description | Effect of Increasing | Typical Values |
| --- | --- | --- | --- |
| period | Length of seasonal cycle (P) | N/A — must match data frequency | 12 (monthly), 52 (weekly), 24 (hourly) |
| seasonal (nₛ) | LOESS window for seasonal sub-series | Smoother seasonal — less year-to-year variation | Odd, ≥ 7; try 7, 11, 13, 15 |
| trend (nₜ) | LOESS window for trend smoother | Smoother trend — slower adaptation | Odd, ≥ P; rule of thumb: ceil(1.5·P/(1−1.5/nₛ)) |
| robust | Boolean: use bisquare outer-loop weights | N/A — boolean flag | True when series has outliers or irregular shocks |
| low_pass (nₗ) | Low-pass filter window for seasonal step | Smoother seasonal extraction | Smallest odd integer > P |

## Residual Analysis and Diagnostics

```python
import numpy as np
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import acf
from statsmodels.stats.diagnostic import acorr_ljungbox

np.random.seed(9)
n = 120
t = np.arange(n)
y = 60 + 0.4*t + 12*np.sin(2*np.pi*t/12) + 2.5*np.random.randn(n)

stl = STL(y, period=12, seasonal=11, robust=True)
result = stl.fit()
resid = result.resid

acf_r = acf(resid, nlags=24, alpha=0.05)
print("Residual ACF at key lags (should be near zero):")
for lag in [1, 6, 12, 24]:
    print(f"  lag {lag:2d}: ACF={acf_r[0][lag]:.4f}  95%CI=[{acf_r[1][lag][0]:.3f}, {acf_r[1][lag][1]:.3f}]")

lb = acorr_ljungbox(resid, lags=[12, 24], return_df=True)
print("\nLjung-Box test:")
print(lb[['lb_stat', 'lb_pvalue']].to_string())

strength_s = max(0, 1 - resid.var() / (result.seasonal + resid).var())
strength_t = max(0, 1 - resid.var() / (result.trend   + resid).var())
print(f"\nSeasonal strength: {strength_s:.4f}  (>0.6 = strong seasonality)")
print(f"Trend strength:    {strength_t:.4f}  (>0.6 = strong trend)")
```

> **Seasonal Strength Metric**: The seasonal strength Fs = max(0, 1 − Var(Rₜ)/Var(Sₜ + Rₜ)) measures how much of the seasonal+residual variance is explained by the seasonal component. Values above 0.6 indicate strong, forecastable seasonality. The corresponding trend strength Ft = max(0, 1 − Var(Rₜ)/Var(Tₜ + Rₜ)) similarly quantifies the trend. Both metrics are used in the Theta method and M4/M5 competition feature engineering pipelines.

## STL vs Classical Decomposition

- STL works for any seasonal period P; classical requires P to divide evenly into the series length.
- STL allows the seasonal component to change slowly over time; classical uses fixed seasonal factors.
- Robust STL down-weights outliers; classical decomposition has no outlier protection.
- Classical decomposition loses P/2 observations at each end (border effect); STL uses LOESS which also struggles at boundaries but less severely.
- STL is additive only; apply log transform before STL for multiplicative series.
- STL is computationally more expensive than classical decomposition but still very fast in practice.

---

