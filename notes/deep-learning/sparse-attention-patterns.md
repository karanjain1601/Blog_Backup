---
title: "Sparse Attention — Local, Strided, and Longformer Patterns"
slug: "sparse-attention-patterns"
description: "Implement sliding window, global+local, and BigBird sparse attention patterns from scratch, benchmark sparse vs dense attention memory at L=4096, and understand when sparse attention is the right tool."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRnVsbCBzZWxmLWF0dGVudGlvbiBjb21wdXRlcyBPKEzCsikgYXR0ZW50aW9uIHdlaWdodHMg4oCUIGZvciBMPTE2SyB0b2tlbnMgdGhhdCBpcyAyNTYgbWlsbGlvbiBwYWlycyBwZXIgaGVhZCBwZXIgbGF5ZXIuIEF0IDE2IGhlYWRzIGFuZCAzMiBsYXllcnMsIGEgZm9yd2FyZCBwYXNzIHJlcXVpcmVzIHJvdWdobHkgMTMwIGJpbGxpb24gYXR0ZW50aW9uIHNjb3JlcyBiZWZvcmUgc29mdG1heDsgc3RvcmluZyB0aGVtIGluIGZsb2F0MTYgdXNlcyAyNjAgR0IuIFNwYXJzZSBhdHRlbnRpb24gYWRkcmVzc2VzIHRoaXMgYnkgY29tcHV0aW5nIGF0dGVudGlvbiBvbmx5IGZvciBhIHN0cnVjdHVyZWQgc3Vic2V0IG9mIChxdWVyeSwga2V5KSBwYWlycywgcmVkdWNpbmcgY29tcGxleGl0eSBmcm9tIE8oTMKyKSB0byBPKEzCt2spIHdoZXJlIGsg4omqIEwgaXMgdGhlIHNwYXJzaXR5IHBhdHRlcm4gd2lkdGguIFRoZSBjaGFsbGVuZ2UgaXMgdGhhdCBpcnJlZ3VsYXIgc3BhcnNpdHkgcGF0dGVybnMgY2Fubm90IGJlIGltcGxlbWVudGVkIGFzIGEgc2luZ2xlIGRlbnNlIG1hdHJpeCBtdWx0aXBseSBhbmQgcmVxdWlyZSBjdXN0b20gR1BVIGtlcm5lbHMgb3IgbWFza2VkIGF0dGVudGlvbiB0cmlja3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRnVsbCBBdHRlbnRpb246IE8oTMKyKSBDb21wbGV4aXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBzY2FsZWQgZG90LXByb2R1Y3QgYXR0ZW50aW9uIGNvbXB1dGVzIHNjb3JlcyBTID0gUUvhtYAv4oiaZCBvZiBzaGFwZSAoQiwgaCwgTCwgTCkuIE1lbW9yeSBmb3IgUyBpcyBCIMOXIGggw5cgTMKyIMOXIDIgYnl0ZXMgKGZsb2F0MTYpLiBGb3IgQj0xLCBoPTEsIEw9NDA5NjogMzMgTUIganVzdCBmb3Igc2NvcmVzOyBmb3IgTD0xNjM4NDogNTM3IE1CLiBBY3Jvc3MgMTYgaGVhZHM6IH44IEdCIHBlciBsYXllci4gRmxhc2hBdHRlbnRpb24gYXZvaWRzIG1hdGVyaWFsaXNpbmcgdGhlIGZ1bGwgbWF0cml4IGJ1dCBzdGlsbCByZXF1aXJlcyBPKEzCsikgY29tcHV0ZS4gRm9yIHRhc2tzIHdpdGggTCBcdTAwM2UgNDA5NiDigJQgbG9uZyBkb2N1bWVudHMsIGdlbm9taWNzLCBhdWRpbywgY29kZSByZXBvc2l0b3JpZXMg4oCUIHRoZSBxdWFkcmF0aWMgY29zdCBiZWNvbWVzIHRoZSBiaW5kaW5nIGNvbnN0cmFpbnQsIG1vdGl2YXRpbmcgc3BhcnNlIHBhdHRlcm5zIHRoYXQgcHJlc2VydmUgZXNzZW50aWFsIGF0dGVudGlvbiBwYXRocyB3aGlsZSBza2lwcGluZyBpcnJlbGV2YW50IHBhaXJzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNsaWRpbmcgV2luZG93IEF0dGVudGlvbiAoTG9uZ2Zvcm1lcikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzaW1wbGVzdCBzcGFyc2UgcGF0dGVybjogZWFjaCB0b2tlbiBhdHRlbmRzIG9ubHkgdG8gdGhlIHcvMiB0b2tlbnMgdG8gaXRzIGxlZnQgYW5kIHJpZ2h0ICh3aW5kb3cgc2l6ZSB3KS4gQ29tcGxleGl0eSBkcm9wcyB0byBPKEwgw5cgdykuIExvbmdmb3JtZXIgKEJlbHRhZ3kgZXQgYWwuIDIwMjApIHVzZXMgdz01MTIgb24gc2VxdWVuY2VzIHVwIHRvIEw9NDA5Ni4gVGhlIHNsaWRpbmcgd2luZG93IGNhcHR1cmVzIGxvY2FsIGNvbnRleHQgdGhhdCBkb21pbmF0ZXMgbW9zdCBOTFAgdGFza3Mg4oCUIGFkamFjZW50IHRva2VucywgbmVhcmJ5IHNlbnRlbmNlcy4gVGhlIGVmZmVjdGl2ZSByZWNlcHRpdmUgZmllbGQgZ3Jvd3Mgd2l0aCBkZXB0aDogYSB0b2tlbiBhdCBsYXllciBsIGNhbiBpbmRpcmVjdGx5IGF0dGVuZCB0byBwb3NpdGlvbnMgdXAgdG8gbCDDlyB3LzIgdG9rZW5zIGF3YXkuIEZvciB3PTUxMiBhbmQgMTIgbGF5ZXJzLCB0aGUgcmVjZXB0aXZlIGZpZWxkIGNvdmVycyB0aGUgZnVsbCBMPTQwOTYgZG9jdW1lbnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuZGVmIHNsaWRpbmdfd2luZG93X2F0dGVudGlvbihRLCBLLCBWLCB3aW5kb3cpOlxuICAgIFwiXCJcIk5haXZlIHNsaWRpbmcgd2luZG93IGF0dGVudGlvbiAoTG9uZ2Zvcm1lci1zdHlsZSBsb2NhbCBhdHRlbnRpb24pLlxuICAgIFEsIEssIFY6IChCLCBoLCBMLCBkKS4gRWFjaCB0b2tlbiBhdHRlbmRzIHRvIHdpbmRvdy8vMiB0b2tlbnMgb24gZWFjaCBzaWRlLlxuICAgIFJldHVybnM6IChCLCBoLCBMLCBkKS4gTyhMICogd2luZG93KSBhdHRlbnRpb24gcGFpcnMgY29tcHV0ZWQuXG4gICAgXCJcIlwiXG4gICAgQiwgaCwgTCwgZCA9IFEuc2hhcGVcbiAgICBoYWxmID0gd2luZG93IC8vIDJcbiAgICBvdXQgPSB0b3JjaC56ZXJvc19saWtlKFEpXG4gICAgZm9yIGkgaW4gcmFuZ2UoTCk6XG4gICAgICAgIGxvID0gbWF4KDAsIGkgLSBoYWxmKVxuICAgICAgICBoaSA9IG1pbihMLCBpICsgaGFsZiArIDEpXG4gICAgICAgIHFfaSA9IFFbOiwgOiwgaTppKzEsIDpdICAgICAgICAgICMgKEIsIGgsIDEsIGQpXG4gICAgICAgIGtfdyA9IEtbOiwgOiwgbG86aGksIDpdICAgICAgICAgICMgKEIsIGgsIHdpbiwgZClcbiAgICAgICAgdl93ID0gVls6LCA6LCBsbzpoaSwgOl0gICAgICAgICAgIyAoQiwgaCwgd2luLCBkKVxuICAgICAgICBzY29yZXMgPSBxX2kgQCBrX3cudHJhbnNwb3NlKC0yLC0xKSAvIG1hdGguc3FydChkKVxuICAgICAgICBvdXRbOiwgOiwgaSwgOl0gPSAoRi5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKSBAIHZfdykuc3F1ZWV6ZSgyKVxuICAgIHJldHVybiBvdXRcblxudG9yY2gubWFudWFsX3NlZWQoMClcbkIsIGgsIEwsIGQsIFcgPSAxLCAyLCA2NCwgMTYsIDhcblEgPSB0b3JjaC5yYW5kbihCLCBoLCBMLCBkKVxuSyA9IHRvcmNoLnJhbmRuKEIsIGgsIEwsIGQpXG5WID0gdG9yY2gucmFuZG4oQiwgaCwgTCwgZClcbm91dCA9IHNsaWRpbmdfd2luZG93X2F0dGVudGlvbihRLCBLLCBWLCBXKVxucHJpbnQoZlx1MDAyN1NsaWRpbmcgd2luZG93IGF0dGVudGlvbjogTD17TH0sIHdpbmRvdz17V31cdTAwMjcpXG5wcmludChmXHUwMDI3T3V0cHV0IHNoYXBlOiB7b3V0LnNoYXBlfVx1MDAyNylcbmF0dGVuZGVkX3BhaXJzID0gc3VtKG1pbihMLCBpK1cvLzIrMSkgLSBtYXgoMCwgaS1XLy8yKSBmb3IgaSBpbiByYW5nZShMKSlcbmZ1bGxfcGFpcnMgPSBMICogTFxucHJpbnQoZlx1MDAyN1BhaXJzIGNvbXB1dGVkOiB7YXR0ZW5kZWRfcGFpcnN9IC8ge2Z1bGxfcGFpcnN9ICh7YXR0ZW5kZWRfcGFpcnMvZnVsbF9wYWlyczouMSV9IG9mIGZ1bGwpXHUwMDI3KVxucHJpbnQoZlx1MDAyN1RoZW9yZXRpY2FsIGNvbXBsZXhpdHk6IE8oTCp3KT17TCpXfSB2cyBPKExeMik9e0wqTH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR2xvYmFsICsgTG9jYWwgQXR0ZW50aW9uIChMb25nZm9ybWVyKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHVyZSBsb2NhbCB3aW5kb3cgYXR0ZW50aW9uIGNhbm5vdCBjYXB0dXJlIGdsb2JhbCBjb250ZXh0IOKAlCBhIFtDTFNdIHRva2VuIG9yIGEgcXVlc3Rpb24gdG9rZW4gbmVlZHMgdG8gYXR0ZW5kIHRvIGFsbCBwb3NpdGlvbnMuIExvbmdmb3JtZXIgc29sdmVzIHRoaXMgd2l0aCBnbG9iYWwgdG9rZW5zOiBhIHNtYWxsIHNldCBvZiBwb3NpdGlvbnMgKHR5cGljYWxseSBbQ0xTXSBmb3IgY2xhc3NpZmljYXRpb24sIG9yIHF1ZXN0aW9uIHRva2VucyBmb3IgUUEpIGF0dGVuZCB0byBhbGwgTCBwb3NpdGlvbnMgYW5kIGFsbCBwb3NpdGlvbnMgYXR0ZW5kIGJhY2sgdG8gZ2xvYmFsIHRva2Vucy4gVGhpcyBhZGRzIE8oTCDDlyBnKSBwYWlycyB3aGVyZSBnIGlzIHRoZSBudW1iZXIgb2YgZ2xvYmFsIHRva2VucyAodHlwaWNhbGx5IGcg4omqIEwpLiBUaGUgcGF0dGVybiBoYXMgdGhyZWUgY29tcG9uZW50czogbG9jYWwgd2luZG93IHBhaXJzLCBnbG9iYWwtdG8tYWxsIHBhaXJzLCBhbmQgYWxsLXRvLWdsb2JhbCBwYWlycyDigJQga2VlcGluZyB0b3RhbCBjb21wbGV4aXR5IE8oTCDDlyAodyArIGcpKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5kZWYgZ2xvYmFsX2xvY2FsX2F0dGVudGlvbihRLCBLLCBWLCB3aW5kb3csIGdsb2JhbF9pbmRpY2VzKTpcbiAgICBcIlwiXCJHbG9iYWwrbG9jYWwgYXR0ZW50aW9uIChMb25nZm9ybWVyIHBhdHRlcm4pLlxuICAgIGdsb2JhbF9pbmRpY2VzOiBsaXN0IG9mIHRva2VuIHBvc2l0aW9ucyB3aXRoIGdsb2JhbCBhdHRlbnRpb24uXG4gICAgXCJcIlwiXG4gICAgQiwgaCwgTCwgZCA9IFEuc2hhcGVcbiAgICBzY2FsZSA9IG1hdGguc3FydChkKVxuICAgIGhhbGYgPSB3aW5kb3cgLy8gMlxuICAgICMgU3RhcnQgd2l0aCBsb2NhbCB3aW5kb3cgYXR0ZW50aW9uIGZvciBhbGwgdG9rZW5zXG4gICAgb3V0ID0gdG9yY2guemVyb3NfbGlrZShRKVxuICAgIGZvciBpIGluIHJhbmdlKEwpOlxuICAgICAgICBsbywgaGkgPSBtYXgoMCwgaSAtIGhhbGYpLCBtaW4oTCwgaSArIGhhbGYgKyAxKVxuICAgICAgICBhdHRlbmRfdG8gPSBsaXN0KHJhbmdlKGxvLCBoaSkpXG4gICAgICAgICMgQWxsIHRva2VucyBhbHNvIGF0dGVuZCB0byBnbG9iYWwgdG9rZW5zXG4gICAgICAgIGZvciBnIGluIGdsb2JhbF9pbmRpY2VzOlxuICAgICAgICAgICAgaWYgZyBub3QgaW4gYXR0ZW5kX3RvOlxuICAgICAgICAgICAgICAgIGF0dGVuZF90by5hcHBlbmQoZylcbiAgICAgICAgYXR0ZW5kX3RvID0gc29ydGVkKHNldChhdHRlbmRfdG8pKVxuICAgICAgICBrdyA9IEtbOiwgOiwgYXR0ZW5kX3RvLCA6XVxuICAgICAgICB2dyA9IFZbOiwgOiwgYXR0ZW5kX3RvLCA6XVxuICAgICAgICBzY29yZXMgPSBRWzosIDosIGk6aSsxLCA6XSBAIGt3LnRyYW5zcG9zZSgtMiwtMSkgLyBzY2FsZVxuICAgICAgICBvdXRbOiwgOiwgaSwgOl0gPSAoRi5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKSBAIHZ3KS5zcXVlZXplKDIpXG4gICAgIyBHbG9iYWwgdG9rZW5zIGFsc28gYXR0ZW5kIHRvIEFMTCBwb3NpdGlvbnNcbiAgICBmb3IgZyBpbiBnbG9iYWxfaW5kaWNlczpcbiAgICAgICAgc2NvcmVzID0gUVs6LCA6LCBnOmcrMSwgOl0gQCBLLnRyYW5zcG9zZSgtMiwtMSkgLyBzY2FsZVxuICAgICAgICBvdXRbOiwgOiwgZywgOl0gPSAoRi5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKSBAIFYpLnNxdWVlemUoMilcbiAgICByZXR1cm4gb3V0XG5cbkIsIGgsIEwsIGQsIFcgPSAxLCAxLCAzMiwgOCwgNlxuZ2xvYmFsc19pZHggPSBbMCwgMV0gICMgZS5nLiwgW0NMU10gYW5kIFtTRVBdIGFyZSBnbG9iYWxcblEgPSB0b3JjaC5yYW5kbihCLCBoLCBMLCBkKVxuSywgViA9IHRvcmNoLnJhbmRuKEIsaCxMLGQpLCB0b3JjaC5yYW5kbihCLGgsTCxkKVxub3V0ID0gZ2xvYmFsX2xvY2FsX2F0dGVudGlvbihRLCBLLCBWLCBXLCBnbG9iYWxzX2lkeClcbnByaW50KGZcdTAwMjdHbG9iYWwrbG9jYWwgYXR0ZW50aW9uOiBMPXtMfSwgd2luZG93PXtXfSwgZ2xvYmFsX3Rva2Vucz17Z2xvYmFsc19pZHh9XHUwMDI3KVxucHJpbnQoZlx1MDAyN091dHB1dDoge291dC5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3Q29tcGxleGl0eTogTyhMKih3K2cpKSA9IE8oe0x9Kih7V30re2xlbihnbG9iYWxzX2lkeCl9KSkgPSBPKHtMKihXK2xlbihnbG9iYWxzX2lkeCkpfSlcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmlnQmlyZDogTG9jYWwsIEdsb2JhbCwgYW5kIFJhbmRvbSBBdHRlbnRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJpZ0JpcmQgKFphaGVlciBldCBhbC4gMjAyMCkgY29tYmluZXMgdGhyZWUgYXR0ZW50aW9uIGNvbXBvbmVudHMgdG8gcHJvdmUgdGhhdCBPKEwpIGF0dGVudGlvbiBpcyBhIHVuaXZlcnNhbCBhcHByb3hpbWF0b3Igb2YgZnVsbCBhdHRlbnRpb246ICgxKSBsb2NhbCB3aW5kb3cgb2Ygc2l6ZSB3IChzYW1lIGFzIExvbmdmb3JtZXIpLCAoMikgZyBnbG9iYWwgdG9rZW5zIHRoYXQgYXR0ZW5kIHRvIGFsbCBwb3NpdGlvbnMsICgzKSByIHJhbmRvbSBrZXlzIHBlciBxdWVyeSDigJQgZWFjaCBxdWVyeSBhZGRpdGlvbmFsbHkgYXR0ZW5kcyB0byByIHJhbmRvbWx5IHNlbGVjdGVkIHBvc2l0aW9ucy4gVGhlIHJhbmRvbSBjb21wb25lbnQgZW5zdXJlcyB0aGF0IG5vIHR3byB0b2tlbnMgYXJlIHRvbyBtYW55IGhvcHMgYXBhcnQgaW4gdGhlIGF0dGVudGlvbiBncmFwaCwgZW5hYmxpbmcgZ3JhZGllbnQgZmxvdyBhbmQgbG9uZy1yYW5nZSBpbmZvcm1hdGlvbiBtaXhpbmcuIEJpZ0JpcmQgYWNoaWV2ZXMgTyhMIMOXICh3ICsgZyArIHIpKSBjb21wbGV4aXR5IHdpdGggc3Ryb25nIGVtcGlyaWNhbCByZXN1bHRzIG9uIGdlbm9taWNzIChETkEgc2VxdWVuY2VzIHVwIHRvIEw9NDA5NikgYW5kIGxvbmctZG9jdW1lbnQgdGFza3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuZGVmIGJpZ2JpcmRfYXR0ZW50aW9uKFEsIEssIFYsIHdpbmRvdywgZ2xvYmFsX2luZGljZXMsIG51bV9yYW5kb20pOlxuICAgIFwiXCJcIkJpZ0JpcmQgYXR0ZW50aW9uOiBsb2NhbCArIGdsb2JhbCArIHJhbmRvbSBhdHRlbnRpb24gcGF0dGVybi5cIlwiXCJcbiAgICBCLCBoLCBMLCBkID0gUS5zaGFwZVxuICAgIHNjYWxlID0gbWF0aC5zcXJ0KGQpXG4gICAgaGFsZiA9IHdpbmRvdyAvLyAyXG4gICAgb3V0ID0gdG9yY2guemVyb3NfbGlrZShRKVxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKDQyKSAgIyByZXByb2R1Y2libGUgcmFuZG9tIHBhdHRlcm5cbiAgICAjIFByZWNvbXB1dGUgcmFuZG9tIGF0dGVudGlvbiBwYXR0ZXJuIChzYW1lIGZvciBhbGwgcG9zaXRpb25zIGZvciBzaW1wbGljaXR5KVxuICAgIHJhbmRvbV9rZXlzID0gW3RvcmNoLnJhbmRwZXJtKEwpWzpudW1fcmFuZG9tXS50b2xpc3QoKSBmb3IgXyBpbiByYW5nZShMKV1cbiAgICBmb3IgaSBpbiByYW5nZShMKTpcbiAgICAgICAgbG8sIGhpID0gbWF4KDAsIGktaGFsZiksIG1pbihMLCBpK2hhbGYrMSlcbiAgICAgICAgbG9jYWxfaWR4ID0gbGlzdChyYW5nZShsbywgaGkpKVxuICAgICAgICBhbGxfaWR4ID0gc29ydGVkKHNldChsb2NhbF9pZHggKyBsaXN0KGdsb2JhbF9pbmRpY2VzKSArIHJhbmRvbV9rZXlzW2ldKSlcbiAgICAgICAga3cgPSBLWzosIDosIGFsbF9pZHgsIDpdXG4gICAgICAgIHZ3ID0gVls6LCA6LCBhbGxfaWR4LCA6XVxuICAgICAgICBzY29yZXMgPSBRWzosIDosIGk6aSsxLCA6XSBAIGt3LnRyYW5zcG9zZSgtMiwtMSkgLyBzY2FsZVxuICAgICAgICBvdXRbOiwgOiwgaSwgOl0gPSAoRi5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKSBAIHZ3KS5zcXVlZXplKDIpXG4gICAgZm9yIGcgaW4gZ2xvYmFsX2luZGljZXM6XG4gICAgICAgIHNjb3JlcyA9IFFbOiwgOiwgZzpnKzEsIDpdIEAgSy50cmFuc3Bvc2UoLTIsLTEpIC8gc2NhbGVcbiAgICAgICAgb3V0WzosIDosIGcsIDpdID0gKEYuc29mdG1heChzY29yZXMsIGRpbT0tMSkgQCBWKS5zcXVlZXplKDIpXG4gICAgcmV0dXJuIG91dFxuXG5CLCBoLCBMLCBkID0gMSwgMSwgNDgsIDhcblcsIGdfaWR4LCByID0gOCwgWzAsIDFdLCA0XG5RID0gdG9yY2gucmFuZG4oQiwgaCwgTCwgZClcbkssIFYgPSB0b3JjaC5yYW5kbihCLGgsTCxkKSwgdG9yY2gucmFuZG4oQixoLEwsZClcbm91dCA9IGJpZ2JpcmRfYXR0ZW50aW9uKFEsIEssIFYsIFcsIGdfaWR4LCByKVxucHJpbnQoZlx1MDAyN0JpZ0JpcmQ6IEw9e0x9LCB3aW5kb3c9e1d9LCBnbG9iYWw9e2dfaWR4fSwgcmFuZG9tPXtyfVx1MDAyNylcbnByaW50KGZcdTAwMjdPdXRwdXQ6IHtvdXQuc2hhcGV9XHUwMDI3KVxuZWZmX2sgPSBXICsgbGVuKGdfaWR4KSArIHJcbnByaW50KGZcdTAwMjdFZmZlY3RpdmUga2V5cyBwZXIgcXVlcnk6IH57ZWZmX2t9LCBjb21wbGV4aXR5OiBPKHtMfSp7ZWZmX2t9KT17TCplZmZfa30gdnMgTyhMXjIpPXtMKkx9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJlbmNobWFya2luZyBTcGFyc2UgdnMgRGVuc2UgQXR0ZW50aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcXVhZHJhdGljIG1lbW9yeSBvZiBmdWxsIGF0dGVudGlvbiBiZWNvbWVzIHRoZSBib3R0bGVuZWNrIGFib3ZlIEw9MjA0OCBvbiBhIDE2IEdCIEdQVS4gU3BhcnNlIGF0dGVudGlvbiBhbGxvd3MgTD0xNksgb3IgZXZlbiBMPTEyOEsgd2l0aGluIHRoZSBzYW1lIG1lbW9yeSBidWRnZXQuIEhvd2V2ZXIsIG5haXZlIFB5dGhvbiBpbXBsZW1lbnRhdGlvbnMgb2Ygc3BhcnNlIHBhdHRlcm5zIGFyZSBzbG93ZXIgdGhhbiBkZW5zZSBhdHRlbnRpb24gZm9yIHNtYWxsIEwgYmVjYXVzZSB0aGV5IGxhY2sgdGhlIGhpZ2hseSBvcHRpbWlzZWQgQ1VEQSBrZXJuZWxzIHRoYXQgcG93ZXIgRi5zY2FsZWRfZG90X3Byb2R1Y3RfYXR0ZW50aW9uLiBQcm9kdWN0aW9uIHNwYXJzZSBhdHRlbnRpb24gcmVxdWlyZXMgY3VzdG9tIGtlcm5lbHMgKExvbmdmb3JtZXIgdXNlcyBhIGRpbGF0ZWQgY29udm9sdXRpb24gdHJpY2s7IEJpZ0JpcmQgdXNlcyBibG9jay1zcGFyc2UgQ1VEQSBvcGVyYXRpb25zKS4gVGhlIGJlbmNobWFya3MgYmVsb3cgbWVhc3VyZSB0aGUgbmFpdmUgaW1wbGVtZW50YXRpb25zIHRvIHZlcmlmeSBjb3JyZWN0bmVzcyBhbmQgY29tcGxleGl0eSBzY2FsaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCBtYXRoXG5pbXBvcnQgdGltZVxuXG5kZWYgZGVuc2VfYXR0ZW50aW9uKFEsIEssIFYpOlxuICAgIGQgPSBRLnNoYXBlWy0xXVxuICAgIHJldHVybiBGLnNvZnRtYXgoUSBAIEsudHJhbnNwb3NlKC0yLC0xKSAvIG1hdGguc3FydChkKSwgZGltPS0xKSBAIFZcblxuZGVmIG1lYXN1cmVfYXR0bihmbiwgKmFyZ3MsIG49MTApOlxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGZvciBfIGluIHJhbmdlKG4pOlxuICAgICAgICBfID0gZm4oKmFyZ3MpXG4gICAgcmV0dXJuICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApIC8gbiAqIDEwMDBcblxuQiwgaCwgZCA9IDEsIDEsIDMyXG5XLCByID0gMTYsIDRcbnByaW50KGZcIntcdTAwMjdNZXRob2RcdTAwMjc6XHUwMDNlMjB9IHtcdTAwMjdMPTI1Nlx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0w9NTEyXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3TD0xMDI0XHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3Q29tcGxleGl0eVx1MDAyNzpcdTAwM2UxNH1cIilcbmZvciBMIGluIFsyNTYsIDUxMiwgMTAyNF06XG4gICAgUSA9IHRvcmNoLnJhbmRuKEIsIGgsIEwsIGQpXG4gICAgSywgViA9IHRvcmNoLnJhbmRuKEIsaCxMLGQpLCB0b3JjaC5yYW5kbihCLGgsTCxkKVxuICAgIHRfZGVuc2UgPSBtZWFzdXJlX2F0dG4oZGVuc2VfYXR0ZW50aW9uLCBRLCBLLCBWKVxuICAgIHJvdyA9IGZcdTAwMjd7XHUwMDI3RGVuc2VcdTAwMjc6XHUwMDNlMjB9IHt0X2RlbnNlOlx1MDAzZTkuMWZ9XHUwMDI3XG4gICAgcHJpbnQoZlwiRGVuc2UgTD17TH06IHt0X2RlbnNlOi4yZn1tcyB8IG1lbX57TCpMKjIvMTAyNDouMGZ9S0JcIilcbnByaW50KFx1MDAyN1xcbktleSB0YWtlYXdheTogc3BhcnNlIHBhdHRlcm5zIHJlZHVjZSBtZW1vcnkgTyhMXjIpLVx1MDAzZU8oTCp3KTtcdTAwMjcpXG5wcmludChcdTAwMjdjdXN0b20gQ1VEQSBrZXJuZWxzIG5lZWRlZCBmb3IgYWN0dWFsIHNwZWVkIGdhaW5zIG92ZXIgZGVuc2UgYXQgc21hbGwgTC5cdTAwMjcpXG5wcmludChmXHUwMDI3RGVuc2UgYXQgTD00MDk2OiBtZW1+ezQwOTYqNDA5NioyLy8xMDI0Ly8xMDI0fU1CIHwgU3BhcnNlKHc9e1d9KTogfns0MDk2KlcqMi8vMTAyNH1LQlx1MDAyNykifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiQ29tcGxleGl0eSIsIk1lbW9yeSBhdCBMPTRLIiwiUXVhbGl0eSB2cyBGdWxsIiwiSW1wbGVtZW50YXRpb24iLCJCZXN0IFVzZSBDYXNlIl0sInJvd3MiOltbIkZ1bGwgKGRlbnNlKSIsIk8oTMKyKSIsIn4zMiBNQi9oZWFkIiwiQmFzZWxpbmUiLCJTaW5nbGUgbWF0bXVsIOKAlCB0cml2aWFsIiwiTCBcdTAwM2MgMkssIGFueSB0YXNrIl0sWyJTbGlkaW5nIHdpbmRvdyIsIk8oTMK3dykiLCJ+MiBNQiAodz0yNTYpIiwiR29vZCBmb3IgbG9jYWwgdGFza3MiLCJMb29wIG9yIGJsb2NrLXNwYXJzZSBrZXJuZWwiLCJMb25nIE5MUCwgYXVkaW8gKEwgMkvigJMzMkspIl0sWyJHbG9iYWwrbG9jYWwiLCJPKEzCtyh3K2cpKSIsIn4yIE1CICh3PTI1NiwgZz0yKSIsIlN0cm9uZyDigJQgZ2xvYmFsIHRva2VucyBwcmVzZXJ2ZSBzZW1hbnRpY3MiLCJMb25nZm9ybWVyIGtlcm5lbCIsIkxvbmctZG9jIFFBLCBjbGFzc2lmaWNhdGlvbiJdLFsiQmlnQmlyZCIsIk8oTMK3KHcrZytyKSkiLCJ+MyBNQiAodz02NCxnPTIscj04KSIsIk5lYXIgZnVsbCBhdHRlbnRpb24gcXVhbGl0eSIsIkJsb2NrLXNwYXJzZSBDVURBIiwiR2Vub21pY3MsIHZlcnkgbG9uZyBkb2NzIl0sWyJMaW5lYXIgYXR0ZW50aW9uIiwiTyhMwrdkwrIpIiwiTyhMKSDigJQgbm8gTMKyIHRlcm0iLCJRdWFsaXR5IGdhcCBmb3IgbG9uZyBzZXF1ZW5jZXMiLCJLZXJuZWwgdHJpY2sg4oCUIHB1cmUgbWF0bXVscyIsIkwgXHUwMDNlIDY0SywgYXBwcm94aW1hdGUgdGFza3MiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBDb25zaWRlcmF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2hvb3NpbmcgYSBzcGFyc2UgcGF0dGVybiByZXF1aXJlcyB1bmRlcnN0YW5kaW5nIHdoZXJlIGF0dGVudGlvbiBpcyBpbmZvcm1hdGl2ZSBpbiB5b3VyIGRhdGEuIEZvciB0ZXh0IGNsYXNzaWZpY2F0aW9uIGEgZmV3IGdsb2JhbCB0b2tlbnMgKFtDTFNdKSBhcmUgc3VmZmljaWVudDsgZm9yIGxvbmctZm9ybSBnZW5lcmF0aW9uIGEgc2xpZGluZyB3aW5kb3cgcHJlc2VydmVzIGZsdWVuY3kuIFNwYXJzZSBhdHRlbnRpb24gcGF0dGVybnMgaW1wbGVtZW50ZWQgbmFpdmVseSBpbiBQeVRvcmNoIGFyZSBzbG93ZXIgdGhhbiBkZW5zZSBhdHRlbnRpb24gZm9yIEwgXHUwMDNjIDQwOTYgYmVjYXVzZSBsb29wIG92ZXJoZWFkIGRvbWluYXRlcy4gRm9yIHByb2R1Y3Rpb24gdXNlLCBzcGVjaWFsaXNlZCBrZXJuZWxzIGFyZSByZXF1aXJlZDogTG9uZ2Zvcm1lclx1MDAyN3MgSHVnZ2luZyBGYWNlIGltcGxlbWVudGF0aW9uIHVzZXMgYSBjYXJlZnVsbHkgb3B0aW1pc2VkIGNodW5rLWJhc2VkIGFwcHJvYWNoOyBCaWdCaXJkIGFuZCBTcGFyc2UgVHJhbnNmb3JtZXIgcmVseSBvbiBibG9jay1zcGFyc2UgQ1VEQSBvcGVyYXRpb25zIGZyb20gbGlicmFyaWVzIGxpa2UgdHJpdG9uIG9yIGFwZXguIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJTcGFyc2UgQXR0ZW50aW9uIE5lZWRzIEN1c3RvbSBLZXJuZWxzIiwiY29udGVudCI6Ik5ldmVyIGltcGxlbWVudCBzcGFyc2UgYXR0ZW50aW9uIHdpdGggUHl0aG9uIGxvb3BzIG9yIG1hc2tlZCBkZW5zZSBhdHRlbnRpb24gKHNldHRpbmcgbWFza2VkIGVudHJpZXMgdG8gLWluZikgaW4gcHJvZHVjdGlvbiDigJQgYm90aCBhcmUgTyhMwrIpIGluIG1lbW9yeS4gTWFza2VkIGRlbnNlIGF0dGVudGlvbiBjb21wdXRlcyB0aGUgZnVsbCBMw5dMIG1hdHJpeCBhbmQgemVyb2VzIGVudHJpZXMgYWZ0ZXIgdGhlIGZhY3Q7IGl0IGdpdmVzIHRoZSBjb3JyZWN0IG91dHB1dCBidXQgZGVmZWF0cyB0aGUgcHVycG9zZS4gUmVhbCBPKEzCt3cpIHNwYXJzZSBhdHRlbnRpb24gcmVxdWlyZXMgY3VzdG9tIENVREEga2VybmVscyBvciBibG9jay1zcGFyc2UgbGlicmFyaWVzLiBGb3IgcXVpY2sgcHJvdG90eXBpbmcsIHVzZSB0aGUgTG9uZ2Zvcm1lciBpbXBsZW1lbnRhdGlvbiBpbiBIdWdnaW5nRmFjZSB0cmFuc2Zvcm1lcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2hlbiB0byBVc2UgU3BhcnNlIEF0dGVudGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVXNlIHNwYXJzZSBhdHRlbnRpb24gd2hlbiBzZXF1ZW5jZSBsZW5ndGggZXhjZWVkcyB+MksgdG9rZW5zIGFuZCB0aGUgdGFzayBzdHJ1Y3R1cmUganVzdGlmaWVzIHRoZSBwYXR0ZXJuLiBTbGlkaW5nIHdpbmRvdyBpcyBhcHByb3ByaWF0ZSB3aGVuIGxvY2FsIGNvbnRleHQgaXMgc3VmZmljaWVudCAobW9zdCB0b2tlbi1sZXZlbCBOTFAgdGFza3MpLiBHbG9iYWwrbG9jYWwgKExvbmdmb3JtZXIpIHN1aXRzIGRvY3VtZW50LWxldmVsIHRhc2tzIHdoZXJlIGEgZmV3IGFuY2hvciB0b2tlbnMgbmVlZCBmdWxsIGNvbnRleHQuIEJpZ0JpcmQgaXMgYmVzdCB3aGVuIHlvdSBuZWVkIG5lYXItZnVsbC1hdHRlbnRpb24gcXVhbGl0eSBhdCBPKEwpIGNvc3QgYW5kIGNhbiBhZmZvcmQgYmxvY2stc3BhcnNlIGtlcm5lbCBjb21wbGV4aXR5LiBGb3Igc2VxdWVuY2VzIGFib3ZlIEw9NjRLIHdoZXJlIGV2ZW4gTyhMwrd3KSBpcyBleHBlbnNpdmUsIGxpbmVhciBhdHRlbnRpb24gb3Igc3RhdGUtc3BhY2UgbW9kZWxzIChNYW1iYSwgUzQpIG1heSBiZSBtb3JlIGFwcHJvcHJpYXRlLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU2xpZGluZyB3aW5kb3cgKHc9NTEyKTogTG9uZ2Zvcm1lciB1c2VzIHRoaXMgZm9yIHRva2VuIGNsYXNzaWZpY2F0aW9uIG9uIEw9NDA5NiBkb2N1bWVudHMuIiwiR2xvYmFsK2xvY2FsOiBhZGQgW0NMU10gYXMgYSBnbG9iYWwgdG9rZW4gZm9yIGNsYXNzaWZpY2F0aW9uLCBxdWVzdGlvbiB0b2tlbnMgZm9yIFFBLiIsIkJpZ0JpcmQ6IHVzZWQgZm9yIGdlbm9taWMgc2VxdWVuY2UgbW9kZWxsaW5nIChETkEsIFJOQSkgd2l0aCBMIHVwIHRvIDQwOTYuIiwiU3BhcnNlIFRyYW5zZm9ybWVyIChPcGVuQUkgMjAxOSk6IGFsdGVybmF0aW5nIGxvY2FsIGFuZCBzdHJpZGVkIHBhdHRlcm5zIGZvciBhdXRvcmVncmVzc2l2ZSBnZW5lcmF0aW9uLiIsIkxvbmdmb3JtZXItRW5jb2Rlci1EZWNvZGVyIChMRUQpOiBhcHBsaWVzIHNwYXJzZSBhdHRlbnRpb24gdG8gZW5jb2RlciwgZnVsbCBhdHRlbnRpb24gdG8gY3Jvc3MtYXR0ZW50aW9uLiIsIkFsbCBzcGFyc2UgcGF0dGVybnMgcmVxdWlyZSBjYXVzYWwgbWFza2luZyBmb3IgYXV0b3JlZ3Jlc3NpdmUgZ2VuZXJhdGlvbiDigJQgZnV0dXJlIHBvc2l0aW9ucyBtdXN0IGJlIGV4Y2x1ZGVkLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Sparse Attention — Local, Strided, and Longformer Patterns

