---
title: "Video Swin Transformer: Spatiotemporal Shifted Window Attention"
slug: "video-swin-transformer"
description: ""
tags: [""]
topic: ""
status: ""
updated: ""
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWaWRlbyBTd2luIFRyYW5zZm9ybWVyIChMaXUgZXQgYWwuLCAyMDIyKSBhZGFwdHMgdGhlIGltYWdlIFN3aW4gVHJhbnNmb3JtZXIgZm9yIHZpZGVvIGJ5IGV4dGVuZGluZyBpdHMgbG9jYWwgd2luZG93IGF0dGVudGlvbiB0byB0aHJlZSBkaW1lbnNpb25zOiB0ZW1wb3JhbCwgaGVpZ2h0LCBhbmQgd2lkdGguIEVhY2ggYXR0ZW50aW9uIGxheWVyIG9wZXJhdGVzIHdpdGhpbiBzbWFsbCBub24tb3ZlcmxhcHBpbmcgc3BhdGlvdGVtcG9yYWwgd2luZG93cywga2VlcGluZyBjb21wbGV4aXR5IGxpbmVhciBpbiB2aWRlbyBsZW5ndGguIFRoZSBzaGlmdGVkLXdpbmRvdyBtZWNoYW5pc20gY29ubmVjdHMgYWRqYWNlbnQgd2luZG93cyBhY3Jvc3MgbGF5ZXJzIHRvIGFjaGlldmUgZ2xvYmFsIHJlY2VwdGl2ZSBmaWVsZHMgZWZmaWNpZW50bHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbWFnZSBTd2luIHVzZXMgMkQgc2hpZnRlZCB3aW5kb3dzIG9mIHNpemUgN8OXNy4gVmlkZW8gU3dpbiBhZGRzIGEgdGVtcG9yYWwgd2luZG93IG9mIHNpemUgMiwgY3JlYXRpbmcgMsOXN8OXNyBzcGF0aW90ZW1wb3JhbCBjdWJlcy4gVGhlIHBhdGNoIGVtYmVkZGluZyBhYnNvcmJzIGZyYW1lcyBhcyB0b2tlbnM6IGEgVMOXSMOXVyB2aWRlbyBiZWNvbWVzIFTDlyhILzQpw5coVy80KSB0b2tlbnMgYWZ0ZXIgdGhlIGluaXRpYWwgMsOXNMOXNCBwYXRjaCBwYXJ0aXRpb24uIFN0YWdlLXdpc2UgcGF0Y2ggbWVyZ2luZyBwcm9ncmVzc2l2ZWx5IHJlZHVjZXMgc3BhdGlhbCBhbmQgdGVtcG9yYWwgcmVzb2x1dGlvbiwgYnVpbGRpbmcgYSBoaWVyYXJjaGljYWwgZmVhdHVyZSBweXJhbWlkIGZvciBkb3duc3RyZWFtIHRhc2tzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IjNEIFNoaWZ0ZWQgV2luZG93cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgM0Qgc2VsZi1hdHRlbnRpb24gaXMgTygoVMK3SMK3VynCsiksIGluZmVhc2libGUgZm9yIGV2ZW4gc2hvcnQgY2xpcHMuIFZpZGVvIFN3aW4gcmVzdHJpY3RzIGF0dGVudGlvbiB0byBsb2NhbCAzRCB3aW5kb3dzIG9mIHNpemUgV3TDl1dow5dXdyAoZGVmYXVsdCAyw5c3w5c3KSwgZ2l2aW5nIE8oVMK3SMK3V8K3V3TCt1dowrdXdykgY29tcGxleGl0eSDigJQgbGluZWFyIGluIHZpZGVvIGxlbmd0aC4gV2l0aGluIGVhY2ggd2luZG93LCBtdWx0aS1oZWFkIHNlbGYtYXR0ZW50aW9uIGNhcHR1cmVzIGxvY2FsIHNwYXRpb3RlbXBvcmFsIGRlcGVuZGVuY2llczsgYmV0d2Vlbi13aW5kb3cgaW5mb3JtYXRpb24gZmxvd3MgdmlhIHdpbmRvdyBzaGlmdHMgaW4gYWx0ZXJuYXRpbmcgdHJhbnNmb3JtZXIgYmxvY2tzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gZWlub3BzIGltcG9ydCByZWFycmFuZ2VcblxuZGVmIHdpbmRvd19wYXJ0aXRpb25fM2QoeCwgd2luZG93X3NpemU9KDIsIDcsIDcpKTpcbiAgICBcIlwiXCJQYXJ0aXRpb24gKEIsVCxILFcsQykgaW50byAobnVtX3dpbmRvd3MqQiwgV3QqV2gqV3csIEMpLlwiXCJcIlxuICAgIFd0LCBXaCwgV3cgPSB3aW5kb3dfc2l6ZVxuICAgIEIsIFQsIEgsIFcsIEMgPSB4LnNoYXBlXG4gICAgeCA9IHgudmlldyhCLCBULy9XdCwgV3QsIEgvL1doLCBXaCwgVy8vV3csIFd3LCBDKVxuICAgIHdpbmRvd3MgPSB4LnBlcm11dGUoMCwgMSwgMywgNSwgMiwgNCwgNiwgNykuY29udGlndW91cygpXG4gICAgd2luZG93cyA9IHdpbmRvd3MudmlldygtMSwgV3QgKiBXaCAqIFd3LCBDKVxuICAgIHJldHVybiB3aW5kb3dzICAjIChudW1fd2luZG93cyAqIEIsIHRva2Vuc19wZXJfd2luZG93LCBDKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5nIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiBzaGlmdGVkX3dpbmRvd19hdHRuXzNkKHgsIHdpbl9zaXplLCBzaGlmdCwgbWFzayk6XG4gICAgQiwgVCwgSCwgVywgQyA9IHguc2hhcGVcbiAgICBpZiBhbnkocyBcdTAwM2UgMCBmb3IgcyBpbiBzaGlmdCk6XG4gICAgICAgIHggPSB0b3JjaC5yb2xsKFxuICAgICAgICAgICAgeCxcbiAgICAgICAgICAgIHNoaWZ0cz0oLXNoaWZ0WzBdLCAtc2hpZnRbMV0sIC1zaGlmdFsyXSksXG4gICAgICAgICAgICBkaW1zPSgxLCAyLCAzKVxuICAgICAgICApXG4gICAgd2lucyA9IHdpbmRvd19wYXJ0aXRpb25fM2QoeCwgd2luX3NpemUpXG4gICAgb3V0ICA9IHdpbmRvd19tc2Eod2lucywgbWFzaz1tYXNrKVxuICAgIHggICAgPSB3aW5kb3dfcmV2ZXJzZV8zZChvdXQsIHdpbl9zaXplLCBULCBILCBXKVxuICAgIGlmIGFueShzIFx1MDAzZSAwIGZvciBzIGluIHNoaWZ0KTpcbiAgICAgICAgeCA9IHRvcmNoLnJvbGwoXG4gICAgICAgICAgICB4LCBzaGlmdHM9KHNoaWZ0WzBdLCBzaGlmdFsxXSwgc2hpZnRbMl0pLCBkaW1zPSgxLCAyLCAzKVxuICAgICAgICApXG4gICAgcmV0dXJuIHgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjeWNsaWMgc2hpZnQgZm9yIGJvdW5kYXJ5IGhhbmRsaW5nIGlzIGlkZW50aWNhbCB0byBpbWFnZSBTd2luIGJ1dCBleHRlbmRlZCB0byAzRDogYWZ0ZXIgcm9sbGluZyB0aGUgdGVuc29yIGJ5ICgtMSwgLTMsIC0zKSBpbiAoVCwgSCwgVyksIHdpbmRvd3MgbmVhciBib3VuZGFyaWVzIGNvbnRhaW4gdG9rZW5zIGZyb20gb3Bwb3NpdGUgZW5kcyBvZiB0aGUgdm9sdW1lLiBBbiBhdHRlbnRpb24gbWFzayB6ZXJvZXMgb3V0IGNyb3NzLWJvdW5kYXJ5IGF0dGVudGlvbiBzY29yZXMsIGVuc3VyaW5nIHNoaWZ0ZWQtd2luZG93IGF0dGVudGlvbiBpcyBlcXVpdmFsZW50IHRvIHBhcnRpdGlvbmluZyB0aGUgY3ljbGljYWxseSBzaGlmdGVkIHRlbnNvciBpbnRvIHByb3BlciBub24tb3ZlcmxhcHBpbmcgd2luZG93cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTcGF0aW90ZW1wb3JhbCBMb2NhbGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BhdGlvdGVtcG9yYWwgbG9jYWxpdHkgaXMgd2VsbC1qdXN0aWZpZWQgZm9yIHZpZGVvOiBhZGphY2VudCBmcmFtZXMgc2hhcmUgbW9zdCBjb250ZW50LCBhbmQgbG9jYWwgb2JqZWN0IG1vdGlvbiByYXJlbHkgc3BhbnMgbW9yZSB0aGFuIGEgZmV3IHBpeGVscyBwZXIgZnJhbWUuIEEgdGVtcG9yYWwgd2luZG93IG9mIHNpemUgMiBjb3ZlcnMgdHdvIGNvbnNlY3V0aXZlIGZyYW1lcyDigJQgc3VmZmljaWVudCB0byBjYXB0dXJlIGludGVyLWZyYW1lIG1vdGlvbiBhdCB0eXBpY2FsIHZpZGVvIGZyYW1lIHJhdGVzLiBMYXJnZXIgdGVtcG9yYWwgd2luZG93cyBpbmNyZWFzZSBGTE9QcyBxdWFkcmF0aWNhbGx5IHdpdGhpbiB0aGUgd2luZG93IGFuZCBzaG93IGRpbWluaXNoaW5nIGFjY3VyYWN5IHJldHVybnMgb24gc3RhbmRhcmQgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbXBhcmVkIHRvIGZ1bGwgc3BhdGlvdGVtcG9yYWwgYXR0ZW50aW9uICh1c2VkIGluIFRpbWVTZm9ybWVyIHNwYWNlLXRpbWUgbW9kZSksIFZpZGVvIFN3aW5cdTAwMjdzIHdpbmRvdyBhdHRlbnRpb24gcmVkdWNlcyBGTE9QcyBieSByb3VnaGx5IDEwIHRvIDUww5cgb24gOC1mcmFtZSBjbGlwcy4gVGltZVNmb3JtZXIgdXNlcyBkaXZpZGVkIHNwYWNlLXRpbWUgYXR0ZW50aW9uIOKAlCBzZXBhcmF0ZSBzcGF0aWFsIGFuZCB0ZW1wb3JhbCBzdGFnZXMg4oCUIGFsc28gYWNoaWV2aW5nIGxpbmVhciBjb21wbGV4aXR5LCBidXQgVmlkZW8gU3dpblx1MDAyN3Mgam9pbnQgc3BhdGlvdGVtcG9yYWwgd2luZG93cyBjYXB0dXJlIGNyb3NzLW1vZGFsIGNvcnJlbGF0aW9ucyBtb3JlIGRpcmVjdGx5IHdpdGhpbiBlYWNoIGF0dGVudGlvbiBsYXllci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUZW1wb3JhbCBEb3duc2FtcGxpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZpZGVvIFN3aW4gdXNlcyBmb3VyIHN0YWdlcyB3aXRoIHNwYXRpYWwgcGF0Y2ggbWVyZ2luZyBhZnRlciBzdGFnZXMgMSwgMiwgYW5kIDMuIFNwYXRpYWwgcmVzb2x1dGlvbiBkcm9wcyBmcm9tIEgvNCB0byBILzgsIEgvMTYsIGFuZCBILzMyLiBUZW1wb3JhbCBwYXRjaCBtZXJnaW5nIGNhbiBiZSBhcHBsaWVkIHNpbWlsYXJseSwgaGFsdmluZyB0ZW1wb3JhbCByZXNvbHV0aW9uIGF0IHNlbGVjdGVkIHN0YWdlcy4gVGhpcyBjcmVhdGVzIGEgZmVhdHVyZSBweXJhbWlkIHJldXNhYmxlIGZvciBkZW5zZSBkb3duc3RyZWFtIHRhc2tzIGxpa2UgYWN0aW9uIHNlZ21lbnRhdGlvbiwgdmlkZW8gb2JqZWN0IGRldGVjdGlvbiwgYW5kIHNwYXRpb3RlbXBvcmFsIGRlbnNlIHByZWRpY3Rpb24gd2l0aCBtaW5pbWFsIGFkYXB0YXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFRlbXBvcmFsUGF0Y2hNZXJnaW5nKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5vcm0gPSBubi5MYXllck5vcm0oMiAqIGRpbSlcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uTGluZWFyKDIgKiBkaW0sIGRpbSwgYmlhcz1GYWxzZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiAgIyB4OiAoQiwgVCwgSCwgVywgQylcbiAgICAgICAgeDAgPSB4WzosIDA6OjJdICAgIyBldmVuLWluZGV4ZWQgZnJhbWVzXG4gICAgICAgIHgxID0geFs6LCAxOjoyXSAgICMgb2RkLWluZGV4ZWQgZnJhbWVzXG4gICAgICAgIHggID0gdG9yY2guY2F0KFt4MCwgeDFdLCBkaW09LTEpICAjIChCLCBULy8yLCBILCBXLCAyQylcbiAgICAgICAgcmV0dXJuIHNlbGYucHJvaihzZWxmLm5vcm0oeCkpICAgICMgKEIsIFQvLzIsIEgsIFcsIEMpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdGVtcG9yYWwgcmVzb2x1dGlvbiBzY2hlZHVsZSBkZXBlbmRzIG9uIHRoZSB0YXNrOiBmb3Igc2hvcnQtY2xpcCBjbGFzc2lmaWNhdGlvbiB1c2luZyA4IG9yIDE2IGZyYW1lcywgdGVtcG9yYWwgbWVyZ2luZyBpcyB0eXBpY2FsbHkgZGlzYWJsZWQgdG8gcHJlc2VydmUgYWxsIHRlbXBvcmFsIHRva2Vucy4gRm9yIGxvbmdlciB2aWRlb3MsIHRlbXBvcmFsIG1lcmdpbmcgYWZ0ZXIgc3RhZ2UgMSBvciAyIHJlZHVjZXMgbWVtb3J5IGZvb3RwcmludC4gVGhlIFZpZGVvIFN3aW4tQiBtb2RlbCB1c2VzIHdpbmRvdyBzaXplcyAoOCwgNywgNykgYXQgbGF0ZXIgc3RhZ2VzIHdoZXJlIHRlbXBvcmFsIHJlc29sdXRpb24gaGFzIGJlZW4gcmVkdWNlZCBieSBlYXJsaWVyIHBhdGNoIG1lcmdpbmcgbGF5ZXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gdG8gM0QgQ05OcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmlkZW8gU3dpbiBvdXRwZXJmb3JtcyAzRCBDTk5zIGluIHRocmVlIGtleSB3YXlzLiBGaXJzdCwgYXR0ZW50aW9uIGlzIGRhdGEtYWRhcHRpdmU6IHdpbmRvdyBhdHRlbnRpb24gd2VpZ2h0cyBkZXBlbmQgb24gY29udGVudCwgdW5saWtlIGZpeGVkIGNvbnZvbHV0aW9uIGtlcm5lbHMuIFNlY29uZCwgSW1hZ2VOZXQtMjFLIHByZXRyYWluaW5nIHRyYW5zZmVycyB3ZWxsIGJlY2F1c2UgaW1hZ2UgYW5kIHZpZGVvIFN3aW4gc2hhcmUgYXJjaGl0ZWN0dXJhbCBkZXNpZ24uIFRoaXJkLCBoaWVyYXJjaGljYWwgZmVhdHVyZXMgYXQgbXVsdGlwbGUgc2NhbGVzIG1ha2UgVmlkZW8gU3dpbiBkaXJlY3RseSB1c2FibGUgZm9yIGRlbnNlIHByZWRpY3Rpb24gd2l0aG91dCBhZGRpdGlvbmFsIGFkYXB0b3IgbW9kdWxlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJkZWYgbG9hZF92aWRlb19zd2luX2Zyb21faW1hZ2UoaW1hZ2VfY2twdCwgbnVtX2ZyYW1lcz0xNik6XG4gICAgbW9kZWwgPSBWaWRlb1N3aW5UcmFuc2Zvcm1lcihcbiAgICAgICAgZW1iZWRfZGltPTEyOCwgZGVwdGhzPVsyLCAyLCAxOCwgMl0sXG4gICAgICAgIG51bV9oZWFkcz1bNCwgOCwgMTYsIDMyXSwgd2luZG93X3NpemU9KDgsIDcsIDcpXG4gICAgKVxuICAgIHN0YXRlID0gdG9yY2gubG9hZChpbWFnZV9ja3B0LCBtYXBfbG9jYXRpb249XHUwMDI3Y3B1XHUwMDI3KVtcdTAwMjdtb2RlbFx1MDAyN11cbiAgICAjIEluZmxhdGUgMkQgcGF0Y2ggZW1iZWQgKEMsIDMsIDQsIDQpIC1cdTAwM2UgM0QgKEMsIDMsIDIsIDQsIDQpXG4gICAgcGUgPSBzdGF0ZVtcdTAwMjdwYXRjaF9lbWJlZC5wcm9qLndlaWdodFx1MDAyN10udW5zcXVlZXplKDIpXG4gICAgc3RhdGVbXHUwMDI3cGF0Y2hfZW1iZWQucHJvai53ZWlnaHRcdTAwMjddID0gcGUucmVwZWF0KDEsIDEsIDIsIDEsIDEpIC8gMlxuICAgIG1vZGVsLmxvYWRfc3RhdGVfZGljdChzdGF0ZSwgc3RyaWN0PUZhbHNlKVxuICAgIHJldHVybiBtb2RlbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmluZS10dW5pbmcgZnJvbSBpbWFnZSBTd2luIHJlcXVpcmVzIHR3byBtb2RpZmljYXRpb25zOiByZXBsYWNlIDJEIHBvc2l0aW9uIGVtYmVkZGluZ3Mgd2l0aCBpbnRlcnBvbGF0ZWQgM0QgZW1iZWRkaW5ncywgYW5kIGFkYXB0IHRoZSBwYXRjaCBlbWJlZGRpbmcgdG8gYWNjZXB0IFQgZnJhbWVzLiBUaGUgdGVtcG9yYWwgd2luZG93IHNpemUgaXMgc2V0IHRvIDIgcmVnYXJkbGVzcyBvZiBob3cgbWFueSBmcmFtZXMgYXJlIHVzZWQgYXQgZmluZS10dW5lIHRpbWUuIEtpbmV0aWNzIGZpbmUtdHVuaW5nIHVzZXMgYSAzRCByYW5kb20gY3JvcCBvZiAxNsOXMjI0w5cyMjQsIHdlaWdodCBkZWNheSAwLjA1LCBhbmQgY29zaW5lIGxlYXJuaW5nIHJhdGUgZGVjYXkgb3ZlciAzMCB0cmFpbmluZyBlcG9jaHMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwiY29udGVudCI6IlZpZGVvIFN3aW4gZXh0ZW5kcyBpbWFnZSBTd2luIGJ5IGFkZGluZyBhIHRlbXBvcmFsIHdpbmRvdyBkaW1lbnNpb24gKHNpemUgMikgYW5kIHNoaWZ0aW5nIGJ5ICgtMSwgLTMsIC0zKSBpbiAoVCwgSCwgVykuIFRoZSB0ZW1wb3JhbCB3aW5kb3cgb2YgMiBpcyBpbnRlbnRpb25hbGx5IHNtYWxsIOKAlCBtb3N0IG1vdGlvbiBpcyBsb2NhbCBpbiB0aW1lLCBhbmQgc21hbGwgd2luZG93cyBrZWVwIEZMT1BzIGxpbmVhciBpbiB2aWRlbyBsZW5ndGguIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiUHJldHJhaW4iLCJLaW5ldGljcy00MDAgJSIsIktpbmV0aWNzLTYwMCAlIiwiUGFyYW1zIChNKSIsIkZMT1BzIChHKSJdLCJyb3dzIjpbWyJUaW1lU2Zvcm1lciIsIkltYWdlTmV0LTIxSyIsIjc4LjAiLCI3OS43IiwiMTIxIiwiNTkwIl0sWyJWaVZpVCIsIkltYWdlTmV0LTIxSyIsIjgwLjciLCI4My4wIiwiMzA4IiwiMzk4MSJdLFsiVmlkZW8gU3dpbi1UIiwiSW1hZ2VOZXQtMUsiLCI3OC44IiwiODAuNiIsIjI4IiwiODgiXSxbIlZpZGVvIFN3aW4tQiIsIkltYWdlTmV0LTIxSyIsIjgyLjciLCI4NC4wIiwiODgiLCIyODIiXSxbIlZpZGVvIFN3aW4tTCIsIkltYWdlTmV0LTIxSyIsIjg0LjYiLCI4Ni4xIiwiMTk3IiwiNjA0Il1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaW5kb3cgYXR0ZW50aW9uIGlzIHRoZSBrZXkgdG8gc2NhbGFibGUgdmlkZW8gdHJhbnNmb3JtZXJzLiBCeSByZXN0cmljdGluZyBzZWxmLWF0dGVudGlvbiB0byBsb2NhbCBzcGF0aW90ZW1wb3JhbCB3aW5kb3dzICgyw5c3w5c3KSwgVmlkZW8gU3dpbiBhY2hpZXZlcyBsaW5lYXIgY29tcGxleGl0eSBpbiB2aWRlbyBsZW5ndGggd2hpbGUgbWFpbnRhaW5pbmcgY29tcGV0aXRpdmUgYWNjdXJhY3kuIFRoZSBzaGlmdGVkLXdpbmRvdyBtZWNoYW5pc20gZW5hYmxlcyBjcm9zcy13aW5kb3cgY29tbXVuaWNhdGlvbiB3aXRob3V0IHF1YWRyYXRpYyBjb3N0LCBtYWtpbmcgVmlkZW8gU3dpbiBwcmFjdGljYWwgZm9yIGNsaXBzIHVwIHRvIDMyIGZyYW1lcyBvbiBhIHNpbmdsZSBHUFUgYXQgaW5mZXJlbmNlIHRpbWUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcmV0cmFpbmluZyBkYXRhc2V0IHF1YWxpdHkgZHJpdmVzIG1vc3Qgb2YgdGhlIGFjY3VyYWN5IGdhcCBiZXR3ZWVuIHZhcmlhbnRzLiBWaWRlbyBTd2luLUwgcHJldHJhaW5lZCBvbiBJbWFnZU5ldC0yMUsgcmVhY2hlcyA4NC42JSBvbiBLaW5ldGljcy00MDA7IHRoZSBzYW1lIGFyY2hpdGVjdHVyZSBmcm9tIEltYWdlTmV0LTFLIGxvc2VzIDIgdG8gMyUuIExhcmdlciBwcmV0cmFpbmluZyBkYXRhc2V0cyBpbXByb3ZlIGxvdy1sZXZlbCBmZWF0dXJlIHF1YWxpdHkgYW5kIHJlZ3VsYXJpemUgYXR0ZW50aW9uIGhlYWRzLCByZWR1Y2luZyBvdmVyZml0dGluZyB0byBLaW5ldGljcyB0cmFpbmluZyBjbGlwcyB0aGF0IGFyZSBvZnRlbiB2aXN1YWxseSBzaW1pbGFyIHdpdGhpbiBhY3Rpb24gY2F0ZWdvcmllcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZpZGVvIFN3aW4gZXN0YWJsaXNoZWQgdGhhdCBwdXJlIHRyYW5zZm9ybWVyIGFyY2hpdGVjdHVyZXMgY2FuIG1hdGNoIGFuZCBleGNlZWQgM0QgQ05OcyBvbiBzdGFuZGFyZCB2aWRlbyBiZW5jaG1hcmtzLiBTdWJzZXF1ZW50IG1vZGVscyDigJQgVmlkZW9NQUUsIEludGVyblZpZGVvLCBVTVQg4oCUIGJ1aWxkIGRpcmVjdGx5IG9uIHRoaXMgZm91bmRhdGlvbiwgdXNpbmcgbWFza2VkIGF1dG9lbmNvZGluZyBwcmV0cmFpbmluZyBvbiBWaWRlbyBTd2luLXN0eWxlIGFyY2hpdGVjdHVyZXMuIFRoZSBzcGF0aW90ZW1wb3JhbCBsb2NhbGl0eSBpbmR1Y3RpdmUgYmlhcyBvZiB3aW5kb3dlZCBhdHRlbnRpb24gcmVtYWlucyB2YWx1YWJsZSBldmVuIGFzIG1vZGVsIHNjYWxlIGFuZCBwcmV0cmFpbmluZyBkYXRhIGNvbnRpbnVlIHRvIGdyb3cuIn1d"
---
# Video Swin Transformer: Spatiotemporal Shifted Window Attention

