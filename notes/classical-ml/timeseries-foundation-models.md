---
title: "Time-Series Foundation Models — TimesFM, Chronos, Moirai"
slug: "timeseries-foundation-models"
description: "Survey time-series foundation models: TimesFM decoder-only patched Transformer, Chronos tokenized probabilistic forecasting, and Moirai unified multi-variate model. Compare zero-shot performance vs task-specific models and fine-tuning strategies."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGltZS1zZXJpZXMgZm91bmRhdGlvbiBtb2RlbHMgdHJhaW4gb24gbWFzc2l2ZSwgZGl2ZXJzZSBkYXRhc2V0cyBhbmQgZ2VuZXJhbGlzZSB6ZXJvLXNob3QgdG8gbmV3IHRpbWUgc2VyaWVzIHdpdGhvdXQgdGFzay1zcGVjaWZpYyByZXRyYWluaW5nLiBNb3RpdmF0ZWQgYnkgdGhlIHN1Y2Nlc3Mgb2YgTExNcywgdGhleSBhZGRyZXNzIGEga2V5IGxpbWl0YXRpb24gb2YgY2xhc3NpY2FsIG1vZGVsczogZWFjaCBuZXcgZGF0YXNldCByZXF1aXJlcyBmaXR0aW5nIGEgZnJlc2ggbW9kZWwuIFRpbWVzRk0gKEdvb2dsZSksIENocm9ub3MgKEFtYXpvbiksIGFuZCBNb2lyYWkgKFNhbGVzZm9yY2UpIHJlcHJlc2VudCB0aHJlZSBkaXN0aW5jdCBhcmNoaXRlY3R1cmFsIHBoaWxvc29waGllcywgc3Bhbm5pbmcgZGVjb2Rlci1vbmx5IFRyYW5zZm9ybWVycywgbGFuZ3VhZ2UtbW9kZWwgdG9rZW5pemF0aW9uLCBhbmQgdW5pZmllZCBtdWx0aS12YXJpYXRlIGF0dGVudGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb3RpdmF0aW9uIOKAlCBUcmFpbiBPbmNlLCBGb3JlY2FzdCBFdmVyeXdoZXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFzc2ljYWwgbW9kZWxzIChBUklNQSwgRVRTLCBQcm9waGV0KSBtdXN0IGJlIGZpdCBwZXIgc2VyaWVzLCB3aGljaCBpcyBleHBlbnNpdmUgYXQgc2NhbGUuIFRhc2stc3BlY2lmaWMgZGVlcCBtb2RlbHMgKE5CRUFUUywgVEZUKSByZXF1aXJlIGEgdHJhaW5pbmcgZGF0YXNldCBvZiByZWxhdGVkIHNlcmllcy4gRm91bmRhdGlvbiBtb2RlbHMgc2lkZXN0ZXAgdGhpcyBieSBwcmV0cmFpbmluZyBvbiAxMDBCKyB0aW1lIHBvaW50cyBmcm9tIGRpdmVyc2UgZG9tYWlucyAoZW5lcmd5LCBmaW5hbmNlLCB3ZWF0aGVyLCB0cmFmZmljKSwgbGVhcm5pbmcgdW5pdmVyc2FsIHRlbXBvcmFsIHBhdHRlcm5zLiBBdCBpbmZlcmVuY2UsIHRoZXkgYWNjZXB0IGFueSBuZXcgc2VyaWVzIGFzIGNvbnRleHQgYW5kIHByb2R1Y2UgZm9yZWNhc3RzIHplcm8tc2hvdCwgc2ltaWxhciB0byBHUFQtNCBhbnN3ZXJpbmcgbmV3IHF1ZXN0aW9ucyB3aXRob3V0IGZpbmUtdHVuaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRpbWVzRk0g4oCUIERlY29kZXItT25seSBQYXRjaGVkIFRyYW5zZm9ybWVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaW1lc0ZNIChHb29nbGUgRGVlcE1pbmQsIDIwMjQpIGlzIGEgMjAwTS1wYXJhbWV0ZXIgZGVjb2Rlci1vbmx5IFRyYW5zZm9ybWVyLiBUaGUgaW5wdXQgc2VyaWVzIGlzIGRpdmlkZWQgaW50byBub24tb3ZlcmxhcHBpbmcgcGF0Y2hlcyBvZiBsZW5ndGggMzIgb3IgNjQuIEVhY2ggcGF0Y2ggaXMgcHJvamVjdGVkIHRvIGFuIGVtYmVkZGluZyBhbmQgcHJvY2Vzc2VkIGJ5IHRoZSBUcmFuc2Zvcm1lci4gUHJldHJhaW5pbmcgdXNlcyBtYXNrZWQgcGF0Y2ggcHJlZGljdGlvbiBvbiAxMDBCIHRpbWUgcG9pbnRzIGZyb20gR29vZ2xlLWludGVybmFsIGFuZCBwdWJsaWMgZGF0YXNldHMuIFRoZSBtb2RlbCBvdXRwdXRzIHBvaW50IGZvcmVjYXN0cyBhbmQgb3B0aW9uYWxseSBxdWFudGlsZSBmb3JlY2FzdHMuIEl0IGFjaGlldmVzIHN0cm9uZyB6ZXJvLXNob3QgcGVyZm9ybWFuY2Ugb24gTW9uYXNoIGFuZCBHSUZULUV2YWwgYmVuY2htYXJrcywgb2Z0ZW4gY29tcGV0aXRpdmUgd2l0aCB0YXNrLXNwZWNpZmljIG1vZGVscyB0cmFpbmVkIG9uIGluLWRvbWFpbiBkYXRhLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIHBpcCBpbnN0YWxsIHRpbWVzZm1cbmltcG9ydCBudW1weSBhcyBucFxuXG50cnk6XG4gICAgaW1wb3J0IHRpbWVzZm1cbiAgICB0Zm0gPSB0aW1lc2ZtLlRpbWVzRm0oXG4gICAgICAgIGhwYXJhbXM9dGltZXNmbS5UaW1lc0ZtSHBhcmFtcyhcbiAgICAgICAgICAgIGJhY2tlbmQ9XHUwMDI3Y3B1XHUwMDI3LFxuICAgICAgICAgICAgcGVyX2NvcmVfYmF0Y2hfc2l6ZT0zMixcbiAgICAgICAgICAgIGhvcml6b25fbGVuPTI0LFxuICAgICAgICApLFxuICAgICAgICBjaGVja3BvaW50PXRpbWVzZm0uVGltZXNGbUNoZWNrcG9pbnQoXG4gICAgICAgICAgICBodWdnaW5nZmFjZV9yZXBvX2lkPVx1MDAyN2dvb2dsZS90aW1lc2ZtLTEuMC0yMDBtLXB5dG9yY2hcdTAwMjdcbiAgICAgICAgKSxcbiAgICApXG4gICAgbnAucmFuZG9tLnNlZWQoMClcbiAgICBjb250ZXh0ID0gW25wLmN1bXN1bShucC5yYW5kb20ucmFuZG4oOTYpKSArIDEwMC4wIGZvciBfIGluIHJhbmdlKDQpXVxuICAgIGZyZXEgPSBbMF0gKiA0ICAgIyAwPWhpZ2hfZnJlcSwgMT1tZWRpdW0sIDI9bG93XG4gICAgcG9pbnRfZmMsIHF1YW50aWxlX2ZjID0gdGZtLmZvcmVjYXN0KGlucHV0cz1jb250ZXh0LCBmcmVxPWZyZXEpXG4gICAgcHJpbnQoZlx1MDAyN1BvaW50IGZvcmVjYXN0IHNoYXBlOiAgICB7cG9pbnRfZmMuc2hhcGV9XHUwMDI3KSAgICAgIyAoYmF0Y2gsIGhvcml6b24pXG4gICAgcHJpbnQoZlx1MDAyN1F1YW50aWxlIGZvcmVjYXN0IHNoYXBlOiB7cXVhbnRpbGVfZmMuc2hhcGV9XHUwMDI3KSAgIyAoYmF0Y2gsIGhvcml6b24sIG5fcXVhbnRpbGVzKVxuICAgIHByaW50KGZcdTAwMjdNZWFuIDI0LXN0ZXAgYWhlYWQ6IHtwb2ludF9mY1swXS5tZWFuKCk6LjNmfVx1MDAyNylcbmV4Y2VwdCBJbXBvcnRFcnJvcjpcbiAgICBwcmludChcdTAwMjdUaW1lc0ZNIEFQSSBzdW1tYXJ5Olx1MDAyNylcbiAgICBwcmludChcdTAwMjcgIElucHV0OiBMaXN0W25wLm5kYXJyYXldLCBlYWNoIHNoYXBlIChjb250ZXh0X2xlbiwpXHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgZnJlcTogIExpc3RbaW50XSAgLS0gMD1oaWdoLCAxPW1lZGl1bSwgMj1sb3cgZnJlcXVlbmN5XHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgT3V0cHV0OiBwb2ludF9mb3JlY2FzdCAoYmF0Y2gsIGhvcml6b24pXHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgUGF0Y2ggbGVuZ3RoOiAzMiBvciA2NCB0aW1lIHN0ZXBzXHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgUHJldHJhaW5pbmc6IG1hc2tlZCBwYXRjaCBwcmVkaWN0aW9uIG9uIDEwMEIrIHRpbWUgcG9pbnRzXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNocm9ub3Mg4oCUIFRva2VuaXplZCBQcm9iYWJpbGlzdGljIEZvcmVjYXN0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDaHJvbm9zIChBbWF6b24sIDIwMjQpIGFkYXB0cyBhIFQ1IGxhbmd1YWdlIG1vZGVsIChlbmNvZGVyLWRlY29kZXIpIHRvIHRpbWUgc2VyaWVzIGJ5IHF1YW50aXppbmcgY29udGludW91cyB2YWx1ZXMgaW50byBkaXNjcmV0ZSB0b2tlbnMgdmlhIHVuaWZvcm0gYmlubmluZy4gRWFjaCBiaW4gaXMgYSB2b2NhYnVsYXJ5IHRva2VuOyB0aGUgbW9kZWwgaXMgdHJhaW5lZCB0byBwcmVkaWN0IHRoZSBuZXh0IHRva2VuIGRpc3RyaWJ1dGlvbi4gQXQgaW5mZXJlbmNlLCBtdWx0aXBsZSBzYW1wbGUgdHJhamVjdG9yaWVzIGFyZSBkcmF3biBmcm9tIHRoZSBwcmVkaWN0ZWQgZGlzdHJpYnV0aW9ucywgeWllbGRpbmcgYSBwcm9iYWJpbGlzdGljIGZvcmVjYXN0LiBDaHJvbm9zIHJlcXVpcmVzIG5vIGZyZXF1ZW5jeSBpbmZvcm1hdGlvbiBvciBzY2FsaW5nIGhldXJpc3RpY3Mg4oCUIGl0IG5vcm1hbGl6ZXMgZWFjaCBzZXJpZXMgYnkgaXRzIG1lYW4gYmVmb3JlIHRva2VuaXphdGlvbi4gSXQgZXhjZWxzIGF0IHVuY2VydGFpbnR5IHF1YW50aWZpY2F0aW9uIGFuZCBoYW5kbGVzIGlycmVndWxhciBzYW1wbGluZyBuYXR1cmFsbHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6IiMgcGlwIGluc3RhbGwgY2hyb25vcy1mb3JlY2FzdGluZ1xuaW1wb3J0IG51bXB5IGFzIG5wXG5cbnRyeTpcbiAgICBpbXBvcnQgdG9yY2hcbiAgICBmcm9tIGNocm9ub3MgaW1wb3J0IENocm9ub3NQaXBlbGluZVxuXG4gICAgcGlwZWxpbmUgPSBDaHJvbm9zUGlwZWxpbmUuZnJvbV9wcmV0cmFpbmVkKFxuICAgICAgICBcdTAwMjdhbWF6b24vY2hyb25vcy10NS1zbWFsbFx1MDAyNyxcbiAgICAgICAgZGV2aWNlX21hcD1cdTAwMjdjcHVcdTAwMjcsXG4gICAgICAgIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MzIsXG4gICAgKVxuICAgIG5wLnJhbmRvbS5zZWVkKDQyKVxuICAgIGNvbnRleHQgPSB0b3JjaC50ZW5zb3IoXG4gICAgICAgIG5wLmN1bXN1bShucC5yYW5kb20ucmFuZG4oMTIwKSkgKyA1MC4wLCBkdHlwZT10b3JjaC5mbG9hdDMyXG4gICAgKS51bnNxdWVlemUoMCkgICMgc2hhcGUgKDEsIGNvbnRleHRfbGVuKVxuXG4gICAgZm9yZWNhc3QgPSBwaXBlbGluZS5wcmVkaWN0KGNvbnRleHQsIHByZWRpY3Rpb25fbGVuZ3RoPTI0LCBudW1fc2FtcGxlcz0xMDApXG4gICAgbG93ICAgID0gbnAucXVhbnRpbGUoZm9yZWNhc3RbMF0ubnVtcHkoKSwgMC4xLCBheGlzPTApXG4gICAgbWVkaWFuID0gbnAucXVhbnRpbGUoZm9yZWNhc3RbMF0ubnVtcHkoKSwgMC41LCBheGlzPTApXG4gICAgaGlnaCAgID0gbnAucXVhbnRpbGUoZm9yZWNhc3RbMF0ubnVtcHkoKSwgMC45LCBheGlzPTApXG4gICAgcHJpbnQoZlx1MDAyN0ZvcmVjYXN0IHNhbXBsZXMgc2hhcGU6IHtmb3JlY2FzdFswXS5zaGFwZX1cdTAwMjcpICAjIChudW1fc2FtcGxlcywgaG9yaXpvbilcbiAgICBwcmludChmXHUwMDI3TWVkaWFuIGZvcmVjYXN0IChmaXJzdCA0KToge21lZGlhbls6NF0ucm91bmQoMil9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjc4MCUgUEkgd2lkdGggKG1lYW4pOiB7KGhpZ2ggLSBsb3cpLm1lYW4oKTouM2Z9XHUwMDI3KVxuZXhjZXB0IEltcG9ydEVycm9yOlxuICAgIHByaW50KFx1MDAyN0Nocm9ub3MgQVBJOiBDaHJvbm9zUGlwZWxpbmUuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUpXHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgcGlwZWxpbmUucHJlZGljdChjb250ZXh0X3RlbnNvciwgcHJlZGljdGlvbl9sZW5ndGg9SCwgbnVtX3NhbXBsZXM9TilcdTAwMjcpXG4gICAgcHJpbnQoXHUwMDI3ICBSZXR1cm5zOiB0ZW5zb3IgKGJhdGNoLCBudW1fc2FtcGxlcywgaG9yaXpvbikgZm9yIHByb2JhYmlsaXN0aWMgb3V0cHV0XHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgTW9kZWxzOiBjaHJvbm9zLXQ1LXRpbnkgKDhNKSwgc21hbGwgKDQ2TSksIGJhc2UgKDIwME0pLCBsYXJnZSAoNzEwTSlcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9pcmFpIOKAlCBVbmlmaWVkIE11bHRpLVZhcmlhdGUgRm9yZWNhc3RpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1vaXJhaSAoU2FsZXNmb3JjZSwgMjAyNCkgaXMgYW4gZW5jb2Rlci1vbmx5IFRyYW5zZm9ybWVyIHRyYWluZWQgb24gdGhlIExPVFNBIGRhdGFzZXQgKDI3QiBvYnNlcnZhdGlvbnMgYWNyb3NzIDkgZG9tYWlucykuIEl0IGludHJvZHVjZXMgYW55LXZhcmlhdGUgYXR0ZW50aW9uOiBhIHNpbmdsZSBtb2RlbCBoYW5kbGVzIGJvdGggdW5pdmFyaWF0ZSBhbmQgbXVsdGktdmFyaWF0ZSBzZXJpZXMgYnkgYXR0ZW5kaW5nIGFjcm9zcyBhbGwgdmFyaWF0ZXMgc2ltdWx0YW5lb3VzbHkuIEtleSBpbm5vdmF0aW9uczogZnJlcXVlbmN5LWF3YXJlIHRva2VuaXphdGlvbiAoZnJlcXVlbmN5IHRva2VuIHByZXBlbmRlZCksIG11bHRpcGxlIHBhdGNoIHNpemVzIHJlc29sdmVkIGR5bmFtaWNhbGx5LCBhbmQgbGFnLWJhc2VkIGZlYXR1cmUgYXVnbWVudGF0aW9uLiBNb2lyYWkgYWNoaWV2ZXMgc3Ryb25nIHplcm8tc2hvdCBwZXJmb3JtYW5jZSBhbmQgY2FuIGJlIGZpbmUtdHVuZWQgZWZmaWNpZW50bHkgd2l0aCBMb1JBIGFkYXB0ZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiIjIHBpcCBpbnN0YWxsIHVuaTJ0c1xuaW1wb3J0IG51bXB5IGFzIG5wXG5cbnRyeTpcbiAgICBpbXBvcnQgdG9yY2hcbiAgICBmcm9tIGVpbm9wcyBpbXBvcnQgcmVhcnJhbmdlXG4gICAgZnJvbSB1bmkydHMubW9kZWwubW9pcmFpIGltcG9ydCBNb2lyYWlGb3JlY2FzdCwgTW9pcmFpTW9kdWxlXG5cbiAgICBtb2RlbCA9IE1vaXJhaUZvcmVjYXN0KFxuICAgICAgICBtb2R1bGU9TW9pcmFpTW9kdWxlLmZyb21fcHJldHJhaW5lZChcdTAwMjdTYWxlc2ZvcmNlL21vaXJhaS0xLjAtUi1zbWFsbFx1MDAyNyksXG4gICAgICAgIHByZWRpY3Rpb25fbGVuZ3RoPTI0LFxuICAgICAgICBjb250ZXh0X2xlbmd0aD0yMDAsXG4gICAgICAgIHBhdGNoX3NpemU9MzIsXG4gICAgICAgIG51bV9zYW1wbGVzPTEwMCxcbiAgICAgICAgdGFyZ2V0X2RpbT0xLFxuICAgICAgICBmZWF0X2R5bmFtaWNfcmVhbF9kaW09MCxcbiAgICAgICAgcGFzdF9mZWF0X2R5bmFtaWNfcmVhbF9kaW09MCxcbiAgICApXG4gICAgbnAucmFuZG9tLnNlZWQoNylcbiAgICBwYXN0X3RhcmdldCA9IHRvcmNoLnJhbmRuKDEsIDIwMCwgMSkgICMgKGJhdGNoLCBjb250ZXh0X2xlbiwgdGFyZ2V0X2RpbSlcbiAgICBmb3JlY2FzdCA9IG1vZGVsKHBhc3RfdGFyZ2V0KSAgICAgICAgICAjIChiYXRjaCwgbnVtX3NhbXBsZXMsIGhvcml6b24sIHRhcmdldF9kaW0pXG4gICAgc2FtcGxlcyA9IGZvcmVjYXN0WzBdLm51bXB5KCkgICAgICAgICAjIChudW1fc2FtcGxlcywgaG9yaXpvbiwgMSlcbiAgICBwcmludChmXHUwMDI3Rm9yZWNhc3Qgc2hhcGU6IHtzYW1wbGVzLnNoYXBlfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3TWVkaWFuIChmaXJzdCA0IHN0ZXBzKToge25wLm1lZGlhbihzYW1wbGVzWzosIDo0LCAwXSwgYXhpcz0wKS5yb3VuZCgzKX1cdTAwMjcpXG5leGNlcHQgSW1wb3J0RXJyb3I6XG4gICAgcHJpbnQoXHUwMDI3TW9pcmFpIEFQSTogTW9pcmFpRm9yZWNhc3QobW9kdWxlLCBwcmVkaWN0aW9uX2xlbmd0aCwgY29udGV4dF9sZW5ndGgpXHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgU3VwcG9ydHM6IHVuaXZhcmlhdGUgYW5kIG11bHRpLXZhcmlhdGUgKHRhcmdldF9kaW0gXHUwMDNlIDEpXHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgcGF0Y2hfc2l6ZTogOCwgMTYsIG9yIDMyIChyZXNvbHZlZCBkeW5hbWljYWxseSBhdCBpbmZlcmVuY2UpXHUwMDI3KVxuICAgIHByaW50KFx1MDAyNyAgTE9UU0EgcHJldHJhaW5pbmc6IDI3QiBvYnNlcnZhdGlvbnMgYWNyb3NzIDkgZG9tYWluc1x1MDAyNylcbiAgICBwcmludChcdTAwMjcgIEZpbmUtdHVuaW5nOiBMb1JBIGFkYXB0ZXJzIG9uIHByZXRyYWluZWQgbW9kdWxlXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJlbmNobWFya2luZyBGb3VuZGF0aW9uIHZzIFRhc2stU3BlY2lmaWMgTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPbiBHSUZULUV2YWwgYW5kIE1vbmFzaCBiZW5jaG1hcmtzLCBmb3VuZGF0aW9uIG1vZGVscyBhY2hpZXZlIGNvbXBldGl0aXZlIHplcm8tc2hvdCBwZXJmb3JtYW5jZSwgb2Z0ZW4gc3VycGFzc2luZyBzdGF0aXN0aWNhbCBtb2RlbHMgKEVUUywgQVJJTUEpIGFuZCBtYXRjaGluZyBvciBiZWF0aW5nIHRhc2stc3BlY2lmaWMgZGVlcCBtb2RlbHMgb24gc2hvcnQtdG8tbWVkaXVtIGhvcml6b25zLiBIb3dldmVyLCB0YXNrLXNwZWNpZmljIG1vZGVscyBmaW5lLXR1bmVkIG9uIGluLWRvbWFpbiBkYXRhIHdpdGggc3VmZmljaWVudCB0cmFpbmluZyBkYXRhIHR5cGljYWxseSBvdXRwZXJmb3JtIGZvdW5kYXRpb24gbW9kZWxzLiBUaGUgY3Jvc3NvdmVyIHBvaW50IGRlcGVuZHMgb24gZGF0YXNldCBzaXplOiB3aXRoIGZld2VyIHRoYW4gfjUwMCB0cmFpbmluZyBzZXJpZXMsIGZvdW5kYXRpb24gbW9kZWxzIG9mdGVuIHdpbjsgd2l0aCBsYXJnZXIgaW4tZG9tYWluIGRhdGFzZXRzLCBmaW5lLXR1bmVkIG9yIHRhc2stc3BlY2lmaWMgbW9kZWxzIHdpbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBSaWRnZVxuXG5ucC5yYW5kb20uc2VlZCg0Milcbm5fc2VyaWVzLCBob3Jpem9uLCBjb250ZXh0X2xlbiA9IDIwLCAxMiwgNjBcblxuZGVmIGdlbmVyYXRlX3NlcmllcyhuLCBsZW5ndGgpOlxuICAgIHRyZW5kID0gbnAubGluc3BhY2UoMCwgMSwgbGVuZ3RoKVxuICAgIHNlYXNvbmFsID0gbnAuc2luKDIgKiBucC5waSAqIG5wLmFyYW5nZShsZW5ndGgpIC8gMTIpXG4gICAgcmV0dXJuIG5wLnN0YWNrKFt0cmVuZCArIHNlYXNvbmFsICsgMC4xICogbnAucmFuZG9tLnJhbmRuKGxlbmd0aCkgZm9yIF8gaW4gcmFuZ2UobildKVxuXG5zZXJpZXMgPSBnZW5lcmF0ZV9zZXJpZXMobl9zZXJpZXMsIGNvbnRleHRfbGVuICsgaG9yaXpvbilcbnRyYWluX2N0eCA9IHNlcmllc1s6LCA6Y29udGV4dF9sZW5dXG50ZXN0X3kgICAgPSBzZXJpZXNbOiwgY29udGV4dF9sZW46XVxuXG5kZWYgbmFpdmVfc2Vhc29uYWxfZm9yZWNhc3QoY3R4LCBoLCBwZXJpb2Q9MTIpOlxuICAgIHJldHVybiBucC5zdGFjayhbY3R4WzosIC1wZXJpb2Q6XSBmb3IgXyBpbiByYW5nZSgoaCAvLyBwZXJpb2QpICsgMSldLCBheGlzPTFcbiAgICAgICAgICAgICAgICAgICAgKS5yZXNoYXBlKGN0eC5zaGFwZVswXSwgLTEpWzosIDpoXVxuXG5kZWYgcmlkZ2VfZGlyZWN0X2ZvcmVjYXN0KGN0eCwgeSwgaCk6XG4gICAgcHJlZHMgPSBucC56ZXJvcygoY3R4LnNoYXBlWzBdLCBoKSlcbiAgICBmb3Igc3RlcCBpbiByYW5nZShoKTpcbiAgICAgICAgbW9kZWwgPSBSaWRnZShhbHBoYT0xLjApLmZpdChjdHhbOi0xXSwgeVs6LTEsIHN0ZXBdKVxuICAgICAgICBwcmVkc1stMSwgc3RlcF0gPSBtb2RlbC5wcmVkaWN0KGN0eFtbLTFdXSlbMF1cbiAgICByZXR1cm4gcHJlZHNcblxubmFpdmVfZmMgPSBuYWl2ZV9zZWFzb25hbF9mb3JlY2FzdCh0cmFpbl9jdHgsIGhvcml6b24pXG5wcmludChcdTAwMjdCZW5jaG1hcmsgKHNpbXVsYXRlZCwgbm8gcmVhbCBmb3VuZGF0aW9uIG1vZGVsIGNhbGwpOlx1MDAyNylcbnByaW50KGZcdTAwMjdOYWl2ZSBzZWFzb25hbCBNQUU6IHtucC5hYnMobmFpdmVfZmMgLSB0ZXN0X3kpLm1lYW4oKTouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3Rm91bmRhdGlvbiBtb2RlbCB6ZXJvLXNob3QgdHlwaWNhbGx5IGJlYXRzIG5haXZlIG9uIGRpdmVyc2UgaGVsZC1vdXQgZGF0YS5cdTAwMjcpXG5wcmludChcdTAwMjdUYXNrLXNwZWNpZmljIG1vZGVsIHRyYWluZWQgb24gMTAwMCsgc2ltaWxhciBzZXJpZXMgdHlwaWNhbGx5IGJlYXRzIGZvdW5kYXRpb24uXHUwMDI3KVxucHJpbnQoXHUwMDI3Q3Jvc3NvdmVyOiB+NTAwIHRyYWluaW5nIHNlcmllcyBkZXBlbmRpbmcgb24gZG9tYWluIHNpbWlsYXJpdHkuXHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiWmVyby1TaG90IHZzIEZpbmUtVHVuZWQiLCJjb250ZW50IjoiRm91bmRhdGlvbiBtb2RlbHMgd2luIHdoZW4gbGFiZWxsZWQgdHJhaW5pbmcgZGF0YSBpcyBzY2FyY2Ugb3Igd2hlbiB0aGUgZGVwbG95bWVudCBzZXJpZXMgaXMgZnJvbSBhIG5ldyBkb21haW4uIFdoZW4gc3VmZmljaWVudCBpbi1kb21haW4gdHJhaW5pbmcgZGF0YSBleGlzdHMgKFx1MDAzZTUwMCBzZXJpZXMpLCBmaW5lLXR1bmVkIHRhc2stc3BlY2lmaWMgbW9kZWxzIHR5cGljYWxseSBvdXRwZXJmb3JtLiBGaW5lLXR1bmluZyBhIGZvdW5kYXRpb24gbW9kZWwgd2l0aCBMb1JBIGFkYXB0ZXJzIGNvbWJpbmVzIGJvdGggd29ybGRzOiBzdHJvbmcgcHJpb3JzIGZyb20gcHJldHJhaW5pbmcgd2l0aCBkb21haW4gYWRhcHRhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGb3VuZGF0aW9uIE1vZGVsIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJBcmNoaXRlY3R1cmUiLCJQYXJhbXMiLCJQcm9iYWJpbGlzdGljIiwiWmVyby1TaG90IiwiRmluZS1UdW5lIiwiQmVzdCBVc2UiXSwicm93cyI6W1siVGltZXNGTSIsIkRlY29kZXItb25seSBUcmFuc2Zvcm1lciwgcGF0Y2hlcyIsIjIwME0iLCJZZXMgKHF1YW50aWxlKSIsIlllcyIsIlBhcnRpYWwiLCJQb2ludCArIHF1YW50aWxlIGZvcmVjYXN0cyBhdCBzY2FsZSJdLFsiQ2hyb25vcyIsIlQ1IChlbmMtZGVjKSwgdG9rZW5pemVkIHZhbHVlcyIsIjhN4oCTNzEwTSIsIlllcyAoc2FtcGxpbmcpIiwiWWVzIiwiWWVzIiwiUHJvYmFiaWxpc3RpYyBmb3JlY2FzdGluZywgYW5vbWFseSJdLFsiTW9pcmFpIiwiRW5jb2RlciBUcmFuc2Zvcm1lciwgYW55LXZhcmlhdGUiLCIxNE3igJMzMTFNIiwiWWVzIChzYW1wbGluZykiLCJZZXMiLCJZZXMgKExvUkEpIiwiTXVsdGktdmFyaWF0ZSwgbWl4ZWQgZnJlcXVlbmNpZXMiXSxbIkxhZy1MbGFtYSIsIkxsYW1hIGRlY29kZXIsIGxhZyBmZWF0dXJlcyIsIn40MDBNIiwiWWVzIChkaXN0IGhlYWQpIiwiWWVzIiwiWWVzIiwiTG9uZy1jb250ZXh0IHVuaXZhcmlhdGUiXSxbIk1PTUVOVCIsIk1hc2tlZCBFbmNvZGVyIChUNS1saWtlKSIsIjM4NU0iLCJMaW1pdGVkIiwiWWVzIiwiWWVzIiwiUmVwcmVzZW50YXRpb24gbGVhcm5pbmcgKyBjbGFzc2lmaWNhdGlvbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmluZS1UdW5pbmcgU3RyYXRlZ2llcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm91bmRhdGlvbiBtb2RlbHMgY2FuIGJlIGFkYXB0ZWQgdG8gbmV3IGRvbWFpbnMgdmlhIHNldmVyYWwgc3RyYXRlZ2llczogKDEpIGZ1bGwgZmluZS10dW5pbmcgb24gaW4tZG9tYWluIGRhdGEgKGV4cGVuc2l2ZSBidXQgbW9zdCBlZmZlY3RpdmUpLCAoMikgTG9SQSAoTG93LVJhbmsgQWRhcHRhdGlvbikg4oCUIGFkZGluZyBzbWFsbCB0cmFpbmFibGUgcmFuay1yIG1hdHJpY2VzIHRvIGF0dGVudGlvbiB3ZWlnaHRzLCAoMykgcHJvbXB0IHR1bmluZyDigJQgcHJlcGVuZGluZyBsZWFybmFibGUgY29udGV4dCB0b2tlbnMsICg0KSB6ZXJvLXNob3QgZXZhbHVhdGlvbiB3aXRoIHBlci1zZXJpZXMgbm9ybWFsaXNhdGlvbi4gQ2hyb25vcyBzdXBwb3J0cyBmaW5lLXR1bmluZyB3aXRoIGFzIGZldyBhcyAxMDAgc2VyaWVzLiBNb2lyYWnigJlzIExvUkEgYWRhcHRlcnMgYWRkIG9ubHkgMC4xJSBleHRyYSBwYXJhbWV0ZXJzIHdoaWxlIGFjaGlldmluZyBuZWFyLWZ1bGwtZmluZS10dW5lIGFjY3VyYWN5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiR0lGVC1FdmFsOiAyMy1kYXRhc2V0IGJlbmNobWFyayBjb3ZlcmluZyBtdWx0aXBsZSBmcmVxdWVuY2llcyBhbmQgZG9tYWluczsgdXNlIGZvciB6ZXJvLXNob3QgY29tcGFyaXNvbi4iLCJNb25hc2ggUmVwb3NpdG9yeTogMzArIGRhdGFzZXRzOyBzdGFuZGFyZCBmb3IgY29tcGFyaW5nIGNsYXNzaWNhbCB2cyBkZWVwIHZzIGZvdW5kYXRpb24gbW9kZWxzLiIsIkNSUFMgYW5kIFdRTDogcHJlZmVyIHRoZXNlIG92ZXIgTUFFIGZvciBwcm9iYWJpbGlzdGljIG1vZGVsIGNvbXBhcmlzb24uIiwiTG9SQSByYW5rIDgtMzIgaXMgZWZmZWN0aXZlIGZvciBkb21haW4gYWRhcHRhdGlvbiBvZiBNb2lyYWkgYW5kIENocm9ub3MuIiwiVGltZXNGTSBjb250ZXh0IHdpbmRvdzogNTEyIHRpbWUgc3RlcHM7IGxvbmdlciBzZXJpZXMgbXVzdCBiZSBjaHVua2VkIG9yIHN0cmlkZWQuIiwiQ2hyb25vcyBUNS1zbWFsbCAoNDZNIHBhcmFtcykgb2Z0ZW4gbWF0Y2hlcyBUNS1sYXJnZSAoNzEwTSkgd2l0aCBtdWNoIGxlc3MgY29tcHV0ZS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Time-Series Foundation Models — TimesFM, Chronos, Moirai

