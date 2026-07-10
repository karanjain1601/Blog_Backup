---
title: "Contrastive Losses — Triplet, NT-Xent, and InfoNCE"
slug: "contrastive-losses"
description: "Learn how contrastive losses train embeddings where similar pairs cluster close and dissimilar pairs push apart — covering triplet loss with hard negative mining, NT-Xent (SimCLR), InfoNCE (MoCo), and SupCon, with full implementations."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udHJhc3RpdmUgbGVhcm5pbmcgdHJhaW5zIGFuIGVtYmVkZGluZyBmdW5jdGlvbiBmOiBYIOKGkiDihJ3htYggc3VjaCB0aGF0IHNlbWFudGljYWxseSBzaW1pbGFyIGlucHV0cyBtYXAgdG8gbmVhcmJ5IHBvaW50cyBhbmQgZGlzc2ltaWxhciBpbnB1dHMgdG8gZGlzdGFudCBvbmVzLiBVbmxpa2Ugc3VwZXJ2aXNlZCBjcm9zcy1lbnRyb3B5IHdoaWNoIHRyYWlucyBwZXItY2xhc3MgZGVjaXNpb24gYm91bmRhcmllcywgY29udHJhc3RpdmUgbG9zc2VzIG9wZXJhdGUgb24gcGFpcnMgb3IgdHJpcGxldHMgYW5kIGRpcmVjdGx5IHNoYXBlIHRoZSBnZW9tZXRyeSBvZiB0aGUgcmVwcmVzZW50YXRpb24gc3BhY2UuIFRoZSBmaWVsZCBwcm9kdWNlZCB0aHJlZSBkb21pbmFudCBsb3NzIGZvcm11bGF0aW9ucyDigJQgdHJpcGxldCwgTlQtWGVudCwgYW5kIEluZm9OQ0Ug4oCUIGVhY2ggd2l0aCBkaWZmZXJlbnQgYXNzdW1wdGlvbnMgYWJvdXQgaG93IG5lZ2F0aXZlcyBhcmUgc291cmNlZCBhbmQgY291bnRlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmlwbGV0IExvc3MgYW5kIEhhcmQgTmVnYXRpdmUgTWluaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmlwbGV0IGxvc3Mgb3BlcmF0ZXMgb24gYW4gYW5jaG9yIGEsIGEgcG9zaXRpdmUgcCAoc2FtZSBjbGFzcyBvciBhdWdtZW50ZWQgdmlldyksIGFuZCBhIG5lZ2F0aXZlIG4gKGRpZmZlcmVudCBjbGFzcykuIFRoZSBsb3NzIGlzIEwgPSBtYXgoMCwgZChhLHApIOKIkiBkKGEsbikgKyDOsSkgd2hlcmUgZCBpcyBFdWNsaWRlYW4gb3IgY29zaW5lIGRpc3RhbmNlIGFuZCDOsSBcdTAwM2UgMCBpcyB0aGUgbWFyZ2luLiBHZW9tZXRyaWNhbGx5LCB0aGlzIHB1c2hlcyB0aGUgbmVnYXRpdmUgYXQgbGVhc3QgzrEgZnVydGhlciBmcm9tIHRoZSBhbmNob3IgdGhhbiB0aGUgcG9zaXRpdmUuIFdpdGggcmFuZG9tIG5lZ2F0aXZlcyB0aGUgbG9zcyBzYXR1cmF0ZXMgcXVpY2tseSDigJQgaGFyZCBuZWdhdGl2ZSBtaW5pbmcgc2VsZWN0cyBuZWdhdGl2ZXMgdGhhdCB2aW9sYXRlIHRoZSBtYXJnaW4sIGtlZXBpbmcgZ3JhZGllbnRzIGluZm9ybWF0aXZlIHRocm91Z2hvdXQgdHJhaW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBoYXJkX25lZ2F0aXZlX3RyaXBsZXRfbG9zcyhlbWJlZGRpbmdzLCBsYWJlbHMsIG1hcmdpbj0wLjMpOlxuICAgIEIgPSBlbWJlZGRpbmdzLnNpemUoMClcbiAgICBkaXN0ID0gdG9yY2guY2Rpc3QoZW1iZWRkaW5ncywgZW1iZWRkaW5ncywgcD0yKVxuICAgIGxvc3NfdG90YWwgPSB0b3JjaC50ZW5zb3IoMC4wKVxuICAgIG5fdHJpcGxldHMgPSAwXG4gICAgZm9yIGkgaW4gcmFuZ2UoQik6XG4gICAgICAgIGlkeCA9IHRvcmNoLmFyYW5nZShCKVxuICAgICAgICBwb3NfbWFzayA9IChsYWJlbHMgPT0gbGFiZWxzW2ldKSBcdTAwMjYgKGlkeCAhPSBpKVxuICAgICAgICBuZWdfbWFzayA9IGxhYmVscyAhPSBsYWJlbHNbaV1cbiAgICAgICAgaWYgbm90IHBvc19tYXNrLmFueSgpIG9yIG5vdCBuZWdfbWFzay5hbnkoKTpcbiAgICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgIGRfYXAgPSBkaXN0W2ldW3Bvc19tYXNrXS5tYXgoKVxuICAgICAgICBkX2FuID0gZGlzdFtpXVtuZWdfbWFza10ubWluKClcbiAgICAgICAgbG9zc190b3RhbCA9IGxvc3NfdG90YWwgKyBGLnJlbHUoZF9hcCAtIGRfYW4gKyBtYXJnaW4pXG4gICAgICAgIG5fdHJpcGxldHMgKz0gMVxuICAgIHJldHVybiBsb3NzX3RvdGFsIC8gbWF4KG5fdHJpcGxldHMsIDEpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuZW1icyA9IEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKDE2LCAxMjgpLCBkaW09MSlcbmxhYmVscyA9IHRvcmNoLnRlbnNvcihbMCwwLDAsMCwxLDEsMSwxLDIsMiwyLDIsMywzLDMsM10pXG5wcmludChmXHUwMDI3VHJpcGxldCBsb3NzOiB7aGFyZF9uZWdhdGl2ZV90cmlwbGV0X2xvc3MoZW1icywgbGFiZWxzKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5ULVhlbnQgTG9zcyAoU2ltQ0xSKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTlQtWGVudCAoTm9ybWFsaXplZCBUZW1wZXJhdHVyZS1zY2FsZWQgQ3Jvc3MgRW50cm9weSkgaXMgdGhlIGxvc3MgdXNlZCBpbiBTaW1DTFIuIEZvciBhIGJhdGNoIG9mIE4gZXhhbXBsZXMsIGVhY2ggaXMgYXVnbWVudGVkIHR3aWNlIHRvIHByb2R1Y2UgMk4gdmlld3MuIEZvciBhIHBvc2l0aXZlIHBhaXIgKGksaik6IExfe2ksan0gPSDiiJJsb2dbZXhwKHNpbSh64bWiLHrisbwpL8+EKSAvIM6jX3tr4omgaX0gZXhwKHNpbSh64bWiLHrigpYpL8+EKV0uIFRoZSBkZW5vbWluYXRvciBzdW1zIG92ZXIgYWxsIDJO4oiSMiBuZWdhdGl2ZXMuIFRlbXBlcmF0dXJlIM+EIGNvbnRyb2xzIHNoYXJwbmVzcyDigJQgbG93IM+EIGNvbmNlbnRyYXRlcyB0aGUgZGlzdHJpYnV0aW9uLCBtYWtpbmcgdGhlIHRhc2sgaGFyZGVyLiBTaW1DTFIgc2hvd2VkIHRoYXQgbGFyZ2VyIGJhdGNoZXMgYXJlIGNyaXRpY2FsIGJlY2F1c2UgdGhleSBwcm92aWRlIG1vcmUgbmVnYXRpdmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIG50X3hlbnRfbG9zcyh6MSwgejIsIHRlbXBlcmF0dXJlPTAuNSk6XG4gICAgQiA9IHoxLnNpemUoMClcbiAgICB6ID0gRi5ub3JtYWxpemUodG9yY2guY2F0KFt6MSwgejJdLCBkaW09MCksIGRpbT0xKVxuICAgIHNpbSA9IHRvcmNoLm1tKHosIHoudCgpKSAvIHRlbXBlcmF0dXJlXG4gICAgbWFzayA9IHRvcmNoLmV5ZSgyICogQiwgZHR5cGU9dG9yY2guYm9vbClcbiAgICBzaW0ubWFza2VkX2ZpbGxfKG1hc2ssIGZsb2F0KFx1MDAyNy1pbmZcdTAwMjcpKVxuICAgIGxhYmVscyA9IHRvcmNoLmNhdChbdG9yY2guYXJhbmdlKEIsIDIqQiksIHRvcmNoLmFyYW5nZShCKV0pXG4gICAgcmV0dXJuIEYuY3Jvc3NfZW50cm9weShzaW0sIGxhYmVscylcblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIEQgPSA2NCwgMTI4XG56MSA9IEYubm9ybWFsaXplKHRvcmNoLnJhbmRuKEIsIEQpLCBkaW09MSlcbnoyID0gRi5ub3JtYWxpemUoejEgKyAwLjEgKiB0b3JjaC5yYW5kbihCLCBEKSwgZGltPTEpXG5mb3IgdGF1IGluIFswLjEsIDAuNSwgMS4wXTpcbiAgICBwcmludChmXHUwMDI3dGF1PXt0YXV9OiBOVC1YZW50ID0ge250X3hlbnRfbG9zcyh6MSwgejIsIHRlbXBlcmF0dXJlPXRhdSk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbmZvTkNFIExvc3MgKE1vQ28gU3R5bGUgd2l0aCBRdWV1ZSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluZm9OQ0UgKGZyb20gQ29udHJhc3RpdmUgUHJlZGljdGl2ZSBDb2RpbmcpIGlzIGEgbG93ZXIgYm91bmQgb24gbXV0dWFsIGluZm9ybWF0aW9uIEkoWDtZKS4gTW9DbyB1c2VzIGEgcXVldWUgb2YgSyBuZWdhdGl2ZXMgbWFpbnRhaW5lZCBhY3Jvc3MgYmF0Y2hlcywgYWxsb3dpbmcgbGFyZ2UgZWZmZWN0aXZlIGJhdGNoIHNpemVzIHdpdGhvdXQgcHJvcG9ydGlvbmFsbHkgaW5jcmVhc2luZyBHUFUgbWVtb3J5LiBUaGUgbW9tZW50dW0gZW5jb2RlciB1cGRhdGUgaXMgzrjigpYg4oaQIG3Ct8644oKWICsgKDHiiJJtKcK3zrhxIChFTUEpLCBlbnN1cmluZyBxdWV1ZSBrZXlzIHN0YXkgY29uc2lzdGVudCBkZXNwaXRlIG5vdCBiZWluZyBlbmQtdG8tZW5kIGRpZmZlcmVudGlhdGVkLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IGNvcHlcblxuY2xhc3MgSW5mb05DRVdpdGhRdWV1ZShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBlbmNvZGVyLCBkaW09MTI4LCBLPTQwOTYsIG09MC45OTksIHRhdT0wLjA3KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jb2Rlcl9xID0gZW5jb2RlclxuICAgICAgICBzZWxmLmVuY29kZXJfayA9IGNvcHkuZGVlcGNvcHkoZW5jb2RlcilcbiAgICAgICAgZm9yIHAgaW4gc2VsZi5lbmNvZGVyX2sucGFyYW1ldGVycygpOiBwLnJlcXVpcmVzX2dyYWRfKEZhbHNlKVxuICAgICAgICBzZWxmLnRhdSwgc2VsZi5tID0gdGF1LCBtXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFx1MDAyN3F1ZXVlXHUwMDI3LCBGLm5vcm1hbGl6ZSh0b3JjaC5yYW5kbihkaW0sIEspLCBkaW09MCkpXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFx1MDAyN3B0clx1MDAyNywgdG9yY2guemVyb3MoMSwgZHR5cGU9dG9yY2gubG9uZykpXG5cbiAgICBAdG9yY2gubm9fZ3JhZCgpXG4gICAgZGVmIF9lbWEoc2VsZik6XG4gICAgICAgIGZvciBwcSwgcGsgaW4gemlwKHNlbGYuZW5jb2Rlcl9xLnBhcmFtZXRlcnMoKSwgc2VsZi5lbmNvZGVyX2sucGFyYW1ldGVycygpKTpcbiAgICAgICAgICAgIHBrLmRhdGEgPSBway5kYXRhICogc2VsZi5tICsgcHEuZGF0YSAqICgxIC0gc2VsZi5tKVxuXG4gICAgQHRvcmNoLm5vX2dyYWQoKVxuICAgIGRlZiBfZW5xdWV1ZShzZWxmLCBrKTpcbiAgICAgICAgcHRyID0gaW50KHNlbGYucHRyKVxuICAgICAgICBzZWxmLnF1ZXVlWzosIHB0cjpwdHIray5zaXplKDApXSA9IGsuVFxuICAgICAgICBzZWxmLnB0clswXSA9IChwdHIgKyBrLnNpemUoMCkpICUgc2VsZi5xdWV1ZS5zaXplKDEpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4cSwgeGspOlxuICAgICAgICBxID0gRi5ub3JtYWxpemUoc2VsZi5lbmNvZGVyX3EoeHEpLCBkaW09MSlcbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICBzZWxmLl9lbWEoKVxuICAgICAgICAgICAgayA9IEYubm9ybWFsaXplKHNlbGYuZW5jb2Rlcl9rKHhrKSwgZGltPTEpXG4gICAgICAgIGxfcG9zID0gKHEgKiBrKS5zdW0oMSwga2VlcGRpbT1UcnVlKSAvIHNlbGYudGF1XG4gICAgICAgIGxfbmVnID0gcSBAIHNlbGYucXVldWUuZGV0YWNoKCkgLyBzZWxmLnRhdVxuICAgICAgICBsb3NzID0gRi5jcm9zc19lbnRyb3B5KHRvcmNoLmNhdChbbF9wb3MsIGxfbmVnXSwgZGltPTEpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvcmNoLnplcm9zKHEuc2l6ZSgwKSwgZHR5cGU9dG9yY2gubG9uZykpXG4gICAgICAgIHNlbGYuX2VucXVldWUoaylcbiAgICAgICAgcmV0dXJuIGxvc3MifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdXBlcnZpc2VkIENvbnRyYXN0aXZlIExvc3MgKFN1cENvbikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN1cENvbiAoS2hvc2xhIGV0IGFsLiAyMDIwKSBleHRlbmRzIE5ULVhlbnQgdG8gdGhlIHN1cGVydmlzZWQgc2V0dGluZy4gSW5zdGVhZCBvZiB0cmVhdGluZyBvbmx5IHRoZSBhdWdtZW50ZWQgcGFpciBhcyBwb3NpdGl2ZXMsIGFsbCBzYW1wbGVzIGZyb20gdGhlIHNhbWUgY2xhc3MgYWN0IGFzIHBvc2l0aXZlczogTF9zdXAgPSDOo+G1oiAo4oiSMS98UChpKXwpIM6jX3tw4oiIUChpKX0gbG9nW2V4cChzaW0oeuG1oix64oKaKS/PhCkgLyDOo197a+KJoGl9IGV4cChzaW0oeuG1oix64oKWKS/PhCldLiBUaGlzIGNvbnNpc3RlbnRseSBvdXRwZXJmb3JtcyBjcm9zcy1lbnRyb3B5IG9uIEltYWdlTmV0IGJ5IDHigJMyJSBiZWNhdXNlIHRoZSBsb3NzIGV4cGxpY2l0bHkgc2hhcGVzIGVtYmVkZGluZyBnZW9tZXRyeS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBzdXBjb25fbG9zcyhlbWJlZGRpbmdzLCBsYWJlbHMsIHRlbXBlcmF0dXJlPTAuMSk6XG4gICAgQiA9IGVtYmVkZGluZ3Muc2l6ZSgwKVxuICAgIHogPSBGLm5vcm1hbGl6ZShlbWJlZGRpbmdzLCBkaW09MSlcbiAgICBzaW0gPSB0b3JjaC5tbSh6LCB6LnQoKSkgLyB0ZW1wZXJhdHVyZVxuICAgIGxhYmVsX21hc2sgPSAobGFiZWxzLnVuc3F1ZWV6ZSgwKSA9PSBsYWJlbHMudW5zcXVlZXplKDEpKVxuICAgIHNlbGZfbWFzayAgPSB0b3JjaC5leWUoQiwgZHR5cGU9dG9yY2guYm9vbClcbiAgICBwb3NfbWFzayAgID0gbGFiZWxfbWFzayBcdTAwMjYgfnNlbGZfbWFza1xuICAgIHNpbS5tYXNrZWRfZmlsbF8oc2VsZl9tYXNrLCBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSlcbiAgICBsb2dfcHJvYiA9IHNpbSAtIHRvcmNoLmxvZ3N1bWV4cChzaW0sIGRpbT0xLCBrZWVwZGltPVRydWUpXG4gICAgbl9wb3MgPSBwb3NfbWFzay5zdW0oMSkuY2xhbXAobWluPTEpXG4gICAgbG9zcyAgPSAtKGxvZ19wcm9iICogcG9zX21hc2spLnN1bSgxKSAvIG5fcG9zXG4gICAgcmV0dXJuIGxvc3MubWVhbigpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5CLCBEID0gMzIsIDY0XG5lbWIgPSB0b3JjaC5yYW5kbihCLCBEKVxubGJsID0gdG9yY2gudGVuc29yKFtpIC8vIDggZm9yIGkgaW4gcmFuZ2UoQildKVxucHJpbnQoZlx1MDAyN1N1cENvbiBsb3NzOiB7c3VwY29uX2xvc3MoZW1iLCBsYmwpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJvamVjdGlvbiBIZWFkIGFuZCBSZXByZXNlbnRhdGlvbiBRdWFsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIDItbGF5ZXIgTUxQIHByb2plY3Rpb24gaGVhZCB6ID0gZyhoKSBwbGFjZWQgYmV0d2VlbiB0aGUgZW5jb2RlciBvdXRwdXQgYW5kIHRoZSBjb250cmFzdGl2ZSBsb3NzIGltcHJvdmVzIGRvd25zdHJlYW0gbGluZWFyIHByb2JpbmcgcGVyZm9ybWFuY2UuIFRoZSBwcm9qZWN0aW9uIGhlYWQgd2FycHMgdGhlIGVtYmVkZGluZyBzcGFjZSBpbiB3YXlzIHRoYXQgb3B0aW1pemUgdGhlIGNvbnRyYXN0aXZlIG9iamVjdGl2ZSBidXQgaHVydCBsaW5lYXIgc2VwYXJhYmlsaXR5LiBEaXNjYXJkaW5nIHRoZSBwcm9qZWN0aW9uIGhlYWQgYW5kIHVzaW5nIGggZm9yIGRvd25zdHJlYW0gdGFza3MgcmVjb3ZlcnMgdGhpcyBxdWFsaXR5LiBUaGlzIHdhcyB0aGUga2V5IGVuZ2luZWVyaW5nIGluc2lnaHQgaW4gU2ltQ0xSIOKAlCB0aGUgbG9zcyBzaG91bGQgYWN0IG9uIHByb2plY3RlZCBlbWJlZGRpbmdzLCBub3Qgb24gdGhlIGZpbmFsIHJlcHJlc2VudGF0aW9uLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTDItbm9ybWFsaXppbmcgZW1iZWRkaW5ncyBiZWZvcmUgY29tcHV0aW5nIGNvc2luZSBzaW1pbGFyaXR5IGlzIGVxdWFsbHkgaW1wb3J0YW50LiBXaXRob3V0IG5vcm1hbGl6YXRpb24sIHRoZSBlbWJlZGRpbmcgbm9ybSBhYnNvcmJzIHRoZSB0ZW1wZXJhdHVyZSBzY2FsaW5nIGFuZCB0aGUgbG9zcyBkZWdlbmVyYXRlcyDigJQgaGlnaC1ub3JtIGVtYmVkZGluZ3MgYWx3YXlzIGRvbWluYXRlIHRoZSBzb2Z0bWF4IHJlZ2FyZGxlc3Mgb2YgZGlyZWN0aW9uLiBOb3JtYWxpemUgYmVmb3JlIGJvdGggdGhlIGNvbnRyYXN0aXZlIGxvc3MgYW5kIGFueSBkb3duc3RyZWFtIGV2YWx1YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hvb3NpbmcgdGhlIFJpZ2h0IExvc3MifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiVGVtcGVyYXR1cmUgz4QgU2VsZWN0aW9uIiwiY29udGVudCI6IlRvbyBoaWdoICjPhCDihpIgMSk6IGFsbCBzaW1pbGFyaXRpZXMgcm91Z2hseSBlcXVhbCwgbW9kZWwgY2Fubm90IGRpc2NyaW1pbmF0ZS4gVG9vIGxvdyAoz4Qg4oaSIDApOiBsb3NzIGZvY3VzZXMgb25seSBvbiB0aGUgc2luZ2xlIGhhcmRlc3QgbmVnYXRpdmUuIFNpbUNMUiBmb3VuZCDPhD0wLjUgb3B0aW1hbDsgTW9DbyB1c2VzIM+EPTAuMDcuIEFsd2F5cyBzd2VlcCDPhCB3aXRoIGEgc21hbGwgbGluZWFyIHByb2JlIGVhcmx5IGluIHRyYWluaW5nLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJMb3NzIiwiTmVnYXRpdmVzIHBlciBzYW1wbGUiLCJCYXRjaCBzaXplIHNlbnNpdGl2aXR5IiwiVGVtcGVyYXR1cmUiLCJCZXN0IHVzZSBjYXNlIl0sInJvd3MiOltbIlRyaXBsZXQiLCIxIGhhcmRlc3QgbmVnYXRpdmUiLCJMb3cg4oCUIHdvcmtzIHdpdGggc21hbGwgYmF0Y2hlcyIsIk5vbmUgKG1hcmdpbiDOsSkiLCJNZXRyaWMgbGVhcm5pbmcsIGZhY2UgdmVyaWZpY2F0aW9uIl0sWyJOVC1YZW50IChTaW1DTFIpIiwiMk7iiJIyIGluLWJhdGNoIiwiSGlnaCDigJQgbmVlZHMg4omlMjU2Iiwiz4Qg4oiIIFswLjEsIDAuNV0iLCJTZWxmLXN1cGVydmlzZWQgY29udHJhc3RpdmUgcHJlLXRyYWluaW5nIl0sWyJJbmZvTkNFIChNb0NvKSIsIlF1ZXVlIEs9NDA5NuKAkzY1NTM2IiwiTG93IOKAlCBxdWV1ZSBkZWNvdXBsZXMgZnJvbSBiYXRjaCIsIs+EIOKIiCBbMC4wMywgMC4xXSIsIk1lbW9yeS1lZmZpY2llbnQgU1NMIGF0IGFueSBiYXRjaCBzaXplIl0sWyJTdXBDb24iLCJBbGwgbm9uLXNhbWUtY2xhc3MgaW4gYmF0Y2giLCJNZWRpdW0iLCLPhCDiiIggWzAuMSwgMC41XSIsIlN1cGVydmlzZWQgZmluZS10dW5pbmcsIGxhYmVsLWVmZmljaWVudCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFByYWN0aWNhbCBSdWxlcyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiSGFyZCBuZWdhdGl2ZSBtaW5pbmcgaXMgZXNzZW50aWFsIGZvciB0cmlwbGV0IOKAlCByYW5kb20gbmVnYXRpdmVzIHNhdHVyYXRlIHRoZSBsb3NzIGluIDHigJMyIGVwb2Nocy4iLCJOVC1YZW50IHRyZWF0cyB0aGUgZW50aXJlIDJOIGJhdGNoIGFzIG5lZ2F0aXZlcyBleGNlcHQgdGhlIHBhaXJlZCB2aWV3OyBiYXRjaCBzaXplIGlzIGEgaHlwZXJwYXJhbWV0ZXIuIiwiSW5mb05DRSBsb3dlci1ib3VuZHMgbXV0dWFsIGluZm9ybWF0aW9uIOKAlCBtYXhpbWl6aW5nIGl0IG1heGltaXplcyByZXByZXNlbnRhdGlvbiBxdWFsaXR5IHVwIHRvIGVuY29kZXIgY2FwYWNpdHkuIiwiVXNlIGEgMi1sYXllciBNTFAgcHJvamVjdGlvbiBoZWFkIGR1cmluZyB0cmFpbmluZzsgZGlzY2FyZCBpdCBmb3IgZG93bnN0cmVhbSB0YXNrcy4iLCJBbHdheXMgTDItbm9ybWFsaXplIGVtYmVkZGluZ3MgYmVmb3JlIGNvbXB1dGluZyBjb3NpbmUgc2ltaWxhcml0eS4iLCJTdXBDb24gY29uc2lzdGVudGx5IGJlYXRzIGNyb3NzLWVudHJvcHkgYnkgMeKAkzIlIG9uIEltYWdlTmV0LXNjYWxlIGJlbmNobWFya3MuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Contrastive Losses — Triplet, NT-Xent, and InfoNCE

