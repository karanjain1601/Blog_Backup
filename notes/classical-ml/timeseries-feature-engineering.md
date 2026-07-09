---
title: "Time-Series Feature Engineering — Lag, Rolling, and Fourier Features"
slug: "timeseries-feature-engineering"
description: "Build lag features, rolling statistics, Fourier seasonal encodings, and cyclical calendar features that convert raw time-series observations into tabular inputs for gradient-boosted trees and other ML models."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2xhc3NpY2FsIE1MIG1vZGVscyAoUmFuZG9tIEZvcmVzdCwgTGlnaHRHQk0sIFhHQm9vc3QpIGNhbm5vdCBwcm9jZXNzIHJhdyB0aW1lLXNlcmllcyBzZXF1ZW5jZXMg4oCUIHRoZXkgbmVlZCBhIGZpeGVkLXdpZHRoIGZlYXR1cmUgdmVjdG9yIHBlciBwcmVkaWN0aW9uIHBvaW50LiBGZWF0dXJlIGVuZ2luZWVyaW5nIGNvbnZlcnRzIHNlcXVlbnRpYWwgb2JzZXJ2YXRpb25zIGludG8gdGFidWxhciBpbnB1dHM6IGxhZyBmZWF0dXJlcyBjYXB0dXJlIGF1dG9jb3JyZWxhdGlvbiwgcm9sbGluZyBzdGF0aXN0aWNzIHN1bW1hcmlzZSBsb2NhbCB0cmVuZHMgYW5kIHZvbGF0aWxpdHksIEZvdXJpZXIgdGVybXMgZW5jb2RlIHNlYXNvbmFsaXR5IGNvbXBhY3RseSwgYW5kIGN5Y2xpY2FsIGNhbGVuZGFyIGVuY29kaW5ncyBwcmVzZXJ2ZSB0aGUgY2lyY3VsYXIgc3RydWN0dXJlIG9mIGhvdXJzLCBkYXlzLCBhbmQgbW9udGhzLiBUaG91Z2h0ZnVsIGZlYXR1cmUgY29uc3RydWN0aW9uIG9mdGVuIG91dHBlcmZvcm1zIGRlZXAgc2VxdWVuY2UgbW9kZWxzIGZvciBzaG9ydC10by1tZWRpdW0gaG9yaXpvbiBmb3JlY2FzdGluZyBvbiBzdHJ1Y3R1cmVkIGRhdGEuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGFnIEZlYXR1cmVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMYWcgZmVhdHVyZXMgeOKCnOKCi+KCgSwgeOKCnOKCi+KCgiwgLi4uLCB44oKc4oKL4oKaIHByb3ZpZGUgYXV0b3JlZ3Jlc3NpdmUgaW5wdXRzIHRvIGFueSBNTCBtb2RlbC4gVGhlIGxhZyBvcmRlciBwIHNob3VsZCBjb3ZlciB0aGUgcmVsZXZhbnQgYXV0b2NvcnJlbGF0aW9uIHN0cnVjdHVyZSDigJQgaW5zcGVjdCB0aGUgUEFDRiBwbG90IHRvIGlkZW50aWZ5IG1lYW5pbmdmdWwgbGFncy4gQ29tbW9uIGNob2ljZXM6IGxhZy0xIChkYWlseSksIGxhZy03ICh3ZWVrbHkpLCBsYWctMjggKG1vbnRobHkpIGZvciBkYWlseSBzZXJpZXM7IGxhZy0xMiwgbGFnLTI0IGZvciBob3VybHkgc2VyaWVzIHdpdGggZGFpbHkvd2Vla2x5IGN5Y2xlcy4gTGFncyBpbnRyb2R1Y2UgTmFOIHZhbHVlcyBhdCB0aGUgc3RhcnQgb2YgdGhlIHNlcmllcyDigJQgZHJvcCB0aGVzZSByb3dzIG9yIGltcHV0ZSBjYXJlZnVsbHkuIEFsd2F5cyBjcmVhdGUgbGFncyBhZnRlciB0aGUgdHJhaW4vdGVzdCBzcGxpdCBvciB1c2Ugc3RyaWN0bHkgcGFzdCB2YWx1ZXMgdG8gcHJldmVudCBsZWFrYWdlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBwYW5kYXMgYXMgcGRcblxubnAucmFuZG9tLnNlZWQoNDIpXG5kYXRlcyA9IHBkLmRhdGVfcmFuZ2UoXHUwMDI3MjAyMy0wMS0wMVx1MDAyNywgcGVyaW9kcz0zNjUsIGZyZXE9XHUwMDI3RFx1MDAyNylcbnQgPSBucC5hcmFuZ2UoMzY1KVxueSA9IDUwICsgMC4xICogdCArIDggKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDcpICsgbnAucmFuZG9tLnJhbmRuKDM2NSkgKiAyXG5kZiA9IHBkLkRhdGFGcmFtZSh7XHUwMDI3ZGF0ZVx1MDAyNzogZGF0ZXMsIFx1MDAyN3lcdTAwMjc6IHl9KS5zZXRfaW5kZXgoXHUwMDI3ZGF0ZVx1MDAyNylcblxubGFnX2NvbHMgPSBbMSwgMiwgMywgNywgMTQsIDI4XVxuZm9yIGxhZyBpbiBsYWdfY29sczpcbiAgICBkZltmXHUwMDI3bGFnX3tsYWd9XHUwMDI3XSA9IGRmW1x1MDAyN3lcdTAwMjddLnNoaWZ0KGxhZylcblxud2luZG93cyA9IFszLCA3LCAxNF1cbmZvciB3IGluIHdpbmRvd3M6XG4gICAgZGZbZlx1MDAyN3JvbGxfbWVhbl97d31cdTAwMjddID0gZGZbXHUwMDI3eVx1MDAyN10uc2hpZnQoMSkucm9sbGluZyh3KS5tZWFuKClcbiAgICBkZltmXHUwMDI3cm9sbF9zdGRfe3d9XHUwMDI3XSAgPSBkZltcdTAwMjd5XHUwMDI3XS5zaGlmdCgxKS5yb2xsaW5nKHcpLnN0ZCgpXG4gICAgZGZbZlx1MDAyN3JvbGxfbWF4X3t3fVx1MDAyN10gID0gZGZbXHUwMDI3eVx1MDAyN10uc2hpZnQoMSkucm9sbGluZyh3KS5tYXgoKVxuXG5kZltcdTAwMjdld21fN1x1MDAyN10gID0gZGZbXHUwMDI3eVx1MDAyN10uc2hpZnQoMSkuZXdtKHNwYW49NywgYWRqdXN0PUZhbHNlKS5tZWFuKClcbmRmW1x1MDAyN2RpZmZfMVx1MDAyN10gPSBkZltcdTAwMjd5XHUwMDI3XS5kaWZmKDEpXG5kZltcdTAwMjdwY3RfY2hhbmdlXzFcdTAwMjddID0gZGZbXHUwMDI3eVx1MDAyN10ucGN0X2NoYW5nZSgxKVxuXG5kZl9mZWF0ID0gZGYuZHJvcG5hKClcbnByaW50KGZcdTAwMjdGZWF0dXJlIG1hdHJpeCBzaGFwZToge2RmX2ZlYXQuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0ZlYXR1cmVzOiB7bGlzdChkZl9mZWF0LmNvbHVtbnMpfVx1MDAyNylcbnByaW50KGRmX2ZlYXQuaGVhZCgzKS50b19zdHJpbmcoKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSb2xsaW5nIFN0YXRpc3RpY3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJvbGxpbmcgc3RhdGlzdGljcyBzdW1tYXJpc2UgcmVjZW50IGhpc3RvcnkgaW4gYSBzaW5nbGUgc2NhbGFyLiBSb2xsaW5nIG1lYW4gKHdpbmRvdyB3KTogc21vb3RocyBsb2NhbCBsZXZlbCwgYW5hbG9nb3VzIHRvIGEgbW92aW5nIGF2ZXJhZ2UgdHJlbmQuIFJvbGxpbmcgc3RkOiBjYXB0dXJlcyBsb2NhbCB2b2xhdGlsaXR5IOKAlCB1c2VmdWwgZm9yIGZpbmFuY2lhbCBhbmQgZGVtYW5kIHNlcmllcy4gUm9sbGluZyBtaW4vbWF4OiByZXZlYWxzIHJhbmdlIGFuZCBleHRyZW1lIHZhbHVlcyBpbiB0aGUgcmVjZW50IHdpbmRvdy4gRXhwb25lbnRpYWxseSB3ZWlnaHRlZCBtb3ZpbmcgKGV3bSkgc3RhdGlzdGljcyBkb3duLXdlaWdodCBkaXN0YW50IG9ic2VydmF0aW9ucyB3aXRoaW4gdGhlIHdpbmRvdy4gQ3JpdGljYWwgcnVsZTogYWxsIHJvbGxpbmcgZmVhdHVyZXMgbXVzdCB1c2Ugc2hpZnQoMSkgYmVmb3JlIHRoZSByb2xsaW5nIGNhbGwgdG8gZW5zdXJlIHRoZSB3aW5kb3cgY292ZXJzIG9ubHkgcGFzdCBvYnNlcnZhdGlvbnMgKHQtdyB0byB0LTEpLCBwcmV2ZW50aW5nIGxlYWthZ2Ugb2YgdGhlIGN1cnJlbnQgdGFyZ2V0IHnigpwgaW50byB0aGUgZmVhdHVyZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRm91cmllciBGZWF0dXJlcyBmb3IgU2Vhc29uYWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvdXJpZXIgZmVhdHVyZXMgZW5jb2RlIHBlcmlvZGljIHBhdHRlcm5zIHdpdGhvdXQgaW5kaWNhdG9yIGR1bW1pZXMuIEZvciBhIHNlYXNvbmFsIHBlcmlvZCBQIGFuZCBoYXJtb25pYyBvcmRlciBLLCB0aGUgZmVhdHVyZXMgYXJlIHNpbigyz4BrdC9QKSBhbmQgY29zKDLPgGt0L1ApIGZvciBrPTEsLi4uLEsuIEsgcGFpcnMgb2Ygc2luL2NvcyB0ZXJtcyBjYW4gcmVwcmVzZW50IGFueSBzZWFzb25hbCBwYXR0ZXJuOyBLPTEgY2FwdHVyZXMgdGhlIGZ1bmRhbWVudGFsIGZyZXF1ZW5jeSwgaGlnaGVyIEsgYWRkIGhhcm1vbmljcyBmb3Igbm9uLXNpbnVzb2lkYWwgc2hhcGVzLiBXaXRoIEs9MyBhbmQgUD03IHlvdSBuZWVkIG9ubHkgNiBmZWF0dXJlcyB2ZXJzdXMgNiBkdW1taWVzIGZvciBkYXktb2Ytd2Vlay4gRm91cmllciBmZWF0dXJlcyBhcmUgY29udGludW91cyBhbmQgZ2VuZXJhbGlzZSB0byBzZXJpZXMgc2hvcnRlciB0aGFuIG9uZSBmdWxsIHBlcmlvZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgcGFuZGFzIGFzIHBkXG5cbmRlZiBmb3VyaWVyX2ZlYXR1cmVzKHRpbWVfaW5kZXgsIHBlcmlvZCwgSyk6XG4gICAgXCJcIlwiUmV0dXJuIHNpbi9jb3MgRm91cmllciBmZWF0dXJlcyBmb3IgZ2l2ZW4gcGVyaW9kIGFuZCBoYXJtb25pYyBvcmRlciBLLlwiXCJcIlxuICAgIGZlYXR1cmVzID0ge31cbiAgICBmb3IgayBpbiByYW5nZSgxLCBLICsgMSk6XG4gICAgICAgIGZlYXR1cmVzW2ZcdTAwMjdzaW5fUHtwZXJpb2R9X0t7a31cdTAwMjddID0gbnAuc2luKDIgKiBucC5waSAqIGsgKiB0aW1lX2luZGV4IC8gcGVyaW9kKVxuICAgICAgICBmZWF0dXJlc1tmXHUwMDI3Y29zX1B7cGVyaW9kfV9Le2t9XHUwMDI3XSA9IG5wLmNvcygyICogbnAucGkgKiBrICogdGltZV9pbmRleCAvIHBlcmlvZClcbiAgICByZXR1cm4gcGQuRGF0YUZyYW1lKGZlYXR1cmVzKVxuXG50ID0gbnAuYXJhbmdlKDM2NSlcbnkgPSA1MCArIDEwICogbnAuc2luKDIgKiBucC5waSAqIHQgLyA3KSArIDUgKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDM2NSkgKyBucC5yYW5kb20ucmFuZG4oMzY1KVxuXG4jIFdlZWtseSBzZWFzb25hbGl0eSAoUD03LCBLPTMpICsgYW5udWFsIHNlYXNvbmFsaXR5IChQPTM2NSwgSz0yKVxuZmZfd2Vla2x5ICA9IGZvdXJpZXJfZmVhdHVyZXModCwgcGVyaW9kPTcsICAgSz0zKVxuZmZfYW5udWFsICA9IGZvdXJpZXJfZmVhdHVyZXModCwgcGVyaW9kPTM2NSwgSz0yKVxuWF9mb3VyaWVyICA9IHBkLmNvbmNhdChbZmZfd2Vla2x5LCBmZl9hbm51YWxdLCBheGlzPTEpXG5cbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcjJfc2NvcmVcblxubW9kZWwgPSBSaWRnZShhbHBoYT0xLjApLmZpdChYX2ZvdXJpZXJbOjMwMF0sIHlbOjMwMF0pXG5wcmVkICA9IG1vZGVsLnByZWRpY3QoWF9mb3VyaWVyWzMwMDpdKVxucHJpbnQoZlx1MDAyN0ZvdXJpZXIgZmVhdHVyZSBjb3VudDoge1hfZm91cmllci5zaGFwZVsxXX1cdTAwMjcpXG5wcmludChmXHUwMDI3VGVzdCBSwrIgdXNpbmcgb25seSBGb3VyaWVyIGZlYXR1cmVzOiB7cjJfc2NvcmUoeVszMDA6XSwgcHJlZCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN0ZlYXR1cmUgbmFtZXM6XHUwMDI3LCBsaXN0KFhfZm91cmllci5jb2x1bW5zKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDeWNsaWNhbCBFbmNvZGluZyBmb3IgQ2FsZW5kYXIgRmVhdHVyZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNhbGVuZGFyIGZlYXR1cmVzIGxpa2UgaG91ci1vZi1kYXkgKDDigJMyMyksIGRheS1vZi13ZWVrICgw4oCTNiksIGFuZCBtb250aC1vZi15ZWFyICgx4oCTMTIpIGFyZSBjaXJjdWxhcjogaG91ciAyMyBpcyBhZGphY2VudCB0byBob3VyIDAuIEVuY29kaW5nIHRoZW0gYXMgaW50ZWdlcnMgKDAsIDEsIDIsIC4uLikgZ2l2ZXMgZGlzdGFuY2UgMjMgYmV0d2VlbiBob3VyIDAgYW5kIGhvdXIgMjMsIHdoZW4gdGhlIHRydWUgZGlzdGFuY2UgaXMgMS4gQ3ljbGljYWwgZW5jb2RpbmcgbWFwcyBpbnRlZ2VyIHYgdG8gc2luKDLPgHYvbWF4X3YpIGFuZCBjb3MoMs+Adi9tYXhfdiksIHBsYWNpbmcgdmFsdWVzIG9uIGEgdW5pdCBjaXJjbGUgc28gZGlzdGFuY2UgaXMgcHJlc2VydmVkLiBUaGlzIGdpdmVzIHRoZSBtb2RlbCBhIGNvbnRpbnVvdXMsIHBlcmlvZGljIHJlcHJlc2VudGF0aW9uIHdpdGhvdXQgYW55IGRpc2NvbnRpbnVpdHkgYXQgdGhlIGJvdW5kYXJ5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBwYW5kYXMgYXMgcGRcblxuZGVmIGN5Y2xpY2FsX2VuY29kZShzZXJpZXMsIG1heF92YWwpOlxuICAgIFwiXCJcIkVuY29kZSBhIGNpcmN1bGFyIGZlYXR1cmUgYXMgKHNpbiwgY29zKSBwYWlyLlwiXCJcIlxuICAgIGFuZ2xlID0gMiAqIG5wLnBpICogc2VyaWVzIC8gbWF4X3ZhbFxuICAgIHJldHVybiBucC5zaW4oYW5nbGUpLCBucC5jb3MoYW5nbGUpXG5cbmRhdGVzID0gcGQuZGF0ZV9yYW5nZShcdTAwMjcyMDIzLTAxLTAxXHUwMDI3LCBwZXJpb2RzPTg3NjAsIGZyZXE9XHUwMDI3aFx1MDAyNylcbmRmID0gcGQuRGF0YUZyYW1lKHtcdTAwMjdkYXRldGltZVx1MDAyNzogZGF0ZXN9KVxuZGZbXHUwMDI3aG91clx1MDAyN10gICAgICAgID0gZGZbXHUwMDI3ZGF0ZXRpbWVcdTAwMjddLmR0LmhvdXJcbmRmW1x1MDAyN2RheW9md2Vla1x1MDAyN10gICA9IGRmW1x1MDAyN2RhdGV0aW1lXHUwMDI3XS5kdC5kYXlvZndlZWtcbmRmW1x1MDAyN21vbnRoXHUwMDI3XSAgICAgICA9IGRmW1x1MDAyN2RhdGV0aW1lXHUwMDI3XS5kdC5tb250aFxuZGZbXHUwMDI3ZGF5b2Z5ZWFyXHUwMDI3XSAgID0gZGZbXHUwMDI3ZGF0ZXRpbWVcdTAwMjddLmR0LmRheW9meWVhclxuXG5kZltcdTAwMjdob3VyX3Npblx1MDAyN10sICAgZGZbXHUwMDI3aG91cl9jb3NcdTAwMjddICAgPSBjeWNsaWNhbF9lbmNvZGUoZGZbXHUwMDI3aG91clx1MDAyN10sICAgICAgMjQpXG5kZltcdTAwMjdkb3dfc2luXHUwMDI3XSwgICAgZGZbXHUwMDI3ZG93X2Nvc1x1MDAyN10gICAgPSBjeWNsaWNhbF9lbmNvZGUoZGZbXHUwMDI3ZGF5b2Z3ZWVrXHUwMDI3XSwgIDcpXG5kZltcdTAwMjdtb250aF9zaW5cdTAwMjddLCAgZGZbXHUwMDI3bW9udGhfY29zXHUwMDI3XSAgPSBjeWNsaWNhbF9lbmNvZGUoZGZbXHUwMDI3bW9udGhcdTAwMjddLCAgICAgMTIpXG5kZltcdTAwMjdkb3lfc2luXHUwMDI3XSwgICAgZGZbXHUwMDI3ZG95X2Nvc1x1MDAyN10gICAgPSBjeWNsaWNhbF9lbmNvZGUoZGZbXHUwMDI3ZGF5b2Z5ZWFyXHUwMDI3XSwgMzY1KVxuXG5kZltcdTAwMjdpc193ZWVrZW5kXHUwMDI3XSAgPSAoZGZbXHUwMDI3ZGF5b2Z3ZWVrXHUwMDI3XSBcdTAwM2U9IDUpLmFzdHlwZShpbnQpXG5kZltcdTAwMjdpc19idXNpbmVzc1x1MDAyN10gPSAoKGRmW1x1MDAyN2hvdXJcdTAwMjddIFx1MDAzZT0gOSkgXHUwMDI2IChkZltcdTAwMjdob3VyXHUwMDI3XSBcdTAwM2MgMTcpIFx1MDAyNiAoZGZbXHUwMDI3aXNfd2Vla2VuZFx1MDAyN10gPT0gMCkpLmFzdHlwZShpbnQpXG5cbmN5Y2xpY2FsX2NvbHMgPSBbYyBmb3IgYyBpbiBkZi5jb2x1bW5zIGlmIGMuZW5kc3dpdGgoXHUwMDI3X3Npblx1MDAyNykgb3IgYy5lbmRzd2l0aChcdTAwMjdfY29zXHUwMDI3KV1cbnByaW50KGZcdTAwMjdDeWNsaWNhbCBmZWF0dXJlczoge2N5Y2xpY2FsX2NvbHN9XHUwMDI3KVxucHJpbnQoZlx1MDAyN2hvdXI9MCAgLVx1MDAzZSBzaW49e2RmLmxvY1swLFwiaG91cl9zaW5cIl06LjNmfSwgY29zPXtkZi5sb2NbMCxcImhvdXJfY29zXCJdOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3aG91cj0yMyAtXHUwMDNlIHNpbj17ZGYubG9jWzIzLFwiaG91cl9zaW5cIl06LjNmfSwgY29zPXtkZi5sb2NbMjMsXCJob3VyX2Nvc1wiXTouM2Z9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiUHJldmVudCBUYXJnZXQgTGVha2FnZSB3aXRoIExhZyBBbGlnbm1lbnQiLCJjb250ZW50IjoiV2hlbiBjb21wdXRpbmcgcm9sbGluZyBmZWF0dXJlcyBmb3Igcm93IHQsIHRoZSB3aW5kb3cgbXVzdCBjb3ZlciBvbmx5IHQtdyB0byB0LTEuIEFsd2F5cyBjYWxsIHNoaWZ0KDEpIGJlZm9yZSByb2xsaW5nKCkgaW4gcGFuZGFzOiBkZltcdTAwMjd5XHUwMDI3XS5zaGlmdCgxKS5yb2xsaW5nKDcpLm1lYW4oKS4gV2l0aG91dCBzaGlmdCgxKSwgdGhlIHJvbGxpbmcgd2luZG93IGluY2x1ZGVzIHnigpwgaXRzZWxmLCBsZWFraW5nIHRoZSB0YXJnZXQgaW50byB0aGUgZmVhdHVyZSBhbmQgcHJvZHVjaW5nIHVucmVhbGlzdGljYWxseSBsb3cgdHJhaW5pbmcgZXJyb3IuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmVhdHVyZSBJbXBvcnRhbmNlIHdpdGggTGlnaHRHQk0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkdyYWRpZW50LWJvb3N0ZWQgdHJlZXMgKExpZ2h0R0JNLCBYR0Jvb3N0LCBDYXRCb29zdCkgYXJlIHRoZSBkb21pbmFudCB0YWJ1bGFyIGZvcmVjYXN0aW5nIG1vZGVscyB3aGVuIGNvbWJpbmVkIHdpdGggcmljaCBsYWcgYW5kIHJvbGxpbmcgZmVhdHVyZXMuIExpZ2h0R0JNXHUwMDI3cyBzcGxpdC1nYWluIGltcG9ydGFuY2UgcmV2ZWFscyB3aGljaCBmZWF0dXJlcyB0aGUgbW9kZWwgcmVsaWVzIG9uIG1vc3Q6IGxhZ18xIGFuZCBsYWdfNyB0eXBpY2FsbHkgZG9taW5hdGUgZm9yIGRhaWx5IHNlcmllcyB3aXRoIHdlZWtseSBwYXR0ZXJucywgd2hpbGUgRm91cmllciBmZWF0dXJlcyBvdXRwZXJmb3JtIHJhdyBkYXktb2Ytd2VlayBkdW1taWVzIGZvciBsb25nIHNlYXNvbmFsIGN5Y2xlcy4gUnVubmluZyBmZWF0dXJlIGltcG9ydGFuY2UgYWZ0ZXIgdGhlIGZpcnN0IHRyYWluaW5nIHBhc3MgZ3VpZGVzIHBydW5pbmcg4oCUIHJlbW92aW5nIGxvdy1pbXBvcnRhbmNlIGZlYXR1cmVzIHJlZHVjZXMgb3ZlcmZpdHRpbmcgYW5kIHNwZWVkcyBpbmZlcmVuY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHBhbmRhcyBhcyBwZFxuaW1wb3J0IGxpZ2h0Z2JtIGFzIGxnYlxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuXG5ucC5yYW5kb20uc2VlZCgwKVxudCA9IG5wLmFyYW5nZSg1MDApXG55ID0gMzAgKyAwLjIgKiB0ICsgMTIgKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDcpICsgbnAucmFuZG9tLnJhbmRuKDUwMCkgKiAzXG5kZiA9IHBkLkRhdGFGcmFtZSh7XHUwMDI3eVx1MDAyNzogeX0pXG5cbmZvciBsYWcgaW4gWzEsIDIsIDMsIDcsIDE0XTpcbiAgICBkZltmXHUwMDI3bGFnX3tsYWd9XHUwMDI3XSA9IGRmW1x1MDAyN3lcdTAwMjddLnNoaWZ0KGxhZylcbmZvciB3IGluIFszLCA3LCAxNF06XG4gICAgZGZbZlx1MDAyN3JvbGxfbWVhbl97d31cdTAwMjddID0gZGZbXHUwMDI3eVx1MDAyN10uc2hpZnQoMSkucm9sbGluZyh3KS5tZWFuKClcbiAgICBkZltmXHUwMDI3cm9sbF9zdGRfe3d9XHUwMDI3XSAgPSBkZltcdTAwMjd5XHUwMDI3XS5zaGlmdCgxKS5yb2xsaW5nKHcpLnN0ZCgpXG5cbmRmW1x1MDAyN2Rvd19zaW5cdTAwMjddID0gbnAuc2luKDIgKiBucC5waSAqICh0ICUgNykgLyA3KVxuZGZbXHUwMDI3ZG93X2Nvc1x1MDAyN10gPSBucC5jb3MoMiAqIG5wLnBpICogKHQgJSA3KSAvIDcpXG5kZiA9IGRmLmRyb3BuYSgpXG5cblggPSBkZi5kcm9wKFx1MDAyN3lcdTAwMjcsIGF4aXM9MSlcbnlfY2xlYW4gPSBkZltcdTAwMjd5XHUwMDI3XS52YWx1ZXNcblxubW9kZWwgPSBsZ2IuTEdCTVJlZ3Jlc3NvcihuX2VzdGltYXRvcnM9MzAwLCBsZWFybmluZ19yYXRlPTAuMDUsIHJhbmRvbV9zdGF0ZT00Milcbm1vZGVsLmZpdChYLCB5X2NsZWFuKVxuXG5pbXBvcnRhbmNlID0gcGQuU2VyaWVzKG1vZGVsLmZlYXR1cmVfaW1wb3J0YW5jZXNfLCBpbmRleD1YLmNvbHVtbnMpXG5wcmludChcdTAwMjdUb3AgMTAgZmVhdHVyZXMgYnkgTGlnaHRHQk0gaW1wb3J0YW5jZTpcdTAwMjcpXG5wcmludChpbXBvcnRhbmNlLm5sYXJnZXN0KDEwKS50b19zdHJpbmcoKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGZWF0dXJlIEVuZ2luZWVyaW5nIFJlZmVyZW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJGZWF0dXJlIFR5cGUiLCJDYXB0dXJlcyIsIkhpc3RvcnkgTmVlZGVkIiwiTGVha2FnZSBSaXNrIiwiTm90ZXMiXSwicm93cyI6W1siTGFnICh0LWspIiwiQXV0b2NvcnJlbGF0aW9uIGF0IGxhZyBrIiwiayBwZXJpb2RzIiwiTG93IGlmIGsg4omlIGZvcmVjYXN0IGhvcml6b24iLCJVc2UgUEFDRiB0byBjaG9vc2UgayJdLFsiUm9sbGluZyBtZWFuICh3KSIsIkxvY2FsIGxldmVsIC8gdHJlbmQiLCJ3IHBlcmlvZHMiLCJIaWdoIHdpdGhvdXQgc2hpZnQoMSkiLCJBbHdheXMgc2hpZnQoMSkgYmVmb3JlIHJvbGxpbmciXSxbIlJvbGxpbmcgc3RkICh3KSIsIkxvY2FsIHZvbGF0aWxpdHkiLCJ3IHBlcmlvZHMiLCJIaWdoIHdpdGhvdXQgc2hpZnQoMSkiLCJVc2VmdWwgZm9yIGZpbmFuY2lhbCBzZXJpZXMiXSxbIkZvdXJpZXIgc2luL2NvcyIsIkdsb2JhbCBwZXJpb2RpY2l0eSBhdCBQIiwiRnVsbCBwZXJpb2QgUCIsIk5vbmUg4oCUIGRldGVybWluaXN0aWMiLCJLPTMgdXN1YWxseSBzdWZmaWNpZW50Il0sWyJDeWNsaWNhbCBzaW4vY29zIiwiQ2lyY3VsYXIgY2FsZW5kYXIgZmVhdHVyZXMiLCJOb25lIOKAlCBkZXJpdmVkIiwiTm9uZSDigJQgZGV0ZXJtaW5pc3RpYyIsIlJlcGxhY2UgcmF3IGludGVnZXIgZW5jb2RpbmdzIl0sWyJEZWx0YSAvIGRpZmYoaykiLCJSYXRlIG9mIGNoYW5nZSIsImsrMSBwZXJpb2RzIiwiTG93IGlmIGsg4omlIGhvcml6b24iLCJTdGFiaWxpc2VzIG5vbi1zdGF0aW9uYXJ5IHNlcmllcyJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJBbHdheXMgaW5zcGVjdCB0aGUgUEFDRiBwbG90IGJlZm9yZSBzZWxlY3RpbmcgbGFnIG9yZGVycyDigJQgb25seSBpbmNsdWRlIGxhZ3Mgd2l0aCBzaWduaWZpY2FudCBwYXJ0aWFsIGF1dG9jb3JyZWxhdGlvbnMuIiwiSW5jbHVkZSBsYWctNyBhbmQgbGFnLTE0IGZvciB3ZWVrbHkgZGFpbHkgZGF0YTsgbGFnLTEyIGFuZCBsYWctMjQgZm9yIGhvdXJseSBkYXRhIHdpdGggZGFpbHkvd2Vla2x5IGN5Y2xlcy4iLCJGb3VyaWVyIGZlYXR1cmVzIG91dHBlcmZvcm0gb25lLWhvdCBkYXkvbW9udGggZHVtbWllcyB3aGVuIHRoZSBzZWFzb25hbCBwYXR0ZXJuIGlzIHNtb290aC4iLCJDeWNsaWNhbCBzaW4vY29zIGVuY29kaW5nIGlzIGVzc2VudGlhbCBmb3IgaG91ci1vZi1kYXkgYW5kIGRheS1vZi13ZWVrIHdoZW4gdXNpbmcgZGlzdGFuY2UtYmFzZWQgbW9kZWxzIChLTk4sIFNWTSkuIiwiRGVsdGEgZmVhdHVyZXMgKHnigpwgLSB54oKc4oKL4oKBKSByZWR1Y2Ugbm9uLXN0YXRpb25hcml0eSBhbmQgY2FuIGltcHJvdmUgdHJlZSBtb2RlbCBwZXJmb3JtYW5jZS4iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGZWF0dXJlIHNlbGVjdGlvbiBmb3IgdGltZS1zZXJpZXMgTUwgZm9sbG93cyBhIGRpZmZlcmVudCBsb2dpYyB0aGFuIHN0YXRpYyB0YWJ1bGFyIGRhdGEuIEJlY2F1c2UgbGFnIGZlYXR1cmVzIGFyZSBjb3JyZWxhdGVkIChsYWdfMSBhbmQgbGFnXzIgY2Fycnkgb3ZlcmxhcHBpbmcgaW5mb3JtYXRpb24pLCBzdGFuZGFyZCBTSEFQIHZhbHVlcyBvciBwZXJtdXRhdGlvbiBpbXBvcnRhbmNlIGNhbiBiZSBtaXNsZWFkaW5nIOKAlCByZW1vdmluZyBhbnkgc2luZ2xlIGNvcnJlbGF0ZWQgbGFnIG1heSBub3QgcmVkdWNlIGVycm9yIGJlY2F1c2Ugb3RoZXJzIGNvbXBlbnNhdGUuIEluc3RlYWQsIHVzZSByZWN1cnNpdmUgZmVhdHVyZSBlbGltaW5hdGlvbiB3aXRoIGEgdGVtcG9yYWwgQ1YgbG9vcCB0byBpZGVudGlmeSB0aGUgbWluaW11bSBmZWF0dXJlIHNldCB0aGF0IHByZXNlcnZlcyBvdXQtb2Ytc2FtcGxlIGFjY3VyYWN5LCB0aGVuIHJlLXRyYWluIHRoZSBmaW5hbCBtb2RlbCBvbiB0aGUgZnVsbCByZWR1Y2VkIGZlYXR1cmUgc2V0LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIG11bHRpdmFyaWF0ZSBmb3JlY2FzdGluZyB3aGVyZSBjb3ZhcmlhdGVzICh3ZWF0aGVyLCBwcm9tb3Rpb25zLCBwcmljZXMpIHN1cHBsZW1lbnQgdGhlIHRhcmdldCBzZXJpZXMsIGZlYXR1cmUgZW5naW5lZXJpbmcgZXh0ZW5kcyBuYXR1cmFsbHkuIENyZWF0ZSBsYWcgYW5kIHJvbGxpbmcgZmVhdHVyZXMgZm9yIGVhY2ggY292YXJpYXRlIGluIGFkZGl0aW9uIHRvIHRoZSB0YXJnZXQuIEZvciBrbm93biBmdXR1cmUgY292YXJpYXRlcyAoZS5nLiwgcHJvbW90aW9ucyBjYWxlbmRhciwgaG9saWRheSBmbGFncykgbm8gbGFnIGFsaWdubWVudCBpcyBuZWVkZWQg4oCUIHRoZWlyIGZ1dHVyZSB2YWx1ZXMgYXJlIGF2YWlsYWJsZSBhdCBwcmVkaWN0aW9uIHRpbWUuIEZvciB1bmtub3duIGZ1dHVyZSBjb3ZhcmlhdGVzIChlLmcuLCBjb21wZXRpdG9yIHByaWNlcyksIHVzZSB0aGVpciBsYWdnZWQgdmFsdWVzIG9ubHkgYW5kIGJlIGV4cGxpY2l0IGFib3V0IHRoZSBpbmZvcm1hdGlvbiBjdXRvZmYgaG9yaXpvbiB0aGV5IGltcG9zZS4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Time-Series Feature Engineering — Lag, Rolling, and Fourier Features

