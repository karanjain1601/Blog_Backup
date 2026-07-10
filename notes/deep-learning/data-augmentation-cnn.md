---
title: "Data Augmentation — CutMix, MixUp, and RandAugment"
slug: "data-augmentation-cnn"
description: "Modern data augmentation for CNNs: MixUp (image and label interpolation), CutMix (patch-based mixing with area-weighted labels), Cutout, RandAugment, AugMix, and TrivialAugment. Covers implementation, calibration improvement (ECE), and choosing the right strategy."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGF0YSBhdWdtZW50YXRpb24gaXMgdGhlIG1vc3QgcmVsaWFibGUgcmVndWxhcml6YXRpb24gdGVjaG5pcXVlIGZvciBDTk5zOiBpdCBhcnRpZmljaWFsbHkgZXhwYW5kcyB0aGUgdHJhaW5pbmcgc2V0IGJ5IGFwcGx5aW5nIGxhYmVsLXByZXNlcnZpbmcgdHJhbnNmb3JtYXRpb25zIHRvIHRyYWluaW5nIGltYWdlcy4gU3RhbmRhcmQgYXVnbWVudGF0aW9uIChyYW5kb20gY3JvcHMsIGZsaXBzLCBjb2xvciBqaXR0ZXIpIGhhcyBiZWVuIHN0YW5kYXJkIHNpbmNlIEFsZXhOZXQuIE1vZGVybiBhdWdtZW50YXRpb24gc3RyYXRlZ2llcyBnbyBmdXJ0aGVyIOKAlCBNaXhVcCBhbmQgQ3V0TWl4IG1peCBpbWFnZXMgYW5kIGxhYmVscyB0b2dldGhlciwgUmFuZEF1Z21lbnQgYXV0b21hdGVzIHRoZSBzZWxlY3Rpb24gb2YgYXVnbWVudGF0aW9uIHBvbGljaWVzLCBhbmQgQXVnTWl4IGltcHJvdmVzIHJvYnVzdG5lc3MgdG8gZGlzdHJpYnV0aW9uIHNoaWZ0LiBUaGVzZSB0ZWNobmlxdWVzIGNvbnNpc3RlbnRseSBpbXByb3ZlIGJvdGggYWNjdXJhY3kgYW5kIGNhbGlicmF0aW9uIChob3cgd2VsbCBjb25maWRlbmNlIHNjb3JlcyByZWZsZWN0IHRydWUgYWNjdXJhY3kpLCBtYWtpbmcgdGhlbSBpbXBvcnRhbnQgdG9vbHMgZm9yIHByb2R1Y3Rpb24gZGVwbG95bWVudC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdGFuZGFyZCBBdWdtZW50YXRpb24gUGlwZWxpbmUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzdGFuZGFyZCBJbWFnZU5ldCBhdWdtZW50YXRpb24gcGlwZWxpbmU6ICgxKSBSYW5kb21SZXNpemVkQ3JvcCDigJQgcmFuZG9tbHkgY3JvcCB0aGVuIHJlc2l6ZSB0byAyMjTDlzIyNCwgc2FtcGxpbmcgY3JvcCBzY2FsZSB1bmlmb3JtbHkgZnJvbSBbMC4wOCwgMS4wXSBhbmQgYXNwZWN0IHJhdGlvIGZyb20gWzMvNCwgNC8zXTsgKDIpIFJhbmRvbUhvcml6b250YWxGbGlwIHdpdGggcD0wLjU7ICgzKSBDb2xvckppdHRlciDigJQgcmFuZG9tbHkgcGVydHVyYiBicmlnaHRuZXNzICgwLjQpLCBjb250cmFzdCAoMC40KSwgc2F0dXJhdGlvbiAoMC40KSwgaHVlICgwLjEpOyAoNCkgTm9ybWFsaXplIHdpdGggSW1hZ2VOZXQgbWVhbiBbMC40ODUsIDAuNDU2LCAwLjQwNl0gYW5kIHN0ZCBbMC4yMjksIDAuMjI0LCAwLjIyNV0uIEF0IHRlc3QgdGltZTogUmVzaXplIHRvIDI1NiwgQ2VudGVyQ3JvcCAyMjQsIE5vcm1hbGl6ZS4gVGhpcyBwaXBlbGluZSBpcyB0aGUgYmFzZWxpbmUgZm9yIG1vc3QgY2xhc3NpZmljYXRpb24gbW9kZWxzIGFuZCBjYW4gYmUgaW1wbGVtZW50ZWQgd2l0aCA1IGxpbmVzIGluIHRvcmNodmlzaW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1peFVwIOKAlCBJbWFnZSBhbmQgTGFiZWwgSW50ZXJwb2xhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWl4VXAgKFpoYW5nIGV0IGFsLiwgSUNMUiAyMDE4KSBjcmVhdGVzIHRyYWluaW5nIHNhbXBsZXMgYnkgbGluZWFybHkgaW50ZXJwb2xhdGluZyBwYWlycyBvZiBpbWFnZXMgQU5EIHRoZWlyIGxhYmVsczogeMyDID0gzrt44bWiICsgKDEtzrspeOKxvCwg4bu5ID0gzrt54bWiICsgKDEtzrspeeKxvCwgd2hlcmUgzrsgfiBCZXRhKM6xLCDOsSkuIFRoZSBtaXhlZCBpbWFnZSBpcyBhIHBpeGVsLXdpc2UgYmxlbmQgb2YgdHdvIHRyYWluaW5nIGltYWdlczsgdGhlIG1peGVkIGxhYmVsIGlzIGEgc29mdCBsYWJlbCBjb21iaW5pbmcgdGhlIHR3byBjbGFzcyBkaXN0cmlidXRpb25zLiBUcmFpbmluZyB3aXRoIE1peFVwIHByZXZlbnRzIHRoZSBtb2RlbCBmcm9tIGJlaW5nIG92ZXJjb25maWRlbnQgb24gYW55IGluZGl2aWR1YWwgdHJhaW5pbmcgZXhhbXBsZSDigJQgaXQgZm9yY2VzIHRoZSBtb2RlbCB0byBvdXRwdXQgaW50ZXJtZWRpYXRlIHByb2JhYmlsaXRpZXMgZm9yIG1peGVkIGlucHV0cywgd2hpY2ggaW1wcm92ZXMgY2FsaWJyYXRpb24gKEVDRSkuIE1peFVwIGNvbnNpc3RlbnRseSBpbXByb3ZlcyB0b3AtMSBhY2N1cmFjeSBieSAwLjLigJMwLjUlIGFuZCByZWR1Y2VzIEVDRSBieSAzMOKAkzUwJSByZWxhdGl2ZS4gzrE9MC40IGlzIHRoZSBzdGFuZGFyZCBkZWZhdWx0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkN1dE1peCDigJQgUGF0Y2gtQmFzZWQgTWl4aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDdXRNaXggKFl1biBldCBhbC4sIElDQ1YgMjAxOSkgcmVwbGFjZXMgYSByZWN0YW5ndWxhciBwYXRjaCBvZiBvbmUgdHJhaW5pbmcgaW1hZ2Ugd2l0aCB0aGUgY29ycmVzcG9uZGluZyBwYXRjaCBmcm9tIGFub3RoZXIgaW1hZ2UsIGFuZCBtaXhlcyBsYWJlbHMgcHJvcG9ydGlvbmFsbHkgdG8gdGhlIHBhdGNoIGFyZWE6IOG7uSA9IM67eeG1oiArICgxLc67KXnisbwgd2hlcmUgzrsgPSAxIOKIkiAocGF0Y2ggYXJlYSkvKGltYWdlIGFyZWEpLiBVbmxpa2UgTWl4VXAgd2hpY2ggYmxlbmRzIGVudGlyZSBpbWFnZXMsIEN1dE1peCBrZWVwcyBib3RoIHJlZ2lvbnMgbG9jYWxseSBwdXJlIChubyBibGVuZGluZyBhcnRpZmFjdHMpLCB3aGljaCBtYWtlcyBpdCBjb21wYXRpYmxlIHdpdGggb2JqZWN0IGRldGVjdGlvbiAoTWl4VXAgY3JlYXRlcyBvYmplY3RzLXdpdGhpbi1vYmplY3RzLCBjb25mdXNpbmcgZGV0ZWN0b3JzKS4gQ3V0TWl4IGlzIGdlbmVyYWxseSBwcmVmZXJyZWQgb3ZlciBNaXhVcCBmb3IgZGV0ZWN0aW9uIGFuZCBzZWdtZW50YXRpb24gdGFza3MsIGFuZCBwcm92aWRlcyBjb21wYXJhYmxlIGJlbmVmaXRzIGZvciBjbGFzc2lmaWNhdGlvbi4gVGhlIGJvdW5kaW5nIGJveCBpcyBzYW1wbGVkIHVuaWZvcm1seSwgYW5kIHRoZSBsYWJlbCBtaXhpbmcgcmF0aW8gaXMgZXhhY3QgKGFyZWEgcHJvcG9ydGlvbikuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6Ik1peFVwIHZzIEN1dE1peDogV2hlbiB0byBVc2UgV2hpY2giLCJjb250ZW50IjoiVXNlIE1peFVwIGZvciBjbGFzc2lmaWNhdGlvbiB0YXNrcyB3aGVyZSBnbG9iYWwgaW1hZ2Ugc3RhdGlzdGljcyBtYXR0ZXIgYW5kIHRoZSBtb2RlbCBzaG91bGQgaW50ZXJwb2xhdGUgYmV0d2VlbiBjbGFzc2VzIHNtb290aGx5LiBVc2UgQ3V0TWl4IGZvciBkZXRlY3Rpb24gYW5kIHNlZ21lbnRhdGlvbiB0YXNrcyBiZWNhdXNlIGl0IHByZXNlcnZlcyBzcGF0aWFsIGxvY2FsaXR5IOKAlCB0aGUgcGFzdGVkIHJlZ2lvbiBjb250YWlucyBhIHJlYWwgb2JqZWN0IHBhdGNoLCBub3QgYSBibGVuZGVkIGdob3N0LiBGb3IgYSBjb21iaW5lZCBzdHJhdGVneTogYXBwbHkgQ3V0TWl4IHdpdGggcHJvYmFiaWxpdHkgcD0wLjUgYW5kIE1peFVwIG90aGVyd2lzZSwgd2hpY2ggY2FwdHVyZXMgYmVuZWZpdHMgb2YgYm90aC4gQm90aCBtZXRob2RzIGNhbiBiZSBhcHBsaWVkIHNpbXVsdGFuZW91c2x5IGluIHRoZSBzYW1lIGJhdGNoIHVzaW5nIGRpZmZlcmVudCBhbHBoYSB2YWx1ZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZSBFeGFtcGxlcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBtaXh1cF9kYXRhKHg6IHRvcmNoLlRlbnNvciwgeTogdG9yY2guVGVuc29yLCBhbHBoYTogZmxvYXQgPSAwLjQpOlxuICAgIFwiXCJcIk1peFVwOiBsaW5lYXJseSBpbnRlcnBvbGF0ZSBpbWFnZSBwYWlycyBhbmQgdGhlaXIgbGFiZWxzLlwiXCJcIlxuICAgIGxhbSA9IG5wLnJhbmRvbS5iZXRhKGFscGhhLCBhbHBoYSkgaWYgYWxwaGEgXHUwMDNlIDAgZWxzZSAxLjBcbiAgICBwZXJtID0gdG9yY2gucmFuZHBlcm0oeC5zaXplKDApLCBkZXZpY2U9eC5kZXZpY2UpXG4gICAgeF9taXggID0gbGFtICogeCArICgxLjAgLSBsYW0pICogeFtwZXJtXVxuICAgIHlfYSwgeV9iID0geSwgeVtwZXJtXVxuICAgIHJldHVybiB4X21peCwgeV9hLCB5X2IsIGxhbVxuXG5kZWYgbWl4dXBfY3JpdGVyaW9uKGNyaXRlcmlvbiwgcHJlZCwgeV9hLCB5X2IsIGxhbSk6XG4gICAgXCJcIlwiTWl4ZWQgbG9zczogbGFtICogQ0UocHJlZCwgeWEpICsgKDEtbGFtKSAqIENFKHByZWQsIHliKS5cIlwiXCJcbiAgICByZXR1cm4gbGFtICogY3JpdGVyaW9uKHByZWQsIHlfYSkgKyAoMS4wIC0gbGFtKSAqIGNyaXRlcmlvbihwcmVkLCB5X2IpXG5cbiMgU2ltdWxhdGUgb25lIHRyYWluaW5nIGJhdGNoIHdpdGggTWl4VXBcbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5ucC5yYW5kb20uc2VlZCgwKVxubW9kZWwgICAgID0gbm4uTGluZWFyKDEyOCwgMTApXG5jcml0ZXJpb24gPSBubi5Dcm9zc0VudHJvcHlMb3NzKClcbnggPSB0b3JjaC5yYW5kbigzMiwgMTI4KVxueSA9IHRvcmNoLnJhbmRpbnQoMCwgMTAsICgzMiwpKVxuXG54X21peCwgeWEsIHliLCBsYW0gPSBtaXh1cF9kYXRhKHgsIHksIGFscGhhPTAuNClcbnByZWQgPSBtb2RlbCh4X21peClcbmxvc3MgPSBtaXh1cF9jcml0ZXJpb24oY3JpdGVyaW9uLCBwcmVkLCB5YSwgeWIsIGxhbSlcbnByaW50KGZcIkxhbWJkYTogICAgICB7bGFtOi40Zn1cIilcbnByaW50KGZcInhfbWl4IGlzIHtsYW06LjElfSBvZiB4W2ldICsgeygxLWxhbSk6LjElfSBvZiB4W3Blcm1baV1dXCIpXG5wcmludChmXCJNaXhVcCBsb3NzOiAge2xvc3MuaXRlbSgpOi40Zn0gIChzb2Z0IGNyb3NzLWVudHJvcHkgb3ZlciB0d28gbGFiZWxzKVwiKVxucHJpbnQoXCJFZmZlY3Q6IHByZXZlbnRzIG92ZXJjb25maWRlbmNlOyBpbXByb3ZlcyBjYWxpYnJhdGlvbiAobG93ZXIgRUNFKVwiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgcmFuZF9iYm94KEg6IGludCwgVzogaW50LCBsYW06IGZsb2F0KTpcbiAgICBcIlwiXCJTYW1wbGUgYSByYW5kb20gYm91bmRpbmcgYm94IHdpdGggYXJlYSBwcm9wb3J0aW9uICgxLWxhbSkuXCJcIlwiXG4gICAgY3V0X3JhdGlvID0gbnAuc3FydCgxLjAgLSBsYW0pXG4gICAgY3V0X2gsIGN1dF93ID0gaW50KEggKiBjdXRfcmF0aW8pLCBpbnQoVyAqIGN1dF9yYXRpbylcbiAgICBjeSwgY3ggPSBucC5yYW5kb20ucmFuZGludChIKSwgbnAucmFuZG9tLnJhbmRpbnQoVylcbiAgICB5MSA9IG5wLmNsaXAoY3kgLSBjdXRfaCAvLyAyLCAwLCBIKVxuICAgIHkyID0gbnAuY2xpcChjeSArIGN1dF9oIC8vIDIsIDAsIEgpXG4gICAgeDEgPSBucC5jbGlwKGN4IC0gY3V0X3cgLy8gMiwgMCwgVylcbiAgICB4MiA9IG5wLmNsaXAoY3ggKyBjdXRfdyAvLyAyLCAwLCBXKVxuICAgIHJldHVybiB5MSwgeTIsIHgxLCB4MlxuXG5kZWYgY3V0bWl4X2JhdGNoKHg6IHRvcmNoLlRlbnNvciwgeTogdG9yY2guVGVuc29yLCBhbHBoYTogZmxvYXQgPSAxLjApOlxuICAgIFwiXCJcIkN1dE1peDogcGFzdGUgYSByZWN0YW5ndWxhciBjcm9wIGZyb20gb25lIGltYWdlIG9udG8gYW5vdGhlci5cIlwiXCJcbiAgICBsYW0gPSBucC5yYW5kb20uYmV0YShhbHBoYSwgYWxwaGEpXG4gICAgQiwgQywgSCwgVyA9IHguc2hhcGVcbiAgICBwZXJtID0gdG9yY2gucmFuZHBlcm0oQilcbiAgICB5MSwgeTIsIHgxLCB4MiA9IHJhbmRfYmJveChILCBXLCBsYW0pXG4gICAgeF9jdXQgPSB4LmNsb25lKClcbiAgICB4X2N1dFs6LCA6LCB5MTp5MiwgeDE6eDJdID0geFtwZXJtLCA6LCB5MTp5MiwgeDE6eDJdICAjIHBhc3RlIHBhdGNoIGZyb20gcGVybVxuICAgIGxhbV9hY3R1YWwgPSAxLjAgLSAoeTIgLSB5MSkgKiAoeDIgLSB4MSkgLyAoSCAqIFcpICAgICMgYWN0dWFsIGFyZWEgcmF0aW9cbiAgICByZXR1cm4geF9jdXQsIHksIHlbcGVybV0sIGxhbV9hY3R1YWxcblxudG9yY2gubWFudWFsX3NlZWQoMSk7IG5wLnJhbmRvbS5zZWVkKDEpXG54ID0gdG9yY2gucmFuZG4oOCwgMywgMjI0LCAyMjQpXG55ID0gdG9yY2gucmFuZGludCgwLCAxMDAwLCAoOCwpKVxueF9jdXQsIHlhLCB5YiwgbGFtID0gY3V0bWl4X2JhdGNoKHgsIHksIGFscGhhPTEuMClcbnByaW50KGZcIklucHV0OiAge3guc2hhcGV9XCIpXG5wcmludChmXCJPdXRwdXQ6IHt4X2N1dC5zaGFwZX1cIilcbnByaW50KGZcImxhbSAoYWN0dWFsIGFyZWEgZnJhY3Rpb24pOiB7bGFtOi40Zn1cIilcbnByaW50KGZcIkxhYmVsIG1peDoge2xhbTouMiV9IHlhICsgezEtbGFtOi4yJX0geWIgIChwcm9wb3J0aW9uYWwgdG8gcHJlc2VydmVkIGFyZWEpXCIpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgdHJhbnNmb3Jtc1xuZnJvbSB0b3JjaHZpc2lvbi50cmFuc2Zvcm1zIGltcG9ydCBSYW5kQXVnbWVudCwgQXV0b0F1Z21lbnRcblxuIyBSYW5kQXVnbWVudChudW1fb3BzPU4sIG1hZ25pdHVkZT1NKVxuIyBSYW5kb21seSBwaWNrcyBOIHRyYW5zZm9ybXMgZnJvbSBhIHBvb2wgb2YgMTQgYXQgZWFjaCBzdGVwLFxuIyBlYWNoIGFwcGxpZWQgd2l0aCB0aGUgc2FtZSBtYWduaXR1ZGUgTSAocmFuZ2UgMC0zMDsgZGVmYXVsdCBNPTkpXG5yYW5kX2F1ZyA9IFJhbmRBdWdtZW50KG51bV9vcHM9MiwgbWFnbml0dWRlPTkpXG5cbiMgVGhlIDE0IGF2YWlsYWJsZSBvcGVyYXRpb25zIGluIHRoZSBwb29sOlxub3BzID0gW1xuICAgIFx1MDAyN0lkZW50aXR5XHUwMDI3LCBcdTAwMjdBdXRvQ29udHJhc3RcdTAwMjcsIFx1MDAyN0VxdWFsaXplXHUwMDI3LCBcdTAwMjdSb3RhdGVcdTAwMjcsXG4gICAgXHUwMDI3U29sYXJpemVcdTAwMjcsIFx1MDAyN0NvbG9yXHUwMDI3LCBcdTAwMjdQb3N0ZXJpemVcdTAwMjcsIFx1MDAyN0NvbnRyYXN0XHUwMDI3LFxuICAgIFx1MDAyN0JyaWdodG5lc3NcdTAwMjcsIFx1MDAyN1NoYXJwbmVzc1x1MDAyNywgXHUwMDI3U2hlYXJYXHUwMDI3LCBcdTAwMjdTaGVhcllcdTAwMjcsXG4gICAgXHUwMDI3VHJhbnNsYXRlWFx1MDAyNywgXHUwMDI3VHJhbnNsYXRlWVx1MDAyNyxcbl1cbnByaW50KGZcIlJhbmRBdWdtZW50IHBvb2w6IHtsZW4ob3BzKX0gb3BlcmF0aW9uc1wiKVxucHJpbnQoZlwiRGVmYXVsdDogTj0yIG9wcywgTT05IG1hZ25pdHVkZSAocmFuZ2UgMC0zMClcIilcbnByaW50KGZcIk9ubHkgMiBoeXBlcnBhcmFtZXRlcnMgdnMgMjUrIGZvciBBdXRvQXVnbWVudCBwb2xpY3kgc2VhcmNoXCIpXG5cbiMgU3RhbmRhcmQgdHJhaW5pbmcgcGlwZWxpbmUgd2l0aCBSYW5kQXVnbWVudFxudHJhaW5fdHJhbnNmb3JtID0gdHJhbnNmb3Jtcy5Db21wb3NlKFtcbiAgICB0cmFuc2Zvcm1zLlJhbmRvbVJlc2l6ZWRDcm9wKDIyNCksXG4gICAgdHJhbnNmb3Jtcy5SYW5kb21Ib3Jpem9udGFsRmxpcCgpLFxuICAgIFJhbmRBdWdtZW50KG51bV9vcHM9MiwgbWFnbml0dWRlPTkpLFxuICAgIHRyYW5zZm9ybXMuVG9UZW5zb3IoKSxcbiAgICB0cmFuc2Zvcm1zLk5vcm1hbGl6ZShbMC40ODUsIDAuNDU2LCAwLjQwNl0sIFswLjIyOSwgMC4yMjQsIDAuMjI1XSksXG5dKVxucHJpbnQoKVxucHJpbnQoXCJUcmFpbmluZyBwaXBlbGluZTogUmFuZG9tUmVzaXplZENyb3AgLVx1MDAzZSBGbGlwIC1cdTAwM2UgUmFuZEF1Z21lbnQoTj0yLE09OSkgLVx1MDAzZSBOb3JtYWxpemVcIilcbnByaW50KFwiVHJpdmlhbEF1Z21lbnQ6IHVuaWZvcm1seSByYW5kb20gb3AgKyBtYWduaXR1ZGUgLS0gc2ltcGxlc3QgU09UQSBhcHByb2FjaFwiKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZXhwZWN0ZWRfY2FsaWJyYXRpb25fZXJyb3IocHJvYnM6IG5wLm5kYXJyYXksIGxhYmVsczogbnAubmRhcnJheSwgbl9iaW5zOiBpbnQgPSAxMCk6XG4gICAgXCJcIlwiRUNFOiBtZWFzdXJlIGhvdyB3ZWxsIG1vZGVsIGNvbmZpZGVuY2UgbWF0Y2hlcyBhY2N1cmFjeSAobG93ZXIgaXMgYmV0dGVyKS5cIlwiXCJcbiAgICBjb25maWRlbmNlcyA9IHByb2JzLm1heChheGlzPTEpXG4gICAgcHJlZGljdGlvbnMgPSBwcm9icy5hcmdtYXgoYXhpcz0xKVxuICAgIGNvcnJlY3QgPSAocHJlZGljdGlvbnMgPT0gbGFiZWxzKS5hc3R5cGUoZmxvYXQpXG4gICAgYmluX2VkZ2VzID0gbnAubGluc3BhY2UoMCwgMSwgbl9iaW5zICsgMSlcbiAgICBlY2UgPSAwLjBcbiAgICBmb3IgbG8sIGhpIGluIHppcChiaW5fZWRnZXNbOi0xXSwgYmluX2VkZ2VzWzE6XSk6XG4gICAgICAgIG1hc2sgPSAoY29uZmlkZW5jZXMgXHUwMDNlIGxvKSBcdTAwMjYgKGNvbmZpZGVuY2VzIFx1MDAzYz0gaGkpXG4gICAgICAgIGlmIG1hc2suc3VtKCkgPT0gMDpcbiAgICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgIGFjYyAgPSBjb3JyZWN0W21hc2tdLm1lYW4oKVxuICAgICAgICBjb25mID0gY29uZmlkZW5jZXNbbWFza10ubWVhbigpXG4gICAgICAgIGVjZSArPSAobWFzay5tZWFuKCkgKiBhYnMoYWNjIC0gY29uZikpXG4gICAgcmV0dXJuIGVjZVxuXG4jIFNpbXVsYXRlZCBjYWxpYnJhdGlvbiByZXN1bHRzIGZvciBkaWZmZXJlbnQgYXVnbWVudGF0aW9uIHN0cmF0ZWdpZXNcbnJlc3VsdHMgPSBbXG4gICAgKFx1MDAyN05vIGF1Z21lbnRhdGlvblx1MDAyNywgICAgICAwLjkyMSwgMC4wNDMpLFxuICAgIChcdTAwMjdCYXNpYyAoZmxpcCtjcm9wKVx1MDAyNywgICAgMC45MzQsIDAuMDMxKSxcbiAgICAoXHUwMDI3Q3V0b3V0XHUwMDI3LCAgICAgICAgICAgICAgIDAuOTM3LCAwLjAyNiksXG4gICAgKFx1MDAyN01peFVwIChhbHBoYT0wLjQpXHUwMDI3LCAgICAwLjk0MSwgMC4wMTgpLFxuICAgIChcdTAwMjdDdXRNaXggKGFscGhhPTEuMClcdTAwMjcsICAgMC45NDMsIDAuMDE1KSxcbiAgICAoXHUwMDI3UmFuZEF1Z21lbnQgKE49MixNPTkpXHUwMDI3LDAuOTQ2LCAwLjAxNiksXG4gICAgKFx1MDAyN0F1Z01peFx1MDAyNywgICAgICAgICAgICAgICAwLjk0NCwgMC4wMTIpLFxuXVxuXG5wcmludChmXCJ7XHUwMDI3TWV0aG9kXHUwMDI3Olx1MDAzYzI4fSB7XHUwMDI3VG9wLTEgQWNjXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3RUNFXHUwMDI3Olx1MDAzZTh9ICBOb3Rlc1wiKVxucHJpbnQoXHUwMDI3LVx1MDAyNyAqIDY1KVxuZm9yIG1ldGhvZCwgYWNjLCBlY2UgaW4gcmVzdWx0czpcbiAgICBub3RlID0gXHUwMDI3YmVzdCBjYWxpYnJhdGlvblx1MDAyNyBpZiBlY2UgPT0gbWluKHJbMl0gZm9yIHIgaW4gcmVzdWx0cykgZWxzZSBcdTAwMjdcdTAwMjdcbiAgICBwcmludChmXCJ7bWV0aG9kOlx1MDAzYzI4fSB7YWNjOlx1MDAzZTkuM2Z9ICB7ZWNlOlx1MDAzZTcuM2Z9ICB7bm90ZX1cIilcbnByaW50KClcbnByaW50KFwiRUNFID0gRXhwZWN0ZWQgQ2FsaWJyYXRpb24gRXJyb3IgKGxvd2VyID0gcHJlZGljdGlvbnMgYXJlIGJldHRlciBjYWxpYnJhdGVkKVwiKVxucHJpbnQoXCJNaXhVcC9DdXRNaXggcHJldmVudCBvdmVyY29uZmlkZW5jZSBieSB0cmFpbmluZyBvbiBtaXhlZC9pbnRlcnBvbGF0ZWQgbGFiZWxzXCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmFuZEF1Z21lbnQgYW5kIFRyaXZpYWxBdWdtZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSYW5kQXVnbWVudCAoQ3VidWsgZXQgYWwuLCAyMDE5KSBzaW1wbGlmaWVzIGF1Z21lbnRhdGlvbiBwb2xpY3kgc2VhcmNoIHRvIGp1c3QgdHdvIGh5cGVycGFyYW1ldGVyczogTiAobnVtYmVyIG9mIG9wZXJhdGlvbnMgdG8gYXBwbHkgcGVyIGltYWdlKSBhbmQgTSAodGhlIHNoYXJlZCBtYWduaXR1ZGUgb2YgYWxsIG9wZXJhdGlvbnMpLiBBdCBlYWNoIHRyYWluaW5nIHN0ZXAsIE4gb3BlcmF0aW9ucyBhcmUgc2FtcGxlZCB1bmlmb3JtbHkgZnJvbSBhIHBvb2wgb2YgMTQgYW5kIGFwcGxpZWQgc2VxdWVudGlhbGx5IHdpdGggbWFnbml0dWRlIE0uIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IGEgc2hhcmVkIG1hZ25pdHVkZSBpcyBhbG1vc3QgYXMgZ29vZCBhcyBwZXItb3BlcmF0aW9uIG1hZ25pdHVkZXMsIGRyYW1hdGljYWxseSByZWR1Y2luZyB0aGUgc2VhcmNoIHNwYWNlLiBEZWZhdWx0IE49MiwgTT05IHdvcmtzIHdlbGwgYWNyb3NzIG1vc3QgdGFza3MuIFRyaXZpYWxBdWdtZW50IChNw7xsbGVyIFx1MDAyNiBIdXR0ZXIsIDIwMjEpIHNpbXBsaWZpZXMgZXZlbiBmdXJ0aGVyOiBzYW1wbGUgb25lIG9wZXJhdGlvbiBhdCByYW5kb20gYW5kIHNhbXBsZSBpdHMgbWFnbml0dWRlIHVuaWZvcm1seSBmcm9tIHRoZSBmdWxsIHJhbmdlIOKAlCB6ZXJvIGh5cGVycGFyYW1ldGVycyB0byB0dW5lLCBvZnRlbiBjb21wZXRpdGl2ZSB3aXRoIFJhbmRBdWdtZW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF1Z01peCBhbmQgUm9idXN0bmVzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXVnTWl4IChIZW5kcnlja3MgZXQgYWwuLCAyMDIwKSBpcyBkZXNpZ25lZCBzcGVjaWZpY2FsbHkgdG8gaW1wcm92ZSByb2J1c3RuZXNzIHRvIGRpc3RyaWJ1dGlvbiBzaGlmdCwgbm90IGp1c3QgY2xlYW4gYWNjdXJhY3kuIEl0IGdlbmVyYXRlcyBtdWx0aXBsZSBhdWdtZW50ZWQgdmVyc2lvbnMgb2YgZWFjaCBpbWFnZSB1c2luZyBkaWZmZXJlbnQgcmFuZG9tbHkgc2FtcGxlZCBhdWdtZW50YXRpb24gY2hhaW5zLCB0aGVuIG1peGVzIHRoZW0gd2l0aCB0aGUgb3JpZ2luYWwgaW1hZ2UgdXNpbmcgRGlyaWNobGV0LXNhbXBsZWQgd2VpZ2h0cy4gQSBKZW5zZW4tU2hhbm5vbiBjb25zaXN0ZW5jeSBsb3NzIGVuY291cmFnZXMgdGhlIG1vZGVsIHRvIG1ha2UgY29uc2lzdGVudCBwcmVkaWN0aW9ucyBhY3Jvc3MgYWxsIGF1Z21lbnRlZCB2ZXJzaW9ucy4gQXVnTWl4IGltcHJvdmVzIHBlcmZvcm1hbmNlIG9uIEltYWdlTmV0LUMgKGNvcnJ1cHRlZCBJbWFnZU5ldCkgYnkgMTLigJMxNSUgd2hpbGUgbWFpbnRhaW5pbmcgY2xlYW4gYWNjdXJhY3kuIEl0IGlzIHRoZSBwcmVmZXJyZWQgYXVnbWVudGF0aW9uIHdoZW4gcm9idXN0bmVzcyB0byByZWFsLXdvcmxkIGRpc3RyaWJ1dGlvbiBzaGlmdCAoYmx1ciwgbm9pc2UsIGNvbXByZXNzaW9uIGFydGlmYWN0cykgbWF0dGVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBdWdtZW50YXRpb24gTWV0aG9kIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiTGFiZWwgTWl4aW5nIiwiRGV0ZWN0aW9uIFNhZmUiLCJUcmFpbmluZyBPdmVyaGVhZCIsIkNhbGlicmF0aW9uIChFQ0UpIiwiQ29ycnVwdGlvbiBSb2J1c3RuZXNzIl0sInJvd3MiOltbIkJhc2ljIChmbGlwICsgY3JvcCkiLCJObyIsIlllcyIsIk5vbmUiLCJQb29yIiwiTG93Il0sWyJDdXRvdXQiLCJObyIsIlBhcnRpYWwiLCJNaW5pbWFsIiwiTW9kZXJhdGUiLCJNb2RlcmF0ZSJdLFsiTWl4VXAgKM6xPTAuNCkiLCJZZXMg4oCUIGxpbmVhciBibGVuZCIsIk5vIiwiTWluaW1hbCIsIkdvb2QiLCJNb2RlcmF0ZSJdLFsiQ3V0TWl4ICjOsT0xLjApIiwiWWVzIOKAlCBhcmVhLXdlaWdodGVkIiwiWWVzIiwiTWluaW1hbCIsIkdvb2QiLCJHb29kIl0sWyJSYW5kQXVnbWVudCAoTj0yLE09OSkiLCJObyIsIlllcyIsIkxvdyAoMiBleHRyYSBhdWdtZW50cykiLCJNb2RlcmF0ZSIsIkhpZ2giXSxbIkF1Z01peCIsIk5vIChKUyBjb25zaXN0ZW5jeSBsb3NzKSIsIlllcyIsIk1lZGl1bSAoM3ggZm9yd2FyZCkiLCJCZXN0IiwiSGlnaGVzdCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hvb3NpbmcgYW4gQXVnbWVudGF0aW9uIFN0cmF0ZWd5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2hvaWNlIG9mIGF1Z21lbnRhdGlvbiBzaG91bGQgYmUgZ3VpZGVkIGJ5IHRoZSB0YXNrIGFuZCBkZXBsb3ltZW50IGNvbnRleHQuIEZvciBzdGFuZGFyZCBJbWFnZU5ldCBjbGFzc2lmaWNhdGlvbiwgUmFuZEF1Z21lbnQoTj0yLCBNPTkpIHdpdGggQ3V0TWl4IGlzIHRoZSBjdXJyZW50IGRlZmF1bHQgaW4gbW9zdCBTT1RBIHRyYWluaW5nIHJlY2lwZXMgKHRpbW0gbGlicmFyeSB1c2VzIHRoaXMgYnkgZGVmYXVsdCkuIEZvciBvYmplY3QgZGV0ZWN0aW9uIGFuZCBzZWdtZW50YXRpb24sIHVzZSBDdXRNaXggb3ZlciBNaXhVcCBhbmQgYXZvaWQgYXVnbWVudGF0aW9ucyB0aGF0IGJsZW5kIG9iamVjdCBib3VuZGFyaWVzIChubyBNaXhVcCBvbiBib3VuZGluZyBib3hlcykuIEZvciBtb2RlbHMgdGhhdCB3aWxsIGJlIGRlcGxveWVkIG9uIGNvcnJ1cHRlZCBvciBvdXQtb2YtZGlzdHJpYnV0aW9uIGRhdGEgKG1lZGljYWwgZGV2aWNlcywgYXV0b25vbW91cyB2ZWhpY2xlcywgY2FtZXJhcyBpbiB2YXJpYWJsZSBjb25kaXRpb25zKSwgQXVnTWl4IHdpdGggdGhlIEplbnNlbi1TaGFubm9uIGNvbnNpc3RlbmN5IGxvc3MgcHJvdmlkZXMgdGhlIGJlc3Qgcm9idXN0bmVzcy4gRm9yIHRpbnkgZGF0YXNldHMgKFx1MDAzYzEwMDAgaW1hZ2VzKSwgYWdncmVzc2l2ZSBzdGFuZGFyZCBhdWdtZW50YXRpb24gKGhlYXZ5IGNyb3AsIGZsaXAsIGNvbG9yIGppdHRlciwgcm90YXRpb24pIGlzIG1vcmUgYmVuZWZpY2lhbCB0aGFuIE1peFVwL0N1dE1peCwgd2hpY2ggcmVxdWlyZSBzdWZmaWNpZW50IGNsYXNzIGNvdmVyYWdlIHdpdGhpbiBlYWNoIGJhdGNoLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3RhbmRhcmQgYmFzZWxpbmU6IFJhbmRvbVJlc2l6ZWRDcm9wKDIyNCkgKyBIb3Jpem9udGFsRmxpcCgwLjUpICsgQ29sb3JKaXR0ZXIgKyBOb3JtYWxpemUuIiwiTWl4VXA6IGJsZW5kIHR3byBpbWFnZXMgYW5kIGxhYmVsczsgzrt+QmV0YSjOsSzOsSk7IHByZXZlbnRzIG92ZXJjb25maWRlbmNlOyBpbXByb3ZlcyBFQ0UuIiwiQ3V0TWl4OiBwYXN0ZSByZWN0YW5ndWxhciBwYXRjaDsgbGFiZWwg4oidIGFyZWE7IGRldGVjdGlvbi1zYWZlIChubyBibGVuZGluZyBhcnRpZmFjdHMpLiIsIlJhbmRBdWdtZW50OiBOIG9wcyBmcm9tIHBvb2wgb2YgMTQsIG1hZ25pdHVkZSBNOyBvbmx5IDIgaHlwZXJwYXJhbXM7IGRlZmF1bHQgTj0yLCBNPTkuIiwiVHJpdmlhbEF1Z21lbnQ6IDEgcmFuZG9tIG9wLCByYW5kb20gbWFnbml0dWRlOyB6ZXJvIGh5cGVycGFyYW1zOyBjb21wZXRpdGl2ZSB3aXRoIFJhbmRBdWdtZW50LiIsIkF1Z01peDogY29uc2lzdGVuY3kgbG9zcyBvdmVyIGF1Z21lbnRhdGlvbiBjaGFpbnM7IGJlc3QgZm9yIHJvYnVzdG5lc3MgdG8gZGlzdHJpYnV0aW9uIHNoaWZ0LiJdfV0="
---
# Data Augmentation — CutMix, MixUp, and RandAugment

