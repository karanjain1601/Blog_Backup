---
title: "AdamW — Decoupled Weight Decay"
slug: "adamw-weight-decay"
description: "Rigorous analysis of why L2 regularization in standard Adam is corrupted by adaptive learning rates, AdamW's decoupled weight decay fix, and its role as the standard LLM optimizer."
tags: ["optimization", "regularization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3RhbmRhcmQgQWRhbSB3aXRoIEwyIHJlZ3VsYXJpemF0aW9uIHNpbGVudGx5IGNvcnJ1cHRzIHRoZSByZWd1bGFyaXphdGlvbjogdGhlIGFkYXB0aXZlIGRlbm9taW5hdG9yIHNxcnQodl9oYXQpIHNjYWxlcyBlYWNoIHBhcmFtZXRlcidzIGdyYWRpZW50IGRpZmZlcmVudGx5LCBtZWFuaW5nIEwyIHdlaWdodCBkZWNheSBpcyBhcHBsaWVkIG5vbi11bmlmb3JtbHkg4oCUIGV4YWN0bHkgdGhlIG9wcG9zaXRlIG9mIGl0cyBpbnRlbnQuIEFkYW1XIChMb3NoY2hpbG92ICYgSHV0dGVyIDIwMTkpIGZpeGVzIHRoaXMgYnkgZGVjb3VwbGluZyB3ZWlnaHQgZGVjYXkgZnJvbSB0aGUgZ3JhZGllbnQgdXBkYXRlLiBUaGlzIGluc2lnaHQgbWFrZXMgQWRhbVcgdGhlIHN0YW5kYXJkIG9wdGltaXplciBmb3IgdHJhaW5pbmcgR1BULCBCRVJULCBMTGFNQSwgYW5kIHZpcnR1YWxseSBldmVyeSBsYXJnZS1zY2FsZSBsYW5ndWFnZSBtb2RlbC4gVW5kZXJzdGFuZGluZyB3aHkgQWRhbStMMiBmYWlscyDigJQgYW5kIGhvdyBBZGFtVyBmaXhlcyBpdCDigJQgaXMgZXNzZW50aWFsIGZvciBhbnkgcHJhY3RpdGlvbmVyIHRyYWluaW5nIHRyYW5zZm9ybWVycyBhdCBzY2FsZS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJUaGUgUHJvYmxlbTogQWRhcHRpdmUgUmF0ZXMgQ29ycnVwdCBMMiBSZWd1bGFyaXphdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkluIHZhbmlsbGEgU0dEOiBMMiBtZWFucyBhZGRpbmcgbGFtYmRhKnRoZXRhIHRvIGdyYWRpZW50LCBzbyBlZmZlY3RpdmUgdXBkYXRlIGlzIHRoZXRhIDwtIHRoZXRhKigxLWV0YSpsYW1iZGEpIC0gZXRhKmcuIFRoZSBMMiBkZWNheSBldGEqbGFtYmRhIGlzIGFwcGxpZWQgdW5pZm9ybWx5IGFjcm9zcyBhbGwgcGFyYW1ldGVycy4gSW4gQWRhbTogdGhlIGVmZmVjdGl2ZSBncmFkaWVudCBpcyBnX2VmZiA9IGcgKyBsYW1iZGEqdGhldGEsIHdoaWNoIGlzIHRoZW4gZGl2aWRlZCBieSBzcXJ0KHZfaGF0KStlcHMuIFRoZSBlZmZlY3RpdmUgZGVjYXkgcGVyIHBhcmFtZXRlciBiZWNvbWVzIGV0YSpsYW1iZGEqdGhldGFfaS8oc3FydCh2X2hhdF9pKStlcHMpIOKAlCBpdCB2YXJpZXMgd2l0aCBncmFkaWVudCBoaXN0b3J5LiBQYXJhbWV0ZXJzIHdpdGggbGFyZ2UgZ3JhZGllbnQgaGlzdG9yeSAobGFyZ2Ugdl9pKSByZWNlaXZlIHdlYWtlciBMMiByZWd1bGFyaXphdGlvbi4gUGFyYW1ldGVycyB1cGRhdGVkIHJhcmVseSAoc21hbGwgdl9pKSByZWNlaXZlIHN0cm9uZ2VyIEwyLiBUaGlzIGlzIHRoZSBvcHBvc2l0ZSBvZiB3aGF0IEwyIGludGVuZHM6IGl0IHNob3VsZCBwZW5hbGl6ZSBsYXJnZSB3ZWlnaHRzIHVuaWZvcm1seSwgcmVnYXJkbGVzcyBvZiBncmFkaWVudCBoaXN0b3J5LiBUaGUgY29ycnVwdGlvbiBpcyB3b3JzdCB3aGVuIGdyYWRpZW50IG1hZ25pdHVkZXMgdmFyeSB3aWRlbHkgYWNyb3NzIHBhcmFtZXRlcnMg4oCUIGV4YWN0bHkgdGhlIGNhc2UgaW4gdHJhbnNmb3JtZXJzLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBTaG93IGVmZmVjdGl2ZSBMMiBkZWNheSBwZXIgcGFyYW1ldGVyIGZvciBBZGFtK0wyIHZzIEFkYW1XXG5ucC5yYW5kb20uc2VlZCg0Milcbm5fcGFyYW1zID0gNlxubGFtID0gMC4wMVxubHIgPSAxZS0zXG5cbiMgU2ltdWxhdGUgZGl2ZXJzZSBncmFkaWVudCBoaXN0b3JpZXNcbnRoZXRhID0gbnAub25lcyhuX3BhcmFtcykgKiAyLjBcbnZfaGF0ID0gbnAuYXJyYXkoWzFlLTQsIDFlLTMsIDAuMDEsIDAuMSwgMS4wLCAxMC4wXSkgICMgcmFuZ2Ugb2Ygc2Vjb25kIG1vbWVudHNcbmVwcyA9IDFlLThcblxuIyBBZGFtK0wyOiBlZmZlY3RpdmUgZGVjYXkgPSBsciAqIGxhbSAvIChzcXJ0KHZfaGF0KSArIGVwcylcbmcgPSBucC5vbmVzKG5fcGFyYW1zKSAqIDAuNSAgICMgdW5pZm9ybSBncmFkaWVudFxuZ19sMiA9IGcgKyBsYW0gKiB0aGV0YSAgICAgICAgICMgTDIgYWRkcyBsYW1iZGEqdGhldGEgdG8gZ3JhZGllbnRcbmVmZl9kZWNheV9hZGFtID0gbHIgKiBsYW0gKiB0aGV0YSAvIChucC5zcXJ0KHZfaGF0KSArIGVwcylcblxuIyBBZGFtVzogZWZmZWN0aXZlIGRlY2F5ID0gbHIgKiBsYW0gKHVuaWZvcm0pXG5lZmZfZGVjYXlfYWRhbXcgPSBucC5mdWxsKG5fcGFyYW1zLCBsciAqIGxhbSAqIHRoZXRhWzBdKVxuXG5wcmludChmXCJ7J3ZfaGF0Jzo+MTB9IHwgeydBZGFtK0wyIGRlY2F5Jzo+MTV9IHwgeydBZGFtVyBkZWNheSc6PjEyfSB8IHsncmF0aW8nOj44fVwiKVxucHJpbnQoXCItXCIgKiA1NSlcbmZvciBpIGluIHJhbmdlKG5fcGFyYW1zKTpcbiAgICByYXRpbyA9IGVmZl9kZWNheV9hZGFtW2ldIC8gZWZmX2RlY2F5X2FkYW13W2ldXG4gICAgcHJpbnQoZlwie3ZfaGF0W2ldOj4xMC40Zn0gfCB7ZWZmX2RlY2F5X2FkYW1baV06PjE1LjZmfSB8IHtlZmZfZGVjYXlfYWRhbXdbaV06PjEyLjZmfSB8IHtyYXRpbzo+OC40Zn1cIilcbnByaW50KClcbnByaW50KFwiQWRhbStMMiBkZWNheSB2YXJpZXMgMTAweCBhY3Jvc3MgcGFyYW1zOyBBZGFtVyBpcyB1bmlmb3JtLlwiKVxuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQWRhbVc6IERlY291cGxlZCBXZWlnaHQgRGVjYXkifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJBZGFtVyAoTG9zaGNoaWxvdiAmIEh1dHRlciAyMDE5KSBkZWNvdXBsZXMgd2VpZ2h0IGRlY2F5IGZyb20gdGhlIGFkYXB0aXZlIHVwZGF0ZTogKDEpIGNvbXB1dGUgZ3JhZGllbnQgZ190IHdpdGhvdXQgTDIgdGVybTsgKDIpIGNvbXB1dGUgbW9tZW50IGVzdGltYXRlcyBtX3QsIHZfdCBhbmQgYmlhcy1jb3JyZWN0ZWQgbV9oYXRfdCwgdl9oYXRfdDsgKDMpIGFwcGx5IHdlaWdodCBkZWNheSBkaXJlY3RseTogdGhldGFfdCA9IHRoZXRhX3t0LTF9KigxIC0gYWxwaGEqbGFtYmRhKSAtIGFscGhhKm1faGF0X3QvKHNxcnQodl9oYXRfdCkrZXBzKS4gVGhlIGRlY2F5IGFscGhhKmxhbWJkYSBpcyB1bmlmb3JtIGFjcm9zcyBhbGwgcGFyYW1ldGVycyByZWdhcmRsZXNzIG9mIGdyYWRpZW50IGhpc3RvcnkuIFdlaWdodCBkZWNheSBmb3IgdHJhbnNmb3JtZXJzOiBsYW1iZGE9MC4wMSAoQkVSVCksIGxhbWJkYT0wLjEgKEdQVC0yKSwgbGFtYmRhPTAuMDEtMC4xIChMTGFNQSkuIENyaXRpY2FsbHksIGVtYmVkZGluZ3MgYW5kIExheWVyTm9ybSBwYXJhbWV0ZXJzIGFyZSB0eXBpY2FsbHkgZXhjbHVkZWQgZnJvbSB3ZWlnaHQgZGVjYXkg4oCUIHRoZXkgaGF2ZSBubyBuYXR1cmFsIHNtYWxsLWlzLWJldHRlciBwcmlvciwgYW5kIHNocmlua2luZyB0aGVtIHRvd2FyZCB6ZXJvIGNhbiBkZXN0YWJpbGl6ZSBub3JtYWxpemF0aW9uLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgYWRhbXdfc3RlcCh0aGV0YSwgZywgbSwgdiwgdCwgbHI9MWUtMywgYjE9MC45LCBiMj0wLjk5OSwgZXBzPTFlLTgsIHdkPTAuMDEpOlxuICAgICMgU3RlcCAxOiBjb21wdXRlIGdyYWRpZW50IChubyBMMiB0ZXJtKVxuICAgIG0gPSBiMSAqIG0gKyAoMSAtIGIxKSAqIGdcbiAgICB2ID0gYjIgKiB2ICsgKDEgLSBiMikgKiBnICoqIDJcbiAgICBtX2hhdCA9IG0gLyAoMSAtIGIxICoqIHQpXG4gICAgdl9oYXQgPSB2IC8gKDEgLSBiMiAqKiB0KVxuICAgICMgU3RlcCAyOiBkZWNvdXBsZWQgd2VpZ2h0IGRlY2F5XG4gICAgdGhldGEgPSB0aGV0YSAqICgxIC0gbHIgKiB3ZClcbiAgICAjIFN0ZXAgMzogYWRhcHRpdmUgZ3JhZGllbnQgdXBkYXRlXG4gICAgdGhldGEgPSB0aGV0YSAtIGxyICogbV9oYXQgLyAobnAuc3FydCh2X2hhdCkgKyBlcHMpXG4gICAgcmV0dXJuIHRoZXRhLCBtLCB2XG5cbiMgVmVyaWZ5IGFnYWluc3QgdG9yY2gub3B0aW0uQWRhbVdcbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5tb2RlbF9wYXJhbSA9IHRvcmNoLm5uLlBhcmFtZXRlcih0b3JjaC50ZW5zb3IoWzIuMCwgLTEuNSwgMC44LCAtMC4zXSkpXG5vcHRpbWl6ZXIgPSB0b3JjaC5vcHRpbS5BZGFtVyhbbW9kZWxfcGFyYW1dLCBscj0xZS0zLCB3ZWlnaHRfZGVjYXk9MC4wMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBiZXRhcz0oMC45LCAwLjk5OSksIGVwcz0xZS04KVxuXG50aGV0YV9ucCA9IG5wLmFycmF5KFsyLjAsIC0xLjUsIDAuOCwgLTAuM10pXG5tID0gdiA9IG5wLnplcm9zKDQpXG5cbmZvciB0IGluIHJhbmdlKDEsIDExKTpcbiAgICBncmFkX25wID0gbnAuYXJyYXkoWzAuNSwgLTAuMywgMC4xLCAwLjhdKVxuICAgIGdyYWRfdCAgPSB0b3JjaC50ZW5zb3IoZ3JhZF9ucClcblxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgIG1vZGVsX3BhcmFtLmdyYWQgPSBncmFkX3QuY2xvbmUoKVxuICAgIG9wdGltaXplci5zdGVwKClcblxuICAgIHRoZXRhX25wLCBtLCB2ID0gYWRhbXdfc3RlcCh0aGV0YV9ucCwgZ3JhZF9ucCwgbSwgdiwgdClcblxucHJpbnQoXCJQeVRvcmNoIEFkYW1XIHZzIG51bXB5IEFkYW1XIGFmdGVyIDEwIHN0ZXBzOlwiKVxucHJpbnQoZlwiICBQeVRvcmNoOiB7bW9kZWxfcGFyYW0uZGF0YS5udW1weSgpLnJvdW5kKDYpfVwiKVxucHJpbnQoZlwiICBOdW1QeTogICB7dGhldGFfbnAucm91bmQoNil9XCIpXG5wcmludChmXCIgIE1heCBkaWZmOiB7bnAuYWJzKG1vZGVsX3BhcmFtLmRhdGEubnVtcHkoKSAtIHRoZXRhX25wKS5tYXgoKTouMmV9XCIpXG4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJXaGljaCBQYXJhbWV0ZXJzIEdldCBXZWlnaHQgRGVjYXk/In0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3RhbmRhcmQgcHJhY3RpY2U6IGFwcGx5IHdlaWdodCBkZWNheSB0byB3ZWlnaHQgbWF0cmljZXMgKDJEKyB0ZW5zb3JzKSBidXQgbm90IHRvIGJpYXNlcyBvciBub3JtYWxpemF0aW9uIHBhcmFtZXRlcnMgKExheWVyTm9ybSBnYW1tYSwgYmV0YTsgQmF0Y2hOb3JtIHNjYWxlLCBzaGlmdCkuIFJhdGlvbmFsZTogd2VpZ2h0IGRlY2F5IHNocmlua3Mgd2VpZ2h0cyB0b3dhcmQgemVybywgcmVndWxhcml6aW5nIHRoZSBmdW5jdGlvbiBieSByZWR1Y2luZyBpdHMgZWZmZWN0aXZlIG5vcm0uIEJpYXNlcyBhbmQgbm9ybWFsaXphdGlvbiBwYXJhbWV0ZXJzIGhhdmUgbm8gbmF0dXJhbCBzbWFsbC1pcy1iZXR0ZXIgcHJpb3Ig4oCUIHNocmlua2luZyBMYXllck5vcm0ncyBnYW1tYSB0b3dhcmQgemVybyB3b3VsZCBjb2xsYXBzZSBub3JtYWxpemF0aW9uLiBFeGNsdWRpbmcgdGhlbSBhdm9pZHMgbnVtZXJpY2FsIGlzc3VlcyB3aXRoIHZlcnkgc21hbGwgc2NhbGUgcGFyYW1ldGVycy4gSW4gY29kZTogY3JlYXRlIHR3byBwYXJhbWV0ZXIgZ3JvdXBzIOKAlCBvbmUgd2l0aCB3ZWlnaHRfZGVjYXkgZm9yIHdlaWdodCBtYXRyaWNlcywgb25lIHdpdGhvdXQgZm9yIGJpYXNlcyBhbmQgbm9ybWFsaXphdGlvbi4gVGhpcyBpcyB0aGUgc3RhbmRhcmQgcmVjaXBlIGluIEh1Z2dpbmcgRmFjZSB0cmFuc2Zvcm1lcnMgYW5kIGFsbCBtYWpvciBMTE0gdHJhaW5pbmcgZnJhbWV3b3JrcywgYW5kIGZhaWx1cmUgdG8gZG8gdGhpcyBjb3JyZWN0bHkgaXMgYSBjb21tb24gc291cmNlIG9mIHN1YnRsZSB0cmFpbmluZyBpbnN0YWJpbGl0eS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuIyBTdGFuZGFyZCB0cmFuc2Zvcm1lciBwYXJhbWV0ZXIgZ3JvdXBpbmcgZm9yIEFkYW1XXG5kZWYgZ2V0X3BhcmFtX2dyb3Vwcyhtb2RlbCwgd2VpZ2h0X2RlY2F5PTAuMDEpOlxuICAgIGRlY2F5X3BhcmFtcyAgICA9IFtdXG4gICAgbm9fZGVjYXlfcGFyYW1zID0gW11cbiAgICBmb3IgbmFtZSwgcGFyYW0gaW4gbW9kZWwubmFtZWRfcGFyYW1ldGVycygpOlxuICAgICAgICBpZiBub3QgcGFyYW0ucmVxdWlyZXNfZ3JhZDpcbiAgICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgICMgd2VpZ2h0IG1hdHJpY2VzICgyRCspIGdldCBkZWNheTsgYmlhc2VzIGFuZCBub3JtcyBkbyBub3RcbiAgICAgICAgaWYgcGFyYW0ubmRpbSA+PSAyIGFuZCAnd2VpZ2h0JyBpbiBuYW1lIGFuZCAnbm9ybScgbm90IGluIG5hbWU6XG4gICAgICAgICAgICBkZWNheV9wYXJhbXMuYXBwZW5kKHBhcmFtKVxuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgbm9fZGVjYXlfcGFyYW1zLmFwcGVuZChwYXJhbSlcbiAgICByZXR1cm4gW1xuICAgICAgICB7J3BhcmFtcyc6IGRlY2F5X3BhcmFtcywgICAgJ3dlaWdodF9kZWNheSc6IHdlaWdodF9kZWNheX0sXG4gICAgICAgIHsncGFyYW1zJzogbm9fZGVjYXlfcGFyYW1zLCAnd2VpZ2h0X2RlY2F5JzogMC4wfSxcbiAgICBdXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxubW9kZWwgPSBubi5TZXF1ZW50aWFsKFxuICAgIG5uLkxpbmVhcig2NCwgMTI4KSwgbm4uTGF5ZXJOb3JtKDEyOCksXG4gICAgbm4uTGluZWFyKDEyOCwgNjQpLCBubi5MYXllck5vcm0oNjQpLFxuICAgIG5uLkxpbmVhcig2NCwgMTApXG4pXG5ncm91cHMgPSBnZXRfcGFyYW1fZ3JvdXBzKG1vZGVsLCB3ZWlnaHRfZGVjYXk9MC4wMSlcbmRlY2F5X2NvdW50ICAgID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBncm91cHNbMF1bJ3BhcmFtcyddKVxubm9fZGVjYXlfY291bnQgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIGdyb3Vwc1sxXVsncGFyYW1zJ10pXG5wcmludChmXCJEZWNheSBwYXJhbXM6ICAgIHtkZWNheV9jb3VudDosfSAoe2xlbihncm91cHNbMF1bJ3BhcmFtcyddKX0gdGVuc29ycylcIilcbnByaW50KGZcIk5vLWRlY2F5IHBhcmFtczoge25vX2RlY2F5X2NvdW50Oix9ICh7bGVuKGdyb3Vwc1sxXVsncGFyYW1zJ10pfSB0ZW5zb3JzKVwiKVxub3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbVcoZ3JvdXBzLCBscj0zZS00KVxucHJpbnQoZlwiT3B0aW1pemVyOiB7b3B0aW1pemVyLl9fY2xhc3NfXy5fX25hbWVfX30gd2l0aCB7bGVuKGdyb3Vwcyl9IHBhcmFtZXRlciBncm91cHNcIilcbiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkxpb24gYW5kIEFkYUZhY3RvcjogQWx0ZXJuYXRpdmUgT3B0aW1pemVycyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlJlY2VudCBBZGFtVyBhbHRlcm5hdGl2ZXMgYWRkcmVzcyBtZW1vcnkgYW5kIGVmZmljaWVuY3kuIExpb24gKENoZW4gMjAyMykgdXNlcyBzaWduKGNfdCkgaW5zdGVhZCBvZiB0aGUgYWRhcHRpdmUgZGVub21pbmF0b3IsIHJlcXVpcmluZyBvbmx5IG9uZSBtb21lbnR1bSBidWZmZXIgdnMgQWRhbSdzIHR3byDigJQgMzMlIGxlc3Mgb3B0aW1pemVyIG1lbW9yeS4gQWRhRmFjdG9yIChTaGF6ZWVyIDIwMTgpIGZhY3Rvcml6ZXMgdGhlIHNlY29uZCBtb21lbnQgbWF0cml4OiBpbnN0ZWFkIG9mIHN0b3Jpbmcgdl9paiAob25lIHZhbHVlIHBlciB3ZWlnaHQpLCBzdG9yZXMgcm93IGFuZCBjb2x1bW4gc3VtcywgTyhuK20pIHZzIE8obiptKSDigJQgZW5hYmxpbmcgZnVsbC1wcmVjaXNpb24gdHJhaW5pbmcgb2YgMTBCKyBtb2RlbHMgb24gbGltaXRlZCBHUFUgbWVtb3J5LiBNdW9uIChLb3N0cmlrb3YgMjAyNCkgYXBwbGllcyBOZXN0ZXJvdiBtb21lbnR1bSBhbmQgdGhlbiBvcnRob2dvbmFsaXplcyB1cGRhdGVzIHVzaW5nIE5ld3Rvbi1TY2h1bHogaXRlcmF0aW9uIGZvciBtYXRyaXggcGFyYW1ldGVycywgYXJndWluZyB0aGF0IHVwZGF0ZXMgc2hvdWxkIHByZXNlcnZlIGVmZmVjdGl2ZSByYW5rLiBBbGwgc3VwcG9ydCBkZWNvdXBsZWQgd2VpZ2h0IGRlY2F5LiBBZGFtVyByZW1haW5zIHRoZSBkZWZhdWx0LCBidXQgTGlvbiBhbmQgQWRhRmFjdG9yIGFyZSBjb21wZWxsaW5nIHdoZW4gbWVtb3J5IGlzIHRoZSBiaW5kaW5nIGNvbnN0cmFpbnQuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTUwgQ29ubmVjdGlvbnM6IExMTSBUcmFpbmluZyBQcmFjdGljZSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkFkYW1XIHdpdGggY29zaW5lIExSIHNjaGVkdWxlIGlzIHRoZSBzdGFuZGFyZCBmb3IgcHJlLXRyYWluaW5nIExMTXMuIFR5cGljYWwgcmVjaXBlIGZvciBhIDdCIHBhcmFtZXRlciBtb2RlbDogYWxwaGE9M2UtNCwgYmV0YTE9MC45LCBiZXRhMj0wLjk1IChmYXN0ZXIgYWRhcHRhdGlvbiksIGVwcz0xZS04LCBsYW1iZGE9MC4xLCB3YXJtdXAgMTAwMCBzdGVwcywgY29zaW5lIGRlY2F5IHRvIDEwJSBvZiBwZWFrIExSLiBCZXRhMj0wLjk1IHJhdGhlciB0aGFuIDAuOTk5IGlzIGRlbGliZXJhdGU6IHdpdGggMC45OTksIHNlY29uZCBtb21lbnQgZXN0aW1hdGVzIHRha2UgfjEwMDAgc3RlcHMgdG8gd2FybSB1cDsgd2l0aCAwLjk1LCB0aGV5IHdhcm0gdXAgaW4gfjIwIHN0ZXBzIOKAlCBpbXBvcnRhbnQgZm9yIExMTXMgd2hlcmUgZ3JhZGllbnQgZGlzdHJpYnV0aW9uIHNoaWZ0cyBzaWduaWZpY2FudGx5IGR1cmluZyBlYXJseSB0cmFpbmluZyBvbiBkaXZlcnNlIGRhdGEuIFdlaWdodCBkZWNheSAwLjEgaXMgbGFyZ2VyIHRoYW4gdmlzaW9uIG1vZGVscyBiZWNhdXNlIG92ZXJwYXJhbWV0ZXJpemF0aW9uIGlzIG1vcmUgZXh0cmVtZSBpbiBMTE1zLiBUaGUgTWlzdHJhbCBhbmQgTExhTUEgdHJhaW5pbmcgcmVjaXBlcyBib3RoIHVzZSB0aGlzIGNvbmZpZ3VyYXRpb24gd2l0aCBtaW5vciB2YXJpYXRpb25zLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkltcGxlbWVudGF0aW9uIFBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiUGl0ZmFsbCAxOiBhcHBseWluZyB3ZWlnaHQgZGVjYXkgdG8gTGF5ZXJOb3JtIGFuZCBlbWJlZGRpbmcgcGFyYW1ldGVycyDigJQgTGF5ZXJOb3JtIGdhbW1hIGFuZCBiZXRhIG11c3QgaGF2ZSB3ZWlnaHRfZGVjYXk9MCB0byBhdm9pZCBjb2xsYXBzaW5nIG5vcm1hbGl6YXRpb24gc2NhbGUuIFBpdGZhbGwgMjogdXNpbmcgdG9yY2gub3B0aW0uQWRhbSB3aXRoIHdlaWdodF9kZWNheT0gaW5zdGVhZCBvZiBBZGFtVyDigJQgbWFueSB0dXRvcmlhbHMgc3RpbGwgZG8gdGhpcywgZ2l2aW5nIGNvcnJ1cHRlZCBMMiByZWd1bGFyaXphdGlvbi4gVXNlIHRvcmNoLm9wdGltLkFkYW1XIGFsd2F5cy4gUGl0ZmFsbCAzOiBub3QgYWNjb3VudGluZyBmb3IgTFIgc2NhbGluZyDigJQgZWZmZWN0aXZlIHdlaWdodCBkZWNheSBpcyBhbHBoYSpsYW1iZGEsIG5vdCBsYW1iZGEgYWxvbmUuIElmIGNvc2luZSBhbm5lYWxpbmcgaGFsdmVzIExSIGJ5IGVuZCBvZiB0cmFpbmluZywgZWZmZWN0aXZlIHdlaWdodCBkZWNheSBhbHNvIGhhbHZlcy4gSWYgY29uc3RhbnQgcmVndWxhcml6YXRpb24gc3RyZW5ndGggdGhyb3VnaG91dCB0cmFpbmluZyBpcyBkZXNpcmVkLCB0aGlzIG11c3QgYmUgZXhwbGljaXRseSBjb21wZW5zYXRlZCB3aXRoIGEgc2VwYXJhdGUgd2VpZ2h0IGRlY2F5IHNjaGVkdWxlIG9yIGJ5IHVzaW5nIGEgY29uc3RhbnQgTFIgd2l0aCBzdGVwLXdpc2Ugd2FybXVwLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlByYWN0aWNhbCBHdWlkYW5jZSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlVzZSBBZGFtVyBmb3IgYWxsIHRyYW5zZm9ybWVyIGFuZCBsYXJnZS1zY2FsZSBuZXVyYWwgbmV0d29yayB0cmFpbmluZy4gU3RhbmRhcmQgcGFyYW1ldGVyIGdyb3VwczogcGFyYW1zX2RlY2F5ID0gYWxsIHdlaWdodCBtYXRyaWNlcyAobmRpbSA+PSAyLCAnbm9ybScgbm90IGluIG5hbWUpLCBwYXJhbXNfbm9fZGVjYXkgPSBiaWFzZXMgYW5kIExheWVyTm9ybSBwYXJhbWV0ZXJzLiBXZWlnaHQgZGVjYXkgbGFtYmRhPTAuMDEgZm9yIHZpc2lvbiwgMC4xIGZvciBsYW5ndWFnZSBtb2RlbHMuIE1vbml0b3IgdGhlIHJhdGlvIG5vcm0oZGVsdGFfdGhldGEpL25vcm0odGhldGEpIHBlciBsYXllcjogc2hvdWxkIGJlIH4xZS0zIGZvciBoZWFsdGh5IHRyYWluaW5nLiBJZiB3ZWlnaHQgZGVjYXkgY2F1c2VzIHRoaXMgcmF0aW8gdG8gZHJvcCBiZWxvdyAxZS00IGZvciBzb21lIGxheWVycywgcmVkdWNlIGxhbWJkYSBvciBleGNsdWRlIHRob3NlIGxheWVycyBmcm9tIGRlY2F5LiBBbHdheXMgY2hlY2twb2ludCB0aGUgb3B0aW1pemVyIHN0YXRlIGFsb25nc2lkZSBtb2RlbCB3ZWlnaHRzIHRvIGNvcnJlY3RseSByZXN1bWUgdHJhaW5pbmcuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbiMgQWRhbVcgdHJhaW5pbmcgbG9vcCBtb25pdG9yaW5nIHVwZGF0ZS10by13ZWlnaHQgcmF0aW8gcGVyIGxheWVyXG50b3JjaC5tYW51YWxfc2VlZCg0MilcblxuZGVmIGdldF9wYXJhbV9ncm91cHMobW9kZWwsIHdkPTAuMSk6XG4gICAgZGVjYXksIG5vX2RlY2F5ID0gW10sIFtdXG4gICAgZm9yIG5hbWUsIHAgaW4gbW9kZWwubmFtZWRfcGFyYW1ldGVycygpOlxuICAgICAgICBpZiBwLnJlcXVpcmVzX2dyYWQ6XG4gICAgICAgICAgICAobm9fZGVjYXkgaWYgKHAubmRpbSA8IDIgb3IgJ25vcm0nIGluIG5hbWUpIGVsc2UgZGVjYXkpLmFwcGVuZChwKVxuICAgIHJldHVybiBbeydwYXJhbXMnOiBkZWNheSwgJ3dlaWdodF9kZWNheSc6IHdkfSxcbiAgICAgICAgICAgIHsncGFyYW1zJzogbm9fZGVjYXksICd3ZWlnaHRfZGVjYXknOiAwLjB9XVxuXG5tb2RlbCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uTGluZWFyKDMyLCA2NCksIG5uLkxheWVyTm9ybSg2NCksIG5uLlJlTFUoKSxcbiAgICBubi5MaW5lYXIoNjQsIDEwKVxuKVxub3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbVcoZ2V0X3BhcmFtX2dyb3Vwcyhtb2RlbCwgd2Q9MC4xKSwgbHI9M2UtNClcbnNjaGVkdWxlciA9IHRvcmNoLm9wdGltLmxyX3NjaGVkdWxlci5Db3NpbmVBbm5lYWxpbmdMUihvcHRpbWl6ZXIsIFRfbWF4PTEwMClcblxueCA9IHRvcmNoLnJhbmRuKDE2LCAzMilcbnkgPSB0b3JjaC5yYW5kaW50KDAsIDEwLCAoMTYsKSlcblxuZm9yIHN0ZXAgaW4gcmFuZ2UoMjApOlxuICAgIG9sZF9wYXJhbXMgPSB7bjogcC5kZXRhY2goKS5jbG9uZSgpIGZvciBuLCBwIGluIG1vZGVsLm5hbWVkX3BhcmFtZXRlcnMoKX1cbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpKG1vZGVsKHgpLCB5KVxuICAgIGxvc3MuYmFja3dhcmQoKVxuICAgIHRvcmNoLm5uLnV0aWxzLmNsaXBfZ3JhZF9ub3JtXyhtb2RlbC5wYXJhbWV0ZXJzKCksIDEuMClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgc2NoZWR1bGVyLnN0ZXAoKVxuXG4jIE1vbml0b3IgdXBkYXRlLXRvLXdlaWdodCByYXRpbyAoc2hvdWxkIGJlIH4xZS0zIGZvciBoZWFsdGh5IHRyYWluaW5nKVxucHJpbnQoXCJVcGRhdGUtdG8td2VpZ2h0IHJhdGlvIHBlciBsYXllcjpcIilcbmZvciBuYW1lLCBwIGluIG1vZGVsLm5hbWVkX3BhcmFtZXRlcnMoKTpcbiAgICBpZiBwLnJlcXVpcmVzX2dyYWQgYW5kIG9sZF9wYXJhbXNbbmFtZV0ubm9ybSgpID4gMDpcbiAgICAgICAgcmF0aW8gPSAocC5kZXRhY2goKSAtIG9sZF9wYXJhbXNbbmFtZV0pLm5vcm0oKSAvIG9sZF9wYXJhbXNbbmFtZV0ubm9ybSgpXG4gICAgICAgIHByaW50KGZcIiAge25hbWU6MzBzfToge3JhdGlvLml0ZW0oKTouMmV9XCIpXG4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidGl0bGUiOiAiRWZmZWN0aXZlIFdlaWdodCBEZWNheSBTY2FsZXMgd2l0aCBMZWFybmluZyBSYXRlIiwgImNvbnRlbnQiOiAiQWRhbVcgdXBkYXRlOiB0aGV0YSA8LSB0aGV0YSooMSAtIGFscGhhKmxhbWJkYSkgLSBhZGFwdGl2ZV91cGRhdGUuIFRoZSBlZmZlY3RpdmUgZGVjYXkgcmF0ZSBpcyBhbHBoYSpsYW1iZGEsIG5vdCBsYW1iZGEgYWxvbmUuIFdoZW4gdXNpbmcgY29zaW5lIGFubmVhbGluZyB0aGF0IHJlZHVjZXMgYWxwaGEgYnkgMTB4LCBlZmZlY3RpdmUgd2VpZ2h0IGRlY2F5IGFsc28gZmFsbHMgMTB4LiBJZiBjb25zaXN0ZW50IHJlZ3VsYXJpemF0aW9uIHRocm91Z2hvdXQgdHJhaW5pbmcgaXMgZGVzaXJlZCwgeW91IG11c3QgYWNjb3VudCBmb3IgdGhpczogZWl0aGVyIHVzZSBhIGNvbnN0YW50IExSIHdpdGggc3RlcCBkZWNheSwgb3IgaW1wbGVtZW50IGEgc2VwYXJhdGUgd2VpZ2h0X2RlY2F5IHNjaGVkdWxlIHRoYXQgY29tcGVuc2F0ZXMgZm9yIExSIGNoYW5nZXMuIFNvbWUgZnJhbWV3b3JrcyBpbXBsZW1lbnQgYSBub3JtYWxpemVkIHdlaWdodCBkZWNheTogbGFtYmRhX2VmZiA9IGxhbWJkYSAvIHNxcnQoVCkgd2hlcmUgVCBpcyB0cmFpbmluZyBzdGVwcy4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIk9wdGltaXplciIsICJMMiBSZWd1bGFyaXphdGlvbiIsICJNZW1vcnkiLCAiQ29udmVyZ2VuY2UiLCAiQmVzdCBVc2UgQ2FzZSJdLCAicm93cyI6IFtbIlNHRCtMMiIsICJDb3JyZWN0IHVuaWZvcm0gZGVjYXkiLCAiMSBidWZmZXIvcGFyYW0iLCAiTyhrYXBwYSkgc3RlcHMiLCAiQ29udmV4LCBpbWFnZSBjbGFzc2lmaWNhdGlvbiJdLCBbIkFkYW0rTDIiLCAiQ29ycnVwdGVkICh2YXJpZXMgcGVyIHBhcmFtKSIsICIyIGJ1ZmZlcnMvcGFyYW0iLCAiRmFzdCAoYWRhcHRpdmUpIiwgIkF2b2lkIGZvciByZWd1bGFyaXplZCB0cmFpbmluZyJdLCBbIkFkYW1XIiwgIkNvcnJlY3QgZGVjb3VwbGVkIGRlY2F5IiwgIjIgYnVmZmVycy9wYXJhbSIsICJGYXN0IChhZGFwdGl2ZSkiLCAiU3RhbmRhcmQgZm9yIExMTXMsIHRyYW5zZm9ybWVycyJdLCBbIkFkYUZhY3RvcitXRCIsICJDb3JyZWN0IGRlY291cGxlZCBkZWNheSIsICJPKG4rbSkgZmFjdG9yZWQiLCAiU2ltaWxhciB0byBBZGFtVyIsICJNZW1vcnktY29uc3RyYWluZWQgTExNIHRyYWluaW5nIl0sIFsiTGlvbitXRCIsICJDb3JyZWN0IGRlY291cGxlZCBkZWNheSIsICIxIGJ1ZmZlci9wYXJhbSIsICJDb21wYXJhYmxlIHRvIEFkYW1XIiwgIk1lbW9yeS1lZmZpY2llbnQgTExNIHRyYWluaW5nIl1dfSwgeyJ0eXBlIjogImRpdmlkZXIifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJLZXkgVGFrZWF3YXlzIn0sIHsidHlwZSI6ICJsaXN0IiwgIml0ZW1zIjogWyJBZGFtK0wyIGNvcnJ1cHRzIHJlZ3VsYXJpemF0aW9uOiB0aGUgYWRhcHRpdmUgZGVub21pbmF0b3IgbWFrZXMgZWZmZWN0aXZlIHdlaWdodCBkZWNheSBub24tdW5pZm9ybSwgdmFyeWluZyBpbnZlcnNlbHkgd2l0aCBncmFkaWVudCBoaXN0b3J5LiIsICJBZGFtVyBkZWNvdXBsZXMgd2VpZ2h0IGRlY2F5OiBhcHBseSB0aGV0YSooMS1hbHBoYSpsYW1iZGEpIGJlZm9yZSB0aGUgYWRhcHRpdmUgdXBkYXRlLCBnaXZpbmcgdW5pZm9ybSBzaHJpbmthZ2UgYWNyb3NzIGFsbCBwYXJhbWV0ZXJzLiIsICJBbHdheXMgZXhjbHVkZSBiaWFzZXMgYW5kIExheWVyTm9ybSBwYXJhbWV0ZXJzIGZyb20gd2VpZ2h0IGRlY2F5IOKAlCB0d28gcGFyYW1ldGVyIGdyb3VwcyBhcmUgcmVxdWlyZWQgaW4gYW55IHRyYW5zZm9ybWVyIHRyYWluaW5nIHJlY2lwZS4iLCAiTExNIHN0YW5kYXJkOiBBZGFtVyB3aXRoIGJldGEyPTAuOTUsIHdlaWdodF9kZWNheT0wLjEsIHdhcm11cCAxMDAwIHN0ZXBzLCBjb3NpbmUgZGVjYXkg4oCUIG5vdCBiZXRhMj0wLjk5OSBhbmQgbm90IEFkYW0uIiwgIkVmZmVjdGl2ZSB3ZWlnaHQgZGVjYXkgPSBhbHBoYSpsYW1iZGE7IGFzIExSIGRlY2F5cyB2aWEgY29zaW5lIGFubmVhbGluZywgZWZmZWN0aXZlIHJlZ3VsYXJpemF0aW9uIHdlYWtlbnMgY29ycmVzcG9uZGluZ2x5LiIsICJNb25pdG9yIHVwZGF0ZS10by13ZWlnaHQgcmF0aW8gbm9ybShkZWx0YV90aGV0YSkvbm9ybSh0aGV0YSkgfjFlLTMgcGVyIGxheWVyIHRvIHZlcmlmeSBoZWFsdGh5IHRyYWluaW5nIGR5bmFtaWNzLiJdfV0="
---

# AdamW — Decoupled Weight Decay

Standard Adam with L2 regularization silently corrupts the regularization: the adaptive denominator sqrt(v_hat) scales each parameter's gradient differently, meaning L2 weight decay is applied non-uniformly — exactly the opposite of its intent. AdamW (Loshchilov & Hutter 2019) fixes this by decoupling weight decay from the gradient update. This insight makes AdamW the standard optimizer for training GPT, BERT, LLaMA, and virtually every large-scale language model. Understanding why Adam+L2 fails — and how AdamW fixes it — is essential for any practitioner training transformers at scale.

## The Problem: Adaptive Rates Corrupt L2 Regularization

In vanilla SGD: L2 means adding lambda*theta to gradient, so effective update is theta <- theta*(1-eta*lambda) - eta*g. The L2 decay eta*lambda is applied uniformly across all parameters. In Adam: the effective gradient is g_eff = g + lambda*theta, which is then divided by sqrt(v_hat)+eps. The effective decay per parameter becomes eta*lambda*theta_i/(sqrt(v_hat_i)+eps) — it varies with gradient history. Parameters with large gradient history (large v_i) receive weaker L2 regularization. Parameters updated rarely (small v_i) receive stronger L2. This is the opposite of what L2 intends: it should penalize large weights uniformly, regardless of gradient history. The corruption is worst when gradient magnitudes vary widely across parameters — exactly the case in transformers.

```python
import numpy as np

# Show effective L2 decay per parameter for Adam+L2 vs AdamW
np.random.seed(42)
n_params = 6
lam = 0.01
lr = 1e-3

# Simulate diverse gradient histories
theta = np.ones(n_params) * 2.0
v_hat = np.array([1e-4, 1e-3, 0.01, 0.1, 1.0, 10.0])  # range of second moments
eps = 1e-8

# Adam+L2: effective decay = lr * lam / (sqrt(v_hat) + eps)
g = np.ones(n_params) * 0.5   # uniform gradient
g_l2 = g + lam * theta         # L2 adds lambda*theta to gradient
eff_decay_adam = lr * lam * theta / (np.sqrt(v_hat) + eps)

# AdamW: effective decay = lr * lam (uniform)
eff_decay_adamw = np.full(n_params, lr * lam * theta[0])

print(f"{'v_hat':>10} | {'Adam+L2 decay':>15} | {'AdamW decay':>12} | {'ratio':>8}")
print("-" * 55)
for i in range(n_params):
    ratio = eff_decay_adam[i] / eff_decay_adamw[i]
    print(f"{v_hat[i]:>10.4f} | {eff_decay_adam[i]:>15.6f} | {eff_decay_adamw[i]:>12.6f} | {ratio:>8.4f}")
print()
print("Adam+L2 decay varies 100x across params; AdamW is uniform.")

```

## AdamW: Decoupled Weight Decay

AdamW (Loshchilov & Hutter 2019) decouples weight decay from the adaptive update: (1) compute gradient g_t without L2 term; (2) compute moment estimates m_t, v_t and bias-corrected m_hat_t, v_hat_t; (3) apply weight decay directly: theta_t = theta_{t-1}*(1 - alpha*lambda) - alpha*m_hat_t/(sqrt(v_hat_t)+eps). The decay alpha*lambda is uniform across all parameters regardless of gradient history. Weight decay for transformers: lambda=0.01 (BERT), lambda=0.1 (GPT-2), lambda=0.01-0.1 (LLaMA). Critically, embeddings and LayerNorm parameters are typically excluded from weight decay — they have no natural small-is-better prior, and shrinking them toward zero can destabilize normalization.

```python
import torch
import numpy as np

def adamw_step(theta, g, m, v, t, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8, wd=0.01):
    # Step 1: compute gradient (no L2 term)
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    m_hat = m / (1 - b1 ** t)
    v_hat = v / (1 - b2 ** t)
    # Step 2: decoupled weight decay
    theta = theta * (1 - lr * wd)
    # Step 3: adaptive gradient update
    theta = theta - lr * m_hat / (np.sqrt(v_hat) + eps)
    return theta, m, v

# Verify against torch.optim.AdamW
torch.manual_seed(0)
model_param = torch.nn.Parameter(torch.tensor([2.0, -1.5, 0.8, -0.3]))
optimizer = torch.optim.AdamW([model_param], lr=1e-3, weight_decay=0.01,
                               betas=(0.9, 0.999), eps=1e-8)

theta_np = np.array([2.0, -1.5, 0.8, -0.3])
m = v = np.zeros(4)

for t in range(1, 11):
    grad_np = np.array([0.5, -0.3, 0.1, 0.8])
    grad_t  = torch.tensor(grad_np)

    optimizer.zero_grad()
    model_param.grad = grad_t.clone()
    optimizer.step()

    theta_np, m, v = adamw_step(theta_np, grad_np, m, v, t)

print("PyTorch AdamW vs numpy AdamW after 10 steps:")
print(f"  PyTorch: {model_param.data.numpy().round(6)}")
print(f"  NumPy:   {theta_np.round(6)}")
print(f"  Max diff: {np.abs(model_param.data.numpy() - theta_np).max():.2e}")

```

## Which Parameters Get Weight Decay?

Standard practice: apply weight decay to weight matrices (2D+ tensors) but not to biases or normalization parameters (LayerNorm gamma, beta; BatchNorm scale, shift). Rationale: weight decay shrinks weights toward zero, regularizing the function by reducing its effective norm. Biases and normalization parameters have no natural small-is-better prior — shrinking LayerNorm's gamma toward zero would collapse normalization. Excluding them avoids numerical issues with very small scale parameters. In code: create two parameter groups — one with weight_decay for weight matrices, one without for biases and normalization. This is the standard recipe in Hugging Face transformers and all major LLM training frameworks, and failure to do this correctly is a common source of subtle training instability.

```python
import torch
import torch.nn as nn

# Standard transformer parameter grouping for AdamW
def get_param_groups(model, weight_decay=0.01):
    decay_params    = []
    no_decay_params = []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        # weight matrices (2D+) get decay; biases and norms do not
        if param.ndim >= 2 and 'weight' in name and 'norm' not in name:
            decay_params.append(param)
        else:
            no_decay_params.append(param)
    return [
        {'params': decay_params,    'weight_decay': weight_decay},
        {'params': no_decay_params, 'weight_decay': 0.0},
    ]

torch.manual_seed(42)
model = nn.Sequential(
    nn.Linear(64, 128), nn.LayerNorm(128),
    nn.Linear(128, 64), nn.LayerNorm(64),
    nn.Linear(64, 10)
)
groups = get_param_groups(model, weight_decay=0.01)
decay_count    = sum(p.numel() for p in groups[0]['params'])
no_decay_count = sum(p.numel() for p in groups[1]['params'])
print(f"Decay params:    {decay_count:,} ({len(groups[0]['params'])} tensors)")
print(f"No-decay params: {no_decay_count:,} ({len(groups[1]['params'])} tensors)")
optimizer = torch.optim.AdamW(groups, lr=3e-4)
print(f"Optimizer: {optimizer.__class__.__name__} with {len(groups)} parameter groups")

```

## Lion and AdaFactor: Alternative Optimizers

Recent AdamW alternatives address memory and efficiency. Lion (Chen 2023) uses sign(c_t) instead of the adaptive denominator, requiring only one momentum buffer vs Adam's two — 33% less optimizer memory. AdaFactor (Shazeer 2018) factorizes the second moment matrix: instead of storing v_ij (one value per weight), stores row and column sums, O(n+m) vs O(n*m) — enabling full-precision training of 10B+ models on limited GPU memory. Muon (Kostrikov 2024) applies Nesterov momentum and then orthogonalizes updates using Newton-Schulz iteration for matrix parameters, arguing that updates should preserve effective rank. All support decoupled weight decay. AdamW remains the default, but Lion and AdaFactor are compelling when memory is the binding constraint.

## ML Connections: LLM Training Practice

AdamW with cosine LR schedule is the standard for pre-training LLMs. Typical recipe for a 7B parameter model: alpha=3e-4, beta1=0.9, beta2=0.95 (faster adaptation), eps=1e-8, lambda=0.1, warmup 1000 steps, cosine decay to 10% of peak LR. Beta2=0.95 rather than 0.999 is deliberate: with 0.999, second moment estimates take ~1000 steps to warm up; with 0.95, they warm up in ~20 steps — important for LLMs where gradient distribution shifts significantly during early training on diverse data. Weight decay 0.1 is larger than vision models because overparameterization is more extreme in LLMs. The Mistral and LLaMA training recipes both use this configuration with minor variations.

## Implementation Pitfalls

Pitfall 1: applying weight decay to LayerNorm and embedding parameters — LayerNorm gamma and beta must have weight_decay=0 to avoid collapsing normalization scale. Pitfall 2: using torch.optim.Adam with weight_decay= instead of AdamW — many tutorials still do this, giving corrupted L2 regularization. Use torch.optim.AdamW always. Pitfall 3: not accounting for LR scaling — effective weight decay is alpha*lambda, not lambda alone. If cosine annealing halves LR by end of training, effective weight decay also halves. If constant regularization strength throughout training is desired, this must be explicitly compensated with a separate weight decay schedule or by using a constant LR with step-wise warmup.

## Practical Guidance

Use AdamW for all transformer and large-scale neural network training. Standard parameter groups: params_decay = all weight matrices (ndim >= 2, 'norm' not in name), params_no_decay = biases and LayerNorm parameters. Weight decay lambda=0.01 for vision, 0.1 for language models. Monitor the ratio norm(delta_theta)/norm(theta) per layer: should be ~1e-3 for healthy training. If weight decay causes this ratio to drop below 1e-4 for some layers, reduce lambda or exclude those layers from decay. Always checkpoint the optimizer state alongside model weights to correctly resume training.

```python
import torch
import torch.nn as nn

# AdamW training loop monitoring update-to-weight ratio per layer
torch.manual_seed(42)

def get_param_groups(model, wd=0.1):
    decay, no_decay = [], []
    for name, p in model.named_parameters():
        if p.requires_grad:
            (no_decay if (p.ndim < 2 or 'norm' in name) else decay).append(p)
    return [{'params': decay, 'weight_decay': wd},
            {'params': no_decay, 'weight_decay': 0.0}]

model = nn.Sequential(
    nn.Linear(32, 64), nn.LayerNorm(64), nn.ReLU(),
    nn.Linear(64, 10)
)
optimizer = torch.optim.AdamW(get_param_groups(model, wd=0.1), lr=3e-4)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)

x = torch.randn(16, 32)
y = torch.randint(0, 10, (16,))

for step in range(20):
    old_params = {n: p.detach().clone() for n, p in model.named_parameters()}
    optimizer.zero_grad()
    loss = nn.CrossEntropyLoss()(model(x), y)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()
    scheduler.step()

# Monitor update-to-weight ratio (should be ~1e-3 for healthy training)
print("Update-to-weight ratio per layer:")
for name, p in model.named_parameters():
    if p.requires_grad and old_params[name].norm() > 0:
        ratio = (p.detach() - old_params[name]).norm() / old_params[name].norm()
        print(f"  {name:30s}: {ratio.item():.2e}")

```

> **Effective Weight Decay Scales with Learning Rate**: AdamW update: theta <- theta*(1 - alpha*lambda) - adaptive_update. The effective decay rate is alpha*lambda, not lambda alone. When using cosine annealing that reduces alpha by 10x, effective weight decay also falls 10x. If consistent regularization throughout training is desired, you must account for this: either use a constant LR with step decay, or implement a separate weight_decay schedule that compensates for LR changes. Some frameworks implement a normalized weight decay: lambda_eff = lambda / sqrt(T) where T is training steps.

| Optimizer | L2 Regularization | Memory | Convergence | Best Use Case |
|---|---|---|---|---|
| SGD+L2 | Correct uniform decay | 1 buffer/param | O(kappa) steps | Convex, image classification |
| Adam+L2 | Corrupted (varies per param) | 2 buffers/param | Fast (adaptive) | Avoid for regularized training |
| AdamW | Correct decoupled decay | 2 buffers/param | Fast (adaptive) | Standard for LLMs, transformers |
| AdaFactor+WD | Correct decoupled decay | O(n+m) factored | Similar to AdamW | Memory-constrained LLM training |
| Lion+WD | Correct decoupled decay | 1 buffer/param | Comparable to AdamW | Memory-efficient LLM training |

---

## Key Takeaways

- Adam+L2 corrupts regularization: the adaptive denominator makes effective weight decay non-uniform, varying inversely with gradient history.
- AdamW decouples weight decay: apply theta*(1-alpha*lambda) before the adaptive update, giving uniform shrinkage across all parameters.
- Always exclude biases and LayerNorm parameters from weight decay — two parameter groups are required in any transformer training recipe.
- LLM standard: AdamW with beta2=0.95, weight_decay=0.1, warmup 1000 steps, cosine decay — not beta2=0.999 and not Adam.
- Effective weight decay = alpha*lambda; as LR decays via cosine annealing, effective regularization weakens correspondingly.
- Monitor update-to-weight ratio norm(delta_theta)/norm(theta) ~1e-3 per layer to verify healthy training dynamics.

