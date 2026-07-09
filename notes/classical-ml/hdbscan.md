---
title: "HDBSCAN — Hierarchical Density-Based Clustering"
slug: "hdbscan"
description: "Understand how HDBSCAN extends DBSCAN to handle variable-density clusters: mutual reachability distance, minimum spanning tree, cluster hierarchy condensation, stability-based cluster extraction, soft membership probabilities, and outlier scores for anomaly detection."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiSERCU0NBTiAoSGllcmFyY2hpY2FsIERCU0NBTikgc29sdmVzIERCU0NBTlx1MDAyN3MgZnVuZGFtZW50YWwgbGltaXRhdGlvbjogYSBzaW5nbGUgZ2xvYmFsIGRlbnNpdHkgdGhyZXNob2xkIGNhbm5vdCBzaW11bHRhbmVvdXNseSBoYW5kbGUgY2x1c3RlcnMgb2YgZGlmZmVyZW50IGRlbnNpdGllcy4gSERCU0NBTiBpbnN0ZWFkIGJ1aWxkcyBhIGhpZXJhcmNoeSBvZiBjbHVzdGVyaW5ncyBhY3Jvc3MgYWxsIGRlbnNpdHkgbGV2ZWxzLCB0aGVuIGV4dHJhY3RzIHRoZSBtb3N0IHN0YWJsZSAocGVyc2lzdGVudCkgZmxhdCBjbHVzdGVyaW5nIGZyb20gdGhlIGhpZXJhcmNoeS4gVGhlIHJlc3VsdCBpcyBhbiBhbGdvcml0aG0gdGhhdCBmaW5kcyB2YXJpYWJsZS1kZW5zaXR5IGNsdXN0ZXJzLCBhc3NpZ25zIG1lbWJlcnNoaXAgcHJvYmFiaWxpdGllcywgYW5kIGNvbXB1dGVzIG91dGxpZXIgc2NvcmVzIOKAlCBhbGwgZnJvbSBhIHNpbmdsZSBwYXNzIHdpdGggYSBzaW5nbGUgcGFyYW1ldGVyIChtaW5fY2x1c3Rlcl9zaXplKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJGcm9tIERCU0NBTiB0byBIREJTQ0FOIOKAlCBUaGUgQ29yZSBEaXN0YW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSERCU0NBTiB0cmFuc2Zvcm1zIHRoZSBkaXN0YW5jZSBtZXRyaWMgdXNpbmcgdGhlIGNvcmUgZGlzdGFuY2U6IGNvcmVfayh4KSA9IGRpc3RhbmNlIHRvIHRoZSBrLXRoIG5lYXJlc3QgbmVpZ2hib3Igb2YgeCAod2hlcmUgayA9IG1pbl9zYW1wbGVzKS4gVGhlIG11dHVhbCByZWFjaGFiaWxpdHkgZGlzdGFuY2UgYmV0d2VlbiB0d28gcG9pbnRzIGlzIG1yZWFjaF9rKGEsYikgPSBtYXgoY29yZV9rKGEpLCBjb3JlX2soYiksIGRpc3QoYSxiKSkuIFRoaXMgdHJhbnNmb3JtYXRpb24gbWFrZXMgc3BhcnNlIHBvaW50cyBhcHBlYXIgZmFydGhlciBmcm9tIGV2ZXJ5dGhpbmcgKHRoZWlyIGNvcmUgZGlzdGFuY2UgaXMgbGFyZ2UpLCBzbW9vdGhpbmcgb3V0IG5vaXNlIGFuZCBnaXZpbmcgYSBub2lzZS1yb2J1c3QgZGlzdGFuY2UgbWVhc3VyZS4gQnkgY29tcHV0aW5nIHRoZSBtaW5pbXVtIHNwYW5uaW5nIHRyZWUgb2YgYWxsIHBhaXJ3aXNlIG11dHVhbCByZWFjaGFiaWxpdHkgZGlzdGFuY2VzLCBIREJTQ0FOIGNyZWF0ZXMgYSBjb21wbGV0ZSBoaWVyYXJjaHkgaW4gb25lIHN0ZXAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQnVpbGRpbmcgdGhlIEhpZXJhcmNoeSDigJQgRml2ZSBTdGVwcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIEhEQlNDQU4gcGlwZWxpbmU6ICgxKSBDb21wdXRlIGNvcmUgZGlzdGFuY2VzIGZvciBlYWNoIHBvaW50IHVzaW5nIGs9bWluX3NhbXBsZXMgbmVhcmVzdCBuZWlnaGJvcnMuICgyKSBDb21wdXRlIG11dHVhbCByZWFjaGFiaWxpdHkgZGlzdGFuY2VzIGJldHdlZW4gYWxsIHBhaXJzLiAoMykgQnVpbGQgdGhlIG1pbmltdW0gc3Bhbm5pbmcgdHJlZSAoTVNUKSBvZiB0aGUgbXV0dWFsIHJlYWNoYWJpbGl0eSBncmFwaCDigJQgTyhuwrIgbG9nIG4pIG5haXZlbHksIE8obiBsb2cgbikgd2l0aCBCb3LFr3ZrYVx1MDAyN3MgYWxnb3JpdGhtIG9uIHRoZSBrLU5OIGdyYXBoLiAoNCkgQ29udmVydCB0aGUgTVNUIHRvIGEgZGVuZHJvZ3JhbSBieSBzb3J0aW5nIGVkZ2Ugd2VpZ2h0czogcmVtb3ZpbmcgZWRnZXMgaW4gZGVjcmVhc2luZyB3ZWlnaHQgb3JkZXIgdHJhY2VzIHRoZSBjbHVzdGVyIGhpZXJhcmNoeS4gKDUpIENvbmRlbnNlIHRoZSBkZW5kcm9ncmFtIGJ5IG9ubHkgcmVjb3JkaW5nIHNwbGl0cyB3aGVyZSBhdCBsZWFzdCBvbmUgcmVzdWx0aW5nIGNsdXN0ZXIgaGFzIOKJpSBtaW5fY2x1c3Rlcl9zaXplIHBvaW50czsgYnJhbmNoZXMgdGhhdCBhcmUgdG9vIHNtYWxsIGJlY29tZSBwb2ludC1sZXZlbCBsZWF2ZXMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOnRydWUsIml0ZW1zIjpbIkNvbXB1dGUgY29yZV9rKHgpIGZvciBhbGwgeDogZGlzdGFuY2UgdG8gay10aCBuZWFyZXN0IG5laWdoYm9yLiIsIkNvbXB1dGUgbXJlYWNoKGEsYikgPSBtYXgoY29yZV9rKGEpLCBjb3JlX2soYiksIGRpc3QoYSxiKSkgZm9yIGFsbCBwYWlycy4iLCJCdWlsZCBtaW5pbXVtIHNwYW5uaW5nIHRyZWUgb24gdGhlIG11dHVhbCByZWFjaGFiaWxpdHkgZ3JhcGgg4oCUIE8obiBsb2cgbikgd2l0aCBCb3LFr3ZrYS4iLCJTb3J0IE1TVCBlZGdlcyBieSB3ZWlnaHQgYW5kIHJlbW92ZSBpbiBkZWNyZWFzaW5nIG9yZGVyIHRvIGJ1aWxkIHRoZSBkZW5kcm9ncmFtLiIsIkNvbmRlbnNlOiBvbmx5IHJlY29yZCBzcGxpdHMgd2hlcmUgY2hpbGQgY2x1c3RlciBzaXplIOKJpSBtaW5fY2x1c3Rlcl9zaXplOyBzbWFsbCBzcGxpdHMgYmVjb21lIG5vaXNlLiIsIkV4dHJhY3Qgc3RhYmxlIGNsdXN0ZXJzIGJ5IG1heGltaXppbmcgdGhlIHRvdGFsIHN0YWJpbGl0eSDOo197eOKIiEN9ICjOu19kZWF0aCh4KSDiiJIgzrtfYmlydGgoQykpLiJdfSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfYmxvYnMsIG1ha2VfbW9vbnNcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG50cnk6XG4gICAgaW1wb3J0IGhkYnNjYW5cbiAgICBIQVNfSERCU0NBTiA9IFRydWVcbmV4Y2VwdCBJbXBvcnRFcnJvcjpcbiAgICBIQVNfSERCU0NBTiA9IEZhbHNlXG4gICAgcHJpbnQoXCJJbnN0YWxsOiBwaXAgaW5zdGFsbCBoZGJzY2FuXCIpXG5cbmlmIEhBU19IREJTQ0FOOlxuICAgICMgVmFyaWFibGUtZGVuc2l0eSBkYXRhOiB0aWdodCBjbHVzdGVyICsgc3ByZWFkIGNsdXN0ZXJcbiAgICBybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG4gICAgWF90aWdodCA9IHJuZy5ub3JtYWwoWzAsIDBdLCAwLjIsICgxMDAsIDIpKVxuICAgIFhfc3ByZWFkID0gcm5nLm5vcm1hbChbNSwgMF0sIDEuNSwgKDIwMCwgMikpXG4gICAgWF9ub2lzZSA9IHJuZy51bmlmb3JtKC0yLCA4LCAoMjAsIDIpKVxuICAgIFggPSBucC52c3RhY2soW1hfdGlnaHQsIFhfc3ByZWFkLCBYX25vaXNlXSlcblxuICAgIGNsdXN0ZXJlciA9IGhkYnNjYW4uSERCU0NBTihtaW5fY2x1c3Rlcl9zaXplPTE1LCBtaW5fc2FtcGxlcz01LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByZWRpY3Rpb25fZGF0YT1UcnVlKVxuICAgIGNsdXN0ZXJlci5maXQoWClcbiAgICBsYWJlbHMgPSBjbHVzdGVyZXIubGFiZWxzX1xuICAgIG5fY2x1c3RlcnMgPSBsZW4oc2V0KGxhYmVscykpIC0gKDEgaWYgLTEgaW4gbGFiZWxzIGVsc2UgMClcbiAgICBuX25vaXNlID0gKGxhYmVscyA9PSAtMSkuc3VtKClcbiAgICBwcmludChmXCJGb3VuZCB7bl9jbHVzdGVyc30gY2x1c3RlcnMsIHtuX25vaXNlfSBub2lzZSBwb2ludHNcIilcbiAgICBwcmludChmXCJDbHVzdGVyIHNpemVzOiB7WyhsYWJlbHM9PWkpLnN1bSgpIGZvciBpIGluIHJhbmdlKG5fY2x1c3RlcnMpXX1cIilcbiAgICBwcmludChmXCJDbHVzdGVyIHBlcnNpc3RlbmNlIChzdGFiaWxpdHkpOiB7Y2x1c3RlcmVyLmNsdXN0ZXJfcGVyc2lzdGVuY2VffVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNsdXN0ZXIgU3RhYmlsaXR5IGFuZCBFeHRyYWN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFYWNoIGNsdXN0ZXIgQyBpbiB0aGUgY29uZGVuc2VkIGhpZXJhcmNoeSBoYXMgYSBiaXJ0aCBsZXZlbCDOu19iaXJ0aChDKSA9IDEvzrVfc3BsaXQgKHRoZSBkZW5zaXR5IGF0IHdoaWNoIEMgc3BsaXQgZnJvbSBpdHMgcGFyZW50KSBhbmQgYSBkZWF0aCBsZXZlbCDOu19kZWF0aCh4KSA9IDEvzrVfZmFsbCBmb3IgZWFjaCBtZW1iZXIgeCAodGhlIGRlbnNpdHkgYXQgd2hpY2ggeCBmYWxscyBvdXQgb2YgdGhlIGNsdXN0ZXIpLiBUaGUgc3RhYmlsaXR5IG9mIGNsdXN0ZXIgQyBpcyDOo197eOKIiEN9ICjOu19kZWF0aCh4KSDiiJIgzrtfYmlydGgoQykpLiBUaGUgZmxhdCBjbHVzdGVyaW5nIHRoYXQgbWF4aW1pemVzIHRvdGFsIHN0YWJpbGl0eSBpcyBmb3VuZCBieSBhIGJvdHRvbS11cCB0cmVlIHRyYXZlcnNhbDogYSBjbHVzdGVyIGlzIHNlbGVjdGVkIGlmIGl0cyBvd24gc3RhYmlsaXR5IGV4Y2VlZHMgdGhlIHN1bSBvZiBzdGFiaWxpdGllcyBvZiBpdHMgc3ViLWNsdXN0ZXJzLiBUaGlzIGdyZWVkeSBhbGdvcml0aG0gcnVucyBpbiBPKG4pIGFmdGVyIHRoZSBoaWVyYXJjaHkgaXMgYnVpbHQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5pZiBIQVNfSERCU0NBTjpcbiAgICBmcm9tIGhkYnNjYW4gaW1wb3J0IEhEQlNDQU5cbiAgICBmcm9tIGhkYnNjYW4ucHJlZGljdGlvbiBpbXBvcnQgYXBwcm94aW1hdGVfcHJlZGljdFxuICAgIGZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9ibG9ic1xuXG4gICAgWF90cmFpbiwgeV90cnVlID0gbWFrZV9ibG9icyhuX3NhbXBsZXM9NDAwLCBjZW50ZXJzPTQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNsdXN0ZXJfc3RkPVswLjMsIDAuOCwgMC41LCAxLjJdLCByYW5kb21fc3RhdGU9NylcbiAgICBjbHVzdGVyZXIgPSBIREJTQ0FOKG1pbl9jbHVzdGVyX3NpemU9MjAsIG1pbl9zYW1wbGVzPTUsIHByZWRpY3Rpb25fZGF0YT1UcnVlKVxuICAgIGNsdXN0ZXJlci5maXQoWF90cmFpbilcblxuICAgICMgU29mdCBjbHVzdGVyaW5nIOKAlCBtZW1iZXJzaGlwIHByb2JhYmlsaXRpZXNcbiAgICBzb2Z0X2xhYmVscywgc3RyZW5ndGhzID0gaGRic2Nhbi5hbGxfcG9pbnRzX21lbWJlcnNoaXBfdmVjdG9ycyhjbHVzdGVyZXIpXG4gICAgaGFyZF9sYWJlbHMgPSBucC5hcmdtYXgoc29mdF9sYWJlbHMsIGF4aXM9MSlcblxuICAgIHByaW50KGZcIlNvZnQgY2x1c3RlciBtZW1iZXJzaGlwIHNoYXBlOiB7c29mdF9sYWJlbHMuc2hhcGV9XCIpXG4gICAgcHJpbnQoZlwiTWVhbiBtZW1iZXJzaGlwIHN0cmVuZ3RoIChjb25maWRlbmNlKToge3N0cmVuZ3Rocy5tZWFuKCk6LjRmfVwiKVxuICAgICMgUG9pbnRzIHdpdGggbG93IG1heCBtZW1iZXJzaGlwIGFyZSB1bmNlcnRhaW4gLyBub2lzZS1saWtlXG4gICAgdW5jZXJ0YWluID0gKHNvZnRfbGFiZWxzLm1heChheGlzPTEpIFx1MDAzYyAwLjUpLnN1bSgpXG4gICAgcHJpbnQoZlwiUG9pbnRzIHdpdGggYW1iaWd1b3VzIG1lbWJlcnNoaXAgKFx1MDAzYzUwJSBtYXggcHJvYik6IHt1bmNlcnRhaW59XCIpXG4gICAgZm9yIGkgaW4gcmFuZ2Uoc29mdF9sYWJlbHMuc2hhcGVbMV0pOlxuICAgICAgICBwcmludChmXCIgIENvbXBvbmVudCB7aX06IHsoaGFyZF9sYWJlbHMgPT0gaSkuc3VtKCl9IGhhcmQtYXNzaWduZWQsIFwiXG4gICAgICAgICAgICAgIGZcIm1lYW4gcHJvYj17c29mdF9sYWJlbHNbOiwgaV0ubWVhbigpOi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPdXRsaWVyIFNjb3JlcyBmb3IgQW5vbWFseSBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkhEQlNDQU4gY29tcHV0ZXMgYW4gb3V0bGllciBzY29yZSBmb3IgZXZlcnkgcG9pbnQ6IHRoZSBHTE9TSCAoR2xvYmFsLUxvY2FsIE91dGxpZXIgU2NvcmUgZnJvbSBIaWVyYXJjaGllcykgc2NvcmUuIEEgcG9pbnRcdTAwMjdzIG91dGxpZXIgc2NvcmUgaXMgMSDiiJIgbWF4X21lbWJlcnNoaXBfcHJvYmFiaWxpdHkg4oiIIFswLDFdLiBQb2ludHMgbmV2ZXIgYmVsb25naW5nIHRvIGFueSBjbHVzdGVyIGhhdmUgc2NvcmUgMTsgY29yZSBtZW1iZXJzIG9mIGRlbnNlIGNsdXN0ZXJzIGhhdmUgc2NvcmVzIG5lYXIgMC4gVGhpcyBnaXZlcyBhIGNvbnRpbnVvdXMgb3V0bGllciByYW5raW5nIHRoYXQgY2FuIGJlIHRocmVzaG9sZGVkIHRvIGZsYWcgYW5vbWFsaWVzLCBtYWtpbmcgSERCU0NBTiBhIG5hdHVyYWwgb25lLWNsYXNzIGFub21hbHkgZGV0ZWN0b3Ig4oCUIGZpdCBvbiBub3JtYWwgZGF0YSwgdGhlbiBmbGFnIHBvaW50cyB3aXRoIGhpZ2ggb3V0bGllciBzY29yZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5pZiBIQVNfSERCU0NBTjpcbiAgICBmcm9tIGhkYnNjYW4gaW1wb3J0IEhEQlNDQU5cbiAgICBmcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuICAgIHJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZygwKVxuICAgIFhfbm9ybWFsID0gcm5nLm11bHRpdmFyaWF0ZV9ub3JtYWwoWzAsIDBdLCBbWzEsIDAuNV0sIFswLjUsIDFdXSwgNDAwKVxuICAgIFhfYW5vbWFseSA9IHJuZy51bmlmb3JtKC01LCA1LCAoMjAsIDIpKVxuICAgIFhfYWxsID0gbnAudnN0YWNrKFtYX25vcm1hbCwgWF9hbm9tYWx5XSlcbiAgICB5X3RydWUgPSBucC5hcnJheShbMF0qNDAwICsgWzFdKjIwKVxuXG4gICAgWF9hbGwgPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWF9hbGwpXG4gICAgY2x1c3RlcmVyID0gSERCU0NBTihtaW5fY2x1c3Rlcl9zaXplPTIwLCBtaW5fc2FtcGxlcz01LCBwcmVkaWN0aW9uX2RhdGE9VHJ1ZSlcbiAgICBjbHVzdGVyZXIuZml0KFhfYWxsKVxuXG4gICAgc2NvcmVzID0gY2x1c3RlcmVyLm91dGxpZXJfc2NvcmVzX1xuICAgIHRocmVzaG9sZCA9IG5wLnBlcmNlbnRpbGUoc2NvcmVzLCA5NSlcbiAgICBmbGFnZ2VkID0gKHNjb3JlcyBcdTAwM2UgdGhyZXNob2xkKS5hc3R5cGUoaW50KVxuXG4gICAgZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IHByZWNpc2lvbl9zY29yZSwgcmVjYWxsX3Njb3JlLCBmMV9zY29yZVxuICAgIHByaW50KGZcIk91dGxpZXIgc2NvcmUgdGhyZXNob2xkICg5NXRoIHBjdCk6IHt0aHJlc2hvbGQ6LjRmfVwiKVxuICAgIHByaW50KGZcIlByZWNpc2lvbjoge3ByZWNpc2lvbl9zY29yZSh5X3RydWUsIGZsYWdnZWQpOi40Zn1cIilcbiAgICBwcmludChmXCJSZWNhbGw6ICAgIHtyZWNhbGxfc2NvcmUoeV90cnVlLCBmbGFnZ2VkKTouNGZ9XCIpXG4gICAgcHJpbnQoZlwiRjE6ICAgICAgICB7ZjFfc2NvcmUoeV90cnVlLCBmbGFnZ2VkKTouNGZ9XCIpXG4gICAgcHJpbnQoZlwiTWVhbiBzY29yZSDigJQgbm9ybWFsOiB7c2NvcmVzWzo0MDBdLm1lYW4oKTouNGZ9LCBhbm9tYWx5OiB7c2NvcmVzWzQwMDpdLm1lYW4oKTouNGZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSERCU0NBTiB2cyBEQlNDQU4g4oCUIFdoZW4gdG8gQ2hvb3NlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEQlNDQU4gaXMgc2ltcGxlciBhbmQgaW50ZXJwcmV0YWJsZTogaWYgeW91IGtub3cgdGhlIGRlbnNpdHkgc2NhbGUgb2YgeW91ciBkYXRhIGFuZCBjbHVzdGVycyBoYXZlIHJvdWdobHkgdW5pZm9ybSBkZW5zaXR5LCBEQlNDQU4gd2l0aCB0aGUgay1kaXN0YW5jZS1lbGJvdyDOtSBpcyBvZnRlbiBzdWZmaWNpZW50LiBIREJTQ0FOIGlzIHN0cmljdGx5IG1vcmUgcG93ZXJmdWwgYnV0IHNsb3dlciB0byBidWlsZCBhbmQgaGFyZGVyIHRvIGludGVycHJldC4gQ2hvb3NlIEhEQlNDQU4gd2hlbjogY2x1c3RlcnMgaGF2ZSB2YXJpYWJsZSBkZW5zaXR5LCB5b3Ugd2FudCBzb2Z0IG1lbWJlcnNoaXAgcHJvYmFiaWxpdGllcywgeW91IG5lZWQgY29udGludW91cyBvdXRsaWVyIHNjb3Jlcywgb3IgeW91IHdhbnQgcm9idXN0bmVzcyB0byB0aGUgzrUgcGFyYW1ldGVyLiBIREJTQ0FOXHUwMDI3cyBwcmltYXJ5IHBhcmFtZXRlciBtaW5fY2x1c3Rlcl9zaXplIGlzIG1vcmUgaW50dWl0aXZlIHRoYW4gzrUgYmVjYXVzZSBpdCBzcGVjaWZpZXMgbWluaW11bSBjbHVzdGVyIHNpemUgcmF0aGVyIHRoYW4gYSBnZW9tZXRyaWMgZGlzdGFuY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmNsdXN0ZXIgaW1wb3J0IERCU0NBTlxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFkanVzdGVkX3JhbmRfc2NvcmVcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ybmcgPSBucC5yYW5kb20uZGVmYXVsdF9ybmcoNDIpXG4jIFZhcmlhYmxlLWRlbnNpdHkgY2x1c3RlcnM6IG9uZSB0aWdodCwgb25lIHNwcmVhZFxuWF90aWdodCA9IHJuZy5ub3JtYWwoWzAsIDBdLCAwLjMsICgxNTAsIDIpKVxuWF9zcHJlYWQgPSBybmcubm9ybWFsKFs0LCAwXSwgMS44LCAoMTUwLCAyKSlcblggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0obnAudnN0YWNrKFtYX3RpZ2h0LCBYX3NwcmVhZF0pKVxueV90cnVlID0gbnAuYXJyYXkoWzBdKjE1MCArIFsxXSoxNTApXG5cbiMgREJTQ0FOIG5lZWRzIGRpZmZlcmVudCBlcHMgZm9yIGRpZmZlcmVudCBkZW5zaXRpZXNcbmZvciBlcHMgaW4gWzAuMTUsIDAuMywgMC41LCAwLjhdOlxuICAgIGRiID0gREJTQ0FOKGVwcz1lcHMsIG1pbl9zYW1wbGVzPTUpLmZpdChYKVxuICAgIG5fY2wgPSBsZW4oc2V0KGRiLmxhYmVsc18pKSAtICgxIGlmIC0xIGluIGRiLmxhYmVsc18gZWxzZSAwKVxuICAgIGFyaSA9IGFkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCBkYi5sYWJlbHNfKSBpZiBuX2NsIFx1MDAzZSAwIGVsc2UgMC4wXG4gICAgbm9pc2UgPSAoZGIubGFiZWxzXyA9PSAtMSkuc3VtKClcbiAgICBwcmludChmXCJEQlNDQU4gZXBzPXtlcHM6LjJmfToge25fY2x9IGNsdXN0ZXJzLCB7bm9pc2V9IG5vaXNlLCBBUkk9e2FyaTouNGZ9XCIpXG5cbmlmIEhBU19IREJTQ0FOOlxuICAgIGhkYiA9IGhkYnNjYW4uSERCU0NBTihtaW5fY2x1c3Rlcl9zaXplPTIwLCBtaW5fc2FtcGxlcz01KS5maXQoWClcbiAgICBuX2NsID0gbGVuKHNldChoZGIubGFiZWxzXykpIC0gKDEgaWYgLTEgaW4gaGRiLmxhYmVsc18gZWxzZSAwKVxuICAgIGFyaSA9IGFkanVzdGVkX3JhbmRfc2NvcmUoeV90cnVlLCBoZGIubGFiZWxzXylcbiAgICBwcmludChmXCJcXG5IREJTQ0FOOiB7bl9jbH0gY2x1c3RlcnMsIHsoaGRiLmxhYmVsc189PS0xKS5zdW0oKX0gbm9pc2UsIEFSST17YXJpOi40Zn1cIikifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiUGFyYW1ldGVyIFR1bmluZyBHdWlkZSIsImNvbnRlbnQiOiJTZXQgbWluX2NsdXN0ZXJfc2l6ZSB0byB0aGUgbWluaW11bSBudW1iZXIgb2YgcG9pbnRzIHlvdSB3b3VsZCBhY2NlcHQgYXMgYSBtZWFuaW5nZnVsIGNsdXN0ZXIgKGRvbWFpbiBrbm93bGVkZ2UpLiBTZXQgbWluX3NhbXBsZXMgKGFuYWxvZ291cyB0byBtaW5QdHMpIGVxdWFsIHRvIG1pbl9jbHVzdGVyX3NpemUgZm9yIHNpbXBsaWNpdHksIG9yIGxvd2VyIHRvIGFsbG93IHNwYXJzZXIgY2x1c3RlcnMuIFVubGlrZSBEQlNDQU5cdTAwMjdzIM61LCB0aGVzZSBwYXJhbWV0ZXJzIGhhdmUgaW50dWl0aXZlIHVuaXRzLiBIREJTQ0FOIGlzIHJvYnVzdCB0byBtaW5fY2x1c3Rlcl9zaXplIHdpdGhpbiBhbiBvcmRlciBvZiBtYWduaXR1ZGU7IGxhcmdlIGNoYW5nZXMgYXJlIG5lZWRlZCB0byBtYXRlcmlhbGx5IGNoYW5nZSB0aGUgcmVzdWx0LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBXb3JrZmxvdyBhbmQgSW5zdGFsbGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgaGRic2NhbiBwYWNrYWdlIChwaXAgaW5zdGFsbCBoZGJzY2FuKSBwcm92aWRlcyB0aGUgcmVmZXJlbmNlIGltcGxlbWVudGF0aW9uIHdpdGggQyBleHRlbnNpb25zIGZvciBzcGVlZC4gU2tsZWFybiAxLjMrIGFsc28gaW5jbHVkZXMgSERCU0NBTiB2aWEgc2tsZWFybi5jbHVzdGVyLkhEQlNDQU4uIFRoZSBza2xlYXJuIHZlcnNpb24gaW50ZWdyYXRlcyBjbGVhbmx5IGludG8gc2tsZWFybiBwaXBlbGluZXMgYnV0IGxhY2tzIHRoZSBzb2Z0IGNsdXN0ZXJpbmcgYW5kIG91dGxpZXIgc2NvcmUgQVBJLiBGb3IgcHJvZHVjdGlvbiB1c2U6ICgxKSBmaXQgSERCU0NBTiBvbiB0cmFpbmluZyBkYXRhOyAoMikgdXNlIGFwcHJveGltYXRlX3ByZWRpY3QgZm9yIG5ldyBwb2ludHMgKHJlcXVpcmVzIHByZWRpY3Rpb25fZGF0YT1UcnVlKTsgKDMpIGZsYWcgcG9pbnRzIHdpdGggb3V0bGllciBzY29yZSBhYm92ZSB0aGUgOTV0aOKAkzk5dGggcGVyY2VudGlsZSBvZiB0cmFpbmluZyBzY29yZXMgYXMgYW5vbWFsaWVzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsibWluX2NsdXN0ZXJfc2l6ZTogcHJpbWFyeSBwYXJhbWV0ZXIg4oCUIHNldCB0byB0aGUgbWluaW11bSBtZWFuaW5nZnVsIGNsdXN0ZXIgc2l6ZSBpbiB5b3VyIGRvbWFpbiAoZS5nLiwgNTAgZm9yIGN1c3RvbWVyIHNlZ21lbnRzLCA1IGZvciBhbm9tYWx5IGRldGVjdGlvbikuIiwibWluX3NhbXBsZXM6IGNvbnRyb2xzIG5vaXNlIHJvYnVzdG5lc3Mg4oCUIGhpZ2hlciB2YWx1ZXMgcHJvZHVjZSBtb3JlIG5vaXNlIHBvaW50cyBidXQgbW9yZSBjb25maWRlbnQgY2x1c3RlcnMuIERlZmF1bHQ6IG1pbl9jbHVzdGVyX3NpemUuIiwiY2x1c3Rlcl9zZWxlY3Rpb25fbWV0aG9kOiBcdTAwMjdlb21cdTAwMjcgKGV4Y2VzcyBvZiBtYXNzLCBkZWZhdWx0KSBtYXhpbWl6ZXMgc3RhYmlsaXR5OyBcdTAwMjdsZWFmXHUwMDI3IHNlbGVjdHMgdGhlIGZpbmVzdC1ncmFpbmVkIGNsdXN0ZXJzIGZyb20gdGhlIGhpZXJhcmNoeS4iLCJhbHBoYTogY29udHJvbHMgaG93IGNvbnNlcnZhdGl2ZWx5IHRoZSBtdXR1YWwgcmVhY2hhYmlsaXR5IGdyYXBoIGlzIGJ1aWx0IChkZWZhdWx0IDEuMCkuIFJhcmVseSBuZWVkcyB0dW5pbmcuIiwibWV0cmljOiBzdXBwb3J0cyBhbnkgc2tsZWFybiBkaXN0YW5jZSBtZXRyaWMg4oCUIFx1MDAyN2V1Y2xpZGVhblx1MDAyNyAoZGVmYXVsdCksIFx1MDAyN21hbmhhdHRhblx1MDAyNywgXHUwMDI3Y29zaW5lXHUwMDI3IGZvciB0ZXh0L2hpZ2gtZCBkYXRhLiJdfSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRmVhdHVyZSIsIkRCU0NBTiIsIkhEQlNDQU4iXSwicm93cyI6W1siS2V5IHBhcmFtZXRlcnMiLCLOtSAocmFkaXVzKSwgbWluUHRzIiwibWluX2NsdXN0ZXJfc2l6ZSwgbWluX3NhbXBsZXMiXSxbIlZhcmlhYmxlIGRlbnNpdHkgY2x1c3RlcnMiLCJObyDigJQgc2luZ2xlIGdsb2JhbCB0aHJlc2hvbGQiLCJZZXMg4oCUIG11bHRpLXNjYWxlIGhpZXJhcmNoeSJdLFsiU29mdCBtZW1iZXJzaGlwIiwiTm8g4oCUIGhhcmQgYXNzaWdubWVudCIsIlllcyDigJQgbWVtYmVyc2hpcCBwcm9iYWJpbGl0aWVzIl0sWyJPdXRsaWVyIHNjb3JlcyIsIkJpbmFyeSAobm9pc2Uvbm90KSIsIkNvbnRpbnVvdXMgR0xPU0ggc2NvcmUiXSxbIkNsdXN0ZXIgc3RhYmlsaXR5IiwiTm8iLCJZZXMg4oCUIHBlcnNpc3RlbmNlLXdlaWdodGVkIGV4dHJhY3Rpb24iXSxbIkNvbXBsZXhpdHkiLCJPKG4gbG9nIG4pIHdpdGggaW5kZXgiLCJPKG4gbG9nIG4pIHdpdGggQm9yxa92a2EiXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# HDBSCAN — Hierarchical Density-Based Clustering

