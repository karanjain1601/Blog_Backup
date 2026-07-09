---
title: "DBSCAN — Density-Based Spatial Clustering"
slug: "dbscan"
description: "Master DBSCAN's density-reachability framework: core, border, and noise points, the cluster expansion algorithm, O(n log n) complexity with spatial indexing, ε selection via the k-distance graph, and a head-to-head comparison with k-means on non-convex data."
tags: ["unsupervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiREJTQ0FOIChEZW5zaXR5LUJhc2VkIFNwYXRpYWwgQ2x1c3RlcmluZyBvZiBBcHBsaWNhdGlvbnMgd2l0aCBOb2lzZSkgZGlzY292ZXJzIGNsdXN0ZXJzIGFzIGRlbnNlIHJlZ2lvbnMgc2VwYXJhdGVkIGJ5IGxvdy1kZW5zaXR5IGFyZWFzLiBVbmxpa2Ugay1tZWFucyBvciBHTU1zLCBEQlNDQU4gcmVxdWlyZXMgbm8gYXNzdW1wdGlvbiBhYm91dCB0aGUgbnVtYmVyIG9mIGNsdXN0ZXJzLCBoYW5kbGVzIGFyYml0cmFyaWx5IHNoYXBlZCBjbHVzdGVycywgYW5kIG5hdHVyYWxseSBsYWJlbHMgb3V0bGllcnMgYXMgbm9pc2UuIEl0cyB0d28gcGFyYW1ldGVycyDigJQgzrUgKG5laWdoYm9yaG9vZCByYWRpdXMpIGFuZCBtaW5QdHMgKG1pbmltdW0gbmVpZ2hib3Job29kIHNpemUpIOKAlCBjb250cm9sIHRoZSBkZW5zaXR5IHRocmVzaG9sZCB0aGF0IGRlZmluZXMgYSBjbHVzdGVyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvcmUsIEJvcmRlciwgYW5kIE5vaXNlIFBvaW50cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiREJTQ0FOIGNsYXNzaWZpZXMgZXZlcnkgcG9pbnQgaW50byBvbmUgb2YgdGhyZWUgcm9sZXMgYmFzZWQgb24gaXRzIM61LW5laWdoYm9yaG9vZCBOzrUoeCkgPSB7eSA6IGRpc3QoeCx5KSDiiaQgzrV9OiBhIGNvcmUgcG9pbnQgaGFzIHxOzrUoeCl8IOKJpSBtaW5QdHMgKHN1ZmZpY2llbnQgbG9jYWwgZGVuc2l0eSB0byBmb3JtIGEgY2x1c3Rlcik7IGEgYm9yZGVyIHBvaW50IGhhcyB8Ts61KHgpfCBcdTAwM2MgbWluUHRzIGJ1dCBpcyB3aXRoaW4gzrUgb2YgYXQgbGVhc3Qgb25lIGNvcmUgcG9pbnQgKG9uIHRoZSBlZGdlIG9mIGEgY2x1c3Rlcik7IGEgbm9pc2UgcG9pbnQgKG91dGxpZXIpIGlzIG5laXRoZXIgYSBjb3JlIG5vciBhIGJvcmRlciBwb2ludC4gVGhlc2Ugcm9sZXMgY2FwdHVyZSB0aGUgaW50dWl0aW9uIHRoYXQgY2x1c3RlcnMgaGF2ZSBhIGRlbnNlIGludGVyaW9yLCBhIHRyYW5zaXRpb24gcmVnaW9uLCBhbmQgaXNvbGF0ZWQgb3V0bGllcnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJDb3JlIHBvaW50OiDiiaUgbWluUHRzIHBvaW50cyAoaW5jbHVkaW5nIGl0c2VsZikgd2l0aGluIGRpc3RhbmNlIM61LiBUaGVzZSBmb3JtIHRoZSBjbHVzdGVyIHNrZWxldG9uLiIsIkJvcmRlciBwb2ludDogZmV3ZXIgdGhhbiBtaW5QdHMgbmVpZ2hib3JzIHdpdGhpbiDOtSwgYnV0IHJlYWNoYWJsZSBmcm9tIGEgY29yZSBwb2ludC4gQmVsb25ncyB0byBhIGNsdXN0ZXIgYnV0IG5vdCBpdHMgaW50ZXJpb3IuIiwiTm9pc2UgcG9pbnQ6IGZld2VyIHRoYW4gbWluUHRzIG5laWdoYm9ycyB3aXRoaW4gzrUgYW5kIG5vdCByZWFjaGFibGUgZnJvbSBhbnkgY29yZSBwb2ludC4gTGFiZWxlZCDiiJIxIGluIHNrbGVhcm4uIiwiRGVuc2l0eS1yZWFjaGFiaWxpdHk6IHggaXMgZGVuc2l0eS1yZWFjaGFibGUgZnJvbSB5IGlmIHRoZXJlIGlzIGEgY2hhaW4gb2YgY29yZSBwb2ludHMgY29ubmVjdGluZyB0aGVtIHdpdGhpbiDOtS4iLCJEZW5zaXR5LWNvbm5lY3Rpdml0eTogeCBhbmQgeSBhcmUgZGVuc2l0eS1jb25uZWN0ZWQgaWYgdGhlcmUgZXhpc3RzIGEgcG9pbnQgeiBmcm9tIHdoaWNoIGJvdGggYXJlIGRlbnNpdHktcmVhY2hhYmxlLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgREJTQ0FOIEFsZ29yaXRobSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGFsZ29yaXRobSBpdGVyYXRlcyB0aHJvdWdoIGFsbCB1bnZpc2l0ZWQgcG9pbnRzOiBpZiBhIHBvaW50IGlzIGEgY29yZSBwb2ludCwgYSBuZXcgY2x1c3RlciBpcyBzdGFydGVkIGJ5IGV4cGFuZGluZyBmcm9tIGl0IOKAlCBhbGwgZGVuc2l0eS1yZWFjaGFibGUgcG9pbnRzIGFyZSByZWN1cnNpdmVseSBhZGRlZC4gQm9yZGVyIHBvaW50cyBhcmUgYWRkZWQgd2hlbiB0aGV5IGZhbGwgd2l0aGluIM61IG9mIGFuIGV4cGFuZGluZyBjb3JlIGNsdXN0ZXIuIFBvaW50cyB0aGF0IGFyZSBuZXZlciByZWFjaGVkIGFyZSBtYXJrZWQgYXMgbm9pc2UuIFdpdGggYSBzcGF0aWFsIGluZGV4IChlLmcuLCBhIEtELXRyZWUgb3IgYmFsbCB0cmVlKSwgbmVpZ2hib3Job29kIHF1ZXJpZXMgdGFrZSBPKGxvZyBuKSBvbiBhdmVyYWdlLCBnaXZpbmcgTyhuIGxvZyBuKSB0b3RhbCBjb21wbGV4aXR5LiBXaXRob3V0IGEgc3BhdGlhbCBpbmRleCB0aGUgbmFpdmUgaW1wbGVtZW50YXRpb24gaXMgTyhuwrIpLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IGRlcXVlXG5cbmRlZiBkYnNjYW5fbmFpdmUoWCwgZXBzLCBtaW5fcHRzKTpcbiAgICBcIlwiXCJEQlNDQU4gZnJvbSBzY3JhdGNoIOKAlCBPKG5eMiksIGZvciBwZWRhZ29naWNhbCBjbGFyaXR5LlwiXCJcIlxuICAgIG4gPSBYLnNoYXBlWzBdXG4gICAgbGFiZWxzID0gbnAuZnVsbChuLCAtMiwgZHR5cGU9aW50KSAgIyAtMiA9IHVudmlzaXRlZCwgLTEgPSBub2lzZVxuICAgIGNsdXN0ZXJfaWQgPSAwXG5cbiAgICBkZWYgbmVpZ2hib3JzKGlkeCk6XG4gICAgICAgIGRpc3RzID0gbnAuc3FydCgoKFggLSBYW2lkeF0pICoqIDIpLnN1bShheGlzPTEpKVxuICAgICAgICByZXR1cm4gbnAud2hlcmUoZGlzdHMgXHUwMDNjPSBlcHMpWzBdXG5cbiAgICBmb3IgaSBpbiByYW5nZShuKTpcbiAgICAgICAgaWYgbGFiZWxzW2ldICE9IC0yOlxuICAgICAgICAgICAgY29udGludWVcbiAgICAgICAgbmJycyA9IG5laWdoYm9ycyhpKVxuICAgICAgICBpZiBsZW4obmJycykgXHUwMDNjIG1pbl9wdHM6XG4gICAgICAgICAgICBsYWJlbHNbaV0gPSAtMSAgIyBub2lzZSAobWF5IGJlIHJlYXNzaWduZWQgYXMgYm9yZGVyIGxhdGVyKVxuICAgICAgICAgICAgY29udGludWVcbiAgICAgICAgbGFiZWxzW2ldID0gY2x1c3Rlcl9pZFxuICAgICAgICBxdWV1ZSA9IGRlcXVlKG5icnMpXG4gICAgICAgIHdoaWxlIHF1ZXVlOlxuICAgICAgICAgICAgaiA9IHF1ZXVlLnBvcGxlZnQoKVxuICAgICAgICAgICAgaWYgbGFiZWxzW2pdID09IC0xOlxuICAgICAgICAgICAgICAgIGxhYmVsc1tqXSA9IGNsdXN0ZXJfaWQgICMgYm9yZGVyIHBvaW50XG4gICAgICAgICAgICBpZiBsYWJlbHNbal0gIT0gLTI6XG4gICAgICAgICAgICAgICAgY29udGludWVcbiAgICAgICAgICAgIGxhYmVsc1tqXSA9IGNsdXN0ZXJfaWRcbiAgICAgICAgICAgIG5icnNfaiA9IG5laWdoYm9ycyhqKVxuICAgICAgICAgICAgaWYgbGVuKG5icnNfaikgXHUwMDNlPSBtaW5fcHRzOlxuICAgICAgICAgICAgICAgIHF1ZXVlLmV4dGVuZChuYnJzX2opICAjIGNvcmUgcG9pbnQ6IGV4cGFuZFxuICAgICAgICBjbHVzdGVyX2lkICs9IDFcbiAgICByZXR1cm4gbGFiZWxzXG5cbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9tb29uc1xuWCwgeV90cnVlID0gbWFrZV9tb29ucyhuX3NhbXBsZXM9MjAwLCBub2lzZT0wLjA4LCByYW5kb21fc3RhdGU9NDIpXG5sYWJlbHMgPSBkYnNjYW5fbmFpdmUoWCwgZXBzPTAuMiwgbWluX3B0cz01KVxubl9jbHVzdGVycyA9IGxlbihzZXQobGFiZWxzKSkgLSAoMSBpZiAtMSBpbiBsYWJlbHMgZWxzZSAwKVxucHJpbnQoZlwiRm91bmQge25fY2x1c3RlcnN9IGNsdXN0ZXJzLCB7KGxhYmVscyA9PSAtMSkuc3VtKCl9IG5vaXNlIHBvaW50c1wiKVxucHJpbnQoZlwiQVJJOiB7X19pbXBvcnRfXyhcdTAwMjdza2xlYXJuLm1ldHJpY3NcdTAwMjcsIGZyb21saXN0PVtcdTAwMjdhZGp1c3RlZF9yYW5kX3Njb3JlXHUwMDI3XSkuYWRqdXN0ZWRfcmFuZF9zY29yZSh5X3RydWUsIGxhYmVscyk6LjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNob29zaW5nIM61IOKAlCBUaGUgSy1EaXN0YW5jZSBHcmFwaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1vc3QgZWZmZWN0aXZlIGhldXJpc3RpYyBmb3IgY2hvb3NpbmcgzrUgaXMgdGhlIGstZGlzdGFuY2UgZ3JhcGg6IGZvciBlYWNoIHBvaW50LCBjb21wdXRlIGl0cyBkaXN0YW5jZSB0byBpdHMgay10aCBuZWFyZXN0IG5laWdoYm9yICh3aGVyZSBrID0gbWluUHRzKSBhbmQgc29ydCB0aGVzZSBkaXN0YW5jZXMgaW4gYXNjZW5kaW5nIG9yZGVyLiBQbG90IHRoZSBzb3J0ZWQgay1kaXN0YW5jZXM7IHRoZSBcdTAwMjdlbGJvd1x1MDAyNyAocG9pbnQgb2YgbWF4aW11bSBjdXJ2YXR1cmUpIHN1Z2dlc3RzIGEgZ29vZCDOtSDigJQgYmVsb3cgdGhpcyB2YWx1ZSBtb3N0IHBvaW50cyBoYXZlIGF0IGxlYXN0IG1pblB0cyBuZWlnaGJvcnMsIGZvcm1pbmcgZGVuc2UgY2x1c3RlcnM7IGFib3ZlIGl0LCBuZWlnaGJvcmhvb2RzIGNvbGxhcHNlLiBUaGUgcnVsZSBvZiB0aHVtYiBmb3IgbWluUHRzIGlzIDJkICh0d2ljZSB0aGUgZGltZW5zaW9uYWxpdHkpLCB3aXRoIGEgbWluaW11bSBvZiA0IGZvciAyRCBkYXRhLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5uZWlnaGJvcnMgaW1wb3J0IE5lYXJlc3ROZWlnaGJvcnNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9tb29ucywgbWFrZV9jaXJjbGVzXG5cblhfbW9vbiwgXyA9IG1ha2VfbW9vbnMobl9zYW1wbGVzPTMwMCwgbm9pc2U9MC4wNywgcmFuZG9tX3N0YXRlPTApXG5YX2NpcmNsZXMsIF8gPSBtYWtlX2NpcmNsZXMobl9zYW1wbGVzPTMwMCwgbm9pc2U9MC4wNSwgZmFjdG9yPTAuNSwgcmFuZG9tX3N0YXRlPTApXG5cbmZvciBuYW1lLCBYIGluIFsoXHUwMDI3TW9vbnNcdTAwMjcsIFhfbW9vbiksIChcdTAwMjdDaXJjbGVzXHUwMDI3LCBYX2NpcmNsZXMpXTpcbiAgICBtaW5fcHRzID0gNVxuICAgIG5icnMgPSBOZWFyZXN0TmVpZ2hib3JzKG5fbmVpZ2hib3JzPW1pbl9wdHMpLmZpdChYKVxuICAgIGRpc3RzLCBfID0gbmJycy5rbmVpZ2hib3JzKFgpXG4gICAga19kaXN0cyA9IG5wLnNvcnQoZGlzdHNbOiwgLTFdKVxuICAgICMgRmluZCBlbGJvdyB2aWEgbWF4aW11bSBzZWNvbmQgZGVyaXZhdGl2ZVxuICAgIGQyID0gbnAuZGlmZihucC5kaWZmKGtfZGlzdHMpKVxuICAgIGVsYm93X2lkeCA9IG5wLmFyZ21heChkMikgKyAxXG4gICAgc3VnZ2VzdGVkX2VwcyA9IGtfZGlzdHNbZWxib3dfaWR4XVxuICAgIHByaW50KGZcIntuYW1lfTogc3VnZ2VzdGVkIGVwcz17c3VnZ2VzdGVkX2VwczouNGZ9IChmcm9tIGs9e21pbl9wdHN9IGRpc3RhbmNlIGdyYXBoKVwiKVxuICAgIHByaW50KGZcIiAgay1kaXN0YW5jZXMgcmFuZ2U6IFt7a19kaXN0c1swXTouNGZ9LCB7a19kaXN0c1stMV06LjRmfV1cIilcbiAgICBwcmludChmXCIgIEVsYm93IGF0IGluZGV4IHtlbGJvd19pZHh9L3tsZW4oa19kaXN0cyl9XCIpXG4gICAgcHJpbnQoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRCU0NBTiBvbiBOb24tQ29udmV4IFNoYXBlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiREJTQ0FOIGV4Y2VscyBvbiB0aGUgY2Fub25pY2FsIG5vbi1jb252ZXggYmVuY2htYXJrcyB3aGVyZSBrLW1lYW5zIGNvbXBsZXRlbHkgZmFpbHMuIEZvciBpbnRlcmxlYXZlZCBoYWxmLW1vb25zIGFuZCBjb25jZW50cmljIHJpbmdzLCB0aGUgZGVuc2l0eS1iYXNlZCBkZWZpbml0aW9uIG9mIGNvbm5lY3Rpdml0eSBjb3JyZWN0bHkgdHJhY2VzIHRoZSBnZW9tZXRyaWMgc3RydWN0dXJlIHdpdGhvdXQgbmVlZGluZyB0byBrbm93IHRoZSBudW1iZXIgb2YgY2x1c3RlcnMgdXBmcm9udC4gVGhlIGtleSBpbnNpZ2h0IGlzIHRoYXQgZGVuc2l0eS1yZWFjaGFiaWxpdHkgaXMgdHJhbnNpdGl2ZSDigJQgYSBwb2ludCBkZWVwIGluc2lkZSBhIGNsdXN0ZXIgY2FuIHJlYWNoIGEgcG9pbnQgZmFyIGF3YXkgdmlhIGEgY2hhaW4gb2Ygb3ZlcmxhcHBpbmcgbmVpZ2hib3Job29kcywgc28gdGhlIGVudGlyZSBjb25uZWN0ZWQgZGVuc2UgcmVnaW9uIGZvcm1zIG9uZSBjbHVzdGVyIHJlZ2FyZGxlc3Mgb2YgaXRzIGdsb2JhbCBzaGFwZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uY2x1c3RlciBpbXBvcnQgREJTQ0FOLCBLTWVhbnNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9tb29ucywgbWFrZV9jaXJjbGVzXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWRqdXN0ZWRfcmFuZF9zY29yZVxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbmRhdGFzZXRzID0gW1xuICAgIChcdTAwMjdNb29uc1x1MDAyNywgICAqbWFrZV9tb29ucyhuX3NhbXBsZXM9MzAwLCBub2lzZT0wLjA3LCByYW5kb21fc3RhdGU9NDIpKSxcbiAgICAoXHUwMDI3Q2lyY2xlc1x1MDAyNywgKm1ha2VfY2lyY2xlcyhuX3NhbXBsZXM9MzAwLCBub2lzZT0wLjA1LCBmYWN0b3I9MC41LCByYW5kb21fc3RhdGU9NDIpKSxcbl1cblxuZm9yIG5hbWUsIFgsIHlfdHJ1ZSBpbiBkYXRhc2V0czpcbiAgICBYID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG4gICAgZGIgPSBEQlNDQU4oZXBzPTAuMywgbWluX3NhbXBsZXM9NSkuZml0KFgpXG4gICAga20gPSBLTWVhbnMobl9jbHVzdGVycz0yLCBuX2luaXQ9MTAsIHJhbmRvbV9zdGF0ZT00MikuZml0KFgpXG4gICAgYXJpX2RiID0gYWRqdXN0ZWRfcmFuZF9zY29yZSh5X3RydWUsIGRiLmxhYmVsc18pXG4gICAgYXJpX2ttID0gYWRqdXN0ZWRfcmFuZF9zY29yZSh5X3RydWUsIGttLmxhYmVsc18pXG4gICAgbl9jbHVzdGVyc19kYiA9IGxlbihzZXQoZGIubGFiZWxzXykpIC0gKDEgaWYgLTEgaW4gZGIubGFiZWxzXyBlbHNlIDApXG4gICAgbl9ub2lzZSA9IChkYi5sYWJlbHNfID09IC0xKS5zdW0oKVxuICAgIHByaW50KGZcIntuYW1lfTpcIilcbiAgICBwcmludChmXCIgIERCU0NBTiAg4oCUIGNsdXN0ZXJzPXtuX2NsdXN0ZXJzX2RifSwgbm9pc2U9e25fbm9pc2V9LCBBUkk9e2FyaV9kYjouNGZ9XCIpXG4gICAgcHJpbnQoZlwiICBLTWVhbnMgIOKAlCBjbHVzdGVycz0yLCAgbm9pc2U9MCwgICAgICBBUkk9e2FyaV9rbTouNGZ9XCIpXG4gICAgcHJpbnQoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRCU0NBTiB2cyBLLU1lYW5zIOKAlCBIZWFkLXRvLUhlYWQgb24gTm9uLUNvbnZleCBEYXRhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZGVmaW5pdGl2ZSBhZHZhbnRhZ2Ugb2YgREJTQ0FOIG92ZXIgay1tZWFucyBpcyBvbiBub24tY29udmV4IGRhdGEuIEstbWVhbnMgcGFydGl0aW9ucyBzcGFjZSB2aWEgc3RyYWlnaHQgVm9yb25vaSBib3VuZGFyaWVzLCB3aGljaCBjYW5ub3QgdHJhY2UgY3VydmVkIGNsdXN0ZXIgZ2VvbWV0cnkuIERCU0NBTiB1c2VzIGxvY2FsIGRlbnNpdHkgY29ubmVjdGl2aXR5IGFuZCBjYW4gZm9sbG93IGFyYml0cmFyaWx5IGN1cnZlZCBib3VuZGFyaWVzIGFzIGxvbmcgYXMgdGhlIGRlbnNpdHkgaXMgY29uc2lzdGVudGx5IGFib3ZlIHRoZSB0aHJlc2hvbGQuIFRoZSBjb21wYXJpc29uIGlzIG1vc3QgZHJhbWF0aWMgb24gaW50ZXJsZWF2ZWQgbW9vbnMgYW5kIGNvbmNlbnRyaWMgcmluZ3MsIHdoZXJlIGstbWVhbnMgQVJJIOKJiCAwIGFuZCBEQlNDQU4gQVJJIOKJiCAxLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5jbHVzdGVyIGltcG9ydCBEQlNDQU4sIEtNZWFuc1xuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX21vb25zLCBtYWtlX2NpcmNsZXNcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBhZGp1c3RlZF9yYW5kX3Njb3JlXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuZGF0YXNldHMgPSBbXG4gICAgKFx1MDAyN01vb25zXHUwMDI3LCAgIG1ha2VfbW9vbnMobl9zYW1wbGVzPTQwMCwgbm9pc2U9MC4wNiwgcmFuZG9tX3N0YXRlPTQyKSksXG4gICAgKFx1MDAyN0NpcmNsZXNcdTAwMjcsIG1ha2VfY2lyY2xlcyhuX3NhbXBsZXM9NDAwLCBub2lzZT0wLjA0LCBmYWN0b3I9MC41LCByYW5kb21fc3RhdGU9NDIpKSxcbl1cblxucHJpbnQoZlwie1x1MDAyN0RhdGFzZXRcdTAwMjc6MTBzfSB8IHtcdTAwMjdEQlNDQU4gZXBzXHUwMDI3Olx1MDAzZTEyfSB8IHtcdTAwMjdEQlNDQU4gQVJJXHUwMDI3Olx1MDAzZTEyfSB8IHtcdTAwMjdLTWVhbnMgQVJJXHUwMDI3Olx1MDAzZTEyfSB8IHtcdTAwMjdOb2lzZVx1MDAyNzpcdTAwM2U2fVwiKVxuZm9yIG5hbWUsIChYLCB5X3RydWUpIGluIGRhdGFzZXRzOlxuICAgIFggPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcbiAgICAjIFR1bmUgZXBzIGZyb20gay1kaXN0YW5jZSBlbGJvd1xuICAgIGZyb20gc2tsZWFybi5uZWlnaGJvcnMgaW1wb3J0IE5lYXJlc3ROZWlnaGJvcnNcbiAgICBubiA9IE5lYXJlc3ROZWlnaGJvcnMobl9uZWlnaGJvcnM9NSkuZml0KFgpXG4gICAgZGlzdHMsIF8gPSBubi5rbmVpZ2hib3JzKFgpXG4gICAga19kaXN0cyA9IG5wLnNvcnQoZGlzdHNbOiwgLTFdKVxuICAgIGQyID0gbnAuZGlmZihucC5kaWZmKGtfZGlzdHMpKVxuICAgIGVwcyA9IGtfZGlzdHNbbnAuYXJnbWF4KGQyKSArIDFdXG4gICAgZGIgPSBEQlNDQU4oZXBzPWVwcywgbWluX3NhbXBsZXM9NSkuZml0KFgpXG4gICAga20gPSBLTWVhbnMobl9jbHVzdGVycz0yLCBuX2luaXQ9MTAsIHJhbmRvbV9zdGF0ZT00MikuZml0KFgpXG4gICAgYXJpX2RiID0gYWRqdXN0ZWRfcmFuZF9zY29yZSh5X3RydWUsIGRiLmxhYmVsc18pXG4gICAgYXJpX2ttID0gYWRqdXN0ZWRfcmFuZF9zY29yZSh5X3RydWUsIGttLmxhYmVsc18pXG4gICAgbl9ub2lzZSA9IChkYi5sYWJlbHNfID09IC0xKS5zdW0oKVxuICAgIHByaW50KGZcIntuYW1lOjEwc30gfCB7ZXBzOlx1MDAzZTEyLjRmfSB8IHthcmlfZGI6XHUwMDNlMTIuNGZ9IHwge2FyaV9rbTpcdTAwM2UxMi40Zn0gfCB7bl9ub2lzZTpcdTAwM2U2fVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxpbWl0YXRpb25zIG9mIERCU0NBTiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiREJTQ0FOXHUwMDI3cyBtYWluIGxpbWl0YXRpb24gaXMgaXRzIHNpbmdsZSBnbG9iYWwgZGVuc2l0eSB0aHJlc2hvbGQuIENsdXN0ZXJzIHdpdGggZGlmZmVyZW50IGRlbnNpdGllcyByZXF1aXJlIGRpZmZlcmVudCDOtSB2YWx1ZXMsIGJ1dCBEQlNDQU4gdXNlcyBvbmUgzrUgZm9yIHRoZSBlbnRpcmUgZGF0YXNldC4gQSBkZW5zZSBjbHVzdGVyIGFuZCBhIHNwYXJzZSBjbHVzdGVyIGNhbm5vdCBib3RoIGJlIGNvcnJlY3RseSBpZGVudGlmaWVkIHVubGVzcyB0aGVpciBkZW5zaXR5IGRpZmZlcmVuY2UgaXMgc21hbGwuIEluIGhpZ2ggZGltZW5zaW9ucyAoZCBcdTAwM2UgMTApLCB0aGUgY3Vyc2Ugb2YgZGltZW5zaW9uYWxpdHkgY2F1c2VzIGFsbCBwYWlyd2lzZSBkaXN0YW5jZXMgdG8gY29uY2VudHJhdGUsIG1ha2luZyDOtSBzZWxlY3Rpb24gZXh0cmVtZWx5IHNlbnNpdGl2ZSDigJQgYSB0aW55IGNoYW5nZSBpbiDOtSBjaGFuZ2VzIHdoaWNoIHBvaW50cyBhcmUgY29yZXMsIG9mdGVuIGRyYXN0aWNhbGx5LiBIREJTQ0FOIGFkZHJlc3NlcyB0aGUgdmFyaWFibGUtZGVuc2l0eSBsaW1pdGF0aW9uIGJ5IGNvbnN0cnVjdGluZyBhIGhpZXJhcmNoeSBvZiBkZW5zaXR5IGxldmVscy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkRCU0NBTiBpbiBIaWdoIERpbWVuc2lvbnMiLCJjb250ZW50IjoiRm9yIGQgXHUwMDNlIDEwLCBEQlNDQU4gYmVjb21lcyB1bnJlbGlhYmxlIGJlY2F1c2UgRXVjbGlkZWFuIGRpc3RhbmNlIGxvc2VzIGRpc2NyaW1pbmF0aXZlIHBvd2VyIOKAlCB0aGUgcmF0aW8gb2YgbWF4L21pbiBwYWlyd2lzZSBkaXN0YW5jZSBhcHByb2FjaGVzIDEgYXMgZCBpbmNyZWFzZXMuIEJlZm9yZSBhcHBseWluZyBEQlNDQU4gdG8gaGlnaC1kaW1lbnNpb25hbCBkYXRhLCByZWR1Y2UgZGltZW5zaW9uYWxpdHkgd2l0aCBQQ0Egb3IgVU1BUCB0byAy4oCTMTAgZGltZW5zaW9ucywgdGhlbiB0dW5lIM61IG9uIHRoZSByZWR1Y2VkIHNwYWNlLiBUaGUgbWluUHRzIHJ1bGUgb2YgdGh1bWIgKDJkKSBhbHNvIHByb2R1Y2VzIHZlcnkgbGFyZ2UgdmFsdWVzIGluIGhpZ2ggZCwgY2F1c2luZyBldmVyeXRoaW5nIHRvIGJlIGxhYmVsZWQgbm9pc2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiSy1NZWFucyIsIkdNTSIsIkRCU0NBTiIsIkhEQlNDQU4iXSwicm93cyI6W1siQ2x1c3RlciBzaGFwZSIsIkNvbnZleCAoc3BoZXJpY2FsKSIsIkVsbGlwdGljYWwiLCJBcmJpdHJhcnkiLCJBcmJpdHJhcnkiXSxbIk91dGxpZXIgaGFuZGxpbmciLCJOb25lIOKAlCBhbGwgcG9pbnRzIGFzc2lnbmVkIiwiU29mdCAobG93IHJlc3BvbnNpYmlsaXR5KSIsIkV4cGxpY2l0IG5vaXNlIGxhYmVsIiwiT3V0bGllciBzY29yZXMiXSxbImsgcmVxdWlyZWQiLCJZZXMiLCJZZXMiLCJObyIsIk5vIl0sWyJWYXJpYWJsZSBkZW5zaXR5IiwiTm8iLCJQYXJ0aWFsbHkiLCJObyDigJQgc2luZ2xlIGdsb2JhbCDOtSIsIlllcyDigJQgbXVsdGktc2NhbGUiXSxbIkNvbXBsZXhpdHkiLCJPKG5rZFQpIiwiTyhua8KyZFQpIiwiTyhuIGxvZyBuKSB3aXRoIGluZGV4IiwiTyhuIGxvZyBuKSJdXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIHRvIGNob29zZSBEQlNDQU46IHRoZSBkYXRhIGhhcyBjbGVhciBzcGF0aWFsIGRlbnNpdHkgc3RydWN0dXJlLCBvdXRsaWVycyBuZWVkIGV4cGxpY2l0IGlkZW50aWZpY2F0aW9uLCBjbHVzdGVyIGNvdW50IGlzIHVua25vd24sIGFuZCBkYXRhIGRpbWVuc2lvbmFsaXR5IGlzIG1vZGVyYXRlIChkIOKJpCAyMCkuIFdoZW4gdG8gYXZvaWQgaXQ6IHZhcmlhYmxlIGNsdXN0ZXIgZGVuc2l0aWVzICh1c2UgSERCU0NBTiksIGhpZ2ggZGltZW5zaW9ucyAodXNlIFVNQVAgKyBEQlNDQU4pLCBvciB3aGVuIGFsbCBwb2ludHMgc2hvdWxkIGJlIGFzc2lnbmVkIHRvIGNsdXN0ZXJzICh1c2Ugay1tZWFucyBvciBHTU0pLiBEQlNDQU4gcmVtYWlucyBvbmUgb2YgdGhlIG1vc3QgY2l0ZWQgYWxnb3JpdGhtcyBpbiBjbHVzdGVyaW5nIGxpdGVyYXR1cmUgcHJlY2lzZWx5IGJlY2F1c2Ugb2YgaXRzIGNvbWJpbmF0aW9uIG9mIG91dGxpZXIgcm9idXN0bmVzcywgYXJiaXRyYXJ5IHNoYXBlIGRldGVjdGlvbiwgYW5kIGF1dG9tYXRpYyBjbHVzdGVyIGNvdW50IGRldGVybWluYXRpb24uIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# DBSCAN — Density-Based Spatial Clustering

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) discovers clusters as dense regions separated by low-density areas. Unlike k-means or GMMs, DBSCAN requires no assumption about the number of clusters, handles arbitrarily shaped clusters, and naturally labels outliers as noise. Its two parameters — ε (neighborhood radius) and minPts (minimum neighborhood size) — control the density threshold that defines a cluster.