Data augmentation is the most reliable regularization technique for CNNs: it artificially expands the training set by applying label-preserving transformations to training images. Standard augmentation (random crops, flips, color jitter) has been standard since AlexNet. Modern augmentation strategies go further — MixUp and CutMix mix images and labels together, RandAugment automates the selection of augmentation policies, and AugMix improves robustness to distribution shift. These techniques consistently improve both accuracy and calibration (how well confidence scores reflect true accuracy), making them important tools for production deployment.

## Standard Augmentation Pipeline

The standard ImageNet augmentation pipeline: (1) RandomResizedCrop — randomly crop then resize to 224×224, sampling crop scale uniformly from [0.08, 1.0] and aspect ratio from [3/4, 4/3]; (2) RandomHorizontalFlip with p=0.5; (3) ColorJitter — randomly perturb brightness (0.4), contrast (0.4), saturation (0.4), hue (0.1); (4) Normalize with ImageNet mean [0.485, 0.456, 0.406] and std [0.229, 0.224, 0.225]. At test time: Resize to 256, CenterCrop 224, Normalize. This pipeline is the baseline for most classification models and can be implemented with 5 lines in torchvision.

## MixUp — Image and Label Interpolation

MixUp (Zhang et al., ICLR 2018) creates training samples by linearly interpolating pairs of images AND their labels: x̃ = λxᵢ + (1-λ)xⱼ, ỹ = λyᵢ + (1-λ)yⱼ, where λ ~ Beta(α, α). The mixed image is a pixel-wise blend of two training images; the mixed label is a soft label combining the two class distributions. Training with MixUp prevents the model from being overconfident on any individual training example — it forces the model to output intermediate probabilities for mixed inputs, which improves calibration (ECE). MixUp consistently improves top-1 accuracy by 0.2–0.5% and reduces ECE by 30–50% relative. α=0.4 is the standard default.

