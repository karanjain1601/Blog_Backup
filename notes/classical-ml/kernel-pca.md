---
title: "Kernel PCA — Nonlinear Dimensionality Reduction"
slug: "kernel-pca"
description: "How kernel PCA implicitly maps data to a high-dimensional feature space, centers the kernel matrix, and projects onto nonlinear principal components — covering RBF, polynomial kernels, Swiss roll unfolding, and the Nyström approximation."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgUENBIGZpbmRzIGxpbmVhciBkaXJlY3Rpb25zIG9mIG1heGltdW0gdmFyaWFuY2UuIFdoZW4gZGF0YSBsaXZlcyBvbiBhIG5vbmxpbmVhciBtYW5pZm9sZCDigJQgYSBTd2lzcyByb2xsLCBjb25jZW50cmljIGNpcmNsZXMsIG9yIGFuIFMtY3VydmUg4oCUIGxpbmVhciBQQ0EgZmFpbHMgdG8gc2VwYXJhdGUgY2xhc3NlcyB0aGF0IGFyZSBsaW5lYXJseSBlbnRhbmdsZWQuIEtlcm5lbCBQQ0EgZXh0ZW5kcyBQQ0EgdG8gbm9ubGluZWFyIHN0cnVjdHVyZSBieSBpbXBsaWNpdGx5IG1hcHBpbmcgZGF0YSB0byBhIGhpZ2gtZGltZW5zaW9uYWwgKHBvc3NpYmx5IGluZmluaXRlLWRpbWVuc2lvbmFsKSBmZWF0dXJlIHNwYWNlIHZpYSB0aGUga2VybmVsIHRyaWNrLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBLZXJuZWwgVHJpY2sifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikluc3RlYWQgb2YgZXhwbGljaXRseSBjb21wdXRpbmcgdGhlIGZlYXR1cmUgbWFwIM+GKHgpLCBrZXJuZWwgUENBIHdvcmtzIHdpdGggdGhlIGtlcm5lbCBtYXRyaXggS+G1ouKxvCA9IGsoeOG1oiwgeOKxvCkgPSDPhih44bWiKeG1gM+GKHjisbwpLiBQQ0EgaW4gZmVhdHVyZSBzcGFjZSByZXF1aXJlcyBjb21wdXRpbmcgdGhlIGNvdmFyaWFuY2UgzqNfz4YgPSAoMS9uKc6jz4YoeOG1oinPhih44bWiKeG1gCBhbmQgaXRzIGVpZ2VudmVjdG9ycy4gSXQgdHVybnMgb3V0IHRoZSBlaWdlbnZlY3RvcnMgY2FuIGJlIGV4cHJlc3NlZCBhcyBsaW5lYXIgY29tYmluYXRpb25zIG9mIHRoZSBmZWF0dXJlIG1hcHMsIGFuZCB0aGUgcHJvamVjdGlvbiBzY29yZXMgYXJlIGdpdmVuIGRpcmVjdGx5IGJ5IHRoZSBrZXJuZWwgbWF0cml4IOKAlCBubyBleHBsaWNpdCDPhiBuZWVkZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2VudGVyaW5nIGluIEZlYXR1cmUgU3BhY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrZXJuZWwgbWF0cml4IG11c3QgYmUgY2VudGVyZWQgaW4gZmVhdHVyZSBzcGFjZSAobm90IGluIGlucHV0IHNwYWNlKS4gVGhlIGNlbnRlcmluZyBvcGVyYXRpb24gaXM6IEvMgyA9IEsgLSAx4oKZSyAtIEsx4oKZICsgMeKCmUsx4oKZLCB3aGVyZSAx4oKZIGlzIHRoZSBuw5duIG1hdHJpeCB3aXRoIGFsbCBlbnRyaWVzIDEvbi4gRWlnZW5kZWNvbXBvc2luZyBLzIMgPSBRzptR4bWAIGdpdmVzIHNjb3JlczogdGhlIHByb2plY3Rpb24gb250byB0aGUgcC10aCBjb21wb25lbnQgaXMgS8yDzrHigpov4oiazrvigposIHdoZXJlIM6x4oKaID0gceKCmi/iiJrOu+KCmiAobm9ybWFsaXNlZCBlaWdlbnZlY3RvcikuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX21vb25zXG5cbiMgR2VuZXJhdGUgbm9ubGluZWFyIGRhdGFcblgsIHkgPSBtYWtlX21vb25zKG5fc2FtcGxlcz0yMDAsIG5vaXNlPTAuMDUsIHJhbmRvbV9zdGF0ZT00Milcbm4gPSBsZW4oWClcblxuIyBSQkYga2VybmVsOiBLW2ksal0gPSBleHAoLWdhbW1hICogfHx4X2kgLSB4X2p8fF4yKVxuZGVmIHJiZl9rZXJuZWwoWCwgZ2FtbWE9MS4wKTpcbiAgICBzcV9kaXN0cyA9IChucC5zdW0oWCoqMiwgYXhpcz0xLCBrZWVwZGltcz1UcnVlKVxuICAgICAgICAgICAgICAgICsgbnAuc3VtKFgqKjIsIGF4aXM9MSlcbiAgICAgICAgICAgICAgICAtIDIgKiBYIEAgWC5UKVxuICAgIHJldHVybiBucC5leHAoLWdhbW1hICogc3FfZGlzdHMpXG5cbksgPSByYmZfa2VybmVsKFgsIGdhbW1hPTEuMClcblxuIyBDZW50ZXIgaW4gZmVhdHVyZSBzcGFjZVxub25lX24gPSBucC5vbmVzKChuLCBuKSkgLyBuXG5LX2MgPSBLIC0gb25lX24gQCBLIC0gSyBAIG9uZV9uICsgb25lX24gQCBLIEAgb25lX25cblxuIyBFaWdlbmRlY29tcG9zZSBjZW50ZXJlZCBrZXJuZWxcbnZhbHMsIHZlY3MgPSBucC5saW5hbGcuZWlnaChLX2MpXG5pZHggPSBucC5hcmdzb3J0KHZhbHMpWzo6LTFdICAjIGRlc2NlbmRpbmdcbnZhbHMsIHZlY3MgPSB2YWxzW2lkeF0sIHZlY3NbOiwgaWR4XVxuXG4jIFByb2plY3Rpb24gb250byB0b3AgMiBrZXJuZWwgUENzXG5rX2NvbXAgPSAyXG5YX2twY2EgPSB2ZWNzWzosIDprX2NvbXBdICogbnAuc3FydChucC5tYXhpbXVtKHZhbHNbOmtfY29tcF0sIDApKVxucHJpbnQoZlx1MDAyN2tQQ0EgcHJvamVjdGlvbiBzaGFwZToge1hfa3BjYS5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3VG9wIGVpZ2VudmFsdWVzOiB7dmFsc1s6NV0ucm91bmQoMil9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbW1vbiBLZXJuZWxzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJSQkYgLyBHYXVzc2lhbjogayh4LHopID0gZXhwKC3Os+KAlngteuKAlsKyKSDigJQgdW5pdmVyc2FsIGFwcHJveGltYXRvciwgbW9zdCBjb21tb25seSB1c2VkIiwiUG9seW5vbWlhbDogayh4LHopID0gKM6zeOG1gHogKyByKeG1iCDigJQgY2FwdHVyZXMgZmVhdHVyZSBpbnRlcmFjdGlvbnMgdXAgdG8gZGVncmVlIGQiLCJTaWdtb2lkOiBrKHgseikgPSB0YW5oKM6zeOG1gHogKyByKSDigJQgbWltaWNzIG5ldXJhbCBuZXR3b3JrIGFjdGl2YXRpb25zIiwiTGluZWFyOiBrKHgseikgPSB44bWAeiDigJQgZXF1aXZhbGVudCB0byBzdGFuZGFyZCBQQ0EgKHVzZWZ1bCBhcyBhIGJhc2VsaW5lKSIsIkxhcGxhY2lhbjogayh4LHopID0gZXhwKC3Os+KAlngteuKAlikg4oCUIGhlYXZpZXIgdGFpbCB0aGFuIFJCRiwgcm9idXN0IHRvIG91dGxpZXJzIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6InNrbGVhcm4gS2VybmVsUENBOiBMaW5lYXIgdnMgUkJGIHZzIFBvbHlub21pYWwifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfbW9vbnMsIG1ha2VfY2lyY2xlc1xuZnJvbSBza2xlYXJuLmRlY29tcG9zaXRpb24gaW1wb3J0IEtlcm5lbFBDQSwgUENBXG5cbmRhdGFzZXRzID0gW1xuICAgIChcdTAwMjdNb29uc1x1MDAyNywgKm1ha2VfbW9vbnMobl9zYW1wbGVzPTMwMCwgbm9pc2U9MC4wNSwgcmFuZG9tX3N0YXRlPTQyKSksXG4gICAgKFx1MDAyN0NpcmNsZXNcdTAwMjcsICptYWtlX2NpcmNsZXMobl9zYW1wbGVzPTMwMCwgbm9pc2U9MC4wNSwgZmFjdG9yPTAuNCwgcmFuZG9tX3N0YXRlPTQyKSlcbl1cbmtlcm5lbHMgPSBbXHUwMDI3bGluZWFyXHUwMDI3LCBcdTAwMjdyYmZcdTAwMjcsIFx1MDAyN3BvbHlcdTAwMjddXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMobGVuKGRhdGFzZXRzKSwgbGVuKGtlcm5lbHMpICsgMSwgZmlnc2l6ZT0oMTYsIDgpKVxuXG5mb3Igcm93LCAobmFtZSwgWCwgeSkgaW4gZW51bWVyYXRlKGRhdGFzZXRzKTpcbiAgICBYX3BjYSA9IFBDQShuX2NvbXBvbmVudHM9MikuZml0X3RyYW5zZm9ybShYKVxuICAgIGF4ZXNbcm93LCAwXS5zY2F0dGVyKFhfcGNhWzosIDBdLCBYX3BjYVs6LCAxXSwgYz15LCBjbWFwPVx1MDAyN2J3clx1MDAyNywgcz0xMClcbiAgICBheGVzW3JvdywgMF0uc2V0X3RpdGxlKGZcdTAwMjd7bmFtZX06IExpbmVhciBQQ0FcdTAwMjcpXG5cbiAgICBmb3IgY29sLCBrZXJuZWwgaW4gZW51bWVyYXRlKGtlcm5lbHMpOlxuICAgICAgICBrcGNhID0gS2VybmVsUENBKG5fY29tcG9uZW50cz0yLCBrZXJuZWw9a2VybmVsLCBnYW1tYT01LjAsIHJhbmRvbV9zdGF0ZT00MilcbiAgICAgICAgWF9rID0ga3BjYS5maXRfdHJhbnNmb3JtKFgpXG4gICAgICAgIGF4ZXNbcm93LCBjb2wgKyAxXS5zY2F0dGVyKFhfa1s6LCAwXSwgWF9rWzosIDFdLCBjPXksIGNtYXA9XHUwMDI3YndyXHUwMDI3LCBzPTEwKVxuICAgICAgICBheGVzW3JvdywgY29sICsgMV0uc2V0X3RpdGxlKGZcdTAwMjd7bmFtZX06IHtrZXJuZWx9XHUwMDI3KVxuXG5wbHQuc3VwdGl0bGUoXHUwMDI3S2VybmVsIFBDQSBvbiBOb25saW5lYXIgRGF0YXNldHNcdTAwMjcsIGZvbnRzaXplPTEzKVxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2hvdygpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6Iktlcm5lbCBTZWxlY3Rpb24iLCJjb250ZW50IjoiU3RhcnQgd2l0aCB0aGUgUkJGIGtlcm5lbCBhbmQgdHVuZSDOsyB2aWEgY3Jvc3MtdmFsaWRhdGlvbiBvciByZWNvbnN0cnVjdGlvbiBlcnJvciBvbiBoZWxkLW91dCBkYXRhLiBQb2x5bm9taWFsIGtlcm5lbHMgd29yayB3ZWxsIHdoZW4geW91IGtub3cgZmVhdHVyZXMgaW50ZXJhY3QgbXVsdGlwbGljYXRpdmVseS4gVGhlIGxpbmVhciBrZXJuZWwgc2VydmVzIGFzIGEgc2FuaXR5IGNoZWNrIOKAlCBpZiBpdCBwZXJmb3JtcyBhcyB3ZWxsIGFzIFJCRiwgeW91ciBkYXRhIGlzIGFwcHJveGltYXRlbHkgbGluZWFybHkgc2VwYXJhYmxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVuZm9sZGluZyBOb25saW5lYXIgTWFuaWZvbGRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGNsYXNzaWMgZGVtb25zdHJhdGlvbiBpcyB0aGUgU3dpc3Mgcm9sbDogYSAyRCBzaGVldCByb2xsZWQgdXAgaW4gM0Qgc3BhY2UuIExpbmVhciBQQ0EgcHJvamVjdHMgaXQgZmxhdCBidXQgcHJlc2VydmVzIHRoZSByb2xsZWQgc3RydWN0dXJlLiBLZXJuZWwgUENBIHdpdGggYW4gYXBwcm9wcmlhdGUgUkJGIGJhbmR3aWR0aCBjYW4gXHUwMDI3dW5yb2xsXHUwMDI3IHRoZSBtYW5pZm9sZCwgcmVjb3ZlcmluZyB0aGUgb3JpZ2luYWwgMkQgc2hlZXQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX3N3aXNzX3JvbGxcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBLZXJuZWxQQ0EsIFBDQVxuXG5YLCBjb2xvciA9IG1ha2Vfc3dpc3Nfcm9sbChuX3NhbXBsZXM9MTAwMCwgbm9pc2U9MC4xLCByYW5kb21fc3RhdGU9NDIpXG5cbmZpZyA9IHBsdC5maWd1cmUoZmlnc2l6ZT0oMTQsIDQpKVxuXG4jIDNEIG9yaWdpbmFsXG5heCA9IGZpZy5hZGRfc3VicGxvdCgxMzEsIHByb2plY3Rpb249XHUwMDI3M2RcdTAwMjcpXG5heC5zY2F0dGVyKFhbOiwgMF0sIFhbOiwgMV0sIFhbOiwgMl0sIGM9Y29sb3IsIGNtYXA9XHUwMDI3U3BlY3RyYWxcdTAwMjcsIHM9NSlcbmF4LnNldF90aXRsZShcdTAwMjdTd2lzcyBSb2xsICgzRClcdTAwMjcpXG5cbiMgU3RhbmRhcmQgUENBIOKAlCBmYWlscyB0byB1bnJvbGxcblhfcGNhID0gUENBKG5fY29tcG9uZW50cz0yKS5maXRfdHJhbnNmb3JtKFgpXG5heDIgPSBmaWcuYWRkX3N1YnBsb3QoMTMyKVxuYXgyLnNjYXR0ZXIoWF9wY2FbOiwgMF0sIFhfcGNhWzosIDFdLCBjPWNvbG9yLCBjbWFwPVx1MDAyN1NwZWN0cmFsXHUwMDI3LCBzPTUpXG5heDIuc2V0X3RpdGxlKFx1MDAyN1BDQSAyRCDigJQgZmFpbHNcdTAwMjcpXG5cbiMgS2VybmVsIFBDQSB3aXRoIFJCRiDigJQgdW5yb2xscyB0aGUgbWFuaWZvbGRcbmtwY2EgPSBLZXJuZWxQQ0Eobl9jb21wb25lbnRzPTIsIGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTAuMDQsXG4gICAgICAgICAgICAgICAgICByYW5kb21fc3RhdGU9NDIsIGZpdF9pbnZlcnNlX3RyYW5zZm9ybT1UcnVlKVxuWF9rcGNhID0ga3BjYS5maXRfdHJhbnNmb3JtKFgpXG5heDMgPSBmaWcuYWRkX3N1YnBsb3QoMTMzKVxuYXgzLnNjYXR0ZXIoWF9rcGNhWzosIDBdLCBYX2twY2FbOiwgMV0sIGM9Y29sb3IsIGNtYXA9XHUwMDI3U3BlY3RyYWxcdTAwMjcsIHM9NSlcbmF4My5zZXRfdGl0bGUoXHUwMDI3S2VybmVsIFBDQSDigJQgdW5yb2xsZWRcdTAwMjcpXG5cbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNob3coKVxucHJpbnQoZlx1MDAyN2tQQ0Egb3V0cHV0IHNoYXBlOiB7WF9rcGNhLnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsYWJpbGl0eSBhbmQgdGhlIE55c3Ryw7ZtIEFwcHJveGltYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbXB1dGluZyB0aGUgZnVsbCBrZXJuZWwgbWF0cml4IGNvc3RzIE8obsKyZCkgbWVtb3J5IGFuZCBPKG7CsykgZm9yIHRoZSBlaWdlbmRlY29tcG9zaXRpb24uIEZvciBuPTEwLDAwMCB0aGF0IGlzIDEwME0gZW50cmllcyDigJQgZmVhc2libGUuIEZvciBuPTEwMCwwMDAgaXQgYmVjb21lcyBpbXByYWN0aWNhbC4gVGhlIE55c3Ryw7ZtIGFwcHJveGltYXRpb24gc2VsZWN0cyBtIOKJqiBuIGxhbmRtYXJrIHBvaW50cywgY29tcHV0ZXMgYSByYW5rLW0gYXBwcm94aW1hdGlvbiBLIOKJiCBLX25tIEtfbW3igbvCuSBLX21uLCBhbmQgYXBwbGllcyBQQ0Egb24gdGhlIHJlc3VsdGluZyBtLWRpbWVuc2lvbmFsIGZlYXR1cmUgbWFwIOKAlCByZWR1Y2luZyBjb3N0IHRvIE8obm1kKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5rZXJuZWxfYXBwcm94aW1hdGlvbiBpbXBvcnQgTnlzdHJvZW1cbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBQQ0FcbmZyb20gc2tsZWFybi5waXBlbGluZSBpbXBvcnQgUGlwZWxpbmVcbmZyb20gc2tsZWFybi5zdm0gaW1wb3J0IExpbmVhclNWQ1xuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgY3Jvc3NfdmFsX3Njb3JlXG5pbXBvcnQgdGltZVxuXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihuX3NhbXBsZXM9MTAwMDAsIG5fZmVhdHVyZXM9NTAsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9pbmZvcm1hdGl2ZT0yMCwgcmFuZG9tX3N0YXRlPTQyKVxuXG4jIE55c3Ryw7ZtOiBtPTMwMCBsYW5kbWFya3MgYXBwcm94aW1hdGUgdGhlIGZ1bGwgUkJGIGtlcm5lbFxubSA9IDMwMFxubnlzdHJvbSA9IE55c3Ryb2VtKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTAuMDEsIG5fY29tcG9uZW50cz1tLCByYW5kb21fc3RhdGU9NDIpXG5cbnQwID0gdGltZS50aW1lKClcblhfYXBwcm94ID0gbnlzdHJvbS5maXRfdHJhbnNmb3JtKFgpXG5wcmludChmXHUwMDI3TnlzdHJvZW0gdGltZToge3RpbWUudGltZSgpIC0gdDA6LjJmfXMsIHNoYXBlOiB7WF9hcHByb3guc2hhcGV9XHUwMDI3KVxuXG4jIFBDQSBvbiB0aGUgYXBwcm94aW1hdGUgZmVhdHVyZSBtYXBcbnBjYSA9IFBDQShuX2NvbXBvbmVudHM9NTApXG5YX2ZpbmFsID0gcGNhLmZpdF90cmFuc2Zvcm0oWF9hcHByb3gpXG5wcmludChmXHUwMDI3RXhwbGFpbmVkIHZhciAoTnlzdHJvZW0rUENBKToge3BjYS5leHBsYWluZWRfdmFyaWFuY2VfcmF0aW9fLnN1bSgpOi4zZn1cdTAwMjcpXG5cbiMgRW5kLXRvLWVuZCBwaXBlbGluZSBmb3IgY2xhc3NpZmljYXRpb25cbnBpcGUgPSBQaXBlbGluZShbXG4gICAgKFx1MDAyN255c3Ryb21cdTAwMjcsIE55c3Ryb2VtKGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPTAuMDEsIG5fY29tcG9uZW50cz0yMDAsIHJhbmRvbV9zdGF0ZT00MikpLFxuICAgIChcdTAwMjdjbGZcdTAwMjcsIExpbmVhclNWQyhtYXhfaXRlcj0xMDAwLCByYW5kb21fc3RhdGU9NDIpKVxuXSlcbnNjb3JlcyA9IGNyb3NzX3ZhbF9zY29yZShwaXBlLCBYLCB5LCBjdj0zLCBzY29yaW5nPVx1MDAyN2FjY3VyYWN5XHUwMDI3KVxucHJpbnQoZlx1MDAyN055c3Ryb2VtK0xpbmVhclNWQyBhY2N1cmFjeToge3Njb3Jlcy5tZWFuKCk6LjNmfSArLy0ge3Njb3Jlcy5zdGQoKTouM2Z9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikh5cGVycGFyYW1ldGVyIFR1bmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIHRoZSBSQkYga2VybmVsLCDOsyA9IDEvKDLPg8KyKSBjb250cm9scyB0aGUgcmFkaXVzIG9mIGluZmx1ZW5jZSBvZiBlYWNoIHRyYWluaW5nIHBvaW50LiBTbWFsbCDOsyDihpIgd2lkZSBHYXVzc2lhbiwgc21vb3RoIGJvdW5kYXJpZXM7IGxhcmdlIM6zIOKGkiB0aWdodCBpbmZsdWVuY2UsIHJpc2sgb2Ygb3ZlcmZpdHRpbmcuIEEgcHJhY3RpY2FsIHN0YXJ0aW5nIHBvaW50OiDOsyA9IDEvZF9mZWF0dXJlcyAodGhlIGRlZmF1bHQgaW4gc2tsZWFybikuIEZvciBwb2x5bm9taWFsIGtlcm5lbHMsIGRlZ3JlZSBkPTIgb3IgZD0zIHdpdGggY29lZjA9MSBpcyBhIGNvbW1vbiBjaG9pY2UuIFR1bmUgzrMgdmlhIGNyb3NzLXZhbGlkYXRlZCByZWNvbnN0cnVjdGlvbiBlcnJvciBvciBkb3duc3RyZWFtIGNsYXNzaWZpY2F0aW9uIGFjY3VyYWN5LCBub3QgYnkgdmlzdWFsIGluc3BlY3Rpb24gb2YgdGhlIGVtYmVkZGluZyBhbG9uZS4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiUHJvcGVydHkiLCJQQ0EiLCJLZXJuZWwgUENBIiwidC1TTkUiLCJVTUFQIl0sInJvd3MiOltbIkxpbmVhciIsIlllcyIsIk5vIChub25saW5lYXIpIiwiTm8iLCJObyJdLFsiUHJlc2VydmVzIGdsb2JhbCBzdHJ1Y3R1cmUiLCJZZXMiLCJQYXJ0aWFsIiwiTm8iLCJCZXR0ZXIgdGhhbiB0LVNORSJdLFsiU2NhbGFibGUgdG8gbGFyZ2UgbiIsIlllcyAoVHJ1bmNhdGVkU1ZEKSIsIk5vIChPKG7CsykpIiwiTm8gKE8obsKyKSkiLCJZZXMgKE8obl4xLjE0KSkiXSxbIkRldGVybWluaXN0aWMiLCJZZXMiLCJZZXMiLCJObyIsIlllcyAoZml4ZWQgc2VlZCkiXSxbIk5ldyBwb2ludCBwcm9qZWN0aW9uIiwiWWVzIiwiQXBwcm94IChOeXN0cm9lbSkiLCJObyIsIlllcyJdXX0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS2VybmVsIFBDQSBpcyB0aGUgcHJpbmNpcGxlZCBleHRlbnNpb24gb2YgUENBIHRvIG5vbmxpbmVhciBkYXRhLiBJdHMga2V5IGxpbWl0YXRpb24gaXMgY29tcHV0YXRpb25hbCBjb3N0OiBPKG7CsikgbWVtb3J5IGFuZCBPKG7CsykgZWlnZW5kZWNvbXBvc2l0aW9uLiBGb3IgbGFyZ2UgZGF0YXNldHMsIHRoZSBOeXN0csO2bSBhcHByb3hpbWF0aW9uIG9yIFVNQVAgKHdoaWNoIGhhcyBiZXR0ZXIgc2NhbGFiaWxpdHkpIGFyZSBtb3JlIHByYWN0aWNhbCBjaG9pY2VzLiBXaGVuIHRoZSBkYXRhIHN0cnVjdHVyZSBpcyB3ZWxsLXVuZGVyc3Rvb2QgYW5kIGEgc3BlY2lmaWMga2VybmVsIGNhcHR1cmVzIGl0LCBLZXJuZWwgUENBIHByb3ZpZGVzIGNsZWFuZXIgdGhlb3JldGljYWwgZ3VhcmFudGVlcyB0aGFuIG1hbmlmb2xkIG1ldGhvZHMgbGlrZSB0LVNORSBvciBVTUFQLiJ9XQ=="
---
# Kernel PCA — Nonlinear Dimensionality Reduction

