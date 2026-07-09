---
title: "SARIMA — Seasonal ARIMA and Period Selection"
slug: "sarima"
description: "Extend ARIMA with seasonal AR, I, and MA operators at period S, learn to identify seasonal orders from ACF/PACF spikes at seasonal lags, select S via periodogram and domain knowledge, and grid-search SARIMA orders by AIC."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU0FSSU1BIOKAlCBTZWFzb25hbCBBUklNQSDigJQgZXh0ZW5kcyB0aGUgQm94LUplbmtpbnMgZnJhbWV3b3JrIHRvIHNlcmllcyB3aXRoIHBlcmlvZGljIGJlaGF2aW91ci4gTW9udGhseSByZXRhaWwgc2FsZXMsIHF1YXJ0ZXJseSBHRFAsIGRhaWx5IHRlbXBlcmF0dXJlLCBhbmQgd2Vla2x5IHdlYiB0cmFmZmljIGFsbCBleGhpYml0IHJlZ3VsYXIgcGF0dGVybnMgdGhhdCByZXBlYXQgYXQgYSBrbm93biBwZXJpb2QgUy4gVGhlIFNBUklNQSBtb2RlbCBhZGRzIHNlYXNvbmFsIEFSLCBJIChkaWZmZXJlbmNpbmcpLCBhbmQgTUEgb3BlcmF0b3JzIHRoYXQgYWN0IGF0IG11bHRpcGxlcyBvZiBTLCBhbGxvd2luZyB0aGUgbW9kZWwgdG8gY2FwdHVyZSBib3RoIHRoZSBzaG9ydC1ydW4gYXV0b2NvcnJlbGF0aW9uIHN0cnVjdHVyZSBhbmQgdGhlIGxvbmctcnVuIHNlYXNvbmFsIGRlcGVuZGVuY2llcyBzaW11bHRhbmVvdXNseS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTQVJJTUEgTm90YXRpb24gYW5kIEJhY2tzaGlmdCBPcGVyYXRvcnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNBUklNQShwLGQscSkoUCxELFEpW1NdIGlzIHdyaXR0ZW4gaW4gb3BlcmF0b3IgZm9ybSBhcyDOpuKCmihCKcK3z4ZfUChCy6IpwrcoMeKIkkIp4bWIwrcoMeKIkkLLoinhtLDCt3nigpwgPSDOmHEoQinCt864X1EoQsuiKcK3zrXigpwsIHdoZXJlIM+GX1AoQsuiKSA9IDEg4oiSIM6m4oKBQsuiIOKIkiDigKYg4oiSIM6mX1BCXihQUykgaXMgdGhlIHNlYXNvbmFsIEFSIHBvbHlub21pYWwsIM64X1EoQsuiKSBpcyB0aGUgc2Vhc29uYWwgTUEgcG9seW5vbWlhbCwgKDHiiJJCy6Ip4bSwIGFwcGxpZXMgRCBzZWFzb25hbCBkaWZmZXJlbmNlcywgYW5kICgx4oiSQinhtYggYXBwbGllcyBkIHJlZ3VsYXIgZGlmZmVyZW5jZXMuIFRoZSBub24tc2Vhc29uYWwgKHAsZCxxKSBwYXJ0IGFuZCB0aGUgc2Vhc29uYWwgKFAsRCxRKVtTXSBwYXJ0IG11bHRpcGx5IHRvZ2V0aGVyIHRvIGZvcm0gdGhlIGZ1bGwgbW9kZWwg4oCUIHRoZSB0b3RhbCBudW1iZXIgb2YgQVIgYW5kIE1BIHBhcmFtZXRlcnMgaXMgcCArIFAuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGNvbW1vbiBwcmFjdGljYWwgbW9kZWwgZm9yIG1vbnRobHkgZGF0YSBpcyBTQVJJTUEoMSwxLDEpKDEsMSwxKVsxMl0g4oCUIHRoZSBhaXJsaW5lIG1vZGVsIOKAlCBwb3B1bGFyaXNlZCBieSBCb3ggYW5kIEplbmtpbnMgaW4gdGhlaXIgYW5hbHlzaXMgb2YgdGhlIGludGVybmF0aW9uYWwgYWlybGluZSBwYXNzZW5nZXIgZGF0YXNldC4gSXQgaGFzOiBvbmUgcmVndWxhciBBUiBsYWcsIG9uZSBzZWFzb25hbCBBUiBsYWcgYXQgbGFnIDEyLCBvbmUgcmVndWxhciBNQSBlcnJvciwgb25lIHNlYXNvbmFsIE1BIGVycm9yIGF0IGxhZyAxMiwgb25lIHJlZ3VsYXIgZGlmZmVyZW5jZSwgYW5kIG9uZSBzZWFzb25hbCBkaWZmZXJlbmNlLiBEZXNwaXRlIGhhdmluZyBvbmx5IDQgZnJlZSBwYXJhbWV0ZXJzIHBsdXMgc2lnbWHCsiwgaXQgY2FwdHVyZXMgdGhlIGRvbWluYW50IHN0cnVjdHVyZSBvZiBtYW55IG1vbnRobHkgZWNvbm9taWMgc2VyaWVzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVGhlIHNlYXNvbmFsIEFSIHBvbHlub21pYWwgz4ZfUChCy6IpID0gMSDiiJIgzqbigoFCy6Ig4oiSIOKApiDiiJIgzqZfUEJee1BTfSBvcGVyYXRlcyBhdCBtdWx0aXBsZXMgb2YgUyAobGFncyBTLCAyUywg4oCmKS4iLCJUaGUgc2Vhc29uYWwgTUEgcG9seW5vbWlhbCDOuF9RKELLoikgYWRkcyBzbW9vdGhpbmcgb2YgcGFzdCBzZWFzb25hbCBlcnJvcnMg4oCUIHNhbWUgZnJlcXVlbmN5IHN0cnVjdHVyZSBhcyBzZWFzb25hbCBBUi4iLCJTZWFzb25hbCBkaWZmZXJlbmNpbmcgKDEg4oiSIELLoinhtLAgYW5kIHJlZ3VsYXIgZGlmZmVyZW5jaW5nICgxIOKIkiBCKeG1iCBhcmUgYXBwbGllZCBiZWZvcmUgdGhlIEFSTUEgZml0dGluZy4iLCJUb3RhbCBwYXJhbWV0ZXJzOiBwICsgUCBBUiBjb2VmZmljaWVudHMsIHEgKyBRIE1BIGNvZWZmaWNpZW50cywgcGx1cyBzaWdtYcKyIOKAlCB0eXBpY2FsbHkgNOKAkzggcGFyYW1ldGVycyBmb3IgY29tbW9uIHNlYXNvbmFsIG1vZGVscy4iLCJTdGF0aW9uYXJpdHkgcmVxdWlyZXMgYWxsIHJvb3RzIG9mIM+GX3AoeinCt8+GX1AoesuiKSB0byBsaWUgb3V0c2lkZSB0aGUgdW5pdCBjaXJjbGU7IGludmVydGliaWxpdHkgcmVxdWlyZXMgdGhlIHNhbWUgZm9yIM64X3EoeinCt864X1EoesuiKS4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2xhc3NpYyBFeGFtcGxlIOKAlCBBaXJsaW5lIFBhc3NlbmdlcnMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgcGFuZGFzIGFzIHBkXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0ZXNwYWNlLnNhcmltYXggaW1wb3J0IFNBUklNQVhcbmZyb20gc3RhdHNtb2RlbHMuZGF0YXNldHMgaW1wb3J0IGdldF9yZGF0YXNldFxuXG4jIExvYWQgY2xhc3NpYyBhaXJsaW5lIHBhc3NlbmdlcnMgZGF0YXNldFxuZGF0YSA9IGdldF9yZGF0YXNldChcdTAwMjdBaXJQYXNzZW5nZXJzXHUwMDI3LCBcdTAwMjdkYXRhc2V0c1x1MDAyNylcbnkgPSBucC5sb2coZGF0YS5kYXRhW1x1MDAyN3ZhbHVlXHUwMDI3XS52YWx1ZXMpICAjIGxvZy10cmFuc2Zvcm0gZm9yIGFkZGl0aXZlIHRyZWF0bWVudFxubiA9IGxlbih5KVxudHJhaW4sIHRlc3QgPSB5WzoxMjBdLCB5WzEyMDpdICAjIDEzMiBtb250aHM6IHVzZSAxMjAgZm9yIHRyYWluaW5nXG5cbiMgRml0IFNBUklNQSgxLDEsMSkoMSwxLDEpWzEyXSAtLSB0aGUgY2xhc3NpYyBhaXJsaW5lIG1vZGVsXG5tb2RlbCA9IFNBUklNQVgodHJhaW4sIG9yZGVyPSgxLCAxLCAxKSwgc2Vhc29uYWxfb3JkZXI9KDEsIDEsIDEsIDEyKSxcbiAgICAgICAgICAgICAgICB0cmVuZD1cdTAwMjduXHUwMDI3LCBlbmZvcmNlX3N0YXRpb25hcml0eT1UcnVlLCBlbmZvcmNlX2ludmVydGliaWxpdHk9VHJ1ZSlcbmZpdCA9IG1vZGVsLmZpdChkaXNwPUZhbHNlKVxuXG5wcmludChcIlNBUklNQSgxLDEsMSkoMSwxLDEpWzEyXSAtLSBBaXJsaW5lIFBhc3NlbmdlcnMgKGxvZyBzY2FsZSlcIilcbnByaW50KGZcIiAgQVIgcGhpMSAgID0ge2ZpdC5wYXJhbXNbXHUwMDI3YXIuTDFcdTAwMjddOi40Zn1cIilcbnByaW50KGZcIiAgTUEgdGhldGExID0ge2ZpdC5wYXJhbXNbXHUwMDI3bWEuTDFcdTAwMjddOi40Zn1cIilcbnByaW50KGZcIiAgU0FSIFBoaTEgID0ge2ZpdC5wYXJhbXNbXHUwMDI3YXIuUy5MMTJcdTAwMjddOi40Zn1cIilcbnByaW50KGZcIiAgU01BIFRoZXRhMT0ge2ZpdC5wYXJhbXNbXHUwMDI3bWEuUy5MMTJcdTAwMjddOi40Zn1cIilcbnByaW50KGZcIiAgQUlDICAgICAgID0ge2ZpdC5haWM6LjJmfVwiKVxuXG4jIEZvcmVjYXN0IHJlbWFpbmluZyAxMiBtb250aHNcbmZjID0gZml0LmdldF9mb3JlY2FzdChzdGVwcz0xMilcbmZlYXRfZXhwID0gbnAuZXhwKGZjLnByZWRpY3RlZF9tZWFuKVxudGVzdF9leHAgID0gbnAuZXhwKHRlc3QpXG5tYXBlID0gbnAubWVhbihucC5hYnMoKHRlc3RfZXhwIC0gZmVhdF9leHApIC8gdGVzdF9leHApKSAqIDEwMFxucHJpbnQoZlwiICBUZXN0IE1BUEUgKGxhc3QgMTIgbW9udGhzKSA9IHttYXBlOi4yZn0lXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2Vhc29uYWwgRGlmZmVyZW5jaW5nIGFuZCBBQ0YgSWRlbnRpZmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNlYXNvbmFsIGRpZmZlcmVuY2luZyDOlOKCm1nigpwgPSBZ4oKcIOKIkiBZ4oKc4oKL4oKbIHJlbW92ZXMgYSBzZWFzb25hbCB1bml0IHJvb3QgKGEgdW5pdCByb290IGF0IHRoZSBzZWFzb25hbCBmcmVxdWVuY3kpLiBBZnRlciBEID0gMSBzZWFzb25hbCBkaWZmZXJlbmNlLCB0aGUgc2Vhc29uYWwgc3Bpa2VzIGluIHRoZSBBQ0Ygc2hvdWxkIGRpbWluaXNoLiBJZiB0aGV5IHJlbWFpbiwgY29uc2lkZXIgRCA9IDEgcmVndWxhciBkaWZmZXJlbmNlIGFkZGl0aW9uYWxseS4gVGhlIHNlYXNvbmFsIEFDRiBvZiB0aGUgZG91Ymx5LWRpZmZlcmVuY2VkIHNlcmllcyB0aGVuIHNob3dzIHRoZSByZXNpZHVhbCBzZWFzb25hbCBBUi9NQSBzdHJ1Y3R1cmUuIE92ZXJseSBhZ2dyZXNzaXZlIGRpZmZlcmVuY2luZyAoRCBcdTAwM2UgMSkgaXMgcmFyZWx5IGp1c3RpZmllZCBhbmQgb3Zlci1jb21wbGljYXRlcyB0aGUgbW9kZWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzdGF0c21vZGVscy50c2Euc3RhdHRvb2xzIGltcG9ydCBhY2ZcbmZyb20gc3RhdHNtb2RlbHMuZGF0YXNldHMgaW1wb3J0IGdldF9yZGF0YXNldFxuXG5kYXRhID0gZ2V0X3JkYXRhc2V0KFx1MDAyN0FpclBhc3NlbmdlcnNcdTAwMjcsIFx1MDAyN2RhdGFzZXRzXHUwMDI3KVxueV9sb2cgPSBucC5sb2coZGF0YS5kYXRhW1x1MDAyN3ZhbHVlXHUwMDI3XS52YWx1ZXMpXG5cbiMgUmVndWxhciBkaWZmZXJlbmNlXG55X2QxID0gbnAuZGlmZih5X2xvZylcblxuIyBTZWFzb25hbCBkaWZmZXJlbmNlIG9mIHJlZ3VsYXItZGlmZmVyZW5jZWQgc2VyaWVzXG55X2QxX0QxID0gbnAuZGlmZih5X2QxLCBuPTEyKVxuXG5jaSA9IDEuOTYgLyBucC5zcXJ0KGxlbih5X2QxX0QxKSlcbmFjZl9kMV9EMSA9IGFjZih5X2QxX0QxLCBubGFncz0yNClcblxucHJpbnQoZlwiQWZ0ZXIgKDEsMSwxKSBkaWZmZXJlbmNpbmc6IG49e2xlbih5X2QxX0QxKX0sIENJPSsvLXtjaTouNGZ9XCIpXG5wcmludCgpXG5wcmludChmXCJ7XHUwMDI3TGFnXHUwMDI3Olx1MDAzZTRzfSAge1x1MDAyN0FDRlx1MDAyNzpcdTAwM2U3c30gIHtcdTAwMjdTaWc/XHUwMDI3Olx1MDAzZTZzfVwiKVxucHJpbnQoXCItXCIgKiAyNClcbmZvciBrIGluIFsxLCAyLCAzLCAxMiwgMTMsIDI0XTpcbiAgICBzaWcgPSBcIllFU1wiIGlmIGFicyhhY2ZfZDFfRDFba10pIFx1MDAzZSBjaSBlbHNlIFwibm9cIlxuICAgIHByaW50KGZcIntrOjRkfSAge2FjZl9kMV9EMVtrXTo3LjRmfSAge3NpZzpcdTAwM2U2c31cIilcbnByaW50KFwiXFxuU3Bpa2UgYXQgbGFnIDEgPVx1MDAzZSBNQSgxKTsgc3Bpa2UgYXQgbGFnIDEyID1cdTAwM2UgU01BKDEpIC0tIGNvbnNpc3RlbnQgd2l0aCBhaXJsaW5lIG1vZGVsXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hvb3NpbmcgdGhlIFNlYXNvbmFsIFBlcmlvZCBTIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2Vhc29uYWwgcGVyaW9kIFMgbXVzdCBiZSBrbm93biBvciBlc3RpbWF0ZWQgYmVmb3JlIGZpdHRpbmcgU0FSSU1BLiBJbiBtb3N0IGNhc2VzIFMgaXMgZGV0ZXJtaW5lZCBieSBkb21haW4ga25vd2xlZGdlOiBtb250aGx5IGRhdGEg4oaSIFMgPSAxMiwgcXVhcnRlcmx5IOKGkiBTID0gNCwgd2Vla2x5IOKGkiBTID0gNTIsIGRhaWx5IHdpdGggd2Vla2x5IHBhdHRlcm4g4oaSIFMgPSA3LiBXaGVuIHRoZSBwZXJpb2QgaXMgdW5jZXJ0YWluLCBhIHBlcmlvZG9ncmFtIChzcGVjdHJhbCBkZW5zaXR5IGVzdGltYXRlKSByZXZlYWxzIHBlYWtzIGF0IHRoZSBkb21pbmFudCBmcmVxdWVuY2llcywgZnJvbSB3aGljaCBTID0gMS9mcmVxdWVuY3kuIFNUTCBkZWNvbXBvc2l0aW9uIHdpdGggdW5rbm93biBwZXJpb2QgY2FuIGFsc28gYmUgZXN0aW1hdGVkIGl0ZXJhdGl2ZWx5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTW9udGhseSBkYXRhOiBTID0gMTIgKGFubnVhbCBjeWNsZSByZXBlYXRzIGV2ZXJ5IDEyIG1vbnRocykuIiwiUXVhcnRlcmx5IGRhdGE6IFMgPSA0IChhbm51YWwgY3ljbGUgaW4gZm91ciBxdWFydGVycykuIiwiRGFpbHkgZGF0YSB3aXRoIHdlZWtseSBzZWFzb25hbGl0eTogUyA9IDcuIiwiSG91cmx5IGRhdGEgd2l0aCBkYWlseSBzZWFzb25hbGl0eTogUyA9IDI0OyB3aXRoIHdlZWtseTogUyA9IDE2OC4iLCJVc2UgdGhlIHBlcmlvZG9ncmFtIChzY2lweS5zaWduYWwucGVyaW9kb2dyYW0pIHRvIGZpbmQgZG9taW5hbnQgZnJlcXVlbmN5IHBlYWtzIHdoZW4gcGVyaW9kIGlzIHVua25vd24uIiwiUGxvdCBzZWFzb25hbCBzdWItc2VyaWVzIChhbGwgSmFudWFyaWVzLCBhbGwgRmVicnVhcmllcywgZXRjLikgdG8gdmlzdWFsbHkgY29uZmlybSBTLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHcmlkIFNlYXJjaCBmb3IgQmVzdCBTQVJJTUEgT3JkZXJzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHdhcm5pbmdzXG5mcm9tIGl0ZXJ0b29scyBpbXBvcnQgcHJvZHVjdFxuZnJvbSBzdGF0c21vZGVscy50c2Euc3RhdGVzcGFjZS5zYXJpbWF4IGltcG9ydCBTQVJJTUFYXG5mcm9tIHN0YXRzbW9kZWxzLmRhdGFzZXRzIGltcG9ydCBnZXRfcmRhdGFzZXRcblxuZGF0YSA9IGdldF9yZGF0YXNldChcdTAwMjdBaXJQYXNzZW5nZXJzXHUwMDI3LCBcdTAwMjdkYXRhc2V0c1x1MDAyNylcbnkgPSBucC5sb2coZGF0YS5kYXRhW1x1MDAyN3ZhbHVlXHUwMDI3XS52YWx1ZXMpWzoxMjBdICAjIHRyYWluaW5nIHNldFxuXG5iZXN0X2FpYywgYmVzdF9vcmRlciwgYmVzdF9zb3JkZXIgPSBucC5pbmYsIE5vbmUsIE5vbmVcbnJlc3VsdHMgPSBbXVxuXG5mb3IgcCwgcSwgUCwgUSBpbiBwcm9kdWN0KHJhbmdlKDMpLCByYW5nZSgzKSwgcmFuZ2UoMiksIHJhbmdlKDIpKTpcbiAgICB0cnk6XG4gICAgICAgIHdpdGggd2FybmluZ3MuY2F0Y2hfd2FybmluZ3MoKTpcbiAgICAgICAgICAgIHdhcm5pbmdzLnNpbXBsZWZpbHRlcihcImlnbm9yZVwiKVxuICAgICAgICAgICAgbW9kID0gU0FSSU1BWCh5LCBvcmRlcj0ocCwxLHEpLCBzZWFzb25hbF9vcmRlcj0oUCwxLFEsMTIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICB0cmVuZD1cdTAwMjduXHUwMDI3LCBlbmZvcmNlX3N0YXRpb25hcml0eT1UcnVlLCBlbmZvcmNlX2ludmVydGliaWxpdHk9VHJ1ZSlcbiAgICAgICAgICAgIGZpdCA9IG1vZC5maXQoZGlzcD1GYWxzZSlcbiAgICAgICAgcmVzdWx0cy5hcHBlbmQoKGZpdC5haWMsIGZpdC5iaWMsIChwLDEscSksIChQLDEsUSwxMikpKVxuICAgICAgICBpZiBmaXQuYWljIFx1MDAzYyBiZXN0X2FpYzpcbiAgICAgICAgICAgIGJlc3RfYWljLCBiZXN0X29yZGVyLCBiZXN0X3NvcmRlciA9IGZpdC5haWMsIChwLDEscSksIChQLDEsUSwxMilcbiAgICBleGNlcHQgRXhjZXB0aW9uOlxuICAgICAgICBjb250aW51ZVxuXG5yZXN1bHRzLnNvcnQoKVxucHJpbnQoZlwie1x1MDAyN0FSSU1BXHUwMDI3Olx1MDAzZTEyc30gIHtcdTAwMjdTZWFzb25hbFx1MDAyNzpcdTAwM2UxNHN9ICB7XHUwMDI3QUlDXHUwMDI3Olx1MDAzZThzfSAge1x1MDAyN0JJQ1x1MDAyNzpcdTAwM2U4c31cIilcbnByaW50KFwiLVwiICogNTApXG5mb3IgYWljLCBiaWMsIG9yZHIsIHNvcmRyIGluIHJlc3VsdHNbOjZdOlxuICAgIHByaW50KGZcIntzdHIob3Jkcik6XHUwMDNlMTJzfSAge3N0cihzb3Jkcik6XHUwMDNlMTRzfSAge2FpYzo4LjJmfSAge2JpYzo4LjJmfVwiKVxucHJpbnQoZlwiXFxuQmVzdDogQVJJTUF7YmVzdF9vcmRlcn0geCB7YmVzdF9zb3JkZXJ9ICBBSUM9e2Jlc3RfYWljOi4yZn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTQVJJTUEgRm9yZWNhc3Qgd2l0aCBQcmVkaWN0aW9uIEludGVydmFscyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc3RhdHNtb2RlbHMudHNhLnN0YXRlc3BhY2Uuc2FyaW1heCBpbXBvcnQgU0FSSU1BWFxuZnJvbSBzdGF0c21vZGVscy5kYXRhc2V0cyBpbXBvcnQgZ2V0X3JkYXRhc2V0XG5cbmRhdGEgPSBnZXRfcmRhdGFzZXQoXHUwMDI3QWlyUGFzc2VuZ2Vyc1x1MDAyNywgXHUwMDI3ZGF0YXNldHNcdTAwMjcpXG55X2xvZyAgPSBucC5sb2coZGF0YS5kYXRhW1x1MDAyN3ZhbHVlXHUwMDI3XS52YWx1ZXMpXG50cmFpbiAgPSB5X2xvZ1s6MTIwXVxudGVzdCAgID0gbnAuZXhwKHlfbG9nWzEyMDpdKVxuaG9yaXpvbiA9IDEyXG5cbmZpdCA9IFNBUklNQVgodHJhaW4sIG9yZGVyPSgxLDEsMSksIHNlYXNvbmFsX29yZGVyPSgxLDEsMSwxMiksXG4gICAgICAgICAgICAgIHRyZW5kPVx1MDAyN25cdTAwMjcpLmZpdChkaXNwPUZhbHNlKVxuXG5mYyA9IGZpdC5nZXRfZm9yZWNhc3Qoc3RlcHM9aG9yaXpvbilcbnByZWQgID0gbnAuZXhwKGZjLnByZWRpY3RlZF9tZWFuKVxuY2kgICAgPSBucC5leHAoZmMuY29uZl9pbnQoYWxwaGE9MC4wNSkpXG5cbnByaW50KGZcIntcdTAwMjdNb250aFx1MDAyNzpcdTAwM2U2c30gIHtcdTAwMjdBY3R1YWxcdTAwMjc6XHUwMDNlOHN9ICB7XHUwMDI3Rm9yZWNhc3RcdTAwMjc6XHUwMDNlOXN9ICB7XHUwMDI3OTUlIExvXHUwMDI3Olx1MDAzZThzfSAge1x1MDAyNzk1JSBIaVx1MDAyNzpcdTAwM2U4c30gIHtcdTAwMjdBUEUlXHUwMDI3Olx1MDAzZTZzfVwiKVxucHJpbnQoXCItXCIgKiA1NSlcbmZvciBpIGluIHJhbmdlKGhvcml6b24pOlxuICAgIGFwZSA9IGFicyh0ZXN0LnZhbHVlc1tpXSAtIHByZWQuaWxvY1tpXSkgLyB0ZXN0LnZhbHVlc1tpXSAqIDEwMFxuICAgIHByaW50KGZcIntpKzE6NmR9ICB7dGVzdC52YWx1ZXNbaV06OC4xZn0gIHtwcmVkLmlsb2NbaV06OS4xZn0gIHtjaS5pbG9jW2ksMF06OC4xZn0gIHtjaS5pbG9jW2ksMV06OC4xZn0gIHthcGU6Ni4yZn1cIilcbnByaW50KGZcIlxcbk1BUEUgPSB7bnAubWVhbihucC5hYnMoKHRlc3QudmFsdWVzIC0gcHJlZC52YWx1ZXMpL3Rlc3QudmFsdWVzKSkqMTAwOi4yZn0lXCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlNlYXNvbmFsIERpZmZlcmVuY2luZyB2cyBTZWFzb25hbCBBUiIsImNvbnRlbnQiOiJVc2Ugc2Vhc29uYWwgZGlmZmVyZW5jaW5nIChEPTEpIHdoZW4gdGhlIHNlYXNvbmFsIHBhdHRlcm4gaXMgc3RvY2hhc3RpYyDigJQgaXQgZXZvbHZlcyByYW5kb21seSBvdmVyIHRpbWUsIGFzIGluIG1vc3QgZWNvbm9taWMgc2VyaWVzLiBVc2UgYSBzZWFzb25hbCBBUiAoUD0xLCBEPTApIHdoZW4gdGhlIHNlYXNvbmFsIHBhdHRlcm4gaXMgc3RhYmxlIGFuZCBkZXRlcm1pbmlzdGljLiBBIHF1aWNrIGRpYWdub3N0aWM6IGlmIHRoZSBzZWFzb25hbCBBQ0Ygc3Bpa2VzIGF0IGxhZ3MgUywgMlMsIDNTIGRvIG5vdCBkZWNheSBhbmQgdGhlIEtQU1MgdGVzdCBhdCB0aGUgc2Vhc29uYWwgZnJlcXVlbmN5IHJlamVjdHMsIHNldCBEPTEuIElmIHRoZSBzcGlrZXMgZGVjYXkgZ2VvbWV0cmljYWxseSwgUD0xIHdpdGhvdXQgc2Vhc29uYWwgZGlmZmVyZW5jaW5nIG1heSBiZSBzdWZmaWNpZW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNBUklNQSBDb21wb25lbnRzIFJlZmVyZW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQYXJhbWV0ZXIiLCJNZWFuaW5nIiwiSWRlbnRpZmljYXRpb24gTWV0aG9kIiwiVHlwaWNhbCBSYW5nZSJdLCJyb3dzIjpbWyJwIiwiTm9uLXNlYXNvbmFsIEFSIG9yZGVyIiwiUEFDRiBjdXRzIG9mZiBhZnRlciBsYWcgcCAob24gc3RhdGlvbmFyeSBzZXJpZXMpIiwiMOKAkzMiXSxbImQiLCJSZWd1bGFyIGRpZmZlcmVuY2VzIiwiQURGL0tQU1MgdGVzdCBvbiBvcmlnaW5hbCBzZXJpZXMiLCIw4oCTMiAodXN1YWxseSAwIG9yIDEpIl0sWyJxIiwiTm9uLXNlYXNvbmFsIE1BIG9yZGVyIiwiQUNGIGN1dHMgb2ZmIGFmdGVyIGxhZyBxIChvbiBzdGF0aW9uYXJ5IHNlcmllcykiLCIw4oCTMyJdLFsiUCIsIlNlYXNvbmFsIEFSIG9yZGVyIiwiUEFDRiBzcGlrZSBhdCBsYWcgUyBjdXRzIG9mZiBhZnRlciBQIHNlYXNvbmFsIGxhZ3MiLCIw4oCTMiJdLFsiRCIsIlNlYXNvbmFsIGRpZmZlcmVuY2VzIiwiQURGL0tQU1MgYXQgc2Vhc29uYWwgZnJlcXVlbmN5OyBIRUdZIHRlc3QiLCIw4oCTMSAocmFyZWx5IDIpIl0sWyJRIiwiU2Vhc29uYWwgTUEgb3JkZXIiLCJBQ0Ygc3Bpa2UgYXQgbGFnIFMgY3V0cyBvZmYgYWZ0ZXIgUSBzZWFzb25hbCBsYWdzIiwiMOKAkzIiXSxbIlMiLCJTZWFzb25hbCBwZXJpb2QiLCJEb21haW4ga25vd2xlZGdlLCBwZXJpb2RvZ3JhbSwgb3IgU1RMIGRlY29tcG9zaXRpb24iLCI0LCA3LCAxMiwgMjQsIDUyIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgdXNlZnVsIHByYWN0aWNhbCBoZXVyaXN0aWM6IHN0YXJ0IHdpdGggU0FSSU1BKDEsMSwxKSgxLDEsMSlbU10gKHRoZSBhaXJsaW5lIG1vZGVsIGdlbmVyYWxpc2VkIHRvIHlvdXIgcGVyaW9kKSBhbmQgY29tcGFyZSBpdCBhZ2FpbnN0IHNpbXBsZXIgYWx0ZXJuYXRpdmVzICgwLDEsMSkoMCwxLDEpW1NdIGFuZCAoMSwxLDApKDEsMSwwKVtTXSkgdmlhIEFJQy4gRm9yIHF1YXJ0ZXJseSBHRFAgb3IgbW9udGhseSByZXRhaWwgZGF0YSB0aGlzIHNob3J0bGlzdCBjb3ZlcnMgdGhlIHdpbm5pbmcgbW9kZWwgdGhlIG1ham9yaXR5IG9mIHRoZSB0aW1lLiBSZXNlcnZlIGdyaWQgc2VhcmNoIGZvciBzZXJpZXMgdGhhdCBhcmUgY2xlYXJseSBtaXMtc3BlY2lmaWVkIGFmdGVyIHJlc2lkdWFsIGRpYWdub3N0aWNzLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# SARIMA — Seasonal ARIMA and Period Selection

