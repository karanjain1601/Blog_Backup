---
title: "GP Prior — Sampling Functions and Prior Specification"
slug: "gp-prior-sampling"
description: "How a GP prior f~GP(m,k) encodes beliefs about functions before data: Cholesky sampling, kernel choice, length-scale and signal variance effects, and prior predictive checks."
tags: ["gaussian-processes", "kernel-methods", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoYXQgSXMgYSBHUCBQcmlvcj8ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgR2F1c3NpYW4gUHJvY2VzcyAoR1ApIGlzIGEgZGlzdHJpYnV0aW9uIG92ZXIgZnVuY3Rpb25zLiBXcml0aW5nIGYgfiBHUChtLCBrKSBtZWFuczogYW55IGZpbml0ZSBjb2xsZWN0aW9uIG9mIGZ1bmN0aW9uIHZhbHVlcyAoZih44oKBKSwg4oCmLCBmKHjigpkpKSBmb2xsb3dzIGEgbXVsdGl2YXJpYXRlIG5vcm1hbCBkaXN0cmlidXRpb24gd2l0aCBtZWFuIHZlY3RvciBbbSh44oKBKSwg4oCmLCBtKHjigpkpXSBhbmQgY292YXJpYW5jZSBtYXRyaXggS+G1ouKxvCA9IGsoeOG1oiwgeOKxvCkuIFRoZSBwcmlvciBlbmNvZGVzIGV2ZXJ5dGhpbmcgd2UgYmVsaWV2ZSBhYm91dCB0aGUgZnVuY3Rpb24gYmVmb3JlIG9ic2VydmluZyBkYXRhIOKAlCBpdHMgc21vb3RobmVzcywgYW1wbGl0dWRlLCBhbmQgbWVhbiB0cmVuZC4gVW5saWtlIHBhcmFtZXRyaWMgbW9kZWxzLCB0aGUgcHJpb3IgbGl2ZXMgZGlyZWN0bHkgaW4gZnVuY3Rpb24gc3BhY2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2FtcGxpbmcgZnJvbSBhIEdQIFByaW9yIHdpdGggQ2hvbGVza3kgRGVjb21wb3NpdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG8gZHJhdyBhIGZ1bmN0aW9uIHNhbXBsZTogKDEpIGNob29zZSBhIHNldCBvZiB0ZXN0IHBvaW50cyBYKiwgKDIpIGNvbXB1dGUgdGhlIGNvdmFyaWFuY2UgbWF0cml4IEsgPSBrKFgqLCBYKiksICgzKSBhZGQgYSBzbWFsbCBqaXR0ZXIgzrVJIGZvciBudW1lcmljYWwgc3RhYmlsaXR5LCAoNCkgY29tcHV0ZSB0aGUgQ2hvbGVza3kgZmFjdG9yIEwgPSBjaG9sKEsgKyDOtUkpLCAoNSkgZHJhdyB6IH4gTigwLCBJKSwgKDYpIHJldHVybiBmID0gbShYKikgKyBMei4gVGhlIENob2xlc2t5IG1ldGhvZCBpcyBwcmVmZXJyZWQgb3ZlciBlaWdlbmRlY29tcG9zaXRpb24gZm9yIG51bWVyaWNhbCBzdGFiaWxpdHkgYW5kIGdpdmVzIHNhbXBsZXMgd2l0aCBleGFjdGx5IHRoZSByaWdodCBtYXJnaW5hbCBjb3ZhcmlhbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBsZW5ndGhfc2NhbGU9MS4wLCBzaWduYWxfdmFyPTEuMCk6XG4gICAgXCJcIlwiU3F1YXJlZCBFeHBvbmVudGlhbCAoUkJGKSBrZXJuZWwgayh4LHhcdTAwMjcpID0gz4PCsl9mIGV4cCgtfHx4LXhcdTAwMjd8fMKyLygy4oSTwrIpKVwiXCJcIlxuICAgIFgxID0gbnAuYXRsZWFzdF8yZChYMSkucmVzaGFwZSgtMSwgMSlcbiAgICBYMiA9IG5wLmF0bGVhc3RfMmQoWDIpLnJlc2hhcGUoLTEsIDEpXG4gICAgc3FkaXN0ID0gbnAuc3VtKFgxKioyLCAxKS5yZXNoYXBlKC0xLDEpICsgbnAuc3VtKFgyKioyLCAxKSAtIDIqWDFAWDIuVFxuICAgIHJldHVybiBzaWduYWxfdmFyICogbnAuZXhwKC0wLjUgKiBzcWRpc3QgLyBsZW5ndGhfc2NhbGUqKjIpXG5cbmRlZiBzYW1wbGVfZ3BfcHJpb3IoeCwga2VybmVsX2ZuLCBuX3NhbXBsZXM9NSwgaml0dGVyPTFlLTYsICoqa2VybmVsX2t3YXJncyk6XG4gICAgSyA9IGtlcm5lbF9mbih4LCB4LCAqKmtlcm5lbF9rd2FyZ3MpXG4gICAgTCA9IG5wLmxpbmFsZy5jaG9sZXNreShLICsgaml0dGVyICogbnAuZXllKGxlbih4KSkpXG4gICAgeiA9IG5wLnJhbmRvbS5yYW5kbihsZW4oeCksIG5fc2FtcGxlcylcbiAgICByZXR1cm4gTCBAIHogICAjIHNoYXBlIChuX3BvaW50cywgbl9zYW1wbGVzKVxuXG5ucC5yYW5kb20uc2VlZCg0MilcbnggPSBucC5saW5zcGFjZSgtNSwgNSwgMjAwKVxuc2FtcGxlcyA9IHNhbXBsZV9ncF9wcmlvcih4LCByYmZfa2VybmVsLCBuX3NhbXBsZXM9NSwgbGVuZ3RoX3NjYWxlPTEuMCwgc2lnbmFsX3Zhcj0xLjApXG5cbnBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsIDQpKVxuZm9yIGkgaW4gcmFuZ2UoNSk6XG4gICAgcGx0LnBsb3QoeCwgc2FtcGxlc1s6LCBpXSwgbHc9MS41LCBhbHBoYT0wLjgsIGxhYmVsPWZcdTAwMjdTYW1wbGUge2krMX1cdTAwMjcpXG5wbHQuYXhobGluZSgwLCBjb2xvcj1cdTAwMjdrXHUwMDI3LCBsdz0wLjgsIGxzPVx1MDAyNy0tXHUwMDI3LCBsYWJlbD1cdTAwMjdNZWFuIG0oeCk9MFx1MDAyNylcbnBsdC50aXRsZShcdTAwMjdHUCBQcmlvciBTYW1wbGVzIOKAlCBSQkYgS2VybmVsICjihJM9MSwgz4PCsl9mPTEpXHUwMDI3KVxucGx0LnhsYWJlbChcdTAwMjd4XHUwMDI3KTsgcGx0LnlsYWJlbChcdTAwMjdmKHgpXHUwMDI3KTsgcGx0LmxlZ2VuZChuY29sPTMpOyBwbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXJuZWwgRnVuY3Rpb25zIGFuZCBQcmlvciBTbW9vdGhuZXNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUga2VybmVsIGsoeCwgeFx1MDAyNykgY29tcGxldGVseSBkZXRlcm1pbmVzIHRoZSBzbW9vdGhuZXNzIGFuZCBjb3JyZWxhdGlvbiBzdHJ1Y3R1cmUgb2YgcHJpb3Igc2FtcGxlcy4gVGhlIFJCRiBrZXJuZWwgcHJvZHVjZXMgaW5maW5pdGVseSBkaWZmZXJlbnRpYWJsZSAoYW5hbHl0aWMpIGZ1bmN0aW9ucy4gVGhlIE1hdMOpcm4gZmFtaWx5IHBhcmFtZXRlcmlzZXMgc21vb3RobmVzcyB2aWEgzr06IE1hdMOpcm4tMS8yIGdpdmVzIGNvbnRpbnVvdXMgYnV0IG5vd2hlcmUtZGlmZmVyZW50aWFibGUgcGF0aHMgKGxpa2UgQnJvd25pYW4gbW90aW9uKSwgTWF0w6lybi0zLzIgZ2l2ZXMgb25jZS1kaWZmZXJlbnRpYWJsZSBwYXRocywgYW5kIE1hdMOpcm4tNS8yIGdpdmVzIHR3aWNlLWRpZmZlcmVudGlhYmxlIHBhdGhzLiBDaG9pY2Ugb2Yga2VybmVsIGVuY29kZXMgZG9tYWluIGtub3dsZWRnZSBhYm91dCB0aGUgZnVuY3Rpb25cdTAwMjdzIHJlZ3VsYXJpdHkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBzY2lweS5zcGF0aWFsLmRpc3RhbmNlIGltcG9ydCBjZGlzdFxuXG5kZWYgbWF0ZXJuX2tlcm5lbChYMSwgWDIsIGxlbmd0aF9zY2FsZT0xLjAsIHNpZ25hbF92YXI9MS4wLCBudT0xLjUpOlxuICAgIFgxID0gbnAuYXRsZWFzdF8yZChYMSkucmVzaGFwZSgtMSwgMSlcbiAgICBYMiA9IG5wLmF0bGVhc3RfMmQoWDIpLnJlc2hhcGUoLTEsIDEpXG4gICAgciA9IGNkaXN0KFgxLCBYMikgLyBsZW5ndGhfc2NhbGVcbiAgICBpZiBudSA9PSAwLjU6XG4gICAgICAgIHJldHVybiBzaWduYWxfdmFyICogbnAuZXhwKC1yKVxuICAgIGVsaWYgbnUgPT0gMS41OlxuICAgICAgICByZXR1cm4gc2lnbmFsX3ZhciAqICgxICsgbnAuc3FydCgzKSpyKSAqIG5wLmV4cCgtbnAuc3FydCgzKSpyKVxuICAgIGVsaWYgbnUgPT0gMi41OlxuICAgICAgICByZXR1cm4gc2lnbmFsX3ZhciAqICgxICsgbnAuc3FydCg1KSpyICsgNSpyKioyLzMpICogbnAuZXhwKC1ucC5zcXJ0KDUpKnIpXG4gICAgZWxzZTpcbiAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihmXHUwMDI3bnU9e251fSBub3Qgc3VwcG9ydGVkXHUwMDI3KVxuXG5ucC5yYW5kb20uc2VlZCgwKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG5rZXJuZWxzID0gWyhcdTAwMjdSQkYgKOKIni1kaWZmKVx1MDAyNywgbGFtYmRhIFgxLFgyOiBtYXRlcm5fa2VybmVsKFgxLFgyLG51PTIuNSkqMCtcbiAgICAgICAgICAgIF9faW1wb3J0X18oXHUwMDI3bnVtcHlcdTAwMjcpLmV4cCgtMC41KmNkaXN0KG5wLmF0bGVhc3RfMmQoWDEpLnJlc2hhcGUoLTEsMSksXG4gICAgICAgICAgICBucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLDEpKSoqMikpLFxuICAgICAgICAgICAoXHUwMDI3TWF0w6lybi0xLzJcdTAwMjcsIGxhbWJkYSBYMSxYMjogbWF0ZXJuX2tlcm5lbChYMSxYMixudT0wLjUpKSxcbiAgICAgICAgICAgKFx1MDAyN01hdMOpcm4tNS8yXHUwMDI3LCBsYW1iZGEgWDEsWDI6IG1hdGVybl9rZXJuZWwoWDEsWDIsbnU9Mi41KSldXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAzLCBmaWdzaXplPSgxNCwgNCksIHNoYXJleT1UcnVlKVxuZm9yIGF4LCAobmFtZSwga2ZuKSBpbiB6aXAoYXhlcywga2VybmVscyk6XG4gICAgSyA9IGtmbih4LCB4KVxuICAgIEwgPSBucC5saW5hbGcuY2hvbGVza3koSyArIDFlLTYqbnAuZXllKGxlbih4KSkpXG4gICAgZm9yIF8gaW4gcmFuZ2UoNCk6XG4gICAgICAgIGF4LnBsb3QoeCwgTCBAIG5wLnJhbmRvbS5yYW5kbihsZW4oeCkpLCBsdz0xLjIsIGFscGhhPTAuOClcbiAgICBheC5zZXRfdGl0bGUobmFtZSk7IGF4LnNldF94bGFiZWwoXHUwMDI3eFx1MDAyNylcbmF4ZXNbMF0uc2V0X3lsYWJlbChcdTAwMjdmKHgpXHUwMDI3KVxucGx0LnN1cHRpdGxlKFx1MDAyN1ByaW9yIFNhbXBsZXMgYnkgS2VybmVsIFNtb290aG5lc3MgQ2xhc3NcdTAwMjcpXG5wbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zaG93KCkifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiS2VybmVsIiwiRGlmZmVyZW50aWFiaWxpdHkiLCJUeXBpY2FsIOKEkyBSYW5nZSIsIkJlc3QgRG9tYWluIl0sInJvd3MiOltbIlJCRiAoU0UpIiwiSW5maW5pdGVseSBkaWZmZXJlbnRpYWJsZSAoYW5hbHl0aWMpIiwiMC4xIOKAkyAxMCIsIlBoeXNpY3Mgc2ltdWxhdGlvbnMsIHNtb290aCBzaWduYWxzIl0sWyJNYXTDqXJuLTEvMiIsIkNvbnRpbnVvdXMsIG5vdCBkaWZmZXJlbnRpYWJsZSIsIjAuMDUg4oCTIDUiLCJSb3VnaCB0ZXJyYWluLCBmaW5hbmNpYWwgcmV0dXJucyJdLFsiTWF0w6lybi0zLzIiLCJPbmNlIGRpZmZlcmVudGlhYmxlIiwiMC4xIOKAkyA1IiwiUm9ib3RpY3MsIHNwZWVjaCBmZWF0dXJlcyJdLFsiTWF0w6lybi01LzIiLCJUd2ljZSBkaWZmZXJlbnRpYWJsZSIsIjAuMSDigJMgMTAiLCJHZW5lcmFsIHJlZ3Jlc3Npb24sIG1vc3QgdGFidWxhciBkYXRhIl0sWyJQZXJpb2RpYyIsIkluZmluaXRlbHkgZGlmZmVyZW50aWFibGUsIHBlcmlvZGljIiwicGVyaW9kOiAwLjXigJM1MCIsIlNlYXNvbmFsaXR5LCBjeWNsaWMgcHJvY2Vzc2VzIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFZmZlY3Qgb2YgTGVuZ3RoLVNjYWxlIG9uIEZ1bmN0aW9uIFNtb290aG5lc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsZW5ndGgtc2NhbGUg4oSTIGNvbnRyb2xzIHRoZSBjb3JyZWxhdGlvbiByYW5nZTogayh4LCB4XHUwMDI3KSBkZWNheXMgYXMgfHjiiJJ4XHUwMDI3fCBncm93cyByZWxhdGl2ZSB0byDihJMuIExhcmdlIOKEkyBtZWFucyBwb2ludHMgZmFyIGFwYXJ0IGFyZSBzdGlsbCBjb3JyZWxhdGVkIOKAlCBwcmlvciBzYW1wbGVzIGFyZSBzbG93bHkgdmFyeWluZyBhbmQgc21vb3RoLiBTbWFsbCDihJMgbWVhbnMgdGhlIGNvcnJlbGF0aW9uIGRlY2F5cyBxdWlja2x5IOKAlCBwcmlvciBzYW1wbGVzIGFyZSB3aWdnbHkgYW5kIG5lYXJseSBpbmRlcGVuZGVudCBhdCBkaXN0YW5jZXMgbGFyZ2VyIHRoYW4g4oSTLiBUaGUgc2lnbmFsIHZhcmlhbmNlIM+DwrJfZiBzY2FsZXMgdGhlIG92ZXJhbGwgYW1wbGl0dWRlIG9mIHRoZSBmdW5jdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgZWxsPTEuMCwgc2YyPTEuMCk6XG4gICAgWDEgPSBucC5hdGxlYXN0XzJkKFgxKS5yZXNoYXBlKC0xLCAxKVxuICAgIFgyID0gbnAuYXRsZWFzdF8yZChYMikucmVzaGFwZSgtMSwgMSlcbiAgICBzcWRpc3QgPSAoWDEgLSBYMi5UKSoqMlxuICAgIHJldHVybiBzZjIgKiBucC5leHAoLTAuNSAqIHNxZGlzdCAvIGVsbCoqMilcblxubnAucmFuZG9tLnNlZWQoNylcbnggPSBucC5saW5zcGFjZSgtNSwgNSwgMjAwKVxubGVuZ3RoX3NjYWxlcyA9IFswLjMsIDEuMCwgMy4wXVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMSwgMywgZmlnc2l6ZT0oMTQsIDQpLCBzaGFyZXk9VHJ1ZSlcbmZvciBheCwgZWxsIGluIHppcChheGVzLCBsZW5ndGhfc2NhbGVzKTpcbiAgICBLID0gcmJmX2tlcm5lbCh4LCB4LCBlbGw9ZWxsKVxuICAgIEwgPSBucC5saW5hbGcuY2hvbGVza3koSyArIDFlLTYqbnAuZXllKGxlbih4KSkpXG4gICAgZm9yIF8gaW4gcmFuZ2UoNSk6XG4gICAgICAgIGYgPSBMIEAgbnAucmFuZG9tLnJhbmRuKGxlbih4KSlcbiAgICAgICAgYXgucGxvdCh4LCBmLCBsdz0xLjIsIGFscGhhPTAuNzUpXG4gICAgYXguc2V0X3RpdGxlKGZcdTAwMjfihJMgPSB7ZWxsfVx1MDAyNylcbiAgICBheC5zZXRfeGxhYmVsKFx1MDAyN3hcdTAwMjcpXG4gICAgYXguc2V0X3lsaW0oLTMuNSwgMy41KVxuYXhlc1swXS5zZXRfeWxhYmVsKFx1MDAyN2YoeClcdTAwMjcpXG5wbHQuc3VwdGl0bGUoXHUwMDI3UkJGIFByaW9yIFNhbXBsZXM6IEVmZmVjdCBvZiBMZW5ndGgtU2NhbGVcdTAwMjcpXG5wbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zaG93KClcblxuIyBQcmludCBjb3JyZWxhdGlvbiBhdCBkaWZmZXJlbnQgZGlzdGFuY2VzXG5mb3IgZWxsIGluIGxlbmd0aF9zY2FsZXM6XG4gICAgcjEgPSBucC5leHAoLTAuNSAqIDEuMCoqMiAvIGVsbCoqMilcbiAgICByMiA9IG5wLmV4cCgtMC41ICogMi4wKioyIC8gZWxsKioyKVxuICAgIHByaW50KGZcdTAwMjfihJM9e2VsbH06IGNvcnIozpQ9MSk9e3IxOi4zZn0sIGNvcnIozpQ9Mik9e3IyOi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IkNob29zaW5nIExlbmd0aC1TY2FsZSBmcm9tIERvbWFpbiBLbm93bGVkZ2UiLCJjb250ZW50IjoiSWYgeW91IGtub3cgdGhhdCB5b3VyIGZ1bmN0aW9uIGNoYW5nZXMgbWVhbmluZ2Z1bGx5IG92ZXIgYSBkaXN0YW5jZSBvZiByb3VnaGx5IGQgdW5pdHMsIGluaXRpYWxpc2Ug4oSTIOKJiCBkLiBGb3Igc3BhdGlhbCBkYXRhIGluIGtpbG9tZXRyZXMsIOKEkyBpbiB0aGUgdGVucy4gRm9yIG5vcm1hbGlzZWQgZmVhdHVyZXMgaW4gWzAsMV0sIOKEkyBiZXR3ZWVuIDAuMSBhbmQgMC41LiBBbHdheXMgdmVyaWZ5IHlvdXIgY2hvaWNlIHdpdGggYSBwcmlvciBwcmVkaWN0aXZlIGNoZWNrLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByaW9yIFByZWRpY3RpdmUgQ2hlY2tzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIHByaW9yIHByZWRpY3RpdmUgY2hlY2sgYXNrczogZG8gcmFuZG9tIGRyYXdzIGZyb20gdGhlIHByaW9yIGxvb2sgbGlrZSBwbGF1c2libGUgZGF0YT8gUGxvdCAxMOKAkzIwIHByaW9yIHNhbXBsZXMgb3ZlcmxhaWQgb24gdGhlIGRvbWFpbi4gSWYgdGhlIHByaW9yIGFtcGxpdHVkZSBpcyB3aWxkbHkgd3JvbmcgKGFsbCBzYW1wbGVzIG5lYXIgMCB3aGVuIHRoZSBkYXRhIHNwYW5zIDEwMCB1bml0cyksIGFkanVzdCDPg8KyX2YuIElmIHRoZSB3aWdnbGVzIGFyZSBmYXIgdG9vIGZhc3QsIGluY3JlYXNlIOKEky4gVGhpcyBpcyBhbiBpbXBvcnRhbnQgZGlhZ25vc3RpYyBiZWZvcmUgc3BlbmRpbmcgY29tcHV0ZSBvbiBwb3N0ZXJpb3IgaW5mZXJlbmNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBlbGw9MS4wLCBzZjI9MS4wKTpcbiAgICBYMSA9IG5wLmF0bGVhc3RfMmQoWDEpLnJlc2hhcGUoLTEsIDEpXG4gICAgWDIgPSBucC5hdGxlYXN0XzJkKFgyKS5yZXNoYXBlKC0xLCAxKVxuICAgIHJldHVybiBzZjIgKiBucC5leHAoLTAuNSAqIChYMSAtIFgyLlQpKioyIC8gZWxsKioyKVxuXG5ucC5yYW5kb20uc2VlZCg5OSlcbiMgU3VwcG9zZSB3ZSBleHBlY3QgZnVuY3Rpb24gdmFsdWVzIGluIFswLCAxMF0gb3ZlciB4IGluIFswLCA1XVxueCA9IG5wLmxpbnNwYWNlKDAsIDUsIDE1MClcblxuIyBCYWQgcHJpb3I6IGRlZmF1bHQgcGFyYW1zIG1pc2FsaWduZWQgd2l0aCBkb21haW5cbktfYmFkID0gcmJmX2tlcm5lbCh4LCB4LCBlbGw9MC4xLCBzZjI9MS4wKVxuTF9iYWQgPSBucC5saW5hbGcuY2hvbGVza3koS19iYWQgKyAxZS02Km5wLmV5ZShsZW4oeCkpKVxuXG4jIEdvb2QgcHJpb3I6IGRvbWFpbi1pbmZvcm1lZCBwYXJhbXNcbktfZ29vZCA9IHJiZl9rZXJuZWwoeCwgeCwgZWxsPTEuNSwgc2YyPTI1LjApICAjIHNmPTUgLVx1MDAzZSBhbXBsaXR1ZGUgfjUsIGVsbD0xLjVcbkxfZ29vZCA9IG5wLmxpbmFsZy5jaG9sZXNreShLX2dvb2QgKyAxZS02Km5wLmV5ZShsZW4oeCkpKVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMSwgMiwgZmlnc2l6ZT0oMTIsIDQpKVxuZm9yIGkgaW4gcmFuZ2UoOCk6XG4gICAgYXhlc1swXS5wbG90KHgsIExfYmFkIEAgbnAucmFuZG9tLnJhbmRuKGxlbih4KSksIGx3PTEsIGFscGhhPTAuNilcbiAgICBheGVzWzFdLnBsb3QoeCwgNSArIExfZ29vZCBAIG5wLnJhbmRvbS5yYW5kbihsZW4oeCkpLCBsdz0xLCBhbHBoYT0wLjYpXG5heGVzWzBdLnNldF90aXRsZShcdTAwMjdCYWQgUHJpb3IgKOKEkz0wLjEsIM+DwrJfZj0xKSDigJQgdG9vIHdpZ2dseSwgd3Jvbmcgc2NhbGVcdTAwMjcpXG5heGVzWzFdLnNldF90aXRsZShcdTAwMjdEb21haW4tSW5mb3JtZWQgUHJpb3IgKOKEkz0xLjUsIM+DwrJfZj0yNSkg4oCUIHBsYXVzaWJsZVx1MDAyNylcbmZvciBheCBpbiBheGVzOlxuICAgIGF4LnNldF94bGFiZWwoXHUwMDI3eFx1MDAyNyk7IGF4LnNldF95bGFiZWwoXHUwMDI3Zih4KVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKTsgcGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNob29zaW5nIEtlcm5lbHMgZnJvbSBEb21haW4gS25vd2xlZGdlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJLZXJuZWwgc2VsZWN0aW9uIGlzIHRoZSBwcmltYXJ5IG1vZGVsbGluZyBkZWNpc2lvbiBpbiBHUCByZWdyZXNzaW9uLiBVc2UgdGhlIFJCRiBrZXJuZWwgYXMgYSBiYXNlbGluZSB3aGVuIHlvdSBleHBlY3QgYSBzbW9vdGggZnVuY3Rpb24gd2l0aCBubyBzdHJvbmcgcGVyaW9kaWNpdHkuIFByZWZlciBNYXTDqXJuLTUvMiBmb3IgbW9zdCByZWdyZXNzaW9uIHRhc2tzIOKAlCBpdCBpcyBzbW9vdGggZW5vdWdoIGZvciBncmFkaWVudC1iYXNlZCBvcHRpbWlzYXRpb24gYnV0IGxlc3MgcHJvbmUgdG8gb3ZlcmZpdHRpbmcgd2lnZ2x5IGFydGVmYWN0cyB0aGFuIFJCRi4gVXNlIHBlcmlvZGljIGtlcm5lbHMgZm9yIHNlYXNvbmFsIHRpbWUgc2VyaWVzLiBDb21wb3NpdGUga2VybmVscyAoZS5nLiwgUkJGICsgcGVyaW9kaWMgKyBsaW5lYXIpIGRlY29tcG9zZSBzaWduYWxzIGludG8gaW50ZXJwcmV0YWJsZSBjb21wb25lbnRzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUkJGOiBkZWZhdWx0IGZvciBzbW9vdGgsIG5vbi1wZXJpb2RpYyBmdW5jdGlvbnM7IGRpZmZlcmVudGlhYmxlIGV2ZXJ5d2hlcmUiLCJNYXTDqXJuLTUvMjogYmV0dGVyIGdlbmVyYWxpc2F0aW9uIHRoYW4gUkJGIGluIG1vc3QgcmVhbC13b3JsZCB0YWJ1bGFyIHRhc2tzIiwiTWF0w6lybi0xLzI6IHJvdWdoIHByb2Nlc3NlcyDigJQgd2VhdGhlciwgZmluYW5jaWFsIGxvZy1yZXR1cm5zIiwiUGVyaW9kaWM6IHNlYXNvbmFsaXR5IHdpdGgga25vd24gcGVyaW9kIChlLmcuLCB5ZWFybHksIHdlZWtseSkiLCJMaW5lYXIga2VybmVsOiBHUCBiZWNvbWVzIEJheWVzaWFuIGxpbmVhciByZWdyZXNzaW9uIOKAlCB1c2VmdWwgYXMgYSBiYXNlbGluZSBjb21wb25lbnQiLCJDb21wb3NpdGUgayA9IGvigoEgKyBr4oKCOiBhZGRpdGl2ZSBzdHJ1Y3R1cmU7IGsgPSBr4oKBIMOXIGvigoI6IGludGVyYWN0aW9uIHRlcm1zIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBHUCBwcmlvciBmIH4gR1AobSwgaykgZGVmaW5lcyBhIGRpc3RyaWJ1dGlvbiBvdmVyIGZ1bmN0aW9ucyB2aWEgaXRzIG1lYW4gZnVuY3Rpb24gbSBhbmQga2VybmVsIGsuIFNhbXBsaW5nIHVzZXMgdGhlIENob2xlc2t5IGRlY29tcG9zaXRpb24gb2YgdGhlIGtlcm5lbCBtYXRyaXg6IGYgPSBtICsgTHogd2hlcmUgTCA9IGNob2woSyArIM61SSkgYW5kIHogfiBOKDAsIEkpLiBLZXJuZWwgY2hvaWNlIGRldGVybWluZXMgZGlmZmVyZW50aWFiaWxpdHkgKFJCRiDihpIgc21vb3RoLCBNYXTDqXJuLTEvMiDihpIgcm91Z2gpLiBMZW5ndGgtc2NhbGUg4oSTIGNvbnRyb2xzIGNvcnJlbGF0aW9uIHJhbmdlOyBzaWduYWwgdmFyaWFuY2Ugz4PCsl9mIGNvbnRyb2xzIGFtcGxpdHVkZS4gQWx3YXlzIHJ1biBhIHByaW9yIHByZWRpY3RpdmUgY2hlY2sgYmVmb3JlIGZpdHRpbmcg4oCUIGl0IGNhdGNoZXMgbWlzY29uZmlndXJlZCBoeXBlcnBhcmFtZXRlcnMgYmVmb3JlIGV4cGVuc2l2ZSBpbmZlcmVuY2UuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJOdW1lcmljYWwgU3RhYmlsaXR5IFJlcXVpcmVzIEppdHRlciIsImNvbnRlbnQiOiJXaXRob3V0IGEgc21hbGwgaml0dGVyIHRlcm0gzrVJIGFkZGVkIHRvIEssIHRoZSBDaG9sZXNreSBkZWNvbXBvc2l0aW9uIHdpbGwgZmFpbCBvbiBuZWFyLXNpbmd1bGFyIG1hdHJpY2VzIChlLmcuLCB3aGVuIHR3byB4LXBvaW50cyBhcmUgdmVyeSBjbG9zZSkuIEEgaml0dGVyIG9mIDFlLTYgdG8gMWUtNCBpcyBzdGFuZGFyZCBhbmQgZG9lcyBub3QgbWVhbmluZ2Z1bGx5IGFsdGVyIHRoZSBwcmlvci4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlByaW9yIGYgfiBHUChtLGspOiBtZWFuIGZ1bmN0aW9uIG0oeCkgYW5kIGtlcm5lbCBrKHgseFx1MDAyNykgZnVsbHkgc3BlY2lmeSBiZWxpZWZzIiwiQ2hvbGVza3kgc2FtcGxpbmc6IGRyYXcgen5OKDAsSSksIHJldHVybiBtICsgTHogd2hlcmUgTD1jaG9sKEsrzrVJKSIsIlJCRiBrZXJuZWwg4oaSIGluZmluaXRlbHkgZGlmZmVyZW50aWFibGU7IE1hdMOpcm4tMS8yIOKGkiBjb250aW51b3VzIG9ubHkiLCJMZW5ndGgtc2NhbGUg4oSTOiBsYXJnZSDihpIgc21vb3RoIHNsb3dseSB2YXJ5aW5nOyBzbWFsbCDihpIgd2lnZ2x5IHJhcGlkbHkgdmFyeWluZyIsIlNpZ25hbCB2YXJpYW5jZSDPg8KyX2Y6IHNjYWxlcyBvdmVyYWxsIGZ1bmN0aW9uIGFtcGxpdHVkZSIsIlByaW9yIHByZWRpY3RpdmUgY2hlY2s6IHBsb3QgMTAtMjAgcHJpb3Igc2FtcGxlcyBiZWZvcmUgZml0dGluZyB0byBkYXRhIiwiQ29tcG9zaXRlIGtlcm5lbHMgYWxsb3cgYWRkaXRpdmUgZGVjb21wb3NpdGlvbiBvZiBzaWduYWwgY29tcG9uZW50cyJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# GP Prior — Sampling Functions and Prior Specification

## What Is a GP Prior?

A Gaussian Process (GP) is a distribution over functions. Writing f ~ GP(m, k) means: any finite collection of function values (f(x₁), …, f(xₙ)) follows a multivariate normal distribution with mean vector [m(x₁), …, m(xₙ)] and covariance matrix Kᵢⱼ = k(xᵢ, xⱼ). The prior encodes everything we believe about the function before observing data — its smoothness, amplitude, and mean trend. Unlike parametric models, the prior lives directly in function space.

## Sampling from a GP Prior with Cholesky Decomposition

To draw a function sample: (1) choose a set of test points X*, (2) compute the covariance matrix K = k(X*, X*), (3) add a small jitter εI for numerical stability, (4) compute the Cholesky factor L = chol(K + εI), (5) draw z ~ N(0, I), (6) return f = m(X*) + Lz. The Cholesky method is preferred over eigendecomposition for numerical stability and gives samples with exactly the right marginal covariance.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, length_scale=1.0, signal_var=1.0):
    """Squared Exponential (RBF) kernel k(x,x') = σ²_f exp(-||x-x'||²/(2ℓ²))"""
    X1 = np.atleast_2d(X1).reshape(-1, 1)
    X2 = np.atleast_2d(X2).reshape(-1, 1)
    sqdist = np.sum(X1**2, 1).reshape(-1,1) + np.sum(X2**2, 1) - 2*X1@X2.T
    return signal_var * np.exp(-0.5 * sqdist / length_scale**2)

