---
title: "ARIMA — AR, I, MA Components and Box-Jenkins Methodology"
slug: "arima"
description: "Derive AR, MA, and ARIMA models from first principles, understand invertibility and stationarity conditions, walk through Box-Jenkins identification and MLE estimation, and apply automatic order selection with pmdarima."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQVJJTUEg4oCUIEF1dG9SZWdyZXNzaXZlIEludGVncmF0ZWQgTW92aW5nIEF2ZXJhZ2Ug4oCUIGlzIHRoZSB3b3JraG9yc2UgbW9kZWwgb2YgY2xhc3NpY2FsIHRpbWUtc2VyaWVzIGZvcmVjYXN0aW5nLiBJdCB1bmlmaWVzIHRocmVlIGlkZWFzOiBBUiB0ZXJtcyBjYXB0dXJlIGRlcGVuZGVuY2Ugb24gcGFzdCB2YWx1ZXMsIE1BIHRlcm1zIGNhcHR1cmUgZGVwZW5kZW5jZSBvbiBwYXN0IGZvcmVjYXN0IGVycm9ycywgYW5kIHRoZSBJIChpbnRlZ3JhdGVkKSBjb21wb25lbnQgaGFuZGxlcyBub24tc3RhdGlvbmFyaXR5IGJ5IGRpZmZlcmVuY2luZy4gQm94IGFuZCBKZW5raW5zICgxOTcwKSBmb3JtYWxpc2VkIGEgc3lzdGVtYXRpYyBtZXRob2RvbG9neSBmb3IgaWRlbnRpZnlpbmcsIGVzdGltYXRpbmcsIGFuZCBkaWFnbm9zaW5nIEFSSU1BIG1vZGVscyB0aGF0IHJlbWFpbnMgc3RhbmRhcmQgcHJhY3RpY2UgZmlmdHkgeWVhcnMgbGF0ZXIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQVIocCkg4oCUIEF1dG9yZWdyZXNzaXZlIFByb2Nlc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuIEFSKHApIG1vZGVsIGV4cHJlc3NlcyB0aGUgY3VycmVudCB2YWx1ZSBhcyBhIGxpbmVhciBjb21iaW5hdGlvbiBvZiBwIHBhc3QgdmFsdWVzIHBsdXMgd2hpdGUgbm9pc2U6IHnigpwgPSBjICsgz4bigoF54oKc4oKL4oKBICsgz4bigoJ54oKc4oKL4oKCICsg4oCmICsgz4bigpp54oKc4oKL4oKaICsgzrXigpwuIFVzaW5nIHRoZSBiYWNrc2hpZnQgb3BlcmF0b3IgQiAoQsqyeeKCnCA9IHnigpzigovisbwpLCB0aGlzIGlzICgxIOKIkiDPhuKCgUIg4oiSIM+G4oKCQsKyIOKIkiDigKYg4oiSIM+G4oKaQuG1lil54oKcID0gYyArIM614oKcLiBTdGF0aW9uYXJpdHkgcmVxdWlyZXMgYWxsIHJvb3RzIG9mIHRoZSBjaGFyYWN0ZXJpc3RpYyBwb2x5bm9taWFsIM+GKHopID0gMSDiiJIgz4bigoF6IOKIkiDigKYg4oiSIM+G4oKaeuG1liB0byBsaWUgc3RyaWN0bHkgb3V0c2lkZSB0aGUgdW5pdCBjaXJjbGUgaW4gdGhlIGNvbXBsZXggcGxhbmUuIEFuIEFSKDEpIHdpdGggz4bigoEgPSAxIGlzIHRoZSByYW5kb20gd2FsayAodW5pdCByb290LCBub24tc3RhdGlvbmFyeSkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTUEocSkg4oCUIE1vdmluZyBBdmVyYWdlIFByb2Nlc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuIE1BKHEpIG1vZGVsIGV4cHJlc3NlcyB0aGUgY3VycmVudCB2YWx1ZSBhcyBhIGxpbmVhciBjb21iaW5hdGlvbiBvZiBxIHBhc3QgZXJyb3JzOiB54oKcID0gzrwgKyDOteKCnCArIM644oKBzrXigpzigovigoEgKyDigKYgKyDOuHHOteKCnOKCi3EuIE1BIHByb2Nlc3NlcyBhcmUgYWx3YXlzIHN0YXRpb25hcnkgcmVnYXJkbGVzcyBvZiB0aGUgzrggdmFsdWVzIGJlY2F1c2UgdGhleSBhcmUgZmluaXRlIHN1bXMgb2Ygd2hpdGUgbm9pc2UuIEludmVydGliaWxpdHkg4oCUIHRoZSBjb25kaXRpb24gdGhhdCBtYWtlcyB0aGUgTUEgcmVwcmVzZW50YWJsZSBhcyBhbiBpbmZpbml0ZSBBUiDigJQgcmVxdWlyZXMgcm9vdHMgb2YgzrgoeikgPSAxICsgzrjigoF6ICsg4oCmICsgzrhxenEgdG8gbGllIG91dHNpZGUgdGhlIHVuaXQgY2lyY2xlLiBOb24taW52ZXJ0aWJsZSBNQSBtb2RlbHMgYXJlIHN0YXRpc3RpY2FsbHkgaW5kaXN0aW5ndWlzaGFibGUgZnJvbSBpbnZlcnRpYmxlIG9uZXMgYnkgdGhlaXIgQUNGLCBidXQgZ2l2ZSBkaWZmZXJlbnQgZm9yZWNhc3RzOyBieSBjb252ZW50aW9uIHdlIGFsd2F5cyBjaG9vc2UgdGhlIGludmVydGlibGUgcmVwcmVzZW50YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQVJJTUEocCxkLHEpIOKAlCBJbnRlZ3JhdGlvbiBhbmQgRGlmZmVyZW5jaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBUklNQShwLGQscSkgYXBwbGllcyBkIGRpZmZlcmVuY2VzIHRvIHnigpwgYmVmb3JlIGZpdHRpbmcgYW4gQVJNQShwLHEpOiBsZXQgd+KCnCA9IM6U4bWIeeKCnCA9ICgx4oiSQinhtYh54oKcOyB0aGVuIM+GKEIpd+KCnCA9IM64KEIpzrXigpwuIFRoZSBkIHBhcmFtZXRlciBpcyB0aGUgbnVtYmVyIG9mIHVuaXQgcm9vdHMgaW4gdGhlIG9yaWdpbmFsIHNlcmllcy4gQVJJTUEoMCwxLDApIGlzIHRoZSByYW5kb20gd2FsazsgQVJJTUEoMCwyLDApIGlzIHRoZSByYW5kb20gYWNjZWxlcmF0aW9uIChkb3VibGUtaW50ZWdyYXRlZCByYW5kb20gd2FsaykuIE1vc3QgZWNvbm9taWMgYW5kIGZpbmFuY2lhbCBzZXJpZXMgcmVxdWlyZSBkID0gMSBvciBkID0gMDsgb3Zlci1kaWZmZXJlbmNpbmcgKHVzaW5nIGQgPSAyIHdoZW4gZCA9IDEgc3VmZmljZXMpIGludHJvZHVjZXMgc3B1cmlvdXMgTUEgc3RydWN0dXJlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc3RhdHNtb2RlbHMudHNhLnN0YXR0b29scyBpbXBvcnQgYWNmXG5cbm5wLnJhbmRvbS5zZWVkKDApXG5uID0gMzAwXG5lcHMgPSBucC5yYW5kb20ucmFuZG4obiArIDUpXG5cbiMgU2ltdWxhdGUgQVIoMik6IHBoaTE9MC43LCBwaGkyPS0wLjJcbnlfYXIyID0gbnAuemVyb3MobilcbmZvciB0IGluIHJhbmdlKDIsIG4pOlxuICAgIHlfYXIyW3RdID0gMC43KnlfYXIyW3QtMV0gLSAwLjIqeV9hcjJbdC0yXSArIGVwc1t0XVxuXG4jIFNpbXVsYXRlIE1BKDIpOiB0aGV0YTE9MC42LCB0aGV0YTI9MC4zXG55X21hMiA9IG5wLmFycmF5KFtlcHNbdF0gKyAwLjYqZXBzW3QtMV0gKyAwLjMqZXBzW3QtMl0gZm9yIHQgaW4gcmFuZ2UoMiwgbisyKV0pXG5cbiMgU2ltdWxhdGUgQVJJTUEoMSwxLDEpOiBkaWZmZXJlbmNlIG9uY2UgdG8gZ2V0IHN0YXRpb25hcnlcbnd0ID0gbnAuemVyb3MobilcbmZvciB0IGluIHJhbmdlKDEsIG4pOlxuICAgIHd0W3RdID0gMC41Knd0W3QtMV0gKyBlcHNbdF0gKyAwLjQqZXBzW3QtMV1cbnlfYXJpbWEgPSBucC5jdW1zdW0od3QpICAjIGludGVncmF0ZSBvbmNlOiBkPTFcblxucHJpbnQoXCJQcm9jZXNzIHN0YXRpc3RpY3MgKGFsbCBjb21wdXRlZCBvbiBzdGF0aW9uYXJ5IGZvcm0pOlwiKVxucHJpbnQoZlwiQVIoMik6ICBtZWFuPXt5X2FyMi5tZWFuKCk6LjNmfSAgc3RkPXt5X2FyMi5zdGQoKTouM2Z9XCIpXG5wcmludChmXCJNQSgyKTogIG1lYW49e3lfbWEyLm1lYW4oKTouM2Z9ICBzdGQ9e3lfbWEyLnN0ZCgpOi4zZn1cIilcbnByaW50KGZcIkFSSU1BKDEsMSwxKSBmaXJzdC1kaWZmIG1lYW49e25wLmRpZmYoeV9hcmltYSkubWVhbigpOi4zZn0gIHN0ZD17bnAuZGlmZih5X2FyaW1hKS5zdGQoKTouM2Z9XCIpXG5cbiMgVmVyaWZ5IEFSKDIpIHN0YXRpb25hcml0eSB2aWEgY2hhcmFjdGVyaXN0aWMgcm9vdHNcbmltcG9ydCBudW1weS5wb2x5bm9taWFsLnBvbHlub21pYWwgYXMgUFxucm9vdHMgPSBucC5yb290cyhbMSwgLTAuNywgMC4yXSkgICMgY2hhciBwb2x5OiAxIC0gMC43eiAtICgtMC4yKXpeMi4uLiBub3RlIHNpZ25cbnByaW50KGZcIkFSKDIpIGNoYXIgcm9vdHMgbW9kdWx1czoge25wLmFicyhyb290cyl9ICAobXVzdCBiZSBcdTAwM2UgMSBmb3Igc3RhdGlvbmFyaXR5KVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJveC1KZW5raW5zIE1ldGhvZG9sb2d5IOKAlCBTdGVwIGJ5IFN0ZXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJveC1KZW5raW5zIGlzIGFuIGl0ZXJhdGl2ZSBpZGVudGlmaWNhdGlvbi1lc3RpbWF0aW9uLWRpYWdub3N0aWMtZm9yZWNhc3QgY3ljbGUuIEl0IHJlcXVpcmVzIHRoZSBhbmFseXN0IHRvIGludGVyYWN0IHdpdGggdGhlIGRhdGEgYXQgZWFjaCBzdGFnZTogcmVzaWR1YWwgZGlhZ25vc3RpY3MgZmVlZCBiYWNrIGludG8gbW9kZWwgaWRlbnRpZmljYXRpb24uIEF1dG9tYXRlZCBhcHByb2FjaGVzIChhdXRvX2FyaW1hKSBjYW4gbWltaWMgdGhlIGN5Y2xlLCBidXQgdW5kZXJzdGFuZGluZyB0aGUgbWFudWFsIHByb2NlZHVyZSBpcyBlc3NlbnRpYWwgZm9yIGRpYWdub3NpbmcgZmFpbHVyZXMgYW5kIGhhbmRsaW5nIHVudXN1YWwgc2VyaWVzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjp0cnVlLCJpdGVtcyI6WyJJZGVudGlmaWNhdGlvbjogUGxvdCB0aGUgc2VyaWVzLCB0ZXN0IGZvciBzdGF0aW9uYXJpdHkgKEFERi9LUFNTKSwgZGV0ZXJtaW5lIGQuIFRoZW4gcGxvdCBBQ0YgYW5kIFBBQ0Ygb2YgdGhlIGRpZmZlcmVuY2VkIHNlcmllcyB0byBpZGVudGlmeSBjYW5kaWRhdGUgKHAsIHEpLiIsIkVzdGltYXRpb246IEZpdCB0aGUgQVJJTUEocCxkLHEpIGJ5IE1heGltdW0gTGlrZWxpaG9vZC4gVGhlIGxpa2VsaWhvb2QgaXMgY29tcHV0ZWQgdmlhIHRoZSBLYWxtYW4gZmlsdGVyIChvciBpbm5vdmF0aW9ucyBhbGdvcml0aG0pIHRyZWF0aW5nIHRoZSBtb2RlbCBpbiBzdGF0ZSBzcGFjZSBmb3JtLiIsIkRpYWdub3N0aWMgY2hlY2tpbmc6IFBsb3QgcmVzaWR1YWwgQUNGL1BBQ0YgKHNob3VsZCBiZSB3aGl0ZSBub2lzZSksIHJ1biBManVuZy1Cb3ggdGVzdCwgY2hlY2sgbm9ybWFsaXR5IHdpdGggUS1RIHBsb3QgYW5kIEphcnF1ZS1CZXJhIHRlc3QuIiwiTW9kZWwgc2VsZWN0aW9uOiBDb21wYXJlIGNhbmRpZGF0ZSBtb2RlbHMgYnkgQUlDID0g4oiSMsK3bG9nKEwpICsgMsK3ayBvciBCSUMgPSDiiJIywrdsb2coTCkgKyBrwrdsb2cobikuIEFJQyBmYXZvdXJzIHNsaWdodGx5IG1vcmUgY29tcGxleCBtb2RlbHM7IEJJQyBpcyBtb3JlIHBhcnNpbW9uaW91cy4iLCJGb3JlY2FzdGluZzogR2VuZXJhdGUgaC1zdGVwLWFoZWFkIHBvaW50IGZvcmVjYXN0cyBhbmQgcHJlZGljdGlvbiBpbnRlcnZhbHMuIEludGVydmFsIHdpZHRoIGdyb3dzIHdpdGggaG9yaXpvbiBhcyBmb3JlY2FzdCB1bmNlcnRhaW50eSBhY2N1bXVsYXRlcy4iXX0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2EuYXJpbWEubW9kZWwgaW1wb3J0IEFSSU1BXG5mcm9tIHN0YXRzbW9kZWxzLnN0YXRzLmRpYWdub3N0aWMgaW1wb3J0IGFjb3JyX2xqdW5nYm94XG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubiA9IDIwMFxuZXBzID0gbnAucmFuZG9tLnJhbmRuKG4gKyAyKVxuXG4jIFRydWUgcHJvY2VzczogQVJJTUEoMSwxLDEpXG53dCA9IG5wLnplcm9zKG4pXG5mb3IgdCBpbiByYW5nZSgxLCBuKTpcbiAgICB3dFt0XSA9IDAuNip3dFt0LTFdICsgZXBzW3RdICsgMC4zKmVwc1t0LTFdXG55ID0gbnAuY3Vtc3VtKHd0KVxuXG4jIEZpdCBBUklNQSgxLDEsMSlcbm1vZGVsID0gQVJJTUEoeSwgb3JkZXI9KDEsIDEsIDEpKVxuZml0ICAgPSBtb2RlbC5maXQoKVxuXG5wcmludChcIkFSSU1BKDEsMSwxKSBmaXQgc3VtbWFyeTpcIilcbnByaW50KGZcIiAgQVIgcGhpICA9IHtmaXQucGFyYW1zW1x1MDAyN2FyLkwxXHUwMDI3XTouNGZ9XCIpXG5wcmludChmXCIgIE1BIHRoZXRhID0ge2ZpdC5wYXJhbXNbXHUwMDI3bWEuTDFcdTAwMjddOi40Zn1cIilcbnByaW50KGZcIiAgc2lnbWFeMiAgPSB7Zml0LnBhcmFtc1tcdTAwMjdzaWdtYTJcdTAwMjddOi40Zn1cIilcbnByaW50KGZcIiAgQUlDICAgICAgPSB7Zml0LmFpYzouMmZ9XCIpXG5wcmludChmXCIgIEJJQyAgICAgID0ge2ZpdC5iaWM6LjJmfVwiKVxuXG4jIFJlc2lkdWFsIGRpYWdub3N0aWNzXG5yZXNpZCA9IGZpdC5yZXNpZFxubGIgPSBhY29ycl9sanVuZ2JveChyZXNpZFsyOl0sIGxhZ3M9WzEwLCAyMF0sIHJldHVybl9kZj1UcnVlKVxucHJpbnQoXCJcXG5ManVuZy1Cb3ggb24gcmVzaWR1YWxzOlwiKVxucHJpbnQobGJbW1x1MDAyN2xiX3N0YXRcdTAwMjcsIFx1MDAyN2xiX3B2YWx1ZVx1MDAyN11dLnRvX3N0cmluZygpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1dG9tYXRpYyBPcmRlciBTZWxlY3Rpb24gd2l0aCBhdXRvX2FyaW1hIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNYW51YWwgQm94LUplbmtpbnMgcmVxdWlyZXMgZXhwZXJpZW5jZSBhbmQgY2FuIGJlIGFtYmlndW91cyB3aGVuIEFDRi9QQUNGIHBhdHRlcm5zIGFyZSB1bmNsZWFyLiBUaGUgYXV0b19hcmltYSBmdW5jdGlvbiAocG1kYXJpbWEpIGF1dG9tYXRlcyBvcmRlciBzZWxlY3Rpb246IGl0IHNlYXJjaGVzIGEgZ3JpZCBvZiAocCwgZCwgcSkgY29tYmluYXRpb25zLCBlc3RpbWF0ZXMgZWFjaCBtb2RlbCB2aWEgTUxFLCBhbmQgcmV0dXJucyB0aGUgb25lIHdpdGggdGhlIGxvd2VzdCBBSUMgb3IgQklDLiBJdCBhbHNvIHRlc3RzIGZvciBzdGF0aW9uYXJpdHkgaW50ZXJuYWxseSAodXNpbmcgQURGKSB0byBkZXRlcm1pbmUgZCBhdXRvbWF0aWNhbGx5LCBhbmQgY2FuIGhhbmRsZSBzZWFzb25hbCBvcmRlcnMuIFRoZSBzZWFyY2ggaXMgbWFkZSBlZmZpY2llbnQgYnkgYSBzdGVwd2lzZSBhbGdvcml0aG0gdGhhdCBzdGFydHMgZnJvbSBhIGRlZmF1bHQgbW9kZWwgYW5kIGV4cGxvcmVzIG5laWdoYm91cmluZyBvcmRlcnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHBtZGFyaW1hIGFzIHBtXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5hcmltYS5tb2RlbCBpbXBvcnQgQVJJTUFcblxubnAucmFuZG9tLnNlZWQoNSlcbm4gPSAzMDBcbmVwcyA9IG5wLnJhbmRvbS5yYW5kbihuICsgMylcblxuIyBUcnVlIEFSSU1BKDIsMSwxKSBwcm9jZXNzXG53dCA9IG5wLnplcm9zKG4pXG5mb3IgdCBpbiByYW5nZSgyLCBuKTpcbiAgICB3dFt0XSA9IDAuNSp3dFt0LTFdIC0gMC4yKnd0W3QtMl0gKyBlcHNbdF0gKyAwLjQqZXBzW3QtMV1cbnkgPSBucC5jdW1zdW0od3QpXG5cbiMgQXV0by1BUklNQSBzZWFyY2hcbmF1dG8gPSBwbS5hdXRvX2FyaW1hKFxuICAgIHksXG4gICAgc3RhcnRfcD0wLCBtYXhfcD00LFxuICAgIHN0YXJ0X3E9MCwgbWF4X3E9NCxcbiAgICBkPU5vbmUsICAgICAgICAjIGF1dG8tZGV0ZXJtaW5lIHZpYSBBREYgdGVzdFxuICAgIGluZm9ybWF0aW9uX2NyaXRlcmlvbj1cdTAwMjdhaWNcdTAwMjcsXG4gICAgc3RlcHdpc2U9VHJ1ZSxcbiAgICBzZWFzb25hbD1GYWxzZSxcbiAgICBlcnJvcl9hY3Rpb249XHUwMDI3aWdub3JlXHUwMDI3LFxuICAgIHN1cHByZXNzX3dhcm5pbmdzPVRydWVcbilcblxucHJpbnQoZlwiQmVzdCBvcmRlciBzZWxlY3RlZDogQVJJTUF7YXV0by5vcmRlcn1cIilcbnByaW50KGZcIkFJQz17YXV0by5haWMoKTouMmZ9ICBCSUM9e2F1dG8uYmljKCk6LjJmfVwiKVxucHJpbnQoYXV0by5zdW1tYXJ5KCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRm9yZWNhc3RpbmcgYW5kIFByZWRpY3Rpb24gSW50ZXJ2YWxzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2EuYXJpbWEubW9kZWwgaW1wb3J0IEFSSU1BXG5cbm5wLnJhbmRvbS5zZWVkKDEwKVxubiA9IDE1MFxuZXBzID0gbnAucmFuZG9tLnJhbmRuKG4gKyAxKVxuXG53dCA9IG5wLnplcm9zKG4pXG5mb3IgdCBpbiByYW5nZSgxLCBuKTpcbiAgICB3dFt0XSA9IDAuNyp3dFt0LTFdICsgZXBzW3RdICsgMC4yKmVwc1t0LTFdXG55ID0gbnAuY3Vtc3VtKHd0KVxuXG50cmFpbiwgdGVzdCA9IHlbOjEyMF0sIHlbMTIwOl1cblxuZml0ID0gQVJJTUEodHJhaW4sIG9yZGVyPSgxLCAxLCAxKSkuZml0KClcblxuZm9yIGggaW4gWzEsIDUsIDEwLCAyMCwgMzBdOlxuICAgIGZjID0gZml0LmdldF9mb3JlY2FzdChzdGVwcz1oKVxuICAgIG1lYW5fZmMgID0gZmMucHJlZGljdGVkX21lYW5cbiAgICBjaSAgICAgICA9IGZjLmNvbmZfaW50KGFscGhhPTAuMDUpXG4gICAgaW50ZXJ2YWwgPSBjaS5pbG9jWy0xLCAxXSAtIGNpLmlsb2NbLTEsIDBdICAjIHdpZHRoIGF0IGhvcml6b24gaFxuICAgIHByaW50KGZcImg9e2g6MmR9OiBwb2ludD17bWVhbl9mYy5pbG9jWy0xXTorNy4zZn0gIDk1JSBDSSB3aWR0aD17aW50ZXJ2YWw6LjNmfVwiKVxuXG5wcmludChcIlxcbkludGVydmFsIHdpZHRoIGdyb3dzIHdpdGggaG9yaXpvbiAtLSB1bmNlcnRhaW50eSBhY2N1bXVsYXRlcyBvdmVyIHRpbWVcIilcbnByaW50KFwiRm9yIEFSSU1BKDEsMSwxKSwgbG9uZy1ydW4gZm9yZWNhc3QgY29udmVyZ2VzIHRvIGEgcmFuZG9tIHdhbGsgcGF0dGVyblwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQVJJTUEgUHJlZGljdGlvbiBJbnRlcnZhbHMgQXNzdW1lIE5vcm1hbCBFcnJvcnMiLCJjb250ZW50IjoiUHJlZGljdGlvbiBpbnRlcnZhbHMgZm9yIEFSSU1BIGFyZSBleGFjdCBvbmx5IHdoZW4gzrXigpwgfiBOKDAsIM+DwrIpLiBGb3IgZmF0LXRhaWxlZCByZXNpZHVhbHMgKGNvbW1vbiBpbiBmaW5hbmNpYWwgcmV0dXJucyksIHRoZSBub3JtYWwtYmFzZWQgaW50ZXJ2YWxzIHVuZGVyLWNvdmVyIGF0IGhpZ2ggc2lnbmlmaWNhbmNlIGxldmVscy4gQ2hlY2sgcmVzaWR1YWwgUS1RIHBsb3RzOiBpZiB0YWlscyBhcmUgaGVhdmllciB0aGFuIG5vcm1hbCwgY29uc2lkZXIgYm9vdHN0cmFwcGVkIHByZWRpY3Rpb24gaW50ZXJ2YWxzIG9yIHN3aXRjaCB0byBhIG1vZGVsIHdpdGggdC1kaXN0cmlidXRlZCBpbm5vdmF0aW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBUklNQSBPcmRlciBTZWxlY3Rpb24gR3VpZGUifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQUNGIFBhdHRlcm4iLCJQQUNGIFBhdHRlcm4iLCJBREYgUmVzdWx0IiwiU3VnZ2VzdGVkIGQiLCJTdWdnZXN0ZWQgcCIsIlN1Z2dlc3RlZCBxIl0sInJvd3MiOltbIkRlY2F5cyBzbG93bHksIG5lYXIgMSIsIk5lYXIgMSBhdCBsYWcgMSB0aGVuIGRyb3BzIiwiRmFpbCB0byByZWplY3QgKG5vbi1zdGF0KSIsIjEiLCLigJQiLCLigJQiXSxbIkN1dHMgb2ZmIGFmdGVyIGxhZyAxIiwiRGVjYXlzIGdlb21ldHJpY2FsbHkiLCJSZWplY3QgSDAgKHN0YXQpIiwiMCIsIjAiLCIxIl0sWyJDdXRzIG9mZiBhZnRlciBsYWcgMiIsIkRlY2F5cyBnZW9tZXRyaWNhbGx5IiwiUmVqZWN0IEgwIiwiMCIsIjAiLCIyIl0sWyJEZWNheXMgZ2VvbWV0cmljYWxseSIsIkN1dHMgb2ZmIGFmdGVyIGxhZyAxIiwiUmVqZWN0IEgwIiwiMCIsIjEiLCIwIl0sWyJEZWNheXMgZ2VvbWV0cmljYWxseSIsIkN1dHMgb2ZmIGFmdGVyIGxhZyAyIiwiUmVqZWN0IEgwIiwiMCIsIjIiLCIwIl0sWyJCb3RoIGRlY2F5IGdlb21ldHJpY2FsbHkiLCJCb3RoIGRlY2F5IGdlb21ldHJpY2FsbHkiLCJSZWplY3QgSDAiLCIwIiwiMeKAkzIiLCIx4oCTMiAodXNlIEFJQykiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiBBSUMgYW5kIEJJQyBkaXNhZ3JlZSwgcHJlZmVyIEJJQyBmb3IgZmluYWwgbW9kZWwgc2VsZWN0aW9uIGluIGxhcmdlIHNhbXBsZXMgKGl0IGlzIG1vZGVsLXNlbGVjdGlvbiBjb25zaXN0ZW50KSBhbmQgQUlDIHdoZW4gcHJlZGljdGlvbiBhY2N1cmFjeSBhdCBzaG9ydCBob3Jpem9ucyBpcyBwYXJhbW91bnQuIEFsd2F5cyByZWZpdCB0aGUgZmluYWwgbW9kZWwgb24gdGhlIGZ1bGwgc2FtcGxlIGJlZm9yZSBnZW5lcmF0aW5nIGxpdmUgZm9yZWNhc3RzIOKAlCBhdm9pZCByZWx5aW5nIG9uIG1vZGVscyBlc3RpbWF0ZWQgb25seSBvbiB0aGUgdHJhaW5pbmcgc3BsaXQuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# ARIMA — AR, I, MA Components and Box-Jenkins Methodology

