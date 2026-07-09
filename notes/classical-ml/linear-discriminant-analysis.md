---
title: "Linear Discriminant Analysis (LDA)"
slug: "linear-discriminant-analysis"
description: "Derive LDA from Gaussian class-conditional distributions, understand Fisher's discriminant as a projection maximising class separability, compare LDA vs QDA vs logistic regression, and use LDA for dimensionality reduction."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGluZWFyIERpc2NyaW1pbmFudCBBbmFseXNpcyAoTERBKSBhc3N1bWVzIHRoYXQgZWFjaCBjbGFzcyBnZW5lcmF0ZXMgZGF0YSBmcm9tIGEgbXVsdGl2YXJpYXRlIEdhdXNzaWFuIGRpc3RyaWJ1dGlvbiB3aXRoIGNsYXNzLXNwZWNpZmljIG1lYW4gYnV0IGEgc2hhcmVkIGNvdmFyaWFuY2UgbWF0cml4OiBwKHh8eT1rKSA9IE4ozrzigpYsIM6jKS4gQXBwbHlpbmcgQmF5ZXNcdTAwMjcgdGhlb3JlbSBhbmQgdGFraW5nIGxvZy1yYXRpb3MsIHRoZSBkZWNpc2lvbiBib3VuZGFyeSBiZWNvbWVzIGxpbmVhciBpbiB4IGJlY2F1c2UgdGhlIHF1YWRyYXRpYyB0ZXJtcyBpbiB44bWAzqPigbvCuXggY2FuY2VsIChzaGFyZWQgzqMpLiBMREEgaXMgYm90aCBhIGNsYXNzaWZpZXIgYW5kIGEgZGltZW5zaW9uYWxpdHkgcmVkdWN0aW9uIG1ldGhvZDogaXQgZmluZHMgYXQgbW9zdCBLLTEgZGlyZWN0aW9ucyB0aGF0IG1heGltYWxseSBzZXBhcmF0ZSBLIGNsYXNzZXMgd2hpbGUgbWluaW1pc2luZyB3aXRoaW4tY2xhc3Mgc3ByZWFkLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpc2NyaW1pbmFudCBGdW5jdGlvbiBEZXJpdmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaXRoIGNsYXNzLWNvbmRpdGlvbmFsIEdhdXNzaWFucyBhbmQgc2hhcmVkIGNvdmFyaWFuY2UsIHRoZSBsb2cgcG9zdGVyaW9yIGlzOiBsb2cgcCh5PWt8eCkg4oidIGxvZyDPgOKCliAtICgxLzIpKHgtzrzigpYp4bWAzqPigbvCuSh4Lc684oKWKS4gRXhwYW5kaW5nOiA9IGxvZyDPgOKCliAtICgxLzIpzrzigpbhtYDOo+KBu8K5zrzigpYgKyB44bWAzqPigbvCuc684oKWIC0gKDEvMil44bWAzqPigbvCuXguIFRoZSB0ZXJtIC0oMS8yKXjhtYDOo+KBu8K5eCBpcyB0aGUgc2FtZSBmb3IgYWxsIGNsYXNzZXMgYW5kIGNhbmNlbHMgaW4gYXJnbWF4LiBUaGUgbGluZWFyIGRpc2NyaW1pbmFudCBmdW5jdGlvbiBmb3IgY2xhc3MgayBpczogzrTigpYoeCkgPSB44bWAzqPigbvCuc684oKWIC0gKDEvMinOvOKCluG1gM6j4oG7wrnOvOKCliArIGxvZyDPgOKCli4gQ2xhc3NpZnkgeCB0byBhcmdtYXhfayDOtOKClih4KS4gVGhlIGRlY2lzaW9uIGJvdW5kYXJ5IGJldHdlZW4gY2xhc3NlcyBrIGFuZCBsIGlzIHRoZSBzZXQgb2YgeCB3aGVyZSDOtOKClih4KSA9IM604oKXKHgpLCB3aGljaCBpcyBhIGh5cGVycGxhbmUgKGxpbmVhciBpbiB4KSDigJQgaGVuY2UgXHUwMDI3TGluZWFyXHUwMDI3IERpc2NyaW1pbmFudCBBbmFseXNpcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaXRoaW4tQ2xhc3MgYW5kIEJldHdlZW4tQ2xhc3MgU2NhdHRlciBNYXRyaWNlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHNoYXJlZCBjb3ZhcmlhbmNlIChwb29sZWQgd2l0aGluLWNsYXNzIHNjYXR0ZXIpIGlzIFNXID0gzqPigpYgzqPhtaLiiIhD4oKWICh44bWiLc684oKWKSh44bWiLc684oKWKeG1gCAvIChuLUspLiBUaGUgYmV0d2Vlbi1jbGFzcyBzY2F0dGVyIGlzIFNCID0gzqPigpYgbuKClijOvOKCli3OvCkozrzigpYtzrwp4bWAIHdoZXJlIM68IGlzIHRoZSBnbG9iYWwgbWVhbi4gRmlzaGVyXHUwMDI3cyBjcml0ZXJpb24gbWF4aW1pc2VzIEoodykgPSB34bWAU0J3IC8gd+G1gFNXdyDigJQgdGhlIHJhdGlvIG9mIGJldHdlZW4tY2xhc3MgdG8gd2l0aGluLWNsYXNzIHByb2plY3RlZCB2YXJpYW5jZS4gVGhlIHNvbHV0aW9uIGlzIHRoZSBnZW5lcmFsaXNlZCBlaWdlbnZhbHVlIHByb2JsZW0gU1figbvCuVNCdyA9IM67dywgd2hvc2UgZWlnZW52ZWN0b3JzIGFyZSB0aGUgTERBIGRpcmVjdGlvbnMuIFNpbmNlIFNCIGhhcyByYW5rIGF0IG1vc3QgSy0xLCB0aGVyZSBhcmUgYXQgbW9zdCBLLTEgbm9uemVybyBlaWdlbnZhbHVlcyBhbmQgdGhlcmVmb3JlIGF0IG1vc3QgSy0xIHVzZWZ1bCBkaXNjcmltaW5hbnQgZGltZW5zaW9ucy4gRm9yIGJpbmFyeSBjbGFzc2lmaWNhdGlvbiwgdGhlIHNpbmdsZSBkaXJlY3Rpb24gaXMgdyA9IFNX4oG7wrkozrzigoEtzrzigoIpIOKAlCB0aGUgTWFoYWxhbm9iaXMgZGlyZWN0aW9uIGJldHdlZW4gY2xhc3MgbWVhbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2lyaXNcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBhY2N1cmFjeV9zY29yZVxuXG5jbGFzcyBMREFGcm9tU2NyYXRjaDpcbiAgICBkZWYgZml0KHNlbGYsIFgsIHkpOlxuICAgICAgICBzZWxmLmNsYXNzZXNfID0gbnAudW5pcXVlKHkpXG4gICAgICAgIG4sIHAgPSBYLnNoYXBlXG4gICAgICAgIHNlbGYucHJpb3JzXywgc2VsZi5tZWFuc18gPSB7fSwge31cbiAgICAgICAgU3cgPSBucC56ZXJvcygocCwgcCkpXG4gICAgICAgIGZvciBjIGluIHNlbGYuY2xhc3Nlc186XG4gICAgICAgICAgICBYYyA9IFhbeSA9PSBjXVxuICAgICAgICAgICAgc2VsZi5wcmlvcnNfW2NdID0gbGVuKFhjKSAvIG5cbiAgICAgICAgICAgIHNlbGYubWVhbnNfW2NdICA9IFhjLm1lYW4oYXhpcz0wKVxuICAgICAgICAgICAgZGlmZiA9IFhjIC0gc2VsZi5tZWFuc19bY11cbiAgICAgICAgICAgIFN3ICs9IGRpZmYuVCBAIGRpZmZcbiAgICAgICAgc2VsZi5TaWdtYV8gPSBTdyAvIChuIC0gbGVuKHNlbGYuY2xhc3Nlc18pKSAgIyBwb29sZWQgY292YXJpYW5jZVxuICAgICAgICBzZWxmLlNpZ21hX2ludl8gPSBucC5saW5hbGcucGludihzZWxmLlNpZ21hXylcbiAgICAgICAgcmV0dXJuIHNlbGZcblxuICAgIGRlZiBfZGlzY3JpbWluYW50KHNlbGYsIHgsIGMpOlxuICAgICAgICBtdSA9IHNlbGYubWVhbnNfW2NdXG4gICAgICAgIHJldHVybiAoeCBAIHNlbGYuU2lnbWFfaW52XyBAIG11XG4gICAgICAgICAgICAgICAgLSAwLjUgKiBtdSBAIHNlbGYuU2lnbWFfaW52XyBAIG11XG4gICAgICAgICAgICAgICAgKyBucC5sb2coc2VsZi5wcmlvcnNfW2NdKSlcblxuICAgIGRlZiBwcmVkaWN0KHNlbGYsIFgpOlxuICAgICAgICBzY29yZXMgPSBucC5hcnJheShbW3NlbGYuX2Rpc2NyaW1pbmFudCh4LCBjKSBmb3IgYyBpbiBzZWxmLmNsYXNzZXNfXVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgZm9yIHggaW4gWF0pXG4gICAgICAgIHJldHVybiBzZWxmLmNsYXNzZXNfW25wLmFyZ21heChzY29yZXMsIGF4aXM9MSldXG5cblgsIHkgPSBsb2FkX2lyaXMocmV0dXJuX1hfeT1UcnVlKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMywgcmFuZG9tX3N0YXRlPTQyKVxubGRhX3MgPSBMREFGcm9tU2NyYXRjaCgpLmZpdChYX3RyLCB5X3RyKVxucHJpbnQoZlx1MDAyN0xEQSBzY3JhdGNoOiB7YWNjdXJhY3lfc2NvcmUoeV90ZSwgbGRhX3MucHJlZGljdChYX3RlKSk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGaXNoZXJcdTAwMjdzIERpc2NyaW1pbmFudCBhbmQgRGltZW5zaW9uYWxpdHkgUmVkdWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMREEgYXMgZGltZW5zaW9uYWxpdHkgcmVkdWN0aW9uIHByb2plY3RzIEstY2xhc3MgZGF0YSBvbnRvIEstMSBkaXNjcmltaW5hbnQgZGltZW5zaW9ucyB0aGF0IG1heGltaXNlIGNsYXNzIHNlcGFyYWJpbGl0eS4gRm9yIHRoZSBJcmlzIGRhdGFzZXQgKEs9MyBjbGFzc2VzLCBwPTQgZmVhdHVyZXMpLCBMREEgZmluZHMgZXhhY3RseSAyIGRpc2NyaW1pbmFudCBkaXJlY3Rpb25zLCBjb21wcmVzc2luZyA0RCBkYXRhIGludG8gMkQgd2hpbGUgcHJlc2VydmluZyBtb3N0IG9mIHRoZSBjbGFzcyBzZXBhcmF0aW9uLiBUaGlzIGlzIGZhciBtb3JlIHVzZWZ1bCBmb3IgY2xhc3NpZmljYXRpb24gdGhhbiBQQ0FcdTAwMjdzIDJEIHByb2plY3Rpb24sIHdoaWNoIG1heGltaXNlcyB0b3RhbCB2YXJpYW5jZSByZWdhcmRsZXNzIG9mIGNsYXNzIGxhYmVscy4gQWZ0ZXIgcHJvamVjdGluZyB0byBMREEgc3BhY2UsIGEgc2ltcGxlIGNsYXNzaWZpZXIgKGxpbmVhciwga05OKSBhcHBsaWVkIHRvIHRoZSBsb3ctZGltZW5zaW9uYWwgcmVwcmVzZW50YXRpb24gb2Z0ZW4gYWNoaWV2ZXMgbmVhci1vcHRpbWFsIGFjY3VyYWN5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kaXNjcmltaW5hbnRfYW5hbHlzaXMgaW1wb3J0IExpbmVhckRpc2NyaW1pbmFudEFuYWx5c2lzXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfaXJpc1xuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFjY3VyYWN5X3Njb3JlXG5cblgsIHkgPSBsb2FkX2lyaXMocmV0dXJuX1hfeT1UcnVlKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMywgcmFuZG9tX3N0YXRlPTQyKVxuXG5sZGEgPSBMaW5lYXJEaXNjcmltaW5hbnRBbmFseXNpcyhzb2x2ZXI9XHUwMDI3c3ZkXHUwMDI3LCBzdG9yZV9jb3ZhcmlhbmNlPVRydWUpXG5sZGEuZml0KFhfdHIsIHlfdHIpXG5wcmludChmXHUwMDI3TERBIGNsYXNzaWZpZXIgYWNjdXJhY3k6IHthY2N1cmFjeV9zY29yZSh5X3RlLCBsZGEucHJlZGljdChYX3RlKSk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdFeHBsYWluZWQgdmFyaWFuY2UgcmF0aW86IHtsZGEuZXhwbGFpbmVkX3ZhcmlhbmNlX3JhdGlvX31cdTAwMjcpXG5cbiMgTERBIGZvciBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb24gKEstMSA9IDIgZGltcyBmb3IgMy1jbGFzcyBwcm9ibGVtKVxuWF9sZGFfdHIgPSBsZGEudHJhbnNmb3JtKFhfdHIpXG5YX2xkYV90ZSA9IGxkYS50cmFuc2Zvcm0oWF90ZSlcbnByaW50KGZcdTAwMjdQcm9qZWN0ZWQgc2hhcGU6IHtYX2xkYV90ci5zaGFwZX0gIChmcm9tIHtYX3RyLnNoYXBlWzFdfSAtXHUwMDNlIHtYX2xkYV90ci5zaGFwZVsxXX0gZGltcylcdTAwMjcpXG5mb3IgYyBpbiBucC51bmlxdWUoeV90cik6XG4gICAgbWVhbl9wcm9qID0gWF9sZGFfdHJbeV90ciA9PSBjXS5tZWFuKGF4aXM9MClcbiAgICBwcmludChmXHUwMDI3ICBDbGFzcyB7Y30gbWVhbiBpbiBMREEgc3BhY2U6IHttZWFuX3Byb2oucm91bmQoMyl9XHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBQQ0FcbmZyb20gc2tsZWFybi5kaXNjcmltaW5hbnRfYW5hbHlzaXMgaW1wb3J0IExpbmVhckRpc2NyaW1pbmFudEFuYWx5c2lzXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfd2luZVxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgTG9naXN0aWNSZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWNjdXJhY3lfc2NvcmVcblxuWCwgeSA9IGxvYWRfd2luZShyZXR1cm5fWF95PVRydWUpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4zLCByYW5kb21fc3RhdGU9NDIpXG5cbiMgUENBIHRvIDJEIHRoZW4gY2xhc3NpZnlcbnBjYSA9IFBDQShuX2NvbXBvbmVudHM9MilcblhfcGNhX3RyID0gcGNhLmZpdF90cmFuc2Zvcm0oWF90cilcblhfcGNhX3RlID0gcGNhLnRyYW5zZm9ybShYX3RlKVxubHJfcGNhID0gTG9naXN0aWNSZWdyZXNzaW9uKG1heF9pdGVyPTUwMCkuZml0KFhfcGNhX3RyLCB5X3RyKVxuXG4jIExEQSB0byBLLTE9MkQgdGhlbiBjbGFzc2lmeVxubGRhID0gTGluZWFyRGlzY3JpbWluYW50QW5hbHlzaXMobl9jb21wb25lbnRzPTIpXG5YX2xkYV90ciA9IGxkYS5maXRfdHJhbnNmb3JtKFhfdHIsIHlfdHIpXG5YX2xkYV90ZSA9IGxkYS50cmFuc2Zvcm0oWF90ZSlcbmxyX2xkYSA9IExvZ2lzdGljUmVncmVzc2lvbihtYXhfaXRlcj01MDApLmZpdChYX2xkYV90ciwgeV90cilcblxuIyBGdWxsIExEQSBjbGFzc2lmaWVyXG5sZGFfZnVsbCA9IExpbmVhckRpc2NyaW1pbmFudEFuYWx5c2lzKCkuZml0KFhfdHIsIHlfdHIpXG5cbnByaW50KGZcdTAwMjdMUiBvbiAyIFBDQSBkaW1zOiAgICAgIHthY2N1cmFjeV9zY29yZSh5X3RlLCBscl9wY2EucHJlZGljdChYX3BjYV90ZSkpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3TFIgb24gMiBMREEgZGltczogICAgICB7YWNjdXJhY3lfc2NvcmUoeV90ZSwgbHJfbGRhLnByZWRpY3QoWF9sZGFfdGUpKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0Z1bGwgTERBIGNsYXNzaWZpZXI6ICAge2FjY3VyYWN5X3Njb3JlKHlfdGUsIGxkYV9mdWxsLnByZWRpY3QoWF90ZSkpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJMREEgdnMgUENBIOKAlCBTYW1lIEdvYWwsIERpZmZlcmVudCBDcml0ZXJpb24iLCJjb250ZW50IjoiUENBIGZpbmRzIGRpcmVjdGlvbnMgb2YgbWF4aW11bSB2YXJpYW5jZSBpbiBYLCBpZ25vcmluZyBjbGFzcyBsYWJlbHMuIExEQSBmaW5kcyBkaXJlY3Rpb25zIG9mIG1heGltdW0gY2xhc3Mgc2VwYXJhYmlsaXR5IOKAlCBiZXR3ZWVuLWNsYXNzIHZhcmlhbmNlIHJlbGF0aXZlIHRvIHdpdGhpbi1jbGFzcyB2YXJpYW5jZS4gV2hlbiBjbGFzc2VzIGFyZSB3ZWxsLXNlcGFyYXRlZCBidXQgbm90IGFsaWduZWQgd2l0aCB0aGUgaGlnaGVzdC12YXJpYW5jZSBkaXJlY3Rpb25zIChjb21tb24gaW4gcmVhbCBkYXRhc2V0cyksIExEQSBwcm9qZWN0aW9ucyBhcmUgZHJhbWF0aWNhbGx5IGJldHRlciBmb3IgY2xhc3NpZmljYXRpb24uIFVzZSBQQ0Egd2hlbiB0aGUgZ29hbCBpcyBjb21wcmVzc2lvbiBvciB1bnN1cGVydmlzZWQgc3RydWN0dXJlOyB1c2UgTERBIHdoZW4geW91IGhhdmUgY2xhc3MgbGFiZWxzIGFuZCB3YW50IGRpc2NyaW1pbmF0aXZlIGRpbWVuc2lvbmFsaXR5IHJlZHVjdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGlzY3JpbWluYW50X2FuYWx5c2lzIGltcG9ydCBMaW5lYXJEaXNjcmltaW5hbnRBbmFseXNpcywgUXVhZHJhdGljRGlzY3JpbWluYW50QW5hbHlzaXNcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExvZ2lzdGljUmVncmVzc2lvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgY3Jvc3NfdmFsX3Njb3JlXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuIyBDYXNlIDE6IHNhbWUgY292YXJpYW5jZSDigJQgTERBIGFzc3VtcHRpb24gc2F0aXNmaWVkXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cblgxLCB5MSA9IG1ha2VfY2xhc3NpZmljYXRpb24obl9zYW1wbGVzPTUwMCwgbl9mZWF0dXJlcz0xMCwgbl9pbmZvcm1hdGl2ZT01LCByYW5kb21fc3RhdGU9NDIpXG5cbiMgQ2FzZSAyOiBjbGFzcy1zcGVjaWZpYyBjb3ZhcmlhbmNlIOKAlCBMREEgYXNzdW1wdGlvbiB2aW9sYXRlZCwgUURBIHNob3VsZCB3aW5cblgyXzAgPSBucC5yYW5kb20ubXVsdGl2YXJpYXRlX25vcm1hbChbMF0qNiwgbnAuZXllKDYpKjAuNSwgMjUwKVxuWDJfMSA9IG5wLnJhbmRvbS5tdWx0aXZhcmlhdGVfbm9ybWFsKFsyXSo2LCBucC5kaWFnKFsyLCAzLCAxLCAwLjUsIDQsIDFdKSwgMjUwKVxuWDIsIHkyID0gbnAudnN0YWNrKFtYMl8wLCBYMl8xXSksIG5wLmFycmF5KFswXSoyNTAgKyBbMV0qMjUwKVxuXG5mb3IgZG5hbWUsIFhkLCB5ZCBpbiBbKFx1MDAyN0VxdWFsIGNvdmFyaWFuY2VcdTAwMjcsIFgxLCB5MSksIChcdTAwMjdEaWZmZXJlbnQgY292YXJpYW5jZVx1MDAyNywgWDIsIHkyKV06XG4gICAgcHJpbnQoZlx1MDAyN1xcbntkbmFtZX06XHUwMDI3KVxuICAgIGZvciBuYW1lLCBjbGYgaW4gWyhcdTAwMjdMREFcdTAwMjcsIExpbmVhckRpc2NyaW1pbmFudEFuYWx5c2lzKCkpLFxuICAgICAgICAgICAgICAgICAgICAgICAoXHUwMDI3UURBXHUwMDI3LCBRdWFkcmF0aWNEaXNjcmltaW5hbnRBbmFseXNpcygpKSxcbiAgICAgICAgICAgICAgICAgICAgICAgKFx1MDAyN0xSXHUwMDI3LCAgTG9naXN0aWNSZWdyZXNzaW9uKG1heF9pdGVyPTUwMCkpXTpcbiAgICAgICAgc2NvcmUgPSBjcm9zc192YWxfc2NvcmUoY2xmLCBYZCwgeWQsIGN2PTUsIHNjb3Jpbmc9XHUwMDI3YWNjdXJhY3lcdTAwMjcpLm1lYW4oKVxuICAgICAgICBwcmludChmXHUwMDI3ICB7bmFtZX06IHtzY29yZTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlZ3VsYXJpc2VkIExEQSBmb3IgU21hbGwgU2FtcGxlIFNpemVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIG4gXHUwMDNjIHAgKG1vcmUgZmVhdHVyZXMgdGhhbiBzYW1wbGVzKSwgdGhlIHBvb2xlZCB3aXRoaW4tY2xhc3Mgc2NhdHRlciBtYXRyaXggU1cgaXMgc2luZ3VsYXIgYW5kIGNhbm5vdCBiZSBpbnZlcnRlZC4gUmVndWxhcmlzZWQgTERBIHJlcGxhY2VzIFNXIHdpdGggKDEtzrMpU1cgKyDOs8K3KHRyYWNlKFNXKS9wKcK3SSBmb3IgzrMg4oiIIFswLDFdLiBXaGVuIM6zPTEsIHRoZSByZXN1bHQgaXMgYSBzY2FsZWQgaWRlbnRpdHkg4oCUIGVxdWl2YWxlbnQgdG8gYXNzdW1pbmcgYWxsIGZlYXR1cmVzIGFyZSB1bmNvcnJlbGF0ZWQgd2l0aCBlcXVhbCB2YXJpYW5jZSAoaWRlbnRpY2FsIHRvIEdhdXNzaWFuIE5haXZlIEJheWVzKS4gc2tsZWFyblx1MDAyN3MgTGluZWFyRGlzY3JpbWluYW50QW5hbHlzaXMgd2l0aCBzb2x2ZXI9XHUwMDI3bHNxclx1MDAyNyBhbmQgc2hyaW5rYWdlPVx1MDAyN2F1dG9cdTAwMjcgdXNlcyB0aGUgYW5hbHl0aWNhbGx5IG9wdGltYWwgTGVkb2l0LVdvbGYgc2hyaW5rYWdlIGVzdGltYXRvciwgd2hpY2ggY2hvb3NlcyDOsyB0byBtaW5pbWlzZSB0aGUgRnJvYmVuaXVzIG5vcm0gb2YgdGhlIGVzdGltYXRpb24gZXJyb3IuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkFzc3VtcHRpb24iLCJEZWNpc2lvbiBCb3VuZGFyeSIsIlNtYWxsIG4/IiwiQmVzdCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJMREEiLCJTaGFyZWQgR2F1c3NpYW4gY292YXJpYW5jZSDOoyIsIkxpbmVhciBoeXBlcnBsYW5lIiwiWWVzIOKAlCB1c2UgcmVndWxhcmlzZWQgTERBIiwiV2VsbC1zZXBhcmF0ZWQgY2xhc3NlcywgcCBtb2RlcmF0ZSJdLFsiUURBIiwiQ2xhc3Mtc3BlY2lmaWMgR2F1c3NpYW4gY292YXJpYW5jZSDOo+KCliIsIlF1YWRyYXRpYyBzdXJmYWNlIiwiTm8g4oCUIG5lZWRzIG4gXHUwMDNlXHUwMDNlIHDCt0siLCJDbGFzc2VzIHdpdGggZGlmZmVyZW50IHNwcmVhZC9vcmllbnRhdGlvbiJdLFsiTG9naXN0aWMgUmVncmVzc2lvbiIsIk5vbmUg4oCUIGRpc2NyaW1pbmF0aXZlIiwiTGluZWFyIGh5cGVycGxhbmUiLCJZZXMgd2l0aCBMMiByZWd1bGFyaXNhdGlvbiIsIkdlbmVyYWwgYmluYXJ5L211bHRpY2xhc3MsIG5vIGRpc3RyaWJ1dGlvbmFsIGFzc3VtcHRpb24iXSxbIkdhdXNzaWFuIE5haXZlIEJheWVzIiwiRGlhZ29uYWwgY292YXJpYW5jZSAoaW5kZXBlbmRlbmNlKSIsIlF1YWRyYXRpYyBvciBsaW5lYXIiLCJZZXMg4oCUIGZld2VzdCBwYXJhbWV0ZXJzIiwiSGlnaC1kLCBzbWFsbCBuLCBzdHJlYW1pbmcsIG9ubGluZSJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMREEgcmVxdWlyZXMgbiBcdTAwM2UgcCBmb3IgYSBmdWxsLXJhbmsgcG9vbGVkIGNvdmFyaWFuY2UgbWF0cml4OyB1c2Ugc2hyaW5rYWdlPVx1MDAyN2F1dG9cdTAwMjcgZm9yIGhpZ2gtZCBkYXRhLiIsIkZvciBLIGNsYXNzZXMsIExEQSBwcm9kdWNlcyBhdCBtb3N0IEstMSBkaXNjcmltaW5hbnQgZGlyZWN0aW9ucyDigJQgdXNlIGZvciBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb24gZmlyc3QuIiwiV2hlbiBjbGFzcyBjb3ZhcmlhbmNlcyBkaWZmZXIgc3Vic3RhbnRpYWxseSwgUURBIHByb2R1Y2VzIGJldHRlciBib3VuZGFyaWVzIGJ1dCBuZWVkcyBtb3JlIGRhdGEuIiwiTERBIGlzIGVxdWl2YWxlbnQgdG8gR2F1c3NpYW4gTmFpdmUgQmF5ZXMgd2l0aCBlcXVhbCwgbm9uLWRpYWdvbmFsIGNvdmFyaWFuY2UgYWNyb3NzIGNsYXNzZXMuIiwiQ2hlY2sgTERBIGFzc3VtcHRpb25zOiBwbG90IGNsYXNzLWNvbmRpdGlvbmFsIGRpc3RyaWJ1dGlvbnMgYW5kIHRlc3QgZm9yIG5vcm1hbGl0eSB3aXRoIFNoYXBpcm8tV2lsay4iLCJGb3IgaW1iYWxhbmNlZCBjbGFzc2VzLCBhZGp1c3QgcHJpb3JzXz1jbGFzc19mcmVxdWVuY2llcyB0byBhdm9pZCBtYWpvcml0eS1jbGFzcyBiaWFzLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxEQSByZW1haW5zIGEgcG93ZXJmdWwgYmFzZWxpbmUgZm9yIG11bHRpLWNsYXNzIGNsYXNzaWZpY2F0aW9uIHdoZW4gR2F1c3NpYW4gYXNzdW1wdGlvbnMgaG9sZCBhcHByb3hpbWF0ZWx5LiBJdHMgY2xvc2VkLWZvcm0gc29sdXRpb24sIGxhY2sgb2YgaHlwZXJwYXJhbWV0ZXJzIChiZXlvbmQgcmVndWxhcmlzYXRpb24gc3RyZW5ndGgpLCBhbmQgbmF0dXJhbCBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb24gY2FwYWJpbGl0eSBtYWtlIGl0IGEgdmFsdWFibGUgZmlyc3Qgc3RlcCBpbiBhbnkgY2xhc3NpZmljYXRpb24gcGlwZWxpbmUuIFdoZW4gTERBIHBlcmZvcm1zIHdlbGwsIGl0IHN1Z2dlc3RzIHRoZSBkYXRhIGlzIGFwcHJveGltYXRlbHkgR2F1c3NpYW4gd2l0aCBzaGFyZWQgY292YXJpYW5jZSDigJQgYSByZXN1bHQgd29ydGgga25vd2luZyBiZWZvcmUgcmVhY2hpbmcgZm9yIG1vcmUgY29tcGxleCBtb2RlbHMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJMREEgTm9ybWFsaXR5IEFzc3VtcHRpb24gaW4gUHJhY3RpY2UiLCJjb250ZW50IjoiTERBIGFzc3VtZXMgY2xhc3MtY29uZGl0aW9uYWwgR2F1c3NpYW4gZGlzdHJpYnV0aW9ucy4gQ29tbW9uIHZpb2xhdGlvbnM6IHNrZXdlZCBmZWF0dXJlcyAoYXBwbHkgbG9nIHRyYW5zZm9ybSksIGhlYXZ5IHRhaWxzICh0cmltIG91dGxpZXJzKSwgbXVsdGltb2RhbCB3aXRoaW4tY2xhc3MgZGlzdHJpYnV0aW9ucyAoY29uc2lkZXIgbWl4dHVyZSBtb2RlbHMpLiBIb3dldmVyLCBsaWtlIE5haXZlIEJheWVzLCBMREEgaXMgb2Z0ZW4gcm9idXN0IHRvIG1pbGQgbm9ybWFsaXR5IHZpb2xhdGlvbnMgaW4gY2xhc3NpZmljYXRpb24gdGFza3MgYmVjYXVzZSB0aGUgYXJnbWF4IG9mIHRoZSBkaXNjcmltaW5hbnQgZnVuY3Rpb24gY2FuIHN0aWxsIGJlIGNvcnJlY3QuIEZvciBzZXZlcmVseSBub24tR2F1c3NpYW4gZGF0YSwgbG9naXN0aWMgcmVncmVzc2lvbiAoZGlzY3JpbWluYXRpdmUsIG5vIGRpc3RyaWJ1dGlvbmFsIGFzc3VtcHRpb24pIGlzIHRoZSBzYWZlciBjaG9pY2UuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNdWx0aS1jbGFzcyBMREEgd2l0aCBLIGNsYXNzZXMgZmluZHMgYXQgbW9zdCBLLTEgZGlzY3JpbWluYW50IGRpcmVjdGlvbnMgYmVjYXVzZSB0aGUgYmV0d2Vlbi1jbGFzcyBzY2F0dGVyIG1hdHJpeCBTQiBoYXMgcmFuayBhdCBtb3N0IEstMS4gRm9yIEs9MiB0aGUgc2luZ2xlIGRpcmVjdGlvbiBpcyB3ID0gU1deey0xfShtdV8xIC0gbXVfMikuIEZvciBLPTEwIChkaWdpdCByZWNvZ25pdGlvbiksIExEQSBwcm92aWRlcyBhIDlEIHN1YnNwYWNlIGNhcHR1cmluZyBhbGwgY2xhc3MtZGlzY3JpbWluYXRpdmUgaW5mb3JtYXRpb24uIFByb2plY3RpbmcgdG8gdGhpcyBzdWJzcGFjZSBhbmQgYXBwbHlpbmcgYSBuZWFyZXN0LWNlbnRyb2lkIGNsYXNzaWZpZXIgaXMgYSBjb21wZXRpdGl2ZSBiYXNlbGluZSBmb3IgbW9kZXJhdGUtZGltZW5zaW9uYWwgbXVsdGktY2xhc3MgcHJvYmxlbXMgYW5kIGlzIHVzZWQgaW4gZmFjZSByZWNvZ25pdGlvbiAoRmlzaGVyZmFjZXMpLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTERBIGhhcyBhIGRlZXAgY29ubmVjdGlvbiB0byBsb2dpc3RpYyByZWdyZXNzaW9uOiBib3RoIHByb2R1Y2UgbGluZWFyIGRlY2lzaW9uIGJvdW5kYXJpZXMgYnV0IHZpYSBkaWZmZXJlbnQgZXN0aW1hdGlvbiBwcmluY2lwbGVzLiBMREEgZXN0aW1hdGVzIHRoZSBqb2ludCBkaXN0cmlidXRpb24gcCh4LHkpIGFuZCBkZXJpdmVzIHRoZSBib3VuZGFyeSBhbmFseXRpY2FsbHkgKGdlbmVyYXRpdmUpOyBsb2dpc3RpYyByZWdyZXNzaW9uIG1heGltaXNlcyB0aGUgY29uZGl0aW9uYWwgbGlrZWxpaG9vZCBwKHl8eCkgZGlyZWN0bHkgKGRpc2NyaW1pbmF0aXZlKS4gV2hlbiB0aGUgR2F1c3NpYW4gYXNzdW1wdGlvbiBob2xkcywgTERBIGlzIG1vcmUgc3RhdGlzdGljYWxseSBlZmZpY2llbnQuIFdoZW4gaXQgZG9lcyBub3QgaG9sZCwgbG9naXN0aWMgcmVncmVzc2lvbiBpcyBtb3JlIHJvYnVzdC4gQWx3YXlzIHRyeSBib3RoIGFzIGJhc2VsaW5lcyBiZWZvcmUgcmVhY2hpbmcgZm9yIG1vcmUgY29tcGxleCBtb2RlbHMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTaHJpbmthZ2UgTERBICh1c2luZyB0aGUgTGVkb2l0LVdvbGYgb3B0aW1hbCBlc3RpbWF0b3IgZm9yIHRoZSBjb3ZhcmlhbmNlIG1hdHJpeCkgaXMgZXNzZW50aWFsIGluIGhpZ2gtZGltZW5zaW9uYWwgc2V0dGluZ3Mgd2hlcmUgcCBcdTAwM2VcdTAwM2Ugbi4gV2l0aCBMaW5lYXJEaXNjcmltaW5hbnRBbmFseXNpcyhzb2x2ZXI9XHUwMDI3bHNxclx1MDAyNywgc2hyaW5rYWdlPVx1MDAyN2F1dG9cdTAwMjcpLCB0aGUgb3B0aW1hbCBzaHJpbmthZ2UgcGFyYW1ldGVyIGdhbW1hIGlzIGNvbXB1dGVkIGFuYWx5dGljYWxseSBmcm9tIHRoZSBkYXRhIOKAlCBubyBjcm9zcy12YWxpZGF0aW9uIG5lZWRlZC4gVGhpcyBtYWtlcyByZWd1bGFyaXNlZCBMREEgYSBwcmFjdGljYWwgZGVmYXVsdCBmb3IgZ2Vub21pY3MsIG5ldXJvaW1hZ2luZywgYW5kIHRleHQgd2hlcmUgdGhlIHN0YW5kYXJkIHBvb2xlZCBjb3ZhcmlhbmNlIHdvdWxkIGJlIHNpbmd1bGFyLiBUaGUgcmVzdWx0IGludGVycG9sYXRlcyBiZXR3ZWVuIHRoZSBmdWxsIHBvb2xlZCBjb3ZhcmlhbmNlIChnYW1tYT0wKSBhbmQgYSBzY2FsZWQgaWRlbnRpdHkgKGdhbW1hPTEsIGVxdWl2YWxlbnQgdG8gR2F1c3NpYW4gTmFpdmUgQmF5ZXMpLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Linear Discriminant Analysis (LDA)