Time-series foundation models train on massive, diverse datasets and generalise zero-shot to new time series without task-specific retraining. Motivated by the success of LLMs, they address a key limitation of classical models: each new dataset requires fitting a fresh model. TimesFM (Google), Chronos (Amazon), and Moirai (Salesforce) represent three distinct architectural philosophies, spanning decoder-only Transformers, language-model tokenization, and unified multi-variate attention.

## Motivation — Train Once, Forecast Everywhere

Classical models (ARIMA, ETS, Prophet) must be fit per series, which is expensive at scale. Task-specific deep models (NBEATS, TFT) require a training dataset of related series. Foundation models sidestep this by pretraining on 100B+ time points from diverse domains (energy, finance, weather, traffic), learning universal temporal patterns. At inference, they accept any new series as context and produce forecasts zero-shot, similar to GPT-4 answering new questions without fine-tuning.

## TimesFM — Decoder-Only Patched Transformer

TimesFM (Google DeepMind, 2024) is a 200M-parameter decoder-only Transformer. The input series is divided into non-overlapping patches of length 32 or 64. Each patch is projected to an embedding and processed by the Transformer. Pretraining uses masked patch prediction on 100B time points from Google-internal and public datasets. The model outputs point forecasts and optionally quantile forecasts. It achieves strong zero-shot performance on Monash and GIFT-Eval benchmarks, often competitive with task-specific models trained on in-domain data.