## CutMix — Patch-Based Mixing

CutMix (Yun et al., ICCV 2019) replaces a rectangular patch of one training image with the corresponding patch from another image, and mixes labels proportionally to the patch area: ỹ = λyᵢ + (1-λ)yⱼ where λ = 1 − (patch area)/(image area). Unlike MixUp which blends entire images, CutMix keeps both regions locally pure (no blending artifacts), which makes it compatible with object detection (MixUp creates objects-within-objects, confusing detectors). CutMix is generally preferred over MixUp for detection and segmentation tasks, and provides comparable benefits for classification. The bounding box is sampled uniformly, and the label mixing ratio is exact (area proportion).

> **MixUp vs CutMix: When to Use Which**: Use MixUp for classification tasks where global image statistics matter and the model should interpolate between classes smoothly. Use CutMix for detection and segmentation tasks because it preserves spatial locality — the pasted region contains a real object patch, not a blended ghost. For a combined strategy: apply CutMix with probability p=0.5 and MixUp otherwise, which captures benefits of both. Both methods can be applied simultaneously in the same batch using different alpha values.

## Code Examples

```python
import torch
import torch.nn as nn
import numpy as np

def mixup_data(x: torch.Tensor, y: torch.Tensor, alpha: float = 0.4):
    """MixUp: linearly interpolate image pairs and their labels."""
    lam = np.random.beta(alpha, alpha) if alpha > 0 else 1.0
    perm = torch.randperm(x.size(0), device=x.device)
    x_mix  = lam * x + (1.0 - lam) * x[perm]
    y_a, y_b = y, y[perm]
    return x_mix, y_a, y_b, lam

def mixup_criterion(criterion, pred, y_a, y_b, lam):
    """Mixed loss: lam * CE(pred, ya) + (1-lam) * CE(pred, yb)."""
    return lam * criterion(pred, y_a) + (1.0 - lam) * criterion(pred, y_b)

# Simulate one training batch with MixUp
torch.manual_seed(0)
np.random.seed(0)
model     = nn.Linear(128, 10)
criterion = nn.CrossEntropyLoss()
x = torch.randn(32, 128)
y = torch.randint(0, 10, (32,))

x_mix, ya, yb, lam = mixup_data(x, y, alpha=0.4)
pred = model(x_mix)
loss = mixup_criterion(criterion, pred, ya, yb, lam)
print(f"Lambda:      {lam:.4f}")
print(f"x_mix is {lam:.1%} of x[i] + {(1-lam):.1%} of x[perm[i]]")
print(f"MixUp loss:  {loss.item():.4f}  (soft cross-entropy over two labels)")
print("Effect: prevents overconfidence; improves calibration (lower ECE)")
```

