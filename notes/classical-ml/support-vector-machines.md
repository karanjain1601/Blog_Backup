---
title: "Support Vector Machines — Margin Maximisation and the Dual"
slug: "support-vector-machines"
description: "Derive the hard-margin SVM primal and dual, understand KKT conditions, implement SMO, visualise support vectors, and see why the dual enables the kernel trick."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3VwcG9ydCBWZWN0b3IgTWFjaGluZXMgZmluZCB0aGUgbWF4aW11bS1tYXJnaW4gc2VwYXJhdGluZyBoeXBlcnBsYW5lIGJldHdlZW4gdHdvIGNsYXNzZXMuIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IG9ubHkgdGhlIHRyYWluaW5nIHBvaW50cyBuZWFyZXN0IHRoZSBib3VuZGFyeSDigJQgdGhlIHN1cHBvcnQgdmVjdG9ycyDigJQgZGV0ZXJtaW5lIHRoZSBkZWNpc2lvbiBmdW5jdGlvbi4gVGhlIHByaW1hbCBmb3JtdWxhdGlvbiBpcyBhIHF1YWRyYXRpYyBwcm9ncmFtOyBpdHMgTGFncmFuZ2lhbiBkdWFsIHJlcGxhY2VzIGRhdGEgcG9pbnRzIHdpdGggaW5uZXIgcHJvZHVjdHMsIGVuYWJsaW5nIHRoZSBrZXJuZWwgdHJpY2suIFNWTXMgYWNoaWV2ZSBzdHJvbmcgZ2VuZXJhbGlzYXRpb24gYm91bmRzIHZpYSBWQyB0aGVvcnkgYW5kIHRoZSBtYXJnaW4sIG1ha2luZyB0aGVtIGVmZmVjdGl2ZSBldmVuIGluIGhpZ2ggZGltZW5zaW9ucy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNYXhpbXVtIE1hcmdpbiBDbGFzc2lmaWVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2VwYXJhdGluZyBoeXBlcnBsYW5lIGlzIHt4IDogd+G1gHggKyBiID0gMH0uIEEgcG9pbnQgeOG1oiBpcyBjb3JyZWN0bHkgY2xhc3NpZmllZCBpZiB54bWiKHfhtYB44bWiICsgYikgXHUwMDNlIDAuIFRvIG1heGltaXNlIHRoZSBtYXJnaW4gKHdpZHRoIGJldHdlZW4gdGhlIHR3byBjbGFzcyBib3VuZGFyaWVzKSwgd2UgcmVxdWlyZSB54bWiKHfhtYB44bWiICsgYikg4omlIDEgZm9yIGFsbCBpIGFuZCBtYXhpbWlzZSAyL+KAlnfigJYsIGVxdWl2YWxlbnRseSBtaW5pbWlzaW5nIOKAlnfigJbCsi8yLiBQb2ludHMgdGhhdCBzYXRpc2Z5IHnhtaIod+G1gHjhtaIgKyBiKSA9IDEgYXJlIG9uIHRoZSBtYXJnaW4gYm91bmRhcnkg4oCUIHRoZXNlIGFyZSB0aGUgc3VwcG9ydCB2ZWN0b3JzLiBUaGUgbWFyZ2luIGVxdWFscyAyL+KAlnfigJY7IG1heGltaXNpbmcgaXQgaXMgZXF1aXZhbGVudCB0byBtaW5pbWlzaW5nIOKAlnfigJbCsiBzdWJqZWN0IHRvIHRoZSBjb25zdHJhaW50cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYWdyYW5naWFuIGFuZCBLS1QgQ29uZGl0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHByaW1hbCBpczogbWluX3t3LGJ9IMK94oCWd+KAlsKyIHMudC4geeG1oih34bWAeOG1oitiKSDiiaUgMS4gRm9ybWluZyB0aGUgTGFncmFuZ2lhbjogTCA9IMK94oCWd+KAlsKyIOKIkiDOo+G1os6x4bWiW3nhtaIod+G1gHjhtaIrYiniiJIxXSB3aXRoIM6x4bWiIOKJpSAwLiBTdGF0aW9uYXJpdHkgS0tUIGNvbmRpdGlvbnM6IOKIgkwv4oiCdyA9IHcg4oiSIM6jzrHhtaJ54bWieOG1oiA9IDAg4oaSIHcgPSDOo86x4bWieeG1onjhtaI7IOKIgkwv4oiCYiA9IOKIks6jzrHhtaJ54bWiID0gMC4gQ29tcGxlbWVudGFyeSBzbGFja25lc3M6IM6x4bWiW3nhtaIod+G1gHjhtaIrYiniiJIxXSA9IDAg4oCUIGVpdGhlciDOseG1oj0wIChwb2ludCBvZmYgbWFyZ2luKSBvciB0aGUgY29uc3RyYWludCBpcyBhY3RpdmUgKHBvaW50IGlzIGEgc3VwcG9ydCB2ZWN0b3IpLiBUaGUgZGVjaXNpb24gYm91bmRhcnkgaXMgZGV0ZXJtaW5lZCBlbnRpcmVseSBieSBzdXBwb3J0IHZlY3RvcnMgd2l0aCDOseG1oiBcdTAwM2UgMC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcbmZyb20gc2tsZWFybi5zdm0gaW1wb3J0IFNWQ1xuXG50cnk6XG4gICAgaW1wb3J0IGN2eHB5IGFzIGNwXG5cbiAgICBucC5yYW5kb20uc2VlZCg0MilcbiAgICBYLCB5X3JhdyA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTQwLCBjZW50ZXJzPTIsIHJhbmRvbV9zdGF0ZT00MilcbiAgICB5ID0gMiAqIHlfcmF3IC0gMSAgIyBtYXAgdG8gey0xLCArMX1cblxuICAgIG4sIGQgPSBYLnNoYXBlXG4gICAgd192YXIgPSBjcC5WYXJpYWJsZShkKVxuICAgIGJfdmFyID0gY3AuVmFyaWFibGUoKVxuICAgIGNvbnN0cmFpbnRzID0gW3lbaV0gKiAoWFtpXSBAIHdfdmFyICsgYl92YXIpIFx1MDAzZT0gMSBmb3IgaSBpbiByYW5nZShuKV1cbiAgICBwcm9iID0gY3AuUHJvYmxlbShjcC5NaW5pbWl6ZSgwLjUgKiBjcC5zdW1fc3F1YXJlcyh3X3ZhcikpLCBjb25zdHJhaW50cylcbiAgICBwcm9iLnNvbHZlKHNvbHZlcj1jcC5PU1FQLCBlcHNfYWJzPTFlLTgsIGVwc19yZWw9MWUtOClcblxuICAgIHdfY3Z4ID0gd192YXIudmFsdWVcbiAgICBiX2N2eCA9IGJfdmFyLnZhbHVlXG4gICAgbWFyZ2luID0gMi4wIC8gbnAubGluYWxnLm5vcm0od19jdngpXG5cbiAgICBzdmMgPSBTVkMoa2VybmVsPVx1MDAyN2xpbmVhclx1MDAyNywgQz0xZTYpLmZpdChYLCB5KVxuICAgIHByaW50KGZcdTAwMjdjdnhweSBtYXJnaW46ICAge21hcmdpbjouNGZ9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdza2xlYXJuIG1hcmdpbjogezIuMCAvIG5wLmxpbmFsZy5ub3JtKHN2Yy5jb2VmXyk6LjRmfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3TWF4IHcgZGlmZjogICAgIHtucC5hYnMod19jdnggLSBzdmMuY29lZl9bMF0pLm1heCgpOi40Zn1cdTAwMjcpXG5leGNlcHQgSW1wb3J0RXJyb3I6XG4gICAgcHJpbnQoXHUwMDI3Y3Z4cHkgbm90IGluc3RhbGxlZCDigJQgdXNpbmcgc2NpcHkgZm9yIFFQIGluc3RlYWQuXHUwMDI3KVxuICAgIGZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuICAgIGZyb20gc2tsZWFybi5zdm0gaW1wb3J0IFNWQ1xuICAgIG5wLnJhbmRvbS5zZWVkKDQyKVxuICAgIFgsIHlfcmF3ID0gbWFrZV9ibG9icyhuX3NhbXBsZXM9NDAsIGNlbnRlcnM9MiwgcmFuZG9tX3N0YXRlPTQyKVxuICAgIHN2YyA9IFNWQyhrZXJuZWw9XHUwMDI3bGluZWFyXHUwMDI3LCBDPTFlNikuZml0KFgsIHlfcmF3KVxuICAgIHByaW50KGZcdTAwMjdza2xlYXJuIG1hcmdpbjogezIuMCAvIG5wLmxpbmFsZy5ub3JtKHN2Yy5jb2VmXyk6LjRmfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3U3VwcG9ydCB2ZWN0b3JzOiB7c3ZjLm5fc3VwcG9ydF99XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBEdWFsIFByb2JsZW0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN1YnN0aXR1dGluZyB0aGUgS0tUIGNvbmRpdGlvbnMgdyA9IM6jzrHhtaJ54bWieOG1oiBiYWNrIGludG8gdGhlIExhZ3JhbmdpYW4gZ2l2ZXMgdGhlIGR1YWw6IG1heGltaXNlIM6jzrHhtaIg4oiSIMK9zqPhtaLOo+KxvCDOseG1os6x4rG8eeG1onnisbx44bWi4bWAeOKxvCwgc3ViamVjdCB0byDOseG1oiDiiaUgMCBhbmQgzqPOseG1onnhtaIgPSAwLiBUaGlzIGlzIGEgcXVhZHJhdGljIHByb2dyYW0gaW4gbiB2YXJpYWJsZXMgKG9uZSBwZXIgdHJhaW5pbmcgcG9pbnQpLiBUaGUgb2JqZWN0aXZlIGludm9sdmVzIG9ubHkgaW5uZXIgcHJvZHVjdHMgeOG1ouG1gHjisbwg4oCUIHRoaXMgaXMgd2h5IGtlcm5lbHMgY2FuIHJlcGxhY2UgeOG1gHogd2l0aCBrKHgseikgd2l0aG91dCBjaGFuZ2luZyB0aGUgYWxnb3JpdGhtLiBUaGUgZGVjaXNpb24gZnVuY3Rpb24gaXMgZih4KSA9IHNpZ24ozqMgzrHhtaJ54bWiayh44bWiLHgpICsgYikuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgU1ZDXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcblxuZGVmIHNtb19zaW1wbGlmaWVkKFgsIHksIEM9MWU2LCB0b2w9MWUtNCwgbWF4X3Bhc3Nlcz0xMDApOlxuICAgIG4gPSBsZW4oeSlcbiAgICBhbHBoYSA9IG5wLnplcm9zKG4pXG4gICAgYiA9IDAuMFxuICAgIHBhc3NlcyA9IDBcbiAgICBLID0gWCBAIFguVCAgIyBrZXJuZWwgbWF0cml4IChsaW5lYXIpXG4gICAgd2hpbGUgcGFzc2VzIFx1MDAzYyBtYXhfcGFzc2VzOlxuICAgICAgICBudW1fY2hhbmdlZCA9IDBcbiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uobik6XG4gICAgICAgICAgICBFaSA9IG5wLnN1bShhbHBoYSAqIHkgKiBLWzosIGldKSArIGIgLSB5W2ldXG4gICAgICAgICAgICBpZiAoeVtpXSpFaSBcdTAwM2MgLXRvbCBhbmQgYWxwaGFbaV0gXHUwMDNjIEMpIG9yICh5W2ldKkVpIFx1MDAzZSB0b2wgYW5kIGFscGhhW2ldIFx1MDAzZSAwKTpcbiAgICAgICAgICAgICAgICBqID0gbnAucmFuZG9tLmNob2ljZShbayBmb3IgayBpbiByYW5nZShuKSBpZiBrICE9IGldKVxuICAgICAgICAgICAgICAgIEVqID0gbnAuc3VtKGFscGhhICogeSAqIEtbOiwgal0pICsgYiAtIHlbal1cbiAgICAgICAgICAgICAgICBhaV9vbGQsIGFqX29sZCA9IGFscGhhW2ldLCBhbHBoYVtqXVxuICAgICAgICAgICAgICAgIEwgPSBtYXgoMCwgYWpfb2xkIC0gYWlfb2xkKSBpZiB5W2ldICE9IHlbal0gZWxzZSBtYXgoMCwgYWlfb2xkICsgYWpfb2xkIC0gQylcbiAgICAgICAgICAgICAgICBIID0gbWluKEMsIEMgKyBhal9vbGQgLSBhaV9vbGQpIGlmIHlbaV0gIT0geVtqXSBlbHNlIG1pbihDLCBhaV9vbGQgKyBhal9vbGQpXG4gICAgICAgICAgICAgICAgaWYgTCBcdTAwM2U9IEg6IGNvbnRpbnVlXG4gICAgICAgICAgICAgICAgZXRhID0gMipLW2ksal0gLSBLW2ksaV0gLSBLW2osal1cbiAgICAgICAgICAgICAgICBpZiBldGEgXHUwMDNlPSAwOiBjb250aW51ZVxuICAgICAgICAgICAgICAgIGFscGhhW2pdID0gbnAuY2xpcChhal9vbGQgLSB5W2pdKihFaS1FaikvZXRhLCBMLCBIKVxuICAgICAgICAgICAgICAgIGlmIGFicyhhbHBoYVtqXSAtIGFqX29sZCkgXHUwMDNjIDFlLTU6IGNvbnRpbnVlXG4gICAgICAgICAgICAgICAgYWxwaGFbaV0gKz0geVtpXSp5W2pdKihhal9vbGQgLSBhbHBoYVtqXSlcbiAgICAgICAgICAgICAgICBiIC09IEVpICsgeVtpXSooYWxwaGFbaV0tYWlfb2xkKSpLW2ksaV0gKyB5W2pdKihhbHBoYVtqXS1hal9vbGQpKktbaSxqXVxuICAgICAgICAgICAgICAgIG51bV9jaGFuZ2VkICs9IDFcbiAgICAgICAgcGFzc2VzID0gMCBpZiBudW1fY2hhbmdlZCBcdTAwM2UgMCBlbHNlIHBhc3NlcyArIDFcbiAgICByZXR1cm4gYWxwaGEsIGJcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5X3JhdyA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTMwLCBjZW50ZXJzPTIsIGNsdXN0ZXJfc3RkPTAuOCwgcmFuZG9tX3N0YXRlPTQyKVxueSA9IDIqeV9yYXcgLSAxXG5hbHBoYSwgYiA9IHNtb19zaW1wbGlmaWVkKFgsIHksIEM9MWU2KVxuc3ZzID0gbnAud2hlcmUoYWxwaGEgXHUwMDNlIDFlLTUpWzBdXG5wcmludChmXHUwMDI3U01PIHN1cHBvcnQgdmVjdG9yczoge3N2c31cdTAwMjcpXG5wcmludChmXHUwMDI3c2tsZWFybiBTVnM6ICAgICAgICAge1NWQyhrZXJuZWw9XCJsaW5lYXJcIixDPTFlNikuZml0KFgseSkuc3VwcG9ydF99XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZpc3VhbGlzaW5nIFN1cHBvcnQgVmVjdG9ycyBhbmQgdGhlIERlY2lzaW9uIEJvdW5kYXJ5In0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgU1ZDXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5ID0gbWFrZV9ibG9icyhuX3NhbXBsZXM9NjAsIGNlbnRlcnM9MiwgY2x1c3Rlcl9zdGQ9MC45LCByYW5kb21fc3RhdGU9NDIpXG5cbnN2YyA9IFNWQyhrZXJuZWw9XHUwMDI3bGluZWFyXHUwMDI3LCBDPTFlNilcbnN2Yy5maXQoWCwgeSlcblxudyA9IHN2Yy5jb2VmX1swXVxuYiA9IHN2Yy5pbnRlcmNlcHRfWzBdXG5tYXJnaW4gPSAyLjAgLyBucC5saW5hbGcubm9ybSh3KVxuXG5wcmludChcdTAwMjc9PT0gSGFyZC1tYXJnaW4gU1ZNIERlY2lzaW9uIEJvdW5kYXJ5ID09PVx1MDAyNylcbnByaW50KGZcdTAwMjdXZWlnaHQgdmVjdG9yIHc6IHtucC5yb3VuZCh3LCA0KX1cdTAwMjcpXG5wcmludChmXHUwMDI3QmlhcyBiOiAgICAgICAgICB7YjouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01hcmdpbiB3aWR0aDogICAge21hcmdpbjouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN051bWJlciBvZiBzdXBwb3J0IHZlY3RvcnM6IHtzdmMubl9zdXBwb3J0X31cdTAwMjcpXG5wcmludChmXHUwMDI3U3VwcG9ydCB2ZWN0b3IgaW5kaWNlczoge3N2Yy5zdXBwb3J0X31cdTAwMjcpXG5cbiMgVmVyaWZ5IHN1cHBvcnQgdmVjdG9ycyBhcmUgb24gdGhlIG1hcmdpblxuZm9yIGkgaW4gc3ZjLnN1cHBvcnRfOlxuICAgIG1hcmdpbl92YWwgPSB5W2ldICogKFhbaV0gQCB3ICsgYilcbiAgICBwcmludChmXHUwMDI3ICBQb2ludCB7aX06IHkqKHd4K2IpID0ge21hcmdpbl92YWw6LjRmfSAgKHNob3VsZCBiZSB+MS4wIGZvciBoYXJkLW1hcmdpbilcdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJPbmx5IFN1cHBvcnQgVmVjdG9ycyBNYXR0ZXIiLCJjb250ZW50IjoiVGhlIFNWTSBkZWNpc2lvbiBmdW5jdGlvbiBmKHgpID0gzqPhtaIgzrHhtaJ54bWiayh44bWiLHgpICsgYiBpbnZvbHZlcyBvbmx5IHBvaW50cyB3aXRoIM6x4bWiIFx1MDAzZSAwIOKAlCB0aGUgc3VwcG9ydCB2ZWN0b3JzLiBBbGwgb3RoZXIgdHJhaW5pbmcgcG9pbnRzIGhhdmUgzrHhtaIgPSAwIGFuZCBkbyBub3QgYWZmZWN0IHRoZSBib3VuZGFyeS4gVGhpcyBtYWtlcyBTVk1zIHNwYXJzZSBpbiB0aGUgZHVhbCBhbmQgZWZmaWNpZW50IGF0IHByZWRpY3Rpb24gdGltZS4gVHlwaWNhbGx5IG9ubHkgMTDigJMzMCUgb2YgdHJhaW5pbmcgcG9pbnRzIGJlY29tZSBzdXBwb3J0IHZlY3RvcnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJpbWFsIHZzIER1YWwg4oCUIFdoZW4gdG8gVXNlIEVhY2gifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uc3ZtIGltcG9ydCBTVkNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuXG5ucC5yYW5kb20uc2VlZCgwKVxuWCwgeV9yYXcgPSBtYWtlX2Jsb2JzKG5fc2FtcGxlcz00MCwgY2VudGVycz0yLCBjbHVzdGVyX3N0ZD0wLjgsIHJhbmRvbV9zdGF0ZT0wKVxueSA9IDIgKiB5X3JhdyAtIDFcblxuc3ZjID0gU1ZDKGtlcm5lbD1cdTAwMjdsaW5lYXJcdTAwMjcsIEM9MWU2KVxuc3ZjLmZpdChYLCB5KVxuXG4jIFByaW1hbDogdyBmcm9tIHNrbGVhcm5cbndfcHJpbWFsID0gc3ZjLmNvZWZfWzBdXG5iX3ByaW1hbCA9IHN2Yy5pbnRlcmNlcHRfWzBdXG5cbiMgRHVhbDogcmVjb25zdHJ1Y3QgdyBmcm9tIGR1YWwgYWxwaGFzIGFuZCBzdXBwb3J0IHZlY3RvcnNcbmFscGhhX2R1YWwgPSBzdmMuZHVhbF9jb2VmX1swXSAgICMgPSBhbHBoYV9pICogeV9pIGZvciBzdXBwb3J0IHZlY3RvcnNcblhfc3YgPSBzdmMuc3VwcG9ydF92ZWN0b3JzX1xud19kdWFsID0gWF9zdi5UIEAgYWxwaGFfZHVhbFxuXG5wcmludChcdTAwMjdQcmltYWwgdzpcdTAwMjcsIG5wLnJvdW5kKHdfcHJpbWFsLCA0KSlcbnByaW50KFx1MDAyN0R1YWwgICB3Olx1MDAyNywgbnAucm91bmQod19kdWFsLCAgIDQpKVxucHJpbnQoZlx1MDAyN01heCB8d19wcmltYWwgLSB3X2R1YWx8ID0ge25wLmFicyh3X3ByaW1hbCAtIHdfZHVhbCkubWF4KCk6LjJlfVx1MDAyNylcblxuIyBEZWNpc2lvbiB2YWx1ZXNcbmR2X3ByaW1hbCA9IFggQCB3X3ByaW1hbCArIGJfcHJpbWFsXG5kdl9kdWFsICAgPSBzdmMuZGVjaXNpb25fZnVuY3Rpb24oWClcbnByaW50KGZcdTAwMjdEZWNpc2lvbiBmdW5jdGlvbiBtYXggZGlmZjoge25wLmFicyhkdl9wcmltYWwgLSBkdl9kdWFsKS5tYXgoKTouMmV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0JvdGggcHJpbWFsIGFuZCBkdWFsIGZvcm11bGF0aW9ucyBhZ3JlZS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJpbWFsIHZzIER1YWwgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJBc3BlY3QiLCJQcmltYWwiLCJEdWFsIl0sInJvd3MiOltbIlZhcmlhYmxlcyIsIncg4oiIIOKEneG1iCwgYiDiiIgg4oSdIiwizrEg4oiIIOKEneKBvyJdLFsiUVAgc2l6ZSIsImQrMSB2YXJpYWJsZXMiLCJuIHZhcmlhYmxlcyJdLFsiUHJlZmVycmVkIHdoZW4iLCJuIFx1MDAzZVx1MDAzZSBkICh3aWRlIGRhdGEpIiwiZCBcdTAwM2VcdTAwM2UgbiAodGFsbC9rZXJuZWwgZGF0YSkiXSxbIkVuYWJsZXMga2VybmVscyIsIk5vIOKAlCBleHBsaWNpdCB3IHJlcXVpcmVkIiwiWWVzIOKAlCBvbmx5IHjhtaLhtYB44rG8IGFwcGVhcnMiXSxbIlNwYXJzaXR5IiwiTm8gaW5oZXJlbnQgc3BhcnNpdHkiLCJTcGFyc2U6IM6x4bWiPTAgZm9yIG5vbi1TVnMiXSxbIlByZWRpY3Rpb24gY29zdCIsIk8oZCkgcGVyIHBvaW50IiwiTyhuX3N2IMK3IGQpIHBlciBwb2ludCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiR2VuZXJhbGlzYXRpb24gYW5kIFZDIERpbWVuc2lvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVkMgdGhlb3J5IGJvdW5kcyBnZW5lcmFsaXNhdGlvbiBlcnJvcjogd2l0aCBwcm9iYWJpbGl0eSAx4oiSzrQsIHRlc3QgZXJyb3Ig4omkIHRyYWluaW5nIGVycm9yICsgTyjiiJooVkNfZGltwrdsb2cobikvbiArIGxvZygxL860KS9uKSkuIEZvciBsaW5lYXIgU1ZNcyB0aGUgVkMgZGltZW5zaW9uIGVxdWFscyBkKzEuIEJ1dCB0aGUgbWFyZ2luLWJhc2VkIGJvdW5kIGlzIHRpZ2h0ZXI6IHRlc3QgZXJyb3Ig4omkIE8oUsKyL86zwrIgLyBuICsgbG9nKDEvzrQpL24pIHdoZXJlIFIgaXMgdGhlIGRhdGEgcmFkaXVzIGFuZCDOsyBpcyB0aGUgbWFyZ2luLiBBIGxhcmdlIG1hcmdpbiBpbXBsaWVzIGdvb2QgZ2VuZXJhbGlzYXRpb24gaW5kZXBlbmRlbnQgb2YgZGltZW5zaW9uIGQg4oCUIGV4cGxhaW5pbmcgd2h5IFNWTXMgd2l0aCBrZXJuZWxzIGNhbiBnZW5lcmFsaXNlIGluIGluZmluaXRlLWRpbWVuc2lvbmFsIGZlYXR1cmUgc3BhY2VzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVGhlIFNWTSBtYXJnaW4gYm91bmQgZGVwZW5kcyBvbiBSwrIvzrPCsiwgbm90IG9uIHRoZSBhbWJpZW50IGRpbWVuc2lvbiBkIOKAlCBrZXkgYWR2YW50YWdlIG9mIGxhcmdlLW1hcmdpbiBjbGFzc2lmaWVycy4iLCJTdXBwb3J0IHZlY3RvcnMgYXJlIHRoZSBvbmx5IHRyYWluaW5nIHBvaW50cyB0aGF0IGluZmx1ZW5jZSB0aGUgYm91bmRhcnk7IHJlbW92aW5nIG5vbi1TVnMgbGVhdmVzIHRoZSBtb2RlbCB1bmNoYW5nZWQuIiwiVGhlIGR1YWwgUVAgaGFzIG4gdmFyaWFibGVzOyBTTU8gZGVjb21wb3NlcyBpdCBpbnRvIDItdmFyaWFibGUgc3VicHJvYmxlbXMgc29sdmFibGUgYW5hbHl0aWNhbGx5LiIsIkZvciBsaW5lYXIgU1ZNIHdpdGggbGFyZ2UgbiwgcHJpbWFsIG1ldGhvZHMgKExpYkxpbmVhciwgU0dEKSBhcmUgZmFzdGVyOyBkdWFsIFNNTyBpcyBwcmVmZXJyZWQgZm9yIGtlcm5lbCBTVk1zLiIsIkFsd2F5cyBzY2FsZSBmZWF0dXJlcyBiZWZvcmUgdHJhaW5pbmcgU1ZNIOKAlCB0aGUgTDIgbm9ybSB1c2VkIGluIHRoZSBtYXJnaW4gaXMgc2Vuc2l0aXZlIHRvIGZlYXR1cmUgc2NhbGUuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBDb25zaWRlcmF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmVhdHVyZSBzY2FsaW5nIGlzIGNyaXRpY2FsOiBTVk1zIG9wdGltaXNlIOKAlnfigJbCsiB3aGljaCBpcyBzY2FsZS1zZW5zaXRpdmUsIHNvIGFsd2F5cyB1c2UgU3RhbmRhcmRTY2FsZXIuIFRoZSByZWd1bGFyaXNhdGlvbiBwYXJhbWV0ZXIgQyBjb250cm9scyB0aGUgdHJhZGUtb2ZmIGJldHdlZW4gbWF4aW1pc2luZyB0aGUgbWFyZ2luIGFuZCBhbGxvd2luZyBtaXNjbGFzc2lmaWNhdGlvbnMgKGluIHRoZSBzb2Z0LW1hcmdpbiBjYXNlKS4gQ3Jvc3MtdmFsaWRhdGUgQyBvdmVyIGEgbG9nLXNwYWNlZCBncmlkIChlLmcuLCAxMOKBu8KzIHRvIDEwwrMpLiBGb3IgbGFyZ2UgbiAoXHUwMDNlIDUwLDAwMCksIHVzZSBMaW5lYXJTVkMgKHByaW1hbCBTR0QpIGluc3RlYWQgb2YgU1ZDIChkdWFsIFNNTykgZm9yIGRyYW1hdGljYWxseSBiZXR0ZXIgc3BlZWQuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Support Vector Machines — Margin Maximisation and the Dual