```python
# pip install timesfm
import numpy as np

try:
    import timesfm
    tfm = timesfm.TimesFm(
        hparams=timesfm.TimesFmHparams(
            backend='cpu',
            per_core_batch_size=32,
            horizon_len=24,
        ),
        checkpoint=timesfm.TimesFmCheckpoint(
            huggingface_repo_id='google/timesfm-1.0-200m-pytorch'
        ),
    )
    np.random.seed(0)
    context = [np.cumsum(np.random.randn(96)) + 100.0 for _ in range(4)]
    freq = [0] * 4   # 0=high_freq, 1=medium, 2=low
    point_fc, quantile_fc = tfm.forecast(inputs=context, freq=freq)
    print(f'Point forecast shape:    {point_fc.shape}')     # (batch, horizon)
    print(f'Quantile forecast shape: {quantile_fc.shape}')  # (batch, horizon, n_quantiles)
    print(f'Mean 24-step ahead: {point_fc[0].mean():.3f}')
except ImportError:
    print('TimesFM API summary:')
    print('  Input: List[np.ndarray], each shape (context_len,)')
    print('  freq:  List[int]  -- 0=high, 1=medium, 2=low frequency')
    print('  Output: point_forecast (batch, horizon)')
    print('  Patch length: 32 or 64 time steps')
    print('  Pretraining: masked patch prediction on 100B+ time points')
```

