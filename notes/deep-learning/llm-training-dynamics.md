---
title: "LLM Training Dynamics — Warmup, Loss Spikes, and Gradient Norm Monitoring"
slug: "llm-training-dynamics"
description: "Practical guide to LLM pretraining stability: LR warmup schedules, cosine annealing, loss spike causes and recovery, gradient norm clipping, and checkpoint strategies for robust large-scale training."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhaW5pbmcgbGFyZ2UgbGFuZ3VhZ2UgbW9kZWxzIGF0IHNjYWxlIHN1cmZhY2VzIGEgY2xhc3Mgb2YgaW5zdGFiaWxpdHkgcHJvYmxlbXMgdGhhdCBkbyBub3QgYXBwZWFyIGF0IHNtYWxsZXIgc2NhbGVzOiBsb3NzIHNwaWtlcyB0aGF0IGNhbiBkZXJhaWwgYSBydW4gYWZ0ZXIgdGhvdXNhbmRzIG9mIEdQVS1ob3VycywgZ3JhZGllbnQgZXhwbG9zaW9ucyB0aGF0IGNvcnJ1cHQgbW9kZWwgd2VpZ2h0cywgYW5kIHNjaGVkdWxpbmcgYnVncyB0aGF0IGNhdXNlIHNpbGVudCB1bmRlcmZpdHRpbmcuIFVuZGVyc3RhbmRpbmcgdGhlIGludGVycGxheSBiZXR3ZWVuIHRoZSBsZWFybmluZyByYXRlIHNjaGVkdWxlLCB0aGUgQWRhbSBvcHRpbWl6ZXJcdTAwMjdzIG1vbWVudCBlc3RpbWF0ZXMsIGFuZCBncmFkaWVudCBub3JtIGR5bmFtaWNzIGlzIGVzc2VudGlhbCBmb3IgYW55b25lIHJ1bm5pbmcgb3IgZGVidWdnaW5nIExMTSBwcmV0cmFpbmluZy4gVGhpcyBub3RlIGNvdmVycyB0aGUgZm91ciBtb3N0IGltcG9ydGFudCBsZXZlcnM6IHdhcm11cCwgY29zaW5lIGFubmVhbGluZywgZ3JhZGllbnQgbm9ybSBtb25pdG9yaW5nLCBhbmQgY2hlY2twb2ludCByb2xsYmFjay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMZWFybmluZyBSYXRlIFdhcm11cCBhbmQgdGhlIEFkYW0gQmlhcyBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdCBzdGVwIDAsIEFkYW1cdTAwMjdzIGZpcnN0LW1vbWVudCBlc3RpbWF0ZSBt4oKAID0gMCBhbmQgc2Vjb25kLW1vbWVudCBlc3RpbWF0ZSB24oKAID0gMC4gVGhlIGJpYXMgY29ycmVjdGlvbiBmYWN0b3JzIDEvKDEg4oiSIM6y4oKB4bWXKSBhbmQgMS8oMSDiiJIgzrLigoLhtZcpIHBhcnRpYWxseSBjb21wZW5zYXRlIGZvciB0aGlzIGNvbGQtc3RhcnQsIGJ1dCBpbiBwcmFjdGljZSB0aGUgZWZmZWN0aXZlIHBlci1wYXJhbWV0ZXIgc3RlcCBzaXplcyBhcmUgcG9vcmx5IGNhbGlicmF0ZWQgZm9yIHRoZSBmaXJzdCBmZXcgaHVuZHJlZCBzdGVwcy4gU3RhcnRpbmcgYXQgdGhlIGZ1bGwgdGFyZ2V0IGxlYXJuaW5nIHJhdGUgZHVyaW5nIHRoaXMgcGVyaW9kIGNhdXNlcyBsYXJnZSwgbm9pc3kgZ3JhZGllbnQgdXBkYXRlcyB0aGF0IG1vdmUgcGFyYW1ldGVycyBmYXIgZnJvbSB0aGVpciBpbml0aWFsaXphdGlvbi4gTGluZWFyIHdhcm11cCBmcm9tIDAgdG8gzrdfbWF4IG92ZXIgdGhlIGZpcnN0IH4yMDAwIHN0ZXBzIGFsbG93cyB0aGUgbW9tZW50IGVzdGltYXRlcyB0byBzdGFiaWxpemUgYmVmb3JlIHRoZSBvcHRpbWl6ZXIgb3BlcmF0ZXMgYXQgZnVsbCBsZWFybmluZyByYXRlLCBkcmFtYXRpY2FsbHkgcmVkdWNpbmcgZWFybHktdHJhaW5pbmcgZGl2ZXJnZW5jZSByaXNrLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTGluZWFyIHdhcm11cDogTFIodCkgPSDOt19tYXggw5cgdCAvIFRfd2FybXVwIGZvciB0IFx1MDAzYyBUX3dhcm11cCwgdHlwaWNhbGx5IFRfd2FybXVwID0gMjAwMCBzdGVwcyIsIs6y4oKCID0gMC45NeKAkzAuOTk5IGluIGxhcmdlIExMTXM7IGhpZ2hlciDOsuKCgiBtZWFucyBsb25nZXIgbW9tZW50IHdhcm0tdXAgcGVyaW9kIiwiU2tpcHBpbmcgd2FybXVwIHdpdGggQWRhbSBhdCBMUj0zZS00IG9uIGEgVHJhbnNmb3JtZXIgb2Z0ZW4gY2F1c2VzIGRpdmVyZ2VuY2UgaW4gZmlyc3QgMTAwIHN0ZXBzIiwiR1BULTMgdXNlZCBUX3dhcm11cCA9IDM3NU0gdG9rZW5zOyBMTGFNQSB1c2VkIFRfd2FybXVwIOKJiCAyMDAwIHN0ZXBzIGF0IGJhdGNoIDRNIHRva2VucyIsImJmMTYgdHJhaW5pbmcgaXMgbW9yZSBzZW5zaXRpdmUgdG8gZWFybHkgTFIgc3Bpa2VzIHRoYW4gZnAzMiBkdWUgdG8gcmVkdWNlZCBwcmVjaXNpb24gcmFuZ2UiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29zaW5lIEFubmVhbGluZyBBZnRlciBXYXJtdXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFmdGVyIHdhcm11cCwgdGhlIHN0YW5kYXJkIHNjaGVkdWxlIGZvciBMTE0gcHJldHJhaW5pbmcgaXMgY29zaW5lIGFubmVhbGluZzogTFIodCkgPSDOt19taW4gKyAozrdfbWF4IOKIkiDOt19taW4pIMOXIGNvcyjPgCDDlyB0IC8gVCkgLyAyLCB3aGVyZSBUIGlzIHRoZSB0b3RhbCB0cmFpbmluZyBzdGVwcyBhbmQgzrdfbWluIGlzIGEgZmxvb3IgKHR5cGljYWxseSAxZS01IG9yIDEwJSBvZiDOt19tYXgpLiBDb3NpbmUgZGVjYXkgaXMgcHJlZmVycmVkIG92ZXIgc3RlcCBkZWNheSBiZWNhdXNlIGl0IHByb3ZpZGVzIGEgc21vb3RoLCBjb250aW51b3VzIHJlZHVjdGlvbiB0aGF0IGF2b2lkcyBzdWRkZW4gTFIgZHJvcHMgd2hpY2ggY2FuIGRlc3RhYmlsaXplIEFkYW1cdTAwMjdzIG1vbWVudHVtIGVzdGltYXRlcy4gVGhlIGZpbmFsIDEwJSBvZiB0cmFpbmluZyBhdCBuZWFyLXplcm8gTFIgb2Z0ZW4gcmVjb3ZlcnMgMC4z4oCTMC41IHBlcnBsZXhpdHkgcG9pbnRzIGNvbXBhcmVkIHRvIHN0b3BwaW5nIGNvc2luZSBkZWNheSBlYXJseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG1hdGhcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIGdldF9scihzdGVwLCB3YXJtdXBfc3RlcHMsIHRvdGFsX3N0ZXBzLCBscl9tYXgsIGxyX21pbj0xZS01KTpcbiAgICBcIlwiXCJMaW5lYXIgd2FybXVwIHRoZW4gY29zaW5lIGFubmVhbGluZyB0byBscl9taW4uXCJcIlwiXG4gICAgaWYgc3RlcCBcdTAwM2Mgd2FybXVwX3N0ZXBzOlxuICAgICAgICByZXR1cm4gbHJfbWF4ICogc3RlcCAvIG1heCh3YXJtdXBfc3RlcHMsIDEpXG4gICAgcHJvZ3Jlc3MgPSAoc3RlcCAtIHdhcm11cF9zdGVwcykgLyBtYXgodG90YWxfc3RlcHMgLSB3YXJtdXBfc3RlcHMsIDEpXG4gICAgcmV0dXJuIGxyX21pbiArIDAuNSAqIChscl9tYXggLSBscl9taW4pICogKDEgKyBtYXRoLmNvcyhtYXRoLnBpICogcHJvZ3Jlc3MpKVxuXG53YXJtdXBfc3RlcHMsIHRvdGFsX3N0ZXBzID0gMjAwMCwgMTAwXzAwMFxubHJfbWF4LCBscl9taW4gPSAzZS00LCAxZS01XG5cbnN0ZXBzID0gbGlzdChyYW5nZSgwLCB0b3RhbF9zdGVwcywgMjAwKSlcbmxycyAgID0gW2dldF9scihzLCB3YXJtdXBfc3RlcHMsIHRvdGFsX3N0ZXBzLCBscl9tYXgsIGxyX21pbikgZm9yIHMgaW4gc3RlcHNdXG5cbmZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oMTAsIDQpKVxuYXgucGxvdChzdGVwcywgbHJzLCBcdTAwMjdiLVx1MDAyNywgbGluZXdpZHRoPTIsIGxhYmVsPVx1MDAyN0xSIHNjaGVkdWxlXHUwMDI3KVxuYXguYXh2bGluZSh3YXJtdXBfc3RlcHMsIGNvbG9yPVx1MDAyN29yYW5nZVx1MDAyNywgbGluZXN0eWxlPVx1MDAyNy0tXHUwMDI3LCBsYWJlbD1mXHUwMDI3V2FybXVwIGVuZCAoe3dhcm11cF9zdGVwc30gc3RlcHMpXHUwMDI3KVxuYXguc2V0X3hsYWJlbChcdTAwMjdUcmFpbmluZyBTdGVwXHUwMDI3KTsgYXguc2V0X3lsYWJlbChcdTAwMjdMZWFybmluZyBSYXRlXHUwMDI3KVxuYXguc2V0X3RpdGxlKFx1MDAyN0xSOiBMaW5lYXIgV2FybXVwICsgQ29zaW5lIEFubmVhbGluZyAoZXRhX21pbj0xZS01KVx1MDAyNylcbmF4LmxlZ2VuZCgpOyBheC5ncmlkKFRydWUsIGFscGhhPTAuMylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3bHJfc2NoZWR1bGUucG5nXHUwMDI3LCBkcGk9MTIwKVxucHJpbnQoZlwiUGVhayBMUjoge21heChscnMpOi4yZX0gIEVuZCBMUjoge2xyc1stMV06LjJlfSAgV2FybXVwOiB7d2FybXVwX3N0ZXBzL3RvdGFsX3N0ZXBzOi4xJX0gb2YgdHJhaW5pbmdcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb3NzIFNwaWtlcyDigJQgQ2F1c2VzIGFuZCBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgbG9zcyBzcGlrZSBpcyBhIHN1ZGRlbiBzaGFycCBpbmNyZWFzZSBpbiB0cmFpbmluZyBsb3NzIOKAlCB0eXBpY2FsbHkgMuKAkzEww5cgYmFzZWxpbmUg4oCUIGZvbGxvd2VkIGJ5IGdyYWR1YWwgcmVjb3Zlcnkgb3ZlciAxMDDigJM1MDAgc3RlcHMuIFNwaWtlcyBhcmUgdGhlIG1vc3QgY29tbW9uIGNhdXNlIG9mIGNhdGFzdHJvcGhpYyBMTE0gcHJldHJhaW5pbmcgZmFpbHVyZXMuIE1vc3Qgc3Bpa2VzIHNlbGYtaGVhbCBpZiB0aGUgTFIgaXMgbm90IHRvbyBoaWdoOyBpbiBzZXZlcmUgY2FzZXMgdGhlIG1vZGVsIG5ldmVyIHJlY292ZXJzIGFuZCB0aGUgcnVuIG11c3QgYmUgcmVzdGFydGVkIGZyb20gYSBjaGVja3BvaW50LiBUaGUgcHJpbWFyeSBjYXVzZXMgYXJlIGRhdGEtcmVsYXRlZDogbWFsZm9ybWVkIFVuaWNvZGUgc2VxdWVuY2VzIGNhdXNlIHRva2VuaXplciBvdXRwdXQgYW5vbWFsaWVzOyByZXBlYXRlZCB0b2tlbnMgcGFkIGRvY3VtZW50cyB0byBleHRyZW1lIGxlbmd0aHM7IGVtcHR5IG9yIG5lYXItZW1wdHkgZG9jdW1lbnRzIHByb2R1Y2UgdW5kZWZpbmVkIGxvc3MgdmFsdWVzLiBIYXJkd2FyZSBmYXVsdHMgKE5hTi1wcm9kdWNpbmcgRlAgb3BlcmF0aW9ucykgYW5kIExSIHNjaGVkdWxlIGJ1Z3MgYXJlIHNlY29uZGFyeSBjYXVzZXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJEYXRhIGFub21hbGllczogbWFsZm9ybWVkIFVuaWNvZGUsIGVuY29kaW5nIGVycm9ycywgZW1wdHkgZG9jdW1lbnRzLCByZXBlYXRlZC10b2tlbiBwYWRkaW5nIiwiTFIgdG9vIGhpZ2g6IGdyYWRpZW50IHN0ZXAgb3Zlcmhvb3RzIGxvc3MgbWluaW11bSwgY2F1c2VzIGNoYW90aWMgd2FuZGVyaW5nIiwiQmFkIGJhdGNoOiBzaW5nbGUgZXh0cmVtZWx5IGhpZ2gtbG9zcyBkb2N1bWVudCAoY29ycnVwdGVkIGxhYmVsIG9yIGxlbmd0aCBvdXRsaWVyKSIsIkdyYWRpZW50IG92ZXJmbG93OiBmcDE2L2JmMTYgZ3JhZGllbnRzIHNhdHVyYXRlOyBOYU4gcHJvcGFnYXRlcyBpbnRvIHdlaWdodHMgdmlhIEFkYW0gdXBkYXRlIiwiQXJjaGl0ZWN0dXJlIGJ1ZzogYXR0ZW50aW9uIGxvZ2l0IGV4cGxvc2lvbiBpbiBkZWVwIG1vZGVscyB3aXRoIGluY29ycmVjdCBpbml0aWFsaXphdGlvbiJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6Ildhcm5pbmciLCJjb250ZW50IjoiTG9zcyBzcGlrZXMgZnJvbSBkYXRhIHF1YWxpdHkgaXNzdWVzIChtYWxmb3JtZWQgVW5pY29kZSwgZW1wdHkgZG9jdW1lbnRzLCByZXBlYXRlZCB0b2tlbnMpIGFyZSB0aGUgbW9zdCBjb21tb24gY2F1c2Ugb2YgTExNIHRyYWluaW5nIGluc3RhYmlsaXR5IOKAlCBhZ2dyZXNzaXZlIGRhdGEgZmlsdGVyaW5nIGFuZCBkb2N1bWVudCBsZW5ndGggY2FwcGluZyBwcmV2ZW50IG1vc3Qgc3Bpa2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdyYWRpZW50IE5vcm0gTW9uaXRvcmluZyBhbmQgQ2xpcHBpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBnbG9iYWwgZ3JhZGllbnQgbm9ybSDigJbiiIdM4oCW4oKCID0gc3FydCjOo+G1oiDigJbiiIdM4bWi4oCWwrIpIGNvbXB1dGVkIGFjcm9zcyBhbGwgcGFyYW1ldGVycyBpcyBvbmUgb2YgdGhlIG1vc3QgaW5mb3JtYXRpdmUgdHJhaW5pbmcgZGlhZ25vc3RpY3MuIEEgaGVhbHRoeSBMTE0gcnVuIHNob3dzIGdyYWRpZW50IG5vcm1zIGluIHRoZSByYW5nZSAwLjHigJMyLjAuIFN1c3RhaW5lZCBub3JtcyBhYm92ZSA1LjAgaW5kaWNhdGUgaW5zdGFiaWxpdHkgdGhhdCB1c3VhbGx5IHByZWNlZGVzIGEgbG9zcyBzcGlrZSBieSA1MOKAkzIwMCBzdGVwcy4gR2xvYmFsIG5vcm0gY2xpcHBpbmcgcmVzY2FsZXMgdGhlIGVudGlyZSBncmFkaWVudCB2ZWN0b3Igd2hlbiDigJZn4oCWIFx1MDAzZSBjbGlwX25vcm06IGcg4oaQIGcgw5cgKGNsaXBfbm9ybSAvIOKAlmfigJYpLiBUaGlzIHByZXZlbnRzIGFueSBzaW5nbGUgbGFyZ2UgZ3JhZGllbnQgZnJvbSBkcml2aW5nIGEgZGVzdHJ1Y3RpdmUgcGFyYW1ldGVyIHVwZGF0ZSB3aXRob3V0IHJlZHVjaW5nIHNtYWxsZXIgZ3JhZGllbnRzLiBTdGFuZGFyZCBjbGlwX25vcm0gPSAxLjAgZm9yIG1vc3QgTExNIHRyYWluaW5nOyBzb21lIHJlY2lwZXMgdXNlIDAuNSBmb3IgdmVyeSBkZWVwIG1vZGVscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGNvbXB1dGVfZ2xvYmFsX2dyYWRfbm9ybShtb2RlbCk6XG4gICAgXCJcIlwiQ29tcHV0ZSBnbG9iYWwgTDIgZ3JhZGllbnQgbm9ybSBhY3Jvc3MgYWxsIHBhcmFtZXRlcnMuXCJcIlwiXG4gICAgdG90YWxfbm9ybSA9IDAuMFxuICAgIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgaWYgcC5ncmFkIGlzIG5vdCBOb25lOlxuICAgICAgICAgICAgdG90YWxfbm9ybSArPSBwLmdyYWQuZGV0YWNoKCkubm9ybSgyKS5pdGVtKCkgKiogMlxuICAgIHJldHVybiB0b3RhbF9ub3JtICoqIDAuNVxuXG5kZWYgdHJhaW5fc3RlcF93aXRoX2NsaXAobW9kZWwsIG9wdGltaXplciwgbG9zcywgY2xpcF9ub3JtPTEuMCk6XG4gICAgb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgcHJlX2NsaXBfbm9ybSA9IGNvbXB1dGVfZ2xvYmFsX2dyYWRfbm9ybShtb2RlbClcbiAgICBpZiBwcmVfY2xpcF9ub3JtIFx1MDAzZSBjbGlwX25vcm06XG4gICAgICAgIHRvcmNoLm5uLnV0aWxzLmNsaXBfZ3JhZF9ub3JtXyhtb2RlbC5wYXJhbWV0ZXJzKCksIGNsaXBfbm9ybSlcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgcmV0dXJuIHByZV9jbGlwX25vcm0sIHByZV9jbGlwX25vcm0gXHUwMDNlIGNsaXBfbm9ybVxuXG4jIFNpbXVsYXRlIDEwIHRyYWluaW5nIHN0ZXBzIGFuZCBsb2cgZ3JhZGllbnQgbm9ybXNcbm1vZGVsICAgICA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDEyOCwgMjU2KSwgbm4uR0VMVSgpLCBubi5MaW5lYXIoMjU2LCAxMjgpKVxub3B0aW1pemVyID0gdG9yY2gub3B0aW0uQWRhbVcobW9kZWwucGFyYW1ldGVycygpLCBscj0zZS00LCBiZXRhcz0oMC45LCAwLjk1KSlcbm5vcm1fbG9nICA9IFtdXG5mb3Igc3RlcCBpbiByYW5nZSgxMCk6XG4gICAgeCAgICAgICAgID0gdG9yY2gucmFuZG4oMTYsIDEyOClcbiAgICBsb3NzICAgICAgPSAobW9kZWwoeCkgKiogMikubWVhbigpICsgMC4wMSAqIHRvcmNoLnJhbmRuKDEpLmFicygpXG4gICAgZ25vcm0sIGNsaXBwZWQgPSB0cmFpbl9zdGVwX3dpdGhfY2xpcChtb2RlbCwgb3B0aW1pemVyLCBsb3NzLCBjbGlwX25vcm09MS4wKVxuICAgIG5vcm1fbG9nLmFwcGVuZChnbm9ybSlcbiAgICBzdGF0dXMgPSBcdTAwMjdDTElQUEVEXHUwMDI3IGlmIGNsaXBwZWQgZWxzZSBcdTAwMjdva1x1MDAyN1xuICAgIHByaW50KGZcIlN0ZXAge3N0ZXA6MmR9OiBncmFkX25vcm09e2dub3JtOi40Zn0gIFt7c3RhdHVzfV1cIilcbnByaW50KGZcIk1lYW4gbm9ybToge3N1bShub3JtX2xvZykvbGVuKG5vcm1fbG9nKTouNGZ9ICBNYXg6IHttYXgobm9ybV9sb2cpOi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTcGlrZSBEZXRlY3Rpb24gYW5kIENoZWNrcG9pbnQgUm9sbGJhY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkF1dG9tYXRlZCBzcGlrZSBkZXRlY3Rpb24gY29tcGFyZXMgdGhlIGN1cnJlbnQgbG9zcyB0byBhIHJvbGxpbmcgYmFzZWxpbmUgY29tcHV0ZWQgb3ZlciB0aGUgbGFzdCA1MCBzdGVwcy4gSWYgdGhlIGN1cnJlbnQgbG9zcyBleGNlZWRzIHRoZSBiYXNlbGluZSBieSBtb3JlIHRoYW4gYSB0aHJlc2hvbGQgKHR5cGljYWxseSAzw5cpLCB0aGUgdHJhaW5pbmcgbG9vcCB0cmlnZ2VycyBhIHJvbGxiYWNrOiBsb2FkIHRoZSBtb3N0IHJlY2VudCBnb29kIGNoZWNrcG9pbnQsIHJlZHVjZSB0aGUgbGVhcm5pbmcgcmF0ZSBieSAyMOKAkzUwJSwgYW5kIHJlc3VtZSB0cmFpbmluZy4gTW9zdCB0cmFpbmluZyBmcmFtZXdvcmtzIHNhdmUgY2hlY2twb2ludHMgZXZlcnkgNTAw4oCTMTAwMCBzdGVwczsgc2F2aW5nIG1vcmUgZnJlcXVlbnRseSBpcyBleHBlbnNpdmUgYnV0IGFsbG93cyBmaW5lci1ncmFpbmVkIHJlY292ZXJ5LiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCBzcGlrZSByZWNvdmVyeSBpcyBtdWNoIGZhc3RlciB3aGVuIHRoZSBjaGVja3BvaW50IGlzIGNsb3NlIHRvIHRoZSBzcGlrZSDigJQgcmVzdW1pbmcgZnJvbSBzdGVwIE4tMTAwIHdpdGggcmVkdWNlZCBMUiB0eXBpY2FsbHkgcmVjb3ZlcnMgaW4gMjAw4oCTNTAwIHN0ZXBzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBvc1xuXG5kZWYgZGV0ZWN0X3NwaWtlKGxvc3NfaGlzdG9yeSwgY3VycmVudF9sb3NzLCB0aHJlc2hvbGQ9My4wLCB3aW5kb3c9NTApOlxuICAgIFwiXCJcIlJldHVybiBUcnVlIGlmIGN1cnJlbnRfbG9zcyBpcyB0aHJlc2hvbGTDlyBhYm92ZSByZWNlbnQgYmFzZWxpbmUuXCJcIlwiXG4gICAgaWYgbGVuKGxvc3NfaGlzdG9yeSkgXHUwMDNjIHdpbmRvdzpcbiAgICAgICAgcmV0dXJuIEZhbHNlXG4gICAgYmFzZWxpbmUgPSBzdW0obG9zc19oaXN0b3J5Wy13aW5kb3c6XSkgLyB3aW5kb3dcbiAgICByZXR1cm4gY3VycmVudF9sb3NzIFx1MDAzZSBiYXNlbGluZSAqIHRocmVzaG9sZFxuXG5kZWYgbG9hZF9sYXN0X2NoZWNrcG9pbnQoY2twdF9kaXIsIG1vZGVsLCBvcHRpbWl6ZXIpOlxuICAgIFwiXCJcIkxvYWQgdGhlIG1vc3QgcmVjZW50IC5wdCBjaGVja3BvaW50IGFuZCByZXR1cm4gdGhlIHN0ZXAgbnVtYmVyLlwiXCJcIlxuICAgIGNrcHRzID0gc29ydGVkKFtmIGZvciBmIGluIG9zLmxpc3RkaXIoY2twdF9kaXIpIGlmIGYuZW5kc3dpdGgoXHUwMDI3LnB0XHUwMDI3KV0pXG4gICAgaWYgbm90IGNrcHRzOlxuICAgICAgICBwcmludChcIk5vIGNoZWNrcG9pbnRzIGZvdW5kLlwiKVxuICAgICAgICByZXR1cm4gMFxuICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oY2twdF9kaXIsIGNrcHRzWy0xXSlcbiAgICBja3B0ID0gdG9yY2gubG9hZChwYXRoLCBtYXBfbG9jYXRpb249XHUwMDI3Y3B1XHUwMDI3KVxuICAgIG1vZGVsLmxvYWRfc3RhdGVfZGljdChja3B0W1x1MDAyN21vZGVsXHUwMDI3XSlcbiAgICBvcHRpbWl6ZXIubG9hZF9zdGF0ZV9kaWN0KGNrcHRbXHUwMDI3b3B0aW1pemVyXHUwMDI3XSlcbiAgICBwcmludChmXCJSb2xsZWQgYmFjayB0byBzdGVwIHtja3B0W1x1MDAyN3N0ZXBcdTAwMjddfSAobG9zcz17Y2twdFtcdTAwMjdsb3NzXHUwMDI3XTouNGZ9KVwiKVxuICAgIHJldHVybiBja3B0W1x1MDAyN3N0ZXBcdTAwMjddXG5cbiMgU2ltdWxhdGUgc3Bpa2UgZGV0ZWN0aW9uIG92ZXIgNjUgc3RlcHNcbmxvc3NfaGlzdG9yeSA9IFsyLjEgKyAwLjA0ICogKGkgJSA0KSBmb3IgaSBpbiByYW5nZSg2MCldXG50ZXN0X2xvc3NlcyAgPSBbKDIuMCwgXHUwMDI3bm9ybWFsXHUwMDI3KSwgKDIuMywgXHUwMDI3ZWxldmF0ZWRcdTAwMjcpLCAoNy44LCBcdTAwMjdTUElLRVx1MDAyNyksICgyLjA1LCBcdTAwMjdwb3N0LXNwaWtlXHUwMDI3KV1cbmZvciB2YWwsIGxhYmVsIGluIHRlc3RfbG9zc2VzOlxuICAgIGlzX3NwaWtlID0gZGV0ZWN0X3NwaWtlKGxvc3NfaGlzdG9yeSwgdmFsLCB0aHJlc2hvbGQ9My4wKVxuICAgIGFjdGlvbiAgID0gXHUwMDI3Uk9MTEJBQ0sgKyByZWR1Y2UgTFJcdTAwMjcgaWYgaXNfc3Bpa2UgZWxzZSBcdTAwMjdjb250aW51ZVx1MDAyN1xuICAgIHByaW50KGZcIntsYWJlbDoxMnN9OiBsb3NzPXt2YWw6LjJmfSAgc3Bpa2U9e2lzX3NwaWtlfSAgYWN0aW9uPXthY3Rpb259XCIpXG4gICAgaWYgbm90IGlzX3NwaWtlOlxuICAgICAgICBsb3NzX2hpc3RvcnkuYXBwZW5kKHZhbCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyBNZXRyaWNzIExvZ2dpbmcifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGNzdiwgb3MsIHRpbWVcbmltcG9ydCB0b3JjaFxuXG5kZWYgbG9nX21ldHJpY3Moc3RlcCwgbG9zcywgbHIsIGdyYWRfbm9ybSwgbG9nX2ZpbGU9XHUwMDI3dHJhaW5pbmdfbG9nLmNzdlx1MDAyNywgdXNlX3dhbmRiPUZhbHNlKTpcbiAgICBcIlwiXCJMb2cgc3RlcCBtZXRyaWNzIHRvIENTViBhbmQgb3B0aW9uYWxseSB0byBXXHUwMDI2Qi5cIlwiXCJcbiAgICBwcGwgPSBtaW4oMiAqKiBsb3NzLCAxZTkpIGlmIGxvc3MgXHUwMDNjIDMwIGVsc2UgZmxvYXQoXHUwMDI3aW5mXHUwMDI3KVxuICAgIHJvdyA9IHtcbiAgICAgICAgXHUwMDI3c3RlcFx1MDAyNzogICAgICAgc3RlcCxcbiAgICAgICAgXHUwMDI3bG9zc1x1MDAyNzogICAgICAgcm91bmQobG9zcywgNCksXG4gICAgICAgIFx1MDAyN3BlcnBsZXhpdHlcdTAwMjc6IHJvdW5kKHBwbCwgMiksXG4gICAgICAgIFx1MDAyN2xyXHUwMDI3OiAgICAgICAgIGZcdTAwMjd7bHI6LjJlfVx1MDAyNyxcbiAgICAgICAgXHUwMDI3Z3JhZF9ub3JtXHUwMDI3OiAgcm91bmQoZ3JhZF9ub3JtLCA0KSxcbiAgICAgICAgXHUwMDI3Z3B1X21lbV9nYlx1MDAyNzogcm91bmQodG9yY2guY3VkYS5tZW1vcnlfYWxsb2NhdGVkKCkgLyAxZTkgaWYgdG9yY2guY3VkYS5pc19hdmFpbGFibGUoKSBlbHNlIDAuMCwgMiksXG4gICAgICAgIFx1MDAyN3RpbWVzdGFtcFx1MDAyNzogIHRpbWUuc3RyZnRpbWUoXHUwMDI3JUg6JU06JVNcdTAwMjcpLFxuICAgIH1cbiAgICB3cml0ZV9oZWFkZXIgPSBub3Qgb3MucGF0aC5leGlzdHMobG9nX2ZpbGUpXG4gICAgd2l0aCBvcGVuKGxvZ19maWxlLCBcdTAwMjdhXHUwMDI3LCBuZXdsaW5lPVx1MDAyN1x1MDAyNykgYXMgZjpcbiAgICAgICAgdyA9IGNzdi5EaWN0V3JpdGVyKGYsIGZpZWxkbmFtZXM9cm93LmtleXMoKSlcbiAgICAgICAgaWYgd3JpdGVfaGVhZGVyOlxuICAgICAgICAgICAgdy53cml0ZWhlYWRlcigpXG4gICAgICAgIHcud3JpdGVyb3cocm93KVxuICAgIGlmIHVzZV93YW5kYjpcbiAgICAgICAgaW1wb3J0IHdhbmRiXG4gICAgICAgIHdhbmRiLmxvZyh7azogdiBmb3IgaywgdiBpbiByb3cuaXRlbXMoKSBpZiBrICE9IFx1MDAyN3RpbWVzdGFtcFx1MDAyN30sIHN0ZXA9c3RlcClcbiAgICByZXR1cm4gcm93XG5cbiMgU2ltdWxhdGUgNSBzdGVwc1xuZm9yIHMgaW4gcmFuZ2UoNSk6XG4gICAgbSA9IGxvZ19tZXRyaWNzKHMgKiA1MDAsIGxvc3M9Mi41IC0gcyAqIDAuMDcsIGxyPTNlLTQgKiAoMSAtIHMgKiAwLjAxNSksXG4gICAgICAgICAgICAgICAgICAgIGdyYWRfbm9ybT0wLjcyICsgcyAqIDAuMDQsIGxvZ19maWxlPVx1MDAyN3RyYWluaW5nX21ldHJpY3MuY3N2XHUwMDI3KVxuICAgIHByaW50KGZcIlN0ZXAge21bXHUwMDI3c3RlcFx1MDAyN119OiBsb3NzPXttW1x1MDAyN2xvc3NcdTAwMjddfSAgcHBsPXttW1x1MDAyN3BlcnBsZXhpdHlcdTAwMjddfSAgZ25vcm09e21bXHUwMDI3Z3JhZF9ub3JtXHUwMDI3XX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIZWFsdGh5IHZzIFBhdGhvbG9naWNhbCBUcmFpbmluZyBTaWduYWxzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldHJpYyIsIkhlYWx0aHkgUmFuZ2UiLCJXYXJuaW5nIFNpZ24iLCJMaWtlbHkgQ2F1c2UiLCJSZXNwb25zZSBBY3Rpb24iXSwicm93cyI6W1siVHJhaW5pbmcgbG9zcyIsIlNtb290aCBtb25vdG9uaWMgZGVjcmVhc2UiLCJTcGlrZSBcdTAwM2Uzw5cgcm9sbGluZyBhdmciLCJCYWQgYmF0Y2ggLyBMUiB0b28gaGlnaCIsIlJvbGxiYWNrIGNoZWNrcG9pbnQsIHJlZHVjZSBMUiAzMCUiXSxbIkdyYWRpZW50IG5vcm0g4oCWZ+KAliIsIjAuMSDigJMgMS41IHBlciBzdGVwIiwiU3VzdGFpbmVkIFx1MDAzZTUuMCBvciBOYU4iLCJFeHBsb2RpbmcgZ3JhZGllbnRzIC8gZGF0YSBhbm9tYWx5IiwiUmVkdWNlIExSLCBjaGVjayBkYXRhIHBpcGVsaW5lIl0sWyJQZXJwbGV4aXR5IiwiQ29uc2lzdGVudCBkZWNyZWFzZSIsIlBsYXRlYXUgZm9yIFx1MDAzZTEwSyBzdGVwcyIsIkxSIHRvbyBsb3cgb3IgZGF0YSBzYXR1cmF0aW9uIiwiQ2hlY2sgc2NoZWR1bGUsIHJlc2h1ZmZsZSBkYXRhIl0sWyJMUiAoYWN0dWFsIHZzIHNjaGVkdWxlZCkiLCJGb2xsb3dzIHNjaGVkdWxlIGV4YWN0bHkiLCJEcmlmdCBvciB6ZXJvIGFmdGVyIHJlc3VtZSIsIk9wdGltaXplciBzdGF0ZSBub3QgcmVzdG9yZWQiLCJWZXJpZnkgY2hlY2twb2ludCBsb2FkICsgc3RlcCBjb3VudGVyIl0sWyJHUFUgbWVtb3J5IChHQikiLCJTdGFibGUgYWNyb3NzIHN0ZXBzIiwiTW9ub3RvbmljIGdyb3d0aCAvIE9PTSIsIkFjdGl2YXRpb24gbWVtb3J5IGxlYWsiLCJHcmFkaWVudCBjaGVja3BvaW50aW5nLCByZWR1Y2UgYmF0Y2giXSxbIkxvc3Mgc3Bpa2UgZnJlcXVlbmN5IiwiXHUwMDNjMSBwZXIgNUsgc3RlcHMiLCJcdTAwM2UzIHNwaWtlcyBwZXIgMUsgc3RlcHMiLCJEYXRhIHF1YWxpdHkgaXNzdWVzIiwiRmlsdGVyIG1hbGZvcm1lZCBkb2NzLCBjYXAgZG9jIGxlbmd0aCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiYmYxNiB2cyBmcDE2IGFuZCBDaGVja3BvaW50aW5nIFN0cmF0ZWd5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJiZjE2IChiZmxvYXQxNikgaGFzIHRoZSBzYW1lIDgtYml0IGV4cG9uZW50IGFzIGZwMzIgYnV0IG9ubHkgNyBtYW50aXNzYSBiaXRzIHZlcnN1cyBmcDE2XHUwMDI3cyAxMC4gVGhpcyBtZWFucyBiZjE2IGhhcyBhIG11Y2ggd2lkZXIgZHluYW1pYyByYW5nZSAoc2FtZSBhcyBmcDMyOiDCsTMuNMOXMTDCs+KBuCkgYnV0IGxvd2VyIHByZWNpc2lvbiBmb3Igc21hbGwgdmFsdWVzLiBJbiBwcmFjdGljZSwgYmYxNiB0cmFpbmluZyBzdWZmZXJzIGZhciBmZXdlciBncmFkaWVudCBvdmVyZmxvdyBldmVudHMgdGhhbiBmcDE2IGJlY2F1c2UgYWN0aXZhdGlvbiBhbmQgZ3JhZGllbnQgbWFnbml0dWRlcyBjYW4gc3BhbiBtYW55IG9yZGVycyBvZiBtYWduaXR1ZGUgZHVyaW5nIGEgc3Bpa2UuIGZwMTYgdHJhaW5pbmcgcmVxdWlyZXMgbG9zcyBzY2FsaW5nIHRvIGF2b2lkIHVuZGVyZmxvdzsgYmYxNiBkb2VzIG5vdC4gRm9yIGNoZWNrcG9pbnRpbmcsIHNhdmUgb3B0aW1pemVyIHN0YXRlIChBZGFtIG0gYW5kIHYgZm9yIGV2ZXJ5IHBhcmFtZXRlciksIG1vZGVsIHdlaWdodHMsIHRoZSByYW5kb20gc3RhdGUgZm9yIGRhdGEgc2FtcGxpbmcsIGFuZCB0aGUgc2NoZWR1bGVyIHN0ZXAuIE1pc3NpbmcgYW55IG9mIHRoZXNlIGNhdXNlcyBzaWxlbnQgZGl2ZXJnZW5jZSBvbiByZXN1bWUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTYXZlIGV2ZXJ5IDEwMDAgc3RlcHMgbWluaW11bTsgZXZlcnkgNTAwIHN0ZXBzIGlmIHRyYWluaW5nIGlzIHVuc3RhYmxlIG9yIGV4cGVuc2l2ZSIsIkNoZWNrcG9pbnQgaW5jbHVkZXM6IG1vZGVsIHdlaWdodHMsIG9wdGltaXplciBzdGF0ZSAobSwgdiksIHNjaGVkdWxlciBzdGVwLCBSTkcgc2VlZHMiLCJVc2UgbWl4ZWQgcHJlY2lzaW9uOiB3ZWlnaHRzIGluIGZwMzIsIGZvcndhcmQvYmFja3dhcmQgaW4gYmYxNiAoQU1QIHdpdGggYmYxNikiLCJLZWVwIHRoZSBsYXN0IDPigJM1IGNoZWNrcG9pbnRzIHRvIGFsbG93IHJvbGxiYWNrIHBhc3QgbXVsdGlwbGUgY29uc2VjdXRpdmUgc3Bpa2VzIiwiVmFsaWRhdGUgY2hlY2twb2ludCBpbnRlZ3JpdHkgYWZ0ZXIgc2F2aW5nOiBsb2FkIGFuZCBjaGVjayBsb3NzIG9uIGEgZml4ZWQgdmFsaWRhdGlvbiBiYXRjaCJdfV0="
---
# LLM Training Dynamics — Warmup, Loss Spikes, and Gradient Norm Monitoring

