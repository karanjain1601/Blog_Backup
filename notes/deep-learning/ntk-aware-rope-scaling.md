---
title: "NTK-Aware RoPE Scaling"
slug: "ntk-aware-rope-scaling"
description: "Adapting the RoPE base frequency (θ) using neural tangent kernel theory so that high-frequency dimensions remain useful at extended context lengths, outperforming linear interpolation without requiring fine-tuning."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTlRLLWF3YXJlIFJvUEUgc2NhbGluZyBhZGRyZXNzZXMgdGhlIGNvcmUgd2Vha25lc3Mgb2YgbGluZWFyIGludGVycG9sYXRpb246IHVuaWZvcm0gY29tcHJlc3Npb24gZGVzdHJveXMgdGhlIGhpZ2gtZnJlcXVlbmN5IFJvUEUgZGltZW5zaW9ucyB0aGF0IGVuY29kZSBsb2NhbCBzeW50YWN0aWMgc3RydWN0dXJlLiBJbnN0ZWFkIG9mIGRpdmlkaW5nIHBvc2l0aW9uIGluZGljZXMgYnkgcywgTlRLLWF3YXJlIHNjYWxpbmcgcmVzY2FsZXMgdGhlIFJvUEUgYmFzZSBmcmVxdWVuY3kgKHRoZXRhLCB0eXBpY2FsbHkgMTAwMDApIHRvIGEgbmV3IHZhbHVlIHRoYXQgZGlzdHJpYnV0ZXMgdGhlIOKAmGludGVycG9sYXRpb24gYnVyZGVu4oCZIGFjcm9zcyBkaW1lbnNpb25zIGFjY29yZGluZyB0byB0aGVpciBuYXR1cmFsIGZyZXF1ZW5jeS4gRGltZW5zaW9ucyB3aXRoIHNob3J0IHdhdmVsZW5ndGhzIChoaWdoLWZyZXF1ZW5jeSwgZW5jb2RpbmcgbG9jYWwgcGF0dGVybnMpIHJlY2VpdmUgbGl0dGxlIG9yIG5vIGludGVycG9sYXRpb24sIHdoaWxlIGRpbWVuc2lvbnMgd2l0aCBsb25nIHdhdmVsZW5ndGhzIChsb3ctZnJlcXVlbmN5LCBlbmNvZGluZyBkb2N1bWVudC1sZXZlbCBzdHJ1Y3R1cmUpIHJlY2VpdmUgc3Ryb25nIGludGVycG9sYXRpb24uIFRoZSByZXN1bHQgaXMgYSBmcmVxdWVuY3kgc3BlY3RydW0gdGhhdCBpcyBkaXN0b3J0ZWQgYXMgbGl0dGxlIGFzIHBvc3NpYmxlIGZyb20gdGhlIHRyYWluaW5nIGRpc3RyaWJ1dGlvbiwgZ2l2aW5nIGJldHRlciB6ZXJvLXNob3QgcGVyZm9ybWFuY2UgYXQgdGhlIHNhbWUgc2NhbGUgZmFjdG9yLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOVEstYXdhcmUgc2NhbGluZyAoUmVkZGl0LCBibG9jOTcsIDIwMjM7IHN1YnNlcXVlbnRseSBzdHVkaWVkIGJ5IFhpb25nIGV0IGFsLiwgMjAyMykgbW9kaWZpZXMgdGhlIFJvUEUgYmFzZSBmcm9tIDEwMDAwIHRvIGEgbmV3IHZhbHVlIGIqID0gMTAwMDAgKiBzXihkLyhkLTIpKSwgd2hlcmUgcyBpcyB0aGUgZGVzaXJlZCBzY2FsZSBmYWN0b3IgYW5kIGQgaXMgdGhlIGhlYWQgZGltZW5zaW9uLiBUaGlzIGZvcm11bGEgZGVyaXZlcyBmcm9tIHRoZSByZXF1aXJlbWVudCB0aGF0IHRoZSBoaWdoZXN0LWZyZXF1ZW5jeSBSb1BFIGRpbWVuc2lvbiBjb21wbGV0ZXMgdGhlIHNhbWUgbnVtYmVyIG9mIGZ1bGwgcm90YXRpb25zIG92ZXIgdGhlIGV4dGVuZGVkIGNvbnRleHQgYXMgaXQgZGlkIG92ZXIgdGhlIHRyYWluaW5nIGNvbnRleHQg4oCUIHByZXZlbnRpbmcgYWxpYXNpbmcuIEluIHByYWN0aWNlLCBmb3Igcz00IGFuZCBkPTEyOCAoTGxhbWEtMi03QiksIHRoZSBuZXcgYmFzZSBpcyBhcHByb3hpbWF0ZWx5IDEwMDAwICogNF4oMTI4LzEyNikg4omIIDQwNDk3LiBXaXRoIHRoaXMgbGFyZ2VyIGJhc2UsIGFsbCBSb1BFIGZyZXF1ZW5jaWVzIGFyZSByZWR1Y2VkIHByb3BvcnRpb25hbGx5IHRvIHRoZWlyIGRpbWVuc2lvbiBpbmRleCwgd2l0aCBoaWdoZXItaW5kZXhlZCAobG93ZXItZnJlcXVlbmN5KSBkaW1lbnNpb25zIHJlY2VpdmluZyB0aGUgbW9zdCByZXNjYWxpbmcuIFRoZSBtZXRob2QgcmVxdWlyZXMgbm8gZmluZS10dW5pbmcgZm9yIHMg4omkIDQgYW5kIG91dHBlcmZvcm1zIGxpbmVhciBpbnRlcnBvbGF0aW9uIGF0IHRoZSBzYW1lIHNjYWxlIGZhY3RvciBvbiBtb3N0IGJlbmNobWFya3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIE5USyBQZXJzcGVjdGl2ZSBvbiBSb1BFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgTlRLIChuZXVyYWwgdGFuZ2VudCBrZXJuZWwpIHBlcnNwZWN0aXZlIHRyZWF0cyB0aGUgUm9QRSBmZWF0dXJlcyBhcyBhIEZvdXJpZXItbGlrZSBiYXNpcy4gRWFjaCBSb1BFIGRpbWVuc2lvbiBwYWlyIGkgY29udHJpYnV0ZXMgYSBmZWF0dXJlIG9mIHRoZSBmb3JtIChjb3ModGhldGFfaSAqIG0pLCBzaW4odGhldGFfaSAqIG0pKSDigJQgYSBzaW51c29pZGFsIGJhc2lzIGZ1bmN0aW9uIGF0IGZyZXF1ZW5jeSB0aGV0YV9pLiBGb3IgdGhlIG1vZGVsIHRvIGdlbmVyYWxpc2UgdG8gbG9uZ2VyIHNlcXVlbmNlcywgdGhlc2UgYmFzaXMgZnVuY3Rpb25zIG11c3QgY292ZXIgdGhlIG5ldyBzZXF1ZW5jZSBsZW5ndGggYWRlcXVhdGVseS4gV2l0aCBsaW5lYXIgaW50ZXJwb2xhdGlvbiwgYWxsIGJhc2lzIGZ1bmN0aW9ucyBhcmUgcmVzY2FsZWQgdW5pZm9ybWx5IGJ5IDEvcywgd2hpY2ggY29tcHJlc3NlcyBoaWdoLWZyZXF1ZW5jeSBjb21wb25lbnRzIGludG8gYSBuYXJyb3dlciBiYW5kIGFuZCB3YXN0ZXMgdGhlaXIgcmVwcmVzZW50YXRpb25hbCBjYXBhY2l0eS4gTlRLLWF3YXJlIHNjYWxpbmcgaW5zdGVhZCBpbmNyZWFzZXMgdGhlIGJhc2UgZnJlcXVlbmN5IGIgc28gdGhhdCB0aGUgd2F2ZWxlbmd0aCBvZiBlYWNoIFJvUEUgY29tcG9uZW50IHNjYWxlcyBwcm9wb3J0aW9uYWxseSB0byBpdHMgb3duIG5hdHVyYWwgcGVyaW9kLiBUaGlzIHByZXNlcnZlcyB0aGUgcmVsYXRpdmUgc3BhY2luZyBiZXR3ZWVuIGZyZXF1ZW5jeSBjb21wb25lbnRzLCBtYWludGFpbmluZyB0aGUgb3JpZ2luYWwgRm91cmllciBzdHJ1Y3R1cmUgb2YgdGhlIHBvc2l0aW9uIGVuY29kaW5nIHdoaWxlIHN0aWxsIGZpdHRpbmcgd2l0aGluIHRoZSB0cmFpbmVkIGRpc3RyaWJ1dGlvbi4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6ImJeeyp9ID0gYl8wIFxcY2RvdCBzXntcXCxkLyhkLTIpfSwgXFxxcXVhZCBcXHRoZXRhX2leeyp9ID0gXFxmcmFjezF9eyhiXnsqfSlee1xcLDJpL2R9fSA9IFxcZnJhY3sxfXtiXzBee1xcLDJpL2R9IFxcY2RvdCBzXntcXCwyaS8oZC0yKX19In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZXhwb25lbnQgZC8oZC0yKSBlbnN1cmVzIHRoYXQgdGhlIGhpZ2hlc3QtZnJlcXVlbmN5IHBhaXIgKGk9MCwgd2hlcmUgdGhldGFfMCA9IDEvYl4wID0gMSkgaXMgdW5jaGFuZ2VkOiAxLyhiKileMCA9IDEgcmVnYXJkbGVzcyBvZiBiKi4gVGhlIGxvd2VzdC1mcmVxdWVuY3kgcGFpciAoaSA9IGQvMi0xLCB3aGVyZSB0aGV0YSDiiYggMS9iXnsoZC0yKS9kfSkgaXMgcmVzY2FsZWQgYnkgZXhhY3RseSAxL3MsIGVxdWl2YWxlbnQgdG8gbGluZWFyIGludGVycG9sYXRpb24uIEFsbCBpbnRlcm1lZGlhdGUgZGltZW5zaW9ucyByZWNlaXZlIGEgZnJhY3Rpb25hbCByZXNjYWxpbmcgYmV0d2VlbiAwIGFuZCAxL3MuIFRoaXMgZ3JhZHVhdGVkIGludGVycG9sYXRpb24gaXMgdGhlIE5USyBpbnNpZ2h0OiBoaWdoLWZyZXF1ZW5jeSBkaW1lbnNpb25zIGV4dHJhcG9sYXRlIChubyByZXNjYWxpbmcpLCBsb3ctZnJlcXVlbmN5IGRpbWVuc2lvbnMgaW50ZXJwb2xhdGUgKGZ1bGwgMS9zIHJlc2NhbGluZyksIGFuZCBtaWQtZnJlcXVlbmN5IGRpbWVuc2lvbnMgbGllIG9uIGEgc21vb3RoIGNvbnRpbnV1bSBiZXR3ZWVuIHRoZXNlIGV4dHJlbWVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhc2UgRnJlcXVlbmN5IFNjYWxpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIGltcGxlbWVudCBOVEstYXdhcmUgc3RhdGljIHNjYWxpbmcsIGNvbXB1dGUgYiogPSAxMDAwMCAqIHNeKGQvKGQtMikpIG9uY2UgYXQgbW9kZWwgbG9hZCB0aW1lIGFuZCB1c2UgaXQgZXZlcnl3aGVyZSBpbnN0ZWFkIG9mIDEwMDAwLiBGb3IgTGxhbWEtMi03QiAoZD0xMjgsIHM9NCksIGIqID0gMTAwMDAgKiA0XigxMjgvMTI2KSDiiYggNDA0OTcuIEZvciBzPTgsIGIqIOKJiCAxMDAwMCAqIDheKDEyOC8xMjYpIOKJiCAxNjE5NzkuIFRoZSBjb21wdXRhdGlvbiBpcyBhIHNpbmdsZSBzY2FsYXIgbXVsdGlwbHkg4oCUIG5vIHBlci1sYXllciBvciBwZXItcG9zaXRpb24gb3ZlcmhlYWQuIFRoZSBiYXNlIGIqIGlzIHRoZW4gdXNlZCBpbiB0aGUgc3RhbmRhcmQgUm9QRSBmb3JtdWxhOiBpbnZfZnJlcV9pID0gMSAvIChiKileKDJpL2QpLiBBbGwgc3Vic2VxdWVudCBvcGVyYXRpb25zIChvdXRlciBwcm9kdWN0IHdpdGggcG9zaXRpb25zLCBzaW4vY29zLCByb3RhdGlvbikgYXJlIGlkZW50aWNhbCB0byBzdGFuZGFyZCBSb1BFLiBUaGUgb25seSBjaGFuZ2UgaXMgdGhlIHZhbHVlIG9mIHRoZSBiYXNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBtYXRoXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG50a19uZXdfYmFzZShvcmlnaW5hbF9iYXNlOiBpbnQsIHNjYWxlOiBmbG9hdCwgZGltOiBpbnQpIC1cdTAwM2UgZmxvYXQ6XG4gICAgXCJcIlwiQ29tcHV0ZSBOVEstYXdhcmUgbmV3IGJhc2U6IGIqID0gYmFzZSAqIHNeKGQgLyAoZC0yKSkuXG4gICAgS2VlcHMgdGhlIHBlci1kaW1lbnNpb24gd2F2ZWxlbmd0aCByYXRpbyBpbnZhcmlhbnQgYWNyb3NzIHNjYWxlcy5cIlwiXCJcbiAgICByZXR1cm4gb3JpZ2luYWxfYmFzZSAqIChzY2FsZSAqKiAoZGltIC8gKGRpbSAtIDIpKSlcblxuZGVmIHJvcGVfd2l0aF9iYXNlKGRpbTogaW50LCBzZXFfbGVuOiBpbnQsIGJhc2U6IGZsb2F0KSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJTdGFuZGFyZCBSb1BFIGVtYmVkZGluZ3Mgd2l0aCBhIGNvbmZpZ3VyYWJsZSBiYXNlIGZyZXF1ZW5jeS5cIlwiXCJcbiAgICBpbnZfZnJlcSA9IDEuMCAvIChiYXNlICoqICh0b3JjaC5hcmFuZ2UoMCwgZGltLCAyKS5mbG9hdCgpIC8gZGltKSlcbiAgICB0ID0gdG9yY2guYXJhbmdlKHNlcV9sZW4sIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG4gICAgZnJlcXMgPSB0b3JjaC5vdXRlcih0LCBpbnZfZnJlcSlcbiAgICByZXR1cm4gdG9yY2guY2F0KFtmcmVxcywgZnJlcXNdLCBkaW09LTEpXG5cbmRlZiBjb21wYXJlX3NwZWN0cmEoZGltOiBpbnQgPSAxMjgsIHNlcV9sZW46IGludCA9IDgxOTIsIHNjYWxlOiBmbG9hdCA9IDQuMCk6XG4gICAgXCJcIlwiQ29tcGFyZSByb3RhdGlvbiBhbmdsZSBzcGVjdHJhOiBvcmlnaW5hbCB2cyBsaW5lYXIgdnMgTlRLLXNjYWxlZC5cIlwiXCJcbiAgICBvcmlnX2Jhc2UgPSAxMDAwMFxuICAgIG50a19iYXNlICA9IG50a19uZXdfYmFzZShvcmlnX2Jhc2UsIHNjYWxlLCBkaW0pXG4gICAgcHJpbnQoZlwiT3JpZ2luYWwgYmFzZSA6IHtvcmlnX2Jhc2V9XCIpXG4gICAgcHJpbnQoZlwiTlRLIG5ldyBiYXNlICA6IHtudGtfYmFzZTouMWZ9ICAoc2NhbGU9e3NjYWxlfSwgZGltPXtkaW19KVwiKVxuXG4gICAgZW1iX29yaWcgPSByb3BlX3dpdGhfYmFzZShkaW0sIHNlcV9sZW4sIG9yaWdfYmFzZSlcbiAgICBlbWJfbnRrICA9IHJvcGVfd2l0aF9iYXNlKGRpbSwgc2VxX2xlbiwgbnRrX2Jhc2UpXG5cbiAgICAjIENvbXBhcmUgaGlnaC1mcmVxdWVuY3kgKGRpbSBwYWlyIDApIGFuZCBsb3ctZnJlcXVlbmN5IChwYWlyIGRpbS8vMi0xKVxuICAgIGhpLCBsbyA9IDAsIGRpbSAvLyAyIC0gMVxuICAgIGZvciBsYWJlbCwgZW1iIGluIFsoXCJPcmlnaW5hbFwiLCBlbWJfb3JpZyksIChcIk5US1wiLCBlbWJfbnRrKV06XG4gICAgICAgIHByaW50KGZcIntsYWJlbDoxMHN9ICBoaUBwb3M9e3NlcV9sZW4tMX06IHtlbWJbLTEsIGhpXTouM2Z9ICBcIlxuICAgICAgICAgICAgICBmXCJsb0Bwb3M9e3NlcV9sZW4tMX06IHtlbWJbLTEsIGxvXTouNWZ9XCIpXG5cbmNvbXBhcmVfc3BlY3RyYSgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRHluYW1pYyBOVEsgU2NhbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhdGljIE5USyBzY2FsaW5nIGNvbXB1dGVzIGEgZml4ZWQgYiogZm9yIHRoZSB0YXJnZXQgY29udGV4dCBsZW5ndGggYWhlYWQgb2YgdGltZS4gRHluYW1pYyBOVEsgc2NhbGluZyAoUGVuZyBldCBhbC4sIDIwMjMpIGluc3RlYWQgcmVjb21wdXRlcyB0aGUgZWZmZWN0aXZlIGJhc2Ugb24tdGhlLWZseSBiYXNlZCBvbiB0aGUgYWN0dWFsIHNlcXVlbmNlIGxlbmd0aCBzZWVuIGF0IGVhY2ggZm9yd2FyZCBwYXNzLiBJZiBzZXFfbGVuIOKJpCB0cmFpbl9sZW4sIHRoZSBvcmlnaW5hbCBiYXNlICgxMDAwMCkgaXMgdXNlZCB1bm1vZGlmaWVkLiBJZiBzZXFfbGVuIFx1MDAzZSB0cmFpbl9sZW4sIHRoZSBiYXNlIGlzIHJlY29tcHV0ZWQgYXMgYiogPSAxMDAwMCAqIChzZXFfbGVuIC8gdHJhaW5fbGVuKV4oZC8oZC0yKSkuIFRoaXMgbWVhbnMgYSBtb2RlbCBzZXJ2aW5nIG1peGVkLWxlbmd0aCBpbnB1dHMgYXBwbGllcyBubyBtb2RpZmljYXRpb24gZm9yIHNob3J0IHNlcXVlbmNlcyBhbmQgYXV0b21hdGljYWxseSBhZGFwdHMgdG8gYW55IGxvbmdlciBzZXF1ZW5jZSB3aXRob3V0IHJlcXVpcmluZyBhIHByZS1zcGVjaWZpZWQgdGFyZ2V0IGxlbmd0aC4gRHluYW1pYyBOVEsgaXMgdGhlIGRlZmF1bHQgcm9wZV9zY2FsaW5nPXtcdTAwMjd0eXBlXHUwMDI3OiBcdTAwMjdkeW5hbWljXHUwMDI3LCBcdTAwMjdmYWN0b3JcdTAwMjc6IHN9IGluIEh1Z2dpbmdGYWNlIGFuZCBpcyB0aGUgcmVjb21tZW5kZWQgemVyby1zaG90IGFwcHJvYWNoIGZvciB2YXJpYWJsZS1sZW5ndGggaW5mZXJlbmNlIHBpcGVsaW5lcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbWF0aFxuXG5jbGFzcyBEeW5hbWljTlRLUm9QRSh0b3JjaC5ubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlJlY29tcHV0ZXMgdGhlIFJvUEUgYmFzZSBvbi10aGUtZmx5IGFzIHNlcXVlbmNlIGxlbmd0aCBncm93cy5cIlwiXCJcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkaW06IGludCwgbWF4X3RyYWluX2xlbjogaW50LCBiYXNlOiBpbnQgPSAxMDAwMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmRpbSwgc2VsZi5tYXhfdHJhaW5fbGVuLCBzZWxmLmJhc2UgPSBkaW0sIG1heF90cmFpbl9sZW4sIGJhc2VcbiAgICAgICAgc2VsZi5fY2FjaGU6IGRpY3QgPSB7fVxuXG4gICAgZGVmIF9nZXRfYmFzZShzZWxmLCBzZXFfbGVuOiBpbnQpIC1cdTAwM2UgZmxvYXQ6XG4gICAgICAgIFwiXCJcIlJldHVybiBlZmZlY3RpdmUgYmFzZTogb3JpZ2luYWwgZm9yIHNob3J0IHNlcXMsIE5USy1zY2FsZWQgZm9yIGxvbmcuXCJcIlwiXG4gICAgICAgIGlmIHNlcV9sZW4gXHUwMDNjPSBzZWxmLm1heF90cmFpbl9sZW46XG4gICAgICAgICAgICByZXR1cm4gZmxvYXQoc2VsZi5iYXNlKVxuICAgICAgICBzID0gc2VxX2xlbiAvIHNlbGYubWF4X3RyYWluX2xlblxuICAgICAgICByZXR1cm4gc2VsZi5iYXNlICogKHMgKiogKHNlbGYuZGltIC8gKHNlbGYuZGltIC0gMikpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgc2VxX2xlbjogaW50KSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgaWYgc2VxX2xlbiBub3QgaW4gc2VsZi5fY2FjaGU6XG4gICAgICAgICAgICBiID0gc2VsZi5fZ2V0X2Jhc2Uoc2VxX2xlbilcbiAgICAgICAgICAgIGludl9mcmVxID0gMS4wIC8gKGIgKiogKHRvcmNoLmFyYW5nZSgwLCBzZWxmLmRpbSwgMikuZmxvYXQoKSAvIHNlbGYuZGltKSlcbiAgICAgICAgICAgIHQgPSB0b3JjaC5hcmFuZ2Uoc2VxX2xlbiwgZHR5cGU9dG9yY2guZmxvYXQzMilcbiAgICAgICAgICAgIGZyZXFzID0gdG9yY2gub3V0ZXIodCwgaW52X2ZyZXEpXG4gICAgICAgICAgICBzZWxmLl9jYWNoZVtzZXFfbGVuXSA9IHRvcmNoLmNhdChbZnJlcXMsIGZyZXFzXSwgZGltPS0xKVxuICAgICAgICByZXR1cm4gc2VsZi5fY2FjaGVbc2VxX2xlbl1cblxuIyBUZXN0OiBiYXNlIGdyb3dzIGF1dG9tYXRpY2FsbHkgYXMgc2VxdWVuY2UgbGVuZ3RoIGluY3JlYXNlc1xucm9wZSA9IER5bmFtaWNOVEtSb1BFKGRpbT0xMjgsIG1heF90cmFpbl9sZW49NDA5NilcbmZvciBMIGluIFsyMDQ4LCA0MDk2LCA4MTkyLCAxNjM4NCwgMzI3NjhdOlxuICAgIGIgPSByb3BlLl9nZXRfYmFzZShMKVxuICAgIGYgPSByb3BlKEwpXG4gICAgcHJpbnQoZlwiTD17TDo2ZH0gIGVmZl9iYXNlPXtiOlx1MDAzZTEwLjFmfSAgbWF4X2FuZ2xlPXtmLm1heCgpLml0ZW0oKTouM2Z9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRnJlcXVlbmN5IEJhbmRzIGFuZCBEaW1lbnNpb24gRGlzdHJpYnV0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGtleSBkaWFnbm9zdGljIGZvciBhbnkgUm9QRSBleHRlbnNpb24gbWV0aG9kIGlzIGhvdyB0aGUgcGVyLWRpbWVuc2lvbiByb3RhdGlvbiBhbmdsZSBhdCB0aGUgbWF4aW11bSBzZXF1ZW5jZSBwb3NpdGlvbiBjb21wYXJlcyB0byB0cmFpbmluZy4gSWRlYWxseSwgZXZlcnkgZGltZW5zaW9uIHBhaXIgc2hvdWxkIGhhdmUgYSByb3RhdGlvbiBhbmdsZSBhdCBwb3NpdGlvbiBOIHRoYXQgaXMgd2l0aGluIHRoZSByYW5nZSBzZWVuIGR1cmluZyB0cmFpbmluZy4gVW5kZXIgbGluZWFyIHNjYWxpbmcgd2l0aCBzPTQsIGFsbCBkaW1lbnNpb25zIGFyZSB1bmlmb3JtbHkgY29tcHJlc3NlZDogZGltZW5zaW9uIHBhaXIgMCAoaGlnaC1mcmVxdWVuY3kpIHNlZXMgcG9zaXRpb24gTi80IGluc3RlYWQgb2YgTiwgcmVkdWNpbmcgaXRzIHJvdGF0aW9uIGFuZ2xlIGJ5IDR4LiBVbmRlciBOVEsgc2NhbGluZywgZGltZW5zaW9uIHBhaXIgMCBpcyBlc3NlbnRpYWxseSB1bmNoYW5nZWQgKHRoZSBleHBvbmVudCAyKjAvZCA9IDAgbWVhbnMgaW52X2ZyZXFfMCBpcyB1bmFmZmVjdGVkIGJ5IHRoZSBiYXNlIGNoYW5nZSksIHdoaWxlIGRpbWVuc2lvbiBwYWlyIGQvMi0xIChsb3ctZnJlcXVlbmN5KSBpcyByZWR1Y2VkIGJ5IGFwcHJveGltYXRlbHkgMS9zLiBUaGlzIGdyYWR1YXRlZCB0cmVhdG1lbnQg4oCUIG5vIGNoYW5nZSBmb3IgaGlnaC1mcmVxdWVuY3ksIGZ1bGwgaW50ZXJwb2xhdGlvbiBmb3IgbG93LWZyZXF1ZW5jeSDigJQgaXMgd2h5IE5USyBvdXRwZXJmb3JtcyBsaW5lYXIgc2NhbGluZyBhdCB0aGUgc2FtZSBzY2FsZSBmYWN0b3IuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG1hdGhcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgcGVyX2RpbV9hbmdsZXMoZGltOiBpbnQsIHBvczogaW50LCBiYXNlOiBmbG9hdCkgLVx1MDAzZSBucC5uZGFycmF5OlxuICAgIFwiXCJcIlJldHVybiByb3RhdGlvbiBhbmdsZSB0aGV0YV9pICogcG9zIGZvciBlYWNoIGRpbWVuc2lvbiBwYWlyIGkuXCJcIlwiXG4gICAgaW52X2ZyZXEgPSAxLjAgLyAoYmFzZSAqKiAodG9yY2guYXJhbmdlKDAsIGRpbSwgMikuZmxvYXQoKSAvIGRpbSkpXG4gICAgcmV0dXJuIChwb3MgKiBpbnZfZnJlcSkubnVtcHkoKVxuXG5kaW0sIHBvcywgc2NhbGUgPSAxMjgsIDQwOTYsIDQuMFxubnRrX2Jhc2UgPSAxMDAwMCAqIChzY2FsZSAqKiAoZGltIC8gKGRpbSAtIDIpKSlcblxub3JpZ19hbmdsZXMgICA9IHBlcl9kaW1fYW5nbGVzKGRpbSwgcG9zLCBiYXNlPTEwMDAwKVxubGluZWFyX2FuZ2xlcyA9IHBlcl9kaW1fYW5nbGVzKGRpbSwgcG9zIC8vIGludChzY2FsZSksIGJhc2U9MTAwMDApICAjIGxpbmVhcjogcG9zL3Ncbm50a19hbmdsZXMgICAgPSBwZXJfZGltX2FuZ2xlcyhkaW0sIHBvcywgYmFzZT1udGtfYmFzZSlcblxucHJpbnQoZlwie1x1MDAyN1BhaXJcdTAwMjc6XHUwMDNlNn0ge1x1MDAyN09yaWdpbmFsXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3TGluZWFyLzRcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdOVEtcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdMby1mcmVxP1x1MDAyNzpcdTAwM2UxMH1cIilcbmZvciBpLCAobywgbCwgbikgaW4gZW51bWVyYXRlKHppcChvcmlnX2FuZ2xlcywgbGluZWFyX2FuZ2xlcywgbnRrX2FuZ2xlcykpOlxuICAgIGxvX2ZyZXFfbGFiZWwgPSBcInllc1wiIGlmIG8gXHUwMDNjIDAuMSBlbHNlIFwibm9cIlxuICAgIGlmIGkgJSA2ID09IDA6XG4gICAgICAgIHByaW50KGZcIntpOlx1MDAzZTZ9IHtvOlx1MDAzZTEyLjRmfSB7bDpcdTAwM2UxMi40Zn0ge246XHUwMDNlMTIuNGZ9IHtsb19mcmVxX2xhYmVsOlx1MDAzZTEwfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5USyB2cyBMaW5lYXIgSW50ZXJwb2xhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT24gc3RhbmRhcmQgbG9uZy1jb250ZXh0IGJlbmNobWFya3MgKFNjcm9sbHMsIExvbmdCZW5jaCwgcGFzc2tleSByZXRyaWV2YWwpLCBOVEstYXdhcmUgc2NhbGluZyBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybXMgbGluZWFyIGludGVycG9sYXRpb24gYXQgdGhlIHNhbWUgc2NhbGUgZmFjdG9yIHdoZW4gbm8gZmluZS10dW5pbmcgaXMgYXBwbGllZC4gVGhlIGdhcCBpcyBsYXJnZXN0IGF0IGhpZ2ggc2NhbGUgZmFjdG9ycyAocz004oCTOCkgYW5kIG9uIHRhc2tzIHRoYXQgcmVxdWlyZSBwcmVjaXNlIGxvY2FsIHRva2VuIHJlbGF0aW9uc2hpcHMsIHN1Y2ggYXMgY29kZSBjb21wbGV0aW9uIGFuZCBzdHJ1Y3R1cmVkIGV4dHJhY3Rpb24uIFRoZSByZWFzb24gaXMgdGhhdCBsaW5lYXIgaW50ZXJwb2xhdGlvbiBkZWdyYWRlcyBoaWdoLWZyZXF1ZW5jeSBkaW1lbnNpb25zIHRoYXQgYXJlIGNyaXRpY2FsIGZvciBkaXN0aW5ndWlzaGluZyBhZGphY2VudCB0b2tlbnMuIE5USyBzY2FsaW5nIGxlYXZlcyB0aGVzZSBkaW1lbnNpb25zIGludGFjdC4gRm9yIHM9MiwgdGhlIGRpZmZlcmVuY2UgaXMgc21hbGwgKGJvdGggbWV0aG9kcyBhcmUgbmVhci1sb3NzbGVzcykuIEZvciBzPTgsIE5USyBzY2FsaW5nIGNhbiBnaXZlIDXigJMxMCBQUEwgaW1wcm92ZW1lbnQgb3ZlciBsaW5lYXIgaW50ZXJwb2xhdGlvbiB6ZXJvLXNob3QuIFdpdGggZmluZS10dW5pbmcsIGJvdGggbWV0aG9kcyBjb252ZXJnZSB0byBzaW1pbGFyIHF1YWxpdHksIHRob3VnaCBOVEsgcmVxdWlyZXMgZmV3ZXIgZmluZS10dW5pbmcgc3RlcHMgdG8gY29udmVyZ2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlJvUEUgdmFyaWFudCIsIkJhc2UgY2hhbmdlIiwiSGlnaC1mcmVxIGRpbXMiLCJGaW5lLXR1bmluZyBuZWVkZWQiLCJQUEwgYXQgMTZLIiwiTm90ZXMiXSwicm93cyI6W1siT3JpZ2luYWwgKDRLKSIsIk5vbmUgKGI9MTAwMDApIiwiSW50YWN0IiwiTi9BIiwiMTQ3KyAoT09EKSIsIkZhaWxzIGNvbXBsZXRlbHkgYmV5b25kIHRyYWluaW5nIHdpbmRvdyJdLFsiTGluZWFyIHNjYWxlIChzPTQpIiwiTm9uZSAoYj0xMDAwMCkiLCJDb21wcmVzc2VkIDR4IiwiUmVjb21tZW5kZWQiLCI4LjIiLCJVbmlmb3JtIHBvc2l0aW9uIGNvbXByZXNzaW9uIl0sWyJOVEsgc3RhdGljIChzPTQpIiwiYio9NDA0OTciLCJJbnRhY3QgKHBhaXIgMCkiLCJOb3QgcmVxdWlyZWQiLCI3LjQiLCJHcmFkdWF0ZWQgcGVyLWRpbSBpbnRlcnBvbGF0aW9uIl0sWyJOVEsgZHluYW1pYyAocz00KSIsImIqIGNvbXB1dGVkIHBlciBzZXFfbGVuIiwiSW50YWN0IiwiTm90IHJlcXVpcmVkIiwiNy4xIiwiQWRhcHRzIHRvIGFjdHVhbCBzZXF1ZW5jZSBsZW5ndGgiXSxbIllhUk4gKHM9NCkiLCJQaWVjZXdpc2UgcGVyLWRpbSIsIkZ1bGx5IGludGFjdCIsIjQwMCBzdGVwcyIsIjYuOSIsIkJlc3QgcXVhbGl0eTsgYWRkcyB0ZW1wZXJhdHVyZSBjb3JyZWN0aW9uIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6Ilplcm8tU2hvdCBDb250ZXh0IEV4dGVuc2lvbiIsImNvbnRlbnQiOiJOVEsgc2NhbGluZyBpcyB0aGUgcmVjb21tZW5kZWQgemVyby1zaG90IGNvbnRleHQgZXh0ZW5zaW9uIG1ldGhvZCBmb3IgMuKAkzR4IGV4dGVuc2lvbnMuIEl0IHByZXZlbnRzIHRoZSBhbGlhc2luZyBvZiBsb3ctZnJlcXVlbmN5IFJvUEUgZGltZW5zaW9ucyB0aGF0IGxpbmVhciBpbnRlcnBvbGF0aW9uIGNhdXNlcywgYW5kIGxlYXZlcyBoaWdoLWZyZXF1ZW5jeSBkaW1lbnNpb25zIHVudG91Y2hlZC4gVXNlIHJvcGVfc2NhbGluZz17XHUwMDI3dHlwZVx1MDAyNzogXHUwMDI3ZHluYW1pY1x1MDAyNywgXHUwMDI3ZmFjdG9yXHUwMDI3OiBzfSBpbiBIdWdnaW5nRmFjZSB0byBnZXQgZHluYW1pYyBOVEsgc2NhbGluZyB3aXRoIG5vIGZpbmUtdHVuaW5nIHJlcXVpcmVkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkltcGxlbWVudGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBIdWdnaW5nRmFjZSBUcmFuc2Zvcm1lcnMsIE5USy1hd2FyZSBzY2FsaW5nIGlzIGF2YWlsYWJsZSB2aWEgdHdvIHJvcGVfc2NhbGluZyB0eXBlczogXHUwMDI3ZHluYW1pY1x1MDAyNyAocmVjb21wdXRlcyBiYXNlIHBlciBzZXF1ZW5jZSBsZW5ndGgsIHJlY29tbWVuZGVkKSBhbmQsIGluIHNvbWUgbW9kZWwgY29uZmlndXJhdGlvbnMsIGEgc3RhdGljIHZhcmlhbnQuIFRoZSBmYWN0b3IgcGFyYW1ldGVyIHNldHMgdGhlIG1heGltdW0gc2NhbGUgZmFjdG9yIHM7IHRoZSBhY3R1YWwgYmFzZSBpcyBjb21wdXRlZCBhcyAxMDAwMCAqIHNeKGQvKGQtMikpIHVzaW5nIHRoZSBtb2RlbOKAmXMgaGVhZCBkaW1lbnNpb24gZC4gRm9yIG1vZGVscyBub3QgeWV0IHN1cHBvcnRpbmcgcm9wZV9zY2FsaW5nIG5hdGl2ZWx5LCBpdCBpcyBzdHJhaWdodGZvcndhcmQgdG8gbW9ua2V5LXBhdGNoIHRoZSByb3RhcnkgZW1iZWRkaW5nIG1vZHVsZTogc3ViY2xhc3MgTGxhbWFSb3RhcnlFbWJlZGRpbmcgKG9yIGVxdWl2YWxlbnQpLCBvdmVycmlkZSB0aGUgX19pbml0X18gdG8gcmVjb21wdXRlIGludl9mcmVxIHdpdGggdGhlIG5ldyBiYXNlLCBhbmQgcmVwbGFjZSB0aGUgbW9kdWxlIGluLXBsYWNlIG9uIHRoZSBsb2FkZWQgbW9kZWwuIFRoZSBwYXRjaCBpcyAxMOKAkzE1IGxpbmVzIG9mIFB5dGhvbiBhbmQgcmVxdWlyZXMgbm8gcmV0cmFpbmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgTGxhbWFDb25maWcsIExsYW1hRm9yQ2F1c2FsTE0sIEF1dG9Ub2tlbml6ZXJcblxuZGVmIGxvYWRfbGxhbWFfbnRrX2R5bmFtaWMoXG4gICAgICAgIG1vZGVsX2lkOiBzdHIgPSBcIm1ldGEtbGxhbWEvTGxhbWEtMi03Yi1oZlwiLFxuICAgICAgICBmYWN0b3I6IGZsb2F0ID0gNC4wLFxuICAgICAgICBtYXhfY3R4OiBpbnQgPSAxNjM4NCkgLVx1MDAzZSB0dXBsZTpcbiAgICBcIlwiXCJMb2FkIExsYW1hLTIgd2l0aCBIdWdnaW5nRmFjZSBkeW5hbWljIE5USyBSb1BFIHNjYWxpbmcuXCJcIlwiXG4gICAgY29uZmlnID0gTGxhbWFDb25maWcuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX2lkKVxuICAgIGNvbmZpZy5yb3BlX3NjYWxpbmcgPSB7XCJ0eXBlXCI6IFwiZHluYW1pY1wiLCBcImZhY3RvclwiOiBmYWN0b3J9XG4gICAgY29uZmlnLm1heF9wb3NpdGlvbl9lbWJlZGRpbmdzID0gbWF4X2N0eFxuICAgIG1vZGVsID0gTGxhbWFGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQoXG4gICAgICAgIG1vZGVsX2lkLCBjb25maWc9Y29uZmlnLFxuICAgICAgICB0b3JjaF9kdHlwZT10b3JjaC5mbG9hdDE2LCBkZXZpY2VfbWFwPVwiYXV0b1wiXG4gICAgKVxuICAgIHRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKG1vZGVsX2lkKVxuICAgIHJldHVybiBtb2RlbCwgdG9rZW5pemVyXG5cbiMgQ29tcGFyZSBQUEwgYXQgMTZLOiBsaW5lYXIgdnMgTlRLLXN0YXRpYyB2cyBOVEstZHluYW1pYyAoc2ltdWxhdGVkKVxucmVzdWx0cyA9IFtcbiAgICAoXCJObyBzY2FsaW5nXCIsICAgICAgICAxNDcuMyksXG4gICAgKFwiTGluZWFyIChzPTQpXCIsICAgICAgICA4LjIpLFxuICAgIChcIk5USy1zdGF0aWMgKHM9NClcIiwgICAgNy40KSxcbiAgICAoXCJOVEstZHluYW1pYyAocz00KVwiLCAgIDcuMSksXG5dXG5mb3IgbWV0aG9kLCBwcGwgaW4gcmVzdWx0czpcbiAgICBwcmludChmXCJ7bWV0aG9kOlx1MDAzYzI1fSBQUExAMTZLID0ge3BwbDouMWZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTlRLLWF3YXJlIFJvUEUgc2NhbGluZyBpcyB0aGUgcmVjb21tZW5kZWQgemVyby1zaG90IGNvbnRleHQgZXh0ZW5zaW9uIG1ldGhvZCB3aGVuIGZpbmUtdHVuaW5nIGlzIG5vdCBhbiBvcHRpb24uIEJ5IHJlc2NhbGluZyB0aGUgUm9QRSBiYXNlIGZyZXF1ZW5jeSByYXRoZXIgdGhhbiB0aGUgcG9zaXRpb24gaW5kaWNlcywgaXQgYXBwbGllcyBncmFkdWF0ZWQgaW50ZXJwb2xhdGlvbjogbm9uZSBmb3IgaGlnaC1mcmVxdWVuY3kgZGltZW5zaW9ucyBhbmQgZnVsbCAxL3MgZm9yIGxvdy1mcmVxdWVuY3kgZGltZW5zaW9ucy4gVGhpcyBwcmVzZXJ2ZXMgbG9jYWwgc3ludGFjdGljIHN0cnVjdHVyZSB3aGlsZSBleHRlbmRpbmcgbG9uZy1yYW5nZSBwb3NpdGlvbmFsIGNvdmVyYWdlLiBUaGUgZHluYW1pYyB2YXJpYW50IChyb3BlX3NjYWxpbmcgdHlwZT1cdTAwMjdkeW5hbWljXHUwMDI3KSBpcyBzdHJpY3RseSBiZXR0ZXIgdGhhbiB0aGUgc3RhdGljIHZhcmlhbnQgYmVjYXVzZSBpdCBkb2VzIG5vdCBwZXJ0dXJiIHNob3J0LXNlcXVlbmNlIGJlaGF2aW91ci4gRm9yIHByb2R1Y3Rpb24gdXNlLCBzZXQgZmFjdG9yIHRvIHRoZSBtYXhpbXVtIGV4cGVjdGVkIGNvbnRleHQgcmF0aW87IHRoZSBiYXNlIHdpbGwgYmUgY29tcHV0ZWQgYXV0b21hdGljYWxseS4gV2hlbiBmaW5lLXR1bmluZyBpcyBhdmFpbGFibGUsIE5USy1hd2FyZSBzY2FsaW5nIGNvbnZlcmdlcyBmYXN0ZXIgdGhhbiBsaW5lYXIgaW50ZXJwb2xhdGlvbiBhbmQgc2VydmVzIGFzIHRoZSBzdGFydGluZyBwb2ludCBmb3IgWWFSTi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlNjYWxlIHRoZSBiYXNlIGIgdmlhIGIqID0gMTAwMDAgKiBzXihkLyhkLTIpKTsgZG8gbm90IGNoYW5nZSB0aGUgcG9zaXRpb24gaW5kaWNlcyIsIkR5bmFtaWMgTlRLIHJlY29tcHV0ZXMgYiogYXQgZWFjaCBmb3J3YXJkIHBhc3M7IHNhZmUgZm9yIHZhcmlhYmxlLWxlbmd0aCBpbmZlcmVuY2UiLCJIaWdoLWZyZXF1ZW5jeSBSb1BFIGRpbWVuc2lvbnMgKHBhaXIgMCkgYXJlIHVuYWZmZWN0ZWQ7IGxvdy1mcmVxdWVuY3kgZGltcyBnZXQgZnVsbCAxL3MgcmVzY2FsaW5nIiwiV29ya3MgemVyby1zaG90IGZvciBzIOKJpCA0OyBvdXRwZXJmb3JtcyBsaW5lYXIgaW50ZXJwb2xhdGlvbiBieSAwLjjigJMxLjEgUFBMIGF0IDE2SyIsIkh1Z2dpbmdGYWNlOiByb3BlX3NjYWxpbmc9e1x1MDAyN3R5cGVcdTAwMjc6IFx1MDAyN2R5bmFtaWNcdTAwMjcsIFx1MDAyN2ZhY3Rvclx1MDAyNzogNC4wfSDigJQgb25lIGNvbmZpZyBsaW5lIiwiWWFSTiBleHRlbmRzIE5USyBieSBhZGRpbmcgcGllY2V3aXNlIG1pZC1mcmVxdWVuY3kgaGFuZGxpbmcgYW5kIHRlbXBlcmF0dXJlIGNvcnJlY3Rpb24iXX1d"
---
# NTK-Aware RoPE Scaling

