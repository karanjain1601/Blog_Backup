---
title: "Hierarchical Clustering — Linkage Methods and Dendrograms"
slug: "hierarchical-clustering"
description: "Master agglomerative hierarchical clustering: single, complete, average, and Ward linkage criteria, reading and cutting dendrograms, cophenetic correlation coefficient for evaluating linkage quality, and comparison with k-means on compact and chained data."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSGllcmFyY2hpY2FsIGNsdXN0ZXJpbmcgYnVpbGRzIGEgdHJlZSBvZiBuZXN0ZWQgcGFydGl0aW9ucyB3aXRob3V0IHJlcXVpcmluZyBrIHRvIGJlIHNwZWNpZmllZCBpbiBhZHZhbmNlLiBUaGUgZGVuZHJvZ3JhbSByZWNvcmRzIHRoZSBlbnRpcmUgbWVyZ2UgaGlzdG9yeSDigJQgeW91IGNob29zZSB0aGUgbnVtYmVyIG9mIGNsdXN0ZXJzIHBvc3QtaG9jIGJ5IGN1dHRpbmcgdGhlIHRyZWUgYXQgYW55IGhlaWdodC4gQWdnbG9tZXJhdGl2ZSAoYm90dG9tLXVwKSBoaWVyYXJjaGljYWwgY2x1c3RlcmluZyBzdGFydHMgd2l0aCBlYWNoIHBvaW50IGFzIGl0cyBvd24gY2x1c3RlciBhbmQgZ3JlZWRpbHkgbWVyZ2VzIHRoZSB0d28gY2xvc2VzdCBjbHVzdGVycyBhdCBlYWNoIHN0ZXAuIFRoZSBjaG9pY2Ugb2YgbGlua2FnZSBjcml0ZXJpb24g4oCUIGhvdyBpbnRlci1jbHVzdGVyIGRpc3RhbmNlIGlzIG1lYXN1cmVkIOKAlCBoYXMgYSBtYWpvciBlZmZlY3Qgb24gY2x1c3RlciBzaGFwZSBhbmQgcXVhbGl0eS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBZ2dsb21lcmF0aXZlIEFsZ29yaXRobSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhcnRpbmcgd2l0aCBuIHNpbmdsZXRvbiBjbHVzdGVycywgYXQgZWFjaCBzdGVwIGZpbmQgdGhlIHBhaXIgb2YgY2x1c3RlcnMgKEPhtaIsIEPisbwpIHdpdGggdGhlIHNtYWxsZXN0IGludGVyLWNsdXN0ZXIgZGlzdGFuY2UgZChD4bWiLEPisbwpIChkZXRlcm1pbmVkIGJ5IHRoZSBsaW5rYWdlIGNyaXRlcmlvbiksIG1lcmdlIHRoZW0gaW50byBvbmUgY2x1c3RlciwgdXBkYXRlIHRoZSBkaXN0YW5jZSBtYXRyaXgsIGFuZCByZXBlYXQgdW50aWwgb25lIGNsdXN0ZXIgcmVtYWlucy4gVGhlIG1lcmdlIGhpc3RvcnkgaXMgcmVjb3JkZWQgYXMgYSBkZW5kcm9ncmFtOiBlYWNoIGludGVybmFsIG5vZGUgcmVwcmVzZW50cyBhIG1lcmdlLCBpdHMgaGVpZ2h0IGlzIHRoZSBkaXN0YW5jZSBhdCB3aGljaCB0aGUgbWVyZ2Ugb2NjdXJyZWQsIGFuZCBjdXR0aW5nIHRoZSB0cmVlIGhvcml6b250YWxseSBhdCBoZWlnaHQgaCB5aWVsZHMgdGhlIGZsYXQgY2x1c3RlcmluZyBhdCB0aGF0IHJlc29sdXRpb24uIFRoZSBuYWl2ZSBpbXBsZW1lbnRhdGlvbiBpcyBPKG7CsykgYnV0IHRoZSBwcmlvcml0eS1xdWV1ZSB2ZXJzaW9uIGlzIE8obsKyIGxvZyBuKSBmb3IgbW9zdCBsaW5rYWdlcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcblxuZGVmIHNpbmdsZV9saW5rYWdlX2FnZ2xvbWVyYXRpdmUoWCk6XG4gICAgXCJcIlwiU2luZ2xlIGxpbmthZ2UgaGllcmFyY2hpY2FsIGNsdXN0ZXJpbmcgZnJvbSBzY3JhdGNoLlwiXCJcIlxuICAgIG4gPSBYLnNoYXBlWzBdXG4gICAgIyBEaXN0YW5jZSBtYXRyaXhcbiAgICBkaXN0cyA9IG5wLnNxcnQoKChYWzosIE5vbmUsIDpdIC0gWFtOb25lLCA6LCA6XSkgKiogMikuc3VtKGF4aXM9MikpXG4gICAgbnAuZmlsbF9kaWFnb25hbChkaXN0cywgbnAuaW5mKVxuICAgICMgVHJhY2sgY2x1c3RlciBtZW1iZXJzaGlwXG4gICAgY2x1c3RlcnMgPSBbe2l9IGZvciBpIGluIHJhbmdlKG4pXVxuICAgIGFjdGl2ZSA9IGxpc3QocmFuZ2UobikpXG4gICAgbWVyZ2VfaGlzdG9yeSA9IFtdICAjIChjbHVzdGVyX2FfaWR4LCBjbHVzdGVyX2JfaWR4LCBkaXN0YW5jZSlcbiAgICBmb3Igc3RlcCBpbiByYW5nZShuIC0gMSk6XG4gICAgICAgICMgRmluZCBtaW5pbXVtIGludGVyLWNsdXN0ZXIgZGlzdGFuY2UgdXNpbmcgYWN0aXZlIGNsdXN0ZXIgcmVwcmVzZW50YXRpdmVzXG4gICAgICAgIGJlc3RfZCwgYmVzdF9pLCBiZXN0X2ogPSBucC5pbmYsIC0xLCAtMVxuICAgICAgICBmb3IgaWR4X2EgaW4gcmFuZ2UobGVuKGFjdGl2ZSkpOlxuICAgICAgICAgICAgZm9yIGlkeF9iIGluIHJhbmdlKGlkeF9hICsgMSwgbGVuKGFjdGl2ZSkpOlxuICAgICAgICAgICAgICAgIGFfcHRzID0gbGlzdChjbHVzdGVyc1thY3RpdmVbaWR4X2FdXSlcbiAgICAgICAgICAgICAgICBiX3B0cyA9IGxpc3QoY2x1c3RlcnNbYWN0aXZlW2lkeF9iXV0pXG4gICAgICAgICAgICAgICAgIyBTaW5nbGUgbGlua2FnZTogbWluaW11bSBwYWlyd2lzZSBkaXN0YW5jZVxuICAgICAgICAgICAgICAgIGQgPSBkaXN0c1tucC5peF8oYV9wdHMsIGJfcHRzKV0ubWluKClcbiAgICAgICAgICAgICAgICBpZiBkIFx1MDAzYyBiZXN0X2Q6XG4gICAgICAgICAgICAgICAgICAgIGJlc3RfZCwgYmVzdF9pLCBiZXN0X2ogPSBkLCBpZHhfYSwgaWR4X2JcbiAgICAgICAgY2ksIGNqID0gYWN0aXZlW2Jlc3RfaV0sIGFjdGl2ZVtiZXN0X2pdXG4gICAgICAgIG1lcmdlX2hpc3RvcnkuYXBwZW5kKChjaSwgY2osIGJlc3RfZCkpXG4gICAgICAgIGNsdXN0ZXJzW2NpXSA9IGNsdXN0ZXJzW2NpXSB8IGNsdXN0ZXJzW2NqXVxuICAgICAgICBhY3RpdmUucG9wKGJlc3RfailcbiAgICByZXR1cm4gbWVyZ2VfaGlzdG9yeVxuXG5YLCB5ID0gbWFrZV9ibG9icyhuX3NhbXBsZXM9MTIsIGNlbnRlcnM9MywgcmFuZG9tX3N0YXRlPTApXG5oaXN0b3J5ID0gc2luZ2xlX2xpbmthZ2VfYWdnbG9tZXJhdGl2ZShYKVxucHJpbnQoXCJNZXJnZSBoaXN0b3J5IChjbHVzdGVyX2EsIGNsdXN0ZXJfYiwgZGlzdGFuY2UpOlwiKVxuZm9yIGEsIGIsIGQgaW4gaGlzdG9yeVs6Nl06XG4gICAgcHJpbnQoZlwiICBjbHVzdGVycyB7YX0gKyB7Yn0gYXQgZGlzdGFuY2Uge2Q6LjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbmthZ2UgQ3JpdGVyaWEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBsaW5rYWdlIGNyaXRlcmlvbiBkZWZpbmVzIGhvdyB0aGUgZGlzdGFuY2UgYmV0d2VlbiB0d28gY2x1c3RlcnMgaXMgY29tcHV0ZWQgZnJvbSBwYWlyd2lzZSBwb2ludCBkaXN0YW5jZXMuIFNpbmdsZSBsaW5rYWdlIGQoQSxCKSA9IG1pbl97YeKIiEEsYuKIiEJ9IGRpc3QoYSxiKSB0ZW5kcyB0byBwcm9kdWNlIGVsb25nYXRlZCwgY2hhaW5lZCBjbHVzdGVycyAoXHUwMDI3Y2hhaW5pbmcgZWZmZWN0XHUwMDI3KS4gQ29tcGxldGUgbGlua2FnZSBkKEEsQikgPSBtYXhfe2HiiIhBLGLiiIhCfSBkaXN0KGEsYikgZm9yY2VzIGNvbXBhY3QgY2x1c3RlcnMgYnV0IHNwbGl0cyBsYXJnZSBkaWZmdXNlIGNsdXN0ZXJzLiBBdmVyYWdlIGxpbmthZ2UgKFVQR01BKSBkKEEsQikgPSAoMS98QXx8QnwpIM6jIGRpc3QoYSxiKSBpcyBhIGJhbGFuY2VkIGNvbXByb21pc2UuIFdhcmQgbGlua2FnZSBtaW5pbWl6ZXMgdGhlIGluY3JlYXNlIGluIHRvdGFsIHdpdGhpbi1jbHVzdGVyIHZhcmlhbmNlIGF0IGVhY2ggbWVyZ2U6IM6UKEEsQikgPSB8QXx8QnwvKHxBfCt8QnwpIMOXIOKAls68X0Eg4oiSIM68X0LigJbCsiDigJQgZXF1aXZhbGVudCB0byBrLW1lYW5zIG9iamVjdGl2ZSwgdHlwaWNhbGx5IHByb2R1Y2luZyB0aGUgbW9zdCBjb21wYWN0IGNsdXN0ZXJzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJMaW5rYWdlIiwiRGlzdGFuY2UgRm9ybXVsYSIsIkNoYWluIEVmZmVjdCIsIk91dGxpZXIgU2Vuc2l0aXZlIiwiVHlwaWNhbCBVc2UiXSwicm93cyI6W1siU2luZ2xlIiwibWluIHBhaXJ3aXNlIGRpc3RhbmNlIiwiWWVzIOKAlCBwcm9uZSB0byBjaGFpbmluZyIsIlllcyDigJQgb25lIGJyaWRnZSBtZXJnZXMgY2x1c3RlcnMiLCJOb24tY29udmV4IGNoYWlucywgZGVuZHJvZ3JhbSBhbmFseXNpcyJdLFsiQ29tcGxldGUiLCJtYXggcGFpcndpc2UgZGlzdGFuY2UiLCJObyDigJQgY29tcGFjdCBjbHVzdGVycyIsIlllcyDigJQgb3V0bGllcnMgZGVsYXkgbWVyZ2VzIiwiQ29tcGFjdCwgc2ltaWxhcmx5LXNpemVkIGNsdXN0ZXJzIl0sWyJBdmVyYWdlIChVUEdNQSkiLCJtZWFuIHBhaXJ3aXNlIGRpc3RhbmNlIiwiTWlsZCIsIk1vZGVyYXRlIiwiR2VuZXJhbCBwdXJwb3NlLCBiYWxhbmNlZCBjbHVzdGVycyJdLFsiV2FyZCIsIm1pbiB2YXJpYW5jZSBpbmNyZWFzZSIsIk5vIOKAlCBtb3N0IGNvbXBhY3QiLCJObyDigJQgdXNlcyBjbHVzdGVyIG1lYW5zIiwiRGVmYXVsdCBjaG9pY2UgZm9yIGNvbXBhY3QgY2x1c3RlcnMiXV19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2NpcHkuY2x1c3Rlci5oaWVyYXJjaHkgaW1wb3J0IGRlbmRyb2dyYW0sIGxpbmthZ2UsIGZjbHVzdGVyXG5mcm9tIHNjaXB5LnNwYXRpYWwuZGlzdGFuY2UgaW1wb3J0IHBkaXN0XG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5YLCB5X3RydWUgPSBtYWtlX2Jsb2JzKG5fc2FtcGxlcz0xNTAsIGNlbnRlcnM9NCwgY2x1c3Rlcl9zdGQ9MC44LCByYW5kb21fc3RhdGU9NDIpXG5YID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG5cbnByaW50KGZcIntcdTAwMjdMaW5rYWdlXHUwMDI3OjEwc30ge1x1MDAyN0FSSVx1MDAyNzpcdTAwM2U4fSB7XHUwMDI3U2lsaG91ZXR0ZVx1MDAyNzpcdTAwM2UxMn1cIilcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBhZGp1c3RlZF9yYW5kX3Njb3JlLCBzaWxob3VldHRlX3Njb3JlXG5mb3IgbWV0aG9kIGluIFtcdTAwMjdzaW5nbGVcdTAwMjcsIFx1MDAyN2NvbXBsZXRlXHUwMDI3LCBcdTAwMjdhdmVyYWdlXHUwMDI3LCBcdTAwMjd3YXJkXHUwMDI3XTpcbiAgICBaID0gbGlua2FnZShYLCBtZXRob2Q9bWV0aG9kKVxuICAgIGxhYmVscyA9IGZjbHVzdGVyKFosIHQ9NCwgY3JpdGVyaW9uPVx1MDAyN21heGNsdXN0XHUwMDI3KSAtIDFcbiAgICBhcmkgPSBhZGp1c3RlZF9yYW5kX3Njb3JlKHlfdHJ1ZSwgbGFiZWxzKVxuICAgIHNpbCA9IHNpbGhvdWV0dGVfc2NvcmUoWCwgbGFiZWxzKVxuICAgIHByaW50KGZcInttZXRob2Q6MTBzfSB7YXJpOlx1MDAzZTguNGZ9IHtzaWw6XHUwMDNlMTIuNGZ9XCIpXG5cbiMgU2hvdyBXYXJkIGRlbmRyb2dyYW0gaW5mb1xuWl93YXJkID0gbGlua2FnZShYLCBtZXRob2Q9XHUwMDI3d2FyZFx1MDAyNylcbnByaW50KGZcIlxcbldhcmQ6IGxhc3QgNSBtZXJnZSBoZWlnaHRzOiB7Wl93YXJkWy01OiwgMl0ucm91bmQoMyl9XCIpXG5wcmludChcIkxhcmdlIGdhcCBiZXR3ZWVuIGhlaWdodFstMl0gYW5kIGhlaWdodFstMV0gaW5kaWNhdGVzIG5hdHVyYWwgY2x1c3RlciBjb3VudC5cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXYXJkIExpbmthZ2UgdnMgSy1NZWFucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiV2FyZCBsaW5rYWdlIG1pbmltaXplcyB0aGUgc2FtZSBjcml0ZXJpb24gYXMgay1tZWFucyDigJQgdG90YWwgd2l0aGluLWNsdXN0ZXIgdmFyaWFuY2Ug4oCUIGJ1dCBwcm9kdWNlcyBhIGhpZXJhcmNoaWNhbCByZXN1bHQgcmF0aGVyIHRoYW4gYSBmbGF0IHBhcnRpdGlvbi4gV2FyZCBjbHVzdGVyaW5nIHRlbmRzIHRvIHByb2R1Y2Ugc2ltaWxhcmx5LXNpemVkIGNvbXBhY3QgY2x1c3RlcnMgYW5kIG9mdGVuIGdpdmVzIHJlc3VsdHMgdmVyeSBzaW1pbGFyIHRvIGstbWVhbnMuIFRoZSBhZHZhbnRhZ2Ugb2YgV2FyZCBvdmVyIGstbWVhbnMgaXMgdGhlIGRlbmRyb2dyYW06IHlvdSBjYW4gZXhwbG9yZSBkaWZmZXJlbnQgbnVtYmVycyBvZiBjbHVzdGVycyB3aXRob3V0IHJlcnVubmluZyB0aGUgYWxnb3JpdGhtLiBUaGUgZGlzYWR2YW50YWdlIGlzIHF1YWRyYXRpYyBtZW1vcnkgTyhuwrIpIGZvciB0aGUgZGlzdGFuY2UgbWF0cml4LCBsaW1pdGluZyBXYXJkIHRvIG4gXHUwMDNjIDUwLDAwMCBpbiBwcmFjdGljZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LmNsdXN0ZXIuaGllcmFyY2h5IGltcG9ydCBsaW5rYWdlLCBmY2x1c3RlclxuZnJvbSBza2xlYXJuLmNsdXN0ZXIgaW1wb3J0IEtNZWFuc1xuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2Jsb2JzXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWRqdXN0ZWRfcmFuZF9zY29yZSwgc2lsaG91ZXR0ZV9zY29yZVxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0MilcblgsIHlfdHJ1ZSA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTQwMCwgY2VudGVycz01LCBjbHVzdGVyX3N0ZD0wLjksIHJhbmRvbV9zdGF0ZT00MilcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxuWl93YXJkID0gbGlua2FnZShYLCBtZXRob2Q9XHUwMDI3d2FyZFx1MDAyNylcbnByaW50KGZcIntcdTAwMjdrXHUwMDI3Olx1MDAzZTR9IHtcdTAwMjdXYXJkIEFSSVx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0tNZWFucyBBUklcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdXYXJkIFNpbFx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0tNZWFucyBTaWxcdTAwMjc6XHUwMDNlMTJ9XCIpXG5mb3IgayBpbiBbMywgNCwgNSwgNiwgN106XG4gICAgd2FyZF9sYWJlbHMgPSBmY2x1c3RlcihaX3dhcmQsIHQ9aywgY3JpdGVyaW9uPVx1MDAyN21heGNsdXN0XHUwMDI3KSAtIDFcbiAgICBrbV9sYWJlbHMgPSBLTWVhbnMobl9jbHVzdGVycz1rLCBuX2luaXQ9MTAsIHJhbmRvbV9zdGF0ZT00MikuZml0X3ByZWRpY3QoWClcbiAgICB3YXJkX2FyaSA9IGFkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCB3YXJkX2xhYmVscylcbiAgICBrbV9hcmkgPSBhZGp1c3RlZF9yYW5kX3Njb3JlKHlfdHJ1ZSwga21fbGFiZWxzKVxuICAgIHdhcmRfc2lsID0gc2lsaG91ZXR0ZV9zY29yZShYLCB3YXJkX2xhYmVscylcbiAgICBrbV9zaWwgPSBzaWxob3VldHRlX3Njb3JlKFgsIGttX2xhYmVscylcbiAgICBwcmludChmXCJ7azpcdTAwM2U0fSB7d2FyZF9hcmk6XHUwMDNlMTAuNGZ9IHtrbV9hcmk6XHUwMDNlMTIuNGZ9IHt3YXJkX3NpbDpcdTAwM2UxMC40Zn0ge2ttX3NpbDpcdTAwM2UxMi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb3BoZW5ldGljIENvcnJlbGF0aW9uIENvZWZmaWNpZW50In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY29waGVuZXRpYyBkaXN0YW5jZSBiZXR3ZWVuIHR3byBwb2ludHMgaXMgdGhlIGhlaWdodCBpbiB0aGUgZGVuZHJvZ3JhbSBhdCB3aGljaCB0aGV5IGZpcnN0IG1lcmdlLiBUaGUgY29waGVuZXRpYyBjb3JyZWxhdGlvbiBjb2VmZmljaWVudCAoQ0NDKSBpcyB0aGUgUGVhcnNvbiBjb3JyZWxhdGlvbiBiZXR3ZWVuIHRoZSBvcmlnaW5hbCBwYWlyd2lzZSBkaXN0YW5jZXMgYW5kIHRoZSBjb3BoZW5ldGljIGRpc3RhbmNlcy4gQSBoaWdoIENDQyAoXHUwMDNlIDAuOCkgaW5kaWNhdGVzIHRoYXQgdGhlIGRlbmRyb2dyYW0gZmFpdGhmdWxseSByZXByZXNlbnRzIHRoZSB0cnVlIGRpc3RhbmNlcyDigJQgdGhlIGhpZXJhcmNoaWNhbCBzdHJ1Y3R1cmUgaXMgYSBnb29kIHN1bW1hcnkgb2YgdGhlIGRhdGEgZ2VvbWV0cnkuIENDQyBjYW4gYmUgdXNlZCB0byBjb21wYXJlIGxpbmthZ2UgbWV0aG9kczogdGhlIGxpbmthZ2Ugd2l0aCB0aGUgaGlnaGVzdCBDQ0MgcHJlc2VydmVzIHBhaXJ3aXNlIGRpc3RhbmNlIGluZm9ybWF0aW9uIGJlc3QuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5jbHVzdGVyLmhpZXJhcmNoeSBpbXBvcnQgbGlua2FnZSwgY29waGVuZXRcbmZyb20gc2NpcHkuc3BhdGlhbC5kaXN0YW5jZSBpbXBvcnQgcGRpc3RcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cblgsIF8gPSBtYWtlX2Jsb2JzKG5fc2FtcGxlcz0yMDAsIGNlbnRlcnM9NCwgY2x1c3Rlcl9zdGQ9MC44LCByYW5kb21fc3RhdGU9MClcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcbmRpc3Rfb3JpZyA9IHBkaXN0KFgpXG5cbnByaW50KGZcIntcdTAwMjdMaW5rYWdlXHUwMDI3OjEwc30ge1x1MDAyN0NvcGhlbmV0aWMgQ29yclx1MDAyNzpcdTAwM2UxOH0ge1x1MDAyN0ludGVycHJldGF0aW9uXHUwMDI3fVwiKVxuZm9yIG1ldGhvZCBpbiBbXHUwMDI3c2luZ2xlXHUwMDI3LCBcdTAwMjdjb21wbGV0ZVx1MDAyNywgXHUwMDI3YXZlcmFnZVx1MDAyNywgXHUwMDI3d2FyZFx1MDAyN106XG4gICAgWiA9IGxpbmthZ2UoWCwgbWV0aG9kPW1ldGhvZClcbiAgICBjY2MsIF8gPSBjb3BoZW5ldChaLCBkaXN0X29yaWcpXG4gICAgaW50ZXJwcmV0YXRpb24gPSAoXG4gICAgICAgIFx1MDAyN0V4Y2VsbGVudFx1MDAyNyBpZiBjY2MgXHUwMDNlIDAuOCBlbHNlXG4gICAgICAgIFx1MDAyN0dvb2RcdTAwMjcgaWYgY2NjIFx1MDAzZSAwLjcgZWxzZVxuICAgICAgICBcdTAwMjdGYWlyXHUwMDI3IGlmIGNjYyBcdTAwM2UgMC42IGVsc2UgXHUwMDI3UG9vclx1MDAyN1xuICAgIClcbiAgICBwcmludChmXCJ7bWV0aG9kOjEwc30ge2NjYzpcdTAwM2UxOC40Zn0ge2ludGVycHJldGF0aW9ufVwiKVxuXG5wcmludChcIlxcbkF2ZXJhZ2UgbGlua2FnZSB0eXBpY2FsbHkgYWNoaWV2ZXMgdGhlIGhpZ2hlc3QgY29waGVuZXRpYyBjb3JyZWxhdGlvbi5cIilcbnByaW50KFwiV2FyZCBoYXMgbG93ZXIgQ0NDIGJ1dCBvZnRlbiBnaXZlcyB0aGUgbW9zdCBwcmFjdGljYWxseSB1c2VmdWwgY2x1c3RlcnMuXCIpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJEZW5kcm9ncmFtIFJlYWRpbmcgR3VpZGUiLCJjb250ZW50IjoiQ3V0IHRoZSBkZW5kcm9ncmFtIGhvcml6b250YWxseTogdGhlIG51bWJlciBvZiB2ZXJ0aWNhbCBsaW5lcyBpbnRlcnNlY3RlZCBlcXVhbHMgdGhlIG51bWJlciBvZiBjbHVzdGVycy4gVGhlIGhlaWdodCBvZiBhIG1lcmdlIGluZGljYXRlcyBob3cgZGlzc2ltaWxhciB0aGUgbWVyZ2luZyBjbHVzdGVycyB3ZXJlIOKAlCBhIGxhcmdlIGp1bXAgaW4gaGVpZ2h0IGJldHdlZW4gY29uc2VjdXRpdmUgbWVyZ2VzIHNpZ25hbHMgYSBuYXR1cmFsIGNsdXN0ZXIgYm91bmRhcnkuIEZvciBXYXJkIGxpbmthZ2UsIGxvb2sgZm9yIHRoZSBsYXJnZXN0IGdhcCBiZXR3ZWVuIGNvbnNlY3V0aXZlIG1lcmdlIGhlaWdodHMgaW4gdGhlIHRvcCBwb3J0aW9uIG9mIHRoZSB0cmVlIHRvIGlkZW50aWZ5IHRoZSBuYXR1cmFsIG51bWJlciBvZiBjbHVzdGVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25uZWN0aXZpdHkgQ29uc3RyYWludHMg4oCUIFN0cnVjdHVyZWQgQ2x1c3RlcmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50Ijoic2tsZWFyblx1MDAyN3MgQWdnbG9tZXJhdGl2ZUNsdXN0ZXJpbmcgYWNjZXB0cyBhIGNvbm5lY3Rpdml0eSBtYXRyaXggdGhhdCByZXN0cmljdHMgbWVyZ2VzIHRvIGFkamFjZW50IG5vZGVzIGluIGEgZ3JhcGggKGUuZy4sIHNwYXRpYWwgbmVpZ2hib3JzIG9yIGstTk4gZ3JhcGgpLiBUaGlzIGRyYW1hdGljYWxseSByZWR1Y2VzIHRoZSBzZXQgb2YgY2FuZGlkYXRlIG1lcmdlcyBhdCBlYWNoIHN0ZXAsIGxvd2VyaW5nIGNvbXBsZXhpdHkgZnJvbSBPKG7CsikgdG8gTyhuKSBmb3Igc3BhcnNlIGdyYXBocyBhbmQgZW5hYmxpbmcgY2x1c3RlcmluZyBvZiBpbWFnZXMsIG1lc2hlcywgb3IgdGltZS1zZXJpZXMgd2hlcmUgb25seSBuZWlnaGJvcmluZyBwb2ludHMgc2hvdWxkIG1lcmdlLiBUaGUgY29ubmVjdGl2aXR5IGNvbnN0cmFpbnQgZWZmZWN0aXZlbHkgZW5mb3JjZXMgc3BhdGlhbGx5IGNvaGVyZW50IGNsdXN0ZXJzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBBZ2dsb21lcmF0aXZlQ2x1c3RlcmluZ1xuZnJvbSBza2xlYXJuLm5laWdoYm9ycyBpbXBvcnQga25laWdoYm9yc19ncmFwaFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2Jsb2JzXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWRqdXN0ZWRfcmFuZF9zY29yZVxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cblgsIHlfdHJ1ZSA9IG1ha2VfYmxvYnMobl9zYW1wbGVzPTUwMCwgY2VudGVycz01LCBjbHVzdGVyX3N0ZD0wLjksIHJhbmRvbV9zdGF0ZT00MilcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxuIyBXaXRob3V0IGNvbm5lY3Rpdml0eTogc3RhbmRhcmQgYWdnbG9tZXJhdGl2ZVxuYWdnX25vX2Nvbm4gPSBBZ2dsb21lcmF0aXZlQ2x1c3RlcmluZyhuX2NsdXN0ZXJzPTUsIGxpbmthZ2U9XHUwMDI3d2FyZFx1MDAyNylcbmxhYmVsc19ub19jb25uID0gYWdnX25vX2Nvbm4uZml0X3ByZWRpY3QoWClcblxuIyBXaXRoIGstTk4gY29ubmVjdGl2aXR5OiByZXN0cmljdHMgdG8gbG9jYWwgbWVyZ2VzXG5jb25uID0ga25laWdoYm9yc19ncmFwaChYLCBuX25laWdoYm9ycz0xNSwgaW5jbHVkZV9zZWxmPUZhbHNlKVxuYWdnX2Nvbm4gPSBBZ2dsb21lcmF0aXZlQ2x1c3RlcmluZyhuX2NsdXN0ZXJzPTUsIGxpbmthZ2U9XHUwMDI3d2FyZFx1MDAyNywgY29ubmVjdGl2aXR5PWNvbm4pXG5sYWJlbHNfY29ubiA9IGFnZ19jb25uLmZpdF9wcmVkaWN0KFgpXG5cbmFyaV9ubyA9IGFkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCBsYWJlbHNfbm9fY29ubilcbmFyaV9jbyA9IGFkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCBsYWJlbHNfY29ubilcbnByaW50KGZcIldhcmQgKG5vIGNvbm5lY3Rpdml0eSk6ICBBUkk9e2FyaV9ubzouNGZ9XCIpXG5wcmludChmXCJXYXJkIChrLU5OIGNvbm4sIGs9MTUpOiBBUkk9e2FyaV9jbzouNGZ9XCIpXG5wcmludChcIkNvbm5lY3Rpdml0eSBjYW4gaW1wcm92ZSByZXN1bHRzIG9uIHNwYXRpYWxseSBzdHJ1Y3R1cmVkIGRhdGFcIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEaXZpc2l2ZSB2cyBBZ2dsb21lcmF0aXZlIENsdXN0ZXJpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpdmlzaXZlICh0b3AtZG93bikgaGllcmFyY2hpY2FsIGNsdXN0ZXJpbmcgc3RhcnRzIHdpdGggYWxsIHBvaW50cyBpbiBvbmUgY2x1c3RlciBhbmQgcmVjdXJzaXZlbHkgc3BsaXRzLiBUaGUgb3B0aW1hbCBzcGxpdCBhdCBlYWNoIGxldmVsIGlzIE5QLWhhcmQsIHNvIGRpdmlzaXZlIG1ldGhvZHMgdHlwaWNhbGx5IHVzZSBhIGZhc3QgaGV1cmlzdGljIChlLmcuLCBrLW1lYW5zIHdpdGggaz0yKS4gRGlhbmEgKERpdmlzaXZlIEFuYWx5c2lzKSBpcyB0aGUgc3RhbmRhcmQgZGl2aXNpdmUgYWxnb3JpdGhtLiBEaXZpc2l2ZSBjbHVzdGVyaW5nIHRlbmRzIHRvIGlkZW50aWZ5IHRoZSB0b3AtbGV2ZWwgc3RydWN0dXJlIGJldHRlciAoZmV3ZXIgbGFyZ2UgY2x1c3RlcnMpIHdoaWxlIGFnZ2xvbWVyYXRpdmUgYmV0dGVyIGNhcHR1cmVzIGZpbmUtZ3JhaW5lZCBzdHJ1Y3R1cmUuIEluIHByYWN0aWNlIGFnZ2xvbWVyYXRpdmUgV2FyZCBsaW5rYWdlIGRvbWluYXRlcyBiZWNhdXNlIGl0IG9wdGltaXplcyB0aGUgc2FtZSB2YXJpYW5jZSBjcml0ZXJpb24gYXMgay1tZWFucyB3aGlsZSBwcm92aWRpbmcgdGhlIGZ1bGwgaGllcmFyY2h5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBsZXhpdHkgYW5kIFNjYWxhYmlsaXR5In0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJOYWl2ZSBoaWVyYXJjaGljYWwgY2x1c3RlcmluZzogTyhuwrMpIHRpbWUsIE8obsKyKSBzcGFjZSBmb3IgdGhlIGRpc3RhbmNlIG1hdHJpeC4iLCJXYXJkIGFuZCBhdmVyYWdlIGxpbmthZ2Ugd2l0aCBwcmlvcml0eSBxdWV1ZSAoc2NpcHkgaW1wbGVtZW50YXRpb24pOiBPKG7CsiBsb2cgbikgdGltZSwgTyhuwrIpIHNwYWNlLiIsIlNpbmdsZSBsaW5rYWdlIG9ubHk6IE8obsKyIGxvZyBuKSB2aWEgUHJpbVx1MDAyN3MgTVNUIGFsZ29yaXRobSDigJQgY2FuIGhhbmRsZSBuIOKJiCA1MDBLLiIsIlByYWN0aWNhbCBsaW1pdCBmb3IgV2FyZC9jb21wbGV0ZS9hdmVyYWdlOiBuIOKJiCAxMCwwMDDigJM1MCwwMDAgZGVwZW5kaW5nIG9uIGF2YWlsYWJsZSBSQU0uIiwiRm9yIGxhcmdlciBuOiB1c2Ugay1tZWFucyBvciBtaW5pLWJhdGNoIGstbWVhbnMsIHRoZW4gaGllcmFyY2hpY2FsbHkgY2x1c3RlciB0aGUgayBjZW50cm9pZHMgKGRpdmlzaXZlIGFwcHJvYWNoKS4iLCJza2xlYXJuIEFnZ2xvbWVyYXRpdmVDbHVzdGVyaW5nIHdpdGggY29ubmVjdGl2aXR5IGNvbnN0cmFpbnRzIGNhbiBzY2FsZSB0byBsYXJnZXIgbiBieSByZXN0cmljdGluZyBtZXJnZXMgdG8gYSBzcGFyc2UgZ3JhcGguIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Hierarchical Clustering — Linkage Methods and Dendrograms

