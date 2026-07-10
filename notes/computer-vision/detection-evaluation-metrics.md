---
title: "Detection Evaluation: COCO mAP and Metrics"
slug: "detection-evaluation-metrics"
description: "COCO evaluation protocol — mAP@50, mAP@50:95, AP for small/medium/large objects, AR@100, and how to use pycocotools to evaluate a custom detector."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImgyIiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDT0NPIChDb21tb24gT2JqZWN0cyBpbiBDb250ZXh0KSBkZWZpbmVzIHRoZSBzdGFuZGFyZCBldmFsdWF0aW9uIHByb3RvY29sIGZvciBtb2Rlcm4gb2JqZWN0IGRldGVjdGlvbi4gVGhlIHByaW1hcnkgbWV0cmljIGlzIEFQNTA6OTUg4oCUIHRoZSBtZWFuIGF2ZXJhZ2UgcHJlY2lzaW9uIGF2ZXJhZ2VkIGFjcm9zcyAxMCBJb1UgdGhyZXNob2xkcyBmcm9tIDAuNSB0byAwLjk1LiBUaGlzIHN0cmljdGVyIHByb3RvY29sIHJld2FyZHMgZGV0ZWN0b3JzIHRoYXQgbG9jYWxpc2UgdGlnaHRseSwgbm90IGp1c3QgZGV0ZWN0b3JzIHRoYXQgZmluZCBvYmplY3RzIGFwcHJveGltYXRlbHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZXlvbmQgdGhlIGhlYWRsaW5lIG51bWJlciwgQ09DTyByZXBvcnRzIEFQIGJyb2tlbiBkb3duIGJ5IG9iamVjdCBzY2FsZSAoc21hbGwgXHUwMDNjMzLCsiwgbWVkaXVtIDMy4oCTOTbCsiwgbGFyZ2UgXHUwMDNlOTbCsiksIG1heGltdW0gcmVjYWxsIGF0IDEvMTAvMTAwIGRldGVjdGlvbnMgcGVyIGltYWdlLCBhbmQgcGVyLWNhdGVnb3J5IEFQLiBUaGVzZSBkaWFnbm9zdGljcyByZXZlYWwgd2hldGhlciBhIG1vZGVsIGZhaWxzIG9uIHRpbnkgb2JqZWN0cywgY3Jvd2RzLCBvciBzcGVjaWZpYyBzZW1hbnRpYyBjYXRlZ29yaWVzLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IlByZWNpc2lvbi1SZWNhbGwgQ3VydmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBhIHNpbmdsZSBjbGFzcyBhdCBhIGZpeGVkIElvVSB0aHJlc2hvbGQsIGV2YWx1YXRpb24gc29ydHMgYWxsIHByZWRpY3Rpb25zIGFjcm9zcyBhbGwgaW1hZ2VzIGJ5IGNvbmZpZGVuY2UgKGRlc2NlbmRpbmcpLiBFYWNoIHByZWRpY3Rpb24gaXMgbWF0Y2hlZCB0byBhbiB1bm1hdGNoZWQgZ3JvdW5kLXRydXRoIGJveCDigJQgaWYgSW9VIOKJpSB0aHJlc2hvbGQgaXQgaXMgYSB0cnVlIHBvc2l0aXZlLCBvdGhlcndpc2UgYSBmYWxzZSBwb3NpdGl2ZS4gUnVubmluZyBQIGFuZCBSIGFyZSBjb21wdXRlZCBjdW11bGF0aXZlbHksIHRyYWNpbmcgdGhlIFAtUiBjdXJ2ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHByZWNpc2lvbl9yZWNhbGxfY3VydmUoc2NvcmVzLCB0cF9mbGFncywgbl9ndCk6XG4gICAgXCJcIlwiXG4gICAgc2NvcmVzOiAgIChOLCkgY29uZmlkZW5jZSBzY29yZXNcbiAgICB0cF9mbGFnczogKE4sKSAxIGlmIFRQLCAwIGlmIEZQIChzb3J0ZWQgYnkgc2NvcmUgZGVzYylcbiAgICBuX2d0OiAgICAgdG90YWwgZ3JvdW5kLXRydXRoIGNvdW50IGZvciB0aGlzIGNsYXNzXG4gICAgXCJcIlwiXG4gICAgb3JkZXIgPSBucC5hcmdzb3J0KC1zY29yZXMpXG4gICAgdHAgPSB0cF9mbGFnc1tvcmRlcl1cbiAgICBmcCA9IDEgLSB0cFxuICAgIGN1bV90cCA9IG5wLmN1bXN1bSh0cClcbiAgICBjdW1fZnAgPSBucC5jdW1zdW0oZnApXG4gICAgcHJlY2lzaW9uID0gY3VtX3RwIC8gKGN1bV90cCArIGN1bV9mcCkuY2xpcChtaW49MWUtOClcbiAgICByZWNhbGwgPSBjdW1fdHAgLyBtYXgobl9ndCwgMSlcbiAgICByZXR1cm4gcHJlY2lzaW9uLCByZWNhbGwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgZ29vZCBkZXRlY3RvciB0cmFjZXMgYSBQLVIgY3VydmUgdGhhdCBodWdzIHRoZSB0b3AtcmlnaHQgY29ybmVyIOKAlCBoaWdoIHByZWNpc2lvbiBldmVuIGF0IGhpZ2ggcmVjYWxsLiBBcmVhIHVuZGVyIHRoaXMgY3VydmUgKEF2ZXJhZ2UgUHJlY2lzaW9uKSBzdW1tYXJpc2VzIHRoZSBlbnRpcmUgcHJlY2lzaW9uLXJlY2FsbCB0cmFkZS1vZmYgaW4gYSBzaW5nbGUgbnVtYmVyLCBpbmRlcGVuZGVudCBvZiBhbnkgb3BlcmF0aW5nIHBvaW50IHRocmVzaG9sZCBjaG9zZW4gYXQgaW5mZXJlbmNlIHRpbWUuIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoibUFQQDUwIHZzIG1BUEA1MDo5NSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoibUFQQDUwIChQYXNjYWwgVk9DIG1ldHJpYykgZGVjbGFyZXMgYSBkZXRlY3Rpb24gY29ycmVjdCBpZiBJb1Ugd2l0aCBhbnkgZ3JvdW5kLXRydXRoIGJveCBleGNlZWRzIDAuNS4gQSBib3ggY292ZXJpbmcgcm91Z2hseSB0aGUgcmlnaHQgYXJlYSBxdWFsaWZpZXMuIG1BUEA1MDo5NSByZXBlYXRzIHRoaXMgYXQgMTAgdGhyZXNob2xkcyAoMC41MCwgMC41NSwg4oCmLCAwLjk1KSBhbmQgYXZlcmFnZXMg4oCUIGEgYm94IG11c3QgbG9jYWxpc2UgdGlnaHRseSB0byBzY29yZSB3ZWxsIGF0IDAuNzUgb3IgMC45NS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGNvbXB1dGVfYXBfMTAxKHByZWNpc2lvbiwgcmVjYWxsKTpcbiAgICBcIlwiXCIxMDEtcG9pbnQgaW50ZXJwb2xhdGVkIEFQIChDT0NPIHN0eWxlKS5cIlwiXCJcbiAgICByZWNhbGxfdGhyZXNob2xkcyA9IG5wLmxpbnNwYWNlKDAsIDEsIDEwMSlcbiAgICBhcCA9IDAuMFxuICAgIGZvciB0aHIgaW4gcmVjYWxsX3RocmVzaG9sZHM6XG4gICAgICAgIHBfYXRfciA9IHByZWNpc2lvbltyZWNhbGwgXHUwMDNlPSB0aHJdXG4gICAgICAgIGFwICs9IChwX2F0X3IubWF4KCkgaWYgcF9hdF9yLnNpemUgXHUwMDNlIDAgZWxzZSAwLjApXG4gICAgcmV0dXJuIGFwIC8gMTAxXG5cbmRlZiBtYXBfNTBfOTUocGVyX2lvdV9hcHMpOlxuICAgIFwiXCJcInBlcl9pb3VfYXBzOiBsaXN0IG9mIDEwIEFQIHZhbHVlcyBhdCBJb1UgMC41Li4wLjk1XCJcIlwiXG4gICAgcmV0dXJuIGZsb2F0KG5wLm1lYW4ocGVyX2lvdV9hcHMpKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJjYWxsb3V0VHlwZSI6Indhcm5pbmciLCJjb250ZW50IjoiQVA1MCAoUGFzY2FsIFZPQyBzdHlsZSkgaXMgbXVjaCBlYXNpZXIgdG8gZ2FtZSB0aGFuIEFQNTA6OTUg4oCUIGEgbW9kZWwgY2FuIHNjb3JlIDYwJSBBUDUwIGJ1dCBvbmx5IDQwJSBBUDUwOjk1LiBVc2UgQ09DT1x1MDAyN3MgcHJpbWFyeSBtZXRyaWMgKEFQNTA6OTUpIGZvciBmYWlyIGNvbXBhcmlzb24uIn0seyJ0eXBlIjoiaDIiLCJjb250ZW50IjoiU21hbGwgLyBNZWRpdW0gLyBMYXJnZSBPYmplY3QgQVAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNPQ08gc2VnbWVudHMgQVAgYnkgb2JqZWN0IGFyZWE6IEFQcyAoYXJlYSBcdTAwM2MgMzLCsj0xMDI0IHB4wrIpLCBBUG0gKDEwMjTigJM5MjE2IHB4wrIpLCBBUGwgKFx1MDAzZTkyMTYgcHjCsikuIFNtYWxsIG9iamVjdCBBUCBpcyBjb25zaXN0ZW50bHkgdGhlIGhhcmRlc3QgbWV0cmljIOKAlCBkZXRlY3RvcnMgc3RydWdnbGUgYmVjYXVzZSBmZWF0dXJlcyBhcmUgbG93LXJlc29sdXRpb24gYW5kIGNvbnRleHQgaXMgbGltaXRlZC4gSW1wcm92ZW1lbnRzIG9uIEFQcyB1c3VhbGx5IGNvbWUgZnJvbSBoaWdoZXIgaW5wdXQgcmVzb2x1dGlvbiBvciBiZXR0ZXIgRlBOIGRlc2lnbi4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0cmljIiwiSW9VIHRocmVzaG9sZCIsIk9iamVjdCBzaXplIiwiV2hhdCBpdCBtZWFzdXJlcyJdLCJyb3dzIjpbWyJBUCAocHJpbWFyeSkiLCIwLjUwOjAuMDU6MC45NSIsIkFsbCIsIk92ZXJhbGwgbG9jYWxpc2F0aW9uIHF1YWxpdHkiXSxbIkFQNTAiLCIwLjUwIiwiQWxsIiwiQ29hcnNlIGRldGVjdGlvbiAoVk9DIHN0eWxlKSJdLFsiQVA3NSIsIjAuNzUiLCJBbGwiLCJTdHJpY3QgbG9jYWxpc2F0aW9uIl0sWyJBUHMiLCIwLjUwOjAuOTUiLCJcdTAwM2MgMzLDlzMyIHB4IiwiU21hbGwgb2JqZWN0IHBlcmZvcm1hbmNlIl0sWyJBUG0iLCIwLjUwOjAuOTUiLCIzMuKAkzk2IHB4IiwiTWVkaXVtIG9iamVjdCBwZXJmb3JtYW5jZSJdLFsiQVBsIiwiMC41MDowLjk1IiwiXHUwMDNlIDk2w5c5NiBweCIsIkxhcmdlIG9iamVjdCBwZXJmb3JtYW5jZSJdLFsiQVIxMDAiLCIwLjUwOjAuOTUiLCJBbGwiLCJNYXggcmVjYWxsIGF0IDEwMCBkZXRzL2ltZyJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBUiAoQXZlcmFnZSBSZWNhbGwpIGF0IDEwMCBkZXRlY3Rpb25zIHBlciBpbWFnZSBtZWFzdXJlcyB0aGUgdXBwZXIgYm91bmQgb24gcmVjYWxsIGdpdmVuIGEgZml4ZWQgZGV0ZWN0aW9uIGJ1ZGdldC4gQSBoaWdoIEFSMTAwIHdpdGggbG93IEFQIGluZGljYXRlcyB0aGUgbW9kZWwgZmluZHMgb2JqZWN0cyBidXQgcmFua3MgdGhlbSBwb29ybHkg4oCUIHRoZSBjb25maWRlbmNlIGNhbGlicmF0aW9uIG9yIE5NUyB0aHJlc2hvbGQgbmVlZHMgdHVuaW5nLiJ9LHsidHlwZSI6ImgyIiwiY29udGVudCI6IlVzaW5nIHB5Y29jb3Rvb2xzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJweWNvY290b29scyBpcyB0aGUgb2ZmaWNpYWwgQ09DTyBldmFsdWF0aW9uIGxpYnJhcnkuIEl0IGV4cGVjdHMgcHJlZGljdGlvbnMgaW4gQ09DTyByZXN1bHQgZm9ybWF0OiBhIEpTT04gYXJyYXkgb2Ygb2JqZWN0cyB3aXRoIGltYWdlX2lkLCBjYXRlZ29yeV9pZCwgYmJveCAoW3gseSx3LGhdIGZvcm1hdCksIGFuZCBzY29yZS4gVGhlIGxpYnJhcnkgaGFuZGxlcyBtYXRjaGluZywgSW9VIGNvbXB1dGF0aW9uLCBhbmQgYWxsIDEyIHN0YW5kYXJkIG1ldHJpY3MgaW4gYSBzaW5nbGUgZXZhbHVhdGUoKSArIHN1bW1hcml6ZSgpIGNhbGwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmciOiJweXRob24iLCJjb250ZW50IjoiZnJvbSBweWNvY290b29scy5jb2NvIGltcG9ydCBDT0NPXG5mcm9tIHB5Y29jb3Rvb2xzLmNvY29ldmFsIGltcG9ydCBDT0NPZXZhbFxuaW1wb3J0IGpzb25cblxuIyBMb2FkIGdyb3VuZCB0cnV0aFxuY29jb19ndCA9IENPQ08oXHUwMDI3YW5ub3RhdGlvbnMvaW5zdGFuY2VzX3ZhbDIwMTcuanNvblx1MDAyNylcblxuIyBMb2FkIHByZWRpY3Rpb25zIChsaXN0IG9mIGRpY3RzIHdpdGggaW1hZ2VfaWQsIGNhdGVnb3J5X2lkLCBiYm94LCBzY29yZSlcbndpdGggb3BlbihcdTAwMjdwcmVkaWN0aW9ucy5qc29uXHUwMDI3KSBhcyBmOlxuICAgIHByZWRfbGlzdCA9IGpzb24ubG9hZChmKVxuXG5jb2NvX2R0ID0gY29jb19ndC5sb2FkUmVzKHByZWRfbGlzdClcbmV2YWwgPSBDT0NPZXZhbChjb2NvX2d0LCBjb2NvX2R0LCBpb3VUeXBlPVx1MDAyN2Jib3hcdTAwMjcpXG5ldmFsLmV2YWx1YXRlKClcbmV2YWwuYWNjdW11bGF0ZSgpXG5ldmFsLnN1bW1hcml6ZSgpICAjIHByaW50cyBhbGwgMTIgbWV0cmljcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG8gZXZhbHVhdGUgb24gYSBzdWJzZXQgb2YgY2F0ZWdvcmllcyBvciBpbWFnZXMsIHNldCBldmFsLnBhcmFtcy5jYXRJZHMgYW5kIGV2YWwucGFyYW1zLmltZ0lkcyBiZWZvcmUgY2FsbGluZyBldmFsdWF0ZSgpLiBQZXItY2F0ZWdvcnkgQVAgcmVxdWlyZXMgaXRlcmF0aW5nIG92ZXIgY2F0ZWdvcmllcyBhbmQgc2V0dGluZyBwYXJhbXMuY2F0SWRzID0gW2NhdF9pZF0gZm9yIGVhY2gsIHRoZW4gcmVhZGluZyBldmFsLnN0YXRzWzBdIChBUDUwOjk1IGZvciB0aGF0IGNhdGVnb3J5KS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZyI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHB5Y29jb3Rvb2xzLmNvY28gaW1wb3J0IENPQ09cbmZyb20gcHljb2NvdG9vbHMuY29jb2V2YWwgaW1wb3J0IENPQ09ldmFsXG5cbmRlZiBwZXJfY2F0ZWdvcnlfYXAoY29jb19ndCwgY29jb19kdCk6XG4gICAgcmVzdWx0cyA9IHt9XG4gICAgZm9yIGNhdCBpbiBjb2NvX2d0LmxvYWRDYXRzKGNvY29fZ3QuZ2V0Q2F0SWRzKCkpOlxuICAgICAgICBldiA9IENPQ09ldmFsKGNvY29fZ3QsIGNvY29fZHQsIGlvdVR5cGU9XHUwMDI3YmJveFx1MDAyNylcbiAgICAgICAgZXYucGFyYW1zLmNhdElkcyA9IFtjYXRbXHUwMDI3aWRcdTAwMjddXVxuICAgICAgICBldi5ldmFsdWF0ZSgpXG4gICAgICAgIGV2LmFjY3VtdWxhdGUoKVxuICAgICAgICBldi5zdW1tYXJpemUoKVxuICAgICAgICByZXN1bHRzW2NhdFtcdTAwMjduYW1lXHUwMDI3XV0gPSByb3VuZChmbG9hdChldi5zdGF0c1swXSksIDQpXG4gICAgcmV0dXJuIHJlc3VsdHMifSx7InR5cGUiOiJoMiIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbHdheXMgcmVwb3J0IEFQNTA6OTUgYXMgdGhlIHByaW1hcnkgbWV0cmljIGZvciBDT0NPIGNvbXBhcmlzb25zLiBBUDUwIGFsb25lIG92ZXJzdGF0ZXMgbW9kZWwgcXVhbGl0eS4gV2hlbiBkZWJ1Z2dpbmcsIEFQcyBpcyB0aGUgZmlyc3QgcGxhY2UgdG8gbG9vayBmb3IgaGVhZHJvb20g4oCUIG1vc3QgU09UQSBtb2RlbHMgc3RpbGwgbGFnIHNpZ25pZmljYW50bHkgb24gc21hbGwgb2JqZWN0cyBjb21wYXJlZCB0byBtZWRpdW0gYW5kIGxhcmdlIG9uZXMuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb25maWRlbmNlIGNhbGlicmF0aW9uIG1hdHRlcnM6IGEgbWlzY2FsaWJyYXRlZCBtb2RlbCB0aGF0IHJhbmtzIEZQcyBhYm92ZSBUUHMgZGVncmFkZXMgQVAgd2l0aG91dCBhZmZlY3RpbmcgY2xhc3NpZmljYXRpb24gYWNjdXJhY3kuIFRlbXBlcmF0dXJlIHNjYWxpbmcgb3IgUGxhdHQgc2NhbGluZyBvbiBkZXRlY3RvciBjb25maWRlbmNlIHNjb3JlcyBjYW4gaW1wcm92ZSBBUCBieSAx4oCTMyBwb2ludHMgd2l0aG91dCByZXRyYWluaW5nIHRoZSBiYWNrYm9uZS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gY29tcGFyaW5nIGN1c3RvbSBkb21haW4gcmVzdWx0cyB0byBDT0NPIGJlbmNobWFya3MsIG5vdGUgdGhhdCBDT0NPIGhhcyA4MCBjYXRlZ29yaWVzIHdpdGggaGVhdnkgbG9uZy10YWlsIGRpc3RyaWJ1dGlvbi4gQSBtb2RlbCB0cmFpbmVkIG9uIDUgYmFsYW5jZWQgY2F0ZWdvcmllcyBtYXkgcmVwb3J0IGluZmxhdGVkIEFQIGJlY2F1c2UgcmFyZSBoYXJkIG5lZ2F0aXZlcyBhcmUgYWJzZW50LiBBbHdheXMgY29udGV4dHVhbGlzZSBtZXRyaWNzIGFnYWluc3QgdGhlIGV2YWx1YXRpb24gc2V0IGRpZmZpY3VsdHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBUjEwMCBpcyB1bmRlcnV0aWxpc2VkIGluIHByYWN0aWNlIGJ1dCB2YWx1YWJsZSBmb3IgdHdvLXN0YWdlIHBpcGVsaW5lcy4gSWYgeW91ciByZWdpb24gcHJvcG9zYWwgbmV0d29yayBpcyB0aGUgYm90dGxlbmVjaywgbWF4aW1pc2UgQVIxMDAgb2YgcHJvcG9zYWxzIGJlZm9yZSB3b3JyeWluZyBhYm91dCB0aGUgZGV0ZWN0aW9uIGhlYWQuIEEgcHJvcG9zYWwgQVIxMDAgYmVsb3cgOTAlIGNhcHMgZmluYWwgZGV0ZWN0b3IgQVAgcmVnYXJkbGVzcyBvZiBoZWFkIHF1YWxpdHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJweWNvY290b29scyBzdXBwb3J0cyBzZWdtZW50YXRpb24gKGlvdVR5cGU9XHUwMDI3c2VnbVx1MDAyNykgYW5kIGtleXBvaW50IChpb3VUeXBlPVx1MDAyN2tleXBvaW50c1x1MDAyNykgZXZhbHVhdGlvbiB3aXRoIHRoZSBzYW1lIEFQSS4gSW5zdGFuY2Ugc2VnbWVudGF0aW9uIG1vZGVscyBhcmUgZXZhbHVhdGVkIG9uIG1hc2sgSW9VLCBub3QgYm94IElvVSDigJQgYSBjb21tb24gc291cmNlIG9mIGNvbmZ1c2lvbiB3aGVuIGFkYXB0aW5nIGJveCBkZXRlY3RvcnMgdG8gc2VnbWVudGF0aW9uIHRhc2tzLiJ9XQ=="
---
# Detection Evaluation: COCO mAP and Metrics