## Core, Border, and Noise Points

DBSCAN classifies every point into one of three roles based on its ε-neighborhood Nε(x) = {y : dist(x,y) ≤ ε}: a core point has |Nε(x)| ≥ minPts (sufficient local density to form a cluster); a border point has |Nε(x)| < minPts but is within ε of at least one core point (on the edge of a cluster); a noise point (outlier) is neither a core nor a border point. These roles capture the intuition that clusters have a dense interior, a transition region, and isolated outliers.

- Core point: ≥ minPts points (including itself) within distance ε. These form the cluster skeleton.
- Border point: fewer than minPts neighbors within ε, but reachable from a core point. Belongs to a cluster but not its interior.
- Noise point: fewer than minPts neighbors within ε and not reachable from any core point. Labeled −1 in sklearn.
- Density-reachability: x is density-reachable from y if there is a chain of core points connecting them within ε.
- Density-connectivity: x and y are density-connected if there exists a point z from which both are density-reachable.

## The DBSCAN Algorithm

The algorithm iterates through all unvisited points: if a point is a core point, a new cluster is started by expanding from it — all density-reachable points are recursively added. Border points are added when they fall within ε of an expanding core cluster. Points that are never reached are marked as noise. With a spatial index (e.g., a KD-tree or ball tree), neighborhood queries take O(log n) on average, giving O(n log n) total complexity. Without a spatial index the naive implementation is O(n²).

