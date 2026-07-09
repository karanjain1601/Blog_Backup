---
title: "Subspace Methods — Robust PCA and Sparse PCA"
slug: "subspace-methods"
description: "How standard PCA fails under outliers, Robust PCA via Principal Component Pursuit decomposing M = L + S with nuclear norm and L1 penalties, ADMM optimisation, Sparse PCA for interpretable loadings, and NMF as a parts-based representation."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgUENBIG1pbmltaXNlcyBhIHNxdWFyZWQtZXJyb3IgKEwyKSBvYmplY3RpdmUsIG1ha2luZyBpdCBleHRyZW1lbHkgc2Vuc2l0aXZlIHRvIG91dGxpZXJzOiBhIHNpbmdsZSBjb3JydXB0ZWQgcG9pbnQgY2FuIHJvdGF0ZSBhbiBlbnRpcmUgcHJpbmNpcGFsIGNvbXBvbmVudC4gUm9idXN0IFBDQSBhbmQgU3BhcnNlIFBDQSBhcmUgZXh0ZW5zaW9ucyB0aGF0IGhhbmRsZSBjb3JydXB0ZWQgZGF0YSBvciBlbmZvcmNlIGludGVycHJldGFibGUsIHNwYXJzZSBzdHJ1Y3R1cmUgaW4gdGhlIGxvYWRpbmdzLiBUaGVzZSBtZXRob2RzIGFyZSBjcml0aWNhbCBpbiBjb21wdXRlciB2aXNpb24sIHNpZ25hbCBwcm9jZXNzaW5nLCBhbmQgZ2Vub21pY3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFN0YW5kYXJkIFBDQSBGYWlscyBVbmRlciBPdXRsaWVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEwyIG9iamVjdGl2ZSDigJZYIC0gVeKCls6j4oKWVuKCluG1gOKAll9GwrIgYXNzaWducyBlcXVhbCB3ZWlnaHQgdG8gYWxsIGVudHJpZXMuIEEgc2luZ2xlIGdyb3NzIG91dGxpZXIgKGUuZy4gYSBjb3JydXB0ZWQgcGl4ZWwgb3Igc2Vuc29yIHNwaWtlKSBjYW4gY29udHJpYnV0ZSBtb3JlIHRvIHRoZSBvYmplY3RpdmUgdGhhbiBodW5kcmVkcyBvZiBub3JtYWwgb2JzZXJ2YXRpb25zLiBCZWNhdXNlIFBDQSBtaW5pbWlzZXMgYSBnbG9iYWwgc3VtIG9mIHNxdWFyZWQgcmVzaWR1YWxzLCBpdCB3aWxsIHRpbHQgaXRzIHByaW5jaXBhbCBjb21wb25lbnRzIHRvIHBhcnRpYWxseSBhY2NvbW1vZGF0ZSB0aGUgb3V0bGllciBhdCB0aGUgZXhwZW5zZSBvZiB0aGUgdHJ1ZSBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUm9idXN0IFBDQTogRGVjb21wb3NpdGlvbiBNID0gTCArIFMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJvYnVzdCBQQ0EgKENhbmTDqHMgZXQgYWwuIDIwMTEpIGRlY29tcG9zZXMgdGhlIGRhdGEgbWF0cml4IE0gaW50byBhIGxvdy1yYW5rIG1hdHJpeCBMICh0aGUgXHUwMDI3YmFja2dyb3VuZFx1MDAyNyBvciBzaWduYWwpIGFuZCBhIHNwYXJzZSBtYXRyaXggUyAodGhlIFx1MDAyN2ZvcmVncm91bmRcdTAwMjcgb3Igb3V0bGllcnMpOiBNID0gTCArIFMuIFRoZSBjb252ZXggcmVsYXhhdGlvbiBpcyBQcmluY2lwYWwgQ29tcG9uZW50IFB1cnN1aXQ6IG1pbmltaXNlIG51Y2xlYXJfbm9ybShMKSArIM674oCWU+KAluKCgSBzdWJqZWN0IHRvIEwgKyBTID0gTS4gVGhlIG51Y2xlYXIgbm9ybSAoc3VtIG9mIHNpbmd1bGFyIHZhbHVlcykgaXMgdGhlIGNvbnZleCBzdXJyb2dhdGUgZm9yIHJhbmsoTCk7IHRoZSBMMSBub3JtIGVuZm9yY2VzIHNwYXJzaXR5IGluIFMuIFRoZSBvcHRpbWFsIM67ID0gMS/iiJptYXgobSxuKSB1bmRlciBpbmNvaGVyZW5jZSBjb25kaXRpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIHJvYnVzdF9wY2FfYWRtbShNLCBsYW09Tm9uZSwgbXU9Tm9uZSwgbWF4X2l0ZXI9NTAwLCB0b2w9MWUtNik6XG4gICAgXCJcIlwiUHJpbmNpcGFsIENvbXBvbmVudCBQdXJzdWl0IHZpYSBBRE1NLlwiXCJcIlxuICAgIG0sIG4gPSBNLnNoYXBlXG4gICAgbGFtID0gbGFtIG9yIDEuMCAvIG5wLnNxcnQobWF4KG0sIG4pKVxuICAgIG11ID0gbXUgb3IgbSAqIG4gLyAoNC4wICogbnAuYWJzKE0pLnN1bSgpKVxuXG4gICAgTCA9IG5wLnplcm9zX2xpa2UoTSlcbiAgICBTID0gbnAuemVyb3NfbGlrZShNKVxuICAgIFkgPSBucC56ZXJvc19saWtlKE0pICAjIExhZ3JhbmdlIG11bHRpcGxpZXJcblxuICAgIGRlZiBzdnQoWCwgdGF1KTpcbiAgICAgICAgXCJcIlwiU2luZ3VsYXIgdmFsdWUgdGhyZXNob2xkaW5nIChudWNsZWFyIG5vcm0gcHJveCkuXCJcIlwiXG4gICAgICAgIFUsIHMsIFZ0ID0gbnAubGluYWxnLnN2ZChYLCBmdWxsX21hdHJpY2VzPUZhbHNlKVxuICAgICAgICBzX3QgPSBucC5tYXhpbXVtKHMgLSB0YXUsIDApXG4gICAgICAgIHJldHVybiBVIEAgbnAuZGlhZyhzX3QpIEAgVnQsIChzX3QgXHUwMDNlIDApLnN1bSgpXG5cbiAgICBkZWYgc29mdChYLCB0YXUpOlxuICAgICAgICBcIlwiXCJFbGVtZW50LXdpc2Ugc29mdCB0aHJlc2hvbGRpbmcgKEwxIHByb3gpLlwiXCJcIlxuICAgICAgICByZXR1cm4gbnAuc2lnbihYKSAqIG5wLm1heGltdW0obnAuYWJzKFgpIC0gdGF1LCAwKVxuXG4gICAgZm9yIGkgaW4gcmFuZ2UobWF4X2l0ZXIpOlxuICAgICAgICBMLCByYW5rID0gc3Z0KE0gLSBTICsgWSAvIG11LCAxLjAgLyBtdSlcbiAgICAgICAgUyA9IHNvZnQoTSAtIEwgKyBZIC8gbXUsIGxhbSAvIG11KVxuICAgICAgICByZXNpZHVhbCA9IE0gLSBMIC0gU1xuICAgICAgICBZID0gWSArIG11ICogcmVzaWR1YWxcbiAgICAgICAgZXJyID0gbnAubGluYWxnLm5vcm0ocmVzaWR1YWwsIFx1MDAyN2Zyb1x1MDAyNykgLyAobnAubGluYWxnLm5vcm0oTSwgXHUwMDI3ZnJvXHUwMDI3KSArIDFlLTEwKVxuICAgICAgICBpZiBlcnIgXHUwMDNjIHRvbDpcbiAgICAgICAgICAgIHByaW50KGZcdTAwMjdDb252ZXJnZWQgYXQgaXRlciB7aSsxfSwgcmFuayhMKT17cmFua31cdTAwMjcpXG4gICAgICAgICAgICByZXR1cm4gTCwgU1xuICAgIHByaW50KGZcdTAwMjdNYXggaXRlciByZWFjaGVkLCByYW5rKEwpPXtyYW5rfVx1MDAyNylcbiAgICByZXR1cm4gTCwgU1xuXG4jIFNpbXVsYXRlIHZpZGVvIGZvcmVncm91bmQvYmFja2dyb3VuZCBzZXBhcmF0aW9uXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5uX2ZyYW1lcywgbl9waXhlbHMgPSAxMDAsIDMwMFxuYmFja2dyb3VuZCA9IHJuZy5ub3JtYWwoMCwgMC4xLCAobl9mcmFtZXMsIG5fcGl4ZWxzKSlcbmZvcmVncm91bmQgPSBucC56ZXJvcygobl9mcmFtZXMsIG5fcGl4ZWxzKSlcbmZvcmVncm91bmRbMjA6NzAsIDUwOjgwXSA9IHJuZy5ub3JtYWwoMi4wLCAwLjMsICg1MCwgMzApKSAgIyBtb3Zpbmcgb2JqZWN0XG5NID0gYmFja2dyb3VuZCArIGZvcmVncm91bmRcbkwsIFMgPSByb2J1c3RfcGNhX2FkbW0oTSlcbnByaW50KGZcdTAwMjdTIG5vbi16ZXJvczogeyhucC5hYnMoUykgXHUwMDNlIDAuMDUpLnN1bSgpfSAvIHtTLnNpemV9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiTGFtYmRhIENob2ljZSIsImNvbnRlbnQiOiJUaGUgdGhlb3JldGljYWwgb3B0aW1hbCDOuyA9IDEv4oiabWF4KG0sbikgd29ya3Mgd2VsbCB3aGVuIHRoZSBpbmNvaGVyZW5jZSBjb25kaXRpb25zIGhvbGQgKGxvdy1yYW5rIHBhcnQgaXMgbm90IHRvbyBcdTAwMjdzcGlreVx1MDAyNywgc3BhcnNlIHBhcnQgaXMgbm90IHRvbyBcdTAwMjdkZW5zZVx1MDAyNykuIEluIHByYWN0aWNlLCBpbmNyZWFzZSDOuyB0byByZWNvdmVyIGRlbnNlciBmb3JlZ3JvdW5kIG9yIGRlY3JlYXNlIGl0IHRvIHRvbGVyYXRlIGRlbnNlciBhbm9tYWxpZXMuIENyb3NzLXZhbGlkYXRlIGJ5IHJlY29uc3RydWN0aW5nIGhlbGQtb3V0IGNvcnJ1cHRlZCB0ZXN0IGZyYW1lcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTcGFyc2UgUENBIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTcGFyc2UgUENBIChab3UgZXQgYWwuIDIwMDYpIHNlZWtzIHByaW5jaXBhbCBjb21wb25lbnRzIHdpdGggc3BhcnNlIGxvYWRpbmdzIOKAlCBvbmx5IGEgZmV3IGZlYXR1cmVzIGFyZSBub24temVybyBpbiBlYWNoIGNvbXBvbmVudC4gVGhpcyBtYWtlcyB0aGUgY29tcG9uZW50cyBtb3JlIGludGVycHJldGFibGU6IGluc3RlYWQgb2YgYSBnbG9iYWwgbWl4dHVyZSBvZiBhbGwgZmVhdHVyZXMsIGVhY2ggUEMgY2FuIGJlIGF0dHJpYnV0ZWQgdG8gYSBtZWFuaW5nZnVsIHN1YnNldC4gc2tsZWFybiBpbXBsZW1lbnRzIHRoaXMgdmlhIGFuIGVsYXN0aWMgbmV0IHBlbmFsdHkgb24gdGhlIGxvYWRpbmdzLCBhbHRlcm5hdGluZyBiZXR3ZWVuIHVwZGF0aW5nIHNjb3JlcyBhbmQgdXBkYXRpbmcgKHNwYXJzZSkgbG9hZGluZ3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmRlY29tcG9zaXRpb24gaW1wb3J0IFNwYXJzZVBDQSwgUENBXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGZldGNoX29saXZldHRpX2ZhY2VzXG5cbmZhY2VzID0gZmV0Y2hfb2xpdmV0dGlfZmFjZXMoKVxuWCA9IGZhY2VzLmRhdGEgICMgKDQwMCwgNDA5NilcbnByaW50KGZcdTAwMjdGYWNlcyBkYXRhc2V0OiB7WC5zaGFwZX1cdTAwMjcpXG5cbm5fY29tcCA9IDIwXG5wY2EgPSBQQ0Eobl9jb21wb25lbnRzPW5fY29tcCwgcmFuZG9tX3N0YXRlPTQyKVxuWF9wY2EgPSBwY2EuZml0X3RyYW5zZm9ybShYKVxuXG5zcGNhID0gU3BhcnNlUENBKG5fY29tcG9uZW50cz1uX2NvbXAsIGFscGhhPTEuMCxcbiAgICAgICAgICAgICAgICAgIHJhbmRvbV9zdGF0ZT00Miwgbl9qb2JzPS0xLCBtYXhfaXRlcj0xMDApXG5YX3NwY2EgPSBzcGNhLmZpdF90cmFuc2Zvcm0oWClcblxucGNhX2RlbnNpdHkgPSAobnAuYWJzKHBjYS5jb21wb25lbnRzXykgXHUwMDNlIDFlLTMpLm1lYW4oKVxuc3BjYV9kZW5zaXR5ID0gKG5wLmFicyhzcGNhLmNvbXBvbmVudHNfKSBcdTAwM2UgMWUtMykubWVhbigpXG5wcmludChmXHUwMDI3UENBIGxvYWRpbmdzIGRlbnNpdHk6ICAgICAgICB7cGNhX2RlbnNpdHk6LjNmfVx1MDAyNylcbnByaW50KGZcdTAwMjdTcGFyc2VQQ0EgbG9hZGluZ3MgZGVuc2l0eTogIHtzcGNhX2RlbnNpdHk6LjNmfVx1MDAyNylcblxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDQsIDUsIGZpZ3NpemU9KDE0LCAxMikpXG5mb3IgaSwgYXggaW4gZW51bWVyYXRlKGF4ZXNbOjJdLmZsYXQpOlxuICAgIGF4Lmltc2hvdyhwY2EuY29tcG9uZW50c19baV0ucmVzaGFwZSg2NCwgNjQpLCBjbWFwPVx1MDAyN2dyYXlcdTAwMjcpXG4gICAgYXguc2V0X3RpdGxlKGZcdTAwMjdQQ0Ege2krMX1cdTAwMjcpOyBheC5heGlzKFx1MDAyN29mZlx1MDAyNylcbmZvciBpLCBheCBpbiBlbnVtZXJhdGUoYXhlc1syOl0uZmxhdCk6XG4gICAgYXguaW1zaG93KHNwY2EuY29tcG9uZW50c19baV0ucmVzaGFwZSg2NCwgNjQpLCBjbWFwPVx1MDAyN2dyYXlcdTAwMjcpXG4gICAgYXguc2V0X3RpdGxlKGZcdTAwMjdTUENBIHtpKzF9XHUwMDI3KTsgYXguYXhpcyhcdTAwMjdvZmZcdTAwMjcpXG5wbHQuc3VwdGl0bGUoXHUwMDI3U3RhbmRhcmQgUENBIHZzIFNwYXJzZSBQQ0EgQ29tcG9uZW50c1x1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwYXJzZSBQQ0EgZm9yIEZlYXR1cmUgU2VsZWN0aW9uIGFuZCBJbnRlcnByZXRhYmlsaXR5In0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLmRlY29tcG9zaXRpb24gaW1wb3J0IFNwYXJzZVBDQSwgUENBXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGxvYWRfYnJlYXN0X2NhbmNlclxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbmRhdGEgPSBsb2FkX2JyZWFzdF9jYW5jZXIoKVxuWCA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShkYXRhLmRhdGEpXG5mZWF0dXJlX25hbWVzID0gZGF0YS5mZWF0dXJlX25hbWVzXG5cbnNwY2EgPSBTcGFyc2VQQ0Eobl9jb21wb25lbnRzPTUsIGFscGhhPTMuMCwgcmFuZG9tX3N0YXRlPTQyLCBuX2pvYnM9LTEpXG5YX3NwY2EgPSBzcGNhLmZpdF90cmFuc2Zvcm0oWClcblxucGNhID0gUENBKG5fY29tcG9uZW50cz01KVxuWF9wY2EgPSBwY2EuZml0X3RyYW5zZm9ybShYKVxuXG5wcmludChcdTAwMjc9PT0gU3BhcnNlIFBDQTogQWN0aXZlIEZlYXR1cmVzIHBlciBDb21wb25lbnQgPT09XHUwMDI3KVxuZm9yIGsgaW4gcmFuZ2UoNSk6XG4gICAgY29tcCA9IHNwY2EuY29tcG9uZW50c19ba11cbiAgICBhY3RpdmVfaWR4ID0gbnAud2hlcmUobnAuYWJzKGNvbXApIFx1MDAzZSAxZS0zKVswXVxuICAgIG5fYWN0aXZlID0gbGVuKGFjdGl2ZV9pZHgpXG4gICAgbmFtZXNfc3RyID0gXHUwMDI3LCBcdTAwMjcuam9pbihmZWF0dXJlX25hbWVzW2FjdGl2ZV9pZHhbOjVdXSlcbiAgICBwcmludChmXHUwMDI3ICBQQ3trKzF9ICh7bl9hY3RpdmV9L3tsZW4oZmVhdHVyZV9uYW1lcyl9IGFjdGl2ZSk6IHtuYW1lc19zdHJ9XHUwMDI3KVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMSwgMiwgZmlnc2l6ZT0oMTQsIDUpKVxuZm9yIGsgaW4gcmFuZ2UoNSk6XG4gICAgYXhlc1swXS5wbG90KG5wLmFicyhwY2EuY29tcG9uZW50c19ba10pLCBsYWJlbD1mXHUwMDI3UEN7aysxfVx1MDAyNywgYWxwaGE9MC43KVxuICAgIGF4ZXNbMV0ucGxvdChucC5hYnMoc3BjYS5jb21wb25lbnRzX1trXSksIGxhYmVsPWZcdTAwMjdTUEN7aysxfVx1MDAyNywgYWxwaGE9MC43KVxuYXhlc1swXS5zZXRfdGl0bGUoXHUwMDI3UENBIOKAlCBkZW5zZSBsb2FkaW5nc1x1MDAyNyk7IGF4ZXNbMF0ubGVnZW5kKClcbmF4ZXNbMV0uc2V0X3RpdGxlKFx1MDAyN1NwYXJzZSBQQ0Eg4oCUIHNwYXJzZSBsb2FkaW5nc1x1MDAyNyk7IGF4ZXNbMV0ubGVnZW5kKClcbnBsdC5zdXB0aXRsZShcdTAwMjdGZWF0dXJlIExvYWRpbmdzOiBQQ0EgdnMgU3BhcnNlIFBDQVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik5NRiBhcyBQYXJ0cy1CYXNlZCBSZXByZXNlbnRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTk1GIChMZWUgXHUwMDI2IFNldW5nIDE5OTkpIGRlY29tcG9zZXMgYSBub24tbmVnYXRpdmUgbWF0cml4IFYg4omIIFdIIHdoZXJlIGJvdGggVyBhbmQgSCBhcmUgbm9uLW5lZ2F0aXZlLiBGb3IgZmFjZSBpbWFnZXMsIHRoaXMgcHJvZHVjZXMgcGFydHMtYmFzZWQgcmVwcmVzZW50YXRpb25zOiBpbmRpdmlkdWFsIGNvbXBvbmVudHMgY29ycmVzcG9uZCB0byBmYWNpYWwgcGFydHMgKGV5ZXMsIG5vc2UsIGNoZWVrcykgcmF0aGVyIHRoYW4gdGhlIGhvbGlzdGljIFx1MDAyN2VpZ2VuZmFjZXNcdTAwMjcgb2YgUENBLiBUaGlzIG9jY3VycyBiZWNhdXNlIG5vbi1uZWdhdGl2aXR5IHByZXZlbnRzIGNhbmNlbGxhdGl2ZSBjb21iaW5hdGlvbnMg4oCUIGZlYXR1cmVzIGNhbiBvbmx5IGJlIGFkZGVkLCBub3Qgc3VidHJhY3RlZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgTk1GLCBQQ0FcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgZmV0Y2hfb2xpdmV0dGlfZmFjZXNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBNaW5NYXhTY2FsZXJcblxuZmFjZXMgPSBmZXRjaF9vbGl2ZXR0aV9mYWNlcygpXG5YID0gTWluTWF4U2NhbGVyKCkuZml0X3RyYW5zZm9ybShmYWNlcy5kYXRhKSAgIyBub24tbmVnYXRpdmUgcmVxdWlyZWQgZm9yIE5NRlxubl9jb21wID0gMTZcblxubm1mID0gTk1GKG5fY29tcG9uZW50cz1uX2NvbXAsIGluaXQ9XHUwMDI3bm5kc3ZkXHUwMDI3LFxuICAgICAgICAgICByYW5kb21fc3RhdGU9NDIsIG1heF9pdGVyPTUwMCwgYWxwaGFfVz0wLjAxKVxuV19ubWYgPSBubWYuZml0X3RyYW5zZm9ybShYKVxuSF9ubWYgPSBubWYuY29tcG9uZW50c18gICMgcGFydHNcblxucGNhID0gUENBKG5fY29tcG9uZW50cz1uX2NvbXAsIHJhbmRvbV9zdGF0ZT00MilcbnBjYS5maXQoWClcblxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDQsIDgsIGZpZ3NpemU9KDE2LCA5KSlcbmZvciBpLCBheCBpbiBlbnVtZXJhdGUoYXhlc1s6Ml0uZmxhdCk6XG4gICAgYXguaW1zaG93KHBjYS5jb21wb25lbnRzX1tpXS5yZXNoYXBlKDY0LCA2NCksIGNtYXA9XHUwMDI3Z3JheVx1MDAyNylcbiAgICBheC5zZXRfdGl0bGUoZlx1MDAyN0VGIHtpKzF9XHUwMDI3LCBmb250c2l6ZT04KTsgYXguYXhpcyhcdTAwMjdvZmZcdTAwMjcpXG5mb3IgaSwgYXggaW4gZW51bWVyYXRlKGF4ZXNbMjpdLmZsYXQpOlxuICAgIGF4Lmltc2hvdyhIX25tZltpXS5yZXNoYXBlKDY0LCA2NCksIGNtYXA9XHUwMDI3aG90XHUwMDI3KVxuICAgIGF4LnNldF90aXRsZShmXHUwMDI3Tk1GIHtpKzF9XHUwMDI3LCBmb250c2l6ZT04KTsgYXguYXhpcyhcdTAwMjdvZmZcdTAwMjcpXG5cbnBsdC5zdXB0aXRsZShcdTAwMjdQQ0EgRWlnZW5mYWNlcyAoaG9saXN0aWMsIGNhbiBjYW5jZWwpIHZzIE5NRiBQYXJ0cyAoYWRkaXRpdmUgb25seSlcdTAwMjcpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zaG93KClcbnByaW50KGZcdTAwMjdOTUYgcmVjb25zdHJ1Y3Rpb24gZXJyb3I6IHtubWYucmVjb25zdHJ1Y3Rpb25fZXJyXzouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoZW4gdG8gVXNlIEVhY2ggTWV0aG9kIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTdGFuZGFyZCBQQ0E6IGNsZWFuIGRhdGEsIGxpbmVhciBzdHJ1Y3R1cmUsIGZhc3QgZXhwbG9yYXRpb24g4oCUIGFsd2F5cyB0cnkgZmlyc3QiLCJSb2J1c3QgUENBOiBkYXRhIHdpdGggZ3Jvc3MgY29ycnVwdGlvbnMsIG1pc3NpbmcgZGF0YSwgc3VydmVpbGxhbmNlIHZpZGVvIGJhY2tncm91bmQgc2VwYXJhdGlvbiIsIlNwYXJzZSBQQ0E6IHdoZW4gaW50ZXJwcmV0YWJpbGl0eSBvZiBpbmRpdmlkdWFsIGZlYXR1cmVzIG1hdHRlcnMgKGdlbm9taWNzLCBmaW5hbmNlLCBjbGluaWNhbCkiLCJOTUY6IG5vbi1uZWdhdGl2ZSBkYXRhIChjb3VudHMsIHNwZWN0cmEsIGltYWdlcykgd2hlcmUgcGFydHMtYmFzZWQgaW50ZXJwcmV0YXRpb24gaXMgZGVzaXJlZCIsIkZhY3RvciBBbmFseXNpczogd2hlbiB5b3Ugd2FudCB0byBtb2RlbCBvYnNlcnZhdGlvbiBub2lzZSBleHBsaWNpdGx5IChjb21tb24gaW4gcHN5Y2hvbWV0cmljcykiXX0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiUENBIiwiUm9idXN0IFBDQSIsIlNwYXJzZSBQQ0EiLCJOTUYiXSwicm93cyI6W1siUm9idXN0IHRvIG91dGxpZXJzIiwiTm8iLCJZZXMgKEwxIG9uIFMpIiwiTm8iLCJNb2RlcmF0ZSJdLFsiU3BhcnNlIGxvYWRpbmdzIiwiTm8iLCJObyIsIlllcyIsIlllcyAobm9uLW5lZ2F0aXZlKSJdLFsiTm9uLW5lZ2F0aXZlIiwiTm8iLCJObyIsIk5vIiwiWWVzIChyZXF1aXJlZCkiXSxbIkludGVycHJldGFibGUiLCJNb2RlcmF0ZSIsIkxvdyIsIkhpZ2giLCJIaWdoIl0sWyJDb21wdXRhdGlvbmFsIGNvc3QiLCJPKG5kIG1pbihuLGQpKSIsIk8obsKyZCkgcGVyIEFETU0iLCJPKG7CsmspIGFsdGVybmF0aW5nIiwiTyhuZGspIGFsdGVybmF0aW5nIl0sWyJCZXN0IHVzZSBjYXNlIiwiRXhwbG9yYXRpb24iLCJDb3JydXB0ZWQgZGF0YSIsIkdlbm9taWNzLCBmaW5hbmNlIiwiU3BlY3RyYSwgaW1hZ2VzLCB0ZXh0Il1dfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiQ2hvb3NpbmcgdGhlIFJpZ2h0IFN1YnNwYWNlIE1ldGhvZCIsImNvbnRlbnQiOiJJZiB5b3VyIGRhdGEgaGFzIGdyb3NzIG91dGxpZXJzIChub3QganVzdCBHYXVzc2lhbiBub2lzZSk6IHVzZSBSb2J1c3QgUENBLiBJZiB5b3UgbmVlZCB0byBleHBsYWluIHdoaWNoIGZlYXR1cmVzIGRyaXZlIGVhY2ggY29tcG9uZW50IHRvIGEgZG9tYWluIGV4cGVydDogdXNlIFNwYXJzZSBQQ0Egd2l0aCBhbHBoYSB0dW5lZCB0byB0aGUgZGVzaXJlZCBzcGFyc2l0eSBsZXZlbC4gSWYgeW91ciBkYXRhIGlzIG5vbi1uZWdhdGl2ZSAoZ2VuZSBjb3VudHMsIFRGLUlERiwgc3BlY3Ryb2dyYW1zKTogTk1GIGlzIHRoZSBuYXR1cmFsIGNob2ljZSBhbmQgb2Z0ZW4gcHJvZHVjZXMgbW9yZSBpbnRlcnByZXRhYmxlIGNvbXBvbmVudHMgdGhhbiBzcGFyc2UgUENBLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmV5b25kIHRoZXNlIGZvdXIgbWV0aG9kcywgdmFyaW1heCByb3RhdGlvbiBvZiBQQ0EgY29tcG9uZW50cyAob3J0aG9nb25hbCByb3RhdGlvbiB0byBtYXhpbWlzZSBjb21wb25lbnQgc2ltcGxpY2l0eSkgYW5kIEZhY3RvciBBbmFseXNpcyAod2hpY2ggYWRkcyBhIG5vaXNlIG1vZGVsOiBYID0gV1ogKyDOtSkgYXJlIHZhbHVhYmxlIHdoZW4geW91IHdhbnQgaW50ZXJwcmV0YWJsZSBQQ0EtbGlrZSBjb21wb25lbnRzIHdpdGhvdXQgdGhlIGZ1bGwgc3BhcnNpdHkgY29uc3RyYWludC4gVmFyaW1heCBpcyBhIGNvbXB1dGF0aW9uYWxseSBjaGVhcCBwb3N0LXByb2Nlc3Npbmcgc3RlcCB0aGF0IG9mdGVuIHByb2R1Y2VzIG1vcmUgaW50ZXJwcmV0YWJsZSBsb2FkaW5ncyB0aGFuIHJhdyBQQ0Egd2l0aG91dCBhbnkgaXRlcmF0aXZlIG9wdGltaXNhdGlvbi4ifSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSb2J1c3QgUENBLCBTcGFyc2UgUENBLCBhbmQgTk1GIGFyZSBjb21wbGVtZW50YXJ5IGV4dGVuc2lvbnMgb2Ygc3RhbmRhcmQgUENBIHRoYXQgdHJhZGUgb2ZmIG9wdGltYWxpdHkgZm9yIHJvYnVzdG5lc3MsIGludGVycHJldGFiaWxpdHksIG9yIHN0cnVjdHVyYWwgY29uc3RyYWludHMuIEluIHByYWN0aWNlLCB0cnkgc3RhbmRhcmQgUENBIGZpcnN0LCB0aGVuIGFwcGx5IFJvYnVzdCBQQ0EgaWYgb3V0bGllcnMgYXJlIHN1c3BlY3RlZCwgU3BhcnNlIFBDQSBpZiBsb2FkaW5ncyBtdXN0IGJlIGludGVycHJldGFibGUsIG9yIE5NRiBpZiBub24tbmVnYXRpdml0eSBpcyBzZW1hbnRpY2FsbHkgbWVhbmluZ2Z1bCBmb3IgeW91ciBkb21haW4uIn1d"
---
# Subspace Methods — Robust PCA and Sparse PCA