SARIMA — Seasonal ARIMA — extends the Box-Jenkins framework to series with periodic behaviour. Monthly retail sales, quarterly GDP, daily temperature, and weekly web traffic all exhibit regular patterns that repeat at a known period S. The SARIMA model adds seasonal AR, I (differencing), and MA operators that act at multiples of S, allowing the model to capture both the short-run autocorrelation structure and the long-run seasonal dependencies simultaneously.

## SARIMA Notation and Backshift Operators

SARIMA(p,d,q)(P,D,Q)[S] is written in operator form as Φₚ(B)·φ_P(Bˢ)·(1−B)ᵈ·(1−Bˢ)ᴰ·yₜ = Θq(B)·θ_Q(Bˢ)·εₜ, where φ_P(Bˢ) = 1 − Φ₁Bˢ − … − Φ_PB^(PS) is the seasonal AR polynomial, θ_Q(Bˢ) is the seasonal MA polynomial, (1−Bˢ)ᴰ applies D seasonal differences, and (1−B)ᵈ applies d regular differences. The non-seasonal (p,d,q) part and the seasonal (P,D,Q)[S] part multiply together to form the full model — the total number of AR and MA parameters is p + P.

A common practical model for monthly data is SARIMA(1,1,1)(1,1,1)[12] — the airline model — popularised by Box and Jenkins in their analysis of the international airline passenger dataset. It has: one regular AR lag, one seasonal AR lag at lag 12, one regular MA error, one seasonal MA error at lag 12, one regular difference, and one seasonal difference. Despite having only 4 free parameters plus sigma², it captures the dominant structure of many monthly economic series.

