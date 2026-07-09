---
title: "Linear Regression — OLS, Normal Equations, and QR"
slug: "linear-regression"
description: "Derive OLS θ=(XᵀX)⁻¹Xᵀy from first principles, explore QR decomposition for numerical stability, compute hat-matrix leverage and Cook's distance, and trace the ridge regression coefficient path."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTGluZWFyIHJlZ3Jlc3Npb24gbW9kZWxzIHRoZSByZXNwb25zZSB5IOKIiCDihJ3igb8gYXMgeSA9IFjOuCArIM61LCB3aGVyZSBYIOKIiCDihJ3igb/Lo+G1liBpcyB0aGUgZGVzaWduIG1hdHJpeCwgzrgg4oiIIOKEneG1liBhcmUgdW5rbm93biBwYXJhbWV0ZXJzLCBhbmQgzrUgaXMgdGhlIGVycm9yIHZlY3Rvci4gVW5kZXIgc3RhbmRhcmQgR2F1c3MtTWFya292IGFzc3VtcHRpb25zLCBPcmRpbmFyeSBMZWFzdCBTcXVhcmVzIChPTFMpIHByb2R1Y2VzIHRoZSBCZXN0IExpbmVhciBVbmJpYXNlZCBFc3RpbWF0b3IuIFVuZGVyc3RhbmRpbmcgdGhlIGNsb3NlZC1mb3JtIHNvbHV0aW9uLCBpdHMgZ2VvbWV0cmljIGludGVycHJldGF0aW9uIHRocm91Z2ggdGhlIGhhdCBtYXRyaXgsIGFuZCBudW1lcmljYWxseSBzdGFibGUgaW1wbGVtZW50YXRpb24gdmlhIFFSIGRlY29tcG9zaXRpb24gaXMgZm91bmRhdGlvbmFsIHRvIGFsbCBzdXBlcnZpc2VkIGxlYXJuaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9MUyBPYmplY3RpdmUgYW5kIERlcml2YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9MUyBtaW5pbWlzZXMgdGhlIFJlc2lkdWFsIFN1bSBvZiBTcXVhcmVzOiBSU1MgPSDigJZ5IOKIkiBYzrjigJbCsiA9ICh5IOKIkiBYzrgp4bWAKHkg4oiSIFjOuCkuIEV4cGFuZGluZyBnaXZlcyB54bWAeSDiiJIgMs644bWAWOG1gHkgKyDOuOG1gFjhtYBYzrguIERpZmZlcmVudGlhdGluZyB3aXRoIHJlc3BlY3QgdG8gzrggYW5kIHNldHRpbmcgdGhlIGdyYWRpZW50IHRvIHplcm86IOKIglJTUy/iiILOuCA9IOKIkjJY4bWAeSArIDJY4bWAWM64ID0gMCwgd2hpY2ggZ2l2ZXMgdGhlIE5vcm1hbCBFcXVhdGlvbnMgWOG1gFjOuCA9IFjhtYB5LiBTaW5jZSBY4bWAWCBpcyBwb3NpdGl2ZSBzZW1pLWRlZmluaXRlLCB0aGlzIGlzIGEgY29udmV4IHF1YWRyYXRpYyB3aXRoIGEgdW5pcXVlIG1pbmltdW0gd2hlbiBY4bWAWCBpcyBpbnZlcnRpYmxlIChYIGhhcyBmdWxsIGNvbHVtbiByYW5rIHApLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5vcm1hbCBFcXVhdGlvbnMgYW5kIEludmVydGliaWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gWCBoYXMgZnVsbCBjb2x1bW4gcmFuaywgdGhlIHVuaXF1ZSBPTFMgc29sdXRpb24gaXMgzrjMgiA9IChY4bWAWCnigbvCuVjhtYB5LiBNdWx0aWNvbGxpbmVhcml0eSBjYXVzZXMgbmVhci1yYW5rIGRlZmljaWVuY3k6IFjhtYBYIGJlY29tZXMgbmVhcmx5IHNpbmd1bGFyIGFuZCB0aGUgVmFyaWFuY2UgSW5mbGF0aW9uIEZhY3RvciBWSUZfaiA9IDEvKDHiiJJSwrJfaikgZGl2ZXJnZXMuIFRoZSBjb25kaXRpb24gbnVtYmVyIHNhdGlzZmllcyDOuihY4bWAWCkgPSDOuihYKcKyLCBzbyBmb3JtaW5nIHRoZSBub3JtYWwgZXF1YXRpb25zIHNxdWFyZXMgdGhlIG51bWVyaWNhbCBkaWZmaWN1bHR5LiBSaWRnZSByZWdyZXNzaW9uIGd1YXJhbnRlZXMgaW52ZXJ0aWJpbGl0eSBieSBhZGRpbmcgzrtJOiDOuMyCX3JpZGdlID0gKFjhtYBYICsgzrtJKeKBu8K5WOG1gHksIHdoaWNoIGFsd2F5cyB5aWVsZHMgYSBwb3NpdGl2ZS1kZWZpbml0ZSBzeXN0ZW0gZm9yIM67IFx1MDAzZSAwLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExpbmVhclJlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9yZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcjJfc2NvcmVcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5LCB0cnVlX2NvZWYgPSBtYWtlX3JlZ3Jlc3Npb24oXG4gICAgbl9zYW1wbGVzPTIwMCwgbl9mZWF0dXJlcz01LCBub2lzZT0xMC4wLCBjb2VmPVRydWUsIHJhbmRvbV9zdGF0ZT00MlxuKVxuXG4jIE9MUyBjbG9zZWQgZm9ybTogdGhldGEgPSAoWF5UIFgpXnstMX0gWF5UIHlcblhfYiA9IG5wLmhzdGFjayhbbnAub25lcygobGVuKFgpLCAxKSksIFhdKSAgIyBwcmVwZW5kIGludGVyY2VwdCBjb2x1bW5cblh0WCA9IFhfYi5UIEAgWF9iXG5YdHkgPSBYX2IuVCBAIHlcbnRoZXRhX29scyA9IG5wLmxpbmFsZy5zb2x2ZShYdFgsIFh0eSkgICMgcHJlZmVyIHNvbHZlIG92ZXIgaW52XG5cbmxyID0gTGluZWFyUmVncmVzc2lvbigpLmZpdChYLCB5KVxuXG5wcmludChcdTAwMjdPTFMgc2NyYXRjaDogaW50ZXJjZXB0PXs6LjRmfVx1MDAyNy5mb3JtYXQodGhldGFfb2xzWzBdKSlcbnByaW50KFx1MDAyN3NrbGVhcm46ICAgICBpbnRlcmNlcHQ9ezouNGZ9XHUwMDI3LmZvcm1hdChsci5pbnRlcmNlcHRfKSlcbnByaW50KFx1MDAyN01heCBjb2VmIGRpZmZlcmVuY2U6IHs6LjJlfVx1MDAyNy5mb3JtYXQoXG4gICAgbnAuYWJzKHRoZXRhX29sc1sxOl0gLSBsci5jb2VmXykubWF4KCkpKVxucHJpbnQoXHUwMDI3Ul4yID0gezouNGZ9XHUwMDI3LmZvcm1hdChyMl9zY29yZSh5LCBYX2IgQCB0aGV0YV9vbHMpKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJRUiBEZWNvbXBvc2l0aW9uIGZvciBOdW1lcmljYWwgU3RhYmlsaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJRUiBkZWNvbXBvc2l0aW9uIHdyaXRlcyBYID0gUVIgd2hlcmUgUSDiiIgg4oSd4oG/y6PhtZYgaGFzIG9ydGhvbm9ybWFsIGNvbHVtbnMgKFHhtYBRID0gSSkgYW5kIFIg4oiIIOKEneG1lsuj4bWWIGlzIHVwcGVyIHRyaWFuZ3VsYXIuIFN1YnN0aXR1dGluZyBpbnRvIHRoZSBub3JtYWwgZXF1YXRpb25zOiBS4bWAUs64ID0gUuG1gFHhtYB5IOKGkiBSzrggPSBR4bWAeS4gU29sdmluZyB0aGlzIHRyaWFuZ3VsYXIgc3lzdGVtIHZpYSBiYWNrLXN1YnN0aXR1dGlvbiBoYXMgY29uZGl0aW9uIG51bWJlciDOuihSKSA9IM66KFgpLCBub3QgzrooWCnCsi4gVGhpcyBhdm9pZHMgc3F1YXJpbmcgdGhlIG51bWVyaWNhbCBkaWZmaWN1bHR5IGFuZCBpcyB0aGUgcHJlZmVycmVkIGFwcHJvYWNoIGZvciBpbGwtY29uZGl0aW9uZWQgZGVzaWducy4gTEFQQUNLXHUwMDI3cyBkZ2Vsc2QgYW5kIGRnZWxzeSByb3V0aW5lcyAodXNlZCBieSBudW1weSBhbmQgc2tsZWFybikgaW50ZXJuYWxseSB1c2UgUVIgd2l0aCBjb2x1bW4gcGl2b3RpbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5ucC5yYW5kb20uc2VlZCgwKVxubiwgcCA9IDE1MCwgMTJcblggPSBucC5yYW5kb20ucmFuZG4obiwgcClcbnkgPSBYIEAgbnAucmFuZG9tLnJhbmRuKHApICsgMC4xICogbnAucmFuZG9tLnJhbmRuKG4pXG5YX2IgPSBucC5oc3RhY2soW25wLm9uZXMoKG4sIDEpKSwgWF0pXG5cbiMgTm9ybWFsIGVxdWF0aW9uczogY29uZGl0aW9uIG51bWJlciBzcXVhcmVkXG5rYXBwYV94dHggPSBucC5saW5hbGcuY29uZChYX2IuVCBAIFhfYilcbnRoZXRhX25lID0gbnAubGluYWxnLnNvbHZlKFhfYi5UIEAgWF9iLCBYX2IuVCBAIHkpXG5cbiMgUVIgZGVjb21wb3NpdGlvbjogY29uZGl0aW9uIG51bWJlciBwcmVzZXJ2ZWRcblEsIFIgPSBucC5saW5hbGcucXIoWF9iLCBtb2RlPVx1MDAyN3JlZHVjZWRcdTAwMjcpXG50aGV0YV9xciA9IG5wLmxpbmFsZy5zb2x2ZShSLCBRLlQgQCB5KVxuXG5rYXBwYV94ID0gbnAubGluYWxnLmNvbmQoWF9iKVxucHJpbnQoZlx1MDAyN2NvbmQoWF9iKSAgICAgID0ge2thcHBhX3g6LjJmfVx1MDAyNylcbnByaW50KGZcdTAwMjdjb25kKFhfYlQgWF9iKSA9IHtrYXBwYV94dHg6LjJmfSAgKGNvbmReMiA9IHtrYXBwYV94KioyOi4yZn0pXHUwMDI3KVxucHJpbnQoZlx1MDAyN01heCB8dGhldGFfTkUgLSB0aGV0YV9RUnwgPSB7bnAuYWJzKHRoZXRhX25lIC0gdGhldGFfcXIpLm1heCgpOi4yZX1cdTAwMjcpXG5wcmludChcdTAwMjdRUiBhdm9pZHMgc3F1YXJpbmcgdGhlIGNvbmRpdGlvbiBudW1iZXIuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhhdCBNYXRyaXggYW5kIEluZmx1ZW5jZSBEaWFnbm9zdGljcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGhhdCBtYXRyaXggSCA9IFgoWOG1gFgp4oG7wrlY4bWAIHByb2plY3RzIHkgb250byBjb2woWCk6IMW3ID0gSHkuIEggaXMgc3ltbWV0cmljIGFuZCBpZGVtcG90ZW50IHdpdGggdHJhY2UoSCkgPSByYW5rKFgpID0gcC4gVGhlIGRpYWdvbmFsIGjhtaLhtaIg4oiIIFtwL24sIDFdIGlzIHRoZSBsZXZlcmFnZSBzY29yZSBvZiBvYnNlcnZhdGlvbiBpIOKAlCBob3cgbXVjaCBpdCBpbmZsdWVuY2VzIGl0cyBvd24gZml0dGVkIHZhbHVlLiBUaGUgc3RhbmRhcmQgdGhyZXNob2xkIGZvciBoaWdoIGxldmVyYWdlIGlzIGjhtaLhtaIgXHUwMDNlIDJwL24uIENvb2tcdTAwMjdzIGRpc3RhbmNlIEThtaIgPSBy4bWiwrIgaOG1ouG1oiAvIChwIMK3IE1TRSDCtyAoMeKIkmjhtaLhtaIpwrIpIG1lYXN1cmVzIGhvdyBtdWNoIHRoZSBmdWxsIGNvZWZmaWNpZW50IHZlY3RvciBzaGlmdHMgd2hlbiBvYnNlcnZhdGlvbiBpIGlzIHJlbW92ZWQsIGNvbWJpbmluZyBsZXZlcmFnZSBhbmQgcmVzaWR1YWwgbWFnbml0dWRlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExpbmVhclJlZ3Jlc3Npb25cblxubnAucmFuZG9tLnNlZWQoMSlcbm4gPSA2MFxuWCA9IG5wLnJhbmRvbS5yYW5kbihuLCAzKVxueSA9IDIgKiBYWzosIDBdIC0gWFs6LCAxXSArIG5wLnJhbmRvbS5yYW5kbihuKVxuXG4jIEluamVjdCBhIGhpZ2gtbGV2ZXJhZ2Ugb3V0bGllclxuWFstMV0gPSBbOS4wLCA5LjAsIDkuMF1cbnlbLTFdID0gLTMwLjBcblxuWF9iID0gbnAuaHN0YWNrKFtucC5vbmVzKChuLCAxKSksIFhdKVxucF9wYXJhbXMgPSBYX2Iuc2hhcGVbMV1cblxuSCA9IFhfYiBAIG5wLmxpbmFsZy5zb2x2ZShYX2IuVCBAIFhfYiwgWF9iLlQpXG5sZXZlcmFnZXMgPSBucC5kaWFnKEgpXG50aHJlc2hvbGQgPSAyICogcF9wYXJhbXMgLyBuXG5cbmxyID0gTGluZWFyUmVncmVzc2lvbigpLmZpdChYLCB5KVxucmVzaWQgPSB5IC0gbHIucHJlZGljdChYKVxubXNlID0gcmVzaWQgQCByZXNpZCAvIChuIC0gcF9wYXJhbXMpXG5jb29rc19kID0gKHJlc2lkKioyIC8gKHBfcGFyYW1zICogbXNlKSkgKiAobGV2ZXJhZ2VzIC8gKDEgLSBsZXZlcmFnZXMpKioyKVxuXG5wcmludChmXHUwMDI3TGV2ZXJhZ2UgdGhyZXNob2xkIDJwL24gPSB7dGhyZXNob2xkOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3T3V0bGllciBsZXZlcmFnZSA9IHtsZXZlcmFnZXNbLTFdOi40Zn0sIENvb2sgRCA9IHtjb29rc19kWy0xXTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0hpZ2gtbGV2ZXJhZ2UgaW5kaWNlczoge25wLndoZXJlKGxldmVyYWdlcyBcdTAwM2UgdGhyZXNob2xkKVswXS50b2xpc3QoKX1cdTAwMjcpXG5wcmludChmXHUwMDI3VHIoSCkgPSB7bGV2ZXJhZ2VzLnN1bSgpOi4xZn0sIHAgPSB7cF9wYXJhbXN9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiSGlnaCBMZXZlcmFnZSDiiaAgSGlnaCBJbmZsdWVuY2UiLCJjb250ZW50IjoiQSBoaWdoLWxldmVyYWdlIHBvaW50IChsYXJnZSBo4bWi4bWiKSBsaWVzIGZhciBmcm9tIHRoZSBjZW50cm9pZCBvZiBYIGFuZCBoYXMgdGhlIHBvdGVudGlhbCB0byBwdWxsIHRoZSByZWdyZXNzaW9uIGxpbmUuIEl0IGV4ZXJ0cyBoaWdoIGluZmx1ZW5jZSBvbmx5IHdoZW4gaXQgaXMgYWxzbyBhIHJlc3BvbnNlIG91dGxpZXIuIEFsd2F5cyBleGFtaW5lIGJvdGggbGV2ZXJhZ2UgKGjhtaLhtaIgXHUwMDNlIDJwL24pIGFuZCBDb29rXHUwMDI3cyBkaXN0YW5jZSAoROG1oiBcdTAwM2UgNC9uKSBiZWZvcmUgcmVtb3ZpbmcgYW55IG9ic2VydmF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJpZGdlIFJlZ3Jlc3Npb24gUGF0aCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmlkZ2UgcmVncmVzc2lvbiBhZGRzIGFuIEwyIHBlbmFsdHk6IG1pbmltaXNlIOKAlnkg4oiSIFjOuOKAlsKyICsgzrvigJbOuOKAlsKyLiBUaGUgY2xvc2VkLWZvcm0gc29sdXRpb24gzrjMgl9yaWRnZSA9IChY4bWAWCArIM67SSnigbvCuVjhtYB5IGFsd2F5cyBleGlzdHMgZm9yIM67IFx1MDAzZSAwIGJlY2F1c2UgWOG1gFggKyDOu0kgaXMgcG9zaXRpdmUgZGVmaW5pdGUgZXZlbiB3aGVuIFjhtYBYIGlzIHNpbmd1bGFyLiBBcyDOuyBpbmNyZWFzZXMgYWxsIGNvZWZmaWNpZW50cyBzaHJpbmsgcHJvcG9ydGlvbmFsbHkgdG93YXJkIHplcm8g4oCUIGJ1dCBuZXZlciBleGFjdGx5IHplcm8uIFRoZSBCYXllc2lhbiBpbnRlcnByZXRhdGlvbjogcmlkZ2UgaXMgdGhlIE1BUCBlc3RpbWF0ZSB1bmRlciBhIEdhdXNzaWFuIHByaW9yIM64IH4gTigwLCDPg8KySS/OuykuIFRoZSBvcHRpbWFsIM67IGlzIGZvdW5kIHZpYSBjcm9zcy12YWxpZGF0aW9uIG9yIGdlbmVyYWxpc2VkIGNyb3NzLXZhbGlkYXRpb24gKEdDVikuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUmlkZ2VcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX3JlZ3Jlc3Npb25cblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5ID0gbWFrZV9yZWdyZXNzaW9uKG5fc2FtcGxlcz0xMDAsIG5fZmVhdHVyZXM9MTAsIG5faW5mb3JtYXRpdmU9NSxcbiAgICAgICAgICAgICAgICAgICAgICAgIG5vaXNlPTE1LjAsIHJhbmRvbV9zdGF0ZT00MilcbnNjYWxlciA9IFN0YW5kYXJkU2NhbGVyKClcblhfcyA9IHNjYWxlci5maXRfdHJhbnNmb3JtKFgpXG5cbmxhbWJkYXMgPSBucC5sb2dzcGFjZSgtMywgNSwgMzAwKVxuY29lZnMgPSBucC52c3RhY2soW1JpZGdlKGFscGhhPWxhbSkuZml0KFhfcywgeSkuY29lZl8gZm9yIGxhbSBpbiBsYW1iZGFzXSlcblxuIyBWZXJpZnkgY2xvc2VkIGZvcm0gYXQgbGFtYmRhPTEwXG5sYW1fY2hlY2sgPSAxMC4wXG50aGV0YV9jZiA9IG5wLmxpbmFsZy5zb2x2ZShcbiAgICBYX3MuVCBAIFhfcyArIGxhbV9jaGVjayAqIG5wLmV5ZShYX3Muc2hhcGVbMV0pLCBYX3MuVCBAIHlcbilcbnNrX2NvZWYgPSBSaWRnZShhbHBoYT1sYW1fY2hlY2spLmZpdChYX3MsIHkpLmNvZWZfXG5wcmludChmXHUwMDI3Q2xvc2VkIGZvcm0gdnMgc2tsZWFybiBhdCBsYW1iZGE9e2xhbV9jaGVja306IG1heCBkaWZmID0ge25wLmFicyh0aGV0YV9jZiAtIHNrX2NvZWYpLm1heCgpOi4yZX1cdTAwMjcpXG5cbmZvciBpZHgsIGxhYmVsIGluIFsoMCwgXHUwMDI3bGFtYmRhPTAuMDAxXHUwMDI3KSwgKDE1MCwgXHUwMDI3bGFtYmRhPTMyXHUwMDI3KSwgKDI4MCwgXHUwMDI3bGFtYmRhPTFlNFx1MDAyNyldOlxuICAgIHByaW50KGZcdTAwMjcgIHtsYWJlbH06IGNvZWYgbm9ybSA9IHtucC5saW5hbGcubm9ybShjb2Vmc1tpZHhdKTouM2Z9XHUwMDI3KVxucHJpbnQoXHUwMDI3QWxsIGNvZWZzIHNocmluayB0b3dhcmQgemVybyBhcyBsYW1iZGEgaW5jcmVhc2VzOyBub25lIGJlY29tZSBleGFjdGx5IHplcm8uXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik9MUyB2cyBSaWRnZSB2cyBMQVNTTyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiT0xTIiwiUmlkZ2UgKEwyKSIsIkxBU1NPIChMMSkiXSwicm93cyI6W1siQ2xvc2VkIGZvcm0iLCJZZXMg4oCUIChY4bWAWCnigbvCuVjhtYB5IiwiWWVzIOKAlCAoWOG1gFgrzrtJKeKBu8K5WOG1gHkiLCJObyDigJQgbm9uLWRpZmZlcmVudGlhYmxlIGF0IDAiXSxbIkhhbmRsZXMgbXVsdGljb2xsaW5lYXJpdHkiLCJObyDigJQgWOG1gFggbWF5IGJlIHNpbmd1bGFyIiwiWWVzIOKAlCDOu0kgZ3VhcmFudGVlcyBQRCIsIlBhcnRpYWwg4oCUIHBpY2tzIG9uZSBvZiBjb3JyZWxhdGVkIGdyb3VwIl0sWyJFeGFjdCBzcGFyc2l0eSIsIk5vIiwiTm8gKHNocmlua3Mg4omIIDApIiwiWWVzIOKAlCB0cnVlIHplcm9zIl0sWyJCYXllc2lhbiBwcmlvciIsIkZsYXQgKGltcHJvcGVyKSIsIkdhdXNzaWFuIE4oMCwgz4PCsi/Ou8K3SSkiLCJMYXBsYWNlIChkb3VibGUtZXhwb25lbnRpYWwpIl0sWyJHZW9tZXRyeSIsIlVuY29uc3RyYWluZWQgbWluIiwiTDIgYmFsbCAoc3BoZXJlKSIsIkwxIGJhbGwgKGRpYW1vbmQvcG9seXRvcGUpIl0sWyJJbnRlcnByZXRhYmlsaXR5IiwiVW5iaWFzZWQgY29lZmZpY2llbnRzIiwiQmlhc2VkIGJ1dCBzdGFibGUiLCJTcGFyc2UsIGVhc3kgdG8gZXhwbGFpbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR2F1c3MtTWFya292IFRoZW9yZW0gYW5kIEFzc3VtcHRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHYXVzcy1NYXJrb3Y6IE9MUyBpcyBCTFVFIChCZXN0IExpbmVhciBVbmJpYXNlZCBFc3RpbWF0b3IpIHVuZGVyIGZvdXIgY29uZGl0aW9uczogKDEpIGxpbmVhcml0eSBFW3l8WF09WM64LCAoMikgc3RyaWN0IGV4b2dlbmVpdHkgRVvOtXxYXT0wLCAoMykgaG9tb3NjZWRhc3RpY2l0eSBWYXIozrV8WCk9z4PCskksICg0KSBubyBwZXJmZWN0IG11bHRpY29sbGluZWFyaXR5LiBcdTAwMjdCZXN0XHUwMDI3IG1lYW5zIG1pbmltdW0gdmFyaWFuY2UgYW1vbmcgYWxsIGxpbmVhciB1bmJpYXNlZCBlc3RpbWF0b3JzLiBOb3JtYWxpdHkgb2YgzrUgaXMgTk9UIHJlcXVpcmVkIGZvciBCTFVFIOKAlCBpdCBpcyBuZWVkZWQgZm9yIGV4YWN0IGZpbml0ZS1zYW1wbGUgaW5mZXJlbmNlICh0LSBhbmQgRi10ZXN0cykuIFVuZGVyIG5vcm1hbGl0eSwgT0xTIGNvaW5jaWRlcyB3aXRoIE1MRS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkxpbmVhcml0eTogRVt5fFhdPVjOuC4gRGlhZ25vc2Ugd2l0aCByZXNpZHVhbCB2cyBmaXR0ZWQgcGxvdHM7IGZpeCB3aXRoIHRyYW5zZm9ybWF0aW9ucy4iLCJTdHJpY3QgZXhvZ2VuZWl0eTogRVvOtXxYXT0wLiBWaW9sYXRlZCBieSBvbWl0dGVkIHZhcmlhYmxlcywgc2ltdWx0YW5laXR5LCBvciBtZWFzdXJlbWVudCBlcnJvci4iLCJIb21vc2NlZGFzdGljaXR5OiBWYXIozrV8WCk9z4PCskkuIFRlc3Qgd2l0aCBCcmV1c2NoLVBhZ2FuOyBmaXggd2l0aCBXTFMgb3Igc2FuZHdpY2ggc3RhbmRhcmQgZXJyb3JzLiIsIk5vIGF1dG9jb3JyZWxhdGlvbjogQ292KM614bWiLM614rG8KT0wLiBVc2UgRHVyYmluLVdhdHNvbiB0ZXN0OyBhcHBseSBHTFMgb3IgSEFDIGVycm9ycyBmb3IgdGltZSBzZXJpZXMuIiwiTm8gcGVyZmVjdCBtdWx0aWNvbGxpbmVhcml0eTogcmFuayhYKT1wLiBDaGVjayBWSUYg4oCUIHZhbHVlcyBhYm92ZSAxMCBpbmRpY2F0ZSBzZXJpb3VzIGNvbGxpbmVhcml0eS4iLCJOb3JtYWxpdHkgb2YgZXJyb3JzOiBuZWVkZWQgZm9yIGV4YWN0IEYvdCB0ZXN0czsgbm90IHJlcXVpcmVkIGZvciBjb25zaXN0ZW5jeSBvciB0aGUgQkxVRSBwcm9wZXJ0eS4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUi1zcXVhcmVkIGFuZCBBZGp1c3RlZCBSLXNxdWFyZWQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlLCsiA9IDEg4oiSIFJTUy9UU1MgbWVhc3VyZXMgdGhlIHByb3BvcnRpb24gb2YgdG90YWwgdmFyaWFuY2UgZXhwbGFpbmVkLiBJdCBhbHdheXMgaW5jcmVhc2VzIHdoZW4gcHJlZGljdG9ycyBhcmUgYWRkZWQsIGV2ZW4gc3B1cmlvdXMgb25lcywgbWFraW5nIGl0IGEgcG9vciBtb2RlbCBzZWxlY3Rpb24gY3JpdGVyaW9uLiBBZGp1c3RlZCBSwrIgPSAxIOKIkiAoUlNTLyhu4oiScOKIkjEpKS8oVFNTLyhu4oiSMSkpIHBlbmFsaXNlcyBleHRyYSBwYXJhbWV0ZXJzIGFuZCBjYW4gZGVjcmVhc2UuIEZvciBmb3JtYWwgbW9kZWwgY29tcGFyaXNvbiB1c2UgQUlDID0gbsK3bG4oUlNTL24pICsgMnAgb3IgQklDID0gbsK3bG4oUlNTL24pICsgcMK3bG4obikuIEJJQyBwZW5hbGlzZXMgY29tcGxleGl0eSBtb3JlIGhlYXZpbHkgYW5kIGlzIG1vZGVsLXNlbGVjdGlvbiBjb25zaXN0ZW50IOKAlCBpdCBzZWxlY3RzIHRoZSB0cnVlIG1vZGVsIGFzIG7ihpLiiJ4gaWYgdGhlIHRydWUgbW9kZWwgaXMgaW4gdGhlIGNhbmRpZGF0ZSBzZXQuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Linear Regression — OLS, Normal Equations, and QR