```python
import numpy as np
from collections import deque

def dbscan_naive(X, eps, min_pts):
    """DBSCAN from scratch — O(n^2), for pedagogical clarity."""
    n = X.shape[0]
    labels = np.full(n, -2, dtype=int)  # -2 = unvisited, -1 = noise
    cluster_id = 0

    def neighbors(idx):
        dists = np.sqrt(((X - X[idx]) ** 2).sum(axis=1))
        return np.where(dists <= eps)[0]

    for i in range(n):
        if labels[i] != -2:
            continue
        nbrs = neighbors(i)
        if len(nbrs) < min_pts:
            labels[i] = -1  # noise (may be reassigned as border later)
            continue
        labels[i] = cluster_id
        queue = deque(nbrs)
        while queue:
            j = queue.popleft()
            if labels[j] == -1:
                labels[j] = cluster_id  # border point
            if labels[j] != -2:
                continue
            labels[j] = cluster_id
            nbrs_j = neighbors(j)
            if len(nbrs_j) >= min_pts:
                queue.extend(nbrs_j)  # core point: expand
        cluster_id += 1
    return labels

from sklearn.datasets import make_moons
X, y_true = make_moons(n_samples=200, noise=0.08, random_state=42)
labels = dbscan_naive(X, eps=0.2, min_pts=5)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Found {n_clusters} clusters, {(labels == -1).sum()} noise points")
print(f"ARI: {__import__('sklearn.metrics', fromlist=['adjusted_rand_score']).adjusted_rand_score(y_true, labels):.4f}")
```