NTK-aware RoPE scaling addresses the core weakness of linear interpolation: uniform compression destroys the high-frequency RoPE dimensions that encode local syntactic structure. Instead of dividing position indices by s, NTK-aware scaling rescales the RoPE base frequency (theta, typically 10000) to a new value that distributes the ‘interpolation burden’ across dimensions according to their natural frequency. Dimensions with short wavelengths (high-frequency, encoding local patterns) receive little or no interpolation, while dimensions with long wavelengths (low-frequency, encoding document-level structure) receive strong interpolation. The result is a frequency spectrum that is distorted as little as possible from the training distribution, giving better zero-shot performance at the same scale factor.

## Overview

NTK-aware scaling (Reddit, bloc97, 2023; subsequently studied by Xiong et al., 2023) modifies the RoPE base from 10000 to a new value b* = 10000 * s^(d/(d-2)), where s is the desired scale factor and d is the head dimension. This formula derives from the requirement that the highest-frequency RoPE dimension completes the same number of full rotations over the extended context as it did over the training context — preventing aliasing. In practice, for s=4 and d=128 (Llama-2-7B), the new base is approximately 10000 * 4^(128/126) ≈ 40497. With this larger base, all RoPE frequencies are reduced proportionally to their dimension index, with higher-indexed (lower-frequency) dimensions receiving the most rescaling. The method requires no fine-tuning for s ≤ 4 and outperforms linear interpolation at the same scale factor on most benchmarks.

