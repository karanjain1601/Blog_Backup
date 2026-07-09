---
title: "t-SNE — Perplexity, Crowding Problem, and Pitfalls"
slug: "tsne"
description: "How t-SNE converts pairwise similarities to probabilities, why the Student-t distribution solves the crowding problem, the KL divergence objective, Barnes-Hut approximation, and the five most common pitfalls when interpreting t-SNE plots."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoidC1TTkUgKHQtZGlzdHJpYnV0ZWQgU3RvY2hhc3RpYyBOZWlnaGJvciBFbWJlZGRpbmcpIGlzIGEgbm9ubGluZWFyIGRpbWVuc2lvbmFsaXR5IHJlZHVjdGlvbiB0ZWNobmlxdWUgZGVzaWduZWQgdG8gcHJlc2VydmUgbG9jYWwgc3RydWN0dXJlOiBuZWFyYnkgcG9pbnRzIGluIHRoZSBoaWdoLWRpbWVuc2lvbmFsIHNwYWNlIHNob3VsZCByZW1haW4gbmVhcmJ5IGluIHRoZSAyRCBvciAzRCBlbWJlZGRpbmcuIEl0IGlzIHRoZSBkb21pbmFudCB0ZWNobmlxdWUgZm9yIHZpc3VhbGlzaW5nIGhpZ2gtZGltZW5zaW9uYWwgZGF0YSwgYnV0IGNvbWVzIHdpdGggc2V2ZXJlIHBpdGZhbGxzIHRoYXQgbWFrZSBuYWl2ZSBpbnRlcnByZXRhdGlvbiBkYW5nZXJvdXMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSGlnaC1EaW1lbnNpb25hbCBTaW1pbGFyaXRpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciBlYWNoIHBhaXIgb2YgcG9pbnRzIGksaiwgdC1TTkUgY29tcHV0ZXMgYSBjb25kaXRpb25hbCBHYXVzc2lhbiBzaW1pbGFyaXR5OiBw4rG8fOG1oiA9IGV4cCgt4oCWeOG1oi144rG84oCWwrIvMs+D4bWiwrIpIC8gzqPigpbiiaDhtaIgZXhwKC3igJZ44bWiLXjigpbigJbCsi8yz4PhtaLCsikuIFRoZSBiYW5kd2lkdGggz4PhtaIgaXMgdHVuZWQgcGVyIHBvaW50IHNvIHRoYXQgdGhlIHBlcnBsZXhpdHkgUGVycChQ4bWiKSA9IDJeSChQ4bWiKSBtYXRjaGVzIHRoZSB1c2VyLXNwZWNpZmllZCBwZXJwbGV4aXR5IGh5cGVycGFyYW1ldGVyLiBUaGUgc3ltbWV0cmlzZWQgam9pbnQgcHJvYmFiaWxpdHkgaXMgcOG1ouKxvCA9IChw4rG8fOG1oiArIHDhtaJ84rG8KS8oMm4pLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikxvdy1EaW1lbnNpb25hbCBTaW1pbGFyaXRpZXMgYW5kIHRoZSBDcm93ZGluZyBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY3Jvd2RpbmcgcHJvYmxlbTogaW4gaGlnaC1kaW1lbnNpb25hbCBzcGFjZSwgbWFueSBwb2ludHMgY2FuIGJlIHJvdWdobHkgZXF1aWRpc3RhbnQgZnJvbSBhIGNlbnRyZSBwb2ludCAodGhlIHNwaGVyZSBzdXJmYWNlIGdyb3dzIGFzIHLhtYgpLiBXaGVuIGNvbXByZXNzZWQgdG8gMkQsIGEgR2F1c3NpYW4ga2VybmVsIHdvdWxkIGFzc2lnbiBuZWFyLXplcm8gcHJvYmFiaWxpdHkgdG8gYWxsIGJ1dCBhIGZldyBuZWlnaGJvdXJzIOKAlCBjcnVzaGluZyBtYW55IG5hdHVyYWwgbmVpZ2hib3VycyB0b2dldGhlciBpbiBhIHRpbnkgcmVnaW9uLiB0LVNORSBmaXhlcyB0aGlzIGJ5IHVzaW5nIGEgU3R1ZGVudC10IGRpc3RyaWJ1dGlvbiB3aXRoIDEgZGVncmVlIG9mIGZyZWVkb20gKENhdWNoeSkgZm9yIGxvdy1kaW1lbnNpb25hbCBzaW1pbGFyaXRpZXM6IHHhtaLisbwgPSAoMSArIOKAlnnhtaIteeKxvOKAlsKyKeKBu8K5IC8gzqPigpbiiaDigpcoMSArIOKAlnnigpYteeKCl+KAlsKyKeKBu8K5LiBUaGUgaGVhdnkgdGFpbHMgYWxsb2NhdGUgbXVjaCBtb3JlIHByb2JhYmlsaXR5IG1hc3MgdG8gbW9kZXJhdGUgZGlzdGFuY2VzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcblxuIyBJbGx1c3RyYXRlIHdoeSBTdHVkZW50LXQgc29sdmVzIHRoZSBjcm93ZGluZyBwcm9ibGVtXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG5kX2hpZ2ggPSAxMDAgICMgaW50cmluc2ljIGRpbWVuc2lvbmFsaXR5IG9mIGhpZ2gtZGltIHNwaGVyZVxuXG4jIFNpbXVsYXRlIGRpc3RhbmNlcyBmcm9tIGEgY2VudHJlIHBvaW50IHRvIG5laWdoYm91cnMgb24gYSBzcGhlcmVcbmRpc3RhbmNlcyA9IG5wLnNxcnQocm5nLmNoaXNxdWFyZShkX2hpZ2gsIHNpemU9MjAwMCkgLyBkX2hpZ2gpXG5cbiMgR2F1c3NpYW4gbG93LWRpbSBzaW1pbGFyaXR5ICh2YW5pbGxhIFNORSlcbnNpZ21hID0gMC4zXG5xX2dhdXNzID0gbnAuZXhwKC1kaXN0YW5jZXMqKjIgLyAoMiAqIHNpZ21hKioyKSlcbnFfZ2F1c3MgLz0gcV9nYXVzcy5zdW0oKVxuXG4jIFN0dWRlbnQtdCBzaW1pbGFyaXR5ICh0LVNORSlcbnFfdCA9IDEuMCAvICgxLjAgKyBkaXN0YW5jZXMqKjIpXG5xX3QgLz0gcV90LnN1bSgpXG5cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCAyLCBmaWdzaXplPSgxMiwgNCkpXG5heGVzWzBdLmhpc3QocV9nYXVzcyAqIDEwMDAsIGJpbnM9ODAsIGFscGhhPTAuNywgY29sb3I9XHUwMDI3c3RlZWxibHVlXHUwMDI3KVxuYXhlc1swXS5zZXRfdGl0bGUoXHUwMDI3R2F1c3NpYW4gcSDigJQgY3Jvd2RlZCBuZWFyIHplcm9cdTAwMjcpXG5heGVzWzBdLnNldF94bGFiZWwoXHUwMDI3U2NhbGVkIHNpbWlsYXJpdHlcdTAwMjcpXG5cbmF4ZXNbMV0uaGlzdChxX3QgKiAxMDAwLCBiaW5zPTgwLCBhbHBoYT0wLjcsIGNvbG9yPVx1MDAyN2NvcmFsXHUwMDI3KVxuYXhlc1sxXS5zZXRfdGl0bGUoXHUwMDI3U3R1ZGVudC10IHEg4oCUIGJldHRlciBzcHJlYWRcdTAwMjcpXG5heGVzWzFdLnNldF94bGFiZWwoXHUwMDI3U2NhbGVkIHNpbWlsYXJpdHlcdTAwMjcpXG5cbmVmZl9nYXVzcyA9IChxX2dhdXNzIFx1MDAzZSAwLjAwMSAvIGxlbihkaXN0YW5jZXMpKS5zdW0oKVxuZWZmX3QgPSAocV90IFx1MDAzZSAwLjAwMSAvIGxlbihkaXN0YW5jZXMpKS5zdW0oKVxucHJpbnQoZlx1MDAyN0VmZmVjdGl2ZSBuZWlnaGJvdXJzIChHYXVzc2lhbik6IHtlZmZfZ2F1c3N9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0VmZmVjdGl2ZSBuZWlnaGJvdXJzIChTdHVkZW50LXQpOiB7ZWZmX3R9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktMIERpdmVyZ2VuY2UgT2JqZWN0aXZlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJ0LVNORSBtaW5pbWlzZXMgdGhlIEt1bGxiYWNrLUxlaWJsZXIgZGl2ZXJnZW5jZSBiZXR3ZWVuIHRoZSBoaWdoLWRpbSBqb2ludCBkaXN0cmlidXRpb24gUCBhbmQgdGhlIGxvdy1kaW0gZGlzdHJpYnV0aW9uIFE6IENvc3QgPSBLTChQ4oCWUSkgPSDOo+G1ouKxvCBw4bWi4rG8IGxvZyhw4bWi4rG8L3HhtaLisbwpLiBCZWNhdXNlIEtMIGlzIGFzeW1tZXRyaWMsIHBsYWNpbmcgd2VsbC1zZXBhcmF0ZWQgaGlnaC1kaW0gbmVpZ2hib3VycyAobGFyZ2UgcOG1ouKxvCkgZmFyIGluIHRoZSBsb3ctZGltIHNwYWNlIChzbWFsbCBx4bWi4rG8KSBpbmN1cnMgYSBsYXJnZSBwZW5hbHR5LiBCdXQgcGxhY2luZyBub24tbmVpZ2hib3VycyAoc21hbGwgcOG1ouKxvCkgdG9nZXRoZXIgaW5jdXJzIGxpdHRsZSBjb3N0IOKAlCBoZW5jZSB0LVNORSBjYW4gY3JlYXRlIHNwdXJpb3VzIGNsdXN0ZXIgc3RydWN0dXJlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgZmV0Y2hfb3Blbm1sXG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgUENBXG5mcm9tIHNrbGVhcm4ubWFuaWZvbGQgaW1wb3J0IFRTTkVcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG4jIE1OSVNUIHN1YnNldCDigJQgcHJlLXJlZHVjZSB3aXRoIFBDQSBmaXJzdCAocmVjb21tZW5kZWQpXG5tbmlzdCA9IGZldGNoX29wZW5tbChcdTAwMjdtbmlzdF83ODRcdTAwMjcsIHZlcnNpb249MSwgYXNfZnJhbWU9RmFsc2UpXG5YID0gbW5pc3QuZGF0YVs6MzAwMF0uYXN0eXBlKGZsb2F0KVxueSA9IG1uaXN0LnRhcmdldFs6MzAwMF0uYXN0eXBlKGludClcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblhfcGNhID0gUENBKG5fY29tcG9uZW50cz01MCwgcmFuZG9tX3N0YXRlPTQyKS5maXRfdHJhbnNmb3JtKFgpXG5cbnBlcnBsZXhpdGllcyA9IFs1LCAzMCwgNTAsIDEwMF1cbmZpZywgYXhlcyA9IHBsdC5zdWJwbG90cygxLCA0LCBmaWdzaXplPSgyMCwgNSkpXG5cbmZvciBheCwgcGVycCBpbiB6aXAoYXhlcywgcGVycGxleGl0aWVzKTpcbiAgICB0c25lID0gVFNORShuX2NvbXBvbmVudHM9MiwgcGVycGxleGl0eT1wZXJwLCByYW5kb21fc3RhdGU9NDIsXG4gICAgICAgICAgICAgICAgbl9pdGVyPTUwMCwgbWV0aG9kPVx1MDAyN2Jhcm5lc19odXRcdTAwMjcpXG4gICAgWF90c25lID0gdHNuZS5maXRfdHJhbnNmb3JtKFhfcGNhKVxuICAgIHNjID0gYXguc2NhdHRlcihYX3RzbmVbOiwgMF0sIFhfdHNuZVs6LCAxXSwgYz15LCBjbWFwPVx1MDAyN3RhYjEwXHUwMDI3LCBzPTUsIGFscGhhPTAuNylcbiAgICBheC5zZXRfdGl0bGUoZlx1MDAyN1BlcnBsZXhpdHkgPSB7cGVycH1cdTAwMjcpXG4gICAgYXguYXhpcyhcdTAwMjdvZmZcdTAwMjcpXG5cbnBsdC5zdXB0aXRsZShcdTAwMjd0LVNORSBvbiBNTklTVCDigJQgRWZmZWN0IG9mIFBlcnBsZXhpdHlcdTAwMjcsIGZvbnRzaXplPTEzKVxucGx0LmNvbG9yYmFyKHNjLCBheD1heGVzLCBsYWJlbD1cdTAwMjdEaWdpdFx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoidC1TTkUgUGl0ZmFsbHMiLCJjb250ZW50IjoiQ2x1c3RlciBzaXplcyBpbiB0LVNORSBwbG90cyBhcmUgbWVhbmluZ2xlc3Mg4oCUIGEgbGFyZ2UgY2x1c3RlciBkb2VzIG5vdCBtZWFuIG1vcmUgcG9pbnRzLiBJbnRlci1jbHVzdGVyIGRpc3RhbmNlcyBhcmUgYWxzbyBtZWFuaW5nbGVzcyDigJQgY2x1c3RlcnMgZmFyIGFwYXJ0IGluIDJEIG1heSBiZSBuZWlnaGJvdXJzIGluIGhpZ2gtZGltIHNwYWNlLiB0LVNORSBpcyBzdG9jaGFzdGljOyBydW4gaXQgbXVsdGlwbGUgdGltZXMgYW5kIGNvbXBhcmUuIFBlcnBsZXhpdHkgZHJhbWF0aWNhbGx5IGNoYW5nZXMgYXBwYXJlbnQgc3RydWN0dXJlLiBOZXZlciBkcmF3IHF1YW50aXRhdGl2ZSBjb25jbHVzaW9ucyBmcm9tIHQtU05FIGFsb25lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhcm5lcy1IdXQgQXBwcm94aW1hdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmHDr3ZlIHQtU05FIGdyYWRpZW50IGNvbXB1dGF0aW9uIGNvc3RzIE8obsKyKSBwZXIgaXRlcmF0aW9uIOKAlCBpbnRyYWN0YWJsZSBmb3IgbiBcdTAwM2UgNSwwMDAuIEJhcm5lcy1IdXQgdC1TTkUgdXNlcyBhIHF1YWQtdHJlZSAoMkQpIG9yIG9jdHJlZSAoM0QpIHRvIGFwcHJveGltYXRlIHJlcHVsc2l2ZSBmb3JjZXMgaW4gTyhuIGxvZyBuKTogY2VsbHMgZmFyIGZyb20gYSBwb2ludCBjb250cmlidXRlIGEgc2luZ2xlIHN1bW1hcmlzZWQgZm9yY2UuIFRoaXMgcmVkdWNlcyB3YWxsIHRpbWUgZnJvbSBob3VycyB0byBtaW51dGVzIGZvciBuIH4gMTAsMDAw4oCTMTAwLDAwMC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdGltZVxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBmZXRjaF9vcGVubWxcbmZyb20gc2tsZWFybi5kZWNvbXBvc2l0aW9uIGltcG9ydCBQQ0FcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLm1hbmlmb2xkIGltcG9ydCBUU05FXG5cbm1uaXN0ID0gZmV0Y2hfb3Blbm1sKFx1MDAyN21uaXN0Xzc4NFx1MDAyNywgdmVyc2lvbj0xLCBhc19mcmFtZT1GYWxzZSlcblggPSBtbmlzdC5kYXRhWzo1MDAwXS5hc3R5cGUoZmxvYXQpXG55ID0gbW5pc3QudGFyZ2V0Wzo1MDAwXVxuWCA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKVxuWF9wY2EgPSBQQ0Eobl9jb21wb25lbnRzPTUwLCByYW5kb21fc3RhdGU9NDIpLmZpdF90cmFuc2Zvcm0oWClcblxuIyBza2xlYXJuIFRTTkUgd2l0aCBCYXJuZXMtSHV0XG50MCA9IHRpbWUudGltZSgpXG5YX3RzbmVfc2sgPSBUU05FKG5fY29tcG9uZW50cz0yLCBwZXJwbGV4aXR5PTMwLCByYW5kb21fc3RhdGU9NDIsXG4gICAgICAgICAgICAgICAgICBtZXRob2Q9XHUwMDI3YmFybmVzX2h1dFx1MDAyNywgbl9pdGVyPTUwMCkuZml0X3RyYW5zZm9ybShYX3BjYSlcbnNrX3RpbWUgPSB0aW1lLnRpbWUoKSAtIHQwXG5wcmludChmXHUwMDI3c2tsZWFybiBUU05FIChCYXJuZXMtSHV0KToge3NrX3RpbWU6LjFmfXNcdTAwMjcpXG5cbiMgb3BlblRTTkUg4oCUIGZhc3Rlciwgc3VwcG9ydHMgb3V0LW9mLXNhbXBsZSBleHRlbnNpb25cbnRyeTpcbiAgICBmcm9tIG9wZW5UU05FIGltcG9ydCBUU05FIGFzIG9wZW5UU05FXG4gICAgdDAgPSB0aW1lLnRpbWUoKVxuICAgIHRzbmVfb3BlbiA9IG9wZW5UU05FKHBlcnBsZXhpdHk9MzAsIHJhbmRvbV9zdGF0ZT00Miwgbl9qb2JzPS0xLCBuX2l0ZXI9NTAwKVxuICAgIFhfdHNuZV9vcGVuID0gdHNuZV9vcGVuLmZpdChYX3BjYSlcbiAgICBvcGVuX3RpbWUgPSB0aW1lLnRpbWUoKSAtIHQwXG4gICAgcHJpbnQoZlx1MDAyN29wZW5UU05FOiB7b3Blbl90aW1lOi4xZn1zICAoc3BlZWR1cDoge3NrX3RpbWUgLyBvcGVuX3RpbWU6LjFmfXgpXHUwMDI3KVxuICAgICMgT3V0LW9mLXNhbXBsZTogZW1iZWQgbmV3IHBvaW50cyB3aXRob3V0IHJlZml0dGluZ1xuICAgIFhfbmV3X2VtYmVkZGVkID0gdHNuZV9vcGVuLnRyYW5zZm9ybShYX3BjYVs6NTBdKVxuICAgIHByaW50KGZcdTAwMjdOZXcgcG9pbnRzIGVtYmVkZGVkIHNoYXBlOiB7WF9uZXdfZW1iZWRkZWQuc2hhcGV9XHUwMDI3KVxuZXhjZXB0IEltcG9ydEVycm9yOlxuICAgIHByaW50KFx1MDAyN3BpcCBpbnN0YWxsIG9wZW50c25lIGZvciBmYXN0ZXIgdC1TTkVcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRGVtb25zdHJhdGluZyBQaXRmYWxscyB3aXRoIFN5bnRoZXRpYyBEYXRhIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSBza2xlYXJuLm1hbmlmb2xkIGltcG9ydCBUU05FXG5cbnJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyg0MilcblxuIyBUaHJlZSBjbHVzdGVyczogZGlmZmVyZW50IHNpemVzIEFORCBkaWZmZXJlbnQgZGVuc2l0aWVzXG5zbWFsbF90aWdodCA9IHJuZy5ub3JtYWwoWzAsIDBdLCAwLjUsICgyMCwgMTApKVxubGFyZ2Vfc3ByZWFkID0gcm5nLm5vcm1hbChbOCwgMF0sIDMuMCwgKDIwMCwgMTApKVxuc21hbGxfZmFyID0gcm5nLm5vcm1hbChbMjAsIDBdLCAwLjUsICgyMCwgMTApKVxuXG5YID0gbnAudnN0YWNrKFtzbWFsbF90aWdodCwgbGFyZ2Vfc3ByZWFkLCBzbWFsbF9mYXJdKVxubGFiZWxzID0gbnAuYXJyYXkoWzBdKjIwICsgWzFdKjIwMCArIFsyXSoyMClcblxuIyBQQ0Eg4oCUIHNob3dzIHRydWUgcmVsYXRpdmUgcG9zaXRpb25zXG5mcm9tIHNrbGVhcm4uZGVjb21wb3NpdGlvbiBpbXBvcnQgUENBXG5YX3BjYSA9IFBDQShuX2NvbXBvbmVudHM9MikuZml0X3RyYW5zZm9ybShYKVxuZmlnLCBheGVzID0gcGx0LnN1YnBsb3RzKDEsIDIsIGZpZ3NpemU9KDEyLCA1KSlcbmF4ZXNbMF0uc2NhdHRlcihYX3BjYVs6LCAwXSwgWF9wY2FbOiwgMV0sIGM9bGFiZWxzLCBjbWFwPVx1MDAyN1NldDFcdTAwMjcsIHM9MjApXG5heGVzWzBdLnNldF90aXRsZShcdTAwMjdQQ0Eg4oCUIHRydWU6IGRpZmZlcmVudCBzaXplcyBcdTAwMjYgZGlzdGFuY2VzXHUwMDI3KVxuXG4jIHQtU05FIOKAlCBkaXN0b3J0cyBib3RoIGNsdXN0ZXIgc2l6ZSBhbmQgaW50ZXItY2x1c3RlciBkaXN0YW5jZVxuWF90c25lID0gVFNORShuX2NvbXBvbmVudHM9MiwgcGVycGxleGl0eT0zMCwgcmFuZG9tX3N0YXRlPTQyLCBuX2l0ZXI9MTAwMCkuZml0X3RyYW5zZm9ybShYKVxuYXhlc1sxXS5zY2F0dGVyKFhfdHNuZVs6LCAwXSwgWF90c25lWzosIDFdLCBjPWxhYmVscywgY21hcD1cdTAwMjdTZXQxXHUwMDI3LCBzPTIwKVxuYXhlc1sxXS5zZXRfdGl0bGUoXHUwMDI3dC1TTkUg4oCUIHNpemVzIGFuZCBkaXN0YW5jZXMgQVJFIE1FQU5JTkdMRVNTXHUwMDI3KVxucGx0LnN1cHRpdGxlKFx1MDAyN3QtU05FIFBpdGZhbGw6IENsdXN0ZXIgU2l6ZSBhbmQgRGlzdGFuY2UgTm90IFByZXNlcnZlZFx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBpdGZhbGwgUmVmZXJlbmNlIFRhYmxlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk15dGgiLCJSZWFsaXR5IiwiV2h5Il0sInJvd3MiOltbIkNsdXN0ZXIgc2l6ZSBpbmRpY2F0ZXMgbnVtYmVyIG9mIHBvaW50cyIsIkZhbHNlIOKAlCBzaXplIGlzIGFyYml0cmFyeSIsIktMIGFzeW1tZXRyeSBhbGxvd3MgY29tcGFjdCBvciBleHBhbmRlZCBjbHVzdGVycyJdLFsiRGlzdGFuY2UgYmV0d2VlbiBjbHVzdGVycyBpcyBtZWFuaW5nZnVsIiwiRmFsc2Ug4oCUIG9ubHkgbG9jYWwgc3RydWN0dXJlIHByZXNlcnZlZCIsIlJlcHVsc2l2ZSBmb3JjZXMgcHVzaCBhbGwgY2x1c3RlcnMgYXBhcnQgc2ltaWxhcmx5Il0sWyJBIHNpbmdsZSB0LVNORSBwbG90IGlzIGVub3VnaCIsIkZhbHNlIOKAlCBhbHdheXMgdHJ5IG11bHRpcGxlIHNlZWRzIiwiT2JqZWN0aXZlIGhhcyBtYW55IGxvY2FsIG1pbmltYSJdLFsiUGVycGxleGl0eSBkb2VzIG5vdCBtYXR0ZXIgbXVjaCIsIkZhbHNlIOKAlCBpdCBjb250cm9scyBuZWlnaGJvdXJob29kIHJhZGl1cyIsIkxvdyBwZXJwbGV4aXR5IOKGkiBmcmFnbWVudGVkOyBoaWdoIOKGkiBtZXJnZWQgY2x1c3RlcnMiXSxbIklzb2xhdGVkIHBvaW50cyBhcmUgZ2VudWluZSBvdXRsaWVycyIsIkZhbHNlIOKAlCBtYXkgYmUgbWlzcGxhY2VkIGJ5IGNyb3dkaW5nIiwiUG9pbnRzIHdpdGggZmV3IG5laWdoYm91cnMgYXJlIHB1c2hlZCBmYXIgYXdheSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIFJlY29tbWVuZGF0aW9ucyJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiUHJlLXJlZHVjZSB3aXRoIFBDQSB0byA1MCBkaW1lbnNpb25zIGJlZm9yZSBydW5uaW5nIHQtU05FIOKAlCByZWR1Y2VzIG5vaXNlIGFuZCBzcGVlZHMgY29tcHV0YXRpb24iLCJVc2UgcGVycGxleGl0eSBpbiB0aGUgcmFuZ2UgNeKAkzUwIGZvciBtb3N0IGRhdGFzZXRzOyB0cnkgc2V2ZXJhbCB2YWx1ZXMgYW5kIGNvbXBhcmUiLCJSdW4gZm9yIGF0IGxlYXN0IDEwMDAgaXRlcmF0aW9uczsgd2F0Y2ggdGhlIEtMIGRpdmVyZ2VuY2UgdW50aWwgaXQgcGxhdGVhdXMiLCJVc2Ugb3BlblRTTkUgb3IgUkFQSURTIGN1TUwgZm9yIGxhcmdlIGRhdGFzZXRzIChuIFx1MDAzZSA1MCwwMDApIiwiQ29tYmluZSB0LVNORSB3aXRoIGNsdXN0ZXIgbGFiZWxzIGZyb20gay1tZWFucyBvciBIREJTQ0FOIGZvciBxdWFudGl0YXRpdmUgdmFsaWRhdGlvbiIsIk5ldmVyIHVzZSB0LVNORSBhcyBpbnB1dCBmZWF0dXJlcyBmb3IgZG93bnN0cmVhbSBtb2RlbHMg4oCUIHVzZSBQQ0Egb3IgVU1BUCBpbnN0ZWFkIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJSdW5uaW5nIHQtU05FIFJlbGlhYmx5IiwiY29udGVudCI6IkFsd2F5cyBwcmUtcmVkdWNlIHRvIDUwIFBDQSBkaW1lbnNpb25zIGJlZm9yZSB0LVNORSDigJQgaXQgcmVtb3ZlcyBub2lzZSBhbmQgY2FuIHJlZHVjZSB3YWxsIHRpbWUgMTDDly4gVXNlIGF0IGxlYXN0IDEwMDAgaXRlcmF0aW9ucyAobl9pdGVyPTEwMDApIGFuZCB3YWl0IGZvciB0aGUgS0wgZGl2ZXJnZW5jZSB0byBwbGF0ZWF1LiBSdW4gM+KAkzUgdGltZXMgd2l0aCBkaWZmZXJlbnQgcmFuZG9tIHNlZWRzOyBpZiB0aGUgaGlnaC1sZXZlbCBjbHVzdGVyIHRvcG9sb2d5IGNoYW5nZXMgZHJhbWF0aWNhbGx5IGJldHdlZW4gcnVucywgeW91ciBzYW1wbGUgc2l6ZSBtYXkgYmUgdG9vIHNtYWxsIGZvciBzdGFibGUgcmVzdWx0cy4ifSx7InR5cGUiOiJkaXZpZGVyIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJ0LVNORSBleGNlbHMgYXQgcHJvZHVjaW5nIHZpc3VhbGx5IGNvbXBlbGxpbmcgbG93LWRpbWVuc2lvbmFsIGxheW91dHMgdGhhdCByZXZlYWwgY2x1c3RlciBzdHJ1Y3R1cmUuIFVzZWQgY29ycmVjdGx5IOKAlCB3aXRoIGF3YXJlbmVzcyBvZiBpdHMgcGl0ZmFsbHMsIG11bHRpcGxlIHJ1bnMsIGFuZCBjb21wbGVtZW50YXJ5IHF1YW50aXRhdGl2ZSBhbmFseXNpcyDigJQgaXQgaXMgaW52YWx1YWJsZSBmb3IgZGF0YSBleHBsb3JhdGlvbi4gRm9yIHByZXNlcnZpbmcgZ2xvYmFsIHN0cnVjdHVyZSBvciBlbWJlZGRpbmcgbmV3IHBvaW50cywgVU1BUCBpcyBnZW5lcmFsbHkgdGhlIGJldHRlciBjaG9pY2UuIn1d"
---
# t-SNE — Perplexity, Crowding Problem, and Pitfalls