Standard PCA minimises a squared-error (L2) objective, making it extremely sensitive to outliers: a single corrupted point can rotate an entire principal component. Robust PCA and Sparse PCA are extensions that handle corrupted data or enforce interpretable, sparse structure in the loadings. These methods are critical in computer vision, signal processing, and genomics.

## Why Standard PCA Fails Under Outliers

The L2 objective ‖X - UₖΣₖVₖᵀ‖_F² assigns equal weight to all entries. A single gross outlier (e.g. a corrupted pixel or sensor spike) can contribute more to the objective than hundreds of normal observations. Because PCA minimises a global sum of squared residuals, it will tilt its principal components to partially accommodate the outlier at the expense of the true structure.

## Robust PCA: Decomposition M = L + S

Robust PCA (Candès et al. 2011) decomposes the data matrix M into a low-rank matrix L (the 'background' or signal) and a sparse matrix S (the 'foreground' or outliers): M = L + S. The convex relaxation is Principal Component Pursuit: minimise nuclear_norm(L) + λ‖S‖₁ subject to L + S = M. The nuclear norm (sum of singular values) is the convex surrogate for rank(L); the L1 norm enforces sparsity in S. The optimal λ = 1/√max(m,n) under incoherence conditions.

```python
import numpy as np

def robust_pca_admm(M, lam=None, mu=None, max_iter=500, tol=1e-6):
    """Principal Component Pursuit via ADMM."""
    m, n = M.shape
    lam = lam or 1.0 / np.sqrt(max(m, n))
    mu = mu or m * n / (4.0 * np.abs(M).sum())

    L = np.zeros_like(M)
    S = np.zeros_like(M)
    Y = np.zeros_like(M)  # Lagrange multiplier

    def svt(X, tau):
        """Singular value thresholding (nuclear norm prox)."""
        U, s, Vt = np.linalg.svd(X, full_matrices=False)
        s_t = np.maximum(s - tau, 0)
        return U @ np.diag(s_t) @ Vt, (s_t > 0).sum()

    def soft(X, tau):
        """Element-wise soft thresholding (L1 prox)."""
        return np.sign(X) * np.maximum(np.abs(X) - tau, 0)

    for i in range(max_iter):
        L, rank = svt(M - S + Y / mu, 1.0 / mu)
        S = soft(M - L + Y / mu, lam / mu)
        residual = M - L - S
        Y = Y + mu * residual
        err = np.linalg.norm(residual, 'fro') / (np.linalg.norm(M, 'fro') + 1e-10)
        if err < tol:
            print(f'Converged at iter {i+1}, rank(L)={rank}')
            return L, S
    print(f'Max iter reached, rank(L)={rank}')
    return L, S

# Simulate video foreground/background separation
rng = np.random.default_rng(42)
n_frames, n_pixels = 100, 300
background = rng.normal(0, 0.1, (n_frames, n_pixels))
foreground = np.zeros((n_frames, n_pixels))
foreground[20:70, 50:80] = rng.normal(2.0, 0.3, (50, 30))  # moving object
M = background + foreground
L, S = robust_pca_admm(M)
print(f'S non-zeros: {(np.abs(S) > 0.05).sum()} / {S.size}')
```