- The seasonal AR polynomial φ_P(Bˢ) = 1 − Φ₁Bˢ − … − Φ_PB^{PS} operates at multiples of S (lags S, 2S, …).
- The seasonal MA polynomial θ_Q(Bˢ) adds smoothing of past seasonal errors — same frequency structure as seasonal AR.
- Seasonal differencing (1 − Bˢ)ᴰ and regular differencing (1 − B)ᵈ are applied before the ARMA fitting.
- Total parameters: p + P AR coefficients, q + Q MA coefficients, plus sigma² — typically 4–8 parameters for common seasonal models.
- Stationarity requires all roots of φ_p(z)·φ_P(zˢ) to lie outside the unit circle; invertibility requires the same for θ_q(z)·θ_Q(zˢ).

## Classic Example — Airline Passengers

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.datasets import get_rdataset

# Load classic airline passengers dataset
data = get_rdataset('AirPassengers', 'datasets')
y = np.log(data.data['value'].values)  # log-transform for additive treatment
n = len(y)
train, test = y[:120], y[120:]  # 132 months: use 120 for training

# Fit SARIMA(1,1,1)(1,1,1)[12] -- the classic airline model
model = SARIMAX(train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12),
                trend='n', enforce_stationarity=True, enforce_invertibility=True)
fit = model.fit(disp=False)