t-SNE (t-distributed Stochastic Neighbor Embedding) is a nonlinear dimensionality reduction technique designed to preserve local structure: nearby points in the high-dimensional space should remain nearby in the 2D or 3D embedding. It is the dominant technique for visualising high-dimensional data, but comes with severe pitfalls that make naive interpretation dangerous.

## High-Dimensional Similarities

For each pair of points i,j, t-SNE computes a conditional Gaussian similarity: pⱼ|ᵢ = exp(-‖xᵢ-xⱼ‖²/2σᵢ²) / Σₖ≠ᵢ exp(-‖xᵢ-xₖ‖²/2σᵢ²). The bandwidth σᵢ is tuned per point so that the perplexity Perp(Pᵢ) = 2^H(Pᵢ) matches the user-specified perplexity hyperparameter. The symmetrised joint probability is pᵢⱼ = (pⱼ|ᵢ + pᵢ|ⱼ)/(2n).

## Low-Dimensional Similarities and the Crowding Problem

The crowding problem: in high-dimensional space, many points can be roughly equidistant from a centre point (the sphere surface grows as rᵈ). When compressed to 2D, a Gaussian kernel would assign near-zero probability to all but a few neighbours — crushing many natural neighbours together in a tiny region. t-SNE fixes this by using a Student-t distribution with 1 degree of freedom (Cauchy) for low-dimensional similarities: qᵢⱼ = (1 + ‖yᵢ-yⱼ‖²)⁻¹ / Σₖ≠ₗ(1 + ‖yₖ-yₗ‖²)⁻¹. The heavy tails allocate much more probability mass to moderate distances.

