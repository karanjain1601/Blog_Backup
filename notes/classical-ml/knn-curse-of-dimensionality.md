---
title: "k-Nearest Neighbors and the Curse of Dimensionality"
slug: "knn-curse-of-dimensionality"
description: "Understand kNN from first principles, demonstrate distance concentration in high dimensions, and explore approximate nearest neighbor methods (HNSW, Faiss) that make kNN practical at scale."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50Ijoiay1OZWFyZXN0IE5laWdoYm9ycyBpcyBhbW9uZyB0aGUgc2ltcGxlc3Qgbm9uLXBhcmFtZXRyaWMgbGVhcm5pbmcgYWxnb3JpdGhtczogZm9yIGEgcXVlcnkgcG9pbnQgeCwgZmluZCB0aGUgayB0cmFpbmluZyBwb2ludHMgY2xvc2VzdCBpbiBmZWF0dXJlIHNwYWNlIGFuZCBwcmVkaWN0IGJ5IG1ham9yaXR5IHZvdGUgKGNsYXNzaWZpY2F0aW9uKSBvciBtZWFuIChyZWdyZXNzaW9uKS4gRGVzcGl0ZSBpdHMgc2ltcGxpY2l0eSwga05OIGhhcyBzdHJvbmcgdGhlb3JldGljYWwgZm91bmRhdGlvbnMg4oCUIGFzIG7ihpLiiJ4gd2l0aCBrL27ihpIwLCB0aGUga05OIGVycm9yIGNvbnZlcmdlcyB0byB0d2ljZSB0aGUgQmF5ZXMgZXJyb3IuIEhvd2V2ZXIsIGtOTiBkZWdyYWRlcyBzZXZlcmVseSBpbiBoaWdoIGRpbWVuc2lvbnMgZHVlIHRvIHRoZSBjdXJzZSBvZiBkaW1lbnNpb25hbGl0eSwgd2hlcmUgYWxsIHBhaXJ3aXNlIGRpc3RhbmNlcyBiZWNvbWUgYXBwcm94aW1hdGVseSBlcXVhbCwgbWFraW5nIFx1MDAyN25lYXJlc3RcdTAwMjcgbWVhbmluZ2xlc3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50Ijoia05OIGZyb20gRmlyc3QgUHJpbmNpcGxlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2l2ZW4gYSBxdWVyeSB4LCBjb21wdXRlIGQoeCwgeOG1oikgZm9yIGFsbCBuIHRyYWluaW5nIHBvaW50cywgc29ydCwgdGFrZSB0aGUgayBzbWFsbGVzdCwgYW5kIGFnZ3JlZ2F0ZSBsYWJlbHMuIFRoZSBjaG9pY2Ugb2YgayBjb250cm9scyB0aGUgYmlhcy12YXJpYW5jZSB0cmFkZW9mZjogaz0xIGdpdmVzIHplcm8gdHJhaW5pbmcgZXJyb3IgKGV4dHJlbWVseSBoaWdoIHZhcmlhbmNlKTsgbGFyZ2UgayBnaXZlcyBzbW9vdGgsIHN0YWJsZSBib3VuZGFyaWVzIChoaWdoZXIgYmlhcykuIFRoZSBvcHRpbWFsIGsgaXMgZm91bmQgdmlhIGNyb3NzLXZhbGlkYXRpb24uIFRoZSBhbGdvcml0aG0gaXMgbGF6eSAobm9uLXBhcmFtZXRyaWMpOiBhbGwgY29tcHV0YXRpb24gaGFwcGVucyBhdCBxdWVyeSB0aW1lLCB3aXRoIE8obmQpIGNvc3QgcGVyIHF1ZXJ5IGZvciBicnV0ZSBmb3JjZS4ga05OIGlzIG5vbi1wYXJhbWV0cmljIOKAlCBpdCBtYWtlcyBubyBhc3N1bXB0aW9uIGFib3V0IHRoZSBmdW5jdGlvbmFsIGZvcm0gb2YgdGhlIGRlY2lzaW9uIGJvdW5kYXJ5LCBvbmx5IHRoYXQgbmVhcmJ5IHBvaW50cyBzaGFyZSB0aGUgc2FtZSBsYWJlbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBhY2N1cmFjeV9zY29yZVxuXG5jbGFzcyBLTk5DbGFzc2lmaWVyOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBrPTUsIG1ldHJpYz1cdTAwMjdldWNsaWRlYW5cdTAwMjcpOlxuICAgICAgICBzZWxmLmsgPSBrXG4gICAgICAgIHNlbGYubWV0cmljID0gbWV0cmljXG5cbiAgICBkZWYgZml0KHNlbGYsIFgsIHkpOlxuICAgICAgICBzZWxmLlhfdHJhaW4gPSBYLmNvcHkoKVxuICAgICAgICBzZWxmLnlfdHJhaW4gPSB5LmNvcHkoKVxuICAgICAgICByZXR1cm4gc2VsZlxuXG4gICAgZGVmIF9kaXN0YW5jZXMoc2VsZiwgeCk6XG4gICAgICAgIGlmIHNlbGYubWV0cmljID09IFx1MDAyN2V1Y2xpZGVhblx1MDAyNzpcbiAgICAgICAgICAgIHJldHVybiBucC5zcXJ0KG5wLnN1bSgoc2VsZi5YX3RyYWluIC0geCkqKjIsIGF4aXM9MSkpXG4gICAgICAgIGVsaWYgc2VsZi5tZXRyaWMgPT0gXHUwMDI3bWFuaGF0dGFuXHUwMDI3OlxuICAgICAgICAgICAgcmV0dXJuIG5wLnN1bShucC5hYnMoc2VsZi5YX3RyYWluIC0geCksIGF4aXM9MSlcbiAgICAgICAgZWxpZiBzZWxmLm1ldHJpYyA9PSBcdTAwMjdjb3NpbmVcdTAwMjc6XG4gICAgICAgICAgICBub3JtID0gbnAubGluYWxnLm5vcm0oc2VsZi5YX3RyYWluLCBheGlzPTEpICogbnAubGluYWxnLm5vcm0oeCkgKyAxZS0xMFxuICAgICAgICAgICAgcmV0dXJuIDEgLSAoc2VsZi5YX3RyYWluIEAgeCkgLyBub3JtXG5cbiAgICBkZWYgcHJlZGljdChzZWxmLCBYKTpcbiAgICAgICAgcHJlZHMgPSBbXVxuICAgICAgICBmb3IgeCBpbiBYOlxuICAgICAgICAgICAgZGlzdHMgPSBzZWxmLl9kaXN0YW5jZXMoeClcbiAgICAgICAgICAgIG5uX2lkeCA9IG5wLmFyZ3NvcnQoZGlzdHMpWzpzZWxmLmtdXG4gICAgICAgICAgICB2b3RlcyA9IHNlbGYueV90cmFpbltubl9pZHhdXG4gICAgICAgICAgICBwcmVkcy5hcHBlbmQobnAuYmluY291bnQodm90ZXMpLmFyZ21heCgpKVxuICAgICAgICByZXR1cm4gbnAuYXJyYXkocHJlZHMpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24obl9zYW1wbGVzPTUwMCwgbl9mZWF0dXJlcz02LCBuX2luZm9ybWF0aXZlPTQsIHJhbmRvbV9zdGF0ZT00MilcblhfdHIsIFhfdGUsIHlfdHIsIHlfdGUgPSB0cmFpbl90ZXN0X3NwbGl0KFgsIHksIHRlc3Rfc2l6ZT0wLjI1LCByYW5kb21fc3RhdGU9NDIpXG5cbmZvciBrIGluIFsxLCAzLCA1LCAxMSwgMjFdOlxuICAgIGtubiA9IEtOTkNsYXNzaWZpZXIoaz1rKS5maXQoWF90ciwgeV90cilcbiAgICBhY2MgPSBhY2N1cmFjeV9zY29yZSh5X3RlLCBrbm4ucHJlZGljdChYX3RlKSlcbiAgICBwcmludChmXHUwMDI3az17azpcdTAwM2UyfTogYWNjdXJhY3k9e2FjYzouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpc3RhbmNlIE1ldHJpY3MgYW5kIENob29zaW5nIHRoZSBSaWdodCBPbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjaG9pY2Ugb2YgZGlzdGFuY2UgbWV0cmljIGlzIGNyaXRpY2FsIGZvciBrTk4uIEV1Y2xpZGVhbiAoTDIpOiBzcXJ0KM6jKHjhtaIteeG1oinCsikg4oCUIHNlbnNpdGl2ZSB0byBzY2FsZSwgZG9taW5hdGVkIGJ5IGhpZ2gtbWFnbml0dWRlIGZlYXR1cmVzLCByZXF1aXJlcyBzdGFuZGFyZGlzYXRpb24uIE1hbmhhdHRhbiAoTDEpOiDOo3x44bWiLXnhtaJ8IOKAlCBtb3JlIHJvYnVzdCB0byBvdXRsaWVycywgcHJlZmVycmVkIGZvciBzcGFyc2UgaGlnaC1kaW1lbnNpb25hbCBkYXRhLiBDb3NpbmU6IDEgLSAoeMK3eSkvKOKAlnjigJbigJZ54oCWKSDigJQgbWVhc3VyZXMgYW5nbGUsIGlnbm9yZXMgbWFnbml0dWRlLCBpZGVhbCBmb3IgdGV4dCBlbWJlZGRpbmdzIGFuZCBkb2N1bWVudHMuIE1haGFsYW5vYmlzOiBzcXJ0KCh4LXkp4bWAzqPigbvCuSh4LXkpKSDigJQgYWNjb3VudHMgZm9yIGZlYXR1cmUgY29ycmVsYXRpb25zIGFuZCBzY2FsZXMsIGVxdWl2YWxlbnQgdG8gRXVjbGlkZWFuIGFmdGVyIHdoaXRlbmluZy4gSGFtbWluZyBkaXN0YW5jZSBmb3IgYmluYXJ5IGZlYXR1cmVzLiBBbHdheXMgc3RhbmRhcmRpc2UgZmVhdHVyZXMgYmVmb3JlIEV1Y2xpZGVhbiBrTk4g4oCUIGEgZmVhdHVyZSB3aXRoIHJhbmdlIFswLCAxMDAwXSBkb21pbmF0ZXMgb25lIHdpdGggcmFuZ2UgWzAsIDFdLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBDdXJzZSBvZiBEaW1lbnNpb25hbGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gZCBkaW1lbnNpb25zLCB0aGUgY29uY2VudHJhdGlvbiBvZiBtZWFzdXJlIHBoZW5vbWVub24gc3RhdGVzIHRoYXQgYWxsIHBhaXJ3aXNlIGRpc3RhbmNlcyBjb252ZXJnZSB0byB0aGUgc2FtZSB2YWx1ZSBhcyBk4oaS4oieOiAobWF4X2Rpc3QgLSBtaW5fZGlzdCkgLyBtaW5fZGlzdCDihpIgMC4gVGhlIHZvbHVtZSBvZiBhIHVuaXQgYmFsbCBzaHJpbmtzIHJlbGF0aXZlIHRvIHRoZSB1bml0IGh5cGVyY3ViZSBhcyAoz4Bee2QvMn0vzpMoZC8yKzEpKSAvIDJeZCDihpIgMCBhcyBk4oaS4oieLiBUbyBjYXB0dXJlIGEgZml4ZWQgZnJhY3Rpb24gcCBvZiB0aGUgdHJhaW5pbmcgZGF0YSBpbiBhIG5lYXJlc3QtbmVpZ2hib3IgYmFsbCwgdGhlIGJhbGwgcmFkaXVzIG11c3QgZ3JvdyB0byByID0gcF57MS9kfS4gRm9yIHA9MC4wMSAoMSUgb2YgZGF0YSkgYW5kIGQ9MTAwLCByIOKJiCAwLjk1NSDigJQgYWxtb3N0IHRoZSBmdWxsIHJhbmdlIG9mIHRoZSB1bml0IGh5cGVyY3ViZS4gV2hlbiBhbGwgZGlzdGFuY2VzIGFyZSBhcHByb3hpbWF0ZWx5IGVxdWFsLCB0aGUgY29uY2VwdCBvZiBcdTAwMjduZWFyZXN0XHUwMDI3IGxvc2VzIG1lYW5pbmcgYW5kIGtOTiBkZWdyYWRlcyB0byByYW5kb20gZ3Vlc3NpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5ucC5yYW5kb20uc2VlZCg0Milcbm5fcmVmLCBuX3F1ZXJ5ID0gMTAwMCwgMTAwXG5cbnByaW50KGZcdTAwMjd7XHUwMDI3RGltXHUwMDI3Olx1MDAzZTV9IHtcdTAwMjdNZWFuIERpc3RcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdTdGQgRGlzdFx1MDAyNzpcdTAwM2UxMn0ge1x1MDAyN0NvVlx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN1JlbCBSYW5nZVx1MDAyNzpcdTAwM2UxMn1cdTAwMjcpXG5mb3IgZCBpbiBbMiwgNSwgMTAsIDIwLCA1MCwgMTAwLCAyMDAsIDUwMF06XG4gICAgWF9yZWYgPSBucC5yYW5kb20udW5pZm9ybSgwLCAxLCAobl9yZWYsIGQpKVxuICAgIFhfcSAgID0gbnAucmFuZG9tLnVuaWZvcm0oMCwgMSwgKG5fcXVlcnksIGQpKVxuICAgICMgRXVjbGlkZWFuIGRpc3RhbmNlcyBmcm9tIGFsbCBxdWVyeSBwb2ludHMgdG8gYWxsIHJlZmVyZW5jZSBwb2ludHNcbiAgICBkaXN0cyA9IG5wLnNxcnQobnAuc3VtKChYX3JlZltOb25lLDosOl0gLSBYX3FbOixOb25lLDpdKSoqMiwgYXhpcz0yKSkucmF2ZWwoKVxuICAgIG1lYW5fZCA9IGRpc3RzLm1lYW4oKVxuICAgIHN0ZF9kICA9IGRpc3RzLnN0ZCgpXG4gICAgY292ICAgID0gc3RkX2QgLyAobWVhbl9kICsgMWUtMTIpICAgICAgICAgICMgY29lZmZpY2llbnQgb2YgdmFyaWF0aW9uXG4gICAgcmVsX3JhbmdlID0gKGRpc3RzLm1heCgpIC0gZGlzdHMubWluKCkpIC8gKGRpc3RzLm1pbigpICsgMWUtMTIpXG4gICAgcHJpbnQoZlx1MDAyN3tkOlx1MDAzZTV9IHttZWFuX2Q6XHUwMDNlMTIuNGZ9IHtzdGRfZDpcdTAwM2UxMi40Zn0ge2NvdjpcdTAwM2UxMC40Zn0ge3JlbF9yYW5nZTpcdTAwM2UxMi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJrTk4gRmFpbHMgU2lsZW50bHkgaW4gSGlnaCBEaW1lbnNpb25zIiwiY29udGVudCI6IkluIGhpZ2ggZGltZW5zaW9ucywga05OIHN0aWxsIHJldHVybnMgcHJlZGljdGlvbnMg4oCUIGl0IGp1c3QgcmV0dXJucyBtZWFuaW5nbGVzcyBvbmVzLiBUaGUgayBuZWFyZXN0IG5laWdoYm9ycyBvZiBhIHF1ZXJ5IHBvaW50IGFyZSBubyBtb3JlIHNpbWlsYXIgdG8gaXQgdGhhbiByYW5kb20gcG9pbnRzIGZyb20gdGhlIGRhdGFzZXQuIFRoZSBtb2RlbCBhcHBlYXJzIHRvIHdvcmsgb24gdGhlIHRyYWluaW5nIHNldCBidXQgZ2VuZXJhbGlzZXMgcG9vcmx5LiBBbHdheXMgY2hlY2sgcGVyZm9ybWFuY2UgdnMgZGltZW5zaW9uYWxpdHkgYW5kIGFwcGx5IFBDQSwgVU1BUCwgb3IgZmVhdHVyZSBzZWxlY3Rpb24gYmVmb3JlIGFwcGx5aW5nIGtOTiB0byBkYXRhIHdpdGggZCBcdTAwM2UgMjAuIEEgc2hhcnAgZHJvcCBpbiByZWNhbGwgb2YgdGhlIGV4YWN0IG5lYXJlc3QgbmVpZ2hib3IgaXMgYSByZWxpYWJsZSBkaWFnbm9zdGljLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6ImtkLVRyZWVzIGFuZCBCYWxsIFRyZWVzIGZvciBFeGFjdCBOTiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGxvdy1kaW1lbnNpb25hbCBkYXRhIChkIOKJpCAyMCksIGV4YWN0IG5lYXJlc3QgbmVpZ2hib3Igc2VhcmNoIGNhbiBiZSBhY2NlbGVyYXRlZCBiZXlvbmQgYnJ1dGUgZm9yY2UuIGtkLXRyZWVzIHJlY3Vyc2l2ZWx5IHBhcnRpdGlvbiBzcGFjZSB3aXRoIGF4aXMtYWxpZ25lZCBzcGxpdHMsIGVuYWJsaW5nIE8obG9nIG4pIGF2ZXJhZ2UgcXVlcnkgdGltZSBmb3IgZCDiiaQgMjAg4oCUIGJ1dCBwZXJmb3JtYW5jZSBkZWdyYWRlcyBiYWNrIHRvIE8obikgZm9yIGQgXHUwMDNlIDIwIGJlY2F1c2UgdGhlIHRyZWUgaGFzIE8oMl5kKSBsZWFmIG5vZGVzLiBCYWxsIHRyZWVzIHBhcnRpdGlvbiBzcGFjZSB3aXRoIGh5cGVyc3BoZXJlcyBpbnN0ZWFkIG9mIGh5cGVycGxhbmVzLCB3aGljaCBoYW5kbGVzIG5vbi1heGlzLWFsaWduZWQgYm91bmRhcmllcyBiZXR0ZXIgYW5kIHdvcmtzIHdlbGwgdXAgdG8gZCDiiYggMzAuIEJvdGggYXJlIGltcGxlbWVudGVkIGluIHNrbGVhcm5cdTAwMjdzIE5lYXJlc3ROZWlnaGJvcnMgd2l0aCBhbGdvcml0aG09XHUwMDI3a2RfdHJlZVx1MDAyNyBvciBcdTAwMjdiYWxsX3RyZWVcdTAwMjcuIEZvciBkIFx1MDAzZSAyMC0zMCwgYXBwcm94aW1hdGUgbWV0aG9kcyAoSE5TVywgRmFpc3MpIGFyZSBuZWNlc3NhcnkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXBwcm94aW1hdGUgTmVhcmVzdCBOZWlnaGJvcnMg4oCUIEhOU1cgYW5kIEZhaXNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIaWVyYXJjaGljYWwgTmF2aWdhYmxlIFNtYWxsIFdvcmxkIChITlNXKSBncmFwaHMgYnVpbGQgYSBtdWx0aS1sYXllciBwcm94aW1pdHkgZ3JhcGggd2hlcmUgbGF5ZXIgMCBjb250YWlucyBhbGwgcG9pbnRzIGFuZCBoaWdoZXIgbGF5ZXJzIGNvbnRhaW4gcHJvZ3Jlc3NpdmVseSBmZXdlciBwb2ludHMuIFF1ZXJ5IHRpbWUgaXMgTyhsb2cgbikgd2l0aCBcdTAwM2U5OSUgcmVjYWxsIGF0IHR5cGljYWwgc2V0dGluZ3MuIEhOU1cgaXMgdGhlIGVuZ2luZSBiZWhpbmQgbWFueSBwcm9kdWN0aW9uIHZlY3RvciBzZWFyY2ggc3lzdGVtcy4gRmFpc3MgKEZhY2Vib29rIEFJIFNpbWlsYXJpdHkgU2VhcmNoKSBwcm92aWRlcyBHUFUtYWNjZWxlcmF0ZWQgQU5OIHdpdGggSVZGIChJbnZlcnRlZCBGaWxlIEluZGV4KSB3aGljaCBjbHVzdGVycyB0aGUgZGF0YSBhbmQgc2VhcmNoZXMgb25seSBuZWFyYnkgY2x1c3RlcnMgKG5wcm9iZSBjbHVzdGVycyksIGdpdmluZyBjb250cm9sbGFibGUgc3BlZWQtcmVjYWxsIHRyYWRlb2ZmcyBhdCBiaWxsaW9uLXNjYWxlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0aW1lXG5mcm9tIHNrbGVhcm4ubmVpZ2hib3JzIGltcG9ydCBOZWFyZXN0TmVpZ2hib3JzXG5cbnRyeTpcbiAgICBpbXBvcnQgaG5zd2xpYlxuICAgIGhhc19obnN3ID0gVHJ1ZVxuZXhjZXB0IEltcG9ydEVycm9yOlxuICAgIGhhc19obnN3ID0gRmFsc2VcbiAgICBwcmludChcdTAwMjdobnN3bGliIG5vdCBpbnN0YWxsZWRcdTAwMjcpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuZCwgbl9pbmRleCwgbl9xdWVyeSA9IDY0LCAxMDAwMCwgMjAwXG5YX2luZGV4ID0gbnAucmFuZG9tLnJhbmRuKG5faW5kZXgsIGQpLmFzdHlwZShucC5mbG9hdDMyKVxuWF9xdWVyeSA9IG5wLnJhbmRvbS5yYW5kbihuX3F1ZXJ5LCBkKS5hc3R5cGUobnAuZmxvYXQzMilcblxuIyBCcnV0ZSBmb3JjZSBleGFjdCBOTlxuYmYgPSBOZWFyZXN0TmVpZ2hib3JzKG5fbmVpZ2hib3JzPTEwLCBhbGdvcml0aG09XHUwMDI3YnJ1dGVcdTAwMjcsIG1ldHJpYz1cdTAwMjdldWNsaWRlYW5cdTAwMjcpXG5iZi5maXQoWF9pbmRleClcbnQwID0gdGltZS50aW1lKClcbmJmX2Rpc3QsIGJmX2lkeCA9IGJmLmtuZWlnaGJvcnMoWF9xdWVyeSlcbmJmX3RpbWUgPSB0aW1lLnRpbWUoKSAtIHQwXG5wcmludChmXHUwMDI3QnJ1dGUgZm9yY2U6IHtiZl90aW1lKjEwMDA6LjFmfSBtcyBmb3Ige25fcXVlcnl9IHF1ZXJpZXNcdTAwMjcpXG5cbmlmIGhhc19obnN3OlxuICAgIHAgPSBobnN3bGliLkluZGV4KHNwYWNlPVx1MDAyN2wyXHUwMDI3LCBkaW09ZClcbiAgICBwLmluaXRfaW5kZXgobWF4X2VsZW1lbnRzPW5faW5kZXgsIGVmX2NvbnN0cnVjdGlvbj0yMDAsIE09MTYpXG4gICAgcC5hZGRfaXRlbXMoWF9pbmRleClcbiAgICBwLnNldF9lZig1MCkgICMgZWYgY29udHJvbHMgcmVjYWxsIHZzIHNwZWVkXG4gICAgdDAgPSB0aW1lLnRpbWUoKVxuICAgIGhuc3dfaWR4LCBfID0gcC5rbm5fcXVlcnkoWF9xdWVyeSwgaz0xMClcbiAgICBobnN3X3RpbWUgPSB0aW1lLnRpbWUoKSAtIHQwXG4gICAgcmVjYWxsID0gbnAubWVhbihbbGVuKHNldChobnN3X2lkeFtpXSkgXHUwMDI2IHNldChiZl9pZHhbaV0pKSAvIDEwIGZvciBpIGluIHJhbmdlKG5fcXVlcnkpXSlcbiAgICBwcmludChmXHUwMDI3SE5TVzoge2huc3dfdGltZSoxMDAwOi4xZn0gbXMsICByZWNhbGxAMTA9e3JlY2FsbDouNGZ9LCAgc3BlZWR1cD17YmZfdGltZS9obnN3X3RpbWU6LjFmfXhcdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IHRpbWVcblxudHJ5OlxuICAgIGltcG9ydCBmYWlzc1xuICAgIGhhc19mYWlzcyA9IFRydWVcbmV4Y2VwdCBJbXBvcnRFcnJvcjpcbiAgICBoYXNfZmFpc3MgPSBGYWxzZVxuICAgIHByaW50KFx1MDAyN2ZhaXNzIG5vdCBpbnN0YWxsZWQ7IHNraXBwaW5nXHUwMDI3KVxuXG5pZiBoYXNfZmFpc3M6XG4gICAgbnAucmFuZG9tLnNlZWQoNDIpXG4gICAgZCwgbl90cmFpbiwgbl9xdWVyeSwgayA9IDEyOCwgNTAwMDAsIDEwMDAsIDEwXG4gICAgWF90cmFpbiA9IG5wLnJhbmRvbS5yYW5kbihuX3RyYWluLCBkKS5hc3R5cGUobnAuZmxvYXQzMilcbiAgICBYX3F1ZXJ5ID0gbnAucmFuZG9tLnJhbmRuKG5fcXVlcnksIGQpLmFzdHlwZShucC5mbG9hdDMyKVxuXG4gICAgIyBFeGFjdCBicnV0ZSBmb3JjZSAoRmxhdClcbiAgICBpbmRleF9mbGF0ID0gZmFpc3MuSW5kZXhGbGF0TDIoZClcbiAgICBpbmRleF9mbGF0LmFkZChYX3RyYWluKVxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBEX2ZsYXQsIElfZmxhdCA9IGluZGV4X2ZsYXQuc2VhcmNoKFhfcXVlcnksIGspXG4gICAgdF9mbGF0ID0gdGltZS50aW1lKCkgLSB0MFxuXG4gICAgIyBJVkYgYXBwcm94aW1hdGUg4oCUIGNsdXN0ZXJzIHRoZW4gc2VhcmNoZXMgbnByb2JlIGNsdXN0ZXJzXG4gICAgcXVhbnRpemVyID0gZmFpc3MuSW5kZXhGbGF0TDIoZClcbiAgICBpbmRleF9pdmYgPSBmYWlzcy5JbmRleElWRkZsYXQocXVhbnRpemVyLCBkLCAxMDApXG4gICAgaW5kZXhfaXZmLnRyYWluKFhfdHJhaW4pXG4gICAgaW5kZXhfaXZmLmFkZChYX3RyYWluKVxuICAgIGluZGV4X2l2Zi5ucHJvYmUgPSAxMFxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBEX2l2ZiwgSV9pdmYgPSBpbmRleF9pdmYuc2VhcmNoKFhfcXVlcnksIGspXG4gICAgdF9pdmYgPSB0aW1lLnRpbWUoKSAtIHQwXG5cbiAgICByZWNhbGwgPSBucC5tZWFuKFtsZW4oc2V0KElfaXZmW2ldKSBcdTAwMjYgc2V0KElfZmxhdFtpXSkpIC8gayBmb3IgaSBpbiByYW5nZShuX3F1ZXJ5KV0pXG4gICAgcHJpbnQoZlx1MDAyN0ZsYXQgZXhhY3Q6IHt0X2ZsYXQqMTAwMDouMWZ9IG1zXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdJVkYgYXBwcm94OiB7dF9pdmYqMTAwMDouMWZ9IG1zICByZWNhbGxAe2t9PXtyZWNhbGw6LjRmfSAgc3BlZWR1cD17dF9mbGF0L3RfaXZmOi4xZn14XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpbWVuc2lvbmFsaXR5IFJlZHVjdGlvbiBhbmQga05OIGZvciBBbm9tYWx5IERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHN0YW5kYXJkIHJlbWVkeSBmb3Iga05OIGluIGhpZ2ggZGltZW5zaW9ucyBpcyBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb24gYmVmb3JlIGNvbXB1dGluZyBkaXN0YW5jZXMuIFBDQSBpcyB0aGUgbW9zdCBjb21tb24gZmlyc3Qgc3RlcCDigJQgcHJvamVjdGluZyB0byB0aGUgdG9wIDUw4oCTMTAwIHByaW5jaXBhbCBjb21wb25lbnRzIHJlbW92ZXMgbm9pc2UgZGltZW5zaW9ucyB3aGlsZSBwcmVzZXJ2aW5nIHRoZSBidWxrIG9mIHZhcmlhbmNlLiBVTUFQIChVbmlmb3JtIE1hbmlmb2xkIEFwcHJveGltYXRpb24gYW5kIFByb2plY3Rpb24pIGlzIGJldHRlciBmb3IgcHJlc2VydmluZyBsb2NhbCBzdHJ1Y3R1cmUgYW5kIGlzIGNvbW1vbmx5IHVzZWQgYmVmb3JlIGtOTi1iYXNlZCBjbHVzdGVyaW5nIG9yIHJldHJpZXZhbC4gRm9yIGFub21hbHkgZGV0ZWN0aW9uLCB0aGUgTG9jYWwgT3V0bGllciBGYWN0b3IgKExPRikgdXNlcyBrTk4gZGlzdGFuY2VzIHRvIGNvbXB1dGUgYSBsb2NhbCBkZW5zaXR5IHNjb3JlOiBwb2ludHMgaW4gc3BhcnNlIG5laWdoYm9yaG9vZHMgKGZhciBmcm9tIHRoZWlyIGsgbmVhcmVzdCBuZWlnaGJvcnMgcmVsYXRpdmUgdG8gdGhvc2UgbmVpZ2hib3JzXHUwMDI3IG11dHVhbCBkaXN0YW5jZXMpIGFyZSBmbGFnZ2VkIGFzIG91dGxpZXJzLiBUaGlzIHdvcmtzIHdlbGwgaW4gbW9kZXJhdGUgZGltZW5zaW9ucyAoZCDiiaQgMjApIGJ1dCByZXF1aXJlcyBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb24gZmlyc3QgaW4gaGlnaC1kIHNldHRpbmdzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJRdWVyeSBTcGVlZCIsIk1lbW9yeSIsIlJlY2FsbCIsIkRpbWVuc2lvbiBMaW1pdCIsIk5vdGVzIl0sInJvd3MiOltbIkJydXRlIGZvcmNlIChMMikiLCJPKG5kKSIsIk8obmQpIiwiMTAwJSBleGFjdCIsIkFueSAoc2xvdykiLCJCZXN0IGZvciBuIFx1MDAzYyAxMGsgb3IgZCBcdTAwM2MgMTAiXSxbImtkLXRyZWUiLCJPKGxvZyBuKSBmb3IgZOKJpDIwIiwiTyhuZCkiLCIxMDAlIGV4YWN0IiwiZCDiiaQgMjAiLCJGYWxscyBiYWNrIHRvIGJydXRlIGZvcmNlIGluIGhpZ2ggZCJdLFsiQmFsbCB0cmVlIiwiTyhsb2cgbikgZm9yIGTiiaQzMCIsIk8obmQpIiwiMTAwJSBleGFjdCIsImQg4omkIDMwIiwiU2xpZ2h0bHkgYmV0dGVyIHRoYW4ga2QtdHJlZSBpbiBtZWRpdW0gZCJdLFsiSE5TVyIsIk8obG9nIG4pIiwiTyhuwrdNwrdkKSIsIlx1MDAzZTk5JSB3aXRoIGVmIHR1bmluZyIsImQg4omkIDE1MzYrIiwiQmVzdCBmb3IgaGlnaCBkLCBHUFUtZnJlZSBwcm9kdWN0aW9uIl0sWyJGYWlzcyBJVkYiLCJPKG5saXN0wrducHJvYmXCt2QpIiwiTyhuZCkiLCJUdW5hYmxlIHZpYSBucHJvYmUiLCJkIOKJpCA0MDk2KyIsIkJlc3QgZm9yIEdQVSArIGJpbGxpb24tc2NhbGUgcmV0cmlldmFsIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFsd2F5cyBzdGFuZGFyZGlzZSBmZWF0dXJlcyBiZWZvcmUgY29tcHV0aW5nIEV1Y2xpZGVhbiBkaXN0YW5jZXMg4oCUIGRpZmZlcmluZyBzY2FsZXMgZG9taW5hdGUgdGhlIG1ldHJpYy4iLCJGb3IgZCBcdTAwM2UgMjAsIHVzZSBza2xlYXJuXHUwMDI3cyBcdTAwMjdiYWxsX3RyZWVcdTAwMjcgYWxnb3JpdGhtOyBmb3IgZCBcdTAwM2UgMzAsIHN3aXRjaCB0byBITlNXIG9yIEZhaXNzLiIsIkFwcGx5IFBDQSAoNTDigJMxMDAgY29tcG9uZW50cykgb3IgVU1BUCBiZWZvcmUga05OIGluIGhpZ2gtZGltZW5zaW9uYWwgc2V0dGluZ3MuIiwiQ3Jvc3MtdmFsaWRhdGUgayBvdmVyIGEgbG9nLXNwYWNlZCByYW5nZSBbMSwgMywgNSwgMTEsIDIxLCA1MV07IG9kZCB2YWx1ZXMgYXZvaWQgdGllcyBpbiBiaW5hcnkgY2xhc3NpZmljYXRpb24uIiwiRm9yIHRleHQvZW1iZWRkaW5ncywgdXNlIGNvc2luZSBkaXN0YW5jZSBpbnN0ZWFkIG9mIEV1Y2xpZGVhbiB0byBmb2N1cyBvbiBkaXJlY3Rpb24gcmF0aGVyIHRoYW4gbWFnbml0dWRlLiIsIkZvciBhbm9tYWx5IGRldGVjdGlvbiwgdXNlIExPRiAoTG9jYWxPdXRsaWVyRmFjdG9yIGluIHNrbGVhcm4pIHdoaWNoIHVzZXMga05OIGRpc3RhbmNlcyBmb3IgbG9jYWwgZGVuc2l0eSBlc3RpbWF0aW9uLiJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQWx3YXlzIFN0YW5kYXJkaXNlIEJlZm9yZSBrTk4iLCJjb250ZW50Ijoia05OIGlzIGV4dHJlbWVseSBzZW5zaXRpdmUgdG8gZmVhdHVyZSBzY2FsZS4gQSBmZWF0dXJlIHdpdGggcmFuZ2UgWzAsIDEwMDBdIGRvbWluYXRlcyBvbmUgd2l0aCByYW5nZSBbMCwgMV0gaW4gRXVjbGlkZWFuIGRpc3RhbmNlLiBBbHdheXMgYXBwbHkgU3RhbmRhcmRTY2FsZXIgYmVmb3JlIGtOTi4gVXNlIGNvc2luZSBzaW1pbGFyaXR5IGZvciB0ZXh0L2VtYmVkZGluZ3Mgd2hlcmUgbWFnbml0dWRlIGlzIGlycmVsZXZhbnQuIE1haGFsYW5vYmlzIGRpc3RhbmNlIGFjY291bnRzIGZvciBmZWF0dXJlIGNvcnJlbGF0aW9ucyBhbmQgaXMgZXF1aXZhbGVudCB0byBFdWNsaWRlYW4gYWZ0ZXIgUENBLXdoaXRlbmluZywgYnV0IHJlcXVpcmVzIGVzdGltYXRpbmcgdGhlIGNvdmFyaWFuY2UgbWF0cml4IChuZWVkcyBuIFx1MDAzZVx1MDAzZSBwKS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikh5cGVycGFyYW1ldGVyIHNlbGVjdGlvbjogayBpcyBjaG9zZW4gYnkgY3Jvc3MtdmFsaWRhdGlvbiBvdmVyIGEgbG9nLXNwYWNlZCBncmlkIFsxLCAzLCA1LCAxMSwgMjEsIDUxXS4gT2RkIHZhbHVlcyBhdm9pZCB0aWUtYnJlYWtpbmcgaW4gYmluYXJ5IGNsYXNzaWZpY2F0aW9uLiBMYXJnZXIgayBnaXZlcyBzbW9vdGhlciBib3VuZGFyaWVzIGFuZCBoaWdoZXIgYmlhczsgaz0xIGdpdmVzIHplcm8gdHJhaW5pbmcgZXJyb3IgYW5kIG1heGltdW0gdmFyaWFuY2UuIFdlaWdodCBjYW4gYmUgYWRkZWQgdG8gbmVpZ2hib3JzIGJ5IGludmVyc2UgZGlzdGFuY2UgKHdlaWdodHM9XHUwMDI3ZGlzdGFuY2VcdTAwMjcgaW4gc2tsZWFybikgdG8gcmVkdWNlIHRoZSBjb250cmlidXRpb24gb2YgZmFyLWF3YXkgbmVpZ2hib3JzLiBGb3IgaGlnaC1kIGRhdGEsIGFsd2F5cyByZWR1Y2UgZGltZW5zaW9uYWxpdHkgZmlyc3Qg4oCUIHRoZSBlZmZlY3RpdmUgayBpcyBtdWNoIGxhcmdlciBpbiBoaWdoIGRpbWVuc2lvbnMgdGhhbiB0aGUgbm9taW5hbCB2YWx1ZSBzdWdnZXN0cy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# k-Nearest Neighbors and the Curse of Dimensionality

