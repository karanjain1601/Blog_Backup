---
title: "Fine-Grained Mixture of Experts"
slug: "fine-grained-moe"
description: "Using many small experts instead of few large ones — as in DeepSeek-MoE and MiniMax — to improve expert specialization and routing granularity without increasing computation."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhZGl0aW9uYWwgTW9FIGFyY2hpdGVjdHVyZXMgdXNlIGEgc21hbGwgbnVtYmVyIG9mIGxhcmdlIGV4cGVydHMg4oCUIHR5cGljYWxseSA4IG9yIDE2LCBlYWNoIHdpdGggdGhlIHNhbWUgaGlkZGVuIGRpbWVuc2lvbiBhcyBhIGRlbnNlIEZGTi4gRmluZS1ncmFpbmVkIE1vRSAoRGFpIGV0IGFsLiwgMjAyNCwgRGVlcFNlZWstTW9FOyBhbmQgc3Vic2VxdWVudCB3b3JrKSBjaGFsbGVuZ2VzIHRoaXMgZGVmYXVsdCBieSBzcGxpdHRpbmcgZWFjaCBleHBlcnQgaW50byBtYW55IHNtYWxsZXIgc3ViLWV4cGVydHMuIEluc3RlYWQgb2YgOCBleHBlcnRzIGVhY2ggd2l0aCBoaWRkZW4gZGltZW5zaW9uIGRfZmYsIGZpbmUtZ3JhaW5lZCBNb0UgdXNlcyA2NCBvciAxMjggZXhwZXJ0cyBlYWNoIHdpdGggaGlkZGVuIGRpbWVuc2lvbiBkX2ZmLzguIFRvdGFsIHBhcmFtZXRlciBjb3VudCBpcyBpZGVudGljYWwsIHRvcC1LIGFjdGl2ZSBGTE9QcyBhcmUgaWRlbnRpY2FsIChyb3V0aW5nIHRvcC0xNiBvZiAxMjggc21hbGwgZXhwZXJ0cyDiiYggcm91dGluZyB0b3AtMiBvZiAxNiBsYXJnZSBleHBlcnRzKSwgYnV0IHRoZSBncmFudWxhcml0eSBvZiB0aGUgcm91dGluZyBkZWNpc2lvbiBpcyBtdWNoIGZpbmVyLiBUaGlzIGZpbmVyIGdyYW51bGFyaXR5IGFsbG93cyBlYWNoIGV4cGVydCB0byBzcGVjaWFsaXNlIG1vcmUgbmFycm93bHksIHJlZHVjaW5nIGtub3dsZWRnZSByZWR1bmRhbmN5IGFuZCBpbXByb3ZpbmcgdGhlIGluZm9ybWF0aW9uIGVmZmljaWVuY3kgb2YgdGhlIHBhcmFtZXRlciBidWRnZXQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZpbmUtZ3JhaW5lZCBNb0Ugd2FzIGludHJvZHVjZWQgaW4gdGhlIERlZXBTZWVrLU1vRSBwYXBlciAoRGFpIGV0IGFsLiwgMjAyNCkgYW5kIGFkb3B0ZWQgaW4gRGVlcFNlZWstVjIgKDIzNkIgdG90YWwsIDIxQiBhY3RpdmUpLiBUaGUga2V5IG9ic2VydmF0aW9uIGlzIHRoYXQgY29hcnNlIE1vRSAoOCBsYXJnZSBleHBlcnRzKSBmb3JjZXMgZWFjaCBleHBlcnQgdG8gYmUgZ2VuZXJhbCDigJQgaXQgY2Fubm90IGFmZm9yZCB0byBzcGVjaWFsaXNlIHRvbyBuYXJyb3dseSBiZWNhdXNlIGl0IG11c3QgcHJvY2VzcyAxLzggb2YgYWxsIHRva2VucyBpbmNsdWRpbmcgbWFueSBmb3Igd2hpY2ggaXQgaGFzIG5vIGV4cGVydGlzZS4gRmluZS1ncmFpbmVkIE1vRSAoNjTigJMxMjggc21hbGwgZXhwZXJ0cykgYWxsb3dzIGVhY2ggZXhwZXJ0IHRvIHByb2Nlc3Mgb25seSAxLzY04oCTMS8xMjggb2YgdG9rZW5zLCBlbmFibGluZyBtdWNoIHRpZ2h0ZXIgc3BlY2lhbGlzYXRpb24uIFJvdXRpbmcgdG9wLUtfciBvZiBOX3IgZmluZS1ncmFpbmVkIGV4cGVydHMgKHdpdGggS19yL05fciA9IEsvTiwgc2FtZSBhY3RpdmUgZnJhY3Rpb24pIHByb2R1Y2VzIGlkZW50aWNhbCBjb21wdXRlIHdoaWxlIGdhaW5pbmcgcm91dGluZyBwcmVjaXNpb24uIFRoZSBwcmFjdGljYWwgYmVuZWZpdCBpcyBtZWFzdXJhYmxlIGltcHJvdmVtZW50IGluIGRvd25zdHJlYW0gdGFzayBhY2N1cmFjeSBhdCB0aGUgc2FtZSBGTE9Qcywgd2l0aCB0aGUgbWFpbiBjb3N0IGJlaW5nIG1vcmUgY29tcGxleCByb3V0aW5nIGFuZCBsb2FkLWJhbGFuY2luZyBhY3Jvc3MgbWFueSBtb3JlIGV4cGVydHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29hcnNlIHZzIEZpbmUtR3JhaW5lZCBFeHBlcnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZnVuZGFtZW50YWwgZGlmZmVyZW5jZSBiZXR3ZWVuIGNvYXJzZSBhbmQgZmluZS1ncmFpbmVkIE1vRSBpcyB0aGUgZ3JhbnVsYXJpdHkgb2YgdGhlIGV4cGVydCBmdW5jdGlvbi4gQSBjb2Fyc2UgZXhwZXJ0IHdpdGggaGlkZGVuIGRpbWVuc2lvbiBkX2ZmIGxlYXJucyBhIGdlbmVyYWwgdHJhbnNmb3JtYXRpb24gdGhhdCBhcHBsaWVzIHRvIG1hbnkgdG9rZW4gdHlwZXMuIEEgZmluZS1ncmFpbmVkIGV4cGVydCB3aXRoIGhpZGRlbiBkaW1lbnNpb24gZF9mZi9tIChmb3IgbS1mb2xkIHNwbGl0dGluZykgbGVhcm5zIGEgbmFycm93ZXIgdHJhbnNmb3JtYXRpb24gdGhhdCBhcHBsaWVzIHRvIG0gdGltZXMgZmV3ZXIgdG9rZW5zIG9uIGF2ZXJhZ2UuIFRoZSBhbmFsb2d5IGlzIHByb2Zlc3Npb25hbCB2ZXJzdXMgZ2VuZXJhbGlzdDogYSBjb2Fyc2UgZXhwZXJ0IGlzIGxpa2UgYSBnZW5lcmFsaXN0IGRvY3RvciB3aG8gc2VlcyBldmVyeSBwYXRpZW50OyBhIGZpbmUtZ3JhaW5lZCBleHBlcnQgaXMgbGlrZSBhIHNwZWNpYWxpc3Qgd2hvIHNlZXMgb25seSBwYXRpZW50cyB3aXRoIGEgc3BlY2lmaWMgY29uZGl0aW9uLiBUaGUgc3BlY2lhbGlzdCBjYW4gZGV2ZWxvcCBtdWNoIGRlZXBlciBleHBlcnRpc2UgaW4gdGhhdCBuYXJyb3cgZG9tYWluLiBUaGUgY2hhbGxlbmdlIGlzIHRoYXQgd2l0aCBtYW55IHNtYWxsIGV4cGVydHMsIHRoZSByb3V0aW5nIGRlY2lzaW9uICh3aGljaCBzcGVjaWFsaXN0PykgYmVjb21lcyBtb3JlIGNyaXRpY2FsIOKAlCBhIG1pc3JvdXRlZCB0b2tlbiByZWNlaXZlcyBhIGxlc3MtYXBwbGljYWJsZSB0cmFuc2Zvcm1hdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgRmluZUdyYWluZWRNb0VMYXllcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkZpbmUtZ3JhaW5lZCBNb0U6IG1hbnkgc21hbGwgZXhwZXJ0cyB2cyBmZXcgbGFyZ2UgZXhwZXJ0cy5cbiAgICBTYW1lIHRvdGFsIHBhcmFtcyBhbmQgc2FtZSBhY3RpdmUgRkxPUHMgYXMgY29hcnNlIE1vRS5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbDogaW50LCBkX2ZmOiBpbnQsXG4gICAgICAgICAgICAgICAgIG5fZXhwZXJ0czogaW50LCB0b3BfazogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgICMgRWFjaCBleHBlcnQgaGFzIGRfZmYgaGlkZGVuIHVuaXRzIChzYW1lIGFzIGNvYXJzZSlcbiAgICAgICAgIyBidXQgbl9leHBlcnRzIGlzIG11Y2ggbGFyZ2VyIChlLmcuLCA2NCB2cyA4KVxuICAgICAgICBzZWxmLm5fZXhwZXJ0cywgc2VsZi50b3BfayA9IG5fZXhwZXJ0cywgdG9wX2tcbiAgICAgICAgc2VsZi5yb3V0ZXIgID0gbm4uTGluZWFyKGRfbW9kZWwsIG5fZXhwZXJ0cywgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi53MSA9IG5uLlBhcmFtZXRlcih0b3JjaC5yYW5kbihuX2V4cGVydHMsIGRfbW9kZWwsIGRfZmYpICogMC4wMilcbiAgICAgICAgc2VsZi53MiA9IG5uLlBhcmFtZXRlcih0b3JjaC5yYW5kbihuX2V4cGVydHMsIGRfZmYsIGRfbW9kZWwpICogMC4wMilcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIE4sIEQgPSB4LnNoYXBlWzBdICogeC5zaGFwZVsxXSwgeC5zaGFwZVsyXVxuICAgICAgICB4ZiAgID0geC52aWV3KE4sIEQpXG4gICAgICAgIHByb2JzLCBpZHggPSB0b3JjaC50b3BrKEYuc29mdG1heChzZWxmLnJvdXRlcih4ZiksIC0xKSwgc2VsZi50b3BfaywgLTEpXG4gICAgICAgIHByb2JzID0gcHJvYnMgLyBwcm9icy5zdW0oLTEsIGtlZXBkaW09VHJ1ZSlcbiAgICAgICAgb3V0ICAgPSB0b3JjaC56ZXJvc19saWtlKHhmKVxuICAgICAgICBmb3IgayBpbiByYW5nZShzZWxmLnRvcF9rKTpcbiAgICAgICAgICAgIGZvciBlIGluIHJhbmdlKHNlbGYubl9leHBlcnRzKTpcbiAgICAgICAgICAgICAgICBtID0gaWR4WzosIGtdID09IGVcbiAgICAgICAgICAgICAgICBpZiBub3QgbS5hbnkoKTogY29udGludWVcbiAgICAgICAgICAgICAgICBoID0gRi5nZWx1KHhmW21dIEAgc2VsZi53MVtlXSlcbiAgICAgICAgICAgICAgICBvdXRbbV0gKz0gcHJvYnNbbSwgazprKzFdICogKGggQCBzZWxmLncyW2VdKVxuICAgICAgICByZXR1cm4gb3V0LnZpZXdfYXMoeClcblxuIyBDb2Fyc2U6IDggZXhwZXJ0cywgdG9wLTIgfCBGaW5lLWdyYWluZWQ6IDY0IGV4cGVydHMsIHRvcC0xNiAoc2FtZSBhY3RpdmUgZnJhY3Rpb24pXG5jb2Fyc2UgPSBGaW5lR3JhaW5lZE1vRUxheWVyKDUxMiwgMjA0OCwgbl9leHBlcnRzPTgsICB0b3Bfaz0yKVxuZmluZSAgID0gRmluZUdyYWluZWRNb0VMYXllcig1MTIsIDIwNDgsIG5fZXhwZXJ0cz02NCwgdG9wX2s9MTYpXG5wcmludChmXCJDb2Fyc2UgcGFyYW1zOiB7c3VtKHAubnVtZWwoKSBmb3IgcCBpbiBjb2Fyc2UucGFyYW1ldGVycygpKTosfVwiKVxucHJpbnQoZlwiRmluZSAgIHBhcmFtczoge3N1bShwLm51bWVsKCkgZm9yIHAgaW4gZmluZS5wYXJhbWV0ZXJzKCkpOix9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVlcFNlZWstTW9FIERlc2lnbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVlcFNlZWstTW9FIHVzZXMgTl9yPTY0IGZpbmUtZ3JhaW5lZCByb3V0ZWQgZXhwZXJ0cyAoY29tcGFyZWQgdG8gTWl4dHJhbFx1MDAyN3MgOCksIHJvdXRpbmcgdG9wLUtfcj02IHBlciB0b2tlbi4gQWRkaXRpb25hbGx5LCBpdCBhZGRzIE5fcz0yIHNoYXJlZCBleHBlcnRzIHRoYXQgYWx3YXlzIGFjdGl2YXRlIGZvciBldmVyeSB0b2tlbiByZWdhcmRsZXNzIG9mIHJvdXRpbmcg4oCUIHRoZXNlIGhhbmRsZSBjb21tb24ga25vd2xlZGdlIHRoYXQgZXZlcnkgdG9rZW4gbmVlZHMuIFRoZSByb3V0aW5nIGlzOiBvdXRwdXQgPSBzdW0oc2hhcmVkX2V4cGVydF9pKHgpKSArIHN1bV97ayBpbiB0b3AtS19yfSBnX2sgKiBFX2soeCkuIFRoZSA2NCBzbWFsbCByb3V0ZWQgZXhwZXJ0cyB0b2dldGhlciB3aXRoIDIgYWx3YXlzLWFjdGl2ZSBzaGFyZWQgZXhwZXJ0cyBnaXZlIERlZXBTZWVrLU1vRSBzaWduaWZpY2FudGx5IGhpZ2hlciBzcGVjaWFsaXNhdGlvbiB0aGFuIGEgY29tcGFyYWJsZSA4LWV4cGVydCBtb2RlbC4gVGhlIHBhcGVyIGRlbW9uc3RyYXRlcyB0aGF0IHRoZSBmaW5lLWdyYWluZWQgZXhwZXJ0cyBkZXZlbG9wIG1vcmUgZGlzdGluY3Qgd2VpZ2h0IG1hdHJpY2VzIChsb3dlciBjb3NpbmUgc2ltaWxhcml0eSBiZXR3ZWVuIGV4cGVydCB3ZWlnaHQgcGFpcnMpIGFuZCBzaG93IHNoYXJwZXIgdG9rZW4gcm91dGluZyBwYXR0ZXJucyB0aGFuIGNvYXJzZSBleHBlcnRzIHRyYWluZWQgd2l0aCB0aGUgc2FtZSBjb21wdXRlIGJ1ZGdldC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIGl0ZXJ0b29scyBpbXBvcnQgY29tYmluYXRpb25zXG5cbmRlZiBtZWFzdXJlX2tub3dsZWRnZV9yZWR1bmRhbmN5KGV4cGVydF93ZWlnaHRzOiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJNZWFzdXJlIGNvc2luZSBzaW1pbGFyaXR5IGJldHdlZW4gZXhwZXJ0IHdlaWdodCBtYXRyaWNlcy5cbiAgICBMb3dlciBtZWFuIHNpbWlsYXJpdHkgPSBtb3JlIHNwZWNpYWxpc2F0aW9uID0gbGVzcyByZWR1bmRhbmN5LlxuICAgIGV4cGVydF93ZWlnaHRzOiAobl9leHBlcnRzLCBkX2luICogZF9vdXQpIGZsYXR0ZW5lZCB3ZWlnaHQgdmVjdG9ycy5cIlwiXCJcbiAgICBuID0gZXhwZXJ0X3dlaWdodHMuc2hhcGVbMF1cbiAgICBub3JtcyAgPSBGLm5vcm1hbGl6ZShleHBlcnRfd2VpZ2h0cywgZGltPS0xKSAgICAgICAgICAgICMgKEUsIEQpXG4gICAgc2ltcyAgID0gW11cbiAgICBmb3IgaSwgaiBpbiBjb21iaW5hdGlvbnMocmFuZ2UobiksIDIpOlxuICAgICAgICBzaW1zLmFwcGVuZCgobm9ybXNbaV0gKiBub3Jtc1tqXSkuc3VtKCkuaXRlbSgpKVxuICAgIHNpbXMgPSB0b3JjaC50ZW5zb3Ioc2ltcylcbiAgICByZXR1cm4ge1wibWVhbl9zaW1cIjogc2ltcy5tZWFuKCkuaXRlbSgpLFxuICAgICAgICAgICAgXCJzdGRfc2ltXCI6ICBzaW1zLnN0ZCgpLml0ZW0oKSxcbiAgICAgICAgICAgIFwibWF4X3NpbVwiOiAgc2ltcy5tYXgoKS5pdGVtKCl9XG5cbiMgU2ltdWxhdGUgcmFuZG9tIGV4cGVydCB3ZWlnaHRzIGZvciBjb2Fyc2UgKDgpIHZzIGZpbmUtZ3JhaW5lZCAoNjQpXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbmZvciBuYW1lLCBuX2V4cCBpbiBbKFwiY29hcnNlLThcIiwgOCksIChcImZpbmUtNjRcIiwgNjQpXTpcbiAgICBXID0gdG9yY2gucmFuZG4obl9leHAsIDUxMiAqIDEyOCkgICAgICAgICAgICAgICAgICAgICAgIyBmbGF0dGVuIGRfbW9kZWwgeCBkX2ZmXG4gICAgciA9IG1lYXN1cmVfa25vd2xlZGdlX3JlZHVuZGFuY3koVylcbiAgICBwcmludChmXCJ7bmFtZTpcdTAwM2UxMH06IG1lYW5fc2ltPXtyW1x1MDAyN21lYW5fc2ltXHUwMDI3XTouNGZ9ICBtYXhfc2ltPXtyW1x1MDAyN21heF9zaW1cdTAwMjddOi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFeHBlcnQgR3JhbnVsYXJpdHkgVHJhZGVvZmZzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbmNyZWFzaW5nIHRoZSBudW1iZXIgb2YgZXhwZXJ0cyB3aGlsZSBob2xkaW5nIHRvdGFsIHBhcmFtZXRlcnMgYW5kIGFjdGl2ZSBGTE9QcyBjb25zdGFudCBpbnZvbHZlcyBnZW51aW5lIHRyYWRlb2Zmcy4gU21hbGxlciBpbmRpdmlkdWFsIGV4cGVydHMgaGF2ZSBsb3dlciBoaWRkZW4gZGltZW5zaW9uIChkX2ZmL20gZm9yIG0tZm9sZCBzcGxpdCkgYW5kIHRoZXJlZm9yZSBsb3dlciByZXByZXNlbnRhdGlvbmFsIGNhcGFjaXR5IHBlciBleHBlcnQuIEZvciB2ZXJ5IGZpbmUtZ3JhaW5lZCBleHBlcnRzIChtPTE2LCBoaWRkZW4gZGltIHJlZHVjZWQgMTZ4KSwgZWFjaCBleHBlcnQgbWF5IGxhY2sgdGhlIGNhcGFjaXR5IHRvIGxlYXJuIGNvbXBsZXggdHJhbnNmb3JtYXRpb25zLiBBZGRpdGlvbmFsbHksIHdpdGggbWFueSBleHBlcnRzLCByb3V0aW5nIGJlY29tZXMgbW9yZSBjcml0aWNhbDogdGhlIHJvdXRlciBtdXN0IGNvcnJlY3RseSBhc3NpZ24gZWFjaCB0b2tlbiB0byBpdHMgbW9zdCBhcHByb3ByaWF0ZSBleHBlcnQgYW1vbmcgNjQgb3IgMTI4IG9wdGlvbnMsIGEgaGFyZGVyIHByb2JsZW0gdGhhbiBjaG9vc2luZyBhbW9uZyA4LiBUaGlzIHJlcXVpcmVzIHRoZSByb3V0ZXIgdG8gZGV2ZWxvcCBmaW5lci1ncmFpbmVkIHJlcHJlc2VudGF0aW9ucyBhbmQgbWF5IHJlcXVpcmUgbG9uZ2VyIHRyYWluaW5nIHRvIGNvbnZlcmdlLiBUaGUgc3dlZXQgc3BvdCBpbiBwcmFjdGljZSBhcHBlYXJzIHRvIGJlIGFyb3VuZCAzMuKAkzEyOCBleHBlcnRzIGZvciBtb3N0IG1vZGVsIHNjYWxlcywgYmFsYW5jaW5nIHNwZWNpYWxpc2F0aW9uIGJlbmVmaXRzIGFnYWluc3QgcGVyLWV4cGVydCBjYXBhY2l0eSBhbmQgcm91dGluZyBkaWZmaWN1bHR5LiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDb25maWciLCJOIGV4cGVydHMiLCJFeHBlcnQgaGlkZGVuIGRpbSIsIlRvcC1LIiwiQWN0aXZlIHBhcmFtcyAoTSkiLCJTcGVjaWFsaXNhdGlvbiJdLCJyb3dzIjpbWyJHU2hhcmQgMjA0OEUiLCIyMDQ4IiwiZF9mZiAoZnVsbCkiLCIyIiwifjJ4IGRlbnNlIEZGTiIsIlZlcnkgaGlnaCAoYnV0IHJvdXRpbmcgaGFyZCkiXSxbIlN3aXRjaC1DIDIwNDhFIiwiMjA0OCIsImRfZmYgKGZ1bGwpIiwiMSIsIn4xeCBkZW5zZSBGRk4iLCJIaWdoIl0sWyJNaXh0cmFsIDhFIiwiOCIsImRfZmYgKGZ1bGwpIiwiMiIsIn4yeCBkZW5zZSBGRk4iLCJNb2RlcmF0ZSJdLFsiRGVlcFNlZWstTW9FIDY0RSIsIjY0IiwiZF9mZi84IiwiNiByb3V0ZWQgKyAyIHNoYXJlZCIsIn4xeCBkZW5zZSBGRk4iLCJIaWdoIl0sWyJGaW5lLWdyYWluZWQgMTI4RSIsIjEyOCIsImRfZmYvMTYiLCIxNiIsIn4xeCBkZW5zZSBGRk4iLCJWZXJ5IGhpZ2giXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJvdXRpbmcgd2l0aCBNYW55IEV4cGVydHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJvdXRpbmcgYW1vbmcgNjQgb3IgMTI4IGV4cGVydHMgaW50cm9kdWNlcyBuZXcgY2hhbGxlbmdlcy4gVGhlIHJvdXRlciBpcyBhIGxpbmVhciBsYXllciBvZiBzaXplIGRfbW9kZWwgw5cgbl9leHBlcnRzOyBhdCBuX2V4cGVydHM9MTI4LCB0aGlzIGlzIGRfbW9kZWwgw5cgMTI4IHBhcmFtZXRlcnMg4oCUIHN0aWxsIGEgc21hbGwgZnJhY3Rpb24gb2YgdG90YWwgcGFyYW1zLiBUaGUgc29mdG1heCBvdmVyIDEyOCBsb2dpdHMgaXMgbW9yZSBkaWZmdXNlIHRoYW4gb3ZlciA4LCBtZWFuaW5nIHRoZSB0b3AtSyBwcm9iYWJpbGl0eSBtYXNzIGlzIG1vcmUgc3ByZWFkIG91dC4gVGhpcyBjYW4gbWFrZSB0aGUgcm91dGVyIHNpZ25hbCB3ZWFrZXIgYW5kIHNsb3dlciB0byBkZXZlbG9wLiBEZWVwU2Vlay1Nb0UgYWRkcmVzc2VzIHRoaXMgd2l0aCBhIG5vcm1hbGlzZWQgdG9wLUsgc2VsZWN0aW9uOiBhZnRlciBjb21wdXRpbmcgdGhlIHRvcC1LIGV4cGVydHMsIHRoZSBnYXRpbmcgd2VpZ2h0cyBhcmUgcmVub3JtYWxpc2VkIHRvIHN1bSB0byAxLCBzaGFycGVuaW5nIHRoZSBzaWduYWwuIEFkZGl0aW9uYWxseSwgdGhlIGxvYWQtYmFsYW5jaW5nIGNoYWxsZW5nZSBpcyBoYXJkZXIgd2l0aCBtb3JlIGV4cGVydHMg4oCUIGVuc3VyaW5nIGVhY2ggb2YgMTI4IGV4cGVydHMgcmVjZWl2ZXMgcm91Z2hseSAxLzEyOCBvZiB0b2tlbnMgcmVxdWlyZXMgc3Ryb25nZXIgcmVndWxhcmlzYXRpb24gb3IgZXhwZXJ0IGNob2ljZSByb3V0aW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBEZWVwU2Vla01vRVN0eWxlKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiRmluZS1ncmFpbmVkIE1vRSB3aXRoIHNoYXJlZCArIHJvdXRlZCBleHBlcnRzIChEZWVwU2Vlay1Nb0Ugc3R5bGUpLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX21vZGVsOiBpbnQsIGRfZmY6IGludCxcbiAgICAgICAgICAgICAgICAgbl9zaGFyZWQ6IGludCwgbl9yb3V0ZWQ6IGludCwgdG9wX2s6IGludCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnRvcF9rID0gdG9wX2tcbiAgICAgICAgc2VsZi5yb3V0ZXIgPSBubi5MaW5lYXIoZF9tb2RlbCwgbl9yb3V0ZWQsIGJpYXM9RmFsc2UpXG4gICAgICAgICMgU2hhcmVkIGV4cGVydHM6IGFsd2F5cyBhY3RpdmUgZm9yIGV2ZXJ5IHRva2VuXG4gICAgICAgIHNlbGYuc2hhcmVkID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkX21vZGVsLCBkX2ZmKSwgbm4uR0VMVSgpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICBubi5MaW5lYXIoZF9mZiwgZF9tb2RlbCkpIGZvciBfIGluIHJhbmdlKG5fc2hhcmVkKV0pXG4gICAgICAgICMgUm91dGVkIGV4cGVydHM6IGZpbmUtZ3JhaW5lZCAoc21hbGxlciBkX2ZmKVxuICAgICAgICBzZWxmLnJvdXRlZCA9IG5uLk1vZHVsZUxpc3QoW1xuICAgICAgICAgICAgbm4uU2VxdWVudGlhbChubi5MaW5lYXIoZF9tb2RlbCwgZF9mZiksIG5uLkdFTFUoKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgbm4uTGluZWFyKGRfZmYsIGRfbW9kZWwpKSBmb3IgXyBpbiByYW5nZShuX3JvdXRlZCldKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgIyBTaGFyZWQgZXhwZXJ0IG91dHB1dCAoYWx3YXlzIGFjdGl2ZSlcbiAgICAgICAgc2hhcmVkX291dCA9IHN1bShlKHgpIGZvciBlIGluIHNlbGYuc2hhcmVkKVxuICAgICAgICAjIFJvdXRlZCBleHBlcnQgb3V0cHV0ICh0b3AtSyBvZiBOX3IpXG4gICAgICAgIE4sIEQgID0geC5zaGFwZVswXSAqIHguc2hhcGVbMV0sIHguc2hhcGVbMl1cbiAgICAgICAgeGYgICAgPSB4LnZpZXcoTiwgRClcbiAgICAgICAgcHJvYnMsIGlkeCA9IHRvcmNoLnRvcGsoRi5zb2Z0bWF4KHNlbGYucm91dGVyKHhmKSwgLTEpLCBzZWxmLnRvcF9rLCAtMSlcbiAgICAgICAgcHJvYnMgPSBwcm9icyAvIHByb2JzLnN1bSgtMSwga2VlcGRpbT1UcnVlKVxuICAgICAgICByb3V0ZWRfb3V0ID0gdG9yY2guemVyb3NfbGlrZSh4ZilcbiAgICAgICAgZm9yIGsgaW4gcmFuZ2Uoc2VsZi50b3Bfayk6XG4gICAgICAgICAgICBmb3IgZSwgZXhwZXJ0IGluIGVudW1lcmF0ZShzZWxmLnJvdXRlZCk6XG4gICAgICAgICAgICAgICAgbSA9IGlkeFs6LCBrXSA9PSBlXG4gICAgICAgICAgICAgICAgaWYgbS5hbnkoKTpcbiAgICAgICAgICAgICAgICAgICAgcm91dGVkX291dFttXSArPSBwcm9ic1ttLCBrOmsrMV0gKiBleHBlcnQoeGZbbV0pXG4gICAgICAgIHJldHVybiBzaGFyZWRfb3V0ICsgcm91dGVkX291dC52aWV3X2FzKHgpXG5cbm1vZGVsID0gRGVlcFNlZWtNb0VTdHlsZSg1MTIsIDI1Niwgbl9zaGFyZWQ9Miwgbl9yb3V0ZWQ9NjQsIHRvcF9rPTYpXG5wcmludChtb2RlbCh0b3JjaC5yYW5kbigyLCA4LCA1MTIpKS5zaGFwZSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLbm93bGVkZ2UgUmVkdW5kYW5jeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBrZXkgbW90aXZhdGlvbiBmb3IgZmluZS1ncmFpbmVkIE1vRSBpcyByZWR1Y2luZyBrbm93bGVkZ2UgcmVkdW5kYW5jeSDigJQgdGhlIHBoZW5vbWVub24gd2hlcmUgbXVsdGlwbGUgZXhwZXJ0cyBpbiBhIGNvYXJzZSBNb0UgbGVhcm4gc2ltaWxhciBmdW5jdGlvbnMgYmVjYXVzZSB0aGV5IGVhY2ggbXVzdCBjb3ZlciBhIGJyb2FkIHJhbmdlIG9mIHRva2VuIHR5cGVzLiBXaGVuIDggZXhwZXJ0cyBlYWNoIHByb2Nlc3MgMS84IG9mIHRva2VucyBhbmQgdGhlIHRva2VuIGRpc3RyaWJ1dGlvbiBpcyBub3QgY2xlYW5seSBzZXBhcmFibGUgaW50byA4IGNsdXN0ZXJzLCBleHBlcnRzIG11c3QgZ2VuZXJhbGlzZSBhY3Jvc3MgbXVsdGlwbGUgY2x1c3RlcnMsIGxlYWRpbmcgdG8gb3ZlcmxhcHBpbmcgd2VpZ2h0IG1hdHJpY2VzLiBGaW5lLWdyYWluZWQgTW9FIHdpdGggNjQgZXhwZXJ0cyBhbGxvd3MgZWFjaCBleHBlcnQgdG8gc3BlY2lhbGlzZSBpbiBhIHRpZ2h0ZXIgY2x1c3RlciwgcmVkdWNpbmcgd2VpZ2h0IG1hdHJpeCBvdmVybGFwLiBEZWVwU2Vlay1Nb0UgcXVhbnRpZmllcyB0aGlzIGJ5IG1lYXN1cmluZyBwYWlyd2lzZSBjb3NpbmUgc2ltaWxhcml0eSBiZXR3ZWVuIGV4cGVydCB3ZWlnaHQgbWF0cmljZXM6IGZpbmUtZ3JhaW5lZCBtb2RlbHMgc2hvdyBsb3dlciBtZWFuIHNpbWlsYXJpdHkgKG1vcmUgZGl2ZXJzZSBleHBlcnRpc2UpIHRoYW4gY29hcnNlIG1vZGVscywgZXZlbiBhdCBpZGVudGljYWwgdG90YWwgcGFyYW1ldGVyIGNvdW50LiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJGaW5lLUdyYWluZWQgU3BlY2lhbGlzYXRpb24iLCJjb250ZW50IjoiRmluZS1ncmFpbmVkIE1vRSB3aXRoIDY0KyBleHBlcnRzIHR5cGljYWxseSBzaG93cyBoaWdoZXIgZXhwZXJ0IHNwZWNpYWxpc2F0aW9uIOKAlCBkaWZmZXJlbnQgZXhwZXJ0cyBsZWFybiBzeW50YXggdnMgc2VtYW50aWNzIHZzIGRvbWFpbiBrbm93bGVkZ2Ug4oCUIHRoYW4gY29hcnNlIE1vRSB3aXRoIDggZXhwZXJ0cy4gQnV0IGl0IHJlcXVpcmVzIGNhcmVmdWwgbG9hZCBiYWxhbmNpbmcgYWNyb3NzIG1hbnkgbW9yZSBleHBlcnRzIGFuZCBhIHJvdXRlciB0aGF0IGNhbiBkaXN0aW5ndWlzaCBhbW9uZyA2NCsgb3B0aW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaGFyZWQgRXhwZXJ0IENvbWJpbmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZWVwU2Vlay1Nb0UgY29tYmluZXMgZmluZS1ncmFpbmVkIHJvdXRlZCBleHBlcnRzIHdpdGggYSBzbWFsbCBudW1iZXIgb2YgYWx3YXlzLWFjdGl2ZSBzaGFyZWQgZXhwZXJ0cy4gVGhlIHNoYXJlZCBleHBlcnRzIGhhbmRsZSBjb21tb24ga25vd2xlZGdlIOKAlCBwYXR0ZXJucyB0aGF0IGFwcGVhciBpbiBuZWFybHkgZXZlcnkgdG9rZW4gdHlwZSBhbmQgdGhlcmVmb3JlIHNob3VsZCBub3QgYmUgXHUwMDI3d2FzdGVkXHUwMDI3IG9uIHJvdXRlZCBleHBlcnRzIHRoYXQgc3BlY2lhbGlzZSBpbiBuYXJyb3cgZG9tYWlucy4gQnkgb2ZmbG9hZGluZyBjb21tb24gcGF0dGVybnMgdG8gc2hhcmVkIGV4cGVydHMsIHRoZSByb3V0ZWQgZXhwZXJ0cyBhcmUgZnJlZWQgdG8gc3BlY2lhbGlzZSBtb3JlIGFnZ3Jlc3NpdmVseS4gVGhpcyBpcyBhbmFsb2dvdXMgdG8gaGF2aW5nIGdlbmVyYWxpc3Qgc3RhZmYgd2hvIGhhbmRsZSByb3V0aW5lIHdvcmsgd2hpbGUgc3BlY2lhbGlzdHMgZm9jdXMgb24gY29tcGxleCBjYXNlcy4gSW4gcHJhY3RpY2UsIDLigJM0IHNoYXJlZCBleHBlcnRzIGFyZSBzdWZmaWNpZW50OyBtb3JlIHNoYXJlZCBleHBlcnRzIHJlZHVjZSB0aGUgc3BlY2lhbGlzYXRpb24gYmVuZWZpdCBvZiByb3V0aW5nLiBUaGUgbG9hZC1iYWxhbmNpbmcgYXV4aWxpYXJ5IGxvc3MgaXMgYXBwbGllZCBvbmx5IHRvIHRoZSByb3V0ZWQgZXhwZXJ0cyAoc2hhcmVkIGV4cGVydHMgYWN0aXZhdGUgZm9yIGFsbCB0b2tlbnMsIHNvIHRoZXkgYXJlIGFsd2F5cyBwZXJmZWN0bHkgYmFsYW5jZWQpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZXhwZXJ0X3NwZWNpYWxpc2F0aW9uX3N3ZWVwKG5fZXhwZXJ0c19saXN0OiBsaXN0LCBuX3Rva2VuczogaW50ID0gMTAwMDAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvcF9rOiBpbnQgPSAyKSAtXHUwMDNlIE5vbmU6XG4gICAgXCJcIlwiTWVhc3VyZSByb3V0aW5nIGVudHJvcHkgYXMgYSBwcm94eSBmb3Igc3BlY2lhbGlzYXRpb24gYWNyb3NzIGV4cGVydCBjb3VudHMuXG4gICAgSGlnaGVyIGVudHJvcHkgcGVyIGV4cGVydCA9IGJyb2FkZXIgY292ZXJhZ2UgPSBsZXNzIHNwZWNpYWxpc2F0aW9uLlwiXCJcIlxuICAgIHByaW50KGZcIntcdTAwMjdOIGV4cGVydHNcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdleHBlcnQgaGlkZGVuXHUwMDI3Olx1MDAzZTE0fSB7XHUwMDI3dG9wX2tcdTAwMjc6XHUwMDNlN30gXCJcbiAgICAgICAgICBmXCJ7XHUwMDI3YWN0aXZlIGZyYWNcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdsb2FkX2N2X2VzdFx1MDAyNzpcdTAwM2UxMn1cIilcbiAgICBmb3IgbiBpbiBuX2V4cGVydHNfbGlzdDpcbiAgICAgICAgIyBTaW11bGF0ZSB1bmlmb3JtIHJvdXRpbmcgKGJlc3QgY2FzZSBmb3IgbG9hZCBiYWxhbmNlKVxuICAgICAgICBjb3VudHMgPSB0b3JjaC56ZXJvcyhuKVxuICAgICAgICBmb3IgXyBpbiByYW5nZShuX3Rva2Vucyk6XG4gICAgICAgICAgICBjaG9zZW4gPSB0b3JjaC5yYW5kcGVybShuKVs6dG9wX2tdXG4gICAgICAgICAgICBjb3VudHNbY2hvc2VuXSArPSAxXG4gICAgICAgIGxvYWQgPSBjb3VudHMgLyBjb3VudHMuc3VtKClcbiAgICAgICAgY3YgICA9IChsb2FkLnN0ZCgpIC8gbG9hZC5tZWFuKCkpLml0ZW0oKVxuICAgICAgICBhY3RpdmVfZnJhYyA9IHRvcF9rIC8gblxuICAgICAgICBleHBlcnRfaGlkZGVuID0gZlwiZF9mZi97bi8vOH1cIiBpZiBuIFx1MDAzZT0gOCBlbHNlIFwiZF9mZlwiXG4gICAgICAgIHByaW50KGZcIntuOlx1MDAzZTEyfSB7ZXhwZXJ0X2hpZGRlbjpcdTAwM2UxNH0ge3RvcF9rOlx1MDAzZTd9IFwiXG4gICAgICAgICAgICAgIGZcInthY3RpdmVfZnJhYzpcdTAwM2UxMi4zZn0ge2N2Olx1MDAzZTEyLjRmfVwiKVxuXG5leHBlcnRfc3BlY2lhbGlzYXRpb25fc3dlZXAoWzgsIDE2LCAzMiwgNjQsIDEyOF0sIHRvcF9rPTIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmluZS1ncmFpbmVkIE1vRSBpcyBhbiBhcmNoaXRlY3R1cmFsIHJlZmluZW1lbnQgdGhhdCBpbXByb3ZlcyBleHBlcnQgc3BlY2lhbGlzYXRpb24gd2l0aG91dCBjaGFuZ2luZyB0b3RhbCBwYXJhbWV0ZXIgY291bnQgb3IgYWN0aXZlIEZMT1BzLiBCeSBzcGxpdHRpbmcgZWFjaCBvZiBOIGNvYXJzZSBleHBlcnRzIGludG8gbSBmaW5lLWdyYWluZWQgZXhwZXJ0cyBhbmQgaW5jcmVhc2luZyB0b3AtSyBwcm9wb3J0aW9uYWxseSwgdGhlIGFjdGl2ZSBjb21wdXRhdGlvbiBidWRnZXQgc3RheXMgdGhlIHNhbWUgd2hpbGUgdGhlIHJvdXRpbmcgcHJlY2lzaW9uIGltcHJvdmVzIGRyYW1hdGljYWxseS4gRGVlcFNlZWstTW9FIGRlbW9uc3RyYXRlcyB0aGF0IDY0IGZpbmUtZ3JhaW5lZCByb3V0ZWQgZXhwZXJ0cyBwbHVzIDIgc2hhcmVkIGV4cGVydHMgb3V0cGVyZm9ybSA4IGNvYXJzZSBleHBlcnRzIGF0IHRoZSBzYW1lIEZMT1BzIG9uIGRvd25zdHJlYW0gYmVuY2htYXJrcy4gVGhlIG1haW4gY29zdHMgYXJlIGluY3JlYXNlZCByb3V0aW5nIGNvbXBsZXhpdHksIGhhcmRlciBsb2FkIGJhbGFuY2luZyBhY3Jvc3MgbW9yZSBleHBlcnRzLCBhbmQgcG90ZW50aWFsbHkgd2Vha2VyIHBlci1leHBlcnQgY2FwYWNpdHkgaWYgZXhwZXJ0IGhpZGRlbiBkaW1lbnNpb24gYmVjb21lcyB0b28gc21hbGwuIFRoZSBvcHRpbWFsIGdyYW51bGFyaXR5IGRlcGVuZHMgb24gbW9kZWwgc2NhbGUgYW5kIHRyYWluaW5nIGRhdGEgZGl2ZXJzaXR5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRmluZS1ncmFpbmVkIE1vRTogbWFueSBzbWFsbCBleHBlcnRzICg2NOKAkzEyOCkgdnMgZmV3IGxhcmdlIG9uZXMgKDjigJMxNiksIHNhbWUgdG90YWwgcGFyYW1zIGFuZCBGTE9QcyIsIkV4cGVydHMgc3BlY2lhbGlzZSBtb3JlIG5hcnJvd2x5LCByZWR1Y2luZyB3ZWlnaHQgbWF0cml4IGNvc2luZSBzaW1pbGFyaXR5IChrbm93bGVkZ2UgcmVkdW5kYW5jeSkiLCJEZWVwU2Vlay1Nb0UgdXNlcyA2NCByb3V0ZWQgKyAyIHNoYXJlZCBleHBlcnRzOyByb3V0ZXMgdG9wLTYgcm91dGVkIGV4cGVydHMgcGVyIHRva2VuIiwiTG9hZCBiYWxhbmNpbmcgaXMgaGFyZGVyIGFjcm9zcyA2NCsgZXhwZXJ0cyDigJQgdXNlIHN0cm9uZ2VyIGF1eCBsb3NzIG9yIGV4cGVydCBjaG9pY2Ugcm91dGluZyIsIlNoYXJlZCBleHBlcnRzIGhhbmRsZSBjb21tb24gcGF0dGVybnM7IGZyZWVzIHJvdXRlZCBleHBlcnRzIHRvIHNwZWNpYWxpc2UgbW9yZSBhZ2dyZXNzaXZlbHkiLCJTd2VldCBzcG90OiAzMuKAkzEyOCBleHBlcnRzIGZvciB0eXBpY2FsIExMTSBzY2FsZXM7IGJleW9uZCAyNTYgcm91dGluZyBxdWFsaXR5IGRlZ3JhZGVzIl19XQ=="
---
# Fine-Grained Mixture of Experts