```python
import numpy as np
import matplotlib.pyplot as plt

# Illustrate why Student-t solves the crowding problem
rng = np.random.default_rng(42)
d_high = 100  # intrinsic dimensionality of high-dim sphere

# Simulate distances from a centre point to neighbours on a sphere
distances = np.sqrt(rng.chisquare(d_high, size=2000) / d_high)

# Gaussian low-dim similarity (vanilla SNE)
sigma = 0.3
q_gauss = np.exp(-distances**2 / (2 * sigma**2))
q_gauss /= q_gauss.sum()

# Student-t similarity (t-SNE)
q_t = 1.0 / (1.0 + distances**2)
q_t /= q_t.sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(q_gauss * 1000, bins=80, alpha=0.7, color='steelblue')
axes[0].set_title('Gaussian q — crowded near zero')
axes[0].set_xlabel('Scaled similarity')

axes[1].hist(q_t * 1000, bins=80, alpha=0.7, color='coral')
axes[1].set_title('Student-t q — better spread')
axes[1].set_xlabel('Scaled similarity')

eff_gauss = (q_gauss > 0.001 / len(distances)).sum()
eff_t = (q_t > 0.001 / len(distances)).sum()
print(f'Effective neighbours (Gaussian): {eff_gauss}')
print(f'Effective neighbours (Student-t): {eff_t}')
```

