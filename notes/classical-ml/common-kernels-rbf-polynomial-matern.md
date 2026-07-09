---
title: "Common Kernels — RBF, Polynomial, and Matérn"
slug: "common-kernels-rbf-polynomial-matern"
description: "A practical guide to the most widely used kernel functions: RBF/Gaussian, polynomial, Matérn family, and periodic kernels. Covers smoothness properties, parameter effects, and which kernel to choose for different regression tasks."
tags: ["kernel-methods", "gaussian-processes", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNob2ljZSBvZiBrZXJuZWwgZnVuY3Rpb24gaXMgdGhlIG1vc3QgY29uc2VxdWVudGlhbCBtb2RlbGluZyBkZWNpc2lvbiBpbiBhbnkga2VybmVsIG1ldGhvZCBvciBHYXVzc2lhbiBwcm9jZXNzLiBUaGUga2VybmVsIGVuY29kZXMgYWxsIHByaW9yIGFzc3VtcHRpb25zIGFib3V0IHRoZSBmdW5jdGlvblx1MDAyN3Mgc21vb3RobmVzcywgcGVyaW9kaWNpdHksIGFuZCBjb3JyZWxhdGlvbiBzdHJ1Y3R1cmUuIFVuZGVyc3RhbmRpbmcgdGhlIG1hdGhlbWF0aWNhbCBmb3JtLCBzbW9vdGhuZXNzIGNsYXNzLCBhbmQgaHlwZXJwYXJhbWV0ZXJzIG9mIGVhY2gga2VybmVsIGlzIGVzc2VudGlhbCBmb3Igc2VsZWN0aW5nIHRoZSByaWdodCBvbmUgZm9yIGEgZ2l2ZW4gcHJvYmxlbS4gVGhpcyBub3RlIGNvdmVycyB0aGUgZml2ZSBtb3N0IGltcG9ydGFudCBrZXJuZWwgZmFtaWxpZXMgd2l0aCB0aGVpciBtYXRoZW1hdGljYWwgcHJvcGVydGllcyBhbmQgcHJhY3RpY2FsIHRyYWRlb2Zmcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSQkYgKEdhdXNzaWFuKSBLZXJuZWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBSYWRpYWwgQmFzaXMgRnVuY3Rpb24gKFJCRikgb3IgR2F1c3NpYW4ga2VybmVsIGlzIHRoZSBkZWZhdWx0IGNob2ljZSBmb3Igc21vb3RoLCB1bmtub3duIGZ1bmN0aW9ucy4gSXQgbWVhc3VyZXMgc2ltaWxhcml0eSBwdXJlbHkgdGhyb3VnaCBFdWNsaWRlYW4gZGlzdGFuY2UuIEZ1bmN0aW9ucyBkcmF3biBmcm9tIGEgR1Agd2l0aCBSQkYgY292YXJpYW5jZSBhcmUgaW5maW5pdGVseSBkaWZmZXJlbnRpYWJsZSAoQ+KIniBzbW9vdGgpIOKAlCB0aGlzIGNhbiBiZSB1bnJlYWxpc3RpY2FsbHkgc21vb3RoIGZvciBwaHlzaWNhbCBwcm9jZXNzZXMuIFRoZSBSQkYgaXMgYSB1bml2ZXJzYWwga2VybmVsOiBpdCBjYW4gYXBwcm94aW1hdGUgYW55IGNvbnRpbnVvdXMgZnVuY3Rpb24gb24gYSBjb21wYWN0IGRvbWFpbiB0byBhcmJpdHJhcnkgYWNjdXJhY3kgZ2l2ZW4gZW5vdWdoIGRhdGEuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJrX3tcXHRleHR7UkJGfX0oeCwgeikgPSBcXHNpZ21hXjIgXFxleHBcXCFcXGxlZnQoLVxcZnJhY3tcXHx4IC0gelxcfF4yfXsyXFxlbGxeMn1cXHJpZ2h0KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBvbHlub21pYWwgYW5kIExpbmVhciBLZXJuZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcG9seW5vbWlhbCBrZXJuZWwgb2YgZGVncmVlIGQgY29ycmVzcG9uZHMgdG8gYSBmaW5pdGUtZGltZW5zaW9uYWwgZmVhdHVyZSBzcGFjZSBjb250YWluaW5nIGFsbCBtb25vbWlhbHMgdXAgdG8gZGVncmVlIGQuIEZvciBkPTEgYW5kIGM9MCwgaXQgcmVkdWNlcyB0byB0aGUgbGluZWFyIGtlcm5lbCB44bWAei4gVGhlIG9mZnNldCBjIFx1MDAzZSAwIGFkZHMgbG93ZXItZGVncmVlIHRlcm1zLiBQb2x5bm9taWFsIGtlcm5lbHMgYXJlIHBvcHVsYXIgaW4gdGV4dCBjbGFzc2lmaWNhdGlvbiAoYmFnLW9mLXdvcmRzIGZlYXR1cmVzKSBhbmQgZm9yIHByb2JsZW1zIHdoZXJlIHBvbHlub21pYWwgaW50ZXJhY3Rpb25zIGJldHdlZW4gZmVhdHVyZXMgYXJlIGV4cGVjdGVkLiBVbmxpa2UgUkJGLCBwb2x5bm9taWFsIGtlcm5lbHMgYXJlIG5vdCB1bml2ZXJzYWwg4oCUIHRoZXkgY2Fubm90IHJlcHJlc2VudCBhcmJpdHJhcnkgc21vb3RoIGZ1bmN0aW9ucy4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6Imtfe1xcdGV4dHtwb2x5fX0oeCwgeikgPSAoeF5cXHRvcCB6ICsgYyleZCwgXFxxdWFkIGMgXFxnZXEgMCwgXFw7IGQgXFxpbiBcXG1hdGhiYntafV97K30ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYXTDqXJuIEtlcm5lbCBGYW1pbHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBNYXTDqXJuIGZhbWlseSBwYXJhbWV0ZXJpemVzIHNtb290aG5lc3MgdGhyb3VnaCBhIG5vbi1uZWdhdGl2ZSBwYXJhbWV0ZXIgzr0uIEEgR1Agd2l0aCBNYXTDqXJuLc69IGtlcm5lbCBoYXMgc2FtcGxlIHBhdGhzIHRoYXQgYXJlIOKMis694oyLIHRpbWVzIGRpZmZlcmVudGlhYmxlLiBLZXkgaW5zdGFuY2VzOiDOvT0xLzIgKExhcGxhY2lhbi9leHBvbmVudGlhbCwgY29udGludW91cyBidXQgbm93aGVyZSBkaWZmZXJlbnRpYWJsZSksIM69PTMvMiAob25jZSBkaWZmZXJlbnRpYWJsZSksIM69PTUvMiAodHdpY2UgZGlmZmVyZW50aWFibGUpLCDOveKGkuKIniAocmVjb3ZlcnMgdGhlIFJCRikuIEZvciBtb3N0IHBoeXNpY2FsIGFuZCBlbmdpbmVlcmluZyBwcm9ibGVtcywgTWF0w6lybi01LzIgc3RyaWtlcyB0aGUgYmVzdCBiYWxhbmNlOiBpdCBhbGxvd3MgdHdpY2UtZGlmZmVyZW50aWFibGUgZnVuY3Rpb25zIHdpdGhvdXQgYXNzdW1pbmcgaW5maW5pdGUgc21vb3RobmVzcyBsaWtlIFJCRi4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6Imtfe1xcbnV9KHgsIHopID0gXFxmcmFjezJeezEtXFxudX19e1xcR2FtbWEoXFxudSl9XFxsZWZ0KFxcZnJhY3tcXHNxcnR7MlxcbnV9XFwscn17XFxlbGx9XFxyaWdodCleXFxudSBLX1xcbnVcXCFcXGxlZnQoXFxmcmFje1xcc3FydHsyXFxudX1cXCxyfXtcXGVsbH1cXHJpZ2h0KSwgXFxxdWFkIHIgPSBcXHx4LXpcXHwifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IldoeSBNYXTDqXJuIElzIE9mdGVuIFByZWZlcnJlZCBPdmVyIFJCRiIsImNvbnRlbnQiOiJSQkYgZnVuY3Rpb25zIGFyZSBD4oieIOKAlCBpbmZpbml0ZWx5IHNtb290aC4gUmVhbCBwaHlzaWNhbCBwcm9jZXNzZXMgKHRlbXBlcmF0dXJlIGZpZWxkcywgbWF0ZXJpYWwgcHJvcGVydGllcywgZmluYW5jaWFsIHRpbWUgc2VyaWVzKSBhcmUgdHlwaWNhbGx5IGZpbml0ZWx5IHNtb290aDogdHdpY2Ugb3IgdGhyaWNlIGRpZmZlcmVudGlhYmxlIGF0IG1vc3QuIEZpdHRpbmcgYW4gUkJGIGtlcm5lbCB0byBzdWNoIGRhdGEgZm9yY2VzIHRoZSBtb2RlbCB0byBiZSBvdmVyY29uZmlkZW50IGFib3V0IHNtb290aG5lc3MgYmV0d2VlbiBvYnNlcnZhdGlvbnMuIE1hdMOpcm4tNS8yIG9yIE1hdMOpcm4tMy8yIGFyZSBiZXR0ZXIgZGVmYXVsdCBjaG9pY2VzIGZvciBtb3N0IHJlYWwtd29ybGQgcmVncmVzc2lvbiB0YXNrcyBiZWNhdXNlIHRoZXkgbWFrZSBtb3JlIHJlYWxpc3RpYyBzbW9vdGhuZXNzIGFzc3VtcHRpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBlcmlvZGljIEtlcm5lbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHBlcmlvZGljIGtlcm5lbCBnZW5lcmF0ZXMgZnVuY3Rpb25zIHRoYXQgcmVwZWF0IGV4YWN0bHkgd2l0aCBwZXJpb2QgcC4gSXQgYXJpc2VzIGZyb20gbWFwcGluZyB0aGUgaW5wdXQgdGhyb3VnaCAoc2luKM+AeC9wKSwgY29zKM+AeC9wKSkgYW5kIGFwcGx5aW5nIGFuIFJCRiBrZXJuZWwgaW4gdGhhdCBlbWJlZGRpbmcuIFRoZSBsZW5ndGgtc2NhbGUg4oSTIGNvbnRyb2xzIGhvdyBxdWlja2x5IHRoZSBmdW5jdGlvbiB2YXJpZXMgd2l0aGluIGVhY2ggcGVyaW9kLiBGb3IgdGltZSBzZXJpZXMgd2l0aCBhIGtub3duIHNlYXNvbmFsaXR5IHBlcmlvZCAoZS5nLiwgMjQgaG91cnMsIDcgZGF5cywgMTIgbW9udGhzKSwgdGhlIHBlcmlvZGljIGtlcm5lbCBkaXJlY3RseSBlbmNvZGVzIHRoaXMgc3RydWN0dXJlIHJhdGhlciB0aGFuIGZvcmNpbmcgdGhlIG1vZGVsIHRvIGxlYXJuIGl0IGZyb20gZGF0YS4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6Imtfe1xcdGV4dHtwZXJ9fSh4LCB6KSA9IFxcc2lnbWFeMiBcXGV4cFxcIVxcbGVmdCgtXFxmcmFjezJcXHNpbl4yKFxccGl8eC16fC9wKX17XFxlbGxeMn1cXHJpZ2h0KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikxlbmd0aC1TY2FsZSBhbmQgU2lnbmFsIFZhcmlhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFdmVyeSBzdGF0aW9uYXJ5IGtlcm5lbCBoYXMgYXQgbGVhc3QgdHdvIGh5cGVycGFyYW1ldGVycy4gVGhlIGxlbmd0aC1zY2FsZSDihJMgY29udHJvbHMgdGhlIHJhbmdlIG9mIGNvcnJlbGF0aW9uOiBzbWFsbCDihJMg4oaSIGNvcnJlbGF0aW9uIGRlY2F5cyBxdWlja2x5IOKGkiByYXBpZCB2YXJpYXRpb247IGxhcmdlIOKEkyDihpIgY29ycmVsYXRpb24gZGVjYXlzIHNsb3dseSDihpIgc21vb3RoLCBzbG93bHkgdmFyeWluZyBmdW5jdGlvbnMuIFRoZSBzaWduYWwgdmFyaWFuY2Ugz4PCsiBzY2FsZXMgdGhlIG92ZXJhbGwgYW1wbGl0dWRlIG9mIHRoZSBmdW5jdGlvbi4gQm90aCBhcmUgbGVhcm5lZCBieSBtYXhpbWl6aW5nIHRoZSBtYXJnaW5hbCBsaWtlbGlob29kICh0eXBlLUlJIE1MRSkgcmF0aGVyIHRoYW4gY3Jvc3MtdmFsaWRhdGlvbiwgd2hpY2ggZWZmaWNpZW50bHkgaW50ZWdyYXRlcyBvdmVyIGFsbCBmdW5jdGlvbnMgY29uc2lzdGVudCB3aXRoIHRoZSBwcmlvci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIEV4YW1wbGVzIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgcmJmX2tlcm5lbChYLCBZLCBlbGw9MS4wLCBzaWdtYTI9MS4wKTpcbiAgICBkaWZmID0gWFs6LCBOb25lLCA6XSAtIFlbTm9uZSwgOiwgOl1cbiAgICByZXR1cm4gc2lnbWEyICogbnAuZXhwKC1ucC5zdW0oZGlmZioqMiwgYXhpcz0tMSkgLyAoMiAqIGVsbCoqMikpXG5cbmRlZiBwb2x5X2tlcm5lbChYLCBZLCBkPTMsIGM9MS4wKTpcbiAgICByZXR1cm4gKFggQCBZLlQgKyBjKSAqKiBkXG5cbmRlZiBsaW5lYXJfa2VybmVsKFgsIFkpOlxuICAgIHJldHVybiBYIEAgWS5UXG5cbmRlZiBtYXRlcm41Ml9rZXJuZWwoWCwgWSwgZWxsPTEuMCwgc2lnbWEyPTEuMCk6XG4gICAgZGlmZiA9IFhbOiwgTm9uZSwgOl0gLSBZW05vbmUsIDosIDpdXG4gICAgciA9IG5wLnNxcnQobnAuc3VtKGRpZmYqKjIsIGF4aXM9LTEpKSAvIGVsbFxuICAgIHJldHVybiBzaWdtYTIgKiAoMSArIG5wLnNxcnQoNSkqciArIDUqcioqMi8zKSAqIG5wLmV4cCgtbnAuc3FydCg1KSpyKVxuXG5ybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoNDIpXG5YID0gcm5nLnJhbmRuKDMwLCAyKVxua2VybmVscyA9IFtyYmZfa2VybmVsLCBwb2x5X2tlcm5lbCwgbGluZWFyX2tlcm5lbCwgbWF0ZXJuNTJfa2VybmVsXVxubmFtZXMgPSBbXHUwMDI3UkJGXHUwMDI3LCBcdTAwMjdQb2x5bm9taWFsIChkPTMpXHUwMDI3LCBcdTAwMjdMaW5lYXJcdTAwMjcsIFx1MDAyN01hdGVybi01LzJcdTAwMjddXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCA0LCBmaWdzaXplPSgxNiwgNCkpXG5mb3IgYXgsIGtmbiwgbmFtZSBpbiB6aXAoYXhlcywga2VybmVscywgbmFtZXMpOlxuICAgIEsgPSBrZm4oWCwgWClcbiAgICBpbSA9IGF4Lmltc2hvdyhLLCBjbWFwPVx1MDAyN3ZpcmlkaXNcdTAwMjcpXG4gICAgYXguc2V0X3RpdGxlKG5hbWUpXG4gICAgcGx0LmNvbG9yYmFyKGltLCBheD1heClcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3Z3JhbV9tYXRyaWNlcy5wbmdcdTAwMjcsIGRwaT0xMDApXG5wcmludChcdTAwMjdHcmFtIG1hdHJpY2VzIHNhdmVkLiBFYWNoIHNob3dzIGNvcnJlbGF0aW9uIHN0cnVjdHVyZSBmb3IgMzAgcmFuZG9tIHBvaW50cy5cdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5kZWYgc2FtcGxlX2dwKHgsIGtlcm5lbF9mbiwgbl9zYW1wbGVzPTQsIHNlZWQ9MCk6XG4gICAgWCA9IHhbOiwgTm9uZV1cbiAgICBLID0ga2VybmVsX2ZuKFgsIFgpICsgMWUtOCAqIG5wLmV5ZShsZW4oeCkpXG4gICAgTCA9IG5wLmxpbmFsZy5jaG9sZXNreShLKVxuICAgIHJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZShzZWVkKVxuICAgIHJldHVybiAoTCBAIHJuZy5yYW5kbihsZW4oeCksIG5fc2FtcGxlcykpLlRcblxueCA9IG5wLmxpbnNwYWNlKC01LCA1LCAzMDApXG5cbmRlZiByYmYoWDEsIFgyLCBlbGw9MS4wKTpcbiAgICByMiA9IG5wLnN1bSgoWDFbOiwgTm9uZSwgOl0gLSBYMltOb25lLCA6LCA6XSkqKjIsIGF4aXM9LTEpXG4gICAgcmV0dXJuIG5wLmV4cCgtcjIgLyAoMiAqIGVsbCoqMikpXG5cbmRlZiBtYXRlcm4xMihYMSwgWDIsIGVsbD0xLjApOlxuICAgIHIgPSBucC5hYnMoWDFbOiwgTm9uZSwgMF0gLSBYMltOb25lLCA6LCAwXSkgLyBlbGxcbiAgICByZXR1cm4gbnAuZXhwKC1yKVxuXG5kZWYgbWF0ZXJuNTIoWDEsIFgyLCBlbGw9MS4wKTpcbiAgICByID0gbnAuYWJzKFgxWzosIE5vbmUsIDBdIC0gWDJbTm9uZSwgOiwgMF0pIC8gZWxsXG4gICAgcmV0dXJuICgxICsgbnAuc3FydCg1KSpyICsgNSpyKioyLzMpICogbnAuZXhwKC1ucC5zcXJ0KDUpKnIpXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAzLCBmaWdzaXplPSgxNCwgNCkpXG5mb3IgYXgsIChuYW1lLCBrZm4pIGluIHppcChheGVzLCBbXG4gICAgKFx1MDAyN1JCRiBlbGw9MSAoQy1pbmYgc21vb3RoKVx1MDAyNywgcmJmKSxcbiAgICAoXHUwMDI3TWF0ZXJuLTEvMiBlbGw9MSAocm91Z2gpXHUwMDI3LCBtYXRlcm4xMiksXG4gICAgKFx1MDAyN01hdGVybi01LzIgZWxsPTEgKG1vZGVyYXRlKVx1MDAyNywgbWF0ZXJuNTIpLFxuXSk6XG4gICAgZm9yIHMgaW4gc2FtcGxlX2dwKHgsIGtmbik6XG4gICAgICAgIGF4LnBsb3QoeCwgcywgYWxwaGE9MC43NSlcbiAgICBheC5zZXRfdGl0bGUobmFtZSlcbiAgICBheC5zZXRfeWxpbSgtMywgMylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3a2VybmVsX2dwX3NhbXBsZXMucG5nXHUwMDI3LCBkcGk9MTAwKVxucHJpbnQoXHUwMDI3U2F2ZWQga2VybmVsX2dwX3NhbXBsZXMucG5nXHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIHJiZl9rZXJuZWxfMWQoeDEsIHgyLCBlbGwsIHNpZ21hMik6XG4gICAgZGlmZiA9IG5wLnN1YnRyYWN0Lm91dGVyKHgxLCB4MilcbiAgICByZXR1cm4gc2lnbWEyICogbnAuZXhwKC1kaWZmKioyIC8gKDIgKiBlbGwqKjIpKVxuXG5kZWYgc2FtcGxlX2Zyb21fa2VybmVsKHgsIEssIHNlZWQpOlxuICAgIEsgPSBLICsgMWUtOCAqIG5wLmV5ZShsZW4oeCkpXG4gICAgTCA9IG5wLmxpbmFsZy5jaG9sZXNreShLKVxuICAgIHJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZShzZWVkKVxuICAgIHJldHVybiBMIEAgcm5nLnJhbmRuKGxlbih4KSlcblxueCA9IG5wLmxpbnNwYWNlKC01LCA1LCAyMDApXG5jb25maWdzID0gW1xuICAgICgwLjMsIDEuMCwgXHUwMDI3ZWxsPTAuMyBzaWdtYTI9MSAoc2hvcnQgcmFuZ2UpXHUwMDI3KSxcbiAgICAoMS4wLCAxLjAsIFx1MDAyN2VsbD0xLjAgc2lnbWEyPTEgKG1lZGl1bSByYW5nZSlcdTAwMjcpLFxuICAgICgzLjAsIDEuMCwgXHUwMDI3ZWxsPTMuMCBzaWdtYTI9MSAobG9uZyByYW5nZSlcdTAwMjcpLFxuICAgICgxLjAsIDAuMjUsIFx1MDAyN2VsbD0xLjAgc2lnbWEyPTAuMjUgKGxvdyB2YXIpXHUwMDI3KSxcbiAgICAoMS4wLCAxLjAsICBcdTAwMjdlbGw9MS4wIHNpZ21hMj0xLjAwICh1bml0IHZhcilcdTAwMjcpLFxuICAgICgxLjAsIDQuMCwgIFx1MDAyN2VsbD0xLjAgc2lnbWEyPTQuMDAgKGhpZ2ggdmFyKVx1MDAyNyksXG5dXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMiwgMywgZmlnc2l6ZT0oMTQsIDYpKVxuZm9yIGF4LCAoZWxsLCBzaWdtYTIsIHRpdGxlKSBpbiB6aXAoYXhlcy5mbGF0LCBjb25maWdzKTpcbiAgICBLID0gcmJmX2tlcm5lbF8xZCh4LCB4LCBlbGwsIHNpZ21hMilcbiAgICBmb3Igc2VlZCBpbiByYW5nZSg0KTpcbiAgICAgICAgYXgucGxvdCh4LCBzYW1wbGVfZnJvbV9rZXJuZWwoeCwgSywgc2VlZCksIGFscGhhPTAuNylcbiAgICBheC5zZXRfdGl0bGUodGl0bGUsIGZvbnRzaXplPTkpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zYXZlZmlnKFx1MDAyN3JiZl9sZW5ndGhfc2NhbGUucG5nXHUwMDI3LCBkcGk9MTAwKVxucHJpbnQoXHUwMDI3U2F2ZWQgcmJmX2xlbmd0aF9zY2FsZS5wbmdcdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmtlcm5lbF9yaWRnZSBpbXBvcnQgS2VybmVsUmlkZ2VcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IGNyb3NzX3ZhbF9zY29yZVxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbmRlZiBtYWtlX2RhdGFzZXRzKCk6XG4gICAgcm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKDQyKVxuICAgIHggPSBucC5saW5zcGFjZSgwLCAxMCwgMTAwKVs6LCBOb25lXVxuICAgIHlfc21vb3RoICAgPSBucC5zaW4oeC5yYXZlbCgpKSArIHJuZy5yYW5kbigxMDApICogMC4xXG4gICAgeV9wZXJpb2RpYyA9IG5wLnNpbigyICogbnAucGkgKiB4LnJhdmVsKCkgLyAzKSArIHJuZy5yYW5kbigxMDApICogMC4xXG4gICAgeV9yb3VnaCAgICA9IG5wLmFicyhucC5zaW4oeC5yYXZlbCgpKSkgKyBybmcucmFuZG4oMTAwKSAqIDAuMlxuICAgIHJldHVybiB4LCB7XHUwMDI3c21vb3RoXHUwMDI3OiB5X3Ntb290aCwgXHUwMDI3cGVyaW9kaWNcdTAwMjc6IHlfcGVyaW9kaWMsIFx1MDAyN3JvdWdoXHUwMDI3OiB5X3JvdWdofVxuXG54LCBkYXRhc2V0cyA9IG1ha2VfZGF0YXNldHMoKVxua2VybmVscyA9IHtcbiAgICBcdTAwMjdyYmZcdTAwMjc6ICAgICAgIEtlcm5lbFJpZGdlKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGFscGhhPTAuMSwgZ2FtbWE9MS4wKSxcbiAgICBcdTAwMjdwb2x5XHUwMDI3OiAgICAgIEtlcm5lbFJpZGdlKGtlcm5lbD1cdTAwMjdwb2x5XHUwMDI3LCBhbHBoYT0wLjEsIGRlZ3JlZT0zLCBjb2VmMD0xKSxcbiAgICBcdTAwMjdsYXBsYWNpYW5cdTAwMjc6IEtlcm5lbFJpZGdlKGtlcm5lbD1cdTAwMjdsYXBsYWNpYW5cdTAwMjcsIGFscGhhPTAuMSwgZ2FtbWE9MS4wKSxcbn1cbnByaW50KGZcdTAwMjd7XCJEYXRhc2V0XCI6XHUwMDNjMTJ9IHtcIktlcm5lbFwiOlx1MDAzYzEyfSBDViBSMiBtZWFuICsvLSBzdGRcdTAwMjcpXG5wcmludChcdTAwMjctXHUwMDI3ICogNDgpXG5mb3IgZHNfbmFtZSwgeSBpbiBkYXRhc2V0cy5pdGVtcygpOlxuICAgIGZvciBrX25hbWUsIG1vZGVsIGluIGtlcm5lbHMuaXRlbXMoKTpcbiAgICAgICAgc2NvcmVzID0gY3Jvc3NfdmFsX3Njb3JlKG1vZGVsLCB4LCB5LCBjdj01LCBzY29yaW5nPVx1MDAyN3IyXHUwMDI3KVxuICAgICAgICBwcmludChmXHUwMDI3e2RzX25hbWU6XHUwMDNjMTJ9IHtrX25hbWU6XHUwMDNjMTJ9IHtzY29yZXMubWVhbigpOi4zZn0gKy8tIHtzY29yZXMuc3RkKCk6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXJuZWwgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJLZXJuZWwiLCJTbW9vdGhuZXNzIENsYXNzIiwiS2V5IFBhcmFtZXRlcnMiLCJVbml2ZXJzYWwgQXBwcm94aW1hdG9yIiwiQmVzdCBVc2UgQ2FzZSJdLCJyb3dzIjpbWyJSQkYgKEdhdXNzaWFuKSIsIkPiiJ4gKGluZmluaXRlbHkgZGlmZmVyZW50aWFibGUpIiwiTGVuZ3RoLXNjYWxlIOKEkywgdmFyaWFuY2Ugz4PCsiIsIlllcyIsIlNtb290aCB1bmtub3duIGZ1bmN0aW9ucywgZGVmYXVsdCBHUCJdLFsiUG9seW5vbWlhbCAoZGVncmVlIGQpIiwiQ+KIniBidXQgZmluaXRlLXJhbmsgUktIUyIsIkRlZ3JlZSBkLCBvZmZzZXQgYyIsIk5vIiwiVGV4dCBrZXJuZWxzLCBwb2x5bm9taWFsIGludGVyYWN0aW9ucyJdLFsiTWF0w6lybi0xLzIgKExhcGxhY2lhbikiLCJD4oGwIChjb250aW51b3VzLCBub3QgZGlmZi4pIiwiTGVuZ3RoLXNjYWxlIOKEkyIsIlllcyIsIlJvdWdoIHBoeXNpY2FsIHByb2Nlc3NlcywgT1UgcHJvY2VzcyJdLFsiTWF0w6lybi01LzIiLCJD4oG0ICh0d2ljZSBkaWZmZXJlbnRpYWJsZSkiLCJMZW5ndGgtc2NhbGUg4oSTIiwiWWVzIiwiTW9zdCBwaHlzaWNhbCBhbmQgZW5naW5lZXJpbmcgcHJvYmxlbXMiXSxbIlBlcmlvZGljIiwiQ+KIniBidXQgcGVyaW9kaWMgc3RydWN0dXJlIiwiUGVyaW9kIHAsIGxlbmd0aC1zY2FsZSDihJMiLCJObyAocGVyaW9kaWMgb25seSkiLCJUaW1lIHNlcmllcyB3aXRoIGtub3duIHNlYXNvbmFsaXR5Il1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5vIHNpbmdsZSBrZXJuZWwgaXMgdW5pdmVyc2FsbHkgYmVzdC4gVGhlIFJCRiBpcyBhIHNhZmUgZGVmYXVsdCBmb3Igc21vb3RoIGZ1bmN0aW9ucywgTWF0w6lybi01LzIgZm9yIG1vc3QgcmVhbC13b3JsZCByZWdyZXNzaW9uIHRhc2tzLCBhbmQgdGhlIHBlcmlvZGljIGtlcm5lbCB3aGVuIHBlcmlvZGljaXR5IGlzIGtub3duLiBLZXJuZWwgY29tcG9zaXRpb24gcnVsZXMgYWxsb3cgY29tYmluaW5nIHRoZXNlIHByaW1pdGl2ZXMgdG8gaGFuZGxlIG1vcmUgY29tcGxleCBmdW5jdGlvbiBjbGFzc2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNob29zaW5nIHRoZSBSaWdodCBLZXJuZWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc3lzdGVtYXRpYyBhcHByb2FjaCB0byBrZXJuZWwgc2VsZWN0aW9uOiBzdGFydCB3aXRoIGRvbWFpbiBrbm93bGVkZ2UgYWJvdXQgc21vb3RobmVzcyAoZG8geW91IGV4cGVjdCBD4oieIG9yIGZpbml0ZWx5IGRpZmZlcmVudGlhYmxlIGZ1bmN0aW9ucz8pLCB0aGVuIHZhbGlkYXRlIGJ5IGNvbXBhcmluZyBtYXJnaW5hbCBsaWtlbGlob29kcyBvbiBoZWxkLW91dCBkYXRhLiBDb25zaWRlciB0aGVzZSBwcmFjdGljYWwgZ3VpZGVsaW5lczoifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlVua25vd24gc21vb3RoIGZ1bmN0aW9uIHdpdGggbm8gc3BlY2lhbCBzdHJ1Y3R1cmUg4oaSIHN0YXJ0IHdpdGggUkJGIG9yIE1hdMOpcm4tNS8yLiIsIlBoeXNpY2FsIHByb2Nlc3MgKGhlYXQsIGZsdWlkLCBtYXRlcmlhbHMpIOKGkiBNYXTDqXJuLTUvMiBvciBNYXTDqXJuLTMvMiAoYXZvaWQgb3Zlci1zbW9vdGggUkJGKS4iLCJUaW1lIHNlcmllcyB3aXRoIGtub3duIHNlYXNvbmFsaXR5IOKGkiBwZXJpb2RpYyBrZXJuZWwgb3IgcGVyaW9kaWMgw5cgUkJGIGNvbXBvc2l0ZS4iLCJIaWdoLWRpbWVuc2lvbmFsIHNwYXJzZSBkYXRhICh0ZXh0LCBnZW5vbWljcykg4oaSIGxpbmVhciBvciBwb2x5bm9taWFsIGtlcm5lbC4iLCJGdW5jdGlvbiB3aXRoIG11bHRpcGxlIGxlbmd0aC1zY2FsZXMg4oaSIEFSRCBrZXJuZWwgd2l0aCBwZXItZGltZW5zaW9uIOKEk+G1oi4iLCJXaGVuIHVuY2VydGFpbiDihpIgY29tcGFyZSBsb2cgbWFyZ2luYWwgbGlrZWxpaG9vZHMgYWNyb3NzIDLigJMzIGNhbmRpZGF0ZSBrZXJuZWxzLiJdfV0="
---
# Common Kernels — RBF, Polynomial, and Matérn

The choice of kernel function is the most consequential modeling decision in any kernel method or Gaussian process. The kernel encodes all prior assumptions about the function's smoothness, periodicity, and correlation structure. Understanding the mathematical form, smoothness class, and hyperparameters of each kernel is essential for selecting the right one for a given problem. This note covers the five most important kernel families with their mathematical properties and practical tradeoffs.

## RBF (Gaussian) Kernel

The Radial Basis Function (RBF) or Gaussian kernel is the default choice for smooth, unknown functions. It measures similarity purely through Euclidean distance. Functions drawn from a GP with RBF covariance are infinitely differentiable (C∞ smooth) — this can be unrealistically smooth for physical processes. The RBF is a universal kernel: it can approximate any continuous function on a compact domain to arbitrary accuracy given enough data.

$$k_{\text{RBF}}(x, z) = \sigma^2 \exp\!\left(-\frac{\|x - z\|^2}{2\ell^2}\right)$$

## Polynomial and Linear Kernels

The polynomial kernel of degree d corresponds to a finite-dimensional feature space containing all monomials up to degree d. For d=1 and c=0, it reduces to the linear kernel xᵀz. The offset c > 0 adds lower-degree terms. Polynomial kernels are popular in text classification (bag-of-words features) and for problems where polynomial interactions between features are expected. Unlike RBF, polynomial kernels are not universal — they cannot represent arbitrary smooth functions.

$$k_{\text{poly}}(x, z) = (x^\top z + c)^d, \quad c \geq 0, \; d \in \mathbb{Z}_{+}$$

## Matérn Kernel Family

The Matérn family parameterizes smoothness through a non-negative parameter ν. A GP with Matérn-ν kernel has sample paths that are ⌊ν⌋ times differentiable. Key instances: ν=1/2 (Laplacian/exponential, continuous but nowhere differentiable), ν=3/2 (once differentiable), ν=5/2 (twice differentiable), ν→∞ (recovers the RBF). For most physical and engineering problems, Matérn-5/2 strikes the best balance: it allows twice-differentiable functions without assuming infinite smoothness like RBF.

$$k_{\nu}(x, z) = \frac{2^{1-\nu}}{\Gamma(\nu)}\left(\frac{\sqrt{2\nu}\,r}{\ell}\right)^\nu K_\nu\!\left(\frac{\sqrt{2\nu}\,r}{\ell}\right), \quad r = \|x-z\|$$

> **Why Matérn Is Often Preferred Over RBF**: RBF functions are C∞ — infinitely smooth. Real physical processes (temperature fields, material properties, financial time series) are typically finitely smooth: twice or thrice differentiable at most. Fitting an RBF kernel to such data forces the model to be overconfident about smoothness between observations. Matérn-5/2 or Matérn-3/2 are better default choices for most real-world regression tasks because they make more realistic smoothness assumptions.

## Periodic Kernel

The periodic kernel generates functions that repeat exactly with period p. It arises from mapping the input through (sin(πx/p), cos(πx/p)) and applying an RBF kernel in that embedding. The length-scale ℓ controls how quickly the function varies within each period. For time series with a known seasonality period (e.g., 24 hours, 7 days, 12 months), the periodic kernel directly encodes this structure rather than forcing the model to learn it from data.

$$k_{\text{per}}(x, z) = \sigma^2 \exp\!\left(-\frac{2\sin^2(\pi|x-z|/p)}{\ell^2}\right)$$

## Length-Scale and Signal Variance

Every stationary kernel has at least two hyperparameters. The length-scale ℓ controls the range of correlation: small ℓ → correlation decays quickly → rapid variation; large ℓ → correlation decays slowly → smooth, slowly varying functions. The signal variance σ² scales the overall amplitude of the function. Both are learned by maximizing the marginal likelihood (type-II MLE) rather than cross-validation, which efficiently integrates over all functions consistent with the prior.

## Code Examples

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X, Y, ell=1.0, sigma2=1.0):
    diff = X[:, None, :] - Y[None, :, :]
    return sigma2 * np.exp(-np.sum(diff**2, axis=-1) / (2 * ell**2))