## Choosing ε — The K-Distance Graph

The most effective heuristic for choosing ε is the k-distance graph: for each point, compute its distance to its k-th nearest neighbor (where k = minPts) and sort these distances in ascending order. Plot the sorted k-distances; the 'elbow' (point of maximum curvature) suggests a good ε — below this value most points have at least minPts neighbors, forming dense clusters; above it, neighborhoods collapse. The rule of thumb for minPts is 2d (twice the dimensionality), with a minimum of 4 for 2D data.

```python
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.datasets import make_moons, make_circles

X_moon, _ = make_moons(n_samples=300, noise=0.07, random_state=0)
X_circles, _ = make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=0)

for name, X in [('Moons', X_moon), ('Circles', X_circles)]:
    min_pts = 5
    nbrs = NearestNeighbors(n_neighbors=min_pts).fit(X)
    dists, _ = nbrs.kneighbors(X)
    k_dists = np.sort(dists[:, -1])
    # Find elbow via maximum second derivative
    d2 = np.diff(np.diff(k_dists))
    elbow_idx = np.argmax(d2) + 1
    suggested_eps = k_dists[elbow_idx]
    print(f"{name}: suggested eps={suggested_eps:.4f} (from k={min_pts} distance graph)")
    print(f"  k-distances range: [{k_dists[0]:.4f}, {k_dists[-1]:.4f}]")
    print(f"  Elbow at index {elbow_idx}/{len(k_dists)}")
    print()
```

