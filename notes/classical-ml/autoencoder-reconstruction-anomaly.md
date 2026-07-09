---
title: "Autoencoder Reconstruction Error for Anomaly Detection"
slug: "autoencoder-reconstruction-anomaly"
description: "Train autoencoders on normal data and use reconstruction error as anomaly score — covering dense, CNN, and LSTM architectures with threshold selection strategies and memorization pitfalls."
tags: ["anomaly-detection", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXV0b2VuY29kZXJzIGxlYXJuIGEgY29tcHJlc3NlZCByZXByZXNlbnRhdGlvbiBvZiBub3JtYWwgdHJhaW5pbmcgZGF0YSBieSBlbmNvZGluZyBpdCBpbnRvIGEgbG93LWRpbWVuc2lvbmFsIGxhdGVudCBzcGFjZSBhbmQgZGVjb2RpbmcgaXQgYmFjay4gVHJhaW5lZCBleGNsdXNpdmVseSBvbiBub3JtYWwgZGF0YSwgdGhlIGF1dG9lbmNvZGVyIGxlYXJucyB0aGUgbWFuaWZvbGQgb2Ygbm9ybWFsIHBhdHRlcm5zLiBBdCB0ZXN0IHRpbWUsIG5vcm1hbCBwb2ludHMgcmVjb25zdHJ1Y3Qgd2VsbCAobG93IGVycm9yKSB3aGlsZSBhbm9tYWxpZXMg4oCUIHdoaWNoIGRvIG5vdCBsaWUgb24gdGhlIGxlYXJuZWQgbWFuaWZvbGQg4oCUIHByb2R1Y2UgaGlnaCByZWNvbnN0cnVjdGlvbiBlcnJvcnMuIFRoZSBhbm9tYWx5IHNjb3JlIGlzIHNpbXBseSDigJZ4IOKIkiBkZWNvZGVyKGVuY29kZXIoeCkp4oCWwrIuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVjb25zdHJ1Y3Rpb24gRXJyb3IgYXMgQW5vbWFseSBTY29yZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGF1dG9lbmNvZGVyIG1pbmltaXNlcyByZWNvbnN0cnVjdGlvbiBlcnJvciBvdmVyIG5vcm1hbCB0cmFpbmluZyBkYXRhLiBUaGUgYm90dGxlbmVjayAobGF0ZW50IGRpbWVuc2lvbiBcdTAwM2MgaW5wdXQgZGltZW5zaW9uKSBmb3JjZXMgdGhlIG1vZGVsIHRvIGxlYXJuIGEgY29tcGFjdCByZXByZXNlbnRhdGlvbiBjYXB0dXJpbmcgb25seSB0aGUgbWFpbiB2YXJpYW5jZSBkaXJlY3Rpb25zLiBBbm9tYWxpZXMsIGJ5IGRlZmluaXRpb24gbm90IHdlbGwtcmVwcmVzZW50ZWQgYnkgdGhpcyBjb21wYWN0IGNvZGUsIHByb2R1Y2UgaGlnaCBkZWNvZGVyIGVycm9yLiBUaGUga2V5IHBhcmFtZXRlcnMgYXJlIGxhdGVudCBkaW1lbnNpb24gKHNtYWxsZXIgPSBtb3JlIGNvbXByZXNzaW9uID0gaGlnaGVyIHNlbnNpdGl2aXR5IGJ1dCBtb3JlIGZhbHNlIHBvc2l0aXZlcykgYW5kIGFyY2hpdGVjdHVyZSBkZXB0aC4ifSx7InR5cGUiOiJtYXRoIiwiZGlzcGxheSI6dHJ1ZSwiY29udGVudCI6IlxcdGV4dHtzY29yZX0oeCkgPSBcXHx4IC0gZyhmKHgpKVxcfF4yLCBcXHF1YWQgXFx0ZXh0e2ZsYWcgaWYgc2NvcmV9KHgpIFx1MDAzZSBcXHRhdSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlbnNlIEF1dG9lbmNvZGVyIGZvciBUYWJ1bGFyIERhdGEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciB0YWJ1bGFyIGRhdGEsIGEgZGVuc2UgKGZ1bGx5IGNvbm5lY3RlZCkgYXV0b2VuY29kZXIgd2l0aCAyLTMgaGlkZGVuIGxheWVycyBhbmQgYSBib3R0bGVuZWNrIGxhdGVudCBkaW1lbnNpb24gb2YgMi04IGlzIHR5cGljYWxseSBzdWZmaWNpZW50LiBUcmFpbiBvbmx5IG9uIG5vcm1hbCBkYXRhIHVzaW5nIEFkYW0sIG1lYW4tc3F1YXJlZCBlcnJvciBsb3NzLCBhbmQgZWFybHkgc3RvcHBpbmcgb24gYSBoZWxkLW91dCB2YWxpZGF0aW9uIHNldCBvZiBub3JtYWwgZGF0YS4gQWZ0ZXIgdHJhaW5pbmcsIGNvbXB1dGUgcGVyLXNhbXBsZSByZWNvbnN0cnVjdGlvbiBlcnJvciBvbiB0aGUgZnVsbCBkYXRhc2V0IHRvIGdlbmVyYXRlIGFub21hbHkgc2NvcmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFMb2FkZXIsIFRlbnNvckRhdGFzZXRcblxubnAucmFuZG9tLnNlZWQoNDIpOyB0b3JjaC5tYW51YWxfc2VlZCg0Milcblhfbm9ybWFsICA9IG5wLnJhbmRvbS5ub3JtYWwoMCwgMSwgKDEwMDAsIDIwKSkuYXN0eXBlKG5wLmZsb2F0MzIpXG5YX2Fub21hbHkgPSBucC5yYW5kb20udW5pZm9ybSgtNCwgNCwgKDUwLCAgMjApKS5hc3R5cGUobnAuZmxvYXQzMilcblxuY2xhc3MgQXV0b2VuY29kZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9pbiwgZF9sYXQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbmMgPSBubi5TZXF1ZW50aWFsKG5uLkxpbmVhcihkX2luLCA2NCksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBubi5MaW5lYXIoNjQsIGRfbGF0KSwgbm4uUmVMVSgpKVxuICAgICAgICBzZWxmLmRlYyA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKGRfbGF0LCA2NCksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBubi5MaW5lYXIoNjQsIGRfaW4pKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiByZXR1cm4gc2VsZi5kZWMoc2VsZi5lbmMoeCkpXG5cbmRzICA9IFRlbnNvckRhdGFzZXQodG9yY2gudGVuc29yKFhfbm9ybWFsKSlcbmRsICA9IERhdGFMb2FkZXIoZHMsIGJhdGNoX3NpemU9NjQsIHNodWZmbGU9VHJ1ZSlcbm1kbCA9IEF1dG9lbmNvZGVyKDIwLCA0KVxub3B0ID0gdG9yY2gub3B0aW0uQWRhbShtZGwucGFyYW1ldGVycygpLCBscj0xZS0zKVxuXG5mb3IgZXBvY2ggaW4gcmFuZ2UoNTApOlxuICAgIGZvciAoeGIsKSBpbiBkbDpcbiAgICAgICAgbG9zcyA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MobWRsKHhiKSwgeGIpXG4gICAgICAgIG9wdC56ZXJvX2dyYWQoKTsgbG9zcy5iYWNrd2FyZCgpOyBvcHQuc3RlcCgpXG5cbm1kbC5ldmFsKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIFhuX3QgPSB0b3JjaC50ZW5zb3IoWF9ub3JtYWwpXG4gICAgWGFfdCA9IHRvcmNoLnRlbnNvcihYX2Fub21hbHkpXG4gICAgZXJyX24gPSBubi5mdW5jdGlvbmFsLm1zZV9sb3NzKG1kbChYbl90KSwgWG5fdCwgcmVkdWN0aW9uPVx1MDAyN25vbmVcdTAwMjcpLm1lYW4oMSkubnVtcHkoKVxuICAgIGVycl9hID0gbm4uZnVuY3Rpb25hbC5tc2VfbG9zcyhtZGwoWGFfdCksIFhhX3QsIHJlZHVjdGlvbj1cdTAwMjdub25lXHUwMDI3KS5tZWFuKDEpLm51bXB5KClcbnByaW50KGZcdTAwMjdOb3JtYWwgIHJlY29uIGVycm9yOiB7ZXJyX24ubWVhbigpOi4zZn0gKy8tIHtlcnJfbi5zdGQoKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0Fub21hbHkgcmVjb24gZXJyb3I6IHtlcnJfYS5tZWFuKCk6LjNmfSArLy0ge2Vycl9hLnN0ZCgpOi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhyZXNob2xkIFNlbGVjdGlvbiBTdHJhdGVnaWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdGhyZXNob2xkIM+EIGRldGVybWluZXMgdGhlIHByZWNpc2lvbi1yZWNhbGwgdHJhZGVvZmYuIENvbW1vbiBzdHJhdGVnaWVzOiAoMSkgZml4ZWQgcGVyY2VudGlsZSBvZiB0cmFpbmluZyBlcnJvcnMgKGUuZy4sIDk1dGggb3IgOTl0aCBwZXJjZW50aWxlKSwgKDIpIG9wdGltaXNlIEYxIG9uIGEgc21hbGwgbGFiZWxsZWQgdmFsaWRhdGlvbiBzZXQsICgzKSBmaXQgZXh0cmVtZSB2YWx1ZSB0aGVvcnkgKEd1bWJlbCkgdG8gdHJhaW5pbmcgZXJyb3JzIGFuZCB1c2UgYSByZXR1cm4gbGV2ZWwsICg0KSBQUi1jdXJ2ZSBvcHRpbXVtIGZvciB0aGUgdGFyZ2V0IHJlY2FsbC4gVHJhaW5pbmcgcGVyY2VudGlsZSBpcyB0aGUgc2ltcGxlc3QgYW5kIG1vc3QgY29tbW9uIGFwcHJvYWNoIGluIHByYWN0aWNlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBwcmVjaXNpb25fcmVjYWxsX2N1cnZlLCBhdmVyYWdlX3ByZWNpc2lvbl9zY29yZVxuXG5ucC5yYW5kb20uc2VlZCg0MilcbnRyYWluX2Vycm9ycyAgPSBucC5yYW5kb20uZXhwb25lbnRpYWwoc2NhbGU9MC41LCBzaXplPTEwMDApXG5ub3JtYWxfdGVzdCAgID0gbnAucmFuZG9tLmV4cG9uZW50aWFsKHNjYWxlPTAuNSwgc2l6ZT0yMDApXG5hbm9tYWx5X3Rlc3QgID0gbnAucmFuZG9tLmV4cG9uZW50aWFsKHNjYWxlPTIuNSwgc2l6ZT0zMClcbnRlc3RfZXJyb3JzICAgPSBucC5jb25jYXRlbmF0ZShbbm9ybWFsX3Rlc3QsIGFub21hbHlfdGVzdF0pXG55X3RydWUgICAgICAgID0gbnAuYXJyYXkoWzBdKjIwMCArIFsxXSozMClcblxucHJpbnQoXHUwMDI3LS0tIFBlcmNlbnRpbGUgVGhyZXNob2xkcyAtLS1cdTAwMjcpXG5mb3IgcGN0IGluIFs5MCwgOTUsIDk5XTpcbiAgICB0YXUgPSBucC5wZXJjZW50aWxlKHRyYWluX2Vycm9ycywgcGN0KVxuICAgIHByZWRzID0gKHRlc3RfZXJyb3JzIFx1MDAzZSB0YXUpLmFzdHlwZShpbnQpXG4gICAgcHJlYyA9IChwcmVkcyBcdTAwMjYgeV90cnVlKS5zdW0oKSAvIG1heChwcmVkcy5zdW0oKSwgMSlcbiAgICByZWMgID0gKHByZWRzIFx1MDAyNiB5X3RydWUpLnN1bSgpIC8geV90cnVlLnN1bSgpXG4gICAgZjEgICA9IDIqcHJlYypyZWMvKHByZWMrcmVjKzFlLTgpXG4gICAgcHJpbnQoZlx1MDAyNyAgUHtwY3R9OiB0YXU9e3RhdTouM2Z9ICBQPXtwcmVjOi4yZn0gIFI9e3JlYzouMmZ9ICBGMT17ZjE6LjJmfVx1MDAyNylcblxucHJpbnQoXHUwMDI3LS0tIFBSLUN1cnZlIE9wdGltYWwgVGhyZXNob2xkIC0tLVx1MDAyNylcbnByZWNfYywgcmVjX2MsIHRocmVzID0gcHJlY2lzaW9uX3JlY2FsbF9jdXJ2ZSh5X3RydWUsIHRlc3RfZXJyb3JzKVxuZjFfYyA9IDIqcHJlY19jKnJlY19jLyhwcmVjX2MrcmVjX2MrMWUtOClcbmJlc3QgPSBucC5hcmdtYXgoZjFfYylcbnByaW50KGZcdTAwMjcgIHRhdT17dGhyZXNbYmVzdF06LjNmfSAgUD17cHJlY19jW2Jlc3RdOi4yZn0gIFI9e3JlY19jW2Jlc3RdOi4yZn0gIEYxPXtmMV9jW2Jlc3RdOi4yZn1cdTAwMjcpXG5hcCA9IGF2ZXJhZ2VfcHJlY2lzaW9uX3Njb3JlKHlfdHJ1ZSwgdGVzdF9lcnJvcnMpXG5wcmludChmXHUwMDI3ICBBVVBSQzoge2FwOi4zZn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ05OIEF1dG9lbmNvZGVyIGZvciBJbWFnZSBBbm9tYWx5IERldGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGltYWdlIGRhdGEsIGNvbnZvbHV0aW9uYWwgYXV0b2VuY29kZXJzIGNhcHR1cmUgc3BhdGlhbCBzdHJ1Y3R1cmUgbW9yZSBlZmZlY3RpdmVseSB0aGFuIGRlbnNlIGF1dG9lbmNvZGVycy4gVGhlIGVuY29kZXIgdXNlcyBDb252MmQgKyBNYXhQb29sMmQgdG8gZG93bnNhbXBsZTsgdGhlIGRlY29kZXIgdXNlcyBDb252VHJhbnNwb3NlMmQgdG8gdXBzYW1wbGUgYmFjayB0byBvcmlnaW5hbCByZXNvbHV0aW9uLiBUaGUgcmVjb25zdHJ1Y3Rpb24gZXJyb3IgaXMgY29tcHV0ZWQgcGVyLXBpeGVsIGFuZCBhdmVyYWdlZC4gVGhlIGJvdHRsZW5lY2sgc3BhdGlhbCByZXNvbHV0aW9uIChub3QganVzdCBjaGFubmVsIGNvdW50KSBjb250cm9scyBjb21wcmVzc2lvbjogYSA3w5c3IGJvdHRsZW5lY2sgZm9yIDI4w5cyOCBpbWFnZXMgY2FwdHVyZXMgZ2xvYmFsIHN0cnVjdHVyZSBvbmx5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxuXG5jbGFzcyBDb252QUUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmVuYyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoMSwgMTYsIDMsIHBhZGRpbmc9MSksIG5uLlJlTFUoKSwgbm4uTWF4UG9vbDJkKDIpLFxuICAgICAgICAgICAgbm4uQ29udjJkKDE2LCA4LCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKCksIG5uLk1heFBvb2wyZCgyKVxuICAgICAgICApXG4gICAgICAgIHNlbGYuZGVjID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnZUcmFuc3Bvc2UyZCg4LCAxNiwgMiwgc3RyaWRlPTIpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252VHJhbnNwb3NlMmQoMTYsIDEsIDIsIHN0cmlkZT0yKSwgbm4uU2lnbW9pZCgpXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTogcmV0dXJuIHNlbGYuZGVjKHNlbGYuZW5jKHgpKVxuXG5tb2RlbCA9IENvbnZBRSgpXG5vcHQgICA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0zKVxuXG5YX25vcm1hbCAgPSB0b3JjaC56ZXJvcygyMDAsIDEsIDI4LCAyOCkgKyAwLjMqdG9yY2gucmFuZG4oMjAwLCAxLCAyOCwgMjgpXG5YX2Fub21hbHkgPSB0b3JjaC5yYW5kKDEwLCAxLCAyOCwgMjgpXG5cbmZvciBfIGluIHJhbmdlKDMwKTpcbiAgICByZWMgID0gbW9kZWwoWF9ub3JtYWwpXG4gICAgbG9zcyA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MocmVjLCBYX25vcm1hbClcbiAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuXG5tb2RlbC5ldmFsKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIGVycl9uID0gbm4uZnVuY3Rpb25hbC5tc2VfbG9zcyhtb2RlbChYX25vcm1hbCksICBYX25vcm1hbCwgIHJlZHVjdGlvbj1cdTAwMjdub25lXHUwMDI3KS5tZWFuKFsxLDIsM10pXG4gICAgZXJyX2EgPSBubi5mdW5jdGlvbmFsLm1zZV9sb3NzKG1vZGVsKFhfYW5vbWFseSksIFhfYW5vbWFseSwgcmVkdWN0aW9uPVx1MDAyN25vbmVcdTAwMjcpLm1lYW4oWzEsMiwzXSlcbnByaW50KGZcdTAwMjdOb3JtYWwgIHJlY29uIGVycm9yOiB7ZXJyX24ubWVhbigpOi40Zn0gKy8tIHtlcnJfbi5zdGQoKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0Fub21hbHkgcmVjb24gZXJyb3I6IHtlcnJfYS5tZWFuKCk6LjRmfSArLy0ge2Vycl9hLnN0ZCgpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3U2VwYXJhdGlvbiByYXRpbzoge2Vycl9hLm1lYW4oKS9lcnJfbi5tZWFuKCk6LjFmfXhcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTFNUTSBBdXRvZW5jb2RlciBmb3IgU2VxdWVuY2UgQW5vbWFseSBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkZvciB0aW1lLXNlcmllcyBhbmQgc2VxdWVuY2UgZGF0YSwgTFNUTSBhdXRvZW5jb2RlcnMgZW5jb2RlIHRoZSBmdWxsIHNlcXVlbmNlIGludG8gYSBmaXhlZC1zaXplIGhpZGRlbiBzdGF0ZSBhbmQgZGVjb2RlIGl0IGJhY2sgdG8gdGhlIG9yaWdpbmFsIHNlcXVlbmNlLiBUaGUgZW5jb2RlciByZWFkcyB0aGUgc2VxdWVuY2UgZm9yd2FyZDsgdGhlIGRlY29kZXIgcmVjZWl2ZXMgdGhlIGZpbmFsIGhpZGRlbiBzdGF0ZSByZXBlYXRlZCBhcyBpbnB1dCBhbmQgZ2VuZXJhdGVzIHRoZSByZWNvbnN0cnVjdGlvbi4gVHJhaW5pbmcgb24gbm9ybWFsIHNlcXVlbmNlcyB0ZWFjaGVzIHRoZSBtb2RlbCB0ZW1wb3JhbCBwYXR0ZXJuczsgYW5vbWFsb3VzIHNlcXVlbmNlcyB3aXRoIHVudXN1YWwgZHluYW1pY3MgcHJvZHVjZSBoaWdoIHBlci10aW1lc3RlcCByZWNvbnN0cnVjdGlvbiBlcnJvci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBudW1weSBhcyBucFxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcblNFUSwgRkVBVCA9IDMwLCA1XG5cbmNsYXNzIExTVE1BdXRvZW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX2ZlYXQsIGxhdGVudD04KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jID0gbm4uTFNUTShuX2ZlYXQsICBsYXRlbnQsIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgICAgIHNlbGYuZGVjID0gbm4uTFNUTShsYXRlbnQsIG5fZmVhdCwgIGJhdGNoX2ZpcnN0PVRydWUpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIF8sIChoLCBfKSA9IHNlbGYuZW5jKHgpXG4gICAgICAgIGhfcmVwID0gaC5zcXVlZXplKDApLnVuc3F1ZWV6ZSgxKS5yZXBlYXQoMSwgeC5zaXplKDEpLCAxKVxuICAgICAgICBvdXQsIF8gPSBzZWxmLmRlYyhoX3JlcClcbiAgICAgICAgcmV0dXJuIG91dFxuXG5tb2RlbCA9IExTVE1BdXRvZW5jb2RlcihGRUFUKVxub3B0ICAgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcblxudCA9IHRvcmNoLmxpbnNwYWNlKDAsIDYuMjgsIFNFUSlcblhfbm9ybWFsICA9IHRvcmNoLnN0YWNrKFt0b3JjaC5zdGFjayhbXG4gICAgdG9yY2guc2luKHQgKyBpKjAuNSArIGopIGZvciBqIGluIHJhbmdlKEZFQVQpXSwgZGltPTEpIGZvciBpIGluIHJhbmdlKDMwMCldKVxuWF9hbm9tYWx5ID0gdG9yY2gucmFuZG4oMjAsIFNFUSwgRkVBVCkgKiAzXG5cbmZvciBfIGluIHJhbmdlKDQwKTpcbiAgICByZWMgID0gbW9kZWwoWF9ub3JtYWwpXG4gICAgbG9zcyA9IG5uLmZ1bmN0aW9uYWwubXNlX2xvc3MocmVjLCBYX25vcm1hbClcbiAgICBvcHQuemVyb19ncmFkKCk7IGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuXG5tb2RlbC5ldmFsKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIGVycl9uID0gbm4uZnVuY3Rpb25hbC5tc2VfbG9zcyhtb2RlbChYX25vcm1hbCksICBYX25vcm1hbCwgIHJlZHVjdGlvbj1cdTAwMjdub25lXHUwMDI3KS5tZWFuKFsxLDJdKS5udW1weSgpXG4gICAgZXJyX2EgPSBubi5mdW5jdGlvbmFsLm1zZV9sb3NzKG1vZGVsKFhfYW5vbWFseSksIFhfYW5vbWFseSwgcmVkdWN0aW9uPVx1MDAyN25vbmVcdTAwMjcpLm1lYW4oWzEsMl0pLm51bXB5KClcbnByaW50KGZcdTAwMjdOb3JtYWwgIHNlcSBlcnJvcjoge2Vycl9uLm1lYW4oKTouNGZ9ICsvLSB7ZXJyX24uc3RkKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdBbm9tYWx5IHNlcSBlcnJvcjoge2Vycl9hLm1lYW4oKTouNGZ9ICsvLSB7ZXJyX2Euc3RkKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaHJlc2hvbGQgTWV0aG9kcyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkxhYmVsIFJlcXVpcmVtZW50IiwiQ2FsaWJyYXRpb24iLCJSb2J1c3RuZXNzIiwiUmVjb21tZW5kZWQgRm9yIl0sInJvd3MiOltbIkZpeGVkIHBlcmNlbnRpbGUgKFA5NS9QOTkpIiwiTm9uZSAodHJhaW4gZXJyb3JzIG9ubHkpIiwiU2ltcGxlIOKAlCBzaW5nbGUgcGFyYW1ldGVyIiwiU2Vuc2l0aXZlIHRvIHRyYWluIGRpc3RyaWJ1dGlvbiIsIlF1aWNrIGJhc2VsaW5lLCBubyBsYWJlbGxlZCBhbm9tYWxpZXMiXSxbIlZhbGlkYXRpb24gc2V0IG9wdGltaXNhdGlvbiIsIlNtYWxsIGxhYmVsbGVkIHNldCBuZWVkZWQiLCJPcHRpbWlzZXMgdGFyZ2V0IG1ldHJpYyAoRjEvQVVQUkMpIiwiR29vZCBpZiB2YWwgc2V0IGlzIHJlcHJlc2VudGF0aXZlIiwiV2hlbiBhIGZldyBsYWJlbGxlZCBhbm9tYWxpZXMgYXJlIGF2YWlsYWJsZSJdLFsiRXh0cmVtZSB2YWx1ZSB0aGVvcnkgKEd1bWJlbCkiLCJOb25lICh0cmFpbiBlcnJvcnMgb25seSkiLCJQcmluY2lwbGVkIHN0YXRpc3RpY2FsIG1vZGVsIiwiUm9idXN0IGZvciByYXJlIGV4dHJlbWVzIiwiV2hlbiBhbm9tYWxpZXMgYXJlIHJhcmUgYW5kIGV4dHJlbWUiXSxbIlBSLWN1cnZlIG9wdGltdW0iLCJMYWJlbGxlZCB0ZXN0IHNldCByZXF1aXJlZCIsIk1heGltaXNlcyBGMSBhdCB0YXJnZXQgcmVjYWxsIiwiRGVwZW5kcyBvbiB0ZXN0IHNldCBxdWFsaXR5IiwiRXZhbHVhdGlvbiBhbmQgb2ZmbGluZSB0aHJlc2hvbGQgc2VsZWN0aW9uIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNZW1vcml6YXRpb24gUHJvYmxlbSBhbmQgUmVndWxhcmlzYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcG93ZXJmdWwgYXV0b2VuY29kZXIgKG1hbnkgbGF5ZXJzLCBsYXJnZSBsYXRlbnQgZGltKSBjYW4gbWVtb3Jpc2UgdHJhaW5pbmcgZGF0YSBhbmQgZ2VuZXJhbGlzZSB3ZWxsIGV2ZW4gdG8gYW5vbWFsaWVzLCBlbGltaW5hdGluZyB0aGUgc2NvcmUgZ2FwLiBSZWd1bGFyaXNhdGlvbiBzdHJhdGVnaWVzIHRvIHByZXZlbnQgdGhpczogKDEpIHVuZGVyY29tcGxldGUgYXJjaGl0ZWN0dXJlIChzbWFsbCBsYXRlbnQgZGltIGZvcmNlcyBjb21wcmVzc2lvbiksICgyKSBzcGFyc2UgYXV0b2VuY29kZXIgKEwxIHBlbmFsdHkgb24gbGF0ZW50IGFjdGl2YXRpb25zKSwgKDMpIGRlbm9pc2luZyBhdXRvZW5jb2RlciAodHJhaW4gdG8gcmVtb3ZlIG5vaXNlIOKAlCBhbm9tYWxpZXMgY2Fubm90IGJlIGRlbm9pc2VkKSwgKDQpIGRyb3BvdXQgaW4gZW5jb2Rlci9kZWNvZGVyLCAoNSkgZWFybHkgc3RvcHBpbmcgYmVmb3JlIHRoZSBtb2RlbCBvdmVyZml0cy4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6Ik1lbW9yaXNhdGlvbiBSaXNrIiwiY29udGVudCI6IklmIHRoZSB2YWxpZGF0aW9uIHJlY29uc3RydWN0aW9uIGVycm9yIHN0b3BzIGRlY3JlYXNpbmcgYnV0IHRoZSBnYXAgYmV0d2VlbiBub3JtYWwgYW5kIGFub21hbHkgc2NvcmVzIGNvbGxhcHNlcywgdGhlIG1vZGVsIGlzIG1lbW9yaXNpbmcgcmF0aGVyIHRoYW4gZ2VuZXJhbGlzaW5nLiBVc2UgZWFybHkgc3RvcHBpbmcgbW9uaXRvcmVkIG9uIGEgdmFsaWRhdGlvbiBzZXQgb2Ygbm9ybWFsIGRhdGEsIGFuZCBlbnN1cmUgdGhlIGxhdGVudCBkaW1lbnNpb24gaXMgbXVjaCBzbWFsbGVyIHRoYW4gdGhlIGlucHV0IGRpbWVuc2lvbiAocnVsZSBvZiB0aHVtYjogbGF0ZW50X2RpbSBcdTAwM2MgMC4yICogaW5wdXRfZGltIGZvciB0YWJ1bGFyIGRhdGEpLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIHRoZSA5NXRoIG9yIDk5dGggcGVyY2VudGlsZSBvZiB0cmFpbiByZWNvbnN0cnVjdGlvbiBlcnJvcnMgYXMgdGhlIGluaXRpYWwgdGhyZXNob2xkIiwiQWx3YXlzIHZpc3VhbGlzZSB0aGUgc2NvcmUgaGlzdG9ncmFtcyBmb3Igbm9ybWFsIGFuZCBhbm9tYWxvdXMgcG9pbnRzIHRvIGNoZWNrIHNlcGFyYXRpb24iLCJGb3IgaW1hZ2UgZGF0YSwgYWxzbyBpbnNwZWN0IHdvcnN0LXJlY29uc3RydWN0ZWQgaW1hZ2VzIHF1YWxpdGF0aXZlbHkiLCJEZW5vaXNpbmcgYXV0b2VuY29kZXJzIGFyZSBtb3JlIHJvYnVzdCB0byBtZW1vcmlzYXRpb24gdGhhbiBzdGFuZGFyZCBhdXRvZW5jb2RlcnMiLCJBVVBSQyAoYXJlYSB1bmRlciBwcmVjaXNpb24tcmVjYWxsIGN1cnZlKSBpcyB0aGUgcmlnaHQgZXZhbHVhdGlvbiBtZXRyaWMgZm9yIGltYmFsYW5jZWQgYW5vbWFseSBkZXRlY3Rpb24iXX1d"
---
# Autoencoder Reconstruction Error for Anomaly Detection

Autoencoders learn a compressed representation of normal training data by encoding it into a low-dimensional latent space and decoding it back. Trained exclusively on normal data, the autoencoder learns the manifold of normal patterns. At test time, normal points reconstruct well (low error) while anomalies — which do not lie on the learned manifold — produce high reconstruction errors. The anomaly score is simply ‖x − decoder(encoder(x))‖².

## Reconstruction Error as Anomaly Score

The autoencoder minimises reconstruction error over normal training data. The bottleneck (latent dimension < input dimension) forces the model to learn a compact representation capturing only the main variance directions. Anomalies, by definition not well-represented by this compact code, produce high decoder error. The key parameters are latent dimension (smaller = more compression = higher sensitivity but more false positives) and architecture depth.

$$\text{score}(x) = \|x - g(f(x))\|^2, \quad \text{flag if score}(x) > \tau$$

## Dense Autoencoder for Tabular Data

For tabular data, a dense (fully connected) autoencoder with 2-3 hidden layers and a bottleneck latent dimension of 2-8 is typically sufficient. Train only on normal data using Adam, mean-squared error loss, and early stopping on a held-out validation set of normal data. After training, compute per-sample reconstruction error on the full dataset to generate anomaly scores.

```python
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

np.random.seed(42); torch.manual_seed(42)
X_normal  = np.random.normal(0, 1, (1000, 20)).astype(np.float32)
X_anomaly = np.random.uniform(-4, 4, (50,  20)).astype(np.float32)

class Autoencoder(nn.Module):
    def __init__(self, d_in, d_lat):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(d_in, 64), nn.ReLU(),
                                  nn.Linear(64, d_lat), nn.ReLU())
        self.dec = nn.Sequential(nn.Linear(d_lat, 64), nn.ReLU(),
                                  nn.Linear(64, d_in))
    def forward(self, x): return self.dec(self.enc(x))

ds  = TensorDataset(torch.tensor(X_normal))
dl  = DataLoader(ds, batch_size=64, shuffle=True)
mdl = Autoencoder(20, 4)
opt = torch.optim.Adam(mdl.parameters(), lr=1e-3)

for epoch in range(50):
    for (xb,) in dl:
        loss = nn.functional.mse_loss(mdl(xb), xb)
        opt.zero_grad(); loss.backward(); opt.step()

mdl.eval()
with torch.no_grad():
    Xn_t = torch.tensor(X_normal)
    Xa_t = torch.tensor(X_anomaly)
    err_n = nn.functional.mse_loss(mdl(Xn_t), Xn_t, reduction='none').mean(1).numpy()
    err_a = nn.functional.mse_loss(mdl(Xa_t), Xa_t, reduction='none').mean(1).numpy()
print(f'Normal  recon error: {err_n.mean():.3f} +/- {err_n.std():.3f}')
print(f'Anomaly recon error: {err_a.mean():.3f} +/- {err_a.std():.3f}')
```

## Threshold Selection Strategies

The threshold τ determines the precision-recall tradeoff. Common strategies: (1) fixed percentile of training errors (e.g., 95th or 99th percentile), (2) optimise F1 on a small labelled validation set, (3) fit extreme value theory (Gumbel) to training errors and use a return level, (4) PR-curve optimum for the target recall. Training percentile is the simplest and most common approach in practice.

```python
import numpy as np
from sklearn.metrics import precision_recall_curve, average_precision_score

np.random.seed(42)
train_errors  = np.random.exponential(scale=0.5, size=1000)
normal_test   = np.random.exponential(scale=0.5, size=200)
anomaly_test  = np.random.exponential(scale=2.5, size=30)
test_errors   = np.concatenate([normal_test, anomaly_test])
y_true        = np.array([0]*200 + [1]*30)

print('--- Percentile Thresholds ---')
for pct in [90, 95, 99]:
    tau = np.percentile(train_errors, pct)
    preds = (test_errors > tau).astype(int)
    prec = (preds & y_true).sum() / max(preds.sum(), 1)
    rec  = (preds & y_true).sum() / y_true.sum()
    f1   = 2*prec*rec/(prec+rec+1e-8)
    print(f'  P{pct}: tau={tau:.3f}  P={prec:.2f}  R={rec:.2f}  F1={f1:.2f}')

print('--- PR-Curve Optimal Threshold ---')
prec_c, rec_c, thres = precision_recall_curve(y_true, test_errors)
f1_c = 2*prec_c*rec_c/(prec_c+rec_c+1e-8)
best = np.argmax(f1_c)
print(f'  tau={thres[best]:.3f}  P={prec_c[best]:.2f}  R={rec_c[best]:.2f}  F1={f1_c[best]:.2f}')
ap = average_precision_score(y_true, test_errors)
print(f'  AUPRC: {ap:.3f}')
```

## CNN Autoencoder for Image Anomaly Detection

For image data, convolutional autoencoders capture spatial structure more effectively than dense autoencoders. The encoder uses Conv2d + MaxPool2d to downsample; the decoder uses ConvTranspose2d to upsample back to original resolution. The reconstruction error is computed per-pixel and averaged. The bottleneck spatial resolution (not just channel count) controls compression: a 7×7 bottleneck for 28×28 images captures global structure only.

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(42)

class ConvAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2)
        )
        self.dec = nn.Sequential(
            nn.ConvTranspose2d(8, 16, 2, stride=2), nn.ReLU(),
            nn.ConvTranspose2d(16, 1, 2, stride=2), nn.Sigmoid()
        )
    def forward(self, x): return self.dec(self.enc(x))

