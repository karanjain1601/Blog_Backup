---
title: "The Kernel Trick — Mercer's Theorem and Feature Maps"
slug: "kernel-trick"
description: "Understand kernels as implicit inner products in feature space, apply Mercer's theorem to validate kernels, compare RBF/polynomial/linear kernels, and use kernelised SVM, kernel PCA, and the representer theorem."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtlcm5lbCB0cmljayBhbGxvd3MgbGVhcm5pbmcgYWxnb3JpdGhtcyB0aGF0IGRlcGVuZCBvbmx5IG9uIGlubmVyIHByb2R1Y3RzIGJldHdlZW4gZGF0YSBwb2ludHMgdG8gb3BlcmF0ZSBpbiB2ZXJ5IGhpZ2ggKG9yIGluZmluaXRlKSBkaW1lbnNpb25hbCBmZWF0dXJlIHNwYWNlcyB3aXRob3V0IGV4cGxpY2l0bHkgY29tcHV0aW5nIHRoZSBmZWF0dXJlIG1hcCDPhi4gQSBrZXJuZWwgZnVuY3Rpb24gayh4LHopID0gz4YoeCnCt8+GKHopIGNvbXB1dGVzIHRoZSBpbm5lciBwcm9kdWN0IGltcGxpY2l0bHkuIFRoaXMgcG93ZXJzIGtlcm5lbGlzZWQgU1ZNcywgR2F1c3NpYW4gcHJvY2Vzc2VzLCBrZXJuZWwgUENBLCBhbmQga2VybmVsIHJpZGdlIHJlZ3Jlc3Npb24g4oCUIGVuYWJsaW5nIG5vbmxpbmVhciBtb2RlbHMgd2hpbGUgcmV0YWluaW5nIGNvbnZleCBvcHRpbWlzYXRpb24gZ3VhcmFudGVlcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGZWF0dXJlIE1hcHMgYW5kIHRoZSBLZXJuZWwgRnVuY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBmZWF0dXJlIG1hcCDPhjog4oSd4bWIIOKGkiDihIsgZW1iZWRzIGRhdGEgaW50byBhIChwb3NzaWJseSBpbmZpbml0ZS1kaW1lbnNpb25hbCkgSGlsYmVydCBzcGFjZSDihIsuIEEga2VybmVsIGs6IOKEneG1iCDDlyDihJ3htYgg4oaSIOKEnSBzYXRpc2ZpZXMgayh4LHopID0g4p+oz4YoeCksIM+GKHop4p+pX+KEiy4gVGhlIHBvd2VyOiB3ZSBjYW4gY29tcHV0ZSBrKHgseikgZGlyZWN0bHkgaW4gTyhkKSB0aW1lIGV2ZW4gd2hlbiBkaW0o4oSLKSA9IOKIni4gRXhhbXBsZTogUkJGIGtlcm5lbCBrKHgseikgPSBleHAo4oiSzrPigJZ44oiSeuKAlsKyKSBjb3JyZXNwb25kcyB0byBhbiBpbmZpbml0ZS1kaW1lbnNpb25hbCDPhiAoYSBHYXVzc2lhbiBmdW5jdGlvbiBiYXNpcykuIFBvbHlub21pYWwga2VybmVsIGsoeCx6KSA9ICh44bWAeiArIGMpXmQgY29ycmVzcG9uZHMgdG8gYWxsIG1vbm9taWFscyB1cCB0byBkZWdyZWUgZCwgZ2l2aW5nIE8oZF5EKSBmZWF0dXJlcyBjb21wdXRlZCBpbiBPKGQpIHRpbWUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLm1ldHJpY3MucGFpcndpc2UgaW1wb3J0IHJiZl9rZXJuZWwsIHBvbHlub21pYWxfa2VybmVsLCBsaW5lYXJfa2VybmVsXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCA9IG5wLnJhbmRvbS5yYW5kbig1LCAzKSAgICMgNSBwb2ludHMgaW4gUl4zXG5aID0gbnAucmFuZG9tLnJhbmRuKDQsIDMpICAgIyA0IHF1ZXJ5IHBvaW50c1xuXG4jIFJCRiBrZXJuZWw6IGsoeCx6KSA9IGV4cCgtZ2FtbWEgKiB8fHgtenx8XjIpXG5nYW1tYSA9IDAuNVxuS19yYmYgID0gcmJmX2tlcm5lbChYLCBaLCBnYW1tYT1nYW1tYSlcblxuIyBQb2x5bm9taWFsIGtlcm5lbDogayh4LHopID0gKHheVCB6ICsgMSleM1xuS19wb2x5ID0gcG9seW5vbWlhbF9rZXJuZWwoWCwgWiwgZGVncmVlPTMsIGNvZWYwPTEuMClcblxuIyBMaW5lYXIga2VybmVsOiBrKHgseikgPSB4XlQgelxuS19saW4gID0gbGluZWFyX2tlcm5lbChYLCBaKVxuXG5wcmludChmXHUwMDI3UkJGIGtlcm5lbCBtYXRyaXggc2hhcGU6ICAgICAgICB7S19yYmYuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1BvbHlub21pYWwga2VybmVsIG1hdHJpeCBzaGFwZToge0tfcG9seS5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3TGluZWFyIGtlcm5lbCBtYXRyaXggc2hhcGU6ICAgICB7S19saW4uc2hhcGV9XHUwMDI3KVxuXG4jIFZlcmlmeSBSQkYgbWFudWFsbHlcbmksIGogPSAwLCAwXG5yYmZfbWFudWFsID0gbnAuZXhwKC1nYW1tYSAqIG5wLnN1bSgoWFtpXSAtIFpbal0pKioyKSlcbnByaW50KGZcdTAwMjdcXG5SQkYgS1swLDBdIHNrbGVhcm46ICB7S19yYmZbMCwwXTouNmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1JCRiBLWzAsMF0gbWFudWFsOiAgIHtyYmZfbWFudWFsOi42Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVyY2VyXHUwMDI3cyBUaGVvcmVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGZ1bmN0aW9uIGsoeCx6KSBpcyBhIHZhbGlkIGtlcm5lbCAoaS5lLiwgdGhlcmUgZXhpc3RzIGEgZmVhdHVyZSBtYXAgz4Ygc3VjaCB0aGF0IGsoeCx6KSA9IOKfqM+GKHgpLM+GKHop4p+pKSBpZiBhbmQgb25seSBpZiB0aGUgR3JhbSBtYXRyaXggSyDiiIgg4oSd4oG/y6Pigb8gd2l0aCBL4bWi4rG8ID0gayh44bWiLHjisbwpIGlzIHBvc2l0aXZlIHNlbWktZGVmaW5pdGUgKFBTRCkgZm9yIGV2ZXJ5IGZpbml0ZSBzZXQgb2YgcG9pbnRzIHt44oKBLC4uLix44oKZfS4gRXF1aXZhbGVudGx5LCBrIG11c3QgYmUgYSBzeW1tZXRyaWMgZnVuY3Rpb24gd2l0aCBhbGwgZWlnZW52YWx1ZXMgb2YgSyBub24tbmVnYXRpdmUuIE1lcmNlclx1MDAyN3MgdGhlb3JlbSBwcm92aWRlcyB0aGUgY29uc3RydWN0aXZlIGRpcmVjdGlvbjogdGhlIGVpZ2VuZnVuY3Rpb25zIG9mIHRoZSBpbnRlZ3JhbCBvcGVyYXRvciBnaXZlIHRoZSBmZWF0dXJlIG1hcC4gUFNELW5lc3MgY2FuIGJlIHZlcmlmaWVkIGJ5IGNoZWNraW5nIHRoYXQgYWxsIGVpZ2VudmFsdWVzIG9mIEsgYXJlIOKJpSAwLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiS2VybmVsIFZhbGlkaXR5IGFuZCB0aGUgUFNEIENvbmRpdGlvbiIsImNvbnRlbnQiOiJOb3QgZXZlcnkgc3ltbWV0cmljIHNpbWlsYXJpdHkgZnVuY3Rpb24gaXMgYSB2YWxpZCBrZXJuZWwuIEhldXJpc3RpYyBcdTAwMjdrZXJuZWxzXHUwMDI3IGxpa2Ugayh4LHopID0gZXhwKOKIkuKAlnjiiJJ64oCWKSAobm90IHNxdWFyZWQpIGFyZSBjb25kaXRpb25hbGx5IG5lZ2F0aXZlIGRlZmluaXRlIGFuZCBjYW4gY2F1c2UgaW5kZWZpbml0ZSBHcmFtIG1hdHJpY2VzLCBicmVha2luZyB0aGUgU1ZNIFFQIGNvbnZleGl0eS4gQWx3YXlzIHZlcmlmeSBQU0QtbmVzcyBiZWZvcmUgdXNpbmcgYSBjdXN0b20ga2VybmVsLiBBIHByYWN0aWNhbCBjaGVjazogY29tcHV0ZSBLIG9uIGEgc2FtcGxlIGFuZCB2ZXJpZnkgYWxsIGVpZ2VudmFsdWVzIOKJpSDiiJLOtSBmb3Igc21hbGwgbWFjaGluZS1wcmVjaXNpb24gzrUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tbW9uIEtlcm5lbHMgYW5kIFRoZWlyIFByb3BlcnRpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0aHJlZSBtb3N0IHdpZGVseSB1c2VkIGtlcm5lbHMgYXJlOiBSQkYgKEdhdXNzaWFuKSBrKHgseikgPSBleHAo4oiSzrPigJZ44oiSeuKAlsKyKSDigJQgdW5pdmVyc2FsIGFwcHJveGltYXRvciwgaW5maW5pdGUtZGltZW5zaW9uYWwgz4YsIGxvY2FsaXplZCAoZGVwZW5kcyBvbmx5IG9uIGRpc3RhbmNlKTsgUG9seW5vbWlhbCBrKHgseikgPSAoeOG1gHorYyleZCDigJQgY2FwdHVyZXMgaW50ZXJhY3Rpb24gdGVybXMsIG5vdCB1bml2ZXJzYWwsIGNhbiBoYXZlIG51bWVyaWNhbCBpc3N1ZXMgZm9yIGxhcmdlIGQ7IExpbmVhciBrKHgseikgPSB44bWAeiDigJQgZXF1aXZhbGVudCB0byBhIGxpbmVhciBtb2RlbCwgbm8gz4YgdHJhbnNmb3JtYXRpb24uIE1hdMOpcm4ga2VybmVscyBnZW5lcmFsaXNlIFJCRiB3aXRoIGEgc21vb3RobmVzcyBwYXJhbWV0ZXIgzr0uIEtlcm5lbCBjb21wb3NpdGlvbiBydWxlczogc3VtcywgcHJvZHVjdHMsIGFuZCBwb3NpdGl2ZSBzY2FsYXIgbXVsdGlwbGVzIG9mIHZhbGlkIGtlcm5lbHMgYXJlIHZhbGlkIGtlcm5lbHMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIktlcm5lbCIsIkZvcm11bGEiLCJEaW0oz4YpIiwiSHlwZXJwYXJhbXMiLCJXaGVuIHRvIFVzZSJdLCJyb3dzIjpbWyJMaW5lYXIiLCJ44bWAeiIsImQgKHNhbWUgYXMgaW5wdXQpIiwiTm9uZSIsIkxpbmVhcmx5IHNlcGFyYWJsZSwgbGFyZ2UgbiJdLFsiUG9seW5vbWlhbCIsIih44bWAeiArIGMpXmQiLCJPKGReZCkiLCJkZWdyZWUgZCwgY29lZjAgYyIsIkludGVyYWN0aW9uIGZlYXR1cmVzLCBOTFAgbi1ncmFtcyJdLFsiUkJGIChHYXVzc2lhbikiLCJleHAo4oiSzrPigJZ44oiSeuKAlsKyKSIsIuKIniIsIs6zIChiYW5kd2lkdGgpIiwiR2VuZXJhbCBwdXJwb3NlIG5vbmxpbmVhciBkZWZhdWx0Il0sWyJNYXTDqXJuIM69PTMvMiIsIigxK+KImjPigJZ44oiSeuKAli9sKWV4cCjiiJLiiJoz4oCWeOKIknrigJYvbCkiLCLiiJ4iLCJsZW5ndGgtc2NhbGUgbCIsIkdQcywgc21vb3RoZXIgdGhhbiBSQkYiXSxbIlNpZ21vaWQiLCJ0YW5oKM6xeOG1gHogKyBjKSIsIuKAlCIsIs6xLCBjIiwiTm90IGFsd2F5cyBQU0Qg4oCUIHVzZSB3aXRoIGNhcmUiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Iktlcm5lbGlzZWQgU1ZNIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZXBsYWNpbmcgeOG1ouG1gHjisbwgd2l0aCBrKHjhtaIseOKxvCkgaW4gdGhlIFNWTSBkdWFsIGlzIGFsbCB0aGF0IGlzIG5lZWRlZCB0byBrZXJuZWxpc2U6IG1heGltaXNlIM6jzrHhtaIg4oiSIMK9zqPhtaLOo+KxvCDOseG1os6x4rG8eeG1onnisbxrKHjhtaIseOKxvCkuIFRoZSBkZWNpc2lvbiBmdW5jdGlvbiBiZWNvbWVzIGYoeCkgPSBzaWduKM6j4bWiIM6x4bWieeG1omsoeOG1oix4KSArIGIpLiBUaGUgd2VpZ2h0IHZlY3RvciB3IGV4aXN0cyBpbiB0aGUgZmVhdHVyZSBzcGFjZSDihIsgYnV0IG1heSBiZSBpbmZpbml0ZS1kaW1lbnNpb25hbCDigJQgaXQgaXMgbmV2ZXIgY29tcHV0ZWQgZXhwbGljaXRseS4gVGhpcyBpcyB0aGUga2VybmVsIHRyaWNrLiBUaGUgUkJGIFNWTSBjYW4gZm9ybSBhbnkgZGVjaXNpb24gYm91bmRhcnksIG1ha2luZyBpdCBhIHVuaXZlcnNhbCBjbGFzc2lmaWVyIGZvciBjb21wYWN0IGZlYXR1cmUgc3BhY2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5zdm0gaW1wb3J0IFNWQ1xuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NpcmNsZXMsIG1ha2VfbW9vbnNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgY3Jvc3NfdmFsX3Njb3JlXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCwgeSA9IG1ha2VfbW9vbnMobl9zYW1wbGVzPTMwMCwgbm9pc2U9MC4yLCByYW5kb21fc3RhdGU9NDIpXG5YX3MgPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxua2VybmVscyA9IFtcbiAgICAoXHUwMDI3bGluZWFyXHUwMDI3LCAgICBTVkMoa2VybmVsPVx1MDAyN2xpbmVhclx1MDAyNywgICAgICAgICAgICAgIEM9MS4wKSksXG4gICAgKFx1MDAyN3BvbHkgZD0zXHUwMDI3LCAgU1ZDKGtlcm5lbD1cdTAwMjdwb2x5XHUwMDI3LCBkZWdyZWU9MywgICAgICBDPTEuMCwgY29lZjA9MSkpLFxuICAgIChcdTAwMjdSQkYgZz0xXHUwMDI3LCAgIFNWQyhrZXJuZWw9XHUwMDI3cmJmXHUwMDI3LCAgZ2FtbWE9MS4wLCAgICAgQz0xLjApKSxcbiAgICAoXHUwMDI3UkJGIGc9MC4xXHUwMDI3LCBTVkMoa2VybmVsPVx1MDAyN3JiZlx1MDAyNywgIGdhbW1hPTAuMSwgICAgIEM9MS4wKSksXG5dXG5cbnByaW50KGZcdTAwMjd7XCJLZXJuZWxcIjpcdTAwM2UxNH0ge1wiTWVhbiBDViBBY2NcIjpcdTAwM2UxMn0ge1wiU3RkXCI6XHUwMDNlNn1cdTAwMjcpXG5mb3IgbmFtZSwgY2xmIGluIGtlcm5lbHM6XG4gICAgc2NvcmVzID0gY3Jvc3NfdmFsX3Njb3JlKGNsZiwgWF9zLCB5LCBjdj01LCBzY29yaW5nPVx1MDAyN2FjY3VyYWN5XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2UxNH0ge3Njb3Jlcy5tZWFuKCk6XHUwMDNlMTIuNGZ9IHtzY29yZXMuc3RkKCk6XHUwMDNlNi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2VybmVsIFBDQSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgUENBIGZpbmRzIGxpbmVhciBzdWJzcGFjZXMgb2YgbWF4aW11bSB2YXJpYW5jZS4gS2VybmVsIFBDQSBmaXJzdCBtYXBzIGRhdGEgdG8g4oSLIHZpYSDPhiwgdGhlbiBwZXJmb3JtcyBQQ0EgaW4g4oSLIOKAlCBmaW5kaW5nIG5vbmxpbmVhciBsb3ctZGltZW5zaW9uYWwgc3RydWN0dXJlLiBCZWNhdXNlIG9ubHkgaW5uZXIgcHJvZHVjdHMg4p+oz4YoeOG1oiksz4YoeOKxvCnin6kgPSBrKHjhtaIseOKxvCkgYXJlIG5lZWRlZCwgdGhlIGZ1bGwgY29tcHV0YXRpb24gcmVxdWlyZXMgb25seSB0aGUgbsOXbiBrZXJuZWwgbWF0cml4LiBUaGUgcHJvamVjdGVkIGNvb3JkaW5hdGVzIGluIOKEiyBhcmUgdGhlIGVpZ2VudmVjdG9ycyBvZiB0aGUgY2VudHJlZCBrZXJuZWwgbWF0cml4LiBUaGlzIGNhbiBzZXBhcmF0ZSBjbGFzc2VzIHRoYXQgYXJlIG5vdCBsaW5lYXJseSBzZXBhcmFibGUgaW4gdGhlIG9yaWdpbmFsIHNwYWNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBLZXJuZWxQQ0EsIFBDQVxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NpcmNsZXNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgTG9naXN0aWNSZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ucGlwZWxpbmUgaW1wb3J0IFBpcGVsaW5lXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCBjcm9zc192YWxfc2NvcmVcblxubnAucmFuZG9tLnNlZWQoMClcblgsIHkgPSBtYWtlX2NpcmNsZXMobl9zYW1wbGVzPTQwMCwgbm9pc2U9MC4xLCBmYWN0b3I9MC4zLCByYW5kb21fc3RhdGU9MClcblhfcyA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKVxuXG4jIExpbmVhciBQQ0E6IGNhbm5vdCBzZXBhcmF0ZSBjb25jZW50cmljIGNpcmNsZXNcbnBjYV9hY2MgPSBjcm9zc192YWxfc2NvcmUoXG4gICAgUGlwZWxpbmUoWyhcdTAwMjdwY2FcdTAwMjcsIFBDQShuX2NvbXBvbmVudHM9MSkpLCAoXHUwMDI3bHJcdTAwMjcsIExvZ2lzdGljUmVncmVzc2lvbigpKV0pLFxuICAgIFhfcywgeSwgY3Y9NVxuKS5tZWFuKClcblxuIyBLZXJuZWwgUENBIHdpdGggUkJGOiBtYXBzIHRvIHNwYWNlIHdoZXJlIGNsYXNzZXMgYXJlIGxpbmVhcmx5IHNlcGFyYWJsZVxua3BjYV9hY2MgPSBjcm9zc192YWxfc2NvcmUoXG4gICAgUGlwZWxpbmUoWyhcdTAwMjdrcGNhXHUwMDI3LCBLZXJuZWxQQ0Eobl9jb21wb25lbnRzPTIsIGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTUuMCkpLFxuICAgICAgICAgICAgICAgKFx1MDAyN2xyXHUwMDI3LCAgIExvZ2lzdGljUmVncmVzc2lvbigpKV0pLFxuICAgIFhfcywgeSwgY3Y9NVxuKS5tZWFuKClcblxucHJpbnQoZlx1MDAyN1BDQSAgKyBMUiBhY2N1cmFjeTogICAgICAgIHtwY2FfYWNjOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3S1BDQSArIExSIGFjY3VyYWN5OiAgICAgICAge2twY2FfYWNjOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3Q29uY2VudHJpYyBjaXJjbGVzIG5lZWQgbm9ubGluZWFyIGVtYmVkZGluZyDigJQgS1BDQSBzdWNjZWVkcyB3aGVyZSBQQ0EgZmFpbHMuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Iktlcm5lbCBSaWRnZSBSZWdyZXNzaW9uIGFuZCB0aGUgUmVwcmVzZW50ZXIgVGhlb3JlbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFJlcHJlc2VudGVyIFRoZW9yZW0gKEtpbWVsZG9yZiBcdTAwMjYgV2FoYmEsIDE5NzEpIHN0YXRlcyB0aGF0IHRoZSBvcHRpbWFsIHNvbHV0aW9uIHRvIGFueSByZWd1bGFyaXNlZCBlbXBpcmljYWwgcmlzayBtaW5pbWlzYXRpb24gcHJvYmxlbSBpbiBhbiBSS0hTIGxpZXMgaW4gdGhlIHNwYW4gb2Yga2VybmVsIGZ1bmN0aW9ucyBhdCB0aGUgdHJhaW5pbmcgcG9pbnRzOiBmKih4KSA9IM6j4bWiIM6x4bWiayh44bWiLHgpLiBLZXJuZWwgcmlkZ2UgcmVncmVzc2lvbiAoS1JSKSBtaW5pbWlzZXMg4oCWeSDiiJIgZuKAlsKyICsgzrvigJZm4oCWwrJf4oSLIGFuZCBoYXMgdGhlIGNsb3NlZC1mb3JtIGR1YWwgc29sdXRpb24gzrEgPSAoSyArIM67SSnigbvCuXksIHdoZXJlIEsgaXMgdGhlIGtlcm5lbCBtYXRyaXguIEtSUiBpcyBlcXVpdmFsZW50IHRvIEdhdXNzaWFuIHByb2Nlc3MgcmVncmVzc2lvbiB3aXRoIGEgc3F1YXJlZC1leHBvbmVudGlhbCBjb3ZhcmlhbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5rZXJuZWxfcmlkZ2UgaW1wb3J0IEtlcm5lbFJpZGdlXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBSaWRnZVxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgbWVhbl9zcXVhcmVkX2Vycm9yXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubiA9IDE1MFxuWCA9IG5wLnNvcnQobnAucmFuZG9tLnVuaWZvcm0oLTQsIDQsIG4pKS5yZXNoYXBlKC0xLCAxKVxueSA9IG5wLnNpbihYKS5yYXZlbCgpICsgMC4zICogbnAucmFuZG9tLnJhbmRuKG4pXG5YX3MgPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxuIyBTdGFuZGFyZCBSaWRnZSAobGluZWFyKVxucmlkZ2UgPSBSaWRnZShhbHBoYT0xLjApLmZpdChYX3MsIHkpXG5cbiMgS2VybmVsIFJpZGdlIHdpdGggUkJGIChub25saW5lYXIpXG5rcnIgPSBLZXJuZWxSaWRnZShhbHBoYT0wLjEsIGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTEuMCkuZml0KFhfcywgeSlcblxuWF90ZXN0ID0gbnAubGluc3BhY2UoLTQsIDQsIDIwMCkucmVzaGFwZSgtMSwgMSlcblhfdGVzdF9zID0gU3RhbmRhcmRTY2FsZXIoKS5maXQoWCkudHJhbnNmb3JtKFhfdGVzdClcblxucmlkZ2VfbXNlID0gbWVhbl9zcXVhcmVkX2Vycm9yKG5wLnNpbihYX3Rlc3QpLCByaWRnZS5wcmVkaWN0KFhfdGVzdF9zKSlcbmtycl9tc2UgICA9IG1lYW5fc3F1YXJlZF9lcnJvcihucC5zaW4oWF90ZXN0KSwga3JyLnByZWRpY3QoWF90ZXN0X3MpKVxuXG5wcmludChmXHUwMDI3UmlkZ2UgKGxpbmVhcikgdGVzdCBNU0U6IHtyaWRnZV9tc2U6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdLZXJuZWwgUmlkZ2UgKFJCRikgTVNFOiAge2tycl9tc2U6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdLUlIgYWxwaGEgc2hhcGU6IHtrcnIuZHVhbF9jb2VmXy5zaGFwZX0gIChvbmUgYWxwaGEgcGVyIHRyYWluaW5nIHBvaW50KVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXJuZWwgQ29tcG9zaXRpb24gUnVsZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5ldyBrZXJuZWxzIGNhbiBiZSBidWlsdCBmcm9tIGV4aXN0aW5nIHZhbGlkIGtlcm5lbHMgdXNpbmcgdGhlc2UgY2xvc3VyZSBwcm9wZXJ0aWVzLiBJZiBr4oKBIGFuZCBr4oKCIGFyZSB2YWxpZCBrZXJuZWxzIGFuZCBjIFx1MDAzZSAwLCB0aGVuIHRoZSBmb2xsb3dpbmcgYXJlIGFsc28gdmFsaWQga2VybmVsczoga+KCgSArIGvigoIgKHN1bSksIGvigoEgwrcga+KCgiAocHJvZHVjdCksIGMgwrcga+KCgSAoc2NhbGFyIG11bHRpcGxlKSwgZXhwKGvigoEpIChtYXRyaXggZXhwb25lbnRpYWwpLCBmKHgpwrdr4oKBKHgseinCt2YoeikgZm9yIGFueSBmdW5jdGlvbiBmLCBhbmQgayjPhih4KSwgz4YoeikpIGZvciBhbnkgZnVuY3Rpb24gz4YuIFRoZXNlIHJ1bGVzIGxldCBwcmFjdGl0aW9uZXJzIGJ1aWxkIGRvbWFpbi1zcGVjaWZpYyBrZXJuZWxzIGZvciBzdHJpbmdzLCBncmFwaHMsIHRpbWUgc2VyaWVzLCBvciBpbWFnZXMgYnkgY29tYmluaW5nIHNpbXBsZXIga2VybmVscy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlN1bToga+KCgSh4LHopICsga+KCgih4LHopIOKAlCBjb21iaW5lcyBmZWF0dXJlcyBmcm9tIHR3byBzcGFjZXMgYWRkaXRpdmVseS4iLCJQcm9kdWN0OiBr4oKBKHgseikgwrcga+KCgih4LHopIOKAlCBtb2RlbHMgYWxsIHBhaXJ3aXNlIGludGVyYWN0aW9ucyBiZXR3ZWVuIHRoZSB0d28gZmVhdHVyZSBzZXRzLiIsIlNjYWxhciBtdWx0aXBsZTogYyDCtyBrKHgseikg4oCUIHNjYWxlcyB0aGUgZmVhdHVyZSBzcGFjZTsgYyBtdXN0IGJlIHBvc2l0aXZlLiIsIkV4cG9uZW50aWF0aW9uOiBleHAoayh4LHopKSDigJQgYWx3YXlzIGEgdmFsaWQga2VybmVsIHdoZW4gayBpcyBhbnkgdmFsaWQga2VybmVsLiIsIkZ1bmN0aW9uIHNjYWxpbmc6IGYoeCkgwrcgayh4LHopIMK3IGYoeikg4oCUIHJlLXdlaWdodHMgdGhlIGZlYXR1cmUgc3BhY2UgYnkgZnVuY3Rpb24gZi4iLCJDb21wb3NpdGlvbjogayjPhih4KSwgz4YoeikpIOKAlCBhcHBsaWVzIGEgcHJlcHJvY2Vzc2luZyBtYXAgz4YgYmVmb3JlIGNvbXB1dGluZyB0aGUga2VybmVsLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# The Kernel Trick — Mercer's Theorem and Feature Maps