## DBSCAN on Non-Convex Shapes

DBSCAN excels on the canonical non-convex benchmarks where k-means completely fails. For interleaved half-moons and concentric rings, the density-based definition of connectivity correctly traces the geometric structure without needing to know the number of clusters upfront. The key insight is that density-reachability is transitive — a point deep inside a cluster can reach a point far away via a chain of overlapping neighborhoods, so the entire connected dense region forms one cluster regardless of its global shape.

```python
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import make_moons, make_circles
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

datasets = [
    ('Moons',   *make_moons(n_samples=300, noise=0.07, random_state=42)),
    ('Circles', *make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=42)),
]

for name, X, y_true in datasets:
    X = StandardScaler().fit_transform(X)
    db = DBSCAN(eps=0.3, min_samples=5).fit(X)
    km = KMeans(n_clusters=2, n_init=10, random_state=42).fit(X)
    ari_db = adjusted_rand_score(y_true, db.labels_)
    ari_km = adjusted_rand_score(y_true, km.labels_)
    n_clusters_db = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
    n_noise = (db.labels_ == -1).sum()
    print(f"{name}:")
    print(f"  DBSCAN  — clusters={n_clusters_db}, noise={n_noise}, ARI={ari_db:.4f}")
    print(f"  KMeans  — clusters=2,  noise=0,      ARI={ari_km:.4f}")
    print()
```