Hierarchical clustering builds a tree of nested partitions without requiring k to be specified in advance. The dendrogram records the entire merge history — you choose the number of clusters post-hoc by cutting the tree at any height. Agglomerative (bottom-up) hierarchical clustering starts with each point as its own cluster and greedily merges the two closest clusters at each step. The choice of linkage criterion — how inter-cluster distance is measured — has a major effect on cluster shape and quality.

## Agglomerative Algorithm

Starting with n singleton clusters, at each step find the pair of clusters (Cᵢ, Cⱼ) with the smallest inter-cluster distance d(Cᵢ,Cⱼ) (determined by the linkage criterion), merge them into one cluster, update the distance matrix, and repeat until one cluster remains. The merge history is recorded as a dendrogram: each internal node represents a merge, its height is the distance at which the merge occurred, and cutting the tree horizontally at height h yields the flat clustering at that resolution. The naive implementation is O(n³) but the priority-queue version is O(n² log n) for most linkages.

```python
import numpy as np
from sklearn.datasets import make_blobs

def single_linkage_agglomerative(X):
    """Single linkage hierarchical clustering from scratch."""
    n = X.shape[0]
    # Distance matrix
    dists = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2))
    np.fill_diagonal(dists, np.inf)
    # Track cluster membership
    clusters = [{i} for i in range(n)]
    active = list(range(n))
    merge_history = []  # (cluster_a_idx, cluster_b_idx, distance)
    for step in range(n - 1):
        # Find minimum inter-cluster distance using active cluster representatives
        best_d, best_i, best_j = np.inf, -1, -1
        for idx_a in range(len(active)):
            for idx_b in range(idx_a + 1, len(active)):
                a_pts = list(clusters[active[idx_a]])
                b_pts = list(clusters[active[idx_b]])
                # Single linkage: minimum pairwise distance
                d = dists[np.ix_(a_pts, b_pts)].min()
                if d < best_d:
                    best_d, best_i, best_j = d, idx_a, idx_b
        ci, cj = active[best_i], active[best_j]
        merge_history.append((ci, cj, best_d))
        clusters[ci] = clusters[ci] | clusters[cj]
        active.pop(best_j)
    return merge_history

X, y = make_blobs(n_samples=12, centers=3, random_state=0)
history = single_linkage_agglomerative(X)
print("Merge history (cluster_a, cluster_b, distance):")
for a, b, d in history[:6]:
    print(f"  clusters {a} + {b} at distance {d:.4f}")
```

