---
title: "Exponential Smoothing — Holt-Winters and ETS Models"
slug: "exponential-smoothing"
description: "Implement Simple Exponential Smoothing, Holt linear, and Holt-Winters from first principles, use the ETS state-space framework to compare model configurations by AIC, and trace the connection SES = ARIMA(0,1,1)."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXhwb25lbnRpYWwgc21vb3RoaW5nIHdlaWdodHMgcmVjZW50IG9ic2VydmF0aW9ucyBtb3JlIGhlYXZpbHkgdGhhbiBkaXN0YW50IG9uZXMgdXNpbmcgZ2VvbWV0cmljYWxseSBkZWNheWluZyB3ZWlnaHRzOiB0aGUgb2JzZXJ2YXRpb24gayBzdGVwcyBiYWNrIHJlY2VpdmVzIHdlaWdodCDOsSgxLc6xKV5rLCBzbyB0aGUgZm9yZWNhc3QgxbfigpzigorigoEgPSDOsc6j4oKWKDEtzrEpXmsgeeKCnOKCi+KCliBpcyBhbiBleHBvbmVudGlhbGx5IHdlaWdodGVkIGF2ZXJhZ2Ugb2YgYWxsIHBhc3QgdmFsdWVzLiBUaGUgRVRTIChFcnJvci1UcmVuZC1TZWFzb25hbCkgc3RhdGUtc3BhY2UgZnJhbWV3b3JrIHVuaWZpZXMgU2ltcGxlIEV4cG9uZW50aWFsIFNtb290aGluZywgSG9sdCBsaW5lYXIsIGFuZCBIb2x0LVdpbnRlcnMgdW5kZXIgYSBzaW5nbGUgbGlrZWxpaG9vZCwgZW5hYmxpbmcgcHJpbmNpcGxlZCBzZWxlY3Rpb24gYW1vbmcgMzAgbW9kZWwgY29uZmlndXJhdGlvbnMgYnkgQUlDLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNpbXBsZSBFeHBvbmVudGlhbCBTbW9vdGhpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNFUyBhcHBsaWVzIHRvIHNlcmllcyB3aXRoIG5vIHRyZW5kIGFuZCBubyBzZWFzb25hbGl0eS4gVGhlIHVwZGF0ZSBlcXVhdGlvbiDFt+KCnOKCiuKCgSA9IM6xeeKCnCArICgxLc6xKcW34oKcLCB3aXRoIM6xIOKIiCAoMCwxKSwgcGxhY2VzIHdlaWdodCDOsSBvbiB0aGUgbGF0ZXN0IG9ic2VydmF0aW9uIGFuZCAoMS3OsSkgb24gdGhlIHByZXZpb3VzIGZvcmVjYXN0LiBFeHBhbmRpbmcgcmVjdXJzaXZlbHkgeWllbGRzIHRoZSB3ZWlnaHRlZCBhdmVyYWdlIGZvcm0uIFNtYWxsIM6xIChuZWFyIDApIHNtb290aHMgaGVhdmlseSBhbmQgcmVhY3RzIHNsb3dseTsgbGFyZ2UgzrEgKG5lYXIgMSkgdHJhY2tzIHRoZSBzZXJpZXMgbmVhcmx5IG9ic2VydmF0aW9uLWJ5LW9ic2VydmF0aW9uLiBUaGUgb3B0aW1hbCDOsSBtaW5pbWlzZXMgdGhlIHN1bSBvZiBzcXVhcmVkIG9uZS1zdGVwLWFoZWFkIGZvcmVjYXN0IGVycm9ycywgc29sdmVkIG51bWVyaWNhbGx5IG9yIGJ5IGdyaWQgc2VhcmNoLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBtZWFuX3NxdWFyZWRfZXJyb3JcblxuZGVmIHNpbXBsZV9leHBfc21vb3RoaW5nKHNlcmllcywgYWxwaGEpOlxuICAgIFwiXCJcIlNFUyBmcm9tIHNjcmF0Y2gg4oCUIHJldHVybnMgaW4tc2FtcGxlIG9uZS1zdGVwLWFoZWFkIGZpdHRlZCB2YWx1ZXMuXCJcIlwiXG4gICAgbiA9IGxlbihzZXJpZXMpXG4gICAgZml0dGVkID0gbnAuemVyb3MobilcbiAgICBmaXR0ZWRbMF0gPSBzZXJpZXNbMF1cbiAgICBmb3IgdCBpbiByYW5nZSgxLCBuKTpcbiAgICAgICAgZml0dGVkW3RdID0gYWxwaGEgKiBzZXJpZXNbdCAtIDFdICsgKDEgLSBhbHBoYSkgKiBmaXR0ZWRbdCAtIDFdXG4gICAgcmV0dXJuIGZpdHRlZFxuXG5kZWYgb3B0aW1pc2VfYWxwaGEoc2VyaWVzKTpcbiAgICBcIlwiXCJHcmlkIHNlYXJjaCBmb3IgYWxwaGEgbWluaW1pc2luZyBpbi1zYW1wbGUgU1NFLlwiXCJcIlxuICAgIGJlc3RfYWxwaGEsIGJlc3Rfc3NlID0gMC4xLCBucC5pbmZcbiAgICBmb3IgYWxwaGEgaW4gbnAuYXJhbmdlKDAuMDUsIDEuMCwgMC4wNSk6XG4gICAgICAgIGZpdHRlZCA9IHNpbXBsZV9leHBfc21vb3RoaW5nKHNlcmllcywgYWxwaGEpXG4gICAgICAgIHNzZSA9IG5wLnN1bSgoc2VyaWVzWzE6XSAtIGZpdHRlZFsxOl0pICoqIDIpXG4gICAgICAgIGlmIHNzZSBcdTAwM2MgYmVzdF9zc2U6XG4gICAgICAgICAgICBiZXN0X3NzZSwgYmVzdF9hbHBoYSA9IHNzZSwgYWxwaGFcbiAgICByZXR1cm4gYmVzdF9hbHBoYVxuXG5ucC5yYW5kb20uc2VlZCg0MilcbnkgPSBucC5jdW1zdW0obnAucmFuZG9tLnJhbmRuKDEyMCkpICsgNTBcbmFscGhhX29wdCA9IG9wdGltaXNlX2FscGhhKHkpXG5maXR0ZWQgPSBzaW1wbGVfZXhwX3Ntb290aGluZyh5LCBhbHBoYV9vcHQpXG5uZXh0X3N0ZXAgPSBhbHBoYV9vcHQgKiB5Wy0xXSArICgxIC0gYWxwaGFfb3B0KSAqIGZpdHRlZFstMV1cbnJtc2UgPSBucC5zcXJ0KG1lYW5fc3F1YXJlZF9lcnJvcih5WzE6XSwgZml0dGVkWzE6XSkpXG5wcmludChmXHUwMDI3T3B0aW1hbCBhbHBoYSA9IHthbHBoYV9vcHQ6LjJmfVx1MDAyNylcbnByaW50KGZcdTAwMjdJbi1zYW1wbGUgUk1TRSA9IHtybXNlOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3T25lLXN0ZXAtYWhlYWQgZm9yZWNhc3QgPSB7bmV4dF9zdGVwOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSG9sdFx1MDAyN3MgTGluZWFyIE1ldGhvZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSG9sdFx1MDAyN3MgbGluZWFyIG1ldGhvZCBhZGRzIGEgdHJlbmQgY29tcG9uZW50IGLigpwgdG8gU0VTLiBMZXZlbDogbOKCnCA9IM6xeeKCnCArICgxLc6xKShs4oKc4oKL4oKBICsgYuKCnOKCi+KCgSkuIFRyZW5kOiBi4oKcID0gzrIobOKCnCAtIGzigpzigovigoEpICsgKDEtzrIpYuKCnOKCi+KCgS4gaC1zdGVwIGZvcmVjYXN0OiDFt+KCnOKCiuKClSA9IGzigpwgKyBowrdi4oKcLiBUaGUgZGFtcGVkIHZhcmlhbnQgbXVsdGlwbGllcyBlYWNoIHRyZW5kIHN0ZXAgYnkgz4Yg4oiIICgwLDEpOiDFt+KCnOKCiuKClSA9IGzigpwgKyAoz4YgKyDPhsKyICsgLi4uICsgz4bKsCli4oKcLCBwcmV2ZW50aW5nIGxpbmVhciBleHRyYXBvbGF0aW9uIGZyb20gb3ZlcnNob290aW5nIG9uIGxvbmcgaG9yaXpvbnMuIERhbXBlZCB0cmVuZCBpcyBlbXBpcmljYWxseSB0aGUgYmVzdCBzaW5nbGUgbWV0aG9kIGFjcm9zcyBtYWpvciBmb3JlY2FzdGluZyBjb21wZXRpdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSG9sdC1XaW50ZXJzIFNlYXNvbmFsIE1vZGVsIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIb2x0LVdpbnRlcnMgYWRkcyBhIHNlYXNvbmFsIGNvbXBvbmVudCBz4oKcIHdpdGggcGVyaW9kIG0uIEFkZGl0aXZlIGZvcm0gKGNvbnN0YW50IHNlYXNvbmFsIGFtcGxpdHVkZSk6IGxldmVsIGzigpwgPSDOsSh54oKcIC0gc+KCnOKCi+KCmCkgKyAoMS3OsSkobOKCnOKCi+KCgSArIGLigpzigovigoEpLCBzZWFzb25hbCBz4oKcID0gzrMoeeKCnCAtIGzigpwpICsgKDEtzrMpc+KCnOKCi+KCmCwgZm9yZWNhc3QgxbfigpzigorigpUgPSBs4oKcICsgaMK3YuKCnCArIHPigpzigovigpjigorigpUuIE11bHRpcGxpY2F0aXZlIGZvcm0gKGFtcGxpdHVkZSBzY2FsZXMgd2l0aCBsZXZlbCk6IGZvcmVjYXN0IMW34oKc4oKK4oKVID0gKGzigpwgKyBowrdi4oKcKcK3c+KCnOKCi+KCmOKCiuKClS4gVXNlIGFkZGl0aXZlIHdoZW4gc2Vhc29uYWwgc3dpbmcgaXMgY29uc3RhbnQgb3ZlciB0aW1lOyBtdWx0aXBsaWNhdGl2ZSB3aGVuIHNlYXNvbmFsIHN3aW5nIGdyb3dzIHByb3BvcnRpb25hbGx5IHdpdGggdGhlIGxldmVsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBwYW5kYXMgYXMgcGRcbmZyb20gc3RhdHNtb2RlbHMudHNhLmhvbHR3aW50ZXJzIGltcG9ydCBFeHBvbmVudGlhbFNtb290aGluZ1xuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IG1lYW5fYWJzb2x1dGVfZXJyb3JcblxubnAucmFuZG9tLnNlZWQoMClcbnQgPSBucC5hcmFuZ2UoMTIwKVxueSA9IHBkLlNlcmllcyhcbiAgICA1MCArIDAuMyAqIHQgKyAxMCAqIG5wLnNpbigyICogbnAucGkgKiB0IC8gMTIpICsgbnAucmFuZG9tLnJhbmRuKDEyMCkgKiAyXG4pXG50cmFpbiwgdGVzdCA9IHlbOjk2XSwgeVs5NjpdXG5cbmh3X2FkZCA9IEV4cG9uZW50aWFsU21vb3RoaW5nKFxuICAgIHRyYWluLCB0cmVuZD1cdTAwMjdhZGRcdTAwMjcsIHNlYXNvbmFsPVx1MDAyN2FkZFx1MDAyNywgc2Vhc29uYWxfcGVyaW9kcz0xMlxuKS5maXQob3B0aW1pemVkPVRydWUpXG5cbnNoaWZ0ID0gYWJzKHRyYWluLm1pbigpKSArIDEwXG5od19tdWwgPSBFeHBvbmVudGlhbFNtb290aGluZyhcbiAgICB0cmFpbiArIHNoaWZ0LCB0cmVuZD1cdTAwMjdhZGRcdTAwMjcsIHNlYXNvbmFsPVx1MDAyN211bFx1MDAyNywgc2Vhc29uYWxfcGVyaW9kcz0xMlxuKS5maXQob3B0aW1pemVkPVRydWUpXG5cbmZjc3RfYWRkID0gaHdfYWRkLmZvcmVjYXN0KDI0KVxuZmNzdF9tdWwgPSBod19tdWwuZm9yZWNhc3QoMjQpIC0gc2hpZnRcblxucHJpbnQoZlx1MDAyN0hXIEFkZGl0aXZlICAgIE1BRSA9IHttZWFuX2Fic29sdXRlX2Vycm9yKHRlc3QsIGZjc3RfYWRkKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0hXIE11bHRpcGxpY2F0aXZlIE1BRSA9IHttZWFuX2Fic29sdXRlX2Vycm9yKHRlc3QsIGZjc3RfbXVsKTouM2Z9XHUwMDI3KVxucCA9IGh3X2FkZC5wYXJhbXNcbnByaW50KGZcdTAwMjdhbHBoYT17cFtcInNtb290aGluZ19sZXZlbFwiXTouM2Z9ICBiZXRhPXtwW1wic21vb3RoaW5nX3RyZW5kXCJdOi4zZn0gIGdhbW1hPXtwW1wic21vb3RoaW5nX3NlYXNvbmFsXCJdOi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRVRTIFN0YXRlLVNwYWNlIEZyYW1ld29yayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRVRTIHJlZm9ybXVsYXRlcyBleHBvbmVudGlhbCBzbW9vdGhpbmcgYXMgYSBzdGF0ZS1zcGFjZSBtb2RlbCB3aXRoIGEgc2luZ2xlIHNvdXJjZSBvZiBlcnJvciAoaW5ub3ZhdGlvbnMpLiBFYWNoIGNvbXBvbmVudCDigJQgRXJyb3IgKEUpLCBUcmVuZCAoVCksIFNlYXNvbmFsIChTKSDigJQgY2FuIGJlIE5vbmUgKE4pLCBBZGRpdGl2ZSAoQSksIG9yIE11bHRpcGxpY2F0aXZlIChNKSwgZ2l2aW5nIHVwIHRvIDMwIHZhbGlkIGNvbWJpbmF0aW9ucy4gU0VTID0gRVRTKEEsTixOKSwgSG9sdCBsaW5lYXIgPSBFVFMoQSxBLE4pLCBIb2x0LVdpbnRlcnMgYWRkaXRpdmUgPSBFVFMoQSxBLEEpLiBUaGUgaW5ub3ZhdGlvbnMgZm9ybSBlbmFibGVzIGV4YWN0IGxpa2VsaWhvb2QgY29tcHV0YXRpb24sIHNvIG1vZGVscyBhcmUgY29tcGFyZWQgYnkgQUlDID0gLTLihJMgKyAyaywgd2hlcmUgayBpcyB0aGUgcGFyYW1ldGVyIGNvdW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBwYW5kYXMgYXMgcGRcbmZyb20gc3RhdHNtb2RlbHMudHNhLmV4cG9uZW50aWFsX3Ntb290aGluZy5ldHMgaW1wb3J0IEVUU01vZGVsXG5pbXBvcnQgd2FybmluZ3Ncbndhcm5pbmdzLmZpbHRlcndhcm5pbmdzKFx1MDAyN2lnbm9yZVx1MDAyNylcblxubnAucmFuZG9tLnNlZWQoMSlcbnQgPSBucC5hcmFuZ2UoOTYpXG55ID0gcGQuU2VyaWVzKDUwICsgMC4yICogdCArIDggKiBucC5zaW4oMiAqIG5wLnBpICogdCAvIDEyKSArIG5wLnJhbmRvbS5yYW5kbig5NikpXG5cbmNvbmZpZ3VyYXRpb25zID0gW1xuICAgIChcdTAwMjdFVFMoQSxOLE4pXHUwMDI3LCBkaWN0KGVycm9yPVx1MDAyN2FkZFx1MDAyNywgdHJlbmQ9Tm9uZSwgICBzZWFzb25hbD1Ob25lKSksXG4gICAgKFx1MDAyN0VUUyhBLEEsTilcdTAwMjcsIGRpY3QoZXJyb3I9XHUwMDI3YWRkXHUwMDI3LCB0cmVuZD1cdTAwMjdhZGRcdTAwMjcsICBzZWFzb25hbD1Ob25lKSksXG4gICAgKFx1MDAyN0VUUyhBLEFkLE4pXHUwMDI3LGRpY3QoZXJyb3I9XHUwMDI3YWRkXHUwMDI3LCB0cmVuZD1cdTAwMjdhZGRcdTAwMjcsICBzZWFzb25hbD1Ob25lLCBkYW1wZWRfdHJlbmQ9VHJ1ZSkpLFxuICAgIChcdTAwMjdFVFMoQSxBLEEpXHUwMDI3LCBkaWN0KGVycm9yPVx1MDAyN2FkZFx1MDAyNywgdHJlbmQ9XHUwMDI3YWRkXHUwMDI3LCAgc2Vhc29uYWw9XHUwMDI3YWRkXHUwMDI3KSksXG4gICAgKFx1MDAyN0VUUyhNLEEsTSlcdTAwMjcsIGRpY3QoZXJyb3I9XHUwMDI3bXVsXHUwMDI3LCB0cmVuZD1cdTAwMjdhZGRcdTAwMjcsICBzZWFzb25hbD1cdTAwMjdtdWxcdTAwMjcpKSxcbl1cblxucmVzdWx0cyA9IFtdXG5mb3IgbGFiZWwsIGNmZyBpbiBjb25maWd1cmF0aW9uczpcbiAgICB0cnk6XG4gICAgICAgIG0gPSBFVFNNb2RlbCh5LCBzZWFzb25hbF9wZXJpb2RzPTEyLCAqKmNmZykuZml0KGRpc3A9RmFsc2UpXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKChsYWJlbCwgbS5haWMsIG0uYmljKSlcbiAgICBleGNlcHQgRXhjZXB0aW9uOlxuICAgICAgICBwYXNzXG5cbnJlc3VsdHMuc29ydChrZXk9bGFtYmRhIHg6IHhbMV0pXG5wcmludChmXHUwMDI3e1wiTW9kZWxcIjpcdTAwM2MxNH0ge1wiQUlDXCI6XHUwMDNlOX0ge1wiQklDXCI6XHUwMDNlOX1cdTAwMjcpXG5mb3IgbGFiZWwsIGFpYywgYmljIGluIHJlc3VsdHM6XG4gICAgcHJpbnQoZlx1MDAyN3tsYWJlbDpcdTAwM2MxNH0ge2FpYzpcdTAwM2U5LjJmfSB7YmljOlx1MDAzZTkuMmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0Jlc3QgYnkgQUlDOiB7cmVzdWx0c1swXVswXX1cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJTRVMgPSBBUklNQSgwLDEsMSkiLCJjb250ZW50IjoiU2ltcGxlIEV4cG9uZW50aWFsIFNtb290aGluZyBpcyBhbGdlYnJhaWNhbGx5IGVxdWl2YWxlbnQgdG8gQVJJTUEoMCwxLDEpLiBUaGUgU0VTIGZvcmVjYXN0IMW34oKc4oKK4oKBID0gxbfigpwgLSAoMS3OsSll4oKcIG1hdGNoZXMgdGhlIEFSSU1BKDAsMSwxKSBmb3JlY2FzdCB3aXRoIE1BIGNvZWZmaWNpZW50IM64ID0gLSgxLc6xKS4gSWYgYXV0by1BUklNQSBzZWxlY3RzIEFSSU1BKDAsMSwxKSBmb3IgYSBzZXJpZXMsIFNFUyB3aXRoIM6xID0gMSArIM64IGdpdmVzIGlkZW50aWNhbCBwb2ludCBmb3JlY2FzdHMgaW4gYSBtb3JlIGludGVycHJldGFibGUgcGFyYW1ldGVyaXNhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXJhbWV0ZXIgRXN0aW1hdGlvbiB2aWEgTUxFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYWRkaXRpdmUtZXJyb3IgRVRTIG1vZGVscyB0aGUgY29uY2VudHJhdGVkIGxvZy1saWtlbGlob29kIHNpbXBsaWZpZXMgdG8gbWluaW1pc2luZyDOo2XigpzCsiBvdmVyIHNtb290aGluZyBwYXJhbWV0ZXJzIGFuZCBpbml0aWFsIHN0YXRlcy4gRm9yIG11bHRpcGxpY2F0aXZlLWVycm9yIG1vZGVscyB0aGUgbGlrZWxpaG9vZCBpcyDihJMgPSAtbi8ywrcoMSArIGxuKDLPgCkgKyBsbijOoyhl4oKcL8684oKcKcKyL24pKSwgd2hlcmUgzrzigpwgaXMgdGhlIGNvbmRpdGlvbmFsIG1lYW4uIFN0YXRzbW9kZWxzIHVzZXMgTC1CRkdTLUIgd2l0aCBib3ggY29uc3RyYWludHMgMCBcdTAwM2MgzrEsIM6yLCDOsyBcdTAwM2MgMS4gU2Vhc29uYWwgaW5pdGlhbCBzdGF0ZXMgYXJlIGVzdGltYXRlZCBmcm9tIHRoZSBmaXJzdCAx4oCTMiBjeWNsZXMsIHN1YnN0YW50aWFsbHkgcmVkdWNpbmcgc2Vuc2l0aXZpdHkgdG8gc3RhcnRpbmcgdmFsdWVzIGZvciBuIOKJpSAybS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGb3JlY2FzdCBDb21wYXJpc29uOiBTRVMgdnMgSG9sdCB2cyBIb2x0LVdpbnRlcnMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgcGFuZGFzIGFzIHBkXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5ob2x0d2ludGVycyBpbXBvcnQgRXhwb25lbnRpYWxTbW9vdGhpbmcsIFNpbXBsZUV4cFNtb290aGluZywgSG9sdFxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IG1lYW5fYWJzb2x1dGVfZXJyb3IsIG1lYW5fc3F1YXJlZF9lcnJvclxuXG5ucC5yYW5kb20uc2VlZCg0MilcbnQgPSBucC5hcmFuZ2UoMTQ0KVxueSA9IHBkLlNlcmllcyg0MCArIDAuNSAqIHQgKyAxMiAqIG5wLnNpbigyICogbnAucGkgKiB0IC8gMTIpICsgbnAucmFuZG9tLnJhbmRuKDE0NCkgKiAzKVxudHJhaW4sIHRlc3QgPSB5WzoxMjBdLCB5WzEyMDpdXG5cbm1vZGVscyA9IHtcbiAgICBcdTAwMjdTRVNcdTAwMjc6ICAgIFNpbXBsZUV4cFNtb290aGluZyh0cmFpbikuZml0KG9wdGltaXplZD1UcnVlKSxcbiAgICBcdTAwMjdIb2x0XHUwMDI3OiAgIEhvbHQodHJhaW4sIGRhbXBlZF90cmVuZD1GYWxzZSkuZml0KG9wdGltaXplZD1UcnVlKSxcbiAgICBcdTAwMjdIb2x0LURcdTAwMjc6IEhvbHQodHJhaW4sIGRhbXBlZF90cmVuZD1UcnVlKS5maXQob3B0aW1pemVkPVRydWUpLFxuICAgIFx1MDAyN0hXLUFkZFx1MDAyNzogRXhwb25lbnRpYWxTbW9vdGhpbmcoXG4gICAgICAgIHRyYWluLCB0cmVuZD1cdTAwMjdhZGRcdTAwMjcsIHNlYXNvbmFsPVx1MDAyN2FkZFx1MDAyNywgc2Vhc29uYWxfcGVyaW9kcz0xMikuZml0KCksXG59XG5cbnByaW50KGZcdTAwMjd7XCJNb2RlbFwiOlx1MDAzYzEwfSB7XCJNQUVcIjpcdTAwM2U4fSB7XCJSTVNFXCI6XHUwMDNlOH1cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogMjgpXG5mb3IgbmFtZSwgZml0IGluIG1vZGVscy5pdGVtcygpOlxuICAgIGZjc3QgPSBmaXQuZm9yZWNhc3QoMjQpXG4gICAgbWFlICA9IG1lYW5fYWJzb2x1dGVfZXJyb3IodGVzdCwgZmNzdClcbiAgICBybXNlID0gbnAuc3FydChtZWFuX3NxdWFyZWRfZXJyb3IodGVzdCwgZmNzdCkpXG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lOlx1MDAzYzEwfSB7bWFlOlx1MDAzZTguM2Z9IHtybXNlOlx1MDAzZTguM2Z9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVUUyBNb2RlbCBSZWZlcmVuY2UifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJFVFMgQ29kZSIsIlRyZW5kIiwiU2Vhc29uYWwiLCJGcmVlIFBhcmFtcyIsIkJlc3QgRm9yIl0sInJvd3MiOltbIlNFUyIsIkVUUyhBLE4sTikiLCJOb25lIiwiTm9uZSIsIs6xLCBs4oKAIiwiU3RhdGlvbmFyeSBvciByYW5kb20td2FsayBzZXJpZXMiXSxbIkhvbHQgTGluZWFyIiwiRVRTKEEsQSxOKSIsIkFkZGl0aXZlIiwiTm9uZSIsIs6xLCDOsiwgbOKCgCwgYuKCgCIsIlRyZW5kaW5nIG5vbi1zZWFzb25hbCBzZXJpZXMiXSxbIkhvbHQgRGFtcGVkIiwiRVRTKEEsQWQsTikiLCJEYW1wZWQiLCJOb25lIiwizrEsIM6yLCDPhiwgbOKCgCwgYuKCgCIsIlRyZW5kaW5nLCB1bmNlcnRhaW4gbG9uZyBob3Jpem9uIl0sWyJIVyBBZGRpdGl2ZSIsIkVUUyhBLEEsQSkiLCJBZGRpdGl2ZSIsIkFkZGl0aXZlIiwizrEsIM6yLCDOsyArIG0gaW5pdCIsIlNlYXNvbmFsIHdpdGggY29uc3RhbnQgc3dpbmcgYW1wbGl0dWRlIl0sWyJIVyBNdWx0aXBsaWNhdGl2ZSIsIkVUUyhBLEEsTSkiLCJBZGRpdGl2ZSIsIk11bHRpcGxpY2F0aXZlIiwizrEsIM6yLCDOsyArIG0gaW5pdCIsIlNlYXNvbmFsIHdpdGggZ3Jvd2luZyBzd2luZyBhbXBsaXR1ZGUiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU2VsZWN0IG1vZGVscyB1c2luZyBBSUMsIG5vdCB0cmFpbmluZyBSTVNFIOKAlCBBSUMgcGVuYWxpc2VzIHBhcmFtZXRlciBjb3VudCBhbmQgcHJldmVudHMgb3ZlcmZpdHRpbmcuIiwiRGFtcGVkIHRyZW5kICjPhiDiiYggMC45OCkgZW1waXJpY2FsbHkgb3V0cGVyZm9ybXMgbGluZWFyIHRyZW5kIGZvciBob3Jpem9ucyBoIOKJpSA2LiIsIk11bHRpcGxpY2F0aXZlIHNlYXNvbmFsaXR5IHJlcXVpcmVzIHN0cmljdGx5IHBvc2l0aXZlIHZhbHVlcyDigJQgYWRkIGEgY29uc3RhbnQgb2Zmc2V0IGlmIG5lY2Vzc2FyeS4iLCJGb3IgdmVyeSBzaG9ydCBzZXJpZXMgKG4gXHUwMDNjIDJtKSBmaXggdGhlIHNlYXNvbmFsIHBlcmlvZDsgYXZvaWQgZXN0aW1hdGluZyBpdCBmcm9tIGZld2VyIHRoYW4gdHdvIGZ1bGwgY3ljbGVzLiIsIlRoZSBhdXRvX2FyaW1hIGZ1bmN0aW9uIGZyb20gcG1kYXJpbWEgY2FuIHNlcnZlIGFzIGEgYmFzZWxpbmUgYWxvbmdzaWRlIEVUUyBmb3IgbW9kZWwgc2VsZWN0aW9uLiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV4cG9uZW50aWFsIHNtb290aGluZyByZW1haW5zIGhpZ2hseSBjb21wZXRpdGl2ZSBpbiBwcmFjdGljZS4gVGhlIE0zIGFuZCBNNCBmb3JlY2FzdGluZyBjb21wZXRpdGlvbnMgc2hvd2VkIEVUUyB3aXRoIGRhbXBlZCB0cmVuZCByYW5raW5nIGluIHRoZSB0b3AgdGllciBhY3Jvc3MgdGhvdXNhbmRzIG9mIGhldGVyb2dlbmVvdXMgc2VyaWVzLCBvZnRlbiBvdXRwZXJmb3JtaW5nIGZhciBtb3JlIGNvbXBsZXggTUwgbW9kZWxzLiBUaGUgY29tcGxldGUgcGlwZWxpbmUg4oCUIGRhdGEgaW5nZXN0aW9uLCBFVFMgbW9kZWwgc2VsZWN0aW9uIHZpYSBBSUMsIGFuZCBpbnRlcnZhbCBmb3JlY2FzdCBnZW5lcmF0aW9uIGZyb20gdGhlIGlubm92YXRpb25zIHN0YXRlLXNwYWNlIHJlcHJlc2VudGF0aW9uIOKAlCBjYW4gYmUgZXhwcmVzc2VkIGluIHVuZGVyIHRlbiBsaW5lcyBvZiBzdGF0c21vZGVscyBjb2RlLCBtYWtpbmcgRVRTIHRoZSBkZWZhdWx0IGJhc2VsaW5lIHRvIGJlYXQgYmVmb3JlIGFkZGluZyBjb21wbGV4aXR5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHJlZGljdGlvbiBpbnRlcnZhbHMgZm9yIEVUUyBtb2RlbHMgYXJlIGRlcml2ZWQgYW5hbHl0aWNhbGx5IGZyb20gdGhlIGlubm92YXRpb25zIHZhcmlhbmNlOiBmb3IgaC1zdGVwLWFoZWFkIGZvcmVjYXN0cywgdGhlIGludGVydmFsIHdpZHRoIGdyb3dzIHdpdGggaCB1bmRlciBhZGRpdGl2ZSBlcnJvcnMuIEZvciBtdWx0aXBsaWNhdGl2ZS1lcnJvciBtb2RlbHMsIHNpbXVsYXRpb24tYmFzZWQgaW50ZXJ2YWxzIChkcmF3aW5nIGZyb20gdGhlIGZpdHRlZCBlcnJvciBkaXN0cmlidXRpb24pIGFyZSByZWNvbW1lbmRlZC4gVGhlIGV0cy5zaW11bGF0ZSgpIG1ldGhvZCBpbiBzdGF0c21vZGVscyBkcmF3cyBzYW1wbGUgcGF0aHMgZnJvbSB0aGUgZml0dGVkIHN0YXRlLXNwYWNlIG1vZGVsLCBlbmFibGluZyBlbXBpcmljYWwgY292ZXJhZ2UgYXNzZXNzbWVudCB0aGF0IGRvZXMgbm90IHJlbHkgb24gR2F1c3NpYW4gZXJyb3IgYXNzdW1wdGlvbnMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Exponential Smoothing — Holt-Winters and ETS Models