HDBSCAN (Hierarchical DBSCAN) solves DBSCAN's fundamental limitation: a single global density threshold cannot simultaneously handle clusters of different densities. HDBSCAN instead builds a hierarchy of clusterings across all density levels, then extracts the most stable (persistent) flat clustering from the hierarchy. The result is an algorithm that finds variable-density clusters, assigns membership probabilities, and computes outlier scores — all from a single pass with a single parameter (min_cluster_size).

## From DBSCAN to HDBSCAN — The Core Distance

HDBSCAN transforms the distance metric using the core distance: core_k(x) = distance to the k-th nearest neighbor of x (where k = min_samples). The mutual reachability distance between two points is mreach_k(a,b) = max(core_k(a), core_k(b), dist(a,b)). This transformation makes sparse points appear farther from everything (their core distance is large), smoothing out noise and giving a noise-robust distance measure. By computing the minimum spanning tree of all pairwise mutual reachability distances, HDBSCAN creates a complete hierarchy in one step.

## Building the Hierarchy — Five Steps

The HDBSCAN pipeline: (1) Compute core distances for each point using k=min_samples nearest neighbors. (2) Compute mutual reachability distances between all pairs. (3) Build the minimum spanning tree (MST) of the mutual reachability graph — O(n² log n) naively, O(n log n) with Borůvka's algorithm on the k-NN graph. (4) Convert the MST to a dendrogram by sorting edge weights: removing edges in decreasing weight order traces the cluster hierarchy. (5) Condense the dendrogram by only recording splits where at least one resulting cluster has ≥ min_cluster_size points; branches that are too small become point-level leaves.

