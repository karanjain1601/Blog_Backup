---
title: "UMAP — Topological Data Analysis and Fuzzy Simplicial Sets"
slug: "umap"
description: "UMAP's mathematical foundations in fuzzy simplicial sets and Riemannian geometry, how it optimises a cross-entropy objective, key hyperparameters, comparison with t-SNE, supervised UMAP, and parametric UMAP with a neural encoder."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVU1BUCAoVW5pZm9ybSBNYW5pZm9sZCBBcHByb3hpbWF0aW9uIGFuZCBQcm9qZWN0aW9uKSBpcyBncm91bmRlZCBpbiBhbGdlYnJhaWMgdG9wb2xvZ3kgYW5kIFJpZW1hbm5pYW4gZ2VvbWV0cnkgcmF0aGVyIHRoYW4gcHJvYmFiaWxpc3RpYyBtb2RlbGxpbmcuIEl0IG91dHBlcmZvcm1zIHQtU05FIG9uIHNwZWVkLCBnbG9iYWwgc3RydWN0dXJlIHByZXNlcnZhdGlvbiwgYW5kIHNjYWxhYmlsaXR5LCBhbmQgaXQgc3VwcG9ydHMgb3V0LW9mLXNhbXBsZSBwcm9qZWN0aW9uIOKAlCBtYWtpbmcgaXQgdXNlZnVsIGJleW9uZCB2aXN1YWxpc2F0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZ1enp5IFNpbXBsaWNpYWwgU2V0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVU1BUCBtb2RlbHMgdGhlIGhpZ2gtZGltZW5zaW9uYWwgZGF0YSBhcyBhIGZ1enp5IHNpbXBsaWNpYWwgc2V0OiBlYWNoIHBvaW50IHjhtaIgZGVmaW5lcyBhbiBvcGVuIGJhbGwgb2YgcmFkaXVzIM+B4bWiIChkaXN0YW5jZSB0byBuZWFyZXN0IG5laWdoYm91ciwgbWFraW5nIHRoZSBsb2NhbCBtZXRyaWMgYWRhcHRpdmUpLiBPdmVybGFwIGJldHdlZW4gYmFsbHMgZGVmaW5lcyBmdXp6eSBzZXQgbWVtYmVyc2hpcDogzrzhtaLisbwgPSBleHAoLShk4bWi4rG8IC0gz4HhtaIpL8+D4bWiKSwgd2hlcmUgz4PhtaIgaXMgdHVuZWQgc28gdGhhdCDOo+KxvCDOvOG1ouKxvCA9IGxvZ+KCgihuX25laWdoYm9ycykuIFRoZSB1bmlvbiBvZiB0aGVzZSBsb2NhbCBmdXp6eSBzZXRzIGZvcm1zIHRoZSBoaWdoLWRpbWVuc2lvbmFsIHRvcG9sb2dpY2FsIHJlcHJlc2VudGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNyb3NzLUVudHJvcHkgT3B0aW1pc2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVTUFQIG9wdGltaXNlcyB0aGUgbG93LWRpbWVuc2lvbmFsIGxheW91dCBieSBtaW5pbWlzaW5nIHRoZSBjcm9zcy1lbnRyb3B5IGJldHdlZW4gdGhlIGhpZ2gtZGltZW5zaW9uYWwgZnV6enkgZ3JhcGggYW5kIGEgbG93LWRpbWVuc2lvbmFsIGNvdW50ZXJwYXJ0OiBDID0gzqPhtaLisbwgW8684bWi4rG8IGxvZyjOvOG1ouKxvC/OveG1ouKxvCkgKyAoMS3OvOG1ouKxvCkgbG9nKCgxLc684bWi4rG8KS8oMS3OveG1ouKxvCkpXSwgd2hlcmUgzr3htaLisbwgPSAoMSArIGHigJZ54bWiLXnisbzigJbCsuG1hynigbvCuSBpcyB0aGUgbG93LWRpbSBzaW1pbGFyaXR5LiBVbmxpa2UgdC1TTkUsIHRoZSByZXB1bHNpdmUgdGVybSAoMS3OvCkoMS3OvSkgaXMgZXhwbGljaXRseSBpbmNsdWRlZCBhbmQgYmFsYW5jZWQuIE9wdGltaXNhdGlvbiB1c2VzIHN0b2NoYXN0aWMgZ3JhZGllbnQgZGVzY2VudCB3aXRoIG5lZ2F0aXZlIHNhbXBsaW5nLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgZmV0Y2hfb3Blbm1sXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBQQ0FcbmltcG9ydCB1bWFwICAjIHBpcCBpbnN0YWxsIHVtYXAtbGVhcm5cblxubW5pc3QgPSBmZXRjaF9vcGVubWwoXHUwMDI3bW5pc3RfNzg0XHUwMDI3LCB2ZXJzaW9uPTEsIGFzX2ZyYW1lPUZhbHNlKVxuWCA9IG1uaXN0LmRhdGFbOjUwMDBdLmFzdHlwZShmbG9hdClcbnkgPSBtbmlzdC50YXJnZXRbOjUwMDBdLmFzdHlwZShpbnQpXG5YID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG5YX3BjYSA9IFBDQShuX2NvbXBvbmVudHM9NTAsIHJhbmRvbV9zdGF0ZT00MikuZml0X3RyYW5zZm9ybShYKVxuXG4jIG5fbmVpZ2hib3JzIGNvbnRyb2xzIGxvY2FsIHZzIGdsb2JhbCB0cmFkZW9mZlxubl9uZWlnaGJvcnNfdmFscyA9IFs1LCAxNSwgNTAsIDIwMF1cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCA0LCBmaWdzaXplPSgyMCwgNSkpXG5cbmZvciBheCwgbl9uZWlnaCBpbiB6aXAoYXhlcywgbl9uZWlnaGJvcnNfdmFscyk6XG4gICAgcmVkdWNlciA9IHVtYXAuVU1BUChuX25laWdoYm9ycz1uX25laWdoLCBtaW5fZGlzdD0wLjEsXG4gICAgICAgICAgICAgICAgICAgICAgICByYW5kb21fc3RhdGU9NDIsIG5fY29tcG9uZW50cz0yKVxuICAgIFhfdW1hcCA9IHJlZHVjZXIuZml0X3RyYW5zZm9ybShYX3BjYSlcbiAgICBheC5zY2F0dGVyKFhfdW1hcFs6LCAwXSwgWF91bWFwWzosIDFdLCBjPXksIGNtYXA9XHUwMDI3dGFiMTBcdTAwMjcsIHM9MywgYWxwaGE9MC43KVxuICAgIGF4LnNldF90aXRsZShmXHUwMDI3bl9uZWlnaGJvcnM9e25fbmVpZ2h9XHUwMDI3KVxuICAgIGF4LmF4aXMoXHUwMDI3b2ZmXHUwMDI3KVxuXG5wbHQuc3VwdGl0bGUoXHUwMDI3VU1BUDogbl9uZWlnaGJvcnMgQ29udHJvbHMgTG9jYWwgdnMgR2xvYmFsIFN0cnVjdHVyZVx1MDAyNywgZm9udHNpemU9MTMpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgSHlwZXJwYXJhbWV0ZXJzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJuX25laWdoYm9ycyAoNeKAkzIwMCk6IGNvbnRyb2xzIHRoZSBiYWxhbmNlIGJldHdlZW4gbG9jYWwgYW5kIGdsb2JhbCBzdHJ1Y3R1cmUuIFNtYWxsIOKGkiBmaW5lIGxvY2FsIGRldGFpbCwgZGlzY29ubmVjdGVkIGNsdXN0ZXJzLiBMYXJnZSDihpIgZ2xvYmFsIHRvcG9sb2d5IHByZXNlcnZlZCBidXQgbG9jYWwgZGV0YWlsIHNtb290aGVkLiIsIm1pbl9kaXN0ICgwLjDigJMwLjkpOiBjb250cm9scyBob3cgdGlnaHRseSBwb2ludHMgYXJlIHBhY2tlZCBpbiB0aGUgZW1iZWRkaW5nLiBTbWFsbCDihpIgdGlnaHQgY2x1c3RlcnMuIExhcmdlIOKGkiB1bmlmb3JtLCBzcHJlYWQtb3V0IGxheW91dC4iLCJtZXRyaWM6IHRoZSBkaXN0YW5jZSBtZXRyaWMgaW4gaW5wdXQgc3BhY2UuIENvc2luZSBmb3IgdGV4dC9lbWJlZGRpbmdzLCBldWNsaWRlYW4gZm9yIGltYWdlcywgY29ycmVsYXRpb24gZm9yIHRpbWUtc2VyaWVzLiIsIm5fY29tcG9uZW50czogdXN1YWxseSAyIGZvciB2aXN1YWxpc2F0aW9uLCBidXQgVU1BUCBpcyBlZmZlY3RpdmUgZm9yIGhpZ2hlci1kaW1lbnNpb25hbCBwcmVwcm9jZXNzaW5nIChlLmcuIDEw4oCTNTAgZGltcyBiZWZvcmUgY2x1c3RlcmluZykuIiwibl9lcG9jaHM6IG1vcmUgZXBvY2hzIOKGkiBtb3JlIHJlZmluZWQgZW1iZWRkaW5nLiBEZWZhdWx0IDIwMCAoc21hbGwgZGF0YSkgb3IgNTAwIChsYXJnZSBkYXRhKS4iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6Ikh5cGVycGFyYW1ldGVyIFN0YXJ0aW5nIFBvaW50cyIsImNvbnRlbnQiOiJGb3IgdmlzdWFsaXNhdGlvbjogbl9uZWlnaGJvcnM9MTUsIG1pbl9kaXN0PTAuMSwgbWV0cmljPVx1MDAyN2V1Y2xpZGVhblx1MDAyNy4gRm9yIGRvd25zdHJlYW0gY2x1c3RlcmluZzogbl9uZWlnaGJvcnM9MzAsIG1pbl9kaXN0PTAuMCB0byBwcm9kdWNlIGNvbXBhY3QgY2x1c3RlcnMuIEZvciBwcmVzZXJ2aW5nIGdsb2JhbCBzdHJ1Y3R1cmU6IG5fbmVpZ2hib3JzPTUw4oCTMTAwLiBBbHdheXMgcHJlLXJlZHVjZSB3aXRoIFBDQSB0byA1MCBkaW1zIGJlZm9yZSBVTUFQIHdoZW4gaW5wdXQgZGltZW5zaW9uYWxpdHkgaXMgXHUwMDNlIDEwMC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVTUFQIHZzIHQtU05FOiBTcGVlZCBhbmQgR2xvYmFsIFN0cnVjdHVyZSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0aW1lXG5pbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0XG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IGZldGNoX29wZW5tbFxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgUENBXG5mcm9tIHNrbGVhcm4ubWFuaWZvbGQgaW1wb3J0IFRTTkVcbmltcG9ydCB1bWFwXG5cbm1uaXN0ID0gZmV0Y2hfb3Blbm1sKFx1MDAyN21uaXN0Xzc4NFx1MDAyNywgdmVyc2lvbj0xLCBhc19mcmFtZT1GYWxzZSlcblggPSBtbmlzdC5kYXRhWzoxMDAwMF0uYXN0eXBlKGZsb2F0KVxueSA9IG1uaXN0LnRhcmdldFs6MTAwMDBdLmFzdHlwZShpbnQpXG5YID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG5YX3BjYSA9IFBDQShuX2NvbXBvbmVudHM9NTAsIHJhbmRvbV9zdGF0ZT00MikuZml0X3RyYW5zZm9ybShYKVxuXG50MCA9IHRpbWUudGltZSgpXG5YX3RzbmUgPSBUU05FKG5fY29tcG9uZW50cz0yLCBwZXJwbGV4aXR5PTMwLCByYW5kb21fc3RhdGU9NDIsXG4gICAgICAgICAgICAgIG5faXRlcj01MDApLmZpdF90cmFuc2Zvcm0oWF9wY2EpXG50c25lX3QgPSB0aW1lLnRpbWUoKSAtIHQwXG5wcmludChmXHUwMDI3dC1TTkU6IHt0c25lX3Q6LjFmfXNcdTAwMjcpXG5cbnQwID0gdGltZS50aW1lKClcblhfdW1hcCA9IHVtYXAuVU1BUChuX25laWdoYm9ycz0xNSwgbWluX2Rpc3Q9MC4xLCByYW5kb21fc3RhdGU9NDIpLmZpdF90cmFuc2Zvcm0oWF9wY2EpXG51bWFwX3QgPSB0aW1lLnRpbWUoKSAtIHQwXG5wcmludChmXHUwMDI3VU1BUDoge3VtYXBfdDouMWZ9cyAgKHNwZWVkdXA6IHt0c25lX3QgLyB1bWFwX3Q6LjFmfXgpXHUwMDI3KVxuXG5maWcsIChheDEsIGF4MikgPSBwbHQuc3VicGxvdHMoMSwgMiwgZmlnc2l6ZT0oMTQsIDUpKVxuYXgxLnNjYXR0ZXIoWF90c25lWzosIDBdLCBYX3RzbmVbOiwgMV0sIGM9eSwgY21hcD1cdTAwMjd0YWIxMFx1MDAyNywgcz0yLCBhbHBoYT0wLjUpXG5heDEuc2V0X3RpdGxlKGZcdTAwMjd0LVNORSAoe3RzbmVfdDouMGZ9cyk6IGdvb2QgbG9jYWwsIHBvb3IgZ2xvYmFsXHUwMDI3KVxuYXgyLnNjYXR0ZXIoWF91bWFwWzosIDBdLCBYX3VtYXBbOiwgMV0sIGM9eSwgY21hcD1cdTAwMjd0YWIxMFx1MDAyNywgcz0yLCBhbHBoYT0wLjUpXG5heDIuc2V0X3RpdGxlKGZcdTAwMjdVTUFQICh7dW1hcF90Oi4wZn1zKTogYmV0dGVyIGdsb2JhbCBzdHJ1Y3R1cmVcdTAwMjcpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdXBlcnZpc2VkIFVNQVAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVNQVAgY2FuIGluY29ycG9yYXRlIGNsYXNzIGxhYmVscyB0byBndWlkZSB0aGUgZW1iZWRkaW5nOiBzdXBlcnZpc2VkIFVNQVAgcHVsbHMgc2FtZS1jbGFzcyBwb2ludHMgdG9nZXRoZXIgYW5kIHB1c2hlcyBkaWZmZXJlbnQtY2xhc3MgcG9pbnRzIGFwYXJ0LiBUaGUgZW1iZWRkaW5nIGJlY29tZXMgbW9yZSBjbGFzcy1kaXNjcmltaW5hdGl2ZSwgbWFraW5nIGl0IHVzZWZ1bCBhcyBhIGZlYXR1cmUgZXh0cmFjdG9yIGJlZm9yZSBjbGFzc2lmaWNhdGlvbi4gQSBtZXRyaWMgcGFyYW1ldGVyIGNvbnRyb2xzIHRoZSByZWxhdGl2ZSB3ZWlnaHQgb2Ygc3VwZXJ2aXNlZCB2cyB1bnN1cGVydmlzZWQgc2lnbmFsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9kaWdpdHNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuaW1wb3J0IHVtYXBcblxuWCwgeSA9IGxvYWRfZGlnaXRzKHJldHVybl9YX3k9VHJ1ZSlcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblhfdHJhaW4sIFhfdGVzdCwgeV90cmFpbiwgeV90ZXN0ID0gdHJhaW5fdGVzdF9zcGxpdChcbiAgICBYLCB5LCB0ZXN0X3NpemU9MC4zLCByYW5kb21fc3RhdGU9NDIpXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAzLCBmaWdzaXplPSgxOCwgNSkpXG5cbiMgVW5zdXBlcnZpc2VkIFVNQVBcbnVuc3VwID0gdW1hcC5VTUFQKG5fbmVpZ2hib3JzPTE1LCBtaW5fZGlzdD0wLjEsIHJhbmRvbV9zdGF0ZT00MilcblhfdHJfdSA9IHVuc3VwLmZpdF90cmFuc2Zvcm0oWF90cmFpbilcblhfdGVfdSA9IHVuc3VwLnRyYW5zZm9ybShYX3Rlc3QpXG5heGVzWzBdLnNjYXR0ZXIoWF90cl91WzosIDBdLCBYX3RyX3VbOiwgMV0sIGM9eV90cmFpbiwgY21hcD1cdTAwMjd0YWIxMFx1MDAyNywgcz0xMCwgYWxwaGE9MC42KVxuYXhlc1swXS5zZXRfdGl0bGUoXHUwMDI3VW5zdXBlcnZpc2VkIFVNQVAgKHRyYWluKVx1MDAyNylcblxuIyBTdXBlcnZpc2VkIFVNQVAgKHBhc3MgeSB0byBmaXQpXG5zdXAgPSB1bWFwLlVNQVAobl9uZWlnaGJvcnM9MTUsIG1pbl9kaXN0PTAuMSwgcmFuZG9tX3N0YXRlPTQyKVxuWF90cl9zID0gc3VwLmZpdF90cmFuc2Zvcm0oWF90cmFpbiwgeT15X3RyYWluKSAgIyBsYWJlbHMgZ3VpZGUgZW1iZWRkaW5nXG5YX3RlX3MgPSBzdXAudHJhbnNmb3JtKFhfdGVzdClcbmF4ZXNbMV0uc2NhdHRlcihYX3RyX3NbOiwgMF0sIFhfdHJfc1s6LCAxXSwgYz15X3RyYWluLCBjbWFwPVx1MDAyN3RhYjEwXHUwMDI3LCBzPTEwLCBhbHBoYT0wLjYpXG5heGVzWzFdLnNldF90aXRsZShcdTAwMjdTdXBlcnZpc2VkIFVNQVAgKHRyYWluKSDigJQgY2xlYW5lciBzZXBhcmF0aW9uXHUwMDI3KVxuYXhlc1syXS5zY2F0dGVyKFhfdGVfc1s6LCAwXSwgWF90ZV9zWzosIDFdLCBjPXlfdGVzdCwgY21hcD1cdTAwMjd0YWIxMFx1MDAyNywgcz0xMCwgYWxwaGE9MC42KVxuYXhlc1syXS5zZXRfdGl0bGUoXHUwMDI3U3VwZXJ2aXNlZCBVTUFQICh0ZXN0KSDigJQgb3V0LW9mLXNhbXBsZVx1MDAyNylcblxucGx0LnN1cHRpdGxlKFx1MDAyN1N1cGVydmlzZWQgdnMgVW5zdXBlcnZpc2VkIFVNQVBcdTAwMjcpXG5wbHQudGlnaHRfbGF5b3V0KClcbnBsdC5zaG93KCkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXJhbWV0cmljIFVNQVAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIFVNQVAgaXMgYSBub24tcGFyYW1ldHJpYyBlbWJlZGRpbmcg4oCUIGl0IGNhbm5vdCBkaXJlY3RseSBlbWJlZCBuZXcgcG9pbnRzIHdpdGhvdXQgcmVmaXR0aW5nLiBQYXJhbWV0cmljIFVNQVAgdHJhaW5zIGEgbmV1cmFsIG5ldHdvcmsgZW5jb2RlciB0aGF0IGFwcHJveGltYXRlcyB0aGUgVU1BUCBtYXBwaW5nLCBlbmFibGluZyBmYXN0IG91dC1vZi1zYW1wbGUgaW5mZXJlbmNlIGFuZCBwcm92aWRpbmcgYSBjb250aW51b3VzLCBkaWZmZXJlbnRpYWJsZSBsYXRlbnQgc3BhY2UuIEl0IGlzIHBhcnRpY3VsYXJseSB1c2VmdWwgZm9yIG9ubGluZSBsZWFybmluZyBzY2VuYXJpb3Mgb3Igd2hlbiBjb21iaW5pbmcgZGltZW5zaW9uYWxpdHkgcmVkdWN0aW9uIHdpdGggZG93bnN0cmVhbSBuZXVyYWwgbW9kZWxzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbG9hZF9kaWdpdHNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5YLCB5ID0gbG9hZF9kaWdpdHMocmV0dXJuX1hfeT1UcnVlKVxuWCA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKS5hc3R5cGUobnAuZmxvYXQzMilcblxudHJ5OlxuICAgIGltcG9ydCB0ZW5zb3JmbG93IGFzIHRmXG4gICAgZnJvbSB1bWFwLnBhcmFtZXRyaWNfdW1hcCBpbXBvcnQgUGFyYW1ldHJpY1VNQVBcblxuICAgIGVuY29kZXIgPSB0Zi5rZXJhcy5TZXF1ZW50aWFsKFtcbiAgICAgICAgdGYua2VyYXMubGF5ZXJzLkRlbnNlKDEyOCwgYWN0aXZhdGlvbj1cdTAwMjdyZWx1XHUwMDI3LCBpbnB1dF9zaGFwZT0oNjQsKSksXG4gICAgICAgIHRmLmtlcmFzLmxheWVycy5EZW5zZSg2NCwgYWN0aXZhdGlvbj1cdTAwMjdyZWx1XHUwMDI3KSxcbiAgICAgICAgdGYua2VyYXMubGF5ZXJzLkRlbnNlKDIpXG4gICAgXSlcblxuICAgIHBfdW1hcCA9IFBhcmFtZXRyaWNVTUFQKFxuICAgICAgICBlbmNvZGVyPWVuY29kZXIsXG4gICAgICAgIG5fY29tcG9uZW50cz0yLFxuICAgICAgICBuX2Vwb2Nocz01MCxcbiAgICAgICAgYmF0Y2hfc2l6ZT02NCxcbiAgICAgICAgcmFuZG9tX3N0YXRlPTQyXG4gICAgKVxuICAgIFhfZW1iID0gcF91bWFwLmZpdF90cmFuc2Zvcm0oWClcbiAgICBwcmludChmXHUwMDI3RW1iZWRkaW5nIHNoYXBlOiB7WF9lbWIuc2hhcGV9XHUwMDI3KVxuXG4gICAgIyBGYXN0IG91dC1vZi1zYW1wbGUgaW5mZXJlbmNlIHZpYSBuZXVyYWwgbmV0d29ya1xuICAgIFhfbmV3X2VtYiA9IHBfdW1hcC50cmFuc2Zvcm0oWFs6MjBdKVxuICAgIHByaW50KGZcdTAwMjdOZXcgcG9pbnRzIHNoYXBlOiB7WF9uZXdfZW1iLnNoYXBlfVx1MDAyNylcblxuICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oNywgNikpXG4gICAgcGx0LnNjYXR0ZXIoWF9lbWJbOiwgMF0sIFhfZW1iWzosIDFdLCBjPXksIGNtYXA9XHUwMDI3dGFiMTBcdTAwMjcsIHM9MTUpXG4gICAgcGx0LnRpdGxlKFx1MDAyN1BhcmFtZXRyaWMgVU1BUCAobmV1cmFsIGVuY29kZXIpXHUwMDI3KVxuICAgIHBsdC5jb2xvcmJhcihsYWJlbD1cdTAwMjdEaWdpdCBjbGFzc1x1MDAyNylcbiAgICBwbHQuc2hvdygpXG5leGNlcHQgSW1wb3J0RXJyb3I6XG4gICAgcHJpbnQoXHUwMDI3cGlwIGluc3RhbGwgdW1hcC1sZWFybltwYXJhbWV0cmljX3VtYXBdIHRlbnNvcmZsb3dcdTAwMjcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiUENBIiwidC1TTkUiLCJVTUFQIl0sInJvd3MiOltbIkdsb2JhbCBzdHJ1Y3R1cmUiLCJFeGNlbGxlbnQiLCJQb29yIiwiR29vZCJdLFsiTG9jYWwgc3RydWN0dXJlIiwiTW9kZXJhdGUiLCJFeGNlbGxlbnQiLCJFeGNlbGxlbnQiXSxbIlNwZWVkIChuPTUwaykiLCJGYXN0IiwiU2xvdyAofmhvdXJzKSIsIkZhc3QgKH5taW51dGVzKSJdLFsiRGV0ZXJtaW5pc3RpYyIsIlllcyIsIk5vIiwiWWVzIChmaXhlZCBzZWVkKSJdLFsiTmV3IHBvaW50IHByb2plY3Rpb24iLCJZZXMiLCJObyIsIlllcyJdLFsiQ2x1c3RlciBzZXBhcmF0aW9uIiwiUG9vciIsIkdvb2QiLCJWZXJ5IGdvb2QiXSxbIlNjYWxhYmlsaXR5IiwiWWVzIChzcGFyc2UgU1ZEKSIsIk5vIiwiWWVzIChhcHByb3hpbWF0ZSBOTikiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlVNQVAgZm9yIERvd25zdHJlYW0gVGFza3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlVubGlrZSB0LVNORSwgVU1BUCBjYW4gZW1iZWQgbmV3ICh1bnNlZW4pIHBvaW50cyB1c2luZyB0aGUgdHJhbnNmb3JtKCkgbWV0aG9kIHdpdGhvdXQgcmVmaXR0aW5nLiBUaGlzIG1ha2VzIGl0IHZpYWJsZSBhcyBhIHByZXByb2Nlc3Npbmcgc3RlcCBiZWZvcmUgY2xhc3NpZmljYXRpb24gb3IgY2x1c3RlcmluZzogZml0IG9uIHRyYWluaW5nIGRhdGEsIHRyYW5zZm9ybSB0ZXN0IGRhdGEsIHRoZW4gdHJhaW4gYSBjbGFzc2lmaWVyIGluIHRoZSBsb3ctZGltZW5zaW9uYWwgc3BhY2UuIEZvciBjbHVzdGVyaW5nLCB1c2UgbWluX2Rpc3Q9MC4wIGFuZCBuX25laWdoYm9ycz0zMCB0byBwcm9kdWNlIGNvbXBhY3QsIHdlbGwtc2VwYXJhdGVkIGNsdXN0ZXJzIHRoYXQgZmVlZCBjbGVhbmx5IGludG8gSERCU0NBTiBvciBrLW1lYW5zLiJ9LHsidHlwZSI6ImRpdmlkZXIifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlJlcHJvZHVjaWJpbGl0eSIsImNvbnRlbnQiOiJVTUFQIGlzIGRldGVybWluaXN0aWMgd2hlbiByYW5kb21fc3RhdGUgaXMgc2V0IEFORCB3aGVuIHVzaW5nIGEgc2luZ2xlIHRocmVhZCAobl9qb2JzPTEpLiBNdWx0aS10aHJlYWRlZCBydW5zIG1heSBwcm9kdWNlIHNsaWdodGx5IGRpZmZlcmVudCByZXN1bHRzLiBGb3IgcHVibGljYXRpb24tcXVhbGl0eSBmaWd1cmVzLCBhbHdheXMgc2V0IHJhbmRvbV9zdGF0ZSBhbmQgbl9qb2JzPTEsIG9yIHNhdmUgdGhlIGVtYmVkZGluZyBhbmQgcmVsb2FkIGl0LiJ9XQ=="
---
# UMAP — Topological Data Analysis and Fuzzy Simplicial Sets