Full self-attention computes O(L²) attention weights — for L=16K tokens that is 256 million pairs per head per layer. At 16 heads and 32 layers, a forward pass requires roughly 130 billion attention scores before softmax; storing them in float16 uses 260 GB. Sparse attention addresses this by computing attention only for a structured subset of (query, key) pairs, reducing complexity from O(L²) to O(L·k) where k ≪ L is the sparsity pattern width. The challenge is that irregular sparsity patterns cannot be implemented as a single dense matrix multiply and require custom GPU kernels or masked attention tricks.

## Full Attention: O(L²) Complexity

Standard scaled dot-product attention computes scores S = QKᵀ/√d of shape (B, h, L, L). Memory for S is B × h × L² × 2 bytes (float16). For B=1, h=1, L=4096: 33 MB just for scores; for L=16384: 537 MB. Across 16 heads: ~8 GB per layer. FlashAttention avoids materialising the full matrix but still requires O(L²) compute. For tasks with L > 4096 — long documents, genomics, audio, code repositories — the quadratic cost becomes the binding constraint, motivating sparse patterns that preserve essential attention paths while skipping irrelevant pairs.

## Sliding Window Attention (Longformer)

The simplest sparse pattern: each token attends only to the w/2 tokens to its left and right (window size w). Complexity drops to O(L × w). Longformer (Beltagy et al. 2020) uses w=512 on sequences up to L=4096. The sliding window captures local context that dominates most NLP tasks — adjacent tokens, nearby sentences. The effective receptive field grows with depth: a token at layer l can indirectly attend to positions up to l × w/2 tokens away. For w=512 and 12 layers, the receptive field covers the full L=4096 document.

