---
title: "Mahalanobis Distance — Multivariate Anomaly Detection"
slug: "mahalanobis-distance-anomaly"
description: "Detect multivariate anomalies using Mahalanobis distance with chi-squared thresholds and robust MCD estimation — and see exactly why Euclidean distance fails on correlated features."
tags: ["anomaly-detection", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXVjbGlkZWFuIGRpc3RhbmNlIHRyZWF0cyBldmVyeSBmZWF0dXJlIGRpbWVuc2lvbiBhcyBlcXVhbGx5IGltcG9ydGFudCBhbmQgaW5kZXBlbmRlbnQuIFdoZW4gZmVhdHVyZXMgYXJlIGNvcnJlbGF0ZWQgb3IgaGF2ZSBkaWZmZXJlbnQgc2NhbGVzLCBFdWNsaWRlYW4gZGlzdGFuY2UgbWlzaWRlbnRpZmllcyB3aGljaCBwb2ludHMgYXJlIHRydWx5IHVudXN1YWwuIE1haGFsYW5vYmlzIGRpc3RhbmNlIGNvcnJlY3RzIGZvciBib3RoIGNvcnJlbGF0aW9uICh2aWEgdGhlIGNvdmFyaWFuY2UgbWF0cml4IM6jKSBhbmQgc2NhbGUgKHZpYSDOo1x1MDAyN3MgZGlhZ29uYWwpLCBwcm9kdWNpbmcgYSBzaW5nbGUgdW5pdGxlc3MgZGlzdGFuY2UgdGhhdCBhY2NvdW50cyBmb3IgdGhlIGpvaW50IGRpc3RyaWJ1dGlvbiBvZiBhbGwgZmVhdHVyZXMgc2ltdWx0YW5lb3VzbHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWFoYWxhbm9iaXMgRGlzdGFuY2Ug4oCUIERlZmluaXRpb24gYW5kIEdlb21ldHJ5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBwb2ludCB4IGluIGQtZGltZW5zaW9uYWwgc3BhY2Ugd2l0aCBwb3B1bGF0aW9uIG1lYW4gzrwgYW5kIGNvdmFyaWFuY2UgzqMsIHRoZSBNYWhhbGFub2JpcyBkaXN0YW5jZSBpcyBkX00oeCkgPSDiiJooKHjiiJLOvCnhtYDOo+KBu8K5KHjiiJLOvCkpLiBUaGUgdGVybSDOo+KBu8K5IHdoaXRlbnMgdGhlIGRhdGE6IGl0IHJvdGF0ZXMgYXhlcyB0byBhbGlnbiB3aXRoIHByaW5jaXBhbCBjb21wb25lbnRzIGFuZCBzY2FsZXMgZWFjaCBheGlzIGJ5IDEv4oiazrvhtaIgd2hlcmUgzrvhtaIgaXMgdGhlIGktdGggZWlnZW52YWx1ZS4gVW5kZXIgYSBtdWx0aXZhcmlhdGUgR2F1c3NpYW4sIGTCsl9NIGZvbGxvd3MgYSBjaGktc3F1YXJlZCBkaXN0cmlidXRpb24gd2l0aCBkIGRlZ3JlZXMgb2YgZnJlZWRvbSDigJQgZ2l2aW5nIGEgcHJpbmNpcGxlZCBzdGF0aXN0aWNhbCB0aHJlc2hvbGQgZm9yIGFueSBkaW1lbnNpb24uIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJkX00oXFxtYXRoYmZ7eH0pID0gXFxzcXJ0eyhcXG1hdGhiZnt4fS1cXGJvbGRzeW1ib2x7XFxtdX0pXlxcdG9wIFxcYm9sZHN5bWJvbHtcXFNpZ21hfV57LTF9IChcXG1hdGhiZnt4fS1cXGJvbGRzeW1ib2x7XFxtdX0pfSwgXFxxdWFkIGRfTV4yIFxcc2ltIFxcY2hpXjIoZCkgXFx0ZXh0eyB1bmRlciBHYXVzc2lhbn0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGcm9tIFNjcmF0Y2ggdnMgc2NpcHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzcXVhcmVkIE1haGFsYW5vYmlzIGRpc3RhbmNlIGNhbiBiZSBjb21wdXRlZCBhcyBhIHF1YWRyYXRpYyBmb3JtIHVzaW5nIHRoZSBpbnZlcnNlIGNvdmFyaWFuY2UgbWF0cml4LiBzY2lweS5zcGF0aWFsLmRpc3RhbmNlLm1haGFsYW5vYmlzIGFjY2VwdHMgdGhlIGludmVyc2UgY292YXJpYW5jZSBtYXRyaXggKFZJIHBhcmFtZXRlcikgZGlyZWN0bHkuIEZvciBiYXRjaGVzIG9mIHBvaW50cywgdXNlIG51bXB5IGVpbnN1bSBmb3IgdmVjdG9yaXNlZCBjb21wdXRhdGlvbi4gV2hlbiB0aGUgY292YXJpYW5jZSBtYXRyaXggaXMgbmVhci1zaW5ndWxhciAoZCBjbG9zZSB0byBuKSwgdXNlIHRoZSBwc2V1ZG9pbnZlcnNlIG9yIHJlZ3VsYXJpc2Ugd2l0aCBhIHNtYWxsIGRpYWdvbmFsOiDOo19yZWcgPSDOoyArIM61SS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnNwYXRpYWwuZGlzdGFuY2UgaW1wb3J0IG1haGFsYW5vYmlzXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBjaGkyXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCA9IG5wLnJhbmRvbS5tdWx0aXZhcmlhdGVfbm9ybWFsKFswLCAwXSwgW1sxLCAwLjhdLCBbMC44LCAxXV0sIDIwMClcblhfdGVzdCA9IG5wLmFycmF5KFtbMy4wLCAzLjBdLCBbMC41LCAtMC41XSwgWy0yLjAsIDIuMF1dKVxuXG5tdSA9IFgubWVhbihheGlzPTApXG5TaWdtYSA9IG5wLmNvdihYLlQpXG5TaWdtYV9pbnYgPSBucC5saW5hbGcuaW52KFNpZ21hKVxuXG5kZWYgbWFoYWxfc2NyYXRjaCh4LCBtdSwgU2lnbWFfaW52KTpcbiAgICBkaWZmID0geCAtIG11XG4gICAgcmV0dXJuIG5wLnNxcnQoZGlmZiBAIFNpZ21hX2ludiBAIGRpZmYpXG5cbmRfc2NyYXRjaCA9IG5wLmFycmF5KFttYWhhbF9zY3JhdGNoKHgsIG11LCBTaWdtYV9pbnYpIGZvciB4IGluIFhfdGVzdF0pXG5kX3NjaXB5ICAgPSBucC5hcnJheShbbWFoYWxhbm9iaXMoeCwgbXUsIFNpZ21hX2ludikgZm9yIHggaW4gWF90ZXN0XSlcbmRfc3EgICAgICA9IG5wLmFycmF5KFsoeC1tdSkgQCBTaWdtYV9pbnYgQCAoeC1tdSkgZm9yIHggaW4gWF90ZXN0XSlcblxucHJpbnQoXHUwMDI3UG9pbnQgICAgICAgICAgIHwgZF9zY3JhdGNoIHwgZF9zY2lweSB8IGReMiAgICB8IHAtdmFsIChjaGkyKVx1MDAyNylcbmZvciBpLCB4IGluIGVudW1lcmF0ZShYX3Rlc3QpOlxuICAgIHB2YWwgPSAxIC0gY2hpMi5jZGYoZF9zcVtpXSwgZGY9MilcbiAgICBwcmludChmXHUwMDI3e3N0cih4KToxNnN9IHwge2Rfc2NyYXRjaFtpXTo5LjRmfSB8IHtkX3NjaXB5W2ldOjcuNGZ9IHwge2Rfc3FbaV06Ni4zZn0gfCB7cHZhbDouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01heCBkaWZmIHNjcmF0Y2ggdnMgc2NpcHk6IHtucC5hYnMoZF9zY3JhdGNoIC0gZF9zY2lweSkubWF4KCk6LjJlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDaGktU3F1YXJlZCBUaHJlc2hvbGQgZm9yIEFub21hbHkgRmxhZ2dpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVuZGVyIGEgbXVsdGl2YXJpYXRlIEdhdXNzaWFuLCBkwrJfTSB+IM+HwrIoZCkuIEFuIGFub21hbHkgdGhyZXNob2xkIGF0IHNpZ25pZmljYW5jZSDOsSBpcyB0aGUgKDHiiJLOsSkgcXVhbnRpbGUgb2Ygz4fCsihkKS4gRm9yIGQ9MiwgzrE9MC4wMSBnaXZlcyB0aHJlc2hvbGQg4omIIDkuMjEgKGRfTSDiiYggMy4wMykuIFRoaXMgdGhyZXNob2xkIHdvcmtzIHJlZ2FyZGxlc3Mgb2YgZmVhdHVyZSBzY2FsZSBhbmQgYXV0b21hdGljYWxseSB0aWdodGVucyBhcyBkaW1lbnNpb24gZCBpbmNyZWFzZXMg4oCUIG9uZSBvZiBNYWhhbGFub2JpcyBkaXN0YW5jZVx1MDAyN3Mga2V5IGFkdmFudGFnZXMgb3ZlciBhZC1ob2MgcGVyLWZlYXR1cmUgWi1zY29yZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgY2hpMlxuXG5ucC5yYW5kb20uc2VlZCg0MilcbmQgPSA0ICAjIGRpbWVuc2lvbnNcblggPSBucC5yYW5kb20ubXVsdGl2YXJpYXRlX25vcm1hbChucC56ZXJvcyhkKSxcbiAgICBucC5hcnJheShbWzEsMC42LDAuMywwLjFdLFswLjYsMSwwLjQsMC4yXSxbMC4zLDAuNCwxLDAuNV0sWzAuMSwwLjIsMC41LDFdXSksIDUwMClcblhfYW5vbWFseSA9IG5wLnJhbmRvbS51bmlmb3JtKC00LCA0LCAoMjAsIGQpKVxuXG5tdSA9IFgubWVhbihheGlzPTApXG5TaWdtYV9pbnYgPSBucC5saW5hbGcuaW52KG5wLmNvdihYLlQpKVxuXG5kZWYgbWFoYWxfc3FfYmF0Y2gocG9pbnRzLCBtdSwgU2lnbWFfaW52KTpcbiAgICBkaWZmID0gcG9pbnRzIC0gbXVcbiAgICByZXR1cm4gbnAuZWluc3VtKFx1MDAyN2lqLGprLGlrLVx1MDAzZWlcdTAwMjcsIGRpZmYsIFNpZ21hX2ludiwgZGlmZilcblxuZm9yIGFscGhhIGluIFswLjA1LCAwLjAxLCAwLjAwMV06XG4gICAgdGhyZXNoID0gY2hpMi5wcGYoMSAtIGFscGhhLCBkZj1kKVxuICAgIGQyX25vcm1hbCAgPSBtYWhhbF9zcV9iYXRjaChYLCBtdSwgU2lnbWFfaW52KVxuICAgIGQyX2Fub21hbHkgPSBtYWhhbF9zcV9iYXRjaChYX2Fub21hbHksIG11LCBTaWdtYV9pbnYpXG4gICAgZnAgPSAoZDJfbm9ybWFsICBcdTAwM2UgdGhyZXNoKS5tZWFuKClcbiAgICB0cCA9IChkMl9hbm9tYWx5IFx1MDAzZSB0aHJlc2gpLm1lYW4oKVxuICAgIHByaW50KGZcdTAwMjdhbHBoYT17YWxwaGE6LjNmfTogdGhyZXNob2xkPXt0aHJlc2g6LjJmfSAgRlAgcmF0ZT17ZnA6LjNmfSAgYW5vbWFseSByZWNhbGw9e3RwOi4yZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUm9idXN0IEVzdGltYXRpb24gdmlhIE1DRCBhbmQgRWxsaXB0aWNFbnZlbG9wZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2FtcGxlIG1lYW4gYW5kIGNvdmFyaWFuY2UgYXJlIG5vbi1yb2J1c3Q6IGEgY29udGFtaW5hdGVkIGRhdGFzZXQgc2hpZnRzIGJvdGggZXN0aW1hdGVzIHRvd2FyZCB0aGUgb3V0bGllcnMsIG1hc2tpbmcgdGhlIGFub21hbGllcyAobWFza2luZykgb3IgZmxhZ2dpbmcgZ2VudWluZSBub3JtYWwgcG9pbnRzIChzd2FtcGluZykuIFRoZSBNaW5pbXVtIENvdmFyaWFuY2UgRGV0ZXJtaW5hbnQgKE1DRCkgZXN0aW1hdG9yIGZpbmRzIHRoZSBzdWJzZXQgb2YgaCDiiaUgKG4rZCsxKS8yIG9ic2VydmF0aW9ucyB3aXRoIHRoZSBzbWFsbGVzdCBjb3ZhcmlhbmNlIGRldGVybWluYW50IOKAlCB0eXBpY2FsbHkgaD03NSUgb2Ygbi4gVGhlIHJlc3VsdGluZyByb2J1c3QgbG9jYXRpb24gYW5kIHNjYXR0ZXIgYXJlIHVuYWZmZWN0ZWQgYnkgdXAgdG8gfjI1JSBjb250YW1pbmF0aW9uLiBza2xlYXJuIHdyYXBzIE1DRCBpbiBFbGxpcHRpY0VudmVsb3BlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jb3ZhcmlhbmNlIGltcG9ydCBFbGxpcHRpY0VudmVsb3BlLCBNaW5Db3ZEZXRcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YX2NsZWFuID0gbnAucmFuZG9tLm11bHRpdmFyaWF0ZV9ub3JtYWwoWzAsIDBdLCBbWzEsIDAuNl0sIFswLjYsIDFdXSwgMjAwKVxuWF9jb250YW1pbmF0ZWQgPSBucC52c3RhY2soW1hfY2xlYW4sXG4gICAgbnAucmFuZG9tLm11bHRpdmFyaWF0ZV9ub3JtYWwoWzUsIDVdLCBbWzAuMywgMF0sIFswLCAwLjNdXSwgMjApXSlcblxuIyBTdGFuZGFyZCAobm9uLXJvYnVzdCkgZXN0aW1hdGVzXG5tdV9zdGQgPSBYX2NvbnRhbWluYXRlZC5tZWFuKGF4aXM9MClcblxuIyBSb2J1c3QgZXN0aW1hdGVzIHZpYSBNQ0Rcbm1jZCA9IE1pbkNvdkRldChzdXBwb3J0X2ZyYWN0aW9uPTAuNzUsIHJhbmRvbV9zdGF0ZT00Milcbm1jZC5maXQoWF9jb250YW1pbmF0ZWQpXG5tdV9yb2IgPSBtY2QubG9jYXRpb25fXG5cbiMgRWxsaXB0aWNFbnZlbG9wZSBmb3IgYW5vbWFseSBkZXRlY3Rpb25cbmVudiA9IEVsbGlwdGljRW52ZWxvcGUoY29udGFtaW5hdGlvbj0wLjA5LCBzdXBwb3J0X2ZyYWN0aW9uPTAuNzUsIHJhbmRvbV9zdGF0ZT00MilcbmVudi5maXQoWF9jb250YW1pbmF0ZWQpXG5wcmVkcyA9IGVudi5wcmVkaWN0KFhfY29udGFtaW5hdGVkKVxubl9kZXRlY3RlZCA9IChwcmVkcyA9PSAtMSkuc3VtKClcblxucHJpbnQoZlx1MDAyN1N0YW5kYXJkIG11OiAge211X3N0ZC5yb3VuZCgzKX0gKGJpYXNlZCB0b3dhcmQgaW5qZWN0ZWQgY2x1c3RlcilcdTAwMjcpXG5wcmludChmXHUwMDI3Um9idXN0IG11OiAgICB7bXVfcm9iLnJvdW5kKDMpfSAoY2xvc2UgdG8gdHJ1ZSBbMCwwXSlcdTAwMjcpXG5wcmludChmXHUwMDI3RWxsaXB0aWNFbnZlbG9wZToge25fZGV0ZWN0ZWR9IGFub21hbGllcyAoaW5qZWN0ZWQgMjApXHUwMDI3KVxucHJpbnQoZlx1MDAyN1RydWUgcG9zaXRpdmUgcmF0ZTogeygocHJlZHNbLTIwOl0pID09IC0xKS5tZWFuKCk6LjAlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYWhhbGFub2JpcyB2cyBFdWNsaWRlYW4gb24gQ29ycmVsYXRlZCBGZWF0dXJlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBpbnNpZ2h0OiBhIHBvaW50IHRoYXQgZm9sbG93cyB0aGUgY29ycmVsYXRpb24gc3RydWN0dXJlIG9mIHRoZSBkYXRhIChlLmcuLCB0YWxsIGhlaWdodCArIGhpZ2ggd2VpZ2h0KSBtYXkgaGF2ZSBsYXJnZSBFdWNsaWRlYW4gZGlzdGFuY2UgZnJvbSB0aGUgbWVhbiBidXQgc21hbGwgTWFoYWxhbm9iaXMgZGlzdGFuY2UuIENvbnZlcnNlbHksIGEgcG9pbnQgdGhhdCBicmVha3MgdGhlIGNvcnJlbGF0aW9uIChlLmcuLCB2ZXJ5IHRhbGwgKyB2ZXJ5IGxvdyB3ZWlnaHQpIGhhcyBzbWFsbCBFdWNsaWRlYW4gZGlzdGFuY2UgYnV0IGxhcmdlIE1haGFsYW5vYmlzIGRpc3RhbmNlIGFuZCBpcyB0aGUgdHJ1ZSBhbm9tYWx5LiBFdWNsaWRlYW4gZGlzdGFuY2UgY2Fubm90IGRpc3Rpbmd1aXNoIHRoZXNlIGNhc2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IGNoaTJcblxubnAucmFuZG9tLnNlZWQoNDIpXG5jb3YgPSBbWzEuMCwgMC45NV0sIFswLjk1LCAxLjBdXVxuWCA9IG5wLnJhbmRvbS5tdWx0aXZhcmlhdGVfbm9ybWFsKFswLCAwXSwgY292LCAzMDApXG5cbm11ID0gWC5tZWFuKGF4aXM9MClcblNpZ21hID0gbnAuY292KFguVClcblNpZ21hX2ludiA9IG5wLmxpbmFsZy5pbnYoU2lnbWEpXG5cbmRlZiBldWNsaWRfZGlzdChwLCBtdSk6XG4gICAgcmV0dXJuIG5wLnNxcnQobnAuc3VtKChwIC0gbXUpKioyLCBheGlzPTEpKVxuXG5kZWYgbWFoYWxfZGlzdChwLCBtdSwgU2lnbWFfaW52KTpcbiAgICBkID0gcCAtIG11XG4gICAgcmV0dXJuIG5wLnNxcnQobnAuZWluc3VtKFx1MDAyN2lqLGprLGlrLVx1MDAzZWlcdTAwMjcsIGQsIFNpZ21hX2ludiwgZCkpXG5cbiMgUG9pbnQgQSBmb2xsb3dzIGNvcnJlbGF0aW9uOiBbMywgM10g4oCUIGFsb25nIHRoZSBtYWluIGF4aXNcbiMgUG9pbnQgQiBicmVha3MgY29ycmVsYXRpb246IFsxLCAtMV0g4oCUIGFnYWluc3QgdGhlIGNvcnJlbGF0aW9uXG5wdHMgPSBucC5hcnJheShbWzMuMCwgMy4wXSwgWzEuMCwgLTEuMF1dKVxubGFiZWxzID0gW1x1MDAyN0E6IHdpdGggY29ycmVsYXRpb24gKDMsMylcdTAwMjcsIFx1MDAyN0I6IGFnYWluc3QgY29ycmVsYXRpb24gKDEsLTEpXHUwMDI3XVxudGhyZXNob2xkX21haGFsID0gbnAuc3FydChjaGkyLnBwZigwLjk5LCBkZj0yKSlcblxuZm9yIGxhYmVsLCBwdCBpbiB6aXAobGFiZWxzLCBwdHMpOlxuICAgIHAgPSBwdC5yZXNoYXBlKDEsIC0xKVxuICAgIGVkID0gZXVjbGlkX2Rpc3QocCwgbXUpWzBdXG4gICAgbWQgPSBtYWhhbF9kaXN0KHAsIG11LCBTaWdtYV9pbnYpWzBdXG4gICAgcHJpbnQoZlx1MDAyN3tsYWJlbH1cdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyNyAgRXVjbGlkZWFuPXtlZDouM2Z9ICBNYWhhbGFub2Jpcz17bWQ6LjNmfSAgdGhyZXNob2xkPXt0aHJlc2hvbGRfbWFoYWw6LjNmfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBBbm9tYWx5IGJ5IEV1Y2xpZGVhbiAoXHUwMDNlMyk6IHtlZFx1MDAzZTN9ICAgYnkgTWFoYWxhbm9iaXM6IHttZFx1MDAzZXRocmVzaG9sZF9tYWhhbH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWV0aG9kIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJFdWNsaWRlYW4iLCJQZXItZmVhdHVyZSBaLXNjb3JlIiwiTWFoYWxhbm9iaXMiLCJSb2J1c3QgTWFoYWxhbm9iaXMgKE1DRCkiXSwicm93cyI6W1siSGFuZGxlcyBmZWF0dXJlIGNvcnJlbGF0aW9uIiwiTm8iLCJObyIsIlllcyAodmlhIM6j4oG7wrkpIiwiWWVzIl0sWyJTY2FsZSBpbnZhcmlhbnQiLCJObyIsIlllcyAocGVyIGZlYXR1cmUpIiwiWWVzIiwiWWVzIl0sWyJNdWx0aXZhcmlhdGUgdGhyZXNob2xkIiwiTm8gKHBlci1heGlzKSIsIk5vIiwiWWVzICjPh8KyKGQpKSIsIlllcyJdLFsiUm9idXN0bmVzcyB0byBjb250YW1pbmF0aW9uIiwiTG93IiwiTG93IiwiTG93IiwiSGlnaCAoNTAlIGJyZWFrZG93bikiXSxbIlJlcXVpcmVzIGQgXHUwMDNjIG4vMiIsIk5vIiwiTm8iLCJZZXMgKM6jIGludmVydGlibGUpIiwiTGVzcyBzdHJpY3QiXSxbIkNvbXB1dGF0aW9uYWwgY29zdCIsIk8obmQpIiwiTyhuZCkiLCJPKG5kwrIgKyBkwrMpIiwiTyhuwrJkwrIpIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW1pdGF0aW9ucyBhbmQgUHJhY3RpY2FsIE5vdGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNYWhhbGFub2JpcyBkaXN0YW5jZSBhc3N1bWVzIHRoZSBkYXRhIGZvbGxvd3MgYSBtdWx0aXZhcmlhdGUgR2F1c3NpYW4uIFdoZW4gdGhlIHRydWUgZGlzdHJpYnV0aW9uIGhhcyBoZWF2eSB0YWlscyBvciBtdWx0aXBsZSBjbHVzdGVycywgdGhlIHNpbmdsZSBHYXVzc2lhbiBhc3N1bXB0aW9uIGJyZWFrcyBkb3duIGFuZCBhbm9tYWx5IGRldGVjdGlvbiBzdWZmZXJzLiBXaGVuIGQgXHUwMDNlIG4vMiwgdGhlIHNhbXBsZSBjb3ZhcmlhbmNlIGlzIHNpbmd1bGFyIOKAlCB1c2UgcHNldWRvLWludmVyc2UsIGRpYWdvbmFsIHJlZ3VsYXJpc2F0aW9uICjOoyArIM61SSksIG9yIHJlZHVjZSBkaW1lbnNpb25zIGZpcnN0IHdpdGggUENBLiBGb3IgdmVyeSBoaWdoLWRpbWVuc2lvbmFsIGRhdGEgKGQgXHUwMDNlIDEwMCksIGNvbnNpZGVyIElzb2xhdGlvbiBGb3Jlc3QgaW5zdGVhZC4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6Ik1haGFsYW5vYmlzIGZvciBBbm9tYWx5IFNjb3JpbmciLCJjb250ZW50IjoiUmF0aGVyIHRoYW4gdXNpbmcgYSBoYXJkIGNoaS1zcXVhcmVkIHRocmVzaG9sZCwgeW91IGNhbiB1c2UgZMKyX00gZGlyZWN0bHkgYXMgYSBjb250aW51b3VzIGFub21hbHkgc2NvcmUg4oCUIGxhcmdlciB2YWx1ZXMgaW5kaWNhdGUgbW9yZSBhbm9tYWxvdXMgcG9pbnRzLiBUaGlzIGF2b2lkcyBjb21taXR0aW5nIHRvIGFuIM6xIGxldmVsIGFuZCBhbGxvd3MgZG93bnN0cmVhbSByYW5raW5nIG9yIHRocmVzaG9sZCB0dW5pbmcgdXNpbmcgYSB2YWxpZGF0aW9uIHNldCB3aXRoIGxhYmVsbGVkIGFub21hbGllcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFsd2F5cyB1c2Ugcm9idXN0IE1DRCBlc3RpbWF0aW9uIChFbGxpcHRpY0VudmVsb3BlKSB3aGVuIGNvbnRhbWluYXRpb24gaXMgZXhwZWN0ZWQiLCJWZXJpZnkgYXBwcm94aW1hdGUgbXVsdGl2YXJpYXRlIG5vcm1hbGl0eSB3aXRoIE1hcmRpYVx1MDAyN3MgdGVzdCBvciBRLVEgcGxvdHMgb2YgZMKyX00iLCJXaGVuIGQgXHUwMDNlIG4vMiwgcmVndWxhcmlzZTogU2lnbWFfcmVnID0gU2lnbWEgKyBsYW0gKiBucC5leWUoZCkiLCJGb3Igbm9uLUdhdXNzaWFuIGRhdGEsIGNvbnNpZGVyIGtlcm5lbCBNYWhhbGFub2JpcyBvciBzd2l0Y2ggdG8gSXNvbGF0aW9uIEZvcmVzdCIsIlVzZSBjaGkyLnBwZigxLWFscGhhLCBkZj1kKSB0byBzZXQgdGhlIHRocmVzaG9sZCDigJQgaXQgc2NhbGVzIGNvcnJlY3RseSB3aXRoIGRpbWVuc2lvbiJdfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1haGFsYW5vYmlzIGRpc3RhbmNlIGlzIGFsc28gdXNlZCBpbiBub3ZlbHR5IGRldGVjdGlvbjogZml0IHRoZSBjb3ZhcmlhbmNlIG9uIHRyYWluaW5nIChub3JtYWwpIGRhdGEsIHRoZW4gc2NvcmUgdGVzdCBwb2ludHMuIEJlY2F1c2UgdGhlIHRocmVzaG9sZCBmcm9tIM+HwrIoZCkgaXMgdGhlb3JldGljYWxseSBtb3RpdmF0ZWQsIGl0IGRvZXMgbm90IG5lZWQgbWFudWFsIHR1bmluZyDigJQgYSBrZXkgYWR2YW50YWdlIG92ZXIgbWV0aG9kcyBsaWtlIExPRiBvciBJc29sYXRpb24gRm9yZXN0IHRoYXQgcmVxdWlyZSBjb250YW1pbmF0aW9uIHBhcmFtZXRlciBlc3RpbWF0aW9uLiJ9XQ=="
---
# Mahalanobis Distance — Multivariate Anomaly Detection

Euclidean distance treats every feature dimension as equally important and independent. When features are correlated or have different scales, Euclidean distance misidentifies which points are truly unusual. Mahalanobis distance corrects for both correlation (via the covariance matrix Σ) and scale (via Σ's diagonal), producing a single unitless distance that accounts for the joint distribution of all features simultaneously.

## Mahalanobis Distance — Definition and Geometry

For a point x in d-dimensional space with population mean μ and covariance Σ, the Mahalanobis distance is d_M(x) = √((x−μ)ᵀΣ⁻¹(x−μ)). The term Σ⁻¹ whitens the data: it rotates axes to align with principal components and scales each axis by 1/√λᵢ where λᵢ is the i-th eigenvalue. Under a multivariate Gaussian, d²_M follows a chi-squared distribution with d degrees of freedom — giving a principled statistical threshold for any dimension.

$$d_M(\mathbf{x}) = \sqrt{(\mathbf{x}-\boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x}-\boldsymbol{\mu})}, \quad d_M^2 \sim \chi^2(d) \text{ under Gaussian}$$

## From Scratch vs scipy

The squared Mahalanobis distance can be computed as a quadratic form using the inverse covariance matrix. scipy.spatial.distance.mahalanobis accepts the inverse covariance matrix (VI parameter) directly. For batches of points, use numpy einsum for vectorised computation. When the covariance matrix is near-singular (d close to n), use the pseudoinverse or regularise with a small diagonal: Σ_reg = Σ + εI.

```python
import numpy as np
from scipy.spatial.distance import mahalanobis
from scipy.stats import chi2

np.random.seed(42)
X = np.random.multivariate_normal([0, 0], [[1, 0.8], [0.8, 1]], 200)
X_test = np.array([[3.0, 3.0], [0.5, -0.5], [-2.0, 2.0]])

mu = X.mean(axis=0)
Sigma = np.cov(X.T)
Sigma_inv = np.linalg.inv(Sigma)

def mahal_scratch(x, mu, Sigma_inv):
    diff = x - mu
    return np.sqrt(diff @ Sigma_inv @ diff)

d_scratch = np.array([mahal_scratch(x, mu, Sigma_inv) for x in X_test])
d_scipy   = np.array([mahalanobis(x, mu, Sigma_inv) for x in X_test])
d_sq      = np.array([(x-mu) @ Sigma_inv @ (x-mu) for x in X_test])

print('Point           | d_scratch | d_scipy | d^2    | p-val (chi2)')
for i, x in enumerate(X_test):
    pval = 1 - chi2.cdf(d_sq[i], df=2)
    print(f'{str(x):16s} | {d_scratch[i]:9.4f} | {d_scipy[i]:7.4f} | {d_sq[i]:6.3f} | {pval:.4f}')
print(f'Max diff scratch vs scipy: {np.abs(d_scratch - d_scipy).max():.2e}')
```

## Chi-Squared Threshold for Anomaly Flagging

Under a multivariate Gaussian, d²_M ~ χ²(d). An anomaly threshold at significance α is the (1−α) quantile of χ²(d). For d=2, α=0.01 gives threshold ≈ 9.21 (d_M ≈ 3.03). This threshold works regardless of feature scale and automatically tightens as dimension d increases — one of Mahalanobis distance's key advantages over ad-hoc per-feature Z-scores.

```python
import numpy as np
from scipy.stats import chi2

np.random.seed(42)
d = 4  # dimensions
X = np.random.multivariate_normal(np.zeros(d),
    np.array([[1,0.6,0.3,0.1],[0.6,1,0.4,0.2],[0.3,0.4,1,0.5],[0.1,0.2,0.5,1]]), 500)
X_anomaly = np.random.uniform(-4, 4, (20, d))

mu = X.mean(axis=0)
Sigma_inv = np.linalg.inv(np.cov(X.T))

def mahal_sq_batch(points, mu, Sigma_inv):
    diff = points - mu
    return np.einsum('ij,jk,ik->i', diff, Sigma_inv, diff)

for alpha in [0.05, 0.01, 0.001]:
    thresh = chi2.ppf(1 - alpha, df=d)
    d2_normal  = mahal_sq_batch(X, mu, Sigma_inv)
    d2_anomaly = mahal_sq_batch(X_anomaly, mu, Sigma_inv)
    fp = (d2_normal  > thresh).mean()
    tp = (d2_anomaly > thresh).mean()
    print(f'alpha={alpha:.3f}: threshold={thresh:.2f}  FP rate={fp:.3f}  anomaly recall={tp:.2f}')
```

## Robust Estimation via MCD and EllipticEnvelope

Sample mean and covariance are non-robust: a contaminated dataset shifts both estimates toward the outliers, masking the anomalies (masking) or flagging genuine normal points (swamping). The Minimum Covariance Determinant (MCD) estimator finds the subset of h ≥ (n+d+1)/2 observations with the smallest covariance determinant — typically h=75% of n. The resulting robust location and scatter are unaffected by up to ~25% contamination. sklearn wraps MCD in EllipticEnvelope.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope, MinCovDet

np.random.seed(42)
X_clean = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], 200)
X_contaminated = np.vstack([X_clean,
    np.random.multivariate_normal([5, 5], [[0.3, 0], [0, 0.3]], 20)])