k-Nearest Neighbors is among the simplest non-parametric learning algorithms: for a query point x, find the k training points closest in feature space and predict by majority vote (classification) or mean (regression). Despite its simplicity, kNN has strong theoretical foundations — as n→∞ with k/n→0, the kNN error converges to twice the Bayes error. However, kNN degrades severely in high dimensions due to the curse of dimensionality, where all pairwise distances become approximately equal, making 'nearest' meaningless.

## kNN from First Principles

Given a query x, compute d(x, xᵢ) for all n training points, sort, take the k smallest, and aggregate labels. The choice of k controls the bias-variance tradeoff: k=1 gives zero training error (extremely high variance); large k gives smooth, stable boundaries (higher bias). The optimal k is found via cross-validation. The algorithm is lazy (non-parametric): all computation happens at query time, with O(nd) cost per query for brute force. kNN is non-parametric — it makes no assumption about the functional form of the decision boundary, only that nearby points share the same label.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class KNNClassifier:
    def __init__(self, k=5, metric='euclidean'):
        self.k = k
        self.metric = metric

    def fit(self, X, y):
        self.X_train = X.copy()
        self.y_train = y.copy()
        return self

    def _distances(self, x):
        if self.metric == 'euclidean':
            return np.sqrt(np.sum((self.X_train - x)**2, axis=1))
        elif self.metric == 'manhattan':
            return np.sum(np.abs(self.X_train - x), axis=1)
        elif self.metric == 'cosine':
            norm = np.linalg.norm(self.X_train, axis=1) * np.linalg.norm(x) + 1e-10
            return 1 - (self.X_train @ x) / norm

    def predict(self, X):
        preds = []
        for x in X:
            dists = self._distances(x)
            nn_idx = np.argsort(dists)[:self.k]
            votes = self.y_train[nn_idx]
            preds.append(np.bincount(votes).argmax())
        return np.array(preds)

