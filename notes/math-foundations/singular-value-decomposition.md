---
title: "Singular Value Decomposition (SVD)"
slug: "singular-value-decomposition"
description: "The full SVD formula, geometric interpretation, truncated SVD for low-rank approximation, pseudoinverse, and ML applications."
tags: ["linear-algebra", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2luZ3VsYXIgVmFsdWUgRGVjb21wb3NpdGlvbiAoU1ZEKSBpcyBhcmd1YWJseSB0aGUgbW9zdCBpbXBvcnRhbnQgbWF0cml4IGZhY3Rvcml6YXRpb24gaW4gYXBwbGllZCBtYXRoZW1hdGljcy4gVW5saWtlIGVpZ2VuZGVjb21wb3NpdGlvbiAod2hpY2ggcmVxdWlyZXMgc3F1YXJlIG1hdHJpY2VzKSwgU1ZEIHdvcmtzIG9uIGFueSBtYXRyaXggb2YgYW55IHNoYXBlIGFuZCByZXZlYWxzIHRoZSBpbnRyaW5zaWMgZ2VvbWV0cmljIHN0cnVjdHVyZSBvZiB0aGUgbGluZWFyIHRyYW5zZm9ybWF0aW9uIGl0IHJlcHJlc2VudHMuIFNWRCB1bmRlcnBpbnMgUENBLCByZWNvbW1lbmRlciBzeXN0ZW1zLCBuYXR1cmFsIGxhbmd1YWdlIHByb2Nlc3NpbmcsIGNvbXByZXNzZWQgc2Vuc2luZywgYW5kIG51bWVyaWNhbCBsaW5lYXIgYWxnZWJyYSBzb2x2ZXJzLiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBTVkQgRm9ybXVsYTogQSA9IFXOo1bhtYAifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkV2ZXJ5IHJlYWwgbWF0cml4ICoqQSoqIChtw5duKSBjYW4gYmUgZmFjdG9yZWQgYXM6XG5cbiAgKipBID0gVc6jVuG1gCoqXG5cbndoZXJlOlxuLSAqKlUqKiBpcyBtw5dtIG9ydGhvZ29uYWwgKCoqVeG1gFUgPSBJKiopOiBsZWZ0IHNpbmd1bGFyIHZlY3RvcnMgKGNvbHVtbnMgc3BhbiBjb2x1bW4gc3BhY2Ugb2YgQSlcbi0gKirOoyoqIGlzIG3Dl24gZGlhZ29uYWwgd2l0aCBub24tbmVnYXRpdmUgZW50cmllcyDPg+KCgSDiiaUgz4PigoIg4omlIC4uLiDiiaUgz4PigpjhtaLigpnigo3igpgs4oKZ4oKOIOKJpSAwOiB0aGUgKipzaW5ndWxhciB2YWx1ZXMqKlxuLSAqKlYqKiBpcyBuw5duIG9ydGhvZ29uYWwgKCoqVuG1gFYgPSBJKiopOiByaWdodCBzaW5ndWxhciB2ZWN0b3JzIChjb2x1bW5zIHNwYW4gcm93IHNwYWNlIG9mIEEpXG5cblRoZSBudW1iZXIgb2Ygbm9uemVybyBzaW5ndWxhciB2YWx1ZXMgZXF1YWxzIHRoZSAqKnJhbmsqKiBvZiAqKkEqKi4gVGhlIHNpbmd1bGFyIHZhbHVlcyBhcmUgYWx3YXlzIHJlYWwgYW5kIG5vbi1uZWdhdGl2ZSwgZXZlbiB3aGVuIEEgaXMgbm90IHNxdWFyZSBvciBub3Qgc3ltbWV0cmljLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuQSA9IG5wLmFycmF5KFtbMSwgMiwgMF0sXG4gICAgICAgICAgICAgIFswLCAzLCAxXSxcbiAgICAgICAgICAgICAgWzEsIDEsIDJdXSwgZHR5cGU9ZmxvYXQpXG5cblUsIHNpZ21hLCBWdCA9IG5wLmxpbmFsZy5zdmQoQSkgICAgIyBmdWxsIFNWRFxucHJpbnQoJ1Ugc2hhcGU6JywgVS5zaGFwZSkgICAgICAgICAgIyAoMywzKVxucHJpbnQoJ3NpZ21hOicsIHNpZ21hKSAgICAgICAgICAgICAgIyBbNC4xMSwgMi41NCwgMC43Nl0gKHNvcnRlZCBkZXNjKVxucHJpbnQoJ1Z0IHNoYXBlOicsIFZ0LnNoYXBlKSAgICAgICAgIyAoMywzKVxuXG4jIFJlY29uc3RydWN0IEFcblNpZ21hID0gbnAuemVyb3NfbGlrZShBKVxubnAuZmlsbF9kaWFnb25hbChTaWdtYSwgc2lnbWEpXG5BX3JlY29uc3RydWN0ZWQgPSBVIEAgU2lnbWEgQCBWdFxucHJpbnQoJ1JlY29uc3RydWN0aW9uIGVycm9yOicsIG5wLmxpbmFsZy5ub3JtKEEgLSBBX3JlY29uc3RydWN0ZWQpKSAgIyB+MWUtMTVcblxuIyBSYW5rXG5yYW5rID0gbnAuc3VtKHNpZ21hID4gMWUtMTApXG5wcmludCgnUmFuazonLCByYW5rKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikdlb21ldHJpYyBJbnRlcnByZXRhdGlvbjogUm90YXRpb24tU2NhbGUtUm90YXRpb24ifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBTVkQgKipBID0gVc6jVuG1gCoqIGRlY29tcG9zZXMgdGhlIGxpbmVhciB0cmFuc2Zvcm1hdGlvbiBpbnRvIHRocmVlIHN0YWdlcywgYXBwbGllZCByaWdodC10by1sZWZ0OlxuXG4xLiAqKlbhtYAqKjogUm90YXRlL3JlZmxlY3QgdGhlIGlucHV0IHNwYWNlIChvcnRob2dvbmFsIHRyYW5zZm9ybWF0aW9uIOKAlCBwcmVzZXJ2ZXMgbGVuZ3RocyBhbmQgYW5nbGVzKVxuMi4gKirOoyoqOiBTY2FsZSBhbG9uZyB0aGUgY29vcmRpbmF0ZSBheGVzIGJ5IM+D4oKBLCDPg+KCgiwgLi4uLCDPg+KCliAocHVyZWx5IHN0cmV0Y2hpbmcvY29tcHJlc3NpbmcpXG4zLiAqKlUqKjogUm90YXRlL3JlZmxlY3QgaW50byB0aGUgb3V0cHV0IHNwYWNlIChhbm90aGVyIG9ydGhvZ29uYWwgdHJhbnNmb3JtYXRpb24pXG5cblRoaXMgbWVhbnMgKmV2ZXJ5IGxpbmVhciB0cmFuc2Zvcm1hdGlvbiBpcyBqdXN0IHJvdGF0aW9ucyBhbmQgc2NhbGluZ3MgaW4gZGlzZ3Vpc2UqLiBUaGUgc2luZ3VsYXIgdmFsdWVzIG1lYXN1cmUgdGhlIHN0cmV0Y2hpbmc6IHRoZSB1bml0IHNwaGVyZSBpbiBpbnB1dCBzcGFjZSBnZXRzIG1hcHBlZCB0byBhbiBlbGxpcHNvaWQgaW4gb3V0cHV0IHNwYWNlLCB3aGVyZSB0aGUgc2VtaS1heGlzIGxlbmd0aHMgYXJlIGV4YWN0bHkgdGhlIHNpbmd1bGFyIHZhbHVlcywgYW5kIHRoZSBheGlzIGRpcmVjdGlvbnMgYXJlIHRoZSBsZWZ0L3JpZ2h0IHNpbmd1bGFyIHZlY3RvcnMuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVsYXRpb25zaGlwIHRvIEVpZ2VuZGVjb21wb3NpdGlvbiJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU1ZEIGFuZCBlaWdlbmRlY29tcG9zaXRpb24gYXJlIGludGltYXRlbHkgcmVsYXRlZC4gVGhlIHJpZ2h0IHNpbmd1bGFyIHZlY3RvcnMgKGNvbHVtbnMgb2YgKipWKiopIGFyZSB0aGUgZWlnZW52ZWN0b3JzIG9mICoqQeG1gEEqKiwgYW5kIHRoZSBsZWZ0IHNpbmd1bGFyIHZlY3RvcnMgKGNvbHVtbnMgb2YgKipVKiopIGFyZSB0aGUgZWlnZW52ZWN0b3JzIG9mICoqQUHhtYAqKjpcblxuICAqKkHhtYBBID0gVs6j4bWAzqNW4bWAKiog4oaSIGVpZ2VuZGVjb21wb3NpdGlvbiBvZiBB4bWAQVxuICAqKkFB4bWAID0gVc6jzqPhtYBV4bWAKiog4oaSIGVpZ2VuZGVjb21wb3NpdGlvbiBvZiBBQeG1gFxuXG5UaGUgc2luZ3VsYXIgdmFsdWVzIHNhdGlzZnkgz4PhtaIgPSDiiJrOu+G1oiB3aGVyZSDOu+G1oiBhcmUgdGhlIGVpZ2VudmFsdWVzIG9mICoqQeG1gEEqKiAoYWxsIG5vbi1uZWdhdGl2ZSBmb3IgUFNEIG1hdHJpY2VzKS4gRm9yIGEgc3F1YXJlIHN5bW1ldHJpYyBtYXRyaXggKipBKiosIHRoZSBzaW5ndWxhciB2YWx1ZXMgYXJlIHRoZSBhYnNvbHV0ZSB2YWx1ZXMgb2YgdGhlIGVpZ2VudmFsdWVzLiBUaGlzIGlzIHdoeSBTVkQgaXMgcHJlZmVycmVkIGZvciBnZW5lcmFsIG1hdHJpY2VzOiBpdCBhdm9pZHMgc3F1YXJpbmcgdGhlIGNvbmRpdGlvbiBudW1iZXIgKGFuZCB0aHVzIGxvc2luZyBudW1lcmljYWwgcHJlY2lzaW9uKSB0aGF0IGhhcHBlbnMgd2hlbiBjb21wdXRpbmcgQeG1gEEgZXhwbGljaXRseS4ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcnVuY2F0ZWQgU1ZEIGZvciBMb3ctUmFuayBBcHByb3hpbWF0aW9uIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgKipFY2thcnQtWW91bmctTWlyc2t5IHRoZW9yZW0qKiBzdGF0ZXMgdGhhdCB0aGUgYmVzdCByYW5rLWsgYXBwcm94aW1hdGlvbiBvZiAqKkEqKiAoaW4gYm90aCBGcm9iZW5pdXMgYW5kIHNwZWN0cmFsIG5vcm1zKSBpcyBnaXZlbiBieSBrZWVwaW5nIG9ubHkgdGhlIHRvcC1rIHNpbmd1bGFyIHZhbHVlczpcblxuICAqKkHigpYgPSBV4oKWzqPigpZW4oKW4bWAKipcblxud2hlcmUgKipV4oKWKiogdXNlcyBvbmx5IHRoZSBmaXJzdCBrIGNvbHVtbnMgb2YgKipVKiosICoqzqPigpYqKiBpcyBrw5drIGRpYWdvbmFsLCBhbmQgKipW4oKW4bWAKiogdXNlcyB0aGUgZmlyc3QgayByb3dzIG9mICoqVuG1gCoqLiBUaGUgYXBwcm94aW1hdGlvbiBlcnJvciBpczogfHxBIC0gQeKClnx8X0bCsiA9IM+D4oKW4oKK4oKBwrIgKyAuLi4gKyDPg+G1o8KyLiBUaGlzIGlzIHRoZSBtYXRoZW1hdGljYWwgZm91bmRhdGlvbiBvZjpcbi0gUENBIChwcm9qZWN0IGRhdGEgb250byB0b3AtayBwcmluY2lwYWwgYXhlcylcbi0gUmVjb21tZW5kZXIgc3lzdGVtcyAoYXBwcm94aW1hdGUgdGhlIHVzZXItaXRlbSBtYXRyaXgpXG4tIEltYWdlIGNvbXByZXNzaW9uIChzdG9yZSBrIHNpbmd1bGFyIHRyaXBsZXRzIGluc3RlYWQgb2YgYWxsIHBpeGVscylcbi0gTGF0ZW50IFNlbWFudGljIEFuYWx5c2lzIChsb3ctcmFuayBhcHByb3hpbWF0aW9uIG9mIHRlcm0tZG9jdW1lbnQgbWF0cml4KSJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBJbWFnZSBjb21wcmVzc2lvbiB2aWEgdHJ1bmNhdGVkIFNWRFxubnAucmFuZG9tLnNlZWQoMClcbmltZyA9IG5wLnJhbmRvbS5yYW5kbigyNTYsIDI1NikgICMgc2ltdWxhdGUgZ3JheXNjYWxlIGltYWdlXG5cblUsIHNpZ21hLCBWdCA9IG5wLmxpbmFsZy5zdmQoaW1nLCBmdWxsX21hdHJpY2VzPUZhbHNlKSAgIyBlY29ub215IFNWRFxuXG5mb3IgayBpbiBbNSwgMjAsIDUwXTpcbiAgICBpbWdfayA9IFVbOiwgOmtdIEAgbnAuZGlhZyhzaWdtYVs6a10pIEAgVnRbOmssIDpdXG4gICAgZXJyb3IgPSBucC5saW5hbGcubm9ybShpbWcgLSBpbWdfaywgJ2ZybycpIC8gbnAubGluYWxnLm5vcm0oaW1nLCAnZnJvJylcbiAgICBjb21wcmVzc2lvbiA9IGsgKiAoMjU2ICsgMSArIDI1NikgLyAoMjU2ICogMjU2KVxuICAgIHByaW50KGYnaz17azozZH06IGVycm9yPXtlcnJvcjouM2Z9LCBzaXplPXtjb21wcmVzc2lvbjouMSV9IG9mIG9yaWdpbmFsJylcblxuIyBFeHBsYWluZWQgdmFyaWFuY2VcbnZhcl9leHBsYWluZWQgPSBucC5jdW1zdW0oc2lnbWEqKjIpIC8gbnAuc3VtKHNpZ21hKioyKVxucHJpbnQoZidUb3AtNSBleHBsYWlucyB7dmFyX2V4cGxhaW5lZFs0XTouMSV9IG9mIEZyb2Jlbml1cyBub3JtIHNxdWFyZWQnKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBQc2V1ZG9pbnZlcnNlIChNb29yZS1QZW5yb3NlIEludmVyc2UpIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3Igbm9uLXNxdWFyZSBvciByYW5rLWRlZmljaWVudCBtYXRyaWNlcyB0aGF0IGxhY2sgYSB0cnVlIGludmVyc2UsIHRoZSAqKk1vb3JlLVBlbnJvc2UgcHNldWRvaW52ZXJzZSoqICoqQeKBuioqIGlzIHRoZSBnZW5lcmFsaXphdGlvbiB0aGF0IHNhdGlzZmllcyB0aGUgbGVhc3Qtc3F1YXJlcyBzb2x1dGlvbi4gR2l2ZW4gKipBID0gVc6jVuG1gCoqLCB0aGUgcHNldWRvaW52ZXJzZSBpczpcblxuICAqKkHigbogPSBWzqPigbpV4bWAKipcblxud2hlcmUgKirOo+KBuioqIHJlcGxhY2VzIGVhY2ggbm9uemVybyBzaW5ndWxhciB2YWx1ZSDPg+G1oiB3aXRoIDEvz4PhtaIgKGFuZCBsZWF2ZXMgemVyb3MgYXMgemVyb3MpLiBUaGUgbGVhc3Qtc3F1YXJlcyBzb2x1dGlvbiB0byAqKkF4IOKJiCBiKiogaXMgKip4KiA9IEHigbpiKiosIHdoaWNoIG1pbmltaXplcyB8fEF4IC0gYnx84oKCLiBXaGVuIHRoZSBzeXN0ZW0gaXMgdW5kZXJkZXRlcm1pbmVkIChpbmZpbml0ZWx5IG1hbnkgc29sdXRpb25zKSwgKipB4oG6YioqIGdpdmVzIHRoZSBtaW5pbXVtLW5vcm0gc29sdXRpb24uIFRoaXMgaXMgd2h5IFNWRCBpcyB0aGUgd29ya2hvcnNlIGJlaGluZCBgbnVtcHkubGluYWxnLmxzdHNxYC4ifSwKICB7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgU29sdmUgb3ZlcmRldGVybWluZWQgc3lzdGVtIEF4ID0gYiB2aWEgcHNldWRvaW52ZXJzZVxubnAucmFuZG9tLnNlZWQoMSlcbkEgPSBucC5yYW5kb20ucmFuZG4oMTAsIDMpICAgIyAxMCBlcXVhdGlvbnMsIDMgdW5rbm93bnNcbmIgPSBucC5yYW5kb20ucmFuZG4oMTApXG5cbiMgVmlhIFNWRCAocHNldWRvaW52ZXJzZSlcblUsIHMsIFZ0ID0gbnAubGluYWxnLnN2ZChBLCBmdWxsX21hdHJpY2VzPUZhbHNlKVxuc19pbnYgPSAxLjAgLyBzICAgICAgICAgICAgICAjIHJlY2lwcm9jYWwgc2luZ3VsYXIgdmFsdWVzXG54X3N2ZCA9IFZ0LlQgQCAobnAuZGlhZyhzX2ludikgQCAoVS5UIEAgYikpXG5cbiMgVmlhIG51bXB5IGxzdHNxIChhbHNvIFNWRC1iYXNlZCBpbnRlcm5hbGx5KVxueF9sc3RzcSwgXywgXywgXyA9IG5wLmxpbmFsZy5sc3RzcShBLCBiLCByY29uZD1Ob25lKVxuXG5wcmludCgnfHxBeCAtIGJ8fCB2aWEgU1ZEOicsIG5wLmxpbmFsZy5ub3JtKEEgQCB4X3N2ZCAtIGIpKVxucHJpbnQoJ3x8QXggLSBifHwgdmlhIGxzdHNxOicsIG5wLmxpbmFsZy5ub3JtKEEgQCB4X2xzdHNxIC0gYikpXG5wcmludCgnU29sdXRpb25zIG1hdGNoOicsIG5wLmFsbGNsb3NlKHhfc3ZkLCB4X2xzdHNxKSkifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTVkQgaW4gUmVjb21tZW5kZXIgU3lzdGVtcyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSB1c2VyLWl0ZW0gcmF0aW5nIG1hdHJpeCAqKlIqKiAobSB1c2VycyDDlyBuIGl0ZW1zKSBpcyB0eXBpY2FsbHkgdmVyeSBzcGFyc2UgKG1vc3QgdXNlcnMgaGF2ZSByYXRlZCBmZXcgaXRlbXMpLiAqKk1hdHJpeCBmYWN0b3JpemF0aW9uKiogYXBwcm94aW1hdGVzICoqUiDiiYggVVbhtYAqKiB3aGVyZSAqKlUqKiAobcOXaykgcmVwcmVzZW50cyB1c2VycyBhbmQgKipWKiogKG7Dl2spIHJlcHJlc2VudHMgaXRlbXMgaW4gYSBrLWRpbWVuc2lvbmFsIGxhdGVudCBzcGFjZS4gRWFjaCBsYXRlbnQgZGltZW5zaW9uIGNhcHR1cmVzIGEgY29uY2VwdCAoZ2VucmUsIHN0eWxlLCB0aGVtZSkuXG5cblRoZSBjbGFzc2ljICoqU2ltb24gRnVuayBTVkQqKiAodXNlZCBpbiB0aGUgTmV0ZmxpeCBQcml6ZSkgc29sdmVzIHRoaXMgdmlhIHN0b2NoYXN0aWMgZ3JhZGllbnQgZGVzY2VudCBvbiBvYnNlcnZlZCBlbnRyaWVzIG9ubHksIGxlYXJuaW5nIHVzZXIvaXRlbSBlbWJlZGRpbmdzIHRoYXQgcHJlZGljdCByYXRpbmdzIGZvciB1bm9ic2VydmVkIHBhaXJzLiBUaGlzIGlzICoqY29sbGFib3JhdGl2ZSBmaWx0ZXJpbmcqKjogc2ltaWxhciB1c2VycyAoY2xvc2UgaW4gVSkgdGVuZCB0byBsaWtlIHNpbWlsYXIgaXRlbXMgKGNsb3NlIGluIFYpLCBlbmFibGluZyBwZXJzb25hbGl6ZWQgcmVjb21tZW5kYXRpb25zIHdpdGhvdXQgaXRlbSBjb250ZW50LiJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxhdGVudCBTZW1hbnRpYyBBbmFseXNpcyBhbmQgV29yZCBFbWJlZGRpbmdzIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiIqKkxhdGVudCBTZW1hbnRpYyBBbmFseXNpcyAoTFNBKSoqIGFwcGxpZXMgdHJ1bmNhdGVkIFNWRCB0byBhIHRlcm0tZG9jdW1lbnQgbWF0cml4ICoqTSoqIHdoZXJlIE1baSxqXSA9IFRGLUlERiB3ZWlnaHQgb2YgdGVybSBpIGluIGRvY3VtZW50IGouIFRoZSBsb3ctcmFuayBhcHByb3hpbWF0aW9uICoqTeKCliA9IFXigpbOo+KCllbigpbhtYAqKiBtYXBzIGJvdGggdGVybXMgYW5kIGRvY3VtZW50cyBpbnRvIGEgc2hhcmVkIGstZGltZW5zaW9uYWwgc2VtYW50aWMgc3BhY2UuXG5cbldvcmRzIHVzZWQgaW4gc2ltaWxhciBjb250ZXh0cyBlbmQgdXAgY2xvc2UgaW4gdGhpcyBzcGFjZSwgY2FwdHVyaW5nIHNlbWFudGljIHNpbWlsYXJpdHkgZXZlbiB3aGVuIGV4YWN0IHdvcmQgbWF0Y2hlcyBmYWlsIChzeW5vbnlteSBhbmQgcG9seXNlbXkgaGFuZGxpbmcpLiBMU0EgcHJlZGF0ZXMgbmV1cmFsIHdvcmQgZW1iZWRkaW5ncyAod29yZDJ2ZWMsIEdsb1ZlKSBidXQgbW90aXZhdGVkIHRoZSBzYW1lIGNvcmUgaW5zaWdodDogc2VtYW50aWMgbWVhbmluZyBjYW4gYmUgY2FwdHVyZWQgYnkgbG93LXJhbmsgc3RydWN0dXJlIGluIGNvLW9jY3VycmVuY2Ugc3RhdGlzdGljcy4ifSwKICB7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkVjb25vbXkgdnMgRnVsbCBTVkQg4oCUIE1lbW9yeSBJbXBsaWNhdGlvbnMiLCJjb250ZW50IjoibnVtcHkubGluYWxnLnN2ZChBKSBieSBkZWZhdWx0IGNvbXB1dGVzIHRoZSBmdWxsIFNWRCwgcmV0dXJuaW5nIFUgYXMgKG0sbSkgZXZlbiBmb3IgYSAobSxuKSBtYXRyaXggd2l0aCBtID4+IG4uIEZvciBBIHdpdGggc2hhcGUgKDEwMDAwLCAxMDApLCB0aGUgZnVsbCBVIGlzIDEwMDAww5cxMDAwMCA9IDgwME1CLiBVc2UgZnVsbF9tYXRyaWNlcz1GYWxzZSAoZWNvbm9teS90aGluIFNWRCkgdG8gZ2V0IFUgYXMgKG0sIG1pbihtLG4pKSA9ICgxMDAwMCwgMTAwKSDigJQgYSAxMDDDlyBtZW1vcnkgcmVkdWN0aW9uLiBTaW1pbGFybHksIHNjaXB5LnNwYXJzZS5saW5hbGcuc3ZkcyBjb21wdXRlcyBvbmx5IHRoZSB0b3AtayBzaW5ndWxhciB0cmlwbGV0cyBhbmQgaXMgZXNzZW50aWFsIGZvciB2ZXJ5IGxhcmdlIHNwYXJzZSBtYXRyaWNlcy4ifSwKICB7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXBwbGljYXRpb24iLCJNYXRyaXgiLCJMb3ctUmFuayBNZWFuaW5nIl0sInJvd3MiOltbIkltYWdlIGNvbXByZXNzaW9uIiwiUGl4ZWwgbWF0cml4IiwiVG9wLWsgdmlzdWFsIHBhdHRlcm5zIChlZGdlcywgdGV4dHVyZXMpIl0sWyJQQ0EiLCJEYXRhIG1hdHJpeCBYIiwiVG9wIHZhcmlhbmNlIGRpcmVjdGlvbnMiXSxbIlJlY29tbWVuZGVyIHN5c3RlbXMiLCJVc2VyIMOXIEl0ZW0gcmF0aW5ncyIsIkxhdGVudCB0YXN0ZS9zdHlsZSBmYWN0b3JzIl0sWyJOTFAgKExTQSkiLCJUZXJtIMOXIERvY3VtZW50IFRGLUlERiIsIkxhdGVudCBzZW1hbnRpYyB0b3BpY3MiXSxbIk5ldXJhbCBuZXQgY29tcHJlc3Npb24iLCJXZWlnaHQgbWF0cml4IFciLCJSZW1vdmUgbG93LXZhcmlhbmNlIHRyYW5zZm9ybWF0aW9uIGRpcmVjdGlvbnMiXSxbIkRhdGEgd2hpdGVuaW5nIiwiQ292YXJpYW5jZSBtYXRyaXggQyIsIk5vcm1hbGl6ZSBhbmQgZGVjb3JyZWxhdGUgZmVhdHVyZXMiXV19LAogIHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJOdW1lcmljYWwgUmFuayB2aWEgU2luZ3VsYXIgVmFsdWVzIiwiY29udGVudCI6IlRvIGRldGVybWluZSB0aGUgbnVtZXJpY2FsIHJhbmsgb2YgYSBtYXRyaXggKGhvdyBtYW55IHNpbmd1bGFyIHZhbHVlcyBhcmUgJ2VmZmVjdGl2ZWx5IG5vbnplcm8nKSwgdXNlOiByYW5rID0gbnAuc3VtKHNpZ21hID4gdGhyZXNob2xkICogc2lnbWFbMF0gKiBtYXgobSxuKSAqIGVwcykgd2hlcmUgZXBzID0gbnAuZmluZm8oZmxvYXQpLmVwcyAofjIuMmUtMTYpLiBUaGlzIGlzIGV4YWN0bHkgd2hhdCBudW1weS5saW5hbGcubWF0cml4X3JhbmsgdXNlcyBpbnRlcm5hbGx5LiBOZXZlciBjb21wdXRlIHJhbmsgdmlhIGRldGVybWluYW50IChudW1lcmljYWxseSB1bnN0YWJsZSkgb3Igcm93IHJlZHVjdGlvbiB3aXRob3V0IHBpdm90aW5nLiJ9Cl0K"
---

# Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) is arguably the most important matrix factorization in applied mathematics. Unlike eigendecomposition (which requires square matrices), SVD works on any matrix of any shape and reveals the intrinsic geometric structure of the linear transformation it represents. SVD underpins PCA, recommender systems, natural language processing, compressed sensing, and numerical linear algebra solvers.

## The SVD Formula: A = UΣVᵀ

Every real matrix **A** (m×n) can be factored as:

  **A = UΣVᵀ**

where:
- **U** is m×m orthogonal (**UᵀU = I**): left singular vectors (columns span column space of A)
- **Σ** is m×n diagonal with non-negative entries σ₁ ≥ σ₂ ≥ ... ≥ σₘᵢₙ₍ₘ,ₙ₎ ≥ 0: the **singular values**
- **V** is n×n orthogonal (**VᵀV = I**): right singular vectors (columns span row space of A)

The number of nonzero singular values equals the **rank** of **A**. The singular values are always real and non-negative, even when A is not square or not symmetric.

```python
import numpy as np

A = np.array([[1, 2, 0],
              [0, 3, 1],
              [1, 1, 2]], dtype=float)

U, sigma, Vt = np.linalg.svd(A)    # full SVD
print('U shape:', U.shape)          # (3,3)
print('sigma:', sigma)              # [4.11, 2.54, 0.76] (sorted desc)
print('Vt shape:', Vt.shape)        # (3,3)

# Reconstruct A
Sigma = np.zeros_like(A)
np.fill_diagonal(Sigma, sigma)
A_reconstructed = U @ Sigma @ Vt
print('Reconstruction error:', np.linalg.norm(A - A_reconstructed))  # ~1e-15

# Rank
rank = np.sum(sigma > 1e-10)
print('Rank:', rank)
```

## Geometric Interpretation: Rotation-Scale-Rotation

The SVD **A = UΣVᵀ** decomposes the linear transformation into three stages, applied right-to-left:

1. **Vᵀ**: Rotate/reflect the input space (orthogonal transformation — preserves lengths and angles)
2. **Σ**: Scale along the coordinate axes by σ₁, σ₂, ..., σₖ (purely stretching/compressing)
3. **U**: Rotate/reflect into the output space (another orthogonal transformation)

This means *every linear transformation is just rotations and scalings in disguise*. The singular values measure the stretching: the unit sphere in input space gets mapped to an ellipsoid in output space, where the semi-axis lengths are exactly the singular values, and the axis directions are the left/right singular vectors.

## Relationship to Eigendecomposition

SVD and eigendecomposition are intimately related. The right singular vectors (columns of **V**) are the eigenvectors of **AᵀA**, and the left singular vectors (columns of **U**) are the eigenvectors of **AAᵀ**:

  **AᵀA = VΣᵀΣVᵀ** → eigendecomposition of AᵀA
  **AAᵀ = UΣΣᵀUᵀ** → eigendecomposition of AAᵀ

The singular values satisfy σᵢ = √λᵢ where λᵢ are the eigenvalues of **AᵀA** (all non-negative for PSD matrices). For a square symmetric matrix **A**, the singular values are the absolute values of the eigenvalues. This is why SVD is preferred for general matrices: it avoids squaring the condition number (and thus losing numerical precision) that happens when computing AᵀA explicitly.

## Truncated SVD for Low-Rank Approximation

The **Eckart-Young-Mirsky theorem** states that the best rank-k approximation of **A** (in both Frobenius and spectral norms) is given by keeping only the top-k singular values:

  **Aₖ = UₖΣₖVₖᵀ**

where **Uₖ** uses only the first k columns of **U**, **Σₖ** is k×k diagonal, and **Vₖᵀ** uses the first k rows of **Vᵀ**. The approximation error is: ||A - Aₖ||_F² = σₖ₊₁² + ... + σᵣ². This is the mathematical foundation of:
- PCA (project data onto top-k principal axes)
- Recommender systems (approximate the user-item matrix)
- Image compression (store k singular triplets instead of all pixels)
- Latent Semantic Analysis (low-rank approximation of term-document matrix)

```python
import numpy as np

# Image compression via truncated SVD
np.random.seed(0)
img = np.random.randn(256, 256)  # simulate grayscale image

U, sigma, Vt = np.linalg.svd(img, full_matrices=False)  # economy SVD

for k in [5, 20, 50]:
    img_k = U[:, :k] @ np.diag(sigma[:k]) @ Vt[:k, :]
    error = np.linalg.norm(img - img_k, 'fro') / np.linalg.norm(img, 'fro')
    compression = k * (256 + 1 + 256) / (256 * 256)
    print(f'k={k:3d}: error={error:.3f}, size={compression:.1%} of original')

# Explained variance
var_explained = np.cumsum(sigma**2) / np.sum(sigma**2)
print(f'Top-5 explains {var_explained[4]:.1%} of Frobenius norm squared')
```

## The Pseudoinverse (Moore-Penrose Inverse)

For non-square or rank-deficient matrices that lack a true inverse, the **Moore-Penrose pseudoinverse** **A⁺** is the generalization that satisfies the least-squares solution. Given **A = UΣVᵀ**, the pseudoinverse is:

  **A⁺ = VΣ⁺Uᵀ**

where **Σ⁺** replaces each nonzero singular value σᵢ with 1/σᵢ (and leaves zeros as zeros). The least-squares solution to **Ax ≈ b** is **x* = A⁺b**, which minimizes ||Ax - b||₂. When the system is underdetermined (infinitely many solutions), **A⁺b** gives the minimum-norm solution. This is why SVD is the workhorse behind `numpy.linalg.lstsq`.

```python
import numpy as np

# Solve overdetermined system Ax = b via pseudoinverse
np.random.seed(1)
A = np.random.randn(10, 3)   # 10 equations, 3 unknowns
b = np.random.randn(10)

# Via SVD (pseudoinverse)
U, s, Vt = np.linalg.svd(A, full_matrices=False)
s_inv = 1.0 / s              # reciprocal singular values
x_svd = Vt.T @ (np.diag(s_inv) @ (U.T @ b))

# Via numpy lstsq (also SVD-based internally)
x_lstsq, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

print('||Ax - b|| via SVD:', np.linalg.norm(A @ x_svd - b))
print('||Ax - b|| via lstsq:', np.linalg.norm(A @ x_lstsq - b))
print('Solutions match:', np.allclose(x_svd, x_lstsq))
```

## SVD in Recommender Systems

A user-item rating matrix **R** (m users × n items) is typically very sparse (most users have rated few items). **Matrix factorization** approximates **R ≈ UVᵀ** where **U** (m×k) represents users and **V** (n×k) represents items in a k-dimensional latent space. Each latent dimension captures a concept (genre, style, theme).

The classic **Simon Funk SVD** (used in the Netflix Prize) solves this via stochastic gradient descent on observed entries only, learning user/item embeddings that predict ratings for unobserved pairs. This is **collaborative filtering**: similar users (close in U) tend to like similar items (close in V), enabling personalized recommendations without item content.

## Latent Semantic Analysis and Word Embeddings

**Latent Semantic Analysis (LSA)** applies truncated SVD to a term-document matrix **M** where M[i,j] = TF-IDF weight of term i in document j. The low-rank approximation **Mₖ = UₖΣₖVₖᵀ** maps both terms and documents into a shared k-dimensional semantic space.

Words used in similar contexts end up close in this space, capturing semantic similarity even when exact word matches fail (synonymy and polysemy handling). LSA predates neural word embeddings (word2vec, GloVe) but motivated the same core insight: semantic meaning can be captured by low-rank structure in co-occurrence statistics.

> **[WARNING] Economy vs Full SVD — Memory Implications**
>
> numpy.linalg.svd(A) by default computes the full SVD, returning U as (m,m) even for a (m,n) matrix with m >> n. For A with shape (10000, 100), the full U is 10000×10000 = 800MB. Use full_matrices=False (economy/thin SVD) to get U as (m, min(m,n)) = (10000, 100) — a 100× memory reduction. Similarly, scipy.sparse.linalg.svds computes only the top-k singular triplets and is essential for very large sparse matrices.

| Application | Matrix | Low-Rank Meaning |
| --- | --- | --- |
| Image compression | Pixel matrix | Top-k visual patterns (edges, textures) |
| PCA | Data matrix X | Top variance directions |
| Recommender systems | User × Item ratings | Latent taste/style factors |
| NLP (LSA) | Term × Document TF-IDF | Latent semantic topics |
| Neural net compression | Weight matrix W | Remove low-variance transformation directions |
| Data whitening | Covariance matrix C | Normalize and decorrelate features |

> **[TIP] Numerical Rank via Singular Values**
>
> To determine the numerical rank of a matrix (how many singular values are 'effectively nonzero'), use: rank = np.sum(sigma > threshold * sigma[0] * max(m,n) * eps) where eps = np.finfo(float).eps (~2.2e-16). This is exactly what numpy.linalg.matrix_rank uses internally. Never compute rank via determinant (numerically unstable) or row reduction without pivoting.