## Overview

Video Swin Transformer (Liu et al., 2022) adapts the image Swin Transformer for video by extending its local window attention to three dimensions: temporal, height, and width. Each attention layer operates within small non-overlapping spatiotemporal windows, keeping complexity linear in video length. The shifted-window mechanism connects adjacent windows across layers to achieve global receptive fields efficiently.

Image Swin uses 2D shifted windows of size 7×7. Video Swin adds a temporal window of size 2, creating 2×7×7 spatiotemporal cubes. The patch embedding absorbs frames as tokens: a T×H×W video becomes T×(H/4)×(W/4) tokens after the initial 2×4×4 patch partition. Stage-wise patch merging progressively reduces spatial and temporal resolution, building a hierarchical feature pyramid for downstream tasks.

## 3D Shifted Windows

Standard 3D self-attention is O((T·H·W)²), infeasible for even short clips. Video Swin restricts attention to local 3D windows of size Wt×Wh×Ww (default 2×7×7), giving O(T·H·W·Wt·Wh·Ww) complexity — linear in video length. Within each window, multi-head self-attention captures local spatiotemporal dependencies; between-window information flows via window shifts in alternating transformer blocks.

```
from einops import rearrange

def window_partition_3d(x, window_size=(2, 7, 7)):
    """Partition (B,T,H,W,C) into (num_windows*B, Wt*Wh*Ww, C)."""
    Wt, Wh, Ww = window_size
    B, T, H, W, C = x.shape
    x = x.view(B, T//Wt, Wt, H//Wh, Wh, W//Ww, Ww, C)
    windows = x.permute(0, 1, 3, 5, 2, 4, 6, 7).contiguous()
    windows = windows.view(-1, Wt * Wh * Ww, C)
    return windows  # (num_windows * B, tokens_per_window, C)
```