Contrastive learning trains an embedding function f: X → ℝᵈ such that semantically similar inputs map to nearby points and dissimilar inputs to distant ones. Unlike supervised cross-entropy which trains per-class decision boundaries, contrastive losses operate on pairs or triplets and directly shape the geometry of the representation space. The field produced three dominant loss formulations — triplet, NT-Xent, and InfoNCE — each with different assumptions about how negatives are sourced and counted.

## Triplet Loss and Hard Negative Mining

Triplet loss operates on an anchor a, a positive p (same class or augmented view), and a negative n (different class). The loss is L = max(0, d(a,p) − d(a,n) + α) where d is Euclidean or cosine distance and α > 0 is the margin. Geometrically, this pushes the negative at least α further from the anchor than the positive. With random negatives the loss saturates quickly — hard negative mining selects negatives that violate the margin, keeping gradients informative throughout training.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def hard_negative_triplet_loss(embeddings, labels, margin=0.3):
    B = embeddings.size(0)
    dist = torch.cdist(embeddings, embeddings, p=2)
    loss_total = torch.tensor(0.0)
    n_triplets = 0
    for i in range(B):
        idx = torch.arange(B)
        pos_mask = (labels == labels[i]) & (idx != i)
        neg_mask = labels != labels[i]
        if not pos_mask.any() or not neg_mask.any():
            continue
        d_ap = dist[i][pos_mask].max()
        d_an = dist[i][neg_mask].min()
        loss_total = loss_total + F.relu(d_ap - d_an + margin)
        n_triplets += 1
    return loss_total / max(n_triplets, 1)