Support Vector Machines find the maximum-margin separating hyperplane between two classes. The key insight is that only the training points nearest the boundary — the support vectors — determine the decision function. The primal formulation is a quadratic program; its Lagrangian dual replaces data points with inner products, enabling the kernel trick. SVMs achieve strong generalisation bounds via VC theory and the margin, making them effective even in high dimensions.

## Maximum Margin Classifier

The separating hyperplane is {x : wᵀx + b = 0}. A point xᵢ is correctly classified if yᵢ(wᵀxᵢ + b) > 0. To maximise the margin (width between the two class boundaries), we require yᵢ(wᵀxᵢ + b) ≥ 1 for all i and maximise 2/‖w‖, equivalently minimising ‖w‖²/2. Points that satisfy yᵢ(wᵀxᵢ + b) = 1 are on the margin boundary — these are the support vectors. The margin equals 2/‖w‖; maximising it is equivalent to minimising ‖w‖² subject to the constraints.

## Lagrangian and KKT Conditions

The primal is: min_{w,b} ½‖w‖² s.t. yᵢ(wᵀxᵢ+b) ≥ 1. Forming the Lagrangian: L = ½‖w‖² − Σᵢαᵢ[yᵢ(wᵀxᵢ+b)−1] with αᵢ ≥ 0. Stationarity KKT conditions: ∂L/∂w = w − Σαᵢyᵢxᵢ = 0 → w = Σαᵢyᵢxᵢ; ∂L/∂b = −Σαᵢyᵢ = 0. Complementary slackness: αᵢ[yᵢ(wᵀxᵢ+b)−1] = 0 — either αᵢ=0 (point off margin) or the constraint is active (point is a support vector). The decision boundary is determined entirely by support vectors with αᵢ > 0.

