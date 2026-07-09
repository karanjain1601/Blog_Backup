---
title: "Local Outlier Factor (LOF) — Local Density Comparison"
slug: "local-outlier-factor"
description: "Implement LOF from scratch using k-distance, reachability distance, and local reachability density — then compare LOF against Isolation Forest on variable-density clustered data."
tags: ["anomaly-detection", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2xvYmFsIGFub21hbHkgZGV0ZWN0b3JzIChaLXNjb3JlLCBNYWhhbGFub2JpcykgZmFpbCB3aGVuIHRoZSBkYXRhc2V0IGhhcyBjbHVzdGVycyBvZiBkaWZmZXJlbnQgZGVuc2l0aWVzOiBhIHBvaW50IGluIGEgc3BhcnNlIGNsdXN0ZXIgbG9va3MgYW5vbWFsb3VzIGdsb2JhbGx5IGV2ZW4gaWYgaXQgYmVsb25ncyB0byBhIGdlbnVpbmUgc3BhcnNlIGNsdXN0ZXIuIExPRiBhZGRyZXNzZXMgdGhpcyBieSBjb21wYXJpbmcgdGhlIGxvY2FsIGRlbnNpdHkgb2YgZWFjaCBwb2ludCB0byB0aGUgbG9jYWwgZGVuc2l0eSBvZiBpdHMgbmVpZ2hib3Vycy4gQSBwb2ludCBpcyBhbm9tYWxvdXMgb25seSBpZiBpdCBpcyBzaWduaWZpY2FudGx5IGxlc3MgZGVuc2UgdGhhbiBpdHMgc3Vycm91bmRpbmcgbmVpZ2hib3VyaG9vZCDigJQgcmVnYXJkbGVzcyBvZiB0aGUgYWJzb2x1dGUgZGVuc2l0eS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJrLURpc3RhbmNlIGFuZCBSZWFjaGFiaWxpdHkgRGlzdGFuY2UifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrLWRpc3RhbmNlKHApIGlzIHRoZSBkaXN0YW5jZSBmcm9tIHBvaW50IHAgdG8gaXRzIGstdGggbmVhcmVzdCBuZWlnaGJvdXIuIFRoZSByZWFjaGFiaWxpdHkgZGlzdGFuY2UgcmVhY2hfZGlzdF9rKHAsbykgPSBtYXgoay1kaXN0YW5jZShvKSwgZGlzdChwLG8pKSBzbW9vdGhzIGRpc3RhbmNlcyBmb3IgbmVhcmJ5IHBvaW50czogaWYgcCBpcyB2ZXJ5IGNsb3NlIHRvIG8sIHRoZSBrLWRpc3RhbmNlKG8pIGJlY29tZXMgdGhlIGVmZmVjdGl2ZSBkaXN0YW5jZSwgcmVkdWNpbmcgdmFyaWFuY2UgaW4gbHJkIGZvciBkZW5zZSByZWdpb25zLiBUaGlzIHJlZ3VsYXJpc2F0aW9uIHByZXZlbnRzIGRpdmlzaW9uIGJ5IG5lYXItemVybyBkaXN0YW5jZXMgaW4gdGhlIGxyZCBjb21wdXRhdGlvbi4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6IlxcdGV4dHtscmR9X2socCkgPSBcXGZyYWN7MX17XFxmcmFjezF9e3xOX2socCl8fVxcc3VtX3tvIFxcaW4gTl9rKHApfSBcXHRleHR7cmVhY2gtZGlzdH1fayhwLG8pfSwgXFxxdWFkIFxcdGV4dHtMT0Z9X2socCkgPSBcXGZyYWN7XFxzdW1fe29cXGluIE5fayhwKX0gXFxmcmFje1xcdGV4dHtscmR9X2sobyl9e1xcdGV4dHtscmR9X2socCl9fXt8Tl9rKHApfH0ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMT0YgZnJvbSBTY3JhdGNoIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb21wdXRpbmcgTE9GIGZyb20gc2NyYXRjaCByZXF1aXJlczogKDEpIGZpbmRpbmcgay1uZWFyZXN0IG5laWdoYm91cnMgZm9yIGFsbCBwb2ludHMsICgyKSBjb21wdXRpbmcgay1kaXN0YW5jZXMsICgzKSBjb21wdXRpbmcgcmVhY2hhYmlsaXR5IGRpc3RhbmNlcywgKDQpIGNvbXB1dGluZyBsb2NhbCByZWFjaGFiaWxpdHkgZGVuc2l0eSAobHJkKSBhcyB0aGUgcmVjaXByb2NhbCBvZiBtZWFuIHJlYWNoYWJpbGl0eSBkaXN0YW5jZSwgYW5kICg1KSBjb21wdXRpbmcgTE9GIGFzIHRoZSBtZWFuIHJhdGlvIG9mIG5laWdoYm91ciBscmQgdG8gb3duIGxyZC4gTE9GIFx1MDAzZSAxIG1lYW5zIHRoZSBwb2ludCBpcyBsZXNzIGRlbnNlIHRoYW4gaXRzIG5laWdoYm91cnM7IExPRiDiiYggMSBtZWFucyBpdCBmaXRzIGl0cyBuZWlnaGJvdXJob29kLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5uZWlnaGJvcnMgaW1wb3J0IE5lYXJlc3ROZWlnaGJvcnNcblxuZGVmIGxvZl9mcm9tX3NjcmF0Y2goWCwgaz01KTpcbiAgICBuID0gbGVuKFgpXG4gICAgbmJycyA9IE5lYXJlc3ROZWlnaGJvcnMobl9uZWlnaGJvcnM9aysxKS5maXQoWClcbiAgICBkaXN0cywgaW5kaWNlcyA9IG5icnMua25laWdoYm9ycyhYKVxuICAgICMgay1kaXN0YW5jZTogZGlzdGFuY2UgdG8gay10aCBOTiAoaW5kZXggaywgc2tpcCBzZWxmIGF0IDApXG4gICAga19kaXN0cyA9IGRpc3RzWzosIGtdXG5cbiAgICBkZWYgcmVhY2hfZGlzdChwLCBvKTpcbiAgICAgICAgcmV0dXJuIG1heChrX2Rpc3RzW29dLCBucC5saW5hbGcubm9ybShYW3BdIC0gWFtvXSkpXG5cbiAgICAjIExvY2FsIHJlYWNoYWJpbGl0eSBkZW5zaXR5XG4gICAgbHJkID0gbnAuemVyb3MobilcbiAgICBmb3IgcCBpbiByYW5nZShuKTpcbiAgICAgICAgbmVpZ2hib3JzID0gaW5kaWNlc1twLCAxOl1cbiAgICAgICAgYXZnX3JkID0gbnAubWVhbihbcmVhY2hfZGlzdChwLCBpbnQobykpIGZvciBvIGluIG5laWdoYm9yc10pXG4gICAgICAgIGxyZFtwXSA9IDEuMCAvIChhdmdfcmQgKyAxZS0xMClcblxuICAgICMgTE9GIHNjb3JlXG4gICAgbG9mID0gbnAuemVyb3MobilcbiAgICBmb3IgcCBpbiByYW5nZShuKTpcbiAgICAgICAgbmVpZ2hib3JzID0gaW5kaWNlc1twLCAxOl1cbiAgICAgICAgbG9mW3BdID0gbnAubWVhbihbbHJkW2ludChvKV0gLyBscmRbcF0gZm9yIG8gaW4gbmVpZ2hib3JzXSlcbiAgICByZXR1cm4gbG9mXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCA9IG5wLnZzdGFjayhbXG4gICAgbnAucmFuZG9tLm5vcm1hbCgwLCAwLjUsICg4MCwgMikpLFxuICAgIG5wLnJhbmRvbS5ub3JtYWwoNSwgMC41LCAoODAsIDIpKSxcbiAgICBbWzguMCwgMS4wXSwgWy0xLjUsIDAuNV1dICAjIHRydWUgYW5vbWFsaWVzXG5dKVxubG9mX3Njb3JlcyA9IGxvZl9mcm9tX3NjcmF0Y2goWCwgaz0xMClcbnByaW50KGZcdTAwMjdUb3AgNSBMT0Ygc2NvcmVzOiB7bnAuc29ydChsb2Zfc2NvcmVzKVstNTpdWzo6LTFdLnJvdW5kKDIpLnRvbGlzdCgpfVx1MDAyNylcbnByaW50KGZcdTAwMjdBbm9tYWx5IGluZGljZXMgKExPRlx1MDAzZTIpOiB7bnAud2hlcmUobG9mX3Njb3JlcyBcdTAwM2UgMi4wKVswXS50b2xpc3QoKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50Ijoic2tsZWFybiBMT0Ygb24gTXVsdGktRGVuc2l0eSBEYXRhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJza2xlYXJuXHUwMDI3cyBMb2NhbE91dGxpZXJGYWN0b3IgY29tcHV0ZXMgTE9GIGVmZmljaWVudGx5IHVzaW5nIGEgYmFsbCB0cmVlIG9yIEtELXRyZWUgZm9yIG5laWdoYm91ciBxdWVyaWVzLiBUaGUgbmVnYXRpdmVfb3V0bGllcl9mYWN0b3JfIGF0dHJpYnV0ZSBjb250YWlucyDiiJJMT0YgKG1vcmUgbmVnYXRpdmUgPSBtb3JlIGFub21hbG91cywgY29uc2lzdGVudCB3aXRoIHNrbGVhcm5cdTAwMjdzIHNjb3JpbmcgY29udmVudGlvbikuIFRoZSBjb250YW1pbmF0aW9uIHBhcmFtZXRlciBzZXRzIHRoZSB0aHJlc2hvbGQ6IHBvaW50cyB3aG9zZSBMT0YgZXhjZWVkcyB0aGUgKDHiiJJjb250YW1pbmF0aW9uKSBxdWFudGlsZSBhcmUgZGVjbGFyZWQgYW5vbWFsaWVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2tsZWFybi5uZWlnaGJvcnMgaW1wb3J0IExvY2FsT3V0bGllckZhY3RvclxuXG5ucC5yYW5kb20uc2VlZCg0MilcblggPSBucC52c3RhY2soW1xuICAgIG5wLnJhbmRvbS5ub3JtYWwoWzAsMF0sICAwLjMsICgxMDAsIDIpKSwgICMgZGVuc2UgY2x1c3RlclxuICAgIG5wLnJhbmRvbS5ub3JtYWwoWzgsOF0sICAwLjMsICgxMDAsIDIpKSwgICMgZGVuc2UgY2x1c3RlclxuICAgIG5wLnJhbmRvbS5ub3JtYWwoWzQsNF0sICAyLjAsICg1MCwgIDIpKSwgICMgc3BhcnNlIHJlZ2lvblxuICAgIFtbMTIuMCwgMC4wXSwgWy0yLjAsIDguMF0sIFs0LjAsIDkuNV1dICAgIyB0cnVlIGFub21hbGllc1xuXSlcblxuY2xmID0gTG9jYWxPdXRsaWVyRmFjdG9yKG5fbmVpZ2hib3JzPTIwLCBjb250YW1pbmF0aW9uPTAuMDQpXG5wcmVkcyAgPSBjbGYuZml0X3ByZWRpY3QoWClcbnNjb3JlcyA9IC1jbGYubmVnYXRpdmVfb3V0bGllcl9mYWN0b3JfXG5cbnByaW50KGZcdTAwMjdEZXRlY3RlZCB7KHByZWRzPT0tMSkuc3VtKCl9IGFub21hbGllc1x1MDAyNylcbnByaW50KGZcdTAwMjdMT0Ygc2NvcmVzIGZvciBpbmplY3RlZCBhbm9tYWxpZXM6IHtzY29yZXNbLTM6XS5yb3VuZCgyKS50b2xpc3QoKX1cdTAwMjcpXG5wcmludChmXHUwMDI3TE9GIHNjb3JlcyBmb3IgZGVuc2UgY2x1c3RlciAoZmlyc3QgNSk6IHtzY29yZXNbOjVdLnJvdW5kKDIpLnRvbGlzdCgpfVx1MDAyNylcblxuZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSg4LCA2KSlcbnNjID0gYXguc2NhdHRlcihYWzosMF0sIFhbOiwxXSwgYz1zY29yZXMsIGNtYXA9XHUwMDI3WWxPclJkXHUwMDI3LCBzPTIwLCBhbHBoYT0wLjgpXG5heC5zY2F0dGVyKFhbcHJlZHM9PS0xLDBdLCBYW3ByZWRzPT0tMSwxXSxcbiAgICAgICAgICAgZWRnZWNvbG9ycz1cdTAwMjdyZWRcdTAwMjcsIGZhY2Vjb2xvcnM9XHUwMDI3bm9uZVx1MDAyNywgcz04MCwgbHc9MilcbnBsdC5jb2xvcmJhcihzYywgYXg9YXgsIGxhYmVsPVx1MDAyN0xPRiBTY29yZVx1MDAyNylcbmF4LnNldF90aXRsZShcdTAwMjdMT0Yg4oCUIE11bHRpLURlbnNpdHkgRGF0YVx1MDAyNylcbnBsdC50aWdodF9sYXlvdXQoKVxucGx0LnNhdmVmaWcoXHUwMDI3bG9mX211bHRpZGVuc2l0eS5wbmdcdTAwMjcsIGRwaT0xMDApIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTE9GIHZzIElzb2xhdGlvbiBGb3Jlc3Qgb24gVmFyaWFibGUtRGVuc2l0eSBDbHVzdGVycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTE9GIGV4Y2VscyB3aGVuIGFub21hbGllcyBhcmUgZGVmaW5lZCByZWxhdGl2ZSB0byBsb2NhbCBuZWlnaGJvdXJob29kIGRlbnNpdHkuIElzb2xhdGlvbiBGb3Jlc3QgdXNlcyBnbG9iYWwgcmFuZG9tIHBhcnRpdGlvbmluZyBhbmQgY2FuIG1pc3MgYW5vbWFsaWVzIHRoYXQgYXJlIG9ubHkgdW51c3VhbCB3aXRoaW4gYSBsb2NhbCBjb250ZXh0LiBUaGUgZGlmZmVyZW5jZSBpcyBtb3N0IHByb25vdW5jZWQgd2hlbiB0aGUgZGF0YXNldCBjb250YWlucyBjbHVzdGVycyBvZiB2ZXJ5IGRpZmZlcmVudCBzaXplcyBvciBkZW5zaXRpZXMg4oCUIExPRiBhZGFwdHMgdG8gZWFjaCBjbHVzdGVyXHUwMDI3cyBzY2FsZSB3aGlsZSBJc29sYXRpb24gRm9yZXN0IGFwcGxpZXMgYSBnbG9iYWwgaXNvbGF0aW9uIGNyaXRlcmlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubmVpZ2hib3JzIGltcG9ydCBMb2NhbE91dGxpZXJGYWN0b3JcbmZyb20gc2tsZWFybi5lbnNlbWJsZSBpbXBvcnQgSXNvbGF0aW9uRm9yZXN0XG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYXZlcmFnZV9wcmVjaXNpb25fc2NvcmVcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YX2RlbnNlICA9IG5wLnJhbmRvbS5ub3JtYWwoWzAsMF0sIDAuMywgKDIwMCwgMikpXG5YX3NwYXJzZSA9IG5wLnJhbmRvbS5ub3JtYWwoWzYsNl0sIDEuNSwgKDUwLCAgMikpXG5YX291dCAgICA9IG5wLmFycmF5KFtbMy4wLDMuMF0sIFstMi4wLDAuMF0sIFs4LjAsMC4wXSwgWzYuMCwxMC4wXV0pXG5YID0gbnAudnN0YWNrKFtYX2RlbnNlLCBYX3NwYXJzZSwgWF9vdXRdKVxueSA9IG5wLmFycmF5KFswXSoyNTAgKyBbMV0qNClcblxubG9mID0gTG9jYWxPdXRsaWVyRmFjdG9yKG5fbmVpZ2hib3JzPTE1LCBjb250YW1pbmF0aW9uPTAuMDE1KVxubG9mX3ByZWRzICA9IGxvZi5maXRfcHJlZGljdChYKVxubG9mX3Njb3JlcyA9IC1sb2YubmVnYXRpdmVfb3V0bGllcl9mYWN0b3JfXG5cbmlmbyA9IElzb2xhdGlvbkZvcmVzdChuX2VzdGltYXRvcnM9MTAwLCBjb250YW1pbmF0aW9uPTAuMDE1LCByYW5kb21fc3RhdGU9NDIpXG5pZm9fcHJlZHMgID0gaWZvLmZpdF9wcmVkaWN0KFgpXG5pZm9fc2NvcmVzID0gLWlmby5zY29yZV9zYW1wbGVzKFgpXG5cbmxvZl9hcCA9IGF2ZXJhZ2VfcHJlY2lzaW9uX3Njb3JlKHksIGxvZl9zY29yZXMpXG5pZm9fYXAgPSBhdmVyYWdlX3ByZWNpc2lvbl9zY29yZSh5LCBpZm9fc2NvcmVzKVxucHJpbnQoZlx1MDAyN0xPRiAg4oCUIEF2ZXJhZ2UgUHJlY2lzaW9uOiB7bG9mX2FwOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3SXNvRiDigJQgQXZlcmFnZSBQcmVjaXNpb246IHtpZm9fYXA6LjNmfVx1MDAyNylcbnByaW50KGZcdTAwMjdMT0YgIGRldGVjdGVkOiB7KGxvZl9wcmVkcz09LTEpLnN1bSgpfSB8IElzb0YgZGV0ZWN0ZWQ6IHsoaWZvX3ByZWRzPT0tMSkuc3VtKCl9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmVjdCBvZiBrIG9uIExPRiBTdGFiaWxpdHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNob29zaW5nIGsgaXMgdGhlIG1haW4gdHVuaW5nIGRlY2lzaW9uIGZvciBMT0YuIFNtYWxsIGsgKDMtNSkgaXMgdmVyeSBzZW5zaXRpdmUgdG8gbG9jYWwgZmx1Y3R1YXRpb25zIGFuZCBwcm9kdWNlcyBub2lzeSBMT0Ygc2NvcmVzLiBMYXJnZSBrICg0MCspIHN0YXJ0cyBjYXB0dXJpbmcgZ2xvYmFsIHN0cnVjdHVyZSByYXRoZXIgdGhhbiBsb2NhbCBkZW5zaXR5IGFuZCBjYW4gbWlzcyBsb2NhbCBhbm9tYWxpZXMuIFZhbHVlcyBpbiB0aGUgcmFuZ2Ugaz0xMCB0byAyMCBiYWxhbmNlIGxvY2FsIHNlbnNpdGl2aXR5IGFuZCBzdGFiaWxpdHkgZm9yIG1vc3QgZGF0YXNldHMuIElmIHRoZSBjbHVzdGVyIHNpemVzIGFyZSB2ZXJ5IGRpZmZlcmVudCwgc2V0IGsgc21hbGxlciB0aGFuIHRoZSBzbWFsbGVzdCBjbHVzdGVyIHNpemUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLm5laWdoYm9ycyBpbXBvcnQgTG9jYWxPdXRsaWVyRmFjdG9yXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWF9ub3JtYWwgID0gbnAucmFuZG9tLm5vcm1hbCgwLCAwLjUsICgxNTAsIDIpKVxuWF9hbm9tYWx5ID0gbnAuYXJyYXkoW1s0LjAsIDQuMF0sIFstMi4wLCAwLjVdXSlcblggPSBucC52c3RhY2soW1hfbm9ybWFsLCBYX2Fub21hbHldKVxuXG5rX3ZhbHVlcyA9IFszLCA1LCAxMCwgMjAsIDM1LCA1MF1cbnByaW50KGZcdTAwMjd7XCJrXCI6XHUwMDNlNH0ge1wiQW5vbWFseSBMT0YgKG1lYW4pXCI6XHUwMDNlMjB9IHtcIk5vcm1hbCBMT0YgKG1lYW4pXCI6XHUwMDNlMTh9IHtcIlNlcGFyYXRpb25cIjpcdTAwM2UxMn1cdTAwMjcpXG5mb3IgayBpbiBrX3ZhbHVlczpcbiAgICBjbGYgPSBMb2NhbE91dGxpZXJGYWN0b3Iobl9uZWlnaGJvcnM9aylcbiAgICBjbGYuZml0X3ByZWRpY3QoWClcbiAgICBsb2ZfcyA9IC1jbGYubmVnYXRpdmVfb3V0bGllcl9mYWN0b3JfXG4gICAgYV9zY29yZSA9IGxvZl9zWy0yOl0ubWVhbigpXG4gICAgbl9zY29yZSA9IGxvZl9zWzotMl0ubWVhbigpXG4gICAgc2VwID0gYV9zY29yZSAvIG5fc2NvcmUgaWYgbl9zY29yZSBcdTAwM2UgMCBlbHNlIGZsb2F0KFx1MDAyN2luZlx1MDAyNylcbiAgICBwcmludChmXHUwMDI3e2s6XHUwMDNlNH0ge2Ffc2NvcmU6XHUwMDNlMjAuM2Z9IHtuX3Njb3JlOlx1MDAzZTE4LjNmfSB7c2VwOlx1MDAzZTEyLjJmfXhcdTAwMjcpXG5wcmludChcdTAwMjdTbWFsbCBrOiBub2lzeS4gaz0xMC0yMDogZ29vZCBiYWxhbmNlLiBMYXJnZSBrOiBnbG9iYWwsIG1pc3NlcyBsb2NhbCBhbm9tYWxpZXMuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1ldGhvZCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkxvY2FsIHZzIEdsb2JhbCIsIkNvbXBsZXhpdHkiLCJIaWdoLWRpbSIsIlZhcmlhYmxlLWRlbnNpdHkgY2x1c3RlcnMiLCJUaHJlc2hvbGQiXSwicm93cyI6W1siTE9GIiwiTG9jYWwiLCJPKG7CsiBrKSBuYWl2ZSIsIlBvb3IiLCJFeGNlbGxlbnQiLCJMT0YgXHUwMDNlIHRocmVzaG9sZCJdLFsiR0xPU0ggKEhEQlNDQU4pIiwiSGllcmFyY2hpY2FsIGxvY2FsIiwiTyhuIGxvZyBuKSIsIk1vZGVyYXRlIiwiR29vZCIsIlNjb3JlIFx1MDAzZSBwZXJjZW50aWxlIl0sWyJJc29sYXRpb24gRm9yZXN0IiwiR2xvYmFsIiwiTyhuIGxvZyBuKSIsIkV4Y2VsbGVudCIsIk1vZGVyYXRlIiwiY29udGFtaW5hdGlvbiBwYXJhbSJdLFsia05OLWRpc3RhbmNlIiwiTG9jYWwiLCJPKG7CsiBrKSIsIlBvb3IiLCJHb29kIiwiRGlzdGFuY2UgXHUwMDNlIHBlcmNlbnRpbGUiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiTE9GIGluIEhpZ2ggRGltZW5zaW9ucyIsImNvbnRlbnQiOiJJbiBoaWdoLWRpbWVuc2lvbmFsIHNwYWNlcyAoZCBcdTAwM2UgMjApLCBhbGwgcGFpcndpc2UgZGlzdGFuY2VzIGNvbnZlcmdlIHRvIHRoZSBzYW1lIHZhbHVlIChjb25jZW50cmF0aW9uIG9mIG1lYXN1cmUpLiBUaGlzIG1lYW5zIGtOTiBkaXN0YW5jZXMgYmVjb21lIG5lYXJseSBlcXVhbCBhY3Jvc3MgYWxsIHBvaW50cywgYW5kIExPRiBzY29yZXMgbG9zZSBkaXNjcmltaW5hdGlvbiBwb3dlci4gRm9yIGhpZ2gtZGltZW5zaW9uYWwgZGF0YSwgcHJlZmVyIElzb2xhdGlvbiBGb3Jlc3Qgb3IgYSBkaW1lbnNpb25hbGl0eSByZWR1Y3Rpb24gc3RlcCBiZWZvcmUgTE9GLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR0xPU0ggKEdsb2JhbC1Mb2NhbCBPdXRsaWVyIFNjb3JlcyBmcm9tIEhpZXJhcmNoaWVzKSBpcyBhIHJlbGF0ZWQgYWxnb3JpdGhtIHRoYXQgY29tcHV0ZXMgb3V0bGllciBzY29yZXMgZnJvbSB0aGUgSERCU0NBTiBjbHVzdGVyaW5nIGhpZXJhcmNoeS4gVW5saWtlIExPRiB3aGljaCB1c2VzIGEgZml4ZWQgaywgR0xPU0ggYWRhcHRzIHRoZSBuZWlnaGJvdXJob29kIHNjYWxlIGF1dG9tYXRpY2FsbHkuIEl0IGlzIGltcGxlbWVudGVkIGluIGhkYnNjYW4uSERCU0NBTiB3aXRoIHRoZSBvdXRsaWVyX3Njb3Jlc18gYXR0cmlidXRlIGFuZCBpcyBwYXJ0aWN1bGFybHkgZWZmZWN0aXZlIHdoZW4gY2x1c3RlciBzaXplcyB2YXJ5IGdyZWF0bHkgYWNyb3NzIHRoZSBkYXRhc2V0LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTE9GID0gMS4wIG1lYW5zIGEgcG9pbnQgaXMgYXMgZGVuc2UgYXMgaXRzIG5laWdoYm91cnMg4oCUIG5vcm1hbCIsIkxPRiBcdTAwM2VcdTAwM2UgMSBtZWFucyBhIHBvaW50IGlzIG11Y2ggbGVzcyBkZW5zZSB0aGFuIGl0cyBuZWlnaGJvdXJzIOKAlCBhbm9tYWx5IiwiTE9GIHNsaWdodGx5IFx1MDAzYyAxIGNhbiBpbmRpY2F0ZSBhIHBvaW50IGluIGEgZGVuc2VyIHN1Yi1yZWdpb24gdGhhbiBpdHMgbmVpZ2hib3VycyIsIlVzZSBrPTIwIGFzIGEgc3RhcnRpbmcgZGVmYXVsdDsgdHVuZSBieSBpbnNwZWN0aW5nIExPRiBzY29yZSBoaXN0b2dyYW1zIiwiRm9yIGxhcmdlIGRhdGFzZXRzIChuIFx1MDAzZSA1MCwwMDApLCB1c2UgYXBwcm94aW1hdGUgbmVpZ2hib3VycyAoYWxnb3JpdGhtPVx1MDAyN2JhbGxfdHJlZVx1MDAyNyBvciBGQUlTUykiXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMT0YgaXMgYXZhaWxhYmxlIGluIHNjaWtpdC1sZWFybiBpbiB0d28gbW9kZXM6IGZpdF9wcmVkaWN0KCkgZm9yIG9mZmxpbmUgYW5vbWFseSBkZXRlY3Rpb24gKHRyYWlucyBhbmQgc2NvcmVzIHRoZSBzYW1lIGRhdGEpLCBhbmQgbm92ZWx0eT1UcnVlIG1vZGUgZm9yIG9ubGluZSBub3ZlbHR5IGRldGVjdGlvbiAodHJhaW5zIG9uIGNsZWFuIGRhdGEsIHNjb3JlcyBuZXcgcG9pbnRzKS4gSW4gbm92ZWx0eSBtb2RlLCB0aGUgZGVjaXNpb25fZnVuY3Rpb24oKSBhbmQgcHJlZGljdCgpIG1ldGhvZHMgd29yayBvbiBuZXcgZGF0YSwgbWFraW5nIExPRiB1c2FibGUgaW4gcHJvZHVjdGlvbiBzY29yaW5nIHBpcGVsaW5lcy4ifV0="
---
# Local Outlier Factor (LOF) — Local Density Comparison

Global anomaly detectors (Z-score, Mahalanobis) fail when the dataset has clusters of different densities: a point in a sparse cluster looks anomalous globally even if it belongs to a genuine sparse cluster. LOF addresses this by comparing the local density of each point to the local density of its neighbours. A point is anomalous only if it is significantly less dense than its surrounding neighbourhood — regardless of the absolute density.

## k-Distance and Reachability Distance

The k-distance(p) is the distance from point p to its k-th nearest neighbour. The reachability distance reach_dist_k(p,o) = max(k-distance(o), dist(p,o)) smooths distances for nearby points: if p is very close to o, the k-distance(o) becomes the effective distance, reducing variance in lrd for dense regions. This regularisation prevents division by near-zero distances in the lrd computation.

$$\text{lrd}_k(p) = \frac{1}{\frac{1}{|N_k(p)|}\sum_{o \in N_k(p)} \text{reach-dist}_k(p,o)}, \quad \text{LOF}_k(p) = \frac{\sum_{o\in N_k(p)} \frac{\text{lrd}_k(o)}{\text{lrd}_k(p)}}{|N_k(p)|}$$

## LOF from Scratch

Computing LOF from scratch requires: (1) finding k-nearest neighbours for all points, (2) computing k-distances, (3) computing reachability distances, (4) computing local reachability density (lrd) as the reciprocal of mean reachability distance, and (5) computing LOF as the mean ratio of neighbour lrd to own lrd. LOF > 1 means the point is less dense than its neighbours; LOF ≈ 1 means it fits its neighbourhood.

```python
import numpy as np
from sklearn.neighbors import NearestNeighbors

def lof_from_scratch(X, k=5):
    n = len(X)
    nbrs = NearestNeighbors(n_neighbors=k+1).fit(X)
    dists, indices = nbrs.kneighbors(X)
    # k-distance: distance to k-th NN (index k, skip self at 0)
    k_dists = dists[:, k]

    def reach_dist(p, o):
        return max(k_dists[o], np.linalg.norm(X[p] - X[o]))

    # Local reachability density
    lrd = np.zeros(n)
    for p in range(n):
        neighbors = indices[p, 1:]
        avg_rd = np.mean([reach_dist(p, int(o)) for o in neighbors])
        lrd[p] = 1.0 / (avg_rd + 1e-10)

    # LOF score
    lof = np.zeros(n)
    for p in range(n):
        neighbors = indices[p, 1:]
        lof[p] = np.mean([lrd[int(o)] / lrd[p] for o in neighbors])
    return lof

np.random.seed(42)
X = np.vstack([
    np.random.normal(0, 0.5, (80, 2)),
    np.random.normal(5, 0.5, (80, 2)),
    [[8.0, 1.0], [-1.5, 0.5]]  # true anomalies
])
lof_scores = lof_from_scratch(X, k=10)
print(f'Top 5 LOF scores: {np.sort(lof_scores)[-5:][::-1].round(2).tolist()}')
print(f'Anomaly indices (LOF>2): {np.where(lof_scores > 2.0)[0].tolist()}')
```

## sklearn LOF on Multi-Density Data

sklearn's LocalOutlierFactor computes LOF efficiently using a ball tree or KD-tree for neighbour queries. The negative_outlier_factor_ attribute contains −LOF (more negative = more anomalous, consistent with sklearn's scoring convention). The contamination parameter sets the threshold: points whose LOF exceeds the (1−contamination) quantile are declared anomalies.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