np.random.seed(42)
X, y = make_classification(n_samples=500, n_features=6, n_informative=4, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)

for k in [1, 3, 5, 11, 21]:
    knn = KNNClassifier(k=k).fit(X_tr, y_tr)
    acc = accuracy_score(y_te, knn.predict(X_te))
    print(f'k={k:>2}: accuracy={acc:.4f}')
```

## Distance Metrics and Choosing the Right One

The choice of distance metric is critical for kNN. Euclidean (L2): sqrt(Σ(xᵢ-yᵢ)²) — sensitive to scale, dominated by high-magnitude features, requires standardisation. Manhattan (L1): Σ|xᵢ-yᵢ| — more robust to outliers, preferred for sparse high-dimensional data. Cosine: 1 - (x·y)/(‖x‖‖y‖) — measures angle, ignores magnitude, ideal for text embeddings and documents. Mahalanobis: sqrt((x-y)ᵀΣ⁻¹(x-y)) — accounts for feature correlations and scales, equivalent to Euclidean after whitening. Hamming distance for binary features. Always standardise features before Euclidean kNN — a feature with range [0, 1000] dominates one with range [0, 1].

## The Curse of Dimensionality

In d dimensions, the concentration of measure phenomenon states that all pairwise distances converge to the same value as d→∞: (max_dist - min_dist) / min_dist → 0. The volume of a unit ball shrinks relative to the unit hypercube as (π^{d/2}/Γ(d/2+1)) / 2^d → 0 as d→∞. To capture a fixed fraction p of the training data in a nearest-neighbor ball, the ball radius must grow to r = p^{1/d}. For p=0.01 (1% of data) and d=100, r ≈ 0.955 — almost the full range of the unit hypercube. When all distances are approximately equal, the concept of 'nearest' loses meaning and kNN degrades to random guessing.

```python
import numpy as np

