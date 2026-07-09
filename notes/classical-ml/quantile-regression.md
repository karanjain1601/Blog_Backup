---
title: "Quantile Regression — Conditional Quantile Estimation"
slug: "quantile-regression"
description: "Derive quantile regression via the pinball loss, estimate simultaneous prediction intervals at multiple quantiles, address the quantile crossing problem with isotonic regression, and apply conformal prediction for distribution-free coverage guarantees."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiT3JkaW5hcnkgbGVhc3Qgc3F1YXJlcyBlc3RpbWF0ZXMgdGhlIGNvbmRpdGlvbmFsIG1lYW4gRVtZfFg9eF0uIFF1YW50aWxlIHJlZ3Jlc3Npb24gZXN0aW1hdGVzIGFueSBjb25kaXRpb25hbCBxdWFudGlsZSBRX8+EKFl8WD14KSBmb3Igz4Qg4oiIICgwLDEpIOKAlCBmb3IgZXhhbXBsZSwgdGhlIDkwdGggcGVyY2VudGlsZSBvZiBob3VzZSBwcmljZXMgZ2l2ZW4gc3F1YXJlIGZvb3RhZ2UsIG9yIHRoZSA1dGggcGVyY2VudGlsZSBvZiBkYWlseSByZXR1cm5zIGZvciBWYVIuIFRoaXMgcHJvdmlkZXMgYSBjb21wbGV0ZSBwaWN0dXJlIG9mIHRoZSBjb25kaXRpb25hbCBkaXN0cmlidXRpb246IGhvdyBkb2VzIHRoZSBzcHJlYWQsIHNrZXduZXNzLCBhbmQgdGFpbCBiZWhhdmlvdXIgY2hhbmdlIHdpdGggWD8gQXBwbGljYXRpb25zIGluY2x1ZGUgZGVtYW5kIGZvcmVjYXN0aW5nICh1cHBlciBxdWFudGlsZSBmb3IgaW52ZW50b3J5IHBsYW5uaW5nKSwgcmlzayBtYW5hZ2VtZW50IChWYWx1ZS1hdC1SaXNrKSwgYW5kIHVuY2VydGFpbnR5IHF1YW50aWZpY2F0aW9uIGZvciBtYWNoaW5lIGxlYXJuaW5nIHByZWRpY3Rpb25zLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZSBQaW5iYWxsIChUaWx0ZWQgTDEpIExvc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlF1YW50aWxlIHJlZ3Jlc3Npb24gbWluaW1pc2VzIHRoZSBwaW5iYWxsIGxvc3M6IM+BX8+EKHUpID0gdcK3z4QgaWYgdSDiiaUgMCAodW5kZXJwcmVkaWN0aW9uKSwgdcK3KM+ELTEpIGlmIHUgXHUwMDNjIDAgKG92ZXJwcmVkaWN0aW9uKS4gRm9yIM+EPTAuOSwgdW5kZXJwcmVkaWN0aW9uIGlzIHBlbmFsaXNlZCA5eCBtb3JlIHRoYW4gb3ZlcnByZWRpY3Rpb24g4oCUIHRoaXMgYXN5bW1ldHJ5IGZvcmNlcyB0aGUgb3B0aW1hbCBwcmVkaWN0aW9uIHRvIGJlIHRoZSA5MHRoIHBlcmNlbnRpbGUuIEF0IHRoZSBvcHRpbXVtLCBleGFjdGx5IM+EwrduIG9mIHRoZSByZXNpZHVhbHMgYXJlIHBvc2l0aXZlIGFuZCAoMS3PhCnCt24gYXJlIG5lZ2F0aXZlOiBleGFjdGx5IHRoZSBkZWZpbml0aW9uIG9mIHRoZSDPhC10aCBzYW1wbGUgcXVhbnRpbGUuIEZvciDPhD0wLjUsIHRoZSBsb3NzIHJlZHVjZXMgdG8gfHV8LzIsIHRoZSBMMSBsb3NzIOKAlCBzbyBtZWRpYW4gcmVncmVzc2lvbiBpcyBhIHNwZWNpYWwgY2FzZS4gVW5saWtlIE9MUywgcGluYmFsbCBsb3NzIGlzIHJvYnVzdCB0byBvdXRsaWVycyBvbiB0aGUgaGVhdnkgdGFpbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfcmVncmVzc2lvblxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuXG5kZWYgcGluYmFsbF9sb3NzKHlfdHJ1ZSwgeV9wcmVkLCB0YXUpOlxuICAgIHJlc2lkdWFscyA9IHlfdHJ1ZSAtIHlfcHJlZFxuICAgIHJldHVybiBucC53aGVyZShyZXNpZHVhbHMgXHUwMDNlPSAwLCB0YXUgKiByZXNpZHVhbHMsICh0YXUgLSAxKSAqIHJlc2lkdWFscykubWVhbigpXG5cbmNsYXNzIFF1YW50aWxlUmVncmVzc2lvbkdEOlxuICAgIFwiXCJcIlF1YW50aWxlIHJlZ3Jlc3Npb24gdmlhIHN1YmdyYWRpZW50IGRlc2NlbnQgb24gcGluYmFsbCBsb3NzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0YXU9MC41LCBscj0wLjAxLCBuX2l0ZXI9MjAwMCk6XG4gICAgICAgIHNlbGYudGF1ID0gdGF1XG4gICAgICAgIHNlbGYubHIgPSBsclxuICAgICAgICBzZWxmLm5faXRlciA9IG5faXRlclxuXG4gICAgZGVmIGZpdChzZWxmLCBYLCB5KTpcbiAgICAgICAgbiwgcCA9IFguc2hhcGVcbiAgICAgICAgWF9iID0gbnAuaHN0YWNrKFtucC5vbmVzKChuLCAxKSksIFhdKVxuICAgICAgICBzZWxmLndfID0gbnAuemVyb3MoWF9iLnNoYXBlWzFdKVxuICAgICAgICBmb3IgXyBpbiByYW5nZShzZWxmLm5faXRlcik6XG4gICAgICAgICAgICByZXNpZCA9IHkgLSBYX2IgQCBzZWxmLndfXG4gICAgICAgICAgICBzdWJncmFkID0gbnAud2hlcmUocmVzaWQgXHUwMDNlPSAwLCAtc2VsZi50YXUsIC0oc2VsZi50YXUgLSAxKSlcbiAgICAgICAgICAgIHNlbGYud18gLT0gc2VsZi5sciAqIChYX2IuVCBAIHN1YmdyYWQpIC8gblxuICAgICAgICByZXR1cm4gc2VsZlxuXG4gICAgZGVmIHByZWRpY3Qoc2VsZiwgWCk6XG4gICAgICAgIFhfYiA9IG5wLmhzdGFjayhbbnAub25lcygobGVuKFgpLCAxKSksIFhdKVxuICAgICAgICByZXR1cm4gWF9iIEAgc2VsZi53X1xuXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHkgPSBtYWtlX3JlZ3Jlc3Npb24obl9zYW1wbGVzPTMwMCwgbl9mZWF0dXJlcz0zLCBub2lzZT0yMC4wLCByYW5kb21fc3RhdGU9NDIpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYLCB5LCB0ZXN0X3NpemU9MC4yNSwgcmFuZG9tX3N0YXRlPTQyKVxuXG5mb3IgdGF1IGluIFswLjEsIDAuNSwgMC45XTpcbiAgICBxciA9IFF1YW50aWxlUmVncmVzc2lvbkdEKHRhdT10YXUsIGxyPTAuMDA1LCBuX2l0ZXI9MzAwMCkuZml0KFhfdHIsIHlfdHIpXG4gICAgcGJsID0gcGluYmFsbF9sb3NzKHlfdGUsIHFyLnByZWRpY3QoWF90ZSksIHRhdSlcbiAgICBjb3ZlcmFnZSA9ICh5X3RlIFx1MDAzYyBxci5wcmVkaWN0KFhfdGUpKS5tZWFuKClcbiAgICBwcmludChmXHUwMDI3dGF1PXt0YXV9OiBwaW5iYWxsX2xvc3M9e3BibDouM2Z9LCBlbXBpcmljYWxfY292ZXJhZ2U9e2NvdmVyYWdlOi4zZn0gKHRhcmdldD17dGF1fSlcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU2tsZWFybiBRdWFudGlsZVJlZ3Jlc3NvciBhbmQgR3JhZGllbnQgQm9vc3RpbmcgUXVhbnRpbGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJza2xlYXJuXHUwMDI3cyBRdWFudGlsZVJlZ3Jlc3NvciAoYWRkZWQgaW4gMS4wKSBzb2x2ZXMgcXVhbnRpbGUgcmVncmVzc2lvbiBleGFjdGx5IGFzIGEgbGluZWFyIHByb2dyYW0gdXNpbmcgaW50ZXJpb3IgcG9pbnQgbWV0aG9kcyDigJQgZmFyIG1vcmUgbnVtZXJpY2FsbHkgc3RhYmxlIHRoYW4gZ3JhZGllbnQgZGVzY2VudC4gVGhlIGFscGhhIHBhcmFtZXRlciBhZGRzIEwxIHJlZ3VsYXJpc2F0aW9uIG9uIHRoZSB3ZWlnaHRzLiBGb3Igbm9ubGluZWFyIHF1YW50aWxlIHJlZ3Jlc3Npb24sIEdyYWRpZW50Qm9vc3RpbmdSZWdyZXNzb3Igd2l0aCBsb3NzPVx1MDAyN3F1YW50aWxlXHUwMDI3LCBhbHBoYT10YXUgZml0cyBncmFkaWVudCBib29zdGVkIHRyZWVzIHRhcmdldGluZyB0aGUgcGluYmFsbCBsb3NzLCBlbmFibGluZyBmbGV4aWJsZSBub25saW5lYXIgY29uZGl0aW9uYWwgcXVhbnRpbGUgZXN0aW1hdGlvbi4gU2ltdWx0YW5lb3VzIHF1YW50aWxlIHJlZ3Jlc3Npb24gZml0cyBtdWx0aXBsZSDPhCB2YWx1ZXMsIG9mdGVuIHdpdGggYSBzaW5nbGUgc2hhcmVkIG1vZGVsIGJhY2tib25lLCB0byBwcm9kdWNlIGNvbnNpc3RlbnQgcHJlZGljdGlvbiBpbnRlcnZhbHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUXVhbnRpbGVSZWdyZXNzb3JcbmZyb20gc2tsZWFybi5lbnNlbWJsZSBpbXBvcnQgR3JhZGllbnRCb29zdGluZ1JlZ3Jlc3NvclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuXG5ucC5yYW5kb20uc2VlZCg0Milcbm4gPSA1MDBcblhfMWQgPSBucC5yYW5kb20udW5pZm9ybSgwLCAxMCwgbikucmVzaGFwZSgtMSwgMSlcbiMgSGV0ZXJvc2NlZGFzdGljOiB2YXJpYW5jZSBpbmNyZWFzZXMgd2l0aCBYXG55ID0gMiAqIFhfMWQucmF2ZWwoKSArIG5wLnJhbmRvbS5yYW5kbihuKSAqICgwLjUgKyAwLjMgKiBYXzFkLnJhdmVsKCkpXG5YX3RyLCBYX3RlLCB5X3RyLCB5X3RlID0gdHJhaW5fdGVzdF9zcGxpdChYXzFkLCB5LCB0ZXN0X3NpemU9MC4yNSwgcmFuZG9tX3N0YXRlPTQyKVxuXG5tb2RlbHMgPSB7fVxuZm9yIHRhdSBpbiBbMC4xLCAwLjUsIDAuOV06XG4gICAgcXIgPSBRdWFudGlsZVJlZ3Jlc3NvcihxdWFudGlsZT10YXUsIGFscGhhPTAuMSwgc29sdmVyPVx1MDAyN2hpZ2hzXHUwMDI3KVxuICAgIHFyLmZpdChYX3RyLCB5X3RyKVxuICAgIG1vZGVsc1t0YXVdID0gcXJcbiAgICBjb3ZlcmFnZSA9ICh5X3RlIFx1MDAzYyBxci5wcmVkaWN0KFhfdGUpKS5tZWFuKClcbiAgICBwcmludChmXHUwMDI3TGluZWFyIFFSICB0YXU9e3RhdX06IGNvdmVyYWdlPXtjb3ZlcmFnZTouM2Z9ICh0YXJnZXQge3RhdTouMWZ9KVx1MDAyNylcblxuIyBHcmFkaWVudCBib29zdGluZyBmb3Igbm9ubGluZWFyIHF1YW50aWxlIGVzdGltYXRpb25cbmdiOTAgPSBHcmFkaWVudEJvb3N0aW5nUmVncmVzc29yKGxvc3M9XHUwMDI3cXVhbnRpbGVcdTAwMjcsIGFscGhhPTAuOSwgbl9lc3RpbWF0b3JzPTIwMCwgcmFuZG9tX3N0YXRlPTQyKVxuZ2I5MC5maXQoWF90ciwgeV90cilcbnByaW50KGZcdTAwMjdHQiBRUiAgdGF1PTAuOTogY292ZXJhZ2U9eyh5X3RlIFx1MDAzYyBnYjkwLnByZWRpY3QoWF90ZSkpLm1lYW4oKTouM2Z9XHUwMDI3KVxuXG5sb3dlciA9IG1vZGVsc1swLjFdLnByZWRpY3QoWF90ZSlcbnVwcGVyID0gbW9kZWxzWzAuOV0ucHJlZGljdChYX3RlKVxucHJpbnQoZlx1MDAyNzgwJSBQSSBjb3ZlcmFnZTogeygoeV90ZSBcdTAwM2U9IGxvd2VyKSBcdTAwMjYgKHlfdGUgXHUwMDNjPSB1cHBlcikpLm1lYW4oKTouM2Z9ICh0YXJnZXQgMC44MClcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUXVhbnRpbGUgQ3Jvc3NpbmcgYW5kIElzb3RvbmljIFJlZ3Jlc3Npb24gRml4In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaGVuIGZpdHRpbmcgcXVhbnRpbGUgbW9kZWxzIGF0IG11bHRpcGxlIM+EIHZhbHVlcyBpbmRlcGVuZGVudGx5LCB0aGVpciBwcmVkaWN0aW9ucyBjYW4gY3Jvc3M6IHRoZSA5MHRoIHBlcmNlbnRpbGUgcHJlZGljdGlvbiBjYW4gYmUgbG93ZXIgdGhhbiB0aGUgODB0aCBwZXJjZW50aWxlIGZvciBzb21lIHggdmFsdWVzLiBUaGlzIGlzIHN0YXRpc3RpY2FsbHkgaW5jb2hlcmVudCDigJQgcXVhbnRpbGUgZnVuY3Rpb25zIFFfz4QoWXxYPXgpIG11c3QgYmUgbm9uLWRlY3JlYXNpbmcgaW4gz4QgZm9yIGVhY2ggeC4gVGhlIHN0YW5kYXJkIGZpeCBpcyBpc290b25pYyByZWdyZXNzaW9uOiBhZnRlciBvYnRhaW5pbmcgcmF3IHByZWRpY3Rpb25zIGF0IGFsbCDPhCB2YWx1ZXMgZm9yIGVhY2ggdGVzdCBwb2ludCwgYXBwbHkgaXNvdG9uaWMgcmVncmVzc2lvbiBhY3Jvc3Mgz4QgdG8gZW5mb3JjZSBtb25vdG9uaWNpdHkuIFRoaXMgaXMgYSBwb3N0LXByb2Nlc3Npbmcgc3RlcCB3aXRoIE8oSyBsb2cgSykgY29zdCBwZXIgc2FtcGxlIHdoZXJlIEsgaXMgdGhlIG51bWJlciBvZiBxdWFudGlsZSBsZXZlbHMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJRdWFudGlsZSBDcm9zc2luZyBpcyBhIFNpbGVudCBCdWciLCJjb250ZW50IjoiQ3Jvc3NlZCBxdWFudGlsZXMgKGUuZy4sIFFfOTAgXHUwMDNjIFFfODAgZm9yIHNvbWUgeCkgcHJvZHVjZSBwcmVkaWN0aW9uIGludGVydmFscyB3aXRoIG5lZ2F0aXZlIHdpZHRoIOKAlCBhIHNpbGVudCBidWcgdGhhdCBpbnZhbGlkYXRlcyBhbGwgZG93bnN0cmVhbSBjYWxjdWxhdGlvbnMuIEFsd2F5cyBjaGVjayBmb3IgY3Jvc3NpbmdzIGFmdGVyIGZpdHRpbmcgbXVsdGlwbGUgcXVhbnRpbGVzIGluZGVwZW5kZW50bHkuIEFwcGx5IGlzb3RvbmljIHJlZ3Jlc3Npb24gb3IgdXNlIG5vbi1jcm9zc2luZyBxdWFudGlsZSByZWdyZXNzaW9uIHZhcmlhbnRzIChqb2ludCBvcHRpbWlzYXRpb24gd2l0aCBvcmRlcmluZyBjb25zdHJhaW50cykuIHNrbGVhcm5cdTAwMjdzIFF1YW50aWxlUmVncmVzc29yIGlzIHBhcnRpY3VsYXJseSBwcm9uZSB0byBjcm9zc2luZyBmb3Igc21hbGwgZGF0YXNldHMgb3IgaGlnaCByZWd1bGFyaXNhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBRdWFudGlsZVJlZ3Jlc3NvclxuZnJvbSBza2xlYXJuLmlzb3RvbmljIGltcG9ydCBJc290b25pY1JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IHRyYWluX3Rlc3Rfc3BsaXRcblxubnAucmFuZG9tLnNlZWQoNDIpXG5uID0gMzAwXG5YID0gbnAucmFuZG9tLnVuaWZvcm0oMCwgMTAsIG4pLnJlc2hhcGUoLTEsIDEpXG55ID0gMyAqIFgucmF2ZWwoKSArIG5wLnJhbmRvbS5yYW5kbihuKSAqICgxICsgMC41ICogWC5yYXZlbCgpKVxuWF90ciwgWF90ZSwgeV90ciwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWCwgeSwgdGVzdF9zaXplPTAuMywgcmFuZG9tX3N0YXRlPTQyKVxuXG50YXVzID0gbnAubGluc3BhY2UoMC4wNSwgMC45NSwgMTkpXG5wcmVkc19yYXcgPSBucC56ZXJvcygobGVuKFhfdGUpLCBsZW4odGF1cykpKVxuXG5mb3IgaiwgdGF1IGluIGVudW1lcmF0ZSh0YXVzKTpcbiAgICBxciA9IFF1YW50aWxlUmVncmVzc29yKHF1YW50aWxlPXRhdSwgYWxwaGE9MC4wMSwgc29sdmVyPVx1MDAyN2hpZ2hzXHUwMDI3KVxuICAgIHFyLmZpdChYX3RyLCB5X3RyKVxuICAgIHByZWRzX3Jhd1s6LCBqXSA9IHFyLnByZWRpY3QoWF90ZSlcblxuY3Jvc3NpbmdzX2JlZm9yZSA9IG5wLnN1bShucC5kaWZmKHByZWRzX3JhdywgYXhpcz0xKSBcdTAwM2MgMClcbnByaW50KGZcdTAwMjdRdWFudGlsZSBjcm9zc2luZ3MgYmVmb3JlIGlzb3RvbmljOiB7Y3Jvc3NpbmdzX2JlZm9yZX1cdTAwMjcpXG5cbiMgQXBwbHkgaXNvdG9uaWMgcmVncmVzc2lvbiBwZXIgc2FtcGxlIHRvIGVuZm9yY2UgdGF1LW1vbm90b25pY2l0eVxucHJlZHNfaXNvID0gbnAuemVyb3NfbGlrZShwcmVkc19yYXcpXG5pc28gPSBJc290b25pY1JlZ3Jlc3Npb24oaW5jcmVhc2luZz1UcnVlKVxuZm9yIGkgaW4gcmFuZ2UobGVuKFhfdGUpKTpcbiAgICBwcmVkc19pc29baV0gPSBpc28uZml0X3RyYW5zZm9ybSh0YXVzLCBwcmVkc19yYXdbaV0pXG5cbmNyb3NzaW5nc19hZnRlciA9IG5wLnN1bShucC5kaWZmKHByZWRzX2lzbywgYXhpcz0xKSBcdTAwM2MgMClcbnByaW50KGZcdTAwMjdRdWFudGlsZSBjcm9zc2luZ3MgYWZ0ZXIgaXNvdG9uaWM6ICB7Y3Jvc3NpbmdzX2FmdGVyfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb25mb3JtYWwgUXVhbnRpbGUgUmVncmVzc2lvbiBmb3IgR3VhcmFudGVlZCBDb3ZlcmFnZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgcXVhbnRpbGUgcmVncmVzc2lvbiB0YXJnZXRzIFFfz4QoWXxYPXgpIGJ1dCBwcm92aWRlcyBubyBmaW5pdGUtc2FtcGxlIGNvdmVyYWdlIGd1YXJhbnRlZSDigJQgY292ZXJhZ2UgaXMgb25seSBhcHByb3hpbWF0ZSwgZXNwZWNpYWxseSB3aXRoIGxpbWl0ZWQgZGF0YSBvciBtb2RlbCBtaXNzcGVjaWZpY2F0aW9uLiBDb25mb3JtYWwgUXVhbnRpbGUgUmVncmVzc2lvbiAoQ1FSLCBSb21hbm8gZXQgYWwuIDIwMTkpIHByb3ZpZGVzIGEgZGlzdHJpYnV0aW9uLWZyZWUsIGZpbml0ZS1zYW1wbGUgZ3VhcmFudGVlOiB0aGUgaW50ZXJ2YWwgW8W3X2xvIC0gccyCLCDFt19oaSArIHHMgl0gY292ZXJzIHRoZSB0cnVlIHkgd2l0aCBwcm9iYWJpbGl0eSBleGFjdGx5IOKJpSAxLc6xLCByZWdhcmRsZXNzIG9mIHRoZSB1bmRlcmx5aW5nIG1vZGVsIG9yIGRpc3RyaWJ1dGlvbi4gVGhlIHNjYWxhciBxzIIgaXMgY29tcHV0ZWQgb24gYSBoZWxkLW91dCBjYWxpYnJhdGlvbiBzZXQgYXMgdGhlICgxLc6xKSgxKzEvbl9jYWwpLXRoIHF1YW50aWxlIG9mIHRoZSBub24tY29uZm9ybWl0eSBzY29yZXMgbWF4KMW3X2xvIC0geSwgeSAtIMW3X2hpKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBRdWFudGlsZVJlZ3Jlc3NvclxuZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdFxuXG5ucC5yYW5kb20uc2VlZCg0Milcbm4gPSAxMDAwXG5YID0gbnAucmFuZG9tLnVuaWZvcm0oMCwgMTAsIG4pLnJlc2hhcGUoLTEsIDEpXG55ID0gMiAqIFgucmF2ZWwoKSArIG5wLnNpbihYLnJhdmVsKCkpICsgbnAucmFuZG9tLnJhbmRuKG4pICogKDAuNSArIDAuNCAqIFgucmF2ZWwoKSlcblxuWF90ciwgWF9yZXN0LCB5X3RyLCB5X3Jlc3QgPSB0cmFpbl90ZXN0X3NwbGl0KFgsIHksIHRlc3Rfc2l6ZT0wLjQsIHJhbmRvbV9zdGF0ZT00MilcblhfY2FsLCBYX3RlLCB5X2NhbCwgeV90ZSA9IHRyYWluX3Rlc3Rfc3BsaXQoWF9yZXN0LCB5X3Jlc3QsIHRlc3Rfc2l6ZT0wLjUsIHJhbmRvbV9zdGF0ZT00MilcblxuYWxwaGFfbGV2ZWwgPSAwLjEgICMgdGFyZ2V0IDkwJSBjb3ZlcmFnZVxudGF1X2xvLCB0YXVfaGkgPSBhbHBoYV9sZXZlbCAvIDIsIDEgLSBhbHBoYV9sZXZlbCAvIDJcblxucXJfbG8gPSBRdWFudGlsZVJlZ3Jlc3NvcihxdWFudGlsZT10YXVfbG8sIGFscGhhPTAuMDEsIHNvbHZlcj1cdTAwMjdoaWdoc1x1MDAyNykuZml0KFhfdHIsIHlfdHIpXG5xcl9oaSA9IFF1YW50aWxlUmVncmVzc29yKHF1YW50aWxlPXRhdV9oaSwgYWxwaGE9MC4wMSwgc29sdmVyPVx1MDAyN2hpZ2hzXHUwMDI3KS5maXQoWF90ciwgeV90cilcblxuIyBOb24tY29uZm9ybWl0eSBzY29yZXMgb24gY2FsaWJyYXRpb24gc2V0XG5zY29yZXMgPSBucC5tYXhpbXVtKHFyX2xvLnByZWRpY3QoWF9jYWwpIC0geV9jYWwsXG4gICAgICAgICAgICAgICAgICAgICB5X2NhbCAtIHFyX2hpLnByZWRpY3QoWF9jYWwpKVxuXG4jIENvbmZvcm1hbCBxdWFudGlsZSB0aHJlc2hvbGRcbm5fY2FsID0gbGVuKHlfY2FsKVxucV9oYXQgPSBucC5xdWFudGlsZShzY29yZXMsIG5wLmNlaWwoKDEtYWxwaGFfbGV2ZWwpKihuX2NhbCsxKSkvbl9jYWwpXG5cbiMgVGVzdCBjb3ZlcmFnZSB3aXRoIGNvbmZvcm1hbCBhZGp1c3RtZW50XG55X2xvID0gcXJfbG8ucHJlZGljdChYX3RlKSAtIHFfaGF0XG55X2hpID0gcXJfaGkucHJlZGljdChYX3RlKSArIHFfaGF0XG5jb3ZlcmFnZSA9ICgoeV90ZSBcdTAwM2U9IHlfbG8pIFx1MDAyNiAoeV90ZSBcdTAwM2M9IHlfaGkpKS5tZWFuKClcbndpZHRoICAgID0gKHlfaGkgLSB5X2xvKS5tZWFuKClcbnByaW50KGZcdTAwMjdUYXJnZXQgY292ZXJhZ2U6IHsxLWFscGhhX2xldmVsOi4yZn1cdTAwMjcpXG5wcmludChmXHUwMDI3Q1FSIGNvdmVyYWdlOiAgICB7Y292ZXJhZ2U6LjRmfSAgKGd1YXJhbnRlZWQgXHUwMDNlPSB7MS1hbHBoYV9sZXZlbH0pXHUwMDI3KVxucHJpbnQoZlx1MDAyN01lYW4gUEkgd2lkdGg6ICAge3dpZHRoOi4zZn1cdTAwMjcpXG5wcmludChmXHUwMDI3Q29uZm9ybWFsIHFfaGF0OiB7cV9oYXQ6LjNmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcHBsaWNhdGlvbnMgYW5kIFByYWN0aWNhbCBOb3RlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUXVhbnRpbGUgcmVncmVzc2lvbiBpcyBlc3NlbnRpYWwgaW4gZGVtYW5kIGZvcmVjYXN0aW5nOiB0aGUgODB0aCBwZXJjZW50aWxlIHByZWRpY3Rpb24gZGV0ZXJtaW5lcyBzYWZldHkgc3RvY2sgaW4gaW52ZW50b3J5IG1hbmFnZW1lbnQuIEluIGZpbmFuY2lhbCByaXNrIG1hbmFnZW1lbnQsIHRoZSA1dGggcGVyY2VudGlsZSBvZiBwb3J0Zm9saW8gcmV0dXJuIGRpc3RyaWJ1dGlvbiBpcyB0aGUgVmFsdWUtYXQtUmlzayAoVmFSKS4gRm9yIExMTSBvdXRwdXQgdW5jZXJ0YWludHksIHF1YW50aWxlIHJlZ3Jlc3Npb24gb3ZlciB0b2tlbi1sZXZlbCB1bmNlcnRhaW50eSBzY29yZXMgcHJvZHVjZXMgY2FsaWJyYXRlZCBwcmVkaWN0aW9uIGJhbmRzIHdpdGhvdXQgYSBCYXllc2lhbiBwcmlvci4gQSBrZXkgYWR2YW50YWdlIG92ZXIgbWVhbiByZWdyZXNzaW9uOiBxdWFudGlsZSByZWdyZXNzaW9uIGlzIHJvYnVzdCB0byBvdXRsaWVycyBhbmQgc2tld2VkIGRpc3RyaWJ1dGlvbnMsIHNpbmNlIHRoZSBwaW5iYWxsIGxvc3MgaXMgYm91bmRlZCBieSB0aGUgb3V0bGllclx1MDAyN3MgZGlzdGFuY2UgdG8gdGhlIHF1YW50aWxlIGxldmVsLCBub3QgaXRzIHNxdWFyZWQgZGlzdGFuY2UuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkNvdmVyYWdlIEd1YXJhbnRlZSIsIkNvbXB1dGF0aW9uIiwiQXNzdW1wdGlvbiIsIkJlc3QgVXNlIENhc2UiXSwicm93cyI6W1siUXVhbnRpbGUgUmVncmVzc2lvbiAobGluZWFyKSIsIkFwcHJveGltYXRlIChsYXJnZSBuKSIsIkxQIHNvbHZlciwgZmFzdCIsIkxpbmVhciBjb25kaXRpb25hbCBxdWFudGlsZSIsIkludGVycHJldGFibGUgcXVhbnRpbGUgZXN0aW1hdGVzLCBmZWF0dXJlIGVmZmVjdHMiXSxbIkdCIFF1YW50aWxlIFJlZ3Jlc3Npb24iLCJBcHByb3hpbWF0ZSIsIk1vZGVyYXRlIChib29zdGluZykiLCJTbW9vdGggY29uZGl0aW9uYWwgcXVhbnRpbGUiLCJOb25saW5lYXIgaGV0ZXJvc2NlZGFzdGljIGRhdGEiXSxbIkNvbmZvcm1hbCBRUiAoQ1FSKSIsIkV4YWN0IGZpbml0ZS1zYW1wbGUgKG1hcmdpbmFsKSIsIlJlcXVpcmVzIGNhbGlicmF0aW9uIHNldCIsIkV4Y2hhbmdlYWJsZSAoaWlkKSBkYXRhIiwiV2hlbiBjb3ZlcmFnZSBndWFyYW50ZWUgaXMgbGVnYWxseSBvciBwcmFjdGljYWxseSByZXF1aXJlZCJdLFsiQmF5ZXNpYW4gcHJlZGljdGlvbiBpbnRlcnZhbCIsIkFwcHJveGltYXRlIChwb3N0ZXJpb3IpIiwiTUNNQyBvciBWSSIsIlByaW9yICsgbGlrZWxpaG9vZCBjb3JyZWN0IiwiRnVsbCB1bmNlcnRhaW50eSBkZWNvbXBvc2l0aW9uLCBzbWFsbCBkYXRhIl0sWyJCb290c3RyYXAgUEkiLCJBcHByb3hpbWF0ZSIsIkIgbW9kZWwgcmVmaXRzIiwiQXN5bXB0b3RpYywgaWlkIiwiU2ltcGxlLCBtb2RlbC1hZ25vc3RpYyB1bmNlcnRhaW50eSBlc3RpbWF0aW9uIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkNoZWNrIGVtcGlyaWNhbCBjb3ZlcmFnZSBvbiBhIGhlbGQtb3V0IHNldDogaWYgZnJhY3Rpb24gYmVsb3cgXHUwMDNjIHRhdSwgdGhlIG1vZGVsIHVuZGVyZXN0aW1hdGVzIHRoYXQgcXVhbnRpbGUuIiwiVXNlIEdyYWRpZW50Qm9vc3RpbmdSZWdyZXNzb3IobG9zcz1cdTAwMjdxdWFudGlsZVx1MDAyNywgYWxwaGE9dGF1KSBmb3Igbm9ubGluZWFyIGhldGVyb3NjZWRhc3RpYyBkYXRhLiIsIkZpdCBtdWx0aXBsZSBxdWFudGlsZXMgYW5kIGFwcGx5IGlzb3RvbmljIHJlZ3Jlc3Npb24gcGVyIHNhbXBsZSB0byBwcmV2ZW50IGNyb3NzaW5nIGFydGlmYWN0cy4iLCJDb25mb3JtYWwgUVIgZ2l2ZXMgdGhlIG9ubHkgZGlzdHJpYnV0aW9uLWZyZWUgZmluaXRlLXNhbXBsZSBjb3ZlcmFnZSBndWFyYW50ZWUg4oCUIHVzZSBpdCB3aGVuIGNvdmVyYWdlIGlzIGNyaXRpY2FsLiIsInRhdT0wLjUgKG1lZGlhbiByZWdyZXNzaW9uKSBpcyByb2J1c3QgdG8gb3V0bGllcnM7IHByZWZlciBvdmVyIE9MUyB3aGVuIGhlYXZ5LXRhaWxlZCBlcnJvcnMgYXJlIGV4cGVjdGVkLiIsIkZvciB0aW1lIHNlcmllcyBxdWFudGlsZSBmb3JlY2FzdGluZywgdXNlIHF1YW50aWxlIHJlZ3Jlc3Npb24gZm9yZXN0cyBvciBBUklNQS1xdWFudGlsZSBtb2RlbHMgZm9yIHRlbXBvcmFsIGRlcGVuZGVuY2UuIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJNZWRpYW4gUmVncmVzc2lvbiBpcyBSb2J1c3QgdG8gT3V0bGllcnMiLCJjb250ZW50IjoiUXVhbnRpbGUgcmVncmVzc2lvbiBhdCB0YXU9MC41IChtZWRpYW4gcmVncmVzc2lvbikgaXMgZXF1aXZhbGVudCB0byBMMSByZWdyZXNzaW9uIGFuZCBpcyBoaWdobHkgcm9idXN0IHRvIG91dGxpZXJzIGluIHkuIFdoaWxlIE9MUyBtaW5pbWlzZXMgc3VtIG9mIHNxdWFyZWQgcmVzaWR1YWxzIChnaXZpbmcgb3V0bGllcnMgcXVhZHJhdGljIGluZmx1ZW5jZSksIG1lZGlhbiByZWdyZXNzaW9uIG1pbmltaXNlcyBzdW0gb2YgYWJzb2x1dGUgcmVzaWR1YWxzIChsaW5lYXIgaW5mbHVlbmNlKS4gQSBzaW5nbGUgb3V0bGllciB3aXRoIHkgYXBwcm9hY2hpbmcgaW5maW5pdHkgd2lsbCBub3Qgc2hpZnQgdGhlIG1lZGlhbiByZWdyZXNzaW9uIGxpbmUgaWYgaXQgcmVwcmVzZW50cyBsZXNzIHRoYW4gNTAlIG9mIHRoZSBkYXRhLiBVc2UgbWVkaWFuIHJlZ3Jlc3Npb24gYXMgYSByb2J1c3QgYWx0ZXJuYXRpdmUgdG8gT0xTIHdoZW4gdGhlIHJlc3BvbnNlIGhhcyBoZWF2eS10YWlsZWQgbm9pc2Ugb3IgbWVhc3VyZW1lbnQgZXJyb3JzLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2ltdWx0YW5lb3VzIHF1YW50aWxlIHJlZ3Jlc3Npb24gZml0cyBhbGwgcXVhbnRpbGUgbGV2ZWxzIChlLmcuLCB0YXUgaW4gezAuMDUsIDAuMTAsIC4uLiwgMC45NX0pIHVzaW5nIGEgc2luZ2xlIHNoYXJlZCBtb2RlbCDigJQgZm9yIGV4YW1wbGUsIGEgbmV1cmFsIG5ldHdvcmsgd2l0aCBhIG11bHRpLW91dHB1dCBoZWFkIHdoZXJlIGVhY2ggb3V0cHV0IGNvcnJlc3BvbmRzIHRvIG9uZSB0YXUgdmFsdWUuIFRoaXMgYXBwcm9hY2ggbmF0dXJhbGx5IHJlZHVjZXMgY3Jvc3NpbmcgYXJ0aWZhY3RzIGJlY2F1c2UgdGhlIG1vZGVsIHNoYXJlcyByZXByZXNlbnRhdGlvbnMgYWNyb3NzIHF1YW50aWxlIGxldmVscywgYW5kIGV4cGxpY2l0IG5vbi1jcm9zc2luZyBwZW5hbHRpZXMgY2FuIGJlIGFkZGVkIHRvIHRoZSBqb2ludCB0cmFpbmluZyBsb3NzLiBGb3IgZ3JhZGllbnQgYm9vc3RlZCB0cmVlcywgZml0IGVhY2ggdGF1IHNlcGFyYXRlbHkgd2l0aCBHcmFkaWVudEJvb3N0aW5nUmVncmVzc29yKGxvc3M9XHUwMDI3cXVhbnRpbGVcdTAwMjcsIGFscGhhPXRhdSkgYW5kIGFwcGx5IGlzb3RvbmljIHJlZ3Jlc3Npb24gcG9zdC1ob2MgdG8gZW5mb3JjZSBtb25vdG9uaWNpdHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJRdWFudGlsZSByZWdyZXNzaW9uIGZvcmVzdHMgKE1laW5zaGF1c2VuIDIwMDYpIGV4dGVuZCByYW5kb20gZm9yZXN0cyB0byBjb25kaXRpb25hbCBxdWFudGlsZSBlc3RpbWF0aW9uLiBJbnN0ZWFkIG9mIGF2ZXJhZ2luZyBsZWFmIHByZWRpY3Rpb25zLCBxdWFudGlsZSByZWdyZXNzaW9uIGZvcmVzdHMgY29tcHV0ZSB0aGUgZW1waXJpY2FsIHRhdS10aCBxdWFudGlsZSBvZiB0cmFpbmluZyBsYWJlbHMgcmVhY2hpbmcgZWFjaCBsZWFmLiBGb3IgYSBxdWVyeSB4LCB0aGUgZm9yZXN0IHJvdXRlcyB4IHRvIGEgbGVhZiBpbiBlYWNoIHRyZWUsIGNvbGxlY3RzIGFsbCB0cmFpbmluZyBsYWJlbHMgZnJvbSB0aG9zZSBsZWF2ZXMsIGFuZCByZXR1cm5zIHRoZSB0YXUtdGggZW1waXJpY2FsIHF1YW50aWxlLiBUaGlzIGlzIGRpc3RyaWJ1dGlvbi1mcmVlIChubyBwYXJhbWV0cmljIGZvcm0gYXNzdW1lZCBmb3IgcCh5fHgpKSwgbmF0dXJhbGx5IGhhbmRsZXMgaGV0ZXJvc2NlZGFzdGljaXR5IGFuZCBtdWx0aW1vZGFsIGNvbmRpdGlvbmFsIGRpc3RyaWJ1dGlvbnMsIGFuZCBpcyBvbmUgb2YgdGhlIG1vc3Qgcm9idXN0IG5vbmxpbmVhciBxdWFudGlsZSBlc3RpbWF0b3JzIGF2YWlsYWJsZSB3aXRob3V0IHJlcXVpcmluZyBncmFkaWVudCBib29zdGVkIHRyZWVzLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Quantile Regression — Conditional Quantile Estimation