print("SARIMA(1,1,1)(1,1,1)[12] -- Airline Passengers (log scale)")
print(f"  AR phi1   = {fit.params['ar.L1']:.4f}")
print(f"  MA theta1 = {fit.params['ma.L1']:.4f}")
print(f"  SAR Phi1  = {fit.params['ar.S.L12']:.4f}")
print(f"  SMA Theta1= {fit.params['ma.S.L12']:.4f}")
print(f"  AIC       = {fit.aic:.2f}")

# Forecast remaining 12 months
fc = fit.get_forecast(steps=12)
feat_exp = np.exp(fc.predicted_mean)
test_exp  = np.exp(test)
mape = np.mean(np.abs((test_exp - feat_exp) / test_exp)) * 100
print(f"  Test MAPE (last 12 months) = {mape:.2f}%")
```

## Seasonal Differencing and ACF Identification

Seasonal differencing ΔₛYₜ = Yₜ − Yₜ₋ₛ removes a seasonal unit root (a unit root at the seasonal frequency). After D = 1 seasonal difference, the seasonal spikes in the ACF should diminish. If they remain, consider D = 1 regular difference additionally. The seasonal ACF of the doubly-differenced series then shows the residual seasonal AR/MA structure. Overly aggressive differencing (D > 1) is rarely justified and over-complicates the model.

```python
import numpy as np
from statsmodels.tsa.stattools import acf
from statsmodels.datasets import get_rdataset