## DBSCAN vs K-Means — Head-to-Head on Non-Convex Data

The definitive advantage of DBSCAN over k-means is on non-convex data. K-means partitions space via straight Voronoi boundaries, which cannot trace curved cluster geometry. DBSCAN uses local density connectivity and can follow arbitrarily curved boundaries as long as the density is consistently above the threshold. The comparison is most dramatic on interleaved moons and concentric rings, where k-means ARI ≈ 0 and DBSCAN ARI ≈ 1.

```python
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import make_moons, make_circles
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

datasets = [
    ('Moons',   make_moons(n_samples=400, noise=0.06, random_state=42)),
    ('Circles', make_circles(n_samples=400, noise=0.04, factor=0.5, random_state=42)),
]

print(f"{'Dataset':10s} | {'DBSCAN eps':>12} | {'DBSCAN ARI':>12} | {'KMeans ARI':>12} | {'Noise':>6}")
for name, (X, y_true) in datasets:
    X = StandardScaler().fit_transform(X)
    # Tune eps from k-distance elbow
    from sklearn.neighbors import NearestNeighbors
    nn = NearestNeighbors(n_neighbors=5).fit(X)
    dists, _ = nn.kneighbors(X)
    k_dists = np.sort(dists[:, -1])
    d2 = np.diff(np.diff(k_dists))
    eps = k_dists[np.argmax(d2) + 1]
    db = DBSCAN(eps=eps, min_samples=5).fit(X)
    km = KMeans(n_clusters=2, n_init=10, random_state=42).fit(X)
    ari_db = adjusted_rand_score(y_true, db.labels_)
    ari_km = adjusted_rand_score(y_true, km.labels_)
    n_noise = (db.labels_ == -1).sum()
    print(f"{name:10s} | {eps:>12.4f} | {ari_db:>12.4f} | {ari_km:>12.4f} | {n_noise:>6}")
```

