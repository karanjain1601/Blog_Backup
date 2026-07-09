---
title: "The Exponential Family"
slug: "exponential-family"
description: "Canonical form, natural parameters, sufficient statistics, log-partition function, moment-generating properties, connection to GLMs, conjugate priors, maximum entropy principle, and natural gradient descent."
tags: ["probability", "statistics", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIGV4cG9uZW50aWFsIGZhbWlseSBpcyB0aGUgbW9zdCBpbXBvcnRhbnQgcGFyYW1ldHJpYyBjbGFzcyBvZiBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb25zIGluIHN0YXRpc3RpY3MgYW5kIE1MLiBJdCB1bmlmaWVzIEdhdXNzaWFuLCBCZXJub3VsbGksIFBvaXNzb24sIEdhbW1hLCBEaXJpY2hsZXQsIGFuZCBkb3plbnMgb2Ygb3RoZXIgZGlzdHJpYnV0aW9ucyB1bmRlciBhIHNpbmdsZSBjYW5vbmljYWwgZm9ybS4gVGhpcyB1bmlmaWNhdGlvbiByZXZlYWxzIGRlZXAgc3RydWN0dXJhbCBwcm9wZXJ0aWVzOiB0aGUgbG9nLXBhcnRpdGlvbiBmdW5jdGlvbiBnZW5lcmF0ZXMgYWxsIG1vbWVudHMgYnkgZGlmZmVyZW50aWF0aW9uLCBNTEUgcmVkdWNlcyB0byBtYXRjaGluZyBleHBlY3RlZCBzdWZmaWNpZW50IHN0YXRpc3RpY3MgdG8gb2JzZXJ2ZWQgc3VmZmljaWVudCBzdGF0aXN0aWNzLCBjb25qdWdhdGUgcHJpb3JzIGFsd2F5cyBleGlzdCBpbiBjbG9zZWQgZm9ybSBmb3IgQmF5ZXNpYW4gdXBkYXRpbmcsIGFuZCB0aGUgRmlzaGVyIGluZm9ybWF0aW9uIGhhcyBhIHBhcnRpY3VsYXJseSBjbGVhbiBleHByZXNzaW9uIGFzIHRoZSBIZXNzaWFuIG9mIHRoZSBsb2ctcGFydGl0aW9uIGZ1bmN0aW9uLiBHTE1zIGFuZCBuYXR1cmFsIGdyYWRpZW50IGRlc2NlbnQgYXJlIGJvdGggYnVpbHQgb24gZXhwb25lbnRpYWwgZmFtaWx5IHN0cnVjdHVyZS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJDb3JlIERlZmluaXRpb24g4oCUIFRoZSBDYW5vbmljYWwgRm9ybSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkEgZGlzdHJpYnV0aW9uIGJlbG9uZ3MgdG8gdGhlIGV4cG9uZW50aWFsIGZhbWlseSBpZiBpdHMgUERGL1BNRiBjYW4gYmUgd3JpdHRlbiBhczpcblxucCh4fM63KSA9IGgoeCkgZXhwKM634bWAIFQoeCkg4oiSIEEozrcpKVxuXG53aGVyZTpcbi0gzrcg4oiIIOKEneG1jzogbmF0dXJhbCBwYXJhbWV0ZXJzIChjYW5vbmljYWwgcGFyYW1ldGVycylcbi0gVCh4KSDiiIgg4oSd4bWPOiBzdWZmaWNpZW50IHN0YXRpc3RpY3Mg4oCUIHRoZSBmdW5jdGlvbnMgb2YgZGF0YSB0aGF0IGNhcnJ5IGFsbCBpbmZvcm1hdGlvbiBhYm91dCDOt1xuLSBBKM63KTogbG9nLXBhcnRpdGlvbiBmdW5jdGlvbiDigJQgZW5zdXJlcyBub3JtYWxpc2F0aW9uOiBleHAoQSjOtykpID0g4oirIGgoeCkgZXhwKM634bWAIFQoeCkpIGR4XG4tIGgoeCk6IGJhc2UgbWVhc3VyZSDigJQgZG9lcyBub3QgZGVwZW5kIG9uIM63XG5cbkVxdWl2YWxlbnRseSBpbiBtZWFuIHBhcmFtZXRlciBmb3JtOiDOvCA9IEVfzrdbVChYKV0gPSDiiIdBKM63KS4gVGhlIG5hdHVyYWwgcGFyYW1ldGVycyDOtyBhbmQgbWVhbiBwYXJhbWV0ZXJzIM68IGFyZSBkdWFsIHJlcHJlc2VudGF0aW9ucyByZWxhdGVkIGJ5IHRoZSBMZWdlbmRyZSB0cmFuc2Zvcm0gb2YgQSjOtykuIFRoZSBuYXR1cmFsIHBhcmFtZXRlcmlzYXRpb24gaXMgbW9zdCBjb252ZW5pZW50IGZvciBjb25qdWdhdGUgcHJpb3JzIGFuZCBuYXR1cmFsIGdyYWRpZW50OyB0aGUgbWVhbiBwYXJhbWV0ZXJpc2F0aW9uIGlzIG1vc3QgY29udmVuaWVudCBmb3IgaW50ZXJwcmV0YXRpb24uIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zcGVjaWFsIGltcG9ydCBnYW1tYWxuXG5cbiMgVmVyaWZ5IHRocmVlIGtleSBkaXN0cmlidXRpb25zIGJlbG9uZyB0byB0aGUgZXhwb25lbnRpYWwgZmFtaWx5XG5cbmRlZiBnYXVzc2lhbl9sb2dfcCh4LCBtdSwgc2lnbWEyKTpcbiAgICBcIlwiXCJcbiAgICBHYXVzc2lhbiBhcyBleHBvbmVudGlhbCBmYW1pbHk6XG4gICAgZXRhID0gKG11L3NpZ21hMiwgLTEvKDIqc2lnbWEyKSksIFQoeCkgPSAoeCwgeF4yKVxuICAgIEEoZXRhKSA9IC1ldGExXjIvKDQqZXRhMikgLSAwLjUqbG9nKC0yKmV0YTIpXG4gICAgaCh4KSA9IDEvc3FydCgyKnBpKVxuICAgIFwiXCJcIlxuICAgIGV0YTEgPSBtdSAvIHNpZ21hMlxuICAgIGV0YTIgPSAtMS4wIC8gKDIgKiBzaWdtYTIpXG4gICAgQSA9IC1ldGExKioyIC8gKDQqZXRhMikgLSAwLjUgKiBucC5sb2coLTIqZXRhMilcbiAgICBoX2xvZyA9IC0wLjUgKiBucC5sb2coMiAqIG5wLnBpKVxuICAgIHJldHVybiBoX2xvZyArIGV0YTEqeCArIGV0YTIqeCoqMiAtIEFcblxuZGVmIGJlcm5vdWxsaV9sb2dfcCh4LCBwKTpcbiAgICBcIlwiXCJcbiAgICBCZXJub3VsbGkgYXMgZXhwb25lbnRpYWwgZmFtaWx5OlxuICAgIGV0YSA9IGxvZyhwLygxLXApKSBbbG9nLW9kZHNdLCBUKHgpID0geCwgQShldGEpID0gbG9nKDErZXhwKGV0YSkpXG4gICAgXCJcIlwiXG4gICAgZXRhID0gbnAubG9nKHAgLyAoMSAtIHApKVxuICAgIEEgICA9IG5wLmxvZygxICsgbnAuZXhwKGV0YSkpXG4gICAgcmV0dXJuIGV0YSAqIHggLSBBICAgIyBoKHgpID0gMVxuXG5kZWYgcG9pc3Nvbl9sb2dfcCh4LCBsYW0pOlxuICAgIFwiXCJcIlxuICAgIFBvaXNzb24gYXMgZXhwb25lbnRpYWwgZmFtaWx5OlxuICAgIGV0YSA9IGxvZyhsYW1iZGEpLCBUKHgpID0geCwgQShldGEpID0gZXhwKGV0YSksIGgoeCkgPSAxL3ghXG4gICAgXCJcIlwiXG4gICAgZXRhID0gbnAubG9nKGxhbSlcbiAgICBBICAgPSBucC5leHAoZXRhKVxuICAgIHJldHVybiAtZ2FtbWFsbih4ICsgMSkgKyBldGEgKiB4IC0gQVxuXG4jIFZlcmlmeSBhZ2FpbnN0IHNjaXB5XG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBub3JtLCBiZXJub3VsbGksIHBvaXNzb25cbnByaW50KFwiPT09IEV4cG9uZW50aWFsIEZhbWlseSBWZXJpZmljYXRpb24gPT09XCIpXG54X2csIG11LCBzaWcyID0gMi41LCAyLjAsIDEuMFxucHJpbnQoZlwiR2F1c3NpYW4gbG9nIHAoMi41fG11PTIsczI9MSk6IEV4cEZhbT17Z2F1c3NpYW5fbG9nX3AoeF9nLG11LHNpZzIpOi42Zn0gIFwiXG4gICAgICBmXCJzY2lweT17bm9ybS5sb2dwZGYoeF9nLG11LG5wLnNxcnQoc2lnMikpOi42Zn1cIilcblxueF9iLCBwX2IgPSAxLCAwLjdcbnByaW50KGZcIkJlcm5vdWxsaSBsb2cgcCgxfHA9MC43KTogICAgICBFeHBGYW09e2Jlcm5vdWxsaV9sb2dfcCh4X2IscF9iKTouNmZ9ICBcIlxuICAgICAgZlwic2NpcHk9e2Jlcm5vdWxsaS5sb2dwbWYoeF9iLHBfYik6LjZmfVwiKVxuXG54X3AsIGxhbSA9IDMsIDIuMFxucHJpbnQoZlwiUG9pc3NvbiBsb2cgcCgzfGxhbT0yKTogICAgICAgIEV4cEZhbT17cG9pc3Nvbl9sb2dfcCh4X3AsbGFtKTouNmZ9ICBcIlxuICAgICAgZlwic2NpcHk9e3BvaXNzb24ubG9ncG1mKHhfcCxsYW0pOi42Zn1cIilcblxuIyBMb2ctcGFydGl0aW9uIGZ1bmN0aW9uIEEoZXRhKSBnZW5lcmF0ZXMgbW9tZW50c1xucHJpbnQoXCJcXG49PT0gQShldGEpIEdyYWRpZW50ID0gRVtUKFgpXSA9PT1cIilcbiMgRm9yIEJlcm5vdWxsaTogQShldGEpID0gbG9nKDErZXhwKGV0YSkpLCBkQS9kZXRhID0gc2lnbW9pZChldGEpID0gcCA9IEVbWF1cbmZvciBwX3ZhbCBpbiBbMC4zLCAwLjUsIDAuOF06XG4gICAgZXRhX3ZhbCA9IG5wLmxvZyhwX3ZhbCAvICgxIC0gcF92YWwpKVxuICAgIGRBID0gbnAuZXhwKGV0YV92YWwpIC8gKDEgKyBucC5leHAoZXRhX3ZhbCkpICAgIyBzaWdtb2lkXG4gICAgcHJpbnQoZlwiICBwPXtwX3ZhbH06IGV0YT17ZXRhX3ZhbDouM2Z9ICBkQS9kZXRhPXtkQTouM2Z9PXAgIEVbWF09e3BfdmFsOi4zZn0gIG1hdGNoOntucC5pc2Nsb3NlKGRBLHBfdmFsKX1cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJLZXkgUHJvcGVydGllcyBvZiB0aGUgTG9nLVBhcnRpdGlvbiBGdW5jdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBsb2ctcGFydGl0aW9uIGZ1bmN0aW9uIEEozrcpIGlzIHRoZSBjdW11bGFudC1nZW5lcmF0aW5nIGZ1bmN0aW9uIG9mIFQoWCkgYW5kIGhhcyByZW1hcmthYmxlIHByb3BlcnRpZXM6XG5cbioqRmlyc3QgZGVyaXZhdGl2ZSA9IGV4cGVjdGVkIHN1ZmZpY2llbnQgc3RhdGlzdGljczoqKlxu4oiCQSjOtykv4oiCzrcgPSBFX863W1QoWCldXG5cbioqU2Vjb25kIGRlcml2YXRpdmUgPSBjb3ZhcmlhbmNlIG9mIHN1ZmZpY2llbnQgc3RhdGlzdGljczoqKlxu4oiCwrJBKM63KS/iiILOt8KyID0gQ292X863W1QoWCldXG5cbkJlY2F1c2UgY292YXJpYW5jZSBtYXRyaWNlcyBhcmUgYWx3YXlzIHBvc2l0aXZlIHNlbWktZGVmaW5pdGUsIOKIh8KyQSjOtykg4omlIDAg4oCUIEEozrcpIGlzIGFsd2F5cyBjb252ZXguIFRoaXMgZ3VhcmFudGVlcyB0aGF0IE1MRSBpbiB0aGUgZXhwb25lbnRpYWwgZmFtaWx5IGlzIGEgY29udmV4IG9wdGltaXNhdGlvbiBwcm9ibGVtIHdpdGggbm8gbG9jYWwgbWluaW1hLlxuXG5Gb3IgR2F1c3NpYW4gd2l0aCBUKHgpID0gKHgsIHjCsik6XG4tIOKIgkEv4oiCzrfigoEgPSBFW1hdID0gzrxcbi0g4oiCwrJBL+KIgs634oKBwrIgPSBWYXJbWF0gPSDPg8KyXG5cbkZvciBCZXJub3VsbGkgd2l0aCBUKHgpID0geDpcbi0g4oiCQS/iiILOtyA9IHAgPSDPgyjOtylcbi0g4oiCwrJBL+KIgs63wrIgPSBwKDHiiJJwKSA9IFZhcltYXSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk1MRSB2aWEgU3VmZmljaWVudCBTdGF0aXN0aWNzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIE1MRSBmb3IgZXhwb25lbnRpYWwgZmFtaWx5IGRpc3RyaWJ1dGlvbnMgaGFzIGEgYmVhdXRpZnVsbHkgc2ltcGxlIGZvcm0g4oCUIHNldCB0aGUgZXhwZWN0ZWQgc3VmZmljaWVudCBzdGF0aXN0aWNzIGVxdWFsIHRvIHRoZSBlbXBpcmljYWwgKG9ic2VydmVkKSBzdWZmaWNpZW50IHN0YXRpc3RpY3M6XG5cbuKIh0EozrfMgikgPSBFX3vOt8yCfVtUKFgpXSA9IHTMhCA9ICgxL24pIM6j4bWiIFQoeOG1oilcblxuRm9yIEdhdXNzaWFuOiAoRVtYXSwgRVtYwrJdKSA9IChzYW1wbGUgbWVhbiwgc2FtcGxlIDJuZCBtb21lbnQpIOKGkiBnaXZlcyDOvMyCID0geMyEIGFuZCDPg8yCwrIgPSBtZWFuKHjCsikg4oiSIHjMhMKyIChzYW1wbGUgdmFyaWFuY2UpLlxuXG5Gb3IgQmVybm91bGxpOiBFW1hdID0gcMyCID0gay9uIChzYW1wbGUgcHJvcG9ydGlvbikuXG5cbkZvciBQb2lzc29uOiBFW1hdID0gzrvMgiA9IHjMhC5cblxuVGhpcyBNTEUgY29uZGl0aW9uIChtYXRjaCBtb21lbnRzIHRvIGRhdGEpIGlzIHRoZSBtZXRob2Qgb2YgbW9tZW50cyDigJQgYnV0IGhlcmUgaXQgaXMgbm90IGFuIGFwcHJveGltYXRpb247IGl0IGdpdmVzIHRoZSBleGFjdCBNTEUuIFRoZSBGaXNoZXItTmV5bWFuIGZhY3RvcmlzYXRpb24gdGhlb3JlbSBzdGF0ZXMgdGhhdCBUKHgpIGNvbnRhaW5zIGFsbCBpbmZvcm1hdGlvbiBhYm91dCDOtyBpbiB0aGUgZGF0YSDigJQgbm8gb3RoZXIgc3RhdGlzdGljIG9mIHRoZSBzYW1lIGRpbWVuc2lvbiBjYW4gaW1wcm92ZSBpbmZlcmVuY2UgYWJvdXQgzrcuIFQoeCkgaXMgdGhlIG1pbmltYWwgc3VmZmljaWVudCBzdGF0aXN0aWMuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zcGVjaWFsIGltcG9ydCBleHBpdCAgIyBudW1lcmljYWxseSBzdGFibGUgc2lnbW9pZFxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgTUxFIHZpYSBzdWZmaWNpZW50IHN0YXRpc3RpY3MgZm9yIHRocmVlIGV4cG9uZW50aWFsIGZhbWlsaWVzXG5wcmludChcIj09PSBFeHBvbmVudGlhbCBGYW1pbHkgTUxFIHZpYSBTdWZmaWNpZW50IFN0YXRpc3RpY3MgPT09XCIpXG5cbiMgMS4gR2F1c3NpYW46IG1hdGNoIChFW1hdLCBFW1heMl0pIHRvIChzYW1wbGUgbWVhbiwgc2FtcGxlIDJuZCBtb21lbnQpXG5tdV90cnVlLCBzaWdtYTJfdHJ1ZSA9IDIuMCwgMS41XG5YID0gcm5nLm5vcm1hbChtdV90cnVlLCBucC5zcXJ0KHNpZ21hMl90cnVlKSwgMTAwMClcbnQxID0gbnAubWVhbihYKSAgICAgICAjIEVbWF0gc3VmZmljaWVudCBzdGF0XG50MiA9IG5wLm1lYW4oWCoqMikgICAgIyBFW1heMl0gc3VmZmljaWVudCBzdGF0XG5tdV9oYXQgICAgPSB0MVxuc2lnbWEyX2hhdCA9IHQyIC0gdDEqKjIgICAjIEVbWF4yXSAtIEVbWF1eMiA9IFZhcltYXVxucHJpbnQoZlwiR2F1c3NpYW46IHRydWUgKG11PXttdV90cnVlfSwgczI9e3NpZ21hMl90cnVlfSksIE1MRSAobXU9e211X2hhdDouNGZ9LCBzMj17c2lnbWEyX2hhdDouNGZ9KVwiKVxuXG4jIDIuIEJlcm5vdWxsaTogbWF0Y2ggRVtYXSA9IGsvblxuaywgbl9iZXJuID0gNzMsIDEwMFxucF9oYXQgPSBrIC8gbl9iZXJuXG5wcmludChmXCJCZXJub3VsbGk6IG9ic2VydmVkIGs9e2t9L3tuX2Jlcm59LCBNTEUgcD17cF9oYXQ6LjRmfVwiKVxuXG4jIDMuIFBvaXNzb246IG1hdGNoIEVbWF0gPSBzYW1wbGUgbWVhblxuWF9wb2lzID0gcm5nLnBvaXNzb24obGFtPTMuNSwgc2l6ZT01MDApXG5sYW1faGF0ID0gbnAubWVhbihYX3BvaXMpICAgIyBzdWZmaWNpZW50IHN0YXQgPSBzdW0oWClcbnByaW50KGZcIlBvaXNzb246IHRydWUgbGFtPTMuNSwgTUxFIGxhbT17bGFtX2hhdDouNGZ9XCIpXG5cbiMgR0xNOiBMb2dpc3RpYyByZWdyZXNzaW9uIGFzIGV4cG9uZW50aWFsIGZhbWlseSAoQmVybm91bGxpLCBsb2dpdCBsaW5rKVxucHJpbnQoXCJcXG49PT0gR0xNIOKAlCBMb2dpc3RpYyBSZWdyZXNzaW9uIChNTEUgdmlhIElSTFMpID09PVwiKVxubiwgZCA9IDQwMCwgNFxuWF9nbG0gPSBucC5oc3RhY2soW25wLm9uZXMoKG4sMSkpLCBybmcuc3RhbmRhcmRfbm9ybWFsKChuLCBkLTEpKV0pXG53X3RydWUgPSBucC5hcnJheShbMC41LCAxLjIsIC0wLjgsIDAuM10pXG55ID0gKHJuZy51bmlmb3JtKHNpemU9bikgPCBleHBpdChYX2dsbSBAIHdfdHJ1ZSkpLmFzdHlwZShmbG9hdClcblxudyA9IG5wLnplcm9zKGQpXG5mb3IgaXQgaW4gcmFuZ2UoMTUpOlxuICAgIHBfaGF0X2dsbSA9IGV4cGl0KFhfZ2xtIEAgdylcbiAgICAjIFNjb3JlID0gWF5UKHkgLSBwX2hhdCkgPSBYXlQob2JzZXJ2ZWQgVChYKSAtIGV4cGVjdGVkIFQoWCkpXG4gICAgZ3JhZCA9IFhfZ2xtLlQgQCAoeSAtIHBfaGF0X2dsbSlcbiAgICAjIEhlc3NpYW4gPSAtWF5UIGRpYWcocCgxLXApKSBYIChuZWdhdGl2ZSBvZiBGaXNoZXIgaW5mb3JtYXRpb24pXG4gICAgRCAgICA9IHBfaGF0X2dsbSAqICgxIC0gcF9oYXRfZ2xtKVxuICAgIEggICAgPSAtWF9nbG0uVCBAIChYX2dsbSAqIERbOiwgTm9uZV0pICAgIyBYXlQgRCBYXG4gICAgdyAgIC09IG5wLmxpbmFsZy5zb2x2ZShILCBncmFkKSAgICAgICAgICAgICMgTmV3dG9uIHN0ZXBcbiAgICBpZiBucC5saW5hbGcubm9ybShncmFkKSA8IDFlLTg6XG4gICAgICAgIHByaW50KGZcIiAgQ29udmVyZ2VkIGF0IGl0ZXJhdGlvbiB7aXQrMX1cIik7IGJyZWFrXG5cbnByaW50KGZcIiAgVHJ1ZSB3OiAge25wLnJvdW5kKHdfdHJ1ZSwgMyl9XCIpXG5wcmludChmXCIgIE1MRSB3OiAgIHtucC5yb3VuZCh3LCAzKX1cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJHZW5lcmFsaXNlZCBMaW5lYXIgTW9kZWxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiR2VuZXJhbGlzZWQgbGluZWFyIG1vZGVscyAoR0xNcykgZXh0ZW5kIGxpbmVhciByZWdyZXNzaW9uIHRvIG5vbi1HYXVzc2lhbiByZXNwb25zZXMgdXNpbmcgZXhwb25lbnRpYWwgZmFtaWx5IGRpc3RyaWJ1dGlvbnMuIEEgR0xNIHNwZWNpZmllczpcblxuMS4gKipSYW5kb20gY29tcG9uZW50Kio6IFkgfCB4IH4gRXhwb25lbnRpYWxGYW1pbHkozrcpXG4yLiAqKlN5c3RlbWF0aWMgY29tcG9uZW50Kio6IM63ID0geF5UIM6yIChsaW5lYXIgcHJlZGljdG9yIGVxdWFscyBuYXR1cmFsIHBhcmFtZXRlcilcbjMuICoqTGluayBmdW5jdGlvbioqOiBnIHN1Y2ggdGhhdCBFW1l8eF0gPSDOvCA9IGfigbvCuSh4XlQgzrIpXG5cbkZvciBlYWNoIGV4cG9uZW50aWFsIGZhbWlseSwgdGhlIGNhbm9uaWNhbCBsaW5rIG1hcHMgdGhlIG1lYW4gZGlyZWN0bHkgdG8gdGhlIG5hdHVyYWwgcGFyYW1ldGVyOlxuLSBHYXVzc2lhbjogY2Fub25pY2FsIGxpbmsgPSBpZGVudGl0eSAobGluZWFyIHJlZ3Jlc3Npb24pXG4tIEJlcm5vdWxsaTogY2Fub25pY2FsIGxpbmsgPSBsb2dpdCBsb2cocC8oMS1wKSkgKGxvZ2lzdGljIHJlZ3Jlc3Npb24pXG4tIFBvaXNzb246IGNhbm9uaWNhbCBsaW5rID0gbG9nIChQb2lzc29uIHJlZ3Jlc3Npb24gZm9yIGNvdW50IGRhdGEpXG4tIEdhbW1hOiBjYW5vbmljYWwgbGluayA9IGludmVyc2UgMS/OvCAoc3Vydml2YWwgYW5hbHlzaXMpXG5cbkFsbCBHTE1zIHNoYXJlIHRoZSBzYW1lIGZpdHRpbmcgYWxnb3JpdGhtOiBJUkxTIChJdGVyYXRpdmVseSBSZXdlaWdodGVkIExlYXN0IFNxdWFyZXMpLCB3aGljaCBpcyBOZXd0b24tUmFwaHNvbiBhcHBsaWVkIHRvIHRoZSBsb2ctbGlrZWxpaG9vZC4gVGhlIGdyYWRpZW50IGlzIGFsd2F5cyBYXlQoeSDiiJIgzrzMgikgYW5kIHRoZSBIZXNzaWFuIGlzIOKIklheVCBXIFggd2hlcmUgVyA9IGRpYWcod+G1oikgYXJlIHRoZSBJUkxTIHdlaWdodHMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29uanVnYXRlIFByaW9ycyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZvciBldmVyeSBleHBvbmVudGlhbCBmYW1pbHkgbGlrZWxpaG9vZCBwKHh8zrcpLCBhIGNvbmp1Z2F0ZSBwcmlvciBvbiDOtyBleGlzdHMgc3VjaCB0aGF0IHRoZSBwb3N0ZXJpb3IgaXMgaW4gdGhlIHNhbWUgZmFtaWx5IGFzIHRoZSBwcmlvciDigJQgZW5hYmxpbmcgY2xvc2VkLWZvcm0gQmF5ZXNpYW4gdXBkYXRlcyB3aXRob3V0IE1DTUMuXG5cblRoZSBjb25qdWdhdGUgcHJpb3IgZm9yIHAoeHzOtykgPSBoKHgpIGV4cCjOt+G1gFQoeCkg4oiSIEEozrcpKSBoYXMgdGhlIGZvcm06XG5wKM63fM+HLCDOvSkg4oidIGV4cCjPh+G1gCDOtyDiiJIgzr0gQSjOtykpXG5cbkFmdGVyIG9ic2VydmluZyBuIGlpZCBzYW1wbGVzIHjigoEsIOKApiwgeOKCmSwgdGhlIHBvc3RlcmlvciBpczpcbnAozrd8eOKCgTrigpksIM+HLCDOvSkg4oidIGV4cCgoz4cgKyDOo+G1oiBUKHjhtaIpKeG1gCDOtyDiiJIgKM69ICsgbikgQSjOtykpXG5cbkJheWVzaWFuIHVwZGF0aW5nIHJlZHVjZXMgdG86XG4tIE5ldyBwc2V1ZG8tY291bnQ6IM69JyA9IM69ICsgblxuLSBOZXcgaHlwZXJwYXJhbWV0ZXI6IM+HJyA9IM+HICsgzqPhtaIgVCh44bWiKVxuXG5Db25jcmV0ZSBleGFtcGxlczpcbi0gQmVybm91bGxpIHdpdGggQmV0YSjOsSzOsikgcHJpb3I6IHBvc3RlcmlvciBpcyBCZXRhKM6xICsgzqN44bWiLCDOsiArIG4g4oiSIM6jeOG1oilcbi0gUG9pc3NvbiB3aXRoIEdhbW1hKGEsYikgcHJpb3I6IHBvc3RlcmlvciBpcyBHYW1tYShhICsgzqN44bWiLCBiICsgbilcbi0gR2F1c3NpYW4gKGtub3duIM+DwrIpIHdpdGggTijOvOKCgCzPhMKyKSBwcmlvcjogcG9zdGVyaW9yIGlzIEdhdXNzaWFuIHdpdGggdXBkYXRlZCBtZWFuIGFuZCB2YXJpYW5jZSJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IGJldGEgYXMgYmV0YV9kaXN0LCBnYW1tYSBhcyBnYW1tYV9kaXN0XG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0MilcblxuIyBDb25qdWdhdGUgcHJpb3IgdXBkYXRpbmc6IEJlcm5vdWxsaSB3aXRoIEJldGEgcHJpb3JcbnByaW50KFwiPT09IEJldGEtQmVybm91bGxpIENvbmp1Z2F0ZSBVcGRhdGVzID09PVwiKVxuYSwgYiA9IDIuMCwgMi4wICAgIyBCZXRhKDIsMikgcHJpb3I6IHN5bW1ldHJpYywgc2xpZ2h0IGluZm9ybWF0aXZlbmVzc1xuZmxpcHMgPSBbMSwwLDEsMSwwLDEsMSwxLDAsMSwwLDEsMSwwLDFdICAjIDEwIGhlYWRzLCA1IHRhaWxzXG5wcmludChmXCJQcmlvcjogQmV0YSh7YX0se2J9KSAgbWVhbj17YS8oYStiKTouM2Z9ICBzdGQ9e25wLnNxcnQoYSpiLyhhK2IpKioyLyhhK2IrMSkpOi4zZn1cIilcbmZvciBpLCBmbGlwIGluIGVudW1lcmF0ZShmbGlwcywgMSk6XG4gICAgYSArPSBmbGlwOyBiICs9ICgxLWZsaXApXG4gICAgcG9zdF9tZWFuID0gYS8oYStiKVxuICAgIGNpX2xvLCBjaV9oaSA9IGJldGFfZGlzdC5wcGYoWzAuMDI1LCAwLjk3NV0sIGEsIGIpXG4gICAgaWYgaSBpbiBbMSwgNSwgMTAsIDE1XTpcbiAgICAgICAgcHJpbnQoZlwiICBBZnRlciB7aToyZH0gb2JzOiBCZXRhKHthOi4wZn0se2I6LjBmfSkgbWVhbj17cG9zdF9tZWFuOi4zZn0gOTUlQ0k9W3tjaV9sbzouM2Z9LHtjaV9oaTouM2Z9XVwiKVxuXG4jIENvbmp1Z2F0ZSB1cGRhdGluZzogUG9pc3NvbiB3aXRoIEdhbW1hIHByaW9yXG5wcmludChcIlxcbj09PSBHYW1tYS1Qb2lzc29uIENvbmp1Z2F0ZSBVcGRhdGVzID09PVwiKVxuYV9wcmlvciwgYl9wcmlvciA9IDMuMCwgMS4wICAgIyBHYW1tYSgzLDEpIHByaW9yOiBFW2xhbWJkYV0gPSBhL2IgPSAzXG5sYW1iZGFfdHJ1ZSA9IDQuNVxuWF9wb2lzID0gcm5nLnBvaXNzb24obGFtPWxhbWJkYV90cnVlLCBzaXplPTUwKVxuYV9wb3N0ID0gYV9wcmlvciArIG5wLnN1bShYX3BvaXMpXG5iX3Bvc3QgPSBiX3ByaW9yICsgbGVuKFhfcG9pcylcbnBvc3RfbWVhbiA9IGFfcG9zdCAvIGJfcG9zdFxucG9zdF9tb2RlID0gKGFfcG9zdCAtIDEpIC8gYl9wb3N0IGlmIGFfcG9zdCA+PSAxIGVsc2UgMFxucHJpbnQoZlwiVHJ1ZSBsYW1iZGE6IHtsYW1iZGFfdHJ1ZX0sIFByaW9yOiBHYW1tYSh7YV9wcmlvcn0se2JfcHJpb3J9KSBFPXthX3ByaW9yL2JfcHJpb3I6LjFmfVwiKVxucHJpbnQoZlwiUG9zdGVyaW9yOiBHYW1tYSh7YV9wb3N0fSx7Yl9wb3N0Oi4wZn0pIG1lYW49e3Bvc3RfbWVhbjouNGZ9IG1vZGU9e3Bvc3RfbW9kZTouNGZ9XCIpXG5cbiMgTmF0dXJhbCBncmFkaWVudCB2cyBFdWNsaWRlYW4gZ3JhZGllbnQgZm9yIEJlcm5vdWxsaVxucHJpbnQoXCJcXG49PT0gTmF0dXJhbCBHcmFkaWVudCB2cyBFdWNsaWRlYW4gR3JhZGllbnQgKEJlcm5vdWxsaSkgPT09XCIpXG4jIFRhcmdldDogcCA9IDAuOC4gQ3VycmVudDogcCA9IDAuNS4gR3JhZGllbnQgYXNjZW50IG9uIGxvZy1saWtlbGlob29kLlxucF90cnVlID0gMC44XG5YX2Jlcm4gPSBybmcuYmlub21pYWwoMSwgcF90cnVlLCAxMDApXG4jIE5hdHVyYWwgZ3JhZGllbnQgaW4gZXRhLXNwYWNlOiBncmFkX25hdCA9IDEvSShldGEpICogZ3JhZF9ldGFcbiMgRm9yIEJlcm5vdWxsaTogSShldGEpID0gcCgxLXApID0gc2lnbWEoZXRhKSooMS1zaWdtYShldGEpKSA9IGReMkEvZGV0YV4yXG5ldGFfbmF0ID0gMC4wOyBldGFfZ2QgPSAwLjAgICAjIGJvdGggc3RhcnQgYXQgZXRhPTAgKHA9MC41KVxubHIgPSAwLjVcbmZvciBzdGVwIGluIHJhbmdlKDIwKTpcbiAgICBwX25hdCA9IDEvKDErbnAuZXhwKC1ldGFfbmF0KSk7IHBfZ2QgID0gMS8oMStucC5leHAoLWV0YV9nZCkpXG4gICAgIyBTY29yZSAoZ3JhZGllbnQgdy5yLnQuIGV0YSlcbiAgICBncmFkX25hdCA9IG5wLm1lYW4oWF9iZXJuKSAtIHBfbmF0ICAgIyBkQS9kZXRhID0gcCwgc28gc2NvcmUgPSB4X2JhciAtIHBcbiAgICBncmFkX2dkICA9IG5wLm1lYW4oWF9iZXJuKSAtIHBfZ2RcbiAgICAjIEZpc2hlciBmb3IgQmVybm91bGxpOiBJKGV0YSkgPSBwKDEtcClcbiAgICBmaXNoZXIgPSBwX25hdCAqICgxIC0gcF9uYXQpXG4gICAgbmF0X2dyYWQgPSBncmFkX25hdCAvIGZpc2hlciAgICAgICAgICMgbmF0dXJhbCBncmFkaWVudCA9IEleey0xfSAqIHNjb3JlXG4gICAgZXRhX25hdCArPSBsciAqIG5hdF9ncmFkICAgICAgICAgICAgICMgbmF0dXJhbCBncmFkaWVudCBzdGVwIChOZXd0b24gc3RlcClcbiAgICBldGFfZ2QgICs9IGxyICogZ3JhZF9nZCAgICAgICAgICAgICAjIEV1Y2xpZGVhbiBncmFkaWVudCBzdGVwXG5wcmludChmXCJBZnRlciAyMCBzdGVwczogbmF0X2dyYWQgcD17MS8oMStucC5leHAoLWV0YV9uYXQpKTouNGZ9ICBldWNsX2dyYWQgcD17MS8oMStucC5leHAoLWV0YV9nZCkpOi40Zn1cIilcbnByaW50KGZcIlRydWUgcCA9IHtwX3RydWV9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTmF0dXJhbCBHcmFkaWVudCBEZXNjZW50In0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3RhbmRhcmQgZ3JhZGllbnQgZGVzY2VudCBmb2xsb3dzIHN0ZWVwZXN0IGFzY2VudCBpbiBFdWNsaWRlYW4gcGFyYW1ldGVyIHNwYWNlOiDOlM63IOKInSDiiIdfzrcg4oSTKM63KS4gQnV0IHRoZSBFdWNsaWRlYW4gZGlzdGFuY2UgYmV0d2VlbiBwYXJhbWV0ZXJzIGRvZXMgbm90IHJlZmxlY3QgZGlzdGFuY2UgYmV0d2VlbiBkaXN0cmlidXRpb25zIOKAlCBjaGFuZ2luZyDOtyBieSB0aGUgc2FtZSBFdWNsaWRlYW4gc3RlcCBjYW4gaGF2ZSB2ZXJ5IGRpZmZlcmVudCBlZmZlY3RzIGRlcGVuZGluZyBvbiB0aGUgY3VydmF0dXJlIG9mIEEozrcpLlxuXG5OYXR1cmFsIGdyYWRpZW50IGRlc2NlbnQgZm9sbG93cyBzdGVlcGVzdCBhc2NlbnQgaW4gdGhlIHNwYWNlIG9mIHByb2JhYmlsaXR5IGRpc3RyaWJ1dGlvbnMgKEZpc2hlci1SYW8gbWV0cmljKTpcbs6Uzrcg4oidIEYozrcp4oG7wrkg4oiHX863IOKEkyjOtylcblxud2hlcmUgRijOtykgPSBFWyjiiIdfzrcgbG9nIHApKOKIh1/OtyBsb2cgcCleVF0gaXMgdGhlIEZpc2hlciBpbmZvcm1hdGlvbiBtYXRyaXguIEZvciBleHBvbmVudGlhbCBmYW1pbGllczogRijOtykgPSDiiIfCskEozrcpID0gQ292X863W1QoWCldIOKAlCB0aGUgRmlzaGVyIGVxdWFscyB0aGUgSGVzc2lhbiBvZiB0aGUgbG9nLXBhcnRpdGlvbiBmdW5jdGlvbi5cblxuVGhlcmVmb3JlLCBmb3IgZXhwb25lbnRpYWwgZmFtaWxpZXMsIG5hdHVyYWwgZ3JhZGllbnQgPSBOZXd0b24gc3RlcC4gTmF0dXJhbCBncmFkaWVudCBjb252ZXJnZXMgaW4gTygxKSBzdGVwcyBmb3IgbGluZWFyIG1vZGVscywgY29tcGFyZWQgdG8gTyjOuikgZm9yIGdyYWRpZW50IGRlc2NlbnQgKM66ID0gY29uZGl0aW9uIG51bWJlcikuIEtGQUMsIFNoYW1wb28sIGFuZCBvdGhlciBzZWNvbmQtb3JkZXIgb3B0aW1pc2VycyBhcHByb3hpbWF0ZSB0aGUgRmlzaGVyIGZvciBuZXVyYWwgbmV0d29ya3MuIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInZhcmlhbnQiOiAidGlwIiwgInRpdGxlIjogIk1heGltdW0gRW50cm9weSBQcmluY2lwbGUiLCAiY29udGVudCI6ICJFeHBvbmVudGlhbCBmYW1pbHkgZGlzdHJpYnV0aW9ucyBhcmUgZXhhY3RseSB0aG9zZSB0aGF0IG1heGltaXNlIGVudHJvcHkgc3ViamVjdCB0byBtb21lbnQgY29uc3RyYWludHMuIElmIHdlIGtub3cgRVtUKFgpXSA9IHQgYW5kIHdhbnQgdGhlIG1heGltYWxseSB1bmluZm9ybWF0aXZlIGRpc3RyaWJ1dGlvbiBvdGhlcndpc2UsIHRoZSBzb2x1dGlvbiBpcyBwKih4KSDiiJ0gaCh4KSBleHAozrfhtYAgVCh4KSkgd2hlcmUgzrcgaXMgY2hvc2VuIHNvIEVfcCpbVChYKV0gPSB0LiBUaGlzIGp1c3RpZmllczogR2F1c3NpYW4gKG1heCBlbnRyb3B5IHdpdGggZml4ZWQgbWVhbiBhbmQgdmFyaWFuY2UpLCBMYXBsYWNlIChtYXggZW50cm9weSB3aXRoIGZpeGVkIG1lYW4gYWJzb2x1dGUgZGV2aWF0aW9uKSwgY2F0ZWdvcmljYWwvc29mdG1heCAobWF4IGVudHJvcHkgd2l0aCBmaXhlZCBtYXJnaW5hbCBwcm9iYWJpbGl0aWVzKS4gQWx3YXlzIHVzZSB0aGUgZXhwb25lbnRpYWwgZmFtaWx5IG1lbWJlciBtYXRjaGluZyB5b3VyIGtub3duIG1vbWVudCBjb25zdHJhaW50cy4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidmFyaWFudCI6ICJpbmZvIiwgInRpdGxlIjogIkV4cG9uZW50aWFsIEZhbWlseSBhbmQgTmV1cmFsIE5ldHdvcmtzIiwgImNvbnRlbnQiOiAiU29mdG1heCBvdXRwdXQgbGF5ZXJzIGltcGxlbWVudCB0aGUgY2F0ZWdvcmljYWwgZXhwb25lbnRpYWwgZmFtaWx5OiBwKHk9a3x4KSA9IGV4cCjOt+KClikgLyDOo+KxvCBleHAozrfisbwpIHdoZXJlIM634oKWID0gd+KCluG1gCB4IGFyZSB0aGUgbmF0dXJhbCBwYXJhbWV0ZXJzIGFuZCBBKM63KSA9IGxvZyDOo+KxvCBleHAozrfisbwpIGlzIHRoZSBsb2ctc29mdG1heCBkZW5vbWluYXRvci4gQ3Jvc3MtZW50cm9weSBsb3NzID0gbmVnYXRpdmUgbG9nLWxpa2VsaWhvb2QgPSBBKM63KSDiiJIgzrdbeV90YXJnZXRdLiBUcmFpbmluZyB3aXRoIGNyb3NzLWVudHJvcHkgaXMgTUxFIGluIHRoZSBjYXRlZ29yaWNhbCBleHBvbmVudGlhbCBmYW1pbHkg4oCUIHRoZSBsb2ctcGFydGl0aW9uIGZ1bmN0aW9uIGFwcGVhcnMgaW4gZXZlcnkgZm9yd2FyZCBwYXNzIGFzIHRoZSBub3JtYWxpc2F0aW9uIGNvbXB1dGF0aW9uLiJ9LCB7InR5cGUiOiAidGFibGUiLCAiaGVhZGVycyI6IFsiRGlzdHJpYnV0aW9uIiwgIs63IChuYXR1cmFsKSIsICJUKHgpIChzdWZmaWNpZW50IHN0YXQpIiwgIkEozrcpIChsb2ctcGFydGl0aW9uKSIsICJDb25qdWdhdGUgcHJpb3IiXSwgInJvd3MiOiBbWyJCZXJub3VsbGkocCkiLCAibG9nKHAvKDEtcCkpIiwgIngiLCAibG9nKDErZXhwKM63KSkiLCAiQmV0YSjOsSzOsikiXSwgWyJHYXVzc2lhbijOvCzPg8KyKSIsICIozrwvz4PCsiwg4oiSMS8oMs+DwrIpKSIsICIoeCwgeMKyKSIsICLiiJLOt+KCgcKyLyg0zrfigoIp4oiSwr1sb2co4oiSMs634oKCKSIsICJOb3JtYWwtSW52ZXJzZS1HYW1tYSJdLCBbIlBvaXNzb24ozrspIiwgImxvZyDOuyIsICJ4IiwgImV4cCjOtykgPSDOuyIsICJHYW1tYSjOsSzOsikiXSwgWyJHYW1tYSjOsSzOsikiLCAiKM6x4oiSMSwg4oiSzrIpIiwgIihsb2cgeCwgeCkiLCAibG9nIM6TKM634oKBKzEp4oiSKM634oKBKzEpbG9nKOKIks634oKCKSIsICLigJQiXSwgWyJDYXRlZ29yaWNhbChwKSIsICJsb2cocOKCli9w4oKWKSBmb3IgazxLIiwgIjFbeD1rXSBlYWNoIGsiLCAibG9nIM6jIGV4cCjOt+KClikiLCAiRGlyaWNobGV0KM6xKSJdXX0sIHsidHlwZSI6ICJkaXZpZGVyIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2V5IFRha2Vhd2F5cyJ9LCB7InR5cGUiOiAibGlzdCIsICJvcmRlcmVkIjogZmFsc2UsICJpdGVtcyI6IFsiRXhwb25lbnRpYWwgZmFtaWx5OiBwKHh8zrcpID0gaCh4KSBleHAozrfhtYBUKHgpIOKIkiBBKM63KSkgdW5pZmllcyBHYXVzc2lhbiwgQmVybm91bGxpLCBQb2lzc29uLCBHYW1tYSwgRGlyaWNobGV0IGFuZCBtYW55IG1vcmUgdW5kZXIgb25lIGZyYW1ld29yay4iLCAiVGhlIGxvZy1wYXJ0aXRpb24gQSjOtykgaXMgYWx3YXlzIGNvbnZleDog4oiHQSjOtykgPSBFW1QoWCldIGFuZCDiiIfCskEozrcpID0gQ292W1QoWCldIOKJpSAwIOKAlCBNTEUgaXMgYSBjb252ZXggb3B0aW1pc2F0aW9uIHdpdGggbm8gbG9jYWwgbWluaW1hLiIsICJNTEUgZm9yIGV4cG9uZW50aWFsIGZhbWlsaWVzOiBzZXQgZXhwZWN0ZWQgc3VmZmljaWVudCBzdGF0aXN0aWNzIEVbVChYKV0gZXF1YWwgdG8gb2JzZXJ2ZWQgc3VmZmljaWVudCBzdGF0aXN0aWNzIHTMhCA9ICgxL24pIM6jIFQoeOG1oikuIiwgIlN1ZmZpY2llbnQgc3RhdGlzdGljcyBUKHgpIGNvbnRhaW4gYWxsIGluZm9ybWF0aW9uIGFib3V0IM63IOKAlCBubyBvdGhlciBzdGF0aXN0aWMgb2YgdGhlIHNhbWUgZGltZW5zaW9uIGNhbiBpbXByb3ZlIGluZmVyZW5jZSAoRmlzaGVyLU5leW1hbiBmYWN0b3Jpc2F0aW9uKS4iLCAiQ29uanVnYXRlIHByaW9ycyBmb3IgZXhwb25lbnRpYWwgZmFtaWxpZXMgYWx3YXlzIGV4aXN0OyBCYXllc2lhbiB1cGRhdGVzIHJlZHVjZSB0byBhZGRpbmcgb2JzZXJ2ZWQgc3VmZmljaWVudCBzdGF0aXN0aWNzIHRvIHByaW9yIGh5cGVycGFyYW1ldGVycy4iLCAiR0xNcyB1c2UgZXhwb25lbnRpYWwgZmFtaWx5IHJlc3BvbnNlcyB3aXRoIGEgbGluayBmdW5jdGlvbiBjb25uZWN0aW5nIHRoZSBtZWFuIHRvIHRoZSBsaW5lYXIgcHJlZGljdG9yOyBhbGwgZml0IHZpYSBJUkxTIChOZXd0b24tUmFwaHNvbiBvbiBsb2ctbGlrZWxpaG9vZCkuIiwgIk5hdHVyYWwgZ3JhZGllbnQgPSBGKM63KeKBu8K5IOKIh+KEkyA9IOKIh8KyQSjOtynigbvCuSDiiIfihJMg4oCUIGZvciBleHBvbmVudGlhbCBmYW1pbGllcyB0aGlzIGlzIHRoZSBOZXd0b24gc3RlcCwgY29udmVyZ2luZyBpbiBPKDEpIHN0ZXBzIGZvciBsaW5lYXIgbW9kZWxzIHZlcnN1cyBPKM66KSBmb3IgZ3JhZGllbnQgZGVzY2VudC4iXX1d"
---
# The Exponential Family

The exponential family is the most important parametric class of probability distributions in statistics and ML. It unifies Gaussian, Bernoulli, Poisson, Gamma, Dirichlet, and dozens of other distributions under a single canonical form. This unification reveals deep structural properties: the log-partition function generates all moments by differentiation, MLE reduces to matching expected sufficient statistics to observed sufficient statistics, conjugate priors always exist in closed form for Bayesian updating, and the Fisher information has a particularly clean expression as the Hessian of the log-partition function. GLMs and natural gradient descent are both built on exponential family structure.

## Core Definition — The Canonical Form

A distribution belongs to the exponential family if its PDF/PMF can be written as:

p(x|η) = h(x) exp(ηᵀ T(x) − A(η))

where:
- η ∈ ℝᵏ: natural parameters (canonical parameters)
- T(x) ∈ ℝᵏ: sufficient statistics — the functions of data that carry all information about η
- A(η): log-partition function — ensures normalisation: exp(A(η)) = ∫ h(x) exp(ηᵀ T(x)) dx
- h(x): base measure — does not depend on η

Equivalently in mean parameter form: μ = E_η[T(X)] = ∇A(η). The natural parameters η and mean parameters μ are dual representations related by the Legendre transform of A(η). The natural parameterisation is most convenient for conjugate priors and natural gradient; the mean parameterisation is most convenient for interpretation.

```python
import numpy as np
from scipy.special import gammaln

# Verify three key distributions belong to the exponential family

def gaussian_log_p(x, mu, sigma2):
    """
    Gaussian as exponential family:
    eta = (mu/sigma2, -1/(2*sigma2)), T(x) = (x, x^2)
    A(eta) = -eta1^2/(4*eta2) - 0.5*log(-2*eta2)
    h(x) = 1/sqrt(2*pi)
    """
    eta1 = mu / sigma2
    eta2 = -1.0 / (2 * sigma2)
    A = -eta1**2 / (4*eta2) - 0.5 * np.log(-2*eta2)
    h_log = -0.5 * np.log(2 * np.pi)
    return h_log + eta1*x + eta2*x**2 - A

def bernoulli_log_p(x, p):
    """
    Bernoulli as exponential family:
    eta = log(p/(1-p)) [log-odds], T(x) = x, A(eta) = log(1+exp(eta))
    """
    eta = np.log(p / (1 - p))
    A   = np.log(1 + np.exp(eta))
    return eta * x - A   # h(x) = 1

def poisson_log_p(x, lam):
    """
    Poisson as exponential family:
    eta = log(lambda), T(x) = x, A(eta) = exp(eta), h(x) = 1/x!
    """
    eta = np.log(lam)
    A   = np.exp(eta)
    return -gammaln(x + 1) + eta * x - A

# Verify against scipy
from scipy.stats import norm, bernoulli, poisson
print("=== Exponential Family Verification ===")
x_g, mu, sig2 = 2.5, 2.0, 1.0
print(f"Gaussian log p(2.5|mu=2,s2=1): ExpFam={gaussian_log_p(x_g,mu,sig2):.6f}  "
      f"scipy={norm.logpdf(x_g,mu,np.sqrt(sig2)):.6f}")

x_b, p_b = 1, 0.7
print(f"Bernoulli log p(1|p=0.7):      ExpFam={bernoulli_log_p(x_b,p_b):.6f}  "
      f"scipy={bernoulli.logpmf(x_b,p_b):.6f}")

x_p, lam = 3, 2.0
print(f"Poisson log p(3|lam=2):        ExpFam={poisson_log_p(x_p,lam):.6f}  "
      f"scipy={poisson.logpmf(x_p,lam):.6f}")

# Log-partition function A(eta) generates moments
print("\n=== A(eta) Gradient = E[T(X)] ===")
# For Bernoulli: A(eta) = log(1+exp(eta)), dA/deta = sigmoid(eta) = p = E[X]
for p_val in [0.3, 0.5, 0.8]:
    eta_val = np.log(p_val / (1 - p_val))
    dA = np.exp(eta_val) / (1 + np.exp(eta_val))   # sigmoid
    print(f"  p={p_val}: eta={eta_val:.3f}  dA/deta={dA:.3f}=p  E[X]={p_val:.3f}  match:{np.isclose(dA,p_val)}")
```

## Key Properties of the Log-Partition Function

The log-partition function A(η) is the cumulant-generating function of T(X) and has remarkable properties:

**First derivative = expected sufficient statistics:**
∂A(η)/∂η = E_η[T(X)]

**Second derivative = covariance of sufficient statistics:**
∂²A(η)/∂η² = Cov_η[T(X)]

Because covariance matrices are always positive semi-definite, ∇²A(η) ≥ 0 — A(η) is always convex. This guarantees that MLE in the exponential family is a convex optimisation problem with no local minima.

For Gaussian with T(x) = (x, x²):
- ∂A/∂η₁ = E[X] = μ
- ∂²A/∂η₁² = Var[X] = σ²

For Bernoulli with T(x) = x:
- ∂A/∂η = p = σ(η)
- ∂²A/∂η² = p(1−p) = Var[X]

## MLE via Sufficient Statistics

The MLE for exponential family distributions has a beautifully simple form — set the expected sufficient statistics equal to the empirical (observed) sufficient statistics:

∇A(η̂) = E_{η̂}[T(X)] = t̄ = (1/n) Σᵢ T(xᵢ)

For Gaussian: (E[X], E[X²]) = (sample mean, sample 2nd moment) → gives μ̂ = x̄ and σ̂² = mean(x²) − x̄² (sample variance).

For Bernoulli: E[X] = p̂ = k/n (sample proportion).

For Poisson: E[X] = λ̂ = x̄.

This MLE condition (match moments to data) is the method of moments — but here it is not an approximation; it gives the exact MLE. The Fisher-Neyman factorisation theorem states that T(x) contains all information about η in the data — no other statistic of the same dimension can improve inference about η. T(x) is the minimal sufficient statistic.

```python
import numpy as np
from scipy.special import expit  # numerically stable sigmoid

rng = np.random.default_rng(42)

# MLE via sufficient statistics for three exponential families
print("=== Exponential Family MLE via Sufficient Statistics ===")

# 1. Gaussian: match (E[X], E[X^2]) to (sample mean, sample 2nd moment)
mu_true, sigma2_true = 2.0, 1.5
X = rng.normal(mu_true, np.sqrt(sigma2_true), 1000)
t1 = np.mean(X)       # E[X] sufficient stat
t2 = np.mean(X**2)    # E[X^2] sufficient stat
mu_hat    = t1
sigma2_hat = t2 - t1**2   # E[X^2] - E[X]^2 = Var[X]
print(f"Gaussian: true (mu={mu_true}, s2={sigma2_true}), MLE (mu={mu_hat:.4f}, s2={sigma2_hat:.4f})")

# 2. Bernoulli: match E[X] = k/n
k, n_bern = 73, 100
p_hat = k / n_bern
print(f"Bernoulli: observed k={k}/{n_bern}, MLE p={p_hat:.4f}")

# 3. Poisson: match E[X] = sample mean
X_pois = rng.poisson(lam=3.5, size=500)
lam_hat = np.mean(X_pois)   # sufficient stat = sum(X)
print(f"Poisson: true lam=3.5, MLE lam={lam_hat:.4f}")

# GLM: Logistic regression as exponential family (Bernoulli, logit link)
print("\n=== GLM — Logistic Regression (MLE via IRLS) ===")
n, d = 400, 4
X_glm = np.hstack([np.ones((n,1)), rng.standard_normal((n, d-1))])
w_true = np.array([0.5, 1.2, -0.8, 0.3])
y = (rng.uniform(size=n) < expit(X_glm @ w_true)).astype(float)

w = np.zeros(d)
for it in range(15):
    p_hat_glm = expit(X_glm @ w)
    # Score = X^T(y - p_hat) = X^T(observed T(X) - expected T(X))
    grad = X_glm.T @ (y - p_hat_glm)
    # Hessian = -X^T diag(p(1-p)) X (negative of Fisher information)
    D    = p_hat_glm * (1 - p_hat_glm)
    H    = -X_glm.T @ (X_glm * D[:, None])   # X^T D X
    w   -= np.linalg.solve(H, grad)            # Newton step
    if np.linalg.norm(grad) < 1e-8:
        print(f"  Converged at iteration {it+1}"); break

print(f"  True w:  {np.round(w_true, 3)}")
print(f"  MLE w:   {np.round(w, 3)}")
```

## Generalised Linear Models

Generalised linear models (GLMs) extend linear regression to non-Gaussian responses using exponential family distributions. A GLM specifies:

1. **Random component**: Y | x ~ ExponentialFamily(η)
2. **Systematic component**: η = x^T β (linear predictor equals natural parameter)
3. **Link function**: g such that E[Y|x] = μ = g⁻¹(x^T β)

For each exponential family, the canonical link maps the mean directly to the natural parameter:
- Gaussian: canonical link = identity (linear regression)
- Bernoulli: canonical link = logit log(p/(1-p)) (logistic regression)
- Poisson: canonical link = log (Poisson regression for count data)
- Gamma: canonical link = inverse 1/μ (survival analysis)

All GLMs share the same fitting algorithm: IRLS (Iteratively Reweighted Least Squares), which is Newton-Raphson applied to the log-likelihood. The gradient is always X^T(y − μ̂) and the Hessian is −X^T W X where W = diag(wᵢ) are the IRLS weights.

## Conjugate Priors

For every exponential family likelihood p(x|η), a conjugate prior on η exists such that the posterior is in the same family as the prior — enabling closed-form Bayesian updates without MCMC.

The conjugate prior for p(x|η) = h(x) exp(ηᵀT(x) − A(η)) has the form:
p(η|χ, ν) ∝ exp(χᵀ η − ν A(η))

After observing n iid samples x₁, …, xₙ, the posterior is:
p(η|x₁:ₙ, χ, ν) ∝ exp((χ + Σᵢ T(xᵢ))ᵀ η − (ν + n) A(η))

Bayesian updating reduces to:
- New pseudo-count: ν' = ν + n
- New hyperparameter: χ' = χ + Σᵢ T(xᵢ)

Concrete examples:
- Bernoulli with Beta(α,β) prior: posterior is Beta(α + Σxᵢ, β + n − Σxᵢ)
- Poisson with Gamma(a,b) prior: posterior is Gamma(a + Σxᵢ, b + n)
- Gaussian (known σ²) with N(μ₀,τ²) prior: posterior is Gaussian with updated mean and variance

```python
import numpy as np
from scipy.stats import beta as beta_dist, gamma as gamma_dist

rng = np.random.default_rng(42)

# Conjugate prior updating: Bernoulli with Beta prior
print("=== Beta-Bernoulli Conjugate Updates ===")
a, b = 2.0, 2.0   # Beta(2,2) prior: symmetric, slight informativeness
flips = [1,0,1,1,0,1,1,1,0,1,0,1,1,0,1]  # 10 heads, 5 tails
print(f"Prior: Beta({a},{b})  mean={a/(a+b):.3f}  std={np.sqrt(a*b/(a+b)**2/(a+b+1)):.3f}")
for i, flip in enumerate(flips, 1):
    a += flip; b += (1-flip)
    post_mean = a/(a+b)
    ci_lo, ci_hi = beta_dist.ppf([0.025, 0.975], a, b)
    if i in [1, 5, 10, 15]:
        print(f"  After {i:2d} obs: Beta({a:.0f},{b:.0f}) mean={post_mean:.3f} 95%CI=[{ci_lo:.3f},{ci_hi:.3f}]")

# Conjugate updating: Poisson with Gamma prior
print("\n=== Gamma-Poisson Conjugate Updates ===")
a_prior, b_prior = 3.0, 1.0   # Gamma(3,1) prior: E[lambda] = a/b = 3
lambda_true = 4.5
X_pois = rng.poisson(lam=lambda_true, size=50)
a_post = a_prior + np.sum(X_pois)
b_post = b_prior + len(X_pois)
post_mean = a_post / b_post
post_mode = (a_post - 1) / b_post if a_post >= 1 else 0
print(f"True lambda: {lambda_true}, Prior: Gamma({a_prior},{b_prior}) E={a_prior/b_prior:.1f}")
print(f"Posterior: Gamma({a_post},{b_post:.0f}) mean={post_mean:.4f} mode={post_mode:.4f}")

# Natural gradient vs Euclidean gradient for Bernoulli
print("\n=== Natural Gradient vs Euclidean Gradient (Bernoulli) ===")
# Target: p = 0.8. Current: p = 0.5. Gradient ascent on log-likelihood.
p_true = 0.8
X_bern = rng.binomial(1, p_true, 100)
# Natural gradient in eta-space: grad_nat = 1/I(eta) * grad_eta
# For Bernoulli: I(eta) = p(1-p) = sigma(eta)*(1-sigma(eta)) = d^2A/deta^2
eta_nat = 0.0; eta_gd = 0.0   # both start at eta=0 (p=0.5)
lr = 0.5
for step in range(20):
    p_nat = 1/(1+np.exp(-eta_nat)); p_gd  = 1/(1+np.exp(-eta_gd))
    # Score (gradient w.r.t. eta)
    grad_nat = np.mean(X_bern) - p_nat   # dA/deta = p, so score = x_bar - p
    grad_gd  = np.mean(X_bern) - p_gd
    # Fisher for Bernoulli: I(eta) = p(1-p)
    fisher = p_nat * (1 - p_nat)
    nat_grad = grad_nat / fisher         # natural gradient = I^{-1} * score
    eta_nat += lr * nat_grad             # natural gradient step (Newton step)
    eta_gd  += lr * grad_gd             # Euclidean gradient step
print(f"After 20 steps: nat_grad p={1/(1+np.exp(-eta_nat)):.4f}  eucl_grad p={1/(1+np.exp(-eta_gd)):.4f}")
print(f"True p = {p_true}")
```

## Natural Gradient Descent

Standard gradient descent follows steepest ascent in Euclidean parameter space: Δη ∝ ∇_η ℓ(η). But the Euclidean distance between parameters does not reflect distance between distributions — changing η by the same Euclidean step can have very different effects depending on the curvature of A(η).

Natural gradient descent follows steepest ascent in the space of probability distributions (Fisher-Rao metric):
Δη ∝ F(η)⁻¹ ∇_η ℓ(η)

where F(η) = E[(∇_η log p)(∇_η log p)^T] is the Fisher information matrix. For exponential families: F(η) = ∇²A(η) = Cov_η[T(X)] — the Fisher equals the Hessian of the log-partition function.

Therefore, for exponential families, natural gradient = Newton step. Natural gradient converges in O(1) steps for linear models, compared to O(κ) for gradient descent (κ = condition number). KFAC, Shampoo, and other second-order optimisers approximate the Fisher for neural networks.

> **TIP: Maximum Entropy Principle**
>
> Exponential family distributions are exactly those that maximise entropy subject to moment constraints. If we know E[T(X)] = t and want the maximally uninformative distribution otherwise, the solution is p*(x) ∝ h(x) exp(ηᵀ T(x)) where η is chosen so E_p*[T(X)] = t. This justifies: Gaussian (max entropy with fixed mean and variance), Laplace (max entropy with fixed mean absolute deviation), categorical/softmax (max entropy with fixed marginal probabilities). Always use the exponential family member matching your known moment constraints.

> **INFO: Exponential Family and Neural Networks**
>
> Softmax output layers implement the categorical exponential family: p(y=k|x) = exp(ηₖ) / Σⱼ exp(ηⱼ) where ηₖ = wₖᵀ x are the natural parameters and A(η) = log Σⱼ exp(ηⱼ) is the log-softmax denominator. Cross-entropy loss = negative log-likelihood = A(η) − η[y_target]. Training with cross-entropy is MLE in the categorical exponential family — the log-partition function appears in every forward pass as the normalisation computation.

| Distribution | η (natural) | T(x) (sufficient stat) | A(η) (log-partition) | Conjugate prior |
| --- | --- | --- | --- | --- |
| Bernoulli(p) | log(p/(1-p)) | x | log(1+exp(η)) | Beta(α,β) |
| Gaussian(μ,σ²) | (μ/σ², −1/(2σ²)) | (x, x²) | −η₁²/(4η₂)−½log(−2η₂) | Normal-Inverse-Gamma |
| Poisson(λ) | log λ | x | exp(η) = λ | Gamma(α,β) |
| Gamma(α,β) | (α−1, −β) | (log x, x) | log Γ(η₁+1)−(η₁+1)log(−η₂) | — |
| Categorical(p) | log(pₖ/pₖ) for k<K | 1[x=k] each k | log Σ exp(ηₖ) | Dirichlet(α) |

---

## Key Takeaways

- Exponential family: p(x|η) = h(x) exp(ηᵀT(x) − A(η)) unifies Gaussian, Bernoulli, Poisson, Gamma, Dirichlet and many more under one framework.
- The log-partition A(η) is always convex: ∇A(η) = E[T(X)] and ∇²A(η) = Cov[T(X)] ≥ 0 — MLE is a convex optimisation with no local minima.
- MLE for exponential families: set expected sufficient statistics E[T(X)] equal to observed sufficient statistics t̄ = (1/n) Σ T(xᵢ).
- Sufficient statistics T(x) contain all information about η — no other statistic of the same dimension can improve inference (Fisher-Neyman factorisation).
- Conjugate priors for exponential families always exist; Bayesian updates reduce to adding observed sufficient statistics to prior hyperparameters.
- GLMs use exponential family responses with a link function connecting the mean to the linear predictor; all fit via IRLS (Newton-Raphson on log-likelihood).
- Natural gradient = F(η)⁻¹ ∇ℓ = ∇²A(η)⁻¹ ∇ℓ — for exponential families this is the Newton step, converging in O(1) steps for linear models versus O(κ) for gradient descent.