```python
import torch
import numpy as np

def rand_bbox(H: int, W: int, lam: float):
    """Sample a random bounding box with area proportion (1-lam)."""
    cut_ratio = np.sqrt(1.0 - lam)
    cut_h, cut_w = int(H * cut_ratio), int(W * cut_ratio)
    cy, cx = np.random.randint(H), np.random.randint(W)
    y1 = np.clip(cy - cut_h // 2, 0, H)
    y2 = np.clip(cy + cut_h // 2, 0, H)
    x1 = np.clip(cx - cut_w // 2, 0, W)
    x2 = np.clip(cx + cut_w // 2, 0, W)
    return y1, y2, x1, x2

def cutmix_batch(x: torch.Tensor, y: torch.Tensor, alpha: float = 1.0):
    """CutMix: paste a rectangular crop from one image onto another."""
    lam = np.random.beta(alpha, alpha)
    B, C, H, W = x.shape
    perm = torch.randperm(B)
    y1, y2, x1, x2 = rand_bbox(H, W, lam)
    x_cut = x.clone()
    x_cut[:, :, y1:y2, x1:x2] = x[perm, :, y1:y2, x1:x2]  # paste patch from perm
    lam_actual = 1.0 - (y2 - y1) * (x2 - x1) / (H * W)    # actual area ratio
    return x_cut, y, y[perm], lam_actual

torch.manual_seed(1); np.random.seed(1)
x = torch.randn(8, 3, 224, 224)
y = torch.randint(0, 1000, (8,))
x_cut, ya, yb, lam = cutmix_batch(x, y, alpha=1.0)
print(f"Input:  {x.shape}")
print(f"Output: {x_cut.shape}")
print(f"lam (actual area fraction): {lam:.4f}")
print(f"Label mix: {lam:.2%} ya + {1-lam:.2%} yb  (proportional to preserved area)")
```

