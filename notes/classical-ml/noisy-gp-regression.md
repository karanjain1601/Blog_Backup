---
title: "Noisy GP Regression — Signal vs Noise Separation"
slug: "noisy-gp-regression"
description: "Observation model y=f(x)+ε, learning noise variance from data, heteroskedastic GPs, and the signal-to-noise ratio diagnostic for diagnosing overfitting vs underfitting."
tags: ["gaussian-processes", "kernel-methods", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBPYnNlcnZhdGlvbiBNb2RlbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gR1AgcmVncmVzc2lvbiB0aGUgb2JzZXJ2YXRpb24gbW9kZWwgaXMgeSh4KSA9IGYoeCkgKyDOtSwgd2hlcmUgZiB+IEdQKG0sIGspIGlzIHRoZSBsYXRlbnQgZnVuY3Rpb24gYW5kIM61IH4gTigwLCDPg8KyX24pIGlzIGluZGVwZW5kZW50IG9ic2VydmF0aW9uIG5vaXNlLiBUaGUgY29tYmluZWQgY292YXJpYW5jZSBvZiBvYnNlcnZhdGlvbnMgYXQgdHdvIGlucHV0cyB4LCB4XHUwMDI3IGlzIGtfeSh4LHhcdTAwMjcpID0ga19mKHgseFx1MDAyNykgKyDPg8KyX24gzrQoeCx4XHUwMDI3KS4gQWRkaW5nIM+DwrJfbiB0byB0aGUgZGlhZ29uYWwgb2YgdGhlIGtlcm5lbCBtYXRyaXggSyBoYXMgdHdvIGVmZmVjdHM6IGl0IHNtb290aHMgdGhlIHBvc3RlcmlvciBtZWFuIChkb2VzIG5vdCBpbnRlcnBvbGF0ZSBleGFjdGx5KSBhbmQgaXQgc3RhYmlsaXNlcyB0aGUgbWF0cml4IGludmVyc2lvbiBudW1lcmljYWxseSAoaW1wcm92ZXMgY29uZGl0aW9uIG51bWJlcikuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMYXRlbnQgZnVuY3Rpb24gZiB+IEdQKG0sIGspOiB0aGUgdHJ1ZSB1bmRlcmx5aW5nIHNpZ25hbCBiZWluZyBlc3RpbWF0ZWQiLCJPYnNlcnZhdGlvbiBub2lzZSDOtSB+IE4oMCwgz4PCsl9uKTogaW5kZXBlbmRlbnQgcGVyLW9ic2VydmF0aW9uIG1lYXN1cmVtZW50IGVycm9yIiwiQ29tYmluZWQgb2JzZXJ2YXRpb24gY292YXJpYW5jZTogS195ID0gS19mICsgz4PCsl9uIEkgKG5vaXNlIG9uIGRpYWdvbmFsIG9ubHkpIiwiz4PCsl9uIFx1MDAzZSAwOiBzbW9vdGhlZCBwb3N0ZXJpb3IsIGltcHJvdmVkIG51bWVyaWNhbCBjb25kaXRpb25pbmciLCLPg8KyX24gPSAwOiBleGFjdCBpbnRlcnBvbGF0aW9uLCBudW1lcmljYWxseSBmcmFnaWxlIOKAlCBhbHdheXMgYWRkIGF0IGxlYXN0IGEgaml0dGVyIiwiU2lnbmFsLXRvLU5vaXNlIFJhdGlvIChTTlIpID0gz4PCsl9mIC8gz4PCsl9uIOKAlCBrZXkgbW9kZWwgaGVhbHRoIGRpYWdub3N0aWMiXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJOb2lzZSB2cyBKaXR0ZXIg4oCUIFR3byBEaXN0aW5jdCBSb2xlcyIsImNvbnRlbnQiOiJPYnNlcnZhdGlvbiBub2lzZSDPg8KyX24gaXMgYSBtb2RlbGxpbmcgY2hvaWNlIHRoYXQgcmVmbGVjdHMgcmVhbCBtZWFzdXJlbWVudCB1bmNlcnRhaW50eS4gSml0dGVyICh0eXBpY2FsbHkgMWUtNikgaXMgYSBwdXJlIG51bWVyaWNhbCBkZXZpY2UgYWRkZWQgdG8gZ3VhcmFudGVlIHBvc2l0aXZlIGRlZmluaXRlbmVzcyByZWdhcmRsZXNzIG9mIM+DwrJfbi4gV2hlbiDPg8KyX24gaXMgYWxyZWFkeSBsYXJnZSwgaml0dGVyIGlzIGlycmVsZXZhbnQ7IGZvciBub2lzZWxlc3MgbW9kZWxzIM+DwrJfbj0wIHRoZSBqaXR0ZXIgYmVjb21lcyBjcml0aWNhbC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOb2lzeSB2cyBOb2lzZWxlc3MgUG9zdGVyaW9yIEJlaGF2aW91ciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2l0aCBub2lzZSDPg8KyX24gXHUwMDNlIDA6IHBvc3RlcmlvciBtZWFuIGlzIGEgc21vb3RoZWQgZXN0aW1hdGUgb2YgZiB0aGF0IGRvZXMgbm90IHBhc3MgdGhyb3VnaCBvYnNlcnZhdGlvbnM7IHBvc3RlcmlvciB2YXJpYW5jZSBhdCB0cmFpbmluZyBpbnB1dHMgaXMgcG9zaXRpdmUgKOKJiCDPg8KyX24gZm9yIHdlbGwtZml0dGVkIG1vZGVscykuIFdpdGggbm9pc2Ugz4PCsl9uID0gMCAob3IgdmVyeSBzbWFsbCBqaXR0ZXIpOiBwb3N0ZXJpb3IgaXMgYW4gZXhhY3QgaW50ZXJwb2xhbnQgdGhyb3VnaCB0cmFpbmluZyBwb2ludHM7IHBvc3RlcmlvciB2YXJpYW5jZSBpcyAwIGF0IHRyYWluaW5nIGlucHV0cy4gTm9pc2VsZXNzIG1vZGVscyBhcmUgYXBwcm9wcmlhdGUgb25seSBmb3IgZGV0ZXJtaW5pc3RpYyBzaW11bGF0b3JzIG9yIGNvbXB1dGVyIGV4cGVyaW1lbnRzIHdoZXJlIG9ic2VydmF0aW9ucyBjYXJyeSBubyBtZWFzdXJlbWVudCBlcnJvci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgZWxsPTEuMCwgc2YyPTEuMCk6XG4gICAgWDEgPSBucC5hdGxlYXN0XzJkKFgxKS5yZXNoYXBlKC0xLDEpXG4gICAgWDIgPSBucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLDEpXG4gICAgcmV0dXJuIHNmMiAqIG5wLmV4cCgtMC41KihYMS1YMi5UKSoqMi9lbGwqKjIpXG5cbmRlZiBncF9wcmVkaWN0KFhfdHIsIHlfdHIsIFhfdGUsIGVsbCwgc2YyLCBzbjIpOlxuICAgIG4gPSBsZW4oWF90cilcbiAgICBLICAgID0gcmJmX2tlcm5lbChYX3RyLCBYX3RyLCBlbGwsIHNmMikgKyBzbjIqbnAuZXllKG4pXG4gICAgS19zICA9IHJiZl9rZXJuZWwoWF90ciwgWF90ZSwgZWxsLCBzZjIpXG4gICAgS19zcyA9IHJiZl9rZXJuZWwoWF90ZSwgWF90ZSwgZWxsLCBzZjIpXG4gICAgTCAgICA9IG5wLmxpbmFsZy5jaG9sZXNreShLKVxuICAgIGFscGhhID0gbnAubGluYWxnLnNvbHZlKEwuVCwgbnAubGluYWxnLnNvbHZlKEwsIHlfdHIpKVxuICAgIG11ICAgPSBLX3MuVCBAIGFscGhhXG4gICAgdiAgICA9IG5wLmxpbmFsZy5zb2x2ZShMLCBLX3MpXG4gICAgdmFyICA9IG5wLm1heGltdW0obnAuZGlhZyhLX3NzIC0gdi5UQHYpLCAwKVxuICAgIHJldHVybiBtdSwgbnAuc3FydCh2YXIpXG5cbm5wLnJhbmRvbS5zZWVkKDEpXG5YX3RyID0gbnAuc29ydChucC5yYW5kb20udW5pZm9ybSgtNCw0LDEyKSlcbnlfdHIgPSBucC5zaW4oWF90cikgKyAwLjQqbnAucmFuZG9tLnJhbmRuKDEyKVxuWF90ZSA9IG5wLmxpbnNwYWNlKC01LCA1LCAzMDApXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMyw0KSwgc2hhcmV5PVRydWUpXG5mb3IgYXgsIHNuMiwgbGJsIGluIHppcChheGVzLCBbMWUtNiwgMC4zXSxcbiAgICBbXHUwMDI3Tm9pc2VsZXNzICjPg8KyX249MCkg4oCUIGludGVycG9sYXRpb25cdTAwMjcsIFx1MDAyN05vaXN5ICjPg8KyX249MC4zKSDigJQgc21vb3RoaW5nXHUwMDI3XSk6XG4gICAgbXUsIHN0ZCA9IGdwX3ByZWRpY3QoWF90ciwgeV90ciwgWF90ZSwgZWxsPTEuMCwgc2YyPTEuMCwgc24yPXNuMilcbiAgICBheC5maWxsX2JldHdlZW4oWF90ZSwgbXUtMipzdGQsIG11KzIqc3RkLCBhbHBoYT0wLjI1KVxuICAgIGF4LnBsb3QoWF90ZSwgbXUsIGx3PTIpXG4gICAgYXguc2NhdHRlcihYX3RyLCB5X3RyLCBjPVx1MDAyN3JcdTAwMjcsIHpvcmRlcj01LCBzPTYwKVxuICAgIGF4LnNldF90aXRsZShsYmwpOyBheC5zZXRfeGxhYmVsKFx1MDAyN3hcdTAwMjcpXG5heGVzWzBdLnNldF95bGFiZWwoXHUwMDI3eVx1MDAyNyk7IHBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIk5vaXNlbGVzcyBHUCAoz4NfbuKJiDApIiwiTm9pc3kgR1AgKM+DX25cdTAwM2UwKSJdLCJyb3dzIjpbWyJQYXNzZXMgdGhyb3VnaCB0cmFpbmluZyBkYXRhIiwiWWVzIOKAlCBleGFjdCBpbnRlcnBvbGF0aW9uIiwiTm8g4oCUIHNtb290aCBmaXQiXSxbIlBvc3RlcmlvciB2YXJpYW5jZSBhdCBYX3RyYWluIiwiMCIsIkFwcHJveCDPg8KyX24iXSxbIk51bWVyaWNhbCBzdGFiaWxpdHkiLCJQb29yIChuZWFybHkgc2luZ3VsYXIgSykiLCJHb29kIChkaWFnb25hbCByZWd1bGFyaXNhdGlvbikiXSxbIlVzZSBjYXNlIiwiRGV0ZXJtaW5pc3RpYyBzaW11bGF0b3JzLCBleGFjdCBkYXRhIiwiUmVhbC13b3JsZCBzZW5zb3IvbWVhc3VyZW1lbnQgZGF0YSJdLFsiTWFyZ2luYWwgbGlrZWxpaG9vZCIsIlRlbmRzIHRvIG92ZXJmaXQgKHNoYXJwIHBlYWspIiwiQmFsYW5jZWQgZml0LWNvbXBsZXhpdHkgdHJhZGUtb2ZmIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMZWFybmluZyBOb2lzZSBMZXZlbCBmcm9tIERhdGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBub2lzZSB2YXJpYW5jZSDPg8KyX24gc2hvdWxkIGJlIGxlYXJuZWQgZnJvbSBkYXRhIHZpYSBtYXJnaW5hbCBsaWtlbGlob29kIG9wdGltaXNhdGlvbiByYXRoZXIgdGhhbiBzZXQgYnkgaGFuZC4gVGhlIG1hcmdpbmFsIGxpa2VsaWhvb2QgYXV0b21hdGljYWxseSBhc3NpZ25zIGEgbm9pc2UgbGV2ZWwgY29uc2lzdGVudCB3aXRoIHRoZSBvYnNlcnZlZCBzY2F0dGVyLiBJZiDPg8KyX24gaXMgdG9vIHNtYWxsLCB0aGUgbW9kZWwgaW50ZXJwb2xhdGVzIGFuZCBvdmVyZml0czsgaWYgdG9vIGxhcmdlLCB0aGUgbWVhbiBmdW5jdGlvbiBpcyBvdmVyLXNtb290aGVkLiBUaGUgbGVhcm5lZCBTTlIgPSDPg8KyX2YgLyDPg8KyX24gcHJvdmlkZXMgYSB1c2VmdWwgZGlhZ25vc3RpYzogU05SIFx1MDAzYyAxIG1lYW5zIHRoZSBtb2RlbCBzZWVzIG1vcmUgbm9pc2UgdGhhbiBzaWduYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5vcHRpbWl6ZSBpbXBvcnQgbWluaW1pemVcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBlbGwsIHNmMik6XG4gICAgWDEgPSBucC5hdGxlYXN0XzJkKFgxKS5yZXNoYXBlKC0xLDEpXG4gICAgWDIgPSBucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLDEpXG4gICAgcmV0dXJuIHNmMiAqIG5wLmV4cCgtMC41KihYMS1YMi5UKSoqMi9lbGwqKjIpXG5cbmRlZiBuZWdfbG1sKHBhcmFtcywgWCwgeSk6XG4gICAgZWxsLCBzZjIsIHNuMiA9IG5wLmV4cChwYXJhbXMpXG4gICAgbiA9IGxlbih5KVxuICAgIEsgPSByYmZfa2VybmVsKFgsIFgsIGVsbCwgc2YyKSArIHNuMipucC5leWUobilcbiAgICB0cnk6XG4gICAgICAgIEwgPSBucC5saW5hbGcuY2hvbGVza3koSylcbiAgICAgICAgYWxwaGEgPSBucC5saW5hbGcuc29sdmUoTC5ULCBucC5saW5hbGcuc29sdmUoTCwgeSkpXG4gICAgICAgIHJldHVybiAwLjUqKHlAYWxwaGEpICsgbnAuc3VtKG5wLmxvZyhucC5kaWFnKEwpKSkgKyAwLjUqbipucC5sb2coMipucC5waSlcbiAgICBleGNlcHQgRXhjZXB0aW9uOlxuICAgICAgICByZXR1cm4gMWUxMFxuXG5ucC5yYW5kb20uc2VlZCg3KVxuWCA9IG5wLnNvcnQobnAucmFuZG9tLnVuaWZvcm0oLTUsNSw2MCkpXG50cnVlX3Nucl9zY2VuYXJpbyA9IHtcdTAwMjdsb3dfbm9pc2VcdTAwMjc6IDAuMSwgXHUwMDI3aGlnaF9ub2lzZVx1MDAyNzogMS4wfVxuZm9yIHNjZW5hcmlvLCBzbiBpbiB0cnVlX3Nucl9zY2VuYXJpby5pdGVtcygpOlxuICAgIHkgPSBucC5zaW4oWCkgKyBzbipucC5yYW5kb20ucmFuZG4oNjApXG4gICAgcmVzID0gbWluaW1pemUobmVnX2xtbCwgWzAsMCwtMl0sIGFyZ3M9KFgseSksIG1ldGhvZD1cdTAwMjdMLUJGR1MtQlx1MDAyNylcbiAgICBlbGwsIHNmMiwgc24yID0gbnAuZXhwKHJlcy54KVxuICAgIHByaW50KGZcdTAwMjd7c2NlbmFyaW99OiDihJM9e2VsbDouM2Z9LCDPg8KyX2Y9e3NmMjouM2Z9LCDPg8KyX249e3NuMjouNGZ9LCBTTlI9e3NmMi9zbjI6LjJmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IlNOUiBhcyBhIE1vZGVsIEhlYWx0aCBEaWFnbm9zdGljIiwiY29udGVudCI6IkFmdGVyIG9wdGltaXNhdGlvbiwgY29tcHV0ZSBTTlIgPSDPg8KyX2YgLyDPg8KyX24uIFNOUiBcdTAwM2VcdTAwM2UgMSAoZS5nLiwgMTArKTogbW9kZWwgaXMgZG9taW5hdGVkIGJ5IHNpZ25hbCDigJQgY2hlY2sgZm9yIG92ZXJmaXR0aW5nIGlmIHRoZSBwb3N0ZXJpb3IgZml0cyB0cmFpbmluZyBkYXRhIHRvbyB0aWdodGx5LiBTTlIg4omIIDE6IHNpZ25hbCBhbmQgbm9pc2UgYXJlIGNvbXBhcmFibGUg4oCUIHR5cGljYWwgZm9yIHJlYWwtd29ybGQgZGF0YS4gU05SIFx1MDAzY1x1MDAzYyAxOiBub2lzZSBkb21pbmF0ZXMg4oCUIGRhdGEgbWF5IGJlIHRvbyBub2lzeSBmb3IgdGhlIG1vZGVsIHRvIGV4dHJhY3Qgc2lnbmFsLCBvciBsZW5ndGgtc2NhbGUgaXMgbWlzY29uZmlndXJlZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIZXRlcm9za2VkYXN0aWMgR1Ag4oCUIElucHV0LURlcGVuZGVudCBOb2lzZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSG9tb3NrZWRhc3RpYyBHUHMgYXNzdW1lIGNvbnN0YW50IM+DwrJfbiBldmVyeXdoZXJlLiBSZWFsIHNpZ25hbHMgb2Z0ZW4gaGF2ZSBpbnB1dC1kZXBlbmRlbnQgbm9pc2UgKGhldGVyb3NrZWRhc3RpY2l0eSkg4oCUIGUuZy4sIG1lYXN1cmVtZW50IHVuY2VydGFpbnR5IHZhcmllcyB3aXRoIHNlbnNvciBsb2FkLCBvciBmaW5hbmNpYWwgdm9sYXRpbGl0eSBjbHVzdGVycyBpbiB0aW1lLiBIZXRlcm9za2VkYXN0aWMgR1BzIG1vZGVsIHRoZSBub2lzZSBhcyBhIGZ1bmN0aW9uIG9mIHgsIG9mdGVuIGJ5IHBsYWNpbmcgYSBzZWNvbmQgR1Agb3ZlciBsb2cgz4PCsl9uKHgpIG9yIGJ5IHVzaW5nIGEgd2FycGVkIGxpa2VsaWhvb2QuIEEgc2ltcGxlIGFwcHJveGltYXRpb246IGJpbm5lZCBub2lzZSBlc3RpbWF0aW9uIGZvbGxvd2VkIGJ5IGEgZml4ZWQgZGlhZ29uYWwgbm9pc2UgbWF0cml4LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBlbGw9MS4wLCBzZjI9MS4wKTpcbiAgICBYMSA9IG5wLmF0bGVhc3RfMmQoWDEpLnJlc2hhcGUoLTEsMSlcbiAgICBYMiA9IG5wLmF0bGVhc3RfMmQoWDIpLnJlc2hhcGUoLTEsMSlcbiAgICByZXR1cm4gc2YyICogbnAuZXhwKC0wLjUqKFgxLVgyLlQpKioyL2VsbCoqMilcblxubnAucmFuZG9tLnNlZWQoNClcblhfdHIgPSBucC5zb3J0KG5wLnJhbmRvbS51bmlmb3JtKC01LDUsNjApKVxuIyBOb2lzZSBncm93cyB3aXRoIHx4fFxubm9pc2Vfc3RkID0gMC4xICsgMC4zKm5wLmFicyhYX3RyKVxueV90ciA9IG5wLnNpbihYX3RyKSArIG5vaXNlX3N0ZCpucC5yYW5kb20ucmFuZG4oNjApXG5cblhfdGUgPSBucC5saW5zcGFjZSgtNiw2LDMwMClcblxuZGVmIGdwX2hldGVybyhYX3RyLCB5X3RyLCBYX3RlLCBub2lzZV92ZWMsIGVsbD0xLjUsIHNmMj0xLjApOlxuICAgIEsgICAgPSByYmZfa2VybmVsKFhfdHIsWF90cixlbGwsc2YyKSArIG5wLmRpYWcobm9pc2VfdmVjKioyKVxuICAgIEtfcyAgPSByYmZfa2VybmVsKFhfdHIsWF90ZSxlbGwsc2YyKVxuICAgIEtfc3MgPSByYmZfa2VybmVsKFhfdGUsWF90ZSxlbGwsc2YyKVxuICAgIEwgICAgPSBucC5saW5hbGcuY2hvbGVza3koSylcbiAgICBhbHBoYSA9IG5wLmxpbmFsZy5zb2x2ZShMLlQsbnAubGluYWxnLnNvbHZlKEwseV90cikpXG4gICAgbXUgICA9IEtfcy5UQGFscGhhXG4gICAgdiAgICA9IG5wLmxpbmFsZy5zb2x2ZShMLEtfcylcbiAgICByZXR1cm4gbXUsIG5wLnNxcnQobnAubWF4aW11bShucC5kaWFnKEtfc3Mtdi5UQHYpLDApKVxuXG5tdSwgc3RkID0gZ3BfaGV0ZXJvKFhfdHIsIHlfdHIsIFhfdGUsIG5vaXNlX3N0ZClcbnBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsNCkpXG5wbHQuZmlsbF9iZXR3ZWVuKFhfdGUsbXUtMipzdGQsbXUrMipzdGQsYWxwaGE9MC4yNSxsYWJlbD1cdTAwMjfCsTLPgyAoaG9tb3NrZWRhc3RpYyBwb3N0LilcdTAwMjcpXG5wbHQucGxvdChYX3RlLCBtdSwgbHc9MiwgbGFiZWw9XHUwMDI3UG9zdGVyaW9yIG1lYW5cdTAwMjcpXG5wbHQuZXJyb3JiYXIoWF90ciwgeV90ciwgeWVycj0yKm5vaXNlX3N0ZCwgZm10PVx1MDAyN3IuXHUwMDI3LCBhbHBoYT0wLjQsIG1zPTQsIGxhYmVsPVx1MDAyN09icyDCsTLPg19uKHgpXHUwMDI3KVxucGx0LnRpdGxlKFx1MDAyN0hldGVyb3NrZWRhc3RpYyBHUCAoa25vd24gaW5wdXQtZGVwZW5kZW50IG5vaXNlKVx1MDAyNylcbnBsdC54bGFiZWwoXHUwMDI3eFx1MDAyNyk7IHBsdC55bGFiZWwoXHUwMDI3eVx1MDAyNyk7IHBsdC5sZWdlbmQoKTsgcGx0LnRpZ2h0X2xheW91dCgpOyBwbHQuc2hvdygpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTW9kZWwgU2VsZWN0aW9uIHZpYSBNYXJnaW5hbCBMaWtlbGlob29kIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbG9nIG1hcmdpbmFsIGxpa2VsaWhvb2QgY2FuIGNvbXBhcmUgZGlmZmVyZW50IG5vaXNlIGFzc3VtcHRpb25zIHdpdGhvdXQgYSBoZWxkLW91dCBzZXQuIE1vZGVscyB3aXRoIHVucmVhbGlzdGljYWxseSBzbWFsbCDPg8KyX24gd2lsbCBoYXZlIGhpZ2ggZGF0YS1maXQgYnV0IGEgbGFyZ2UgY29tcGxleGl0eSBwZW5hbHR5IGZyb20gdGhlIGFsbW9zdC1zaW5ndWxhciBrZXJuZWwgbWF0cml4OyB0aGUgbWFyZ2luYWwgbGlrZWxpaG9vZCBwZW5hbGlzZXMgdGhpcy4gQ29tcGFyaW5nIExNTCB2YWx1ZXMgYWNyb3NzIG1vZGVsIHZhcmlhbnRzIChkaWZmZXJlbnQga2VybmVscywgZGlmZmVyZW50IG5vaXNlIG1vZGVscykgaW1wbGVtZW50cyBmb3JtYWwgQmF5ZXNpYW4gbW9kZWwgc2VsZWN0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgZWxsLCBzZjIpOlxuICAgIFgxPW5wLmF0bGVhc3RfMmQoWDEpLnJlc2hhcGUoLTEsMSk7IFgyPW5wLmF0bGVhc3RfMmQoWDIpLnJlc2hhcGUoLTEsMSlcbiAgICByZXR1cm4gc2YyKm5wLmV4cCgtMC41KihYMS1YMi5UKSoqMi9lbGwqKjIpXG5cbmRlZiBmaXRfYW5kX3Njb3JlKFgsIHksIGZpeGVkX3NuMj1Ob25lKTpcbiAgICBkZWYgbmVnX2xtbChwYXJhbXMpOlxuICAgICAgICBpZiBmaXhlZF9zbjIgaXMgTm9uZTpcbiAgICAgICAgICAgIGVsbCxzZjIsc24yID0gbnAuZXhwKHBhcmFtcylcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIGVsbCxzZjIgPSBucC5leHAocGFyYW1zKTsgc24yID0gZml4ZWRfc24yXG4gICAgICAgIG4gPSBsZW4oeSk7IEsgPSByYmZfa2VybmVsKFgsWCxlbGwsc2YyKStzbjIqbnAuZXllKG4pXG4gICAgICAgIHRyeTpcbiAgICAgICAgICAgIEw9bnAubGluYWxnLmNob2xlc2t5KEspOyBhPW5wLmxpbmFsZy5zb2x2ZShMLlQsbnAubGluYWxnLnNvbHZlKEwseSkpXG4gICAgICAgICAgICByZXR1cm4gMC41Kih5QGEpK25wLnN1bShucC5sb2cobnAuZGlhZyhMKSkpKzAuNSpuKm5wLmxvZygyKm5wLnBpKVxuICAgICAgICBleGNlcHQ6IHJldHVybiAxZTEwXG4gICAgbl9wYXJhbXMgPSAyIGlmIGZpeGVkX3NuMiBlbHNlIDNcbiAgICB4MCA9IG5wLnplcm9zKG5fcGFyYW1zKVxuICAgIHJlcyA9IG1pbmltaXplKG5lZ19sbWwsIHgwLCBtZXRob2Q9XHUwMDI3TC1CRkdTLUJcdTAwMjcpXG4gICAgcmV0dXJuIC1yZXMuZnVuXG5cbm5wLnJhbmRvbS5zZWVkKDk5KVxuWCA9IG5wLnNvcnQobnAucmFuZG9tLnVuaWZvcm0oLTUsNSw1MCkpXG55ID0gbnAuc2luKFgpKzAuMipucC5yYW5kb20ucmFuZG4oNTApXG5mb3IgbGFiZWwsIHNuIGluIFsoXHUwMDI3SW50ZXJwb2xhdGluZyAoz4Nfbj0xZS00KVx1MDAyNywxZS00KSxcbiAgICAgICAgICAgICAgICAgIChcdTAwMjdMZWFybmVkIG5vaXNlXHUwMDI3LCBOb25lKSxcbiAgICAgICAgICAgICAgICAgIChcdTAwMjdPdmVyLXNtb290aGVkICjPg19uPTIuMClcdTAwMjcsMi4wKV06XG4gICAgbG1sID0gZml0X2FuZF9zY29yZShYLCB5LCBmaXhlZF9zbjI9c24gaWYgc24gZWxzZSBOb25lKVxuICAgIHByaW50KGZcdTAwMjd7bGFiZWw6XHUwMDNjMzVzfTogTE1MID0ge2xtbDouMmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvYnNlcnZhdGlvbiBtb2RlbCB5ID0gZih4KSArIM61IHNlcGFyYXRlcyB0aGUgbGF0ZW50IHNpZ25hbCBmIGZyb20gbWVhc3VyZW1lbnQgbm9pc2UgzrUgfiBOKDAsIM+DwrJfbikuIEFkZGluZyDPg8KyX24gdG8gdGhlIGRpYWdvbmFsIG9mIEsgcmVndWxhcmlzZXMgdGhlIG1hdHJpeCAobnVtZXJpY2FsIHN0YWJpbGl0eSkgYW5kIHByb2R1Y2VzIGEgc21vb3RoZWQgcG9zdGVyaW9yIG1lYW4gcmF0aGVyIHRoYW4gZXhhY3QgaW50ZXJwb2xhdGlvbi4gVGhlIG5vaXNlIGxldmVsIGlzIGJlc3QgbGVhcm5lZCB2aWEgbWFyZ2luYWwgbGlrZWxpaG9vZCBvcHRpbWlzYXRpb24uIFNOUiA9IM+DwrJfZi/Pg8KyX24gaXMgYSB1c2VmdWwgaGVhbHRoIGRpYWdub3N0aWMuIEhldGVyb3NrZWRhc3RpYyBleHRlbnNpb25zIG1vZGVsIGlucHV0LWRlcGVuZGVudCBub2lzZSB2aWEgYSBzZWNvbmQgR1Agb3ZlciBsb2cgbm9pc2UuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyLPg8KyX24gb24gSyBkaWFnb25hbDogbnVtZXJpY2FsIHN0YWJpbGl0eSArIHNtb290aGVkIHBvc3RlcmlvciIsIk5vaXNlbGVzcyBHUCAoz4PCsl9uPTApOiBpbnRlcnBvbGF0aW9uLCBhcHByb3ByaWF0ZSBvbmx5IGZvciBkZXRlcm1pbmlzdGljIHNpbXVsYXRvcnMiLCJMZWFybiDPg8KyX24gZnJvbSBtYXJnaW5hbCBsaWtlbGlob29kIOKAlCBub3QgY3Jvc3MtdmFsaWRhdGlvbiIsIlNOUiA9IM+DwrJfZi/Pg8KyX246IGhpZ2gg4oaSIHNpZ25hbC1kb21pbmF0ZWQ7IGxvdyDihpIgbm9pc2UtZG9taW5hdGVkIiwiSGV0ZXJvc2tlZGFzdGljIEdQOiBtb2RlbCDPg8KyX24oeCkgYXMgYSBmdW5jdGlvbiBvZiBpbnB1dCBmb3Igbm9uLWNvbnN0YW50IG5vaXNlIiwiTWFyZ2luYWwgbGlrZWxpaG9vZCBmb3JtYWxseSBjb21wYXJlcyBub2lzZSBtb2RlbHMgd2l0aG91dCBoZWxkLW91dCBkYXRhIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Noisy GP Regression — Signal vs Noise Separation

## The Observation Model

In GP regression the observation model is y(x) = f(x) + ε, where f ~ GP(m, k) is the latent function and ε ~ N(0, σ²_n) is independent observation noise. The combined covariance of observations at two inputs x, x' is k_y(x,x') = k_f(x,x') + σ²_n δ(x,x'). Adding σ²_n to the diagonal of the kernel matrix K has two effects: it smooths the posterior mean (does not interpolate exactly) and it stabilises the matrix inversion numerically (improves condition number).