Ordinary least squares estimates the conditional mean E[Y|X=x]. Quantile regression estimates any conditional quantile Q_τ(Y|X=x) for τ ∈ (0,1) — for example, the 90th percentile of house prices given square footage, or the 5th percentile of daily returns for VaR. This provides a complete picture of the conditional distribution: how does the spread, skewness, and tail behaviour change with X? Applications include demand forecasting (upper quantile for inventory planning), risk management (Value-at-Risk), and uncertainty quantification for machine learning predictions.

## The Pinball (Tilted L1) Loss

Quantile regression minimises the pinball loss: ρ_τ(u) = u·τ if u ≥ 0 (underprediction), u·(τ-1) if u < 0 (overprediction). For τ=0.9, underprediction is penalised 9x more than overprediction — this asymmetry forces the optimal prediction to be the 90th percentile. At the optimum, exactly τ·n of the residuals are positive and (1-τ)·n are negative: exactly the definition of the τ-th sample quantile. For τ=0.5, the loss reduces to |u|/2, the L1 loss — so median regression is a special case. Unlike OLS, pinball loss is robust to outliers on the heavy tail.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

def pinball_loss(y_true, y_pred, tau):
    residuals = y_true - y_pred
    return np.where(residuals >= 0, tau * residuals, (tau - 1) * residuals).mean()