# Standard (non-robust) estimates
mu_std = X_contaminated.mean(axis=0)

# Robust estimates via MCD
mcd = MinCovDet(support_fraction=0.75, random_state=42)
mcd.fit(X_contaminated)
mu_rob = mcd.location_

# EllipticEnvelope for anomaly detection
env = EllipticEnvelope(contamination=0.09, support_fraction=0.75, random_state=42)
env.fit(X_contaminated)
preds = env.predict(X_contaminated)
n_detected = (preds == -1).sum()

print(f'Standard mu:  {mu_std.round(3)} (biased toward injected cluster)')
print(f'Robust mu:    {mu_rob.round(3)} (close to true [0,0])')
print(f'EllipticEnvelope: {n_detected} anomalies (injected 20)')
print(f'True positive rate: {((preds[-20:]) == -1).mean():.0%}')
```

## Mahalanobis vs Euclidean on Correlated Features

The key insight: a point that follows the correlation structure of the data (e.g., tall height + high weight) may have large Euclidean distance from the mean but small Mahalanobis distance. Conversely, a point that breaks the correlation (e.g., very tall + very low weight) has small Euclidean distance but large Mahalanobis distance and is the true anomaly. Euclidean distance cannot distinguish these cases.

```python
import numpy as np
from scipy.stats import chi2