Linear regression models the response y ∈ ℝⁿ as y = Xθ + ε, where X ∈ ℝⁿˣᵖ is the design matrix, θ ∈ ℝᵖ are unknown parameters, and ε is the error vector. Under standard Gauss-Markov assumptions, Ordinary Least Squares (OLS) produces the Best Linear Unbiased Estimator. Understanding the closed-form solution, its geometric interpretation through the hat matrix, and numerically stable implementation via QR decomposition is foundational to all supervised learning.

## OLS Objective and Derivation

OLS minimises the Residual Sum of Squares: RSS = ‖y − Xθ‖² = (y − Xθ)ᵀ(y − Xθ). Expanding gives yᵀy − 2θᵀXᵀy + θᵀXᵀXθ. Differentiating with respect to θ and setting the gradient to zero: ∂RSS/∂θ = −2Xᵀy + 2XᵀXθ = 0, which gives the Normal Equations XᵀXθ = Xᵀy. Since XᵀX is positive semi-definite, this is a convex quadratic with a unique minimum when XᵀX is invertible (X has full column rank p).

## Normal Equations and Invertibility

When X has full column rank, the unique OLS solution is θ̂ = (XᵀX)⁻¹Xᵀy. Multicollinearity causes near-rank deficiency: XᵀX becomes nearly singular and the Variance Inflation Factor VIF_j = 1/(1−R²_j) diverges. The condition number satisfies κ(XᵀX) = κ(X)², so forming the normal equations squares the numerical difficulty. Ridge regression guarantees invertibility by adding λI: θ̂_ridge = (XᵀX + λI)⁻¹Xᵀy, which always yields a positive-definite system for λ > 0.

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score

