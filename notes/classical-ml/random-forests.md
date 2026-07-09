---
title: "Random Forests — Bagging and Feature Subsampling"
slug: "random-forests"
description: "How Random Forests reduce variance through bootstrap aggregation and feature subsampling, OOB error as free validation, Gini vs permutation importance, and Extra-Trees as a faster variant."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhZ2dpbmcg4oCUIEJvb3RzdHJhcCBBZ2dyZWdhdGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmFnZ2luZyAoYm9vdHN0cmFwIGFnZ3JlZ2F0aW5nKSB0cmFpbnMgQiBtb2RlbHMgb24gQiBib290c3RyYXAgc2FtcGxlcyBkcmF3biB3aXRoIHJlcGxhY2VtZW50IGZyb20gdGhlIHRyYWluaW5nIHNldC4gRWFjaCBib290c3RyYXAgc2FtcGxlIGNvbnRhaW5zIH42My4yJSB1bmlxdWUgZXhhbXBsZXMgKHRoZSByZXN0IGFyZSBkdXBsaWNhdGVzKS4gUHJlZGljdGlvbnMgYXJlIGFnZ3JlZ2F0ZWQgYnkgbWFqb3JpdHkgdm90ZSAoY2xhc3NpZmljYXRpb24pIG9yIG1lYW4gKHJlZ3Jlc3Npb24pLiBUaGUgdmFyaWFuY2Ugb2YgdGhlIGF2ZXJhZ2Ugb2YgQiBjb3JyZWxhdGVkIGVzdGltYXRvcnMgaXMgz4PCsigoMS3PgSkvQiArIM+BKSDigJQgd2hlbiDPgT0wIChwZXJmZWN0bHkgdW5jb3JyZWxhdGVkKSwgdmFyaWFuY2Ugc2hyaW5rcyBhcyAxL0I7IHdoZW4gz4E9MSAoaWRlbnRpY2FsIG1vZGVscyksIG5vIHJlZHVjdGlvbi4gRGVjb3JyZWxhdGlvbiBpcyB0aGVyZWZvcmUgZXNzZW50aWFsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi50cmVlIGltcG9ydCBEZWNpc2lvblRyZWVDbGFzc2lmaWVyXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfaXJpc1xuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuXG5jbGFzcyBCYWdnaW5nQ2xhc3NpZmllcjpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbl9lc3RpbWF0b3JzPTUwLCBtYXhfZGVwdGg9NSwgcmFuZG9tX3N0YXRlPTQyKTpcbiAgICAgICAgc2VsZi5uX2VzdGltYXRvcnMgPSBuX2VzdGltYXRvcnNcbiAgICAgICAgc2VsZi5tYXhfZGVwdGggPSBtYXhfZGVwdGhcbiAgICAgICAgc2VsZi5yYW5kb21fc3RhdGUgPSByYW5kb21fc3RhdGVcbiAgICAgICAgc2VsZi50cmVlcyA9IFtdXG5cbiAgICBkZWYgZml0KHNlbGYsIFgsIHkpOlxuICAgICAgICBybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoc2VsZi5yYW5kb21fc3RhdGUpXG4gICAgICAgIG4gPSBsZW4oeSlcbiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uoc2VsZi5uX2VzdGltYXRvcnMpOlxuICAgICAgICAgICAgaWR4ID0gcm5nLmNob2ljZShuLCBzaXplPW4sIHJlcGxhY2U9VHJ1ZSkgICAjIGJvb3RzdHJhcFxuICAgICAgICAgICAgdHJlZSA9IERlY2lzaW9uVHJlZUNsYXNzaWZpZXIobWF4X2RlcHRoPXNlbGYubWF4X2RlcHRoLCByYW5kb21fc3RhdGU9aSlcbiAgICAgICAgICAgIHRyZWUuZml0KFhbaWR4XSwgeVtpZHhdKVxuICAgICAgICAgICAgc2VsZi50cmVlcy5hcHBlbmQodHJlZSlcbiAgICAgICAgcmV0dXJuIHNlbGZcblxuICAgIGRlZiBwcmVkaWN0KHNlbGYsIFgpOlxuICAgICAgICBwcmVkcyA9IG5wLmFycmF5KFt0LnByZWRpY3QoWCkgZm9yIHQgaW4gc2VsZi50cmVlc10pXG4gICAgICAgIHJldHVybiBucC5hcHBseV9hbG9uZ19heGlzKFxuICAgICAgICAgICAgbGFtYmRhIHg6IG5wLmJpbmNvdW50KHguYXN0eXBlKGludCkpLmFyZ21heCgpLCBheGlzPTAsIGFycj1wcmVkcylcblxuWCwgeSA9IGxvYWRfaXJpcyhyZXR1cm5fWF95PVRydWUpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4yLCByYW5kb21fc3RhdGU9NDIpXG5tb2RlbCA9IEJhZ2dpbmdDbGFzc2lmaWVyKG5fZXN0aW1hdG9ycz0xMDAsIG1heF9kZXB0aD01KS5maXQoWF90ciwgeV90cilcbnByZWRzID0gbW9kZWwucHJlZGljdChYX3RlKVxucHJpbnQoZlx1MDAyN0JhZ2dpbmcgYWNjdXJhY3k6IHsocHJlZHMgPT0geV90ZSkubWVhbigpOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmVhdHVyZSBTdWJzYW1wbGluZyBhbmQgRGVjb3JyZWxhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmFuZG9tIEZvcmVzdHMgYWRkIGEgc2Vjb25kIHNvdXJjZSBvZiByYW5kb21uZXNzOiBhdCBlYWNoIHNwbGl0IG9ubHkgYSByYW5kb20gc3Vic2V0IG9mIG0gZmVhdHVyZXMgaXMgY29uc2lkZXJlZCAobm90IGFsbCBwKS4gVGhpcyBkZWNvcnJlbGF0ZXMgdGhlIHRyZWVzIGV2ZW4gd2hlbiBvbmUgZmVhdHVyZSBkb21pbmF0ZXMsIGJyZWFraW5nIHRoZSBjb3JyZWxhdGlvbiDPgSBpbiB0aGUgdmFyaWFuY2UgZm9ybXVsYS4gU3RhbmRhcmQgY2hvaWNlczogbSA9IOKImnAgZm9yIGNsYXNzaWZpY2F0aW9uLCBtID0gcC8zIGZvciByZWdyZXNzaW9uLiBTbWFsbGVyIG0g4oaSIG1vcmUgZGVjb3JyZWxhdGlvbiDihpIgbW9yZSB2YXJpYW5jZSByZWR1Y3Rpb24sIGJ1dCBlYWNoIGluZGl2aWR1YWwgdHJlZSBpcyB3ZWFrZXIgKGhpZ2hlciBiaWFzKS4gVGhlIGJpYXMtdmFyaWFuY2Ugc3dlZXQgc3BvdCBpcyB0eXBpY2FsbHkg4oiacC4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoeSA2My4yJSBVbmlxdWUgU2FtcGxlcyBwZXIgQm9vdHN0cmFwIiwiY29udGVudCI6IldpdGggbiBkcmF3cyBmcm9tIG4gc2FtcGxlcyB3aXRoIHJlcGxhY2VtZW50LCB0aGUgcHJvYmFiaWxpdHkgYSBzcGVjaWZpYyBzYW1wbGUgaXMgbmV2ZXIgY2hvc2VuIGlzICgxIOKIkiAxL24pXm4g4oaSIDEvZSDiiYggMzYuOCUgYXMgbiDihpIg4oieLiBTbyBlYWNoIGJvb3RzdHJhcCBzYW1wbGUgY29udGFpbnMgcm91Z2hseSA2My4yJSB1bmlxdWUgdHJhaW5pbmcgZXhhbXBsZXMsIGxlYXZpbmcgfjM2LjglIGFzIHRoZSBvdXQtb2YtYmFnIChPT0IpIHNldCBmb3IgZnJlZSB2YWxpZGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik91dC1vZi1CYWcgRXJyb3IgYW5kIHNrbGVhcm4gSW1wbGVtZW50YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB+MzYuOCUgb2Ygc2FtcGxlcyBub3QgaW5jbHVkZWQgaW4gZWFjaCB0cmVlXHUwMDI3cyBib290c3RyYXAgc2FtcGxlIGZvcm0gaXRzIG91dC1vZi1iYWcgc2V0LiBFYWNoIHNhbXBsZVx1MDAyN3MgT09CIHByZWRpY3Rpb24gaXMgdGhlIGFnZ3JlZ2F0ZSBvZiB0cmVlcyB0aGF0IGRpZCBub3QgdHJhaW4gb24gaXQuIE9PQiBlcnJvciBpcyBhIG5lYXJseSB1bmJpYXNlZCBlc3RpbWF0ZSBvZiB0ZXN0IGVycm9yIOKAlCBlc3NlbnRpYWxseSBhIGZyZWUgY3Jvc3MtdmFsaWRhdGlvbiDigJQgdmFsaWQgd2hlbiB0aGUgZm9yZXN0IGlzIGxhcmdlIGVub3VnaCAo4omlMjAwIHRyZWVzKS4gRW5hYmxlIHdpdGggb29iX3Njb3JlPVRydWUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImZyb20gc2tsZWFybi5lbnNlbWJsZSBpbXBvcnQgUmFuZG9tRm9yZXN0Q2xhc3NpZmllclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2JyZWFzdF9jYW5jZXJcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcblxuWCwgeSA9IGxvYWRfYnJlYXN0X2NhbmNlcihyZXR1cm5fWF95PVRydWUpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4yLCByYW5kb21fc3RhdGU9NDIpXG5cbnJmID0gUmFuZG9tRm9yZXN0Q2xhc3NpZmllcihcbiAgICBuX2VzdGltYXRvcnM9MzAwLFxuICAgIG1heF9mZWF0dXJlcz1cdTAwMjdzcXJ0XHUwMDI3LCAgICAgICAjIHNxcnQocCkgZmVhdHVyZXMgcGVyIHNwbGl0XG4gICAgbWF4X2RlcHRoPU5vbmUsXG4gICAgbWluX3NhbXBsZXNfbGVhZj0zLFxuICAgIG9vYl9zY29yZT1UcnVlLCAgICAgICAgICAgICMgZnJlZSB2YWxpZGF0aW9uIGZyb20gfjM2LjglIE9PQiBzYW1wbGVzXG4gICAgbl9qb2JzPS0xLFxuICAgIHJhbmRvbV9zdGF0ZT00MlxuKVxucmYuZml0KFhfdHIsIHlfdHIpXG5cbnByaW50KGZcdTAwMjdPT0Igc2NvcmU6ICAgICAge3JmLm9vYl9zY29yZV86LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdUZXN0IHNjb3JlOiAgICAge3JmLnNjb3JlKFhfdGUsIHlfdGUpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3RmVhdHVyZXMvc3BsaXQ6IHtyZi5tYXhfZmVhdHVyZXNffSBvZiB7WC5zaGFwZVsxXX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmVhdHVyZSBJbXBvcnRhbmNlIOKAlCBHaW5pIHZzIFBlcm11dGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHaW5pIGltcG9ydGFuY2UgKE1ESSkgc3VtcyBpbXB1cml0eSByZWR1Y3Rpb25zIHdlaWdodGVkIGJ5IHNhbXBsZSBmcmFjdGlvbiBhY3Jvc3MgYWxsIHRyZWVzLiBJdCBpcyBmYXN0IGJ1dCBiaWFzZWQgdG93YXJkIGhpZ2gtY2FyZGluYWxpdHkgYW5kIGNvbnRpbnVvdXMgZmVhdHVyZXMuIFBlcm11dGF0aW9uIGltcG9ydGFuY2UgbWVhc3VyZXMgdGhlIGRyb3AgaW4gbW9kZWwgYWNjdXJhY3kgd2hlbiBhIGZlYXR1cmVcdTAwMjdzIHZhbHVlcyBhcmUgcmFuZG9tbHkgc2h1ZmZsZWQgb24gdGhlIHRlc3Qgc2V0IOKAlCBpdCBpcyBtb2RlbC1hZ25vc3RpYyBhbmQgdW5iaWFzZWQuIFJ1biBrPTEwLTMwIHJlcGV0aXRpb25zIGZvciBzdGFibGUgZXN0aW1hdGVzLiBTSEFQIGdpdmVzIGxvY2FsIGV4cGxhbmF0aW9ucyBvbiB0b3Agb2YgZ2xvYmFsIGltcG9ydGFuY2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkJpYXMgKGNhcmRpbmFsaXR5KSIsIkNvcnJlbGF0ZWQgRmVhdHVyZXMiLCJDb3N0IiwiR2xvYmFsIC8gTG9jYWwiXSwicm93cyI6W1siR2luaSAvIE1ESSIsIlllcyDigJQgaGlnaC1jYXJkaW5hbGl0eSBpbmZsYXRlZCIsIkluZmxhdGVzIGJvdGggZmVhdHVyZXMiLCJOZWdsaWdpYmxlIChjb21wdXRlZCBkdXJpbmcgdHJhaW5pbmcpIiwiR2xvYmFsIG9ubHkiXSxbIlBlcm11dGF0aW9uIiwiTm9uZSIsIlNwbGl0cyBpbXBvcnRhbmNlIGJldHdlZW4gY29ycmVsYXRlZCIsIk1vZGVyYXRlIChrIMOXIG4gcHJlZGljdGlvbnMpIiwiR2xvYmFsIG9ubHkiXSxbIlNIQVAiLCJOb25lIiwiRGlzdHJpYnV0ZXMgZmFpcmx5IiwiSGlnaCAoTyhUTETCsikgVHJlZVNIQVApIiwiQm90aCBnbG9iYWwgYW5kIGxvY2FsIl0sWyJMSU1FIiwiTm9uZSIsIlVuc3RhYmxlIiwiTW9kZXJhdGUiLCJMb2NhbCBvbmx5Il1dfSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZW5zZW1ibGUgaW1wb3J0IFJhbmRvbUZvcmVzdENsYXNzaWZpZXJcbmZyb20gc2tsZWFybi5pbnNwZWN0aW9uIGltcG9ydCBwZXJtdXRhdGlvbl9pbXBvcnRhbmNlXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcblxuIyBDb3JyZWxhdGVkIGZlYXR1cmVzIGhpZ2hsaWdodCBNREkgYmlhc1xuWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24obl9zYW1wbGVzPTEwMDAsIG5fZmVhdHVyZXM9MTAsIG5faW5mb3JtYXRpdmU9MyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX3JlZHVuZGFudD01LCByYW5kb21fc3RhdGU9NDIpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4yLCByYW5kb21fc3RhdGU9NDIpXG5cbnJmID0gUmFuZG9tRm9yZXN0Q2xhc3NpZmllcihuX2VzdGltYXRvcnM9MjAwLCByYW5kb21fc3RhdGU9NDIpXG5yZi5maXQoWF90ciwgeV90cilcblxuZ2luaV9pbXAgPSByZi5mZWF0dXJlX2ltcG9ydGFuY2VzX1xucGVybSA9IHBlcm11dGF0aW9uX2ltcG9ydGFuY2UocmYsIFhfdGUsIHlfdGUsIG5fcmVwZWF0cz0xNSwgcmFuZG9tX3N0YXRlPTQyKVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMSwgMiwgZmlnc2l6ZT0oMTMsIDUpKVxuYXhlc1swXS5iYXIocmFuZ2UoMTApLCBnaW5pX2ltcCk7IGF4ZXNbMF0uc2V0X3RpdGxlKFx1MDAyN0dpbmkgKE1ESSkgSW1wb3J0YW5jZVx1MDAyNylcbmF4ZXNbMV0uYmFyKHJhbmdlKDEwKSwgcGVybS5pbXBvcnRhbmNlc19tZWFuKTsgYXhlc1sxXS5zZXRfdGl0bGUoXHUwMDI3UGVybXV0YXRpb24gSW1wb3J0YW5jZVx1MDAyNylcbmZvciBheCBpbiBheGVzOlxuICAgIGF4LnNldF94bGFiZWwoXHUwMDI3RmVhdHVyZSBpbmRleFx1MDAyNyk7IGF4LnNldF95bGFiZWwoXHUwMDI3SW1wb3J0YW5jZVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKVxucHJpbnQoXHUwMDI3UGVhcnNvbiByIChHaW5pIHZzIFBlcm0pOlx1MDAyNyxcbiAgICAgIHJvdW5kKG5wLmNvcnJjb2VmKGdpbmlfaW1wLCBwZXJtLmltcG9ydGFuY2VzX21lYW4pWzAsIDFdLCAzKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFeHRyYS1UcmVlcyDigJQgUmFuZG9tIFRocmVzaG9sZCBTZWxlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV4dHJlbWVseSBSYW5kb21pc2VkIFRyZWVzIChFeHRyYS1UcmVlcykgcHVzaCByYW5kb21pc2F0aW9uIGZ1cnRoZXI6IGluc3RlYWQgb2YgZmluZGluZyB0aGUgb3B0aW1hbCB0aHJlc2hvbGQgZm9yIGVhY2ggY2FuZGlkYXRlIGZlYXR1cmUsIHRoZXkgZHJhdyBhIHJhbmRvbSB0aHJlc2hvbGQgYW5kIHBpY2sgdGhlIGJlc3QgYW1vbmcgcmFuZG9tIChmZWF0dXJlLCB0aHJlc2hvbGQpIHBhaXJzLiBUaGlzIGVsaW1pbmF0ZXMgdGhlIHRocmVzaG9sZC1vcHRpbWlzYXRpb24gc3RlcCBlbnRpcmVseSwgbWFraW5nIGVhY2ggdHJlZSBtdWNoIGZhc3RlciB0byB0cmFpbi4gRXh0cmEtVHJlZXMgdHlwaWNhbGx5IG1hdGNoIFJhbmRvbSBGb3Jlc3QgYWNjdXJhY3kgb24gbW9zdCBkYXRhc2V0cyB3aGlsZSB0cmFpbmluZyBzaWduaWZpY2FudGx5IGZhc3Rlci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiZnJvbSBza2xlYXJuLmVuc2VtYmxlIGltcG9ydCBSYW5kb21Gb3Jlc3RDbGFzc2lmaWVyLCBFeHRyYVRyZWVzQ2xhc3NpZmllclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCBjcm9zc192YWxfc2NvcmVcbmltcG9ydCB0aW1lXG5cblgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKG5fc2FtcGxlcz01MDAwLCBuX2ZlYXR1cmVzPTIwLCBuX2luZm9ybWF0aXZlPTEwLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5fcmVkdW5kYW50PTUsIHJhbmRvbV9zdGF0ZT00MilcblxucmVzdWx0cyA9IHt9XG5mb3IgbmFtZSwgY2xmIGluIFtcbiAgICAoXHUwMDI3UmFuZG9tRm9yZXN0XHUwMDI3LCBSYW5kb21Gb3Jlc3RDbGFzc2lmaWVyKG5fZXN0aW1hdG9ycz0yMDAsIHJhbmRvbV9zdGF0ZT00MikpLFxuICAgIChcdTAwMjdFeHRyYVRyZWVzXHUwMDI3LCAgIEV4dHJhVHJlZXNDbGFzc2lmaWVyKG5fZXN0aW1hdG9ycz0yMDAsIHJhbmRvbV9zdGF0ZT00MikpXG5dOlxuICAgIHQwID0gdGltZS50aW1lKClcbiAgICBzY29yZXMgPSBjcm9zc192YWxfc2NvcmUoY2xmLCBYLCB5LCBjdj01LCBzY29yaW5nPVx1MDAyN2FjY3VyYWN5XHUwMDI3LCBuX2pvYnM9LTEpXG4gICAgZWxhcHNlZCA9IHRpbWUudGltZSgpIC0gdDBcbiAgICByZXN1bHRzW25hbWVdID0ge1x1MDAyN21lYW5cdTAwMjc6IHNjb3Jlcy5tZWFuKCksIFx1MDAyN3N0ZFx1MDAyNzogc2NvcmVzLnN0ZCgpLCBcdTAwMjd0aW1lXHUwMDI3OiBlbGFwc2VkfVxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2MxNH0gYWNjPXtzY29yZXMubWVhbigpOi40Zn3CsXtzY29yZXMuc3RkKCk6LjRmfSAgdGltZT17ZWxhcHNlZDouMmZ9c1x1MDAyNylcblxucmF0aW8gPSByZXN1bHRzW1x1MDAyN1JhbmRvbUZvcmVzdFx1MDAyN11bXHUwMDI3dGltZVx1MDAyN10gLyByZXN1bHRzW1x1MDAyN0V4dHJhVHJlZXNcdTAwMjddW1x1MDAyN3RpbWVcdTAwMjddXG5wcmludChmXHUwMDI3RXh0cmFUcmVlcyBpcyB7cmF0aW86LjFmfXggZmFzdGVyIHRoYW4gUmFuZG9tRm9yZXN0XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJpYXMtVmFyaWFuY2UgYW5kIFBhcmFsbGVsIFRyYWluaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVbmxpa2UgYm9vc3RpbmcgKHdoaWNoIHJlZHVjZXMgYmlhcyksIGJhZ2dpbmcgcHJpbWFyaWx5IHJlZHVjZXMgdmFyaWFuY2UuIEVhY2ggdHJlZSBpcyBhIGhpZ2gtdmFyaWFuY2UsIGxvdy1iaWFzIGVzdGltYXRvciAoZGVlcCwgdW5jb25zdHJhaW5lZCkuIEF2ZXJhZ2luZyBCIHN1Y2ggdHJlZXMgcmVkdWNlcyB2YXJpYW5jZSBieSBhIGZhY3RvciBhcHByb2FjaGluZyAxL0IgYXMgdHJlZSBjb3JyZWxhdGlvbiDPgSDihpIgMC4gQmlhcyBzdGF5cyB0aGUgc2FtZSBhcyBhIHNpbmdsZSB0cmVlLiBUaGlzIG1lYW5zIFJhbmRvbSBGb3Jlc3RzIHdvcmsgYmVzdCB3aGVuIGluZGl2aWR1YWwgdHJlZXMgYXJlIGFjY3VyYXRlIGJ1dCB1bnN0YWJsZSDigJQgd2hpY2ggaXMgZXhhY3RseSB3aHkgZGVlcCwgdW5jb25zdHJhaW5lZCB0cmVlcyBhcmUgcHJlZmVycmVkIGluc2lkZSBmb3Jlc3RzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRWFjaCB0cmVlIGlzIHRyYWluZWQgaW5kZXBlbmRlbnRseSDigJQgdHJpdmlhbGx5IHBhcmFsbGVsaXNhYmxlIHdpdGggbl9qb2JzPS0xIiwibl9lc3RpbWF0b3JzOiBtb3JlIHRyZWVzIGFsd2F5cyBoZWxwcyB1bnRpbCBPT0IgZXJyb3IgcGxhdGVhdXMgKH4yMDAtNTAwIHN1ZmZpY2llbnQpIiwibWF4X2ZlYXR1cmVzOiBrZXkgZGl2ZXJzaXR5IGxldmVyIOKAlCBzbWFsbGVyIHZhbHVlID0gbW9yZSBkZWNvcnJlbGF0aW9uIGJ1dCB3ZWFrZXIgdHJlZXMiLCJtYXhfZGVwdGg9Tm9uZSAoZGVmYXVsdCkgaXMgZmluZSBpbnNpZGUgZm9yZXN0cyDigJQgZGVwdGggaXMgcmVndWxhcmlzZWQgYnkgYXZlcmFnaW5nIiwibWluX3NhbXBsZXNfbGVhZj0zLTUgcHJldmVudHMgdmVyeSBzbWFsbCBsZWF2ZXMgd2l0aG91dCBoYXJtaW5nIG11Y2giLCJvb2Jfc2NvcmU9VHJ1ZSBnaXZlcyBmcmVlIHZhbGlkYXRpb24g4oCUIGNvbXBhcmUgd2l0aCBoZWxkLW91dCB0ZXN0IGFjY3VyYWN5Il19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiR2luaSBJbXBvcnRhbmNlIEJpYXMgaW4gSGlnaC1DYXJkaW5hbGl0eSBTZXR0aW5ncyIsImNvbnRlbnQiOiJPbiBkYXRhc2V0cyB3aXRoIG1peGVkIGZlYXR1cmUgdHlwZXMgKGNvbnRpbnVvdXMgKyBjYXRlZ29yaWNhbCB3aXRoIG1hbnkgY2F0ZWdvcmllcyksIEdpbmkgaW1wb3J0YW5jZSBzeXN0ZW1hdGljYWxseSBvdmVyZXN0aW1hdGVzIGNvbnRpbnVvdXMgZmVhdHVyZXMuIEFsd2F5cyBjcm9zcy1jaGVjayB3aXRoIHBlcm11dGF0aW9uIGltcG9ydGFuY2Ugb24gYSBoZWxkLW91dCBzZXQsIGVzcGVjaWFsbHkgYmVmb3JlIHJlcG9ydGluZyBmZWF0dXJlIHJhbmtpbmdzIHRvIHN0YWtlaG9sZGVycy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiUmFuZG9tIEZvcmVzdCB2cyBFeHRyYS1UcmVlcyBSdWxlIG9mIFRodW1iIiwiY29udGVudCI6IlN0YXJ0IHdpdGggUmFuZG9tRm9yZXN0LiBJZiB0cmFpbmluZyB0aW1lIGlzIGEgYm90dGxlbmVjayBhbmQgYWNjdXJhY3kgaXMgc2ltaWxhciBvbiB5b3VyIHZhbGlkYXRpb24gc2V0LCBzd2l0Y2ggdG8gRXh0cmFUcmVlc0NsYXNzaWZpZXIg4oCUIGl0IHRyYWlucyAyLTV4IGZhc3RlciB3aXRoIGlkZW50aWNhbCBhY2N1cmFjeSBvbiBtb3N0IHJlYWwtd29ybGQgZGF0YXNldHMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Random Forests — Bagging and Feature Subsampling