## KL Divergence Objective

t-SNE minimises the Kullback-Leibler divergence between the high-dim joint distribution P and the low-dim distribution Q: Cost = KL(P‖Q) = Σᵢⱼ pᵢⱼ log(pᵢⱼ/qᵢⱼ). Because KL is asymmetric, placing well-separated high-dim neighbours (large pᵢⱼ) far in the low-dim space (small qᵢⱼ) incurs a large penalty. But placing non-neighbours (small pᵢⱼ) together incurs little cost — hence t-SNE can create spurious cluster structure.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# MNIST subset — pre-reduce with PCA first (recommended)
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X = mnist.data[:3000].astype(float)
y = mnist.target[:3000].astype(int)
X = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=50, random_state=42).fit_transform(X)

perplexities = [5, 30, 50, 100]
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

for ax, perp in zip(axes, perplexities):
    tsne = TSNE(n_components=2, perplexity=perp, random_state=42,
                n_iter=500, method='barnes_hut')
    X_tsne = tsne.fit_transform(X_pca)
    sc = ax.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', s=5, alpha=0.7)
    ax.set_title(f'Perplexity = {perp}')
    ax.axis('off')

plt.suptitle('t-SNE on MNIST — Effect of Perplexity', fontsize=13)
plt.colorbar(sc, ax=axes, label='Digit')
plt.tight_layout()
plt.show()
```

> **t-SNE Pitfalls**: Cluster sizes in t-SNE plots are meaningless — a large cluster does not mean more points. Inter-cluster distances are also meaningless — clusters far apart in 2D may be neighbours in high-dim space. t-SNE is stochastic; run it multiple times and compare. Perplexity dramatically changes apparent structure. Never draw quantitative conclusions from t-SNE alone.

## Barnes-Hut Approximation

Naïve t-SNE gradient computation costs O(n²) per iteration — intractable for n > 5,000. Barnes-Hut t-SNE uses a quad-tree (2D) or octree (3D) to approximate repulsive forces in O(n log n): cells far from a point contribute a single summarised force. This reduces wall time from hours to minutes for n ~ 10,000–100,000.

```python
import numpy as np
import time
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X = mnist.data[:5000].astype(float)
y = mnist.target[:5000]
X = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=50, random_state=42).fit_transform(X)