The kernel trick allows learning algorithms that depend only on inner products between data points to operate in very high (or infinite) dimensional feature spaces without explicitly computing the feature map φ. A kernel function k(x,z) = φ(x)·φ(z) computes the inner product implicitly. This powers kernelised SVMs, Gaussian processes, kernel PCA, and kernel ridge regression — enabling nonlinear models while retaining convex optimisation guarantees.

## Feature Maps and the Kernel Function

The feature map φ: ℝᵈ → ℋ embeds data into a (possibly infinite-dimensional) Hilbert space ℋ. A kernel k: ℝᵈ × ℝᵈ → ℝ satisfies k(x,z) = ⟨φ(x), φ(z)⟩_ℋ. The power: we can compute k(x,z) directly in O(d) time even when dim(ℋ) = ∞. Example: RBF kernel k(x,z) = exp(−γ‖x−z‖²) corresponds to an infinite-dimensional φ (a Gaussian function basis). Polynomial kernel k(x,z) = (xᵀz + c)^d corresponds to all monomials up to degree d, giving O(d^D) features computed in O(d) time.

```python
import numpy as np
from sklearn.metrics.pairwise import rbf_kernel, polynomial_kernel, linear_kernel

np.random.seed(42)
X = np.random.randn(5, 3)   # 5 points in R^3
Z = np.random.randn(4, 3)   # 4 query points

# RBF kernel: k(x,z) = exp(-gamma * ||x-z||^2)
gamma = 0.5
K_rbf  = rbf_kernel(X, Z, gamma=gamma)

# Polynomial kernel: k(x,z) = (x^T z + 1)^3
K_poly = polynomial_kernel(X, Z, degree=3, coef0=1.0)

# Linear kernel: k(x,z) = x^T z
K_lin  = linear_kernel(X, Z)

print(f'RBF kernel matrix shape:        {K_rbf.shape}')
print(f'Polynomial kernel matrix shape: {K_poly.shape}')
print(f'Linear kernel matrix shape:     {K_lin.shape}')

# Verify RBF manually
i, j = 0, 0
rbf_manual = np.exp(-gamma * np.sum((X[i] - Z[j])**2))
print(f'\nRBF K[0,0] sklearn:  {K_rbf[0,0]:.6f}')
print(f'RBF K[0,0] manual:   {rbf_manual:.6f}')
```