ARIMA — AutoRegressive Integrated Moving Average — is the workhorse model of classical time-series forecasting. It unifies three ideas: AR terms capture dependence on past values, MA terms capture dependence on past forecast errors, and the I (integrated) component handles non-stationarity by differencing. Box and Jenkins (1970) formalised a systematic methodology for identifying, estimating, and diagnosing ARIMA models that remains standard practice fifty years later.

## AR(p) — Autoregressive Process

An AR(p) model expresses the current value as a linear combination of p past values plus white noise: yₜ = c + φ₁yₜ₋₁ + φ₂yₜ₋₂ + … + φₚyₜ₋ₚ + εₜ. Using the backshift operator B (Bʲyₜ = yₜ₋ⱼ), this is (1 − φ₁B − φ₂B² − … − φₚBᵖ)yₜ = c + εₜ. Stationarity requires all roots of the characteristic polynomial φ(z) = 1 − φ₁z − … − φₚzᵖ to lie strictly outside the unit circle in the complex plane. An AR(1) with φ₁ = 1 is the random walk (unit root, non-stationary).

## MA(q) — Moving Average Process

An MA(q) model expresses the current value as a linear combination of q past errors: yₜ = μ + εₜ + θ₁εₜ₋₁ + … + θqεₜ₋q. MA processes are always stationary regardless of the θ values because they are finite sums of white noise. Invertibility — the condition that makes the MA representable as an infinite AR — requires roots of θ(z) = 1 + θ₁z + … + θqzq to lie outside the unit circle. Non-invertible MA models are statistically indistinguishable from invertible ones by their ACF, but give different forecasts; by convention we always choose the invertible representation.