# sklearn TSNE with Barnes-Hut
t0 = time.time()
X_tsne_sk = TSNE(n_components=2, perplexity=30, random_state=42,
                  method='barnes_hut', n_iter=500).fit_transform(X_pca)
sk_time = time.time() - t0
print(f'sklearn TSNE (Barnes-Hut): {sk_time:.1f}s')

# openTSNE — faster, supports out-of-sample extension
try:
    from openTSNE import TSNE as openTSNE
    t0 = time.time()
    tsne_open = openTSNE(perplexity=30, random_state=42, n_jobs=-1, n_iter=500)
    X_tsne_open = tsne_open.fit(X_pca)
    open_time = time.time() - t0
    print(f'openTSNE: {open_time:.1f}s  (speedup: {sk_time / open_time:.1f}x)')
    # Out-of-sample: embed new points without refitting
    X_new_embedded = tsne_open.transform(X_pca[:50])
    print(f'New points embedded shape: {X_new_embedded.shape}')
except ImportError:
    print('pip install opentsne for faster t-SNE')
```

## Demonstrating Pitfalls with Synthetic Data

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

rng = np.random.default_rng(42)

# Three clusters: different sizes AND different densities
small_tight = rng.normal([0, 0], 0.5, (20, 10))
large_spread = rng.normal([8, 0], 3.0, (200, 10))
small_far = rng.normal([20, 0], 0.5, (20, 10))

X = np.vstack([small_tight, large_spread, small_far])
labels = np.array([0]*20 + [1]*200 + [2]*20)

# PCA — shows true relative positions
from sklearn.decomposition import PCA
X_pca = PCA(n_components=2).fit_transform(X)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='Set1', s=20)
axes[0].set_title('PCA — true: different sizes & distances')

# t-SNE — distorts both cluster size and inter-cluster distance
X_tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=1000).fit_transform(X)
axes[1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels, cmap='Set1', s=20)
axes[1].set_title('t-SNE — sizes and distances ARE MEANINGLESS')
plt.suptitle('t-SNE Pitfall: Cluster Size and Distance Not Preserved')
plt.tight_layout()
plt.show()
```