Linear Discriminant Analysis (LDA) assumes that each class generates data from a multivariate Gaussian distribution with class-specific mean but a shared covariance matrix: p(x|y=k) = N(μₖ, Σ). Applying Bayes' theorem and taking log-ratios, the decision boundary becomes linear in x because the quadratic terms in xᵀΣ⁻¹x cancel (shared Σ). LDA is both a classifier and a dimensionality reduction method: it finds at most K-1 directions that maximally separate K classes while minimising within-class spread.

## Discriminant Function Derivation

With class-conditional Gaussians and shared covariance, the log posterior is: log p(y=k|x) ∝ log πₖ - (1/2)(x-μₖ)ᵀΣ⁻¹(x-μₖ). Expanding: = log πₖ - (1/2)μₖᵀΣ⁻¹μₖ + xᵀΣ⁻¹μₖ - (1/2)xᵀΣ⁻¹x. The term -(1/2)xᵀΣ⁻¹x is the same for all classes and cancels in argmax. The linear discriminant function for class k is: δₖ(x) = xᵀΣ⁻¹μₖ - (1/2)μₖᵀΣ⁻¹μₖ + log πₖ. Classify x to argmax_k δₖ(x). The decision boundary between classes k and l is the set of x where δₖ(x) = δₗ(x), which is a hyperplane (linear in x) — hence 'Linear' Discriminant Analysis.