Training large language models at scale surfaces a class of instability problems that do not appear at smaller scales: loss spikes that can derail a run after thousands of GPU-hours, gradient explosions that corrupt model weights, and scheduling bugs that cause silent underfitting. Understanding the interplay between the learning rate schedule, the Adam optimizer's moment estimates, and gradient norm dynamics is essential for anyone running or debugging LLM pretraining. This note covers the four most important levers: warmup, cosine annealing, gradient norm monitoring, and checkpoint rollback.

## Learning Rate Warmup and the Adam Bias Problem

At step 0, Adam's first-moment estimate m₀ = 0 and second-moment estimate v₀ = 0. The bias correction factors 1/(1 − β₁ᵗ) and 1/(1 − β₂ᵗ) partially compensate for this cold-start, but in practice the effective per-parameter step sizes are poorly calibrated for the first few hundred steps. Starting at the full target learning rate during this period causes large, noisy gradient updates that move parameters far from their initialization. Linear warmup from 0 to η_max over the first ~2000 steps allows the moment estimates to stabilize before the optimizer operates at full learning rate, dramatically reducing early-training divergence risk.

- Linear warmup: LR(t) = η_max × t / T_warmup for t < T_warmup, typically T_warmup = 2000 steps
- β₂ = 0.95–0.999 in large LLMs; higher β₂ means longer moment warm-up period
- Skipping warmup with Adam at LR=3e-4 on a Transformer often causes divergence in first 100 steps
- GPT-3 used T_warmup = 375M tokens; LLaMA used T_warmup ≈ 2000 steps at batch 4M tokens
- bf16 training is more sensitive to early LR spikes than fp32 due to reduced precision range