np.random.seed(42)
cov = [[1.0, 0.95], [0.95, 1.0]]
X = np.random.multivariate_normal([0, 0], cov, 300)

mu = X.mean(axis=0)
Sigma = np.cov(X.T)
Sigma_inv = np.linalg.inv(Sigma)

def euclid_dist(p, mu):
    return np.sqrt(np.sum((p - mu)**2, axis=1))

def mahal_dist(p, mu, Sigma_inv):
    d = p - mu
    return np.sqrt(np.einsum('ij,jk,ik->i', d, Sigma_inv, d))

# Point A follows correlation: [3, 3] — along the main axis
# Point B breaks correlation: [1, -1] — against the correlation
pts = np.array([[3.0, 3.0], [1.0, -1.0]])
labels = ['A: with correlation (3,3)', 'B: against correlation (1,-1)']
threshold_mahal = np.sqrt(chi2.ppf(0.99, df=2))

for label, pt in zip(labels, pts):
    p = pt.reshape(1, -1)
    ed = euclid_dist(p, mu)[0]
    md = mahal_dist(p, mu, Sigma_inv)[0]
    print(f'{label}')
    print(f'  Euclidean={ed:.3f}  Mahalanobis={md:.3f}  threshold={threshold_mahal:.3f}')
    print(f'  Anomaly by Euclidean (>3): {ed>3}   by Mahalanobis: {md>threshold_mahal}')
