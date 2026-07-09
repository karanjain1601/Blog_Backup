---
title: "Change Point Detection — PELT and BOCPD"
slug: "change-point-detection"
description: "Detect structural breaks in time series: PELT offline dynamic programming with pruning, BOCPD Bayesian online method with posterior over run lengths, ruptures library, and Bai-Perron structural break test for econometric applications."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBjaGFuZ2UgcG9pbnQgaXMgYSB0aW1lIGluZGV4IM+EIGF0IHdoaWNoIHRoZSBzdGF0aXN0aWNhbCBwcm9wZXJ0aWVzIG9mIGEgdGltZSBzZXJpZXMgc2hpZnQ6IGEgY2hhbmdlIGluIG1lYW4sIHZhcmlhbmNlLCB0cmVuZCwgb3IgZnVsbCBkaXN0cmlidXRpb24uIENoYW5nZSBwb2ludCBkZXRlY3Rpb24gaXMgZnVuZGFtZW50YWwgdG8gc2VnbWVudGF0aW9uLCBhbm9tYWx5IGRldGVjdGlvbiwgYW5kIHByZXByb2Nlc3NpbmcgYmVmb3JlIGZvcmVjYXN0aW5nLiBUd28gZG9taW5hbnQgcGFyYWRpZ21zIGV4aXN0OiBvZmZsaW5lIChiYXRjaCkgbWV0aG9kcyB0aGF0IGZpbmQgYWxsIGNoYW5nZSBwb2ludHMgc2ltdWx0YW5lb3VzbHkgZ2l2ZW4gdGhlIGZ1bGwgc2VyaWVzLCBhbmQgb25saW5lIChzdHJlYW1pbmcpIG1ldGhvZHMgdGhhdCBkZXRlY3QgY2hhbmdlIHBvaW50cyBzZXF1ZW50aWFsbHkgYXMgZGF0YSBhcnJpdmVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoYXQgSXMgYSBDaGFuZ2UgUG9pbnQ/In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHaXZlbiBhIHRpbWUgc2VyaWVzIHlfezE6bn0sIGEgY2hhbmdlIHBvaW50IM+EIHBhcnRpdGlvbnMgdGhlIHNlcmllcyBpbnRvIHNlZ21lbnRzIHdpdGggZGlmZmVyZW50IGRpc3RyaWJ1dGlvbmFsIHBhcmFtZXRlcnMuIEZvciBLIGNoYW5nZSBwb2ludHMgYXQgz4RfMSBcdTAwM2Mgz4RfMiBcdTAwM2MgLi4uIFx1MDAzYyDPhF9LLCBlYWNoIHNlZ21lbnQgeV97z4Rfe2stMX0rMTrPhF9rfSBpcyBhc3N1bWVkIGkuaS5kLiBmcm9tIHNvbWUgZGlzdHJpYnV0aW9uIFBfay4gVGhlIGNvc3Qgb2YgYSBzZWdtZW50IGlzIEMoeV97YTpifSksIGUuZy4sIG5lZ2F0aXZlIGxvZy1saWtlbGlob29kIG9yIHN1bSBvZiBzcXVhcmVkIGRldmlhdGlvbnMgZnJvbSB0aGUgc2VnbWVudCBtZWFuLiBUaGUgb2JqZWN0aXZlIGlzIHRvIG1pbmltaXNlIHRvdGFsIGNvc3QgKyBhIHBlbmFsdHkgzrJLIGZvciBLIHNlZ21lbnRzOiDOoyBDKHlfe8+EX3trLTF9Os+EX2t9KSArIM6ySy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQRUxUIOKAlCBQcnVuZWQgRXhhY3QgTGluZWFyIFRpbWUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBFTFQgKEtpbGxpY2sgZXQgYWwuLCAyMDEyKSBzb2x2ZXMgdGhlIHNlZ21lbnRhdGlvbiBwcm9ibGVtIGV4YWN0bHkgdXNpbmcgZHluYW1pYyBwcm9ncmFtbWluZyB3aXRoIGEgcHJ1bmluZyBjb25kaXRpb24uIERlZmluZSBGKHQpID0gbWluIGNvc3Qgb2Ygc2VnbWVudGluZyB5X3sxOnR9LiBUaGUgcmVjdXJzaW9uIGlzIEYodCkgPSBtaW5fe8+EIFx1MDAzYyB0fSBbRijPhCkgKyBDKHlfe8+EKzE6dH0pICsgzrJdLiBQRUxUIHBydW5lcyBjYW5kaWRhdGUgY2hhbmdlIHBvaW50czogaWYgRijPhCkgKyBDKHlfe8+EKzE6c30pICsgzrIg4omlIEYocykgZm9yIHNvbWUgcywgdGhlbiDPhCBjYW4gbmV2ZXIgYmUgdGhlIGxhc3QgY2hhbmdlIHBvaW50IGZvciBhbnkgZnV0dXJlIHRpbWUgdC4gVW5kZXIgbWlsZCBjb25kaXRpb25zIHRoaXMgYWNoaWV2ZXMgTyhuKSBleHBlY3RlZCBjb21wbGV4aXR5IChlbXBpcmljYWxseSBPKG4gbG9nIG4pKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBwZWx0KHksIHBlbmFsdHk9MTAuMCk6XG4gICAgXCJcIlwiXG4gICAgUEVMVCBjaGFuZ2UgcG9pbnQgZGV0ZWN0aW9uIHdpdGggTVNFIGNvc3QgKG1lYW4gc2hpZnQgbW9kZWwpLlxuICAgIFJldHVybnMgbGlzdCBvZiBjaGFuZ2UgcG9pbnQgaW5kaWNlcyAoc3RhcnRzIG9mIG5ldyBzZWdtZW50cykuXG4gICAgXCJcIlwiXG4gICAgbiA9IGxlbih5KVxuICAgIEYgPSBucC5mdWxsKG4gKyAxLCBucC5pbmYpXG4gICAgRlswXSA9IC1wZW5hbHR5XG4gICAgbGFzdF9jcCA9IFstMV0gKiAobiArIDEpXG4gICAgYWRtaXNzaWJsZSA9IFswXSAgIyBjYW5kaWRhdGUgbGFzdCBjaGFuZ2UgcG9pbnRzXG5cbiAgICBkZWYgc2VnX2Nvc3QocywgZSk6XG4gICAgICAgIFwiXCJcIk1TRSBjb3N0OiBzdW0gb2Ygc3F1YXJlZCBkZXZpYXRpb25zIGZyb20gc2VnbWVudCBtZWFuLlwiXCJcIlxuICAgICAgICBzZWcgPSB5W3M6ZV1cbiAgICAgICAgcmV0dXJuIG5wLnN1bSgoc2VnIC0gc2VnLm1lYW4oKSkqKjIpXG5cbiAgICBmb3IgdCBpbiByYW5nZSgxLCBuICsgMSk6XG4gICAgICAgIGJlc3RfY29zdCA9IG5wLmluZlxuICAgICAgICBuZXdfYWRtaXNzaWJsZSA9IFtdXG4gICAgICAgIGZvciB0YXUgaW4gYWRtaXNzaWJsZTpcbiAgICAgICAgICAgIGNvc3QgPSBGW3RhdV0gKyBzZWdfY29zdCh0YXUsIHQpICsgcGVuYWx0eVxuICAgICAgICAgICAgaWYgY29zdCBcdTAwM2MgYmVzdF9jb3N0OlxuICAgICAgICAgICAgICAgIGJlc3RfY29zdCA9IGNvc3RcbiAgICAgICAgICAgICAgICBGW3RdID0gYmVzdF9jb3N0XG4gICAgICAgICAgICAgICAgbGFzdF9jcFt0XSA9IHRhdVxuICAgICAgICAjIFBydW5pbmc6IHJlbW92ZSB0YXUgaWYgRlt0YXVdICsgc2VnX2Nvc3QodGF1LCB0KSArIHBlbmFsdHkgXHUwMDNlPSBGW3RdXG4gICAgICAgIGZvciB0YXUgaW4gYWRtaXNzaWJsZTpcbiAgICAgICAgICAgIGlmIEZbdGF1XSArIHNlZ19jb3N0KHRhdSwgdCkgXHUwMDNjPSBGW3RdOlxuICAgICAgICAgICAgICAgIG5ld19hZG1pc3NpYmxlLmFwcGVuZCh0YXUpXG4gICAgICAgIG5ld19hZG1pc3NpYmxlLmFwcGVuZCh0KVxuICAgICAgICBhZG1pc3NpYmxlID0gbmV3X2FkbWlzc2libGVcblxuICAgICMgQmFja3RyYWNrIGNoYW5nZSBwb2ludHNcbiAgICBjcHMsIGlkeCA9IFtdLCBuXG4gICAgd2hpbGUgbGFzdF9jcFtpZHhdIFx1MDAzZSAwOlxuICAgICAgICBjcHMuYXBwZW5kKGxhc3RfY3BbaWR4XSlcbiAgICAgICAgaWR4ID0gbGFzdF9jcFtpZHhdXG4gICAgcmV0dXJuIHNvcnRlZChjcHMpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxueSA9IG5wLmNvbmNhdGVuYXRlKFtucC5yYW5kb20ucmFuZG4oODApLCBucC5yYW5kb20ucmFuZG4oODApICsgMy4wLFxuICAgICAgICAgICAgICAgICAgICBucC5yYW5kb20ucmFuZG4oODApIC0gMS41XSlcbmNwcyA9IHBlbHQoeSwgcGVuYWx0eT0xNS4wKVxucHJpbnQoZlx1MDAyN1RydWUgY2hhbmdlIHBvaW50czogWzgwLCAxNjBdXHUwMDI3KVxucHJpbnQoZlx1MDAyN1BFTFQgZGV0ZWN0ZWQ6ICAgICAge2Nwc31cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoicnVwdHVyZXMgTGlicmFyeSDigJQgTXVsdGlwbGUgQ2hhbmdlIFBvaW50IERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJ1cHR1cmVzIGxpYnJhcnkgKFRydW9uZyBldCBhbC4sIDIwMjApIHByb3ZpZGVzIFBFTFQsIEJpbmFyeSBTZWdtZW50YXRpb24sIEJvdHRvbS1VcCwgYW5kIFdpbmRvdyBTbGlkaW5nIG1ldGhvZHMgd2l0aCBtb2R1bGFyIGNvc3QgZnVuY3Rpb25zIChNU0UsIFJCRiBrZXJuZWwsIGxpbmVhciwgQVIpLiBDb3N0IGNob2ljZXM6IGwyIChtZWFuIHNoaWZ0KSwgcmJmIChub24tcGFyYW1ldHJpYywgZGlzdHJpYnV0aW9uLWZyZWUpLCBhciAoYXV0b3JlZ3Jlc3NpdmUgY2hhbmdlKS4gUGVuYWx0eSBzZWxlY3Rpb246IEJJQyAozrIgPSBsb2cobikgw5cgZGltKSwgbW9kaWZpZWQgQklDIChtYmljKSwgb3IgY3Jvc3MtdmFsaWRhdGlvbi4gcnVwdHVyZXMgYWxzbyBvZmZlcnMgYW4gbl9ia3BzIGludGVyZmFjZSB3aGVuIHRoZSBudW1iZXIgb2YgY2hhbmdlIHBvaW50cyBpcyBrbm93bi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgcnVwdHVyZXMgYXMgcnB0XG5cbm5wLnJhbmRvbS5zZWVkKDEpXG5zaWduYWwsIHRydWVfY3BzID0gcnB0LnB3X2NvbnN0YW50KG5fc2FtcGxlcz0zMDAsIG5fZmVhdHVyZXM9MSwgbl9ia3BzPTMsIG5vaXNlX3N0ZD0wLjUpXG50cnVlX2NwcyA9IFt0IGZvciB0IGluIHRydWVfY3BzIGlmIHQgXHUwMDNjIDMwMF1cblxuIyBQRUxUIHdpdGggUkJGIGNvc3QgKG5vbi1wYXJhbWV0cmljLCB3b3JrcyBmb3IgbWVhbiArIHZhcmlhbmNlIGNoYW5nZXMpXG5hbGdvX3BlbHQgPSBycHQuUGVsdChtb2RlbD1cdTAwMjdyYmZcdTAwMjcsIG1pbl9zaXplPTEwLCBqdW1wPTEpLmZpdChzaWduYWwpXG5jcHNfcGVsdCAgPSBhbGdvX3BlbHQucHJlZGljdChwZW49My4wKVs6LTFdICAjIGxhc3QgZWxlbWVudCBpcyBuLCBleGNsdWRlIGl0XG5cbiMgQmluYXJ5IFNlZ21lbnRhdGlvbiAoZmFzdGVyIGJ1dCBhcHByb3hpbWF0ZSkgd2l0aCBMMiBjb3N0XG5hbGdvX2JpbnNlZyA9IHJwdC5CaW5zZWcobW9kZWw9XHUwMDI3bDJcdTAwMjcpLmZpdChzaWduYWwpXG5jcHNfYmluc2VnICA9IGFsZ29fYmluc2VnLnByZWRpY3Qobl9ia3BzPTMpWzotMV1cblxuIyBXaW5kb3cgU2xpZGluZ1xuYWxnb193aW5kb3cgPSBycHQuV2luZG93KHdpZHRoPTMwLCBtb2RlbD1cdTAwMjdsMlx1MDAyNykuZml0KHNpZ25hbClcbmNwc193aW5kb3cgID0gYWxnb193aW5kb3cucHJlZGljdChuX2JrcHM9MylbOi0xXVxuXG5wcmludChmXHUwMDI3VHJ1ZSBjaGFuZ2UgcG9pbnRzOiB7dHJ1ZV9jcHN9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1BFTFQgKHJiZiwgcGVuPTMpOiAge2Nwc19wZWx0fVx1MDAyNylcbnByaW50KGZcdTAwMjdCaW5TZWcgKGwyLCBLPTMpOiAgIHtjcHNfYmluc2VnfVx1MDAyNylcbnByaW50KGZcdTAwMjdXaW5kb3cgKGwyLCBLPTMpOiAgIHtjcHNfd2luZG93fVx1MDAyNylcblxuIyBFdmFsdWF0ZTogbWVhbiBhYnNvbHV0ZSBlcnJvciBvZiBkZXRlY3RlZCB2cyB0cnVlIGNoYW5nZSBwb2ludHNcbmRlZiBjcF9lcnJvcihkZXRlY3RlZCwgdHJ1ZSk6XG4gICAgaWYgbm90IGRldGVjdGVkIG9yIG5vdCB0cnVlOlxuICAgICAgICByZXR1cm4gZmxvYXQoXHUwMDI3aW5mXHUwMDI3KVxuICAgIHJldHVybiBucC5tZWFuKFttaW4oYWJzKGQgLSB0KSBmb3IgdCBpbiB0cnVlKSBmb3IgZCBpbiBkZXRlY3RlZF0pXG5wcmludChmXHUwMDI3UEVMVCBNQUUgdG8gdHJ1ZSBDUHM6IHtjcF9lcnJvcihjcHNfcGVsdCwgdHJ1ZV9jcHMpOi4xZn0gc3RlcHNcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQk9DUEQg4oCUIEJheWVzaWFuIE9ubGluZSBDaGFuZ2UgUG9pbnQgRGV0ZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCT0NQRCAoQWRhbXMgXHUwMDI2IE1hY0theSwgMjAwNykgbWFpbnRhaW5zIGEgcG9zdGVyaW9yIGRpc3RyaWJ1dGlvbiBvdmVyIHRoZSBydW4gbGVuZ3RoIHJfdCAodGltZSBzaW5jZSB0aGUgbGFzdCBjaGFuZ2UgcG9pbnQpLiBBdCBlYWNoIHN0ZXAsIGl0IGV2YWx1YXRlcyB0d28gaHlwb3RoZXNlczogKDEpIGNvbnRpbnVlIHRoZSBjdXJyZW50IHNlZ21lbnQgKHJ1biBsZW5ndGggZ3Jvd3MgYnkgMSkgb3IgKDIpIGEgY2hhbmdlIHBvaW50IG9jY3VycyAocnVuIGxlbmd0aCByZXNldHMgdG8gMCkuIFRoZSBoYXphcmQgZnVuY3Rpb24gSCBjb250cm9scyB0aGUgcHJpb3IgcHJvYmFiaWxpdHkgb2YgYSBjaGFuZ2UgcG9pbnQgYXQgZWFjaCBzdGVwLiBQcmVkaWN0aXZlIGRpc3RyaWJ1dGlvbnMgYXJlIGNvbXB1dGVkIHVzaW5nIGNvbmp1Z2F0ZSBtb2RlbHMgKE5vcm1hbC1JbnZlcnNlLUdhbW1hIGZvciBHYXVzc2lhbiBkYXRhLCBvciBTdHVkZW50LXQgcHJlZGljdGl2ZSkuIEJPQ1BEIGlzIGV4YWN0IGFuZCBvbmxpbmUgYnV0IE8odCkgcGVyIHN0ZXAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgdCBhcyBzdHVkZW50X3RcblxuZGVmIGJvY3BkX2dhdXNzaWFuKHksIGhhemFyZD0wLjAxLCBtdTA9MC4wLCBrYXBwYTA9MS4wLCBhbHBoYTA9MS4wLCBiZXRhMD0xLjApOlxuICAgIFwiXCJcIlxuICAgIEJheWVzaWFuIE9ubGluZSBDaGFuZ2UgUG9pbnQgRGV0ZWN0aW9uIHdpdGggTm9ybWFsLUludmVyc2UtR2FtbWEgcHJpb3IuXG4gICAgUmV0dXJuczogcnVuX2xlbmd0aF9wcm9icyAoVCB4IFQrMSksIGNoYW5nZV9wb2ludF9wcm9icyAoVCwpXG4gICAgXCJcIlwiXG4gICAgVCA9IGxlbih5KVxuICAgIFIgPSBucC56ZXJvcygoVCArIDEsIFQgKyAxKSlcbiAgICBSWzAsIDBdID0gMS4wXG4gICAgIyBTdWZmaWNpZW50IHN0YXRpc3RpY3MgZm9yIGVhY2ggcnVuIGxlbmd0aFxuICAgIG11ICAgPSBucC5mdWxsKFQgKyAxLCBtdTApXG4gICAga2FwcGEgPSBucC5mdWxsKFQgKyAxLCBrYXBwYTApXG4gICAgYWxwaGEgPSBucC5mdWxsKFQgKyAxLCBhbHBoYTApXG4gICAgYmV0YSAgPSBucC5mdWxsKFQgKyAxLCBiZXRhMClcbiAgICBjcF9wcm9icyA9IG5wLnplcm9zKFQpXG5cbiAgICBmb3IgdCBpbiByYW5nZShUKTpcbiAgICAgICAgIyBQcmVkaWN0aXZlOiBTdHVkZW50LXQgZGlzdHJpYnV0aW9uXG4gICAgICAgIGRmICAgPSAyICogYWxwaGFcbiAgICAgICAgc2NhbGUgPSBucC5zcXJ0KGJldGEgKiAoa2FwcGEgKyAxKSAvIChhbHBoYSAqIGthcHBhKSlcbiAgICAgICAgcHJlZCAgPSBzdHVkZW50X3QucGRmKHlbdF0sIGRmPWRmLCBsb2M9bXUsIHNjYWxlPXNjYWxlKSArIDFlLTMwMFxuICAgICAgICAjIEdyb3d0aDogcnVuIGxlbmd0aCBpbmNyZW1lbnRzXG4gICAgICAgIFJbdCArIDEsIDE6dCArIDJdID0gUlt0LCA6dCArIDFdICogcHJlZFs6dCArIDFdICogKDEgLSBoYXphcmQpXG4gICAgICAgICMgQ2hhbmdlIHBvaW50OiBydW4gbGVuZ3RoIHJlc2V0c1xuICAgICAgICBSW3QgKyAxLCAwXSA9IG5wLnN1bShSW3QsIDp0ICsgMV0gKiBwcmVkWzp0ICsgMV0pICogaGF6YXJkXG4gICAgICAgIFJbdCArIDFdIC89IChSW3QgKyAxXS5zdW0oKSArIDFlLTMwMCkgICMgbm9ybWFsaXNlXG4gICAgICAgICMgTUFQIHJ1biBsZW5ndGhcbiAgICAgICAgY3BfcHJvYnNbdF0gPSBSW3QgKyAxLCAwXVxuICAgIHJldHVybiBSLCBjcF9wcm9ic1xuXG5ucC5yYW5kb20uc2VlZCgzKVxueSA9IG5wLmNvbmNhdGVuYXRlKFtucC5yYW5kb20ucmFuZG4oMTAwKSwgbnAucmFuZG9tLnJhbmRuKDEwMCkgKyAzLjBdKVxuUiwgY3BfcHJvYnMgPSBib2NwZF9nYXVzc2lhbih5LCBoYXphcmQ9MS81MClcbnByaW50KGZcdTAwMjdNYXggQ1AgcHJvYiBsb2NhdGlvbjoge2NwX3Byb2JzLmFyZ21heCgpfSAodHJ1ZSBjaGFuZ2UgcG9pbnQ6IDEwMClcdTAwMjcpXG5wcmludChmXHUwMDI3Q1AgcHJvYiBhdCB0PTEwMDoge2NwX3Byb2JzWzEwMF06LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdDUCBwcm9iIGF0IHQ9NTA6ICB7Y3BfcHJvYnNbNTBdOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmFpLVBlcnJvbiBTdHJ1Y3R1cmFsIEJyZWFrIFRlc3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIGVjb25vbWV0cmljcywgc3RydWN0dXJhbCBicmVha3MgYXJlIHRlc3RlZCBmb3JtYWxseS4gVGhlIENob3cgdGVzdCBjaGVja3MgZm9yIGEgYnJlYWsgYXQgYSBrbm93biBkYXRlLiBUaGUgQmFpLVBlcnJvbiB0ZXN0ICgxOTk4LCAyMDAzKSBhbGxvd3MgYW4gdW5rbm93biBudW1iZXIgb2YgYnJlYWtzOiBpdCBlc3RpbWF0ZXMgYnJlYWsgZGF0ZXMgYW5kIHRlc3RzIHRoZWlyIHNpZ25pZmljYW5jZSB1c2luZyBzdXBGIHN0YXRpc3RpY3MuIHN0YXRzbW9kZWxzIGltcGxlbWVudHMgdGhpcyBhcyBCcmVha3BvaW50RXN0aW1hdG9yLiBUaGUgQmFpLVBlcnJvbiBwcm9jZWR1cmU6ICgxKSBmaXQgT0xTIG9uIGVhY2ggY2FuZGlkYXRlIHNlZ21lbnQsICgyKSB1c2UgZHluYW1pYyBwcm9ncmFtbWluZyB0byBmaW5kIGdsb2JhbGx5IG9wdGltYWwgYnJlYWsgZGF0ZXMsICgzKSB0ZXN0IHZpYSBzdXAtRiBhbmQgc2VxdWVudGlhbCBzdXAtRiBmb3IgdGhlIG51bWJlciBvZiBicmVha3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHN0YXRzbW9kZWxzLmFwaSBhcyBzbVxuZnJvbSBzdGF0c21vZGVscy5zdGF0cy5kaWFnbm9zdGljIGltcG9ydCBicmVha3NfY3VzdW1vbHNyZXNpZFxuXG5ucC5yYW5kb20uc2VlZCg1KVxuVCA9IDIwMFxudCA9IG5wLmFyYW5nZShUKVxuIyBTdHJ1Y3R1cmFsIGJyZWFrOiBpbnRlcmNlcHQgc2hpZnRzIGF0IHQ9MTAwXG55ID0gbnAud2hlcmUodCBcdTAwM2MgMTAwLCAyLjAgKyAwLjAxKnQgKyBucC5yYW5kb20ucmFuZG4oVCkqMC41LFxuICAgICAgICAgICAgICAgICAgICAgICA1LjAgKyAwLjAxKnQgKyBucC5yYW5kb20ucmFuZG4oVCkqMC41KVxuWCA9IHNtLmFkZF9jb25zdGFudCh0LnJlc2hhcGUoLTEsIDEpKVxuXG4jIE9MUyBiYXNlbGluZVxubW9kZWwgPSBzbS5PTFMoeSwgWCkuZml0KClcbnByaW50KGZcdTAwMjdPTFMgUi1zcXVhcmVkOiB7bW9kZWwucnNxdWFyZWQ6LjRmfVx1MDAyNylcblxuIyBDVVNVTSBvZiBPTFMgcmVzaWR1YWxzIHRlc3QgZm9yIHN0cnVjdHVyYWwgaW5zdGFiaWxpdHlcbmN1c3VtX3N0YXQsIGN1c3VtX3B2YWwsIGN1c3VtX2NyaXQgPSBicmVha3NfY3VzdW1vbHNyZXNpZChtb2RlbC5yZXNpZCwgZGRvZj0yKVxucHJpbnQoZlx1MDAyN0NVU1VNLU9MUyBzdGF0OiB7Y3VzdW1fc3RhdDouNGZ9LCBwLXZhbHVlOiB7Y3VzdW1fcHZhbDouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JlamVjdCBzdHJ1Y3R1cmFsIHN0YWJpbGl0eToge2N1c3VtX3B2YWwgXHUwMDNjIDAuMDV9XHUwMDI3KVxuXG4jIE1hbnVhbCBDaG93IHRlc3QgYXQga25vd24gYnJlYWsgdD0xMDBcbm1vZGVsX3ByZSAgPSBzbS5PTFMoeVs6MTAwXSwgWFs6MTAwXSkuZml0KClcbm1vZGVsX3Bvc3QgPSBzbS5PTFMoeVsxMDA6XSwgWFsxMDA6XSkuZml0KClcbnJzc19jb21iaW5lZCA9IG1vZGVsLnNzclxucnNzX3NwbGl0ICAgID0gbW9kZWxfcHJlLnNzciArIG1vZGVsX3Bvc3Quc3NyXG5rID0gWC5zaGFwZVsxXVxuRl9jaG93ID0gKChyc3NfY29tYmluZWQgLSByc3Nfc3BsaXQpIC8gaykgLyAocnNzX3NwbGl0IC8gKFQgLSAyKmspKVxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgZiBhcyBmX2Rpc3RcbnBfY2hvdyA9IDEgLSBmX2Rpc3QuY2RmKEZfY2hvdywgZGZuPWssIGRmZD1UIC0gMiprKVxucHJpbnQoZlx1MDAyN0Nob3cgRi1zdGF0OiB7Rl9jaG93Oi40Zn0sIHAtdmFsdWU6IHtwX2Nob3c6LjRmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQ2hvb3NpbmcgT2ZmbGluZSB2cyBPbmxpbmUgTWV0aG9kcyIsImNvbnRlbnQiOiJVc2UgUEVMVCBvciBydXB0dXJlcyBmb3IgcmV0cm9zcGVjdGl2ZSBhbmFseXNpcyB3aGVyZSB5b3UgaGF2ZSB0aGUgZnVsbCBzZXJpZXMgYW5kIHdhbnQgZ2xvYmFsbHkgb3B0aW1hbCBzZWdtZW50YXRpb24uIFVzZSBCT0NQRCB3aGVuIG9wZXJhdGluZyBpbiByZWFsIHRpbWUgYW5kIG5lZWRpbmcgcG9zdGVyaW9yIHVuY2VydGFpbnR5IG92ZXIgdGhlIGNoYW5nZSBwb2ludCBsb2NhdGlvbi4gVXNlIEJhaS1QZXJyb24gZm9yIGVjb25vbWV0cmljIHNlcmllcyB3aGVyZSBmb3JtYWwgaHlwb3RoZXNpcyB0ZXN0aW5nIGFuZCBjb25maWRlbmNlIGludGVydmFscyBvbiBicmVhayBkYXRlcyBhcmUgcmVxdWlyZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hhbmdlIFBvaW50IE1ldGhvZCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIk9ubGluZS9PZmZsaW5lIiwiQmF5ZXNpYW4iLCJNdWx0aXBsZSBDUHMiLCJDb3N0IEZ1bmN0aW9uIiwiQ29tcGxleGl0eSJdLCJyb3dzIjpbWyJQRUxUIiwiT2ZmbGluZSIsIk5vIiwiWWVzIChleGFjdCkiLCJNb2R1bGFyIChMMiwgUkJGLCBBUikiLCJPKG4pIGF2ZywgTyhuwrIpIHdvcnN0Il0sWyJCaW5hcnkgU2VnbWVudGF0aW9uIiwiT2ZmbGluZSIsIk5vIiwiWWVzIChncmVlZHkpIiwiTW9kdWxhciIsIk8obiBsb2cgbikiXSxbIldpbmRvdyBTbGlkaW5nIiwiT2ZmbGluZSIsIk5vIiwiWWVzIChhcHByb3gpIiwiTW9kdWxhciIsIk8obikiXSxbIkJPQ1BEIiwiT25saW5lIiwiWWVzIiwiU2VxdWVudGlhbCAob25lIGF0IGEgdGltZSkiLCJDb25qdWdhdGUgbW9kZWxzIiwiTyh0KSBwZXIgc3RlcCJdLFsiQk9DUEQtQVJHUCIsIk9ubGluZSIsIlllcyIsIlNlcXVlbnRpYWwiLCJHUC1iYXNlZCwgZmxleGlibGUiLCJPKHTCsikgcGVyIHN0ZXAiXSxbIkJhaS1QZXJyb24iLCJPZmZsaW5lIiwiTm8iLCJZZXMgKExSIHRlc3QpIiwiT0xTIHJlc2lkdWFscyIsIk8obsKyIGspIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQZW5hbHR5IFNlbGVjdGlvbiBhbmQgQ29zdCBGdW5jdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBlbmFsdHkgc2VsZWN0aW9uIGlzIHRoZSBoYXJkZXN0IHByYWN0aWNhbCBjaGFsbGVuZ2UgaW4gUEVMVCBhbmQgc2VnbWVudGF0aW9uIG1ldGhvZHMuIFRvbyBsb3cgYSBwZW5hbHR5IHlpZWxkcyB0b28gbWFueSBzZWdtZW50czsgdG9vIGhpZ2ggbWlzc2VzIHJlYWwgYnJlYWtzLiBQcmluY2lwbGVkIGNob2ljZXM6IEJJQyBwZW5hbHR5IM6yID0gZGltIMOXIGxvZyhuKSwgd2hlcmUgZGltIGlzIHRoZSBudW1iZXIgb2YgcGFyYW1ldGVycyB0aGF0IGNoYW5nZSBhdCBlYWNoIGJyZWFrLiBGb3IgdGhlIG1lYW4tc2hpZnQgbW9kZWwgKDEgcGFyYW1ldGVyKSwgzrIgPSBsb2cobikuIE1vZGlmaWVkIEJJQyAobWJpYyBpbiBydXB0dXJlcykgaXMgbW9yZSBjb25zZXJ2YXRpdmUuIEZvciBub24tcGFyYW1ldHJpYyBSQkYgY29zdCwgdGhlIHBlbmFsdHkgaGFzIG5vIGNsb3NlZCBmb3JtIGFuZCBtdXN0IGJlIGNhbGlicmF0ZWQgYnkgY3Jvc3MtdmFsaWRhdGlvbiBvciB0aGUgZWxib3cgbWV0aG9kIG9uIHRvdGFsIGNvc3QgdnMgSy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkwyIGNvc3QgKE1TRSk6IGRldGVjdHMgbWVhbiBzaGlmdHM7IGluc2Vuc2l0aXZlIHRvIHZhcmlhbmNlIGNoYW5nZXMuIiwiUkJGIGtlcm5lbCBjb3N0OiBub24tcGFyYW1ldHJpYywgZGV0ZWN0cyBtZWFuIGFuZCB2YXJpYW5jZSBjaGFuZ2VzOyBubyBkaXN0cmlidXRpb25hbCBhc3N1bXB0aW9uLiIsIkFSIGNvc3Q6IGRldGVjdHMgY2hhbmdlcyBpbiBhdXRvcmVncmVzc2l2ZSBzdHJ1Y3R1cmU7IHVzZWZ1bCBmb3IgdGltZSBzZXJpZXMgd2l0aCBhdXRvY29ycmVsYXRpb24uIiwiUEVMVCBtaW5fc2l6ZTogbWluaW11bSBzZWdtZW50IGxlbmd0aCB0byBhdm9pZCB0cml2aWFsIHNpbmdsZS1wb2ludCBzZWdtZW50cyAodHlwaWNhbGx5IDEwLTMwKS4iLCJCT0NQRCBoYXphcmQ9MS/Ouzogc2V0IM67IHRvIGV4cGVjdGVkIG1lYW4gc2VnbWVudCBsZW5ndGggaW4gbnVtYmVyIG9mIG9ic2VydmF0aW9ucy4iLCJFbGJvdyBwbG90OiBwbG90IHRvdGFsIGNvc3QgdnMgbnVtYmVyIG9mIGJyZWFrcG9pbnRzOyBwaWNrIHRoZSBlbGJvdyBmb3IgYXV0b21hdGljIEsgc2VsZWN0aW9uLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Change Point Detection — PELT and BOCPD