Exponential smoothing weights recent observations more heavily than distant ones using geometrically decaying weights: the observation k steps back receives weight α(1-α)^k, so the forecast ŷₜ₊₁ = αΣₖ(1-α)^k yₜ₋ₖ is an exponentially weighted average of all past values. The ETS (Error-Trend-Seasonal) state-space framework unifies Simple Exponential Smoothing, Holt linear, and Holt-Winters under a single likelihood, enabling principled selection among 30 model configurations by AIC.

## Simple Exponential Smoothing

SES applies to series with no trend and no seasonality. The update equation ŷₜ₊₁ = αyₜ + (1-α)ŷₜ, with α ∈ (0,1), places weight α on the latest observation and (1-α) on the previous forecast. Expanding recursively yields the weighted average form. Small α (near 0) smooths heavily and reacts slowly; large α (near 1) tracks the series nearly observation-by-observation. The optimal α minimises the sum of squared one-step-ahead forecast errors, solved numerically or by grid search.

```python
import numpy as np
from sklearn.metrics import mean_squared_error

def simple_exp_smoothing(series, alpha):
    """SES from scratch — returns in-sample one-step-ahead fitted values."""
    n = len(series)
    fitted = np.zeros(n)
    fitted[0] = series[0]
    for t in range(1, n):
        fitted[t] = alpha * series[t - 1] + (1 - alpha) * fitted[t - 1]
    return fitted

def optimise_alpha(series):
    """Grid search for alpha minimising in-sample SSE."""
    best_alpha, best_sse = 0.1, np.inf
    for alpha in np.arange(0.05, 1.0, 0.05):
        fitted = simple_exp_smoothing(series, alpha)
        sse = np.sum((series[1:] - fitted[1:]) ** 2)
        if sse < best_sse:
            best_sse, best_alpha = sse, alpha
    return best_alpha

np.random.seed(42)
y = np.cumsum(np.random.randn(120)) + 50
alpha_opt = optimise_alpha(y)
fitted = simple_exp_smoothing(y, alpha_opt)
next_step = alpha_opt * y[-1] + (1 - alpha_opt) * fitted[-1]
rmse = np.sqrt(mean_squared_error(y[1:], fitted[1:]))
print(f'Optimal alpha = {alpha_opt:.2f}')
print(f'In-sample RMSE = {rmse:.4f}')
print(f'One-step-ahead forecast = {next_step:.4f}')
```

