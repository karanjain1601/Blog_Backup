---
title: "Soft-Margin SVM and Slack Variables"
slug: "soft-margin-svm"
description: "Extend hard-margin SVM to non-separable data with slack variables, understand hinge loss, the C parameter, dual box constraints, support vector types, and ν-SVM parameterisation."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGhhcmQtbWFyZ2luIFNWTSByZXF1aXJlcyBwZXJmZWN0IGxpbmVhciBzZXBhcmFiaWxpdHksIHdoaWNoIHJlYWwgZGF0YSByYXJlbHkgc2F0aXNmaWVzLiBFdmVuIHdoZW4gc2VwYXJhYmxlLCBhIHNpbmdsZSBvdXRsaWVyIGNhbiBkcmFzdGljYWxseSBzaGlmdCB0aGUgbWF4aW11bS1tYXJnaW4gaHlwZXJwbGFuZS4gU29mdC1tYXJnaW4gU1ZNIGludHJvZHVjZXMgc2xhY2sgdmFyaWFibGVzIM6+4bWiIOKJpSAwIHRoYXQgYWxsb3cgcG9pbnRzIHRvIHZpb2xhdGUgdGhlIG1hcmdpbiBvciBiZSBtaXNjbGFzc2lmaWVkLCBwZW5hbGlzaW5nIHZpb2xhdGlvbnMgaW4gcHJvcG9ydGlvbiB0byBDLiBUaGlzIG1ha2VzIHRoZSBTVk0gcm9idXN0IHRvIG5vaXNlIGFuZCBhcHBsaWNhYmxlIHRvIGFueSBkYXRhc2V0LCBhdCB0aGUgY29zdCBvZiBhIG1vZGVsLXNlbGVjdGlvbiBjaG9pY2UgZm9yIEMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IEhhcmQtTWFyZ2luIEZhaWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIYXJkLW1hcmdpbiBTVk0gZmFpbHMgaW4gdHdvIHNjZW5hcmlvczogKDEpIHRoZSBkYXRhIGlzIG5vdCBsaW5lYXJseSBzZXBhcmFibGUg4oCUIG5vIGh5cGVycGxhbmUgYWNoaWV2ZXMgemVybyB0cmFpbmluZyBlcnJvcjsgKDIpIG9uZSBvciBhIGZldyBvdXRsaWVycyBsaWUgb24gdGhlIHdyb25nIHNpZGUgb2YgdGhlIG5hdHVyYWwgYm91bmRhcnksIGZvcmNpbmcgdGhlIG1hcmdpbiB0byBjb2xsYXBzZSB0b3dhcmQgemVybyB0byBhY2NvbW1vZGF0ZSB0aGVtLiBCb3RoIGNhc2VzIHByb2R1Y2UgYW4gaW5mZWFzaWJsZSBvciBoaWdobHkgdW5zdGFibGUgb3B0aW1pc2F0aW9uIHByb2JsZW0uIFRoZSBzb2Z0LW1hcmdpbiBleHRlbnNpb24gYWxsb3dzIGNvbnRyb2xsZWQgbWlzY2xhc3NpZmljYXRpb24sIGJhbGFuY2luZyBtYXJnaW4gd2lkdGggYWdhaW5zdCB0cmFpbmluZyBlcnJvci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTbGFjayBWYXJpYWJsZXMgYW5kIHRoZSBQcmltYWwifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkludHJvZHVjZSBzbGFjayB2YXJpYWJsZXMgzr7htaIg4omlIDAgZm9yIGVhY2ggdHJhaW5pbmcgcG9pbnQuIFRoZSBzb2Z0LW1hcmdpbiBwcmltYWwgaXM6IG1pbmltaXNlIMK94oCWd+KAlsKyICsgQ8K3zqPhtaLOvuG1oiwgc3ViamVjdCB0byB54bWiKHfhtYB44bWiK2IpIOKJpSAxIOKIkiDOvuG1oiBhbmQgzr7htaIg4omlIDAuIFdoZW4gzr7htaIgPSAwIHRoZSBwb2ludCBpcyBjb3JyZWN0bHkgY2xhc3NpZmllZCBvdXRzaWRlIG9yIG9uIHRoZSBtYXJnaW4uIFdoZW4gMCBcdTAwM2Mgzr7htaIg4omkIDEgdGhlIHBvaW50IGlzIGluc2lkZSB0aGUgbWFyZ2luIChtYXJnaW4gdmlvbGF0b3IpLiBXaGVuIM6+4bWiIFx1MDAzZSAxIHRoZSBwb2ludCBpcyBtaXNjbGFzc2lmaWVkLiBUaGUgcGFyYW1ldGVyIEMgXHUwMDNlIDAgY29udHJvbHMgdGhlIHBlbmFsdHkgZm9yIHZpb2xhdGlvbnM6IGxhcmdlIEMg4oaSIGhhcmQgbWFyZ2luIChmZXcgdmlvbGF0aW9ucyksIHNtYWxsIEMg4oaSIHdpZGUgbWFyZ2luIChtb3JlIHZpb2xhdGlvbnMgdG9sZXJhdGVkKS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJIaW5nZSBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2xhY2sgdmFyaWFibGUgzr7htaIgZXF1YWxzIHRoZSBoaW5nZSBsb3NzOiDOvuG1oiA9IG1heCgwLCAxIOKIkiB54bWiKHfhtYB44bWiK2IpKS4gU3Vic3RpdHV0aW5nLCB0aGUgc29mdC1tYXJnaW4gU1ZNIG1pbmltaXNlcyDCveKAlnfigJbCsiArIEPCt86jIG1heCgwLCAxIOKIkiB54bWiZih44bWiKSkg4oCUIGEgcmVndWxhcmlzZWQgaGluZ2UgbG9zcy4gVGhlIGhpbmdlIGxvc3MgaXMgemVybyBmb3IgY29ycmVjdGx5IGNsYXNzaWZpZWQgcG9pbnRzIG91dHNpZGUgdGhlIG1hcmdpbiAoZnVuY3Rpb25hbCBtYXJnaW4g4omlIDEpIGFuZCBncm93cyBsaW5lYXJseSBmb3IgcG9pbnRzIGluc2lkZSBvciBvbiB0aGUgd3Jvbmcgc2lkZS4gVGhpcyBpcyBjb252ZXggYW5kIHN1Yi1kaWZmZXJlbnRpYWJsZSwgZW5hYmxpbmcgZ3JhZGllbnQvc3ViZ3JhZGllbnQgb3B0aW1pc2F0aW9uIG1ldGhvZHMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJJbnRlcnByZXRpbmcgdGhlIEMgUGFyYW1ldGVyIiwiY29udGVudCI6IkMgYWN0cyBhcyB0aGUgaW52ZXJzZSByZWd1bGFyaXNhdGlvbiBzdHJlbmd0aCAoYW5hbG9nb3VzIHRvIDEvzrsgaW4gUmlkZ2UpLiBMYXJnZSBDOiBtb2RlbCBpcyBwZW5hbGlzZWQgaGVhdmlseSBmb3IgZXJyb3JzIOKGkiBuYXJyb3cgbWFyZ2luLCBsb3cgdHJhaW5pbmcgZXJyb3IsIHJpc2sgb2Ygb3ZlcmZpdHRpbmcuIFNtYWxsIEM6IGVycm9ycyBhcmUgY2hlYXAg4oaSIHdpZGUgbWFyZ2luLCBoaWdoZXIgdHJhaW5pbmcgZXJyb3IsIGJldHRlciBnZW5lcmFsaXNhdGlvbi4gQ3Jvc3MtdmFsaWRhdGUgQyBvdmVyIGEgbG9nLXNwYWNlZCBncmlkIChlLmcuLCAxMOKBu8KzIHRvIDEwwrMpLiBUaGUgcmF0aW8gQy9uIGlzIHNjYWxlLXNlbnNpdGl2ZSDigJQgd2hlbiBuIGNoYW5nZXMsIHJlc2NhbGUgQyBwcm9wb3J0aW9uYWxseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uc3ZtIGltcG9ydCBTVkNcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5mcm9tIHNrbGVhcm4ubW9kZWxfc2VsZWN0aW9uIGltcG9ydCB0cmFpbl90ZXN0X3NwbGl0XG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgYWNjdXJhY3lfc2NvcmVcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihcbiAgICBuX3NhbXBsZXM9MzAwLCBuX2ZlYXR1cmVzPTIsIG5fcmVkdW5kYW50PTAsXG4gICAgbl9pbmZvcm1hdGl2ZT0yLCBuX2NsdXN0ZXJzX3Blcl9jbGFzcz0xLFxuICAgIGNsYXNzX3NlcD0wLjgsIHJhbmRvbV9zdGF0ZT00MlxuKVxueSA9IDIqeSAtIDEgICMgbWFwIHRvIHstMSwgKzF9XG5zY2FsZXIgPSBTdGFuZGFyZFNjYWxlcigpXG5YX3MgPSBzY2FsZXIuZml0X3RyYW5zZm9ybShYKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWF9zLCB5LCB0ZXN0X3NpemU9MC4zLCByYW5kb21fc3RhdGU9MClcblxucHJpbnQoZlx1MDAyN3tcIkNcIjpcdTAwM2U4fSB7XCJNYXJnaW5cIjpcdTAwM2UxMH0ge1wibl9TVnNcIjpcdTAwM2U2fSB7XCJUcmFpbiBBY2NcIjpcdTAwM2UxMH0ge1wiVGVzdCBBY2NcIjpcdTAwM2UxMH1cdTAwMjcpXG5mb3IgQyBpbiBbMC4wMSwgMC4xLCAxLjAsIDEwLjAsIDEwMC4wXTpcbiAgICBzdm0gPSBTVkMoa2VybmVsPVx1MDAyN2xpbmVhclx1MDAyNywgQz1DKS5maXQoWF90ciwgeV90cilcbiAgICBtYXJnaW4gPSAyLjAgLyBucC5saW5hbGcubm9ybShzdm0uY29lZl8pXG4gICAgdHJhaW5fYWNjID0gYWNjdXJhY3lfc2NvcmUoeV90ciwgc3ZtLnByZWRpY3QoWF90cikpXG4gICAgdGVzdF9hY2MgID0gYWNjdXJhY3lfc2NvcmUoeV90ZSwgc3ZtLnByZWRpY3QoWF90ZSkpXG4gICAgcHJpbnQoZlx1MDAyN3tDOlx1MDAzZTh9IHttYXJnaW46XHUwMDNlMTAuNGZ9IHtzdm0ubl9zdXBwb3J0Xy5zdW0oKTpcdTAwM2U2fSB7dHJhaW5fYWNjOlx1MDAzZTEwLjRmfSB7dGVzdF9hY2M6XHUwMDNlMTAuNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhpbmdlIExvc3MgdnMgTG9naXN0aWMgTG9zcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuIyBDb21wYXJlIGhpbmdlIGFuZCBsb2dpc3RpYyBsb3NzIGFzIGEgZnVuY3Rpb24gb2YgZnVuY3Rpb25hbCBtYXJnaW4gZiA9IHkgKiAod15UIHggKyBiKVxuZl92YWxzID0gbnAubGluc3BhY2UoLTMsIDMsIDMwMClcblxuaGluZ2VfbG9zcyAgID0gbnAubWF4aW11bSgwLCAxIC0gZl92YWxzKVxubG9naXN0aWNfbG9zcyA9IG5wLmxvZygxICsgbnAuZXhwKC1mX3ZhbHMpKVxuemVyb19vbmVfbG9zcyA9IChmX3ZhbHMgXHUwMDNjIDApLmFzdHlwZShmbG9hdClcblxucHJpbnQoZlx1MDAyN3tcImY9eSpzY29yZVwiOlx1MDAzZTEwfSB7XCJIaW5nZVwiOlx1MDAzZTh9IHtcIkxvZ2lzdGljXCI6XHUwMDNlMTB9IHtcIjAtMVwiOlx1MDAzZTZ9XHUwMDI3KVxuZm9yIGYgaW4gWy0yLjAsIC0xLjAsIDAuMCwgMC41LCAxLjAsIDIuMF06XG4gICAgaCA9IG1heCgwLCAxIC0gZilcbiAgICBsID0gbnAubG9nKDEgKyBucC5leHAoLWYpKVxuICAgIHpvID0gZmxvYXQoZiBcdTAwM2MgMClcbiAgICBwcmludChmXHUwMDI3e2Y6XHUwMDNlMTAuMWZ9IHtoOlx1MDAzZTguNGZ9IHtsOlx1MDAzZTEwLjRmfSB7em86XHUwMDNlNi4wZn1cdTAwMjcpXG5cbnByaW50KFx1MDAyN1xcbkhpbmdlOiB6ZXJvIGV4YWN0bHkgZm9yIGYgXHUwMDNlPSAxIChpbnNpZGUgY29ycmVjdCBtYXJnaW4pLlx1MDAyNylcbnByaW50KFx1MDAyN0xvZ2lzdGljOiBhc3ltcHRvdGljYWxseSBzbWFsbCBidXQgbmV2ZXIgZXhhY3RseSB6ZXJvLlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgRHVhbCB3aXRoIEJveCBDb25zdHJhaW50cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHNvZnQtbWFyZ2luIGR1YWwgaW50cm9kdWNlcyBib3ggY29uc3RyYWludHMgb24gzrE6IG1heGltaXNlIM6jzrHhtaIg4oiSIMK9zqPhtaLOo+KxvM6x4bWizrHisbx54bWieeKxvGsoeOG1oix44rG8KSwgc3ViamVjdCB0byAwIOKJpCDOseG1oiDiiaQgQyBhbmQgzqPOseG1onnhtaIgPSAwLiBUaGUgdXBwZXIgYm91bmQgzrHhtaIg4omkIEMgY29tZXMgZnJvbSB0aGUgc2xhY2sgZHVhbCBtdWx0aXBsaWVyLiBUaHJlZSB0eXBlcyBvZiBzdXBwb3J0IHZlY3RvcnMgZW1lcmdlIGZyb20gS0tUIGNvbXBsZW1lbnRhcnkgc2xhY2tuZXNzOiBmcmVlIFNWcyAoMCBcdTAwM2MgzrHhtaIgXHUwMDNjIEMsIM6+4bWiID0gMCwgcG9pbnQgb24gdGhlIG1hcmdpbiksIGJvdW5kZWQgU1ZzICjOseG1oiA9IEMsIM6+4bWiIFx1MDAzZSAwLCBwb2ludCBpbnNpZGUgbWFyZ2luIG9yIG1pc2NsYXNzaWZpZWQpLCBhbmQgbm9uLVNWcyAozrHhtaIgPSAwLCDOvuG1oiA9IDAsIHBvaW50IG91dHNpZGUgbWFyZ2luIGFuZCBjb3JyZWN0bHkgY2xhc3NpZmllZCkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ3Jvc3MtVmFsaWRhdGluZyBDIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnN2bSBpbXBvcnQgU1ZDXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgR3JpZFNlYXJjaENWLCBTdHJhdGlmaWVkS0ZvbGRcblxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5ID0gbWFrZV9jbGFzc2lmaWNhdGlvbihcbiAgICBuX3NhbXBsZXM9NTAwLCBuX2ZlYXR1cmVzPTEwLCBuX2luZm9ybWF0aXZlPTYsXG4gICAgbl9yZWR1bmRhbnQ9MiwgcmFuZG9tX3N0YXRlPTQyXG4pXG5YX3MgPSBTdGFuZGFyZFNjYWxlcigpLmZpdF90cmFuc2Zvcm0oWClcblxucGFyYW1fZ3JpZCA9IHtcdTAwMjdDXHUwMDI3OiBucC5sb2dzcGFjZSgtMywgMywgMTMpfVxuY3YgPSBTdHJhdGlmaWVkS0ZvbGQobl9zcGxpdHM9NSwgc2h1ZmZsZT1UcnVlLCByYW5kb21fc3RhdGU9MClcblxuZ3JpZCA9IEdyaWRTZWFyY2hDVihcbiAgICBTVkMoa2VybmVsPVx1MDAyN3JiZlx1MDAyNywgZ2FtbWE9XHUwMDI3c2NhbGVcdTAwMjcpLFxuICAgIHBhcmFtX2dyaWQsXG4gICAgY3Y9Y3YsXG4gICAgc2NvcmluZz1cdTAwMjdhY2N1cmFjeVx1MDAyNyxcbiAgICByZXR1cm5fdHJhaW5fc2NvcmU9VHJ1ZSxcbiAgICBuX2pvYnM9LTFcbilcbmdyaWQuZml0KFhfcywgeSlcblxuYmVzdF9DICAgPSBncmlkLmJlc3RfcGFyYW1zX1tcdTAwMjdDXHUwMDI3XVxuYmVzdF9hY2MgPSBncmlkLmJlc3Rfc2NvcmVfXG5wcmludChmXHUwMDI3QmVzdCBDOiAgICAgICAgICAgIHtiZXN0X0M6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdCZXN0IENWIGFjY3VyYWN5OiAge2Jlc3RfYWNjOi40Zn1cdTAwMjcpXG5cbnJlc3VsdHMgPSBncmlkLmN2X3Jlc3VsdHNfXG5mb3IgaSwgQyBpbiBlbnVtZXJhdGUocmVzdWx0c1tcdTAwMjdwYXJhbV9DXHUwMDI3XSk6XG4gICAgaWYgYWJzKEMgLSBiZXN0X0MpIC8gbWF4KEMsIGJlc3RfQykgXHUwMDNjIDAuMDU6XG4gICAgICAgIHRyID0gcmVzdWx0c1tcdTAwMjdtZWFuX3RyYWluX3Njb3JlXHUwMDI3XVtpXVxuICAgICAgICB2YSA9IHJlc3VsdHNbXHUwMDI3bWVhbl90ZXN0X3Njb3JlXHUwMDI3XVtpXVxuICAgICAgICBwcmludChmXHUwMDI3Qz17QzouNGZ9OiB0cmFpbj17dHI6LjRmfSwgdmFsPXt2YTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Im51LVNWTSBQYXJhbWV0ZXJpc2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgzr0tU1ZNIHJlcGFyYW1ldGVyaXNlcyB0aGUgc29mdC1tYXJnaW4gU1ZNIHVzaW5nIM69IOKIiCAoMCwxXSBpbnN0ZWFkIG9mIEMuIFRoZSBwYXJhbWV0ZXIgzr0gaGFzIGEgZGlyZWN0IGludGVycHJldGF0aW9uOiBpdCBpcyBib3RoIGEgbG93ZXIgYm91bmQgb24gdGhlIGZyYWN0aW9uIG9mIHN1cHBvcnQgdmVjdG9ycyBhbmQgYW4gdXBwZXIgYm91bmQgb24gdGhlIGZyYWN0aW9uIG9mIG1hcmdpbiBlcnJvcnMuIFRoaXMgbWFrZXMgzr0gbW9yZSBpbnRlcnByZXRhYmxlIHRoYW4gQzogc2V0dGluZyDOvT0wLjEgbWVhbnMgXHUwMDI3YXQgbW9zdCAxMCUgb2YgdHJhaW5pbmcgcG9pbnRzIGFyZSBtYXJnaW4gZXJyb3JzIGFuZCBhdCBsZWFzdCAxMCUgYXJlIHN1cHBvcnQgdmVjdG9ycy5cdTAwMjcgVGhlIHByaW1hbCBpczogbWluaW1pc2Ugwr3igJZ34oCWwrIg4oiSIM69z4EgKyAoMS9uKc6jzr7htaIgc3ViamVjdCB0byB54bWiKHfhtYB44bWiK2IpIOKJpSDPgSDiiJIgzr7htaIsIM6+4bWiIOKJpSAwLCDPgSDiiaUgMC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uc3ZtIGltcG9ydCBOdVNWQ1xuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IGNyb3NzX3ZhbF9zY29yZVxuXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHkgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKFxuICAgIG5fc2FtcGxlcz00MDAsIG5fZmVhdHVyZXM9OCwgbl9pbmZvcm1hdGl2ZT01LCByYW5kb21fc3RhdGU9NDJcbilcblhfcyA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKVxuXG5wcmludChmXHUwMDI3e1wibnVcIjpcdTAwM2U2fSB7XCJuX1NWc1wiOlx1MDAzZTh9IHtcIlNWIGZyYWN0aW9uXCI6XHUwMDNlMTJ9IHtcIkNWIEFjY3VyYWN5XCI6XHUwMDNlMTJ9XHUwMDI3KVxuZm9yIG51IGluIFswLjA1LCAwLjEwLCAwLjIwLCAwLjMwLCAwLjUwXTpcbiAgICB0cnk6XG4gICAgICAgIG51c3ZjID0gTnVTVkMobnU9bnUsIGtlcm5lbD1cdTAwMjdyYmZcdTAwMjcsIGdhbW1hPVx1MDAyN3NjYWxlXHUwMDI3KVxuICAgICAgICBzY29yZXMgPSBjcm9zc192YWxfc2NvcmUobnVzdmMsIFhfcywgeSwgY3Y9NSwgc2NvcmluZz1cdTAwMjdhY2N1cmFjeVx1MDAyNylcbiAgICAgICAgbnVzdmMuZml0KFhfcywgeSlcbiAgICAgICAgbl9zdiA9IG51c3ZjLm5fc3VwcG9ydF8uc3VtKClcbiAgICAgICAgc3ZfZnJhYyA9IG5fc3YgLyBsZW4oWF9zKVxuICAgICAgICBwcmludChmXHUwMDI3e251Olx1MDAzZTYuMmZ9IHtuX3N2Olx1MDAzZThkfSB7c3ZfZnJhYzpcdTAwM2UxMi40Zn0ge3Njb3Jlcy5tZWFuKCk6XHUwMDNlMTIuNGZ9XHUwMDI3KVxuICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZTpcbiAgICAgICAgcHJpbnQoZlx1MDAyN3tudTpcdTAwM2U2LjJmfSAgaW5mZWFzaWJsZToge2V9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhhcmQtTWFyZ2luIHZzIFNvZnQtTWFyZ2luIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXNwZWN0IiwiSGFyZC1NYXJnaW4gU1ZNIiwiU29mdC1NYXJnaW4gU1ZNIChDLVNWTSkiXSwicm93cyI6W1siRmVhc2liaWxpdHkiLCJPbmx5IGlmIGRhdGEgaXMgbGluZWFybHkgc2VwYXJhYmxlIiwiQWx3YXlzIGZlYXNpYmxlIl0sWyJQcmltYWwgY29uc3RyYWludCIsInnhtaIod+G1gHjhtaIrYikg4omlIDEiLCJ54bWiKHfhtYB44bWiK2IpIOKJpSAxIOKIkiDOvuG1oiJdLFsiRHVhbCBjb25zdHJhaW50IG9uIM6xIiwiMCDiiaQgzrHhtaIiLCIwIOKJpCDOseG1oiDiiaQgQyAoYm94IGNvbnN0cmFpbnQpIl0sWyJPdXRsaWVyIHNlbnNpdGl2aXR5IiwiVmVyeSBoaWdoIOKAlCBvbmUgb3V0bGllciBjb2xsYXBzZXMgbWFyZ2luIiwiQ29udHJvbGxlZCBieSBDIl0sWyJTdXBwb3J0IHZlY3RvciB0eXBlcyIsIk9uIG1hcmdpbiBvbmx5ICjOseG1olx1MDAzZTApIiwiTWFyZ2luICgwXHUwMDNjzrHhtaJcdTAwM2NDKSArIGJvdW5kZWQgKM6x4bWiPUMpIl0sWyJPdmVyZml0dGluZyByaXNrIiwiVmVyeSBoaWdoIGZvciBuZWFybHktc2VwYXJhYmxlIG5vaXN5IGRhdGEiLCJDb250cm9sbGVkIHZpYSBjcm9zcy12YWxpZGF0ZWQgQyJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEd1aWRlbGluZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFsd2F5cyBzdGFuZGFyZGlzZSBmZWF0dXJlcyBiZWZvcmUgdHJhaW5pbmcgU1ZNIOKAlCB0aGUgTDIgbm9ybSBpbiB0aGUgb2JqZWN0aXZlIGlzIHNjYWxlLXNlbnNpdGl2ZS4gVXNlIEdyaWRTZWFyY2hDViBvciBSYW5kb21pemVkU2VhcmNoQ1Ygd2l0aCBhIGxvZy1zcGFjZWQgQyBncmlkICgxMOKBu8KzIHRvIDEwwrMpIGFuZCDOsyBncmlkIGZvciBSQkYga2VybmVscy4gV2l0aCBSQkYgU1ZNLCBDIGFuZCDOsyBpbnRlcmFjdDogbGFyZ2UgzrMgKyBzbWFsbCBDIHJpc2tzIHVuZGVyZml0dGluZzsgc21hbGwgzrMgKyBsYXJnZSBDIHJpc2tzIG92ZXJmaXR0aW5nLiBBcyBuIGdyb3dzIGJleW9uZCB+NTAsMDAwLCBzd2l0Y2ggdG8gTGluZWFyU1ZDICh1c2VzIGxpYmxpbmVhclx1MDAyN3MgZHVhbCBDRCkgd2hpY2ggaXMgTyhuKSBwZXIgaXRlcmF0aW9uIHJhdGhlciB0aGFuIE8obsKyKSB0byBPKG7CsykgZm9yIHRoZSBmdWxsIGtlcm5lbCBTVk0uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTY2FsZSBhbGwgZmVhdHVyZXMgd2l0aCBTdGFuZGFyZFNjYWxlciBiZWZvcmUgZml0dGluZyBhbnkgU1ZNIOKAlCBtYXJnaW4gd2lkdGggaXMgbm90IHNjYWxlIGludmFyaWFudC4iLCJGb3IgUkJGIFNWTSwgam9pbnRseSBjcm9zcy12YWxpZGF0ZSBDIGFuZCBnYW1tYTsgYSBkaWFnb25hbCBvZiB0aGUgKEMsZ2FtbWEpIGdyaWQgb2Z0ZW4gd29ya3Mgd2VsbC4iLCJMYXJnZSBDIOKGkiBsb3cgdHJhaW5pbmcgZXJyb3IsIHJpc2sgb2Ygb3ZlcmZpdHRpbmc7IHNtYWxsIEMg4oaSIGxhcmdlciBtYXJnaW4sIGhpZ2hlciB0cmFpbmluZyBlcnJvci4iLCJVc2UgTnVTVkMgd2hlbiB5b3Ugd2FudCBkaXJlY3QgY29udHJvbCBvdmVyIHRoZSBmcmFjdGlvbiBvZiBzdXBwb3J0IHZlY3RvcnMgKG51ID0gdGhhdCBmcmFjdGlvbiDCsSDOtSkuIiwiRm9yIG4gXHUwMDNlIDUwaywgdXNlIExpbmVhclNWQyBvciBTR0RDbGFzc2lmaWVyIHdpdGggaGluZ2UgbG9zcyDigJQgZnVsbCBrZXJuZWwgU1ZNIGJlY29tZXMgdG9vIHNsb3cuIiwiQ2hlY2sgbl9zdXBwb3J0XyBhZnRlciBmaXR0aW5nOiBpZiBuZWFybHkgYWxsIHBvaW50cyBhcmUgU1ZzLCBDIGlzIHRvbyBzbWFsbCBvciB0aGUgcHJvYmxlbSBpcyBoYXJkLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Soft-Margin SVM and Slack Variables