```
def shifted_window_attn_3d(x, win_size, shift, mask):
    B, T, H, W, C = x.shape
    if any(s > 0 for s in shift):
        x = torch.roll(
            x,
            shifts=(-shift[0], -shift[1], -shift[2]),
            dims=(1, 2, 3)
        )
    wins = window_partition_3d(x, win_size)
    out  = window_msa(wins, mask=mask)
    x    = window_reverse_3d(out, win_size, T, H, W)
    if any(s > 0 for s in shift):
        x = torch.roll(
            x, shifts=(shift[0], shift[1], shift[2]), dims=(1, 2, 3)
        )
    return x
```

The cyclic shift for boundary handling is identical to image Swin but extended to 3D: after rolling the tensor by (-1, -3, -3) in (T, H, W), windows near boundaries contain tokens from opposite ends of the volume. An attention mask zeroes out cross-boundary attention scores, ensuring shifted-window attention is equivalent to partitioning the cyclically shifted tensor into proper non-overlapping windows.

## Spatiotemporal Locality

Spatiotemporal locality is well-justified for video: adjacent frames share most content, and local object motion rarely spans more than a few pixels per frame. A temporal window of size 2 covers two consecutive frames — sufficient to capture inter-frame motion at typical video frame rates. Larger temporal windows increase FLOPs quadratically within the window and show diminishing accuracy returns on standard benchmarks.

