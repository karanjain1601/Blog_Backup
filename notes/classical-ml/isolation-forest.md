---
title: "Isolation Forest — Path Length and Random Partitioning"
slug: "isolation-forest"
description: "Understand Isolation Forest's path-length anomaly scoring, build an isolation tree from scratch, compare standard vs extended variants, and see why anomalies are isolated in fewer steps."
tags: ["anomaly-detection", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSXNvbGF0aW9uIEZvcmVzdCBleHBsb2l0cyBhIGtleSBpbnNpZ2h0OiBhbm9tYWxpZXMgYXJlIGZldyBhbmQgZGlmZmVyZW50IOKAlCB0aGV5IGFyZSBlYXNpZXIgdG8gaXNvbGF0ZSB0aGFuIG5vcm1hbCBwb2ludHMuIEJ5IGJ1aWxkaW5nIGFuIGVuc2VtYmxlIG9mIHJhbmRvbSBiaW5hcnkgdHJlZXMgdGhhdCByZWN1cnNpdmVseSBwYXJ0aXRpb24gdGhlIGZlYXR1cmUgc3BhY2UsIGFub21hbGllcyByZXF1aXJlIGZld2VyIHNwbGl0cyB0byBpc29sYXRlIChzaG9ydGVyIHBhdGggbGVuZ3RoKSB3aGlsZSBub3JtYWwgcG9pbnRzIGNsdXN0ZXIgdG9nZXRoZXIgYW5kIG5lZWQgbWFueSBzcGxpdHMuIE5vIGRpc3RhbmNlIG9yIGRlbnNpdHkgY29tcHV0YXRpb24gaXMgcmVxdWlyZWQsIG1ha2luZyBpdCBlZmZpY2llbnQgaW4gaGlnaCBkaW1lbnNpb25zIGFuZCB3aXRoIGxhcmdlIGRhdGFzZXRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Iklzb2xhdGlvbiBUcmVlIEFsZ29yaXRobSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQW4gaXNvbGF0aW9uIHRyZWUgaXMgYnVpbHQgYnk6ICgxKSByYW5kb21seSBzZWxlY3RpbmcgYSBmZWF0dXJlLCAoMikgcmFuZG9tbHkgc2VsZWN0aW5nIGEgc3BsaXQgdmFsdWUgYmV0d2VlbiB0aGUgZmVhdHVyZVx1MDAyN3MgbWluIGFuZCBtYXgsICgzKSBwYXJ0aXRpb25pbmcgdGhlIGRhdGEgYW5kIHJlY3Vyc2luZyBvbiBlYWNoIGJyYW5jaCB1bnRpbCBkZXB0aCBsaW1pdCBvciBhIHNpbmdsZSBwb2ludCByZW1haW5zLiBUaGUgcGF0aCBsZW5ndGggZm9yIGEgcG9pbnQgeCBpcyB0aGUgbnVtYmVyIG9mIHNwbGl0cyByZXF1aXJlZCB0byBpc29sYXRlIGl0LiBUaGUgZXhwZWN0ZWQgcGF0aCBsZW5ndGggZm9yIGEgc3VidHJlZSBvZiBzaXplIG4gaXMgYyhuKSA9IDJIKG7iiJIxKSDiiJIgMihu4oiSMSkvbiB3aGVyZSBIIGlzIHRoZSBoYXJtb25pYyBudW1iZXIuIFVzaW5nIGMobikgbm9ybWFsaXNlcyBmb3IgZGlmZmVyZW50IHN1YnRyZWUgc2l6ZXMuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJzKHgsIG4pID0gMl57LVxcZnJhY3tFW2goeCldfXtjKG4pfX0sIFxccXVhZCBjKG4pID0gMkgobi0xKSAtIFxcZnJhY3syKG4tMSl9e259LCBcXHF1YWQgSChpKSBcXGFwcHJveCBcXGxuIGkgKyAwLjU3NzIifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIElzb2xhdGlvblRyZWU6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG1heF9kZXB0aD04KTpcbiAgICAgICAgc2VsZi5tYXhfZGVwdGggPSBtYXhfZGVwdGhcblxuICAgIGRlZiBmaXQoc2VsZiwgWCwgZGVwdGg9MCk6XG4gICAgICAgIG4sIGQgPSBYLnNoYXBlXG4gICAgICAgIGlmIGRlcHRoIFx1MDAzZT0gc2VsZi5tYXhfZGVwdGggb3IgbiBcdTAwM2M9IDE6XG4gICAgICAgICAgICBzZWxmLmlzX2xlYWYsIHNlbGYuc2l6ZSA9IFRydWUsIG5cbiAgICAgICAgICAgIHJldHVybiBzZWxmXG4gICAgICAgIHNlbGYuaXNfbGVhZiA9IEZhbHNlXG4gICAgICAgIHNlbGYuZmVhdCA9IG5wLnJhbmRvbS5yYW5kaW50KGQpXG4gICAgICAgIGNvbCA9IFhbOiwgc2VsZi5mZWF0XVxuICAgICAgICBsbywgaGkgPSBjb2wubWluKCksIGNvbC5tYXgoKVxuICAgICAgICBpZiBsbyA9PSBoaTpcbiAgICAgICAgICAgIHNlbGYuaXNfbGVhZiwgc2VsZi5zaXplID0gVHJ1ZSwgblxuICAgICAgICAgICAgcmV0dXJuIHNlbGZcbiAgICAgICAgc2VsZi5zcGxpdCA9IG5wLnJhbmRvbS51bmlmb3JtKGxvLCBoaSlcbiAgICAgICAgbWFzayA9IGNvbCBcdTAwM2Mgc2VsZi5zcGxpdFxuICAgICAgICBzZWxmLmxlZnQgID0gSXNvbGF0aW9uVHJlZShzZWxmLm1heF9kZXB0aCkuZml0KFhbbWFza10sICBkZXB0aCsxKVxuICAgICAgICBzZWxmLnJpZ2h0ID0gSXNvbGF0aW9uVHJlZShzZWxmLm1heF9kZXB0aCkuZml0KFhbfm1hc2tdLCBkZXB0aCsxKVxuICAgICAgICByZXR1cm4gc2VsZlxuXG4gICAgZGVmIF9jKHNlbGYsIG4pOlxuICAgICAgICBpZiBuIFx1MDAzYz0gMTogcmV0dXJuIDBcbiAgICAgICAgcmV0dXJuIDIqKG5wLmxvZyhuLTEpKzAuNTc3MjE1NjY0OSkgLSAyKihuLTEpL25cblxuICAgIGRlZiBwYXRoX2xlbmd0aChzZWxmLCB4LCBkZXB0aD0wKTpcbiAgICAgICAgaWYgc2VsZi5pc19sZWFmOlxuICAgICAgICAgICAgcmV0dXJuIGRlcHRoICsgc2VsZi5fYyhzZWxmLnNpemUpXG4gICAgICAgIHJldHVybiAoc2VsZi5sZWZ0IGlmIHhbc2VsZi5mZWF0XSBcdTAwM2Mgc2VsZi5zcGxpdCBlbHNlIHNlbGYucmlnaHQpLnBhdGhfbGVuZ3RoKHgsIGRlcHRoKzEpXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWF90ciA9IG5wLnJhbmRvbS5ub3JtYWwoMCwgMSwgKDEwMCwgMikpXG5YX291dCA9IG5wLmFycmF5KFtbNS4wLCA1LjBdLCBbLTUuMCwgNC4wXV0pXG50cmVlID0gSXNvbGF0aW9uVHJlZShtYXhfZGVwdGg9OCkuZml0KFhfdHIpXG5jbiA9IHRyZWUuX2MobGVuKFhfdHIpKVxuc2NvcmVzX24gPSBbMioqKC10cmVlLnBhdGhfbGVuZ3RoKHgpL2NuKSBmb3IgeCBpbiBYX3RyXVxuc2NvcmVzX2EgPSBbMioqKC10cmVlLnBhdGhfbGVuZ3RoKHgpL2NuKSBmb3IgeCBpbiBYX291dF1cbnByaW50KGZcdTAwMjdOb3JtYWwgYXZnIHNjb3JlOiB7bnAubWVhbihzY29yZXNfbik6LjNmfSAoc2hvdWxkIGJlIH4wLjUpXHUwMDI3KVxucHJpbnQoZlx1MDAyN0Fub21hbHkgc2NvcmVzOiAgIHtbcm91bmQocywzKSBmb3IgcyBpbiBzY29yZXNfYV19IChzaG91bGQgYmUgfjEuMClcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50Ijoic2tsZWFybiBJc29sYXRpb25Gb3Jlc3QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBza2xlYXJuIGltcGxlbWVudGF0aW9uIHVzZXMgbl9lc3RpbWF0b3JzIHRyZWVzIChkZWZhdWx0IDEwMCksIHN1Yi1zYW1wbGluZyAyNTYgcG9pbnRzIHBlciB0cmVlLiBTdWItc2FtcGxpbmcgcmVkdWNlcyB2YXJpYW5jZSBhbmQgbGltaXRzIHRoZSBkZXB0aCBuZWVkZWQg4oCUIHdpdGggb25seSAyNTYgcG9pbnRzLCBhbm9tYWxpZXMgYXJlIGFsbW9zdCBhbHdheXMgaXNvbGF0ZWQgYmVmb3JlIG5vcm1hbCBwb2ludHMuIFRoZSBjb250YW1pbmF0aW9uIHBhcmFtZXRlciBzZXRzIHRoZSB0aHJlc2hvbGQgZm9yIHByZWRpY3QoKTogaXQgZGV0ZXJtaW5lcyB3aGF0IGZyYWN0aW9uIG9mIHRyYWluaW5nIGRhdGEgaXMgbGFiZWxsZWQgYW5vbWFseS4gVGhlIHNjb3JlX3NhbXBsZXMoKSBtZXRob2QgcmV0dXJucyB0aGUgcmF3IGFub21hbHkgc2NvcmUgKG1vcmUgbmVnYXRpdmUgPSBtb3JlIGFub21hbG91cykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmVuc2VtYmxlIGltcG9ydCBJc29sYXRpb25Gb3Jlc3RcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YX25vcm1hbCAgPSBucC5yYW5kb20ubm9ybWFsKDAsIDEsICgzMDAsIDIpKVxuWF9hbm9tYWx5ID0gbnAucmFuZG9tLnVuaWZvcm0oLTUsIDUsICgyMCwgMikpXG5YID0gbnAudnN0YWNrKFtYX25vcm1hbCwgWF9hbm9tYWx5XSlcblxuY2xmID0gSXNvbGF0aW9uRm9yZXN0KG5fZXN0aW1hdG9ycz0xMDAsIGNvbnRhbWluYXRpb249MC4wNiwgcmFuZG9tX3N0YXRlPTQyKVxuY2xmLmZpdChYKVxuc2NvcmVzID0gY2xmLnNjb3JlX3NhbXBsZXMoWClcbnByZWRzICA9IGNsZi5wcmVkaWN0KFgpXG5cbnByaW50KGZcdTAwMjdBbm9tYWxpZXMgZGV0ZWN0ZWQ6IHsocHJlZHM9PS0xKS5zdW0oKX1cdTAwMjcpXG5wcmludChmXHUwMDI3U2NvcmUgcmFuZ2U6IFt7c2NvcmVzLm1pbigpOi4zZn0sIHtzY29yZXMubWF4KCk6LjNmfV1cdTAwMjcpXG5cbnh4LCB5eSA9IG5wLm1lc2hncmlkKG5wLmxpbnNwYWNlKC02LCA2LCAxMDApLCBucC5saW5zcGFjZSgtNiwgNiwgMTAwKSlcblogPSBjbGYuc2NvcmVfc2FtcGxlcyhucC5jX1t4eC5yYXZlbCgpLCB5eS5yYXZlbCgpXSkucmVzaGFwZSh4eC5zaGFwZSlcbnBsdC5jb250b3VyZih4eCwgeXksIFosIGxldmVscz0yMCwgY21hcD1cdTAwMjdSZFlsR25cdTAwMjcpXG5wbHQuc2NhdHRlcihYW3ByZWRzPT0xLDBdLCAgWFtwcmVkcz09MSwxXSwgIGM9XHUwMDI3c3RlZWxibHVlXHUwMDI3LCBzPTEwLCBsYWJlbD1cdTAwMjdOb3JtYWxcdTAwMjcpXG5wbHQuc2NhdHRlcihYW3ByZWRzPT0tMSwwXSwgWFtwcmVkcz09LTEsMV0sIGM9XHUwMDI3cmVkXHUwMDI3LCBzPTQwLCBtYXJrZXI9XHUwMDI3eFx1MDAyNywgbGFiZWw9XHUwMDI3QW5vbWFseVx1MDAyNylcbnBsdC5sZWdlbmQoKVxucGx0LnRpdGxlKFx1MDAyN0lzb2xhdGlvbiBGb3Jlc3Qg4oCUIFNjb3JlIENvbnRvdXJzXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdpc29sYXRpb25fZm9yZXN0LnBuZ1x1MDAyNywgZHBpPTEwMCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFeHRlbmRlZCBJc29sYXRpb24gRm9yZXN0IOKAlCBSb3RhdGlvbmFsIEludmFyaWFuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIElzb2xhdGlvbiBGb3Jlc3QgdXNlcyBheGlzLWFsaWduZWQgc3BsaXRzLCB3aGljaCBjcmVhdGVzIGdob3N0IGFub21hbGllcyBuZWFyIHNwbGl0IGJvdW5kYXJpZXMgYWxvbmcgdGhlIGF4ZXMuIEV4dGVuZGVkIElzb2xhdGlvbiBGb3Jlc3QgKEVJRikgdXNlcyByYW5kb20gaHlwZXJwbGFuZSBzcGxpdHMg4oCUIGl0IHNlbGVjdHMgYSByYW5kb20gbm9ybWFsIHZlY3RvciBuIGFuZCBhIHJhbmRvbSBpbnRlcmNlcHQgcCwgdGhlbiBzcGxpdHMgb24gbuG1gHgg4omkIG7htYBwLiBUaGlzIGVsaW1pbmF0ZXMgdGhlIGF4aXMtYWxpZ25lZCBiaWFzIGFuZCB3b3JrcyBiZXR0ZXIgb24gZGF0YSB3aXRoIGRpYWdvbmFsIGNvcnJlbGF0aW9uIHN0cnVjdHVyZSBvciByb3RhdGVkIGNsdXN0ZXJzLiBFSUYgcmVxdWlyZXMgdGhlIGVpZiBwYWNrYWdlIG9yIGEgY3VzdG9tIGltcGxlbWVudGF0aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5lbnNlbWJsZSBpbXBvcnQgSXNvbGF0aW9uRm9yZXN0XG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYXZlcmFnZV9wcmVjaXNpb25fc2NvcmVcblxubnAucmFuZG9tLnNlZWQoNDIpXG5jb3YgPSBbWzIuMCwgMS44XSwgWzEuOCwgMi4wXV1cblhfbm9ybWFsICA9IG5wLnJhbmRvbS5tdWx0aXZhcmlhdGVfbm9ybWFsKFswLDBdLCBjb3YsIDQwMClcblhfYW5vbWFseSA9IG5wLnJhbmRvbS51bmlmb3JtKC02LCA2LCAoMjAsIDIpKVxuWCA9IG5wLnZzdGFjayhbWF9ub3JtYWwsIFhfYW5vbWFseV0pXG55X3RydWUgPSBucC5hcnJheShbMF0qNDAwICsgWzFdKjIwKVxuXG5zdGRfaWYgPSBJc29sYXRpb25Gb3Jlc3Qobl9lc3RpbWF0b3JzPTIwMCwgY29udGFtaW5hdGlvbj0wLjA0NywgcmFuZG9tX3N0YXRlPTQyKVxuc3RkX3ByZWRzID0gc3RkX2lmLmZpdF9wcmVkaWN0KFgpXG5zdGRfc2NvcmVzID0gLXN0ZF9pZi5zY29yZV9zYW1wbGVzKFgpXG5zdGRfYXAgPSBhdmVyYWdlX3ByZWNpc2lvbl9zY29yZSh5X3RydWUsIHN0ZF9zY29yZXMpXG5cbiMgQXBwcm94aW1hdGUgRUlGIHZpYSByYW5kb20gcHJvamVjdGlvbnNcbnJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZSg0MilcbnByb2pfc2NvcmVzID0gbnAuemVyb3MobGVuKFgpKVxuZm9yIF8gaW4gcmFuZ2UoMjAwKTpcbiAgICBuX3ZlYyA9IHJuZy5yYW5kbigyKVxuICAgIG5fdmVjIC89IG5wLmxpbmFsZy5ub3JtKG5fdmVjKVxuICAgIFgxZCA9IChYIEAgbl92ZWMpLnJlc2hhcGUoLTEsIDEpXG4gICAgY2xmMWQgPSBJc29sYXRpb25Gb3Jlc3Qobl9lc3RpbWF0b3JzPTEsIGNvbnRhbWluYXRpb249MC4wNDcsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcmFuZG9tX3N0YXRlPXJuZy5yYW5kaW50KDEwMDAwKSkuZml0KFgxZClcbiAgICBwcm9qX3Njb3JlcyArPSAtY2xmMWQuc2NvcmVfc2FtcGxlcyhYMWQpXG5wcm9qX2FwID0gYXZlcmFnZV9wcmVjaXNpb25fc2NvcmUoeV90cnVlLCBwcm9qX3Njb3JlcylcblxucHJpbnQoZlx1MDAyN1N0YW5kYXJkIElGICBBUDoge3N0ZF9hcDouM2Z9IChheGlzLWFsaWduZWQgc3BsaXRzLCBiaWFzIG9uIHJvdGF0ZWQgZGF0YSlcdTAwMjcpXG5wcmludChmXHUwMDI3UHJvamVjdGVkIElGIEFQOiB7cHJval9hcDouM2Z9IChyYW5kb20gaHlwZXJwbGFuZXMgcmVkdWNlIGF4aXMgYmlhcylcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQW5vbWFseSBTY29yZSBEaXN0cmlidXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRyYWluaW5nIHRoZSBtb2RlbCBvbiBub3JtYWwgZGF0YSBvbmx5ICh1bnN1cGVydmlzZWQgbm92ZWx0eSBkZXRlY3Rpb24pIGFuZCBzY29yaW5nIGJvdGggbm9ybWFsIGFuZCBhbm9tYWxvdXMgdGVzdCBwb2ludHMgcmV2ZWFscyB0aGUgc2NvcmUgc2VwYXJhdGlvbi4gQW5vbWFsaWVzIGNsdXN0ZXIgbmVhciBzY29yZSDiiJIwLjUgYW5kIG5vcm1hbCBwb2ludHMgY2x1c3RlciBuZWFyIOKIkjAuMSB0byAwIChza2xlYXJuIGNvbnZlbnRpb246IG1vcmUgbmVnYXRpdmUgPSBtb3JlIGFub21hbG91cykuIFRoZSBvdmVybGFwIGJldHdlZW4gdGhlIGRpc3RyaWJ1dGlvbnMgZGV0ZXJtaW5lcyB0aGUgYWNoaWV2YWJsZSBwcmVjaXNpb24tcmVjYWxsIHRyYWRlb2ZmIGF0IGFueSBnaXZlbiB0aHJlc2hvbGQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmVuc2VtYmxlIGltcG9ydCBJc29sYXRpb25Gb3Jlc3RcblxubnAucmFuZG9tLnNlZWQoMClcblhfdHJhaW4gICA9IG5wLnJhbmRvbS5ub3JtYWwoMCwgMSwgKDUwMCwgNSkpXG5YX3Rlc3RfbiAgPSBucC5yYW5kb20ubm9ybWFsKDAsIDEsICgyMDAsIDUpKVxuWF90ZXN0X2EgID0gbnAucmFuZG9tLnVuaWZvcm0oLTQsIDQsICg1MCwgNSkpXG5cbmNsZiA9IElzb2xhdGlvbkZvcmVzdChuX2VzdGltYXRvcnM9MTAwLCByYW5kb21fc3RhdGU9MClcbmNsZi5maXQoWF90cmFpbilcbnNjb3Jlc19uID0gY2xmLnNjb3JlX3NhbXBsZXMoWF90ZXN0X24pXG5zY29yZXNfYSA9IGNsZi5zY29yZV9zYW1wbGVzKFhfdGVzdF9hKVxuXG5wcmludChmXHUwMDI3Tm9ybWFsICBzY29yZXM6IG1lYW49e3Njb3Jlc19uLm1lYW4oKTouM2Z9ICBzdGQ9e3Njb3Jlc19uLnN0ZCgpOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3QW5vbWFseSBzY29yZXM6IG1lYW49e3Njb3Jlc19hLm1lYW4oKTouM2Z9ICBzdGQ9e3Njb3Jlc19hLnN0ZCgpOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3VGhyZXNob2xkIHVzZWQ6IHtjbGYudGhyZXNob2xkXzouM2Z9XHUwMDI3KVxuXG5maWcsIGF4ID0gcGx0LnN1YnBsb3RzKGZpZ3NpemU9KDksIDQpKVxuYXguaGlzdChzY29yZXNfbiwgYmlucz0zMCwgYWxwaGE9MC42LCBsYWJlbD1cdTAwMjdOb3JtYWwgdGVzdFx1MDAyNywgIGNvbG9yPVx1MDAyN3N0ZWVsYmx1ZVx1MDAyNylcbmF4Lmhpc3Qoc2NvcmVzX2EsIGJpbnM9MjAsIGFscGhhPTAuNiwgbGFiZWw9XHUwMDI3QW5vbWFseSB0ZXN0XHUwMDI3LCBjb2xvcj1cdTAwMjdjcmltc29uXHUwMDI3KVxuYXguYXh2bGluZShjbGYudGhyZXNob2xkXywgY29sb3I9XHUwMDI3YmxhY2tcdTAwMjcsIGxpbmVzdHlsZT1cdTAwMjctLVx1MDAyNywgbGluZXdpZHRoPTIsIGxhYmVsPVx1MDAyN1RocmVzaG9sZFx1MDAyNylcbmF4LnNldF94bGFiZWwoXHUwMDI3SXNvbGF0aW9uIEZvcmVzdCBTY29yZVx1MDAyNylcbmF4LmxlZ2VuZCgpXG5heC5zZXRfdGl0bGUoXHUwMDI3U2NvcmUgRGlzdHJpYnV0aW9uOiBOb3JtYWwgdnMgQW5vbWFseSAoNS1kaW0pXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdpZl9zY29yZV9kaXN0LnBuZ1x1MDAyNywgZHBpPTEwMCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpc29uIHdpdGggT3RoZXIgRGV0ZWN0b3JzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkFzc3VtcHRpb24iLCJIaWdoLWRpbSIsIlNwZWVkIiwiSW50ZXJwcmV0YWJsZSIsIkNvbnRhbWluYXRpb24gcGFyYW0iXSwicm93cyI6W1siSXNvbGF0aW9uIEZvcmVzdCIsIkFub21hbGllcyBhcmUgZmV3IGFuZCBkaWZmZXJlbnQiLCJFeGNlbGxlbnQiLCJPKG4gbG9nIG4pIiwiUGFydGlhbGx5IChwYXRoIGxlbmd0aCkiLCJZZXMg4oCUIGNvbnRhbWluYXRpb24iXSxbIkxPRiIsIkxvY2FsIGRlbnNpdHkgY29tcGFyaXNvbiIsIlBvb3IgKGRpc3RhbmNlcyBjb252ZXJnZSkiLCJPKG7CsiBrKSIsIlllcyAoTE9GIHNjb3JlIHJhdGlvKSIsIkltcGxpY2l0IHZpYSBrIl0sWyJPbmUtQ2xhc3MgU1ZNIiwiTm9ybWFsIGRhdGEgb24gb25lIHNpZGUgb2YgaHlwZXJwbGFuZSIsIlBvb3IgKGtlcm5lbCBjb3N0KSIsIk8obsKyIFNWKSIsIkxvdyAoa2VybmVsIGJvdW5kYXJ5KSIsIlllcyDigJQgbnUiXSxbIkF1dG9lbmNvZGVyIiwiQW5vbWFsaWVzIG5vdCBvbiBub3JtYWwgbWFuaWZvbGQiLCJHb29kIiwiRGVwZW5kcyBvbiBhcmNoIiwiTG93IiwiVmlhIHRocmVzaG9sZCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEd1aWRhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTZXQgbl9lc3RpbWF0b3JzPTEwMCBhcyBhIGJhc2VsaW5lOyAyMDAtMzAwIGlmIHByZWNpc2lvbiBtYXR0ZXJzLiBTdWItc2FtcGxlIHNpemUgb2YgMjU2IChtYXhfc2FtcGxlcz0yNTYpIHdvcmtzIHdlbGwgZm9yIG1vc3QgZGF0YXNldHMg4oCUIGluY3JlYXNpbmcgaXQgcmFyZWx5IGhlbHBzIGFuZCBzbG93cyB0cmFpbmluZy4gV2hlbiBjb250YW1pbmF0aW9uIGlzIHVua25vd24sIHNldCBjb250YW1pbmF0aW9uPVx1MDAyN2F1dG9cdTAwMjcgYW5kIHVzZSBzY29yZV9zYW1wbGVzKCkgd2l0aCBhIHRocmVzaG9sZCBmcm9tIGEgaGVsZC1vdXQgdmFsaWRhdGlvbiBzZXQuIEZvciBzdHJlYW1pbmcgYW5vbWFseSBkZXRlY3Rpb24sIHRyYWluIG9uIGEgcm9sbGluZyB3aW5kb3cgYW5kIHJlLWZpdCBwZXJpb2RpY2FsbHkuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IldoZW4gdG8gUHJlZmVyIElzb2xhdGlvbiBGb3Jlc3QiLCJjb250ZW50IjoiSXNvbGF0aW9uIEZvcmVzdCBpcyB0aGUgcmVjb21tZW5kZWQgZmlyc3QgY2hvaWNlIGZvciBhbm9tYWx5IGRldGVjdGlvbiBpbiBoaWdoLWRpbWVuc2lvbmFsIHRhYnVsYXIgZGF0YSAoZCBcdTAwM2UgMTApLCB3aGVuIHRoZSBkYXRhc2V0IGlzIGxhcmdlIChuIFx1MDAzZSAxMCwwMDApLCBvciB3aGVuIG5vIGFzc3VtcHRpb24gYWJvdXQgdGhlIG5vcm1hbCBkaXN0cmlidXRpb24gY2FuIGJlIG1hZGUuIEl0cyBPKG4gbG9nIG4pIGNvbXBsZXhpdHkgYW5kIGxhY2sgb2YgcGFpcndpc2UgZGlzdGFuY2UgY29tcHV0YXRpb24gbWFrZSBpdCBmYXIgZmFzdGVyIHRoYW4gTE9GIG9yIE9uZS1DbGFzcyBTVk0gYXQgc2NhbGUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdWItc2FtcGxpbmcgaXMgYSBrZXkgZGVzaWduIGNob2ljZTogZWFjaCB0cmVlIGlzIGJ1aWx0IG9uIGEgcmFuZG9tIHNhbXBsZSBvZiBtYXhfc2FtcGxlcyBwb2ludHMgKGRlZmF1bHQgMjU2KS4gQmVjYXVzZSBhbm9tYWxpZXMgYXJlIHJhcmUgYW5kIGlzb2xhdGVkLCAyNTYgcG9pbnRzIGlzIGFsbW9zdCBhbHdheXMgZW5vdWdoIHRvIGlzb2xhdGUgdGhlbSBuZWFyIHRoZSByb290LiBJbmNyZWFzaW5nIG1heF9zYW1wbGVzIGJleW9uZCAyNTYgZG9lcyBub3Qgc3lzdGVtYXRpY2FsbHkgaW1wcm92ZSBkZXRlY3Rpb24gYW5kIHNpZ25pZmljYW50bHkgc2xvd3MgdHJhaW5pbmcuIElmIHRoZSBkYXRhc2V0IGlzIHZlcnkgc21hbGwgKG4gXHUwMDNjIDI1NiksIHNldCBtYXhfc2FtcGxlcz1uIHRvIHVzZSBhbGwgZGF0YS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVzZSBtYXhfc2FtcGxlcz0yNTYgKGRlZmF1bHQpIOKAlCBpbmNyZWFzaW5nIGl0IHJhcmVseSBpbXByb3ZlcyByZXN1bHRzIiwiU2V0IGNvbnRhbWluYXRpb24gdG8gdGhlIGV4cGVjdGVkIGFub21hbHkgZnJhY3Rpb24sIG9yIHR1bmUgb24gYSBsYWJlbGxlZCB2YWxpZGF0aW9uIHNldCIsIlNjb3JlIHdpdGggc2NvcmVfc2FtcGxlcygpIGZvciBjb250aW51b3VzIHJhbmtpbmcgcmF0aGVyIHRoYW4gYmluYXJ5IHByZWRpY3QoKSIsIkNvbnNpZGVyIEV4dGVuZGVkIElzb2xhdGlvbiBGb3Jlc3Qgd2hlbiBkYXRhIGhhcyBzdHJvbmcgZGlhZ29uYWwgY29ycmVsYXRpb24gc3RydWN0dXJlIiwiRm9yIG9ubGluZS9zdHJlYW1pbmcgZGF0YSwgZml0IGEgbmV3IG1vZGVsIHBlcmlvZGljYWxseSBvbiBhIHJlY2VudCB3aW5kb3ciXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUbyBldmFsdWF0ZSBwZXJmb3JtYW5jZSB3aXRob3V0IGxhYmVsbGVkIGRhdGEsIHVzZSB0aGUgYW5vbWFseSBzY29yZSBkaXN0cmlidXRpb246IGEgd2VsbC10cmFpbmVkIElzb2xhdGlvbiBGb3Jlc3Qgc2hvdWxkIHNob3cgYSBjbGVhciBiaW1vZGFsIGRpc3RyaWJ1dGlvbiBvZiBzY29yZXMgd2hlbiBhbm9tYWxpZXMgYXJlIHByZXNlbnQg4oCUIGEgZGVuc2UgY2x1c3RlciBuZWFyIDAgKG5vcm1hbCkgYW5kIGEgc3BhcnNlIGNsdXN0ZXIgbmVhciDiiJIwLjUgYW5kIGJlbG93IChhbm9tYWxvdXMpLiBJZiB0aGUgZGlzdHJpYnV0aW9uIGlzIHVuaW1vZGFsLCBlaXRoZXIgY29udGFtaW5hdGlvbiBpcyB2ZXJ5IGxvdyBvciB0aGUgYW5vbWFsaWVzIGFyZSBub3QgaXNvbGF0ZWQgYnkgcmFuZG9tIHBhcnRpdGlvbmluZy4ifV0="
---
# Isolation Forest — Path Length and Random Partitioning

Isolation Forest exploits a key insight: anomalies are few and different — they are easier to isolate than normal points. By building an ensemble of random binary trees that recursively partition the feature space, anomalies require fewer splits to isolate (shorter path length) while normal points cluster together and need many splits. No distance or density computation is required, making it efficient in high dimensions and with large datasets.

## Isolation Tree Algorithm

An isolation tree is built by: (1) randomly selecting a feature, (2) randomly selecting a split value between the feature's min and max, (3) partitioning the data and recursing on each branch until depth limit or a single point remains. The path length for a point x is the number of splits required to isolate it. The expected path length for a subtree of size n is c(n) = 2H(n−1) − 2(n−1)/n where H is the harmonic number. Using c(n) normalises for different subtree sizes.

$$s(x, n) = 2^{-\frac{E[h(x)]}{c(n)}}, \quad c(n) = 2H(n-1) - \frac{2(n-1)}{n}, \quad H(i) \approx \ln i + 0.5772$$

```python
import numpy as np

class IsolationTree:
    def __init__(self, max_depth=8):
        self.max_depth = max_depth

    def fit(self, X, depth=0):
        n, d = X.shape
        if depth >= self.max_depth or n <= 1:
            self.is_leaf, self.size = True, n
            return self
        self.is_leaf = False
        self.feat = np.random.randint(d)
        col = X[:, self.feat]
        lo, hi = col.min(), col.max()
        if lo == hi:
            self.is_leaf, self.size = True, n
            return self
        self.split = np.random.uniform(lo, hi)
        mask = col < self.split
        self.left  = IsolationTree(self.max_depth).fit(X[mask],  depth+1)
        self.right = IsolationTree(self.max_depth).fit(X[~mask], depth+1)
        return self

    def _c(self, n):
        if n <= 1: return 0
        return 2*(np.log(n-1)+0.5772156649) - 2*(n-1)/n

    def path_length(self, x, depth=0):
        if self.is_leaf:
            return depth + self._c(self.size)
        return (self.left if x[self.feat] < self.split else self.right).path_length(x, depth+1)

np.random.seed(42)
X_tr = np.random.normal(0, 1, (100, 2))
X_out = np.array([[5.0, 5.0], [-5.0, 4.0]])
tree = IsolationTree(max_depth=8).fit(X_tr)
cn = tree._c(len(X_tr))
scores_n = [2**(-tree.path_length(x)/cn) for x in X_tr]
scores_a = [2**(-tree.path_length(x)/cn) for x in X_out]
print(f'Normal avg score: {np.mean(scores_n):.3f} (should be ~0.5)')
print(f'Anomaly scores:   {[round(s,3) for s in scores_a]} (should be ~1.0)')
```

## sklearn IsolationForest

The sklearn implementation uses n_estimators trees (default 100), sub-sampling 256 points per tree. Sub-sampling reduces variance and limits the depth needed — with only 256 points, anomalies are almost always isolated before normal points. The contamination parameter sets the threshold for predict(): it determines what fraction of training data is labelled anomaly. The score_samples() method returns the raw anomaly score (more negative = more anomalous).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

np.random.seed(42)
X_normal  = np.random.normal(0, 1, (300, 2))
X_anomaly = np.random.uniform(-5, 5, (20, 2))
X = np.vstack([X_normal, X_anomaly])

clf = IsolationForest(n_estimators=100, contamination=0.06, random_state=42)
clf.fit(X)
scores = clf.score_samples(X)
preds  = clf.predict(X)

print(f'Anomalies detected: {(preds==-1).sum()}')
print(f'Score range: [{scores.min():.3f}, {scores.max():.3f}]')

xx, yy = np.meshgrid(np.linspace(-6, 6, 100), np.linspace(-6, 6, 100))
Z = clf.score_samples(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, levels=20, cmap='RdYlGn')
plt.scatter(X[preds==1,0],  X[preds==1,1],  c='steelblue', s=10, label='Normal')
plt.scatter(X[preds==-1,0], X[preds==-1,1], c='red', s=40, marker='x', label='Anomaly')
plt.legend()
plt.title('Isolation Forest — Score Contours')
plt.tight_layout()
plt.savefig('isolation_forest.png', dpi=100)
```

## Extended Isolation Forest — Rotational Invariance

Standard Isolation Forest uses axis-aligned splits, which creates ghost anomalies near split boundaries along the axes. Extended Isolation Forest (EIF) uses random hyperplane splits — it selects a random normal vector n and a random intercept p, then splits on nᵀx ≤ nᵀp. This eliminates the axis-aligned bias and works better on data with diagonal correlation structure or rotated clusters. EIF requires the eif package or a custom implementation.

```python
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import average_precision_score

np.random.seed(42)
cov = [[2.0, 1.8], [1.8, 2.0]]
X_normal  = np.random.multivariate_normal([0,0], cov, 400)
X_anomaly = np.random.uniform(-6, 6, (20, 2))
X = np.vstack([X_normal, X_anomaly])
y_true = np.array([0]*400 + [1]*20)

std_if = IsolationForest(n_estimators=200, contamination=0.047, random_state=42)
std_preds = std_if.fit_predict(X)
std_scores = -std_if.score_samples(X)
std_ap = average_precision_score(y_true, std_scores)

# Approximate EIF via random projections
rng = np.random.RandomState(42)
proj_scores = np.zeros(len(X))
for _ in range(200):
    n_vec = rng.randn(2)
    n_vec /= np.linalg.norm(n_vec)
    X1d = (X @ n_vec).reshape(-1, 1)
    clf1d = IsolationForest(n_estimators=1, contamination=0.047,
                            random_state=rng.randint(10000)).fit(X1d)
    proj_scores += -clf1d.score_samples(X1d)
proj_ap = average_precision_score(y_true, proj_scores)

print(f'Standard IF  AP: {std_ap:.3f} (axis-aligned splits, bias on rotated data)')
print(f'Projected IF AP: {proj_ap:.3f} (random hyperplanes reduce axis bias)')
```

## Anomaly Score Distribution

Training the model on normal data only (unsupervised novelty detection) and scoring both normal and anomalous test points reveals the score separation. Anomalies cluster near score −0.5 and normal points cluster near −0.1 to 0 (sklearn convention: more negative = more anomalous). The overlap between the distributions determines the achievable precision-recall tradeoff at any given threshold.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

np.random.seed(0)
X_train   = np.random.normal(0, 1, (500, 5))
X_test_n  = np.random.normal(0, 1, (200, 5))
X_test_a  = np.random.uniform(-4, 4, (50, 5))

clf = IsolationForest(n_estimators=100, random_state=0)
clf.fit(X_train)
scores_n = clf.score_samples(X_test_n)
scores_a = clf.score_samples(X_test_a)

print(f'Normal  scores: mean={scores_n.mean():.3f}  std={scores_n.std():.3f}')
print(f'Anomaly scores: mean={scores_a.mean():.3f}  std={scores_a.std():.3f}')
print(f'Threshold used: {clf.threshold_:.3f}')

fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(scores_n, bins=30, alpha=0.6, label='Normal test',  color='steelblue')
ax.hist(scores_a, bins=20, alpha=0.6, label='Anomaly test', color='crimson')
ax.axvline(clf.threshold_, color='black', linestyle='--', linewidth=2, label='Threshold')
ax.set_xlabel('Isolation Forest Score')
ax.legend()
ax.set_title('Score Distribution: Normal vs Anomaly (5-dim)')
plt.tight_layout()
plt.savefig('if_score_dist.png', dpi=100)
```

## Comparison with Other Detectors

| Method | Assumption | High-dim | Speed | Interpretable | Contamination param |
| --- | --- | --- | --- | --- | --- |
| Isolation Forest | Anomalies are few and different | Excellent | O(n log n) | Partially (path length) | Yes — contamination |
| LOF | Local density comparison | Poor (distances converge) | O(n² k) | Yes (LOF score ratio) | Implicit via k |
| One-Class SVM | Normal data on one side of hyperplane | Poor (kernel cost) | O(n² SV) | Low (kernel boundary) | Yes — nu |
| Autoencoder | Anomalies not on normal manifold | Good | Depends on arch | Low | Via threshold |

## Practical Guidance

Set n_estimators=100 as a baseline; 200-300 if precision matters. Sub-sample size of 256 (max_samples=256) works well for most datasets — increasing it rarely helps and slows training. When contamination is unknown, set contamination='auto' and use score_samples() with a threshold from a held-out validation set. For streaming anomaly detection, train on a rolling window and re-fit periodically.

> **When to Prefer Isolation Forest**: Isolation Forest is the recommended first choice for anomaly detection in high-dimensional tabular data (d > 10), when the dataset is large (n > 10,000), or when no assumption about the normal distribution can be made. Its O(n log n) complexity and lack of pairwise distance computation make it far faster than LOF or One-Class SVM at scale.

Sub-sampling is a key design choice: each tree is built on a random sample of max_samples points (default 256). Because anomalies are rare and isolated, 256 points is almost always enough to isolate them near the root. Increasing max_samples beyond 256 does not systematically improve detection and significantly slows training. If the dataset is very small (n < 256), set max_samples=n to use all data.

- Use max_samples=256 (default) — increasing it rarely improves results
- Set contamination to the expected anomaly fraction, or tune on a labelled validation set
- Score with score_samples() for continuous ranking rather than binary predict()
- Consider Extended Isolation Forest when data has strong diagonal correlation structure
- For online/streaming data, fit a new model periodically on a recent window

To evaluate performance without labelled data, use the anomaly score distribution: a well-trained Isolation Forest should show a clear bimodal distribution of scores when anomalies are present — a dense cluster near 0 (normal) and a sparse cluster near −0.5 and below (anomalous). If the distribution is unimodal, either contamination is very low or the anomalies are not isolated by random partitioning.

