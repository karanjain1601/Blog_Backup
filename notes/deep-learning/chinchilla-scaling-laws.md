---
title: "Chinchilla Scaling Laws — Compute-Optimal Token-to-Parameter Ratios"
slug: "chinchilla-scaling-laws"
description: "Hoffmann et al. (2022, DeepMind): by sweeping (N, D) at fixed compute, the true optimal D/N ratio is ~20 tokens per parameter — not ~1 as Kaplan suggested — showing GPT-3, Gopher, and most pre-2022 LLMs were severely undertrained on data."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gMjAyMiwgSG9mZm1hbm4gZXQgYWwuIGF0IERlZXBNaW5kIHB1Ymxpc2hlZCB0aGUgQ2hpbmNoaWxsYSBwYXBlciwgb3ZlcnR1cm5pbmcgdGhlIHByZXZhaWxpbmcgS2FwbGFuLWRlcml2ZWQgd2lzZG9tIHRoYXQgbW9kZWwgc2l6ZSBzaG91bGQgc2NhbGUgZmFzdGVyIHRoYW4gZGF0YS4gQnkgdHJhaW5pbmcgb3ZlciA0MDAgbW9kZWxzIHJhbmdpbmcgZnJvbSA3ME0gdG8gMTZCIHBhcmFtZXRlcnMgb24gNUIgdG8gNTAwQiB0b2tlbnMsIHRoZXkgaWRlbnRpZmllZCB0aGUgdHJ1ZSBjb21wdXRlLW9wdGltYWwgYWxsb2NhdGlvbjogZm9yIGEgZml4ZWQgY29tcHV0ZSBidWRnZXQgQywgYm90aCBtb2RlbCBzaXplIE4qIGFuZCB0b2tlbiBjb3VudCBEKiBzaG91bGQgc2NhbGUgZXF1YWxseSDigJQgcHJvcG9ydGlvbmFsIHRvIENeMC41IGVhY2guIFRoZSBrZXkgcmVzdWx0OiBEL04gYXBwcm94aW1hdGVseSAyMCB0b2tlbnMgcGVyIHBhcmFtZXRlciBhdCB0aGUgb3B0aW1hbCBwb2ludCwgbm90IDEgYXMgS2FwbGFuIHByZWRpY3RlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgQ29tcHV0ZS1PcHRpbWFsIEluc2lnaHQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNoaW5jaGlsbGEgKDcwQiBwYXJhbWV0ZXJzLCAxLjRUIHRyYWluaW5nIHRva2Vucykgb3V0cGVyZm9ybWVkIEdvcGhlciAoMjgwQiBwYXJhbWV0ZXJzLCAzMDBCIHRva2VucykgYXQgdGhlIHNhbWUgY29tcHV0ZSBidWRnZXQsIGRlbW9uc3RyYXRpbmcgdGhhdCBkYXRhIHF1YW50aXR5IG1hdHRlcnMgYXMgbXVjaCBhcyBtb2RlbCBzaXplLiBHUFQtMyAoMTc1QiBwYXJhbWV0ZXJzLCAzMDBCIHRva2Vucykgd2FzIHVuZGVydHJhaW5lZCBieSBhcHByb3hpbWF0ZWx5IDEweCBvbiBkYXRhIHJlbGF0aXZlIHRvIGl0cyBwYXJhbWV0ZXIgY291bnQuIFRoZSBqb2ludCBsb3NzIGZvcm11bGEgTChOLCBEKSA9IEUgKyBBL05eYWxwaGEgKyBCL0ReYmV0YSB3YXMgZml0dGVkIHdpdGggRT0xLjY5LCBBPTQwNi40LCBhbHBoYT0wLjM0LCBCPTQxMC43LCBiZXRhPTAuMjgsIGVuYWJsaW5nIHByZWNpc2Ugb3B0aW1pemF0aW9uIG9mIHRoZSBOLUQgdHJhZGUtb2ZmIGF0IGFueSBjb21wdXRlIGxldmVsLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiT3B0aW1hbCBEL04gPSAyMDogdHJhaW4gb24gMjAgdG9rZW5zIHBlciBwYXJhbWV0ZXIgYXQgY29tcHV0ZS1vcHRpbWFsIGFsbG9jYXRpb24iLCJOKiBwcm9wb3J0aW9uYWwgdG8gQ14wLjUgYW5kIEQqIHByb3BvcnRpb25hbCB0byBDXjAuNTogZXF1YWwgc2NhbGluZyBvZiBtb2RlbCBhbmQgZGF0YSIsIkNoaW5jaGlsbGEgKDcwQiwgMS40VCkgYmVhdHMgR29waGVyICgyODBCLCAzMDBCKSBhdCBzYW1lIGNvbXB1dGUg4oCUIDR4IHNtYWxsZXIgbW9kZWwsIDV4IG1vcmUgZGF0YSIsIkdQVC0zICgxNzVCLCAzMDBCIHRva2Vucyk6IEQvTiA9IDEuNywgYXBwcm94aW1hdGVseSAxMHggdW5kZXItdHJhaW5lZCBvbiBkYXRhIiwiQyA9IDYqTipEIGFwcHJveGltYXRpb246IDYgbXVsdGlwbHktYWRkcyBwZXIgcGFyYW1ldGVyIHBlciB0b2tlbiAoMiBmb3J3YXJkICsgNCBiYWNrd2FyZCkiLCJMTGFNQS0xICg3QiwgMVQgdG9rZW5zKTogRC9OID0gMTQzLCBhcHByb3hpbWF0ZWx5IDd4IG92ZXItdHJhaW5lZCDigJQgaW5mZXJlbmNlLW9wdGltaXplZCJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIENoaW5jaGlsbGEgTG9zcyBGb3JtdWxhIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG4jIENoaW5jaGlsbGEgZml0dGVkIGNvbnN0YW50cyAoSG9mZm1hbm4gZXQgYWwuLCAyMDIyLCBUYWJsZSAzKVxuRV9DT05TVCA9IDEuNjkgICAgIyBpcnJlZHVjaWJsZSBsb3NzOiBlbnRyb3B5IGZsb29yIG9mIG5hdHVyYWwgbGFuZ3VhZ2VcbkFfQ09OU1QgPSA0MDYuNCAgICMgcGFyYW1ldGVyIHNjYWxpbmcgY29lZmZpY2llbnRcbkJfQ09OU1QgPSA0MTAuNyAgICMgZGF0YSBzY2FsaW5nIGNvZWZmaWNpZW50XG5BTFBIQSAgID0gMC4zNCAgICAjIHBhcmFtZXRlciBzY2FsaW5nIGV4cG9uZW50XG5CRVRBICAgID0gMC4yOCAgICAjIGRhdGEgc2NhbGluZyBleHBvbmVudFxuXG5kZWYgY2hpbmNoaWxsYV9sb3NzKE4sIEQpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0woTiwgRCkgPSBFICsgQS9OXmFscGhhICsgQi9EXmJldGFcdTAwMjdcdTAwMjdcdTAwMjdcbiAgICByZXR1cm4gRV9DT05TVCArIEFfQ09OU1QgKiBOICoqICgtQUxQSEEpICsgQl9DT05TVCAqIEQgKiogKC1CRVRBKVxuXG4jIEZpeCBjb21wdXRlIEMsIHN3ZWVwIE4gd2hpbGUgRCA9IEMgLyAoNipOKVxuQ19maXhlZCA9IDZlMjEgICAjIH4zMEIgbW9kZWwtc2NhbGUgY29tcHV0ZSBidWRnZXRcbk5fcmFuZ2UgPSBucC5sb2dzcGFjZSg4LCAxMiwgMzAwKSAgIyAxMDBNIHRvIDFUIHBhcmFtZXRlcnNcbkRfcmFuZ2UgPSBDX2ZpeGVkIC8gKDYuMCAqIE5fcmFuZ2UpXG5cbkxfcmFuZ2UgID0gY2hpbmNoaWxsYV9sb3NzKE5fcmFuZ2UsIERfcmFuZ2UpXG5iZXN0X2lkeCA9IG5wLmFyZ21pbihMX3JhbmdlKVxuTl9vcHQsIERfb3B0LCBMX21pbiA9IE5fcmFuZ2VbYmVzdF9pZHhdLCBEX3JhbmdlW2Jlc3RfaWR4XSwgTF9yYW5nZVtiZXN0X2lkeF1cbnByaW50KFx1MDAyN0NvbXB1dGUgYnVkZ2V0OiB7Oi4xZX0gRkxPUHNcdTAwMjcuZm9ybWF0KENfZml4ZWQpKVxucHJpbnQoXHUwMDI3T3B0aW1hbCBOKjogezouMmZ9QiBwYXJhbXMgfCBEKjogezouMmZ9QiB0b2tlbnMgfCBEL046IHs6LjFmfSB8IExfbWluOiB7Oi40Zn1cdTAwMjcuZm9ybWF0KFxuICAgIE5fb3B0LzFlOSwgRF9vcHQvMWU5LCBEX29wdC9OX29wdCwgTF9taW4pKVxuXG5wbHQuZmlndXJlKGZpZ3NpemU9KDksIDUpKVxucGx0LnNlbWlsb2d4KE5fcmFuZ2UgLyAxZTksIExfcmFuZ2UsIFx1MDAyN2ItXHUwMDI3LCBsdz0yLCBsYWJlbD1cdTAwMjdMKE4sIEQpIGF0IGZpeGVkIENcdTAwMjcpXG5wbHQuYXh2bGluZShOX29wdCAvIDFlOSwgY29sb3I9XHUwMDI3clx1MDAyNywgbHM9XHUwMDI3LS1cdTAwMjcsIGx3PTIsIGxhYmVsPVx1MDAyN09wdGltYWwgTiogPSB7Oi4xZn1CXHUwMDI3LmZvcm1hdChOX29wdC8xZTkpKVxucGx0LnhsYWJlbChcdTAwMjdNb2RlbCBTaXplIE4gKGJpbGxpb25zIG9mIHBhcmFtZXRlcnMpXHUwMDI3LCBmb250c2l6ZT0xMilcbnBsdC55bGFiZWwoXHUwMDI3UHJlZGljdGVkIExvc3MgTChOLCBEKVx1MDAyNywgZm9udHNpemU9MTIpXG5wbHQudGl0bGUoXHUwMDI3Q2hpbmNoaWxsYSBMb3NzIHZzIE4gZm9yIEZpeGVkIENvbXB1dGUgQyA9IHs6LjFlfSBGTE9Qc1x1MDAyNy5mb3JtYXQoQ19maXhlZCksIGZvbnRzaXplPTEyKVxucGx0LmxlZ2VuZChmb250c2l6ZT0xMSlcbnBsdC5ncmlkKFRydWUsIGFscGhhPTAuMylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3Y2hpbmNoaWxsYV9sb3NzX2N1cnZlLnBuZ1x1MDAyNywgZHBpPTE1MClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPcHRpbWFsIFRva2VuLXRvLVBhcmFtZXRlciBSYXRpbyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIDIwOjEgdG9rZW4tdG8tcGFyYW1ldGVyIHJhdGlvIGVtZXJnZXMgZnJvbSB0aGUgc3ltbWV0cnkgb2YgdGhlIENoaW5jaGlsbGEgbG9zcyBmb3JtdWxhIHdoZW4gYm90aCBhbHBoYSBhbmQgYmV0YSBhcmUgc2ltaWxhciAoMC4zNCB2cyAwLjI4KS4gVGhlIG9wdGltYWwgYWxsb2NhdGlvbiBtaW5pbWl6ZXMgTChOLCBEKSA9IEUgKyBBL05eYWxwaGEgKyBCL0ReYmV0YSBzdWJqZWN0IHRvIEMgPSA2TkQuIFRha2luZyBwYXJ0aWFsIGRlcml2YXRpdmVzIGFuZCBzZXR0aW5nIHRoZW0gZXF1YWwgZ2l2ZXMgdGhlIGNvbmRpdGlvbiBBKmFscGhhL05eKGFscGhhKzEpID0gQipiZXRhL0ReKGJldGErMSksIHdoaWNoIHdpdGggYWxwaGEgYXBwcm94aW1hdGVseSBiZXRhIGxlYWRzIHRvIEEvTl5hbHBoYSBhcHByb3hpbWF0ZWx5IEIvRF5iZXRhIOKAlCByb3VnaGx5IGVxdWFsIGNvbnRyaWJ1dGlvbnMgZnJvbSBlYWNoIHRlcm0uIFNpbmNlIEEgYW5kIEIgYXJlIG5lYXJseSBlcXVhbCAoNDA2LjQgdnMgNDEwLjcpLCBhbmQgYWxwaGEgYW5kIGJldGEgYXJlIGNsb3NlLCB0aGUgb3B0aW1hbCBOIGFuZCBEIGVuZCB1cCByb3VnaGx5IGVxdWFsIGluIHRoZWlyIGNvbnRyaWJ1dGlvbiwgeWllbGRpbmcgRC9OID0gMjAgYXMgdGhlIGVtcGlyaWNhbCByYXRpby4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDIg4oCUIENvbXB1dGUtT3B0aW1hbCBGcm9udGllciJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIGNoaW5jaGlsbGFfb3B0aW1hbChDKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdDaGluY2hpbGxhOiBlcXVhbCBzY2FsaW5nLCBEKiA9IDIwKk4qLCBDID0gNipOKkQqID0gMTIwKk4qXjIuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgTl9zdGFyID0gbnAuc3FydChDIC8gMTIwLjApXG4gICAgRF9zdGFyID0gMjAuMCAqIE5fc3RhclxuICAgIHJldHVybiBOX3N0YXIsIERfc3RhclxuXG5kZWYga2FwbGFuX29wdGltYWwoQywga19OPTEuM2UtNSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3S2FwbGFuOiBOIHNjYWxlcyBmYXN0ZXIgdGhhbiBEIChOKiBwcm9wb3J0aW9uYWwgdG8gQ14wLjczKS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBOX3N0YXIgPSBrX04gKiAoQyAqKiAwLjczKVxuICAgIERfc3RhciA9IEMgLyAoNi4wICogTl9zdGFyKVxuICAgIHJldHVybiBOX3N0YXIsIERfc3RhclxuXG5DX3JhbmdlID0gbnAubG9nc3BhY2UoMTgsIDI0LCAxNTApXG5jaF9OLCBjaF9EID0gY2hpbmNoaWxsYV9vcHRpbWFsKENfcmFuZ2UpXG5rcF9OLCBrcF9EID0ga2FwbGFuX29wdGltYWwoQ19yYW5nZSlcblxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDEsIDIsIGZpZ3NpemU9KDEzLCA1KSlcbmF4ZXNbMF0ubG9nbG9nKENfcmFuZ2UsIGNoX04vMWU5LCBcdTAwMjdiLVx1MDAyNywgIGx3PTIsIGxhYmVsPVx1MDAyN0NoaW5jaGlsbGEgTipcdTAwMjcpXG5heGVzWzBdLmxvZ2xvZyhDX3JhbmdlLCBrcF9OLzFlOSwgXHUwMDI3ci0tXHUwMDI3LCBsdz0yLCBsYWJlbD1cdTAwMjdLYXBsYW4gTipcdTAwMjcpXG5heGVzWzBdLnNldCh4bGFiZWw9XHUwMDI3Q29tcHV0ZSBDIChGTE9QcylcdTAwMjcsIHlsYWJlbD1cdTAwMjdPcHRpbWFsIE4qIChiaWxsaW9ucylcdTAwMjcsXG4gICAgICAgICAgICB0aXRsZT1cdTAwMjdPcHRpbWFsIE1vZGVsIFNpemUgdnMgQ29tcHV0ZVx1MDAyNylcbmF4ZXNbMF0ubGVnZW5kKCk7IGF4ZXNbMF0uZ3JpZChUcnVlLCBhbHBoYT0wLjMpXG5cbmF4ZXNbMV0ubG9nbG9nKENfcmFuZ2UsIGNoX0QvMWU5LCBcdTAwMjdiLVx1MDAyNywgIGx3PTIsIGxhYmVsPVx1MDAyN0NoaW5jaGlsbGEgRCpcdTAwMjcpXG5heGVzWzFdLmxvZ2xvZyhDX3JhbmdlLCBrcF9ELzFlOSwgXHUwMDI3ci0tXHUwMDI3LCBsdz0yLCBsYWJlbD1cdTAwMjdLYXBsYW4gRCpcdTAwMjcpXG5heGVzWzFdLnNldCh4bGFiZWw9XHUwMDI3Q29tcHV0ZSBDIChGTE9QcylcdTAwMjcsIHlsYWJlbD1cdTAwMjdPcHRpbWFsIEQqIChCIHRva2VucylcdTAwMjcsXG4gICAgICAgICAgICB0aXRsZT1cdTAwMjdPcHRpbWFsIFRva2VuIENvdW50IHZzIENvbXB1dGVcdTAwMjcpXG5heGVzWzFdLmxlZ2VuZCgpOyBheGVzWzFdLmdyaWQoVHJ1ZSwgYWxwaGE9MC4zKVxuXG5wbHQuc3VwdGl0bGUoXHUwMDI3S2FwbGFuIHZzIENoaW5jaGlsbGE6IENvbXB1dGUtT3B0aW1hbCBGcm9udGllclx1MDAyNywgZm9udHNpemU9MTMpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zYXZlZmlnKFx1MDAyN2NoaW5jaGlsbGFfdnNfa2FwbGFuX2Zyb250aWVyLnBuZ1x1MDAyNywgZHBpPTE1MClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyBGTE9QcyBFc3RpbWF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQyA9IDZORCBhcHByb3hpbWF0aW9uIGNvdW50cyBmb3J3YXJkIGFuZCBiYWNrd2FyZCBwYXNzZXMgdGhyb3VnaCBhIHRyYW5zZm9ybWVyLiBFYWNoIG11bHRpcGx5LWFkZCBvcGVyYXRpb24gY29udHJpYnV0ZXMgMiBGTE9QcyAob25lIG11bHRpcGx5LCBvbmUgYWRkKS4gVGhlIGZvcndhcmQgcGFzcyByZXF1aXJlcyByb3VnaGx5IDJORCBGTE9QcyAob25lIHBhc3MgdGhyb3VnaCBOIHBhcmFtZXRlcnMgZm9yIGVhY2ggb2YgRCB0b2tlbnMpLiBUaGUgYmFja3dhcmQgcGFzcyByZXF1aXJlcyByb3VnaGx5IDRORCBGTE9QcyAodHdvIHBhc3NlczogY29tcHV0aW5nIGdyYWRpZW50cyB3aXRoIHJlc3BlY3QgdG8gd2VpZ2h0cyBhbmQgd2l0aCByZXNwZWN0IHRvIGFjdGl2YXRpb25zKS4gVG90YWw6IDZORCBGTE9Qcy4gVGhpcyBhcHByb3hpbWF0aW9uIGlnbm9yZXMgYXR0ZW50aW9uIEZMT1AgY29udHJpYnV0aW9ucyAoTyhUXjIpIHBlciBsYXllciksIGVtYmVkZGluZyBsb29rdXBzLCBhbmQgbGF5ZXIgbm9ybSDigJQgdGhlc2UgYWRkIHJvdWdobHkgMTAtMjAlIG92ZXJoZWFkIGZvciB0eXBpY2FsIHNlcXVlbmNlIGxlbmd0aHMgYW5kIGFyY2hpdGVjdHVyZSBjaG9pY2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMyDigJQgVHJhaW5pbmcgRkxPUHMgRXN0aW1hdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBDID0gNiAqIE4gKiBEIGFwcHJveGltYXRpb24gKENoaW5jaGlsbGEgcGFwZXIpXG4jIEZhY3RvciBvZiA2ID0gMiAoZm9yd2FyZCBwYXNzKSArIDQgKGJhY2t3YXJkIHBhc3MpIHBlciBwYXJhbWV0ZXIgcGVyIHRva2VuXG5cbmRlZiB0cmFpbmluZ19mbG9wcyhOX3BhcmFtcywgRF90b2tlbnMpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0VzdGltYXRlIHRyYWluaW5nIEZMT1BzOiBDID0gNiAqIE4gKiBELlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIHJldHVybiA2LjAgKiBOX3BhcmFtcyAqIERfdG9rZW5zXG5cbiMgS25vd24gbW9kZWwgc3BlY3M6IChuYW1lLCBOX3BhcmFtcywgRF90b2tlbnMpXG5tb2RlbHMgPSBbXG4gICAgKFx1MDAyN0dQVC0zIDE3NUJcdTAwMjcsICAgICAgMTc1ZTksICAgMzAwZTkpLFxuICAgIChcdTAwMjdDaGluY2hpbGxhIDcwQlx1MDAyNywgICA3MGU5LCAgMTQwMGU5KSxcbiAgICAoXHUwMDI3R29waGVyIDI4MEJcdTAwMjcsICAgICAyODBlOSwgICAzMDBlOSksXG4gICAgKFx1MDAyN0xMYU1BLTEgN0JcdTAwMjcsICAgICAgICA3ZTksICAxMDAwZTkpLFxuICAgIChcdTAwMjdMTGFNQS0yIDcwQlx1MDAyNywgICAgICA3MGU5LCAgMjAwMGU5KSxcbl1cblxuY2hpbmNoaWxsYV9yYXRpbyA9IDIwLjAgICMgY29tcHV0ZS1vcHRpbWFsIEQvTlxuXG5wcmludChcdTAwMjd7Olx1MDAzYzIwfSB7Olx1MDAzZTh9IHs6XHUwMDNlMTB9IHs6XHUwMDNlOH0gezpcdTAwM2UxNX0gezpcdTAwM2UxNX1cdTAwMjcuZm9ybWF0KFxuICAgIFx1MDAyN01vZGVsXHUwMDI3LCBcdTAwMjdOIChCKVx1MDAyNywgXHUwMDI3RCAoQiB0b2spXHUwMDI3LCBcdTAwMjdEL05cdTAwMjcsIFx1MDAyN0MgKEZMT1BzKVx1MDAyNywgXHUwMDI3dnMgQ2hpbmNoaWxsYVx1MDAyNykpXG5wcmludChcdTAwMjctXHUwMDI3ICogODIpXG5mb3IgbmFtZSwgTiwgRCBpbiBtb2RlbHM6XG4gICAgQyAgID0gdHJhaW5pbmdfZmxvcHMoTiwgRClcbiAgICBkbiAgPSBEIC8gTlxuICAgIHJhdGlvID0gZG4gLyBjaGluY2hpbGxhX3JhdGlvXG4gICAgdGFnID0gXHUwMDI3b3B0aW1hbFx1MDAyNyBpZiAwLjggXHUwMDNjPSByYXRpbyBcdTAwM2M9IDEuMiBlbHNlIFx1MDAyN3s6LjFmfXggb3Zlclx1MDAyNy5mb3JtYXQocmF0aW8pIGlmIHJhdGlvIFx1MDAzZSAxIGVsc2UgXHUwMDI3ezouMWZ9eCB1bmRlclx1MDAyNy5mb3JtYXQoMS9yYXRpbylcbiAgICBwcmludChcdTAwMjd7Olx1MDAzYzIwfSB7Olx1MDAzZTguMGZ9IHs6XHUwMDNlMTAuMGZ9IHs6XHUwMDNlOC4xZn0gezpcdTAwM2UxNS4yZX0gezpcdTAwM2UxNX1cdTAwMjcuZm9ybWF0KG5hbWUsIE4vMWU5LCBELzFlOSwgZG4sIEMsIHRhZykpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSA0IOKAlCBNb2RlbCBDb21wYXJpc29uIG9uIENvbXB1dGUtT3B0aW1hbCBDdXJ2ZSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuRV9DT05TVCwgQV9DT05TVCwgQl9DT05TVCwgQUxQSEEsIEJFVEEgPSAxLjY5LCA0MDYuNCwgNDEwLjcsIDAuMzQsIDAuMjhcblxuZGVmIGNoaW5jaGlsbGFfbG9zcyhOLCBEKTpcbiAgICByZXR1cm4gRV9DT05TVCArIEFfQ09OU1QgKiBOKiooLUFMUEhBKSArIEJfQ09OU1QgKiBEKiooLUJFVEEpXG5cbiMgUmVhbCBtb2RlbHMgdG8gcGxvdDogKG5hbWUsIE5fcGFyYW1zLCBEX3Rva2VucywgY29sb3IpXG5tb2RlbHMgPSBbXG4gICAgKFx1MDAyN0dQVC0zIDE3NUJcdTAwMjcsICAgICAgMTc1ZTksICAzMDBlOSwgXHUwMDI3I2U3NGMzY1x1MDAyNyksXG4gICAgKFx1MDAyN0dvcGhlciAyODBCXHUwMDI3LCAgICAgMjgwZTksICAzMDBlOSwgXHUwMDI3I2U2N2UyMlx1MDAyNyksXG4gICAgKFx1MDAyN0NoaW5jaGlsbGEgNzBCXHUwMDI3LCAgIDcwZTksIDE0MDBlOSwgXHUwMDI3IzI3YWU2MFx1MDAyNyksXG4gICAgKFx1MDAyN0xMYU1BLTEgN0JcdTAwMjcsICAgICAgICA3ZTksIDEwMDBlOSwgXHUwMDI3IzM0OThkYlx1MDAyNyksXG5dXG5cbiMgQ29tcHV0ZS1vcHRpbWFsIGZyb250aWVyXG5DX3JhbmdlID0gbnAubG9nc3BhY2UoMTksIDI0LCAzMDApXG5OX29wdF9mID0gbnAuc3FydChDX3JhbmdlIC8gMTIwLjApXG5EX29wdF9mID0gMjAuMCAqIE5fb3B0X2Zcbkxfb3B0X2YgPSBjaGluY2hpbGxhX2xvc3MoTl9vcHRfZiwgRF9vcHRfZilcblxucGx0LmZpZ3VyZShmaWdzaXplPSg5LCA1KSlcbnBsdC5wbG90KENfcmFuZ2UsIExfb3B0X2YsIFx1MDAyN2stXHUwMDI3LCBsdz0yLCBsYWJlbD1cdTAwMjdDaGluY2hpbGxhLW9wdGltYWwgZnJvbnRpZXJcdTAwMjcpXG5mb3IgbmFtZSwgTiwgRCwgY29sIGluIG1vZGVsczpcbiAgICBDX21vZGVsID0gNi4wICogTiAqIERcbiAgICBwbHQuc2NhdHRlcihDX21vZGVsLCBjaGluY2hpbGxhX2xvc3MoTiwgRCksIHM9MTMwLCBjb2xvcj1jb2wsIHpvcmRlcj01LCBsYWJlbD1uYW1lKVxucGx0LnhzY2FsZShcdTAwMjdsb2dcdTAwMjcpXG5wbHQueGxhYmVsKFx1MDAyN0NvbXB1dGUgQyAoRkxPUHMpXHUwMDI3LCBmb250c2l6ZT0xMilcbnBsdC55bGFiZWwoXHUwMDI3UHJlZGljdGVkIFRlc3QgTG9zcyAobmF0cylcdTAwMjcsIGZvbnRzaXplPTEyKVxucGx0LnRpdGxlKFx1MDAyN01vZGVscyB2cyBDaGluY2hpbGxhIENvbXB1dGUtT3B0aW1hbCBGcm9udGllclx1MDAyNywgZm9udHNpemU9MTMpXG5wbHQubGVnZW5kKGZvbnRzaXplPTEwKVxucGx0LmdyaWQoVHJ1ZSwgYWxwaGE9MC4zKVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdtb2RlbF9mcm9udGllcl9jb21wYXJpc29uLnBuZ1x1MDAyNywgZHBpPTE1MClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0YWJsZSBiZWxvdyBjb21wYXJlcyBwcmUtQ2hpbmNoaWxsYSBhbmQgcG9zdC1DaGluY2hpbGxhIG1vZGVscyBzaG93aW5nIHRoZWlyIHBhcmFtZXRlciBjb3VudCwgdG9rZW4gY291bnQsIEQvTiByYXRpbywgYW5kIGhvdyBmYXIgZWFjaCBpcyBmcm9tIHRoZSBjb21wdXRlLW9wdGltYWwgYWxsb2NhdGlvbi4gTW9kZWxzIGFib3ZlIHRoZSBjb21wdXRlLW9wdGltYWwgRC9OIGFyZSBpbmZlcmVuY2Utb3B0aW1pemVkICh0cmFpbmVkIGJleW9uZCBDaGluY2hpbGxhLW9wdGltYWwgdG8gcmVkdWNlIHBlci1xdWVyeSBzZXJ2aW5nIGNvc3QpLiBNb2RlbHMgYmVsb3cgYXJlIHRyYWluaW5nLWNvbXB1dGUtb3B0aW1pemVkLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCIsIlBhcmFtcyAoQikiLCJUb2tlbnMgKEIpIiwiRC9OIFJhdGlvIiwiUmVsLiB0byBDb21wdXRlLU9wdGltYWwiLCJOb3RlcyJdLCJyb3dzIjpbWyJHUFQtMyIsIjE3NSIsIjMwMCIsIjEuNyIsIn4xMHggdW5kZXIgKGRhdGEpIiwiUHJlLUNoaW5jaGlsbGEgcGFyYWRpZ20iXSxbIkdvcGhlciIsIjI4MCIsIjMwMCIsIjEuMSIsIn4xOHggdW5kZXIgKGRhdGEpIiwiUHJlLUNoaW5jaGlsbGEgcGFyYWRpZ20iXSxbIkNoaW5jaGlsbGEiLCI3MCIsIjE0MDAiLCIyMCIsIkNvbXB1dGUtb3B0aW1hbCIsIkJlbmNobWFyayBtb2RlbCJdLFsiTExhTUEtMSA3QiIsIjciLCIxMDAwIiwiMTQzIiwifjd4IG92ZXIgKGRhdGEpIiwiSW5mZXJlbmNlLW9wdGltaXplZCJdLFsiTExhTUEtMiA3MEIiLCI3MCIsIjIwMDAiLCIyOC42IiwifjEuNHggb3ZlciAoZGF0YSkiLCJOZWFyIGNvbXB1dGUtb3B0aW1hbCJdLFsiTWlzdHJhbCA3QiIsIjciLCIyMDAwIiwiMjg2IiwifjE0eCBvdmVyIChkYXRhKSIsIkluZmVyZW5jZS1vcHRpbWl6ZWQiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIENoaW5jaGlsbGEgcmVzdWx0IGltbWVkaWF0ZWx5IHJlZnJhbWVkIHRoZSBmaWVsZC4gTW9kZWxzIGxpa2UgR1BULTQgYW5kIHN1YnNlcXVlbnQgZnJvbnRpZXIgc3lzdGVtcyBzaGlmdGVkIHRvIHRyYWluaW5nIHNtYWxsZXIgYXJjaGl0ZWN0dXJlcyBvbiB2YXN0bHkgbW9yZSB0b2tlbnMuIFRoZSBwcmFjdGljYWwgcXVlc3Rpb24gY2hhbmdlZCBmcm9tIFx1MDAyN2hvdyBsYXJnZSBzaG91bGQgdGhlIG1vZGVsIGJlP1x1MDAyNyB0byBcdTAwMjdob3cgbWFueSB0b2tlbnMgY2FuIHdlIGFmZm9yZCB0byB0cmFpbiBvbiwgYW5kIHdoYXQgc2l6ZSBtb2RlbCBpcyBjb21wdXRlLW9wdGltYWwgZm9yIHRoYXQgZGF0YSBidWRnZXQ/XHUwMDI3In0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJGb3IgYW55IGZpeGVkIGNvbXB1dGUgYnVkZ2V0IEM6IHRyYWluIE4qID0gc3FydChDLzEyMCkgcGFyYW1zIG9uIEQqID0gMjAqTiogdG9rZW5zIiwiR1BULTMgbmVlZGVkIH4zVCB0b2tlbnMgdG8gYmUgY29tcHV0ZS1vcHRpbWFsIGF0IDE3NUIgcGFyYW1zIOKAlCBpdCBvbmx5IHNhdyAzMDBCIiwiQ2hpbmNoaWxsYSA3MEIgbWF0Y2hlcyBvciBiZWF0cyBHUFQtMyAxNzVCIGF0IDR4IGZld2VyIHBhcmFtZXRlcnMgYW5kIHNhbWUgY29tcHV0ZSIsIlBvc3QtQ2hpbmNoaWxsYSBtb2RlbHMgKExMYU1BLCBGYWxjb24sIE1pc3RyYWwpIGludGVudGlvbmFsbHkgb3Zlci10cmFpbiBmb3IgaW5mZXJlbmNlIHNhdmluZ3MiLCJPcHRpbWFsIGFsbG9jYXRpb24gZGVwZW5kcyBvbiBpbmZlcmVuY2UgY29zdDogaWYgc2VydmluZyBhdCBzY2FsZSwgc21hbGxlciBtb2RlbHMgYXJlIGJldHRlciJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkluZm8iLCJjb250ZW50IjoiQ2hpbmNoaWxsYVx1MDAyN3MgMjA6MSB0b2tlbi10by1wYXJhbWV0ZXIgcmF0aW8gYXNzdW1lcyB0cmFpbmluZyBpcyBkb25lIG9uY2UgZm9yIGRlcGxveW1lbnQg4oCUIGlmIHlvdSBwbGFuIHRvIHNlcnZlIGEgbW9kZWwgYXQgc2NhbGUsIHRyYWluaW5nIHNtYWxsZXIgbW9kZWxzIG9uIG1vcmUgZGF0YSByZWR1Y2VzIGluZmVyZW5jZSBjb3N0IHBlciBxdWVyeSB3aGlsZSBtYXRjaGluZyB0aGUgc2FtZSBjb21wdXRlIGJ1ZGdldC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW1pdGF0aW9ucyBhbmQgQ2F2ZWF0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIENoaW5jaGlsbGEgcmVzdWx0cyBoYXZlIGltcG9ydGFudCBzY29wZSBsaW1pdGF0aW9ucy4gRmlyc3QsIHRoZSBvcHRpbWFsIEQvTiByYXRpbyBhc3N1bWVzIGFsbCB0cmFpbmluZyBjb21wdXRlIGlzIHRoZSBjb25zdHJhaW50IOKAlCBpZiBpbmZlcmVuY2UgY29zdCBkb21pbmF0ZXMgKG1pbGxpb25zIG9mIHF1ZXJpZXMgcGVyIGRheSksIGEgc21hbGxlciBtb2RlbCB0cmFpbmVkIG9uIGZhciBtb3JlIHRva2VucyBpcyBvZnRlbiBiZXR0ZXIuIFNlY29uZCwgdGhlIGZpdHRlZCBjb25zdGFudHMgKEEsIEIsIGFscGhhLCBiZXRhKSB3ZXJlIG1lYXN1cmVkIG9uIFRoZSBQaWxlIGFuZCBtYXkgbm90IHRyYW5zZmVyIHRvIGRvbWFpbi1zcGVjaWZpYyBjb3Jwb3JhIHN1Y2ggYXMgY29kZSBvciBtYXRoLiBUaGlyZCwgdGhlIGFwcHJveGltYXRpb24gQyA9IDZORCBpZ25vcmVzIGF0dGVudGlvbiBjb21wbGV4aXR5LCBlbWJlZGRpbmcgdGFibGVzLCBhbmQgbGF5ZXIgbm9ybWFsaXphdGlvbi4gRm91cnRoLCB0aGUgc2NhbGluZyBsYXdzIGRlc2NyaWJlIHByZS10cmFpbmluZyBvbmx5IOKAlCBpbnN0cnVjdGlvbiB0dW5pbmcsIFJMSEYsIGFuZCBEUE8gcG9zdC10cmFpbmluZyBjb3N0IGlzIG5vdCBjYXB0dXJlZC4gRmlmdGgsIGRpbWluaXNoaW5nIHJldHVybnMgZnJvbSBkYXRhIHF1YWxpdHkgYW5kIGRlZHVwbGljYXRpb24gbWVhbiB0aGF0IDFUIHRva2VucyBvZiB3ZWIgdGV4dCBtYXkgYmUgZXF1aXZhbGVudCB0byBmYXIgZmV3ZXIgaGlnaC1xdWFsaXR5IHRva2Vucy4ifV0="
---
# Chinchilla Scaling Laws — Compute-Optimal Token-to-Parameter Ratios