data = get_rdataset('AirPassengers', 'datasets')
y_log = np.log(data.data['value'].values)

# Regular difference
y_d1 = np.diff(y_log)

# Seasonal difference of regular-differenced series
y_d1_D1 = np.diff(y_d1, n=12)

ci = 1.96 / np.sqrt(len(y_d1_D1))
acf_d1_D1 = acf(y_d1_D1, nlags=24)

print(f"After (1,1,1) differencing: n={len(y_d1_D1)}, CI=+/-{ci:.4f}")
print()
print(f"{'Lag':>4s}  {'ACF':>7s}  {'Sig?':>6s}")
print("-" * 24)
for k in [1, 2, 3, 12, 13, 24]:
    sig = "YES" if abs(acf_d1_D1[k]) > ci else "no"
    print(f"{k:4d}  {acf_d1_D1[k]:7.4f}  {sig:>6s}")
print("\nSpike at lag 1 => MA(1); spike at lag 12 => SMA(1) -- consistent with airline model")
```

## Choosing the Seasonal Period S

The seasonal period S must be known or estimated before fitting SARIMA. In most cases S is determined by domain knowledge: monthly data → S = 12, quarterly → S = 4, weekly → S = 52, daily with weekly pattern → S = 7. When the period is uncertain, a periodogram (spectral density estimate) reveals peaks at the dominant frequencies, from which S = 1/frequency. STL decomposition with unknown period can also be estimated iteratively.

- Monthly data: S = 12 (annual cycle repeats every 12 months).
- Quarterly data: S = 4 (annual cycle in four quarters).
- Daily data with weekly seasonality: S = 7.
- Hourly data with daily seasonality: S = 24; with weekly: S = 168.
- Use the periodogram (scipy.signal.periodogram) to find dominant frequency peaks when period is unknown.
- Plot seasonal sub-series (all Januaries, all Februaries, etc.) to visually confirm S.

## Grid Search for Best SARIMA Orders

```python
import numpy as np
import warnings
from itertools import product
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.datasets import get_rdataset