> **Lambda Choice**: The theoretical optimal λ = 1/√max(m,n) works well when the incoherence conditions hold (low-rank part is not too 'spiky', sparse part is not too 'dense'). In practice, increase λ to recover denser foreground or decrease it to tolerate denser anomalies. Cross-validate by reconstructing held-out corrupted test frames.

## Sparse PCA

Sparse PCA (Zou et al. 2006) seeks principal components with sparse loadings — only a few features are non-zero in each component. This makes the components more interpretable: instead of a global mixture of all features, each PC can be attributed to a meaningful subset. sklearn implements this via an elastic net penalty on the loadings, alternating between updating scores and updating (sparse) loadings.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import SparsePCA, PCA
from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces()
X = faces.data  # (400, 4096)
print(f'Faces dataset: {X.shape}')

n_comp = 20
pca = PCA(n_components=n_comp, random_state=42)
X_pca = pca.fit_transform(X)

spca = SparsePCA(n_components=n_comp, alpha=1.0,
                  random_state=42, n_jobs=-1, max_iter=100)
X_spca = spca.fit_transform(X)

pca_density = (np.abs(pca.components_) > 1e-3).mean()
spca_density = (np.abs(spca.components_) > 1e-3).mean()
print(f'PCA loadings density:        {pca_density:.3f}')
print(f'SparsePCA loadings density:  {spca_density:.3f}')

