---
title: "State Space Models and the Kalman Filter"
slug: "state-space-models-kalman"
description: "Formulate time series as state space models with latent state and observation equations, derive the Kalman filter predict-update cycle, implement the local level model, connect SSM to ARIMA, and extend to nonlinear systems via the Unscented Kalman Filter."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhdGUgc3BhY2UgbW9kZWxzIChTU01zKSBwcm92aWRlIGEgZ2VuZXJhbCBmcmFtZXdvcmsgZm9yIHRpbWUtc2VyaWVzIG1vZGVsbGluZyBieSBzZXBhcmF0aW5nIHRoZSBvYnNlcnZlZCBtZWFzdXJlbWVudHMgZnJvbSBhbiB1bmRlcmx5aW5nIGxhdGVudCBzdGF0ZSB0aGF0IGV2b2x2ZXMgb3ZlciB0aW1lLiBBbnkgQVJJTUEgbW9kZWwgY2FuIGJlIHdyaXR0ZW4gaW4gc3RhdGUgc3BhY2UgZm9ybSwgYnV0IFNTTXMgYXJlIHN0cmljdGx5IG1vcmUgZ2VuZXJhbDogdGhleSBjYW4gaW5jb3Jwb3JhdGUgdGltZS12YXJ5aW5nIHBhcmFtZXRlcnMsIG11bHRpcGxlIG9ic2VydmF0aW9uIGVxdWF0aW9ucywgbWlzc2luZyBkYXRhLCBhbmQgc3RydWN0dXJhbCBjb21wb25lbnRzICh0cmVuZCwgc2Vhc29uYWwsIHJlZ3Jlc3Npb24pIHRoYXQgY2hhbmdlIHNtb290aGx5IG92ZXIgdGltZS4gVGhlIEthbG1hbiBmaWx0ZXIgZ2l2ZXMgdGhlIG9wdGltYWwgbGluZWFyIHVwZGF0ZSBydWxlIGZvciB0cmFja2luZyB0aGUgbGF0ZW50IHN0YXRlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0YXRlIFNwYWNlIEZvcm11bGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbGluZWFyIEdhdXNzaWFuIHN0YXRlIHNwYWNlIG1vZGVsIGNvbnNpc3RzIG9mIHR3byBlcXVhdGlvbnMuIFRoZSBzdGF0ZSAodHJhbnNpdGlvbikgZXF1YXRpb24geOKCnCA9IEZ44oKc4oKL4oKBICsgQnfigpwgZGVzY3JpYmVzIGhvdyB0aGUgaGlkZGVuIHN0YXRlIHjigpwg4oiIIOKEneG1kCBldm9sdmVzIHdpdGggc3RhdGUgdHJhbnNpdGlvbiBtYXRyaXggRiDiiIgg4oSd4bWQy6PhtZAgYW5kIHByb2Nlc3Mgbm9pc2Ugd+KCnCB+IE4oMCwgUSkuIFRoZSBvYnNlcnZhdGlvbiBlcXVhdGlvbiB54oKcID0gSHjigpwgKyB24oKcIGxpbmtzIHRoZSBzdGF0ZSB0byB0aGUgb2JzZXJ2ZWQgbWVhc3VyZW1lbnQgeeKCnCDiiIgg4oSd4oG/IHZpYSBvYnNlcnZhdGlvbiBtYXRyaXggSCDiiIgg4oSd4oG/y6PhtZAgYW5kIG9ic2VydmF0aW9uIG5vaXNlIHbigpwgfiBOKDAsIFIpLiBUaGUgbWF0cmljZXMgRiwgSCwgUSwgUiBtYXkgYmUgdGltZS12YXJ5aW5nIGJ1dCBhcmUgYXNzdW1lZCBrbm93biBmb3IgZmlsdGVyaW5nOyB0aGV5IGFyZSBlc3RpbWF0ZWQgYnkgTUxFIGR1cmluZyB0cmFpbmluZy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlN0YXRlIHZlY3RvciB44oKcOiBlbmNvZGVzIHRoZSBsYXRlbnQgcXVhbnRpdGllcyBkcml2aW5nIHRoZSBvYnNlcnZhdGlvbnMgKGxldmVsLCB0cmVuZCwgc2Vhc29uYWwgZmFjdG9ycywgZXRjLikuIiwiRiAodHJhbnNpdGlvbiBtYXRyaXgpOiBnb3Zlcm5zIGhvdyB0aGUgc3RhdGUgZXZvbHZlcyDigJQgaWRlbnRpdHkgZm9yIHJhbmRvbSB3YWxrLCByb3RhdGlvbiBtYXRyaXggZm9yIHNlYXNvbmFsIGN5Y2xlLiIsIlEgKHByb2Nlc3Mgbm9pc2UgY292YXJpYW5jZSk6IGNvbnRyb2xzIGhvdyByYXBpZGx5IHRoZSBzdGF0ZSBjYW4gY2hhbmdlIOKAlCBsYXJnZSBRID0gcmFwaWRseSBldm9sdmluZyBjb21wb25lbnRzLiIsIkggKG9ic2VydmF0aW9uIG1hdHJpeCk6IHNlbGVjdHMgd2hpY2ggY29tcG9uZW50cyBvZiB0aGUgc3RhdGUgYXJlIG9ic2VydmVkIOKAlCBvZnRlbiBbMSwgMCwgMCwg4oCmXS4iLCJSIChvYnNlcnZhdGlvbiBub2lzZSBjb3ZhcmlhbmNlKTogcmVwcmVzZW50cyBtZWFzdXJlbWVudCBlcnJvciBvciBpZGlvc3luY3JhdGljIG5vaXNlIGluIHRoZSBvYnNlcnZhdGlvbnMuIiwiSW5pdGlhbCBjb25kaXRpb25zOiB44oKAfOKCgCB+IE4obeKCgCwgUOKCgCkg4oCUIHByaW9yIG9uIHRoZSBzdGF0ZSBiZWZvcmUgc2VlaW5nIGFueSBkYXRhLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgS2FsbWFuIEZpbHRlciDigJQgUHJlZGljdCBhbmQgVXBkYXRlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgS2FsbWFuIGZpbHRlciBjb21wdXRlcyB0aGUgb3B0aW1hbCAobWluaW11bSBtZWFuIHNxdWFyZWQgZXJyb3IpIGxpbmVhciBlc3RpbWF0ZSBvZiB0aGUgc3RhdGUgZ2l2ZW4gYWxsIHBhc3Qgb2JzZXJ2YXRpb25zLiBJdCBhbHRlcm5hdGVzIHR3byBzdGVwcy4gUHJlZGljdDogeMyC4oKcfHTigovigoEgPSBGeMyC4oKc4oKL4oKBfHTigovigoEgKHN0YXRlIHByZWRpY3Rpb24pLCBQ4oKcfHTigovigoEgPSBGUOKCnOKCi+KCgXx04oKL4oKBRuG1gCArIFEgKHVuY2VydGFpbnR5IHByb3BhZ2F0aW9uKS4gVXBkYXRlOiBpbm5vdmF0aW9uIGXigpwgPSB54oKcIOKIkiBIeMyC4oKcfHTigovigoEsIGlubm92YXRpb24gY292YXJpYW5jZSBT4oKcID0gSFDigpx8dOKCi+KCgUjhtYAgKyBSLCBLYWxtYW4gZ2FpbiBL4oKcID0gUOKCnHx04oKL4oKBSOG1gFPigpzigbvCuSwgc3RhdGUgdXBkYXRlIHjMguKCnHx0ID0geMyC4oKcfHTigovigoEgKyBL4oKcZeKCnCwgY292YXJpYW5jZSB1cGRhdGUgUOKCnHx0ID0gKEkg4oiSIEvigpxIKVDigpx8dOKCi+KCgS4gVGhlIEthbG1hbiBnYWluIEvigpwgYmFsYW5jZXMgdHJ1c3QgYmV0d2VlbiB0aGUgc3RhdGUgcHJlZGljdGlvbiBhbmQgdGhlIG5ldyBvYnNlcnZhdGlvbiwgd2VpZ2h0aW5nIHRvd2FyZCB0aGUgb2JzZXJ2YXRpb24gd2hlbiBSIGlzIHNtYWxsIHJlbGF0aXZlIHRvIEhQSFx1MDAyNy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBrYWxtYW5fZmlsdGVyKHksIEYsIEgsIFEsIFIsIG0wLCBQMCk6XG4gICAgXCJcIlwiTGluZWFyIEthbG1hbiBmaWx0ZXIuIFJldHVybnMgZmlsdGVyZWQgbWVhbnMgYW5kIGNvdmFyaWFuY2VzLlwiXCJcIlxuICAgIG4gPSBsZW4oeSlcbiAgICBtID0gRi5zaGFwZVswXVxuICAgIHhfZmlsdCA9IG5wLnplcm9zKChuLCBtKSlcbiAgICBQX2ZpbHQgPSBucC56ZXJvcygobiwgbSwgbSkpXG4gICAgbG9nX2xpayA9IDAuMFxuICAgIHggPSBtMC5jb3B5KClcbiAgICBQID0gUDAuY29weSgpXG4gICAgZm9yIHQgaW4gcmFuZ2Uobik6XG4gICAgICAgICMgUHJlZGljdFxuICAgICAgICB4X3ByZWQgPSBGIEAgeFxuICAgICAgICBQX3ByZWQgPSBGIEAgUCBAIEYuVCArIFFcbiAgICAgICAgIyBJbm5vdmF0aW9uXG4gICAgICAgIGlubm92ID0geVt0XSAtIEggQCB4X3ByZWRcbiAgICAgICAgUyAgICAgPSBIIEAgUF9wcmVkIEAgSC5UICsgUlxuICAgICAgICBLICAgICA9IFBfcHJlZCBAIEguVCAvIFNbMCwgMF0gICMgc2NhbGFyIG9iczogUyBpcyAxeDFcbiAgICAgICAgIyBVcGRhdGVcbiAgICAgICAgeCA9IHhfcHJlZCArIEsgKiBpbm5vdlxuICAgICAgICBQID0gKG5wLmV5ZShtKSAtIEtbOiwgTm9uZV0gKiBIKSBAIFBfcHJlZFxuICAgICAgICB4X2ZpbHRbdF0gPSB4XG4gICAgICAgIFBfZmlsdFt0XSA9IFBcbiAgICAgICAgbG9nX2xpayAgLT0gMC41ICogKG5wLmxvZygyICogbnAucGkgKiBTWzAsIDBdKSArIGlubm92KioyIC8gU1swLCAwXSlcbiAgICByZXR1cm4geF9maWx0LCBQX2ZpbHQsIGxvZ19saWtcblxuIyBUZXN0IG9uIGEgc2ltcGxlIEFSKDEpIGluIHN0YXRlIHNwYWNlIGZvcm1cbm5wLnJhbmRvbS5zZWVkKDApXG5uICA9IDEwMFxueSAgPSBucC56ZXJvcyhuKVxuZm9yIHQgaW4gcmFuZ2UoMSwgbik6XG4gICAgeVt0XSA9IDAuOCAqIHlbdC0xXSArIG5wLnJhbmRvbS5yYW5kbigpXG55ICs9IDAuNSAqIG5wLnJhbmRvbS5yYW5kbihuKSAgIyBvYnNlcnZhdGlvbiBub2lzZVxuXG5GICA9IG5wLmFycmF5KFtbMC44XV0pXG5IICA9IG5wLmFycmF5KFtbMS4wXV0pXG5RICA9IG5wLmFycmF5KFtbMS4wXV0pXG5SICA9IG5wLmFycmF5KFtbMC4yNV1dKVxubTAgPSBucC5hcnJheShbMC4wXSlcblAwID0gbnAuYXJyYXkoW1sxLjBdXSlcblxuZmlsdCwgXywgbGwgPSBrYWxtYW5fZmlsdGVyKHksIEYsIEgsIFEsIFIsIG0wLCBQMClcbnByaW50KGZcIkxvZy1saWtlbGlob29kOiB7bGw6LjRmfVwiKVxucHJpbnQoZlwiRmlsdGVyIFJNU0UgdnMgb2JzZXJ2YXRpb25zOiB7bnAuc3FydChucC5tZWFuKChmaWx0WzosMF0teSkqKjIpKTouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG9jYWwgTGV2ZWwgTW9kZWwg4oCUIFRyZW5kIEZpbHRlcmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGxvY2FsIGxldmVsIG1vZGVsIChMTE0pIGlzIHRoZSBzaW1wbGVzdCBTU006IHRoZSBzdGF0ZSB44oKcIGZvbGxvd3MgYSByYW5kb20gd2FsayAoeOKCnCA9IHjigpzigovigoEgKyB34oKcLCB34oKcIH4gTigwLCDPg8KyX863KSkgYW5kIG9ic2VydmF0aW9ucyB54oKcID0geOKCnCArIHbigpwsIHbigpwgfiBOKDAsIM+DwrJfzrUpLiBJbiBtYXRyaXggZm9ybSBGID0gSCA9IDEsIFEgPSDPg8KyX863LCBSID0gz4PCsl/OtS4gVGhlIHNpZ25hbC10by1ub2lzZSByYXRpbyBxID0gz4PCsl/Oty/Pg8KyX861IGNvbnRyb2xzIGhvdyByYXBpZGx5IHRoZSBmaWx0ZXJlZCB0cmVuZCB0cmFja3MgdGhlIG9ic2VydmF0aW9uczogbGFyZ2UgcSBtZWFucyB0aGUgdHJlbmQgbW92ZXMgcXVpY2tseSAoZm9sbG93cyBlYWNoIG9ic2VydmF0aW9uKSwgc21hbGwgcSBtZWFucyB0aGUgdHJlbmQgaXMgc21vb3RoIChpZ25vcmVzIG5vaXNlKS4gVGhlIExMTSBpcyBlcXVpdmFsZW50IHRvIGV4cG9uZW50aWFsIHNtb290aGluZyAoRVdNQSkgd2hlbiB0aGUgS2FsbWFuIGdhaW4gaGFzIGNvbnZlcmdlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubiA9IDIwMFxuXG4jIFRydWUgc2xvd2x5LWV2b2x2aW5nIGxldmVsXG5sZXZlbF90cnVlID0gbnAuY3Vtc3VtKDAuMiAqIG5wLnJhbmRvbS5yYW5kbihuKSlcbnkgPSBsZXZlbF90cnVlICsgMy4wICogbnAucmFuZG9tLnJhbmRuKG4pICAjIGhpZ2ggb2JzIG5vaXNlXG5cbmRlZiBsbG1fZmlsdGVyKHksIHNpZ21hX2V0YSwgc2lnbWFfZXBzKTpcbiAgICB4LCBQID0gMC4wLCAxLjBcbiAgICBmaWx0ZXJlZCA9IG5wLnplcm9zKG4pXG4gICAgZm9yIHQgaW4gcmFuZ2Uobik6XG4gICAgICAgICMgUHJlZGljdFxuICAgICAgICBQX3ByZWQgPSBQICsgc2lnbWFfZXRhKioyXG4gICAgICAgICMgVXBkYXRlXG4gICAgICAgIEsgPSBQX3ByZWQgLyAoUF9wcmVkICsgc2lnbWFfZXBzKioyKVxuICAgICAgICB4ID0geCArIEsgKiAoeVt0XSAtIHgpXG4gICAgICAgIFAgPSAoMSAtIEspICogUF9wcmVkXG4gICAgICAgIGZpbHRlcmVkW3RdID0geFxuICAgIHJldHVybiBmaWx0ZXJlZFxuXG5wcmludChmXCJ7XHUwMDI3c2lnbWFfZXRhXHUwMDI3Olx1MDAzZTEwc30gIHtcdTAwMjdzaWdtYV9lcHNcdTAwMjc6XHUwMDNlMTBzfSAge1x1MDAyN1NOUiBxXHUwMDI3Olx1MDAzZThzfSAge1x1MDAyN1JNU0UgKHZzIHRydWUgbGV2ZWwpXHUwMDI3Olx1MDAzZTIyc31cIilcbnByaW50KFwiLVwiICogNTgpXG5mb3Igc19ldGEgaW4gWzAuMSwgMC41LCAxLjAsIDIuMF06XG4gICAgZmlsdCA9IGxsbV9maWx0ZXIoeSwgc19ldGEsIDMuMClcbiAgICBybXNlID0gbnAuc3FydChucC5tZWFuKChmaWx0IC0gbGV2ZWxfdHJ1ZSkqKjIpKVxuICAgIHEgICAgPSBzX2V0YSoqMiAvIDkuMFxuICAgIHByaW50KGZcIntzX2V0YToxMC4yZn0gIHszLjA6MTAuMmZ9ICB7cTo4LjRmfSAge3Jtc2U6MjIuNGZ9XCIpXG5wcmludChcIlNtYWxsIHEgLVx1MDAzZSBzbW9vdGggdHJlbmQ7IExhcmdlIHEgLVx1MDAzZSB0cmFja3Mgb2JzZXJ2YXRpb25zIGNsb3NlbHlcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25uZWN0aW9uIHRvIEFSSU1BIGFuZCBNTEUgRXN0aW1hdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGFyYW1ldGVyIGVzdGltYXRpb24gaW4gU1NNcyBwcm9jZWVkcyBieSBtYXhpbWlzaW5nIHRoZSBHYXVzc2lhbiBsb2ctbGlrZWxpaG9vZCBMID0g4oiSwr3Oo1tsb2coMs+AfFPigpx8KSArIGXigpzhtYBT4oKc4oG7wrll4oKcXSwgd2hlcmUgZeKCnCBhcmUgdGhlIEthbG1hbiBmaWx0ZXIgaW5ub3ZhdGlvbnMgYW5kIFPigpwgdGhlaXIgY292YXJpYW5jZSBtYXRyaWNlcy4gQmVjYXVzZSB0aGUgS2FsbWFuIGZpbHRlciBjb21wdXRlcyBpbm5vdmF0aW9ucyBzZXF1ZW50aWFsbHksIHRoaXMgZXhwcmVzc2lvbiBpcyBlZmZpY2llbnRseSBldmFsdWF0ZWQgaW4gTyhuwrdtwrMpIHRpbWUuIEdyYWRpZW50LWJhc2VkIG9wdGltaXNhdGlvbiAoTC1CRkdTLCBFTSBhbGdvcml0aG0pIHRoZW4gZmluZHMgdGhlIE1MRSBlc3RpbWF0ZXMgb2YgRiwgUSwgSCwgUi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV2ZXJ5IEFSSU1BKHAsZCxxKSBtb2RlbCBoYXMgYW4gZXhhY3Qgc3RhdGUgc3BhY2UgcmVwcmVzZW50YXRpb24uIFRoZSBzdGF0ZSB2ZWN0b3IgZW5jb2RlcyB0aGUgbGFnZ2VkIHZhbHVlcyBuZWVkZWQgdG8gcmVjdXJzaXZlbHkgY29tcHV0ZSB0aGUgaW5ub3ZhdGlvbnMuIFRoaXMgaXMgaW1wb3J0YW50IGZvciB0d28gcmVhc29uczogdGhlIEthbG1hbiBmaWx0ZXIgcHJvdmlkZXMgYSBjb21wdXRhdGlvbmFsbHkgZWZmaWNpZW50IE8obsK3bcKzKSBhbGdvcml0aG0gdG8gZXZhbHVhdGUgdGhlIEdhdXNzaWFuIGxvZy1saWtlbGlob29kIG9mIGFueSBBUklNQSBtb2RlbCwgZW5hYmxpbmcgZ3JhZGllbnQtYmFzZWQgTUxFOyBhbmQgdGhlIHN0YXRlIHNwYWNlIGZvcm0gaGFuZGxlcyBtaXNzaW5nIGRhdGEgbmF0dXJhbGx5IOKAlCBtaXNzaW5nIG9ic2VydmF0aW9ucyBzaW1wbHkgc2tpcCB0aGUgdXBkYXRlIHN0ZXAgKHRoZSBwcmVkaWN0IHN0ZXAgc3RpbGwgcnVucyksIGFsbG93aW5nIGVzdGltYXRpb24gZXZlbiB3aXRoIGdhcHMgaW4gdGhlIHNlcmllcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdHJ1Y3R1cmFsIFRpbWUgU2VyaWVzIHdpdGggVW5vYnNlcnZlZENvbXBvbmVudHMifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHN0YXRzbW9kZWxzLnRzYS5zdGF0ZXNwYWNlLnN0cnVjdHVyYWwgaW1wb3J0IFVub2JzZXJ2ZWRDb21wb25lbnRzXG5cbm5wLnJhbmRvbS5zZWVkKDcpXG5uID0gMjAwXG50ID0gbnAuYXJhbmdlKG4pXG5cbiMgR2VuZXJhdGU6IHN0b2NoYXN0aWMgbGV2ZWwgKyBkZXRlcm1pbmlzdGljIHNsb3BlICsgc2Vhc29uYWwgKyBub2lzZVxubGV2ZWwgICA9IG5wLmN1bXN1bSgwLjMgKiBucC5yYW5kb20ucmFuZG4obikpXG5zbG9wZSAgID0gMC4xICogdFxuc2Vhc29uICA9IDUuMCAqIG5wLnNpbigyICogbnAucGkgKiB0IC8gMTIpXG55ID0gbGV2ZWwgKyBzbG9wZSArIHNlYXNvbiArIG5wLnJhbmRvbS5yYW5kbihuKVxuXG4jIEZpdCBsb2NhbCBsaW5lYXIgdHJlbmQgKyBzdG9jaGFzdGljIGN5Y2xlIG1vZGVsXG5tb2RlbCA9IFVub2JzZXJ2ZWRDb21wb25lbnRzKFxuICAgIHksXG4gICAgbGV2ZWw9XHUwMDI3bG9jYWwgbGluZWFyIHRyZW5kXHUwMDI3LFxuICAgIHNlYXNvbmFsPTEyLFxuICAgIHN0b2NoYXN0aWNfc2Vhc29uYWw9VHJ1ZVxuKVxuZml0ID0gbW9kZWwuZml0KGRpc3A9RmFsc2UsIG1ldGhvZD1cdTAwMjdsYmZnc1x1MDAyNylcblxucHJpbnQoXCJVbm9ic2VydmVkQ29tcG9uZW50cyAoQlNUUy1saWtlKSBmaXQ6XCIpXG5wcmludChmXCIgIExvZy1saWtlbGlob29kOiB7Zml0LmxsZjouNGZ9XCIpXG5wcmludChmXCIgIEFJQzogICAgICAgICAgICB7Zml0LmFpYzouNGZ9XCIpXG5cbiMgU21vb3RoZWQgY29tcG9uZW50c1xuc21vb3RoZWQgPSBmaXQuc21vb3RoZXJfcmVzdWx0c1xucHJpbnQoZlwiICBMZXZlbCBzaWdtYV4yOiAgICB7Zml0LnBhcmFtcy5nZXQoXHUwMDI3c2lnbWEyLmxldmVsXHUwMDI3LCBcdTAwMjdOL0FcdTAwMjcpfVwiKVxucHJpbnQoZlwiICBTZWFzb25hbCBzaWdtYV4yOiB7Zml0LnBhcmFtcy5nZXQoXHUwMDI3c2lnbWEyLnNlYXNvbmFsXHUwMDI3LCBcdTAwMjdOL0FcdTAwMjcpfVwiKVxuZmMgPSBmaXQuZ2V0X2ZvcmVjYXN0KDEyKVxucHJpbnQoZlwiICAxMi1zdGVwIE1BUEU6ICAgICBOL0EgKG5vIHRlc3Qgc2V0OyBpbnNwZWN0IGNvbmZfaW50IGZvciBpbnRlcnZhbCB3aWR0aClcIilcbnByaW50KGZpdC5zdW1tYXJ5KCkudGFibGVzWzFdKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuc2NlbnRlZCBLYWxtYW4gRmlsdGVyIGZvciBOb25saW5lYXIgU3lzdGVtcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHN0YW5kYXJkIEthbG1hbiBmaWx0ZXIgaXMgb3B0aW1hbCBvbmx5IGZvciBsaW5lYXIgR2F1c3NpYW4gc3lzdGVtcy4gV2hlbiB0aGUgc3RhdGUgb3Igb2JzZXJ2YXRpb24gZXF1YXRpb25zIGFyZSBub25saW5lYXIg4oCUIGUuZy4sIHjigpwgPSBmKHjigpzigovigoEpICsgbm9pc2UsIHnigpwgPSBoKHjigpwpICsgbm9pc2Ug4oCUIHRoZSBFeHRlbmRlZCBLYWxtYW4gRmlsdGVyIChFS0YpIGxpbmVhcmlzZXMgZiBhbmQgaCB2aWEgSmFjb2JpYW5zLCBidXQgdGhpcyBjYW4gYmUgaW5hY2N1cmF0ZSBmb3IgaGlnaGx5IG5vbmxpbmVhciBmdW5jdGlvbnMuIFRoZSBVbnNjZW50ZWQgS2FsbWFuIEZpbHRlciAoVUtGKSBpbnN0ZWFkIHByb3BhZ2F0ZXMgYSBzbWFsbCBzZXQgb2YgZGV0ZXJtaW5pc3RpY2FsbHkgY2hvc2VuIHNpZ21hIHBvaW50cyB0aHJvdWdoIHRoZSBub25saW5lYXIgZnVuY3Rpb25zLCBjYXB0dXJpbmcgdGhlIG1lYW4gYW5kIGNvdmFyaWFuY2UgdG8gdGhpcmQgb3JkZXIgKHZzIGZpcnN0IG9yZGVyIGZvciBFS0YpLCB3aXRob3V0IGNvbXB1dGluZyBKYWNvYmlhbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgdWtmXzFkKHksIGYsIGgsIFEsIFIsIHgwLCBQMCwgYWxwaGE9MWUtMywgYmV0YT0yLjAsIGthcHBhPTAuMCk6XG4gICAgXCJcIlwiTWluaW1hbCBzY2FsYXItc3RhdGUgVUtGIGZvciBkZW1vbnN0cmF0aW9uLlwiXCJcIlxuICAgIG5feCA9IDFcbiAgICBsYW0gPSBhbHBoYSoqMiAqIChuX3ggKyBrYXBwYSkgLSBuX3hcbiAgICBXbSAgPSBucC5hcnJheShbbGFtLyhuX3grbGFtKSwgMC41LyhuX3grbGFtKSwgMC41LyhuX3grbGFtKV0pXG4gICAgV2MgID0gV20uY29weSgpXG4gICAgV2NbMF0gKz0gKDEgLSBhbHBoYSoqMiArIGJldGEpXG4gICAgeCwgUCA9IHgwLCBQMFxuICAgIGZpbHRlcmVkID0gbnAuemVyb3MobGVuKHkpKVxuICAgIGZvciB0IGluIHJhbmdlKGxlbih5KSk6XG4gICAgICAgICMgU2lnbWEgcG9pbnRzXG4gICAgICAgIHNwcmVhZCA9IG5wLnNxcnQoKG5feCArIGxhbSkgKiBQKVxuICAgICAgICBzaWdtYXMgPSBucC5hcnJheShbeCwgeCArIHNwcmVhZCwgeCAtIHNwcmVhZF0pXG4gICAgICAgICMgUHJlZGljdFxuICAgICAgICBzaWdtYXNfZiA9IG5wLmFycmF5KFtmKHMpIGZvciBzIGluIHNpZ21hc10pXG4gICAgICAgIHhfcCA9IG5wLmRvdChXbSwgc2lnbWFzX2YpXG4gICAgICAgIFBfcCA9IG5wLmRvdChXYywgKHNpZ21hc19mIC0geF9wKSoqMikgKyBRXG4gICAgICAgICMgT2JzZXJ2YXRpb24gc2lnbWEgcG9pbnRzXG4gICAgICAgIHNpZ21hc19wID0gbnAuYXJyYXkoW3hfcCwgeF9wICsgbnAuc3FydCgobl94K2xhbSkqUF9wKSwgeF9wIC0gbnAuc3FydCgobl94K2xhbSkqUF9wKV0pXG4gICAgICAgIHNpZ21hc19oID0gbnAuYXJyYXkoW2gocykgZm9yIHMgaW4gc2lnbWFzX3BdKVxuICAgICAgICB5X3AgPSBucC5kb3QoV20sIHNpZ21hc19oKVxuICAgICAgICBQeXkgPSBucC5kb3QoV2MsIChzaWdtYXNfaCAtIHlfcCkqKjIpICsgUlxuICAgICAgICBQeHkgPSBucC5kb3QoV2MsIChzaWdtYXNfcCAtIHhfcCkgKiAoc2lnbWFzX2ggLSB5X3ApKVxuICAgICAgICBLICAgPSBQeHkgLyBQeXlcbiAgICAgICAgeCAgID0geF9wICsgSyAqICh5W3RdIC0geV9wKVxuICAgICAgICBQICAgPSBQX3AgLSBLKioyICogUHl5XG4gICAgICAgIGZpbHRlcmVkW3RdID0geFxuICAgIHJldHVybiBmaWx0ZXJlZFxuXG5ucC5yYW5kb20uc2VlZCgzKVxubiA9IDEwMFxudHJ1ZV94ID0gbnAuY3Vtc3VtKDAuMSAqIG5wLnJhbmRvbS5yYW5kbihuKSlcbnkgPSB0cnVlX3gqKjIgKyAwLjUgKiBucC5yYW5kb20ucmFuZG4obikgICMgbm9ubGluZWFyIG9ic2VydmF0aW9uOiBoKHgpPXheMlxuXG5maWx0ZXJlZCA9IHVrZl8xZCh5LCBmPWxhbWJkYSB4OiB4LCBoPWxhbWJkYSB4OiB4KioyLCBRPTAuMDEsIFI9MC4yNSwgeDA9MC4wLCBQMD0xLjApXG5ybXNlID0gbnAuc3FydChucC5tZWFuKChmaWx0ZXJlZCAtIHRydWVfeCkqKjIpKVxucHJpbnQoZlwiVUtGIFJNU0UgKHN0YXRlIGVzdGltYXRlIHZzIHRydWUgeCk6IHtybXNlOi40Zn1cIilcbnByaW50KFwiVUtGIGhhbmRsZXMgbm9ubGluZWFyIG9ic2VydmF0aW9uIGgoeCk9eF4yIHdpdGhvdXQgSmFjb2JpYW5zXCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJXaGVuIHRvIFVzZSBTdGF0ZSBTcGFjZSB2cyBBUklNQSIsImNvbnRlbnQiOiJBUklNQSBpcyBzdWZmaWNpZW50IHdoZW4gdGhlIGRhdGEtZ2VuZXJhdGluZyBwcm9jZXNzIGlzIHN0YWJsZSwgdGhlIHNlcmllcyBpcyB1bml2YXJpYXRlLCBhbmQgeW91IG5lZWQgYSBmYXN0LCBpbnRlcnByZXRhYmxlIG1vZGVsLiBDaG9vc2UgYSBzdGF0ZSBzcGFjZSAvIHN0cnVjdHVyYWwgbW9kZWwgd2hlbiB5b3UgbmVlZDogZXhwbGljaXQgc2VwYXJhdGlvbiBvZiB0cmVuZCwgc2Vhc29uYWwsIGFuZCByZWdyZXNzaW9uIGNvbXBvbmVudHM7IHRpbWUtdmFyeWluZyBwYXJhbWV0ZXJzIChlLmcuLCBzZWFzb25hbGl0eSB0aGF0IGV2b2x2ZXMpOyBtaXNzaW5nIGRhdGEgaGFuZGxpbmc7IGluY29ycG9yYXRpb24gb2YgZXhvZ2Vub3VzIHJlZ3Jlc3NvcnMgaW50byB0aGUgc3RhdGU7IG9yIGEgQmF5ZXNpYW4gdHJlYXRtZW50IHdpdGggcHJpb3IgZGlzdHJpYnV0aW9ucyBvbiB2YXJpYW5jZSBjb21wb25lbnRzIChCU1RTKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTU00gQ29tcG9uZW50IFJlZmVyZW5jZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDb21wb25lbnQiLCJNYXRyaXggLyBFcXVhdGlvbiIsIkRpbWVuc2lvbnMiLCJJbnRlcnByZXRhdGlvbiJdLCJyb3dzIjpbWyJTdGF0ZSB0cmFuc2l0aW9uIiwieOKCnCA9IEZ44oKc4oKL4oKBICsgQnfigpwiLCJGOiBtw5dtLCB4OiBtw5cxIiwiSG93IHRoZSBoaWRkZW4gc3RhdGUgZXZvbHZlcyBhY3Jvc3MgdGltZSBzdGVwcyJdLFsiT2JzZXJ2YXRpb24iLCJ54oKcID0gSHjigpwgKyB24oKcIiwiSDogbsOXbSwgeTogbsOXMSIsIk1hcHMgbGF0ZW50IHN0YXRlIHRvIG9ic2VydmVkIG1lYXN1cmVtZW50Il0sWyJQcm9jZXNzIG5vaXNlIGNvdiIsIlEgPSBFW3figpx34oKc4bWAXSIsIlE6IG3Dl20gcG9zaXRpdmUgc2VtaWRlZmluaXRlIiwiVW5jZXJ0YWludHkgaW5qZWN0ZWQgaW50byB0aGUgc3RhdGUgZWFjaCBzdGVwIl0sWyJPYnNlcnZhdGlvbiBub2lzZSBjb3YiLCJSID0gRVt24oKcduKCnOG1gF0iLCJSOiBuw5duIHBvc2l0aXZlIGRlZmluaXRlIiwiTWVhc3VyZW1lbnQgZXJyb3IgdmFyaWFuY2UiXSxbIkthbG1hbiBnYWluIiwiS+KCnCA9IFDigpx8dOKCi+KCgUjhtYAoSFDigpx8dOKCi+KCgUjhtYArUinigbvCuSIsIks6IG3Dl24iLCJPcHRpbWFsIHdlaWdodDogaGlnaCBLIHRydXN0cyBvYnMgb3ZlciBwcmVkaWN0aW9uIl0sWyJJbm5vdmF0aW9uIiwiZeKCnCA9IHnigpwg4oiSIEh4zILigpx8dOKCi+KCgSIsImU6IG7DlzEiLCJSZXNpZHVhbCBiZXR3ZWVuIHByZWRpY3RlZCBhbmQgYWN0dWFsIG9ic2VydmF0aW9uIl0sWyJTdGF0ZSB1cGRhdGUiLCJ4zILigpx8dCA9IHjMguKCnHx04oKL4oKBICsgS+KCnGXigpwiLCJ4zII6IG3DlzEiLCJQb3N0ZXJpb3IgbWVhbiBvZiBzdGF0ZSBnaXZlbiBhbGwgb2JzZXJ2YXRpb25zIHVwIHRvIHQiXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# State Space Models and the Kalman Filter

