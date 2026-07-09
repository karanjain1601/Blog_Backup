---
title: "Gradient Boosting — Additive Model and Stage-Wise Fitting"
slug: "gradient-boosting"
description: "How gradient boosting builds an additive model by fitting new trees to the negative gradient of the loss, functional gradient descent in function space, shrinkage, and the bias-variance contrast with bagging."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFkZGl0aXZlIE1vZGVsIGFuZCBTdGFnZS1XaXNlIEZpdHRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdyYWRpZW50IGJvb3N0aW5nIGJ1aWxkcyBhbiBhZGRpdGl2ZSBtb2RlbCBGX00oeCkgPSBGXzAoeCkgKyDOo197bT0xfV57TX0gzrfCt2hfbSh4KSB3aGVyZSBlYWNoIGhfbSBpcyBhIHdlYWsgbGVhcm5lciAodHlwaWNhbGx5IGEgc2hhbGxvdyB0cmVlKSBhbmQgzrcgaXMgdGhlIGxlYXJuaW5nIHJhdGUgKHNocmlua2FnZSkuIFVubGlrZSBuZXVyYWwgbmV0d29ya3MgdGhhdCBhZGp1c3QgYWxsIHBhcmFtZXRlcnMgc2ltdWx0YW5lb3VzbHksIHN0YWdlLXdpc2UgZml0dGluZyBpcyBncmVlZHkg4oCUIGVhY2ggbmV3IHRyZWUgaXMgYWRkZWQgdG8gbWluaW1pc2UgdGhlIGN1cnJlbnQgbG9zcyB3aXRob3V0IG1vZGlmeWluZyBwcmV2aW91cyB0cmVlcy4gVGhpcyBncmVlZHksIG5vbi1wYXJhbWV0cmljIGFwcHJvYWNoIGlzIHdoYXQgbWFrZXMgZ3JhZGllbnQgYm9vc3Rpbmcgc28gZmxleGlibGU6IGFueSBkaWZmZXJlbnRpYWJsZSBsb3NzIGZ1bmN0aW9uIGNhbiBiZSBvcHRpbWlzZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR3JhZGllbnQgQm9vc3RpbmcgYXMgRnVuY3Rpb25hbCBHcmFkaWVudCBEZXNjZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBncmFkaWVudCBkZXNjZW50IG1vdmVzIHBhcmFtZXRlcnMgzrggaW4gdGhlIGRpcmVjdGlvbiDiiJLiiIdfzrggTC4gR3JhZGllbnQgYm9vc3RpbmcgaW5zdGVhZCBkb2VzIGdyYWRpZW50IGRlc2NlbnQgaW4gZnVuY3Rpb24gc3BhY2U6IHRoZSBuZWdhdGl2ZSBncmFkaWVudCDiiJLiiIJML+KIgkYgZXZhbHVhdGVkIGF0IHRoZSBjdXJyZW50IHByZWRpY3Rpb25zIHRlbGxzIHVzIHRoZSBkaXJlY3Rpb24gdG8gbW92ZSB0aGUgZnVuY3Rpb24gRi4gRm9yIE1TRSBsb3NzIEwgPSAoMS8yKSh5IOKIkiBGKcKyLCB0aGUgbmVnYXRpdmUgZ3JhZGllbnQgaXMgeSDiiJIgRiDigJQgdGhlIHJlc2lkdWFsLiBTbyByZXNpZHVhbCBib29zdGluZyBpcyBhIHNwZWNpYWwgY2FzZSBvZiBncmFkaWVudCBib29zdGluZy4gRm9yIGxvZy1sb3NzIChiaW5hcnkgY2xhc3NpZmljYXRpb24pIEwgPSDiiJJ5IGxvZyBwIOKIkiAoMeKIknkpIGxvZygx4oiScCksIHRoZSBuZWdhdGl2ZSBncmFkaWVudCBpcyB5IOKIkiBwIHdoZXJlIHAgPSDPgyhGKS4gRWFjaCBuZXcgdHJlZSBpcyBmaXR0ZWQgdG8gdGhlc2UgcHNldWRvLXJlc2lkdWFscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4udHJlZSBpbXBvcnQgRGVjaXNpb25UcmVlUmVncmVzc29yXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfcmVncmVzc2lvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IG1lYW5fc3F1YXJlZF9lcnJvclxuXG5jbGFzcyBHcmFkaWVudEJvb3N0aW5nTVNFOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2VzdGltYXRvcnM9MTAwLCBsZWFybmluZ19yYXRlPTAuMSwgbWF4X2RlcHRoPTMpOlxuICAgICAgICBzZWxmLm4gPSBuX2VzdGltYXRvcnM7IHNlbGYubHIgPSBsZWFybmluZ19yYXRlXG4gICAgICAgIHNlbGYubWF4X2RlcHRoID0gbWF4X2RlcHRoOyBzZWxmLnRyZWVzID0gW107IHNlbGYuRjAgPSBOb25lXG5cbiAgICBkZWYgZml0KHNlbGYsIFgsIHkpOlxuICAgICAgICBzZWxmLkYwID0geS5tZWFuKCkgICAgICAgICAgICMgaW5pdGlhbCBwcmVkaWN0aW9uID0gZ2xvYmFsIG1lYW5cbiAgICAgICAgRiA9IG5wLmZ1bGwobGVuKHkpLCBzZWxmLkYwKVxuICAgICAgICBmb3IgXyBpbiByYW5nZShzZWxmLm4pOlxuICAgICAgICAgICAgcmVzaWR1YWxzID0geSAtIEYgICAgICAgICMgbmVnYXRpdmUgZ3JhZGllbnQgb2YgTVNFXG4gICAgICAgICAgICB0cmVlID0gRGVjaXNpb25UcmVlUmVncmVzc29yKG1heF9kZXB0aD1zZWxmLm1heF9kZXB0aClcbiAgICAgICAgICAgIHRyZWUuZml0KFgsIHJlc2lkdWFscylcbiAgICAgICAgICAgIEYgKz0gc2VsZi5sciAqIHRyZWUucHJlZGljdChYKVxuICAgICAgICAgICAgc2VsZi50cmVlcy5hcHBlbmQodHJlZSlcbiAgICAgICAgcmV0dXJuIHNlbGZcblxuICAgIGRlZiBwcmVkaWN0KHNlbGYsIFgpOlxuICAgICAgICBwcmVkID0gbnAuZnVsbChYLnNoYXBlWzBdLCBzZWxmLkYwKVxuICAgICAgICBmb3IgdHJlZSBpbiBzZWxmLnRyZWVzOlxuICAgICAgICAgICAgcHJlZCArPSBzZWxmLmxyICogdHJlZS5wcmVkaWN0KFgpXG4gICAgICAgIHJldHVybiBwcmVkXG5cblgsIHkgPSBtYWtlX3JlZ3Jlc3Npb24obl9zYW1wbGVzPTYwMCwgbl9mZWF0dXJlcz0xMCwgbm9pc2U9MjAsIHJhbmRvbV9zdGF0ZT00MilcblhfdHIsIFhfdGUsIHlfdHIsIHlfdGUgPSB0cmFpbl90ZXN0X3NwbGl0KFgsIHksIHRlc3Rfc2l6ZT0wLjIsIHJhbmRvbV9zdGF0ZT00MilcbmdiID0gR3JhZGllbnRCb29zdGluZ01TRShuX2VzdGltYXRvcnM9MTUwLCBsZWFybmluZ19yYXRlPTAuMSwgbWF4X2RlcHRoPTMpXG5nYi5maXQoWF90ciwgeV90cilcbnJtc2UgPSBucC5zcXJ0KG1lYW5fc3F1YXJlZF9lcnJvcih5X3RlLCBnYi5wcmVkaWN0KFhfdGUpKSlcbnByaW50KGZcdTAwMjdDdXN0b20gR0IgUk1TRToge3Jtc2U6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb3NzIEZ1bmN0aW9ucyBhbmQgVGhlaXIgR3JhZGllbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHcmFkaWVudCBib29zdGluZ1x1MDAyN3MgcG93ZXIgY29tZXMgZnJvbSBwbHVnZ2luZyBpbiBhbnkgZGlmZmVyZW50aWFibGUgbG9zcy4gTVNFIGxvc3MgZ2l2ZXMgZ3JhZGllbnQgPSB5IOKIkiBGIChyZXNpZHVhbHMpLiBMb2ctbG9zcyBmb3IgYmluYXJ5IGNsYXNzaWZpY2F0aW9uIGdpdmVzIGdyYWRpZW50ID0geSDiiJIgz4MoRikgd2hlcmUgz4MgaXMgdGhlIHNpZ21vaWQg4oCUIHRyZWVzIGFyZSBmaXR0ZWQgdG8gdGhlIGRpZmZlcmVuY2UgYmV0d2VlbiB0cnVlIGxhYmVscyBhbmQgY3VycmVudCBwcmVkaWN0ZWQgcHJvYmFiaWxpdGllcy4gSHViZXIgbG9zcyAocm9idXN0IHJlZ3Jlc3Npb24pIGdpdmVzIGdyYWRpZW50IHRoYXQgaXMgbGluZWFyIGZvciBzbWFsbCByZXNpZHVhbHMgYW5kIGJvdW5kZWQgZm9yIG91dGxpZXJzLiBRdWFudGlsZSBsb3NzIGVuYWJsZXMgcHJlZGljdGlvbiBpbnRlcnZhbHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnRyZWUgaW1wb3J0IERlY2lzaW9uVHJlZVJlZ3Jlc3NvclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2JyZWFzdF9jYW5jZXJcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBsb2dfbG9zc1xuXG5kZWYgc2lnbW9pZCh4KTpcbiAgICByZXR1cm4gMS4wIC8gKDEuMCArIG5wLmV4cCgtbnAuY2xpcCh4LCAtMTAsIDEwKSkpXG5cblgsIHkgPSBsb2FkX2JyZWFzdF9jYW5jZXIocmV0dXJuX1hfeT1UcnVlKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMiwgcmFuZG9tX3N0YXRlPTQyKVxuXG5GID0gbnAuemVyb3MobGVuKHlfdHIpKSAgICAgIyBzdGFydCBhdCBGPTAgKHNpZ21vaWQgZ2l2ZXMgcD0wLjUpXG50cmVlcywgbHIgPSBbXSwgMC4xXG5cbmZvciBtIGluIHJhbmdlKDEwMCk6XG4gICAgcCA9IHNpZ21vaWQoRilcbiAgICBncmFkaWVudCA9IHlfdHIgLSBwICAgICAgICMgbmVnYXRpdmUgZ3JhZGllbnQgb2YgbG9nLWxvc3NcbiAgICB0cmVlID0gRGVjaXNpb25UcmVlUmVncmVzc29yKG1heF9kZXB0aD0zKVxuICAgIHRyZWUuZml0KFhfdHIsIGdyYWRpZW50KVxuICAgIEYgKz0gbHIgKiB0cmVlLnByZWRpY3QoWF90cilcbiAgICB0cmVlcy5hcHBlbmQodHJlZSlcblxuIyBFdmFsdWF0ZSBvbiB0ZXN0IHNldFxuRl90ZSA9IG5wLnplcm9zKGxlbih5X3RlKSlcbmZvciB0cmVlIGluIHRyZWVzOlxuICAgIEZfdGUgKz0gbHIgKiB0cmVlLnByZWRpY3QoWF90ZSlcblxucHJlZHMgPSAoc2lnbW9pZChGX3RlKSBcdTAwM2UgMC41KS5hc3R5cGUoaW50KVxucHJpbnQoZlx1MDAyN0N1c3RvbSBsb2ctbG9zcyBHQiBhY2N1cmFjeTogeyhwcmVkcyA9PSB5X3RlKS5tZWFuKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdMb2ctbG9zcyBvbiB0ZXN0IHNldDogICAgICAgIHtsb2dfbG9zcyh5X3RlLCBzaWdtb2lkKEZfdGUpKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IFJlc2lkdWFscyBFcXVhbCBOZWdhdGl2ZSBHcmFkaWVudCBmb3IgTVNFIiwiY29udGVudCI6Ik1TRSBsb3NzIGlzIEwoeSwgRikgPSAoMS8yKSh5IOKIkiBGKcKyLiBJdHMgZGVyaXZhdGl2ZSB3aXRoIHJlc3BlY3QgdG8gRiBpcyDiiIJML+KIgkYgPSBGIOKIkiB5ID0g4oiSKHkg4oiSIEYpLiBTbyB0aGUgbmVnYXRpdmUgZ3JhZGllbnQgaXMgeSDiiJIgRiwgd2hpY2ggaXMgZXhhY3RseSB0aGUgcmVzaWR1YWwuIEZpdHRpbmcgYSB0cmVlIHRvIHJlc2lkdWFscyBhbmQgYWRkaW5nIGl0IHRvIEYgaXMgZ3JhZGllbnQgZGVzY2VudCBpbiBmdW5jdGlvbiBzcGFjZSDigJQgcmVzaWR1YWwgYm9vc3Rpbmcgd2FzIGludmVudGVkIGJlZm9yZSB0aGUgZ3JhZGllbnQgaW50ZXJwcmV0YXRpb24gd2FzIGZvcm1hbGlzZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50Ijoic2tsZWFybiBHcmFkaWVudEJvb3N0aW5nQ2xhc3NpZmllciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50Ijoic2tsZWFyblx1MDAyN3MgR3JhZGllbnRCb29zdGluZ0NsYXNzaWZpZXIgaW1wbGVtZW50cyB0aGUgb3JpZ2luYWwgRnJpZWRtYW4gKDIwMDEpIHN0b2NoYXN0aWMgZ3JhZGllbnQgYm9vc3RpbmcgYWxnb3JpdGhtLiBLZXkgcGFyYW1ldGVyczogbl9lc3RpbWF0b3JzIChudW1iZXIgb2YgdHJlZXMpLCBsZWFybmluZ19yYXRlIChzaHJpbmthZ2UgzrcpLCBtYXhfZGVwdGggKHR5cGljYWwgMy01IGZvciBib29zdGluZyksIHN1YnNhbXBsZSAoc3RvY2hhc3RpYyBHQiDigJQgdXNlIDAuNS0wLjggdG8gYWRkIHZhcmlhbmNlIHJlZHVjdGlvbiBhbG9uZ3NpZGUgYmlhcyByZWR1Y3Rpb24pLiBUaGUgZGV2aWFuY2UgKGxvZy1sb3NzKSBhbmQgZXhwb25lbnRpYWwgKEFkYUJvb3N0KSBsb3NzIGZ1bmN0aW9ucyBhcmUgYm90aCBzdXBwb3J0ZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gc2tsZWFybi5lbnNlbWJsZSBpbXBvcnQgR3JhZGllbnRCb29zdGluZ0NsYXNzaWZpZXJcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9icmVhc3RfY2FuY2VyXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCB0cmFpbl90ZXN0X3NwbGl0LCBjcm9zc192YWxfc2NvcmVcbmltcG9ydCBudW1weSBhcyBucFxuXG5YLCB5ID0gbG9hZF9icmVhc3RfY2FuY2VyKHJldHVybl9YX3k9VHJ1ZSlcblhfdHIsIFhfdGUsIHlfdHIsIHlfdGUgPSB0cmFpbl90ZXN0X3NwbGl0KFgsIHksIHRlc3Rfc2l6ZT0wLjIsIHJhbmRvbV9zdGF0ZT00MilcblxuZ2IgPSBHcmFkaWVudEJvb3N0aW5nQ2xhc3NpZmllcihcbiAgICBuX2VzdGltYXRvcnM9MjAwLFxuICAgIGxlYXJuaW5nX3JhdGU9MC4wNSwgICAgIyBzaHJpbmthZ2Ug4oCUIHNtYWxsZXIgPSBtb3JlIHJlZ3VsYXJpc2F0aW9uXG4gICAgbWF4X2RlcHRoPTMsICAgICAgICAgICAjIHNoYWxsb3cgdHJlZXMgcHJlZmVycmVkIGZvciBib29zdGluZ1xuICAgIHN1YnNhbXBsZT0wLjgsICAgICAgICAgIyBzdG9jaGFzdGljIEdCOiA4MCUgb2YgZGF0YSBwZXIgdHJlZVxuICAgIG1pbl9zYW1wbGVzX2xlYWY9NSxcbiAgICByYW5kb21fc3RhdGU9NDJcbilcbmdiLmZpdChYX3RyLCB5X3RyKVxuXG5wcmludChmXHUwMDI3VHJhaW46IHtnYi5zY29yZShYX3RyLCB5X3RyKTouNGZ9ICBUZXN0OiB7Z2Iuc2NvcmUoWF90ZSwgeV90ZSk6LjRmfVx1MDAyNylcbmN2ID0gY3Jvc3NfdmFsX3Njb3JlKGdiLCBYLCB5LCBjdj01KVxucHJpbnQoZlx1MDAyNzUtZm9sZCBDVjoge2N2Lm1lYW4oKTouNGZ9ICsvLSB7Y3Yuc3RkKCk6LjRmfVx1MDAyNylcbnRvcDMgPSBnYi5mZWF0dXJlX2ltcG9ydGFuY2VzXy5hcmdzb3J0KClbOjotMV1bOjNdXG5wcmludChmXHUwMDI3VG9wLTMgZmVhdHVyZXMgYnkgTURJOiB7dG9wM31cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGVhcm5pbmcgUmF0ZSB2cyBuX2VzdGltYXRvcnMgVHJhZGUtb2ZmIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaHJpbmthZ2UgKHNtYWxsIGxlYXJuaW5nIHJhdGUgzrcpIGlzIHRoZSBtb3N0IGVmZmVjdGl2ZSByZWd1bGFyaXNlciBpbiBncmFkaWVudCBib29zdGluZy4gQSBzbWFsbGVyIM63IHJlcXVpcmVzIG1vcmUgdHJlZXMgdG8gZml0IHRoZSB0cmFpbmluZyBkYXRhIOKAlCB0aGUgcmVsYXRpb25zaGlwIGlzIHJvdWdobHkgbl9lc3RpbWF0b3JzIOKInSAxL863LiBUaGlzIG1lYW5zIGEgbW9kZWwgd2l0aCBscj0wLjA1IGFuZCA0MDAgdHJlZXMgdGVuZHMgdG8gbWF0Y2ggbHI9MC4xIGFuZCAyMDAgdHJlZXMgaW4gYWNjdXJhY3kgd2hpbGUgYmVpbmcgbW9yZSByb2J1c3QgdG8gb3ZlcmZpdHRpbmcuIFRoZSBjb21wdXRhdGlvbmFsIGNvc3QgaXMgaWRlbnRpY2FsLiBGaW5kaW5nIHRoZSByaWdodCBuX2VzdGltYXRvcnMgZm9yIGEgZ2l2ZW4gbHIgaXMgYmVzdCBkb25lIHdpdGggZWFybHkgc3RvcHBpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmVuc2VtYmxlIGltcG9ydCBHcmFkaWVudEJvb3N0aW5nQ2xhc3NpZmllclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2JyZWFzdF9jYW5jZXJcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcblxuWCwgeSA9IGxvYWRfYnJlYXN0X2NhbmNlcihyZXR1cm5fWF95PVRydWUpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4yLCByYW5kb21fc3RhdGU9NDIpXG5cbmNvbmZpZ3MgPSBbKDAuNTAsIDUwKSwgKDAuMTAsIDIwMCksICgwLjA1LCA0MDApLCAoMC4wMSwgMTAwMCldXG5yZXN1bHRzID0gW11cbmZvciBsciwgbl9lc3QgaW4gY29uZmlnczpcbiAgICBnYiA9IEdyYWRpZW50Qm9vc3RpbmdDbGFzc2lmaWVyKFxuICAgICAgICBuX2VzdGltYXRvcnM9bl9lc3QsIGxlYXJuaW5nX3JhdGU9bHIsIG1heF9kZXB0aD0zLCByYW5kb21fc3RhdGU9NDIpXG4gICAgZ2IuZml0KFhfdHIsIHlfdHIpXG4gICAgcmVzdWx0cy5hcHBlbmQoe1x1MDAyN2xyXHUwMDI3OiBsciwgXHUwMDI3blx1MDAyNzogbl9lc3QsXG4gICAgICAgICAgICAgICAgICAgIFx1MDAyN3RyYWluXHUwMDI3OiBnYi5zY29yZShYX3RyLCB5X3RyKSxcbiAgICAgICAgICAgICAgICAgICAgXHUwMDI3dGVzdFx1MDAyNzogIGdiLnNjb3JlKFhfdGUsIHlfdGUpfSlcbiAgICBwcmludChmXHUwMDI3bHI9e2xyOjUuMmZ9ICBuPXtuX2VzdDo0ZH0gIFx1MDAyN1xuICAgICAgICAgIGZcdTAwMjd0cmFpbj17cmVzdWx0c1stMV1bXCJ0cmFpblwiXTouNGZ9ICB0ZXN0PXtyZXN1bHRzWy0xXVtcInRlc3RcIl06LjRmfVx1MDAyNylcblxuYmVzdCA9IG1heChyZXN1bHRzLCBrZXk9bGFtYmRhIHI6IHJbXHUwMDI3dGVzdFx1MDAyN10pXG5wcmludChmXHUwMDI3QmVzdCBjb25maWc6IGxyPXtiZXN0W1wibHJcIl19LCBuX2VzdGltYXRvcnM9e2Jlc3RbXCJuXCJdfSwgdGVzdD17YmVzdFtcInRlc3RcIl06LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCYWdnaW5nIHZzIEJvb3N0aW5nIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFzcGVjdCIsIkJhZ2dpbmcgKFJhbmRvbSBGb3Jlc3QpIiwiQm9vc3RpbmcgKEdyYWRpZW50IEJvb3N0aW5nKSJdLCJyb3dzIjpbWyJQcmltYXJ5IGVmZmVjdCIsIlJlZHVjZXMgdmFyaWFuY2UiLCJSZWR1Y2VzIGJpYXMiXSxbIlRyZWUgZGVwdGgiLCJEZWVwICh1bmNvbnN0cmFpbmVkKSIsIlNoYWxsb3cgKGRlcHRoIDMtNSB0eXBpY2FsKSJdLFsiVHJlZSB0cmFpbmluZyIsIlBhcmFsbGVsIChpbmRlcGVuZGVudCkiLCJTZXF1ZW50aWFsIChkZXBlbmRlbnQpIl0sWyJPdmVyZml0dGluZyByaXNrIiwiTG93IChhdmVyYWdpbmcgcmVndWxhcmlzZXMpIiwiSGlnaCBpZiBsciB0b28gbGFyZ2Ugb3IgdG9vIG1hbnkgdHJlZXMiXSxbIk5vaXNlIHNlbnNpdGl2aXR5IiwiTG93IChhdmVyYWdpbmcgZGlsdXRlcyBvdXRsaWVycykiLCJIaWdoIChmaXRzIHJlc2lkdWFscyBpbmNsdWRpbmcgbm9pc2UiXSxbIlBhcmFsbGVsaXNhYmxlIiwiWWVzICh0cml2aWFsbHkpIiwiTm8gKGVhY2ggdHJlZSBkZXBlbmRzIG9uIHByZXZpb3VzKSJdLFsiRGVmYXVsdCB1c2UgY2FzZSIsIkhpZ2gtdmFyaWFuY2UgZGF0YXNldHMiLCJMb3ctYmlhcyByZXF1aXJlbWVudCwgc3RydWN0dXJlZCBkYXRhIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJvb3N0aW5nIHJlZHVjZXMgYmlhczsgYmFnZ2luZyByZWR1Y2VzIHZhcmlhbmNlIOKAlCB0aGV5IGFyZSBjb21wbGVtZW50YXJ5IHN0cmF0ZWdpZXMiLCJTaGFsbG93IHRyZWVzIChkZXB0aCAzLTUpIHdvcmsgYmVzdCBmb3IgYm9vc3Rpbmc7IGRlZXAgdHJlZXMgd29yayBiZXN0IGluc2lkZSBmb3Jlc3RzIiwiU21hbGxlciBsZWFybmluZyByYXRlICsgbW9yZSB0cmVlcyBpcyBhbG1vc3QgYWx3YXlzIGJldHRlciB0aGFuIGxhcmdlIGxyICsgZmV3IHRyZWVzIiwiU3RvY2hhc3RpYyBHQiAoc3Vic2FtcGxlIFx1MDAzYyAxKSBhZGRzIHZhcmlhbmNlIHJlZHVjdGlvbiBvbiB0b3Agb2YgYmlhcyByZWR1Y3Rpb24iLCJHcmFkaWVudCBib29zdGluZyBjYW4gZml0IGFueSBkaWZmZXJlbnRpYWJsZSBsb3NzIGJ5IGNoYW5naW5nIHRoZSBncmFkaWVudCB0YXJnZXQiLCJVbmxpa2UgbmV1cmFsIG5ldHdvcmtzLCBncmFkaWVudCBib29zdGluZyByZXF1aXJlcyBubyBmZWF0dXJlIG5vcm1hbGlzYXRpb24iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJHcmFkaWVudCBCb29zdGluZyBPdmVyZml0cyBXaXRob3V0IFNocmlua2FnZSIsImNvbnRlbnQiOiJXaXRob3V0IHNocmlua2FnZSAobGVhcm5pbmdfcmF0ZT0xLjApLCBncmFkaWVudCBib29zdGluZyBhZ2dyZXNzaXZlbHkgZml0cyB0aGUgdHJhaW5pbmcgZGF0YSBhbmQgb3ZlcmZpdHMgcXVpY2tseS4gQWx3YXlzIHVzZSBsZWFybmluZ19yYXRlIFx1MDAzYyAwLjEgaW4gcHJvZHVjdGlvbi4gVXNlIGVhcmx5IHN0b3BwaW5nIG9uIGEgdmFsaWRhdGlvbiBzZXQgdG8gYXV0b21hdGljYWxseSBmaW5kIHRoZSByaWdodCBuX2VzdGltYXRvcnMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlN0YXJ0aW5nIENvbmZpZ3VyYXRpb24gZm9yIHNrbGVhcm4gR0IiLCJjb250ZW50IjoiQSByZWxpYWJsZSBzdGFydGluZyBwb2ludDogbGVhcm5pbmdfcmF0ZT0wLjA1LCBtYXhfZGVwdGg9NCwgbl9lc3RpbWF0b3JzPTMwMCwgc3Vic2FtcGxlPTAuOCwgbWluX3NhbXBsZXNfbGVhZj01LiBUaGVuIHR1bmUgbl9lc3RpbWF0b3JzIHdpdGggZWFybHkgc3RvcHBpbmcuIFRoaXMgYmVhdHMgZGVmYXVsdCBzZXR0aW5ncyBvbiBtb3N0IHRhYnVsYXIgZGF0YXNldHMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Gradient Boosting — Additive Model and Stage-Wise Fitting

