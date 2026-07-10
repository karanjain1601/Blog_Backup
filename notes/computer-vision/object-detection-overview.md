---
title: "Object Detection: Fundamentals and Pipeline"
slug: "object-detection-overview"
description: "The object detection task — bounding box formats (xyxy, xywh, cxcywh), IoU computation, NMS, detection pipeline stages, and the one-stage vs two-stage paradigm."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPYmplY3QgZGV0ZWN0aW9uIGlzIHRoZSB0YXNrIG9mIGxvY2FsaXppbmcgYW5kIGNsYXNzaWZ5aW5nIG11bHRpcGxlIG9iamVjdHMgd2l0aGluIGFuIGltYWdlLiBVbmxpa2UgaW1hZ2UgY2xhc3NpZmljYXRpb24sIHdoaWNoIG91dHB1dHMgYSBzaW5nbGUgbGFiZWwsIGRldGVjdGlvbiBtb2RlbHMgb3V0cHV0IGEgc2V0IG9mIGJvdW5kaW5nIGJveGVzIOKAlCBlYWNoIHBhaXJlZCB3aXRoIGEgY2xhc3MgbGFiZWwgYW5kIGNvbmZpZGVuY2Ugc2NvcmUuIFRoZSBjb3JlIHBpcGVsaW5lIGludm9sdmVzIGZlYXR1cmUgZXh0cmFjdGlvbiwgcmVnaW9uIHNjb3JpbmcsIGJveCByZWdyZXNzaW9uLCBhbmQgcG9zdC1wcm9jZXNzaW5nIHN0ZXBzIGxpa2UgTk1TLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGV0ZWN0aW9uIGJlbmNobWFya3MgdXNlIG1ldHJpY3MgbGlrZSBtZWFuIEF2ZXJhZ2UgUHJlY2lzaW9uIChtQVApLCBtZWFzdXJlZCBhdCBzcGVjaWZpYyBJb1UgdGhyZXNob2xkcyAoZS5nLiwgQVA1MCwgQVA3NSwgb3IgQ09DT1x1MDAyN3MgQVAgYXZlcmFnZWQgZnJvbSAwLjUgdG8gMC45NSkuIFVuZGVyc3RhbmRpbmcgYm94IGZvcm1hdHMgYW5kIGdlb21ldHJpYyBvcGVyYXRpb25zIGxpa2UgSW9VIGlzIGVzc2VudGlhbCBiZWZvcmUgZGl2aW5nIGludG8gYW55IGRldGVjdG9yIGFyY2hpdGVjdHVyZS4gVGhpcyBub3RlIGNvdmVycyB0aGUgYnVpbGRpbmcgYmxvY2tzIHNoYXJlZCBieSB2aXJ0dWFsbHkgZXZlcnkgZGV0ZWN0aW9uIHBpcGVsaW5lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJvdW5kaW5nIEJveCBSZXByZXNlbnRhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJvdW5kaW5nIGJveGVzIGFyZSByZWN0YW5ndWxhciByZWdpb25zIHRoYXQgdGlnaHRseSBlbmNsb3NlIGRldGVjdGVkIG9iamVjdHMuIFNldmVyYWwgY29vcmRpbmF0ZSBmb3JtYXRzIGFyZSB1c2VkIGFjcm9zcyBmcmFtZXdvcmtzIGFuZCBkYXRhc2V0cy4geHl4eSBzdG9yZXMgdGhlIHRvcC1sZWZ0IGFuZCBib3R0b20tcmlnaHQgY29ybmVycy4geHl3aCBzdG9yZXMgdGhlIHRvcC1sZWZ0IGNvcm5lciBwbHVzIHdpZHRoIGFuZCBoZWlnaHQuIGN4Y3l3aCBzdG9yZXMgdGhlIGNlbnRlciBwb2ludCBwbHVzIHdpZHRoIGFuZCBoZWlnaHQuIEVhY2ggZm9ybWF0IGhhcyBkaWZmZXJlbnQgYWxnZWJyYWljIHByb3BlcnRpZXMgdGhhdCBtYWtlIGl0IG1vcmUgbmF0dXJhbCBmb3Igc3BlY2lmaWMgb3BlcmF0aW9ucy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNPQ08gYW5ub3RhdGlvbnMgdXNlIHh5d2ggd2l0aCBhYnNvbHV0ZSBwaXhlbCB2YWx1ZXMsIHdoaWxlIFlPTE8gbW9kZWxzIHdvcmsgd2l0aCBub3JtYWxpemVkIGN4Y3l3aCAodmFsdWVzIGluIFswLDFdIHJlbGF0aXZlIHRvIGltYWdlIGRpbWVuc2lvbnMpLiB0b3JjaHZpc2lvbiBpbnRlcm5hbGx5IHVzZXMgeHl4eSBmb3JtYXQuIEVmZmljaWVudCBkZXRlY3Rpb24gY29kZSBtdXN0IGhhbmRsZSBjb252ZXJzaW9ucyBjbGVhbmx5LCBhbmQgTnVtUHkgYnJvYWRjYXN0aW5nIG1ha2VzIGl0IHN0cmFpZ2h0Zm9yd2FyZCB0byBjb252ZXJ0IGVudGlyZSBhcnJheXMgb2YgYm94ZXMgYXQgb25jZSB3aXRob3V0IGxvb3BzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHh5eHlfdG9feHl3aChib3hlcyk6XG4gICAgIyBib3hlczogW04sNF0gaW4geHl4eSBmb3JtYXQgLVx1MDAzZSBbeDEseTEsdyxoXVxuICAgIHJldHVybiBucC5zdGFjayhbYm94ZXNbOiwwXSwgYm94ZXNbOiwxXSxcbiAgICAgICAgICAgICAgICAgICAgIGJveGVzWzosMl0tYm94ZXNbOiwwXSxcbiAgICAgICAgICAgICAgICAgICAgIGJveGVzWzosM10tYm94ZXNbOiwxXV0sIGF4aXM9MSlcblxuZGVmIHh5d2hfdG9fY3hjeXdoKGJveGVzKTpcbiAgICAjIGJveGVzOiBbTiw0XSBpbiB4eXdoIGZvcm1hdCAtXHUwMDNlIFtjeCxjeSx3LGhdXG4gICAgcmV0dXJuIG5wLnN0YWNrKFtib3hlc1s6LDBdK2JveGVzWzosMl0vMixcbiAgICAgICAgICAgICAgICAgICAgIGJveGVzWzosMV0rYm94ZXNbOiwzXS8yLFxuICAgICAgICAgICAgICAgICAgICAgYm94ZXNbOiwyXSwgYm94ZXNbOiwzXV0sIGF4aXM9MSlcblxuZGVmIHh5eHlfdG9fY3hjeXdoKGJveGVzKTpcbiAgICByZXR1cm4geHl3aF90b19jeGN5d2goeHl4eV90b194eXdoKGJveGVzKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnRlcnNlY3Rpb24gb3ZlciBVbmlvbiAoSW9VKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW9VIGlzIHRoZSByYXRpbyBvZiB0aGUgaW50ZXJzZWN0aW9uIGFyZWEgdG8gdGhlIHVuaW9uIGFyZWEgb2YgdHdvIGJvdW5kaW5nIGJveGVzLiBJdCBtZWFzdXJlcyBob3cgd2VsbCB0d28gYm94ZXMgb3ZlcmxhcCBhbmQgaXMgdXNlZCBpbiB0d28gY3JpdGljYWwgcGxhY2VzOiBhbmNob3IgYXNzaWdubWVudCBkdXJpbmcgdHJhaW5pbmcgKGRlY2lkaW5nIHdoZXRoZXIgYW4gYW5jaG9yIGlzIHBvc2l0aXZlIG9yIG5lZ2F0aXZlKSBhbmQgTk1TIGR1cmluZyBpbmZlcmVuY2UgKGRlY2lkaW5nIHdoZXRoZXIgdHdvIGRldGVjdGlvbnMgcmVmZXIgdG8gdGhlIHNhbWUgb2JqZWN0KS4gSW9VIG9mIDAgbWVhbnMgbm8gb3ZlcmxhcDsgMS4wIG1lYW5zIHBlcmZlY3Qgb3ZlcmxhcC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIHNldCBvZiBwcmVkaWN0ZWQgYm94ZXMgYW5kIGdyb3VuZC10cnV0aCBib3hlcywgd2Ugb2Z0ZW4gbmVlZCBwYWlyd2lzZSBJb1Ug4oCUIGEgbWF0cml4IG9mIHNoYXBlIFtOX3ByZWQsIE5fZ3RdLiBUaGlzIGlzIGNvbXB1dGVkIGVmZmljaWVudGx5IHVzaW5nIGJyb2FkY2FzdGluZy4gVmVjdG9yaXplZCBJb1UgaXMgZXNzZW50aWFsIGZvciBmYXN0IGFuY2hvciBtYXRjaGluZyBkdXJpbmcgdHJhaW5pbmcsIHdoZXJlIHRob3VzYW5kcyBvZiBhbmNob3JzIG11c3QgYmUgY29tcGFyZWQgYWdhaW5zdCBkb3plbnMgb2YgR1QgYm94ZXMgd2l0aG91dCBQeXRob24gbG9vcHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY29tcHV0ZV9pb3UoYm94X2EsIGJveF9iKTpcbiAgICAjIENvbXB1dGUgSW9VIGJldHdlZW4gdHdvIGJveGVzIGluIHh5eHkgZm9ybWF0XG4gICAgeGEgPSBtYXgoYm94X2FbMF0sIGJveF9iWzBdKVxuICAgIHlhID0gbWF4KGJveF9hWzFdLCBib3hfYlsxXSlcbiAgICB4YiA9IG1pbihib3hfYVsyXSwgYm94X2JbMl0pXG4gICAgeWIgPSBtaW4oYm94X2FbM10sIGJveF9iWzNdKVxuXG4gICAgaW50ZXIgPSBtYXgoMCwgeGIgLSB4YSkgKiBtYXgoMCwgeWIgLSB5YSlcbiAgICBhcmVhX2EgPSAoYm94X2FbMl0tYm94X2FbMF0pICogKGJveF9hWzNdLWJveF9hWzFdKVxuICAgIGFyZWFfYiA9IChib3hfYlsyXS1ib3hfYlswXSkgKiAoYm94X2JbM10tYm94X2JbMV0pXG4gICAgdW5pb24gPSBhcmVhX2EgKyBhcmVhX2IgLSBpbnRlclxuICAgIHJldHVybiBpbnRlciAvIHVuaW9uIGlmIHVuaW9uIFx1MDAzZSAwIGVsc2UgMC4wIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTm9uLU1heGltdW0gU3VwcHJlc3Npb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5NUyBpcyB0aGUgcG9zdC1wcm9jZXNzaW5nIHN0ZXAgdGhhdCByZW1vdmVzIGR1cGxpY2F0ZSBkZXRlY3Rpb25zLiBCZWNhdXNlIG11bHRpcGxlIGFuY2hvcnMgb3IgZ3JpZCBjZWxscyBtYXkgcmVzcG9uZCB0byB0aGUgc2FtZSBvYmplY3QsIGRldGVjdG9ycyBvZnRlbiBwcm9kdWNlIGh1bmRyZWRzIG9mIG92ZXJsYXBwaW5nIGJveGVzIGZvciBhIHNpbmdsZSBpbnN0YW5jZS4gTk1TIHJldGFpbnMgdGhlIGhpZ2hlc3Qtc2NvcmluZyBib3ggZm9yIGVhY2ggb2JqZWN0IGFuZCBzdXBwcmVzc2VzIGFsbCBvdGhlciBib3hlcyB3aG9zZSBJb1Ugd2l0aCB0aGUga2VwdCBib3ggZXhjZWVkcyBhIHRocmVzaG9sZCAodHlwaWNhbGx5IDAuNSBmb3IgQ09DTykuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTb2Z0LU5NUyBpcyBhIHZhcmlhbnQgdGhhdCBkZWNheXMgc2NvcmVzIG9mIG92ZXJsYXBwaW5nIGJveGVzIHJhdGhlciB0aGFuIGhhcmQtcmVtb3ZpbmcgdGhlbSwgaW1wcm92aW5nIHJlY2FsbCBpbiBkZW5zZSBzY2VuZXMuIEZvciBtdWx0aS1jbGFzcyBkZXRlY3Rpb24sIHN0YW5kYXJkIE5NUyBpcyBhcHBsaWVkIHBlciBjbGFzcyBpbmRlcGVuZGVudGx5LiB0b3JjaHZpc2lvblx1MDAyN3MgYmF0Y2hlZF9ubXMgaGFuZGxlcyB0aGlzIGVmZmljaWVudGx5IGJ5IG9mZnNldHRpbmcgYm94ZXMgYnkgY2xhc3MgaW5kZXggYmVmb3JlIGFwcGx5aW5nIGNsYXNzLWFnbm9zdGljIE5NUy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBubXMoYm94ZXMsIHNjb3JlcywgaW91X3RocmVzaG9sZD0wLjUpOlxuICAgICMgR3JlZWR5IE5NUy4gYm94ZXM6IFtOLDRdIHh5eHksIHNjb3JlczogW05dXG4gICAgb3JkZXIgPSBzY29yZXMuYXJnc29ydCgpWzo6LTFdXG4gICAga2VlcCA9IFtdXG4gICAgd2hpbGUgb3JkZXIuc2l6ZSBcdTAwM2UgMDpcbiAgICAgICAgaSA9IG9yZGVyWzBdXG4gICAgICAgIGtlZXAuYXBwZW5kKGkpXG4gICAgICAgIGlvdXMgPSBucC5hcnJheShbY29tcHV0ZV9pb3UoYm94ZXNbaV0sIGJveGVzW2pdKVxuICAgICAgICAgICAgICAgICAgICAgICAgIGZvciBqIGluIG9yZGVyWzE6XV0pXG4gICAgICAgIG9yZGVyID0gb3JkZXJbMTpdW2lvdXMgXHUwMDNjPSBpb3VfdGhyZXNob2xkXVxuICAgIHJldHVybiBrZWVwIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaHZpc2lvbi5vcHMgaW1wb3J0IGJhdGNoZWRfbm1zXG5cbiMgYm94ZXM6IFtOLDRdIHh5eHkgZmxvYXQsIHNjb3JlczogW05dLCBsYWJlbHM6IFtOXSBpbnRcbmJveGVzID0gdG9yY2gudGVuc29yKFtbMTAsMjAsNTAsODBdLFsxMiwyMiw1Miw4Ml0sXG4gICAgICAgICAgICAgICAgICAgICAgIFsxMDAsMTAwLDIwMCwyMDBdXSwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnNjb3JlcyA9IHRvcmNoLnRlbnNvcihbMC45LCAwLjg1LCAwLjk1XSlcbmxhYmVscyA9IHRvcmNoLnRlbnNvcihbMCwgMCwgMV0pXG5cbmtlZXAgPSBiYXRjaGVkX25tcyhib3hlcywgc2NvcmVzLCBsYWJlbHMsIGlvdV90aHJlc2hvbGQ9MC41KVxucHJpbnQoXHUwMDI3S2VwdCBpbmRpY2VzOlx1MDAyNywga2VlcClcbiMgTk1TIGFwcGxpZWQgcGVyIGNsYXNzOyBib3hlcyBmcm9tIGRpZmZlcmVudCBjbGFzc2VzXG4jIGFyZSBuZXZlciBzdXBwcmVzc2VkIGFnYWluc3QgZWFjaCBvdGhlci4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJjb250ZW50IjoiTk1TIGlzIGNsYXNzLXNwZWNpZmljIGJ5IGRlZmF1bHQg4oCUIHVzZSBiYXRjaGVkX25tcyBpbiB0b3JjaHZpc2lvbiB0byBhcHBseSBOTVMgcGVyIGNsYXNzLiBDbGFzcy1hZ25vc3RpYyBOTVMgY2FuIHN1cHByZXNzIHZhbGlkIGJveGVzIGZyb20gZGlmZmVyZW50IGNsYXNzZXMgdGhhdCBvdmVybGFwLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9uZS1TdGFnZSB2cyBUd28tU3RhZ2UgRGV0ZWN0b3JzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUd28tc3RhZ2UgZGV0ZWN0b3JzIChSLUNOTiBmYW1pbHkpIGZpcnN0IGdlbmVyYXRlIHJlZ2lvbiBwcm9wb3NhbHMgdXNpbmcgYSBkZWRpY2F0ZWQgbmV0d29yayAoUlBOKSwgdGhlbiBjbGFzc2lmeSBhbmQgcmVmaW5lIGVhY2ggcHJvcG9zYWwgaW4gYSBzZWNvbmQgc3RhZ2UuIFRoaXMgZGVjb3VwbGluZyBhbGxvd3MgaGlnaCBhY2N1cmFjeSBidXQgYWRkcyBsYXRlbmN5LiBPbmUtc3RhZ2UgZGV0ZWN0b3JzIChZT0xPLCBTU0QsIFJldGluYU5ldCkgcHJlZGljdCBib3hlcyBhbmQgY2xhc3Mgc2NvcmVzIGRpcmVjdGx5IGZyb20gYSBmZWF0dXJlIG1hcCBncmlkIGluIGEgc2luZ2xlIGZvcndhcmQgcGFzcywgdHJhZGluZyBzb21lIGFjY3VyYWN5IGZvciBzcGVlZC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJldGluYU5ldCBpbnRyb2R1Y2VkIGZvY2FsIGxvc3MgdG8gYWRkcmVzcyB0aGUgZXh0cmVtZSBjbGFzcyBpbWJhbGFuY2UgaW4gb25lLXN0YWdlIGRldGVjdG9ycyDigJQgbW9zdCBhbmNob3JzIGFyZSBlYXN5IG5lZ2F0aXZlcy4gRm9jYWwgbG9zcyBkb3duLXdlaWdodHMgd2VsbC1jbGFzc2lmaWVkIGV4YW1wbGVzLCBsZXR0aW5nIHRoZSBtb2RlbCBmb2N1cyBvbiBoYXJkIGNhc2VzLiBNb2Rlcm4gYW5jaG9yLWZyZWUgb25lLXN0YWdlIGRldGVjdG9ycyBsaWtlIEZDT1MgcHJlZGljdCBib3hlcyBmcm9tIGV2ZXJ5IGZvcmVncm91bmQgcGl4ZWwgcmF0aGVyIHRoYW4gZnJvbSBkaXNjcmV0ZSBhbmNob3IgdGVtcGxhdGVzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhbnNmb3JtZXItYmFzZWQgZGV0ZWN0b3JzIGxpa2UgREVUUiByZWZvcm11bGF0ZSBkZXRlY3Rpb24gYXMgYSBzZXQgcHJlZGljdGlvbiBwcm9ibGVtLCBlbGltaW5hdGluZyBOTVMgZW50aXJlbHkgYnkgdXNpbmcgYmlwYXJ0aXRlIG1hdGNoaW5nIGR1cmluZyB0cmFpbmluZy4gV2hpbGUgc2xvd2VyIHRvIHRyYWluIHRoYW4gQ05OLWJhc2VkIG1ldGhvZHMsIERFVFIgdmFyaWFudHMgKERlZm9ybWFibGUgREVUUiwgRElOTykgbm93IG1hdGNoIG9yIGV4Y2VlZCB0d28tc3RhZ2UgYWNjdXJhY3kgb24gQ09DTyB3aXRoIHNpbXBsZXIgcG9zdC1wcm9jZXNzaW5nIHBpcGVsaW5lcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHNvbGlkIGdyYXNwIG9mIGJveCBmb3JtYXRzLCBJb1UgY29tcHV0YXRpb24sIGFuZCBOTVMgaXMgcHJlcmVxdWlzaXRlIGtub3dsZWRnZSBmb3IgZXZlcnkgZGV0ZWN0aW9uIGFyY2hpdGVjdHVyZS4gVGhlc2UgcHJpbWl0aXZlcyBhcHBlYXIgaW4gdHJhaW5pbmcgKGFuY2hvciBhc3NpZ25tZW50LCBsb3NzIGNvbXB1dGF0aW9uKSBhbmQgaW5mZXJlbmNlIChib3ggZGVjb2RpbmcsIGR1cGxpY2F0ZSBzdXBwcmVzc2lvbikuIEJ1aWxkaW5nIGVmZmljaWVudCB2ZWN0b3JpemVkIGltcGxlbWVudGF0aW9ucyBvZiB0aGVzZSBvcGVyYXRpb25zIGlzIGEgcHJhY3RpY2FsIHNraWxsIGZvciBhbnlvbmUgd29ya2luZyBvbiBjdXN0b20gZGV0ZWN0b3JzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJGb3JtYXQiLCJGaWVsZHMiLCJDZW50ZXI/IiwiU2l6ZSBGaWVsZHMiLCJVc2VkIEJ5Il0sInJvd3MiOltbInh5eHkiLCJ4MSx5MSx4Mix5MiIsIk5vIiwiSW1wbGljaXQiLCJ0b3JjaHZpc2lvbiwgQ09DTyBldmFsIl0sWyJ4eXdoIiwieDEseTEsdyxoIiwiTm8iLCJ3LGgiLCJDT0NPIGFubm90YXRpb25zIl0sWyJjeGN5d2giLCJjeCxjeSx3LGgiLCJZZXMiLCJ3LGgiLCJZT0xPIGFic29sdXRlIGNvb3JkcyJdLFsibm9ybWFsaXplZCB4eXdoIiwiY3gsY3ksdyxoICgwLTEpIiwiWWVzIiwidyxoIiwiWU9MTyBsYWJlbCBmaWxlcyJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIHNlbGVjdGluZyBhIGRldGVjdGlvbiBmcmFtZXdvcmssIGNvbnNpZGVyIGluZmVyZW5jZSBzcGVlZCAoRlBTKSwgbW9kZWwgc2l6ZSwgYW5kIHdoZXRoZXIgdGhlIGRlcGxveW1lbnQgdGFyZ2V0IGhhcyBHUFUgc3VwcG9ydC4gVHdvLXN0YWdlIGRldGVjdG9ycyBnZW5lcmFsbHkgZXhjZWwgYXQgc21hbGwgb2JqZWN0IGRldGVjdGlvbiBkdWUgdG8gdGhlaXIgaGlnaC1yZXNvbHV0aW9uIFJvSSBmZWF0dXJlcywgd2hpbGUgb25lLXN0YWdlIGRldGVjdG9ycyBhcmUgcHJlZmVycmVkIGZvciByZWFsLXRpbWUgYXBwbGljYXRpb25zLiBBbmNob3ItZnJlZSBhcHByb2FjaGVzIHJlZHVjZSBoeXBlcnBhcmFtZXRlciB0dW5pbmcgc2lnbmlmaWNhbnRseS4ifV0="
---
# Object Detection: Fundamentals and Pipeline