## Within-Class and Between-Class Scatter Matrices

The shared covariance (pooled within-class scatter) is SW = Σₖ Σᵢ∈Cₖ (xᵢ-μₖ)(xᵢ-μₖ)ᵀ / (n-K). The between-class scatter is SB = Σₖ nₖ(μₖ-μ)(μₖ-μ)ᵀ where μ is the global mean. Fisher's criterion maximises J(w) = wᵀSBw / wᵀSWw — the ratio of between-class to within-class projected variance. The solution is the generalised eigenvalue problem SW⁻¹SBw = λw, whose eigenvectors are the LDA directions. Since SB has rank at most K-1, there are at most K-1 nonzero eigenvalues and therefore at most K-1 useful discriminant dimensions. For binary classification, the single direction is w = SW⁻¹(μ₁-μ₂) — the Mahalanobis direction between class means.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class LDAFromScratch:
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        n, p = X.shape
        self.priors_, self.means_ = {}, {}
        Sw = np.zeros((p, p))
        for c in self.classes_:
            Xc = X[y == c]
            self.priors_[c] = len(Xc) / n
            self.means_[c]  = Xc.mean(axis=0)
            diff = Xc - self.means_[c]
            Sw += diff.T @ diff
        self.Sigma_ = Sw / (n - len(self.classes_))  # pooled covariance
        self.Sigma_inv_ = np.linalg.pinv(self.Sigma_)
        return self

    def _discriminant(self, x, c):
        mu = self.means_[c]
        return (x @ self.Sigma_inv_ @ mu
                - 0.5 * mu @ self.Sigma_inv_ @ mu
                + np.log(self.priors_[c]))

    def predict(self, X):
        scores = np.array([[self._discriminant(x, c) for c in self.classes_]
                           for x in X])
        return self.classes_[np.argmax(scores, axis=1)]

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
lda_s = LDAFromScratch().fit(X_tr, y_tr)
print(f'LDA scratch: {accuracy_score(y_te, lda_s.predict(X_te)):.4f}')
```

## Fisher's Discriminant and Dimensionality Reduction

LDA as dimensionality reduction projects K-class data onto K-1 discriminant dimensions that maximise class separability. For the Iris dataset (K=3 classes, p=4 features), LDA finds exactly 2 discriminant directions, compressing 4D data into 2D while preserving most of the class separation. This is far more useful for classification than PCA's 2D projection, which maximises total variance regardless of class labels. After projecting to LDA space, a simple classifier (linear, kNN) applied to the low-dimensional representation often achieves near-optimal accuracy.

```python
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)