Traditional MoE architectures use a small number of large experts — typically 8 or 16, each with the same hidden dimension as a dense FFN. Fine-grained MoE (Dai et al., 2024, DeepSeek-MoE; and subsequent work) challenges this default by splitting each expert into many smaller sub-experts. Instead of 8 experts each with hidden dimension d_ff, fine-grained MoE uses 64 or 128 experts each with hidden dimension d_ff/8. Total parameter count is identical, top-K active FLOPs are identical (routing top-16 of 128 small experts ≈ routing top-2 of 16 large experts), but the granularity of the routing decision is much finer. This finer granularity allows each expert to specialise more narrowly, reducing knowledge redundancy and improving the information efficiency of the parameter budget.

## Overview

Fine-grained MoE was introduced in the DeepSeek-MoE paper (Dai et al., 2024) and adopted in DeepSeek-V2 (236B total, 21B active). The key observation is that coarse MoE (8 large experts) forces each expert to be general — it cannot afford to specialise too narrowly because it must process 1/8 of all tokens including many for which it has no expertise. Fine-grained MoE (64–128 small experts) allows each expert to process only 1/64–1/128 of tokens, enabling much tighter specialisation. Routing top-K_r of N_r fine-grained experts (with K_r/N_r = K/N, same active fraction) produces identical compute while gaining routing precision. The practical benefit is measurable improvement in downstream task accuracy at the same FLOPs, with the main cost being more complex routing and load-balancing across many more experts.