np.random.seed(42)
X, y, true_coef = make_regression(
    n_samples=200, n_features=5, noise=10.0, coef=True, random_state=42
)

# OLS closed form: theta = (X^T X)^{-1} X^T y
X_b = np.hstack([np.ones((len(X), 1)), X])  # prepend intercept column
XtX = X_b.T @ X_b
Xty = X_b.T @ y
theta_ols = np.linalg.solve(XtX, Xty)  # prefer solve over inv

lr = LinearRegression().fit(X, y)

print('OLS scratch: intercept={:.4f}'.format(theta_ols[0]))
print('sklearn:     intercept={:.4f}'.format(lr.intercept_))
print('Max coef difference: {:.2e}'.format(
    np.abs(theta_ols[1:] - lr.coef_).max()))
print('R^2 = {:.4f}'.format(r2_score(y, X_b @ theta_ols)))
```

## QR Decomposition for Numerical Stability

QR decomposition writes X = QR where Q ∈ ℝⁿˣᵖ has orthonormal columns (QᵀQ = I) and R ∈ ℝᵖˣᵖ is upper triangular. Substituting into the normal equations: RᵀRθ = RᵀQᵀy → Rθ = Qᵀy. Solving this triangular system via back-substitution has condition number κ(R) = κ(X), not κ(X)². This avoids squaring the numerical difficulty and is the preferred approach for ill-conditioned designs. LAPACK's dgelsd and dgelsy routines (used by numpy and sklearn) internally use QR with column pivoting.

```python
import numpy as np