The hard-margin SVM requires perfect linear separability, which real data rarely satisfies. Even when separable, a single outlier can drastically shift the maximum-margin hyperplane. Soft-margin SVM introduces slack variables ξᵢ ≥ 0 that allow points to violate the margin or be misclassified, penalising violations in proportion to C. This makes the SVM robust to noise and applicable to any dataset, at the cost of a model-selection choice for C.

## Why Hard-Margin Fails

Hard-margin SVM fails in two scenarios: (1) the data is not linearly separable — no hyperplane achieves zero training error; (2) one or a few outliers lie on the wrong side of the natural boundary, forcing the margin to collapse toward zero to accommodate them. Both cases produce an infeasible or highly unstable optimisation problem. The soft-margin extension allows controlled misclassification, balancing margin width against training error.

## Slack Variables and the Primal

Introduce slack variables ξᵢ ≥ 0 for each training point. The soft-margin primal is: minimise ½‖w‖² + C·Σᵢξᵢ, subject to yᵢ(wᵀxᵢ+b) ≥ 1 − ξᵢ and ξᵢ ≥ 0. When ξᵢ = 0 the point is correctly classified outside or on the margin. When 0 < ξᵢ ≤ 1 the point is inside the margin (margin violator). When ξᵢ > 1 the point is misclassified. The parameter C > 0 controls the penalty for violations: large C → hard margin (few violations), small C → wide margin (more violations tolerated).