Standard PCA finds linear directions of maximum variance. When data lives on a nonlinear manifold — a Swiss roll, concentric circles, or an S-curve — linear PCA fails to separate classes that are linearly entangled. Kernel PCA extends PCA to nonlinear structure by implicitly mapping data to a high-dimensional (possibly infinite-dimensional) feature space via the kernel trick.

## The Kernel Trick

Instead of explicitly computing the feature map φ(x), kernel PCA works with the kernel matrix Kᵢⱼ = k(xᵢ, xⱼ) = φ(xᵢ)ᵀφ(xⱼ). PCA in feature space requires computing the covariance Σ_φ = (1/n)Σφ(xᵢ)φ(xᵢ)ᵀ and its eigenvectors. It turns out the eigenvectors can be expressed as linear combinations of the feature maps, and the projection scores are given directly by the kernel matrix — no explicit φ needed.

## Centering in Feature Space

The kernel matrix must be centered in feature space (not in input space). The centering operation is: K̃ = K - 1ₙK - K1ₙ + 1ₙK1ₙ, where 1ₙ is the n×n matrix with all entries 1/n. Eigendecomposing K̃ = QΛQᵀ gives scores: the projection onto the p-th component is K̃αₚ/√λₚ, where αₚ = qₚ/√λₚ (normalised eigenvector).