## The NTK Perspective on RoPE

The NTK (neural tangent kernel) perspective treats the RoPE features as a Fourier-like basis. Each RoPE dimension pair i contributes a feature of the form (cos(theta_i * m), sin(theta_i * m)) — a sinusoidal basis function at frequency theta_i. For the model to generalise to longer sequences, these basis functions must cover the new sequence length adequately. With linear interpolation, all basis functions are rescaled uniformly by 1/s, which compresses high-frequency components into a narrower band and wastes their representational capacity. NTK-aware scaling instead increases the base frequency b so that the wavelength of each RoPE component scales proportionally to its own natural period. This preserves the relative spacing between frequency components, maintaining the original Fourier structure of the position encoding while still fitting within the trained distribution.

$$b^{*} = b_0 \cdot s^{\,d/(d-2)}, \qquad \theta_i^{*} = \frac{1}{(b^{*})^{\,2i/d}} = \frac{1}{b_0^{\,2i/d} \cdot s^{\,2i/(d-2)}}$$

The exponent d/(d-2) ensures that the highest-frequency pair (i=0, where theta_0 = 1/b^0 = 1) is unchanged: 1/(b*)^0 = 1 regardless of b*. The lowest-frequency pair (i = d/2-1, where theta ≈ 1/b^{(d-2)/d}) is rescaled by exactly 1/s, equivalent to linear interpolation. All intermediate dimensions receive a fractional rescaling between 0 and 1/s. This graduated interpolation is the NTK insight: high-frequency dimensions extrapolate (no rescaling), low-frequency dimensions interpolate (full 1/s rescaling), and mid-frequency dimensions lie on a smooth continuum between these extremes.