## Additive Model and Stage-Wise Fitting

Gradient boosting builds an additive model F_M(x) = F_0(x) + Σ_{m=1}^{M} η·h_m(x) where each h_m is a weak learner (typically a shallow tree) and η is the learning rate (shrinkage). Unlike neural networks that adjust all parameters simultaneously, stage-wise fitting is greedy — each new tree is added to minimise the current loss without modifying previous trees. This greedy, non-parametric approach is what makes gradient boosting so flexible: any differentiable loss function can be optimised.

## Gradient Boosting as Functional Gradient Descent

Standard gradient descent moves parameters θ in the direction −∇_θ L. Gradient boosting instead does gradient descent in function space: the negative gradient −∂L/∂F evaluated at the current predictions tells us the direction to move the function F. For MSE loss L = (1/2)(y − F)², the negative gradient is y − F — the residual. So residual boosting is a special case of gradient boosting. For log-loss (binary classification) L = −y log p − (1−y) log(1−p), the negative gradient is y − p where p = σ(F). Each new tree is fitted to these pseudo-residuals.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class GradientBoostingMSE:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n = n_estimators; self.lr = learning_rate
        self.max_depth = max_depth; self.trees = []; self.F0 = None

    def fit(self, X, y):
        self.F0 = y.mean()           # initial prediction = global mean
        F = np.full(len(y), self.F0)
        for _ in range(self.n):
            residuals = y - F        # negative gradient of MSE
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            tree.fit(X, residuals)
            F += self.lr * tree.predict(X)
            self.trees.append(tree)
        return self

    def predict(self, X):
        pred = np.full(X.shape[0], self.F0)
        for tree in self.trees:
            pred += self.lr * tree.predict(X)
        return pred