```python
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

try:
    import cvxpy as cp

    np.random.seed(42)
    X, y_raw = make_blobs(n_samples=40, centers=2, random_state=42)
    y = 2 * y_raw - 1  # map to {-1, +1}

    n, d = X.shape
    w_var = cp.Variable(d)
    b_var = cp.Variable()
    constraints = [y[i] * (X[i] @ w_var + b_var) >= 1 for i in range(n)]
    prob = cp.Problem(cp.Minimize(0.5 * cp.sum_squares(w_var)), constraints)
    prob.solve(solver=cp.OSQP, eps_abs=1e-8, eps_rel=1e-8)

    w_cvx = w_var.value
    b_cvx = b_var.value
    margin = 2.0 / np.linalg.norm(w_cvx)

    svc = SVC(kernel='linear', C=1e6).fit(X, y)
    print(f'cvxpy margin:   {margin:.4f}')
    print(f'sklearn margin: {2.0 / np.linalg.norm(svc.coef_):.4f}')
    print(f'Max w diff:     {np.abs(w_cvx - svc.coef_[0]).max():.4f}')
except ImportError:
    print('cvxpy not installed — using scipy for QP instead.')
    from sklearn.datasets import make_blobs
    from sklearn.svm import SVC
    np.random.seed(42)
    X, y_raw = make_blobs(n_samples=40, centers=2, random_state=42)
    svc = SVC(kernel='linear', C=1e6).fit(X, y_raw)
    print(f'sklearn margin: {2.0 / np.linalg.norm(svc.coef_):.4f}')
    print(f'Support vectors: {svc.n_support_}')
```

