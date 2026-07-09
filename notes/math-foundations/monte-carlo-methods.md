---
title: "Monte Carlo Methods"
slug: "monte-carlo-methods"
description: "Monte Carlo integration, the O(1/sqrt(N)) convergence rate, variance reduction techniques (control variates, antithetic sampling, stratified sampling), quasi-Monte Carlo with Sobol sequences, and Monte Carlo policy evaluation for RL."
tags: ["probability", "statistics", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiTW9udGUgQ2FybG8gbWV0aG9kcyB1c2UgcmFuZG9tIHNhbXBsaW5nIHRvIHNvbHZlIGRldGVybWluaXN0aWMgYW5kIHN0b2NoYXN0aWMgcHJvYmxlbXMgdGhhdCBhcmUgYW5hbHl0aWNhbGx5IGludHJhY3RhYmxlLiBUaGVpciBraWxsZXIgZmVhdHVyZSBpcyBkaW1lbnNpb24taW5kZXBlbmRlbmNlOiBjbGFzc2ljYWwgcXVhZHJhdHVyZSAodHJhcGV6b2lkYWwgcnVsZSwgR2F1c3NpYW4gcXVhZHJhdHVyZSkgYWNoaWV2ZXMgTyhOXnstay9kfSkgY29udmVyZ2VuY2Ugd2hlcmUgayBpcyB0aGUgb3JkZXIgb2YgdGhlIG1ldGhvZCBhbmQgZCBpcyB0aGUgZGltZW5zaW9uIOKAlCB0aGlzIGJlY29tZXMgY2F0YXN0cm9waGljYWxseSBzbG93IGluIGhpZ2ggZGltZW5zaW9ucy4gTW9udGUgQ2FybG8gYWNoaWV2ZXMgTygxL+KImk4pIGNvbnZlcmdlbmNlIGluZGVwZW5kZW50IG9mIGRpbWVuc2lvbiwgbWFraW5nIGl0IHRoZSBvbmx5IHByYWN0aWNhbCBpbnRlZ3JhdGlvbiBtZXRob2QgZm9yIHRoZSBoaWdoLWRpbWVuc2lvbmFsIGludGVncmFscyB0aGF0IGFwcGVhciB0aHJvdWdob3V0IHByb2JhYmlsaXN0aWMgTUwsIEJheWVzaWFuIGluZmVyZW5jZSwgYW5kIHJlaW5mb3JjZW1lbnQgbGVhcm5pbmcuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29yZSBEZWZpbml0aW9uIOKAlCBNb250ZSBDYXJsbyBJbnRlZ3JhdGlvbiJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRvIGVzdGltYXRlIEVfcFtmKFgpXSA9IOKIqyBmKHgpIHAoeCkgZHgsIGRyYXcgTiBpbmRlcGVuZGVudCBzYW1wbGVzIHjigoEsIOKApiwgeOKCmSB+IHAoWCkgYW5kIGNvbXB1dGU6XG5cbsOKW2ZdID0gKDEvTikgzqPhtaIgZih44bWiKVxuXG5CeSB0aGUgTGF3IG9mIExhcmdlIE51bWJlcnMsIMOKW2ZdIOKGkiBFW2ZdIGFzIE4g4oaSIOKIni4gQnkgdGhlIENlbnRyYWwgTGltaXQgVGhlb3JlbTpcblxu4oiaTiAow4pbZl0g4oiSIEVbZl0pIOKGkiBOKDAsIFZhcl9wW2YoWCldKVxuXG5TbyB0aGUgc3RhbmRhcmQgZXJyb3Igb2YgdGhlIE1vbnRlIENhcmxvIGVzdGltYXRlIGlzOlxuXG5TRSA9IOKImihWYXJfcFtmKFgpXSAvIE4pID0gz4NfZiAvIOKImk5cblxuVGhpcyBPKDEv4oiaTikgY29udmVyZ2VuY2UgcmF0ZSBpcyBzbG93IOKAlCB0byBoYWx2ZSB0aGUgZXJyb3IgeW91IG5lZWQgNMOXIGFzIG1hbnkgc2FtcGxlcyDigJQgYnV0IGNydWNpYWxseSwgaXQgaXMgaW5kZXBlbmRlbnQgb2YgZGltZW5zaW9uIGQuIEZvciBkID0gMTAwIGZlYXR1cmVzLCBjbGFzc2ljYWwgbnVtZXJpY2FsIGludGVncmF0aW9uIHdpdGggMTAgZ3JpZCBwb2ludHMgcGVyIGRpbWVuc2lvbiByZXF1aXJlcyAxMF4xMDAgZnVuY3Rpb24gZXZhbHVhdGlvbnM7IE1vbnRlIENhcmxvIG5lZWRzIHRoZSBzYW1lIE4gcmVnYXJkbGVzcyBvZiBkLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliXG5tYXRwbG90bGliLnVzZSgnQWdnJylcblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxuXG4jIE1vbnRlIENhcmxvIGludGVncmF0aW9uOiBFW1heMl0gd2hlcmUgWCB+IFVuaWZvcm0oMCwxKVxuIyBUcnVlIHZhbHVlOiBpbnRlZ3JhbF8wXjEgeF4yIGR4ID0gMS8zXG50cnVlX3ZhbCA9IDEuMCAvIDMuMFxucHJpbnQoXCI9PT0gTUMgSW50ZWdyYXRpb246IEVbWF4yXSwgWH5Vbmlmb3JtKDAsMSkgPT09XCIpXG5wcmludChmXCJUcnVlIHZhbHVlOiB7dHJ1ZV92YWw6LjhmfVwiKVxuXG5mb3IgTiBpbiBbMTAwLCAxXzAwMCwgMTBfMDAwLCAxMDBfMDAwLCAxXzAwMF8wMDBdOlxuICAgIHNhbXBsZXMgPSBybmcudW5pZm9ybSgwLCAxLCBOKVxuICAgIGVzdGltYXRlID0gbnAubWVhbihzYW1wbGVzKioyKVxuICAgIHNlID0gbnAuc3RkKHNhbXBsZXMqKjIsIGRkb2Y9MSkgLyBucC5zcXJ0KE4pXG4gICAgZXJyb3IgPSBhYnMoZXN0aW1hdGUgLSB0cnVlX3ZhbClcbiAgICBwcmludChmXCIgIE49e046PjksfTogZXN0aW1hdGU9e2VzdGltYXRlOi42Zn0gIFNFPXtzZTouMmV9ICBlcnJvcj17ZXJyb3I6LjJlfVwiKVxuXG4jIENvbnZlcmdlbmNlIHJhdGU6IGVycm9yIH4gMS9zcXJ0KE4pXG5wcmludChcIlxcbj09PSBDb252ZXJnZW5jZSBSYXRlIFZlcmlmaWNhdGlvbiA9PT1cIilcbk5fdmFscyA9IFsxMDAsIDEwMDAsIDEwMDAwLCAxMDAwMDBdXG5lcnJvcnMgPSBbXVxuZm9yIE4gaW4gTl92YWxzOlxuICAgIG5fcmVwcyA9IDIwMFxuICAgIGVzdHMgPSBbbnAubWVhbihybmcudW5pZm9ybSgwLDEsTikqKjIpIGZvciBfIGluIHJhbmdlKG5fcmVwcyldXG4gICAgZXJyb3JzLmFwcGVuZChucC5zdGQoZXN0cykpXG5cbmZvciBOLCBlcnIgaW4gemlwKE5fdmFscywgZXJyb3JzKTpcbiAgICBwcmludChmXCIgIE49e046PjcsfTogZW1waXJpY2FsIFNFPXtlcnI6LjRlfSAgdGhlb3J5PXsxLygzKm5wLnNxcnQoTikpOi40ZX1cIilcblxuIyBNQyBlc3RpbWF0ZSBvZiBwaTogZnJhY3Rpb24gb2YgcG9pbnRzIGluc2lkZSB1bml0IGNpcmNsZVxucHJpbnQoXCJcXG49PT0gTW9udGUgQ2FybG8gZm9yIHBpID09PVwiKVxuTiA9IDFfMDAwXzAwMFxueCwgeSA9IHJuZy51bmlmb3JtKC0xLCAxLCBOKSwgcm5nLnVuaWZvcm0oLTEsIDEsIE4pXG5waV9lc3QgPSA0ICogbnAubWVhbih4KioyICsgeSoqMiA8PSAxKVxucHJpbnQoZlwicGkgZXN0aW1hdGUgKE49e046LH0pOiB7cGlfZXN0Oi42Zn0gICh0cnVlOiB7bnAucGk6LjZmfSlcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJWYXJpYW5jZSBSZWR1Y3Rpb24gVGVjaG5pcXVlcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlRoZSBNb250ZSBDYXJsbyBTRSA9IM+DX2YgLyDiiJpOIGNhbiBiZSByZWR1Y2VkIGJ5IGRlY3JlYXNpbmcgz4NfZiByYXRoZXIgdGhhbiBpbmNyZWFzaW5nIE4uIFNldmVyYWwgdGVjaG5pcXVlcyBhY2hpZXZlIHRoaXM6XG5cbioqQ29udHJvbCB2YXJpYXRlcyoqOiBpZiB3ZSBrbm93IEVbZyhYKV0gYW5hbHl0aWNhbGx5IGFuZCBnIGlzIGNvcnJlbGF0ZWQgd2l0aCBmLCB1c2UgdGhlIGVzdGltYXRvcjpcbsOKX0NWW2ZdID0gKDEvTikgzqMgW2YoeOG1oikg4oiSIGMoZyh44bWiKSDiiJIgRVtnKFgpXSldXG5UaGUgb3B0aW1hbCBjb25zdGFudCBjKiA9IENvdihmLCBnKSAvIFZhcihnKSBhY2hpZXZlcyB2YXJpYW5jZSByZWR1Y3Rpb24gb2YgZmFjdG9yIDEg4oiSIM+BwrIoZixnKS5cblxuKipBbnRpdGhldGljIHZhcmlhdGVzKio6IHVzZSBwYWlycyAoeOG1oiwgeMyD4bWiKSB3aGVyZSB4zIPhtaIgaXMgdGhlICdyZWZsZWN0aW9uJyBvZiB44bWiIChlLmcuLCBmb3IgdW5pZm9ybSBzYW1wbGVzLCB4zIPhtaIgPSAxIOKIkiB44bWiKS4gSWYgZih4KSBhbmQgZih4zIMpIGFyZSBuZWdhdGl2ZWx5IGNvcnJlbGF0ZWQsIFZhcihmKHgpICsgZih4zIMpKS8yIDwgVmFyKGYoeCkpLlxuXG4qKlN0cmF0aWZpZWQgc2FtcGxpbmcqKjogZGl2aWRlIHRoZSBkb21haW4gaW50byBLIHN0cmF0YSBhbmQgZHJhdyBOL0sgc2FtcGxlcyBmcm9tIGVhY2guIFZhcmlhbmNlIG9mIHRoZSBlc3RpbWF0b3IgaXMgcmVkdWNlZCBieSBlbGltaW5hdGluZyBiZXR3ZWVuLXN0cmF0dW0gdmFyaWFiaWxpdHkuXG5cbioqUmFvLUJsYWNrd2VsbGl6YXRpb24qKjogY29uZGl0aW9uIG9uIGEgc3VmZmljaWVudCBzdGF0aXN0aWMgdG8gcmVkdWNlIHZhcmlhbmNlIHdpdGhvdXQgaW50cm9kdWNpbmcgYmlhczogRVtmKFgsWSl8WV0gdXNlcyB0aGUgY29uZGl0aW9uYWwgZXhwZWN0YXRpb24sIHdoaWNoIGFsd2F5cyBoYXMgdmFyaWFuY2Ug4omkIFZhcihmKFgsWSkpLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxuXG4jIFRhcmdldDogRVtleHAoWCldIHdoZXJlIFh+VW5pZm9ybSgwLDEpXG4jIFRydWUgdmFsdWU6IGludGVncmFsXzBeMSBleHAoeCkgZHggPSBlIC0gMSDiiYggMS43MTgyOFxudHJ1ZV92YWwgPSBucC5lIC0gMS4wXG5mID0gbnAuZXhwXG5cbnByaW50KFwiPT09IFZhcmlhbmNlIFJlZHVjdGlvbiBmb3IgRVtleHAoWCldLCBYflUoMCwxKSA9PT1cIilcbnByaW50KGZcIlRydWUgdmFsdWU6IHt0cnVlX3ZhbDouOGZ9XCIpXG5cbk4gPSAxMF8wMDBcblxuIyAxLiBTdGFuZGFyZCBNQ1xueF9tYyA9IHJuZy51bmlmb3JtKDAsIDEsIE4pXG5tY19lc3QgPSBucC5tZWFuKGYoeF9tYykpXG5tY19zZSAgPSBucC5zdGQoZih4X21jKSkgLyBucC5zcXJ0KE4pXG5wcmludChmXCJcXG5TdGFuZGFyZCBNQzogICAgICBlc3Q9e21jX2VzdDouNmZ9ICBTRT17bWNfc2U6LjRlfVwiKVxuXG4jIDIuIEFudGl0aGV0aWMgdmFyaWF0ZXM6IHBhaXIgeCB3aXRoICgxLXgpXG54X2FudGkgPSBybmcudW5pZm9ybSgwLCAxLCBOIC8vIDIpXG55X2FudGkgPSAxIC0geF9hbnRpXG5hbnRpX3ZhbHMgPSAoZih4X2FudGkpICsgZih5X2FudGkpKSAvIDJcbmFudGlfZXN0ICA9IG5wLm1lYW4oYW50aV92YWxzKVxuYW50aV9zZSAgID0gbnAuc3RkKGFudGlfdmFscykgLyBucC5zcXJ0KE4gLy8gMilcbnByaW50KGZcIkFudGl0aGV0aWM6ICAgICAgIGVzdD17YW50aV9lc3Q6LjZmfSAgU0U9e2FudGlfc2U6LjRlfSAgXCJcbiAgICAgIGZcInNwZWVkdXA9e21jX3NlL2FudGlfc2U6LjFmfXhcIilcblxuIyAzLiBDb250cm9sIHZhcmlhdGU6IGcoeCkgPSB4LCBFW2ddID0gMC41XG54X2N2ID0gcm5nLnVuaWZvcm0oMCwgMSwgTilcbmZfY3YgPSBmKHhfY3YpXG5nX2N2ID0geF9jdlxuRV9nICA9IDAuNVxuIyBPcHRpbWFsIGMqOiByZWdyZXNzIGYgb24gZ1xuY19zdGFyID0gbnAuY292KGZfY3YsIGdfY3YpWzAsMV0gLyBucC52YXIoZ19jdilcbmN2X3ZhbHMgPSBmX2N2IC0gY19zdGFyICogKGdfY3YgLSBFX2cpXG5jdl9lc3QgID0gbnAubWVhbihjdl92YWxzKVxuY3Zfc2UgICA9IG5wLnN0ZChjdl92YWxzKSAvIG5wLnNxcnQoTilcbnByaW50KGZcIkNvbnRyb2wgdmFyaWF0ZTogIGVzdD17Y3ZfZXN0Oi42Zn0gIFNFPXtjdl9zZTouNGV9ICBcIlxuICAgICAgZlwic3BlZWR1cD17bWNfc2UvY3Zfc2U6LjFmfXggIGMqPXtjX3N0YXI6LjRmfVwiKVxuXG4jIDQuIFN0cmF0aWZpZWQgc2FtcGxpbmc6IDEwIHN0cmF0YVxuSyA9IDEwXG54X3N0cmF0ID0gbnAuY29uY2F0ZW5hdGUoW3JuZy51bmlmb3JtKGsvSywgKGsrMSkvSywgTi8vSykgZm9yIGsgaW4gcmFuZ2UoSyldKVxuc3RyYXRfZXN0ID0gbnAubWVhbihmKHhfc3RyYXQpKVxuc3RyYXRfc2UgID0gbnAuc3RkKFtucC5tZWFuKGYocm5nLnVuaWZvcm0oay9LLCAoaysxKS9LLCBOLy9LKSkpIGZvciBrIGluIHJhbmdlKEspXSkgLyBucC5zcXJ0KEspXG5wcmludChmXCJTdHJhdGlmaWVkOiAgICAgICBlc3Q9e3N0cmF0X2VzdDouNmZ9ICBTRT17c3RyYXRfc2U6LjRlfSAgc3BlZWR1cD17bWNfc2Uvc3RyYXRfc2U6LjFmfXhcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJRdWFzaS1Nb250ZSBDYXJsbyBhbmQgTG93LURpc2NyZXBhbmN5IFNlcXVlbmNlcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlN0YW5kYXJkIE1vbnRlIENhcmxvIHVzZXMgcHNldWRvLXJhbmRvbSBzYW1wbGVzIHRoYXQgY2FuIGNsdXN0ZXIgb3IgbGVhdmUgZ2FwcyBieSBjaGFuY2UsIGV2ZW4gd2l0aCBnb29kIHJhbmRvbSBudW1iZXIgZ2VuZXJhdG9ycy4gUXVhc2ktTW9udGUgQ2FybG8gKFFNQykgcmVwbGFjZXMgcmFuZG9tIHNhbXBsZXMgd2l0aCBkZXRlcm1pbmlzdGljIGxvdy1kaXNjcmVwYW5jeSBzZXF1ZW5jZXMg4oCUIHNlcXVlbmNlcyBkZXNpZ25lZCB0byBjb3ZlciB0aGUgZG9tYWluIGFzIHVuaWZvcm1seSBhcyBwb3NzaWJsZS5cblxuU29ib2wgc2VxdWVuY2VzIGFyZSB0aGUgbW9zdCB3aWRlbHkgdXNlZDogdGhleSBhY2hpZXZlIGRpc2NyZXBhbmN5IE8oKGxvZyBOKV5kIC8gTiksIGxlYWRpbmcgdG8gY29udmVyZ2VuY2UgcmF0ZXMgYXBwcm9hY2hpbmcgTygxL04pIGZvciBzbW9vdGggaW50ZWdyYW5kcyDigJQgbXVjaCBmYXN0ZXIgdGhhbiBPKDEv4oiaTikuIEhvd2V2ZXIsIHRoZSBhZHZhbnRhZ2UgZGltaW5pc2hlcyBpbiBoaWdoIGRpbWVuc2lvbnMgKGQgPiAyMCBvciBzbykgYmVjYXVzZSB0aGUgKGxvZyBOKV5kIGZhY3RvciBiZWNvbWVzIGxhcmdlLlxuXG5IYWx0b24gc2VxdWVuY2VzIHVzZSBkaWZmZXJlbnQgcHJpbWVzIGZvciBlYWNoIGRpbWVuc2lvbi4gTGF0dGljZSBydWxlcyAocmFuay0xIGxhdHRpY2VzKSBhcmUgcG9wdWxhciBmb3IgQmF5ZXNpYW4gaW50ZWdyYXRpb24uIFB5VG9yY2ggaW5jbHVkZXMgdG9yY2gucXVhc2lyYW5kb20uU29ib2xFbmdpbmUgZm9yIFFNQyBzYW1wbGluZywgbWFraW5nIGl0IGVhc3kgdG8gdXNlIGluIE1MIGV4cGVyaW1lbnRzIChoeXBlcnBhcmFtZXRlciBzZWFyY2gsIGludGVncmF0aW9uIGluIG5vcm1hbGl6aW5nIGZsb3dzKS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzLnFtYyBpbXBvcnQgU29ib2wsIEhhbHRvblxuaW1wb3J0IHdhcm5pbmdzOyB3YXJuaW5ncy5maWx0ZXJ3YXJuaW5ncygnaWdub3JlJylcblxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxuXG4jIENvbXBhcmUgcmFuZG9tIE1DIHZzIFNvYm9sIFFNQyBmb3IgcGkgZXN0aW1hdGlvblxuZGVmIGVzdGltYXRlX3BpKHNhbXBsZXNfMmQpOlxuICAgIHgsIHkgPSBzYW1wbGVzXzJkWzosIDBdLCBzYW1wbGVzXzJkWzosIDFdXG4gICAgcmV0dXJuIDQgKiBucC5tZWFuKHgqKjIgKyB5KioyIDw9IDEpXG5cbnByaW50KFwiPT09IE1DIHZzIFFNQzogZXN0aW1hdGluZyBwaSA9PT1cIilcbmZvciBOIGluIFsyNTYsIDEwMjQsIDQwOTYsIDE2Mzg0XTpcbiAgICAjIFJhbmRvbSBNQ1xuICAgIG1jX3NhbXBsZXMgID0gcm5nLnVuaWZvcm0oMCwgMSwgKE4sIDIpKVxuICAgIG1jX3BpICAgICAgID0gZXN0aW1hdGVfcGkobWNfc2FtcGxlcylcbiAgICBtY19lcnIgICAgICA9IGFicyhtY19waSAtIG5wLnBpKVxuXG4gICAgIyBTb2JvbCBRTUNcbiAgICBzb2JvbCA9IFNvYm9sKGQ9Miwgc2NyYW1ibGU9VHJ1ZSwgc2VlZD00MilcbiAgICBxbWNfc2FtcGxlcyA9IHNvYm9sLnJhbmRvbShOKVxuICAgIHFtY19waSAgPSBlc3RpbWF0ZV9waShxbWNfc2FtcGxlcylcbiAgICBxbWNfZXJyID0gYWJzKHFtY19waSAtIG5wLnBpKVxuXG4gICAgcHJpbnQoZlwiICBOPXtOOj42LH06IE1DX2Vycj17bWNfZXJyOi40Zn0gIFFNQ19lcnI9e3FtY19lcnI6LjRmfSAgcmF0aW89e21jX2Vyci9xbWNfZXJyOi4xZn14XCIpXG5cbiMgU29ib2wgZm9yIGh5cGVycGFyYW1ldGVyIHNlYXJjaCAoYmV0dGVyIGNvdmVyYWdlIHRoYW4gcmFuZG9tIGdyaWQpXG5wcmludChcIlxcbj09PSBTb2JvbCBmb3IgM0QgSHlwZXJwYXJhbWV0ZXIgU2VhcmNoID09PVwiKVxuc29ib2wzID0gU29ib2woZD0zLCBzY3JhbWJsZT1UcnVlLCBzZWVkPTApXG5ocF9zYW1wbGVzID0gc29ib2wzLnJhbmRvbSgxNikgICMgMTYgY29uZmlncyBpbiBbMCwxXV4zXG4jIE1hcCB0byBhY3R1YWwgaHlwZXJwYXJhbWV0ZXIgcmFuZ2VzXG5sciAgICAgPSAxMCAqKiAoaHBfc2FtcGxlc1s6LCAwXSAqICgtNCkgKyAoLTIpKSAgIyBbMWUtNCwgMWUtMl0gbG9nLXNjYWxlXG53ZCAgICAgPSAxMCAqKiAoaHBfc2FtcGxlc1s6LCAxXSAqICgtNikgKyAoLTIpKSAgIyBbMWUtNiwgMWUtMl0gbG9nLXNjYWxlXG5kcm9wICAgPSBocF9zYW1wbGVzWzosIDJdICogMC41ICAgICAgICAgICAgICAgICAgICMgWzAsIDAuNV1cbmZvciBpIGluIHJhbmdlKDQpOlxuICAgIHByaW50KGZcIiAgY29uZmlnIHtpfTogbHI9e2xyW2ldOi4yZX0gIHdkPXt3ZFtpXTouMmV9ICBkcm9wb3V0PXtkcm9wW2ldOi4zZn1cIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJNb250ZSBDYXJsbyBQb2xpY3kgRXZhbHVhdGlvbiAoUkwpIn0sIHsidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiSW4gcmVpbmZvcmNlbWVudCBsZWFybmluZywgTW9udGUgQ2FybG8gKE1DKSBwb2xpY3kgZXZhbHVhdGlvbiBlc3RpbWF0ZXMgdGhlIHZhbHVlIGZ1bmN0aW9uIFZez4AocykgPSBFW0dfdCB8IFNfdCA9IHNdIGJ5IGF2ZXJhZ2luZyB0aGUgYWN0dWFsIHJldHVybnMgR190IG9ic2VydmVkIGZyb20gc3RhdGUgcyB3aGVuIGZvbGxvd2luZyBwb2xpY3kgz4AuIFVubGlrZSB0ZW1wb3JhbCBkaWZmZXJlbmNlIChURCkgbWV0aG9kcywgTUMgdXNlcyBmdWxsIGVwaXNvZGUgcmV0dXJucyBhbmQgZG9lcyBub3QgYm9vdHN0cmFwLlxuXG5Gb3IgZXBpc29kaWMgTURQczpcbjEuIEdlbmVyYXRlIGVwaXNvZGU6IFPigoAsIEHigoAsIFLigoEsIFPigoEsIEHigoEsIFLigoIsIOKApiwgU19UIGZvbGxvd2luZyBwb2xpY3kgz4BcbjIuIENvbXB1dGUgcmV0dXJuczogR190ID0gUl97dCsxfSArIM6zIFJfe3QrMn0gKyDigKYgKyDOs157VC10LTF9IFJfVFxuMy4gVXBkYXRlOiBWKFNfdCkg4oaQIFYoU190KSArIM6xKEdfdCDiiJIgVihTX3QpKSAgW2luY3JlbWVudGFsIG1lYW5dXG5cbkV2ZXJ5LXZpc2l0IE1DIGF2ZXJhZ2VzIG92ZXIgYWxsIHZpc2l0cyB0byBzdGF0ZSBzIGluIGFsbCBlcGlzb2Rlcy4gRmlyc3QtdmlzaXQgTUMgYXZlcmFnZXMgb25seSB0aGUgZmlyc3QgdmlzaXQgcGVyIGVwaXNvZGUgKGdpdmVzIHVuYmlhc2VkIGVzdGltYXRlIG9mIFZez4AocykpLiBNQyBpcyB1bmJpYXNlZCBidXQgaGlnaC12YXJpYW5jZTsgVEQgaXMgYmlhc2VkIGJ1dCBsb3dlci12YXJpYW5jZS4gVGhlIGJpYXMtdmFyaWFuY2UgdHJhZGVvZmYgYmV0d2VlbiBNQyBhbmQgVEQgaXMgY29udHJvbGxlZCBieSBuLXN0ZXAgcmV0dXJucyBhbmQgzrsgaW4gVEQozrspLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBTaW1wbGUgR3JpZFdvcmxkIE1EUCBmb3IgTW9udGUgQ2FybG8gcG9saWN5IGV2YWx1YXRpb25cbmNsYXNzIEdyaWRXb3JsZDpcbiAgICBcIlwiXCI0eDQgZ3JpZCwgYWJzb3JiaW5nIGNvcm5lcnMgYXQgKDAsMCkgYW5kICgzLDMpLCByZXdhcmQgLTEgcGVyIHN0ZXAuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHNpemU9NCk6XG4gICAgICAgIHNlbGYuc2l6ZSA9IHNpemVcbiAgICAgICAgc2VsZi50ZXJtaW5hbCA9IHsoMCwwKSwgKHNpemUtMSwgc2l6ZS0xKX1cbiAgICAgICAgc2VsZi5hY3Rpb25zID0gWygwLDEpLCgwLC0xKSwoMSwwKSwoLTEsMCldICAjIFIsTCxELFVcblxuICAgIGRlZiBzdGVwKHNlbGYsIHN0YXRlLCBhY3Rpb24pOlxuICAgICAgICBpZiBzdGF0ZSBpbiBzZWxmLnRlcm1pbmFsOlxuICAgICAgICAgICAgcmV0dXJuIHN0YXRlLCAwLjAsIFRydWVcbiAgICAgICAgciwgYyA9IHN0YXRlXG4gICAgICAgIGRyLCBkYyA9IGFjdGlvblxuICAgICAgICBuciwgbmMgPSBucC5jbGlwKHIrZHIsIDAsIHNlbGYuc2l6ZS0xKSwgbnAuY2xpcChjK2RjLCAwLCBzZWxmLnNpemUtMSlcbiAgICAgICAgbmV3X3N0YXRlID0gKG5yLCBuYylcbiAgICAgICAgZG9uZSA9IG5ld19zdGF0ZSBpbiBzZWxmLnRlcm1pbmFsXG4gICAgICAgIHJldHVybiBuZXdfc3RhdGUsIC0xLjAsIGRvbmVcblxuZGVmIGdlbmVyYXRlX2VwaXNvZGUoZW52LCBwb2xpY3ksIG1heF9zdGVwcz0yMDApOlxuICAgIFwiXCJcIkdlbmVyYXRlIG9uZSBlcGlzb2RlIGZvbGxvd2luZyBwb2xpY3kuXCJcIlwiXG4gICAgcyA9IChucC5yYW5kb20ucmFuZGludChlbnYuc2l6ZSksIG5wLnJhbmRvbS5yYW5kaW50KGVudi5zaXplKSlcbiAgICB3aGlsZSBzIGluIGVudi50ZXJtaW5hbDpcbiAgICAgICAgcyA9IChucC5yYW5kb20ucmFuZGludChlbnYuc2l6ZSksIG5wLnJhbmRvbS5yYW5kaW50KGVudi5zaXplKSlcbiAgICB0cmFqZWN0b3J5ID0gW11cbiAgICBmb3IgXyBpbiByYW5nZShtYXhfc3RlcHMpOlxuICAgICAgICBhID0gcG9saWN5KHMpXG4gICAgICAgIHNfbmV4dCwgciwgZG9uZSA9IGVudi5zdGVwKHMsIGEpXG4gICAgICAgIHRyYWplY3RvcnkuYXBwZW5kKChzLCBhLCByKSlcbiAgICAgICAgcyA9IHNfbmV4dFxuICAgICAgICBpZiBkb25lOiBicmVha1xuICAgIHJldHVybiB0cmFqZWN0b3J5XG5cbmRlZiBtY19wb2xpY3lfZXZhbHVhdGlvbihlbnYsIHBvbGljeSwgbl9lcGlzb2Rlcz01MDAwLCBnYW1tYT0wLjk5KTpcbiAgICBcIlwiXCJGaXJzdC12aXNpdCBNb250ZSBDYXJsbyBwb2xpY3kgZXZhbHVhdGlvbi5cIlwiXCJcbiAgICBWID0ge307IHJldHVybnMgPSB7fVxuICAgIGZvciBlcCBpbiByYW5nZShuX2VwaXNvZGVzKTpcbiAgICAgICAgdHJhaiA9IGdlbmVyYXRlX2VwaXNvZGUoZW52LCBwb2xpY3kpXG4gICAgICAgIEcgPSAwLjBcbiAgICAgICAgdmlzaXRlZCA9IHNldCgpXG4gICAgICAgIGZvciBzLCBhLCByIGluIHJldmVyc2VkKHRyYWopOlxuICAgICAgICAgICAgRyA9IHIgKyBnYW1tYSAqIEdcbiAgICAgICAgICAgIGlmIHMgbm90IGluIHZpc2l0ZWQ6ICAjIGZpcnN0LXZpc2l0XG4gICAgICAgICAgICAgICAgdmlzaXRlZC5hZGQocylcbiAgICAgICAgICAgICAgICByZXR1cm5zLnNldGRlZmF1bHQocywgW10pLmFwcGVuZChHKVxuICAgICAgICAgICAgICAgIFZbc10gPSBucC5tZWFuKHJldHVybnNbc10pXG4gICAgcmV0dXJuIFZcblxubnAucmFuZG9tLnNlZWQoNDIpXG5lbnYgPSBHcmlkV29ybGQoNClcbiMgUmFuZG9tIHBvbGljeTogdW5pZm9ybSBvdmVyIDQgYWN0aW9uc1xucG9saWN5ID0gbGFtYmRhIHM6IGVudi5hY3Rpb25zW25wLnJhbmRvbS5yYW5kaW50KDQpXVxuXG5WID0gbWNfcG9saWN5X2V2YWx1YXRpb24oZW52LCBwb2xpY3ksIG5fZXBpc29kZXM9MTAwMDApXG5wcmludChcIj09PSBWYWx1ZSBGdW5jdGlvbiAocmFuZG9tIHBvbGljeSwgZ2FtbWE9MC45OSkgPT09XCIpXG5ncmlkID0gbnAuemVyb3MoKDQsIDQpKVxuZm9yIChyLCBjKSwgdiBpbiBWLml0ZW1zKCk6XG4gICAgZ3JpZFtyLCBjXSA9IHZcbmZvciBpLCByb3cgaW4gZW51bWVyYXRlKGdyaWQpOlxuICAgIHByaW50KGZcIiAgcm93IHtpfToge1tmJ3t2OjYuMWZ9JyBmb3IgdiBpbiByb3ddfVwiKVxucHJpbnQoXCIgICgwLDApIGFuZCAoMywzKSBhcmUgdGVybWluYWwgc3RhdGVzIHdpdGggdmFsdWUgMClcIikifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQaXRmYWxscyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkNvbW1vbiBNb250ZSBDYXJsbyBtaXN0YWtlczpcblxuMS4gKipJbnN1ZmZpY2llbnQgc2FtcGxlcyBmb3IgaGlnaC12YXJpYW5jZSBpbnRlZ3JhbmRzKio6IGlmIGYoeCkgaGFzIGhlYXZ5IHRhaWxzLCB0aGUgZW1waXJpY2FsIHZhcmlhbmNlIGVzdGltYXRlIGlzIHVucmVsaWFibGUgYW5kIFNFIGVzdGltYXRlcyBhcmUgdG9vIG9wdGltaXN0aWMuIENoZWNrIGZvciBvdXRsaWVycy5cblxuMi4gKipDb3JyZWxhdGVkIHNhbXBsZXMgd2l0aG91dCBhY2NvdW50aW5nIGZvciBpdCoqOiBNQ01DIHNhbXBsZXMgYXJlIGNvcnJlbGF0ZWQuIFRyZWF0aW5nIHRoZW0gYXMgaW5kZXBlbmRlbnQgdW5kZXJlc3RpbWF0ZXMgdGhlIHRydWUgU0UgYnkgdXAgdG8g4oiaKDLPhCkgd2hlcmUgz4QgaXMgdGhlIGF1dG9jb3JyZWxhdGlvbiB0aW1lLlxuXG4zLiAqKlVzaW5nIFFNQyB3aGVuIHNhbXBsZXMgYXJlIG5vdCBpLmkuZC4qKjogU29ib2wgYW5kIEhhbHRvbiBzZXF1ZW5jZXMgYXJlIGRlc2lnbmVkIGZvciBpbnRlZ3JhdGlvbiwgbm90IGZvciBwcm9iYWJpbGlzdGljIHNhbXBsaW5nLiBVc2luZyB0aGVtIGFzICdyYW5kb20nIHNhbXBsZXMgaW4gcHJvYmFiaWxpc3RpYyBhbGdvcml0aG1zIChlLmcuLCBCYXllc2lhbiBvcHRpbWlzYXRpb24gYWNxdWlzaXRpb24pIGNhbiBnaXZlIG92ZXJjb25maWRlbnQgZXN0aW1hdGVzLlxuXG40LiAqKkZvcmdldHRpbmcgdGhhdCAxL+KImk4gY29udmVyZ2VuY2UgaXMgc2xvdyoqOiBnb2luZyBmcm9tIDElIHRvIDAuMSUgZXJyb3IgcmVxdWlyZXMgMTAww5cgbW9yZSBzYW1wbGVzLiBWYXJpYW5jZSByZWR1Y3Rpb24gdGVjaG5pcXVlcyBvciBiZXR0ZXIgZXN0aW1hdG9ycyBhcmUgb2Z0ZW4gbW9yZSBjb3N0LWVmZmVjdGl2ZSB0aGFuIGJydXRlLWZvcmNlIHNhbXBsZSBpbmNyZWFzZS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQcmFjdGljYWwgR3VpZGFuY2UifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJHdWlkZWxpbmVzIGZvciBNb250ZSBDYXJsbyBpbiBNTDpcblxuLSAqKkFsd2F5cyBlc3RpbWF0ZSB0aGUgU0UqKjogcmVwb3J0IFNFID0gc3RkKGYoeOG1oikpIC8g4oiaTiBhbG9uZ3NpZGUgdGhlIGVzdGltYXRlLiBJZiBTRSA+IGRlc2lyZWQgYWNjdXJhY3ksIGluY3JlYXNlIE4gb3IgYXBwbHkgdmFyaWFuY2UgcmVkdWN0aW9uLlxuLSAqKkZvciBoeXBlcnBhcmFtZXRlciBzZWFyY2gqKjogdXNlIFNvYm9sIHNlcXVlbmNlcyBpbnN0ZWFkIG9mIHJhbmRvbSBzZWFyY2gg4oCUIHNhbWUgbnVtYmVyIG9mIGV2YWx1YXRpb25zLCBiZXR0ZXIgY292ZXJhZ2UsIGVzcGVjaWFsbHkgZm9yIGQg4omkIDIwIGRpbWVuc2lvbnMuXG4tICoqRm9yIGludGVncmF0aW9uIGluIGRlZXAgbGVhcm5pbmcqKiAoRUxCTyBlc3RpbWF0aW9uLCBwb2xpY3kgZ3JhZGllbnQpOiB1c2UgY29udHJvbCB2YXJpYXRlcyAoZS5nLiwgYmFzZWxpbmUgc3VidHJhY3Rpb24gaW4gUkVJTkZPUkNFKSB0byByZWR1Y2UgZ3JhZGllbnQgdmFyaWFuY2UuXG4tICoqRm9yIE1DTUMqKjogY29tcHV0ZSB0aGUgZWZmZWN0aXZlIHNhbXBsZSBzaXplIEVTUyA9IE4gLyAoMSArIDIgzqPigpYgz4HigpYpIHdoZXJlIM+B4oKWIGlzIHRoZSBsYWctayBhdXRvY29ycmVsYXRpb24uIEVTUyA8PCBOIGluZGljYXRlcyBwb29yIG1peGluZyBhbmQgaW5mbGF0ZWQgU0UuIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInZhcmlhbnQiOiAidGlwIiwgInRpdGxlIjogIkNvbnRyb2wgVmFyaWF0ZXMgaW4gUkVJTkZPUkNFIiwgImNvbnRlbnQiOiAiVGhlIFJFSU5GT1JDRSBncmFkaWVudCBlc3RpbWF0b3Ig4oiHzrggRVtSXSA9IEVbUiDiiIfOuCBsb2cgz4AoYXxzLM64KV0gaGFzIGhpZ2ggdmFyaWFuY2UuIFN1YnRyYWN0aW5nIGEgYmFzZWxpbmUgYihzKSAoY29udHJvbCB2YXJpYXRlKTog4oiHzrggRVtSXSA9IEVbKFIg4oiSIGIocykpIOKIh864IGxvZyDPgChhfHMszrgpXS4gVGhlIGJhc2VsaW5lIGRvZXMgbm90IGJpYXMgdGhlIGdyYWRpZW50IGJlY2F1c2UgRVtiKHMpIOKIh864IGxvZyDPgF0gPSAwLiBBIGNvbW1vbiBjaG9pY2UgaXMgdGhlIHZhbHVlIGZ1bmN0aW9uIGVzdGltYXRlIFYocykgYXMgdGhlIGJhc2VsaW5lIOKAlCB0aGlzIGlzIHRoZSBhZHZhbnRhZ2UgYWN0b3ItY3JpdGljIG1ldGhvZC4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIk1ldGhvZCIsICJDb252ZXJnZW5jZSIsICJTdHJlbmd0aHMiLCAiV2Vha25lc3NlcyJdLCAicm93cyI6IFtbIlN0YW5kYXJkIE1DIiwgIk8oMS/iiJpOKSIsICJTaW1wbGUsIHVuYmlhc2VkLCBkaW1lbnNpb24tZnJlZSIsICJIaWdoIHZhcmlhbmNlIGZvciBzbW9vdGggaW50ZWdyYW5kcyJdLCBbIkNvbnRyb2wgdmFyaWF0ZXMiLCAiQmV0dGVyIE8oMS/iiJpOKSIsICJDYW4gZ2l2ZSAxMHgrIHNwZWVkdXAiLCAiUmVxdWlyZXMgY29ycmVsYXRlZCBlc3RpbWF0b3Igd2l0aCBrbm93biBtZWFuIl0sIFsiQW50aXRoZXRpYyB2YXJpYXRlcyIsICJCZXR0ZXIgTygxL+KImk4pIiwgIkVhc3kgdG8gaW1wbGVtZW50IiwgIk9ubHkgd29ya3MgZm9yIG1vbm90b25lIGludGVncmFuZHMiXSwgWyJTdHJhdGlmaWVkIHNhbXBsaW5nIiwgIk8oMS9OKSBmb3IgMUQiLCAiR3VhcmFudGVlZCBjb3ZlcmFnZSIsICJIYXJkIHRvIGV4dGVuZCB0byBoaWdoIGRpbWVuc2lvbnMiXSwgWyJTb2JvbCBRTUMiLCAifk8oMS9OKSIsICJCZXN0IGZvciBkPDIwLCBzbW9vdGggZiIsICJOb3QgcHJvYmFiaWxpc3RpY2FsbHkgdmFsaWQgc2FtcGxlcyJdLCBbIk1DTUMgKE1ldHJvcG9saXMpIiwgIk8oMS/iiJpOX2VmZikiLCAiQ2FuIHNhbXBsZSBmcm9tIHVubm9ybWFsaXNlZCBwIiwgIkNvcnJlbGF0ZWQgc2FtcGxlczsgc2xvdyBtaXhpbmciXV19LCB7InR5cGUiOiAiZGl2aWRlciJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIktleSBUYWtlYXdheXMifSwgeyJ0eXBlIjogImxpc3QiLCAib3JkZXJlZCI6IGZhbHNlLCAiaXRlbXMiOiBbIk1DIGludGVncmF0aW9uOiDDiltmXSA9ICgxL04pIM6jIGYoeOG1oikgd2l0aCB44bWifnAgY29udmVyZ2VzIGF0IE8oMS/iiJpOKSBpbmRlcGVuZGVudCBvZiBkaW1lbnNpb24g4oCUIHRoZSBrZXkgYWR2YW50YWdlIG92ZXIgY2xhc3NpY2FsIHF1YWRyYXR1cmUuIiwgIlNFID0gz4NfZiAvIOKImk46IHRvIGhhbHZlIHRoZSBlcnJvciByZXF1aXJlcyA0w5cgc2FtcGxlczsgdmFyaWFuY2UgcmVkdWN0aW9uIGlzIG9mdGVuIG1vcmUgY29zdC1lZmZlY3RpdmUgdGhhbiBpbmNyZWFzaW5nIE4uIiwgIkNvbnRyb2wgdmFyaWF0ZXMgKHN1YnRyYWN0IGEgdGVybSB3aXRoIGtub3duIGV4cGVjdGF0aW9uKSwgYW50aXRoZXRpYyB2YXJpYXRlcyAodXNlIHBhaXJlZCByZWZsZWN0aW9ucyksIGFuZCBzdHJhdGlmaWVkIHNhbXBsaW5nIGFsbCByZWR1Y2UgdmFyaWFuY2Ugd2l0aG91dCBpbmNyZWFzaW5nIE4uIiwgIlNvYm9sIHF1YXNpLU1vbnRlIENhcmxvIGFjaGlldmVzIH5PKDEvTikgY29udmVyZ2VuY2UgZm9yIHNtb290aCBkPDIwIGludGVncmFuZHMgYnkgcmVwbGFjaW5nIHJhbmRvbSBzYW1wbGVzIHdpdGggbG93LWRpc2NyZXBhbmN5IGRldGVybWluaXN0aWMgc2VxdWVuY2VzLiIsICJJbiBSTCwgZmlyc3QtdmlzaXQgTW9udGUgQ2FybG8gcG9saWN5IGV2YWx1YXRpb24gYXZlcmFnZXMgZnVsbCBlcGlzb2RlIHJldHVybnMgZnJvbSBlYWNoIGZpcnN0IHZpc2l0IHRvIGEgc3RhdGUg4oCUIHVuYmlhc2VkIGJ1dCBoaWdoIHZhcmlhbmNlIGNvbXBhcmVkIHRvIFREIG1ldGhvZHMuIiwgIkFsd2F5cyByZXBvcnQgU0UgYWxvbmdzaWRlIE1DIGVzdGltYXRlczsgZm9yIE1DTUMgc2FtcGxlcyBjb21wdXRlIEVTUyB0byBhY2NvdW50IGZvciBhdXRvY29ycmVsYXRpb24gYmVmb3JlIGludGVycHJldGluZyB0aGUgU0UuIiwgIkNvbnRyb2wgdmFyaWF0ZXMgYXBwZWFyIGluIFJMIGFzIGJhc2VsaW5lcyAoYWR2YW50YWdlIGFjdG9yLWNyaXRpYyksIGluIHZhcmlhdGlvbmFsIGluZmVyZW5jZSBhcyB2YXJpYW5jZSByZWR1Y3Rpb24gZm9yIEVMQk8gZ3JhZGllbnQgZXN0aW1hdGVzLiJdfV0="
---
# Monte Carlo Methods

Monte Carlo methods use random sampling to solve deterministic and stochastic problems that are analytically intractable. Their killer feature is dimension-independence: classical quadrature (trapezoidal rule, Gaussian quadrature) achieves O(N^{-k/d}) convergence where k is the order of the method and d is the dimension — this becomes catastrophically slow in high dimensions. Monte Carlo achieves O(1/√N) convergence independent of dimension, making it the only practical integration method for the high-dimensional integrals that appear throughout probabilistic ML, Bayesian inference, and reinforcement learning.

## Core Definition — Monte Carlo Integration

To estimate E_p[f(X)] = ∫ f(x) p(x) dx, draw N independent samples x₁, …, xₙ ~ p(X) and compute:

Ê[f] = (1/N) Σᵢ f(xᵢ)

By the Law of Large Numbers, Ê[f] → E[f] as N → ∞. By the Central Limit Theorem:

√N (Ê[f] − E[f]) → N(0, Var_p[f(X)])

So the standard error of the Monte Carlo estimate is:

SE = √(Var_p[f(X)] / N) = σ_f / √N

This O(1/√N) convergence rate is slow — to halve the error you need 4× as many samples — but crucially, it is independent of dimension d. For d = 100 features, classical numerical integration with 10 grid points per dimension requires 10^100 function evaluations; Monte Carlo needs the same N regardless of d.

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')

rng = np.random.default_rng(42)

# Monte Carlo integration: E[X^2] where X ~ Uniform(0,1)
# True value: integral_0^1 x^2 dx = 1/3
true_val = 1.0 / 3.0
print("=== MC Integration: E[X^2], X~Uniform(0,1) ===")
print(f"True value: {true_val:.8f}")

for N in [100, 1_000, 10_000, 100_000, 1_000_000]:
    samples = rng.uniform(0, 1, N)
    estimate = np.mean(samples**2)
    se = np.std(samples**2, ddof=1) / np.sqrt(N)
    error = abs(estimate - true_val)
    print(f"  N={N:>9,}: estimate={estimate:.6f}  SE={se:.2e}  error={error:.2e}")

# Convergence rate: error ~ 1/sqrt(N)
print("\n=== Convergence Rate Verification ===")
N_vals = [100, 1000, 10000, 100000]
errors = []
for N in N_vals:
    n_reps = 200
    ests = [np.mean(rng.uniform(0,1,N)**2) for _ in range(n_reps)]
    errors.append(np.std(ests))

for N, err in zip(N_vals, errors):
    print(f"  N={N:>7,}: empirical SE={err:.4e}  theory={1/(3*np.sqrt(N)):.4e}")

# MC estimate of pi: fraction of points inside unit circle
print("\n=== Monte Carlo for pi ===")
N = 1_000_000
x, y = rng.uniform(-1, 1, N), rng.uniform(-1, 1, N)
pi_est = 4 * np.mean(x**2 + y**2 <= 1)
print(f"pi estimate (N={N:,}): {pi_est:.6f}  (true: {np.pi:.6f})")
```

## Variance Reduction Techniques

The Monte Carlo SE = σ_f / √N can be reduced by decreasing σ_f rather than increasing N. Several techniques achieve this:

**Control variates**: if we know E[g(X)] analytically and g is correlated with f, use the estimator:
Ê_CV[f] = (1/N) Σ [f(xᵢ) − c(g(xᵢ) − E[g(X)])]
The optimal constant c* = Cov(f, g) / Var(g) achieves variance reduction of factor 1 − ρ²(f,g).

**Antithetic variates**: use pairs (xᵢ, x̃ᵢ) where x̃ᵢ is the 'reflection' of xᵢ (e.g., for uniform samples, x̃ᵢ = 1 − xᵢ). If f(x) and f(x̃) are negatively correlated, Var(f(x) + f(x̃))/2 < Var(f(x)).

**Stratified sampling**: divide the domain into K strata and draw N/K samples from each. Variance of the estimator is reduced by eliminating between-stratum variability.

**Rao-Blackwellization**: condition on a sufficient statistic to reduce variance without introducing bias: E[f(X,Y)|Y] uses the conditional expectation, which always has variance ≤ Var(f(X,Y)).

```python
import numpy as np

rng = np.random.default_rng(42)

# Target: E[exp(X)] where X~Uniform(0,1)
# True value: integral_0^1 exp(x) dx = e - 1 ≈ 1.71828
true_val = np.e - 1.0
f = np.exp

print("=== Variance Reduction for E[exp(X)], X~U(0,1) ===")
print(f"True value: {true_val:.8f}")

N = 10_000

# 1. Standard MC
x_mc = rng.uniform(0, 1, N)
mc_est = np.mean(f(x_mc))
mc_se  = np.std(f(x_mc)) / np.sqrt(N)
print(f"\nStandard MC:      est={mc_est:.6f}  SE={mc_se:.4e}")

# 2. Antithetic variates: pair x with (1-x)
x_anti = rng.uniform(0, 1, N // 2)
y_anti = 1 - x_anti
anti_vals = (f(x_anti) + f(y_anti)) / 2
anti_est  = np.mean(anti_vals)
anti_se   = np.std(anti_vals) / np.sqrt(N // 2)
print(f"Antithetic:       est={anti_est:.6f}  SE={anti_se:.4e}  "
      f"speedup={mc_se/anti_se:.1f}x")

# 3. Control variate: g(x) = x, E[g] = 0.5
x_cv = rng.uniform(0, 1, N)
f_cv = f(x_cv)
g_cv = x_cv
E_g  = 0.5
# Optimal c*: regress f on g
c_star = np.cov(f_cv, g_cv)[0,1] / np.var(g_cv)
cv_vals = f_cv - c_star * (g_cv - E_g)
cv_est  = np.mean(cv_vals)
cv_se   = np.std(cv_vals) / np.sqrt(N)
print(f"Control variate:  est={cv_est:.6f}  SE={cv_se:.4e}  "
      f"speedup={mc_se/cv_se:.1f}x  c*={c_star:.4f}")

# 4. Stratified sampling: 10 strata
K = 10
x_strat = np.concatenate([rng.uniform(k/K, (k+1)/K, N//K) for k in range(K)])
strat_est = np.mean(f(x_strat))
strat_se  = np.std([np.mean(f(rng.uniform(k/K, (k+1)/K, N//K))) for k in range(K)]) / np.sqrt(K)
print(f"Stratified:       est={strat_est:.6f}  SE={strat_se:.4e}  speedup={mc_se/strat_se:.1f}x")
```

## Quasi-Monte Carlo and Low-Discrepancy Sequences

Standard Monte Carlo uses pseudo-random samples that can cluster or leave gaps by chance, even with good random number generators. Quasi-Monte Carlo (QMC) replaces random samples with deterministic low-discrepancy sequences — sequences designed to cover the domain as uniformly as possible.

Sobol sequences are the most widely used: they achieve discrepancy O((log N)^d / N), leading to convergence rates approaching O(1/N) for smooth integrands — much faster than O(1/√N). However, the advantage diminishes in high dimensions (d > 20 or so) because the (log N)^d factor becomes large.

Halton sequences use different primes for each dimension. Lattice rules (rank-1 lattices) are popular for Bayesian integration. PyTorch includes torch.quasirandom.SobolEngine for QMC sampling, making it easy to use in ML experiments (hyperparameter search, integration in normalizing flows).

```python
import numpy as np
from scipy.stats.qmc import Sobol, Halton
import warnings; warnings.filterwarnings('ignore')

rng = np.random.default_rng(42)

# Compare random MC vs Sobol QMC for pi estimation
def estimate_pi(samples_2d):
    x, y = samples_2d[:, 0], samples_2d[:, 1]
    return 4 * np.mean(x**2 + y**2 <= 1)

print("=== MC vs QMC: estimating pi ===")
for N in [256, 1024, 4096, 16384]:
    # Random MC
    mc_samples  = rng.uniform(0, 1, (N, 2))
    mc_pi       = estimate_pi(mc_samples)
    mc_err      = abs(mc_pi - np.pi)

    # Sobol QMC
    sobol = Sobol(d=2, scramble=True, seed=42)
    qmc_samples = sobol.random(N)
    qmc_pi  = estimate_pi(qmc_samples)
    qmc_err = abs(qmc_pi - np.pi)

    print(f"  N={N:>6,}: MC_err={mc_err:.4f}  QMC_err={qmc_err:.4f}  ratio={mc_err/qmc_err:.1f}x")

# Sobol for hyperparameter search (better coverage than random grid)
print("\n=== Sobol for 3D Hyperparameter Search ===")
sobol3 = Sobol(d=3, scramble=True, seed=0)
hp_samples = sobol3.random(16)  # 16 configs in [0,1]^3
# Map to actual hyperparameter ranges
lr     = 10 ** (hp_samples[:, 0] * (-4) + (-2))  # [1e-4, 1e-2] log-scale
wd     = 10 ** (hp_samples[:, 1] * (-6) + (-2))  # [1e-6, 1e-2] log-scale
drop   = hp_samples[:, 2] * 0.5                   # [0, 0.5]
for i in range(4):
    print(f"  config {i}: lr={lr[i]:.2e}  wd={wd[i]:.2e}  dropout={drop[i]:.3f}")
```

## Monte Carlo Policy Evaluation (RL)

In reinforcement learning, Monte Carlo (MC) policy evaluation estimates the value function V^π(s) = E[G_t | S_t = s] by averaging the actual returns G_t observed from state s when following policy π. Unlike temporal difference (TD) methods, MC uses full episode returns and does not bootstrap.

For episodic MDPs:
1. Generate episode: S₀, A₀, R₁, S₁, A₁, R₂, …, S_T following policy π
2. Compute returns: G_t = R_{t+1} + γ R_{t+2} + … + γ^{T-t-1} R_T
3. Update: V(S_t) ← V(S_t) + α(G_t − V(S_t))  [incremental mean]

Every-visit MC averages over all visits to state s in all episodes. First-visit MC averages only the first visit per episode (gives unbiased estimate of V^π(s)). MC is unbiased but high-variance; TD is biased but lower-variance. The bias-variance tradeoff between MC and TD is controlled by n-step returns and λ in TD(λ).

```python
import numpy as np

# Simple GridWorld MDP for Monte Carlo policy evaluation
class GridWorld:
    """4x4 grid, absorbing corners at (0,0) and (3,3), reward -1 per step."""
    def __init__(self, size=4):
        self.size = size
        self.terminal = {(0,0), (size-1, size-1)}
        self.actions = [(0,1),(0,-1),(1,0),(-1,0)]  # R,L,D,U

    def step(self, state, action):
        if state in self.terminal:
            return state, 0.0, True
        r, c = state
        dr, dc = action
        nr, nc = np.clip(r+dr, 0, self.size-1), np.clip(c+dc, 0, self.size-1)
        new_state = (nr, nc)
        done = new_state in self.terminal
        return new_state, -1.0, done

def generate_episode(env, policy, max_steps=200):
    """Generate one episode following policy."""
    s = (np.random.randint(env.size), np.random.randint(env.size))
    while s in env.terminal:
        s = (np.random.randint(env.size), np.random.randint(env.size))
    trajectory = []
    for _ in range(max_steps):
        a = policy(s)
        s_next, r, done = env.step(s, a)
        trajectory.append((s, a, r))
        s = s_next
        if done: break
    return trajectory

def mc_policy_evaluation(env, policy, n_episodes=5000, gamma=0.99):
    """First-visit Monte Carlo policy evaluation."""
    V = {}; returns = {}
    for ep in range(n_episodes):
        traj = generate_episode(env, policy)
        G = 0.0
        visited = set()
        for s, a, r in reversed(traj):
            G = r + gamma * G
            if s not in visited:  # first-visit
                visited.add(s)
                returns.setdefault(s, []).append(G)
                V[s] = np.mean(returns[s])
    return V

np.random.seed(42)
env = GridWorld(4)
# Random policy: uniform over 4 actions
policy = lambda s: env.actions[np.random.randint(4)]

V = mc_policy_evaluation(env, policy, n_episodes=10000)
print("=== Value Function (random policy, gamma=0.99) ===")
grid = np.zeros((4, 4))
for (r, c), v in V.items():
    grid[r, c] = v
for i, row in enumerate(grid):
    print(f"  row {i}: {[f'{v:6.1f}' for v in row]}")
print("  (0,0) and (3,3) are terminal states with value 0)")
```

## Pitfalls

Common Monte Carlo mistakes:

1. **Insufficient samples for high-variance integrands**: if f(x) has heavy tails, the empirical variance estimate is unreliable and SE estimates are too optimistic. Check for outliers.

2. **Correlated samples without accounting for it**: MCMC samples are correlated. Treating them as independent underestimates the true SE by up to √(2τ) where τ is the autocorrelation time.

3. **Using QMC when samples are not i.i.d.**: Sobol and Halton sequences are designed for integration, not for probabilistic sampling. Using them as 'random' samples in probabilistic algorithms (e.g., Bayesian optimisation acquisition) can give overconfident estimates.

4. **Forgetting that 1/√N convergence is slow**: going from 1% to 0.1% error requires 100× more samples. Variance reduction techniques or better estimators are often more cost-effective than brute-force sample increase.

## Practical Guidance

Guidelines for Monte Carlo in ML:

- **Always estimate the SE**: report SE = std(f(xᵢ)) / √N alongside the estimate. If SE > desired accuracy, increase N or apply variance reduction.
- **For hyperparameter search**: use Sobol sequences instead of random search — same number of evaluations, better coverage, especially for d ≤ 20 dimensions.
- **For integration in deep learning** (ELBO estimation, policy gradient): use control variates (e.g., baseline subtraction in REINFORCE) to reduce gradient variance.
- **For MCMC**: compute the effective sample size ESS = N / (1 + 2 Σₖ ρₖ) where ρₖ is the lag-k autocorrelation. ESS << N indicates poor mixing and inflated SE.

> **TIP: Control Variates in REINFORCE**
>
> The REINFORCE gradient estimator ∇θ E[R] = E[R ∇θ log π(a|s,θ)] has high variance. Subtracting a baseline b(s) (control variate): ∇θ E[R] = E[(R − b(s)) ∇θ log π(a|s,θ)]. The baseline does not bias the gradient because E[b(s) ∇θ log π] = 0. A common choice is the value function estimate V(s) as the baseline — this is the advantage actor-critic method.

| Method | Convergence | Strengths | Weaknesses |
| --- | --- | --- | --- |
| Standard MC | O(1/√N) | Simple, unbiased, dimension-free | High variance for smooth integrands |
| Control variates | Better O(1/√N) | Can give 10x+ speedup | Requires correlated estimator with known mean |
| Antithetic variates | Better O(1/√N) | Easy to implement | Only works for monotone integrands |
| Stratified sampling | O(1/N) for 1D | Guaranteed coverage | Hard to extend to high dimensions |
| Sobol QMC | ~O(1/N) | Best for d<20, smooth f | Not probabilistically valid samples |
| MCMC (Metropolis) | O(1/√N_eff) | Can sample from unnormalised p | Correlated samples; slow mixing |

---

## Key Takeaways

- MC integration: Ê[f] = (1/N) Σ f(xᵢ) with xᵢ~p converges at O(1/√N) independent of dimension — the key advantage over classical quadrature.
- SE = σ_f / √N: to halve the error requires 4× samples; variance reduction is often more cost-effective than increasing N.
- Control variates (subtract a term with known expectation), antithetic variates (use paired reflections), and stratified sampling all reduce variance without increasing N.
- Sobol quasi-Monte Carlo achieves ~O(1/N) convergence for smooth d<20 integrands by replacing random samples with low-discrepancy deterministic sequences.
- In RL, first-visit Monte Carlo policy evaluation averages full episode returns from each first visit to a state — unbiased but high variance compared to TD methods.
- Always report SE alongside MC estimates; for MCMC samples compute ESS to account for autocorrelation before interpreting the SE.
- Control variates appear in RL as baselines (advantage actor-critic), in variational inference as variance reduction for ELBO gradient estimates.