1. Compute core_k(x) for all x: distance to k-th nearest neighbor.
2. Compute mreach(a,b) = max(core_k(a), core_k(b), dist(a,b)) for all pairs.
3. Build minimum spanning tree on the mutual reachability graph — O(n log n) with Borůvka.
4. Sort MST edges by weight and remove in decreasing order to build the dendrogram.
5. Condense: only record splits where child cluster size ≥ min_cluster_size; small splits become noise.
6. Extract stable clusters by maximizing the total stability Σ_{x∈C} (λ_death(x) − λ_birth(C)).

```python
import numpy as np
from sklearn.datasets import make_blobs, make_moons
from sklearn.preprocessing import StandardScaler

try:
    import hdbscan
    HAS_HDBSCAN = True
except ImportError:
    HAS_HDBSCAN = False
    print("Install: pip install hdbscan")

if HAS_HDBSCAN:
    # Variable-density data: tight cluster + spread cluster
    rng = np.random.default_rng(42)
    X_tight = rng.normal([0, 0], 0.2, (100, 2))
    X_spread = rng.normal([5, 0], 1.5, (200, 2))
    X_noise = rng.uniform(-2, 8, (20, 2))
    X = np.vstack([X_tight, X_spread, X_noise])

    clusterer = hdbscan.HDBSCAN(min_cluster_size=15, min_samples=5,
                                  prediction_data=True)
    clusterer.fit(X)
    labels = clusterer.labels_
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = (labels == -1).sum()
    print(f"Found {n_clusters} clusters, {n_noise} noise points")
    print(f"Cluster sizes: {[(labels==i).sum() for i in range(n_clusters)]}")
    print(f"Cluster persistence (stability): {clusterer.cluster_persistence_}")
```