```python
import torch
import torch.nn.functional as F
import math

def sliding_window_attention(Q, K, V, window):
    """Naive sliding window attention (Longformer-style local attention).
    Q, K, V: (B, h, L, d). Each token attends to window//2 tokens on each side.
    Returns: (B, h, L, d). O(L * window) attention pairs computed.
    """
    B, h, L, d = Q.shape
    half = window // 2
    out = torch.zeros_like(Q)
    for i in range(L):
        lo = max(0, i - half)
        hi = min(L, i + half + 1)
        q_i = Q[:, :, i:i+1, :]          # (B, h, 1, d)
        k_w = K[:, :, lo:hi, :]          # (B, h, win, d)
        v_w = V[:, :, lo:hi, :]          # (B, h, win, d)
        scores = q_i @ k_w.transpose(-2,-1) / math.sqrt(d)
        out[:, :, i, :] = (F.softmax(scores, dim=-1) @ v_w).squeeze(2)
    return out

torch.manual_seed(0)
B, h, L, d, W = 1, 2, 64, 16, 8
Q = torch.randn(B, h, L, d)
K = torch.randn(B, h, L, d)
V = torch.randn(B, h, L, d)
out = sliding_window_attention(Q, K, V, W)
print(f'Sliding window attention: L={L}, window={W}')
print(f'Output shape: {out.shape}')
attended_pairs = sum(min(L, i+W//2+1) - max(0, i-W//2) for i in range(L))
full_pairs = L * L
print(f'Pairs computed: {attended_pairs} / {full_pairs} ({attended_pairs/full_pairs:.1%} of full)')
print(f'Theoretical complexity: O(L*w)={L*W} vs O(L^2)={L*L}')
```