torch.manual_seed(42)
embs = F.normalize(torch.randn(16, 128), dim=1)
labels = torch.tensor([0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3])
print(f'Triplet loss: {hard_negative_triplet_loss(embs, labels):.4f}')
```

## NT-Xent Loss (SimCLR)

NT-Xent (Normalized Temperature-scaled Cross Entropy) is the loss used in SimCLR. For a batch of N examples, each is augmented twice to produce 2N views. For a positive pair (i,j): L_{i,j} = −log[exp(sim(zᵢ,zⱼ)/τ) / Σ_{k≠i} exp(sim(zᵢ,zₖ)/τ)]. The denominator sums over all 2N−2 negatives. Temperature τ controls sharpness — low τ concentrates the distribution, making the task harder. SimCLR showed that larger batches are critical because they provide more negatives.

```python
import torch
import torch.nn.functional as F

def nt_xent_loss(z1, z2, temperature=0.5):
    B = z1.size(0)
    z = F.normalize(torch.cat([z1, z2], dim=0), dim=1)
    sim = torch.mm(z, z.t()) / temperature
    mask = torch.eye(2 * B, dtype=torch.bool)
    sim.masked_fill_(mask, float('-inf'))
    labels = torch.cat([torch.arange(B, 2*B), torch.arange(B)])
    return F.cross_entropy(sim, labels)