COCO (Common Objects in Context) defines the standard evaluation protocol for modern object detection. The primary metric is AP50:95 — the mean average precision averaged across 10 IoU thresholds from 0.5 to 0.95. This stricter protocol rewards detectors that localise tightly, not just detectors that find objects approximately.

Beyond the headline number, COCO reports AP broken down by object scale (small <32², medium 32–96², large >96²), maximum recall at 1/10/100 detections per image, and per-category AP. These diagnostics reveal whether a model fails on tiny objects, crowds, or specific semantic categories.

For a single class at a fixed IoU threshold, evaluation sorts all predictions across all images by confidence (descending). Each prediction is matched to an unmatched ground-truth box — if IoU ≥ threshold it is a true positive, otherwise a false positive. Running P and R are computed cumulatively, tracing the P-R curve.

```
import numpy as np

def precision_recall_curve(scores, tp_flags, n_gt):
    """
    scores:   (N,) confidence scores
    tp_flags: (N,) 1 if TP, 0 if FP (sorted by score desc)
    n_gt:     total ground-truth count for this class
    """
    order = np.argsort(-scores)
    tp = tp_flags[order]
    fp = 1 - tp
    cum_tp = np.cumsum(tp)
    cum_fp = np.cumsum(fp)
    precision = cum_tp / (cum_tp + cum_fp).clip(min=1e-8)
    recall = cum_tp / max(n_gt, 1)
    return precision, recall
```