def poly_kernel(X, Y, d=3, c=1.0):
    return (X @ Y.T + c) ** d

def linear_kernel(X, Y):
    return X @ Y.T

def matern52_kernel(X, Y, ell=1.0, sigma2=1.0):
    diff = X[:, None, :] - Y[None, :, :]
    r = np.sqrt(np.sum(diff**2, axis=-1)) / ell
    return sigma2 * (1 + np.sqrt(5)*r + 5*r**2/3) * np.exp(-np.sqrt(5)*r)

rng = np.random.RandomState(42)
X = rng.randn(30, 2)
kernels = [rbf_kernel, poly_kernel, linear_kernel, matern52_kernel]
names = ['RBF', 'Polynomial (d=3)', 'Linear', 'Matern-5/2']

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, kfn, name in zip(axes, kernels, names):
    K = kfn(X, X)
    im = ax.imshow(K, cmap='viridis')
    ax.set_title(name)
    plt.colorbar(im, ax=ax)
plt.tight_layout()
plt.savefig('gram_matrices.png', dpi=100)
print('Gram matrices saved. Each shows correlation structure for 30 random points.')
```

```python
import numpy as np
import matplotlib.pyplot as plt

def sample_gp(x, kernel_fn, n_samples=4, seed=0):
    X = x[:, None]
    K = kernel_fn(X, X) + 1e-8 * np.eye(len(x))
    L = np.linalg.cholesky(K)
    rng = np.random.RandomState(seed)
    return (L @ rng.randn(len(x), n_samples)).T