X, y = make_regression(n_samples=600, n_features=10, noise=20, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
gb = GradientBoostingMSE(n_estimators=150, learning_rate=0.1, max_depth=3)
gb.fit(X_tr, y_tr)
rmse = np.sqrt(mean_squared_error(y_te, gb.predict(X_te)))
print(f'Custom GB RMSE: {rmse:.4f}')
```

## Loss Functions and Their Gradients

Gradient boosting's power comes from plugging in any differentiable loss. MSE loss gives gradient = y − F (residuals). Log-loss for binary classification gives gradient = y − σ(F) where σ is the sigmoid — trees are fitted to the difference between true labels and current predicted probabilities. Huber loss (robust regression) gives gradient that is linear for small residuals and bounded for outliers. Quantile loss enables prediction intervals.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -10, 10)))

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

F = np.zeros(len(y_tr))     # start at F=0 (sigmoid gives p=0.5)
trees, lr = [], 0.1

for m in range(100):
    p = sigmoid(F)
    gradient = y_tr - p       # negative gradient of log-loss
    tree = DecisionTreeRegressor(max_depth=3)
    tree.fit(X_tr, gradient)
    F += lr * tree.predict(X_tr)
    trees.append(tree)

# Evaluate on test set
F_te = np.zeros(len(y_te))
for tree in trees:
    F_te += lr * tree.predict(X_te)

preds = (sigmoid(F_te) > 0.5).astype(int)
print(f'Custom log-loss GB accuracy: {(preds == y_te).mean():.4f}')
print(f'Log-loss on test set:        {log_loss(y_te, sigmoid(F_te)):.4f}')
```

> **Why Residuals Equal Negative Gradient for MSE**: MSE loss is L(y, F) = (1/2)(y − F)². Its derivative with respect to F is ∂L/∂F = F − y = −(y − F). So the negative gradient is y − F, which is exactly the residual. Fitting a tree to residuals and adding it to F is gradient descent in function space — residual boosting was invented before the gradient interpretation was formalised.

## sklearn GradientBoostingClassifier

sklearn's GradientBoostingClassifier implements the original Friedman (2001) stochastic gradient boosting algorithm. Key parameters: n_estimators (number of trees), learning_rate (shrinkage η), max_depth (typical 3-5 for boosting), subsample (stochastic GB — use 0.5-0.8 to add variance reduction alongside bias reduction). The deviance (log-loss) and exponential (AdaBoost) loss functions are both supported.

```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

gb = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,    # shrinkage — smaller = more regularisation
    max_depth=3,           # shallow trees preferred for boosting
    subsample=0.8,         # stochastic GB: 80% of data per tree
    min_samples_leaf=5,
    random_state=42
)
gb.fit(X_tr, y_tr)

print(f'Train: {gb.score(X_tr, y_tr):.4f}  Test: {gb.score(X_te, y_te):.4f}')
cv = cross_val_score(gb, X, y, cv=5)
print(f'5-fold CV: {cv.mean():.4f} +/- {cv.std():.4f}')
top3 = gb.feature_importances_.argsort()[::-1][:3]
print(f'Top-3 features by MDI: {top3}')
```

## Learning Rate vs n_estimators Trade-off

Shrinkage (small learning rate η) is the most effective regulariser in gradient boosting. A smaller η requires more trees to fit the training data — the relationship is roughly n_estimators ∝ 1/η. This means a model with lr=0.05 and 400 trees tends to match lr=0.1 and 200 trees in accuracy while being more robust to overfitting. The computational cost is identical. Finding the right n_estimators for a given lr is best done with early stopping.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

configs = [(0.50, 50), (0.10, 200), (0.05, 400), (0.01, 1000)]
results = []
for lr, n_est in configs:
    gb = GradientBoostingClassifier(
        n_estimators=n_est, learning_rate=lr, max_depth=3, random_state=42)
    gb.fit(X_tr, y_tr)
    results.append({'lr': lr, 'n': n_est,
                    'train': gb.score(X_tr, y_tr),
                    'test':  gb.score(X_te, y_te)})
    print(f'lr={lr:5.2f}  n={n_est:4d}  '
          f'train={results[-1]["train"]:.4f}  test={results[-1]["test"]:.4f}')

best = max(results, key=lambda r: r['test'])
print(f'Best config: lr={best["lr"]}, n_estimators={best["n"]}, test={best["test"]:.4f}')
```

## Bagging vs Boosting

| Aspect | Bagging (Random Forest) | Boosting (Gradient Boosting) |
| --- | --- | --- |
| Primary effect | Reduces variance | Reduces bias |
| Tree depth | Deep (unconstrained) | Shallow (depth 3-5 typical) |
| Tree training | Parallel (independent) | Sequential (dependent) |
| Overfitting risk | Low (averaging regularises) | High if lr too large or too many trees |
| Noise sensitivity | Low (averaging dilutes outliers) | High (fits residuals including noise |
| Parallelisable | Yes (trivially) | No (each tree depends on previous) |
| Default use case | High-variance datasets | Low-bias requirement, structured data |

- Boosting reduces bias; bagging reduces variance — they are complementary strategies
- Shallow trees (depth 3-5) work best for boosting; deep trees work best inside forests
- Smaller learning rate + more trees is almost always better than large lr + few trees
- Stochastic GB (subsample < 1) adds variance reduction on top of bias reduction
- Gradient boosting can fit any differentiable loss by changing the gradient target
- Unlike neural networks, gradient boosting requires no feature normalisation

> **Gradient Boosting Overfits Without Shrinkage**: Without shrinkage (learning_rate=1.0), gradient boosting aggressively fits the training data and overfits quickly. Always use learning_rate < 0.1 in production. Use early stopping on a validation set to automatically find the right n_estimators.

> **Starting Configuration for sklearn GB**: A reliable starting point: learning_rate=0.05, max_depth=4, n_estimators=300, subsample=0.8, min_samples_leaf=5. Then tune n_estimators with early stopping. This beats default settings on most tabular datasets.

---

