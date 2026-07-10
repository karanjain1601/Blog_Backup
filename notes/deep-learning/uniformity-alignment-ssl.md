---
title: "Uniformity and Alignment — Geometric Theory of Contrastive Learning"
slug: "uniformity-alignment-ssl"
description: "Wang and Isola (2020) decompose contrastive learning objectives into two geometric properties on the unit hypersphere: alignment (positive pairs attract) and uniformity (features spread evenly), providing a principled diagnostic framework for understanding and detecting representational collapse."
tags: ["deep-learning", "self-supervised-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2FuZyBhbmQgSXNvbGEgKDIwMjApIG9mZmVyZWQgb25lIG9mIHRoZSBjbGVhcmVzdCB0aGVvcmV0aWNhbCBmcmFtZXdvcmtzIGZvciB1bmRlcnN0YW5kaW5nIHdoeSBjb250cmFzdGl2ZSBsZWFybmluZyB3b3Jrcy4gVGhleSBzaG93ZWQgdGhhdCBjb250cmFzdGl2ZSBsb3NzIG9uIHRoZSB1bml0IGh5cGVyc3BoZXJlIGNhbiBiZSBkZWNvbXBvc2VkIGludG8gdHdvIGNvbXBldGluZyBnZW9tZXRyaWMgcHJvcGVydGllczogYWxpZ25tZW50IChwb3NpdGl2ZSBwYWlycyBzaG91bGQgYmUgY2xvc2UgdG9nZXRoZXIpIGFuZCB1bmlmb3JtaXR5IChhbGwgZmVhdHVyZXMgc2hvdWxkIGJlIHNwcmVhZCBhcyB1bmlmb3JtbHkgYXMgcG9zc2libGUgYWNyb3NzIHRoZSBzcGhlcmUpLiBUaGVzZSB0d28gcHJvcGVydGllcyBhcmUgbm90IGFyYml0cmFyeSDigJQgdGhleSBjb3JyZXNwb25kIHRvIGFuIGlkZWFsIHJlcHJlc2VudGF0aW9uIHRoYXQgaXMgbWF4aW1hbGx5IGluZm9ybWF0aXZlOiBwb3NpdGl2ZSBwYWlycyBhZ3JlZSAoYWxpZ25tZW50KSBhbmQgdGhlIGVudGlyZSBmZWF0dXJlIHNwYWNlIGlzIHVzZWQgd2l0aG91dCBjb2xsYXBzZSAodW5pZm9ybWl0eSkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWxpZ25tZW50IOKAlCBBdHRyYWN0aW5nIFBvc2l0aXZlIFBhaXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGlnbm1lbnQgbWVhc3VyZXMgaG93IHdlbGwgdGhlIGVuY29kZXIgbWFwcyBzZW1hbnRpY2FsbHkgc2ltaWxhciBpbnB1dHMgdG8gbmVhcmJ5IHJlcHJlc2VudGF0aW9ucy4gRm9yIGEgZGlzdHJpYnV0aW9uIG9mIHBvc2l0aXZlIHBhaXJzICh4LCB4XHUwMDI3KSBkcmF3biBmcm9tIHRoZSBzYW1lIGltYWdlIHdpdGggZGlmZmVyZW50IGF1Z21lbnRhdGlvbnMsIHRoZSBhbGlnbm1lbnQgbG9zcyBpcyB0aGUgZXhwZWN0ZWQgc3F1YXJlZCBFdWNsaWRlYW4gZGlzdGFuY2UgYmV0d2VlbiB0aGVpciBMMi1ub3JtYWxpc2VkIHJlcHJlc2VudGF0aW9uczogTF9hbGlnbiA9IEVfeyh4LHhcdTAwMjcpfnBfcG9zfVvigJZmKHgpIOKIkiBmKHhcdTAwMjcp4oCWwrJdLiBGb3IgdW5pdC1ub3JtIHZlY3RvcnMsIHRoaXMgZXF1YWxzIDIoMSDiiJIgY29zaW5lX3NpbWlsYXJpdHkoZih4KSwgZih4XHUwMDI3KSkpLiBQZXJmZWN0IGFsaWdubWVudCAoTF9hbGlnbiA9IDApIG1lYW5zIHRoZSBlbmNvZGVyIGlzIGludmFyaWFudCB0byBhdWdtZW50YXRpb24g4oCUIGJvdGggdmlld3MgbWFwIHRvIHRoZSBleGFjdCBzYW1lIHBvaW50LiBUaGlzIGlzIHRoZSBzaW1wbGVzdCBmb3JtIG9mIHJlcHJlc2VudGF0aW9uIGxlYXJuaW5nOiBpbnZhcmlhbmNlIHRvIG51aXNhbmNlIHZhcmlhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cblxuZGVmIGFsaWdubWVudF9sb3NzKHoxOiB0b3JjaC5UZW5zb3IsIHoyOiB0b3JjaC5UZW5zb3IsIGFscGhhOiBmbG9hdCA9IDIuMCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiQWxpZ25tZW50IGxvc3M6IGV4cGVjdGVkIHx8Zih4KSAtIGYoeFx1MDAyNyl8fF5hbHBoYSBmb3IgcG9zaXRpdmUgcGFpcnMuXG4gICAgejEsIHoyOiAoTiwgRCkgTDItbm9ybWFsaXNlZCBlbWJlZGRpbmdzIG9mIHR3byBhdWdtZW50ZWQgdmlld3MuXG4gICAgYWxwaGE9MiBnaXZlcyBzcXVhcmVkIEV1Y2xpZGVhbiBkaXN0YW5jZSBvbiB1bml0IHNwaGVyZS5cbiAgICBcIlwiXCJcbiAgICB6MSA9IEYubm9ybWFsaXplKHoxLCBkaW09MSkgICMgZW5zdXJlIHVuaXQgbm9ybVxuICAgIHoyID0gRi5ub3JtYWxpemUoejIsIGRpbT0xKVxuICAgIHJldHVybiAoejEgLSB6Mikubm9ybShkaW09MSkucG93KGFscGhhKS5tZWFuKClcblxuXG5kZWYgYWxpZ25tZW50X3ZpYV9jb3NpbmUoejE6IHRvcmNoLlRlbnNvciwgejI6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiRXF1aXZhbGVudDogTF9hbGlnbiA9IDIgKiAoMSAtIG1lYW4gY29zaW5lIHNpbWlsYXJpdHkpLlwiXCJcIlxuICAgIHoxID0gRi5ub3JtYWxpemUoejEsIGRpbT0xKVxuICAgIHoyID0gRi5ub3JtYWxpemUoejIsIGRpbT0xKVxuICAgIGNvc19zaW0gPSAoejEgKiB6Mikuc3VtKGRpbT0xKSAgICMgKE4sKSBjb3NpbmUgc2ltaWxhcml0eSBwZXIgcGFpclxuICAgIHJldHVybiAyICogKDEgLSBjb3Nfc2ltLm1lYW4oKSlcblxuXG4jIERlbW86IHBlcmZlY3QgYWxpZ25tZW50LCByYW5kb20gYWxpZ25tZW50LCBjb2xsYXBzZWQgYWxpZ25tZW50XG50b3JjaC5tYW51YWxfc2VlZCg0MilcbnogPSBGLm5vcm1hbGl6ZSh0b3JjaC5yYW5kbig2NCwgMTI4KSwgZGltPTEpXG5wcmludChcdTAwMjdQZXJmZWN0IGFsaWdubWVudCAoejEgPT0gejIpOiAgXHUwMDI3LCBhbGlnbm1lbnRfbG9zcyh6LCB6KS5pdGVtKCkpICAgICAgICAgICMgMC4wXG5cbnoyX3JhbmQgPSBGLm5vcm1hbGl6ZSh0b3JjaC5yYW5kbig2NCwgMTI4KSwgZGltPTEpXG5wcmludChcdTAwMjdSYW5kb20gYWxpZ25tZW50OiAgICAgICAgICAgICAgIFx1MDAyNywgYWxpZ25tZW50X2xvc3MoeiwgejJfcmFuZCkuaXRlbSgpKSAgICMgfjIuMFxuXG56Ml9ub2lzZSA9IEYubm9ybWFsaXplKHogKyAwLjA1ICogdG9yY2gucmFuZG5fbGlrZSh6KSwgZGltPTEpXG5wcmludChcdTAwMjdOZWFyLXBlcmZlY3QgYWxpZ25tZW50IChub2lzZSk6XHUwMDI3LCBhbGlnbm1lbnRfbG9zcyh6LCB6Ml9ub2lzZSkuaXRlbSgpKSAgICMgc21hbGwifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVbmlmb3JtaXR5IOKAlCBTcHJlYWRpbmcgRmVhdHVyZXMgb24gdGhlIEh5cGVyc3BoZXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVbmlmb3JtaXR5IG1lYXN1cmVzIGhvdyBldmVubHkgdGhlIGVuY29kZXJcdTAwMjdzIG91dHB1dCBkaXN0cmlidXRpb24gY292ZXJzIHRoZSB1bml0IGh5cGVyc3BoZXJlLiBBIGNvbXBsZXRlbHkgdW5pZm9ybSBkaXN0cmlidXRpb24gbWF4aW1pc2VzIGVudHJvcHkg4oCUIGV2ZXJ5IGRpbWVuc2lvbiBpcyB1c2VkIGFuZCBubyBpbmZvcm1hdGlvbiBpcyB3YXN0ZWQuIFRoZSB1bmlmb3JtaXR5IGxvc3MgdXNlcyBhIEdhdXNzaWFuIGtlcm5lbCB0byBtZWFzdXJlIHRoZSBhdmVyYWdlIHBhaXJ3aXNlIHNpbWlsYXJpdHk6IExfdW5pZm9ybSA9IGxvZyBFX3t4LHl+cF9kYXRhfVtlXnstMuKAlmYoeCniiJJmKHkp4oCWwrJ9XS4gVGhlIEdhdXNzaWFuIGtlcm5lbCBlXnstMuKAlnXiiJJ24oCWwrJ9IGRlY2F5cyBmcm9tIDEgKHdoZW4gdSA9IHYpIHRvIDAgKHdoZW4gdSBhbmQgdiBhcmUgb3J0aG9nb25hbCkuIFRoZSBsb2cgZW5zdXJlcyB0aGUgc2NhbGUgaXMgYWRkaXRpdmUuIE1pbmltaXNpbmcgTF91bmlmb3JtIHB1c2hlcyBmZWF0dXJlcyBhcGFydCDigJQgdGhlIG9wdGltYWwgc29sdXRpb24gaXMgYSB1bmlmb3JtIGRpc3RyaWJ1dGlvbiBvbiB0aGUgc3BoZXJlIChhIHBlcmZlY3RseSBzcHJlYWQgcGFja2luZykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5cbmRlZiB1bmlmb3JtaXR5X2xvc3MoejogdG9yY2guVGVuc29yLCB0OiBmbG9hdCA9IDIuMCkgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgXCJcIlwiVW5pZm9ybWl0eSBsb3NzOiBsb2ctYXZlcmFnZSBvZiBHYXVzc2lhbiBrZXJuZWwgb3ZlciBhbGwgcGFpcnMuXG4gICAgejogKE4sIEQpIEwyLW5vcm1hbGlzZWQgZW1iZWRkaW5ncy5cbiAgICB0OiBHYXVzc2lhbiBrZXJuZWwgYmFuZHdpZHRoIChkZWZhdWx0IDIgZ2l2ZXMgZV57LTJ8fHUtdnx8XjJ9KS5cbiAgICBcIlwiXCJcbiAgICB6ID0gRi5ub3JtYWxpemUoeiwgZGltPTEpICAgICAgICAgICAgICAgICAgICAgICAgIyAoTiwgRClcbiAgICAjIFBhaXJ3aXNlIHNxdWFyZWQgZGlzdGFuY2VzOiB8fHUtdnx8XjIgPSAyIC0gMip1LnYgZm9yIHVuaXQgdmVjdG9yc1xuICAgIHNxX2Rpc3RzID0gMiAtIDIgKiAoeiBAIHouVCkgICAgICAgICAgICAgICAgICAgICMgKE4sIE4pXG4gICAgIyBHYXVzc2lhbiBrZXJuZWw7IGluY2x1ZGUgYWxsIHBhaXJzIChkaWFnb25hbCA9IHNlbGYsIGNvbnRyaWJ1dGVzIDEpXG4gICAga2VybmVsICAgPSB0b3JjaC5leHAoLXQgKiBzcV9kaXN0cykgICAgICAgICAgICAgICMgKE4sIE4pXG4gICAgIyBMb2cgYXZlcmFnZSBvdmVyIGFsbCBOXjIgcGFpcnNcbiAgICByZXR1cm4ga2VybmVsLm1lYW4oKS5sb2coKVxuXG5cbiMgRGVtbzogY29sbGFwc2VkIChhbGwgc2FtZSkgdnMgdW5pZm9ybSAocmFuZG9tIHVuaXQgdmVjdG9ycylcbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5OLCBEID0gMjU2LCAxMjhcblxuIyBDb2xsYXBzZWQ6IGFsbCBlbWJlZGRpbmdzIGlkZW50aWNhbFxuel9jb2xsYXBzZWQgPSBGLm5vcm1hbGl6ZSh0b3JjaC5vbmVzKE4sIEQpLCBkaW09MSlcbnByaW50KFx1MDAyN1VuaWZvcm1pdHkgKGNvbGxhcHNlZCk6XHUwMDI3LCB1bmlmb3JtaXR5X2xvc3Moel9jb2xsYXBzZWQpLml0ZW0oKSkgICAjIG5lYXIgMCAoYmFkKVxuXG4jIFJhbmRvbSB1bml0IHZlY3RvcnMgYXBwcm94aW1hdGUgdW5pZm9ybSBkaXN0cmlidXRpb25cbnpfdW5pZm9ybSA9IEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKE4sIEQpLCBkaW09MSlcbnByaW50KFx1MDAyN1VuaWZvcm1pdHkgKHJhbmRvbSk6ICAgXHUwMDI3LCB1bmlmb3JtaXR5X2xvc3Moel91bmlmb3JtKS5pdGVtKCkpICAgICAjIHZlcnkgbmVnYXRpdmUgKGdvb2QpXG5cbiMgU2xpZ2h0IGNsdXN0ZXIgc3RydWN0dXJlXG56X21peGVkID0gRi5ub3JtYWxpemUodG9yY2gucmFuZG4oTiwgRCkgKiAwLjUgKyB0b3JjaC5yYW5kbigxLCBEKSwgZGltPTEpXG5wcmludChcdTAwMjdVbmlmb3JtaXR5IChjbHVzdGVyZWQpOlx1MDAyNywgdW5pZm9ybWl0eV9sb3NzKHpfbWl4ZWQpLml0ZW0oKSkgICAgICAgIyBiZXR3ZWVuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTlQtWGVudCBhcyBBbGlnbm1lbnQgUGx1cyBVbmlmb3JtaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXYW5nIGFuZCBJc29sYSBwcm92ZWQgdGhhdCB0aGUgTlQtWGVudCBsb3NzICh1c2VkIGJ5IFNpbUNMUikgYXN5bXB0b3RpY2FsbHkgZGVjb21wb3NlcyBpbnRvIHRoZSBhbGlnbm1lbnQgYW5kIHVuaWZvcm1pdHkgdGVybXMuIFRoZSBudW1lcmF0b3Igb2YgTlQtWGVudCBtYXhpbWlzZXMgdGhlIHNpbWlsYXJpdHkgb2YgcG9zaXRpdmUgcGFpcnMg4oCUIHRoaXMgaXMgdGhlIGFsaWdubWVudCB0ZXJtLiBUaGUgZGVub21pbmF0b3Igbm9ybWFsaXNlcyBhZ2FpbnN0IGFsbCBwYWlycyBpbmNsdWRpbmcgbmVnYXRpdmVzIOKAlCB0aGlzIGlzIHRoZSB1bmlmb3JtaXR5IHRlcm0gKHB1c2hpbmcgZmVhdHVyZXMgYXBhcnQpLiBBcyBiYXRjaCBzaXplIOKGkiDiiJ4sIE5ULVhlbnQgPSDiiJJhbGlnbm1lbnRfdGVybSArIHVuaWZvcm1pdHlfY29uc3RhbnQuIFRoaXMgZGVjb21wb3NpdGlvbiBzaG93cyB0aGF0IE5ULVhlbnQgaW1wbGljaXRseSBvcHRpbWlzZXMgYm90aCBnZW9tZXRyaWMgcHJvcGVydGllcyBzaW11bHRhbmVvdXNseSwgZXhwbGFpbmluZyB3aHkgaXQgZ2VuZXJhbGlzZXMgYmV5b25kIGl0cyBvcmlnaW5hbCBjb250cmFzdGl2ZSBmcmFtaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuXG5kZWYgbnRfeGVudF9kZWNvbXBvc2VkKHoxOiB0b3JjaC5UZW5zb3IsIHoyOiB0b3JjaC5UZW5zb3IsXG4gICAgICAgICAgICAgICAgICAgICAgIHRlbXBlcmF0dXJlOiBmbG9hdCA9IDAuNSkgLVx1MDAzZSBkaWN0OlxuICAgIFwiXCJcIkNvbXB1dGUgTlQtWGVudCBhbmQgaXRzIGFsaWdubWVudCArIHVuaWZvcm1pdHkgZGVjb21wb3NpdGlvbi5cbiAgICB6MSwgejI6IChOLCBEKSBMMi1ub3JtYWxpc2VkIGVtYmVkZGluZ3MuXG4gICAgUmV0dXJucyBkaWN0IHdpdGggdG90YWwgbG9zcywgYWxpZ25tZW50IGNvbXBvbmVudCwgdW5pZm9ybWl0eSBjb21wb25lbnQuXG4gICAgXCJcIlwiXG4gICAgTiA9IHoxLnNpemUoMClcbiAgICB6MSA9IEYubm9ybWFsaXplKHoxLCBkaW09MSlcbiAgICB6MiA9IEYubm9ybWFsaXplKHoyLCBkaW09MSlcbiAgICB6ICA9IHRvcmNoLmNhdChbejEsIHoyXSwgZGltPTApICAgIyAoMk4sIEQpXG5cbiAgICAjIE5ULVhlbnQgdG90YWwgbG9zc1xuICAgIHNpbV9tYXQgPSAoeiBAIHouVCkgLyB0ZW1wZXJhdHVyZSAgICMgKDJOLCAyTilcbiAgICBtYXNrICAgID0gdG9yY2guZXllKDIqTiwgZHR5cGU9dG9yY2guYm9vbCwgZGV2aWNlPXouZGV2aWNlKVxuICAgIHNpbV9tYXQubWFza2VkX2ZpbGxfKG1hc2ssIGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpKVxuICAgIGxhYmVscyAgPSB0b3JjaC5jYXQoW3RvcmNoLmFyYW5nZShOLCAyKk4pLCB0b3JjaC5hcmFuZ2UoTildKS50byh6LmRldmljZSlcbiAgICBudF94ZW50ID0gRi5jcm9zc19lbnRyb3B5KHNpbV9tYXQsIGxhYmVscylcblxuICAgICMgQWxpZ25tZW50IGNvbXBvbmVudCAobG9nIG51bWVyYXRvciwgbm9ybWFsaXNlZClcbiAgICBwb3Nfc2ltID0gKHoxICogejIpLnN1bShkaW09MSkgLyB0ZW1wZXJhdHVyZSAgICMgKE4sKVxuICAgIGFsaWduICAgPSAtcG9zX3NpbS5tZWFuKClcblxuICAgICMgVW5pZm9ybWl0eSBjb21wb25lbnQgKGxvZyBkZW5vbWluYXRvciwgYXBwcm94aW1hdGlvbilcbiAgICB1bmlmb3JtID0gdW5pZm9ybWl0eV9sb3NzKHosIHQ9Mi4wKVxuXG4gICAgcmV0dXJuIHtcdTAwMjdudF94ZW50XHUwMDI3OiBudF94ZW50Lml0ZW0oKSwgXHUwMDI3YWxpZ25tZW50XHUwMDI3OiBhbGlnbi5pdGVtKCksIFx1MDAyN3VuaWZvcm1pdHlcdTAwMjc6IHVuaWZvcm0uaXRlbSgpfVxuXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDcpXG56MSA9IEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKDEyOCwgNjQpLCBkaW09MSlcbnoyID0gRi5ub3JtYWxpemUodG9yY2gucmFuZG4oMTI4LCA2NCksIGRpbT0xKVxucmVzdWx0ID0gbnRfeGVudF9kZWNvbXBvc2VkKHoxLCB6MilcbmZvciBrLCB2IGluIHJlc3VsdC5pdGVtcygpOlxuICAgIHByaW50KGZcdTAwMjd7azpcdTAwM2UxMn06IHt2Oi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29sbGFwc2UgRGV0ZWN0aW9uIER1cmluZyBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiT25lIG9mIHRoZSBtb3N0IHByYWN0aWNhbCBhcHBsaWNhdGlvbnMgb2YgdGhlIGFsaWdubWVudC91bmlmb3JtaXR5IGRlY29tcG9zaXRpb24gaXMgZWFybHkgY29sbGFwc2UgZGV0ZWN0aW9uLiBSZXByZXNlbnRhdGlvbmFsIGNvbGxhcHNlIOKAlCB3aGVyZSB0aGUgZW5jb2RlciBtYXBzIGFsbCBpbnB1dHMgdG8gdGhlIHNhbWUgcG9pbnQg4oCUIHByb2R1Y2VzIHBlcmZlY3QgYWxpZ25tZW50IChMX2FsaWduIOKJiCAwKSBidXQgbWF4aW1hbGx5IGJhZCB1bmlmb3JtaXR5IChMX3VuaWZvcm0g4omIIDAsIHNpbmNlIHRoZSBHYXVzc2lhbiBrZXJuZWwgZm9yIGlkZW50aWNhbCB2ZWN0b3JzIGlzIDEsIGFuZCBsb2coMSkgPSAwKS4gQnkgdHJhY2tpbmcgYm90aCBtZXRyaWNzIGluZGVwZW5kZW50bHkgZHVyaW5nIHRyYWluaW5nLCBwcmFjdGl0aW9uZXJzIGNhbiBkaWFnbm9zZSBjb2xsYXBzZSBiZWZvcmUgaXQgZnVsbHkgc2V0cyBpbi4gTWV0aG9kcyBsaWtlIEJZT0wgdGhhdCBsYWNrIGV4cGxpY2l0IG5lZ2F0aXZlIHRlcm1zIGFyZSBlc3BlY2lhbGx5IHZ1bG5lcmFibGUgdG8gc2lsZW50IGNvbGxhcHNlIOKAlCBtb25pdG9yaW5nIHVuaWZvcm1pdHkgcmV2ZWFscyB0aGlzIGltbWVkaWF0ZWx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuXG5jbGFzcyBDb2xsYXBzZU1vbml0b3I6XG4gICAgXCJcIlwiVHJhY2sgYWxpZ25tZW50IGFuZCB1bmlmb3JtaXR5IGFjcm9zcyB0cmFpbmluZyB0byBkZXRlY3QgY29sbGFwc2UuXCJcIlwiXG5cbiAgICBkZWYgX19pbml0X18oc2VsZiwgd2luZG93OiBpbnQgPSA1MCk6XG4gICAgICAgIHNlbGYud2luZG93ID0gd2luZG93XG4gICAgICAgIHNlbGYuYWxpZ25faGlzdG9yeSAgID0gW11cbiAgICAgICAgc2VsZi51bmlmb3JtX2hpc3RvcnkgPSBbXVxuXG4gICAgZGVmIHVwZGF0ZShzZWxmLCB6MTogdG9yY2guVGVuc29yLCB6MjogdG9yY2guVGVuc29yKTpcbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICB6MW4gPSBGLm5vcm1hbGl6ZSh6MS5kZXRhY2goKSwgZGltPTEpXG4gICAgICAgICAgICB6Mm4gPSBGLm5vcm1hbGl6ZSh6Mi5kZXRhY2goKSwgZGltPTEpXG4gICAgICAgICAgICBhbGlnbiAgID0gKHoxbiAtIHoybikubm9ybShkaW09MSkucG93KDIpLm1lYW4oKS5pdGVtKClcbiAgICAgICAgICAgIHNxX2Rpc3QgPSAyIC0gMiAqICh6MW4gQCB6MW4uVClcbiAgICAgICAgICAgIHVuaWZvcm0gPSB0b3JjaC5leHAoLTIgKiBzcV9kaXN0KS5tZWFuKCkubG9nKCkuaXRlbSgpXG4gICAgICAgIHNlbGYuYWxpZ25faGlzdG9yeS5hcHBlbmQoYWxpZ24pXG4gICAgICAgIHNlbGYudW5pZm9ybV9oaXN0b3J5LmFwcGVuZCh1bmlmb3JtKVxuXG4gICAgZGVmIGlzX2NvbGxhcHNpbmcoc2VsZiwgYWxpZ25fdGhyZXNoOiBmbG9hdCA9IDAuMDUsXG4gICAgICAgICAgICAgICAgICAgICAgdW5pZm9ybV90aHJlc2g6IGZsb2F0ID0gLTAuNSkgLVx1MDAzZSBib29sOlxuICAgICAgICBpZiBsZW4oc2VsZi5hbGlnbl9oaXN0b3J5KSBcdTAwM2Mgc2VsZi53aW5kb3c6XG4gICAgICAgICAgICByZXR1cm4gRmFsc2VcbiAgICAgICAgcmVjZW50X2FsaWduICAgPSBzdW0oc2VsZi5hbGlnbl9oaXN0b3J5Wy1zZWxmLndpbmRvdzpdKSAvIHNlbGYud2luZG93XG4gICAgICAgIHJlY2VudF91bmlmb3JtID0gc3VtKHNlbGYudW5pZm9ybV9oaXN0b3J5Wy1zZWxmLndpbmRvdzpdKSAvIHNlbGYud2luZG93XG4gICAgICAgIHJldHVybiByZWNlbnRfYWxpZ24gXHUwMDNjIGFsaWduX3RocmVzaCBhbmQgcmVjZW50X3VuaWZvcm0gXHUwMDNlIHVuaWZvcm1fdGhyZXNoXG5cbiAgICBkZWYgcmVwb3J0KHNlbGYpOlxuICAgICAgICBpZiBzZWxmLmFsaWduX2hpc3Rvcnk6XG4gICAgICAgICAgICBwcmludChmXHUwMDI3QWxpZ25tZW50OiAgIHtzZWxmLmFsaWduX2hpc3RvcnlbLTFdOi40Zn0gKGxvd2VyPW1vcmUgYWxpZ25lZClcdTAwMjcpXG4gICAgICAgICAgICBwcmludChmXHUwMDI3VW5pZm9ybWl0eTogIHtzZWxmLnVuaWZvcm1faGlzdG9yeVstMV06LjRmfSAobW9yZSBuZWdhdGl2ZT1tb3JlIHVuaWZvcm0pXHUwMDI3KVxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyN0NvbGxhcHNpbmc6ICB7c2VsZi5pc19jb2xsYXBzaW5nKCl9XHUwMDI3KVxuXG5cbm1vbml0b3IgPSBDb2xsYXBzZU1vbml0b3IoKVxudG9yY2gubWFudWFsX3NlZWQoMClcbnoxID0gRi5ub3JtYWxpemUodG9yY2gucmFuZG4oNjQsIDEyOCksIGRpbT0xKVxuejIgPSBGLm5vcm1hbGl6ZSh0b3JjaC5yYW5kbig2NCwgMTI4KSwgZGltPTEpXG5mb3IgXyBpbiByYW5nZSg1NSk6XG4gICAgbW9uaXRvci51cGRhdGUoejEsIHoyKVxubW9uaXRvci5yZXBvcnQoKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQ29sbGFwc2UgSXMgU2lsZW50IFdpdGhvdXQgVW5pZm9ybWl0eSBUcmFja2luZyIsImNvbnRlbnQiOiJNZXRob2RzIHdpdGhvdXQgZXhwbGljaXQgbmVnYXRpdmUgdGVybXMgKEJZT0wsIFNpbVNpYW0sIEpFUEEpIGFyZSBhdCByaXNrIG9mIHJlcHJlc2VudGF0aW9uYWwgY29sbGFwc2Ug4oCUIGFsbCBlbWJlZGRpbmdzIGNvbnZlcmdlIHRvIHRoZSBzYW1lIHBvaW50LiBUaGUgbG9zcyBtYXkgYXBwZWFyIHRvIGRlY3JlYXNlIGV2ZW4gYXMgY29sbGFwc2UgcHJvZ3Jlc3NlcyBiZWNhdXNlIGFsaWdubWVudCBpbXByb3Zlcy4gTW9uaXRvcmluZyB0aGUgdW5pZm9ybWl0eSBtZXRyaWMgc2VwYXJhdGVseSBpcyB0aGUgbW9zdCByZWxpYWJsZSBlYXJseSB3YXJuaW5nLiBJZiB1bmlmb3JtaXR5IHJpc2VzIHRvd2FyZCAwIHdoaWxlIGFsaWdubWVudCBmYWxscyB0b3dhcmQgMCwgY29sbGFwc2UgaXMgaW1taW5lbnQuIEdvb2QgdHJhaW5pbmcgc2hvd3MgYm90aCBtZXRyaWNzIGltcHJvdmluZzogYWxpZ25tZW50IGRlY3JlYXNpbmcgYW5kIHVuaWZvcm1pdHkgYmVjb21pbmcgbW9yZSBuZWdhdGl2ZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbmZvcm1hdGlvbi1UaGVvcmV0aWMgSW50ZXJwcmV0YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVuaWZvcm1pdHkgb24gdGhlIGh5cGVyc3BoZXJlIGlzIGNvbm5lY3RlZCB0byBkaWZmZXJlbnRpYWwgZW50cm9weS4gVGhlIHVuaWZvcm0gZGlzdHJpYnV0aW9uIG9uIHRoZSBzcGhlcmUgaGFzIG1heGltdW0gZW50cm9weSBhbW9uZyBhbGwgZGlzdHJpYnV0aW9ucyB3aXRoIHVuaXQtbm9ybSBzdXBwb3J0IOKAlCBpdCBpcyB0aGUgbWF4aW11bS1lbnRyb3B5IGRpc3RyaWJ1dGlvbiB1bmRlciB0aGUgY29uc3RyYWludCB0aGF0IGZlYXR1cmVzIGFyZSBMMi1ub3JtYWxpc2VkLiBNYXhpbWlzaW5nIHVuaWZvcm1pdHkgaXMgdGhlcmVmb3JlIGVxdWl2YWxlbnQgdG8gbWF4aW1pc2luZyB0aGUgZW50cm9weSBvZiB0aGUgZmVhdHVyZSBkaXN0cmlidXRpb24sIHdoaWNoIGluIHR1cm4gbWF4aW1pc2VzIHRoZSBtdXR1YWwgaW5mb3JtYXRpb24gYmV0d2VlbiBmZWF0dXJlcyBhbmQgaW5wdXQg4oCUIHRoZSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrIHBlcnNwZWN0aXZlIG9uIHJlcHJlc2VudGF0aW9uIGxlYXJuaW5nLiBBbGlnbm1lbnQgc2ltdWx0YW5lb3VzbHkgbWluaW1pc2VzIHRoZSBlbnRyb3B5IG9mIHRoZSBjb25kaXRpb25hbCBmZWF0dXJlIGRpc3RyaWJ1dGlvbiBnaXZlbiB0aGUgYXVnbWVudGVkIHZpZXcuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJVbmlmb3JtaXR5ID0gbWF4aW11bSBlbnRyb3B5IHByaW5jaXBsZSBvbiB1bml0IHNwaGVyZSA9IG1heGltdW0gaW5mb3JtYXRpb24gaW4gZmVhdHVyZSBkaXN0cmlidXRpb24uIiwiQWxpZ25tZW50ID0gbWluaW11bSBlbnRyb3B5IG9mIGNvbmRpdGlvbmFsIGRpc3RyaWJ1dGlvbiBwKGYoeFx1MDAyNyl8Zih4KSkg4oCUIGludmFyaWFuY2UgdG8gbnVpc2FuY2UuIiwiT3B0aW1hbCByZXByZXNlbnRhdGlvbjogcGVyZmVjdCBhbGlnbm1lbnQgd2l0aCBtYXhpbXVtIHVuaWZvcm1pdHkgKHplcm8gcmVkdW5kYW5jeSwgemVybyBjb2xsYXBzZSkuIiwiSW4gcHJhY3RpY2U6IHRoZXNlIHR3byBvYmplY3RpdmVzIGNvbXBldGUg4oCUIHRoZXkgbXVzdCBiZSBiYWxhbmNlZCBieSB0aGUgbG9zcyB3ZWlnaHRpbmcuIiwiTlQtWGVudCB0ZW1wZXJhdHVyZSDPhDogbG93ZXIgz4QgaW5jcmVhc2VzIGdyYWRpZW50IG9uIGhhcmQgbmVnYXRpdmVzLCBzdHJvbmdlciB1bmlmb3JtaXR5IHB1c2guIiwiQmFybG93IFR3aW5zIC8gVklDUmVnIGFjaGlldmUgdW5pZm9ybWl0eSBkaWZmZXJlbnRseSDigJQgdmlhIGNyb3NzLWNvcnJlbGF0aW9uIG9yIHZhcmlhbmNlIHBlbmFsdGllcy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiBBY3Jvc3MgU1NMIE1ldGhvZHMifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQWxpZ25tZW50IE1lY2hhbmlzbSIsIlVuaWZvcm1pdHkgTWVjaGFuaXNtIiwiQ29sbGFwc2UgUHJldmVudGlvbiIsIk5lZWRzIE5lZ2F0aXZlcyJdLCJyb3dzIjpbWyJTaW1DTFIiLCJQb3NpdGl2ZSBwYWlyIHNpbWlsYXJpdHkgbWF4aW1pc2F0aW9uIiwiSW4tYmF0Y2ggbmVnYXRpdmVzIHJlcHVsc2lvbiIsIkltcGxpY2l0IChsYXJnZSBiYXRjaCkiLCJZZXMiXSxbIkJZT0wiLCJPbmxpbmUg4oaSIHRhcmdldCBuZXR3b3JrIE1TRSIsIk5vbmUgZXhwbGljaXQiLCJFTUEgKyBwcmVkaWN0b3IgYXN5bW1ldHJ5IiwiTm8iXSxbIkJhcmxvdyBUd2lucyIsIkNyb3NzLWNvcnJlbGF0aW9uIGRpYWdvbmFsID0gMSIsIk9mZi1kaWFnb25hbCBjcm9zcy1jb3JyZWxhdGlvbiA9IDAiLCJSZWR1bmRhbmN5IHJlZHVjdGlvbiIsIk5vIl0sWyJWSUNSZWciLCJQb3NpdGl2ZSBwYWlyIE1TRSIsIlZhcmlhbmNlIHJlZ3VsYXJpc2VyIHBlciBkaW0iLCJFeHBsaWNpdCB2YXJpYW5jZSB0ZXJtIiwiTm8iXSxbIkRJTk8iLCJDTFMgdG9rZW4gY3Jvc3MtZW50cm9weSBtYXRjaCIsIkNlbnRlcmluZyArIHNoYXJwZW5pbmcgKFNpbmtob3JuKSIsIkNlbnRlcmluZyBwcmV2ZW50cyBjb2xsYXBzZSIsIk5vIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBhbGlnbm1lbnQvdW5pZm9ybWl0eSBmcmFtZXdvcmsgcmV2ZWFscyB0aGF0IG1ldGhvZHMgd2l0aG91dCBuZWdhdGl2ZXMgKEJZT0wsIEJhcmxvdyBUd2lucywgVklDUmVnLCBESU5PKSBhcmUgbm90IGF2b2lkaW5nIHRoZSBmdW5kYW1lbnRhbCB0cmFkZW9mZiDigJQgdGhleSBhcmUgaW1wbGVtZW50aW5nIHVuaWZvcm1pdHkgdGhyb3VnaCBkaWZmZXJlbnQgbWVjaGFuaXNtcy4gQllPTCByZWxpZXMgb24gdGhlIEVNQSBhc3ltbWV0cnkgdG8gaW1wbGljaXRseSBzcHJlYWQgZmVhdHVyZXM7IEJhcmxvdyBUd2lucyB1c2VzIGNyb3NzLWNvcnJlbGF0aW9uIG9mZi1kaWFnb25hbCBwZW5hbHR5OyBWSUNSZWcgYWRkcyBhbiBleHBsaWNpdCB2YXJpYW5jZSB0ZXJtIHBlciBlbWJlZGRpbmcgZGltZW5zaW9uLiBBbGwgYXJlIGdlb21ldHJpYyByZWd1bGFyaXNlcnMgb24gdGhlIGh5cGVyc3BoZXJlLCBhY2hpZXZlaW5nIHRoZSBzYW1lIHB1cnBvc2UgYXMgZXhwbGljaXQgbmVnYXRpdmVzIGJ1dCB0aHJvdWdoIGFyY2hpdGVjdHVyYWwgb3IgbG9zcyBlbmdpbmVlcmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgR3VpZGFuY2UgZm9yIFNTTCBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTG9nIGJvdGggYWxpZ25tZW50IGFuZCB1bmlmb3JtaXR5IGV2ZXJ5IDEwMCBzdGVwcyBkdXJpbmcgdHJhaW5pbmcuIEEgaGVhbHRoeSB0cmFpbmluZyBydW4gc2hvd3MgYWxpZ25tZW50IGRlY3JlYXNpbmcgZnJvbSB+Mi4wIHRvd2FyZCB+MC4xIGFuZCB1bmlmb3JtaXR5IGJlY29taW5nIG1vcmUgbmVnYXRpdmUgKGZyb20gbmVhciAwIHRvd2FyZCAtNC4wIG9yIGxvd2VyKSBhcyBmZWF0dXJlcyBzcHJlYWQuIElmIGFsaWdubWVudCBkZWNyZWFzZXMgYnV0IHVuaWZvcm1pdHkgc3RhZ25hdGVzLCBpbmNyZWFzZSBiYXRjaCBzaXplIG9yIGFkZCBzdHJvbmdlciBhdWdtZW50YXRpb24gdG8gcHJvdmlkZSBtb3JlIGRpdmVyc2UgbmVnYXRpdmVzLiBJZiB1bmlmb3JtaXR5IGltcHJvdmVzIGJ1dCBhbGlnbm1lbnQgcmVtYWlucyBoaWdoLCB0aGUgYXVnbWVudGF0aW9ucyBtYXkgYmUgdG9vIGFnZ3Jlc3NpdmUgb3IgdGhlIHBvc2l0aXZlIHBhaXJzIGFyZSBub3QgY29uc2lzdGVudGx5IHNpbWlsYXIuIFRlbXBlcmF0dXJlIM+EIGlzIHRoZSBwcmltYXJ5IGtub2IgZm9yIHRoZSB1bmlmb3JtaXR54oCTYWxpZ25tZW50IHRyYWRlb2ZmIGluIGNvbnRyYXN0aXZlIG1ldGhvZHM6IGxvd2VyIM+EIGluY3JlYXNlcyB0aGUgdW5pZm9ybWl0eSBncmFkaWVudCBhdCB0aGUgY29zdCBvZiBoYXJkZXIgcG9zaXRpdmUgYWxpZ25tZW50LiJ9XQ=="
---
# Uniformity and Alignment — Geometric Theory of Contrastive Learning

Wang and Isola (2020) offered one of the clearest theoretical frameworks for understanding why contrastive learning works. They showed that contrastive loss on the unit hypersphere can be decomposed into two competing geometric properties: alignment (positive pairs should be close together) and uniformity (all features should be spread as uniformly as possible across the sphere). These two properties are not arbitrary — they correspond to an ideal representation that is maximally informative: positive pairs agree (alignment) and the entire feature space is used without collapse (uniformity).

## Alignment — Attracting Positive Pairs

Alignment measures how well the encoder maps semantically similar inputs to nearby representations. For a distribution of positive pairs (x, x') drawn from the same image with different augmentations, the alignment loss is the expected squared Euclidean distance between their L2-normalised representations: L_align = E_{(x,x')~p_pos}[‖f(x) − f(x')‖²]. For unit-norm vectors, this equals 2(1 − cosine_similarity(f(x), f(x'))). Perfect alignment (L_align = 0) means the encoder is invariant to augmentation — both views map to the exact same point. This is the simplest form of representation learning: invariance to nuisance variation.