Classical ML models (Random Forest, LightGBM, XGBoost) cannot process raw time-series sequences — they need a fixed-width feature vector per prediction point. Feature engineering converts sequential observations into tabular inputs: lag features capture autocorrelation, rolling statistics summarise local trends and volatility, Fourier terms encode seasonality compactly, and cyclical calendar encodings preserve the circular structure of hours, days, and months. Thoughtful feature construction often outperforms deep sequence models for short-to-medium horizon forecasting on structured data.

## Lag Features

Lag features xₜ₋₁, xₜ₋₂, ..., xₜ₋ₚ provide autoregressive inputs to any ML model. The lag order p should cover the relevant autocorrelation structure — inspect the PACF plot to identify meaningful lags. Common choices: lag-1 (daily), lag-7 (weekly), lag-28 (monthly) for daily series; lag-12, lag-24 for hourly series with daily/weekly cycles. Lags introduce NaN values at the start of the series — drop these rows or impute carefully. Always create lags after the train/test split or use strictly past values to prevent leakage.

```python
import numpy as np
import pandas as pd

np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
t = np.arange(365)
y = 50 + 0.1 * t + 8 * np.sin(2 * np.pi * t / 7) + np.random.randn(365) * 2
df = pd.DataFrame({'date': dates, 'y': y}).set_index('date')

lag_cols = [1, 2, 3, 7, 14, 28]
for lag in lag_cols:
    df[f'lag_{lag}'] = df['y'].shift(lag)

windows = [3, 7, 14]
for w in windows:
    df[f'roll_mean_{w}'] = df['y'].shift(1).rolling(w).mean()
    df[f'roll_std_{w}']  = df['y'].shift(1).rolling(w).std()
    df[f'roll_max_{w}']  = df['y'].shift(1).rolling(w).max()

df['ewm_7']  = df['y'].shift(1).ewm(span=7, adjust=False).mean()
df['diff_1'] = df['y'].diff(1)
df['pct_change_1'] = df['y'].pct_change(1)

df_feat = df.dropna()
print(f'Feature matrix shape: {df_feat.shape}')
print(f'Features: {list(df_feat.columns)}')
print(df_feat.head(3).to_string())
```