np.random.seed(0)
n, p = 150, 12
X = np.random.randn(n, p)
y = X @ np.random.randn(p) + 0.1 * np.random.randn(n)
X_b = np.hstack([np.ones((n, 1)), X])

# Normal equations: condition number squared
kappa_xtx = np.linalg.cond(X_b.T @ X_b)
theta_ne = np.linalg.solve(X_b.T @ X_b, X_b.T @ y)

# QR decomposition: condition number preserved
Q, R = np.linalg.qr(X_b, mode='reduced')
theta_qr = np.linalg.solve(R, Q.T @ y)

kappa_x = np.linalg.cond(X_b)
print(f'cond(X_b)      = {kappa_x:.2f}')
print(f'cond(X_bT X_b) = {kappa_xtx:.2f}  (cond^2 = {kappa_x**2:.2f})')
print(f'Max |theta_NE - theta_QR| = {np.abs(theta_ne - theta_qr).max():.2e}')
print('QR avoids squaring the condition number.')
```

## Hat Matrix and Influence Diagnostics

The hat matrix H = X(XᵀX)⁻¹Xᵀ projects y onto col(X): ŷ = Hy. H is symmetric and idempotent with trace(H) = rank(X) = p. The diagonal hᵢᵢ ∈ [p/n, 1] is the leverage score of observation i — how much it influences its own fitted value. The standard threshold for high leverage is hᵢᵢ > 2p/n. Cook's distance Dᵢ = rᵢ² hᵢᵢ / (p · MSE · (1−hᵢᵢ)²) measures how much the full coefficient vector shifts when observation i is removed, combining leverage and residual magnitude.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(1)
n = 60
X = np.random.randn(n, 3)
y = 2 * X[:, 0] - X[:, 1] + np.random.randn(n)

# Inject a high-leverage outlier
X[-1] = [9.0, 9.0, 9.0]
y[-1] = -30.0

X_b = np.hstack([np.ones((n, 1)), X])
p_params = X_b.shape[1]

H = X_b @ np.linalg.solve(X_b.T @ X_b, X_b.T)
leverages = np.diag(H)
threshold = 2 * p_params / n

lr = LinearRegression().fit(X, y)
resid = y - lr.predict(X)
mse = resid @ resid / (n - p_params)
cooks_d = (resid**2 / (p_params * mse)) * (leverages / (1 - leverages)**2)

print(f'Leverage threshold 2p/n = {threshold:.3f}')
print(f'Outlier leverage = {leverages[-1]:.4f}, Cook D = {cooks_d[-1]:.4f}')
print(f'High-leverage indices: {np.where(leverages > threshold)[0].tolist()}')
print(f'Tr(H) = {leverages.sum():.1f}, p = {p_params}')
```