## Linkage Criteria

The linkage criterion defines how the distance between two clusters is computed from pairwise point distances. Single linkage d(A,B) = min_{a∈A,b∈B} dist(a,b) tends to produce elongated, chained clusters ('chaining effect'). Complete linkage d(A,B) = max_{a∈A,b∈B} dist(a,b) forces compact clusters but splits large diffuse clusters. Average linkage (UPGMA) d(A,B) = (1/|A||B|) Σ dist(a,b) is a balanced compromise. Ward linkage minimizes the increase in total within-cluster variance at each merge: Δ(A,B) = |A||B|/(|A|+|B|) × ‖μ_A − μ_B‖² — equivalent to k-means objective, typically producing the most compact clusters.

| Linkage | Distance Formula | Chain Effect | Outlier Sensitive | Typical Use |
| --- | --- | --- | --- | --- |
| Single | min pairwise distance | Yes — prone to chaining | Yes — one bridge merges clusters | Non-convex chains, dendrogram analysis |
| Complete | max pairwise distance | No — compact clusters | Yes — outliers delay merges | Compact, similarly-sized clusters |
| Average (UPGMA) | mean pairwise distance | Mild | Moderate | General purpose, balanced clusters |
| Ward | min variance increase | No — most compact | No — uses cluster means | Default choice for compact clusters |