```python
import torch
import torch.nn.functional as F


def alignment_loss(z1: torch.Tensor, z2: torch.Tensor, alpha: float = 2.0) -> torch.Tensor:
    """Alignment loss: expected ||f(x) - f(x')||^alpha for positive pairs.
    z1, z2: (N, D) L2-normalised embeddings of two augmented views.
    alpha=2 gives squared Euclidean distance on unit sphere.
    """
    z1 = F.normalize(z1, dim=1)  # ensure unit norm
    z2 = F.normalize(z2, dim=1)
    return (z1 - z2).norm(dim=1).pow(alpha).mean()


def alignment_via_cosine(z1: torch.Tensor, z2: torch.Tensor) -> torch.Tensor:
    """Equivalent: L_align = 2 * (1 - mean cosine similarity)."""
    z1 = F.normalize(z1, dim=1)
    z2 = F.normalize(z2, dim=1)
    cos_sim = (z1 * z2).sum(dim=1)   # (N,) cosine similarity per pair
    return 2 * (1 - cos_sim.mean())


# Demo: perfect alignment, random alignment, collapsed alignment
torch.manual_seed(42)
z = F.normalize(torch.randn(64, 128), dim=1)
print('Perfect alignment (z1 == z2):  ', alignment_loss(z, z).item())          # 0.0

z2_rand = F.normalize(torch.randn(64, 128), dim=1)
print('Random alignment:               ', alignment_loss(z, z2_rand).item())   # ~2.0

z2_noise = F.normalize(z + 0.05 * torch.randn_like(z), dim=1)
print('Near-perfect alignment (noise):', alignment_loss(z, z2_noise).item())   # small
```