## The Dual Problem

Substituting the KKT conditions w = Σαᵢyᵢxᵢ back into the Lagrangian gives the dual: maximise Σαᵢ − ½ΣᵢΣⱼ αᵢαⱼyᵢyⱼxᵢᵀxⱼ, subject to αᵢ ≥ 0 and Σαᵢyᵢ = 0. This is a quadratic program in n variables (one per training point). The objective involves only inner products xᵢᵀxⱼ — this is why kernels can replace xᵀz with k(x,z) without changing the algorithm. The decision function is f(x) = sign(Σ αᵢyᵢk(xᵢ,x) + b).

```python
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_blobs

def smo_simplified(X, y, C=1e6, tol=1e-4, max_passes=100):
    n = len(y)
    alpha = np.zeros(n)
    b = 0.0
    passes = 0
    K = X @ X.T  # kernel matrix (linear)
    while passes < max_passes:
        num_changed = 0
        for i in range(n):
            Ei = np.sum(alpha * y * K[:, i]) + b - y[i]
            if (y[i]*Ei < -tol and alpha[i] < C) or (y[i]*Ei > tol and alpha[i] > 0):
                j = np.random.choice([k for k in range(n) if k != i])
                Ej = np.sum(alpha * y * K[:, j]) + b - y[j]
                ai_old, aj_old = alpha[i], alpha[j]
                L = max(0, aj_old - ai_old) if y[i] != y[j] else max(0, ai_old + aj_old - C)
                H = min(C, C + aj_old - ai_old) if y[i] != y[j] else min(C, ai_old + aj_old)
                if L >= H: continue
                eta = 2*K[i,j] - K[i,i] - K[j,j]
                if eta >= 0: continue
                alpha[j] = np.clip(aj_old - y[j]*(Ei-Ej)/eta, L, H)
                if abs(alpha[j] - aj_old) < 1e-5: continue
                alpha[i] += y[i]*y[j]*(aj_old - alpha[j])
                b -= Ei + y[i]*(alpha[i]-ai_old)*K[i,i] + y[j]*(alpha[j]-aj_old)*K[i,j]
                num_changed += 1
        passes = 0 if num_changed > 0 else passes + 1
    return alpha, b

np.random.seed(42)
X, y_raw = make_blobs(n_samples=30, centers=2, cluster_std=0.8, random_state=42)
y = 2*y_raw - 1
alpha, b = smo_simplified(X, y, C=1e6)
svs = np.where(alpha > 1e-5)[0]
print(f'SMO support vectors: {svs}')
print(f'sklearn SVs:         {SVC(kernel="linear",C=1e6).fit(X,y).support_}')
```