## Coarse vs Fine-Grained Experts

The fundamental difference between coarse and fine-grained MoE is the granularity of the expert function. A coarse expert with hidden dimension d_ff learns a general transformation that applies to many token types. A fine-grained expert with hidden dimension d_ff/m (for m-fold splitting) learns a narrower transformation that applies to m times fewer tokens on average. The analogy is professional versus generalist: a coarse expert is like a generalist doctor who sees every patient; a fine-grained expert is like a specialist who sees only patients with a specific condition. The specialist can develop much deeper expertise in that narrow domain. The challenge is that with many small experts, the routing decision (which specialist?) becomes more critical — a misrouted token receives a less-applicable transformation.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class FineGrainedMoELayer(nn.Module):
    """Fine-grained MoE: many small experts vs few large experts.
    Same total params and same active FLOPs as coarse MoE."""
    def __init__(self, d_model: int, d_ff: int,
                 n_experts: int, top_k: int):
        super().__init__()
        # Each expert has d_ff hidden units (same as coarse)
        # but n_experts is much larger (e.g., 64 vs 8)
        self.n_experts, self.top_k = n_experts, top_k
        self.router  = nn.Linear(d_model, n_experts, bias=False)
        self.w1 = nn.Parameter(torch.randn(n_experts, d_model, d_ff) * 0.02)
        self.w2 = nn.Parameter(torch.randn(n_experts, d_ff, d_model) * 0.02)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        N, D = x.shape[0] * x.shape[1], x.shape[2]
        xf   = x.view(N, D)
        probs, idx = torch.topk(F.softmax(self.router(xf), -1), self.top_k, -1)
        probs = probs / probs.sum(-1, keepdim=True)
        out   = torch.zeros_like(xf)
        for k in range(self.top_k):
            for e in range(self.n_experts):
                m = idx[:, k] == e
                if not m.any(): continue
                h = F.gelu(xf[m] @ self.w1[e])
                out[m] += probs[m, k:k+1] * (h @ self.w2[e])
        return out.view_as(x)