## Pitfall Reference Table

| Myth | Reality | Why |
| --- | --- | --- |
| Cluster size indicates number of points | False — size is arbitrary | KL asymmetry allows compact or expanded clusters |
| Distance between clusters is meaningful | False — only local structure preserved | Repulsive forces push all clusters apart similarly |
| A single t-SNE plot is enough | False — always try multiple seeds | Objective has many local minima |
| Perplexity does not matter much | False — it controls neighbourhood radius | Low perplexity → fragmented; high → merged clusters |
| Isolated points are genuine outliers | False — may be misplaced by crowding | Points with few neighbours are pushed far away |

## Practical Recommendations

- Pre-reduce with PCA to 50 dimensions before running t-SNE — reduces noise and speeds computation
- Use perplexity in the range 5–50 for most datasets; try several values and compare
- Run for at least 1000 iterations; watch the KL divergence until it plateaus
- Use openTSNE or RAPIDS cuML for large datasets (n > 50,000)
- Combine t-SNE with cluster labels from k-means or HDBSCAN for quantitative validation
- Never use t-SNE as input features for downstream models — use PCA or UMAP instead

> **Running t-SNE Reliably**: Always pre-reduce to 50 PCA dimensions before t-SNE — it removes noise and can reduce wall time 10×. Use at least 1000 iterations (n_iter=1000) and wait for the KL divergence to plateau. Run 3–5 times with different random seeds; if the high-level cluster topology changes dramatically between runs, your sample size may be too small for stable results.

---

t-SNE excels at producing visually compelling low-dimensional layouts that reveal cluster structure. Used correctly — with awareness of its pitfalls, multiple runs, and complementary quantitative analysis — it is invaluable for data exploration. For preserving global structure or embedding new points, UMAP is generally the better choice.