State space models (SSMs) provide a general framework for time-series modelling by separating the observed measurements from an underlying latent state that evolves over time. Any ARIMA model can be written in state space form, but SSMs are strictly more general: they can incorporate time-varying parameters, multiple observation equations, missing data, and structural components (trend, seasonal, regression) that change smoothly over time. The Kalman filter gives the optimal linear update rule for tracking the latent state.

## State Space Formulation

The linear Gaussian state space model consists of two equations. The state (transition) equation xₜ = Fxₜ₋₁ + Bwₜ describes how the hidden state xₜ ∈ ℝᵐ evolves with state transition matrix F ∈ ℝᵐˣᵐ and process noise wₜ ~ N(0, Q). The observation equation yₜ = Hxₜ + vₜ links the state to the observed measurement yₜ ∈ ℝⁿ via observation matrix H ∈ ℝⁿˣᵐ and observation noise vₜ ~ N(0, R). The matrices F, H, Q, R may be time-varying but are assumed known for filtering; they are estimated by MLE during training.

- State vector xₜ: encodes the latent quantities driving the observations (level, trend, seasonal factors, etc.).
- F (transition matrix): governs how the state evolves — identity for random walk, rotation matrix for seasonal cycle.
- Q (process noise covariance): controls how rapidly the state can change — large Q = rapidly evolving components.
- H (observation matrix): selects which components of the state are observed — often [1, 0, 0, …].
- R (observation noise covariance): represents measurement error or idiosyncratic noise in the observations.
- Initial conditions: x₀|₀ ~ N(m₀, P₀) — prior on the state before seeing any data.