np.random.seed(42)
X = np.vstack([
    np.random.normal([0,0],  0.3, (100, 2)),  # dense cluster
    np.random.normal([8,8],  0.3, (100, 2)),  # dense cluster
    np.random.normal([4,4],  2.0, (50,  2)),  # sparse region
    [[12.0, 0.0], [-2.0, 8.0], [4.0, 9.5]]   # true anomalies
])

clf = LocalOutlierFactor(n_neighbors=20, contamination=0.04)
preds  = clf.fit_predict(X)
scores = -clf.negative_outlier_factor_

print(f'Detected {(preds==-1).sum()} anomalies')
print(f'LOF scores for injected anomalies: {scores[-3:].round(2).tolist()}')
print(f'LOF scores for dense cluster (first 5): {scores[:5].round(2).tolist()}')

fig, ax = plt.subplots(figsize=(8, 6))
sc = ax.scatter(X[:,0], X[:,1], c=scores, cmap='YlOrRd', s=20, alpha=0.8)
ax.scatter(X[preds==-1,0], X[preds==-1,1],
           edgecolors='red', facecolors='none', s=80, lw=2)
plt.colorbar(sc, ax=ax, label='LOF Score')
ax.set_title('LOF — Multi-Density Data')
plt.tight_layout()
plt.savefig('lof_multidensity.png', dpi=100)
```

## LOF vs Isolation Forest on Variable-Density Clusters

LOF excels when anomalies are defined relative to local neighbourhood density. Isolation Forest uses global random partitioning and can miss anomalies that are only unusual within a local context. The difference is most pronounced when the dataset contains clusters of very different sizes or densities — LOF adapts to each cluster's scale while Isolation Forest applies a global isolation criterion.

```python
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.metrics import average_precision_score