A change point is a time index τ at which the statistical properties of a time series shift: a change in mean, variance, trend, or full distribution. Change point detection is fundamental to segmentation, anomaly detection, and preprocessing before forecasting. Two dominant paradigms exist: offline (batch) methods that find all change points simultaneously given the full series, and online (streaming) methods that detect change points sequentially as data arrives.

## What Is a Change Point?

Given a time series y_{1:n}, a change point τ partitions the series into segments with different distributional parameters. For K change points at τ_1 < τ_2 < ... < τ_K, each segment y_{τ_{k-1}+1:τ_k} is assumed i.i.d. from some distribution P_k. The cost of a segment is C(y_{a:b}), e.g., negative log-likelihood or sum of squared deviations from the segment mean. The objective is to minimise total cost + a penalty βK for K segments: Σ C(y_{τ_{k-1}:τ_k}) + βK.

## PELT — Pruned Exact Linear Time

PELT (Killick et al., 2012) solves the segmentation problem exactly using dynamic programming with a pruning condition. Define F(t) = min cost of segmenting y_{1:t}. The recursion is F(t) = min_{τ < t} [F(τ) + C(y_{τ+1:t}) + β]. PELT prunes candidate change points: if F(τ) + C(y_{τ+1:s}) + β ≥ F(s) for some s, then τ can never be the last change point for any future time t. Under mild conditions this achieves O(n) expected complexity (empirically O(n log n)).