UMAP (Uniform Manifold Approximation and Projection) is grounded in algebraic topology and Riemannian geometry rather than probabilistic modelling. It outperforms t-SNE on speed, global structure preservation, and scalability, and it supports out-of-sample projection — making it useful beyond visualisation.

## Fuzzy Simplicial Sets

UMAP models the high-dimensional data as a fuzzy simplicial set: each point xᵢ defines an open ball of radius ρᵢ (distance to nearest neighbour, making the local metric adaptive). Overlap between balls defines fuzzy set membership: μᵢⱼ = exp(-(dᵢⱼ - ρᵢ)/σᵢ), where σᵢ is tuned so that Σⱼ μᵢⱼ = log₂(n_neighbors). The union of these local fuzzy sets forms the high-dimensional topological representation.

## Cross-Entropy Optimisation

UMAP optimises the low-dimensional layout by minimising the cross-entropy between the high-dimensional fuzzy graph and a low-dimensional counterpart: C = Σᵢⱼ [μᵢⱼ log(μᵢⱼ/νᵢⱼ) + (1-μᵢⱼ) log((1-μᵢⱼ)/(1-νᵢⱼ))], where νᵢⱼ = (1 + a‖yᵢ-yⱼ‖²ᵇ)⁻¹ is the low-dim similarity. Unlike t-SNE, the repulsive term (1-μ)(1-ν) is explicitly included and balanced. Optimisation uses stochastic gradient descent with negative sampling.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import umap  # pip install umap-learn

mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X = mnist.data[:5000].astype(float)
y = mnist.target[:5000].astype(int)
X = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=50, random_state=42).fit_transform(X)

# n_neighbors controls local vs global tradeoff
n_neighbors_vals = [5, 15, 50, 200]
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

for ax, n_neigh in zip(axes, n_neighbors_vals):
    reducer = umap.UMAP(n_neighbors=n_neigh, min_dist=0.1,
                        random_state=42, n_components=2)
    X_umap = reducer.fit_transform(X_pca)
    ax.scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='tab10', s=3, alpha=0.7)
    ax.set_title(f'n_neighbors={n_neigh}')
    ax.axis('off')

plt.suptitle('UMAP: n_neighbors Controls Local vs Global Structure', fontsize=13)
plt.tight_layout()
plt.show()
```

## Key Hyperparameters

- n_neighbors (5–200): controls the balance between local and global structure. Small → fine local detail, disconnected clusters. Large → global topology preserved but local detail smoothed.
- min_dist (0.0–0.9): controls how tightly points are packed in the embedding. Small → tight clusters. Large → uniform, spread-out layout.
- metric: the distance metric in input space. Cosine for text/embeddings, euclidean for images, correlation for time-series.
- n_components: usually 2 for visualisation, but UMAP is effective for higher-dimensional preprocessing (e.g. 10–50 dims before clustering).
- n_epochs: more epochs → more refined embedding. Default 200 (small data) or 500 (large data).

> **Hyperparameter Starting Points**: For visualisation: n_neighbors=15, min_dist=0.1, metric='euclidean'. For downstream clustering: n_neighbors=30, min_dist=0.0 to produce compact clusters. For preserving global structure: n_neighbors=50–100. Always pre-reduce with PCA to 50 dims before UMAP when input dimensionality is > 100.

## UMAP vs t-SNE: Speed and Global Structure

```python
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X = mnist.data[:10000].astype(float)
y = mnist.target[:10000].astype(int)
X = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=50, random_state=42).fit_transform(X)