def sample_gp_prior(x, kernel_fn, n_samples=5, jitter=1e-6, **kernel_kwargs):
    K = kernel_fn(x, x, **kernel_kwargs)
    L = np.linalg.cholesky(K + jitter * np.eye(len(x)))
    z = np.random.randn(len(x), n_samples)
    return L @ z   # shape (n_points, n_samples)

np.random.seed(42)
x = np.linspace(-5, 5, 200)
samples = sample_gp_prior(x, rbf_kernel, n_samples=5, length_scale=1.0, signal_var=1.0)

plt.figure(figsize=(10, 4))
for i in range(5):
    plt.plot(x, samples[:, i], lw=1.5, alpha=0.8, label=f'Sample {i+1}')
plt.axhline(0, color='k', lw=0.8, ls='--', label='Mean m(x)=0')
plt.title('GP Prior Samples — RBF Kernel (ℓ=1, σ²_f=1)')
plt.xlabel('x'); plt.ylabel('f(x)'); plt.legend(ncol=3); plt.tight_layout()
plt.show()
```

## Kernel Functions and Prior Smoothness

The kernel k(x, x') completely determines the smoothness and correlation structure of prior samples. The RBF kernel produces infinitely differentiable (analytic) functions. The Matérn family parameterises smoothness via ν: Matérn-1/2 gives continuous but nowhere-differentiable paths (like Brownian motion), Matérn-3/2 gives once-differentiable paths, and Matérn-5/2 gives twice-differentiable paths. Choice of kernel encodes domain knowledge about the function's regularity.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

def matern_kernel(X1, X2, length_scale=1.0, signal_var=1.0, nu=1.5):
    X1 = np.atleast_2d(X1).reshape(-1, 1)
    X2 = np.atleast_2d(X2).reshape(-1, 1)
    r = cdist(X1, X2) / length_scale
    if nu == 0.5:
        return signal_var * np.exp(-r)
    elif nu == 1.5:
        return signal_var * (1 + np.sqrt(3)*r) * np.exp(-np.sqrt(3)*r)
    elif nu == 2.5:
        return signal_var * (1 + np.sqrt(5)*r + 5*r**2/3) * np.exp(-np.sqrt(5)*r)
    else:
        raise ValueError(f'nu={nu} not supported')

np.random.seed(0)
x = np.linspace(-4, 4, 200)
kernels = [('RBF (∞-diff)', lambda X1,X2: matern_kernel(X1,X2,nu=2.5)*0+
            __import__('numpy').exp(-0.5*cdist(np.atleast_2d(X1).reshape(-1,1),
            np.atleast_2d(X2).reshape(-1,1))**2)),
           ('Matérn-1/2', lambda X1,X2: matern_kernel(X1,X2,nu=0.5)),
           ('Matérn-5/2', lambda X1,X2: matern_kernel(X1,X2,nu=2.5))]

fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
for ax, (name, kfn) in zip(axes, kernels):
    K = kfn(x, x)
    L = np.linalg.cholesky(K + 1e-6*np.eye(len(x)))
    for _ in range(4):
        ax.plot(x, L @ np.random.randn(len(x)), lw=1.2, alpha=0.8)
    ax.set_title(name); ax.set_xlabel('x')
axes[0].set_ylabel('f(x)')
plt.suptitle('Prior Samples by Kernel Smoothness Class')
plt.tight_layout(); plt.show()
```