Compared to full spatiotemporal attention (used in TimeSformer space-time mode), Video Swin's window attention reduces FLOPs by roughly 10 to 50× on 8-frame clips. TimeSformer uses divided space-time attention — separate spatial and temporal stages — also achieving linear complexity, but Video Swin's joint spatiotemporal windows capture cross-modal correlations more directly within each attention layer.

## Temporal Downsampling

Video Swin uses four stages with spatial patch merging after stages 1, 2, and 3. Spatial resolution drops from H/4 to H/8, H/16, and H/32. Temporal patch merging can be applied similarly, halving temporal resolution at selected stages. This creates a feature pyramid reusable for dense downstream tasks like action segmentation, video object detection, and spatiotemporal dense prediction with minimal adaptation.

```
import torch.nn as nn

class TemporalPatchMerging(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.norm = nn.LayerNorm(2 * dim)
        self.proj = nn.Linear(2 * dim, dim, bias=False)

    def forward(self, x):  # x: (B, T, H, W, C)
        x0 = x[:, 0::2]   # even-indexed frames
        x1 = x[:, 1::2]   # odd-indexed frames
        x  = torch.cat([x0, x1], dim=-1)  # (B, T//2, H, W, 2C)
        return self.proj(self.norm(x))    # (B, T//2, H, W, C)
```