> **High Leverage ≠ High Influence**: A high-leverage point (large hᵢᵢ) lies far from the centroid of X and has the potential to pull the regression line. It exerts high influence only when it is also a response outlier. Always examine both leverage (hᵢᵢ > 2p/n) and Cook's distance (Dᵢ > 4/n) before removing any observation.

## Ridge Regression Path

Ridge regression adds an L2 penalty: minimise ‖y − Xθ‖² + λ‖θ‖². The closed-form solution θ̂_ridge = (XᵀX + λI)⁻¹Xᵀy always exists for λ > 0 because XᵀX + λI is positive definite even when XᵀX is singular. As λ increases all coefficients shrink proportionally toward zero — but never exactly zero. The Bayesian interpretation: ridge is the MAP estimate under a Gaussian prior θ ~ N(0, σ²I/λ). The optimal λ is found via cross-validation or generalised cross-validation (GCV).

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression

np.random.seed(42)
X, y = make_regression(n_samples=100, n_features=10, n_informative=5,
                        noise=15.0, random_state=42)
scaler = StandardScaler()
X_s = scaler.fit_transform(X)

lambdas = np.logspace(-3, 5, 300)
coefs = np.vstack([Ridge(alpha=lam).fit(X_s, y).coef_ for lam in lambdas])

