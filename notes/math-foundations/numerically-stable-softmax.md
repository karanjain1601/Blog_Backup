---
title: "Numerically Stable Softmax and Log-Softmax"
slug: "numerically-stable-softmax"
description: "Derivation of naive softmax instabilities, the max-shift stabilization, log-softmax, PyTorch F.cross_entropy internals, temperature scaling, and online softmax for streaming inference."
tags: ["numerical-methods", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU29mdG1heCBpcyB0aGUgbW9zdCB3aWRlbHkgdXNlZCBub3JtYWxpemF0aW9uIGZ1bmN0aW9uIGluIGRlZXAgbGVhcm5pbmcg4oCUIGl0IGFwcGVhcnMgaW4gb3V0cHV0IGxheWVycywgYXR0ZW50aW9uIG1lY2hhbmlzbXMsIG1peHR1cmUgbW9kZWxzLCBhbmQgcG9saWN5IG5ldHdvcmtzLiBEZXNwaXRlIGl0cyBzaW1wbGUgZm9ybXVsYSwgbmFpdmUgc29mdG1heCBpbXBsZW1lbnRhdGlvbnMgZmFpbCBjYXRhc3Ryb3BoaWNhbGx5IGZvciBsYXJnZSBvciBzbWFsbCBsb2dpdHMuIFVuZGVyc3RhbmRpbmcgd2h5IHNvZnRtYXggaXMgbnVtZXJpY2FsbHkgdW5zdGFibGUsIGhvdyB0aGUgbWF4LXNoaWZ0IHRyaWNrIGZpeGVzIGl0LCBhbmQgaG93IGxvZy1zb2Z0bWF4IGFuZCBjcm9zcy1lbnRyb3B5IGNvbXBvc2UgaW50byBhIHNhZmUgcGlwZWxpbmUgaXMgZXNzZW50aWFsIGZvciBhbnlvbmUgaW1wbGVtZW50aW5nIGN1c3RvbSBhdHRlbnRpb24sIGxvc3MgZnVuY3Rpb25zLCBvciBpbmZlcmVuY2Uga2VybmVscy4gVGhlIG9ubGluZSBzb2Z0bWF4IGFsZ29yaXRobSwgdXNlZCBieSBGbGFzaEF0dGVudGlvbiwgZnVydGhlciBzaG93cyBob3cgdG8gY29tcHV0ZSBzb2Z0bWF4IGluIGEgc2luZ2xlIHN0cmVhbWluZyBwYXNzIHdpdGhvdXQgbWF0ZXJpYWxpemluZyB0aGUgZnVsbCBkZW5vbWluYXRvci4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJDb3JlIERlZmluaXRpb24ifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJHaXZlbiBhIHZlY3RvciB4ID0gKHjigoEsIOKApiwgeOKCmSksIHNvZnRtYXggcHJvZHVjZXMgYSBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb246XG5cbnNvZnRtYXgoeCnhtaIgPSBleHAoeOG1oikgLyDOo+KxvCBleHAoeOKxvClcblxuUHJvcGVydGllczogYWxsIG91dHB1dHMgYXJlIGluICgwLDEpLCBvdXRwdXRzIHN1bSB0byAxLCB0cmFuc2xhdGlvbi1pbnZhcmlhbnQgKHNvZnRtYXgoeCtjKSA9IHNvZnRtYXgoeCkgZm9yIGFueSBzY2FsYXIgYyksIGFuZCBwcmVzZXJ2ZXMgcmVsYXRpdmUgb3JkZXJpbmcuXG5cbk5haXZlIGltcGxlbWVudGF0aW9uIHByb2JsZW1zOlxuLSBJZiBhbnkgeOG1oiA+IDg4LjcyIGluIGZwMzIsIGV4cCh44bWiKSA9IOKIniwgbWFraW5nIHRoZSBkZW5vbWluYXRvciDiiJ4sIGFuZCAwL+KIniA9IE5hTiBvciDiiJ4v4oieID0gTmFOLlxuLSBJZiBhbGwgeOG1oiA8IOKIkjg3LjM0IGluIGZwMzIsIGFsbCBleHAoeOG1oikgdW5kZXJmbG93IHRvIDAsIGdpdmluZyAwLzAgPSBOYU4uXG4tIFRoZXNlIGZhaWx1cmVzIGFyZSBjb21tb24gaW4gZWFybHkgdHJhaW5pbmcgKHJhbmRvbSBpbml0aWFsaXphdGlvbiBjYW4gcHJvZHVjZSBsYXJnZSBsb2dpdHMpLCB3aXRoIHRlbXBlcmF0dXJlIFQgPCAxLCBhbmQgaW4gYXR0ZW50aW9uIHdpdGggbGFyZ2UgZF9rLlxuXG5UaGUgZml4OiBleHBsb2l0IHRyYW5zbGF0aW9uIGludmFyaWFuY2UuIFN1YnRyYWN0IG0gPSBtYXgoeCkgYmVmb3JlIGV4cG9uZW50aWF0aW5nLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG4jIE5haXZlIHNvZnRtYXggZmFpbHMgd2l0aCBsYXJnZSBvciBzbWFsbCBsb2dpdHNcbmRlZiBuYWl2ZV9zb2Z0bWF4KHgpOlxuICAgIGUgPSBucC5leHAoeClcbiAgICByZXR1cm4gZSAvIGUuc3VtKClcblxuIyBTdGFibGUgc29mdG1heDogc3VidHJhY3QgbWF4IGZpcnN0XG5kZWYgc3RhYmxlX3NvZnRtYXgoeCk6XG4gICAgZSA9IG5wLmV4cCh4IC0geC5tYXgoKSlcbiAgICByZXR1cm4gZSAvIGUuc3VtKClcblxuIyBUZXN0IGNhc2VzXG50ZXN0X2Nhc2VzID0ge1xuICAgIFwibm9ybWFsXCI6ICAgICAgbnAuYXJyYXkoWzEuMCwgMi4wLCAzLjBdKSxcbiAgICBcImxhcmdlIHBvc1wiOiAgIG5wLmFycmF5KFsxMDAuMCwgMTAxLjAsIDEwMi4wXSksXG4gICAgXCJleHRyZW1lIHBvc1wiOiBucC5hcnJheShbMTAwMC4wLCAxMDAxLjAsIDEwMDIuMF0pLFxuICAgIFwibGFyZ2UgbmVnXCI6ICAgbnAuYXJyYXkoWy0xMDAuMCwgLTEwMS4wLCAtMTAyLjBdKSxcbn1cblxucHJpbnQoZlwieydDYXNlJzo8MTV9IHsnbmFpdmUnOjwyNX0geydzdGFibGUnOjwyNX1cIilcbnByaW50KFwiLVwiICogNjUpXG5mb3IgbmFtZSwgeCBpbiB0ZXN0X2Nhc2VzLml0ZW1zKCk6XG4gICAgbmFpdmUgID0gbmFpdmVfc29mdG1heCh4KVxuICAgIHN0YWJsZSA9IHN0YWJsZV9zb2Z0bWF4KHgpXG4gICAgcHJpbnQoZlwie25hbWU6PDE1fSB7c3RyKG5wLnJvdW5kKG5haXZlLDQpKTo8MjV9IHtzdHIobnAucm91bmQoc3RhYmxlLDQpKTo8MjV9XCIpXG5cbiMgTWF0aGVtYXRpY2FsIGVxdWl2YWxlbmNlOiBzb2Z0bWF4KHgpID0gc29mdG1heCh4IC0gYykgZm9yIGFueSBjXG54ID0gbnAuYXJyYXkoWzEuMCwgMi4wLCAzLjBdKVxucHJpbnQoXCJcXG49PT0gTWF0aGVtYXRpY2FsIEVxdWl2YWxlbmNlID09PVwiKVxucHJpbnQoZlwic29mdG1heCh4KTogICAgIHtzdGFibGVfc29mdG1heCh4KX1cIilcbnByaW50KGZcInNvZnRtYXgoeC0xMDApOiB7c3RhYmxlX3NvZnRtYXgoeCAtIDEwMC4wKX1cIilcbnByaW50KGZcInNvZnRtYXgoeCsxMDApOiB7c3RhYmxlX3NvZnRtYXgoeCArIDEwMC4wKX1cIilcbiMgQWxsIGlkZW50aWNhbCDigJQgc29mdG1heCBpcyB0cmFuc2xhdGlvbi1pbnZhcmlhbnQifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNYXRoZW1hdGljYWwgRGVyaXZhdGlvbiBvZiBTdGFiaWxpdHkifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUaGUgdHJhbnNsYXRpb24gaW52YXJpYW5jZSBvZiBzb2Z0bWF4IGlzIHRoZSBrZXkgaW5zaWdodDpcblxuc29mdG1heCh4KeG1oiA9IGV4cCh44bWiKSAvIM6j4rG8IGV4cCh44rG8KVxuICAgICAgICAgICAgID0gZXhwKHjhtaIg4oiSIG0pIMOXIGV4cChtKSAvIFvOo+KxvCBleHAoeOKxvCDiiJIgbSkgw5cgZXhwKG0pXSAgIChtdWx0aXBseSBudW0vZGVub20gYnkgZXhwKOKIkm0pKVxuICAgICAgICAgICAgID0gZXhwKHjhtaIg4oiSIG0pIC8gzqPisbwgZXhwKHjisbwg4oiSIG0pXG5cbldpdGggbSA9IG1heCh4KTpcbi0gVGhlIGxhcmdlc3QgZXhwb25lbnQgYXJndW1lbnQgaXMgeOKCmOKCkOKCkyDiiJIgbSA9IDAsIHNvIGV4cCgwKSA9IDEuIE5vIG92ZXJmbG93LlxuLSBBbGwgb3RoZXIgYXJndW1lbnRzIGFyZSDiiaQgMCwgc28gYWxsIGV4cCB2YWx1ZXMgYXJlIGluICgwLCAxXS4gTm8gb3ZlcmZsb3cuXG4tIFRoZSBtaW5pbXVtIGFyZ3VtZW50IGlzIHhfbWluIOKIkiBtLiBGb3IgdHlwaWNhbCBsb2dpdCByYW5nZXMgKDwgMTAwIHVuaXRzKSwgZXhwKOKIkjEwMCkg4omIIDMuN8OXMTDigbvigbTigbQgaW4gZnAzMiwgd2hpY2ggaXMgY2xvc2UgdG8gdGhlIHVuZGVyZmxvdyB0aHJlc2hvbGQgYnV0IHRoZSB1bmRlcmZsb3dlZC10by16ZXJvIHRlcm1zIGNvbnRyaWJ1dGUgbmVnbGlnaWJseSB0byB0aGUgZGVub21pbmF0b3IgYW55d2F5LlxuXG5UaGlzIGFsZ2VicmFpYyBpZGVudGl0eSBjb21lcyBhdCBubyBhY2N1cmFjeSBjb3N0IGFuZCByZXF1aXJlcyBvbmx5IG9uZSBleHRyYSBwYXNzIHRvIGZpbmQgdGhlIG1heGltdW0uIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTG9nLVNvZnRtYXggYW5kIENyb3NzLUVudHJvcHkifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJMb2ctc29mdG1heCBpcyBsb2cgYXBwbGllZCB0byBzb2Z0bWF4OlxuXG5sb2cgc29mdG1heCh4KeG1oiA9IGxvZyhleHAoeOG1oikgLyDOo+KxvCBleHAoeOKxvCkpXG4gICAgICAgICAgICAgICA9IHjhtaIg4oiSIGxvZyDOo+KxvCBleHAoeOKxvClcbiAgICAgICAgICAgICAgID0geOG1oiDiiJIgbG9nc3VtZXhwKHgpXG4gICAgICAgICAgICAgICA9IHjhtaIg4oiSIG0g4oiSIGxvZyDOo+KxvCBleHAoeOKxvCDiiJIgbSkgICAgKHN0YWJsZSBmb3JtKVxuXG5UaGlzIGlzIGEgcHVyZSBzdWJ0cmFjdGlvbiBvbiB0aGUgb3V0cHV0IOKAlCBubyBleHAgb24gdGhlIHJlc3VsdCBzaWRlLiBUaGUgb25seSBleHAgY2FsbHMgYXJlIGluIGNvbXB1dGluZyDOo+KxvCBleHAoeOKxvCDiiJIgbSksIHdoaWNoIGlzIHNhZmUgYmVjYXVzZSBhbGwgYXJndW1lbnRzIGFyZSDiiaQgMC5cblxuTmVnYXRpdmUgbG9nLWxpa2VsaWhvb2QgKE5MTCkgbG9zcyBmb3IgY2xhc3MgYzogbG9zcyA9IOKIkmxvZyBzb2Z0bWF4KHgpX2MgPSDiiJJsb2cgc29mdG1heCh4KVtjXS5cblxuUHlUb3JjaCdzIEYuY3Jvc3NfZW50cm9weShsb2dpdHMsIHRhcmdldCkgaW1wbGVtZW50cyBleGFjdGx5IHRoaXM6IGl0IGNvbXB1dGVzIGxvZ19zb2Z0bWF4IHN0YWJseSBhbmQgdGhlbiBzZWxlY3RzIHRoZSBuZWdhdGl2ZSB2YWx1ZSBhdCB0aGUgdGFyZ2V0IGluZGV4LiBJdCBpcyB0aGUgcHJlZmVycmVkIHBhdHRlcm4gYW5kIHNob3VsZCBiZSB1c2VkIGluc3RlYWQgb2YgbWFudWFsIHNvZnRtYXgg4oaSIGxvZyDihpIgaW5kZXguIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgU3RhYmxlIGxvZy1zb2Z0bWF4IGZyb20gc2NyYXRjaFxuZGVmIHN0YWJsZV9sb2dfc29mdG1heCh4KTpcbiAgICBcIlwiXCJOdW1lcmljYWxseSBzdGFibGUgbG9nLXNvZnRtYXggdXNpbmcgbG9nc3VtZXhwIHRyaWNrLlwiXCJcIlxuICAgIG0gPSB4Lm1heCgpXG4gICAgbG9nX1ogPSBtICsgbnAubG9nKG5wLnN1bShucC5leHAoeCAtIG0pKSkgICMgc3RhYmxlIGxvZ3N1bWV4cFxuICAgIHJldHVybiB4IC0gbG9nX1pcblxuIyBDb21wYXJpc29uOiB1bnN0YWJsZSB2cyBzdGFibGUgbG9nLXNvZnRtYXhcbmxvZ2l0cyA9IG5wLmFycmF5KFsxMDAwLjAsIDEwMDEuMCwgMTAwMi4wXSwgZHR5cGU9bnAuZmxvYXQzMilcblxuIyBOYWl2ZTogbG9nKHNvZnRtYXgoeCkpIOKAlCB0d28tc3RlcCwgZmFpbHNcbm5haXZlX3NtICA9IG5wLmV4cChsb2dpdHMpIC8gbnAuc3VtKG5wLmV4cChsb2dpdHMpKSAgICMgb3ZlcmZsb3dcbnByaW50KFwiTmFpdmUgc29mdG1heDogICAgIFwiLCBuYWl2ZV9zbSkgICAgICAgICAgICAgICAgICAjIG5hblxuXG4jIFN0YWJsZSBmcm9tIHNjcmF0Y2hcbnByaW50KFwiU3RhYmxlIGxvZ19zb2Z0bWF4OlwiLCBzdGFibGVfbG9nX3NvZnRtYXgobG9naXRzKSkgICMgWy0yLjQwOCwgLTEuNDA4LCAtMC40MDhdXG5cbiMgUHlUb3JjaCAodXNlIHRoaXMgaW4gcHJhY3RpY2UpXG5sb2dpdHNfdCA9IHRvcmNoLnRlbnNvcihsb2dpdHMpXG5wcmludChcIkYubG9nX3NvZnRtYXg6ICAgICBcIiwgRi5sb2dfc29mdG1heChsb2dpdHNfdCwgZGltPTApLm51bXB5KCkpXG5cbiMgQ3Jvc3MtZW50cm9weTogZnVzZWQgc3RhYmxlIG9wZXJhdGlvblxuYmF0Y2ggICA9IHRvcmNoLnRlbnNvcihbWzEwMDAuMCwgMTAwMS4wLCAxMDAyLjBdXSlcbnRhcmdldCAgPSB0b3JjaC50ZW5zb3IoWzJdKSAgIyBjb3JyZWN0IGNsYXNzID0gMlxuXG4jIFdST05HOiBtYW51YWwgcGlwZWxpbmVcbnByb2JzID0gdG9yY2guc29mdG1heChiYXRjaCwgZGltPTEpICAgICAgICAgIyBuYW5cbmxvc3NfYmFkID0gLXRvcmNoLmxvZyhwcm9ic1s6LCAyXSlcbnByaW50KFwiXFxuTWFudWFsIHNvZnRtYXgtPmxvZy0+TkxMOlwiLCBsb3NzX2JhZC5pdGVtKCkpICAgIyBuYW5cblxuIyBDT1JSRUNUOiBmdXNlZFxubG9zc19nb29kID0gRi5jcm9zc19lbnRyb3B5KGJhdGNoLCB0YXJnZXQpXG5wcmludChcIkYuY3Jvc3NfZW50cm9weTogICAgICAgICBcIiwgbG9zc19nb29kLml0ZW0oKSkgICAgIyAwLjQwNzZcblxuIyBJbnRlcm5hbHMgb2YgRi5jcm9zc19lbnRyb3B5XG5sb2dfc20gICA9IEYubG9nX3NvZnRtYXgoYmF0Y2gsIGRpbT0xKVxubG9zc19ubGwgPSBGLm5sbF9sb3NzKGxvZ19zbSwgdGFyZ2V0KVxucHJpbnQoXCJsb2dfc29mdG1heCArIE5MTDogICAgICAgXCIsIGxvc3NfbmxsLml0ZW0oKSkgICAgICMgMC40MDc2IChzYW1lKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlRlbXBlcmF0dXJlIFNjYWxpbmcifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJUZW1wZXJhdHVyZSBzY2FsaW5nIG1vZGlmaWVzIHNvZnRtYXggc2hhcnBuZXNzOlxuXG5zb2Z0bWF4KHgvVCnhtaIgPSBleHAoeOG1oi9UKSAvIM6j4rG8IGV4cCh44rG8L1QpXG5cbi0gVCDihpIgMDogYXJnbWF4IChvbmUtaG90IGRpc3RyaWJ1dGlvbilcbi0gVCA9IDE6IHN0YW5kYXJkIHNvZnRtYXhcbi0gVCDihpIg4oieOiB1bmlmb3JtIGRpc3RyaWJ1dGlvblxuXG5TbWFsbCBUIDwgMSAoc2hhcnBlbmluZykgZGl2aWRlcyBsb2dpdHMgYnkgVCwgYW1wbGlmeWluZyB0aGVpciBtYWduaXR1ZGUgYnkgMS9ULiBUaGlzIGluY3JlYXNlcyBvdmVyZmxvdyByaXNrIHNpZ25pZmljYW50bHkuIEZvciB0ZW1wZXJhdHVyZSBUID0gMC4xIGFuZCBpbml0aWFsIGxvZ2l0cyBuZWFyIDUwIChub3QgdW51c3VhbCBpbiBsYXJnZSBtb2RlbHMpLCB0aGUgZWZmZWN0aXZlIGxvZ2l0cyBiZWNvbWUgNTAwIOKAlCBmYXIgYWJvdmUgdGhlIGZwMzIgb3ZlcmZsb3cgdGhyZXNob2xkIG9mIDg4LjcyLlxuXG5UaGUgc3RhYmxlIGltcGxlbWVudGF0aW9uOiBhcHBseSB0aGUgbWF4LXNoaWZ0IHRyaWNrIGFmdGVyIGRpdmlkaW5nIGJ5IFQuIFB5VG9yY2gncyBGLnNvZnRtYXgobG9naXRzIC8gVCkgZG9lcyB0aGlzIGNvcnJlY3RseSBiZWNhdXNlIEYuc29mdG1heCBpcyBpbnRlcm5hbGx5IHN0YWJsZS4gQSBtYW51YWwgaW1wbGVtZW50YXRpb24gbXVzdCBleHBsaWNpdGx5IHN1YnRyYWN0IHRoZSBtYXggYWZ0ZXIgZGl2aWRpbmcuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbiMgVGVtcGVyYXR1cmUgc2NhbGluZ1xuZGVmIHRlbXBfc29mdG1heCh4LCBUPTEuMCk6XG4gICAgXCJcIlwiTnVtZXJpY2FsbHkgc3RhYmxlIHRlbXBlcmF0dXJlLXNjYWxlZCBzb2Z0bWF4LlwiXCJcIlxuICAgIHNjYWxlZCA9IHggLyBUXG4gICAgc2NhbGVkID0gc2NhbGVkIC0gc2NhbGVkLm1heCgpICAjIG1heC1zaGlmdCBBRlRFUiB0ZW1wZXJhdHVyZSBzY2FsaW5nXG4gICAgZSA9IG5wLmV4cChzY2FsZWQpXG4gICAgcmV0dXJuIGUgLyBlLnN1bSgpXG5cbnggPSBucC5hcnJheShbMS4wLCAyLjAsIDMuMCwgNC4wLCA1LjBdKVxucHJpbnQoXCI9PT0gRWZmZWN0IG9mIFRlbXBlcmF0dXJlID09PVwiKVxuZm9yIFQgaW4gWzAuMSwgMC41LCAxLjAsIDIuMCwgMTAuMF06XG4gICAgcyA9IHRlbXBfc29mdG1heCh4LCBUKVxuICAgIHByaW50KGZcIlQ9e1Q6NC4xZn06IHtucC5yb3VuZChzLCAzKX1cIilcbiMgVD0wLjEg4oaSIHZlcnkgcGVha2VkOyBUPTEwIOKGkiBuZWFybHkgdW5pZm9ybVxuXG4jIE92ZXJmbG93IHdpdGggbmFpdmUgdGVtcGVyYXR1cmUgc2NhbGluZ1xueF9sYXJnZSA9IG5wLmFycmF5KFs1MC4wLCA2MC4wLCA3MC4wXSwgZHR5cGU9bnAuZmxvYXQzMilcblQgPSAwLjFcbnByaW50KFwiXFxuPT09IE92ZXJmbG93IHdpdGggc21hbGwgVCA9PT1cIilcbnNjYWxlZF9uYWl2ZSA9IHhfbGFyZ2UgLyBUICAgIyBbNTAwLCA2MDAsIDcwMF0g4oCUIGZhciBhYm92ZSBmcDMyIG92ZXJmbG93IHRocmVzaG9sZFxucHJpbnQoZlwiTG9naXRzIC8gVCA9IHtzY2FsZWRfbmFpdmV9XCIpXG5wcmludChmXCJucC5leHAoNzAwKSA9IHtucC5leHAobnAuZmxvYXQzMig3MDApKX1cIikgICMgaW5mXG5uYWl2ZSA9IG5wLmV4cChzY2FsZWRfbmFpdmUpOyBwcmludChmXCJOYWl2ZSBzb2Z0bWF4OiB7bmFpdmUgLyBuYWl2ZS5zdW0oKX1cIikgICMgbmFuXG5cbiMgU3RhYmxlOiBzdWJ0cmFjdCBtYXggQUZURVIgZGl2aWRpbmcgYnkgVFxuc2NhbGVkX3N0YWJsZSA9IHNjYWxlZF9uYWl2ZSAtIHNjYWxlZF9uYWl2ZS5tYXgoKVxuZSA9IG5wLmV4cChzY2FsZWRfc3RhYmxlKTsgcHJpbnQoZlwiU3RhYmxlIHNvZnRtYXg6IHtucC5yb3VuZChlIC8gZS5zdW0oKSwgNCl9XCIpXG5cbiMgUHlUb3JjaCBGLnNvZnRtYXggaXMgYWx3YXlzIHN0YWJsZVxubG9naXRzX3QgPSB0b3JjaC50ZW5zb3IoeF9sYXJnZSlcbnByaW50KGZcIkYuc29mdG1heCh4L1Q9MC4xKToge0Yuc29mdG1heChsb2dpdHNfdCAvIFQsIGRpbT0wKS5udW1weSgpfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk9ubGluZSBTb2Z0bWF4IGZvciBTdHJlYW1pbmcgSW5mZXJlbmNlIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3RhbmRhcmQgc29mdG1heCByZXF1aXJlcyB0d28gcGFzc2VzIG92ZXIgdGhlIGlucHV0OiBvbmUgdG8gZmluZCB0aGUgbWF4aW11bSAoZm9yIHN0YWJpbGl0eSksIGFuZCBvbmUgdG8gY29tcHV0ZSBleHAgYW5kIG5vcm1hbGl6ZS4gRm9yIG1lbW9yeS1jb25zdHJhaW5lZCBpbmZlcmVuY2UgKGUuZy4sIEZsYXNoQXR0ZW50aW9uIHByb2Nlc3NpbmcgYXR0ZW50aW9uIHNjb3JlcyBpbiB0aWxlcyksIGFuIG9ubGluZSBvbmUtcGFzcyBhbGdvcml0aG0gaXMgbmVlZGVkLlxuXG5UaGUgb25saW5lIHNvZnRtYXggYWxnb3JpdGhtIG1haW50YWlucyBhIHJ1bm5pbmcgbWF4aW11bSBtIGFuZCBhIHJ1bm5pbmcgc3VtIHMuIFdoZW4gYSBuZXcgZWxlbWVudCB44oKcIGFycml2ZXM6XG4tIG1fbmV3ID0gbWF4KG1fb2xkLCB44oKcKVxuLSBzX25ldyA9IHNfb2xkIMOXIGV4cChtX29sZCDiiJIgbV9uZXcpICsgZXhwKHjigpwg4oiSIG1fbmV3KVxuXG5UaGUgY29ycmVjdGlvbiBmYWN0b3IgZXhwKG1fb2xkIOKIkiBtX25ldykgcmVzY2FsZXMgcHJldmlvdXNseSBhY2N1bXVsYXRlZCBleHAgdmFsdWVzIHRvIHRoZSBuZXcgcnVubmluZyBtYXhpbXVtLiBBdCBlYWNoIHN0ZXAsIHRoZSBjdXJyZW50IGVzdGltYXRlIHNvZnRtYXgoeF97MTp0fSkgY2FuIGJlIGNvbXB1dGVkIGFzIGV4cCh44bWiIOKIkiBtX3QpIC8gc190IGZvciBhbnkgcHJldmlvdXMgeOG1oiwgdGhvdWdoIGluIHByYWN0aWNlIEZsYXNoQXR0ZW50aW9uIGNvbXB1dGVzIHRoZSB3ZWlnaHRlZCB2YWx1ZSBhY2N1bXVsYXRpb24gb25saW5lIHdpdGhvdXQgbWF0ZXJpYWxpemluZyBpbmRpdmlkdWFsIHNvZnRtYXggdmFsdWVzLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuXG5kZWYgb25saW5lX3NvZnRtYXgoeCk6XG4gICAgXCJcIlwiXG4gICAgT25saW5lIChvbmUtcGFzcykgc29mdG1heCDigJQgdGhlIGFsZ29yaXRobSBiZWhpbmQgRmxhc2hBdHRlbnRpb24uXG4gICAgUmV0dXJucyBzb2Z0bWF4IHZhbHVlcyB3aXRoIG51bWVyaWNhbGx5IHN0YWJsZSBydW5uaW5nIG1heC9zdW0uXG4gICAgXCJcIlwiXG4gICAgbSA9IC1ucC5pbmYgICAjIHJ1bm5pbmcgbWF4aW11bVxuICAgIHMgPSAwLjAgICAgICAgIyBydW5uaW5nIHN1bSBvZiBleHAoeOG1oiAtIG0pXG4gICAgZm9yIHhpIGluIHg6XG4gICAgICAgIG1fbmV3ID0gbWF4KG0sIHhpKVxuICAgICAgICBzID0gcyAqIG5wLmV4cChtIC0gbV9uZXcpICsgbnAuZXhwKHhpIC0gbV9uZXcpICAjIHJlc2NhbGUgb2xkLCBhZGQgbmV3XG4gICAgICAgIG0gPSBtX25ld1xuICAgIHJldHVybiBucC5hcnJheShbbnAuZXhwKHhpIC0gbSkgLyBzIGZvciB4aSBpbiB4XSlcblxuZGVmIHR3b19wYXNzX3NvZnRtYXgoeCk6XG4gICAgXCJcIlwiU3RhbmRhcmQgdHdvLXBhc3Mgc3RhYmxlIHNvZnRtYXggZm9yIGNvbXBhcmlzb24uXCJcIlwiXG4gICAgZSA9IG5wLmV4cCh4IC0geC5tYXgoKSlcbiAgICByZXR1cm4gZSAvIGUuc3VtKClcblxuIyBWZXJpZnkgY29ycmVjdG5lc3NcbnRlc3RfY2FzZXMgPSBbXG4gICAgbnAuYXJyYXkoWzEuMCwgMi4wLCAzLjBdKSxcbiAgICBucC5hcnJheShbMTAwMC4wLCAxMDAxLjAsIDEwMDIuMF0pLFxuICAgIG5wLmFycmF5KFstMTAwLjAsIC01MC4wLCAwLjAsIDUwLjBdKSxcbl1cbnByaW50KFwiPT09IE9ubGluZSB2cyBUd28tUGFzcyBTb2Z0bWF4ID09PVwiKVxuZm9yIHggaW4gdGVzdF9jYXNlczpcbiAgICBvbmxpbmUgICAgPSBvbmxpbmVfc29mdG1heCh4KVxuICAgIHR3b19wYXNzICA9IHR3b19wYXNzX3NvZnRtYXgoeClcbiAgICBtYXhfZGlmZiAgPSBucC5tYXgobnAuYWJzKG9ubGluZSAtIHR3b19wYXNzKSlcbiAgICBwcmludChmXCJ4flt7eFswXTouMGZ9Li57eFstMV06LjBmfV06IG9ubGluZT17bnAucm91bmQob25saW5lLDQpfSAgbWF4X2RpZmY9e21heF9kaWZmOi4yZX1cIilcblxuIyBPbmxpbmUgc29mdG1heCBmb3IgYXR0ZW50aW9uIChzaW1wbGlmaWVkIEZsYXNoQXR0ZW50aW9uIHBhdHRlcm4pXG5kZWYgZmxhc2hfYXR0ZW50aW9uX3NpbXBsZShRLCBLLCBWLCBzY2FsZSk6XG4gICAgXCJcIlwiU2luZ2xlLWhlYWQgYXR0ZW50aW9uIHdpdGggb25saW5lIHNvZnRtYXggKG5vIG1hdGVyaWFsaXplZCBhdHRlbnRpb24gbWF0cml4KS5cIlwiXCJcbiAgICBUX3EsIFRfayA9IFEuc2hhcGVbMF0sIEsuc2hhcGVbMF1cbiAgICBvdXRwdXQgPSBucC56ZXJvc19saWtlKFEpXG4gICAgZm9yIGkgaW4gcmFuZ2UoVF9xKTpcbiAgICAgICAgc2NvcmVzID0gKFFbaV0gQCBLLlQpICogc2NhbGUgICAjIChUX2ssKVxuICAgICAgICBhdHRuICAgPSBvbmxpbmVfc29mdG1heChzY29yZXMpICAjIG9ubGluZSBzdGFibGUgc29mdG1heFxuICAgICAgICBvdXRwdXRbaV0gPSBhdHRuIEAgVlxuICAgIHJldHVybiBvdXRwdXRcblxubnAucmFuZG9tLnNlZWQoNDIpXG5kLCBUID0gOCwgNFxuUSA9IG5wLnJhbmRvbS5yYW5kbihULCBkKTsgSyA9IG5wLnJhbmRvbS5yYW5kbihULCBkKTsgViA9IG5wLnJhbmRvbS5yYW5kbihULCBkKVxub3V0ID0gZmxhc2hfYXR0ZW50aW9uX3NpbXBsZShRLCBLLCBWLCBzY2FsZT0xLjAvbnAuc3FydChkKSlcbnByaW50KGZcIlxcbkF0dGVudGlvbiBvdXRwdXQgc2hhcGU6IHtvdXQuc2hhcGV9LCBub3JtOiB7bnAubGluYWxnLm5vcm0ob3V0KTouNGZ9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUGl0ZmFsbHMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJDb21tb24gc29mdG1heCBpbXBsZW1lbnRhdGlvbiBtaXN0YWtlczpcblxuMS4gKipDb21wdXRpbmcgbG9nKHNvZnRtYXgoeCkpIGluIHR3byBzdGVwcyoqOiBhbHdheXMgdXNlIGxvZ19zb2Z0bWF4IG9yIEYuY3Jvc3NfZW50cm9weSBpbnN0ZWFkLlxuXG4yLiAqKkZvcmdldHRpbmcgbWF4LXNoaWZ0IGFmdGVyIHRlbXBlcmF0dXJlIHNjYWxpbmcqKjogdGVtcGVyYXR1cmUgPCAxIGFtcGxpZmllcyBsb2dpdHMgYmVmb3JlIHRoZSBtYXgtc2hpZnQgaXMgYXBwbGllZCBpbiBuYWl2ZSBpbXBsZW1lbnRhdGlvbnMuXG5cbjMuICoqVXNpbmcgZnAxNiBmb3IgYXR0ZW50aW9uIHNjb3JlcyB3aXRob3V0IG92ZXJmbG93IGNoZWNrKio6IFFAS15UL+KImmQgY2FuIHByb2R1Y2UgdmFsdWVzIGFib3ZlIHRoZSBmcDE2IG92ZXJmbG93IHRocmVzaG9sZCBvZiB+MTEgZm9yIGxhcmdlIG1vZGVscyB3aXRoIGhpZ2gtZGltZW5zaW9uYWwga2V5cy5cblxuNC4gKipBcHBseWluZyBzb2Z0bWF4IGFsb25nIHRoZSB3cm9uZyBkaW1lbnNpb24qKjogaW4gYmF0Y2hlZCBzZXR0aW5ncywgc29mdG1heCBtdXN0IGJlIGFwcGxpZWQgYWxvbmcgZGltPTEgKG92ZXIgY2xhc3Nlcykgbm90IGRpbT0wIChvdmVyIGJhdGNoKS4gQSBidWcgaGVyZSBwcm9kdWNlcyB2YWxpZC1sb29raW5nIG91dHB1dHMgd2l0aCB3cm9uZyBzZW1hbnRpY3MuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUHJhY3RpY2FsIEd1aWRhbmNlIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQmVzdCBwcmFjdGljZXMgZm9yIHNvZnRtYXggaW4gcHJvZHVjdGlvbjpcblxuLSAqKkZvciBjbGFzc2lmaWNhdGlvbioqOiBhbHdheXMgdXNlIEYuY3Jvc3NfZW50cm9weShsb2dpdHMsIHRhcmdldCksIG5ldmVyIGNvbXB1dGUgc29mdG1heCBwcm9iYWJpbGl0aWVzIG1hbnVhbGx5IGFuZCB0aGVuIGxvZyB0aGVtLlxuLSAqKkZvciBpbmZlcmVuY2UgcHJvYmFiaWxpdGllcyoqOiB1c2UgRi5zb2Z0bWF4KGxvZ2l0cywgZGltPS0xKSDigJQgUHlUb3JjaCdzIGltcGxlbWVudGF0aW9uIGlzIGludGVybmFsbHkgc3RhYmxlLlxuLSAqKkZvciB0ZW1wZXJhdHVyZSBzYW1wbGluZyoqOiBjb21wdXRlIEYuc29mdG1heChsb2dpdHMgLyBULCBkaW09LTEpIGluIG9uZSBzdGVwIHJhdGhlciB0aGFuIGRpdmlkaW5nIGFmdGVyIHNvZnRtYXguXG4tICoqRm9yIGN1c3RvbSBhdHRlbnRpb24qKjogZW5zdXJlIHRoZSBzb2Z0bWF4IGlzIGNvbXB1dGVkIG92ZXIgdGhlIGNvcnJlY3Qgc2VxdWVuY2UgZGltZW5zaW9uIGFuZCBjb25zaWRlciB1c2luZyBGLnNjYWxlZF9kb3RfcHJvZHVjdF9hdHRlbnRpb24gd2hpY2ggaGFuZGxlcyBudW1lcmljYWwgc3RhYmlsaXR5IGludGVybmFsbHkuXG4tICoqRm9yIG51bWVyaWNhbCB0ZXN0aW5nKio6IHZlcmlmeSB0aGF0IHlvdXIgaW1wbGVtZW50YXRpb24gbWF0Y2hlcyBGLnNvZnRtYXggb24gYm90aCBub3JtYWwgaW5wdXRzIFsxLDIsM10gYW5kIGV4dHJlbWUgaW5wdXRzIFsxMDAwLDEwMDEsMTAwMl0uIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInZhcmlhbnQiOiAidGlwIiwgInRpdGxlIjogIlVzZSBGLnNjYWxlZF9kb3RfcHJvZHVjdF9hdHRlbnRpb24iLCAiY29udGVudCI6ICJQeVRvcmNoIDIuMCsgaW5jbHVkZXMgRi5zY2FsZWRfZG90X3Byb2R1Y3RfYXR0ZW50aW9uIHdoaWNoIGRpc3BhdGNoZXMgdG8gRmxhc2hBdHRlbnRpb24gd2hlbiBwb3NzaWJsZSwgaGFuZGxpbmcgbnVtZXJpY2FsIHN0YWJpbGl0eSAob25saW5lIHNvZnRtYXgpLCBtZW1vcnkgZWZmaWNpZW5jeSAobm8gbWF0ZXJpYWxpemVkIGF0dGVudGlvbiBtYXRyaXgpLCBhbmQgbWFzayBoYW5kbGluZyBjb3JyZWN0bHkuIFVubGVzcyBpbXBsZW1lbnRpbmcgYSBjdXN0b20gYXR0ZW50aW9uIHZhcmlhbnQsIHByZWZlciB0aGlzIG92ZXIgbWFudWFsIFFAS15UIC8gc3FydChkKSArIHNvZnRtYXggcGF0dGVybnMuIn0sIHsidHlwZSI6ICJ0YWJsZSIsICJoZWFkZXJzIjogWyJQYXR0ZXJuIiwgIk51bWVyaWNhbGx5IFNhZmU/IiwgIlByZWZlcnJlZCBBbHRlcm5hdGl2ZSJdLCAicm93cyI6IFtbIm5wLmV4cCh4KS9ucC5leHAoeCkuc3VtKCkiLCAiTm8gKG92ZXJmbG93KSIsICJzdGFibGVfc29mdG1heCh4IC0geC5tYXgoKSkiXSwgWyJ0b3JjaC5sb2codG9yY2guc29mdG1heCh4LGQpKSIsICJObyAobmFuIGNoYWluKSIsICJGLmxvZ19zb2Z0bWF4KHgsIGRpbT1kKSJdLCBbIi1sb2coc29mdG1heCh4KVt0YXJnZXRdKSIsICJObyAodHdvLXN0ZXApIiwgIkYuY3Jvc3NfZW50cm9weSh4LCB0YXJnZXQpIl0sIFsic29mdG1heCh4L1QpIHdpdGggVDwxIChtYW51YWwpIiwgIk5vIChvdmVyZmxvdykiLCAiRi5zb2Z0bWF4KHgvVCwgZGltPS0xKSJdLCBbIlFASy5UL3NxcnQoZCkgKyBzb2Z0bWF4IG1hbnVhbGx5IiwgIlJpc2t5IGluIGZwMTYiLCAiRi5zY2FsZWRfZG90X3Byb2R1Y3RfYXR0ZW50aW9uIl0sIFsibG9nYWRkZXhwLnJlZHVjZSh4KSIsICJZZXMiLCAidG9yY2gubG9nc3VtZXhwKHgsIGRpbT0wKSJdXX0sIHsidHlwZSI6ICJkaXZpZGVyIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2V5IFRha2Vhd2F5cyJ9LCB7InR5cGUiOiAibGlzdCIsICJvcmRlcmVkIjogZmFsc2UsICJpdGVtcyI6IFsiTmFpdmUgc29mdG1heCBvdmVyZmxvd3MgZm9yIHhfaSA+IDg4LjcyIChmcDMyKSBvciA+IDExLjA5IChmcDE2KSBhbmQgdW5kZXJmbG93cyB0byBOYU4gd2hlbiBhbGwgbG9naXRzIGFyZSB2ZXJ5IG5lZ2F0aXZlLiIsICJUaGUgbWF4LXNoaWZ0IHRyaWNrIHNvZnRtYXgoeCDiiJIgbWF4KHgpKSBpcyBtYXRoZW1hdGljYWxseSBpZGVudGljYWwgdG8gc29mdG1heCh4KSBidXQgbnVtZXJpY2FsbHkgc2FmZTsgaXQgY29zdHMgb25lIGV4dHJhIHBhc3MgdG8gZmluZCB0aGUgbWF4aW11bS4iLCAiTG9nLXNvZnRtYXggPSB4IOKIkiBsb2dzdW1leHAoeCkgPSB44bWiIOKIkiBtIOKIkiBsb2cgzqMgZXhwKHjisbwg4oiSIG0pOyB0aGUgZmluYWwgb3V0cHV0IGlzIGEgcHVyZSBzdWJ0cmFjdGlvbiB3aXRoIG5vIG92ZXJmbG93IHJpc2suIiwgIkFsd2F5cyB1c2UgRi5jcm9zc19lbnRyb3B5IGluIFB5VG9yY2gg4oCUIGl0IGZ1c2VzIGxvZ19zb2Z0bWF4IGFuZCBOTEwgbG9zcyBpbiBvbmUgc3RhYmxlIG9wZXJhdGlvbi4iLCAiVGVtcGVyYXR1cmUgVCA8IDEgYW1wbGlmaWVzIGxvZ2l0cyBieSAxL1QgYmVmb3JlIHRoZSBtYXgtc2hpZnQg4oCUIGFsd2F5cyBhcHBseSB0aGUgbWF4LXNoaWZ0IGFmdGVyIHRlbXBlcmF0dXJlIHNjYWxpbmcsIG5vdCBiZWZvcmUuIiwgIk9ubGluZSBzb2Z0bWF4IG1haW50YWlucyBhIHJ1bm5pbmcgKG1heCwgc3VtKSBwYWlyIGFuZCByZXNjYWxlcyBwcmV2aW91c2x5IHNlZW4gdmFsdWVzIHdoZW4gYSBuZXcgbWF4aW11bSBpcyBlbmNvdW50ZXJlZCDigJQgdGhpcyBpcyB0aGUgYWxnb3JpdGhtIGJlaGluZCBGbGFzaEF0dGVudGlvbidzIHRpbGVkIGNvbXB1dGF0aW9uLiIsICJGb3IgcHJvZHVjdGlvbiBpbmZlcmVuY2UsIHVzZSBGLnNjYWxlZF9kb3RfcHJvZHVjdF9hdHRlbnRpb24gKFB5VG9yY2ggMi4wKykgd2hpY2ggZGlzcGF0Y2hlcyB0byBGbGFzaEF0dGVudGlvbiBhbmQgaGFuZGxlcyBhbGwgc3RhYmlsaXR5IGFuZCBtZW1vcnkgY29uY2VybnMgYXV0b21hdGljYWxseS4iXX1d"
---
# Numerically Stable Softmax and Log-Softmax

Softmax is the most widely used normalization function in deep learning — it appears in output layers, attention mechanisms, mixture models, and policy networks. Despite its simple formula, naive softmax implementations fail catastrophically for large or small logits. Understanding why softmax is numerically unstable, how the max-shift trick fixes it, and how log-softmax and cross-entropy compose into a safe pipeline is essential for anyone implementing custom attention, loss functions, or inference kernels. The online softmax algorithm, used by FlashAttention, further shows how to compute softmax in a single streaming pass without materializing the full denominator.

## Core Definition

Given a vector x = (x₁, …, xₙ), softmax produces a probability distribution:

softmax(x)ᵢ = exp(xᵢ) / Σⱼ exp(xⱼ)

Properties: all outputs are in (0,1), outputs sum to 1, translation-invariant (softmax(x+c) = softmax(x) for any scalar c), and preserves relative ordering.

Naive implementation problems:
- If any xᵢ > 88.72 in fp32, exp(xᵢ) = ∞, making the denominator ∞, and 0/∞ = NaN or ∞/∞ = NaN.
- If all xᵢ < −87.34 in fp32, all exp(xᵢ) underflow to 0, giving 0/0 = NaN.
- These failures are common in early training (random initialization can produce large logits), with temperature T < 1, and in attention with large d_k.

The fix: exploit translation invariance. Subtract m = max(x) before exponentiating.

```python
import numpy as np
import torch
import torch.nn.functional as F

# Naive softmax fails with large or small logits
def naive_softmax(x):
    e = np.exp(x)
    return e / e.sum()

# Stable softmax: subtract max first
def stable_softmax(x):
    e = np.exp(x - x.max())
    return e / e.sum()

# Test cases
test_cases = {
    "normal":      np.array([1.0, 2.0, 3.0]),
    "large pos":   np.array([100.0, 101.0, 102.0]),
    "extreme pos": np.array([1000.0, 1001.0, 1002.0]),
    "large neg":   np.array([-100.0, -101.0, -102.0]),
}

print(f"{'Case':<15} {'naive':<25} {'stable':<25}")
print("-" * 65)
for name, x in test_cases.items():
    naive  = naive_softmax(x)
    stable = stable_softmax(x)
    print(f"{name:<15} {str(np.round(naive,4)):<25} {str(np.round(stable,4)):<25}")

# Mathematical equivalence: softmax(x) = softmax(x - c) for any c
x = np.array([1.0, 2.0, 3.0])
print("\n=== Mathematical Equivalence ===")
print(f"softmax(x):     {stable_softmax(x)}")
print(f"softmax(x-100): {stable_softmax(x - 100.0)}")
print(f"softmax(x+100): {stable_softmax(x + 100.0)}")
# All identical — softmax is translation-invariant
```

## Mathematical Derivation of Stability

The translation invariance of softmax is the key insight:

softmax(x)ᵢ = exp(xᵢ) / Σⱼ exp(xⱼ)
             = exp(xᵢ − m) × exp(m) / [Σⱼ exp(xⱼ − m) × exp(m)]   (multiply num/denom by exp(−m))
             = exp(xᵢ − m) / Σⱼ exp(xⱼ − m)

With m = max(x):
- The largest exponent argument is xₘₐₓ − m = 0, so exp(0) = 1. No overflow.
- All other arguments are ≤ 0, so all exp values are in (0, 1]. No overflow.
- The minimum argument is x_min − m. For typical logit ranges (< 100 units), exp(−100) ≈ 3.7×10⁻⁴⁴ in fp32, which is close to the underflow threshold but the underflowed-to-zero terms contribute negligibly to the denominator anyway.

This algebraic identity comes at no accuracy cost and requires only one extra pass to find the maximum.

## Log-Softmax and Cross-Entropy

Log-softmax is log applied to softmax:

log softmax(x)ᵢ = log(exp(xᵢ) / Σⱼ exp(xⱼ))
               = xᵢ − log Σⱼ exp(xⱼ)
               = xᵢ − logsumexp(x)
               = xᵢ − m − log Σⱼ exp(xⱼ − m)    (stable form)

This is a pure subtraction on the output — no exp on the result side. The only exp calls are in computing Σⱼ exp(xⱼ − m), which is safe because all arguments are ≤ 0.

Negative log-likelihood (NLL) loss for class c: loss = −log softmax(x)_c = −log softmax(x)[c].

PyTorch's F.cross_entropy(logits, target) implements exactly this: it computes log_softmax stably and then selects the negative value at the target index. It is the preferred pattern and should be used instead of manual softmax → log → index.

```python
import torch
import torch.nn.functional as F
import numpy as np

# Stable log-softmax from scratch
def stable_log_softmax(x):
    """Numerically stable log-softmax using logsumexp trick."""
    m = x.max()
    log_Z = m + np.log(np.sum(np.exp(x - m)))  # stable logsumexp
    return x - log_Z

# Comparison: unstable vs stable log-softmax
logits = np.array([1000.0, 1001.0, 1002.0], dtype=np.float32)

# Naive: log(softmax(x)) — two-step, fails
naive_sm  = np.exp(logits) / np.sum(np.exp(logits))   # overflow
print("Naive softmax:     ", naive_sm)                  # nan

# Stable from scratch
print("Stable log_softmax:", stable_log_softmax(logits))  # [-2.408, -1.408, -0.408]

# PyTorch (use this in practice)
logits_t = torch.tensor(logits)
print("F.log_softmax:     ", F.log_softmax(logits_t, dim=0).numpy())

# Cross-entropy: fused stable operation
batch   = torch.tensor([[1000.0, 1001.0, 1002.0]])
target  = torch.tensor([2])  # correct class = 2

# WRONG: manual pipeline
probs = torch.softmax(batch, dim=1)         # nan
loss_bad = -torch.log(probs[:, 2])
print("\nManual softmax->log->NLL:", loss_bad.item())   # nan

# CORRECT: fused
loss_good = F.cross_entropy(batch, target)
print("F.cross_entropy:         ", loss_good.item())    # 0.4076

# Internals of F.cross_entropy
log_sm   = F.log_softmax(batch, dim=1)
loss_nll = F.nll_loss(log_sm, target)
print("log_softmax + NLL:       ", loss_nll.item())     # 0.4076 (same)
```

## Temperature Scaling

Temperature scaling modifies softmax sharpness:

softmax(x/T)ᵢ = exp(xᵢ/T) / Σⱼ exp(xⱼ/T)

- T → 0: argmax (one-hot distribution)
- T = 1: standard softmax
- T → ∞: uniform distribution

Small T < 1 (sharpening) divides logits by T, amplifying their magnitude by 1/T. This increases overflow risk significantly. For temperature T = 0.1 and initial logits near 50 (not unusual in large models), the effective logits become 500 — far above the fp32 overflow threshold of 88.72.

The stable implementation: apply the max-shift trick after dividing by T. PyTorch's F.softmax(logits / T) does this correctly because F.softmax is internally stable. A manual implementation must explicitly subtract the max after dividing.

```python
import numpy as np
import torch
import torch.nn.functional as F

# Temperature scaling
def temp_softmax(x, T=1.0):
    """Numerically stable temperature-scaled softmax."""
    scaled = x / T
    scaled = scaled - scaled.max()  # max-shift AFTER temperature scaling
    e = np.exp(scaled)
    return e / e.sum()

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print("=== Effect of Temperature ===")
for T in [0.1, 0.5, 1.0, 2.0, 10.0]:
    s = temp_softmax(x, T)
    print(f"T={T:4.1f}: {np.round(s, 3)}")
# T=0.1 → very peaked; T=10 → nearly uniform

# Overflow with naive temperature scaling
x_large = np.array([50.0, 60.0, 70.0], dtype=np.float32)
T = 0.1
print("\n=== Overflow with small T ===")
scaled_naive = x_large / T   # [500, 600, 700] — far above fp32 overflow threshold
print(f"Logits / T = {scaled_naive}")
print(f"np.exp(700) = {np.exp(np.float32(700))}")  # inf
naive = np.exp(scaled_naive); print(f"Naive softmax: {naive / naive.sum()}")  # nan

# Stable: subtract max AFTER dividing by T
scaled_stable = scaled_naive - scaled_naive.max()
e = np.exp(scaled_stable); print(f"Stable softmax: {np.round(e / e.sum(), 4)}")

# PyTorch F.softmax is always stable
logits_t = torch.tensor(x_large)
print(f"F.softmax(x/T=0.1): {F.softmax(logits_t / T, dim=0).numpy()}")
```

## Online Softmax for Streaming Inference

Standard softmax requires two passes over the input: one to find the maximum (for stability), and one to compute exp and normalize. For memory-constrained inference (e.g., FlashAttention processing attention scores in tiles), an online one-pass algorithm is needed.

The online softmax algorithm maintains a running maximum m and a running sum s. When a new element xₜ arrives:
- m_new = max(m_old, xₜ)
- s_new = s_old × exp(m_old − m_new) + exp(xₜ − m_new)

The correction factor exp(m_old − m_new) rescales previously accumulated exp values to the new running maximum. At each step, the current estimate softmax(x_{1:t}) can be computed as exp(xᵢ − m_t) / s_t for any previous xᵢ, though in practice FlashAttention computes the weighted value accumulation online without materializing individual softmax values.

```python
import numpy as np
import torch

def online_softmax(x):
    """
    Online (one-pass) softmax — the algorithm behind FlashAttention.
    Returns softmax values with numerically stable running max/sum.
    """
    m = -np.inf   # running maximum
    s = 0.0       # running sum of exp(xᵢ - m)
    for xi in x:
        m_new = max(m, xi)
        s = s * np.exp(m - m_new) + np.exp(xi - m_new)  # rescale old, add new
        m = m_new
    return np.array([np.exp(xi - m) / s for xi in x])

def two_pass_softmax(x):
    """Standard two-pass stable softmax for comparison."""
    e = np.exp(x - x.max())
    return e / e.sum()

# Verify correctness
test_cases = [
    np.array([1.0, 2.0, 3.0]),
    np.array([1000.0, 1001.0, 1002.0]),
    np.array([-100.0, -50.0, 0.0, 50.0]),
]
print("=== Online vs Two-Pass Softmax ===")
for x in test_cases:
    online    = online_softmax(x)
    two_pass  = two_pass_softmax(x)
    max_diff  = np.max(np.abs(online - two_pass))
    print(f"x~[{x[0]:.0f}..{x[-1]:.0f}]: online={np.round(online,4)}  max_diff={max_diff:.2e}")

# Online softmax for attention (simplified FlashAttention pattern)
def flash_attention_simple(Q, K, V, scale):
    """Single-head attention with online softmax (no materialized attention matrix)."""
    T_q, T_k = Q.shape[0], K.shape[0]
    output = np.zeros_like(Q)
    for i in range(T_q):
        scores = (Q[i] @ K.T) * scale   # (T_k,)
        attn   = online_softmax(scores)  # online stable softmax
        output[i] = attn @ V
    return output

np.random.seed(42)
d, T = 8, 4
Q = np.random.randn(T, d); K = np.random.randn(T, d); V = np.random.randn(T, d)
out = flash_attention_simple(Q, K, V, scale=1.0/np.sqrt(d))
print(f"\nAttention output shape: {out.shape}, norm: {np.linalg.norm(out):.4f}")
```

## Pitfalls

Common softmax implementation mistakes:

1. **Computing log(softmax(x)) in two steps**: always use log_softmax or F.cross_entropy instead.

2. **Forgetting max-shift after temperature scaling**: temperature < 1 amplifies logits before the max-shift is applied in naive implementations.

3. **Using fp16 for attention scores without overflow check**: Q@K^T/√d can produce values above the fp16 overflow threshold of ~11 for large models with high-dimensional keys.

4. **Applying softmax along the wrong dimension**: in batched settings, softmax must be applied along dim=1 (over classes) not dim=0 (over batch). A bug here produces valid-looking outputs with wrong semantics.

## Practical Guidance

Best practices for softmax in production:

- **For classification**: always use F.cross_entropy(logits, target), never compute softmax probabilities manually and then log them.
- **For inference probabilities**: use F.softmax(logits, dim=-1) — PyTorch's implementation is internally stable.
- **For temperature sampling**: compute F.softmax(logits / T, dim=-1) in one step rather than dividing after softmax.
- **For custom attention**: ensure the softmax is computed over the correct sequence dimension and consider using F.scaled_dot_product_attention which handles numerical stability internally.
- **For numerical testing**: verify that your implementation matches F.softmax on both normal inputs [1,2,3] and extreme inputs [1000,1001,1002].

> **TIP: Use F.scaled_dot_product_attention**
>
> PyTorch 2.0+ includes F.scaled_dot_product_attention which dispatches to FlashAttention when possible, handling numerical stability (online softmax), memory efficiency (no materialized attention matrix), and mask handling correctly. Unless implementing a custom attention variant, prefer this over manual Q@K^T / sqrt(d) + softmax patterns.

| Pattern | Numerically Safe? | Preferred Alternative |
| --- | --- | --- |
| np.exp(x)/np.exp(x).sum() | No (overflow) | stable_softmax(x - x.max()) |
| torch.log(torch.softmax(x,d)) | No (nan chain) | F.log_softmax(x, dim=d) |
| -log(softmax(x)[target]) | No (two-step) | F.cross_entropy(x, target) |
| softmax(x/T) with T<1 (manual) | No (overflow) | F.softmax(x/T, dim=-1) |
| Q@K.T/sqrt(d) + softmax manually | Risky in fp16 | F.scaled_dot_product_attention |
| logaddexp.reduce(x) | Yes | torch.logsumexp(x, dim=0) |

---

## Key Takeaways

- Naive softmax overflows for x_i > 88.72 (fp32) or > 11.09 (fp16) and underflows to NaN when all logits are very negative.
- The max-shift trick softmax(x − max(x)) is mathematically identical to softmax(x) but numerically safe; it costs one extra pass to find the maximum.
- Log-softmax = x − logsumexp(x) = xᵢ − m − log Σ exp(xⱼ − m); the final output is a pure subtraction with no overflow risk.
- Always use F.cross_entropy in PyTorch — it fuses log_softmax and NLL loss in one stable operation.
- Temperature T < 1 amplifies logits by 1/T before the max-shift — always apply the max-shift after temperature scaling, not before.
- Online softmax maintains a running (max, sum) pair and rescales previously seen values when a new maximum is encountered — this is the algorithm behind FlashAttention's tiled computation.
- For production inference, use F.scaled_dot_product_attention (PyTorch 2.0+) which dispatches to FlashAttention and handles all stability and memory concerns automatically.