## Cosine Annealing After Warmup

After warmup, the standard schedule for LLM pretraining is cosine annealing: LR(t) = η_min + (η_max − η_min) × cos(π × t / T) / 2, where T is the total training steps and η_min is a floor (typically 1e-5 or 10% of η_max). Cosine decay is preferred over step decay because it provides a smooth, continuous reduction that avoids sudden LR drops which can destabilize Adam's momentum estimates. The final 10% of training at near-zero LR often recovers 0.3–0.5 perplexity points compared to stopping cosine decay early.

```python
import math
import matplotlib.pyplot as plt

def get_lr(step, warmup_steps, total_steps, lr_max, lr_min=1e-5):
    """Linear warmup then cosine annealing to lr_min."""
    if step < warmup_steps:
        return lr_max * step / max(warmup_steps, 1)
    progress = (step - warmup_steps) / max(total_steps - warmup_steps, 1)
    return lr_min + 0.5 * (lr_max - lr_min) * (1 + math.cos(math.pi * progress))

warmup_steps, total_steps = 2000, 100_000
lr_max, lr_min = 3e-4, 1e-5

steps = list(range(0, total_steps, 200))
lrs   = [get_lr(s, warmup_steps, total_steps, lr_max, lr_min) for s in steps]

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(steps, lrs, 'b-', linewidth=2, label='LR schedule')
ax.axvline(warmup_steps, color='orange', linestyle='--', label=f'Warmup end ({warmup_steps} steps)')
ax.set_xlabel('Training Step'); ax.set_ylabel('Learning Rate')
ax.set_title('LR: Linear Warmup + Cosine Annealing (eta_min=1e-5)')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('lr_schedule.png', dpi=120)
print(f"Peak LR: {max(lrs):.2e}  End LR: {lrs[-1]:.2e}  Warmup: {warmup_steps/total_steps:.1%} of training")
```