# Coarse: 8 experts, top-2 | Fine-grained: 64 experts, top-16 (same active fraction)
coarse = FineGrainedMoELayer(512, 2048, n_experts=8,  top_k=2)
fine   = FineGrainedMoELayer(512, 2048, n_experts=64, top_k=16)
print(f"Coarse params: {sum(p.numel() for p in coarse.parameters()):,}")
print(f"Fine   params: {sum(p.numel() for p in fine.parameters()):,}")
```

## DeepSeek-MoE Design

DeepSeek-MoE uses N_r=64 fine-grained routed experts (compared to Mixtral's 8), routing top-K_r=6 per token. Additionally, it adds N_s=2 shared experts that always activate for every token regardless of routing — these handle common knowledge that every token needs. The routing is: output = sum(shared_expert_i(x)) + sum_{k in top-K_r} g_k * E_k(x). The 64 small routed experts together with 2 always-active shared experts give DeepSeek-MoE significantly higher specialisation than a comparable 8-expert model. The paper demonstrates that the fine-grained experts develop more distinct weight matrices (lower cosine similarity between expert weight pairs) and show sharper token routing patterns than coarse experts trained with the same compute budget.

```python
import torch
import torch.nn.functional as F
from itertools import combinations

def measure_knowledge_redundancy(expert_weights: torch.Tensor) -> dict:
    """Measure cosine similarity between expert weight matrices.
    Lower mean similarity = more specialisation = less redundancy.
    expert_weights: (n_experts, d_in * d_out) flattened weight vectors."""
    n = expert_weights.shape[0]
    norms  = F.normalize(expert_weights, dim=-1)            # (E, D)
    sims   = []
    for i, j in combinations(range(n), 2):
        sims.append((norms[i] * norms[j]).sum().item())
    sims = torch.tensor(sims)
    return {"mean_sim": sims.mean().item(),
            "std_sim":  sims.std().item(),
            "max_sim":  sims.max().item()}