## Rolling Statistics

Rolling statistics summarise recent history in a single scalar. Rolling mean (window w): smooths local level, analogous to a moving average trend. Rolling std: captures local volatility — useful for financial and demand series. Rolling min/max: reveals range and extreme values in the recent window. Exponentially weighted moving (ewm) statistics down-weight distant observations within the window. Critical rule: all rolling features must use shift(1) before the rolling call to ensure the window covers only past observations (t-w to t-1), preventing leakage of the current target yₜ into the features.

## Fourier Features for Seasonality

Fourier features encode periodic patterns without indicator dummies. For a seasonal period P and harmonic order K, the features are sin(2πkt/P) and cos(2πkt/P) for k=1,...,K. K pairs of sin/cos terms can represent any seasonal pattern; K=1 captures the fundamental frequency, higher K add harmonics for non-sinusoidal shapes. With K=3 and P=7 you need only 6 features versus 6 dummies for day-of-week. Fourier features are continuous and generalise to series shorter than one full period.

```python
import numpy as np
import pandas as pd

def fourier_features(time_index, period, K):
    """Return sin/cos Fourier features for given period and harmonic order K."""
    features = {}
    for k in range(1, K + 1):
        features[f'sin_P{period}_K{k}'] = np.sin(2 * np.pi * k * time_index / period)
        features[f'cos_P{period}_K{k}'] = np.cos(2 * np.pi * k * time_index / period)
    return pd.DataFrame(features)

t = np.arange(365)
y = 50 + 10 * np.sin(2 * np.pi * t / 7) + 5 * np.sin(2 * np.pi * t / 365) + np.random.randn(365)

# Weekly seasonality (P=7, K=3) + annual seasonality (P=365, K=2)
ff_weekly  = fourier_features(t, period=7,   K=3)
ff_annual  = fourier_features(t, period=365, K=2)
X_fourier  = pd.concat([ff_weekly, ff_annual], axis=1)

from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

model = Ridge(alpha=1.0).fit(X_fourier[:300], y[:300])
pred  = model.predict(X_fourier[300:])
print(f'Fourier feature count: {X_fourier.shape[1]}')
print(f'Test R² using only Fourier features: {r2_score(y[300:], pred):.4f}')
print('Feature names:', list(X_fourier.columns))
```