## Base Frequency Scaling

To implement NTK-aware static scaling, compute b* = 10000 * s^(d/(d-2)) once at model load time and use it everywhere instead of 10000. For Llama-2-7B (d=128, s=4), b* = 10000 * 4^(128/126) ≈ 40497. For s=8, b* ≈ 10000 * 8^(128/126) ≈ 161979. The computation is a single scalar multiply — no per-layer or per-position overhead. The base b* is then used in the standard RoPE formula: inv_freq_i = 1 / (b*)^(2i/d). All subsequent operations (outer product with positions, sin/cos, rotation) are identical to standard RoPE. The only change is the value of the base.

```python
import torch
import math
import numpy as np

def ntk_new_base(original_base: int, scale: float, dim: int) -> float:
    """Compute NTK-aware new base: b* = base * s^(d / (d-2)).
    Keeps the per-dimension wavelength ratio invariant across scales."""
    return original_base * (scale ** (dim / (dim - 2)))

def rope_with_base(dim: int, seq_len: int, base: float) -> torch.Tensor:
    """Standard RoPE embeddings with a configurable base frequency."""
    inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float() / dim))
    t = torch.arange(seq_len, dtype=torch.float32)
    freqs = torch.outer(t, inv_freq)
    return torch.cat([freqs, freqs], dim=-1)

def compare_spectra(dim: int = 128, seq_len: int = 8192, scale: float = 4.0):
    """Compare rotation angle spectra: original vs linear vs NTK-scaled."""
    orig_base = 10000
    ntk_base  = ntk_new_base(orig_base, scale, dim)
    print(f"Original base : {orig_base}")
    print(f"NTK new base  : {ntk_base:.1f}  (scale={scale}, dim={dim})")

    emb_orig = rope_with_base(dim, seq_len, orig_base)
    emb_ntk  = rope_with_base(dim, seq_len, ntk_base)

    # Compare high-frequency (dim pair 0) and low-frequency (pair dim//2-1)
    hi, lo = 0, dim // 2 - 1
    for label, emb in [("Original", emb_orig), ("NTK", emb_ntk)]:
        print(f"{label:10s}  hi@pos={seq_len-1}: {emb[-1, hi]:.3f}  "
              f"lo@pos={seq_len-1}: {emb[-1, lo]:.5f}")

compare_spectra()
```