fig, axes = plt.subplots(4, 5, figsize=(14, 12))
for i, ax in enumerate(axes[:2].flat):
    ax.imshow(pca.components_[i].reshape(64, 64), cmap='gray')
    ax.set_title(f'PCA {i+1}'); ax.axis('off')
for i, ax in enumerate(axes[2:].flat):
    ax.imshow(spca.components_[i].reshape(64, 64), cmap='gray')
    ax.set_title(f'SPCA {i+1}'); ax.axis('off')
plt.suptitle('Standard PCA vs Sparse PCA Components')
plt.tight_layout()
plt.show()
```

## Sparse PCA for Feature Selection and Interpretability

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import SparsePCA, PCA
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X = StandardScaler().fit_transform(data.data)
feature_names = data.feature_names

spca = SparsePCA(n_components=5, alpha=3.0, random_state=42, n_jobs=-1)
X_spca = spca.fit_transform(X)

pca = PCA(n_components=5)
X_pca = pca.fit_transform(X)

print('=== Sparse PCA: Active Features per Component ===')
for k in range(5):
    comp = spca.components_[k]
    active_idx = np.where(np.abs(comp) > 1e-3)[0]
    n_active = len(active_idx)
    names_str = ', '.join(feature_names[active_idx[:5]])
    print(f'  PC{k+1} ({n_active}/{len(feature_names)} active): {names_str}')

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for k in range(5):
    axes[0].plot(np.abs(pca.components_[k]), label=f'PC{k+1}', alpha=0.7)
    axes[1].plot(np.abs(spca.components_[k]), label=f'SPC{k+1}', alpha=0.7)
axes[0].set_title('PCA — dense loadings'); axes[0].legend()
axes[1].set_title('Sparse PCA — sparse loadings'); axes[1].legend()
plt.suptitle('Feature Loadings: PCA vs Sparse PCA')
plt.tight_layout()
plt.show()
```