```python
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, y_true = make_blobs(n_samples=150, centers=4, cluster_std=0.8, random_state=42)
X = StandardScaler().fit_transform(X)

print(f"{'Linkage':10s} {'ARI':>8} {'Silhouette':>12}")
from sklearn.metrics import adjusted_rand_score, silhouette_score
for method in ['single', 'complete', 'average', 'ward']:
    Z = linkage(X, method=method)
    labels = fcluster(Z, t=4, criterion='maxclust') - 1
    ari = adjusted_rand_score(y_true, labels)
    sil = silhouette_score(X, labels)
    print(f"{method:10s} {ari:>8.4f} {sil:>12.4f}")

# Show Ward dendrogram info
Z_ward = linkage(X, method='ward')
print(f"\nWard: last 5 merge heights: {Z_ward[-5:, 2].round(3)}")
print("Large gap between height[-2] and height[-1] indicates natural cluster count.")
```

## Ward Linkage vs K-Means

Ward linkage minimizes the same criterion as k-means — total within-cluster variance — but produces a hierarchical result rather than a flat partition. Ward clustering tends to produce similarly-sized compact clusters and often gives results very similar to k-means. The advantage of Ward over k-means is the dendrogram: you can explore different numbers of clusters without rerunning the algorithm. The disadvantage is quadratic memory O(n²) for the distance matrix, limiting Ward to n < 50,000 in practice.

