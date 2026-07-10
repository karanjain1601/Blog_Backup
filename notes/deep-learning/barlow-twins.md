---
title: "Barlow Twins — Cross-Correlation Matrix and Redundancy Reduction"
slug: "barlow-twins"
description: "Barlow Twins (Zbontar et al. 2021) avoids representational collapse by enforcing the cross-correlation matrix between embeddings of two augmented views to be close to the identity matrix, simultaneously making features invariant and decorrelated."
tags: ["deep-learning", "self-supervised-learning", "contrastive-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFybG93IFR3aW5zIChaYm9udGFyIGV0IGFsLiAyMDIxKSB0YWtlcyBhIGZ1bmRhbWVudGFsbHkgZGlmZmVyZW50IGFwcHJvYWNoIHRvIHNlbGYtc3VwZXJ2aXNlZCBsZWFybmluZy4gUmF0aGVyIHRoYW4gdXNpbmcgYSBjb250cmFzdGl2ZSBsb3NzIG92ZXIgbmVnYXRpdmUgcGFpcnMgb3IgYW4gYXN5bW1ldHJpYyBwcmVkaWN0b3IsIGl0IGRpcmVjdGx5IHJlZ3VsYXJpc2VzIHRoZSBzdGF0aXN0aWNzIG9mIHRoZSByZXByZXNlbnRhdGlvbnMuIFRoZSBvYmplY3RpdmUgaXMgdG8gbWFrZSB0aGUgY3Jvc3MtY29ycmVsYXRpb24gbWF0cml4IEMgYmV0d2VlbiBlbWJlZGRpbmdzIG9mIHR3byBhdWdtZW50ZWQgdmlld3MgYXMgY2xvc2UgYXMgcG9zc2libGUgdG8gdGhlIGlkZW50aXR5IG1hdHJpeCDigJQgc2ltdWx0YW5lb3VzbHkgbWF4aW1pc2luZyBpbnZhcmlhbmNlIHRvIGF1Z21lbnRhdGlvbnMgYW5kIG1pbmltaXNpbmcgcmVkdW5kYW5jeSBiZXR3ZWVuIGVtYmVkZGluZyBkaW1lbnNpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlZHVuZGFuY3kgUmVkdWN0aW9uIFByaW5jaXBsZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG5hbWUgcmVmZXJlbmNlcyBIb3JhY2UgQmFybG93XHUwMDI3cyByZWR1bmRhbmN5LXJlZHVjdGlvbiBwcmluY2lwbGUgZnJvbSBuZXVyb3NjaWVuY2UgKDE5NjEpOiBhbiBlZmZpY2llbnQgbmV1cmFsIGNvZGUgc2hvdWxkIG1pbmltaXNlIHN0YXRpc3RpY2FsIGRlcGVuZGVuY2llcyBiZXR3ZWVuIG5ldXJvbnMuIEluIHRoZSBjb250ZXh0IG9mIHJlcHJlc2VudGF0aW9uIGxlYXJuaW5nLCB0aGlzIG1lYW5zIHRoZSBkaW1lbnNpb25zIG9mIHRoZSBlbWJlZGRpbmcgdmVjdG9yIHNob3VsZCBiZSBkZWNvcnJlbGF0ZWQuIElmIHR3byBkaW1lbnNpb25zIGFyZSBoaWdobHkgY29ycmVsYXRlZCwgdGhleSBjYXJyeSByZWR1bmRhbnQgaW5mb3JtYXRpb24g4oCUIHRoZSBuZXR3b3JrIGlzIHdhc3RpbmcgY2FwYWNpdHkuIEJhcmxvdyBUd2lucyBlbmZvcmNlcyBkZWNvcnJlbGF0aW9uIHRocm91Z2ggdGhlIG9mZi1kaWFnb25hbCB0ZXJtcyBvZiB0aGUgY3Jvc3MtY29ycmVsYXRpb24gbWF0cml4LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNyb3NzLUNvcnJlbGF0aW9uIE1hdHJpeCBhbmQgTG9zcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGEgYmF0Y2ggb2YgTiBpbWFnZXMgcHJvZHVjaW5nIG5vcm1hbGlzZWQgZW1iZWRkaW5ncyBaXkEsIFpeQiDiiIgg4oSdXntOw5dEfSAob25lIHBlciBhdWdtZW50ZWQgdmlldywgbm9ybWFsaXNlZCBhbG9uZyB0aGUgYmF0Y2ggZGltZW5zaW9uKSwgdGhlIGNyb3NzLWNvcnJlbGF0aW9uIG1hdHJpeCBpcyBDIOKIiCDihJ1ee0TDl0R9IHdpdGggQ+G1ouKxvCA9IM6j4oKZIHpeQV97bixpfSB6XkJfe24san0gLyBOLiBUaGUgbG9zcyBoYXMgdHdvIHRlcm1zOiBpbnZhcmlhbmNlIHRlcm0gzqPhtaIoMS1D4bWi4bWiKcKyIGZvcmNlcyBkaWFnb25hbCB0byAxIChlYWNoIGZlYXR1cmUgaW52YXJpYW50KTsgcmVkdW5kYW5jeSByZWR1Y3Rpb24gdGVybSDOu86j4bWizqPisbziiaDhtaIgQ+G1ouKxvMKyIGZvcmNlcyBvZmYtZGlhZ29uYWwgdG8gMCAoZmVhdHVyZXMgZGVjb3JyZWxhdGVkKS4gzrsgY29udHJvbHMgdGhlIHRyYWRlLW9mZiAozrs9MC4wMDUgaW4gdGhlIHBhcGVyKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBiYXJsb3dfdHdpbnNfbG9zcyh6X2EsIHpfYiwgbGFtYmRhX2NvZWZmPTAuMDA1KTpcbiAgICBcIlwiXCJCYXJsb3cgVHdpbnMgbG9zcy5cbiAgICB6X2EsIHpfYjogKE4sIEQpIGVtYmVkZGluZ3MgZnJvbSB0d28gYXVnbWVudGVkIHZpZXdzIChOT1QgeWV0IG5vcm1hbGlzZWQpLlxuICAgIGxhbWJkYV9jb2VmZjogd2VpZ2h0IGZvciByZWR1bmRhbmN5LXJlZHVjdGlvbiAob2ZmLWRpYWdvbmFsKSB0ZXJtLlxuICAgIFwiXCJcIlxuICAgIE4sIEQgPSB6X2Euc2l6ZSgpXG4gICAgIyBOb3JtYWxpc2UgYWxvbmcgYmF0Y2ggZGltZW5zaW9uIChub3QgZmVhdHVyZSBkaW1lbnNpb24pXG4gICAgel9hX25vcm0gPSAoel9hIC0gel9hLm1lYW4oMCkpIC8gKHpfYS5zdGQoMCkgKyAxZS02KSAgIyAoTiwgRClcbiAgICB6X2Jfbm9ybSA9ICh6X2IgLSB6X2IubWVhbigwKSkgLyAoel9iLnN0ZCgwKSArIDFlLTYpXG4gICAgIyBDcm9zcy1jb3JyZWxhdGlvbiBtYXRyaXg6IEMgPSBaX2FeVCBAIFpfYiAvIE4gIOKGkiAgKEQsIEQpXG4gICAgQyA9IHpfYV9ub3JtLlQgQCB6X2Jfbm9ybSAvIE5cbiAgICAjIEludmFyaWFuY2UgbG9zczogKGRpYWdvbmFsIOKGkiAxKVxuICAgIG9uX2RpYWcgID0gKDEgLSBDLmRpYWdvbmFsKCkpLnBvdygyKS5zdW0oKVxuICAgICMgUmVkdW5kYW5jeS1yZWR1Y3Rpb24gbG9zczogKG9mZi1kaWFnb25hbCDihpIgMClcbiAgICBvZmZfZGlhZyA9IG9mZl9kaWFnb25hbChDKS5wb3coMikuc3VtKClcbiAgICByZXR1cm4gb25fZGlhZyArIGxhbWJkYV9jb2VmZiAqIG9mZl9kaWFnXG5cbmRlZiBvZmZfZGlhZ29uYWwoQyk6XG4gICAgXCJcIlwiUmV0dXJuIGFsbCBvZmYtZGlhZ29uYWwgZWxlbWVudHMgb2YgYSBzcXVhcmUgbWF0cml4IGFzIGEgMUQgdGVuc29yLlwiXCJcIlxuICAgIG4gPSBDLnNpemUoMClcbiAgICByZXR1cm4gQy5mbGF0dGVuKClbOi0xXS52aWV3KG4tMSwgbisxKVs6LCAxOl0uZmxhdHRlbigpXG5cbiMgVGVzdFxudG9yY2gubWFudWFsX3NlZWQoMClcbnpfYSA9IHRvcmNoLnJhbmRuKDI1NiwgODE5MilcbnpfYiA9IHRvcmNoLnJhbmRuKDI1NiwgODE5Milcbmxvc3MgPSBiYXJsb3dfdHdpbnNfbG9zcyh6X2EsIHpfYilcbnByaW50KGZcdTAwMjdCYXJsb3cgVHdpbnMgbG9zcyAocmFuZG9tIGVtYmVkZGluZ3MsIEQ9ODE5Mik6IHtsb3NzLml0ZW0oKTouMmZ9XHUwMDI3KVxuIyBXaXRoIGlkZW50aWNhbCBlbWJlZGRpbmdzLCBkaWFnb25hbD0xIHNvIG9uX2RpYWc9MDsgb2ZmLWRpYWcgc3RpbGwgcGVuYWxpc2VkXG56X3NhbWUgPSB0b3JjaC5yYW5kbigyNTYsIDgxOTIpXG5sb3NzX3NhbWUgPSBiYXJsb3dfdHdpbnNfbG9zcyh6X3NhbWUsIHpfc2FtZSlcbnByaW50KGZcdTAwMjdCYXJsb3cgVHdpbnMgbG9zcyAoaWRlbnRpY2FsIHZpZXdzLCBEPTgxOTIpOiB7bG9zc19zYW1lLml0ZW0oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIExvb3AifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBCYXJsb3cgVHdpbnMgdHJhaW5pbmcgbG9vcCBpcyBzeW1tZXRyaWM6IGJvdGggdmlld3MgcGFzcyB0aHJvdWdoIHRoZSBzYW1lIGVuY29kZXIgYW5kIHByb2plY3RvciwgYW5kIHRoZSBsb3NzIGlzIGNvbXB1dGVkIG9uY2UgKG5vdCBzeW1tZXRyaXNlZCBvdmVyIGJvdGggb3JkZXJpbmdzLCBiZWNhdXNlIEMgYW5kIEPhtYAgYm90aCBhcHBlYXIgaW1wbGljaXRseSkuIE5vIHN0b3AtZ3JhZGllbnQgaXMgbmVlZGVkIOKAlCB0aGUgbG9zcyBncmFkaWVudCBuYXR1cmFsbHkgZmxvd3MgdGhyb3VnaCBib3RoIGJyYW5jaGVzLiBUaGUga2V5IGRlc2lnbiBjaG9pY2UgaXMgdGhlIGhpZ2gtZGltZW5zaW9uYWwgcHJvamVjdGlvbiBoZWFkOiBwcm9qZWN0aW5nIHRvIDgxOTIgZGltZW5zaW9ucyAodnMgMTI4IGluIFNpbUNMUikgaXMgYmVuZWZpY2lhbCBiZWNhdXNlIHRoZSBEw5dEIGNyb3NzLWNvcnJlbGF0aW9uIG1hdHJpeCBoYXMgbW9yZSBkZWdyZWVzIG9mIGZyZWVkb20gdG8gY2FwdHVyZSByZWR1bmRhbmN5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IHRvcmNodmlzaW9uLm1vZGVscyBhcyBtb2RlbHNcblxuY2xhc3MgQmFybG93VHdpbnMobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmFja2JvbmVfZm49bW9kZWxzLnJlc25ldDUwLCBwcm9qX2RpbT04MTkyLCBsYW1iZGFfY29lZmY9MC4wMDUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5sYW1iZGFfY29lZmYgPSBsYW1iZGFfY29lZmZcbiAgICAgICAgYmFzZSA9IGJhY2tib25lX2ZuKHdlaWdodHM9Tm9uZSlcbiAgICAgICAgZmVhdF9kaW0gPSBiYXNlLmZjLmluX2ZlYXR1cmVzICAjIDIwNDhcbiAgICAgICAgc2VsZi5lbmNvZGVyID0gbm4uU2VxdWVudGlhbCgqbGlzdChiYXNlLmNoaWxkcmVuKCkpWzotMV0pXG4gICAgICAgICMgUHJvamVjdG9yOiAzLWxheWVyIE1MUCB0byBoaWdoLWRpbWVuc2lvbmFsIHNwYWNlXG4gICAgICAgIHNlbGYucHJvamVjdG9yID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihmZWF0X2RpbSwgODE5MiwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTFkKDgxOTIpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoODE5MiwgODE5MiwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTFkKDgxOTIpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoODE5MiwgcHJval9kaW0sIGJpYXM9RmFsc2UpLFxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4MSwgeDIpOlxuICAgICAgICB6MSA9IHNlbGYucHJvamVjdG9yKHNlbGYuZW5jb2Rlcih4MSkuZmxhdHRlbigxKSkgICMgKE4sIDgxOTIpXG4gICAgICAgIHoyID0gc2VsZi5wcm9qZWN0b3Ioc2VsZi5lbmNvZGVyKHgyKS5mbGF0dGVuKDEpKVxuICAgICAgICBsb3NzID0gYmFybG93X3R3aW5zX2xvc3MoejEsIHoyLCBzZWxmLmxhbWJkYV9jb2VmZilcbiAgICAgICAgcmV0dXJuIGxvc3NcblxuIyBUcmFpbmluZyBzdGVwXG5kZWYgdHJhaW5fc3RlcChtb2RlbCwgYmF0Y2gsIG9wdGltaXplcik6XG4gICAgKHZpZXcxLCB2aWV3MiksIF8gPSBiYXRjaFxuICAgIHZpZXcxLCB2aWV3MiA9IHZpZXcxLmN1ZGEoKSwgdmlldzIuY3VkYSgpXG4gICAgbG9zcyA9IG1vZGVsKHZpZXcxLCB2aWV3MilcbiAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICBsb3NzLmJhY2t3YXJkKClcbiAgICBvcHRpbWl6ZXIuc3RlcCgpXG4gICAgcmV0dXJuIGxvc3MuaXRlbSgpXG5cbm1vZGVsID0gQmFybG93VHdpbnMoKVxucHJpbnQoXHUwMDI3QmFybG93VHdpbnMgcGFyYW1ldGVyczpcdTAwMjcsIHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKSAvLyAxXzAwMF8wMDAsIFx1MDAyN01cdTAwMjcpXG5wcmludChcdTAwMjdQcm9qZWN0b3Igb3V0cHV0IGRpbTogODE5MiDigJQgbXVjaCBsYXJnZXIgdGhhbiBTaW1DTFIgKDEyOClcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVmlzdWFsaXNpbmcgdGhlIENyb3NzLUNvcnJlbGF0aW9uIE1hdHJpeCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSB3ZWxsLXRyYWluZWQgQmFybG93IFR3aW5zIG1vZGVsIHNob3VsZCBwcm9kdWNlIGEgY3Jvc3MtY29ycmVsYXRpb24gbWF0cml4IHRoYXQgYXBwcm9hY2hlcyB0aGUgaWRlbnRpdHk6IGRpYWdvbmFsIGVudHJpZXMgbmVhciAxLjAgYW5kIG9mZi1kaWFnb25hbCBlbnRyaWVzIG5lYXIgMC4wLiBNb25pdG9yaW5nIHRoaXMgbWF0cml4IGR1cmluZyB0cmFpbmluZyBnaXZlcyBpbnNpZ2h0IGludG8gdGhlIHF1YWxpdHkgb2YgcmVwcmVzZW50YXRpb25zLiBJZiB0aGUgZGlhZ29uYWwgZW50cmllcyBhcmUgbG93LCB0aGUgaW52YXJpYW5jZSB0ZXJtIGlzIG5vdCBzYXRpc2ZpZWQg4oCUIHRoZSBlbmNvZGVyIGlzIG5vdCBwcm9kdWNpbmcgYXVnbWVudGF0aW9uLWludmFyaWFudCBmZWF0dXJlcy4gSWYgdGhlIG9mZi1kaWFnb25hbCBlbnRyaWVzIGFyZSBoaWdoLCB0aGUgcmVkdW5kYW5jeS1yZWR1Y3Rpb24gaXMgZmFpbGluZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGNvbXB1dGVfY3Jvc3NfY29ycmVsYXRpb24oel9hLCB6X2IpOlxuICAgIFwiXCJcIkNvbXB1dGUgY3Jvc3MtY29ycmVsYXRpb24gbWF0cml4IGJldHdlZW4gdHdvIGJhdGNoZXMgb2YgZW1iZWRkaW5ncy5cIlwiXCJcbiAgICBOID0gel9hLnNpemUoMClcbiAgICB6X2Ffbm9ybSA9ICh6X2EgLSB6X2EubWVhbigwKSkgLyAoel9hLnN0ZCgwKSArIDFlLTYpXG4gICAgel9iX25vcm0gPSAoel9iIC0gel9iLm1lYW4oMCkpIC8gKHpfYi5zdGQoMCkgKyAxZS02KVxuICAgIHJldHVybiAoel9hX25vcm0uVCBAIHpfYl9ub3JtIC8gTikuZGV0YWNoKCkuY3B1KClcblxuZGVmIGFuYWx5c2VfY2NfbWF0cml4KEMpOlxuICAgIFwiXCJcIlJlcG9ydCBzdGF0aXN0aWNzIG9mIGEgY3Jvc3MtY29ycmVsYXRpb24gbWF0cml4LlwiXCJcIlxuICAgIEQgPSBDLnNpemUoMClcbiAgICBkaWFnID0gQy5kaWFnb25hbCgpXG4gICAgbWFzayA9IH50b3JjaC5leWUoRCwgZHR5cGU9dG9yY2guYm9vbClcbiAgICBvZmYgID0gQ1ttYXNrXVxuICAgIHByaW50KGZcdTAwMjdEaWFnb25hbCAg4oCUIG1lYW46IHtkaWFnLm1lYW4oKTouNGZ9LCBzdGQ6IHtkaWFnLnN0ZCgpOi40Zn1cdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyN09mZi1kaWFnICDigJQgbWVhbjoge29mZi5tZWFuKCk6LjRmfSwgIHN0ZDoge29mZi5zdGQoKTouNGZ9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdGcm9iZW5pdXMgZGlzdGFuY2UgdG8gaWRlbnRpdHk6IHsoQyAtIHRvcmNoLmV5ZShEKSkubm9ybSgpOi40Zn1cdTAwMjcpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuRCA9IDY0XG4jIFNpbXVsYXRlIGFuIHVudHJhaW5lZCBtb2RlbCAocmFuZG9tIGVtYmVkZGluZ3MpXG5DX3JhbmRvbSA9IGNvbXB1dGVfY3Jvc3NfY29ycmVsYXRpb24odG9yY2gucmFuZG4oNTEyLCBEKSwgdG9yY2gucmFuZG4oNTEyLCBEKSlcbnByaW50KFx1MDAyNy0tLSBVbnRyYWluZWQgKHJhbmRvbSkgLS0tXHUwMDI3KVxuYW5hbHlzZV9jY19tYXRyaXgoQ19yYW5kb20pXG5cbiMgU2ltdWxhdGUgYSB3ZWxsLXRyYWluZWQgbW9kZWwgKHNhbWUgZW1iZWRkaW5ncywgZGVjb3JyZWxhdGVkKVxueiA9IHRvcmNoLmxpbmFsZy5xcih0b3JjaC5yYW5kbig1MTIsIEQpKVswXSAqICg1MTIgKiogMC41KSAgIyBvcnRob25vcm1hbCByb3dzXG5DX3RyYWluZWQgPSBjb21wdXRlX2Nyb3NzX2NvcnJlbGF0aW9uKHosIHogKyAwLjEgKiB0b3JjaC5yYW5kbl9saWtlKHopKVxucHJpbnQoXHUwMDI3LS0tIE5lYXItaWRlYWwgbW9kZWwgLS0tXHUwMDI3KVxuYW5hbHlzZV9jY19tYXRyaXgoQ190cmFpbmVkKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhpZ2gtRGltZW5zaW9uYWwgUHJvamVjdGlvbiBIZWFkIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHN1cnByaXNpbmcgZmluZGluZyBvZiBCYXJsb3cgVHdpbnMgaXMgdGhhdCBwcm9qZWN0aW5nIHRvIHZlcnkgaGlnaCBkaW1lbnNpb25zICg4MTkyIHZzIFNpbUNMUlx1MDAyN3MgMTI4KSBzaWduaWZpY2FudGx5IGltcHJvdmVzIHBlcmZvcm1hbmNlLiBUaGUgaW50dWl0aW9uIGlzIHRoYXQgdGhlIGNyb3NzLWNvcnJlbGF0aW9uIG1hdHJpeCBDIOKIiCDihJ1ee0TDl0R9IGdyb3dzIHF1YWRyYXRpY2FsbHkgd2l0aCBELCBwcm92aWRpbmcgRMKyIGNvbnN0cmFpbnRzIGZvciB0aGUgb3B0aW1pc2VyIHRvIHdvcmsgd2l0aC4gQXQgRCA9IDEyOCwgdGhlIG1hdHJpeCBoYXMgb25seSB+MTZLIGVudHJpZXM7IGF0IEQgPSA4MTkyLCB+NjdNIGVudHJpZXMsIHByb3ZpZGluZyBhIG11Y2ggcmljaGVyIHNpZ25hbC4gVGhpcyBpcyB1bmxpa2UgU2ltQ0xSIHdoZXJlIGhpZ2hlciBwcm9qZWN0aW9uIGRpbWVuc2lvbiB5aWVsZHMgZGltaW5pc2hpbmcgcmV0dXJucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGJ1aWxkX2Jhcmxvd19wcm9qZWN0b3IoaW5fZGltPTIwNDgsIGhpZGRlbl9kaW09ODE5Miwgb3V0X2RpbT04MTkyKTpcbiAgICBcIlwiXCJIaWdoLWRpbWVuc2lvbmFsIDMtbGF5ZXIgTUxQIHByb2plY3RvciBmb3IgQmFybG93IFR3aW5zLlwiXCJcIlxuICAgIHJldHVybiBubi5TZXF1ZW50aWFsKFxuICAgICAgICBubi5MaW5lYXIoaW5fZGltLCBoaWRkZW5fZGltLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgbm4uQmF0Y2hOb3JtMWQoaGlkZGVuX2RpbSksXG4gICAgICAgIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgbm4uTGluZWFyKGhpZGRlbl9kaW0sIGhpZGRlbl9kaW0sIGJpYXM9RmFsc2UpLFxuICAgICAgICBubi5CYXRjaE5vcm0xZChoaWRkZW5fZGltKSxcbiAgICAgICAgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICBubi5MaW5lYXIoaGlkZGVuX2RpbSwgb3V0X2RpbSwgYmlhcz1GYWxzZSksXG4gICAgICAgICMgTm8gQk4gb24gZmluYWwgbGF5ZXIg4oCUIHJhdyBvdXRwdXRzIGZvciBjcm9zcy1jb3JyZWxhdGlvbiBub3JtYWxpc2F0aW9uXG4gICAgKVxuXG4jIENvbXBhcmUgcGFyYW1ldGVyIGNvdW50cyBhY3Jvc3MgcHJvamVjdGlvbiBkaW1lbnNpb25zXG5mb3IgZGltIGluIFsxMjgsIDUxMiwgMjA0OCwgODE5Ml06XG4gICAgcHJvaiA9IGJ1aWxkX2Jhcmxvd19wcm9qZWN0b3Iob3V0X2RpbT1kaW0pXG4gICAgcGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBwcm9qLnBhcmFtZXRlcnMoKSkgLy8gMTAwMFxuICAgIG5fbWF0cml4X2VudHJpZXMgPSBkaW0gKiBkaW1cbiAgICBwcmludChmXHUwMDI3ICBEPXtkaW06NWR9OiBwcm9qX3BhcmFtcz17cGFyYW1zOjZkfUssICBcdTAwMjdcbiAgICAgICAgICBmXHUwMDI3Q0MgbWF0cml4IGVudHJpZXM9e25fbWF0cml4X2VudHJpZXM6OWR9LCAgXHUwMDI3XG4gICAgICAgICAgZlx1MDAyN29mZi1kaWFnb25hbCBjb25zdHJhaW50cz17bl9tYXRyaXhfZW50cmllcyAtIGRpbTo5ZH1cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiLOuyBDb250cm9scyBJbnZhcmlhbmNlIHZzIFJlZHVuZGFuY3kgVHJhZGUtb2ZmIiwiY29udGVudCI6IlRoZSDOuyBjb2VmZmljaWVudCAoZGVmYXVsdCAwLjAwNSkgd2VpZ2h0cyB0aGUgb2ZmLWRpYWdvbmFsIHJlZHVuZGFuY3kgdGVybSByZWxhdGl2ZSB0byB0aGUgZGlhZ29uYWwgaW52YXJpYW5jZSB0ZXJtLiBBIHNtYWxsIM67IGVtcGhhc2lzZXMgaW52YXJpYW5jZSAoZGlhZ29uYWwg4oaSIDEpIGJ1dCBhbGxvd3MgY29ycmVsYXRlZCBkaW1lbnNpb25zLiBBIGxhcmdlIM67IGFnZ3Jlc3NpdmVseSBkZWNvcnJlbGF0ZXMgZmVhdHVyZXMgYnV0IG1heSBzYWNyaWZpY2UgaW52YXJpYW5jZS4gSW4gcHJhY3RpY2UsIM67IGlzIHNlbnNpdGl2ZSB0byB0aGUgcHJvamVjdGlvbiBkaW1lbnNpb25hbGl0eTogbGFyZ2VyIEQgb2Z0ZW4gbmVlZHMgc21hbGxlciDOuyBzaW5jZSB0aGUgb2ZmLWRpYWdvbmFsIHN1bSBncm93cyBhcyBPKETCsikgd2hpbGUgdGhlIGRpYWdvbmFsIHN1bSBncm93cyBhcyBPKEQpLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbm5lY3Rpb24gdG8gSW5mb3JtYXRpb24gVGhlb3J5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXJsb3cgVHdpbnMgaGFzIGEgZGlyZWN0IGNvbm5lY3Rpb24gdG8gaW5mb3JtYXRpb24tdGhlb3JldGljIHByaW5jaXBsZXMuIE1heGltaXNpbmcgdGhlIGRpYWdvbmFsIG9mIEMgKGludmFyaWFuY2UpIG1heGltaXNlcyBtdXR1YWwgaW5mb3JtYXRpb24gYmV0d2VlbiB0aGUgdHdvIHZpZXdzIOKAlCB0aGUgcmVwcmVzZW50YXRpb25zIHNob3VsZCBjYXJyeSB0aGUgc2FtZSBjb250ZW50IGRlc3BpdGUgZGlmZmVyZW50IGF1Z21lbnRhdGlvbnMuIE1pbmltaXNpbmcgdGhlIG9mZi1kaWFnb25hbCAocmVkdW5kYW5jeSByZWR1Y3Rpb24pIGltcGxlbWVudHMgYSB3aGl0ZW5pbmctbGlrZSBvYmplY3RpdmUgdGhhdCBzcHJlYWRzIGluZm9ybWF0aW9uIGV2ZW5seSBhY3Jvc3MgZGltZW5zaW9ucy4gVG9nZXRoZXIsIHRoZXNlIG9iamVjdGl2ZXMgcmVzZW1ibGUgbWF4aW1pc2luZyB0aGUgam9pbnQgZW50cm9weSBvZiB0aGUgZW1iZWRkaW5nIHdoaWxlIGNvbnN0cmFpbmluZyBtdXR1YWwgaW5mb3JtYXRpb24gYmV0d2VlbiBkaW1lbnNpb25zLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQmFybG93XHUwMDI3cyByZWR1bmRhbmN5LXJlZHVjdGlvbjogZWZmaWNpZW50IG5ldXJhbCBjb2RlcyBkZWNvcnJlbGF0ZSBvdXRwdXRzIChuZXVyb3NjaWVuY2UsIDE5NjEpLiIsIs67PTAuMDA1IHdvcmtzIGFjcm9zcyBzY2FsZXM7IHR1bmUgaWYgRCBjaGFuZ2VzIHNpZ25pZmljYW50bHkgZnJvbSA4MTkyLiIsIlRyYWluaW5nOiBMQVJTIG9wdGltaXNlciwgYmF0Y2ggMjA0OCwgbHI9MC4yLCB3ZWlnaHRfZGVjYXk9MS41ZS02LCAxMDAwIGVwb2Nocy4iLCJQcm9qZWN0aW9uIG5vcm1hbGlzZWQgYWxvbmcgYmF0Y2ggZGltIChub3QgZmVhdHVyZSBkaW0pIOKAlCB1bmxpa2UgU2ltQ0xSXHUwMDI3cyBMMiBub3JtYWxpc2F0aW9uLiIsIk5vIHN0b3AtZ3JhZGllbnQgbmVlZGVkOiB0aGUgY3Jvc3MtY29ycmVsYXRpb24gbG9zcyBuYXR1cmFsbHkgcHJldmVudHMgY29sbGFwc2UuIl19LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJMb3NzIE1lY2hhbmlzbSIsIk5lZ2F0aXZlcyIsIlByb2ogRGltIiwiTGluZWFyIEV2YWwgVG9wLTEiLCJLZXkgSW5ub3ZhdGlvbiJdLCJyb3dzIjpbWyJCYXJsb3cgVHdpbnMiLCJDcm9zcy1jb3JyIOKGkiBpZGVudGl0eSIsIk5vIiwiODE5MiIsIjczLjIlIiwiUmVkdW5kYW5jeSByZWR1Y3Rpb24gdmlhIG9mZi1kaWFnb25hbCBwZW5hbHR5Il0sWyJWSUNSZWciLCJWYXIgKyBJbnYgKyBDb3YiLCJObyIsIjgxOTIiLCI3My4yJSIsIkV4cGxpY2l0IHZhcmlhbmNlIHRlcm0gcHJldmVudHMgY29sbGFwc2UiXSxbIlNpbUNMUiB2MSIsIk5ULVhlbnQgY29udHJhc3RpdmUiLCJZZXMiLCIxMjgiLCI2OS4zJSIsIkxhcmdlIGJhdGNoIGluLWJhdGNoIG5lZ2F0aXZlcyJdLFsiQllPTCIsIk1TRSAobm9ybWFsaXNlZCkiLCJObyIsIjI1NiIsIjc0LjMlIiwiRU1BIHRhcmdldCArIHByZWRpY3RvciBhc3ltbWV0cnkiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBDb25zaWRlcmF0aW9ucyBhbmQgVHVuaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXJsb3cgVHdpbnMgaXMgc3RyYWlnaHRmb3J3YXJkIHRvIGltcGxlbWVudCBidXQgaGFzIGEgZmV3IHByYWN0aWNhbCBwaXRmYWxscy4gVGhlIGNyb3NzLWNvcnJlbGF0aW9uIG1hdHJpeCBjb21wdXRhdGlvbiBzY2FsZXMgYXMgTyhOwrdEwrIpIGluIG1lbW9yeSBmb3IgYSBELWRpbWVuc2lvbmFsIGVtYmVkZGluZyDigJQgYXQgRD04MTkyIGFuZCBOPTIwNDgsIHRoZSBtYXRyaXggaXRzZWxmIGlzIDgxOTLDlzgxOTIgPSA2N00gZmxvYXQzMiB2YWx1ZXMgKH4yNTYgTUIpLiBUaGlzIGlzIG1hbmFnZWFibGUgb24gYSBzaW5nbGUgR1BVIGJ1dCByZXF1aXJlcyBjYXJlLiBUaGUgb2ZmX2RpYWdvbmFsIGhlbHBlciBmdW5jdGlvbiBtdXN0IGNvcnJlY3RseSBleGNsdWRlIHRoZSBEIGRpYWdvbmFsIGVsZW1lbnRzLiBCYXRjaCBub3JtYWxpc2F0aW9uIGluIHRoZSBwcm9qZWN0b3IgKGJ1dCBub3Qgb24gdGhlIGZpbmFsIG91dHB1dCBsYXllcikgaXMgaW1wb3J0YW50IGZvciB0cmFpbmluZyBzdGFiaWxpdHk7IG9taXR0aW5nIGl0IGNhdXNlcyB0aGUgY3Jvc3MtY29ycmVsYXRpb24gbWF0cml4IHRvIGJlIGlsbC1jb25kaXRpb25lZC4ifV0="
---
# Barlow Twins — Cross-Correlation Matrix and Redundancy Reduction

Barlow Twins (Zbontar et al. 2021) takes a fundamentally different approach to self-supervised learning. Rather than using a contrastive loss over negative pairs or an asymmetric predictor, it directly regularises the statistics of the representations. The objective is to make the cross-correlation matrix C between embeddings of two augmented views as close as possible to the identity matrix — simultaneously maximising invariance to augmentations and minimising redundancy between embedding dimensions.

## Redundancy Reduction Principle

The name references Horace Barlow's redundancy-reduction principle from neuroscience (1961): an efficient neural code should minimise statistical dependencies between neurons. In the context of representation learning, this means the dimensions of the embedding vector should be decorrelated. If two dimensions are highly correlated, they carry redundant information — the network is wasting capacity. Barlow Twins enforces decorrelation through the off-diagonal terms of the cross-correlation matrix.

## Cross-Correlation Matrix and Loss

For a batch of N images producing normalised embeddings Z^A, Z^B ∈ ℝ^{N×D} (one per augmented view, normalised along the batch dimension), the cross-correlation matrix is C ∈ ℝ^{D×D} with Cᵢⱼ = Σₙ z^A_{n,i} z^B_{n,j} / N. The loss has two terms: invariance term Σᵢ(1-Cᵢᵢ)² forces diagonal to 1 (each feature invariant); redundancy reduction term λΣᵢΣⱼ≠ᵢ Cᵢⱼ² forces off-diagonal to 0 (features decorrelated). λ controls the trade-off (λ=0.005 in the paper).

```python
import torch
import torch.nn.functional as F

def barlow_twins_loss(z_a, z_b, lambda_coeff=0.005):
    """Barlow Twins loss.
    z_a, z_b: (N, D) embeddings from two augmented views (NOT yet normalised).
    lambda_coeff: weight for redundancy-reduction (off-diagonal) term.
    """
    N, D = z_a.size()
    # Normalise along batch dimension (not feature dimension)
    z_a_norm = (z_a - z_a.mean(0)) / (z_a.std(0) + 1e-6)  # (N, D)
    z_b_norm = (z_b - z_b.mean(0)) / (z_b.std(0) + 1e-6)
    # Cross-correlation matrix: C = Z_a^T @ Z_b / N  →  (D, D)
    C = z_a_norm.T @ z_b_norm / N
    # Invariance loss: (diagonal → 1)
    on_diag  = (1 - C.diagonal()).pow(2).sum()
    # Redundancy-reduction loss: (off-diagonal → 0)
    off_diag = off_diagonal(C).pow(2).sum()
    return on_diag + lambda_coeff * off_diag

def off_diagonal(C):
    """Return all off-diagonal elements of a square matrix as a 1D tensor."""
    n = C.size(0)
    return C.flatten()[:-1].view(n-1, n+1)[:, 1:].flatten()

# Test
torch.manual_seed(0)
z_a = torch.randn(256, 8192)
z_b = torch.randn(256, 8192)
loss = barlow_twins_loss(z_a, z_b)
print(f'Barlow Twins loss (random embeddings, D=8192): {loss.item():.2f}')
# With identical embeddings, diagonal=1 so on_diag=0; off-diag still penalised
z_same = torch.randn(256, 8192)
loss_same = barlow_twins_loss(z_same, z_same)
print(f'Barlow Twins loss (identical views, D=8192): {loss_same.item():.4f}')
```

## Training Loop

The Barlow Twins training loop is symmetric: both views pass through the same encoder and projector, and the loss is computed once (not symmetrised over both orderings, because C and Cᵀ both appear implicitly). No stop-gradient is needed — the loss gradient naturally flows through both branches. The key design choice is the high-dimensional projection head: projecting to 8192 dimensions (vs 128 in SimCLR) is beneficial because the D×D cross-correlation matrix has more degrees of freedom to capture redundancy.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

class BarlowTwins(nn.Module):
    def __init__(self, backbone_fn=models.resnet50, proj_dim=8192, lambda_coeff=0.005):
        super().__init__()
        self.lambda_coeff = lambda_coeff
        base = backbone_fn(weights=None)
        feat_dim = base.fc.in_features  # 2048
        self.encoder = nn.Sequential(*list(base.children())[:-1])
        # Projector: 3-layer MLP to high-dimensional space
        self.projector = nn.Sequential(
            nn.Linear(feat_dim, 8192, bias=False), nn.BatchNorm1d(8192), nn.ReLU(),
            nn.Linear(8192, 8192, bias=False), nn.BatchNorm1d(8192), nn.ReLU(),
            nn.Linear(8192, proj_dim, bias=False),
        )

    def forward(self, x1, x2):
        z1 = self.projector(self.encoder(x1).flatten(1))  # (N, 8192)
        z2 = self.projector(self.encoder(x2).flatten(1))
        loss = barlow_twins_loss(z1, z2, self.lambda_coeff)
        return loss

# Training step
def train_step(model, batch, optimizer):
    (view1, view2), _ = batch
    view1, view2 = view1.cuda(), view2.cuda()
    loss = model(view1, view2)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss.item()

model = BarlowTwins()
print('BarlowTwins parameters:', sum(p.numel() for p in model.parameters()) // 1_000_000, 'M')
print('Projector output dim: 8192 — much larger than SimCLR (128)')
```

## Visualising the Cross-Correlation Matrix

A well-trained Barlow Twins model should produce a cross-correlation matrix that approaches the identity: diagonal entries near 1.0 and off-diagonal entries near 0.0. Monitoring this matrix during training gives insight into the quality of representations. If the diagonal entries are low, the invariance term is not satisfied — the encoder is not producing augmentation-invariant features. If the off-diagonal entries are high, the redundancy-reduction is failing.

```python
import torch
import torch.nn.functional as F
import numpy as np

def compute_cross_correlation(z_a, z_b):
    """Compute cross-correlation matrix between two batches of embeddings."""
    N = z_a.size(0)
    z_a_norm = (z_a - z_a.mean(0)) / (z_a.std(0) + 1e-6)
    z_b_norm = (z_b - z_b.mean(0)) / (z_b.std(0) + 1e-6)
    return (z_a_norm.T @ z_b_norm / N).detach().cpu()

def analyse_cc_matrix(C):
    """Report statistics of a cross-correlation matrix."""
    D = C.size(0)
    diag = C.diagonal()
    mask = ~torch.eye(D, dtype=torch.bool)
    off  = C[mask]
    print(f'Diagonal  — mean: {diag.mean():.4f}, std: {diag.std():.4f}')
    print(f'Off-diag  — mean: {off.mean():.4f},  std: {off.std():.4f}')
    print(f'Frobenius distance to identity: {(C - torch.eye(D)).norm():.4f}')

torch.manual_seed(42)
D = 64
# Simulate an untrained model (random embeddings)
C_random = compute_cross_correlation(torch.randn(512, D), torch.randn(512, D))
print('--- Untrained (random) ---')
analyse_cc_matrix(C_random)

# Simulate a well-trained model (same embeddings, decorrelated)
z = torch.linalg.qr(torch.randn(512, D))[0] * (512 ** 0.5)  # orthonormal rows
C_trained = compute_cross_correlation(z, z + 0.1 * torch.randn_like(z))
print('--- Near-ideal model ---')
analyse_cc_matrix(C_trained)
```

## High-Dimensional Projection Head

A surprising finding of Barlow Twins is that projecting to very high dimensions (8192 vs SimCLR's 128) significantly improves performance. The intuition is that the cross-correlation matrix C ∈ ℝ^{D×D} grows quadratically with D, providing D² constraints for the optimiser to work with. At D = 128, the matrix has only ~16K entries; at D = 8192, ~67M entries, providing a much richer signal. This is unlike SimCLR where higher projection dimension yields diminishing returns.

```python
import torch
import torch.nn as nn

def build_barlow_projector(in_dim=2048, hidden_dim=8192, out_dim=8192):
    """High-dimensional 3-layer MLP projector for Barlow Twins."""
    return nn.Sequential(
        nn.Linear(in_dim, hidden_dim, bias=False),
        nn.BatchNorm1d(hidden_dim),
        nn.ReLU(inplace=True),
        nn.Linear(hidden_dim, hidden_dim, bias=False),
        nn.BatchNorm1d(hidden_dim),
        nn.ReLU(inplace=True),
        nn.Linear(hidden_dim, out_dim, bias=False),
        # No BN on final layer — raw outputs for cross-correlation normalisation
    )

# Compare parameter counts across projection dimensions
for dim in [128, 512, 2048, 8192]:
    proj = build_barlow_projector(out_dim=dim)
    params = sum(p.numel() for p in proj.parameters()) // 1000
    n_matrix_entries = dim * dim
    print(f'  D={dim:5d}: proj_params={params:6d}K,  '
          f'CC matrix entries={n_matrix_entries:9d},  '
          f'off-diagonal constraints={n_matrix_entries - dim:9d}')
```

> **λ Controls Invariance vs Redundancy Trade-off**: The λ coefficient (default 0.005) weights the off-diagonal redundancy term relative to the diagonal invariance term. A small λ emphasises invariance (diagonal → 1) but allows correlated dimensions. A large λ aggressively decorrelates features but may sacrifice invariance. In practice, λ is sensitive to the projection dimensionality: larger D often needs smaller λ since the off-diagonal sum grows as O(D²) while the diagonal sum grows as O(D).

## Connection to Information Theory

Barlow Twins has a direct connection to information-theoretic principles. Maximising the diagonal of C (invariance) maximises mutual information between the two views — the representations should carry the same content despite different augmentations. Minimising the off-diagonal (redundancy reduction) implements a whitening-like objective that spreads information evenly across dimensions. Together, these objectives resemble maximising the joint entropy of the embedding while constraining mutual information between dimensions.

- Barlow's redundancy-reduction: efficient neural codes decorrelate outputs (neuroscience, 1961).
- λ=0.005 works across scales; tune if D changes significantly from 8192.
- Training: LARS optimiser, batch 2048, lr=0.2, weight_decay=1.5e-6, 1000 epochs.
- Projection normalised along batch dim (not feature dim) — unlike SimCLR's L2 normalisation.
- No stop-gradient needed: the cross-correlation loss naturally prevents collapse.

| Method | Loss Mechanism | Negatives | Proj Dim | Linear Eval Top-1 | Key Innovation |
| --- | --- | --- | --- | --- | --- |
| Barlow Twins | Cross-corr → identity | No | 8192 | 73.2% | Redundancy reduction via off-diagonal penalty |
| VICReg | Var + Inv + Cov | No | 8192 | 73.2% | Explicit variance term prevents collapse |
| SimCLR v1 | NT-Xent contrastive | Yes | 128 | 69.3% | Large batch in-batch negatives |
| BYOL | MSE (normalised) | No | 256 | 74.3% | EMA target + predictor asymmetry |

## Practical Considerations and Tuning

Barlow Twins is straightforward to implement but has a few practical pitfalls. The cross-correlation matrix computation scales as O(N·D²) in memory for a D-dimensional embedding — at D=8192 and N=2048, the matrix itself is 8192×8192 = 67M float32 values (~256 MB). This is manageable on a single GPU but requires care. The off_diagonal helper function must correctly exclude the D diagonal elements. Batch normalisation in the projector (but not on the final output layer) is important for training stability; omitting it causes the cross-correlation matrix to be ill-conditioned.