## Bagging — Bootstrap Aggregating

Bagging (bootstrap aggregating) trains B models on B bootstrap samples drawn with replacement from the training set. Each bootstrap sample contains ~63.2% unique examples (the rest are duplicates). Predictions are aggregated by majority vote (classification) or mean (regression). The variance of the average of B correlated estimators is σ²((1-ρ)/B + ρ) — when ρ=0 (perfectly uncorrelated), variance shrinks as 1/B; when ρ=1 (identical models), no reduction. Decorrelation is therefore essential.

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class BaggingClassifier:
    def __init__(self, n_estimators=50, max_depth=5, random_state=42):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.trees = []

    def fit(self, X, y):
        rng = np.random.RandomState(self.random_state)
        n = len(y)
        for i in range(self.n_estimators):
            idx = rng.choice(n, size=n, replace=True)   # bootstrap
            tree = DecisionTreeClassifier(max_depth=self.max_depth, random_state=i)
            tree.fit(X[idx], y[idx])
            self.trees.append(tree)
        return self

    def predict(self, X):
        preds = np.array([t.predict(X) for t in self.trees])
        return np.apply_along_axis(
            lambda x: np.bincount(x.astype(int)).argmax(), axis=0, arr=preds)

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
model = BaggingClassifier(n_estimators=100, max_depth=5).fit(X_tr, y_tr)
preds = model.predict(X_te)
print(f'Bagging accuracy: {(preds == y_te).mean():.4f}')
```

## Feature Subsampling and Decorrelation

Random Forests add a second source of randomness: at each split only a random subset of m features is considered (not all p). This decorrelates the trees even when one feature dominates, breaking the correlation ρ in the variance formula. Standard choices: m = √p for classification, m = p/3 for regression. Smaller m → more decorrelation → more variance reduction, but each individual tree is weaker (higher bias). The bias-variance sweet spot is typically √p.

> **Why 63.2% Unique Samples per Bootstrap**: With n draws from n samples with replacement, the probability a specific sample is never chosen is (1 − 1/n)^n → 1/e ≈ 36.8% as n → ∞. So each bootstrap sample contains roughly 63.2% unique training examples, leaving ~36.8% as the out-of-bag (OOB) set for free validation.

## Out-of-Bag Error and sklearn Implementation

The ~36.8% of samples not included in each tree's bootstrap sample form its out-of-bag set. Each sample's OOB prediction is the aggregate of trees that did not train on it. OOB error is a nearly unbiased estimate of test error — essentially a free cross-validation — valid when the forest is large enough (≥200 trees). Enable with oob_score=True.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(
    n_estimators=300,
    max_features='sqrt',       # sqrt(p) features per split
    max_depth=None,
    min_samples_leaf=3,
    oob_score=True,            # free validation from ~36.8% OOB samples
    n_jobs=-1,
    random_state=42
)
rf.fit(X_tr, y_tr)

print(f'OOB score:      {rf.oob_score_:.4f}')
print(f'Test score:     {rf.score(X_te, y_te):.4f}')
print(f'Features/split: {rf.max_features_} of {X.shape[1]}')
```