In 2022, Hoffmann et al. at DeepMind published the Chinchilla paper, overturning the prevailing Kaplan-derived wisdom that model size should scale faster than data. By training over 400 models ranging from 70M to 16B parameters on 5B to 500B tokens, they identified the true compute-optimal allocation: for a fixed compute budget C, both model size N* and token count D* should scale equally — proportional to C^0.5 each. The key result: D/N approximately 20 tokens per parameter at the optimal point, not 1 as Kaplan predicted.

## The Compute-Optimal Insight

Chinchilla (70B parameters, 1.4T training tokens) outperformed Gopher (280B parameters, 300B tokens) at the same compute budget, demonstrating that data quantity matters as much as model size. GPT-3 (175B parameters, 300B tokens) was undertrained by approximately 10x on data relative to its parameter count. The joint loss formula L(N, D) = E + A/N^alpha + B/D^beta was fitted with E=1.69, A=406.4, alpha=0.34, B=410.7, beta=0.28, enabling precise optimization of the N-D trade-off at any compute level.

- Optimal D/N = 20: train on 20 tokens per parameter at compute-optimal allocation
- N* proportional to C^0.5 and D* proportional to C^0.5: equal scaling of model and data
- Chinchilla (70B, 1.4T) beats Gopher (280B, 300B) at same compute — 4x smaller model, 5x more data
- GPT-3 (175B, 300B tokens): D/N = 1.7, approximately 10x under-trained on data
- C = 6*N*D approximation: 6 multiply-adds per parameter per token (2 forward + 4 backward)
- LLaMA-1 (7B, 1T tokens): D/N = 143, approximately 7x over-trained — inference-optimized