## NMF as Parts-Based Representation

NMF (Lee & Seung 1999) decomposes a non-negative matrix V ≈ WH where both W and H are non-negative. For face images, this produces parts-based representations: individual components correspond to facial parts (eyes, nose, cheeks) rather than the holistic 'eigenfaces' of PCA. This occurs because non-negativity prevents cancellative combinations — features can only be added, not subtracted.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF, PCA
from sklearn.datasets import fetch_olivetti_faces
from sklearn.preprocessing import MinMaxScaler

faces = fetch_olivetti_faces()
X = MinMaxScaler().fit_transform(faces.data)  # non-negative required for NMF
n_comp = 16

nmf = NMF(n_components=n_comp, init='nndsvd',
           random_state=42, max_iter=500, alpha_W=0.01)
W_nmf = nmf.fit_transform(X)
H_nmf = nmf.components_  # parts

pca = PCA(n_components=n_comp, random_state=42)
pca.fit(X)

fig, axes = plt.subplots(4, 8, figsize=(16, 9))
for i, ax in enumerate(axes[:2].flat):
    ax.imshow(pca.components_[i].reshape(64, 64), cmap='gray')
    ax.set_title(f'EF {i+1}', fontsize=8); ax.axis('off')
for i, ax in enumerate(axes[2:].flat):
    ax.imshow(H_nmf[i].reshape(64, 64), cmap='hot')
    ax.set_title(f'NMF {i+1}', fontsize=8); ax.axis('off')