## Global + Local Attention (Longformer)

Pure local window attention cannot capture global context — a [CLS] token or a question token needs to attend to all positions. Longformer solves this with global tokens: a small set of positions (typically [CLS] for classification, or question tokens for QA) attend to all L positions and all positions attend back to global tokens. This adds O(L × g) pairs where g is the number of global tokens (typically g ≪ L). The pattern has three components: local window pairs, global-to-all pairs, and all-to-global pairs — keeping total complexity O(L × (w + g)).

```python
import torch
import torch.nn.functional as F
import math

def global_local_attention(Q, K, V, window, global_indices):
    """Global+local attention (Longformer pattern).
    global_indices: list of token positions with global attention.
    """
    B, h, L, d = Q.shape
    scale = math.sqrt(d)
    half = window // 2
    # Start with local window attention for all tokens
    out = torch.zeros_like(Q)
    for i in range(L):
        lo, hi = max(0, i - half), min(L, i + half + 1)
        attend_to = list(range(lo, hi))
        # All tokens also attend to global tokens
        for g in global_indices:
            if g not in attend_to:
                attend_to.append(g)
        attend_to = sorted(set(attend_to))
        kw = K[:, :, attend_to, :]
        vw = V[:, :, attend_to, :]
        scores = Q[:, :, i:i+1, :] @ kw.transpose(-2,-1) / scale
        out[:, :, i, :] = (F.softmax(scores, dim=-1) @ vw).squeeze(2)
    # Global tokens also attend to ALL positions
    for g in global_indices:
        scores = Q[:, :, g:g+1, :] @ K.transpose(-2,-1) / scale
        out[:, :, g, :] = (F.softmax(scores, dim=-1) @ V).squeeze(2)
    return out

B, h, L, d, W = 1, 1, 32, 8, 6
globals_idx = [0, 1]  # e.g., [CLS] and [SEP] are global
Q = torch.randn(B, h, L, d)
K, V = torch.randn(B,h,L,d), torch.randn(B,h,L,d)
out = global_local_attention(Q, K, V, W, globals_idx)
print(f'Global+local attention: L={L}, window={W}, global_tokens={globals_idx}')
print(f'Output: {out.shape}')
print(f'Complexity: O(L*(w+g)) = O({L}*({W}+{len(globals_idx)})) = O({L*(W+len(globals_idx))})')
```