- Latent function f ~ GP(m, k): the true underlying signal being estimated
- Observation noise ε ~ N(0, σ²_n): independent per-observation measurement error
- Combined observation covariance: K_y = K_f + σ²_n I (noise on diagonal only)
- σ²_n > 0: smoothed posterior, improved numerical conditioning
- σ²_n = 0: exact interpolation, numerically fragile — always add at least a jitter
- Signal-to-Noise Ratio (SNR) = σ²_f / σ²_n — key model health diagnostic

> **Noise vs Jitter — Two Distinct Roles**: Observation noise σ²_n is a modelling choice that reflects real measurement uncertainty. Jitter (typically 1e-6) is a pure numerical device added to guarantee positive definiteness regardless of σ²_n. When σ²_n is already large, jitter is irrelevant; for noiseless models σ²_n=0 the jitter becomes critical.

## Noisy vs Noiseless Posterior Behaviour

With noise σ²_n > 0: posterior mean is a smoothed estimate of f that does not pass through observations; posterior variance at training inputs is positive (≈ σ²_n for well-fitted models). With noise σ²_n = 0 (or very small jitter): posterior is an exact interpolant through training points; posterior variance is 0 at training inputs. Noiseless models are appropriate only for deterministic simulators or computer experiments where observations carry no measurement error.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1-X2.T)**2/ell**2)