## Chronos — Tokenized Probabilistic Forecasting

Chronos (Amazon, 2024) adapts a T5 language model (encoder-decoder) to time series by quantizing continuous values into discrete tokens via uniform binning. Each bin is a vocabulary token; the model is trained to predict the next token distribution. At inference, multiple sample trajectories are drawn from the predicted distributions, yielding a probabilistic forecast. Chronos requires no frequency information or scaling heuristics — it normalizes each series by its mean before tokenization. It excels at uncertainty quantification and handles irregular sampling naturally.

```python
# pip install chronos-forecasting
import numpy as np

try:
    import torch
    from chronos import ChronosPipeline

    pipeline = ChronosPipeline.from_pretrained(
        'amazon/chronos-t5-small',
        device_map='cpu',
        torch_dtype=torch.float32,
    )
    np.random.seed(42)
    context = torch.tensor(
        np.cumsum(np.random.randn(120)) + 50.0, dtype=torch.float32
    ).unsqueeze(0)  # shape (1, context_len)

    forecast = pipeline.predict(context, prediction_length=24, num_samples=100)
    low    = np.quantile(forecast[0].numpy(), 0.1, axis=0)
    median = np.quantile(forecast[0].numpy(), 0.5, axis=0)
    high   = np.quantile(forecast[0].numpy(), 0.9, axis=0)
    print(f'Forecast samples shape: {forecast[0].shape}')  # (num_samples, horizon)
    print(f'Median forecast (first 4): {median[:4].round(2)}')
    print(f'80% PI width (mean): {(high - low).mean():.3f}')
except ImportError:
    print('Chronos API: ChronosPipeline.from_pretrained(model_name)')
    print('  pipeline.predict(context_tensor, prediction_length=H, num_samples=N)')
    print('  Returns: tensor (batch, num_samples, horizon) for probabilistic output')
    print('  Models: chronos-t5-tiny (8M), small (46M), base (200M), large (710M)')
```