## ARIMA(p,d,q) — Integration and Differencing

ARIMA(p,d,q) applies d differences to yₜ before fitting an ARMA(p,q): let wₜ = Δᵈyₜ = (1−B)ᵈyₜ; then φ(B)wₜ = θ(B)εₜ. The d parameter is the number of unit roots in the original series. ARIMA(0,1,0) is the random walk; ARIMA(0,2,0) is the random acceleration (double-integrated random walk). Most economic and financial series require d = 1 or d = 0; over-differencing (using d = 2 when d = 1 suffices) introduces spurious MA structure.

```python
import numpy as np
from statsmodels.tsa.stattools import acf

np.random.seed(0)
n = 300
eps = np.random.randn(n + 5)

# Simulate AR(2): phi1=0.7, phi2=-0.2
y_ar2 = np.zeros(n)
for t in range(2, n):
    y_ar2[t] = 0.7*y_ar2[t-1] - 0.2*y_ar2[t-2] + eps[t]

# Simulate MA(2): theta1=0.6, theta2=0.3
y_ma2 = np.array([eps[t] + 0.6*eps[t-1] + 0.3*eps[t-2] for t in range(2, n+2)])

# Simulate ARIMA(1,1,1): difference once to get stationary
wt = np.zeros(n)
for t in range(1, n):
    wt[t] = 0.5*wt[t-1] + eps[t] + 0.4*eps[t-1]
y_arima = np.cumsum(wt)  # integrate once: d=1

print("Process statistics (all computed on stationary form):")
print(f"AR(2):  mean={y_ar2.mean():.3f}  std={y_ar2.std():.3f}")
print(f"MA(2):  mean={y_ma2.mean():.3f}  std={y_ma2.std():.3f}")
print(f"ARIMA(1,1,1) first-diff mean={np.diff(y_arima).mean():.3f}  std={np.diff(y_arima).std():.3f}")

# Verify AR(2) stationarity via characteristic roots
import numpy.polynomial.polynomial as P
roots = np.roots([1, -0.7, 0.2])  # char poly: 1 - 0.7z - (-0.2)z^2... note sign
print(f"AR(2) char roots modulus: {np.abs(roots)}  (must be > 1 for stationarity)")
```