x = np.linspace(-5, 5, 300)

def rbf(X1, X2, ell=1.0):
    r2 = np.sum((X1[:, None, :] - X2[None, :, :])**2, axis=-1)
    return np.exp(-r2 / (2 * ell**2))

def matern12(X1, X2, ell=1.0):
    r = np.abs(X1[:, None, 0] - X2[None, :, 0]) / ell
    return np.exp(-r)

def matern52(X1, X2, ell=1.0):
    r = np.abs(X1[:, None, 0] - X2[None, :, 0]) / ell
    return (1 + np.sqrt(5)*r + 5*r**2/3) * np.exp(-np.sqrt(5)*r)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, (name, kfn) in zip(axes, [
    ('RBF ell=1 (C-inf smooth)', rbf),
    ('Matern-1/2 ell=1 (rough)', matern12),
    ('Matern-5/2 ell=1 (moderate)', matern52),
]):
    for s in sample_gp(x, kfn):
        ax.plot(x, s, alpha=0.75)
    ax.set_title(name)
    ax.set_ylim(-3, 3)
plt.tight_layout()
plt.savefig('kernel_gp_samples.png', dpi=100)
print('Saved kernel_gp_samples.png')
```

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel_1d(x1, x2, ell, sigma2):
    diff = np.subtract.outer(x1, x2)
    return sigma2 * np.exp(-diff**2 / (2 * ell**2))

def sample_from_kernel(x, K, seed):
    K = K + 1e-8 * np.eye(len(x))
    L = np.linalg.cholesky(K)
    rng = np.random.RandomState(seed)
    return L @ rng.randn(len(x))

x = np.linspace(-5, 5, 200)
configs = [
    (0.3, 1.0, 'ell=0.3 sigma2=1 (short range)'),
    (1.0, 1.0, 'ell=1.0 sigma2=1 (medium range)'),
    (3.0, 1.0, 'ell=3.0 sigma2=1 (long range)'),
    (1.0, 0.25, 'ell=1.0 sigma2=0.25 (low var)'),
    (1.0, 1.0,  'ell=1.0 sigma2=1.00 (unit var)'),
    (1.0, 4.0,  'ell=1.0 sigma2=4.00 (high var)'),
]
fig, axes = plt.subplots(2, 3, figsize=(14, 6))
for ax, (ell, sigma2, title) in zip(axes.flat, configs):
    K = rbf_kernel_1d(x, x, ell, sigma2)
    for seed in range(4):
        ax.plot(x, sample_from_kernel(x, K, seed), alpha=0.7)
    ax.set_title(title, fontsize=9)
plt.tight_layout()
plt.savefig('rbf_length_scale.png', dpi=100)
print('Saved rbf_length_scale.png')
```