| Kernel | Differentiability | Typical ℓ Range | Best Domain |
| --- | --- | --- | --- |
| RBF (SE) | Infinitely differentiable (analytic) | 0.1 – 10 | Physics simulations, smooth signals |
| Matérn-1/2 | Continuous, not differentiable | 0.05 – 5 | Rough terrain, financial returns |
| Matérn-3/2 | Once differentiable | 0.1 – 5 | Robotics, speech features |
| Matérn-5/2 | Twice differentiable | 0.1 – 10 | General regression, most tabular data |
| Periodic | Infinitely differentiable, periodic | period: 0.5–50 | Seasonality, cyclic processes |

## Effect of Length-Scale on Function Smoothness

The length-scale ℓ controls the correlation range: k(x, x') decays as |x−x'| grows relative to ℓ. Large ℓ means points far apart are still correlated — prior samples are slowly varying and smooth. Small ℓ means the correlation decays quickly — prior samples are wiggly and nearly independent at distances larger than ℓ. The signal variance σ²_f scales the overall amplitude of the function.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1, 1)
    X2 = np.atleast_2d(X2).reshape(-1, 1)
    sqdist = (X1 - X2.T)**2
    return sf2 * np.exp(-0.5 * sqdist / ell**2)

np.random.seed(7)
x = np.linspace(-5, 5, 200)
length_scales = [0.3, 1.0, 3.0]

fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
for ax, ell in zip(axes, length_scales):
    K = rbf_kernel(x, x, ell=ell)
    L = np.linalg.cholesky(K + 1e-6*np.eye(len(x)))
    for _ in range(5):
        f = L @ np.random.randn(len(x))
        ax.plot(x, f, lw=1.2, alpha=0.75)
    ax.set_title(f'ℓ = {ell}')
    ax.set_xlabel('x')
    ax.set_ylim(-3.5, 3.5)
axes[0].set_ylabel('f(x)')
plt.suptitle('RBF Prior Samples: Effect of Length-Scale')
plt.tight_layout(); plt.show()

# Print correlation at different distances
for ell in length_scales:
    r1 = np.exp(-0.5 * 1.0**2 / ell**2)
    r2 = np.exp(-0.5 * 2.0**2 / ell**2)
    print(f'ℓ={ell}: corr(Δ=1)={r1:.3f}, corr(Δ=2)={r2:.3f}')
```

> **Choosing Length-Scale from Domain Knowledge**: If you know that your function changes meaningfully over a distance of roughly d units, initialise ℓ ≈ d. For spatial data in kilometres, ℓ in the tens. For normalised features in [0,1], ℓ between 0.1 and 0.5. Always verify your choice with a prior predictive check.

## Prior Predictive Checks

A prior predictive check asks: do random draws from the prior look like plausible data? Plot 10–20 prior samples overlaid on the domain. If the prior amplitude is wildly wrong (all samples near 0 when the data spans 100 units), adjust σ²_f. If the wiggles are far too fast, increase ℓ. This is an important diagnostic before spending compute on posterior inference.

```python
import numpy as np
import matplotlib.pyplot as plt