## Moirai — Unified Multi-Variate Forecasting

Moirai (Salesforce, 2024) is an encoder-only Transformer trained on the LOTSA dataset (27B observations across 9 domains). It introduces any-variate attention: a single model handles both univariate and multi-variate series by attending across all variates simultaneously. Key innovations: frequency-aware tokenization (frequency token prepended), multiple patch sizes resolved dynamically, and lag-based feature augmentation. Moirai achieves strong zero-shot performance and can be fine-tuned efficiently with LoRA adapters.

```python
# pip install uni2ts
import numpy as np

try:
    import torch
    from einops import rearrange
    from uni2ts.model.moirai import MoiraiForecast, MoiraiModule

    model = MoiraiForecast(
        module=MoiraiModule.from_pretrained('Salesforce/moirai-1.0-R-small'),
        prediction_length=24,
        context_length=200,
        patch_size=32,
        num_samples=100,
        target_dim=1,
        feat_dynamic_real_dim=0,
        past_feat_dynamic_real_dim=0,
    )
    np.random.seed(7)
    past_target = torch.randn(1, 200, 1)  # (batch, context_len, target_dim)
    forecast = model(past_target)          # (batch, num_samples, horizon, target_dim)
    samples = forecast[0].numpy()         # (num_samples, horizon, 1)
    print(f'Forecast shape: {samples.shape}')
    print(f'Median (first 4 steps): {np.median(samples[:, :4, 0], axis=0).round(3)}')
except ImportError:
    print('Moirai API: MoiraiForecast(module, prediction_length, context_length)')
    print('  Supports: univariate and multi-variate (target_dim > 1)')
    print('  patch_size: 8, 16, or 32 (resolved dynamically at inference)')
    print('  LOTSA pretraining: 27B observations across 9 domains')
    print('  Fine-tuning: LoRA adapters on pretrained module')
```