```python
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)
X, y_true = make_blobs(n_samples=400, centers=5, cluster_std=0.9, random_state=42)
X = StandardScaler().fit_transform(X)

Z_ward = linkage(X, method='ward')
print(f"{'k':>4} {'Ward ARI':>10} {'KMeans ARI':>12} {'Ward Sil':>10} {'KMeans Sil':>12}")
for k in [3, 4, 5, 6, 7]:
    ward_labels = fcluster(Z_ward, t=k, criterion='maxclust') - 1
    km_labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X)
    ward_ari = adjusted_rand_score(y_true, ward_labels)
    km_ari = adjusted_rand_score(y_true, km_labels)
    ward_sil = silhouette_score(X, ward_labels)
    km_sil = silhouette_score(X, km_labels)
    print(f"{k:>4} {ward_ari:>10.4f} {km_ari:>12.4f} {ward_sil:>10.4f} {km_sil:>12.4f}")
```

## Cophenetic Correlation Coefficient

The cophenetic distance between two points is the height in the dendrogram at which they first merge. The cophenetic correlation coefficient (CCC) is the Pearson correlation between the original pairwise distances and the cophenetic distances. A high CCC (> 0.8) indicates that the dendrogram faithfully represents the true distances — the hierarchical structure is a good summary of the data geometry. CCC can be used to compare linkage methods: the linkage with the highest CCC preserves pairwise distance information best.