## Code 1 — Chinchilla Loss Formula

```python
import numpy as np
import matplotlib.pyplot as plt

# Chinchilla fitted constants (Hoffmann et al., 2022, Table 3)
E_CONST = 1.69    # irreducible loss: entropy floor of natural language
A_CONST = 406.4   # parameter scaling coefficient
B_CONST = 410.7   # data scaling coefficient
ALPHA   = 0.34    # parameter scaling exponent
BETA    = 0.28    # data scaling exponent

def chinchilla_loss(N, D):
    '''L(N, D) = E + A/N^alpha + B/D^beta'''
    return E_CONST + A_CONST * N ** (-ALPHA) + B_CONST * D ** (-BETA)

# Fix compute C, sweep N while D = C / (6*N)
C_fixed = 6e21   # ~30B model-scale compute budget
N_range = np.logspace(8, 12, 300)  # 100M to 1T parameters
D_range = C_fixed / (6.0 * N_range)

L_range  = chinchilla_loss(N_range, D_range)
best_idx = np.argmin(L_range)
N_opt, D_opt, L_min = N_range[best_idx], D_range[best_idx], L_range[best_idx]
print('Compute budget: {:.1e} FLOPs'.format(C_fixed))
print('Optimal N*: {:.2f}B params | D*: {:.2f}B tokens | D/N: {:.1f} | L_min: {:.4f}'.format(
    N_opt/1e9, D_opt/1e9, D_opt/N_opt, L_min))

plt.figure(figsize=(9, 5))
plt.semilogx(N_range / 1e9, L_range, 'b-', lw=2, label='L(N, D) at fixed C')
plt.axvline(N_opt / 1e9, color='r', ls='--', lw=2, label='Optimal N* = {:.1f}B'.format(N_opt/1e9))
plt.xlabel('Model Size N (billions of parameters)', fontsize=12)
plt.ylabel('Predicted Loss L(N, D)', fontsize=12)
plt.title('Chinchilla Loss vs N for Fixed Compute C = {:.1e} FLOPs'.format(C_fixed), fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chinchilla_loss_curve.png', dpi=150)
plt.show()
```

