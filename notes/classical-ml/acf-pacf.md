---
title: "ACF and PACF — Autocorrelation for Model Identification"
slug: "acf-pacf"
description: "Derive the ACF and PACF from covariance theory, interpret AR/MA/ARMA signatures in their plots, apply the Ljung-Box test for residual autocorrelation, and identify seasonal patterns in ACF for Box-Jenkins model selection."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGF1dG9jb3JyZWxhdGlvbiBmdW5jdGlvbiAoQUNGKSBhbmQgcGFydGlhbCBhdXRvY29ycmVsYXRpb24gZnVuY3Rpb24gKFBBQ0YpIGFyZSB0aGUgcHJpbWFyeSBkaWFnbm9zdGljIHRvb2xzIGZvciBpZGVudGlmeWluZyBBUklNQSBtb2RlbCBvcmRlcnMuIFRvZ2V0aGVyIHRoZXkgZm9ybSB0aGUgZmlyc3Qgc3RlcCBvZiB0aGUgQm94LUplbmtpbnMgbWV0aG9kb2xvZ3k6IHBsb3QgYm90aCBmdW5jdGlvbnMsIHJlY29nbmlzZSB0aGUgc2lnbmF0dXJlIHBhdHRlcm4sIGFuZCByZWFkIG9mZiBjYW5kaWRhdGUgdmFsdWVzIG9mIHAgYW5kIHEuIFVuZGVyc3RhbmRpbmcgdGhlaXIgbWF0aGVtYXRpY2FsIGRlZmluaXRpb25zIOKAlCBhbmQgdGhlIGRpZmZlcmVuY2UgYmV0d2VlbiBkaXJlY3QgYW5kIGluZGlyZWN0IGxhZyBkZXBlbmRlbmNlIOKAlCBpcyBlc3NlbnRpYWwgZm9yIGNvcnJlY3QgaW50ZXJwcmV0YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXV0b2NvcnJlbGF0aW9uIEZ1bmN0aW9uIChBQ0YpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQUNGIGF0IGxhZyBrIGlzIGRlZmluZWQgYXMgz4EoaykgPSDOsyhrKS/OsygwKSwgd2hlcmUgzrMoaykgPSBDb3YoeeKCnCwgeeKCnOKCi+KClikgaXMgdGhlIGF1dG9jb3ZhcmlhbmNlIGF0IGxhZyBrIGFuZCDOsygwKSA9IFZhcih54oKcKS4gVGhlIEFDRiBjYXB0dXJlcyB0aGUgdG90YWwgY29ycmVsYXRpb24gYmV0d2VlbiB54oKcIGFuZCB54oKc4oKL4oKWLCBpbmNsdWRpbmcgaW5kaXJlY3QgY29ycmVsYXRpb25zIG1lZGlhdGVkIGJ5IGludGVybWVkaWF0ZSBsYWdzLiBJZiB54oKcIGlzIGNvcnJlbGF0ZWQgd2l0aCB54oKc4oKL4oKBIGFuZCB54oKc4oKL4oKBIGlzIGNvcnJlbGF0ZWQgd2l0aCB54oKc4oKL4oKCLCB0aGUgQUNGIGF0IGxhZyAyIHdpbGwgYmUgbm9uLXplcm8gZXZlbiBpZiB0aGVyZSBpcyBubyBkaXJlY3QgcmVsYXRpb25zaGlwIGJldHdlZW4geeKCnCBhbmQgeeKCnOKCi+KCgi4gVGhlIHNhbXBsZSBBQ0YgcmVwbGFjZXMgcG9wdWxhdGlvbiBtb21lbnRzIHdpdGggc2FtcGxlIGFuYWxvZ3Vlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXJ0aWFsIEF1dG9jb3JyZWxhdGlvbiBGdW5jdGlvbiAoUEFDRikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBQQUNGIGF0IGxhZyBrIGlzIHRoZSBwYXJ0aWFsIGNvcnJlbGF0aW9uIGJldHdlZW4geeKCnCBhbmQgeeKCnOKCi+KCliBhZnRlciByZW1vdmluZyB0aGUgbGluZWFyIGVmZmVjdHMgb2YgeeKCnOKCi+KCgSwgeeKCnOKCi+KCgiwg4oCmLCB54oKc4oKLKOKCluKCi+KCgSkuIEl0IGlzIGNvbXB1dGVkIHZpYSB0aGUgWXVsZS1XYWxrZXIgZXF1YXRpb25zIG9yIHRoZSBEdXJiaW4tTGV2aW5zb24gcmVjdXJzaW9uLiBUaGUgUEFDRiBpcyB0aGUgbGFzdCBjb2VmZmljaWVudCBpbiB0aGUgQVIoaykgcmVncmVzc2lvbiBvZiB54oKcIG9uIGFsbCBsYWdzIHVwIHRvIGsuIEZvciBhIHRydWUgQVIocCkgcHJvY2VzcywgdGhlIFBBQ0YgaXMgZXhhY3RseSB6ZXJvIGZvciBsYWdzIGJleW9uZCBwIGJlY2F1c2UgdGhlIHByb2Nlc3MgaGFzIG5vIGRpcmVjdCBpbmZsdWVuY2UgYmV5b25kIGl0cyBvcmRlciDigJQgb25seSB0aGUgQUNGIGRlY2F5cyBnZW9tZXRyaWNhbGx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc3RhdHNtb2RlbHMudHNhLnN0YXR0b29scyBpbXBvcnQgYWNmLCBwYWNmXG5cbm5wLnJhbmRvbS5zZWVkKDApXG5uID0gNTAwXG5cbiMgQVIoMik6IHBoaTE9MC42LCBwaGkyPS0wLjNcbnlfYXIyID0gbnAuemVyb3MobilcbmZvciB0IGluIHJhbmdlKDIsIG4pOlxuICAgIHlfYXIyW3RdID0gMC42KnlfYXIyW3QtMV0gLSAwLjMqeV9hcjJbdC0yXSArIG5wLnJhbmRvbS5yYW5kbigpXG5cbmFjZl9hcjIgID0gYWNmKHlfYXIyLCAgbmxhZ3M9MTUpXG5wYWNmX2FyMiA9IHBhY2YoeV9hcjIsIG5sYWdzPTE1LCBtZXRob2Q9XHUwMDI3eXdtXHUwMDI3KVxuXG5wcmludChcIkFSKDIpIHBoaTE9MC42LCBwaGkyPS0wLjNcIilcbnByaW50KGZcIntcdTAwMjdMYWdcdTAwMjc6XHUwMDNlNXN9IHtcdTAwMjdBQ0ZcdTAwMjc6XHUwMDNlOHN9IHtcdTAwMjdQQUNGXHUwMDI3Olx1MDAzZThzfSB7XHUwMDI3UEFDRiBzaWc/XHUwMDI3Olx1MDAzZTEyc31cIilcbnByaW50KFwiLVwiICogMzgpXG5jaSA9IDEuOTYgLyBucC5zcXJ0KG4pXG5mb3IgayBpbiByYW5nZSgxLCAxMCk6XG4gICAgc2lnID0gXCJZRVNcIiBpZiBhYnMocGFjZl9hcjJba10pIFx1MDAzZSBjaSBlbHNlIFwiLS0tXCJcbiAgICBwcmludChmXCJ7azo1ZH0ge2FjZl9hcjJba106OC40Zn0ge3BhY2ZfYXIyW2tdOjguNGZ9IHtzaWc6XHUwMDNlMTJzfVwiKVxucHJpbnQoZlwiXFxuOTUlIENJIHRocmVzaG9sZDogKy8te2NpOi40Zn1cIilcbnByaW50KFwiUEFDRiBzaG91bGQgY3V0IG9mZiBhZnRlciBsYWcgMjsgQUNGIHNob3VsZCBkZWNheSBnZW9tZXRyaWNhbGx5XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQVIsIE1BLCBhbmQgQVJNQSBTaWduYXR1cmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQUNGIGFuZCBQQUNGIGhhdmUgY2hhcmFjdGVyaXN0aWMgc2lnbmF0dXJlcyBmb3IgcHVyZSBBUiBhbmQgTUEgcHJvY2Vzc2VzIHRoYXQgZ3VpZGUgbW9kZWwgaWRlbnRpZmljYXRpb24uIEFuIEFSKHApIHByb2Nlc3MgaGFzIGFuIEFDRiB0aGF0IGRlY2F5cyBnZW9tZXRyaWNhbGx5IChvciBzaW51c29pZGFsbHkgZm9yIGNvbXBsZXggcm9vdHMpIGFuZCBhIFBBQ0YgdGhhdCBjdXRzIG9mZiBzaGFycGx5IHRvIHplcm8gYWZ0ZXIgbGFnIHAuIEFuIE1BKHEpIHByb2Nlc3MgaXMgdGhlIG1pcnJvciBpbWFnZTogdGhlIEFDRiBjdXRzIG9mZiBhZnRlciBsYWcgcSBhbmQgdGhlIFBBQ0YgZGVjYXlzIGdlb21ldHJpY2FsbHkuIEZvciBBUk1BKHAscSksIGJvdGggQUNGIGFuZCBQQUNGIGRlY2F5IGdlb21ldHJpY2FsbHksIG1ha2luZyBvcmRlciBpZGVudGlmaWNhdGlvbiBoYXJkZXIg4oCUIGluZm9ybWF0aW9uIGNyaXRlcmlhIChBSUMsIEJJQykgYXJlIHRoZW4gbW9yZSByZWxpYWJsZSB0aGFuIHZpc3VhbCBpbnNwZWN0aW9uLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9jZXNzIiwiQUNGIFNoYXBlIiwiUEFDRiBTaGFwZSIsIklkZW50aWZpY2F0aW9uIl0sInJvd3MiOltbIkFSKHApIiwiRGVjYXlzIGdlb21ldHJpY2FsbHkgKG9yIG9zY2lsbGF0ZXMgaWYgY29tcGxleCByb290cykiLCJDdXRzIG9mZiBhZnRlciBsYWcgcCIsIlJlYWQgcCBmcm9tIFBBQ0Y6IGxhc3Qgc2lnbmlmaWNhbnQgbGFnIl0sWyJNQShxKSIsIkN1dHMgb2ZmIGFmdGVyIGxhZyBxIiwiRGVjYXlzIGdlb21ldHJpY2FsbHkiLCJSZWFkIHEgZnJvbSBBQ0Y6IGxhc3Qgc2lnbmlmaWNhbnQgbGFnIl0sWyJBUk1BKHAscSkiLCJEZWNheXMgZ2VvbWV0cmljYWxseSBhZnRlciBsYWcgcSIsIkRlY2F5cyBnZW9tZXRyaWNhbGx5IGFmdGVyIGxhZyBwIiwiQm90aCBkZWNheSDigJQgdXNlIEFJQy9CSUMgZ3JpZCBzZWFyY2giXSxbIldoaXRlIG5vaXNlIiwiQWxsIGxhZ3MgbmVhciB6ZXJvIiwiQWxsIGxhZ3MgbmVhciB6ZXJvIiwiTm8gc3RydWN0dXJlIOKAlCByZXNpZHVhbHMgc2hvdWxkIGxvb2sgbGlrZSB0aGlzIl0sWyJSYW5kb20gd2FsayBJKDEpIiwiRGVjYXlzIHZlcnkgc2xvd2x5IChuZWFyIDEgZm9yIG1hbnkgbGFncykiLCJOZWFyIDEgYXQgbGFnIDEsIHRoZW4gZHJvcHMiLCJEaWZmZXJlbmNlIHRoZSBzZXJpZXMgYmVmb3JlIGZpdHRpbmciXSxbIlNlYXNvbmFsIEFSKDEpX3MiLCJTcGlrZXMgYXQgbGFncyBzLCAycywgM3PigKYgZGVjYXkgZ2VvbWV0cmljYWxseSIsIlNwaWtlIGF0IGxhZyBzLCBjdXRzIG9mZiIsIlNlYXNvbmFsIEFSIOKAlCBhZGQgc2Vhc29uYWwgQVJJTUEgY29tcG9uZW50Il1dfSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0dG9vbHMgaW1wb3J0IGFjZiwgcGFjZlxuXG5ucC5yYW5kb20uc2VlZCgxKVxubiA9IDYwMFxuZXBzID0gbnAucmFuZG9tLnJhbmRuKG4gKyAxMClcblxuIyBNQSgxKTogdGhldGEgPSAwLjdcbnlfbWExID0gbnAuYXJyYXkoW2Vwc1t0XSArIDAuNyplcHNbdC0xXSBmb3IgdCBpbiByYW5nZSgxLCBuKzEpXSlcblxuIyBBUk1BKDEsMSk6IHBoaT0wLjUsIHRoZXRhPTAuNFxueV9hcm1hID0gbnAuemVyb3MobilcbmZvciB0IGluIHJhbmdlKDEsIG4pOlxuICAgIHlfYXJtYVt0XSA9IDAuNSp5X2FybWFbdC0xXSArIGVwc1t0XSArIDAuNCplcHNbdC0xXVxuXG5jaSA9IDEuOTYgLyBucC5zcXJ0KG4pXG5mb3IgbGFiZWwsIHkgaW4gWyhcIk1BKDEpIHRoZXRhPTAuN1wiLCB5X21hMSksIChcIkFSTUEoMSwxKSBwaGk9MC41LHRoZXRhPTAuNFwiLCB5X2FybWEpXTpcbiAgICBhICA9IGFjZih5LCAgbmxhZ3M9NilcbiAgICBwYSA9IHBhY2YoeSwgbmxhZ3M9NiwgbWV0aG9kPVx1MDAyN3l3bVx1MDAyNylcbiAgICBwcmludChmXCJcXG57bGFiZWx9XCIpXG4gICAgcHJpbnQoZlwiICB7XHUwMDI3TGFnXHUwMDI3Olx1MDAzZTRzfSAge1x1MDAyN0FDRlx1MDAyNzpcdTAwM2U3c30gIHtcdTAwMjdBQ0Ygc2lnXHUwMDI3Olx1MDAzZThzfSAge1x1MDAyN1BBQ0ZcdTAwMjc6XHUwMDNlN3N9ICB7XHUwMDI3UEFDRiBzaWdcdTAwMjc6XHUwMDNlOXN9XCIpXG4gICAgZm9yIGsgaW4gcmFuZ2UoMSwgNyk6XG4gICAgICAgIHByaW50KGZcIiAge2s6NGR9ICB7YVtrXTo3LjRmfSAge1x1MDAyN1lFU1x1MDAyNyBpZiBhYnMoYVtrXSlcdTAwM2VjaSBlbHNlIFx1MDAyNy0tLVx1MDAyNzpcdTAwM2U4c30gIHtwYVtrXTo3LjRmfSAge1x1MDAyN1lFU1x1MDAyNyBpZiBhYnMocGFba10pXHUwMDNlY2kgZWxzZSBcdTAwMjctLS1cdTAwMjc6XHUwMDNlOXN9XCIpXG5wcmludChmXCJcXG45NSUgQ0k6ICsvLXtjaTouNGZ9ICAobj17bn0pXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29uZmlkZW5jZSBCYW5kcyBhbmQgdGhlIExqdW5nLUJveCBUZXN0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgOTUlIGNvbmZpZGVuY2UgYmFuZCBmb3IgdGhlIHNhbXBsZSBBQ0YgdW5kZXIgdGhlIHdoaXRlLW5vaXNlIG51bGwgaHlwb3RoZXNpcyBpcyDCsTEuOTYv4oiabiwgd2hlcmUgbiBpcyB0aGUgc2VyaWVzIGxlbmd0aC4gU3Bpa2VzIG91dHNpZGUgdGhpcyBiYW5kIGFyZSBzaWduaWZpY2FudCBhdCB0aGUgNSUgbGV2ZWwuIFRoZSBManVuZy1Cb3ggUS1zdGF0aXN0aWMgdGVzdHMgSOKCgDogz4EoMSkgPSDPgSgyKSA9IOKApiA9IM+BKGgpID0gMCAobm8gYXV0b2NvcnJlbGF0aW9uIHVwIHRvIGxhZyBoKS4gSXQgYWdncmVnYXRlcyBhdXRvY29ycmVsYXRpb25zIFEgPSBuKG4rMinOo1vPgcyCKGspwrIvKG7iiJJrKV0gYW5kIGZvbGxvd3MgYSDPh8KyKGgpIGRpc3RyaWJ1dGlvbi4gUmVqZWN0aW5nIEjigoAgbWVhbnMgdGhlcmUgaXMgc2lnbmlmaWNhbnQgYXV0b2NvcnJlbGF0aW9uIGluIHRoZSByZXNpZHVhbHMg4oCUIHRoZSBtb2RlbCBoYXMgbm90IGNhcHR1cmVkIGFsbCBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2Euc3RhdHRvb2xzIGltcG9ydCBhY2ZcbmZyb20gc3RhdHNtb2RlbHMuc3RhdHMuZGlhZ25vc3RpYyBpbXBvcnQgYWNvcnJfbGp1bmdib3hcblxubnAucmFuZG9tLnNlZWQoMylcbm4gPSAyMDBcblxuIyBXaGl0ZSBub2lzZSDigJQgc2hvdWxkIE5PVCByZWplY3QgSDBcbndoaXRlX25vaXNlID0gbnAucmFuZG9tLnJhbmRuKG4pXG5cbiMgQVIoMSkgcmVzaWR1YWxzIOKAlCBsZWZ0b3ZlciBzdHJ1Y3R1cmUgKG1vZGVsIHVuZGVyLWZpdClcbmFyMV9yYXcgPSBucC56ZXJvcyhuKVxuZm9yIHQgaW4gcmFuZ2UoMSwgbik6XG4gICAgYXIxX3Jhd1t0XSA9IDAuNTUgKiBhcjFfcmF3W3QtMV0gKyBucC5yYW5kb20ucmFuZG4oKVxuIyBQcmV0ZW5kIHdlIG9ubHkgcmVtb3ZlZCB0aGUgbWVhbiAoYmFkIHJlc2lkdWFscylcbmJhZF9yZXNpZCA9IGFyMV9yYXcgLSBhcjFfcmF3Lm1lYW4oKVxuXG5mb3IgbGFiZWwsIHJlc2lkIGluIFsoXCJXaGl0ZSBub2lzZVwiLCB3aGl0ZV9ub2lzZSksIChcIkFSKDEpIHBzZXVkby1yZXNpZHVhbHNcIiwgYmFkX3Jlc2lkKV06XG4gICAgbGIgPSBhY29ycl9sanVuZ2JveChyZXNpZCwgbGFncz1bNSwgMTAsIDIwXSwgcmV0dXJuX2RmPVRydWUpXG4gICAgcHJpbnQoZlwiXFxue2xhYmVsfVwiKVxuICAgIHByaW50KGxiW1tcdTAwMjdsYl9zdGF0XHUwMDI3LCBcdTAwMjdsYl9wdmFsdWVcdTAwMjddXS5yZW5hbWUoY29sdW1ucz17XHUwMDI3bGJfc3RhdFx1MDAyNzogXHUwMDI3UVx1MDAyNywgXHUwMDI3bGJfcHZhbHVlXHUwMDI3OiBcdTAwMjdwLXZhbHVlXHUwMDI3fSkudG9fc3RyaW5nKCkpXG4gICAgcHJpbnQoXCIgIEludGVycHJldGF0aW9uOlwiLCBcIk9LXCIgaWYgYWxsKGxiW1x1MDAyN2xiX3B2YWx1ZVx1MDAyN10gXHUwMDNlIDAuMDUpIGVsc2UgXCJGQUlMIOKAlCBhdXRvY29ycmVsYXRpb24gcmVtYWluc1wiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlYXNvbmFsIFBhdHRlcm5zIGluIEFDRiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiBhIHRpbWUgc2VyaWVzIGhhcyBzZWFzb25hbCBzdHJ1Y3R1cmUsIHRoZSBBQ0YgZXhoaWJpdHMgc3Bpa2VzIGF0IG11bHRpcGxlcyBvZiB0aGUgc2Vhc29uYWwgcGVyaW9kIFAg4oCUIGF0IGxhZ3MgUCwgMlAsIDNQLCBhbmQgc28gb24uIEZvciBkYWlseSBkYXRhIHdpdGggd2Vla2x5IHNlYXNvbmFsaXR5IChQID0gNyksIGxhcmdlIEFDRiBzcGlrZXMgYXBwZWFyIGF0IGxhZ3MgNywgMTQsIDIxLiBUaGUgYW1wbGl0dWRlIG9mIHRoZXNlIHNwaWtlcyBkZWNheXMgd2l0aCBsYWcgaWYgdGhlIHNlYXNvbmFsIGRlcGVuZGVuY2UgaXMgbm90IGEgdW5pdCByb290LiBJZiB0aGUgc2Vhc29uYWwgQUNGIHNwaWtlcyBkbyBub3QgZGVjYXksIHNlYXNvbmFsIGRpZmZlcmVuY2luZyBpcyByZXF1aXJlZC4gVGhlIFBBQ0YgbWlycm9ycyB0aGUgc2FtZSBwYXR0ZXJuLCBjdXR0aW5nIG9mZiBhZnRlciB0aGUgc2Vhc29uYWwgbGFnIGZvciBhIHNlYXNvbmFsIEFSKDEpIHN0cnVjdHVyZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0dG9vbHMgaW1wb3J0IGFjZlxuXG5ucC5yYW5kb20uc2VlZCg3KVxubiA9IDM2NSAqIDIgICMgdHdvIHllYXJzIG9mIGRhaWx5IGRhdGFcbnQgPSBucC5hcmFuZ2UobilcblxuIyBXZWVrbHkgc2Vhc29uYWxpdHkgKyB0cmVuZCArIG5vaXNlXG55ID0gNTAgKyAwLjA1KnQgKyA4Km5wLnNpbigyKm5wLnBpKnQvNykgKyAzKm5wLnJhbmRvbS5yYW5kbihuKVxuXG5hY2ZfdmFscyA9IGFjZih5LCBubGFncz0yOClcbmNpID0gMS45NiAvIG5wLnNxcnQobilcblxucHJpbnQoZlwiRGFpbHkgc2VyaWVzIHdpdGggd2Vla2x5IHNlYXNvbmFsaXR5IChQPTcpLCBuPXtufVwiKVxucHJpbnQoZlwiOTUlIENJIGJhbmQ6ICsvLXtjaTouNGZ9XCIpXG5wcmludCgpXG5wcmludChmXCJ7XHUwMDI3TGFnXHUwMDI3Olx1MDAzZTRzfSAge1x1MDAyN0FDRlx1MDAyNzpcdTAwM2U3c30gIHtcdTAwMjdTaWduaWZpY2FudFx1MDAyNzpcdTAwM2UxMnN9ICB7XHUwMDI3Tm90ZVx1MDAyN31cIilcbnByaW50KFwiLVwiICogNTApXG5mb3IgayBpbiBbMSwgMiwgMywgNywgMTQsIDIxLCAyOF06XG4gICAgbm90ZSA9IFwiXHUwMDNjLS0gc2Vhc29uYWwgc3Bpa2VcIiBpZiBrICUgNyA9PSAwIGVsc2UgXCJcIlxuICAgIHNpZyA9IFwiWUVTXCIgaWYgYWJzKGFjZl92YWxzW2tdKSBcdTAwM2UgY2kgZWxzZSBcIm5vXCJcbiAgICBwcmludChmXCJ7azo0ZH0gIHthY2ZfdmFsc1trXTo3LjRmfSAge3NpZzpcdTAwM2UxMnN9ICB7bm90ZX1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCb3gtSmVua2lucyBJZGVudGlmaWNhdGlvbiBTdHJhdGVneSJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjp0cnVlLCJpdGVtcyI6WyJQbG90IHRoZSBzZXJpZXM6IGlkZW50aWZ5IG9idmlvdXMgdHJlbmRzLCBzZWFzb25hbGl0eSwgb3IgY2hhbmdpbmcgdmFyaWFuY2UuIiwiVGVzdCBmb3Igc3RhdGlvbmFyaXR5IChBREYgKyBLUFNTKS4gQXBwbHkgZCBkaWZmZXJlbmNlcyAoYW5kL29yIHNlYXNvbmFsIGRpZmZlcmVuY2luZykgdW50aWwgc3RhdGlvbmFyeS4iLCJQbG90IEFDRiBhbmQgUEFDRiBvZiB0aGUgc3RhdGlvbmFyeSBzZXJpZXMuIENoZWNrIGZvciBzZWFzb25hbCBzcGlrZXMgYXQgbXVsdGlwbGVzIG9mIFAuIiwiSWRlbnRpZnkgcCBmcm9tIFBBQ0YgKGN1dC1vZmYgbGFnKSBhbmQgcSBmcm9tIEFDRiAoY3V0LW9mZiBsYWcpLiBCb3RoIGRlY2F5aW5nIHN1Z2dlc3RzIEFSTUEuIiwiRml0IGNhbmRpZGF0ZSBtb2RlbHMgKHNldmVyYWwgbmVhcmJ5IChwLHEpIGNvbWJpbmF0aW9ucykgYW5kIGNvbXBhcmUgQUlDL0JJQy4iLCJSdW4gZGlhZ25vc3RpYyBjaGVja3M6IExqdW5nLUJveCBvbiByZXNpZHVhbHMsIG5vcm1hbCBRLVEgcGxvdCwgcmVzaWR1YWwgQUNGL1BBQ0YuIiwiU2VsZWN0IHRoZSBtb2RlbCB3aXRoIGxvd2VzdCBBSUMgKG9yIEJJQyBmb3IgcGFyc2ltb255KSB0aGF0IHBhc3NlcyBhbGwgZGlhZ25vc3RpYyBjaGVja3MuIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiOTUlIEJhbmRzIEFyZSBBcHByb3hpbWF0ZSIsImNvbnRlbnQiOiJUaGUgwrExLjk2L+KImm4gY29uZmlkZW5jZSBiYW5kcyBhc3N1bWUgYWxsIGF1dG9jb3JyZWxhdGlvbnMgYXQgb3RoZXIgbGFncyBhcmUgemVybywgd2hpY2ggaXMgb25seSBleGFjdGx5IGNvcnJlY3QgZm9yIHdoaXRlIG5vaXNlLiBGb3IgTUEocSkgbW9kZWxzLCB0aGUgYmFuZHMgc2hvdWxkIHdpZGVuIGZvciBsYWdzIGJleW9uZCBxIHVzaW5nIHRoZSBCYXJ0bGV0dCBmb3JtdWxhLiBJbiBwcmFjdGljZSwgaWYgb25lIG9yIHR3byBsYWdzIG1hcmdpbmFsbHkgZXhjZWVkIHRoZSBiYW5kIHdoaWxlIGFsbCBvdGhlcnMgYXJlIGNsZWFybHkgaW5zaWRlIGl0LCB0cmVhdCB0aG9zZSBhcyBpbnNpZ25pZmljYW50IOKAlCB0aGUgcGF0dGVybiBtYXR0ZXJzIG1vcmUgdGhhbiBpbmRpdmlkdWFsIHNwaWtlIHNpemVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbW1vbiBQaXRmYWxscyBpbiBBQ0YgYW5kIFBBQ0YgSW50ZXJwcmV0YXRpb24ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkludGVycHJldGluZyBBQ0YgYmVmb3JlIGRpZmZlcmVuY2luZzogbm9uLXN0YXRpb25hcnkgc2VyaWVzIHByb2R1Y2UgdmVyeSBzbG93bHkgZGVjYXlpbmcgQUNGIHRoYXQgbG9va3MgbGlrZSBzdHJvbmcgQVIg4oCUIGFsd2F5cyBzdGF0aW9uYXJpc2UgZmlyc3QuIiwiTXVsdGlwbGUgdGVzdGluZzogd2l0aCAyMCBsYWdzIHNob3duLCBleHBlY3Qgcm91Z2hseSAxIGZhbHNlLXBvc2l0aXZlIHNwaWtlIGF0IHRoZSA1JSBsZXZlbCBieSBjaGFuY2UgYWxvbmUuIiwiQ29uZmxhdGluZyBBQ0YgYW5kIFBBQ0Ygcm9sZXM6IEFSIG9yZGVyIGlzIHJlYWQgZnJvbSBQQUNGIGN1dC1vZmY7IE1BIG9yZGVyIGZyb20gQUNGIGN1dC1vZmYg4oCUIG5vdCB0aGUgb3RoZXIgd2F5IHJvdW5kLiIsIklnbm9yaW5nIHNlYXNvbmFsIHNwaWtlczogcmVndWxhciBzcGlrZXMgYXQgbXVsdGlwbGVzIG9mIFAgaW5kaWNhdGUgc2Vhc29uYWwgQVIvTUEgc3RydWN0dXJlLCBub3QgcmFuZG9tIG5vaXNlLiIsIlNtYWxsIHNhbXBsZSBiaWFzOiBzYW1wbGUgQUNGIGlzIGJpYXNlZCB0b3dhcmQgemVybyBmb3Igc2hvcnQgc2VyaWVzIOKAlCB3aXRoIG4gXHUwMDNjIDUwLCBpbnRlcnByZXQgd2l0aCBjYXV0aW9uIGFuZCB1c2UgQUlDL0JJQyBmb3IgbW9kZWwgc2VsZWN0aW9uLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# ACF and PACF — Autocorrelation for Model Identification