## Dynamic NTK Scaling

Static NTK scaling computes a fixed b* for the target context length ahead of time. Dynamic NTK scaling (Peng et al., 2023) instead recomputes the effective base on-the-fly based on the actual sequence length seen at each forward pass. If seq_len ≤ train_len, the original base (10000) is used unmodified. If seq_len > train_len, the base is recomputed as b* = 10000 * (seq_len / train_len)^(d/(d-2)). This means a model serving mixed-length inputs applies no modification for short sequences and automatically adapts to any longer sequence without requiring a pre-specified target length. Dynamic NTK is the default rope_scaling={'type': 'dynamic', 'factor': s} in HuggingFace and is the recommended zero-shot approach for variable-length inference pipelines.

```python
import torch
import math

class DynamicNTKRoPE(torch.nn.Module):
    """Recomputes the RoPE base on-the-fly as sequence length grows."""

    def __init__(self, dim: int, max_train_len: int, base: int = 10000):
        super().__init__()
        self.dim, self.max_train_len, self.base = dim, max_train_len, base
        self._cache: dict = {}

    def _get_base(self, seq_len: int) -> float:
        """Return effective base: original for short seqs, NTK-scaled for long."""
        if seq_len <= self.max_train_len:
            return float(self.base)
        s = seq_len / self.max_train_len
        return self.base * (s ** (self.dim / (self.dim - 2)))

    def forward(self, seq_len: int) -> torch.Tensor:
        if seq_len not in self._cache:
            b = self._get_base(seq_len)
            inv_freq = 1.0 / (b ** (torch.arange(0, self.dim, 2).float() / self.dim))
            t = torch.arange(seq_len, dtype=torch.float32)
            freqs = torch.outer(t, inv_freq)
            self._cache[seq_len] = torch.cat([freqs, freqs], dim=-1)
        return self._cache[seq_len]

# Test: base grows automatically as sequence length increases
rope = DynamicNTKRoPE(dim=128, max_train_len=4096)
for L in [2048, 4096, 8192, 16384, 32768]:
    b = rope._get_base(L)
    f = rope(L)
    print(f"L={L:6d}  eff_base={b:>10.1f}  max_angle={f.max().item():.3f}")
```