data = get_rdataset('AirPassengers', 'datasets')
y = np.log(data.data['value'].values)[:120]  # training set

best_aic, best_order, best_sorder = np.inf, None, None
results = []

for p, q, P, Q in product(range(3), range(3), range(2), range(2)):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            mod = SARIMAX(y, order=(p,1,q), seasonal_order=(P,1,Q,12),
                          trend='n', enforce_stationarity=True, enforce_invertibility=True)
            fit = mod.fit(disp=False)
        results.append((fit.aic, fit.bic, (p,1,q), (P,1,Q,12)))
        if fit.aic < best_aic:
            best_aic, best_order, best_sorder = fit.aic, (p,1,q), (P,1,Q,12)
    except Exception:
        continue

results.sort()
print(f"{'ARIMA':>12s}  {'Seasonal':>14s}  {'AIC':>8s}  {'BIC':>8s}")
print("-" * 50)
for aic, bic, ordr, sordr in results[:6]:
    print(f"{str(ordr):>12s}  {str(sordr):>14s}  {aic:8.2f}  {bic:8.2f}")
print(f"\nBest: ARIMA{best_order} x {best_sorder}  AIC={best_aic:.2f}")
```

## SARIMA Forecast with Prediction Intervals

```python
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.datasets import get_rdataset

