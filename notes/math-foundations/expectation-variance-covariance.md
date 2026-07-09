---
title: "Expectation, Variance, Covariance, and Correlation"
slug: "expectation-variance-covariance"
description: "Expectation via LOTUS, variance and standard deviation, covariance and correlation, covariance matrices and PSD properties, conditional expectation, and the law of total variance."
tags: ["probability", "statistics", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiRXhwZWN0YXRpb24sIHZhcmlhbmNlLCBhbmQgY292YXJpYW5jZSBhcmUgdGhlIGZ1bmRhbWVudGFsIHNlY29uZC1vcmRlciBzdGF0aXN0aWNzIHRoYXQgY2hhcmFjdGVyaXNlIHByb2JhYmlsaXR5IGRpc3RyaWJ1dGlvbnMgaW4gTUwuIFRoZXkgYXBwZWFyIGV2ZXJ5d2hlcmU6IGxvc3MgZnVuY3Rpb25zIGFyZSBleHBlY3RlZCBjb3N0cywgd2VpZ2h0IGluaXRpYWxpc2F0aW9uIHN0cmF0ZWdpZXMgdGFyZ2V0IHNwZWNpZmljIHZhcmlhbmNlIGxldmVscywgZmVhdHVyZSBub3JtYWxpc2F0aW9uIGNvbnRyb2xzIGZpcnN0IGFuZCBzZWNvbmQgbW9tZW50cywgUENBIGV4dHJhY3RzIGVpZ2VudmVjdG9ycyBvZiB0aGUgY292YXJpYW5jZSBtYXRyaXgsIGFuZCBiYXRjaCBub3JtYWxpc2F0aW9uIGV4cGxpY2l0bHkgd2hpdGVucyBhY3RpdmF0aW9ucy4gVW5kZXJzdGFuZGluZyB0aGVzZSBxdWFudGl0aWVzIHJpZ29yb3VzbHkg4oCUIGluY2x1ZGluZyB0aGUgY292YXJpYW5jZSBtYXRyaXgncyBwb3NpdGl2ZSBzZW1pLWRlZmluaXRlIHByb3BlcnR5LCBjb25kaXRpb25hbCBleHBlY3RhdGlvbiwgYW5kIHRoZSBsYXcgb2YgdG90YWwgdmFyaWFuY2Ug4oCUIGlzIGVzc2VudGlhbCBmb3IgZGVzaWduaW5nIHRyYWluaW5nIHByb2NlZHVyZXMgYW5kIGRpYWdub3NpbmcgaW5zdGFiaWxpdGllcy4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJFeHBlY3RhdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBleHBlY3RhdGlvbiAoZXhwZWN0ZWQgdmFsdWUpIG9mIGEgcmFuZG9tIHZhcmlhYmxlIFggaXM6XG5cbkRpc2NyZXRlOiBFW1hdID0gzqPigpMgeCDDlyBQKFggPSB4KVxuQ29udGludW91czogRVtYXSA9IOKIq+KCi+KInl7iiJ4geCDDlyBmKHgpIGR4ICAgd2hlcmUgZiBpcyB0aGUgUERGXG5cbktleSBwcm9wZXJ0aWVzOlxuLSBMaW5lYXJpdHk6IEVbYVggKyBiWV0gPSBhIEVbWF0gKyBiIEVbWV0gKGhvbGRzIHJlZ2FyZGxlc3Mgb2YgZGVwZW5kZW5jZSBiZXR3ZWVuIFggYW5kIFkpXG4tIExPVFVTIChMYXcgb2YgdGhlIFVuY29uc2Npb3VzIFN0YXRpc3RpY2lhbik6IEVbZyhYKV0gPSDOo+KCkyBnKHgpIFAoWD14KSBvciDiiKsgZyh4KSBmKHgpIGR4IOKAlCBubyBuZWVkIHRvIGZpbmQgdGhlIGRpc3RyaWJ1dGlvbiBvZiBnKFgpIHNlcGFyYXRlbHlcbi0gRVtjb25zdGFudF0gPSBjb25zdGFudFxuLSBJZiBYIGFuZCBZIGFyZSBpbmRlcGVuZGVudDogRVtYWV0gPSBFW1hdIEVbWV1cblxuTE9UVVMgaXMgcGFydGljdWxhcmx5IHVzZWZ1bCBpbiBNTDogRVvigJZY4oCWwrJdID0g4oirIOKAlnjigJbCsiBmKHgpIGR4IGRpcmVjdGx5IGdpdmVzIHRoZSBleHBlY3RlZCBzcXVhcmVkIG5vcm0gd2l0aG91dCBjb21wdXRpbmcgdGhlIGRpc3RyaWJ1dGlvbiBvZiDigJZY4oCWwrIuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiVmFyaWFuY2UgYW5kIFN0YW5kYXJkIERldmlhdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSB2YXJpYW5jZSBtZWFzdXJlcyBzcHJlYWQgYXJvdW5kIHRoZSBtZWFuOlxuXG5WYXIoWCkgPSBFWyhYIOKIkiDOvCnCsl0gPSBFW1jCsl0g4oiSIChFW1hdKcKyICAgd2hlcmUgzrwgPSBFW1hdXG5cblRoZSBzZWNvbmQgZm9ybSAoY29tcHV0YXRpb25hbCBmb3JtdWxhKSBpcyB1c2VmdWwgZm9yIGNhbGN1bGF0aW9uIGJ1dCBudW1lcmljYWxseSB1bnN0YWJsZSB3aGVuIHRoZSBtZWFuIGlzIGxhcmdlIChjYXRhc3Ryb3BoaWMgY2FuY2VsbGF0aW9uKS4gVXNlIFdlbGZvcmQncyBhbGdvcml0aG0gZm9yIG9ubGluZSBjb21wdXRhdGlvbi5cblxuU3RhbmRhcmQgZGV2aWF0aW9uOiDPgyA9IOKImlZhcihYKSDigJQgc2FtZSB1bml0cyBhcyBYLlxuXG5LZXkgcHJvcGVydGllczpcbi0gVmFyKGFYICsgYikgPSBhwrIgVmFyKFgpIChzaGlmdCBkb2Vzbid0IGNoYW5nZSB2YXJpYW5jZTsgc2NhbGUgc3F1YXJlcylcbi0gVmFyKFggKyBZKSA9IFZhcihYKSArIFZhcihZKSArIDIgQ292KFgsIFkpXG4tIFZhcihYICsgWSkgPSBWYXIoWCkgKyBWYXIoWSkgIGlmIFggYW5kIFkgYXJlIGluZGVwZW5kZW50XG4tIFNhbXBsZSB2YXJpYW5jZTogc8KyID0gKDEvKG7iiJIxKSkgzqMoeOG1oiDiiJIgeMyEKcKyIChCZXNzZWwncyBjb3JyZWN0aW9uIGZvciB1bmJpYXNlZG5lc3MpXG5cbkJlc3NlbCdzIGNvcnJlY3Rpb24gbuKIkjEgaW5zdGVhZCBvZiBuIGFyaXNlcyBiZWNhdXNlIHRoZSBzYW1wbGUgbWVhbiB4zIQgYWxyZWFkeSB1c2VzIHRoZSBkYXRhLCBjb25zdW1pbmcgb25lIGRlZ3JlZSBvZiBmcmVlZG9tLiBUaGUgTUxFIGVzdGltYXRlIHVzZXMgbiAoYmlhc2VkIGJ1dCBtaW5pbXVtIE1TRSBmb3IgR2F1c3NpYW4pLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkgaW1wb3J0IHN0YXRzXG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0MilcblxuIyBUaGVvcmV0aWNhbCB2cyBzYW1wbGUgbW9tZW50cyBmb3IgR2F1c3NpYW4gTigzLCA0KSBbbWVhbj0zLCB2YXI9NF1cbm11X3RydWUsIHNpZ21hX3RydWUgPSAzLjAsIDIuMFxubiA9IDEwXzAwMFxuWCA9IHJuZy5ub3JtYWwobXVfdHJ1ZSwgc2lnbWFfdHJ1ZSwgbilcblxucHJpbnQoXCI9PT0gR2F1c3NpYW4gTigzLCA0KSBtb21lbnRzID09PVwiKVxucHJpbnQoZlwiVGhlb3JldGljYWwgbWVhbjogICAgIHttdV90cnVlOi40Zn1cIilcbnByaW50KGZcIlNhbXBsZSBtZWFuOiAgICAgICAgICB7bnAubWVhbihYKTouNGZ9XCIpXG5wcmludChmXCJUaGVvcmV0aWNhbCB2YXJpYW5jZToge3NpZ21hX3RydWUqKjI6LjRmfVwiKVxucHJpbnQoZlwiU2FtcGxlIHZhcmlhbmNlOiAgICAgIHtucC52YXIoWCwgZGRvZj0xKTouNGZ9ICAoQmVzc2VsJ3MgY29ycmVjdGlvbilcIilcbnByaW50KGZcIkJpYXNlZCB2YXJpYW5jZTogICAgICB7bnAudmFyKFgsIGRkb2Y9MCk6LjRmfSAgKE1MRSwgbiBkZW5vbWluYXRvcilcIilcbnByaW50KGZcIlNhbXBsZSBzdGQgZGV2OiAgICAgICB7bnAuc3RkKFgsIGRkb2Y9MSk6LjRmfVwiKVxuXG4jIExPVFVTOiBFW1heMl0gYW5kIEVbZXhwKFgpXVxucHJpbnQoXCJcXG49PT0gTE9UVVMgZXhhbXBsZXMgPT09XCIpXG5wcmludChmXCJFW1heMl0gdGhlb3JldGljYWw6ICAge211X3RydWUqKjIgKyBzaWdtYV90cnVlKioyOi40Zn0gIChtdV4yICsgc2lnbWFeMilcIilcbnByaW50KGZcIkVbWF4yXSBzYW1wbGU6ICAgICAgICB7bnAubWVhbihYKioyKTouNGZ9XCIpXG4jIEVbZXhwKFgpXSBmb3IgWH5OKG11LCBzaWdtYV4yKSA9IGV4cChtdSArIHNpZ21hXjIvMikgIFtsb2ctbm9ybWFsIGZvcm11bGFdXG5wcmludChmXCJFW2V4cChYKV0gdGhlb3JldGljYWw6e25wLmV4cChtdV90cnVlICsgc2lnbWFfdHJ1ZSoqMi8yKTouNGZ9ICAobG9nLW5vcm1hbCBNR0YpXCIpXG5wcmludChmXCJFW2V4cChYKV0gc2FtcGxlOiAgICAge25wLm1lYW4obnAuZXhwKFgpKTouNGZ9XCIpXG5cbiMgVmFyaWFuY2Ugb2Ygc3VtOiBWYXIoWCtZKSB2cyBWYXIoWCkgKyBWYXIoWSkgKyAyQ292KFgsWSlcblkgPSAwLjcgKiBYICsgcm5nLm5vcm1hbCgwLCAxLjUsIG4pICAgIyBZIGlzIGNvcnJlbGF0ZWQgd2l0aCBYXG5TID0gWCArIFlcbnByaW50KFwiXFxuPT09IFZhcmlhbmNlIG9mIFN1bSA9PT1cIilcbnByaW50KGZcIlZhcihYKToge25wLnZhcihYLCBkZG9mPTEpOi40Zn1cIilcbnByaW50KGZcIlZhcihZKToge25wLnZhcihZLCBkZG9mPTEpOi40Zn1cIilcbmNvdl94eSA9IG5wLmNvdihYLCBZLCBkZG9mPTEpWzAsIDFdXG5wcmludChmXCIyKkNvdihYLFkpOiB7Mipjb3ZfeHk6LjRmfVwiKVxucHJpbnQoZlwiVmFyKFgpK1ZhcihZKSsyQ292OiB7bnAudmFyKFgsIGRkb2Y9MSkrbnAudmFyKFksIGRkb2Y9MSkrMipjb3ZfeHk6LjRmfVwiKVxucHJpbnQoZlwiVmFyKFgrWSkgZGlyZWN0OiAgICAge25wLnZhcihTLCBkZG9mPTEpOi40Zn1cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJDb3ZhcmlhbmNlLCBDb3JyZWxhdGlvbiwgYW5kIENvdmFyaWFuY2UgTWF0cmljZXMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJDb3ZhcmlhbmNlIG1lYXN1cmVzIGxpbmVhciBkZXBlbmRlbmNlIGJldHdlZW4gdHdvIHJhbmRvbSB2YXJpYWJsZXM6XG5cbkNvdihYLCBZKSA9IEVbKFgg4oiSIM684oKTKShZIOKIkiDOvOG1pyldID0gRVtYWV0g4oiSIEVbWF0gRVtZXVxuXG5Db3YoWCwgWCkgPSBWYXIoWCkuIENvdihYLCBZKSA9IDAgZm9yIGluZGVwZW5kZW50IFgsIFkgKGJ1dCBub3QgY29udmVyc2VseSBpbiBnZW5lcmFsKS5cblxuQ29ycmVsYXRpb24gbm9ybWFsaXNlcyBjb3ZhcmlhbmNlIHRvIFviiJIxLCAxXTpcblxuz4EoWCwgWSkgPSBDb3YoWCwgWSkgLyAoz4PigpMgz4PhtacpXG5cbs+BID0gMSBtZWFucyBwZXJmZWN0IHBvc2l0aXZlIGxpbmVhciBkZXBlbmRlbmNlOyDPgSA9IOKIkjEgbWVhbnMgcGVyZmVjdCBuZWdhdGl2ZTsgz4EgPSAwIG1lYW5zIHVuY29ycmVsYXRlZCAobm90IG5lY2Vzc2FyaWx5IGluZGVwZW5kZW50KS5cblxuRm9yIGEgZC1kaW1lbnNpb25hbCByYW5kb20gdmVjdG9yIFggPSAoWOKCgSwg4oCmLCBYZCleVCwgdGhlIGNvdmFyaWFuY2UgbWF0cml4IM6jIOKIiCDihJ1ee2TDl2R9IGhhcyBlbnRyaWVzOlxuXG7Oo+G1ouKxvCA9IENvdihY4bWiLCBY4rG8KVxuXG5LZXkgcHJvcGVydGllcyBvZiDOozpcbi0gU3ltbWV0cmljOiDOoyA9IM6jXlQgKHNpbmNlIENvdihYLFkpID0gQ292KFksWCkpXG4tIFBvc2l0aXZlIHNlbWktZGVmaW5pdGUgKFBTRCk6IHZeVCDOoyB2IOKJpSAwIGZvciBhbGwgdiAodmFyaWFuY2Ugb2YgYW55IGxpbmVhciBjb21iaW5hdGlvbiBpcyBub24tbmVnYXRpdmUpXG4tIERpYWdvbmFsIHdoZW4gY29tcG9uZW50cyBhcmUgdW5jb3JyZWxhdGVkXG4tIFRoZSBwcmVjaXNpb24gbWF0cml4IM6bID0gzqPigbvCuSAod2hlbiBpdCBleGlzdHMpIGFwcGVhcnMgaW4gdGhlIEdhdXNzaWFuIGV4cG9uZW50OiDiiJLCvSh44oiSzrwpXlQgzpsgKHjiiJLOvCkifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgc2NpcHkubGluYWxnXG5cbiMgQ292YXJpYW5jZSBtYXRyaXg6IGNvbnN0cnVjdGlvbiBhbmQgUFNEIHZlcmlmaWNhdGlvblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxuZCwgbiA9IDQsIDEwMDBcbkEgPSBybmcuc3RhbmRhcmRfbm9ybWFsKChkLCBkKSlcblNpZ21hX3RydWUgPSBBIEAgQS5UIC8gZCArIDAuMSAqIG5wLmV5ZShkKSAgIyBndWFyYW50ZWVkIFBTRFxuXG4jIFNhbXBsZSBjb3ZhcmlhbmNlIG1hdHJpeFxuWCA9IHJuZy5tdWx0aXZhcmlhdGVfbm9ybWFsKG1lYW49bnAuemVyb3MoZCksIGNvdj1TaWdtYV90cnVlLCBzaXplPW4pXG5TaWdtYV9oYXQgPSBucC5jb3YoWC5ULCBkZG9mPTEpICAgIyAoZCwgZCkgc2FtcGxlIGNvdmFyaWFuY2VcblxucHJpbnQoXCI9PT0gQ292YXJpYW5jZSBNYXRyaXggPT09XCIpXG5wcmludChmXCJUcnVlIFNpZ21hIChkaWFnb25hbCk6XFxue25wLmRpYWcoU2lnbWFfdHJ1ZSkucm91bmQoMyl9XCIpXG5wcmludChmXCJTYW1wbGUgU2lnbWEgKGRpYWdvbmFsKTpcXG57bnAuZGlhZyhTaWdtYV9oYXQpLnJvdW5kKDMpfVwiKVxuXG4jIFZlcmlmeSBQU0Q6IGFsbCBlaWdlbnZhbHVlcyA+PSAwXG5laWdlbnZhbHVlcyA9IG5wLmxpbmFsZy5laWd2YWxzaChTaWdtYV9oYXQpXG5wcmludChmXCJcXG5FaWdlbnZhbHVlcyBvZiBTaWdtYV9oYXQ6IHtlaWdlbnZhbHVlcy5yb3VuZCg0KX1cIilcbnByaW50KGZcIkFsbCBlaWdlbnZhbHVlcyA+PSAwOiB7bnAuYWxsKGVpZ2VudmFsdWVzID49IC0xZS0xMCl9XCIpICAjIFBTRFxuXG4jIENvcnJlbGF0aW9uIG1hdHJpeCBmcm9tIGNvdmFyaWFuY2VcbkQgPSBucC5kaWFnKDEuMCAvIG5wLnNxcnQobnAuZGlhZyhTaWdtYV9oYXQpKSlcbkNvcnIgPSBEIEAgU2lnbWFfaGF0IEAgRFxucHJpbnQoZlwiXFxuQ29ycmVsYXRpb24gbWF0cml4IGRpYWdvbmFsIChzaG91bGQgYmUgMXMpOiB7bnAuZGlhZyhDb3JyKS5yb3VuZCg0KX1cIilcbnByaW50KGZcIkNvcnJbMCwxXSA9IHtDb3JyWzAsMV06LjRmfVwiKVxuXG4jIFByZWNpc2lvbiBtYXRyaXggKGludmVyc2UgY292YXJpYW5jZSlcbkxhbWJkYSA9IG5wLmxpbmFsZy5pbnYoU2lnbWFfaGF0KVxucHJpbnQoZlwiXFxuUHJlY2lzaW9uIG1hdHJpeCAodG9wLWxlZnQgMngyKTpcXG57TGFtYmRhWzoyLDoyXS5yb3VuZCgzKX1cIilcblxuIyBWZXJpZnkgU2lnbWEgQCBMYW1iZGEgPSBJXG5wcm9kID0gU2lnbWFfaGF0IEAgTGFtYmRhXG5wcmludChmXCJTaWdtYSBAIExhbWJkYSA9IEk/IG1heF9vZmZfZGlhZz17bnAubWF4KG5wLmFicyhwcm9kIC0gbnAuZXllKGQpKSk6LjJlfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkNvbmRpdGlvbmFsIEV4cGVjdGF0aW9uIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIGNvbmRpdGlvbmFsIGV4cGVjdGF0aW9uIEVbWXxYXSBpcyBhIGZ1bmN0aW9uIG9mIFggdGhhdCBnaXZlcyB0aGUgZXhwZWN0ZWQgdmFsdWUgb2YgWSBnaXZlbiB0aGUgb2JzZXJ2ZWQgdmFsdWUgb2YgWDpcblxuRVtZfFggPSB4XSA9IOKIqyB5IGYoeXx4KSBkeVxuXG5LZXkgcHJvcGVydGllczpcbi0gVG93ZXIgcHJvcGVydHkgKGxhdyBvZiBpdGVyYXRlZCBleHBlY3RhdGlvbik6IEVbRVtZfFhdXSA9IEVbWV1cbi0gRVtnKFgpIFkgfCBYXSA9IGcoWCkgRVtZfFhdICAodGFrZS1vdXQtd2hhdC1pcy1rbm93bilcbi0gRVtZfFhdIGlzIHRoZSBiZXN0IHByZWRpY3RvciBvZiBZIGdpdmVuIFggaW4gdGhlIG1lYW4gc3F1YXJlZCBlcnJvciBzZW5zZTogYXJnbWluX3tmKFgpfSBFWyhZIOKIkiBmKFgpKcKyXSA9IEVbWXxYXVxuXG5UaGUgdG93ZXIgcHJvcGVydHkgc2F5czogZmlyc3QgY29tcHV0ZSB0aGUgY29uZGl0aW9uYWwgZXhwZWN0YXRpb24gKGdpdmVuIFgpLCB0aGVuIGF2ZXJhZ2Ugb3ZlciBYIOKAlCB0aGUgcmVzdWx0IGVxdWFscyB0aGUgdW5jb25kaXRpb25hbCBleHBlY3RhdGlvbi4gVGhpcyBpcyB3aHkgTW9udGUgQ2FybG8gZXN0aW1hdGVzIGFyZSB1bmJpYXNlZDogRV94W2YoeCldID0gRVtmKFgpXSB3aGVuIHggfiBwKFgpLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkxhdyBvZiBUb3RhbCBWYXJpYW5jZSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBsYXcgb2YgdG90YWwgdmFyaWFuY2UgKEV2ZSdzIGxhdykgZGVjb21wb3NlcyB2YXJpYW5jZSBpbnRvIGV4cGxhaW5lZCBhbmQgdW5leHBsYWluZWQgY29tcG9uZW50czpcblxuVmFyKFkpID0gRVtWYXIoWXxYKV0gKyBWYXIoRVtZfFhdKVxuXG5JbnRlcnByZXRhdGlvbjpcbi0gVmFyKFl8WCk6IHZhcmlhbmNlIG9mIFkgd2l0aGluIGVhY2ggZ3JvdXAgZGVmaW5lZCBieSBYICh1bmV4cGxhaW5lZCB2YXJpYW5jZSlcbi0gRVtWYXIoWXxYKV06IGF2ZXJhZ2Ugd2l0aGluLWdyb3VwIHZhcmlhbmNlICh3aGF0IHJlbWFpbnMgdW5wcmVkaWN0YWJsZSBldmVuIGtub3dpbmcgWClcbi0gVmFyKEVbWXxYXSk6IHZhcmlhbmNlIG9mIHRoZSBjb25kaXRpb25hbCBtZWFuIGFjcm9zcyBncm91cHMgKGJldHdlZW4tZ3JvdXAgdmFyaWFuY2UpXG4tIFZhcihFW1l8WF0pOiB0aGUgcmVkdWN0aW9uIGluIHZhcmlhbmNlIGFjaGlldmVkIGJ5IGtub3dpbmcgWCDigJQgdGhlIGV4cGxhaW5lZCB2YXJpYW5jZVxuXG5JbiBNTDogUsKyIChjb2VmZmljaWVudCBvZiBkZXRlcm1pbmF0aW9uKSA9IFZhcihFW1l8WF0pIC8gVmFyKFkpID0gZnJhY3Rpb24gb2YgdmFyaWFuY2UgZXhwbGFpbmVkIGJ5IHRoZSBtb2RlbC4gVGhlIGxhdyBvZiB0b3RhbCB2YXJpYW5jZSBhbHNvIHVuZGVybGllcyB0aGUgYmlhcy12YXJpYW5jZSBkZWNvbXBvc2l0aW9uIG9mIE1TRTogRVsoWSDiiJIgxbcpwrJdID0gQmlhc8KyICsgVmFyaWFuY2UgKyBOb2lzZS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0Milcbm4gPSAxMDBfMDAwXG5cbiMgTGF3IG9mIHRvdGFsIHZhcmlhbmNlIGRlbW9uc3RyYXRpb25cbiMgWSBkZXBlbmRzIG9uIFg6IFkgfCBYPXggfiBOKDJ4LCB4XjIpICAobWVhbiBhbmQgdmFyaWFuY2UgYm90aCBkZXBlbmQgb24geClcblggPSBybmcuZXhwb25lbnRpYWwoc2NhbGU9MS4wLCBzaXplPW4pICAgIyBYIH4gRXhwKDEpXG5ZID0gcm5nLm5vcm1hbChsb2M9MipYLCBzY2FsZT1YKSAgICAgICAgICAjIFl8WCB+IE4oMlgsIFheMilcblxuIyBUaGVvcmV0aWNhbCB2YWx1ZXNcbiMgRVtZXSA9IEVbRVtZfFhdXSA9IEVbMlhdID0gMipFW1hdID0gMioxID0gMlxuIyBFW1ZhcihZfFgpXSA9IEVbWF4yXSA9IFZhcihYKSArIEVbWF1eMiA9IDEgKyAxID0gMlxuIyBWYXIoRVtZfFhdKSA9IFZhcigyWCkgPSA0KlZhcihYKSA9IDQqMSA9IDRcbiMgVmFyKFkpID0gRVtWYXIoWXxYKV0gKyBWYXIoRVtZfFhdKSA9IDIgKyA0ID0gNlxuXG5FX1lfZ2l2ZW5fWCA9IDIgKiBYICAgICAgICMgRVtZfFg9eF0gPSAyeFxuVmFyX1lfZ2l2ZW5fWCA9IFgqKjIgICAgICAgIyBWYXIoWXxYPXgpID0geF4yIChzdGQgZGV2ID0geClcblxucHJpbnQoXCI9PT0gTGF3IG9mIFRvdGFsIFZhcmlhbmNlID09PVwiKVxucHJpbnQoZlwiRVtZXSB0aGVvcmV0aWNhbDogICAgICAgIDIuMDAwMFwiKVxucHJpbnQoZlwiRVtZXSBzYW1wbGU6ICAgICAgICAgICAgIHtucC5tZWFuKFkpOi40Zn1cIilcbnByaW50KClcbnByaW50KGZcIkVbVmFyKFl8WCldIHRoZW9yZXRpY2FsOiAyLjAwMDBcIilcbnByaW50KGZcIkVbVmFyKFl8WCldIHNhbXBsZTogICAgICB7bnAubWVhbihWYXJfWV9naXZlbl9YKTouNGZ9XCIpXG5wcmludCgpXG5wcmludChmXCJWYXIoRVtZfFhdKSB0aGVvcmV0aWNhbDogNC4wMDAwXCIpXG5wcmludChmXCJWYXIoRVtZfFhdKSBzYW1wbGU6ICAgICAge25wLnZhcihFX1lfZ2l2ZW5fWCk6LjRmfVwiKVxucHJpbnQoKVxucHJpbnQoZlwiVmFyKFkpIHRoZW9yZXRpY2FsOiAgICAgIDYuMDAwMFwiKVxucHJpbnQoZlwiVmFyKFkpIHNhbXBsZTogICAgICAgICAgIHtucC52YXIoWSk6LjRmfVwiKVxucHJpbnQoZlwiU3VtIGNoZWNrOiAgICAgICAgICAgICAgIHtucC5tZWFuKFZhcl9ZX2dpdmVuX1gpICsgbnAudmFyKEVfWV9naXZlbl9YKTouNGZ9XCIpXG5cbiMgRnJhY3Rpb24gb2YgdmFyaWFuY2UgZXhwbGFpbmVkIChSLXNxdWFyZWQgYW5hbG9nKVxuUjIgPSBucC52YXIoRV9ZX2dpdmVuX1gpIC8gbnAudmFyKFkpXG5wcmludChmXCJcXG5GcmFjdGlvbiBvZiBWYXIoWSkgZXhwbGFpbmVkIGJ5IFg6IHtSMjouNGZ9XCIpXG5wcmludChmXCIoPSBWYXIoRVtZfFhdKSAvIFZhcihZKSA9IDQvNiA9IHs0LzY6LjRmfSlcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNTCBhbmQgQUkgQ29ubmVjdGlvbnMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJTZWNvbmQtb3JkZXIgc3RhdGlzdGljcyBwZXJ2YWRlIE1MIHRoZW9yeSBhbmQgcHJhY3RpY2U6XG5cbi0gKipXZWlnaHQgaW5pdGlhbGlzYXRpb24qKjogSGUgaW5pdGlhbGlzYXRpb24gZm9yIFJlTFUgc2V0cyBWYXIoVykgPSAyL2Zhbl9pbiB0byBwcmVzZXJ2ZSB2YXJpYW5jZSBhY3Jvc3MgbGF5ZXJzLiBYYXZpZXIvR2xvcm90IHRhcmdldHMgVmFyKFcpID0gMi8oZmFuX2luICsgZmFuX291dCkuIEJvdGggZGVyaXZlIGZyb20gdGhlIHJlcXVpcmVtZW50IFZhcihvdXRwdXQpID0gVmFyKGlucHV0KS5cblxuLSAqKkJhdGNoIG5vcm1hbGlzYXRpb24qKjogZXhwbGljaXRseSBzZXRzIEVbYWN0aXZhdGlvbnNdID0gMCBhbmQgVmFyKGFjdGl2YXRpb25zKSA9IDEgYXQgZWFjaCBsYXllciAodGhlbiByZXNjYWxlcyB3aXRoIGxlYXJuYWJsZSDOsywgzrIpLiBUaGlzIHdoaXRlbnMgYWN0aXZhdGlvbnMsIHJlZHVjaW5nIGNvdmFyaWF0ZSBzaGlmdC5cblxuLSAqKlBDQSoqOiBleHRyYWN0cyBlaWdlbnZlY3RvcnMgb2YgdGhlIHNhbXBsZSBjb3ZhcmlhbmNlIG1hdHJpeCwgcmFua2VkIGJ5IGVpZ2VudmFsdWUgKHZhcmlhbmNlKS4gVGhlIHRvcC1rIGVpZ2VudmVjdG9ycyBjYXB0dXJlIHRoZSBrIGRpbWVuc2lvbnMgb2YgbWF4aW11bSB2YXJpYW5jZS5cblxuLSAqKkthbG1hbiBmaWx0ZXIqKjogbWFpbnRhaW5zIGEgR2F1c3NpYW4gcG9zdGVyaW9yIHdpdGggbWVhbiAoY29uZGl0aW9uYWwgZXhwZWN0YXRpb24pIGFuZCBjb3ZhcmlhbmNlIChjb25kaXRpb25hbCB2YXJpYW5jZSkgdGhhdCBhcmUgdXBkYXRlZCB3aXRoIGVhY2ggbmV3IG9ic2VydmF0aW9uLlxuXG4tICoqR2F1c3NpYW4gcHJvY2VzcyByZWdyZXNzaW9uKio6IHBvc3RlcmlvciBtZWFuIGlzIHRoZSBNTVNFIGVzdGltYXRlIEVbZih4Kil8ZGF0YV07IHBvc3RlcmlvciB2YXJpYW5jZSBxdWFudGlmaWVzIHVuY2VydGFpbnR5LiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQ29tbW9uIG1pc3Rha2VzIHdpdGggc2Vjb25kLW9yZGVyIHN0YXRpc3RpY3M6XG5cbjEuICoqVXNpbmcgbiBpbnN0ZWFkIG9mIG7iiJIxIGZvciBzYW1wbGUgdmFyaWFuY2UqKjogdGhlIE1MRSBlc3RpbWF0ZSAobiBkZW5vbWluYXRvcikgdW5kZXJlc3RpbWF0ZXMgdGhlIHRydWUgdmFyaWFuY2UsIGVzcGVjaWFsbHkgZm9yIHNtYWxsIG4uIFVzZSBkZG9mPTEgaW4gbnVtcHkuXG5cbjIuICoqQ29tcHV0aW5nIHZhcmlhbmNlIGFzIEVbWMKyXSDiiJIgRVtYXcKyIGZvciBsYXJnZSBtZWFucyoqOiBjYXRhc3Ryb3BoaWMgY2FuY2VsbGF0aW9uIHdoZW4gYm90aCB0ZXJtcyBhcmUgbGFyZ2UgYW5kIG5lYXJseSBlcXVhbC4gVXNlIFdlbGZvcmQncyBhbGdvcml0aG0gb3IgY2VudHJlIHRoZSBkYXRhIGZpcnN0LlxuXG4zLiAqKlRyZWF0aW5nIHplcm8gY29ycmVsYXRpb24gYXMgaW5kZXBlbmRlbmNlKio6IHplcm8gY292YXJpYW5jZSDiiaAgaW5kZXBlbmRlbmNlIGV4Y2VwdCBmb3Igam9pbnRseSBHYXVzc2lhbiB2YXJpYWJsZXMuIEV4YW1wbGU6IFkgPSBYwrIsIHdoZXJlIFggfiBOKDAsMSk6IENvdihYLCBZKSA9IEVbWMKzXSA9IDAgYnV0IFggYW5kIFkgYXJlIGhpZ2hseSBkZXBlbmRlbnQuXG5cbjQuICoqQXNzdW1pbmcgY292YXJpYW5jZSBtYXRyaXggaXMgaW52ZXJ0aWJsZSoqOiBzaW5ndWxhciBjb3ZhcmlhbmNlIChyYW5rIGRlZmljaWVudCkgb2NjdXJzIHdoZW4gZmVhdHVyZXMgYXJlIHBlcmZlY3RseSBjb3JyZWxhdGVkIG9yIG4gPCBkLiBVc2UgcHNldWRvaW52ZXJzZSBvciBhZGQgcmVndWxhcmlzYXRpb24gzrtJLiJ9LCB7InR5cGUiOiAiY2FsbG91dCIsICJ2YXJpYW50IjogInRpcCIsICJ0aXRsZSI6ICJQU0QgYW5kIHRoZSBDaG9sZXNreSBEZWNvbXBvc2l0aW9uIiwgImNvbnRlbnQiOiAiQW55IHZhbGlkIGNvdmFyaWFuY2UgbWF0cml4IM6jIGlzIHBvc2l0aXZlIHNlbWktZGVmaW5pdGUgKFBTRCkuIFRoZSBDaG9sZXNreSBkZWNvbXBvc2l0aW9uIM6jID0gTCBMXlQgKHdoZXJlIEwgaXMgbG93ZXIgdHJpYW5ndWxhcikgZXhpc3RzIGlmZiDOoyBpcyBQU0QuIEl0IGlzIHRoZSBlZmZpY2llbnQgd2F5IHRvOiAoMSkgc2FtcGxlIGZyb20gTijOvCzOoykgYXMgzrwgKyBMIHogd2hlcmUgeiB+IE4oMCxJKTsgKDIpIHNvbHZlIM6jIHggPSBiIGFzIHR3byB0cmlhbmd1bGFyIHNvbHZlczsgKDMpIGNvbXB1dGUgbG9nIGRldCjOoykgPSAyIM6jIGxvZyhM4bWi4bWiKSBpbiBPKGTCsikgaW5zdGVhZCBvZiBPKGTCsykuIEFsd2F5cyB1c2UgQ2hvbGVza3kgb3ZlciBkaXJlY3QgbWF0cml4IGludmVyc2UgZm9yIGNvdmFyaWFuY2Ugb3BlcmF0aW9ucy4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIlF1YW50aXR5IiwgIkRlZmluaXRpb24iLCAiS2V5IFByb3BlcnR5IiwgIk1MIEFwcGxpY2F0aW9uIl0sICJyb3dzIjogW1siRVtYXSIsICLOoyB4IHAoeCkgb3Ig4oirIHggZih4KSBkeCIsICJMaW5lYXJpdHk7IEVbYVgrYlldPWFFW1hdK2JFW1ldIiwgIkxvc3MgaXMgZXhwZWN0ZWQgY29zdCJdLCBbIlZhcihYKSIsICJFWyhY4oiSzrwpwrJdIiwgIlZhcihhWCk9YcKyVmFyKFgpIiwgIldlaWdodCBpbml0LCBiYXRjaCBub3JtIl0sIFsiQ292KFgsWSkiLCAiRVsoWOKIks684oKTKShZ4oiSzrzhtacpXSIsICIwIGZvciBpbmRlcGVuZGVudDsgzqPhtaLhtaI9VmFyKFjhtaIpIiwgIkZlYXR1cmUgY29ycmVsYXRpb24iXSwgWyJDb3JyKFgsWSkiLCAiQ292KFgsWSkvKM+D4oKTz4PhtacpIiwgIuKIiCBb4oiSMSwxXTsgc2NhbGUtaW52YXJpYW50IiwgIkZlYXR1cmUgc2VsZWN0aW9uIl0sIFsiQ292YXJpYW5jZSBtYXRyaXggzqMiLCAizqPhtaLisbw9Q292KFjhtaIsWOKxvCkiLCAiQWx3YXlzIFBTRCwgc3ltbWV0cmljIiwgIlBDQSwgR1BzLCBLYWxtYW4iXSwgWyJFW1l8WF0iLCAiQmVzdCBNU0UgcHJlZGljdG9yIG9mIFkgZ2l2ZW4gWCIsICJUb3dlciBwcm9wZXJ0eTogRVtFW1l8WF1dPUVbWV0iLCAiUmVncmVzc2lvbiB0YXJnZXQiXSwgWyJWYXIoWSkiLCAiRVtWYXIoWXxYKV0rVmFyKEVbWXxYXSkiLCAiVG90YWw9d2l0aGluK2JldHdlZW4iLCAiQmlhcy12YXJpYW5jZSB0cmFkZW9mZiJdXX0sIHsidHlwZSI6ICJkaXZpZGVyIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2V5IFRha2Vhd2F5cyJ9LCB7InR5cGUiOiAibGlzdCIsICJvcmRlcmVkIjogZmFsc2UsICJpdGVtcyI6IFsiRVtYXSBpcyB0aGUgcHJvYmFiaWxpdHktd2VpZ2h0ZWQgYXZlcmFnZTsgbGluZWFyaXR5IEVbYVgrYlldPWFFW1hdK2JFW1ldIGhvbGRzIHJlZ2FyZGxlc3Mgb2YgZGVwZW5kZW5jZSBiZXR3ZWVuIFggYW5kIFkuIiwgIkxPVFVTOiBFW2coWCldID0g4oirIGcoeCkgZih4KSBkeCDigJQgbm8gbmVlZCB0byBmaW5kIHRoZSBkaXN0cmlidXRpb24gb2YgZyhYKSB0byBjb21wdXRlIGl0cyBleHBlY3RhdGlvbi4iLCAiVmFyKFgpID0gRVtYwrJdIOKIkiBFW1hdwrI7IHNhbXBsZSB2YXJpYW5jZSB1c2VzIGRkb2Y9MSAoQmVzc2VsJ3MgY29ycmVjdGlvbikgZm9yIHVuYmlhc2VkbmVzcy4iLCAiQ292KFgsWSkgPSBFW1hZXSDiiJIgRVtYXUVbWV07IHplcm8gY292YXJpYW5jZSBkb2VzIG5vdCBpbXBseSBpbmRlcGVuZGVuY2UgZXhjZXB0IGZvciBqb2ludGx5IEdhdXNzaWFuIHZhcmlhYmxlcy4iLCAiQW55IGNvdmFyaWFuY2UgbWF0cml4IM6jIGlzIHN5bW1ldHJpYyBhbmQgcG9zaXRpdmUgc2VtaS1kZWZpbml0ZSAoUFNEKSDigJQgYWxsIGVpZ2VudmFsdWVzIOKJpSAwOyB1c2UgQ2hvbGVza3kgZm9yIGVmZmljaWVudCBzYW1wbGluZyBhbmQgbG9nLWRldGVybWluYW50IGNvbXB1dGF0aW9uLiIsICJUaGUgY29uZGl0aW9uYWwgZXhwZWN0YXRpb24gRVtZfFhdIGlzIHRoZSBiZXN0IE1TRSBwcmVkaWN0b3Igb2YgWSBnaXZlbiBYOyB0aGUgdG93ZXIgcHJvcGVydHkgRVtFW1l8WF1dPUVbWV0gaXMgdGhlIGZvdW5kYXRpb24gb2YgTW9udGUgQ2FybG8gdW5iaWFzZWRuZXNzLiIsICJMYXcgb2YgdG90YWwgdmFyaWFuY2U6IFZhcihZKT1FW1ZhcihZfFgpXStWYXIoRVtZfFhdKSDigJQgdG90YWwgdmFyaWFuY2UgPSB3aXRoaW4tZ3JvdXAgKyBiZXR3ZWVuLWdyb3VwOyBSwrIgPSBWYXIoRVtZfFhdKS9WYXIoWSkgaXMgdGhlIGZyYWN0aW9uIGV4cGxhaW5lZC4iXX1d"
---
# Expectation, Variance, Covariance, and Correlation

Expectation, variance, and covariance are the fundamental second-order statistics that characterise probability distributions in ML. They appear everywhere: loss functions are expected costs, weight initialisation strategies target specific variance levels, feature normalisation controls first and second moments, PCA extracts eigenvectors of the covariance matrix, and batch normalisation explicitly whitens activations. Understanding these quantities rigorously — including the covariance matrix's positive semi-definite property, conditional expectation, and the law of total variance — is essential for designing training procedures and diagnosing instabilities.

## Expectation

The expectation (expected value) of a random variable X is:

Discrete: E[X] = Σₓ x × P(X = x)
Continuous: E[X] = ∫₋∞^∞ x × f(x) dx   where f is the PDF

Key properties:
- Linearity: E[aX + bY] = a E[X] + b E[Y] (holds regardless of dependence between X and Y)
- LOTUS (Law of the Unconscious Statistician): E[g(X)] = Σₓ g(x) P(X=x) or ∫ g(x) f(x) dx — no need to find the distribution of g(X) separately
- E[constant] = constant
- If X and Y are independent: E[XY] = E[X] E[Y]

LOTUS is particularly useful in ML: E[‖X‖²] = ∫ ‖x‖² f(x) dx directly gives the expected squared norm without computing the distribution of ‖X‖².

## Variance and Standard Deviation

The variance measures spread around the mean:

Var(X) = E[(X − μ)²] = E[X²] − (E[X])²   where μ = E[X]

The second form (computational formula) is useful for calculation but numerically unstable when the mean is large (catastrophic cancellation). Use Welford's algorithm for online computation.

Standard deviation: σ = √Var(X) — same units as X.

Key properties:
- Var(aX + b) = a² Var(X) (shift doesn't change variance; scale squares)
- Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y)
- Var(X + Y) = Var(X) + Var(Y)  if X and Y are independent
- Sample variance: s² = (1/(n−1)) Σ(xᵢ − x̄)² (Bessel's correction for unbiasedness)

Bessel's correction n−1 instead of n arises because the sample mean x̄ already uses the data, consuming one degree of freedom. The MLE estimate uses n (biased but minimum MSE for Gaussian).

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Theoretical vs sample moments for Gaussian N(3, 4) [mean=3, var=4]
mu_true, sigma_true = 3.0, 2.0
n = 10_000
X = rng.normal(mu_true, sigma_true, n)

print("=== Gaussian N(3, 4) moments ===")
print(f"Theoretical mean:     {mu_true:.4f}")
print(f"Sample mean:          {np.mean(X):.4f}")
print(f"Theoretical variance: {sigma_true**2:.4f}")
print(f"Sample variance:      {np.var(X, ddof=1):.4f}  (Bessel's correction)")
print(f"Biased variance:      {np.var(X, ddof=0):.4f}  (MLE, n denominator)")
print(f"Sample std dev:       {np.std(X, ddof=1):.4f}")

# LOTUS: E[X^2] and E[exp(X)]
print("\n=== LOTUS examples ===")
print(f"E[X^2] theoretical:   {mu_true**2 + sigma_true**2:.4f}  (mu^2 + sigma^2)")
print(f"E[X^2] sample:        {np.mean(X**2):.4f}")
# E[exp(X)] for X~N(mu, sigma^2) = exp(mu + sigma^2/2)  [log-normal formula]
print(f"E[exp(X)] theoretical:{np.exp(mu_true + sigma_true**2/2):.4f}  (log-normal MGF)")
print(f"E[exp(X)] sample:     {np.mean(np.exp(X)):.4f}")

# Variance of sum: Var(X+Y) vs Var(X) + Var(Y) + 2Cov(X,Y)
Y = 0.7 * X + rng.normal(0, 1.5, n)   # Y is correlated with X
S = X + Y
print("\n=== Variance of Sum ===")
print(f"Var(X): {np.var(X, ddof=1):.4f}")
print(f"Var(Y): {np.var(Y, ddof=1):.4f}")
cov_xy = np.cov(X, Y, ddof=1)[0, 1]
print(f"2*Cov(X,Y): {2*cov_xy:.4f}")
print(f"Var(X)+Var(Y)+2Cov: {np.var(X, ddof=1)+np.var(Y, ddof=1)+2*cov_xy:.4f}")
print(f"Var(X+Y) direct:     {np.var(S, ddof=1):.4f}")
```

## Covariance, Correlation, and Covariance Matrices

Covariance measures linear dependence between two random variables:

Cov(X, Y) = E[(X − μₓ)(Y − μᵧ)] = E[XY] − E[X] E[Y]

Cov(X, X) = Var(X). Cov(X, Y) = 0 for independent X, Y (but not conversely in general).

Correlation normalises covariance to [−1, 1]:

ρ(X, Y) = Cov(X, Y) / (σₓ σᵧ)

ρ = 1 means perfect positive linear dependence; ρ = −1 means perfect negative; ρ = 0 means uncorrelated (not necessarily independent).

For a d-dimensional random vector X = (X₁, …, Xd)^T, the covariance matrix Σ ∈ ℝ^{d×d} has entries:

Σᵢⱼ = Cov(Xᵢ, Xⱼ)

Key properties of Σ:
- Symmetric: Σ = Σ^T (since Cov(X,Y) = Cov(Y,X))
- Positive semi-definite (PSD): v^T Σ v ≥ 0 for all v (variance of any linear combination is non-negative)
- Diagonal when components are uncorrelated
- The precision matrix Λ = Σ⁻¹ (when it exists) appears in the Gaussian exponent: −½(x−μ)^T Λ (x−μ)

```python
import numpy as np
import scipy.linalg

# Covariance matrix: construction and PSD verification
rng = np.random.default_rng(42)
d, n = 4, 1000
A = rng.standard_normal((d, d))
Sigma_true = A @ A.T / d + 0.1 * np.eye(d)  # guaranteed PSD

# Sample covariance matrix
X = rng.multivariate_normal(mean=np.zeros(d), cov=Sigma_true, size=n)
Sigma_hat = np.cov(X.T, ddof=1)   # (d, d) sample covariance

print("=== Covariance Matrix ===")
print(f"True Sigma (diagonal):\n{np.diag(Sigma_true).round(3)}")
print(f"Sample Sigma (diagonal):\n{np.diag(Sigma_hat).round(3)}")

# Verify PSD: all eigenvalues >= 0
eigenvalues = np.linalg.eigvalsh(Sigma_hat)
print(f"\nEigenvalues of Sigma_hat: {eigenvalues.round(4)}")
print(f"All eigenvalues >= 0: {np.all(eigenvalues >= -1e-10)}")  # PSD

# Correlation matrix from covariance
D = np.diag(1.0 / np.sqrt(np.diag(Sigma_hat)))
Corr = D @ Sigma_hat @ D
print(f"\nCorrelation matrix diagonal (should be 1s): {np.diag(Corr).round(4)}")
print(f"Corr[0,1] = {Corr[0,1]:.4f}")

# Precision matrix (inverse covariance)
Lambda = np.linalg.inv(Sigma_hat)
print(f"\nPrecision matrix (top-left 2x2):\n{Lambda[:2,:2].round(3)}")

# Verify Sigma @ Lambda = I
prod = Sigma_hat @ Lambda
print(f"Sigma @ Lambda = I? max_off_diag={np.max(np.abs(prod - np.eye(d))):.2e}")
```

## Conditional Expectation

The conditional expectation E[Y|X] is a function of X that gives the expected value of Y given the observed value of X:

E[Y|X = x] = ∫ y f(y|x) dy

Key properties:
- Tower property (law of iterated expectation): E[E[Y|X]] = E[Y]
- E[g(X) Y | X] = g(X) E[Y|X]  (take-out-what-is-known)
- E[Y|X] is the best predictor of Y given X in the mean squared error sense: argmin_{f(X)} E[(Y − f(X))²] = E[Y|X]

The tower property says: first compute the conditional expectation (given X), then average over X — the result equals the unconditional expectation. This is why Monte Carlo estimates are unbiased: E_x[f(x)] = E[f(X)] when x ~ p(X).

## Law of Total Variance

The law of total variance (Eve's law) decomposes variance into explained and unexplained components:

Var(Y) = E[Var(Y|X)] + Var(E[Y|X])

Interpretation:
- Var(Y|X): variance of Y within each group defined by X (unexplained variance)
- E[Var(Y|X)]: average within-group variance (what remains unpredictable even knowing X)
- Var(E[Y|X]): variance of the conditional mean across groups (between-group variance)
- Var(E[Y|X]): the reduction in variance achieved by knowing X — the explained variance

In ML: R² (coefficient of determination) = Var(E[Y|X]) / Var(Y) = fraction of variance explained by the model. The law of total variance also underlies the bias-variance decomposition of MSE: E[(Y − ŷ)²] = Bias² + Variance + Noise.

```python
import numpy as np

rng = np.random.default_rng(42)
n = 100_000

# Law of total variance demonstration
# Y depends on X: Y | X=x ~ N(2x, x^2)  (mean and variance both depend on x)
X = rng.exponential(scale=1.0, size=n)   # X ~ Exp(1)
Y = rng.normal(loc=2*X, scale=X)          # Y|X ~ N(2X, X^2)

# Theoretical values
# E[Y] = E[E[Y|X]] = E[2X] = 2*E[X] = 2*1 = 2
# E[Var(Y|X)] = E[X^2] = Var(X) + E[X]^2 = 1 + 1 = 2
# Var(E[Y|X]) = Var(2X) = 4*Var(X) = 4*1 = 4
# Var(Y) = E[Var(Y|X)] + Var(E[Y|X]) = 2 + 4 = 6

E_Y_given_X = 2 * X       # E[Y|X=x] = 2x
Var_Y_given_X = X**2       # Var(Y|X=x) = x^2 (std dev = x)

print("=== Law of Total Variance ===")
print(f"E[Y] theoretical:        2.0000")
print(f"E[Y] sample:             {np.mean(Y):.4f}")
print()
print(f"E[Var(Y|X)] theoretical: 2.0000")
print(f"E[Var(Y|X)] sample:      {np.mean(Var_Y_given_X):.4f}")
print()
print(f"Var(E[Y|X]) theoretical: 4.0000")
print(f"Var(E[Y|X]) sample:      {np.var(E_Y_given_X):.4f}")
print()
print(f"Var(Y) theoretical:      6.0000")
print(f"Var(Y) sample:           {np.var(Y):.4f}")
print(f"Sum check:               {np.mean(Var_Y_given_X) + np.var(E_Y_given_X):.4f}")

# Fraction of variance explained (R-squared analog)
R2 = np.var(E_Y_given_X) / np.var(Y)
print(f"\nFraction of Var(Y) explained by X: {R2:.4f}")
print(f"(= Var(E[Y|X]) / Var(Y) = 4/6 = {4/6:.4f})")
```

## ML and AI Connections

Second-order statistics pervade ML theory and practice:

- **Weight initialisation**: He initialisation for ReLU sets Var(W) = 2/fan_in to preserve variance across layers. Xavier/Glorot targets Var(W) = 2/(fan_in + fan_out). Both derive from the requirement Var(output) = Var(input).

- **Batch normalisation**: explicitly sets E[activations] = 0 and Var(activations) = 1 at each layer (then rescales with learnable γ, β). This whitens activations, reducing covariate shift.

- **PCA**: extracts eigenvectors of the sample covariance matrix, ranked by eigenvalue (variance). The top-k eigenvectors capture the k dimensions of maximum variance.

- **Kalman filter**: maintains a Gaussian posterior with mean (conditional expectation) and covariance (conditional variance) that are updated with each new observation.

- **Gaussian process regression**: posterior mean is the MMSE estimate E[f(x*)|data]; posterior variance quantifies uncertainty.

## Pitfalls

Common mistakes with second-order statistics:

1. **Using n instead of n−1 for sample variance**: the MLE estimate (n denominator) underestimates the true variance, especially for small n. Use ddof=1 in numpy.

2. **Computing variance as E[X²] − E[X]² for large means**: catastrophic cancellation when both terms are large and nearly equal. Use Welford's algorithm or centre the data first.

3. **Treating zero correlation as independence**: zero covariance ≠ independence except for jointly Gaussian variables. Example: Y = X², where X ~ N(0,1): Cov(X, Y) = E[X³] = 0 but X and Y are highly dependent.

4. **Assuming covariance matrix is invertible**: singular covariance (rank deficient) occurs when features are perfectly correlated or n < d. Use pseudoinverse or add regularisation λI.

> **TIP: PSD and the Cholesky Decomposition**
>
> Any valid covariance matrix Σ is positive semi-definite (PSD). The Cholesky decomposition Σ = L L^T (where L is lower triangular) exists iff Σ is PSD. It is the efficient way to: (1) sample from N(μ,Σ) as μ + L z where z ~ N(0,I); (2) solve Σ x = b as two triangular solves; (3) compute log det(Σ) = 2 Σ log(Lᵢᵢ) in O(d²) instead of O(d³). Always use Cholesky over direct matrix inverse for covariance operations.

| Quantity | Definition | Key Property | ML Application |
| --- | --- | --- | --- |
| E[X] | Σ x p(x) or ∫ x f(x) dx | Linearity; E[aX+bY]=aE[X]+bE[Y] | Loss is expected cost |
| Var(X) | E[(X−μ)²] | Var(aX)=a²Var(X) | Weight init, batch norm |
| Cov(X,Y) | E[(X−μₓ)(Y−μᵧ)] | 0 for independent; Σᵢᵢ=Var(Xᵢ) | Feature correlation |
| Corr(X,Y) | Cov(X,Y)/(σₓσᵧ) | ∈ [−1,1]; scale-invariant | Feature selection |
| Covariance matrix Σ | Σᵢⱼ=Cov(Xᵢ,Xⱼ) | Always PSD, symmetric | PCA, GPs, Kalman |
| E[Y|X] | Best MSE predictor of Y given X | Tower property: E[E[Y|X]]=E[Y] | Regression target |
| Var(Y) | E[Var(Y|X)]+Var(E[Y|X]) | Total=within+between | Bias-variance tradeoff |

---

## Key Takeaways

- E[X] is the probability-weighted average; linearity E[aX+bY]=aE[X]+bE[Y] holds regardless of dependence between X and Y.
- LOTUS: E[g(X)] = ∫ g(x) f(x) dx — no need to find the distribution of g(X) to compute its expectation.
- Var(X) = E[X²] − E[X]²; sample variance uses ddof=1 (Bessel's correction) for unbiasedness.
- Cov(X,Y) = E[XY] − E[X]E[Y]; zero covariance does not imply independence except for jointly Gaussian variables.
- Any covariance matrix Σ is symmetric and positive semi-definite (PSD) — all eigenvalues ≥ 0; use Cholesky for efficient sampling and log-determinant computation.
- The conditional expectation E[Y|X] is the best MSE predictor of Y given X; the tower property E[E[Y|X]]=E[Y] is the foundation of Monte Carlo unbiasedness.
- Law of total variance: Var(Y)=E[Var(Y|X)]+Var(E[Y|X]) — total variance = within-group + between-group; R² = Var(E[Y|X])/Var(Y) is the fraction explained.