```python
import numpy as np
from sklearn.datasets import make_moons

# Generate nonlinear data
X, y = make_moons(n_samples=200, noise=0.05, random_state=42)
n = len(X)

# RBF kernel: K[i,j] = exp(-gamma * ||x_i - x_j||^2)
def rbf_kernel(X, gamma=1.0):
    sq_dists = (np.sum(X**2, axis=1, keepdims=True)
                + np.sum(X**2, axis=1)
                - 2 * X @ X.T)
    return np.exp(-gamma * sq_dists)

K = rbf_kernel(X, gamma=1.0)

# Center in feature space
one_n = np.ones((n, n)) / n
K_c = K - one_n @ K - K @ one_n + one_n @ K @ one_n

# Eigendecompose centered kernel
vals, vecs = np.linalg.eigh(K_c)
idx = np.argsort(vals)[::-1]  # descending
vals, vecs = vals[idx], vecs[:, idx]

# Projection onto top 2 kernel PCs
k_comp = 2
X_kpca = vecs[:, :k_comp] * np.sqrt(np.maximum(vals[:k_comp], 0))
print(f'kPCA projection shape: {X_kpca.shape}')
print(f'Top eigenvalues: {vals[:5].round(2)}')
```

## Common Kernels

- RBF / Gaussian: k(x,z) = exp(-γ‖x-z‖²) — universal approximator, most commonly used
- Polynomial: k(x,z) = (γxᵀz + r)ᵈ — captures feature interactions up to degree d
- Sigmoid: k(x,z) = tanh(γxᵀz + r) — mimics neural network activations
- Linear: k(x,z) = xᵀz — equivalent to standard PCA (useful as a baseline)
- Laplacian: k(x,z) = exp(-γ‖x-z‖) — heavier tail than RBF, robust to outliers