lda = LinearDiscriminantAnalysis(solver='svd', store_covariance=True)
lda.fit(X_tr, y_tr)
print(f'LDA classifier accuracy: {accuracy_score(y_te, lda.predict(X_te)):.4f}')
print(f'Explained variance ratio: {lda.explained_variance_ratio_}')

# LDA for dimensionality reduction (K-1 = 2 dims for 3-class problem)
X_lda_tr = lda.transform(X_tr)
X_lda_te = lda.transform(X_te)
print(f'Projected shape: {X_lda_tr.shape}  (from {X_tr.shape[1]} -> {X_lda_tr.shape[1]} dims)')
for c in np.unique(y_tr):
    mean_proj = X_lda_tr[y_tr == c].mean(axis=0)
    print(f'  Class {c} mean in LDA space: {mean_proj.round(3)}')
```

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_wine(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)

# PCA to 2D then classify
pca = PCA(n_components=2)
X_pca_tr = pca.fit_transform(X_tr)
X_pca_te = pca.transform(X_te)
lr_pca = LogisticRegression(max_iter=500).fit(X_pca_tr, y_tr)

# LDA to K-1=2D then classify
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda_tr = lda.fit_transform(X_tr, y_tr)
X_lda_te = lda.transform(X_te)
lr_lda = LogisticRegression(max_iter=500).fit(X_lda_tr, y_tr)

# Full LDA classifier
lda_full = LinearDiscriminantAnalysis().fit(X_tr, y_tr)

print(f'LR on 2 PCA dims:      {accuracy_score(y_te, lr_pca.predict(X_pca_te)):.4f}')
print(f'LR on 2 LDA dims:      {accuracy_score(y_te, lr_lda.predict(X_lda_te)):.4f}')
print(f'Full LDA classifier:   {accuracy_score(y_te, lda_full.predict(X_te)):.4f}')
```