## Loss Spikes — Causes and Detection

A loss spike is a sudden sharp increase in training loss — typically 2–10× baseline — followed by gradual recovery over 100–500 steps. Spikes are the most common cause of catastrophic LLM pretraining failures. Most spikes self-heal if the LR is not too high; in severe cases the model never recovers and the run must be restarted from a checkpoint. The primary causes are data-related: malformed Unicode sequences cause tokenizer output anomalies; repeated tokens pad documents to extreme lengths; empty or near-empty documents produce undefined loss values. Hardware faults (NaN-producing FP operations) and LR schedule bugs are secondary causes.

- Data anomalies: malformed Unicode, encoding errors, empty documents, repeated-token padding
- LR too high: gradient step overhoots loss minimum, causes chaotic wandering
- Bad batch: single extremely high-loss document (corrupted label or length outlier)
- Gradient overflow: fp16/bf16 gradients saturate; NaN propagates into weights via Adam update
- Architecture bug: attention logit explosion in deep models with incorrect initialization

> **Warning**: Loss spikes from data quality issues (malformed Unicode, empty documents, repeated tokens) are the most common cause of LLM training instability — aggressive data filtering and document length capping prevent most spikes.

## Gradient Norm Monitoring and Clipping

The global gradient norm ‖∇L‖₂ = sqrt(Σᵢ ‖∇Lᵢ‖²) computed across all parameters is one of the most informative training diagnostics. A healthy LLM run shows gradient norms in the range 0.1–2.0. Sustained norms above 5.0 indicate instability that usually precedes a loss spike by 50–200 steps. Global norm clipping rescales the entire gradient vector when ‖g‖ > clip_norm: g ← g × (clip_norm / ‖g‖). This prevents any single large gradient from driving a destructive parameter update without reducing smaller gradients. Standard clip_norm = 1.0 for most LLM training; some recipes use 0.5 for very deep models.