t0 = time.time()
X_tsne = TSNE(n_components=2, perplexity=30, random_state=42,
              n_iter=500).fit_transform(X_pca)
tsne_t = time.time() - t0
print(f't-SNE: {tsne_t:.1f}s')

t0 = time.time()
X_umap = umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=42).fit_transform(X_pca)
umap_t = time.time() - t0
print(f'UMAP: {umap_t:.1f}s  (speedup: {tsne_t / umap_t:.1f}x)')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', s=2, alpha=0.5)
ax1.set_title(f't-SNE ({tsne_t:.0f}s): good local, poor global')
ax2.scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='tab10', s=2, alpha=0.5)
ax2.set_title(f'UMAP ({umap_t:.0f}s): better global structure')
plt.tight_layout()
plt.show()
```

## Supervised UMAP

UMAP can incorporate class labels to guide the embedding: supervised UMAP pulls same-class points together and pushes different-class points apart. The embedding becomes more class-discriminative, making it useful as a feature extractor before classification. A metric parameter controls the relative weight of supervised vs unsupervised signal.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import umap

X, y = load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Unsupervised UMAP
unsup = umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=42)
X_tr_u = unsup.fit_transform(X_train)
X_te_u = unsup.transform(X_test)
axes[0].scatter(X_tr_u[:, 0], X_tr_u[:, 1], c=y_train, cmap='tab10', s=10, alpha=0.6)
axes[0].set_title('Unsupervised UMAP (train)')

# Supervised UMAP (pass y to fit)
sup = umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=42)
X_tr_s = sup.fit_transform(X_train, y=y_train)  # labels guide embedding
X_te_s = sup.transform(X_test)
axes[1].scatter(X_tr_s[:, 0], X_tr_s[:, 1], c=y_train, cmap='tab10', s=10, alpha=0.6)
axes[1].set_title('Supervised UMAP (train) — cleaner separation')
axes[2].scatter(X_te_s[:, 0], X_te_s[:, 1], c=y_test, cmap='tab10', s=10, alpha=0.6)
axes[2].set_title('Supervised UMAP (test) — out-of-sample')

plt.suptitle('Supervised vs Unsupervised UMAP')
plt.tight_layout()
plt.show()
```