## Feature Importance — Gini vs Permutation

Gini importance (MDI) sums impurity reductions weighted by sample fraction across all trees. It is fast but biased toward high-cardinality and continuous features. Permutation importance measures the drop in model accuracy when a feature's values are randomly shuffled on the test set — it is model-agnostic and unbiased. Run k=10-30 repetitions for stable estimates. SHAP gives local explanations on top of global importance.

| Method | Bias (cardinality) | Correlated Features | Cost | Global / Local |
| --- | --- | --- | --- | --- |
| Gini / MDI | Yes — high-cardinality inflated | Inflates both features | Negligible (computed during training) | Global only |
| Permutation | None | Splits importance between correlated | Moderate (k × n predictions) | Global only |
| SHAP | None | Distributes fairly | High (O(TLD²) TreeSHAP) | Both global and local |
| LIME | None | Unstable | Moderate | Local only |

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Correlated features highlight MDI bias
X, y = make_classification(n_samples=1000, n_features=10, n_informative=3,
                            n_redundant=5, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_tr, y_tr)

gini_imp = rf.feature_importances_
perm = permutation_importance(rf, X_te, y_te, n_repeats=15, random_state=42)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].bar(range(10), gini_imp); axes[0].set_title('Gini (MDI) Importance')
axes[1].bar(range(10), perm.importances_mean); axes[1].set_title('Permutation Importance')
for ax in axes:
    ax.set_xlabel('Feature index'); ax.set_ylabel('Importance')