data = get_rdataset('AirPassengers', 'datasets')
y_log  = np.log(data.data['value'].values)
train  = y_log[:120]
test   = np.exp(y_log[120:])
horizon = 12

fit = SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12),
              trend='n').fit(disp=False)

fc = fit.get_forecast(steps=horizon)
pred  = np.exp(fc.predicted_mean)
ci    = np.exp(fc.conf_int(alpha=0.05))

print(f"{'Month':>6s}  {'Actual':>8s}  {'Forecast':>9s}  {'95% Lo':>8s}  {'95% Hi':>8s}  {'APE%':>6s}")
print("-" * 55)
for i in range(horizon):
    ape = abs(test.values[i] - pred.iloc[i]) / test.values[i] * 100
    print(f"{i+1:6d}  {test.values[i]:8.1f}  {pred.iloc[i]:9.1f}  {ci.iloc[i,0]:8.1f}  {ci.iloc[i,1]:8.1f}  {ape:6.2f}")
print(f"\nMAPE = {np.mean(np.abs((test.values - pred.values)/test.values))*100:.2f}%")
```

> **Seasonal Differencing vs Seasonal AR**: Use seasonal differencing (D=1) when the seasonal pattern is stochastic — it evolves randomly over time, as in most economic series. Use a seasonal AR (P=1, D=0) when the seasonal pattern is stable and deterministic. A quick diagnostic: if the seasonal ACF spikes at lags S, 2S, 3S do not decay and the KPSS test at the seasonal frequency rejects, set D=1. If the spikes decay geometrically, P=1 without seasonal differencing may be sufficient.

## SARIMA Components Reference

| Parameter | Meaning | Identification Method | Typical Range |
| --- | --- | --- | --- |
| p | Non-seasonal AR order | PACF cuts off after lag p (on stationary series) | 0–3 |
| d | Regular differences | ADF/KPSS test on original series | 0–2 (usually 0 or 1) |
| q | Non-seasonal MA order | ACF cuts off after lag q (on stationary series) | 0–3 |
| P | Seasonal AR order | PACF spike at lag S cuts off after P seasonal lags | 0–2 |
| D | Seasonal differences | ADF/KPSS at seasonal frequency; HEGY test | 0–1 (rarely 2) |
| Q | Seasonal MA order | ACF spike at lag S cuts off after Q seasonal lags | 0–2 |
| S | Seasonal period | Domain knowledge, periodogram, or STL decomposition | 4, 7, 12, 24, 52 |

A useful practical heuristic: start with SARIMA(1,1,1)(1,1,1)[S] (the airline model generalised to your period) and compare it against simpler alternatives (0,1,1)(0,1,1)[S] and (1,1,0)(1,1,0)[S]) via AIC. For quarterly GDP or monthly retail data this shortlist covers the winning model the majority of the time. Reserve grid search for series that are clearly mis-specified after residual diagnostics.

---