np.random.seed(42)
n_ref, n_query = 1000, 100

print(f'{'Dim':>5} {'Mean Dist':>12} {'Std Dist':>12} {'CoV':>10} {'Rel Range':>12}')
for d in [2, 5, 10, 20, 50, 100, 200, 500]:
    X_ref = np.random.uniform(0, 1, (n_ref, d))
    X_q   = np.random.uniform(0, 1, (n_query, d))
    # Euclidean distances from all query points to all reference points
    dists = np.sqrt(np.sum((X_ref[None,:,:] - X_q[:,None,:])**2, axis=2)).ravel()
    mean_d = dists.mean()
    std_d  = dists.std()
    cov    = std_d / (mean_d + 1e-12)          # coefficient of variation
    rel_range = (dists.max() - dists.min()) / (dists.min() + 1e-12)
    print(f'{d:>5} {mean_d:>12.4f} {std_d:>12.4f} {cov:>10.4f} {rel_range:>12.4f}')
```

> **kNN Fails Silently in High Dimensions**: In high dimensions, kNN still returns predictions — it just returns meaningless ones. The k nearest neighbors of a query point are no more similar to it than random points from the dataset. The model appears to work on the training set but generalises poorly. Always check performance vs dimensionality and apply PCA, UMAP, or feature selection before applying kNN to data with d > 20. A sharp drop in recall of the exact nearest neighbor is a reliable diagnostic.

## kd-Trees and Ball Trees for Exact NN

For low-dimensional data (d ≤ 20), exact nearest neighbor search can be accelerated beyond brute force. kd-trees recursively partition space with axis-aligned splits, enabling O(log n) average query time for d ≤ 20 — but performance degrades back to O(n) for d > 20 because the tree has O(2^d) leaf nodes. Ball trees partition space with hyperspheres instead of hyperplanes, which handles non-axis-aligned boundaries better and works well up to d ≈ 30. Both are implemented in sklearn's NearestNeighbors with algorithm='kd_tree' or 'ball_tree'. For d > 20-30, approximate methods (HNSW, Faiss) are necessary.

## Approximate Nearest Neighbors — HNSW and Faiss

Hierarchical Navigable Small World (HNSW) graphs build a multi-layer proximity graph where layer 0 contains all points and higher layers contain progressively fewer points. Query time is O(log n) with >99% recall at typical settings. HNSW is the engine behind many production vector search systems. Faiss (Facebook AI Similarity Search) provides GPU-accelerated ANN with IVF (Inverted File Index) which clusters the data and searches only nearby clusters (nprobe clusters), giving controllable speed-recall tradeoffs at billion-scale.

```python
import numpy as np
import time
from sklearn.neighbors import NearestNeighbors

