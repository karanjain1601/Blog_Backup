---
title: "Naive Bayes — Generative Classifier and Feature Independence"
slug: "naive-bayes"
description: "Derive Naive Bayes as a generative classifier using Bayes' theorem, understand Gaussian/Multinomial/Bernoulli variants, implement Laplace smoothing, and compare against logistic regression on text and small datasets."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmFpdmUgQmF5ZXMgaXMgYSBnZW5lcmF0aXZlIGNsYXNzaWZpZXIgdGhhdCBtb2RlbHMgdGhlIGpvaW50IGRpc3RyaWJ1dGlvbiBwKHgsIHkpID0gcCh5KSDCtyBwKHh8eSksIHRoZW4gYXBwbGllcyBCYXllc1x1MDAyNyB0aGVvcmVtIHRvIGdldCB0aGUgcG9zdGVyaW9yIHAoeXx4KSDiiJ0gcCh5KSDCtyBwKHh8eSkuIFRoZSBcdTAwMjduYWl2ZVx1MDAyNyBhc3N1bXB0aW9uIGlzIHRoYXQgZmVhdHVyZXMgYXJlIGNvbmRpdGlvbmFsbHkgaW5kZXBlbmRlbnQgZ2l2ZW4gdGhlIGNsYXNzOiBwKHh8eSkgPSDOoOG1oiBwKHjhtaJ8eSkuIERlc3BpdGUgYmVpbmcgd3JvbmcgaW4gcHJhY3RpY2UsIHRoaXMgYXNzdW1wdGlvbiBwcm9kdWNlcyBzdXJwcmlzaW5nbHkgY29tcGV0aXRpdmUgY2xhc3NpZmllcnMsIGVzcGVjaWFsbHkgZm9yIHRleHQgY2xhc3NpZmljYXRpb24uIE5haXZlIEJheWVzIHRyYWlucyBpbiBPKG5kKSB0aW1lLCBoYW5kbGVzIG1pc3NpbmcgZmVhdHVyZXMgbmF0dXJhbGx5LCBhbmQgdXBkYXRlcyBpbmNyZW1lbnRhbGx5IOKAlCBtYWtpbmcgaXQgaWRlYWwgZm9yIHN0cmVhbWluZyBkYXRhIGFuZCB2ZXJ5IHNtYWxsIGRhdGFzZXRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJheWVzXHUwMDI3IFRoZW9yZW0gYW5kIHRoZSBHZW5lcmF0aXZlIEZyYW1ld29yayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVXNpbmcgQmF5ZXNcdTAwMjcgdGhlb3JlbTogcCh5PWt8eCkgPSBwKHk9aykgwrcgcCh4fHk9aykgLyBwKHgpLiBTaW5jZSBwKHgpIGlzIHRoZSBzYW1lIGZvciBhbGwgY2xhc3NlcywgY2xhc3NpZmljYXRpb24gcmVkdWNlcyB0byBhcmdtYXhfayBwKHk9aykgwrcgcCh4fHk9aykuIFdpdGggdGhlIG5haXZlIGluZGVwZW5kZW5jZSBhc3N1bXB0aW9uOiBsb2cgcCh5PWt8eCkg4oidIGxvZyBwKHk9aykgKyDOo+G1oiBsb2cgcCh44bWifHk9aykuIEVhY2ggdGVybSBpcyBhIHByaW9yIChjbGFzcyBmcmVxdWVuY3kpIHBsdXMgYSBzdW0gb2YgbG9nLWxpa2VsaWhvb2RzIOKAlCBhIGxpbmVhciBmdW5jdGlvbiBpbiBsb2ctcHJvYmFiaWxpdHkgc3BhY2UuIFRoaXMgbWVhbnMgTmFpdmUgQmF5ZXMgaXMgYSBsaW5lYXIgY2xhc3NpZmllciBpbiBsb2ctc3BhY2UsIHdoaWNoIGlzIHdoeSBpdCBhY2hpZXZlcyBjb21wZXRpdGl2ZSBhY2N1cmFjeSBkZXNwaXRlIHRoZSBuYWl2ZSBhc3N1bXB0aW9uOiBtYW55IHJlYWwtd29ybGQgY2xhc3NpZmljYXRpb24gdGFza3MgYXJlIGFwcHJveGltYXRlbHkgbGluZWFybHkgc2VwYXJhYmxlIGluIGxvZy1mZWF0dXJlIHNwYWNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdhdXNzaWFuLCBNdWx0aW5vbWlhbCwgYW5kIEJlcm5vdWxsaSBWYXJpYW50cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHZhcmlhbnQgb2YgTmFpdmUgQmF5ZXMgaXMgZGV0ZXJtaW5lZCBieSB0aGUgYXNzdW1lZCBkaXN0cmlidXRpb24gb2YgcCh44bWifHk9aykuIEdhdXNzaWFuIE5COiB44bWifHk9ayB+IE4ozrzigpbhtaIsIM+DwrLigpbhtaIpLiBQYXJhbWV0ZXJzIGVzdGltYXRlZCBieSBjbGFzcy1jb25kaXRpb25hbCBtZWFucyBhbmQgdmFyaWFuY2VzLiBVc2VkIGZvciBjb250aW51b3VzIGZlYXR1cmVzLiBNdWx0aW5vbWlhbCBOQjogbW9kZWxzIHdvcmQgY291bnRzOyBwKHjhtaJ8eT1rKSBpcyB0aGUgcHJvYmFiaWxpdHkgb2Ygd29yZCBpIGluIGNsYXNzIGsuIE1vc3QgY29tbW9uIGZvciBkb2N1bWVudCBjbGFzc2lmaWNhdGlvbiB3aXRoIFRGIG9yIGNvdW50IGZlYXR1cmVzLiBCZXJub3VsbGkgTkI6IG1vZGVscyBiaW5hcnkgZmVhdHVyZXMgKHdvcmQgcHJlc2VudC9hYnNlbnQpOyBlYWNoIGRpbWVuc2lvbiBpcyBCZXJub3VsbGkozrjigpbhtaIpLiBDb21wbGVtZW50IE5COiBmaXRzIHBhcmFtZXRlcnMgZm9yIHRoZSBjb21wbGVtZW50IG9mIGVhY2ggY2xhc3Mg4oCUIG1vcmUgbnVtZXJpY2FsbHkgc3RhYmxlIGZvciBpbWJhbGFuY2VkIHRleHQgZGF0YXNldHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBsb2FkX2lyaXNcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcbmZyb20gc2tsZWFybi5tZXRyaWNzIGltcG9ydCBhY2N1cmFjeV9zY29yZVxuZnJvbSBza2xlYXJuLm5haXZlX2JheWVzIGltcG9ydCBHYXVzc2lhbk5CXG5cbmNsYXNzIEdhdXNzaWFuTmFpdmVCYXllczpcbiAgICBkZWYgZml0KHNlbGYsIFgsIHkpOlxuICAgICAgICBzZWxmLmNsYXNzZXNfID0gbnAudW5pcXVlKHkpXG4gICAgICAgIHNlbGYucHJpb3JzXyA9IHt9XG4gICAgICAgIHNlbGYubWVhbnNfICA9IHt9XG4gICAgICAgIHNlbGYudmFyc18gICA9IHt9XG4gICAgICAgIGZvciBjIGluIHNlbGYuY2xhc3Nlc186XG4gICAgICAgICAgICBYYyA9IFhbeSA9PSBjXVxuICAgICAgICAgICAgc2VsZi5wcmlvcnNfW2NdID0gbGVuKFhjKSAvIGxlbihYKVxuICAgICAgICAgICAgc2VsZi5tZWFuc19bY10gID0gWGMubWVhbihheGlzPTApXG4gICAgICAgICAgICBzZWxmLnZhcnNfW2NdICAgPSBYYy52YXIoYXhpcz0wKSArIDFlLTlcbiAgICAgICAgcmV0dXJuIHNlbGZcblxuICAgIGRlZiBfbG9nX2xpa2VsaWhvb2Qoc2VsZiwgeCwgYyk6XG4gICAgICAgIG11LCB2YXIgPSBzZWxmLm1lYW5zX1tjXSwgc2VsZi52YXJzX1tjXVxuICAgICAgICByZXR1cm4gLTAuNSAqIG5wLnN1bShucC5sb2coMiAqIG5wLnBpICogdmFyKSArICh4IC0gbXUpKioyIC8gdmFyKVxuXG4gICAgZGVmIHByZWRpY3Qoc2VsZiwgWCk6XG4gICAgICAgIHByZWRzID0gW11cbiAgICAgICAgZm9yIHggaW4gWDpcbiAgICAgICAgICAgIHNjb3JlcyA9IHtjOiBucC5sb2coc2VsZi5wcmlvcnNfW2NdKSArIHNlbGYuX2xvZ19saWtlbGlob29kKHgsIGMpXG4gICAgICAgICAgICAgICAgICAgICAgZm9yIGMgaW4gc2VsZi5jbGFzc2VzX31cbiAgICAgICAgICAgIHByZWRzLmFwcGVuZChtYXgoc2NvcmVzLCBrZXk9c2NvcmVzLmdldCkpXG4gICAgICAgIHJldHVybiBucC5hcnJheShwcmVkcylcblxuWCwgeSA9IGxvYWRfaXJpcyhyZXR1cm5fWF95PVRydWUpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4zLCByYW5kb21fc3RhdGU9NDIpXG5nbmIgPSBHYXVzc2lhbk5haXZlQmF5ZXMoKS5maXQoWF90ciwgeV90cilcbnNrX2duYiA9IEdhdXNzaWFuTkIoKS5maXQoWF90ciwgeV90cilcbnByaW50KGZcdTAwMjdHYXVzc2lhbiBOQiBzY3JhdGNoOiB7YWNjdXJhY3lfc2NvcmUoeV90ZSwgZ25iLnByZWRpY3QoWF90ZSkpOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3R2F1c3NpYW4gTkIgc2tsZWFybjoge2FjY3VyYWN5X3Njb3JlKHlfdGUsIHNrX2duYi5wcmVkaWN0KFhfdGUpKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxhcGxhY2UgU21vb3RoaW5nIOKAlCBIYW5kbGluZyBaZXJvIFByb2JhYmlsaXRpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldpdGggTXVsdGlub21pYWwgb3IgQmVybm91bGxpIE5CLCBhIHdvcmQgdGhhdCBuZXZlciBhcHBlYXJzIGluIGEgY2xhc3MgaW4gdGhlIHRyYWluaW5nIGRhdGEgZ2V0cyBwKHdvcmR8Y2xhc3MpID0gMC4gU2luY2UgdGhlIGpvaW50IHByb2JhYmlsaXR5IGlzIGEgcHJvZHVjdCwgYSBzaW5nbGUgemVybyBwcm9iYWJpbGl0eSBtYWtlcyB0aGUgZW50aXJlIGNsYXNzIHByb2JhYmlsaXR5IHplcm8gcmVnYXJkbGVzcyBvZiBhbGwgb3RoZXIgZmVhdHVyZXMg4oCUIGEgY2F0YXN0cm9waGljIGZhaWx1cmUgY2FsbGVkIHRoZSB6ZXJvLWZyZXF1ZW5jeSBwcm9ibGVtLiBMYXBsYWNlIHNtb290aGluZyAoYWRkLWsgc21vb3RoaW5nKSBhZGRzIGEgc21hbGwgY291bnQgzrEgKHR5cGljYWxseSDOsT0xKSB0byBldmVyeSB3b3JkLWNsYXNzIGNvdW50OiBwKHjhtaJ8eT1rKSA9IChjb3VudCh44bWiLCBrKSArIM6xKSAvIChjb3VudChrKSArIM6xwrdWKSB3aGVyZSBWIGlzIHRoZSB2b2NhYnVsYXJ5IHNpemUuIFRoaXMgZ3VhcmFudGVlcyBubyB6ZXJvIHByb2JhYmlsaXRpZXMgd2hpbGUgYmFyZWx5IGFmZmVjdGluZyBlc3RpbWF0ZXMgZm9yIGZyZXF1ZW50IHdvcmRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBEZW1vbnN0cmF0ZSBjYXRhc3Ryb3BoaWMgemVybyBwcm9iYWJpbGl0eSB3aXRob3V0IHNtb290aGluZ1xudm9jYWIgPSBbXHUwMDI3Z29vZFx1MDAyNywgXHUwMDI3Z3JlYXRcdTAwMjcsIFx1MDAyN2JhZFx1MDAyNywgXHUwMDI3dGVycmlibGVcdTAwMjcsIFx1MDAyN25vdmVsX3dvcmRcdTAwMjddXG5jbGFzc19jb3VudHMgPSB7XHUwMDI3cG9zXHUwMDI3OiB7XHUwMDI3Z29vZFx1MDAyNzogMTAsIFx1MDAyN2dyZWF0XHUwMDI3OiA4LCBcdTAwMjdiYWRcdTAwMjc6IDF9LFxuICAgICAgICAgICAgICAgIFx1MDAyN25lZ1x1MDAyNzoge1x1MDAyN2JhZFx1MDAyNzogMTIsIFx1MDAyN3RlcnJpYmxlXHUwMDI3OiA5LCBcdTAwMjdnb29kXHUwMDI3OiAyfX1cbmNsYXNzX3RvdGFscyA9IHtcdTAwMjdwb3NcdTAwMjc6IDMwLCBcdTAwMjduZWdcdTAwMjc6IDQwfVxucHJpb3JzID0ge1x1MDAyN3Bvc1x1MDAyNzogMC41LCBcdTAwMjduZWdcdTAwMjc6IDAuNX1cblYgPSBsZW4odm9jYWIpXG5cbmRlZiBwcmVkaWN0X25iKHRleHRfd29yZHMsIGFscGhhPTApOlxuICAgIGxvZ19zY29yZXMgPSB7fVxuICAgIGZvciBjIGluIFtcdTAwMjdwb3NcdTAwMjcsIFx1MDAyN25lZ1x1MDAyN106XG4gICAgICAgIGxvZ19wID0gbnAubG9nKHByaW9yc1tjXSlcbiAgICAgICAgZm9yIHdvcmQgaW4gdGV4dF93b3JkczpcbiAgICAgICAgICAgIGNvdW50ID0gY2xhc3NfY291bnRzW2NdLmdldCh3b3JkLCAwKVxuICAgICAgICAgICAgdG90YWwgPSBjbGFzc190b3RhbHNbY11cbiAgICAgICAgICAgIHBfd29yZCA9IChjb3VudCArIGFscGhhKSAvICh0b3RhbCArIGFscGhhICogVilcbiAgICAgICAgICAgICMgV2l0aG91dCBzbW9vdGhpbmcsIHBfd29yZD0wIGNhdXNlcyBsb2coMCkgPSAtaW5mXG4gICAgICAgICAgICBsb2dfcCArPSBucC5sb2cocF93b3JkKSBpZiBwX3dvcmQgXHUwMDNlIDAgZWxzZSBmbG9hdChcdTAwMjctaW5mXHUwMDI3KVxuICAgICAgICBsb2dfc2NvcmVzW2NdID0gbG9nX3BcbiAgICByZXR1cm4gbG9nX3Njb3Jlc1xuXG50ZXN0X2RvYyA9IFtcdTAwMjdnb29kXHUwMDI3LCBcdTAwMjdub3ZlbF93b3JkXHUwMDI3XSAgIyBub3ZlbF93b3JkIGFic2VudCBmcm9tIHRyYWluaW5nXG5wcmludChcdTAwMjdXaXRob3V0IHNtb290aGluZyAoYWxwaGE9MCk6XHUwMDI3KVxuZm9yIGMsIHNjb3JlIGluIHByZWRpY3RfbmIodGVzdF9kb2MsIGFscGhhPTApLml0ZW1zKCk6XG4gICAgcHJpbnQoZlx1MDAyNyAge2N9OiBsb2cgcCA9IHtzY29yZX1cdTAwMjcpXG5wcmludChcdTAwMjdcXG5XaXRoIExhcGxhY2Ugc21vb3RoaW5nIChhbHBoYT0xKTpcdTAwMjcpXG5mb3IgYywgc2NvcmUgaW4gcHJlZGljdF9uYih0ZXN0X2RvYywgYWxwaGE9MSkuaXRlbXMoKTpcbiAgICBwcmludChmXHUwMDI3ICB7Y306IGxvZyBwID0ge3Njb3JlOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBmZXRjaF8yMG5ld3Nncm91cHNcbmZyb20gc2tsZWFybi5mZWF0dXJlX2V4dHJhY3Rpb24udGV4dCBpbXBvcnQgQ291bnRWZWN0b3JpemVyXG5mcm9tIHNrbGVhcm4ubmFpdmVfYmF5ZXMgaW1wb3J0IE11bHRpbm9taWFsTkIsIENvbXBsZW1lbnROQlxuZnJvbSBza2xlYXJuLnBpcGVsaW5lIGltcG9ydCBQaXBlbGluZVxuZnJvbSBza2xlYXJuLm1ldHJpY3MgaW1wb3J0IGFjY3VyYWN5X3Njb3JlXG5cbmNhdHMgPSBbXHUwMDI3c2NpLnNwYWNlXHUwMDI3LCBcdTAwMjdyZWMuc3BvcnQuaG9ja2V5XHUwMDI3LCBcdTAwMjd0YWxrLnBvbGl0aWNzLmd1bnNcdTAwMjcsIFx1MDAyN2NvbXAuZ3JhcGhpY3NcdTAwMjddXG50cmFpbiA9IGZldGNoXzIwbmV3c2dyb3VwcyhzdWJzZXQ9XHUwMDI3dHJhaW5cdTAwMjcsIGNhdGVnb3JpZXM9Y2F0cyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICByZW1vdmU9KFx1MDAyN2hlYWRlcnNcdTAwMjcsIFx1MDAyN2Zvb3RlcnNcdTAwMjcsIFx1MDAyN3F1b3Rlc1x1MDAyNykpXG50ZXN0ICA9IGZldGNoXzIwbmV3c2dyb3VwcyhzdWJzZXQ9XHUwMDI3dGVzdFx1MDAyNywgIGNhdGVnb3JpZXM9Y2F0cyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICByZW1vdmU9KFx1MDAyN2hlYWRlcnNcdTAwMjcsIFx1MDAyN2Zvb3RlcnNcdTAwMjcsIFx1MDAyN3F1b3Rlc1x1MDAyNykpXG5cbmZvciBuYW1lLCBjbGYgaW4gWyhcdTAwMjdNdWx0aW5vbWlhbE5CXHUwMDI3LCBNdWx0aW5vbWlhbE5CKGFscGhhPTEuMCkpLFxuICAgICAgICAgICAgICAgICAgIChcdTAwMjdDb21wbGVtZW50TkJcdTAwMjcsICBDb21wbGVtZW50TkIoYWxwaGE9MS4wKSldOlxuICAgIHBpcGUgPSBQaXBlbGluZShbKFx1MDAyN3ZlY1x1MDAyNywgQ291bnRWZWN0b3JpemVyKG1heF9mZWF0dXJlcz0xMDAwMCkpLCAoXHUwMDI3Y2xmXHUwMDI3LCBjbGYpXSlcbiAgICBwaXBlLmZpdCh0cmFpbi5kYXRhLCB0cmFpbi50YXJnZXQpXG4gICAgcHJlZHMgPSBwaXBlLnByZWRpY3QodGVzdC5kYXRhKVxuICAgIGFjYyA9IGFjY3VyYWN5X3Njb3JlKHRlc3QudGFyZ2V0LCBwcmVkcylcbiAgICBwcmludChmXHUwMDI3e25hbWV9OiBhY2N1cmFjeT17YWNjOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5mcm9tIHNrbGVhcm4ubmFpdmVfYmF5ZXMgaW1wb3J0IEdhdXNzaWFuTkJcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExvZ2lzdGljUmVncmVzc2lvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgY3Jvc3NfdmFsX3Njb3JlXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuWF9mdWxsLCB5X2Z1bGwgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKG5fc2FtcGxlcz01MDAwLCBuX2ZlYXR1cmVzPTIwLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX2luZm9ybWF0aXZlPTEwLCBuX3JlZHVuZGFudD01LCByYW5kb21fc3RhdGU9NDIpXG5cbnByaW50KGZcdTAwMjd7XHUwMDI3bl90cmFpblx1MDAyNzpcdTAwM2U4fSB7XHUwMDI3TkIgYWNjXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3TFIgYWNjXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3V2lubmVyXHUwMDI3Olx1MDAzZTh9XHUwMDI3KVxuZm9yIG5fdHJhaW4gaW4gWzMwLCA2MCwgMTAwLCAyMDAsIDUwMCwgMTAwMCwgMjAwMCwgNTAwMF06XG4gICAgWF9zdWIsIHlfc3ViID0gWF9mdWxsWzpuX3RyYWluXSwgeV9mdWxsWzpuX3RyYWluXVxuICAgIG5iX3Njb3JlID0gY3Jvc3NfdmFsX3Njb3JlKEdhdXNzaWFuTkIoKSwgWF9zdWIsIHlfc3ViLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjdj01LCBzY29yaW5nPVx1MDAyN2FjY3VyYWN5XHUwMDI3KS5tZWFuKClcbiAgICBscl9zY29yZSA9IGNyb3NzX3ZhbF9zY29yZShMb2dpc3RpY1JlZ3Jlc3Npb24obWF4X2l0ZXI9NTAwKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgWF9zdWIsIHlfc3ViLCBjdj01LCBzY29yaW5nPVx1MDAyN2FjY3VyYWN5XHUwMDI3KS5tZWFuKClcbiAgICB3aW5uZXIgPSBcdTAwMjdOQlx1MDAyNyBpZiBuYl9zY29yZSBcdTAwM2UgbHJfc2NvcmUgZWxzZSBcdTAwMjdMUlx1MDAyN1xuICAgIHByaW50KGZcdTAwMjd7bl90cmFpbjpcdTAwM2U4fSB7bmJfc2NvcmU6XHUwMDNlMTAuNGZ9IHtscl9zY29yZTpcdTAwM2UxMC40Zn0ge3dpbm5lcjpcdTAwM2U4fVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiV2hlbiBOYWl2ZSBCYXllcyBXaW5zIiwiY29udGVudCI6Ik5haXZlIEJheWVzIG91dHBlcmZvcm1zIGxvZ2lzdGljIHJlZ3Jlc3Npb24gd2hlbiB0cmFpbmluZyBkYXRhIGlzIHZlcnkgc21hbGwgKG4gXHUwMDNjIDEwMCksIGJlY2F1c2UgYXMgYSBnZW5lcmF0aXZlIG1vZGVsIGl0IG1ha2VzIHN0cm9uZ2VyIGFzc3VtcHRpb25zIGFuZCB0aGVyZWZvcmUgbmVlZHMgZmV3ZXIgZXhhbXBsZXMgdG8gZXN0aW1hdGUgcGFyYW1ldGVycy4gQXMgbiBncm93cywgZGlzY3JpbWluYXRpdmUgbW9kZWxzIGxpa2UgbG9naXN0aWMgcmVncmVzc2lvbiB0aGF0IG1ha2UgZmV3ZXIgYXNzdW1wdGlvbnMgY2F0Y2ggdXAgYW5kIGV2ZW50dWFsbHkgd2luLiBUaGlzIGlzIHRoZSBcdTAwMjdnZW5lcmF0aXZlIHZzIGRpc2NyaW1pbmF0aXZlXHUwMDI3IGFzeW1wdG90aWMgcmVzdWx0IG9mIE5nIGFuZCBKb3JkYW4gKDIwMDIpOiBOQiB3aW5zIGZhc3QsIExSIHdpbnMgYmlnLiBGb3Igc3RyZWFtaW5nIG9yIG9ubGluZSBsZWFybmluZywgdXNlIHBhcnRpYWxfZml0IGZvciBpbmNyZW1lbnRhbCB1cGRhdGVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxvZy1Qcm9iYWJpbGl0eSBhbmQgTnVtZXJpY2FsIFN0YWJpbGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ29tcHV0aW5nIHAoeT1rfHgpID0gcCh5PWspIMK3IM6g4bWiIHAoeOG1onx5PWspIGRpcmVjdGx5IGxlYWRzIHRvIGZsb2F0aW5nLXBvaW50IHVuZGVyZmxvdyBmb3IgZXZlbiBtb2RlcmF0ZS1sZW5ndGggZG9jdW1lbnRzIOKAlCB0aGUgcHJvZHVjdCBvZiBtYW55IHByb2JhYmlsaXRpZXMgaW4gWzAsMV0gdW5kZXJmbG93cyB0byB6ZXJvLiBUaGUgc3RhbmRhcmQgZml4IGlzIHRvIHdvcmsgaW4gbG9nLXNwYWNlOiBsb2cgcCh5PWt8eCkg4oidIGxvZyBwKHk9aykgKyDOo+G1oiBsb2cgcCh44bWifHk9aykuIFRoZW4gY29udmVydCBiYWNrIHVzaW5nIHRoZSBsb2ctc3VtLWV4cCB0cmljazogbG9nIM6j4oKWIGV4cChz4oKWKSA9IG1heChz4oKWKSArIGxvZyDOo+KCliBleHAoc+KCliAtIG1heChz4oKWKSkuIHNrbGVhcm5cdTAwMjdzIE5haXZlIEJheWVzIGltcGxlbWVudGF0aW9ucyB1c2UgbG9nLXByb2JhYmlsaXRpZXMgaW50ZXJuYWxseSB2aWEgcHJlZGljdF9sb2dfcHJvYmEg4oCUIGFsd2F5cyB1c2UgdGhpcyB3aGVuIGltcGxlbWVudGluZyBmcm9tIHNjcmF0Y2guIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT25saW5lIExlYXJuaW5nIHdpdGggTmFpdmUgQmF5ZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik5haXZlIEJheWVzIHN1cHBvcnRzIHRydWUgb25saW5lIGxlYXJuaW5nIHZpYSBwYXJ0aWFsX2ZpdCwgd2hpY2ggdXBkYXRlcyB0aGUgc3VmZmljaWVudCBzdGF0aXN0aWNzIChjbGFzcyBjb3VudHMsIGZlYXR1cmUgbWVhbnMvdmFyaWFuY2VzKSBpbmNyZW1lbnRhbGx5IHdpdGhvdXQgc3RvcmluZyBwYXN0IGRhdGEuIEVhY2ggdXBkYXRlIGNvc3RzIE8ocCkg4oCUIGxpbmVhciBpbiB0aGUgbnVtYmVyIG9mIGZlYXR1cmVzLiBUaGlzIG1ha2VzIE5haXZlIEJheWVzIGlkZWFsIGZvciBzdHJlYW1pbmcgdGV4dCBjbGFzc2lmaWNhdGlvbiwgc3BhbSBmaWx0ZXJpbmcgd2l0aCBldm9sdmluZyB2b2NhYnVsYXJ5LCBhbmQgYW55IHNldHRpbmcgd2hlcmUgdGhlIGRhdGEgZGlzdHJpYnV0aW9uIHNoaWZ0cyBvdmVyIHRpbWUgYW5kIHRoZSBtb2RlbCBuZWVkcyBjb250aW51b3VzIHVwZGF0aW5nLiBJbiBjb250cmFzdCwgbG9naXN0aWMgcmVncmVzc2lvbiByZXF1aXJlcyBzdG9yaW5nIHRoZSBmdWxsIGdyYWRpZW50IGhpc3Rvcnkgb3IgU0dEIHVwZGF0ZXMsIHdoaWNoIGFyZSBub2lzaWVyIGFuZCByZXF1aXJlIGNhcmVmdWwgbGVhcm5pbmcgcmF0ZSB0dW5pbmcuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlZhcmlhbnQiLCJGZWF0dXJlIFR5cGUiLCJMaWtlbGlob29kIiwiUHJpbWFyeSBVc2UgQ2FzZSIsIktleSBBc3N1bXB0aW9uIl0sInJvd3MiOltbIkdhdXNzaWFuIE5CIiwiQ29udGludW91cyIsIk4ozrzigpbhtaIsIM+DwrLigpbhtaIpIiwiTnVtZXJpY2FsIHRhYnVsYXIgZGF0YSIsIkZlYXR1cmVzIGFyZSBHYXVzc2lhbiB3aXRoaW4gZWFjaCBjbGFzcyJdLFsiTXVsdGlub21pYWwgTkIiLCJJbnRlZ2VyIGNvdW50cyIsIk11bHRpbm9taWFsKM644oKWKSIsIlRleHQgKHdvcmQgY291bnRzKSwgZG9jdW1lbnQgY2xhc3NpZmljYXRpb24iLCJXb3JkIGNvdW50cyBhcmUgY29uZGl0aW9uYWxseSBpbmRlcGVuZGVudCJdLFsiQmVybm91bGxpIE5CIiwiQmluYXJ5IDAvMSIsIkJlcm5vdWxsaSjOuOKCluG1oikiLCJTaG9ydCB0ZXh0cywgYmluYXJ5IGZlYXR1cmUgYmFncyIsIkFic2VuY2Ugb2YgYSBmZWF0dXJlIGlzIGFsc28gaW5mb3JtYXRpdmUiXSxbIkNvbXBsZW1lbnQgTkIiLCJJbnRlZ2VyIGNvdW50cyIsIkNvbXBsZW1lbnQgY2xhc3MgbXVsdGlub21pYWwiLCJJbWJhbGFuY2VkIHRleHQgY2xhc3NpZmljYXRpb24iLCJNb3JlIHN0YWJsZSB0aGFuIE1OQiBmb3Igc2tld2VkIGNsYXNzZXMiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQWx3YXlzIHVzZSBsb2ctcHJvYmFiaWxpdGllcyB0byBhdm9pZCB1bmRlcmZsb3cgd2hlbiBtdWx0aXBseWluZyBtYW55IHNtYWxsIHByb2JhYmlsaXRpZXMuIiwiQXBwbHkgTGFwbGFjZSBzbW9vdGhpbmcgKGFscGhhPTEpIGZvciBNdWx0aW5vbWlhbCBhbmQgQmVybm91bGxpIE5CIHRvIHByZXZlbnQgemVybyBwcm9iYWJpbGl0aWVzLiIsIkZvciB0ZXh0IHdpdGggVEYtSURGIGZlYXR1cmVzIChmbG9hdGluZyBwb2ludCksIHVzZSBHYXVzc2lhbiBOQiBvciBjb21wbGVtZW50IE5CLCBub3QgTXVsdGlub21pYWwgTkIuIiwiVXNlIHBhcnRpYWxfZml0IGZvciBvbmxpbmUvc3RyZWFtaW5nIGxlYXJuaW5nIOKAlCBOYWl2ZSBCYXllcyBpcyBvbmUgb2YgdGhlIGZldyBjbGFzc2lmaWVycyB0aGF0IHVwZGF0ZXMgdHJ1bHkgaW5jcmVtZW50YWxseS4iLCJOQiBpcyB3ZWxsLWNhbGlicmF0ZWQgd2hlbiB0aGUgaW5kZXBlbmRlbmNlIGFzc3VtcHRpb24gaXMgYXBwcm94aW1hdGVseSBjb3JyZWN0OyBjaGVjayB3aXRoIGNhbGlicmF0aW9uIGN1cnZlcy4iLCJGb3IgaW1iYWxhbmNlZCBjbGFzc2VzLCB1c2UgQ29tcGxlbWVudE5CIHdoaWNoIGlzIG1vcmUgcm9idXN0IHRvIGNsYXNzIHNrZXcgdGhhbiBNdWx0aW5vbWlhbE5CLiJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoeSB0aGUgTmFpdmUgQXNzdW1wdGlvbiBPZnRlbiBXb3JrcyIsImNvbnRlbnQiOiJEZXNwaXRlIGZlYXR1cmUgaW5kZXBlbmRlbmNlIHJhcmVseSBob2xkaW5nIGluIHByYWN0aWNlLCBOYWl2ZSBCYXllcyBvZnRlbiBwZXJmb3JtcyB3ZWxsLiBUaGUga2V5IGluc2lnaHQgKERvbWluZ29zIGFuZCBQYXp6YW5pIDE5OTcpOiBjbGFzc2lmaWNhdGlvbiBhY2N1cmFjeSBvbmx5IHJlcXVpcmVzIHRoYXQgdGhlIHJhbmtpbmcgb2YgY2xhc3MgcG9zdGVyaW9ycyBpcyBjb3JyZWN0LCBub3QgdGhhdCB0aGUgcHJvYmFiaWxpdGllcyBhcmUgYWNjdXJhdGUuIEV2ZW4gaWYgcCh4fHkpIGlzIHNldmVyZWx5IHdyb25nIGR1ZSB0byBkZXBlbmRlbmNlLCB0aGUgYXJnbWF4IGNsYXNzIG1heSBzdGlsbCBiZSBjb3JyZWN0LiBUaGlzIGlzIHdoeSBOQiBpcyBzdXJwcmlzaW5nbHkgcm9idXN0IHRvIHZpb2xhdGVkIGluZGVwZW5kZW5jZSBhc3N1bXB0aW9ucyBpbiBjbGFzc2lmaWNhdGlvbiwgdGhvdWdoIG5vdCBmb3IgcHJvYmFiaWxpdHkgY2FsaWJyYXRpb24uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOYWl2ZSBCYXllcyBzaXRzIGF0IG9uZSBleHRyZW1lIG9mIHRoZSBnZW5lcmF0aXZlLWRpc2NyaW1pbmF0aXZlIHNwZWN0cnVtLiBHZW5lcmF0aXZlIG1vZGVscyAoTkIsIExEQSkgbW9kZWwgdGhlIGZ1bGwgam9pbnQgcCh4LHkpLCBhbGxvd2luZyBnZW5lcmF0aW9uIG9mIHN5bnRoZXRpYyBkYXRhIGFuZCBuYXR1cmFsIGhhbmRsaW5nIG9mIG1pc3NpbmcgZmVhdHVyZXMuIERpc2NyaW1pbmF0aXZlIG1vZGVscyAobG9naXN0aWMgcmVncmVzc2lvbiwgU1ZNKSBtb2RlbCBvbmx5IHAoeXx4KSwgd2hpY2ggaXMgc3VmZmljaWVudCBmb3IgY2xhc3NpZmljYXRpb24uIFRoZSB0cmFkZW9mZjogZ2VuZXJhdGl2ZSBtb2RlbHMgY29udmVyZ2UgZmFzdGVyIHdpdGggc21hbGwgZGF0YSAoZmV3ZXIgcGFyYW1ldGVycyB0byBlc3RpbWF0ZSk7IGRpc2NyaW1pbmF0aXZlIG1vZGVscyBjb252ZXJnZSB0byBsb3dlciBhc3ltcHRvdGljIGVycm9yIHdpdGggbGFyZ2UgZGF0YSBiZWNhdXNlIHRoZXkgbWFrZSBmZXdlciBhc3N1bXB0aW9ucy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik11bHRpbm9taWFsIE5haXZlIEJheWVzIHdpdGggY291bnQgZmVhdHVyZXMgaXMgYSBzdHJvbmcgdGV4dCBjbGFzc2lmaWNhdGlvbiBiYXNlbGluZS4gRGVzcGl0ZSBpdHMgc2ltcGxpY2l0eSwgTU5CIGFjaGlldmVzIGNvbXBldGl0aXZlIGFjY3VyYWN5IG9uIDIwIE5ld3Nncm91cHMsIHNwYW0gZmlsdGVyaW5nLCBhbmQgc2VudGltZW50IGJlbmNobWFya3Mg4oCUIG9mdGVuIHdpdGhpbiAyLTMlIG9mIGZpbmUtdHVuZWQgZGVlcCBsZWFybmluZyBtb2RlbHMgZm9yIHNob3J0LXRleHQgY2xhc3NpZmljYXRpb24uIEl0cyBwcm9kdWN0aW9uIGFkdmFudGFnZXM6IE8oMSkgaW5mZXJlbmNlIHBlciBkb2N1bWVudCwgdHJpdmlhbGx5IHBhcmFsbGVsaXNhYmxlLCBpbnRlcnByZXRhYmxlIGZlYXR1cmUgd2VpZ2h0cyAobG9nIHAod29yZHxjbGFzcykgZGlyZWN0bHkgc2hvd3Mgd2hpY2ggd29yZHMgY2hhcmFjdGVyaXNlIGVhY2ggY2xhc3MpLCBhbmQgdHJ1ZSBvbmxpbmUgbGVhcm5pbmcgdmlhIHBhcnRpYWxfZml0LiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Naive Bayes — Generative Classifier and Feature Independence