## The Kalman Filter — Predict and Update

The Kalman filter computes the optimal (minimum mean squared error) linear estimate of the state given all past observations. It alternates two steps. Predict: x̂ₜ|t₋₁ = Fx̂ₜ₋₁|t₋₁ (state prediction), Pₜ|t₋₁ = FPₜ₋₁|t₋₁Fᵀ + Q (uncertainty propagation). Update: innovation eₜ = yₜ − Hx̂ₜ|t₋₁, innovation covariance Sₜ = HPₜ|t₋₁Hᵀ + R, Kalman gain Kₜ = Pₜ|t₋₁HᵀSₜ⁻¹, state update x̂ₜ|t = x̂ₜ|t₋₁ + Kₜeₜ, covariance update Pₜ|t = (I − KₜH)Pₜ|t₋₁. The Kalman gain Kₜ balances trust between the state prediction and the new observation, weighting toward the observation when R is small relative to HPH'.

```python
import numpy as np

def kalman_filter(y, F, H, Q, R, m0, P0):
    """Linear Kalman filter. Returns filtered means and covariances."""
    n = len(y)
    m = F.shape[0]
    x_filt = np.zeros((n, m))
    P_filt = np.zeros((n, m, m))
    log_lik = 0.0
    x = m0.copy()
    P = P0.copy()
    for t in range(n):
        # Predict
        x_pred = F @ x
        P_pred = F @ P @ F.T + Q
        # Innovation
        innov = y[t] - H @ x_pred
        S     = H @ P_pred @ H.T + R
        K     = P_pred @ H.T / S[0, 0]  # scalar obs: S is 1x1
        # Update
        x = x_pred + K * innov
        P = (np.eye(m) - K[:, None] * H) @ P_pred
        x_filt[t] = x
        P_filt[t] = P
        log_lik  -= 0.5 * (np.log(2 * np.pi * S[0, 0]) + innov**2 / S[0, 0])
    return x_filt, P_filt, log_lik

# Test on a simple AR(1) in state space form
np.random.seed(0)
n  = 100
y  = np.zeros(n)
for t in range(1, n):
    y[t] = 0.8 * y[t-1] + np.random.randn()
y += 0.5 * np.random.randn(n)  # observation noise

F  = np.array([[0.8]])
H  = np.array([[1.0]])
Q  = np.array([[1.0]])
R  = np.array([[0.25]])
m0 = np.array([0.0])
P0 = np.array([[1.0]])

filt, _, ll = kalman_filter(y, F, H, Q, R, m0, P0)
print(f"Log-likelihood: {ll:.4f}")
print(f"Filter RMSE vs observations: {np.sqrt(np.mean((filt[:,0]-y)**2)):.4f}")
```