A good detector traces a P-R curve that hugs the top-right corner — high precision even at high recall. Area under this curve (Average Precision) summarises the entire precision-recall trade-off in a single number, independent of any operating point threshold chosen at inference time.

mAP@50 (Pascal VOC metric) declares a detection correct if IoU with any ground-truth box exceeds 0.5. A box covering roughly the right area qualifies. mAP@50:95 repeats this at 10 thresholds (0.50, 0.55, …, 0.95) and averages — a box must localise tightly to score well at 0.75 or 0.95.

```
import numpy as np

def compute_ap_101(precision, recall):
    """101-point interpolated AP (COCO style)."""
    recall_thresholds = np.linspace(0, 1, 101)
    ap = 0.0
    for thr in recall_thresholds:
        p_at_r = precision[recall >= thr]
        ap += (p_at_r.max() if p_at_r.size > 0 else 0.0)
    return ap / 101

def map_50_95(per_iou_aps):
    """per_iou_aps: list of 10 AP values at IoU 0.5..0.95"""
    return float(np.mean(per_iou_aps))
```

> ****: AP50 (Pascal VOC style) is much easier to game than AP50:95 — a model can score 60% AP50 but only 40% AP50:95. Use COCO's primary metric (AP50:95) for fair comparison.

COCO segments AP by object area: APs (area < 32²=1024 px²), APm (1024–9216 px²), APl (>9216 px²). Small object AP is consistently the hardest metric — detectors struggle because features are low-resolution and context is limited. Improvements on APs usually come from higher input resolution or better FPN design.