plt.tight_layout(); plt.show()
print('Pearson r (Gini vs Perm):',
      round(np.corrcoef(gini_imp, perm.importances_mean)[0, 1], 3))
```

## Extra-Trees — Random Threshold Selection

Extremely Randomised Trees (Extra-Trees) push randomisation further: instead of finding the optimal threshold for each candidate feature, they draw a random threshold and pick the best among random (feature, threshold) pairs. This eliminates the threshold-optimisation step entirely, making each tree much faster to train. Extra-Trees typically match Random Forest accuracy on most datasets while training significantly faster.

```python
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
import time

X, y = make_classification(n_samples=5000, n_features=20, n_informative=10,
                            n_redundant=5, random_state=42)

results = {}
for name, clf in [
    ('RandomForest', RandomForestClassifier(n_estimators=200, random_state=42)),
    ('ExtraTrees',   ExtraTreesClassifier(n_estimators=200, random_state=42))
]:
    t0 = time.time()
    scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy', n_jobs=-1)
    elapsed = time.time() - t0
    results[name] = {'mean': scores.mean(), 'std': scores.std(), 'time': elapsed}
    print(f'{name:<14} acc={scores.mean():.4f}±{scores.std():.4f}  time={elapsed:.2f}s')

ratio = results['RandomForest']['time'] / results['ExtraTrees']['time']
print(f'ExtraTrees is {ratio:.1f}x faster than RandomForest')
```

## Bias-Variance and Parallel Training

Unlike boosting (which reduces bias), bagging primarily reduces variance. Each tree is a high-variance, low-bias estimator (deep, unconstrained). Averaging B such trees reduces variance by a factor approaching 1/B as tree correlation ρ → 0. Bias stays the same as a single tree. This means Random Forests work best when individual trees are accurate but unstable — which is exactly why deep, unconstrained trees are preferred inside forests.

- Each tree is trained independently — trivially parallelisable with n_jobs=-1
- n_estimators: more trees always helps until OOB error plateaus (~200-500 sufficient)
- max_features: key diversity lever — smaller value = more decorrelation but weaker trees
- max_depth=None (default) is fine inside forests — depth is regularised by averaging
- min_samples_leaf=3-5 prevents very small leaves without harming much
- oob_score=True gives free validation — compare with held-out test accuracy

> **Gini Importance Bias in High-Cardinality Settings**: On datasets with mixed feature types (continuous + categorical with many categories), Gini importance systematically overestimates continuous features. Always cross-check with permutation importance on a held-out set, especially before reporting feature rankings to stakeholders.

> **Random Forest vs Extra-Trees Rule of Thumb**: Start with RandomForest. If training time is a bottleneck and accuracy is similar on your validation set, switch to ExtraTreesClassifier — it trains 2-5x faster with identical accuracy on most real-world datasets.

---