```python
import torch
from torchvision import transforms
from torchvision.transforms import RandAugment, AutoAugment

# RandAugment(num_ops=N, magnitude=M)
# Randomly picks N transforms from a pool of 14 at each step,
# each applied with the same magnitude M (range 0-30; default M=9)
rand_aug = RandAugment(num_ops=2, magnitude=9)

# The 14 available operations in the pool:
ops = [
    'Identity', 'AutoContrast', 'Equalize', 'Rotate',
    'Solarize', 'Color', 'Posterize', 'Contrast',
    'Brightness', 'Sharpness', 'ShearX', 'ShearY',
    'TranslateX', 'TranslateY',
]
print(f"RandAugment pool: {len(ops)} operations")
print(f"Default: N=2 ops, M=9 magnitude (range 0-30)")
print(f"Only 2 hyperparameters vs 25+ for AutoAugment policy search")

# Standard training pipeline with RandAugment
train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    RandAugment(num_ops=2, magnitude=9),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
print()
print("Training pipeline: RandomResizedCrop -> Flip -> RandAugment(N=2,M=9) -> Normalize")
print("TrivialAugment: uniformly random op + magnitude -- simplest SOTA approach")
```

```python
import torch
import numpy as np

def expected_calibration_error(probs: np.ndarray, labels: np.ndarray, n_bins: int = 10):
    """ECE: measure how well model confidence matches accuracy (lower is better)."""
    confidences = probs.max(axis=1)
    predictions = probs.argmax(axis=1)
    correct = (predictions == labels).astype(float)
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
        mask = (confidences > lo) & (confidences <= hi)
        if mask.sum() == 0:
            continue
        acc  = correct[mask].mean()
        conf = confidences[mask].mean()
        ece += (mask.mean() * abs(acc - conf))
    return ece

# Simulated calibration results for different augmentation strategies
results = [
    ('No augmentation',      0.921, 0.043),
    ('Basic (flip+crop)',    0.934, 0.031),
    ('Cutout',               0.937, 0.026),
    ('MixUp (alpha=0.4)',    0.941, 0.018),
    ('CutMix (alpha=1.0)',   0.943, 0.015),
    ('RandAugment (N=2,M=9)',0.946, 0.016),
    ('AugMix',               0.944, 0.012),
]

print(f"{'Method':<28} {'Top-1 Acc':>10} {'ECE':>8}  Notes")
print('-' * 65)
for method, acc, ece in results:
    note = 'best calibration' if ece == min(r[2] for r in results) else ''
    print(f"{method:<28} {acc:>9.3f}  {ece:>7.3f}  {note}")
print()
print("ECE = Expected Calibration Error (lower = predictions are better calibrated)")
print("MixUp/CutMix prevent overconfidence by training on mixed/interpolated labels")
```

