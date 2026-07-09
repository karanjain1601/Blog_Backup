---
title: "Regularisation Paths — LARS and Coordinate Descent"
slug: "regularization-paths"
description: "Understand how the LASSO solution path is piecewise linear, compute full paths with LARS in O(min(n,p)³) operations, implement coordinate descent with soft-thresholding, and select λ via cross-validation with the one-standard-error rule."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSByZWd1bGFyaXNhdGlvbiBwYXRoIHRyYWNlcyBob3cgbW9kZWwgY29lZmZpY2llbnRzIM64KM67KSBjaGFuZ2UgYXMgdGhlIHJlZ3VsYXJpc2F0aW9uIHN0cmVuZ3RoIM67IHZhcmllcyBmcm9tIHZlcnkgbGFyZ2UgKGFsbCB6ZXJvcykgdG8gemVybyAoT0xTIG9yIE1MRSkuIENvbXB1dGluZyB0aGUgZnVsbCBwYXRoIGlzIG1vcmUgaW5mb3JtYXRpdmUgdGhhbiBmaXR0aW5nIGF0IGEgc2luZ2xlIM67OiBpdCByZXZlYWxzIHdoaWNoIGZlYXR1cmVzIGVudGVyIHRoZSBtb2RlbCBmaXJzdCAobW9zdCBpbXBvcnRhbnQpLCBob3cgY29ycmVsYXRlZCBmZWF0dXJlcyBjb21wZXRlLCBhbmQgcHJvdmlkZXMgdGhlIGZ1bGwgdHJhZGVvZmYgYmV0d2VlbiBzcGFyc2l0eSBhbmQgZml0IGZvciBjcm9zcy12YWxpZGF0aW9uLiBUaGUgTEFTU08gcGF0aCBoYXMgYSByZW1hcmthYmxlIHN0cnVjdHVyZTogaXQgaXMgcGllY2V3aXNlIGxpbmVhciwgd2l0aCBicmVha3BvaW50cyAoa25vdHMpIHdoZXJlIHZhcmlhYmxlcyBlbnRlciBvciBsZWF2ZSB0aGUgYWN0aXZlIHNldC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQaWVjZXdpc2UtTGluZWFyIFN0cnVjdHVyZSBvZiB0aGUgTEFTU08gUGF0aCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIExBU1NPIG9iamVjdGl2ZSBpcyBhIHF1YWRyYXRpYyAoaW4gzrgpIHBsdXMgYW4gTDEgcGVuYWx0eS4gQXMgzrsgZGVjcmVhc2VzIGZyb20g4oieLCBjb2VmZmljaWVudHMgc3RhcnQgYXQgemVybyBhbmQgaW5jcmVhc2UgcGllY2V3aXNlIGxpbmVhcmx5LiBBdCBlYWNoIGtub3QsIGVpdGhlciBhIG5ldyB2YXJpYWJsZSBqb2lucyB0aGUgYWN0aXZlIHNldCAoaXRzIGNvcnJlbGF0aW9ucyB3aXRoIHRoZSBjdXJyZW50IHJlc2lkdWFsIGVxdWFscyDOuykgb3IgYW4gYWN0aXZlIHZhcmlhYmxlIGNyb3NzZXMgemVybyBhbmQgaXMgZHJvcHBlZC4gVGhlIG51bWJlciBvZiBrbm90cyBpcyBhdCBtb3N0IG1pbihuLHApLCBzbyB0aGUgZnVsbCBwYXRoIGNhbiBiZSBjb21wdXRlZCBleGFjdGx5IGluIE8obWluKG4scCnCsykgb3BlcmF0aW9ucyB1c2luZyB0aGUgTEFSUyBhbGdvcml0aG0uIEJldHdlZW4ga25vdHMsIGNvZWZmaWNpZW50cyBmb2xsb3cgc3RyYWlnaHQtbGluZSB0cmFqZWN0b3JpZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgTGFzc29DViwgbGFzc29fcGF0aFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX3JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHkgPSBtYWtlX3JlZ3Jlc3Npb24obl9zYW1wbGVzPTEwMCwgbl9mZWF0dXJlcz0xNSwgbl9pbmZvcm1hdGl2ZT02LFxuICAgICAgICAgICAgICAgICAgICAgICAgbm9pc2U9OC4wLCByYW5kb21fc3RhdGU9NDIpXG5zY2FsZXIgPSBTdGFuZGFyZFNjYWxlcigpXG5YX3MgPSBzY2FsZXIuZml0X3RyYW5zZm9ybShYKVxuXG4jIEZ1bGwgTEFTU08gcGF0aFxuYWxwaGFzLCBjb2VmcywgXyA9IGxhc3NvX3BhdGgoWF9zLCB5LCBuX2FscGhhcz0xMDApXG5cbnByaW50KGZcdTAwMjdQYXRoIGNvbXB1dGVkIG92ZXIge2xlbihhbHBoYXMpfSBhbHBoYSB2YWx1ZXNcdTAwMjcpXG5wcmludChmXHUwMDI3QWxwaGEgcmFuZ2U6IFt7YWxwaGFzWy0xXTouNGZ9LCB7YWxwaGFzWzBdOi40Zn1dXHUwMDI3KVxucHJpbnQoZlx1MDAyN05vbnplcm8gY29lZnMgYXQgYWxwaGE9e2FscGhhc1swXTouM2Z9OiB7KGNvZWZzWzosIDBdICAhPSAwKS5zdW0oKX1cdTAwMjcpXG5wcmludChmXHUwMDI3Tm9uemVybyBjb2VmcyBhdCBhbHBoYT17YWxwaGFzWzUwXTouM2Z9OiB7KGNvZWZzWzosIDUwXSAhPSAwKS5zdW0oKX1cdTAwMjcpXG5wcmludChmXHUwMDI3Tm9uemVybyBjb2VmcyBhdCBhbHBoYT17YWxwaGFzWy0xXTouNGZ9OiB7KGNvZWZzWzosIC0xXSAhPSAwKS5zdW0oKX1cdTAwMjcpXG5cbiMgVmFyaWFibGUgZW50cnkgb3JkZXIgKGZpcnN0IGFscGhhIHdoZXJlIGVhY2ggY29lZiBiZWNvbWVzIG5vbnplcm8pXG5lbnRyeV9hbHBoYSA9IFtdXG5mb3IgaiBpbiByYW5nZShjb2Vmcy5zaGFwZVswXSk6XG4gICAgbnogPSBucC53aGVyZShjb2Vmc1tqXSAhPSAwKVswXVxuICAgIGVudHJ5X2FscGhhLmFwcGVuZChhbHBoYXNbbnpbMF1dIGlmIGxlbihueikgXHUwMDNlIDAgZWxzZSAwLjApXG5vcmRlciA9IG5wLmFyZ3NvcnQoZW50cnlfYWxwaGEpWzo6LTFdXG5wcmludChmXHUwMDI3XFxuVmFyaWFibGUgZW50cnkgb3JkZXIgKG1vc3QgdG8gbGVhc3QgaW1wb3J0YW50KToge29yZGVyWzo2XS50b2xpc3QoKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTEFSUyBBbGdvcml0aG0ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxlYXN0IEFuZ2xlIFJlZ3Jlc3Npb24gKExBUlMpIGNvbXB1dGVzIHRoZSBmdWxsIExBU1NPIHBhdGggZWZmaWNpZW50bHkuIFN0YXJ0aW5nIHdpdGggYWxsIGNvZWZmaWNpZW50cyBhdCB6ZXJvLCBMQVJTIGZpbmRzIHRoZSBwcmVkaWN0b3IgbW9zdCBjb3JyZWxhdGVkIHdpdGggdGhlIGN1cnJlbnQgcmVzaWR1YWwgYW5kIG1vdmVzIHRoZSBjb2VmZmljaWVudCBpbiB0aGF0IGRpcmVjdGlvbi4gSXQgbW92ZXMgdW50aWwgYW5vdGhlciBwcmVkaWN0b3IgYmVjb21lcyBlcXVhbGx5IGNvcnJlbGF0ZWQgd2l0aCB0aGUgcmVzaWR1YWwgKHRoZSBlcXVpYW5ndWxhciBkaXJlY3Rpb24pLiBBdCB0aGF0IHBvaW50LCBib3RoIHByZWRpY3RvcnMgam9pbiB0aGUgYWN0aXZlIHNldCBhbmQgdGhlIGFsZ29yaXRobSBwcm9jZWVkcyBpbiB0aGUgam9pbnQgZXF1aWFuZ3VsYXIgZGlyZWN0aW9uLiBBIG1vZGlmaWNhdGlvbiBoYW5kbGVzIExBU1NPOiB3aGVuIGEgY29lZmZpY2llbnQgY3Jvc3NlcyB6ZXJvLCBpdCBpcyBkcm9wcGVkIGZyb20gdGhlIGFjdGl2ZSBzZXQuIFRoaXMgZXhhY3RseSB0cmFjZXMgdGhlIHBpZWNld2lzZS1saW5lYXIgTEFTU08gcGF0aC4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkxBUlMgdnMgQ29vcmRpbmF0ZSBEZXNjZW50IGZvciBQYXRoIENvbXB1dGF0aW9uIiwiY29udGVudCI6IkxBUlMgY29tcHV0ZXMgdGhlIGV4YWN0IHBpZWNld2lzZS1saW5lYXIgcGF0aCBhdCBPKG1pbihuLHApwrMpIGNvc3Qg4oCUIGl0IGlzIHRoZSBnb2xkIHN0YW5kYXJkIHdoZW4geW91IHdhbnQgdGhlIGZ1bGwgcGF0aCBvciB0aGUgdmFyaWFibGUgZW50cnkgb3JkZXIuIENvb3JkaW5hdGUgZGVzY2VudCBpcyBmYXN0ZXIgcGVyLWl0ZXJhdGlvbiBmb3IgYSBzaW5nbGUgzrsgdmFsdWUgYW5kIHNjYWxlcyBiZXR0ZXIgdG8gdmVyeSBsYXJnZSBwIChzcGFyc2UgdXBkYXRlcykuIEZvciBwcm9kdWN0aW9uIHVzZSB3aXRoIHAgXHUwMDNlIDEwLDAwMCwgcHJlZmVyIGNvb3JkaW5hdGUgZGVzY2VudCB3aXRoIHdhcm0gc3RhcnRzIGFsb25nIGEgzrsgZ3JpZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBMYXJzLCBMYXNzb0xhcnNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9yZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5ID0gbWFrZV9yZWdyZXNzaW9uKG5fc2FtcGxlcz0xMDAsIG5fZmVhdHVyZXM9MTUsIG5faW5mb3JtYXRpdmU9NixcbiAgICAgICAgICAgICAgICAgICAgICAgIG5vaXNlPTguMCwgcmFuZG9tX3N0YXRlPTQyKVxuWF9zID0gU3RhbmRhcmRTY2FsZXIoKS5maXRfdHJhbnNmb3JtKFgpXG5cbiMgTGFzc29MYXJzIHRyYWNlcyB0aGUgZXhhY3QgTEFTU08gcGF0aFxubGFzc29fbGFycyA9IExhc3NvTGFycyhhbHBoYT0xZS00LCBub3JtYWxpemU9RmFsc2UsIGZpdF9pbnRlcmNlcHQ9VHJ1ZSlcbmxhc3NvX2xhcnMuZml0KFhfcywgeSlcblxucHJpbnQoZlx1MDAyN051bWJlciBvZiBwYXRoIGtub3RzOiB7bGVuKGxhc3NvX2xhcnMuYWxwaGFzXyl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0FscGhhIHZhbHVlcyAoZmlyc3QgNSk6IHtucC5yb3VuZChsYXNzb19sYXJzLmFscGhhc19bOjVdLCAzKX1cdTAwMjcpXG5wcmludChmXHUwMDI3Q29lZiBwYXRoIHNoYXBlOiB7bGFzc29fbGFycy5jb2VmX3BhdGhfLnNoYXBlfSAgKGZlYXR1cmVzIHgga25vdHMpXHUwMDI3KVxuXG4jIFRyYWNlIHZhcmlhYmxlIGVudHJ5IG9yZGVyXG5wcmV2X2FjdGl2ZSA9IHNldCgpXG5mb3Igc3RlcCBpbiByYW5nZShtaW4oMTAsIGxhc3NvX2xhcnMuY29lZl9wYXRoXy5zaGFwZVsxXSkpOlxuICAgIGFjdGl2ZSA9IHNldChucC53aGVyZShsYXNzb19sYXJzLmNvZWZfcGF0aF9bOiwgc3RlcF0gIT0gMClbMF0pXG4gICAgZW50ZXJlZCA9IGFjdGl2ZSAtIHByZXZfYWN0aXZlXG4gICAgaWYgZW50ZXJlZDpcbiAgICAgICAgcHJpbnQoZlx1MDAyNyAgS25vdCB7c3RlcH06IHZhcmlhYmxlKHMpIHtzb3J0ZWQoZW50ZXJlZCl9IGVudGVyZWQgYWN0aXZlIHNldFx1MDAyNylcbiAgICBwcmV2X2FjdGl2ZSA9IGFjdGl2ZSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvb3JkaW5hdGUgRGVzY2VudCBmb3IgTEFTU08ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvb3JkaW5hdGUgZGVzY2VudCB1cGRhdGVzIG9uZSBjb2VmZmljaWVudCBhdCBhIHRpbWUgd2hpbGUgaG9sZGluZyBvdGhlcnMgZml4ZWQuIEZvciBMQVNTTywgdGhlIG9wdGltYWwgdXBkYXRlIGZvciDOuOKxvCAod2l0aCBhbGwgb3RoZXJzIGZpeGVkKSBpcyB0aGUgc29mdC10aHJlc2hvbGRpbmcgb3BlcmF0b3I6IM644rG8IOKGkCBTKM+B4rG8LCDOuykgPSBzaWduKM+B4rG8KcK3bWF4KHzPgeKxvHwg4oiSIM67LCAwKSwgd2hlcmUgz4HisbwgPSBY4rG84bWAKHkg4oiSIFhfey1qfc64X3stan0pIGlzIHRoZSBwYXJ0aWFsIHJlc2lkdWFsIGNvcnJlbGF0aW9uLiBDeWNsaW5nIHRocm91Z2ggYWxsIGNvb3JkaW5hdGVzIHVudGlsIGNvbnZlcmdlbmNlIGNvc3RzIE8obnApIHBlciBjeWNsZS4gVXNpbmcgd2FybSBzdGFydHMgKGluaXRpYWxpc2luZyBmcm9tIHRoZSBwcmV2aW91cyDOuykgYWxvbmcgYSBkZWNyZWFzaW5nIM67IGdyaWQgbWFrZXMgY29vcmRpbmF0ZSBkZXNjZW50IGV4dHJlbWVseSBlZmZpY2llbnQgZm9yIGNvbXB1dGluZyBwYXRocy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBMYXNzb1xuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX3JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5kZWYgc29mdF90aHJlc2hvbGQocmhvLCBsYW0pOlxuICAgIHJldHVybiBucC5zaWduKHJobykgKiBucC5tYXhpbXVtKG5wLmFicyhyaG8pIC0gbGFtLCAwLjApXG5cbmRlZiBsYXNzb19jb29yZF9kZXNjZW50KFgsIHksIGxhbSwgbWF4X2l0ZXI9MjAwMCwgdG9sPTFlLTYpOlxuICAgIG4sIHAgPSBYLnNoYXBlXG4gICAgdGhldGEgPSBucC56ZXJvcyhwKVxuICAgIFh0eSA9IFguVCBAIHlcbiAgICBYdFhfZGlhZyA9IG5wLnN1bShYKioyLCBheGlzPTApICAjIHByZWNvbXB1dGUgY29sdW1uIG5vcm1zIHNxdWFyZWRcbiAgICBmb3IgaXRlcmF0aW9uIGluIHJhbmdlKG1heF9pdGVyKTpcbiAgICAgICAgdGhldGFfb2xkID0gdGhldGEuY29weSgpXG4gICAgICAgIGZvciBqIGluIHJhbmdlKHApOlxuICAgICAgICAgICAgcmVzaWRfaiA9IHkgLSBYIEAgdGhldGEgKyBYWzosIGpdICogdGhldGFbal1cbiAgICAgICAgICAgIHJob19qICAgPSBYWzosIGpdIEAgcmVzaWRfalxuICAgICAgICAgICAgdGhldGFbal0gPSBzb2Z0X3RocmVzaG9sZChyaG9faiAvIFh0WF9kaWFnW2pdLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGFtICAvIFh0WF9kaWFnW2pdKVxuICAgICAgICBpZiBucC5tYXgobnAuYWJzKHRoZXRhIC0gdGhldGFfb2xkKSkgXHUwMDNjIHRvbDpcbiAgICAgICAgICAgIHByaW50KGZcdTAwMjdDb252ZXJnZWQgYXQgaXRlcmF0aW9uIHtpdGVyYXRpb24rMX1cdTAwMjcpXG4gICAgICAgICAgICBicmVha1xuICAgIHJldHVybiB0aGV0YVxuXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHkgPSBtYWtlX3JlZ3Jlc3Npb24obl9zYW1wbGVzPTEwMCwgbl9mZWF0dXJlcz0xNSwgbl9pbmZvcm1hdGl2ZT02LFxuICAgICAgICAgICAgICAgICAgICAgICAgbm9pc2U9OC4wLCByYW5kb21fc3RhdGU9NDIpXG5YX3MgPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxubGFtID0gNS4wXG50aGV0YV9jZCA9IGxhc3NvX2Nvb3JkX2Rlc2NlbnQoWF9zLCB5LCBsYW0pXG50aGV0YV9zayA9IExhc3NvKGFscGhhPWxhbSwgZml0X2ludGVyY2VwdD1GYWxzZSwgbWF4X2l0ZXI9MTAwMDApLmZpdChYX3MsIHkpLmNvZWZfXG5wcmludChmXHUwMDI3TWF4IGRpZmYgdnMgc2tsZWFybiBMYXNzbzoge25wLmFicyh0aGV0YV9jZCAtIHRoZXRhX3NrKS5tYXgoKTouMmV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN05vbnplcm8gY29lZnMgKHNjcmF0Y2gpOiB7KG5wLmFicyh0aGV0YV9jZCkgXHUwMDNlIDFlLTYpLnN1bSgpfVx1MDAyNylcbnByaW50KGZcdTAwMjdOb256ZXJvIGNvZWZzIChza2xlYXJuKTogeyhucC5hYnModGhldGFfc2spIFx1MDAzZSAxZS02KS5zdW0oKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtVmFsaWRhdGlvbiBhbmQgdGhlIE9uZS1TdGFuZGFyZC1FcnJvciBSdWxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDcm9zcy12YWxpZGF0aW9uIHNlbGVjdHMgzrsgYnkgZXN0aW1hdGluZyB0ZXN0IGVycm9yLiBMYXNzb0NWIGluIHNrbGVhcm4gdXNlcyBlZmZpY2llbnQgd2FybS1zdGFydGVkIGNvb3JkaW5hdGUgZGVzY2VudCBhbG9uZyBhIHBhdGg6IGZpdCBhdCB0aGUgbGFyZ2VzdCDOuywgdGhlbiBkZWNyZWFzZSDOuyBhbmQgaW5pdGlhbGlzZSBmcm9tIHRoZSBwcmV2aW91cyBzb2x1dGlvbi4gVGhlIG9uZS1zdGFuZGFyZC1lcnJvciBydWxlIChIYXN0aWUsIFRpYnNoaXJhbmksIEZyaWVkbWFuKTogaW5zdGVhZCBvZiBwaWNraW5nIHRoZSDOuyB3aXRoIG1pbmltdW0gQ1YgZXJyb3IsIGNob29zZSB0aGUgbGFyZ2VzdCDOuyB3aG9zZSBDViBlcnJvciBpcyB3aXRoaW4gb25lIHN0YW5kYXJkIGVycm9yIG9mIHRoZSBtaW5pbXVtLiBUaGlzIGZhdm91cnMgc3BhcnNlciwgbW9yZSBpbnRlcnByZXRhYmxlIG1vZGVscyB0aGF0IHBlcmZvcm0gbmVhcmx5IGFzIHdlbGwgYXMgdGhlIG1pbmltdW0tQ1YgbW9kZWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgTGFzc29cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IEtGb2xkXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfcmVncmVzc2lvblxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCwgeSA9IG1ha2VfcmVncmVzc2lvbihuX3NhbXBsZXM9MTUwLCBuX2ZlYXR1cmVzPTIwLCBuX2luZm9ybWF0aXZlPTYsXG4gICAgICAgICAgICAgICAgICAgICAgICBub2lzZT0xMC4wLCByYW5kb21fc3RhdGU9NDIpXG5YX3MgPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxuYWxwaGFzID0gbnAubG9nc3BhY2UoLTIsIDIsIDYwKVxua2YgPSBLRm9sZChuX3NwbGl0cz01LCBzaHVmZmxlPVRydWUsIHJhbmRvbV9zdGF0ZT0wKVxuY3ZfbXNlcyA9IG5wLnplcm9zKChsZW4oYWxwaGFzKSwga2Yubl9zcGxpdHMpKVxuXG5mb3IgZm9sZCwgKHRyLCB2YSkgaW4gZW51bWVyYXRlKGtmLnNwbGl0KFhfcykpOlxuICAgIGZvciBpLCBhbHBoYSBpbiBlbnVtZXJhdGUoYWxwaGFzKTpcbiAgICAgICAgbSA9IExhc3NvKGFscGhhPWFscGhhLCBtYXhfaXRlcj0xMDAwMCkuZml0KFhfc1t0cl0sIHlbdHJdKVxuICAgICAgICByZXNpZCA9IHlbdmFdIC0gbS5wcmVkaWN0KFhfc1t2YV0pXG4gICAgICAgIGN2X21zZXNbaSwgZm9sZF0gPSBucC5tZWFuKHJlc2lkKioyKVxuXG5tZWFuX2N2ID0gY3ZfbXNlcy5tZWFuKGF4aXM9MSlcbnNlX2N2ICAgPSBjdl9tc2VzLnN0ZChheGlzPTEpIC8gbnAuc3FydChrZi5uX3NwbGl0cylcblxuYmVzdF9pZHggPSBucC5hcmdtaW4obWVhbl9jdilcbm9uZV9zZV90aHJlc2hvbGQgPSBtZWFuX2N2W2Jlc3RfaWR4XSArIHNlX2N2W2Jlc3RfaWR4XVxub25lX3NlX2lkeCA9IG5wLndoZXJlKChtZWFuX2N2IFx1MDAzYz0gb25lX3NlX3RocmVzaG9sZCkgXHUwMDI2IChhbHBoYXMgXHUwMDNlPSBhbHBoYXNbYmVzdF9pZHhdKSlbMF1cbm9uZV9zZV9pZHggPSBvbmVfc2VfaWR4WzBdIGlmIGxlbihvbmVfc2VfaWR4KSBcdTAwM2UgMCBlbHNlIGJlc3RfaWR4XG5cbnByaW50KGZcdTAwMjdMYW1iZGEgYXQgbWluIENWIE1TRTogICAgICB7YWxwaGFzW2Jlc3RfaWR4XTouNGZ9ICAoTVNFPXttZWFuX2N2W2Jlc3RfaWR4XTouMmZ9KVx1MDAyNylcbnByaW50KGZcdTAwMjdMYW1iZGEgYnkgMS1TRSBydWxlOiAgICAgICB7YWxwaGFzW29uZV9zZV9pZHhdOi40Zn0gIChNU0U9e21lYW5fY3Zbb25lX3NlX2lkeF06LjJmfSlcdTAwMjcpXG5wcmludChmXHUwMDI3Tm9uemVybyBhdCBtaW4tQ1YgbGFtYmRhOiAgeyhMYXNzbyhhbHBoYT1hbHBoYXNbYmVzdF9pZHhdKS5maXQoWF9zLCB5KS5jb2VmXyAhPSAwKS5zdW0oKX1cdTAwMjcpXG5wcmludChmXHUwMDI3Tm9uemVybyBhdCAxLVNFIGxhbWJkYTogICAgeyhMYXNzbyhhbHBoYT1hbHBoYXNbb25lX3NlX2lkeF0pLmZpdChYX3MsIHkpLmNvZWZfICE9IDApLnN1bSgpfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZXRob2QgQ29tcGFyaXNvbiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJQZXItU3RlcCBDb3N0IiwiRXhhY3QgUGF0aCIsIkxhcmdlIHAiLCJPbmxpbmUvU3RyZWFtaW5nIl0sInJvd3MiOltbIkxBUlMiLCJPKHDCsikgcGVyIGtub3QsIE8obWluKG4scCnCsykgdG90YWwiLCJZZXMg4oCUIHBpZWNld2lzZSBsaW5lYXIiLCJQb29yIGZvciBwIFx1MDAzZSAxMGsiLCJObyJdLFsiQ29vcmRpbmF0ZSBkZXNjZW50IiwiTyhucCkgcGVyIGN5Y2xlIiwiTm8g4oCUIGdyaWQgYXBwcm94aW1hdGlvbiIsIkV4Y2VsbGVudCAoc3BhcnNlIHVwZGF0ZXMpIiwiUG9zc2libGUgd2l0aCBTR0QgdmFyaWFudCJdLFsiU3ViZ3JhZGllbnQgZGVzY2VudCIsIk8obnApIHBlciBzdGVwIiwiTm8iLCJHb29kIiwiWWVzIl0sWyJQcm94aW1hbCBncmFkaWVudCAoSVNUQS9GSVNUQSkiLCJPKG5wKSBwZXIgc3RlcCwgZmFzdGVyIGNvbnZlcmdlbmNlIiwiTm8iLCJHb29kIiwiUG9zc2libGUiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ildhcm0gU3RhcnRpbmcgQWxvbmcgdGhlIFBhdGgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbXB1dGluZyB0aGUgc29sdXRpb24gYXQgYSBzZXF1ZW5jZSBvZiDOuyB2YWx1ZXMgKGZyb20gbGFyZ2UgdG8gc21hbGwpIHdpdGggd2FybSBzdGFydHMg4oCUIGluaXRpYWxpc2luZyBlYWNoIHNvbHZlIGZyb20gdGhlIHByZXZpb3VzIHNvbHV0aW9uIOKAlCBkcmFtYXRpY2FsbHkgcmVkdWNlcyB0b3RhbCBjb21wdXRhdGlvbi4gQXQgbGFyZ2UgzrssIG1vc3QgY29lZmZpY2llbnRzIGFyZSB6ZXJvOyBhcyDOuyBkZWNyZWFzZXMsIG9ubHkgYSBmZXcgbmV3IHZhcmlhYmxlcyBlbnRlci4gRWFjaCB3YXJtLXN0YXJ0ZWQgc29sdmUgY29udmVyZ2VzIGluIHZlcnkgZmV3IGl0ZXJhdGlvbnMuIFRoaXMgaXMgaG93IExhc3NvQ1YgYW5kIEVsYXN0aWNOZXRDViBhY2hpZXZlIGZhc3QgY3Jvc3MtdmFsaWRhdGVkIHBhdGggY29tcHV0YXRpb24uIFRoZSBzYXZlZCBzb2x1dGlvbnMgYXQgZWFjaCDOuyBhbHNvIGZvcm0gdGhlIHJlZ3VsYXJpc2F0aW9uIHBhdGggcGxvdCBzaG93aW5nIHZhcmlhYmxlIHNlbGVjdGlvbiBvcmRlci4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkFsd2F5cyBmaXQgdGhlIHBhdGggZnJvbSBsYXJnZSB0byBzbWFsbCDOuyB3aXRoIHdhcm0gc3RhcnRzIOKAlCBjb2xkIHN0YXJ0cyBhcmUgfjEweCBzbG93ZXIuIiwiVXNlIExhc3NvQ1Ygb3IgRWxhc3RpY05ldENWIGluc3RlYWQgb2YgZ3JpZC1zZWFyY2hpbmcgbWFudWFsbHk7IHRoZXkgaW1wbGVtZW50IHdhcm0tc3RhcnRlZCBwYXRocyBpbnRlcm5hbGx5LiIsIlRoZSAxLVNFIHJ1bGUgb2Z0ZW4gc2VsZWN0cyAzMOKAkzYwJSBmZXdlciBmZWF0dXJlcyB0aGFuIHRoZSBtaW4tQ1Ygzrsgd2l0aCBjb21wYXJhYmxlIHRlc3QgcGVyZm9ybWFuY2UuIiwiRm9yIGdlbm9taWNzIChwPTIwayspLCB1c2UgY29vcmRpbmF0ZSBkZXNjZW50IHdpdGggc3BhcnNlIG1hdHJpeCByZXByZXNlbnRhdGlvbiBmb3IgbWVtb3J5IGVmZmljaWVuY3kuIiwiUGxvdCB0aGUgY29lZmZpY2llbnQgcGF0aCB0byBpbnNwZWN0IHZhcmlhYmxlIGVudHJ5IG9yZGVyIOKAlCBhIG5hdHVyYWwgZmVhdHVyZSBpbXBvcnRhbmNlIHJhbmtpbmcuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBXb3JrZmxvdyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSByb2J1c3QgTEFTU08gd29ya2Zsb3c6ICgxKSBzdGFuZGFyZGlzZSBhbGwgZmVhdHVyZXM7ICgyKSBydW4gTGFzc29DViB3aXRoIDUgb3IgMTAgZm9sZHMgb24gYSBsb2ctc3BhY2VkIM67IGdyaWQgY292ZXJpbmcgdGhlIGZ1bGwgcGF0aDsgKDMpIGFwcGx5IHRoZSAxLVNFIHJ1bGUgdG8gZ2V0IGEgc3BhcnNlciBtb2RlbDsgKDQpIGV4YW1pbmUgdGhlIGNvZWZmaWNpZW50IHBhdGggcGxvdCBmb3Igc3RhYmlsaXR5IOKAlCB2YXJpYWJsZXMgdGhhdCBlbnRlciBhbmQgZXhpdCB0aGUgYWN0aXZlIHNldCBhcmUgdW5zdGFibGUgdW5kZXIgc21hbGwgZGF0YSBwZXJ0dXJiYXRpb25zOyAoNSkgcmVmaXQgYSBmaW5hbCBtb2RlbCBhdCB0aGUgY2hvc2VuIM67IG9uIHRoZSBmdWxsIHRyYWluaW5nIHNldDsgKDYpIHJlcG9ydCBmZWF0dXJlcyBzZWxlY3RlZCwgdGhlaXIgY29lZmZpY2llbnRzLCBhbmQgY29uZmlkZW5jZSBpbnRlcnZhbHMgdmlhIGJvb3RzdHJhcCBvciBjcm9zcy12YWxpZGF0ZWQgcmVmaXR0aW5nLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Regularisation Paths — LARS and Coordinate Descent