## sklearn KernelPCA: Linear vs RBF vs Polynomial

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles
from sklearn.decomposition import KernelPCA, PCA

datasets = [
    ('Moons', *make_moons(n_samples=300, noise=0.05, random_state=42)),
    ('Circles', *make_circles(n_samples=300, noise=0.05, factor=0.4, random_state=42))
]
kernels = ['linear', 'rbf', 'poly']
fig, axes = plt.subplots(len(datasets), len(kernels) + 1, figsize=(16, 8))

for row, (name, X, y) in enumerate(datasets):
    X_pca = PCA(n_components=2).fit_transform(X)
    axes[row, 0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='bwr', s=10)
    axes[row, 0].set_title(f'{name}: Linear PCA')

    for col, kernel in enumerate(kernels):
        kpca = KernelPCA(n_components=2, kernel=kernel, gamma=5.0, random_state=42)
        X_k = kpca.fit_transform(X)
        axes[row, col + 1].scatter(X_k[:, 0], X_k[:, 1], c=y, cmap='bwr', s=10)
        axes[row, col + 1].set_title(f'{name}: {kernel}')

plt.suptitle('Kernel PCA on Nonlinear Datasets', fontsize=13)
plt.tight_layout()
plt.show()
```

> **Kernel Selection**: Start with the RBF kernel and tune γ via cross-validation or reconstruction error on held-out data. Polynomial kernels work well when you know features interact multiplicatively. The linear kernel serves as a sanity check — if it performs as well as RBF, your data is approximately linearly separable.

## Unfolding Nonlinear Manifolds

A classic demonstration is the Swiss roll: a 2D sheet rolled up in 3D space. Linear PCA projects it flat but preserves the rolled structure. Kernel PCA with an appropriate RBF bandwidth can 'unroll' the manifold, recovering the original 2D sheet.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_swiss_roll
from sklearn.decomposition import KernelPCA, PCA

X, color = make_swiss_roll(n_samples=1000, noise=0.1, random_state=42)

fig = plt.figure(figsize=(14, 4))

# 3D original
ax = fig.add_subplot(131, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap='Spectral', s=5)
ax.set_title('Swiss Roll (3D)')

# Standard PCA — fails to unroll
X_pca = PCA(n_components=2).fit_transform(X)
ax2 = fig.add_subplot(132)
ax2.scatter(X_pca[:, 0], X_pca[:, 1], c=color, cmap='Spectral', s=5)
ax2.set_title('PCA 2D — fails')

# Kernel PCA with RBF — unrolls the manifold
kpca = KernelPCA(n_components=2, kernel='rbf', gamma=0.04,
                  random_state=42, fit_inverse_transform=True)
X_kpca = kpca.fit_transform(X)
ax3 = fig.add_subplot(133)
ax3.scatter(X_kpca[:, 0], X_kpca[:, 1], c=color, cmap='Spectral', s=5)
ax3.set_title('Kernel PCA — unrolled')

plt.tight_layout()
plt.show()
print(f'kPCA output shape: {X_kpca.shape}')
```