## Holt's Linear Method

Holt's linear method adds a trend component bₜ to SES. Level: lₜ = αyₜ + (1-α)(lₜ₋₁ + bₜ₋₁). Trend: bₜ = β(lₜ - lₜ₋₁) + (1-β)bₜ₋₁. h-step forecast: ŷₜ₊ₕ = lₜ + h·bₜ. The damped variant multiplies each trend step by φ ∈ (0,1): ŷₜ₊ₕ = lₜ + (φ + φ² + ... + φʰ)bₜ, preventing linear extrapolation from overshooting on long horizons. Damped trend is empirically the best single method across major forecasting competitions.

## Holt-Winters Seasonal Model

Holt-Winters adds a seasonal component sₜ with period m. Additive form (constant seasonal amplitude): level lₜ = α(yₜ - sₜ₋ₘ) + (1-α)(lₜ₋₁ + bₜ₋₁), seasonal sₜ = γ(yₜ - lₜ) + (1-γ)sₜ₋ₘ, forecast ŷₜ₊ₕ = lₜ + h·bₜ + sₜ₋ₘ₊ₕ. Multiplicative form (amplitude scales with level): forecast ŷₜ₊ₕ = (lₜ + h·bₜ)·sₜ₋ₘ₊ₕ. Use additive when seasonal swing is constant over time; multiplicative when seasonal swing grows proportionally with the level.

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error