## Local Level Model — Trend Filtering

The local level model (LLM) is the simplest SSM: the state xₜ follows a random walk (xₜ = xₜ₋₁ + wₜ, wₜ ~ N(0, σ²_η)) and observations yₜ = xₜ + vₜ, vₜ ~ N(0, σ²_ε). In matrix form F = H = 1, Q = σ²_η, R = σ²_ε. The signal-to-noise ratio q = σ²_η/σ²_ε controls how rapidly the filtered trend tracks the observations: large q means the trend moves quickly (follows each observation), small q means the trend is smooth (ignores noise). The LLM is equivalent to exponential smoothing (EWMA) when the Kalman gain has converged.

```python
import numpy as np

np.random.seed(42)
n = 200

# True slowly-evolving level
level_true = np.cumsum(0.2 * np.random.randn(n))
y = level_true + 3.0 * np.random.randn(n)  # high obs noise

def llm_filter(y, sigma_eta, sigma_eps):
    x, P = 0.0, 1.0
    filtered = np.zeros(n)
    for t in range(n):
        # Predict
        P_pred = P + sigma_eta**2
        # Update
        K = P_pred / (P_pred + sigma_eps**2)
        x = x + K * (y[t] - x)
        P = (1 - K) * P_pred
        filtered[t] = x
    return filtered

print(f"{'sigma_eta':>10s}  {'sigma_eps':>10s}  {'SNR q':>8s}  {'RMSE (vs true level)':>22s}")
print("-" * 58)
for s_eta in [0.1, 0.5, 1.0, 2.0]:
    filt = llm_filter(y, s_eta, 3.0)
    rmse = np.sqrt(np.mean((filt - level_true)**2))
    q    = s_eta**2 / 9.0
    print(f"{s_eta:10.2f}  {3.0:10.2f}  {q:8.4f}  {rmse:22.4f}")
print("Small q -> smooth trend; Large q -> tracks observations closely")
```

