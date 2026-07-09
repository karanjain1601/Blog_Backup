---
title: "Maximum Likelihood Estimation (MLE)"
slug: "maximum-likelihood-estimation"
description: "Likelihood and log-likelihood, MLE for Gaussian and Bernoulli, logistic regression via MLE, asymptotic properties (consistency, normality, efficiency), Fisher information, and the Cramér-Rao bound."
tags: ["probability", "statistics", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTWF4aW11bSBsaWtlbGlob29kIGVzdGltYXRpb24gaXMgdGhlIHdvcmtob3JzZSBvZiBzdGF0aXN0aWNhbCBpbmZlcmVuY2UgYW5kIHRoZSBkZWZhdWx0IGZyYW1ld29yayBmb3IgdHJhaW5pbmcgTUwgbW9kZWxzLiBUcmFpbmluZyBhIG5ldXJhbCBuZXR3b3JrIHdpdGggY3Jvc3MtZW50cm9weSBsb3NzIGlzIGV4YWN0bHkgTUxFIGZvciBhIGNhdGVnb3JpY2FsIG1vZGVsLiBGaXR0aW5nIGEgR2F1c3NpYW4gdG8gZGF0YSBpcyBNTEUuIExpbmVhciByZWdyZXNzaW9uIHdpdGggTVNFIGxvc3MgaXMgTUxFIHVuZGVyIGEgR2F1c3NpYW4gbm9pc2UgbW9kZWwuIFVuZGVyc3RhbmRpbmcgTUxFIHJpZ29yb3VzbHkg4oCUIHRoZSBsaWtlbGlob29kIGZ1bmN0aW9uLCB3aHkgd2Ugd29yayBpbiBsb2ctc3BhY2UsIGNsb3NlZC1mb3JtIHZzIGdyYWRpZW50LWJhc2VkIHNvbHV0aW9ucywgYW5kIHRoZSBhc3ltcHRvdGljIHByb3BlcnRpZXMgdGhhdCBqdXN0aWZ5IHdoeSBNTEUgd29ya3Mg4oCUIGdpdmVzIGEgdW5pZmllZCB0aGVvcmV0aWNhbCBmb3VuZGF0aW9uIGZvciBhbGwgdGhlc2UgbWV0aG9kcy4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJDb3JlIERlZmluaXRpb24g4oCUIExpa2VsaWhvb2QgYW5kIExvZy1MaWtlbGlob29kIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiR2l2ZW4gYSBwYXJhbWV0cmljIG1vZGVsIHAoeHzOuCkgYW5kIG9ic2VydmVkIGRhdGEgeOKCgSwg4oCmLCB44oKZIChpaWQpLCB0aGUgbGlrZWxpaG9vZCBpczpcblxuTCjOuDsgeOKCgSzigKYseOKCmSkgPSDOoOG1oiBwKHjhtaJ8zrgpXG5cblRoZSBNTEUgaXMgzrjMgiA9IGFyZ21heF/OuCBMKM64OyB4KS4gVGFraW5nIGxvZ3MgKG1vbm90b25lIHRyYW5zZm9ybWF0aW9uLCBwcmVzZXJ2ZXMgYXJnbWF4KTpcblxu4oSTKM64KSA9IGxvZyBMKM64KSA9IM6j4bWiIGxvZyBwKHjhtaJ8zrgpXG5cbldvcmtpbmcgd2l0aCBsb2ctbGlrZWxpaG9vZCBpcyBwcmVmZXJyZWQgZm9yIHR3byByZWFzb25zOlxuMS4gKipOdW1lcmljYWwgc3RhYmlsaXR5Kio6IHByb2R1Y3RzIG9mIG1hbnkgcHJvYmFiaWxpdGllcyB1bmRlcmZsb3cgdG8gMCBmb3IgbGFyZ2Ugbjsgc3VtcyBvZiBsb2ctcHJvYmFiaWxpdGllcyByZW1haW4gcmVwcmVzZW50YWJsZS5cbjIuICoqRGVjb21wb3NhYmlsaXR5Kio6IHRoZSBsb2ctbGlrZWxpaG9vZCBkZWNvbXBvc2VzIGFkZGl0aXZlbHkgb3ZlciBkYXRhIHBvaW50cywgbWFraW5nIG9wdGltaXNhdGlvbiwgU0dELCBhbmQgbWluaS1iYXRjaGluZyBuYXR1cmFsLlxuXG5Gb3IgcmVndWxhciBtb2RlbHMgKHNtb290aGx5IHBhcmFtZXRyaXNlZCwgaWRlbnRpZmlhYmxlKSwgdGhlIE1MRSBpcyBmb3VuZCBieSBzb2x2aW5nIHRoZSBzY29yZSBlcXVhdGlvbnM6IOKIh1/OuCDihJMozrgpID0gMC4gU29tZXRpbWVzIGNsb3NlZC1mb3JtIHNvbHV0aW9ucyBleGlzdCAoR2F1c3NpYW4sIGV4cG9uZW50aWFsIGZhbWlseSk7IG1vcmUgb2Z0ZW4gd2UgdXNlIGdyYWRpZW50LWJhc2VkIG9wdGltaXNhdGlvbi4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5Lm9wdGltaXplIGltcG9ydCBtaW5pbWl6ZVxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybVxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgTUxFIGZvciBHYXVzc2lhbjogY2xvc2VkLWZvcm0gdnMgZ3JhZGllbnQgYXNjZW50XG5uID0gMTAwMFxubXVfdHJ1ZSwgc2lnbWFfdHJ1ZSA9IDMuNSwgMS4yXG5YID0gcm5nLm5vcm1hbChtdV90cnVlLCBzaWdtYV90cnVlLCBuKVxuXG4jIENsb3NlZC1mb3JtIE1MRVxubXVfaGF0ICAgICA9IG5wLm1lYW4oWClcbnNpZ21hX2hhdCAgPSBucC5zdGQoWCwgZGRvZj0wKSAgICMgTUxFIHVzZXMgbiAoYmlhc2VkKVxuc2lnbWFfdW5iICA9IG5wLnN0ZChYLCBkZG9mPTEpICAgIyB1bmJpYXNlZCB1c2VzIG4tMVxuXG5wcmludChcIj09PSBHYXVzc2lhbiBNTEUgKG49MTAwMCkgPT09XCIpXG5wcmludChmXCJUcnVlOiAgbXU9e211X3RydWV9LCBzaWdtYT17c2lnbWFfdHJ1ZX1cIilcbnByaW50KGZcIk1MRTogICBtdT17bXVfaGF0Oi40Zn0sIHNpZ21hPXtzaWdtYV9oYXQ6LjRmfSAgKGJpYXNlZClcIilcbnByaW50KGZcIlVuYmlhc2VkOiBzaWdtYT17c2lnbWFfdW5iOi40Zn0gIChCZXNzZWwncyBjb3JyZWN0aW9uKVwiKVxuXG4jIExvZy1saWtlbGlob29kIGZ1bmN0aW9uXG5kZWYgbmVnX2xvZ19saWtlbGlob29kKHBhcmFtcywgWCk6XG4gICAgbXUsIGxvZ19zaWdtYSA9IHBhcmFtc1xuICAgIHNpZ21hID0gbnAuZXhwKGxvZ19zaWdtYSkgICAjIHJlcGFyYW1ldGVyaXNlIHRvIGVuc3VyZSBzaWdtYSA+IDBcbiAgICByZXR1cm4gLW5wLnN1bShub3JtLmxvZ3BkZihYLCBtdSwgc2lnbWEpKVxuXG4jIEdyYWRpZW50LWJhc2VkIE1MRSAoc2hvdWxkIG1hdGNoIGNsb3NlZC1mb3JtKVxucmVzdWx0ID0gbWluaW1pemUobmVnX2xvZ19saWtlbGlob29kLCB4MD1bMC4wLCAwLjBdLCBhcmdzPShYLCksIG1ldGhvZD0nTC1CRkdTLUInKVxubXVfb3B0LCBzaWdtYV9vcHQgPSByZXN1bHQueFswXSwgbnAuZXhwKHJlc3VsdC54WzFdKVxucHJpbnQoZlwiR3JhZGllbnQgYXNjZW50OiBtdT17bXVfb3B0Oi40Zn0sIHNpZ21hPXtzaWdtYV9vcHQ6LjRmfVwiKVxuXG4jIExvZy1saWtlbGlob29kIGF0IE1MRSB2cyBvdGhlciB2YWx1ZXNcbmVsbF9tbGUgICA9IC1uZWdfbG9nX2xpa2VsaWhvb2QoW211X2hhdCwgbnAubG9nKHNpZ21hX2hhdCldLCBYKVxuZWxsX3dyb25nID0gLW5lZ19sb2dfbGlrZWxpaG9vZChbbXVfaGF0ICsgMC41LCBucC5sb2coc2lnbWFfaGF0KV0sIFgpXG5wcmludChmXCJcXG5Mb2ctbGlrZWxpaG9vZCBhdCBNTEU6ICAgICAgIHtlbGxfbWxlOi4yZn1cIilcbnByaW50KGZcIkxvZy1saWtlbGlob29kIGF0IG11KzAuNTogICAge2VsbF93cm9uZzouMmZ9ICAobG93ZXIsIGFzIGV4cGVjdGVkKVwiKVxuXG4jIE1MRSBmb3IgQmVybm91bGxpOiBwX2hhdCA9IGsvbiAocHJvcG9ydGlvbiBvZiBzdWNjZXNzZXMpXG5rLCBuX2Jlcm4gPSAzNywgMTAwXG5wX2hhdCA9IGsgLyBuX2Jlcm5cbnByaW50KGZcIlxcbj09PSBCZXJub3VsbGkgTUxFID09PVwiKVxucHJpbnQoZlwiT2JzZXJ2ZWQ6IHtrfS97bl9iZXJufSBzdWNjZXNzZXMgPT4gcF9oYXQgPSB7cF9oYXQ6LjRmfVwiKVxuIyBMb2ctbGlrZWxpaG9vZDogaypsb2cocCkgKyAobi1rKSpsb2coMS1wKVxucF9ncmlkID0gbnAubGluc3BhY2UoMC4wMSwgMC45OSwgMTAwMClcbmxsID0gayAqIG5wLmxvZyhwX2dyaWQpICsgKG5fYmVybiAtIGspICogbnAubG9nKDEgLSBwX2dyaWQpXG5wcmludChmXCJNYXggTEwgYXQgcD17cF9ncmlkW25wLmFyZ21heChsbCldOi40Zn1cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNTEUgZm9yIExvZ2lzdGljIFJlZ3Jlc3Npb24ifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJGb3IgYmluYXJ5IGNsYXNzaWZpY2F0aW9uIHdpdGggbGFiZWwgeSDiiIggezAsMX0gYW5kIGZlYXR1cmVzIHgsIGxvZ2lzdGljIHJlZ3Jlc3Npb24gYXNzdW1lczpcblxucCh5PTF8eCwgdykgPSDPgyh34bWAeCkgPSAxLygxICsgZXhwKOKIknfhtYB4KSlcblxuVGhlIGxvZy1saWtlbGlob29kIGZvciBuIGlpZCBvYnNlcnZhdGlvbnMgaXM6XG5cbuKEkyh3KSA9IM6j4bWiIFt54bWiIGxvZyDPgyh34bWAeOG1oikgKyAoMeKIknnhtaIpIGxvZygx4oiSz4Mod+G1gHjhtaIpKV1cbiAgICAgPSDOo+G1oiBbeeG1oiB34bWAeOG1oiDiiJIgbG9nKDEgKyBleHAod+G1gHjhtaIpKV1cblxuVGhpcyBpcyBjb25jYXZlIGluIHcgKHRoZSBIZXNzaWFuIGlzIOKIklheVCBEIFggd2hlcmUgRCBpcyBkaWFnb25hbCB3aXRoIHBvc2l0aXZlIGVudHJpZXMpLCBzbyBncmFkaWVudCBhc2NlbnQgb3IgTmV3dG9uLVJhcGhzb24gY29udmVyZ2VzIHRvIHRoZSBnbG9iYWwgbWF4aW11bS4gVGhlIGdyYWRpZW50IGlzOlxuXG7iiIdfdyDihJModykgPSDOo+G1oiAoeeG1oiDiiJIgz4Mod+G1gHjhtaIpKSB44bWiID0gWF5UICh5IOKIkiDFtylcblxuTmV3dG9uLVJhcGhzb24gdXBkYXRlOiB3X3t0KzF9ID0gd190IOKIkiBI4oG7wrkg4oiH4oSTIHdoZXJlIEggPSDiiJJYXlQgRCBYIChJUkxTOiBpdGVyYXRpdmVseSByZXdlaWdodGVkIGxlYXN0IHNxdWFyZXMpLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3BlY2lhbCBpbXBvcnQgZXhwaXQgICMgbnVtZXJpY2FsbHkgc3RhYmxlIHNpZ21vaWRcblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxuXG4jIEdlbmVyYXRlIGJpbmFyeSBjbGFzc2lmaWNhdGlvbiBkYXRhXG5uLCBkID0gNTAwLCAzXG5YID0gcm5nLnN0YW5kYXJkX25vcm1hbCgobiwgZCkpXG5YID0gbnAuaHN0YWNrKFtucC5vbmVzKChuLDEpKSwgWF0pICAgIyBhZGQgaW50ZXJjZXB0XG53X3RydWUgPSBucC5hcnJheShbMC41LCAxLjIsIC0wLjgsIDAuM10pXG55ID0gKHJuZy51bmlmb3JtKHNpemU9bikgPCBleHBpdChYIEAgd190cnVlKSkuYXN0eXBlKGZsb2F0KVxuXG5kZWYgbG9nX2xpa2VsaWhvb2QodywgWCwgeSk6XG4gICAgcCA9IGV4cGl0KFggQCB3KVxuICAgIHJldHVybiBucC5zdW0oeSAqIG5wLmxvZyhwICsgMWUtMTUpICsgKDEteSkgKiBucC5sb2coMS1wICsgMWUtMTUpKVxuXG5kZWYgZ3JhZGllbnQodywgWCwgeSk6XG4gICAgcmV0dXJuIFguVCBAICh5IC0gZXhwaXQoWCBAIHcpKVxuXG5kZWYgaGVzc2lhbih3LCBYKTpcbiAgICBwID0gZXhwaXQoWCBAIHcpXG4gICAgRCA9IG5wLmRpYWcocCAqICgxIC0gcCkpICAgIyB3ZWlnaHRzXG4gICAgcmV0dXJuIC1YLlQgQCBEIEAgWFxuXG4jIE5ld3Rvbi1SYXBoc29uIChJUkxTKVxucHJpbnQoXCI9PT0gTG9naXN0aWMgUmVncmVzc2lvbjogTmV3dG9uLVJhcGhzb24gPT09XCIpXG53ID0gbnAuemVyb3MoZCArIDEpXG5mb3IgaXQgaW4gcmFuZ2UoMTApOlxuICAgIGcgPSBncmFkaWVudCh3LCBYLCB5KVxuICAgIEggPSBoZXNzaWFuKHcsIFgpXG4gICAgdyA9IHcgLSBucC5saW5hbGcuc29sdmUoSCwgZykgICAjIHcgPSB3IC0gSF57LTF9IGdcbiAgICBsbCA9IGxvZ19saWtlbGlob29kKHcsIFgsIHkpXG4gICAgZ3JhZF9ub3JtID0gbnAubGluYWxnLm5vcm0oZylcbiAgICBwcmludChmXCIgIGl0ZXIge2l0KzE6MmR9OiBsbD17bGw6LjRmfSAgfHxncmFkfHw9e2dyYWRfbm9ybTouNGV9XCIpXG5cbnByaW50KGZcIlxcblRydWUgdzoge3dfdHJ1ZX1cIilcbnByaW50KGZcIk1MRSAgdzoge25wLnJvdW5kKHcsIDQpfVwiKVxuXG4jIEdyYWRpZW50IGFzY2VudCBjb21wYXJpc29uXG5wcmludChcIlxcbj09PSBHcmFkaWVudCBBc2NlbnQgKGxyPTAuMSkgPT09XCIpXG53X2dkID0gbnAuemVyb3MoZCArIDEpXG5mb3IgaXQgaW4gcmFuZ2UoMTAwKTpcbiAgICB3X2dkICs9IDAuMSAqIGdyYWRpZW50KHdfZ2QsIFgsIHkpXG5wcmludChmXCJHRCB3ICgxMDAgc3RlcHMpOiB7bnAucm91bmQod19nZCwgNCl9XCIpXG5wcmludChmXCJOZXd0b24gY29udmVyZ2VzIGluIH41IHN0ZXBzOyBHRCBuZWVkcyBtYW55IG1vcmUuXCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiRmlzaGVyIEluZm9ybWF0aW9uIGFuZCBDcmFtw6lyLVJhbyBCb3VuZCJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBGaXNoZXIgaW5mb3JtYXRpb24gbWF0cml4IG1lYXN1cmVzIGhvdyBtdWNoIGluZm9ybWF0aW9uIHRoZSBkYXRhIGNhcnJpZXMgYWJvdXQgzrg6XG5cbkkozrgpID0gRV/OuFso4oiHX864IGxvZyBwKFh8zrgpKSjiiIdfzrggbG9nIHAoWHzOuCkpXlRdID0g4oiSRV/OuFviiIfCsl/OuCBsb2cgcChYfM64KV1cblxuRm9yIG4gaWlkIG9ic2VydmF0aW9uczogSeKCmSjOuCkgPSBuIEnigoEozrgpLlxuXG5UaGUgQ3JhbcOpci1SYW8gbG93ZXIgYm91bmQgKENSTEIpIHN0YXRlcyB0aGF0IGZvciBhbnkgdW5iaWFzZWQgZXN0aW1hdG9yIM64zIIgb2Ygzrg6XG5cblZhcijOuMyCKSDiiaUgSSjOuCnigbvCuVxuXG5UaGUgTUxFIGFjaGlldmVzIHRoaXMgYm91bmQgYXN5bXB0b3RpY2FsbHkgKGl0IGlzIGFzeW1wdG90aWNhbGx5IGVmZmljaWVudCkuIEZpc2hlciBpbmZvcm1hdGlvbiBhbHNvIGRldGVybWluZXMgdGhlIGdlb21ldHJ5IHVzZWQgYnkgbmF0dXJhbCBncmFkaWVudCBkZXNjZW50OiB0aGUgbmF0dXJhbCBncmFkaWVudCDiiIfMg+KEkyA9IEkozrgp4oG7wrkg4oiH4oSTIGZvbGxvd3MgdGhlIHN0ZWVwZXN0IGFzY2VudCBpbiB0aGUgc3BhY2Ugb2YgcHJvYmFiaWxpdHkgZGlzdHJpYnV0aW9ucyAoRmlzaGVyLVJhbyBtZXRyaWMpLCBub3QgRXVjbGlkZWFuIHBhcmFtZXRlciBzcGFjZS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJBc3ltcHRvdGljIFByb3BlcnRpZXMgb2YgTUxFIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVW5kZXIgcmVndWxhcml0eSBjb25kaXRpb25zLCB0aGUgTUxFIGhhcyB0aHJlZSBrZXkgYXN5bXB0b3RpYyBwcm9wZXJ0aWVzOlxuXG4xLiAqKkNvbnNpc3RlbmN5Kio6IM64zIJfbiDihpIgzrgqIGFzIG4g4oaSIOKIniAoaW4gcHJvYmFiaWxpdHkpLiBUaGUgTUxFIGNvbnZlcmdlcyB0byB0aGUgdHJ1ZSBwYXJhbWV0ZXIuXG5cbjIuICoqQXN5bXB0b3RpYyBub3JtYWxpdHkqKjog4oiabiAozrjMgl9uIOKIkiDOuCopIOKGkiBOKDAsIEkozrgqKeKBu8K5KS4gVGhlIE1MRSBpcyBhcHByb3hpbWF0ZWx5IEdhdXNzaWFuIGFyb3VuZCB0aGUgdHJ1ZSBwYXJhbWV0ZXIsIHdpdGggdmFyaWFuY2Ugc2hyaW5raW5nIGFzIDEvbi5cblxuMy4gKipBc3ltcHRvdGljIGVmZmljaWVuY3kqKjogdGhlIE1MRSBhY2hpZXZlcyB0aGUgQ3JhbcOpci1SYW8gbG93ZXIgYm91bmQg4oCUIG5vIG90aGVyIGNvbnNpc3RlbnQgZXN0aW1hdG9yIGhhcyBzbWFsbGVyIGFzeW1wdG90aWMgdmFyaWFuY2UuXG5cbjQuICoqSW52YXJpYW5jZSoqOiBpZiDOuMyCIGlzIHRoZSBNTEUgb2YgzrgsIHRoZW4gZyjOuMyCKSBpcyB0aGUgTUxFIG9mIGcozrgpIGZvciBhbnkgZnVuY3Rpb24gZy4gVGhpcyBtZWFucyBNTEUgb2Ygz4PCsiBpcyAoz4PMginCsiwgYW5kIE1MRSBvZiBsb2cgz4MgaXMgbG9nIM+DzIIuXG5cblRoZXNlIHByb3BlcnRpZXMganVzdGlmeSB1c2luZyBNTEUgYXMgdGhlIGRlZmF1bHQgZXN0aW1hdG9yOiBpdCBpcyBjb25zaXN0ZW50LCBhcyBlZmZpY2llbnQgYXMgcG9zc2libGUsIGFuZCBpdHMgdW5jZXJ0YWludHkgY2FuIGJlIHF1YW50aWZpZWQgdmlhIHRoZSBGaXNoZXIgaW5mb3JtYXRpb24uIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybVxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgRGVtb25zdHJhdGUgY29uc2lzdGVuY3k6IE1MRSBjb252ZXJnZXMgdG8gdHJ1ZSB0aGV0YSBhcyBuIGdyb3dzXG5tdV90cnVlLCBzaWdtYV90cnVlID0gMi4wLCAxLjVcbnByaW50KFwiPT09IE1MRSBDb25zaXN0ZW5jeSBmb3IgR2F1c3NpYW4gbXUgPT09XCIpXG5wcmludChmXCJUcnVlIG11ID0ge211X3RydWV9XCIpXG5mb3IgbiBpbiBbMTAsIDEwMCwgMTAwMCwgMTAwMDAsIDEwMDAwMF06XG4gICAgWCA9IHJuZy5ub3JtYWwobXVfdHJ1ZSwgc2lnbWFfdHJ1ZSwgbilcbiAgICBtdV9oYXQgPSBucC5tZWFuKFgpXG4gICAgc2UgPSBzaWdtYV90cnVlIC8gbnAuc3FydChuKVxuICAgIHByaW50KGZcIiAgbj17bjo+Nyx9OiBtdV9oYXQ9e211X2hhdDouNGZ9ICBTRT17c2U6LjRmfSAgZXJyb3I9e2FicyhtdV9oYXQtbXVfdHJ1ZSk6LjRmfVwiKVxuXG4jIEZpc2hlciBpbmZvcm1hdGlvbiBmb3IgR2F1c3NpYW46IEkobXUpID0gMS9zaWdtYV4yXG5JX211ID0gMSAvIHNpZ21hX3RydWUqKjJcbnByaW50KGZcIlxcbkZpc2hlciBpbmZvcm1hdGlvbiBJKG11KSA9IDEvc2lnbWFeMiA9IHtJX211Oi40Zn1cIilcbnByaW50KGZcIkNyYW1lci1SYW8gYm91bmQgb24gVmFyKG11X2hhdCk6ID49IDEvKG4qSSkgPSBzaWdtYV4yL25cIilcbnByaW50KGZcIk1MRSBhY2hpZXZlczogVmFyKHNhbXBsZSBtZWFuKSA9IHNpZ21hXjIvbiA9IHtzaWdtYV90cnVlKioyLzEwMDA6LjZmfSAobj0xMDAwKVwiKVxuXG4jIEFzeW1wdG90aWMgbm9ybWFsaXR5OiBzcXJ0KG4pKG11X2hhdCAtIG11X3RydWUpIC0+IE4oMCwgMS9JKVxucHJpbnQoXCJcXG49PT0gQXN5bXB0b3RpYyBOb3JtYWxpdHkgQ2hlY2sgKG49MTAwLCA1MDAwIHJlcHMpID09PVwiKVxubiA9IDEwMDsgbl9yZXBzID0gNTAwMFxubXVfaGF0cyA9IFtucC5tZWFuKHJuZy5ub3JtYWwobXVfdHJ1ZSwgc2lnbWFfdHJ1ZSwgbikpIGZvciBfIGluIHJhbmdlKG5fcmVwcyldXG5zY2FsZWQgPSBucC5zcXJ0KG4pICogKG5wLmFycmF5KG11X2hhdHMpIC0gbXVfdHJ1ZSkgICAjIHNob3VsZCBiZSB+IE4oMCwgc2lnbWFeMilcbnByaW50KGZcIkVtcGlyaWNhbCBzdGQgb2Ygc3FydChuKSoobXVfaGF0IC0gbXUpOiB7bnAuc3RkKHNjYWxlZCk6LjRmfVwiKVxucHJpbnQoZlwiVGhlb3JldGljYWwgKHNpZ21hKTogICAgICAgICAgICAgICAgICAgIHtzaWdtYV90cnVlOi40Zn1cIilcblxuIyBNTEUgaW52YXJpYW5jZTogTUxFIG9mIHNpZ21hXjIgaXMgKHNpZ21hX2hhdCleMlxuWF9zYW1wbGUgPSBybmcubm9ybWFsKG11X3RydWUsIHNpZ21hX3RydWUsIDEwMDApXG5zaWdtYV9oYXQgPSBucC5zdGQoWF9zYW1wbGUsIGRkb2Y9MClcbnByaW50KGZcIlxcbk1MRSBpbnZhcmlhbmNlOiBNTEUgb2Ygc2lnbWFeMiA9IChzaWdtYV9oYXQpXjIgPSB7c2lnbWFfaGF0KioyOi40Zn1cIilcbnByaW50KGZcIkRpcmVjdCBNTEUgb2Ygc2lnbWFeMiA9IHtucC52YXIoWF9zYW1wbGUsIGRkb2Y9MCk6LjRmfSAgKHNhbWUpXCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTUwgYW5kIEFJIENvbm5lY3Rpb25zIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTUxFIHVuaWZpZXMgdGhlIHRyYWluaW5nIG9iamVjdGl2ZXMgb2YgbmVhcmx5IGFsbCBkaXNjcmltaW5hdGl2ZSBtb2RlbHMgaW4gTUw6XG5cbi0gKipDcm9zcy1lbnRyb3B5IGxvc3MqKiA9IG5lZ2F0aXZlIGxvZy1saWtlbGlob29kIG9mIGEgY2F0ZWdvcmljYWwgbW9kZWw6IG1pbmltaXNlIOKIks6j4bWiIGxvZyBwKHnhtaJ8eOG1oiwgzrgpXG4tICoqTVNFIGxvc3MqKiA9IG5lZ2F0aXZlIGxvZy1saWtlbGlob29kIHVuZGVyIGEgR2F1c3NpYW4gbm9pc2UgbW9kZWw6IHAoeXx4LM64KSA9IE4oeTsgZih4LM64KSwgz4PCsilcbi0gKipCaW5hcnkgY3Jvc3MtZW50cm9weSoqID0gbmVnYXRpdmUgbG9nLWxpa2VsaWhvb2Qgb2YgYSBCZXJub3VsbGkgbW9kZWw6IHAoeXx4LM64KSA9IM+DKGYoeCzOuCkpXnkgKDHiiJLPgyhmKHgszrgpKSleezEteX1cbi0gKipDb250cmFzdGl2ZSBsb3NzIC8gSW5mb05DRSoqID0gTUxFIGZvciBub2lzZS1jb250cmFzdGl2ZSBlc3RpbWF0aW9uLCBsZWFybmluZyByZXByZXNlbnRhdGlvbnMgYnkgY2xhc3NpZnlpbmcgcmVhbCBmcm9tIG5vaXNlIHNhbXBsZXNcblxuRmlzaGVyIGluZm9ybWF0aW9uIGFsc28gZHJpdmVzIG5hdHVyYWwgZ3JhZGllbnQgbWV0aG9kcyAoTkdELCBLRkFDLCBTaGFtcG9vKSB3aGljaCByZXNjYWxlIGdyYWRpZW50cyBieSB0aGUgaW52ZXJzZSBGaXNoZXIgbWF0cml4LCB0YWtpbmcgc3RlcHMgdGhhdCBhcmUgZXF1aWRpc3RhbnQgaW4gcHJvYmFiaWxpdHkgc3BhY2UgcmF0aGVyIHRoYW4gcGFyYW1ldGVyIHNwYWNlIOKAlCBwb3RlbnRpYWxseSBtdWNoIGZhc3RlciBjb252ZXJnZW5jZSBmb3IgaWxsLWNvbmRpdGlvbmVkIHByb2JsZW1zLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQ29tbW9uIE1MRSBwaXRmYWxsczpcblxuMS4gKipPdmVyZml0dGluZyBmb3Igc21hbGwgbioqOiBNTEUgaXMgYXN5bXB0b3RpY2FsbHkgZWZmaWNpZW50IGJ1dCBjYW4gc2V2ZXJlbHkgb3ZlcmZpdCBmb3Igc21hbGwgbi4gQSBCZXJub3VsbGkgbW9kZWwgdHJhaW5lZCBvbiAzIGhlYWRzIG91dCBvZiAzIGZsaXBzIGdpdmVzIHDMgiA9IDEuMCDigJQgcHJlZGljdGluZyBoZWFkcyB3aXRoIGNlcnRhaW50eS4gVGhpcyBpcyB3aHkgTUFQIGVzdGltYXRpb24gKGFkZGluZyBhIHByaW9yKSBpcyBwcmVmZXJyZWQgZm9yIHNtYWxsIGRhdGFzZXRzLlxuXG4yLiAqKk5vbi1pZGVudGlmaWFiaWxpdHkqKjogaWYgbXVsdGlwbGUgzrggdmFsdWVzIGdpdmUgdGhlIHNhbWUgbGlrZWxpaG9vZCwgdGhlIE1MRSBpcyBub3QgdW5pcXVlLiBFeGFtcGxlOiBtaXh0dXJlIG1vZGVscyB3aXRoIHBlcm11dGFibGUgY29tcG9uZW50IGxhYmVscy4gUmVndWxhcmlzYXRpb24gb3IgY29uc3RyYWludHMgYnJlYWsgdGhlIHN5bW1ldHJ5LlxuXG4zLiAqKk51bWVyaWNhbCBvdmVyZmxvdyBpbiBsaWtlbGlob29kKio6IGFsd2F5cyB3b3JrIHdpdGggbG9nLWxpa2VsaWhvb2RzLCBuZXZlciByYXcgbGlrZWxpaG9vZHMuIM6g4bWiIHAoeOG1onzOuCkgdW5kZXJmbG93cyB0byAwIGZvciBuIGFzIHNtYWxsIGFzIDEwMCBmb3IgdHlwaWNhbCBNTCBtb2RlbHMuXG5cbjQuICoqQ29uZnVzaW5nIE1MRSB3aXRoIE1NU0UqKjogTUxFIG1heGltaXNlcyBwKER8zrgpIG5vdCBFW864fERdLiBGb3IgYXN5bW1ldHJpYyBwb3N0ZXJpb3JzIG9yIHNtYWxsIG4sIHRoZSBNTEUgY2FuIGJlIGZhciBmcm9tIHRoZSBwb3N0ZXJpb3IgbWVhbi4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidmFyaWFudCI6ICJ3YXJuaW5nIiwgInRpdGxlIjogIk1MRSBSZXF1aXJlcyBpLmkuZC4gRGF0YSIsICJjb250ZW50IjogIlN0YW5kYXJkIE1MRSB0aGVvcnkgYXNzdW1lcyBkYXRhIHBvaW50cyBhcmUgaW5kZXBlbmRlbnQgYW5kIGlkZW50aWNhbGx5IGRpc3RyaWJ1dGVkLiBJbiBwcmFjdGljZSwgZGF0YSBvZnRlbiB2aW9sYXRlcyB0aGlzOiB0aW1lIHNlcmllcyBoYXZlIHRlbXBvcmFsIGNvcnJlbGF0aW9uLCBoaWVyYXJjaGljYWwgZGF0YSBoYXMgY2x1c3RlciBzdHJ1Y3R1cmUsIGFuZCBmaW5lLXR1bmluZyBkYXRhIG1heSBoYXZlIGRvbWFpbiBzaGlmdC4gSWdub3JpbmcgZGVwZW5kZW5jZSBnaXZlcyBhc3ltcHRvdGljYWxseSB3cm9uZyBzdGFuZGFyZCBlcnJvcnMgYW5kIG1heSBiaWFzIHRoZSBNTEUgaXRzZWxmLiBVc2Ugcm9idXN0IHN0YW5kYXJkIGVycm9ycywgbWl4ZWQtZWZmZWN0cyBtb2RlbHMsIG9yIHNlcGFyYXRlIGxpa2VsaWhvb2RzIGZvciBjb3JyZWxhdGVkIGRhdGEuIn0sIHsidHlwZSI6ICJ0YWJsZSIsICJoZWFkZXJzIjogWyJNb2RlbCIsICJMb3NzIEZ1bmN0aW9uIiwgIk1MRSBJbnRlcnByZXRhdGlvbiJdLCAicm93cyI6IFtbIkdhdXNzaWFuIHJlZ3Jlc3Npb24iLCAiTVNFID0gKHktxbcpwrIiLCAiTUxFIHVuZGVyIHAoeXx4KT1OKGYoeCzOuCksIM+DwrIpIl0sIFsiTG9naXN0aWMgcmVncmVzc2lvbiIsICJCaW5hcnkgY3Jvc3MtZW50cm9weSIsICJNTEUgdW5kZXIgcCh5fHgpPUJlcm5vdWxsaSjPgyh34bWAeCkpIl0sIFsiU29mdG1heCBjbGFzc2lmaWVyIiwgIkNyb3NzLWVudHJvcHkiLCAiTUxFIHVuZGVyIHAoeXx4KT1DYXRlZ29yaWNhbChzb2Z0bWF4KFd4KSkiXSwgWyJMYW5ndWFnZSBtb2RlbCIsICJDcm9zcy1lbnRyb3B5IHBlciB0b2tlbiIsICJNTEUgdW5kZXIgcCh44oKcfHhfezx0fSk9Q2F0ZWdvcmljYWwiXSwgWyJWQUUgZW5jb2RlciIsICJFTEJPIiwgIlZhcmlhdGlvbmFsIE1MRSBmb3IgbWFyZ2luYWwgbG9nIHAoeCkiXSwgWyJHQU4gZGlzY3JpbWluYXRvciIsICJCaW5hcnkgY3Jvc3MtZW50cm9weSIsICJOb2lzZS1jb250cmFzdGl2ZSBNTEUiXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAib3JkZXJlZCI6IGZhbHNlLCAiaXRlbXMiOiBbIk1MRSBmaW5kcyDOuMyCID0gYXJnbWF4X864IM6j4bWiIGxvZyBwKHjhtaJ8zrgpIOKAlCBhbHdheXMgd29yayB3aXRoIGxvZy1saWtlbGlob29kIGZvciBudW1lcmljYWwgc3RhYmlsaXR5IGFuZCBhZGRpdGl2ZSBkZWNvbXBvc2FiaWxpdHkuIiwgIkNsb3NlZC1mb3JtIE1MRSBleGlzdHMgZm9yIEdhdXNzaWFuIChzYW1wbGUgbWVhbiBhbmQgYmlhc2VkIHZhcmlhbmNlKSwgQmVybm91bGxpIChzYW1wbGUgcHJvcG9ydGlvbiksIGFuZCBleHBvbmVudGlhbCBmYW1pbHkgZGlzdHJpYnV0aW9ucyBnZW5lcmFsbHkuIiwgIkxvZ2lzdGljIHJlZ3Jlc3Npb24gTUxFIGlzIGNvbmNhdmUgKGdsb2JhbGx5IG9wdGltYWwpLCBmb3VuZCBlZmZpY2llbnRseSB2aWEgTmV3dG9uLVJhcGhzb24gKDUtMTAgaXRlcmF0aW9ucykgb3IgZ3JhZGllbnQgYXNjZW50LiIsICJGaXNoZXIgaW5mb3JtYXRpb24gSSjOuCkgPSBFWyjiiIcgbG9nIHApwrJdIG1lYXN1cmVzIGRhdGEgaW5mb3JtYXRpdmVuZXNzOyB0aGUgQ3JhbcOpci1SYW8gYm91bmQgVmFyKM64zIIpIOKJpSAxL0kozrgpIGxvd2VyLWJvdW5kcyBhbnkgdW5iaWFzZWQgZXN0aW1hdG9yJ3MgdmFyaWFuY2UuIiwgIk1MRSBpcyBhc3ltcHRvdGljYWxseSBjb25zaXN0ZW50LCBub3JtYWxseSBkaXN0cmlidXRlZCwgYW5kIGVmZmljaWVudCDigJQgYnV0IGNhbiBiYWRseSBvdmVyZml0IGZvciBzbWFsbCBuOyB1c2UgTUFQIGVzdGltYXRpb24gKHJlZ3VsYXJpc2F0aW9uKSBpbiB0aGF0IHJlZ2ltZS4iLCAiVHJhaW5pbmcgd2l0aCBjcm9zcy1lbnRyb3B5IGxvc3MsIE1TRSBsb3NzLCBvciBiaW5hcnkgY3Jvc3MtZW50cm9weSBpcyBleGFjdGx5IE1MRSB1bmRlciBDYXRlZ29yaWNhbCwgR2F1c3NpYW4sIGFuZCBCZXJub3VsbGkgbW9kZWxzIHJlc3BlY3RpdmVseS4iLCAiTmF0dXJhbCBncmFkaWVudCBkZXNjZW50IHVzZXMgdGhlIEZpc2hlciBpbmZvcm1hdGlvbiBtYXRyaXggdG8gcmVzY2FsZSBncmFkaWVudHMsIHN0ZXBwaW5nIGluIHByb2JhYmlsaXR5IHNwYWNlIHJhdGhlciB0aGFuIHBhcmFtZXRlciBzcGFjZSBmb3IgZmFzdGVyIGNvbnZlcmdlbmNlIG9uIGlsbC1jb25kaXRpb25lZCBwcm9ibGVtcy4iXX1d"
---
# Maximum Likelihood Estimation (MLE)

Maximum likelihood estimation is the workhorse of statistical inference and the default framework for training ML models. Training a neural network with cross-entropy loss is exactly MLE for a categorical model. Fitting a Gaussian to data is MLE. Linear regression with MSE loss is MLE under a Gaussian noise model. Understanding MLE rigorously — the likelihood function, why we work in log-space, closed-form vs gradient-based solutions, and the asymptotic properties that justify why MLE works — gives a unified theoretical foundation for all these methods.

## Core Definition — Likelihood and Log-Likelihood

Given a parametric model p(x|θ) and observed data x₁, …, xₙ (iid), the likelihood is:

L(θ; x₁,…,xₙ) = Πᵢ p(xᵢ|θ)

The MLE is θ̂ = argmax_θ L(θ; x). Taking logs (monotone transformation, preserves argmax):

ℓ(θ) = log L(θ) = Σᵢ log p(xᵢ|θ)

Working with log-likelihood is preferred for two reasons:
1. **Numerical stability**: products of many probabilities underflow to 0 for large n; sums of log-probabilities remain representable.
2. **Decomposability**: the log-likelihood decomposes additively over data points, making optimisation, SGD, and mini-batching natural.

For regular models (smoothly parametrised, identifiable), the MLE is found by solving the score equations: ∇_θ ℓ(θ) = 0. Sometimes closed-form solutions exist (Gaussian, exponential family); more often we use gradient-based optimisation.

```python
import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm

rng = np.random.default_rng(42)

# MLE for Gaussian: closed-form vs gradient ascent
n = 1000
mu_true, sigma_true = 3.5, 1.2
X = rng.normal(mu_true, sigma_true, n)

# Closed-form MLE
mu_hat     = np.mean(X)
sigma_hat  = np.std(X, ddof=0)   # MLE uses n (biased)
sigma_unb  = np.std(X, ddof=1)   # unbiased uses n-1

print("=== Gaussian MLE (n=1000) ===")
print(f"True:  mu={mu_true}, sigma={sigma_true}")
print(f"MLE:   mu={mu_hat:.4f}, sigma={sigma_hat:.4f}  (biased)")
print(f"Unbiased: sigma={sigma_unb:.4f}  (Bessel's correction)")

# Log-likelihood function
def neg_log_likelihood(params, X):
    mu, log_sigma = params
    sigma = np.exp(log_sigma)   # reparameterise to ensure sigma > 0
    return -np.sum(norm.logpdf(X, mu, sigma))

# Gradient-based MLE (should match closed-form)
result = minimize(neg_log_likelihood, x0=[0.0, 0.0], args=(X,), method='L-BFGS-B')
mu_opt, sigma_opt = result.x[0], np.exp(result.x[1])
print(f"Gradient ascent: mu={mu_opt:.4f}, sigma={sigma_opt:.4f}")

# Log-likelihood at MLE vs other values
ell_mle   = -neg_log_likelihood([mu_hat, np.log(sigma_hat)], X)
ell_wrong = -neg_log_likelihood([mu_hat + 0.5, np.log(sigma_hat)], X)
print(f"\nLog-likelihood at MLE:       {ell_mle:.2f}")
print(f"Log-likelihood at mu+0.5:    {ell_wrong:.2f}  (lower, as expected)")

# MLE for Bernoulli: p_hat = k/n (proportion of successes)
k, n_bern = 37, 100
p_hat = k / n_bern
print(f"\n=== Bernoulli MLE ===")
print(f"Observed: {k}/{n_bern} successes => p_hat = {p_hat:.4f}")
# Log-likelihood: k*log(p) + (n-k)*log(1-p)
p_grid = np.linspace(0.01, 0.99, 1000)
ll = k * np.log(p_grid) + (n_bern - k) * np.log(1 - p_grid)
print(f"Max LL at p={p_grid[np.argmax(ll)]:.4f}")
```

## MLE for Logistic Regression

For binary classification with label y ∈ {0,1} and features x, logistic regression assumes:

p(y=1|x, w) = σ(wᵀx) = 1/(1 + exp(−wᵀx))

The log-likelihood for n iid observations is:

ℓ(w) = Σᵢ [yᵢ log σ(wᵀxᵢ) + (1−yᵢ) log(1−σ(wᵀxᵢ))]
     = Σᵢ [yᵢ wᵀxᵢ − log(1 + exp(wᵀxᵢ))]

This is concave in w (the Hessian is −X^T D X where D is diagonal with positive entries), so gradient ascent or Newton-Raphson converges to the global maximum. The gradient is:

∇_w ℓ(w) = Σᵢ (yᵢ − σ(wᵀxᵢ)) xᵢ = X^T (y − ŷ)

Newton-Raphson update: w_{t+1} = w_t − H⁻¹ ∇ℓ where H = −X^T D X (IRLS: iteratively reweighted least squares).

```python
import numpy as np
from scipy.special import expit  # numerically stable sigmoid

rng = np.random.default_rng(42)

# Generate binary classification data
n, d = 500, 3
X = rng.standard_normal((n, d))
X = np.hstack([np.ones((n,1)), X])   # add intercept
w_true = np.array([0.5, 1.2, -0.8, 0.3])
y = (rng.uniform(size=n) < expit(X @ w_true)).astype(float)

def log_likelihood(w, X, y):
    p = expit(X @ w)
    return np.sum(y * np.log(p + 1e-15) + (1-y) * np.log(1-p + 1e-15))

def gradient(w, X, y):
    return X.T @ (y - expit(X @ w))

def hessian(w, X):
    p = expit(X @ w)
    D = np.diag(p * (1 - p))   # weights
    return -X.T @ D @ X

# Newton-Raphson (IRLS)
print("=== Logistic Regression: Newton-Raphson ===")
w = np.zeros(d + 1)
for it in range(10):
    g = gradient(w, X, y)
    H = hessian(w, X)
    w = w - np.linalg.solve(H, g)   # w = w - H^{-1} g
    ll = log_likelihood(w, X, y)
    grad_norm = np.linalg.norm(g)
    print(f"  iter {it+1:2d}: ll={ll:.4f}  ||grad||={grad_norm:.4e}")

print(f"\nTrue w: {w_true}")
print(f"MLE  w: {np.round(w, 4)}")

# Gradient ascent comparison
print("\n=== Gradient Ascent (lr=0.1) ===")
w_gd = np.zeros(d + 1)
for it in range(100):
    w_gd += 0.1 * gradient(w_gd, X, y)
print(f"GD w (100 steps): {np.round(w_gd, 4)}")
print(f"Newton converges in ~5 steps; GD needs many more.")
```

## Fisher Information and Cramér-Rao Bound

The Fisher information matrix measures how much information the data carries about θ:

I(θ) = E_θ[(∇_θ log p(X|θ))(∇_θ log p(X|θ))^T] = −E_θ[∇²_θ log p(X|θ)]

For n iid observations: Iₙ(θ) = n I₁(θ).

The Cramér-Rao lower bound (CRLB) states that for any unbiased estimator θ̂ of θ:

Var(θ̂) ≥ I(θ)⁻¹

The MLE achieves this bound asymptotically (it is asymptotically efficient). Fisher information also determines the geometry used by natural gradient descent: the natural gradient ∇̃ℓ = I(θ)⁻¹ ∇ℓ follows the steepest ascent in the space of probability distributions (Fisher-Rao metric), not Euclidean parameter space.

## Asymptotic Properties of MLE

Under regularity conditions, the MLE has three key asymptotic properties:

1. **Consistency**: θ̂_n → θ* as n → ∞ (in probability). The MLE converges to the true parameter.

2. **Asymptotic normality**: √n (θ̂_n − θ*) → N(0, I(θ*)⁻¹). The MLE is approximately Gaussian around the true parameter, with variance shrinking as 1/n.

3. **Asymptotic efficiency**: the MLE achieves the Cramér-Rao lower bound — no other consistent estimator has smaller asymptotic variance.

4. **Invariance**: if θ̂ is the MLE of θ, then g(θ̂) is the MLE of g(θ) for any function g. This means MLE of σ² is (σ̂)², and MLE of log σ is log σ̂.

These properties justify using MLE as the default estimator: it is consistent, as efficient as possible, and its uncertainty can be quantified via the Fisher information.

```python
import numpy as np
from scipy.stats import norm

rng = np.random.default_rng(42)

# Demonstrate consistency: MLE converges to true theta as n grows
mu_true, sigma_true = 2.0, 1.5
print("=== MLE Consistency for Gaussian mu ===")
print(f"True mu = {mu_true}")
for n in [10, 100, 1000, 10000, 100000]:
    X = rng.normal(mu_true, sigma_true, n)
    mu_hat = np.mean(X)
    se = sigma_true / np.sqrt(n)
    print(f"  n={n:>7,}: mu_hat={mu_hat:.4f}  SE={se:.4f}  error={abs(mu_hat-mu_true):.4f}")

# Fisher information for Gaussian: I(mu) = 1/sigma^2
I_mu = 1 / sigma_true**2
print(f"\nFisher information I(mu) = 1/sigma^2 = {I_mu:.4f}")
print(f"Cramer-Rao bound on Var(mu_hat): >= 1/(n*I) = sigma^2/n")
print(f"MLE achieves: Var(sample mean) = sigma^2/n = {sigma_true**2/1000:.6f} (n=1000)")

# Asymptotic normality: sqrt(n)(mu_hat - mu_true) -> N(0, 1/I)
print("\n=== Asymptotic Normality Check (n=100, 5000 reps) ===")
n = 100; n_reps = 5000
mu_hats = [np.mean(rng.normal(mu_true, sigma_true, n)) for _ in range(n_reps)]
scaled = np.sqrt(n) * (np.array(mu_hats) - mu_true)   # should be ~ N(0, sigma^2)
print(f"Empirical std of sqrt(n)*(mu_hat - mu): {np.std(scaled):.4f}")
print(f"Theoretical (sigma):                    {sigma_true:.4f}")

# MLE invariance: MLE of sigma^2 is (sigma_hat)^2
X_sample = rng.normal(mu_true, sigma_true, 1000)
sigma_hat = np.std(X_sample, ddof=0)
print(f"\nMLE invariance: MLE of sigma^2 = (sigma_hat)^2 = {sigma_hat**2:.4f}")
print(f"Direct MLE of sigma^2 = {np.var(X_sample, ddof=0):.4f}  (same)")
```

## ML and AI Connections

MLE unifies the training objectives of nearly all discriminative models in ML:

- **Cross-entropy loss** = negative log-likelihood of a categorical model: minimise −Σᵢ log p(yᵢ|xᵢ, θ)
- **MSE loss** = negative log-likelihood under a Gaussian noise model: p(y|x,θ) = N(y; f(x,θ), σ²)
- **Binary cross-entropy** = negative log-likelihood of a Bernoulli model: p(y|x,θ) = σ(f(x,θ))^y (1−σ(f(x,θ)))^{1-y}
- **Contrastive loss / InfoNCE** = MLE for noise-contrastive estimation, learning representations by classifying real from noise samples

Fisher information also drives natural gradient methods (NGD, KFAC, Shampoo) which rescale gradients by the inverse Fisher matrix, taking steps that are equidistant in probability space rather than parameter space — potentially much faster convergence for ill-conditioned problems.

## Pitfalls

Common MLE pitfalls:

1. **Overfitting for small n**: MLE is asymptotically efficient but can severely overfit for small n. A Bernoulli model trained on 3 heads out of 3 flips gives p̂ = 1.0 — predicting heads with certainty. This is why MAP estimation (adding a prior) is preferred for small datasets.

2. **Non-identifiability**: if multiple θ values give the same likelihood, the MLE is not unique. Example: mixture models with permutable component labels. Regularisation or constraints break the symmetry.

3. **Numerical overflow in likelihood**: always work with log-likelihoods, never raw likelihoods. Πᵢ p(xᵢ|θ) underflows to 0 for n as small as 100 for typical ML models.

4. **Confusing MLE with MMSE**: MLE maximises p(D|θ) not E[θ|D]. For asymmetric posteriors or small n, the MLE can be far from the posterior mean.

> **WARNING: MLE Requires i.i.d. Data**
>
> Standard MLE theory assumes data points are independent and identically distributed. In practice, data often violates this: time series have temporal correlation, hierarchical data has cluster structure, and fine-tuning data may have domain shift. Ignoring dependence gives asymptotically wrong standard errors and may bias the MLE itself. Use robust standard errors, mixed-effects models, or separate likelihoods for correlated data.

| Model | Loss Function | MLE Interpretation |
| --- | --- | --- |
| Gaussian regression | MSE = (y-ŷ)² | MLE under p(y|x)=N(f(x,θ), σ²) |
| Logistic regression | Binary cross-entropy | MLE under p(y|x)=Bernoulli(σ(wᵀx)) |
| Softmax classifier | Cross-entropy | MLE under p(y|x)=Categorical(softmax(Wx)) |
| Language model | Cross-entropy per token | MLE under p(xₜ|x_{<t})=Categorical |
| VAE encoder | ELBO | Variational MLE for marginal log p(x) |
| GAN discriminator | Binary cross-entropy | Noise-contrastive MLE |

---

## Key Takeaways

- MLE finds θ̂ = argmax_θ Σᵢ log p(xᵢ|θ) — always work with log-likelihood for numerical stability and additive decomposability.
- Closed-form MLE exists for Gaussian (sample mean and biased variance), Bernoulli (sample proportion), and exponential family distributions generally.
- Logistic regression MLE is concave (globally optimal), found efficiently via Newton-Raphson (5-10 iterations) or gradient ascent.
- Fisher information I(θ) = E[(∇ log p)²] measures data informativeness; the Cramér-Rao bound Var(θ̂) ≥ 1/I(θ) lower-bounds any unbiased estimator's variance.
- MLE is asymptotically consistent, normally distributed, and efficient — but can badly overfit for small n; use MAP estimation (regularisation) in that regime.
- Training with cross-entropy loss, MSE loss, or binary cross-entropy is exactly MLE under Categorical, Gaussian, and Bernoulli models respectively.
- Natural gradient descent uses the Fisher information matrix to rescale gradients, stepping in probability space rather than parameter space for faster convergence on ill-conditioned problems.