## Mercer's Theorem

A function k(x,z) is a valid kernel (i.e., there exists a feature map φ such that k(x,z) = ⟨φ(x),φ(z)⟩) if and only if the Gram matrix K ∈ ℝⁿˣⁿ with Kᵢⱼ = k(xᵢ,xⱼ) is positive semi-definite (PSD) for every finite set of points {x₁,...,xₙ}. Equivalently, k must be a symmetric function with all eigenvalues of K non-negative. Mercer's theorem provides the constructive direction: the eigenfunctions of the integral operator give the feature map. PSD-ness can be verified by checking that all eigenvalues of K are ≥ 0.

> **Kernel Validity and the PSD Condition**: Not every symmetric similarity function is a valid kernel. Heuristic 'kernels' like k(x,z) = exp(−‖x−z‖) (not squared) are conditionally negative definite and can cause indefinite Gram matrices, breaking the SVM QP convexity. Always verify PSD-ness before using a custom kernel. A practical check: compute K on a sample and verify all eigenvalues ≥ −ε for small machine-precision ε.

## Common Kernels and Their Properties

The three most widely used kernels are: RBF (Gaussian) k(x,z) = exp(−γ‖x−z‖²) — universal approximator, infinite-dimensional φ, localized (depends only on distance); Polynomial k(x,z) = (xᵀz+c)^d — captures interaction terms, not universal, can have numerical issues for large d; Linear k(x,z) = xᵀz — equivalent to a linear model, no φ transformation. Matérn kernels generalise RBF with a smoothness parameter ν. Kernel composition rules: sums, products, and positive scalar multiples of valid kernels are valid kernels.