| Metric | IoU threshold | Object size | What it measures |
| --- | --- | --- | --- |
| AP (primary) | 0.50:0.05:0.95 | All | Overall localisation quality |
| AP50 | 0.50 | All | Coarse detection (VOC style) |
| AP75 | 0.75 | All | Strict localisation |
| APs | 0.50:0.95 | < 32×32 px | Small object performance |
| APm | 0.50:0.95 | 32–96 px | Medium object performance |
| APl | 0.50:0.95 | > 96×96 px | Large object performance |
| AR100 | 0.50:0.95 | All | Max recall at 100 dets/img |

AR (Average Recall) at 100 detections per image measures the upper bound on recall given a fixed detection budget. A high AR100 with low AP indicates the model finds objects but ranks them poorly — the confidence calibration or NMS threshold needs tuning.

pycocotools is the official COCO evaluation library. It expects predictions in COCO result format: a JSON array of objects with image_id, category_id, bbox ([x,y,w,h] format), and score. The library handles matching, IoU computation, and all 12 standard metrics in a single evaluate() + summarize() call.

```
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import json

# Load ground truth
coco_gt = COCO('annotations/instances_val2017.json')

# Load predictions (list of dicts with image_id, category_id, bbox, score)
with open('predictions.json') as f:
    pred_list = json.load(f)

coco_dt = coco_gt.loadRes(pred_list)
eval = COCOeval(coco_gt, coco_dt, iouType='bbox')
eval.evaluate()
eval.accumulate()
eval.summarize()  # prints all 12 metrics
```