model = ConvAE()
opt   = torch.optim.Adam(model.parameters(), lr=1e-3)

X_normal  = torch.zeros(200, 1, 28, 28) + 0.3*torch.randn(200, 1, 28, 28)
X_anomaly = torch.rand(10, 1, 28, 28)

for _ in range(30):
    rec  = model(X_normal)
    loss = nn.functional.mse_loss(rec, X_normal)
    opt.zero_grad(); loss.backward(); opt.step()

model.eval()
with torch.no_grad():
    err_n = nn.functional.mse_loss(model(X_normal),  X_normal,  reduction='none').mean([1,2,3])
    err_a = nn.functional.mse_loss(model(X_anomaly), X_anomaly, reduction='none').mean([1,2,3])
print(f'Normal  recon error: {err_n.mean():.4f} +/- {err_n.std():.4f}')
print(f'Anomaly recon error: {err_a.mean():.4f} +/- {err_a.std():.4f}')
print(f'Separation ratio: {err_a.mean()/err_n.mean():.1f}x')
```

## LSTM Autoencoder for Sequence Anomaly Detection

For time-series and sequence data, LSTM autoencoders encode the full sequence into a fixed-size hidden state and decode it back to the original sequence. The encoder reads the sequence forward; the decoder receives the final hidden state repeated as input and generates the reconstruction. Training on normal sequences teaches the model temporal patterns; anomalous sequences with unusual dynamics produce high per-timestep reconstruction error.

```python
import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(42)
SEQ, FEAT = 30, 5

