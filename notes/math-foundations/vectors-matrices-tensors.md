---
title: "Vectors, Matrices, and Tensors"
slug: "vectors-matrices-tensors"
description: "A deep dive into shapes, rank, memory layout, strides, broadcasting, and GPU performance for vectors, matrices, and tensors."
tags: ["linear-algebra", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmVjdG9ycywgbWF0cmljZXMsIGFuZCB0ZW5zb3JzIGFyZSB0aGUgZm91bmRhdGlvbmFsIGRhdGEgc3RydWN0dXJlcyBvZiBtYWNoaW5lIGxlYXJuaW5nLiBBICoqdmVjdG9yKiogaXMgYSAxRCBvcmRlcmVkIGxpc3Qgb2YgbnVtYmVycywgYSAqKm1hdHJpeCoqIGlzIGEgMkQgcmVjdGFuZ3VsYXIgYXJyYXksIGFuZCBhICoqdGVuc29yKiogaXMgdGhlIE4tZGltZW5zaW9uYWwgZ2VuZXJhbGl6YXRpb24uIE1hc3RlcmluZyBob3cgdGhlc2Ugc3RydWN0dXJlcyBhcmUgc2hhcGVkLCBsYWlkIG91dCBpbiBtZW1vcnksIGFuZCBvcGVyYXRlZCBvbiBpcyBlc3NlbnRpYWwgZm9yIHdyaXRpbmcgY29ycmVjdCBhbmQgaGlnaC1wZXJmb3JtYW5jZSBNTCBjb2RlIOKAlCBmcm9tIE51bVB5IHNjcmlwdHMgdG8gQ1VEQSBrZXJuZWxzLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNoYXBlcywgUmFuaywgYW5kIERpbWVuc2lvbmFsaXR5In0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgKipyYW5rKiogb2YgYSB0ZW5zb3IgaXMgaXRzIG51bWJlciBvZiBheGVzIChkaW1lbnNpb25zKS4gVGhpcyBpcyBkaXN0aW5jdCBmcm9tICptYXRyaXggcmFuayogKGxpbmVhciBpbmRlcGVuZGVuY2Ugb2Ygcm93cy9jb2x1bW5zKS4gQSBzY2FsYXIgaXMgcmFuay0wLCBhIHZlY3RvciByYW5rLTEsIGEgbWF0cml4IHJhbmstMi4gTW9kZXJuIGRlZXAgbGVhcm5pbmcgdXNlcyByYW5rLTQgdGVuc29ycyByb3V0aW5lbHk6IHNoYXBlIGAoQiwgQywgSCwgVylgIHJlcHJlc2VudHMgYSBiYXRjaCBvZiBCIGltYWdlcyBlYWNoIHdpdGggQyBjaGFubmVscywgaGVpZ2h0IEgsIGFuZCB3aWR0aCBXLiBFdmVyeSBlbGVtZW50IGlzIGFkZHJlc3NlZCBieSBhbiBpbmRleCB0dXBsZSwgZS5nLiwgYFRbYiwgYywgaCwgd11gLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnAsIHRvcmNoXG5cbnNjYWxhciA9IG5wLmZsb2F0MzIoMy4xNCkgICAgICAgICAgICMgcmFuay0wLCBzaGFwZSAoKVxudmVjdG9yID0gbnAuYXJyYXkoWzEuLCAyLiwgMy5dKSAgICAgIyByYW5rLTEsIHNoYXBlICgzLClcbm1hdHJpeCA9IG5wLm9uZXMoKDQsIDUpKSAgICAgICAgICAgICMgcmFuay0yLCBzaGFwZSAoNCw1KVxudGVuc29yID0gdG9yY2guemVyb3MoMzIsIDMsIDIyNCwgMjI0KSAgIyByYW5rLTQsIHNoYXBlICgzMiwzLDIyNCwyMjQpXG5cbmZvciB0IGluIFtzY2FsYXIsIHZlY3RvciwgbWF0cml4XTpcbiAgICBwcmludChmJ25kaW09e3QubmRpbX0gIHNoYXBlPXt0LnNoYXBlfSAgZHR5cGU9e3QuZHR5cGV9JykifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCcm9hZGNhc3RpbmcgUnVsZXMgKE51bVB5L1B5VG9yY2ggU3R5bGUpIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCcm9hZGNhc3RpbmcgbGV0cyB5b3UgYXBwbHkgZWxlbWVudC13aXNlIG9wZXJhdGlvbnMgb24gYXJyYXlzIG9mIGRpZmZlcmVudCAoYnV0IGNvbXBhdGlibGUpIHNoYXBlcyB3aXRob3V0IGV4cGxpY2l0IGRhdGEgY29weWluZy4gUnVsZXMgYXJlIGFwcGxpZWQgKipyaWdodC10by1sZWZ0KiogYWNyb3NzIGRpbWVuc2lvbnM6XG5cbjEuIFByZXBlbmQgMXMgdG8gdGhlIHNob3J0ZXIgc2hhcGUgdW50aWwgYm90aCBoYXZlIHRoZSBzYW1lIG51bWJlciBvZiBheGVzLlxuMi4gSW4gZWFjaCBheGlzLCBzaXplcyBtdXN0IGJlIGVxdWFsLCBvciBvbmUgb2YgdGhlbSBtdXN0IGJlIDEgKHdoaWNoIGlzIHZpcnR1YWxseSBzdHJldGNoZWQpLlxuMy4gSWYgbmVpdGhlciBjb25kaXRpb24gaG9sZHMsIGFuIGVycm9yIGlzIHJhaXNlZC5cblxuRXhhbXBsZXM6IGAoMywxKSArICgxLDQpIOKGkiAoMyw0KWAsIGAoMzIsNTEyKSArICg1MTIsKSDihpIgKDMyLDUxMilgLCBgKDgsMSw0KSAqICgzLDQpIOKGkiAoOCwzLDQpYC4gVGhpcyBpcyB1YmlxdWl0b3VzIGluIE1MOiBhZGRpbmcgYSBiaWFzIHZlY3RvciBhY3Jvc3MgYSBiYXRjaCwgc2NhbGluZyByb3dzIGJ5IGEgd2VpZ2h0IHZlY3RvciwgY29tcHV0aW5nIHBhaXJ3aXNlIGRpc3RhbmNlcy4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgQ2xhc3NpYyBiaWFzIGFkZGl0aW9uOiBubyBmb3ItbG9vcCBuZWVkZWRcbmJhdGNoID0gbnAucmFuZG9tLnJhbmRuKDMyLCA1MTIpICAgIyAoYmF0Y2hfc2l6ZSwgZmVhdHVyZXMpXG5iaWFzICA9IG5wLnJhbmRvbS5yYW5kbig1MTIpICAgICAgICMgKGZlYXR1cmVzLCkgLT4gYnJvYWRjYXN0IHRvICgxLDUxMilcbm91dCAgID0gYmF0Y2ggKyBiaWFzICAgICAgICAgICAgICAgIyAoMzIsIDUxMilcblxuIyBPdXRlciBwcm9kdWN0IHZpYSBicm9hZGNhc3RpbmdcbnUgPSBucC5hcnJheShbWzFdLFsyXSxbM11dKSAgICAgICAgIyAoMywxKVxudiA9IG5wLmFycmF5KFtbMTAsMjAsMzAsNDBdXSkgICAgICAjICgxLDQpXG5vdXRlciA9IHUgKiB2ICAgICAgICAgICAgICAgICAgICAgICMgKDMsNCkgLS0gb3V0ZXIgcHJvZHVjdCFcbnByaW50KG91dGVyKVxuXG4jIFBhaXJ3aXNlIEwyIGRpc3RhbmNlczogKG4sMSxkKSAtICgxLG0sZCkgLT4gKG4sbSxkKSAtPiAobixtKVxuWCA9IG5wLnJhbmRvbS5yYW5kbigxMDAsIDY0KVxuWSA9IG5wLnJhbmRvbS5yYW5kbigyMDAsIDY0KVxuZGlmZiA9IFhbOixOb25lLDpdIC0gWVtOb25lLDosOl0gICAjICgxMDAsMjAwLDY0KVxuZGlzdHMgPSBucC5zcXJ0KChkaWZmKioyKS5zdW0oLTEpKSAjICgxMDAsMjAwKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1lbW9yeSBMYXlvdXQ6IFJvdy1NYWpvciB2cyBDb2x1bW4tTWFqb3IifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik11bHRpLWRpbWVuc2lvbmFsIGFycmF5cyBhcmUgc3RvcmVkIGFzIGEgZmxhdCAxRCBzZXF1ZW5jZSBpbiBSQU0uIFRoZSAqKm1lbW9yeSBsYXlvdXQqKiBkZXRlcm1pbmVzIHRoZSBvcmRlcmluZyBvZiBlbGVtZW50czpcblxuLSAqKlJvdy1tYWpvciAoQyBvcmRlcikqKjogUmlnaHRtb3N0IGF4aXMgdmFyaWVzIGZhc3Rlc3QuIEZvciBgW1thLGIsY10sW2QsZSxmXV1gLCBtZW1vcnkgaXMgYGEsYixjLGQsZSxmYC4gVXNlZCBieSBDLCBOdW1QeSAoZGVmYXVsdCksIFB5VG9yY2guXG4tICoqQ29sdW1uLW1ham9yIChGb3J0cmFuIG9yZGVyKSoqOiBMZWZ0bW9zdCBheGlzIHZhcmllcyBmYXN0ZXN0LiBNZW1vcnkgaXMgYGEsZCxiLGUsYyxmYC4gVXNlZCBieSBGb3J0cmFuLCBNQVRMQUIsIFIsIEp1bGlhLlxuXG5UaGlzIG1hdHRlcnMgZW5vcm1vdXNseSBmb3IgcGVyZm9ybWFuY2U6IENQVXMgbG9hZCBkYXRhIGluIGNhY2hlIGxpbmVzICg2NCBieXRlcyA9IDE2IGZsb2F0cykuIEFjY2Vzc2luZyBlbGVtZW50cyBpbiBzdG9yYWdlIG9yZGVyIGFjaGlldmVzIG5lYXItcGVhayB0aHJvdWdocHV0OyBhY2Nlc3NpbmcgYWNyb3NzIHRoZSBzdHJpZGUgZGlyZWN0aW9uIGNhdXNlcyBjYWNoZSBtaXNzZXMgYW5kIGNhbiBiZSAxMOKAkzEwMMOXIHNsb3dlci4ifSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkJMQVMgTGlicmFyaWVzIGFuZCBMYXlvdXQgQXNzdW1wdGlvbnMiLCJjb250ZW50IjoiQkxBUyBhbmQgTEFQQUNLICh0aGUgYmFja2VuZHMgZm9yIG51bXB5LmRvdCBhbmQgdG9yY2gubW0pIHdlcmUgd3JpdHRlbiBpbiBGb3J0cmFuIGFuZCBvcmlnaW5hbGx5IGV4cGVjdGVkIGNvbHVtbi1tYWpvciBhcnJheXMuIE51bVB5IGhhbmRsZXMgdGhpcyB0cmFuc3BhcmVudGx5IGJ5IHBhc3NpbmcgYXBwcm9wcmlhdGUgdHJhbnNwb3NlIGZsYWdzIHRvIEJMQVMgcm91dGluZXMsIHNvIHlvdSBub3JtYWxseSBkb24ndCBuZWVkIHRvIHdvcnJ5LiBIb3dldmVyLCBpZiB5b3UncmUgd3JpdGluZyBjdXN0b20gQyBleHRlbnNpb25zIG9yIGNhbGxpbmcgQkxBUyBkaXJlY3RseSwgYWx3YXlzIGNoZWNrIHdoaWNoIGxheW91dCBpcyBleHBlY3RlZCB0byBhdm9pZCBzdWJ0bGUgY29ycmVjdG5lc3MgYW5kIHBlcmZvcm1hbmNlIGJ1Z3MuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RyaWRlczogVGhlIE1lY2hhbmlzbSBCZWhpbmQgWmVyby1Db3B5IE9wZXJhdGlvbnMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgKipzdHJpZGUqKiBpcyB0aGUgbnVtYmVyIG9mIGVsZW1lbnRzIHRvIGFkdmFuY2UgaW4gbWVtb3J5IHdoZW4gbW92aW5nIG9uZSBzdGVwIGFsb25nIGEgZ2l2ZW4gYXhpcy4gRm9yIGEgZmxvYXQzMiBtYXRyaXggb2Ygc2hhcGUgYCgzLDQpYCBpbiByb3ctbWFqb3Igb3JkZXI6XG5cbi0gU3RyaWRlIGFsb25nIGF4aXMgMCAobmV4dCByb3cpOiA0IGVsZW1lbnRzXG4tIFN0cmlkZSBhbG9uZyBheGlzIDEgKG5leHQgY29sdW1uKTogMSBlbGVtZW50XG5cblRyYW5zcG9zaW5nIGEgbWF0cml4IGp1c3QgKipzd2FwcyB0aGUgc3RyaWRlcyoqIOKAlCBubyBkYXRhIG1vdmVtZW50IG9jY3Vycy4gYEEuVGAgaGFzIHN0cmlkZXMgYCgxLDQpYCBpbnN0ZWFkIG9mIGAoNCwxKWAuIFRoaXMgbWFrZXMgdHJhbnNwb3NlIE8oMSkgaW4gdGltZSBhbmQgbWVtb3J5LCBidXQgdGhlIHJlc3VsdCBpcyAqbm9uLWNvbnRpZ3VvdXMqOiBzdWNjZXNzaXZlIGVsZW1lbnRzIG9mIGFueSByb3cgYXJlIDQgZWxlbWVudHMgYXBhcnQgaW4gbWVtb3J5LCB3aGljaCBodXJ0cyBjYWNoZSBwZXJmb3JtYW5jZSBmb3Igc3Vic2VxdWVudCByb3ctb3JpZW50ZWQgb3BlcmF0aW9ucy4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbkEgPSB0b3JjaC5yYW5kbigzLCA0KSAgICAgICAgICAgICAgIyBjb250aWd1b3VzIHJvdy1tYWpvclxucHJpbnQoJ3NoYXBlOicsIEEuc2hhcGUpICAgICAgICAgICAjICgzLCA0KVxucHJpbnQoJ3N0cmlkZXM6JywgQS5zdHJpZGUoKSkgICAgICAjICg0LCAxKSAtLSBpbiBlbGVtZW50c1xucHJpbnQoJ2NvbnRpZ3VvdXM/JywgQS5pc19jb250aWd1b3VzKCkpICAjIFRydWVcblxuQVQgPSBBLlQgICAgICAgICAgICAgICAgICAgICAgICAgICAjIE5PIGNvcHkgLS0ganVzdCBzd2FwcGVkIHN0cmlkZXNcbnByaW50KCdBVCBzdHJpZGVzOicsIEFULnN0cmlkZSgpKSAgICAgICAgICMgKDEsIDQpXG5wcmludCgnQVQgY29udGlndW91cz8nLCBBVC5pc19jb250aWd1b3VzKCkpICMgRmFsc2UhXG5cbiMgLmNvbnRpZ3VvdXMoKSBhbGxvY2F0ZXMgbmV3IG1lbW9yeSBhbmQgY29waWVzIGVsZW1lbnRzIGluIEMgb3JkZXJcbkFUX2MgPSBBVC5jb250aWd1b3VzKClcbnByaW50KCdBVF9jIHN0cmlkZXM6JywgQVRfYy5zdHJpZGUoKSkgICAgICAjICgzLCAxKSAtLSBiYWNrIHRvIEMgb3JkZXJcblxuIyBWZXJpZnk6IHRyYW5zcG9zaW5nIHR3aWNlIGNvc3RzIG9uZSBjb3B5IChub3QgemVybylcbmltcG9ydCB0aW1lXG5iaWcgPSB0b3JjaC5yYW5kbig0MDk2LCA0MDk2KVxuXyA9IGJpZy5ULmNvbnRpZ3VvdXMoKSAgIyBvbmUgYWxsb2NhdGlvbiArIG1lbWNvcHkifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXNoYXBlIHZzIFZpZXcgaW4gUHlUb3JjaCJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQm90aCBvcGVyYXRpb25zIGNoYW5nZSBhbiBhcnJheSdzIHNoYXBlLCBidXQgdGhlaXIgbWVtb3J5IHNlbWFudGljcyBkaWZmZXI6XG5cbi0gKipgdmlldyhuZXdfc2hhcGUpYCoqOiBSZXR1cm5zIGEgdGVuc29yIHNoYXJpbmcgdGhlICpzYW1lIHN0b3JhZ2UqLiBaZXJvLWNvcHkuIFJlcXVpcmVzIHRoZSB0ZW5zb3IgdG8gYmUgY29udGlndW91cyBpbiBtZW1vcnkuIFJhaXNlcyBgUnVudGltZUVycm9yYCBpZiBjYWxsZWQgb24gYSBub24tY29udGlndW91cyB0ZW5zb3IuIFRoZSBzaGFwZSBtdXN0IGJlIGNvbXBhdGlibGUgKHNhbWUgbnVtYmVyIG9mIGVsZW1lbnRzKS5cbi0gKipgcmVzaGFwZShuZXdfc2hhcGUpYCoqOiBSZXR1cm5zIGEgdmlldyBpZiB0aGUgdGVuc29yIGlzIGNvbnRpZ3VvdXMsIG90aGVyd2lzZSBzaWxlbnRseSBhbGxvY2F0ZXMgYW5kIGNvcGllcy4gQWx3YXlzIHN1Y2NlZWRzIGZvciBjb21wYXRpYmxlIHNoYXBlcy4gSGlkZXMgbWVtb3J5IGFsbG9jYXRpb25zIGZyb20gdGhlIGNhbGxlci5cblxuQSBndWlkaW5nIHByaW5jaXBsZTogdXNlIGB2aWV3YCBpbiBwZXJmb3JtYW5jZS1jcml0aWNhbCBwYXRocyB3aGVuIHlvdSBoYXZlIHZlcmlmaWVkIGNvbnRpZ3VpdHksIHNvIHRoYXQgdW5leHBlY3RlZCBjb3BpZXMgc3VyZmFjZSBhcyBlcnJvcnMuIFVzZSBgcmVzaGFwZWAgZm9yIGNvcnJlY3RuZXNzIHdoZW4gY29udGlndWl0eSBpcyB1bmNlcnRhaW4uIn0sCiAgeyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuXG54ID0gdG9yY2gucmFuZG4oMiwgMywgNCkgICAgICAgICAgICMgMjQgZWxlbWVudHMsIGNvbnRpZ3VvdXNcblxuIyB2aWV3OiB6ZXJvLWNvcHksIHNhbWUgc3RvcmFnZVxueSA9IHgudmlldyg2LCA0KVxucHJpbnQoeS5kYXRhX3B0cigpID09IHguZGF0YV9wdHIoKSkgICMgVHJ1ZVxuXG4jIHBlcm11dGUgLT4gbm9uLWNvbnRpZ3VvdXNcbnhwID0geC5wZXJtdXRlKDIsIDAsIDEpICAgICAgICAgICAgIyAoNCwgMiwgMyksIG5vbi1jb250aWd1b3VzXG50cnk6XG4gICAgeHAudmlldyg4LCAzKSAgICAgICAgICAgICAgICAgICAjIFJ1bnRpbWVFcnJvciFcbmV4Y2VwdCBSdW50aW1lRXJyb3IgYXMgZTpcbiAgICBwcmludCgndmlldyBmYWlsZWQ6JywgZSlcblxueXIgPSB4cC5yZXNoYXBlKDgsIDMpICAgICAgICAgICAgICAjIHNpbGVudCBjb3B5IC0tIGRhdGFfcHRyIGRpZmZlcnNcbnByaW50KHlyLmRhdGFfcHRyKCkgPT0geHAuZGF0YV9wdHIoKSkgICMgRmFsc2VcblxuIyBUcmFuc2Zvcm1lciBwYXR0ZXJuOiBzcGxpdCBoZWFkcyBhZnRlciBwcm9qZWN0aW9uXG5CLCBULCBDID0gOCwgMTI4LCA1MTJcbkgsIEQgPSA4LCA2NCAgICAgICAgICAgICAgICAgICAgICAgIyA4IGhlYWRzLCA2NCBkaW1zIGVhY2hcbnEgPSB0b3JjaC5yYW5kbihCLCBULCBDKVxucV9oZWFkcyA9IHEudmlldyhCLCBULCBILCBEKSAgICAgICAjIHplcm8tY29weSBoZWFkIHNwbGl0XG5xX2hlYWRzID0gcV9oZWFkcy50cmFuc3Bvc2UoMSwgMikgICMgKEIsIEgsIFQsIEQpIGZvciBhdHRlbnRpb24ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHUFUgTWVtb3J5IENvYWxlc2NpbmcgYW5kIExheW91dCBQZXJmb3JtYW5jZSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTlZJRElBIEdQVSB0aHJlYWRzIGV4ZWN1dGUgaW4gZ3JvdXBzIG9mIDMyIGNhbGxlZCAqKndhcnBzKiouIFBlYWsgbWVtb3J5IGJhbmR3aWR0aCBpcyBhY2hpZXZlZCBvbmx5IHdoZW4gYWxsIDMyIHRocmVhZHMgaW4gYSB3YXJwIGFjY2VzcyBhIGNvbnRpZ3VvdXMgMTI4LWJ5dGUgcmVnaW9uIOKAlCBjYWxsZWQgKipjb2FsZXNjZWQgYWNjZXNzKiouIE5vbi1jb2FsZXNjZWQgKHN0cmlkZWQpIGFjY2VzcyBjYW4gcmVkdWNlIGVmZmVjdGl2ZSBiYW5kd2lkdGggZnJvbSA5MDAgR0IvcyAoQTEwMCkgdG8gdW5kZXIgMzAgR0Ivcy5cblxuRm9yIENOTiBmZWF0dXJlIG1hcHMsICoqTkNIVyoqIGxheW91dCAoUHlUb3JjaCBkZWZhdWx0KSBtZWFucyBjaGFubmVsIGRhdGEgZm9yIG9uZSBwaXhlbCBpcyBzcHJlYWQgYWNyb3NzIG1lbW9yeSwgd2hpbGUgKipOSFdDKioga2VlcHMgYWxsIGNoYW5uZWxzIG9mIG9uZSBwaXhlbCB0b2dldGhlci4gY3VETk4gc2VsZWN0cyB0aGUgZmFzdGVzdCBhbGdvcml0aG0gcGVyIG9wZXJhdGlvbjsgYHRvcmNoLmNoYW5uZWxzX2xhc3RgIGVuYWJsZXMgTkhXQyBzdG9yYWdlLiBGb3IgdHJhbnNmb3JtZXIgbW9kZWxzIHdpdGggbGFyZ2UgbWF0cml4IG11bHRpcGxpZXMsIGVuc3VyaW5nIGJvdGggb3BlcmFuZHMgYXJlIGNvbnRpZ3VvdXMgYW5kIHJvdy1tYWpvciBiZWZvcmUgYHRvcmNoLm1hdG11bGAgaXMgY3JpdGljYWwuIn0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkNoYW5uZWxzIExhc3QgZm9yIENOTiBBY2NlbGVyYXRpb24iLCJjb250ZW50IjoiQ29udmVydCBDTk4gbW9kZWxzIHRvIGNoYW5uZWxzLWxhc3QgbWVtb3J5IGZvcm1hdCBmb3IgMjDigJM1MCUgc3BlZWR1cHMgb24gQW1wZXJlKyBHUFVzOlxuXG4gIG1vZGVsID0gbW9kZWwudG8obWVtb3J5X2Zvcm1hdD10b3JjaC5jaGFubmVsc19sYXN0KVxuICB4ID0geC50byhtZW1vcnlfZm9ybWF0PXRvcmNoLmNoYW5uZWxzX2xhc3QpXG5cblRoaXMgYWxpZ25zIGZlYXR1cmUgbWFwIGxheW91dCB3aXRoIFRlbnNvciBDb3JlIGlucHV0IHJlcXVpcmVtZW50cy4gUHlUb3JjaCBwcm9wYWdhdGVzIHRoZSBmb3JtYXQgdGhyb3VnaCBtb3N0IENvbnYvQk4vUmVMVSBvcGVyYXRpb25zIGF1dG9tYXRpY2FsbHkuIn0sCiAgeyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk9wZXJhdGlvbiIsIkNvcGllcyBEYXRhPyIsIlJlcXVpcmVzIENvbnRpZ3VvdXM/IiwiVXNlIENhc2UiXSwicm93cyI6W1sidGVuc29yLnZpZXcoKSIsIk5ldmVyIiwiWWVzIChlcnJvciBpZiBub3QpIiwiUGVyZm9ybWFuY2UtY3JpdGljYWwgcmVzaGFwZSJdLFsidGVuc29yLnJlc2hhcGUoKSIsIk9ubHkgaWYgbmVlZGVkIiwiTm8gKGNvcGllcyBzaWxlbnRseSkiLCJHZW5lcmFsLXB1cnBvc2UgcmVzaGFwZSJdLFsidGVuc29yLlQgLyAudHJhbnNwb3NlKCkiLCJOZXZlciIsIk5vIChjaGFuZ2VzIHN0cmlkZXMpIiwiTG9naWNhbCB0cmFuc3Bvc2UiXSxbInRlbnNvci5wZXJtdXRlKCkiLCJOZXZlciIsIk5vIChyZW9yZGVycyBzdHJpZGVzKSIsIkFyYml0cmFyeSBheGlzIHJlb3JkZXIiXSxbInRlbnNvci5jb250aWd1b3VzKCkiLCJJZiBub24tY29udGlndW91cyIsIk4vQSIsIlByZXBhcmUgZm9yIHZpZXcgb3IgQ1VEQSBrZXJuZWwiXSxbInRlbnNvci5leHBhbmQoKSIsIk5ldmVyICh2aXJ0dWFsKSIsIk5vIiwiQnJvYWRjYXN0IHdpdGhvdXQgY29weSJdXX0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJUZW5zb3JzIGluIEpBWCBhbmQgTnVtUHkiLCJjb250ZW50IjoiSkFYIGFycmF5cyBhcmUgYWx3YXlzIGltbXV0YWJsZSBhbmQgcmVwcmVzZW50IHZhbHVlcywgbm90IHZpZXdzLiBKQVgncyBqaXQtY29tcGlsYXRpb24gdHJhY2VzIHRocm91Z2ggc2hhcGUvZHR5cGUgc3RhdGljYWxseSwgc28gZHluYW1pYyByZXNoYXBlcyBtdXN0IHVzZSBzaGFwZXMga25vd24gYXQgdHJhY2UgdGltZS4gTnVtUHkgZm9sbG93cyB0aGUgc2FtZSBjb250aWd1aXR5IHJ1bGVzIGFzIFB5VG9yY2ggYnV0IHVzZXMgLmZsYWdzWydDX0NPTlRJR1VPVVMnXSB0byBjaGVjayBsYXlvdXQuIFRoZSBzdHJpZGUtYmFzZWQgbWVudGFsIG1vZGVsIGFwcGxpZXMgZXF1YWxseSB0byBhbGwgZnJhbWV3b3Jrcy4ifQpdCg=="
---

# Vectors, Matrices, and Tensors

Vectors, matrices, and tensors are the foundational data structures of machine learning. A **vector** is a 1D ordered list of numbers, a **matrix** is a 2D rectangular array, and a **tensor** is the N-dimensional generalization. Mastering how these structures are shaped, laid out in memory, and operated on is essential for writing correct and high-performance ML code — from NumPy scripts to CUDA kernels.

## Shapes, Rank, and Dimensionality

The **rank** of a tensor is its number of axes (dimensions). This is distinct from *matrix rank* (linear independence of rows/columns). A scalar is rank-0, a vector rank-1, a matrix rank-2. Modern deep learning uses rank-4 tensors routinely: shape `(B, C, H, W)` represents a batch of B images each with C channels, height H, and width W. Every element is addressed by an index tuple, e.g., `T[b, c, h, w]`.

```python
import numpy as np, torch

scalar = np.float32(3.14)           # rank-0, shape ()
vector = np.array([1., 2., 3.])     # rank-1, shape (3,)
matrix = np.ones((4, 5))            # rank-2, shape (4,5)
tensor = torch.zeros(32, 3, 224, 224)  # rank-4, shape (32,3,224,224)

for t in [scalar, vector, matrix]:
    print(f'ndim={t.ndim}  shape={t.shape}  dtype={t.dtype}')
```

## Broadcasting Rules (NumPy/PyTorch Style)

Broadcasting lets you apply element-wise operations on arrays of different (but compatible) shapes without explicit data copying. Rules are applied **right-to-left** across dimensions:

1. Prepend 1s to the shorter shape until both have the same number of axes.
2. In each axis, sizes must be equal, or one of them must be 1 (which is virtually stretched).
3. If neither condition holds, an error is raised.

Examples: `(3,1) + (1,4) → (3,4)`, `(32,512) + (512,) → (32,512)`, `(8,1,4) * (3,4) → (8,3,4)`. This is ubiquitous in ML: adding a bias vector across a batch, scaling rows by a weight vector, computing pairwise distances.

```python
import numpy as np

# Classic bias addition: no for-loop needed
batch = np.random.randn(32, 512)   # (batch_size, features)
bias  = np.random.randn(512)       # (features,) -> broadcast to (1,512)
out   = batch + bias               # (32, 512)

# Outer product via broadcasting
u = np.array([[1],[2],[3]])        # (3,1)
v = np.array([[10,20,30,40]])      # (1,4)
outer = u * v                      # (3,4) -- outer product!
print(outer)

# Pairwise L2 distances: (n,1,d) - (1,m,d) -> (n,m,d) -> (n,m)
X = np.random.randn(100, 64)
Y = np.random.randn(200, 64)
diff = X[:,None,:] - Y[None,:,:]   # (100,200,64)
dists = np.sqrt((diff**2).sum(-1)) # (100,200)
```

## Memory Layout: Row-Major vs Column-Major

Multi-dimensional arrays are stored as a flat 1D sequence in RAM. The **memory layout** determines the ordering of elements:

- **Row-major (C order)**: Rightmost axis varies fastest. For `[[a,b,c],[d,e,f]]`, memory is `a,b,c,d,e,f`. Used by C, NumPy (default), PyTorch.
- **Column-major (Fortran order)**: Leftmost axis varies fastest. Memory is `a,d,b,e,c,f`. Used by Fortran, MATLAB, R, Julia.

This matters enormously for performance: CPUs load data in cache lines (64 bytes = 16 floats). Accessing elements in storage order achieves near-peak throughput; accessing across the stride direction causes cache misses and can be 10–100× slower.

> **[WARNING] BLAS Libraries and Layout Assumptions**
>
> BLAS and LAPACK (the backends for numpy.dot and torch.mm) were written in Fortran and originally expected column-major arrays. NumPy handles this transparently by passing appropriate transpose flags to BLAS routines, so you normally don't need to worry. However, if you're writing custom C extensions or calling BLAS directly, always check which layout is expected to avoid subtle correctness and performance bugs.

## Strides: The Mechanism Behind Zero-Copy Operations

A **stride** is the number of elements to advance in memory when moving one step along a given axis. For a float32 matrix of shape `(3,4)` in row-major order:

- Stride along axis 0 (next row): 4 elements
- Stride along axis 1 (next column): 1 element

Transposing a matrix just **swaps the strides** — no data movement occurs. `A.T` has strides `(1,4)` instead of `(4,1)`. This makes transpose O(1) in time and memory, but the result is *non-contiguous*: successive elements of any row are 4 elements apart in memory, which hurts cache performance for subsequent row-oriented operations.

```python
import torch

A = torch.randn(3, 4)              # contiguous row-major
print('shape:', A.shape)           # (3, 4)
print('strides:', A.stride())      # (4, 1) -- in elements
print('contiguous?', A.is_contiguous())  # True

AT = A.T                           # NO copy -- just swapped strides
print('AT strides:', AT.stride())         # (1, 4)
print('AT contiguous?', AT.is_contiguous()) # False!

# .contiguous() allocates new memory and copies elements in C order
AT_c = AT.contiguous()
print('AT_c strides:', AT_c.stride())      # (3, 1) -- back to C order

# Verify: transposing twice costs one copy (not zero)
import time
big = torch.randn(4096, 4096)
_ = big.T.contiguous()  # one allocation + memcopy
```

## Reshape vs View in PyTorch

Both operations change an array's shape, but their memory semantics differ:

- **`view(new_shape)`**: Returns a tensor sharing the *same storage*. Zero-copy. Requires the tensor to be contiguous in memory. Raises `RuntimeError` if called on a non-contiguous tensor. The shape must be compatible (same number of elements).
- **`reshape(new_shape)`**: Returns a view if the tensor is contiguous, otherwise silently allocates and copies. Always succeeds for compatible shapes. Hides memory allocations from the caller.

A guiding principle: use `view` in performance-critical paths when you have verified contiguity, so that unexpected copies surface as errors. Use `reshape` for correctness when contiguity is uncertain.

```python
import torch

x = torch.randn(2, 3, 4)           # 24 elements, contiguous

# view: zero-copy, same storage
y = x.view(6, 4)
print(y.data_ptr() == x.data_ptr())  # True

# permute -> non-contiguous
xp = x.permute(2, 0, 1)            # (4, 2, 3), non-contiguous
try:
    xp.view(8, 3)                   # RuntimeError!
except RuntimeError as e:
    print('view failed:', e)

yr = xp.reshape(8, 3)              # silent copy -- data_ptr differs
print(yr.data_ptr() == xp.data_ptr())  # False

# Transformer pattern: split heads after projection
B, T, C = 8, 128, 512
H, D = 8, 64                       # 8 heads, 64 dims each
q = torch.randn(B, T, C)
q_heads = q.view(B, T, H, D)       # zero-copy head split
q_heads = q_heads.transpose(1, 2)  # (B, H, T, D) for attention
```

## GPU Memory Coalescing and Layout Performance

NVIDIA GPU threads execute in groups of 32 called **warps**. Peak memory bandwidth is achieved only when all 32 threads in a warp access a contiguous 128-byte region — called **coalesced access**. Non-coalesced (strided) access can reduce effective bandwidth from 900 GB/s (A100) to under 30 GB/s.

For CNN feature maps, **NCHW** layout (PyTorch default) means channel data for one pixel is spread across memory, while **NHWC** keeps all channels of one pixel together. cuDNN selects the fastest algorithm per operation; `torch.channels_last` enables NHWC storage. For transformer models with large matrix multiplies, ensuring both operands are contiguous and row-major before `torch.matmul` is critical.

> **[TIP] Channels Last for CNN Acceleration**
>
> Convert CNN models to channels-last memory format for 20–50% speedups on Ampere+ GPUs:

  model = model.to(memory_format=torch.channels_last)
  x = x.to(memory_format=torch.channels_last)

This aligns feature map layout with Tensor Core input requirements. PyTorch propagates the format through most Conv/BN/ReLU operations automatically.

| Operation | Copies Data? | Requires Contiguous? | Use Case |
| --- | --- | --- | --- |
| tensor.view() | Never | Yes (error if not) | Performance-critical reshape |
| tensor.reshape() | Only if needed | No (copies silently) | General-purpose reshape |
| tensor.T / .transpose() | Never | No (changes strides) | Logical transpose |
| tensor.permute() | Never | No (reorders strides) | Arbitrary axis reorder |
| tensor.contiguous() | If non-contiguous | N/A | Prepare for view or CUDA kernel |
| tensor.expand() | Never (virtual) | No | Broadcast without copy |

> **[INFO] Tensors in JAX and NumPy**
>
> JAX arrays are always immutable and represent values, not views. JAX's jit-compilation traces through shape/dtype statically, so dynamic reshapes must use shapes known at trace time. NumPy follows the same contiguity rules as PyTorch but uses .flags['C_CONTIGUOUS'] to check layout. The stride-based mental model applies equally to all frameworks.