np.random.seed(0)
t = np.arange(120)
y = pd.Series(
    50 + 0.3 * t + 10 * np.sin(2 * np.pi * t / 12) + np.random.randn(120) * 2
)
train, test = y[:96], y[96:]

hw_add = ExponentialSmoothing(
    train, trend='add', seasonal='add', seasonal_periods=12
).fit(optimized=True)

shift = abs(train.min()) + 10
hw_mul = ExponentialSmoothing(
    train + shift, trend='add', seasonal='mul', seasonal_periods=12
).fit(optimized=True)

fcst_add = hw_add.forecast(24)
fcst_mul = hw_mul.forecast(24) - shift

print(f'HW Additive    MAE = {mean_absolute_error(test, fcst_add):.3f}')
print(f'HW Multiplicative MAE = {mean_absolute_error(test, fcst_mul):.3f}')
p = hw_add.params
print(f'alpha={p["smoothing_level"]:.3f}  beta={p["smoothing_trend"]:.3f}  gamma={p["smoothing_seasonal"]:.3f}')
```

## ETS State-Space Framework

ETS reformulates exponential smoothing as a state-space model with a single source of error (innovations). Each component — Error (E), Trend (T), Seasonal (S) — can be None (N), Additive (A), or Multiplicative (M), giving up to 30 valid combinations. SES = ETS(A,N,N), Holt linear = ETS(A,A,N), Holt-Winters additive = ETS(A,A,A). The innovations form enables exact likelihood computation, so models are compared by AIC = -2ℓ + 2k, where k is the parameter count.

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.exponential_smoothing.ets import ETSModel
import warnings
warnings.filterwarnings('ignore')

np.random.seed(1)
t = np.arange(96)
y = pd.Series(50 + 0.2 * t + 8 * np.sin(2 * np.pi * t / 12) + np.random.randn(96))

configurations = [
    ('ETS(A,N,N)', dict(error='add', trend=None,   seasonal=None)),
    ('ETS(A,A,N)', dict(error='add', trend='add',  seasonal=None)),
    ('ETS(A,Ad,N)',dict(error='add', trend='add',  seasonal=None, damped_trend=True)),
    ('ETS(A,A,A)', dict(error='add', trend='add',  seasonal='add')),
    ('ETS(M,A,M)', dict(error='mul', trend='add',  seasonal='mul')),
]

results = []
for label, cfg in configurations:
    try:
        m = ETSModel(y, seasonal_periods=12, **cfg).fit(disp=False)
        results.append((label, m.aic, m.bic))
    except Exception:
        pass

results.sort(key=lambda x: x[1])
print(f'{"Model":<14} {"AIC":>9} {"BIC":>9}')
for label, aic, bic in results:
    print(f'{label:<14} {aic:>9.2f} {bic:>9.2f}')
print(f'Best by AIC: {results[0][0]}')
```