class LSTMAutoencoder(nn.Module):
    def __init__(self, n_feat, latent=8):
        super().__init__()
        self.enc = nn.LSTM(n_feat,  latent, batch_first=True)
        self.dec = nn.LSTM(latent, n_feat,  batch_first=True)
    def forward(self, x):
        _, (h, _) = self.enc(x)
        h_rep = h.squeeze(0).unsqueeze(1).repeat(1, x.size(1), 1)
        out, _ = self.dec(h_rep)
        return out

model = LSTMAutoencoder(FEAT)
opt   = torch.optim.Adam(model.parameters(), lr=1e-3)

t = torch.linspace(0, 6.28, SEQ)
X_normal  = torch.stack([torch.stack([
    torch.sin(t + i*0.5 + j) for j in range(FEAT)], dim=1) for i in range(300)])
X_anomaly = torch.randn(20, SEQ, FEAT) * 3

for _ in range(40):
    rec  = model(X_normal)
    loss = nn.functional.mse_loss(rec, X_normal)
    opt.zero_grad(); loss.backward(); opt.step()

model.eval()
with torch.no_grad():
    err_n = nn.functional.mse_loss(model(X_normal),  X_normal,  reduction='none').mean([1,2]).numpy()
    err_a = nn.functional.mse_loss(model(X_anomaly), X_anomaly, reduction='none').mean([1,2]).numpy()