| Kernel | Formula | Dim(φ) | Hyperparams | When to Use |
| --- | --- | --- | --- | --- |
| Linear | xᵀz | d (same as input) | None | Linearly separable, large n |
| Polynomial | (xᵀz + c)^d | O(d^d) | degree d, coef0 c | Interaction features, NLP n-grams |
| RBF (Gaussian) | exp(−γ‖x−z‖²) | ∞ | γ (bandwidth) | General purpose nonlinear default |
| Matérn ν=3/2 | (1+√3‖x−z‖/l)exp(−√3‖x−z‖/l) | ∞ | length-scale l | GPs, smoother than RBF |
| Sigmoid | tanh(αxᵀz + c) | — | α, c | Not always PSD — use with care |

## Kernelised SVM

Replacing xᵢᵀxⱼ with k(xᵢ,xⱼ) in the SVM dual is all that is needed to kernelise: maximise Σαᵢ − ½ΣᵢΣⱼ αᵢαⱼyᵢyⱼk(xᵢ,xⱼ). The decision function becomes f(x) = sign(Σᵢ αᵢyᵢk(xᵢ,x) + b). The weight vector w exists in the feature space ℋ but may be infinite-dimensional — it is never computed explicitly. This is the kernel trick. The RBF SVM can form any decision boundary, making it a universal classifier for compact feature spaces.