The autocorrelation function (ACF) and partial autocorrelation function (PACF) are the primary diagnostic tools for identifying ARIMA model orders. Together they form the first step of the Box-Jenkins methodology: plot both functions, recognise the signature pattern, and read off candidate values of p and q. Understanding their mathematical definitions — and the difference between direct and indirect lag dependence — is essential for correct interpretation.

## Autocorrelation Function (ACF)

The ACF at lag k is defined as ρ(k) = γ(k)/γ(0), where γ(k) = Cov(yₜ, yₜ₋ₖ) is the autocovariance at lag k and γ(0) = Var(yₜ). The ACF captures the total correlation between yₜ and yₜ₋ₖ, including indirect correlations mediated by intermediate lags. If yₜ is correlated with yₜ₋₁ and yₜ₋₁ is correlated with yₜ₋₂, the ACF at lag 2 will be non-zero even if there is no direct relationship between yₜ and yₜ₋₂. The sample ACF replaces population moments with sample analogues.

## Partial Autocorrelation Function (PACF)

The PACF at lag k is the partial correlation between yₜ and yₜ₋ₖ after removing the linear effects of yₜ₋₁, yₜ₋₂, …, yₜ₋(ₖ₋₁). It is computed via the Yule-Walker equations or the Durbin-Levinson recursion. The PACF is the last coefficient in the AR(k) regression of yₜ on all lags up to k. For a true AR(p) process, the PACF is exactly zero for lags beyond p because the process has no direct influence beyond its order — only the ACF decays geometrically.