## Visualising Support Vectors and the Decision Boundary

```python
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_blobs

np.random.seed(42)
X, y = make_blobs(n_samples=60, centers=2, cluster_std=0.9, random_state=42)

svc = SVC(kernel='linear', C=1e6)
svc.fit(X, y)

w = svc.coef_[0]
b = svc.intercept_[0]
margin = 2.0 / np.linalg.norm(w)

print('=== Hard-margin SVM Decision Boundary ===')
print(f'Weight vector w: {np.round(w, 4)}')
print(f'Bias b:          {b:.4f}')
print(f'Margin width:    {margin:.4f}')
print(f'Number of support vectors: {svc.n_support_}')
print(f'Support vector indices: {svc.support_}')

# Verify support vectors are on the margin
for i in svc.support_:
    margin_val = y[i] * (X[i] @ w + b)
    print(f'  Point {i}: y*(wx+b) = {margin_val:.4f}  (should be ~1.0 for hard-margin)')
```

> **Only Support Vectors Matter**: The SVM decision function f(x) = Σᵢ αᵢyᵢk(xᵢ,x) + b involves only points with αᵢ > 0 — the support vectors. All other training points have αᵢ = 0 and do not affect the boundary. This makes SVMs sparse in the dual and efficient at prediction time. Typically only 10–30% of training points become support vectors.

