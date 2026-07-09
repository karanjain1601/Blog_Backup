---
title: "Lagrangian Optimization and KKT Conditions"
slug: "lagrangian-kkt-conditions"
description: "Derivation of Lagrangian mechanics for equality and inequality constraints, KKT conditions with complementary slackness, strong duality via Slater's condition, SVM dual derivation, and constrained policy optimization in RL."
tags: ["optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQ29uc3RyYWluZWQgb3B0aW1pemF0aW9uIGFwcGVhcnMgdGhyb3VnaG91dCBtYWNoaW5lIGxlYXJuaW5nIGluIGZvcm1zIHRoYXQgYXJlIG5vdCBhbHdheXMgcmVjb2duaXphYmxlIGFzIHN1Y2guIFN1cHBvcnQgVmVjdG9yIE1hY2hpbmVzIG1pbmltaXplIHdlaWdodCBub3JtIHN1YmplY3QgdG8gbWFyZ2luIGNvbnN0cmFpbnRzLiBMQVNTTyByZWdyZXNzaW9uIG1pbmltaXplcyBzcXVhcmVkIGVycm9yIHN1YmplY3QgdG8gYW4gTDEgbm9ybSBidWRnZXQuIFBQTyBpbiByZWluZm9yY2VtZW50IGxlYXJuaW5nIGNvbnN0cmFpbnMgdGhlIEtMIGRpdmVyZ2VuY2UgYmV0d2VlbiBuZXcgYW5kIG9sZCBwb2xpY3kuIEZhaXJuZXNzLWF3YXJlIG1vZGVscyBjb25zdHJhaW4gdGhlIHBlcmZvcm1hbmNlIGdhcCBiZXR3ZWVuIGRlbW9ncmFwaGljIGdyb3Vwcy4gSW4gYWxsIHRoZXNlIGNhc2VzLCB0aGUgTGFncmFuZ2lhbiBmcmFtZXdvcmsgcHJvdmlkZXMgYSB1bmlmaWVkIG1hdGhlbWF0aWNhbCBsYW5ndWFnZTogcmVwbGFjZSB0aGUgY29uc3RyYWluZWQgcHJvYmxlbSB3aXRoIGFuIHVuY29uc3RyYWluZWQgTGFncmFuZ2lhbiB0aGF0IHBlbmFsaXplcyBjb25zdHJhaW50IHZpb2xhdGlvbnMsIHRoZW4gZGVyaXZlIG9wdGltYWxpdHkgY29uZGl0aW9ucyAodGhlIEtLVCBjb25kaXRpb25zKSB0aGF0IG11c3QgaG9sZCBhdCB0aGUgc29sdXRpb24uIFRoaXMgbm90ZSBidWlsZHMgZnJvbSB0aGUgZ2VvbWV0cmljIGludHVpdGlvbiBvZiBMYWdyYW5nZSBtdWx0aXBsaWVycyB0aHJvdWdoIEtLVCBjb21wbGVtZW50YXJ5IHNsYWNrbmVzcywgc3Ryb25nIGR1YWxpdHkgdmlhIFNsYXRlcidzIGNvbmRpdGlvbiwgYW5kIHRoZSBTVk0gZHVhbCBkZXJpdmF0aW9uIHRoYXQgZW5hYmxlcyB0aGUga2VybmVsIHRyaWNrLiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkVxdWFsaXR5IENvbnN0cmFpbnRzOiBMYWdyYW5nZSBNdWx0aXBsaWVycyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkNvbnNpZGVyOiBtaW5pbWl6ZSBmKHgpIHN1YmplY3QgdG8gZyh4KSA9IDAuIFRoZSBnZW9tZXRyaWMgaW5zaWdodDogYXQgdGhlIGNvbnN0cmFpbmVkIG9wdGltdW0geCosIHRoZSBncmFkaWVudCDiiIdmKHgqKSBtdXN0IGJlIHBhcmFsbGVsIHRvIOKIh2coeCopLiBJZiB0aGV5IHdlcmUgbm90IHBhcmFsbGVsLCB3ZSBjb3VsZCBtb3ZlIGFsb25nIHRoZSBjb25zdHJhaW50IHN1cmZhY2UgKGluIHRoZSBkaXJlY3Rpb24gcGVycGVuZGljdWxhciB0byDiiIdnLCBzdGF5aW5nIG9uIHRoZSBjb25zdHJhaW50KSBhbmQgZGVjcmVhc2UgZiDigJQgY29udHJhZGljdGluZyBvcHRpbWFsaXR5LiBUaGlzIHBhcmFsbGVsaXNtIGNvbmRpdGlvbiBpcyBmb3JtYWxpemVkIGJ5IHRoZSBMYWdyYW5naWFuOiBMKHgsIM67KSA9IGYoeCkgKyDOu2coeCkuIFRoZSBzdGF0aW9uYXJpdHkgY29uZGl0aW9uIOKIh194IEwgPSAwIGdpdmVzIOKIh2YgKyDOu+KIh2cgPSAwLCBpLmUuLCDiiIdmID0g4oiSzrviiIdnIChncmFkaWVudHMgYXJlIHBhcmFsbGVsIHdpdGggcmF0aW8g4oiSzrspLiBDb21iaW5lZCB3aXRoIGZlYXNpYmlsaXR5IGcoeCopID0gMCwgdGhlc2UgYXJlIG5lY2Vzc2FyeSBhbmQgc3VmZmljaWVudCBjb25kaXRpb25zIGZvciBhIGxvY2FsIG1pbmltdW0gKGZvciBzbW9vdGggZXF1YWxpdHktY29uc3RyYWluZWQgY29udmV4IHByb2JsZW1zOiBzdWZmaWNpZW50IGZvciBnbG9iYWwgbWluaW11bSkuIFRoZSBtdWx0aXBsaWVyIM67IGhhcyBhbiBlY29ub21pYyBpbnRlcnByZXRhdGlvbjogzrsgPSDiiJLiiIJmKi/iiIJjIHdoZXJlIGMgaXMgdGhlIHJpZ2h0LWhhbmQgc2lkZSBvZiBnKHgpID0gYy4gQSBwb3NpdGl2ZSDOuyBtZWFucyB0aWdodGVuaW5nIHRoZSBjb25zdHJhaW50IGluY3JlYXNlcyB0aGUgb2JqZWN0aXZlOyBhIG5lZ2F0aXZlIM67IG1lYW5zIGxvb3NlbmluZyBpdCBkb2VzLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5cbiMgQ29uc3RyYWluZWQgUVA6IG1pbmltaXplIHheMiArIHleMiBzdWJqZWN0IHRvIHggKyB5ID0gMVxuIyBBbmFseXRpY2FsIHNvbHV0aW9uOiB4KiA9IHkqID0gMC41LCBsYW1iZGEqID0gLTFcbmRlZiBvYmplY3RpdmUoeHkpOiByZXR1cm4geHlbMF0qKjIgKyB4eVsxXSoqMlxuZGVmIGNvbnN0cmFpbnRfZXEoeHkpOiByZXR1cm4geHlbMF0gKyB4eVsxXSAtIDEuMFxuXG4jIFNvbHZlIHdpdGggc2NpcHlcbnJlc3VsdCA9IG1pbmltaXplKFxuICAgIG9iamVjdGl2ZSxcbiAgICB4MD1ucC5hcnJheShbMC4wLCAwLjBdKSxcbiAgICBtZXRob2Q9J1NMU1FQJyxcbiAgICBjb25zdHJhaW50cz17J3R5cGUnOiAnZXEnLCAnZnVuJzogY29uc3RyYWludF9lcX1cbilcbnByaW50KFwiU2NpcHkgc29sdXRpb24geCo6XCIsIHJlc3VsdC54LnJvdW5kKDYpKVxucHJpbnQoXCJPYmplY3RpdmUgYXQgeCo6XCIsIHJvdW5kKHJlc3VsdC5mdW4sIDYpKVxuXG4jIFZlcmlmeSBLS1Q6IHN0YXRpb25hcml0eSDiiIdmICsgzrviiIdnID0gMFxueF9zdGFyID0gcmVzdWx0LnhcbmdmID0gbnAuYXJyYXkoWzIgKiB4X3N0YXJbMF0sIDIgKiB4X3N0YXJbMV1dKSAgIyDiiIdmXG5nZyA9IG5wLmFycmF5KFsxLjAsIDEuMF0pICAgICAgICAgICAgICAgICAgICAgICAgICMg4oiHZ1xuIyBsYW1iZGEqIHN1Y2ggdGhhdCBnZiArIGxhbWJkYSAqIGdnID0gMFxubGFtYmRhX3N0YXIgPSAtZ2ZbMF0gLyBnZ1swXVxucHJpbnQoZlwibGFtYmRhKiA9IHtsYW1iZGFfc3RhcjouNmZ9XCIpXG5wcmludChcIlN0YXRpb25hcml0eSBzYXRpc2ZpZWQ6XCIsIG5wLmFsbGNsb3NlKGdmICsgbGFtYmRhX3N0YXIgKiBnZywgMCkpXG5wcmludChcIkZlYXNpYmlsaXR5IHNhdGlzZmllZDpcIiwgbnAuaXNjbG9zZShjb25zdHJhaW50X2VxKHhfc3RhciksIDApKVxucHJpbnQoXCJBbmFseXRpY2FsIHgqOiBbMC41LCAwLjVdLCBtYXRjaGVzOlwiLCBucC5hbGxjbG9zZSh4X3N0YXIsIFswLjUsIDAuNV0pKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkluZXF1YWxpdHkgQ29uc3RyYWludHMgYW5kIEtLVCBDb25kaXRpb25zIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiRm9yIHRoZSBnZW5lcmFsIGNvbnN0cmFpbmVkIHByb2JsZW0g4oCUIG1pbmltaXplIGYoeCkgc3ViamVjdCB0byBo4rG8KHgpIOKJpCAwIGZvciBqPTEuLm0gYW5kIGfhtaIoeCkgPSAwIGZvciBpPTEuLnAg4oCUIHRoZSBMYWdyYW5naWFuIGlzIEwoeCwgzrssIM68KSA9IGYoeCkgKyDOo8674bWiZ+G1oih4KSArIM6jzrzisbxo4rG8KHgpLiBUaGUgS0tUIGNvbmRpdGlvbnMgYXJlIGZvdXIgc2V0cyBvZiByZXF1aXJlbWVudHMgdGhhdCBtdXN0IGhvbGQgYXQgYW55IGxvY2FsIG1pbmltdW0gKGdpdmVuIGNvbnN0cmFpbnQgcXVhbGlmaWNhdGlvbnMpOiAoMSkgU3RhdGlvbmFyaXR5OiDiiIdfeCBMID0g4oiHZiArIM6jzrvhtaLiiIdn4bWiICsgzqPOvOKxvOKIh2jisbwgPSAwOyAoMikgUHJpbWFsIGZlYXNpYmlsaXR5OiBo4rG8KHgqKSDiiaQgMCBhbmQgZ+G1oih4KikgPSAwIGZvciBhbGwgaiwgaTsgKDMpIER1YWwgZmVhc2liaWxpdHk6IM684rG8IOKJpSAwIGZvciBhbGwgaiAobXVsdGlwbGllcnMgZm9yIGluZXF1YWxpdHkgY29uc3RyYWludHMgbXVzdCBiZSBub24tbmVnYXRpdmUpOyAoNCkgQ29tcGxlbWVudGFyeSBzbGFja25lc3M6IM684rG8aOKxvCh4KikgPSAwIGZvciBhbGwgai4gQ29tcGxlbWVudGFyeSBzbGFja25lc3MgaXMgdGhlIGtleSBzdHJ1Y3R1cmFsIGluc2lnaHQ6IGVpdGhlciB0aGUgaW5lcXVhbGl0eSBjb25zdHJhaW50IGlzIGluYWN0aXZlICho4rG8KHgqKSA8IDAsIHN0cmljdCBzbGFjaykgYW5kIGl0cyBtdWx0aXBsaWVyIGlzIHplcm8sIE9SIHRoZSBjb25zdHJhaW50IGlzIGFjdGl2ZSAoaOKxvCh4KikgPSAwLCBiaW5kaW5nKSBhbmQgaXRzIG11bHRpcGxpZXIgY2FuIGJlIG5vbnplcm8uIFRoaXMgbWVhbnMgb25seSB0aGUgYWN0aXZlIGNvbnN0cmFpbnRzICh0aGUgYmluZGluZyBvbmVzKSBpbmZsdWVuY2UgdGhlIG9wdGltYWwgcG9pbnQgdmlhIHRoZWlyIG11bHRpcGxpZXJzLiBGb3IgY29udmV4IHByb2JsZW1zLCBLS1QgY29uZGl0aW9ucyBhcmUgYm90aCBuZWNlc3NhcnkgYW5kIHN1ZmZpY2llbnQgZm9yIGdsb2JhbCBvcHRpbWFsaXR5LiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplLCBMaW5lYXJDb25zdHJhaW50XG5cbiMgUVA6IG1pbmltaXplICh4LTMpXjIgKyAoeS00KV4yIHN1YmplY3QgdG8geCA8PSAyLCB5IDw9IDMsIHggPj0gMCwgeSA+PSAwXG4jIFJld3JpdGUgYXMgaDE6IHgtMiA8PSAwLCBoMjogeS0zIDw9IDAsIGgzOiAteCA8PSAwLCBoNDogLXkgPD0gMFxuZGVmIG9iaih4eSk6IHJldHVybiAoeHlbMF0tMykqKjIgKyAoeHlbMV0tNCkqKjJcbmNvbnN0cmFpbnRzID0gW1xuICAgIHsndHlwZSc6ICdpbmVxJywgJ2Z1bic6IGxhbWJkYSB4eTogMiAtIHh5WzBdfSwgICMgeCA8PSAyLCBhcyAyLXggPj0gMFxuICAgIHsndHlwZSc6ICdpbmVxJywgJ2Z1bic6IGxhbWJkYSB4eTogMyAtIHh5WzFdfSwgICMgeSA8PSAzXG4gICAgeyd0eXBlJzogJ2luZXEnLCAnZnVuJzogbGFtYmRhIHh5OiB4eVswXX0sICAgICAgICMgeCA+PSAwXG4gICAgeyd0eXBlJzogJ2luZXEnLCAnZnVuJzogbGFtYmRhIHh5OiB4eVsxXX0sICAgICAgICMgeSA+PSAwXG5dXG5yZXMgPSBtaW5pbWl6ZShvYmosIFsxLjAsIDEuMF0sIG1ldGhvZD0nU0xTUVAnLCBjb25zdHJhaW50cz1jb25zdHJhaW50cylcbnhfc3RhciA9IHJlcy54XG5wcmludChcIlNvbHV0aW9uIHgqOlwiLCB4X3N0YXIucm91bmQoNCksIFwiKGV4cGVjdGVkOiBbMiwgM10pXCIpXG5cbiMgVmVyaWZ5IEtLVCBtYW51YWxseVxuZ2YgPSBucC5hcnJheShbMiooeF9zdGFyWzBdLTMpLCAyKih4X3N0YXJbMV0tNCldKVxuaF92YWxzID0gWzIteF9zdGFyWzBdLCAzLXhfc3RhclsxXSwgeF9zdGFyWzBdLCB4X3N0YXJbMV1dXG5wcmludChcIkNvbnN0cmFpbnQgdmFsdWVzIChzaG91bGQgYmUgPj0gMCk6XCIsIFtyb3VuZChoLCA0KSBmb3IgaCBpbiBoX3ZhbHNdKVxucHJpbnQoXCJBY3RpdmUgY29uc3RyYWludHMgKGg9MCk6XCIsIFtpIGZvciBpLCBoIGluIGVudW1lcmF0ZShoX3ZhbHMpIGlmIGFicyhoKSA8IDFlLTVdKVxucHJpbnQoXCJQcmltYWwgZmVhc2liaWxpdHk6XCIsIGFsbChoID49IC0xZS02IGZvciBoIGluIGhfdmFscykpXG5wcmludChcIkdyYWRpZW50IOKIh2YgYXQgeCo6XCIsIGdmLnJvdW5kKDQpLCBcIihzaG91bGQgYmUgbm9uLXplcm8sIG9mZnNldCBieSBhY3RpdmUgY29uc3RyYWludHMpXCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiU3Ryb25nIER1YWxpdHkgYW5kIFNsYXRlcidzIENvbmRpdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBMYWdyYW5naWFuIGR1YWwgZnVuY3Rpb24gZyjOuywgzrwpID0gbWluX3ggTCh4LCDOuywgzrwpIGlzIGFsd2F5cyBjb25jYXZlIGluICjOuywgzrwpIChhcyBhIHBvaW50d2lzZSBtaW5pbXVtIG9mIGFmZmluZSBmdW5jdGlvbnMpLiBXZWFrIGR1YWxpdHkgc3RhdGVzIGcozrssIM68KSDiiaQgZih4KikgYWx3YXlzIOKAlCB0aGUgZHVhbCBvYmplY3RpdmUgaXMgYWx3YXlzIGEgbG93ZXIgYm91bmQgb24gdGhlIHByaW1hbCBvcHRpbXVtLiBUaGUgZHVhbGl0eSBnYXAgaXMgZih4Kikg4oiSIGcozrsqLCDOvCopIOKJpSAwLiBTdHJvbmcgZHVhbGl0eSAoemVybyBkdWFsaXR5IGdhcCkgbWVhbnMgZyjOuyosIM68KikgPSBmKHgqKSDigJQgdGhlIGR1YWwgY2FuIGJlIHNvbHZlZCB0byByZWNvdmVyIHRoZSBwcmltYWwgc29sdXRpb24uIFNsYXRlcidzIGNvbmRpdGlvbjogZm9yIGEgY29udmV4IHByaW1hbCBwcm9ibGVtLCBzdHJvbmcgZHVhbGl0eSBob2xkcyBpZiB0aGVyZSBleGlzdHMgYSBzdHJpY3RseSBmZWFzaWJsZSBwb2ludCB4zIQgd2l0aCBo4rG8KHjMhCkgPCAwIChzdHJpY3RseSkgZm9yIGFsbCBqLiBTbGF0ZXIncyBjb25kaXRpb24gaXMgc2F0aXNmaWVkIGJ5IGFsbW9zdCBhbGwgd2VsbC1wb3NlZCBjb252ZXggTUwgcHJvYmxlbXMgKGl0IGZhaWxzIG9ubHkgb24gZGVnZW5lcmF0ZSBjb25zdHJhaW50cykuIFdoZW4gc3Ryb25nIGR1YWxpdHkgaG9sZHMsIHdlIGNhbiBzb2x2ZSB0aGUgZHVhbCAob2Z0ZW4gYSBzaW1wbGVyIHByb2JsZW0pIGluc3RlYWQgb2YgdGhlIHByaW1hbC4gVGhlIGR1YWwgcHJvYmxlbSBpcyBhbHdheXMgY29udmV4ICh3ZSBhcmUgbWF4aW1pemluZyBhIGNvbmNhdmUgZnVuY3Rpb24pLCBldmVuIGlmIHRoZSBwcmltYWwgd2FzIG5vbi1jb252ZXgg4oCUIHRoaXMgaXMgaG93IFNWTSdzIG5vbi1saW5lYXIgZm9ybXVsYXRpb25zIGJlY29tZSB0cmFjdGFibGUgdmlhIHRoZSBrZXJuZWwgdHJpY2suIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiU1ZNIER1YWwgRGVyaXZhdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlNWTSBwcmltYWw6IG1pbmltaXplIMK94oCWd+KAlsKyIHN1YmplY3QgdG8geeG1oih34bWAeOG1oiArIGIpIOKJpSAxIGZvciBhbGwgaSAoZXF1aXZhbGVudGx5LCBo4bWiKHcsYikgPSAxIOKIkiB54bWiKHfhtYB44bWiK2IpIOKJpCAwKS4gTGFncmFuZ2lhbjogTCA9IMK94oCWd+KAlsKyIOKIkiDOo86x4bWiW3nhtaIod+G1gHjhtaIrYikg4oiSIDFdIHdpdGggzrHhtaIg4omlIDAuIEtLVCBzdGF0aW9uYXJpdHkgd2l0aCByZXNwZWN0IHRvIHc6IOKIgkwv4oiCdyA9IHcg4oiSIM6jzrHhtaJ54bWiWOG1oiA9IDAsIHNvIHcqID0gzqPOseG1onnhtaJ44bWiLiBXaXRoIHJlc3BlY3QgdG8gYjog4oiCTC/iiIJiID0g4oiSzqPOseG1onnhtaIgPSAwLCBzbyDOo86x4bWieeG1oiA9IDAuIFN1YnN0aXR1dGluZyB3KiBiYWNrIGludG8gTCBhbmQgc2ltcGxpZnlpbmcgZ2l2ZXMgdGhlIGR1YWw6IG1heGltaXplIEQozrEpID0gzqPOseG1oiDiiJIgwr3Oo+G1ouKxvCDOseG1os6x4rG8eeG1onnisbx44bWi4bWAeOKxvCBzdWJqZWN0IHRvIM6x4bWiIOKJpSAwIGFuZCDOo86x4bWieeG1oiA9IDAuIFRoaXMgaXMgYSBRUCBpbiBuIHZhcmlhYmxlcyAodHJhaW5pbmcgc2FtcGxlcykgaW5zdGVhZCBvZiBkIHZhcmlhYmxlcyAoZmVhdHVyZXMpLiBXaGVuIG4gPCBkLCB0aGUgZHVhbCBpcyBjaGVhcGVyOyBmb3IgbiA+IGQsIHRoZSBwcmltYWwgd2lucy4gTW9yZSBpbXBvcnRhbnRseSwgeOG1ouG1gHjisbwgYXBwZWFycyBvbmx5IGFzIGFuIGlubmVyIHByb2R1Y3QsIHdoaWNoIGNhbiBiZSByZXBsYWNlZCBieSBhbnkga2VybmVsIEsoeOG1oiwgeOKxvCkgPSDPhih44bWiKeG1gM+GKHjisbwpIOKAlCBhbGxvd2luZyBub24tbGluZWFyIGRlY2lzaW9uIGJvdW5kYXJpZXMgd2l0aG91dCBleHBsaWNpdGx5IGNvbXB1dGluZyDPhih4KS4gQnkgS0tUIGNvbXBsZW1lbnRhcnkgc2xhY2tuZXNzOiDOseG1osK3W3nhtaIod+G1gHjhtaIrYiniiJIxXSA9IDAsIHNvIGVpdGhlciDOseG1oiA9IDAgKHBvaW50IGlzIG5vdCBhIHN1cHBvcnQgdmVjdG9yLCBub3Qgb24gdGhlIG1hcmdpbikgb3IgeeG1oih34bWAeOG1oitiKSA9IDEgKHBvaW50IGlzIG9uIHRoZSBtYXJnaW4sIGlzIGEgc3VwcG9ydCB2ZWN0b3IpLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5mcm9tIHNrbGVhcm4uc3ZtIGltcG9ydCBTVkNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuXG4jIEdlbmVyYXRlIGxpbmVhcmx5IHNlcGFyYWJsZSBkYXRhXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHlfcmF3ID0gbWFrZV9ibG9icyhuX3NhbXBsZXM9MzAsIGNlbnRlcnM9MiwgcmFuZG9tX3N0YXRlPTApXG55ID0gMiAqIHlfcmF3IC0gMSAgIyBjb252ZXJ0IHRvIHstMSwgKzF9XG5uID0gbGVuKHkpXG5cbiMgU1ZNIGR1YWw6IG1heGltaXplIM6jzrHhtaIgLSDCvc6j4bWi4rG8IM6x4bWizrHisbx54bWieeKxvHjhtaLhtYB44rG8XG5LID0gKHlbOiwgTm9uZV0gKiBYKSBAICh5WzosIE5vbmVdICogWCkuVCAgIyBHcmFtIG1hdHJpeCB3aXRoIGxhYmVsc1xuZGVmIG5lZ19kdWFsKGFscGhhKTogcmV0dXJuIDAuNSAqIGFscGhhIEAgSyBAIGFscGhhIC0gYWxwaGEuc3VtKClcbmRlZiBuZWdfZHVhbF9ncmFkKGFscGhhKTogcmV0dXJuIEsgQCBhbHBoYSAtIG5wLm9uZXMobilcblxucmVzdWx0ID0gbWluaW1pemUoXG4gICAgbmVnX2R1YWwsIHgwPW5wLnplcm9zKG4pLCBqYWM9bmVnX2R1YWxfZ3JhZCwgbWV0aG9kPSdTTFNRUCcsXG4gICAgYm91bmRzPVsoMCwgTm9uZSldICogbixcbiAgICBjb25zdHJhaW50cz17J3R5cGUnOiAnZXEnLCAnZnVuJzogbGFtYmRhIGE6IChhICogeSkuc3VtKCl9XG4pXG5hbHBoYSA9IHJlc3VsdC54XG53ID0gKGFscGhhICogeSkgQCBYXG5zdl9tYXNrID0gYWxwaGEgPiAxZS00XG5wcmludChmXCJTdXBwb3J0IHZlY3RvcnM6IHtzdl9tYXNrLnN1bSgpfSAvIHtufVwiKVxucHJpbnQoXCJ3IChkdWFsKTpcIiwgdy5yb3VuZCg0KSlcbnNrbGVhcm5fc3ZtID0gU1ZDKGtlcm5lbD0nbGluZWFyJywgQz0xZTYpXG5za2xlYXJuX3N2bS5maXQoWCwgeV9yYXcpXG5wcmludChcIncgKHNrbGVhcm4pOlwiLCBza2xlYXJuX3N2bS5jb2VmXy5yb3VuZCg0KSlcbnByaW50KFwiQ29tcGxlbWVudGFyeSBzbGFja25lc3MgY2hlY2s6XCIpXG5tYXJnaW5zID0geSAqIChYIEAgdylcbnByaW50KFwiICDOsT0wIHBvaW50cyBvbiBtYXJnaW4/XCIsIGFsbChtYXJnaW5zW35zdl9tYXNrXSA+PSAwLjk5KSkifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNTCBDb25uZWN0aW9uczogQ29uc3RyYWluZWQgUkwgYW5kIEZhaXIgTUwifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJLS1QgY29uZGl0aW9ucyBhbmQgdGhlIExhZ3JhbmdpYW4gZnJhbWV3b3JrIGFwcGVhciBpbiBtb2Rlcm4gTUwgYmV5b25kIFNWTS4gSW4gcmVpbmZvcmNlbWVudCBsZWFybmluZzogUFBPIChQcm94aW1hbCBQb2xpY3kgT3B0aW1pemF0aW9uKSBlbmZvcmNlcyBhIHRydXN0IHJlZ2lvbiB2aWEgYSBLTCBwZW5hbHR5IChzb2Z0IGNvbnN0cmFpbnQpOyBDUE8gKENvbnN0cmFpbmVkIFBvbGljeSBPcHRpbWl6YXRpb24sIEFjaGlhbSBldCBhbC4gMjAxNykgZm9ybXVsYXRlcyBzYWZldHkgUkwgYXMgbWluaW1pemUg4oiSRVtyZXdhcmRdIHN1YmplY3QgdG8gRVtjb3N0XSDiiaQgZCwgc29sdmVkIHZpYSBLS1Qgd2l0aCB0aGUgTGFncmFuZ2UgbXVsdGlwbGllciB1cGRhdGVkIGJ5IGR1YWwgZ3JhZGllbnQgYXNjZW50OiDOuyDihpAgbWF4KDAsIM67ICsgzrEoRVtjb3N0XSDiiJIgZCkpLiBUaGUgbXVsdGlwbGllciDOuyBiZWNvbWVzIHRoZSBzYWZldHkgcGVuYWx0eSBjb2VmZmljaWVudCwgYXV0b21hdGljYWxseSBhZGFwdGluZyB0byBjb25zdHJhaW50IHZpb2xhdGlvbnMuIEluIGZhaXIgTUw6IGRlbW9ncmFwaGljIHBhcml0eSBjb25zdHJhaW50cyByZXF1aXJlIGVxdWFsIGFjY3VyYWN5IGFjcm9zcyBncm91cHMsIGZvcm11bGF0ZWQgYXMgbWluaW1pemUgTCjOuCkgc3ViamVjdCB0byB8YWNjX2dyb3VwMSDiiJIgYWNjX2dyb3VwMnwg4omkIM61OyBzb2x2ZWQgdmlhIGF1Z21lbnRlZCBMYWdyYW5naWFuIG9yIHByb2plY3RlZCBncmFkaWVudCBkZXNjZW50LiBMQVNTTyBhcyBhIGNvbnN0cmFpbmVkIHByb2JsZW06IHRoZSBzdGFuZGFyZCBMYWdyYW5naWFuIGZvcm11bGF0aW9uIG1pbmltaXplIOKAlljOsuKIknnigJbCsiArIM674oCWzrLigJbigoEgY29ycmVzcG9uZHMgZXhhY3RseSB0byBtaW5pbWl6ZSDigJZYzrLiiJJ54oCWwrIgc3ViamVjdCB0byDigJbOsuKAluKCgSDiiaQgdCwgd2hlcmUgdGhlIG11bHRpcGxpZXIgzrsgaXMgdGhlIGR1YWwgdmFyaWFibGUgZm9yIHRoZSBMMSBidWRnZXQgY29uc3RyYWludCB0LiBEaWZmZXJlbnQgdmFsdWVzIG9mIM67IHRyYWNlIHRoZSBMQVNTTyByZWd1bGFyaXphdGlvbiBwYXRoLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGR1YWxfZ3JhZGllbnRfYXNjZW50KGZfcHJpbWFsLCBncmFkX2YsIGNvbnN0cmFpbnQsIGdyYWRfY29uc3RyYWludCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgeDAsIGxyX3ByaW1hbD0wLjAxLCBscl9kdWFsPTAuMSwgc3RlcHM9MjAwKTpcbiAgICBcIlwiXCJQcmltYWwtZHVhbCBvcHRpbWl6YXRpb246IG1pbiBmKHgpIHMudC4gYyh4KSA8PSAwLlwiXCJcIlxuICAgIHggPSB4MC5jb3B5KClcbiAgICBsYW0gPSAwLjAgICMgZHVhbCB2YXJpYWJsZSAobXVsdGlwbGllcilcbiAgICBoaXN0b3J5ID0gW11cbiAgICBmb3Igc3RlcCBpbiByYW5nZShzdGVwcyk6XG4gICAgICAgICMgUHJpbWFsIHN0ZXA6IGdyYWRpZW50IGRlc2NlbnQgb24gTGFncmFuZ2lhbiBMID0gZih4KSArIGxhbWJkYSAqIGMoeClcbiAgICAgICAgTF9ncmFkID0gZ3JhZF9mKHgpICsgbGFtICogZ3JhZF9jb25zdHJhaW50KHgpXG4gICAgICAgIHggPSB4IC0gbHJfcHJpbWFsICogTF9ncmFkXG4gICAgICAgICMgRHVhbCBzdGVwOiBncmFkaWVudCBhc2NlbnQgb24gZHVhbCAobWF4aW1pemUgb3ZlciBsYW1iZGEgPj0gMClcbiAgICAgICAgY29uc3RyYWludF92YWwgPSBjb25zdHJhaW50KHgpXG4gICAgICAgIGxhbSA9IG1heCgwLjAsIGxhbSArIGxyX2R1YWwgKiBjb25zdHJhaW50X3ZhbClcbiAgICAgICAgaGlzdG9yeS5hcHBlbmQoeydzdGVwJzogc3RlcCwgJ2YnOiBmX3ByaW1hbCh4KSxcbiAgICAgICAgICAgICAgICAgICAgICAgICdjJzogY29uc3RyYWludF92YWwsICdsYW1iZGEnOiBsYW19KVxuICAgIHJldHVybiB4LCBsYW0sIGhpc3RvcnlcblxuIyBFeGFtcGxlOiBtaW5pbWl6ZSB4XjIgKyB5XjIgc3ViamVjdCB0byB4ICsgeSA+PSAyIChyZXdyaXR0ZW4gYXMgMi14LXkgPD0gMClcbmYgPSBsYW1iZGEgeHk6IHh5WzBdKioyICsgeHlbMV0qKjJcbmdyYWRfZiA9IGxhbWJkYSB4eTogMiAqIHh5XG5jID0gbGFtYmRhIHh5OiAyIC0geHlbMF0gLSB4eVsxXSAgICMgY29uc3RyYWludDogMiAtIHggLSB5IDw9IDBcbmdyYWRfYyA9IGxhbWJkYSB4eTogbnAuYXJyYXkoWy0xLjAsIC0xLjBdKVxuXG5ucC5yYW5kb20uc2VlZCgwKVxueF9zb2wsIGxhbV9zb2wsIGhpc3QgPSBkdWFsX2dyYWRpZW50X2FzY2VudChcbiAgICBmLCBncmFkX2YsIGMsIGdyYWRfYywgeDA9bnAuYXJyYXkoWzAuMSwgMC4xXSkpXG5wcmludChmXCJQcmltYWwgc29sdXRpb24geCo6IHt4X3NvbC5yb3VuZCg0KX0gKGV4cGVjdGVkIFsxLCAxXSlcIilcbnByaW50KGZcIkxhbWJkYSogPSB7bGFtX3NvbDouNGZ9IChleHBlY3RlZCAyLjAsIG1hcmdpbmFsIGNvc3Qgb2YgY29uc3RyYWludClcIilcbnByaW50KGZcIkNvbnN0cmFpbnQgc2F0aXNmaWVkOiB7Yyh4X3NvbCk6LjRmfSA8PSAwXCIpXG5wcmludChmXCJGaW5hbCBvYmplY3RpdmU6IHtmKHhfc29sKTouNGZ9IChleHBlY3RlZCAyLjApXCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiSW1wbGVtZW50YXRpb24gUGl0ZmFsbHMifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJDcml0aWNhbCBwaXRmYWxscyBpbiBjb25zdHJhaW5lZCBvcHRpbWl6YXRpb24gZm9yIE1MLiBGaXJzdCwgY29uZnVzaW5nIG5lY2Vzc2FyeSBhbmQgc3VmZmljaWVudCBjb25kaXRpb25zOiBLS1QgY29uZGl0aW9ucyBhcmUgbmVjZXNzYXJ5IGZvciBsb2NhbCBtaW5pbWEgdW5kZXIgY29uc3RyYWludCBxdWFsaWZpY2F0aW9ucyAobGlrZSBMSUNROiBMaW5lYXIgSW5kZXBlbmRlbmNlIENvbnN0cmFpbnQgUXVhbGlmaWNhdGlvbikgYnV0IG9ubHkgc3VmZmljaWVudCBmb3IgY29udmV4IHByb2JsZW1zLiBGb3Igbm9uLWNvbnZleCBwcm9ibGVtcyAoZGVlcCBSTCBjb25zdHJhaW50cywgbm9uLWxpbmVhciBmYWlybmVzcyBjb25zdHJhaW50cyksIGEgS0tUIHBvaW50IG1heSBiZSBhIHNhZGRsZSBvZiB0aGUgTGFncmFuZ2lhbiByYXRoZXIgdGhhbiBhIG1pbmltdW0uIFNlY29uZCwgdGhlIGR1YWwgZ3JhZGllbnQgYXNjZW50IHN0ZXAgc2l6ZSAobHJfZHVhbCkgbXVzdCBiZSBjaG9zZW4gY2FyZWZ1bGx5OiB0b28gbGFyZ2UgY2F1c2VzIG9zY2lsbGF0aW9ucyBpbiB0aGUgbXVsdGlwbGllciDOuyB3aXRob3V0IGNvbnZlcmdlbmNlOyB0b28gc21hbGwgY29udmVyZ2VzIGV4dHJlbWVseSBzbG93bHkgdG8gdGhlIGZlYXNpYmxlIHJlZ2lvbi4gVGhlIGR1YWwgc3RlcCBzaXplIGlzIHR5cGljYWxseSBzZXQgMTAtMTAww5cgc21hbGxlciB0aGFuIHRoZSBwcmltYWwgc3RlcCBzaXplLiBUaGlyZCwgZm9yIGVxdWFsaXR5IGNvbnN0cmFpbnRzLCBtdWx0aXBsaWVycyBhcmUgdW5jb25zdHJhaW5lZCAoY2FuIGJlIHBvc2l0aXZlIG9yIG5lZ2F0aXZlKTsgZm9yIGluZXF1YWxpdHkgY29uc3RyYWludHMsIG11bHRpcGxpZXJzIG11c3QgYmUgbm9uLW5lZ2F0aXZlIOKAlCBlbmZvcmNpbmcgdGhpcyB2aWEgbWF4KDAsIM67ICsgzrHCt2MoeCkpIGlzIHRoZSBwcm9qZWN0ZWQgZHVhbCB1cGRhdGUuIEZvcmdldHRpbmcgdGhlIHByb2plY3Rpb24gZ2l2ZXMgaW5jb3JyZWN0IG11bHRpcGxpZXJzIGFuZCBpbnZhbGlkIGNvbnN0cmFpbnQgaGFuZGxpbmcuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiUHJhY3RpY2FsIEd1aWRhbmNlIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiUHJhY3RpY2FsIGd1aWRlbGluZXMgZm9yIGNvbnN0cmFpbmVkIG9wdGltaXphdGlvbiBpbiBNTC4gRm9yIGNvbnZleCBwcm9ibGVtcyAoU1ZNLCBMMSByZWdyZXNzaW9uLCBsaW5lYXIgZmFpcm5lc3MgY29uc3RyYWludHMpOiB1c2UgZXN0YWJsaXNoZWQgc29sdmVycyAoc2NpcHkub3B0aW1pemUubWluaW1pemUgd2l0aCBTTFNRUCwgQ1ZYUFksIG9yIHNwZWNpYWxpemVkIFFQIHNvbHZlcnMpIOKAlCB0aGV5IGltcGxlbWVudCBpbnRlcmlvci1wb2ludCBtZXRob2RzIHdpdGggcHJvdmVuIGNvbnZlcmdlbmNlLiBGb3IgY29uc3RyYWluZWQgUkwgKHNhZmV0eSBjb25zdHJhaW50cywgS0wgdHJ1c3QgcmVnaW9ucyk6IHVzZSBkdWFsIGdyYWRpZW50IGFzY2VudCB3aXRoIGEgc2VwYXJhdGUgZHVhbCBsZWFybmluZyByYXRlLCBjbGlwIHRoZSBkdWFsIHZhcmlhYmxlIHRvIHByZXZlbnQgaXQgZnJvbSBncm93aW5nIHVuYm91bmRlZGx5IChtYXhfbGFtYmRhIGh5cGVycGFyYW1ldGVyKSwgYW5kIG1vbml0b3IgYm90aCB0aGUgcHJpbWFsIG9iamVjdGl2ZSBhbmQgY29uc3RyYWludCB2aW9sYXRpb24gc2VwYXJhdGVseSBpbiB0cmFpbmluZyBsb2dzLiBGb3IgTEFTU08gYW5kIGdyb3VwLXNwYXJzZSByZWd1bGFyaXphdGlvbjogdXNlIHRoZSBMYWdyYW5naWFuIGZvcm0gd2l0aCDOuyBhcyBhIGh5cGVycGFyYW1ldGVyIChlcXVpdmFsZW50IHRvIHRoZSBjb25zdHJhaW5lZCBmb3JtIGJ5IHN0cm9uZyBkdWFsaXR5KSByYXRoZXIgdGhhbiB0aGUgY29uc3RyYWluZWQgZm9ybSwgYXMgY29vcmRpbmF0ZSBkZXNjZW50IGFuZCBwcm94aW1hbCBhbGdvcml0aG1zIGFyZSBtb3JlIGVmZmljaWVudCBmb3IgTDEuIEFsd2F5cyB2ZXJpZnkgU2xhdGVyJ3MgY29uZGl0aW9uIGJlZm9yZSBhc3N1bWluZyBzdHJvbmcgZHVhbGl0eTogY2hlY2sgdGhhdCBhIHN0cmljdGx5IGZlYXNpYmxlIHBvaW50IGV4aXN0czsgaWYgdGhlIGNvbnN0cmFpbnQgaXMgYW4gZXF1YWxpdHkgKGjisbwgPSAwKSwgU2xhdGVyIGRvZXMgbm90IGFwcGx5IGFuZCBhZGRpdGlvbmFsIGNvbmRpdGlvbnMgYXJlIG5lZWRlZC4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidGl0bGUiOiAiV2FybmluZyIsICJjb250ZW50IjogIktLVCBjb25kaXRpb25zIGFyZSBuZWNlc3NhcnkgYnV0IE5PVCBzdWZmaWNpZW50IGZvciBub24tY29udmV4IHByb2JsZW1zLiBGb3IgYSBub24tY29udmV4IG9iamVjdGl2ZSB3aXRoIGNvbnN0cmFpbnRzLCBhIHBvaW50IHNhdGlzZnlpbmcgS0tUIGNvdWxkIGJlIGEgc2FkZGxlIHBvaW50IG9mIHRoZSBMYWdyYW5naWFuLCBhIGxvY2FsIG1pbmltdW0gdGhhdCBpcyBub3QgZ2xvYmFsLCBvciBldmVuIGEgbG9jYWwgbWF4aW11bSBvZiB0aGUgTGFncmFuZ2lhbi4gQWx3YXlzIHZlcmlmeSBzZWNvbmQtb3JkZXIgc3VmZmljaWVuY3kgY29uZGl0aW9uczogdGhlIExhZ3JhbmdpYW4gSGVzc2lhbiDiiIfCskwgbXVzdCBiZSBwb3NpdGl2ZSBzZW1pZGVmaW5pdGUgb24gdGhlIHRhbmdlbnQgc3BhY2Ugb2YgYWN0aXZlIGNvbnN0cmFpbnRzLiBGb3IgUkwgYW5kIGZhaXJuZXNzIGNvbnN0cmFpbnRzICh0eXBpY2FsbHkgbm9uLWNvbnZleCksIHRyZWF0IGR1YWwgZ3JhZGllbnQgYXNjZW50IGFzIGEgaGV1cmlzdGljIGFuZCBtb25pdG9yIGNvbnN0cmFpbnQgc2F0aXNmYWN0aW9uIGVtcGlyaWNhbGx5IHJhdGhlciB0aGFuIHJlbHlpbmcgb24gdGhlb3JldGljYWwgZ3VhcmFudGVlcy4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIk1ldGhvZCIsICJIYW5kbGVzIEVxdWFsaXR5IiwgIkhhbmRsZXMgSW5lcXVhbGl0eSIsICJDb252ZXJnZW5jZSIsICJNTCBVc2UgQ2FzZSJdLCAicm93cyI6IFtbIkxhZ3JhbmdlIG11bHRpcGxpZXJzIiwgIlllcyIsICJObyIsICJOZXd0b24gcmF0ZSAobG9jYWwpIiwgIlNWTSwgcGh5c2ljcyBjb25zdHJhaW50cyJdLCBbIktLVCArIE5ld3RvbiIsICJZZXMiLCAiWWVzIiwgIlF1YWRyYXRpYyAobG9jYWwpIiwgIlNtYWxsIFFQcywgU1ZNIl0sIFsiUHJvamVjdGVkIEdEIiwgIlZpYSBwcm9qZWN0aW9uIiwgIlllcyAoc2ltcGxlIHNldHMpIiwgIk8oMS90KSIsICJMMi1iYWxsIGNvbnN0cmFpbnRzLCBzaW1wbGV4Il0sIFsiQXVnbWVudGVkIExhZ3JhbmdpYW4iLCAiWWVzIiwgIlllcyIsICJTdXBlcmxpbmVhciIsICJGYWlybmVzcyBNTCwgQURNTSJdLCBbIkludGVyaW9yIHBvaW50IiwgIlllcyIsICJZZXMgKHN0cmljdCBpbmVxKSIsICJQb2x5bm9taWFsIiwgIkxhcmdlLXNjYWxlIFFQIChTVk0gd2l0aCBzb2Z0IG1hcmdpbikiXSwgWyJQZW5hbHR5IG1ldGhvZCIsICJZZXMgKGFwcHJveCkiLCAiWWVzIChhcHByb3gpIiwgIkRlcGVuZHMgb24gcGVuYWx0eSIsICJRdWljayBwcm90b3R5cGVzLCBQUE8gS0wgcGVuYWx0eSJdXX0sIHsidHlwZSI6ICJkaXZpZGVyIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2V5IFRha2Vhd2F5cyJ9LCB7InR5cGUiOiAibGlzdCIsICJpdGVtcyI6IFsiTGFncmFuZ2UgbXVsdGlwbGllcnMgY29udmVydCBlcXVhbGl0eS1jb25zdHJhaW5lZCBwcm9ibGVtcyB0byB1bmNvbnN0cmFpbmVkIG9uZXM7IHRoZSBvcHRpbWFsaXR5IGNvbmRpdGlvbiDiiIdmID0g4oiSzrviiIdnIGNhcHR1cmVzIGdyYWRpZW50IGFsaWdubWVudCBhdCB0aGUgY29uc3RyYWluZWQgb3B0aW11bS4iLCAiS0tUIGNvbmRpdGlvbnMgZ2VuZXJhbGl6ZSBMYWdyYW5nZSBtdWx0aXBsaWVycyB0byBpbmVxdWFsaXR5IGNvbnN0cmFpbnRzOiBzdGF0aW9uYXJpdHksIHByaW1hbCBmZWFzaWJpbGl0eSwgZHVhbCBmZWFzaWJpbGl0eSAozrzisbwg4omlIDApLCBhbmQgY29tcGxlbWVudGFyeSBzbGFja25lc3MgKM684rG8aOKxvCA9IDApLiIsICJDb21wbGVtZW50YXJ5IHNsYWNrbmVzcyBtZWFucyBvbmx5IGFjdGl2ZSBjb25zdHJhaW50cyAoaOKxvCA9IDApIGhhdmUgbm9uemVybyBtdWx0aXBsaWVycyDigJQgaW5hY3RpdmUgY29uc3RyYWludHMgYXJlIGlycmVsZXZhbnQgYXQgdGhlIG9wdGltdW0uIiwgIlNsYXRlcidzIGNvbmRpdGlvbiAoc3RyaWN0IGludGVyaW9yIHBvaW50IGV4aXN0cykgZ3VhcmFudGVlcyBzdHJvbmcgZHVhbGl0eSBmb3IgY29udmV4IHByb2JsZW1zOiB0aGUgZHVhbCBvYmplY3RpdmUgZXF1YWxzIHRoZSBwcmltYWwgbWluaW11bSwgZW5hYmxpbmcgZHVhbCBzb2x1dGlvbiBtZXRob2RzLiIsICJTVk0gZHVhbCByZXBsYWNlcyBkLWRpbWVuc2lvbmFsIHByaW1hbCAobWluaW1pemUgb3ZlciB3ZWlnaHRzKSB3aXRoIG4tZGltZW5zaW9uYWwgZHVhbCAobWF4aW1pemUgb3ZlciDOsSBwZXIgdHJhaW5pbmcgc2FtcGxlKSwgZW5hYmxpbmcgdGhlIGtlcm5lbCB0cmljayB2aWEgaW5uZXIgcHJvZHVjdCByZXBsYWNlbWVudC4iLCAiQ29uc3RyYWluZWQgUkwgKENQTywgUFBPKSBhbmQgZmFpciBNTCBib3RoIHVzZSBkdWFsIGdyYWRpZW50IGFzY2VudCB0byBlbmZvcmNlIGluZXF1YWxpdHkgY29uc3RyYWludHM6IHVwZGF0ZSBtdWx0aXBsaWVyIGJ5IM67IOKGkCBtYXgoMCwgzrsgKyDOscK3Yyh4KSkgYXQgZWFjaCBzdGVwLiIsICJGb3Igbm9uLWNvbnZleCBwcm9ibGVtcywgS0tUIGNvbmRpdGlvbnMgYXJlIG5lY2Vzc2FyeSBidXQgbm90IHN1ZmZpY2llbnQg4oCUIGFsd2F5cyB2ZXJpZnkgc2Vjb25kLW9yZGVyIGNvbmRpdGlvbnMgYW5kIG1vbml0b3IgY29uc3RyYWludCBzYXRpc2ZhY3Rpb24gZW1waXJpY2FsbHkuIl19XQ=="
---

# Lagrangian Optimization and KKT Conditions

Constrained optimization appears throughout machine learning in forms that are not always recognizable as such. Support Vector Machines minimize weight norm subject to margin constraints. LASSO regression minimizes squared error subject to an L1 norm budget. PPO in reinforcement learning constrains the KL divergence between new and old policy. Fairness-aware models constrain the performance gap between demographic groups. In all these cases, the Lagrangian framework provides a unified mathematical language: replace the constrained problem with an unconstrained Lagrangian that penalizes constraint violations, then derive optimality conditions (the KKT conditions) that must hold at the solution. This note builds from the geometric intuition of Lagrange multipliers through KKT complementary slackness, strong duality via Slater's condition, and the SVM dual derivation that enables the kernel trick.

## Equality Constraints: Lagrange Multipliers

Consider: minimize f(x) subject to g(x) = 0. The geometric insight: at the constrained optimum x*, the gradient ∇f(x*) must be parallel to ∇g(x*). If they were not parallel, we could move along the constraint surface (in the direction perpendicular to ∇g, staying on the constraint) and decrease f — contradicting optimality. This parallelism condition is formalized by the Lagrangian: L(x, λ) = f(x) + λg(x). The stationarity condition ∇_x L = 0 gives ∇f + λ∇g = 0, i.e., ∇f = −λ∇g (gradients are parallel with ratio −λ). Combined with feasibility g(x*) = 0, these are necessary and sufficient conditions for a local minimum (for smooth equality-constrained convex problems: sufficient for global minimum). The multiplier λ has an economic interpretation: λ = −∂f*/∂c where c is the right-hand side of g(x) = c. A positive λ means tightening the constraint increases the objective; a negative λ means loosening it does.

```python
import numpy as np
from scipy.optimize import minimize

# Constrained QP: minimize x^2 + y^2 subject to x + y = 1
# Analytical solution: x* = y* = 0.5, lambda* = -1
def objective(xy): return xy[0]**2 + xy[1]**2
def constraint_eq(xy): return xy[0] + xy[1] - 1.0

# Solve with scipy
result = minimize(
    objective,
    x0=np.array([0.0, 0.0]),
    method='SLSQP',
    constraints={'type': 'eq', 'fun': constraint_eq}
)
print("Scipy solution x*:", result.x.round(6))
print("Objective at x*:", round(result.fun, 6))

# Verify KKT: stationarity ∇f + λ∇g = 0
x_star = result.x
gf = np.array([2 * x_star[0], 2 * x_star[1]])  # ∇f
gg = np.array([1.0, 1.0])                         # ∇g
# lambda* such that gf + lambda * gg = 0
lambda_star = -gf[0] / gg[0]
print(f"lambda* = {lambda_star:.6f}")
print("Stationarity satisfied:", np.allclose(gf + lambda_star * gg, 0))
print("Feasibility satisfied:", np.isclose(constraint_eq(x_star), 0))
print("Analytical x*: [0.5, 0.5], matches:", np.allclose(x_star, [0.5, 0.5]))
```

## Inequality Constraints and KKT Conditions

For the general constrained problem — minimize f(x) subject to hⱼ(x) ≤ 0 for j=1..m and gᵢ(x) = 0 for i=1..p — the Lagrangian is L(x, λ, μ) = f(x) + Σλᵢgᵢ(x) + Σμⱼhⱼ(x). The KKT conditions are four sets of requirements that must hold at any local minimum (given constraint qualifications): (1) Stationarity: ∇_x L = ∇f + Σλᵢ∇gᵢ + Σμⱼ∇hⱼ = 0; (2) Primal feasibility: hⱼ(x*) ≤ 0 and gᵢ(x*) = 0 for all j, i; (3) Dual feasibility: μⱼ ≥ 0 for all j (multipliers for inequality constraints must be non-negative); (4) Complementary slackness: μⱼhⱼ(x*) = 0 for all j. Complementary slackness is the key structural insight: either the inequality constraint is inactive (hⱼ(x*) < 0, strict slack) and its multiplier is zero, OR the constraint is active (hⱼ(x*) = 0, binding) and its multiplier can be nonzero. This means only the active constraints (the binding ones) influence the optimal point via their multipliers. For convex problems, KKT conditions are both necessary and sufficient for global optimality.

```python
import numpy as np
from scipy.optimize import minimize, LinearConstraint

# QP: minimize (x-3)^2 + (y-4)^2 subject to x <= 2, y <= 3, x >= 0, y >= 0
# Rewrite as h1: x-2 <= 0, h2: y-3 <= 0, h3: -x <= 0, h4: -y <= 0
def obj(xy): return (xy[0]-3)**2 + (xy[1]-4)**2
constraints = [
    {'type': 'ineq', 'fun': lambda xy: 2 - xy[0]},  # x <= 2, as 2-x >= 0
    {'type': 'ineq', 'fun': lambda xy: 3 - xy[1]},  # y <= 3
    {'type': 'ineq', 'fun': lambda xy: xy[0]},       # x >= 0
    {'type': 'ineq', 'fun': lambda xy: xy[1]},       # y >= 0
]
res = minimize(obj, [1.0, 1.0], method='SLSQP', constraints=constraints)
x_star = res.x
print("Solution x*:", x_star.round(4), "(expected: [2, 3])")

# Verify KKT manually
gf = np.array([2*(x_star[0]-3), 2*(x_star[1]-4)])
h_vals = [2-x_star[0], 3-x_star[1], x_star[0], x_star[1]]
print("Constraint values (should be >= 0):", [round(h, 4) for h in h_vals])
print("Active constraints (h=0):", [i for i, h in enumerate(h_vals) if abs(h) < 1e-5])
print("Primal feasibility:", all(h >= -1e-6 for h in h_vals))
print("Gradient ∇f at x*:", gf.round(4), "(should be non-zero, offset by active constraints)")
```

## Strong Duality and Slater's Condition

The Lagrangian dual function g(λ, μ) = min_x L(x, λ, μ) is always concave in (λ, μ) (as a pointwise minimum of affine functions). Weak duality states g(λ, μ) ≤ f(x*) always — the dual objective is always a lower bound on the primal optimum. The duality gap is f(x*) − g(λ*, μ*) ≥ 0. Strong duality (zero duality gap) means g(λ*, μ*) = f(x*) — the dual can be solved to recover the primal solution. Slater's condition: for a convex primal problem, strong duality holds if there exists a strictly feasible point x̄ with hⱼ(x̄) < 0 (strictly) for all j. Slater's condition is satisfied by almost all well-posed convex ML problems (it fails only on degenerate constraints). When strong duality holds, we can solve the dual (often a simpler problem) instead of the primal. The dual problem is always convex (we are maximizing a concave function), even if the primal was non-convex — this is how SVM's non-linear formulations become tractable via the kernel trick.

## SVM Dual Derivation

SVM primal: minimize ½‖w‖² subject to yᵢ(wᵀxᵢ + b) ≥ 1 for all i (equivalently, hᵢ(w,b) = 1 − yᵢ(wᵀxᵢ+b) ≤ 0). Lagrangian: L = ½‖w‖² − Σαᵢ[yᵢ(wᵀxᵢ+b) − 1] with αᵢ ≥ 0. KKT stationarity with respect to w: ∂L/∂w = w − ΣαᵢyᵢXᵢ = 0, so w* = Σαᵢyᵢxᵢ. With respect to b: ∂L/∂b = −Σαᵢyᵢ = 0, so Σαᵢyᵢ = 0. Substituting w* back into L and simplifying gives the dual: maximize D(α) = Σαᵢ − ½Σᵢⱼ αᵢαⱼyᵢyⱼxᵢᵀxⱼ subject to αᵢ ≥ 0 and Σαᵢyᵢ = 0. This is a QP in n variables (training samples) instead of d variables (features). When n < d, the dual is cheaper; for n > d, the primal wins. More importantly, xᵢᵀxⱼ appears only as an inner product, which can be replaced by any kernel K(xᵢ, xⱼ) = φ(xᵢ)ᵀφ(xⱼ) — allowing non-linear decision boundaries without explicitly computing φ(x). By KKT complementary slackness: αᵢ·[yᵢ(wᵀxᵢ+b)−1] = 0, so either αᵢ = 0 (point is not a support vector, not on the margin) or yᵢ(wᵀxᵢ+b) = 1 (point is on the margin, is a support vector).

```python
import numpy as np
from scipy.optimize import minimize
from sklearn.svm import SVC
from sklearn.datasets import make_blobs

# Generate linearly separable data
np.random.seed(42)
X, y_raw = make_blobs(n_samples=30, centers=2, random_state=0)
y = 2 * y_raw - 1  # convert to {-1, +1}
n = len(y)

# SVM dual: maximize Σαᵢ - ½Σᵢⱼ αᵢαⱼyᵢyⱼxᵢᵀxⱼ
K = (y[:, None] * X) @ (y[:, None] * X).T  # Gram matrix with labels
def neg_dual(alpha): return 0.5 * alpha @ K @ alpha - alpha.sum()
def neg_dual_grad(alpha): return K @ alpha - np.ones(n)

result = minimize(
    neg_dual, x0=np.zeros(n), jac=neg_dual_grad, method='SLSQP',
    bounds=[(0, None)] * n,
    constraints={'type': 'eq', 'fun': lambda a: (a * y).sum()}
)
alpha = result.x
w = (alpha * y) @ X
sv_mask = alpha > 1e-4
print(f"Support vectors: {sv_mask.sum()} / {n}")
print("w (dual):", w.round(4))
sklearn_svm = SVC(kernel='linear', C=1e6)
sklearn_svm.fit(X, y_raw)
print("w (sklearn):", sklearn_svm.coef_.round(4))
print("Complementary slackness check:")
margins = y * (X @ w)
print("  α=0 points on margin?", all(margins[~sv_mask] >= 0.99))
```

## ML Connections: Constrained RL and Fair ML

KKT conditions and the Lagrangian framework appear in modern ML beyond SVM. In reinforcement learning: PPO (Proximal Policy Optimization) enforces a trust region via a KL penalty (soft constraint); CPO (Constrained Policy Optimization, Achiam et al. 2017) formulates safety RL as minimize −E[reward] subject to E[cost] ≤ d, solved via KKT with the Lagrange multiplier updated by dual gradient ascent: λ ← max(0, λ + α(E[cost] − d)). The multiplier λ becomes the safety penalty coefficient, automatically adapting to constraint violations. In fair ML: demographic parity constraints require equal accuracy across groups, formulated as minimize L(θ) subject to |acc_group1 − acc_group2| ≤ ε; solved via augmented Lagrangian or projected gradient descent. LASSO as a constrained problem: the standard Lagrangian formulation minimize ‖Xβ−y‖² + λ‖β‖₁ corresponds exactly to minimize ‖Xβ−y‖² subject to ‖β‖₁ ≤ t, where the multiplier λ is the dual variable for the L1 budget constraint t. Different values of λ trace the LASSO regularization path.

```python
import numpy as np

def dual_gradient_ascent(f_primal, grad_f, constraint, grad_constraint,
                          x0, lr_primal=0.01, lr_dual=0.1, steps=200):
    """Primal-dual optimization: min f(x) s.t. c(x) <= 0."""
    x = x0.copy()
    lam = 0.0  # dual variable (multiplier)
    history = []
    for step in range(steps):
        # Primal step: gradient descent on Lagrangian L = f(x) + lambda * c(x)
        L_grad = grad_f(x) + lam * grad_constraint(x)
        x = x - lr_primal * L_grad
        # Dual step: gradient ascent on dual (maximize over lambda >= 0)
        constraint_val = constraint(x)
        lam = max(0.0, lam + lr_dual * constraint_val)
        history.append({'step': step, 'f': f_primal(x),
                        'c': constraint_val, 'lambda': lam})
    return x, lam, history

# Example: minimize x^2 + y^2 subject to x + y >= 2 (rewritten as 2-x-y <= 0)
f = lambda xy: xy[0]**2 + xy[1]**2
grad_f = lambda xy: 2 * xy
c = lambda xy: 2 - xy[0] - xy[1]   # constraint: 2 - x - y <= 0
grad_c = lambda xy: np.array([-1.0, -1.0])

np.random.seed(0)
x_sol, lam_sol, hist = dual_gradient_ascent(
    f, grad_f, c, grad_c, x0=np.array([0.1, 0.1]))
print(f"Primal solution x*: {x_sol.round(4)} (expected [1, 1])")
print(f"Lambda* = {lam_sol:.4f} (expected 2.0, marginal cost of constraint)")
print(f"Constraint satisfied: {c(x_sol):.4f} <= 0")
print(f"Final objective: {f(x_sol):.4f} (expected 2.0)")
```

## Implementation Pitfalls

Critical pitfalls in constrained optimization for ML. First, confusing necessary and sufficient conditions: KKT conditions are necessary for local minima under constraint qualifications (like LICQ: Linear Independence Constraint Qualification) but only sufficient for convex problems. For non-convex problems (deep RL constraints, non-linear fairness constraints), a KKT point may be a saddle of the Lagrangian rather than a minimum. Second, the dual gradient ascent step size (lr_dual) must be chosen carefully: too large causes oscillations in the multiplier λ without convergence; too small converges extremely slowly to the feasible region. The dual step size is typically set 10-100× smaller than the primal step size. Third, for equality constraints, multipliers are unconstrained (can be positive or negative); for inequality constraints, multipliers must be non-negative — enforcing this via max(0, λ + α·c(x)) is the projected dual update. Forgetting the projection gives incorrect multipliers and invalid constraint handling.

## Practical Guidance

Practical guidelines for constrained optimization in ML. For convex problems (SVM, L1 regression, linear fairness constraints): use established solvers (scipy.optimize.minimize with SLSQP, CVXPY, or specialized QP solvers) — they implement interior-point methods with proven convergence. For constrained RL (safety constraints, KL trust regions): use dual gradient ascent with a separate dual learning rate, clip the dual variable to prevent it from growing unboundedly (max_lambda hyperparameter), and monitor both the primal objective and constraint violation separately in training logs. For LASSO and group-sparse regularization: use the Lagrangian form with λ as a hyperparameter (equivalent to the constrained form by strong duality) rather than the constrained form, as coordinate descent and proximal algorithms are more efficient for L1. Always verify Slater's condition before assuming strong duality: check that a strictly feasible point exists; if the constraint is an equality (hⱼ = 0), Slater does not apply and additional conditions are needed.

> **Warning**: KKT conditions are necessary but NOT sufficient for non-convex problems. For a non-convex objective with constraints, a point satisfying KKT could be a saddle point of the Lagrangian, a local minimum that is not global, or even a local maximum of the Lagrangian. Always verify second-order sufficiency conditions: the Lagrangian Hessian ∇²L must be positive semidefinite on the tangent space of active constraints. For RL and fairness constraints (typically non-convex), treat dual gradient ascent as a heuristic and monitor constraint satisfaction empirically rather than relying on theoretical guarantees.

| Method | Handles Equality | Handles Inequality | Convergence | ML Use Case |
|---|---|---|---|---|
| Lagrange multipliers | Yes | No | Newton rate (local) | SVM, physics constraints |
| KKT + Newton | Yes | Yes | Quadratic (local) | Small QPs, SVM |
| Projected GD | Via projection | Yes (simple sets) | O(1/t) | L2-ball constraints, simplex |
| Augmented Lagrangian | Yes | Yes | Superlinear | Fairness ML, ADMM |
| Interior point | Yes | Yes (strict ineq) | Polynomial | Large-scale QP (SVM with soft margin) |
| Penalty method | Yes (approx) | Yes (approx) | Depends on penalty | Quick prototypes, PPO KL penalty |

---

## Key Takeaways

- Lagrange multipliers convert equality-constrained problems to unconstrained ones; the optimality condition ∇f = −λ∇g captures gradient alignment at the constrained optimum.
- KKT conditions generalize Lagrange multipliers to inequality constraints: stationarity, primal feasibility, dual feasibility (μⱼ ≥ 0), and complementary slackness (μⱼhⱼ = 0).
- Complementary slackness means only active constraints (hⱼ = 0) have nonzero multipliers — inactive constraints are irrelevant at the optimum.
- Slater's condition (strict interior point exists) guarantees strong duality for convex problems: the dual objective equals the primal minimum, enabling dual solution methods.
- SVM dual replaces d-dimensional primal (minimize over weights) with n-dimensional dual (maximize over α per training sample), enabling the kernel trick via inner product replacement.
- Constrained RL (CPO, PPO) and fair ML both use dual gradient ascent to enforce inequality constraints: update multiplier by λ ← max(0, λ + α·c(x)) at each step.
- For non-convex problems, KKT conditions are necessary but not sufficient — always verify second-order conditions and monitor constraint satisfaction empirically.