class QuantileRegressionGD:
    """Quantile regression via subgradient descent on pinball loss."""
    def __init__(self, tau=0.5, lr=0.01, n_iter=2000):
        self.tau = tau
        self.lr = lr
        self.n_iter = n_iter

    def fit(self, X, y):
        n, p = X.shape
        X_b = np.hstack([np.ones((n, 1)), X])
        self.w_ = np.zeros(X_b.shape[1])
        for _ in range(self.n_iter):
            resid = y - X_b @ self.w_
            subgrad = np.where(resid >= 0, -self.tau, -(self.tau - 1))
            self.w_ -= self.lr * (X_b.T @ subgrad) / n
        return self

    def predict(self, X):
        X_b = np.hstack([np.ones((len(X), 1)), X])
        return X_b @ self.w_

np.random.seed(42)
X, y = make_regression(n_samples=300, n_features=3, noise=20.0, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)

for tau in [0.1, 0.5, 0.9]:
    qr = QuantileRegressionGD(tau=tau, lr=0.005, n_iter=3000).fit(X_tr, y_tr)
    pbl = pinball_loss(y_te, qr.predict(X_te), tau)
    coverage = (y_te < qr.predict(X_te)).mean()
    print(f'tau={tau}: pinball_loss={pbl:.3f}, empirical_coverage={coverage:.3f} (target={tau})')