```python
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_circles, make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

np.random.seed(42)
X, y = make_moons(n_samples=300, noise=0.2, random_state=42)
X_s = StandardScaler().fit_transform(X)

kernels = [
    ('linear',    SVC(kernel='linear',              C=1.0)),
    ('poly d=3',  SVC(kernel='poly', degree=3,      C=1.0, coef0=1)),
    ('RBF g=1',   SVC(kernel='rbf',  gamma=1.0,     C=1.0)),
    ('RBF g=0.1', SVC(kernel='rbf',  gamma=0.1,     C=1.0)),
]

print(f'{"Kernel":>14} {"Mean CV Acc":>12} {"Std":>6}')
for name, clf in kernels:
    scores = cross_val_score(clf, X_s, y, cv=5, scoring='accuracy')
    print(f'{name:>14} {scores.mean():>12.4f} {scores.std():>6.4f}')
```

## Kernel PCA

Standard PCA finds linear subspaces of maximum variance. Kernel PCA first maps data to ℋ via φ, then performs PCA in ℋ — finding nonlinear low-dimensional structure. Because only inner products ⟨φ(xᵢ),φ(xⱼ)⟩ = k(xᵢ,xⱼ) are needed, the full computation requires only the n×n kernel matrix. The projected coordinates in ℋ are the eigenvectors of the centred kernel matrix. This can separate classes that are not linearly separable in the original space.

