---
title: "Learning Rate Schedules"
slug: "learning-rate-schedules"
description: "Covers constant LR pitfalls, linear warmup rationale, cosine annealing, the 1-cycle policy, learning rate finder range test, and the WSD (Warmup-Stable-Decay) schedule used in LLM pretraining."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGxlYXJuaW5nIHJhdGUgaXMgdGhlIHNpbmdsZSBtb3N0IGltcG9ydGFudCBvcHRpbWl6ZXIgaHlwZXJwYXJhbWV0ZXIsIHlldCBhIGNvbnN0YW50IExSIGlzIGFsbW9zdCBuZXZlciBvcHRpbWFsLiBNb2Rlcm4gdHJhaW5pbmcgcmVjaXBlcyBjb21iaW5lIGEgd2FybXVwIHBoYXNlIChyYW1wIGZyb20gbmVhci16ZXJvIHRvIHBlYWsgTFIpLCBhIG1haW4gdHJhaW5pbmcgcGhhc2UsIGFuZCBhIGRlY2F5IHBoYXNlLiBVbmRlcnN0YW5kaW5nIHdoeSBlYWNoIHBoYXNlIGV4aXN0cyDigJQgYW5kIGhvdyB0byBmaW5kIHRoZSByaWdodCBwZWFrIExSIOKAlCBpcyBlc3NlbnRpYWwgZm9yIHRyYWluaW5nIHN0YWJsZSwgd2VsbC1jb252ZXJnZWQgbW9kZWxzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBDb25zdGFudCBMUiBGYWlscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBjb25zdGFudCBMUiB0aGF0IGlzIHRvbyBsYXJnZSBjYXVzZXMgZGl2ZXJnZW5jZSAobG9zcyBzcGlrZXMsIE5hTikgYmVjYXVzZSBncmFkaWVudCBzdGVwcyBvdmVyc2hvb3QgdGhlIGxvc3Mgc3VyZmFjZS4gQSBjb25zdGFudCBMUiB0aGF0IGlzIHRvbyBzbWFsbCBjb252ZXJnZXMgc2xvd2x5IGFuZCBtYXkgbGFuZCBpbiBhIHNoYXJwLCBwb29ybHkgZ2VuZXJhbGl6aW5nIG1pbmltdW0uIFNjaGVkdWxlcyBjb21iaW5lIGEgbGFyZ2UgTFIgZWFybHkgKHRvIGVzY2FwZSBiYWQgaW5pdGlhbGl6YXRpb24pIHdpdGggYSBzbWFsbCBMUiBsYXRlICh0byBzZXR0bGUgaW50byBhIHNtb290aCBtaW5pbXVtKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW5lYXIgV2FybXVwOiBXaHkgSXQgTWF0dGVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gQWRhbSwgdGhlIHNlY29uZCBtb21lbnQgdsyCID0gdi8oMS3OsuKCguG1lykgaXMgbmVhciB6ZXJvIGF0IGluaXRpYWxpemF0aW9uIOKAlCBBZGFtXHUwMDI3cyBiaWFzIGNvcnJlY3Rpb24gY29tcGVuc2F0ZXMsIGJ1dCBpbiBwcmFjdGljZSBlYXJseSBzdGVwcyBjYW4gc3RpbGwgYmUgbGFyZ2UgYW5kIHVuc3RhYmxlLiBXYXJtdXAgc3RhcnRzIGF0IGxyPTAgKG9yIGEgc21hbGwgZnJhY3Rpb24pIGFuZCByYW1wcyBsaW5lYXJseSB0byBwZWFrX2xyIG92ZXIgd2FybXVwX3N0ZXBzLiBUaGlzIGxldHMgdsyCIHN0YWJpbGl6ZSBiZWZvcmUgdGFraW5nIGxhcmdlIHN0ZXBzLCBhbmQgYXZvaWRzIGNhdGFzdHJvcGhpYyBlYXJseSB1cGRhdGVzIHRoYXQgY2FuIGRlc3Ryb3kgZnJlc2hseSBpbml0aWFsaXplZCB3ZWlnaHRzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSG93IExvbmcgdG8gV2FybSBVcCIsImNvbnRlbnQiOiJUeXBpY2FsIHdhcm11cCBpcyAx4oCTNSUgb2YgdG90YWwgdHJhaW5pbmcgc3RlcHMuIEZvciBMTE0gcHJldHJhaW5pbmcgYXQgMTAwayBzdGVwczogMTAwMOKAkzUwMDAgd2FybXVwIHN0ZXBzLiBGb3IgZmluZS10dW5pbmcgc2hvcnQgcnVuczogNTDigJMxMDAgc3RlcHMuIExvbmdlciB3YXJtdXAgaXMgc2FmZXIgYnV0IGRlbGF5cyByZWFjaGluZyBwZWFrIExSLiBUaGUgV1NEIHNjaGVkdWxlIHVzZXMgYSBmaXhlZCB3YXJtdXAgb2YgfjElIGFuZCB0aGVuIGhvbGRzIHRoZSBMUiBzdGFibGUgZm9yIG1vc3Qgb2YgdHJhaW5pbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29zaW5lIEFubmVhbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29zaW5lIGFubmVhbGluZyBzbW9vdGhseSBkZWNheXMgdGhlIExSOiDOtyh0KSA9IM63X21pbiArICjOt19tYXgg4oiSIM63X21pbikvMiDCtyAoMSArIGNvcyjPgHQvVCkpLiBBdCB0PTAgaXQgZXF1YWxzIM63X21heDsgYXQgdD1UIGl0IGVxdWFscyDOt19taW4uIFRoZSBzbW9vdGggZGVjYXkgYXZvaWRzIHRoZSBhYnJ1cHQgTFIgZHJvcHMgb2Ygc3RlcCBkZWNheSwgd2hpY2ggY2FuIGNhdXNlIHN1ZGRlbiBsb3NzIGNoYW5nZXMuIENvc2luZSBhbm5lYWxpbmcgd2l0aCB3YXJtIHJlc3RhcnRzIChTR0RSKSBwZXJpb2RpY2FsbHkgcmVzZXRzIHQgdG8gMCwgYWxsb3dpbmcgdGhlIG1vZGVsIHRvIGVzY2FwZSBsb2NhbCBtaW5pbWEuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdGhcblxuZGVmIGNvc2luZV9hbm5lYWwoc3RlcCwgVCwgZXRhX21heD0xZS0zLCBldGFfbWluPTFlLTYpOlxuICAgICMgZXRhKHQpID0gZXRhX21pbiArIChldGFfbWF4IC0gZXRhX21pbikvMiAqICgxICsgY29zKHBpKnQvVCkpXG4gICAgcmV0dXJuIGV0YV9taW4gKyAoZXRhX21heCAtIGV0YV9taW4pICogMC41ICogKDEuMCArIG1hdGguY29zKG1hdGgucGkgKiBzdGVwIC8gVCkpXG5cbmRlZiB3YXJtdXBfY29zaW5lKHN0ZXAsIHdhcm11cCwgdG90YWwsIGV0YV9tYXg9MWUtMywgZXRhX21pbj0xZS02KTpcbiAgICAjIFBoYXNlIDE6IGxpbmVhciB3YXJtdXAgIFswLCB3YXJtdXApXG4gICAgIyBQaGFzZSAyOiBjb3NpbmUgZGVjYXkgICBbd2FybXVwLCB0b3RhbF1cbiAgICBpZiBzdGVwIFx1MDAzYyB3YXJtdXA6XG4gICAgICAgIHJldHVybiBldGFfbWF4ICogc3RlcCAvIG1heCh3YXJtdXAsIDEpXG4gICAgcHJvZ3Jlc3MgPSAoc3RlcCAtIHdhcm11cCkgLyBtYXgodG90YWwgLSB3YXJtdXAsIDEpXG4gICAgcmV0dXJuIGV0YV9taW4gKyAoZXRhX21heCAtIGV0YV9taW4pICogMC41ICogKDEuMCArIG1hdGguY29zKG1hdGgucGkgKiBwcm9ncmVzcykpXG5cbnRvdGFsLCB3YXJtdXAgPSAxMDAwLCAxMDBcblxucHJpbnQoXHUwMDI3V2FybXVwICsgY29zaW5lIGFubmVhbGluZyBzY2hlZHVsZTpcdTAwMjcpXG5wcmludChcdTAwMjclLTZzICAlLTEycyAgJXNcdTAwMjcgJSAoXHUwMDI3U3RlcFx1MDAyNywgXHUwMDI3TFJcdTAwMjcsIFx1MDAyN0Jhclx1MDAyNykpXG5mb3IgdCBpbiBbMCwgMjUsIDUwLCAxMDAsIDIwMCwgNDAwLCA2MDAsIDgwMCwgOTk5XTpcbiAgICBsciAgPSB3YXJtdXBfY29zaW5lKHQsIHdhcm11cCwgdG90YWwpXG4gICAgYmFyID0gXHUwMDI3I1x1MDAyNyAqIGludChsciAvIDFlLTMgKiAzMClcbiAgICBwcmludChcdTAwMjclNmQgICUuNGUgICAgJXNcdTAwMjcgJSAodCwgbHIsIGJhcikpXG5cbmxycyA9IFt3YXJtdXBfY29zaW5lKHQsIHdhcm11cCwgdG90YWwpIGZvciB0IGluIHJhbmdlKHRvdGFsKV1cbnByaW50KFx1MDAyN1x1MDAyNylcbnByaW50KFx1MDAyN1BlYWsgTFI6ICUuMmUgIHwgIEZpbmFsIExSOiAlLjJlXHUwMDI3ICUgKG1heChscnMpLCBscnNbLTFdKSlcbnByaW50KFx1MDAyN1dhcm11cDogJWQgc3RlcHMgIHwgIENvc2luZSBkZWNheTogJWQgc3RlcHNcdTAwMjcgJSAod2FybXVwLCB0b3RhbCAtIHdhcm11cCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIDEtQ3ljbGUgUG9saWN5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgMS1jeWNsZSBwb2xpY3kgKFNtaXRoIDIwMTcpIHVzZXMgYSB0cmlhbmd1bGFyIExSIHNjaGVkdWxlOiByYW1wIHVwIGZyb20gYmFzZV9sciB0byBtYXhfbHIgb3ZlciBwY3Rfc3RhcnQgZnJhY3Rpb24gb2YgdHJhaW5pbmcsIHRoZW4gZGVjYXkgZnJvbSBtYXhfbHIgYmFjayB0byBiYXNlX2xyL2Rpdl9mYWN0b3IuIEEgZmluYWwgcGhhc2UgZGVjYXlzIHRvIGJhc2VfbHIvZmluYWxfZGl2X2ZhY3Rvci4gVGhpcyBlbmFibGVzIFx1MDAyN3N1cGVyLWNvbnZlcmdlbmNlXHUwMDI3IOKAlCB0cmFpbmluZyBpbiBmYXIgZmV3ZXIgaXRlcmF0aW9ucyB0aGFuIHN0ZXAgZGVjYXkuIFB5VG9yY2ggcHJvdmlkZXMgT25lQ3ljbGVMUiBvdXQgb2YgdGhlIGJveC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuXG5tb2RlbCA9IG5uLkxpbmVhcigxMCwgMilcbm9wdGltaXplciA9IG9wdGltLkFkYW1XKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcblxuIyAxLiBPbmVDeWNsZUxSOiB3YXJtdXAgLVx1MDAzZSBwZWFrIC1cdTAwM2UgY29zaW5lIGFubmVhbFxub25lX2N5Y2xlID0gb3B0aW0ubHJfc2NoZWR1bGVyLk9uZUN5Y2xlTFIoXG4gICAgb3B0aW1pemVyLFxuICAgIG1heF9scj0xZS0yLFxuICAgIHRvdGFsX3N0ZXBzPTEwMDAsXG4gICAgcGN0X3N0YXJ0PTAuMSwgICAgICAgICAgICMgMTAlIHdhcm11cFxuICAgIGFubmVhbF9zdHJhdGVneT1cdTAwMjdjb3NcdTAwMjcsXG4gICAgZGl2X2ZhY3Rvcj0yNSwgICAgICAgICAgICAjIHN0YXJ0IGxyID0gbWF4X2xyIC8gMjVcbiAgICBmaW5hbF9kaXZfZmFjdG9yPTFlNCAgICAgICMgZW5kIGxyID0gc3RhcnRfbHIgLyAxZTRcbilcblxuIyAyLiBDb3NpbmVBbm5lYWxpbmdMUlxuY29zX3NjaGVkID0gb3B0aW0ubHJfc2NoZWR1bGVyLkNvc2luZUFubmVhbGluZ0xSKFxuICAgIG9wdGltaXplciwgVF9tYXg9MTAwMCwgZXRhX21pbj0xZS02KVxuXG4jIDMuIExpbmVhciB3YXJtdXAgLVx1MDAzZSBDb3NpbmUgZGVjYXkgKFNlcXVlbnRpYWxMUilcbndhcm11cF9zY2hlZCA9IG9wdGltLmxyX3NjaGVkdWxlci5MaW5lYXJMUihcbiAgICBvcHRpbWl6ZXIsIHN0YXJ0X2ZhY3Rvcj0wLjAxLCBlbmRfZmFjdG9yPTEuMCwgdG90YWxfaXRlcnM9MTAwKVxuY29zaW5lX3NjaGVkID0gb3B0aW0ubHJfc2NoZWR1bGVyLkNvc2luZUFubmVhbGluZ0xSKFxuICAgIG9wdGltaXplciwgVF9tYXg9OTAwLCBldGFfbWluPTFlLTYpXG5zZXFfc2NoZWQgPSBvcHRpbS5scl9zY2hlZHVsZXIuU2VxdWVudGlhbExSKFxuICAgIG9wdGltaXplciwgc2NoZWR1bGVycz1bd2FybXVwX3NjaGVkLCBjb3NpbmVfc2NoZWRdLCBtaWxlc3RvbmVzPVsxMDBdKVxuXG5wcmludChcdTAwMjdTY2hlZHVsZXIgdHlwZXMgYXZhaWxhYmxlIGluIHRvcmNoLm9wdGltLmxyX3NjaGVkdWxlcjpcdTAwMjcpXG5zY2hlZHVsZXJzID0gW1x1MDAyN1N0ZXBMUlx1MDAyNywgXHUwMDI3TXVsdGlTdGVwTFJcdTAwMjcsIFx1MDAyN0Nvc2luZUFubmVhbGluZ0xSXHUwMDI3LCBcdTAwMjdPbmVDeWNsZUxSXHUwMDI3LFxuICAgICAgICAgICAgICBcdTAwMjdDb3NpbmVBbm5lYWxpbmdXYXJtUmVzdGFydHNcdTAwMjcsIFx1MDAyN1JlZHVjZUxST25QbGF0ZWF1XHUwMDI3LFxuICAgICAgICAgICAgICBcdTAwMjdMaW5lYXJMUlx1MDAyNywgXHUwMDI3U2VxdWVudGlhbExSXHUwMDI3LCBcdTAwMjdDaGFpbmVkU2NoZWR1bGVyXHUwMDI3XVxuZm9yIHMgaW4gc2NoZWR1bGVyczpcbiAgICBwcmludChcdTAwMjcgIC1cdTAwMjcsIHMpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGVhcm5pbmcgUmF0ZSBGaW5kZXIgKFJhbmdlIFRlc3QpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgTFIgcmFuZ2UgdGVzdCAoU21pdGggMjAxNSkgc3dlZXBzIHRoZSBMUiBsb2ctbGluZWFybHkgZnJvbSBhIHRpbnkgdmFsdWUgKDFlLTcpIHRvIGEgbGFyZ2UgdmFsdWUgKDEwKSwgdHJhaW5pbmcgZm9yIG9uZSBzdGVwIHBlciBMUiB2YWx1ZS4gVGhlIGxvc3MgaW5pdGlhbGx5IGRlY3JlYXNlcywgcmVhY2hlcyBhIG1pbmltdW0sIHRoZW4gZXhwbG9kZXMuIFRoZSBvcHRpbWFsIExSIGZvciB0cmFpbmluZyBpcyByb3VnaGx5IG9uZSBvcmRlciBvZiBtYWduaXR1ZGUgYmVsb3cgdGhlIExSIHdoZXJlIGxvc3Mgc3RhcnRzIHRvIGRpdmVyZ2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cbmltcG9ydCBtYXRoXG5cbmRlZiBscl9yYW5nZV90ZXN0KG1vZGVsLCBsb3NzX2ZuLCBkYXRhX2l0ZXIsIHN0YXJ0X2xyPTFlLTcsXG4gICAgICAgICAgICAgICAgICBlbmRfbHI9MTAuMCwgbnVtX3N0ZXBzPTEwMCk6XG4gICAgIyBTd2VlcCBsciBsb2ctbGluZWFybHk7IHJlY29yZCBsb3NzIGF0IGVhY2ggc3RlcFxuICAgIGxycywgbG9zc2VzID0gW10sIFtdXG4gICAgbHIgPSBzdGFydF9sclxuICAgIGZhY3RvciA9IChlbmRfbHIgLyBzdGFydF9scikgKiogKDEuMCAvIG51bV9zdGVwcylcblxuICAgIG9wdCA9IG9wdGltLlNHRChtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPWxyLCBtb21lbnR1bT0wLjkpXG5cbiAgICBmb3Igc3RlcCwgKHgsIHkpIGluIGVudW1lcmF0ZShkYXRhX2l0ZXIpOlxuICAgICAgICBpZiBzdGVwIFx1MDAzZT0gbnVtX3N0ZXBzOlxuICAgICAgICAgICAgYnJlYWtcbiAgICAgICAgZm9yIHBnIGluIG9wdC5wYXJhbV9ncm91cHM6XG4gICAgICAgICAgICBwZ1tcdTAwMjdsclx1MDAyN10gPSBsclxuICAgICAgICBwcmVkID0gbW9kZWwoeClcbiAgICAgICAgbG9zcyA9IGxvc3NfZm4ocHJlZCwgeSlcbiAgICAgICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICBvcHQuc3RlcCgpXG4gICAgICAgIGxycy5hcHBlbmQobHIpXG4gICAgICAgIGxvc3Nlcy5hcHBlbmQobG9zcy5pdGVtKCkpXG4gICAgICAgIGxyICo9IGZhY3RvclxuXG4gICAgIyBGaW5kIHN0ZWVwZXN0IG5lZ2F0aXZlIHNsb3BlXG4gICAgYmVzdF9pZHgsIGJlc3Rfc2xvcGUgPSAxLCAwXG4gICAgZm9yIGkgaW4gcmFuZ2UoMSwgbGVuKGxvc3NlcykgLSAxKTpcbiAgICAgICAgc2xvcGUgPSBsb3NzZXNbaSsxXSAtIGxvc3Nlc1tpLTFdXG4gICAgICAgIGlmIHNsb3BlIFx1MDAzYyBiZXN0X3Nsb3BlOlxuICAgICAgICAgICAgYmVzdF9zbG9wZSwgYmVzdF9pZHggPSBzbG9wZSwgaVxuXG4gICAgcHJpbnQoXHUwMDI3TFIgcmFuZ2UgdGVzdCBjb21wbGV0ZSAoJWQgc3RlcHMpLlx1MDAyNyAlIG51bV9zdGVwcylcbiAgICBwcmludChcdTAwMjdTdGVlcGVzdCBkZXNjZW50IGF0IGxyOiAlLjJlXHUwMDI3ICUgbHJzW2Jlc3RfaWR4XSlcbiAgICBwcmludChcdTAwMjdTdWdnZXN0ZWQgdHJhaW5pbmcgbHI6ICAlLjJlICAoMTB4IGJlbG93IHN0ZWVwZXN0KVx1MDAyNyAlIChscnNbYmVzdF9pZHhdLzEwKSlcbiAgICByZXR1cm4gbHJzLCBsb3NzZXMsIGxyc1tiZXN0X2lkeF0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXU0QgU2NoZWR1bGUgZm9yIExMTSBQcmV0cmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFdhcm11cC1TdGFibGUtRGVjYXkgKFdTRCkgc2NoZWR1bGUgaXMgZmF2b3JlZCBmb3IgTExNIHByZXRyYWluaW5nIChNaW5pQ1BNLCBMbGFtYSAzIHZhcmlhbnRzKS4gSXQgaGFzIHRocmVlIHBoYXNlczogKDEpIGxpbmVhciB3YXJtdXAgdG8gcGVhayBMUiwgKDIpIGhvbGQgTFIgY29uc3RhbnQgZm9yIHRoZSBidWxrIG9mIHRyYWluaW5nIChzdGFibGUgcGhhc2UpLCAoMykgY29zaW5lIGRlY2F5IHRvIG5lYXItemVyby4gVGhlIHN0YWJsZSBwaGFzZSBhbGxvd3MgY29udGludWVkIGRhdGEgc2NhbGluZyB3aXRob3V0IHRoZSBvdmVyaGVhZCBvZiBzY2hlZHVsaW5nLiBUaGUgc2hhcnAgZmluYWwgZGVjYXkgaXMgd2hhdCBwcm9kdWNlcyBtb3N0IG9mIHRoZSBsb3NzIGltcHJvdmVtZW50IGluIHRoZSBsYXN0IH4xMCUgb2YgdHJhaW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBtYXRoXG5cbmRlZiB3c2Rfc2NoZWR1bGUoc3RlcCwgVF93LCBUX3MsIFRfZCwgZXRhX21heCwgZXRhX21pbj0wLjApOlxuICAgICMgV2FybXVwLVN0YWJsZS1EZWNheSAoV1NEKSBzY2hlZHVsZVxuICAgICMgUGhhc2UgMSBbMCwgVF93KTogICAgICAgICAgbGluZWFyIHdhcm11cFxuICAgICMgUGhhc2UgMiBbVF93LCBUX3crVF9zKTogICBzdGFibGUgKGNvbnN0YW50IGF0IGV0YV9tYXgpXG4gICAgIyBQaGFzZSAzIFtUX3crVF9zLCB0b3RhbCk6IGNvc2luZSBkZWNheSB0byBldGFfbWluXG4gICAgaWYgc3RlcCBcdTAwM2MgVF93OlxuICAgICAgICByZXR1cm4gZXRhX21heCAqIHN0ZXAgLyBtYXgoVF93LCAxKVxuICAgIGVsaWYgc3RlcCBcdTAwM2MgVF93ICsgVF9zOlxuICAgICAgICByZXR1cm4gZXRhX21heFxuICAgIGVsc2U6XG4gICAgICAgIHQgPSBzdGVwIC0gVF93IC0gVF9zXG4gICAgICAgIHJldHVybiBldGFfbWluICsgKGV0YV9tYXggLSBldGFfbWluKSAqIDAuNSAqICgxICsgbWF0aC5jb3MobWF0aC5waSAqIHQgLyBtYXgoVF9kLCAxKSkpXG5cbiMgVHlwaWNhbCBMTE0gcHJldHJhaW5pbmcgYnVkZ2V0OiAxMDBrIHN0ZXBzXG5UX3csIFRfcywgVF9kID0gMTAwMCwgODkwMDAsIDEwMDAwXG5ldGFfbWF4ID0gM2UtNFxuZXRhX21pbiA9IDNlLTVcblRfdG90YWwgPSBUX3cgKyBUX3MgKyBUX2RcblxucHJpbnQoXHUwMDI3V1NEIHNjaGVkdWxlICglZCB0b3RhbCBzdGVwcyk6XHUwMDI3ICUgVF90b3RhbClcbnByaW50KFx1MDAyNyAgV2FybXVwOiAlZCAgU3RhYmxlOiAlZCAgRGVjYXk6ICVkXHUwMDI3ICUgKFRfdywgVF9zLCBUX2QpKVxucHJpbnQoXHUwMDI3XHUwMDI3KVxucHJpbnQoXHUwMDI3JS0xMHMgJS0xMnMgJXNcdTAwMjcgJSAoXHUwMDI3U3RlcFx1MDAyNywgXHUwMDI3TFJcdTAwMjcsIFx1MDAyN1BoYXNlXHUwMDI3KSlcbmZvciBzdGVwIGluIFswLCA1MDAsIDEwMDAsIDUwMDAsIDUwMDAwLCA4OTAwMCwgOTAwMDAsIDk1MDAwLCA5OTk5OV06XG4gICAgaWYgc3RlcCBcdTAwM2MgVF90b3RhbDpcbiAgICAgICAgbHIgPSB3c2Rfc2NoZWR1bGUoc3RlcCwgVF93LCBUX3MsIFRfZCwgZXRhX21heCwgZXRhX21pbilcbiAgICAgICAgaWYgc3RlcCBcdTAwM2MgVF93OlxuICAgICAgICAgICAgcGhhc2UgPSBcdTAwMjd3YXJtdXBcdTAwMjdcbiAgICAgICAgZWxpZiBzdGVwIFx1MDAzYyBUX3cgKyBUX3M6XG4gICAgICAgICAgICBwaGFzZSA9IFx1MDAyN3N0YWJsZVx1MDAyN1xuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgcGhhc2UgPSBcdTAwMjdkZWNheVx1MDAyN1xuICAgICAgICBwcmludChcdTAwMjclLTEwZCAlLTEyLjJlICVzXHUwMDI3ICUgKHN0ZXAsIGxyLCBwaGFzZSkpXG5wcmludChcdTAwMjdcdTAwMjcpXG5wcmludChcdTAwMjdNb3N0IGNvbXB1dGUgYnVkZ2V0IGluIHN0YWJsZSBwaGFzZTsgZGVjYXkgZGVsaXZlcnMgZmluYWwgY29udmVyZ2VuY2UuXHUwMDI3KSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJTY2hlZHVsZSIsIkZvcm11bGEgLyBTaGFwZSIsIktleSBIeXBlcnBhcmFtZXRlcnMiLCJCZXN0IEZvciJdLCJyb3dzIjpbWyJDb25zdGFudCIsIs63KHQpID0gzrfigoAiLCLOt+KCgCIsIlByb3RvdHlwaW5nLCBSTCBiYXNlbGluZXMiXSxbIlN0ZXAgZGVjYXkiLCLOt+KCgCDCtyDOs17ijIp0L3N0ZXBfc2l6ZeKMiyIsIs634oKALCDOsywgc3RlcF9zaXplIiwiUmVzTmV0cywgQ1YgdHJhaW5pbmciXSxbIkNvc2luZSBhbm5lYWxpbmciLCLOt19taW4gKyAozrdfbWF44oiSzrdfbWluKS8ywrcoMStjb3Moz4B0L1QpKSIsIs63X21pbiwgzrdfbWF4LCBUIiwiTW9zdCBkZWVwIGxlYXJuaW5nIHRhc2tzIl0sWyIxLUN5Y2xlIiwiV2FybXVwIOKGkiBwZWFrIOKGkiBjb3NpbmUgZGVjYXkiLCJtYXhfbHIsIHBjdF9zdGFydCIsIkZhc3QgdHJhaW5pbmcsIHN1cGVyLWNvbnZlcmdlbmNlIl0sWyJXU0QiLCJMaW5lYXIgd2FybXVwIOKGkiBzdGFibGUg4oaSIGNvc2luZSBkZWNheSIsIs63X21heCwgVF93LCBUX3MsIFRfZCIsIkxMTSBwcmV0cmFpbmluZyBhdCBzY2FsZSJdLFsiQ3ljbGljYWwgTFIiLCJSZXBlYXRlZCB0cmlhbmdsZSB3YXZlcyIsImJhc2VfbHIsIG1heF9sciwgc3RlcF9zaXplIiwiRXNjYXBpbmcgc2hhcnAgbWluaW1hIl0sWyJSZWR1Y2VMUk9uUGxhdGVhdSIsIkRlY2F5IHdoZW4gbWV0cmljIHN0b3BzIGltcHJvdmluZyIsImZhY3RvciwgcGF0aWVuY2UiLCJGaW5lLXR1bmluZywgdW5rbm93biBidWRnZXRzIl1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiTFIgRmluZGVyIEJlZm9yZSBDb21taXR0aW5nIHRvIGEgRnVsbCBSdW4iLCJjb250ZW50IjoiQWx3YXlzIHJ1biBhIDEwMC1zdGVwIExSIHJhbmdlIHRlc3QgYmVmb3JlIGEgZnVsbCB0cmFpbmluZyBydW4uIFNldCB5b3VyIHRyYWluaW5nIExSIHRvIOKJiDEvMTAgb2YgdGhlIExSIHdoZXJlIGxvc3Mgc3RhcnRzIGRpdmVyZ2luZy4gRm9yIEFkYW0vQWRhbVcsIHR5cGljYWwgb3B0aW1hbCBMUnMgZmFsbCBpbiBbMWUtNCwgM2UtM107IGZvciBMaW9uLCBkaXZpZGUgYnkgMTA7IGZvciBTR0Qgd2l0aCBtb21lbnR1bSwgdGhlIHJhbmdlIGlzIG11Y2ggd2lkZXIgKDAuMDHigJMwLjEpLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkN5Y2xpY2FsIExSIGFuZCBTdXBlci1Db252ZXJnZW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ3ljbGljYWwgbGVhcm5pbmcgcmF0ZXMgKENMUiwgU21pdGggMjAxNykgb3NjaWxsYXRlIGJldHdlZW4gYmFzZV9sciBhbmQgbWF4X2xyIHdpdGggYSBmaXhlZCBjeWNsZSBsZW5ndGguIFRoZSBwZXJpb2RpYyBpbmNyZWFzZSBsZXRzIHRoZSBvcHRpbWl6ZXIgZXNjYXBlIHNoYXJwIG1pbmltYSAod2hpY2ggb2Z0ZW4gaGF2ZSBuYXJyb3cgYmFzaW5zKS4gU3VwZXItY29udmVyZ2VuY2UgaXMgdGhlIGVtcGlyaWNhbCBmaW5kaW5nIHRoYXQgQ0xSIHdpdGggYSBsYXJnZSBtYXhfbHIgY2FuIGNvbnZlcmdlIHRvIGdvb2Qgc29sdXRpb25zIGluIDUtMTDDlyBmZXdlciBzdGVwcyB0aGFuIHN0ZXAgZGVjYXksIGF0IGxlYXN0IGZvciBzb21lIGFyY2hpdGVjdHVyZXMgYW5kIGRhdGFzZXRzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQ0xSIGN5Y2xlcyBiZXR3ZWVuIGJhc2VfbHIgYW5kIG1heF9sciDigJQgcGVyaW9kaWMgTFIgaW5jcmVhc2VzIGhlbHAgZXNjYXBlIHNoYXJwIG1pbmltYSIsIlN1cGVyLWNvbnZlcmdlbmNlOiAxLWN5Y2xlIHdpdGggbGFyZ2UgbWF4X2xyIGNhbiB0cmFpbiBSZXNOZXRzIGluIFx1MDAzYzEwIGVwb2NocyAodnMgMTAwKykiLCJDb3NpbmUgYW5uZWFsaW5nIHdpdGggd2FybSByZXN0YXJ0cyAoU0dEUik6IHJlc3RhcnQgY3ljbGUgYXQgVF9pLCBkb3VibGUgcGVyaW9kIGVhY2ggcmVzdGFydCIsIldTRDogc3RhYmxlIHBoYXNlIGVuYWJsZXMgY29udGludWVkIHRyYWluaW5nIHdpdGhvdXQgc2NoZWR1bGUgZW5naW5lZXJpbmciLCJGb3IgTExNczogV1NEIG91dHBlcmZvcm1zIGNvc2luZSBkZWNheSBvbiB0aGUgbG9uZ2VzdCB0cmFpbmluZyBydW5zICgxMDBrKyBzdGVwcykiLCJSZWR1Y2VMUk9uUGxhdGVhdTogYWRhcHRpdmUgc2NoZWR1bGUgYmFzZWQgb24gdmFsaWRhdGlvbiBtZXRyaWMg4oCUIHVzZWZ1bCBmb3IgZmluZS10dW5pbmciXX0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTm8gc2luZ2xlIHNjaGVkdWxlIGlzIHVuaXZlcnNhbGx5IG9wdGltYWwuIFRoZSByaWdodCBzY2hlZHVsZSBkZXBlbmRzIG9uIHRyYWluaW5nIGR1cmF0aW9uLCBiYXRjaCBzaXplIChsYXJnZXIgYmF0Y2hlcyBuZWVkIGhpZ2hlciBMUiBieSB0aGUgbGluZWFyIHNjYWxpbmcgcnVsZSksIG9wdGltaXplciAoQWRhbSB2cyBTR0QgdnMgTGlvbiksIGFuZCB3aGV0aGVyIHlvdSBoYXZlIGEgZml4ZWQgY29tcHV0ZSBidWRnZXQuIFRoZSBMUiBmaW5kZXIsIGNvbWJpbmVkIHdpdGggV1NEIG9yIGNvc2luZSBhbm5lYWxpbmcsIGNvdmVycyB0aGUgbWFqb3JpdHkgb2YgcHJhY3RpY2FsIHRyYWluaW5nIHNjZW5hcmlvcy4ifV0="
---
# Learning Rate Schedules