# Verify closed form at lambda=10
lam_check = 10.0
theta_cf = np.linalg.solve(
    X_s.T @ X_s + lam_check * np.eye(X_s.shape[1]), X_s.T @ y
)
sk_coef = Ridge(alpha=lam_check).fit(X_s, y).coef_
print(f'Closed form vs sklearn at lambda={lam_check}: max diff = {np.abs(theta_cf - sk_coef).max():.2e}')

for idx, label in [(0, 'lambda=0.001'), (150, 'lambda=32'), (280, 'lambda=1e4')]:
    print(f'  {label}: coef norm = {np.linalg.norm(coefs[idx]):.3f}')
print('All coefs shrink toward zero as lambda increases; none become exactly zero.')
```

## OLS vs Ridge vs LASSO Comparison

| Property | OLS | Ridge (L2) | LASSO (L1) |
| --- | --- | --- | --- |
| Closed form | Yes — (XᵀX)⁻¹Xᵀy | Yes — (XᵀX+λI)⁻¹Xᵀy | No — non-differentiable at 0 |
| Handles multicollinearity | No — XᵀX may be singular | Yes — λI guarantees PD | Partial — picks one of correlated group |
| Exact sparsity | No | No (shrinks ≈ 0) | Yes — true zeros |
| Bayesian prior | Flat (improper) | Gaussian N(0, σ²/λ·I) | Laplace (double-exponential) |
| Geometry | Unconstrained min | L2 ball (sphere) | L1 ball (diamond/polytope) |
| Interpretability | Unbiased coefficients | Biased but stable | Sparse, easy to explain |

## Gauss-Markov Theorem and Assumptions

Gauss-Markov: OLS is BLUE (Best Linear Unbiased Estimator) under four conditions: (1) linearity E[y|X]=Xθ, (2) strict exogeneity E[ε|X]=0, (3) homoscedasticity Var(ε|X)=σ²I, (4) no perfect multicollinearity. 'Best' means minimum variance among all linear unbiased estimators. Normality of ε is NOT required for BLUE — it is needed for exact finite-sample inference (t- and F-tests). Under normality, OLS coincides with MLE.

- Linearity: E[y|X]=Xθ. Diagnose with residual vs fitted plots; fix with transformations.
- Strict exogeneity: E[ε|X]=0. Violated by omitted variables, simultaneity, or measurement error.
- Homoscedasticity: Var(ε|X)=σ²I. Test with Breusch-Pagan; fix with WLS or sandwich standard errors.
- No autocorrelation: Cov(εᵢ,εⱼ)=0. Use Durbin-Watson test; apply GLS or HAC errors for time series.
- No perfect multicollinearity: rank(X)=p. Check VIF — values above 10 indicate serious collinearity.
- Normality of errors: needed for exact F/t tests; not required for consistency or the BLUE property.

## R-squared and Adjusted R-squared

R² = 1 − RSS/TSS measures the proportion of total variance explained. It always increases when predictors are added, even spurious ones, making it a poor model selection criterion. Adjusted R² = 1 − (RSS/(n−p−1))/(TSS/(n−1)) penalises extra parameters and can decrease. For formal model comparison use AIC = n·ln(RSS/n) + 2p or BIC = n·ln(RSS/n) + p·ln(n). BIC penalises complexity more heavily and is model-selection consistent — it selects the true model as n→∞ if the true model is in the candidate set.

---