# Simulate random expert weights for coarse (8) vs fine-grained (64)
torch.manual_seed(42)
for name, n_exp in [("coarse-8", 8), ("fine-64", 64)]:
    W = torch.randn(n_exp, 512 * 128)                      # flatten d_model x d_ff
    r = measure_knowledge_redundancy(W)
    print(f"{name:>10}: mean_sim={r['mean_sim']:.4f}  max_sim={r['max_sim']:.4f}")
```

## Expert Granularity Tradeoffs

Increasing the number of experts while holding total parameters and active FLOPs constant involves genuine tradeoffs. Smaller individual experts have lower hidden dimension (d_ff/m for m-fold split) and therefore lower representational capacity per expert. For very fine-grained experts (m=16, hidden dim reduced 16x), each expert may lack the capacity to learn complex transformations. Additionally, with many experts, routing becomes more critical: the router must correctly assign each token to its most appropriate expert among 64 or 128 options, a harder problem than choosing among 8. This requires the router to develop finer-grained representations and may require longer training to converge. The sweet spot in practice appears to be around 32–128 experts for most model scales, balancing specialisation benefits against per-expert capacity and routing difficulty.

| Config | N experts | Expert hidden dim | Top-K | Active params (M) | Specialisation |
| --- | --- | --- | --- | --- | --- |
| GShard 2048E | 2048 | d_ff (full) | 2 | ~2x dense FFN | Very high (but routing hard) |
| Switch-C 2048E | 2048 | d_ff (full) | 1 | ~1x dense FFN | High |
| Mixtral 8E | 8 | d_ff (full) | 2 | ~2x dense FFN | Moderate |
| DeepSeek-MoE 64E | 64 | d_ff/8 | 6 routed + 2 shared | ~1x dense FFN | High |
| Fine-grained 128E | 128 | d_ff/16 | 16 | ~1x dense FFN | Very high |

## Routing with Many Experts

Routing among 64 or 128 experts introduces new challenges. The router is a linear layer of size d_model × n_experts; at n_experts=128, this is d_model × 128 parameters — still a small fraction of total params. The softmax over 128 logits is more diffuse than over 8, meaning the top-K probability mass is more spread out. This can make the router signal weaker and slower to develop. DeepSeek-MoE addresses this with a normalised top-K selection: after computing the top-K experts, the gating weights are renormalised to sum to 1, sharpening the signal. Additionally, the load-balancing challenge is harder with more experts — ensuring each of 128 experts receives roughly 1/128 of tokens requires stronger regularisation or expert choice routing.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DeepSeekMoEStyle(nn.Module):
    """Fine-grained MoE with shared + routed experts (DeepSeek-MoE style)."""
    def __init__(self, d_model: int, d_ff: int,
                 n_shared: int, n_routed: int, top_k: int):
        super().__init__()
        self.top_k = top_k
        self.router = nn.Linear(d_model, n_routed, bias=False)
        # Shared experts: always active for every token
        self.shared = nn.ModuleList([
            nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(),
                          nn.Linear(d_ff, d_model)) for _ in range(n_shared)])
        # Routed experts: fine-grained (smaller d_ff)
        self.routed = nn.ModuleList([
            nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(),
                          nn.Linear(d_ff, d_model)) for _ in range(n_routed)])

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Shared expert output (always active)
        shared_out = sum(e(x) for e in self.shared)
        # Routed expert output (top-K of N_r)
        N, D  = x.shape[0] * x.shape[1], x.shape[2]
        xf    = x.view(N, D)
        probs, idx = torch.topk(F.softmax(self.router(xf), -1), self.top_k, -1)
        probs = probs / probs.sum(-1, keepdim=True)
        routed_out = torch.zeros_like(xf)
        for k in range(self.top_k):
            for e, expert in enumerate(self.routed):
                m = idx[:, k] == e
                if m.any():
                    routed_out[m] += probs[m, k:k+1] * expert(xf[m])
        return shared_out + routed_out.view_as(x)

model = DeepSeekMoEStyle(512, 256, n_shared=2, n_routed=64, top_k=6)
print(model(torch.randn(2, 8, 512)).shape)
```