```python
import numpy as np

def pelt(y, penalty=10.0):
    """
    PELT change point detection with MSE cost (mean shift model).
    Returns list of change point indices (starts of new segments).
    """
    n = len(y)
    F = np.full(n + 1, np.inf)
    F[0] = -penalty
    last_cp = [-1] * (n + 1)
    admissible = [0]  # candidate last change points

    def seg_cost(s, e):
        """MSE cost: sum of squared deviations from segment mean."""
        seg = y[s:e]
        return np.sum((seg - seg.mean())**2)

    for t in range(1, n + 1):
        best_cost = np.inf
        new_admissible = []
        for tau in admissible:
            cost = F[tau] + seg_cost(tau, t) + penalty
            if cost < best_cost:
                best_cost = cost
                F[t] = best_cost
                last_cp[t] = tau
        # Pruning: remove tau if F[tau] + seg_cost(tau, t) + penalty >= F[t]
        for tau in admissible:
            if F[tau] + seg_cost(tau, t) <= F[t]:
                new_admissible.append(tau)
        new_admissible.append(t)
        admissible = new_admissible

    # Backtrack change points
    cps, idx = [], n
    while last_cp[idx] > 0:
        cps.append(last_cp[idx])
        idx = last_cp[idx]
    return sorted(cps)

np.random.seed(42)
y = np.concatenate([np.random.randn(80), np.random.randn(80) + 3.0,
                    np.random.randn(80) - 1.5])
cps = pelt(y, penalty=15.0)
print(f'True change points: [80, 160]')
print(f'PELT detected:      {cps}')
```