## Cluster Stability and Extraction

Each cluster C in the condensed hierarchy has a birth level λ_birth(C) = 1/ε_split (the density at which C split from its parent) and a death level λ_death(x) = 1/ε_fall for each member x (the density at which x falls out of the cluster). The stability of cluster C is Σ_{x∈C} (λ_death(x) − λ_birth(C)). The flat clustering that maximizes total stability is found by a bottom-up tree traversal: a cluster is selected if its own stability exceeds the sum of stabilities of its sub-clusters. This greedy algorithm runs in O(n) after the hierarchy is built.

```python
import numpy as np

if HAS_HDBSCAN:
    from hdbscan import HDBSCAN
    from hdbscan.prediction import approximate_predict
    from sklearn.datasets import make_blobs

    X_train, y_true = make_blobs(n_samples=400, centers=4,
                                   cluster_std=[0.3, 0.8, 0.5, 1.2], random_state=7)
    clusterer = HDBSCAN(min_cluster_size=20, min_samples=5, prediction_data=True)
    clusterer.fit(X_train)

    # Soft clustering — membership probabilities
    soft_labels, strengths = hdbscan.all_points_membership_vectors(clusterer)
    hard_labels = np.argmax(soft_labels, axis=1)

    print(f"Soft cluster membership shape: {soft_labels.shape}")
    print(f"Mean membership strength (confidence): {strengths.mean():.4f}")
    # Points with low max membership are uncertain / noise-like
    uncertain = (soft_labels.max(axis=1) < 0.5).sum()
    print(f"Points with ambiguous membership (<50% max prob): {uncertain}")
    for i in range(soft_labels.shape[1]):
        print(f"  Component {i}: {(hard_labels == i).sum()} hard-assigned, "
              f"mean prob={soft_labels[:, i].mean():.4f}")
```