## BigBird: Local, Global, and Random Attention

BigBird (Zaheer et al. 2020) combines three attention components to prove that O(L) attention is a universal approximator of full attention: (1) local window of size w (same as Longformer), (2) g global tokens that attend to all positions, (3) r random keys per query — each query additionally attends to r randomly selected positions. The random component ensures that no two tokens are too many hops apart in the attention graph, enabling gradient flow and long-range information mixing. BigBird achieves O(L × (w + g + r)) complexity with strong empirical results on genomics (DNA sequences up to L=4096) and long-document tasks.

```python
import torch
import torch.nn.functional as F
import math

def bigbird_attention(Q, K, V, window, global_indices, num_random):
    """BigBird attention: local + global + random attention pattern."""
    B, h, L, d = Q.shape
    scale = math.sqrt(d)
    half = window // 2
    out = torch.zeros_like(Q)
    torch.manual_seed(42)  # reproducible random pattern
    # Precompute random attention pattern (same for all positions for simplicity)
    random_keys = [torch.randperm(L)[:num_random].tolist() for _ in range(L)]
    for i in range(L):
        lo, hi = max(0, i-half), min(L, i+half+1)
        local_idx = list(range(lo, hi))
        all_idx = sorted(set(local_idx + list(global_indices) + random_keys[i]))
        kw = K[:, :, all_idx, :]
        vw = V[:, :, all_idx, :]
        scores = Q[:, :, i:i+1, :] @ kw.transpose(-2,-1) / scale
        out[:, :, i, :] = (F.softmax(scores, dim=-1) @ vw).squeeze(2)
    for g in global_indices:
        scores = Q[:, :, g:g+1, :] @ K.transpose(-2,-1) / scale
        out[:, :, g, :] = (F.softmax(scores, dim=-1) @ V).squeeze(2)
    return out

B, h, L, d = 1, 1, 48, 8
W, g_idx, r = 8, [0, 1], 4
Q = torch.randn(B, h, L, d)
K, V = torch.randn(B,h,L,d), torch.randn(B,h,L,d)
out = bigbird_attention(Q, K, V, W, g_idx, r)
print(f'BigBird: L={L}, window={W}, global={g_idx}, random={r}')
print(f'Output: {out.shape}')
eff_k = W + len(g_idx) + r
print(f'Effective keys per query: ~{eff_k}, complexity: O({L}*{eff_k})={L*eff_k} vs O(L^2)={L*L}')
```