The learning rate is the single most important optimizer hyperparameter, yet a constant LR is almost never optimal. Modern training recipes combine a warmup phase (ramp from near-zero to peak LR), a main training phase, and a decay phase. Understanding why each phase exists — and how to find the right peak LR — is essential for training stable, well-converged models.

## Why Constant LR Fails

A constant LR that is too large causes divergence (loss spikes, NaN) because gradient steps overshoot the loss surface. A constant LR that is too small converges slowly and may land in a sharp, poorly generalizing minimum. Schedules combine a large LR early (to escape bad initialization) with a small LR late (to settle into a smooth minimum).

## Linear Warmup: Why It Matters

In Adam, the second moment v̂ = v/(1-β₂ᵗ) is near zero at initialization — Adam's bias correction compensates, but in practice early steps can still be large and unstable. Warmup starts at lr=0 (or a small fraction) and ramps linearly to peak_lr over warmup_steps. This lets v̂ stabilize before taking large steps, and avoids catastrophic early updates that can destroy freshly initialized weights.

> **How Long to Warm Up**: Typical warmup is 1–5% of total training steps. For LLM pretraining at 100k steps: 1000–5000 warmup steps. For fine-tuning short runs: 50–100 steps. Longer warmup is safer but delays reaching peak LR. The WSD schedule uses a fixed warmup of ~1% and then holds the LR stable for most of training.

