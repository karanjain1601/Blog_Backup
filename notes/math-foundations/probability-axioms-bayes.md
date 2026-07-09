---
title: "Probability Axioms, Bayes' Theorem, and Conditional Probability"
slug: "probability-axioms-bayes"
description: "Kolmogorov axioms, sigma-algebras, conditional probability, independence, law of total probability, Bayes' theorem derivation, base rate neglect, and Bayesian inference as the engine of ML."
tags: ["probability", "statistics", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiUHJvYmFiaWxpdHkgdGhlb3J5IGlzIHRoZSBtYXRoZW1hdGljYWwgbGFuZ3VhZ2UgZm9yIHF1YW50aWZ5aW5nIHVuY2VydGFpbnR5IOKAlCBpbmRpc3BlbnNhYmxlIGZvciBhbnkgTUwgcHJhY3RpdGlvbmVyLiBBbmRyZXkgS29sbW9nb3JvdidzIDE5MzMgYXhpb21hdGlzYXRpb24gcHV0IHByb2JhYmlsaXR5IG9uIHJpZ29yb3VzIG1lYXN1cmUtdGhlb3JldGljIGZvdW5kYXRpb25zLiBFdmVyeXRoaW5nIGZyb20gQmF5ZXNpYW4gbmV0d29ya3MgdG8gZGlmZnVzaW9uIG1vZGVscyBkZXJpdmVzIGZyb20gdGhyZWUgZGVjZXB0aXZlbHkgc2ltcGxlIGF4aW9tcy4gVGhpcyBub3RlIGRldmVsb3BzIHRoZSBmdWxsIGNoYWluOiBmcm9tIGF4aW9tcyB0byBjb25kaXRpb25hbCBwcm9iYWJpbGl0eSwgaW5kZXBlbmRlbmNlLCB0aGUgbGF3IG9mIHRvdGFsIHByb2JhYmlsaXR5LCBCYXllcycgdGhlb3JlbSwgYmFzZSByYXRlIG5lZ2xlY3QsIGFuZCBmaW5hbGx5IHRoZSBCYXllc2lhbiBpbnRlcnByZXRhdGlvbiBvZiByZWd1bGFyaXNhdGlvbiwgTUFQIGVzdGltYXRpb24sIGFuZCBwcmlvciBkZXNpZ24gdGhhdCB1bmRlcmxpZXMgbW9kZXJuIE1MIHRoZW9yeS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJLb2xtb2dvcm92IEF4aW9tcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkxldCDOqSBiZSBhIHNhbXBsZSBzcGFjZSAoYWxsIHBvc3NpYmxlIG91dGNvbWVzKSwgYW5kIGxldCBGIGJlIGEgz4MtYWxnZWJyYSBvZiBldmVudHMgKG1lYXN1cmFibGUgc3Vic2V0cyBvZiDOqSkuIEEgcHJvYmFiaWxpdHkgbWVhc3VyZSBQOiBGIOKGkiBbMCwxXSBtdXN0IHNhdGlzZnkgdGhyZWUgYXhpb21zOlxuXG4xLiBOb24tbmVnYXRpdml0eTogUChBKSDiiaUgMCBmb3IgZXZlcnkgZXZlbnQgQSDiiIggRlxuMi4gTm9ybWFsaXphdGlvbjogUCjOqSkgPSAxIChzb21ldGhpbmcgbXVzdCBoYXBwZW4pXG4zLiBDb3VudGFibGUgYWRkaXRpdml0eTogRm9yIGFueSBjb3VudGFibGUgc2VxdWVuY2Ugb2YgbXV0dWFsbHkgZXhjbHVzaXZlIGV2ZW50cyBB4oKBLCBB4oKCLCDigKY6IFAo4ouD4bWiIEHhtaIpID0gzqPhtaIgUChB4bWiKVxuXG5BbGwgcHJvYmFiaWxpdHkgcnVsZXMgYXJlIHRoZW9yZW1zIGRlcml2ZWQgZnJvbSB0aGVzZSBheGlvbXMgYWxvbmU6XG4tIFAo4oiFKSA9IDAgKGRlcml2ZWQgZnJvbSBheGlvbSAzIHdpdGggYWxsIGVtcHR5IGV2ZW50cylcbi0gUChB4bacKSA9IDEg4oiSIFAoQSkgKGRlcml2ZWQgZnJvbSBheGlvbXMgMiBhbmQgMylcbi0gUChBIOKIqiBCKSA9IFAoQSkgKyBQKEIpIOKIkiBQKEEg4oipIEIpIChpbmNsdXNpb24tZXhjbHVzaW9uKVxuLSBJZiBBIOKKhiBCIHRoZW4gUChBKSDiiaQgUChCKSAobW9ub3RvbmljaXR5KVxuXG5UaGUgz4MtYWxnZWJyYSByZXF1aXJlbWVudCBlbnN1cmVzIHdlIGNhbiB0YWtlIGNvbXBsZW1lbnRzIGFuZCBjb3VudGFibGUgdW5pb25zIG9mIG1lYXN1cmFibGUgZXZlbnRzLCBzaWRlc3RlcHBpbmcgbm9uLW1lYXN1cmFibGUgc2V0IHBhcmFkb3hlcyAoZS5nLiwgQmFuYWNoLVRhcnNraSkgdGhhdCBhcmlzZSBpbiBjb250aW51b3VzIHNwYWNlcy4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidmFyaWFudCI6ICJpbmZvIiwgInRpdGxlIjogIldoeSDPgy1hbGdlYnJhcyBtYXR0ZXIgZm9yIE1MIiwgImNvbnRlbnQiOiAiRm9yIGZpbml0ZSBzYW1wbGUgc3BhY2VzIGV2ZXJ5IHN1YnNldCBpcyB0cml2aWFsbHkgbWVhc3VyYWJsZS4gRm9yIGNvbnRpbnVvdXMgc3BhY2VzICjOqSA9IOKEnSkgd2UgcmVzdHJpY3QgdG8gQm9yZWwgc2V0cyB0byBhdm9pZCBub24tbWVhc3VyYWJsZSBwYXRob2xvZ2llcy4gSW4gTUwgcHJhY3RpY2UgdGhlIM+DLWFsZ2VicmEgaXMgaW52aXNpYmxlLCBidXQgaXQgaXMgd2h5IHdlIGNhbiByaWdvcm91c2x5IHRhbGsgYWJvdXQgUChYIOKJpCB4KSBmb3IgYSBjb250aW51b3VzIHJhbmRvbSB2YXJpYWJsZSBYIOKAlCB0aGlzIGRlZmluZXMgdGhlIENERiwgZnJvbSB3aGljaCBQREZzIGFuZCBleHBlY3RhdGlvbnMgZm9sbG93LiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkNvbmRpdGlvbmFsIFByb2JhYmlsaXR5In0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhlIGNvbmRpdGlvbmFsIHByb2JhYmlsaXR5IG9mIEEgZ2l2ZW4gQiAod2l0aCBQKEIpID4gMCkgaXMgZGVmaW5lZCBhczpcblxuUChBfEIpID0gUChBIOKIqSBCKSAvIFAoQilcblxuSW50ZXJwcmV0YXRpb246IHJlc3RyaWN0IHRoZSBzYW1wbGUgc3BhY2UgdG8gZXZlbnQgQiBhbmQgcmVub3JtYWxpemUuIENvbmRpdGlvbmFsIHByb2JhYmlsaXR5IGlzIGl0c2VsZiBhIHZhbGlkIHByb2JhYmlsaXR5IG1lYXN1cmUgb24gzqkgcmVzdHJpY3RlZCB0byBCIOKAlCBhbGwgdGhyZWUgS29sbW9nb3JvdiBheGlvbXMgaG9sZC5cblxuUHJvZHVjdCBydWxlICh0aGUgZGVmaW5pdGlvbiByZXdyaXR0ZW4pOlxuXG5QKEEg4oipIEIpID0gUChBfEIpIMOXIFAoQikgPSBQKEJ8QSkgw5cgUChBKVxuXG5UaGlzIHNpbXBsZSByZXdyaXRlIOKAlCBlcXVhdGluZyB0d28gd2F5cyB0byBmYWN0b3IgdGhlIGpvaW50IHByb2JhYmlsaXR5IOKAlCBpcyB0aGUgYWxnZWJyYWljIGhlYXJ0IG9mIEJheWVzJyB0aGVvcmVtLiBUaGUgY2hhaW4gcnVsZSBleHRlbmRzIHRoaXMgdG8gbiBldmVudHM6XG5cblAoQeKCgSDiiKkgQeKCgiDiiKkg4oCmIOKIqSBB4oKZKSA9IFAoQeKCgSkgw5cgUChB4oKCfEHigoEpIMOXIFAoQeKCg3xB4oKBLEHigoIpIMOXIOKApiDDlyBQKEHigpl8QeKCgSzigKYsQeKCmeKCi+KCgSlcblxuVGhpcyBmYWN0b3Jpc2F0aW9uIGlzIHRoZSBmb3VuZGF0aW9uIG9mIGF1dG9yZWdyZXNzaXZlIGxhbmd1YWdlIG1vZGVsczogcCh44oKBLOKApix44oKZKSA9IM6g4oKcIHAoeOKCnHx44oKBLOKApix44oKc4oKL4oKBKS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJTdGF0aXN0aWNhbCBJbmRlcGVuZGVuY2UifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJFdmVudHMgQSBhbmQgQiBhcmUgc3RhdGlzdGljYWxseSBpbmRlcGVuZGVudCBpZjpcblxuUChBIOKIqSBCKSA9IFAoQSkgw5cgUChCKSwgIGVxdWl2YWxlbnRseSBQKEF8QikgPSBQKEEpXG5cbktub3dpbmcgQiBjYXJyaWVzIHplcm8gaW5mb3JtYXRpb24gYWJvdXQgQS4gSW5kZXBlbmRlbmNlIGlzIHN5bW1ldHJpYzogQSDiiqUgQiBpZmYgQiDiiqUgQS5cblxuQ29uZGl0aW9uYWwgaW5kZXBlbmRlbmNlOiBBIOKKpSBCIHwgQyBtZWFucyBQKEEg4oipIEIgfCBDKSA9IFAoQXxDKSDDlyBQKEJ8QykuIE5haXZlIEJheWVzIGFzc3VtZXMgZmVhdHVyZXMgWOKCgSwg4oCmLCBYZCBhcmUgY29uZGl0aW9uYWxseSBpbmRlcGVuZGVudCBnaXZlbiBjbGFzcyBZIOKAlCBhIHN0cm9uZyBhc3N1bXB0aW9uIHRoYXQgcmVkdWNlcyBwYXJhbWV0ZXIgY291bnQgZnJvbSBPKHzwnZKzfF5kKSB0byBPKGQgw5cgfPCdkrN8KSBhbmQgbWFrZXMgdHJhaW5pbmcgdHJhY3RhYmxlLlxuXG5Dcml0aWNhbCBkaXN0aW5jdGlvbjogaW5kZXBlbmRlbmNlIGltcGxpZXMgemVybyBjb3ZhcmlhbmNlLCBidXQgemVybyBjb3ZhcmlhbmNlIGRvZXMgTk9UIGltcGx5IGluZGVwZW5kZW5jZSBpbiBnZW5lcmFsLiBUaGUgZXhjZXB0aW9uIGlzIGpvaW50bHkgR2F1c3NpYW4gcmFuZG9tIHZhcmlhYmxlcywgd2hlcmUgdW5jb3JyZWxhdGVkIOKfuiBpbmRlcGVuZGVudC4gVGhpcyBpcyB3aHkgdGhlIEdhdXNzaWFuIGlzIGNlbnRyYWwgdG8gc28gbXVjaCBwcm9iYWJpbGlzdGljIE1MIOKAlCBpdCBpcyB0aGUgb25seSBkaXN0cmlidXRpb24gd2hlcmUgc2Vjb25kLW9yZGVyIHN0YXRpc3RpY3MgZnVsbHkgY2hhcmFjdGVyaXNlIGRlcGVuZGVuY2Ugc3RydWN0dXJlLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkgaW1wb3J0IHN0YXRzXG5cbiMgVmVyaWZ5IEtvbG1vZ29yb3YgYXhpb21zIHdpdGggZW1waXJpY2FsIHByb2JhYmlsaXRpZXNcbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0Milcbm5fdHJpYWxzID0gMTAwXzAwMFxuZGllID0gcm5nLmludGVnZXJzKDEsIDcsIHNpemU9bl90cmlhbHMpICAgIyBmYWlyIDYtc2lkZWQgZGllXG5cblBfZXZlbiA9IG5wLm1lYW4oZGllICUgMiA9PSAwKVxuUF9ndDMgID0gbnAubWVhbihkaWUgPiAzKVxuUF9ib3RoID0gbnAubWVhbigoZGllICUgMiA9PSAwKSAmIChkaWUgPiAzKSkgICAjIGV2ZW4gQU5EID4gMzogezQsIDZ9XG5QX2VpdGhlciA9IG5wLm1lYW4oKGRpZSAlIDIgPT0gMCkgfCAoZGllID4gMykpICMgZXZlbiBPUiA+IDM6IHsyLDQsNSw2fVxuXG5wcmludChcIj09PSBLb2xtb2dvcm92IEF4aW9tIFZlcmlmaWNhdGlvbiA9PT1cIilcbnByaW50KGZcIlAoZXZlbikgPSB7UF9ldmVuOi40Zn0gIChleHBlY3RlZCAwLjUpXCIpXG5wcmludChmXCJQKD4zKSAgID0ge1BfZ3QzOi40Zn0gIChleHBlY3RlZCAwLjUpXCIpXG5wcmludChmXCJQKGV2ZW4gQU5EID4zKSA9IHtQX2JvdGg6LjRmfSAgKGV4cGVjdGVkIDAuMzMzMyA9IHsyLzY6LjRmfSlcIilcbnByaW50KGZcIkluY2x1c2lvbi1leGNsdXNpb246IFAoZSkrUChnKS1QKGUmZykgPSB7UF9ldmVuK1BfZ3QzLVBfYm90aDouNGZ9XCIpXG5wcmludChmXCJQKGV2ZW4gT1IgPjMpICAgICAgID0ge1BfZWl0aGVyOi40Zn0gIChtYXRjaDoge1BfZXZlbitQX2d0My1QX2JvdGg6LjRmfSlcIilcblxuIyBDb25kaXRpb25hbCBwcm9iYWJpbGl0eTogUCg+MyB8IGV2ZW4pXG5QX2d0M19naXZlbl9ldmVuID0gUF9ib3RoIC8gUF9ldmVuXG5wcmludChmXCJcXG5QKD4zIHwgZXZlbikgPSBQKGJvdGgpL1AoZXZlbikgPSB7UF9ndDNfZ2l2ZW5fZXZlbjouNGZ9ICAoZXhwZWN0ZWQgMC42NjY3KVwiKVxuXG4jIEluZGVwZW5kZW5jZSB0ZXN0OiBhcmUgJ2V2ZW4nIGFuZCAnPjMnIGluZGVwZW5kZW50P1xucHJpbnQoZlwiXFxuSW5kZXBlbmRlbmNlIGNoZWNrOiBQKGUpKlAoZykgPSB7UF9ldmVuKlBfZ3QzOi40Zn0gIHZzIFAoZSZnKSA9IHtQX2JvdGg6LjRmfVwiKVxucHJpbnQoZlwiSW5kZXBlbmRlbnQ/IHtucC5pc2Nsb3NlKFBfZXZlbiAqIFBfZ3QzLCBQX2JvdGgsIGF0b2w9MC4wMSl9XCIpICAjIE5vXG5cbiMgR2VuZXJhdGUgaW5kZXBlbmRlbnQgdnMgZGVwZW5kZW50IGV4YW1wbGVzXG54ID0gcm5nLnN0YW5kYXJkX25vcm1hbCgxMDAwMClcbnlfZGVwID0geCArIDAuNSAqIHJuZy5zdGFuZGFyZF9ub3JtYWwoMTAwMDApICAgIyBkZXBlbmRlbnQgb24geFxueV9pbmQgPSBybmcuc3RhbmRhcmRfbm9ybWFsKDEwMDAwKSAgICAgICAgICAgICAgICMgaW5kZXBlbmRlbnQgb2YgeFxucHJpbnQoZlwiXFxuQ29ycih4LCB5X2RlcCkgPSB7bnAuY29ycmNvZWYoeCwgeV9kZXApWzAsMV06LjRmfVwiKVxucHJpbnQoZlwiQ29ycih4LCB5X2luZCkgPSB7bnAuY29ycmNvZWYoeCwgeV9pbmQpWzAsMV06LjRmfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkxhdyBvZiBUb3RhbCBQcm9iYWJpbGl0eSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIklmIHtC4oKBLCBC4oKCLCDigKYsIELigpl9IGlzIGEgcGFydGl0aW9uIG9mIM6pIChtdXR1YWxseSBleGNsdXNpdmUgYW5kIGV4aGF1c3RpdmUgZXZlbnRzKSwgdGhlbjpcblxuUChBKSA9IM6j4bWiIFAoQSB8IELhtaIpIMOXIFAoQuG1oilcblxuSW4gY29udGludW91cyBmb3JtIChtYXJnaW5hbGlzYXRpb24gb3ZlciBhIGxhdGVudCB2YXJpYWJsZSB6KTpcblxucCh4KSA9IOKIqyBwKHggfCB6KSDDlyBwKHopIGR6XG5cblRoaXMgaW50ZWdyYWwgaXMgdGhlIG1hcmdpbmFsIGxpa2VsaWhvb2Qgb3IgZXZpZGVuY2UgaW4gQmF5ZXNpYW4gbW9kZWxzLiBJdCBhcHBlYXJzIGluIHRoZSBkZW5vbWluYXRvciBvZiBCYXllcycgdGhlb3JlbSBhbmQgaXMgYWxtb3N0IGFsd2F5cyBpbnRyYWN0YWJsZSBmb3IgY29tcGxleCBtb2RlbHMg4oCUIHRoZSByb290IGNhdXNlIG9mIHdoeSBNQ01DIGFuZCB2YXJpYXRpb25hbCBpbmZlcmVuY2UgYXJlIG5lZWRlZC4gQ29tcHV0aW5nIHAoeCkgZWZmaWNpZW50bHkgaXMgdGhlIGNlbnRyYWwgY2hhbGxlbmdlIG9mIHByb2JhYmlsaXN0aWMgTUwuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQmF5ZXMnIFRoZW9yZW0ifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJGcm9tIHRoZSBwcm9kdWN0IHJ1bGUsIFAoQSDiiKkgQikgPSBQKEJ8QSkgw5cgUChBKSA9IFAoQXxCKSDDlyBQKEIpLiBTb2x2aW5nIGZvciBQKEF8Qik6XG5cblAoQXxCKSA9IFAoQnxBKSDDlyBQKEEpIC8gUChCKVxuXG5JbiBCYXllc2lhbiBNTCB3aXRoIHBhcmFtZXRlcnMgzrggYW5kIG9ic2VydmVkIGRhdGEgRDpcblxucCjOuHxEKSA9IHAoRHzOuCkgw5cgcCjOuCkgLyBwKEQpXG5cbndoZXJlOlxuLSBQcmlvciBwKM64KTogYmVsaWVmcyBhYm91dCDOuCBiZWZvcmUgc2VlaW5nIGRhdGEg4oCUIGVuY29kZXMgcmVndWxhcmlzYXRpb24gYW5kIGRvbWFpbiBrbm93bGVkZ2Vcbi0gTGlrZWxpaG9vZCBwKER8zrgpOiBwcm9iYWJpbGl0eSBvZiB0aGUgZGF0YSB1bmRlciBlYWNoIHNldHRpbmcgb2Ygzrgg4oCUIHRoZSByb2xlIG9mIHRoZSBtb2RlbFxuLSBQb3N0ZXJpb3IgcCjOuHxEKTogdXBkYXRlZCBiZWxpZWZzIGFmdGVyIG9ic2VydmluZyBEIOKAlCB0aGUgdGFyZ2V0IG9mIEJheWVzaWFuIGluZmVyZW5jZVxuLSBFdmlkZW5jZSBwKEQpID0g4oirIHAoRHzOuCkgcCjOuCkgZM64OiBub3JtYWxpc2luZyBjb25zdGFudCwgaW5kZXBlbmRlbnQgb2YgzrhcblxuQmVjYXVzZSBwKEQpIGRvZXMgbm90IGRlcGVuZCBvbiDOuDogcCjOuHxEKSDiiJ0gcChEfM64KSDDlyBwKM64KS4gVGhlIHBvc3RlcmlvciBpcyBwcm9wb3J0aW9uYWwgdG8gbGlrZWxpaG9vZCDDlyBwcmlvci4gTUFQIGVzdGltYXRpb24sIE1DTUMsIGFuZCB2YXJpYXRpb25hbCBpbmZlcmVuY2UgYWxsIGV4cGxvaXQgdGhpcyBwcm9wb3J0aW9uYWxpdHkuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWJcbm1hdHBsb3RsaWIudXNlKCdBZ2cnKSAgIyBub24taW50ZXJhY3RpdmVcblxuZGVmIGJheWVzX2RpYWdub3N0aWMocHJldmFsZW5jZSwgc2Vuc2l0aXZpdHksIHNwZWNpZmljaXR5KTpcbiAgICBcIlwiXCJcbiAgICBDb21wdXRlIFAoZGlzZWFzZSB8IHBvc2l0aXZlIHRlc3QpIHVzaW5nIEJheWVzJyB0aGVvcmVtLlxuICAgIHNlbnNpdGl2aXR5ID0gUCgrIHwgZGlzZWFzZSksIHNwZWNpZmljaXR5ID0gUCgtIHwgaGVhbHRoeSkuXG4gICAgXCJcIlwiXG4gICAgZnBfcmF0ZSA9IDEgLSBzcGVjaWZpY2l0eSAgICAgICAgICAgICMgUCgrIHwgaGVhbHRoeSlcbiAgICAjIExhdyBvZiB0b3RhbCBwcm9iYWJpbGl0eTogUCgrKSA9IFAoK3xEKVAoRCkgKyBQKCt8SClQKEgpXG4gICAgcF9wb3MgICA9IHNlbnNpdGl2aXR5ICogcHJldmFsZW5jZSArIGZwX3JhdGUgKiAoMSAtIHByZXZhbGVuY2UpXG4gICAgcHB2ICAgICA9IChzZW5zaXRpdml0eSAqIHByZXZhbGVuY2UpIC8gcF9wb3MgICAjIHBvc2l0aXZlIHByZWRpY3RpdmUgdmFsdWVcbiAgICByZXR1cm4gcHB2LCBwX3Bvc1xuXG4jIEJhc2UgcmF0ZSBuZWdsZWN0IGV4YW1wbGVcbnByaW50KFwiPT09IEJhc2UgUmF0ZSBFZmZlY3QgKHRlc3Q6IDk5JSBzZW5zLCA5OSUgc3BlYykgPT09XCIpXG5mb3IgcHJldiBpbiBbMC4wMDEsIDAuMDEsIDAuMDUsIDAuMTAsIDAuNTBdOlxuICAgIHBwdiwgcF9wb3MgPSBiYXllc19kaWFnbm9zdGljKHByZXYsIHNlbnNpdGl2aXR5PTAuOTksIHNwZWNpZmljaXR5PTAuOTkpXG4gICAgcHJpbnQoZlwiICBQcmV2YWxlbmNlIHtwcmV2Oi4zZn06IFAoZGlzZWFzZXwrKSA9IHtwcHY6LjRmfSAgW1AoKykgPSB7cF9wb3M6LjRmfV1cIilcblxuIyBCYXllc2lhbiBjb2luIGZsaXA6IHVwZGF0ZSBwcmlvciBhcyBkYXRhIGFycml2ZXNcbnByaW50KFwiXFxuPT09IEJheWVzaWFuIENvaW4gRmxpcCA9PT1cIilcbiMgQmV0YShhLGIpIGlzIGNvbmp1Z2F0ZSBwcmlvciBmb3IgQmVybm91bGxpXG4jIFBvc3RlcmlvciBhZnRlciBzZWVpbmcgayBoZWFkcywgbi1rIHRhaWxzOiBCZXRhKGEraywgYituLWspXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBiZXRhIGFzIGJldGFfZGlzdFxuXG5hLCBiID0gMi4wLCAyLjAgICAjIHN5bW1ldHJpYyBwcmlvciAoc2xpZ2h0IGJpYXMgdG93YXJkIGZhaXJuZXNzKVxuZmxpcHMgPSBbMSwwLDEsMSwwLDEsMSwxLDAsMV0gICMgSD0xLCBUPTBcbnByaW50KGZcIlByaW9yOiBCZXRhKHthfSwge2J9KSAgbWVhbj17YS8oYStiKTouM2Z9XCIpXG5mb3IgaSwgZmxpcCBpbiBlbnVtZXJhdGUoZmxpcHMsIDEpOlxuICAgIGEgKz0gZmxpcDsgYiArPSAoMSAtIGZsaXApXG4gICAgcG9zdF9tZWFuID0gYSAvIChhICsgYilcbiAgICBjaV9sbywgY2lfaGkgPSBiZXRhX2Rpc3QucHBmKFswLjAyNSwgMC45NzVdLCBhLCBiKVxuICAgIHByaW50KGZcIiAgQWZ0ZXIgZmxpcCB7aToyZH0gKD17J0gnIGlmIGZsaXAgZWxzZSAnVCd9KTogQmV0YSh7YTouMGZ9LHtiOi4wZn0pICBcIlxuICAgICAgICAgIGZcIm1lYW49e3Bvc3RfbWVhbjouM2Z9ICA5NSVDST1be2NpX2xvOi4zZn0sIHtjaV9oaTouM2Z9XVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkJhc2UgUmF0ZSBOZWdsZWN0In0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQmFzZSByYXRlIG5lZ2xlY3QgaXMgdGhlIGNvZ25pdGl2ZSBiaWFzIG9mIGlnbm9yaW5nIHRoZSBwcmlvciBQKEQpIHdoZW4gaW50ZXJwcmV0aW5nIGNvbmRpdGlvbmFsIHByb2JhYmlsaXRpZXMuIEEgY2xhc3NpYyBleGFtcGxlOiBhIGRpc2Vhc2UgdGVzdCB3aXRoIDk5JSBzZW5zaXRpdml0eSBhbmQgOTklIHNwZWNpZmljaXR5IGFwcGxpZWQgdG8gYSBwb3B1bGF0aW9uIHdpdGggMC4xJSBkaXNlYXNlIHByZXZhbGVuY2UuXG5cblAoZGlzZWFzZSB8IHBvc2l0aXZlIHRlc3QpID0gUCgrfGRpc2Vhc2UpIMOXIFAoZGlzZWFzZSkgLyBQKCspXG49ICgwLjk5IMOXIDAuMDAxKSAvICgwLjk5IMOXIDAuMDAxICsgMC4wMSDDlyAwLjk5OSlcbj0gMC4wMDA5OSAvICgwLjAwMDk5ICsgMC4wMDk5OSlcbuKJiCAwLjA5MFxuXG5EZXNwaXRlIGEgOTklLWFjY3VyYXRlIHRlc3QsIGEgcG9zaXRpdmUgcmVzdWx0IG1lYW5zIG9ubHkgfjklIGNoYW5jZSBvZiBhY3R1YWxseSBoYXZpbmcgdGhlIGRpc2Vhc2UuIFRoZSBsb3cgYmFzZSByYXRlIGRvbWluYXRlcyBiZWNhdXNlIHRoZXJlIGFyZSBzbyBtYW55IG1vcmUgaGVhbHRoeSBwZW9wbGUgZ2VuZXJhdGluZyBmYWxzZSBwb3NpdGl2ZXMgdGhhbiBzaWNrIHBlb3BsZSBnZW5lcmF0aW5nIHRydWUgcG9zaXRpdmVzLlxuXG5UaGlzIGZhaWx1cmUgbW9kZSBhcHBlYXJzIGluIE1MOiBjbGFzc2lmaWVyIHByZWNpc2lvbiBpcyBoZWF2aWx5IGluZmx1ZW5jZWQgYnkgY2xhc3MgaW1iYWxhbmNlLiBBIG1vZGVsIHdpdGggOTklIGFjY3VyYWN5IG9uIGEgZGF0YXNldCB3aXRoIDElIHBvc2l0aXZlIHJhdGUgbWF5IHNpbXBseSBiZSBwcmVkaWN0aW5nICduZWdhdGl2ZScgZm9yIGV2ZXJ5dGhpbmcuIEFsd2F5cyBjaGVjayBwcmVjaXNpb24tcmVjYWxsIGN1cnZlcyBhbmQgRjEgc2NvcmVzLCBub3QganVzdCBhY2N1cmFjeS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubmFpdmVfYmF5ZXMgaW1wb3J0IEdhdXNzaWFuTkJcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGNsYXNzaWZpY2F0aW9uX3JlcG9ydFxuXG4jIE5haXZlIEJheWVzIGNsYXNzaWZpZXIgZnJvbSBzY3JhdGNoXG5jbGFzcyBOYWl2ZUJheWVzQ2xhc3NpZmllcjpcbiAgICBcIlwiXCJHYXVzc2lhbiBOYWl2ZSBCYXllczogYXNzdW1lcyBmZWF0dXJlcyB+IE4obXVfYywgc2lnbWFfYykgZ2l2ZW4gY2xhc3MgYy5cIlwiXCJcbiAgICBkZWYgZml0KHNlbGYsIFgsIHkpOlxuICAgICAgICBzZWxmLmNsYXNzZXNfID0gbnAudW5pcXVlKHkpXG4gICAgICAgIHNlbGYubG9nX3ByaW9yc18gPSB7fVxuICAgICAgICBzZWxmLm1lYW5zXyA9IHt9XG4gICAgICAgIHNlbGYuc3Rkc18gID0ge31cbiAgICAgICAgZm9yIGMgaW4gc2VsZi5jbGFzc2VzXzpcbiAgICAgICAgICAgIFhjID0gWFt5ID09IGNdXG4gICAgICAgICAgICBzZWxmLmxvZ19wcmlvcnNfW2NdID0gbnAubG9nKGxlbihYYykgLyBsZW4oWCkpXG4gICAgICAgICAgICBzZWxmLm1lYW5zX1tjXSAgICAgID0gWGMubWVhbihheGlzPTApXG4gICAgICAgICAgICBzZWxmLnN0ZHNfW2NdICAgICAgID0gWGMuc3RkKGF4aXM9MCkgKyAxZS05ICAjIHN0YWJpbGl0eVxuICAgICAgICByZXR1cm4gc2VsZlxuXG4gICAgZGVmIGxvZ19saWtlbGlob29kKHNlbGYsIFgsIGMpOlxuICAgICAgICBcIlwiXCJsb2cgUChYIHwgY2xhc3M9YykgYXNzdW1pbmcgY29uZGl0aW9uYWwgaW5kZXBlbmRlbmNlLlwiXCJcIlxuICAgICAgICBtdSwgc2lnbWEgPSBzZWxmLm1lYW5zX1tjXSwgc2VsZi5zdGRzX1tjXVxuICAgICAgICByZXR1cm4gbnAuc3VtKC0wLjUgKiAoKFggLSBtdSkgLyBzaWdtYSkqKjIgLSBucC5sb2coc2lnbWEpIC0gMC41Km5wLmxvZygyKm5wLnBpKSwgYXhpcz0xKVxuXG4gICAgZGVmIHByZWRpY3Qoc2VsZiwgWCk6XG4gICAgICAgIGxvZ19wb3N0cyA9IG5wLmNvbHVtbl9zdGFjayhbXG4gICAgICAgICAgICBzZWxmLmxvZ19wcmlvcnNfW2NdICsgc2VsZi5sb2dfbGlrZWxpaG9vZChYLCBjKSBmb3IgYyBpbiBzZWxmLmNsYXNzZXNfXG4gICAgICAgIF0pXG4gICAgICAgIHJldHVybiBzZWxmLmNsYXNzZXNfW25wLmFyZ21heChsb2dfcG9zdHMsIGF4aXM9MSldXG5cbiMgVGVzdCBvbiBzeW50aGV0aWMgZGF0YVxuWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24obl9zYW1wbGVzPTUwMCwgbl9mZWF0dXJlcz00LCBuX2NsYXNzZXM9MiwgcmFuZG9tX3N0YXRlPTQyKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxuXG5uYiA9IE5haXZlQmF5ZXNDbGFzc2lmaWVyKCkuZml0KFhfdHIsIHlfdHIpXG5hY2MgPSBucC5tZWFuKG5iLnByZWRpY3QoWF90ZSkgPT0geV90ZSlcbnByaW50KGZcIkN1c3RvbSBOQiBhY2N1cmFjeToge2FjYzouNGZ9XCIpXG5cbiMgQ29tcGFyZSB3aXRoIHNrbGVhcm5cbnNrX25iID0gR2F1c3NpYW5OQigpLmZpdChYX3RyLCB5X3RyKVxucHJpbnQoZlwic2tsZWFybiBOQiBhY2N1cmFjeToge3NrX25iLnNjb3JlKFhfdGUsIHlfdGUpOi40Zn1cIilcbnByaW50KFwiXFxuXCIgKyBjbGFzc2lmaWNhdGlvbl9yZXBvcnQoeV90ZSwgbmIucHJlZGljdChYX3RlKSkpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQmF5ZXMgYXMgdGhlIEVuZ2luZSBvZiBNTCJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlZpcnR1YWxseSBldmVyeSBNTCBhbGdvcml0aG0gY2FuIGJlIGludGVycHJldGVkIHRocm91Z2ggdGhlIEJheWVzaWFuIGxlbnM6XG5cbi0gTUxFIC8gbG9naXN0aWMgcmVncmVzc2lvbjogbWF4aW1pc2UgcChEfM64KSDigJQgaW1wbGljaXQgdW5pZm9ybSBwcmlvclxuLSBSaWRnZSByZWdyZXNzaW9uIChMMik6IE1BUCB3aXRoIEdhdXNzaWFuIHByaW9yIE4oMCwgz4PCskkpIG9uIHdlaWdodHMg4oaSIGxvZyBwKM64KSA9IOKIkuKAls644oCWwrIvKDLPg8KyKVxuLSBMYXNzbyAoTDEpOiBNQVAgd2l0aCBMYXBsYWNlIHByaW9yIG9uIHdlaWdodHMg4oaSIGxvZyBwKM64KSA9IOKIks674oCWzrjigJbigoFcbi0gTmFpdmUgQmF5ZXM6IGRpcmVjdGx5IGFwcGxpZXMgQmF5ZXMnIHRoZW9yZW0gd2l0aCBjb25kaXRpb25hbCBpbmRlcGVuZGVuY2UgYXNzdW1wdGlvblxuLSBHYXVzc2lhbiBwcm9jZXNzZXM6IEJheWVzaWFuIGluZmVyZW5jZSBvdmVyIGZ1bmN0aW9ucyDigJQgcG9zdGVyaW9yIGlzIGFsc28gYSBHUFxuLSBWQUVzOiBhbW9ydGlzZWQgdmFyaWF0aW9uYWwgYXBwcm94aW1hdGlvbiB0byBCYXllc2lhbiBwb3N0ZXJpb3IgcCh6fHgpXG4tIERpZmZ1c2lvbiBtb2RlbHM6IHJldmVyc2UgcHJvY2VzcyBpcyBhIGxlYXJuZWQgcG9zdGVyaW9yIG92ZXIgZGVub2lzaW5nIHN0ZXBzXG5cblRoZSBCYXllc2lhbiBmcmFtZXdvcmsgc3VwcGxpZXMgdGhlIHByaW5jaXBsZWQgdm9jYWJ1bGFyeSBmb3IgdW5jZXJ0YWludHkgcXVhbnRpZmljYXRpb24sIHJlZ3VsYXJpc2F0aW9uLWFzLXByaW9yLCBtb2RlbCBjb21wYXJpc29uIChtYXJnaW5hbCBsaWtlbGlob29kKSwgYW5kIHRoZSBkZXNpZ24gb2YgaW5mZXJlbmNlIGFsZ29yaXRobXMuIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInZhcmlhbnQiOiAid2FybmluZyIsICJ0aXRsZSI6ICJCYXllc2lhbiB2cyBGcmVxdWVudGlzdCBJbnRlcnByZXRhdGlvbiIsICJjb250ZW50IjogIkZyZXF1ZW50aXN0cyB0cmVhdCDOuCBhcyBhIGZpeGVkIHVua25vd247IHByb2JhYmlsaXR5IG1lYW5zIGxvbmctcnVuIGZyZXF1ZW5jeS4gQmF5ZXNpYW5zIHRyZWF0IM64IGFzIHJhbmRvbTsgcHJvYmFiaWxpdHkgZW5jb2RlcyBkZWdyZWVzIG9mIGJlbGllZi4gTmVpdGhlciBpcyB1bml2ZXJzYWxseSBjb3JyZWN0LiBGcmVxdWVudGlzdCBtZXRob2RzIGFyZSBvZnRlbiBzaW1wbGVyIGFuZCBtb3JlIGludGVycHJldGFibGUgZm9yIGxhcmdlIGRhdGFzZXRzLiBCYXllc2lhbiBtZXRob2RzIGV4Y2VsIHdoZW4gZGF0YSBpcyBzY2FyY2UsIHByaW9yIGtub3dsZWRnZSBpcyBzdHJvbmcsIG9yIGNhbGlicmF0ZWQgdW5jZXJ0YWludHkgZXN0aW1hdGVzIGFyZSByZXF1aXJlZCAobWVkaWNhbCBkaWFnbm9zaXMsIHNhZmV0eS1jcml0aWNhbCBzeXN0ZW1zLCBhY3RpdmUgbGVhcm5pbmcpLiJ9LCB7InR5cGUiOiAidGFibGUiLCAiaGVhZGVycyI6IFsiTUwgTWV0aG9kIiwgIkJheWVzaWFuIEludGVycHJldGF0aW9uIiwgIlByaW9yIEltcGxpZWQiXSwgInJvd3MiOiBbWyJNTEUiLCAiTWF4aW1pc2UgcChEfM64KSIsICJVbmlmb3JtIChpbXByb3BlcikiXSwgWyJSaWRnZSByZWdyZXNzaW9uIiwgIk1BUCB3aXRoIEdhdXNzaWFuIHByaW9yIiwgIk4oMCwgz4PCskkpIG9uIHdlaWdodHMiXSwgWyJMYXNzbyIsICJNQVAgd2l0aCBMYXBsYWNlIHByaW9yIiwgIkxhcGxhY2UoMCwgMS/Ouykgb24gd2VpZ2h0cyJdLCBbIk5haXZlIEJheWVzIiwgIkRpcmVjdCBCYXllcyB3aXRoIGNvbmQuIGluZGVwZW5kZW5jZSIsICJDbGFzcy1jb25kaXRpb25hbCBHYXVzc2lhbiJdLCBbIkdhdXNzaWFuIFByb2Nlc3MiLCAiRnVsbCBwb3N0ZXJpb3Igb3ZlciBmdW5jdGlvbnMiLCAiR1AgcHJpb3Igb24gZiJdLCBbIlZBRSIsICJWYXJpYXRpb25hbCBwb3N0ZXJpb3IgcSh6fHgpIOKJiCBwKHp8eCkiLCAiSXNvdHJvcGljIEdhdXNzaWFuIG9uIHoiXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAib3JkZXJlZCI6IGZhbHNlLCAiaXRlbXMiOiBbIlRoZSB0aHJlZSBLb2xtb2dvcm92IGF4aW9tcyAobm9uLW5lZ2F0aXZpdHksIG5vcm1hbGlzYXRpb24sIGNvdW50YWJsZSBhZGRpdGl2aXR5KSBnZW5lcmF0ZSBhbGwgcHJvYmFiaWxpdHkgdGhlb3J5IGFzIHRoZW9yZW1zLiIsICJDb25kaXRpb25hbCBwcm9iYWJpbGl0eSBQKEF8QikgPSBQKEHiiKlCKS9QKEIpIHJlc3RyaWN0cyBhbmQgcmVub3JtYWxpc2VzIHRoZSBzYW1wbGUgc3BhY2U7IHRoZSBwcm9kdWN0IHJ1bGUgUChB4oipQikgPSBQKEF8QilQKEIpIGlzIGl0cyBkaXJlY3QgcmV3cml0ZS4iLCAiSW5kZXBlbmRlbmNlIFAoQeKIqUIpID0gUChBKVAoQikgaW1wbGllcyB6ZXJvIGNvdmFyaWFuY2UsIGJ1dCB6ZXJvIGNvdmFyaWFuY2Ugb25seSBpbXBsaWVzIGluZGVwZW5kZW5jZSBmb3Igam9pbnRseSBHYXVzc2lhbiB2YXJpYWJsZXMuIiwgIlRoZSBsYXcgb2YgdG90YWwgcHJvYmFiaWxpdHkgUChBKSA9IM6j4bWiIFAoQXxC4bWiKVAoQuG1oikgYW5kIGl0cyBjb250aW51b3VzIGZvcm0gKG1hcmdpbmFsaXNhdGlvbikgZXhwbGFpbiB3aHkgZXZpZGVuY2UgcChEKSA9IOKIq3AoRHzOuClwKM64KWTOuCBpcyBpbnRyYWN0YWJsZSBmb3IgY29tcGxleCBtb2RlbHMuIiwgIkJheWVzJyB0aGVvcmVtIHAozrh8RCkg4oidIHAoRHzOuClwKM64KSBpcyB0aGUgZm91bmRhdGlvbiBvZiBhbGwgQmF5ZXNpYW4gTUw6IHRoZSBwcmlvciBlbmNvZGVzIHJlZ3VsYXJpc2F0aW9uLCB0aGUgbGlrZWxpaG9vZCBlbmNvZGVzIHRoZSBtb2RlbCwgdGhlIHBvc3RlcmlvciBlbmNvZGVzIHVwZGF0ZWQgYmVsaWVmcy4iLCAiQmFzZSByYXRlIG5lZ2xlY3Qg4oCUIGlnbm9yaW5nIHRoZSBwcmlvciDigJQgaXMgYSBzeXN0ZW1hdGljIGNvZ25pdGl2ZSBiaWFzIHRoYXQgaW5mbGF0ZXMgY29uZmlkZW5jZSBpbiBwb3NpdGl2ZSB0ZXN0IHJlc3VsdHMgZm9yIHJhcmUgZXZlbnRzOyBpdCBtYW5pZmVzdHMgaW4gTUwgYXMgaWdub3JpbmcgY2xhc3MgaW1iYWxhbmNlLiIsICJSZWd1bGFyaXNhdGlvbiBpbiBkZWVwIGxlYXJuaW5nIGlzIE1BUCBlc3RpbWF0aW9uIHVuZGVyIGEgcHJpb3I6IEwyIHJlZ3VsYXJpc2F0aW9uID0gR2F1c3NpYW4gcHJpb3IsIEwxIHJlZ3VsYXJpc2F0aW9uID0gTGFwbGFjZSBwcmlvci4iXX1d"
---
# Probability Axioms, Bayes' Theorem, and Conditional Probability

Probability theory is the mathematical language for quantifying uncertainty — indispensable for any ML practitioner. Andrey Kolmogorov's 1933 axiomatisation put probability on rigorous measure-theoretic foundations. Everything from Bayesian networks to diffusion models derives from three deceptively simple axioms. This note develops the full chain: from axioms to conditional probability, independence, the law of total probability, Bayes' theorem, base rate neglect, and finally the Bayesian interpretation of regularisation, MAP estimation, and prior design that underlies modern ML theory.

## Kolmogorov Axioms

Let Ω be a sample space (all possible outcomes), and let F be a σ-algebra of events (measurable subsets of Ω). A probability measure P: F → [0,1] must satisfy three axioms:

1. Non-negativity: P(A) ≥ 0 for every event A ∈ F
2. Normalization: P(Ω) = 1 (something must happen)
3. Countable additivity: For any countable sequence of mutually exclusive events A₁, A₂, …: P(⋃ᵢ Aᵢ) = Σᵢ P(Aᵢ)

All probability rules are theorems derived from these axioms alone:
- P(∅) = 0 (derived from axiom 3 with all empty events)
- P(Aᶜ) = 1 − P(A) (derived from axioms 2 and 3)
- P(A ∪ B) = P(A) + P(B) − P(A ∩ B) (inclusion-exclusion)
- If A ⊆ B then P(A) ≤ P(B) (monotonicity)

The σ-algebra requirement ensures we can take complements and countable unions of measurable events, sidestepping non-measurable set paradoxes (e.g., Banach-Tarski) that arise in continuous spaces.

> **INFO: Why σ-algebras matter for ML**
>
> For finite sample spaces every subset is trivially measurable. For continuous spaces (Ω = ℝ) we restrict to Borel sets to avoid non-measurable pathologies. In ML practice the σ-algebra is invisible, but it is why we can rigorously talk about P(X ≤ x) for a continuous random variable X — this defines the CDF, from which PDFs and expectations follow.

## Conditional Probability

The conditional probability of A given B (with P(B) > 0) is defined as:

P(A|B) = P(A ∩ B) / P(B)

Interpretation: restrict the sample space to event B and renormalize. Conditional probability is itself a valid probability measure on Ω restricted to B — all three Kolmogorov axioms hold.

Product rule (the definition rewritten):

P(A ∩ B) = P(A|B) × P(B) = P(B|A) × P(A)

This simple rewrite — equating two ways to factor the joint probability — is the algebraic heart of Bayes' theorem. The chain rule extends this to n events:

P(A₁ ∩ A₂ ∩ … ∩ Aₙ) = P(A₁) × P(A₂|A₁) × P(A₃|A₁,A₂) × … × P(Aₙ|A₁,…,Aₙ₋₁)

This factorisation is the foundation of autoregressive language models: p(x₁,…,xₙ) = Πₜ p(xₜ|x₁,…,xₜ₋₁).

## Statistical Independence

Events A and B are statistically independent if:

P(A ∩ B) = P(A) × P(B),  equivalently P(A|B) = P(A)

Knowing B carries zero information about A. Independence is symmetric: A ⊥ B iff B ⊥ A.

Conditional independence: A ⊥ B | C means P(A ∩ B | C) = P(A|C) × P(B|C). Naive Bayes assumes features X₁, …, Xd are conditionally independent given class Y — a strong assumption that reduces parameter count from O(|𝒳|^d) to O(d × |𝒳|) and makes training tractable.

Critical distinction: independence implies zero covariance, but zero covariance does NOT imply independence in general. The exception is jointly Gaussian random variables, where uncorrelated ⟺ independent. This is why the Gaussian is central to so much probabilistic ML — it is the only distribution where second-order statistics fully characterise dependence structure.

```python
import numpy as np
from scipy import stats

# Verify Kolmogorov axioms with empirical probabilities
rng = np.random.default_rng(42)
n_trials = 100_000
die = rng.integers(1, 7, size=n_trials)   # fair 6-sided die

P_even = np.mean(die % 2 == 0)
P_gt3  = np.mean(die > 3)
P_both = np.mean((die % 2 == 0) & (die > 3))   # even AND > 3: {4, 6}
P_either = np.mean((die % 2 == 0) | (die > 3)) # even OR > 3: {2,4,5,6}

print("=== Kolmogorov Axiom Verification ===")
print(f"P(even) = {P_even:.4f}  (expected 0.5)")
print(f"P(>3)   = {P_gt3:.4f}  (expected 0.5)")
print(f"P(even AND >3) = {P_both:.4f}  (expected 0.3333 = {2/6:.4f})")
print(f"Inclusion-exclusion: P(e)+P(g)-P(e&g) = {P_even+P_gt3-P_both:.4f}")
print(f"P(even OR >3)       = {P_either:.4f}  (match: {P_even+P_gt3-P_both:.4f})")

# Conditional probability: P(>3 | even)
P_gt3_given_even = P_both / P_even
print(f"\nP(>3 | even) = P(both)/P(even) = {P_gt3_given_even:.4f}  (expected 0.6667)")

# Independence test: are 'even' and '>3' independent?
print(f"\nIndependence check: P(e)*P(g) = {P_even*P_gt3:.4f}  vs P(e&g) = {P_both:.4f}")
print(f"Independent? {np.isclose(P_even * P_gt3, P_both, atol=0.01)}")  # No

# Generate independent vs dependent examples
x = rng.standard_normal(10000)
y_dep = x + 0.5 * rng.standard_normal(10000)   # dependent on x
y_ind = rng.standard_normal(10000)               # independent of x
print(f"\nCorr(x, y_dep) = {np.corrcoef(x, y_dep)[0,1]:.4f}")
print(f"Corr(x, y_ind) = {np.corrcoef(x, y_ind)[0,1]:.4f}")
```

## Law of Total Probability

If {B₁, B₂, …, Bₙ} is a partition of Ω (mutually exclusive and exhaustive events), then:

P(A) = Σᵢ P(A | Bᵢ) × P(Bᵢ)

In continuous form (marginalisation over a latent variable z):

p(x) = ∫ p(x | z) × p(z) dz

This integral is the marginal likelihood or evidence in Bayesian models. It appears in the denominator of Bayes' theorem and is almost always intractable for complex models — the root cause of why MCMC and variational inference are needed. Computing p(x) efficiently is the central challenge of probabilistic ML.

## Bayes' Theorem

From the product rule, P(A ∩ B) = P(B|A) × P(A) = P(A|B) × P(B). Solving for P(A|B):

P(A|B) = P(B|A) × P(A) / P(B)

In Bayesian ML with parameters θ and observed data D:

p(θ|D) = p(D|θ) × p(θ) / p(D)

where:
- Prior p(θ): beliefs about θ before seeing data — encodes regularisation and domain knowledge
- Likelihood p(D|θ): probability of the data under each setting of θ — the role of the model
- Posterior p(θ|D): updated beliefs after observing D — the target of Bayesian inference
- Evidence p(D) = ∫ p(D|θ) p(θ) dθ: normalising constant, independent of θ

Because p(D) does not depend on θ: p(θ|D) ∝ p(D|θ) × p(θ). The posterior is proportional to likelihood × prior. MAP estimation, MCMC, and variational inference all exploit this proportionality.

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')  # non-interactive

def bayes_diagnostic(prevalence, sensitivity, specificity):
    """
    Compute P(disease | positive test) using Bayes' theorem.
    sensitivity = P(+ | disease), specificity = P(- | healthy).
    """
    fp_rate = 1 - specificity            # P(+ | healthy)
    # Law of total probability: P(+) = P(+|D)P(D) + P(+|H)P(H)
    p_pos   = sensitivity * prevalence + fp_rate * (1 - prevalence)
    ppv     = (sensitivity * prevalence) / p_pos   # positive predictive value
    return ppv, p_pos

# Base rate neglect example
print("=== Base Rate Effect (test: 99% sens, 99% spec) ===")
for prev in [0.001, 0.01, 0.05, 0.10, 0.50]:
    ppv, p_pos = bayes_diagnostic(prev, sensitivity=0.99, specificity=0.99)
    print(f"  Prevalence {prev:.3f}: P(disease|+) = {ppv:.4f}  [P(+) = {p_pos:.4f}]")

# Bayesian coin flip: update prior as data arrives
print("\n=== Bayesian Coin Flip ===")
# Beta(a,b) is conjugate prior for Bernoulli
# Posterior after seeing k heads, n-k tails: Beta(a+k, b+n-k)
from scipy.stats import beta as beta_dist

a, b = 2.0, 2.0   # symmetric prior (slight bias toward fairness)
flips = [1,0,1,1,0,1,1,1,0,1]  # H=1, T=0
print(f"Prior: Beta({a}, {b})  mean={a/(a+b):.3f}")
for i, flip in enumerate(flips, 1):
    a += flip; b += (1 - flip)
    post_mean = a / (a + b)
    ci_lo, ci_hi = beta_dist.ppf([0.025, 0.975], a, b)
    print(f"  After flip {i:2d} (={'H' if flip else 'T'}): Beta({a:.0f},{b:.0f})  "
          f"mean={post_mean:.3f}  95%CI=[{ci_lo:.3f}, {ci_hi:.3f}]")
```

## Base Rate Neglect

Base rate neglect is the cognitive bias of ignoring the prior P(D) when interpreting conditional probabilities. A classic example: a disease test with 99% sensitivity and 99% specificity applied to a population with 0.1% disease prevalence.

P(disease | positive test) = P(+|disease) × P(disease) / P(+)
= (0.99 × 0.001) / (0.99 × 0.001 + 0.01 × 0.999)
= 0.00099 / (0.00099 + 0.00999)
≈ 0.090

Despite a 99%-accurate test, a positive result means only ~9% chance of actually having the disease. The low base rate dominates because there are so many more healthy people generating false positives than sick people generating true positives.

This failure mode appears in ML: classifier precision is heavily influenced by class imbalance. A model with 99% accuracy on a dataset with 1% positive rate may simply be predicting 'negative' for everything. Always check precision-recall curves and F1 scores, not just accuracy.

```python
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Naive Bayes classifier from scratch
class NaiveBayesClassifier:
    """Gaussian Naive Bayes: assumes features ~ N(mu_c, sigma_c) given class c."""
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.log_priors_ = {}
        self.means_ = {}
        self.stds_  = {}
        for c in self.classes_:
            Xc = X[y == c]
            self.log_priors_[c] = np.log(len(Xc) / len(X))
            self.means_[c]      = Xc.mean(axis=0)
            self.stds_[c]       = Xc.std(axis=0) + 1e-9  # stability
        return self

    def log_likelihood(self, X, c):
        """log P(X | class=c) assuming conditional independence."""
        mu, sigma = self.means_[c], self.stds_[c]
        return np.sum(-0.5 * ((X - mu) / sigma)**2 - np.log(sigma) - 0.5*np.log(2*np.pi), axis=1)

    def predict(self, X):
        log_posts = np.column_stack([
            self.log_priors_[c] + self.log_likelihood(X, c) for c in self.classes_
        ])
        return self.classes_[np.argmax(log_posts, axis=1)]

# Test on synthetic data
X, y = make_classification(n_samples=500, n_features=4, n_classes=2, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

nb = NaiveBayesClassifier().fit(X_tr, y_tr)
acc = np.mean(nb.predict(X_te) == y_te)
print(f"Custom NB accuracy: {acc:.4f}")

# Compare with sklearn
sk_nb = GaussianNB().fit(X_tr, y_tr)
print(f"sklearn NB accuracy: {sk_nb.score(X_te, y_te):.4f}")
print("\n" + classification_report(y_te, nb.predict(X_te)))
```

## Bayes as the Engine of ML

Virtually every ML algorithm can be interpreted through the Bayesian lens:

- MLE / logistic regression: maximise p(D|θ) — implicit uniform prior
- Ridge regression (L2): MAP with Gaussian prior N(0, σ²I) on weights → log p(θ) = −‖θ‖²/(2σ²)
- Lasso (L1): MAP with Laplace prior on weights → log p(θ) = −λ‖θ‖₁
- Naive Bayes: directly applies Bayes' theorem with conditional independence assumption
- Gaussian processes: Bayesian inference over functions — posterior is also a GP
- VAEs: amortised variational approximation to Bayesian posterior p(z|x)
- Diffusion models: reverse process is a learned posterior over denoising steps

The Bayesian framework supplies the principled vocabulary for uncertainty quantification, regularisation-as-prior, model comparison (marginal likelihood), and the design of inference algorithms.

> **WARNING: Bayesian vs Frequentist Interpretation**
>
> Frequentists treat θ as a fixed unknown; probability means long-run frequency. Bayesians treat θ as random; probability encodes degrees of belief. Neither is universally correct. Frequentist methods are often simpler and more interpretable for large datasets. Bayesian methods excel when data is scarce, prior knowledge is strong, or calibrated uncertainty estimates are required (medical diagnosis, safety-critical systems, active learning).

| ML Method | Bayesian Interpretation | Prior Implied |
| --- | --- | --- |
| MLE | Maximise p(D|θ) | Uniform (improper) |
| Ridge regression | MAP with Gaussian prior | N(0, σ²I) on weights |
| Lasso | MAP with Laplace prior | Laplace(0, 1/λ) on weights |
| Naive Bayes | Direct Bayes with cond. independence | Class-conditional Gaussian |
| Gaussian Process | Full posterior over functions | GP prior on f |
| VAE | Variational posterior q(z|x) ≈ p(z|x) | Isotropic Gaussian on z |

---

## Key Takeaways

- The three Kolmogorov axioms (non-negativity, normalisation, countable additivity) generate all probability theory as theorems.
- Conditional probability P(A|B) = P(A∩B)/P(B) restricts and renormalises the sample space; the product rule P(A∩B) = P(A|B)P(B) is its direct rewrite.
- Independence P(A∩B) = P(A)P(B) implies zero covariance, but zero covariance only implies independence for jointly Gaussian variables.
- The law of total probability P(A) = Σᵢ P(A|Bᵢ)P(Bᵢ) and its continuous form (marginalisation) explain why evidence p(D) = ∫p(D|θ)p(θ)dθ is intractable for complex models.
- Bayes' theorem p(θ|D) ∝ p(D|θ)p(θ) is the foundation of all Bayesian ML: the prior encodes regularisation, the likelihood encodes the model, the posterior encodes updated beliefs.
- Base rate neglect — ignoring the prior — is a systematic cognitive bias that inflates confidence in positive test results for rare events; it manifests in ML as ignoring class imbalance.
- Regularisation in deep learning is MAP estimation under a prior: L2 regularisation = Gaussian prior, L1 regularisation = Laplace prior.
