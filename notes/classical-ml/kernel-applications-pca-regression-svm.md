---
title: "Kernel PCA, Kernel Ridge Regression, and Kernel SVM"
slug: "kernel-applications-pca-regression-svm"
description: "How to kernelize classical linear methods using the dual formulation: kernel ridge regression, kernel PCA, and kernel SVM. Covers the kernelization recipe, O(n²) memory bottlenecks, and Nyström approximation for large-scale kernel methods."
tags: ["kernel-methods", "gaussian-processes", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtlcm5lbCB0cmljayBlbmFibGVzIGFueSBhbGdvcml0aG0gdGhhdCBjYW4gYmUgd3JpdHRlbiBpbiB0ZXJtcyBvZiBkb3QgcHJvZHVjdHMgdG8gb3BlcmF0ZSBpbiBhbiBpbmZpbml0ZS1kaW1lbnNpb25hbCBmZWF0dXJlIHNwYWNlIGF0IHRoZSBjb3N0IG9mIG9ubHkgbsOXbiBrZXJuZWwgbWF0cml4IGNvbXB1dGF0aW9ucy4gVGhpcyBzZWN0aW9uIGNvdmVycyB0aHJlZSBjYW5vbmljYWwga2VybmVsaXplZCBhbGdvcml0aG1zIOKAlCBrZXJuZWwgcmlkZ2UgcmVncmVzc2lvbiAoS1JSKSwga2VybmVsIFBDQSwgYW5kIGtlcm5lbCBTVk0g4oCUIGFuZCBleHBsYWlucyB0aGUgc2hhcmVkIGtlcm5lbGl6YXRpb24gcmVjaXBlIHRoYXQgdW5kZXJsaWVzIGFsbCBvZiB0aGVtLiBUaGUgbWFpbiBwcmFjdGljYWwgYm90dGxlbmVjayBpcyB0aGUgTyhuwrIpIG1lbW9yeSBmb3Igc3RvcmluZyB0aGUga2VybmVsIG1hdHJpeCwgYWRkcmVzc2VkIGJ5IHRoZSBOeXN0csO2bSBhcHByb3hpbWF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBLZXJuZWxpemF0aW9uIFJlY2lwZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXZlcnkgbGluZWFyIGFsZ29yaXRobSB0aGF0IG9wZXJhdGVzIG9uIGlubmVyIHByb2R1Y3RzIGNhbiBiZSBrZXJuZWxpemVkIGluIHRocmVlIHN0ZXBzOiAoMSkgZGVyaXZlIHRoZSBkdWFsIGZvcm11bGF0aW9uIGluIHRlcm1zIG9mIOKfqHjhtaIsIHjisbzin6k7ICgyKSByZXBsYWNlIGV2ZXJ5IGlubmVyIHByb2R1Y3Qg4p+oeOG1oiwgeOKxvOKfqSB3aXRoIGsoeOG1oiwgeOKxvCk7ICgzKSBzb2x2ZSB0aGUgZHVhbCBwcm9ibGVtIGluIHRlcm1zIG9mIHRoZSBrZXJuZWwgbWF0cml4IEsuIFRoZSByZXN1bHRpbmcgYWxnb3JpdGhtIGltcGxpY2l0bHkgb3BlcmF0ZXMgaW4gdGhlIGZlYXR1cmUgc3BhY2UgZGVmaW5lZCBieSBrIOKAlCB3aGljaCBjYW4gYmUgaW5maW5pdGUtZGltZW5zaW9uYWwg4oCUIHdoaWxlIHRoZSBjb21wdXRhdGlvbiBvbmx5IHJlcXVpcmVzIGV2YWx1YXRpbmcgbsKyIGtlcm5lbCB2YWx1ZXMuIFRoaXMgaXMgdGhlIGtlcm5lbCB0cmljay4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6IlxcbGFuZ2xlIFxccGhpKHhfaSksIFxccGhpKHhfaikgXFxyYW5nbGVfe0hfa30gPSBrKHhfaSwgeF9qKSBcXHF1YWQgXFxSaWdodGFycm93IFxccXVhZCBcXHRleHR7cmVwbGFjZSB9IHhfaV5cXHRvcCB4X2ogXFxtYXBzdG8gayh4X2ksIHhfaikgXFx0ZXh0eyBpbiBkdWFsfSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2h5IHRoZSBLZXJuZWwgVHJpY2sgSXMgUG93ZXJmdWwiLCJjb250ZW50IjoiVGhlIFJCRiBrZXJuZWwgY29ycmVzcG9uZHMgdG8gYW4gaW5maW5pdGUtZGltZW5zaW9uYWwgZmVhdHVyZSBtYXAsIHlldCBjb21wdXRpbmcgayh4LCB6KSA9IGV4cCjiiJLigJZ44oiSeuKAlsKyLzLihJPCsikgY29zdHMgb25seSBPKGQpIG9wZXJhdGlvbnMgKGQgPSBpbnB1dCBkaW1lbnNpb24pLiBXaXRob3V0IHRoZSBrZXJuZWwgdHJpY2ssIHdvcmtpbmcgd2l0aCB0aGUgaW5maW5pdGUtZGltZW5zaW9uYWwgZmVhdHVyZSBtYXAgd291bGQgYmUgaW1wb3NzaWJsZS4gV2l0aCBpdCwgeW91IGdldCB0aGUgZXhwcmVzc2l2ZSBwb3dlciBvZiBhbiBpbmZpbml0ZSBmZWF0dXJlIHNwYWNlIGF0IE8oZCkgY29zdCBwZXIga2VybmVsIGV2YWx1YXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2VybmVsIFJpZGdlIFJlZ3Jlc3Npb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJpZGdlIHJlZ3Jlc3Npb24gaW4gcHJpbWFsIGZvcm0gc29sdmVzIG1pbncg4oCWWHfiiJJ54oCWwrIgKyDOu+KAlnfigJbCsi4gVXNpbmcgdGhlIHJlcHJlc2VudGVyIHRoZW9yZW0sIHRoZSBkdWFsIGZvcm0gaXM6IGZpbmQgzrEgc3VjaCB0aGF0IGYqKHgpID0gzqPhtaIgzrHhtaIgayh44bWiLCB4KS4gU3Vic3RpdHV0aW5nIGludG8gdGhlIG9iamVjdGl2ZSBhbmQgZGlmZmVyZW50aWF0aW5nIGdpdmVzIM6xID0gKEsrzrtJKeKBu8K5eS4gUHJlZGljdGlvbiBhdCBuZXcgeCogcmVxdWlyZXMgY29tcHV0aW5nIGsoeOG1oiwgeCopIGZvciBhbGwgdHJhaW5pbmcgcG9pbnRzOiDFtyogPSBrKuG1gM6xIHdoZXJlIChrKinhtaIgPSBrKHjhtaIsIHgqKS4gVHJhaW5pbmcgY29zdCBpcyBPKG7CsykgZm9yIHRoZSBtYXRyaXggc29sdmU7IHByZWRpY3Rpb24gaXMgTyhuKSBrZXJuZWwgZXZhbHVhdGlvbnMgcGVyIHRlc3QgcG9pbnQuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJcXGJvbGRzeW1ib2x7XFxhbHBoYX0gPSAoSyArIFxcbGFtYmRhIEkpXnstMX1cXG1hdGhiZnt5fSwgXFxxcXVhZCBcXGhhdHt5fSh4XiopID0gXFxtYXRoYmZ7a31fKl5cXHRvcCBcXGJvbGRzeW1ib2x7XFxhbHBoYX0sIFxccXVhZCAoXFxtYXRoYmZ7a31fKilfaSA9IGsoeF9pLCB4XiopIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2VybmVsIFBDQSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgUENBIGZpbmRzIGEgbGluZWFyIHN1YnNwYWNlIG9mIG1heGltdW0gdmFyaWFuY2UuIEtlcm5lbCBQQ0EgYXBwbGllcyBQQ0EgaW4gdGhlIFJLSFMgZmVhdHVyZSBzcGFjZSDPhih4KSwgZW5hYmxpbmcgbm9ubGluZWFyIGRpbWVuc2lvbmFsaXR5IHJlZHVjdGlvbi4gVGhlIGFsZ29yaXRobTogKDEpIGNlbnRlciB0aGUga2VybmVsIG1hdHJpeCBLzIMgPSBLIOKIkiAx4oKZS+G1gCDiiJIgSzHigpkgKyAx4oKZSzHigpnhtYA7ICgyKSBlaWdlbmRlY29tcG9zZSBLzIMgPSBVzptV4bWAOyAoMykgcHJvamVjdCBuZXcgcG9pbnRzIHVzaW5nIHRoZSBlaWdlbnZlY3RvcnMuIFRoZSByZXN1bHRpbmcgY29tcG9uZW50cyBjYXB0dXJlIG5vbmxpbmVhciBzdHJ1Y3R1cmUgaW4gdGhlIGRhdGEg4oCUIGZvciBleGFtcGxlLCBrZXJuZWwgUENBIHdpdGggYW4gUkJGIGtlcm5lbCBjYW4gdW5mb2xkIGEgU3dpc3Mgcm9sbCBvciBzZXBhcmF0ZSBjb25jZW50cmljIHJpbmdzIHRoYXQgbGluZWFyIFBDQSBjYW5ub3QuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2VybmVsIFNWTSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFNWTSBkdWFsIG1heGltaXplcyDOo+G1oiDOseG1oiDiiJIgwr0gzqPhtaLisbwgzrHhtaLOseKxvHnhtaJ54rG8IGsoeOG1oix44rG8KSBzdWJqZWN0IHRvIDAg4omkIM6x4bWiIOKJpCBDIGFuZCDOo+G1oiDOseG1onnhtaIgPSAwLiBQb2ludHMgd2l0aCDOseG1oiBcdTAwM2UgMCBhcmUgc3VwcG9ydCB2ZWN0b3JzLiBUaGUgZGVjaXNpb24gZnVuY3Rpb24gZih4KSA9IM6j4bWiIM6x4bWieeG1omsoeOG1oix4KSArIGIgb25seSBpbnZvbHZlcyB0aGUgc3VwcG9ydCB2ZWN0b3JzIChvZnRlbiBzcGFyc2UpLiBLZXJuZWwgU1ZNIHJlcXVpcmVzIHNvbHZpbmcgYW4gbsOXbiBRUCBidXQgdGhlIHNwYXJzaXR5IG9mIHRoZSBzb2x1dGlvbiBtZWFucyBwcmVkaWN0aW9uIHVzZXMgZmFyIGZld2VyIHRoYW4gbiBrZXJuZWwgZXZhbHVhdGlvbnMuIFRoZSBDIHBhcmFtZXRlciB0cmFkZXMgb2ZmIG1hcmdpbiB3aWR0aCBhZ2FpbnN0IHRyYWluaW5nIGVycm9yLiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50IjoiZih4KSA9IFxcc3VtX3tpIFxcaW4gU1Z9IFxcYWxwaGFfaSB5X2lcXCwgayh4X2ksIHgpICsgYiwgXFxxdWFkIFxcYWxwaGFfaSBcdTAwM2UgMCBcXHRleHR7IG9ubHkgZm9yIHN1cHBvcnQgdmVjdG9yc30ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wdXRhdGlvbmFsIEJvdHRsZW5lY2tzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGwgZXhhY3Qga2VybmVsIG1ldGhvZHMgc2hhcmUgdGhlIHNhbWUgTyhuwrIpIG1lbW9yeSBib3R0bGVuZWNrOiBzdG9yaW5nIHRoZSBmdWxsIG7Dl24ga2VybmVsIG1hdHJpeC4gRm9yIG49MTAsMDAwIHBvaW50cyB3aXRoIGZsb2F0NjQsIHRoaXMgaXMgODAwIE1COyBmb3Igbj0xMDAsMDAwIGl0IGlzIDgwIEdCIOKAlCBpbmZlYXNpYmxlIG9uIGEgc2luZ2xlIG1hY2hpbmUuIFRyYWluaW5nIGNvc3RzIHJhbmdlIGZyb20gTyhuwrLCt2QpIGZvciBrZXJuZWwgZXZhbHVhdGlvbiB0byBPKG7CsykgZm9yIG1hdHJpeCBzb2x2ZXMgYW5kIGVpZ2VuZGVjb21wb3NpdGlvbnMuIFRoZXNlIGNvc3RzIG1ha2UgZXhhY3Qga2VybmVsIG1ldGhvZHMgc3VpdGFibGUgZm9yIG4gdXAgdG8gfjIwLDAwMCBwb2ludHMgYW5kIG1vdGl2YXRlIGFwcHJveGltYXRpb24gbWV0aG9kcyBmb3IgbGFyZ2VyIGRhdGFzZXRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik55c3Ryw7ZtIEFwcHJveGltYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBOeXN0csO2bSBtZXRob2QgYXBwcm94aW1hdGVzIHRoZSBmdWxsIGtlcm5lbCBtYXRyaXggSyDiiYggS197bm19IEtfe21tfeKBu8K5IEtfe21ufSB1c2luZyBvbmx5IG0g4omqIG4gbGFuZG1hcmsgcG9pbnRzLiBUaGUgbGFuZG1hcmtzIGFyZSBzZWxlY3RlZCByYW5kb21seSBvciBieSBncmVlZHkgc2VsZWN0aW9uLiBUaGlzIHJlZHVjZXMgbWVtb3J5IGZyb20gTyhuwrIpIHRvIE8obm0pIGFuZCB0cmFpbmluZyBjb3N0IGZyb20gTyhuwrMpIHRvIE8obm3CsikuIFRoZSBhcHByb3hpbWF0ZWQga2VybmVsIGZlYXR1cmVzIGNhbiB0aGVuIGJlIGZlZCB0byBhbnkgbGluZWFyIG1vZGVsLiBOeXN0csO2bSBwcm92aWRlcyBhIHByaW5jaXBsZWQgbG93LXJhbmsgYXBwcm94aW1hdGlvbiB3aXRoIGEgY29udmVyZ2VuY2UgZ3VhcmFudGVlOiDigJZLIOKIkiBLzIPigJYg4oaSIDAgYXMgbSDihpIgbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIEV4YW1wbGVzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmtlcm5lbF9yaWRnZSBpbXBvcnQgS2VybmVsUmlkZ2VcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9yZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBtZWFuX3NxdWFyZWRfZXJyb3JcblxuZGVmIHJiZl9ncmFtKFgxLCBYMiwgZ2FtbWE9MS4wKTpcbiAgICBkaWZmID0gWDFbOiwgTm9uZSwgOl0gLSBYMltOb25lLCA6LCA6XVxuICAgIHJldHVybiBucC5leHAoLWdhbW1hICogbnAuc3VtKGRpZmYqKjIsIGF4aXM9LTEpKVxuXG5kZWYga3JyX2Zyb21fc2NyYXRjaChYX3RyYWluLCB5X3RyYWluLCBYX3Rlc3QsIGdhbW1hPTEuMCwgbGFtPTAuMSk6XG4gICAgS190cmFpbiA9IHJiZl9ncmFtKFhfdHJhaW4sIFhfdHJhaW4sIGdhbW1hKVxuICAgIGFscGhhID0gbnAubGluYWxnLnNvbHZlKEtfdHJhaW4gKyBsYW0gKiBucC5leWUobGVuKHlfdHJhaW4pKSwgeV90cmFpbilcbiAgICBLX3Rlc3QgPSByYmZfZ3JhbShYX3Rlc3QsIFhfdHJhaW4sIGdhbW1hKVxuICAgIHJldHVybiBLX3Rlc3QgQCBhbHBoYVxuXG5YLCB5ID0gbWFrZV9yZWdyZXNzaW9uKG5fc2FtcGxlcz0yMDAsIG5fZmVhdHVyZXM9MTAsIG5vaXNlPTAuNSwgcmFuZG9tX3N0YXRlPTApXG5zYyA9IFN0YW5kYXJkU2NhbGVyKClcblggPSBzYy5maXRfdHJhbnNmb3JtKFgpXG5YX3RyLCBYX3RlID0gWFs6MTUwXSwgWFsxNTA6XVxueV90ciwgeV90ZSA9IHlbOjE1MF0sIHlbMTUwOl1cblxueV9zY3JhdGNoID0ga3JyX2Zyb21fc2NyYXRjaChYX3RyLCB5X3RyLCBYX3RlLCBnYW1tYT0wLjUsIGxhbT0wLjEpXG5rcnIgPSBLZXJuZWxSaWRnZShrZXJuZWw9XHUwMDI3cmJmXHUwMDI3LCBhbHBoYT0wLjEsIGdhbW1hPTAuNSlcbmtyci5maXQoWF90ciwgeV90cilcbnlfc2tsZWFybiA9IGtyci5wcmVkaWN0KFhfdGUpXG5cbnByaW50KGZcdTAwMjdGcm9tLXNjcmF0Y2ggS1JSIE1TRToge21lYW5fc3F1YXJlZF9lcnJvcih5X3RlLCB5X3NjcmF0Y2gpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3c2tsZWFybiBLUlIgICAgICBNU0U6IHttZWFuX3NxdWFyZWRfZXJyb3IoeV90ZSwgeV9za2xlYXJuKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01heCBkaWZmOiB7bnAuYWJzKHlfc2NyYXRjaCAtIHlfc2tsZWFybikubWF4KCk6LjJlfVx1MDAyNykifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2Vfc3dpc3Nfcm9sbFxuZnJvbSBza2xlYXJuLmRlY29tcG9zaXRpb24gaW1wb3J0IEtlcm5lbFBDQSwgUENBXG5cblgsIGNvbG9yID0gbWFrZV9zd2lzc19yb2xsKG5fc2FtcGxlcz0xMDAwLCBub2lzZT0wLjEsIHJhbmRvbV9zdGF0ZT00MilcblxucGNhID0gUENBKG5fY29tcG9uZW50cz0yKVxuWF9wY2EgPSBwY2EuZml0X3RyYW5zZm9ybShYKVxuXG5rcGNhID0gS2VybmVsUENBKG5fY29tcG9uZW50cz0yLCBrZXJuZWw9XHUwMDI3cmJmXHUwMDI3LCBnYW1tYT0wLjA0KVxuWF9rcGNhID0ga3BjYS5maXRfdHJhbnNmb3JtKFgpXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAzLCBmaWdzaXplPSgxNSwgNCkpXG5heGVzWzBdLnNjYXR0ZXIoWFs6LCAwXSwgWFs6LCAyXSwgYz1jb2xvciwgY21hcD1cdTAwMjdyYWluYm93XHUwMDI3LCBzPTUpXG5heGVzWzBdLnNldF90aXRsZShcdTAwMjdPcmlnaW5hbCBTd2lzcyBSb2xsICh4LXogdmlldylcdTAwMjcpXG5cbmF4ZXNbMV0uc2NhdHRlcihYX3BjYVs6LCAwXSwgWF9wY2FbOiwgMV0sIGM9Y29sb3IsIGNtYXA9XHUwMDI3cmFpbmJvd1x1MDAyNywgcz01KVxuYXhlc1sxXS5zZXRfdGl0bGUoXHUwMDI3TGluZWFyIFBDQSAoZmFpbHMgdG8gdW5mb2xkKVx1MDAyNylcblxuYXhlc1syXS5zY2F0dGVyKFhfa3BjYVs6LCAwXSwgWF9rcGNhWzosIDFdLCBjPWNvbG9yLCBjbWFwPVx1MDAyN3JhaW5ib3dcdTAwMjcsIHM9NSlcbmF4ZXNbMl0uc2V0X3RpdGxlKFx1MDAyN0tlcm5lbCBQQ0EgUkJGICh1bmZvbGRzIG1hbmlmb2xkKVx1MDAyNylcblxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdrZXJuZWxfcGNhLnBuZ1x1MDAyNywgZHBpPTEwMClcbnByaW50KFx1MDAyN1NhdmVkIGtlcm5lbF9wY2EucG5nXHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5zdm0gaW1wb3J0IFNWQ1xuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFjY3VyYWN5X3Njb3JlXG5cbiMgWE9SIGRhdGFzZXQ6IG5vdCBsaW5lYXJseSBzZXBhcmFibGVcbnJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZSg0MilcblhfcG9zID0gbnAudnN0YWNrKFtybmcucmFuZG4oNTAsIDIpICsgWzEsIDFdLCBybmcucmFuZG4oNTAsIDIpICsgWy0xLCAtMV1dKVxuWF9uZWcgPSBucC52c3RhY2soW3JuZy5yYW5kbig1MCwgMikgKyBbMSwgLTFdLCBybmcucmFuZG4oNTAsIDIpICsgWy0xLCAgMV1dKVxuWCA9IG5wLnZzdGFjayhbWF9wb3MsIFhfbmVnXSlcbnkgPSBucC5oc3RhY2soW25wLm9uZXMoMTAwKSwgLW5wLm9uZXMoMTAwKV0pXG5cbmtlcm5lbHMgPSB7XHUwMDI3bGluZWFyXHUwMDI3OiB7fSwgXHUwMDI3cG9seVx1MDAyNzoge1x1MDAyN2RlZ3JlZVx1MDAyNzogMywgXHUwMDI3Y29lZjBcdTAwMjc6IDF9LCBcdTAwMjdyYmZcdTAwMjc6IHtcdTAwMjdnYW1tYVx1MDAyNzogMC41fX1cbnJlc3VsdHMgPSB7fVxuZm9yIG5hbWUsIGt3YXJncyBpbiBrZXJuZWxzLml0ZW1zKCk6XG4gICAgY2xmID0gU1ZDKGtlcm5lbD1uYW1lLCBDPTEuMCwgKiprd2FyZ3MpXG4gICAgY2xmLmZpdChYLCB5KVxuICAgIGFjYyA9IGFjY3VyYWN5X3Njb3JlKHksIGNsZi5wcmVkaWN0KFgpKVxuICAgIHJlc3VsdHNbbmFtZV0gPSAoY2xmLCBhY2MpXG4gICAgcHJpbnQoZlx1MDAyN2tlcm5lbD17bmFtZX06IGFjY3VyYWN5PXthY2M6LjNmfVx1MDAyNylcblxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDEsIDMsIGZpZ3NpemU9KDE0LCA0KSlcbnh4LCB5eSA9IG5wLm1lc2hncmlkKG5wLmxpbnNwYWNlKC00LCA0LCAyMDApLCBucC5saW5zcGFjZSgtNCwgNCwgMjAwKSlcbmZvciBheCwgKG5hbWUsIChjbGYsIGFjYykpIGluIHppcChheGVzLCByZXN1bHRzLml0ZW1zKCkpOlxuICAgIFogPSBjbGYucHJlZGljdChucC5jX1t4eC5yYXZlbCgpLCB5eS5yYXZlbCgpXSkucmVzaGFwZSh4eC5zaGFwZSlcbiAgICBheC5jb250b3VyZih4eCwgeXksIFosIGFscGhhPTAuMylcbiAgICBheC5zY2F0dGVyKFhbOiwgMF0sIFhbOiwgMV0sIGM9eSwgY21hcD1cdTAwMjdid3JcdTAwMjcsIHM9MTApXG4gICAgYXguc2V0X3RpdGxlKGZcdTAwMjd7bmFtZX0gKGFjYz17YWNjOi4yZn0pXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdrZXJuZWxfc3ZtX3hvci5wbmdcdTAwMjcsIGRwaT0xMDApIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmtlcm5lbF9hcHByb3hpbWF0aW9uIGltcG9ydCBOeXN0cm9lbVxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUmlkZ2VcbmZyb20gc2tsZWFybi5waXBlbGluZSBpbXBvcnQgbWFrZV9waXBlbGluZVxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IG1lYW5fc3F1YXJlZF9lcnJvclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX3JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuaW1wb3J0IHRpbWVcblxuWCwgeSA9IG1ha2VfcmVncmVzc2lvbihuX3NhbXBsZXM9MjAwMCwgbl9mZWF0dXJlcz0yMCwgbm9pc2U9MC41LCByYW5kb21fc3RhdGU9MClcbnNjID0gU3RhbmRhcmRTY2FsZXIoKVxuWCA9IHNjLmZpdF90cmFuc2Zvcm0oWClcblhfdHIsIFhfdGUgPSBYWzoxNTAwXSwgWFsxNTAwOl1cbnlfdHIsIHlfdGUgPSB5WzoxNTAwXSwgeVsxNTAwOl1cblxucHJpbnQoZlx1MDAyN3tcIm5fY29tcG9uZW50c1wiOlx1MDAzYzE0fSB7XCJNU0VcIjpcdTAwM2MxMH0ge1wiVGltZSAocylcIjpcdTAwM2MxMH1cdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogMzYpXG5mb3Igbl9jb21wIGluIFs1MCwgMTAwLCAyMDAsIDUwMF06XG4gICAgdDAgPSB0aW1lLnRpbWUoKVxuICAgIHBpcGUgPSBtYWtlX3BpcGVsaW5lKFxuICAgICAgICBOeXN0cm9lbShrZXJuZWw9XHUwMDI3cmJmXHUwMDI3LCBnYW1tYT0wLjUsIG5fY29tcG9uZW50cz1uX2NvbXAsIHJhbmRvbV9zdGF0ZT0wKSxcbiAgICAgICAgUmlkZ2UoYWxwaGE9MS4wKVxuICAgIClcbiAgICBwaXBlLmZpdChYX3RyLCB5X3RyKVxuICAgIG1zZSA9IG1lYW5fc3F1YXJlZF9lcnJvcih5X3RlLCBwaXBlLnByZWRpY3QoWF90ZSkpXG4gICAgZWxhcHNlZCA9IHRpbWUudGltZSgpIC0gdDBcbiAgICBwcmludChmXHUwMDI3e25fY29tcDpcdTAwM2MxNH0ge21zZTpcdTAwM2MxMC40Zn0ge2VsYXBzZWQ6XHUwMDNjMTAuM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0V4YWN0IGtlcm5lbCBtYXRyaXg6IHsxNTAwKioyICogOCAvIDFlNjouMGZ9IE1CIHZzIE55c3Ryb2VtKG09MjAwKTogezE1MDAqMjAwKjgvMWU2Oi4xZn0gTUJcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWV0aG9kIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiRHVhbCBGb3JtIiwiVHJhaW5pbmcgQ29zdCIsIlByZWRpY3Rpb24gQ29zdCIsIkJlc3QgRm9yIl0sInJvd3MiOltbIktlcm5lbCBSaWRnZSBSZWdyZXNzaW9uIiwizrEgPSAoSyvOu0kp4oG7wrl5IiwiTyhuwrMpIG1hdHJpeCBzb2x2ZSIsIk8obsK3ZCkga2VybmVsIGV2YWxzIHBlciBwb2ludCIsIlNtYWxsLW4gc21vb3RoIHJlZ3Jlc3Npb24iXSxbIktlcm5lbCBQQ0EiLCJFaWdlbmRlY29tcG9zZSBjZW50ZXJlZCBLIiwiTyhuwrMpIGVpZ2VuZGVjb21wIiwiTyhuwrdwKSBwcm9qZWN0aW9ucyBwZXIgcG9pbnQiLCJOb25saW5lYXIgZGltZW5zaW9uYWxpdHkgcmVkdWN0aW9uIl0sWyJLZXJuZWwgU1ZNIiwiUVAgb3ZlciDOsSB3aXRoIGJveCBjb25zdHJhaW50cyIsIk8obsKyKSB0byBPKG7CsykgUVAiLCJPKG5fc3bCt2QpIGtlcm5lbCBldmFscyAoc3BhcnNlKSIsIkNsYXNzaWZpY2F0aW9uIHdpdGggbWFyZ2luIl0sWyJOeXN0csO2bSBBcHByb3guIiwiSyDiiYggS197bm19S197bW194oG7wrlLX3ttbn0iLCJPKG5twrIpIHdpdGggbeKJqm4iLCJPKG0pIGZlYXR1cmUgdmVjdG9yLCBPKDEpIG1vZGVsIiwiTGFyZ2Utc2NhbGUga2VybmVsIG1ldGhvZHMgblx1MDAzZTEwayJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGwgdGhyZWUgbWV0aG9kcyBzaGFyZSB0aGUgc2FtZSBrZXJuZWwgbWF0cml4IGJvdHRsZW5lY2suIEZvciBuIOKJpCA1LDAwMCB1c2UgZXhhY3QgbWV0aG9kczsgZm9yIGxhcmdlciBuIHVzZSBOeXN0csO2bSBhcHByb3hpbWF0aW9uIG9yIHJhbmRvbSBGb3VyaWVyIGZlYXR1cmVzIChSYWhpbWkgXHUwMDI2IFJlY2h0LCAyMDA3KS4gVGhlIGNob2ljZSBiZXR3ZWVuIEtSUiwga1BDQSwgYW5kIGtTVk0gZGVwZW5kcyBvbiB0aGUgdGFzazogcmVncmVzc2lvbiwgZGltZW5zaW9uYWxpdHkgcmVkdWN0aW9uLCBvciBjbGFzc2lmaWNhdGlvbi4ifV0="
---
# Kernel PCA, Kernel Ridge Regression, and Kernel SVM

The kernel trick enables any algorithm that can be written in terms of dot products to operate in an infinite-dimensional feature space at the cost of only n×n kernel matrix computations. This section covers three canonical kernelized algorithms — kernel ridge regression (KRR), kernel PCA, and kernel SVM — and explains the shared kernelization recipe that underlies all of them. The main practical bottleneck is the O(n²) memory for storing the kernel matrix, addressed by the Nyström approximation.

## The Kernelization Recipe

Every linear algorithm that operates on inner products can be kernelized in three steps: (1) derive the dual formulation in terms of ⟨xᵢ, xⱼ⟩; (2) replace every inner product ⟨xᵢ, xⱼ⟩ with k(xᵢ, xⱼ); (3) solve the dual problem in terms of the kernel matrix K. The resulting algorithm implicitly operates in the feature space defined by k — which can be infinite-dimensional — while the computation only requires evaluating n² kernel values. This is the kernel trick.

$$\langle \phi(x_i), \phi(x_j) \rangle_{H_k} = k(x_i, x_j) \quad \Rightarrow \quad \text{replace } x_i^\top x_j \mapsto k(x_i, x_j) \text{ in dual}$$

> **Why the Kernel Trick Is Powerful**: The RBF kernel corresponds to an infinite-dimensional feature map, yet computing k(x, z) = exp(−‖x−z‖²/2ℓ²) costs only O(d) operations (d = input dimension). Without the kernel trick, working with the infinite-dimensional feature map would be impossible. With it, you get the expressive power of an infinite feature space at O(d) cost per kernel evaluation.

## Kernel Ridge Regression

Ridge regression in primal form solves minw ‖Xw−y‖² + λ‖w‖². Using the representer theorem, the dual form is: find α such that f*(x) = Σᵢ αᵢ k(xᵢ, x). Substituting into the objective and differentiating gives α = (K+λI)⁻¹y. Prediction at new x* requires computing k(xᵢ, x*) for all training points: ŷ* = k*ᵀα where (k*)ᵢ = k(xᵢ, x*). Training cost is O(n³) for the matrix solve; prediction is O(n) kernel evaluations per test point.

$$\boldsymbol{\alpha} = (K + \lambda I)^{-1}\mathbf{y}, \qquad \hat{y}(x^*) = \mathbf{k}_*^\top \boldsymbol{\alpha}, \quad (\mathbf{k}_*)_i = k(x_i, x^*)$$

## Kernel PCA

Standard PCA finds a linear subspace of maximum variance. Kernel PCA applies PCA in the RKHS feature space φ(x), enabling nonlinear dimensionality reduction. The algorithm: (1) center the kernel matrix K̃ = K − 1ₙKᵀ − K1ₙ + 1ₙK1ₙᵀ; (2) eigendecompose K̃ = UΛUᵀ; (3) project new points using the eigenvectors. The resulting components capture nonlinear structure in the data — for example, kernel PCA with an RBF kernel can unfold a Swiss roll or separate concentric rings that linear PCA cannot.

## Kernel SVM

The SVM dual maximizes Σᵢ αᵢ − ½ Σᵢⱼ αᵢαⱼyᵢyⱼ k(xᵢ,xⱼ) subject to 0 ≤ αᵢ ≤ C and Σᵢ αᵢyᵢ = 0. Points with αᵢ > 0 are support vectors. The decision function f(x) = Σᵢ αᵢyᵢk(xᵢ,x) + b only involves the support vectors (often sparse). Kernel SVM requires solving an n×n QP but the sparsity of the solution means prediction uses far fewer than n kernel evaluations. The C parameter trades off margin width against training error.

$$f(x) = \sum_{i \in SV} \alpha_i y_i\, k(x_i, x) + b, \quad \alpha_i > 0 \text{ only for support vectors}$$

## Computational Bottlenecks

All exact kernel methods share the same O(n²) memory bottleneck: storing the full n×n kernel matrix. For n=10,000 points with float64, this is 800 MB; for n=100,000 it is 80 GB — infeasible on a single machine. Training costs range from O(n²·d) for kernel evaluation to O(n³) for matrix solves and eigendecompositions. These costs make exact kernel methods suitable for n up to ~20,000 points and motivate approximation methods for larger datasets.

## Nyström Approximation

The Nyström method approximates the full kernel matrix K ≈ K_{nm} K_{mm}⁻¹ K_{mn} using only m ≪ n landmark points. The landmarks are selected randomly or by greedy selection. This reduces memory from O(n²) to O(nm) and training cost from O(n³) to O(nm²). The approximated kernel features can then be fed to any linear model. Nyström provides a principled low-rank approximation with a convergence guarantee: ‖K − K̃‖ → 0 as m → n.

## Code Examples

```python
import numpy as np
from sklearn.kernel_ridge import KernelRidge
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def rbf_gram(X1, X2, gamma=1.0):
    diff = X1[:, None, :] - X2[None, :, :]
    return np.exp(-gamma * np.sum(diff**2, axis=-1))

def krr_from_scratch(X_train, y_train, X_test, gamma=1.0, lam=0.1):
    K_train = rbf_gram(X_train, X_train, gamma)
    alpha = np.linalg.solve(K_train + lam * np.eye(len(y_train)), y_train)
    K_test = rbf_gram(X_test, X_train, gamma)
    return K_test @ alpha

X, y = make_regression(n_samples=200, n_features=10, noise=0.5, random_state=0)
sc = StandardScaler()
X = sc.fit_transform(X)
X_tr, X_te = X[:150], X[150:]
y_tr, y_te = y[:150], y[150:]

y_scratch = krr_from_scratch(X_tr, y_tr, X_te, gamma=0.5, lam=0.1)
krr = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.5)
krr.fit(X_tr, y_tr)
y_sklearn = krr.predict(X_te)

print(f'From-scratch KRR MSE: {mean_squared_error(y_te, y_scratch):.4f}')
print(f'sklearn KRR      MSE: {mean_squared_error(y_te, y_sklearn):.4f}')
print(f'Max diff: {np.abs(y_scratch - y_sklearn).max():.2e}')
```

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_swiss_roll
from sklearn.decomposition import KernelPCA, PCA

X, color = make_swiss_roll(n_samples=1000, noise=0.1, random_state=42)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

kpca = KernelPCA(n_components=2, kernel='rbf', gamma=0.04)
X_kpca = kpca.fit_transform(X)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].scatter(X[:, 0], X[:, 2], c=color, cmap='rainbow', s=5)
axes[0].set_title('Original Swiss Roll (x-z view)')