```python
import numpy as np
from statsmodels.tsa.stattools import acf, pacf

np.random.seed(0)
n = 500

# AR(2): phi1=0.6, phi2=-0.3
y_ar2 = np.zeros(n)
for t in range(2, n):
    y_ar2[t] = 0.6*y_ar2[t-1] - 0.3*y_ar2[t-2] + np.random.randn()

acf_ar2  = acf(y_ar2,  nlags=15)
pacf_ar2 = pacf(y_ar2, nlags=15, method='ywm')

print("AR(2) phi1=0.6, phi2=-0.3")
print(f"{'Lag':>5s} {'ACF':>8s} {'PACF':>8s} {'PACF sig?':>12s}")
print("-" * 38)
ci = 1.96 / np.sqrt(n)
for k in range(1, 10):
    sig = "YES" if abs(pacf_ar2[k]) > ci else "---"
    print(f"{k:5d} {acf_ar2[k]:8.4f} {pacf_ar2[k]:8.4f} {sig:>12s}")
print(f"\n95% CI threshold: +/-{ci:.4f}")
print("PACF should cut off after lag 2; ACF should decay geometrically")
```

## AR, MA, and ARMA Signatures

The ACF and PACF have characteristic signatures for pure AR and MA processes that guide model identification. An AR(p) process has an ACF that decays geometrically (or sinusoidally for complex roots) and a PACF that cuts off sharply to zero after lag p. An MA(q) process is the mirror image: the ACF cuts off after lag q and the PACF decays geometrically. For ARMA(p,q), both ACF and PACF decay geometrically, making order identification harder — information criteria (AIC, BIC) are then more reliable than visual inspection.