> **LDA vs PCA — Same Goal, Different Criterion**: PCA finds directions of maximum variance in X, ignoring class labels. LDA finds directions of maximum class separability — between-class variance relative to within-class variance. When classes are well-separated but not aligned with the highest-variance directions (common in real datasets), LDA projections are dramatically better for classification. Use PCA when the goal is compression or unsupervised structure; use LDA when you have class labels and want discriminative dimensionality reduction.

```python
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

np.random.seed(42)
# Case 1: same covariance — LDA assumption satisfied
from sklearn.datasets import make_classification
X1, y1 = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)

# Case 2: class-specific covariance — LDA assumption violated, QDA should win
X2_0 = np.random.multivariate_normal([0]*6, np.eye(6)*0.5, 250)
X2_1 = np.random.multivariate_normal([2]*6, np.diag([2, 3, 1, 0.5, 4, 1]), 250)
X2, y2 = np.vstack([X2_0, X2_1]), np.array([0]*250 + [1]*250)

for dname, Xd, yd in [('Equal covariance', X1, y1), ('Different covariance', X2, y2)]:
    print(f'\n{dname}:')
    for name, clf in [('LDA', LinearDiscriminantAnalysis()),
                       ('QDA', QuadraticDiscriminantAnalysis()),
                       ('LR',  LogisticRegression(max_iter=500))]:
        score = cross_val_score(clf, Xd, yd, cv=5, scoring='accuracy').mean()
        print(f'  {name}: {score:.4f}')
```