```python
import numpy as np
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

def make_datasets():
    rng = np.random.RandomState(42)
    x = np.linspace(0, 10, 100)[:, None]
    y_smooth   = np.sin(x.ravel()) + rng.randn(100) * 0.1
    y_periodic = np.sin(2 * np.pi * x.ravel() / 3) + rng.randn(100) * 0.1
    y_rough    = np.abs(np.sin(x.ravel())) + rng.randn(100) * 0.2
    return x, {'smooth': y_smooth, 'periodic': y_periodic, 'rough': y_rough}

x, datasets = make_datasets()
kernels = {
    'rbf':       KernelRidge(kernel='rbf', alpha=0.1, gamma=1.0),
    'poly':      KernelRidge(kernel='poly', alpha=0.1, degree=3, coef0=1),
    'laplacian': KernelRidge(kernel='laplacian', alpha=0.1, gamma=1.0),
}
print(f'{"Dataset":<12} {"Kernel":<12} CV R2 mean +/- std')
print('-' * 48)
for ds_name, y in datasets.items():
    for k_name, model in kernels.items():
        scores = cross_val_score(model, x, y, cv=5, scoring='r2')
        print(f'{ds_name:<12} {k_name:<12} {scores.mean():.3f} +/- {scores.std():.3f}')
```