## RandAugment and TrivialAugment

RandAugment (Cubuk et al., 2019) simplifies augmentation policy search to just two hyperparameters: N (number of operations to apply per image) and M (the shared magnitude of all operations). At each training step, N operations are sampled uniformly from a pool of 14 and applied sequentially with magnitude M. The key insight is that a shared magnitude is almost as good as per-operation magnitudes, dramatically reducing the search space. Default N=2, M=9 works well across most tasks. TrivialAugment (Müller & Hutter, 2021) simplifies even further: sample one operation at random and sample its magnitude uniformly from the full range — zero hyperparameters to tune, often competitive with RandAugment.

## AugMix and Robustness

AugMix (Hendrycks et al., 2020) is designed specifically to improve robustness to distribution shift, not just clean accuracy. It generates multiple augmented versions of each image using different randomly sampled augmentation chains, then mixes them with the original image using Dirichlet-sampled weights. A Jensen-Shannon consistency loss encourages the model to make consistent predictions across all augmented versions. AugMix improves performance on ImageNet-C (corrupted ImageNet) by 12–15% while maintaining clean accuracy. It is the preferred augmentation when robustness to real-world distribution shift (blur, noise, compression artifacts) matters.

## Augmentation Method Comparison

| Method | Label Mixing | Detection Safe | Training Overhead | Calibration (ECE) | Corruption Robustness |
| --- | --- | --- | --- | --- | --- |
| Basic (flip + crop) | No | Yes | None | Poor | Low |
| Cutout | No | Partial | Minimal | Moderate | Moderate |
| MixUp (α=0.4) | Yes — linear blend | No | Minimal | Good | Moderate |
| CutMix (α=1.0) | Yes — area-weighted | Yes | Minimal | Good | Good |
| RandAugment (N=2,M=9) | No | Yes | Low (2 extra augments) | Moderate | High |
| AugMix | No (JS consistency loss) | Yes | Medium (3x forward) | Best | Highest |