## Regularised LDA for Small Sample Sizes

When n < p (more features than samples), the pooled within-class scatter matrix SW is singular and cannot be inverted. Regularised LDA replaces SW with (1-γ)SW + γ·(trace(SW)/p)·I for γ ∈ [0,1]. When γ=1, the result is a scaled identity — equivalent to assuming all features are uncorrelated with equal variance (identical to Gaussian Naive Bayes). sklearn's LinearDiscriminantAnalysis with solver='lsqr' and shrinkage='auto' uses the analytically optimal Ledoit-Wolf shrinkage estimator, which chooses γ to minimise the Frobenius norm of the estimation error.

| Method | Assumption | Decision Boundary | Small n? | Best Use Case |
| --- | --- | --- | --- | --- |
| LDA | Shared Gaussian covariance Σ | Linear hyperplane | Yes — use regularised LDA | Well-separated classes, p moderate |
| QDA | Class-specific Gaussian covariance Σₖ | Quadratic surface | No — needs n >> p·K | Classes with different spread/orientation |
| Logistic Regression | None — discriminative | Linear hyperplane | Yes with L2 regularisation | General binary/multiclass, no distributional assumption |
| Gaussian Naive Bayes | Diagonal covariance (independence) | Quadratic or linear | Yes — fewest parameters | High-d, small n, streaming, online |