def rbf_kernel(X1, X2, ell=1.0, sf2=1.0):
    X1 = np.atleast_2d(X1).reshape(-1, 1)
    X2 = np.atleast_2d(X2).reshape(-1, 1)
    return sf2 * np.exp(-0.5 * (X1 - X2.T)**2 / ell**2)

np.random.seed(99)
# Suppose we expect function values in [0, 10] over x in [0, 5]
x = np.linspace(0, 5, 150)

# Bad prior: default params misaligned with domain
K_bad = rbf_kernel(x, x, ell=0.1, sf2=1.0)
L_bad = np.linalg.cholesky(K_bad + 1e-6*np.eye(len(x)))

# Good prior: domain-informed params
K_good = rbf_kernel(x, x, ell=1.5, sf2=25.0)  # sf=5 -> amplitude ~5, ell=1.5
L_good = np.linalg.cholesky(K_good + 1e-6*np.eye(len(x)))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for i in range(8):
    axes[0].plot(x, L_bad @ np.random.randn(len(x)), lw=1, alpha=0.6)
    axes[1].plot(x, 5 + L_good @ np.random.randn(len(x)), lw=1, alpha=0.6)
axes[0].set_title('Bad Prior (ℓ=0.1, σ²_f=1) — too wiggly, wrong scale')
axes[1].set_title('Domain-Informed Prior (ℓ=1.5, σ²_f=25) — plausible')
for ax in axes:
    ax.set_xlabel('x'); ax.set_ylabel('f(x)')