```

## Sklearn QuantileRegressor and Gradient Boosting Quantiles

sklearn's QuantileRegressor (added in 1.0) solves quantile regression exactly as a linear program using interior point methods — far more numerically stable than gradient descent. The alpha parameter adds L1 regularisation on the weights. For nonlinear quantile regression, GradientBoostingRegressor with loss='quantile', alpha=tau fits gradient boosted trees targeting the pinball loss, enabling flexible nonlinear conditional quantile estimation. Simultaneous quantile regression fits multiple τ values, often with a single shared model backbone, to produce consistent prediction intervals.

```python
import numpy as np
from sklearn.linear_model import QuantileRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

np.random.seed(42)
n = 500
X_1d = np.random.uniform(0, 10, n).reshape(-1, 1)
# Heteroscedastic: variance increases with X
y = 2 * X_1d.ravel() + np.random.randn(n) * (0.5 + 0.3 * X_1d.ravel())
X_tr, X_te, y_tr, y_te = train_test_split(X_1d, y, test_size=0.25, random_state=42)

models = {}
for tau in [0.1, 0.5, 0.9]:
    qr = QuantileRegressor(quantile=tau, alpha=0.1, solver='highs')
    qr.fit(X_tr, y_tr)
    models[tau] = qr
    coverage = (y_te < qr.predict(X_te)).mean()
    print(f'Linear QR  tau={tau}: coverage={coverage:.3f} (target {tau:.1f})')