## Uniformity — Spreading Features on the Hypersphere

Uniformity measures how evenly the encoder's output distribution covers the unit hypersphere. A completely uniform distribution maximises entropy — every dimension is used and no information is wasted. The uniformity loss uses a Gaussian kernel to measure the average pairwise similarity: L_uniform = log E_{x,y~p_data}[e^{-2‖f(x)−f(y)‖²}]. The Gaussian kernel e^{-2‖u−v‖²} decays from 1 (when u = v) to 0 (when u and v are orthogonal). The log ensures the scale is additive. Minimising L_uniform pushes features apart — the optimal solution is a uniform distribution on the sphere (a perfectly spread packing).

```python
import torch
import torch.nn.functional as F


def uniformity_loss(z: torch.Tensor, t: float = 2.0) -> torch.Tensor:
    """Uniformity loss: log-average of Gaussian kernel over all pairs.
    z: (N, D) L2-normalised embeddings.
    t: Gaussian kernel bandwidth (default 2 gives e^{-2||u-v||^2}).
    """
    z = F.normalize(z, dim=1)                        # (N, D)
    # Pairwise squared distances: ||u-v||^2 = 2 - 2*u.v for unit vectors
    sq_dists = 2 - 2 * (z @ z.T)                    # (N, N)
    # Gaussian kernel; include all pairs (diagonal = self, contributes 1)
    kernel   = torch.exp(-t * sq_dists)              # (N, N)
    # Log average over all N^2 pairs
    return kernel.mean().log()


# Demo: collapsed (all same) vs uniform (random unit vectors)
torch.manual_seed(0)
N, D = 256, 128

# Collapsed: all embeddings identical
z_collapsed = F.normalize(torch.ones(N, D), dim=1)
print('Uniformity (collapsed):', uniformity_loss(z_collapsed).item())   # near 0 (bad)

# Random unit vectors approximate uniform distribution
z_uniform = F.normalize(torch.randn(N, D), dim=1)
print('Uniformity (random):   ', uniformity_loss(z_uniform).item())     # very negative (good)

# Slight cluster structure
z_mixed = F.normalize(torch.randn(N, D) * 0.5 + torch.randn(1, D), dim=1)
print('Uniformity (clustered):', uniformity_loss(z_mixed).item())       # between
```