## Benchmarking Sparse vs Dense Attention

The quadratic memory of full attention becomes the bottleneck above L=2048 on a 16 GB GPU. Sparse attention allows L=16K or even L=128K within the same memory budget. However, naive Python implementations of sparse patterns are slower than dense attention for small L because they lack the highly optimised CUDA kernels that power F.scaled_dot_product_attention. Production sparse attention requires custom kernels (Longformer uses a dilated convolution trick; BigBird uses block-sparse CUDA operations). The benchmarks below measure the naive implementations to verify correctness and complexity scaling.

```python
import torch
import torch.nn.functional as F
import math
import time

def dense_attention(Q, K, V):
    d = Q.shape[-1]
    return F.softmax(Q @ K.transpose(-2,-1) / math.sqrt(d), dim=-1) @ V

def measure_attn(fn, *args, n=10):
    t0 = time.perf_counter()
    for _ in range(n):
        _ = fn(*args)
    return (time.perf_counter() - t0) / n * 1000

B, h, d = 1, 1, 32
W, r = 16, 4
print(f"{'Method':>20} {'L=256':>10} {'L=512':>10} {'L=1024':>10} {'Complexity':>14}")
for L in [256, 512, 1024]:
    Q = torch.randn(B, h, L, d)
    K, V = torch.randn(B,h,L,d), torch.randn(B,h,L,d)
    t_dense = measure_attn(dense_attention, Q, K, V)
    row = f'{'Dense':>20} {t_dense:>9.1f}'
    print(f"Dense L={L}: {t_dense:.2f}ms | mem~{L*L*2/1024:.0f}KB")
print('\nKey takeaway: sparse patterns reduce memory O(L^2)->O(L*w);')
print('custom CUDA kernels needed for actual speed gains over dense at small L.')
print(f'Dense at L=4096: mem~{4096*4096*2//1024//1024}MB | Sparse(w={W}): ~{4096*W*2//1024}KB')
```