## Optimal Token-to-Parameter Ratio

The 20:1 token-to-parameter ratio emerges from the symmetry of the Chinchilla loss formula when both alpha and beta are similar (0.34 vs 0.28). The optimal allocation minimizes L(N, D) = E + A/N^alpha + B/D^beta subject to C = 6ND. Taking partial derivatives and setting them equal gives the condition A*alpha/N^(alpha+1) = B*beta/D^(beta+1), which with alpha approximately beta leads to A/N^alpha approximately B/D^beta — roughly equal contributions from each term. Since A and B are nearly equal (406.4 vs 410.7), and alpha and beta are close, the optimal N and D end up roughly equal in their contribution, yielding D/N = 20 as the empirical ratio.

## Code 2 — Compute-Optimal Frontier

```python
import numpy as np
import matplotlib.pyplot as plt

def chinchilla_optimal(C):
    '''Chinchilla: equal scaling, D* = 20*N*, C = 6*N*D* = 120*N*^2.'''
    N_star = np.sqrt(C / 120.0)
    D_star = 20.0 * N_star
    return N_star, D_star

def kaplan_optimal(C, k_N=1.3e-5):
    '''Kaplan: N scales faster than D (N* proportional to C^0.73).'''
    N_star = k_N * (C ** 0.73)
    D_star = C / (6.0 * N_star)
    return N_star, D_star

C_range = np.logspace(18, 24, 150)
ch_N, ch_D = chinchilla_optimal(C_range)
kp_N, kp_D = kaplan_optimal(C_range)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].loglog(C_range, ch_N/1e9, 'b-',  lw=2, label='Chinchilla N*')
axes[0].loglog(C_range, kp_N/1e9, 'r--', lw=2, label='Kaplan N*')
axes[0].set(xlabel='Compute C (FLOPs)', ylabel='Optimal N* (billions)',
            title='Optimal Model Size vs Compute')
axes[0].legend(); axes[0].grid(True, alpha=0.3)

axes[1].loglog(C_range, ch_D/1e9, 'b-',  lw=2, label='Chinchilla D*')
axes[1].loglog(C_range, kp_D/1e9, 'r--', lw=2, label='Kaplan D*')
axes[1].set(xlabel='Compute C (FLOPs)', ylabel='Optimal D* (B tokens)',
            title='Optimal Token Count vs Compute')
axes[1].legend(); axes[1].grid(True, alpha=0.3)

plt.suptitle('Kaplan vs Chinchilla: Compute-Optimal Frontier', fontsize=13)
plt.tight_layout()
plt.savefig('chinchilla_vs_kaplan_frontier.png', dpi=150)
plt.show()
```