try:
    import hnswlib
    has_hnsw = True
except ImportError:
    has_hnsw = False
    print('hnswlib not installed')

np.random.seed(42)
d, n_index, n_query = 64, 10000, 200
X_index = np.random.randn(n_index, d).astype(np.float32)
X_query = np.random.randn(n_query, d).astype(np.float32)

# Brute force exact NN
bf = NearestNeighbors(n_neighbors=10, algorithm='brute', metric='euclidean')
bf.fit(X_index)
t0 = time.time()
bf_dist, bf_idx = bf.kneighbors(X_query)
bf_time = time.time() - t0
print(f'Brute force: {bf_time*1000:.1f} ms for {n_query} queries')

if has_hnsw:
    p = hnswlib.Index(space='l2', dim=d)
    p.init_index(max_elements=n_index, ef_construction=200, M=16)
    p.add_items(X_index)
    p.set_ef(50)  # ef controls recall vs speed
    t0 = time.time()
    hnsw_idx, _ = p.knn_query(X_query, k=10)
    hnsw_time = time.time() - t0
    recall = np.mean([len(set(hnsw_idx[i]) & set(bf_idx[i])) / 10 for i in range(n_query)])
    print(f'HNSW: {hnsw_time*1000:.1f} ms,  recall@10={recall:.4f},  speedup={bf_time/hnsw_time:.1f}x')
