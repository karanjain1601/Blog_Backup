---
title: "ICA — Non-Gaussianity and the FastICA Algorithm"
slug: "ica"
description: "Independent Component Analysis from the ground up: the non-Gaussianity principle, negentropy maximisation, fixed-point FastICA, the cocktail party problem, preprocessing via whitening, and applications to EEG artifact removal."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUENBIGZpbmRzIHVuY29ycmVsYXRlZCBjb21wb25lbnRzIOKAlCBjb21wb25lbnRzIHdpdGggemVybyBjb3ZhcmlhbmNlLiBJQ0EgKEluZGVwZW5kZW50IENvbXBvbmVudCBBbmFseXNpcykgZmluZHMgc3RhdGlzdGljYWxseSBpbmRlcGVuZGVudCBjb21wb25lbnRzLCBhIHN0cmljdGx5IHN0cm9uZ2VyIHJlcXVpcmVtZW50LiBQQ0EgdXNlcyBzZWNvbmQtb3JkZXIgc3RhdGlzdGljcyAoY292YXJpYW5jZSk7IElDQSBleHBsb2l0cyBoaWdoZXItb3JkZXIgc3RhdGlzdGljcyB0byBmaW5kIHNvdXJjZXMgdGhhdCBhcmUgYXMgbm9uLUdhdXNzaWFuIGFzIHBvc3NpYmxlLiBJdCBpcyB0aGUgYWxnb3JpdGhtIGJlaGluZCB0aGUgY29ja3RhaWwgcGFydHkgcHJvYmxlbSBhbmQgRUVHL2ZNUkkgc291cmNlIHNlcGFyYXRpb24uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW5kZXBlbmRlbmNlIHZzIFVuY29ycmVsYXRlZG5lc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVuY29ycmVsYXRlZCBtZWFucyBFW3jhtaJ44rG8XSA9IDAuIEluZGVwZW5kZW50IG1lYW5zIHAoeOG1oiwgeOKxvCkgPSBwKHjhtaIpcCh44rG8KSDigJQgdGhlIGpvaW50IGRlbnNpdHkgZmFjdG9yaXNlcy4gSW5kZXBlbmRlbmNlIGltcGxpZXMgdW5jb3JyZWxhdGVkbmVzcyBidXQgbm90IHZpY2UgdmVyc2EuIFRoZSBDZW50cmFsIExpbWl0IFRoZW9yZW0gdGVsbHMgdXMgdGhhdCBzdW1zIG9mIGluZGVwZW5kZW50IHJhbmRvbSB2YXJpYWJsZXMgY29udmVyZ2UgdG8gR2F1c3NpYW4uIElDQSByZXZlcnNlcyB0aGlzOiBpdCBmaW5kcyB1bm1peGluZyBkaXJlY3Rpb25zIHdoZXJlIHByb2plY3Rpb25zIGFyZSBtYXhpbWFsbHkgbm9uLUdhdXNzaWFuLCByZWNvdmVyaW5nIHRoZSBvcmlnaW5hbCBpbmRlcGVuZGVudCBzb3VyY2VzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5vbi1HYXVzc2lhbml0eSBhbmQgTmVnZW50cm9weSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSUNBIG1lYXN1cmVzIG5vbi1HYXVzc2lhbml0eSB2aWEgbmVnZW50cm9weSBKKHkpID0gSCh5X0dhdXNzaWFuKSAtIEgoeSksIHRoZSBlbnRyb3B5IGRpZmZlcmVuY2UgZnJvbSBhIEdhdXNzaWFuIHdpdGggdGhlIHNhbWUgdmFyaWFuY2UgKGFsd2F5cyDiiaUgMCkuIFByYWN0aWNhbCBhcHByb3hpbWF0aW9uczoga3VydG9zaXMga3VydCh5KSA9IEVbeeKBtF0gLSAzIChmYXN0IGJ1dCBzZW5zaXRpdmUgdG8gb3V0bGllcnMpIGFuZCBsb2ctY29zaDogSih5KSDiiYggW0VbbG9nIGNvc2goeSldIC0gRVtsb2cgY29zaCh5X0dhdXNzaWFuKV1dwrIuIEZhc3RJQ0EgdXNlcyB0aGUgbG9nLWNvc2ggYXBwcm94aW1hdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBmYXN0X2ljYShYLCBuX2NvbXBvbmVudHMsIG1heF9pdGVyPTMwMCwgdG9sPTFlLTYpOlxuICAgIFwiXCJcIkZhc3RJQ0EgdmlhIGZpeGVkLXBvaW50IGl0ZXJhdGlvbiB3aXRoIGxvZy1jb3NoIG5lZ2VudHJvcHkuXCJcIlwiXG4gICAgbiwgZCA9IFguc2hhcGVcbiAgICAjIFN0ZXAgMTogY2VudGVyXG4gICAgWCA9IFggLSBYLm1lYW4oYXhpcz0wKVxuICAgICMgU3RlcCAyOiB3aGl0ZW4gdmlhIFNWRFxuICAgIFUsIHMsIFZ0ID0gbnAubGluYWxnLnN2ZChYLCBmdWxsX21hdHJpY2VzPUZhbHNlKVxuICAgIFhfd2hpdGUgPSBVICogbnAuc3FydChuKSAgIyAobiwgZCkg4oCUIGlkZW50aXR5IGNvdmFyaWFuY2VcblxuICAgIFcgPSBucC56ZXJvcygobl9jb21wb25lbnRzLCBkKSlcbiAgICBmb3IgcCBpbiByYW5nZShuX2NvbXBvbmVudHMpOlxuICAgICAgICB3ID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKHApLnN0YW5kYXJkX25vcm1hbChkKVxuICAgICAgICB3IC89IG5wLmxpbmFsZy5ub3JtKHcpXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG1heF9pdGVyKTpcbiAgICAgICAgICAgIHUgPSBYX3doaXRlIEAgdyAgICAgICAgICAgICAgICAjIChuLClcbiAgICAgICAgICAgIGcgPSBucC50YW5oKHUpICAgICAgICAgICAgICAgICAjIGxvZy1jb3NoIGRlcml2YXRpdmVcbiAgICAgICAgICAgIGdfcHJpbWUgPSAxLjAgLSBnKioyXG4gICAgICAgICAgICB3X25ldyA9IFhfd2hpdGUuVCBAIGcgLyBuIC0gZ19wcmltZS5tZWFuKCkgKiB3XG4gICAgICAgICAgICAjIEdyYW0tU2NobWlkdCBkZWZsYXRpb25cbiAgICAgICAgICAgIHdfbmV3IC09IFdbOnBdLlQgQCAoV1s6cF0gQCB3X25ldylcbiAgICAgICAgICAgIHdfbmV3IC89IG5wLmxpbmFsZy5ub3JtKHdfbmV3KVxuICAgICAgICAgICAgaWYgbnAuYWJzKG5wLmRvdCh3X25ldywgdykpIFx1MDAzZSAxLjAgLSB0b2w6XG4gICAgICAgICAgICAgICAgYnJlYWtcbiAgICAgICAgICAgIHcgPSB3X25ld1xuICAgICAgICBXW3BdID0gd19uZXdcbiAgICByZXR1cm4gWF93aGl0ZSBAIFcuVCwgVyAgIyAobiwgbl9jb21wb25lbnRzKSwgdW5taXhpbmdcblxuIyBRdWljayB0ZXN0IG9uIGEgMi1zb3VyY2UgbWl4dHVyZVxucm5nID0gbnAucmFuZG9tLmRlZmF1bHRfcm5nKDQyKVxudCA9IG5wLmxpbnNwYWNlKDAsIDgsIDEwMDApXG5TID0gbnAuY19bbnAuc2luKDIqbnAucGkqdCksIG5wLnNpZ24obnAuc2luKDMqbnAucGkqdCkpXVxuQSA9IG5wLmFycmF5KFtbMC44LCAwLjRdLCBbMC4zLCAwLjldXSlcblhfbWl4ID0gUyBAIEEuVFxuU19yZWMsIFcgPSBmYXN0X2ljYShYX21peCwgbl9jb21wb25lbnRzPTIpXG5wcmludChmXHUwMDI3UmVjb3ZlcmVkIHNoYXBlOiB7U19yZWMuc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBGYXN0SUNBIEFsZ29yaXRobSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmFzdElDQSBpdGVyYXRlcyBhIGZpeGVkLXBvaW50IHVwZGF0ZSB0aGF0IGNvbnZlcmdlcyBjdWJpY2FsbHkgKGZhc3RlciB0aGFuIGdyYWRpZW50IGRlc2NlbnQpOiB3IOKGkCBFW3ggZyh34bWAeCldIC0gRVtnXHUwMDI3KHfhtYB4KV0gdywgdGhlbiBub3JtYWxpc2UuIE11bHRpcGxlIGNvbXBvbmVudHMgYXJlIGV4dHJhY3RlZCBzZXF1ZW50aWFsbHkgdXNpbmcgZGVmbGF0aW9uIChHcmFtLVNjaG1pZHQgb3J0aG9nb25hbGlzYXRpb24pIG9yIHNpbXVsdGFuZW91c2x5IHVzaW5nIHRoZSBzeW1tZXRyaWMgZGVjb3JyZWxhdGlvbiBXIOKGkCBXKFfhtYBXKeKBu8K5L8KyLiBTeW1tZXRyaWMgZGVjb3JyZWxhdGlvbiBpcyBtb3JlIHJvYnVzdCB0byBzbG93IGNvbnZlcmdlbmNlIGluIG9uZSBjb21wb25lbnQgYWZmZWN0aW5nIG90aGVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2NrdGFpbCBQYXJ0eSBQcm9ibGVtIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmRlY29tcG9zaXRpb24gaW1wb3J0IEZhc3RJQ0EsIFBDQVxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5uID0gMjAwMFxudCA9IG5wLmxpbnNwYWNlKDAsIDgsIG4pXG5cbiMgVGhyZWUgaW5kZXBlbmRlbnQgc291cmNlc1xuczEgPSBucC5zaW4oMiAqIG5wLnBpICogdCkgICAgICAgICAgICMgc2luZSB3YXZlXG5zMiA9IG5wLnNpZ24obnAuc2luKDMgKiBucC5waSAqIHQpKSAjIHNxdWFyZSB3YXZlXG5zMyA9IHJuZy5sYXBsYWNlKHNpemU9bikgICAgICAgICAgICAgIyBub24tR2F1c3NpYW4gbm9pc2VcblMgPSBucC5jb2x1bW5fc3RhY2soW3MxLCBzMiwgczNdKVxuUyAvPSBTLnN0ZChheGlzPTApXG5cbiMgUmFuZG9tIG1peGluZyBtYXRyaXggKHNpbXVsYXRlcyByb29tIGFjb3VzdGljcylcbkEgPSBucC5hcnJheShbWzEuMCwgMC41LCAwLjJdLFxuICAgICAgICAgICAgICBbMC4zLCAxLjAsIDAuNF0sXG4gICAgICAgICAgICAgIFswLjYsIDAuMiwgMS4wXV0pXG5YID0gUyBAIEEuVCAgIyBtaXhlZCBvYnNlcnZhdGlvbnMgYXQgMyBtaWNyb3Bob25lc1xuXG5maWNhID0gRmFzdElDQShuX2NvbXBvbmVudHM9MywgcmFuZG9tX3N0YXRlPTQyLCBtYXhfaXRlcj01MDApXG5TX2ljYSA9IGZpY2EuZml0X3RyYW5zZm9ybShYKVxuU19wY2EgPSBQQ0Eobl9jb21wb25lbnRzPTMpLmZpdF90cmFuc2Zvcm0oWClcblxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDMsIDMsIGZpZ3NpemU9KDE0LCA4KSlcbmxhYmVscyA9IFtcdTAwMjdUcnVlIFNvdXJjZXNcdTAwMjcsIFx1MDAyN1BDQVx1MDAyNywgXHUwMDI3RmFzdElDQVx1MDAyN11cbmZvciBjb2wsIChTcCwgbGFiKSBpbiBlbnVtZXJhdGUoemlwKFtTLCBTX3BjYSwgU19pY2FdLCBsYWJlbHMpKTpcbiAgICBmb3Igcm93IGluIHJhbmdlKDMpOlxuICAgICAgICBheGVzW3JvdywgY29sXS5wbG90KHRbOjIwMF0sIFNwWzoyMDAsIHJvd10sIGx3PTAuOClcbiAgICAgICAgYXhlc1tyb3csIGNvbF0uc2V0X3RpdGxlKGZcdTAwMjd7bGFifSDigJQgU291cmNlIHtyb3crMX1cdTAwMjcpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkZ1bmRhbWVudGFsIElDQSBBbWJpZ3VpdGllcyIsImNvbnRlbnQiOiJJQ0EgY2Fubm90IHJlY292ZXIgKDEpIHRoZSBvcmRlciBvZiBpbmRlcGVuZGVudCBjb21wb25lbnRzIOKAlCB0aGV5IGNhbiBiZSBwZXJtdXRlZCBhcmJpdHJhcmlseTsgKDIpIHRoZSBzY2FsZSBvZiBlYWNoIGNvbXBvbmVudCDigJQgb25seSB0aGUgcmF0aW8gaXMgZGV0ZXJtaW5lZDsgKDMpIHRoZSBzaWduIG9mIGVhY2ggY29tcG9uZW50LiBUaGVzZSBhbWJpZ3VpdGllcyBhcmUgZnVuZGFtZW50YWwgYW5kIHVuYXZvaWRhYmxlLiBJQ0EgYWxzbyBmYWlscyB3aGVuIGZld2VyIHRoYW4gMiBzb3VyY2VzIGFyZSBub24tR2F1c3NpYW4gKGUuZy4gb25seSBHYXVzc2lhbiBzb3VyY2VzIOKAlCB0aGVuIGFueSByb3RhdGlvbiBpcyBlcXVpdmFsZW50KS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmVwcm9jZXNzaW5nOiBDZW50ZXIgYW5kIFdoaXRlbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBGYXN0SUNBXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfZGlnaXRzXG5cblgsIHkgPSBsb2FkX2RpZ2l0cyhyZXR1cm5fWF95PVRydWUpXG4jIFVzZSBhIHN1YnNldCBvZiBwaXhlbCBkaW1lbnNpb25zIGFzIFx1MDAyN29ic2VydmVkIHNpZ25hbHNcdTAwMjdcblhfb2JzID0gWFs6MjAwLCA6MTBdLmFzdHlwZShmbG9hdCkgICMgMjAwIHNhbXBsZXMsIDEwIGNoYW5uZWxzXG5cbiMgc2tsZWFybiBGYXN0SUNBIGhhbmRsZXMgY2VudGVyaW5nIGFuZCB3aGl0ZW5pbmcgaW50ZXJuYWxseVxubl9jb21wID0gNVxuaWNhID0gRmFzdElDQShuX2NvbXBvbmVudHM9bl9jb21wLCByYW5kb21fc3RhdGU9NDIsIG1heF9pdGVyPTEwMDAsIHRvbD0wLjAwMSlcblNfaWNhID0gaWNhLmZpdF90cmFuc2Zvcm0oWF9vYnMpICAjICgyMDAsIDUpXG5cbnByaW50KGZcdTAwMjdNaXhpbmcgbWF0cml4IHNoYXBlOiB7aWNhLm1peGluZ18uc2hhcGV9XHUwMDI3KSAgICMgKDEwLCA1KVxucHJpbnQoZlx1MDAyN1JlY292ZXJlZCBzb3VyY2VzIHNoYXBlOiB7U19pY2Euc2hhcGV9XHUwMDI3KVxuXG4jIENoZWNrIHN0YXRpc3RpY2FsIGluZGVwZW5kZW5jZSAoc2hvdWxkIGJlIG5lYXItZGlhZ29uYWwpXG5jb3YgPSBucC5jb3YoU19pY2EuVClcbnByaW50KFx1MDAyN1xcbkNvdmFyaWFuY2Ugb2YgcmVjb3ZlcmVkIHNvdXJjZXMgKHNob3VsZCBiZSBuZWFyIGRpYWdvbmFsKTpcdTAwMjcpXG5wcmludChjb3Yucm91bmQoMykpXG5cbiMgUmVjb25zdHJ1Y3Qgb3JpZ2luYWwgc2lnbmFsc1xuWF9yZWNvbiA9IFNfaWNhIEAgaWNhLm1peGluZ18uVCArIGljYS5tZWFuX1xucmVjb25fZXJyID0gbnAubWVhbigoWF9vYnMgLSBYX3JlY29uKSAqKiAyKVxucHJpbnQoZlx1MDAyN1JlY29uc3RydWN0aW9uIE1TRToge3JlY29uX2VycjouNmZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IklDQSBmb3IgRUVHIEFydGlmYWN0IFJlbW92YWwifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgRmFzdElDQVxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5uX2NoLCBuX3QgPSAxNiwgMjAwMFxudCA9IG5wLmxpbnNwYWNlKDAsIDIsIG5fdClcblxuIyBTaW11bGF0ZSBFRUc6IGJyYWluIG9zY2lsbGF0aW9ucyArIGJsaW5rICsgY2FyZGlhY1xuYnJhaW4gPSBucC5hcnJheShbbnAuc2luKDIqbnAucGkqKDgraSkqdCkgKiAwLjUgZm9yIGkgaW4gcmFuZ2UoMTQpXSkgICMgYWxwaGFcbmJsaW5rID0gbnAuemVyb3MoKDEsIG5fdCkpXG5ibGlua1swLCA4MDA6ODQwXSA9IDguMCAgICMgZXllIGJsaW5rXG5lY2cgPSBucC5hcnJheShbMC4zICogbnAuc2luKDIqbnAucGkqMS4yKnQpXSlcblxuU190cnVlID0gbnAudnN0YWNrKFticmFpbiwgYmxpbmssIGVjZ10pLlQgICMgKG5fdCwgbl9jaClcbkEgPSBybmcubm9ybWFsKDAsIDAuMywgKG5fY2gsIG5fY2gpKSArIG5wLmV5ZShuX2NoKSAqIDJcblhfZWVnID0gU190cnVlIEAgQS5UXG5cbiMgSUNBIGRlY29tcG9zaXRpb25cbmljYSA9IEZhc3RJQ0Eobl9jb21wb25lbnRzPW5fY2gsIHJhbmRvbV9zdGF0ZT00MiwgbWF4X2l0ZXI9MTAwMClcblNfaWNhID0gaWNhLmZpdF90cmFuc2Zvcm0oWF9lZWcpICAjIChuX3QsIG5fY2gpXG5cbiMgSWRlbnRpZnkgYmxpbms6IGNvbXBvbmVudCB3aXRoIGhpZ2hlc3Qga3VydG9zaXMgKG1vc3Qgbm9uLUdhdXNzaWFuIHNwaWtlKVxua3VydG9zZXMgPSBbKG5wLm1lYW4oU19pY2FbOiwga10qKjQpIC8gbnAubWVhbihTX2ljYVs6LCBrXSoqMikqKjIgLSAzKVxuICAgICAgICAgICAgIGZvciBrIGluIHJhbmdlKG5fY2gpXVxuYmxpbmtfaWMgPSBpbnQobnAuYXJnbWF4KGt1cnRvc2VzKSlcbnByaW50KGZcdTAwMjdCbGluayBJQzoge2JsaW5rX2ljfSwga3VydG9zaXM6IHtrdXJ0b3Nlc1tibGlua19pY106LjJmfVx1MDAyNylcblxuIyBSZWNvbnN0cnVjdCB3aXRob3V0IGJsaW5rXG5TX2NsZWFuID0gU19pY2EuY29weSgpXG5TX2NsZWFuWzosIGJsaW5rX2ljXSA9IDBcblhfY2xlYW4gPSBTX2NsZWFuIEAgaWNhLm1peGluZ18uVCArIFhfZWVnLm1lYW4oYXhpcz0wKVxucHJpbnQoZlx1MDAyN1ZhcmlhbmNlIGJlZm9yZToge1hfZWVnLnZhcigpOi40Zn0sIGFmdGVyOiB7WF9jbGVhbi52YXIoKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIlBDQSIsIklDQSIsIk5NRiJdLCJyb3dzIjpbWyJBc3N1bXB0aW9uIiwiVW5jb3JyZWxhdGVkIiwiU3RhdGlzdGljYWxseSBpbmRlcGVuZGVudCIsIk5vbi1uZWdhdGl2ZSwgcGFydHMtYmFzZWQiXSxbIlNlY29uZC1vcmRlciBzdGF0cyIsIlllcyIsIk5vICh1c2VzIGhpZ2hlci1vcmRlcikiLCJObyJdLFsiSW50ZXJwcmV0YWJsZSBjb21wb25lbnRzIiwiTW9kZXJhdGUiLCJZZXMgKHNvdXJjZXMpIiwiWWVzIChwYXJ0cykiXSxbIk5vbi1uZWdhdGl2ZSBjb25zdHJhaW50IiwiTm8iLCJObyIsIlllcyJdLFsiTGluZWFyIG1peGluZyBhc3N1bWVkIiwiWWVzIiwiWWVzIiwiWWVzIl0sWyJQcmltYXJ5IHVzZSBjYXNlIiwiRGltZW5zaW9uYWxpdHkgcmVkdWN0aW9uIiwiU291cmNlIHNlcGFyYXRpb24sIEJTUyIsIlNwYXJzZSBwYXJ0cywgdG9waWMgbW9kZWxzIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkJsaW5kIHNvdXJjZSBzZXBhcmF0aW9uIChhdWRpbywgdmlkZW8pIiwiRUVHL01FRyBhcnRpZmFjdCByZW1vdmFsIChleWUgYmxpbmtzLCBtdXNjbGUgYWN0aXZpdHksIGNhcmRpYWMpIiwiZk1SSSBzcGF0aWFsIElDQSBmb3IgcmVzdGluZy1zdGF0ZSBuZXR3b3JrIGRpc2NvdmVyeSIsIkZpbmFuY2lhbCB0aW1lIHNlcmllczogc2VwYXJhdGluZyBtYXJrZXQtd2lkZSBmcm9tIGlkaW9zeW5jcmF0aWMgZmFjdG9ycyIsIkltYWdlIHByb2Nlc3Npbmc6IHNlcGFyYXRpbmcgaWxsdW1pbmF0aW9uIGZyb20gcmVmbGVjdGFuY2UiXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hvb3NpbmcgdGhlIE51bWJlciBvZiBDb21wb25lbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVbmxpa2UgUENBLCBJQ0EgaGFzIG5vIG5hdHVyYWwgY3JpdGVyaW9uIGxpa2UgZXhwbGFpbmVkIHZhcmlhbmNlIHRvIHNlbGVjdCB0aGUgbnVtYmVyIG9mIGNvbXBvbmVudHMuIENvbW1vbiBhcHByb2FjaGVzOiAoMSkgZml4IG5fY29tcG9uZW50cyBlcXVhbCB0byB0aGUgbnVtYmVyIG9mIHN1c3BlY3RlZCBzb3VyY2VzIGlmIGtub3duIGEgcHJpb3JpOyAoMikgYXBwbHkgUENBIGZpcnN0IChyZXRhaW5pbmcgOTXigJM5OSUgdmFyaWFuY2UpIGFuZCBzZXQgbl9jb21wb25lbnRzID0gUENBIG91dHB1dCBkaW1lbnNpb247ICgzKSB1c2UgdGhlIG1pbmltdW0gZGVzY3JpcHRpb24gbGVuZ3RoIChNREwpIGNyaXRlcmlvbjsgKDQpIGZvciBFRUcvZk1SSSwgZG9tYWluIGtub3dsZWRnZSBjb25zdHJhaW5zIHRoZSBudW1iZXIgb2YgbmV1cm9waHlzaW9sb2dpY2FsbHkgcGxhdXNpYmxlIGNvbXBvbmVudHMuIE92ZXItZXh0cmFjdGluZyBpcyBwcmVmZXJhYmxlIHRvIHVuZGVyLWV4dHJhY3Rpbmcg4oCUIGV4dHJhIGNvbXBvbmVudHMgY2FuIGJlIGRpc2NhcmRlZCBhZnRlciBpbnNwZWN0aW9uLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJQcmFjdGljYWwgSUNBIFdvcmtmbG93IiwiY29udGVudCI6IlN0ZXAgMTogc3RhbmRhcmRpc2UgYW5kIGNlbnRlciBkYXRhLiBTdGVwIDI6IGFwcGx5IFBDQSB3aGl0ZW5pbmcgKHJlZHVjZXMgdG8gbl9jb21wb25lbnRzIHVuY29ycmVsYXRlZCwgdW5pdC12YXJpYW5jZSBzaWduYWxzKS4gU3RlcCAzOiBydW4gRmFzdElDQSBvbiB3aGl0ZW5lZCBkYXRhIChza2xlYXJuIGhhbmRsZXMgc3RlcHMgMS0zIGF1dG9tYXRpY2FsbHkpLiBTdGVwIDQ6IGluc3BlY3QgY29tcG9uZW50IHRpbWUgY291cnNlcyBhbmQgc3BlY3RyYSB0byBpZGVudGlmeSBhbmQgcmVtb3ZlIGFydGlmYWN0IGNvbXBvbmVudHMuIFN0ZXAgNTogcmVjb25zdHJ1Y3QgY2xlYW4gc2lnbmFsIGJ5IHplcm9pbmcgYXJ0aWZhY3QgY29tcG9uZW50cyBhbmQgYmFjay1wcm9qZWN0aW5nIHRocm91Z2ggdGhlIG1peGluZyBtYXRyaXguIn0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiV2hlbiBJQ0EgRmFpbHMiLCJjb250ZW50IjoiSUNBIHJlcXVpcmVzIGF0IGxlYXN0IG4tMSBub24tR2F1c3NpYW4gc291cmNlcyAob25lIGNhbiBiZSBHYXVzc2lhbikuIEl0IGZhaWxzIHdoZW46IGFsbCBzb3VyY2VzIGFyZSBHYXVzc2lhbiAoUENBIGlzIG9wdGltYWwpOyB0aGUgbWl4aW5nIGlzIG5vbmxpbmVhcjsgZmV3ZXIgb2JzZXJ2YXRpb25zIHRoYW4gc291cmNlcyAodW5kZXJkZXRlcm1pbmVkIEJTUyk7IG9yIGRhdGEgaXMgbm9uLXN0YXRpb25hcnkgd2l0aCBjaGFuZ2luZyBtaXhpbmcuIEluIHRoZXNlIGNhc2VzIGNvbnNpZGVyIFNPQkkgKHNlY29uZC1vcmRlciBCU1MgdXNpbmcgdGltZSBzdHJ1Y3R1cmUpIG9yIG5vbmxpbmVhciBJQ0EgYXBwcm9hY2hlcy4ifV0="
---
# ICA — Non-Gaussianity and the FastICA Algorithm