def gp_predict(X_tr, y_tr, X_te, ell, sf2, sn2):
    n = len(X_tr)
    K    = rbf_kernel(X_tr, X_tr, ell, sf2) + sn2*np.eye(n)
    K_s  = rbf_kernel(X_tr, X_te, ell, sf2)
    K_ss = rbf_kernel(X_te, X_te, ell, sf2)
    L    = np.linalg.cholesky(K)
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, y_tr))
    mu   = K_s.T @ alpha
    v    = np.linalg.solve(L, K_s)
    var  = np.maximum(np.diag(K_ss - v.T@v), 0)
    return mu, np.sqrt(var)

np.random.seed(1)
X_tr = np.sort(np.random.uniform(-4,4,12))
y_tr = np.sin(X_tr) + 0.4*np.random.randn(12)
X_te = np.linspace(-5, 5, 300)

fig, axes = plt.subplots(1, 2, figsize=(13,4), sharey=True)
for ax, sn2, lbl in zip(axes, [1e-6, 0.3],
    ['Noiseless (σ²_n=0) — interpolation', 'Noisy (σ²_n=0.3) — smoothing']):
    mu, std = gp_predict(X_tr, y_tr, X_te, ell=1.0, sf2=1.0, sn2=sn2)
    ax.fill_between(X_te, mu-2*std, mu+2*std, alpha=0.25)
    ax.plot(X_te, mu, lw=2)
    ax.scatter(X_tr, y_tr, c='r', zorder=5, s=60)
    ax.set_title(lbl); ax.set_xlabel('x')