## Cyclical Encoding for Calendar Features

Calendar features like hour-of-day (0–23), day-of-week (0–6), and month-of-year (1–12) are circular: hour 23 is adjacent to hour 0. Encoding them as integers (0, 1, 2, ...) gives distance 23 between hour 0 and hour 23, when the true distance is 1. Cyclical encoding maps integer v to sin(2πv/max_v) and cos(2πv/max_v), placing values on a unit circle so distance is preserved. This gives the model a continuous, periodic representation without any discontinuity at the boundary.

```python
import numpy as np
import pandas as pd

def cyclical_encode(series, max_val):
    """Encode a circular feature as (sin, cos) pair."""
    angle = 2 * np.pi * series / max_val
    return np.sin(angle), np.cos(angle)

dates = pd.date_range('2023-01-01', periods=8760, freq='h')
df = pd.DataFrame({'datetime': dates})
df['hour']        = df['datetime'].dt.hour
df['dayofweek']   = df['datetime'].dt.dayofweek
df['month']       = df['datetime'].dt.month
df['dayofyear']   = df['datetime'].dt.dayofyear

df['hour_sin'],   df['hour_cos']   = cyclical_encode(df['hour'],      24)
df['dow_sin'],    df['dow_cos']    = cyclical_encode(df['dayofweek'],  7)
df['month_sin'],  df['month_cos']  = cyclical_encode(df['month'],     12)
df['doy_sin'],    df['doy_cos']    = cyclical_encode(df['dayofyear'], 365)

df['is_weekend']  = (df['dayofweek'] >= 5).astype(int)
df['is_business'] = ((df['hour'] >= 9) & (df['hour'] < 17) & (df['is_weekend'] == 0)).astype(int)

cyclical_cols = [c for c in df.columns if c.endswith('_sin') or c.endswith('_cos')]
print(f'Cyclical features: {cyclical_cols}')
print(f'hour=0  -> sin={df.loc[0,"hour_sin"]:.3f}, cos={df.loc[0,"hour_cos"]:.3f}')
print(f'hour=23 -> sin={df.loc[23,"hour_sin"]:.3f}, cos={df.loc[23,"hour_cos"]:.3f}')
```