> **SES = ARIMA(0,1,1)**: Simple Exponential Smoothing is algebraically equivalent to ARIMA(0,1,1). The SES forecast ŷₜ₊₁ = ŷₜ - (1-α)eₜ matches the ARIMA(0,1,1) forecast with MA coefficient θ = -(1-α). If auto-ARIMA selects ARIMA(0,1,1) for a series, SES with α = 1 + θ gives identical point forecasts in a more interpretable parameterisation.

## Parameter Estimation via MLE

For additive-error ETS models the concentrated log-likelihood simplifies to minimising Σeₜ² over smoothing parameters and initial states. For multiplicative-error models the likelihood is ℓ = -n/2·(1 + ln(2π) + ln(Σ(eₜ/μₜ)²/n)), where μₜ is the conditional mean. Statsmodels uses L-BFGS-B with box constraints 0 < α, β, γ < 1. Seasonal initial states are estimated from the first 1–2 cycles, substantially reducing sensitivity to starting values for n ≥ 2m.

## Forecast Comparison: SES vs Holt vs Holt-Winters

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt
from sklearn.metrics import mean_absolute_error, mean_squared_error

np.random.seed(42)
t = np.arange(144)
y = pd.Series(40 + 0.5 * t + 12 * np.sin(2 * np.pi * t / 12) + np.random.randn(144) * 3)
train, test = y[:120], y[120:]