axes[0].set_ylabel('y'); plt.tight_layout(); plt.show()
```

| Property | Noiseless GP (σ_n≈0) | Noisy GP (σ_n>0) |
| --- | --- | --- |
| Passes through training data | Yes — exact interpolation | No — smooth fit |
| Posterior variance at X_train | 0 | Approx σ²_n |
| Numerical stability | Poor (nearly singular K) | Good (diagonal regularisation) |
| Use case | Deterministic simulators, exact data | Real-world sensor/measurement data |
| Marginal likelihood | Tends to overfit (sharp peak) | Balanced fit-complexity trade-off |

## Learning Noise Level from Data

The noise variance σ²_n should be learned from data via marginal likelihood optimisation rather than set by hand. The marginal likelihood automatically assigns a noise level consistent with the observed scatter. If σ²_n is too small, the model interpolates and overfits; if too large, the mean function is over-smoothed. The learned SNR = σ²_f / σ²_n provides a useful diagnostic: SNR < 1 means the model sees more noise than signal.

```python
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell, sf2):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1-X2.T)**2/ell**2)

def neg_lml(params, X, y):
    ell, sf2, sn2 = np.exp(params)
    n = len(y)
    K = rbf_kernel(X, X, ell, sf2) + sn2*np.eye(n)
    try:
        L = np.linalg.cholesky(K)
        alpha = np.linalg.solve(L.T, np.linalg.solve(L, y))
        return 0.5*(y@alpha) + np.sum(np.log(np.diag(L))) + 0.5*n*np.log(2*np.pi)
    except Exception:
        return 1e10

