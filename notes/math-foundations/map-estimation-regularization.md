---
title: "MAP Estimation and Its Connection to Regularization"
slug: "map-estimation-regularization"
description: "MAP estimation as penalised MLE, Gaussian prior yields L2 regularisation, Laplace prior yields L1 (Lasso), empirical Bayes for hyperparameter selection, and when MAP differs from the posterior mean."
tags: ["probability", "statistics", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTWF4aW11bSBhIHBvc3RlcmlvcmkgKE1BUCkgZXN0aW1hdGlvbiBpcyB0aGUgbW9zdCBjb21tb24gYnJpZGdlIGJldHdlZW4gQmF5ZXNpYW4gc3RhdGlzdGljcyBhbmQgcHJhY3RpY2FsIE1MLiBJdCBhZGRzIGEgcHJpb3IgcCjOuCkgdG8gdGhlIE1MRSBvYmplY3RpdmUgYW5kIG1heGltaXNlcyB0aGUgdW5ub3JtYWxpc2VkIHBvc3RlcmlvciBwKER8zrgpIHAozrgpLiBUaGUgcmVtYXJrYWJsZSBpbnNpZ2h0IGlzIHRoYXQgdGhpcyBpcyBlcXVpdmFsZW50IHRvIHJlZ3VsYXJpc2VkIG1heGltdW0gbGlrZWxpaG9vZDogdGhlIEdhdXNzaWFuIHByaW9yIHByb2R1Y2VzIGV4YWN0bHkgTDIgKHJpZGdlKSByZWd1bGFyaXNhdGlvbiwgYW5kIHRoZSBMYXBsYWNlIHByaW9yIHByb2R1Y2VzIGV4YWN0bHkgTDEgKExhc3NvKSByZWd1bGFyaXNhdGlvbi4gVW5kZXJzdGFuZGluZyBNQVAgZXN0aW1hdGlvbiBzaG93cyB0aGF0IHJlZ3VsYXJpc2F0aW9uIGlzIG5vdCBhbiBhZCBob2MgdHJpY2sgYnV0IGEgcHJpbmNpcGxlZCBCYXllc2lhbiBjaG9pY2Ugb2YgcHJpb3IsIGFuZCB0aGF0IHRoZSByZWd1bGFyaXNhdGlvbiBzdHJlbmd0aCDOuyBjb250cm9scyB0aGUgcHJpb3Igc2NhbGUuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29yZSBEZWZpbml0aW9uIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTUFQIGVzdGltYXRpb24gZmluZHMgdGhlIG1vZGUgb2YgdGhlIHBvc3RlcmlvciBkaXN0cmlidXRpb246XG5cbs64zIJfTUFQID0gYXJnbWF4X864IHAozrh8RClcbiAgICAgICA9IGFyZ21heF/OuCBbbG9nIHAoRHzOuCkgKyBsb2cgcCjOuCldXG4gICAgICAgPSBhcmdtYXhfzrggW+KEkyjOuCkgKyBsb2cgcCjOuCldXG5cbkJlY2F1c2UgcChEKSBkb2VzIG5vdCBkZXBlbmQgb24gzrgsIHdlIG1heGltaXNlIHRoZSB1bm5vcm1hbGlzZWQgcG9zdGVyaW9yLiBNQVAgZXF1YWxzIE1MRSB3aGVuIHRoZSBwcmlvciBwKM64KSBpcyB1bmlmb3JtIChmbGF0L3VuaW5mb3JtYXRpdmUpIOKAlCB1bmlmb3JtIHByaW9yIGNvbnRyaWJ1dGVzIGEgY29uc3RhbnQgbG9nIHByaW9yIGFuZCBkb2VzIG5vdCBjaGFuZ2UgdGhlIGFyZ21heC5cblxuSW4gY29udHJhc3QgdG8gZnVsbCBCYXllc2lhbiBpbmZlcmVuY2UgKHdoaWNoIGNvbXB1dGVzIHRoZSBlbnRpcmUgcG9zdGVyaW9yIGRpc3RyaWJ1dGlvbiBwKM64fEQpKSwgTUFQIHJldHVybnMgb25seSBhIHBvaW50IGVzdGltYXRlIOKAlCB0aGUgcGVhayBvZiB0aGUgcG9zdGVyaW9yLiBUaGlzIG1ha2VzIE1BUCBjb21wdXRhdGlvbmFsbHkgdHJhY3RhYmxlIChvcHRpbWlzYXRpb24gcmF0aGVyIHRoYW4gaW50ZWdyYXRpb24pIGJ1dCBkaXNjYXJkcyB1bmNlcnRhaW50eSBpbmZvcm1hdGlvbi4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJHYXVzc2lhbiBQcmlvciA9IEwyIFJlZ3VsYXJpc2F0aW9uIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3VwcG9zZSB0aGUgcHJpb3Igb24gd2VpZ2h0cyB3IGlzIGFuIGlzb3Ryb3BpYyBHYXVzc2lhbjogcCh3KSA9IE4oMCwgz4NfcMKyIEkpLlxuXG5sb2cgcCh3KSA9IOKIkuKAlnfigJbCsiAvICgyz4NfcMKyKSArIGNvbnN0XG5cbk1BUCBvYmplY3RpdmU6XG7OuMyCX01BUCA9IGFyZ21heF93IFvihJModykg4oiSIOKAlnfigJbCsiAvICgyz4NfcMKyKV1cbiAgICAgICA9IGFyZ21pbl93IFviiJLihJModykgKyDOu+KAlnfigJbCsl0gICB3aGVyZSDOuyA9IDEvKDLPg19wwrIpXG5cblRoaXMgaXMgZXhhY3RseSByaWRnZSByZWdyZXNzaW9uIChMMi1yZWd1bGFyaXNlZCBsaW5lYXIgcmVncmVzc2lvbikgb3Igd2VpZ2h0IGRlY2F5IGluIG5ldXJhbCBuZXR3b3Jrcy4gVGhlIHJlZ3VsYXJpc2F0aW9uIHN0cmVuZ3RoIM67IGlzIHRoZSBpbnZlcnNlIG9mIHR3aWNlIHRoZSBwcmlvciB2YXJpYW5jZTpcbi0gTGFyZ2Ugz4NfcCAoZGlmZnVzZSBwcmlvcikg4oaSIHNtYWxsIM67IOKGkiB3ZWFrIHJlZ3VsYXJpc2F0aW9uIOKGkiBhcHByb2FjaGVzIE1MRVxuLSBTbWFsbCDPg19wICh0aWdodCBwcmlvciBuZWFyIDApIOKGkiBsYXJnZSDOuyDihpIgc3Ryb25nIHJlZ3VsYXJpc2F0aW9uIOKGkiBzaHJpbmtzIHdlaWdodHMgdG8gMFxuXG5UaGlzIHJldmVhbHMgdGhhdCB3ZWlnaHQgZGVjYXkgaW4gbmV1cmFsIG5ldHdvcmsgdHJhaW5pbmcgaXMgZXF1aXZhbGVudCB0byBwbGFjaW5nIGEgR2F1c3NpYW4gcHJpb3Igb24gdGhlIHdlaWdodHMg4oCUIGEgZnVuZGFtZW50YWwgQmF5ZXNpYW4ganVzdGlmaWNhdGlvbiBmb3IgdGhpcyB1bml2ZXJzYWwgaGV1cmlzdGljLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlLCBMYXNzbywgTGluZWFyUmVncmVzc2lvblxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgR2VuZXJhdGUgcmVncmVzc2lvbiBkYXRhXG5uLCBkID0gMTAwLCAyMFxuWCA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoKG4sIGQpKVxud190cnVlID0gcm5nLnN0YW5kYXJkX25vcm1hbChkKSAqIDAuNVxud190cnVlWzEwOl0gPSAwLjAgICAjIGxhc3QgMTAgY29lZmZpY2llbnRzIGFyZSB6ZXJvIChzcGFyc2UpXG55ID0gWCBAIHdfdHJ1ZSArIHJuZy5ub3JtYWwoMCwgMC41LCBuKVxuXG4jIE1MRSA9IE9MUyAodW5pZm9ybSBwcmlvcilcbm9scyA9IExpbmVhclJlZ3Jlc3Npb24oZml0X2ludGVyY2VwdD1GYWxzZSkuZml0KFgsIHkpXG5cbiMgTUFQIHdpdGggR2F1c3NpYW4gcHJpb3IgKHNpZ21hX3AgPSAxKSA9PiBMMiByZWcgd2l0aCBsYW1iZGEgPSAxLygyKjFeMikgPSAwLjVcbiMgQnV0IHNrbGVhcm4gUmlkZ2UgdXNlcyBhbHBoYSA9IGxhbWJkYSwgc28gYWxwaGEgPSAwLjVcbnNpZ21hX3AgPSAxLjBcbmxhbV9yaWRnZSA9IDEgLyAoMiAqIHNpZ21hX3AqKjIpXG5yaWRnZSA9IFJpZGdlKGFscGhhPWxhbV9yaWRnZSwgZml0X2ludGVyY2VwdD1GYWxzZSkuZml0KFgsIHkpXG5cbiMgTUFQIHdpdGggTGFwbGFjZSBwcmlvciAoYj0xKSA9PiBMMSByZWcgd2l0aCBsYW1iZGEgPSAxL2IgPSAxXG5iX2xhcGxhY2UgPSAxLjBcbmxhbV9sYXNzbyA9IDEgLyBiX2xhcGxhY2Vcbmxhc3NvID0gTGFzc28oYWxwaGE9bGFtX2xhc3NvIC8gbiwgZml0X2ludGVyY2VwdD1GYWxzZSwgbWF4X2l0ZXI9MTAwMDApLmZpdChYLCB5KVxuXG5wcmludChcIj09PSBNQVAgdnMgTUxFOiBjb2VmZmljaWVudCByZWNvdmVyeSA9PT1cIilcbnByaW50KGZcIlRydWUgdyAoZmlyc3QgNSk6ICB7bnAucm91bmQod190cnVlWzo1XSwgMyl9XCIpXG5wcmludChmXCJPTFMgIHcgKGZpcnN0IDUpOiAge25wLnJvdW5kKG9scy5jb2VmX1s6NV0sIDMpfVwiKVxucHJpbnQoZlwiUmlkZ2UgdyAoZmlyc3QgNSk6IHtucC5yb3VuZChyaWRnZS5jb2VmX1s6NV0sIDMpfVwiKVxucHJpbnQoZlwiTGFzc28gdyAoZmlyc3QgNSk6IHtucC5yb3VuZChsYXNzby5jb2VmX1s6NV0sIDMpfVwiKVxucHJpbnQoKVxucHJpbnQoZlwiVHJ1ZSB3IChsYXN0IDUsIHNob3VsZCBiZSAwKToge25wLnJvdW5kKHdfdHJ1ZVsxNTpdLCAzKX1cIilcbnByaW50KGZcIk9MUyAgdyAobGFzdCA1KTogIHtucC5yb3VuZChvbHMuY29lZl9bMTU6XSwgMyl9XCIpXG5wcmludChmXCJSaWRnZSB3IChsYXN0IDUpOiB7bnAucm91bmQocmlkZ2UuY29lZl9bMTU6XSwgMyl9XCIpXG5wcmludChmXCJMYXNzbyB3IChsYXN0IDUpOiB7bnAucm91bmQobGFzc28uY29lZl9bMTU6XSwgMyl9XCIpXG5cbnByaW50KFwiXFxuPT09IE51bWJlciBvZiB6ZXJvIGNvZWZmaWNpZW50cyAoc3BhcnNpdHkpID09PVwiKVxuZXBzID0gMWUtNFxucHJpbnQoZlwiT0xTICAgemVyb3M6IHtucC5zdW0obnAuYWJzKG9scy5jb2VmXykgICA8IGVwcyl9LzIwXCIpXG5wcmludChmXCJSaWRnZSB6ZXJvczoge25wLnN1bShucC5hYnMocmlkZ2UuY29lZl8pIDwgZXBzKX0vMjBcIilcbnByaW50KGZcIkxhc3NvIHplcm9zOiB7bnAuc3VtKG5wLmFicyhsYXNzby5jb2VmXykgPCBlcHMpfS8yMFwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkxhcGxhY2UgUHJpb3IgPSBMMSBSZWd1bGFyaXNhdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBMYXBsYWNlIChkb3VibGUgZXhwb25lbnRpYWwpIHByaW9yOiBwKHcpIOKInSBleHAo4oiSzrt8d3wpXG5cbmxvZyBwKHcpID0g4oiSzrvigJZ34oCW4oKBICsgY29uc3RcblxuTUFQIG9iamVjdGl2ZTpcbs64zIJfTUFQID0gYXJnbWluX3cgW+KIkuKEkyh3KSArIM674oCWd+KAluKCgV1cblxuVGhpcyBpcyB0aGUgTGFzc28gKExlYXN0IEFic29sdXRlIFNocmlua2FnZSBhbmQgU2VsZWN0aW9uIE9wZXJhdG9yKSBmb3IgbGluZWFyIHJlZ3Jlc3Npb24uIFRoZSBMYXBsYWNlIHByaW9yIGhhcyBoZWF2aWVyIHRhaWxzIHRoYW4gdGhlIEdhdXNzaWFuIGJ1dCBhIHNoYXJwIHBlYWsgYXQgemVybywgd2hpY2ggZW5jb3VyYWdlcyBleGFjdCBzcGFyc2l0eTogbWFueSB3ZWlnaHRzIGFyZSBzZXQgdG8gZXhhY3RseSAwLiBJbiBjb250cmFzdCwgdGhlIEdhdXNzaWFuIHByaW9yIHNocmlua3Mgd2VpZ2h0cyB0b3dhcmQgemVybyBidXQgYWxtb3N0IG5ldmVyIHNldHMgdGhlbSBleGFjdGx5IHRvIHplcm8uXG5cbkludHVpdGl2ZWx5OiBhdCBhIHdlaWdodCB3ID0gzrUgbmVhciB6ZXJvLCB0aGUgTDIgcGVuYWx0eSBncmFkaWVudCBpcyAyzrvOtSAoc21hbGwpLCBub3QgcHVzaGluZyBzdHJvbmdseSB0b3dhcmQgemVyby4gVGhlIEwxIHBlbmFsdHkgZ3JhZGllbnQgaXMgzrsgKGNvbnN0YW50KSwgYWx3YXlzIHB1c2hpbmcgdG93YXJkIHplcm8gd2l0aCB0aGUgc2FtZSBmb3JjZSByZWdhcmRsZXNzIG9mIHRoZSB3ZWlnaHQgbWFnbml0dWRlLiBUaGlzIGNvbnN0YW50IHB1c2ggaXMgd2hhdCBjcmVhdGVzIGV4YWN0IHplcm9zIHRocm91Z2ggdGhlIHN1YmRpZmZlcmVudGlhbCBhdCB3ID0gMC4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJFbXBpcmljYWwgQmF5ZXMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJIb3cgZG8gd2UgY2hvb3NlIHRoZSByZWd1bGFyaXNhdGlvbiBzdHJlbmd0aCDOuyAoZXF1aXZhbGVudGx5LCB0aGUgcHJpb3IgaHlwZXJwYXJhbWV0ZXIgz4NfcCk/IFNldmVyYWwgYXBwcm9hY2hlczpcblxuMS4gKipDcm9zcy12YWxpZGF0aW9uKio6IGdyaWQgc2VhcmNoIG92ZXIgzrsgdmFsdWVzLCBzZWxlY3QgYnkgaGVsZC1vdXQgbG9zcy4gUHJhY3RpY2FsIGFuZCBtb2RlbC1hZ25vc3RpYy5cblxuMi4gKipFbXBpcmljYWwgQmF5ZXMgKFR5cGUtSUkgTUxFKSoqOiBtYXhpbWlzZSB0aGUgbWFyZ2luYWwgbGlrZWxpaG9vZCBwKER8zrspID0g4oirIHAoRHx3LCDOuykgcCh3fM67KSBkdyBvdmVyIM67LiBUaGlzIG1hcmdpbmFsaXNlcyBvdXQgdywgc28gzrsgaXMgY2hvc2VuIGJ5IHRoZSBkYXRhIGl0c2VsZiDigJQgJ2xldHRpbmcgdGhlIGRhdGEgY2hvb3NlIHRoZSBwcmlvcicuXG5cbjMuICoqRXZpZGVuY2UgbWF4aW1pc2F0aW9uKio6IGZvciBHYXVzc2lhbiBsaW5lYXIgbW9kZWxzLCB0aGUgbWFyZ2luYWwgbGlrZWxpaG9vZCBoYXMgYSBjbG9zZWQgZm9ybS4gRm9yIG5ldXJhbCBuZXR3b3JrcywgaXQgaXMgYXBwcm94aW1hdGVkIHZpYSBMYXBsYWNlIGFwcHJveGltYXRpb24gb3IgRUxCTyBtZXRob2RzLlxuXG5FbXBpcmljYWwgQmF5ZXMgY2FuIG92ZXJmaXQgKGVzcGVjaWFsbHkgZm9yIHNtYWxsIGRhdGFzZXRzKSBiZWNhdXNlIHdlIGFyZSBjaG9vc2luZyB0aGUgcHJpb3IgYmFzZWQgb24gdGhlIGRhdGEg4oCUIHRlY2huaWNhbGx5IGEgZnJlcXVlbnRpc3QgbWV0aG9kIGRlc3BpdGUgdGhlIEJheWVzaWFuIGZyYW1pbmcuIFVzZSBjcm9zcy12YWxpZGF0aW9uIGFzIGEgc2FuaXR5IGNoZWNrLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplX3NjYWxhclxuZnJvbSBzY2lweS5saW5hbGcgaW1wb3J0IHNvbHZlXG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0MilcblxuIyBFbXBpcmljYWwgQmF5ZXMgZm9yIEdhdXNzaWFuIGxpbmVhciByZWdyZXNzaW9uXG4jIE1vZGVsOiB5ID0gWHcgKyBlcHMsIHcgfiBOKDAsIGFscGhhXnstMX0gSSksIGVwcyB+IE4oMCwgYmV0YV57LTF9IEkpXG4jIE1hcmdpbmFsIGxpa2VsaWhvb2Q6IHAoeXxYLCBhbHBoYSwgYmV0YSkgPSBOKHk7IDAsIGJldGFeey0xfUkgKyBhbHBoYV57LTF9IFhYXlQpXG4jIEhlcmUgd2UgZmluZCBhbHBoYSAocHJpb3IgcHJlY2lzaW9uKSB2aWEgbWFyZ2luYWwgbGlrZWxpaG9vZCBtYXhpbWlzYXRpb25cblxubiwgZCA9IDUwLCA1XG5YID0gcm5nLnN0YW5kYXJkX25vcm1hbCgobiwgZCkpXG53X3RydWUgPSBybmcuc3RhbmRhcmRfbm9ybWFsKGQpXG5iZXRhID0gMjUuMCAgIyBub2lzZSBwcmVjaXNpb24gKGtub3duIGZvciBzaW1wbGljaXR5KVxueSA9IFggQCB3X3RydWUgKyBybmcubm9ybWFsKDAsIDEvbnAuc3FydChiZXRhKSwgbilcblxuZGVmIGxvZ19tYXJnaW5hbF9saWtlbGlob29kKGxvZ19hbHBoYSk6XG4gICAgYWxwaGEgPSBucC5leHAobG9nX2FscGhhKVxuICAgICMgQ292YXJpYW5jZSBvZiB5OiBDID0gKDEvYmV0YSkgSSArICgxL2FscGhhKSBYIFheVFxuICAgIEMgPSAoMS9iZXRhKSAqIG5wLmV5ZShuKSArICgxL2FscGhhKSAqIFggQCBYLlRcbiAgICBzaWduLCBsb2dkZXQgPSBucC5saW5hbGcuc2xvZ2RldChDKVxuICAgIHlfQ2ludl95ID0geSBAIG5wLmxpbmFsZy5zb2x2ZShDLCB5KVxuICAgIHJldHVybiAtMC41ICogKG4gKiBucC5sb2coMipucC5waSkgKyBsb2dkZXQgKyB5X0NpbnZfeSlcblxuIyBTZWFyY2ggb3ZlciBhbHBoYSB2YWx1ZXNcbmFscGhhX2dyaWQgPSBucC5sb2dzcGFjZSgtMywgMywgMTAwKVxubG1sX3ZhbHMgPSBbbG9nX21hcmdpbmFsX2xpa2VsaWhvb2QobnAubG9nKGEpKSBmb3IgYSBpbiBhbHBoYV9ncmlkXVxuYmVzdF9hbHBoYSA9IGFscGhhX2dyaWRbbnAuYXJnbWF4KGxtbF92YWxzKV1cbnByaW50KGZcIkVtcGlyaWNhbCBCYXllcyBiZXN0IGFscGhhIChwcmlvciBwcmVjaXNpb24pID0ge2Jlc3RfYWxwaGE6LjRmfVwiKVxucHJpbnQoZlwiQ29ycmVzcG9uZGluZyBsYW1iZGEgPSBhbHBoYS9iZXRhID0ge2Jlc3RfYWxwaGEvYmV0YTouNGZ9XCIpXG5wcmludChmXCJDb3JyZXNwb25kaW5nIHNpZ21hX3ByaW9yID0gMS9zcXJ0KGFscGhhKSA9IHsxL25wLnNxcnQoYmVzdF9hbHBoYSk6LjRmfVwiKVxuXG4jIE1BUCBlc3RpbWF0ZSB3aXRoIGVtcGlyaWNhbCBCYXllcyBwcmlvclxuQSA9IGJldGEgKiBYLlQgQCBYICsgYmVzdF9hbHBoYSAqIG5wLmV5ZShkKVxud19tYXAgPSBiZXRhICogc29sdmUoQSwgWC5UIEAgeSlcbndfbWxlID0gbnAubGluYWxnLmxzdHNxKFgsIHksIHJjb25kPU5vbmUpWzBdXG5wcmludChmXCJcXG5UcnVlIHc6ICAgICAgIHtucC5yb3VuZCh3X3RydWUsIDMpfVwiKVxucHJpbnQoZlwiTUxFIHc6ICAgICAgICB7bnAucm91bmQod19tbGUsIDMpfVwiKVxucHJpbnQoZlwiRW1wLiBCYXllcyB3OiB7bnAucm91bmQod19tYXAsIDMpfVwiKVxucHJpbnQoZlwiXFxuTVNFKE1MRSk6ICAgIHtucC5tZWFuKCh3X21sZSAtIHdfdHJ1ZSkqKjIpOi40Zn1cIilcbnByaW50KGZcIk1TRShFQi1NQVApOiB7bnAubWVhbigod19tYXAgLSB3X3RydWUpKioyKTouNGZ9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTUFQIHZzIE1MRSB2cyBQb3N0ZXJpb3IgTWVhbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZvciBhIEdhdXNzaWFuIHBvc3RlcmlvciAoZS5nLiwgQmF5ZXNpYW4gbGluZWFyIHJlZ3Jlc3Npb24gd2l0aCBHYXVzc2lhbiBwcmlvciBhbmQgR2F1c3NpYW4gbGlrZWxpaG9vZCksIHRoZSBNQVAgZXN0aW1hdGUgZXF1YWxzIHRoZSBwb3N0ZXJpb3IgbWVhbi4gVGhpcyBpcyBiZWNhdXNlIGEgR2F1c3NpYW4gaXMgc3ltbWV0cmljIGFuZCB1bmltb2RhbCwgc28gaXRzIG1vZGUgZXF1YWxzIGl0cyBtZWFuLlxuXG5Gb3Igbm9uLUdhdXNzaWFuIHBvc3RlcmlvcnMgKGxvZ2lzdGljIHJlZ3Jlc3Npb24sIGNvbXBsZXggbW9kZWxzKSwgTUFQIGRpZmZlcnMgZnJvbSB0aGUgcG9zdGVyaW9yIG1lYW46XG4tIE1BUCBpcyB0aGUgbW9kZTogdGhlIHNpbmdsZSBtb3N0IHByb2JhYmxlIHBhcmFtZXRlciB2YWx1ZVxuLSBQb3N0ZXJpb3IgbWVhbjogdGhlIHByb2JhYmlsaXR5LXdlaWdodGVkIGF2ZXJhZ2Ugb3ZlciBhbGwgcGFyYW1ldGVyIHZhbHVlc1xuLSBQb3N0ZXJpb3IgbWVhbiBtaW5pbWlzZXMgZXhwZWN0ZWQgc3F1YXJlZCBsb3NzLCBNQVAgbWluaW1pc2VzIDAtMSBsb3NzIChmaW5kcyB0aGUgbW9zdCBwcm9iYWJsZSBwb2ludClcblxuRm9yIGFzeW1tZXRyaWMgb3IgbXVsdGltb2RhbCBwb3N0ZXJpb3JzIChjb21tb24gaW4gZGVlcCBsZWFybmluZyksIHRoZSBNQVAgZXN0aW1hdGUgbWF5IGJlIGEgcG9vciBzdW1tYXJ5IG9mIHRoZSBwb3N0ZXJpb3IuIEZvciBleGFtcGxlLCBpZiB0aGUgcG9zdGVyaW9yIGhhcyB0d28gcm91Z2hseSBlcXVhbCBtb2RlcywgdGhlIE1BUCBwaWNrcyBvbmUgYW5kIGlnbm9yZXMgdGhlIG90aGVyIOKAlCB0aGUgcG9zdGVyaW9yIG1lYW4gbWlnaHQgZmFsbCBiZXR3ZWVuIHRoZSBtb2RlcyBpbiBhIGxvdy1wcm9iYWJpbGl0eSByZWdpb24uIEluIGRlZXAgbGVhcm5pbmcsIG1hbnkgbG9jYWwgbWluaW1hIGFyZSBhcHByb3hpbWF0ZWx5IGVxdWFsbHkgZ29vZCAoZmxhdCBsb3NzIGxhbmRzY2FwZSksIGFuZCBNQVAganVzdCBmaW5kcyBvbmUgb2YgdGhlbS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5IGltcG9ydCBzdGF0c1xuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgQmV0YS1CaW5vbWlhbDogTUFQIHZzIHBvc3RlcmlvciBtZWFuXG4jIFBvc3RlcmlvcjogQmV0YShhICsgaywgYiArIG4gLSBrKSB3aGVyZSBwcmlvciBpcyBCZXRhKGEsIGIpXG4jIE1BUCA9IChhICsgayAtIDEpIC8gKGEgKyBiICsgbiAtIDIpICAgKG1vZGUgb2YgQmV0YSlcbiMgTWVhbiA9IChhICsgaykgLyAoYSArIGIgKyBuKVxuXG5uX2ZsaXBzLCBrX2hlYWRzID0gMTAsIDNcbmFfcHJpb3IsIGJfcHJpb3IgPSAyLjAsIDIuMCAgIyBCZXRhKDIsMikgc3ltbWV0cmljIHByaW9yXG5cbmFfcG9zdCA9IGFfcHJpb3IgKyBrX2hlYWRzXG5iX3Bvc3QgPSBiX3ByaW9yICsgKG5fZmxpcHMgLSBrX2hlYWRzKVxuXG5tYXBfZXN0ICA9IChhX3Bvc3QgLSAxKSAvIChhX3Bvc3QgKyBiX3Bvc3QgLSAyKVxucG9zdF9tZWFuID0gYV9wb3N0IC8gKGFfcG9zdCArIGJfcG9zdClcbm1sZV9lc3QgID0ga19oZWFkcyAvIG5fZmxpcHNcblxucHJpbnQoXCI9PT0gQmV0YS1CZXJub3VsbGk6IE1BUCB2cyBNTEUgdnMgUG9zdGVyaW9yIE1lYW4gPT09XCIpXG5wcmludChmXCJEYXRhOiB7a19oZWFkc30ve25fZmxpcHN9IGhlYWRzLCBQcmlvcjogQmV0YSh7YV9wcmlvcn0sIHtiX3ByaW9yfSlcIilcbnByaW50KGZcIlBvc3RlcmlvcjogQmV0YSh7YV9wb3N0fSwge2JfcG9zdH0pXCIpXG5wcmludChmXCJNTEU6ICAgICAgICAgICAge21sZV9lc3Q6LjRmfVwiKVxucHJpbnQoZlwiTUFQOiAgICAgICAgICAgIHttYXBfZXN0Oi40Zn0gIChtb2RlIG9mIEJldGEpXCIpXG5wcmludChmXCJQb3N0ZXJpb3IgbWVhbjoge3Bvc3RfbWVhbjouNGZ9ICAobWVhbiBvZiBCZXRhKVwiKVxuXG4jIEVmZmVjdCBvZiBzYW1wbGUgc2l6ZSBvbiBNQVAgdnMgcG9zdGVyaW9yIG1lYW4gZ2FwXG5wcmludChcIlxcbj09PSBNQVAgdnMgUG9zdGVyaW9yIE1lYW4gYXMgbiBncm93cyA9PT1cIilcbmZvciBuIGluIFs1LCAyMCwgMTAwLCAxMDAwXTpcbiAgICBrID0gcm91bmQoMC4zICogbikgICMgMzAlIGhlYWRzXG4gICAgYXAsIGJwID0gYV9wcmlvciArIGssIGJfcHJpb3IgKyAobiAtIGspXG4gICAgbWFwX2UgID0gKGFwIC0gMSkgLyAoYXAgKyBicCAtIDIpXG4gICAgbWVhbl9lID0gYXAgLyAoYXAgKyBicClcbiAgICBwcmludChmXCIgIG49e246PjV9OiBrPXtrOj4zfSAgTUFQPXttYXBfZTouNGZ9ICBFW3RoZXRhfERdPXttZWFuX2U6LjRmfSAgZGlmZj17YWJzKG1hcF9lLW1lYW5fZSk6LjRmfVwiKVxucHJpbnQoXCIgIC0+IE1BUCBhbmQgcG9zdGVyaW9yIG1lYW4gY29udmVyZ2UgYXMgbiAtPiBpbmZcIilcblxuIyBWaXN1YWxpc2U6IE1BUCB2cyBwb3N0ZXJpb3IgbWVhbiBmb3Igc2tld2VkIHBvc3RlcmlvclxucHJpbnQoXCJcXG49PT0gU2tld2VkIEdhbW1hIHBvc3RlcmlvciA9PT1cIilcbiMgUG9zdGVyaW9yIH4gR2FtbWEoc2hhcGUsIHJhdGUpIOKAlCBhc3ltbWV0cmljLCBNQVAgIT0gbWVhblxuc2hhcGUsIHJhdGUgPSAyLjUsIDMuMFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgZ2FtbWFcbm1vZGVfZ2FtbWEgPSAoc2hhcGUgLSAxKSAvIHJhdGUgaWYgc2hhcGUgPj0gMSBlbHNlIDAuMFxubWVhbl9nYW1tYSA9IHNoYXBlIC8gcmF0ZVxucHJpbnQoZlwiR2FtbWEoe3NoYXBlfSwge3JhdGV9KTogbW9kZShNQVApPXttb2RlX2dhbW1hOi40Zn0sIG1lYW49e21lYW5fZ2FtbWE6LjRmfSwgZGlmZj17YWJzKG1lYW5fZ2FtbWEtbW9kZV9nYW1tYSk6LjRmfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQ29tbW9uIE1BUCBlc3RpbWF0aW9uIHBpdGZhbGxzOlxuXG4xLiAqKkNvbmZ1c2luZyBwcmlvciBzY2FsZSB3aXRoIHJlZ3VsYXJpc2F0aW9uIHN0cmVuZ3RoKio6IM67ID0gMS8oMs+DX3DCsikgZm9yIEwyOyBkb3VibGluZyB0aGUgcHJpb3IgdmFyaWFuY2UgaGFsdmVzIM67LiBBbHdheXMgYmUgY2xlYXIgd2hpY2ggcGFyYW1ldGVyaXNhdGlvbiB5b3UncmUgdXNpbmcuXG5cbjIuICoqTUFQIGlnbm9yZXMgcG9zdGVyaW9yIHVuY2VydGFpbnR5Kio6IGEgc2luZ2xlIHBvaW50IGVzdGltYXRlIGRpc2NhcmRzIHRoZSBzaGFwZSwgd2lkdGgsIGFuZCBtdWx0aW1vZGFsaXR5IG9mIHRoZSBwb3N0ZXJpb3IuIEZvciBzYWZldHktY3JpdGljYWwgYXBwbGljYXRpb25zLCBjb21wdXRlIHBvc3RlcmlvciBjcmVkaWJsZSBpbnRlcnZhbHMuXG5cbjMuICoqTW9kZSB2cyBtZWFuIG1pc21hdGNoKio6IGZvciBza2V3ZWQgcG9zdGVyaW9ycyAoR2FtbWEsIEJldGEgd2l0aCBsb3cgY291bnRzKSwgdGhlIE1BUCAobW9kZSkgY2FuIGJlIGZhciBmcm9tIHRoZSBwb3N0ZXJpb3IgbWVhbi4gVGhlIE1BUCBtaW5pbWlzZXMgMC0xIGxvc3M7IHRoZSBtZWFuIG1pbmltaXNlcyBzcXVhcmVkIGxvc3MuXG5cbjQuICoqRmxhdCByZWdpb25zIGluIGRlZXAgbGVhcm5pbmcqKjogbmV1cmFsIG5ldHdvcmtzIG9mdGVuIGhhdmUgbGFyZ2UgZmxhdCByZWdpb25zIGluIGxvc3MgbGFuZHNjYXBlIHdoZXJlIG1hbnkgY29uZmlndXJhdGlvbnMgYXJlIGFwcHJveGltYXRlbHkgZXF1YWxseSBnb29kLiAnTUFQJyBpbiB0aGlzIGNvbnRleHQgaXMganVzdCBvbmUgb2YgbWFueSBlcXVpdmFsZW50IHNvbHV0aW9ucyDigJQgdGhlIGludmFyaWFuY2Ugb2Ygb3ZlcnBhcmFtZXRlcmlzZWQgbW9kZWxzIG1ha2VzIHRoZSBwcmlvciBjaG9pY2UgcGFydGljdWxhcmx5IGltcG9ydGFudCBmb3IgaW1wbGljaXQgcmVndWxhcmlzYXRpb24uIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInZhcmlhbnQiOiAidGlwIiwgInRpdGxlIjogIkwyIFJlZ3VsYXJpc2F0aW9uIOKJoCBXZWlnaHQgRGVjYXkgaW4gQWRhcHRpdmUgTWV0aG9kcyIsICJjb250ZW50IjogIkZvciBTR0Qgd2l0aCBtb21lbnR1bSwgTDIgcmVndWxhcmlzYXRpb24gKGFkZGluZyDOu+KAlnfigJbCsiB0byB0aGUgbG9zcykgYW5kIHdlaWdodCBkZWNheSAobXVsdGlwbHlpbmcgd2VpZ2h0cyBieSAoMeKIks67wrdscikgYWZ0ZXIgZWFjaCBzdGVwKSBhcmUgZXF1aXZhbGVudC4gRm9yIEFkYW0gYW5kIG90aGVyIGFkYXB0aXZlIG1ldGhvZHMsIHRoZXkgYXJlIE5PVCBlcXVpdmFsZW50OiBMMiByZWcgcmVzY2FsZXMgdGhlIGdyYWRpZW50LCB3aGljaCBpcyB0aGVuIGRpdmlkZWQgYnkgdGhlIGFkYXB0aXZlIHN0ZXAgc2l6ZSwgcmVkdWNpbmcgdGhlIGVmZmVjdGl2ZSByZWd1bGFyaXNhdGlvbiBmb3IgcGFyYW1ldGVycyB3aXRoIGxhcmdlIGdyYWRpZW50cy4gQWRhbVcgKGRlY291cGxlZCB3ZWlnaHQgZGVjYXkpIGFwcGxpZXMgd2VpZ2h0IGRlY2F5IGRpcmVjdGx5IHRvIHRoZSB3ZWlnaHRzLCBub3QgdGhyb3VnaCB0aGUgZ3JhZGllbnQsIHJlc3RvcmluZyB0aGUgaW50ZW5kZWQgQmF5ZXNpYW4gcHJpb3IgaW50ZXJwcmV0YXRpb24uIn0sIHsidHlwZSI6ICJ0YWJsZSIsICJoZWFkZXJzIjogWyJQcmlvciIsICJSZWd1bGFyaXNhdGlvbiIsICJFZmZlY3QiLCAiVHlwaWNhbCDOuyJdLCAicm93cyI6IFtbIlVuaWZvcm0gKGltcHJvcGVyKSIsICJOb25lIChNTEUpIiwgIk5vIHNocmlua2FnZSIsICLigJQiXSwgWyJHYXVzc2lhbiBOKDAsz4PCskkpIiwgIkwyIC8gUmlkZ2UgLyB3ZWlnaHQgZGVjYXkiLCAiU2hyaW5rcyBhbGwgd2VpZ2h0cyB0b3dhcmQgMCIsICIwLjAx4oCTMC4xIl0sIFsiTGFwbGFjZSgwLGIpIiwgIkwxIC8gTGFzc28iLCAiRXhhY3Qgc3BhcnNpdHksIGZlYXR1cmUgc2VsZWN0aW9uIiwgIjAuMDAx4oCTMC4xIl0sIFsiU3R1ZGVudC10IiwgIlJvYnVzdCAoaGVhdnkgdGFpbHMpIiwgIkFsbG93cyBvY2Nhc2lvbmFsIGxhcmdlIHdlaWdodHMiLCAiQXBwbGljYXRpb24tc3BlY2lmaWMiXSwgWyJTcGlrZS1hbmQtc2xhYiIsICJIYXJkIHNwYXJzaXR5IiwgIkJpbmFyeSBtYXNrIG9uIGVhY2ggd2VpZ2h0IiwgIlZhcmlhdGlvbmFsIG9yIE1DTUMiXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAib3JkZXJlZCI6IGZhbHNlLCAiaXRlbXMiOiBbIk1BUCA9IGFyZ21heF/OuCBbbG9nIHAoRHzOuCkgKyBsb2cgcCjOuCldIOKAlCBpdCBpcyBNTEUgcGx1cyBhIGxvZy1wcmlvciBwZW5hbHR5OyB1bmlmb3JtIHByaW9yIHJlY292ZXJzIE1MRS4iLCAiR2F1c3NpYW4gcHJpb3IgTigwLCDPg19wwrJJKSDihpQgTDIgcmVndWxhcmlzYXRpb24gzrvigJZ34oCWwrIgd2l0aCDOuyA9IDEvKDLPg19wwrIpOyBsYXJnZSBwcmlvciB2YXJpYW5jZSA9IHdlYWsgcmVndWxhcmlzYXRpb24uIiwgIkxhcGxhY2UgcHJpb3IgZXhwKOKIks67fHd8KSDihpQgTDEgcmVndWxhcmlzYXRpb24gzrvigJZ34oCW4oKBOyB0aGUgc2hhcnAgemVyby1wZWFrIGNyZWF0ZXMgZXhhY3Qgc3BhcnNpdHkgdW5saWtlIHRoZSBHYXVzc2lhbi4iLCAiRW1waXJpY2FsIEJheWVzIHNlbGVjdHMgdGhlIHByaW9yIGh5cGVycGFyYW1ldGVyIM67IGJ5IG1heGltaXNpbmcgdGhlIG1hcmdpbmFsIGxpa2VsaWhvb2QgcChEfM67KSDigJQgbGV0dGluZyBkYXRhIGNob29zZSB0aGUgcHJpb3IuIiwgIk1BUCBlcXVhbHMgdGhlIHBvc3RlcmlvciBtZWFuIG9ubHkgZm9yIEdhdXNzaWFuIHBvc3RlcmlvcnMgKHN5bW1ldHJpYywgdW5pbW9kYWwpOyBmb3IgYXN5bW1ldHJpYyBvciBtdWx0aW1vZGFsIHBvc3RlcmlvcnMgdGhleSBkaWZmZXIuIiwgIkFkYW1XIGltcGxlbWVudHMgZGVjb3VwbGVkIHdlaWdodCBkZWNheSDigJQgZXF1aXZhbGVudCB0byBhIEdhdXNzaWFuIHByaW9yIHVuZGVyIEFkYW0g4oCUIHdoaWxlIEwyIHJlZ3VsYXJpc2F0aW9uIGluIEFkYW0gaXMgbm90IGVxdWl2YWxlbnQgZHVlIHRvIGFkYXB0aXZlIHN0ZXAgcmVzY2FsaW5nLiIsICJSZWd1bGFyaXNhdGlvbiBpbiBkZWVwIGxlYXJuaW5nIGlzIGltcGxpY2l0IE1BUDogTDIgd2VpZ2h0IGRlY2F5IGVuY29kZXMgYSBHYXVzc2lhbiBwcmlvciBvbiBhbGwgd2VpZ2h0czsgZHJvcG91dCBhcHByb3hpbWF0ZXMgYSBCZXJub3VsbGkgc3Bpa2UtYW5kLXNsYWIgcHJpb3IuIl19XQ=="
---
# MAP Estimation and Its Connection to Regularization

Maximum a posteriori (MAP) estimation is the most common bridge between Bayesian statistics and practical ML. It adds a prior p(θ) to the MLE objective and maximises the unnormalised posterior p(D|θ) p(θ). The remarkable insight is that this is equivalent to regularised maximum likelihood: the Gaussian prior produces exactly L2 (ridge) regularisation, and the Laplace prior produces exactly L1 (Lasso) regularisation. Understanding MAP estimation shows that regularisation is not an ad hoc trick but a principled Bayesian choice of prior, and that the regularisation strength λ controls the prior scale.

## Core Definition

MAP estimation finds the mode of the posterior distribution:

θ̂_MAP = argmax_θ p(θ|D)
       = argmax_θ [log p(D|θ) + log p(θ)]
       = argmax_θ [ℓ(θ) + log p(θ)]

Because p(D) does not depend on θ, we maximise the unnormalised posterior. MAP equals MLE when the prior p(θ) is uniform (flat/uninformative) — uniform prior contributes a constant log prior and does not change the argmax.

In contrast to full Bayesian inference (which computes the entire posterior distribution p(θ|D)), MAP returns only a point estimate — the peak of the posterior. This makes MAP computationally tractable (optimisation rather than integration) but discards uncertainty information.

## Gaussian Prior = L2 Regularisation

Suppose the prior on weights w is an isotropic Gaussian: p(w) = N(0, σ_p² I).

log p(w) = −‖w‖² / (2σ_p²) + const

MAP objective:
θ̂_MAP = argmax_w [ℓ(w) − ‖w‖² / (2σ_p²)]
       = argmin_w [−ℓ(w) + λ‖w‖²]   where λ = 1/(2σ_p²)

This is exactly ridge regression (L2-regularised linear regression) or weight decay in neural networks. The regularisation strength λ is the inverse of twice the prior variance:
- Large σ_p (diffuse prior) → small λ → weak regularisation → approaches MLE
- Small σ_p (tight prior near 0) → large λ → strong regularisation → shrinks weights to 0

This reveals that weight decay in neural network training is equivalent to placing a Gaussian prior on the weights — a fundamental Bayesian justification for this universal heuristic.

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso, LinearRegression

rng = np.random.default_rng(42)

# Generate regression data
n, d = 100, 20
X = rng.standard_normal((n, d))
w_true = rng.standard_normal(d) * 0.5
w_true[10:] = 0.0   # last 10 coefficients are zero (sparse)
y = X @ w_true + rng.normal(0, 0.5, n)

# MLE = OLS (uniform prior)
ols = LinearRegression(fit_intercept=False).fit(X, y)

# MAP with Gaussian prior (sigma_p = 1) => L2 reg with lambda = 1/(2*1^2) = 0.5
# But sklearn Ridge uses alpha = lambda, so alpha = 0.5
sigma_p = 1.0
lam_ridge = 1 / (2 * sigma_p**2)
ridge = Ridge(alpha=lam_ridge, fit_intercept=False).fit(X, y)

# MAP with Laplace prior (b=1) => L1 reg with lambda = 1/b = 1
b_laplace = 1.0
lam_lasso = 1 / b_laplace
lasso = Lasso(alpha=lam_lasso / n, fit_intercept=False, max_iter=10000).fit(X, y)

print("=== MAP vs MLE: coefficient recovery ===")
print(f"True w (first 5):  {np.round(w_true[:5], 3)}")
print(f"OLS  w (first 5):  {np.round(ols.coef_[:5], 3)}")
print(f"Ridge w (first 5): {np.round(ridge.coef_[:5], 3)}")
print(f"Lasso w (first 5): {np.round(lasso.coef_[:5], 3)}")
print()
print(f"True w (last 5, should be 0): {np.round(w_true[15:], 3)}")
print(f"OLS  w (last 5):  {np.round(ols.coef_[15:], 3)}")
print(f"Ridge w (last 5): {np.round(ridge.coef_[15:], 3)}")
print(f"Lasso w (last 5): {np.round(lasso.coef_[15:], 3)}")

print("\n=== Number of zero coefficients (sparsity) ===")
eps = 1e-4
print(f"OLS   zeros: {np.sum(np.abs(ols.coef_)   < eps)}/20")
print(f"Ridge zeros: {np.sum(np.abs(ridge.coef_) < eps)}/20")
print(f"Lasso zeros: {np.sum(np.abs(lasso.coef_) < eps)}/20")
```

## Laplace Prior = L1 Regularisation

The Laplace (double exponential) prior: p(w) ∝ exp(−λ|w|)

log p(w) = −λ‖w‖₁ + const

MAP objective:
θ̂_MAP = argmin_w [−ℓ(w) + λ‖w‖₁]

This is the Lasso (Least Absolute Shrinkage and Selection Operator) for linear regression. The Laplace prior has heavier tails than the Gaussian but a sharp peak at zero, which encourages exact sparsity: many weights are set to exactly 0. In contrast, the Gaussian prior shrinks weights toward zero but almost never sets them exactly to zero.

Intuitively: at a weight w = ε near zero, the L2 penalty gradient is 2λε (small), not pushing strongly toward zero. The L1 penalty gradient is λ (constant), always pushing toward zero with the same force regardless of the weight magnitude. This constant push is what creates exact zeros through the subdifferential at w = 0.

## Empirical Bayes

How do we choose the regularisation strength λ (equivalently, the prior hyperparameter σ_p)? Several approaches:

1. **Cross-validation**: grid search over λ values, select by held-out loss. Practical and model-agnostic.

2. **Empirical Bayes (Type-II MLE)**: maximise the marginal likelihood p(D|λ) = ∫ p(D|w, λ) p(w|λ) dw over λ. This marginalises out w, so λ is chosen by the data itself — 'letting the data choose the prior'.

3. **Evidence maximisation**: for Gaussian linear models, the marginal likelihood has a closed form. For neural networks, it is approximated via Laplace approximation or ELBO methods.

Empirical Bayes can overfit (especially for small datasets) because we are choosing the prior based on the data — technically a frequentist method despite the Bayesian framing. Use cross-validation as a sanity check.

```python
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.linalg import solve

rng = np.random.default_rng(42)

# Empirical Bayes for Gaussian linear regression
# Model: y = Xw + eps, w ~ N(0, alpha^{-1} I), eps ~ N(0, beta^{-1} I)
# Marginal likelihood: p(y|X, alpha, beta) = N(y; 0, beta^{-1}I + alpha^{-1} XX^T)
# Here we find alpha (prior precision) via marginal likelihood maximisation

n, d = 50, 5
X = rng.standard_normal((n, d))
w_true = rng.standard_normal(d)
beta = 25.0  # noise precision (known for simplicity)
y = X @ w_true + rng.normal(0, 1/np.sqrt(beta), n)

def log_marginal_likelihood(log_alpha):
    alpha = np.exp(log_alpha)
    # Covariance of y: C = (1/beta) I + (1/alpha) X X^T
    C = (1/beta) * np.eye(n) + (1/alpha) * X @ X.T
    sign, logdet = np.linalg.slogdet(C)
    y_Cinv_y = y @ np.linalg.solve(C, y)
    return -0.5 * (n * np.log(2*np.pi) + logdet + y_Cinv_y)

# Search over alpha values
alpha_grid = np.logspace(-3, 3, 100)
lml_vals = [log_marginal_likelihood(np.log(a)) for a in alpha_grid]
best_alpha = alpha_grid[np.argmax(lml_vals)]
print(f"Empirical Bayes best alpha (prior precision) = {best_alpha:.4f}")
print(f"Corresponding lambda = alpha/beta = {best_alpha/beta:.4f}")
print(f"Corresponding sigma_prior = 1/sqrt(alpha) = {1/np.sqrt(best_alpha):.4f}")

# MAP estimate with empirical Bayes prior
A = beta * X.T @ X + best_alpha * np.eye(d)
w_map = beta * solve(A, X.T @ y)
w_mle = np.linalg.lstsq(X, y, rcond=None)[0]
print(f"\nTrue w:       {np.round(w_true, 3)}")
print(f"MLE w:        {np.round(w_mle, 3)}")
print(f"Emp. Bayes w: {np.round(w_map, 3)}")
print(f"\nMSE(MLE):    {np.mean((w_mle - w_true)**2):.4f}")
print(f"MSE(EB-MAP): {np.mean((w_map - w_true)**2):.4f}")
```

## MAP vs MLE vs Posterior Mean

For a Gaussian posterior (e.g., Bayesian linear regression with Gaussian prior and Gaussian likelihood), the MAP estimate equals the posterior mean. This is because a Gaussian is symmetric and unimodal, so its mode equals its mean.

For non-Gaussian posteriors (logistic regression, complex models), MAP differs from the posterior mean:
- MAP is the mode: the single most probable parameter value
- Posterior mean: the probability-weighted average over all parameter values
- Posterior mean minimises expected squared loss, MAP minimises 0-1 loss (finds the most probable point)

For asymmetric or multimodal posteriors (common in deep learning), the MAP estimate may be a poor summary of the posterior. For example, if the posterior has two roughly equal modes, the MAP picks one and ignores the other — the posterior mean might fall between the modes in a low-probability region. In deep learning, many local minima are approximately equally good (flat loss landscape), and MAP just finds one of them.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Beta-Binomial: MAP vs posterior mean
# Posterior: Beta(a + k, b + n - k) where prior is Beta(a, b)
# MAP = (a + k - 1) / (a + b + n - 2)   (mode of Beta)
# Mean = (a + k) / (a + b + n)

n_flips, k_heads = 10, 3
a_prior, b_prior = 2.0, 2.0  # Beta(2,2) symmetric prior

a_post = a_prior + k_heads
b_post = b_prior + (n_flips - k_heads)

map_est  = (a_post - 1) / (a_post + b_post - 2)
post_mean = a_post / (a_post + b_post)
mle_est  = k_heads / n_flips

print("=== Beta-Bernoulli: MAP vs MLE vs Posterior Mean ===")
print(f"Data: {k_heads}/{n_flips} heads, Prior: Beta({a_prior}, {b_prior})")
print(f"Posterior: Beta({a_post}, {b_post})")
print(f"MLE:            {mle_est:.4f}")
print(f"MAP:            {map_est:.4f}  (mode of Beta)")
print(f"Posterior mean: {post_mean:.4f}  (mean of Beta)")

# Effect of sample size on MAP vs posterior mean gap
print("\n=== MAP vs Posterior Mean as n grows ===")
for n in [5, 20, 100, 1000]:
    k = round(0.3 * n)  # 30% heads
    ap, bp = a_prior + k, b_prior + (n - k)
    map_e  = (ap - 1) / (ap + bp - 2)
    mean_e = ap / (ap + bp)
    print(f"  n={n:>5}: k={k:>3}  MAP={map_e:.4f}  E[theta|D]={mean_e:.4f}  diff={abs(map_e-mean_e):.4f}")
print("  -> MAP and posterior mean converge as n -> inf")

# Visualise: MAP vs posterior mean for skewed posterior
print("\n=== Skewed Gamma posterior ===")
# Posterior ~ Gamma(shape, rate) — asymmetric, MAP != mean
shape, rate = 2.5, 3.0
from scipy.stats import gamma
mode_gamma = (shape - 1) / rate if shape >= 1 else 0.0
mean_gamma = shape / rate
print(f"Gamma({shape}, {rate}): mode(MAP)={mode_gamma:.4f}, mean={mean_gamma:.4f}, diff={abs(mean_gamma-mode_gamma):.4f}")
```

## Pitfalls

Common MAP estimation pitfalls:

1. **Confusing prior scale with regularisation strength**: λ = 1/(2σ_p²) for L2; doubling the prior variance halves λ. Always be clear which parameterisation you're using.

2. **MAP ignores posterior uncertainty**: a single point estimate discards the shape, width, and multimodality of the posterior. For safety-critical applications, compute posterior credible intervals.

3. **Mode vs mean mismatch**: for skewed posteriors (Gamma, Beta with low counts), the MAP (mode) can be far from the posterior mean. The MAP minimises 0-1 loss; the mean minimises squared loss.

4. **Flat regions in deep learning**: neural networks often have large flat regions in loss landscape where many configurations are approximately equally good. 'MAP' in this context is just one of many equivalent solutions — the invariance of overparameterised models makes the prior choice particularly important for implicit regularisation.

> **TIP: L2 Regularisation ≠ Weight Decay in Adaptive Methods**
>
> For SGD with momentum, L2 regularisation (adding λ‖w‖² to the loss) and weight decay (multiplying weights by (1−λ·lr) after each step) are equivalent. For Adam and other adaptive methods, they are NOT equivalent: L2 reg rescales the gradient, which is then divided by the adaptive step size, reducing the effective regularisation for parameters with large gradients. AdamW (decoupled weight decay) applies weight decay directly to the weights, not through the gradient, restoring the intended Bayesian prior interpretation.

| Prior | Regularisation | Effect | Typical λ |
| --- | --- | --- | --- |
| Uniform (improper) | None (MLE) | No shrinkage | — |
| Gaussian N(0,σ²I) | L2 / Ridge / weight decay | Shrinks all weights toward 0 | 0.01–0.1 |
| Laplace(0,b) | L1 / Lasso | Exact sparsity, feature selection | 0.001–0.1 |
| Student-t | Robust (heavy tails) | Allows occasional large weights | Application-specific |
| Spike-and-slab | Hard sparsity | Binary mask on each weight | Variational or MCMC |

---

## Key Takeaways

- MAP = argmax_θ [log p(D|θ) + log p(θ)] — it is MLE plus a log-prior penalty; uniform prior recovers MLE.
- Gaussian prior N(0, σ_p²I) ↔ L2 regularisation λ‖w‖² with λ = 1/(2σ_p²); large prior variance = weak regularisation.
- Laplace prior exp(−λ|w|) ↔ L1 regularisation λ‖w‖₁; the sharp zero-peak creates exact sparsity unlike the Gaussian.
- Empirical Bayes selects the prior hyperparameter λ by maximising the marginal likelihood p(D|λ) — letting data choose the prior.
- MAP equals the posterior mean only for Gaussian posteriors (symmetric, unimodal); for asymmetric or multimodal posteriors they differ.
- AdamW implements decoupled weight decay — equivalent to a Gaussian prior under Adam — while L2 regularisation in Adam is not equivalent due to adaptive step rescaling.
- Regularisation in deep learning is implicit MAP: L2 weight decay encodes a Gaussian prior on all weights; dropout approximates a Bernoulli spike-and-slab prior.