```python
import torch
import torch.nn as nn

def compute_global_grad_norm(model):
    """Compute global L2 gradient norm across all parameters."""
    total_norm = 0.0
    for p in model.parameters():
        if p.grad is not None:
            total_norm += p.grad.detach().norm(2).item() ** 2
    return total_norm ** 0.5

def train_step_with_clip(model, optimizer, loss, clip_norm=1.0):
    optimizer.zero_grad()
    loss.backward()
    pre_clip_norm = compute_global_grad_norm(model)
    if pre_clip_norm > clip_norm:
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip_norm)
    optimizer.step()
    return pre_clip_norm, pre_clip_norm > clip_norm

# Simulate 10 training steps and log gradient norms
model     = nn.Sequential(nn.Linear(128, 256), nn.GELU(), nn.Linear(256, 128))
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, betas=(0.9, 0.95))
norm_log  = []
for step in range(10):
    x         = torch.randn(16, 128)
    loss      = (model(x) ** 2).mean() + 0.01 * torch.randn(1).abs()
    gnorm, clipped = train_step_with_clip(model, optimizer, loss, clip_norm=1.0)
    norm_log.append(gnorm)
    status = 'CLIPPED' if clipped else 'ok'
    print(f"Step {step:2d}: grad_norm={gnorm:.4f}  [{status}]")
print(f"Mean norm: {sum(norm_log)/len(norm_log):.4f}  Max: {max(norm_log):.4f}")
```