## Outlier Scores for Anomaly Detection

HDBSCAN computes an outlier score for every point: the GLOSH (Global-Local Outlier Score from Hierarchies) score. A point's outlier score is 1 − max_membership_probability ∈ [0,1]. Points never belonging to any cluster have score 1; core members of dense clusters have scores near 0. This gives a continuous outlier ranking that can be thresholded to flag anomalies, making HDBSCAN a natural one-class anomaly detector — fit on normal data, then flag points with high outlier scores.

```python
import numpy as np

if HAS_HDBSCAN:
    from hdbscan import HDBSCAN
    from sklearn.preprocessing import StandardScaler

    rng = np.random.default_rng(0)
    X_normal = rng.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 400)
    X_anomaly = rng.uniform(-5, 5, (20, 2))
    X_all = np.vstack([X_normal, X_anomaly])
    y_true = np.array([0]*400 + [1]*20)

    X_all = StandardScaler().fit_transform(X_all)
    clusterer = HDBSCAN(min_cluster_size=20, min_samples=5, prediction_data=True)
    clusterer.fit(X_all)

    scores = clusterer.outlier_scores_
    threshold = np.percentile(scores, 95)
    flagged = (scores > threshold).astype(int)

    from sklearn.metrics import precision_score, recall_score, f1_score
    print(f"Outlier score threshold (95th pct): {threshold:.4f}")
    print(f"Precision: {precision_score(y_true, flagged):.4f}")
    print(f"Recall:    {recall_score(y_true, flagged):.4f}")
    print(f"F1:        {f1_score(y_true, flagged):.4f}")
    print(f"Mean score — normal: {scores[:400].mean():.4f}, anomaly: {scores[400:].mean():.4f}")
```