```python
import numpy as np
from sklearn.decomposition import KernelPCA, PCA
from sklearn.datasets import make_circles
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

np.random.seed(0)
X, y = make_circles(n_samples=400, noise=0.1, factor=0.3, random_state=0)
X_s = StandardScaler().fit_transform(X)

# Linear PCA: cannot separate concentric circles
pca_acc = cross_val_score(
    Pipeline([('pca', PCA(n_components=1)), ('lr', LogisticRegression())]),
    X_s, y, cv=5
).mean()

# Kernel PCA with RBF: maps to space where classes are linearly separable
kpca_acc = cross_val_score(
    Pipeline([('kpca', KernelPCA(n_components=2, kernel='rbf', gamma=5.0)),
               ('lr',   LogisticRegression())]),
    X_s, y, cv=5
).mean()

print(f'PCA  + LR accuracy:        {pca_acc:.4f}')
print(f'KPCA + LR accuracy:        {kpca_acc:.4f}')
print(f'Concentric circles need nonlinear embedding — KPCA succeeds where PCA fails.')
```

## Kernel Ridge Regression and the Representer Theorem

The Representer Theorem (Kimeldorf & Wahba, 1971) states that the optimal solution to any regularised empirical risk minimisation problem in an RKHS lies in the span of kernel functions at the training points: f*(x) = Σᵢ αᵢk(xᵢ,x). Kernel ridge regression (KRR) minimises ‖y − f‖² + λ‖f‖²_ℋ and has the closed-form dual solution α = (K + λI)⁻¹y, where K is the kernel matrix. KRR is equivalent to Gaussian process regression with a squared-exponential covariance.