Naive Bayes is a generative classifier that models the joint distribution p(x, y) = p(y) · p(x|y), then applies Bayes' theorem to get the posterior p(y|x) ∝ p(y) · p(x|y). The 'naive' assumption is that features are conditionally independent given the class: p(x|y) = Πᵢ p(xᵢ|y). Despite being wrong in practice, this assumption produces surprisingly competitive classifiers, especially for text classification. Naive Bayes trains in O(nd) time, handles missing features naturally, and updates incrementally — making it ideal for streaming data and very small datasets.

## Bayes' Theorem and the Generative Framework

Using Bayes' theorem: p(y=k|x) = p(y=k) · p(x|y=k) / p(x). Since p(x) is the same for all classes, classification reduces to argmax_k p(y=k) · p(x|y=k). With the naive independence assumption: log p(y=k|x) ∝ log p(y=k) + Σᵢ log p(xᵢ|y=k). Each term is a prior (class frequency) plus a sum of log-likelihoods — a linear function in log-probability space. This means Naive Bayes is a linear classifier in log-space, which is why it achieves competitive accuracy despite the naive assumption: many real-world classification tasks are approximately linearly separable in log-feature space.

## Gaussian, Multinomial, and Bernoulli Variants

The variant of Naive Bayes is determined by the assumed distribution of p(xᵢ|y=k). Gaussian NB: xᵢ|y=k ~ N(μₖᵢ, σ²ₖᵢ). Parameters estimated by class-conditional means and variances. Used for continuous features. Multinomial NB: models word counts; p(xᵢ|y=k) is the probability of word i in class k. Most common for document classification with TF or count features. Bernoulli NB: models binary features (word present/absent); each dimension is Bernoulli(θₖᵢ). Complement NB: fits parameters for the complement of each class — more numerically stable for imbalanced text datasets.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