| Process | ACF Shape | PACF Shape | Identification |
| --- | --- | --- | --- |
| AR(p) | Decays geometrically (or oscillates if complex roots) | Cuts off after lag p | Read p from PACF: last significant lag |
| MA(q) | Cuts off after lag q | Decays geometrically | Read q from ACF: last significant lag |
| ARMA(p,q) | Decays geometrically after lag q | Decays geometrically after lag p | Both decay — use AIC/BIC grid search |
| White noise | All lags near zero | All lags near zero | No structure — residuals should look like this |
| Random walk I(1) | Decays very slowly (near 1 for many lags) | Near 1 at lag 1, then drops | Difference the series before fitting |
| Seasonal AR(1)_s | Spikes at lags s, 2s, 3s… decay geometrically | Spike at lag s, cuts off | Seasonal AR — add seasonal ARIMA component |

```python
import numpy as np
from statsmodels.tsa.stattools import acf, pacf

np.random.seed(1)
n = 600
eps = np.random.randn(n + 10)

# MA(1): theta = 0.7
y_ma1 = np.array([eps[t] + 0.7*eps[t-1] for t in range(1, n+1)])

# ARMA(1,1): phi=0.5, theta=0.4
y_arma = np.zeros(n)
for t in range(1, n):
    y_arma[t] = 0.5*y_arma[t-1] + eps[t] + 0.4*eps[t-1]

ci = 1.96 / np.sqrt(n)
for label, y in [("MA(1) theta=0.7", y_ma1), ("ARMA(1,1) phi=0.5,theta=0.4", y_arma)]:
    a  = acf(y,  nlags=6)
    pa = pacf(y, nlags=6, method='ywm')
    print(f"\n{label}")
    print(f"  {'Lag':>4s}  {'ACF':>7s}  {'ACF sig':>8s}  {'PACF':>7s}  {'PACF sig':>9s}")
    for k in range(1, 7):
        print(f"  {k:4d}  {a[k]:7.4f}  {'YES' if abs(a[k])>ci else '---':>8s}  {pa[k]:7.4f}  {'YES' if abs(pa[k])>ci else '---':>9s}")
print(f"\n95% CI: +/-{ci:.4f}  (n={n})")
```

