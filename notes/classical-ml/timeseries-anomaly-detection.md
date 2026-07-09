---
title: "Time-Series Anomaly Detection — ARIMA Residuals and LSTM Reconstruction"
slug: "timeseries-anomaly-detection"
description: "Implement time-series anomaly detection using ARIMA residuals for linear stationary processes, STL decomposition for seasonal data, LSTM autoencoders for complex temporal patterns, and point-adjust F1 evaluation with delay tolerance for fair benchmark comparison."
tags: ["anomaly-detection", "density-estimation", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGltZS1zZXJpZXMgYW5vbWFseSBkZXRlY3Rpb24gaXMgaGFyZGVyIHRoYW4gdGFidWxhciBhbm9tYWx5IGRldGVjdGlvbiBiZWNhdXNlIHRoZSB0ZW1wb3JhbCBzdHJ1Y3R1cmUgY3JlYXRlcyBkZXBlbmRlbmNpZXMgYmV0d2VlbiBvYnNlcnZhdGlvbnMuIEEgdmFsdWUgb2YgMTAwIG1heSBiZSBub3JtYWwgYXQgbm9vbiBidXQgYW5vbWFsb3VzIGF0IDNhbS4gTWV0aG9kcyBtdXN0IG1vZGVsIHRoZSBleHBlY3RlZCB0ZW1wb3JhbCBwYXR0ZXJuIGFuZCBmbGFnIGRldmlhdGlvbnMg4oCUIHJlc2lkdWFsLWJhc2VkIGFwcHJvYWNoZXMgKEFSSU1BLCBTVEwpIGZvciBsaW5lYXIgc3RhdGlvbmFyeSBkYXRhLCBhbmQgbmV1cmFsIHJlY29uc3RydWN0aW9uIG1ldGhvZHMgKExTVE0gYXV0b2VuY29kZXIpIGZvciBjb21wbGV4IG5vbi1saW5lYXIgcGF0dGVybnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHlwZXMgb2YgVGVtcG9yYWwgQW5vbWFsaWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaHJlZSBmdW5kYW1lbnRhbCBhbm9tYWx5IHR5cGVzIGFyaXNlIGluIHRpbWUgc2VyaWVzOiAoMSkgUG9pbnQgYW5vbWFsaWVzIOKAlCBhIHNpbmdsZSBvYnNlcnZhdGlvbiBkZXZpYXRlcyBmcm9tIGl0cyBuZWlnaGJvdXJzOyBlYXNpZXN0IHRvIGRldGVjdC4gKDIpIENvbnRleHR1YWwgYW5vbWFsaWVzIOKAlCBhIHZhbHVlIGlzIG5vcm1hbCBnbG9iYWxseSBidXQgYW5vbWFsb3VzIGluIGNvbnRleHQgKGUuZy4sIDE1wrBDIGlzIG5vcm1hbCBpbiBzdW1tZXIgYnV0IGFub21hbG91cyBpbiB3aW50ZXIpLiAoMykgQ29sbGVjdGl2ZSBhbm9tYWxpZXMg4oCUIGEgc3Vic2VxdWVuY2UgaXMgYW5vbWFsb3VzIGV2ZW4gdGhvdWdoIGluZGl2aWR1YWwgdmFsdWVzIGFwcGVhciBub3JtYWwgKGUuZy4sIGEgbWFjaGluZSB2aWJyYXRpbmcgYXQgdGhlIHdyb25nIGZyZXF1ZW5jeSBmb3IgMTAgbWludXRlcykuIEVhY2ggdHlwZSByZXF1aXJlcyBhIGRpZmZlcmVudCBkZXRlY3Rpb24gc3RyYXRlZ3kuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJQb2ludCBhbm9tYWxpZXM6IHVzZSB1bml2YXJpYXRlIHJlc2lkdWFsIHRocmVzaG9sZGluZyAoQVJJTUEsIFNUTCkgb3Igei1zY29yZSBvbiBzbGlkaW5nIHdpbmRvd3MuIiwiQ29udGV4dHVhbCBhbm9tYWxpZXM6IGNvbmRpdGlvbiBvbiB0ZW1wb3JhbCBjb250ZXh0IOKAlCBBUklNQSBjYXB0dXJlcyBsaW5lYXIgY29udGV4dDsgTFNUTSBjYXB0dXJlcyBub24tbGluZWFyIGNvbnRleHQuIiwiQ29sbGVjdGl2ZSBhbm9tYWxpZXM6IGNvbXBhcmUgc3Vic2VxdWVuY2VzIHVzaW5nIHNoYXBlLWJhc2VkIGRpc3RhbmNlcyAoRFRXKSBvciByZWNvbnN0cnVjdGlvbiBlcnJvciBvdmVyIHdpbmRvd3MuIiwiU2Vhc29uYWwgYW5vbWFsaWVzOiBTVEwgZGVjb21wb3NlcyB0cmVuZCArIHNlYXNvbmFsaXR5ICsgcmVzaWR1YWw7IGFub21hbHkgPSBsYXJnZSByZXNpZHVhbCBhZnRlciBzZWFzb25hbCByZW1vdmFsLiIsIlN0cmVhbWluZyB2cyBiYXRjaDogQVJJTUEgY2FuIGJlIHVwZGF0ZWQgb25saW5lOyBMU1RNIHJlcXVpcmVzIG9mZmxpbmUgd2luZG93IHByb2Nlc3NpbmcuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFSSU1BIFJlc2lkdWFsLUJhc2VkIERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQVJJTUEocCxkLHEpIGZpdHMgYSBsaW5lYXIgbW9kZWwgdG8gc3RhdGlvbmFyeSB0aW1lIHNlcmllczogdGhlIEFSKHApIGNvbXBvbmVudCBjYXB0dXJlcyBhdXRvY29ycmVsYXRpb24sIHRoZSBJKGQpIGNvbXBvbmVudCBoYW5kbGVzIG5vbi1zdGF0aW9uYXJpdHkgdmlhIGRpZmZlcmVuY2luZywgYW5kIHRoZSBNQShxKSBjb21wb25lbnQgbW9kZWxzIHRoZSBtb3ZpbmcgYXZlcmFnZSBvZiByZXNpZHVhbHMuIEFmdGVyIGZpdHRpbmcgdG8gbm9ybWFsIGRhdGEsIHRoZSByZXNpZHVhbCBl4oKcID0geOKCnCDiiJIgeMyC4oKcIHNob3VsZCBiZSB3aGl0ZSBub2lzZS4gQW5vbWFsaWVzIHByb2R1Y2UgbGFyZ2UgfGXigpx8LiBUaGUgdGhyZXNob2xkIGlzIHNldCBhdCDOvMKxM8+DIG9mIHRoZSByZXNpZHVhbCBkaXN0cmlidXRpb24uIFRoaXMgYXBwcm9hY2ggaXMgZmFzdCwgaW50ZXJwcmV0YWJsZSwgYW5kIHdvcmtzIHdlbGwgZm9yIHN0YXRpb25hcnkgb3IgbWlsZGx5IG5vbi1zdGF0aW9uYXJ5IHVuaXZhcmlhdGUgc2VyaWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc3RhdHNtb2RlbHMudHNhLmFyaW1hLm1vZGVsIGltcG9ydCBBUklNQVxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IHJvY19hdWNfc2NvcmVcblxubnAucmFuZG9tLnNlZWQoNDIpXG4jIFN5bnRoZXRpYyB0aW1lIHNlcmllczogQVIoMSkgd2l0aCBpbmplY3RlZCBhbm9tYWxpZXNcbm4gPSAzMDBcbnRzID0gbnAuemVyb3MobilcbnRzWzBdID0gMC4wXG5mb3IgdCBpbiByYW5nZSgxLCBuKTpcbiAgICB0c1t0XSA9IDAuNyAqIHRzW3QtMV0gKyBucC5yYW5kb20ucmFuZG4oKVxuYW5vbV9pZHggPSBbODAsIDEzMCwgMjAwLCAyNTBdXG5mb3IgaWR4IGluIGFub21faWR4OlxuICAgIHRzW2lkeF0gKz0gbnAucmFuZG9tLmNob2ljZShbLTEsIDFdKSAqIDYuMFxuXG4jIEZpdCBBUklNQSBvbiBmaXJzdCAyMDAgcG9pbnRzIChub3JtYWwgdHJhaW5pbmcgd2luZG93KVxudHJhaW4sIHRlc3QgPSB0c1s6MjAwXSwgdHNbMjAwOl1cbm1vZGVsID0gQVJJTUEodHJhaW4sIG9yZGVyPSgxLCAwLCAxKSkuZml0KClcbnJlc2lkX3RyYWluID0gbW9kZWwucmVzaWRcbm11X3IsIHNpZ19yID0gcmVzaWRfdHJhaW4ubWVhbigpLCByZXNpZF90cmFpbi5zdGQoKVxuXG4jIFNjb3JlIHRlc3QgcG9pbnRzIHZpYSBvbmUtc3RlcC1haGVhZCBmb3JlY2FzdFxuZm9yZWNhc3RzID0gbW9kZWwuZm9yZWNhc3Qoc3RlcHM9bGVuKHRlc3QpKVxucmVzaWRfdGVzdCA9IG5wLmFicyh0ZXN0IC0gZm9yZWNhc3RzKVxudGhyID0gbXVfciArIDMgKiBzaWdfclxuYWxlcnRzID0gcmVzaWRfdGVzdCBcdTAwM2UgdGhyXG55X3RydWUgPSBucC56ZXJvcyhsZW4odGVzdCkpOyB5X3RydWVbWzAsIDUwXV0gPSAxICAjIGtub3duIGFub20gaW5kaWNlc1xucHJpbnQoZlx1MDAyN0FSSU1BIHJlc2lkdWFsIHRocmVzaG9sZCAoM3NpZ21hKToge3RocjouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0FsZXJ0cyBpbiB0ZXN0IHdpbmRvdzoge2FsZXJ0cy5zdW0oKX1cdTAwMjcpXG5wcmludChmXHUwMDI3UmVzaWR1YWwgbWVhbjoge3Jlc2lkX3Rlc3QubWVhbigpOi40Zn0sIHN0ZDoge3Jlc2lkX3Rlc3Quc3RkKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTVEwgRGVjb21wb3NpdGlvbiBhbmQgUmVzaWR1YWwgVGhyZXNob2xkaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3Igc2Vhc29uYWwgdGltZSBzZXJpZXMsIEFSSU1BIHJlc2lkdWFscyBtYXkgYmUgbGFyZ2UgbWVyZWx5IGR1ZSB0byBzZWFzb25hbCBwYXR0ZXJucyB0aGUgbW9kZWwgZGlkIG5vdCBjYXB0dXJlLiBTVEwgKFNlYXNvbmFsIGFuZCBUcmVuZCBkZWNvbXBvc2l0aW9uIHVzaW5nIExvZXNzKSBkZWNvbXBvc2VzIHjigpwgPSBU4oKcICsgU+KCnCArIFLigpwgd2hlcmUgVOKCnCBpcyB0aGUgdHJlbmQsIFPigpwgaXMgdGhlIHNlYXNvbmFsIGNvbXBvbmVudCwgYW5kIFLigpwgaXMgdGhlIHJlbWFpbmRlci4gQW5vbWFsaWVzIGFwcGVhciBhcyBsYXJnZSBS4oKcLiBTVEwgaXMgcm9idXN0IHRvIG91dGxpZXJzICh1c2VzIGxvY2FsbHkgd2VpZ2h0ZWQgcmVncmVzc2lvbikgYW5kIGhhbmRsZXMgaXJyZWd1bGFyIHNlYXNvbmFsIHBhdHRlcm5zIGJldHRlciB0aGFuIGFkZGl0aXZlIGRlY29tcG9zaXRpb24uIEFmdGVyIHJlbW92aW5nIHRyZW5kIGFuZCBzZWFzb25hbGl0eSwgYXBwbHkgYSByb2xsaW5nIHotc2NvcmUgb3IgSVFSLWJhc2VkIHRocmVzaG9sZCBvbiBS4oKcLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxTVE0gQXV0b2VuY29kZXIgZm9yIFNlcXVlbmNlIEFub21hbHkgRGV0ZWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbiBMU1RNIGF1dG9lbmNvZGVyIGxlYXJucyB0byBjb21wcmVzcyBhbmQgcmVjb25zdHJ1Y3Qgbm9ybWFsIHRpbWUtc2VyaWVzIHdpbmRvd3MuIFRoZSBlbmNvZGVyIExTVE0gbWFwcyBhIHdpbmRvdyBvZiBsZW5ndGggVyB0byBhIGxhdGVudCB2ZWN0b3I7IHRoZSBkZWNvZGVyIExTVE0gcmVjb25zdHJ1Y3RzIHRoZSBvcmlnaW5hbCB3aW5kb3cuIFRyYWluZWQgZXhjbHVzaXZlbHkgb24gbm9ybWFsIHdpbmRvd3MsIHRoZSBtb2RlbCBsZWFybnMgdGVtcG9yYWwgcGF0dGVybnMgc3BlY2lmaWMgdG8gdGhlIG5vcm1hbCByZWdpbWUuIEF0IHRlc3QgdGltZSwgdGhlIHJlY29uc3RydWN0aW9uIGVycm9yIOKAlnjigpw64oKc4oKKVyDiiJIgeMyC4oKcOuKCnOKCilfigJbCsiBpcyBoaWdoIGZvciBhbm9tYWxvdXMgd2luZG93cyBiZWNhdXNlIHRoZSBtb2RlbCBmYWlscyB0byByZWNvbnN0cnVjdCB1bnNlZW4gYWJub3JtYWwgcGF0dGVybnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxuY2xhc3MgTFNUTUF1dG9lbmNvZGVyKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fZmVhdHVyZXM9MSwgaGlkZGVuPTMyLCBuX2xheWVycz0xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IG5uLkxTVE0obl9mZWF0dXJlcywgaGlkZGVuLCBuX2xheWVycywgYmF0Y2hfZmlyc3Q9VHJ1ZSlcbiAgICAgICAgc2VsZi5kZWNvZGVyID0gbm4uTFNUTShoaWRkZW4sIGhpZGRlbiwgbl9sYXllcnMsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYub3V0X3Byb2ogPSBubi5MaW5lYXIoaGlkZGVuLCBuX2ZlYXR1cmVzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgICMgeDogKGJhdGNoLCBzZXFfbGVuLCBmZWF0dXJlcylcbiAgICAgICAgXywgKGgsIGMpID0gc2VsZi5lbmNvZGVyKHgpXG4gICAgICAgICMgUmVwZWF0IGNvbnRleHQgdmVjdG9yIGZvciBkZWNvZGVyXG4gICAgICAgIGRlY19pbnB1dCA9IGhbLTFdLnVuc3F1ZWV6ZSgxKS5yZXBlYXQoMSwgeC5zaXplKDEpLCAxKVxuICAgICAgICBkZWNfb3V0LCBfID0gc2VsZi5kZWNvZGVyKGRlY19pbnB1dClcbiAgICAgICAgcmV0dXJuIHNlbGYub3V0X3Byb2ooZGVjX291dClcblxudG9yY2gubWFudWFsX3NlZWQoMCk7IG5wLnJhbmRvbS5zZWVkKDApXG5XID0gMzAgICMgd2luZG93IHNpemVcbm5wLnJhbmRvbS5zZWVkKDApXG50c19ub3JtID0gbnAuc2luKG5wLmxpbnNwYWNlKDAsIDIwICogbnAucGksIDEwMDApKSArIDAuMSAqIG5wLnJhbmRvbS5yYW5kbigxMDAwKVxud2luZG93cyA9IG5wLmFycmF5KFt0c19ub3JtW2k6aStXXSBmb3IgaSBpbiByYW5nZShsZW4odHNfbm9ybSktVyldKVxuWF93aW4gPSB0b3JjaC50ZW5zb3Iod2luZG93c1s6LCA6LCBOb25lXSwgZHR5cGU9dG9yY2guZmxvYXQzMilcblxuYWVfbHN0bSA9IExTVE1BdXRvZW5jb2RlcihuX2ZlYXR1cmVzPTEsIGhpZGRlbj0zMilcbm9wdF9sc3RtID0gdG9yY2gub3B0aW0uQWRhbShhZV9sc3RtLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbmZvciBlcCBpbiByYW5nZSgyMCk6XG4gICAgcHJlZCA9IGFlX2xzdG0oWF93aW4pXG4gICAgbG9zcyA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MocHJlZCwgWF93aW4pXG4gICAgb3B0X2xzdG0uemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0X2xzdG0uc3RlcCgpXG4gICAgaWYgKGVwKzEpICUgNSA9PSAwOlxuICAgICAgICBwcmludChmXHUwMDI3RXBvY2gge2VwKzE6MmR9IHwgUmVjb24gTVNFOiB7bG9zcy5pdGVtKCk6LjZmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSb2xsaW5nIFdpbmRvdyBSZWNvbnN0cnVjdGlvbiBFcnJvciB3aXRoIFRocmVzaG9sZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXQgdGVzdCB0aW1lLCBjb21wdXRlIHJlY29uc3RydWN0aW9uIGVycm9yIGZvciBldmVyeSByb2xsaW5nIHdpbmRvdyBhbmQgYXNzaWduIHRoZSB3aW5kb3dcdTAwMjdzIGVycm9yIHRvIHRoZSBmaW5hbCB0aW1lc3RlcCBpbiB0aGUgd2luZG93LiBUaGlzIHByb2R1Y2VzIGEgc2NhbGFyIGFub21hbHkgc2NvcmUgZm9yIGVhY2ggdGltZSBzdGVwLiBUaGUgdGhyZXNob2xkIGlzIHRoZSAoMeKIks6xKSBxdWFudGlsZSBvZiByZWNvbnN0cnVjdGlvbiBlcnJvcnMgb24gbm9ybWFsIHdpbmRvd3MuIEEgcHJhY3RpY2FsIHJlZmluZW1lbnQ6IHNtb290aCB0aGUgc2NvcmUgd2l0aCBhIHJvbGxpbmcgbWVkaWFuIHRvIHJlZHVjZSBwb2ludC1hbm9tYWx5IHNlbnNpdGl2aXR5IGFuZCBiZXR0ZXIgY2FwdHVyZSBjb2xsZWN0aXZlIGFub21hbGllcy4gVmlzdWFsaXNpbmcgdGhlIHNjb3JlIGFsb25nc2lkZSB0aGUgcmF3IHRpbWUgc2VyaWVzIGhlbHBzIGlkZW50aWZ5IGFub21hbHkgYm91bmRhcmllcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCByb2NfYXVjX3Njb3JlXG5cbmRlZiByb2xsaW5nX3JlY29uX3Njb3JlKG1vZGVsLCB0c19yYXcsIHdpbmRvdz0zMCk6XG4gICAgbW9kZWwuZXZhbCgpXG4gICAgc2NvcmVzID0gbnAuZnVsbChsZW4odHNfcmF3KSwgbnAubmFuKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4odHNfcmF3KSAtIHdpbmRvdyk6XG4gICAgICAgICAgICB3aW4gPSB0b3JjaC50ZW5zb3IodHNfcmF3W2k6aSt3aW5kb3ddW05vbmUsIDosIE5vbmVdLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgICAgICAgICAgcHJlZCA9IG1vZGVsKHdpbilcbiAgICAgICAgICAgIGVyciA9ICgod2luIC0gcHJlZCkgKiogMikubWVhbigpLml0ZW0oKVxuICAgICAgICAgICAgc2NvcmVzW2kgKyB3aW5kb3cgLSAxXSA9IGVyclxuICAgIHJldHVybiBzY29yZXNcblxubnAucmFuZG9tLnNlZWQoNSlcbiMgVGVzdCBzZXJpZXM6IG1vc3RseSBub3JtYWwgc2luZSArIDMgYW5vbWFseSB3aW5kb3dzXG50c190ZXN0ID0gbnAuc2luKG5wLmxpbnNwYWNlKDAsIDEwKm5wLnBpLCA0MDApKSArIDAuMSpucC5yYW5kb20ucmFuZG4oNDAwKVxudHNfdGVzdFsxNTA6MTY1XSArPSAzLjAgICMgY29sbGVjdGl2ZSBhbm9tYWx5XG50c190ZXN0WzI4MF0gICAgICs9IDUuMCAgIyBwb2ludCBhbm9tYWx5XG50c190ZXN0WzMzMDozNDBdIC09IDIuNSAgIyBjb250ZXh0dWFsIGRpcFxuXG5zY29yZXMgPSByb2xsaW5nX3JlY29uX3Njb3JlKGFlX2xzdG0sIHRzX3Rlc3QsIHdpbmRvdz0zMClcbnZhbGlkID0gfm5wLmlzbmFuKHNjb3JlcylcbnRociA9IG5wLnBlcmNlbnRpbGUoc2NvcmVzW3ZhbGlkXVs6MTAwXSwgOTUpXG5hbGVydHMgPSBzY29yZXNbdmFsaWRdIFx1MDAzZSB0aHJcbnByaW50KGZcdTAwMjdUaHJlc2hvbGQgKDk1dGggcGN0IG9uIGZpcnN0IDEwMCB3aW5kb3dzKToge3RocjouNmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1RvdGFsIGFsZXJ0czoge2FsZXJ0cy5zdW0oKX0gb2Yge3ZhbGlkLnN1bSgpfSBzY29yZWQgdGltZXN0ZXBzXHUwMDI3KVxucHJpbnQoZlx1MDAyN0Fub21hbHkgd2luZG93czogMTUwLTE2NSwgMjgwLCAzMzAtMzQwXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFub21hbHkgRXZhbHVhdGlvbiBNZXRyaWNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQb2ludC1sZXZlbCBwcmVjaXNpb24vcmVjYWxsIGlzIG1pc2xlYWRpbmcgZm9yIHRpbWUtc2VyaWVzOiBhIGRldGVjdG9yIHRoYXQgZmlyZXMgb25lIHN0ZXAgbGF0ZSBmb3IgZXZlcnkgYW5vbWFseSBnZXRzIHplcm8gcmVjYWxsIGJ1dCBoYXMgZGV0ZWN0ZWQgZXZlcnkgZXZlbnQuIFBvaW50LWFkanVzdCBGMSBhZGRyZXNzZXMgdGhpczogaWYgYW55IGFsZXJ0IGZhbGxzIHdpdGhpbiBhbiBhbm9tYWx5IHNlZ21lbnQsIGFsbCB0aW1lc3RlcHMgaW4gdGhhdCBzZWdtZW50IGFyZSBjb3VudGVkIGFzIGRldGVjdGVkLiBGb3JtYWxseTogZm9yIGVhY2ggY29udGlndW91cyBhbm9tYWx5IHNlZ21lbnQsIGlmIGF0IGxlYXN0IG9uZSBwcmVkaWN0aW9uIGluIHRoZSBzZWdtZW50IGlzIDEsIHNldCBhbGwgcHJlZGljdGlvbnMgaW4gdGhlIHNlZ21lbnQgdG8gMSBiZWZvcmUgY29tcHV0aW5nIG1ldHJpY3MuIFRoaXMgbWV0cmljIGFsaWducyBldmFsdWF0aW9uIHdpdGggb3BlcmF0aW9uYWwgcmVxdWlyZW1lbnRzIHdoZXJlIGRldGVjdGluZyBhbiBldmVudCBtYXR0ZXJzIG1vcmUgdGhhbiB0aGUgZXhhY3QgdGltZXN0YW1wLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJFdmFsdWF0aW9uIFByb3RvY29sIGZvciBUaW1lLVNlcmllcyBBbm9tYWx5IERldGVjdGlvbiIsImNvbnRlbnQiOiJBbHdheXMgcmVwb3J0IGJvdGggcG9pbnQtbGV2ZWwgRjEgYW5kIHBvaW50LWFkanVzdCBGMS4gUG9pbnQtYWRqdXN0IHJld2FyZHMgZXZlbnQtbGV2ZWwgZGV0ZWN0aW9uOyBwb2ludC1sZXZlbCByZXdhcmRzIHByZWNpc2UgdGltaW5nLiBVc2UgZGVsYXkgdG9sZXJhbmNlIChtYXhpbXVtIGFjY2VwdGFibGUgZGVsYXkgaW4gc2FtcGxlcykgYXMgYSB0aGlyZCBtZXRyaWMgd2hlbiBlYXJseSBkZXRlY3Rpb24gaXMgY3JpdGljYWwuIEZvciBzdHJlYW1pbmcgc3lzdGVtcywgYWxzbyByZXBvcnQgbGF0ZW5jeTogdGhlIG1lYW4gdGltZSBmcm9tIGV2ZW50IG9uc2V0IHRvIGZpcnN0IGFsZXJ0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBmMV9zY29yZSwgcm9jX2F1Y19zY29yZVxuXG5kZWYgcG9pbnRfYWRqdXN0X2YxKHlfdHJ1ZSwgeV9wcmVkLCBkZWxheV90b2xlcmFuY2U9NSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3UG9pbnQtYWRqdXN0OiBpZiBhbnkgYWxlcnQgd2l0aGluIGFuIGFub21hbHkgc2VnbWVudCwgY3JlZGl0IHRoZSB3aG9sZSBzZWdtZW50Llx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIHlfYWRqID0geV9wcmVkLmNvcHkoKS5hc3R5cGUoaW50KVxuICAgIG4gPSBsZW4oeV90cnVlKVxuICAgIGkgPSAwXG4gICAgd2hpbGUgaSBcdTAwM2MgbjpcbiAgICAgICAgaWYgeV90cnVlW2ldID09IDE6XG4gICAgICAgICAgICAjIEZpbmQgZW5kIG9mIGFub21hbHkgc2VnbWVudFxuICAgICAgICAgICAgaiA9IGlcbiAgICAgICAgICAgIHdoaWxlIGogXHUwMDNjIG4gYW5kIHlfdHJ1ZVtqXSA9PSAxOlxuICAgICAgICAgICAgICAgIGogKz0gMVxuICAgICAgICAgICAgIyBDaGVjayBpZiBhbnkgcHJlZGljdGlvbiBpbiBzZWdtZW50ICh3aXRoIHRvbGVyYW5jZSkgaXMgMVxuICAgICAgICAgICAgc3RhcnQgPSBtYXgoMCwgaSAtIGRlbGF5X3RvbGVyYW5jZSlcbiAgICAgICAgICAgIGVuZCAgID0gbWluKG4sIGogKyBkZWxheV90b2xlcmFuY2UpXG4gICAgICAgICAgICBpZiB5X3ByZWRbc3RhcnQ6ZW5kXS5hbnkoKTpcbiAgICAgICAgICAgICAgICB5X2FkaltpOmpdID0gMSAgIyBjcmVkaXQgZW50aXJlIHNlZ21lbnRcbiAgICAgICAgICAgIGkgPSBqXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICBpICs9IDFcbiAgICBmMV9wdCAgPSBmMV9zY29yZSh5X3RydWUsIHlfcHJlZCwgIHplcm9fZGl2aXNpb249MClcbiAgICBmMV9hZGogPSBmMV9zY29yZSh5X3RydWUsIHlfYWRqLCB6ZXJvX2RpdmlzaW9uPTApXG4gICAgcmV0dXJuIGYxX3B0LCBmMV9hZGpcblxubnAucmFuZG9tLnNlZWQoOClcbnlfdHJ1ZV90cyA9IG5wLnplcm9zKDMwMCwgZHR5cGU9aW50KVxueV90cnVlX3RzWzgwOjk1XSA9IDE7IHlfdHJ1ZV90c1syMDA6MjEwXSA9IDEgICMgdHdvIGFub21hbHkgc2VnbWVudHNcbnlfcHJlZF90cyA9IG5wLnplcm9zKDMwMCwgZHR5cGU9aW50KVxueV9wcmVkX3RzWzg4XSA9IDEgICMgbGF0ZSBkZXRlY3Rpb24gb2YgZmlyc3RcbnlfcHJlZF90c1syMDVdID0gMSAgIyBkZXRlY3Rpb24gaW5zaWRlIHNlY29uZFxuZjFfcCwgZjFfYSA9IHBvaW50X2FkanVzdF9mMSh5X3RydWVfdHMsIHlfcHJlZF90cylcbnByaW50KGZcdTAwMjdQb2ludC1sZXZlbCBGMTogIHtmMV9wOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3UG9pbnQtYWRqdXN0IEYxOiB7ZjFfYTouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3TGF0ZSBkZXRlY3Rpb24gY3JlZGl0ZWQgYnkgcG9pbnQtYWRqdXN0IGJ1dCBub3QgcG9pbnQtbGV2ZWwuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRpbWUtU2VyaWVzIEFub21hbHkgTWV0aG9kIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQXNzdW1wdGlvbiIsIlN0cmVhbWluZyIsIkxhYmVsZWQgRGF0YSBOZWVkZWQiLCJBbm9tYWx5IFR5cGVzIiwiVHJhaW5pbmcgQ29zdCJdLCJyb3dzIjpbWyJBUklNQSByZXNpZHVhbHMiLCJMaW5lYXIsIHN0YXRpb25hcnkgcHJvY2VzcyIsIlllcyAob25saW5lIHVwZGF0ZSkiLCJObyIsIlBvaW50LCBjb250ZXh0dWFsIiwiVmVyeSBsb3cg4oCUIHN0YXRzbW9kZWxzIl0sWyJTVEwgKyB0aHJlc2hvbGQiLCJBZGRpdGl2ZSB0cmVuZCtzZWFzb24rbm9pc2UiLCJObyAoYmF0Y2gpIiwiTm8iLCJQb2ludCwgc2Vhc29uYWwiLCJMb3cg4oCUIExvZXNzIHJlZ3Jlc3Npb24iXSxbIkxTVE0gcmVjb25zdHJ1Y3Rpb24iLCJOb24tbGluZWFyIHRlbXBvcmFsIHBhdHRlcm5zIiwiTm8gKHdpbmRvd2VkKSIsIk5vIChzZWxmLXN1cGVydmlzZWQpIiwiUG9pbnQsIGNvbGxlY3RpdmUiLCJIaWdoIOKAlCBHUFUgdHJhaW5pbmciXSxbIk9uZS1jbGFzcyBMU1RNIChwcmVkaWN0aW9uKSIsIk5vbi1saW5lYXIsIHByZWRpY3RhYmxlIiwiWWVzIChhdXRvcmVncmVzc2l2ZSkiLCJObyIsIlBvaW50LCBjb250ZXh0dWFsIiwiSGlnaCDigJQgR1BVIHRyYWluaW5nIl0sWyJJc29sYXRpb24gRm9yZXN0IG9uIHdpbmRvd3MiLCJJSUQgd2l0aGluIHdpbmRvd3MiLCJObyIsIk5vIiwiUG9pbnQsIGNvbGxlY3RpdmUiLCJNZWRpdW0g4oCUIHRyZWUgZW5zZW1ibGUiXV19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIHByb2R1Y3Rpb24gdGltZS1zZXJpZXMgYW5vbWFseSBkZXRlY3Rpb246IHVzZSBBUklNQSBhcyBhIGZhc3QgYmFzZWxpbmUg4oCUIGl0IG9mdGVuIGhhbmRsZXMgS1BJIG1vbml0b3JpbmcgKENQVSwgbGF0ZW5jeSkgd2VsbCBiZWNhdXNlIHRoZXNlIHNlcmllcyBhcmUgbmVhcmx5IHN0YXRpb25hcnkgd2l0aGluIHNsaWRpbmcgd2luZG93cy4gVXNlIExTVE0gYXV0b2VuY29kZXIgd2hlbiB0aGUgc2VyaWVzIGhhcyBjb21wbGV4IG5vbi1saW5lYXIgcGF0dGVybnMgKHNlbnNvciBmdXNpb24sIG11bHRpLXZhcmlhdGUpIGFuZCB5b3UgaGF2ZSBlbm91Z2ggY2xlYW4gdHJhaW5pbmcgZGF0YSAoXHUwMDNlMTBLIHRpbWVzdGVwcykuIENvbWJpbmUgYm90aDogQVJJTUEgZm9yIGZhc3Qgb25saW5lIHNjb3JpbmcsIExTVE0gZm9yIG9mZmxpbmUgZGVlcCBhbmFseXNpcyBvZiBmbGFnZ2VkIHdpbmRvd3MuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Time-Series Anomaly Detection — ARIMA Residuals and LSTM Reconstruction

Time-series anomaly detection is harder than tabular anomaly detection because the temporal structure creates dependencies between observations. A value of 100 may be normal at noon but anomalous at 3am. Methods must model the expected temporal pattern and flag deviations — residual-based approaches (ARIMA, STL) for linear stationary data, and neural reconstruction methods (LSTM autoencoder) for complex non-linear patterns.

## Types of Temporal Anomalies

Three fundamental anomaly types arise in time series: (1) Point anomalies — a single observation deviates from its neighbours; easiest to detect. (2) Contextual anomalies — a value is normal globally but anomalous in context (e.g., 15°C is normal in summer but anomalous in winter). (3) Collective anomalies — a subsequence is anomalous even though individual values appear normal (e.g., a machine vibrating at the wrong frequency for 10 minutes). Each type requires a different detection strategy.

- Point anomalies: use univariate residual thresholding (ARIMA, STL) or z-score on sliding windows.
- Contextual anomalies: condition on temporal context — ARIMA captures linear context; LSTM captures non-linear context.
- Collective anomalies: compare subsequences using shape-based distances (DTW) or reconstruction error over windows.
- Seasonal anomalies: STL decomposes trend + seasonality + residual; anomaly = large residual after seasonal removal.
- Streaming vs batch: ARIMA can be updated online; LSTM requires offline window processing.

## ARIMA Residual-Based Detection

ARIMA(p,d,q) fits a linear model to stationary time series: the AR(p) component captures autocorrelation, the I(d) component handles non-stationarity via differencing, and the MA(q) component models the moving average of residuals. After fitting to normal data, the residual eₜ = xₜ − x̂ₜ should be white noise. Anomalies produce large |eₜ|. The threshold is set at μ±3σ of the residual distribution. This approach is fast, interpretable, and works well for stationary or mildly non-stationary univariate series.

```python
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import roc_auc_score

np.random.seed(42)
# Synthetic time series: AR(1) with injected anomalies
n = 300
ts = np.zeros(n)
ts[0] = 0.0
for t in range(1, n):
    ts[t] = 0.7 * ts[t-1] + np.random.randn()
anom_idx = [80, 130, 200, 250]
for idx in anom_idx:
    ts[idx] += np.random.choice([-1, 1]) * 6.0

# Fit ARIMA on first 200 points (normal training window)
train, test = ts[:200], ts[200:]
model = ARIMA(train, order=(1, 0, 1)).fit()
resid_train = model.resid
mu_r, sig_r = resid_train.mean(), resid_train.std()

# Score test points via one-step-ahead forecast
forecasts = model.forecast(steps=len(test))
resid_test = np.abs(test - forecasts)
thr = mu_r + 3 * sig_r
alerts = resid_test > thr
y_true = np.zeros(len(test)); y_true[[0, 50]] = 1  # known anom indices
print(f'ARIMA residual threshold (3sigma): {thr:.4f}')
print(f'Alerts in test window: {alerts.sum()}')
print(f'Residual mean: {resid_test.mean():.4f}, std: {resid_test.std():.4f}')
```

## STL Decomposition and Residual Thresholding

For seasonal time series, ARIMA residuals may be large merely due to seasonal patterns the model did not capture. STL (Seasonal and Trend decomposition using Loess) decomposes xₜ = Tₜ + Sₜ + Rₜ where Tₜ is the trend, Sₜ is the seasonal component, and Rₜ is the remainder. Anomalies appear as large Rₜ. STL is robust to outliers (uses locally weighted regression) and handles irregular seasonal patterns better than additive decomposition. After removing trend and seasonality, apply a rolling z-score or IQR-based threshold on Rₜ.

## LSTM Autoencoder for Sequence Anomaly Detection

An LSTM autoencoder learns to compress and reconstruct normal time-series windows. The encoder LSTM maps a window of length W to a latent vector; the decoder LSTM reconstructs the original window. Trained exclusively on normal windows, the model learns temporal patterns specific to the normal regime. At test time, the reconstruction error ‖xₜ:ₜ₊W − x̂ₜ:ₜ₊W‖² is high for anomalous windows because the model fails to reconstruct unseen abnormal patterns.

```python
import torch
import torch.nn as nn
import numpy as np

class LSTMAutoencoder(nn.Module):
    def __init__(self, n_features=1, hidden=32, n_layers=1):
        super().__init__()
        self.encoder = nn.LSTM(n_features, hidden, n_layers, batch_first=True)
        self.decoder = nn.LSTM(hidden, hidden, n_layers, batch_first=True)
        self.out_proj = nn.Linear(hidden, n_features)

    def forward(self, x):
        # x: (batch, seq_len, features)
        _, (h, c) = self.encoder(x)
        # Repeat context vector for decoder
        dec_input = h[-1].unsqueeze(1).repeat(1, x.size(1), 1)
        dec_out, _ = self.decoder(dec_input)
        return self.out_proj(dec_out)

torch.manual_seed(0); np.random.seed(0)
W = 30  # window size
np.random.seed(0)
ts_norm = np.sin(np.linspace(0, 20 * np.pi, 1000)) + 0.1 * np.random.randn(1000)
windows = np.array([ts_norm[i:i+W] for i in range(len(ts_norm)-W)])
X_win = torch.tensor(windows[:, :, None], dtype=torch.float32)

ae_lstm = LSTMAutoencoder(n_features=1, hidden=32)
opt_lstm = torch.optim.Adam(ae_lstm.parameters(), lr=1e-3)
for ep in range(20):
    pred = ae_lstm(X_win)
    loss = nn.functional.mse_loss(pred, X_win)
    opt_lstm.zero_grad(); loss.backward(); opt_lstm.step()
    if (ep+1) % 5 == 0:
        print(f'Epoch {ep+1:2d} | Recon MSE: {loss.item():.6f}')
```

## Rolling Window Reconstruction Error with Threshold

At test time, compute reconstruction error for every rolling window and assign the window's error to the final timestep in the window. This produces a scalar anomaly score for each time step. The threshold is the (1−α) quantile of reconstruction errors on normal windows. A practical refinement: smooth the score with a rolling median to reduce point-anomaly sensitivity and better capture collective anomalies. Visualising the score alongside the raw time series helps identify anomaly boundaries.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score

def rolling_recon_score(model, ts_raw, window=30):
    model.eval()
    scores = np.full(len(ts_raw), np.nan)
    with torch.no_grad():
        for i in range(len(ts_raw) - window):
            win = torch.tensor(ts_raw[i:i+window][None, :, None], dtype=torch.float32)
            pred = model(win)
            err = ((win - pred) ** 2).mean().item()
            scores[i + window - 1] = err
    return scores

np.random.seed(5)
# Test series: mostly normal sine + 3 anomaly windows
ts_test = np.sin(np.linspace(0, 10*np.pi, 400)) + 0.1*np.random.randn(400)
ts_test[150:165] += 3.0  # collective anomaly
ts_test[280]     += 5.0  # point anomaly
ts_test[330:340] -= 2.5  # contextual dip

scores = rolling_recon_score(ae_lstm, ts_test, window=30)
valid = ~np.isnan(scores)
thr = np.percentile(scores[valid][:100], 95)
alerts = scores[valid] > thr
print(f'Threshold (95th pct on first 100 windows): {thr:.6f}')
print(f'Total alerts: {alerts.sum()} of {valid.sum()} scored timesteps')
print(f'Anomaly windows: 150-165, 280, 330-340')
```

## Anomaly Evaluation Metrics

Point-level precision/recall is misleading for time-series: a detector that fires one step late for every anomaly gets zero recall but has detected every event. Point-adjust F1 addresses this: if any alert falls within an anomaly segment, all timesteps in that segment are counted as detected. Formally: for each contiguous anomaly segment, if at least one prediction in the segment is 1, set all predictions in the segment to 1 before computing metrics. This metric aligns evaluation with operational requirements where detecting an event matters more than the exact timestamp.

> **Evaluation Protocol for Time-Series Anomaly Detection**: Always report both point-level F1 and point-adjust F1. Point-adjust rewards event-level detection; point-level rewards precise timing. Use delay tolerance (maximum acceptable delay in samples) as a third metric when early detection is critical. For streaming systems, also report latency: the mean time from event onset to first alert.

```python
import numpy as np
from sklearn.metrics import f1_score, roc_auc_score

def point_adjust_f1(y_true, y_pred, delay_tolerance=5):
    '''Point-adjust: if any alert within an anomaly segment, credit the whole segment.'''
    y_adj = y_pred.copy().astype(int)
    n = len(y_true)
    i = 0
    while i < n:
        if y_true[i] == 1:
            # Find end of anomaly segment
            j = i
            while j < n and y_true[j] == 1:
                j += 1
            # Check if any prediction in segment (with tolerance) is 1
            start = max(0, i - delay_tolerance)
            end   = min(n, j + delay_tolerance)
            if y_pred[start:end].any():
                y_adj[i:j] = 1  # credit entire segment
            i = j
        else:
            i += 1
    f1_pt  = f1_score(y_true, y_pred,  zero_division=0)
    f1_adj = f1_score(y_true, y_adj, zero_division=0)
    return f1_pt, f1_adj

np.random.seed(8)
y_true_ts = np.zeros(300, dtype=int)
y_true_ts[80:95] = 1; y_true_ts[200:210] = 1  # two anomaly segments
y_pred_ts = np.zeros(300, dtype=int)
y_pred_ts[88] = 1  # late detection of first
y_pred_ts[205] = 1  # detection inside second
f1_p, f1_a = point_adjust_f1(y_true_ts, y_pred_ts)
print(f'Point-level F1:  {f1_p:.4f}')
print(f'Point-adjust F1: {f1_a:.4f}')
print('Late detection credited by point-adjust but not point-level.')
```

## Time-Series Anomaly Method Comparison

| Method | Assumption | Streaming | Labeled Data Needed | Anomaly Types | Training Cost |
| --- | --- | --- | --- | --- | --- |
| ARIMA residuals | Linear, stationary process | Yes (online update) | No | Point, contextual | Very low — statsmodels |
| STL + threshold | Additive trend+season+noise | No (batch) | No | Point, seasonal | Low — Loess regression |
| LSTM reconstruction | Non-linear temporal patterns | No (windowed) | No (self-supervised) | Point, collective | High — GPU training |
| One-class LSTM (prediction) | Non-linear, predictable | Yes (autoregressive) | No | Point, contextual | High — GPU training |
| Isolation Forest on windows | IID within windows | No | No | Point, collective | Medium — tree ensemble |

For production time-series anomaly detection: use ARIMA as a fast baseline — it often handles KPI monitoring (CPU, latency) well because these series are nearly stationary within sliding windows. Use LSTM autoencoder when the series has complex non-linear patterns (sensor fusion, multi-variate) and you have enough clean training data (>10K timesteps). Combine both: ARIMA for fast online scoring, LSTM for offline deep analysis of flagged windows.

---