## Spike Detection and Checkpoint Rollback

Automated spike detection compares the current loss to a rolling baseline computed over the last 50 steps. If the current loss exceeds the baseline by more than a threshold (typically 3×), the training loop triggers a rollback: load the most recent good checkpoint, reduce the learning rate by 20–50%, and resume training. Most training frameworks save checkpoints every 500–1000 steps; saving more frequently is expensive but allows finer-grained recovery. The key insight is that spike recovery is much faster when the checkpoint is close to the spike — resuming from step N-100 with reduced LR typically recovers in 200–500 steps.

```python
import torch
import os

def detect_spike(loss_history, current_loss, threshold=3.0, window=50):
    """Return True if current_loss is threshold× above recent baseline."""
    if len(loss_history) < window:
        return False
    baseline = sum(loss_history[-window:]) / window
    return current_loss > baseline * threshold

def load_last_checkpoint(ckpt_dir, model, optimizer):
    """Load the most recent .pt checkpoint and return the step number."""
    ckpts = sorted([f for f in os.listdir(ckpt_dir) if f.endswith('.pt')])
    if not ckpts:
        print("No checkpoints found.")
        return 0
    path = os.path.join(ckpt_dir, ckpts[-1])
    ckpt = torch.load(path, map_location='cpu')
    model.load_state_dict(ckpt['model'])
    optimizer.load_state_dict(ckpt['optimizer'])
    print(f"Rolled back to step {ckpt['step']} (loss={ckpt['loss']:.4f})")
    return ckpt['step']

# Simulate spike detection over 65 steps
loss_history = [2.1 + 0.04 * (i % 4) for i in range(60)]
test_losses  = [(2.0, 'normal'), (2.3, 'elevated'), (7.8, 'SPIKE'), (2.05, 'post-spike')]
for val, label in test_losses:
    is_spike = detect_spike(loss_history, val, threshold=3.0)
    action   = 'ROLLBACK + reduce LR' if is_spike else 'continue'
    print(f"{label:12s}: loss={val:.2f}  spike={is_spike}  action={action}")
    if not is_spike:
        loss_history.append(val)
```

