---
title: "NumPy — Broadcasting, Vectorization, and Advanced Indexing"
slug: "numpy-vectorization"
description: "NumPy's core patterns for high-performance array computing: broadcasting rules, replacing Python loops with vectorized operations, fancy and boolean indexing, and einsum for tensor contractions."
tags: ["pytorch", "tools", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTnVtUHkgaXMgdGhlIGZvdW5kYXRpb24gb2Ygc2NpZW50aWZpYyBQeXRob24gY29tcHV0aW5nLiBJdHMgcGVyZm9ybWFuY2UgYWR2YW50YWdlIG92ZXIgcHVyZSBQeXRob24gY29tZXMgZnJvbSB0aHJlZSBtZWNoYW5pc21zOiB2ZWN0b3JpemVkIG9wZXJhdGlvbnMgKEMtY29tcGlsZWQga2VybmVscyBvdmVyIGVudGlyZSBhcnJheXMpLCBicm9hZGNhc3RpbmcgKGltcGxpY2l0IHNoYXBlIGFsaWdubWVudCB3aXRob3V0IGNvcHlpbmcpLCBhbmQgYWR2YW5jZWQgaW5kZXhpbmcgKGZhbmN5IGFuZCBib29sZWFuIG1hc2tzKS4gTWFzdGVyaW5nIHRoZXNlIHJlcGxhY2VzIHNsb3cgUHl0aG9uIGxvb3BzIHdpdGggZmFzdCwgcmVhZGFibGUgYXJyYXkgZXhwcmVzc2lvbnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJWZWN0b3JpemVkIG9wczogQy1jb21waWxlZCwgbm8gUHl0aG9uIGxvb3Agb3ZlcmhlYWQg4oCUIDEw4oCTMTAwMHggZmFzdGVyIHRoYW4gZm9yIGxvb3BzIGZvciBudW1lcmljYWwgd29yayIsIkJyb2FkY2FzdGluZzogaW1wbGljaXQgc2hhcGUgYWxpZ25tZW50IHdpdGhvdXQgZGF0YSBjb3B5aW5nIOKAlCBzaGFwZXMgZXhwYW5kZWQgbG9naWNhbGx5LCBub3QgcGh5c2ljYWxseSIsIkZhbmN5IGluZGV4aW5nOiBzZWxlY3QgYXJiaXRyYXJ5IGVsZW1lbnRzIHdpdGggaW50ZWdlciBhcnJheXMg4oCUIGFsd2F5cyByZXR1cm5zIGEgY29weSAoc2FmZSB0byBtb2RpZnkpIiwiQm9vbGVhbiBpbmRleGluZzogbWFzayBhcnJheXMgd2l0aCBib29sZWFuIGNvbmRpdGlvbnMg4oCUIHVzZSBucC53aGVyZSBmb3IgY29uZGl0aW9uYWwgYXNzaWdubWVudCIsImVpbnN1bTogRWluc3RlaW4gbm90YXRpb24gZm9yIGFyYml0cmFyeSB0ZW5zb3IgY29udHJhY3Rpb25zIOKAlCBjbGVhcmVyIGFuZCBvZnRlbiBmYXN0ZXIgdGhhbiBjaGFpbmVkIGRvdHMiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVmVjdG9yaXphdGlvbjogUmVwbGFjaW5nIFB5dGhvbiBMb29wcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHl0aG9uIGxvb3BzIG92ZXIgYXJyYXkgZWxlbWVudHMgYXJlIHNsb3cgYmVjYXVzZSBlYWNoIGl0ZXJhdGlvbiBpbmN1cnMgUHl0aG9uIGludGVycHJldGVyIG92ZXJoZWFkLiBOdW1QeSBvcGVyYXRpb25zIGV4ZWN1dGUgaW4gQyBvdmVyIGNvbnRpZ3VvdXMgbWVtb3J5IGJsb2NrcyDigJQgMTAgdG8gMTAwMHggZmFzdGVyIGZvciBudW1lcmljYWwgY29tcHV0YXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0aW1lXG5cbiMgQmVuY2htYXJrOiBjb21wdXRlIHBhaXJ3aXNlIHNxdWFyZWQgZGlzdGFuY2VzXG4jIFB5dGhvbiBsb29wIHZlcnNpb25cbmRlZiBwYWlyd2lzZV9kaXN0X3B5dGhvbihYKTpcbiAgICBuID0gbGVuKFgpXG4gICAgRCA9IG5wLnplcm9zKChuLCBuKSlcbiAgICBmb3IgaSBpbiByYW5nZShuKTpcbiAgICAgICAgZm9yIGogaW4gcmFuZ2Uobik6XG4gICAgICAgICAgICBkaWZmID0gWFtpXSAtIFhbal1cbiAgICAgICAgICAgIERbaSwgal0gPSBucC5kb3QoZGlmZiwgZGlmZilcbiAgICByZXR1cm4gRFxuXG4jIFZlY3Rvcml6ZWQgdmVyc2lvbiB1c2luZyBicm9hZGNhc3RpbmdcbmRlZiBwYWlyd2lzZV9kaXN0X251bXB5KFgpOlxuICAgICMgfHx4X2kgLSB4X2p8fF4yID0gfHx4X2l8fF4yICsgfHx4X2p8fF4yIC0gMiB4X2nCt3hfalxuICAgIHNxX25vcm1zID0gKFggKiogMikuc3VtKGF4aXM9MSkgICAgICAgIyAobiwpXG4gICAgRCA9IHNxX25vcm1zWzosIE5vbmVdICsgc3Ffbm9ybXNbTm9uZSwgOl0gLSAyICogWCBAIFguVFxuICAgIHJldHVybiBucC5tYXhpbXVtKEQsIDApICAgICAgICAgICAgICAgIyBjbGlwIG51bWVyaWNhbCBuZWdhdGl2ZXNcblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxuWCAgID0gcm5nLnN0YW5kYXJkX25vcm1hbCgoMjAwLCAzMikpXG5cbnQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuRF9weSA9IHBhaXJ3aXNlX2Rpc3RfcHl0aG9uKFgpXG5weV90ID0gdGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwXG5cbnQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuRF9ucCA9IHBhaXJ3aXNlX2Rpc3RfbnVtcHkoWClcbm5wX3QgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gdDBcblxucHJpbnQoZlx1MDAyN1B5dGhvbiBsb29wOiB7cHlfdCoxMDAwOi4xZn0gbXNcdTAwMjcpXG5wcmludChmXHUwMDI3TnVtUHkgdmVjOiAgIHtucF90KjEwMDA6LjJmfSBtc1x1MDAyNylcbnByaW50KGZcdTAwMjdTcGVlZHVwOiAgICAge3B5X3QvbnBfdDouMGZ9eFx1MDAyNylcbnByaW50KGZcdTAwMjdSZXN1bHRzIG1hdGNoOiB7bnAuYWxsY2xvc2UoRF9weSwgRF9ucCwgYXRvbD0xZS04KX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQnJvYWRjYXN0aW5nIFJ1bGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCcm9hZGNhc3RpbmcgYWxsb3dzIG9wZXJhdGlvbnMgYmV0d2VlbiBhcnJheXMgb2YgZGlmZmVyZW50IHNoYXBlcyB3aXRob3V0IGV4cGxpY2l0IGNvcHlpbmcuIFRoZSBydWxlcyBhcmUgYXBwbGllZCB0byB0cmFpbGluZyBkaW1lbnNpb25zOiBhcnJheXMgYXJlIGNvbXBhdGlibGUgaWYgY29ycmVzcG9uZGluZyBkaW1lbnNpb25zIGFyZSBlcXVhbCBvciBvbmUgb2YgdGhlbSBpcyAxLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3RlcCAxOiBQcmVwZW5kIDFzIHRvIHRoZSBzaG9ydGVyIHNoYXBlIHVudGlsIGJvdGggaGF2ZSB0aGUgc2FtZSBudW1iZXIgb2YgZGltZW5zaW9ucyIsIlN0ZXAgMjogT3V0cHV0IHNoYXBlID0gbWF4IG9mIGVhY2ggcGFpciBvZiBkaW1lbnNpb25zIChlcnJvciBpZiBuZWl0aGVyIGlzIDEgYW5kIHRoZXkgZGlmZmVyKSIsIkV4YW1wbGU6ICgzLCAxLCA1KSArICg0LCAxKSDihpIgKDMsIDEsIDUpICsgKDEsIDQsIDEpIOKGkiBvdXRwdXQgKDMsIDQsIDUpIiwiTm8gZGF0YSBpcyBjb3BpZWQg4oCUIGJyb2FkY2FzdGluZyBpcyBhIHZpcnR1YWwgcmVwbGljYXRpb24gYXBwbGllZCBkdXJpbmcgY29tcHV0YXRpb24iLCJDb21tb24gdXNlOiBzdWJ0cmFjdCByb3cgbWVhbiAoWCAtIFgubWVhbihheGlzPTEsIGtlZXBkaW1zPVRydWUpKSDigJQga2VlcGRpbXMgcHJlc2VydmVzIGJyb2FkY2FzdGFibGUgc2hhcGUiXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoMClcblggICA9IHJuZy5pbnRlZ2VycygwLCAxMCwgKDQsIDMpKSAgICMgKDQsIDMpIG1hdHJpeFxucHJpbnQoXHUwMDI3WCBzaGFwZTpcdTAwMjcsIFguc2hhcGUpXG5cbiMgU3VidHJhY3QgY29sdW1uIG1lYW4gKGJyb2FkY2FzdCBvdmVyIHJvd3MpXG5jb2xfbWVhbiA9IFgubWVhbihheGlzPTApICAgICAgICAgICAgIyAoMywpXG5YX2NlbnRlcmVkID0gWCAtIGNvbF9tZWFuICAgICAgICAgICAgIyAoNCwgMykgLSAoMywpIC1cdTAwM2UgYnJvYWRjYXN0cyB0byAoNCwgMylcbnByaW50KFx1MDAyN0NvbHVtbi1jZW50ZXJlZCBzaGFwZTpcdTAwMjcsIFhfY2VudGVyZWQuc2hhcGUpXG5cbiMgU3VidHJhY3Qgcm93IG1lYW5cbnJvd19tZWFuID0gWC5tZWFuKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSkgICMgKDQsIDEpIOKAlCBrZWVwZGltcyBwcmVzZXJ2ZXMgcmFua1xuWF9yb3dfY2VudGVyZWQgPSBYIC0gcm93X21lYW4gICAgICAgICAgICAgIyAoNCwgMykgLSAoNCwgMSkgLVx1MDAzZSBicm9hZGNhc3RzIHRvICg0LCAzKVxucHJpbnQoXHUwMDI3Um93LWNlbnRlcmVkIHNoYXBlOlx1MDAyNywgWF9yb3dfY2VudGVyZWQuc2hhcGUpXG5cbiMgT3V0ZXIgcHJvZHVjdCB2aWEgYnJvYWRjYXN0aW5nXG5hID0gbnAuYXJyYXkoWzEsIDIsIDNdKSAgICMgKDMsKVxuYiA9IG5wLmFycmF5KFsxMCwgMjBdKSAgICAjICgyLClcbm91dGVyID0gYVs6LCBOb25lXSAqIGJbTm9uZSwgOl0gICMgKDMsIDEpICogKDEsIDIpIC1cdTAwM2UgKDMsIDIpXG5wcmludChcdTAwMjdPdXRlciBwcm9kdWN0Olx1MDAyNywgb3V0ZXIpXG5cbiMgUGFpcndpc2UgZGlmZmVyZW5jZXMgYmV0d2VlbiB0d28gc2V0cyBvZiBwb2ludHNcbkEgPSBybmcuc3RhbmRhcmRfbm9ybWFsKCg1LCA0KSkgICMgNSBwb2ludHMgaW4gUl40XG5CID0gcm5nLnN0YW5kYXJkX25vcm1hbCgoMywgNCkpICAjIDMgcG9pbnRzIGluIFJeNFxuZGlmZiA9IEFbOiwgTm9uZSwgOl0gLSBCW05vbmUsIDosIDpdICAjICg1LCAxLCA0KSAtICgxLCAzLCA0KSAtXHUwMDNlICg1LCAzLCA0KVxucHJpbnQoXHUwMDI3UGFpcndpc2UgZGlmZiBzaGFwZTpcdTAwMjcsIGRpZmYuc2hhcGUpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWR2YW5jZWQgSW5kZXhpbmc6IEZhbmN5IGFuZCBCb29sZWFuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBZHZhbmNlZCBpbmRleGluZyBzZWxlY3RzIGFyYml0cmFyeSBzdWJzZXRzIG9mIGFuIGFycmF5IGJ5IHByb3ZpZGluZyBpbnRlZ2VyIGFycmF5cyAoZmFuY3kgaW5kZXhpbmcg4oCUIGdhdGhlciBvcGVyYXRpb24pIG9yIGJvb2xlYW4gbWFza3MuIEFkdmFuY2VkIGluZGV4aW5nIGFsd2F5cyByZXR1cm5zIGEgY29weSwgdW5saWtlIGJhc2ljIHNsaWNpbmcgd2hpY2ggcmV0dXJucyBhIHZpZXcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5YICAgPSBybmcuaW50ZWdlcnMoMCwgMTAwLCAoOCwgNSkpXG5wcmludChcdTAwMjdYIHNoYXBlOlx1MDAyNywgWC5zaGFwZSlcblxuIyBGYW5jeSBpbmRleGluZzogc2VsZWN0IHNwZWNpZmljIHJvd3MgYnkgaW5kZXggYXJyYXlcbnJvd19pbmRpY2VzID0gbnAuYXJyYXkoWzAsIDMsIDcsIDJdKVxuc2VsZWN0ZWQgPSBYW3Jvd19pbmRpY2VzXSAgICAjICg0LCA1KSDigJQgY29waWVzIHJvd3MgMCwgMywgNywgMlxucHJpbnQoXHUwMDI3RmFuY3kgaW5kZXhlZCBzaGFwZTpcdTAwMjcsIHNlbGVjdGVkLnNoYXBlKVxuXG4jIEJvb2xlYW4gaW5kZXhpbmcgKG1hc2spXG5tYXNrID0gWFs6LCAwXSBcdTAwM2UgNTAgICAgICAgICAgIyAoOCwpIGJvb2xlYW4gbWFzayBvbiBmaXJzdCBjb2x1bW5cblhfZmlsdGVyZWQgPSBYW21hc2tdICAgICAgICAgIyByb3dzIHdoZXJlIGZpcnN0IGNvbHVtbiBcdTAwM2UgNTBcbnByaW50KGZcdTAwMjdCb29sZWFuIGZpbHRlcmVkOiB7WF9maWx0ZXJlZC5zaGFwZVswXX0gcm93cyBrZXB0XHUwMDI3KVxuXG4jIENvbWJpbmVkOiBmYW5jeSByb3cgKyBjb2x1bW4gaW5kZXhpbmcgKGdhdGhlcilcbnJvd3MgPSBucC5hcnJheShbMCwgMSwgMiwgM10pXG5jb2xzID0gbnAuYXJyYXkoWzQsIDMsIDIsIDFdKSAgIyBvbmUgY29sIHBlciByb3dcbmRpYWdfbGlrZSA9IFhbcm93cywgY29sc10gICAgICAjICg0LCkg4oCUIGVsZW1lbnQgKDAsNCksICgxLDMpLCAoMiwyKSwgKDMsMSlcbnByaW50KFx1MDAyN1NjYXR0ZXIgZ2F0aGVyIHJlc3VsdDpcdTAwMjcsIGRpYWdfbGlrZSlcblxuIyBTY2F0dGVyOiBwbGFjZSB2YWx1ZXMgYXQgc3BlY2lmaWMgaW5kaWNlc1xub3V0ID0gbnAuemVyb3MoKDEwLCA1KSwgZHR5cGU9aW50KVxub3V0W3Jvd19pbmRpY2VzXSA9IHNlbGVjdGVkICAgICMgc2NhdHRlciByb3dzIGJhY2tcbnByaW50KFx1MDAyN1NjYXR0ZXIgb3V0cHV0IHNoYXBlOlx1MDAyNywgb3V0LnNoYXBlKVxuXG4jIEFkdmFuY2VkIGluZGV4IGlzIGEgQ09QWSDigJQgbW9kaWZ5aW5nIGRvZXMgbm90IGFmZmVjdCBvcmlnaW5hbFxuWF9maWx0ZXJlZFswLCAwXSA9IDk5OVxucHJpbnQoZlx1MDAyN09yaWdpbmFsIFhbMCwwXSB1bmNoYW5nZWQ6IHtYWzAsMF0gIT0gOTk5fVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJlaW5zdW0gZm9yIFRlbnNvciBDb250cmFjdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Im5wLmVpbnN1bSAoRWluc3RlaW4gc3VtbWF0aW9uIG5vdGF0aW9uKSBleHByZXNzZXMgYXJiaXRyYXJ5IHRlbnNvciBvcGVyYXRpb25zIGluIGEgY29uY2lzZSBzdHJpbmcgc3ludGF4LiBJdCByZXBsYWNlcyBuZXN0ZWQgZG90IHByb2R1Y3RzLCB0cmFuc3Bvc2l0aW9ucywgYW5kIHRyYWNlIG9wZXJhdGlvbnMgd2l0aCBhIHNpbmdsZSByZWFkYWJsZSBleHByZXNzaW9uLCBhbmQgY2FuIGJlIGNvbXBpbGVkIHRvIG9wdGltaXplZCBCTEFTIGNhbGxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxucm5nICA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZygwKVxuQSAgICA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoKDMsIDQpKVxuQiAgICA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoKDQsIDUpKVxuQyAgICA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoKDMsIDQsIDUpKVxuRCAgICA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoKDMsIDQpKVxuXG4jIE1hdHJpeCBtdWx0aXBseTogaWosamsgLVx1MDAzZSBpa1xuQUIgICA9IG5wLmVpbnN1bShcdTAwMjdpaixqay1cdTAwM2Vpa1x1MDAyNywgQSwgQilcbmFzc2VydCBBQi5zaGFwZSA9PSAoMywgNSlcbmFzc2VydCBucC5hbGxjbG9zZShBQiwgQSBAIEIpXG5wcmludChmXHUwMDI3bWF0bXVsOiAgICAgICAge0FCLnNoYXBlfVx1MDAyNylcblxuIyBPdXRlciBwcm9kdWN0OiBpLGogLVx1MDAzZSBpalxuYSwgYiA9IG5wLmFycmF5KFsxLiwgMi4sIDMuXSksIG5wLmFycmF5KFsxMC4sIDIwLiwgMzAuLCA0MC5dKVxub3V0ZXIgPSBucC5laW5zdW0oXHUwMDI3aSxqLVx1MDAzZWlqXHUwMDI3LCBhLCBiKVxuYXNzZXJ0IG5wLmFsbGNsb3NlKG91dGVyLCBucC5vdXRlcihhLCBiKSlcbnByaW50KGZcdTAwMjdvdXRlciBwcm9kdWN0OiB7b3V0ZXIuc2hhcGV9XHUwMDI3KVxuXG4jIFRyYWNlOiBpaSAtXHUwMDNlIChzY2FsYXIpXG5zcSA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoKDUsIDUpKVxudHJhY2UgPSBucC5laW5zdW0oXHUwMDI3aWktXHUwMDNlXHUwMDI3LCBzcSlcbmFzc2VydCBucC5pc2Nsb3NlKHRyYWNlLCBucC50cmFjZShzcSkpXG5wcmludChmXHUwMDI3dHJhY2U6ICAgICAgICAge3RyYWNlOi40Zn1cdTAwMjcpXG5cbiMgQmF0Y2ggbWF0cml4IG11bHRpcGx5OiBiaWosYmprIC1cdTAwM2UgYmlrXG5iYXRjaF9BID0gcm5nLnN0YW5kYXJkX25vcm1hbCgoOCwgMywgNCkpXG5iYXRjaF9CID0gcm5nLnN0YW5kYXJkX25vcm1hbCgoOCwgNCwgNSkpXG5iYXRjaF9BQiA9IG5wLmVpbnN1bShcdTAwMjdiaWosYmprLVx1MDAzZWJpa1x1MDAyNywgYmF0Y2hfQSwgYmF0Y2hfQilcbmFzc2VydCBiYXRjaF9BQi5zaGFwZSA9PSAoOCwgMywgNSlcbnByaW50KGZcdTAwMjdiYXRjaCBtYXRtdWw6ICB7YmF0Y2hfQUIuc2hhcGV9XHUwMDI3KVxuXG4jIEF0dGVudGlvbiBzY29yZXM6IGJocWQsYmhrZCAtXHUwMDNlIGJocWtcblEgPSBybmcuc3RhbmRhcmRfbm9ybWFsKCgyLCA0LCAxMCwgNjQpKSAgIyBiYXRjaCwgaGVhZHMsIHF1ZXJpZXMsIGRcbksgPSBybmcuc3RhbmRhcmRfbm9ybWFsKCgyLCA0LCAxMiwgNjQpKSAgIyBiYXRjaCwgaGVhZHMsIGtleXMsIGRcbnNjb3JlcyA9IG5wLmVpbnN1bShcdTAwMjdiaHFkLGJoa2QtXHUwMDNlYmhxa1x1MDAyNywgUSwgSylcbnByaW50KGZcdTAwMjdhdHRlbnRpb246ICAgICB7c2NvcmVzLnNoYXBlfVx1MDAyNykgICMgKDIsIDQsIDEwLCAxMikifSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiZWluc3VtIFBhdHRlcm4gUmVmZXJlbmNlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk9wZXJhdGlvbiIsImVpbnN1bSBOb3RhdGlvbiIsIkVxdWl2YWxlbnQgTnVtUHkgQ2FsbCIsIlVzZSBDYXNlIl0sInJvd3MiOltbIk1hdHJpeCBtdWx0aXBseSIsImlqLGprLVx1MDAzZWlrIiwiQSBAIEIiLCJMaW5lYXIgbGF5ZXJzLCBhdHRlbnRpb24iXSxbIk91dGVyIHByb2R1Y3QiLCJpLGotXHUwMDNlaWoiLCJucC5vdXRlcihhLCBiKSIsIlJhbmstMSB1cGRhdGUsIGVtYmVkZGluZyBvdXRlciJdLFsiVHJhY2UiLCJpaS1cdTAwM2UiLCJucC50cmFjZShBKSIsIlJlZ3VsYXJpemF0aW9uIHRlcm1zIl0sWyJCYXRjaCBtYXRtdWwiLCJiaWosYmprLVx1MDAzZWJpayIsIm5wLm1hdG11bChBLCBCKSIsIkJhdGNoZWQgbGluZWFyIHRyYW5zZm9ybXMiXSxbIkF0dGVudGlvbiBzY29yZXMiLCJiaHFkLGJoa2QtXHUwMDNlYmhxayIsIihRIEAgSy5UKSBwZXIgaGVhZCIsIk11bHRpLWhlYWQgc2VsZi1hdHRlbnRpb24iXSxbIkVsZW1lbnQgc3VtIG92ZXIgYXhpcyIsImlqLVx1MDAzZWkiLCJBLnN1bShheGlzPTEpIiwiUm93IHJlZHVjdGlvbiJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgcGVyZm9ybWFuY2UtY3JpdGljYWwgcGF0aHMsIGJlbmNobWFyayBucC5laW5zdW0gYWdhaW5zdCBtYW51YWwgQCBjaGFpbnMuIE9uIHNtYWxsIGFycmF5cywgZWluc3VtIG92ZXJoZWFkIGNhbiBkb21pbmF0ZTsgb24gbGFyZ2UgdGVuc29ycyAoXHUwMDNlMTAwMCBlbGVtZW50cyBwZXIgZGltZW5zaW9uKSwgZWluc3VtIG9mdGVuIG1hdGNoZXMgb3IgYmVhdHMgbWFudWFsIGltcGxlbWVudGF0aW9ucyBiZWNhdXNlIE51bVB5IHNlbGVjdHMgb3B0aW1hbCBCTEFTIHJvdXRpbmVzIGludGVybmFsbHkuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6ImVpbnN1bSBPcHRpbWl6YXRpb24gd2l0aCBvcHRpbWl6ZT1UcnVlIiwiY29udGVudCI6IkZvciBlaW5zdW0gZXhwcmVzc2lvbnMgaW52b2x2aW5nIHRocmVlIG9yIG1vcmUgdGVuc29ycywgdXNlIG5wLmVpbnN1bShcdTAwMjcuLi5cdTAwMjcsIEEsIEIsIEMsIG9wdGltaXplPVRydWUpLiBOdW1QeSBmaW5kcyB0aGUgb3B0aW1hbCBjb250cmFjdGlvbiBvcmRlciDigJQgd2hpY2ggY2FuIHJlZHVjZSBjb21wbGV4aXR5IGZyb20gTyhuXjYpIHRvIE8obl40KSBmb3IgYSB0aHJlZS10ZW5zb3IgY29udHJhY3Rpb24uIEFsd2F5cyBiZW5jaG1hcmsgYWdhaW5zdCBtYW51YWwgQCBjaGFpbnMgZm9yIHBlcmZvcm1hbmNlLWNyaXRpY2FsIHBhdGhzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlZlY3Rvcml6YXRpb24gcmVwbGFjZXMgUHl0aG9uIGxvb3BzIHdpdGggQy1jb21waWxlZCBhcnJheSBvcGVyYXRpb25zIOKAlCAxMC0xMDAweCBzcGVlZHVwIiwiQnJvYWRjYXN0aW5nOiBhbGlnbiB0cmFpbGluZyBkaW1zLCBwcmVwZW5kIDFzIHRvIHNob3J0ZXIgc2hhcGUsIGV4cGFuZCBkaW1zIHdpdGggc2l6ZSAxIOKAlCBubyBkYXRhIGNvcHkiLCJGYW5jeSBpbmRleGluZyByZXR1cm5zIGEgY29weTsgYmFzaWMgc2xpY2luZyByZXR1cm5zIGEgdmlldyDigJQgbW9kaWZ5aW5nIGEgZmFuY3kgaW5kZXggcmVzdWx0IGlzIHNhZmUiLCJlaW5zdW0gZXhwcmVzc2VzIGFyYml0cmFyeSB0ZW5zb3IgY29udHJhY3Rpb25zIGluIEVpbnN0ZWluIG5vdGF0aW9uIOKAlCBjbGVhcmVyIHRoYW4gbmVzdGVkIHRyYW5zcG9zZXMgYW5kIGRvdHMiLCJVc2Ugb3B0aW1pemU9VHJ1ZSBpbiBlaW5zdW0gZm9yIG11bHRpLXRlbnNvciBjb250cmFjdGlvbnMgYW5kIG5wLmVpbnN1bV9wYXRoIGZvciBwcm9maWxpbmcgdGhlIGNvbnRyYWN0aW9uIG9yZGVyIl19XQ=="
---
# NumPy — Broadcasting, Vectorization, and Advanced Indexing

NumPy is the foundation of scientific Python computing. Its performance advantage over pure Python comes from three mechanisms: vectorized operations (C-compiled kernels over entire arrays), broadcasting (implicit shape alignment without copying), and advanced indexing (fancy and boolean masks). Mastering these replaces slow Python loops with fast, readable array expressions.

- Vectorized ops: C-compiled, no Python loop overhead — 10–1000x faster than for loops for numerical work
- Broadcasting: implicit shape alignment without data copying — shapes expanded logically, not physically
- Fancy indexing: select arbitrary elements with integer arrays — always returns a copy (safe to modify)
- Boolean indexing: mask arrays with boolean conditions — use np.where for conditional assignment
- einsum: Einstein notation for arbitrary tensor contractions — clearer and often faster than chained dots

## Vectorization: Replacing Python Loops

Python loops over array elements are slow because each iteration incurs Python interpreter overhead. NumPy operations execute in C over contiguous memory blocks — 10 to 1000x faster for numerical computations.

```python
import numpy as np
import time

# Benchmark: compute pairwise squared distances
# Python loop version
def pairwise_dist_python(X):
    n = len(X)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            diff = X[i] - X[j]
            D[i, j] = np.dot(diff, diff)
    return D

# Vectorized version using broadcasting
def pairwise_dist_numpy(X):
    # ||x_i - x_j||^2 = ||x_i||^2 + ||x_j||^2 - 2 x_i·x_j
    sq_norms = (X ** 2).sum(axis=1)       # (n,)
    D = sq_norms[:, None] + sq_norms[None, :] - 2 * X @ X.T
    return np.maximum(D, 0)               # clip numerical negatives

rng = np.random.default_rng(42)
X   = rng.standard_normal((200, 32))

t0 = time.perf_counter()
D_py = pairwise_dist_python(X)
py_t = time.perf_counter() - t0

t0 = time.perf_counter()
D_np = pairwise_dist_numpy(X)
np_t = time.perf_counter() - t0

print(f'Python loop: {py_t*1000:.1f} ms')
print(f'NumPy vec:   {np_t*1000:.2f} ms')
print(f'Speedup:     {py_t/np_t:.0f}x')
print(f'Results match: {np.allclose(D_py, D_np, atol=1e-8)}')
```

## Broadcasting Rules

Broadcasting allows operations between arrays of different shapes without explicit copying. The rules are applied to trailing dimensions: arrays are compatible if corresponding dimensions are equal or one of them is 1.

- Step 1: Prepend 1s to the shorter shape until both have the same number of dimensions
- Step 2: Output shape = max of each pair of dimensions (error if neither is 1 and they differ)
- Example: (3, 1, 5) + (4, 1) → (3, 1, 5) + (1, 4, 1) → output (3, 4, 5)
- No data is copied — broadcasting is a virtual replication applied during computation
- Common use: subtract row mean (X - X.mean(axis=1, keepdims=True)) — keepdims preserves broadcastable shape

```python
import numpy as np

rng = np.random.default_rng(0)
X   = rng.integers(0, 10, (4, 3))   # (4, 3) matrix
print('X shape:', X.shape)

# Subtract column mean (broadcast over rows)
col_mean = X.mean(axis=0)            # (3,)
X_centered = X - col_mean            # (4, 3) - (3,) -> broadcasts to (4, 3)
print('Column-centered shape:', X_centered.shape)

# Subtract row mean
row_mean = X.mean(axis=1, keepdims=True)  # (4, 1) — keepdims preserves rank
X_row_centered = X - row_mean             # (4, 3) - (4, 1) -> broadcasts to (4, 3)
print('Row-centered shape:', X_row_centered.shape)

# Outer product via broadcasting
a = np.array([1, 2, 3])   # (3,)
b = np.array([10, 20])    # (2,)
outer = a[:, None] * b[None, :]  # (3, 1) * (1, 2) -> (3, 2)
print('Outer product:', outer)

# Pairwise differences between two sets of points
A = rng.standard_normal((5, 4))  # 5 points in R^4
B = rng.standard_normal((3, 4))  # 3 points in R^4
diff = A[:, None, :] - B[None, :, :]  # (5, 1, 4) - (1, 3, 4) -> (5, 3, 4)
print('Pairwise diff shape:', diff.shape)
```

## Advanced Indexing: Fancy and Boolean

Advanced indexing selects arbitrary subsets of an array by providing integer arrays (fancy indexing — gather operation) or boolean masks. Advanced indexing always returns a copy, unlike basic slicing which returns a view.

```python
import numpy as np

rng = np.random.default_rng(42)
X   = rng.integers(0, 100, (8, 5))
print('X shape:', X.shape)

# Fancy indexing: select specific rows by index array
row_indices = np.array([0, 3, 7, 2])
selected = X[row_indices]    # (4, 5) — copies rows 0, 3, 7, 2
print('Fancy indexed shape:', selected.shape)

# Boolean indexing (mask)
mask = X[:, 0] > 50          # (8,) boolean mask on first column
X_filtered = X[mask]         # rows where first column > 50
print(f'Boolean filtered: {X_filtered.shape[0]} rows kept')

# Combined: fancy row + column indexing (gather)
rows = np.array([0, 1, 2, 3])
cols = np.array([4, 3, 2, 1])  # one col per row
diag_like = X[rows, cols]      # (4,) — element (0,4), (1,3), (2,2), (3,1)
print('Scatter gather result:', diag_like)

# Scatter: place values at specific indices
out = np.zeros((10, 5), dtype=int)
out[row_indices] = selected    # scatter rows back
print('Scatter output shape:', out.shape)

# Advanced index is a COPY — modifying does not affect original
X_filtered[0, 0] = 999
print(f'Original X[0,0] unchanged: {X[0,0] != 999}')
```

## einsum for Tensor Contractions

np.einsum (Einstein summation notation) expresses arbitrary tensor operations in a concise string syntax. It replaces nested dot products, transpositions, and trace operations with a single readable expression, and can be compiled to optimized BLAS calls.

```python
import numpy as np

rng  = np.random.default_rng(0)
A    = rng.standard_normal((3, 4))
B    = rng.standard_normal((4, 5))
C    = rng.standard_normal((3, 4, 5))
D    = rng.standard_normal((3, 4))

# Matrix multiply: ij,jk -> ik
AB   = np.einsum('ij,jk->ik', A, B)
assert AB.shape == (3, 5)
assert np.allclose(AB, A @ B)
print(f'matmul:        {AB.shape}')

# Outer product: i,j -> ij
a, b = np.array([1., 2., 3.]), np.array([10., 20., 30., 40.])
outer = np.einsum('i,j->ij', a, b)
assert np.allclose(outer, np.outer(a, b))
print(f'outer product: {outer.shape}')

# Trace: ii -> (scalar)
sq = rng.standard_normal((5, 5))
trace = np.einsum('ii->', sq)
assert np.isclose(trace, np.trace(sq))
print(f'trace:         {trace:.4f}')

# Batch matrix multiply: bij,bjk -> bik
batch_A = rng.standard_normal((8, 3, 4))
batch_B = rng.standard_normal((8, 4, 5))
batch_AB = np.einsum('bij,bjk->bik', batch_A, batch_B)
assert batch_AB.shape == (8, 3, 5)
print(f'batch matmul:  {batch_AB.shape}')

# Attention scores: bhqd,bhkd -> bhqk
Q = rng.standard_normal((2, 4, 10, 64))  # batch, heads, queries, d
K = rng.standard_normal((2, 4, 12, 64))  # batch, heads, keys, d
scores = np.einsum('bhqd,bhkd->bhqk', Q, K)
print(f'attention:     {scores.shape}')  # (2, 4, 10, 12)
```

---

## einsum Pattern Reference

| Operation | einsum Notation | Equivalent NumPy Call | Use Case |
| --- | --- | --- | --- |
| Matrix multiply | ij,jk->ik | A @ B | Linear layers, attention |
| Outer product | i,j->ij | np.outer(a, b) | Rank-1 update, embedding outer |
| Trace | ii-> | np.trace(A) | Regularization terms |
| Batch matmul | bij,bjk->bik | np.matmul(A, B) | Batched linear transforms |
| Attention scores | bhqd,bhkd->bhqk | (Q @ K.T) per head | Multi-head self-attention |
| Element sum over axis | ij->i | A.sum(axis=1) | Row reduction |

For performance-critical paths, benchmark np.einsum against manual @ chains. On small arrays, einsum overhead can dominate; on large tensors (>1000 elements per dimension), einsum often matches or beats manual implementations because NumPy selects optimal BLAS routines internally.

> **einsum Optimization with optimize=True**: For einsum expressions involving three or more tensors, use np.einsum('...', A, B, C, optimize=True). NumPy finds the optimal contraction order — which can reduce complexity from O(n^6) to O(n^4) for a three-tensor contraction. Always benchmark against manual @ chains for performance-critical paths.

## Key Takeaways

- Vectorization replaces Python loops with C-compiled array operations — 10-1000x speedup
- Broadcasting: align trailing dims, prepend 1s to shorter shape, expand dims with size 1 — no data copy
- Fancy indexing returns a copy; basic slicing returns a view — modifying a fancy index result is safe
- einsum expresses arbitrary tensor contractions in Einstein notation — clearer than nested transposes and dots
- Use optimize=True in einsum for multi-tensor contractions and np.einsum_path for profiling the contraction order

