---
title: "Probabilistic Forecasting — Quantile Regression and Conformal Prediction"
slug: "probabilistic-forecasting"
description: "Move beyond point forecasts to uncertainty quantification: quantile regression for prediction intervals, CRPS as a proper scoring rule, split conformal prediction with coverage guarantees, and adaptive conformal prediction for non-stationary series."
tags: ["time-series", "forecasting", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUG9pbnQgZm9yZWNhc3RzIGFyZSBpbnN1ZmZpY2llbnQgZm9yIG1vc3QgcmVhbC13b3JsZCBkZWNpc2lvbnMuIEEgcmV0YWlsZXIgc3RvY2tpbmcgaW52ZW50b3J5IG5lZWRzIG5vdCBqdXN0IHRoZSBleHBlY3RlZCBkZW1hbmQgYnV0IGEgcmFuZ2UgaXQgbWlnaHQgZmFsbCBpbi4gQW4gZWxlY3RyaWNpdHkgZ3JpZCBvcGVyYXRvciBuZWVkcyB0byBrbm93IHRoZSBwcm9iYWJpbGl0eSBvZiBkZW1hbmQgZXhjZWVkaW5nIGEgdGhyZXNob2xkLiBQcm9iYWJpbGlzdGljIGZvcmVjYXN0aW5nIHF1YW50aWZpZXMgdGhpcyB1bmNlcnRhaW50eSBieSBwcm9kdWNpbmcgZGlzdHJpYnV0aW9ucywgcHJlZGljdGlvbiBpbnRlcnZhbHMsIG9yIHF1YW50aWxlIGVzdGltYXRlcyByYXRoZXIgdGhhbiBhIHNpbmdsZSBudW1iZXIuIFRoaXMgbm90ZSBjb3ZlcnMgcXVhbnRpbGUgcmVncmVzc2lvbiwgQ1JQUyBldmFsdWF0aW9uLCBhbmQgY29uZm9ybWFsIHByZWRpY3Rpb24g4oCUIGEgZGlzdHJpYnV0aW9uLWZyZWUgbWV0aG9kIHdpdGggZmluaXRlLXNhbXBsZSBjb3ZlcmFnZSBndWFyYW50ZWVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoeSBQb2ludCBGb3JlY2FzdHMgQXJlIEluc3VmZmljaWVudCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBwb2ludCBmb3JlY2FzdCBtaW5pbWlzZXMgZXhwZWN0ZWQgbG9zcyB1bmRlciBhIHNwZWNpZmljIGxvc3MgZnVuY3Rpb24gKGUuZy4sIE1BRSBtaW5pbWlzZXMgbWVkaWFuLCBNU0UgbWluaW1pc2VzIG1lYW4pLiBCdXQgZGVjaXNpb24tbWFraW5nIHVuZGVyIHVuY2VydGFpbnR5IHJlcXVpcmVzIGtub3dpbmcgdGhlIGZ1bGwgcHJlZGljdGl2ZSBkaXN0cmlidXRpb24gb3IgYXQgbGVhc3Qga2V5IHF1YW50aWxlcy4gRm9yIGFzeW1tZXRyaWMgY29zdHMg4oCUIHdoZXJlIHN0b2Nrb3V0cyBjb3N0IG1vcmUgdGhhbiBvdmVyc3RvY2tpbmcg4oCUIHRoZSBvcHRpbWFsIGFjdGlvbiBkZXBlbmRzIG9uIHF1YW50aWxlcywgbm90IHRoZSBtZWFuLiBGb3Igc2FmZXR5LWNyaXRpY2FsIHN5c3RlbXMsIHRoZSA5OXRoIHBlcmNlbnRpbGUgbWF0dGVycyBtb3JlIHRoYW4gdGhlIGV4cGVjdGVkIHZhbHVlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlF1YW50aWxlIFJlZ3Jlc3Npb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlF1YW50aWxlIHJlZ3Jlc3Npb24gcHJlZGljdHMgdGhlIM+ELXRoIHF1YW50aWxlIFFfz4QoeXx4KSBmb3IgbXVsdGlwbGUgbGV2ZWxzIM+EIOKIiCB7MC4xLCAwLjIsIC4uLiwgMC45fS4gVGhlIHBpbmJhbGwgbG9zcyAoYWxzbyBjYWxsZWQgcXVhbnRpbGUgbG9zcykgaXM6IExfz4QoeSwgcSkgPSDPhCh5LXEpIGlmIHkg4omlIHEsIGVsc2UgKDEtz4QpKHEteSkuIE1pbmltaXNpbmcgdGhpcyBsb3NzIG92ZXIgdGhlIHRyYWluaW5nIHNldCB5aWVsZHMgYSBjYWxpYnJhdGVkIHF1YW50aWxlIGVzdGltYXRlLiBBIHByZWRpY3Rpb24gaW50ZXJ2YWwgW1FfMC4xLCBRXzAuOV0gZ2l2ZXMgYW4gODAlIG5vbWluYWwgaW50ZXJ2YWwuIFRoZSBtb2RlbCBtdXN0IGJlIHRyYWluZWQgc2VwYXJhdGVseSBmb3IgZWFjaCBxdWFudGlsZSwgb3Igam9pbnRseSB3aXRoIGEgbXVsdGktb3V0cHV0IGhlYWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmVuc2VtYmxlIGltcG9ydCBHcmFkaWVudEJvb3N0aW5nUmVncmVzc29yXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxubnAucmFuZG9tLnNlZWQoNDIpXG5uX3RyYWluLCBuX3Rlc3QsIGhvcml6b24gPSA1MDAsIDEwMCwgMVxudF9hbGwgPSBucC5hcmFuZ2Uobl90cmFpbiArIG5fdGVzdClcbnlfYWxsID0gKG5wLnNpbigyICogbnAucGkgKiB0X2FsbCAvIDUyKSAgICAgICAgICAjIGFubnVhbCBzZWFzb25hbGl0eVxuICAgICAgICAgKyAwLjUgKiBucC5zaW4oMiAqIG5wLnBpICogdF9hbGwgLyAxMykgICMgcXVhcnRlcmx5XG4gICAgICAgICArIG5wLnJhbmRvbS5yYW5kbihsZW4odF9hbGwpKSAqIDAuNSlcblxuZGVmIG1ha2VfZmVhdHVyZXMoeSwgbGFncz0xMik6XG4gICAgWCA9IG5wLnN0YWNrKFt5W2k6bGVuKHkpLWxhZ3MraV0gZm9yIGkgaW4gcmFuZ2UobGFncyldLCBheGlzPTEpXG4gICAgcmV0dXJuIFhbOi0xXSwgeVtsYWdzOl1cblxuWF9hbGwsIHlfZmVhdCA9IG1ha2VfZmVhdHVyZXMoeV9hbGwpXG5YX3RyYWluLCB5X3RyYWluID0gWF9hbGxbOm5fdHJhaW5dLCB5X2ZlYXRbOm5fdHJhaW5dXG5YX3Rlc3QsICB5X3Rlc3QgID0gWF9hbGxbbl90cmFpbjpdLCB5X2ZlYXRbbl90cmFpbjpdXG5cbnF1YW50aWxlcyA9IFswLjEsIDAuNSwgMC45XVxuZm9yZWNhc3RzID0ge31cbmZvciBxIGluIHF1YW50aWxlczpcbiAgICBnYnIgPSBHcmFkaWVudEJvb3N0aW5nUmVncmVzc29yKGxvc3M9XHUwMDI3cXVhbnRpbGVcdTAwMjcsIGFscGhhPXEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX2VzdGltYXRvcnM9MTAwLCBtYXhfZGVwdGg9MylcbiAgICBnYnIuZml0KFhfdHJhaW4sIHlfdHJhaW4pXG4gICAgZm9yZWNhc3RzW3FdID0gZ2JyLnByZWRpY3QoWF90ZXN0KVxuXG5jb3ZlcmFnZSA9IG5wLm1lYW4oKHlfdGVzdCBcdTAwM2U9IGZvcmVjYXN0c1swLjFdKSBcdTAwMjYgKHlfdGVzdCBcdTAwM2M9IGZvcmVjYXN0c1swLjldKSlcbnByaW50KGZcdTAwMjdOb21pbmFsIDgwJSBQSSBjb3ZlcmFnZToge2NvdmVyYWdlOi4zZn0gKHRhcmdldCAwLjgwKVx1MDAyNylcbnByaW50KGZcdTAwMjdNZWRpYW4gTUFFOiB7bnAuYWJzKHlfdGVzdCAtIGZvcmVjYXN0c1swLjVdKS5tZWFuKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdNZWFuIFBJIHdpZHRoOiB7KGZvcmVjYXN0c1swLjldIC0gZm9yZWNhc3RzWzAuMV0pLm1lYW4oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNSUFMg4oCUIENvbnRpbnVvdXMgUmFua2VkIFByb2JhYmlsaXR5IFNjb3JlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDUlBTIChDb250aW51b3VzIFJhbmtlZCBQcm9iYWJpbGl0eSBTY29yZSkgaXMgYSBwcm9wZXIgc2NvcmluZyBydWxlIGZvciBldmFsdWF0aW5nIGRpc3RyaWJ1dGlvbmFsIGZvcmVjYXN0cy4gRm9yIGEgZm9yZWNhc3QgQ0RGIEYgYW5kIG9ic2VydmF0aW9uIHk6IENSUFMoRiwgeSkgPSDiiKtbRih6KSAtIDEoeiDiiaUgeSldwrIgZHogPSBFW3xYIC0geXxdIC0gKDEvMilFW3xYIC0gWFx1MDAyN3xdIHdoZXJlIFgsIFhcdTAwMjcgfiBGIGluZGVwZW5kZW50bHkuIExvd2VyIENSUFMgaXMgYmV0dGVyLiBDUlBTIGdlbmVyYWxpc2VzIE1BRTogaWYgRiBpcyBhIHBvaW50IG1hc3MgYXQgxbcsIENSUFMgPSB8eSAtIMW3fCA9IE1BRS4gSXQgcmV3YXJkcyBib3RoIGFjY3VyYWN5IChsb3cgYmlhcykgYW5kIGNhbGlicmF0aW9uIChhcHByb3ByaWF0ZSBzcHJlYWQpLiBGb3IgZW5zZW1ibGUgZm9yZWNhc3RzIHdpdGggTSBzYW1wbGVzLCBDUlBTID0gKDEvTSnOo3x4X20gLSB5fCAtICgxLzJNwrIpzqN8eF9tIC0geF97bVx1MDAyN318LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IG5vcm1cblxuZGVmIGNycHNfZ2F1c3NpYW4obXUsIHNpZ21hLCB5KTpcbiAgICBcIlwiXCJBbmFseXRpY2FsIENSUFMgZm9yIEdhdXNzaWFuIHByZWRpY3RpdmUgZGlzdHJpYnV0aW9uLlwiXCJcIlxuICAgIHogPSAoeSAtIG11KSAvIHNpZ21hXG4gICAgcGhpID0gbm9ybS5wZGYoeilcbiAgICBQaGkgPSBub3JtLmNkZih6KVxuICAgIHJldHVybiBzaWdtYSAqICh6ICogKDIqUGhpIC0gMSkgKyAyKnBoaSAtIDEvbnAuc3FydChucC5waSkpXG5cbmRlZiBjcnBzX2Vuc2VtYmxlKHNhbXBsZXMsIHkpOlxuICAgIFwiXCJcIkNSUFMgZnJvbSBlbnNlbWJsZSBzYW1wbGVzOiBFfFgteXwgLSAwLjUqRXxYLVhcdTAwMjd8LlwiXCJcIlxuICAgIE0gPSBzYW1wbGVzLnNoYXBlWzBdXG4gICAgdGVybTEgPSBucC5tZWFuKG5wLmFicyhzYW1wbGVzIC0geSkpXG4gICAgdGVybTIgPSBucC5tZWFuKG5wLmFicyhzYW1wbGVzWzosIE5vbmVdIC0gc2FtcGxlc1tOb25lLCA6XSkpXG4gICAgcmV0dXJuIHRlcm0xIC0gMC41ICogdGVybTJcblxubnAucmFuZG9tLnNlZWQoMClcbnlfdHJ1ZSA9IG5wLnJhbmRvbS5yYW5kbigyMDApICogMiArIDVcbm11X3ByZWQgPSA1LjAgKiBucC5vbmVzKDIwMClcbnNpZ21hX2dvb2QgPSAyLjAgKiBucC5vbmVzKDIwMClcbnNpZ21hX2JhZCAgPSA1LjAgKiBucC5vbmVzKDIwMClcblxuY3Jwc19nb29kID0gY3Jwc19nYXVzc2lhbihtdV9wcmVkLCBzaWdtYV9nb29kLCB5X3RydWUpLm1lYW4oKVxuY3Jwc19iYWQgID0gY3Jwc19nYXVzc2lhbihtdV9wcmVkLCBzaWdtYV9iYWQsICB5X3RydWUpLm1lYW4oKVxucG9pbnRfbWFlID0gbnAuYWJzKHlfdHJ1ZSAtIG11X3ByZWQpLm1lYW4oKVxucHJpbnQoZlx1MDAyN0NSUFMgKHNpZ21hPTIuMCwgY29ycmVjdCk6IHtjcnBzX2dvb2Q6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdDUlBTIChzaWdtYT01LjAsIHRvbyB3aWRlKToge2NycHNfYmFkOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3UG9pbnQgTUFFIChzYW1lIG1lYW4pOiAgICAgIHtwb2ludF9tYWU6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN0NSUFMgcGVuYWxpc2VzIGJvdGggYmlhcyBhbmQgbWlzY2FsaWJyYXRlZCBzcHJlYWQuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwbGl0IENvbmZvcm1hbCBQcmVkaWN0aW9uIGZvciBUaW1lIFNlcmllcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29uZm9ybWFsIHByZWRpY3Rpb24gcHJvdmlkZXMgYSBkaXN0cmlidXRpb24tZnJlZSBwcmVkaWN0aW9uIGludGVydmFsIHdpdGggYSBmaW5pdGUtc2FtcGxlIGNvdmVyYWdlIGd1YXJhbnRlZTogUCh5X3tuKzF9IOKIiCBDKHhfe24rMX0pKSDiiaUgMS3OsS4gU3BsaXQgY29uZm9ybWFsOiAoMSkgZml0IGEgcG9pbnQgZm9yZWNhc3QgbW9kZWwgb24gYSB0cmFpbmluZyBzZXQsICgyKSBjb21wdXRlIG5vbmNvbmZvcm1pdHkgc2NvcmVzIHNfaSA9IHx5X2kgLSDFt19pfCBvbiBhIGhlbGQtb3V0IGNhbGlicmF0aW9uIHNldCwgKDMpIHNldCB0aHJlc2hvbGQgccyCID0gKDEtzrEpKDEgKyAxL25fe2NhbH0pIHF1YW50aWxlIG9mIGNhbGlicmF0aW9uIHNjb3JlcywgKDQpIGludGVydmFsID0gW8W3X3tuKzF9IC0gccyCLCDFt197bisxfSArIHHMgl0uIFRoZSBjb3ZlcmFnZSBndWFyYW50ZWUgaG9sZHMgdW5kZXIgZXhjaGFuZ2VhYmlsaXR5IG9mIGNhbGlicmF0aW9uIGFuZCB0ZXN0IHBvaW50cywgd2hpY2ggaXMgYXBwcm94aW1hdGVseSBzYXRpc2ZpZWQgZm9yIHNob3J0LXJhbmdlIHRpbWUgc2VyaWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxubnAucmFuZG9tLnNlZWQoNDIpXG5UID0gNDAwXG50ID0gbnAuYXJhbmdlKFQpXG55ID0gbnAuc2luKDIgKiBucC5waSAqIHQgLyA1MikgKyAwLjMgKiB0IC8gVCArIG5wLnJhbmRvbS5yYW5kbihUKSAqIDAuM1xuXG5kZWYgbGFnX2ZlYXR1cmVzKHksIG5fbGFncz04KTpcbiAgICBYID0gbnAuc3RhY2soW3lbaTpsZW4oeSktbl9sYWdzK2ldIGZvciBpIGluIHJhbmdlKG5fbGFncyldLCBheGlzPTEpXG4gICAgcmV0dXJuIFhbOi0xXSwgeVtuX2xhZ3M6XVxuXG5YLCB5X2ZlYXQgPSBsYWdfZmVhdHVyZXMoeSlcbm5fdHJhaW4sIG5fY2FsID0gMjUwLCAxMDBcblhfdHJhaW4sIHlfdHJhaW4gPSBYWzpuX3RyYWluXSwgeV9mZWF0WzpuX3RyYWluXVxuWF9jYWwsICAgeV9jYWwgICA9IFhbbl90cmFpbjpuX3RyYWluK25fY2FsXSwgeV9mZWF0W25fdHJhaW46bl90cmFpbituX2NhbF1cblhfdGVzdCwgIHlfdGVzdCAgPSBYW25fdHJhaW4rbl9jYWw6XSwgeV9mZWF0W25fdHJhaW4rbl9jYWw6XVxuXG5tb2RlbCA9IFJpZGdlKGFscGhhPTEuMCkuZml0KFhfdHJhaW4sIHlfdHJhaW4pXG5jYWxfc2NvcmVzID0gbnAuYWJzKHlfY2FsIC0gbW9kZWwucHJlZGljdChYX2NhbCkpICAjIG5vbmNvbmZvcm1pdHkgc2NvcmVzXG5cbmFscGhhID0gMC4xMFxucV9sZXZlbCA9IG5wLmNlaWwoKDEgLSBhbHBoYSkgKiAobl9jYWwgKyAxKSkgLyBuX2NhbFxucV9oYXQgPSBucC5xdWFudGlsZShjYWxfc2NvcmVzLCBtaW4ocV9sZXZlbCwgMS4wKSlcblxueV9wcmVkID0gbW9kZWwucHJlZGljdChYX3Rlc3QpXG5sb3dlciwgdXBwZXIgPSB5X3ByZWQgLSBxX2hhdCwgeV9wcmVkICsgcV9oYXRcbmNvdmVyYWdlID0gbnAubWVhbigoeV90ZXN0IFx1MDAzZT0gbG93ZXIpIFx1MDAyNiAoeV90ZXN0IFx1MDAzYz0gdXBwZXIpKVxucHJpbnQoZlx1MDAyN1NwbGl0IGNvbmZvcm1hbCB0aHJlc2hvbGQgcV9oYXQ6IHtxX2hhdDouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0VtcGlyaWNhbCBjb3ZlcmFnZToge2NvdmVyYWdlOi4zZn0gICh0YXJnZXQ6IHsxLWFscGhhOi4yZn0pXHUwMDI3KVxucHJpbnQoZlx1MDAyN01lYW4gaW50ZXJ2YWwgd2lkdGg6IHsodXBwZXIgLSBsb3dlcikubWVhbigpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQWRhcHRpdmUgQ29uZm9ybWFsIFByZWRpY3Rpb24gZm9yIE5vbi1TdGF0aW9uYXJ5IFNlcmllcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgc3BsaXQgY29uZm9ybWFsIGFzc3VtZXMgZXhjaGFuZ2VhYmlsaXR5LCB3aGljaCBmYWlscyB1bmRlciBkaXN0cmlidXRpb24gc2hpZnQuIEFkYXB0aXZlIGNvbmZvcm1hbCBwcmVkaWN0aW9uIChBQ0kpIHVwZGF0ZXMgdGhlIHNpZ25pZmljYW5jZSBsZXZlbCDOsV90IG9ubGluZTogzrFfe3QrMX0gPSDOsV90ICsgzrMozrEgLSBlcnJfdCkgd2hlcmUgZXJyX3QgPSAxKHlfdCDiiIkgQ190KS4gVGhpcyBmb3JjZXMgbG9uZy1ydW4gY292ZXJhZ2UgdG8gZXF1YWwgdGhlIHRhcmdldCAxLc6xLiBFbmJQSSAoRW5zZW1ibGUgQmF0Y2ggUHJlZGljdGlvbiBJbnRlcnZhbHMpIGZ1cnRoZXIgdXNlcyBsZWF2ZS1vbmUtb3V0IGVuc2VtYmxlIHJlc2lkdWFscyBvbiBhIHJvbGxpbmcgd2luZG93IGZvciBtb3JlIGFkYXB0aXZlIGludGVydmFsIHdpZHRocy4gQm90aCBtZXRob2RzIGhhbmRsZSBjb25jZXB0IGRyaWZ0IHdpdGhvdXQgcmV0cmFpbmluZyB0aGUgcG9pbnQgZm9yZWNhc3QgbW9kZWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUmlkZ2VcblxubnAucmFuZG9tLnNlZWQoMClcblRfdHJhaW4sIFRfdGVzdCA9IDIwMCwgMTUwXG50X2FsbCA9IG5wLmFyYW5nZShUX3RyYWluICsgVF90ZXN0KVxueV9hbGwgPSBucC5zaW4oMiAqIG5wLnBpICogdF9hbGwgLyAzMCkgKyBucC5yYW5kb20ucmFuZG4obGVuKHRfYWxsKSkgKiAwLjJcbiMgSW5qZWN0IGRpc3RyaWJ1dGlvbiBzaGlmdCBhdCB0PVRfdHJhaW5cbnlfYWxsW1RfdHJhaW46XSArPSAyLjBcblxuZGVmIGxhZ19mZWF0dXJlcyh5LCBsYWdzPTYpOlxuICAgIFggPSBucC5zdGFjayhbeVtpOmxlbih5KS1sYWdzK2ldIGZvciBpIGluIHJhbmdlKGxhZ3MpXSwgYXhpcz0xKVxuICAgIHJldHVybiBYWzotMV0sIHlbbGFnczpdXG5cblhfYWxsLCB5X2ZlYXQgPSBsYWdfZmVhdHVyZXMoeV9hbGwpXG5YX3RyLCB5X3RyID0gWF9hbGxbOlRfdHJhaW5dLCB5X2ZlYXRbOlRfdHJhaW5dXG5YX3RlLCB5X3RlID0gWF9hbGxbVF90cmFpbjpdLCB5X2ZlYXRbVF90cmFpbjpdXG5cbm1vZGVsID0gUmlkZ2UoYWxwaGE9MS4wKS5maXQoWF90ciwgeV90cilcbmFscGhhX3RhcmdldCA9IDAuMTBcbmdhbW1hID0gMC4wMDVcbmFscGhhcywgY292ZXJlZCA9IFthbHBoYV90YXJnZXRdLCBbXVxuXG5jYWxfc2NvcmVzID0gbnAuYWJzKHlfdHIgLSBtb2RlbC5wcmVkaWN0KFhfdHIpKVxuZm9yIGkgaW4gcmFuZ2UobGVuKFhfdGUpKTpcbiAgICBhbHBoYV90ID0gYWxwaGFzWy0xXVxuICAgIHFfaGF0ID0gbnAucXVhbnRpbGUoY2FsX3Njb3JlcywgbWluKDEgLSBhbHBoYV90LCAxLjApKVxuICAgIHByZWQgICA9IG1vZGVsLnByZWRpY3QoWF90ZVtbaV1dKVswXVxuICAgIG1pc3NlZCA9IGludCh5X3RlW2ldIFx1MDAzYyBwcmVkIC0gcV9oYXQgb3IgeV90ZVtpXSBcdTAwM2UgcHJlZCArIHFfaGF0KVxuICAgIGNvdmVyZWQuYXBwZW5kKDEgLSBtaXNzZWQpXG4gICAgYWxwaGFzLmFwcGVuZChhbHBoYV90ICsgZ2FtbWEgKiAoYWxwaGFfdGFyZ2V0IC0gbWlzc2VkKSlcblxucHJpbnQoZlx1MDAyN0FDSSBlbXBpcmljYWwgY292ZXJhZ2U6IHtucC5tZWFuKGNvdmVyZWQpOi4zZn0gKHRhcmdldCB7MS1hbHBoYV90YXJnZXQ6LjJmfSlcdTAwMjcpXG5wcmludChmXHUwMDI3RmluYWwgYWxwaGE6IHthbHBoYXNbLTFdOi40Zn0gIChzdGFydGVkIGF0IHthbHBoYV90YXJnZXQ6LjJmfSlcdTAwMjcpXG5wcmludChcdTAwMjdBbHBoYSBhZGFwdHMgdXB3YXJkIHdoZW4gY292ZXJhZ2UgaXMgdG9vIGxvdywgZG93bndhcmQgd2hlbiBvdmVyLWNvdmVyaW5nLlx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkNvbmZvcm1hbCBQcmVkaWN0aW9uIElzIE5vdCBhIE1hZ2ljIEJ1bGxldCIsImNvbnRlbnQiOiJDb25mb3JtYWwgcHJlZGljdGlvbiBndWFyYW50ZWVzIG1hcmdpbmFsIGNvdmVyYWdlIGF2ZXJhZ2VkIG92ZXIgdGhlIGNhbGlicmF0aW9uIGRpc3RyaWJ1dGlvbi4gSXQgZG9lcyBub3QgZ3VhcmFudGVlIGNvbmRpdGlvbmFsIGNvdmVyYWdlIChlLmcuLCBjb3ZlcmFnZSBvbiBwZWFrcyBvbmx5KS4gRm9yIGhpZ2hseSBub24tc3RhdGlvbmFyeSBzZXJpZXMgdGhlIGV4Y2hhbmdlYWJpbGl0eSBhc3N1bXB0aW9uIGJyZWFrcyBkb3duLCBsZWFkaW5nIHRvIHVuZGVyLWNvdmVyYWdlIGR1cmluZyBzaGlmdHMuIFVzZSBBQ0kgb3Igc2xpZGluZy13aW5kb3cgY2FsaWJyYXRpb24gdG8gbWl0aWdhdGUgdGhpcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIG9mIFByb2JhYmlsaXN0aWMgRm9yZWNhc3QgTWV0aG9kcyJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJDb3ZlcmFnZSBHdWFyYW50ZWUiLCJDYWxpYnJhdGlvbiIsIkRpc3RyaWJ1dGlvbiBBc3N1bXB0aW9uIiwiSGFuZGxlcyBTaGlmdCIsIkNvbXB1dGUgQ29zdCJdLCJyb3dzIjpbWyJRdWFudGlsZSByZWdyZXNzaW9uIiwiTm8gKGFzeW1wdG90aWMpIiwiVHJhaW5pbmctZGF0YSBkZXBlbmRlbnQiLCJOb25lIChtb2RlbC1iYXNlZCkiLCJJZiByZXRyYWluZWQiLCJMb3ciXSxbIkNvbmZvcm1hbCBwcmVkaWN0aW9uIiwiWWVzIChmaW5pdGUtc2FtcGxlKSIsIkV4Y2hhbmdlYWJpbGl0eSByZXF1aXJlZCIsIkRpc3RyaWJ1dGlvbi1mcmVlIiwiQUNJIHZhcmlhbnQgbmVlZGVkIiwiVmVyeSBsb3ciXSxbIkJheWVzaWFuIChHUCwgQk5OKSIsIkFwcHJveGltYXRlIiwiUHJpb3ItZGVwZW5kZW50IiwiRnVsbCBwcm9iYWJpbGlzdGljIG1vZGVsIiwiTGltaXRlZCIsIkhpZ2giXSxbIkVuc2VtYmxlIChNNCwgTldQKSIsIk5vIChlbXBpcmljYWwpIiwiR29vZCB3aXRoIGRpdmVyc2UgbW9kZWxzIiwiTm9uZSAobW9kZWwtYmFzZWQpIiwiUGFydGlhbCIsIk1lZGl1bSJdLFsiQ1JQUy1vcHRpbWlzZWQiLCJObyBndWFyYW50ZWUiLCJQcm9wZXIgc2NvcmluZyIsIk5vbmUiLCJJZiByZXRyYWluZWQiLCJMb3figJNNZWRpdW0iXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVuc2VtYmxlIEZvcmVjYXN0cyBhbmQgUHJhY3RpY2FsIEd1aWRhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFbnNlbWJsZSBmb3JlY2FzdHMgY29tYmluZSBwcmVkaWN0aW9ucyBmcm9tIG11bHRpcGxlIG1vZGVscyBvciBwYXJhbWV0ZXIgZHJhd3MuIEVtcGlyaWNhbGx5LCBlbnNlbWJsaW5nIDEw4oCTMjAgZGl2ZXJzZSBtb2RlbHMgcmVkdWNlcyB2YXJpYW5jZSBieSAzMOKAkzUwJSB2ZXJzdXMgYW55IHNpbmdsZSBtb2RlbC4gVGhlIE00IGNvbXBldGl0aW9uIHdpbm5lciB1c2VkIGEgY29tYmluYXRpb24gb2Ygc3RhdGlzdGljYWwgKEVUUywgQVJJTUEpIGFuZCBuZXVyYWwgbW9kZWxzLiBGb3Igb3BlcmF0aW9uYWwgc3lzdGVtcywgYSBzaW1wbGUgbWVhbiBvciBtZWRpYW4gZW5zZW1ibGUgb2YgM+KAkzUgd2VsbC10dW5lZCBtb2RlbHMgb2Z0ZW4gYWNoaWV2ZXMgOTAlIG9mIHRoZSBnYWluIG9mIGEgc29waGlzdGljYXRlZCBlbnNlbWJsZS4gQWx3YXlzIGV2YWx1YXRlIHByb2JhYmlsaXN0aWMgZm9yZWNhc3RzIHdpdGggcHJvcGVyIHNjb3JpbmcgcnVsZXMgKENSUFMsIFdRTCkgcmF0aGVyIHRoYW4ganVzdCBpbnRlcnZhbCB3aWR0aC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlBpbmJhbGwgbG9zcyA9IHF1YW50aWxlIGxvc3M7IG9wdGltaXNlIGRpcmVjdGx5IGZvciBxdWFudGlsZSBmb3JlY2FzdHMuIiwiQ1JQUyBpcyB0aGUgZ29sZCBzdGFuZGFyZCBmb3IgZXZhbHVhdGluZyBwcm9iYWJpbGlzdGljIGZvcmVjYXN0czsgYWx3YXlzIHJlcG9ydCBpdCBhbG9uZ3NpZGUgTUFFLiIsIjgwJSBQSSA9IFtRXzAuMSwgUV8wLjldOyA5MCUgUEkgPSBbUV8wLjA1LCBRXzAuOTVdOyByZXBvcnQgbm9taW5hbCBhbmQgZW1waXJpY2FsIGNvdmVyYWdlLiIsIkNhbGlicmF0aW9uIHBsb3Q6IHNjYXR0ZXIgbm9taW5hbCBjb3ZlcmFnZSB2cyBlbXBpcmljYWwgY292ZXJhZ2UgYWNyb3NzIG11bHRpcGxlIHF1YW50aWxlIGxldmVscy4iLCJGb3Igc3BsaXQgY29uZm9ybWFsLCBjYWxpYnJhdGlvbiBzZXQgc2l6ZSBuX2NhbCBcdTAwM2U9IDIwMCBmb3Igc3RhYmxlIGNvdmVyYWdlIGVzdGltYXRlcy4iLCJFbmJQSTogdXNlIG5fYm9vdHN0cmFwPTMwIHdpdGggYSByb2xsaW5nIGNhbGlicmF0aW9uIHdpbmRvdyBvZiA2MOKAkzEyMCBvYnNlcnZhdGlvbnMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Probabilistic Forecasting — Quantile Regression and Conformal Prediction

Point forecasts are insufficient for most real-world decisions. A retailer stocking inventory needs not just the expected demand but a range it might fall in. An electricity grid operator needs to know the probability of demand exceeding a threshold. Probabilistic forecasting quantifies this uncertainty by producing distributions, prediction intervals, or quantile estimates rather than a single number. This note covers quantile regression, CRPS evaluation, and conformal prediction — a distribution-free method with finite-sample coverage guarantees.

## Why Point Forecasts Are Insufficient

A point forecast minimises expected loss under a specific loss function (e.g., MAE minimises median, MSE minimises mean). But decision-making under uncertainty requires knowing the full predictive distribution or at least key quantiles. For asymmetric costs — where stockouts cost more than overstocking — the optimal action depends on quantiles, not the mean. For safety-critical systems, the 99th percentile matters more than the expected value.

## Quantile Regression

Quantile regression predicts the τ-th quantile Q_τ(y|x) for multiple levels τ ∈ {0.1, 0.2, ..., 0.9}. The pinball loss (also called quantile loss) is: L_τ(y, q) = τ(y-q) if y ≥ q, else (1-τ)(q-y). Minimising this loss over the training set yields a calibrated quantile estimate. A prediction interval [Q_0.1, Q_0.9] gives an 80% nominal interval. The model must be trained separately for each quantile, or jointly with a multi-output head.

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n_train, n_test, horizon = 500, 100, 1
t_all = np.arange(n_train + n_test)
y_all = (np.sin(2 * np.pi * t_all / 52)          # annual seasonality
         + 0.5 * np.sin(2 * np.pi * t_all / 13)  # quarterly
         + np.random.randn(len(t_all)) * 0.5)

def make_features(y, lags=12):
    X = np.stack([y[i:len(y)-lags+i] for i in range(lags)], axis=1)
    return X[:-1], y[lags:]

X_all, y_feat = make_features(y_all)
X_train, y_train = X_all[:n_train], y_feat[:n_train]
X_test,  y_test  = X_all[n_train:], y_feat[n_train:]

quantiles = [0.1, 0.5, 0.9]
forecasts = {}
for q in quantiles:
    gbr = GradientBoostingRegressor(loss='quantile', alpha=q,
                                    n_estimators=100, max_depth=3)
    gbr.fit(X_train, y_train)
    forecasts[q] = gbr.predict(X_test)

coverage = np.mean((y_test >= forecasts[0.1]) & (y_test <= forecasts[0.9]))
print(f'Nominal 80% PI coverage: {coverage:.3f} (target 0.80)')
print(f'Median MAE: {np.abs(y_test - forecasts[0.5]).mean():.4f}')
print(f'Mean PI width: {(forecasts[0.9] - forecasts[0.1]).mean():.4f}')
```

## CRPS — Continuous Ranked Probability Score

CRPS (Continuous Ranked Probability Score) is a proper scoring rule for evaluating distributional forecasts. For a forecast CDF F and observation y: CRPS(F, y) = ∫[F(z) - 1(z ≥ y)]² dz = E[|X - y|] - (1/2)E[|X - X'|] where X, X' ~ F independently. Lower CRPS is better. CRPS generalises MAE: if F is a point mass at ŷ, CRPS = |y - ŷ| = MAE. It rewards both accuracy (low bias) and calibration (appropriate spread). For ensemble forecasts with M samples, CRPS = (1/M)Σ|x_m - y| - (1/2M²)Σ|x_m - x_{m'}|.

```python
import numpy as np
from scipy.stats import norm

def crps_gaussian(mu, sigma, y):
    """Analytical CRPS for Gaussian predictive distribution."""
    z = (y - mu) / sigma
    phi = norm.pdf(z)
    Phi = norm.cdf(z)
    return sigma * (z * (2*Phi - 1) + 2*phi - 1/np.sqrt(np.pi))

def crps_ensemble(samples, y):
    """CRPS from ensemble samples: E|X-y| - 0.5*E|X-X'|."""
    M = samples.shape[0]
    term1 = np.mean(np.abs(samples - y))
    term2 = np.mean(np.abs(samples[:, None] - samples[None, :]))
    return term1 - 0.5 * term2

np.random.seed(0)
y_true = np.random.randn(200) * 2 + 5
mu_pred = 5.0 * np.ones(200)
sigma_good = 2.0 * np.ones(200)
sigma_bad  = 5.0 * np.ones(200)

crps_good = crps_gaussian(mu_pred, sigma_good, y_true).mean()
crps_bad  = crps_gaussian(mu_pred, sigma_bad,  y_true).mean()
point_mae = np.abs(y_true - mu_pred).mean()
print(f'CRPS (sigma=2.0, correct): {crps_good:.4f}')
print(f'CRPS (sigma=5.0, too wide): {crps_bad:.4f}')
print(f'Point MAE (same mean):      {point_mae:.4f}')
print('CRPS penalises both bias and miscalibrated spread.')
```

## Split Conformal Prediction for Time Series

Conformal prediction provides a distribution-free prediction interval with a finite-sample coverage guarantee: P(y_{n+1} ∈ C(x_{n+1})) ≥ 1-α. Split conformal: (1) fit a point forecast model on a training set, (2) compute nonconformity scores s_i = |y_i - ŷ_i| on a held-out calibration set, (3) set threshold q̂ = (1-α)(1 + 1/n_{cal}) quantile of calibration scores, (4) interval = [ŷ_{n+1} - q̂, ŷ_{n+1} + q̂]. The coverage guarantee holds under exchangeability of calibration and test points, which is approximately satisfied for short-range time series.

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
T = 400
t = np.arange(T)
y = np.sin(2 * np.pi * t / 52) + 0.3 * t / T + np.random.randn(T) * 0.3

def lag_features(y, n_lags=8):
    X = np.stack([y[i:len(y)-n_lags+i] for i in range(n_lags)], axis=1)
    return X[:-1], y[n_lags:]

X, y_feat = lag_features(y)
n_train, n_cal = 250, 100
X_train, y_train = X[:n_train], y_feat[:n_train]
X_cal,   y_cal   = X[n_train:n_train+n_cal], y_feat[n_train:n_train+n_cal]
X_test,  y_test  = X[n_train+n_cal:], y_feat[n_train+n_cal:]

model = Ridge(alpha=1.0).fit(X_train, y_train)
cal_scores = np.abs(y_cal - model.predict(X_cal))  # nonconformity scores

alpha = 0.10
q_level = np.ceil((1 - alpha) * (n_cal + 1)) / n_cal
q_hat = np.quantile(cal_scores, min(q_level, 1.0))

y_pred = model.predict(X_test)
lower, upper = y_pred - q_hat, y_pred + q_hat
coverage = np.mean((y_test >= lower) & (y_test <= upper))
print(f'Split conformal threshold q_hat: {q_hat:.4f}')
print(f'Empirical coverage: {coverage:.3f}  (target: {1-alpha:.2f})')
print(f'Mean interval width: {(upper - lower).mean():.4f}')
```

## Adaptive Conformal Prediction for Non-Stationary Series

Standard split conformal assumes exchangeability, which fails under distribution shift. Adaptive conformal prediction (ACI) updates the significance level α_t online: α_{t+1} = α_t + γ(α - err_t) where err_t = 1(y_t ∉ C_t). This forces long-run coverage to equal the target 1-α. EnbPI (Ensemble Batch Prediction Intervals) further uses leave-one-out ensemble residuals on a rolling window for more adaptive interval widths. Both methods handle concept drift without retraining the point forecast model.

```python
import numpy as np
from sklearn.linear_model import Ridge

np.random.seed(0)
T_train, T_test = 200, 150
t_all = np.arange(T_train + T_test)
y_all = np.sin(2 * np.pi * t_all / 30) + np.random.randn(len(t_all)) * 0.2
# Inject distribution shift at t=T_train
y_all[T_train:] += 2.0

def lag_features(y, lags=6):
    X = np.stack([y[i:len(y)-lags+i] for i in range(lags)], axis=1)
    return X[:-1], y[lags:]

X_all, y_feat = lag_features(y_all)
X_tr, y_tr = X_all[:T_train], y_feat[:T_train]
X_te, y_te = X_all[T_train:], y_feat[T_train:]

model = Ridge(alpha=1.0).fit(X_tr, y_tr)
alpha_target = 0.10
gamma = 0.005
alphas, covered = [alpha_target], []

cal_scores = np.abs(y_tr - model.predict(X_tr))
for i in range(len(X_te)):
    alpha_t = alphas[-1]
    q_hat = np.quantile(cal_scores, min(1 - alpha_t, 1.0))
    pred   = model.predict(X_te[[i]])[0]
    missed = int(y_te[i] < pred - q_hat or y_te[i] > pred + q_hat)
    covered.append(1 - missed)
    alphas.append(alpha_t + gamma * (alpha_target - missed))

print(f'ACI empirical coverage: {np.mean(covered):.3f} (target {1-alpha_target:.2f})')
print(f'Final alpha: {alphas[-1]:.4f}  (started at {alpha_target:.2f})')
print('Alpha adapts upward when coverage is too low, downward when over-covering.')
```

> **Conformal Prediction Is Not a Magic Bullet**: Conformal prediction guarantees marginal coverage averaged over the calibration distribution. It does not guarantee conditional coverage (e.g., coverage on peaks only). For highly non-stationary series the exchangeability assumption breaks down, leading to under-coverage during shifts. Use ACI or sliding-window calibration to mitigate this.

## Comparison of Probabilistic Forecast Methods

| Method | Coverage Guarantee | Calibration | Distribution Assumption | Handles Shift | Compute Cost |
| --- | --- | --- | --- | --- | --- |
| Quantile regression | No (asymptotic) | Training-data dependent | None (model-based) | If retrained | Low |
| Conformal prediction | Yes (finite-sample) | Exchangeability required | Distribution-free | ACI variant needed | Very low |
| Bayesian (GP, BNN) | Approximate | Prior-dependent | Full probabilistic model | Limited | High |
| Ensemble (M4, NWP) | No (empirical) | Good with diverse models | None (model-based) | Partial | Medium |
| CRPS-optimised | No guarantee | Proper scoring | None | If retrained | Low–Medium |

## Ensemble Forecasts and Practical Guidance

Ensemble forecasts combine predictions from multiple models or parameter draws. Empirically, ensembling 10–20 diverse models reduces variance by 30–50% versus any single model. The M4 competition winner used a combination of statistical (ETS, ARIMA) and neural models. For operational systems, a simple mean or median ensemble of 3–5 well-tuned models often achieves 90% of the gain of a sophisticated ensemble. Always evaluate probabilistic forecasts with proper scoring rules (CRPS, WQL) rather than just interval width.

- Pinball loss = quantile loss; optimise directly for quantile forecasts.
- CRPS is the gold standard for evaluating probabilistic forecasts; always report it alongside MAE.
- 80% PI = [Q_0.1, Q_0.9]; 90% PI = [Q_0.05, Q_0.95]; report nominal and empirical coverage.
- Calibration plot: scatter nominal coverage vs empirical coverage across multiple quantile levels.
- For split conformal, calibration set size n_cal >= 200 for stable coverage estimates.
- EnbPI: use n_bootstrap=30 with a rolling calibration window of 60–120 observations.

---