A regularisation path traces how model coefficients θ(λ) change as the regularisation strength λ varies from very large (all zeros) to zero (OLS or MLE). Computing the full path is more informative than fitting at a single λ: it reveals which features enter the model first (most important), how correlated features compete, and provides the full tradeoff between sparsity and fit for cross-validation. The LASSO path has a remarkable structure: it is piecewise linear, with breakpoints (knots) where variables enter or leave the active set.

## Piecewise-Linear Structure of the LASSO Path

The LASSO objective is a quadratic (in θ) plus an L1 penalty. As λ decreases from ∞, coefficients start at zero and increase piecewise linearly. At each knot, either a new variable joins the active set (its correlations with the current residual equals λ) or an active variable crosses zero and is dropped. The number of knots is at most min(n,p), so the full path can be computed exactly in O(min(n,p)³) operations using the LARS algorithm. Between knots, coefficients follow straight-line trajectories.

```python
import numpy as np
from sklearn.linear_model import LassoCV, lasso_path
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X, y = make_regression(n_samples=100, n_features=15, n_informative=6,
                        noise=8.0, random_state=42)
scaler = StandardScaler()
X_s = scaler.fit_transform(X)

# Full LASSO path
alphas, coefs, _ = lasso_path(X_s, y, n_alphas=100)

print(f'Path computed over {len(alphas)} alpha values')
print(f'Alpha range: [{alphas[-1]:.4f}, {alphas[0]:.4f}]')
print(f'Nonzero coefs at alpha={alphas[0]:.3f}: {(coefs[:, 0]  != 0).sum()}')
print(f'Nonzero coefs at alpha={alphas[50]:.3f}: {(coefs[:, 50] != 0).sum()}')
print(f'Nonzero coefs at alpha={alphas[-1]:.4f}: {(coefs[:, -1] != 0).sum()}')

# Variable entry order (first alpha where each coef becomes nonzero)
entry_alpha = []
for j in range(coefs.shape[0]):
    nz = np.where(coefs[j] != 0)[0]
    entry_alpha.append(alphas[nz[0]] if len(nz) > 0 else 0.0)
order = np.argsort(entry_alpha)[::-1]
print(f'\nVariable entry order (most to least important): {order[:6].tolist()}')
```

