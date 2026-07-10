---
title: "Attention Transfer — Spatial Attention Map Distillation"
slug: "attention-transfer-distillation"
description: "Transfer where the teacher looks by matching spatial attention maps computed from intermediate feature tensors. Covers sum-squared and max attention maps, multi-stage AT loss, gradient-based attention, combined AT and logit KD training, and SemCKD cross-layer attention transfer."
tags: ["deep-learning", "model-compression", "knowledge-distillation"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXR0ZW50aW9uIFRyYW5zZmVyIChaYWdvcnV5a28gXHUwMDI2IEtvbW9kYWtpcyAyMDE3KSBkaXN0aWxscyBub3Qgd2hhdCB0aGUgdGVhY2hlciBrbm93cyBidXQgd2hlcmUgaXQgbG9va3MuIEEgd2VsbC10cmFpbmVkIHRlYWNoZXIgaGFzIGxlYXJuZWQgdG8gZm9jdXMgb24gZGlzY3JpbWluYXRpdmUgcmVnaW9ucyDigJQgdGhlIGFuaW1hbFx1MDAyN3MgZmFjZSByYXRoZXIgdGhhbiB0aGUgYmFja2dyb3VuZCwgdGhlIHdoZWVsIGFyY2ggcmF0aGVyIHRoYW4gdGhlIGNhciBkb29yLiBUaGUgc3R1ZGVudCBzaG91bGQgbG9vayBhdCB0aG9zZSBzYW1lIHJlZ2lvbnMuIEFUIGNvbXB1dGVzIGEgc3BhdGlhbCBhdHRlbnRpb24gbWFwIGZyb20gZWFjaCBpbnRlcm1lZGlhdGUgZmVhdHVyZSB0ZW5zb3IgYW5kIHBlbmFsaXplcyB0aGUgc3R1ZGVudCBmb3IgbG9va2luZyBhdCBkaWZmZXJlbnQgcmVnaW9ucyB0aGFuIHRoZSB0ZWFjaGVyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF0dGVudGlvbiBNYXAgQ29tcHV0YXRpb246IFN1bSwgTWF4LCBhbmQgTDIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdpdmVuIGEgZmVhdHVyZSB0ZW5zb3IgRiDiiIgg4oSdXntDw5dIw5dXfSwgdGhyZWUgYXR0ZW50aW9uIG1hcCB2YXJpYW50cyBhcmUgY29tbW9ubHkgdXNlZC4gU3VtLXNxdWFyZWQgKGRlZmF1bHQgQVQpOiBBX3N1bSA9IM6jX2MgRl9rwrIg4oCUIHN1bSBvZiBzcXVhcmVkIGFjdGl2YXRpb25zIG92ZXIgY2hhbm5lbHMsIHByb2R1Y2luZyBhIChIw5dXKSBoZWF0bWFwLiBNYXggYWJzb2x1dGU6IEFfbWF4ID0gbWF4X2MgfEZfa3wg4oCUIG1heGltdW0gYWJzb2x1dGUgYWN0aXZhdGlvbiBvdmVyIGNoYW5uZWxzLiBMMiBub3JtOiBBX2wyID0g4oCWRl9r4oCWXzIgb3ZlciBjaGFubmVscy4gQWxsIG1hcHMgYXJlIG5vcm1hbGl6ZWQgYnkgdGhlaXIgRnJvYmVuaXVzIG5vcm06IMSAID0gQSAvIOKAlkHigJZfRi4gVGhlIHN1bS1zcXVhcmVkIHZhcmlhbnQgaXMgdGhlIHN0YW5kYXJkIGNob2ljZSBhbmQgcGVyZm9ybXMgYmVzdCBpbiBwcmFjdGljZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBjb21wdXRlX2F0dGVudGlvbl9tYXBzKGZlYXR1cmU6IHRvcmNoLlRlbnNvcik6XG4gICAgXCJcIlwiXG4gICAgQ29tcHV0ZSB0aHJlZSBhdHRlbnRpb24gbWFwIHZhcmlhbnRzIGZyb20gRiBpbiBSXntCIHggQyB4IEggeCBXfS5cbiAgICBBbGwgbWFwcyBub3JtYWxpemVkIHRvIHVuaXQgTDIgbm9ybSBwZXIgc2FtcGxlLlxuICAgIFJldHVybnM6IChBX3N1bSwgQV9tYXgsIEFfbDIpIGVhY2ggb2Ygc2hhcGUgKEIsIEgqVykuXG4gICAgXCJcIlwiXG4gICAgQiwgQywgSCwgVyA9IGZlYXR1cmUuc2hhcGVcblxuICAgIEFfc3VtID0gZmVhdHVyZS5wb3coMikuc3VtKGRpbT0xKS52aWV3KEIsIC0xKSAgICAgICAjIChCLCBIKlcpXG4gICAgQV9tYXggPSBmZWF0dXJlLmFicygpLm1heChkaW09MSkudmFsdWVzLnZpZXcoQiwgLTEpICAjIChCLCBIKlcpXG4gICAgQV9sMiAgPSBmZWF0dXJlLm5vcm0ocD0yLCBkaW09MSkudmlldyhCLCAtMSkgICAgICAgICAjIChCLCBIKlcpXG5cbiAgICBub3JtYWxpemUgPSBsYW1iZGEgQTogRi5ub3JtYWxpemUoQSwgcD0yLCBkaW09MSlcbiAgICByZXR1cm4gbm9ybWFsaXplKEFfc3VtKSwgbm9ybWFsaXplKEFfbWF4KSwgbm9ybWFsaXplKEFfbDIpXG5cblxudG9yY2gubWFudWFsX3NlZWQoNylcbkIsIEMsIEgsIFcgPSA0LCAxMjgsIDgsIDhcbmZlYXR1cmUgPSB0b3JjaC5yYW5kbihCLCBDLCBILCBXKVxuXG5BX3N1bSwgQV9tYXgsIEFfbDIgPSBjb21wdXRlX2F0dGVudGlvbl9tYXBzKGZlYXR1cmUpXG5wcmludChmXHUwMDI3RmVhdHVyZSBzaGFwZTogICB7ZmVhdHVyZS5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3QXR0ZW50aW9uIHNoYXBlczogc3VtPXtBX3N1bS5zaGFwZX0gIG1heD17QV9tYXguc2hhcGV9ICBsMj17QV9sMi5zaGFwZX1cdTAwMjcpXG5cbiMgQ3Jvc3MtdmFyaWFudCBjb3JyZWxhdGlvbiAoc2hvdWxkIGJlIGhpZ2gg4oCUIGFsbCBjYXB0dXJlIHNpbWlsYXIgc3BhdGlhbCBzdHJ1Y3R1cmUpXG5jb3JyX3NtID0gKEFfc3VtICogQV9tYXgpLnN1bSgxKS5tZWFuKCkuaXRlbSgpXG5jb3JyX3NsID0gKEFfc3VtICogQV9sMikuc3VtKDEpLm1lYW4oKS5pdGVtKClcbnByaW50KGZcdTAwMjdDb3JyZWxhdGlvbiBzdW0tbWF4OiB7Y29ycl9zbTouNGZ9ICAgc3VtLWwyOiB7Y29ycl9zbDouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3U3VtLW9mLXNxdWFyZXMgaXMgc3RhbmRhcmQgKFphZ29ydXlrbyBcdTAwMjYgS29tb2Rha2lzIDIwMTcpLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBVCBMb3NzIGF0IE11bHRpcGxlIEludGVybWVkaWF0ZSBMYXllcnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFwcGx5aW5nIEFUIGF0IGEgc2luZ2xlIGxheWVyIHByb3ZpZGVzIGxpbWl0ZWQgc3VwZXJ2aXNpb24uIFRoZSBmdWxsIEFUIG1ldGhvZCBhcHBsaWVzIHRoZSBsb3NzIGFmdGVyIGVhY2ggbWFqb3Igc3RhZ2UgKGUuZy4sIGFmdGVyIGVhY2ggcmVzaWR1YWwgYmxvY2sgZ3JvdXAgaW4gUmVzTmV0KS4gVGhpcyBtZWFucyB0aGUgc3R1ZGVudCBpcyBndWlkZWQgdG8gbG9vayBpbiB0aGUgcmlnaHQgcGxhY2VzIGF0IGV2ZXJ5IGxldmVsIG9mIGFic3RyYWN0aW9uIOKAlCBsb3ctbGV2ZWwgdGV4dHVyZSByZWdpb25zIGluIGVhcmx5IHN0YWdlcywgc2VtYW50aWMgb2JqZWN0IHJlZ2lvbnMgaW4gbGF0ZXIgc3RhZ2VzLiBUaGUgdG90YWwgQVQgbG9zcyBpcyB0aGUgc3VtIGFjcm9zcyBhbGwgcGFpcmVkIHN0YWdlcywgZWFjaCB3ZWlnaHRlZCBieSB0aGUgc2FtZSDOsi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGF0X21hcChmZWF0dXJlOiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlN1bS1vZi1zcXVhcmVkIGNoYW5uZWxzIGF0dGVudGlvbiBtYXAsIEwyLW5vcm1hbGl6ZWQuIFNoYXBlOiAoQiwgSCpXKS5cIlwiXCJcbiAgICBCID0gZmVhdHVyZS5zaGFwZVswXVxuICAgIEEgPSBmZWF0dXJlLnBvdygyKS5zdW0oZGltPTEpLnZpZXcoQiwgLTEpXG4gICAgcmV0dXJuIEYubm9ybWFsaXplKEEsIHA9MiwgZGltPTEpXG5cbmNsYXNzIE11bHRpU3RhZ2VBVExvc3Mobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJBVCBsb3NzIHN1bW1lZCBvdmVyIG11bHRpcGxlIHBhaXJlZCBmZWF0dXJlIG1hcCBzdGFnZXMuXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmV0YTogZmxvYXQgPSAxMDAwLjApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5iZXRhID0gYmV0YVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgc3R1ZGVudF9mZWF0czogbGlzdCwgdGVhY2hlcl9mZWF0czogbGlzdCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIGFzc2VydCBsZW4oc3R1ZGVudF9mZWF0cykgPT0gbGVuKHRlYWNoZXJfZmVhdHMpXG4gICAgICAgIGRldmljZSA9IHN0dWRlbnRfZmVhdHNbMF0uZGV2aWNlXG4gICAgICAgIHRvdGFsID0gdG9yY2guemVyb3MoMSwgZGV2aWNlPWRldmljZSlcbiAgICAgICAgZm9yIGZzLCBmdCBpbiB6aXAoc3R1ZGVudF9mZWF0cywgdGVhY2hlcl9mZWF0cyk6XG4gICAgICAgICAgICBBX3MgPSBhdF9tYXAoZnMpXG4gICAgICAgICAgICBBX3QgPSBhdF9tYXAoZnQpLmRldGFjaCgpXG4gICAgICAgICAgICBpZiBBX3Muc2hhcGUgIT0gQV90LnNoYXBlOiAgIyByZXNhbXBsZSBpZiBzcGF0aWFsIHNpemVzIGRpZmZlclxuICAgICAgICAgICAgICAgIEFfdCA9IEYuaW50ZXJwb2xhdGUoQV90LnVuc3F1ZWV6ZSgxKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNpemU9QV9zLnNoYXBlWy0xXSwgbW9kZT1cdTAwMjdsaW5lYXJcdTAwMjcpLnNxdWVlemUoMSlcbiAgICAgICAgICAgIHRvdGFsID0gdG90YWwgKyAoc2VsZi5iZXRhIC8gMi4wKSAqIChBX3MgLSBBX3QpLnBvdygyKS5tZWFuKClcbiAgICAgICAgcmV0dXJuIHRvdGFsXG5cblxuIyBEZW1vOiAzLXN0YWdlIFJlc05ldC1zdHlsZSBmZWF0dXJlIG1hcHMgKHRlYWNoZXIgd2lkZXIgdGhhbiBzdHVkZW50KVxuQiA9IDRcbnN0dWRlbnRfZmVhdHMgPSBbdG9yY2gucmFuZG4oQiwgIDY0LCAyOCwgMjgpLFxuICAgICAgICAgICAgICAgICB0b3JjaC5yYW5kbihCLCAxMjgsIDE0LCAxNCksXG4gICAgICAgICAgICAgICAgIHRvcmNoLnJhbmRuKEIsIDI1NiwgIDcsICA3KV1cbnRlYWNoZXJfZmVhdHMgPSBbdG9yY2gucmFuZG4oQiwgMTI4LCAyOCwgMjgpLFxuICAgICAgICAgICAgICAgICB0b3JjaC5yYW5kbihCLCAyNTYsIDE0LCAxNCksXG4gICAgICAgICAgICAgICAgIHRvcmNoLnJhbmRuKEIsIDUxMiwgIDcsICA3KV1cblxuYXRfbG9zcyA9IE11bHRpU3RhZ2VBVExvc3MoYmV0YT0xMDAwLjApXG5sb3NzID0gYXRfbG9zcyhzdHVkZW50X2ZlYXRzLCB0ZWFjaGVyX2ZlYXRzKVxucHJpbnQoZlx1MDAyN011bHRpLXN0YWdlIEFUIGxvc3MgKDMgc3RhZ2VzKToge2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQtQmFzZWQgQXR0ZW50aW9uIE1hcHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuIGFsdGVybmF0aXZlIHRvIGFjdGl2YXRpb24tYmFzZWQgbWFwcyBpcyBncmFkaWVudC1iYXNlZCBhdHRlbnRpb246IHRoZSBKYWNvYmlhbiBvZiB0aGUgbW9kZWxcdTAwMjdzIG91dHB1dCB3aXRoIHJlc3BlY3QgdG8gYW4gaW50ZXJtZWRpYXRlIGZlYXR1cmUgdGVuc29yLiDiiIJ5L+KIgkZfayBjYXB0dXJlcyBob3cgc2Vuc2l0aXZlIHRoZSBmaW5hbCBwcmVkaWN0aW9uIGlzIHRvIGVhY2ggc3BhdGlhbCBsb2NhdGlvbiBpbiBsYXllciBrIOKAlCBhIG1vcmUgaW5mb3JtYXRpdmUgc2lnbmFsIHRoYW4gcmF3IGFjdGl2YXRpb24gbWFnbml0dWRlcy4gR3JhZENBTS1zdHlsZSBhdHRlbnRpb24gY29tYmluZXMgZ3JhZGllbnRzIGFuZCBhY3RpdmF0aW9uczogQV9HcmFkQ0FNID0gUmVMVSjOo19jICjiiIJ5L+KIgkZfYykgwrcgRl9jKS4gVGhlIGNvc3QgaXMgb25lIGFkZGl0aW9uYWwgYmFja3dhcmQgcGFzcyBwZXIgbGF5ZXI7IGltcHJhY3RpY2FsIGZvciBhbGwgbGF5ZXJzIGJ1dCBlZmZlY3RpdmUgYXQgYSBzaW5nbGUgY2FyZWZ1bGx5IGNob3NlbiBsYXllci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWaXN1YWxpemluZyBUZWFjaGVyIHZzIFN0dWRlbnQgQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZWZvcmUgYW5kIGFmdGVyIEFUIHRyYWluaW5nLCBjb21wYXJpbmcgdGhlIHRlYWNoZXJcdTAwMjdzIGFuZCBzdHVkZW50XHUwMDI3cyBhdHRlbnRpb24gbWFwcyByZXZlYWxzIHdoZXRoZXIgdGhlIHN0dWRlbnQgaGFzIGxlYXJuZWQgdG8gbG9vayBhdCB0aGUgcmlnaHQgaW1hZ2UgcmVnaW9ucy4gSGlnaCBjb3NpbmUgc2ltaWxhcml0eSBiZXR3ZWVuIHRoZSBmbGF0dGVuZWQsIG5vcm1hbGl6ZWQgbWFwcyBpbmRpY2F0ZXMgc3VjY2Vzc2Z1bCBhdHRlbnRpb24gdHJhbnNmZXIuIEluIHByYWN0aWNlLCBhIHN0dWRlbnQgdHJhaW5lZCB3aXRoIEFUIHNob3dzIG11Y2ggaGlnaGVyIGNvc2luZSBzaW1pbGFyaXR5IHRvIHRoZSB0ZWFjaGVyXHUwMDI3cyBtYXBzIHRoYW4gYSBzdHVkZW50IHRyYWluZWQgd2l0aCBsb2dpdCBLRCBhbG9uZSwgd2hpY2ggZXhwbGFpbnMgdGhlIGFjY3VyYWN5IGltcHJvdmVtZW50IOKAlCB0aGUgc3R1ZGVudCBsaXRlcmFsbHkgZm9jdXNlcyBvbiB0aGUgY29ycmVjdCBkaXNjcmltaW5hdGl2ZSByZWdpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgYXR0ZW50aW9uX2hlYXRtYXAoZmVhdHVyZTogdG9yY2guVGVuc29yKSAtXHUwMDNlIG5wLm5kYXJyYXk6XG4gICAgXCJcIlwiQ29udmVydCBhIHNpbmdsZS1zYW1wbGUgZmVhdHVyZSAoQywgSCwgVykgdG8gYSBub3JtYWxpemVkIChILCBXKSBoZWF0bWFwLlwiXCJcIlxuICAgIEEgPSBmZWF0dXJlLnBvdygyKS5zdW0oZGltPTApLmRldGFjaCgpLmNwdSgpLm51bXB5KCkgICMgKEgsIFcpXG4gICAgcmV0dXJuIChBIC0gQS5taW4oKSkgLyAoQS5tYXgoKSAtIEEubWluKCkgKyAxZS02KVxuXG5kZWYgY29tcGFyZV9hdHRlbnRpb25fbWFwcyh0ZWFjaGVyX2ZlYXQ6IHRvcmNoLlRlbnNvciwgc3R1ZGVudF9mZWF0OiB0b3JjaC5UZW5zb3IpOlxuICAgIFwiXCJcIlByaW50IHN0YXRpc3RpY3MgY29tcGFyaW5nIHRlYWNoZXIgYW5kIHN0dWRlbnQgc3BhdGlhbCBhdHRlbnRpb24uXCJcIlwiXG4gICAgQV90ID0gYXR0ZW50aW9uX2hlYXRtYXAodGVhY2hlcl9mZWF0KVxuICAgIEFfcyA9IGF0dGVudGlvbl9oZWF0bWFwKHN0dWRlbnRfZmVhdClcblxuICAgIHRfZmxhdCA9IEFfdC5mbGF0dGVuKClcbiAgICBzX2ZsYXQgPSBBX3MuZmxhdHRlbigpXG4gICAgY29zX3NpbSA9IG5wLmRvdCh0X2ZsYXQsIHNfZmxhdCkgLyAoXG4gICAgICAgIG5wLmxpbmFsZy5ub3JtKHRfZmxhdCkgKiBucC5saW5hbGcubm9ybShzX2ZsYXQpICsgMWUtNilcblxuICAgIHByaW50KGZcdTAwMjdUZWFjaGVyIGF0dG4g4oCUIG1lYW46IHtBX3QubWVhbigpOi40Zn0gIHN0ZDoge0FfdC5zdGQoKTouNGZ9ICBtYXg6IHtBX3QubWF4KCk6LjRmfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3U3R1ZGVudCBhdHRuIOKAlCBtZWFuOiB7QV9zLm1lYW4oKTouNGZ9ICBzdGQ6IHtBX3Muc3RkKCk6LjRmfSAgbWF4OiB7QV9zLm1heCgpOi40Zn1cdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN0Nvc2luZSBzaW1pbGFyaXR5ICh0ZWFjaGVyIHZzIHN0dWRlbnQpOiB7Y29zX3NpbTouNGZ9XHUwMDI3KVxuICAgIHByaW50KFx1MDAyN0FmdGVyIEFUIHRyYWluaW5nLCBjb3NpbmUgc2ltaWxhcml0eSBzaG91bGQgYXBwcm9hY2ggMS4wLlx1MDAyNylcblxuXG50b3JjaC5tYW51YWxfc2VlZCgzKVxuQywgSCwgVyA9IDY0LCAxNCwgMTRcbnRlYWNoZXJfZmVhdCA9IHRvcmNoLnJhbmRuKEMsIEgsIFcpLmFicygpICAjIHBvc3QtUmVMVSwgbm9uLW5lZ2F0aXZlXG5zdHVkZW50X2ZlYXQgPSB0b3JjaC5yYW5kbihDLCBILCBXKS5hYnMoKVxuY29tcGFyZV9hdHRlbnRpb25fbWFwcyh0ZWFjaGVyX2ZlYXQsIHN0dWRlbnRfZmVhdCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBVCArIExvZ2l0IEtEIENvbWJpbmVkIFRyYWluaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBVCBhbG9uZSB3aXRob3V0IGxvZ2l0IEtEIGxlYXZlcyBhY2N1cmFjeSBvbiB0aGUgdGFibGUuIFRoZSBiZXN0IHJlc3VsdHMgY29tZSBmcm9tIGNvbWJpbmluZyBib3RoOiB0aGUgbG9naXQgS0QgdGVybSB0cmFuc2ZlcnMgY2xhc3MtbGV2ZWwgZGFyayBrbm93bGVkZ2Ugd2hpbGUgdGhlIEFUIHRlcm0gYWxpZ25zIHNwYXRpYWwgYXR0ZW50aW9uIGF0IGV2ZXJ5IHN0YWdlLiBUaGUgY29tYmluZWQgbG9zcyBpcyBMID0gzrHCt0NFKGhhcmQpICsgKDEtzrEpwrdUwrLCt0tMKHNvZnQpICsgTF9BVC4gVHlwaWNhbCB3ZWlnaHRzOiDOsT0wLjMsIM6yPTEwMDAuIFRoZSBBVCB0ZXJtIGlzIHVzdWFsbHkgdW53ZWlnaHRlZCByZWxhdGl2ZSB0byB0aGUgS0QgdGVybTsgaXRzIG5hdHVyYWwgc2NhbGUgbWF0Y2hlcyB0aGUgS0QgbG9zcyB3aXRob3V0IGV4cGxpY2l0IHR1bmluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCB0b3JjaC5vcHRpbSBhcyBvcHRpbVxuXG5kZWYgYXRfbWFwKGZlYXR1cmUpOlxuICAgIEIgPSBmZWF0dXJlLnNoYXBlWzBdXG4gICAgcmV0dXJuIEYubm9ybWFsaXplKGZlYXR1cmUucG93KDIpLnN1bSgxKS52aWV3KEIsIC0xKSwgcD0yLCBkaW09MSlcblxuZGVmIGNvbWJpbmVkX2F0X2tkX2xvc3Moc19sb2dpdHMsIHRfbG9naXRzLCBzX2ZlYXRzLCB0X2ZlYXRzLCBsYWJlbHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgVD00LjAsIGFscGhhPTAuMywgYmV0YT0xMDAwLjApOlxuICAgIFwiXCJcIkNFICsgbG9naXQgS0QgKyBtdWx0aS1zdGFnZSBBVC5cIlwiXCJcbiAgICBoYXJkID0gRi5jcm9zc19lbnRyb3B5KHNfbG9naXRzLCBsYWJlbHMpXG4gICAga2QgICA9IEYua2xfZGl2KEYubG9nX3NvZnRtYXgoc19sb2dpdHMgLyBULCBkaW09LTEpLFxuICAgICAgICAgICAgICAgICAgICBGLnNvZnRtYXgodF9sb2dpdHMgLyBULCBkaW09LTEpLmRldGFjaCgpLFxuICAgICAgICAgICAgICAgICAgICByZWR1Y3Rpb249XHUwMDI3YmF0Y2htZWFuXHUwMDI3KSAqIFQgKiogMlxuICAgIGF0ICAgPSBzdW0oKGJldGEgLyAyLjApICogKGF0X21hcChmcykgLSBhdF9tYXAoZnQpLmRldGFjaCgpKS5wb3coMikubWVhbigpXG4gICAgICAgICAgICAgICBmb3IgZnMsIGZ0IGluIHppcChzX2ZlYXRzLCB0X2ZlYXRzKSlcbiAgICByZXR1cm4gYWxwaGEgKiBoYXJkICsgKDEgLSBhbHBoYSkgKiBrZCArIGF0LCBoYXJkLml0ZW0oKSwga2QuaXRlbSgpLCBhdC5pdGVtKClcblxuZGVmIHRyYWluX2F0X2tkKHN0dWRlbnQsIHRlYWNoZXIsIGxvYWRlciwgZGV2aWNlLCBlcG9jaHM9Myk6XG4gICAgdGVhY2hlci5ldmFsKClcbiAgICBmb3IgcCBpbiB0ZWFjaGVyLnBhcmFtZXRlcnMoKTogcC5yZXF1aXJlc19ncmFkXyhGYWxzZSlcbiAgICBvcHRpbWl6ZXIgPSBvcHRpbS5TR0Qoc3R1ZGVudC5wYXJhbWV0ZXJzKCksIGxyPTAuMDEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgIG1vbWVudHVtPTAuOSwgd2VpZ2h0X2RlY2F5PTFlLTQpXG4gICAgZm9yIGVwb2NoIGluIHJhbmdlKGVwb2Nocyk6XG4gICAgICAgIHN0dWRlbnQudHJhaW4oKVxuICAgICAgICB0b3RhbCA9IDAuMFxuICAgICAgICBmb3IgWCwgeSBpbiBsb2FkZXI6XG4gICAgICAgICAgICBYLCB5ID0gWC50byhkZXZpY2UpLCB5LnRvKGRldmljZSlcbiAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICAgICAgICAgIHRfbG9naXRzLCB0X2ZlYXRzID0gdGVhY2hlcihYLCByZXR1cm5fZmVhdHM9VHJ1ZSlcbiAgICAgICAgICAgIHNfbG9naXRzLCBzX2ZlYXRzID0gc3R1ZGVudChYLCByZXR1cm5fZmVhdHM9VHJ1ZSlcbiAgICAgICAgICAgIGxvc3MsIGgsIGssIGEgPSBjb21iaW5lZF9hdF9rZF9sb3NzKHNfbG9naXRzLCB0X2xvZ2l0cyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc19mZWF0cywgdF9mZWF0cywgeSlcbiAgICAgICAgICAgIG9wdGltaXplci56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgICAgICAgICB0b3RhbCArPSBsb3NzLml0ZW0oKVxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2Vwb2NoKzF9OiB0b3RhbD17dG90YWwvbGVuKGxvYWRlcik6LjRmfSAgaD17aDouM2Z9ICBrZD17azouM2Z9ICBhdD17YTouM2Z9XHUwMDI3KVxuXG5wcmludChcdTAwMjdBVCtLRDogc3R1ZGVudCBmb3J3YXJkIG11c3QgcmV0dXJuIChsb2dpdHMsIFtmZWF0X3N0YWdlMSwgZmVhdF9zdGFnZTIsIGZlYXRfc3RhZ2UzXSkuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlbUNLRCBhbmQgQ3Jvc3MtTGF5ZXIgQXR0ZW50aW9uIFRyYW5zZmVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZW1hbnRpYyBDYWxpYnJhdGlvbiBmb3IgS25vd2xlZGdlIERpc3RpbGxhdGlvbiAoU2VtQ0tELCBDaGVuIGV0IGFsLiAyMDIxKSBleHRlbmRzIEFUIHRvIGNyb3NzLWxheWVyIGF0dGVudGlvbjogaW5zdGVhZCBvZiBtYXRjaGluZyBlYWNoIHN0dWRlbnQgbGF5ZXIgdG8gb25lIHRlYWNoZXIgbGF5ZXIsIGl0IGNvbXB1dGVzIGFuIGF0dGVudGlvbiBtYXRyaXggQSDiiIgg4oSdXntOX3Mgw5cgTl90fSB0aGF0IGFzc2lnbnMgZWFjaCBzdHVkZW50IGxheWVyIHRvIGEgd2VpZ2h0ZWQgY29tYmluYXRpb24gb2YgdGVhY2hlciBsYXllcnMuIFRoZSB3ZWlnaHRzIGFyZSBsZWFybmVkIGR1cmluZyB0cmFpbmluZywgYWxsb3dpbmcgdGhlIHN0dWRlbnQgdG8gYWxpZ24gd2l0aCB3aGljaGV2ZXIgdGVhY2hlciBsYXllciBpcyBtb3N0IGluZm9ybWF0aXZlIGZvciBlYWNoIHN0dWRlbnQgbGF5ZXIuIFRoaXMgYXZvaWRzIHRoZSBoYW5kLXR1bmVkIGxheWVyIHBhaXJpbmcgcmVxdWlyZWQgYnkgRml0TmV0cyBhbmQgQVQuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IldoZW4gdG8gVXNlIEFUIHZzIEZpdE5ldHMgdnMgQ1JEIiwiY29udGVudCI6IlVzZSBBVCB3aGVuIHlvdSB3YW50IGEgc2ltcGxlLCBsb3ctb3ZlcmhlYWQgZmVhdHVyZSBkaXN0aWxsYXRpb24gd2l0aCBubyBleHRyYSBwYXJhbWV0ZXJzIChubyBhZGFwdGVyLCBubyBtZW1vcnkgYmFuaykuIFVzZSBGaXROZXRzIHdoZW4gdGhlIHN0dWRlbnQgaXMgbXVjaCBzaGFsbG93ZXIgYW5kIG5lZWRzIGd1aWRlZCBpbnRlcm1lZGlhdGUgcmVwcmVzZW50YXRpb25zIHRvIGZpbmQgYSBnb29kIG9wdGltaXphdGlvbiBwYXRoLiBVc2UgQ1JEIHdoZW4geW91IGNhbiBhZmZvcmQgdGhlIG1lbW9yeSBiYW5rIGFuZCB3YW50IHRoZSBzdHJvbmdlc3Qgc2luZ2xlLW1ldGhvZCBiZW5jaG1hcmsgcGVyZm9ybWFuY2UuIEZvciBwcm9kdWN0aW9uLCBBVCArIGxvZ2l0IEtEIGNvbWJpbmVkIGlzIG9mdGVuIHRoZSBiZXN0IGVmZm9ydC10by1nYWluIHRyYWRlLW9mZi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgUmVjb21tZW5kYXRpb25zIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJBcHBseSBBVCBhdCBhbGwgZG93bnNhbXBsaW5nIGJvdW5kYXJpZXMgKGFmdGVyIGVhY2ggUmVzTmV0IHN0YWdlKSDigJQgMyBvciA0IGxvc3MgdGVybXMgdG90YWwuIiwizrI9MTAwMCBpcyByb2J1c3QgYWNyb3NzIGRhdGFzZXRzOyByZWR1Y2UgdG8gMTAwIGlmIHRoZSBBVCBsb3NzIGRvbWluYXRlcyB0aGUgbG9naXQgS0QgdGVybSBpbiBlYXJseSB0cmFpbmluZy4iLCJDb21iaW5lIEFUIHdpdGggbG9naXQgS0QgKFQ9NCwgzrE9MC4zKTogcHVyZSBBVCB3aXRob3V0IGxvZ2l0IEtEIGNvbnNpc3RlbnRseSB1bmRlcnBlcmZvcm1zIHRoZSBjb21iaW5lZCBsb3NzLiIsIkdyYWRpZW50LUFUIChKYWNvYmlhbiBtYXBzKSBnaXZlcyBoaWdoZXIgY29zaW5lIHNpbWlsYXJpdHkgYnV0IHJlcXVpcmVzIGFuIGV4dHJhIGJhY2t3YXJkIHBhc3MgcGVyIGxheWVyIOKAlCB1c2Ugb25seSBhdCAx4oCTMiBrZXkgbGF5ZXJzLiIsIlNlbUNLRCBpcyB0aGUgc3Ryb25nZXN0IHZhcmlhbnQgYnV0IGFkZHMgbGVhcm5lZCBjcm9zcy1sYXllciBhdHRlbnRpb24gcGFyYW1ldGVyczsgcmVzZXJ2ZSBmb3IgYmVuY2htYXJrLWNyaXRpY2FsIHVzZSBjYXNlcy4iLCJTcGF0aWFsIHNpemUgbWlzbWF0Y2g6IGJpbGluZWFyLWludGVycG9sYXRlIHRoZSB0ZWFjaGVyXHUwMDI3cyBhdHRlbnRpb24gbWFwIHRvIG1hdGNoIHRoZSBzdHVkZW50XHUwMDI3cyAoSMOXVykgYmVmb3JlIGNvbXB1dGluZyB0aGUgbG9zcy4iLCJNb25pdG9yIGNvc2luZSBzaW1pbGFyaXR5IGJldHdlZW4gdGVhY2hlciBhbmQgc3R1ZGVudCBhdHRlbnRpb24gbWFwcyBkdXJpbmcgdHJhaW5pbmcgYXMgYSBkaWFnbm9zdGljIOKAlCBzdGFsbGVkIHNpbWlsYXJpdHkgaW5kaWNhdGVzIHRvby1zbWFsbCDOsiBvciBiYWQgbGF5ZXIgcGFpcmluZy4iXX0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIldoYXQgSXMgTWF0Y2hlZCIsIlNwYXRpYWwgSW5mbyIsIkdyYWRpZW50IENvc3QiLCJBY2N1cmFjeSBHYWluIiwiTGF5ZXJzIFVzZWQiXSwicm93cyI6W1siRmVhdHVyZSBLRCAoRml0TmV0cykiLCJSYXcgZmVhdHVyZSBtYXBzIChMMiBNU0UpIiwiWWVzIChIw5dXKSIsIkxvdyIsIisyLjXigJM0LjAlIiwiT25lIGhpbnQgbGF5ZXIiXSxbIkFUIChaYWdvcnV5a28gMjAxNykiLCJTdW0tc3F1YXJlZCBhdHRlbnRpb24gbWFwcyIsIlllcyAoSMOXVykiLCJMb3ciLCIrMi4w4oCTMy41JSIsIk11bHRpcGxlIHN0YWdlcyJdLFsiR3JhZGllbnQtQVQgKEphY29iaWFuKSIsIkphY29iaWFuIG9mIG91dHB1dCB3LnIudC4gZmVhdHVyZXMiLCJZZXMgKEjDl1cpIiwiSGlnaCDigJQgZXh0cmEgYmFja3dhcmQgcGVyIGxheWVyIiwiKzMuMOKAkzQuNSUiLCIx4oCTMiBrZXkgbGF5ZXJzIl0sWyJTZW1DS0QgKENoZW4gMjAyMSkiLCJDcm9zcy1sYXllciBhdHRlbnRpb24gbWF0cml4IChOw5dOKSIsIkNyb3NzLWxheWVyIiwiTWVkaXVtIOKAlCBsZWFybmVkIGF0dGVudGlvbiB3ZWlnaHRzIiwiKzMuNeKAkzUuMCUiLCJBbGwgbGF5ZXIgcGFpcnMiXSxbIkdyYWRDQU0tQVQiLCJDbGFzcyBhY3RpdmF0aW9uIHNhbGllbmN5IG1hcHMiLCJZZXMgKEjDl1cpIiwiSGlnaCDigJQgY2xhc3Mtc3BlY2lmaWMgYmFja3dhcmQgcGFzcyIsIisyLjXigJM0LjAlIiwiTXVsdGlwbGUgc3RhZ2VzIl1dfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Attention Transfer — Spatial Attention Map Distillation

Attention Transfer (Zagoruyko & Komodakis 2017) distills not what the teacher knows but where it looks. A well-trained teacher has learned to focus on discriminative regions — the animal's face rather than the background, the wheel arch rather than the car door. The student should look at those same regions. AT computes a spatial attention map from each intermediate feature tensor and penalizes the student for looking at different regions than the teacher.

## Attention Map Computation: Sum, Max, and L2

Given a feature tensor F ∈ ℝ^{C×H×W}, three attention map variants are commonly used. Sum-squared (default AT): A_sum = Σ_c F_k² — sum of squared activations over channels, producing a (H×W) heatmap. Max absolute: A_max = max_c |F_k| — maximum absolute activation over channels. L2 norm: A_l2 = ‖F_k‖_2 over channels. All maps are normalized by their Frobenius norm: Ā = A / ‖A‖_F. The sum-squared variant is the standard choice and performs best in practice.

```python
import torch
import torch.nn.functional as F

def compute_attention_maps(feature: torch.Tensor):
    """
    Compute three attention map variants from F in R^{B x C x H x W}.
    All maps normalized to unit L2 norm per sample.
    Returns: (A_sum, A_max, A_l2) each of shape (B, H*W).
    """
    B, C, H, W = feature.shape

    A_sum = feature.pow(2).sum(dim=1).view(B, -1)       # (B, H*W)
    A_max = feature.abs().max(dim=1).values.view(B, -1)  # (B, H*W)
    A_l2  = feature.norm(p=2, dim=1).view(B, -1)         # (B, H*W)

    normalize = lambda A: F.normalize(A, p=2, dim=1)
    return normalize(A_sum), normalize(A_max), normalize(A_l2)


torch.manual_seed(7)
B, C, H, W = 4, 128, 8, 8
feature = torch.randn(B, C, H, W)

A_sum, A_max, A_l2 = compute_attention_maps(feature)
print(f'Feature shape:   {feature.shape}')
print(f'Attention shapes: sum={A_sum.shape}  max={A_max.shape}  l2={A_l2.shape}')

# Cross-variant correlation (should be high — all capture similar spatial structure)
corr_sm = (A_sum * A_max).sum(1).mean().item()
corr_sl = (A_sum * A_l2).sum(1).mean().item()
print(f'Correlation sum-max: {corr_sm:.4f}   sum-l2: {corr_sl:.4f}')
print('Sum-of-squares is standard (Zagoruyko & Komodakis 2017).')
```

## AT Loss at Multiple Intermediate Layers

Applying AT at a single layer provides limited supervision. The full AT method applies the loss after each major stage (e.g., after each residual block group in ResNet). This means the student is guided to look in the right places at every level of abstraction — low-level texture regions in early stages, semantic object regions in later stages. The total AT loss is the sum across all paired stages, each weighted by the same β.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def at_map(feature: torch.Tensor) -> torch.Tensor:
    """Sum-of-squared channels attention map, L2-normalized. Shape: (B, H*W)."""
    B = feature.shape[0]
    A = feature.pow(2).sum(dim=1).view(B, -1)
    return F.normalize(A, p=2, dim=1)

class MultiStageATLoss(nn.Module):
    """AT loss summed over multiple paired feature map stages."""

    def __init__(self, beta: float = 1000.0):
        super().__init__()
        self.beta = beta

    def forward(self, student_feats: list, teacher_feats: list) -> torch.Tensor:
        assert len(student_feats) == len(teacher_feats)
        device = student_feats[0].device
        total = torch.zeros(1, device=device)
        for fs, ft in zip(student_feats, teacher_feats):
            A_s = at_map(fs)
            A_t = at_map(ft).detach()
            if A_s.shape != A_t.shape:  # resample if spatial sizes differ
                A_t = F.interpolate(A_t.unsqueeze(1),
                                    size=A_s.shape[-1], mode='linear').squeeze(1)
            total = total + (self.beta / 2.0) * (A_s - A_t).pow(2).mean()
        return total


# Demo: 3-stage ResNet-style feature maps (teacher wider than student)
B = 4
student_feats = [torch.randn(B,  64, 28, 28),
                 torch.randn(B, 128, 14, 14),
                 torch.randn(B, 256,  7,  7)]
teacher_feats = [torch.randn(B, 128, 28, 28),
                 torch.randn(B, 256, 14, 14),
                 torch.randn(B, 512,  7,  7)]

at_loss = MultiStageATLoss(beta=1000.0)
loss = at_loss(student_feats, teacher_feats)
print(f'Multi-stage AT loss (3 stages): {loss.item():.4f}')
```

## Gradient-Based Attention Maps

An alternative to activation-based maps is gradient-based attention: the Jacobian of the model's output with respect to an intermediate feature tensor. ∂y/∂F_k captures how sensitive the final prediction is to each spatial location in layer k — a more informative signal than raw activation magnitudes. GradCAM-style attention combines gradients and activations: A_GradCAM = ReLU(Σ_c (∂y/∂F_c) · F_c). The cost is one additional backward pass per layer; impractical for all layers but effective at a single carefully chosen layer.

## Visualizing Teacher vs Student Attention

Before and after AT training, comparing the teacher's and student's attention maps reveals whether the student has learned to look at the right image regions. High cosine similarity between the flattened, normalized maps indicates successful attention transfer. In practice, a student trained with AT shows much higher cosine similarity to the teacher's maps than a student trained with logit KD alone, which explains the accuracy improvement — the student literally focuses on the correct discriminative regions.

```python
import torch
import torch.nn.functional as F
import numpy as np

def attention_heatmap(feature: torch.Tensor) -> np.ndarray:
    """Convert a single-sample feature (C, H, W) to a normalized (H, W) heatmap."""
    A = feature.pow(2).sum(dim=0).detach().cpu().numpy()  # (H, W)
    return (A - A.min()) / (A.max() - A.min() + 1e-6)

def compare_attention_maps(teacher_feat: torch.Tensor, student_feat: torch.Tensor):
    """Print statistics comparing teacher and student spatial attention."""
    A_t = attention_heatmap(teacher_feat)
    A_s = attention_heatmap(student_feat)

    t_flat = A_t.flatten()
    s_flat = A_s.flatten()
    cos_sim = np.dot(t_flat, s_flat) / (
        np.linalg.norm(t_flat) * np.linalg.norm(s_flat) + 1e-6)

    print(f'Teacher attn — mean: {A_t.mean():.4f}  std: {A_t.std():.4f}  max: {A_t.max():.4f}')
    print(f'Student attn — mean: {A_s.mean():.4f}  std: {A_s.std():.4f}  max: {A_s.max():.4f}')
    print(f'Cosine similarity (teacher vs student): {cos_sim:.4f}')
    print('After AT training, cosine similarity should approach 1.0.')


torch.manual_seed(3)
C, H, W = 64, 14, 14
teacher_feat = torch.randn(C, H, W).abs()  # post-ReLU, non-negative
student_feat = torch.randn(C, H, W).abs()
compare_attention_maps(teacher_feat, student_feat)
```

## AT + Logit KD Combined Training

AT alone without logit KD leaves accuracy on the table. The best results come from combining both: the logit KD term transfers class-level dark knowledge while the AT term aligns spatial attention at every stage. The combined loss is L = α·CE(hard) + (1-α)·T²·KL(soft) + L_AT. Typical weights: α=0.3, β=1000. The AT term is usually unweighted relative to the KD term; its natural scale matches the KD loss without explicit tuning.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

def at_map(feature):
    B = feature.shape[0]
    return F.normalize(feature.pow(2).sum(1).view(B, -1), p=2, dim=1)

def combined_at_kd_loss(s_logits, t_logits, s_feats, t_feats, labels,
                         T=4.0, alpha=0.3, beta=1000.0):
    """CE + logit KD + multi-stage AT."""
    hard = F.cross_entropy(s_logits, labels)
    kd   = F.kl_div(F.log_softmax(s_logits / T, dim=-1),
                    F.softmax(t_logits / T, dim=-1).detach(),
                    reduction='batchmean') * T ** 2
    at   = sum((beta / 2.0) * (at_map(fs) - at_map(ft).detach()).pow(2).mean()
               for fs, ft in zip(s_feats, t_feats))
    return alpha * hard + (1 - alpha) * kd + at, hard.item(), kd.item(), at.item()

def train_at_kd(student, teacher, loader, device, epochs=3):
    teacher.eval()
    for p in teacher.parameters(): p.requires_grad_(False)
    optimizer = optim.SGD(student.parameters(), lr=0.01,
                          momentum=0.9, weight_decay=1e-4)
    for epoch in range(epochs):
        student.train()
        total = 0.0
        for X, y in loader:
            X, y = X.to(device), y.to(device)
            with torch.no_grad():
                t_logits, t_feats = teacher(X, return_feats=True)
            s_logits, s_feats = student(X, return_feats=True)
            loss, h, k, a = combined_at_kd_loss(s_logits, t_logits,
                                                  s_feats, t_feats, y)
            optimizer.zero_grad(); loss.backward(); optimizer.step()
            total += loss.item()
        print(f'Epoch {epoch+1}: total={total/len(loader):.4f}  h={h:.3f}  kd={k:.3f}  at={a:.3f}')

print('AT+KD: student forward must return (logits, [feat_stage1, feat_stage2, feat_stage3]).')
```

## SemCKD and Cross-Layer Attention Transfer

Semantic Calibration for Knowledge Distillation (SemCKD, Chen et al. 2021) extends AT to cross-layer attention: instead of matching each student layer to one teacher layer, it computes an attention matrix A ∈ ℝ^{N_s × N_t} that assigns each student layer to a weighted combination of teacher layers. The weights are learned during training, allowing the student to align with whichever teacher layer is most informative for each student layer. This avoids the hand-tuned layer pairing required by FitNets and AT.

> **When to Use AT vs FitNets vs CRD**: Use AT when you want a simple, low-overhead feature distillation with no extra parameters (no adapter, no memory bank). Use FitNets when the student is much shallower and needs guided intermediate representations to find a good optimization path. Use CRD when you can afford the memory bank and want the strongest single-method benchmark performance. For production, AT + logit KD combined is often the best effort-to-gain trade-off.

## Practical Recommendations

- Apply AT at all downsampling boundaries (after each ResNet stage) — 3 or 4 loss terms total.
- β=1000 is robust across datasets; reduce to 100 if the AT loss dominates the logit KD term in early training.
- Combine AT with logit KD (T=4, α=0.3): pure AT without logit KD consistently underperforms the combined loss.
- Gradient-AT (Jacobian maps) gives higher cosine similarity but requires an extra backward pass per layer — use only at 1–2 key layers.
- SemCKD is the strongest variant but adds learned cross-layer attention parameters; reserve for benchmark-critical use cases.
- Spatial size mismatch: bilinear-interpolate the teacher's attention map to match the student's (H×W) before computing the loss.
- Monitor cosine similarity between teacher and student attention maps during training as a diagnostic — stalled similarity indicates too-small β or bad layer pairing.

| Method | What Is Matched | Spatial Info | Gradient Cost | Accuracy Gain | Layers Used |
| --- | --- | --- | --- | --- | --- |
| Feature KD (FitNets) | Raw feature maps (L2 MSE) | Yes (H×W) | Low | +2.5–4.0% | One hint layer |
| AT (Zagoruyko 2017) | Sum-squared attention maps | Yes (H×W) | Low | +2.0–3.5% | Multiple stages |
| Gradient-AT (Jacobian) | Jacobian of output w.r.t. features | Yes (H×W) | High — extra backward per layer | +3.0–4.5% | 1–2 key layers |
| SemCKD (Chen 2021) | Cross-layer attention matrix (N×N) | Cross-layer | Medium — learned attention weights | +3.5–5.0% | All layer pairs |
| GradCAM-AT | Class activation saliency maps | Yes (H×W) | High — class-specific backward pass | +2.5–4.0% | Multiple stages |

---