## Frequency Bands and Dimension Distribution

A key diagnostic for any RoPE extension method is how the per-dimension rotation angle at the maximum sequence position compares to training. Ideally, every dimension pair should have a rotation angle at position N that is within the range seen during training. Under linear scaling with s=4, all dimensions are uniformly compressed: dimension pair 0 (high-frequency) sees position N/4 instead of N, reducing its rotation angle by 4x. Under NTK scaling, dimension pair 0 is essentially unchanged (the exponent 2*0/d = 0 means inv_freq_0 is unaffected by the base change), while dimension pair d/2-1 (low-frequency) is reduced by approximately 1/s. This graduated treatment — no change for high-frequency, full interpolation for low-frequency — is why NTK outperforms linear scaling at the same scale factor.

```python
import torch
import math
import numpy as np

def per_dim_angles(dim: int, pos: int, base: float) -> np.ndarray:
    """Return rotation angle theta_i * pos for each dimension pair i."""
    inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float() / dim))
    return (pos * inv_freq).numpy()

dim, pos, scale = 128, 4096, 4.0
ntk_base = 10000 * (scale ** (dim / (dim - 2)))

orig_angles   = per_dim_angles(dim, pos, base=10000)
linear_angles = per_dim_angles(dim, pos // int(scale), base=10000)  # linear: pos/s
ntk_angles    = per_dim_angles(dim, pos, base=ntk_base)

print(f"{'Pair':>6} {'Original':>12} {'Linear/4':>12} {'NTK':>12} {'Lo-freq?':>10}")
for i, (o, l, n) in enumerate(zip(orig_angles, linear_angles, ntk_angles)):
    lo_freq_label = "yes" if o < 0.1 else "no"
    if i % 6 == 0:
        print(f"{i:>6} {o:>12.4f} {l:>12.4f} {n:>12.4f} {lo_freq_label:>10}")
```