## Limitations of DBSCAN

DBSCAN's main limitation is its single global density threshold. Clusters with different densities require different ε values, but DBSCAN uses one ε for the entire dataset. A dense cluster and a sparse cluster cannot both be correctly identified unless their density difference is small. In high dimensions (d > 10), the curse of dimensionality causes all pairwise distances to concentrate, making ε selection extremely sensitive — a tiny change in ε changes which points are cores, often drastically. HDBSCAN addresses the variable-density limitation by constructing a hierarchy of density levels.

> **DBSCAN in High Dimensions**: For d > 10, DBSCAN becomes unreliable because Euclidean distance loses discriminative power — the ratio of max/min pairwise distance approaches 1 as d increases. Before applying DBSCAN to high-dimensional data, reduce dimensionality with PCA or UMAP to 2–10 dimensions, then tune ε on the reduced space. The minPts rule of thumb (2d) also produces very large values in high d, causing everything to be labeled noise.

| Property | K-Means | GMM | DBSCAN | HDBSCAN |
| --- | --- | --- | --- | --- |
| Cluster shape | Convex (spherical) | Elliptical | Arbitrary | Arbitrary |
| Outlier handling | None — all points assigned | Soft (low responsibility) | Explicit noise label | Outlier scores |
| k required | Yes | Yes | No | No |
| Variable density | No | Partially | No — single global ε | Yes — multi-scale |
| Complexity | O(nkdT) | O(nk²dT) | O(n log n) with index | O(n log n) |

When to choose DBSCAN: the data has clear spatial density structure, outliers need explicit identification, cluster count is unknown, and data dimensionality is moderate (d ≤ 20). When to avoid it: variable cluster densities (use HDBSCAN), high dimensions (use UMAP + DBSCAN), or when all points should be assigned to clusters (use k-means or GMM). DBSCAN remains one of the most cited algorithms in clustering literature precisely because of its combination of outlier robustness, arbitrary shape detection, and automatic cluster count determination.

---