```python
import numpy as np
from scipy.cluster.hierarchy import linkage, cophenet
from scipy.spatial.distance import pdist
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, _ = make_blobs(n_samples=200, centers=4, cluster_std=0.8, random_state=0)
X = StandardScaler().fit_transform(X)
dist_orig = pdist(X)

print(f"{'Linkage':10s} {'Cophenetic Corr':>18} {'Interpretation'}")
for method in ['single', 'complete', 'average', 'ward']:
    Z = linkage(X, method=method)
    ccc, _ = cophenet(Z, dist_orig)
    interpretation = (
        'Excellent' if ccc > 0.8 else
        'Good' if ccc > 0.7 else
        'Fair' if ccc > 0.6 else 'Poor'
    )
    print(f"{method:10s} {ccc:>18.4f} {interpretation}")

print("\nAverage linkage typically achieves the highest cophenetic correlation.")
print("Ward has lower CCC but often gives the most practically useful clusters.")
```

> **Dendrogram Reading Guide**: Cut the dendrogram horizontally: the number of vertical lines intersected equals the number of clusters. The height of a merge indicates how dissimilar the merging clusters were — a large jump in height between consecutive merges signals a natural cluster boundary. For Ward linkage, look for the largest gap between consecutive merge heights in the top portion of the tree to identify the natural number of clusters.