## Hinge Loss

The slack variable ξᵢ equals the hinge loss: ξᵢ = max(0, 1 − yᵢ(wᵀxᵢ+b)). Substituting, the soft-margin SVM minimises ½‖w‖² + C·Σ max(0, 1 − yᵢf(xᵢ)) — a regularised hinge loss. The hinge loss is zero for correctly classified points outside the margin (functional margin ≥ 1) and grows linearly for points inside or on the wrong side. This is convex and sub-differentiable, enabling gradient/subgradient optimisation methods.

> **Interpreting the C Parameter**: C acts as the inverse regularisation strength (analogous to 1/λ in Ridge). Large C: model is penalised heavily for errors → narrow margin, low training error, risk of overfitting. Small C: errors are cheap → wide margin, higher training error, better generalisation. Cross-validate C over a log-spaced grid (e.g., 10⁻³ to 10³). The ratio C/n is scale-sensitive — when n changes, rescale C proportionally.

```python
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)
X, y = make_classification(
    n_samples=300, n_features=2, n_redundant=0,
    n_informative=2, n_clusters_per_class=1,
    class_sep=0.8, random_state=42
)
y = 2*y - 1  # map to {-1, +1}
scaler = StandardScaler()
X_s = scaler.fit_transform(X)
X_tr, X_te, y_tr, y_te = train_test_split(X_s, y, test_size=0.3, random_state=0)

print(f'{"C":>8} {"Margin":>10} {"n_SVs":>6} {"Train Acc":>10} {"Test Acc":>10}')
for C in [0.01, 0.1, 1.0, 10.0, 100.0]:
    svm = SVC(kernel='linear', C=C).fit(X_tr, y_tr)
    margin = 2.0 / np.linalg.norm(svm.coef_)
    train_acc = accuracy_score(y_tr, svm.predict(X_tr))
    test_acc  = accuracy_score(y_te, svm.predict(X_te))
    print(f'{C:>8} {margin:>10.4f} {svm.n_support_.sum():>6} {train_acc:>10.4f} {test_acc:>10.4f}')
```