## Parametric UMAP

Standard UMAP is a non-parametric embedding — it cannot directly embed new points without refitting. Parametric UMAP trains a neural network encoder that approximates the UMAP mapping, enabling fast out-of-sample inference and providing a continuous, differentiable latent space. It is particularly useful for online learning scenarios or when combining dimensionality reduction with downstream neural models.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler

X, y = load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X).astype(np.float32)

try:
    import tensorflow as tf
    from umap.parametric_umap import ParametricUMAP

    encoder = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(64,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(2)
    ])

    p_umap = ParametricUMAP(
        encoder=encoder,
        n_components=2,
        n_epochs=50,
        batch_size=64,
        random_state=42
    )
    X_emb = p_umap.fit_transform(X)
    print(f'Embedding shape: {X_emb.shape}')

    # Fast out-of-sample inference via neural network
    X_new_emb = p_umap.transform(X[:20])
    print(f'New points shape: {X_new_emb.shape}')

    plt.figure(figsize=(7, 6))
    plt.scatter(X_emb[:, 0], X_emb[:, 1], c=y, cmap='tab10', s=15)
    plt.title('Parametric UMAP (neural encoder)')
    plt.colorbar(label='Digit class')
    plt.show()
except ImportError:
    print('pip install umap-learn[parametric_umap] tensorflow')
```

| Property | PCA | t-SNE | UMAP |
| --- | --- | --- | --- |
| Global structure | Excellent | Poor | Good |
| Local structure | Moderate | Excellent | Excellent |
| Speed (n=50k) | Fast | Slow (~hours) | Fast (~minutes) |
| Deterministic | Yes | No | Yes (fixed seed) |
| New point projection | Yes | No | Yes |
| Cluster separation | Poor | Good | Very good |
| Scalability | Yes (sparse SVD) | No | Yes (approximate NN) |

## UMAP for Downstream Tasks

Unlike t-SNE, UMAP can embed new (unseen) points using the transform() method without refitting. This makes it viable as a preprocessing step before classification or clustering: fit on training data, transform test data, then train a classifier in the low-dimensional space. For clustering, use min_dist=0.0 and n_neighbors=30 to produce compact, well-separated clusters that feed cleanly into HDBSCAN or k-means.

---

> **Reproducibility**: UMAP is deterministic when random_state is set AND when using a single thread (n_jobs=1). Multi-threaded runs may produce slightly different results. For publication-quality figures, always set random_state and n_jobs=1, or save the embedding and reload it.