np.random.seed(42)
X_dense  = np.random.normal([0,0], 0.3, (200, 2))
X_sparse = np.random.normal([6,6], 1.5, (50,  2))
X_out    = np.array([[3.0,3.0], [-2.0,0.0], [8.0,0.0], [6.0,10.0]])
X = np.vstack([X_dense, X_sparse, X_out])
y = np.array([0]*250 + [1]*4)

lof = LocalOutlierFactor(n_neighbors=15, contamination=0.015)
lof_preds  = lof.fit_predict(X)
lof_scores = -lof.negative_outlier_factor_

ifo = IsolationForest(n_estimators=100, contamination=0.015, random_state=42)
ifo_preds  = ifo.fit_predict(X)
ifo_scores = -ifo.score_samples(X)

lof_ap = average_precision_score(y, lof_scores)
ifo_ap = average_precision_score(y, ifo_scores)
print(f'LOF  — Average Precision: {lof_ap:.3f}')
print(f'IsoF — Average Precision: {ifo_ap:.3f}')
print(f'LOF  detected: {(lof_preds==-1).sum()} | IsoF detected: {(ifo_preds==-1).sum()}')
```

## Effect of k on LOF Stability

Choosing k is the main tuning decision for LOF. Small k (3-5) is very sensitive to local fluctuations and produces noisy LOF scores. Large k (40+) starts capturing global structure rather than local density and can miss local anomalies. Values in the range k=10 to 20 balance local sensitivity and stability for most datasets. If the cluster sizes are very different, set k smaller than the smallest cluster size.

```python
import numpy as np
from sklearn.neighbors import LocalOutlierFactor