## ruptures Library — Multiple Change Point Detection

The ruptures library (Truong et al., 2020) provides PELT, Binary Segmentation, Bottom-Up, and Window Sliding methods with modular cost functions (MSE, RBF kernel, linear, AR). Cost choices: l2 (mean shift), rbf (non-parametric, distribution-free), ar (autoregressive change). Penalty selection: BIC (β = log(n) × dim), modified BIC (mbic), or cross-validation. ruptures also offers an n_bkps interface when the number of change points is known.

```python
import numpy as np
import ruptures as rpt

np.random.seed(1)
signal, true_cps = rpt.pw_constant(n_samples=300, n_features=1, n_bkps=3, noise_std=0.5)
true_cps = [t for t in true_cps if t < 300]

# PELT with RBF cost (non-parametric, works for mean + variance changes)
algo_pelt = rpt.Pelt(model='rbf', min_size=10, jump=1).fit(signal)
cps_pelt  = algo_pelt.predict(pen=3.0)[:-1]  # last element is n, exclude it

# Binary Segmentation (faster but approximate) with L2 cost
algo_binseg = rpt.Binseg(model='l2').fit(signal)
cps_binseg  = algo_binseg.predict(n_bkps=3)[:-1]

# Window Sliding
algo_window = rpt.Window(width=30, model='l2').fit(signal)
cps_window  = algo_window.predict(n_bkps=3)[:-1]

print(f'True change points: {true_cps}')
print(f'PELT (rbf, pen=3):  {cps_pelt}')
print(f'BinSeg (l2, K=3):   {cps_binseg}')
print(f'Window (l2, K=3):   {cps_window}')

# Evaluate: mean absolute error of detected vs true change points
def cp_error(detected, true):
    if not detected or not true:
        return float('inf')
    return np.mean([min(abs(d - t) for t in true) for d in detected])
print(f'PELT MAE to true CPs: {cp_error(cps_pelt, true_cps):.1f} steps')
```

