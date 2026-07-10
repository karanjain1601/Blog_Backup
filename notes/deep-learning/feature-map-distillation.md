---
title: "Feature Map Distillation — FitNets and Intermediate Representations"
slug: "feature-map-distillation"
description: "Go beyond output logits by aligning intermediate feature maps between teacher and student. Covers FitNets hint training, two-stage schedules, attention transfer, layer-to-layer mapping, PKT, CRD, and a comparison of feature distillation methods."
tags: ["deep-learning", "model-compression", "knowledge-distillation"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT3V0cHV0LW9ubHkga25vd2xlZGdlIGRpc3RpbGxhdGlvbiB0cmFuc2ZlcnMgb25seSB0aGUgdGVhY2hlclx1MDAyN3MgZmluYWwgcHJlZGljdGlvbnMuIFRoaXMgbWlzc2VzIHRoZSByaWNoIGludGVybWVkaWF0ZSByZXByZXNlbnRhdGlvbnMgYnVpbHQgdXAgYWNyb3NzIHRoZSB0ZWFjaGVyXHUwMDI3cyBsYXllcnMg4oCUIHJlcHJlc2VudGF0aW9ucyBlbmNvZGluZyBlZGdlcywgdGV4dHVyZXMsIG9iamVjdCBwYXJ0cywgYW5kIHNlbWFudGljIHN0cnVjdHVyZS4gRmVhdHVyZSBtYXAgZGlzdGlsbGF0aW9uIG1ldGhvZHMgdHJhbnNmZXIgdGhlc2UgaW50ZXJuYWwgcmVwcmVzZW50YXRpb25zIGRpcmVjdGx5LCBnaXZpbmcgdGhlIHN0dWRlbnQgYSByaWNoZXIgdHJhaW5pbmcgc2lnbmFsIGFuZCBiZXR0ZXIgaW5pdGlhbGl6YXRpb24gZm9yIGxlYXJuaW5nIHRoZSB0YXNrLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZpdE5ldHMgYW5kIEhpbnQgTGF5ZXIgVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZpdE5ldHMgKFJvbWVybyBldCBhbC4gMjAxNSkgZXh0ZW5kIGRpc3RpbGxhdGlvbiB0byBpbnRlcm1lZGlhdGUgbGF5ZXJzLiBBIFx1MDAyN2hpbnQgbGF5ZXJcdTAwMjcgaW4gdGhlIHRlYWNoZXIgYW5kIGEgXHUwMDI3Z3VpZGVkIGxheWVyXHUwMDI3IGluIHRoZSBzdHVkZW50IGFyZSBjaG9zZW4gYXQgbWF0Y2hpbmcgZGVwdGhzLiBUaGUgc3R1ZGVudCBpcyB0cmFpbmVkIHRvIHByZWRpY3QgdGhlIHRlYWNoZXJcdTAwMjdzIGhpbnQgbGF5ZXIgb3V0cHV0OiBMX2hpbnQgPSDigJZXX2goRl9zdHVkZW50KSAtIEZfdGVhY2hlcuKAlsKyLCB3aGVyZSBXX2ggaXMgYSAxw5cxIGNvbnZvbHV0aW9uYWwgYWRhcHRlciB0aGF0IHByb2plY3RzIHRoZSBzdHVkZW50XHUwMDI3cyBmZWF0dXJlIG1hcCB0byB0aGUgdGVhY2hlclx1MDAyN3MgY2hhbm5lbCBkaW1lbnNpb24uIFRoaXMgZm9yY2VzIHRoZSBzdHVkZW50IHRvIGJ1aWxkIHRoZSBzYW1lIGludGVybWVkaWF0ZSByZXByZXNlbnRhdGlvbnMgYXMgdGhlIHRlYWNoZXIsIG5vdCBqdXN0IG1hdGNoIGZpbmFsIHByZWRpY3Rpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBIaW50TG9zcyhubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkZpdE5ldHMgaGludCBsb3NzOiBhbGlnbiBzdHVkZW50IGZlYXR1cmUgbWFwIHRvIHRlYWNoZXIgdmlhIDF4MSBjb252IGFkYXB0ZXIuXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgc3R1ZGVudF9jaGFubmVsczogaW50LCB0ZWFjaGVyX2NoYW5uZWxzOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgIyBBZGFwdGVyIFdfaDogbWFwcyBzdHVkZW50IGRpbSAtXHUwMDNlIHRlYWNoZXIgZGltXG4gICAgICAgIHNlbGYuYWRhcHRlciA9IG5uLkNvbnYyZChzdHVkZW50X2NoYW5uZWxzLCB0ZWFjaGVyX2NoYW5uZWxzLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAga2VybmVsX3NpemU9MSwgYmlhcz1GYWxzZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGZfc3R1ZGVudDogdG9yY2guVGVuc29yLCBmX3RlYWNoZXI6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIFwiXCJcIlxuICAgICAgICBmX3N0dWRlbnQ6IChCLCBDX1MsIEgsIFcpICBzdHVkZW50IGludGVybWVkaWF0ZSBmZWF0dXJlIG1hcFxuICAgICAgICBmX3RlYWNoZXI6IChCLCBDX1QsIEgsIFcpICB0ZWFjaGVyIGludGVybWVkaWF0ZSBmZWF0dXJlIG1hcCAoZGV0YWNoZWQpXG4gICAgICAgIFJldHVybnM6IHx8V19oKEZfcykgLSBGX3R8fF4yIC8gTlxuICAgICAgICBcIlwiXCJcbiAgICAgICAgZl9hZGFwdGVkID0gc2VsZi5hZGFwdGVyKGZfc3R1ZGVudCkgICAgICAgICAgICMgKEIsIENfVCwgSCwgVylcbiAgICAgICAgcmV0dXJuIEYubXNlX2xvc3MoZl9hZGFwdGVkLCBmX3RlYWNoZXIuZGV0YWNoKCkpXG5cblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIEgsIFcgPSA0LCAxNCwgMTRcbkNfdGVhY2hlciwgQ19zdHVkZW50ID0gMjU2LCAxMjhcblxuZl90ZWFjaGVyID0gdG9yY2gucmFuZG4oQiwgQ190ZWFjaGVyLCBILCBXKVxuZl9zdHVkZW50ICA9IHRvcmNoLnJhbmRuKEIsIENfc3R1ZGVudCwgIEgsIFcpXG5cbmhpbnQgPSBIaW50TG9zcyhDX3N0dWRlbnQsIENfdGVhY2hlcilcbmxvc3MgPSBoaW50KGZfc3R1ZGVudCwgZl90ZWFjaGVyKVxucHJpbnQoZlx1MDAyN0hpbnQgbG9zczoge2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3QWRhcHRlcjoge0Nfc3R1ZGVudH0gLVx1MDAzZSB7Q190ZWFjaGVyfSBjaGFubmVscywgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBoaW50LnBhcmFtZXRlcnMoKSl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlR3by1TdGFnZSBUcmFpbmluZzogSGludCBUaGVuIEtEIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGaXROZXRzIHVzZSB0d28gdHJhaW5pbmcgc3RhZ2VzLiBTdGFnZSAxIChoaW50IHRyYWluaW5nKTogb3B0aW1pemUgb25seSB0aGUgaGludCBsb3NzIExfaGludCB0byBhbGlnbiB0aGUgc3R1ZGVudFx1MDAyN3MgaW50ZXJtZWRpYXRlIGZlYXR1cmUgbWFwIHdpdGggdGhlIHRlYWNoZXJcdTAwMjdzIGhpbnQgbGF5ZXIuIFRoaXMgZ2l2ZXMgdGhlIHN0dWRlbnQgYSBiZXR0ZXIgc3RhcnRpbmcgcG9pbnQgdGhhbiByYW5kb20gaW5pdGlhbGl6YXRpb24uIFN0YWdlIDIgKEtEIHRyYWluaW5nKTogZGlzY2FyZCB0aGUgYWRhcHRlciBhbmQgdHJhaW4gdGhlIGZ1bGwgc3R1ZGVudCB3aXRoIHRoZSBzdGFuZGFyZCBsb2dpdC1sZXZlbCBkaXN0aWxsYXRpb24gbG9zcyB1c2luZyB0aGUgdGVhY2hlclx1MDAyN3Mgb3V0cHV0IHByb2JhYmlsaXRpZXMuIFRoZSB0d28tc3RhZ2Ugc2NoZWR1bGUgY29uc2lzdGVudGx5IG91dHBlcmZvcm1zIHNpbmdsZS1zdGFnZSBsb2dpdCBLRCwgZXNwZWNpYWxseSBmb3IgZGVlcCBzdHVkZW50cyB0cmFpbmVkIG9uIHNtYWxsIGRhdGFzZXRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IHRvcmNoLm9wdGltIGFzIG9wdGltXG5cbmRlZiBzdGFnZTFfaGludF90cmFpbmluZyhzdHVkZW50LCB0ZWFjaGVyLCBoaW50X2xvc3NfZm4sIGxvYWRlciwgZGV2aWNlLCBlcG9jaHM9MiwgbHI9MWUtMyk6XG4gICAgXCJcIlwiU3RhZ2UgMTogdHJhaW4gc3R1ZGVudCB0byBtYXRjaCB0ZWFjaGVyIGludGVybWVkaWF0ZSBmZWF0dXJlIG1hcHMuXCJcIlwiXG4gICAgcGFyYW1zID0gbGlzdChzdHVkZW50LnBhcmFtZXRlcnMoKSkgKyBsaXN0KGhpbnRfbG9zc19mbi5wYXJhbWV0ZXJzKCkpXG4gICAgb3B0aW1pemVyID0gb3B0aW0uQWRhbShwYXJhbXMsIGxyPWxyKVxuICAgIGZvciBlcG9jaCBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICB0b3RhbCA9IDAuMFxuICAgICAgICBmb3IgWCwgXyBpbiBsb2FkZXI6XG4gICAgICAgICAgICBYID0gWC50byhkZXZpY2UpXG4gICAgICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgICAgICBmX3RlYWNoZXIgPSB0ZWFjaGVyLmdldF9oaW50X2ZlYXR1cmVzKFgpXG4gICAgICAgICAgICBmX3N0dWRlbnQgPSBzdHVkZW50LmdldF9ndWlkZWRfZmVhdHVyZXMoWClcbiAgICAgICAgICAgIGxvc3MgPSBoaW50X2xvc3NfZm4oZl9zdHVkZW50LCBmX3RlYWNoZXIpXG4gICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICAgICAgb3B0aW1pemVyLnN0ZXAoKVxuICAgICAgICAgICAgdG90YWwgKz0gbG9zcy5pdGVtKClcbiAgICAgICAgcHJpbnQoZlx1MDAyNyAgSGludCBlcG9jaCB7ZXBvY2grMX06IGhpbnRfbG9zcz17dG90YWwvbGVuKGxvYWRlcik6LjRmfVx1MDAyNylcblxuZGVmIHN0YWdlMl9rZF90cmFpbmluZyhzdHVkZW50LCB0ZWFjaGVyLCBsb2FkZXIsIGRldmljZSxcbiAgICAgICAgICAgICAgICAgICAgICAgIHRlbXBlcmF0dXJlPTQuMCwgYWxwaGE9MC41LCBlcG9jaHM9NSwgbHI9NWUtNCk6XG4gICAgXCJcIlwiU3RhZ2UgMjogZnVsbCBLRCB3aXRoIHRlYWNoZXIgbG9naXRzIChoaW50IGFkYXB0ZXIgaXMgZGlzY2FyZGVkKS5cIlwiXCJcbiAgICBvcHRpbWl6ZXIgPSBvcHRpbS5BZGFtKHN0dWRlbnQucGFyYW1ldGVycygpLCBscj1scilcbiAgICBUID0gdGVtcGVyYXR1cmVcbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgdG90YWwgPSAwLjBcbiAgICAgICAgZm9yIFgsIHkgaW4gbG9hZGVyOlxuICAgICAgICAgICAgWCwgeSA9IFgudG8oZGV2aWNlKSwgeS50byhkZXZpY2UpXG4gICAgICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgICAgICB0X2xvZ2l0cyA9IHRlYWNoZXIoWClcbiAgICAgICAgICAgIHNfbG9naXRzID0gc3R1ZGVudChYKVxuICAgICAgICAgICAgaGFyZCA9IEYuY3Jvc3NfZW50cm9weShzX2xvZ2l0cywgeSlcbiAgICAgICAgICAgIHNvZnQgPSBGLmtsX2RpdihGLmxvZ19zb2Z0bWF4KHNfbG9naXRzIC8gVCwgZGltPS0xKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBGLnNvZnRtYXgodF9sb2dpdHMgLyBULCBkaW09LTEpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJlZHVjdGlvbj1cdTAwMjdiYXRjaG1lYW5cdTAwMjcpICogVCAqKiAyXG4gICAgICAgICAgICBsb3NzID0gYWxwaGEgKiBoYXJkICsgKDEgLSBhbHBoYSkgKiBzb2Z0XG4gICAgICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0aW1pemVyLnN0ZXAoKVxuICAgICAgICAgICAgdG90YWwgKz0gbG9zcy5pdGVtKClcbiAgICAgICAgcHJpbnQoZlx1MDAyNyAgS0QgZXBvY2gge2Vwb2NoKzF9OiBsb3NzPXt0b3RhbC9sZW4obG9hZGVyKTouNGZ9XHUwMDI3KVxuXG5wcmludChcdTAwMjdUd28tc3RhZ2UgRml0TmV0czogc3RhZ2UxPWhpbnQgYWxpZ25tZW50LCBzdGFnZTI9ZnVsbCBsb2dpdCBLRC5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXR0ZW50aW9uIFRyYW5zZmVyIChBVCkgTG9zcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXR0ZW50aW9uIFRyYW5zZmVyIChaYWdvcnV5a28gXHUwMDI2IEtvbW9kYWtpcyAyMDE3KSBkaXN0aWxscyBzcGF0aWFsIGF0dGVudGlvbiBtYXBzIHJhdGhlciB0aGFuIHJhdyBmZWF0dXJlIHZhbHVlcy4gVGhlIGF0dGVudGlvbiBtYXAgZnJvbSBmZWF0dXJlIHRlbnNvciBGIOKIiCDihJ1ee0PDl0jDl1d9IGlzIGNvbXB1dGVkIGFzIEFfc3VtID0gzqNfYyBGX2vCsiDigJQgc3VtbWluZyBzcXVhcmVkIGFjdGl2YXRpb25zIG92ZXIgdGhlIGNoYW5uZWwgZGltZW5zaW9uLCB5aWVsZGluZyBhIChIw5dXKSBoZWF0bWFwIG9mIFx1MDAyN3doZXJlXHUwMDI3IHRoZSBuZXR3b3JrIGlzIGxvb2tpbmcuIEFmdGVyIG5vcm1hbGl6aW5nIGJ5IHRoZSBGcm9iZW5pdXMgbm9ybSwgdGhlIEFUIGxvc3MgbWluaW1pemVzIM6yLzIgwrcg4oCWxIBfc3R1ZGVudCAtIMSAX3RlYWNoZXLigJbCsi4gVGhpcyBpcyBhcHBsaWVkIGF0IG11bHRpcGxlIGludGVybWVkaWF0ZSBzdGFnZXMgc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBhdHRlbnRpb25fbWFwKGZlYXR1cmU6IHRvcmNoLlRlbnNvciwgbW9kZTogc3RyID0gXHUwMDI3c3VtXHUwMDI3KSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJcbiAgICBDb21wdXRlIHNwYXRpYWwgYXR0ZW50aW9uIG1hcCBmcm9tIEYgaW4gUl57QiB4IEMgeCBIIHggV30uXG4gICAgbW9kZT1cdTAwMjdzdW1cdTAwMjc6IHN1bSBvZiBzcXVhcmVkIGFjdGl2YXRpb25zIG92ZXIgY2hhbm5lbHMgLVx1MDAzZSAoQiwgSCpXKVxuICAgIG1vZGU9XHUwMDI3bWF4XHUwMDI3OiBtYXggYWJzb2x1dGUgYWN0aXZhdGlvbiBvdmVyIGNoYW5uZWxzIC1cdTAwM2UgKEIsIEgqVylcbiAgICBSZXR1cm5zIEwyLW5vcm1hbGl6ZWQgbWFwLlxuICAgIFwiXCJcIlxuICAgIEIgPSBmZWF0dXJlLnNoYXBlWzBdXG4gICAgaWYgbW9kZSA9PSBcdTAwMjdzdW1cdTAwMjc6XG4gICAgICAgIEEgPSBmZWF0dXJlLnBvdygyKS5zdW0oZGltPTEpLnZpZXcoQiwgLTEpICAgICAgICMgKEIsIEgqVylcbiAgICBlbGlmIG1vZGUgPT0gXHUwMDI3bWF4XHUwMDI3OlxuICAgICAgICBBID0gZmVhdHVyZS5hYnMoKS5tYXgoZGltPTEpLnZhbHVlcy52aWV3KEIsIC0xKSAgIyAoQiwgSCpXKVxuICAgIGVsc2U6XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZlx1MDAyN1Vua25vd24gbW9kZToge21vZGV9XHUwMDI3KVxuICAgIHJldHVybiBGLm5vcm1hbGl6ZShBLCBwPTIsIGRpbT0xKVxuXG5kZWYgYXRfbG9zcyhmX3N0dWRlbnQ6IHRvcmNoLlRlbnNvciwgZl90ZWFjaGVyOiB0b3JjaC5UZW5zb3IsIGJldGE6IGZsb2F0ID0gMTAwMC4wKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICBcIlwiXCJBVCBsb3NzOiBiZXRhLzIgKiB8fEFfc3R1ZGVudCAtIEFfdGVhY2hlcnx8XjJcIlwiXCJcbiAgICBBX3MgPSBhdHRlbnRpb25fbWFwKGZfc3R1ZGVudClcbiAgICBBX3QgPSBhdHRlbnRpb25fbWFwKGZfdGVhY2hlcikuZGV0YWNoKClcbiAgICByZXR1cm4gKGJldGEgLyAyLjApICogKEFfcyAtIEFfdCkucG93KDIpLm1lYW4oKVxuXG5cbkIsIEMsIEgsIFcgPSA0LCA2NCwgMTQsIDE0XG5mX3MgPSB0b3JjaC5yYW5kbihCLCBDLCBILCBXKVxuZl90ID0gdG9yY2gucmFuZG4oQiwgQywgSCwgVylcbmxvc3MgPSBhdF9sb3NzKGZfcywgZl90LCBiZXRhPTEwMDAuMClcbnByaW50KGZcdTAwMjdBVCBsb3NzIChzdW0gbW9kZSk6IHtsb3NzLml0ZW0oKTouNGZ9XHUwMDI3KVxuQSA9IGF0dGVudGlvbl9tYXAoZl9zKVxucHJpbnQoZlx1MDAyN0F0dGVudGlvbiBtYXAgc2hhcGU6IHtBLnNoYXBlfSAgKG5vcm0gc2hvdWxkIGJlIH4xKToge0Eubm9ybShkaW09MSkubWVhbigpLml0ZW0oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxheWVyLXRvLUxheWVyIE1hcHBpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNob29zaW5nIHdoaWNoIHN0dWRlbnQgbGF5ZXIgdG8gYWxpZ24gd2l0aCB3aGljaCB0ZWFjaGVyIGxheWVyIHJlcXVpcmVzIGNhcmUuIEEgbWlzbWF0Y2ggaW4gc3BhdGlhbCByZXNvbHV0aW9uIG1ha2VzIGRpcmVjdCBjb21wYXJpc29uIGltcG9zc2libGUgd2l0aG91dCB1cHNhbXBsaW5nLiBUaGUgc3RhbmRhcmQgc3RyYXRlZ3kgaXMgdG8gbWF0Y2ggbGF5ZXJzIGJ5IHRoZWlyIHNwYXRpYWwgcmVzb2x1dGlvbiAoSMOXVyk6IGFmdGVyIGVhY2ggZG93bnNhbXBsaW5nIHN0YWdlIGluIHRoZSB0ZWFjaGVyLCBmaW5kIHRoZSBjb3JyZXNwb25kaW5nIHN0dWRlbnQgbGF5ZXIgd2l0aCB0aGUgc2FtZSBzcGF0aWFsIG91dHB1dCBzaXplLiBGb3IgUmVzTmV0LXN0eWxlIG5ldHdvcmtzIHRoaXMgaXMgc3RyYWlnaHRmb3J3YXJkIOKAlCBlYWNoIHN0YWdlIGN1dHMgc3BhdGlhbCByZXNvbHV0aW9uIGJ5IDLDly4gRm9yIGFyY2hpdGVjdHVyZXMgd2l0aCBkaWZmZXJlbnQgZGVwdGhzLCBhIHJlZ3Jlc3NvciBuZXR3b3JrIHRoYXQgbWFwcyBiZXR3ZWVuIG1pc21hdGNoZWQgcmVzb2x1dGlvbnMgaXMgbmVlZGVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgbWFwX2xheWVyc19ieV9zcGF0aWFsX3NpemUodGVhY2hlcjogbm4uTW9kdWxlLCBzdHVkZW50OiBubi5Nb2R1bGUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlucHV0X3NoYXBlPSgxLCAzLCAzMiwgMzIpKTpcbiAgICBcIlwiXCJcbiAgICBSZWdpc3RlciBmb3J3YXJkIGhvb2tzLCBydW4gYSBkdW1teSBpbnB1dCwgdGhlbiBtYXRjaCBzdHVkZW50L3RlYWNoZXJcbiAgICBDb252MmQgbGF5ZXJzIHRoYXQgc2hhcmUgdGhlIHNhbWUgc3BhdGlhbCBvdXRwdXQgcmVzb2x1dGlvbiAoSCB4IFcpLlxuICAgIFwiXCJcIlxuICAgIHRlYWNoZXJfc2hhcGVzLCBzdHVkZW50X3NoYXBlcyA9IHt9LCB7fVxuXG4gICAgZGVmIG1ha2VfaG9vayhzdG9yZSwgbmFtZSk6XG4gICAgICAgIGRlZiBob29rKF8sIF9fLCBvdXQpOlxuICAgICAgICAgICAgaWYgaXNpbnN0YW5jZShvdXQsIHRvcmNoLlRlbnNvcik6XG4gICAgICAgICAgICAgICAgc3RvcmVbbmFtZV0gPSB0dXBsZShvdXQuc2hhcGVbMjpdKSAgIyAoSCwgVylcbiAgICAgICAgcmV0dXJuIGhvb2tcblxuICAgIHRfaG9va3MgPSBbbS5yZWdpc3Rlcl9mb3J3YXJkX2hvb2sobWFrZV9ob29rKHRlYWNoZXJfc2hhcGVzLCBmXHUwMDI3VC57bn1cdTAwMjcpKVxuICAgICAgICAgICAgICAgZm9yIG4sIG0gaW4gdGVhY2hlci5uYW1lZF9tb2R1bGVzKCkgaWYgaXNpbnN0YW5jZShtLCBubi5Db252MmQpXVxuICAgIHNfaG9va3MgPSBbbS5yZWdpc3Rlcl9mb3J3YXJkX2hvb2sobWFrZV9ob29rKHN0dWRlbnRfc2hhcGVzLCBmXHUwMDI3Uy57bn1cdTAwMjcpKVxuICAgICAgICAgICAgICAgZm9yIG4sIG0gaW4gc3R1ZGVudC5uYW1lZF9tb2R1bGVzKCkgaWYgaXNpbnN0YW5jZShtLCBubi5Db252MmQpXVxuXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIHRlYWNoZXIodG9yY2gucmFuZG4oaW5wdXRfc2hhcGUpKVxuICAgICAgICBzdHVkZW50KHRvcmNoLnJhbmRuKGlucHV0X3NoYXBlKSlcbiAgICBmb3IgaCBpbiB0X2hvb2tzICsgc19ob29rczogaC5yZW1vdmUoKVxuXG4gICAgcHJpbnQoZlx1MDAyN3tcIlRlYWNoZXIgbGF5ZXJcIjpcdTAwM2MzMH0gXHUwMDNjLVx1MDAzZSB7XCJTdHVkZW50IGxheWVyXCI6XHUwMDNjMzB9ICB7XCJIeFdcIn1cdTAwMjcpXG4gICAgcHJpbnQoXHUwMDI3LVx1MDAyNyAqIDc1KVxuICAgIG1hdGNoZWQgPSBbXVxuICAgIGZvciB0X25hbWUsIHRfaHcgaW4gdGVhY2hlcl9zaGFwZXMuaXRlbXMoKTpcbiAgICAgICAgZm9yIHNfbmFtZSwgc19odyBpbiBzdHVkZW50X3NoYXBlcy5pdGVtcygpOlxuICAgICAgICAgICAgaWYgdF9odyA9PSBzX2h3IGFuZCAodF9uYW1lLCBzX25hbWUpIG5vdCBpbiBtYXRjaGVkOlxuICAgICAgICAgICAgICAgIHByaW50KGZcdTAwMjd7dF9uYW1lOlx1MDAzYzMwfSAgICAge3NfbmFtZTpcdTAwM2MzMH0gIHt0X2h3fVx1MDAyNylcbiAgICAgICAgICAgICAgICBtYXRjaGVkLmFwcGVuZCgodF9uYW1lLCBzX25hbWUpKVxuICAgICAgICAgICAgICAgIGJyZWFrXG4gICAgcmV0dXJuIG1hdGNoZWRcblxudGVhY2hlciA9IG5uLlNlcXVlbnRpYWwobm4uQ29udjJkKDMsIDY0LCAzLCBwYWRkaW5nPTEpLCBubi5Db252MmQoNjQsIDEyOCwgMywgc3RyaWRlPTIsIHBhZGRpbmc9MSkpXG5zdHVkZW50ID0gbm4uU2VxdWVudGlhbChubi5Db252MmQoMywgMzIsIDMsIHBhZGRpbmc9MSksIG5uLkNvbnYyZCgzMiwgIDY0LCAzLCBzdHJpZGU9MiwgcGFkZGluZz0xKSlcbm1hcF9sYXllcnNfYnlfc3BhdGlhbF9zaXplKHRlYWNoZXIsIHN0dWRlbnQpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmV5b25kIEZpdE5ldHM6IFBLVCwgQ1JELCBhbmQgTlNUIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZXZlcmFsIG1ldGhvZHMgZXh0ZW5kIHRoZSBmZWF0dXJlIGRpc3RpbGxhdGlvbiBpZGVhLiBQcm9iYWJpbGlzdGljIEtub3dsZWRnZSBUcmFuc2ZlciAoUEtULCBQYXNzYWxpcyAyMDE4KSBtYXRjaGVzIHRoZSBkaXN0cmlidXRpb24gb2Ygc3R1ZGVudCBhbmQgdGVhY2hlciBmZWF0dXJlcyBieSBtaW5pbWl6aW5nIGEga2VybmVsLWJhc2VkIGRpc3RhbmNlIGJldHdlZW4gdGhlaXIgZmVhdHVyZSBzaW1pbGFyaXR5IG1hdHJpY2VzIOKAlCBhbiBPKE7Csikgb3BlcmF0aW9uIG92ZXIgYSBiYXRjaC4gQ29udHJhc3RpdmUgUmVwcmVzZW50YXRpb24gRGlzdGlsbGF0aW9uIChDUkQsIFRpYW4gMjAyMCkgdXNlcyBhIGNvbnRyYXN0aXZlIG9iamVjdGl2ZTogc3R1ZGVudCBmZWF0dXJlcyBzaG91bGQgYmUgc2ltaWxhciB0byB0aGUgdGVhY2hlclx1MDAyN3MgZmVhdHVyZXMgZm9yIHRoZSBzYW1lIHNhbXBsZSBhbmQgZGlzc2ltaWxhciB0byBmZWF0dXJlcyBmcm9tIG90aGVyIHNhbXBsZXMgaW4gYSBtZW1vcnkgYmFuay4gTmV1cm9uIFNlbGVjdGl2aXR5IFRyYW5zZmVyIChOU1QpIG1hdGNoZXMgaGlnaGVyLW9yZGVyIHN0YXRpc3RpY3Mgb2YgdGhlIGZlYXR1cmUgZGlzdHJpYnV0aW9ucy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQ2hvb3NpbmcgQmV0d2VlbiBMb2dpdCBLRCBhbmQgRmVhdHVyZSBEaXN0aWxsYXRpb24iLCJjb250ZW50IjoiTG9naXQgS0QgaXMgc2ltcGxlciBhbmQgb2Z0ZW4gc3VmZmljaWVudCB3aGVuIHRlYWNoZXIgYW5kIHN0dWRlbnQgaGF2ZSBzaW1pbGFyIGRlcHRocy4gVXNlIGZlYXR1cmUgZGlzdGlsbGF0aW9uIChGaXROZXRzIG9yIEFUKSB3aGVuIHRoZSBzdHVkZW50IGlzIG11Y2ggc2hhbGxvd2VyIOKAlCB0aGUgaW50ZXJtZWRpYXRlIHN1cGVydmlzaW9uIGd1aWRlcyB0aGUgc3R1ZGVudCB0aHJvdWdoIGxheWVycyB0aGF0IHdvdWxkIG90aGVyd2lzZSByZWNlaXZlIG5vIGRpcmVjdCBncmFkaWVudCBzaWduYWwgZnJvbSB0aGUgdGFzay4gQ1JEIGlzIHRoZSBzdHJvbmdlc3Qgc2luZ2xlIG1ldGhvZCBieSBiZW5jaG1hcmsgYnV0IHJlcXVpcmVzIGEgbWVtb3J5IGJhbmsgYW5kIGJhdGNoIHNpemUgdHVuaW5nOyBBVCBpcyB0aGUgYmVzdCBzaW1wbGljaXR5LXZzLWdhaW4gdHJhZGUtb2ZmLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBSZWNvbW1lbmRhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBGaXROZXRzLCBzZWxlY3QgdGhlIGhpbnQgbGF5ZXIgYXQgcm91Z2hseSB0aGUgbWlkcG9pbnQgb2YgdGhlIHRlYWNoZXIgbmV0d29yaywgYW5kIHRoZSBndWlkZWQgbGF5ZXIgYXQgdGhlIG1pZHBvaW50IG9mIHRoZSBzdHVkZW50LiBVc2UgYSAxw5cxIGNvbnYgYWRhcHRlciBpZiBjaGFubmVsIGNvdW50cyBkaWZmZXI7IGJpbGluZWFyIGludGVycG9sYXRpb24gaWYgc3BhdGlhbCBzaXplcyBkaWZmZXIuIFJ1biBTdGFnZSAxIGZvciAyMOKAkzMwJSBvZiB0aGUgdG90YWwgdHJhaW5pbmcgYnVkZ2V0LCB0aGVuIFN0YWdlIDIgZm9yIHRoZSByZW1haW5kZXIuIFJlZHVjZSB0aGUgbGVhcm5pbmcgcmF0ZSBieSAxMMOXIGZvciBTdGFnZSAyIHJlbGF0aXZlIHRvIFN0YWdlIDEgdG8gYXZvaWQgZGlzcnVwdGluZyB0aGUgaGludC1iYXNlZCBpbml0aWFsaXphdGlvbi4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkhpbnQgbGF5ZXI6IHRlYWNoZXIgbWlkcG9pbnQgKGUuZy4sIGxheWVyIDggb2YgMTYpOyBndWlkZWQgbGF5ZXI6IHN0dWRlbnQgbWlkcG9pbnQgKGUuZy4sIGxheWVyIDQgb2YgOCkuIiwiQWRhcHRlciBXX2g6IDHDlzEgY29udiDigJQgYWRkcyBvbmx5IENfUyDDlyBDX1QgcGFyYW1ldGVycywgbmVnbGlnaWJsZSBjb3N0LiIsIlN0YWdlIDEgYnVkZ2V0OiAyMOKAkzMwJSBvZiB0b3RhbCBlcG9jaHM7IFN0YWdlIDI6IHJlbWFpbmluZyA3MOKAkzgwJSB3aXRoIGxvZ2l0IEtELiIsIkFUIGJldGEgaHlwZXJwYXJhbWV0ZXI6IM6yPTEwMDAgaXMgdGhlIGRlZmF1bHQgZnJvbSB0aGUgcGFwZXI7IHNjYWxlIGRvd24gaWYgQVQgbG9zcyBkb21pbmF0ZXMuIiwiQ1JEIG1lbW9yeSBiYW5rIHNpemU6IDQwOTbigJMxNjM4NCBuZWdhdGl2ZXM7IGxhcmdlciBiYW5rcyBnaXZlIGJldHRlciBjb250cmFzdGl2ZSBzaWduYWwuIiwiTGF5ZXIgbWlzbWF0Y2g6IGlmIHRlYWNoZXIgYW5kIHN0dWRlbnQgaGF2ZSBkaWZmZXJlbnQgZGVwdGhzLCBhcHBseSBBVCBvbmx5IGF0IHRoZSBsYXN0IDLigJMzIHN0YWdlcyB3aGVyZSBzcGF0aWFsIHNpemVzIG1hdGNoLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGZWF0dXJlIERpc3RpbGxhdGlvbiBNZXRob2QgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJNYXRjaGVkIFF1YW50aXR5IiwiQWRhcHRlciBOZWVkZWQiLCJBY2N1cmFjeSBHYWluIChDSUZBUi0xMDApIiwiQ29tcHV0YXRpb24gT3ZlcmhlYWQiXSwicm93cyI6W1siTG9naXQgS0QgKEhpbnRvbikiLCJPdXRwdXQgcHJvYmFiaWxpdGllcyIsIk5vbmUiLCIrMS414oCTMi41JSIsIkxvdyDigJQgb25lIHRlYWNoZXIgZm9yd2FyZCBwYXNzIl0sWyJGaXROZXRzIiwiSW50ZXJtZWRpYXRlIGZlYXR1cmUgbWFwcyAoTDIpIiwiMcOXMSBjb252IChXX2gpIiwiKzIuNeKAkzQuMCUiLCJNZWRpdW0g4oCUIHR3byB0cmFpbmluZyBzdGFnZXMiXSxbIkFUIChaYWdvcnV5a28pIiwiU3BhdGlhbCBhdHRlbnRpb24gbWFwcyIsIk5vbmUiLCIrMi4w4oCTMy41JSIsIkxvdyDigJQgYXR0ZW50aW9uIG1hcCBjb21wdXRhdGlvbiBvbmx5Il0sWyJQS1QiLCJLZXJuZWwtYmFzZWQgZmVhdHVyZSBzaW1pbGFyaXR5IiwiUHJvamVjdGlvbiBoZWFkIiwiKzIuMOKAkzMuMCUiLCJNZWRpdW0g4oCUIE8oTsKyKSBrZXJuZWwgbWF0cml4Il0sWyJDUkQgKFRpYW4gMjAyMCkiLCJDb250cmFzdGl2ZSBwYWlyIHNpbWlsYXJpdHkiLCJQcm9qZWN0aW9uIE1MUCIsIiszLjXigJM1LjAlIiwiSGlnaCDigJQgbWVtb3J5IGJhbmsgcmVxdWlyZWQiXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Feature Map Distillation — FitNets and Intermediate Representations

Output-only knowledge distillation transfers only the teacher's final predictions. This misses the rich intermediate representations built up across the teacher's layers — representations encoding edges, textures, object parts, and semantic structure. Feature map distillation methods transfer these internal representations directly, giving the student a richer training signal and better initialization for learning the task.

## FitNets and Hint Layer Training

FitNets (Romero et al. 2015) extend distillation to intermediate layers. A 'hint layer' in the teacher and a 'guided layer' in the student are chosen at matching depths. The student is trained to predict the teacher's hint layer output: L_hint = ‖W_h(F_student) - F_teacher‖², where W_h is a 1×1 convolutional adapter that projects the student's feature map to the teacher's channel dimension. This forces the student to build the same intermediate representations as the teacher, not just match final predictions.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class HintLoss(nn.Module):
    """FitNets hint loss: align student feature map to teacher via 1x1 conv adapter."""

    def __init__(self, student_channels: int, teacher_channels: int):
        super().__init__()
        # Adapter W_h: maps student dim -> teacher dim
        self.adapter = nn.Conv2d(student_channels, teacher_channels,
                                 kernel_size=1, bias=False)

    def forward(self, f_student: torch.Tensor, f_teacher: torch.Tensor) -> torch.Tensor:
        """
        f_student: (B, C_S, H, W)  student intermediate feature map
        f_teacher: (B, C_T, H, W)  teacher intermediate feature map (detached)
        Returns: ||W_h(F_s) - F_t||^2 / N
        """
        f_adapted = self.adapter(f_student)           # (B, C_T, H, W)
        return F.mse_loss(f_adapted, f_teacher.detach())


torch.manual_seed(0)
B, H, W = 4, 14, 14
C_teacher, C_student = 256, 128

f_teacher = torch.randn(B, C_teacher, H, W)
f_student  = torch.randn(B, C_student,  H, W)

hint = HintLoss(C_student, C_teacher)
loss = hint(f_student, f_teacher)
print(f'Hint loss: {loss.item():.4f}')
print(f'Adapter: {C_student} -> {C_teacher} channels, params: {sum(p.numel() for p in hint.parameters())}')
```

## Two-Stage Training: Hint Then KD

FitNets use two training stages. Stage 1 (hint training): optimize only the hint loss L_hint to align the student's intermediate feature map with the teacher's hint layer. This gives the student a better starting point than random initialization. Stage 2 (KD training): discard the adapter and train the full student with the standard logit-level distillation loss using the teacher's output probabilities. The two-stage schedule consistently outperforms single-stage logit KD, especially for deep students trained on small datasets.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

def stage1_hint_training(student, teacher, hint_loss_fn, loader, device, epochs=2, lr=1e-3):
    """Stage 1: train student to match teacher intermediate feature maps."""
    params = list(student.parameters()) + list(hint_loss_fn.parameters())
    optimizer = optim.Adam(params, lr=lr)
    for epoch in range(epochs):
        total = 0.0
        for X, _ in loader:
            X = X.to(device)
            with torch.no_grad():
                f_teacher = teacher.get_hint_features(X)
            f_student = student.get_guided_features(X)
            loss = hint_loss_fn(f_student, f_teacher)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total += loss.item()
        print(f'  Hint epoch {epoch+1}: hint_loss={total/len(loader):.4f}')

def stage2_kd_training(student, teacher, loader, device,
                        temperature=4.0, alpha=0.5, epochs=5, lr=5e-4):
    """Stage 2: full KD with teacher logits (hint adapter is discarded)."""
    optimizer = optim.Adam(student.parameters(), lr=lr)
    T = temperature
    for epoch in range(epochs):
        total = 0.0
        for X, y in loader:
            X, y = X.to(device), y.to(device)
            with torch.no_grad():
                t_logits = teacher(X)
            s_logits = student(X)
            hard = F.cross_entropy(s_logits, y)
            soft = F.kl_div(F.log_softmax(s_logits / T, dim=-1),
                            F.softmax(t_logits / T, dim=-1),
                            reduction='batchmean') * T ** 2
            loss = alpha * hard + (1 - alpha) * soft
            optimizer.zero_grad(); loss.backward(); optimizer.step()
            total += loss.item()
        print(f'  KD epoch {epoch+1}: loss={total/len(loader):.4f}')

print('Two-stage FitNets: stage1=hint alignment, stage2=full logit KD.')
```

## Attention Transfer (AT) Loss

Attention Transfer (Zagoruyko & Komodakis 2017) distills spatial attention maps rather than raw feature values. The attention map from feature tensor F ∈ ℝ^{C×H×W} is computed as A_sum = Σ_c F_k² — summing squared activations over the channel dimension, yielding a (H×W) heatmap of 'where' the network is looking. After normalizing by the Frobenius norm, the AT loss minimizes β/2 · ‖Ā_student - Ā_teacher‖². This is applied at multiple intermediate stages simultaneously.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def attention_map(feature: torch.Tensor, mode: str = 'sum') -> torch.Tensor:
    """
    Compute spatial attention map from F in R^{B x C x H x W}.
    mode='sum': sum of squared activations over channels -> (B, H*W)
    mode='max': max absolute activation over channels -> (B, H*W)
    Returns L2-normalized map.
    """
    B = feature.shape[0]
    if mode == 'sum':
        A = feature.pow(2).sum(dim=1).view(B, -1)       # (B, H*W)
    elif mode == 'max':
        A = feature.abs().max(dim=1).values.view(B, -1)  # (B, H*W)
    else:
        raise ValueError(f'Unknown mode: {mode}')
    return F.normalize(A, p=2, dim=1)

def at_loss(f_student: torch.Tensor, f_teacher: torch.Tensor, beta: float = 1000.0) -> torch.Tensor:
    """AT loss: beta/2 * ||A_student - A_teacher||^2"""
    A_s = attention_map(f_student)
    A_t = attention_map(f_teacher).detach()
    return (beta / 2.0) * (A_s - A_t).pow(2).mean()


B, C, H, W = 4, 64, 14, 14
f_s = torch.randn(B, C, H, W)
f_t = torch.randn(B, C, H, W)
loss = at_loss(f_s, f_t, beta=1000.0)
print(f'AT loss (sum mode): {loss.item():.4f}')
A = attention_map(f_s)
print(f'Attention map shape: {A.shape}  (norm should be ~1): {A.norm(dim=1).mean().item():.4f}')
```

## Layer-to-Layer Mapping

Choosing which student layer to align with which teacher layer requires care. A mismatch in spatial resolution makes direct comparison impossible without upsampling. The standard strategy is to match layers by their spatial resolution (H×W): after each downsampling stage in the teacher, find the corresponding student layer with the same spatial output size. For ResNet-style networks this is straightforward — each stage cuts spatial resolution by 2×. For architectures with different depths, a regressor network that maps between mismatched resolutions is needed.

```python
import torch
import torch.nn as nn

def map_layers_by_spatial_size(teacher: nn.Module, student: nn.Module,
                                input_shape=(1, 3, 32, 32)):
    """
    Register forward hooks, run a dummy input, then match student/teacher
    Conv2d layers that share the same spatial output resolution (H x W).
    """
    teacher_shapes, student_shapes = {}, {}

    def make_hook(store, name):
        def hook(_, __, out):
            if isinstance(out, torch.Tensor):
                store[name] = tuple(out.shape[2:])  # (H, W)
        return hook

    t_hooks = [m.register_forward_hook(make_hook(teacher_shapes, f'T.{n}'))
               for n, m in teacher.named_modules() if isinstance(m, nn.Conv2d)]
    s_hooks = [m.register_forward_hook(make_hook(student_shapes, f'S.{n}'))
               for n, m in student.named_modules() if isinstance(m, nn.Conv2d)]

    with torch.no_grad():
        teacher(torch.randn(input_shape))
        student(torch.randn(input_shape))
    for h in t_hooks + s_hooks: h.remove()

    print(f'{"Teacher layer":<30} <-> {"Student layer":<30}  {"HxW"}')
    print('-' * 75)
    matched = []
    for t_name, t_hw in teacher_shapes.items():
        for s_name, s_hw in student_shapes.items():
            if t_hw == s_hw and (t_name, s_name) not in matched:
                print(f'{t_name:<30}     {s_name:<30}  {t_hw}')
                matched.append((t_name, s_name))
                break
    return matched

teacher = nn.Sequential(nn.Conv2d(3, 64, 3, padding=1), nn.Conv2d(64, 128, 3, stride=2, padding=1))
student = nn.Sequential(nn.Conv2d(3, 32, 3, padding=1), nn.Conv2d(32,  64, 3, stride=2, padding=1))
map_layers_by_spatial_size(teacher, student)
```

## Beyond FitNets: PKT, CRD, and NST

Several methods extend the feature distillation idea. Probabilistic Knowledge Transfer (PKT, Passalis 2018) matches the distribution of student and teacher features by minimizing a kernel-based distance between their feature similarity matrices — an O(N²) operation over a batch. Contrastive Representation Distillation (CRD, Tian 2020) uses a contrastive objective: student features should be similar to the teacher's features for the same sample and dissimilar to features from other samples in a memory bank. Neuron Selectivity Transfer (NST) matches higher-order statistics of the feature distributions.

> **Choosing Between Logit KD and Feature Distillation**: Logit KD is simpler and often sufficient when teacher and student have similar depths. Use feature distillation (FitNets or AT) when the student is much shallower — the intermediate supervision guides the student through layers that would otherwise receive no direct gradient signal from the task. CRD is the strongest single method by benchmark but requires a memory bank and batch size tuning; AT is the best simplicity-vs-gain trade-off.

## Practical Recommendations

For FitNets, select the hint layer at roughly the midpoint of the teacher network, and the guided layer at the midpoint of the student. Use a 1×1 conv adapter if channel counts differ; bilinear interpolation if spatial sizes differ. Run Stage 1 for 20–30% of the total training budget, then Stage 2 for the remainder. Reduce the learning rate by 10× for Stage 2 relative to Stage 1 to avoid disrupting the hint-based initialization.

- Hint layer: teacher midpoint (e.g., layer 8 of 16); guided layer: student midpoint (e.g., layer 4 of 8).
- Adapter W_h: 1×1 conv — adds only C_S × C_T parameters, negligible cost.
- Stage 1 budget: 20–30% of total epochs; Stage 2: remaining 70–80% with logit KD.
- AT beta hyperparameter: β=1000 is the default from the paper; scale down if AT loss dominates.
- CRD memory bank size: 4096–16384 negatives; larger banks give better contrastive signal.
- Layer mismatch: if teacher and student have different depths, apply AT only at the last 2–3 stages where spatial sizes match.

## Feature Distillation Method Comparison

| Method | Matched Quantity | Adapter Needed | Accuracy Gain (CIFAR-100) | Computation Overhead |
| --- | --- | --- | --- | --- |
| Logit KD (Hinton) | Output probabilities | None | +1.5–2.5% | Low — one teacher forward pass |
| FitNets | Intermediate feature maps (L2) | 1×1 conv (W_h) | +2.5–4.0% | Medium — two training stages |
| AT (Zagoruyko) | Spatial attention maps | None | +2.0–3.5% | Low — attention map computation only |
| PKT | Kernel-based feature similarity | Projection head | +2.0–3.0% | Medium — O(N²) kernel matrix |
| CRD (Tian 2020) | Contrastive pair similarity | Projection MLP | +3.5–5.0% | High — memory bank required |

---