## Cosine Annealing

Cosine annealing smoothly decays the LR: η(t) = η_min + (η_max − η_min)/2 · (1 + cos(πt/T)). At t=0 it equals η_max; at t=T it equals η_min. The smooth decay avoids the abrupt LR drops of step decay, which can cause sudden loss changes. Cosine annealing with warm restarts (SGDR) periodically resets t to 0, allowing the model to escape local minima.

```python
import numpy as np
import math

def cosine_anneal(step, T, eta_max=1e-3, eta_min=1e-6):
    # eta(t) = eta_min + (eta_max - eta_min)/2 * (1 + cos(pi*t/T))
    return eta_min + (eta_max - eta_min) * 0.5 * (1.0 + math.cos(math.pi * step / T))

def warmup_cosine(step, warmup, total, eta_max=1e-3, eta_min=1e-6):
    # Phase 1: linear warmup  [0, warmup)
    # Phase 2: cosine decay   [warmup, total]
    if step < warmup:
        return eta_max * step / max(warmup, 1)
    progress = (step - warmup) / max(total - warmup, 1)
    return eta_min + (eta_max - eta_min) * 0.5 * (1.0 + math.cos(math.pi * progress))

total, warmup = 1000, 100

print('Warmup + cosine annealing schedule:')
print('%-6s  %-12s  %s' % ('Step', 'LR', 'Bar'))
for t in [0, 25, 50, 100, 200, 400, 600, 800, 999]:
    lr  = warmup_cosine(t, warmup, total)
    bar = '#' * int(lr / 1e-3 * 30)
    print('%6d  %.4e    %s' % (t, lr, bar))

lrs = [warmup_cosine(t, warmup, total) for t in range(total)]
print('')
print('Peak LR: %.2e  |  Final LR: %.2e' % (max(lrs), lrs[-1]))
print('Warmup: %d steps  |  Cosine decay: %d steps' % (warmup, total - warmup))
```