## BOCPD — Bayesian Online Change Point Detection

BOCPD (Adams & MacKay, 2007) maintains a posterior distribution over the run length r_t (time since the last change point). At each step, it evaluates two hypotheses: (1) continue the current segment (run length grows by 1) or (2) a change point occurs (run length resets to 0). The hazard function H controls the prior probability of a change point at each step. Predictive distributions are computed using conjugate models (Normal-Inverse-Gamma for Gaussian data, or Student-t predictive). BOCPD is exact and online but O(t) per step.

```python
import numpy as np
from scipy.stats import t as student_t

def bocpd_gaussian(y, hazard=0.01, mu0=0.0, kappa0=1.0, alpha0=1.0, beta0=1.0):
    """
    Bayesian Online Change Point Detection with Normal-Inverse-Gamma prior.
    Returns: run_length_probs (T x T+1), change_point_probs (T,)
    """
    T = len(y)
    R = np.zeros((T + 1, T + 1))
    R[0, 0] = 1.0
    # Sufficient statistics for each run length
    mu   = np.full(T + 1, mu0)
    kappa = np.full(T + 1, kappa0)
    alpha = np.full(T + 1, alpha0)
    beta  = np.full(T + 1, beta0)
    cp_probs = np.zeros(T)

    for t in range(T):
        # Predictive: Student-t distribution
        df   = 2 * alpha
        scale = np.sqrt(beta * (kappa + 1) / (alpha * kappa))
        pred  = student_t.pdf(y[t], df=df, loc=mu, scale=scale) + 1e-300
        # Growth: run length increments
        R[t + 1, 1:t + 2] = R[t, :t + 1] * pred[:t + 1] * (1 - hazard)
        # Change point: run length resets
        R[t + 1, 0] = np.sum(R[t, :t + 1] * pred[:t + 1]) * hazard
        R[t + 1] /= (R[t + 1].sum() + 1e-300)  # normalise
        # MAP run length
        cp_probs[t] = R[t + 1, 0]
    return R, cp_probs

np.random.seed(3)
y = np.concatenate([np.random.randn(100), np.random.randn(100) + 3.0])
R, cp_probs = bocpd_gaussian(y, hazard=1/50)
print(f'Max CP prob location: {cp_probs.argmax()} (true change point: 100)')
print(f'CP prob at t=100: {cp_probs[100]:.4f}')
print(f'CP prob at t=50:  {cp_probs[50]:.4f}')
```