# Gradient boosting for nonlinear quantile estimation
gb90 = GradientBoostingRegressor(loss='quantile', alpha=0.9, n_estimators=200, random_state=42)
gb90.fit(X_tr, y_tr)
print(f'GB QR  tau=0.9: coverage={(y_te < gb90.predict(X_te)).mean():.3f}')

lower = models[0.1].predict(X_te)
upper = models[0.9].predict(X_te)
print(f'80% PI coverage: {((y_te >= lower) & (y_te <= upper)).mean():.3f} (target 0.80)')
```

## Quantile Crossing and Isotonic Regression Fix

When fitting quantile models at multiple τ values independently, their predictions can cross: the 90th percentile prediction can be lower than the 80th percentile for some x values. This is statistically incoherent — quantile functions Q_τ(Y|X=x) must be non-decreasing in τ for each x. The standard fix is isotonic regression: after obtaining raw predictions at all τ values for each test point, apply isotonic regression across τ to enforce monotonicity. This is a post-processing step with O(K log K) cost per sample where K is the number of quantile levels.

> **Quantile Crossing is a Silent Bug**: Crossed quantiles (e.g., Q_90 < Q_80 for some x) produce prediction intervals with negative width — a silent bug that invalidates all downstream calculations. Always check for crossings after fitting multiple quantiles independently. Apply isotonic regression or use non-crossing quantile regression variants (joint optimisation with ordering constraints). sklearn's QuantileRegressor is particularly prone to crossing for small datasets or high regularisation.

```python
import numpy as np
from sklearn.linear_model import QuantileRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)
n = 300
X = np.random.uniform(0, 10, n).reshape(-1, 1)
y = 3 * X.ravel() + np.random.randn(n) * (1 + 0.5 * X.ravel())
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)