## Hinge Loss vs Logistic Loss

```python
import numpy as np

# Compare hinge and logistic loss as a function of functional margin f = y * (w^T x + b)
f_vals = np.linspace(-3, 3, 300)

hinge_loss   = np.maximum(0, 1 - f_vals)
logistic_loss = np.log(1 + np.exp(-f_vals))
zero_one_loss = (f_vals < 0).astype(float)

print(f'{"f=y*score":>10} {"Hinge":>8} {"Logistic":>10} {"0-1":>6}')
for f in [-2.0, -1.0, 0.0, 0.5, 1.0, 2.0]:
    h = max(0, 1 - f)
    l = np.log(1 + np.exp(-f))
    zo = float(f < 0)
    print(f'{f:>10.1f} {h:>8.4f} {l:>10.4f} {zo:>6.0f}')

print('\nHinge: zero exactly for f >= 1 (inside correct margin).')
print('Logistic: asymptotically small but never exactly zero.')
```

## The Dual with Box Constraints

The soft-margin dual introduces box constraints on α: maximise Σαᵢ − ½ΣᵢΣⱼαᵢαⱼyᵢyⱼk(xᵢ,xⱼ), subject to 0 ≤ αᵢ ≤ C and Σαᵢyᵢ = 0. The upper bound αᵢ ≤ C comes from the slack dual multiplier. Three types of support vectors emerge from KKT complementary slackness: free SVs (0 < αᵢ < C, ξᵢ = 0, point on the margin), bounded SVs (αᵢ = C, ξᵢ > 0, point inside margin or misclassified), and non-SVs (αᵢ = 0, ξᵢ = 0, point outside margin and correctly classified).