## Training FLOPs Estimation

The C = 6ND approximation counts forward and backward passes through a transformer. Each multiply-add operation contributes 2 FLOPs (one multiply, one add). The forward pass requires roughly 2ND FLOPs (one pass through N parameters for each of D tokens). The backward pass requires roughly 4ND FLOPs (two passes: computing gradients with respect to weights and with respect to activations). Total: 6ND FLOPs. This approximation ignores attention FLOP contributions (O(T^2) per layer), embedding lookups, and layer norm — these add roughly 10-20% overhead for typical sequence lengths and architecture choices.

## Code 3 — Training FLOPs Estimation

```python
import numpy as np

# C = 6 * N * D approximation (Chinchilla paper)
# Factor of 6 = 2 (forward pass) + 4 (backward pass) per parameter per token

def training_flops(N_params, D_tokens):
    '''Estimate training FLOPs: C = 6 * N * D.'''
    return 6.0 * N_params * D_tokens

# Known model specs: (name, N_params, D_tokens)
models = [
    ('GPT-3 175B',      175e9,   300e9),
    ('Chinchilla 70B',   70e9,  1400e9),
    ('Gopher 280B',     280e9,   300e9),
    ('LLaMA-1 7B',        7e9,  1000e9),
    ('LLaMA-2 70B',      70e9,  2000e9),
]

chinchilla_ratio = 20.0  # compute-optimal D/N

print('{:<20} {:>8} {:>10} {:>8} {:>15} {:>15}'.format(
    'Model', 'N (B)', 'D (B tok)', 'D/N', 'C (FLOPs)', 'vs Chinchilla'))
print('-' * 82)
for name, N, D in models:
    C   = training_flops(N, D)
    dn  = D / N
    ratio = dn / chinchilla_ratio
    tag = 'optimal' if 0.8 <= ratio <= 1.2 else '{:.1f}x over'.format(ratio) if ratio > 1 else '{:.1f}x under'.format(1/ratio)
    print('{:<20} {:>8.0f} {:>10.0f} {:>8.1f} {:>15.2e} {:>15}'.format(name, N/1e9, D/1e9, dn, C, tag))
```