```

## Method Comparison

| Property | Euclidean | Per-feature Z-score | Mahalanobis | Robust Mahalanobis (MCD) |
| --- | --- | --- | --- | --- |
| Handles feature correlation | No | No | Yes (via Σ⁻¹) | Yes |
| Scale invariant | No | Yes (per feature) | Yes | Yes |
| Multivariate threshold | No (per-axis) | No | Yes (χ²(d)) | Yes |
| Robustness to contamination | Low | Low | Low | High (50% breakdown) |
| Requires d < n/2 | No | No | Yes (Σ invertible) | Less strict |
| Computational cost | O(nd) | O(nd) | O(nd² + d³) | O(n²d²) |

## Limitations and Practical Notes

Mahalanobis distance assumes the data follows a multivariate Gaussian. When the true distribution has heavy tails or multiple clusters, the single Gaussian assumption breaks down and anomaly detection suffers. When d > n/2, the sample covariance is singular — use pseudo-inverse, diagonal regularisation (Σ + εI), or reduce dimensions first with PCA. For very high-dimensional data (d > 100), consider Isolation Forest instead.

> **Mahalanobis for Anomaly Scoring**: Rather than using a hard chi-squared threshold, you can use d²_M directly as a continuous anomaly score — larger values indicate more anomalous points. This avoids committing to an α level and allows downstream ranking or threshold tuning using a validation set with labelled anomalies.

- Always use robust MCD estimation (EllipticEnvelope) when contamination is expected
- Verify approximate multivariate normality with Mardia's test or Q-Q plots of d²_M
- When d > n/2, regularise: Sigma_reg = Sigma + lam * np.eye(d)
- For non-Gaussian data, consider kernel Mahalanobis or switch to Isolation Forest
- Use chi2.ppf(1-alpha, df=d) to set the threshold — it scales correctly with dimension

Mahalanobis distance is also used in novelty detection: fit the covariance on training (normal) data, then score test points. Because the threshold from χ²(d) is theoretically motivated, it does not need manual tuning — a key advantage over methods like LOF or Isolation Forest that require contamination parameter estimation.