> **Prevent Target Leakage with Lag Alignment**: When computing rolling features for row t, the window must cover only t-w to t-1. Always call shift(1) before rolling() in pandas: df['y'].shift(1).rolling(7).mean(). Without shift(1), the rolling window includes yₜ itself, leaking the target into the feature and producing unrealistically low training error.

## Feature Importance with LightGBM

Gradient-boosted trees (LightGBM, XGBoost, CatBoost) are the dominant tabular forecasting models when combined with rich lag and rolling features. LightGBM's split-gain importance reveals which features the model relies on most: lag_1 and lag_7 typically dominate for daily series with weekly patterns, while Fourier features outperform raw day-of-week dummies for long seasonal cycles. Running feature importance after the first training pass guides pruning — removing low-importance features reduces overfitting and speeds inference.

```python
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split

np.random.seed(0)
t = np.arange(500)
y = 30 + 0.2 * t + 12 * np.sin(2 * np.pi * t / 7) + np.random.randn(500) * 3
df = pd.DataFrame({'y': y})

for lag in [1, 2, 3, 7, 14]:
    df[f'lag_{lag}'] = df['y'].shift(lag)
for w in [3, 7, 14]:
    df[f'roll_mean_{w}'] = df['y'].shift(1).rolling(w).mean()
    df[f'roll_std_{w}']  = df['y'].shift(1).rolling(w).std()

df['dow_sin'] = np.sin(2 * np.pi * (t % 7) / 7)
df['dow_cos'] = np.cos(2 * np.pi * (t % 7) / 7)
df = df.dropna()

X = df.drop('y', axis=1)
y_clean = df['y'].values

model = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.05, random_state=42)
model.fit(X, y_clean)

importance = pd.Series(model.feature_importances_, index=X.columns)
print('Top 10 features by LightGBM importance:')
print(importance.nlargest(10).to_string())
```