## Bai-Perron Structural Break Test

In econometrics, structural breaks are tested formally. The Chow test checks for a break at a known date. The Bai-Perron test (1998, 2003) allows an unknown number of breaks: it estimates break dates and tests their significance using supF statistics. statsmodels implements this as BreakpointEstimator. The Bai-Perron procedure: (1) fit OLS on each candidate segment, (2) use dynamic programming to find globally optimal break dates, (3) test via sup-F and sequential sup-F for the number of breaks.

```python
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import breaks_cusumolsresid

np.random.seed(5)
T = 200
t = np.arange(T)
# Structural break: intercept shifts at t=100
y = np.where(t < 100, 2.0 + 0.01*t + np.random.randn(T)*0.5,
                       5.0 + 0.01*t + np.random.randn(T)*0.5)
X = sm.add_constant(t.reshape(-1, 1))

# OLS baseline
model = sm.OLS(y, X).fit()
print(f'OLS R-squared: {model.rsquared:.4f}')

# CUSUM of OLS residuals test for structural instability
cusum_stat, cusum_pval, cusum_crit = breaks_cusumolsresid(model.resid, ddof=2)
print(f'CUSUM-OLS stat: {cusum_stat:.4f}, p-value: {cusum_pval:.4f}')
print(f'Reject structural stability: {cusum_pval < 0.05}')

# Manual Chow test at known break t=100
model_pre  = sm.OLS(y[:100], X[:100]).fit()
model_post = sm.OLS(y[100:], X[100:]).fit()
rss_combined = model.ssr
rss_split    = model_pre.ssr + model_post.ssr
k = X.shape[1]
F_chow = ((rss_combined - rss_split) / k) / (rss_split / (T - 2*k))
from scipy.stats import f as f_dist
p_chow = 1 - f_dist.cdf(F_chow, dfn=k, dfd=T - 2*k)
print(f'Chow F-stat: {F_chow:.4f}, p-value: {p_chow:.4f}')
```