## Confidence Bands and the Ljung-Box Test

The 95% confidence band for the sample ACF under the white-noise null hypothesis is ±1.96/√n, where n is the series length. Spikes outside this band are significant at the 5% level. The Ljung-Box Q-statistic tests H₀: ρ(1) = ρ(2) = … = ρ(h) = 0 (no autocorrelation up to lag h). It aggregates autocorrelations Q = n(n+2)Σ[ρ̂(k)²/(n−k)] and follows a χ²(h) distribution. Rejecting H₀ means there is significant autocorrelation in the residuals — the model has not captured all structure.

```python
import numpy as np
from statsmodels.tsa.stattools import acf
from statsmodels.stats.diagnostic import acorr_ljungbox

np.random.seed(3)
n = 200

# White noise — should NOT reject H0
white_noise = np.random.randn(n)

# AR(1) residuals — leftover structure (model under-fit)
ar1_raw = np.zeros(n)
for t in range(1, n):
    ar1_raw[t] = 0.55 * ar1_raw[t-1] + np.random.randn()
# Pretend we only removed the mean (bad residuals)
bad_resid = ar1_raw - ar1_raw.mean()

for label, resid in [("White noise", white_noise), ("AR(1) pseudo-residuals", bad_resid)]:
    lb = acorr_ljungbox(resid, lags=[5, 10, 20], return_df=True)
    print(f"\n{label}")
    print(lb[['lb_stat', 'lb_pvalue']].rename(columns={'lb_stat': 'Q', 'lb_pvalue': 'p-value'}).to_string())
    print("  Interpretation:", "OK" if all(lb['lb_pvalue'] > 0.05) else "FAIL — autocorrelation remains")
```