torch.manual_seed(0)
B, D = 64, 128
z1 = F.normalize(torch.randn(B, D), dim=1)
z2 = F.normalize(z1 + 0.1 * torch.randn(B, D), dim=1)
for tau in [0.1, 0.5, 1.0]:
    print(f'tau={tau}: NT-Xent = {nt_xent_loss(z1, z2, temperature=tau):.4f}')
```

## InfoNCE Loss (MoCo Style with Queue)

InfoNCE (from Contrastive Predictive Coding) is a lower bound on mutual information I(X;Y). MoCo uses a queue of K negatives maintained across batches, allowing large effective batch sizes without proportionally increasing GPU memory. The momentum encoder update is θₖ ← m·θₖ + (1−m)·θq (EMA), ensuring queue keys stay consistent despite not being end-to-end differentiated.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import copy

class InfoNCEWithQueue(nn.Module):
    def __init__(self, encoder, dim=128, K=4096, m=0.999, tau=0.07):
        super().__init__()
        self.encoder_q = encoder
        self.encoder_k = copy.deepcopy(encoder)
        for p in self.encoder_k.parameters(): p.requires_grad_(False)
        self.tau, self.m = tau, m
        self.register_buffer('queue', F.normalize(torch.randn(dim, K), dim=0))
        self.register_buffer('ptr', torch.zeros(1, dtype=torch.long))

    @torch.no_grad()
    def _ema(self):
        for pq, pk in zip(self.encoder_q.parameters(), self.encoder_k.parameters()):
            pk.data = pk.data * self.m + pq.data * (1 - self.m)

    @torch.no_grad()
    def _enqueue(self, k):
        ptr = int(self.ptr)
        self.queue[:, ptr:ptr+k.size(0)] = k.T
        self.ptr[0] = (ptr + k.size(0)) % self.queue.size(1)

    def forward(self, xq, xk):
        q = F.normalize(self.encoder_q(xq), dim=1)
        with torch.no_grad():
            self._ema()
            k = F.normalize(self.encoder_k(xk), dim=1)
        l_pos = (q * k).sum(1, keepdim=True) / self.tau
        l_neg = q @ self.queue.detach() / self.tau
        loss = F.cross_entropy(torch.cat([l_pos, l_neg], dim=1),
                               torch.zeros(q.size(0), dtype=torch.long))
        self._enqueue(k)
        return loss
```