class GaussianNaiveBayes:
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.priors_ = {}
        self.means_  = {}
        self.vars_   = {}
        for c in self.classes_:
            Xc = X[y == c]
            self.priors_[c] = len(Xc) / len(X)
            self.means_[c]  = Xc.mean(axis=0)
            self.vars_[c]   = Xc.var(axis=0) + 1e-9
        return self

    def _log_likelihood(self, x, c):
        mu, var = self.means_[c], self.vars_[c]
        return -0.5 * np.sum(np.log(2 * np.pi * var) + (x - mu)**2 / var)

    def predict(self, X):
        preds = []
        for x in X:
            scores = {c: np.log(self.priors_[c]) + self._log_likelihood(x, c)
                      for c in self.classes_}
            preds.append(max(scores, key=scores.get))
        return np.array(preds)

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
gnb = GaussianNaiveBayes().fit(X_tr, y_tr)
sk_gnb = GaussianNB().fit(X_tr, y_tr)
print(f'Gaussian NB scratch: {accuracy_score(y_te, gnb.predict(X_te)):.4f}')
print(f'Gaussian NB sklearn: {accuracy_score(y_te, sk_gnb.predict(X_te)):.4f}')
```

## Laplace Smoothing — Handling Zero Probabilities

With Multinomial or Bernoulli NB, a word that never appears in a class in the training data gets p(word|class) = 0. Since the joint probability is a product, a single zero probability makes the entire class probability zero regardless of all other features — a catastrophic failure called the zero-frequency problem. Laplace smoothing (add-k smoothing) adds a small count α (typically α=1) to every word-class count: p(xᵢ|y=k) = (count(xᵢ, k) + α) / (count(k) + α·V) where V is the vocabulary size. This guarantees no zero probabilities while barely affecting estimates for frequent words.

```python
import numpy as np