PCA finds uncorrelated components — components with zero covariance. ICA (Independent Component Analysis) finds statistically independent components, a strictly stronger requirement. PCA uses second-order statistics (covariance); ICA exploits higher-order statistics to find sources that are as non-Gaussian as possible. It is the algorithm behind the cocktail party problem and EEG/fMRI source separation.

## Independence vs Uncorrelatedness

Uncorrelated means E[xᵢxⱼ] = 0. Independent means p(xᵢ, xⱼ) = p(xᵢ)p(xⱼ) — the joint density factorises. Independence implies uncorrelatedness but not vice versa. The Central Limit Theorem tells us that sums of independent random variables converge to Gaussian. ICA reverses this: it finds unmixing directions where projections are maximally non-Gaussian, recovering the original independent sources.

## Non-Gaussianity and Negentropy

ICA measures non-Gaussianity via negentropy J(y) = H(y_Gaussian) - H(y), the entropy difference from a Gaussian with the same variance (always ≥ 0). Practical approximations: kurtosis kurt(y) = E[y⁴] - 3 (fast but sensitive to outliers) and log-cosh: J(y) ≈ [E[log cosh(y)] - E[log cosh(y_Gaussian)]]². FastICA uses the log-cosh approximation.

```python
import numpy as np

def fast_ica(X, n_components, max_iter=300, tol=1e-6):
    """FastICA via fixed-point iteration with log-cosh negentropy."""
    n, d = X.shape
    # Step 1: center
    X = X - X.mean(axis=0)
    # Step 2: whiten via SVD
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    X_white = U * np.sqrt(n)  # (n, d) — identity covariance

    W = np.zeros((n_components, d))
    for p in range(n_components):
        w = np.random.default_rng(p).standard_normal(d)
        w /= np.linalg.norm(w)
        for _ in range(max_iter):
            u = X_white @ w                # (n,)
            g = np.tanh(u)                 # log-cosh derivative
            g_prime = 1.0 - g**2
            w_new = X_white.T @ g / n - g_prime.mean() * w
            # Gram-Schmidt deflation
            w_new -= W[:p].T @ (W[:p] @ w_new)
            w_new /= np.linalg.norm(w_new)
            if np.abs(np.dot(w_new, w)) > 1.0 - tol:
                break
            w = w_new
        W[p] = w_new
    return X_white @ W.T, W  # (n, n_components), unmixing

# Quick test on a 2-source mixture
rng = np.random.default_rng(42)
t = np.linspace(0, 8, 1000)
S = np.c_[np.sin(2*np.pi*t), np.sign(np.sin(3*np.pi*t))]
A = np.array([[0.8, 0.4], [0.3, 0.9]])
X_mix = S @ A.T
S_rec, W = fast_ica(X_mix, n_components=2)
print(f'Recovered shape: {S_rec.shape}')
```