print(f'Normal  seq error: {err_n.mean():.4f} +/- {err_n.std():.4f}')
print(f'Anomaly seq error: {err_a.mean():.4f} +/- {err_a.std():.4f}')
```

## Threshold Methods Comparison

| Method | Label Requirement | Calibration | Robustness | Recommended For |
| --- | --- | --- | --- | --- |
| Fixed percentile (P95/P99) | None (train errors only) | Simple — single parameter | Sensitive to train distribution | Quick baseline, no labelled anomalies |
| Validation set optimisation | Small labelled set needed | Optimises target metric (F1/AUPRC) | Good if val set is representative | When a few labelled anomalies are available |
| Extreme value theory (Gumbel) | None (train errors only) | Principled statistical model | Robust for rare extremes | When anomalies are rare and extreme |
| PR-curve optimum | Labelled test set required | Maximises F1 at target recall | Depends on test set quality | Evaluation and offline threshold selection |

## Memorization Problem and Regularisation

A powerful autoencoder (many layers, large latent dim) can memorise training data and generalise well even to anomalies, eliminating the score gap. Regularisation strategies to prevent this: (1) undercomplete architecture (small latent dim forces compression), (2) sparse autoencoder (L1 penalty on latent activations), (3) denoising autoencoder (train to remove noise — anomalies cannot be denoised), (4) dropout in encoder/decoder, (5) early stopping before the model overfits.

> **Memorisation Risk**: If the validation reconstruction error stops decreasing but the gap between normal and anomaly scores collapses, the model is memorising rather than generalising. Use early stopping monitored on a validation set of normal data, and ensure the latent dimension is much smaller than the input dimension (rule of thumb: latent_dim < 0.2 * input_dim for tabular data).

- Use the 95th or 99th percentile of train reconstruction errors as the initial threshold
- Always visualise the score histograms for normal and anomalous points to check separation
- For image data, also inspect worst-reconstructed images qualitatively
- Denoising autoencoders are more robust to memorisation than standard autoencoders
- AUPRC (area under precision-recall curve) is the right evaluation metric for imbalanced anomaly detection

