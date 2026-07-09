---
title: "Statistical Anomaly Detection — Z-Score, IQR, and Grubbs Test"
slug: "statistical-anomaly-detection"
description: "Master univariate anomaly detection with Z-score, modified Z-score (MAD), IQR fences, Grubbs test, and extreme value theory — with robust implementations and statistical foundations."
tags: ["anomaly-detection", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhdGlzdGljYWwgbWV0aG9kcyBkZXRlY3QgYW5vbWFsaWVzIGJ5IG1vZGVsbGluZyB0aGUgZXhwZWN0ZWQgZGlzdHJpYnV0aW9uIG9mIG5vcm1hbCBkYXRhIGFuZCBmbGFnZ2luZyBvYnNlcnZhdGlvbnMgaW4gdGhlIHRhaWxzLiBUaGV5IGFyZSBpbnRlcnByZXRhYmxlLCBmYXN0LCBhbmQgcmVxdWlyZSBubyB0cmFpbmluZyBiZXlvbmQgc3VtbWFyeSBzdGF0aXN0aWNzLiBUaGUgY29yZSB0cmFkZW9mZiBpcyB0aGUgZGlzdHJpYnV0aW9uYWwgYXNzdW1wdGlvbjogWi1zY29yZSBhc3N1bWVzIEdhdXNzaWFuLCBJUVIgaXMgZGlzdHJpYnV0aW9uLWZyZWUgYnV0IHVuaXZhcmlhdGUsIGFuZCBleHRyZW1lIHZhbHVlIHRoZW9yeSB0YXJnZXRzIHRoZSBiZWhhdmlvdXIgb2YgYmxvY2sgbWF4aW1hLiBBbGwgbWV0aG9kcyBhcmUgc3RyaWN0bHkgdW5pdmFyaWF0ZSDigJQgdGhleSBmbGFnIGluZGl2aWR1YWwgZmVhdHVyZXMsIG5vdCBjb21iaW5hdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiWi1TY29yZSBNZXRob2QifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBaLXNjb3JlIHN0YW5kYXJkaXNlcyBlYWNoIG9ic2VydmF0aW9uIHJlbGF0aXZlIHRvIHRoZSBzYW1wbGUgbWVhbiBhbmQgc3RhbmRhcmQgZGV2aWF0aW9uLiBQb2ludHMgd2l0aCB8enwgXHUwMDNlIDMgZmFsbCBtb3JlIHRoYW4gdGhyZWUgc3RhbmRhcmQgZGV2aWF0aW9ucyBmcm9tIHRoZSBtZWFuOyB1bmRlciBhIEdhdXNzaWFuIHRoaXMgZW5jb21wYXNzZXMgOTkuNzMlIG9mIHByb2JhYmlsaXR5IG1hc3MsIHNvIGZsYWdnZWQgcG9pbnRzIGFyZSByYXJlIGJ5IGNvbnN0cnVjdGlvbi4gSG93ZXZlciwgYm90aCDOvCBhbmQgz4MgYXJlIG5vbi1yb2J1c3Q6IGEgc2luZ2xlIGV4dHJlbWUgb3V0bGllciBpbmZsYXRlcyDPgyBhbmQgZGVmbGF0ZXMgZXZlcnkgb3RoZXIgWi1zY29yZSDigJQgdGhlIG1hc2tpbmcgZWZmZWN0LiBPbmUtc2lkZWQgdGVzdHMgKHogXHUwMDNlIDMgb25seSkgYXJlIGFwcHJvcHJpYXRlIHdoZW4gYW5vbWFsaWVzIG9jY3VyIG9ubHkgaW4gdGhlIHBvc2l0aXZlIGRpcmVjdGlvbi4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6InpfaSA9IFxcZnJhY3t4X2kgLSBcXG11fXtcXHNpZ21hfSwgXFxxdWFkIFxcdGV4dHtmbGFnIGlmIH0gfHpfaXwgXHUwMDNlIDMifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb2RpZmllZCBaLVNjb3JlIOKAlCBNQUQtQmFzZWQgUm9idXN0bmVzcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1vZGlmaWVkIFotc2NvcmUgcmVwbGFjZXMgzrwgd2l0aCB0aGUgc2FtcGxlIG1lZGlhbiB4zIMgYW5kIM+DIHdpdGggTUFEID0gbWVkaWFuKHx44bWiIOKIkiB4zIN8KS4gVGhlIGNvbnN0YW50IDAuNjc0NSBtYWtlcyBNQUQgYSBjb25zaXN0ZW50IGVzdGltYXRvciBvZiDPgyB1bmRlciBhIEdhdXNzaWFuLiBCb3RoIG1lZGlhbiBhbmQgTUFEIGhhdmUgYnJlYWtkb3duIHBvaW50IDUwJTogdXAgdG8gaGFsZiB0aGUgZGF0YSBjYW4gYmUgY29ycnVwdGVkIHdpdGhvdXQgZGlzdG9ydGluZyB0aGUgZXN0aW1hdGVzLiBSZWNvbW1lbmRlZCB0aHJlc2hvbGQgaXMgfE3htaJ8IFx1MDAzZSAzLjUuIFRoZSBtb2RpZmllZCBaLXNjb3JlIGlzIHRoZSBwcmVmZXJyZWQgdW5pdmFyaWF0ZSBtZXRob2Qgd2hlbiB0aGUgZGF0YSBtYXkgYmUgY29udGFtaW5hdGVkLiJ9LHsidHlwZSI6Im1hdGgiLCJkaXNwbGF5Ijp0cnVlLCJjb250ZW50IjoiTV9pID0gXFxmcmFjezAuNjc0NSh4X2kgLSBcXHRpbGRle3h9KX17XFxvcGVyYXRvcm5hbWV7TUFEfX0sIFxccXVhZCBcXG9wZXJhdG9ybmFtZXtNQUR9ID0gXFxvcGVyYXRvcm5hbWV7bWVkaWFufSh8eF9pIC0gXFx0aWxkZXt4fXwpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweSBpbXBvcnQgc3RhdHNcblxubnAucmFuZG9tLnNlZWQoNDIpXG5kYXRhID0gbnAuY29uY2F0ZW5hdGUoW25wLnJhbmRvbS5ub3JtYWwoMCwgMSwgMTAwKSwgWzEwLjAsIC04LjUsIDE1LjBdXSlcblxuZGVmIHpzY29yZV9mbGFncyh4LCB0aHJlc2hvbGQ9My4wKTpcbiAgICBtdSwgc2lnbWEgPSB4Lm1lYW4oKSwgeC5zdGQoZGRvZj0xKVxuICAgIHogPSAoeCAtIG11KSAvIHNpZ21hXG4gICAgcmV0dXJuIG5wLmFicyh6KSBcdTAwM2UgdGhyZXNob2xkLCB6XG5cbmRlZiBtb2RpZmllZF96c2NvcmVfZmxhZ3MoeCwgdGhyZXNob2xkPTMuNSk6XG4gICAgbWVkID0gbnAubWVkaWFuKHgpXG4gICAgbWFkID0gbnAubWVkaWFuKG5wLmFicyh4IC0gbWVkKSlcbiAgICBtYWQgPSBtYXgobWFkLCAxZS05KVxuICAgIG0gPSAwLjY3NDUgKiAoeCAtIG1lZCkgLyBtYWRcbiAgICByZXR1cm4gbnAuYWJzKG0pIFx1MDAzZSB0aHJlc2hvbGQsIG1cblxuZmxhZ196LCB6X3Njb3JlcyAgID0genNjb3JlX2ZsYWdzKGRhdGEpXG5mbGFnX216LCBtel9zY29yZXMgPSBtb2RpZmllZF96c2NvcmVfZmxhZ3MoZGF0YSlcbnByaW50KGZcdTAwMjdaLXNjb3JlOiAgICAgICAgICB7ZmxhZ196LnN1bSgpfSBhbm9tYWxpZXMgYXQge25wLndoZXJlKGZsYWdfeilbMF0udG9saXN0KCl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN01vZGlmaWVkIFotc2NvcmU6IHtmbGFnX216LnN1bSgpfSBhbm9tYWxpZXMgYXQge25wLndoZXJlKGZsYWdfbXopWzBdLnRvbGlzdCgpfVx1MDAyNylcblxuIyBNYXNraW5nOiBpbmplY3RpbmcgYSBnaWFudCBvdXRsaWVyIHJlZHVjZXMgc2Vuc2l0aXZpdHkgb2Ygc3RhbmRhcmQgWi1zY29yZVxubWFza2VkID0gbnAuY29uY2F0ZW5hdGUoW2RhdGEsIFsxMDAuMF1dKVxuZmxhZ19tYXNrZWQsIF8gPSB6c2NvcmVfZmxhZ3MobWFza2VkKVxucHJpbnQoZlx1MDAyN0FmdGVyIGluamVjdGluZyAxMDAuMCDigJQgWi1zY29yZSBkZXRlY3RzOiB7ZmxhZ19tYXNrZWQuc3VtKCl9IChtYXNraW5nIGluZmxhdGVzIHNpZ21hKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJUVIgTWV0aG9kIOKAlCBEaXN0cmlidXRpb24tRnJlZSBCb3VuZHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBJUVIgbWV0aG9kIHNldHMgYm91bmRzIGxvd2VyID0gUTEg4oiSIGvCt0lRUiBhbmQgdXBwZXIgPSBRMyArIGvCt0lRUi4gVHVrZXkgaW5uZXIgZmVuY2VzIHVzZSBrPTEuNSAoZmxhZ3MgfjAuNyUgb2YgR2F1c3NpYW4gZGF0YSk7IG91dGVyIGZlbmNlcyB1c2Ugaz0zLjAgZm9yIGV4dHJlbWUgb3V0bGllcnMuIFRoZSBtZXRob2QgcmVxdWlyZXMgbm8gZGlzdHJpYnV0aW9uYWwgYXNzdW1wdGlvbiwgaXMgcmVzaXN0YW50IHRvIHNrZXdlZCBkaXN0cmlidXRpb25zLCBhbmQgaXMgdGhlIHN0YW5kYXJkIGNob2ljZSBmb3IgZXhwbG9yYXRvcnkgZGF0YSBhbmFseXNpcy4gSXRzIHByaW1hcnkgbGltaXRhdGlvbiBpcyBzdHJpY3QgdW5pdmFyaWF0ZSBzY29wZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuZGF0YSA9IG5wLmNvbmNhdGVuYXRlKFtucC5yYW5kb20ubm9ybWFsKDUwLCAxMCwgMjAwKSwgWzUuMCwgLTEwLjAsIDExMC4wLCAxMjUuMF1dKVxuXG5kZWYgaXFyX2JvdW5kcyh4LCBrPTEuNSk6XG4gICAgUTEsIFEzID0gbnAucGVyY2VudGlsZSh4LCBbMjUsIDc1XSlcbiAgICBJUVIgPSBRMyAtIFExXG4gICAgcmV0dXJuIFExIC0gayAqIElRUiwgUTMgKyBrICogSVFSLCBJUVJcblxubG93ZXIsIHVwcGVyLCBpcXIgPSBpcXJfYm91bmRzKGRhdGEpXG5mbGFncyA9IChkYXRhIFx1MDAzYyBsb3dlcikgfCAoZGF0YSBcdTAwM2UgdXBwZXIpXG5cbmZpZywgKGF4MSwgYXgyKSA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMiwgNSkpXG5heDEuYm94cGxvdChkYXRhLCB2ZXJ0PVRydWUpXG5heDEuc2V0X3RpdGxlKFx1MDAyN0JveCBQbG90IHdpdGggSVFSIEZlbmNlc1x1MDAyNylcbmNvbG9ycyA9IFtcdTAwMjdyZWRcdTAwMjcgaWYgZiBlbHNlIFx1MDAyN3N0ZWVsYmx1ZVx1MDAyNyBmb3IgZiBpbiBmbGFnc11cbmF4Mi5zY2F0dGVyKHJhbmdlKGxlbihkYXRhKSksIGRhdGEsIGM9Y29sb3JzLCBhbHBoYT0wLjYsIHM9MjApXG5heDIuYXhobGluZShsb3dlciwgY29sb3I9XHUwMDI3b3JhbmdlXHUwMDI3LCBsaW5lc3R5bGU9XHUwMDI3LS1cdTAwMjcsIGxhYmVsPWZcdTAwMjdMb3dlcj17bG93ZXI6LjFmfVx1MDAyNylcbmF4Mi5heGhsaW5lKHVwcGVyLCBjb2xvcj1cdTAwMjdvcmFuZ2VcdTAwMjcsIGxpbmVzdHlsZT1cdTAwMjctLVx1MDAyNywgbGFiZWw9Zlx1MDAyN1VwcGVyPXt1cHBlcjouMWZ9XHUwMDI3KVxuYXgyLmxlZ2VuZCgpXG5heDIuc2V0X3RpdGxlKGZcdTAwMjdJUVIgQW5vbWFsaWVzIChrPTEuNSk6IHtmbGFncy5zdW0oKX0gZmxhZ2dlZFx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3aXFyX2Fub21hbGllcy5wbmdcdTAwMjcsIGRwaT0xMDApXG5wcmludChmXHUwMDI3SVFSPXtpcXI6LjJmfSAgQm91bmRzPVt7bG93ZXI6LjJmfSwge3VwcGVyOi4yZn1dICBGbGFnZ2VkOiB7ZmxhZ3Muc3VtKCl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdydWJicyBUZXN0IOKAlCBGb3JtYWwgSHlwb3RoZXNpcyBUZXN0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgR3J1YmJzIHRlc3QgKDE5NjkpIGZvcm1hbGx5IHRlc3RzIEjigoA6IG5vIG91dGxpZXJzIGluIGEgR2F1c3NpYW4gc2FtcGxlLiBUZXN0IHN0YXRpc3RpYyBHID0gbWF4fHjhtaIg4oiSIHjMhHwvcyBpcyBjb21wYXJlZCBhZ2FpbnN0IGEgY3JpdGljYWwgdmFsdWUgZnJvbSB0aGUgdC1kaXN0cmlidXRpb24gYXQgc2lnbmlmaWNhbmNlIM6xLiBUaGUgc2VxdWVudGlhbCBHcnViYnMgcHJvY2VkdXJlIHJlbW92ZXMgdGhlIGlkZW50aWZpZWQgb3V0bGllciBhbmQgcmV0ZXN0cyDigJQgYnV0IGVhY2ggaXRlcmF0aW9uIHNob3VsZCB1c2UgYSBjb3JyZWN0ZWQgc2lnbmlmaWNhbmNlIGxldmVsIHRvIGNvbnRyb2wgZmFtaWx5LXdpc2UgZXJyb3IuIE5vcm1hbGl0eSBzaG91bGQgYmUgdmVyaWZpZWQgd2l0aCBTaGFwaXJvLVdpbGsgYmVmb3JlIGFwcGx5aW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkgaW1wb3J0IHN0YXRzXG5cbmRlZiBncnViYnNfc3RhdCh4KTpcbiAgICByZXR1cm4gbnAubWF4KG5wLmFicyh4IC0geC5tZWFuKCkpKSAvIHguc3RkKGRkb2Y9MSlcblxuZGVmIGdydWJic19jcml0aWNhbChuLCBhbHBoYT0wLjA1KTpcbiAgICAjIFR3by1zaWRlZCBjcml0aWNhbCB2YWx1ZSB2aWEgdC1kaXN0cmlidXRpb24gKEdydWJicyAxOTY5KVxuICAgIHAgPSBhbHBoYSAvICgyICogbilcbiAgICB0ID0gc3RhdHMudC5wcGYoMSAtIHAsIGRmPW4gLSAyKVxuICAgIHJldHVybiAoKG4gLSAxKSAvIG5wLnNxcnQobikpICogbnAuc3FydCh0KioyIC8gKG4gLSAyICsgdCoqMikpXG5cbmRlZiBncnViYnNfdGVzdCh4LCBhbHBoYT0wLjA1KTpcbiAgICBuID0gbGVuKHgpXG4gICAgRyA9IGdydWJic19zdGF0KHgpXG4gICAgR19jcml0ID0gZ3J1YmJzX2NyaXRpY2FsKG4sIGFscGhhKVxuICAgIGlkeCA9IGludChucC5hcmdtYXgobnAuYWJzKHggLSB4Lm1lYW4oKSkpKVxuICAgIHJldHVybiBHLCBHX2NyaXQsIEcgXHUwMDNlIEdfY3JpdCwgaWR4LCB4W2lkeF1cblxubnAucmFuZG9tLnNlZWQoMClcbnNhbXBsZSA9IG5wLmNvbmNhdGVuYXRlKFtucC5yYW5kb20ubm9ybWFsKDAsIDEsIDMwKSwgWzYuMl1dKVxuRywgR19jcml0LCByZWplY3QsIGlkeCwgdmFsID0gZ3J1YmJzX3Rlc3Qoc2FtcGxlKVxucHJpbnQoZlx1MDAyN0cgc3RhdGlzdGljIDoge0c6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdHIGNyaXRpY2FsICA6IHtHX2NyaXQ6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdSZWplY3QgSDAgICA6IHtyZWplY3R9ICAob3V0bGllciB2YWx1ZSA9IHt2YWw6LjNmfSlcdTAwMjcpXG5cbmlmIHJlamVjdDpcbiAgICByZWR1Y2VkID0gbnAuZGVsZXRlKHNhbXBsZSwgaWR4KVxuICAgIEcyLCBHMmMsIHIyLCBfLCBfID0gZ3J1YmJzX3Rlc3QocmVkdWNlZClcbiAgICBwcmludChmXHUwMDI3U2VxdWVudGlhbCDigJQgYWZ0ZXIgcmVtb3ZhbDogRz17RzI6LjRmfSwgR19jcml0PXtHMmM6LjRmfSwgcmVqZWN0PXtyMn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRXh0cmVtZSBWYWx1ZSBUaGVvcnkg4oCUIEJsb2NrIE1heGltYSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXh0cmVtZSBWYWx1ZSBUaGVvcnkgKEVWVCkgbW9kZWxzIHRoZSBkaXN0cmlidXRpb24gb2YgbWF4aW1hIHJhdGhlciB0aGFuIGluZGl2aWR1YWwgb2JzZXJ2YXRpb25zLiBCeSB0aGUgRmlzaGVyLVRpcHBldHQtR25lZGVua28gdGhlb3JlbSwgdGhlIG1heGltdW0gb2YgbiBpLmkuZC4gcmFuZG9tIHZhcmlhYmxlcyBjb252ZXJnZXMgdG8gYSBHZW5lcmFsaXplZCBFeHRyZW1lIFZhbHVlIChHRVYpIGRpc3RyaWJ1dGlvbiB3aXRoIHNoYXBlIHBhcmFtZXRlciDOvjogzr49MCAoR3VtYmVsLCBsaWdodC10YWlsZWQpLCDOvlx1MDAzZTAgKEZyw6ljaGV0LCBoZWF2eS10YWlsZWQpLCDOvlx1MDAzYzAgKFdlaWJ1bGwsIGJvdW5kZWQpLiBGaXQgR0VWIHRvIGJsb2NrIG1heGltYSAoZS5nLiwgYW5udWFsIG1heGltYSkgdG8gY29tcHV0ZSByZXR1cm4gbGV2ZWxzOiB0aGUgVC15ZWFyIHJldHVybiBsZXZlbCBpcyBleGNlZWRlZCB3aXRoIHByb2JhYmlsaXR5IDEvVCBwZXIgeWVhci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBndW1iZWxfciwgZ2VuZXh0cmVtZVxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG5ucC5yYW5kb20uc2VlZCg0MilcbmRhaWx5ID0gbnAucmFuZG9tLm5vcm1hbCgyMCwgNSwgMzY1ICogMzApXG5hbm51YWxfbWF4ID0gbnAuYXJyYXkoW2RhaWx5W2kqMzY1OihpKzEpKjM2NV0ubWF4KCkgZm9yIGkgaW4gcmFuZ2UoMzApXSlcblxubG9jLCBzY2FsZSA9IGd1bWJlbF9yLmZpdChhbm51YWxfbWF4KVxucHJpbnQoZlx1MDAyN0d1bWJlbCBmaXQg4oCUIGxvY2F0aW9uOiB7bG9jOi4yZn0sIHNjYWxlOiB7c2NhbGU6LjJmfVx1MDAyNylcblxuZm9yIHJwIGluIFsyLCA1LCAxMCwgMjUsIDUwXTpcbiAgICBsZXZlbCA9IGd1bWJlbF9yLnBwZigxIC0gMS9ycCwgbG9jPWxvYywgc2NhbGU9c2NhbGUpXG4gICAgcHJpbnQoZlx1MDAyNyAge3JwOjNkfS15ciByZXR1cm4gbGV2ZWw6IHtsZXZlbDouMmZ9XHUwMDI3KVxuXG5zaGFwZSwgbG9jX2csIHNjYWxlX2cgPSBnZW5leHRyZW1lLmZpdChhbm51YWxfbWF4KVxucHJpbnQoZlx1MDAyN0dFViBzaGFwZSB4aSA9IHtzaGFwZTouM2Z9IChHdW1iZWwgaWYgfjAsIEZyZWNoZXQgaWYgXHUwMDNlMClcdTAwMjcpXG5cbnRocmVzaG9sZF81MCA9IGd1bWJlbF9yLnBwZigwLjk4LCBsb2M9bG9jLCBzY2FsZT1zY2FsZSlcbmFub21hbGllcyA9IGFubnVhbF9tYXhbYW5udWFsX21heCBcdTAwM2UgdGhyZXNob2xkXzUwXVxucHJpbnQoZlx1MDAyN0Fub21hbGllcyBhYm92ZSA1MC15ciBsZXZlbCAoe3RocmVzaG9sZF81MDouMmZ9KToge2xlbihhbm9tYWxpZXMpfVx1MDAyNylcblxueCA9IG5wLmxpbnNwYWNlKGFubnVhbF9tYXgubWluKCkgLSAyLCBhbm51YWxfbWF4Lm1heCgpICsgOCwgMjAwKVxucGx0LnBsb3QoeCwgZ3VtYmVsX3IucGRmKHgsIGxvYz1sb2MsIHNjYWxlPXNjYWxlKSwgbGFiZWw9XHUwMDI3R3VtYmVsIGZpdFx1MDAyNylcbnBsdC5oaXN0KGFubnVhbF9tYXgsIGJpbnM9OCwgZGVuc2l0eT1UcnVlLCBhbHBoYT0wLjUsIGxhYmVsPVx1MDAyN0FubnVhbCBtYXhpbWFcdTAwMjcpXG5wbHQuYXh2bGluZSh0aHJlc2hvbGRfNTAsIGNvbG9yPVx1MDAyN3JlZFx1MDAyNywgbGluZXN0eWxlPVx1MDAyNy0tXHUwMDI3LCBsYWJlbD1cdTAwMjc1MC15ciBsZXZlbFx1MDAyNylcbnBsdC5sZWdlbmQoKVxucGx0LnRpdGxlKFx1MDAyN0VWVCDigJQgR3VtYmVsIEZpdCB0byBBbm51YWwgTWF4aW1hXHUwMDI3KVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdldnRfZ3VtYmVsLnBuZ1x1MDAyNywgZHBpPTEwMCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZXRob2QgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJEaXN0cmlidXRpb24iLCJSb2J1c3RuZXNzIiwiTXVsdGl2YXJpYXRlIiwiQ29tcGxleGl0eSIsIkJlc3QgVXNlIENhc2UiXSwicm93cyI6W1siWi1zY29yZSIsIkdhdXNzaWFuIiwiTG93ICjOvCzPgyBub24tcm9idXN0KSIsIk5vIiwiTyhuKSIsIkNsZWFuIEdhdXNzaWFuIGRhdGEsIG5vIG1hc2tpbmcgcmlzayJdLFsiTW9kaWZpZWQgWi1zY29yZSIsIkFwcHJveC4gR2F1c3NpYW4iLCJIaWdoIChNQUQsIG1lZGlhbikiLCJObyIsIk8obiBsb2cgbikiLCJDb250YW1pbmF0ZWQgdW5pdmFyaWF0ZSBkYXRhIl0sWyJJUVIgKFR1a2V5KSIsIk5vbmUgKGZyZWUpIiwiSGlnaCAocXVhcnRpbGUtYmFzZWQpIiwiTm8iLCJPKG4gbG9nIG4pIiwiRXhwbG9yYXRvcnkgYW5hbHlzaXMsIGFueSBkaXN0cmlidXRpb24iXSxbIkdydWJicyIsIkdhdXNzaWFuIChzdHJpY3QpIiwiTG93IiwiTm8iLCJPKG4pIiwiRm9ybWFsIHRlc3QsIHNpbmdsZSBvdXRsaWVyLCBzbWFsbCBuIl0sWyJFVlQgKEdFVikiLCJHRVYgLyBHdW1iZWwiLCJNb2RlcmF0ZSIsIk5vIChleHRlbnNpb25zIGV4aXN0KSIsIk8obikiLCJSYXJlIGV4dHJlbWVzLCByZXR1cm4tbGV2ZWwgZXN0aW1hdGlvbiJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGltaXRhdGlvbnMgYW5kIFByYWN0aWNhbCBHdWlkYW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWxsIG1ldGhvZHMgYWJvdmUgYXJlIHN0cmljdGx5IHVuaXZhcmlhdGU6IHRoZXkgY2Fubm90IGRldGVjdCBjb21iaW5hdGlvbnMgb2YgZmVhdHVyZXMgdGhhdCBhcmUgam9pbnRseSB1bnVzdWFsIChlLmcuLCBoZWlnaHQ9MTkwY20gaXMgbm9ybWFsLCB3ZWlnaHQ9NDBrZyBpcyBub3JtYWwsIGJ1dCB0aGUgY29tYmluYXRpb24gaXMgYW5vbWFsb3VzKS4gRm9yIG11bHRpdmFyaWF0ZSBhbm9tYWx5IGRldGVjdGlvbiB1c2UgTWFoYWxhbm9iaXMgZGlzdGFuY2Ugb3IgSXNvbGF0aW9uIEZvcmVzdC4gWi1zY29yZSBhbmQgR3J1YmJzIHJlcXVpcmUgYXBwcm94aW1hdGUgbm9ybWFsaXR5IOKAlCBhbHdheXMgY2hlY2sgd2l0aCBhIFEtUSBwbG90IG9yIFNoYXBpcm8tV2lsayB0ZXN0IGZpcnN0LiBJUVIgYW5kIG1vZGlmaWVkIFotc2NvcmUgYXJlIHNhZmUgZGVmYXVsdHMgd2hlbiB0aGUgZGlzdHJpYnV0aW9uIGlzIHVua25vd24uIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJNdWx0aXBsZSBUZXN0aW5nIENvcnJlY3Rpb24iLCJjb250ZW50IjoiV2hlbiBmbGFnZ2luZyBhbm9tYWxpZXMgYWNyb3NzIHAgZmVhdHVyZXMgc2ltdWx0YW5lb3VzbHkgd2l0aCDOsT0wLjA1IHBlciB0ZXN0LCB0aGUgZXhwZWN0ZWQgbnVtYmVyIG9mIGZhbHNlIHBvc2l0aXZlcyBpcyAwLjA1wrdwLiBXaXRoIHA9MTAwIGZlYXR1cmVzLCBleHBlY3QgNSBzcHVyaW91cyBhbm9tYWx5IGZsYWdzIHBlciBub3JtYWwgcG9pbnQuIEFwcGx5IEJvbmZlcnJvbmkgY29ycmVjdGlvbiAozrEvcCkgb3IgQmVuamFtaW5pLUhvY2hiZXJnIEZEUiBjb250cm9sIHRvIGxpbWl0IGZhbWlseS13aXNlIGVycm9yIHJhdGUgYWNyb3NzIHZhcmlhYmxlcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlByZWZlciBtb2RpZmllZCBaLXNjb3JlIG92ZXIgc3RhbmRhcmQgWi1zY29yZSB3aGVuZXZlciBjb250YW1pbmF0aW9uIGlzIHBvc3NpYmxlIiwiSVFSIGlzIHRoZSBzYWZlc3QgY2hvaWNlIHdoZW4gdGhlIGRpc3RyaWJ1dGlvbiBpcyB1bmtub3duIG9yIHNrZXdlZCIsIkdydWJicyB0ZXN0IGlzIGFwcHJvcHJpYXRlIGZvciBzbWFsbCwgYXBwcm94aW1hdGVseSBub3JtYWwgc2FtcGxlcyAobiBcdTAwM2MgMTAwKSIsIkVWVCBpcyBlc3NlbnRpYWwgZm9yIG1vZGVsbGluZyBwcm9iYWJpbGl0eSBvZiByYXJlIGV4dHJlbWUgZXZlbnRzIChmbG9vZHMsIG5ldHdvcmsgc3Bpa2VzKSIsIkFsd2F5cyB2aXN1YWxpc2Ugd2l0aCBib3ggcGxvdHMgYW5kIFEtUSBwbG90cyBiZWZvcmUgY2hvb3NpbmcgYSBtZXRob2QiXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJPbmUtc2lkZWQgdnMgdHdvLXNpZGVkIHRlc3RzIG1hdHRlcjogZGV0ZWN0aW5nIG9ubHkgdW51c3VhbGx5IGhpZ2ggdmFsdWVzIChuZXR3b3JrIHRyYWZmaWMsIGVycm9yIHJhdGVzKSB1c2VzIG9uZS1zaWRlZCB0ZXN0cyB3aXRoIHRocmVzaG9sZCB6IFx1MDAzZSAzLiBUd28tc2lkZWQgdGVzdHMgZmxhZyBib3RoIGV4dHJlbWVzIGFuZCBhcmUgYXBwcm9wcmlhdGUgd2hlbiBhbm9tYWxpZXMgY2FuIG9jY3VyIGluIGVpdGhlciBkaXJlY3Rpb24uIFdoZW4gdGVzdGluZyBtdWx0aXBsZSB0aW1lIHBvaW50cyBzZXF1ZW50aWFsbHksIGFwcGx5IGEgY29ycmVjdGlvbiBmb3IgdGVtcG9yYWwgYXV0b2NvcnJlbGF0aW9uIChlLmcuLCB1c2UgYSBDVVNVTSBjaGFydCBpbnN0ZWFkIG9mIGluZGVwZW5kZW50IFotdGVzdHMpLiJ9XQ=="
---
# Statistical Anomaly Detection — Z-Score, IQR, and Grubbs Test

Statistical methods detect anomalies by modelling the expected distribution of normal data and flagging observations in the tails. They are interpretable, fast, and require no training beyond summary statistics. The core tradeoff is the distributional assumption: Z-score assumes Gaussian, IQR is distribution-free but univariate, and extreme value theory targets the behaviour of block maxima. All methods are strictly univariate — they flag individual features, not combinations.

## Z-Score Method

The Z-score standardises each observation relative to the sample mean and standard deviation. Points with |z| > 3 fall more than three standard deviations from the mean; under a Gaussian this encompasses 99.73% of probability mass, so flagged points are rare by construction. However, both μ and σ are non-robust: a single extreme outlier inflates σ and deflates every other Z-score — the masking effect. One-sided tests (z > 3 only) are appropriate when anomalies occur only in the positive direction.

$$z_i = \frac{x_i - \mu}{\sigma}, \quad \text{flag if } |z_i| > 3$$

## Modified Z-Score — MAD-Based Robustness

The modified Z-score replaces μ with the sample median x̃ and σ with MAD = median(|xᵢ − x̃|). The constant 0.6745 makes MAD a consistent estimator of σ under a Gaussian. Both median and MAD have breakdown point 50%: up to half the data can be corrupted without distorting the estimates. Recommended threshold is |Mᵢ| > 3.5. The modified Z-score is the preferred univariate method when the data may be contaminated.

$$M_i = \frac{0.6745(x_i - \tilde{x})}{\operatorname{MAD}}, \quad \operatorname{MAD} = \operatorname{median}(|x_i - \tilde{x}|)$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
data = np.concatenate([np.random.normal(0, 1, 100), [10.0, -8.5, 15.0]])

def zscore_flags(x, threshold=3.0):
    mu, sigma = x.mean(), x.std(ddof=1)
    z = (x - mu) / sigma
    return np.abs(z) > threshold, z

def modified_zscore_flags(x, threshold=3.5):
    med = np.median(x)
    mad = np.median(np.abs(x - med))
    mad = max(mad, 1e-9)
    m = 0.6745 * (x - med) / mad
    return np.abs(m) > threshold, m

flag_z, z_scores   = zscore_flags(data)
flag_mz, mz_scores = modified_zscore_flags(data)
print(f'Z-score:          {flag_z.sum()} anomalies at {np.where(flag_z)[0].tolist()}')
print(f'Modified Z-score: {flag_mz.sum()} anomalies at {np.where(flag_mz)[0].tolist()}')

# Masking: injecting a giant outlier reduces sensitivity of standard Z-score
masked = np.concatenate([data, [100.0]])
flag_masked, _ = zscore_flags(masked)
print(f'After injecting 100.0 — Z-score detects: {flag_masked.sum()} (masking inflates sigma)')
```

## IQR Method — Distribution-Free Bounds

The IQR method sets bounds lower = Q1 − k·IQR and upper = Q3 + k·IQR. Tukey inner fences use k=1.5 (flags ~0.7% of Gaussian data); outer fences use k=3.0 for extreme outliers. The method requires no distributional assumption, is resistant to skewed distributions, and is the standard choice for exploratory data analysis. Its primary limitation is strict univariate scope.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.concatenate([np.random.normal(50, 10, 200), [5.0, -10.0, 110.0, 125.0]])

def iqr_bounds(x, k=1.5):
    Q1, Q3 = np.percentile(x, [25, 75])
    IQR = Q3 - Q1
    return Q1 - k * IQR, Q3 + k * IQR, IQR

lower, upper, iqr = iqr_bounds(data)
flags = (data < lower) | (data > upper)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.boxplot(data, vert=True)
ax1.set_title('Box Plot with IQR Fences')
colors = ['red' if f else 'steelblue' for f in flags]
ax2.scatter(range(len(data)), data, c=colors, alpha=0.6, s=20)
ax2.axhline(lower, color='orange', linestyle='--', label=f'Lower={lower:.1f}')
ax2.axhline(upper, color='orange', linestyle='--', label=f'Upper={upper:.1f}')
ax2.legend()
ax2.set_title(f'IQR Anomalies (k=1.5): {flags.sum()} flagged')
plt.tight_layout()
plt.savefig('iqr_anomalies.png', dpi=100)
print(f'IQR={iqr:.2f}  Bounds=[{lower:.2f}, {upper:.2f}]  Flagged: {flags.sum()}')
```

## Grubbs Test — Formal Hypothesis Testing

The Grubbs test (1969) formally tests H₀: no outliers in a Gaussian sample. Test statistic G = max|xᵢ − x̄|/s is compared against a critical value from the t-distribution at significance α. The sequential Grubbs procedure removes the identified outlier and retests — but each iteration should use a corrected significance level to control family-wise error. Normality should be verified with Shapiro-Wilk before applying.

```python
import numpy as np
from scipy import stats

def grubbs_stat(x):
    return np.max(np.abs(x - x.mean())) / x.std(ddof=1)

def grubbs_critical(n, alpha=0.05):
    # Two-sided critical value via t-distribution (Grubbs 1969)
    p = alpha / (2 * n)
    t = stats.t.ppf(1 - p, df=n - 2)
    return ((n - 1) / np.sqrt(n)) * np.sqrt(t**2 / (n - 2 + t**2))

def grubbs_test(x, alpha=0.05):
    n = len(x)
    G = grubbs_stat(x)
    G_crit = grubbs_critical(n, alpha)
    idx = int(np.argmax(np.abs(x - x.mean())))
    return G, G_crit, G > G_crit, idx, x[idx]

np.random.seed(0)
sample = np.concatenate([np.random.normal(0, 1, 30), [6.2]])
G, G_crit, reject, idx, val = grubbs_test(sample)
print(f'G statistic : {G:.4f}')
print(f'G critical  : {G_crit:.4f}')
print(f'Reject H0   : {reject}  (outlier value = {val:.3f})')

if reject:
    reduced = np.delete(sample, idx)
    G2, G2c, r2, _, _ = grubbs_test(reduced)
    print(f'Sequential — after removal: G={G2:.4f}, G_crit={G2c:.4f}, reject={r2}')
```

## Extreme Value Theory — Block Maxima

Extreme Value Theory (EVT) models the distribution of maxima rather than individual observations. By the Fisher-Tippett-Gnedenko theorem, the maximum of n i.i.d. random variables converges to a Generalized Extreme Value (GEV) distribution with shape parameter ξ: ξ=0 (Gumbel, light-tailed), ξ>0 (Fréchet, heavy-tailed), ξ<0 (Weibull, bounded). Fit GEV to block maxima (e.g., annual maxima) to compute return levels: the T-year return level is exceeded with probability 1/T per year.

```python
import numpy as np
from scipy.stats import gumbel_r, genextreme
import matplotlib.pyplot as plt

np.random.seed(42)
daily = np.random.normal(20, 5, 365 * 30)
annual_max = np.array([daily[i*365:(i+1)*365].max() for i in range(30)])

loc, scale = gumbel_r.fit(annual_max)
print(f'Gumbel fit — location: {loc:.2f}, scale: {scale:.2f}')

for rp in [2, 5, 10, 25, 50]:
    level = gumbel_r.ppf(1 - 1/rp, loc=loc, scale=scale)
    print(f'  {rp:3d}-yr return level: {level:.2f}')

shape, loc_g, scale_g = genextreme.fit(annual_max)
print(f'GEV shape xi = {shape:.3f} (Gumbel if ~0, Frechet if >0)')

threshold_50 = gumbel_r.ppf(0.98, loc=loc, scale=scale)
anomalies = annual_max[annual_max > threshold_50]
print(f'Anomalies above 50-yr level ({threshold_50:.2f}): {len(anomalies)}')

x = np.linspace(annual_max.min() - 2, annual_max.max() + 8, 200)
plt.plot(x, gumbel_r.pdf(x, loc=loc, scale=scale), label='Gumbel fit')
plt.hist(annual_max, bins=8, density=True, alpha=0.5, label='Annual maxima')
plt.axvline(threshold_50, color='red', linestyle='--', label='50-yr level')
plt.legend()
plt.title('EVT — Gumbel Fit to Annual Maxima')
plt.tight_layout()
plt.savefig('evt_gumbel.png', dpi=100)
```

## Method Comparison

| Method | Distribution | Robustness | Multivariate | Complexity | Best Use Case |
| --- | --- | --- | --- | --- | --- |
| Z-score | Gaussian | Low (μ,σ non-robust) | No | O(n) | Clean Gaussian data, no masking risk |
| Modified Z-score | Approx. Gaussian | High (MAD, median) | No | O(n log n) | Contaminated univariate data |
| IQR (Tukey) | None (free) | High (quartile-based) | No | O(n log n) | Exploratory analysis, any distribution |
| Grubbs | Gaussian (strict) | Low | No | O(n) | Formal test, single outlier, small n |
| EVT (GEV) | GEV / Gumbel | Moderate | No (extensions exist) | O(n) | Rare extremes, return-level estimation |

## Limitations and Practical Guidance

All methods above are strictly univariate: they cannot detect combinations of features that are jointly unusual (e.g., height=190cm is normal, weight=40kg is normal, but the combination is anomalous). For multivariate anomaly detection use Mahalanobis distance or Isolation Forest. Z-score and Grubbs require approximate normality — always check with a Q-Q plot or Shapiro-Wilk test first. IQR and modified Z-score are safe defaults when the distribution is unknown.

> **Multiple Testing Correction**: When flagging anomalies across p features simultaneously with α=0.05 per test, the expected number of false positives is 0.05·p. With p=100 features, expect 5 spurious anomaly flags per normal point. Apply Bonferroni correction (α/p) or Benjamini-Hochberg FDR control to limit family-wise error rate across variables.

- Prefer modified Z-score over standard Z-score whenever contamination is possible
- IQR is the safest choice when the distribution is unknown or skewed
- Grubbs test is appropriate for small, approximately normal samples (n < 100)
- EVT is essential for modelling probability of rare extreme events (floods, network spikes)
- Always visualise with box plots and Q-Q plots before choosing a method

One-sided vs two-sided tests matter: detecting only unusually high values (network traffic, error rates) uses one-sided tests with threshold z > 3. Two-sided tests flag both extremes and are appropriate when anomalies can occur in either direction. When testing multiple time points sequentially, apply a correction for temporal autocorrelation (e.g., use a CUSUM chart instead of independent Z-tests).