## HDBSCAN vs DBSCAN — When to Choose

DBSCAN is simpler and interpretable: if you know the density scale of your data and clusters have roughly uniform density, DBSCAN with the k-distance-elbow ε is often sufficient. HDBSCAN is strictly more powerful but slower to build and harder to interpret. Choose HDBSCAN when: clusters have variable density, you want soft membership probabilities, you need continuous outlier scores, or you want robustness to the ε parameter. HDBSCAN's primary parameter min_cluster_size is more intuitive than ε because it specifies minimum cluster size rather than a geometric distance.

```python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)
# Variable-density clusters: one tight, one spread
X_tight = rng.normal([0, 0], 0.3, (150, 2))
X_spread = rng.normal([4, 0], 1.8, (150, 2))
X = StandardScaler().fit_transform(np.vstack([X_tight, X_spread]))
y_true = np.array([0]*150 + [1]*150)

# DBSCAN needs different eps for different densities
for eps in [0.15, 0.3, 0.5, 0.8]:
    db = DBSCAN(eps=eps, min_samples=5).fit(X)
    n_cl = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
    ari = adjusted_rand_score(y_true, db.labels_) if n_cl > 0 else 0.0
    noise = (db.labels_ == -1).sum()
    print(f"DBSCAN eps={eps:.2f}: {n_cl} clusters, {noise} noise, ARI={ari:.4f}")

if HAS_HDBSCAN:
    hdb = hdbscan.HDBSCAN(min_cluster_size=20, min_samples=5).fit(X)
    n_cl = len(set(hdb.labels_)) - (1 if -1 in hdb.labels_ else 0)
    ari = adjusted_rand_score(y_true, hdb.labels_)
    print(f"\nHDBSCAN: {n_cl} clusters, {(hdb.labels_==-1).sum()} noise, ARI={ari:.4f}")
```