## Connection to ARIMA and MLE Estimation

Parameter estimation in SSMs proceeds by maximising the Gaussian log-likelihood L = −½Σ[log(2π|Sₜ|) + eₜᵀSₜ⁻¹eₜ], where eₜ are the Kalman filter innovations and Sₜ their covariance matrices. Because the Kalman filter computes innovations sequentially, this expression is efficiently evaluated in O(n·m³) time. Gradient-based optimisation (L-BFGS, EM algorithm) then finds the MLE estimates of F, Q, H, R.

Every ARIMA(p,d,q) model has an exact state space representation. The state vector encodes the lagged values needed to recursively compute the innovations. This is important for two reasons: the Kalman filter provides a computationally efficient O(n·m³) algorithm to evaluate the Gaussian log-likelihood of any ARIMA model, enabling gradient-based MLE; and the state space form handles missing data naturally — missing observations simply skip the update step (the predict step still runs), allowing estimation even with gaps in the series.

## Structural Time Series with UnobservedComponents

```python
import numpy as np
from statsmodels.tsa.statespace.structural import UnobservedComponents

np.random.seed(7)
n = 200
t = np.arange(n)

# Generate: stochastic level + deterministic slope + seasonal + noise
level   = np.cumsum(0.3 * np.random.randn(n))
slope   = 0.1 * t
season  = 5.0 * np.sin(2 * np.pi * t / 12)
y = level + slope + season + np.random.randn(n)

# Fit local linear trend + stochastic cycle model
model = UnobservedComponents(
    y,
    level='local linear trend',
    seasonal=12,
    stochastic_seasonal=True
)
fit = model.fit(disp=False, method='lbfgs')

print("UnobservedComponents (BSTS-like) fit:")
print(f"  Log-likelihood: {fit.llf:.4f}")
print(f"  AIC:            {fit.aic:.4f}")

# Smoothed components
smoothed = fit.smoother_results
print(f"  Level sigma^2:    {fit.params.get('sigma2.level', 'N/A')}")
print(f"  Seasonal sigma^2: {fit.params.get('sigma2.seasonal', 'N/A')}")
fc = fit.get_forecast(12)
print(f"  12-step MAPE:     N/A (no test set; inspect conf_int for interval width)")
print(fit.summary().tables[1])
```