## Code 4 — Model Comparison on Compute-Optimal Curve

```python
import numpy as np
import matplotlib.pyplot as plt

E_CONST, A_CONST, B_CONST, ALPHA, BETA = 1.69, 406.4, 410.7, 0.34, 0.28

def chinchilla_loss(N, D):
    return E_CONST + A_CONST * N**(-ALPHA) + B_CONST * D**(-BETA)

# Real models to plot: (name, N_params, D_tokens, color)
models = [
    ('GPT-3 175B',      175e9,  300e9, '#e74c3c'),
    ('Gopher 280B',     280e9,  300e9, '#e67e22'),
    ('Chinchilla 70B',   70e9, 1400e9, '#27ae60'),
    ('LLaMA-1 7B',        7e9, 1000e9, '#3498db'),
]

# Compute-optimal frontier
C_range = np.logspace(19, 24, 300)
N_opt_f = np.sqrt(C_range / 120.0)
D_opt_f = 20.0 * N_opt_f
L_opt_f = chinchilla_loss(N_opt_f, D_opt_f)

plt.figure(figsize=(9, 5))
plt.plot(C_range, L_opt_f, 'k-', lw=2, label='Chinchilla-optimal frontier')
for name, N, D, col in models:
    C_model = 6.0 * N * D
    plt.scatter(C_model, chinchilla_loss(N, D), s=130, color=col, zorder=5, label=name)
plt.xscale('log')
plt.xlabel('Compute C (FLOPs)', fontsize=12)
plt.ylabel('Predicted Test Loss (nats)', fontsize=12)
plt.title('Models vs Chinchilla Compute-Optimal Frontier', fontsize=13)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('model_frontier_comparison.png', dpi=150)
plt.show()
```