## Kernel Comparison

| Kernel | Smoothness Class | Key Parameters | Universal Approximator | Best Use Case |
| --- | --- | --- | --- | --- |
| RBF (Gaussian) | C∞ (infinitely differentiable) | Length-scale ℓ, variance σ² | Yes | Smooth unknown functions, default GP |
| Polynomial (degree d) | C∞ but finite-rank RKHS | Degree d, offset c | No | Text kernels, polynomial interactions |
| Matérn-1/2 (Laplacian) | C⁰ (continuous, not diff.) | Length-scale ℓ | Yes | Rough physical processes, OU process |
| Matérn-5/2 | C⁴ (twice differentiable) | Length-scale ℓ | Yes | Most physical and engineering problems |
| Periodic | C∞ but periodic structure | Period p, length-scale ℓ | No (periodic only) | Time series with known seasonality |

No single kernel is universally best. The RBF is a safe default for smooth functions, Matérn-5/2 for most real-world regression tasks, and the periodic kernel when periodicity is known. Kernel composition rules allow combining these primitives to handle more complex function classes.

## Choosing the Right Kernel

A systematic approach to kernel selection: start with domain knowledge about smoothness (do you expect C∞ or finitely differentiable functions?), then validate by comparing marginal likelihoods on held-out data. Consider these practical guidelines:

- Unknown smooth function with no special structure → start with RBF or Matérn-5/2.
- Physical process (heat, fluid, materials) → Matérn-5/2 or Matérn-3/2 (avoid over-smooth RBF).
- Time series with known seasonality → periodic kernel or periodic × RBF composite.
- High-dimensional sparse data (text, genomics) → linear or polynomial kernel.
- Function with multiple length-scales → ARD kernel with per-dimension ℓᵢ.
- When uncertain → compare log marginal likelihoods across 2–3 candidate kernels.