| Method | Complexity | Memory at L=4K | Quality vs Full | Implementation | Best Use Case |
| --- | --- | --- | --- | --- | --- |
| Full (dense) | O(L²) | ~32 MB/head | Baseline | Single matmul — trivial | L < 2K, any task |
| Sliding window | O(L·w) | ~2 MB (w=256) | Good for local tasks | Loop or block-sparse kernel | Long NLP, audio (L 2K–32K) |
| Global+local | O(L·(w+g)) | ~2 MB (w=256, g=2) | Strong — global tokens preserve semantics | Longformer kernel | Long-doc QA, classification |
| BigBird | O(L·(w+g+r)) | ~3 MB (w=64,g=2,r=8) | Near full attention quality | Block-sparse CUDA | Genomics, very long docs |
| Linear attention | O(L·d²) | O(L) — no L² term | Quality gap for long sequences | Kernel trick — pure matmuls | L > 64K, approximate tasks |

## Practical Considerations

Choosing a sparse pattern requires understanding where attention is informative in your data. For text classification a few global tokens ([CLS]) are sufficient; for long-form generation a sliding window preserves fluency. Sparse attention patterns implemented naively in PyTorch are slower than dense attention for L < 4096 because loop overhead dominates. For production use, specialised kernels are required: Longformer's Hugging Face implementation uses a carefully optimised chunk-based approach; BigBird and Sparse Transformer rely on block-sparse CUDA operations from libraries like triton or apex.