- LDA requires n > p for a full-rank pooled covariance matrix; use shrinkage='auto' for high-d data.
- For K classes, LDA produces at most K-1 discriminant directions — use for dimensionality reduction first.
- When class covariances differ substantially, QDA produces better boundaries but needs more data.
- LDA is equivalent to Gaussian Naive Bayes with equal, non-diagonal covariance across classes.
- Check LDA assumptions: plot class-conditional distributions and test for normality with Shapiro-Wilk.
- For imbalanced classes, adjust priors_=class_frequencies to avoid majority-class bias.

LDA remains a powerful baseline for multi-class classification when Gaussian assumptions hold approximately. Its closed-form solution, lack of hyperparameters (beyond regularisation strength), and natural dimensionality reduction capability make it a valuable first step in any classification pipeline. When LDA performs well, it suggests the data is approximately Gaussian with shared covariance — a result worth knowing before reaching for more complex models.

> **LDA Normality Assumption in Practice**: LDA assumes class-conditional Gaussian distributions. Common violations: skewed features (apply log transform), heavy tails (trim outliers), multimodal within-class distributions (consider mixture models). However, like Naive Bayes, LDA is often robust to mild normality violations in classification tasks because the argmax of the discriminant function can still be correct. For severely non-Gaussian data, logistic regression (discriminative, no distributional assumption) is the safer choice.