# Demonstrate catastrophic zero probability without smoothing
vocab = ['good', 'great', 'bad', 'terrible', 'novel_word']
class_counts = {'pos': {'good': 10, 'great': 8, 'bad': 1},
                'neg': {'bad': 12, 'terrible': 9, 'good': 2}}
class_totals = {'pos': 30, 'neg': 40}
priors = {'pos': 0.5, 'neg': 0.5}
V = len(vocab)

def predict_nb(text_words, alpha=0):
    log_scores = {}
    for c in ['pos', 'neg']:
        log_p = np.log(priors[c])
        for word in text_words:
            count = class_counts[c].get(word, 0)
            total = class_totals[c]
            p_word = (count + alpha) / (total + alpha * V)
            # Without smoothing, p_word=0 causes log(0) = -inf
            log_p += np.log(p_word) if p_word > 0 else float('-inf')
        log_scores[c] = log_p
    return log_scores

test_doc = ['good', 'novel_word']  # novel_word absent from training
print('Without smoothing (alpha=0):')
for c, score in predict_nb(test_doc, alpha=0).items():
    print(f'  {c}: log p = {score}')
print('\nWith Laplace smoothing (alpha=1):')
for c, score in predict_nb(test_doc, alpha=1).items():
    print(f'  {c}: log p = {score:.4f}')