The table below compares pre-Chinchilla and post-Chinchilla models showing their parameter count, token count, D/N ratio, and how far each is from the compute-optimal allocation. Models above the compute-optimal D/N are inference-optimized (trained beyond Chinchilla-optimal to reduce per-query serving cost). Models below are training-compute-optimized.

| Model | Params (B) | Tokens (B) | D/N Ratio | Rel. to Compute-Optimal | Notes |
| --- | --- | --- | --- | --- | --- |
| GPT-3 | 175 | 300 | 1.7 | ~10x under (data) | Pre-Chinchilla paradigm |
| Gopher | 280 | 300 | 1.1 | ~18x under (data) | Pre-Chinchilla paradigm |
| Chinchilla | 70 | 1400 | 20 | Compute-optimal | Benchmark model |
| LLaMA-1 7B | 7 | 1000 | 143 | ~7x over (data) | Inference-optimized |
| LLaMA-2 70B | 70 | 2000 | 28.6 | ~1.4x over (data) | Near compute-optimal |
| Mistral 7B | 7 | 2000 | 286 | ~14x over (data) | Inference-optimized |

The Chinchilla result immediately reframed the field. Models like GPT-4 and subsequent frontier systems shifted to training smaller architectures on vastly more tokens. The practical question changed from 'how large should the model be?' to 'how many tokens can we afford to train on, and what size model is compute-optimal for that data budget?'