## Unscented Kalman Filter for Nonlinear Systems

The standard Kalman filter is optimal only for linear Gaussian systems. When the state or observation equations are nonlinear — e.g., xₜ = f(xₜ₋₁) + noise, yₜ = h(xₜ) + noise — the Extended Kalman Filter (EKF) linearises f and h via Jacobians, but this can be inaccurate for highly nonlinear functions. The Unscented Kalman Filter (UKF) instead propagates a small set of deterministically chosen sigma points through the nonlinear functions, capturing the mean and covariance to third order (vs first order for EKF), without computing Jacobians.

```python
import numpy as np

def ukf_1d(y, f, h, Q, R, x0, P0, alpha=1e-3, beta=2.0, kappa=0.0):
    """Minimal scalar-state UKF for demonstration."""
    n_x = 1
    lam = alpha**2 * (n_x + kappa) - n_x
    Wm  = np.array([lam/(n_x+lam), 0.5/(n_x+lam), 0.5/(n_x+lam)])
    Wc  = Wm.copy()
    Wc[0] += (1 - alpha**2 + beta)
    x, P = x0, P0
    filtered = np.zeros(len(y))
    for t in range(len(y)):
        # Sigma points
        spread = np.sqrt((n_x + lam) * P)
        sigmas = np.array([x, x + spread, x - spread])
        # Predict
        sigmas_f = np.array([f(s) for s in sigmas])
        x_p = np.dot(Wm, sigmas_f)
        P_p = np.dot(Wc, (sigmas_f - x_p)**2) + Q
        # Observation sigma points
        sigmas_p = np.array([x_p, x_p + np.sqrt((n_x+lam)*P_p), x_p - np.sqrt((n_x+lam)*P_p)])
        sigmas_h = np.array([h(s) for s in sigmas_p])
        y_p = np.dot(Wm, sigmas_h)
        Pyy = np.dot(Wc, (sigmas_h - y_p)**2) + R
        Pxy = np.dot(Wc, (sigmas_p - x_p) * (sigmas_h - y_p))
        K   = Pxy / Pyy
        x   = x_p + K * (y[t] - y_p)
        P   = P_p - K**2 * Pyy
        filtered[t] = x
    return filtered

np.random.seed(3)
n = 100
true_x = np.cumsum(0.1 * np.random.randn(n))
y = true_x**2 + 0.5 * np.random.randn(n)  # nonlinear observation: h(x)=x^2

filtered = ukf_1d(y, f=lambda x: x, h=lambda x: x**2, Q=0.01, R=0.25, x0=0.0, P0=1.0)
rmse = np.sqrt(np.mean((filtered - true_x)**2))
print(f"UKF RMSE (state estimate vs true x): {rmse:.4f}")
print("UKF handles nonlinear observation h(x)=x^2 without Jacobians")
```