To evaluate on a subset of categories or images, set eval.params.catIds and eval.params.imgIds before calling evaluate(). Per-category AP requires iterating over categories and setting params.catIds = [cat_id] for each, then reading eval.stats[0] (AP50:95 for that category).

```
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

def per_category_ap(coco_gt, coco_dt):
    results = {}
    for cat in coco_gt.loadCats(coco_gt.getCatIds()):
        ev = COCOeval(coco_gt, coco_dt, iouType='bbox')
        ev.params.catIds = [cat['id']]
        ev.evaluate()
        ev.accumulate()
        ev.summarize()
        results[cat['name']] = round(float(ev.stats[0]), 4)
    return results
```

Always report AP50:95 as the primary metric for COCO comparisons. AP50 alone overstates model quality. When debugging, APs is the first place to look for headroom — most SOTA models still lag significantly on small objects compared to medium and large ones.

Confidence calibration matters: a miscalibrated model that ranks FPs above TPs degrades AP without affecting classification accuracy. Temperature scaling or Platt scaling on detector confidence scores can improve AP by 1–3 points without retraining the backbone.

When comparing custom domain results to COCO benchmarks, note that COCO has 80 categories with heavy long-tail distribution. A model trained on 5 balanced categories may report inflated AP because rare hard negatives are absent. Always contextualise metrics against the evaluation set difficulty.

AR100 is underutilised in practice but valuable for two-stage pipelines. If your region proposal network is the bottleneck, maximise AR100 of proposals before worrying about the detection head. A proposal AR100 below 90% caps final detector AP regardless of head quality.

pycocotools supports segmentation (iouType='segm') and keypoint (iouType='keypoints') evaluation with the same API. Instance segmentation models are evaluated on mask IoU, not box IoU — a common source of confusion when adapting box detectors to segmentation tasks.