## Feature Engineering Reference

| Feature Type | Captures | History Needed | Leakage Risk | Notes |
| --- | --- | --- | --- | --- |
| Lag (t-k) | Autocorrelation at lag k | k periods | Low if k ≥ forecast horizon | Use PACF to choose k |
| Rolling mean (w) | Local level / trend | w periods | High without shift(1) | Always shift(1) before rolling |
| Rolling std (w) | Local volatility | w periods | High without shift(1) | Useful for financial series |
| Fourier sin/cos | Global periodicity at P | Full period P | None — deterministic | K=3 usually sufficient |
| Cyclical sin/cos | Circular calendar features | None — derived | None — deterministic | Replace raw integer encodings |
| Delta / diff(k) | Rate of change | k+1 periods | Low if k ≥ horizon | Stabilises non-stationary series |

- Always inspect the PACF plot before selecting lag orders — only include lags with significant partial autocorrelations.
- Include lag-7 and lag-14 for weekly daily data; lag-12 and lag-24 for hourly data with daily/weekly cycles.
- Fourier features outperform one-hot day/month dummies when the seasonal pattern is smooth.
- Cyclical sin/cos encoding is essential for hour-of-day and day-of-week when using distance-based models (KNN, SVM).
- Delta features (yₜ - yₜ₋₁) reduce non-stationarity and can improve tree model performance.

Feature selection for time-series ML follows a different logic than static tabular data. Because lag features are correlated (lag_1 and lag_2 carry overlapping information), standard SHAP values or permutation importance can be misleading — removing any single correlated lag may not reduce error because others compensate. Instead, use recursive feature elimination with a temporal CV loop to identify the minimum feature set that preserves out-of-sample accuracy, then re-train the final model on the full reduced feature set.

For multivariate forecasting where covariates (weather, promotions, prices) supplement the target series, feature engineering extends naturally. Create lag and rolling features for each covariate in addition to the target. For known future covariates (e.g., promotions calendar, holiday flags) no lag alignment is needed — their future values are available at prediction time. For unknown future covariates (e.g., competitor prices), use their lagged values only and be explicit about the information cutoff horizon they impose.

---