## NT-Xent as Alignment Plus Uniformity

Wang and Isola proved that the NT-Xent loss (used by SimCLR) asymptotically decomposes into the alignment and uniformity terms. The numerator of NT-Xent maximises the similarity of positive pairs — this is the alignment term. The denominator normalises against all pairs including negatives — this is the uniformity term (pushing features apart). As batch size → ∞, NT-Xent = −alignment_term + uniformity_constant. This decomposition shows that NT-Xent implicitly optimises both geometric properties simultaneously, explaining why it generalises beyond its original contrastive framing.

```python
import torch
import torch.nn.functional as F


def nt_xent_decomposed(z1: torch.Tensor, z2: torch.Tensor,
                       temperature: float = 0.5) -> dict:
    """Compute NT-Xent and its alignment + uniformity decomposition.
    z1, z2: (N, D) L2-normalised embeddings.
    Returns dict with total loss, alignment component, uniformity component.
    """
    N = z1.size(0)
    z1 = F.normalize(z1, dim=1)
    z2 = F.normalize(z2, dim=1)
    z  = torch.cat([z1, z2], dim=0)   # (2N, D)

    # NT-Xent total loss
    sim_mat = (z @ z.T) / temperature   # (2N, 2N)
    mask    = torch.eye(2*N, dtype=torch.bool, device=z.device)
    sim_mat.masked_fill_(mask, float('-inf'))
    labels  = torch.cat([torch.arange(N, 2*N), torch.arange(N)]).to(z.device)
    nt_xent = F.cross_entropy(sim_mat, labels)

    # Alignment component (log numerator, normalised)
    pos_sim = (z1 * z2).sum(dim=1) / temperature   # (N,)
    align   = -pos_sim.mean()

    # Uniformity component (log denominator, approximation)
    uniform = uniformity_loss(z, t=2.0)

    return {'nt_xent': nt_xent.item(), 'alignment': align.item(), 'uniformity': uniform.item()}


torch.manual_seed(7)
z1 = F.normalize(torch.randn(128, 64), dim=1)
z2 = F.normalize(torch.randn(128, 64), dim=1)
result = nt_xent_decomposed(z1, z2)
for k, v in result.items():
    print(f'{k:>12}: {v:.4f}')
```

