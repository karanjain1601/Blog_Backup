---
title: "Machine Epsilon and Floating-Point Precision"
slug: "machine-epsilon"
description: "Machine epsilon definition, the relative error model, float equality pitfalls, Kahan compensated summation, and how floating-point precision constrains gradient computation in mixed-precision ML training."
tags: ["numerical-methods", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTWFjaGluZSBlcHNpbG9uIGlzIHRoZSBmdW5kYW1lbnRhbCBwcmVjaXNpb24gbGltaXQgb2YgZmxvYXRpbmctcG9pbnQgYXJpdGhtZXRpYy4gSXQgZGV0ZXJtaW5lcyB0aGUgc21hbGxlc3QgcmVsYXRpdmUgZGlmZmVyZW5jZSB0aGF0IGNhbiBiZSBkaXN0aW5ndWlzaGVkIGZyb20gemVybywgc2V0cyB0aGUgZmxvb3IgZm9yIG51bWVyaWNhbCBkaWZmZXJlbnRpYXRpb24gc3RlcCBzaXplcywgYW5kIHF1YW50aWZpZXMgdGhlIHByZWNpc2lvbiBvZiBncmFkaWVudCBjb21wdXRhdGlvbnMgYWNyb3NzIGV2ZXJ5IGxheWVyIG9mIGEgZGVlcCBuZXR3b3JrLiBVbmRlcnN0YW5kaW5nIG1hY2hpbmUgZXBzaWxvbiBpcyBlc3NlbnRpYWwgZm9yIGRpYWdub3NpbmcgbnVtZXJpY2FsIGluc3RhYmlsaXRpZXMsIGNob29zaW5nIGNvbnZlcmdlbmNlIHRvbGVyYW5jZXMsIGFuZCByZWFzb25pbmcgYWJvdXQgd2hpY2ggb3BlcmF0aW9ucyBjYW4gc2FmZWx5IHJ1biBpbiBiZjE2IHZlcnN1cyB0aG9zZSB0aGF0IHJlcXVpcmUgZnAzMi4gRXZlcnkgcHJhY3RpdGlvbmVyIGJ1aWxkaW5nIGF0IHNjYWxlIHdpbGwgZXZlbnR1YWxseSBoaXQgYSB3YWxsIGNhdXNlZCBieSBpbnN1ZmZpY2llbnQgbnVtZXJpY2FsIHByZWNpc2lvbiDigJQgdW5kZXJzdGFuZGluZyBlcHNpbG9uIGlzIHRoZSBzdGFydGluZyBwb2ludCBmb3IgZGVidWdnaW5nIHN1Y2ggZmFpbHVyZXMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29yZSBEZWZpbml0aW9uIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTWFjaGluZSBlcHNpbG9uICjOtV9tYWNoKSBpcyB0aGUgc21hbGxlc3QgcG9zaXRpdmUgZmxvYXRpbmctcG9pbnQgbnVtYmVyIM61IHN1Y2ggdGhhdCBmbCgxICsgzrUpID4gMSDigJQgZXF1aXZhbGVudGx5LCB0aGUgc3BhY2luZyBiZXR3ZWVuIDEuMCBhbmQgdGhlIG5leHQgcmVwcmVzZW50YWJsZSBudW1iZXIuIEZvciBhIGZvcm1hdCB3aXRoIG0gbWFudGlzc2EgYml0czpcblxuzrVfbWFjaCA9IDJee+KIkm19XG5cblZhbHVlcyBieSBmb3JtYXQ6XG4tIGZwNjQgKGRvdWJsZSk6IM61ID0gMl574oiSNTJ9IOKJiCAyLjIyw5cxMOKBu8K54oG2ICAoNTMgc2lnbmlmaWNhbnQgYml0cylcbi0gZnAzMiAoZmxvYXQpOiAgzrUgPSAyXnviiJIyM30g4omIIDEuMTnDlzEw4oG74oG3ICAoMjQgc2lnbmlmaWNhbnQgYml0cylcbi0gZnAxNiAoaGFsZik6ICAgzrUgPSAyXnviiJIxMH0g4omIIDkuNzfDlzEw4oG74oG0ICAoMTEgc2lnbmlmaWNhbnQgYml0cylcbi0gYmYxNjogICAgICAgICAgzrUgPSAyXnviiJI3fSAg4omIIDcuODHDlzEw4oG7wrMgICg4IHNpZ25pZmljYW50IGJpdHMpXG5cblRoZSB1bml0IHJvdW5kb2ZmIGlzIM61X21hY2gvMiDigJQgdGhlIG1heGltdW0gcmVsYXRpdmUgcm91bmRpbmcgZXJyb3IgZm9yIGFueSBzaW5nbGUgSUVFRSA3NTQgb3BlcmF0aW9uLiBDcnVjaWFsbHksIGZsb2F0aW5nLXBvaW50IG51bWJlcnMgYXJlIG5vdCB1bmlmb3JtbHkgc3BhY2VkOiB0aGV5IGFyZSBkZW5zZXIgbmVhciB6ZXJvIGFuZCBzcGFyc2VyIGZvciBsYXJnZSBtYWduaXR1ZGVzLiBGb3IgYSB2YWx1ZSB4LCB0aGUgYWJzb2x1dGUgc3BhY2luZyBpcyBhcHByb3hpbWF0ZWx5IHx4fCDDlyDOtV9tYWNoLCBzbyBwcmVjaXNpb24gaXMgYWx3YXlzIG1lYXN1cmVkIGluIHJlbGF0aXZlIHRlcm1zLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuXG4jIE1hY2hpbmUgZXBzaWxvbiBmcm9tIG51bXB5IGZpbmZvXG5wcmludChcIj09PSBmaW5mbyB2YWx1ZXMgPT09XCIpXG5mb3IgZHR5cGUgaW4gW25wLmZsb2F0MTYsIG5wLmZsb2F0MzIsIG5wLmZsb2F0NjRdOlxuICAgIGluZm8gPSBucC5maW5mbyhkdHlwZSlcbiAgICBwcmludChmXCJ7ZHR5cGUuX19uYW1lX186MTBzfTogZXBzPXtpbmZvLmVwczouM2V9ICB0aW55PXtpbmZvLnRpbnk6LjNlfSAgbWF4PXtpbmZvLm1heDouM2V9XCIpXG5cbiMgYmZsb2F0MTYgaXMgdG9yY2gtb25seVxucHJpbnQoKVxuZm9yIGR0eXBlIGluIFt0b3JjaC5mbG9hdDE2LCB0b3JjaC5iZmxvYXQxNiwgdG9yY2guZmxvYXQzMiwgdG9yY2guZmxvYXQ2NF06XG4gICAgaW5mbyA9IHRvcmNoLmZpbmZvKGR0eXBlKVxuICAgIHByaW50KGZcIntzdHIoZHR5cGUpOjIwc306IGVwcz17aW5mby5lcHM6LjNlfSAgYml0cz17aW5mby5iaXRzfVwiKVxuXG4jIEVtcGlyaWNhbGx5IGNvbXB1dGUgZnAzMiBlcHNpbG9uXG5wcmludChcIlxcbj09PSBFbXBpcmljYWwgZnAzMiBlcHNpbG9uID09PVwiKVxuZXBzID0gbnAuZmxvYXQzMigxLjApXG53aGlsZSBucC5mbG9hdDMyKDEuMCkgKyBlcHMgLyBucC5mbG9hdDMyKDIuMCkgPiBucC5mbG9hdDMyKDEuMCk6XG4gICAgZXBzID0gZXBzIC8gbnAuZmxvYXQzMigyLjApXG5wcmludChmXCJFbXBpcmljYWwgZnAzMiBlcHMgPSB7ZXBzICogMjouNmV9ICAobnAuZmluZm8gPSB7bnAuZmluZm8obnAuZmxvYXQzMikuZXBzOi42ZX0pXCIpXG5cbiMgTm9uLXVuaWZvcm0gc3BhY2luZzogYWJzb2x1dGUgcHJlY2lzaW9uIGRlcGVuZHMgb24gbWFnbml0dWRlXG5wcmludChcIlxcbj09PSBTcGFjaW5nIGF0IERpZmZlcmVudCBNYWduaXR1ZGVzIChmcDMyKSA9PT1cIilcbmZvciB4X3ZhbCBpbiBbMC41LCAxLjAsIDE2LjAsIDEwMjQuMCwgMWU2XTpcbiAgICB4ID0gbnAuZmxvYXQzMih4X3ZhbClcbiAgICBueHQgPSBucC5uZXh0YWZ0ZXIoeCwgbnAuZmxvYXQzMihucC5pbmYpKVxuICAgIHNwYWNpbmcgPSBmbG9hdChueHQgLSB4KVxuICAgIHByaW50KGZcIiAgeD17eF92YWw6PjEwZ306IGFic19zcGFjaW5nPXtzcGFjaW5nOi4zZX0gIHJlbF9zcGFjaW5nPXtzcGFjaW5nL3hfdmFsOi4zZX1cIilcbiMgT2JzZXJ2YXRpb246IHJlbGF0aXZlIHNwYWNpbmcgfmNvbnN0YW50IChlcHNfbWFjaCksIGFic29sdXRlIHNwYWNpbmcgZ3Jvd3Mgd2l0aCB4In0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiVGhlIFJlbGF0aXZlIEVycm9yIE1vZGVsIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIElFRUUgNzU0IHN0YW5kYXJkIGd1YXJhbnRlZXMgdGhhdCBldmVyeSBjb3JyZWN0bHktcm91bmRlZCBvcGVyYXRpb24gc2F0aXNmaWVzOlxuXG5mbChhIOKImCBiKSA9IChhIOKImCBiKSgxICsgzrQpLCAgfM60fCDiiaQgzrVfbWFjaC8yXG5cblRoaXMgaG9sZHMgZm9yIGFkZGl0aW9uLCBzdWJ0cmFjdGlvbiwgbXVsdGlwbGljYXRpb24sIGRpdmlzaW9uLCBhbmQgc3F1YXJlIHJvb3QuIEl0IG1lYW5zIGV2ZXJ5IHNpbmdsZSBmbG9hdGluZy1wb2ludCBvcGVyYXRpb24gaW50cm9kdWNlcyByZWxhdGl2ZSBlcnJvciBhdCBtb3N0IM61X21hY2gvMi4gRm9yIGEgY29tcHV0YXRpb24gaW52b2x2aW5nIE4gb3BlcmF0aW9ucywgYWNjdW11bGF0ZWQgZXJyb3IgaXMgYXQgbW9zdCBOIMOXIM61X21hY2gvMiBpbiB0aGUgd29yc3QgY2FzZSAoYWxsIGVycm9ycyBjb25zdHJ1Y3RpdmVseSByZWluZm9yY2UpLCB0aG91Z2ggaW4gcHJhY3RpY2UgcmFuZG9tIGNhbmNlbGxhdGlvbiByZWR1Y2VzIHRoaXMgdG8gcm91Z2hseSDiiJpOIMOXIM61X21hY2gvMi5cblxuSW1wbGljYXRpb24gZm9yIGdyYWRpZW50IGNvbXB1dGF0aW9uOiBpZiBncmFkaWVudCBtYWduaXR1ZGVzIGFyZSBPKDEpLCBmcDMyIGdyYWRpZW50cyBhcmUgYWNjdXJhdGUgdG8gfjcgZGVjaW1hbCBwbGFjZXMg4oCUIG1vcmUgdGhhbiBzdWZmaWNpZW50LiBJZiBncmFkaWVudHMgYXJlIHZlcnkgc21hbGwgKE8oMWUtNikgb3Igc21hbGxlciksIHRoZSByZWxhdGl2ZSBlcnJvciBvZiBmcDE2IGNhbiBkb21pbmF0ZS4gVGhpcyBpcyB3aHkgZnAzMiBtYXN0ZXIgd2VpZ2h0cyBhcmUgbWFpbnRhaW5lZCBpbiBtaXhlZC1wcmVjaXNpb24gdHJhaW5pbmcgZXZlbiB3aGVuIGZvcndhcmQgYW5kIGJhY2t3YXJkIHBhc3NlcyBydW4gaW4gYmYxNi4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJGbG9hdCBFcXVhbGl0eSBhbmQgQ29tcGFyaXNvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkRpcmVjdCBlcXVhbGl0eSBjb21wYXJpc29uIChhID09IGIpIGlzIGFsbW9zdCBuZXZlciBhcHByb3ByaWF0ZSBmb3IgZmxvYXRpbmctcG9pbnQgdmFsdWVzIGNvbXB1dGVkIGJ5IGRpZmZlcmVudCBjb2RlIHBhdGhzLiBCZWNhdXNlIGludGVybWVkaWF0ZSByb3VuZGluZyBlcnJvcnMgYWNjdW11bGF0ZSBkaWZmZXJlbnRseSwgdHdvIG1hdGhlbWF0aWNhbGx5IGlkZW50aWNhbCBjb21wdXRhdGlvbnMgY2FuIHByb2R1Y2Ugc2xpZ2h0bHkgZGlmZmVyZW50IHJlc3VsdHMuIFRoZSBjbGFzc2ljIGV4YW1wbGU6IDAuMSArIDAuMiDiiaAgMC4zIGluIGJpbmFyeSBmbG9hdGluZy1wb2ludCBiZWNhdXNlIG5vbmUgb2YgdGhlc2UgdmFsdWVzIGFyZSBleGFjdGx5IHJlcHJlc2VudGFibGUuXG5cbkNvcnJlY3QgYXBwcm9hY2g6IGNoZWNrIGlmIHxhIOKIkiBifCDiiaQgYXRvbCArIHJ0b2wgw5cgfGJ8IGZvciBhcHByb3ByaWF0ZSB0b2xlcmFuY2VzLiBUaGlzIGlzIGV4YWN0bHkgd2hhdCBudW1weS5pc2Nsb3NlIGFuZCB0b3JjaC5pc2Nsb3NlIGltcGxlbWVudC4gRm9yIGZwMzIgY29tcHV0YXRpb25zIHdpdGggfjEwMCBvcGVyYXRpb25zLCBydG9sPTFlLTQgYW5kIGF0b2w9MWUtNiBpcyBhIHJlYXNvbmFibGUgZGVmYXVsdC4gRm9yIGJmMTYsIHJ0b2w9MWUtMiByZWZsZWN0cyB0aGUgZm9ybWF0J3MgbGltaXRlZCBwcmVjaXNpb24uIEZvciBncmFkaWVudCBjaGVja2luZyAobnVtZXJpY2FsIHZzIGFuYWx5dGljYWwpLCB1c2UgY2VudHJhbCBkaWZmZXJlbmNlcyB3aXRoIHN0ZXAgaCDiiYgg4oiazrVfbWFjaCDiiYggMWUtNCBmb3IgZnAzMi4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcblxuIyBDbGFzc2ljIGZsb2F0IGVxdWFsaXR5IGZhaWx1cmVcbnByaW50KFwiMC4xICsgMC4yID09IDAuMzpcIiwgMC4xICsgMC4yID09IDAuMykgICAjIEZhbHNlXG5wcmludChmXCIwLjEgKyAwLjIgPSB7MC4xICsgMC4yOi4xN2Z9XCIpXG5wcmludChmXCIwLjMgICAgICAgPSB7MC4zOi4xN2Z9XCIpXG5cbiMgQ29ycmVjdDogdG9sZXJhbmNlLWJhc2VkIGNvbXBhcmlzb25cbnByaW50KFwibnAuaXNjbG9zZTpcIiwgbnAuaXNjbG9zZSgwLjEgKyAwLjIsIDAuMykpICAjIFRydWVcbiMgRm9ybXVsYTogfGEtYnwgPD0gYXRvbCArIHJ0b2wgKiB8YnxcblxuIyBmcDMyIHJvdW5kdHJpcCB0aHJvdWdoIHN0cmluZyB2cyBjb21wdXRhdGlvblxuYSA9IG5wLmZsb2F0MzIoMS4wIC8gMy4wKVxuYiA9IG5wLmZsb2F0MzIoMC4zMzMzMzMpXG5wcmludChmXCJcXG4xLzMgZnAzMj17YTouOGZ9LCAwLjMzMzMzMz17YjouOGZ9LCBpc2Nsb3NlPXtucC5pc2Nsb3NlKGEsIGIsIHJ0b2w9MWUtNCl9XCIpXG5cbiMgdG9yY2guaXNjbG9zZSBmb3IgdGVuc29yIGNvbXBhcmlzb25cbnggPSB0b3JjaC50ZW5zb3IoWzEuMCwgMS4wICsgMWUtNywgMTAwMC4wXSwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnkgPSB0b3JjaC50ZW5zb3IoWzEuMCwgMS4wLCAgICAgICAgIDEwMDAuMCArIDFlLTRdLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxucHJpbnQoXCJ0b3JjaC5pc2Nsb3NlIChydG9sPTFlLTQsIGF0b2w9MWUtNik6XCIsIHRvcmNoLmlzY2xvc2UoeCwgeSwgcnRvbD0xZS00LCBhdG9sPTFlLTYpKVxuXG4jIE9wdGltYWwgc3RlcCBmb3IgZ3JhZGllbnQgY2hlY2tpbmc6IGggPSBzcXJ0KGVwc19tYWNoKVxuZnAzMl9lcHMgPSBucC5maW5mbyhucC5mbG9hdDMyKS5lcHNcbmggPSBucC5zcXJ0KGZwMzJfZXBzKVxucHJpbnQoZlwiXFxuT3B0aW1hbCBncmFkaWVudC1jaGVjayBzdGVwIChmcDMyKTogaCA9IHNxcnQoe2ZwMzJfZXBzOi4yZX0pID0ge2g6LjRlfVwiKVxuXG5kZWYgbnVtZXJpY2FsX2dyYWRfY2VudHJhbChmLCB4LCBoPTFlLTQpOlxuICAgIHJldHVybiAoZih4ICsgaCkgLSBmKHggLSBoKSkgLyAoMiAqIGgpXG5cbmYgPSBsYW1iZGEgeDogeCoqMyAtIDIqeCArIDFcbnByaW50KGZcIk51bWVyaWNhbCBncmFkIG9mIHheMy0yeCsxIGF0IHg9Mjoge251bWVyaWNhbF9ncmFkX2NlbnRyYWwoZiwgMi4wKTouOGZ9XCIpXG5wcmludChmXCJBbmFseXRpY2FsICgzeF4yLTIpIGF0IHg9MjogICAgICAgICB7Myo0IC0gMjouOGZ9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2FoYW4gQ29tcGVuc2F0ZWQgU3VtbWF0aW9uIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTmFpdmUgc2VxdWVudGlhbCBzdW1tYXRpb24gYWNjdW11bGF0ZXMgTyhuIMOXIM61X21hY2gpIGVycm9yOiBlYWNoIGFkZGl0aW9uIGludHJvZHVjZXMgYSBzbWFsbCByb3VuZGluZyBlcnJvciB0aGF0IGdyb3dzIHdpdGggbi4gRm9yIG4gPSAxMCBtaWxsaW9uIGZwMzIgYWRkaXRpb25zLCB0aGUgd29yc3QtY2FzZSBhY2N1bXVsYXRlZCBlcnJvciBpcyB+MS4xOS4gVGhlIEthaGFuIGNvbXBlbnNhdGVkIHN1bW1hdGlvbiBhbGdvcml0aG0gcmVkdWNlcyB0aGlzIHRvIE8ozrVfbWFjaCkgaW5kZXBlbmRlbnQgb2YgbiBieSB0cmFja2luZyB0aGUgbG93LW9yZGVyIGJpdHMgZGlzY2FyZGVkIGluIGVhY2ggYWRkaXRpb24uXG5cblRoZSBhbGdvcml0aG0gbWFpbnRhaW5zIGEgY29tcGVuc2F0aW9uIHZhcmlhYmxlIGMuIEF0IGVhY2ggc3RlcDpcbi0geSA9IHjhtaIg4oiSIGMgICAoYWRqdXN0IGlucHV0IGJ5IGFjY3VtdWxhdGVkIGVycm9yKVxuLSB0ID0gdG90YWwgKyB5ICAoYWRkIGFkanVzdGVkIHZhbHVlKVxuLSBjID0gKHQg4oiSIHRvdGFsKSDiiJIgeSAgKGNhcHR1cmUgYml0cyBsb3N0IHdoZW4gYWRkaW5nIHkgdG8gdG90YWwpXG4tIHRvdGFsID0gdFxuXG5UaGUga2V5IGluc2lnaHQ6ICh0IOKIkiB0b3RhbCkgcmVjb3ZlcnMgd2hhdCB3YXMgYWN0dWFsbHkgYWRkZWQgdG8gdG90YWwgKG5vdCBleGFjdGx5IHkgZHVlIHRvIHJvdW5kaW5nKSwgc28gKHQg4oiSIHRvdGFsKSDiiJIgeSBjYXB0dXJlcyB0aGUgcm91bmRpbmcgZXJyb3IuIE51bVB5J3MgYnVpbHQtaW4gc3VtIHVzZXMgcGFpcndpc2Ugc3VtbWF0aW9uLCBhY2hpZXZpbmcgTyhsb2cgbiDDlyDOtV9tYWNoKSDigJQgYmV0dGVyIHRoYW4gbmFpdmUgYnV0IHdvcnNlIHRoYW4gS2FoYW4uIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbmFpdmVfc3VtKGFycik6XG4gICAgXCJcIlwiU2VxdWVudGlhbCBzdW1tYXRpb24g4oCUIE8obiAqIGVwcykgYWNjdW11bGF0ZWQgZXJyb3IuXCJcIlwiXG4gICAgdG90YWwgPSBhcnIuZHR5cGUudHlwZSgwLjApXG4gICAgZm9yIHggaW4gYXJyOlxuICAgICAgICB0b3RhbCArPSB4XG4gICAgcmV0dXJuIGZsb2F0KHRvdGFsKVxuXG5kZWYga2FoYW5fc3VtKGFycik6XG4gICAgXCJcIlwiS2FoYW4gY29tcGVuc2F0ZWQgc3VtbWF0aW9uIOKAlCBPKGVwcykgZXJyb3IgaW5kZXBlbmRlbnQgb2Ygbi5cIlwiXCJcbiAgICB0b3RhbCA9IGFyci5kdHlwZS50eXBlKDAuMClcbiAgICBjb21wICA9IGFyci5kdHlwZS50eXBlKDAuMClcbiAgICBmb3IgeCBpbiBhcnI6XG4gICAgICAgIHkgICAgID0geCAtIGNvbXAgICAgICAgICMgY29ycmVjdGVkIGFkZGVuZFxuICAgICAgICB0ICAgICA9IHRvdGFsICsgeSAgICAgICAjIHByb3Zpc2lvbmFsIHN1bVxuICAgICAgICBjb21wICA9ICh0IC0gdG90YWwpIC0geSAjIG5ldyBjb21wZW5zYXRpb24gKGJpdHMgbG9zdClcbiAgICAgICAgdG90YWwgPSB0XG4gICAgcmV0dXJuIGZsb2F0KHRvdGFsKVxuXG4jIENvbXBhcmUgb24gMTBNIGZwMzIgdmFsdWVzXG5uID0gMTBfMDAwXzAwMFxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxudmFsc19mMzIgPSBybmcuc3RhbmRhcmRfbm9ybWFsKG4pLmFzdHlwZShucC5mbG9hdDMyKVxudHJ1ZV9zdW0gPSBmbG9hdChucC5zdW0odmFsc19mMzIuYXN0eXBlKG5wLmZsb2F0NjQpKSkgICMgZnA2NCBncm91bmQgdHJ1dGhcblxubmFpdmUgID0gbmFpdmVfc3VtKHZhbHNfZjMyKVxua2FoYW4gID0ga2FoYW5fc3VtKHZhbHNfZjMyKVxubnBfc3VtID0gZmxvYXQobnAuc3VtKHZhbHNfZjMyKSkgICAjIHBhaXJ3aXNlIHN1bW1hdGlvblxuXG5wcmludChmXCJUcnVlIHN1bSAoZnA2NCk6IHt0cnVlX3N1bTouOGZ9XCIpXG5wcmludChmXCJOYWl2ZSBmcDMyOiAgZXJyb3I9e2FicyhuYWl2ZSAgLSB0cnVlX3N1bSk6LjNlfVwiKVxucHJpbnQoZlwiS2FoYW4gZnAzMjogIGVycm9yPXthYnMoa2FoYW4gIC0gdHJ1ZV9zdW0pOi4zZX1cIilcbnByaW50KGZcIm5wLnN1bSBmcDMyOiBlcnJvcj17YWJzKG5wX3N1bSAtIHRydWVfc3VtKTouM2V9XCIpXG5cbiMgRXJyb3Igc2NhbGluZyB3aXRoIG5cbnByaW50KFwiXFxuLS0tIEVycm9yIGdyb3d0aCB2cyBuIChhbGwtb25lcyAqIDFlLTcpIC0tLVwiKVxuZm9yIG5fdCBpbiBbMTAwLCAxMF8wMDAsIDFfMDAwXzAwMF06XG4gICAgdiA9IG5wLm9uZXMobl90LCBkdHlwZT1ucC5mbG9hdDMyKSAqIG5wLmZsb2F0MzIoMWUtNylcbiAgICB0cnVlX3YgPSBuX3QgKiAxZS03XG4gICAgbmUgPSBhYnMobmFpdmVfc3VtKHYpIC0gdHJ1ZV92KTsga2UgPSBhYnMoa2FoYW5fc3VtKHYpIC0gdHJ1ZV92KVxuICAgIHByaW50KGZcIiAgbj17bl90Oj45LH06IG5haXZlX2Vycj17bmU6LjJlfSAga2FoYW5fZXJyPXtrZTouMmV9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiTUwgYW5kIEFJIENvbm5lY3Rpb25zIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiSW4gZGVlcCBsZWFybmluZywgZmxvYXRpbmctcG9pbnQgcHJlY2lzaW9uIGFmZmVjdHMgZXZlcnkgY29tcHV0YXRpb24gc3RhZ2UgZGlmZmVyZW50bHkuIFRoZSBmb3J3YXJkIHBhc3MgaXMgdXN1YWxseSBmaW5lIGluIGJmMTYgYmVjYXVzZSBMYXllck5vcm0gYW5kIHJlc2lkdWFsIGNvbm5lY3Rpb25zIGtlZXAgYWN0aXZhdGlvbnMgaW4gYSBoZWFsdGh5IHJhbmdlLiBUaGUgYmFja3dhcmQgcGFzcyBpcyBtb3JlIHNlbnNpdGl2ZTogZ3JhZGllbnRzIG11c3Qgc3Vydml2ZSBtYW55IG1hdHJpeCBtdWx0aXBsaWNhdGlvbnMsIGFuZCB2YW5pc2hpbmcgZ3JhZGllbnRzIGNvbXBvdW5kIHByZWNpc2lvbiBsb3NzLiBMb3NzIHNjYWxpbmcgKHVzZWQgaW4gQU1QL0ZTRFAgdHJhaW5pbmcpIG11bHRpcGxpZXMgdGhlIGxvc3MgYnkgYSBsYXJnZSBmYWN0b3IgKGUuZy4sIDJeMTUgPSAzMjc2OCkgYmVmb3JlIGJhY2t3YXJkLCBzaGlmdGluZyBzbWFsbCBncmFkaWVudHMgaW50byB0aGUgcmVwcmVzZW50YWJsZSBmcDE2IHJhbmdlLCB0aGVuIGRpdmlkZXMgdGhlIHJlY292ZXJlZCBncmFkaWVudHMgYmVmb3JlIHRoZSBvcHRpbWl6ZXIgc3RlcC5cblxuQXR0ZW50aW9uIGlzIHBhcnRpY3VsYXJseSBzZW5zaXRpdmU6IFFAS15UIHZhbHVlcyBjYW4gYmVjb21lIGxhcmdlIGZvciBoaWdoIG1vZGVsIGRpbWVuc2lvbnMsIGNhdXNpbmcgb3ZlcmZsb3cgaW4gZnAxNiAoYnV0IG5vdCBiZjE2LCB3aGljaCBoYXMgdGhlIHNhbWUgZXhwb25lbnQgcmFuZ2UgYXMgZnAzMikuIEZsYXNoQXR0ZW50aW9uIGFkZHJlc3NlcyB0aGlzIGJ5IGNvbXB1dGluZyBzb2Z0bWF4IGluIHRpbGVzIHdpdGggb25saW5lIG5vcm1hbGl6YXRpb24sIGtlZXBpbmcgaW50ZXJtZWRpYXRlIHZhbHVlcyBpbiByZWdpc3RlcnMgYW5kIGF2b2lkaW5nIG1hdGVyaWFsaXphdGlvbiBvZiB0aGUgZnVsbCBhdHRlbnRpb24gbWF0cml4IGluIGxvd2VyLXByZWNpc2lvbiBmb3JtYXRzLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuXG4jIE1peGVkIHByZWNpc2lvbiBkb3QgcHJvZHVjdCBlcnJvciBhbmFseXNpc1xucHJpbnQoXCI9PT0gRG90IHByb2R1Y3QgcHJlY2lzaW9uIGFuYWx5c2lzIChuPTEwMjQpID09PVwiKVxubiA9IDEwMjRcbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0MilcbmEgPSBybmcuc3RhbmRhcmRfbm9ybWFsKG4pLmFzdHlwZShucC5mbG9hdDMyKVxuYiA9IHJuZy5zdGFuZGFyZF9ub3JtYWwobikuYXN0eXBlKG5wLmZsb2F0MzIpXG50cnVlX2RvdCA9IGZsb2F0KG5wLmRvdChhLmFzdHlwZShucC5mbG9hdDY0KSwgYi5hc3R5cGUobnAuZmxvYXQ2NCkpKVxuXG5hX3QsIGJfdCA9IHRvcmNoLnRlbnNvcihhKSwgdG9yY2gudGVuc29yKGIpXG5yZXN1bHRzID0ge1xuICAgIFwiZnAzMlwiOiBmbG9hdCh0b3JjaC5kb3QoYV90LCBiX3QpKSxcbiAgICBcImJmMTYgKGZwMzIgYWNjKVwiOiBmbG9hdCh0b3JjaC5kb3QoYV90LmJmbG9hdDE2KCkuZmxvYXQoKSwgYl90LmJmbG9hdDE2KCkuZmxvYXQoKSkpLFxuICAgIFwiZnAxNiAoZnAzMiBhY2MpXCI6IGZsb2F0KHRvcmNoLmRvdChhX3QuaGFsZigpLmZsb2F0KCksIGJfdC5oYWxmKCkuZmxvYXQoKSkpLFxuICAgIFwiYmYxNiBhY2NcIjogZmxvYXQodG9yY2guZG90KGFfdC5iZmxvYXQxNigpLCBiX3QuYmZsb2F0MTYoKSkpLFxufVxuZm9yIG5hbWUsIHZhbCBpbiByZXN1bHRzLml0ZW1zKCk6XG4gICAgcHJpbnQoZlwiICB7bmFtZToyMHN9OiB7dmFsOi42Zn0gIHJlbF9lcnI9e2Ficyh2YWwtdHJ1ZV9kb3QpL2Ficyh0cnVlX2RvdCk6LjJlfVwiKVxuXG4jIExvc3Mgc2NhbGluZyBzaW11bGF0aW9uIChBTVApXG5wcmludChcIlxcbj09PSBMb3NzIFNjYWxpbmcgKEFNUCkgPT09XCIpXG50aW55X2dyYWQgPSB0b3JjaC50ZW5zb3IoMWUtNiwgZHR5cGU9dG9yY2guZmxvYXQxNilcbnNjYWxlID0gMioqMTVcbnNjYWxlZCA9IHRpbnlfZ3JhZCAqIHNjYWxlXG5wcmludChmXCJUaW55IGdyYWQgZnAxNjoge2Zsb2F0KHRpbnlfZ3JhZCk6LjRlfVwiKVxucHJpbnQoZlwiU2NhbGVkIGJ5IHtzY2FsZX06IHtmbG9hdChzY2FsZWQpOi40ZX1cIilcbnByaW50KGZcIlVuc2NhbGVkOiB7ZmxvYXQoc2NhbGVkIC8gc2NhbGUpOi40ZX1cIilcblxuIyBBY2N1bXVsYXRpb24gZXJyb3IgaW4gaXRlcmF0aXZlIGFsZ29yaXRobVxucHJpbnQoXCJcXG49PT0gSXRlcmF0aXZlIGFjY3VtdWxhdGlvbiBlcnJvciA9PT1cIilcbnhfZnAzMiA9IG5wLmZsb2F0MzIoMC4wKVxuZm9yIF8gaW4gcmFuZ2UoMTAwMDApOiB4X2ZwMzIgKz0gbnAuZmxvYXQzMigwLjAwMDEpXG54X2ZwNjQgPSBzdW0oMC4wMDAxIGZvciBfIGluIHJhbmdlKDEwMDAwKSlcbnByaW50KGZcImZwNjQgcmVmZXJlbmNlOiB7eF9mcDY0Oi4xMGZ9XCIpXG5wcmludChmXCJmcDMyIHJlc3VsdDogICAge2Zsb2F0KHhfZnAzMik6LjEwZn0gIGVycm9yPXthYnMoZmxvYXQoeF9mcDMyKS14X2ZwNjQpOi4zZX1cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQaXRmYWxscyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBtb3N0IGNvbW1vbiBmbG9hdGluZy1wb2ludCBwaXRmYWxscyBpbiBNTCBjb2RlOlxuXG4xLiAqKkNhdGFzdHJvcGhpYyBjYW5jZWxsYXRpb24qKjogc3VidHJhY3RpbmcgbmVhcmx5IGVxdWFsIG51bWJlcnMgZGVzdHJveXMgc2lnbmlmaWNhbnQgZGlnaXRzLiBDb21wdXRpbmcgdmFyaWFuY2UgYXMgRVtYwrJdIOKIkiBFW1hdwrIgY2FuIGxvc2UgYWxsIHByZWNpc2lvbiB3aGVuIHRoZSBtZWFuIGlzIGxhcmdlIHJlbGF0aXZlIHRvIHRoZSBzdGFuZGFyZCBkZXZpYXRpb24uXG5cbjIuICoqT3JkZXItb2Ytb3BlcmF0aW9ucyBzZW5zaXRpdml0eSoqOiAoYSArIGIpICsgYyDiiaAgYSArIChiICsgYykgaW4gZmxvYXRpbmctcG9pbnQuIEdQVSByZWR1Y3Rpb24ga2VybmVscyBtYXkgcHJvZHVjZSBkaWZmZXJlbnQgcmVzdWx0cyBkZXBlbmRpbmcgb24gdGhyZWFkIG9yZGVyaW5nIOKAlCB0aGlzIGlzIGV4cGVjdGVkIGFuZCB1c3VhbGx5IGJlbmlnbi5cblxuMy4gKipDb252ZXJnZW5jZSBjaGVja3Mgd2l0aCBleGFjdCBlcXVhbGl0eSoqOiB3aGlsZSBsb3NzICE9IHByZXZfbG9zcyBjYW4gbG9vcCBmb3JldmVyIG9yIHRlcm1pbmF0ZSBlYXJseS4gQWx3YXlzIHVzZSB0b2xlcmFuY2UtYmFzZWQgY29udmVyZ2VuY2U6IHxsb3NzIOKIkiBwcmV2fCA8IHRvbC5cblxuNC4gKipNaXhpbmcgbWFnbml0dWRlcyoqOiBhZGRpbmcgMWU4IGFuZCAxZS04IGluIGZwMzIgbG9zZXMgdGhlIHNtYWxsIHRlcm0gZW50aXJlbHkg4oCUIGl0IGZhbGxzIHdpdGhpbiBtYWNoaW5lIGVwc2lsb24gb2YgdGhlIGxhcmdlIHRlcm0gYW5kIGdldHMgYWJzb3JiZWQgYXMgcm91bmRpbmcgbm9pc2UuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUHJhY3RpY2FsIEd1aWRhbmNlIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQ29uY3JldGUgcnVsZXMgZm9yIGZsb2F0aW5nLXBvaW50IHByZWNpc2lvbiBpbiBNTCBzeXN0ZW1zOlxuXG4tICoqR3JhZGllbnQgY2hlY2tpbmcqKjogY2VudHJhbCBkaWZmZXJlbmNlcyAoZih4K2gpIOKIkiBmKHjiiJJoKSkvKDJoKSB3aXRoIGggPSDiiJrOtV9tYWNoIOKJiCAxZS00IGZvciBmcDMyLiBFeHBlY3QgcnRvbCDiiYggMWUtNCBmb3IgYWdyZWVtZW50LlxuLSAqKkNvbnZlcmdlbmNlIHRlc3RzKio6IHVzZSB8bG9zcyDiiJIgcHJldl9sb3NzfCA8IHJ0b2wgw5cgfHByZXZfbG9zc3wgKyBhdG9sLCBuZXZlciBleGFjdCBlcXVhbGl0eS5cbi0gKipNaXhlZC1wcmVjaXNpb24gdHJhaW5pbmcqKjoga2VlcCBBZGFtIG0xL20yIGFuZCBtYXN0ZXIgd2VpZ2h0cyBpbiBmcDMyOyBmb3J3YXJkL2JhY2t3YXJkIGluIGJmMTY7IGxvc3MgYW5kIGF0dGVudGlvbiBhY2N1bXVsYXRpb24gaW4gZnAzMi5cbi0gKipIaWdoLXByZWNpc2lvbiByZWR1Y3Rpb25zKio6IHByZWZlciBudW1weSdzIGJ1aWx0LWluIHN1bSAocGFpcndpc2UpIG92ZXIgbmFpdmUgbG9vcHM7IHVzZSBLYWhhbiBzdW1tYXRpb24gZm9yIHZlcnkgaGlnaCBhY2N1cmFjeSByZXF1aXJlbWVudHMuXG4tICoqVGVzdGluZyBudW1lcmljYWwgY29ycmVjdG5lc3MqKjogdG9yY2gudGVzdGluZy5hc3NlcnRfY2xvc2UoYSwgYiwgcnRvbD0xZS00LCBhdG9sPTFlLTYpIGZvciBmcDMyOyBydG9sPTFlLTIgZm9yIGJmMTYuIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInZhcmlhbnQiOiAid2FybmluZyIsICJ0aXRsZSI6ICJQcmVjaXNpb24gaXMgTWFnbml0dWRlLVJlbGF0aXZlIiwgImNvbnRlbnQiOiAiTWFjaGluZSBlcHNpbG9uIGlzIGEgcmVsYXRpdmUgcHJlY2lzaW9uOiB0aGUgYWJzb2x1dGUgcHJlY2lzaW9uIGF0IHZhbHVlIHggaXMgfHh8IMOXIM61X21hY2guIEF0IHggPSAxMOKBtiBpbiBmcDMyLCBhYnNvbHV0ZSBwcmVjaXNpb24g4omIIDAuMTE5IOKAlCBubyBkZWNpbWFsIHBsYWNlcyBhdCBhbGwuIE9wZXJhdGlvbnMgdGhhdCBzaW11bHRhbmVvdXNseSBpbnZvbHZlIHZlcnkgbGFyZ2UgYW5kIHZlcnkgc21hbGwgbnVtYmVycyBhcmUgZXNwZWNpYWxseSBwcm9uZSB0byBjYXRhc3Ryb3BoaWMgY2FuY2VsbGF0aW9uLiBOb3JtYWxpemUgaW5wdXRzIHRvIGEgc2Vuc2libGUgcmFuZ2UgYmVmb3JlIHBlcmZvcm1pbmcgc2Vuc2l0aXZlIG9wZXJhdGlvbnMuIn0sIHsidHlwZSI6ICJ0YWJsZSIsICJoZWFkZXJzIjogWyJGb3JtYXQiLCAiTWFudGlzc2EgYml0cyIsICLOtV9tYWNoIiwgIlNhZmUgTUwgdXNlIl0sICJyb3dzIjogW1siZnA2NCIsICI1MiIsICIyLjIyZS0xNiIsICJHcm91bmQgdHJ1dGgsIG51bWVyaWNhbCB0ZXN0aW5nIl0sIFsiZnAzMiIsICIyMyIsICIxLjE5ZS03IiwgIk9wdGltaXplciBzdGF0ZSwgbWFzdGVyIHdlaWdodHMsIGxvc3MiXSwgWyJmcDE2IiwgIjEwIiwgIjkuNzdlLTQiLCAiVGVuc29yIENvcmUgY29tcHV0ZSAobGltaXRlZCBleHBvbmVudCByYW5nZSkiXSwgWyJiZjE2IiwgIjciLCAiNy44MWUtMyIsICJGb3J3YXJkL2JhY2t3YXJkIHBhc3MgKGZ1bGwgZnAzMiBleHBvbmVudCByYW5nZSkiXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAib3JkZXJlZCI6IGZhbHNlLCAiaXRlbXMiOiBbIs61X21hY2ggPSAyXnstbX0gZm9yIG0gbWFudGlzc2EgYml0czsgZnAzMiDOtSDiiYggMS4xOWUtNywgYmYxNiDOtSDiiYggNy44MWUtMy4iLCAiRXZlcnkgSUVFRSA3NTQgb3BlcmF0aW9uIGludHJvZHVjZXMgcmVsYXRpdmUgZXJyb3Ig4omkIM61X21hY2gvMjsgTiBvcGVyYXRpb25zIGFjY3VtdWxhdGUg4omkIE4gw5cgzrVfbWFjaC8yIHdvcnN0IGNhc2UuIiwgIkZsb2F0aW5nLXBvaW50IG51bWJlcnMgYXJlIG5vdCB1bmlmb3JtbHkgc3BhY2VkIOKAlCBhYnNvbHV0ZSBzcGFjaW5nIHNjYWxlcyBhcyB8eHwgw5cgzrVfbWFjaC4iLCAiTmV2ZXIgdXNlID09IGZvciBmbG9hdCBjb21wYXJpc29uOyB1c2UgbnAuaXNjbG9zZSBvciB0b3JjaC5pc2Nsb3NlIHdpdGggZXhwbGljaXQgcnRvbCBhbmQgYXRvbC4iLCAiS2FoYW4gY29tcGVuc2F0ZWQgc3VtbWF0aW9uIHJlZHVjZXMgZXJyb3IgZnJvbSBPKG4gw5cgzrUpIHRvIE8ozrUpIGluZGVwZW5kZW50IG9mIG4g4oCUIGNyaXRpY2FsIGZvciBoaWdoLXByZWNpc2lvbiByZWR1Y3Rpb25zLiIsICJJbiBtaXhlZC1wcmVjaXNpb24gdHJhaW5pbmcsIGJmMTYgaXMgc2FmZSBmb3IgZm9yd2FyZC9iYWNrd2FyZCBiZWNhdXNlIG1pbmktYmF0Y2ggZ3JhZGllbnQgbm9pc2UgZG9taW5hdGVzIG51bWVyaWNhbCBwcmVjaXNpb24gZXJyb3I7IGZwMzIgaXMgcmVxdWlyZWQgZm9yIG9wdGltaXplciBzdGF0ZSBhbmQgbWFzdGVyIHdlaWdodHMuIiwgIkZvciBncmFkaWVudCBjaGVja2luZywgdXNlIGNlbnRyYWwgZGlmZmVyZW5jZXMgd2l0aCBoIOKJiCDiiJrOtV9tYWNoOyBmb3Igc3RhYmxlIHZhcmlhbmNlLCB1c2UgV2VsZm9yZCdzIG9ubGluZSBhbGdvcml0aG0gcmF0aGVyIHRoYW4gRVtYwrJdIOKIkiBFW1hdwrIuIl19XQ=="
---
# Machine Epsilon and Floating-Point Precision

Machine epsilon is the fundamental precision limit of floating-point arithmetic. It determines the smallest relative difference that can be distinguished from zero, sets the floor for numerical differentiation step sizes, and quantifies the precision of gradient computations across every layer of a deep network. Understanding machine epsilon is essential for diagnosing numerical instabilities, choosing convergence tolerances, and reasoning about which operations can safely run in bf16 versus those that require fp32. Every practitioner building at scale will eventually hit a wall caused by insufficient numerical precision — understanding epsilon is the starting point for debugging such failures.

## Core Definition

Machine epsilon (ε_mach) is the smallest positive floating-point number ε such that fl(1 + ε) > 1 — equivalently, the spacing between 1.0 and the next representable number. For a format with m mantissa bits:

ε_mach = 2^{−m}

Values by format:
- fp64 (double): ε = 2^{−52} ≈ 2.22×10⁻¹⁶  (53 significant bits)
- fp32 (float):  ε = 2^{−23} ≈ 1.19×10⁻⁷  (24 significant bits)
- fp16 (half):   ε = 2^{−10} ≈ 9.77×10⁻⁴  (11 significant bits)
- bf16:          ε = 2^{−7}  ≈ 7.81×10⁻³  (8 significant bits)

The unit roundoff is ε_mach/2 — the maximum relative rounding error for any single IEEE 754 operation. Crucially, floating-point numbers are not uniformly spaced: they are denser near zero and sparser for large magnitudes. For a value x, the absolute spacing is approximately |x| × ε_mach, so precision is always measured in relative terms.

```python
import numpy as np
import torch

# Machine epsilon from numpy finfo
print("=== finfo values ===")
for dtype in [np.float16, np.float32, np.float64]:
    info = np.finfo(dtype)
    print(f"{dtype.__name__:10s}: eps={info.eps:.3e}  tiny={info.tiny:.3e}  max={info.max:.3e}")

# bfloat16 is torch-only
print()
for dtype in [torch.float16, torch.bfloat16, torch.float32, torch.float64]:
    info = torch.finfo(dtype)
    print(f"{str(dtype):20s}: eps={info.eps:.3e}  bits={info.bits}")

# Empirically compute fp32 epsilon
print("\n=== Empirical fp32 epsilon ===")
eps = np.float32(1.0)
while np.float32(1.0) + eps / np.float32(2.0) > np.float32(1.0):
    eps = eps / np.float32(2.0)
print(f"Empirical fp32 eps = {eps * 2:.6e}  (np.finfo = {np.finfo(np.float32).eps:.6e})")

# Non-uniform spacing: absolute precision depends on magnitude
print("\n=== Spacing at Different Magnitudes (fp32) ===")
for x_val in [0.5, 1.0, 16.0, 1024.0, 1e6]:
    x = np.float32(x_val)
    nxt = np.nextafter(x, np.float32(np.inf))
    spacing = float(nxt - x)
    print(f"  x={x_val:>10g}: abs_spacing={spacing:.3e}  rel_spacing={spacing/x_val:.3e}")
# Observation: relative spacing ~constant (eps_mach), absolute spacing grows with x
```

## The Relative Error Model

The IEEE 754 standard guarantees that every correctly-rounded operation satisfies:

fl(a ∘ b) = (a ∘ b)(1 + δ),  |δ| ≤ ε_mach/2

This holds for addition, subtraction, multiplication, division, and square root. It means every single floating-point operation introduces relative error at most ε_mach/2. For a computation involving N operations, accumulated error is at most N × ε_mach/2 in the worst case (all errors constructively reinforce), though in practice random cancellation reduces this to roughly √N × ε_mach/2.

Implication for gradient computation: if gradient magnitudes are O(1), fp32 gradients are accurate to ~7 decimal places — more than sufficient. If gradients are very small (O(1e-6) or smaller), the relative error of fp16 can dominate. This is why fp32 master weights are maintained in mixed-precision training even when forward and backward passes run in bf16.

## Float Equality and Comparison

Direct equality comparison (a == b) is almost never appropriate for floating-point values computed by different code paths. Because intermediate rounding errors accumulate differently, two mathematically identical computations can produce slightly different results. The classic example: 0.1 + 0.2 ≠ 0.3 in binary floating-point because none of these values are exactly representable.

Correct approach: check if |a − b| ≤ atol + rtol × |b| for appropriate tolerances. This is exactly what numpy.isclose and torch.isclose implement. For fp32 computations with ~100 operations, rtol=1e-4 and atol=1e-6 is a reasonable default. For bf16, rtol=1e-2 reflects the format's limited precision. For gradient checking (numerical vs analytical), use central differences with step h ≈ √ε_mach ≈ 1e-4 for fp32.

```python
import numpy as np
import torch

# Classic float equality failure
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)   # False
print(f"0.1 + 0.2 = {0.1 + 0.2:.17f}")
print(f"0.3       = {0.3:.17f}")

# Correct: tolerance-based comparison
print("np.isclose:", np.isclose(0.1 + 0.2, 0.3))  # True
# Formula: |a-b| <= atol + rtol * |b|

# fp32 roundtrip through string vs computation
a = np.float32(1.0 / 3.0)
b = np.float32(0.333333)
print(f"\n1/3 fp32={a:.8f}, 0.333333={b:.8f}, isclose={np.isclose(a, b, rtol=1e-4)}")

# torch.isclose for tensor comparison
x = torch.tensor([1.0, 1.0 + 1e-7, 1000.0], dtype=torch.float32)
y = torch.tensor([1.0, 1.0,         1000.0 + 1e-4], dtype=torch.float32)
print("torch.isclose (rtol=1e-4, atol=1e-6):", torch.isclose(x, y, rtol=1e-4, atol=1e-6))

# Optimal step for gradient checking: h = sqrt(eps_mach)
fp32_eps = np.finfo(np.float32).eps
h = np.sqrt(fp32_eps)
print(f"\nOptimal gradient-check step (fp32): h = sqrt({fp32_eps:.2e}) = {h:.4e}")

def numerical_grad_central(f, x, h=1e-4):
    return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x**3 - 2*x + 1
print(f"Numerical grad of x^3-2x+1 at x=2: {numerical_grad_central(f, 2.0):.8f}")
print(f"Analytical (3x^2-2) at x=2:         {3*4 - 2:.8f}")
```

## Kahan Compensated Summation

Naive sequential summation accumulates O(n × ε_mach) error: each addition introduces a small rounding error that grows with n. For n = 10 million fp32 additions, the worst-case accumulated error is ~1.19. The Kahan compensated summation algorithm reduces this to O(ε_mach) independent of n by tracking the low-order bits discarded in each addition.

The algorithm maintains a compensation variable c. At each step:
- y = xᵢ − c   (adjust input by accumulated error)
- t = total + y  (add adjusted value)
- c = (t − total) − y  (capture bits lost when adding y to total)
- total = t

The key insight: (t − total) recovers what was actually added to total (not exactly y due to rounding), so (t − total) − y captures the rounding error. NumPy's built-in sum uses pairwise summation, achieving O(log n × ε_mach) — better than naive but worse than Kahan.

```python
import numpy as np

def naive_sum(arr):
    """Sequential summation — O(n * eps) accumulated error."""
    total = arr.dtype.type(0.0)
    for x in arr:
        total += x
    return float(total)

def kahan_sum(arr):
    """Kahan compensated summation — O(eps) error independent of n."""
    total = arr.dtype.type(0.0)
    comp  = arr.dtype.type(0.0)
    for x in arr:
        y     = x - comp        # corrected addend
        t     = total + y       # provisional sum
        comp  = (t - total) - y # new compensation (bits lost)
        total = t
    return float(total)

# Compare on 10M fp32 values
n = 10_000_000
rng = np.random.default_rng(42)
vals_f32 = rng.standard_normal(n).astype(np.float32)
true_sum = float(np.sum(vals_f32.astype(np.float64)))  # fp64 ground truth

naive  = naive_sum(vals_f32)
kahan  = kahan_sum(vals_f32)
np_sum = float(np.sum(vals_f32))   # pairwise summation

print(f"True sum (fp64): {true_sum:.8f}")
print(f"Naive fp32:  error={abs(naive  - true_sum):.3e}")
print(f"Kahan fp32:  error={abs(kahan  - true_sum):.3e}")
print(f"np.sum fp32: error={abs(np_sum - true_sum):.3e}")

# Error scaling with n
print("\n--- Error growth vs n (all-ones * 1e-7) ---")
for n_t in [100, 10_000, 1_000_000]:
    v = np.ones(n_t, dtype=np.float32) * np.float32(1e-7)
    true_v = n_t * 1e-7
    ne = abs(naive_sum(v) - true_v); ke = abs(kahan_sum(v) - true_v)
    print(f"  n={n_t:>9,}: naive_err={ne:.2e}  kahan_err={ke:.2e}")
```

## ML and AI Connections

In deep learning, floating-point precision affects every computation stage differently. The forward pass is usually fine in bf16 because LayerNorm and residual connections keep activations in a healthy range. The backward pass is more sensitive: gradients must survive many matrix multiplications, and vanishing gradients compound precision loss. Loss scaling (used in AMP/FSDP training) multiplies the loss by a large factor (e.g., 2^15 = 32768) before backward, shifting small gradients into the representable fp16 range, then divides the recovered gradients before the optimizer step.

Attention is particularly sensitive: Q@K^T values can become large for high model dimensions, causing overflow in fp16 (but not bf16, which has the same exponent range as fp32). FlashAttention addresses this by computing softmax in tiles with online normalization, keeping intermediate values in registers and avoiding materialization of the full attention matrix in lower-precision formats.

```python
import numpy as np
import torch

# Mixed precision dot product error analysis
print("=== Dot product precision analysis (n=1024) ===")
n = 1024
rng = np.random.default_rng(42)
a = rng.standard_normal(n).astype(np.float32)
b = rng.standard_normal(n).astype(np.float32)
true_dot = float(np.dot(a.astype(np.float64), b.astype(np.float64)))

a_t, b_t = torch.tensor(a), torch.tensor(b)
results = {
    "fp32": float(torch.dot(a_t, b_t)),
    "bf16 (fp32 acc)": float(torch.dot(a_t.bfloat16().float(), b_t.bfloat16().float())),
    "fp16 (fp32 acc)": float(torch.dot(a_t.half().float(), b_t.half().float())),
    "bf16 acc": float(torch.dot(a_t.bfloat16(), b_t.bfloat16())),
}
for name, val in results.items():
    print(f"  {name:20s}: {val:.6f}  rel_err={abs(val-true_dot)/abs(true_dot):.2e}")

# Loss scaling simulation (AMP)
print("\n=== Loss Scaling (AMP) ===")
tiny_grad = torch.tensor(1e-6, dtype=torch.float16)
scale = 2**15
scaled = tiny_grad * scale
print(f"Tiny grad fp16: {float(tiny_grad):.4e}")
print(f"Scaled by {scale}: {float(scaled):.4e}")
print(f"Unscaled: {float(scaled / scale):.4e}")

# Accumulation error in iterative algorithm
print("\n=== Iterative accumulation error ===")
x_fp32 = np.float32(0.0)
for _ in range(10000): x_fp32 += np.float32(0.0001)
x_fp64 = sum(0.0001 for _ in range(10000))
print(f"fp64 reference: {x_fp64:.10f}")
print(f"fp32 result:    {float(x_fp32):.10f}  error={abs(float(x_fp32)-x_fp64):.3e}")
```

## Pitfalls

The most common floating-point pitfalls in ML code:

1. **Catastrophic cancellation**: subtracting nearly equal numbers destroys significant digits. Computing variance as E[X²] − E[X]² can lose all precision when the mean is large relative to the standard deviation.

2. **Order-of-operations sensitivity**: (a + b) + c ≠ a + (b + c) in floating-point. GPU reduction kernels may produce different results depending on thread ordering — this is expected and usually benign.

3. **Convergence checks with exact equality**: while loss != prev_loss can loop forever or terminate early. Always use tolerance-based convergence: |loss − prev| < tol.

4. **Mixing magnitudes**: adding 1e8 and 1e-8 in fp32 loses the small term entirely — it falls within machine epsilon of the large term and gets absorbed as rounding noise.

## Practical Guidance

Concrete rules for floating-point precision in ML systems:

- **Gradient checking**: central differences (f(x+h) − f(x−h))/(2h) with h = √ε_mach ≈ 1e-4 for fp32. Expect rtol ≈ 1e-4 for agreement.
- **Convergence tests**: use |loss − prev_loss| < rtol × |prev_loss| + atol, never exact equality.
- **Mixed-precision training**: keep Adam m1/m2 and master weights in fp32; forward/backward in bf16; loss and attention accumulation in fp32.
- **High-precision reductions**: prefer numpy's built-in sum (pairwise) over naive loops; use Kahan summation for very high accuracy requirements.
- **Testing numerical correctness**: torch.testing.assert_close(a, b, rtol=1e-4, atol=1e-6) for fp32; rtol=1e-2 for bf16.

> **WARNING: Precision is Magnitude-Relative**
>
> Machine epsilon is a relative precision: the absolute precision at value x is |x| × ε_mach. At x = 10⁶ in fp32, absolute precision ≈ 0.119 — no decimal places at all. Operations that simultaneously involve very large and very small numbers are especially prone to catastrophic cancellation. Normalize inputs to a sensible range before performing sensitive operations.

| Format | Mantissa bits | ε_mach | Safe ML use |
| --- | --- | --- | --- |
| fp64 | 52 | 2.22e-16 | Ground truth, numerical testing |
| fp32 | 23 | 1.19e-7 | Optimizer state, master weights, loss |
| fp16 | 10 | 9.77e-4 | Tensor Core compute (limited exponent range) |
| bf16 | 7 | 7.81e-3 | Forward/backward pass (full fp32 exponent range) |

---

## Key Takeaways

- ε_mach = 2^{-m} for m mantissa bits; fp32 ε ≈ 1.19e-7, bf16 ε ≈ 7.81e-3.
- Every IEEE 754 operation introduces relative error ≤ ε_mach/2; N operations accumulate ≤ N × ε_mach/2 worst case.
- Floating-point numbers are not uniformly spaced — absolute spacing scales as |x| × ε_mach.
- Never use == for float comparison; use np.isclose or torch.isclose with explicit rtol and atol.
- Kahan compensated summation reduces error from O(n × ε) to O(ε) independent of n — critical for high-precision reductions.
- In mixed-precision training, bf16 is safe for forward/backward because mini-batch gradient noise dominates numerical precision error; fp32 is required for optimizer state and master weights.
- For gradient checking, use central differences with h ≈ √ε_mach; for stable variance, use Welford's online algorithm rather than E[X²] − E[X]².