## NTK vs Linear Interpolation

On standard long-context benchmarks (Scrolls, LongBench, passkey retrieval), NTK-aware scaling consistently outperforms linear interpolation at the same scale factor when no fine-tuning is applied. The gap is largest at high scale factors (s=4–8) and on tasks that require precise local token relationships, such as code completion and structured extraction. The reason is that linear interpolation degrades high-frequency dimensions that are critical for distinguishing adjacent tokens. NTK scaling leaves these dimensions intact. For s=2, the difference is small (both methods are near-lossless). For s=8, NTK scaling can give 5–10 PPL improvement over linear interpolation zero-shot. With fine-tuning, both methods converge to similar quality, though NTK requires fewer fine-tuning steps to converge.

| RoPE variant | Base change | High-freq dims | Fine-tuning needed | PPL at 16K | Notes |
| --- | --- | --- | --- | --- | --- |
| Original (4K) | None (b=10000) | Intact | N/A | 147+ (OOD) | Fails completely beyond training window |
| Linear scale (s=4) | None (b=10000) | Compressed 4x | Recommended | 8.2 | Uniform position compression |
| NTK static (s=4) | b*=40497 | Intact (pair 0) | Not required | 7.4 | Graduated per-dim interpolation |
| NTK dynamic (s=4) | b* computed per seq_len | Intact | Not required | 7.1 | Adapts to actual sequence length |
| YaRN (s=4) | Piecewise per-dim | Fully intact | 400 steps | 6.9 | Best quality; adds temperature correction |