The temporal resolution schedule depends on the task: for short-clip classification using 8 or 16 frames, temporal merging is typically disabled to preserve all temporal tokens. For longer videos, temporal merging after stage 1 or 2 reduces memory footprint. The Video Swin-B model uses window sizes (8, 7, 7) at later stages where temporal resolution has been reduced by earlier patch merging layers.

## Comparison to 3D CNNs

Video Swin outperforms 3D CNNs in three key ways. First, attention is data-adaptive: window attention weights depend on content, unlike fixed convolution kernels. Second, ImageNet-21K pretraining transfers well because image and video Swin share architectural design. Third, hierarchical features at multiple scales make Video Swin directly usable for dense prediction without additional adaptor modules.

```
def load_video_swin_from_image(image_ckpt, num_frames=16):
    model = VideoSwinTransformer(
        embed_dim=128, depths=[2, 2, 18, 2],
        num_heads=[4, 8, 16, 32], window_size=(8, 7, 7)
    )
    state = torch.load(image_ckpt, map_location='cpu')['model']
    # Inflate 2D patch embed (C, 3, 4, 4) -> 3D (C, 3, 2, 4, 4)
    pe = state['patch_embed.proj.weight'].unsqueeze(2)
    state['patch_embed.proj.weight'] = pe.repeat(1, 1, 2, 1, 1) / 2
    model.load_state_dict(state, strict=False)
    return model
```