## Collapse Detection During Training

One of the most practical applications of the alignment/uniformity decomposition is early collapse detection. Representational collapse — where the encoder maps all inputs to the same point — produces perfect alignment (L_align ≈ 0) but maximally bad uniformity (L_uniform ≈ 0, since the Gaussian kernel for identical vectors is 1, and log(1) = 0). By tracking both metrics independently during training, practitioners can diagnose collapse before it fully sets in. Methods like BYOL that lack explicit negative terms are especially vulnerable to silent collapse — monitoring uniformity reveals this immediately.

```python
import torch
import torch.nn.functional as F


class CollapseMonitor:
    """Track alignment and uniformity across training to detect collapse."""

    def __init__(self, window: int = 50):
        self.window = window
        self.align_history   = []
        self.uniform_history = []

    def update(self, z1: torch.Tensor, z2: torch.Tensor):
        with torch.no_grad():
            z1n = F.normalize(z1.detach(), dim=1)
            z2n = F.normalize(z2.detach(), dim=1)
            align   = (z1n - z2n).norm(dim=1).pow(2).mean().item()
            sq_dist = 2 - 2 * (z1n @ z1n.T)
            uniform = torch.exp(-2 * sq_dist).mean().log().item()
        self.align_history.append(align)
        self.uniform_history.append(uniform)

    def is_collapsing(self, align_thresh: float = 0.05,
                      uniform_thresh: float = -0.5) -> bool:
        if len(self.align_history) < self.window:
            return False
        recent_align   = sum(self.align_history[-self.window:]) / self.window
        recent_uniform = sum(self.uniform_history[-self.window:]) / self.window
        return recent_align < align_thresh and recent_uniform > uniform_thresh

    def report(self):
        if self.align_history:
            print(f'Alignment:   {self.align_history[-1]:.4f} (lower=more aligned)')
            print(f'Uniformity:  {self.uniform_history[-1]:.4f} (more negative=more uniform)')
            print(f'Collapsing:  {self.is_collapsing()}')


monitor = CollapseMonitor()
torch.manual_seed(0)
z1 = F.normalize(torch.randn(64, 128), dim=1)
z2 = F.normalize(torch.randn(64, 128), dim=1)
for _ in range(55):
    monitor.update(z1, z2)
monitor.report()
```