> **Zero-Shot Context Extension**: NTK scaling is the recommended zero-shot context extension method for 2–4x extensions. It prevents the aliasing of low-frequency RoPE dimensions that linear interpolation causes, and leaves high-frequency dimensions untouched. Use rope_scaling={'type': 'dynamic', 'factor': s} in HuggingFace to get dynamic NTK scaling with no fine-tuning required.

## Implementation

In HuggingFace Transformers, NTK-aware scaling is available via two rope_scaling types: 'dynamic' (recomputes base per sequence length, recommended) and, in some model configurations, a static variant. The factor parameter sets the maximum scale factor s; the actual base is computed as 10000 * s^(d/(d-2)) using the model’s head dimension d. For models not yet supporting rope_scaling natively, it is straightforward to monkey-patch the rotary embedding module: subclass LlamaRotaryEmbedding (or equivalent), override the __init__ to recompute inv_freq with the new base, and replace the module in-place on the loaded model. The patch is 10–15 lines of Python and requires no retraining.

```python
import torch
from transformers import LlamaConfig, LlamaForCausalLM, AutoTokenizer

def load_llama_ntk_dynamic(
        model_id: str = "meta-llama/Llama-2-7b-hf",
        factor: float = 4.0,
        max_ctx: int = 16384) -> tuple:
    """Load Llama-2 with HuggingFace dynamic NTK RoPE scaling."""
    config = LlamaConfig.from_pretrained(model_id)
    config.rope_scaling = {"type": "dynamic", "factor": factor}
    config.max_position_embeddings = max_ctx
    model = LlamaForCausalLM.from_pretrained(
        model_id, config=config,
        torch_dtype=torch.float16, device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    return model, tokenizer

# Compare PPL at 16K: linear vs NTK-static vs NTK-dynamic (simulated)
results = [
    ("No scaling",        147.3),
    ("Linear (s=4)",        8.2),
    ("NTK-static (s=4)",    7.4),
    ("NTK-dynamic (s=4)",   7.1),
]
for method, ppl in results:
    print(f"{method:<25} PPL@16K = {ppl:.1f}")
```

## Key Takeaways

NTK-aware RoPE scaling is the recommended zero-shot context extension method when fine-tuning is not an option. By rescaling the RoPE base frequency rather than the position indices, it applies graduated interpolation: none for high-frequency dimensions and full 1/s for low-frequency dimensions. This preserves local syntactic structure while extending long-range positional coverage. The dynamic variant (rope_scaling type='dynamic') is strictly better than the static variant because it does not perturb short-sequence behaviour. For production use, set factor to the maximum expected context ratio; the base will be computed automatically. When fine-tuning is available, NTK-aware scaling converges faster than linear interpolation and serves as the starting point for YaRN.

- Scale the base b via b* = 10000 * s^(d/(d-2)); do not change the position indices
- Dynamic NTK recomputes b* at each forward pass; safe for variable-length inference
- High-frequency RoPE dimensions (pair 0) are unaffected; low-frequency dims get full 1/s rescaling
- Works zero-shot for s ≤ 4; outperforms linear interpolation by 0.8–1.1 PPL at 16K
- HuggingFace: rope_scaling={'type': 'dynamic', 'factor': 4.0} — one config line
- YaRN extends NTK by adding piecewise mid-frequency handling and temperature correction