```

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

cats = ['sci.space', 'rec.sport.hockey', 'talk.politics.guns', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=cats,
                            remove=('headers', 'footers', 'quotes'))
test  = fetch_20newsgroups(subset='test',  categories=cats,
                            remove=('headers', 'footers', 'quotes'))

for name, clf in [('MultinomialNB', MultinomialNB(alpha=1.0)),
                   ('ComplementNB',  ComplementNB(alpha=1.0))]:
    pipe = Pipeline([('vec', CountVectorizer(max_features=10000)), ('clf', clf)])
    pipe.fit(train.data, train.target)
    preds = pipe.predict(test.data)
    acc = accuracy_score(test.target, preds)
    print(f'{name}: accuracy={acc:.4f}')
```

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

np.random.seed(42)
X_full, y_full = make_classification(n_samples=5000, n_features=20,
                                      n_informative=10, n_redundant=5, random_state=42)

print(f'{'n_train':>8} {'NB acc':>10} {'LR acc':>10} {'Winner':>8}')
for n_train in [30, 60, 100, 200, 500, 1000, 2000, 5000]:
    X_sub, y_sub = X_full[:n_train], y_full[:n_train]
    nb_score = cross_val_score(GaussianNB(), X_sub, y_sub,
                                cv=5, scoring='accuracy').mean()
    lr_score = cross_val_score(LogisticRegression(max_iter=500),
                                X_sub, y_sub, cv=5, scoring='accuracy').mean()
    winner = 'NB' if nb_score > lr_score else 'LR'
    print(f'{n_train:>8} {nb_score:>10.4f} {lr_score:>10.4f} {winner:>8}')