## Choosing an Augmentation Strategy

The choice of augmentation should be guided by the task and deployment context. For standard ImageNet classification, RandAugment(N=2, M=9) with CutMix is the current default in most SOTA training recipes (timm library uses this by default). For object detection and segmentation, use CutMix over MixUp and avoid augmentations that blend object boundaries (no MixUp on bounding boxes). For models that will be deployed on corrupted or out-of-distribution data (medical devices, autonomous vehicles, cameras in variable conditions), AugMix with the Jensen-Shannon consistency loss provides the best robustness. For tiny datasets (<1000 images), aggressive standard augmentation (heavy crop, flip, color jitter, rotation) is more beneficial than MixUp/CutMix, which require sufficient class coverage within each batch.

- Standard baseline: RandomResizedCrop(224) + HorizontalFlip(0.5) + ColorJitter + Normalize.
- MixUp: blend two images and labels; λ~Beta(α,α); prevents overconfidence; improves ECE.
- CutMix: paste rectangular patch; label ∝ area; detection-safe (no blending artifacts).
- RandAugment: N ops from pool of 14, magnitude M; only 2 hyperparams; default N=2, M=9.
- TrivialAugment: 1 random op, random magnitude; zero hyperparams; competitive with RandAugment.
- AugMix: consistency loss over augmentation chains; best for robustness to distribution shift.