taus = np.linspace(0.05, 0.95, 19)
preds_raw = np.zeros((len(X_te), len(taus)))

for j, tau in enumerate(taus):
    qr = QuantileRegressor(quantile=tau, alpha=0.01, solver='highs')
    qr.fit(X_tr, y_tr)
    preds_raw[:, j] = qr.predict(X_te)

crossings_before = np.sum(np.diff(preds_raw, axis=1) < 0)
print(f'Quantile crossings before isotonic: {crossings_before}')

# Apply isotonic regression per sample to enforce tau-monotonicity
preds_iso = np.zeros_like(preds_raw)
iso = IsotonicRegression(increasing=True)
for i in range(len(X_te)):
    preds_iso[i] = iso.fit_transform(taus, preds_raw[i])

crossings_after = np.sum(np.diff(preds_iso, axis=1) < 0)
print(f'Quantile crossings after isotonic:  {crossings_after}')
```

## Conformal Quantile Regression for Guaranteed Coverage

Standard quantile regression targets Q_τ(Y|X=x) but provides no finite-sample coverage guarantee — coverage is only approximate, especially with limited data or model misspecification. Conformal Quantile Regression (CQR, Romano et al. 2019) provides a distribution-free, finite-sample guarantee: the interval [ŷ_lo - q̂, ŷ_hi + q̂] covers the true y with probability exactly ≥ 1-α, regardless of the underlying model or distribution. The scalar q̂ is computed on a held-out calibration set as the (1-α)(1+1/n_cal)-th quantile of the non-conformity scores max(ŷ_lo - y, y - ŷ_hi).

```python
import numpy as np
from sklearn.linear_model import QuantileRegressor
from sklearn.model_selection import train_test_split

