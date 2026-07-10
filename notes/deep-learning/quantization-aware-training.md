---
title: "Quantization — PTQ, QAT, and W4A16 for LLMs"
slug: "quantization-aware-training"
description: "Reduce model precision from FP32 to INT8 or INT4. Covers symmetric and asymmetric quantization, per-channel scale, post-training quantization (PTQ), quantization-aware training (QAT) with straight-through estimator, LLM.int8, GPTQ, and bitsandbytes 4-bit loading."
tags: ["deep-learning", "model-compression", "pruning", "quantization"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUXVhbnRpemF0aW9uIG1hcHMgZmxvYXRpbmctcG9pbnQgd2VpZ2h0cyBhbmQvb3IgYWN0aXZhdGlvbnMgdG8gbG93ZXItcHJlY2lzaW9uIGludGVnZXJzLiBBIEZQMzIgd2VpZ2h0IGNvbnN1bWVzIDQgYnl0ZXM7IGFuIElOVDggd2VpZ2h0IGNvbnN1bWVzIDEgYnl0ZTsgYW4gSU5UNCB3ZWlnaHQgY29uc3VtZXMgMC41IGJ5dGVzLiBNZW1vcnkgYmFuZHdpZHRoIGlzIG9mdGVuIHRoZSBwcmltYXJ5IGJvdHRsZW5lY2sgZm9yIExMTSBpbmZlcmVuY2Ug4oCUIHF1YW50aXppbmcgd2VpZ2h0cyA0w5cgcmVkdWNlcyB0aGUgYnl0ZXMgdHJhbnNmZXJyZWQgcGVyIHRva2VuLCBkaXJlY3RseSBhY2NlbGVyYXRpbmcgZ2VuZXJhdGlvbi4gUXVhbnRpemF0aW9uIGFsc28gZW5hYmxlcyBkZXBsb3ltZW50IG9uIGhhcmR3YXJlIHdpdGhvdXQgRlAzMiBzdXBwb3J0IChtaWNyb2NvbnRyb2xsZXJzLCBtb2JpbGUgTlBVcykuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3ltbWV0cmljIGFuZCBBc3ltbWV0cmljIFF1YW50aXphdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3ltbWV0cmljIHF1YW50aXphdGlvbjogcSh4KSA9IGNsYW1wKHJvdW5kKHggLyBzY2FsZSksIC0yXihiLTEpLCAyXihiLTEpLTEpIHdoZXJlIHNjYWxlID0gbWF4KHx4fCkgLyAyXihiLTEpLiBEZXF1YW50aXplOiB4zIIgPSBxIMK3IHNjYWxlLiBGb3IgSU5UODogcmFuZ2UgaXMgWy0xMjgsIDEyN10sIHNjYWxlID0gbWF4fHh8LzEyNy4gQXN5bW1ldHJpYyBhZGRzIGEgemVyby1wb2ludCB6OiBxKHgpID0gY2xhbXAocm91bmQoeC9zY2FsZSArIHopLCAwLCAyXmItMSksIHjMgiA9IChxLXopwrdzY2FsZS4gQXN5bW1ldHJpYyBjb3ZlcnMgbm9uLXN5bW1ldHJpYyBkaXN0cmlidXRpb25zIChSZUxVIG91dHB1dHMgYXJlIGFsd2F5cyBub24tbmVnYXRpdmUpIGJ1dCBhZGRzIHplcm8tcG9pbnQgb3ZlcmhlYWQuIFBlci10ZW5zb3IgcXVhbnRpemF0aW9uIHVzZXMgb25lIHNjYWxlIGZvciB0aGUgZW50aXJlIHRlbnNvcjsgcGVyLWNoYW5uZWwgdXNlcyBvbmUgc2NhbGUgcGVyIG91dHB1dCBjaGFubmVsLCBnaXZpbmcgc2lnbmlmaWNhbnRseSBiZXR0ZXIgYWNjdXJhY3kuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBzeW1tZXRyaWNfcXVhbnRpemUoeDogdG9yY2guVGVuc29yLCBiaXRzOiBpbnQgPSA4KTpcbiAgICBcIlwiXCJTeW1tZXRyaWMgcGVyLXRlbnNvciBxdWFudGl6YXRpb24uIFJldHVybnMgKHF1YW50aXplZF9pbnQsIHNjYWxlKS5cIlwiXCJcbiAgICBxbWF4ID0gMiAqKiAoYml0cyAtIDEpIC0gMSAgIyAxMjcgZm9yIElOVDhcbiAgICBzY2FsZSA9IHguYWJzKCkubWF4KCkgLyBxbWF4XG4gICAgc2NhbGUgPSBzY2FsZS5jbGFtcChtaW49MWUtOCkgICMgYXZvaWQgZGl2aXNpb24gYnkgemVyb1xuICAgIHEgPSAoeCAvIHNjYWxlKS5yb3VuZCgpLmNsYW1wKC1xbWF4IC0gMSwgcW1heClcbiAgICByZXR1cm4gcS50byh0b3JjaC5pbnQ4KSwgc2NhbGVcblxuZGVmIGRlcXVhbnRpemUocTogdG9yY2guVGVuc29yLCBzY2FsZTogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICByZXR1cm4gcS5mbG9hdCgpICogc2NhbGVcblxuZGVmIHBlcl9jaGFubmVsX3F1YW50aXplKHdlaWdodDogdG9yY2guVGVuc29yLCBiaXRzOiBpbnQgPSA4KTpcbiAgICBcIlwiXCJQZXIgb3V0cHV0LWNoYW5uZWwgc3ltbWV0cmljIHF1YW50aXphdGlvbiBmb3IgY29udi9saW5lYXIgd2VpZ2h0cy5cIlwiXCJcbiAgICBxbWF4ID0gMiAqKiAoYml0cyAtIDEpIC0gMVxuICAgICMgU2NhbGUgcGVyIG91dHB1dCBjaGFubmVsIChkaW0gMClcbiAgICBzY2FsZSA9IHdlaWdodC5hYnMoKS5hbWF4KGRpbT10dXBsZShyYW5nZSgxLCB3ZWlnaHQubmRpbSkpLCBrZWVwZGltPVRydWUpIC8gcW1heFxuICAgIHNjYWxlID0gc2NhbGUuY2xhbXAobWluPTFlLTgpXG4gICAgcSA9ICh3ZWlnaHQgLyBzY2FsZSkucm91bmQoKS5jbGFtcCgtcW1heCAtIDEsIHFtYXgpLnRvKHRvcmNoLmludDgpXG4gICAgcmV0dXJuIHEsIHNjYWxlXG5cbiMgQ29tcGFyZSBwZXItdGVuc29yIHZzIHBlci1jaGFubmVsIHF1YW50aXphdGlvbiBlcnJvclxudG9yY2gubWFudWFsX3NlZWQoMClcblcgPSB0b3JjaC5yYW5kbig2NCwgMzIpICAjIHNpbXVsYXRlIGEgbGluZWFyIGxheWVyIHdlaWdodFxuXG5xX3B0LCBzX3B0ID0gc3ltbWV0cmljX3F1YW50aXplKFcsIGJpdHM9OClcbldfaGF0X3B0ID0gZGVxdWFudGl6ZShxX3B0LCBzX3B0KVxuZXJyX3B0ID0gKFcgLSBXX2hhdF9wdCkuYWJzKCkubWVhbigpLml0ZW0oKVxuXG5xX3BjLCBzX3BjID0gcGVyX2NoYW5uZWxfcXVhbnRpemUoVywgYml0cz04KVxuV19oYXRfcGMgPSBkZXF1YW50aXplKHFfcGMsIHNfcGMuZXhwYW5kX2FzKFcpKVxuZXJyX3BjID0gKFcgLSBXX2hhdF9wYykuYWJzKCkubWVhbigpLml0ZW0oKVxuXG5wcmludChmXHUwMDI3UGVyLXRlbnNvciAgTUFFOiB7ZXJyX3B0Oi41Zn0gIHNjYWxlPXtzX3B0Lml0ZW0oKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1Blci1jaGFubmVsIE1BRToge2Vycl9wYzouNWZ9ICAob25lIHNjYWxlIHBlciByb3cpXHUwMDI3KVxucHJpbnQoZlx1MDAyN1Blci1jaGFubmVsIGlzIHtlcnJfcHQvZXJyX3BjOi4xZn14IG1vcmUgYWNjdXJhdGVcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUG9zdC1UcmFpbmluZyBRdWFudGl6YXRpb24gd2l0aCBDYWxpYnJhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUFRRIHJlcXVpcmVzIG5vIHJldHJhaW5pbmcuIEEgc21hbGwgY2FsaWJyYXRpb24gZGF0YXNldCAoMTAw4oCTMTAwMCBzYW1wbGVzKSBpcyBmb3J3YXJkZWQgdGhyb3VnaCB0aGUgbW9kZWwgdG8gZ2F0aGVyIGFjdGl2YXRpb24gc3RhdGlzdGljcyAobWluLCBtYXgsIG9yIHBlcmNlbnRpbGUpLiBUaGVzZSBzdGF0aXN0aWNzIGRldGVybWluZSB0aGUgcXVhbnRpemF0aW9uIHNjYWxlIGZvciBlYWNoIGxheWVyLiBBY3RpdmF0aW9uIG91dGxpZXJzIGluZmxhdGUgdGhlIHNjYWxlLCB3YXN0aW5nIHByZWNpc2lvbiBvbiByYXJlIGxhcmdlIHZhbHVlcy4gVGVjaG5pcXVlcyBsaWtlIFNtb290aFF1YW50IG1pZ3JhdGUgdGhlIHF1YW50aXphdGlvbiBkaWZmaWN1bHR5IGZyb20gYWN0aXZhdGlvbnMgdG8gd2VpZ2h0cyAod2hpY2ggYXJlIGVhc2llciB0byBxdWFudGl6ZSkgYnkgbXVsdGlwbHlpbmcgYWN0aXZhdGlvbiBzY2FsZXMgaW50byB0aGUgd2VpZ2h0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlF1YW50aXphdGlvbi1Bd2FyZSBUcmFpbmluZyAoUUFUKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUUFUIHNpbXVsYXRlcyBxdWFudGl6YXRpb24gZHVyaW5nIHRyYWluaW5nOiBpbiB0aGUgZm9yd2FyZCBwYXNzLCB3ZWlnaHRzIGFuZCBhY3RpdmF0aW9ucyBhcmUgZmFrZS1xdWFudGl6ZWQgKHF1YW50aXplIHRoZW4gZGVxdWFudGl6ZSwgc3RheWluZyBpbiBGUDMyIGR0eXBlKS4gVGhlIG1vZGVsIGxlYXJucyB0byBjb21wZW5zYXRlIGZvciBxdWFudGl6YXRpb24gZXJyb3IuIEdyYWRpZW50cyBmbG93IHRocm91Z2ggdGhlIGZha2UtcXVhbnRpemUgb3BlcmF0aW9uIHVzaW5nIHRoZSBzdHJhaWdodC10aHJvdWdoIGVzdGltYXRvciAoU1RFKTogdGhlIGdyYWRpZW50IG9mIHRoZSByb3VuZCBmdW5jdGlvbiBpcyB0cmVhdGVkIGFzIDEgd2l0aGluIHRoZSBjbGFtcCByYW5nZSBhbmQgMCBvdXRzaWRlLiBRQVQgdHlwaWNhbGx5IHJlY292ZXJzIDHigJMyJSBhY2N1cmFjeSBsb3N0IGJ5IFBUUSBhdCBJTlQ4LCBhbmQgaXMgZXNzZW50aWFsIGZvciBJTlQ0IHF1YW50aXphdGlvbiB3aGVyZSBQVFEgYWNjdXJhY3kgZGVncmFkZXMgc2lnbmlmaWNhbnRseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdG9yY2guYXV0b2dyYWQgaW1wb3J0IEZ1bmN0aW9uXG5cbmNsYXNzIEZha2VRdWFudGl6ZShGdW5jdGlvbik6XG4gICAgXCJcIlwiRmFrZSBxdWFudGl6YXRpb24gd2l0aCBzdHJhaWdodC10aHJvdWdoIGVzdGltYXRvci5cIlwiXCJcblxuICAgIEBzdGF0aWNtZXRob2RcbiAgICBkZWYgZm9yd2FyZChjdHgsIHg6IHRvcmNoLlRlbnNvciwgc2NhbGU6IGZsb2F0LCBiaXRzOiBpbnQgPSA4KTpcbiAgICAgICAgcW1heCA9IDIgKiogKGJpdHMgLSAxKSAtIDFcbiAgICAgICAgIyBRdWFudGl6ZSBhbmQgZGVxdWFudGl6ZSAoc3RheXMgZmxvYXQsIGJ1dCBoYXMgcXVhbnRpemF0aW9uIGVycm9yKVxuICAgICAgICBxID0gKHggLyBzY2FsZSkucm91bmQoKS5jbGFtcCgtcW1heCAtIDEsIHFtYXgpXG4gICAgICAgIHhfaGF0ID0gcSAqIHNjYWxlXG4gICAgICAgICMgU1RFOiBwYXNzIGdyYWRpZW50IHRocm91Z2ggY2xhbXAgcmVnaW9uLCB6ZXJvIG91dHNpZGVcbiAgICAgICAgY3R4LnNhdmVfZm9yX2JhY2t3YXJkKHgpXG4gICAgICAgIGN0eC5zY2FsZSA9IHNjYWxlXG4gICAgICAgIGN0eC5xbWF4ID0gcW1heFxuICAgICAgICByZXR1cm4geF9oYXRcblxuICAgIEBzdGF0aWNtZXRob2RcbiAgICBkZWYgYmFja3dhcmQoY3R4LCBncmFkX291dHB1dCk6XG4gICAgICAgIHgsID0gY3R4LnNhdmVkX3RlbnNvcnNcbiAgICAgICAgcW1heCA9IGN0eC5xbWF4XG4gICAgICAgIHNjYWxlID0gY3R4LnNjYWxlXG4gICAgICAgICMgU1RFOiBncmFkaWVudCA9IDEgd2hlcmUgeCBpcyBpbiBxdWFudGl6YXRpb24gcmFuZ2UsIGVsc2UgMFxuICAgICAgICBpbl9yYW5nZSA9ICgoeCAvIHNjYWxlKSBcdTAwM2U9IC0ocW1heCArIDEpKSBcdTAwMjYgKCh4IC8gc2NhbGUpIFx1MDAzYz0gcW1heClcbiAgICAgICAgZ3JhZF9pbnB1dCA9IGdyYWRfb3V0cHV0ICogaW5fcmFuZ2UuZmxvYXQoKVxuICAgICAgICByZXR1cm4gZ3JhZF9pbnB1dCwgTm9uZSwgTm9uZSAgIyBOb25lIGZvciBzY2FsZSBhbmQgYml0c1xuXG5jbGFzcyBRQVRMaW5lYXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fZmVhdHVyZXMsIG91dF9mZWF0dXJlcywgYml0cz04KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubGluZWFyID0gbm4uTGluZWFyKGluX2ZlYXR1cmVzLCBvdXRfZmVhdHVyZXMpXG4gICAgICAgIHNlbGYuYml0cyA9IGJpdHNcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgICMgRmFrZS1xdWFudGl6ZSB3ZWlnaHRzXG4gICAgICAgIFcgPSBzZWxmLmxpbmVhci53ZWlnaHRcbiAgICAgICAgc2NhbGVfdyA9IFcuYWJzKCkubWF4KCkuaXRlbSgpIC8gKDIgKiogKHNlbGYuYml0cyAtIDEpIC0gMSlcbiAgICAgICAgV19mcSA9IEZha2VRdWFudGl6ZS5hcHBseShXLCBzY2FsZV93LCBzZWxmLmJpdHMpXG4gICAgICAgIHJldHVybiBubi5mdW5jdGlvbmFsLmxpbmVhcih4LCBXX2ZxLCBzZWxmLmxpbmVhci5iaWFzKVxuXG4jIFZlcmlmeSBncmFkaWVudCBmbG93cyB0aHJvdWdoIGZha2UgcXVhbnRpemVcbmxheWVyID0gUUFUTGluZWFyKDMyLCAxNiwgYml0cz04KVxueCA9IHRvcmNoLnJhbmRuKDQsIDMyKVxubG9zcyA9IGxheWVyKHgpLnN1bSgpXG5sb3NzLmJhY2t3YXJkKClcbnByaW50KGZcdTAwMjdXZWlnaHQgZ3JhZCBub3JtOiB7bGF5ZXIubGluZWFyLndlaWdodC5ncmFkLm5vcm0oKS5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN0dyYWRpZW50IGZsb3dzIHRocm91Z2ggZmFrZSBxdWFudGl6ZSB2aWEgU1RFLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMTE0gUXVhbnRpemF0aW9uIOKAlCBHUFRRIGFuZCBXNEExNiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIExMTXMgd2l0aCBiaWxsaW9ucyBvZiBwYXJhbWV0ZXJzLCBRQVQgaXMgaW5mZWFzaWJsZSAocmV0cmFpbmluZyBjb3N0cykuIEdQVFEgKEZyYW50YXIgZXQgYWwuIDIwMjIpIGRvZXMgd2VpZ2h0LW9ubHkgcXVhbnRpemF0aW9uOiB3ZWlnaHRzIGFyZSBxdWFudGl6ZWQgdG8gSU5UNCAoVzQpLCBhY3RpdmF0aW9ucyByZW1haW4gRlAxNiAoQTE2KS4gR1BUUSBzb2x2ZXMgYSBsYXllci13aXNlIHJlY29uc3RydWN0aW9uIHByb2JsZW0gdXNpbmcgdGhlIEhlc3NpYW4gb2YgdGhlIGxheWVyXHUwMDI3cyBvdXRwdXQgd2l0aCByZXNwZWN0IHRvIGl0cyB3ZWlnaHRzICh2aWEgdGhlIE9wdGltYWwgQnJhaW4gU3VyZ2VvbiBmcmFtZXdvcmspLiBUaGlzIHByb2R1Y2VzIElOVDQgd2VpZ2h0cyB0aGF0IG1pbmltaXplIHRoZSBpbmNyZWFzZSBpbiBsYXllciBvdXRwdXQgZXJyb3IsIHJlY292ZXJpbmcgY2xvc2UgdG8gRlAxNiBhY2N1cmFjeSB3aXRob3V0IGFueSBncmFkaWVudCBjb21wdXRhdGlvbi4gTExNLmludDggKERldHRtZXJzIDIwMjIpIGhhbmRsZXMgYWN0aXZhdGlvbiBvdXRsaWVycyB2aWEgbWl4ZWQgcHJlY2lzaW9uOiBsYXJnZSBvdXRsaWVyIHJvd3MgaW4gdGhlIGFjdGl2YXRpb24gbWF0cml4IGFyZSBrZXB0IGluIEZQMTYgYW5kIG11bHRpcGxpZWQgc2VwYXJhdGVseSwgd2hpbGUgdGhlIG1ham9yaXR5IG9mIHRoZSBtYXRyaXggaXMgcXVhbnRpemVkIHRvIElOVDguIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6IiMgUmVxdWlyZXM6IHBpcCBpbnN0YWxsIGJpdHNhbmRieXRlcyB0cmFuc2Zvcm1lcnNcbmltcG9ydCB0b3JjaFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Nb2RlbEZvckNhdXNhbExNLCBBdXRvVG9rZW5pemVyLCBCaXRzQW5kQnl0ZXNDb25maWdcblxuZGVmIGxvYWRfbW9kZWxfNGJpdChtb2RlbF9uYW1lOiBzdHIgPSBcdTAwMjdmYWNlYm9vay9vcHQtMTI1bVx1MDAyNyk6XG4gICAgXCJcIlwiTG9hZCBhIGNhdXNhbCBMTSBpbiA0LWJpdCB1c2luZyBiaXRzYW5kYnl0ZXMgTkY0IHF1YW50aXphdGlvbi5cIlwiXCJcbiAgICBibmJfY29uZmlnID0gQml0c0FuZEJ5dGVzQ29uZmlnKFxuICAgICAgICBsb2FkX2luXzRiaXQ9VHJ1ZSxcbiAgICAgICAgYm5iXzRiaXRfcXVhbnRfdHlwZT1cdTAwMjduZjRcdTAwMjcsICAgICAgICAgIyBOb3JtYWxGbG9hdDQg4oCUIG9wdGltYWwgZm9yIG5vcm1hbGx5IGRpc3RyaWJ1dGVkIHdlaWdodHNcbiAgICAgICAgYm5iXzRiaXRfY29tcHV0ZV9kdHlwZT10b3JjaC5mbG9hdDE2LCAgIyBhY3RpdmF0aW9ucyBpbiBGUDE2XG4gICAgICAgIGJuYl80Yml0X3VzZV9kb3VibGVfcXVhbnQ9VHJ1ZSwgICAgIyBxdWFudGl6ZSB0aGUgcXVhbnRpemF0aW9uIGNvbnN0YW50cyB0b29cbiAgICApXG4gICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSlcbiAgICBtb2RlbCA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcbiAgICAgICAgbW9kZWxfbmFtZSxcbiAgICAgICAgcXVhbnRpemF0aW9uX2NvbmZpZz1ibmJfY29uZmlnLFxuICAgICAgICBkZXZpY2VfbWFwPVx1MDAyN2F1dG9cdTAwMjcsXG4gICAgKVxuICAgICMgUmVwb3J0IG1lbW9yeVxuICAgIG1lbV9tYiA9IHN1bShwLm51bWVsKCkgKiBwLmVsZW1lbnRfc2l6ZSgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSkgLyAxMDI0KioyXG4gICAgbl9wYXJhbXMgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSkgLyAxZTZcbiAgICBwcmludChmXHUwMDI3TW9kZWw6IHttb2RlbF9uYW1lfSAgUGFyYW1zOiB7bl9wYXJhbXM6LjFmfU0gIEFwcHJveCBtZW1vcnk6IHttZW1fbWI6LjBmfSBNQlx1MDAyNylcbiAgICBwcmludChmXHUwMDI3UXVhbnRpemF0aW9uOiBXNEExNiAoTkY0IHdlaWdodHMsIEZQMTYgYWN0aXZhdGlvbnMpXHUwMDI3KVxuICAgIHJldHVybiBtb2RlbCwgdG9rZW5pemVyXG5cbiMgRXhwZWN0ZWQgb3V0cHV0IGZvciBPUFQtMTI1TTpcbiMgUGFyYW1zOiAxMjUuME0gIEFwcHJveCBtZW1vcnk6IH42MyBNQiAodnMgNDc3IE1CIEZQMzIpXG5wcmludChcdTAwMjdMb2FkIHdpdGg6IG1vZGVsLCB0b2sgPSBsb2FkX21vZGVsXzRiaXQoXCJmYWNlYm9vay9vcHQtMTI1bVwiKVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6Ik5GNCB2cyBJTlQ0IGZvciBMTE0gV2VpZ2h0cyIsImNvbnRlbnQiOiJOb3JtYWxGbG9hdDQgKE5GNCkgaXMgYSBkYXRhIHR5cGUgb3B0aW1pemVkIGZvciBub3JtYWxseSBkaXN0cmlidXRlZCB3ZWlnaHRzOiB0aGUgMTYgcXVhbnRpemF0aW9uIGxldmVscyBhcmUgc3BhY2VkIGF0IGVxdWFsIHF1YW50aWxlcyBvZiB0aGUgc3RhbmRhcmQgbm9ybWFsIGRpc3RyaWJ1dGlvbiwgbm90IHVuaWZvcm1seS4gU2luY2UgcHJlLXRyYWluZWQgTExNIHdlaWdodHMgYXJlIGFwcHJveGltYXRlbHkgbm9ybWFsbHkgZGlzdHJpYnV0ZWQsIE5GNCB1c2VzIGl0cyA0IGJpdHMgbW9yZSBlZmZpY2llbnRseSB0aGFuIHVuaWZvcm0gSU5UNCwgdHlwaWNhbGx5IHJlY292ZXJpbmcgMC4x4oCTMC41IHBlcnBsZXhpdHkgcG9pbnRzIGF0IHRoZSBzYW1lIGJpdC13aWR0aC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJRdWFudGl6YXRpb24gRm9ybWF0IENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRm9ybWF0IiwiTWVtb3J5ICg3QiBtb2RlbCkiLCJJbmZlcmVuY2UgU3BlZWR1cCIsIkFjY3VyYWN5IExvc3MiLCJQVFEgdnMgUUFUIiwiQmVzdCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJGUDMyIiwiMjggR0IiLCIxw5cgYmFzZWxpbmUiLCJOb25lIiwiTi9BIiwiVHJhaW5pbmcsIHJlc2VhcmNoIl0sWyJGUDE2IC8gQkYxNiIsIjE0IEdCIiwiMS414oCTMsOXIChUZW5zb3IgQ29yZSkiLCJOZWdsaWdpYmxlIiwiTi9BIiwiVHJhaW5pbmcgKyBpbmZlcmVuY2UiXSxbIklOVDggKFc4QTgpIiwiNyBHQiIsIjLigJMzw5cgKElOVDggR0VNTSkiLCItMC4xIHRvIC0wLjUlIiwiUFRRIHdpdGggY2FsaWJyYXRpb24iLCJQcm9kdWN0aW9uIGluZmVyZW5jZSwgQ05OcyJdLFsiVzhBMTYgKExMTS5pbnQ4KSIsIjcgR0IiLCIxLjXDlyAoYmFuZHdpZHRoIGJvdW5kKSIsIi0wLjElIiwiUFRRIOKAlCBvdXRsaWVyIGRlY29tcG9zZSIsIkxMTSBpbmZlcmVuY2UsIG91dGxpZXItaGVhdnkiXSxbIlc0QTE2IChHUFRRL05GNCkiLCIzLjUgR0IiLCIy4oCTNMOXIChiYW5kd2lkdGgpIiwiLTAuNSB0byAtMSUiLCJQVFEg4oCUIE9CUyBmcmFtZXdvcmsiLCJMTE0gb24gY29uc3VtZXIgR1BVIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTbW9vdGhRdWFudCDigJQgTWlncmF0aW5nIFF1YW50aXphdGlvbiBEaWZmaWN1bHR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMTE0gYWN0aXZhdGlvbnMgY29udGFpbiBvdXRsaWVyIGNoYW5uZWxzOiBhIHNtYWxsIGZyYWN0aW9uIG9mIGNoYW5uZWxzICgwLjElKSBoYXZlIHZhbHVlcyAxMDDDlyBsYXJnZXIgdGhhbiB0aGUgcmVzdC4gVGhlc2Ugb3V0bGllcnMgaW5mbGF0ZSB0aGUgcXVhbnRpemF0aW9uIHNjYWxlLCB3YXN0aW5nIG1vc3Qgb2YgdGhlIElOVDggcmFuZ2Ugb24gdGhlIGZldyBleHRyZW1lIHZhbHVlcy4gU21vb3RoUXVhbnQgKFhpYW8gZXQgYWwuIDIwMjMpIG1pZ3JhdGVzIHRoZSBxdWFudGl6YXRpb24gZGlmZmljdWx0eSBmcm9tIGFjdGl2YXRpb25zIHRvIHdlaWdodHM6IGZvciBlYWNoIGNoYW5uZWwgaiwgZGl2aWRlIGFjdGl2YXRpb24gYnkgYSBwZXItY2hhbm5lbCBzbW9vdGhpbmcgZmFjdG9yIHNfaiBhbmQgbXVsdGlwbHkgdGhlIGNvcnJlc3BvbmRpbmcgd2VpZ2h0IGNvbHVtbiBieSBzX2ouIEFjdGl2YXRpb25zIGJlY29tZSBlYXNpZXIgdG8gcXVhbnRpemUgKHNtYWxsZXIgcmFuZ2UpIHdoaWxlIHdlaWdodHMgYWJzb3JiIHRoZSBzY2FsaW5nICh3ZWlnaHRzIGFyZSBhbHJlYWR5IGVhc3kgdG8gcXVhbnRpemUgYmVjYXVzZSB0aGV5IGRvIG5vdCBoYXZlIHBlci10b2tlbiBvdXRsaWVycykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBzbW9vdGhxdWFudF9zY2FsZShhY3RpdmF0aW9uX21heDogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgIHdlaWdodF9tYXg6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICBhbHBoYTogZmxvYXQgPSAwLjUpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlxuICAgIENvbXB1dGUgcGVyLWNoYW5uZWwgc21vb3RoaW5nIGZhY3RvciBzIGZvciBTbW9vdGhRdWFudC5cbiAgICBzX2ogPSBtYXgofFhfanwpXmFscGhhIC8gbWF4KHxXX2p8KV4oMS1hbHBoYSlcbiAgICBhbHBoYT0wLjU6IGVxdWFsIG1pZ3JhdGlvbjsgYWxwaGHihpIxOiBwdXNoIGFsbCBkaWZmaWN1bHR5IHRvIHdlaWdodHMuXG4gICAgYWN0aXZhdGlvbl9tYXg6IChDX2luLCkgcGVyLWNoYW5uZWwgbWF4IGFjdGl2YXRpb24gbWFnbml0dWRlXG4gICAgd2VpZ2h0X21heDogICAgIChDX2luLCkgcGVyLWNoYW5uZWwgbWF4IHdlaWdodCBtYWduaXR1ZGVcbiAgICBcIlwiXCJcbiAgICBzID0gKGFjdGl2YXRpb25fbWF4ICoqIGFscGhhKSAvICh3ZWlnaHRfbWF4ICoqICgxIC0gYWxwaGEpICsgMWUtOClcbiAgICByZXR1cm4gc1xuXG5kZWYgYXBwbHlfc21vb3RocXVhbnQobGluZWFyOiBubi5MaW5lYXIsXG4gICAgICAgICAgICAgICAgICAgICAgY2FsaWJyYXRpb25fYWN0czogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgIGFscGhhOiBmbG9hdCA9IDAuNSk6XG4gICAgXCJcIlwiXG4gICAgQXBwbHkgU21vb3RoUXVhbnQgdG8gYSBMaW5lYXIgbGF5ZXIuXG4gICAgY2FsaWJyYXRpb25fYWN0czogKE4sIENfaW4pIOKAlCBiYXRjaCBvZiBhY3RpdmF0aW9ucyBmb3IgY2FsaWJyYXRpb24uXG4gICAgXCJcIlwiXG4gICAgYWN0X21heCA9IGNhbGlicmF0aW9uX2FjdHMuYWJzKCkuYW1heChkaW09MCkgICMgKENfaW4sKVxuICAgIFcgPSBsaW5lYXIud2VpZ2h0LmRhdGEgICMgKENfb3V0LCBDX2luKVxuICAgIHdfbWF4ID0gVy5hYnMoKS5hbWF4KGRpbT0wKSAgIyAoQ19pbiwpIHBlciBpbnB1dCBjaGFubmVsXG5cbiAgICBzID0gc21vb3RocXVhbnRfc2NhbGUoYWN0X21heCwgd19tYXgsIGFscGhhKVxuICAgICMgTW9kaWZ5IHdlaWdodDogV1x1MDAyNyA9IFcgKiBkaWFnKHMpXG4gICAgbGluZWFyLndlaWdodC5kYXRhID0gVyAqIHMudW5zcXVlZXplKDApXG4gICAgIyBUaGUgY2FsbGVyIG11c3QgZGl2aWRlIGFjdGl2YXRpb25zIGJ5IHMgYmVmb3JlIHBhc3NpbmcgdG8gdGhpcyBsYXllclxuICAgIHByaW50KGZcdTAwMjdTbW9vdGhpbmcgZmFjdG9ycyDigJQgbWluOiB7cy5taW4oKTouM2Z9ICBtYXg6IHtzLm1heCgpOi4zZn0gIG1lYW46IHtzLm1lYW4oKTouM2Z9XHUwMDI3KVxuICAgIHJldHVybiBzICAjIGNhbGxlciBkaXZpZGVzIGFjdGl2YXRpb25zIGJ5IHNcblxuIyBEZW1vXG5saW5lYXIgPSBubi5MaW5lYXIoMTI4LCA2NClcbmNhbGliX2FjdHMgPSB0b3JjaC5yYW5kbig2NCwgMTI4KVxuY2FsaWJfYWN0c1s6LCAzXSAqPSA1MCAgICMgc2ltdWxhdGUgb3V0bGllciBjaGFubmVsIDNcbmNhbGliX2FjdHNbOiwgNzFdICo9IDgwICAjIHNpbXVsYXRlIG91dGxpZXIgY2hhbm5lbCA3MVxucyA9IGFwcGx5X3Ntb290aHF1YW50KGxpbmVhciwgY2FsaWJfYWN0cywgYWxwaGE9MC41KVxucHJpbnQoZlx1MDAyN091dGxpZXIgY2hhbm5lbHMgc2NhbGVkIGRvd246IGNoMz17c1szXTouMmZ9ICBjaDcxPXtzWzcxXTouMmZ9XHUwMDI3KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR1BUUSBxdWFudGl6ZXMgbGF5ZXJzIHNlcXVlbnRpYWxseSBmcm9tIGZpcnN0IHRvIGxhc3QuIEZvciBlYWNoIGxheWVyLCBpdCBjb25zdHJ1Y3RzIHRoZSBIZXNzaWFuIEggPSAyWFheVCAod2hlcmUgWCBpcyB0aGUgbGF5ZXJcdTAwMjdzIGlucHV0IGFjdGl2YXRpb25zIG92ZXIgdGhlIGNhbGlicmF0aW9uIHNldCkgYW5kIG1pbmltaXplcyB0aGUgbGF5ZXIgb3V0cHV0IHJlY29uc3RydWN0aW9uIGVycm9yIOKAlldYIC0gV19xWOKAlsKyIHVuZGVyIHRoZSBJTlQ0IHF1YW50aXphdGlvbiBjb25zdHJhaW50LiBUaGUgT3B0aW1hbCBCcmFpbiBTdXJnZW9uIHVwZGF0ZSBhZGp1c3RzIHJlbWFpbmluZyB1bnF1YW50aXplZCB3ZWlnaHRzIHRvIGNvbXBlbnNhdGUgZm9yIHRoZSBlcnJvciBpbnRyb2R1Y2VkIGJ5IHF1YW50aXppbmcgdGhlIGN1cnJlbnQgd2VpZ2h0LiBUaGlzIHBlci1sYXllciBzZXF1ZW50aWFsIHF1YW50aXphdGlvbiB0YWtlcyAzMOKAkzYwIG1pbnV0ZXMgZm9yIGEgN0IgbW9kZWwgb24gYSBzaW5nbGUgQTEwMC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlBUUSBjYWxpYnJhdGlvbiBzZXQ6IDUxMuKAkzEwMjQgcmFuZG9tIHNhbXBsZXMgYXJlIHN1ZmZpY2llbnQ7IG1vcmUgZG9lcyBub3Qgc2lnbmlmaWNhbnRseSBpbXByb3ZlIGFjY3VyYWN5LiIsIlBlci1jaGFubmVsIHNjYWxlOiBhbHdheXMgdXNlIHBlci1jaGFubmVsIChub3QgcGVyLXRlbnNvcikgcXVhbnRpemF0aW9uIGZvciB3ZWlnaHRzIOKAlCAx4oCTMiUgYWNjdXJhY3kgZGlmZmVyZW5jZS4iLCJBY3RpdmF0aW9uIHF1YW50aXphdGlvbjogaGFyZGVyIHRoYW4gd2VpZ2h0IHF1YW50aXphdGlvbiBkdWUgdG8gZHluYW1pYyByYW5nZSB2YXJpYXRpb24gYWNyb3NzIHRva2Vucy4iLCJJTlQ4IHZzIElOVDQgZm9yIExMTXM6IElOVDggKFc4QTgpIGdpdmVzIG5lYXItbG9zc2xlc3MgcXVhbGl0eTsgSU5UNCAoVzRBMTYpIHRyYWRlcyB+MC41IHBlcnBsZXhpdHkgZm9yIDLDlyBtZW1vcnkuIiwiR3JvdXAgcXVhbnRpemF0aW9uOiBXNCB3aXRoIGdyb3VwIHNpemUgMTI4IChvbmUgc2NhbGUgcGVyIDEyOCB3ZWlnaHRzKSBpbXByb3ZlcyBhY2N1cmFjeSB2cyBwZXItdGVuc29yIGF0IGxvdyBvdmVyaGVhZC4iLCJEb3VibGUgcXVhbnRpemF0aW9uIChRTG9SQSk6IHF1YW50aXplIHRoZSBxdWFudGl6YXRpb24gc2NhbGVzIHRoZW1zZWx2ZXMgdG8gSU5UOCwgc2F2aW5nIGFkZGl0aW9uYWwgMC4zNyBiaXRzIHBlciB3ZWlnaHQuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWl4ZWQtcHJlY2lzaW9uIHF1YW50aXphdGlvbiBhc3NpZ25zIGRpZmZlcmVudCBiaXQtd2lkdGhzIHRvIGRpZmZlcmVudCBsYXllcnMgYmFzZWQgb24gdGhlaXIgc2Vuc2l0aXZpdHkuIFNlbnNpdGl2aXR5IGlzIG1lYXN1cmVkIGJ5IHRoZSBIZXNzaWFuIHRyYWNlIG9mIHRoZSBsb3NzIHdpdGggcmVzcGVjdCB0byBlYWNoIGxheWVyXHUwMDI3cyB3ZWlnaHRzOiBsYXllcnMgd2l0aCBoaWdoIEhlc3NpYW4gdHJhY2UgYXJlIHNlbnNpdGl2ZSAoc21hbGwgd2VpZ2h0IHBlcnR1cmJhdGlvbnMgY2F1c2UgbGFyZ2UgbG9zcyBjaGFuZ2VzKSBhbmQgc2hvdWxkIHVzZSBoaWdoZXIgcHJlY2lzaW9uLiBMYXllcnMgd2l0aCBsb3cgSGVzc2lhbiB0cmFjZSBjYW4gdXNlIElOVDQgc2FmZWx5LiBIQVEgKEhhcmR3YXJlLUF3YXJlIE1peGVkLVByZWNpc2lvbiBRdWFudGl6YXRpb24pIHVzZXMgcmVpbmZvcmNlbWVudCBsZWFybmluZyB0byBzZWFyY2ggZm9yIGJpdC13aWR0aCBhc3NpZ25tZW50cyB1bmRlciBhIGhhcmR3YXJlIGNvbnN0cmFpbnQsIGFjaGlldmluZyBiZXR0ZXIgYWNjdXJhY3ktbWVtb3J5IHRyYWRlLW9mZnMgdGhhbiB1bmlmb3JtIHF1YW50aXphdGlvbiBhdCB0aGUgc2FtZSBhdmVyYWdlIGJpdC13aWR0aC4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Quantization — PTQ, QAT, and W4A16 for LLMs

Quantization maps floating-point weights and/or activations to lower-precision integers. A FP32 weight consumes 4 bytes; an INT8 weight consumes 1 byte; an INT4 weight consumes 0.5 bytes. Memory bandwidth is often the primary bottleneck for LLM inference — quantizing weights 4× reduces the bytes transferred per token, directly accelerating generation. Quantization also enables deployment on hardware without FP32 support (microcontrollers, mobile NPUs).

## Symmetric and Asymmetric Quantization

Symmetric quantization: q(x) = clamp(round(x / scale), -2^(b-1), 2^(b-1)-1) where scale = max(|x|) / 2^(b-1). Dequantize: x̂ = q · scale. For INT8: range is [-128, 127], scale = max|x|/127. Asymmetric adds a zero-point z: q(x) = clamp(round(x/scale + z), 0, 2^b-1), x̂ = (q-z)·scale. Asymmetric covers non-symmetric distributions (ReLU outputs are always non-negative) but adds zero-point overhead. Per-tensor quantization uses one scale for the entire tensor; per-channel uses one scale per output channel, giving significantly better accuracy.

```python
import torch
import torch.nn as nn

def symmetric_quantize(x: torch.Tensor, bits: int = 8):
    """Symmetric per-tensor quantization. Returns (quantized_int, scale)."""
    qmax = 2 ** (bits - 1) - 1  # 127 for INT8
    scale = x.abs().max() / qmax
    scale = scale.clamp(min=1e-8)  # avoid division by zero
    q = (x / scale).round().clamp(-qmax - 1, qmax)
    return q.to(torch.int8), scale

def dequantize(q: torch.Tensor, scale: torch.Tensor) -> torch.Tensor:
    return q.float() * scale

def per_channel_quantize(weight: torch.Tensor, bits: int = 8):
    """Per output-channel symmetric quantization for conv/linear weights."""
    qmax = 2 ** (bits - 1) - 1
    # Scale per output channel (dim 0)
    scale = weight.abs().amax(dim=tuple(range(1, weight.ndim)), keepdim=True) / qmax
    scale = scale.clamp(min=1e-8)
    q = (weight / scale).round().clamp(-qmax - 1, qmax).to(torch.int8)
    return q, scale

# Compare per-tensor vs per-channel quantization error
torch.manual_seed(0)
W = torch.randn(64, 32)  # simulate a linear layer weight

q_pt, s_pt = symmetric_quantize(W, bits=8)
W_hat_pt = dequantize(q_pt, s_pt)
err_pt = (W - W_hat_pt).abs().mean().item()

q_pc, s_pc = per_channel_quantize(W, bits=8)
W_hat_pc = dequantize(q_pc, s_pc.expand_as(W))
err_pc = (W - W_hat_pc).abs().mean().item()

print(f'Per-tensor  MAE: {err_pt:.5f}  scale={s_pt.item():.4f}')
print(f'Per-channel MAE: {err_pc:.5f}  (one scale per row)')
print(f'Per-channel is {err_pt/err_pc:.1f}x more accurate')
```

## Post-Training Quantization with Calibration

PTQ requires no retraining. A small calibration dataset (100–1000 samples) is forwarded through the model to gather activation statistics (min, max, or percentile). These statistics determine the quantization scale for each layer. Activation outliers inflate the scale, wasting precision on rare large values. Techniques like SmoothQuant migrate the quantization difficulty from activations to weights (which are easier to quantize) by multiplying activation scales into the weight.

## Quantization-Aware Training (QAT)

QAT simulates quantization during training: in the forward pass, weights and activations are fake-quantized (quantize then dequantize, staying in FP32 dtype). The model learns to compensate for quantization error. Gradients flow through the fake-quantize operation using the straight-through estimator (STE): the gradient of the round function is treated as 1 within the clamp range and 0 outside. QAT typically recovers 1–2% accuracy lost by PTQ at INT8, and is essential for INT4 quantization where PTQ accuracy degrades significantly.

```python
import torch
import torch.nn as nn
from torch.autograd import Function

class FakeQuantize(Function):
    """Fake quantization with straight-through estimator."""

    @staticmethod
    def forward(ctx, x: torch.Tensor, scale: float, bits: int = 8):
        qmax = 2 ** (bits - 1) - 1
        # Quantize and dequantize (stays float, but has quantization error)
        q = (x / scale).round().clamp(-qmax - 1, qmax)
        x_hat = q * scale
        # STE: pass gradient through clamp region, zero outside
        ctx.save_for_backward(x)
        ctx.scale = scale
        ctx.qmax = qmax
        return x_hat

    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        qmax = ctx.qmax
        scale = ctx.scale
        # STE: gradient = 1 where x is in quantization range, else 0
        in_range = ((x / scale) >= -(qmax + 1)) & ((x / scale) <= qmax)
        grad_input = grad_output * in_range.float()
        return grad_input, None, None  # None for scale and bits

class QATLinear(nn.Module):
    def __init__(self, in_features, out_features, bits=8):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.bits = bits

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Fake-quantize weights
        W = self.linear.weight
        scale_w = W.abs().max().item() / (2 ** (self.bits - 1) - 1)
        W_fq = FakeQuantize.apply(W, scale_w, self.bits)
        return nn.functional.linear(x, W_fq, self.linear.bias)

# Verify gradient flows through fake quantize
layer = QATLinear(32, 16, bits=8)
x = torch.randn(4, 32)
loss = layer(x).sum()
loss.backward()
print(f'Weight grad norm: {layer.linear.weight.grad.norm().item():.4f}')
print('Gradient flows through fake quantize via STE.')
```

## LLM Quantization — GPTQ and W4A16

For LLMs with billions of parameters, QAT is infeasible (retraining costs). GPTQ (Frantar et al. 2022) does weight-only quantization: weights are quantized to INT4 (W4), activations remain FP16 (A16). GPTQ solves a layer-wise reconstruction problem using the Hessian of the layer's output with respect to its weights (via the Optimal Brain Surgeon framework). This produces INT4 weights that minimize the increase in layer output error, recovering close to FP16 accuracy without any gradient computation. LLM.int8 (Dettmers 2022) handles activation outliers via mixed precision: large outlier rows in the activation matrix are kept in FP16 and multiplied separately, while the majority of the matrix is quantized to INT8.

```python
# Requires: pip install bitsandbytes transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

def load_model_4bit(model_name: str = 'facebook/opt-125m'):
    """Load a causal LM in 4-bit using bitsandbytes NF4 quantization."""
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',         # NormalFloat4 — optimal for normally distributed weights
        bnb_4bit_compute_dtype=torch.float16,  # activations in FP16
        bnb_4bit_use_double_quant=True,    # quantize the quantization constants too
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map='auto',
    )
    # Report memory
    mem_mb = sum(p.numel() * p.element_size() for p in model.parameters()) / 1024**2
    n_params = sum(p.numel() for p in model.parameters()) / 1e6
    print(f'Model: {model_name}  Params: {n_params:.1f}M  Approx memory: {mem_mb:.0f} MB')
    print(f'Quantization: W4A16 (NF4 weights, FP16 activations)')
    return model, tokenizer

# Expected output for OPT-125M:
# Params: 125.0M  Approx memory: ~63 MB (vs 477 MB FP32)
print('Load with: model, tok = load_model_4bit("facebook/opt-125m")')
```

> **NF4 vs INT4 for LLM Weights**: NormalFloat4 (NF4) is a data type optimized for normally distributed weights: the 16 quantization levels are spaced at equal quantiles of the standard normal distribution, not uniformly. Since pre-trained LLM weights are approximately normally distributed, NF4 uses its 4 bits more efficiently than uniform INT4, typically recovering 0.1–0.5 perplexity points at the same bit-width.

## Quantization Format Comparison

| Format | Memory (7B model) | Inference Speedup | Accuracy Loss | PTQ vs QAT | Best Use Case |
| --- | --- | --- | --- | --- | --- |
| FP32 | 28 GB | 1× baseline | None | N/A | Training, research |
| FP16 / BF16 | 14 GB | 1.5–2× (Tensor Core) | Negligible | N/A | Training + inference |
| INT8 (W8A8) | 7 GB | 2–3× (INT8 GEMM) | -0.1 to -0.5% | PTQ with calibration | Production inference, CNNs |
| W8A16 (LLM.int8) | 7 GB | 1.5× (bandwidth bound) | -0.1% | PTQ — outlier decompose | LLM inference, outlier-heavy |
| W4A16 (GPTQ/NF4) | 3.5 GB | 2–4× (bandwidth) | -0.5 to -1% | PTQ — OBS framework | LLM on consumer GPU |

## SmoothQuant — Migrating Quantization Difficulty

LLM activations contain outlier channels: a small fraction of channels (0.1%) have values 100× larger than the rest. These outliers inflate the quantization scale, wasting most of the INT8 range on the few extreme values. SmoothQuant (Xiao et al. 2023) migrates the quantization difficulty from activations to weights: for each channel j, divide activation by a per-channel smoothing factor s_j and multiply the corresponding weight column by s_j. Activations become easier to quantize (smaller range) while weights absorb the scaling (weights are already easy to quantize because they do not have per-token outliers).

```python
import torch
import torch.nn as nn

def smoothquant_scale(activation_max: torch.Tensor,
                      weight_max: torch.Tensor,
                      alpha: float = 0.5) -> torch.Tensor:
    """
    Compute per-channel smoothing factor s for SmoothQuant.
    s_j = max(|X_j|)^alpha / max(|W_j|)^(1-alpha)
    alpha=0.5: equal migration; alpha→1: push all difficulty to weights.
    activation_max: (C_in,) per-channel max activation magnitude
    weight_max:     (C_in,) per-channel max weight magnitude
    """
    s = (activation_max ** alpha) / (weight_max ** (1 - alpha) + 1e-8)
    return s

def apply_smoothquant(linear: nn.Linear,
                      calibration_acts: torch.Tensor,
                      alpha: float = 0.5):
    """
    Apply SmoothQuant to a Linear layer.
    calibration_acts: (N, C_in) — batch of activations for calibration.
    """
    act_max = calibration_acts.abs().amax(dim=0)  # (C_in,)
    W = linear.weight.data  # (C_out, C_in)
    w_max = W.abs().amax(dim=0)  # (C_in,) per input channel

    s = smoothquant_scale(act_max, w_max, alpha)
    # Modify weight: W' = W * diag(s)
    linear.weight.data = W * s.unsqueeze(0)
    # The caller must divide activations by s before passing to this layer
    print(f'Smoothing factors — min: {s.min():.3f}  max: {s.max():.3f}  mean: {s.mean():.3f}')
    return s  # caller divides activations by s

# Demo
linear = nn.Linear(128, 64)
calib_acts = torch.randn(64, 128)
calib_acts[:, 3] *= 50   # simulate outlier channel 3
calib_acts[:, 71] *= 80  # simulate outlier channel 71
s = apply_smoothquant(linear, calib_acts, alpha=0.5)
print(f'Outlier channels scaled down: ch3={s[3]:.2f}  ch71={s[71]:.2f}')
```

GPTQ quantizes layers sequentially from first to last. For each layer, it constructs the Hessian H = 2XX^T (where X is the layer's input activations over the calibration set) and minimizes the layer output reconstruction error ‖WX - W_qX‖² under the INT4 quantization constraint. The Optimal Brain Surgeon update adjusts remaining unquantized weights to compensate for the error introduced by quantizing the current weight. This per-layer sequential quantization takes 30–60 minutes for a 7B model on a single A100.

- PTQ calibration set: 512–1024 random samples are sufficient; more does not significantly improve accuracy.
- Per-channel scale: always use per-channel (not per-tensor) quantization for weights — 1–2% accuracy difference.
- Activation quantization: harder than weight quantization due to dynamic range variation across tokens.
- INT8 vs INT4 for LLMs: INT8 (W8A8) gives near-lossless quality; INT4 (W4A16) trades ~0.5 perplexity for 2× memory.
- Group quantization: W4 with group size 128 (one scale per 128 weights) improves accuracy vs per-tensor at low overhead.
- Double quantization (QLoRA): quantize the quantization scales themselves to INT8, saving additional 0.37 bits per weight.

Mixed-precision quantization assigns different bit-widths to different layers based on their sensitivity. Sensitivity is measured by the Hessian trace of the loss with respect to each layer's weights: layers with high Hessian trace are sensitive (small weight perturbations cause large loss changes) and should use higher precision. Layers with low Hessian trace can use INT4 safely. HAQ (Hardware-Aware Mixed-Precision Quantization) uses reinforcement learning to search for bit-width assignments under a hardware constraint, achieving better accuracy-memory trade-offs than uniform quantization at the same average bit-width.

---