## The FastICA Algorithm

FastICA iterates a fixed-point update that converges cubically (faster than gradient descent): w ← E[x g(wᵀx)] - E[g'(wᵀx)] w, then normalise. Multiple components are extracted sequentially using deflation (Gram-Schmidt orthogonalisation) or simultaneously using the symmetric decorrelation W ← W(WᵀW)⁻¹/². Symmetric decorrelation is more robust to slow convergence in one component affecting others.

## Cocktail Party Problem

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA, PCA

rng = np.random.default_rng(42)
n = 2000
t = np.linspace(0, 8, n)

# Three independent sources
s1 = np.sin(2 * np.pi * t)           # sine wave
s2 = np.sign(np.sin(3 * np.pi * t)) # square wave
s3 = rng.laplace(size=n)             # non-Gaussian noise
S = np.column_stack([s1, s2, s3])
S /= S.std(axis=0)

# Random mixing matrix (simulates room acoustics)
A = np.array([[1.0, 0.5, 0.2],
              [0.3, 1.0, 0.4],
              [0.6, 0.2, 1.0]])
X = S @ A.T  # mixed observations at 3 microphones

fica = FastICA(n_components=3, random_state=42, max_iter=500)
S_ica = fica.fit_transform(X)
S_pca = PCA(n_components=3).fit_transform(X)

fig, axes = plt.subplots(3, 3, figsize=(14, 8))
labels = ['True Sources', 'PCA', 'FastICA']
for col, (Sp, lab) in enumerate(zip([S, S_pca, S_ica], labels)):
    for row in range(3):
        axes[row, col].plot(t[:200], Sp[:200, row], lw=0.8)
        axes[row, col].set_title(f'{lab} — Source {row+1}')
plt.tight_layout()
plt.show()
```

> **Fundamental ICA Ambiguities**: ICA cannot recover (1) the order of independent components — they can be permuted arbitrarily; (2) the scale of each component — only the ratio is determined; (3) the sign of each component. These ambiguities are fundamental and unavoidable. ICA also fails when fewer than 2 sources are non-Gaussian (e.g. only Gaussian sources — then any rotation is equivalent).

## Preprocessing: Center and Whiten

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
# Use a subset of pixel dimensions as 'observed signals'
X_obs = X[:200, :10].astype(float)  # 200 samples, 10 channels

# sklearn FastICA handles centering and whitening internally
n_comp = 5
ica = FastICA(n_components=n_comp, random_state=42, max_iter=1000, tol=0.001)
S_ica = ica.fit_transform(X_obs)  # (200, 5)

print(f'Mixing matrix shape: {ica.mixing_.shape}')   # (10, 5)
print(f'Recovered sources shape: {S_ica.shape}')

# Check statistical independence (should be near-diagonal)
cov = np.cov(S_ica.T)
print('\nCovariance of recovered sources (should be near diagonal):')
print(cov.round(3))

# Reconstruct original signals
X_recon = S_ica @ ica.mixing_.T + ica.mean_
recon_err = np.mean((X_obs - X_recon) ** 2)
print(f'Reconstruction MSE: {recon_err:.6f}')
```

## ICA for EEG Artifact Removal

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA

rng = np.random.default_rng(42)
n_ch, n_t = 16, 2000
t = np.linspace(0, 2, n_t)

# Simulate EEG: brain oscillations + blink + cardiac
brain = np.array([np.sin(2*np.pi*(8+i)*t) * 0.5 for i in range(14)])  # alpha
blink = np.zeros((1, n_t))
blink[0, 800:840] = 8.0   # eye blink
ecg = np.array([0.3 * np.sin(2*np.pi*1.2*t)])

S_true = np.vstack([brain, blink, ecg]).T  # (n_t, n_ch)
A = rng.normal(0, 0.3, (n_ch, n_ch)) + np.eye(n_ch) * 2
X_eeg = S_true @ A.T

# ICA decomposition
ica = FastICA(n_components=n_ch, random_state=42, max_iter=1000)
S_ica = ica.fit_transform(X_eeg)  # (n_t, n_ch)

# Identify blink: component with highest kurtosis (most non-Gaussian spike)
kurtoses = [(np.mean(S_ica[:, k]**4) / np.mean(S_ica[:, k]**2)**2 - 3)
             for k in range(n_ch)]
blink_ic = int(np.argmax(kurtoses))
print(f'Blink IC: {blink_ic}, kurtosis: {kurtoses[blink_ic]:.2f}')

# Reconstruct without blink
S_clean = S_ica.copy()
S_clean[:, blink_ic] = 0
X_clean = S_clean @ ica.mixing_.T + X_eeg.mean(axis=0)
print(f'Variance before: {X_eeg.var():.4f}, after: {X_clean.var():.4f}')
```

| Property | PCA | ICA | NMF |
| --- | --- | --- | --- |
| Assumption | Uncorrelated | Statistically independent | Non-negative, parts-based |
| Second-order stats | Yes | No (uses higher-order) | No |
| Interpretable components | Moderate | Yes (sources) | Yes (parts) |
| Non-negative constraint | No | No | Yes |
| Linear mixing assumed | Yes | Yes | Yes |
| Primary use case | Dimensionality reduction | Source separation, BSS | Sparse parts, topic models |

- Blind source separation (audio, video)
- EEG/MEG artifact removal (eye blinks, muscle activity, cardiac)
- fMRI spatial ICA for resting-state network discovery
- Financial time series: separating market-wide from idiosyncratic factors
- Image processing: separating illumination from reflectance

## Choosing the Number of Components

Unlike PCA, ICA has no natural criterion like explained variance to select the number of components. Common approaches: (1) fix n_components equal to the number of suspected sources if known a priori; (2) apply PCA first (retaining 95–99% variance) and set n_components = PCA output dimension; (3) use the minimum description length (MDL) criterion; (4) for EEG/fMRI, domain knowledge constrains the number of neurophysiologically plausible components. Over-extracting is preferable to under-extracting — extra components can be discarded after inspection.

> **Practical ICA Workflow**: Step 1: standardise and center data. Step 2: apply PCA whitening (reduces to n_components uncorrelated, unit-variance signals). Step 3: run FastICA on whitened data (sklearn handles steps 1-3 automatically). Step 4: inspect component time courses and spectra to identify and remove artifact components. Step 5: reconstruct clean signal by zeroing artifact components and back-projecting through the mixing matrix.

---

> **When ICA Fails**: ICA requires at least n-1 non-Gaussian sources (one can be Gaussian). It fails when: all sources are Gaussian (PCA is optimal); the mixing is nonlinear; fewer observations than sources (underdetermined BSS); or data is non-stationary with changing mixing. In these cases consider SOBI (second-order BSS using time structure) or nonlinear ICA approaches.

