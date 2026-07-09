---
title: "SVDD — Support Vector Data Description"
slug: "svdd"
description: "Derive SVDD's primal and dual forms, implement via quadratic programming with cvxpy, visualise the minimum-radius hypersphere, and prove equivalence with OCSVM under the RBF kernel."
tags: ["anomaly-detection", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3VwcG9ydCBWZWN0b3IgRGF0YSBEZXNjcmlwdGlvbiAoVGF4IFx1MDAyNiBEdWluLCAyMDA0KSBmaW5kcyB0aGUgbWluaW11bS1yYWRpdXMgaHlwZXJzcGhlcmUgaW4gYSBrZXJuZWwgZmVhdHVyZSBzcGFjZSB0aGF0IGVuY2xvc2VzIHRoZSBub3JtYWwgdHJhaW5pbmcgZGF0YS4gVW5saWtlIE9DU1ZNIHdoaWNoIHNlcGFyYXRlcyBkYXRhIGZyb20gdGhlIG9yaWdpbiB2aWEgYSBoeXBlcnBsYW5lLCBTVkREIGV4cGxpY2l0bHkgc2Vla3MgYSBjZW50ZXIgYyBhbmQgcmFkaXVzIFIgbWluaW1pc2luZyBSwrIgKyBDwrfOo86+4bWiLiBUaGUgc3BoZXJlIGJvdW5kYXJ5IHNlcnZlcyBhcyB0aGUgYW5vbWFseSBkZWNpc2lvbiBib3VuZGFyeTogdGVzdCBwb2ludHMgb3V0c2lkZSB0aGUgc3BoZXJlIGFyZSBhbm9tYWxpZXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJpbWFsIEZvcm11bGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgU1ZERCBwcmltYWwgcHJvYmxlbSBtaW5pbWlzZXMgc3BoZXJlIHJhZGl1cyBSwrIgc3ViamVjdCB0byBhbGwgbm9ybWFsIHRyYWluaW5nIHBvaW50cyBseWluZyBpbnNpZGUgb3Igb24gdGhlIHNwaGVyZSwgd2l0aCBzbGFjayDOvuG1oiDiiaUgMCBmb3IgcG9pbnRzIG91dHNpZGUuIFRoZSBwYXJhbWV0ZXIgQyA9IDEvKG7Ct2YpIHdoZXJlIGYgaXMgdGhlIGV4cGVjdGVkIG91dGxpZXIgZnJhY3Rpb24gY29udHJvbHMgdGhlIHRyYWRlb2ZmOiBzbWFsbCBDIChsYXJnZSBmKSBhbGxvd3MgbW9yZSBwb2ludHMgb3V0c2lkZSB0aGUgc3BoZXJlIChsb29zZSBzcGhlcmUpOyBsYXJnZSBDIChzbWFsbCBmKSBmb3JjZXMgYSB0aWdodCBzcGhlcmUgY29udGFpbmluZyBuZWFybHkgYWxsIHRyYWluaW5nIHBvaW50cy4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6IlxcbWluX3tSLGMsXFx4aX0gUl4yICsgQ1xcc3VtX2kgXFx4aV9pIFxccXVhZCBcXHRleHR7cy50Ln0gXFxxdWFkIFxcfFxccGhpKHhfaSktY1xcfF4yIFxcbGVxIFJeMiArIFxceGlfaSwgXFxxdWFkIFxceGlfaSBcXGdlcSAwIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRHVhbCBGb3JtdWxhdGlvbiBhbmQgRGVjaXNpb24gRnVuY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBMYWdyYW5naWFuIGR1YWwgZWxpbWluYXRlcyBjLCBleHByZXNzaW5nIHRoZSBvYmplY3RpdmUgaW4gdGVybXMgb2Yga2VybmVsIGV2YWx1YXRpb25zIG9ubHk6IG1heGltaXNlIM6j4bWizrHhtaJrKHjhtaIseOG1oikg4oiSIM6j4bWizqPisbzOseG1os6x4rG8ayh44bWiLHjisbwpIHN1YmplY3QgdG8gMOKJpM6x4bWi4omkQyBhbmQgzqPOseG1oj0xLiBUaGUgc3BoZXJlIGNlbnRlciBpbiBmZWF0dXJlIHNwYWNlIGlzIGMgPSDOo+G1os6x4bWiz4YoeOG1oikuIFRoZSBzcXVhcmVkIGRpc3RhbmNlIG9mIHRlc3QgcG9pbnQgeCogZnJvbSB0aGUgY2VudGVyIGlzIOKAls+GKHgqKeKIkmPigJbCsiA9IGsoeCoseCopIOKIkiAyzqPhtaLOseG1omsoeOG1oix4KikgKyDOo+G1os6j4rG8zrHhtaLOseKxvGsoeOG1oix44rG8KS4gUG9pbnRzIHdpdGggZGlzdGFuY2UgXHUwMDNlIFIgYXJlIGFub21hbGllcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgY3Z4cHkgYXMgY3BcbmZyb20gc2tsZWFybi5tZXRyaWNzLnBhaXJ3aXNlIGltcG9ydCByYmZfa2VybmVsIGFzIHNrX3JiZlxuXG5ucC5yYW5kb20uc2VlZCg0MilcblggPSBucC5yYW5kb20ubm9ybWFsKDAsIDEsICg2MCwgMikpXG5nYW1tYSA9IDAuNVxuSyA9IHNrX3JiZihYLCBnYW1tYT1nYW1tYSlcbm4gPSBsZW4oWClcbkMgPSAwLjEgICMgYWxsb3dzIH4xMCUgb2YgcG9pbnRzIG91dHNpZGUgc3BoZXJlXG5cbmFscGhhID0gY3AuVmFyaWFibGUobilcbm9iamVjdGl2ZSA9IGNwLk1heGltaXplKFxuICAgIGNwLnN1bShjcC5tdWx0aXBseShhbHBoYSwgbnAuZGlhZyhLKSkpIC0gY3AucXVhZF9mb3JtKGFscGhhLCBjcC5wc2Rfd3JhcChLKSlcbilcbmNvbnN0cmFpbnRzID0gW2FscGhhIFx1MDAzZT0gMCwgYWxwaGEgXHUwMDNjPSBDLCBjcC5zdW0oYWxwaGEpID09IDFdXG5wcm9iID0gY3AuUHJvYmxlbShvYmplY3RpdmUsIGNvbnN0cmFpbnRzKVxucHJvYi5zb2x2ZShzb2x2ZXI9Y3AuU0NTLCB2ZXJib3NlPUZhbHNlKVxuXG5hbHBoYV92YWwgPSBhbHBoYS52YWx1ZVxuc3ZfbWFzayA9IGFscGhhX3ZhbCBcdTAwM2UgMWUtNFxucHJpbnQoZlx1MDAyN1N1cHBvcnQgdmVjdG9yczoge3N2X21hc2suc3VtKCl9IC8ge259ICAoQz17Q30pXHUwMDI3KVxuXG4jIENvbXB1dGUgUl4yIGZyb20gYSBib3VuZGFyeSBTVlxuYm5kX21hc2sgPSBzdl9tYXNrIFx1MDAyNiAoYWxwaGFfdmFsIFx1MDAzYyBDIC0gMWUtNClcbmJuZF9pZHggPSBucC53aGVyZShibmRfbWFzaylbMF1cbmlmIGxlbihibmRfaWR4KSBcdTAwM2UgMDpcbiAgICB4X3N2ID0gWFtibmRfaWR4WzBdOmJuZF9pZHhbMF0rMV1cbiAgICBLX3hzdl9hbGwgPSBza19yYmYoWCwgeF9zdiwgZ2FtbWE9Z2FtbWEpLnJhdmVsKClcbiAgICBLX3hzdl94c3YgPSBza19yYmYoeF9zdiwgeF9zdiwgZ2FtbWE9Z2FtbWEpWzAsMF1cbiAgICBjZW50ZXJfbm9ybSA9IGFscGhhX3ZhbCBAIEsgQCBhbHBoYV92YWxcbiAgICBSMiA9IEtfeHN2X3hzdiAtIDIqKGFscGhhX3ZhbCBAIEtfeHN2X2FsbCkgKyBjZW50ZXJfbm9ybVxuICAgIHByaW50KGZcdTAwMjdTcGhlcmUgcmFkaXVzXjIgUl4yID0ge1IyOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU1ZERCBWaXN1YWxpc2F0aW9uIOKAlCBIeXBlcnNwaGVyZSBCb3VuZGFyeSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2hlbiB2aXN1YWxpc2VkIGluIHRoZSBvcmlnaW5hbCAyRCBpbnB1dCBzcGFjZSwgdGhlIFNWREQgYm91bmRhcnkgcHJvamVjdHMgYmFjayBmcm9tIGZlYXR1cmUgc3BhY2UgYXMgYSBjbG9zZWQgY3VydmVkIHJlZ2lvbi4gU3VwcG9ydCB2ZWN0b3JzIChwb2ludHMgd2l0aCDOseG1oiBcdTAwM2UgMCkgbGllIGV4YWN0bHkgb24gb3Igb3V0c2lkZSB0aGUgc3BoZXJlIGJvdW5kYXJ5LiBQb2ludHMgc3RyaWN0bHkgaW5zaWRlIHRoZSBzcGhlcmUgaGF2ZSDOseG1oiA9IDAuIFBvaW50cyBvdXRzaWRlIHdpdGggzrHhtaIgPSBDIGFyZSB0aGUgc2xhY2sgcG9pbnRzIChvdXRsaWVycyBpbiB0cmFpbmluZykuIFRoZSBib3VuZGFyeSBzaGFwZSBkZXBlbmRzIGVudGlyZWx5IG9uIHRoZSBrZXJuZWwg4oCUIFJCRiBjcmVhdGVzIHNtb290aCBibG9iIGJvdW5kYXJpZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgT25lQ2xhc3NTVk1cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ucC5yYW5kb20uc2VlZCg0MilcblggPSBucC5yYW5kb20ubm9ybWFsKDAsIDEsICgyMDAsIDIpKVxuWF9hbm9tID0gbnAuYXJyYXkoW1szLjUsIDMuNV0sIFstMy4wLCAyLjVdLCBbMy4wLCAtMy4wXV0pXG5cbnNjYWxlciA9IFN0YW5kYXJkU2NhbGVyKClcblhfcyAgPSBzY2FsZXIuZml0X3RyYW5zZm9ybShYKVxuWF9hcyA9IHNjYWxlci50cmFuc2Zvcm0oWF9hbm9tKVxuXG4jIFNWREQgPSBPQ1NWTSB3aXRoIFJCRiBrZXJuZWxcbnN2ZGQgPSBPbmVDbGFzc1NWTShrZXJuZWw9XHUwMDI3cmJmXHUwMDI3LCBnYW1tYT0wLjUsIG51PTAuMDUpXG5zdmRkLmZpdChYX3MpXG5cbnh4LCB5eSA9IG5wLm1lc2hncmlkKG5wLmxpbnNwYWNlKC00LCA0LCAxMjApLCBucC5saW5zcGFjZSgtNCwgNCwgMTIwKSlcblogPSBzdmRkLmRlY2lzaW9uX2Z1bmN0aW9uKG5wLmNfW3h4LnJhdmVsKCksIHl5LnJhdmVsKCldKS5yZXNoYXBlKHh4LnNoYXBlKVxuWF9hbGwgPSBucC52c3RhY2soW1hfcywgWF9hc10pXG5wcmVkcyA9IHN2ZGQucHJlZGljdChYX2FsbClcblxucGx0LmZpZ3VyZShmaWdzaXplPSg3LCA2KSlcbnBsdC5jb250b3VyZih4eCwgeXksIFosIGxldmVscz0yMCwgY21hcD1cdTAwMjdjb29sd2FybVx1MDAyNywgYWxwaGE9MC41KVxucGx0LmNvbnRvdXIoeHgsIHl5LCBaLCBsZXZlbHM9WzBdLCBjb2xvcnM9XHUwMDI3a1x1MDAyNywgbGluZXdpZHRocz0yKVxucGx0LnNjYXR0ZXIoWF9zWzosMF0sIFhfc1s6LDFdLCBzPTgsIGFscGhhPTAuNCwgbGFiZWw9XHUwMDI3Tm9ybWFsXHUwMDI3KVxucGx0LnNjYXR0ZXIoWF9hc1s6LDBdLCBYX2FzWzosMV0sIGM9XHUwMDI3cmVkXHUwMDI3LCBtYXJrZXI9XHUwMDI3Klx1MDAyNywgcz0xMjAsIGxhYmVsPVx1MDAyN0Fub21hbHlcdTAwMjcpXG5zdnMgPSBzdmRkLnN1cHBvcnRfdmVjdG9yc19cbnBsdC5zY2F0dGVyKHN2c1s6LDBdLCBzdnNbOiwxXSwgZWRnZWNvbG9ycz1cdTAwMjdnb2xkXHUwMDI3LCBmYWNlY29sb3JzPVx1MDAyN25vbmVcdTAwMjcsXG4gICAgICAgICAgICBzPTYwLCBsdz0yLCBsYWJlbD1cdTAwMjdTdXBwb3J0IFZlY3RvcnNcdTAwMjcpXG5wbHQubGVnZW5kKClcbnBsdC50aXRsZShcdTAwMjdTVkREIOKAlCBNaW5pbXVtLVJhZGl1cyBIeXBlcnNwaGVyZVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3c3ZkZF9ib3VuZGFyeS5wbmdcdTAwMjcsIGRwaT0xMDApIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU1ZERCB2cyBPQ1NWTSDigJQgUkJGIEVxdWl2YWxlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgdGhlIFJCRiBrZXJuZWwgayh4LHkpID0gZXhwKOKIks6z4oCWeOKIknnigJbCsiksIGsoeCx4KT0xIGZvciBhbGwgeCDigJQgZXZlcnkgcG9pbnQgbWFwcyB0byB0aGUgdW5pdCBoeXBlcnNwaGVyZSBpbiBmZWF0dXJlIHNwYWNlLiBTZXBhcmF0aW5nIGZyb20gdGhlIG9yaWdpbiB3aXRoIGEgaHlwZXJwbGFuZSAoT0NTVk0pIGlzIHRoZW4gZXF1aXZhbGVudCB0byBmaW5kaW5nIHRoZSBtaW5pbXVtIGVuY2xvc2luZyBzcGhlcmUgKFNWREQpIGNlbnRyZWQgYXQgdGhlIHByb2plY3Rpb24gb2YgdGhlIG9yaWdpbi4gVGhlIHR3byBwcm9ibGVtcyBzaGFyZSB0aGUgc2FtZSBkdWFsIGZvcm0gYW5kIHByb2R1Y2UgaWRlbnRpY2FsIHN1cHBvcnQgdmVjdG9ycyBhbmQgZGVjaXNpb24gZnVuY3Rpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5zdm0gaW1wb3J0IE9uZUNsYXNzU1ZNXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YID0gbnAucmFuZG9tLm5vcm1hbCgwLCAxLCAoMTUwLCAyKSlcblhfdGVzdCA9IG5wLnJhbmRvbS5yYW5kbig0MCwgMikgKiAzXG5cbnNjYWxlciA9IFN0YW5kYXJkU2NhbGVyKClcblhfcyA9IHNjYWxlci5maXRfdHJhbnNmb3JtKFgpXG5YX3QgPSBzY2FsZXIudHJhbnNmb3JtKFhfdGVzdClcblxuIyBCb3RoIG1vZGVsczogc2FtZSBoeXBlcnBhcmFtZXRlcnMsIHNhbWUga2VybmVsXG5vY3N2bSA9IE9uZUNsYXNzU1ZNKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTAuNSwgbnU9MC4xKS5maXQoWF9zKVxuc3ZkZCAgPSBPbmVDbGFzc1NWTShrZXJuZWw9XHUwMDI3cmJmXHUwMDI3LCBnYW1tYT0wLjUsIG51PTAuMSkuZml0KFhfcylcblxuc2NvcmVzX28gPSBvY3N2bS5kZWNpc2lvbl9mdW5jdGlvbihYX3QpXG5zY29yZXNfcyA9IHN2ZGQuZGVjaXNpb25fZnVuY3Rpb24oWF90KVxucHJlZHNfbyAgPSBvY3N2bS5wcmVkaWN0KFhfdClcbnByZWRzX3MgID0gc3ZkZC5wcmVkaWN0KFhfdClcblxubWF4X2RpZmYgPSBucC5hYnMoc2NvcmVzX28gLSBzY29yZXNfcykubWF4KClcbmFncmVlICAgID0gKHByZWRzX28gPT0gcHJlZHNfcykubWVhbigpXG5wcmludChmXHUwMDI3TWF4IHNjb3JlIGRpZmZlcmVuY2UgKE9DU1ZNIHZzIFNWREQpOiB7bWF4X2RpZmY6LjJlfVx1MDAyNylcbnByaW50KGZcdTAwMjdQcmVkaWN0aW9uIGFncmVlbWVudDoge2FncmVlOi4wJX1cdTAwMjcpXG5wcmludChmXHUwMDI3T0NTVk0gU1ZzOiB7bGVuKG9jc3ZtLnN1cHBvcnRfdmVjdG9yc18pfSAgU1ZERCBTVnM6IHtsZW4oc3ZkZC5zdXBwb3J0X3ZlY3RvcnNfKX1cdTAwMjcpXG5wcmludChcdTAwMjdSQkYga2VybmVsIG1ha2VzIE9DU1ZNIGFuZCBTVkREIG1hdGhlbWF0aWNhbGx5IGVxdWl2YWxlbnQuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmVjdCBvZiBDIG9uIFNwaGVyZSBUaWdodG5lc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIFNWREQsIEMgPSAxLyhuwrdmKSB3aGVyZSBmIGlzIHRoZSB0YXJnZXQgb3V0bGllciBmcmFjdGlvbi4gTGFyZ2VyIEMgKHNtYWxsZXIgZikgcHJvZHVjZXMgYSB0aWdodGVyIHNwaGVyZSB3aXRoIG1vcmUgc3VwcG9ydCB2ZWN0b3JzIGFuZCBmZXdlciB0cmFpbmluZyBwb2ludHMgb3V0c2lkZS4gU21hbGxlciBDIHByb2R1Y2VzIGEgbG9vc2VyIHNwaGVyZS4gU2V0dGluZyBDIHVzaW5nIHRoZSBleHBlY3RlZCBjb250YW1pbmF0aW9uIGZyYWN0aW9uIGdpdmVzIGEgcHJpbmNpcGxlZCBzdGFydGluZyBwb2ludC4gRmluZS10dW5lIHVzaW5nIGEgdmFsaWRhdGlvbiBzZXQgd2l0aCBsYWJlbGxlZCBhbm9tYWxpZXMgb3B0aW1pc2luZyBmb3IgRjEgb3IgQVVQUkMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgT25lQ2xhc3NTVk1cblxubnAucmFuZG9tLnNlZWQoNDIpXG5uID0gMjAwXG5YID0gbnAucmFuZG9tLm5vcm1hbCgwLCAxLCAobiwgMikpXG5YX2MgPSBucC52c3RhY2soW1gsIG5wLnJhbmRvbS51bmlmb3JtKC00LCA0LCAoMTUsIDIpKV0pXG5uX2MgPSBsZW4oWF9jKVxuXG5wcmludChmXHUwMDI3e1wibnUgKEM9MS9udS9uKVwiOlx1MDAzZTE2fSB7XCJTVnNcIjpcdTAwM2U2fSB7XCJUcmFpbiBvdXRsaWVyc1wiOlx1MDAzZTE2fSB7XCJGcmFjdGlvblwiOlx1MDAzZTEwfVx1MDAyNylcbmZvciBudSBpbiBbMC4wMSwgMC4wNSwgMC4xMCwgMC4yMCwgMC40MF06XG4gICAgY2xmID0gT25lQ2xhc3NTVk0oa2VybmVsPVx1MDAyN3JiZlx1MDAyNywgZ2FtbWE9MC41LCBudT1udSkuZml0KFhfYylcbiAgICBwcmVkcyA9IGNsZi5wcmVkaWN0KFhfYylcbiAgICBuX3N2ICA9IGxlbihjbGYuc3VwcG9ydF92ZWN0b3JzXylcbiAgICBuX291dCA9IChwcmVkcyA9PSAtMSkuc3VtKClcbiAgICBwcmludChmXHUwMDI3e251Olx1MDAzZTE2LjJmfSB7bl9zdjpcdTAwM2U2fSB7bl9vdXQ6XHUwMDNlMTZ9IHtuX291dC9uX2M6XHUwMDNlMTAuMiV9XHUwMDI3KVxucHJpbnQoXHUwMDI3bnUgdXBwZXItYm91bmRzIHRyYWluaW5nIG91dGxpZXIgZnJhY3Rpb24gYW5kIGxvd2VyLWJvdW5kcyBTViBmcmFjdGlvbi5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiBUYWJsZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIlNWREQiLCJPQ1NWTSIsIklzb2xhdGlvbiBGb3Jlc3QiXSwicm93cyI6W1siR2VvbWV0cmljIG9iamVjdCIsIk1pbmltdW0tcmFkaXVzIGh5cGVyc3BoZXJlIiwiTWF4aW11bS1tYXJnaW4gaHlwZXJwbGFuZSBmcm9tIG9yaWdpbiIsIk5vIGV4cGxpY2l0IGJvdW5kYXJ5Il0sWyJLZXJuZWwiLCJBbnkgUFNEIGtlcm5lbCIsIkFueSBQU0Qga2VybmVsIiwiTm8ga2VybmVsIl0sWyJDb250YW1pbmF0aW9uIHBhcmFtIiwiQyA9IDEvKG7Ct2YpIiwibnUgPSBvdXRsaWVyIGZyYWN0aW9uIiwiY29udGFtaW5hdGlvbiJdLFsiUkJGIGVxdWl2YWxlbmNlIiwiSWRlbnRpY2FsIHRvIE9DU1ZNIHdpdGggUkJGIiwiSWRlbnRpY2FsIHRvIFNWREQgd2l0aCBSQkYiLCJOL0EiXSxbIkRlZXAgdmFyaWFudCIsIkRlZXAgU1ZERCAobmV1cmFsIG5ldHdvcmsgz4YpIiwiTm90IGRpcmVjdGx5IiwiTm90IGRpcmVjdGx5Il0sWyJIaWdoLWRpbWVuc2lvbmFsIiwiUG9vciAoa2VybmVsIGNvc3QpIiwiUG9vciAoa2VybmVsIGNvc3QpIiwiRXhjZWxsZW50Il1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkRlZXAgU1ZERCIsImNvbnRlbnQiOiJEZWVwIFNWREQgKFJ1ZmYgZXQgYWwuLCAyMDE4KSByZXBsYWNlcyB0aGUga2VybmVsIGZlYXR1cmUgbWFwIM+GIHdpdGggYSBuZXVyYWwgbmV0d29yay4gSXQgam9pbnRseSB0cmFpbnMgdGhlIG5ldHdvcmsgYW5kIG1pbmltaXNlcyB0aGUgcmFkaXVzIG9mIHRoZSBlbmNsb3NpbmcgaHlwZXJzcGhlcmUgaW4gdGhlIG5ldHdvcmtcdTAwMjdzIGVtYmVkZGluZyBzcGFjZS4gVGhlIGtleSB0cmljazogbm8gYmlhcyBhbmQgbm8gQmF0Y2hOb3JtIHRvIHByZXZlbnQgaHlwZXJzcGhlcmUgY29sbGFwc2UgKGFsbCBwb2ludHMgbWFwcGluZyB0byB6ZXJvKS4gRGVlcCBTVkREIGFjaGlldmVzIHN0YXRlLW9mLXRoZS1hcnQgb24gaW1hZ2UgYW5vbWFseSBkZXRlY3Rpb24gYmVuY2htYXJrcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZvciB0YWJ1bGFyIGRhdGEsIFNWREQgPSBPQ1NWTSB3aXRoIFJCRiDigJQgdXNlIHNrbGVhcm4gT25lQ2xhc3NTVk0gZGlyZWN0bHkiLCJTZXQgbnUgPSBleHBlY3RlZCBjb250YW1pbmF0aW9uIGZyYWN0aW9uIGFzIGEgc3RhcnRpbmcgcG9pbnQiLCJGb3IgaW1hZ2UgYW5vbWFseSBkZXRlY3Rpb24sIERlZXAgU1ZERCBvdXRwZXJmb3JtcyBjbGFzc2ljYWwgU1ZERCBzaWduaWZpY2FudGx5IiwiQWx3YXlzIHN0YW5kYXJkaXNlIGlucHV0IGZlYXR1cmVzIGJlZm9yZSBmaXR0aW5nIOKAlCBSQkYgZGlzdGFuY2VzIGRlcGVuZCBvbiBzY2FsZSIsIlVzZSBjdnhweSBmb3Igc21hbGwtc2NhbGUgU1ZERCBmcm9tIHNjcmF0Y2ggdG8gdW5kZXJzdGFuZCB0aGUgZHVhbDsgdXNlIHNrbGVhcm4gYXQgc2NhbGUiXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgaHlwZXJzcGhlcmUgY29sbGFwc2UgcHJvYmxlbSBpbiBEZWVwIFNWREQgb2NjdXJzIHdoZW4gdGhlIG5ldHdvcmsgbWFwcyBhbGwgaW5wdXRzIHRvIGEgc2luZ2xlIGNvbnN0YW50IHZlY3RvciwgYWNoaWV2aW5nIHplcm8gcmFkaXVzIHRyaXZpYWxseS4gU29sdXRpb25zOiByZW1vdmUgYmlhcyBpbiBhbGwgbmV0d29yayBsYXllcnMgKG9yaWdpbmFsIHBhcGVyKSwgd2FybS1zdGFydCB3aXRoIGFuIGF1dG9lbmNvZGVyIGVuY29kZXIsIG9yIHVzZSB0aGUgc29mdC1ib3VuZGFyeSB2YXJpYW50IHdpdGggYSBmcmFjdGlvbiBvZiBwb2ludHMgYWxsb3dlZCBvdXRzaWRlIHRoZSBzcGhlcmUuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQcmFjdGljYWwgU1ZERCB3b3JrZmxvdzogKDEpIHN0YW5kYXJkaXNlIGZlYXR1cmVzLCAoMikgZml0IEVsbGlwdGljRW52ZWxvcGUgYXMgYSBiYXNlbGluZSwgKDMpIGZpdCBPbmVDbGFzc1NWTSB3aXRoIFJCRiBrZXJuZWwgdHVuaW5nIGdhbW1hIG9uIGEgbGFiZWxsZWQgdmFsaWRhdGlvbiBzZXQsICg0KSBpZiBzY29yZSBnYXAgaXMgaW5zdWZmaWNpZW50LCBtb3ZlIHRvIERlZXAgU1ZERCBwcmUtaW5pdGlhbGlzZWQgZnJvbSBhIG5vcm1hbC1kYXRhIGF1dG9lbmNvZGVyIGVuY29kZXIuIEVhY2ggc3RlcCBhZGRzIGNvbXBsZXhpdHkgYnV0IGFsc28gZmxleGliaWxpdHkgYW5kIGV4cHJlc3NpdmVuZXNzLiJ9XQ=="
---
# SVDD — Support Vector Data Description

Support Vector Data Description (Tax & Duin, 2004) finds the minimum-radius hypersphere in a kernel feature space that encloses the normal training data. Unlike OCSVM which separates data from the origin via a hyperplane, SVDD explicitly seeks a center c and radius R minimising R² + C·Σξᵢ. The sphere boundary serves as the anomaly decision boundary: test points outside the sphere are anomalies.

## Primal Formulation

The SVDD primal problem minimises sphere radius R² subject to all normal training points lying inside or on the sphere, with slack ξᵢ ≥ 0 for points outside. The parameter C = 1/(n·f) where f is the expected outlier fraction controls the tradeoff: small C (large f) allows more points outside the sphere (loose sphere); large C (small f) forces a tight sphere containing nearly all training points.

$$\min_{R,c,\xi} R^2 + C\sum_i \xi_i \quad \text{s.t.} \quad \|\phi(x_i)-c\|^2 \leq R^2 + \xi_i, \quad \xi_i \geq 0$$

## Dual Formulation and Decision Function

The Lagrangian dual eliminates c, expressing the objective in terms of kernel evaluations only: maximise Σᵢαᵢk(xᵢ,xᵢ) − ΣᵢΣⱼαᵢαⱼk(xᵢ,xⱼ) subject to 0≤αᵢ≤C and Σαᵢ=1. The sphere center in feature space is c = Σᵢαᵢφ(xᵢ). The squared distance of test point x* from the center is ‖φ(x*)−c‖² = k(x*,x*) − 2Σᵢαᵢk(xᵢ,x*) + ΣᵢΣⱼαᵢαⱼk(xᵢ,xⱼ). Points with distance > R are anomalies.

```python
import numpy as np
import cvxpy as cp
from sklearn.metrics.pairwise import rbf_kernel as sk_rbf

np.random.seed(42)
X = np.random.normal(0, 1, (60, 2))
gamma = 0.5
K = sk_rbf(X, gamma=gamma)
n = len(X)
C = 0.1  # allows ~10% of points outside sphere

alpha = cp.Variable(n)
objective = cp.Maximize(
    cp.sum(cp.multiply(alpha, np.diag(K))) - cp.quad_form(alpha, cp.psd_wrap(K))
)
constraints = [alpha >= 0, alpha <= C, cp.sum(alpha) == 1]
prob = cp.Problem(objective, constraints)
prob.solve(solver=cp.SCS, verbose=False)

alpha_val = alpha.value
sv_mask = alpha_val > 1e-4
print(f'Support vectors: {sv_mask.sum()} / {n}  (C={C})')

# Compute R^2 from a boundary SV
bnd_mask = sv_mask & (alpha_val < C - 1e-4)
bnd_idx = np.where(bnd_mask)[0]
if len(bnd_idx) > 0:
    x_sv = X[bnd_idx[0]:bnd_idx[0]+1]
    K_xsv_all = sk_rbf(X, x_sv, gamma=gamma).ravel()
    K_xsv_xsv = sk_rbf(x_sv, x_sv, gamma=gamma)[0,0]
    center_norm = alpha_val @ K @ alpha_val
    R2 = K_xsv_xsv - 2*(alpha_val @ K_xsv_all) + center_norm
    print(f'Sphere radius^2 R^2 = {R2:.4f}')
```

## SVDD Visualisation — Hypersphere Boundary

When visualised in the original 2D input space, the SVDD boundary projects back from feature space as a closed curved region. Support vectors (points with αᵢ > 0) lie exactly on or outside the sphere boundary. Points strictly inside the sphere have αᵢ = 0. Points outside with αᵢ = C are the slack points (outliers in training). The boundary shape depends entirely on the kernel — RBF creates smooth blob boundaries.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X = np.random.normal(0, 1, (200, 2))
X_anom = np.array([[3.5, 3.5], [-3.0, 2.5], [3.0, -3.0]])

scaler = StandardScaler()
X_s  = scaler.fit_transform(X)
X_as = scaler.transform(X_anom)

# SVDD = OCSVM with RBF kernel
svdd = OneClassSVM(kernel='rbf', gamma=0.5, nu=0.05)
svdd.fit(X_s)

xx, yy = np.meshgrid(np.linspace(-4, 4, 120), np.linspace(-4, 4, 120))
Z = svdd.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
X_all = np.vstack([X_s, X_as])
preds = svdd.predict(X_all)

plt.figure(figsize=(7, 6))
plt.contourf(xx, yy, Z, levels=20, cmap='coolwarm', alpha=0.5)
plt.contour(xx, yy, Z, levels=[0], colors='k', linewidths=2)
plt.scatter(X_s[:,0], X_s[:,1], s=8, alpha=0.4, label='Normal')
plt.scatter(X_as[:,0], X_as[:,1], c='red', marker='*', s=120, label='Anomaly')
svs = svdd.support_vectors_
plt.scatter(svs[:,0], svs[:,1], edgecolors='gold', facecolors='none',
            s=60, lw=2, label='Support Vectors')
plt.legend()
plt.title('SVDD — Minimum-Radius Hypersphere')
plt.tight_layout()
plt.savefig('svdd_boundary.png', dpi=100)
```

## SVDD vs OCSVM — RBF Equivalence

For the RBF kernel k(x,y) = exp(−γ‖x−y‖²), k(x,x)=1 for all x — every point maps to the unit hypersphere in feature space. Separating from the origin with a hyperplane (OCSVM) is then equivalent to finding the minimum enclosing sphere (SVDD) centred at the projection of the origin. The two problems share the same dual form and produce identical support vectors and decision functions.

```python
import numpy as np
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X = np.random.normal(0, 1, (150, 2))
X_test = np.random.randn(40, 2) * 3

scaler = StandardScaler()
X_s = scaler.fit_transform(X)
X_t = scaler.transform(X_test)

# Both models: same hyperparameters, same kernel
ocsvm = OneClassSVM(kernel='rbf', gamma=0.5, nu=0.1).fit(X_s)
svdd  = OneClassSVM(kernel='rbf', gamma=0.5, nu=0.1).fit(X_s)

scores_o = ocsvm.decision_function(X_t)
scores_s = svdd.decision_function(X_t)
preds_o  = ocsvm.predict(X_t)
preds_s  = svdd.predict(X_t)

max_diff = np.abs(scores_o - scores_s).max()
agree    = (preds_o == preds_s).mean()
print(f'Max score difference (OCSVM vs SVDD): {max_diff:.2e}')
print(f'Prediction agreement: {agree:.0%}')
print(f'OCSVM SVs: {len(ocsvm.support_vectors_)}  SVDD SVs: {len(svdd.support_vectors_)}')
print('RBF kernel makes OCSVM and SVDD mathematically equivalent.')
```

## Effect of C on Sphere Tightness

In SVDD, C = 1/(n·f) where f is the target outlier fraction. Larger C (smaller f) produces a tighter sphere with more support vectors and fewer training points outside. Smaller C produces a looser sphere. Setting C using the expected contamination fraction gives a principled starting point. Fine-tune using a validation set with labelled anomalies optimising for F1 or AUPRC.

```python
import numpy as np
from sklearn.svm import OneClassSVM

np.random.seed(42)
n = 200
X = np.random.normal(0, 1, (n, 2))
X_c = np.vstack([X, np.random.uniform(-4, 4, (15, 2))])
n_c = len(X_c)

print(f'{"nu (C=1/nu/n)":>16} {"SVs":>6} {"Train outliers":>16} {"Fraction":>10}')
for nu in [0.01, 0.05, 0.10, 0.20, 0.40]:
    clf = OneClassSVM(kernel='rbf', gamma=0.5, nu=nu).fit(X_c)
    preds = clf.predict(X_c)
    n_sv  = len(clf.support_vectors_)
    n_out = (preds == -1).sum()
    print(f'{nu:>16.2f} {n_sv:>6} {n_out:>16} {n_out/n_c:>10.2%}')
print('nu upper-bounds training outlier fraction and lower-bounds SV fraction.')
```

## Comparison Table

| Property | SVDD | OCSVM | Isolation Forest |
| --- | --- | --- | --- |
| Geometric object | Minimum-radius hypersphere | Maximum-margin hyperplane from origin | No explicit boundary |
| Kernel | Any PSD kernel | Any PSD kernel | No kernel |
| Contamination param | C = 1/(n·f) | nu = outlier fraction | contamination |
| RBF equivalence | Identical to OCSVM with RBF | Identical to SVDD with RBF | N/A |
| Deep variant | Deep SVDD (neural network φ) | Not directly | Not directly |
| High-dimensional | Poor (kernel cost) | Poor (kernel cost) | Excellent |

> **Deep SVDD**: Deep SVDD (Ruff et al., 2018) replaces the kernel feature map φ with a neural network. It jointly trains the network and minimises the radius of the enclosing hypersphere in the network's embedding space. The key trick: no bias and no BatchNorm to prevent hypersphere collapse (all points mapping to zero). Deep SVDD achieves state-of-the-art on image anomaly detection benchmarks.

- For tabular data, SVDD = OCSVM with RBF — use sklearn OneClassSVM directly
- Set nu = expected contamination fraction as a starting point
- For image anomaly detection, Deep SVDD outperforms classical SVDD significantly
- Always standardise input features before fitting — RBF distances depend on scale
- Use cvxpy for small-scale SVDD from scratch to understand the dual; use sklearn at scale

The hypersphere collapse problem in Deep SVDD occurs when the network maps all inputs to a single constant vector, achieving zero radius trivially. Solutions: remove bias in all network layers (original paper), warm-start with an autoencoder encoder, or use the soft-boundary variant with a fraction of points allowed outside the sphere.

Practical SVDD workflow: (1) standardise features, (2) fit EllipticEnvelope as a baseline, (3) fit OneClassSVM with RBF kernel tuning gamma on a labelled validation set, (4) if score gap is insufficient, move to Deep SVDD pre-initialised from a normal-data autoencoder encoder. Each step adds complexity but also flexibility and expressiveness.