> **When to Use State Space vs ARIMA**: ARIMA is sufficient when the data-generating process is stable, the series is univariate, and you need a fast, interpretable model. Choose a state space / structural model when you need: explicit separation of trend, seasonal, and regression components; time-varying parameters (e.g., seasonality that evolves); missing data handling; incorporation of exogenous regressors into the state; or a Bayesian treatment with prior distributions on variance components (BSTS).

## SSM Component Reference

| Component | Matrix / Equation | Dimensions | Interpretation |
| --- | --- | --- | --- |
| State transition | xₜ = Fxₜ₋₁ + Bwₜ | F: m×m, x: m×1 | How the hidden state evolves across time steps |
| Observation | yₜ = Hxₜ + vₜ | H: n×m, y: n×1 | Maps latent state to observed measurement |
| Process noise cov | Q = E[wₜwₜᵀ] | Q: m×m positive semidefinite | Uncertainty injected into the state each step |
| Observation noise cov | R = E[vₜvₜᵀ] | R: n×n positive definite | Measurement error variance |
| Kalman gain | Kₜ = Pₜ|t₋₁Hᵀ(HPₜ|t₋₁Hᵀ+R)⁻¹ | K: m×n | Optimal weight: high K trusts obs over prediction |
| Innovation | eₜ = yₜ − Hx̂ₜ|t₋₁ | e: n×1 | Residual between predicted and actual observation |
| State update | x̂ₜ|t = x̂ₜ|t₋₁ + Kₜeₜ | x̂: m×1 | Posterior mean of state given all observations up to t |

---