## Benchmarking Foundation vs Task-Specific Models

On GIFT-Eval and Monash benchmarks, foundation models achieve competitive zero-shot performance, often surpassing statistical models (ETS, ARIMA) and matching or beating task-specific deep models on short-to-medium horizons. However, task-specific models fine-tuned on in-domain data with sufficient training data typically outperform foundation models. The crossover point depends on dataset size: with fewer than ~500 training series, foundation models often win; with larger in-domain datasets, fine-tuned or task-specific models win.

```python
import numpy as np
from sklearn.linear_model import Ridge

np.random.seed(42)
n_series, horizon, context_len = 20, 12, 60

def generate_series(n, length):
    trend = np.linspace(0, 1, length)
    seasonal = np.sin(2 * np.pi * np.arange(length) / 12)
    return np.stack([trend + seasonal + 0.1 * np.random.randn(length) for _ in range(n)])

series = generate_series(n_series, context_len + horizon)
train_ctx = series[:, :context_len]
test_y    = series[:, context_len:]

def naive_seasonal_forecast(ctx, h, period=12):
    return np.stack([ctx[:, -period:] for _ in range((h // period) + 1)], axis=1
                    ).reshape(ctx.shape[0], -1)[:, :h]

def ridge_direct_forecast(ctx, y, h):
    preds = np.zeros((ctx.shape[0], h))
    for step in range(h):
        model = Ridge(alpha=1.0).fit(ctx[:-1], y[:-1, step])
        preds[-1, step] = model.predict(ctx[[-1]])[0]
    return preds

naive_fc = naive_seasonal_forecast(train_ctx, horizon)
print('Benchmark (simulated, no real foundation model call):')
print(f'Naive seasonal MAE: {np.abs(naive_fc - test_y).mean():.4f}')
print('Foundation model zero-shot typically beats naive on diverse held-out data.')
print('Task-specific model trained on 1000+ similar series typically beats foundation.')
print('Crossover: ~500 training series depending on domain similarity.')
```