## The 1-Cycle Policy

The 1-cycle policy (Smith 2017) uses a triangular LR schedule: ramp up from base_lr to max_lr over pct_start fraction of training, then decay from max_lr back to base_lr/div_factor. A final phase decays to base_lr/final_div_factor. This enables 'super-convergence' — training in far fewer iterations than step decay. PyTorch provides OneCycleLR out of the box.

```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(10, 2)
optimizer = optim.AdamW(model.parameters(), lr=1e-3)

# 1. OneCycleLR: warmup -> peak -> cosine anneal
one_cycle = optim.lr_scheduler.OneCycleLR(
    optimizer,
    max_lr=1e-2,
    total_steps=1000,
    pct_start=0.1,           # 10% warmup
    anneal_strategy='cos',
    div_factor=25,            # start lr = max_lr / 25
    final_div_factor=1e4      # end lr = start_lr / 1e4
)

# 2. CosineAnnealingLR
cos_sched = optim.lr_scheduler.CosineAnnealingLR(
    optimizer, T_max=1000, eta_min=1e-6)

# 3. Linear warmup -> Cosine decay (SequentialLR)
warmup_sched = optim.lr_scheduler.LinearLR(
    optimizer, start_factor=0.01, end_factor=1.0, total_iters=100)
cosine_sched = optim.lr_scheduler.CosineAnnealingLR(
    optimizer, T_max=900, eta_min=1e-6)
seq_sched = optim.lr_scheduler.SequentialLR(
    optimizer, schedulers=[warmup_sched, cosine_sched], milestones=[100])

print('Scheduler types available in torch.optim.lr_scheduler:')
schedulers = ['StepLR', 'MultiStepLR', 'CosineAnnealingLR', 'OneCycleLR',
              'CosineAnnealingWarmRestarts', 'ReduceLROnPlateau',
              'LinearLR', 'SequentialLR', 'ChainedScheduler']
for s in schedulers:
    print('  -', s)
```

