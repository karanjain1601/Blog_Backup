---
title: "RetNet — Retention Mechanism and Parallel/Recurrent Modes"
slug: "retnet-retention-mechanism"
description: "RetNet's retention mechanism with three computation modes — parallel O(L²) training, recurrent O(1) inference, and chunkwise — plus multi-scale decay for different temporal scales."
tags: ["deep-learning", "rnns", "sequence-models", "state-space-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmV0TmV0IChTdW4gZXQgYWwuLCAyMDIzKSB0YXJnZXRzIHRoZSBpbXBvc3NpYmxlIHRyaWFuZ2xlIG9mIHNlcXVlbmNlIG1vZGVsaW5nOiB0cmFpbmluZyBwYXJhbGxlbGlzbSwgbG93LWNvc3QgaW5mZXJlbmNlLCBhbmQgc3Ryb25nIHBlcmZvcm1hbmNlLiBUcmFuc2Zvcm1lcnMgb2ZmZXIgdHJhaW5pbmcgcGFyYWxsZWxpc20gYW5kIHN0cm9uZyBwZXJmb3JtYW5jZSBidXQgTyhMKSBLVi1jYWNoZSBhdCBpbmZlcmVuY2UuIFJOTnMgb2ZmZXIgTygxKSBpbmZlcmVuY2UgYnV0IGFyZSBzZXF1ZW50aWFsIGR1cmluZyB0cmFpbmluZy4gUmV0TmV0IGludHJvZHVjZXMgdGhlIHJldGVudGlvbiBtZWNoYW5pc20g4oCUIGEgbGluZWFyIHJlY3VycmVuY2Ugd2l0aCBleHBvbmVudGlhbCBkZWNheSDigJQgdGhhdCBhY2hpZXZlcyBhbGwgdGhyZWUgc2ltdWx0YW5lb3VzbHk6IHBhcmFsbGVsIG1vZGUgZm9yIGZhc3QgR1BVIHRyYWluaW5nLCByZWN1cnJlbnQgbW9kZSBmb3IgTygxKSBwZXItc3RlcCBpbmZlcmVuY2UsIGFuZCBhIGNodW5rd2lzZSBtb2RlIHRoYXQgaW50ZXJwb2xhdGVzIGJldHdlZW4gdGhlIHR3by4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgVGhyZWUgQ29tcHV0YXRpb24gTW9kZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJldE5ldFx1MDAyN3MgcmV0ZW50aW9uIG1lY2hhbmlzbSBjYW4gYmUgY29tcHV0ZWQgaW4gdGhyZWUgbWF0aGVtYXRpY2FsbHkgZXF1aXZhbGVudCB3YXlzLiBQYXJhbGxlbCBtb2RlOiBSZXQoUSxLLFYpID0gKFFL4bWAIOKKmSBEKSBWIHdoZXJlIERbbSxuXSA9IM6zXnttLW59IGlmIG0g4omlIG4gZWxzZSAwIGlzIHRoZSBjYXVzYWwgZGVjYXkgbWFzayDigJQgaWRlbnRpY2FsIHN0cnVjdHVyZSB0byBhdHRlbnRpb24gYnV0IHdpdGggbm8gc29mdG1heCBhbmQgYW4gZXhwb25lbnRpYWwgZGVjYXkgaW5zdGVhZCBvZiB1bmlmb3JtIHdlaWdodGluZy4gUmVjdXJyZW50IG1vZGU6IFPigpkgPSDOs1PigpnigovigoEgKyBr4oKZ4bWAduKCmSwgcmV04oKZID0gceKCmVPigpkg4oCUIGNvbnN0YW50IE8oZMKyKSBzdGF0ZSB1cGRhdGVkIE8oMSkgcGVyIHN0ZXAuIENodW5rd2lzZSBtb2RlOiBwcm9jZXNzIGNodW5rcyBvZiBDIHRva2VucyBpbiBwYXJhbGxlbCAodXNpbmcgbG9jYWwgZGVjYXkgbWFza3MpIHdoaWxlIG1haW50YWluaW5nIGEgcmVjdXJyZW50IHN0YXRlIGFjcm9zcyBjaHVua3MuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQYXJhbGxlbDogTyhMwrLCt2QpIOKAlCBzYW1lIEdQVSB1dGlsaXphdGlvbiBhcyBhdHRlbnRpb24sIGlkZWFsIGZvciB0cmFpbmluZyIsIlJlY3VycmVudDogTyhkwrIpIHN0YXRlLCBPKGTCsikgcGVyIHN0ZXAg4oCUIGNvbnN0YW50IG1lbW9yeSwgaWRlYWwgZm9yIGluZmVyZW5jZSIsIkNodW5rd2lzZTogTyhDwrLCt2QgKyBML0PCt2TCsikg4oCUIGJhbGFuY2VkIHRyYWluaW5nIGFuZCBwcmVmaWxsIHNwZWVkIiwizrMg4oiIICgwLDEpOiBkZWNheSBmYWN0b3IgcGVyIGhlYWQg4oCUIGNvbnRyb2xzIGhvdyBxdWlja2x5IG9sZCBpbmZvcm1hdGlvbiBpcyBmb3Jnb3R0ZW4iLCJObyBzb2Z0bWF4OiByZXRlbnRpb24gaXMgbGluZWFyIOKAlCByZW1vdmVzIG51bWVyaWNhbCBpbnN0YWJpbGl0eSBhbmQgZW5hYmxlcyByZWN1cnJlbnQgZm9ybSJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXJhbGxlbCBNb2RlIOKAlCBPKEzCsikgVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBwYXJhbGxlbCByZXRlbnRpb24gZm9ybXVsYSBSZXQgPSAoUUvhtYAg4oqZIEQpViBjbG9zZWx5IG1pcnJvcnMgc2NhbGVkIGRvdC1wcm9kdWN0IGF0dGVudGlvbjogUSwgSywgViBhcmUgbGluZWFyIHByb2plY3Rpb25zIG9mIHRoZSBpbnB1dCwgYW5kIHRoZSBvdXRwdXQgaXMgYSB3ZWlnaHRlZCBzdW0gb2YgdmFsdWVzLiBUaGUgZGlmZmVyZW5jZSBpcyBpbiB0aGUgd2VpZ2h0aW5nOiBhdHRlbnRpb24gdXNlcyBzb2Z0bWF4KFFL4bWAIC8g4oiaZCkgZm9yIHBvc2l0aW9uLWF3YXJlIHNvZnQgc2VsZWN0aW9uLCB3aGlsZSByZXRlbnRpb24gdXNlcyB0aGUgZml4ZWQgY2F1c2FsIGRlY2F5IG1hc2sgRFttLG5dID0gzrNee20tbn0gd2hpY2ggZXhwb25lbnRpYWxseSBkb3duLXdlaWdodHMgY29udHJpYnV0aW9ucyBmcm9tIGRpc3RhbnQgcG9zaXRpb25zLiBUaGlzIG1lYW5zIHJldGVudGlvbiBpcyBjb250ZW50LWFnbm9zdGljIGluIGl0cyBwb3NpdGlvbmFsIHdlaWdodGluZyDigJQgaXQgY2Fubm90IGF0dGVuZCBzZWxlY3RpdmVseSBsaWtlIE1hbWJhIOKAlCBidXQgaXQgYWRtaXRzIHRoZSByZWN1cnJlbnQgZm9ybSB0aGF0IGF0dGVudGlvbiBkb2VzIG5vdC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGJ1aWxkX2RlY2F5X21hc2soTCwgZ2FtbWEsIGRldmljZT1cdTAwMjdjcHVcdTAwMjcpOlxuICAgIFwiXCJcIkRbbSxuXSA9IGdhbW1hXihtLW4pIGlmIG1cdTAwM2U9biBlbHNlIDAg4oCUIGNhdXNhbCBleHBvbmVudGlhbCBkZWNheSBtYXNrLlwiXCJcIlxuICAgIGlkeCA9IHRvcmNoLmFyYW5nZShMLCBkZXZpY2U9ZGV2aWNlKS5mbG9hdCgpXG4gICAgRCAgID0gZ2FtbWEgKiogKGlkeC51bnNxdWVlemUoMCkgLSBpZHgudW5zcXVlZXplKDEpKSAgICMgKEwsIEwpXG4gICAgcmV0dXJuIHRvcmNoLnRyaWwoRCkgICAgIyBjYXVzYWw6IHplcm8gb3V0IGZ1dHVyZSBwb3NpdGlvbnNcblxuY2xhc3MgUGFyYWxsZWxSZXRlbnRpb24obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgaGVhZHM9NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmhlYWRzICA9IGhlYWRzXG4gICAgICAgIHNlbGYuZF9oZWFkID0gZF9tb2RlbCAvLyBoZWFkc1xuICAgICAgICBzZWxmLlEgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5LID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuViA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLm91dCA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICAjIE11bHRpLXNjYWxlOiBkaWZmZXJlbnQgZ2FtbWEgcGVyIGhlYWRcbiAgICAgICAgZ2FtbWFzID0gMSAtIDIgKiogKC01IC0gdG9yY2guYXJhbmdlKGhlYWRzKS5mbG9hdCgpKVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdnYW1tYXNcdTAwMjcsIGdhbW1hcylcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBCLCBMLCBkID0geC5zaGFwZVxuICAgICAgICBRID0gc2VsZi5RKHgpLnZpZXcoQiwgTCwgc2VsZi5oZWFkcywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKSAgIyAoQixILEwsZGgpXG4gICAgICAgIEsgPSBzZWxmLksoeCkudmlldyhCLCBMLCBzZWxmLmhlYWRzLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIFYgPSBzZWxmLlYoeCkudmlldyhCLCBMLCBzZWxmLmhlYWRzLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIG91dCA9IHRvcmNoLnplcm9zX2xpa2UoUSlcbiAgICAgICAgZm9yIGggaW4gcmFuZ2Uoc2VsZi5oZWFkcyk6XG4gICAgICAgICAgICBEICAgPSBidWlsZF9kZWNheV9tYXNrKEwsIHNlbGYuZ2FtbWFzW2hdLml0ZW0oKSwgeC5kZXZpY2UpICAgICAjIChMLCBMKVxuICAgICAgICAgICAgcmV0ID0gKFFbOiwgaF0gQCBLWzosIGhdLnRyYW5zcG9zZSgtMSwgLTIpKSAqIEQudW5zcXVlZXplKDApICAjIChCLEwsTClcbiAgICAgICAgICAgIG91dFs6LCBoXSA9IHJldCBAIFZbOiwgaF1cbiAgICAgICAgcmV0dXJuIHNlbGYub3V0KG91dC50cmFuc3Bvc2UoMSwgMikucmVzaGFwZShCLCBMLCBkKSlcblxubW9kZWwgPSBQYXJhbGxlbFJldGVudGlvbihkX21vZGVsPTEyOCwgaGVhZHM9NClcbnggPSB0b3JjaC5yYW5kbigyLCAxNiwgMTI4KVxucHJpbnQoZlwiUGFyYWxsZWwgcmV0ZW50aW9uIG91dHB1dDoge21vZGVsKHgpLnNoYXBlfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlY3VycmVudCBNb2RlIOKAlCBPKDEpIEluZmVyZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlY3VycmVudCBmb3JtIG9mIHJldGVudGlvbiBwcm9jZXNzZXMgb25lIHRva2VuIGF0IGEgdGltZTogYXQgc3RlcCBuLCB0aGUgc3RhdGUgU+KCmSA9IM6zU+KCmeKCi+KCgSArIGvigpnhtYB24oKZIGlzIGEgZCDDlyBkIG1hdHJpeCBhY2N1bXVsYXRpbmcgd2VpZ2h0ZWQgb3V0ZXIgcHJvZHVjdHMgb2Yga2V5cyBhbmQgdmFsdWVzLiBUaGUgb3V0cHV0IGlzIHJldOKCmSA9IHHigplT4oKZIOKAlCBhIHNpbXBsZSBtYXRyaXgtdmVjdG9yIHByb2R1Y3QuIE5vIEtWIGNhY2hlIGlzIG5lZWRlZDogdGhlIGVudGlyZSBzZXF1ZW5jZSBoaXN0b3J5IGlzIGNvbXByZXNzZWQgaW50byB0aGUgZml4ZWQtc2l6ZSBzdGF0ZSBTLiBUaGlzIGdpdmVzIE8oMSkgbWVtb3J5IG92ZXJoZWFkIGFuZCBPKGTCsikgY29tcHV0ZSBwZXIgc3RlcCwgaW5kZXBlbmRlbnQgb2Ygc2VxdWVuY2UgbGVuZ3RoIOKAlCBhIHNpZ25pZmljYW50IGFkdmFudGFnZSBvdmVyIFRyYW5zZm9ybWVyXHUwMDI3cyBPKEzCt2QpIEtWIGNhY2hlIHRoYXQgZ3Jvd3Mgd2l0aCBldmVyeSBuZXcgdG9rZW4uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFJlY3VycmVudFJldGVudGlvbihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlJldE5ldCByZWN1cnJlbnQgbW9kZTogTygxKSBwZXIgc3RlcCwgTyhkXjIpIGZpeGVkIHN0YXRlLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsLCBoZWFkcz00KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuaGVhZHMgID0gaGVhZHNcbiAgICAgICAgc2VsZi5kX2hlYWQgPSBkX21vZGVsIC8vIGhlYWRzXG4gICAgICAgIHNlbGYuUSAgPSBubi5MaW5lYXIoZF9tb2RlbCwgZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5LICA9IG5uLkxpbmVhcihkX21vZGVsLCBkX21vZGVsLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLlYgID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYub3V0ID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIGdhbW1hcyA9IDEgLSAyICoqICgtNSAtIHRvcmNoLmFyYW5nZShoZWFkcykuZmxvYXQoKSlcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3Z2FtbWFzXHUwMDI3LCBnYW1tYXMpXG5cbiAgICBkZWYgc3RlcChzZWxmLCB4X3QsIFMpOlxuICAgICAgICBcIlwiXCJQcm9jZXNzIG9uZSB0b2tlbiwgdXBkYXRlIHN0YXRlIFM6IChCLCBoZWFkcywgZF9oZWFkLCBkX2hlYWQpLlwiXCJcIlxuICAgICAgICBCICA9IHhfdC5zaGFwZVswXVxuICAgICAgICBxICA9IHNlbGYuUSh4X3QpLnZpZXcoQiwgc2VsZi5oZWFkcywgc2VsZi5kX2hlYWQpXG4gICAgICAgIGsgID0gc2VsZi5LKHhfdCkudmlldyhCLCBzZWxmLmhlYWRzLCBzZWxmLmRfaGVhZClcbiAgICAgICAgdiAgPSBzZWxmLlYoeF90KS52aWV3KEIsIHNlbGYuaGVhZHMsIHNlbGYuZF9oZWFkKVxuICAgICAgICAjIFNfbiA9IGdhbW1hICogU197bi0xfSArIGtfbl5UIHZfbiAgKG91dGVyIHByb2R1Y3QgYWNjdW11bGF0aW9uKVxuICAgICAgICBTICA9IHNlbGYuZ2FtbWFzLnZpZXcoMSwtMSwxLDEpICogUyArIHRvcmNoLmVpbnN1bShcdTAwMjdiaGQsYmhlLVx1MDAzZWJoZGVcdTAwMjcsIGssIHYpXG4gICAgICAgICMgcmV0X24gPSBxX24gU19uXG4gICAgICAgIHJldCA9IHRvcmNoLmVpbnN1bShcdTAwMjdiaGQsYmhkZS1cdTAwM2ViaGVcdTAwMjcsIHEsIFMpLnJlc2hhcGUoQiwgLTEpXG4gICAgICAgIHJldHVybiBzZWxmLm91dChyZXQpLCBTXG5cbmQsIEgsIEIgPSA2NCwgNCwgMlxubW9kZWwgPSBSZWN1cnJlbnRSZXRlbnRpb24oZCwgSClcblMgPSB0b3JjaC56ZXJvcyhCLCBILCBkLy9ILCBkLy9IKSAgICAjIGluaXRpYWwgc3RhdGVcbnByaW50KFwiQXV0b3JlZ3Jlc3NpdmUgcmVjdXJyZW50IGdlbmVyYXRpb246XCIpXG5mb3IgdCBpbiByYW5nZSg2KTpcbiAgICB4X3QgPSB0b3JjaC5yYW5kbihCLCBkKVxuICAgIG91dCwgUyA9IG1vZGVsLnN0ZXAoeF90LCBTKVxucHJpbnQoZlwiT3V0cHV0OiB7b3V0LnNoYXBlfSwgU3RhdGU6IHtTLnNoYXBlfSwgU3RhdGUgbm9ybToge1Mubm9ybSgpOi4zZn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDaHVua3dpc2UgTW9kZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNodW5rd2lzZSBtb2RlIHByb2Nlc3NlcyB0aGUgc2VxdWVuY2UgaW4gY2h1bmtzIG9mIHNpemUgQy4gV2l0aGluIGVhY2ggY2h1bmssIHBhcmFsbGVsIHJldGVudGlvbiBpcyBhcHBsaWVkIHVzaW5nIGEgbG9jYWwgZGVjYXkgbWFzayDigJQgaWRlbnRpY2FsIHRvIHBhcmFsbGVsIG1vZGUgYnV0IG9ubHkgQ8OXQyBpbnN0ZWFkIG9mIEzDl0wuIEFjcm9zcyBjaHVua3MsIHRoZSByZWN1cnJlbnQgc3RhdGUgaXMgdXBkYXRlZCB0byBjYXJyeSBpbmZvcm1hdGlvbiBmcm9tIHBhc3QgY2h1bmtzLiBUaGUgd2l0aGluLWNodW5rIHBhcmFsbGVsIGNvbXB1dGF0aW9uIGFjaGlldmVzIGhpZ2ggR1BVIHV0aWxpemF0aW9uLCB3aGlsZSB0aGUgYWNyb3NzLWNodW5rIHJlY3VycmVuY2Uga2VlcHMgbWVtb3J5IGJvdW5kZWQuIENodW5rd2lzZSBpcyB0aGUgcmVjb21tZW5kZWQgbW9kZSBmb3IgdHJhaW5pbmcgb24gbG9uZyBkb2N1bWVudHM6IGNob29zZSBDIHN1Y2ggdGhhdCBDwrIgZml0cyBjb21mb3J0YWJseSBpbiBHUFUgbWVtb3J5IHdoaWxlIEwvQyByZWN1cnJlbnQgdXBkYXRlcyBhcmUgY2hlYXAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG5kZWYgY2h1bmt3aXNlX3JldGVudGlvbihRLCBLLCBWLCBnYW1tYSwgY2h1bmtfc2l6ZT0zMik6XG4gICAgXCJcIlwiXG4gICAgQ2h1bmt3aXNlIHJldGVudGlvbjogcGFyYWxsZWwgd2l0aGluIGNodW5rLCByZWN1cnJlbnQgYWNyb3NzIGNodW5rcy5cbiAgICBRLCBLLCBWOiAoQiwgTCwgZCkg4oCUIGFsbCBzYW1lIGRpbWVuc2lvbiBmb3Igc2ltcGxpY2l0eS5cbiAgICBcIlwiXCJcbiAgICBCLCBMLCBkID0gUS5zaGFwZVxuICAgIG5fY2h1bmtzID0gKEwgKyBjaHVua19zaXplIC0gMSkgLy8gY2h1bmtfc2l6ZVxuICAgIG91dHB1dHMgID0gW11cbiAgICBTID0gdG9yY2guemVyb3MoQiwgZCwgZCwgZGV2aWNlPVEuZGV2aWNlKSAgICAgIyBjcm9zcy1jaHVuayBzdGF0ZSAoQiwgZCwgZClcblxuICAgIGZvciBjIGluIHJhbmdlKG5fY2h1bmtzKTpcbiAgICAgICAgcywgZSAgICA9IGMgKiBjaHVua19zaXplLCBtaW4oKGMrMSkgKiBjaHVua19zaXplLCBMKVxuICAgICAgICBxX2MsIGtfYywgdl9jID0gUVs6LCBzOmVdLCBLWzosIHM6ZV0sIFZbOiwgczplXVxuICAgICAgICBjcyA9IGUgLSBzXG5cbiAgICAgICAgIyBJbnRyYS1jaHVuayBwYXJhbGxlbCByZXRlbnRpb25cbiAgICAgICAgaWR4ID0gdG9yY2guYXJhbmdlKGNzLCBkZXZpY2U9US5kZXZpY2UpLmZsb2F0KClcbiAgICAgICAgRCAgID0gdG9yY2gudHJpbChnYW1tYSAqKiAoaWR4LnVuc3F1ZWV6ZSgwKSAtIGlkeC51bnNxdWVlemUoMSkpKS51bnNxdWVlemUoMClcbiAgICAgICAgaW50cmEgPSAoKHFfYyBAIGtfYy50cmFuc3Bvc2UoLTEsLTIpKSAqIEQpIEAgdl9jICAgICAgICMgKEIsIGNzLCBkKVxuXG4gICAgICAgICMgQ3Jvc3MtY2h1bms6IGNvbnRyaWJ1dGlvbiBmcm9tIGFjY3VtdWxhdGVkIHBhc3Qgc3RhdGVcbiAgICAgICAgZGVjYXkgID0gZ2FtbWEgKiogdG9yY2guYXJhbmdlKGNzLCAwLCAtMSwgZHR5cGU9dG9yY2guZmxvYXQzMiwgZGV2aWNlPVEuZGV2aWNlKVxuICAgICAgICBjcm9zcyAgPSAocV9jICogZGVjYXkudmlldygxLC0xLDEpKSBAIFMgICAgICAgICAgICAgICAgICMgKEIsIGNzLCBkKVxuXG4gICAgICAgIG91dHB1dHMuYXBwZW5kKGludHJhICsgY3Jvc3MpXG4gICAgICAgICMgVXBkYXRlIHN0YXRlOiBTX25ldyA9IGdhbW1hXmNzICogUyArIEtfY15UIFZfY1xuICAgICAgICBTID0gZ2FtbWEqKmNzICogUyArIGtfYy50cmFuc3Bvc2UoLTEsLTIpIEAgdl9jXG5cbiAgICByZXR1cm4gdG9yY2guY2F0KG91dHB1dHMsIGRpbT0xKVxuXG5CLCBMLCBkID0gMiwgNjQsIDMyXG5RID0gSyA9IFYgPSB0b3JjaC5yYW5kbihCLCBMLCBkKVxub3V0ID0gY2h1bmt3aXNlX3JldGVudGlvbihRLCBLLCBWLCBnYW1tYT0wLjksIGNodW5rX3NpemU9MTYpXG5wcmludChmXCJDaHVua3dpc2Ugb3V0cHV0OiB7b3V0LnNoYXBlfVwiKSAgICMgKDIsIDY0LCAzMikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQ2hvb3NpbmcgQ2h1bmsgU2l6ZSIsImNvbnRlbnQiOiJGb3IgdHJhaW5pbmcgb24gc2VxdWVuY2VzIG9mIGxlbmd0aCBMPTgxOTIsIGEgY2h1bmsgc2l6ZSBvZiBDPTUxMiBnaXZlcyAxNiByZWN1cnJlbnQgc3RlcHMgYWNyb3NzIGNodW5rcy4gV2l0aGluIGVhY2ggY2h1bmsgdGhlIEPDl0M9MjYySyBlbGVtZW50IG1hdHJpeCBpcyBzbWFsbCBlbm91Z2ggZm9yIGZhc3QgbWF0cml4IG11bHRpcGxpY2F0aW9uIG9uIG1vZGVybiBHUFVzLiBGb3IgaW5mZXJlbmNlLCBzd2l0Y2ggdG8gcmVjdXJyZW50IG1vZGUgKEM9MSkg4oCUIG5vIGNvZGUgY2hhbmdlcyBuZWVkZWQsIGp1c3QgY2FsbCB0aGUgcmVjdXJyZW50IHN0ZXAgZnVuY3Rpb24gaW5zdGVhZCBvZiB0aGUgcGFyYWxsZWwgZm9yd2FyZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDQg4oCUIFJldE5ldCB2cyBUcmFuc2Zvcm1lciBQZXJwbGV4aXR5IENvbXBhcmlzb24ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5jbGFzcyBUaW55UmV0TmV0KG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiTWluaW1hbCBSZXROZXQtbGlrZSBMTSB1c2luZyBHUlUgYXMgcmV0ZW50aW9uIHByb3h5IGZvciBiZW5jaG1hcmtpbmcuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHZvY2FiLCBkKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW1iZWQgPSBubi5FbWJlZGRpbmcodm9jYWIsIGQpXG4gICAgICAgIHNlbGYuZ3J1ICAgPSBubi5HUlUoZCwgZCwgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5oZWFkICA9IG5uLkxpbmVhcihkLCB2b2NhYilcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgaCwgXyA9IHNlbGYuZ3J1KHNlbGYuZW1iZWQoeCkpXG4gICAgICAgIHJldHVybiBzZWxmLmhlYWQoaClcblxuZGVmIHNpbV9jdXJ2ZShzdGFydCwgcmF0ZSwgZmxvb3IsIG49MjAwLCBub2lzZT0xLjIsIHNlZWQ9MCk6XG4gICAgXCJcIlwiU2ltdWxhdGUgcGVycGxleGl0eSB0cmFpbmluZyBjdXJ2ZS5cIlwiXCJcbiAgICBucC5yYW5kb20uc2VlZChzZWVkKVxuICAgIHJldHVybiBzdGFydCAqIG5wLmV4cCgtcmF0ZSAqIG5wLmFyYW5nZSgxLCBuKzEpKSArIGZsb29yICsgbnAucmFuZG9tLnJhbmRuKG4pICogbm9pc2Vcblxuc3RlcHMgID0gbnAuYXJhbmdlKDEsIDIwMSlcbmN1cnZlcyA9IHtcbiAgICBcdTAwMjdUcmFuc2Zvcm1lclx1MDAyNzogICBzaW1fY3VydmUoMjAwLCAwLjAxOCwgMTUuMCwgc2VlZD0wKSxcbiAgICBcdTAwMjdSZXROZXRcdTAwMjc6ICAgICAgICBzaW1fY3VydmUoMjAwLCAwLjAxOSwgMTQuNSwgc2VlZD0xKSxcbiAgICBcdTAwMjdNYW1iYVx1MDAyNzogICAgICAgICBzaW1fY3VydmUoMjAwLCAwLjAyMCwgMTQuMiwgc2VlZD0yKSxcbiAgICBcdTAwMjdSV0tWXHUwMDI3OiAgICAgICAgICBzaW1fY3VydmUoMjAwLCAwLjAxNywgMTUuOCwgc2VlZD0zKSxcbn1cbmNvbG9ycyA9IFtcdTAwMjdzdGVlbGJsdWVcdTAwMjcsIFx1MDAyN2ZvcmVzdGdyZWVuXHUwMDI3LCBcdTAwMjd0b21hdG9cdTAwMjcsIFx1MDAyN29yYW5nZVx1MDAyN11cblxuZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSg5LCA1KSlcbmZvciAobmFtZSwgcHBsKSwgY29sb3IgaW4gemlwKGN1cnZlcy5pdGVtcygpLCBjb2xvcnMpOlxuICAgIGF4LnBsb3Qoc3RlcHMsIHBwbCwgYWxwaGE9MC44LCBsYWJlbD1uYW1lLCBjb2xvcj1jb2xvciwgbGluZXdpZHRoPTEuNSlcbmF4LnNldF95c2NhbGUoXHUwMDI3bG9nXHUwMDI3KVxuYXguc2V0X3hsYWJlbChcdTAwMjdUcmFpbmluZyBTdGVwc1x1MDAyNyk7IGF4LnNldF95bGFiZWwoXHUwMDI3UGVycGxleGl0eSAobG9nIHNjYWxlKVx1MDAyNylcbmF4LnNldF90aXRsZShcdTAwMjdMTSBUcmFpbmluZyBDdXJ2ZXM6IFJldE5ldCB2cyBBbHRlcm5hdGl2ZXNcdTAwMjcpXG5heC5sZWdlbmQoKTsgYXguZ3JpZChUcnVlLCBhbHBoYT0wLjMpXG5wbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zYXZlZmlnKFx1MDAyN3JldG5ldF9wcGwucG5nXHUwMDI3LCBkcGk9MTIwKTsgcGx0LnNob3coKVxuZm9yIG5hbWUsIHBwbCBpbiBjdXJ2ZXMuaXRlbXMoKTpcbiAgICBwcmludChmXCJ7bmFtZToxNHN9OiBmaW5hbCBQUEwgPSB7cHBsWy0xXTouMWZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktU2NhbGUgUmV0ZW50aW9uIChNU1IpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXROZXQgdXNlcyBtdWx0aS1zY2FsZSByZXRlbnRpb24gKE1TUikgYXMgaXRzIG11bHRpLWhlYWQgbWVjaGFuaXNtOiBlYWNoIGhlYWQgaGFzIGEgZGlmZmVyZW50IGRlY2F5IGZhY3RvciDOs+KClSA9IDEgLSAyXigtNS1oKSBmb3IgaCA9IDAsLi4uLEgtMS4gRm9yIEg9OCBoZWFkcywgdGhlIGdhbW1hcyByYW5nZSBmcm9tIDEtMl57LTV9IOKJiCAwLjk3IChzbG93IGRlY2F5LCBsb25nIG1lbW9yeSkgdG8gMS0yXnstMTJ9IOKJiCAwLjk5OTggKHZlcnkgc2xvdyBkZWNheSkuIFRoaXMgZ2l2ZXMgZGlmZmVyZW50IGhlYWRzIGRpZmZlcmVudCB0ZW1wb3JhbCByZWNlcHRpdmUgZmllbGRzIOKAlCBoZWFkcyB3aXRoIHNtYWxsIM6zIGZvY3VzIG9uIHJlY2VudCBjb250ZXh0IHdoaWxlIGhlYWRzIHdpdGggbGFyZ2UgzrMgbWFpbnRhaW4gbG9uZ2VyIGhpc3RvcnkuIE1TUiBwcm92aWRlcyB0aGUgdGVtcG9yYWwgZGl2ZXJzaXR5IHRoYXQgbXVsdGktaGVhZCBhdHRlbnRpb24gYWNoaWV2ZXMgdGhyb3VnaCBjb250ZW50LWJhc2VkIHNlbGVjdGlvbiwgYnV0IGhlcmUgaXQgaXMgYWNoaWV2ZWQgcHVyZWx5IHRocm91Z2ggc3RydWN0dXJhbCBkZWNheSBwYXJhbWV0ZXJzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsizrMgY2xvc2UgdG8gMSAoZS5nLiAwLjk5OTcpOiB2ZXJ5IHNsb3cgZGVjYXkg4oCUIGhlYWQgcmV0YWlucyBzaWduYWwgb3ZlciB0aG91c2FuZHMgb2Ygc3RlcHMiLCLOsyBjbG9zZSB0byAwLjkgKGUuZy4gMC45Nyk6IGZhc3RlciBkZWNheSDigJQgaGVhZCBmb2N1c2VzIG9uIHRoZSBsYXN0IH4zMCBwb3NpdGlvbnMiLCJFZmZlY3RpdmUgcmVjZXB0aXZlIGZpZWxkIG9mIGhlYWQgaDogYXBwcm94aW1hdGVseSAxLygxLc6z4oKVKSB0b2tlbnMiLCJObyBsZWFybmVkIHBvc2l0aW9uIGVuY29kaW5nIG5lZWRlZDogZGVjYXkgbWFzayBEIGVuY29kZXMgcmVsYXRpdmUgcG9zaXRpb24gaW1wbGljaXRseSIsIk1TUiBjb25jYXRlbmF0ZWQgYW5kIHByb2plY3RlZDogc2FtZSBzaGFwZSBhcyBtdWx0aS1oZWFkIGF0dGVudGlvbiBvdXRwdXQiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9kZWwgQ29tcGFyaXNvbiBUYWJsZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIlBhcmFsbGVsaXphYmxlIiwiSW5mZXJlbmNlIE8oKSIsIlJlY3VycmVudCBTdGF0ZSIsIlNvZnRtYXgiLCJBdHRlbnRpb24gQ29tcGxleGl0eSJdLCJyb3dzIjpbWyJUcmFuc2Zvcm1lciIsIlllcyAoTyhMXjIpKSIsIk8oTMK3ZCkgS1YgY2FjaGUiLCJObyAoS1YgZ3Jvd3MpIiwiWWVzIiwiTyhMXjIpIl0sWyJSZXROZXQiLCJZZXMgKHBhcmFsbGVsIG1vZGUpIiwiTyhkXjIpIGZpeGVkIiwiWWVzIChkw5dkIG1hdHJpeCkiLCJObyIsIk8oTF4yKSB0cmFpbiAvIE8oMSkgaW5mZXIiXSxbIk1hbWJhIiwiWWVzIChwYXJhbGxlbCBzY2FuKSIsIk8oTsK3ZCkgZml4ZWQiLCJZZXMgKE7Dl2QpIiwiTm8iLCJPKEwpIHNjYW4iXSxbIlJXS1YiLCJZZXMgKHBhcmFsbGVsKSIsIk8oZF4yKSBmaXhlZCIsIlllcyAoZMOXZCBtYXRyaXgpIiwiTm8iLCJPKEwpIl0sWyJMaW5lYXIgQXR0biIsIlllcyAoTyhMwrdkXjIpKSIsIk8oZF4yKSBmaXhlZCIsIlllcyAoZMOXZCBtYXRyaXgpIiwiTm8iLCJPKEzCt2QpIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJldE5ldCBvY2N1cGllcyBhbiBpbnRlcmVzdGluZyBwb3NpdGlvbjogaXQgYWNoaWV2ZXMgVHJhbnNmb3JtZXItbGV2ZWwgcGVycGxleGl0eSAod2l0aGluIDAuNSBQUEwgYXQgZXF1aXZhbGVudCBwYXJhbWV0ZXIgY291bnRzKSwgb2ZmZXJzIDjDlyBmYXN0ZXIgaW5mZXJlbmNlIHRoYW4gVHJhbnNmb3JtZXIgYXQgTD04MTkyIGR1ZSB0byB0aGUgZml4ZWQtc2l6ZSBzdGF0ZSwgYW5kIHRyYWlucyBlZmZpY2llbnRseSBpbiBwYXJhbGxlbCBtb2RlLiBJdHMgbWFpbiBsaW1pdGF0aW9uIHJlbGF0aXZlIHRvIE1hbWJhIGlzIHRoZSBsYWNrIG9mIGNvbnRlbnQtc2VsZWN0aXZpdHkg4oCUIHRoZSBleHBvbmVudGlhbCBkZWNheSBpcyBmaXhlZCBwZXIgaGVhZCwgc28gdGhlIG1vZGVsIGNhbm5vdCBkeW5hbWljYWxseSBjaG9vc2UgdG8gYXR0ZW5kIG9yIGlnbm9yZSBzcGVjaWZpYyB0b2tlbnMuIEh5YnJpZCBhcmNoaXRlY3R1cmVzIGNvbWJpbmluZyBSZXROZXQtc3R5bGUgbGluZWFyIHJlY3VycmVuY2UgbGF5ZXJzIHdpdGggb2NjYXNpb25hbCBmdWxsIGF0dGVudGlvbiBsYXllcnMgc2hvdyBwcm9taXNlIGZvciBjb21iaW5pbmcgdGhlIGJlc3Qgb2YgYm90aCBhcHByb2FjaGVzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUmV0TmV0IHBhcGVyIHJlcG9ydHMgOC40w5cgdGhyb3VnaHB1dCBpbXByb3ZlbWVudCBvdmVyIFRyYW5zZm9ybWVyIGF0IGluZmVyZW5jZSAoTD04MTkyKSIsIk1lbW9yeTogTyhkwrIpIHN0YXRlIHZzIE8oTMK3ZCkgS1YgY2FjaGUg4oCUIGZpeGVkIHJlZ2FyZGxlc3Mgb2Ygc2VxdWVuY2UgbGVuZ3RoIiwiTWF0Y2hlcyBHUFQtMyBwZXJwbGV4aXR5IGF0IDYuN0IgcGFyYW1ldGVycyB3aXRoIGZhc3RlciBpbmZlcmVuY2UiLCJ0b3JjaHNjYWxlIGxpYnJhcnkgKE1pY3Jvc29mdCkgaW1wbGVtZW50cyBSZXROZXQ6IHBpcCBpbnN0YWxsIHRvcmNoc2NhbGUiLCJIeWJyaWQgUmV0TmV0ICsgZnVsbCBhdHRlbnRpb24gZXZlcnkgayBsYXllcnMgaW1wcm92ZXMgcXVhbGl0eSB3aXRoIG1pbmltYWwgaW5mZXJlbmNlIGNvc3QiXX1d"
---
# RetNet — Retention Mechanism and Parallel/Recurrent Modes

RetNet (Sun et al., 2023) targets the impossible triangle of sequence modeling: training parallelism, low-cost inference, and strong performance. Transformers offer training parallelism and strong performance but O(L) KV-cache at inference. RNNs offer O(1) inference but are sequential during training. RetNet introduces the retention mechanism — a linear recurrence with exponential decay — that achieves all three simultaneously: parallel mode for fast GPU training, recurrent mode for O(1) per-step inference, and a chunkwise mode that interpolates between the two.

## The Three Computation Modes

RetNet's retention mechanism can be computed in three mathematically equivalent ways. Parallel mode: Ret(Q,K,V) = (QKᵀ ⊙ D) V where D[m,n] = γ^{m-n} if m ≥ n else 0 is the causal decay mask — identical structure to attention but with no softmax and an exponential decay instead of uniform weighting. Recurrent mode: Sₙ = γSₙ₋₁ + kₙᵀvₙ, retₙ = qₙSₙ — constant O(d²) state updated O(1) per step. Chunkwise mode: process chunks of C tokens in parallel (using local decay masks) while maintaining a recurrent state across chunks.

- Parallel: O(L²·d) — same GPU utilization as attention, ideal for training
- Recurrent: O(d²) state, O(d²) per step — constant memory, ideal for inference
- Chunkwise: O(C²·d + L/C·d²) — balanced training and prefill speed
- γ ∈ (0,1): decay factor per head — controls how quickly old information is forgotten
- No softmax: retention is linear — removes numerical instability and enables recurrent form

## Parallel Mode — O(L²) Training

The parallel retention formula Ret = (QKᵀ ⊙ D)V closely mirrors scaled dot-product attention: Q, K, V are linear projections of the input, and the output is a weighted sum of values. The difference is in the weighting: attention uses softmax(QKᵀ / √d) for position-aware soft selection, while retention uses the fixed causal decay mask D[m,n] = γ^{m-n} which exponentially down-weights contributions from distant positions. This means retention is content-agnostic in its positional weighting — it cannot attend selectively like Mamba — but it admits the recurrent form that attention does not.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def build_decay_mask(L, gamma, device='cpu'):
    """D[m,n] = gamma^(m-n) if m>=n else 0 — causal exponential decay mask."""
    idx = torch.arange(L, device=device).float()
    D   = gamma ** (idx.unsqueeze(0) - idx.unsqueeze(1))   # (L, L)
    return torch.tril(D)    # causal: zero out future positions

class ParallelRetention(nn.Module):
    def __init__(self, d_model, heads=4):
        super().__init__()
        self.heads  = heads
        self.d_head = d_model // heads
        self.Q = nn.Linear(d_model, d_model, bias=False)
        self.K = nn.Linear(d_model, d_model, bias=False)
        self.V = nn.Linear(d_model, d_model, bias=False)
        self.out = nn.Linear(d_model, d_model, bias=False)
        # Multi-scale: different gamma per head
        gammas = 1 - 2 ** (-5 - torch.arange(heads).float())
        self.register_buffer('gammas', gammas)

    def forward(self, x):
        B, L, d = x.shape
        Q = self.Q(x).view(B, L, self.heads, self.d_head).transpose(1, 2)  # (B,H,L,dh)
        K = self.K(x).view(B, L, self.heads, self.d_head).transpose(1, 2)
        V = self.V(x).view(B, L, self.heads, self.d_head).transpose(1, 2)
        out = torch.zeros_like(Q)
        for h in range(self.heads):
            D   = build_decay_mask(L, self.gammas[h].item(), x.device)     # (L, L)
            ret = (Q[:, h] @ K[:, h].transpose(-1, -2)) * D.unsqueeze(0)  # (B,L,L)
            out[:, h] = ret @ V[:, h]
        return self.out(out.transpose(1, 2).reshape(B, L, d))

model = ParallelRetention(d_model=128, heads=4)
x = torch.randn(2, 16, 128)
print(f"Parallel retention output: {model(x).shape}")
```

## Recurrent Mode — O(1) Inference

The recurrent form of retention processes one token at a time: at step n, the state Sₙ = γSₙ₋₁ + kₙᵀvₙ is a d × d matrix accumulating weighted outer products of keys and values. The output is retₙ = qₙSₙ — a simple matrix-vector product. No KV cache is needed: the entire sequence history is compressed into the fixed-size state S. This gives O(1) memory overhead and O(d²) compute per step, independent of sequence length — a significant advantage over Transformer's O(L·d) KV cache that grows with every new token.

```python
import torch
import torch.nn as nn

class RecurrentRetention(nn.Module):
    """RetNet recurrent mode: O(1) per step, O(d^2) fixed state."""
    def __init__(self, d_model, heads=4):
        super().__init__()
        self.heads  = heads
        self.d_head = d_model // heads
        self.Q  = nn.Linear(d_model, d_model, bias=False)
        self.K  = nn.Linear(d_model, d_model, bias=False)
        self.V  = nn.Linear(d_model, d_model, bias=False)
        self.out = nn.Linear(d_model, d_model, bias=False)
        gammas = 1 - 2 ** (-5 - torch.arange(heads).float())
        self.register_buffer('gammas', gammas)

    def step(self, x_t, S):
        """Process one token, update state S: (B, heads, d_head, d_head)."""
        B  = x_t.shape[0]
        q  = self.Q(x_t).view(B, self.heads, self.d_head)
        k  = self.K(x_t).view(B, self.heads, self.d_head)
        v  = self.V(x_t).view(B, self.heads, self.d_head)
        # S_n = gamma * S_{n-1} + k_n^T v_n  (outer product accumulation)
        S  = self.gammas.view(1,-1,1,1) * S + torch.einsum('bhd,bhe->bhde', k, v)
        # ret_n = q_n S_n
        ret = torch.einsum('bhd,bhde->bhe', q, S).reshape(B, -1)
        return self.out(ret), S

d, H, B = 64, 4, 2
model = RecurrentRetention(d, H)
S = torch.zeros(B, H, d//H, d//H)    # initial state
print("Autoregressive recurrent generation:")
for t in range(6):
    x_t = torch.randn(B, d)
    out, S = model.step(x_t, S)
print(f"Output: {out.shape}, State: {S.shape}, State norm: {S.norm():.3f}")
```

## Chunkwise Mode

The chunkwise mode processes the sequence in chunks of size C. Within each chunk, parallel retention is applied using a local decay mask — identical to parallel mode but only C×C instead of L×L. Across chunks, the recurrent state is updated to carry information from past chunks. The within-chunk parallel computation achieves high GPU utilization, while the across-chunk recurrence keeps memory bounded. Chunkwise is the recommended mode for training on long documents: choose C such that C² fits comfortably in GPU memory while L/C recurrent updates are cheap.

```python
import torch

def chunkwise_retention(Q, K, V, gamma, chunk_size=32):
    """
    Chunkwise retention: parallel within chunk, recurrent across chunks.
    Q, K, V: (B, L, d) — all same dimension for simplicity.
    """
    B, L, d = Q.shape
    n_chunks = (L + chunk_size - 1) // chunk_size
    outputs  = []
    S = torch.zeros(B, d, d, device=Q.device)     # cross-chunk state (B, d, d)

    for c in range(n_chunks):
        s, e    = c * chunk_size, min((c+1) * chunk_size, L)
        q_c, k_c, v_c = Q[:, s:e], K[:, s:e], V[:, s:e]
        cs = e - s

        # Intra-chunk parallel retention
        idx = torch.arange(cs, device=Q.device).float()
        D   = torch.tril(gamma ** (idx.unsqueeze(0) - idx.unsqueeze(1))).unsqueeze(0)
        intra = ((q_c @ k_c.transpose(-1,-2)) * D) @ v_c       # (B, cs, d)

        # Cross-chunk: contribution from accumulated past state
        decay  = gamma ** torch.arange(cs, 0, -1, dtype=torch.float32, device=Q.device)
        cross  = (q_c * decay.view(1,-1,1)) @ S                 # (B, cs, d)

        outputs.append(intra + cross)
        # Update state: S_new = gamma^cs * S + K_c^T V_c
        S = gamma**cs * S + k_c.transpose(-1,-2) @ v_c

    return torch.cat(outputs, dim=1)

B, L, d = 2, 64, 32
Q = K = V = torch.randn(B, L, d)
out = chunkwise_retention(Q, K, V, gamma=0.9, chunk_size=16)
print(f"Chunkwise output: {out.shape}")   # (2, 64, 32)
```

> **Choosing Chunk Size**: For training on sequences of length L=8192, a chunk size of C=512 gives 16 recurrent steps across chunks. Within each chunk the C×C=262K element matrix is small enough for fast matrix multiplication on modern GPUs. For inference, switch to recurrent mode (C=1) — no code changes needed, just call the recurrent step function instead of the parallel forward.

## Code 4 — RetNet vs Transformer Perplexity Comparison

```python
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

class TinyRetNet(nn.Module):
    """Minimal RetNet-like LM using GRU as retention proxy for benchmarking."""
    def __init__(self, vocab, d):
        super().__init__()
        self.embed = nn.Embedding(vocab, d)
        self.gru   = nn.GRU(d, d, batch_first=True)
        self.head  = nn.Linear(d, vocab)
    def forward(self, x):
        h, _ = self.gru(self.embed(x))
        return self.head(h)

def sim_curve(start, rate, floor, n=200, noise=1.2, seed=0):
    """Simulate perplexity training curve."""
    np.random.seed(seed)
    return start * np.exp(-rate * np.arange(1, n+1)) + floor + np.random.randn(n) * noise

steps  = np.arange(1, 201)
curves = {
    'Transformer':   sim_curve(200, 0.018, 15.0, seed=0),
    'RetNet':        sim_curve(200, 0.019, 14.5, seed=1),
    'Mamba':         sim_curve(200, 0.020, 14.2, seed=2),
    'RWKV':          sim_curve(200, 0.017, 15.8, seed=3),
}
colors = ['steelblue', 'forestgreen', 'tomato', 'orange']

fig, ax = plt.subplots(figsize=(9, 5))
for (name, ppl), color in zip(curves.items(), colors):
    ax.plot(steps, ppl, alpha=0.8, label=name, color=color, linewidth=1.5)
ax.set_yscale('log')
ax.set_xlabel('Training Steps'); ax.set_ylabel('Perplexity (log scale)')
ax.set_title('LM Training Curves: RetNet vs Alternatives')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('retnet_ppl.png', dpi=120); plt.show()
for name, ppl in curves.items():
    print(f"{name:14s}: final PPL = {ppl[-1]:.1f}")
```

## Multi-Scale Retention (MSR)

RetNet uses multi-scale retention (MSR) as its multi-head mechanism: each head has a different decay factor γₕ = 1 - 2^(-5-h) for h = 0,...,H-1. For H=8 heads, the gammas range from 1-2^{-5} ≈ 0.97 (slow decay, long memory) to 1-2^{-12} ≈ 0.9998 (very slow decay). This gives different heads different temporal receptive fields — heads with small γ focus on recent context while heads with large γ maintain longer history. MSR provides the temporal diversity that multi-head attention achieves through content-based selection, but here it is achieved purely through structural decay parameters.

- γ close to 1 (e.g. 0.9997): very slow decay — head retains signal over thousands of steps
- γ close to 0.9 (e.g. 0.97): faster decay — head focuses on the last ~30 positions
- Effective receptive field of head h: approximately 1/(1-γₕ) tokens
- No learned position encoding needed: decay mask D encodes relative position implicitly
- MSR concatenated and projected: same shape as multi-head attention output

## Model Comparison Table

| Model | Parallelizable | Inference O() | Recurrent State | Softmax | Attention Complexity |
| --- | --- | --- | --- | --- | --- |
| Transformer | Yes (O(L^2)) | O(L·d) KV cache | No (KV grows) | Yes | O(L^2) |
| RetNet | Yes (parallel mode) | O(d^2) fixed | Yes (d×d matrix) | No | O(L^2) train / O(1) infer |
| Mamba | Yes (parallel scan) | O(N·d) fixed | Yes (N×d) | No | O(L) scan |
| RWKV | Yes (parallel) | O(d^2) fixed | Yes (d×d matrix) | No | O(L) |
| Linear Attn | Yes (O(L·d^2)) | O(d^2) fixed | Yes (d×d matrix) | No | O(L·d) |

RetNet occupies an interesting position: it achieves Transformer-level perplexity (within 0.5 PPL at equivalent parameter counts), offers 8× faster inference than Transformer at L=8192 due to the fixed-size state, and trains efficiently in parallel mode. Its main limitation relative to Mamba is the lack of content-selectivity — the exponential decay is fixed per head, so the model cannot dynamically choose to attend or ignore specific tokens. Hybrid architectures combining RetNet-style linear recurrence layers with occasional full attention layers show promise for combining the best of both approaches.

- RetNet paper reports 8.4× throughput improvement over Transformer at inference (L=8192)
- Memory: O(d²) state vs O(L·d) KV cache — fixed regardless of sequence length
- Matches GPT-3 perplexity at 6.7B parameters with faster inference
- torchscale library (Microsoft) implements RetNet: pip install torchscale
- Hybrid RetNet + full attention every k layers improves quality with minimal inference cost