```

> **When Naive Bayes Wins**: Naive Bayes outperforms logistic regression when training data is very small (n < 100), because as a generative model it makes stronger assumptions and therefore needs fewer examples to estimate parameters. As n grows, discriminative models like logistic regression that make fewer assumptions catch up and eventually win. This is the 'generative vs discriminative' asymptotic result of Ng and Jordan (2002): NB wins fast, LR wins big. For streaming or online learning, use partial_fit for incremental updates.

## Log-Probability and Numerical Stability

Computing p(y=k|x) = p(y=k) · Πᵢ p(xᵢ|y=k) directly leads to floating-point underflow for even moderate-length documents — the product of many probabilities in [0,1] underflows to zero. The standard fix is to work in log-space: log p(y=k|x) ∝ log p(y=k) + Σᵢ log p(xᵢ|y=k). Then convert back using the log-sum-exp trick: log Σₖ exp(sₖ) = max(sₖ) + log Σₖ exp(sₖ - max(sₖ)). sklearn's Naive Bayes implementations use log-probabilities internally via predict_log_proba — always use this when implementing from scratch.

## Online Learning with Naive Bayes

Naive Bayes supports true online learning via partial_fit, which updates the sufficient statistics (class counts, feature means/variances) incrementally without storing past data. Each update costs O(p) — linear in the number of features. This makes Naive Bayes ideal for streaming text classification, spam filtering with evolving vocabulary, and any setting where the data distribution shifts over time and the model needs continuous updating. In contrast, logistic regression requires storing the full gradient history or SGD updates, which are noisier and require careful learning rate tuning.

| Variant | Feature Type | Likelihood | Primary Use Case | Key Assumption |
| --- | --- | --- | --- | --- |
| Gaussian NB | Continuous | N(μₖᵢ, σ²ₖᵢ) | Numerical tabular data | Features are Gaussian within each class |
| Multinomial NB | Integer counts | Multinomial(θₖ) | Text (word counts), document classification | Word counts are conditionally independent |
| Bernoulli NB | Binary 0/1 | Bernoulli(θₖᵢ) | Short texts, binary feature bags | Absence of a feature is also informative |
| Complement NB | Integer counts | Complement class multinomial | Imbalanced text classification | More stable than MNB for skewed classes |

- Always use log-probabilities to avoid underflow when multiplying many small probabilities.
- Apply Laplace smoothing (alpha=1) for Multinomial and Bernoulli NB to prevent zero probabilities.
- For text with TF-IDF features (floating point), use Gaussian NB or complement NB, not Multinomial NB.
- Use partial_fit for online/streaming learning — Naive Bayes is one of the few classifiers that updates truly incrementally.
- NB is well-calibrated when the independence assumption is approximately correct; check with calibration curves.
- For imbalanced classes, use ComplementNB which is more robust to class skew than MultinomialNB.

> **Why the Naive Assumption Often Works**: Despite feature independence rarely holding in practice, Naive Bayes often performs well. The key insight (Domingos and Pazzani 1997): classification accuracy only requires that the ranking of class posteriors is correct, not that the probabilities are accurate. Even if p(x|y) is severely wrong due to dependence, the argmax class may still be correct. This is why NB is surprisingly robust to violated independence assumptions in classification, though not for probability calibration.

Naive Bayes sits at one extreme of the generative-discriminative spectrum. Generative models (NB, LDA) model the full joint p(x,y), allowing generation of synthetic data and natural handling of missing features. Discriminative models (logistic regression, SVM) model only p(y|x), which is sufficient for classification. The tradeoff: generative models converge faster with small data (fewer parameters to estimate); discriminative models converge to lower asymptotic error with large data because they make fewer assumptions.

Multinomial Naive Bayes with count features is a strong text classification baseline. Despite its simplicity, MNB achieves competitive accuracy on 20 Newsgroups, spam filtering, and sentiment benchmarks — often within 2-3% of fine-tuned deep learning models for short-text classification. Its production advantages: O(1) inference per document, trivially parallelisable, interpretable feature weights (log p(word|class) directly shows which words characterise each class), and true online learning via partial_fit.

---