## Scalability and the Nyström Approximation

Computing the full kernel matrix costs O(n²d) memory and O(n³) for the eigendecomposition. For n=10,000 that is 100M entries — feasible. For n=100,000 it becomes impractical. The Nyström approximation selects m ≪ n landmark points, computes a rank-m approximation K ≈ K_nm K_mm⁻¹ K_mn, and applies PCA on the resulting m-dimensional feature map — reducing cost to O(nmd).

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.kernel_approximation import Nystroem
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
import time

X, y = make_classification(n_samples=10000, n_features=50,
                            n_informative=20, random_state=42)

# Nyström: m=300 landmarks approximate the full RBF kernel
m = 300
nystrom = Nystroem(kernel='rbf', gamma=0.01, n_components=m, random_state=42)

t0 = time.time()
X_approx = nystrom.fit_transform(X)
print(f'Nystroem time: {time.time() - t0:.2f}s, shape: {X_approx.shape}')

# PCA on the approximate feature map
pca = PCA(n_components=50)
X_final = pca.fit_transform(X_approx)
print(f'Explained var (Nystroem+PCA): {pca.explained_variance_ratio_.sum():.3f}')

# End-to-end pipeline for classification
pipe = Pipeline([
    ('nystrom', Nystroem(kernel='rbf', gamma=0.01, n_components=200, random_state=42)),
    ('clf', LinearSVC(max_iter=1000, random_state=42))
])
scores = cross_val_score(pipe, X, y, cv=3, scoring='accuracy')
print(f'Nystroem+LinearSVC accuracy: {scores.mean():.3f} +/- {scores.std():.3f}')
```

## Hyperparameter Tuning

For the RBF kernel, γ = 1/(2σ²) controls the radius of influence of each training point. Small γ → wide Gaussian, smooth boundaries; large γ → tight influence, risk of overfitting. A practical starting point: γ = 1/d_features (the default in sklearn). For polynomial kernels, degree d=2 or d=3 with coef0=1 is a common choice. Tune γ via cross-validated reconstruction error or downstream classification accuracy, not by visual inspection of the embedding alone.

| Property | PCA | Kernel PCA | t-SNE | UMAP |
| --- | --- | --- | --- | --- |
| Linear | Yes | No (nonlinear) | No | No |
| Preserves global structure | Yes | Partial | No | Better than t-SNE |
| Scalable to large n | Yes (TruncatedSVD) | No (O(n³)) | No (O(n²)) | Yes (O(n^1.14)) |
| Deterministic | Yes | Yes | No | Yes (fixed seed) |
| New point projection | Yes | Approx (Nystroem) | No | Yes |

---

Kernel PCA is the principled extension of PCA to nonlinear data. Its key limitation is computational cost: O(n²) memory and O(n³) eigendecomposition. For large datasets, the Nyström approximation or UMAP (which has better scalability) are more practical choices. When the data structure is well-understood and a specific kernel captures it, Kernel PCA provides cleaner theoretical guarantees than manifold methods like t-SNE or UMAP.