```

```python
import numpy as np
import time

try:
    import faiss
    has_faiss = True
except ImportError:
    has_faiss = False
    print('faiss not installed; skipping')

if has_faiss:
    np.random.seed(42)
    d, n_train, n_query, k = 128, 50000, 1000, 10
    X_train = np.random.randn(n_train, d).astype(np.float32)
    X_query = np.random.randn(n_query, d).astype(np.float32)

    # Exact brute force (Flat)
    index_flat = faiss.IndexFlatL2(d)
    index_flat.add(X_train)
    t0 = time.time()
    D_flat, I_flat = index_flat.search(X_query, k)
    t_flat = time.time() - t0

    # IVF approximate — clusters then searches nprobe clusters
    quantizer = faiss.IndexFlatL2(d)
    index_ivf = faiss.IndexIVFFlat(quantizer, d, 100)
    index_ivf.train(X_train)
    index_ivf.add(X_train)
    index_ivf.nprobe = 10
    t0 = time.time()
    D_ivf, I_ivf = index_ivf.search(X_query, k)
    t_ivf = time.time() - t0

    recall = np.mean([len(set(I_ivf[i]) & set(I_flat[i])) / k for i in range(n_query)])
    print(f'Flat exact: {t_flat*1000:.1f} ms')
    print(f'IVF approx: {t_ivf*1000:.1f} ms  recall@{k}={recall:.4f}  speedup={t_flat/t_ivf:.1f}x')