## Overview

Object detection is the task of localizing and classifying multiple objects within an image. Unlike image classification, which outputs a single label, detection models output a set of bounding boxes — each paired with a class label and confidence score. The core pipeline involves feature extraction, region scoring, box regression, and post-processing steps like NMS.

Detection benchmarks use metrics like mean Average Precision (mAP), measured at specific IoU thresholds (e.g., AP50, AP75, or COCO's AP averaged from 0.5 to 0.95). Understanding box formats and geometric operations like IoU is essential before diving into any detector architecture. This note covers the building blocks shared by virtually every detection pipeline.

## Bounding Box Representations

Bounding boxes are rectangular regions that tightly enclose detected objects. Several coordinate formats are used across frameworks and datasets. xyxy stores the top-left and bottom-right corners. xywh stores the top-left corner plus width and height. cxcywh stores the center point plus width and height. Each format has different algebraic properties that make it more natural for specific operations.

COCO annotations use xywh with absolute pixel values, while YOLO models work with normalized cxcywh (values in [0,1] relative to image dimensions). torchvision internally uses xyxy format. Efficient detection code must handle conversions cleanly, and NumPy broadcasting makes it straightforward to convert entire arrays of boxes at once without loops.

```python
import numpy as np

def xyxy_to_xywh(boxes):
    # boxes: [N,4] in xyxy format -> [x1,y1,w,h]
    return np.stack([boxes[:,0], boxes[:,1],
                     boxes[:,2]-boxes[:,0],
                     boxes[:,3]-boxes[:,1]], axis=1)

def xywh_to_cxcywh(boxes):
    # boxes: [N,4] in xywh format -> [cx,cy,w,h]
    return np.stack([boxes[:,0]+boxes[:,2]/2,
                     boxes[:,1]+boxes[:,3]/2,
                     boxes[:,2], boxes[:,3]], axis=1)

def xyxy_to_cxcywh(boxes):
    return xywh_to_cxcywh(xyxy_to_xywh(boxes))
```

## Intersection over Union (IoU)

IoU is the ratio of the intersection area to the union area of two bounding boxes. It measures how well two boxes overlap and is used in two critical places: anchor assignment during training (deciding whether an anchor is positive or negative) and NMS during inference (deciding whether two detections refer to the same object). IoU of 0 means no overlap; 1.0 means perfect overlap.

For a set of predicted boxes and ground-truth boxes, we often need pairwise IoU — a matrix of shape [N_pred, N_gt]. This is computed efficiently using broadcasting. Vectorized IoU is essential for fast anchor matching during training, where thousands of anchors must be compared against dozens of GT boxes without Python loops.

```python
import numpy as np

def compute_iou(box_a, box_b):
    # Compute IoU between two boxes in xyxy format
    xa = max(box_a[0], box_b[0])
    ya = max(box_a[1], box_b[1])
    xb = min(box_a[2], box_b[2])
    yb = min(box_a[3], box_b[3])

    inter = max(0, xb - xa) * max(0, yb - ya)
    area_a = (box_a[2]-box_a[0]) * (box_a[3]-box_a[1])
    area_b = (box_b[2]-box_b[0]) * (box_b[3]-box_b[1])
    union = area_a + area_b - inter
    return inter / union if union > 0 else 0.0
```

## Non-Maximum Suppression

NMS is the post-processing step that removes duplicate detections. Because multiple anchors or grid cells may respond to the same object, detectors often produce hundreds of overlapping boxes for a single instance. NMS retains the highest-scoring box for each object and suppresses all other boxes whose IoU with the kept box exceeds a threshold (typically 0.5 for COCO).

Soft-NMS is a variant that decays scores of overlapping boxes rather than hard-removing them, improving recall in dense scenes. For multi-class detection, standard NMS is applied per class independently. torchvision's batched_nms handles this efficiently by offsetting boxes by class index before applying class-agnostic NMS.

```python
import numpy as np

def nms(boxes, scores, iou_threshold=0.5):
    # Greedy NMS. boxes: [N,4] xyxy, scores: [N]
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        ious = np.array([compute_iou(boxes[i], boxes[j])
                         for j in order[1:]])
        order = order[1:][ious <= iou_threshold]
    return keep
```

```python
import torch
from torchvision.ops import batched_nms

# boxes: [N,4] xyxy float, scores: [N], labels: [N] int
boxes = torch.tensor([[10,20,50,80],[12,22,52,82],
                       [100,100,200,200]], dtype=torch.float32)
scores = torch.tensor([0.9, 0.85, 0.95])
labels = torch.tensor([0, 0, 1])

keep = batched_nms(boxes, scores, labels, iou_threshold=0.5)
print('Kept indices:', keep)
# NMS applied per class; boxes from different classes
# are never suppressed against each other.
```

> **warning**: NMS is class-specific by default — use batched_nms in torchvision to apply NMS per class. Class-agnostic NMS can suppress valid boxes from different classes that overlap.

## One-Stage vs Two-Stage Detectors

Two-stage detectors (R-CNN family) first generate region proposals using a dedicated network (RPN), then classify and refine each proposal in a second stage. This decoupling allows high accuracy but adds latency. One-stage detectors (YOLO, SSD, RetinaNet) predict boxes and class scores directly from a feature map grid in a single forward pass, trading some accuracy for speed.

RetinaNet introduced focal loss to address the extreme class imbalance in one-stage detectors — most anchors are easy negatives. Focal loss down-weights well-classified examples, letting the model focus on hard cases. Modern anchor-free one-stage detectors like FCOS predict boxes from every foreground pixel rather than from discrete anchor templates.

Transformer-based detectors like DETR reformulate detection as a set prediction problem, eliminating NMS entirely by using bipartite matching during training. While slower to train than CNN-based methods, DETR variants (Deformable DETR, DINO) now match or exceed two-stage accuracy on COCO with simpler post-processing pipelines.

## Key Takeaways

A solid grasp of box formats, IoU computation, and NMS is prerequisite knowledge for every detection architecture. These primitives appear in training (anchor assignment, loss computation) and inference (box decoding, duplicate suppression). Building efficient vectorized implementations of these operations is a practical skill for anyone working on custom detectors.

| Format | Fields | Center? | Size Fields | Used By |
| --- | --- | --- | --- | --- |
| xyxy | x1,y1,x2,y2 | No | Implicit | torchvision, COCO eval |
| xywh | x1,y1,w,h | No | w,h | COCO annotations |
| cxcywh | cx,cy,w,h | Yes | w,h | YOLO absolute coords |
| normalized xywh | cx,cy,w,h (0-1) | Yes | w,h | YOLO label files |

When selecting a detection framework, consider inference speed (FPS), model size, and whether the deployment target has GPU support. Two-stage detectors generally excel at small object detection due to their high-resolution RoI features, while one-stage detectors are preferred for real-time applications. Anchor-free approaches reduce hyperparameter tuning significantly.