## LARS Algorithm

Least Angle Regression (LARS) computes the full LASSO path efficiently. Starting with all coefficients at zero, LARS finds the predictor most correlated with the current residual and moves the coefficient in that direction. It moves until another predictor becomes equally correlated with the residual (the equiangular direction). At that point, both predictors join the active set and the algorithm proceeds in the joint equiangular direction. A modification handles LASSO: when a coefficient crosses zero, it is dropped from the active set. This exactly traces the piecewise-linear LASSO path.

> **LARS vs Coordinate Descent for Path Computation**: LARS computes the exact piecewise-linear path at O(min(n,p)³) cost — it is the gold standard when you want the full path or the variable entry order. Coordinate descent is faster per-iteration for a single λ value and scales better to very large p (sparse updates). For production use with p > 10,000, prefer coordinate descent with warm starts along a λ grid.

```python
import numpy as np
from sklearn.linear_model import Lars, LassoLars
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X, y = make_regression(n_samples=100, n_features=15, n_informative=6,
                        noise=8.0, random_state=42)
X_s = StandardScaler().fit_transform(X)

# LassoLars traces the exact LASSO path
lasso_lars = LassoLars(alpha=1e-4, normalize=False, fit_intercept=True)
lasso_lars.fit(X_s, y)

print(f'Number of path knots: {len(lasso_lars.alphas_)}')
print(f'Alpha values (first 5): {np.round(lasso_lars.alphas_[:5], 3)}')
print(f'Coef path shape: {lasso_lars.coef_path_.shape}  (features x knots)')

# Trace variable entry order
prev_active = set()
for step in range(min(10, lasso_lars.coef_path_.shape[1])):
    active = set(np.where(lasso_lars.coef_path_[:, step] != 0)[0])
    entered = active - prev_active
    if entered:
        print(f'  Knot {step}: variable(s) {sorted(entered)} entered active set')
    prev_active = active
```