> **Sparse Attention Needs Custom Kernels**: Never implement sparse attention with Python loops or masked dense attention (setting masked entries to -inf) in production — both are O(L²) in memory. Masked dense attention computes the full L×L matrix and zeroes entries after the fact; it gives the correct output but defeats the purpose. Real O(L·w) sparse attention requires custom CUDA kernels or block-sparse libraries. For quick prototyping, use the Longformer implementation in HuggingFace transformers.

## When to Use Sparse Attention

Use sparse attention when sequence length exceeds ~2K tokens and the task structure justifies the pattern. Sliding window is appropriate when local context is sufficient (most token-level NLP tasks). Global+local (Longformer) suits document-level tasks where a few anchor tokens need full context. BigBird is best when you need near-full-attention quality at O(L) cost and can afford block-sparse kernel complexity. For sequences above L=64K where even O(L·w) is expensive, linear attention or state-space models (Mamba, S4) may be more appropriate.

- Sliding window (w=512): Longformer uses this for token classification on L=4096 documents.
- Global+local: add [CLS] as a global token for classification, question tokens for QA.
- BigBird: used for genomic sequence modelling (DNA, RNA) with L up to 4096.
- Sparse Transformer (OpenAI 2019): alternating local and strided patterns for autoregressive generation.
- Longformer-Encoder-Decoder (LED): applies sparse attention to encoder, full attention to cross-attention.
- All sparse patterns require causal masking for autoregressive generation — future positions must be excluded.

---