np.random.seed(42)
X_normal  = np.random.normal(0, 0.5, (150, 2))
X_anomaly = np.array([[4.0, 4.0], [-2.0, 0.5]])
X = np.vstack([X_normal, X_anomaly])

k_values = [3, 5, 10, 20, 35, 50]
print(f'{"k":>4} {"Anomaly LOF (mean)":>20} {"Normal LOF (mean)":>18} {"Separation":>12}')
for k in k_values:
    clf = LocalOutlierFactor(n_neighbors=k)
    clf.fit_predict(X)
    lof_s = -clf.negative_outlier_factor_
    a_score = lof_s[-2:].mean()
    n_score = lof_s[:-2].mean()
    sep = a_score / n_score if n_score > 0 else float('inf')
    print(f'{k:>4} {a_score:>20.3f} {n_score:>18.3f} {sep:>12.2f}x')
print('Small k: noisy. k=10-20: good balance. Large k: global, misses local anomalies.')
```

## Method Comparison

| Method | Local vs Global | Complexity | High-dim | Variable-density clusters | Threshold |
| --- | --- | --- | --- | --- | --- |
| LOF | Local | O(n² k) naive | Poor | Excellent | LOF > threshold |
| GLOSH (HDBSCAN) | Hierarchical local | O(n log n) | Moderate | Good | Score > percentile |
| Isolation Forest | Global | O(n log n) | Excellent | Moderate | contamination param |
| kNN-distance | Local | O(n² k) | Poor | Good | Distance > percentile |

> **LOF in High Dimensions**: In high-dimensional spaces (d > 20), all pairwise distances converge to the same value (concentration of measure). This means kNN distances become nearly equal across all points, and LOF scores lose discrimination power. For high-dimensional data, prefer Isolation Forest or a dimensionality reduction step before LOF.

GLOSH (Global-Local Outlier Scores from Hierarchies) is a related algorithm that computes outlier scores from the HDBSCAN clustering hierarchy. Unlike LOF which uses a fixed k, GLOSH adapts the neighbourhood scale automatically. It is implemented in hdbscan.HDBSCAN with the outlier_scores_ attribute and is particularly effective when cluster sizes vary greatly across the dataset.

- LOF = 1.0 means a point is as dense as its neighbours — normal
- LOF >> 1 means a point is much less dense than its neighbours — anomaly
- LOF slightly < 1 can indicate a point in a denser sub-region than its neighbours
- Use k=20 as a starting default; tune by inspecting LOF score histograms
- For large datasets (n > 50,000), use approximate neighbours (algorithm='ball_tree' or FAISS)

LOF is available in scikit-learn in two modes: fit_predict() for offline anomaly detection (trains and scores the same data), and novelty=True mode for online novelty detection (trains on clean data, scores new points). In novelty mode, the decision_function() and predict() methods work on new data, making LOF usable in production scoring pipelines.