## Coordinate Descent for LASSO

Coordinate descent updates one coefficient at a time while holding others fixed. For LASSO, the optimal update for θⱼ (with all others fixed) is the soft-thresholding operator: θⱼ ← S(ρⱼ, λ) = sign(ρⱼ)·max(|ρⱼ| − λ, 0), where ρⱼ = Xⱼᵀ(y − X_{-j}θ_{-j}) is the partial residual correlation. Cycling through all coordinates until convergence costs O(np) per cycle. Using warm starts (initialising from the previous λ) along a decreasing λ grid makes coordinate descent extremely efficient for computing paths.

```python
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

def soft_threshold(rho, lam):
    return np.sign(rho) * np.maximum(np.abs(rho) - lam, 0.0)

def lasso_coord_descent(X, y, lam, max_iter=2000, tol=1e-6):
    n, p = X.shape
    theta = np.zeros(p)
    Xty = X.T @ y
    XtX_diag = np.sum(X**2, axis=0)  # precompute column norms squared
    for iteration in range(max_iter):
        theta_old = theta.copy()
        for j in range(p):
            resid_j = y - X @ theta + X[:, j] * theta[j]
            rho_j   = X[:, j] @ resid_j
            theta[j] = soft_threshold(rho_j / XtX_diag[j],
                                       lam  / XtX_diag[j])
        if np.max(np.abs(theta - theta_old)) < tol:
            print(f'Converged at iteration {iteration+1}')
            break
    return theta

np.random.seed(42)
X, y = make_regression(n_samples=100, n_features=15, n_informative=6,
                        noise=8.0, random_state=42)
X_s = StandardScaler().fit_transform(X)

lam = 5.0
theta_cd = lasso_coord_descent(X_s, y, lam)
theta_sk = Lasso(alpha=lam, fit_intercept=False, max_iter=10000).fit(X_s, y).coef_
print(f'Max diff vs sklearn Lasso: {np.abs(theta_cd - theta_sk).max():.2e}')
print(f'Nonzero coefs (scratch): {(np.abs(theta_cd) > 1e-6).sum()}')
print(f'Nonzero coefs (sklearn): {(np.abs(theta_sk) > 1e-6).sum()}')
```