## Box-Jenkins Methodology — Step by Step

Box-Jenkins is an iterative identification-estimation-diagnostic-forecast cycle. It requires the analyst to interact with the data at each stage: residual diagnostics feed back into model identification. Automated approaches (auto_arima) can mimic the cycle, but understanding the manual procedure is essential for diagnosing failures and handling unusual series.

1. Identification: Plot the series, test for stationarity (ADF/KPSS), determine d. Then plot ACF and PACF of the differenced series to identify candidate (p, q).
2. Estimation: Fit the ARIMA(p,d,q) by Maximum Likelihood. The likelihood is computed via the Kalman filter (or innovations algorithm) treating the model in state space form.
3. Diagnostic checking: Plot residual ACF/PACF (should be white noise), run Ljung-Box test, check normality with Q-Q plot and Jarque-Bera test.
4. Model selection: Compare candidate models by AIC = −2·log(L) + 2·k or BIC = −2·log(L) + k·log(n). AIC favours slightly more complex models; BIC is more parsimonious.
5. Forecasting: Generate h-step-ahead point forecasts and prediction intervals. Interval width grows with horizon as forecast uncertainty accumulates.

```python
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox

np.random.seed(42)
n = 200
eps = np.random.randn(n + 2)

# True process: ARIMA(1,1,1)
wt = np.zeros(n)
for t in range(1, n):
    wt[t] = 0.6*wt[t-1] + eps[t] + 0.3*eps[t-1]
y = np.cumsum(wt)

# Fit ARIMA(1,1,1)
model = ARIMA(y, order=(1, 1, 1))
fit   = model.fit()

print("ARIMA(1,1,1) fit summary:")
print(f"  AR phi  = {fit.params['ar.L1']:.4f}")
print(f"  MA theta = {fit.params['ma.L1']:.4f}")
print(f"  sigma^2  = {fit.params['sigma2']:.4f}")
print(f"  AIC      = {fit.aic:.2f}")
print(f"  BIC      = {fit.bic:.2f}")

# Residual diagnostics
resid = fit.resid
lb = acorr_ljungbox(resid[2:], lags=[10, 20], return_df=True)
print("\nLjung-Box on residuals:")
print(lb[['lb_stat', 'lb_pvalue']].to_string())
```

