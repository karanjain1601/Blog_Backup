---
title: "Learned Positional Embeddings — BERT and GPT Style"
slug: "learned-positional-embeddings"
description: "Explore nn.Embedding(max_seq_len, d_model) as a trainable lookup table for positional encoding: parameter count, BERT and GPT-2 maximum lengths, addition to token embeddings, extrapolation failure at lengths beyond training, position interpolation, and empirical comparison against sinusoidal PE."
tags: ["deep-learning", "transformers", "positional-encoding"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhbnNmb3JtZXJzIGhhdmUgbm8gYnVpbHQtaW4gbm90aW9uIG9mIG9yZGVyIOKAlCBhIHNldCBvZiB0b2tlbiBlbWJlZGRpbmdzIHBhc3NlZCB0aHJvdWdoIHNlbGYtYXR0ZW50aW9uIGlzIHBlcm11dGF0aW9uLWVxdWl2YXJpYW50IHdpdGhvdXQgYWRkaXRpb25hbCBzdHJ1Y3R1cmUuIFBvc2l0aW9uYWwgaW5mb3JtYXRpb24gbXVzdCBiZSBpbmplY3RlZCBleHBsaWNpdGx5LiBCRVJUIGFuZCBHUFQtZmFtaWx5IG1vZGVscyBkbyB0aGlzIHdpdGggbGVhcm5lZCBwb3NpdGlvbmFsIGVtYmVkZGluZ3M6IGFuIG5uLkVtYmVkZGluZyhtYXhfc2VxX2xlbiwgZF9tb2RlbCkgbG9va3VwIHRhYmxlIHRyYWluZWQgZW5kLXRvLWVuZCBhbG9uZ3NpZGUgdGhlIHJlc3Qgb2YgdGhlIG1vZGVsLiBFYWNoIHBvc2l0aW9uIGluZGV4IDAsIDEsIOKApiwgbWF4X3NlcV9sZW7iiJIxIG1hcHMgdG8gYSBkZWRpY2F0ZWQgZC1kaW1lbnNpb25hbCB2ZWN0b3IgdGhhdCBpcyBhZGRlZCAobm90IGNvbmNhdGVuYXRlZCkgdG8gdGhlIGNvcnJlc3BvbmRpbmcgdG9rZW4gZW1iZWRkaW5nIGJlZm9yZSB0aGUgZmlyc3QgVHJhbnNmb3JtZXIgbGF5ZXIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFRyYW5zZm9ybWVycyBOZWVkIFBvc2l0aW9uYWwgSW5mb3JtYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNlbGYtYXR0ZW50aW9uIGNvbXB1dGVzIGEgd2VpZ2h0ZWQgc3VtIG9mIHZhbHVlIHZlY3RvcnMgdXNpbmcgcXVlcnkta2V5IGRvdCBwcm9kdWN0cy4gSWYgeW91IHBlcm11dGUgdGhlIGlucHV0IHNlcXVlbmNlLCBldmVyeSBwYWlyd2lzZSBkb3QgcHJvZHVjdCBjaGFuZ2VzLCBidXQgdGhlIHNhbWUgc2V0IG9mIG91dHB1dHMgaXMgcHJvZHVjZWQg4oCUIGp1c3QgcmVvcmRlcmVkLiBUaGlzIG1lYW5zIHRoZSBtb2RlbCBjYW5ub3QgZGlzdGluZ3Vpc2ggXHUwMDI3dGhlIGNhdCBzYXRcdTAwMjcgZnJvbSBcdTAwMjdzYXQgY2F0IHRoZVx1MDAyNyB3aXRob3V0IGFuIGV4dGVybmFsIHBvc2l0aW9uIHNpZ25hbC4gU2ludXNvaWRhbCBhbmQgbGVhcm5lZCBlbWJlZGRpbmdzIGJvdGggc29sdmUgdGhpcyBieSBtYWtpbmcgZWFjaCBwb3NpdGlvblx1MDAyN3MgZW1iZWRkaW5nIHVuaXF1ZSwgc28gYWZ0ZXIgYWRkaXRpb24gdGhlIGF0dGVudGlvbiBzY29yZXMgY2FycnkgcG9zaXRpb24tc2Vuc2l0aXZlIGluZm9ybWF0aW9uLiBUaGUgY2hvaWNlIGJldHdlZW4gc2ludXNvaWRhbCAoZml4ZWQgbWF0aGVtYXRpY2FsIGZvcm11bGEpIGFuZCBsZWFybmVkICh0cmFpbmFibGUgcGFyYW1ldGVycykgYWZmZWN0cyBwYXJhbWV0ZXIgY291bnQsIGV4dHJhcG9sYXRpb24sIGFuZCBwZXJmb3JtYW5jZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMZWFybmVkIFBvc2l0aW9uYWwgRW1iZWRkaW5ncyDigJQgQXJjaGl0ZWN0dXJlIGFuZCBEZXNpZ24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBpbXBsZW1lbnRhdGlvbiBpcyBhIHNpbmdsZSBubi5FbWJlZGRpbmcgbW9kdWxlLiBEdXJpbmcgYSBmb3J3YXJkIHBhc3MsIHRoZSBpbnRlZ2VyIHNlcXVlbmNlIFswLCAxLCDigKYsIEziiJIxXSBpcyBsb29rZWQgdXAgdG8gcHJvZHVjZSBhIChMLCBkX21vZGVsKSBtYXRyaXggdGhhdCBpcyBhZGRlZCBlbGVtZW50LXdpc2UgdG8gdGhlIHRva2VuIGVtYmVkZGluZyBtYXRyaXggb2YgdGhlIHNhbWUgc2hhcGUuIEJFUlQtYmFzZSB1c2VzIG1heF9zZXFfbGVuPTUxMiBhbmQgZF9tb2RlbD03NjgsIGdpdmluZyA1MTIgw5cgNzY4ID0gMzkzLDIxNiBwYXJhbWV0ZXJzIGluIHRoZSBwb3NpdGlvbiB0YWJsZS4gR1BULTIgc21hbGwgdXNlcyBtYXhfc2VxX2xlbj0xMDI0IHdpdGggZF9tb2RlbD03NjgsIGdpdmluZyA3ODYsNDMyIHBhcmFtZXRlcnMuIFRoZXNlIHBhcmFtZXRlcnMgYXJlIHNtYWxsIHJlbGF0aXZlIHRvIHRvdGFsIG1vZGVsIHNpemUgKEJFUlQtYmFzZSBoYXMgfjExME0gdG90YWwgcGFyYW1ldGVycykgYnV0IGltcG9ydGFudCBmb3IgcXVhbGl0eS4gU3RhbmRhcmQgaW5pdGlhbGlzYXRpb24gdXNlcyBOKDAsIDAuMDIpIG9yIE4oMCwgMS/iiJpkX21vZGVsKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgTGVhcm5lZFBvc2l0aW9uYWxFbWJlZGRpbmcobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbWF4X3NlcV9sZW4sIGRfbW9kZWwsIGRyb3BvdXQ9MC4xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYucG9zX2VtYmVkZGluZyA9IG5uLkVtYmVkZGluZyhtYXhfc2VxX2xlbiwgZF9tb2RlbClcbiAgICAgICAgc2VsZi5kcm9wb3V0ID0gbm4uRHJvcG91dChkcm9wb3V0KVxuICAgICAgICBzZWxmLl9pbml0X3dlaWdodHMoKVxuXG4gICAgZGVmIF9pbml0X3dlaWdodHMoc2VsZik6XG4gICAgICAgIG5uLmluaXQubm9ybWFsXyhzZWxmLnBvc19lbWJlZGRpbmcud2VpZ2h0LCBtZWFuPTAuMCwgc3RkPTAuMDIpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB0b2tlbl9lbWJlZGRpbmdzKTpcbiAgICAgICAgIyB0b2tlbl9lbWJlZGRpbmdzOiAoYmF0Y2gsIHNlcV9sZW4sIGRfbW9kZWwpXG4gICAgICAgIGJhdGNoLCBzZXFfbGVuLCBkX21vZGVsID0gdG9rZW5fZW1iZWRkaW5ncy5zaGFwZVxuICAgICAgICBwb3NpdGlvbnMgPSB0b3JjaC5hcmFuZ2Uoc2VxX2xlbiwgZGV2aWNlPXRva2VuX2VtYmVkZGluZ3MuZGV2aWNlKVxuICAgICAgICBwb3NfZW1iID0gc2VsZi5wb3NfZW1iZWRkaW5nKHBvc2l0aW9ucykgICAgICAgICAjIChzZXFfbGVuLCBkX21vZGVsKVxuICAgICAgICByZXR1cm4gc2VsZi5kcm9wb3V0KHRva2VuX2VtYmVkZGluZ3MgKyBwb3NfZW1iKSAjIGJyb2FkY2FzdHMgb3ZlciBiYXRjaFxuXG5tb2RlbCA9IExlYXJuZWRQb3NpdGlvbmFsRW1iZWRkaW5nKG1heF9zZXFfbGVuPTUxMiwgZF9tb2RlbD03NjgpXG54ID0gdG9yY2gucmFuZG4oMiwgMTAsIDc2OClcbm91dCA9IG1vZGVsKHgpXG5wcmludChcdTAwMjdJbnB1dDpcdTAwMjcsIHguc2hhcGUsIFx1MDAyNy1cdTAwM2UgT3V0cHV0Olx1MDAyNywgb3V0LnNoYXBlKVxucGFyYW1fY291bnQgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSlcbnByaW50KFx1MDAyN1BhcmFtZXRlcnM6XHUwMDI3LCBwYXJhbV9jb3VudCwgXHUwMDI3PT0gNTEyIHggNzY4ID1cdTAwMjcsIDUxMio3NjgsIFx1MDAyN2ZvciBCRVJULWJhc2VcdTAwMjcpXG5wcmludChcdTAwMjdFbWJlZGRpbmcgd2VpZ2h0IHNoYXBlOlx1MDAyNywgbW9kZWwucG9zX2VtYmVkZGluZy53ZWlnaHQuc2hhcGUpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUGFyYW1ldGVyIENvdW50IGFuZCBNZW1vcnkgRm9vdHByaW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQYXJhbWV0ZXIgY291bnQgc2NhbGVzIGxpbmVhcmx5IHdpdGggYm90aCBtYXhfc2VxX2xlbiBhbmQgZF9tb2RlbDogcGFyYW1zID0gbWF4X3NlcV9sZW4gw5cgZF9tb2RlbC4gRm9yIEJFUlQtbGFyZ2UgKG1heF9zZXFfbGVuPTUxMiwgZF9tb2RlbD0xMDI0KSB0aGlzIGlzIDUyNCwyODgg4oCUIHN0aWxsIGxlc3MgdGhhbiAwLjUlIG9mIHRoZSAzNDBNIHRvdGFsIHBhcmFtZXRlcnMuIE1lbW9yeSBjb3N0IGF0IGluZmVyZW5jZTogdGhlIGZ1bGwgZW1iZWRkaW5nIHRhYmxlIGlzIGFsd2F5cyBsb2FkZWQgaW50byBHUFUgbWVtb3J5IHJlZ2FyZGxlc3Mgb2YgdGhlIGFjdHVhbCBzZXF1ZW5jZSBsZW5ndGgsIHdoaWNoIG1hdHRlcnMgZm9yIGJhdGNoIGluZmVyZW5jZS4gVGhlIHRhYmxlIGZpdHMgaW4gfjMgTUIgZm9yIEJFUlQtYmFzZSAoMzkzSyDDlyA0IGJ5dGVzIGZsb2F0MzIpLCBuZWdsaWdpYmxlIGNvbXBhcmVkIHRvIGF0dGVudGlvbiBhbmQgRkZOIHdlaWdodHMuIER1cmluZyB0cmFpbmluZywgZ3JhZGllbnRzIGFjY3VtdWxhdGUgb25seSBmb3IgdGhlIHBvc2l0aW9uIHJvd3MgdGhhdCBhcHBlYXIgaW4gdGhlIGN1cnJlbnQgYmF0Y2gsIG1ha2luZyB0aGUgZWZmZWN0aXZlIGdyYWRpZW50IHVwZGF0ZSBzcGFyc2UuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJBZGRpdGlvbiB2cyBDb25jYXRlbmF0aW9uIiwiY29udGVudCI6IkxlYXJuZWQgcG9zaXRpb25hbCBlbWJlZGRpbmdzIGFyZSBhbHdheXMgYWRkZWQgdG8gdG9rZW4gZW1iZWRkaW5ncywgbmV2ZXIgY29uY2F0ZW5hdGVkLiBBZGRpdGlvbiBwcmVzZXJ2ZXMgZF9tb2RlbCBkaW1lbnNpb24gKG5vIHBhcmFtZXRlciBpbmNyZWFzZSBpbiBzdWJzZXF1ZW50IGxheWVycykgYW5kIGFsbG93cyB0aGUgbW9kZWwgdG8gbGVhcm4gYW55IGxpbmVhciBjb21iaW5hdGlvbiBvZiB0b2tlbiBhbmQgcG9zaXRpb24gaW5mb3JtYXRpb24gaW4gdGhlIGZpcnN0IGF0dGVudGlvbiBwcm9qZWN0aW9uLiBDb25jYXRlbmF0aW9uIHdvdWxkIHJlcXVpcmUgaGFsdmluZyBib3RoIHRva2VuIGFuZCBwb3NpdGlvbiBkaW1lbnNpb25zIG9yIGluY3JlYXNpbmcgYWxsIGRvd25zdHJlYW0gd2VpZ2h0IG1hdHJpY2VzIOKAlCBuZWl0aGVyIGlzIHN0YW5kYXJkIHByYWN0aWNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkV4dHJhcG9sYXRpb24gRmFpbHVyZSBCZXlvbmQgVHJhaW5pbmcgTGVuZ3RoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2VudHJhbCB3ZWFrbmVzcyBvZiBsZWFybmVkIHBvc2l0aW9uYWwgZW1iZWRkaW5ncyBpcyBoYXJkIGV4dHJhcG9sYXRpb24gZmFpbHVyZTogcG9zaXRpb24gaW5kZXggTCBpcyBzaW1wbHkgbm90IGluIHRoZSBlbWJlZGRpbmcgdGFibGUgaWYgTCDiiaUgbWF4X3NlcV9sZW4uIEF0dGVtcHRpbmcgYSBmb3J3YXJkIHBhc3Mgd2l0aCBhIHNlcXVlbmNlIGxvbmdlciB0aGFuIHRoZSB0cmFpbmluZyBtYXhpbXVtIHJhaXNlcyBhbiBJbmRleEVycm9yIG9yIHJldHVybnMgZ2FyYmFnZSAoaWYgaW5kaWNlcyBhcmUgY2xhbXBlZCkuIEV2ZW4gd2l0aG91dCBhbiBlcnJvciwgZW1waXJpY2FsIHJlc3VsdHMgc2hvdyBwZXJwbGV4aXR5IHNwaWtpbmcgc2hhcnBseSBhdCBsZW5ndGhzIGJleW9uZCB0aGUgdHJhaW5pbmcgbWF4aW11bSDigJQgdGhlIG1vZGVsIG5ldmVyIGVuY291bnRlcmVkIHRob3NlIHBvc2l0aW9uIHZlY3RvcnMgZHVyaW5nIHRyYWluaW5nLCBzbyB0aGV5IGFyZSBtZWFuaW5nbGVzcyB0byB0aGUgYXR0ZW50aW9uIGhlYWRzLiBUaGlzIGlzIGluIGNvbnRyYXN0IHRvIHNpbnVzb2lkYWwgUEUsIHdoaWNoIGlzIGRlZmluZWQgYnkgYSBjbG9zZWQtZm9ybSBmb3JtdWxhIGF0IGFueSBwb3NpdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgVGlueVRyYW5zZm9ybWVyTE0obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdm9jYWJfc2l6ZSwgZF9tb2RlbCwgbWF4X3NlcV9sZW4pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi50b2tlbl9lbWIgID0gbm4uRW1iZWRkaW5nKHZvY2FiX3NpemUsIGRfbW9kZWwpXG4gICAgICAgIHNlbGYucG9zX2VtYiAgICA9IG5uLkVtYmVkZGluZyhtYXhfc2VxX2xlbiwgZF9tb2RlbClcbiAgICAgICAgbGF5ZXIgPSBubi5UcmFuc2Zvcm1lckVuY29kZXJMYXllcihkX21vZGVsLCBuaGVhZD00LCBiYXRjaF9maXJzdD1UcnVlLCBkaW1fZmVlZGZvcndhcmQ9MTI4KVxuICAgICAgICBzZWxmLmVuY29kZXIgICAgPSBubi5UcmFuc2Zvcm1lckVuY29kZXIobGF5ZXIsIG51bV9sYXllcnM9MilcbiAgICAgICAgc2VsZi5oZWFkICAgICAgID0gbm4uTGluZWFyKGRfbW9kZWwsIHZvY2FiX3NpemUpXG4gICAgICAgIHNlbGYubWF4X3NlcV9sZW4gPSBtYXhfc2VxX2xlblxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHNlcV9sZW4gPSB4LnNoYXBlWzFdXG4gICAgICAgIHBvcyA9IHRvcmNoLmFyYW5nZShzZXFfbGVuLCBkZXZpY2U9eC5kZXZpY2UpXG4gICAgICAgIGVtYiA9IHNlbGYudG9rZW5fZW1iKHgpICsgc2VsZi5wb3NfZW1iKHBvcylcbiAgICAgICAgcmV0dXJuIHNlbGYuaGVhZChzZWxmLmVuY29kZXIoZW1iKSlcblxudG9yY2gubWFudWFsX3NlZWQoNDIpXG5tb2RlbCA9IFRpbnlUcmFuc2Zvcm1lckxNKHZvY2FiX3NpemU9MTAwLCBkX21vZGVsPTY0LCBtYXhfc2VxX2xlbj0zMilcbm1vZGVsLmV2YWwoKVxuY3JpdGVyaW9uID0gbm4uQ3Jvc3NFbnRyb3B5TG9zcygpXG5mb3Igc2VxX2xlbiBpbiBbMTYsIDMyLCA0MCwgNDhdOlxuICAgIHRyeTpcbiAgICAgICAgeCA9IHRvcmNoLnJhbmRpbnQoMCwgMTAwLCAoMSwgc2VxX2xlbikpXG4gICAgICAgIGxvZ2l0cyA9IG1vZGVsKHgpXG4gICAgICAgIGxvc3MgICA9IGNyaXRlcmlvbihsb2dpdHMudmlldygtMSwgMTAwKSwgeC52aWV3KC0xKSlcbiAgICAgICAgcHJpbnQoXHUwMDI3c2VxX2xlbj1cdTAwMjcgKyBzdHIoc2VxX2xlbikgKyBcdTAwMjcgIGxvc3M9XHUwMDI3ICsgc3RyKHJvdW5kKGxvc3MuaXRlbSgpLCAzKSkpXG4gICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOlxuICAgICAgICBwcmludChcdTAwMjdzZXFfbGVuPVx1MDAyNyArIHN0cihzZXFfbGVuKSArIFx1MDAyNyAgRVJST1I6IFx1MDAyNyArIHR5cGUoZSkuX19uYW1lX18pIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUG9zaXRpb24gSW50ZXJwb2xhdGlvbiBmb3IgTGVuZ3RoIEV4dGVuc2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUG9zaXRpb24gaW50ZXJwb2xhdGlvbiAoUHJlc3MgZXQgYWwuIDIwMjI7IENoZW4gZXQgYWwuIDIwMjMgZm9yIFJvUEUpIGFkYXB0cyBsZWFybmVkIGVtYmVkZGluZ3MgdG8gbG9uZ2VyIHNlcXVlbmNlcyBieSByZXNjYWxpbmcgcG9zaXRpb24gSURzIHNvIHRoYXQgbmV3IHBvc2l0aW9ucyBtYXAgaW50byB0aGUgdHJhaW5lZCByYW5nZS4gRm9yIGEgbW9kZWwgdHJhaW5lZCB3aXRoIG1heF9zZXFfbGVuPTUxMiB0aGF0IG5lZWRzIHRvIHByb2Nlc3MgNzY4IHRva2VucywgcG9zaXRpb25zIFswLCA3NjddIGFyZSBsaW5lYXJseSBzY2FsZWQgdG8gWzAsIDUxMV06IHBvc19pZF9uZXcgPSBwb3NfaWQgw5cgKDUxMi83NjgpLiBBZnRlciByZXNjYWxpbmcsIGZyYWN0aW9uYWwgcG9zaXRpb24gSURzIGFyZSByb3VuZGVkIHRvIHRoZSBuZWFyZXN0IGludGVnZXIsIGdpdmluZyBhIG1hcHBpbmcgaW50byB0aGUgdHJhaW5lZCB2b2NhYnVsYXJ5IG9mIHBvc2l0aW9ucy4gVGhlIG1vZGVsIGlzIHRoZW4gZmluZS10dW5lZCBmb3IgYSBzbWFsbCBudW1iZXIgb2Ygc3RlcHMgb24gbG9uZ2VyIHNlcXVlbmNlcyB1c2luZyB0aGUgaW50ZXJwb2xhdGVkIElEcy4gVGhpcyBhcHByb2FjaCBpcyBmYXIgY2hlYXBlciB0aGFuIHJldHJhaW5pbmcgZnJvbSBzY3JhdGNoIGFuZCByZWNvdmVycyBtb3N0IG9mIHRoZSBvcmlnaW5hbCBwZXJmb3JtYW5jZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGludGVycG9sYXRlX3Bvc2l0aW9ucyhzZXFfbGVuLCB0cmFpbmluZ19sZW4pOlxuICAgICMgU2NhbGUgcG9zaXRpb24gSURzIHRvIGZpdCB3aXRoaW4gWzAsIHRyYWluaW5nX2xlbilcbiAgICBwb3NpdGlvbnMgPSB0b3JjaC5hcmFuZ2Uoc2VxX2xlbiwgZHR5cGU9dG9yY2guZmxvYXQzMilcbiAgICBzY2FsZSA9IHRyYWluaW5nX2xlbiAvIHNlcV9sZW5cbiAgICByZXR1cm4gKHBvc2l0aW9ucyAqIHNjYWxlKS5jbGFtcCgwLCB0cmFpbmluZ19sZW4gLSAxKS5sb25nKClcblxuY2xhc3MgTGVhcm5lZFBFSW50ZXJwb2xhdGlvbihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBtYXhfc2VxX2xlbiwgZF9tb2RlbCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBvc19lbWIgICAgID0gbm4uRW1iZWRkaW5nKG1heF9zZXFfbGVuLCBkX21vZGVsKVxuICAgICAgICBzZWxmLm1heF9zZXFfbGVuID0gbWF4X3NlcV9sZW5cblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIHVzZV9pbnRlcnBvbGF0aW9uPUZhbHNlKTpcbiAgICAgICAgc2VxX2xlbiA9IHguc2hhcGVbMV1cbiAgICAgICAgaWYgdXNlX2ludGVycG9sYXRpb24gYW5kIHNlcV9sZW4gXHUwMDNlIHNlbGYubWF4X3NlcV9sZW46XG4gICAgICAgICAgICBwb3NfaWRzID0gaW50ZXJwb2xhdGVfcG9zaXRpb25zKHNlcV9sZW4sIHNlbGYubWF4X3NlcV9sZW4pXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICBwb3NfaWRzID0gdG9yY2guYXJhbmdlKHNlcV9sZW4sIGRldmljZT14LmRldmljZSlcbiAgICAgICAgcmV0dXJuIHggKyBzZWxmLnBvc19lbWIocG9zX2lkcylcblxubW9kZWwgPSBMZWFybmVkUEVJbnRlcnBvbGF0aW9uKG1heF9zZXFfbGVuPTUxMiwgZF9tb2RlbD02NClcbnhfbm9ybWFsID0gdG9yY2gucmFuZG4oMSwgMjU2LCA2NClcbnhfbG9uZyAgID0gdG9yY2gucmFuZG4oMSwgNzY4LCA2NClcbm91dF9ub3JtYWwgPSBtb2RlbCh4X25vcm1hbClcbm91dF9sb25nICAgPSBtb2RlbCh4X2xvbmcsIHVzZV9pbnRlcnBvbGF0aW9uPVRydWUpXG5wcmludChcdTAwMjdOb3JtYWwgc2VxICgyNTYpOlx1MDAyNywgb3V0X25vcm1hbC5zaGFwZSlcbnByaW50KFx1MDAyN0xvbmcgc2VxICg3NjgpIHdpdGggaW50ZXJwb2xhdGlvbjpcdTAwMjcsIG91dF9sb25nLnNoYXBlKVxucHJpbnQoXHUwMDI3UG9zaXRpb25zIDAtNzY3IGFyZSBtYXBwZWQgaW50byBbMCwgNTEyKSB2aWEgbGluZWFyIHJlc2NhbGluZy5cdTAwMjcpXG5wcmludChcdTAwMjdGaW5lLXR1bmluZyBvbiBsb25nZXIgc2VxdWVuY2VzIGFmdGVyIGludGVycG9sYXRpb24gaW1wcm92ZXMgcXVhbGl0eS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGVhcm5lZCB2cyBTaW51c29pZGFsIOKAlCBFbXBpcmljYWwgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gcHJhY3RpY2UsIGxlYXJuZWQgYW5kIHNpbnVzb2lkYWwgcG9zaXRpb25hbCBlbWJlZGRpbmdzIHBlcmZvcm0gc2ltaWxhcmx5IG9uIHN0YW5kYXJkIE5MUCBiZW5jaG1hcmtzLiBUaGUgb3JpZ2luYWwgQkVSVCBwYXBlciAoRGV2bGluIGV0IGFsLiAyMDE4KSBmb3VuZCBubyBzaWduaWZpY2FudCBkaWZmZXJlbmNlIGJldHdlZW4gdGhlIHR3byBvbiBHTFVFIHRhc2tzLiBHUFQtMiB1c2VkIGxlYXJuZWQgZW1iZWRkaW5ncyB3aXRob3V0IGFibGF0aW5nIHNpbnVzb2lkYWwuIEtleSBzdHJ1Y3R1cmFsIGRpZmZlcmVuY2VzOiBzaW51c29pZGFsIGVtYmVkZGluZ3MgZW5jb2RlIG9yZGVyIGJ5IG1hdGhlbWF0aWNhbCBjb25zdHJ1Y3Rpb24g4oCUIG5lYXJieSBwb3NpdGlvbnMgaGF2ZSBzaW1pbGFyIHZlY3RvcnMgYW5kIHRoZSBwYXR0ZXJuIGlzIGRldGVybWluaXN0aWMg4oCUIHdoaWxlIGxlYXJuZWQgZW1iZWRkaW5ncyBzdGFydCByYW5kb20gYW5kIG11c3QgYWNxdWlyZSB0aGlzIHN0cnVjdHVyZSBkdXJpbmcgdHJhaW5pbmcuIE9yZGVyIHNlbnNpdGl2aXR5IG1lYXN1cmVzIGhvdyB3ZWxsIGEgUEUgc2NoZW1lIGRpc3Rpbmd1aXNoZXMgYWRqYWNlbnQgcG9zaXRpb25zOyBzaW51c29pZGFsIGFjaGlldmVzIHRoaXMgYnkgZGVzaWduIHdoaWxlIGxlYXJuZWQgZW1iZWRkaW5ncyBkZXBlbmQgb24gdHJhaW5pbmcgc2lnbmFsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG1hdGhcblxuZGVmIHNpbnVzb2lkYWxfcGUoc2VxX2xlbiwgZF9tb2RlbCk6XG4gICAgcGUgID0gdG9yY2guemVyb3Moc2VxX2xlbiwgZF9tb2RlbClcbiAgICBwb3MgPSB0b3JjaC5hcmFuZ2Uoc2VxX2xlbikudW5zcXVlZXplKDEpLmZsb2F0KClcbiAgICBkaXYgPSB0b3JjaC5leHAodG9yY2guYXJhbmdlKDAsIGRfbW9kZWwsIDIpLmZsb2F0KCkgKiAoLW1hdGgubG9nKDEwMDAwLjApIC8gZF9tb2RlbCkpXG4gICAgcGVbOiwgMDo6Ml0gPSB0b3JjaC5zaW4ocG9zICogZGl2KVxuICAgIHBlWzosIDE6OjJdID0gdG9yY2guY29zKHBvcyAqIGRpdilcbiAgICByZXR1cm4gcGVcblxuZGVmIG9yZGVyX3NlbnNpdGl2aXR5KHBlX21hdHJpeCk6XG4gICAgIyBNZWFuIGNvc2luZSBkaXN0YW5jZSBiZXR3ZWVuIGNvbnNlY3V0aXZlIHBvc2l0aW9uIGVtYmVkZGluZ3NcbiAgICBwZSA9IHBlX21hdHJpeCAvIChwZV9tYXRyaXgubm9ybShkaW09LTEsIGtlZXBkaW09VHJ1ZSkgKyAxZS04KVxuICAgIHJldHVybiAoMSAtIChwZVs6LTFdICogcGVbMTpdKS5zdW0oZGltPS0xKSkubWVhbigpLml0ZW0oKVxuXG5zZXFfbGVuLCBkX21vZGVsID0gNjQsIDEyOFxuc2luX3BlICAgID0gc2ludXNvaWRhbF9wZShzZXFfbGVuLCBkX21vZGVsKVxuc2luX3Njb3JlID0gb3JkZXJfc2Vuc2l0aXZpdHkoc2luX3BlKVxubGVhcm5lZCAgID0gbm4uRW1iZWRkaW5nKHNlcV9sZW4sIGRfbW9kZWwpXG5ubi5pbml0Lm5vcm1hbF8obGVhcm5lZC53ZWlnaHQsIHN0ZD0wLjAyKVxubGVhcm5lZF9wZSAgICA9IGxlYXJuZWQud2VpZ2h0LmRldGFjaCgpXG5sZWFybmVkX3Njb3JlID0gb3JkZXJfc2Vuc2l0aXZpdHkobGVhcm5lZF9wZSlcbnByaW50KFx1MDAyN1NpbnVzb2lkYWwgIG9yZGVyLXNlbnNpdGl2aXR5Olx1MDAyNywgcm91bmQoc2luX3Njb3JlLCA0KSlcbnByaW50KFx1MDAyN0xlYXJuZWQgKHJhbmRvbSBpbml0KTpcdTAwMjcsIHJvdW5kKGxlYXJuZWRfc2NvcmUsIDQpKVxucHJpbnQoXHUwMDI3U2ludXNvaWRhbCBlbmNvZGVzIG9yZGVyIGJ5IGRlc2lnbjsgbGVhcm5lZCBtdXN0IHRyYWluIHRvIGFjaGlldmUgaXQuXHUwMDI3KVxubm9ybV9zaW4gPSBzaW5fcGUgLyBzaW5fcGUubm9ybShkaW09LTEsIGtlZXBkaW09VHJ1ZSlcbmZvciBkIGluIFsxLCA0LCAxNiwgMzJdOlxuICAgIGNvc19zaW0gPSAobm9ybV9zaW5bMF0gKiBub3JtX3NpbltkXSkuc3VtKCkuaXRlbSgpXG4gICAgcHJpbnQoXHUwMDI3Y29zKHBvczAsIHBvc1x1MDAyNyArIHN0cihkKSArIFx1MDAyNyk9XHUwMDI3ICsgc3RyKHJvdW5kKGNvc19zaW0sIDQpKSlcbnByaW50KFx1MDAyN1NpbWlsYXJpdHkgZGVjYXlzIHdpdGggZGlzdGFuY2UgaW4gc2ludXNvaWRhbCBQRSAtXHUwMDNlIGVuY29kZXMgb3JkZXIuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoZW4gdG8gVXNlIFJvUEUgYW5kIEFMaUJpIEluc3RlYWQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhcHBsaWNhdGlvbnMgcmVxdWlyaW5nIHNlcXVlbmNlcyBzaWduaWZpY2FudGx5IGxvbmdlciB0aGFuIHRoZSB0cmFpbmluZyBsZW5ndGgsIG9yIHdoZXJlIHRoZSBtb2RlbCBtdXN0IGhhbmRsZSB2YXJpYWJsZS1sZW5ndGggaW5wdXRzIGVmZmljaWVudGx5LCBSb1BFIChSb3RhcnkgUG9zaXRpb24gRW1iZWRkaW5ncykgYW5kIEFMaUJpIChBdHRlbnRpb24gd2l0aCBMaW5lYXIgQmlhc2VzKSBvdXRwZXJmb3JtIGJvdGggbGVhcm5lZCBhbmQgc2ludXNvaWRhbCBQRS4gUm9QRSBlbmNvZGVzIHJlbGF0aXZlIHBvc2l0aW9uIGRpcmVjdGx5IGluIHRoZSBhdHRlbnRpb24gc2NvcmUgdmlhIHJvdGF0aW9uLCBpcyBwYXJhbWV0ZXItZnJlZSwgYW5kIHN1cHBvcnRzIGxlbmd0aCBleHRlbnNpb24gdmlhIFlhUk4uIEFMaUJpIGFkZHMgYSBwZXItaGVhZCBsaW5lYXIgYmlhcyBwcm9wb3J0aW9uYWwgdG8gdG9rZW4gZGlzdGFuY2UsIGFsc28gcGFyYW1ldGVyLWZyZWUgYW5kIHN0cm9uZyBvbiBsZW5ndGggZ2VuZXJhbGlzYXRpb24uIE1vZGVybiBMTE1zIChMTGFNQSAxLzIvMywgTWlzdHJhbCwgRmFsY29uLCBRd2VuKSBoYXZlIGFsbW9zdCB1bml2ZXJzYWxseSBhZG9wdGVkIFJvUEUgb3ZlciBsZWFybmVkIG9yIHNpbnVzb2lkYWwgZW1iZWRkaW5ncy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVzZSBsZWFybmVkIFBFIHdoZW46IG1heCBzZXF1ZW5jZSBsZW5ndGggaXMgZml4ZWQgYW5kIHdlbGwgd2l0aGluIHRyYWluaW5nIGJ1ZGdldCAoQkVSVCwgR1BULTIgc3R5bGUgY2xhc3NpZmljYXRpb24vZ2VuZXJhdGlvbikiLCJVc2Ugc2ludXNvaWRhbCBQRSB3aGVuOiBubyBleHRyYSBwYXJhbWV0ZXJzIGFyZSBhY2NlcHRhYmxlIGFuZCBtaWxkIGV4dHJhcG9sYXRpb24gaXMgbmVlZGVkIiwiVXNlIFJvUEUgd2hlbjogdHJhaW5pbmcgbGFyZ2UgYXV0b3JlZ3Jlc3NpdmUgTExNcyDigJQgZW5jb2RlcyByZWxhdGl2ZSBkaXN0YW5jZSwgbm8gcGFyYW1zLCBZYVJOIGV4dGVuZHMgY29udGV4dCIsIlVzZSBBTGlCaSB3aGVuOiBzdHJvbmcgb3V0LW9mLWRpc3RyaWJ1dGlvbiBsZW5ndGggZ2VuZXJhbGlzYXRpb24gaXMgcmVxdWlyZWQgd2l0aCBtaW5pbWFsIGltcGxlbWVudGF0aW9uIGNvc3QiLCJBdm9pZCBsZWFybmVkIFBFIGZvcjogbG9uZy1jb250ZXh0IHRhc2tzIChjb2RlLCBsZWdhbCwgc2NpZW50aWZpYykgd2hlcmUgc2VxdWVuY2VzIHJlZ3VsYXJseSBleGNlZWQgdHJhaW5pbmcgbGVuZ3RoIl19LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJQYXJhbXMiLCJFeHRyYXBvbGF0aW9uIiwiUmVsYXRpdmUgSW5mbyBpbiBTY29yZSIsIkN1cnJlbnQgTExNIFVzZSJdLCJyb3dzIjpbWyJTaW51c29pZGFsIFBFIiwiMCIsIldlYWsgKHBlcmlvZGljIGZvcm11bGEpIiwiTm8iLCJSYXJlIOKAlCBvcmlnaW5hbCBUcmFuc2Zvcm1lciBvbmx5Il0sWyJMZWFybmVkIFBFIiwibWF4X2xlbiDDlyBkX21vZGVsIiwiTm9uZSDigJQgSW5kZXhFcnJvciIsIk5vIiwiQkVSVCAoNTEyw5c3Njg9MzkzSyksIEdQVC0yICgxMDI0w5c3NjgpIl0sWyJSb1BFIiwiMCIsIkdvb2QgdmlhIFlhUk4vTGluZWFyIiwiWWVzIOKAlCByb3RhdGlvbiIsIkxMYU1BIDEvMi8zLCBNaXN0cmFsLCBGYWxjb24sIFF3ZW4iXSxbIkFMaUJpIiwiaCBwZXItaGVhZCBzbG9wZXMiLCJTdHJvbmciLCJZZXMg4oCUIGFkZGl0aXZlIGJpYXMiLCJNUFQsIEJMT09NLCBzb21lIFJXS1YgdmFyaWFudHMiXSxbIk5vUEUgKG5vIFBFKSIsIjAiLCJJbXBsaWNpdCB2aWEgY2F1c2FsIG1hc2siLCJJbXBsaWNpdCBvbmx5IiwiRXhwZXJpbWVudGFsIC8gc3BhcnNlIGF0dGVudGlvbiBtb2RlbHMiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRhYmxlIGFib3ZlIHN1bW1hcmlzZXMgdGhlIGZpdmUgbWFpbiBwb3NpdGlvbmFsIGVuY29kaW5nIHN0cmF0ZWdpZXMuIExlYXJuZWQgUEUgcmVtYWlucyBhIHNvbGlkIGJhc2VsaW5lIGZvciBzaG9ydC1jb250ZXh0IG1vZGVscyBidXQgaXMgcmFyZWx5IGNob3NlbiBmb3IgbmV3IGFyY2hpdGVjdHVyZXMgZHVlIHRvIGl0cyBoYXJkIGV4dHJhcG9sYXRpb24gY2VpbGluZy4gUm9QRSBoYXMgZW1lcmdlZCBhcyB0aGUgZG9taW5hbnQgY2hvaWNlIGZvciBkZWNvZGVyLW9ubHkgTExNcyBwcmVjaXNlbHkgYmVjYXVzZSBpdCBlbmNvZGVzIHJlbGF0aXZlIHBvc2l0aW9uIGluIHRoZSBhdHRlbnRpb24gc2NvcmUgd2l0aCB6ZXJvIGFkZGl0aW9uYWwgcGFyYW1ldGVycyBhbmQgc3VwcG9ydHMgY29udGV4dCBleHRlbnNpb24gdmlhIGZyZXF1ZW5jeSBzY2FsaW5nLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Learned Positional Embeddings — BERT and GPT Style

Transformers have no built-in notion of order — a set of token embeddings passed through self-attention is permutation-equivariant without additional structure. Positional information must be injected explicitly. BERT and GPT-family models do this with learned positional embeddings: an nn.Embedding(max_seq_len, d_model) lookup table trained end-to-end alongside the rest of the model. Each position index 0, 1, …, max_seq_len−1 maps to a dedicated d-dimensional vector that is added (not concatenated) to the corresponding token embedding before the first Transformer layer.

## Why Transformers Need Positional Information

Self-attention computes a weighted sum of value vectors using query-key dot products. If you permute the input sequence, every pairwise dot product changes, but the same set of outputs is produced — just reordered. This means the model cannot distinguish 'the cat sat' from 'sat cat the' without an external position signal. Sinusoidal and learned embeddings both solve this by making each position's embedding unique, so after addition the attention scores carry position-sensitive information. The choice between sinusoidal (fixed mathematical formula) and learned (trainable parameters) affects parameter count, extrapolation, and performance.

## Learned Positional Embeddings — Architecture and Design

The implementation is a single nn.Embedding module. During a forward pass, the integer sequence [0, 1, …, L−1] is looked up to produce a (L, d_model) matrix that is added element-wise to the token embedding matrix of the same shape. BERT-base uses max_seq_len=512 and d_model=768, giving 512 × 768 = 393,216 parameters in the position table. GPT-2 small uses max_seq_len=1024 with d_model=768, giving 786,432 parameters. These parameters are small relative to total model size (BERT-base has ~110M total parameters) but important for quality. Standard initialisation uses N(0, 0.02) or N(0, 1/√d_model).

```python
import torch
import torch.nn as nn

class LearnedPositionalEmbedding(nn.Module):
    def __init__(self, max_seq_len, d_model, dropout=0.1):
        super().__init__()
        self.pos_embedding = nn.Embedding(max_seq_len, d_model)
        self.dropout = nn.Dropout(dropout)
        self._init_weights()

    def _init_weights(self):
        nn.init.normal_(self.pos_embedding.weight, mean=0.0, std=0.02)

    def forward(self, token_embeddings):
        # token_embeddings: (batch, seq_len, d_model)
        batch, seq_len, d_model = token_embeddings.shape
        positions = torch.arange(seq_len, device=token_embeddings.device)
        pos_emb = self.pos_embedding(positions)         # (seq_len, d_model)
        return self.dropout(token_embeddings + pos_emb) # broadcasts over batch

model = LearnedPositionalEmbedding(max_seq_len=512, d_model=768)
x = torch.randn(2, 10, 768)
out = model(x)
print('Input:', x.shape, '-> Output:', out.shape)
param_count = sum(p.numel() for p in model.parameters())
print('Parameters:', param_count, '== 512 x 768 =', 512*768, 'for BERT-base')
print('Embedding weight shape:', model.pos_embedding.weight.shape)
```

## Parameter Count and Memory Footprint

Parameter count scales linearly with both max_seq_len and d_model: params = max_seq_len × d_model. For BERT-large (max_seq_len=512, d_model=1024) this is 524,288 — still less than 0.5% of the 340M total parameters. Memory cost at inference: the full embedding table is always loaded into GPU memory regardless of the actual sequence length, which matters for batch inference. The table fits in ~3 MB for BERT-base (393K × 4 bytes float32), negligible compared to attention and FFN weights. During training, gradients accumulate only for the position rows that appear in the current batch, making the effective gradient update sparse.

> **Addition vs Concatenation**: Learned positional embeddings are always added to token embeddings, never concatenated. Addition preserves d_model dimension (no parameter increase in subsequent layers) and allows the model to learn any linear combination of token and position information in the first attention projection. Concatenation would require halving both token and position dimensions or increasing all downstream weight matrices — neither is standard practice.

## Extrapolation Failure Beyond Training Length

The central weakness of learned positional embeddings is hard extrapolation failure: position index L is simply not in the embedding table if L ≥ max_seq_len. Attempting a forward pass with a sequence longer than the training maximum raises an IndexError or returns garbage (if indices are clamped). Even without an error, empirical results show perplexity spiking sharply at lengths beyond the training maximum — the model never encountered those position vectors during training, so they are meaningless to the attention heads. This is in contrast to sinusoidal PE, which is defined by a closed-form formula at any position.

```python
import torch
import torch.nn as nn

class TinyTransformerLM(nn.Module):
    def __init__(self, vocab_size, d_model, max_seq_len):
        super().__init__()
        self.token_emb  = nn.Embedding(vocab_size, d_model)
        self.pos_emb    = nn.Embedding(max_seq_len, d_model)
        layer = nn.TransformerEncoderLayer(d_model, nhead=4, batch_first=True, dim_feedforward=128)
        self.encoder    = nn.TransformerEncoder(layer, num_layers=2)
        self.head       = nn.Linear(d_model, vocab_size)
        self.max_seq_len = max_seq_len

    def forward(self, x):
        seq_len = x.shape[1]
        pos = torch.arange(seq_len, device=x.device)
        emb = self.token_emb(x) + self.pos_emb(pos)
        return self.head(self.encoder(emb))

torch.manual_seed(42)
model = TinyTransformerLM(vocab_size=100, d_model=64, max_seq_len=32)
model.eval()
criterion = nn.CrossEntropyLoss()
for seq_len in [16, 32, 40, 48]:
    try:
        x = torch.randint(0, 100, (1, seq_len))
        logits = model(x)
        loss   = criterion(logits.view(-1, 100), x.view(-1))
        print('seq_len=' + str(seq_len) + '  loss=' + str(round(loss.item(), 3)))
    except Exception as e:
        print('seq_len=' + str(seq_len) + '  ERROR: ' + type(e).__name__)
```

## Position Interpolation for Length Extension

Position interpolation (Press et al. 2022; Chen et al. 2023 for RoPE) adapts learned embeddings to longer sequences by rescaling position IDs so that new positions map into the trained range. For a model trained with max_seq_len=512 that needs to process 768 tokens, positions [0, 767] are linearly scaled to [0, 511]: pos_id_new = pos_id × (512/768). After rescaling, fractional position IDs are rounded to the nearest integer, giving a mapping into the trained vocabulary of positions. The model is then fine-tuned for a small number of steps on longer sequences using the interpolated IDs. This approach is far cheaper than retraining from scratch and recovers most of the original performance.

```python
import torch
import torch.nn as nn

def interpolate_positions(seq_len, training_len):
    # Scale position IDs to fit within [0, training_len)
    positions = torch.arange(seq_len, dtype=torch.float32)
    scale = training_len / seq_len
    return (positions * scale).clamp(0, training_len - 1).long()

class LearnedPEInterpolation(nn.Module):
    def __init__(self, max_seq_len, d_model):
        super().__init__()
        self.pos_emb     = nn.Embedding(max_seq_len, d_model)
        self.max_seq_len = max_seq_len

    def forward(self, x, use_interpolation=False):
        seq_len = x.shape[1]
        if use_interpolation and seq_len > self.max_seq_len:
            pos_ids = interpolate_positions(seq_len, self.max_seq_len)
        else:
            pos_ids = torch.arange(seq_len, device=x.device)
        return x + self.pos_emb(pos_ids)

model = LearnedPEInterpolation(max_seq_len=512, d_model=64)
x_normal = torch.randn(1, 256, 64)
x_long   = torch.randn(1, 768, 64)
out_normal = model(x_normal)
out_long   = model(x_long, use_interpolation=True)
print('Normal seq (256):', out_normal.shape)
print('Long seq (768) with interpolation:', out_long.shape)
print('Positions 0-767 are mapped into [0, 512) via linear rescaling.')
print('Fine-tuning on longer sequences after interpolation improves quality.')
```

## Learned vs Sinusoidal — Empirical Comparison

In practice, learned and sinusoidal positional embeddings perform similarly on standard NLP benchmarks. The original BERT paper (Devlin et al. 2018) found no significant difference between the two on GLUE tasks. GPT-2 used learned embeddings without ablating sinusoidal. Key structural differences: sinusoidal embeddings encode order by mathematical construction — nearby positions have similar vectors and the pattern is deterministic — while learned embeddings start random and must acquire this structure during training. Order sensitivity measures how well a PE scheme distinguishes adjacent positions; sinusoidal achieves this by design while learned embeddings depend on training signal.

```python
import torch
import torch.nn as nn
import math

def sinusoidal_pe(seq_len, d_model):
    pe  = torch.zeros(seq_len, d_model)
    pos = torch.arange(seq_len).unsqueeze(1).float()
    div = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(pos * div)
    pe[:, 1::2] = torch.cos(pos * div)
    return pe

def order_sensitivity(pe_matrix):
    # Mean cosine distance between consecutive position embeddings
    pe = pe_matrix / (pe_matrix.norm(dim=-1, keepdim=True) + 1e-8)
    return (1 - (pe[:-1] * pe[1:]).sum(dim=-1)).mean().item()

seq_len, d_model = 64, 128
sin_pe    = sinusoidal_pe(seq_len, d_model)
sin_score = order_sensitivity(sin_pe)
learned   = nn.Embedding(seq_len, d_model)
nn.init.normal_(learned.weight, std=0.02)
learned_pe    = learned.weight.detach()
learned_score = order_sensitivity(learned_pe)
print('Sinusoidal  order-sensitivity:', round(sin_score, 4))
print('Learned (random init):', round(learned_score, 4))
print('Sinusoidal encodes order by design; learned must train to achieve it.')
norm_sin = sin_pe / sin_pe.norm(dim=-1, keepdim=True)
for d in [1, 4, 16, 32]:
    cos_sim = (norm_sin[0] * norm_sin[d]).sum().item()
    print('cos(pos0, pos' + str(d) + ')=' + str(round(cos_sim, 4)))
print('Similarity decays with distance in sinusoidal PE -> encodes order.')
```

## When to Use RoPE and ALiBi Instead

For applications requiring sequences significantly longer than the training length, or where the model must handle variable-length inputs efficiently, RoPE (Rotary Position Embeddings) and ALiBi (Attention with Linear Biases) outperform both learned and sinusoidal PE. RoPE encodes relative position directly in the attention score via rotation, is parameter-free, and supports length extension via YaRN. ALiBi adds a per-head linear bias proportional to token distance, also parameter-free and strong on length generalisation. Modern LLMs (LLaMA 1/2/3, Mistral, Falcon, Qwen) have almost universally adopted RoPE over learned or sinusoidal embeddings.

- Use learned PE when: max sequence length is fixed and well within training budget (BERT, GPT-2 style classification/generation)
- Use sinusoidal PE when: no extra parameters are acceptable and mild extrapolation is needed
- Use RoPE when: training large autoregressive LLMs — encodes relative distance, no params, YaRN extends context
- Use ALiBi when: strong out-of-distribution length generalisation is required with minimal implementation cost
- Avoid learned PE for: long-context tasks (code, legal, scientific) where sequences regularly exceed training length

| Method | Params | Extrapolation | Relative Info in Score | Current LLM Use |
| --- | --- | --- | --- | --- |
| Sinusoidal PE | 0 | Weak (periodic formula) | No | Rare — original Transformer only |
| Learned PE | max_len × d_model | None — IndexError | No | BERT (512×768=393K), GPT-2 (1024×768) |
| RoPE | 0 | Good via YaRN/Linear | Yes — rotation | LLaMA 1/2/3, Mistral, Falcon, Qwen |
| ALiBi | h per-head slopes | Strong | Yes — additive bias | MPT, BLOOM, some RWKV variants |
| NoPE (no PE) | 0 | Implicit via causal mask | Implicit only | Experimental / sparse attention models |

The table above summarises the five main positional encoding strategies. Learned PE remains a solid baseline for short-context models but is rarely chosen for new architectures due to its hard extrapolation ceiling. RoPE has emerged as the dominant choice for decoder-only LLMs precisely because it encodes relative position in the attention score with zero additional parameters and supports context extension via frequency scaling.

---