## Cross-Validating C

```python
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, StratifiedKFold

np.random.seed(42)
X, y = make_classification(
    n_samples=500, n_features=10, n_informative=6,
    n_redundant=2, random_state=42
)
X_s = StandardScaler().fit_transform(X)

param_grid = {'C': np.logspace(-3, 3, 13)}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

grid = GridSearchCV(
    SVC(kernel='rbf', gamma='scale'),
    param_grid,
    cv=cv,
    scoring='accuracy',
    return_train_score=True,
    n_jobs=-1
)
grid.fit(X_s, y)

best_C   = grid.best_params_['C']
best_acc = grid.best_score_
print(f'Best C:            {best_C:.4f}')
print(f'Best CV accuracy:  {best_acc:.4f}')

results = grid.cv_results_
for i, C in enumerate(results['param_C']):
    if abs(C - best_C) / max(C, best_C) < 0.05:
        tr = results['mean_train_score'][i]
        va = results['mean_test_score'][i]
        print(f'C={C:.4f}: train={tr:.4f}, val={va:.4f}')
```

## nu-SVM Parameterisation

The ν-SVM reparameterises the soft-margin SVM using ν ∈ (0,1] instead of C. The parameter ν has a direct interpretation: it is both a lower bound on the fraction of support vectors and an upper bound on the fraction of margin errors. This makes ν more interpretable than C: setting ν=0.1 means 'at most 10% of training points are margin errors and at least 10% are support vectors.' The primal is: minimise ½‖w‖² − νρ + (1/n)Σξᵢ subject to yᵢ(wᵀxᵢ+b) ≥ ρ − ξᵢ, ξᵢ ≥ 0, ρ ≥ 0.