np.random.seed(7)
X = np.sort(np.random.uniform(-5,5,60))
true_snr_scenario = {'low_noise': 0.1, 'high_noise': 1.0}
for scenario, sn in true_snr_scenario.items():
    y = np.sin(X) + sn*np.random.randn(60)
    res = minimize(neg_lml, [0,0,-2], args=(X,y), method='L-BFGS-B')
    ell, sf2, sn2 = np.exp(res.x)
    print(f'{scenario}: ℓ={ell:.3f}, σ²_f={sf2:.3f}, σ²_n={sn2:.4f}, SNR={sf2/sn2:.2f}')
```

> **SNR as a Model Health Diagnostic**: After optimisation, compute SNR = σ²_f / σ²_n. SNR >> 1 (e.g., 10+): model is dominated by signal — check for overfitting if the posterior fits training data too tightly. SNR ≈ 1: signal and noise are comparable — typical for real-world data. SNR << 1: noise dominates — data may be too noisy for the model to extract signal, or length-scale is misconfigured.

## Heteroskedastic GP — Input-Dependent Noise

Homoskedastic GPs assume constant σ²_n everywhere. Real signals often have input-dependent noise (heteroskedasticity) — e.g., measurement uncertainty varies with sensor load, or financial volatility clusters in time. Heteroskedastic GPs model the noise as a function of x, often by placing a second GP over log σ²_n(x) or by using a warped likelihood. A simple approximation: binned noise estimation followed by a fixed diagonal noise matrix.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1,1)
    X2 = np.atleast_2d(X2).reshape(-1,1)
    return sf2 * np.exp(-0.5*(X1-X2.T)**2/ell**2)

np.random.seed(4)
X_tr = np.sort(np.random.uniform(-5,5,60))
# Noise grows with |x|
noise_std = 0.1 + 0.3*np.abs(X_tr)
y_tr = np.sin(X_tr) + noise_std*np.random.randn(60)

X_te = np.linspace(-6,6,300)

def gp_hetero(X_tr, y_tr, X_te, noise_vec, ell=1.5, sf2=1.0):
    K    = rbf_kernel(X_tr,X_tr,ell,sf2) + np.diag(noise_vec**2)
    K_s  = rbf_kernel(X_tr,X_te,ell,sf2)
    K_ss = rbf_kernel(X_te,X_te,ell,sf2)
    L    = np.linalg.cholesky(K)
    alpha = np.linalg.solve(L.T,np.linalg.solve(L,y_tr))
    mu   = K_s.T@alpha
    v    = np.linalg.solve(L,K_s)
    return mu, np.sqrt(np.maximum(np.diag(K_ss-v.T@v),0))

mu, std = gp_hetero(X_tr, y_tr, X_te, noise_std)
plt.figure(figsize=(10,4))
plt.fill_between(X_te,mu-2*std,mu+2*std,alpha=0.25,label='±2σ (homoskedastic post.)')
plt.plot(X_te, mu, lw=2, label='Posterior mean')
plt.errorbar(X_tr, y_tr, yerr=2*noise_std, fmt='r.', alpha=0.4, ms=4, label='Obs ±2σ_n(x)')
plt.title('Heteroskedastic GP (known input-dependent noise)')
plt.xlabel('x'); plt.ylabel('y'); plt.legend(); plt.tight_layout(); plt.show()
```