> **Zero-Shot vs Fine-Tuned**: Foundation models win when labelled training data is scarce or when the deployment series is from a new domain. When sufficient in-domain training data exists (>500 series), fine-tuned task-specific models typically outperform. Fine-tuning a foundation model with LoRA adapters combines both worlds: strong priors from pretraining with domain adaptation.

## Foundation Model Comparison

| Model | Architecture | Params | Probabilistic | Zero-Shot | Fine-Tune | Best Use |
| --- | --- | --- | --- | --- | --- | --- |
| TimesFM | Decoder-only Transformer, patches | 200M | Yes (quantile) | Yes | Partial | Point + quantile forecasts at scale |
| Chronos | T5 (enc-dec), tokenized values | 8M–710M | Yes (sampling) | Yes | Yes | Probabilistic forecasting, anomaly |
| Moirai | Encoder Transformer, any-variate | 14M–311M | Yes (sampling) | Yes | Yes (LoRA) | Multi-variate, mixed frequencies |
| Lag-Llama | Llama decoder, lag features | ~400M | Yes (dist head) | Yes | Yes | Long-context univariate |
| MOMENT | Masked Encoder (T5-like) | 385M | Limited | Yes | Yes | Representation learning + classification |

## Fine-Tuning Strategies

Foundation models can be adapted to new domains via several strategies: (1) full fine-tuning on in-domain data (expensive but most effective), (2) LoRA (Low-Rank Adaptation) — adding small trainable rank-r matrices to attention weights, (3) prompt tuning — prepending learnable context tokens, (4) zero-shot evaluation with per-series normalisation. Chronos supports fine-tuning with as few as 100 series. Moirai’s LoRA adapters add only 0.1% extra parameters while achieving near-full-fine-tune accuracy.

- GIFT-Eval: 23-dataset benchmark covering multiple frequencies and domains; use for zero-shot comparison.
- Monash Repository: 30+ datasets; standard for comparing classical vs deep vs foundation models.
- CRPS and WQL: prefer these over MAE for probabilistic model comparison.
- LoRA rank 8-32 is effective for domain adaptation of Moirai and Chronos.
- TimesFM context window: 512 time steps; longer series must be chunked or strided.
- Chronos T5-small (46M params) often matches T5-large (710M) with much less compute.

---

