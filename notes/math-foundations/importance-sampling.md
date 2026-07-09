---
title: "Importance Sampling"
slug: "importance-sampling"
description: "The importance sampling estimator, self-normalised IS, effective sample size, variance explosion with mismatched proposals, weight clipping, annealed IS, and applications in off-policy RL and RLHF."
tags: ["probability", "statistics", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiSW1wb3J0YW5jZSBzYW1wbGluZyAoSVMpIHNvbHZlcyBhIGZ1bmRhbWVudGFsIHByb2JsZW06IGVzdGltYXRpbmcgZXhwZWN0YXRpb25zIHVuZGVyIGEgdGFyZ2V0IGRpc3RyaWJ1dGlvbiBwIHdoZW4gc2FtcGxlcyBjYW4gb25seSBiZSBkcmF3biBmcm9tIGEgZGlmZmVyZW50IHByb3Bvc2FsIGRpc3RyaWJ1dGlvbiBxLiBUaGlzIGFyaXNlcyBjb25zdGFudGx5IGluIE1MIOKAlCBjb21wdXRpbmcgZXhwZWN0YXRpb25zIHVuZGVyIGEgY29tcGxleCBwb3N0ZXJpb3Igd2hlbiBvbmx5IGEgc2ltcGxlIGRpc3RyaWJ1dGlvbiBpcyBzYW1wbGVhYmxlLCBjb3JyZWN0aW5nIGZvciBkaXN0cmlidXRpb25hbCBzaGlmdCBiZXR3ZWVuIHRyYWluaW5nIGFuZCBkZXBsb3ltZW50LCBldmFsdWF0aW5nIHBvbGljaWVzIHRyYWluZWQgb24gZGlmZmVyZW50IGRhdGEsIGFuZCBmaW5lLXR1bmluZyBsYW5ndWFnZSBtb2RlbHMgd2l0aCBSTEhGIHdoZXJlIHJlZmVyZW5jZSBhbmQgZmluZS10dW5lZCBkaXN0cmlidXRpb25zIGRpdmVyZ2UuIElTIGlzIGFsc28gdGhlIGZvdW5kYXRpb24gb2YgU2VxdWVudGlhbCBNb250ZSBDYXJsbywgYW5uZWFsZWQgaW1wb3J0YW5jZSBzYW1wbGluZyBmb3IgcGFydGl0aW9uIGZ1bmN0aW9uIGVzdGltYXRpb24sIGFuZCBwb2xpY3kgZ3JhZGllbnQgdmFyaWFuY2UgcmVkdWN0aW9uIHRocm91Z2ggYmFzZWxpbmUgc3VidHJhY3Rpb24uIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29yZSBEZWZpbml0aW9uIOKAlCBUaGUgSVMgRXN0aW1hdG9yIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiR29hbDogZXN0aW1hdGUgRV9wW2YoWCldID0g4oirIGYoeCkgcCh4KSBkeCBidXQgd2UgY2FuIG9ubHkgc2FtcGxlIGZyb20gcSh4KS5cblxuS2V5IGFsZ2VicmFpYyBpZGVudGl0eTpcbkVfcFtmKFgpXSA9IOKIqyBmKHgpIHAoeCkgZHggPSDiiKsgZih4KSBbcCh4KS9xKHgpXSBxKHgpIGR4ID0gRV9xW2YoWCkgdyhYKV1cblxud2hlcmUgdyh4KSA9IHAoeCkvcSh4KSBhcmUgdGhlIGltcG9ydGFuY2Ugd2VpZ2h0cy4gUmVxdWlyZW1lbnRzOiBxIG11c3QgaGF2ZSBzdXBwb3J0IGV2ZXJ5d2hlcmUgcCBpcyBwb3NpdGl2ZSAocSh4KSA+IDAgd2hlbmV2ZXIgcCh4KSA+IDApLlxuXG5JUyBlc3RpbWF0b3IgKHVubm9ybWFsaXNlZCk6XG7Dil9JU1tmXSA9ICgxL04pIM6j4bWiIGYoeOG1oikgdyh44bWiKSwgIHjhtaIgfiBxXG5cblNlbGYtbm9ybWFsaXNlZCBJUyAoU05JUykg4oCUIGRvZXMgbm90IHJlcXVpcmUga25vd2luZyB0aGUgbm9ybWFsaXNhdGlvbiBjb25zdGFudCBvZiBwOlxuw4pfU05JU1tmXSA9IM6j4bWiIGYoeOG1oikgd8yD4bWiICB3aGVyZSB3zIPhtaIgPSB34bWiIC8gzqPisbwgd+KxvFxuXG5TTklTIGlzIGJpYXNlZCBidXQgY29uc2lzdGVudCAoYmlhcyBPKDEvTikpLiBJdCBpcyBwcmVmZXJyZWQgd2hlbiBwIGlzIGtub3duIG9ubHkgdXAgdG8gYSBub3JtYWxpc2luZyBjb25zdGFudCwgd2hpY2ggaXMgdGhlIGNvbW1vbiBjYXNlIGluIEJheWVzaWFuIGluZmVyZW5jZS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5IGltcG9ydCBzdGF0c1xuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgVGFyZ2V0IHA6IE4oMywgMC41XjIpOyBQcm9wb3NhbCBxOiBOKDAsIDJeMilcbiMgR29hbDogRV9wW1heMl0gPSBtdV4yICsgc2lnbWFeMiA9IDkuMjVcbm11X3AsIHNpZ21hX3AgPSAzLjAsIDAuNVxubXVfcSwgc2lnbWFfcSA9IDAuMCwgMi4wXG50cnVlX3ZhbCA9IG11X3AqKjIgKyBzaWdtYV9wKioyICAjIDkuMjVcblxuTiA9IDUwMDBcbnggPSBybmcubm9ybWFsKG11X3EsIHNpZ21hX3EsIE4pICAjIHNhbXBsZSBmcm9tIHFcblxuIyBDb21wdXRlIGxvZyBpbXBvcnRhbmNlIHdlaWdodHMgKGFsd2F5cyB3b3JrIGluIGxvZy1zcGFjZSEpXG5sb2dfdyA9IHN0YXRzLm5vcm0ubG9ncGRmKHgsIG11X3AsIHNpZ21hX3ApIC0gc3RhdHMubm9ybS5sb2dwZGYoeCwgbXVfcSwgc2lnbWFfcSlcbncgPSBucC5leHAobG9nX3cpXG5cbiMgVW5ub3JtYWxpc2VkIElTIChyZXF1aXJlcyBwIHRvIGJlIG5vcm1hbGlzZWQpXG5pc19lc3QgICA9IG5wLm1lYW4oeCoqMiAqIHcpXG5cbiMgU2VsZi1ub3JtYWxpc2VkIElTICh3b3JrcyB3aXRoIHVubm9ybWFsaXNlZCBwKVxud19ub3JtICAgPSB3IC8gdy5zdW0oKVxuc25pc19lc3QgPSBucC5zdW0oeCoqMiAqIHdfbm9ybSlcblxuIyBFZmZlY3RpdmUgc2FtcGxlIHNpemU6IEVTUyA9IChzdW0gdyleMiAvIHN1bSh3XjIpXG5lc3MgPSB3LnN1bSgpKioyIC8gbnAuc3VtKHcqKjIpXG5cbnByaW50KGZcIlRydWUgRV9wW1heMl06ICAgICB7dHJ1ZV92YWw6LjRmfVwiKVxucHJpbnQoZlwiSVMgZXN0aW1hdGU6ICAgICAgIHtpc19lc3Q6LjRmfSAgKHJlcXVpcmVzIG5vcm1hbGlzZWQgcClcIilcbnByaW50KGZcIlNOSVMgZXN0aW1hdGU6ICAgICB7c25pc19lc3Q6LjRmfSAgKHdvcmtzIHdpdGggdW5ub3JtYWxpc2VkIHApXCIpXG5wcmludChmXCJFU1M6IHtlc3M6LjFmfSAvIHtOfSAgKHsxMDAqZXNzL046LjFmfSUpXCIpXG5cbiMgV2VpZ2h0IGRpYWdub3N0aWNzXG53X25vcm1fc29ydGVkID0gbnAuc29ydCh3X25vcm0pWzo6LTFdXG5jdW1zdW0gPSBucC5jdW1zdW0od19ub3JtX3NvcnRlZClcbm5fNTBwY3QgPSBucC5zZWFyY2hzb3J0ZWQoY3Vtc3VtLCAwLjUpICsgMVxucHJpbnQoZlwiVG9wIHtuXzUwcGN0fSBzYW1wbGVzIGNhcnJ5IDUwJSBvZiB0b3RhbCB3ZWlnaHQgKG91dCBvZiB7Tn0pXCIpXG5wcmludChmXCJNYXggd2VpZ2h0OiB7d19ub3JtLm1heCgpOi40ZX0sIG1lYW4gd2VpZ2h0OiB7d19ub3JtLm1lYW4oKTouNGV9XCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiRWZmZWN0aXZlIFNhbXBsZSBTaXplIGFuZCBWYXJpYW5jZSJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBlZmZlY3RpdmUgc2FtcGxlIHNpemUgKEVTUykgbWVhc3VyZXMgaG93IG1hbnkgaS5pLmQuIHNhbXBsZXMgZnJvbSBwIHRoZSBJUyBlc3RpbWF0ZSBpcyBlcXVpdmFsZW50IHRvOlxuXG5FU1MgPSAozqPhtaIgd+G1oinCsiAvIM6j4bWiIHfhtaLCslxuXG5Gb3Igbm9ybWFsaXNlZCB3ZWlnaHRzOiBFU1MgPSAxIC8gzqPhtaIgd8yD4bWiwrIg4oiIIFsxLCBOXS5cblxuUHJvcGVydGllczpcbi0gRVNTID0gTiB3aGVuIGFsbCB3ZWlnaHRzIGFyZSBlcXVhbCDigJQgdGhpcyBoYXBwZW5zIHdoZW4gcSA9IHAgKHBlcmZlY3QgcHJvcG9zYWwpXG4tIEVTUyA9IDEgd2hlbiBvbmUgd2VpZ2h0IGRvbWluYXRlcyBhbGwgb3RoZXJzIOKAlCB3b3JzdCBjYXNlLCB0aGUgZXN0aW1hdGUgaXMgYmFzZWQgb24gYSBzaW5nbGUgc2FtcGxlXG4tIEVTUy9OIG1lYXN1cmVzIHRoZSBlZmZpY2llbmN5IG9mIElTOiB2YWx1ZXMgYWJvdmUgMC41IGluZGljYXRlIHJlYXNvbmFibGUgcHJvcG9zYWxzOyBiZWxvdyAwLjEgaXMgcHJvYmxlbWF0aWNcblxuVmFyaWFuY2Ugb2YgdGhlIElTIGVzdGltYXRvcjpcblZhcl9xW2YoeCkgdyh4KV0gPSDiiKsgKGYoeCkgdyh4KSnCsiBxKHgpIGR4IOKIkiAoRV9wW2YoeCldKcKyXG5cblRoaXMgdmFyaWFuY2UgaXMgZmluaXRlIGlmIGFuZCBvbmx5IGlmIEVfcVsoZih4KSB3KHgpKcKyXSA8IOKIniDigJQgcm91Z2hseSByZXF1aXJpbmcgdGhhdCBwKHgpL3EoeCkgaXMgYm91bmRlZC4gSWYgcSBoYXMgbGlnaHRlciB0YWlscyB0aGFuIHAgYW55d2hlcmUsIHRoZSByYXRpbyBwL3EgY2FuIGJlY29tZSB1bmJvdW5kZWQgYW5kIHZhcmlhbmNlIGlzIGluZmluaXRlLiBUaGUgb3B0aW1hbCBJUyBwcm9wb3NhbCBpcyBxKih4KSDiiJ0gfGYoeCl8IHAoeCksIGNvbmNlbnRyYXRpbmcgc2FtcGxlcyB3aGVyZSB0aGUgaW50ZWdyYW5kIGlzIGxhcmdlc3QuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiVmFyaWFuY2UgRXhwbG9zaW9uIGFuZCBXZWlnaHQgQ2xpcHBpbmcifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJXaGVuIHEgaGFzIGxpZ2h0ZXIgdGFpbHMgdGhhbiBwLCB0aGUgaW1wb3J0YW5jZSB3ZWlnaHRzIHcoeCkgPSBwKHgpL3EoeCkg4oaSIOKIniBmb3IgbGFyZ2UgfHh8LiBUaGlzIGNhdXNlczpcblxuMS4gQSBmZXcgc2FtcGxlcyB3aXRoIGVub3Jtb3VzIHdlaWdodHMgZG9taW5hdGUgdGhlIGVzdGltYXRlIChFU1Mg4oaSIDEpXG4yLiBUaGUgSVMgZXN0aW1hdG9yIGhhcyBpbmZpbml0ZSB2YXJpYW5jZSAoZGVzcGl0ZSBiZWluZyB1bmJpYXNlZClcbjMuIEluIHByYWN0aWNlOiBoaWdobHkgdmFyaWFibGUgZXN0aW1hdGVzLCBudW1lcmljYWwgb3ZlcmZsb3cgaW4gd2VpZ2h0c1xuXG5XZWlnaHQgY2xpcHBpbmcgKHRydW5jYXRpb24pIGNhcHMgd2VpZ2h0cyBhdCBhIG1heGltdW0gdmFsdWUgYzogd8yDKHgpID0gbWluKHcoeCksIGMpLiBUaGlzIGludHJvZHVjZXMgYmlhcyDigJQgaXQgbm8gbG9uZ2VyIGNvcnJlY3RseSBlc3RpbWF0ZXMgRV9wW2ZdIOKAlCBidXQgcmVkdWNlcyB2YXJpYW5jZSBzdWJzdGFudGlhbGx5LiBUaGUgYmlhcyBpcyBPKFAodyhYKSA+IGMpKSB3aGljaCBpcyBzbWFsbCB3aGVuIGMgaXMgY2hvc2VuIGFwcHJvcHJpYXRlbHkuXG5cbkZvciBSTEhGOiB0aGUgcG9saWN5IHJhdGlvIM+AX864KGF8cykvz4BfcmVmKGF8cykgcGxheXMgdGhlIHJvbGUgb2YgYW4gaW1wb3J0YW5jZSB3ZWlnaHQuIFBQTyBjbGlwcyB0aGlzIHJhdGlvIHRvIFsx4oiSzrUsIDErzrVdIGZvciB0aGUgc2FtZSByZWFzb24g4oCUIHByZXZlbnRpbmcgdmFyaWFuY2UgZXhwbG9zaW9uIHdoZW4gdGhlIHBvbGljeSBkcmlmdHMgZmFyIGZyb20gdGhlIHJlZmVyZW5jZSwgYXQgdGhlIGNvc3Qgb2YgaW50cm9kdWNpbmcgYSBzbWFsbCBiaWFzIGluIHRoZSBncmFkaWVudCBlc3RpbWF0ZS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5IGltcG9ydCBzdGF0c1xuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgVmFyaWFuY2UgZXhwbG9zaW9uOiBwcm9wb3NhbCBoYXMgbGlnaHRlciB0YWlscyB0aGFuIHRhcmdldFxuIyBUYXJnZXQgcDogdCgzKSAoaGVhdnkgdGFpbHMpLCBQcm9wb3NhbCBxOiBOKDAsMSkgKGxpZ2h0IHRhaWxzKVxuIyBFX3BbWF4yXSA9IGRmLyhkZi0yKSA9IDMuMCBmb3IgdCgzKVxudHJ1ZV92YWwgPSAzLjBcbk4gPSAyMDAwXG5cbnByaW50KFwiPT09IFZhcmlhbmNlIEV4cGxvc2lvbjogcSAoTm9ybWFsKSBsaWdodGVyIHRoYW4gcCAodCgzKSkgPT09XCIpXG5mb3IgcnVuIGluIHJhbmdlKDQpOlxuICAgIHggPSBybmcuc3RhbmRhcmRfbm9ybWFsKE4pXG4gICAgbG9nX3cgPSBzdGF0cy50LmxvZ3BkZih4LCBkZj0zKSAtIHN0YXRzLm5vcm0ubG9ncGRmKHgsIDAsIDEpXG4gICAgdyA9IG5wLmV4cChsb2dfdylcbiAgICBlc3MgPSB3LnN1bSgpKioyIC8gbnAuc3VtKHcqKjIpXG4gICAgZXN0ID0gbnAuc3VtKHgqKjIgKiB3IC8gdy5zdW0oKSlcbiAgICBwcmludChmXCIgIFJ1biB7cnVuKzF9OiBTTklTPXtlc3Q6Ny4yZn0gIEVTUz17ZXNzOjYuMGZ9ICBtYXhfbG9ndz17bnAubG9nKHcubWF4KCkpOjYuMmZ9XCIpXG5cbnByaW50KFwiXFxuPT09IFdlaWdodCBDbGlwcGluZyBCaWFzLVZhcmlhbmNlIFRyYWRlb2ZmID09PVwiKVxueCA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoTilcbmxvZ193ID0gc3RhdHMudC5sb2dwZGYoeCwgZGY9MykgLSBzdGF0cy5ub3JtLmxvZ3BkZih4LCAwLCAxKVxudyA9IG5wLmV4cChsb2dfdylcbmZvciBjIGluIFtucC5pbmYsIDUwLjAsIDEwLjAsIDUuMCwgMi4wXTpcbiAgICB3X2NsaXBwZWQgPSBucC5taW5pbXVtKHcsIGMpXG4gICAgd19ub3JtICAgID0gd19jbGlwcGVkIC8gd19jbGlwcGVkLnN1bSgpXG4gICAgZXN0ICAgICAgID0gbnAuc3VtKHgqKjIgKiB3X25vcm0pXG4gICAgZXNzICAgICAgID0gMSAvIG5wLnN1bSh3X25vcm0qKjIpXG4gICAgY19zdHIgPSBmXCJ7YzouMGZ9XCIgaWYgYyAhPSBucC5pbmYgZWxzZSBcIm5vbmVcIlxuICAgIHByaW50KGZcIiAgY2xpcD17Y19zdHI6PjV9OiBTTklTPXtlc3Q6LjRmfSAgRVNTPXtlc3M6LjBmfSAgYmlhcz17YWJzKGVzdC10cnVlX3ZhbCk6LjRmfVwiKVxuXG5wcmludChcIlxcbj09PSBDb3JyZWN0OiBxID0gdCgzKSA9IHRhcmdldCA9PT1cIilcbnhfZ29vZCA9IHJuZy5zdGFuZGFyZF90KDMsIE4pXG53X2dvb2QgPSBucC5vbmVzKE4pICAgIyBhbGwgd2VpZ2h0cyA9IDFcbmVzc19nb29kID0gTlxucHJpbnQoZlwiICBTTklTPXtucC5tZWFuKHhfZ29vZCoqMik6LjRmfSAgRVNTPXtlc3NfZ29vZH0gIChhbGwgd2VpZ2h0cyBlcXVhbClcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJPZmYtUG9saWN5IFJMIGFuZCBSTEhGIEFwcGxpY2F0aW9ucyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkltcG9ydGFuY2Ugc2FtcGxpbmcgaXMgY2VudHJhbCB0byBvZmYtcG9saWN5IHJlaW5mb3JjZW1lbnQgbGVhcm5pbmc6IHdlIHdhbnQgdG8gZXZhbHVhdGUgYSB0YXJnZXQgcG9saWN5IM+AX864IHVzaW5nIHRyYWplY3RvcmllcyBjb2xsZWN0ZWQgYnkgYSBiZWhhdmlvdXIgcG9saWN5IM+AX2IuIFRoZSBJUyBjb3JyZWN0aW9uIGZvciBhIFQtc3RlcCB0cmFqZWN0b3J5IM+EID0gKHPigoAsYeKCgCzigKYsc+KCnCkgaXM6XG5cbs+BKM+EKSA9IM6g4oKcIM+AX864KGHigpx8c+KCnCkgLyDPgF9iKGHigpx8c+KCnClcblxuRm9yIGxvbmcgdHJhamVjdG9yaWVzLCDPgSjPhCkgaXMgYSBwcm9kdWN0IG9mIFQgcmF0aW9zIOKAlCBpdCBjYW4gaGF2ZSBleHBvbmVudGlhbGx5IGdyb3dpbmcgdmFyaWFuY2UuIFBlci1kZWNpc2lvbiBJUyB1c2VzIHBhcnRpYWwgcHJvZHVjdHMgz4HigpwgPSDOoF97dCfiiaR0fSDPgF/OuChh4oKcJ3xz4oKcJykgLyDPgF9iKGHigpwnfHPigpwnKSB0aGF0IHJlZHVjZSB2YXJpYW5jZSBzaWduaWZpY2FudGx5LlxuXG5JbiBSTEhGIHdpdGggUFBPOiB0aGUgZmluZS10dW5lZCBwb2xpY3kgz4BfzrggZ2VuZXJhdGVzIHJlc3BvbnNlczsgdGhlIHJld2FyZCBtb2RlbCBzY29yZXMgdGhlbTsgdGhlIFBQTyBsb3NzIGNsaXBzIHRoZSByYXRpbyByX3QgPSDPgF/OuChh4oKcfHPigpwpL8+AX29sZChh4oKcfHPigpwpIHRvIFsx4oiSzrUsIDErzrVdIGF0IGVhY2ggdG9rZW4uIFRoaXMgaXMgd2VpZ2h0IGNsaXBwaW5nIGFwcGxpZWQgcGVyLXRva2VuIGluIHRoZSB0cmFqZWN0b3J5LCBwcmV2ZW50aW5nIGFueSBzaW5nbGUgdXBkYXRlIGZyb20gbW92aW5nIHRoZSBwb2xpY3kgdG9vIGZhciBmcm9tIHRoZSByZWZlcmVuY2UuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgT2ZmLXBvbGljeSBJUzogZXZhbHVhdGUgdGFyZ2V0IHBvbGljeSB1c2luZyBiZWhhdmlvdXItcG9saWN5IHRyYWplY3Rvcmllc1xubl9zdGF0ZXMsIG5fYWN0aW9ucyA9IDUsIDJcbnBpX3RhcmdldCAgID0gbnAuYXJyYXkoW1swLjcsIDAuM11dICogbl9zdGF0ZXMpICAjIHRhcmdldDogYmlhc2VkIHRvd2FyZCBhY3Rpb24gMFxucGlfYmVoYXZpb3IgPSBucC5hcnJheShbWzAuNSwgMC41XV0gKiBuX3N0YXRlcykgICMgYmVoYXZpb3I6IHVuaWZvcm1cblxuZGVmIHJ1bl9lcGlzb2RlKHBpLCBtYXhfc3RlcHM9OCk6XG4gICAgcyA9IHJuZy5pbnRlZ2VycyhuX3N0YXRlcylcbiAgICB0cmFqLCBHID0gW10sIDAuMFxuICAgIGZvciBfIGluIHJhbmdlKG1heF9zdGVwcyk6XG4gICAgICAgIGEgPSBybmcuY2hvaWNlKG5fYWN0aW9ucywgcD1waVtzXSlcbiAgICAgICAgciA9IHJuZy5zdGFuZGFyZF9ub3JtYWwoKVxuICAgICAgICB0cmFqLmFwcGVuZCgocywgYSwgcikpOyBHICs9IHJcbiAgICAgICAgcyA9IHJuZy5pbnRlZ2VycyhuX3N0YXRlcylcbiAgICByZXR1cm4gdHJhaiwgR1xuXG5uX2VwID0gMjAwMFxuaXNfcmV0dXJucywgZGlyZWN0X3JldHVybnMgPSBbXSwgW11cbmZvciBfIGluIHJhbmdlKG5fZXApOlxuICAgIHRyYWosIF8gPSBydW5fZXBpc29kZShwaV9iZWhhdmlvcilcbiAgICAjIFRyYWplY3RvcnkgSVMgd2VpZ2h0IChwcm9kdWN0IG9mIHBlci1zdGVwIHJhdGlvcylcbiAgICBsb2dfcmhvID0gc3VtKG5wLmxvZyhwaV90YXJnZXRbcyxhXSkgLSBucC5sb2cocGlfYmVoYXZpb3JbcyxhXSkgZm9yIHMsYSxyIGluIHRyYWopXG4gICAgcmhvID0gbnAuZXhwKG5wLmNsaXAobG9nX3JobywgLTEwLCAxMCkpICAgIyBjbGlwIGZvciBudW1lcmljYWwgc2FmZXR5XG4gICAgRyA9IHN1bShyIGZvciBfLF8sciBpbiB0cmFqKVxuICAgIGlzX3JldHVybnMuYXBwZW5kKEcgKiByaG8pXG4gICAgZGlyZWN0X3JldHVybnMuYXBwZW5kKEcpXG5cbnRydWVfcmV0dXJucyA9IFtydW5fZXBpc29kZShwaV90YXJnZXQpWzFdIGZvciBfIGluIHJhbmdlKG5fZXApXVxuXG5wcmludChcIj09PSBPZmYtUG9saWN5IFZhbHVlIEVzdGltYXRpb24gPT09XCIpXG5wcmludChmXCJOYWl2ZSAoYmVoYXZpb3IgcG9saWN5KTogICB7bnAubWVhbihkaXJlY3RfcmV0dXJucyk6LjRmfSBTRT17bnAuc3RkKGRpcmVjdF9yZXR1cm5zKS9ucC5zcXJ0KG5fZXApOi40Zn1cIilcbnByaW50KGZcIklTLWNvcnJlY3RlZDogICAgICAgICAgICAgIHtucC5tZWFuKGlzX3JldHVybnMpOi40Zn0gU0U9e25wLnN0ZChpc19yZXR1cm5zKS9ucC5zcXJ0KG5fZXApOi40Zn1cIilcbnByaW50KGZcIlRydWUgKHRhcmdldCBwb2xpY3kpOiAgICAgIHtucC5tZWFuKHRydWVfcmV0dXJucyk6LjRmfSBTRT17bnAuc3RkKHRydWVfcmV0dXJucykvbnAuc3FydChuX2VwKTouNGZ9XCIpXG5cbiMgUFBPLXN0eWxlIHJhdGlvIGNsaXBwaW5nIHNpbXVsYXRpb25cbnByaW50KFwiXFxuPT09IFBQTyBSYXRpbyBDbGlwcGluZyAoZXBzPTAuMikgPT09XCIpXG5sb2dfcmF0aW9zID0gW3N1bShucC5sb2cocGlfdGFyZ2V0W3MsYV0pLW5wLmxvZyhwaV9iZWhhdmlvcltzLGFdKSBmb3IgcyxhLHIgaW4gcnVuX2VwaXNvZGUocGlfYmVoYXZpb3IpWzBdKVxuICAgICAgICAgICAgICBmb3IgXyBpbiByYW5nZSg1MDApXVxucmF0aW9zID0gbnAuZXhwKG5wLmFycmF5KGxvZ19yYXRpb3MpKVxuZXBzID0gMC4yXG5jbGlwcGVkID0gbnAuY2xpcChyYXRpb3MsIDEtZXBzLCAxK2VwcylcbnBjdF9jbGlwcGVkID0gbnAubWVhbigocmF0aW9zIDwgMS1lcHMpIHwgKHJhdGlvcyA+IDErZXBzKSkgKiAxMDBcbnByaW50KGZcIlVuY2xpcHBlZCByYXRpb3M6IG1pbj17cmF0aW9zLm1pbigpOi4zZn0gbWVhbj17cmF0aW9zLm1lYW4oKTouM2Z9IG1heD17cmF0aW9zLm1heCgpOi4zZn1cIilcbnByaW50KGZcIkNsaXBwZWQgcmF0aW9zOiAgIG1pbj17Y2xpcHBlZC5taW4oKTouM2Z9IG1lYW49e2NsaXBwZWQubWVhbigpOi4zZn0gbWF4PXtjbGlwcGVkLm1heCgpOi4zZn1cIilcbnByaW50KGZcIntwY3RfY2xpcHBlZDouMWZ9JSBvZiB0cmFqZWN0b3JpZXMgaGFkIHJhdGlvcyBvdXRzaWRlIFsxLWVwcywgMStlcHNdXCIpIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQW5uZWFsZWQgSW1wb3J0YW5jZSBTYW1wbGluZyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkFubmVhbGVkIGltcG9ydGFuY2Ugc2FtcGxpbmcgKEFJUykgZXN0aW1hdGVzIHRoZSByYXRpbyBvZiBwYXJ0aXRpb24gZnVuY3Rpb25zIFrigoEvWuKCgCDigJQgYSBxdWFudGl0eSBuZWVkZWQgZm9yIEJheWVzaWFuIG1vZGVsIGNvbXBhcmlzb24sIG5vcm1hbGlzaW5nIGZsb3cgbGlrZWxpaG9vZCBldmFsdWF0aW9uLCBhbmQgZW5lcmd5LWJhc2VkIG1vZGVsIHRyYWluaW5nLiBJdCBicmlkZ2VzIGJldHdlZW4gYW4gZWFzeSBwcm9wb3NhbCBw4oKAIGFuZCBhIGhhcmQgdGFyZ2V0IHDigoEgdGhyb3VnaCBhIHNlcXVlbmNlIG9mIGludGVybWVkaWF0ZSBkaXN0cmlidXRpb25zOlxuXG5wX3QoeCkg4oidIHDigoAoeCleezEtzrLigpx9IHDigoEoeClee86y4oKcfSwgIM6y4oKAPTAsIM6y4oKBPTEsIM6y4oKAIDwgzrLigoEgPCDigKYgPCDOsuKCmSA9IDFcblxuVGhlIElTIHdlaWdodCBmb3IgYSBjaGFpbiB44oKAIOKGkiB44oKBIOKGkiDigKYg4oaSIHjigpkgKHdoZXJlIGVhY2ggeOKCnCBpcyBwcm9kdWNlZCBieSBhIHRyYW5zaXRpb24ga2VybmVsIHRhcmdldGluZyBw4oKcKSBpczpcblxudyA9IM6g4oKcIHDigpwoeOKCnOKCi+KCgSkgLyBwX3t0LTF9KHjigpzigovigoEpXG5cbkFJUyB3aXRoIG1hbnkgaW50ZXJtZWRpYXRlIHN0ZXBzIChsYXJnZSBUKSBnaXZlcyBzbWFsbCB2YXJpYW5jZSBhbmQgcmVsaWFibGUgcGFydGl0aW9uIGZ1bmN0aW9uIGVzdGltYXRlcy4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5IGltcG9ydCBzdGF0c1xuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5cbiMgQW5uZWFsZWQgSVM6IGVzdGltYXRlIFpfMS9aXzAgd2hlcmUgcF8wPU4oMCwxKSwgcF8xPU4oMywwLjVeMilcbiMgVHJ1ZSByYXRpbzogWl8xL1pfMCA9IDEgKGJvdGggYXJlIHByb3BlciBHYXVzc2lhbnMpXG4jIEJ1dCBBSVMgZXN0aW1hdGVzIEVfe3BfMX1bZl0gPSBpbnRlZ3JhbCBmKHgpIHBfMSh4KSBkeCAvIFpfMVxuIyBNb3JlIHVzZWZ1bDogQUlTIHRvIGVzdGltYXRlIG5vcm1hbGlzaW5nIGNvbnN0YW50IG9mIHVubm9ybWFsaXNlZCB0YXJnZXRcblxubXVfdGFyZ2V0LCBzaWdtYV90YXJnZXQgPSAzLjAsIDAuNVxuXG5kZWYgbG9nX3AwKHgpOiAgIyBwcm9wb3NhbDogTigwLDEpXG4gICAgcmV0dXJuIHN0YXRzLm5vcm0ubG9ncGRmKHgsIDAsIDEpXG5cbmRlZiBsb2dfcDEoeCk6ICAjIHRhcmdldDogTigzLDAuNSkgKHVubm9ybWFsaXNlZCBpbiBnZW5lcmFsIGNhc2UpXG4gICAgcmV0dXJuIHN0YXRzLm5vcm0ubG9ncGRmKHgsIG11X3RhcmdldCwgc2lnbWFfdGFyZ2V0KVxuXG5kZWYgbG9nX3B0KHgsIGJldGEpOiAgIyBpbnRlcm1lZGlhdGU6IGdlb21ldHJpYyBhdmVyYWdlXG4gICAgcmV0dXJuICgxLWJldGEpKmxvZ19wMCh4KSArIGJldGEqbG9nX3AxKHgpXG5cbmRlZiBhaXNfZXN0aW1hdGUobl9zYW1wbGVzPTUwMCwgbl9zdGVwcz0yMCk6XG4gICAgXCJcIlwiQW5uZWFsZWQgSVMgd2l0aCBHYXVzc2lhbiBNQ01DIHRyYW5zaXRpb25zLlwiXCJcIlxuICAgIGJldGFzID0gbnAubGluc3BhY2UoMCwgMSwgbl9zdGVwcyArIDEpXG4gICAgbG9nX3dlaWdodHMgPSBucC56ZXJvcyhuX3NhbXBsZXMpXG5cbiAgICAjIFN0YXJ0IGZyb20gcHJvcG9zYWxcbiAgICB4ID0gcm5nLnN0YW5kYXJkX25vcm1hbChuX3NhbXBsZXMpXG5cbiAgICBmb3IgdCBpbiByYW5nZSgxLCBsZW4oYmV0YXMpKTpcbiAgICAgICAgYmV0YV9wcmV2LCBiZXRhX2N1cnIgPSBiZXRhc1t0LTFdLCBiZXRhc1t0XVxuICAgICAgICAjIEFJUyB3ZWlnaHQgY29udHJpYnV0aW9uOiBwX3QoeCkgLyBwX3t0LTF9KHgpXG4gICAgICAgIGxvZ193ZWlnaHRzICs9IGxvZ19wdCh4LCBiZXRhX2N1cnIpIC0gbG9nX3B0KHgsIGJldGFfcHJldilcbiAgICAgICAgIyBNQ01DIHRyYW5zaXRpb246IE1ldHJvcG9saXMgc3RlcCB0YXJnZXRpbmcgcF9jdXJyXG4gICAgICAgIHhfcHJvcCA9IHggKyBybmcubm9ybWFsKDAsIDAuNSwgbl9zYW1wbGVzKVxuICAgICAgICBsb2dfYWxwaGEgPSBsb2dfcHQoeF9wcm9wLCBiZXRhX2N1cnIpIC0gbG9nX3B0KHgsIGJldGFfY3VycilcbiAgICAgICAgYWNjZXB0ID0gbnAubG9nKHJuZy51bmlmb3JtKHNpemU9bl9zYW1wbGVzKSkgPCBsb2dfYWxwaGFcbiAgICAgICAgeFthY2NlcHRdID0geF9wcm9wW2FjY2VwdF1cblxuICAgICMgQUlTIGVzdGltYXRlOiBFX3AxW1heMl0gPSBzdW0oWF4yICogdykgLyBzdW0odylcbiAgICBsb2dfd19ub3JtYWxpc2VkID0gbG9nX3dlaWdodHMgLSBucC5sb2dhZGRleHAucmVkdWNlKGxvZ193ZWlnaHRzKVxuICAgIHdfbm9ybSA9IG5wLmV4cChsb2dfd19ub3JtYWxpc2VkKVxuICAgIEVfeDIgICA9IG5wLnN1bSh4KioyICogd19ub3JtKVxuICAgIGVzcyAgICA9IG5wLmV4cCgtbnAubG9nYWRkZXhwLnJlZHVjZSgyICogbG9nX3dfbm9ybWFsaXNlZCkpXG4gICAgcmV0dXJuIEVfeDIsIGVzc1xuXG5wcmludChcIj09PSBBbm5lYWxlZCBJUzogRXN0aW1hdGUgRV9wMVtYXjJdID09PVwiKVxucHJpbnQoZlwiVHJ1ZSB2YWx1ZToge211X3RhcmdldCoqMiArIHNpZ21hX3RhcmdldCoqMjouNGZ9XCIpXG5mb3IgVCBpbiBbNSwgMjAsIDEwMF06XG4gICAgZXN0aW1hdGVzID0gW2Fpc19lc3RpbWF0ZShuX3NhbXBsZXM9MjAwLCBuX3N0ZXBzPVQpIGZvciBfIGluIHJhbmdlKDUpXVxuICAgIGVzdHMgPSBbZVswXSBmb3IgZSBpbiBlc3RpbWF0ZXNdOyBlc3NzID0gW2VbMV0gZm9yIGUgaW4gZXN0aW1hdGVzXVxuICAgIHByaW50KGZcIiAgVD17VDo+NH0gc3RlcHM6IG1lYW49e25wLm1lYW4oZXN0cyk6LjRmfSBzdGQ9e25wLnN0ZChlc3RzKTouNGZ9IGF2Z19FU1M9e25wLm1lYW4oZXNzcyk6LjBmfVwiKSJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIlBpdGZhbGxzIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQ3JpdGljYWwgSVMgZmFpbHVyZSBtb2RlczpcblxuMS4gKipUYWlsIG1pc21hdGNoIGNhdXNpbmcgaW5maW5pdGUgdmFyaWFuY2UqKjogaWYgcSh4KSA9IDAgYW55d2hlcmUgcCh4KSA+IDAsIHRoZSBlc3RpbWF0b3IgaXMgdW5kZWZpbmVkLiBJZiBxIGhhcyBsaWdodGVyIHRhaWxzIHRoYW4gcCwgdmFyaWFuY2UgaXMgaW5maW5pdGUg4oCUIG5vIGFtb3VudCBvZiBzYW1wbGVzIGZpeGVzIHRoaXMuXG5cbjIuICoqTG9uZyB0cmFqZWN0b3J5IElTIHByb2R1Y3QgY29sbGFwc2UqKjogzqDigpwgcChh4oKcKS9xKGHigpwpIG92ZXIgVCBzdGVwcyBoYXMgdmFyaWFuY2UgdGhhdCBncm93cyBleHBvbmVudGlhbGx5IHdpdGggVC4gUGVyLWRlY2lzaW9uIElTLCBWLXRyYWNlLCBvciBjbGlwcGluZyBhcmUgZXNzZW50aWFsIGZvciBsb25nLWhvcml6b24gcHJvYmxlbXMuXG5cbjMuICoqQ29tcHV0aW5nIHdlaWdodHMgaW4gbGluZWFyIHNwYWNlKio6IGZvciBldmVuIG1vZGVyYXRlbHkgZGlmZmVyZW50IGRpc3RyaWJ1dGlvbnMsIHdlaWdodHMgY2FuIGJlIGFzdHJvbm9taWNhbCBvciB6ZXJvLiBBbHdheXMgY29tcHV0ZSBsb2dfdyA9IGxvZyBwKHgpIOKIkiBsb2cgcSh4KSBhbmQgb25seSBleHBvbmVudGlhdGUgYXQgdGhlIGZpbmFsIHN0ZXAuXG5cbjQuICoqSWdub3JpbmcgRVNTIGFzIGEgcXVhbGl0eSBtZXRyaWMqKjogSVMgZXN0aW1hdGVzIGNhbiBsb29rIG51bWVyaWNhbGx5IHN0YWJsZSB3aGlsZSBoYXZpbmcgZXh0cmVtZWx5IGhpZ2ggdmFyaWFuY2UuIEFsd2F5cyBjb21wdXRlIEVTUy9OOyBiZWxvdyAwLjEgaXMgYSByZWQgZmxhZyByZXF1aXJpbmcgYSBiZXR0ZXIgcHJvcG9zYWwgb3IgZmV3ZXIgSVMgY29ycmVjdGlvbiBzdGVwcy4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQcmFjdGljYWwgR3VpZGFuY2UifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJHdWlkZWxpbmVzIGZvciByZWxpYWJsZSBJUyBpbiBNTDpcblxuLSAqKkFsd2F5cyB3b3JrIGluIGxvZy1zcGFjZSoqOiBsb2dfdyA9IGxvZyBwKHgpIOKIkiBsb2cgcSh4KSwgdGhlbiB3ID0gZXhwKGxvZ193IOKIkiBsb2dfdy5tYXgoKSkgZm9yIHN0YWJpbGl0eS5cbi0gKipNb25pdG9yIEVTUy9OKio6IGZsYWcgZXN0aW1hdGVzIHdoZXJlIEVTUy9OIDwgMC4xIGFzIHVucmVsaWFibGUuXG4tICoqV2VpZ2h0IGNsaXBwaW5nKio6IGNhcCB3ZWlnaHRzIGF0IGEgcGVyY2VudGlsZSAoZS5nLiwgOTV0aCBwZXJjZW50aWxlIG9mIHdlaWdodCBkaXN0cmlidXRpb24pIG9yIGF0IGEgZml4ZWQgY29uc3RhbnQuIFRoaXMgaXMgYWx3YXlzIGEgZ29vZCBkZWZhdWx0IGZvciBwcm9kdWN0aW9uIElTLlxuLSAqKkZvciBvZmYtcG9saWN5IFJMKio6IHVzZSBWLXRyYWNlIChwZXItc3RlcCByYXRpbyBjbGlwcGluZykgaW5zdGVhZCBvZiBmdWxsIHRyYWplY3RvcnkgSVMuIFYtdHJhY2UgY2xpcHMgZWFjaCByYXRpbyB0byDPgcyEIGFuZCBjzIQgc2VwYXJhdGVseSBmb3IgdmFyaWFuY2UgYW5kIGJpYXMgY29udHJvbC5cbi0gKipGb3IgUkxIRioqOiBQUE8ncyByYXRpbyBjbGlwcGluZyB0byBbMeKIks61LCAxK861XSBpcyB3ZWlnaHQgY2xpcHBpbmcgYXBwbGllZCBwZXIgdG9rZW4uIFRoZSBLTCBwZW5hbHR5IGluIERQTyBpcyBhbiBhbHRlcm5hdGl2ZSB0aGF0IGF2b2lkcyBleHBsaWNpdCBJUyBjb3JyZWN0aW9uLiJ9LCB7InR5cGUiOiAiY2FsbG91dCIsICJ2YXJpYW50IjogIndhcm5pbmciLCAidGl0bGUiOiAiRVNTIDwgMTAlIEluZGljYXRlcyBTZXZlcmUgSVMgRmFpbHVyZSIsICJjb250ZW50IjogIldoZW4gRVNTL04gPCAwLjEsIGZld2VyIHRoYW4gMTAlIG9mIHNhbXBsZXMgZWZmZWN0aXZlbHkgY29udHJpYnV0ZSB0byB0aGUgZXN0aW1hdGUuIFRoZSB0b3AgZmV3IHNhbXBsZXMgZG9taW5hdGUsIG1ha2luZyB0aGUgZXN0aW1hdGUgdW5yZWxpYWJsZSBhbmQgaGlnaC12YXJpYW5jZS4gUmVtZWRpZXM6ICgxKSB1c2UgYSBoZWF2aWVyLXRhaWxlZCBwcm9wb3NhbDsgKDIpIHJlZHVjZSB0aGUgSVMgY29ycmVjdGlvbiBkaXN0YW5jZSAoc3RheSBjbG9zZXIgdG8gb24tcG9saWN5KTsgKDMpIHVzZSBhbm5lYWxlZCBJUyB0byBicmlkZ2UgZ3JhZHVhbGx5OyAoNCkgdXNlIG5vcm1hbGlzaW5nIGZsb3dzIHRvIGxlYXJuIGEgYmV0dGVyIHByb3Bvc2FsIGRpc3RyaWJ1dGlvbi4ifSwgeyJ0eXBlIjogImNhbGxvdXQiLCAidmFyaWFudCI6ICJ0aXAiLCAidGl0bGUiOiAiT3B0aW1hbCBQcm9wb3NhbCBNaW5pbWlzZXMgSVMgVmFyaWFuY2UiLCAiY29udGVudCI6ICJUaGUgdmFyaWFuY2UtbWluaW1pc2luZyBJUyBwcm9wb3NhbCBpcyBxKih4KSDiiJ0gfGYoeCl8IHAoeCkg4oCUIGl0IGNvbmNlbnRyYXRlcyBzYW1wbGVzIHdoZXJlIHRoZSBpbnRlZ3JhbmQgaXMgbGFyZ2UuIEZvciBmKHgpIOKJpSAwIChlLmcuLCBwb3NpdGl2ZSByZXdhcmQgZnVuY3Rpb25zKSwgcSooeCkg4oidIGYoeCkgcCh4KSBpcyBwcm9wb3J0aW9uYWwgdG8gdGhlIHVubm9ybWFsaXNlZCB0YXJnZXQgbXVsdGlwbGllZCBieSB0aGUgZnVuY3Rpb24gdmFsdWUuIEluIFJMLCB0aGlzIGlzIHRoZSBtb3RpdmF0aW9uIGZvciBleHBlcmllbmNlIHJlcGxheSBwcmlvcml0aXNhdGlvbjogc2FtcGxlIHRyYW5zaXRpb25zIHByb3BvcnRpb25hbGx5IHRvIHzOtHwgKFREIGVycm9yKSwgdGhlbiBjb3JyZWN0IHdpdGggSVMgd2VpZ2h0cy4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIk1ldGhvZCIsICJJUyBDb3JyZWN0aW9uIiwgIkFwcGxpY2F0aW9uIiwgIlZhcmlhbmNlIENvbnRyb2wiXSwgInJvd3MiOiBbWyJWYW5pbGxhIElTIiwgIkZ1bGwgcmF0aW8gcC9xIiwgIlNpbXBsZSBleHBlY3RhdGlvbnMiLCAiQ2FuIGJlIGluZmluaXRlIl0sIFsiU05JUyIsICJOb3JtYWxpc2VkIHdlaWdodHMiLCAiVW5rbm93biBub3JtYWxpc2luZyBjb25zdGFudHMiLCAiQmlhc2VkLCBmaW5pdGUiXSwgWyJQZXItZGVjaXNpb24gSVMiLCAiUGFydGlhbCBwcm9kdWN0cyIsICJPZmYtcG9saWN5IFJMIHZhbHVlIGVzdGltYXRpb24iLCAiTG93ZXIgdGhhbiBmdWxsIElTIl0sIFsiVi10cmFjZSIsICJDbGlwcGVkIHBlci1zdGVwIHJhdGlvcyIsICJPZmYtcG9saWN5IGFjdG9yLWNyaXRpYyAoSU1QQUxBKSIsICJDb250cm9sbGVkLCBib3VuZGVkIl0sIFsiUFBPIiwgIkNsaXBwZWQgcG9saWN5IHJhdGlvIHBlciB0b2tlbiIsICJSTEhGIGZpbmUtdHVuaW5nIiwgIkxvdyAobmVhci1vbi1wb2xpY3kpIl0sIFsiQUlTIiwgIkFubmVhbGVkIHNlcXVlbmNlIiwgIlBhcnRpdGlvbiBmdW5jdGlvbiBlc3RpbWF0aW9uIiwgIlZlcnkgbG93IChtYW55IHN0ZXBzKSJdXX0sIHsidHlwZSI6ICJkaXZpZGVyIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiS2V5IFRha2Vhd2F5cyJ9LCB7InR5cGUiOiAibGlzdCIsICJvcmRlcmVkIjogZmFsc2UsICJpdGVtcyI6IFsiSVMgZXN0aW1hdG9yIMOKX3BbZl0gPSAoMS9OKSDOoyBmKHjhtaIpdyh44bWiKSB3aXRoIHjhtaJ+cSBhbmQgdz1wL3EgY29ycmVjdHMgZm9yIHNhbXBsaW5nIGZyb20gdGhlIHdyb25nIGRpc3RyaWJ1dGlvbi4iLCAiU05JUyBub3JtYWxpc2VzIHdlaWdodHMgdG8gc3VtIHRvIDEsIGVuYWJsaW5nIHVzZSB3aXRoIHVubm9ybWFsaXNlZCBwIChzdGFuZGFyZCBpbiBCYXllc2lhbiBpbmZlcmVuY2UpIOKAlCBiaWFzZWQgYnV0IGNvbnNpc3RlbnQuIiwgIkVTUyA9ICjOo3fhtaIpwrIvzqN34bWiwrIgbWVhc3VyZXMgZWZmaWNpZW5jeTsgRVNTL04gPCAwLjEgaW5kaWNhdGVzIHNldmVyZSB3ZWlnaHQgaW1iYWxhbmNlIGFuZCB1bnJlbGlhYmxlIGVzdGltYXRlcy4iLCAiSVMgaGFzIGZpbml0ZSB2YXJpYW5jZSBvbmx5IGlmIHEgaGFzIGhlYXZpZXIgdGFpbHMgdGhhbiBwIGV2ZXJ5d2hlcmU7IHRhaWwgbWlzbWF0Y2ggY2F1c2VzIGluZmluaXRlIHZhcmlhbmNlIHRoYXQgZXh0cmEgc2FtcGxlcyBjYW5ub3QgZml4LiIsICJXZWlnaHQgY2xpcHBpbmcgKHRydW5jYXRpb24pIGF0IGNvbnN0YW50IGMgdHJhZGVzIGJpYXMgZm9yIHZhcmlhbmNlIHJlZHVjdGlvbiDigJQgdGhlIHByaW5jaXBsZSBiZWhpbmQgUFBPJ3MgcmF0aW8gY2xpcHBpbmcgaW4gUkxIRi4iLCAiQWx3YXlzIGNvbXB1dGUgaW1wb3J0YW5jZSB3ZWlnaHRzIGluIGxvZy1zcGFjZSAobG9nIHAg4oiSIGxvZyBxKSBhbmQgb25seSBleHBvbmVudGlhdGUgYXQgdGhlIGZpbmFsIHN0ZXAgdG8gYXZvaWQgbnVtZXJpY2FsIG92ZXJmbG93LiIsICJBbm5lYWxlZCBJUyBicmlkZ2VzIGJldHdlZW4gYSBzaW1wbGUgcHJvcG9zYWwgYW5kIGEgaGFyZCB0YXJnZXQgdGhyb3VnaCBpbnRlcm1lZGlhdGUgZGlzdHJpYnV0aW9ucywgZW5hYmxpbmcgcmVsaWFibGUgcGFydGl0aW9uIGZ1bmN0aW9uIGVzdGltYXRpb24uIl19XQ=="
---
# Importance Sampling

Importance sampling (IS) solves a fundamental problem: estimating expectations under a target distribution p when samples can only be drawn from a different proposal distribution q. This arises constantly in ML — computing expectations under a complex posterior when only a simple distribution is sampleable, correcting for distributional shift between training and deployment, evaluating policies trained on different data, and fine-tuning language models with RLHF where reference and fine-tuned distributions diverge. IS is also the foundation of Sequential Monte Carlo, annealed importance sampling for partition function estimation, and policy gradient variance reduction through baseline subtraction.

## Core Definition — The IS Estimator

Goal: estimate E_p[f(X)] = ∫ f(x) p(x) dx but we can only sample from q(x).

Key algebraic identity:
E_p[f(X)] = ∫ f(x) p(x) dx = ∫ f(x) [p(x)/q(x)] q(x) dx = E_q[f(X) w(X)]

where w(x) = p(x)/q(x) are the importance weights. Requirements: q must have support everywhere p is positive (q(x) > 0 whenever p(x) > 0).

IS estimator (unnormalised):
Ê_IS[f] = (1/N) Σᵢ f(xᵢ) w(xᵢ),  xᵢ ~ q

Self-normalised IS (SNIS) — does not require knowing the normalisation constant of p:
Ê_SNIS[f] = Σᵢ f(xᵢ) w̃ᵢ  where w̃ᵢ = wᵢ / Σⱼ wⱼ

SNIS is biased but consistent (bias O(1/N)). It is preferred when p is known only up to a normalising constant, which is the common case in Bayesian inference.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Target p: N(3, 0.5^2); Proposal q: N(0, 2^2)
# Goal: E_p[X^2] = mu^2 + sigma^2 = 9.25
mu_p, sigma_p = 3.0, 0.5
mu_q, sigma_q = 0.0, 2.0
true_val = mu_p**2 + sigma_p**2  # 9.25

N = 5000
x = rng.normal(mu_q, sigma_q, N)  # sample from q

# Compute log importance weights (always work in log-space!)
log_w = stats.norm.logpdf(x, mu_p, sigma_p) - stats.norm.logpdf(x, mu_q, sigma_q)
w = np.exp(log_w)

# Unnormalised IS (requires p to be normalised)
is_est   = np.mean(x**2 * w)

# Self-normalised IS (works with unnormalised p)
w_norm   = w / w.sum()
snis_est = np.sum(x**2 * w_norm)

# Effective sample size: ESS = (sum w)^2 / sum(w^2)
ess = w.sum()**2 / np.sum(w**2)

print(f"True E_p[X^2]:     {true_val:.4f}")
print(f"IS estimate:       {is_est:.4f}  (requires normalised p)")
print(f"SNIS estimate:     {snis_est:.4f}  (works with unnormalised p)")
print(f"ESS: {ess:.1f} / {N}  ({100*ess/N:.1f}%)")

# Weight diagnostics
w_norm_sorted = np.sort(w_norm)[::-1]
cumsum = np.cumsum(w_norm_sorted)
n_50pct = np.searchsorted(cumsum, 0.5) + 1
print(f"Top {n_50pct} samples carry 50% of total weight (out of {N})")
print(f"Max weight: {w_norm.max():.4e}, mean weight: {w_norm.mean():.4e}")
```

## Effective Sample Size and Variance

The effective sample size (ESS) measures how many i.i.d. samples from p the IS estimate is equivalent to:

ESS = (Σᵢ wᵢ)² / Σᵢ wᵢ²

For normalised weights: ESS = 1 / Σᵢ w̃ᵢ² ∈ [1, N].

Properties:
- ESS = N when all weights are equal — this happens when q = p (perfect proposal)
- ESS = 1 when one weight dominates all others — worst case, the estimate is based on a single sample
- ESS/N measures the efficiency of IS: values above 0.5 indicate reasonable proposals; below 0.1 is problematic

Variance of the IS estimator:
Var_q[f(x) w(x)] = ∫ (f(x) w(x))² q(x) dx − (E_p[f(x)])²

This variance is finite if and only if E_q[(f(x) w(x))²] < ∞ — roughly requiring that p(x)/q(x) is bounded. If q has lighter tails than p anywhere, the ratio p/q can become unbounded and variance is infinite. The optimal IS proposal is q*(x) ∝ |f(x)| p(x), concentrating samples where the integrand is largest.

## Variance Explosion and Weight Clipping

When q has lighter tails than p, the importance weights w(x) = p(x)/q(x) → ∞ for large |x|. This causes:

1. A few samples with enormous weights dominate the estimate (ESS → 1)
2. The IS estimator has infinite variance (despite being unbiased)
3. In practice: highly variable estimates, numerical overflow in weights

Weight clipping (truncation) caps weights at a maximum value c: w̃(x) = min(w(x), c). This introduces bias — it no longer correctly estimates E_p[f] — but reduces variance substantially. The bias is O(P(w(X) > c)) which is small when c is chosen appropriately.

For RLHF: the policy ratio π_θ(a|s)/π_ref(a|s) plays the role of an importance weight. PPO clips this ratio to [1−ε, 1+ε] for the same reason — preventing variance explosion when the policy drifts far from the reference, at the cost of introducing a small bias in the gradient estimate.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Variance explosion: proposal has lighter tails than target
# Target p: t(3) (heavy tails), Proposal q: N(0,1) (light tails)
# E_p[X^2] = df/(df-2) = 3.0 for t(3)
true_val = 3.0
N = 2000

print("=== Variance Explosion: q (Normal) lighter than p (t(3)) ===")
for run in range(4):
    x = rng.standard_normal(N)
    log_w = stats.t.logpdf(x, df=3) - stats.norm.logpdf(x, 0, 1)
    w = np.exp(log_w)
    ess = w.sum()**2 / np.sum(w**2)
    est = np.sum(x**2 * w / w.sum())
    print(f"  Run {run+1}: SNIS={est:7.2f}  ESS={ess:6.0f}  max_logw={np.log(w.max()):6.2f}")

print("\n=== Weight Clipping Bias-Variance Tradeoff ===")
x = rng.standard_normal(N)
log_w = stats.t.logpdf(x, df=3) - stats.norm.logpdf(x, 0, 1)
w = np.exp(log_w)
for c in [np.inf, 50.0, 10.0, 5.0, 2.0]:
    w_clipped = np.minimum(w, c)
    w_norm    = w_clipped / w_clipped.sum()
    est       = np.sum(x**2 * w_norm)
    ess       = 1 / np.sum(w_norm**2)
    c_str = f"{c:.0f}" if c != np.inf else "none"
    print(f"  clip={c_str:>5}: SNIS={est:.4f}  ESS={ess:.0f}  bias={abs(est-true_val):.4f}")

print("\n=== Correct: q = t(3) = target ===")
x_good = rng.standard_t(3, N)
w_good = np.ones(N)   # all weights = 1
ess_good = N
print(f"  SNIS={np.mean(x_good**2):.4f}  ESS={ess_good}  (all weights equal)")
```

## Off-Policy RL and RLHF Applications

Importance sampling is central to off-policy reinforcement learning: we want to evaluate a target policy π_θ using trajectories collected by a behaviour policy π_b. The IS correction for a T-step trajectory τ = (s₀,a₀,…,sₜ) is:

ρ(τ) = Πₜ π_θ(aₜ|sₜ) / π_b(aₜ|sₜ)

For long trajectories, ρ(τ) is a product of T ratios — it can have exponentially growing variance. Per-decision IS uses partial products ρₜ = Π_{t'≤t} π_θ(aₜ'|sₜ') / π_b(aₜ'|sₜ') that reduce variance significantly.

In RLHF with PPO: the fine-tuned policy π_θ generates responses; the reward model scores them; the PPO loss clips the ratio r_t = π_θ(aₜ|sₜ)/π_old(aₜ|sₜ) to [1−ε, 1+ε] at each token. This is weight clipping applied per-token in the trajectory, preventing any single update from moving the policy too far from the reference.

```python
import numpy as np

rng = np.random.default_rng(42)

# Off-policy IS: evaluate target policy using behaviour-policy trajectories
n_states, n_actions = 5, 2
pi_target   = np.array([[0.7, 0.3]] * n_states)  # target: biased toward action 0
pi_behavior = np.array([[0.5, 0.5]] * n_states)  # behavior: uniform

def run_episode(pi, max_steps=8):
    s = rng.integers(n_states)
    traj, G = [], 0.0
    for _ in range(max_steps):
        a = rng.choice(n_actions, p=pi[s])
        r = rng.standard_normal()
        traj.append((s, a, r)); G += r
        s = rng.integers(n_states)
    return traj, G

n_ep = 2000
is_returns, direct_returns = [], []
for _ in range(n_ep):
    traj, _ = run_episode(pi_behavior)
    # Trajectory IS weight (product of per-step ratios)
    log_rho = sum(np.log(pi_target[s,a]) - np.log(pi_behavior[s,a]) for s,a,r in traj)
    rho = np.exp(np.clip(log_rho, -10, 10))   # clip for numerical safety
    G = sum(r for _,_,r in traj)
    is_returns.append(G * rho)
    direct_returns.append(G)

true_returns = [run_episode(pi_target)[1] for _ in range(n_ep)]

print("=== Off-Policy Value Estimation ===")
print(f"Naive (behavior policy):   {np.mean(direct_returns):.4f} SE={np.std(direct_returns)/np.sqrt(n_ep):.4f}")
print(f"IS-corrected:              {np.mean(is_returns):.4f} SE={np.std(is_returns)/np.sqrt(n_ep):.4f}")
print(f"True (target policy):      {np.mean(true_returns):.4f} SE={np.std(true_returns)/np.sqrt(n_ep):.4f}")

# PPO-style ratio clipping simulation
print("\n=== PPO Ratio Clipping (eps=0.2) ===")
log_ratios = [sum(np.log(pi_target[s,a])-np.log(pi_behavior[s,a]) for s,a,r in run_episode(pi_behavior)[0])
              for _ in range(500)]
ratios = np.exp(np.array(log_ratios))
eps = 0.2
clipped = np.clip(ratios, 1-eps, 1+eps)
pct_clipped = np.mean((ratios < 1-eps) | (ratios > 1+eps)) * 100
print(f"Unclipped ratios: min={ratios.min():.3f} mean={ratios.mean():.3f} max={ratios.max():.3f}")
print(f"Clipped ratios:   min={clipped.min():.3f} mean={clipped.mean():.3f} max={clipped.max():.3f}")
print(f"{pct_clipped:.1f}% of trajectories had ratios outside [1-eps, 1+eps]")
```

## Annealed Importance Sampling

Annealed importance sampling (AIS) estimates the ratio of partition functions Z₁/Z₀ — a quantity needed for Bayesian model comparison, normalising flow likelihood evaluation, and energy-based model training. It bridges between an easy proposal p₀ and a hard target p₁ through a sequence of intermediate distributions:

p_t(x) ∝ p₀(x)^{1-βₜ} p₁(x)^{βₜ},  β₀=0, β₁=1, β₀ < β₁ < … < βₙ = 1

The IS weight for a chain x₀ → x₁ → … → xₙ (where each xₜ is produced by a transition kernel targeting pₜ) is:

w = Πₜ pₜ(xₜ₋₁) / p_{t-1}(xₜ₋₁)

AIS with many intermediate steps (large T) gives small variance and reliable partition function estimates.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Annealed IS: estimate Z_1/Z_0 where p_0=N(0,1), p_1=N(3,0.5^2)
# True ratio: Z_1/Z_0 = 1 (both are proper Gaussians)
# But AIS estimates E_{p_1}[f] = integral f(x) p_1(x) dx / Z_1
# More useful: AIS to estimate normalising constant of unnormalised target

mu_target, sigma_target = 3.0, 0.5

def log_p0(x):  # proposal: N(0,1)
    return stats.norm.logpdf(x, 0, 1)

def log_p1(x):  # target: N(3,0.5) (unnormalised in general case)
    return stats.norm.logpdf(x, mu_target, sigma_target)

def log_pt(x, beta):  # intermediate: geometric average
    return (1-beta)*log_p0(x) + beta*log_p1(x)

def ais_estimate(n_samples=500, n_steps=20):
    """Annealed IS with Gaussian MCMC transitions."""
    betas = np.linspace(0, 1, n_steps + 1)
    log_weights = np.zeros(n_samples)

    # Start from proposal
    x = rng.standard_normal(n_samples)

    for t in range(1, len(betas)):
        beta_prev, beta_curr = betas[t-1], betas[t]
        # AIS weight contribution: p_t(x) / p_{t-1}(x)
        log_weights += log_pt(x, beta_curr) - log_pt(x, beta_prev)
        # MCMC transition: Metropolis step targeting p_curr
        x_prop = x + rng.normal(0, 0.5, n_samples)
        log_alpha = log_pt(x_prop, beta_curr) - log_pt(x, beta_curr)
        accept = np.log(rng.uniform(size=n_samples)) < log_alpha
        x[accept] = x_prop[accept]

    # AIS estimate: E_p1[X^2] = sum(X^2 * w) / sum(w)
    log_w_normalised = log_weights - np.logaddexp.reduce(log_weights)
    w_norm = np.exp(log_w_normalised)
    E_x2   = np.sum(x**2 * w_norm)
    ess    = np.exp(-np.logaddexp.reduce(2 * log_w_normalised))
    return E_x2, ess

print("=== Annealed IS: Estimate E_p1[X^2] ===")
print(f"True value: {mu_target**2 + sigma_target**2:.4f}")
for T in [5, 20, 100]:
    estimates = [ais_estimate(n_samples=200, n_steps=T) for _ in range(5)]
    ests = [e[0] for e in estimates]; esss = [e[1] for e in estimates]
    print(f"  T={T:>4} steps: mean={np.mean(ests):.4f} std={np.std(ests):.4f} avg_ESS={np.mean(esss):.0f}")
```

## Pitfalls

Critical IS failure modes:

1. **Tail mismatch causing infinite variance**: if q(x) = 0 anywhere p(x) > 0, the estimator is undefined. If q has lighter tails than p, variance is infinite — no amount of samples fixes this.

2. **Long trajectory IS product collapse**: Πₜ p(aₜ)/q(aₜ) over T steps has variance that grows exponentially with T. Per-decision IS, V-trace, or clipping are essential for long-horizon problems.

3. **Computing weights in linear space**: for even moderately different distributions, weights can be astronomical or zero. Always compute log_w = log p(x) − log q(x) and only exponentiate at the final step.

4. **Ignoring ESS as a quality metric**: IS estimates can look numerically stable while having extremely high variance. Always compute ESS/N; below 0.1 is a red flag requiring a better proposal or fewer IS correction steps.

## Practical Guidance

Guidelines for reliable IS in ML:

- **Always work in log-space**: log_w = log p(x) − log q(x), then w = exp(log_w − log_w.max()) for stability.
- **Monitor ESS/N**: flag estimates where ESS/N < 0.1 as unreliable.
- **Weight clipping**: cap weights at a percentile (e.g., 95th percentile of weight distribution) or at a fixed constant. This is always a good default for production IS.
- **For off-policy RL**: use V-trace (per-step ratio clipping) instead of full trajectory IS. V-trace clips each ratio to ρ̄ and c̄ separately for variance and bias control.
- **For RLHF**: PPO's ratio clipping to [1−ε, 1+ε] is weight clipping applied per token. The KL penalty in DPO is an alternative that avoids explicit IS correction.

> **WARNING: ESS < 10% Indicates Severe IS Failure**
>
> When ESS/N < 0.1, fewer than 10% of samples effectively contribute to the estimate. The top few samples dominate, making the estimate unreliable and high-variance. Remedies: (1) use a heavier-tailed proposal; (2) reduce the IS correction distance (stay closer to on-policy); (3) use annealed IS to bridge gradually; (4) use normalising flows to learn a better proposal distribution.

> **TIP: Optimal Proposal Minimises IS Variance**
>
> The variance-minimising IS proposal is q*(x) ∝ |f(x)| p(x) — it concentrates samples where the integrand is large. For f(x) ≥ 0 (e.g., positive reward functions), q*(x) ∝ f(x) p(x) is proportional to the unnormalised target multiplied by the function value. In RL, this is the motivation for experience replay prioritisation: sample transitions proportionally to |δ| (TD error), then correct with IS weights.

| Method | IS Correction | Application | Variance Control |
| --- | --- | --- | --- |
| Vanilla IS | Full ratio p/q | Simple expectations | Can be infinite |
| SNIS | Normalised weights | Unknown normalising constants | Biased, finite |
| Per-decision IS | Partial products | Off-policy RL value estimation | Lower than full IS |
| V-trace | Clipped per-step ratios | Off-policy actor-critic (IMPALA) | Controlled, bounded |
| PPO | Clipped policy ratio per token | RLHF fine-tuning | Low (near-on-policy) |
| AIS | Annealed sequence | Partition function estimation | Very low (many steps) |

---

## Key Takeaways

- IS estimator Ê_p[f] = (1/N) Σ f(xᵢ)w(xᵢ) with xᵢ~q and w=p/q corrects for sampling from the wrong distribution.
- SNIS normalises weights to sum to 1, enabling use with unnormalised p (standard in Bayesian inference) — biased but consistent.
- ESS = (Σwᵢ)²/Σwᵢ² measures efficiency; ESS/N < 0.1 indicates severe weight imbalance and unreliable estimates.
- IS has finite variance only if q has heavier tails than p everywhere; tail mismatch causes infinite variance that extra samples cannot fix.
- Weight clipping (truncation) at constant c trades bias for variance reduction — the principle behind PPO's ratio clipping in RLHF.
- Always compute importance weights in log-space (log p − log q) and only exponentiate at the final step to avoid numerical overflow.
- Annealed IS bridges between a simple proposal and a hard target through intermediate distributions, enabling reliable partition function estimation.