## Cross-Validation and the One-Standard-Error Rule

Cross-validation selects λ by estimating test error. LassoCV in sklearn uses efficient warm-started coordinate descent along a path: fit at the largest λ, then decrease λ and initialise from the previous solution. The one-standard-error rule (Hastie, Tibshirani, Friedman): instead of picking the λ with minimum CV error, choose the largest λ whose CV error is within one standard error of the minimum. This favours sparser, more interpretable models that perform nearly as well as the minimum-CV model.

```python
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import KFold
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X, y = make_regression(n_samples=150, n_features=20, n_informative=6,
                        noise=10.0, random_state=42)
X_s = StandardScaler().fit_transform(X)

alphas = np.logspace(-2, 2, 60)
kf = KFold(n_splits=5, shuffle=True, random_state=0)
cv_mses = np.zeros((len(alphas), kf.n_splits))

for fold, (tr, va) in enumerate(kf.split(X_s)):
    for i, alpha in enumerate(alphas):
        m = Lasso(alpha=alpha, max_iter=10000).fit(X_s[tr], y[tr])
        resid = y[va] - m.predict(X_s[va])
        cv_mses[i, fold] = np.mean(resid**2)

mean_cv = cv_mses.mean(axis=1)
se_cv   = cv_mses.std(axis=1) / np.sqrt(kf.n_splits)

best_idx = np.argmin(mean_cv)
one_se_threshold = mean_cv[best_idx] + se_cv[best_idx]
one_se_idx = np.where((mean_cv <= one_se_threshold) & (alphas >= alphas[best_idx]))[0]
one_se_idx = one_se_idx[0] if len(one_se_idx) > 0 else best_idx

print(f'Lambda at min CV MSE:      {alphas[best_idx]:.4f}  (MSE={mean_cv[best_idx]:.2f})')
print(f'Lambda by 1-SE rule:       {alphas[one_se_idx]:.4f}  (MSE={mean_cv[one_se_idx]:.2f})')
print(f'Nonzero at min-CV lambda:  {(Lasso(alpha=alphas[best_idx]).fit(X_s, y).coef_ != 0).sum()}')
print(f'Nonzero at 1-SE lambda:    {(Lasso(alpha=alphas[one_se_idx]).fit(X_s, y).coef_ != 0).sum()}')
```