## Training Metrics Logging

```python
import csv, os, time
import torch

def log_metrics(step, loss, lr, grad_norm, log_file='training_log.csv', use_wandb=False):
    """Log step metrics to CSV and optionally to W&B."""
    ppl = min(2 ** loss, 1e9) if loss < 30 else float('inf')
    row = {
        'step':       step,
        'loss':       round(loss, 4),
        'perplexity': round(ppl, 2),
        'lr':         f'{lr:.2e}',
        'grad_norm':  round(grad_norm, 4),
        'gpu_mem_gb': round(torch.cuda.memory_allocated() / 1e9 if torch.cuda.is_available() else 0.0, 2),
        'timestamp':  time.strftime('%H:%M:%S'),
    }
    write_header = not os.path.exists(log_file)
    with open(log_file, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=row.keys())
        if write_header:
            w.writeheader()
        w.writerow(row)
    if use_wandb:
        import wandb
        wandb.log({k: v for k, v in row.items() if k != 'timestamp'}, step=step)
    return row

# Simulate 5 steps
for s in range(5):
    m = log_metrics(s * 500, loss=2.5 - s * 0.07, lr=3e-4 * (1 - s * 0.015),
                    grad_norm=0.72 + s * 0.04, log_file='training_metrics.csv')
    print(f"Step {m['step']}: loss={m['loss']}  ppl={m['perplexity']}  gnorm={m['grad_norm']}")
```