## Knowledge Redundancy

A key motivation for fine-grained MoE is reducing knowledge redundancy — the phenomenon where multiple experts in a coarse MoE learn similar functions because they each must cover a broad range of token types. When 8 experts each process 1/8 of tokens and the token distribution is not cleanly separable into 8 clusters, experts must generalise across multiple clusters, leading to overlapping weight matrices. Fine-grained MoE with 64 experts allows each expert to specialise in a tighter cluster, reducing weight matrix overlap. DeepSeek-MoE quantifies this by measuring pairwise cosine similarity between expert weight matrices: fine-grained models show lower mean similarity (more diverse expertise) than coarse models, even at identical total parameter count.

> **Fine-Grained Specialisation**: Fine-grained MoE with 64+ experts typically shows higher expert specialisation — different experts learn syntax vs semantics vs domain knowledge — than coarse MoE with 8 experts. But it requires careful load balancing across many more experts and a router that can distinguish among 64+ options.

## Shared Expert Combination

DeepSeek-MoE combines fine-grained routed experts with a small number of always-active shared experts. The shared experts handle common knowledge — patterns that appear in nearly every token type and therefore should not be 'wasted' on routed experts that specialise in narrow domains. By offloading common patterns to shared experts, the routed experts are freed to specialise more aggressively. This is analogous to having generalist staff who handle routine work while specialists focus on complex cases. In practice, 2–4 shared experts are sufficient; more shared experts reduce the specialisation benefit of routing. The load-balancing auxiliary loss is applied only to the routed experts (shared experts activate for all tokens, so they are always perfectly balanced).