## Method Comparison

| Method | Per-Step Cost | Exact Path | Large p | Online/Streaming |
| --- | --- | --- | --- | --- |
| LARS | O(p²) per knot, O(min(n,p)³) total | Yes — piecewise linear | Poor for p > 10k | No |
| Coordinate descent | O(np) per cycle | No — grid approximation | Excellent (sparse updates) | Possible with SGD variant |
| Subgradient descent | O(np) per step | No | Good | Yes |
| Proximal gradient (ISTA/FISTA) | O(np) per step, faster convergence | No | Good | Possible |

## Warm Starting Along the Path

Computing the solution at a sequence of λ values (from large to small) with warm starts — initialising each solve from the previous solution — dramatically reduces total computation. At large λ, most coefficients are zero; as λ decreases, only a few new variables enter. Each warm-started solve converges in very few iterations. This is how LassoCV and ElasticNetCV achieve fast cross-validated path computation. The saved solutions at each λ also form the regularisation path plot showing variable selection order.

- Always fit the path from large to small λ with warm starts — cold starts are ~10x slower.
- Use LassoCV or ElasticNetCV instead of grid-searching manually; they implement warm-started paths internally.
- The 1-SE rule often selects 30–60% fewer features than the min-CV λ with comparable test performance.
- For genomics (p=20k+), use coordinate descent with sparse matrix representation for memory efficiency.
- Plot the coefficient path to inspect variable entry order — a natural feature importance ranking.

## Practical Workflow

A robust LASSO workflow: (1) standardise all features; (2) run LassoCV with 5 or 10 folds on a log-spaced λ grid covering the full path; (3) apply the 1-SE rule to get a sparser model; (4) examine the coefficient path plot for stability — variables that enter and exit the active set are unstable under small data perturbations; (5) refit a final model at the chosen λ on the full training set; (6) report features selected, their coefficients, and confidence intervals via bootstrap or cross-validated refitting.

---