## Supervised Contrastive Loss (SupCon)

SupCon (Khosla et al. 2020) extends NT-Xent to the supervised setting. Instead of treating only the augmented pair as positives, all samples from the same class act as positives: L_sup = Σᵢ (−1/|P(i)|) Σ_{p∈P(i)} log[exp(sim(zᵢ,zₚ)/τ) / Σ_{k≠i} exp(sim(zᵢ,zₖ)/τ)]. This consistently outperforms cross-entropy on ImageNet by 1–2% because the loss explicitly shapes embedding geometry.

```python
import torch
import torch.nn.functional as F

def supcon_loss(embeddings, labels, temperature=0.1):
    B = embeddings.size(0)
    z = F.normalize(embeddings, dim=1)
    sim = torch.mm(z, z.t()) / temperature
    label_mask = (labels.unsqueeze(0) == labels.unsqueeze(1))
    self_mask  = torch.eye(B, dtype=torch.bool)
    pos_mask   = label_mask & ~self_mask
    sim.masked_fill_(self_mask, float('-inf'))
    log_prob = sim - torch.logsumexp(sim, dim=1, keepdim=True)
    n_pos = pos_mask.sum(1).clamp(min=1)
    loss  = -(log_prob * pos_mask).sum(1) / n_pos
    return loss.mean()

torch.manual_seed(0)
B, D = 32, 64
emb = torch.randn(B, D)
lbl = torch.tensor([i // 8 for i in range(B)])
print(f'SupCon loss: {supcon_loss(emb, lbl):.4f}')
```

