---
title: "VICReg — Variance, Invariance, Covariance Regularization"
slug: "vicreg"
description: "VICReg (Bardes et al. 2022) extends Barlow Twins with an explicit variance hinge loss that directly prevents representational collapse, and separates the three objectives — variance, invariance, and covariance — into independently controllable terms."
tags: ["deep-learning", "self-supervised-learning", "contrastive-learning"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVklDUmVnIChWYXJpYW5jZS1JbnZhcmlhbmNlLUNvdmFyaWFuY2UgUmVndWxhcml6YXRpb24sIEJhcmRlcyBldCBhbC4gMjAyMikgbWFrZXMgdGhlIGNvbm5lY3Rpb24gYmV0d2VlbiBCYXJsb3cgVHdpbnMgYW5kIGNvbGxhcHNlIHByZXZlbnRpb24gbW9yZSBleHBsaWNpdC4gV2hpbGUgQmFybG93IFR3aW5zIGltcGxpY2l0bHkgcHJldmVudHMgY29sbGFwc2UgdmlhIHRoZSBkaWFnb25hbCBpbnZhcmlhbmNlIHRlcm0sIFZJQ1JlZyBpbnRyb2R1Y2VzIGEgZGVkaWNhdGVkIHZhcmlhbmNlIGhpbmdlIGxvc3MgdGhhdCBkaXJlY3RseSBwZW5hbGlzZXMgbG93IHZhcmlhbmNlIGluIGFueSBlbWJlZGRpbmcgZGltZW5zaW9uLiBUaGlzIGNsZWFuZXIgZGVjb21wb3NpdGlvbiBtYWtlcyB0aGUgbWV0aG9kIG1vcmUgaW50ZXJwcmV0YWJsZSBhbmQgZWFzaWVyIHRvIHR1bmUsIHdoaWxlIGFjaGlldmluZyB0aGUgc2FtZSBsZXZlbCBvZiBwZXJmb3JtYW5jZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaHJlZS1UZXJtIExvc3MgRnVuY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZJQ1JlZyBkZWNvbXBvc2VzIHRoZSBvYmplY3RpdmUgaW50byB0aHJlZSBpbmRlcGVuZGVudGx5IHdlaWdodGVkIHRlcm1zOiAoMSkgSW52YXJpYW5jZSBzKFosIFpcdTAwMjcpID0gKDEvTinOo+G1ouKAlnrhtaIgLSB6XHUwMDI34bWi4oCWwrIg4oCUIE1TRSBiZXR3ZWVuIGVtYmVkZGluZ3Mgb2YgdGhlIHR3byB2aWV3cyAocHVzaCByZXByZXNlbnRhdGlvbnMgdG9nZXRoZXIpOyAoMikgVmFyaWFuY2UgdihaKSA9IM6j4rG8IG1heCgwLCDOsyAtIFN0ZCh64rG8KSkg4oCUIGhpbmdlIGxvc3MgbWFpbnRhaW5pbmcgcGVyLWRpbWVuc2lvbiBzdGFuZGFyZCBkZXZpYXRpb24g4omlIM6zPTEgKHByZXZlbnQgY29sbGFwc2UpOyAoMykgQ292YXJpYW5jZSBjKFopID0gzqPhtaLiiaDisbwgW0NvdihaKV3CsuG1ouKxvCAvIChkLTEpIOKAlCBzdW0gb2Ygc3F1YXJlZCBvZmYtZGlhZ29uYWwgY292YXJpYW5jZSBlbnRyaWVzIChkZWNvcnJlbGF0ZSBkaW1lbnNpb25zKS4gVG90YWwgbG9zczogzrtzICsgzrxbdihaKSt2KFpcdTAwMjcpXSArIM69W2MoWikrYyhaXHUwMDI3KV0uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgdmljcmVnX2xvc3MoejEsIHoyLCBsYW1iZGFfPTI1LjAsIG11PTI1LjAsIG51PTEuMCwgZ2FtbWE9MS4wKTpcbiAgICBcIlwiXCJWSUNSZWcgbG9zcyB3aXRoIHRocmVlIHRlcm1zOiB2YXJpYW5jZSwgaW52YXJpYW5jZSwgY292YXJpYW5jZS5cbiAgICB6MSwgejI6IChOLCBEKSByYXcgZW1iZWRkaW5ncyAobm90IEwyLW5vcm1hbGlzZWQsIG5vdCBiYXRjaC1ub3JtYWxpc2VkKS5cbiAgICBsYW1iZGFfOiB3ZWlnaHQgZm9yIGludmFyaWFuY2UgdGVybS5cbiAgICBtdTogICAgICB3ZWlnaHQgZm9yIHZhcmlhbmNlIHRlcm0gKGFwcGxpZWQgdG8gYm90aCB6MSBhbmQgejIpLlxuICAgIG51OiAgICAgIHdlaWdodCBmb3IgY292YXJpYW5jZSB0ZXJtIChhcHBsaWVkIHRvIGJvdGggejEgYW5kIHoyKS5cbiAgICBnYW1tYTogICB0YXJnZXQgc3RhbmRhcmQgZGV2aWF0aW9uIGZvciB2YXJpYW5jZSBoaW5nZS5cbiAgICBcIlwiXCJcbiAgICBOLCBEID0gejEuc2l6ZSgpXG4gICAgIyAxLiBJbnZhcmlhbmNlOiBNU0UgYmV0d2VlbiBlbWJlZGRpbmdzIG9mIHR3byB2aWV3c1xuICAgIGludl9sb3NzID0gRi5tc2VfbG9zcyh6MSwgejIpXG4gICAgIyAyLiBWYXJpYW5jZTogaGluZ2UgbG9zcyAoZWFjaCBkaW1lbnNpb24gc3RkIFx1MDAzZT0gZ2FtbWEpXG4gICAgdmFyX2xvc3MgPSB2YXJpYW5jZV9sb3NzKHoxLCBnYW1tYSkgKyB2YXJpYW5jZV9sb3NzKHoyLCBnYW1tYSlcbiAgICAjIDMuIENvdmFyaWFuY2U6IG9mZi1kaWFnb25hbCBjb3ZhcmlhbmNlIC1cdTAwM2UgMFxuICAgIGNvdl9sb3NzID0gY292YXJpYW5jZV9sb3NzKHoxKSArIGNvdmFyaWFuY2VfbG9zcyh6MilcbiAgICBsb3NzID0gbGFtYmRhXyAqIGludl9sb3NzICsgbXUgKiB2YXJfbG9zcyArIG51ICogY292X2xvc3NcbiAgICByZXR1cm4gbG9zcywgaW52X2xvc3MuaXRlbSgpLCB2YXJfbG9zcy5pdGVtKCksIGNvdl9sb3NzLml0ZW0oKVxuXG4jIFF1aWNrIHRlc3RcbnRvcmNoLm1hbnVhbF9zZWVkKDApXG56MSA9IHRvcmNoLnJhbmRuKDI1NiwgMjA0OClcbnoyID0gejEgKyAwLjEgKiB0b3JjaC5yYW5kbl9saWtlKHoxKSAgIyBzbGlnaHQgYXVnbWVudGF0aW9uXG50b3RhbCwgaW52LCB2YXIsIGNvdiA9IHZpY3JlZ19sb3NzKHoxLCB6MilcbnByaW50KGZcdTAwMjdUb3RhbCBsb3NzOiB7dG90YWw6LjJmfVx1MDAyNylcbnByaW50KGZcdTAwMjcgIEludmFyaWFuY2U6IHtpbnY6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjcgIFZhcmlhbmNlOiAgIHt2YXI6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjcgIENvdmFyaWFuY2U6IHtjb3Y6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWYXJpYW5jZSBUZXJtIOKAlCBQcmV2ZW50aW5nIENvbGxhcHNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdmFyaWFuY2UgdGVybSBpcyBhIGhpbmdlIGxvc3MgdGhhdCBwZW5hbGlzZXMgYW55IGVtYmVkZGluZyBkaW1lbnNpb24gd2hvc2Ugc3RhbmRhcmQgZGV2aWF0aW9uIGFjcm9zcyB0aGUgYmF0Y2ggZmFsbHMgYmVsb3cgzrMgPSAxOiB2KFopID0gzqPisbwgbWF4KDAsIM6zIC0g4oiaKFZhcih64rG8KSArIM61KSkuIElmIGFsbCBzYW1wbGVzIGNvbGxhcHNlIHRvIHRoZSBzYW1lIHZlY3RvciwgZXZlcnkgZGltZW5zaW9uXHUwMDI3cyBzdGQg4oaSIDAsIGFuZCB0aGlzIHRlcm0gYmVjb21lcyBodWdlLiBDcnVjaWFsbHksIHRoZSB2YXJpYW5jZSBpcyBjb21wdXRlZCBwZXItZGltZW5zaW9uIGluZGVwZW5kZW50bHkg4oCUIGEgZGltZW5zaW9uIHdpdGggc3RkIOKJpSDOsyBjb250cmlidXRlcyB6ZXJvIHBlbmFsdHkuIFRoaXMgaXMgbW9yZSBkaXJlY3QgdGhhbiBCYXJsb3cgVHdpbnNcdTAwMjcgaW1wbGljaXQgdmFyaWFuY2UgY29udHJvbCB2aWEgdGhlIGRpYWdvbmFsIG9mIHRoZSBjcm9zcy1jb3JyZWxhdGlvbiBtYXRyaXguIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgdmFyaWFuY2VfbG9zcyh6LCBnYW1tYT0xLjAsIGVwcz0xZS00KTpcbiAgICBcIlwiXCJWYXJpYW5jZSBoaW5nZSBsb3NzOiBwZW5hbGlzZSBkaW1lbnNpb25zIHdoZXJlIHN0ZCBcdTAwM2MgZ2FtbWEuXG4gICAgejogKE4sIEQpIGVtYmVkZGluZyBiYXRjaC5cbiAgICBSZXR1cm5zIHNjYWxhciDigJQgc3VtIG9mIGhpbmdlIGxvc3NlcyBhY3Jvc3MgRCBkaW1lbnNpb25zLlxuICAgIFwiXCJcIlxuICAgICMgc3RkIGFsb25nIGJhdGNoIGRpbWVuc2lvbiBmb3IgZWFjaCBmZWF0dXJlXG4gICAgc3RkID0gdG9yY2guc3FydCh6LnZhcihkaW09MCkgKyBlcHMpICAgICAgICMgKEQsKVxuICAgIGhpbmdlID0gRi5yZWx1KGdhbW1hIC0gc3RkKSAgICAgICAgICAgICAgICAgIyAwIGlmIHN0ZCBcdTAwM2U9IGdhbW1hLCBlbHNlIGdhbW1hIC0gc3RkXG4gICAgcmV0dXJuIGhpbmdlLm1lYW4oKSAgIyBwYXBlciB1c2VzIG1lYW4gb3ZlciBEXG5cbiMgRGVtb25zdHJhdGU6IGNvbGxhcHNlIOKGkiBsYXJnZSB2YXJpYW5jZSBsb3NzOyBzcHJlYWQg4oaSIG5lYXItemVyb1xudG9yY2gubWFudWFsX3NlZWQoMSlcbk4sIEQgPSAyNTYsIDEyOFxuXG4jIENvbGxhcHNlZDogYWxsIG91dHB1dHMgY29uc3RhbnRcbnpfY29sbGFwc2VkID0gdG9yY2gub25lcyhOLCBEKVxudl9jb2xsYXBzZWQgPSB2YXJpYW5jZV9sb3NzKHpfY29sbGFwc2VkKVxucHJpbnQoZlx1MDAyN1ZhcmlhbmNlIGxvc3MgKGNvbGxhcHNlZCwgYWxsLW9uZXMpOiB7dl9jb2xsYXBzZWQuaXRlbSgpOi40Zn0gIChleHBlY3RlZCB+MS4wKVx1MDAyNylcblxuIyBTcHJlYWQ6IHJhbmRvbSBub3JtYWwgaGFzIHN0ZCDiiYggMVxuel9zcHJlYWQgPSB0b3JjaC5yYW5kbihOLCBEKVxudl9zcHJlYWQgPSB2YXJpYW5jZV9sb3NzKHpfc3ByZWFkKVxucHJpbnQoZlx1MDAyN1ZhcmlhbmNlIGxvc3MgKHNwcmVhZCwgTigwLDEpKTogICAgICB7dl9zcHJlYWQuaXRlbSgpOi42Zn0gIChleHBlY3RlZCB+MC4wKVx1MDAyNylcblxuIyBQYXJ0aWFsIGNvbGxhcHNlOiBzb21lIGRpbXMgY29sbGFwc2VkXG56X3BhcnRpYWwgPSB0b3JjaC5yYW5kbihOLCBEKVxuel9wYXJ0aWFsWzosIDozMl0gPSB6X3BhcnRpYWxbOiwgOjMyXS5tZWFuKDAsIGtlZXBkaW09VHJ1ZSkuZXhwYW5kKE4sIC0xKSAgIyAzMiBkaW1zIGNvbGxhcHNlZFxudl9wYXJ0aWFsID0gdmFyaWFuY2VfbG9zcyh6X3BhcnRpYWwpXG5wcmludChmXHUwMDI3VmFyaWFuY2UgbG9zcyAoMzIve0R9IGRpbXMgY29sbGFwc2VkKToge3ZfcGFydGlhbC5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb3ZhcmlhbmNlIFJlZ3VsYXJpemF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY292YXJpYW5jZSB0ZXJtIGRlY29ycmVsYXRlcyBlbWJlZGRpbmcgZGltZW5zaW9uczogYyhaKSA9IM6j4bWi4omg4rG8IFtDb3YoWildwrLhtaLisbwgLyAoZC0xKSB3aGVyZSBDb3YoWikgPSAoWiAtIG1lYW4oWikp4bWAKFogLSBtZWFuKFopKSAvIChOLTEpLiBPZmYtZGlhZ29uYWwgY292YXJpYW5jZSBlbnRyaWVzIHNob3VsZCBiZSB6ZXJvLiBOb3RlIHRoYXQgVklDUmVnIGNvbXB1dGVzIHRoaXMgc2VwYXJhdGVseSBmb3IgejEgYW5kIHoyICh0d28gc2VwYXJhdGUgY292YXJpYW5jZSBtYXRyaWNlcyksIHdoZXJlYXMgQmFybG93IFR3aW5zIGNvbXB1dGVzIGEgY3Jvc3MtY292YXJpYW5jZSBiZXR3ZWVuIHoxIGFuZCB6Mi4gVGhpcyBkaWZmZXJlbmNlIG1lYW5zIFZJQ1JlZ1x1MDAyN3MgY292YXJpYW5jZSB0ZXJtIGlzIGFwcGxpZWQgaW5kZXBlbmRlbnRseSB0byBlYWNoIHZpZXcsIHdoaWNoIHByb3ZpZGVzIG1vcmUgc3RhYmxlIGdyYWRpZW50cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBjb3ZhcmlhbmNlX2xvc3MoeiwgZXBzPTFlLTQpOlxuICAgIFwiXCJcIkNvdmFyaWFuY2UgcmVndWxhcmlzYXRpb246IHBlbmFsaXNlIG9mZi1kaWFnb25hbCBjb3ZhcmlhbmNlIGVudHJpZXMuXG4gICAgejogKE4sIEQpIGVtYmVkZGluZyBiYXRjaCAobm90IHByZS1ub3JtYWxpc2VkKS5cbiAgICBSZXR1cm5zIHNjYWxhciBjb3ZhcmlhbmNlIGxvc3MuXG4gICAgXCJcIlwiXG4gICAgTiwgRCA9IHouc2l6ZSgpXG4gICAgIyBDZW50cmUgdGhlIGVtYmVkZGluZ3MgKHN1YnRyYWN0IG1lYW4gcGVyIGRpbWVuc2lvbilcbiAgICB6ID0geiAtIHoubWVhbihkaW09MCkgICAgICAgICAgICAgICAjIChOLCBEKVxuICAgICMgU2FtcGxlIGNvdmFyaWFuY2UgbWF0cml4OiAoRCwgRClcbiAgICBjb3YgPSAoei5UIEAgeikgLyAoTiAtIDEpXG4gICAgIyBPZmYtZGlhZ29uYWwgcGVuYWx0eTogc3VtIG9mIHNxdWFyZWQgb2ZmLWRpYWdvbmFsIGVsZW1lbnRzIC8gKEQtMSlcbiAgICBvZmZfZGlhZ19tYXNrID0gfnRvcmNoLmV5ZShELCBkdHlwZT10b3JjaC5ib29sLCBkZXZpY2U9ei5kZXZpY2UpXG4gICAgY292X2xvc3MgPSBjb3Zbb2ZmX2RpYWdfbWFza10ucG93KDIpLnN1bSgpIC8gKEQgLSAxKVxuICAgIHJldHVybiBjb3ZfbG9zc1xuXG4jIERlbW86IGNvcnJlbGF0ZWQgdnMgZGVjb3JyZWxhdGVkIGVtYmVkZGluZ3NcbnRvcmNoLm1hbnVhbF9zZWVkKDIpXG5OLCBEID0gMjU2LCA2NFxuXG4jIENvcnJlbGF0ZWQ6IHR3byBncm91cHMgb2YgZGltcyB0aGF0IGFyZSBpZGVudGljYWxcbnpfY29yciA9IHRvcmNoLnJhbmRuKE4sIEQgLy8gMikucmVwZWF0KDEsIDIpICAjIGRpbXMgMC4uMzEgPT0gZGltcyAzMi4uNjNcbmNvdl9jb3JyID0gY292YXJpYW5jZV9sb3NzKHpfY29ycilcbnByaW50KGZcdTAwMjdDb3ZhcmlhbmNlIGxvc3MgKGNvcnJlbGF0ZWQpOiB7Y292X2NvcnIuaXRlbSgpOi40Zn1cdTAwMjcpXG5cbiMgRGVjb3JyZWxhdGVkOiBpbmRlcGVuZGVudCByYW5kb20gZGltc1xuel9pbmRlcCA9IHRvcmNoLnJhbmRuKE4sIEQpXG5jb3ZfaW5kZXAgPSBjb3ZhcmlhbmNlX2xvc3Moel9pbmRlcClcbnByaW50KGZcdTAwMjdDb3ZhcmlhbmNlIGxvc3MgKGluZGVwZW5kZW50KToge2Nvdl9pbmRlcC5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWSUNSZWdMIOKAlCBMb2NhbCBhbmQgR2xvYmFsIEZlYXR1cmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWSUNSZWdMIChCYXJkZXMgZXQgYWwuIDIwMjIsIGV4dGVuZGVkKSBpbnRyb2R1Y2VzIGxvY2FsIHJlZ3VsYXJpc2F0aW9uIGZvciBwaXhlbC1sZXZlbCB0YXNrcyAoc2VnbWVudGF0aW9uLCBkZXRlY3Rpb24pLiBJbiBhZGRpdGlvbiB0byB0aGUgZ2xvYmFsIFZJQ1JlZyBsb3NzIG9uIHBvb2xlZCBlbWJlZGRpbmdzLCBpdCBjb21wdXRlcyBhIGxvY2FsIGludmFyaWFuY2UgbG9zcyBiZXR3ZWVuIHNwYXRpYWxseSBjb3JyZXNwb25kaW5nIGZlYXR1cmUgbWFwcy4gRm9yIGVhY2ggcGF0Y2ggaW4gdmlldyAxLCBmaW5kIHRoZSBuZWFyZXN0IHBhdGNoIGluIHZpZXcgMiAodmlhIGNvc2luZSBzaW1pbGFyaXR5IGluIGZlYXR1cmUgc3BhY2UpIGFuZCBhcHBseSB0aGUgaW52YXJpYW5jZSBsb3NzLiBUaGlzIGxvY2FsIHRlcm0gZW5jb3VyYWdlcyB0aGUgZW5jb2RlciB0byBwcm9kdWNlIHNwYXRpYWxseSBjb25zaXN0ZW50IGZlYXR1cmVzLCB3aGljaCBpcyB2YWx1YWJsZSBmb3IgZGVuc2UgcHJlZGljdGlvbiB0YXNrcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiB2aWNyZWdfbG9jYWxfbG9zcyhmZWF0X21hcDEsIGZlYXRfbWFwMiwgYWxwaGE9MC45KTpcbiAgICBcIlwiXCJWSUNSZWdMIGxvY2FsIGludmFyaWFuY2UgdmlhIG5lYXJlc3QtbmVpZ2hib3VyIG1hdGNoaW5nIGluIGZlYXR1cmUgc3BhY2UuXG4gICAgZmVhdF9tYXAxLCBmZWF0X21hcDI6IChOLCBDLCBILCBXKSBmZWF0dXJlIG1hcHMgZnJvbSB0d28gYXVnbWVudGVkIHZpZXdzLlxuICAgIGFscGhhOiB3ZWlnaHQgZm9yIGdsb2JhbCBWSUNSZWcgdnMgbG9jYWwgbWF0Y2hpbmcgbG9zcy5cbiAgICBSZXR1cm5zIGxvY2FsIGludmFyaWFuY2UgbG9zcyAoc2NhbGFyKS5cbiAgICBcIlwiXCJcbiAgICBOLCBDLCBILCBXID0gZmVhdF9tYXAxLnNoYXBlXG4gICAgIyBSZXNoYXBlIHRvIChOLCBIKlcsIEMpIGZvciBjb3NpbmUgc2ltaWxhcml0eSBjb21wdXRhdGlvblxuICAgIGYxID0gZmVhdF9tYXAxLnBlcm11dGUoMCwgMiwgMywgMSkucmVzaGFwZShOLCBIICogVywgQylcbiAgICBmMiA9IGZlYXRfbWFwMi5wZXJtdXRlKDAsIDIsIDMsIDEpLnJlc2hhcGUoTiwgSCAqIFcsIEMpXG4gICAgZjFfbm9ybSA9IEYubm9ybWFsaXplKGYxLCBkaW09MikgICMgKE4sIEgqVywgQylcbiAgICBmMl9ub3JtID0gRi5ub3JtYWxpemUoZjIsIGRpbT0yKVxuICAgICMgRm9yIGVhY2ggcGF0Y2ggaW4gZjEsIGZpbmQgbmVhcmVzdCBuZWlnaGJvdXIgaW4gZjJcbiAgICBzaW0gPSB0b3JjaC5ibW0oZjFfbm9ybSwgZjJfbm9ybS50cmFuc3Bvc2UoMSwgMikpICAjIChOLCBIKlcsIEgqVylcbiAgICBubl9pZHggPSBzaW0uYXJnbWF4KGRpbT0yKSAgICAgICAgICAgICAgICAgICAgICAgICAgIyAoTiwgSCpXKVxuICAgICMgR2F0aGVyIG1hdGNoZWQgcGF0Y2hlcyBmcm9tIGYyXG4gICAgbm5faWR4X2V4cGFuZGVkID0gbm5faWR4LnVuc3F1ZWV6ZSgyKS5leHBhbmQoLTEsIC0xLCBDKSAgIyAoTiwgSCpXLCBDKVxuICAgIGYyX21hdGNoZWQgPSBmMi5nYXRoZXIoMSwgbm5faWR4X2V4cGFuZGVkKSAgICAgICAgICAgICAgICMgKE4sIEgqVywgQylcbiAgICAjIExvY2FsIGludmFyaWFuY2U6IE1TRSBiZXR3ZWVuIGYxIHBhdGNoZXMgYW5kIHRoZWlyIE5OIGluIGYyXG4gICAgbG9jYWxfaW52ID0gRi5tc2VfbG9zcyhmMSwgZjJfbWF0Y2hlZC5kZXRhY2goKSlcbiAgICByZXR1cm4gbG9jYWxfaW52XG5cbiMgRGVtbyB3aXRoIHRpbnkgZmVhdHVyZSBtYXBzXG50b3JjaC5tYW51YWxfc2VlZCgzKVxuZm0xID0gdG9yY2gucmFuZG4oNCwgNTEyLCA3LCA3KSAgICMgKE49NCwgQz01MTIsIEg9NywgVz03KVxuZm0yID0gZm0xICsgMC4yICogdG9yY2gucmFuZG5fbGlrZShmbTEpXG5sb2NhbF9sb3NzID0gdmljcmVnX2xvY2FsX2xvc3MoZm0xLCBmbTIpXG5wcmludChmXHUwMDI3VklDUmVnTCBsb2NhbCBsb3NzIChzbGlnaHQgcGVydHVyYmF0aW9uKToge2xvY2FsX2xvc3MuaXRlbSgpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJWSUNSZWcgdnMgQmFybG93IFR3aW5zIOKAlCBFeHBsaWNpdCB2cyBJbXBsaWNpdCBDb2xsYXBzZSBQcmV2ZW50aW9uIiwiY29udGVudCI6IkluIEJhcmxvdyBUd2lucyB0aGUgZGlhZ29uYWwgb2YgdGhlIGNyb3NzLWNvcnJlbGF0aW9uIG1hdHJpeCBpcyBmb3JjZWQgdG8gMSDigJQgdGhpcyBpbXBsaWNpdGx5IHByZXZlbnRzIGNvbGxhcHNlIGJlY2F1c2UgaWYgYWxsIGVtYmVkZGluZ3MgYXJlIGNvbnN0YW50LCB0aGUgZGlhZ29uYWwgaXMgdW5kZWZpbmVkICh6ZXJvIHZhcmlhbmNlKS4gVklDUmVnIG1ha2VzIHRoaXMgZXhwbGljaXQgd2l0aCBhIGhpbmdlIGxvc3Mgb24gcGVyLWRpbWVuc2lvbiBzdGFuZGFyZCBkZXZpYXRpb24uIFRoZSBwcmFjdGljYWwgZGlmZmVyZW5jZTogVklDUmVnXHUwMDI3cyB2YXJpYW5jZSB0ZXJtIGFjdGl2YXRlcyBvbmx5IHdoZW4gc3RkIFx1MDAzYyDOsyBhbmQgaXMgemVybyBvdGhlcndpc2U7IEJhcmxvdyBUd2luc1x1MDAyNyBkaWFnb25hbCB0ZXJtIGFsd2F5cyBleGVydHMgcHJlc3N1cmUuIFZJQ1JlZyBpcyBvZnRlbiBlYXNpZXIgdG8gdHVuZSBzaW5jZSB0aGUgdGhyZWUgdGVybXMgYXJlIGluZGVwZW5kZW50bHkgY29udHJvbGxlZCBieSDOuywgzrwsIM69LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikh5cGVycGFyYW1ldGVyIFNlbnNpdGl2aXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWSUNSZWcgaW50cm9kdWNlcyB0aHJlZSB3ZWlnaHRpbmcgY29lZmZpY2llbnRzOiDOuyAoaW52YXJpYW5jZSksIM68ICh2YXJpYW5jZSksIM69IChjb3ZhcmlhbmNlKS4gVGhlIGRlZmF1bHQgdmFsdWVzIM67ID0gzrwgPSAyNSwgzr0gPSAxIHdvcmsgd2VsbCBhY3Jvc3MgYXJjaGl0ZWN0dXJlcyBhbmQgZGF0YXNldHMuIFRoZSB2YXJpYW5jZSB3ZWlnaHQgzrwgc2hvdWxkIGJlIGVxdWFsIHRvIM67IHRvIGJhbGFuY2UgdGhlIHR3byBtYWluIG9iamVjdGl2ZXMuIFRoZSBjb3ZhcmlhbmNlIHdlaWdodCDOvSBjYW4gYmUgbXVjaCBzbWFsbGVyICgxLjApIGJlY2F1c2UgdGhlIGNvdmFyaWFuY2UgbG9zcyBpcyB0eXBpY2FsbHkgbXVjaCBsYXJnZXIgaW4gbWFnbml0dWRlIHRoYW4gdGhlIGludmFyaWFuY2UgbG9zcy4gVGhlIM6zID0gMS4wIHRhcmdldCBzdGQgaXMgYXBwcm9wcmlhdGUgd2hlbiBlbWJlZGRpbmdzIGFyZSBub3QgcHJlLW5vcm1hbGlzZWQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyLOuz0yNSwgzrw9MjUsIM69PTEg4oCUIGRlZmF1bHQgaHlwZXJwYXJhbWV0ZXJzOyByb2J1c3QgYWNyb3NzIGFyY2hpdGVjdHVyZXMuIiwizrM9MS4wIHRhcmdldCBzdGQgd29ya3Mgd2hlbiB0aGUgcHJvamVjdG9yIGhhcyBubyBCTiBvbiBmaW5hbCBsYXllci4iLCJQcm9qZWN0b3I6IDMtbGF5ZXIgTUxQIHRvIDgxOTItZGltLCBzYW1lIGFzIEJhcmxvdyBUd2lucy4iLCJMQVJTIG9wdGltaXplciwgYmF0Y2ggMjA0OCwgYmFzZV9scj0wLjIsIHdlaWdodF9kZWNheT0xZS02LCAxMDAwIGVwb2Nocy4iLCJNb25pdG9yIHBlci10ZXJtIGxvc3NlcyBzZXBhcmF0ZWx5IOKAlCBpZiB2YXJfbG9zcyBcdTAwM2UgMCwgbW9kZWwgaXMgY29sbGFwc2luZy4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTXVsdGktTW9kYWwgYW5kIE90aGVyIEFwcGxpY2F0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVklDUmVnXHUwMDI3cyB0aHJlZS10ZXJtIHN0cnVjdHVyZSBnZW5lcmFsaXNlcyBuYXR1cmFsbHkgdG8gbXVsdGktbW9kYWwgc2V0dGluZ3MuIEZvciB2aXNpb24tbGFuZ3VhZ2UgbGVhcm5pbmcsIHRoZSBpbnZhcmlhbmNlIHRlcm0gYWxpZ25zIGltYWdlIGFuZCB0ZXh0IGVtYmVkZGluZ3MsIHdoaWxlIHZhcmlhbmNlIGFuZCBjb3ZhcmlhbmNlIHJlZ3VsYXJpc2F0aW9uIHByZXZlbnQgZGVnZW5lcmF0ZSBzb2x1dGlvbnMuIFVubGlrZSBjb250cmFzdGl2ZSBtZXRob2RzIHRoYXQgcmVxdWlyZSBoYXJkIG5lZ2F0aXZlIG1pbmluZyBhY3Jvc3MgbW9kYWxpdGllcywgVklDUmVnIG9ubHkgbmVlZHMgcG9zaXRpdmUgcGFpcnMgKGltYWdlLWNhcHRpb24gcGFpcnMpLCBtYWtpbmcgaXQgc3VpdGFibGUgd2hlbiBoYXJkIG5lZ2F0aXZlcyBhcmUgZXhwZW5zaXZlIHRvIG1pbmUuIFRoZSBsb2NhbCB2YXJpYW50IChWSUNSZWdMKSBlbmFibGVzIHBpeGVsLWFsaWduZWQgbXVsdGktbW9kYWwgcHJldHJhaW5pbmcgZm9yIHRhc2tzIGxpa2UgdmlzdWFsIHF1ZXN0aW9uIGFuc3dlcmluZy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQ3JpdGVyaW9uIiwiQmFybG93IFR3aW5zIiwiVklDUmVnIl0sInJvd3MiOltbIlZhcmlhbmNlIGNvbnRyb2wiLCJJbXBsaWNpdCAoZGlhZ29uYWwgQyDihpIgMSkiLCJFeHBsaWNpdCBoaW5nZTogbWF4KDAsIM6zLXN0ZCkiXSxbIkludmFyaWFuY2UiLCJEaWFnb25hbCBjcm9zcy1jb3JyZWxhdGlvbiDihpIgMSIsIkRpcmVjdCBNU0UgYmV0d2VlbiB6IGFuZCB6XHUwMDI3Il0sWyJDb3ZhcmlhbmNlIiwiT2ZmLWRpYWdvbmFsIGNyb3NzLWNvcnIg4oaSIDAiLCJPZmYtZGlhZ29uYWwgb2YgcGVyLXZpZXcgY292IOKGkiAwIl0sWyJIeXBlcnBhcmFtZXRlcnMiLCLOuz0wLjAwNSIsIs67PTI1LCDOvD0yNSwgzr09MSJdLFsiTG9jYWwgdmFyaWFudCIsIk5vIiwiVklDUmVnTCDigJQgTk4gbWF0Y2hpbmcgb24gZmVhdHVyZSBtYXBzIl0sWyJNdWx0aS1tb2RhbCBzdXBwb3J0IiwiTGltaXRlZCIsIk5hdHVyYWwgZml0IHZpYSBzZXBhcmF0ZSB2YXJpYW5jZS9pbnYvY292Il1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbXBsZW1lbnRhdGlvbiBHdWlkZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBjb21wbGV0ZSBWSUNSZWcgaW1wbGVtZW50YXRpb24gcmVxdWlyZXMgZm91ciBjb21wb25lbnRzOiAoMSkgZW5jb2RlciAoYW55IFJlc05ldCBvciBWaVQgYmFja2JvbmUpLCAoMikgMy1sYXllciBNTFAgcHJvamVjdG9yIHRvIDgxOTItZGltIHdpdGhvdXQgQk4gb24gdGhlIGZpbmFsIGxheWVyLCAoMykgdGhyZWUgbG9zcyBmdW5jdGlvbnMgKHZhcmlhbmNlLCBpbnZhcmlhbmNlLCBjb3ZhcmlhbmNlKSB3aXRoIHNlcGFyYXRlIG1vbml0b3Jpbmcgb2YgZWFjaCB0ZXJtLCBhbmQgKDQpIExBUlMgb3B0aW1pemVyIHdpdGggYmFzZV9scj0wLjIsIHdlaWdodF9kZWNheT0xZS02LCAxMDAwLWVwb2NoIGNvc2luZSBkZWNheSBzY2hlZHVsZS4gRHVyaW5nIHRyYWluaW5nLCBsb2cgYWxsIHRocmVlIGxvc3MgdGVybXMgc2VwYXJhdGVseSDigJQgYSByaXNpbmcgaW52YXJpYW5jZSB0ZXJtIGluZGljYXRlcyBhdWdtZW50YXRpb25zIGFyZSB0b28gc3Ryb25nOyBhIHJpc2luZyB2YXJpYW5jZSB0ZXJtIGluZGljYXRlcyB0aGUgbW9kZWwgaXMgYXBwcm9hY2hpbmcgY29sbGFwc2U7IGEgcmlzaW5nIGNvdmFyaWFuY2UgdGVybSBpbmRpY2F0ZXMgZGltZW5zaW9uYWwgcmVkdW5kYW5jeS4gVklDUmVnIGlzIHJvYnVzdCB0byBtb2RlcmF0ZSBoeXBlcnBhcmFtZXRlciB2YXJpYXRpb246IGhhbHZpbmcgb3IgZG91YmxpbmcgzrsgYW5kIM68IHR5cGljYWxseSBjYXVzZXMgbGVzcyB0aGFuIDAuNSUgdG9wLTEgcmVncmVzc2lvbi4ifV0="
---
# VICReg — Variance, Invariance, Covariance Regularization

VICReg (Variance-Invariance-Covariance Regularization, Bardes et al. 2022) makes the connection between Barlow Twins and collapse prevention more explicit. While Barlow Twins implicitly prevents collapse via the diagonal invariance term, VICReg introduces a dedicated variance hinge loss that directly penalises low variance in any embedding dimension. This cleaner decomposition makes the method more interpretable and easier to tune, while achieving the same level of performance.

## Three-Term Loss Function

VICReg decomposes the objective into three independently weighted terms: (1) Invariance s(Z, Z') = (1/N)Σᵢ‖zᵢ - z'ᵢ‖² — MSE between embeddings of the two views (push representations together); (2) Variance v(Z) = Σⱼ max(0, γ - Std(zⱼ)) — hinge loss maintaining per-dimension standard deviation ≥ γ=1 (prevent collapse); (3) Covariance c(Z) = Σᵢ≠ⱼ [Cov(Z)]²ᵢⱼ / (d-1) — sum of squared off-diagonal covariance entries (decorrelate dimensions). Total loss: λs + μ[v(Z)+v(Z')] + ν[c(Z)+c(Z')].

```python
import torch
import torch.nn.functional as F

def vicreg_loss(z1, z2, lambda_=25.0, mu=25.0, nu=1.0, gamma=1.0):
    """VICReg loss with three terms: variance, invariance, covariance.
    z1, z2: (N, D) raw embeddings (not L2-normalised, not batch-normalised).
    lambda_: weight for invariance term.
    mu:      weight for variance term (applied to both z1 and z2).
    nu:      weight for covariance term (applied to both z1 and z2).
    gamma:   target standard deviation for variance hinge.
    """
    N, D = z1.size()
    # 1. Invariance: MSE between embeddings of two views
    inv_loss = F.mse_loss(z1, z2)
    # 2. Variance: hinge loss (each dimension std >= gamma)
    var_loss = variance_loss(z1, gamma) + variance_loss(z2, gamma)
    # 3. Covariance: off-diagonal covariance -> 0
    cov_loss = covariance_loss(z1) + covariance_loss(z2)
    loss = lambda_ * inv_loss + mu * var_loss + nu * cov_loss
    return loss, inv_loss.item(), var_loss.item(), cov_loss.item()

# Quick test
torch.manual_seed(0)
z1 = torch.randn(256, 2048)
z2 = z1 + 0.1 * torch.randn_like(z1)  # slight augmentation
total, inv, var, cov = vicreg_loss(z1, z2)
print(f'Total loss: {total:.2f}')
print(f'  Invariance: {inv:.4f}')
print(f'  Variance:   {var:.4f}')
print(f'  Covariance: {cov:.4f}')
```

## Variance Term — Preventing Collapse

The variance term is a hinge loss that penalises any embedding dimension whose standard deviation across the batch falls below γ = 1: v(Z) = Σⱼ max(0, γ - √(Var(zⱼ) + ε)). If all samples collapse to the same vector, every dimension's std → 0, and this term becomes huge. Crucially, the variance is computed per-dimension independently — a dimension with std ≥ γ contributes zero penalty. This is more direct than Barlow Twins' implicit variance control via the diagonal of the cross-correlation matrix.

```python
import torch
import torch.nn.functional as F

def variance_loss(z, gamma=1.0, eps=1e-4):
    """Variance hinge loss: penalise dimensions where std < gamma.
    z: (N, D) embedding batch.
    Returns scalar — sum of hinge losses across D dimensions.
    """
    # std along batch dimension for each feature
    std = torch.sqrt(z.var(dim=0) + eps)       # (D,)
    hinge = F.relu(gamma - std)                 # 0 if std >= gamma, else gamma - std
    return hinge.mean()  # paper uses mean over D

# Demonstrate: collapse → large variance loss; spread → near-zero
torch.manual_seed(1)
N, D = 256, 128

# Collapsed: all outputs constant
z_collapsed = torch.ones(N, D)
v_collapsed = variance_loss(z_collapsed)
print(f'Variance loss (collapsed, all-ones): {v_collapsed.item():.4f}  (expected ~1.0)')

# Spread: random normal has std ≈ 1
z_spread = torch.randn(N, D)
v_spread = variance_loss(z_spread)
print(f'Variance loss (spread, N(0,1)):      {v_spread.item():.6f}  (expected ~0.0)')

# Partial collapse: some dims collapsed
z_partial = torch.randn(N, D)
z_partial[:, :32] = z_partial[:, :32].mean(0, keepdim=True).expand(N, -1)  # 32 dims collapsed
v_partial = variance_loss(z_partial)
print(f'Variance loss (32/{D} dims collapsed): {v_partial.item():.4f}')
```

## Covariance Regularization

The covariance term decorrelates embedding dimensions: c(Z) = Σᵢ≠ⱼ [Cov(Z)]²ᵢⱼ / (d-1) where Cov(Z) = (Z - mean(Z))ᵀ(Z - mean(Z)) / (N-1). Off-diagonal covariance entries should be zero. Note that VICReg computes this separately for z1 and z2 (two separate covariance matrices), whereas Barlow Twins computes a cross-covariance between z1 and z2. This difference means VICReg's covariance term is applied independently to each view, which provides more stable gradients.

```python
import torch

def covariance_loss(z, eps=1e-4):
    """Covariance regularisation: penalise off-diagonal covariance entries.
    z: (N, D) embedding batch (not pre-normalised).
    Returns scalar covariance loss.
    """
    N, D = z.size()
    # Centre the embeddings (subtract mean per dimension)
    z = z - z.mean(dim=0)               # (N, D)
    # Sample covariance matrix: (D, D)
    cov = (z.T @ z) / (N - 1)
    # Off-diagonal penalty: sum of squared off-diagonal elements / (D-1)
    off_diag_mask = ~torch.eye(D, dtype=torch.bool, device=z.device)
    cov_loss = cov[off_diag_mask].pow(2).sum() / (D - 1)
    return cov_loss

# Demo: correlated vs decorrelated embeddings
torch.manual_seed(2)
N, D = 256, 64

# Correlated: two groups of dims that are identical
z_corr = torch.randn(N, D // 2).repeat(1, 2)  # dims 0..31 == dims 32..63
cov_corr = covariance_loss(z_corr)
print(f'Covariance loss (correlated): {cov_corr.item():.4f}')

# Decorrelated: independent random dims
z_indep = torch.randn(N, D)
cov_indep = covariance_loss(z_indep)
print(f'Covariance loss (independent): {cov_indep.item():.4f}')
```

## VICRegL — Local and Global Features

VICRegL (Bardes et al. 2022, extended) introduces local regularisation for pixel-level tasks (segmentation, detection). In addition to the global VICReg loss on pooled embeddings, it computes a local invariance loss between spatially corresponding feature maps. For each patch in view 1, find the nearest patch in view 2 (via cosine similarity in feature space) and apply the invariance loss. This local term encourages the encoder to produce spatially consistent features, which is valuable for dense prediction tasks.

```python
import torch
import torch.nn.functional as F

def vicreg_local_loss(feat_map1, feat_map2, alpha=0.9):
    """VICRegL local invariance via nearest-neighbour matching in feature space.
    feat_map1, feat_map2: (N, C, H, W) feature maps from two augmented views.
    alpha: weight for global VICReg vs local matching loss.
    Returns local invariance loss (scalar).
    """
    N, C, H, W = feat_map1.shape
    # Reshape to (N, H*W, C) for cosine similarity computation
    f1 = feat_map1.permute(0, 2, 3, 1).reshape(N, H * W, C)
    f2 = feat_map2.permute(0, 2, 3, 1).reshape(N, H * W, C)
    f1_norm = F.normalize(f1, dim=2)  # (N, H*W, C)
    f2_norm = F.normalize(f2, dim=2)
    # For each patch in f1, find nearest neighbour in f2
    sim = torch.bmm(f1_norm, f2_norm.transpose(1, 2))  # (N, H*W, H*W)
    nn_idx = sim.argmax(dim=2)                          # (N, H*W)
    # Gather matched patches from f2
    nn_idx_expanded = nn_idx.unsqueeze(2).expand(-1, -1, C)  # (N, H*W, C)
    f2_matched = f2.gather(1, nn_idx_expanded)               # (N, H*W, C)
    # Local invariance: MSE between f1 patches and their NN in f2
    local_inv = F.mse_loss(f1, f2_matched.detach())
    return local_inv

# Demo with tiny feature maps
torch.manual_seed(3)
fm1 = torch.randn(4, 512, 7, 7)   # (N=4, C=512, H=7, W=7)
fm2 = fm1 + 0.2 * torch.randn_like(fm1)
local_loss = vicreg_local_loss(fm1, fm2)
print(f'VICRegL local loss (slight perturbation): {local_loss.item():.4f}')
```

> **VICReg vs Barlow Twins — Explicit vs Implicit Collapse Prevention**: In Barlow Twins the diagonal of the cross-correlation matrix is forced to 1 — this implicitly prevents collapse because if all embeddings are constant, the diagonal is undefined (zero variance). VICReg makes this explicit with a hinge loss on per-dimension standard deviation. The practical difference: VICReg's variance term activates only when std < γ and is zero otherwise; Barlow Twins' diagonal term always exerts pressure. VICReg is often easier to tune since the three terms are independently controlled by λ, μ, ν.

## Hyperparameter Sensitivity

VICReg introduces three weighting coefficients: λ (invariance), μ (variance), ν (covariance). The default values λ = μ = 25, ν = 1 work well across architectures and datasets. The variance weight μ should be equal to λ to balance the two main objectives. The covariance weight ν can be much smaller (1.0) because the covariance loss is typically much larger in magnitude than the invariance loss. The γ = 1.0 target std is appropriate when embeddings are not pre-normalised.

- λ=25, μ=25, ν=1 — default hyperparameters; robust across architectures.
- γ=1.0 target std works when the projector has no BN on final layer.
- Projector: 3-layer MLP to 8192-dim, same as Barlow Twins.
- LARS optimizer, batch 2048, base_lr=0.2, weight_decay=1e-6, 1000 epochs.
- Monitor per-term losses separately — if var_loss > 0, model is collapsing.

## Multi-Modal and Other Applications

VICReg's three-term structure generalises naturally to multi-modal settings. For vision-language learning, the invariance term aligns image and text embeddings, while variance and covariance regularisation prevent degenerate solutions. Unlike contrastive methods that require hard negative mining across modalities, VICReg only needs positive pairs (image-caption pairs), making it suitable when hard negatives are expensive to mine. The local variant (VICRegL) enables pixel-aligned multi-modal pretraining for tasks like visual question answering.

| Criterion | Barlow Twins | VICReg |
| --- | --- | --- |
| Variance control | Implicit (diagonal C → 1) | Explicit hinge: max(0, γ-std) |
| Invariance | Diagonal cross-correlation → 1 | Direct MSE between z and z' |
| Covariance | Off-diagonal cross-corr → 0 | Off-diagonal of per-view cov → 0 |
| Hyperparameters | λ=0.005 | λ=25, μ=25, ν=1 |
| Local variant | No | VICRegL — NN matching on feature maps |
| Multi-modal support | Limited | Natural fit via separate variance/inv/cov |

## Implementation Guide

A complete VICReg implementation requires four components: (1) encoder (any ResNet or ViT backbone), (2) 3-layer MLP projector to 8192-dim without BN on the final layer, (3) three loss functions (variance, invariance, covariance) with separate monitoring of each term, and (4) LARS optimizer with base_lr=0.2, weight_decay=1e-6, 1000-epoch cosine decay schedule. During training, log all three loss terms separately — a rising invariance term indicates augmentations are too strong; a rising variance term indicates the model is approaching collapse; a rising covariance term indicates dimensional redundancy. VICReg is robust to moderate hyperparameter variation: halving or doubling λ and μ typically causes less than 0.5% top-1 regression.