plt.tight_layout(); plt.show()
```

## Choosing Kernels from Domain Knowledge

Kernel selection is the primary modelling decision in GP regression. Use the RBF kernel as a baseline when you expect a smooth function with no strong periodicity. Prefer Matérn-5/2 for most regression tasks — it is smooth enough for gradient-based optimisation but less prone to overfitting wiggly artefacts than RBF. Use periodic kernels for seasonal time series. Composite kernels (e.g., RBF + periodic + linear) decompose signals into interpretable components.

- RBF: default for smooth, non-periodic functions; differentiable everywhere
- Matérn-5/2: better generalisation than RBF in most real-world tabular tasks
- Matérn-1/2: rough processes — weather, financial log-returns
- Periodic: seasonality with known period (e.g., yearly, weekly)
- Linear kernel: GP becomes Bayesian linear regression — useful as a baseline component
- Composite k = k₁ + k₂: additive structure; k = k₁ × k₂: interaction terms

## Key Takeaways

The GP prior f ~ GP(m, k) defines a distribution over functions via its mean function m and kernel k. Sampling uses the Cholesky decomposition of the kernel matrix: f = m + Lz where L = chol(K + εI) and z ~ N(0, I). Kernel choice determines differentiability (RBF → smooth, Matérn-1/2 → rough). Length-scale ℓ controls correlation range; signal variance σ²_f controls amplitude. Always run a prior predictive check before fitting — it catches misconfigured hyperparameters before expensive inference.

> **Numerical Stability Requires Jitter**: Without a small jitter term εI added to K, the Cholesky decomposition will fail on near-singular matrices (e.g., when two x-points are very close). A jitter of 1e-6 to 1e-4 is standard and does not meaningfully alter the prior.

- Prior f ~ GP(m,k): mean function m(x) and kernel k(x,x') fully specify beliefs
- Cholesky sampling: draw z~N(0,I), return m + Lz where L=chol(K+εI)
- RBF kernel → infinitely differentiable; Matérn-1/2 → continuous only
- Length-scale ℓ: large → smooth slowly varying; small → wiggly rapidly varying
- Signal variance σ²_f: scales overall function amplitude
- Prior predictive check: plot 10-20 prior samples before fitting to data
- Composite kernels allow additive decomposition of signal components

---