## Projection Head and Representation Quality

A 2-layer MLP projection head z = g(h) placed between the encoder output and the contrastive loss improves downstream linear probing performance. The projection head warps the embedding space in ways that optimize the contrastive objective but hurt linear separability. Discarding the projection head and using h for downstream tasks recovers this quality. This was the key engineering insight in SimCLR — the loss should act on projected embeddings, not on the final representation.

L2-normalizing embeddings before computing cosine similarity is equally important. Without normalization, the embedding norm absorbs the temperature scaling and the loss degenerates — high-norm embeddings always dominate the softmax regardless of direction. Normalize before both the contrastive loss and any downstream evaluation.

## Choosing the Right Loss

> **Temperature τ Selection**: Too high (τ → 1): all similarities roughly equal, model cannot discriminate. Too low (τ → 0): loss focuses only on the single hardest negative. SimCLR found τ=0.5 optimal; MoCo uses τ=0.07. Always sweep τ with a small linear probe early in training.

| Loss | Negatives per sample | Batch size sensitivity | Temperature | Best use case |
| --- | --- | --- | --- | --- |
| Triplet | 1 hardest negative | Low — works with small batches | None (margin α) | Metric learning, face verification |
| NT-Xent (SimCLR) | 2N−2 in-batch | High — needs ≥256 | τ ∈ [0.1, 0.5] | Self-supervised contrastive pre-training |
| InfoNCE (MoCo) | Queue K=4096–65536 | Low — queue decouples from batch | τ ∈ [0.03, 0.1] | Memory-efficient SSL at any batch size |
| SupCon | All non-same-class in batch | Medium | τ ∈ [0.1, 0.5] | Supervised fine-tuning, label-efficient |

## Key Practical Rules

- Hard negative mining is essential for triplet — random negatives saturate the loss in 1–2 epochs.
- NT-Xent treats the entire 2N batch as negatives except the paired view; batch size is a hyperparameter.
- InfoNCE lower-bounds mutual information — maximizing it maximizes representation quality up to encoder capacity.
- Use a 2-layer MLP projection head during training; discard it for downstream tasks.
- Always L2-normalize embeddings before computing cosine similarity.
- SupCon consistently beats cross-entropy by 1–2% on ImageNet-scale benchmarks.

---