Multi-class LDA with K classes finds at most K-1 discriminant directions because the between-class scatter matrix SB has rank at most K-1. For K=2 the single direction is w = SW^{-1}(mu_1 - mu_2). For K=10 (digit recognition), LDA provides a 9D subspace capturing all class-discriminative information. Projecting to this subspace and applying a nearest-centroid classifier is a competitive baseline for moderate-dimensional multi-class problems and is used in face recognition (Fisherfaces).

LDA has a deep connection to logistic regression: both produce linear decision boundaries but via different estimation principles. LDA estimates the joint distribution p(x,y) and derives the boundary analytically (generative); logistic regression maximises the conditional likelihood p(y|x) directly (discriminative). When the Gaussian assumption holds, LDA is more statistically efficient. When it does not hold, logistic regression is more robust. Always try both as baselines before reaching for more complex models.

Shrinkage LDA (using the Ledoit-Wolf optimal estimator for the covariance matrix) is essential in high-dimensional settings where p >> n. With LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto'), the optimal shrinkage parameter gamma is computed analytically from the data — no cross-validation needed. This makes regularised LDA a practical default for genomics, neuroimaging, and text where the standard pooled covariance would be singular. The result interpolates between the full pooled covariance (gamma=0) and a scaled identity (gamma=1, equivalent to Gaussian Naive Bayes).

---