- For any fixed compute budget C: train N* = sqrt(C/120) params on D* = 20*N* tokens
- GPT-3 needed ~3T tokens to be compute-optimal at 175B params — it only saw 300B
- Chinchilla 70B matches or beats GPT-3 175B at 4x fewer parameters and same compute
- Post-Chinchilla models (LLaMA, Falcon, Mistral) intentionally over-train for inference savings
- Optimal allocation depends on inference cost: if serving at scale, smaller models are better

> **Info**: Chinchilla's 20:1 token-to-parameter ratio assumes training is done once for deployment — if you plan to serve a model at scale, training smaller models on more data reduces inference cost per query while matching the same compute budget.

## Limitations and Caveats

The Chinchilla results have important scope limitations. First, the optimal D/N ratio assumes all training compute is the constraint — if inference cost dominates (millions of queries per day), a smaller model trained on far more tokens is often better. Second, the fitted constants (A, B, alpha, beta) were measured on The Pile and may not transfer to domain-specific corpora such as code or math. Third, the approximation C = 6ND ignores attention complexity, embedding tables, and layer normalization. Fourth, the scaling laws describe pre-training only — instruction tuning, RLHF, and DPO post-training cost is not captured. Fifth, diminishing returns from data quality and deduplication mean that 1T tokens of web text may be equivalent to far fewer high-quality tokens.