## Healthy vs Pathological Training Signals

| Metric | Healthy Range | Warning Sign | Likely Cause | Response Action |
| --- | --- | --- | --- | --- |
| Training loss | Smooth monotonic decrease | Spike >3× rolling avg | Bad batch / LR too high | Rollback checkpoint, reduce LR 30% |
| Gradient norm ‖g‖ | 0.1 – 1.5 per step | Sustained >5.0 or NaN | Exploding gradients / data anomaly | Reduce LR, check data pipeline |
| Perplexity | Consistent decrease | Plateau for >10K steps | LR too low or data saturation | Check schedule, reshuffle data |
| LR (actual vs scheduled) | Follows schedule exactly | Drift or zero after resume | Optimizer state not restored | Verify checkpoint load + step counter |
| GPU memory (GB) | Stable across steps | Monotonic growth / OOM | Activation memory leak | Gradient checkpointing, reduce batch |
| Loss spike frequency | <1 per 5K steps | >3 spikes per 1K steps | Data quality issues | Filter malformed docs, cap doc length |

## bf16 vs fp16 and Checkpointing Strategy

bf16 (bfloat16) has the same 8-bit exponent as fp32 but only 7 mantissa bits versus fp16's 10. This means bf16 has a much wider dynamic range (same as fp32: ±3.4×10³⁸) but lower precision for small values. In practice, bf16 training suffers far fewer gradient overflow events than fp16 because activation and gradient magnitudes can span many orders of magnitude during a spike. fp16 training requires loss scaling to avoid underflow; bf16 does not. For checkpointing, save optimizer state (Adam m and v for every parameter), model weights, the random state for data sampling, and the scheduler step. Missing any of these causes silent divergence on resume.

- Save every 1000 steps minimum; every 500 steps if training is unstable or expensive
- Checkpoint includes: model weights, optimizer state (m, v), scheduler step, RNG seeds
- Use mixed precision: weights in fp32, forward/backward in bf16 (AMP with bf16)
- Keep the last 3–5 checkpoints to allow rollback past multiple consecutive spikes
- Validate checkpoint integrity after saving: load and check loss on a fixed validation batch

