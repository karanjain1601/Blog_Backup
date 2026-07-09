---
title: "Convex vs Non-Convex Loss Landscapes"
slug: "convex-nonconvex-landscapes"
description: "Deep dive into convex and non-convex loss landscapes: definitions, Jensen's inequality, strong convexity, saddle points, loss landscape visualization, mode connectivity, and the NTK regime."
tags: ["calculus", "optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGdlb21ldHJ5IG9mIHRoZSBsb3NzIGxhbmRzY2FwZSBkZXRlcm1pbmVzIHdoZXRoZXIgb3B0aW1pemF0aW9uIGlzIHRyYWN0YWJsZSwgd2hldGhlciBncmFkaWVudCBkZXNjZW50IGNvbnZlcmdlcywgYW5kIHdoZXJlIGl0IGNvbnZlcmdlcyB0by4gQ29udmV4IGxhbmRzY2FwZXMgaGF2ZSBhIHNpbmdsZSBnbG9iYWwgYm93bDsgbm9uLWNvbnZleCBsYW5kc2NhcGVzIGhhdmUgcmlkZ2VzLCB2YWxsZXlzLCBzYWRkbGUgcG9pbnRzLCBhbmQgbWFueSBsb2NhbCBtaW5pbWEuIFVuZGVyc3RhbmRpbmcgdGhlIGRpZmZlcmVuY2UgaXMgZXNzZW50aWFsIGZvciBjaG9vc2luZyBvcHRpbWl6ZXJzLCBkaWFnbm9zaW5nIHRyYWluaW5nIGZhaWx1cmVzLCBhbmQgcmVhc29uaW5nIGFib3V0IGdlbmVyYWxpemF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoYXQgaXMgYSBDb252ZXggRnVuY3Rpb24/In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGZ1bmN0aW9uIGY6IOKEneKBvyDihpIg4oSdIGlzIGNvbnZleCBpZiBmb3IgYWxsIHgsIHkgaW4gaXRzIGRvbWFpbiBhbmQgYWxsIM67IOKIiCBbMCwxXTogZijOu3ggKyAoMeKIks67KXkpIOKJpCDOu2YoeCkgKyAoMeKIks67KWYoeSkuIEdlb21ldHJpY2FsbHksIHRoZSBjaG9yZCBjb25uZWN0aW5nIGFueSB0d28gcG9pbnRzIG9uIHRoZSBncmFwaCBsaWVzIGFib3ZlIG9yIG9uIHRoZSBncmFwaC4gRXF1aXZhbGVudGx5IChmb3IgZGlmZmVyZW50aWFibGUgZik6IGYoeSkg4omlIGYoeCkgKyDiiIdmKHgp4bWAKHniiJJ4KSDigJQgdGhlIGZ1bmN0aW9uIGxpZXMgYWJvdmUgYWxsIGl0cyB0YW5nZW50IGh5cGVycGxhbmVzLiBGb3IgdHdpY2UtZGlmZmVyZW50aWFibGUgZjogdGhlIEhlc3NpYW4g4oiHwrJmKHgpIOKqsCAwIChwb3NpdGl2ZSBzZW1pZGVmaW5pdGUpIGV2ZXJ5d2hlcmUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJDb252ZXg6IGYozrt4KygxLc67KXkpIOKJpCDOu2YoeCkrKDEtzrspZih5KSDigJQgY2hvcmQgbGllcyBhYm92ZSBncmFwaCIsIlN0cmljdGx5IGNvbnZleDogc3RyaWN0IGluZXF1YWxpdHkgZm9yIHjiiaB5IOKAlCB1bmlxdWUgbWluaW1pemVyIiwizrwtc3Ryb25nbHkgY29udmV4OiBmKHkpIOKJpSBmKHgpICsg4oiHZih4KeG1gCh5LXgpICsgKM68LzIp4oCWeS144oCWwrIg4oCUIHF1YWRyYXRpYyBsb3dlciBib3VuZCBndWFyYW50ZWVzIHVuaXF1ZSBnbG9iYWwgbWluaW11bSIsIkwtc21vb3RoOiDigJbiiIdmKHgpLeKIh2YoeSnigJYg4omkIEzigJZ4LXnigJYg4oCUIExpcHNjaGl0eiBncmFkaWVudCwgY29udHJvbHMgc3RlcCBzaXplIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiSmVuc2VuXHUwMDI3cyBJbmVxdWFsaXR5IiwiY29udGVudCI6IkZvciBhIGNvbnZleCBmdW5jdGlvbiBmIGFuZCBhbnkgcHJvYmFiaWxpdHkgZGlzdHJpYnV0aW9uIHAoeCk6IGYoRVt4XSkg4omkIEVbZih4KV0uIFRoaXMgaXMgdGhlIGZ1bmN0aW9uYWwgZm9ybSBvZiBjb252ZXhpdHkgYW5kIHVuZGVybGllcyBFTSwgdmFyaWF0aW9uYWwgaW5mZXJlbmNlLCBhbmQgdGhlIGxvZy1zdW0tZXhwIGJvdW5kLiBFcXVhbGl0eSBob2xkcyBpZmYgeCBpcyBjb25zdGFudCBvciBmIGlzIGxpbmVhci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdHJvbmdseSBDb252ZXggRnVuY3Rpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIM68LXN0cm9uZ2x5IGNvbnZleCBmdW5jdGlvbiBjdXJ2ZXMgYXQgbGVhc3QgYXMgc2hhcnBseSBhcyBhIHF1YWRyYXRpYyB3aXRoIGN1cnZhdHVyZSDOvC4gVGhpcyBndWFyYW50ZWVzOiAoMSkgYSB1bmlxdWUgZ2xvYmFsIG1pbmltdW0sICgyKSBncmFkaWVudCBkZXNjZW50IGNvbnZlcmdlcyBhdCBhIGxpbmVhciByYXRlIE8oKDHiiJLOvC9MKeG1jyksICgzKSB0aGUgY29uZGl0aW9uIG51bWJlciDOuiA9IEwvzrwgY29udHJvbHMgY29udmVyZ2VuY2Ugc3BlZWQg4oCUIHNtYWxsZXIgzrogbWVhbnMgZmFzdGVyIGNvbnZlcmdlbmNlLiBSaWRnZSByZWdyZXNzaW9uIChMMi1yZWd1bGFyaXplZCkgaXMgc3Ryb25nbHkgY29udmV4IGV2ZW4gd2hlbiB0aGUgZGF0YSBtYXRyaXggaXMgcmFuay1kZWZpY2llbnQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IENvbnZleGl0eSBNYXR0ZXJzIGZvciBNTCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29udmV4IG9iamVjdGl2ZXMgb2ZmZXIgYWxnb3JpdGhtaWMgZ3VhcmFudGVlczogYW55IGxvY2FsIG1pbmltdW0gaXMgYSBnbG9iYWwgbWluaW11bSwgZ3JhZGllbnQgZGVzY2VudCB3aXRoIGFwcHJvcHJpYXRlIHN0ZXAgc2l6ZSBjb252ZXJnZXMsIGFuZCB3ZSBjYW4gY2VydGlmeSBvcHRpbWFsaXR5IHZpYSBkdWFsaXR5LiBOb24tY29udmV4IG9iamVjdGl2ZXMgbGFjayB0aGVzZSBndWFyYW50ZWVzIOKAlCBncmFkaWVudCBkZXNjZW50IG1heSBjb252ZXJnZSB0byBkaWZmZXJlbnQgc29sdXRpb25zIGRlcGVuZGluZyBvbiBpbml0aWFsaXphdGlvbiwgbGVhcm5pbmcgcmF0ZSwgYW5kIG5vaXNlLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIkNvbnZleCIsIlN0cm9uZ2x5IENvbnZleCIsIk5vbi1Db252ZXgiXSwicm93cyI6W1siRGVmaW5pdGlvbiIsImYozrt4KygxLc67KXkpIOKJpCDOu2YoeCkrKDEtzrspZih5KSIsImYoeSkg4omlIGYoeCkr4oiHZih4KeG1gCh5LXgpKyjOvC8yKeKAlnkteOKAlsKyIiwiTm8gZ2xvYmFsIGN1cnZhdHVyZSBndWFyYW50ZWUiXSxbIkdsb2JhbCBNaW5pbXVtIiwiQW55IGxvY2FsIG1pbiBpcyBnbG9iYWwiLCJVbmlxdWUgZ2xvYmFsIG1pbmltdW0iLCJNdWx0aXBsZSBsb2NhbCBtaW5pbWEgcG9zc2libGUiXSxbIkhlc3NpYW4iLCLiiIfCsmYg4qqwIDAgZXZlcnl3aGVyZSIsIuKIh8KyZiDiqrAgzrxJIGV2ZXJ5d2hlcmUiLCJJbmRlZmluaXRlIGluIGdlbmVyYWwiXSxbIkV4YW1wbGVzIiwiTGluZWFyIHJlZ3Jlc3Npb24sIGxvZ2lzdGljIHJlZ3Jlc3Npb24sIFNWTXMiLCJSaWRnZSByZWdyZXNzaW9uLCBlbGFzdGljIG5ldCIsIk5ldXJhbCBuZXR3b3JrcywgbWF0cml4IGZhY3Rvcml6YXRpb24iXSxbIk9wdGltaXphdGlvbiIsIkdEIGNvbnZlcmdlcyB0byBnbG9iYWwgbWluIiwiR0QgY29udmVyZ2VzLCBsaW5lYXIgcmF0ZSAxLc68L0wiLCJTR0QvQWRhbSwgbm8gY29udmVyZ2VuY2UgZ3VhcmFudGVlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21tb24gQ29udmV4IE1MIE9iamVjdGl2ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNldmVyYWwgZm91bmRhdGlvbmFsIE1MIG1vZGVscyBoYXZlIGNvbnZleCBsb3NzIGZ1bmN0aW9ucywgd2hpY2ggaXMgd2h5IHRoZXkgY2FuIGJlIHNvbHZlZCByZWxpYWJseS4gTGluZWFyIHJlZ3Jlc3Npb24gd2l0aCBzcXVhcmVkIGxvc3MgaXMgc3Ryb25nbHkgY29udmV4IHdoZW4gWCBoYXMgZnVsbCBjb2x1bW4gcmFuay4gTG9naXN0aWMgcmVncmVzc2lvbiB3aXRoIGxvZy1sb3NzIGlzIGNvbnZleCAoYnV0IG5vdCBzdHJvbmdseSBjb252ZXggd2l0aG91dCByZWd1bGFyaXphdGlvbikuIFNWTXMgd2l0aCBoaW5nZSBsb3NzIGFyZSBjb252ZXggUVBzLiBBZGRpbmcgTDIgcmVndWxhcml6YXRpb24gbWFrZXMgYW55IG9mIHRoZXNlIHN0cm9uZ2x5IGNvbnZleC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkxpbmVhciByZWdyZXNzaW9uOiBmKHcpID0g4oCWWHcgLSB54oCWwrIg4oCUIHF1YWRyYXRpYywgc3Ryb25nbHkgY29udmV4IGlmIFggZnVsbCByYW5rIiwiTG9naXN0aWMgcmVncmVzc2lvbjogZih3KSA9IM6jIGxvZygxK2V4cCgteeG1onfhtYB44bWiKSkg4oCUIGNvbnZleCwgc21vb3RoIiwiU1ZNIGhpbmdlIGxvc3M6IGYodykgPSAozrsvMinigJZ34oCWwrIgKyDOo21heCgwLDEteeG1onfhtYB44bWiKSDigJQgc3Ryb25nbHkgY29udmV4IiwiTGFzc286IGYodykgPSDigJZYdy154oCWwrIgKyDOu+KAlnfigJbigoEg4oCUIGNvbnZleCBidXQgbm9uLXNtb290aCJdfSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbiMgRGVmaW5lIGNvbnZleCBhbmQgbm9uLWNvbnZleCBmdW5jdGlvbnNcbmRlZiBjb252ZXhfZm4oeCwgeSk6XG4gICAgXCJcIlwiQ29udmV4OiBmKHgseSkgPSB4XjIgKyB5XjJcIlwiXCJcbiAgICByZXR1cm4geCoqMiArIHkqKjJcblxuZGVmIG5vbmNvbnZleF9mbih4LCB5KTpcbiAgICBcIlwiXCJOb24tY29udmV4OiBmKHgseSkgPSBzaW4oeCkqY29zKHkpICsgMC4xKih4XjIreV4yKVwiXCJcIlxuICAgIHJldHVybiBucC5zaW4oeCkgKiBucC5jb3MoeSkgKyAwLjEgKiAoeCoqMiArIHkqKjIpXG5cbmRlZiBncmFkaWVudF9kZXNjZW50KGZuX2dyYWQsIHgwLCBscj0wLjEsIHN0ZXBzPTUwKTpcbiAgICBwYXRoID0gW3gwLmNvcHkoKV1cbiAgICB4ID0geDAuY29weSgpXG4gICAgZm9yIF8gaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICB4ID0geCAtIGxyICogZm5fZ3JhZCh4KVxuICAgICAgICBwYXRoLmFwcGVuZCh4LmNvcHkoKSlcbiAgICByZXR1cm4gbnAuYXJyYXkocGF0aClcblxuZGVmIGdyYWRfY29udmV4KHgpOlxuICAgIHJldHVybiAyICogeFxuXG5kZWYgZ3JhZF9ub25jb252ZXgoeCk6XG4gICAgcmV0dXJuIG5wLmFycmF5KFtcbiAgICAgICAgbnAuY29zKHhbMF0pICogbnAuY29zKHhbMV0pICsgMC4yICogeFswXSxcbiAgICAgICAgLW5wLnNpbih4WzBdKSAqIG5wLnNpbih4WzFdKSArIDAuMiAqIHhbMV1cbiAgICBdKVxuXG4jIFJ1biBHRCBmcm9tIG11bHRpcGxlIHN0YXJ0cyBvbiB0aGUgbm9uLWNvbnZleCBzdXJmYWNlXG5zdGFydHMgPSBbbnAuYXJyYXkoWzMuMCwgMi4wXSksIG5wLmFycmF5KFstMy4wLCAyLjVdKSwgbnAuYXJyYXkoWzEuNSwgLTIuMF0pXVxucGF0aHNfbmMgPSBbZ3JhZGllbnRfZGVzY2VudChncmFkX25vbmNvbnZleCwgcywgbHI9MC4wNSkgZm9yIHMgaW4gc3RhcnRzXVxuXG5wcmludChmXCJDb252ZXggZm4gZ2xvYmFsIG1pbmltdW06IHtjb252ZXhfZm4oMCwgMCk6LjRmfVwiKVxucHJpbnQoXCJOb24tY29udmV4OiBHRCBjb252ZXJnZXMgdG8gZGlmZmVyZW50IG1pbmltYSBkZXBlbmRpbmcgb24gc3RhcnQ6XCIpXG5mb3IgaSwgcGF0aCBpbiBlbnVtZXJhdGUocGF0aHNfbmMpOlxuICAgIGZpbmFsID0gcGF0aFstMV1cbiAgICBwcmludChmXCIgIFN0YXJ0IHtzdGFydHNbaV19OiBjb252ZXJnZWQgdG8ge2ZpbmFsfSwgZj17bm9uY29udmV4X2ZuKCpmaW5hbCk6LjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5ldXJhbCBOZXR3b3JrcyBBcmUgTm9uLUNvbnZleCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmV1cmFsIG5ldHdvcmtzIGFyZSBub24tY29udmV4IGJlY2F1c2UgdGhleSBjb21wb3NlIG5vbi1saW5lYXIgYWN0aXZhdGlvbiBmdW5jdGlvbnMgd2l0aCBsZWFybmVkIHdlaWdodCBtYXRyaWNlcy4gRXZlbiBhIHNpbmdsZSBoaWRkZW4gbGF5ZXIgd2l0aCBSZUxVIGFjdGl2YXRpb25zIGNyZWF0ZXMgYSBwaWVjZXdpc2UtbGluZWFyLCBub24tY29udmV4IGxvc3Mgc3VyZmFjZS4gVGhlIG5vbi1jb252ZXhpdHkgYXJpc2VzIGZyb20gd2VpZ2h0IHNwYWNlIHN5bW1ldHJpZXMgKHBlcm11dGF0aW9uIG9mIG5ldXJvbnMpLCB0aGUgcHJvZHVjdCBzdHJ1Y3R1cmUgb2Ygd2VpZ2h0IG1hdHJpY2VzIChiaWxpbmVhciBpbnRlcmFjdGlvbnMpLCBhbmQgbm9uLWxpbmVhciBhY3RpdmF0aW9ucy4gQ3JpdGljYWwgcG9pbnRzIHdoZXJlIOKIh0w9MCBhcmUgY2xhc3NpZmllZCBieSB0aGUgSGVzc2lhbjogcG9zaXRpdmUgZGVmaW5pdGUg4oaSIGxvY2FsIG1pbiwgbmVnYXRpdmUgZGVmaW5pdGUg4oaSIGxvY2FsIG1heCwgaW5kZWZpbml0ZSDihpIgc2FkZGxlIHBvaW50LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkubGluYWxnIGltcG9ydCBlaWdoXG5cbmRlZiBjbGFzc2lmeV9jcml0aWNhbF9wb2ludChoZXNzX21hdHJpeCk6XG4gICAgXCJcIlwiQ2xhc3NpZnkgYSBjcml0aWNhbCBwb2ludCB2aWEgSGVzc2lhbiBlaWdlbnZhbHVlcy5cIlwiXCJcbiAgICBlaWdlbnZhbHVlcywgXyA9IGVpZ2goaGVzc19tYXRyaXgpXG4gICAgaWYgbnAuYWxsKGVpZ2VudmFsdWVzIFx1MDAzZSAxZS0xMCk6XG4gICAgICAgIHJldHVybiBcImxvY2FsIG1pbmltdW1cIiwgZWlnZW52YWx1ZXNcbiAgICBlbGlmIG5wLmFsbChlaWdlbnZhbHVlcyBcdTAwM2MgLTFlLTEwKTpcbiAgICAgICAgcmV0dXJuIFwibG9jYWwgbWF4aW11bVwiLCBlaWdlbnZhbHVlc1xuICAgIGVsc2U6XG4gICAgICAgIHJldHVybiBcInNhZGRsZSBwb2ludFwiLCBlaWdlbnZhbHVlc1xuXG4jIENhbm9uaWNhbCBzYWRkbGU6IGYoeCx5KSA9IHheMiAtIHleMiwgSGVzc2lhbiA9IGRpYWcoMiwgLTIpXG5IX3NhZGRsZSA9IG5wLmFycmF5KFtbMi4wLCAwLjBdLCBbMC4wLCAtMi4wXV0pXG5raW5kLCBlaWdzID0gY2xhc3NpZnlfY3JpdGljYWxfcG9pbnQoSF9zYWRkbGUpXG5wcmludChmXCJmKHgseSk9eMKyLXnCsiAgfCAgSGVzc2lhbiBlaWdlbnZhbHVlczoge2VpZ3N9ICB8ICB7a2luZH1cIilcblxuIyBJbiBoaWdoIGRpbWVuc2lvbnMsIGFsbW9zdCBhbGwgY3JpdGljYWwgcG9pbnRzIGFyZSBzYWRkbGVzXG5ucC5yYW5kb20uc2VlZCg0MilcbmZvciBuX2RpbXMgaW4gWzEwLCAxMDAsIDUwMF06XG4gICAgbl90cmlhbHMgPSAzMDBcbiAgICBzYWRkbGVfY291bnQgPSAwXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl90cmlhbHMpOlxuICAgICAgICAjIFJhbmRvbSBzeW1tZXRyaWMgbWF0cml4IHdpdGggbWl4ZWQgZWlnZW52YWx1ZXNcbiAgICAgICAgUiA9IG5wLnJhbmRvbS5yYW5kbihuX2RpbXMsIG5fZGltcylcbiAgICAgICAgSF9zeW0gPSAoUiArIFIuVCkgLyAyXG4gICAgICAgIGVpZ3NfbmQgPSBucC5saW5hbGcuZWlndmFsc2goSF9zeW0pXG4gICAgICAgIGlmIG5wLmFueShlaWdzX25kIFx1MDAzZSAwKSBhbmQgbnAuYW55KGVpZ3NfbmQgXHUwMDNjIDApOlxuICAgICAgICAgICAgc2FkZGxlX2NvdW50ICs9IDFcbiAgICBwY3QgPSAxMDAgKiBzYWRkbGVfY291bnQgLyBuX3RyaWFsc1xuICAgIHByaW50KGZcIm49e25fZGltczo0ZH06IHtwY3Q6LjFmfSUgb2YgY3JpdGljYWwgcG9pbnRzIGFyZSBzYWRkbGVzXCIpXG5cbnByaW50KFwiXFxuRGF1cGhpbiBldCBhbC4gKDIwMTQpOiBpbiBoaWdoLWRpbSBub24tY29udmV4IGZ1bmN0aW9ucyxcIilcbnByaW50KFwiY3JpdGljYWwgcG9pbnRzIGFyZSBvdmVyd2hlbG1pbmdseSBzYWRkbGUgcG9pbnRzLCBub3QgbG9jYWwgbWluaW1hLlwiKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiU2FkZGxlIFBvaW50cyBEb21pbmF0ZSBIaWdoIERpbWVuc2lvbnMiLCJjb250ZW50IjoiRGF1cGhpbiBldCBhbC4gKDIwMTQpIHNob3dlZCB0aGF0IGluIGhpZ2gtZGltZW5zaW9uYWwgbm9uLWNvbnZleCBmdW5jdGlvbnMsIG5lYXJseSBhbGwgY3JpdGljYWwgcG9pbnRzIGFyZSBzYWRkbGUgcG9pbnRzIHJhdGhlciB0aGFuIGxvY2FsIG1pbmltYS4gVGhlIHByb2JhYmlsaXR5IHRoYXQgYSByYW5kb20gY3JpdGljYWwgcG9pbnQgaXMgYSBsb2NhbCBtaW5pbXVtIGRlY3JlYXNlcyBleHBvbmVudGlhbGx5IHdpdGggZGltZW5zaW9uLiBUaGUgbG9zcyBhdCBzYWRkbGUgcG9pbnRzIGlzIGNsb3NlIHRvIHRoZSBnbG9iYWwgbWluaW11bSBmb3IgbmV1cmFsIG5ldHdvcmtzIOKAlCBlc2NhcGluZyB0aGVtIChub3QgZmluZGluZyB0aGUgZ2xvYmFsIG1pbikgaXMgdGhlIHJlYWwgY2hhbGxlbmdlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikxvc3MgTGFuZHNjYXBlIFZpc3VhbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpcmVjdGx5IHZpc3VhbGl6aW5nIHRoZSBsb3NzIGxhbmRzY2FwZSBvZiBhIG5ldXJhbCBuZXR3b3JrIGlzIGltcG9zc2libGUgKG1pbGxpb25zIG9mIHBhcmFtZXRlcnMpLCBidXQgR2FyaXBvdiBldCBhbC4gaW50cm9kdWNlZCBmaWx0ZXIgbm9ybWFsaXphdGlvbjogcHJvamVjdCBvbnRvIHR3byByYW5kb20gZGlyZWN0aW9ucyBk4oKBLCBk4oKCIHdpdGggZWFjaCBmaWx0ZXIgc2NhbGVkIHRvIG1hdGNoIHRoZSBjb3JyZXNwb25kaW5nIGZpbHRlciBub3JtIGluIHRoZSB0cmFpbmVkIHdlaWdodHMuIFRoaXMgcmVtb3ZlcyB0aGUgc2NhbGUgYW1iaWd1aXR5IGFjcm9zcyBsYXllcnMgYW5kIHByb2R1Y2VzIGludGVycHJldGFibGUgMkQgc3VyZmFjZSBwbG90cy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBmaWx0ZXJfbm9ybWFsaXplX2RpcmVjdGlvbih3ZWlnaHRzX2xpc3QpOlxuICAgIFwiXCJcIkNyZWF0ZSBhIGZpbHRlci1ub3JtYWxpemVkIHJhbmRvbSBwZXJ0dXJiYXRpb24gZGlyZWN0aW9uIChHYXJpcG92IGV0IGFsLikuXCJcIlwiXG4gICAgZGlyZWN0aW9uID0gW11cbiAgICBmb3IgdyBpbiB3ZWlnaHRzX2xpc3Q6XG4gICAgICAgIGQgPSBucC5yYW5kb20ucmFuZG4oKncuc2hhcGUpXG4gICAgICAgIGlmIGQubmRpbSBcdTAwM2U9IDI6XG4gICAgICAgICAgICAjIE5vcm1hbGl6ZSBlYWNoIGZpbHRlciAocm93KSB0byBtYXRjaCB0aGUgd2VpZ2h0IGZpbHRlciBub3JtXG4gICAgICAgICAgICBmb3IgaSBpbiByYW5nZShkLnNoYXBlWzBdKTpcbiAgICAgICAgICAgICAgICB3X25vcm0gPSBucC5saW5hbGcubm9ybSh3W2ldKSArIDFlLTEwXG4gICAgICAgICAgICAgICAgZF9ub3JtID0gbnAubGluYWxnLm5vcm0oZFtpXSkgKyAxZS0xMFxuICAgICAgICAgICAgICAgIGRbaV0gPSBkW2ldICogKHdfbm9ybSAvIGRfbm9ybSlcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIGQgPSBkICogKG5wLmxpbmFsZy5ub3JtKHcpIC8gKG5wLmxpbmFsZy5ub3JtKGQpICsgMWUtMTApKVxuICAgICAgICBkaXJlY3Rpb24uYXBwZW5kKGQpXG4gICAgcmV0dXJuIGRpcmVjdGlvblxuXG5kZWYgbGFuZHNjYXBlX2dyaWQoYmFzZV93ZWlnaHRzLCBkaXIxLCBkaXIyLCBsb3NzX2ZuLCBuPTI1LCBzY2FsZT0xLjApOlxuICAgIFwiXCJcIkV2YWx1YXRlIGxvc3Mgb24gYSAyRCBncmlkIGFyb3VuZCBiYXNlX3dlaWdodHMuXCJcIlwiXG4gICAgYWxwaGFzID0gbnAubGluc3BhY2UoLXNjYWxlLCBzY2FsZSwgbilcbiAgICBncmlkID0gbnAuemVyb3MoKG4sIG4pKVxuICAgIGZvciBpLCBhIGluIGVudW1lcmF0ZShhbHBoYXMpOlxuICAgICAgICBmb3IgaiwgYiBpbiBlbnVtZXJhdGUoYWxwaGFzKTpcbiAgICAgICAgICAgIHB3ID0gW3cgKyBhKmQxICsgYipkMiBmb3IgdywgZDEsIGQyIGluIHppcChiYXNlX3dlaWdodHMsIGRpcjEsIGRpcjIpXVxuICAgICAgICAgICAgZ3JpZFtpLCBqXSA9IGxvc3NfZm4ocHcpXG4gICAgcmV0dXJuIGFscGhhcywgZ3JpZFxuXG5ucC5yYW5kb20uc2VlZCg3KVxuYmFzZSA9IFtucC5yYW5kb20ucmFuZG4oOCwgNCkgKiAwLjMsIG5wLnJhbmRvbS5yYW5kbig4KSAqIDAuMV1cblxuZGVmIHF1YWRfbG9zcyh3cyk6XG4gICAgcmV0dXJuIHN1bShucC5zdW0odyoqMikgZm9yIHcgaW4gd3MpXG5cbmQxID0gZmlsdGVyX25vcm1hbGl6ZV9kaXJlY3Rpb24oYmFzZSlcbmQyID0gZmlsdGVyX25vcm1hbGl6ZV9kaXJlY3Rpb24oYmFzZSlcbmFscGhhcywgTCA9IGxhbmRzY2FwZV9ncmlkKGJhc2UsIGQxLCBkMiwgcXVhZF9sb3NzLCBuPTIwLCBzY2FsZT0wLjgpXG5wcmludChmXCJMYW5kc2NhcGUgZ3JpZCBzaGFwZToge0wuc2hhcGV9XCIpXG5wcmludChmXCJNaW4gbG9zczoge0wubWluKCk6LjRmfSAgTWF4IGxvc3M6IHtMLm1heCgpOi40Zn1cIilcbnByaW50KGZcIkxvc3MgYXQgY2VudGVyICgwLDApOiB7TFsxMCwxMF06LjRmfVwiKVxucHJpbnQoXCJGaWx0ZXIgbm9ybWFsaXphdGlvbiByZW1vdmVzIHNjYWxlIGFydGlmYWN0cyDigJQgaW50ZXJwcmV0YWJsZSB0b3BvbG9neS5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb2RlIENvbm5lY3Rpdml0eSBhbmQgdGhlIE5USyBSZWdpbWUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikdhcmlwb3YgZXQgYWwuIGFuZCBEcmF4bGVyIGV0IGFsLiBmb3VuZCB0aGF0IHR3byBTR0Qgc29sdXRpb25zIGNhbiBiZSBjb25uZWN0ZWQgYnkgYSBsb3ctbG9zcyBwYXRoIChtb2RlIGNvbm5lY3Rpdml0eSkuIFRoZSBsaW5lYXIgaW50ZXJwb2xhdGlvbiBiZXR3ZWVuIHR3byBzb2x1dGlvbnMgb2Z0ZW4gcGFzc2VzIHRocm91Z2ggYSBoaWdoLWxvc3MgYmFycmllciwgYnV0IGEgY3VydmVkIHBhdGggKGUuZy4sIELDqXppZXIgY3VydmUpIGNhbiBtYWludGFpbiBsb3cgbG9zcyB0aHJvdWdob3V0LiBUaGlzIHN1Z2dlc3RzIHRoZSBsb3NzIGxhbmRzY2FwZSBoYXMgY29ubmVjdGVkIHZhbGxleXMgcmF0aGVyIHRoYW4gaXNvbGF0ZWQgbWluaW1hLiBJbiB0aGUgTlRLIChOZXVyYWwgVGFuZ2VudCBLZXJuZWwpIHJlZ2ltZSDigJQgaW5maW5pdGUtd2lkdGggbmV0d29ya3MgdHJhaW5lZCB3aXRoIGluZmluaXRlc2ltYWwgbGVhcm5pbmcgcmF0ZSDigJQgdGhlIG5ldHdvcmsgYmVoYXZlcyBhcyBhIGxpbmVhciBtb2RlbCBhbmQgdGhlIGxvc3MgbGFuZHNjYXBlIGJlY29tZXMgZWZmZWN0aXZlbHkgY29udmV4LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGxpbmVhcl9pbnRlcnBvbGF0ZSh3YSwgd2IsIGFscGhhKTpcbiAgICBcIlwiXCJMaW5lYXJseSBpbnRlcnBvbGF0ZSBiZXR3ZWVuIHR3byB3ZWlnaHQgc2V0cy5cIlwiXCJcbiAgICByZXR1cm4gWygxIC0gYWxwaGEpICogYSArIGFscGhhICogYiBmb3IgYSwgYiBpbiB6aXAod2EsIHdiKV1cblxuZGVmIHBhdGhfbG9zc19wcm9maWxlKHdhLCB3YiwgbG9zc19mbiwgbl9wb2ludHM9MjUpOlxuICAgIFwiXCJcIkV2YWx1YXRlIGxvc3MgYWxvbmcgdGhlIGxpbmVhciBpbnRlcnBvbGF0aW9uIHBhdGguXCJcIlwiXG4gICAgYWxwaGFzID0gbnAubGluc3BhY2UoMCwgMSwgbl9wb2ludHMpXG4gICAgcmV0dXJuIGFscGhhcywgbnAuYXJyYXkoW2xvc3NfZm4obGluZWFyX2ludGVycG9sYXRlKHdhLCB3YiwgYSkpIGZvciBhIGluIGFscGhhc10pXG5cbmRlZiBzaW11bGF0ZV9zZ2QoaW5pdF93ZWlnaHRzLCBscj0wLjAxLCBub2lzZV9zY2FsZT0wLjE1LCBzdGVwcz0xNTApOlxuICAgIFwiXCJcIlNpbXVsYXRlIFNHRCB3aXRoIGdyYWRpZW50IG5vaXNlLCBsYW5kaW5nIGF0IGRpZmZlcmVudCBtaW5pbWEuXCJcIlwiXG4gICAgdyA9IFt4LmNvcHkoKSBmb3IgeCBpbiBpbml0X3dlaWdodHNdXG4gICAgZm9yIF8gaW4gcmFuZ2Uoc3RlcHMpOlxuICAgICAgICB3ID0gW3ggLSBsciAqICgyICogeCArIG5vaXNlX3NjYWxlICogbnAucmFuZG9tLnJhbmRuKCp4LnNoYXBlKSkgZm9yIHggaW4gd11cbiAgICByZXR1cm4gd1xuXG5ucC5yYW5kb20uc2VlZCgwKVxuaW5pdCA9IFtucC5yYW5kb20ucmFuZG4oNiwgNikgKiAxLjUsIG5wLnJhbmRvbS5yYW5kbig2KSAqIDEuNV1cbm1vZGVsX2EgPSBzaW11bGF0ZV9zZ2QoaW5pdCwgbHI9MC4wMiwgbm9pc2Vfc2NhbGU9MC4zKVxubW9kZWxfYiA9IHNpbXVsYXRlX3NnZChpbml0LCBscj0wLjAyLCBub2lzZV9zY2FsZT0wLjMpXG5cbmRlZiBsb3NzX2ZuKHdzKTpcbiAgICByZXR1cm4gc3VtKG5wLnN1bSh3KioyKSBmb3IgdyBpbiB3cylcblxuYWxwaGFzLCBsb3NzZXMgPSBwYXRoX2xvc3NfcHJvZmlsZShtb2RlbF9hLCBtb2RlbF9iLCBsb3NzX2ZuKVxubWlkID0gbG9zc2VzW2xlbihsb3NzZXMpIC8vIDJdXG5lbmRfYXZnID0gKGxvc3Nlc1swXSArIGxvc3Nlc1stMV0pIC8gMlxuYmFycmllciA9IG1pZCAtIGVuZF9hdmdcbnByaW50KGZcIk1vZGVsIEEgbG9zczoge2xvc3Nlc1swXTouNGZ9XCIpXG5wcmludChmXCJNb2RlbCBCIGxvc3M6IHtsb3NzZXNbLTFdOi40Zn1cIilcbnByaW50KGZcIk1pZHBvaW50IGxvc3M6IHttaWQ6LjRmfVwiKVxucHJpbnQoZlwiTG9zcyBiYXJyaWVyIChtaWQgLSBhdmcgZW5kcG9pbnRzKToge2JhcnJpZXI6LjRmfVwiKVxucHJpbnQoXCJMb3cgYmFycmllciA9XHUwMDNlIG1vZGUgY29ubmVjdGl2aXR5OyBtb2RlbHMgc2hhcmUgdGhlIHNhbWUgbG9zcyBiYXNpbi5cIikifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIk5USyByZWdpbWU6IGluZmluaXRlLXdpZHRoIG5ldHdvcmtzIHRyYWluZWQgd2l0aCBncmFkaWVudCBmbG93IOKGkiBsb3NzIGlzIGNvbnZleCBpbiBmdW5jdGlvbiBzcGFjZSIsIkZpbml0ZS13aWR0aCBuZXR3b3JrcyBsZWF2ZSB0aGUgTlRLIHJlZ2ltZSBxdWlja2x5OyBwcmFjdGljYWwgbGFuZHNjYXBlcyBhcmUgbm9uLWNvbnZleCIsIk1vZGUgY29ubmVjdGl2aXR5OiB0d28gU0dEIHNvbHV0aW9ucyBjb25uZWN0ZWQgYnkgYSBsb3ctbG9zcyBjdXJ2ZWQgcGF0aCAoR2FyaXBvdiAyMDE4KSIsIkxvc3MgYmFycmllciBvbiBsaW5lYXIgcGF0aCBkb2VzIG5vdCBpbXBseSBpc29sYXRpb24g4oCUIGN1cnZlZCBwYXRocyBvZnRlbiBieXBhc3MgaXQiLCJQcmFjdGljYWwgaW1wbGljYXRpb246IG1vZGVsIGF2ZXJhZ2luZyAoU1dBKSB3b3JrcyBiZWNhdXNlIHNvbHV0aW9ucyBsaWUgaW4gYSBjb25uZWN0ZWQgdmFsbGV5Il19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Convex vs Non-Convex Loss Landscapes

The geometry of the loss landscape determines whether optimization is tractable, whether gradient descent converges, and where it converges to. Convex landscapes have a single global bowl; non-convex landscapes have ridges, valleys, saddle points, and many local minima. Understanding the difference is essential for choosing optimizers, diagnosing training failures, and reasoning about generalization.

## What is a Convex Function?

A function f: ℝⁿ → ℝ is convex if for all x, y in its domain and all λ ∈ [0,1]: f(λx + (1−λ)y) ≤ λf(x) + (1−λ)f(y). Geometrically, the chord connecting any two points on the graph lies above or on the graph. Equivalently (for differentiable f): f(y) ≥ f(x) + ∇f(x)ᵀ(y−x) — the function lies above all its tangent hyperplanes. For twice-differentiable f: the Hessian ∇²f(x) ⪰ 0 (positive semidefinite) everywhere.

- Convex: f(λx+(1-λ)y) ≤ λf(x)+(1-λ)f(y) — chord lies above graph
- Strictly convex: strict inequality for x≠y — unique minimizer
- μ-strongly convex: f(y) ≥ f(x) + ∇f(x)ᵀ(y-x) + (μ/2)‖y-x‖² — quadratic lower bound guarantees unique global minimum
- L-smooth: ‖∇f(x)-∇f(y)‖ ≤ L‖x-y‖ — Lipschitz gradient, controls step size

> **Jensen's Inequality**: For a convex function f and any probability distribution p(x): f(E[x]) ≤ E[f(x)]. This is the functional form of convexity and underlies EM, variational inference, and the log-sum-exp bound. Equality holds iff x is constant or f is linear.

## Strongly Convex Functions

A μ-strongly convex function curves at least as sharply as a quadratic with curvature μ. This guarantees: (1) a unique global minimum, (2) gradient descent converges at a linear rate O((1−μ/L)ᵏ), (3) the condition number κ = L/μ controls convergence speed — smaller κ means faster convergence. Ridge regression (L2-regularized) is strongly convex even when the data matrix is rank-deficient.

## Why Convexity Matters for ML

Convex objectives offer algorithmic guarantees: any local minimum is a global minimum, gradient descent with appropriate step size converges, and we can certify optimality via duality. Non-convex objectives lack these guarantees — gradient descent may converge to different solutions depending on initialization, learning rate, and noise.

| Property | Convex | Strongly Convex | Non-Convex |
| --- | --- | --- | --- |
| Definition | f(λx+(1-λ)y) ≤ λf(x)+(1-λ)f(y) | f(y) ≥ f(x)+∇f(x)ᵀ(y-x)+(μ/2)‖y-x‖² | No global curvature guarantee |
| Global Minimum | Any local min is global | Unique global minimum | Multiple local minima possible |
| Hessian | ∇²f ⪰ 0 everywhere | ∇²f ⪰ μI everywhere | Indefinite in general |
| Examples | Linear regression, logistic regression, SVMs | Ridge regression, elastic net | Neural networks, matrix factorization |
| Optimization | GD converges to global min | GD converges, linear rate 1-μ/L | SGD/Adam, no convergence guarantee |

## Common Convex ML Objectives

Several foundational ML models have convex loss functions, which is why they can be solved reliably. Linear regression with squared loss is strongly convex when X has full column rank. Logistic regression with log-loss is convex (but not strongly convex without regularization). SVMs with hinge loss are convex QPs. Adding L2 regularization makes any of these strongly convex.

- Linear regression: f(w) = ‖Xw - y‖² — quadratic, strongly convex if X full rank
- Logistic regression: f(w) = Σ log(1+exp(-yᵢwᵀxᵢ)) — convex, smooth
- SVM hinge loss: f(w) = (λ/2)‖w‖² + Σmax(0,1-yᵢwᵀxᵢ) — strongly convex
- Lasso: f(w) = ‖Xw-y‖² + λ‖w‖₁ — convex but non-smooth

```python
import numpy as np
import matplotlib.pyplot as plt

# Define convex and non-convex functions
def convex_fn(x, y):
    """Convex: f(x,y) = x^2 + y^2"""
    return x**2 + y**2

def nonconvex_fn(x, y):
    """Non-convex: f(x,y) = sin(x)*cos(y) + 0.1*(x^2+y^2)"""
    return np.sin(x) * np.cos(y) + 0.1 * (x**2 + y**2)

def gradient_descent(fn_grad, x0, lr=0.1, steps=50):
    path = [x0.copy()]
    x = x0.copy()
    for _ in range(steps):
        x = x - lr * fn_grad(x)
        path.append(x.copy())
    return np.array(path)

def grad_convex(x):
    return 2 * x

def grad_nonconvex(x):
    return np.array([
        np.cos(x[0]) * np.cos(x[1]) + 0.2 * x[0],
        -np.sin(x[0]) * np.sin(x[1]) + 0.2 * x[1]
    ])

# Run GD from multiple starts on the non-convex surface
starts = [np.array([3.0, 2.0]), np.array([-3.0, 2.5]), np.array([1.5, -2.0])]
paths_nc = [gradient_descent(grad_nonconvex, s, lr=0.05) for s in starts]

print(f"Convex fn global minimum: {convex_fn(0, 0):.4f}")
print("Non-convex: GD converges to different minima depending on start:")
for i, path in enumerate(paths_nc):
    final = path[-1]
    print(f"  Start {starts[i]}: converged to {final}, f={nonconvex_fn(*final):.4f}")
```

## Neural Networks Are Non-Convex

Neural networks are non-convex because they compose non-linear activation functions with learned weight matrices. Even a single hidden layer with ReLU activations creates a piecewise-linear, non-convex loss surface. The non-convexity arises from weight space symmetries (permutation of neurons), the product structure of weight matrices (bilinear interactions), and non-linear activations. Critical points where ∇L=0 are classified by the Hessian: positive definite → local min, negative definite → local max, indefinite → saddle point.

```python
import numpy as np
from scipy.linalg import eigh

def classify_critical_point(hess_matrix):
    """Classify a critical point via Hessian eigenvalues."""
    eigenvalues, _ = eigh(hess_matrix)
    if np.all(eigenvalues > 1e-10):
        return "local minimum", eigenvalues
    elif np.all(eigenvalues < -1e-10):
        return "local maximum", eigenvalues
    else:
        return "saddle point", eigenvalues

# Canonical saddle: f(x,y) = x^2 - y^2, Hessian = diag(2, -2)
H_saddle = np.array([[2.0, 0.0], [0.0, -2.0]])
kind, eigs = classify_critical_point(H_saddle)
print(f"f(x,y)=x²-y²  |  Hessian eigenvalues: {eigs}  |  {kind}")

# In high dimensions, almost all critical points are saddles
np.random.seed(42)
for n_dims in [10, 100, 500]:
    n_trials = 300
    saddle_count = 0
    for _ in range(n_trials):
        # Random symmetric matrix with mixed eigenvalues
        R = np.random.randn(n_dims, n_dims)
        H_sym = (R + R.T) / 2
        eigs_nd = np.linalg.eigvalsh(H_sym)
        if np.any(eigs_nd > 0) and np.any(eigs_nd < 0):
            saddle_count += 1
    pct = 100 * saddle_count / n_trials
    print(f"n={n_dims:4d}: {pct:.1f}% of critical points are saddles")

print("\nDauphin et al. (2014): in high-dim non-convex functions,")
print("critical points are overwhelmingly saddle points, not local minima.")
```

> **Saddle Points Dominate High Dimensions**: Dauphin et al. (2014) showed that in high-dimensional non-convex functions, nearly all critical points are saddle points rather than local minima. The probability that a random critical point is a local minimum decreases exponentially with dimension. The loss at saddle points is close to the global minimum for neural networks — escaping them (not finding the global min) is the real challenge.

## Loss Landscape Visualization

Directly visualizing the loss landscape of a neural network is impossible (millions of parameters), but Garipov et al. introduced filter normalization: project onto two random directions d₁, d₂ with each filter scaled to match the corresponding filter norm in the trained weights. This removes the scale ambiguity across layers and produces interpretable 2D surface plots.

```python
import numpy as np

def filter_normalize_direction(weights_list):
    """Create a filter-normalized random perturbation direction (Garipov et al.)."""
    direction = []
    for w in weights_list:
        d = np.random.randn(*w.shape)
        if d.ndim >= 2:
            # Normalize each filter (row) to match the weight filter norm
            for i in range(d.shape[0]):
                w_norm = np.linalg.norm(w[i]) + 1e-10
                d_norm = np.linalg.norm(d[i]) + 1e-10
                d[i] = d[i] * (w_norm / d_norm)
        else:
            d = d * (np.linalg.norm(w) / (np.linalg.norm(d) + 1e-10))
        direction.append(d)
    return direction

def landscape_grid(base_weights, dir1, dir2, loss_fn, n=25, scale=1.0):
    """Evaluate loss on a 2D grid around base_weights."""
    alphas = np.linspace(-scale, scale, n)
    grid = np.zeros((n, n))
    for i, a in enumerate(alphas):
        for j, b in enumerate(alphas):
            pw = [w + a*d1 + b*d2 for w, d1, d2 in zip(base_weights, dir1, dir2)]
            grid[i, j] = loss_fn(pw)
    return alphas, grid

np.random.seed(7)
base = [np.random.randn(8, 4) * 0.3, np.random.randn(8) * 0.1]

def quad_loss(ws):
    return sum(np.sum(w**2) for w in ws)

d1 = filter_normalize_direction(base)
d2 = filter_normalize_direction(base)
alphas, L = landscape_grid(base, d1, d2, quad_loss, n=20, scale=0.8)
print(f"Landscape grid shape: {L.shape}")
print(f"Min loss: {L.min():.4f}  Max loss: {L.max():.4f}")
print(f"Loss at center (0,0): {L[10,10]:.4f}")
print("Filter normalization removes scale artifacts — interpretable topology.")
```

## Mode Connectivity and the NTK Regime

Garipov et al. and Draxler et al. found that two SGD solutions can be connected by a low-loss path (mode connectivity). The linear interpolation between two solutions often passes through a high-loss barrier, but a curved path (e.g., Bézier curve) can maintain low loss throughout. This suggests the loss landscape has connected valleys rather than isolated minima. In the NTK (Neural Tangent Kernel) regime — infinite-width networks trained with infinitesimal learning rate — the network behaves as a linear model and the loss landscape becomes effectively convex.

```python
import numpy as np

def linear_interpolate(wa, wb, alpha):
    """Linearly interpolate between two weight sets."""
    return [(1 - alpha) * a + alpha * b for a, b in zip(wa, wb)]

def path_loss_profile(wa, wb, loss_fn, n_points=25):
    """Evaluate loss along the linear interpolation path."""
    alphas = np.linspace(0, 1, n_points)
    return alphas, np.array([loss_fn(linear_interpolate(wa, wb, a)) for a in alphas])

def simulate_sgd(init_weights, lr=0.01, noise_scale=0.15, steps=150):
    """Simulate SGD with gradient noise, landing at different minima."""
    w = [x.copy() for x in init_weights]
    for _ in range(steps):
        w = [x - lr * (2 * x + noise_scale * np.random.randn(*x.shape)) for x in w]
    return w

np.random.seed(0)
init = [np.random.randn(6, 6) * 1.5, np.random.randn(6) * 1.5]
model_a = simulate_sgd(init, lr=0.02, noise_scale=0.3)
model_b = simulate_sgd(init, lr=0.02, noise_scale=0.3)

def loss_fn(ws):
    return sum(np.sum(w**2) for w in ws)

alphas, losses = path_loss_profile(model_a, model_b, loss_fn)
mid = losses[len(losses) // 2]
end_avg = (losses[0] + losses[-1]) / 2
barrier = mid - end_avg
print(f"Model A loss: {losses[0]:.4f}")
print(f"Model B loss: {losses[-1]:.4f}")
print(f"Midpoint loss: {mid:.4f}")
print(f"Loss barrier (mid - avg endpoints): {barrier:.4f}")
print("Low barrier => mode connectivity; models share the same loss basin.")
```

- NTK regime: infinite-width networks trained with gradient flow → loss is convex in function space
- Finite-width networks leave the NTK regime quickly; practical landscapes are non-convex
- Mode connectivity: two SGD solutions connected by a low-loss curved path (Garipov 2018)
- Loss barrier on linear path does not imply isolation — curved paths often bypass it
- Practical implication: model averaging (SWA) works because solutions lie in a connected valley

---