## Seasonal Patterns in ACF

When a time series has seasonal structure, the ACF exhibits spikes at multiples of the seasonal period P — at lags P, 2P, 3P, and so on. For daily data with weekly seasonality (P = 7), large ACF spikes appear at lags 7, 14, 21. The amplitude of these spikes decays with lag if the seasonal dependence is not a unit root. If the seasonal ACF spikes do not decay, seasonal differencing is required. The PACF mirrors the same pattern, cutting off after the seasonal lag for a seasonal AR(1) structure.

```python
import numpy as np
from statsmodels.tsa.stattools import acf

np.random.seed(7)
n = 365 * 2  # two years of daily data
t = np.arange(n)

# Weekly seasonality + trend + noise
y = 50 + 0.05*t + 8*np.sin(2*np.pi*t/7) + 3*np.random.randn(n)

acf_vals = acf(y, nlags=28)
ci = 1.96 / np.sqrt(n)

print(f"Daily series with weekly seasonality (P=7), n={n}")
print(f"95% CI band: +/-{ci:.4f}")
print()
print(f"{'Lag':>4s}  {'ACF':>7s}  {'Significant':>12s}  {'Note'}")
print("-" * 50)
for k in [1, 2, 3, 7, 14, 21, 28]:
    note = "<-- seasonal spike" if k % 7 == 0 else ""
    sig = "YES" if abs(acf_vals[k]) > ci else "no"
    print(f"{k:4d}  {acf_vals[k]:7.4f}  {sig:>12s}  {note}")
```