axes[1].scatter(X_pca[:, 0], X_pca[:, 1], c=color, cmap='rainbow', s=5)
axes[1].set_title('Linear PCA (fails to unfold)')

axes[2].scatter(X_kpca[:, 0], X_kpca[:, 1], c=color, cmap='rainbow', s=5)
axes[2].set_title('Kernel PCA RBF (unfolds manifold)')

plt.tight_layout()
plt.savefig('kernel_pca.png', dpi=100)
print('Saved kernel_pca.png')
```

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# XOR dataset: not linearly separable
rng = np.random.RandomState(42)
X_pos = np.vstack([rng.randn(50, 2) + [1, 1], rng.randn(50, 2) + [-1, -1]])
X_neg = np.vstack([rng.randn(50, 2) + [1, -1], rng.randn(50, 2) + [-1,  1]])
X = np.vstack([X_pos, X_neg])
y = np.hstack([np.ones(100), -np.ones(100)])

kernels = {'linear': {}, 'poly': {'degree': 3, 'coef0': 1}, 'rbf': {'gamma': 0.5}}
results = {}
for name, kwargs in kernels.items():
    clf = SVC(kernel=name, C=1.0, **kwargs)
    clf.fit(X, y)
    acc = accuracy_score(y, clf.predict(X))
    results[name] = (clf, acc)
    print(f'kernel={name}: accuracy={acc:.3f}')

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
xx, yy = np.meshgrid(np.linspace(-4, 4, 200), np.linspace(-4, 4, 200))
for ax, (name, (clf, acc)) in zip(axes, results.items()):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3)
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', s=10)
    ax.set_title(f'{name} (acc={acc:.2f})')
plt.tight_layout()
plt.savefig('kernel_svm_xor.png', dpi=100)
```