> **Collapse Is Silent Without Uniformity Tracking**: Methods without explicit negative terms (BYOL, SimSiam, JEPA) are at risk of representational collapse — all embeddings converge to the same point. The loss may appear to decrease even as collapse progresses because alignment improves. Monitoring the uniformity metric separately is the most reliable early warning. If uniformity rises toward 0 while alignment falls toward 0, collapse is imminent. Good training shows both metrics improving: alignment decreasing and uniformity becoming more negative.

## Information-Theoretic Interpretation

Uniformity on the hypersphere is connected to differential entropy. The uniform distribution on the sphere has maximum entropy among all distributions with unit-norm support — it is the maximum-entropy distribution under the constraint that features are L2-normalised. Maximising uniformity is therefore equivalent to maximising the entropy of the feature distribution, which in turn maximises the mutual information between features and input — the information bottleneck perspective on representation learning. Alignment simultaneously minimises the entropy of the conditional feature distribution given the augmented view.

- Uniformity = maximum entropy principle on unit sphere = maximum information in feature distribution.
- Alignment = minimum entropy of conditional distribution p(f(x')|f(x)) — invariance to nuisance.
- Optimal representation: perfect alignment with maximum uniformity (zero redundancy, zero collapse).
- In practice: these two objectives compete — they must be balanced by the loss weighting.
- NT-Xent temperature τ: lower τ increases gradient on hard negatives, stronger uniformity push.
- Barlow Twins / VICReg achieve uniformity differently — via cross-correlation or variance penalties.

## Comparison Across SSL Methods

| Method | Alignment Mechanism | Uniformity Mechanism | Collapse Prevention | Needs Negatives |
| --- | --- | --- | --- | --- |
| SimCLR | Positive pair similarity maximisation | In-batch negatives repulsion | Implicit (large batch) | Yes |
| BYOL | Online → target network MSE | None explicit | EMA + predictor asymmetry | No |
| Barlow Twins | Cross-correlation diagonal = 1 | Off-diagonal cross-correlation = 0 | Redundancy reduction | No |
| VICReg | Positive pair MSE | Variance regulariser per dim | Explicit variance term | No |
| DINO | CLS token cross-entropy match | Centering + sharpening (Sinkhorn) | Centering prevents collapse | No |

The alignment/uniformity framework reveals that methods without negatives (BYOL, Barlow Twins, VICReg, DINO) are not avoiding the fundamental tradeoff — they are implementing uniformity through different mechanisms. BYOL relies on the EMA asymmetry to implicitly spread features; Barlow Twins uses cross-correlation off-diagonal penalty; VICReg adds an explicit variance term per embedding dimension. All are geometric regularisers on the hypersphere, achieveing the same purpose as explicit negatives but through architectural or loss engineering.

## Practical Guidance for SSL Training

Log both alignment and uniformity every 100 steps during training. A healthy training run shows alignment decreasing from ~2.0 toward ~0.1 and uniformity becoming more negative (from near 0 toward -4.0 or lower) as features spread. If alignment decreases but uniformity stagnates, increase batch size or add stronger augmentation to provide more diverse negatives. If uniformity improves but alignment remains high, the augmentations may be too aggressive or the positive pairs are not consistently similar. Temperature τ is the primary knob for the uniformity–alignment tradeoff in contrastive methods: lower τ increases the uniformity gradient at the cost of harder positive alignment.