```python
import numpy as np
from sklearn.svm import NuSVC
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

np.random.seed(42)
X, y = make_classification(
    n_samples=400, n_features=8, n_informative=5, random_state=42
)
X_s = StandardScaler().fit_transform(X)

print(f'{"nu":>6} {"n_SVs":>8} {"SV fraction":>12} {"CV Accuracy":>12}')
for nu in [0.05, 0.10, 0.20, 0.30, 0.50]:
    try:
        nusvc = NuSVC(nu=nu, kernel='rbf', gamma='scale')
        scores = cross_val_score(nusvc, X_s, y, cv=5, scoring='accuracy')
        nusvc.fit(X_s, y)
        n_sv = nusvc.n_support_.sum()
        sv_frac = n_sv / len(X_s)
        print(f'{nu:>6.2f} {n_sv:>8d} {sv_frac:>12.4f} {scores.mean():>12.4f}')
    except Exception as e:
        print(f'{nu:>6.2f}  infeasible: {e}')
```

## Hard-Margin vs Soft-Margin Comparison

| Aspect | Hard-Margin SVM | Soft-Margin SVM (C-SVM) |
| --- | --- | --- |
| Feasibility | Only if data is linearly separable | Always feasible |
| Primal constraint | yᵢ(wᵀxᵢ+b) ≥ 1 | yᵢ(wᵀxᵢ+b) ≥ 1 − ξᵢ |
| Dual constraint on α | 0 ≤ αᵢ | 0 ≤ αᵢ ≤ C (box constraint) |
| Outlier sensitivity | Very high — one outlier collapses margin | Controlled by C |
| Support vector types | On margin only (αᵢ>0) | Margin (0<αᵢ<C) + bounded (αᵢ=C) |
| Overfitting risk | Very high for nearly-separable noisy data | Controlled via cross-validated C |

## Practical Guidelines

Always standardise features before training SVM — the L2 norm in the objective is scale-sensitive. Use GridSearchCV or RandomizedSearchCV with a log-spaced C grid (10⁻³ to 10³) and γ grid for RBF kernels. With RBF SVM, C and γ interact: large γ + small C risks underfitting; small γ + large C risks overfitting. As n grows beyond ~50,000, switch to LinearSVC (uses liblinear's dual CD) which is O(n) per iteration rather than O(n²) to O(n³) for the full kernel SVM.

- Scale all features with StandardScaler before fitting any SVM — margin width is not scale invariant.
- For RBF SVM, jointly cross-validate C and gamma; a diagonal of the (C,gamma) grid often works well.
- Large C → low training error, risk of overfitting; small C → larger margin, higher training error.
- Use NuSVC when you want direct control over the fraction of support vectors (nu = that fraction ± ε).
- For n > 50k, use LinearSVC or SGDClassifier with hinge loss — full kernel SVM becomes too slow.
- Check n_support_ after fitting: if nearly all points are SVs, C is too small or the problem is hard.

---