plt.suptitle('PCA Eigenfaces (holistic, can cancel) vs NMF Parts (additive only)')
plt.tight_layout()
plt.show()
print(f'NMF reconstruction error: {nmf.reconstruction_err_:.4f}')
```

## When to Use Each Method

- Standard PCA: clean data, linear structure, fast exploration — always try first
- Robust PCA: data with gross corruptions, missing data, surveillance video background separation
- Sparse PCA: when interpretability of individual features matters (genomics, finance, clinical)
- NMF: non-negative data (counts, spectra, images) where parts-based interpretation is desired
- Factor Analysis: when you want to model observation noise explicitly (common in psychometrics)

| Property | PCA | Robust PCA | Sparse PCA | NMF |
| --- | --- | --- | --- | --- |
| Robust to outliers | No | Yes (L1 on S) | No | Moderate |
| Sparse loadings | No | No | Yes | Yes (non-negative) |
| Non-negative | No | No | No | Yes (required) |
| Interpretable | Moderate | Low | High | High |
| Computational cost | O(nd min(n,d)) | O(n²d) per ADMM | O(n²k) alternating | O(ndk) alternating |
| Best use case | Exploration | Corrupted data | Genomics, finance | Spectra, images, text |

> **Choosing the Right Subspace Method**: If your data has gross outliers (not just Gaussian noise): use Robust PCA. If you need to explain which features drive each component to a domain expert: use Sparse PCA with alpha tuned to the desired sparsity level. If your data is non-negative (gene counts, TF-IDF, spectrograms): NMF is the natural choice and often produces more interpretable components than sparse PCA.

Beyond these four methods, varimax rotation of PCA components (orthogonal rotation to maximise component simplicity) and Factor Analysis (which adds a noise model: X = WZ + ε) are valuable when you want interpretable PCA-like components without the full sparsity constraint. Varimax is a computationally cheap post-processing step that often produces more interpretable loadings than raw PCA without any iterative optimisation.

---

Robust PCA, Sparse PCA, and NMF are complementary extensions of standard PCA that trade off optimality for robustness, interpretability, or structural constraints. In practice, try standard PCA first, then apply Robust PCA if outliers are suspected, Sparse PCA if loadings must be interpretable, or NMF if non-negativity is semantically meaningful for your domain.