## Learning Rate Finder (Range Test)

The LR range test (Smith 2015) sweeps the LR log-linearly from a tiny value (1e-7) to a large value (10), training for one step per LR value. The loss initially decreases, reaches a minimum, then explodes. The optimal LR for training is roughly one order of magnitude below the LR where loss starts to diverge.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import math

def lr_range_test(model, loss_fn, data_iter, start_lr=1e-7,
                  end_lr=10.0, num_steps=100):
    # Sweep lr log-linearly; record loss at each step
    lrs, losses = [], []
    lr = start_lr
    factor = (end_lr / start_lr) ** (1.0 / num_steps)

    opt = optim.SGD(model.parameters(), lr=lr, momentum=0.9)

    for step, (x, y) in enumerate(data_iter):
        if step >= num_steps:
            break
        for pg in opt.param_groups:
            pg['lr'] = lr
        pred = model(x)
        loss = loss_fn(pred, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
        lrs.append(lr)
        losses.append(loss.item())
        lr *= factor

    # Find steepest negative slope
    best_idx, best_slope = 1, 0
    for i in range(1, len(losses) - 1):
        slope = losses[i+1] - losses[i-1]
        if slope < best_slope:
            best_slope, best_idx = slope, i

    print('LR range test complete (%d steps).' % num_steps)
    print('Steepest descent at lr: %.2e' % lrs[best_idx])
    print('Suggested training lr:  %.2e  (10x below steepest)' % (lrs[best_idx]/10))
    return lrs, losses, lrs[best_idx]
```

## WSD Schedule for LLM Pretraining

The Warmup-Stable-Decay (WSD) schedule is favored for LLM pretraining (MiniCPM, Llama 3 variants). It has three phases: (1) linear warmup to peak LR, (2) hold LR constant for the bulk of training (stable phase), (3) cosine decay to near-zero. The stable phase allows continued data scaling without the overhead of scheduling. The sharp final decay is what produces most of the loss improvement in the last ~10% of training.

```python
import math

def wsd_schedule(step, T_w, T_s, T_d, eta_max, eta_min=0.0):
    # Warmup-Stable-Decay (WSD) schedule
    # Phase 1 [0, T_w):          linear warmup
    # Phase 2 [T_w, T_w+T_s):   stable (constant at eta_max)
    # Phase 3 [T_w+T_s, total): cosine decay to eta_min
    if step < T_w:
        return eta_max * step / max(T_w, 1)
    elif step < T_w + T_s:
        return eta_max
    else:
        t = step - T_w - T_s
        return eta_min + (eta_max - eta_min) * 0.5 * (1 + math.cos(math.pi * t / max(T_d, 1)))

# Typical LLM pretraining budget: 100k steps
T_w, T_s, T_d = 1000, 89000, 10000
eta_max = 3e-4
eta_min = 3e-5
T_total = T_w + T_s + T_d

print('WSD schedule (%d total steps):' % T_total)
print('  Warmup: %d  Stable: %d  Decay: %d' % (T_w, T_s, T_d))
print('')
print('%-10s %-12s %s' % ('Step', 'LR', 'Phase'))
for step in [0, 500, 1000, 5000, 50000, 89000, 90000, 95000, 99999]:
    if step < T_total:
        lr = wsd_schedule(step, T_w, T_s, T_d, eta_max, eta_min)
        if step < T_w:
            phase = 'warmup'
        elif step < T_w + T_s:
            phase = 'stable'
        else:
            phase = 'decay'
        print('%-10d %-12.2e %s' % (step, lr, phase))
print('')
print('Most compute budget in stable phase; decay delivers final convergence.')
```

| Schedule | Formula / Shape | Key Hyperparameters | Best For |
| --- | --- | --- | --- |
| Constant | η(t) = η₀ | η₀ | Prototyping, RL baselines |
| Step decay | η₀ · γ^⌊t/step_size⌋ | η₀, γ, step_size | ResNets, CV training |
| Cosine annealing | η_min + (η_max−η_min)/2·(1+cos(πt/T)) | η_min, η_max, T | Most deep learning tasks |
| 1-Cycle | Warmup → peak → cosine decay | max_lr, pct_start | Fast training, super-convergence |
| WSD | Linear warmup → stable → cosine decay | η_max, T_w, T_s, T_d | LLM pretraining at scale |
| Cyclical LR | Repeated triangle waves | base_lr, max_lr, step_size | Escaping sharp minima |
| ReduceLROnPlateau | Decay when metric stops improving | factor, patience | Fine-tuning, unknown budgets |

> **LR Finder Before Committing to a Full Run**: Always run a 100-step LR range test before a full training run. Set your training LR to ≈1/10 of the LR where loss starts diverging. For Adam/AdamW, typical optimal LRs fall in [1e-4, 3e-3]; for Lion, divide by 10; for SGD with momentum, the range is much wider (0.01–0.1).

## Cyclical LR and Super-Convergence

Cyclical learning rates (CLR, Smith 2017) oscillate between base_lr and max_lr with a fixed cycle length. The periodic increase lets the optimizer escape sharp minima (which often have narrow basins). Super-convergence is the empirical finding that CLR with a large max_lr can converge to good solutions in 5-10× fewer steps than step decay, at least for some architectures and datasets.

- CLR cycles between base_lr and max_lr — periodic LR increases help escape sharp minima
- Super-convergence: 1-cycle with large max_lr can train ResNets in <10 epochs (vs 100+)
- Cosine annealing with warm restarts (SGDR): restart cycle at T_i, double period each restart
- WSD: stable phase enables continued training without schedule engineering
- For LLMs: WSD outperforms cosine decay on the longest training runs (100k+ steps)
- ReduceLROnPlateau: adaptive schedule based on validation metric — useful for fine-tuning

---

No single schedule is universally optimal. The right schedule depends on training duration, batch size (larger batches need higher LR by the linear scaling rule), optimizer (Adam vs SGD vs Lion), and whether you have a fixed compute budget. The LR finder, combined with WSD or cosine annealing, covers the majority of practical training scenarios.