```

## Dimensionality Reduction and kNN for Anomaly Detection

The standard remedy for kNN in high dimensions is dimensionality reduction before computing distances. PCA is the most common first step — projecting to the top 50–100 principal components removes noise dimensions while preserving the bulk of variance. UMAP (Uniform Manifold Approximation and Projection) is better for preserving local structure and is commonly used before kNN-based clustering or retrieval. For anomaly detection, the Local Outlier Factor (LOF) uses kNN distances to compute a local density score: points in sparse neighborhoods (far from their k nearest neighbors relative to those neighbors' mutual distances) are flagged as outliers. This works well in moderate dimensions (d ≤ 20) but requires dimensionality reduction first in high-d settings.

| Method | Query Speed | Memory | Recall | Dimension Limit | Notes |
| --- | --- | --- | --- | --- | --- |
| Brute force (L2) | O(nd) | O(nd) | 100% exact | Any (slow) | Best for n < 10k or d < 10 |
| kd-tree | O(log n) for d≤20 | O(nd) | 100% exact | d ≤ 20 | Falls back to brute force in high d |
| Ball tree | O(log n) for d≤30 | O(nd) | 100% exact | d ≤ 30 | Slightly better than kd-tree in medium d |
| HNSW | O(log n) | O(n·M·d) | >99% with ef tuning | d ≤ 1536+ | Best for high d, GPU-free production |
| Faiss IVF | O(nlist·nprobe·d) | O(nd) | Tunable via nprobe | d ≤ 4096+ | Best for GPU + billion-scale retrieval |

- Always standardise features before computing Euclidean distances — differing scales dominate the metric.
- For d > 20, use sklearn's 'ball_tree' algorithm; for d > 30, switch to HNSW or Faiss.
- Apply PCA (50–100 components) or UMAP before kNN in high-dimensional settings.
- Cross-validate k over a log-spaced range [1, 3, 5, 11, 21, 51]; odd values avoid ties in binary classification.
- For text/embeddings, use cosine distance instead of Euclidean to focus on direction rather than magnitude.
- For anomaly detection, use LOF (LocalOutlierFactor in sklearn) which uses kNN distances for local density estimation.

> **Always Standardise Before kNN**: kNN is extremely sensitive to feature scale. A feature with range [0, 1000] dominates one with range [0, 1] in Euclidean distance. Always apply StandardScaler before kNN. Use cosine similarity for text/embeddings where magnitude is irrelevant. Mahalanobis distance accounts for feature correlations and is equivalent to Euclidean after PCA-whitening, but requires estimating the covariance matrix (needs n >> p).

Hyperparameter selection: k is chosen by cross-validation over a log-spaced grid [1, 3, 5, 11, 21, 51]. Odd values avoid tie-breaking in binary classification. Larger k gives smoother boundaries and higher bias; k=1 gives zero training error and maximum variance. Weight can be added to neighbors by inverse distance (weights='distance' in sklearn) to reduce the contribution of far-away neighbors. For high-d data, always reduce dimensionality first — the effective k is much larger in high dimensions than the nominal value suggests.

---