Fine-tuning from image Swin requires two modifications: replace 2D position embeddings with interpolated 3D embeddings, and adapt the patch embedding to accept T frames. The temporal window size is set to 2 regardless of how many frames are used at fine-tune time. Kinetics fine-tuning uses a 3D random crop of 16×224×224, weight decay 0.05, and cosine learning rate decay over 30 training epochs.

> **info**: Video Swin extends image Swin by adding a temporal window dimension (size 2) and shifting by (-1, -3, -3) in (T, H, W). The temporal window of 2 is intentionally small — most motion is local in time, and small windows keep FLOPs linear in video length.

| Model | Pretrain | Kinetics-400 % | Kinetics-600 % | Params (M) | FLOPs (G) |
| --- | --- | --- | --- | --- | --- |
| TimeSformer | ImageNet-21K | 78.0 | 79.7 | 121 | 590 |
| ViViT | ImageNet-21K | 80.7 | 83.0 | 308 | 3981 |
| Video Swin-T | ImageNet-1K | 78.8 | 80.6 | 28 | 88 |
| Video Swin-B | ImageNet-21K | 82.7 | 84.0 | 88 | 282 |
| Video Swin-L | ImageNet-21K | 84.6 | 86.1 | 197 | 604 |

## Key Takeaways

Window attention is the key to scalable video transformers. By restricting self-attention to local spatiotemporal windows (2×7×7), Video Swin achieves linear complexity in video length while maintaining competitive accuracy. The shifted-window mechanism enables cross-window communication without quadratic cost, making Video Swin practical for clips up to 32 frames on a single GPU at inference time.

Pretraining dataset quality drives most of the accuracy gap between variants. Video Swin-L pretrained on ImageNet-21K reaches 84.6% on Kinetics-400; the same architecture from ImageNet-1K loses 2 to 3%. Larger pretraining datasets improve low-level feature quality and regularize attention heads, reducing overfitting to Kinetics training clips that are often visually similar within action categories.

Video Swin established that pure transformer architectures can match and exceed 3D CNNs on standard video benchmarks. Subsequent models — VideoMAE, InternVideo, UMT — build directly on this foundation, using masked autoencoding pretraining on Video Swin-style architectures. The spatiotemporal locality inductive bias of windowed attention remains valuable even as model scale and pretraining data continue to grow.