## Primal vs Dual — When to Use Each

```python
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_blobs

np.random.seed(0)
X, y_raw = make_blobs(n_samples=40, centers=2, cluster_std=0.8, random_state=0)
y = 2 * y_raw - 1

svc = SVC(kernel='linear', C=1e6)
svc.fit(X, y)

# Primal: w from sklearn
w_primal = svc.coef_[0]
b_primal = svc.intercept_[0]

# Dual: reconstruct w from dual alphas and support vectors
alpha_dual = svc.dual_coef_[0]   # = alpha_i * y_i for support vectors
X_sv = svc.support_vectors_
w_dual = X_sv.T @ alpha_dual

print('Primal w:', np.round(w_primal, 4))
print('Dual   w:', np.round(w_dual,   4))
print(f'Max |w_primal - w_dual| = {np.abs(w_primal - w_dual).max():.2e}')

# Decision values
dv_primal = X @ w_primal + b_primal
dv_dual   = svc.decision_function(X)
print(f'Decision function max diff: {np.abs(dv_primal - dv_dual).max():.2e}')
print(f'Both primal and dual formulations agree.')
```

## Primal vs Dual Comparison

| Aspect | Primal | Dual |
| --- | --- | --- |
| Variables | w ∈ ℝᵈ, b ∈ ℝ | α ∈ ℝⁿ |
| QP size | d+1 variables | n variables |
| Preferred when | n >> d (wide data) | d >> n (tall/kernel data) |
| Enables kernels | No — explicit w required | Yes — only xᵢᵀxⱼ appears |
| Sparsity | No inherent sparsity | Sparse: αᵢ=0 for non-SVs |
| Prediction cost | O(d) per point | O(n_sv · d) per point |