> **Parameter Tuning Guide**: Set min_cluster_size to the minimum number of points you would accept as a meaningful cluster (domain knowledge). Set min_samples (analogous to minPts) equal to min_cluster_size for simplicity, or lower to allow sparser clusters. Unlike DBSCAN's ε, these parameters have intuitive units. HDBSCAN is robust to min_cluster_size within an order of magnitude; large changes are needed to materially change the result.

## Practical Workflow and Installation

The hdbscan package (pip install hdbscan) provides the reference implementation with C extensions for speed. Sklearn 1.3+ also includes HDBSCAN via sklearn.cluster.HDBSCAN. The sklearn version integrates cleanly into sklearn pipelines but lacks the soft clustering and outlier score API. For production use: (1) fit HDBSCAN on training data; (2) use approximate_predict for new points (requires prediction_data=True); (3) flag points with outlier score above the 95th–99th percentile of training scores as anomalies.

- min_cluster_size: primary parameter — set to the minimum meaningful cluster size in your domain (e.g., 50 for customer segments, 5 for anomaly detection).
- min_samples: controls noise robustness — higher values produce more noise points but more confident clusters. Default: min_cluster_size.
- cluster_selection_method: 'eom' (excess of mass, default) maximizes stability; 'leaf' selects the finest-grained clusters from the hierarchy.
- alpha: controls how conservatively the mutual reachability graph is built (default 1.0). Rarely needs tuning.
- metric: supports any sklearn distance metric — 'euclidean' (default), 'manhattan', 'cosine' for text/high-d data.

| Feature | DBSCAN | HDBSCAN |
| --- | --- | --- |
| Key parameters | ε (radius), minPts | min_cluster_size, min_samples |
| Variable density clusters | No — single global threshold | Yes — multi-scale hierarchy |
| Soft membership | No — hard assignment | Yes — membership probabilities |
| Outlier scores | Binary (noise/not) | Continuous GLOSH score |
| Cluster stability | No | Yes — persistence-weighted extraction |
| Complexity | O(n log n) with index | O(n log n) with Borůvka |

---

