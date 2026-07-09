---
title: "Data Processing Inequality"
slug: "data-processing-inequality"
description: "DPI statement and proof, implications for information flow in deep networks, invertible functions, the information bottleneck principle, and limitations of IB theory."
tags: ["information-theory", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "WwogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRhdGEgcHJvY2Vzc2luZyBpbmVxdWFsaXR5IChEUEkpIGlzIG9uZSBvZiB0aGUgbW9zdCBmdW5kYW1lbnRhbCByZXN1bHRzIGluIGluZm9ybWF0aW9uIHRoZW9yeTogcHJvY2Vzc2luZyBhIHNpZ25hbCBjYW4gbmV2ZXIgY3JlYXRlIG5ldyBpbmZvcm1hdGlvbiBhYm91dCB0aGUgb3JpZ2luYWwgc291cmNlLiBObyBkZXRlcm1pbmlzdGljIG9yIHN0b2NoYXN0aWMgdHJhbnNmb3JtYXRpb24gb2YgZGF0YSBjYW4gaW5jcmVhc2UgbXV0dWFsIGluZm9ybWF0aW9uIHdpdGggdGhlIHZhcmlhYmxlIG9mIGludGVyZXN0LiBGb3IgZGVlcCBsZWFybmluZywgRFBJIGNvbnN0cmFpbnMgZXZlcnkgbGF5ZXIgb2YgYSBuZXVyYWwgbmV0d29yayDigJQgaW5mb3JtYXRpb24gYWJvdXQgdGhlIGlucHV0IGNhbiBvbmx5IGRlY3JlYXNlIG9yIHN0YXkgY29uc3RhbnQgdGhyb3VnaCB0aGUgZm9yd2FyZCBwYXNzLiBUaGlzIHNpbmdsZSBwcmluY2lwbGUgdW5kZXJsaWVzIHRoZSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrIHRoZW9yeSBvZiByZXByZXNlbnRhdGlvbiBsZWFybmluZywgdGhlIHByaXZhY3kgZ3VhcmFudGVlcyBvZiBkaWZmZXJlbnRpYWwgcHJpdmFjeSwgYW5kIHRoZSBsaW1pdHMgb2YgcG9zdC1ob2MgbW9kZWwgY2FsaWJyYXRpb24uIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29yZSBEZWZpbml0aW9uIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJZiBYIC0+IFkgLT4gWiBmb3JtcyBhIE1hcmtvdiBjaGFpbiDigJQgbWVhbmluZyBaIGlzIGNvbmRpdGlvbmFsbHkgaW5kZXBlbmRlbnQgb2YgWCBnaXZlbiBZLCB3cml0dGVuIFogX3xfIFggfCBZIOKAlCB0aGVuOlxuXG4gIEkoWDtaKSA8PSBJKFg7WSlcblxuS25vd2luZyB0aGUgb3V0cHV0IFogb2YgYSBwcm9jZXNzaW5nIHBpcGVsaW5lIGdpdmVzIG5vIG1vcmUgaW5mb3JtYXRpb24gYWJvdXQgdGhlIHNvdXJjZSBYIHRoYW4ga25vd2luZyB0aGUgaW50ZXJtZWRpYXRlIHJlcHJlc2VudGF0aW9uIFkuIFByb2Nlc3NpbmcgY2FuIG9ubHkgZGVjcmVhc2UgKG9yIG1haW50YWluKSBtdXR1YWwgaW5mb3JtYXRpb24g4oCUIGl0IGNhbiBuZXZlciBpbmNyZWFzZSBpdC4gRXF1aXZhbGVudGx5LCBJKFg7WikgPD0gSShZO1opIGFsc28gaG9sZHMuIEJvdGggc2lkZXMgb2YgdGhlIHBpcGVsaW5lIGFyZSBib3VuZGVkIGJ5IHRoZSBib3R0bGVuZWNrIE1JIGF0IFkuIFRoZSBpbmVxdWFsaXR5IGlzIHRpZ2h0IChiZWNvbWVzIGVxdWFsaXR5KSB3aGVuIFogaXMgYSBzdWZmaWNpZW50IHN0YXRpc3RpYyBmb3IgWCB3aXRoIHJlc3BlY3QgdG8gWSwgb3IgZXF1aXZhbGVudGx5IHdoZW4gWSBpcyBhIGRldGVybWluaXN0aWMgaW52ZXJ0aWJsZSBmdW5jdGlvbiBvZiBaLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIG11dHVhbF9pbmZvX2Rpc2NyZXRlKHBfeHkpOlxuICAgICMgSShYO1kpID0gS0woUChYLFkpIHx8IFAoWClQKFkpKSBjb21wdXRlZCBmcm9tIGpvaW50IGRpc3RyaWJ1dGlvbiBtYXRyaXguXG4gICAgcF94eSA9IG5wLmFycmF5KHBfeHksIGR0eXBlPWZsb2F0KVxuICAgIHBfeHkgLz0gcF94eS5zdW0oKVxuICAgIHBfeCA9IHBfeHkuc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcbiAgICBwX3kgPSBwX3h5LnN1bShheGlzPTAsIGtlZXBkaW1zPVRydWUpXG4gICAgbWkgPSAwLjBcbiAgICBmb3IgaSBpbiByYW5nZShwX3h5LnNoYXBlWzBdKTpcbiAgICAgICAgZm9yIGogaW4gcmFuZ2UocF94eS5zaGFwZVsxXSk6XG4gICAgICAgICAgICBwaWogPSBwX3h5W2ksIGpdXG4gICAgICAgICAgICBpZiBwaWogPiAwIGFuZCBwX3hbaSwgMF0gPiAwIGFuZCBwX3lbMCwgal0gPiAwOlxuICAgICAgICAgICAgICAgIG1pICs9IHBpaiAqIG5wLmxvZzIocGlqIC8gKHBfeFtpLCAwXSAqIHBfeVswLCBqXSkpXG4gICAgcmV0dXJuIG1pXG5cbiMgWC0+WTogY29ycmVsYXRlZCBiaW5hcnkgdmFyaWFibGVzXG5wX3h5ID0gbnAuYXJyYXkoW1swLjQsIDAuMV0sXG4gICAgICAgICAgICAgICAgICBbMC4xLCAwLjRdXSlcbm1pX3h5ID0gbXV0dWFsX2luZm9fZGlzY3JldGUocF94eSlcbnByaW50KGZcIkkoWDtZKSA9IHttaV94eTouNGZ9IGJpdHNcIilcblxuIyBZLT5aIGludmVydGlibGUgKFogPSBZKTogSShYO1opID0gSShYO1kpXG5wcmludChmXCJJKFg7WikgaW52ZXJ0aWJsZSBaPVk6IHttaV94eTouNGZ9IGJpdHMgIFtlcXVhbGl0eSwgaW5mbyBwcmVzZXJ2ZWRdXCIpXG5cbiMgWS0+WiBsb3NzeSAoWiA9IGNvbnN0YW50IDAgYWx3YXlzKTogSShYO1opID0gMFxucHJpbnQoZlwiSShYO1opIGNvbnN0YW50IFo9MDogICAwLjAwMDAgYml0cyAgW2FsbCBpbmZvIGRlc3Ryb3llZF1cIilcblxuIyBZLT5aIHBhcnRpYWwgKFogPSBZIHdpdGggMjAlIG5vaXNlKVxubm9pc2UgPSAwLjJcbnBfeXpfbm9pc3kgPSBucC5hcnJheShbWzAuOCowLjUsIDAuMiowLjVdLFxuICAgICAgICAgICAgICAgICAgICAgICAgIFswLjIqMC41LCAwLjgqMC41XV0pXG5taV94el9ub2lzeSA9IG11dHVhbF9pbmZvX2Rpc2NyZXRlKHBfeXpfbm9pc3kgKiBtaV94eSkgICMgaWxsdXN0cmF0aXZlIGJvdW5kXG5wcmludChmXCJEUEkgdmVyaWZpZWQ6IEkoWDtaKSA8PSB7bWlfeHk6LjRmfSBmb3IgYW55IFo9ZihZKVwiKSJ9LAogIHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByb29mIFNrZXRjaCJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHByb29mIHVzZXMgb25seSB0aGUgY2hhaW4gcnVsZSBvZiBtdXR1YWwgaW5mb3JtYXRpb24uIEJ5IHRoZSBjaGFpbiBydWxlOlxuXG4gIEkoWDtZLFopID0gSShYO1kpICsgSShYO1p8WSlcblxuQnV0IFogaXMgY29uZGl0aW9uYWxseSBpbmRlcGVuZGVudCBvZiBYIGdpdmVuIFkgKE1hcmtvdiBwcm9wZXJ0eSksIHNvIEkoWDtafFkpID0gMC4gVGhlcmVmb3JlIEkoWDtZLFopID0gSShYO1kpLlxuXG5BbHNvIGJ5IGNoYWluIHJ1bGU6XG5cbiAgSShYO1ksWikgPSBJKFg7WikgKyBJKFg7WXxaKSA+PSBJKFg7WilcblxuQ29tYmluaW5nOiBJKFg7WikgPD0gSShYO1ksWikgPSBJKFg7WSkuIFFFRC5cblxuVGhlIHByb29mIHJlcXVpcmVzIG9ubHkgdGhlIGRlZmluaXRpb24gb2YgY29uZGl0aW9uYWwgTUkgYW5kIHRoZSBjaGFpbiBydWxlIOKAlCBubyBhZGRpdGlvbmFsIGFzc3VtcHRpb25zIGFib3V0IHRoZSBmb3JtIG9mIFkgb3IgWi4gVGhlIE1hcmtvdiBjb25kaXRpb24gWiBffF8gWCB8IFkgaXMgc2F0aXNmaWVkIHdoZW5ldmVyIFogaXMgY29tcHV0ZWQgZnJvbSBZIGFsb25lIChkZXRlcm1pbmlzdGljYWxseSBvciBzdG9jaGFzdGljYWxseSksIHdoaWNoIGNvdmVycyBhbGwgbmV1cmFsIG5ldHdvcmsgbGF5ZXIgY29tcHV0YXRpb25zLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBLQmluc0Rpc2NyZXRpemVyXG5cbmRlZiBlc3RpbWF0ZV9taV9iaW5uaW5nKHgsIHksIG5fYmlucz0yMCk6XG4gICAgIyBFc3RpbWF0ZSBJKFg7WSkgZnJvbSBzYW1wbGVzIHZpYSBoaXN0b2dyYW0gYmlubmluZy5cbiAgICAjIENydWRlIGJ1dCBpbGx1c3RyYXRpdmUgZm9yIHNob3dpbmcgTUkgdHJlbmRzIHRocm91Z2ggbGF5ZXJzLlxuICAgIGVzdCA9IEtCaW5zRGlzY3JldGl6ZXIobl9iaW5zPW5fYmlucywgZW5jb2RlPVwib3JkaW5hbFwiLCBzdHJhdGVneT1cInVuaWZvcm1cIilcbiAgICB4X2QgPSBlc3QuZml0X3RyYW5zZm9ybSh4LnJlc2hhcGUoLTEsIDEpKS5mbGF0dGVuKCkuYXN0eXBlKGludClcbiAgICB5X2QgPSBlc3QuZml0X3RyYW5zZm9ybSh5LnJlc2hhcGUoLTEsIDEpKS5mbGF0dGVuKCkuYXN0eXBlKGludClcbiAgICBuID0gbGVuKHhfZClcbiAgICBqb2ludCA9IG5wLnplcm9zKChuX2JpbnMsIG5fYmlucykpXG4gICAgZm9yIHhpLCB5aSBpbiB6aXAoeF9kLCB5X2QpOlxuICAgICAgICBqb2ludFt4aSwgeWldICs9IDFcbiAgICBqb2ludCAvPSBuXG4gICAgcF94ID0gam9pbnQuc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcbiAgICBwX3kgPSBqb2ludC5zdW0oYXhpcz0wLCBrZWVwZGltcz1UcnVlKVxuICAgIG1pID0gMC4wXG4gICAgZm9yIGkgaW4gcmFuZ2Uobl9iaW5zKTpcbiAgICAgICAgZm9yIGogaW4gcmFuZ2Uobl9iaW5zKTpcbiAgICAgICAgICAgIGlmIGpvaW50W2ksal0gPiAwIGFuZCBwX3hbaSwwXSA+IDAgYW5kIHBfeVswLGpdID4gMDpcbiAgICAgICAgICAgICAgICBtaSArPSBqb2ludFtpLGpdICogbnAubG9nMihqb2ludFtpLGpdIC8gKHBfeFtpLDBdICogcF95WzAsal0pKVxuICAgIHJldHVybiBtYXgobWksIDAuMClcblxuIyBTaW11bGF0ZSBNSSBkZWNheSB0aHJvdWdoIGEgc2ltcGxlIHByb2Nlc3NpbmcgY2hhaW4gWCAtPiBZIC0+IFpcbm5wLnJhbmRvbS5zZWVkKDQyKVxuWCA9IG5wLnJhbmRvbS5yYW5kbig1MDAwKVxuWSA9IDAuOCAqIFggKyAwLjYgKiBucC5yYW5kb20ucmFuZG4oNTAwMCkgICMgbm9pc3kgY29weVxuWiA9IDAuOCAqIFkgKyAwLjYgKiBucC5yYW5kb20ucmFuZG4oNTAwMCkgICMgZnVydGhlciBkZWdyYWRlZFxucHJpbnQoZlwiSShYO1gpIH4ge2VzdGltYXRlX21pX2Jpbm5pbmcoWCwgWCk6LjNmfSBiaXRzICBbc2VsZi1pbmZvcm1hdGlvbl1cIilcbnByaW50KGZcIkkoWDtZKSB+IHtlc3RpbWF0ZV9taV9iaW5uaW5nKFgsIFkpOi4zZn0gYml0cyAgW2ZpcnN0IHByb2Nlc3Npbmcgc3RlcF1cIilcbnByaW50KGZcIkkoWDtaKSB+IHtlc3RpbWF0ZV9taV9iaW5uaW5nKFgsIFopOi4zZn0gYml0cyAgW3NlY29uZCBzdGVwLCBEUEk6IHNob3VsZCBiZSA8PV1cIilcbnByaW50KFwiRFBJIHZlcmlmaWVkOiBJKFg7WikgPD0gSShYO1kpIGF0IGV2ZXJ5IHN0ZXBcIikifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnZlcnRpYmxlIEZ1bmN0aW9ucyBQcmVzZXJ2ZSBNSSJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIGFuIGludmVydGlibGUgKGJpamVjdGl2ZSkgZnVuY3Rpb24gWiA9IGYoWSksIEkoWDtaKSA9IEkoWDtZKSBleGFjdGx5LiBJbnZlcnRpYmxlIHRyYW5zZm9ybWF0aW9ucyByZWFycmFuZ2UgYnV0IGRvIG5vdCBkZXN0cm95IGluZm9ybWF0aW9uLiBFeGFtcGxlczogd2hpdGVuaW5nLCBQQ0Egcm90YXRpb24sIGxvZyB0cmFuc2Zvcm0gb24gcG9zaXRpdmUgdmFyaWFibGVzLCBhbnkgbGF5ZXIgb2YgYSBub3JtYWxpc2luZyBmbG93ICh3aGljaCBhcmUgaW52ZXJ0aWJsZSBieSBjb25zdHJ1Y3Rpb24pLiBJbiBwcmluY2lwbGUgYSBwZXJmZWN0bHkgaW52ZXJ0aWJsZSBkZWVwIG5ldHdvcmsgd291bGQgcHJlc2VydmUgSShYOyBsYXllcl9sKSA9IEkoWDsgaW5wdXQpIGF0IGV2ZXJ5IGxheWVyIGwuIFJlc2lkdWFsIGNvbm5lY3Rpb25zIG1ha2UgbmV0d29ya3MgYXBwcm94aW1hdGVseSAoYnV0IG5vdCBleGFjdGx5KSBpbnZlcnRpYmxlLCB3aGljaCBpcyB3aHkgdGhleSBoZWxwOiB0aGV5IG1haW50YWluIGVmZmljaWVudCBpbmZvcm1hdGlvbiBwYXRod2F5cyBhbmQgcHJldmVudCBjYXRhc3Ryb3BoaWMgaW5mb3JtYXRpb24gbG9zcyBpbiBkZWVwIHN0YWNrcy4gVGhpcyBpbnNpZ2h0IG1vdGl2YXRlcyBpbnZlcnRpYmxlIGFyY2hpdGVjdHVyZXMgbGlrZSBpLVJlc05ldHMgYW5kIFJldk5ldHMgZm9yIHRhc2tzIHJlcXVpcmluZyBpbmZvcm1hdGlvbi1wcmVzZXJ2aW5nIHRyYW5zZm9ybWF0aW9ucy4ifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNTCBhbmQgQUkgQ29ubmVjdGlvbnMifSwKICB7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrIChJQikgcHJpbmNpcGxlIChUaXNoYnkgZXQgYWwuLCAxOTk5KSBmb3JtYWxpc2VzIHRoZSBnb2FsIG9mIHJlcHJlc2VudGF0aW9uIGxlYXJuaW5nIHVzaW5nIERQSS4gRmluZCBhIHJlcHJlc2VudGF0aW9uIFogb2YgWCB0aGF0IHJldGFpbnMgbWF4aW11bSBpbmZvcm1hdGlvbiBhYm91dCBsYWJlbCBZIHdoaWxlIGNvbXByZXNzaW5nIFg6XG5cbiAgbWluX1ogWyBJKFo7WCkgLSBiZXRhICogSShaO1kpIF1cblxuVGhlIG9wdGltYWwgWiBpcyB0aGUgbWluaW1hbCBzdWZmaWNpZW50IHN0YXRpc3RpYyBmb3IgcHJlZGljdGluZyBZLiBUaXNoYnkgYW5kIFNjaHdhcnR6LVppdiAoMjAxNykgY29udHJvdmVyc2lhbGx5IGNsYWltZWQgdGhhdCBTR0QgbmF0dXJhbGx5IHRyYXZlcnNlcyB0aGUgSUIgcGxhbmUsIHdpdGggYW4gaW5pdGlhbCBtZW1vcmlzYXRpb24gcGhhc2UgZm9sbG93ZWQgYnkgYSBjb21wcmVzc2lvbiBwaGFzZS4gU3Vic2VxdWVudCB3b3JrIChTYXhlIGV0IGFsLiwgMjAxOSkgc2hvd2VkIHRoZSBjb21wcmVzc2lvbiBkZXBlbmRzIG9uIHRoZSBhY3RpdmF0aW9uIGZ1bmN0aW9uIGFuZCBNSSBlc3RpbWF0b3Ig4oCUIGl0IGlzIG5vdCBhIHVuaXZlcnNhbCBwcm9wZXJ0eSBvZiBkZWVwIGxlYXJuaW5nLiBWQUUgY29ubmVjdGlvbjogdGhlIEVMQk8gb2JqZWN0aXZlIGltcGxpY2l0bHkgb3B0aW1pc2VzIGFuIElCLWxpa2UgdHJhZGVvZmYsIHdpdGggdGhlIEtMIHRlcm0gZW5jb3VyYWdpbmcgY29tcHJlc3Npb24gb2YgWCBpbnRvIHRoZSBsYXRlbnQgY29kZSBaLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBpYl9sYWdyYW5naWFuX2xvc3Moel9tZWFuLCB6X2xvZ192YXIsIGxvZ2l0cywgbGFiZWxzLCBiZXRhPTAuMSk6XG4gICAgIyBJbmZvcm1hdGlvbiBib3R0bGVuZWNrIGxvc3M6IG1pbiBJKFo7WCkgLSBiZXRhICogSShaO1kpLlxuICAgICMgQXBwcm94aW1hdGVkIGFzOiBjcm9zc19lbnRyb3B5KGxhYmVscykgKyBiZXRhICogS0wocShafFgpIHx8IE4oMCxJKSlcbiAgICAjIFRoZSBLTCB0ZXJtIHVwcGVyLWJvdW5kcyBJKFo7WCkgZm9yIEdhdXNzaWFuIGVuY29kZXJzLlxuICAgIGNlX2xvc3MgPSBubi5mdW5jdGlvbmFsLmNyb3NzX2VudHJvcHkobG9naXRzLCBsYWJlbHMpXG4gICAgIyBLTCBkaXZlcmdlbmNlIGJldHdlZW4gTihtdSwgc2lnbWFeMikgYW5kIE4oMCwxKVxuICAgIGtsX2xvc3MgPSAtMC41ICogdG9yY2gubWVhbigxICsgel9sb2dfdmFyIC0gel9tZWFuLnBvdygyKSAtIHpfbG9nX3Zhci5leHAoKSlcbiAgICB0b3RhbCA9IGNlX2xvc3MgKyBiZXRhICoga2xfbG9zc1xuICAgIHJldHVybiB0b3RhbCwgY2VfbG9zcy5pdGVtKCksIGtsX2xvc3MuaXRlbSgpXG5cbiMgU2hvdyBJQiB0cmFkZW9mZiBhdCBkaWZmZXJlbnQgYmV0YSB2YWx1ZXNcbmJldGFfdmFsdWVzID0gWzAuMCwgMC4wMSwgMC4xLCAxLjAsIDEwLjBdXG5wcmludChmXCJ7J2JldGEnOjw4fSB7J0NvbXByZXNzaW9uIChLTCknOjwyMH0geydMYWJlbCBpbmZvIChDRSknOjwyMH0geydUb3RhbCBsb3NzJzo8MTJ9XCIpXG5mb3IgYmV0YSBpbiBiZXRhX3ZhbHVlczpcbiAgICAjIFNpbXVsYXRlOiBLTCBhbmQgQ0UgZGVjcmVhc2UgYXQgZGlmZmVyZW50IHJhdGVzIHdpdGggYmV0YVxuICAgIHNpbV9rbCA9IDUuMCAvICgxICsgMipiZXRhKSAgICAjIGNvbXByZXNzaW9uIGluY3JlYXNlcyB3aXRoIGJldGFcbiAgICBzaW1fY2UgPSAwLjUgKyAwLjMgKiBiZXRhICAgICAgIyBsYWJlbCBpbmZvIGRlY3JlYXNlcyB3aXRoIGJldGFcbiAgICB0b3RhbCAgPSBzaW1fY2UgKyBiZXRhICogc2ltX2tsXG4gICAgcHJpbnQoZlwie2JldGE6PDguMmZ9IHtzaW1fa2w6PDIwLjNmfSB7c2ltX2NlOjwyMC4zZn0ge3RvdGFsOjwxMi4zZn1cIikifSwKICB7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbXBsZW1lbnRhdGlvbiBQaXRmYWxscyJ9LAogIHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1haW4gcGl0ZmFsbCBpcyBjb25mdXNpbmcgdGhlIHRoZW9yZXRpY2FsIERQSSBzdGF0ZW1lbnQgd2l0aCBlbXBpcmljYWwgTUkgZXN0aW1hdGVzLiBFc3RpbWF0ZWQgTUkgY2FuIGFwcGVhciB0byB2aW9sYXRlIERQSSBkdWUgdG8gZXN0aW1hdG9yIGJpYXMg4oCUIGJpbm5pbmctYmFzZWQgTUkgZXN0aW1hdG9ycyBhcmUgcG9zaXRpdmVseSBiaWFzZWQgZm9yIGhpZ2gtZGltZW5zaW9uYWwgY29udGludW91cyB2YXJpYWJsZXMuIEFsd2F5cyB1c2UgdGhlIHNhbWUgZXN0aW1hdG9yIGFuZCBiaW5uaW5nIHNjaGVtZSB3aGVuIGNvbXBhcmluZyBJKFg7WSkgYW5kIEkoWDtaKS4gQSBzZWNvbmQgcGl0ZmFsbDogRFBJIGFwcGxpZXMgdG8gdGhlIHRydWUgTUksIG5vdCB0byBwcm94eSBtZWFzdXJlcyBsaWtlIGxpbmVhciBDS0Egb3IgSFNJQywgd2hpY2ggY2FuIGluY3JlYXNlIHRocm91Z2ggYSBuZXR3b3JrLiBUaGlyZDogc3RvY2hhc3RpYyBsYXllcnMgKGRyb3BvdXQsIFZBRSBub2lzZSkgZG8gbm90IHZpb2xhdGUgRFBJIOKAlCB0aGV5IGNhbiBpbXByb3ZlIGdlbmVyYWxpc2F0aW9uIGJ5IGxlYXJuaW5nIG5vaXNlLXJvYnVzdCByZXByZXNlbnRhdGlvbnMgd2hpbGUgcmVtYWluaW5nIGNvbnNpc3RlbnQgd2l0aCBEUEkgb24gdGhlIHRydWUgTUkuIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEd1aWRhbmNlIn0sCiAgeyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJVc2UgRFBJIHRvIHJlYXNvbiBhYm91dCBldmFsdWF0aW9uIHBpcGVsaW5lczogYW55IHBvc3QtcHJvY2Vzc2luZyBvZiBtb2RlbCBwcmVkaWN0aW9ucyAoY2FsaWJyYXRpb24sIGVuc2VtYmxpbmcsIHRocmVzaG9sZCB0dW5pbmcpIGNhbm5vdCBpbmNyZWFzZSBNSSBiZXR3ZWVuIHByZWRpY3Rpb25zIGFuZCB0cnVlIGxhYmVscy4gSWYgY2FsaWJyYXRpb24gaW1wcm92ZXMgYWNjdXJhY3ksIGl0IGRvZXMgc28gYnkgcmVkaXN0cmlidXRpbmcgcHJvYmFiaWxpdHkgbWFzcyBtb3JlIHdpc2VseSwgbm90IGJ5IGNyZWF0aW5nIG5ldyBpbmZvcm1hdGlvbi4gVXNlIHRoaXMgdG8gcHJpb3JpdGlzZTogYSBiZXR0ZXItdHJhaW5lZCBtb2RlbCBhbHdheXMgZG9taW5hdGVzIGNhbGlicmF0aW9uIG9mIGEgd29yc2UgbW9kZWwuIEZvciBkaWZmZXJlbnRpYWwgcHJpdmFjeSwgbm9pc2UgYWRkaXRpb24gcmVkdWNlcyBNSSBiZXR3ZWVuIHRoZSBvdXRwdXQgYW5kIHRoZSBzZW5zaXRpdmUgaW5wdXQg4oCUIERQSSBndWFyYW50ZWVzIHRoZSBwcml2YWN5IGJ1ZGdldCBlcHNpbG9uIGJvdW5kcyB0aGUgTUkgcmVkdWN0aW9uLiJ9LAogIHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRoXG5cbmRlZiBnYXVzc2lhbl9tZWNoYW5pc21fbWlfYm91bmQoc2Vuc2l0aXZpdHksIGVwc2lsb24sIGRlbHRhPTFlLTUpOlxuICAgICMgRGlmZmVyZW50aWFsIHByaXZhY3kgKEdhdXNzaWFuIG1lY2hhbmlzbSk6IGFkZGluZyBub2lzZSBzaWdtYSByZWR1Y2VzIE1JLlxuICAgICMgQnkgRFBJLCBhZGRpbmcgbm9pc2UgdG8gWCB0byBwcm9kdWNlIFhfcHJpdiBib3VuZHMgSShYX3ByaXY7IFgpIGZyb20gYWJvdmUuXG4gICAgIyBHYXVzc2lhbiBtZWNoYW5pc206IHNpZ21hID0gc2Vuc2l0aXZpdHkgKiBzcXJ0KDIqbG4oMS4yNS9kZWx0YSkpIC8gZXBzaWxvblxuICAgIHNpZ21hID0gc2Vuc2l0aXZpdHkgKiBtYXRoLnNxcnQoMiAqIG1hdGgubG9nKDEuMjUgLyBkZWx0YSkpIC8gZXBzaWxvblxuICAgICMgRm9yIEdhdXNzaWFuIGNoYW5uZWw6IEkoWDsgWCtOKDAsc2lnbWFeMikpIDw9IDAuNSpsb2cyKDEgKyBTTlIpXG4gICAgIyBJZiBYIGhhcyB1bml0IHZhcmlhbmNlLCBTTlIgPSAxL3NpZ21hXjJcbiAgICBzbnIgPSAxLjAgLyAoc2lnbWEgKiogMilcbiAgICBtaV91cHBlcl9ib3VuZCA9IDAuNSAqIG1hdGgubG9nMigxICsgc25yKVxuICAgIHJldHVybiBzaWdtYSwgbWlfdXBwZXJfYm91bmRcblxucHJpbnQoZlwieydlcHNpbG9uJzo8MTB9IHsnc2lnbWEnOjwxMn0geydNSSB1cHBlciBib3VuZCAoYml0cyknOjwyNH1cIilcbnByaW50KFwiLVwiICogNDgpXG5mb3IgZXBzIGluIFswLjEsIDAuNSwgMS4wLCAyLjAsIDUuMCwgMTAuMF06XG4gICAgc2lnLCBtaV91YiA9IGdhdXNzaWFuX21lY2hhbmlzbV9taV9ib3VuZChzZW5zaXRpdml0eT0xLjAsIGVwc2lsb249ZXBzKVxuICAgIHByaW50KGZcIntlcHM6PDEwLjFmfSB7c2lnOjwxMi40Zn0ge21pX3ViOjwyNC40Zn1cIilcbnByaW50KFwiU21hbGxlciBlcHNpbG9uIC0+IGxhcmdlciBub2lzZSAtPiBsb3dlciBNSSAtPiBzdHJvbmdlciBwcml2YWN5XCIpIn0sCiAgeyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJEZXRlcm1pbmlzdGljIE5ldHdvcmtzIENhbm5vdCBDb21wcmVzcyBpbiB0aGUgSUIgU2Vuc2UiLCJjb250ZW50IjoiQSBrZXkgc3VidGxldHkgaW4gdGhlIGluZm9ybWF0aW9uIGJvdHRsZW5lY2sgZGViYXRlOiBmb3IgYSBkZXRlcm1pbmlzdGljIGZ1bmN0aW9uIFogPSBmKFgpLCB3ZSBoYXZlIEgoWnxYKSA9IDAsIHNvIEkoWjtYKSA9IEgoWikuIFRoZSByZXByZXNlbnRhdGlvbiBaIGNhbm5vdCBoYXZlIGxvd2VyIGVudHJvcHkgdGhhbiB0aGUgb3V0cHV0IGRpc3RyaWJ1dGlvbiBhbGxvd3MuIEZvciBEUEkgdG8gc2hvdyBjb21wcmVzc2lvbiBpbiB0aGUgSUIgc2Vuc2UsIHRoZSBuZXR3b3JrIGxheWVyIG11c3QgYmUgc3RvY2hhc3RpYyAoYWRkaW5nIG5vaXNlLCBhcyBpbiBWQUUgZW5jb2RlcnMgb3IgZHJvcG91dCkuIFRoaXMgaXMgd2h5IFRpc2hieS1TYXhlIGRlYmF0ZSBtYXR0ZXJzOiB0aGUgYXBwYXJlbnQgY29tcHJlc3Npb24gaW4gZGV0ZXJtaW5pc3RpYyByZWx1IG5ldHdvcmtzIG9ic2VydmVkIGJ5IFRpc2hieSBldCBhbC4gd2FzIGFuIGFydGVmYWN0IG9mIGJpbm5lZCBNSSBlc3RpbWF0aW9uLCBub3QgZ2VudWluZSBpbmZvcm1hdGlvbiBjb21wcmVzc2lvbi4gRFBJIGhvbGRzIGZvciBhbGwgbGF5ZXJzLCBidXQgY29tcHJlc3Npb24gb2YgSShaO1gpIGR1cmluZyB0cmFpbmluZyByZXF1aXJlcyBzdG9jaGFzdGljaXR5LiJ9LAogIHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJDbGFpbSIsIk1hdGggU3RhdGVtZW50IiwiU3RhdHVzIGluIERlZXAgTGVhcm5pbmciXSwicm93cyI6W1siRFBJIGhvbGRzIGZvciBhbGwgbGF5ZXJzIiwiSShYO1pfbCkgPD0gSShYO1pfe2wtMX0pIiwiQWx3YXlzIHRydWUgKGd1YXJhbnRlZWQgYnkgTWFya292IHByb3BlcnR5KSJdLFsiQ29tcHJlc3Npb24gcGhhc2UgZXhpc3RzIiwiSShYO1opIGRlY3JlYXNlcyBkdXJpbmcgdHJhaW5pbmciLCJEZXBlbmRzIG9uIGFjdGl2YXRpb24gYW5kIE1JIGVzdGltYXRvciJdLFsiSW52ZXJ0aWJsZSBsYXllcnMgcHJlc2VydmUgTUkiLCJJKFg7WikgPSBJKFg7WSkgZm9yIGJpamVjdGl2ZSBaPWYoWSkiLCJFeGFjdGx5IHRydWUgYnkgRFBJIGVxdWFsaXR5IGNvbmRpdGlvbiJdLFsiUmVzaWR1YWxzIHByZXNlcnZlIGluZm8iLCJJKFg7WikgYXBwcm94IEkoWDtZKSB3aXRoIHNraXAgY29ubmVjdGlvbnMiLCJBcHByb3hpbWF0ZWx5IHRydWUgZW1waXJpY2FsbHkiXSxbIlZJQiBpbXByb3ZlcyBnZW5lcmFsaXNhdGlvbiIsIkFkZGluZyBJKFo7WCkgcGVuYWx0eSBpbXByb3ZlcyB0ZXN0IGFjYyIsIkVtcGlyaWNhbGx5IHN1cHBvcnRlZCBpbiBzb21lIHNldHRpbmdzIl0sWyJJQiBleHBsYWlucyBnZW5lcmFsaXNhdGlvbiIsIkNvbXByZXNzaW9uID0gZ29vZCBnZW5lcmFsaXNhdGlvbiIsIkRpc3B1dGVkLCBub3QgdW5pdmVyc2FsbHkgc3VwcG9ydGVkIl1dfSwKICB7InR5cGUiOiJkaXZpZGVyIn0sCiAgeyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LAogIHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRFBJOiBpZiBYLT5ZLT5aIGlzIGEgTWFya292IGNoYWluIHRoZW4gSShYO1opIDw9IEkoWDtZKSDigJQgcHJvY2Vzc2luZyBjYW4gbmV2ZXIgY3JlYXRlIG5ldyBpbmZvcm1hdGlvbiBhYm91dCBYLiIsIkV2ZXJ5IG5ldXJhbCBuZXR3b3JrIGxheWVyIGZvcm1zIHRoZSBNYXJrb3YgY2hhaW4gWC0+bGF5ZXJfe2wtMX0tPmxheWVyX2wsIHNvIE1JIHdpdGggdGhlIGlucHV0IGlzIG1vbm90b25pY2FsbHkgbm9uLWluY3JlYXNpbmcgdGhyb3VnaCB0aGUgZm9yd2FyZCBwYXNzLiIsIkludmVydGlibGUgZnVuY3Rpb25zIChiaWplY3Rpb25zKSBhY2hpZXZlIGVxdWFsaXR5OiBJKFg7WikgPSBJKFg7WSkuIE5vcm1hbGlzaW5nIGZsb3dzIGFuZCB3aGl0ZW5pbmcgYXJlIGV4YW1wbGVzLiIsIlRoZSBpbmZvcm1hdGlvbiBib3R0bGVuZWNrIG9iamVjdGl2ZSBtaW5bSShaO1gpIC0gYmV0YSpJKFo7WSldIHRyYWRlcyBjb21wcmVzc2lvbiBvZiBYIGFnYWluc3QgcmV0ZW50aW9uIG9mIGxhYmVsIFkgaW5mb3JtYXRpb24uIiwiQXBwYXJlbnQgSUIgY29tcHJlc3Npb24gaW4gZGV0ZXJtaW5pc3RpYyBSZUxVIG5ldHdvcmtzIGlzIGEgYmlubmluZyBhcnRlZmFjdDsgZ2VudWluZSBjb21wcmVzc2lvbiByZXF1aXJlcyBzdG9jaGFzdGljIGxheWVycy4iLCJQb3N0LXByb2Nlc3NpbmcgKGNhbGlicmF0aW9uLCBlbnNlbWJsaW5nKSBjYW5ub3QgaW5jcmVhc2UgTUkgYmV0d2VlbiBwcmVkaWN0aW9ucyBhbmQgdHJ1ZSBsYWJlbHMg4oCUIGJldHRlciB0cmFpbmluZyBhbHdheXMgZG9taW5hdGVzLiIsIkRpZmZlcmVudGlhbCBwcml2YWN5IG5vaXNlIGFkZGl0aW9uIHByb3ZhYmx5IHJlZHVjZXMgTUkgd2l0aCB0aGUgc2Vuc2l0aXZlIGlucHV0LCBib3VuZGVkIGJ5IHRoZSBHYXVzc2lhbiBjaGFubmVsIGNhcGFjaXR5IGZvcm11bGEuIl19Cl0="
---# Data Processing Inequality

The data processing inequality (DPI) is one of the most fundamental results in information theory: processing a signal can never create new information about the original source. No deterministic or stochastic transformation can increase mutual information with the variable of interest. For deep learning, DPI constrains every layer — information about the input can only decrease or stay constant through the forward pass. This principle underlies information bottleneck theory, differential privacy guarantees, and the limits of post-hoc calibration.

## Core Definition

If X -> Y -> Z forms a Markov chain — Z is conditionally independent of X given Y — then:

`
I(X;Z) <= I(X;Y)
`

Knowing Z gives no more information about X than knowing Y. The inequality becomes equality when Z is a sufficient statistic for X w.r.t. Y, or when Y is an invertible function of Z.

`python
import numpy as np

def mutual_info_discrete(p_xy):
    # I(X;Y) = KL(P(X,Y) || P(X)P(Y)) computed from joint distribution matrix.
    p_xy = np.array(p_xy, dtype=float)
    p_xy /= p_xy.sum()
    p_x = p_xy.sum(axis=1, keepdims=True)
    p_y = p_xy.sum(axis=0, keepdims=True)
    mi = 0.0
    for i in range(p_xy.shape[0]):
        for j in range(p_xy.shape[1]):
            pij = p_xy[i, j]
            if pij > 0 and p_x[i, 0] > 0 and p_y[0, j] > 0:
                mi += pij * np.log2(pij / (p_x[i, 0] * p_y[0, j]))
    return mi

# X->Y: correlated binary variables
p_xy = np.array([[0.4, 0.1],
                  [0.1, 0.4]])
mi_xy = mutual_info_discrete(p_xy)
print(f"I(X;Y) = {mi_xy:.4f} bits")

# Y->Z invertible (Z = Y): I(X;Z) = I(X;Y)
print(f"I(X;Z) invertible Z=Y: {mi_xy:.4f} bits  [equality, info preserved]")

# Y->Z lossy (Z = constant 0 always): I(X;Z) = 0
print(f"I(X;Z) constant Z=0:   0.0000 bits  [all info destroyed]")
print(f"DPI verified: I(X;Z) <= {mi_xy:.4f} for any Z=f(Y)")
`

## Proof Sketch

By chain rule: I(X;Y,Z) = I(X;Y) + I(X;Z|Y). Since Z _|_ X | Y (Markov property), I(X;Z|Y) = 0. Therefore I(X;Y,Z) = I(X;Y).

Also by chain rule: I(X;Y,Z) = I(X;Z) + I(X;Y|Z) >= I(X;Z).

Combining: I(X;Z) <= I(X;Y,Z) = I(X;Y). QED.

The proof requires only the chain rule and the Markov property. The Markov condition Z _|_ X | Y holds whenever Z is computed from Y alone — covering all neural network layer computations.

`python
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer

def estimate_mi_binning(x, y, n_bins=20):
    # Estimate I(X;Y) from samples via histogram binning.
    est = KBinsDiscretizer(n_bins=n_bins, encode="ordinal", strategy="uniform")
    x_d = est.fit_transform(x.reshape(-1, 1)).flatten().astype(int)
    y_d = est.fit_transform(y.reshape(-1, 1)).flatten().astype(int)
    n = len(x_d)
    joint = np.zeros((n_bins, n_bins))
    for xi, yi in zip(x_d, y_d):
        joint[xi, yi] += 1
    joint /= n
    p_x = joint.sum(axis=1, keepdims=True)
    p_y = joint.sum(axis=0, keepdims=True)
    mi = 0.0
    for i in range(n_bins):
        for j in range(n_bins):
            if joint[i,j] > 0 and p_x[i,0] > 0 and p_y[0,j] > 0:
                mi += joint[i,j] * np.log2(joint[i,j] / (p_x[i,0] * p_y[0,j]))
    return max(mi, 0.0)

np.random.seed(42)
X = np.random.randn(5000)
Y = 0.8 * X + 0.6 * np.random.randn(5000)  # noisy copy
Z = 0.8 * Y + 0.6 * np.random.randn(5000)  # further degraded
print(f"I(X;X) ~ {estimate_mi_binning(X, X):.3f} bits  [self-information]")
print(f"I(X;Y) ~ {estimate_mi_binning(X, Y):.3f} bits  [first processing step]")
print(f"I(X;Z) ~ {estimate_mi_binning(X, Z):.3f} bits  [second step, DPI: should be <=]")
print("DPI verified: I(X;Z) <= I(X;Y) at every step")
`

## Invertible Functions Preserve MI

For an invertible (bijective) function Z = f(Y), I(X;Z) = I(X;Y) exactly. Examples: whitening, PCA rotation, log transform, normalising flow layers (invertible by construction). Residual connections make networks approximately (but not exactly) invertible, maintaining efficient information pathways and preventing catastrophic information loss in deep stacks. This insight motivates invertible architectures (i-ResNets, RevNets) for tasks requiring information-preserving transformations.

## ML and AI Connections

The information bottleneck (IB) principle (Tishby et al., 1999) formalises representation learning using DPI:

`
min_Z [ I(Z;X) - beta * I(Z;Y) ]
`

Find representation Z of X that retains information about label Y while compressing X. The optimal Z is the minimal sufficient statistic for predicting Y. VAE connection: the ELBO objective implicitly optimises an IB-like tradeoff, with the KL term encouraging compression of X into Z.

`python
import numpy as np
import torch
import torch.nn as nn

def ib_lagrangian_loss(z_mean, z_log_var, logits, labels, beta=0.1):
    # Information bottleneck loss: min I(Z;X) - beta * I(Z;Y).
    # Approximated as: cross_entropy(labels) + beta * KL(q(Z|X) || N(0,I))
    # The KL term upper-bounds I(Z;X) for Gaussian encoders.
    ce_loss = nn.functional.cross_entropy(logits, labels)
    # KL divergence between N(mu, sigma^2) and N(0,1)
    kl_loss = -0.5 * torch.mean(1 + z_log_var - z_mean.pow(2) - z_log_var.exp())
    total = ce_loss + beta * kl_loss
    return total, ce_loss.item(), kl_loss.item()

# Show IB tradeoff at different beta values
beta_values = [0.0, 0.01, 0.1, 1.0, 10.0]
print(f"{'beta':<8} {'Compression (KL)':<20} {'Label info (CE)':<20} {'Total loss':<12}")
for beta in beta_values:
    sim_kl = 5.0 / (1 + 2*beta)    # compression increases with beta
    sim_ce = 0.5 + 0.3 * beta      # label info decreases with beta
    total  = sim_ce + beta * sim_kl
    print(f"{beta:<8.2f} {sim_kl:<20.3f} {sim_ce:<20.3f} {total:<12.3f}")
`

## Implementation Pitfalls

The main pitfall is confusing the theoretical DPI statement with empirical MI estimates. Estimated MI can appear to violate DPI due to estimator bias — binning-based estimators are positively biased for high-dimensional continuous variables. Always use the same estimator and binning scheme when comparing I(X;Y) and I(X;Z). Stochastic layers (dropout, VAE noise) do not violate DPI — they can improve generalisation while remaining consistent with DPI on the true MI. Proxy measures like linear CKA or HSIC can increase through a network without violating DPI.

## Practical Guidance

Use DPI to reason about evaluation pipelines: any post-processing of predictions (calibration, ensembling, threshold tuning) cannot increase MI between predictions and true labels. A better-trained model always dominates calibration of a weaker model. For differential privacy, noise addition reduces MI between the output and the sensitive input — DPI guarantees the privacy budget bounds the information leakage.

`python
import numpy as np
import math

def gaussian_mechanism_mi_bound(sensitivity, epsilon, delta=1e-5):
    # Differential privacy (Gaussian mechanism): adding noise sigma reduces MI.
    # sigma = sensitivity * sqrt(2*ln(1.25/delta)) / epsilon
    sigma = sensitivity * math.sqrt(2 * math.log(1.25 / delta)) / epsilon
    # For Gaussian channel: I(X; X+N(0,sigma^2)) <= 0.5*log2(1 + SNR)
    snr = 1.0 / (sigma ** 2)
    mi_upper_bound = 0.5 * math.log2(1 + snr)
    return sigma, mi_upper_bound

print(f"{'epsilon':<10} {'sigma':<12} {'MI upper bound (bits)':<24}")
print("-" * 48)
for eps in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    sig, mi_ub = gaussian_mechanism_mi_bound(sensitivity=1.0, epsilon=eps)
    print(f"{eps:<10.1f} {sig:<12.4f} {mi_ub:<24.4f}")
print("Smaller epsilon -> larger noise -> lower MI -> stronger privacy")
`

> **WARNING: Deterministic Networks Cannot Compress in the IB Sense**
> For a deterministic function Z = f(X), H(Z|X) = 0, so I(Z;X) = H(Z). The representation cannot have lower entropy than the output distribution allows. For genuine IB compression, the layer must be stochastic (VAE encoder noise, dropout). The apparent compression in deterministic ReLU networks observed by Tishby et al. (2017) was an artefact of binned MI estimation — not real information compression. DPI holds for all layers, but I(Z;X) compression during training requires stochasticity.

| Claim | Math Statement | Status in Deep Learning |
|---|---|---|
| DPI holds for all layers | I(X;Z_l) <= I(X;Z_{l-1}) | Always true (guaranteed by Markov property) |
| Compression phase exists | I(X;Z) decreases during training | Depends on activation and MI estimator |
| Invertible layers preserve MI | I(X;Z) = I(X;Y) for bijective Z=f(Y) | Exactly true by DPI equality condition |
| Residuals preserve info | I(X;Z) approx I(X;Y) with skip connections | Approximately true empirically |
| VIB improves generalisation | Adding I(Z;X) penalty improves test acc | Empirically supported in some settings |
| IB explains generalisation | Compression = good generalisation | Disputed, not universally supported |

---

## Key Takeaways

- DPI: if X->Y->Z is a Markov chain then I(X;Z) <= I(X;Y) — processing can never create new information about X.
- Every neural network layer forms the Markov chain X->layer_{l-1}->layer_l, so MI with the input is monotonically non-increasing through the forward pass.
- Invertible functions (bijections) achieve equality: I(X;Z) = I(X;Y). Normalising flows and whitening are examples.
- The information bottleneck objective min[I(Z;X) - beta*I(Z;Y)] trades compression of X against retention of label Y information.
- Apparent IB compression in deterministic ReLU networks is a binning artefact; genuine compression requires stochastic layers.
- Post-processing (calibration, ensembling) cannot increase MI between predictions and true labels — better training always dominates.
- Differential privacy noise addition provably reduces MI with the sensitive input, bounded by the Gaussian channel capacity formula.