```python
import numpy as np
from sklearn.kernel_approximation import Nystroem
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
import time

X, y = make_regression(n_samples=2000, n_features=20, noise=0.5, random_state=0)
sc = StandardScaler()
X = sc.fit_transform(X)
X_tr, X_te = X[:1500], X[1500:]
y_tr, y_te = y[:1500], y[1500:]

print(f'{"n_components":<14} {"MSE":<10} {"Time (s)":<10}')
print('-' * 36)
for n_comp in [50, 100, 200, 500]:
    t0 = time.time()
    pipe = make_pipeline(
        Nystroem(kernel='rbf', gamma=0.5, n_components=n_comp, random_state=0),
        Ridge(alpha=1.0)
    )
    pipe.fit(X_tr, y_tr)
    mse = mean_squared_error(y_te, pipe.predict(X_te))
    elapsed = time.time() - t0
    print(f'{n_comp:<14} {mse:<10.4f} {elapsed:<10.3f}')
print(f'Exact kernel matrix: {1500**2 * 8 / 1e6:.0f} MB vs Nystroem(m=200): {1500*200*8/1e6:.1f} MB')
```

## Method Comparison

| Method | Dual Form | Training Cost | Prediction Cost | Best For |
| --- | --- | --- | --- | --- |
| Kernel Ridge Regression | α = (K+λI)⁻¹y | O(n³) matrix solve | O(n·d) kernel evals per point | Small-n smooth regression |
| Kernel PCA | Eigendecompose centered K | O(n³) eigendecomp | O(n·p) projections per point | Nonlinear dimensionality reduction |
| Kernel SVM | QP over α with box constraints | O(n²) to O(n³) QP | O(n_sv·d) kernel evals (sparse) | Classification with margin |
| Nyström Approx. | K ≈ K_{nm}K_{mm}⁻¹K_{mn} | O(nm²) with m≪n | O(m) feature vector, O(1) model | Large-scale kernel methods n>10k |

All three methods share the same kernel matrix bottleneck. For n ≤ 5,000 use exact methods; for larger n use Nyström approximation or random Fourier features (Rahimi & Recht, 2007). The choice between KRR, kPCA, and kSVM depends on the task: regression, dimensionality reduction, or classification.