## Connectivity Constraints — Structured Clustering

sklearn's AgglomerativeClustering accepts a connectivity matrix that restricts merges to adjacent nodes in a graph (e.g., spatial neighbors or k-NN graph). This dramatically reduces the set of candidate merges at each step, lowering complexity from O(n²) to O(n) for sparse graphs and enabling clustering of images, meshes, or time-series where only neighboring points should merge. The connectivity constraint effectively enforces spatially coherent clusters.

```python
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph
from sklearn.datasets import make_blobs
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

X, y_true = make_blobs(n_samples=500, centers=5, cluster_std=0.9, random_state=42)
X = StandardScaler().fit_transform(X)

# Without connectivity: standard agglomerative
agg_no_conn = AgglomerativeClustering(n_clusters=5, linkage='ward')
labels_no_conn = agg_no_conn.fit_predict(X)

# With k-NN connectivity: restricts to local merges
conn = kneighbors_graph(X, n_neighbors=15, include_self=False)
agg_conn = AgglomerativeClustering(n_clusters=5, linkage='ward', connectivity=conn)
labels_conn = agg_conn.fit_predict(X)

ari_no = adjusted_rand_score(y_true, labels_no_conn)
ari_co = adjusted_rand_score(y_true, labels_conn)
print(f"Ward (no connectivity):  ARI={ari_no:.4f}")
print(f"Ward (k-NN conn, k=15): ARI={ari_co:.4f}")
print("Connectivity can improve results on spatially structured data")
```

## Divisive vs Agglomerative Clustering

Divisive (top-down) hierarchical clustering starts with all points in one cluster and recursively splits. The optimal split at each level is NP-hard, so divisive methods typically use a fast heuristic (e.g., k-means with k=2). Diana (Divisive Analysis) is the standard divisive algorithm. Divisive clustering tends to identify the top-level structure better (fewer large clusters) while agglomerative better captures fine-grained structure. In practice agglomerative Ward linkage dominates because it optimizes the same variance criterion as k-means while providing the full hierarchy.

## Complexity and Scalability

- Naive hierarchical clustering: O(n³) time, O(n²) space for the distance matrix.
- Ward and average linkage with priority queue (scipy implementation): O(n² log n) time, O(n²) space.
- Single linkage only: O(n² log n) via Prim's MST algorithm — can handle n ≈ 500K.
- Practical limit for Ward/complete/average: n ≈ 10,000–50,000 depending on available RAM.
- For larger n: use k-means or mini-batch k-means, then hierarchically cluster the k centroids (divisive approach).
- sklearn AgglomerativeClustering with connectivity constraints can scale to larger n by restricting merges to a sparse graph.

---