## Automatic Order Selection with auto_arima

Manual Box-Jenkins requires experience and can be ambiguous when ACF/PACF patterns are unclear. The auto_arima function (pmdarima) automates order selection: it searches a grid of (p, d, q) combinations, estimates each model via MLE, and returns the one with the lowest AIC or BIC. It also tests for stationarity internally (using ADF) to determine d automatically, and can handle seasonal orders. The search is made efficient by a stepwise algorithm that starts from a default model and explores neighbouring orders.

```python
import numpy as np
import pmdarima as pm
from statsmodels.tsa.arima.model import ARIMA

np.random.seed(5)
n = 300
eps = np.random.randn(n + 3)

# True ARIMA(2,1,1) process
wt = np.zeros(n)
for t in range(2, n):
    wt[t] = 0.5*wt[t-1] - 0.2*wt[t-2] + eps[t] + 0.4*eps[t-1]
y = np.cumsum(wt)

# Auto-ARIMA search
auto = pm.auto_arima(
    y,
    start_p=0, max_p=4,
    start_q=0, max_q=4,
    d=None,        # auto-determine via ADF test
    information_criterion='aic',
    stepwise=True,
    seasonal=False,
    error_action='ignore',
    suppress_warnings=True
)

print(f"Best order selected: ARIMA{auto.order}")
print(f"AIC={auto.aic():.2f}  BIC={auto.bic():.2f}")
print(auto.summary())
```