## Generalisation and VC Dimension

VC theory bounds generalisation error: with probability 1−δ, test error ≤ training error + O(√(VC_dim·log(n)/n + log(1/δ)/n)). For linear SVMs the VC dimension equals d+1. But the margin-based bound is tighter: test error ≤ O(R²/γ² / n + log(1/δ)/n) where R is the data radius and γ is the margin. A large margin implies good generalisation independent of dimension d — explaining why SVMs with kernels can generalise in infinite-dimensional feature spaces.

- The SVM margin bound depends on R²/γ², not on the ambient dimension d — key advantage of large-margin classifiers.
- Support vectors are the only training points that influence the boundary; removing non-SVs leaves the model unchanged.
- The dual QP has n variables; SMO decomposes it into 2-variable subproblems solvable analytically.
- For linear SVM with large n, primal methods (LibLinear, SGD) are faster; dual SMO is preferred for kernel SVMs.
- Always scale features before training SVM — the L2 norm used in the margin is sensitive to feature scale.

## Practical Considerations

Feature scaling is critical: SVMs optimise ‖w‖² which is scale-sensitive, so always use StandardScaler. The regularisation parameter C controls the trade-off between maximising the margin and allowing misclassifications (in the soft-margin case). Cross-validate C over a log-spaced grid (e.g., 10⁻³ to 10³). For large n (> 50,000), use LinearSVC (primal SGD) instead of SVC (dual SMO) for dramatically better speed.

---