```python
import numpy as np
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

np.random.seed(42)
n = 150
X = np.sort(np.random.uniform(-4, 4, n)).reshape(-1, 1)
y = np.sin(X).ravel() + 0.3 * np.random.randn(n)
X_s = StandardScaler().fit_transform(X)

# Standard Ridge (linear)
ridge = Ridge(alpha=1.0).fit(X_s, y)

# Kernel Ridge with RBF (nonlinear)
krr = KernelRidge(alpha=0.1, kernel='rbf', gamma=1.0).fit(X_s, y)

X_test = np.linspace(-4, 4, 200).reshape(-1, 1)
X_test_s = StandardScaler().fit(X).transform(X_test)

ridge_mse = mean_squared_error(np.sin(X_test), ridge.predict(X_test_s))
krr_mse   = mean_squared_error(np.sin(X_test), krr.predict(X_test_s))

print(f'Ridge (linear) test MSE: {ridge_mse:.4f}')
print(f'Kernel Ridge (RBF) MSE:  {krr_mse:.4f}')
print(f'KRR alpha shape: {krr.dual_coef_.shape}  (one alpha per training point)')
```

## Kernel Composition Rules

New kernels can be built from existing valid kernels using these closure properties. If k₁ and k₂ are valid kernels and c > 0, then the following are also valid kernels: k₁ + k₂ (sum), k₁ · k₂ (product), c · k₁ (scalar multiple), exp(k₁) (matrix exponential), f(x)·k₁(x,z)·f(z) for any function f, and k(φ(x), φ(z)) for any function φ. These rules let practitioners build domain-specific kernels for strings, graphs, time series, or images by combining simpler kernels.

- Sum: k₁(x,z) + k₂(x,z) — combines features from two spaces additively.
- Product: k₁(x,z) · k₂(x,z) — models all pairwise interactions between the two feature sets.
- Scalar multiple: c · k(x,z) — scales the feature space; c must be positive.
- Exponentiation: exp(k(x,z)) — always a valid kernel when k is any valid kernel.
- Function scaling: f(x) · k(x,z) · f(z) — re-weights the feature space by function f.
- Composition: k(φ(x), φ(z)) — applies a preprocessing map φ before computing the kernel.

---