## Forecasting and Prediction Intervals

```python
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

np.random.seed(10)
n = 150
eps = np.random.randn(n + 1)

wt = np.zeros(n)
for t in range(1, n):
    wt[t] = 0.7*wt[t-1] + eps[t] + 0.2*eps[t-1]
y = np.cumsum(wt)

train, test = y[:120], y[120:]

fit = ARIMA(train, order=(1, 1, 1)).fit()

for h in [1, 5, 10, 20, 30]:
    fc = fit.get_forecast(steps=h)
    mean_fc  = fc.predicted_mean
    ci       = fc.conf_int(alpha=0.05)
    interval = ci.iloc[-1, 1] - ci.iloc[-1, 0]  # width at horizon h
    print(f"h={h:2d}: point={mean_fc.iloc[-1]:+7.3f}  95% CI width={interval:.3f}")

print("\nInterval width grows with horizon -- uncertainty accumulates over time")
print("For ARIMA(1,1,1), long-run forecast converges to a random walk pattern")
```

> **ARIMA Prediction Intervals Assume Normal Errors**: Prediction intervals for ARIMA are exact only when εₜ ~ N(0, σ²). For fat-tailed residuals (common in financial returns), the normal-based intervals under-cover at high significance levels. Check residual Q-Q plots: if tails are heavier than normal, consider bootstrapped prediction intervals or switch to a model with t-distributed innovations.

## ARIMA Order Selection Guide

| ACF Pattern | PACF Pattern | ADF Result | Suggested d | Suggested p | Suggested q |
| --- | --- | --- | --- | --- | --- |
| Decays slowly, near 1 | Near 1 at lag 1 then drops | Fail to reject (non-stat) | 1 | — | — |
| Cuts off after lag 1 | Decays geometrically | Reject H0 (stat) | 0 | 0 | 1 |
| Cuts off after lag 2 | Decays geometrically | Reject H0 | 0 | 0 | 2 |
| Decays geometrically | Cuts off after lag 1 | Reject H0 | 0 | 1 | 0 |
| Decays geometrically | Cuts off after lag 2 | Reject H0 | 0 | 2 | 0 |
| Both decay geometrically | Both decay geometrically | Reject H0 | 0 | 1–2 | 1–2 (use AIC) |

When AIC and BIC disagree, prefer BIC for final model selection in large samples (it is model-selection consistent) and AIC when prediction accuracy at short horizons is paramount. Always refit the final model on the full sample before generating live forecasts — avoid relying on models estimated only on the training split.

---

