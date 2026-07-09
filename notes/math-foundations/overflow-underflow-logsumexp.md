---
title: "Overflow, Underflow, and the Log-Sum-Exp Trick"
slug: "overflow-underflow-logsumexp"
description: "Floating-point overflow and underflow in exp-based computations, the log-sum-exp trick derivation, numerically stable softmax and log-softmax, and applications in attention, CTC, HMMs, and beam search."
tags: ["numerical-methods", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiT3ZlcmZsb3cgYW5kIHVuZGVyZmxvdyBhcmUgdGhlIHR3byBtb2RlcyBvZiBjYXRhc3Ryb3BoaWMgZmFpbHVyZSBpbiBmbG9hdGluZy1wb2ludCBjb21wdXRhdGlvbi4gT3ZlcmZsb3cgb2NjdXJzIHdoZW4gYSBjb21wdXRlZCB2YWx1ZSBleGNlZWRzIHRoZSBtYXhpbXVtIHJlcHJlc2VudGFibGUgbnVtYmVyLCBwcm9kdWNpbmcgaW5maW5pdHk7IHVuZGVyZmxvdyBjb2xsYXBzZXMgYSB2YWx1ZSB0byB6ZXJvLiBCb3RoIGFyZSBzaWxlbnQg4oCUIGNvbXB1dGF0aW9uIGNvbnRpbnVlcyBidXQgcHJvZHVjZXMgd3JvbmcgYW5zd2Vycy4gVGhlc2UgZmFpbHVyZXMgYXBwZWFyIGNvbnN0YW50bHkgaW4gTUw6IHNvZnRtYXggd2l0aCBsYXJnZSBsb2dpdHMsIGxvZy1wcm9iYWJpbGl0aWVzIG92ZXIgbG9uZyBzZXF1ZW5jZXMsIG5vcm1hbGl6aW5nLWZsb3cgbG9nLWRldGVybWluYW50cywgQ1RDIGFsaWdubWVudCBtYXJnaW5hbGl6YXRpb24sIGFuZCBhdHRlbnRpb24gb3ZlciBoaWdoLWRpbWVuc2lvbmFsIHF1ZXJpZXMuIFRoZSBsb2ctc3VtLWV4cCB0cmljayBpcyBhcmd1YWJseSB0aGUgc2luZ2xlIG1vc3QgaW1wb3J0YW50IG51bWVyaWNhbCB0ZWNobmlxdWUgaW4gTUwsIHNvbHZpbmcgYm90aCBwcm9ibGVtcyBzaW11bHRhbmVvdXNseSBpbiB0aGUgY3JpdGljYWwgY29udGV4dCBvZiBzb2Z0bWF4IGFuZCBsb2ctcHJvYmFiaWxpdHkgY29tcHV0YXRpb25zLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk92ZXJmbG93IGFuZCBVbmRlcmZsb3cgVGhyZXNob2xkcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIk92ZXJmbG93IG9jY3VycyB3aGVuIGEgY29tcHV0ZWQgdmFsdWUgZXhjZWVkcyB0aGUgbWF4aW11bSByZXByZXNlbnRhYmxlIGZsb2F0aW5nLXBvaW50IG51bWJlci4gRm9yIHRoZSBleHAoKSBmdW5jdGlvbjpcblxuLSBmcDMyOiBleHAoeCkgb3ZlcmZsb3dzIHRvIOKIniBmb3IgeCA+IDg4LjcyIChtYXggZnAzMiDiiYggMy40w5cxMMKz4oG4KVxuLSBmcDE2OiBleHAoeCkgb3ZlcmZsb3dzIGZvciB4ID4gMTEuMDkgKG1heCBmcDE2ID0gNjU1MDQpXG4tIGJmMTY6IHNhbWUgZXhwb25lbnQgcmFuZ2UgYXMgZnAzMiwgc28gdGhyZXNob2xkIOKJiCA4OC43MlxuXG5VbmRlcmZsb3cgb2NjdXJzIHdoZW4gYSB2YWx1ZSBpcyBzbWFsbGVyIHRoYW4gdGhlIG1pbmltdW0gbm9ybWFsIG51bWJlciBhbmQgcm91bmRzIHRvIHplcm8gKHZpYSBzdWJub3JtYWxzIG9yIGRpcmVjdGx5KTpcblxuLSBmcDMyOiBleHAoeCkg4oaSIDAgZm9yIHggPCDiiJI4Ny4zNFxuLSBmcDE2OiBleHAoeCkg4oaSIDAgZm9yIHggPCDiiJI5LjcwXG5cbkluIHNvZnRtYXg6IGlmIGFueSB4X2kgPiA4OC43MiBpbiBmcDMyLCB0aGVuIGV4cCh4X2kpID0g4oieLCB0aGUgZGVub21pbmF0b3IgaXMg4oieLCBhbmQgMC/iiJ4gb3Ig4oieL+KIniA9IE5hTi4gSW4gbG9nLXNvZnRtYXg6IGlmIGFsbCB4X2kgYXJlIHZlcnkgbmVnYXRpdmUsIM6jIGV4cCh4X2opIHVuZGVyZmxvd3MgdG8gMCwgdGhlbiBsb2coMCkgPSDiiJLiiJ4sIG1ha2luZyB0aGUgbG9zcyBpbmZpbml0ZS4gQm90aCBmYWlsdXJlcyBhcmUgZXNwZWNpYWxseSBjb21tb24gaW4gZWFybHkgdHJhaW5pbmcgd2hlbiBsb2dpdHMgYXJlIGxhcmdlIG9yIHdoZW4gdXNpbmcgZnAxNi4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJUaGUgTG9nLVN1bS1FeHAgVHJpY2sifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgbG9nc3VtZXhwIHRyaWNrIHByb3ZpZGVzIG51bWVyaWNhbGx5IHN0YWJsZSBjb21wdXRhdGlvbiBvZiBsb2cozqPhtaIgZXhwKHjhtaIpKSBieSBleHBsb2l0aW5nIHRoZSBmb2xsb3dpbmcgYWxnZWJyYWljIGlkZW50aXR5OlxuXG5sb2cgzqPhtaIgZXhwKHjhtaIpID0gbSArIGxvZyDOo+G1oiBleHAoeOG1oiDiiJIgbSksICB3aGVyZSBtID0gbWF4KHgpXG5cblByb29mOiBsb2cgzqPhtaIgZXhwKHjhtaIpID0gbG9nW2V4cChtKSDDlyDOo+G1oiBleHAoeOG1oiDiiJIgbSldID0gbSArIGxvZyDOo+G1oiBleHAoeOG1oiDiiJIgbSkuXG5cbkJ5IHN1YnRyYWN0aW5nIG0gPSBtYXgoeCkgYmVmb3JlIGV4cG9uZW50aWF0aW5nOlxuLSBUaGUgbWF4aW11bSB0ZXJtIGJlY29tZXMgZXhwKDApID0gMSDigJQgbm8gb3ZlcmZsb3cgcG9zc2libGUuXG4tIEFsbCBvdGhlciB0ZXJtcyBhcmUg4omkIDEg4oCUIG5vIG92ZXJmbG93LlxuLSBUaGUgbWluaW11bSB0ZXJtIGlzIGV4cCh44bWiIOKIkiBtKSDiiaUgZXhwKOKIknJhbmdlKSB3aGVyZSByYW5nZSBpcyB0aGUgZHluYW1pYyByYW5nZSBvZiB4IOKAlCB0eXBpY2FsbHkgbm8gc2V2ZXJlIHVuZGVyZmxvdyB1bmxlc3MgbG9naXRzIHNwYW4gaHVuZHJlZHMgb2YgdW5pdHMuXG5cblRoZSByZXN1bHQgaXMgbWF0aGVtYXRpY2FsbHkgaWRlbnRpY2FsIHRvIHRoZSBvcmlnaW5hbCBidXQgbnVtZXJpY2FsbHkgc2FmZS4gVGhpcyBpcyB0aGUgZm91bmRhdGlvbiBvZiBudW1lcmljYWxseSBzdGFibGUgc29mdG1heCwgbG9nLXNvZnRtYXgsIGFuZCBjcm9zcy1lbnRyb3B5LiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG4jIFByb2JsZW06IG5haXZlIGxvZ3N1bWV4cCBvdmVyZmxvd3NcbmRlZiBuYWl2ZV9sb2dzdW1leHAoeCk6XG4gICAgcmV0dXJuIG5wLmxvZyhucC5zdW0obnAuZXhwKHgpKSlcblxueCA9IG5wLmFycmF5KFsxMDAwLjAsIDEwMDEuMCwgMTAwMi4wXSwgZHR5cGU9bnAuZmxvYXQzMilcbnByaW50KFwiTmFpdmUgbG9nc3VtZXhwOlwiLCBuYWl2ZV9sb2dzdW1leHAoeCkpICAjIGluZiAob3ZlcmZsb3cpXG5cbiMgU29sdXRpb246IHN0YWJsZSBsb2dzdW1leHBcbmRlZiBzdGFibGVfbG9nc3VtZXhwKHgpOlxuICAgIG0gPSBucC5tYXgoeClcbiAgICByZXR1cm4gbSArIG5wLmxvZyhucC5zdW0obnAuZXhwKHggLSBtKSkpXG5cbnByaW50KFwiU3RhYmxlIGxvZ3N1bWV4cDpcIiwgc3RhYmxlX2xvZ3N1bWV4cCh4KSkgICAjIDEwMDIuNDA3NiAoY29ycmVjdClcblxuIyBWZXJpZnk6IG1hdGhlbWF0aWNhbGx5IGlkZW50aWNhbCBmb3Igbm9ybWFsIGlucHV0c1xueDIgPSBucC5hcnJheShbMS4wLCAyLjAsIDMuMF0pXG5wcmludChmXCJuYWl2ZT17bmFpdmVfbG9nc3VtZXhwKHgyKTouNmZ9ICBzdGFibGU9e3N0YWJsZV9sb2dzdW1leHAoeDIpOi42Zn1cIilcblxuIyBQeVRvcmNoIGJ1aWx0LWluICh1c2UgdGhpcyBpbiBwcm9kdWN0aW9uKVxucHJpbnQoXCJ0b3JjaC5sb2dzdW1leHA6XCIsIHRvcmNoLmxvZ3N1bWV4cCh0b3JjaC50ZW5zb3IoeCksIGRpbT0wKSkgICMgMTAwMi40MDc2XG5cbiMgVW5kZXJmbG93OiBuYWl2ZSBsb2ctc29mdG1heCBmYWlscyBmb3IgdmVyeSBuZWdhdGl2ZSBsb2dpdHNcbnhfbmVnID0gbnAuYXJyYXkoWy0xMDAwLjAsIC0xMDAxLjAsIC0xMDAyLjBdLCBkdHlwZT1ucC5mbG9hdDMyKVxucHJpbnQoXCJcXG4tLS0gVW5kZXJmbG93IGRlbW8gLS0tXCIpXG5wcmludChcIm5wLmV4cCh4X25lZyk6XCIsIG5wLmV4cCh4X25lZykpICAgICAjIFswLiAwLiAwLl0g4oCUIGFsbCB1bmRlcmZsb3cgdG8gMFxucHJpbnQoXCJuYWl2ZSBsb2coc3VtKGV4cCkpOlwiLCBucC5sb2cobnAuc3VtKG5wLmV4cCh4X25lZykpKSkgICMgLWluZlxucHJpbnQoXCJzdGFibGVfbG9nc3VtZXhwOlwiLCBzdGFibGVfbG9nc3VtZXhwKHhfbmVnKSkgICMgLTEwMDAuNDA3NiAoY29ycmVjdClcblxuIyBOdW1lcmljYWxseSBzdGFibGUgc29mdG1heFxuZGVmIHN0YWJsZV9zb2Z0bWF4KHgpOlxuICAgIGUgPSBucC5leHAoeCAtIG5wLm1heCh4KSlcbiAgICByZXR1cm4gZSAvIGUuc3VtKClcblxucHJpbnQoXCJcXG4tLS0gU3RhYmxlIHNvZnRtYXggLS0tXCIpXG5wcmludChcInN0YWJsZV9zb2Z0bWF4KFsxMDAwLDEwMDEsMTAwMl0pOlwiLCBucC5yb3VuZChzdGFibGVfc29mdG1heCh4KSwgNCkpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTnVtZXJpY2FsbHkgU3RhYmxlIFNvZnRtYXggYW5kIExvZy1Tb2Z0bWF4In0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3RhYmxlIHNvZnRtYXggPSBzdWJ0cmFjdCBtYXggYmVmb3JlIGV4cG9uZW50aWF0aW5nOlxuXG5zb2Z0bWF4KHgp4bWiID0gZXhwKHjhtaIg4oiSIG0pIC8gzqPisbwgZXhwKHjisbwg4oiSIG0pLCAgbSA9IG1heCh4KVxuXG5UaGlzIGlzIG1hdGhlbWF0aWNhbGx5IGVxdWl2YWxlbnQgdG8gdGhlIG9yaWdpbmFsIGJlY2F1c2UgYm90aCBudW1lcmF0b3IgYW5kIGRlbm9taW5hdG9yIGFyZSBtdWx0aXBsaWVkIGJ5IGV4cCjiiJJtKSwgd2hpY2ggY2FuY2Vscy4gVGhlIG9wZXJhdGlvbiBjb3N0cyBvbmUgYWRkaXRpb25hbCBwYXNzIG92ZXIgeCAodG8gZmluZCB0aGUgbWF4aW11bSkgYnV0IGlzIGVudGlyZWx5IHNhZmUuXG5cblN0YWJsZSBsb2ctc29mdG1heCBidWlsZHMgb24gc3RhYmxlIGxvZ3N1bWV4cDpcblxubG9nIHNvZnRtYXgoeCnhtaIgPSB44bWiIOKIkiBsb2dzdW1leHAoeCkgPSB44bWiIOKIkiBtIOKIkiBsb2cgzqPisbwgZXhwKHjisbwg4oiSIG0pXG5cbk5vdGUgdGhhdCB0aGlzIGlzIGp1c3Qgc3VidHJhY3Rpb24g4oCUIG5vIGV4cCBvbiB0aGUgb3V0cHV0IHNpZGUsIHNvIG5vIG92ZXJmbG93IG9yIHVuZGVyZmxvdyBvbiB0aGUgZmluYWwgdmFsdWVzLiBUaGUgb25seSBleHAgY2FsbHMgYXJlIGluIGNvbXB1dGluZyDOo+KxvCBleHAoeOKxvCDiiJIgbSksIHdoaWNoIGlzIHNhZmUgYmVjYXVzZSBhbGwgYXJndW1lbnRzIGFyZSDiiaQgMC5cblxuQ3Jvc3MtZW50cm9weSBsb3NzID0gTkxMKGxvZ19zb2Z0bWF4KGxvZ2l0cyksIHRhcmdldHMpLiBQeVRvcmNoJ3MgRi5jcm9zc19lbnRyb3B5IGNvbWJpbmVzIGJvdGggc3RlcHMgaW4gYSBzaW5nbGUgbnVtZXJpY2FsbHkgc3RhYmxlIGZ1c2VkIG9wZXJhdGlvbi4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBTdGFibGUgbG9nLXNvZnRtYXggZnJvbSBzY3JhdGNoXG5kZWYgc3RhYmxlX2xvZ19zb2Z0bWF4KHgpOlxuICAgIFwiXCJcImxvZyhleHAoeGkpIC8gc3VtKGV4cCh4aikpKSA9IHhpIC0gbG9nc3VtZXhwKHgpLlwiXCJcIlxuICAgIG0gPSB4Lm1heCgpXG4gICAgbG9nX3N1bSA9IG0gKyBucC5sb2cobnAuc3VtKG5wLmV4cCh4IC0gbSkpKVxuICAgIHJldHVybiB4IC0gbG9nX3N1bVxuXG4jIERlbW9uc3RyYXRpb24gd2l0aCBleHRyZW1lIGxvZ2l0c1xubG9naXRzX25wID0gbnAuYXJyYXkoWzEwMDAuMCwgMTAwMS4wLCAxMDAyLjBdLCBkdHlwZT1ucC5mbG9hdDMyKVxubG9naXRzX3QgID0gdG9yY2gudGVuc29yKGxvZ2l0c19ucClcblxucHJpbnQoXCI9PT0gTG9nLVNvZnRtYXggQ29tcGFyaXNvbiA9PT1cIilcbiMgTmFpdmU6IGxvZyhzb2Z0bWF4KHgpKSDigJQgdHdvLXN0ZXAsIHVuc3RhYmxlXG5uYWl2ZV9zbSAgPSBucC5leHAobG9naXRzX25wKSAvIG5wLnN1bShucC5leHAobG9naXRzX25wKSkgICMgaW5mL2luZiA9IG5hblxucHJpbnQoXCJuYWl2ZSBzb2Z0bWF4OlwiLCBuYWl2ZV9zbSlcblxuIyBTdGFibGUgZnJvbSBzY3JhdGNoXG5wcmludChcInN0YWJsZSBsb2dfc29mdG1heDpcIiwgc3RhYmxlX2xvZ19zb2Z0bWF4KGxvZ2l0c19ucCkpXG5cbiMgUHlUb3JjaCBGLmxvZ19zb2Z0bWF4IChzdGFibGUgYnkgZGVzaWduKVxucHJpbnQoXCJGLmxvZ19zb2Z0bWF4OlwiLCBGLmxvZ19zb2Z0bWF4KGxvZ2l0c190LCBkaW09MCkubnVtcHkoKSlcblxuIyBDcm9zcy1lbnRyb3B5OiBhbHdheXMgdXNlIEYuY3Jvc3NfZW50cm9weSwgbm90IG1hbnVhbCBzb2Z0bWF4IC0+IGxvZyAtPiBOTExcbnByaW50KFwiXFxuPT09IENyb3NzLUVudHJvcHkgU3RhYmlsaXR5ID09PVwiKVxuYmF0Y2hfbG9naXRzID0gdG9yY2gudGVuc29yKFtbMTAwMC4wLCAxMDAxLjAsIDEwMDIuMF1dKVxudGFyZ2V0ICAgICAgID0gdG9yY2gudGVuc29yKFsyXSkgICMgY2xhc3MgMiBpcyBjb3JyZWN0XG5cbiMgV1JPTkc6IG1hbnVhbCBzb2Z0bWF4IC0+IGxvZyAtPiBOTExcbnByb2JzID0gdG9yY2guc29mdG1heChiYXRjaF9sb2dpdHMsIGRpbT0xKSAgIyBbMCwgMCwgbmFuXSBvciBzaW1pbGFyXG5sb3NzX3dyb25nID0gLXRvcmNoLmxvZyhwcm9ic1swLCB0YXJnZXRbMF1dKVxucHJpbnQoZlwiV3JvbmcgKHNvZnRtYXgtPmxvZy0+TkxMKToge2xvc3Nfd3JvbmcuaXRlbSgpfVwiKSAgIyBuYW4gb3IgaW5mXG5cbiMgQ09SUkVDVDogRi5jcm9zc19lbnRyb3B5IChmdXNlZCBzdGFibGUgb3BlcmF0aW9uKVxubG9zc19jb3JyZWN0ID0gRi5jcm9zc19lbnRyb3B5KGJhdGNoX2xvZ2l0cywgdGFyZ2V0KVxucHJpbnQoZlwiQ29ycmVjdCAoRi5jcm9zc19lbnRyb3B5KToge2xvc3NfY29ycmVjdC5pdGVtKCk6LjZmfVwiKSAgIyB+MC40MDc2XG5cbiMgVmVyaWZ5OiBzYW1lIHJlc3VsdCB3aXRoIG5vcm1hbCBsb2dpdHNcbm5vcm1hbF9sb2dpdHMgPSB0b3JjaC50ZW5zb3IoW1sxLjAsIDIuMCwgMy4wXV0pXG5wcmludChcIlxcbk5vcm1hbCBsb2dpdHMgY29tcGFyaXNvbjpcIilcbnByaW50KGZcIiAgTWFudWFsOiAgICAgICAgIHstdG9yY2gubG9nKHRvcmNoLnNvZnRtYXgobm9ybWFsX2xvZ2l0cywgZGltPTEpWzAsIDJdKS5pdGVtKCk6LjZmfVwiKVxucHJpbnQoZlwiICBGLmNyb3NzX2VudHJvcHk6e0YuY3Jvc3NfZW50cm9weShub3JtYWxfbG9naXRzLCB0YXJnZXQpLml0ZW0oKTouNmZ9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiVmFyaWFudHMgYW5kIFNwZWNpYWwgQ2FzZXMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJMb2ctZG9tYWluIGFyaXRobWV0aWMgaXMgbmVlZGVkIHdoZW5ldmVyIG11bHRpcGx5aW5nIG1hbnkgcHJvYmFiaWxpdGllcywgc2luY2UgcHJvZHVjdHMgdW5kZXJmbG93IHJhcGlkbHkuIEZvciBhIHNlcXVlbmNlIG9mIFQgdG9rZW5zIGVhY2ggd2l0aCBwcm9iYWJpbGl0eSB+MC4xLCB0aGUgam9pbnQgcHJvYmFiaWxpdHkgaXMgMC4xXlQgd2hpY2ggdW5kZXJmbG93cyB0byAwIGZvciBUID4gNDUgaW4gZnAzMi4gTG9nLWRvbWFpbjogc3VtIGxvZy1wcm9iYWJpbGl0aWVzIGluc3RlYWQuXG5cblRlbXBlcmF0dXJlIHNjYWxpbmcgc29mdG1heCh4L1QpOlxuLSBUIDwgMSAoc2hhcnBlbmluZyk6IGRpdmlkZXMgYnkgVCA8IDEsIHdoaWNoIG11bHRpcGxpZXMgbG9naXQgbWFnbml0dWRlcyBieSAxL1Qg4oCUIG1ha2luZyBvdmVyZmxvdyBtb3JlIGxpa2VseS4gQWx3YXlzIGFwcGx5IHRoZSBtYXgtc2hpZnQgdHJpY2suXG4tIFQgPiAxIChzb2Z0ZW5pbmcpOiByZWR1Y2VzIGxvZ2l0IG1hZ25pdHVkZXMsIGxlc3Mgb3ZlcmZsb3cgcmlzay5cblxubG9nLXN1bS1leHAgd2l0aCB0d28gdGVybXM6IGxvZyhleHAoYSkgKyBleHAoYikpID0gbWF4KGEsYikgKyBsb2coMSArIGV4cCjiiJJ8YeKIkmJ8KSkuIFRoaXMgaXMgdGhlIGxvZ2FkZGV4cCBmdW5jdGlvbiBpbiBudW1weSBhbmQgbG9nMXAoZXhwKHgpKSBmb3Igc29mdHBsdXMuIEJvdGggYXBwZWFyIGZyZXF1ZW50bHkgaW4gcHJvYmFiaWxpc3RpYyBtb2RlbHMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTG9nLURvbWFpbiBITU0gRm9yd2FyZCBBbGdvcml0aG0ifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgSE1NIGZvcndhcmQgYWxnb3JpdGhtIGNvbXB1dGVzIHRoZSBwcm9iYWJpbGl0eSBvZiBhbiBvYnNlcnZlZCBzZXF1ZW5jZSBieSBtYXJnaW5hbGl6aW5nIG92ZXIgYWxsIGhpZGRlbiBzdGF0ZSBzZXF1ZW5jZXMuIFRoZSBwcm9kdWN0IG9mIFQgZW1pc3Npb24gYW5kIHRyYW5zaXRpb24gcHJvYmFiaWxpdGllcyB1bmRlcmZsb3dzIHRvIHplcm8gZm9yIGxvbmcgc2VxdWVuY2VzLiBUaGUgbG9nLWRvbWFpbiBmb3J3YXJkIGFsZ29yaXRobSBtYWludGFpbnMgbG9nIM6xX3QocykgPSBsb2cgUCh44oKBLC4uLix44oKcLCBzdGF0ZV90ID0gcykgYW5kIHBlcmZvcm1zIGFsbCBzdW1tYXRpb25zIHVzaW5nIGxvZ3N1bWV4cDpcblxubG9nIM6xX3QocycpID0gbG9nIFAoeOKCnCB8IHMnKSArIGxvZ3N1bWV4cF9zW2xvZyDOsV97dC0xfShzKSArIGxvZyBBKHPihpJzJyldXG5cblRoaXMgaXMgTyhUIMOXIFPCsikgaW4gdGltZSAoc2FtZSBhcyBzdGFuZGFyZCBmb3J3YXJkIGFsZ29yaXRobSkgYnV0IHN0YWJsZSBmb3Igc2VxdWVuY2VzIG9mIGFueSBsZW5ndGguIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbG9nX2ZvcndhcmRfaG1tKGxvZ19lbWlzc2lvbiwgbG9nX3RyYW5zaXRpb24sIGxvZ19pbml0KTpcbiAgICBcIlwiXCJcbiAgICBMb2ctZG9tYWluIEhNTSBmb3J3YXJkIGFsZ29yaXRobSAobnVtZXJpY2FsbHkgc3RhYmxlKS5cbiAgICBsb2dfZW1pc3Npb246ICAgKFQsIFMpIGxvZyBQKHhfdCB8IHN0YXRlX3MpXG4gICAgbG9nX3RyYW5zaXRpb246IChTLCBTKSBsb2cgUChzdGF0ZV9zJyB8IHN0YXRlX3MpXG4gICAgbG9nX2luaXQ6ICAgICAgIChTLCkgICBsb2cgUChzdGF0ZV9zIGF0IHQ9MClcbiAgICBSZXR1cm5zOiBsb2cgUChvYnNlcnZhdGlvbiBzZXF1ZW5jZSlcbiAgICBcIlwiXCJcbiAgICBULCBTID0gbG9nX2VtaXNzaW9uLnNoYXBlXG4gICAgbG9nX2FscGhhID0gbG9nX2luaXQgKyBsb2dfZW1pc3Npb25bMF0gICMgKFMsKSDigJQgaW5pdCBhdCB0PTBcblxuICAgIGZvciB0IGluIHJhbmdlKDEsIFQpOlxuICAgICAgICAjIGxvZ19hbHBoYVtzJ10gPSBsb2cgc3VtX3MgZXhwKGxvZ19hbHBoYVtzXSArIGxvZ19BW3MscyddKVxuICAgICAgICAjIFNoYXBlIGJyb2FkY2FzdDogbG9nX2FscGhhIChTLDEpICsgbG9nX3RyYW5zaXRpb24gKFMsUykgLT4gKFMsUylcbiAgICAgICAgbG9nX3RyYW5zX2NvbnRyaWIgPSBsb2dfYWxwaGFbOiwgTm9uZV0gKyBsb2dfdHJhbnNpdGlvbiAgIyAoUywgUylcbiAgICAgICAgbG9nX2FscGhhID0gbnAubG9nYWRkZXhwLnJlZHVjZShsb2dfdHJhbnNfY29udHJpYiwgYXhpcz0wKSArIGxvZ19lbWlzc2lvblt0XVxuXG4gICAgIyBUb3RhbCBsb2cgcHJvYmFiaWxpdHk6IHN1bSBvdmVyIGZpbmFsIHN0YXRlc1xuICAgIHJldHVybiBucC5sb2dhZGRleHAucmVkdWNlKGxvZ19hbHBoYSlcblxuIyBEZW1vOiAzLXN0YXRlIEhNTSwgNTAtc3RlcCBzZXF1ZW5jZVxubnAucmFuZG9tLnNlZWQoNDIpXG5TLCBUID0gMywgNTBcbmxvZ19BID0gbnAubG9nKG5wLmFycmF5KFtbMC43LCAwLjIsIDAuMV0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBbMC4xLCAwLjYsIDAuM10sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBbMC4yLCAwLjMsIDAuNV1dKSlcbmxvZ19CID0gbnAucmFuZG9tLnJhbmRuKFQsIFMpIC0gbnAubG9nKFMpICAjIHJhbmRvbSBlbWlzc2lvbiBsb2ctcHJvYnNcbmxvZ19waSA9IG5wLmxvZyhucC5vbmVzKFMpIC8gUylcblxubG9nX3Byb2IgPSBsb2dfZm9yd2FyZF9obW0obG9nX0IsIGxvZ19BLCBsb2dfcGkpXG5wcmludChmXCJMb2cgUChzZXF1ZW5jZSk6IHtsb2dfcHJvYjouNGZ9XCIpXG5wcmludChmXCJQKHNlcXVlbmNlKSA9IGV4cCh7bG9nX3Byb2I6LjRmfSkgPSB7bnAuZXhwKGxvZ19wcm9iKTouNGV9XCIpXG4jIFdpdGhvdXQgbG9nLWRvbWFpbiwgUCB3b3VsZCB1bmRlcmZsb3cgdG8gMCBmb3IgVD01MCBzdGVwcyJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQ29tbW9uIG1pc3Rha2VzIHdpdGggb3ZlcmZsb3cvdW5kZXJmbG93OlxuXG4xLiAqKk1hbnVhbCBzb2Z0bWF4IGJlZm9yZSBsb2cqKjogY29tcHV0aW5nIGxvZyhzb2Z0bWF4KHgpKSBpbiB0d28gc3RlcHMgaW5zdGVhZCBvZiB1c2luZyBsb2dfc29mdG1heC4gVGhlIGludGVybWVkaWF0ZSBzb2Z0bWF4IG1heSBwcm9kdWNlIE5hTiB0aGF0IGxvZyB0aGVuIHByb3BhZ2F0ZXMuXG5cbjIuICoqRm9yZ2V0dGluZyBtYXgtc2hpZnQgd2hlbiBzY2FsaW5nKio6IGRpdmlkaW5nIGxvZ2l0cyBieSB0ZW1wZXJhdHVyZSA8IDEgYmVmb3JlIHNvZnRtYXggaW5mbGF0ZXMgbWFnbml0dWRlcy4gQWx3YXlzIGFwcGx5IHRlbXBlcmF0dXJlIGZpcnN0LCB0aGVuIHVzZSBzdGFibGUgc29mdG1heC5cblxuMy4gKipVc2luZyBmcDE2IGZvciBhdHRlbnRpb24gd2l0aG91dCBtYXgtc2hpZnQqKjogYXR0ZW50aW9uIHNjb3JlcyBRQEteVC/iiJpkIGNhbiBlYXNpbHkgZXhjZWVkIDExIGluIGZwMTYsIGNhdXNpbmcgb3ZlcmZsb3cuIFVzZSBiZjE2IG9yIGVuc3VyZSBGbGFzaEF0dGVudGlvbidzIHRpbGVkIHNvZnRtYXggaXMgYWN0aXZlLlxuXG40LiAqKkFjY3VtdWxhdGluZyBwcm9iYWJpbGl0aWVzIGFjcm9zcyB0b2tlbnMqKjogbXVsdGlwbHlpbmcgcGVyLXRva2VuIHByb2JhYmlsaXRpZXMgaW5zdGVhZCBvZiBhZGRpbmcgbG9nLXByb2JhYmlsaXRpZXMgY2F1c2VzIHJhcGlkIHVuZGVyZmxvdyBmb3Igc2VxdWVuY2VzIGxvbmdlciB0aGFuIH41MCB0b2tlbnMgaW4gZnAzMi4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQcmFjdGljYWwgR3VpZGFuY2UifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJSdWxlcyBmb3IgbnVtZXJpY2FsbHkgc2FmZSBjb21wdXRhdGlvbjpcblxuLSAqKkFsd2F5cyB1c2UgRi5jcm9zc19lbnRyb3B5KiogaW4gUHlUb3JjaCwgbmV2ZXIgbWFudWFsIHNvZnRtYXgg4oaSIGxvZyDihpIgTkxMLlxuLSAqKlVzZSB0b3JjaC5sb2dzdW1leHAqKiByYXRoZXIgdGhhbiBpbXBsZW1lbnRpbmcgbG9nc3VtZXhwIG1hbnVhbGx5LlxuLSAqKkluIGN1c3RvbSBub3JtYWxpemluZy1mbG93IGltcGxlbWVudGF0aW9ucyoqLCBjb21wdXRlIGxvZy1kZXRlcm1pbmFudHMgYXMgc3VtcyBvZiBsb2d8ZGlhZyhKKXwsIG5vdCBwcm9kdWN0cyBvZiB8ZGlhZyhKKXwuXG4tICoqRm9yIGJlYW0gc2VhcmNoKiosIG1haW50YWluIGxvZy1wcm9iYWJpbGl0aWVzIGFuZCBhZGQgcGVyLXN0ZXAgbG9nLXByb2JzOyBvbmx5IGNvbnZlcnQgdG8gcHJvYmFiaWxpdHkgZm9yIGZpbmFsIG91dHB1dC5cbi0gKipWYWxpZGF0ZSB3aXRoIHNtYWxsIHRlc3QgY2FzZXMqKjogdmVyaWZ5IHRoYXQgbmFpdmUgYW5kIHN0YWJsZSBpbXBsZW1lbnRhdGlvbnMgYWdyZWUgb24gbm9ybWFsIGxvZ2l0cyBiZWZvcmUgdGVzdGluZyBvbiBleHRyZW1lIGlucHV0cy4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidmFyaWFudCI6ICJ3YXJuaW5nIiwgInRpdGxlIjogIlRlbXBlcmF0dXJlIDwgMSBBbXBsaWZpZXMgT3ZlcmZsb3cgUmlzayIsICJjb250ZW50IjogIlRlbXBlcmF0dXJlIHNjYWxpbmcgY29tcHV0ZXMgc29mdG1heCh4L1QpLiBGb3IgVCA8IDEgKHNoYXJwZW5pbmcpLCBsb2dpdHMgYXJlIG11bHRpcGxpZWQgYnkgMS9ULCBpbmNyZWFzaW5nIHRoZWlyIG1hZ25pdHVkZS4gV2l0aCBsb2dpdHMgYWxyZWFkeSBuZWFyIHRoZSBmcDMyIG92ZXJmbG93IHRocmVzaG9sZCAofjg4KSwgZGl2aWRpbmcgYnkgVCA9IDAuMSBnaXZlcyBsb2dpdHMgbmVhciA4ODAg4oCUIGNlcnRhaW4gb3ZlcmZsb3cuIEFsd2F5cyBhcHBseSB0aGUgbWF4LXNoaWZ0IHRyaWNrIGV4cGxpY2l0bHkgd2hlbiB1c2luZyB0ZW1wZXJhdHVyZXMgb3RoZXIgdGhhbiAxLjAsIG9yIHVzZSBGLnNvZnRtYXgobG9naXRzIC8gVCkgd2hpY2ggZG9lcyBzbyBpbnRlcm5hbGx5LiJ9LCB7InR5cGUiOiAiY2FsbG91dCIsICJ2YXJpYW50IjogInRpcCIsICJ0aXRsZSI6ICJMb2ctRG9tYWluIEFyaXRobWV0aWMgZm9yIExvbmcgU2VxdWVuY2VzIiwgImNvbnRlbnQiOiAiV2hlbiBjb21wdXRpbmcgcHJvYmFiaWxpdHkgb2YgYSBzZXF1ZW5jZSAocHJvZHVjdCBvZiBjb25kaXRpb25hbHMpLCBhbHdheXMgd29yayBpbiBsb2ctZG9tYWluOiBhZGQgbG9nLXByb2JhYmlsaXRpZXMgaW5zdGVhZCBvZiBtdWx0aXBseWluZyBwcm9iYWJpbGl0aWVzLiBGb3IgTiB0b2tlbnMgZWFjaCB3aXRoIHByb2JhYmlsaXR5IH4wLjEsIGpvaW50IHByb2JhYmlsaXR5IDAuMV5OIHVuZGVyZmxvd3MgZm9yIE4gPiA0NSBpbiBmcDMyLiBJbiBsb2ctZG9tYWluLCBOIMOXIGxvZygwLjEpIOKJiCDiiJJOIMOXIDIuMzAzIHJlbWFpbnMgcGVyZmVjdGx5IHJlcHJlc2VudGFibGUgZm9yIGFueSBOLiJ9LCB7InR5cGUiOiAidGFibGUiLCAiaGVhZGVycyI6IFsiQ29tcHV0YXRpb24iLCAiTmFpdmUgRmFpbHVyZSIsICJTdGFibGUgU29sdXRpb24iXSwgInJvd3MiOiBbWyJsb2dzdW1leHAoeCkiLCAiZXhwIG92ZXJmbG93IiwgIm0gKyBsb2cgzqMgZXhwKHgtbSksIG09bWF4KHgpIl0sIFsic29mdG1heCh4KSIsICJleHAgb3ZlcmZsb3cg4oaSIE5hTiIsICJzb2Z0bWF4KHggLSBtYXgoeCkpIl0sIFsibG9nX3NvZnRtYXgoeCkiLCAibG9nKDApIHdoZW4gZGVub21pbmF0b3IgdW5kZXJmbG93cyIsICJ4IC0gbG9nc3VtZXhwKHgpIl0sIFsiY3Jvc3NfZW50cm9weSIsICJjaGFpbiBvZiBpbnN0YWJpbGl0aWVzIiwgIkYuY3Jvc3NfZW50cm9weSAoZnVzZWQpIl0sIFsic2VxdWVuY2UgcHJvYmFiaWxpdHkiLCAicHJvZHVjdCB1bmRlcmZsb3dzIiwgInN1bSBvZiBsb2ctcHJvYnMiXSwgWyJITU0gZm9yd2FyZCIsICLOsV90IOKGkiAwIGZvciBsb25nIFQiLCAibG9nLWRvbWFpbiB3aXRoIGxvZ2FkZGV4cCJdXX0sIHsidHlwZSI6ICJkaXZpZGVyIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2V5IFRha2Vhd2F5cyJ9LCB7InR5cGUiOiAibGlzdCIsICJvcmRlcmVkIjogZmFsc2UsICJpdGVtcyI6IFsiZXhwKHgpIG92ZXJmbG93cyBpbiBmcDMyIGZvciB4ID4gODguNzIgYW5kIHVuZGVyZmxvd3MgdG8gMCBmb3IgeCA8IOKIkjg3LjM0OyBmcDE2IHRocmVzaG9sZHMgYXJlIG11Y2ggdGlnaHRlciAowrExMSkuIiwgIlRoZSBsb2ctc3VtLWV4cCB0cmljayBsb2cgzqMgZXhwKHjhtaIpID0gbSArIGxvZyDOoyBleHAoeOG1ouKIkm0pIHdpdGggbSA9IG1heCh4KSBpcyBtYXRoZW1hdGljYWxseSBpZGVudGljYWwgYnV0IG51bWVyaWNhbGx5IHNhZmUuIiwgIlN0YWJsZSBzb2Z0bWF4IHN1YnRyYWN0cyBtYXggYmVmb3JlIGV4cG9uZW50aWF0aW5nOyBzdGFibGUgbG9nLXNvZnRtYXggY29tcHV0ZXMgeOG1oiDiiJIgbG9nc3VtZXhwKHgpLiIsICJBbHdheXMgdXNlIEYuY3Jvc3NfZW50cm9weSAoUHlUb3JjaCkg4oCUIGl0IGZ1c2VzIGxvZ19zb2Z0bWF4ICsgTkxMIGluIG9uZSBzdGFibGUgb3BlcmF0aW9uLiIsICJUZW1wZXJhdHVyZSBUIDwgMSBhbXBsaWZpZXMgbG9naXQgbWFnbml0dWRlcyBieSAxL1QsIGluY3JlYXNpbmcgb3ZlcmZsb3cgcmlzayDigJQgYWx3YXlzIHVzZSB0aGUgbWF4LXNoaWZ0IHRyaWNrLiIsICJGb3IgbG9uZyBzZXF1ZW5jZXMsIG1haW50YWluIGFuZCBhY2N1bXVsYXRlIGxvZy1wcm9iYWJpbGl0aWVzIGluc3RlYWQgb2YgbXVsdGlwbHlpbmcgcHJvYmFiaWxpdGllcyAod2hpY2ggdW5kZXJmbG93IHBhc3QgfjQ1IHRva2VucyBpbiBmcDMyKS4iLCAiVGhlIGxvZy1kb21haW4gZm9yd2FyZCBhbGdvcml0aG0gKHVzaW5nIGxvZ2FkZGV4cCByZWR1Y3Rpb25zKSBlbmFibGVzIHN0YWJsZSBITU0gaW5mZXJlbmNlIG92ZXIgYXJiaXRyYXJpbHkgbG9uZyBzZXF1ZW5jZXMuIl19XQ=="
---
# Overflow, Underflow, and the Log-Sum-Exp Trick

Overflow and underflow are the two modes of catastrophic failure in floating-point computation. Overflow occurs when a computed value exceeds the maximum representable number, producing infinity; underflow collapses a value to zero. Both are silent — computation continues but produces wrong answers. These failures appear constantly in ML: softmax with large logits, log-probabilities over long sequences, normalizing-flow log-determinants, CTC alignment marginalization, and attention over high-dimensional queries. The log-sum-exp trick is arguably the single most important numerical technique in ML, solving both problems simultaneously in the critical context of softmax and log-probability computations.

## Overflow and Underflow Thresholds

Overflow occurs when a computed value exceeds the maximum representable floating-point number. For the exp() function:

- fp32: exp(x) overflows to ∞ for x > 88.72 (max fp32 ≈ 3.4×10³⁸)
- fp16: exp(x) overflows for x > 11.09 (max fp16 = 65504)
- bf16: same exponent range as fp32, so threshold ≈ 88.72

Underflow occurs when a value is smaller than the minimum normal number and rounds to zero (via subnormals or directly):

- fp32: exp(x) → 0 for x < −87.34
- fp16: exp(x) → 0 for x < −9.70

In softmax: if any x_i > 88.72 in fp32, then exp(x_i) = ∞, the denominator is ∞, and 0/∞ or ∞/∞ = NaN. In log-softmax: if all x_i are very negative, Σ exp(x_j) underflows to 0, then log(0) = −∞, making the loss infinite. Both failures are especially common in early training when logits are large or when using fp16.

## The Log-Sum-Exp Trick

The logsumexp trick provides numerically stable computation of log(Σᵢ exp(xᵢ)) by exploiting the following algebraic identity:

log Σᵢ exp(xᵢ) = m + log Σᵢ exp(xᵢ − m),  where m = max(x)

Proof: log Σᵢ exp(xᵢ) = log[exp(m) × Σᵢ exp(xᵢ − m)] = m + log Σᵢ exp(xᵢ − m).

By subtracting m = max(x) before exponentiating:
- The maximum term becomes exp(0) = 1 — no overflow possible.
- All other terms are ≤ 1 — no overflow.
- The minimum term is exp(xᵢ − m) ≥ exp(−range) where range is the dynamic range of x — typically no severe underflow unless logits span hundreds of units.

The result is mathematically identical to the original but numerically safe. This is the foundation of numerically stable softmax, log-softmax, and cross-entropy.

```python
import numpy as np
import torch
import torch.nn.functional as F

# Problem: naive logsumexp overflows
def naive_logsumexp(x):
    return np.log(np.sum(np.exp(x)))

x = np.array([1000.0, 1001.0, 1002.0], dtype=np.float32)
print("Naive logsumexp:", naive_logsumexp(x))  # inf (overflow)

# Solution: stable logsumexp
def stable_logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))

print("Stable logsumexp:", stable_logsumexp(x))   # 1002.4076 (correct)

# Verify: mathematically identical for normal inputs
x2 = np.array([1.0, 2.0, 3.0])
print(f"naive={naive_logsumexp(x2):.6f}  stable={stable_logsumexp(x2):.6f}")

# PyTorch built-in (use this in production)
print("torch.logsumexp:", torch.logsumexp(torch.tensor(x), dim=0))  # 1002.4076

# Underflow: naive log-softmax fails for very negative logits
x_neg = np.array([-1000.0, -1001.0, -1002.0], dtype=np.float32)
print("\n--- Underflow demo ---")
print("np.exp(x_neg):", np.exp(x_neg))     # [0. 0. 0.] — all underflow to 0
print("naive log(sum(exp)):", np.log(np.sum(np.exp(x_neg))))  # -inf
print("stable_logsumexp:", stable_logsumexp(x_neg))  # -1000.4076 (correct)

# Numerically stable softmax
def stable_softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()

print("\n--- Stable softmax ---")
print("stable_softmax([1000,1001,1002]):", np.round(stable_softmax(x), 4))
```

## Numerically Stable Softmax and Log-Softmax

Stable softmax = subtract max before exponentiating:

softmax(x)ᵢ = exp(xᵢ − m) / Σⱼ exp(xⱼ − m),  m = max(x)

This is mathematically equivalent to the original because both numerator and denominator are multiplied by exp(−m), which cancels. The operation costs one additional pass over x (to find the maximum) but is entirely safe.

Stable log-softmax builds on stable logsumexp:

log softmax(x)ᵢ = xᵢ − logsumexp(x) = xᵢ − m − log Σⱼ exp(xⱼ − m)

Note that this is just subtraction — no exp on the output side, so no overflow or underflow on the final values. The only exp calls are in computing Σⱼ exp(xⱼ − m), which is safe because all arguments are ≤ 0.

Cross-entropy loss = NLL(log_softmax(logits), targets). PyTorch's F.cross_entropy combines both steps in a single numerically stable fused operation.

```python
import torch
import torch.nn.functional as F
import numpy as np

# Stable log-softmax from scratch
def stable_log_softmax(x):
    """log(exp(xi) / sum(exp(xj))) = xi - logsumexp(x)."""
    m = x.max()
    log_sum = m + np.log(np.sum(np.exp(x - m)))
    return x - log_sum

# Demonstration with extreme logits
logits_np = np.array([1000.0, 1001.0, 1002.0], dtype=np.float32)
logits_t  = torch.tensor(logits_np)

print("=== Log-Softmax Comparison ===")
# Naive: log(softmax(x)) — two-step, unstable
naive_sm  = np.exp(logits_np) / np.sum(np.exp(logits_np))  # inf/inf = nan
print("naive softmax:", naive_sm)

# Stable from scratch
print("stable log_softmax:", stable_log_softmax(logits_np))

# PyTorch F.log_softmax (stable by design)
print("F.log_softmax:", F.log_softmax(logits_t, dim=0).numpy())

# Cross-entropy: always use F.cross_entropy, not manual softmax -> log -> NLL
print("\n=== Cross-Entropy Stability ===")
batch_logits = torch.tensor([[1000.0, 1001.0, 1002.0]])
target       = torch.tensor([2])  # class 2 is correct

# WRONG: manual softmax -> log -> NLL
probs = torch.softmax(batch_logits, dim=1)  # [0, 0, nan] or similar
loss_wrong = -torch.log(probs[0, target[0]])
print(f"Wrong (softmax->log->NLL): {loss_wrong.item()}")  # nan or inf

# CORRECT: F.cross_entropy (fused stable operation)
loss_correct = F.cross_entropy(batch_logits, target)
print(f"Correct (F.cross_entropy): {loss_correct.item():.6f}")  # ~0.4076

# Verify: same result with normal logits
normal_logits = torch.tensor([[1.0, 2.0, 3.0]])
print("\nNormal logits comparison:")
print(f"  Manual:         {-torch.log(torch.softmax(normal_logits, dim=1)[0, 2]).item():.6f}")
print(f"  F.cross_entropy:{F.cross_entropy(normal_logits, target).item():.6f}")
```

## Variants and Special Cases

Log-domain arithmetic is needed whenever multiplying many probabilities, since products underflow rapidly. For a sequence of T tokens each with probability ~0.1, the joint probability is 0.1^T which underflows to 0 for T > 45 in fp32. Log-domain: sum log-probabilities instead.

Temperature scaling softmax(x/T):
- T < 1 (sharpening): divides by T < 1, which multiplies logit magnitudes by 1/T — making overflow more likely. Always apply the max-shift trick.
- T > 1 (softening): reduces logit magnitudes, less overflow risk.

log-sum-exp with two terms: log(exp(a) + exp(b)) = max(a,b) + log(1 + exp(−|a−b|)). This is the logaddexp function in numpy and log1p(exp(x)) for softplus. Both appear frequently in probabilistic models.

## Log-Domain HMM Forward Algorithm

The HMM forward algorithm computes the probability of an observed sequence by marginalizing over all hidden state sequences. The product of T emission and transition probabilities underflows to zero for long sequences. The log-domain forward algorithm maintains log α_t(s) = log P(x₁,...,xₜ, state_t = s) and performs all summations using logsumexp:

log α_t(s') = log P(xₜ | s') + logsumexp_s[log α_{t-1}(s) + log A(s→s')]

This is O(T × S²) in time (same as standard forward algorithm) but stable for sequences of any length.

```python
import numpy as np

def log_forward_hmm(log_emission, log_transition, log_init):
    """
    Log-domain HMM forward algorithm (numerically stable).
    log_emission:   (T, S) log P(x_t | state_s)
    log_transition: (S, S) log P(state_s' | state_s)
    log_init:       (S,)   log P(state_s at t=0)
    Returns: log P(observation sequence)
    """
    T, S = log_emission.shape
    log_alpha = log_init + log_emission[0]  # (S,) — init at t=0

    for t in range(1, T):
        # log_alpha[s'] = log sum_s exp(log_alpha[s] + log_A[s,s'])
        # Shape broadcast: log_alpha (S,1) + log_transition (S,S) -> (S,S)
        log_trans_contrib = log_alpha[:, None] + log_transition  # (S, S)
        log_alpha = np.logaddexp.reduce(log_trans_contrib, axis=0) + log_emission[t]

    # Total log probability: sum over final states
    return np.logaddexp.reduce(log_alpha)

# Demo: 3-state HMM, 50-step sequence
np.random.seed(42)
S, T = 3, 50
log_A = np.log(np.array([[0.7, 0.2, 0.1],
                           [0.1, 0.6, 0.3],
                           [0.2, 0.3, 0.5]]))
log_B = np.random.randn(T, S) - np.log(S)  # random emission log-probs
log_pi = np.log(np.ones(S) / S)

log_prob = log_forward_hmm(log_B, log_A, log_pi)
print(f"Log P(sequence): {log_prob:.4f}")
print(f"P(sequence) = exp({log_prob:.4f}) = {np.exp(log_prob):.4e}")
# Without log-domain, P would underflow to 0 for T=50 steps
```

## Pitfalls

Common mistakes with overflow/underflow:

1. **Manual softmax before log**: computing log(softmax(x)) in two steps instead of using log_softmax. The intermediate softmax may produce NaN that log then propagates.

2. **Forgetting max-shift when scaling**: dividing logits by temperature < 1 before softmax inflates magnitudes. Always apply temperature first, then use stable softmax.

3. **Using fp16 for attention without max-shift**: attention scores Q@K^T/√d can easily exceed 11 in fp16, causing overflow. Use bf16 or ensure FlashAttention's tiled softmax is active.

4. **Accumulating probabilities across tokens**: multiplying per-token probabilities instead of adding log-probabilities causes rapid underflow for sequences longer than ~50 tokens in fp32.

## Practical Guidance

Rules for numerically safe computation:

- **Always use F.cross_entropy** in PyTorch, never manual softmax → log → NLL.
- **Use torch.logsumexp** rather than implementing logsumexp manually.
- **In custom normalizing-flow implementations**, compute log-determinants as sums of log|diag(J)|, not products of |diag(J)|.
- **For beam search**, maintain log-probabilities and add per-step log-probs; only convert to probability for final output.
- **Validate with small test cases**: verify that naive and stable implementations agree on normal logits before testing on extreme inputs.

> **WARNING: Temperature < 1 Amplifies Overflow Risk**
>
> Temperature scaling computes softmax(x/T). For T < 1 (sharpening), logits are multiplied by 1/T, increasing their magnitude. With logits already near the fp32 overflow threshold (~88), dividing by T = 0.1 gives logits near 880 — certain overflow. Always apply the max-shift trick explicitly when using temperatures other than 1.0, or use F.softmax(logits / T) which does so internally.

> **TIP: Log-Domain Arithmetic for Long Sequences**
>
> When computing probability of a sequence (product of conditionals), always work in log-domain: add log-probabilities instead of multiplying probabilities. For N tokens each with probability ~0.1, joint probability 0.1^N underflows for N > 45 in fp32. In log-domain, N × log(0.1) ≈ −N × 2.303 remains perfectly representable for any N.

| Computation | Naive Failure | Stable Solution |
| --- | --- | --- |
| logsumexp(x) | exp overflow | m + log Σ exp(x-m), m=max(x) |
| softmax(x) | exp overflow → NaN | softmax(x - max(x)) |
| log_softmax(x) | log(0) when denominator underflows | x - logsumexp(x) |
| cross_entropy | chain of instabilities | F.cross_entropy (fused) |
| sequence probability | product underflows | sum of log-probs |
| HMM forward | α_t → 0 for long T | log-domain with logaddexp |

---

## Key Takeaways

- exp(x) overflows in fp32 for x > 88.72 and underflows to 0 for x < −87.34; fp16 thresholds are much tighter (±11).
- The log-sum-exp trick log Σ exp(xᵢ) = m + log Σ exp(xᵢ−m) with m = max(x) is mathematically identical but numerically safe.
- Stable softmax subtracts max before exponentiating; stable log-softmax computes xᵢ − logsumexp(x).
- Always use F.cross_entropy (PyTorch) — it fuses log_softmax + NLL in one stable operation.
- Temperature T < 1 amplifies logit magnitudes by 1/T, increasing overflow risk — always use the max-shift trick.
- For long sequences, maintain and accumulate log-probabilities instead of multiplying probabilities (which underflow past ~45 tokens in fp32).
- The log-domain forward algorithm (using logaddexp reductions) enables stable HMM inference over arbitrarily long sequences.