models = {
    'SES':    SimpleExpSmoothing(train).fit(optimized=True),
    'Holt':   Holt(train, damped_trend=False).fit(optimized=True),
    'Holt-D': Holt(train, damped_trend=True).fit(optimized=True),
    'HW-Add': ExponentialSmoothing(
        train, trend='add', seasonal='add', seasonal_periods=12).fit(),
}

print(f'{"Model":<10} {"MAE":>8} {"RMSE":>8}')
print('-' * 28)
for name, fit in models.items():
    fcst = fit.forecast(24)
    mae  = mean_absolute_error(test, fcst)
    rmse = np.sqrt(mean_squared_error(test, fcst))
    print(f'{name:<10} {mae:>8.3f} {rmse:>8.3f}')
```

## ETS Model Reference

| Model | ETS Code | Trend | Seasonal | Free Params | Best For |
| --- | --- | --- | --- | --- | --- |
| SES | ETS(A,N,N) | None | None | α, l₀ | Stationary or random-walk series |
| Holt Linear | ETS(A,A,N) | Additive | None | α, β, l₀, b₀ | Trending non-seasonal series |
| Holt Damped | ETS(A,Ad,N) | Damped | None | α, β, φ, l₀, b₀ | Trending, uncertain long horizon |
| HW Additive | ETS(A,A,A) | Additive | Additive | α, β, γ + m init | Seasonal with constant swing amplitude |
| HW Multiplicative | ETS(A,A,M) | Additive | Multiplicative | α, β, γ + m init | Seasonal with growing swing amplitude |

- Select models using AIC, not training RMSE — AIC penalises parameter count and prevents overfitting.
- Damped trend (φ ≈ 0.98) empirically outperforms linear trend for horizons h ≥ 6.
- Multiplicative seasonality requires strictly positive values — add a constant offset if necessary.
- For very short series (n < 2m) fix the seasonal period; avoid estimating it from fewer than two full cycles.
- The auto_arima function from pmdarima can serve as a baseline alongside ETS for model selection.

Exponential smoothing remains highly competitive in practice. The M3 and M4 forecasting competitions showed ETS with damped trend ranking in the top tier across thousands of heterogeneous series, often outperforming far more complex ML models. The complete pipeline — data ingestion, ETS model selection via AIC, and interval forecast generation from the innovations state-space representation — can be expressed in under ten lines of statsmodels code, making ETS the default baseline to beat before adding complexity.

Prediction intervals for ETS models are derived analytically from the innovations variance: for h-step-ahead forecasts, the interval width grows with h under additive errors. For multiplicative-error models, simulation-based intervals (drawing from the fitted error distribution) are recommended. The ets.simulate() method in statsmodels draws sample paths from the fitted state-space model, enabling empirical coverage assessment that does not rely on Gaussian error assumptions.

---