## Box-Jenkins Identification Strategy

1. Plot the series: identify obvious trends, seasonality, or changing variance.
2. Test for stationarity (ADF + KPSS). Apply d differences (and/or seasonal differencing) until stationary.
3. Plot ACF and PACF of the stationary series. Check for seasonal spikes at multiples of P.
4. Identify p from PACF (cut-off lag) and q from ACF (cut-off lag). Both decaying suggests ARMA.
5. Fit candidate models (several nearby (p,q) combinations) and compare AIC/BIC.
6. Run diagnostic checks: Ljung-Box on residuals, normal Q-Q plot, residual ACF/PACF.
7. Select the model with lowest AIC (or BIC for parsimony) that passes all diagnostic checks.

> **95% Bands Are Approximate**: The ±1.96/√n confidence bands assume all autocorrelations at other lags are zero, which is only exactly correct for white noise. For MA(q) models, the bands should widen for lags beyond q using the Bartlett formula. In practice, if one or two lags marginally exceed the band while all others are clearly inside it, treat those as insignificant — the pattern matters more than individual spike sizes.

## Common Pitfalls in ACF and PACF Interpretation

- Interpreting ACF before differencing: non-stationary series produce very slowly decaying ACF that looks like strong AR — always stationarise first.
- Multiple testing: with 20 lags shown, expect roughly 1 false-positive spike at the 5% level by chance alone.
- Conflating ACF and PACF roles: AR order is read from PACF cut-off; MA order from ACF cut-off — not the other way round.
- Ignoring seasonal spikes: regular spikes at multiples of P indicate seasonal AR/MA structure, not random noise.
- Small sample bias: sample ACF is biased toward zero for short series — with n < 50, interpret with caution and use AIC/BIC for model selection.

---