np.random.seed(42)
n = 1000
X = np.random.uniform(0, 10, n).reshape(-1, 1)
y = 2 * X.ravel() + np.sin(X.ravel()) + np.random.randn(n) * (0.5 + 0.4 * X.ravel())

X_tr, X_rest, y_tr, y_rest = train_test_split(X, y, test_size=0.4, random_state=42)
X_cal, X_te, y_cal, y_te = train_test_split(X_rest, y_rest, test_size=0.5, random_state=42)

alpha_level = 0.1  # target 90% coverage
tau_lo, tau_hi = alpha_level / 2, 1 - alpha_level / 2

qr_lo = QuantileRegressor(quantile=tau_lo, alpha=0.01, solver='highs').fit(X_tr, y_tr)
qr_hi = QuantileRegressor(quantile=tau_hi, alpha=0.01, solver='highs').fit(X_tr, y_tr)

# Non-conformity scores on calibration set
scores = np.maximum(qr_lo.predict(X_cal) - y_cal,
                     y_cal - qr_hi.predict(X_cal))

# Conformal quantile threshold
n_cal = len(y_cal)
q_hat = np.quantile(scores, np.ceil((1-alpha_level)*(n_cal+1))/n_cal)

# Test coverage with conformal adjustment
y_lo = qr_lo.predict(X_te) - q_hat
y_hi = qr_hi.predict(X_te) + q_hat
coverage = ((y_te >= y_lo) & (y_te <= y_hi)).mean()
width    = (y_hi - y_lo).mean()
print(f'Target coverage: {1-alpha_level:.2f}')
print(f'CQR coverage:    {coverage:.4f}  (guaranteed >= {1-alpha_level})')
print(f'Mean PI width:   {width:.3f}')
print(f'Conformal q_hat: {q_hat:.3f}')
```

## Applications and Practical Notes

Quantile regression is essential in demand forecasting: the 80th percentile prediction determines safety stock in inventory management. In financial risk management, the 5th percentile of portfolio return distribution is the Value-at-Risk (VaR). For LLM output uncertainty, quantile regression over token-level uncertainty scores produces calibrated prediction bands without a Bayesian prior. A key advantage over mean regression: quantile regression is robust to outliers and skewed distributions, since the pinball loss is bounded by the outlier's distance to the quantile level, not its squared distance.

| Method | Coverage Guarantee | Computation | Assumption | Best Use Case |
| --- | --- | --- | --- | --- |
| Quantile Regression (linear) | Approximate (large n) | LP solver, fast | Linear conditional quantile | Interpretable quantile estimates, feature effects |
| GB Quantile Regression | Approximate | Moderate (boosting) | Smooth conditional quantile | Nonlinear heteroscedastic data |
| Conformal QR (CQR) | Exact finite-sample (marginal) | Requires calibration set | Exchangeable (iid) data | When coverage guarantee is legally or practically required |
| Bayesian prediction interval | Approximate (posterior) | MCMC or VI | Prior + likelihood correct | Full uncertainty decomposition, small data |
| Bootstrap PI | Approximate | B model refits | Asymptotic, iid | Simple, model-agnostic uncertainty estimation |

- Check empirical coverage on a held-out set: if fraction below < tau, the model underestimates that quantile.
- Use GradientBoostingRegressor(loss='quantile', alpha=tau) for nonlinear heteroscedastic data.
- Fit multiple quantiles and apply isotonic regression per sample to prevent crossing artifacts.
- Conformal QR gives the only distribution-free finite-sample coverage guarantee — use it when coverage is critical.
- tau=0.5 (median regression) is robust to outliers; prefer over OLS when heavy-tailed errors are expected.
- For time series quantile forecasting, use quantile regression forests or ARIMA-quantile models for temporal dependence.

> **Median Regression is Robust to Outliers**: Quantile regression at tau=0.5 (median regression) is equivalent to L1 regression and is highly robust to outliers in y. While OLS minimises sum of squared residuals (giving outliers quadratic influence), median regression minimises sum of absolute residuals (linear influence). A single outlier with y approaching infinity will not shift the median regression line if it represents less than 50% of the data. Use median regression as a robust alternative to OLS when the response has heavy-tailed noise or measurement errors.

Simultaneous quantile regression fits all quantile levels (e.g., tau in {0.05, 0.10, ..., 0.95}) using a single shared model — for example, a neural network with a multi-output head where each output corresponds to one tau value. This approach naturally reduces crossing artifacts because the model shares representations across quantile levels, and explicit non-crossing penalties can be added to the joint training loss. For gradient boosted trees, fit each tau separately with GradientBoostingRegressor(loss='quantile', alpha=tau) and apply isotonic regression post-hoc to enforce monotonicity.

Quantile regression forests (Meinshausen 2006) extend random forests to conditional quantile estimation. Instead of averaging leaf predictions, quantile regression forests compute the empirical tau-th quantile of training labels reaching each leaf. For a query x, the forest routes x to a leaf in each tree, collects all training labels from those leaves, and returns the tau-th empirical quantile. This is distribution-free (no parametric form assumed for p(y|x)), naturally handles heteroscedasticity and multimodal conditional distributions, and is one of the most robust nonlinear quantile estimators available without requiring gradient boosted trees.

---