> **Choosing Offline vs Online Methods**: Use PELT or ruptures for retrospective analysis where you have the full series and want globally optimal segmentation. Use BOCPD when operating in real time and needing posterior uncertainty over the change point location. Use Bai-Perron for econometric series where formal hypothesis testing and confidence intervals on break dates are required.

## Change Point Method Comparison

| Method | Online/Offline | Bayesian | Multiple CPs | Cost Function | Complexity |
| --- | --- | --- | --- | --- | --- |
| PELT | Offline | No | Yes (exact) | Modular (L2, RBF, AR) | O(n) avg, O(n²) worst |
| Binary Segmentation | Offline | No | Yes (greedy) | Modular | O(n log n) |
| Window Sliding | Offline | No | Yes (approx) | Modular | O(n) |
| BOCPD | Online | Yes | Sequential (one at a time) | Conjugate models | O(t) per step |
| BOCPD-ARGP | Online | Yes | Sequential | GP-based, flexible | O(t²) per step |
| Bai-Perron | Offline | No | Yes (LR test) | OLS residuals | O(n² k) |

## Penalty Selection and Cost Functions

Penalty selection is the hardest practical challenge in PELT and segmentation methods. Too low a penalty yields too many segments; too high misses real breaks. Principled choices: BIC penalty β = dim × log(n), where dim is the number of parameters that change at each break. For the mean-shift model (1 parameter), β = log(n). Modified BIC (mbic in ruptures) is more conservative. For non-parametric RBF cost, the penalty has no closed form and must be calibrated by cross-validation or the elbow method on total cost vs K.

- L2 cost (MSE): detects mean shifts; insensitive to variance changes.
- RBF kernel cost: non-parametric, detects mean and variance changes; no distributional assumption.
- AR cost: detects changes in autoregressive structure; useful for time series with autocorrelation.
- PELT min_size: minimum segment length to avoid trivial single-point segments (typically 10-30).
- BOCPD hazard=1/λ: set λ to expected mean segment length in number of observations.
- Elbow plot: plot total cost vs number of breakpoints; pick the elbow for automatic K selection.

---