```python
import torch
import numpy as np

def expert_specialisation_sweep(n_experts_list: list, n_tokens: int = 10000,
                                top_k: int = 2) -> None:
    """Measure routing entropy as a proxy for specialisation across expert counts.
    Higher entropy per expert = broader coverage = less specialisation."""
    print(f"{'N experts':>12} {'expert hidden':>14} {'top_k':>7} "
          f"{'active frac':>12} {'load_cv_est':>12}")
    for n in n_experts_list:
        # Simulate uniform routing (best case for load balance)
        counts = torch.zeros(n)
        for _ in range(n_tokens):
            chosen = torch.randperm(n)[:top_k]
            counts[chosen] += 1
        load = counts / counts.sum()
        cv   = (load.std() / load.mean()).item()
        active_frac = top_k / n
        expert_hidden = f"d_ff/{n//8}" if n >= 8 else "d_ff"
        print(f"{n:>12} {expert_hidden:>14} {top_k:>7} "
              f"{active_frac:>12.3f} {cv:>12.4f}")

expert_specialisation_sweep([8, 16, 32, 64, 128], top_k=2)
```

## Key Takeaways

Fine-grained MoE is an architectural refinement that improves expert specialisation without changing total parameter count or active FLOPs. By splitting each of N coarse experts into m fine-grained experts and increasing top-K proportionally, the active computation budget stays the same while the routing precision improves dramatically. DeepSeek-MoE demonstrates that 64 fine-grained routed experts plus 2 shared experts outperform 8 coarse experts at the same FLOPs on downstream benchmarks. The main costs are increased routing complexity, harder load balancing across more experts, and potentially weaker per-expert capacity if expert hidden dimension becomes too small. The optimal granularity depends on model scale and training data diversity.

- Fine-grained MoE: many small experts (64–128) vs few large ones (8–16), same total params and FLOPs
- Experts specialise more narrowly, reducing weight matrix cosine similarity (knowledge redundancy)
- DeepSeek-MoE uses 64 routed + 2 shared experts; routes top-6 routed experts per token
- Load balancing is harder across 64+ experts — use stronger aux loss or expert choice routing
- Shared experts handle common patterns; frees routed experts to specialise more aggressively
- Sweet spot: 32–128 experts for typical LLM scales; beyond 256 routing quality degrades