## Model Selection via Marginal Likelihood

The log marginal likelihood can compare different noise assumptions without a held-out set. Models with unrealistically small σ²_n will have high data-fit but a large complexity penalty from the almost-singular kernel matrix; the marginal likelihood penalises this. Comparing LML values across model variants (different kernels, different noise models) implements formal Bayesian model selection.

```python
import numpy as np
from scipy.optimize import minimize

def rbf_kernel(X1, X2, ell, sf2):
    X1=np.atleast_2d(X1).reshape(-1,1); X2=np.atleast_2d(X2).reshape(-1,1)
    return sf2*np.exp(-0.5*(X1-X2.T)**2/ell**2)

def fit_and_score(X, y, fixed_sn2=None):
    def neg_lml(params):
        if fixed_sn2 is None:
            ell,sf2,sn2 = np.exp(params)
        else:
            ell,sf2 = np.exp(params); sn2 = fixed_sn2
        n = len(y); K = rbf_kernel(X,X,ell,sf2)+sn2*np.eye(n)
        try:
            L=np.linalg.cholesky(K); a=np.linalg.solve(L.T,np.linalg.solve(L,y))
            return 0.5*(y@a)+np.sum(np.log(np.diag(L)))+0.5*n*np.log(2*np.pi)
        except: return 1e10
    n_params = 2 if fixed_sn2 else 3
    x0 = np.zeros(n_params)
    res = minimize(neg_lml, x0, method='L-BFGS-B')
    return -res.fun

np.random.seed(99)
X = np.sort(np.random.uniform(-5,5,50))
y = np.sin(X)+0.2*np.random.randn(50)
for label, sn in [('Interpolating (σ_n=1e-4)',1e-4),
                  ('Learned noise', None),
                  ('Over-smoothed (σ_n=2.0)',2.0)]:
    lml = fit_and_score(X, y, fixed_sn2=sn if sn else None)
    print(f'{label:<35s}: LML = {lml:.2f}')
```

## Key Takeaways

The observation model y = f(x) + ε separates the latent signal f from measurement noise ε ~ N(0, σ²_n). Adding σ²_n to the diagonal of K regularises the matrix (numerical stability) and produces a smoothed posterior mean rather than exact interpolation. The noise level is best learned via marginal likelihood optimisation. SNR = σ²_f/σ²_n is a useful health diagnostic. Heteroskedastic extensions model input-dependent noise via a second GP over log noise.

- σ²_n on K diagonal: numerical stability + smoothed posterior
- Noiseless GP (σ²_n=0): interpolation, appropriate only for deterministic simulators
- Learn σ²_n from marginal likelihood — not cross-validation
- SNR = σ²_f/σ²_n: high → signal-dominated; low → noise-dominated
- Heteroskedastic GP: model σ²_n(x) as a function of input for non-constant noise
- Marginal likelihood formally compares noise models without held-out data

---

