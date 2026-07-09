---
title: "Bias-Variance Tradeoff"
slug: "bias-variance-tradeoff"
description: "Derive the bias-variance decomposition of expected test error, visualise the U-shaped error curve, demonstrate double descent in overparameterised models, and show how bagging and boosting each address one side of the tradeoff."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRXZlcnkgc3VwZXJ2aXNlZCBsZWFybmluZyBtb2RlbCBtYWtlcyBhbiBlcnJvciB0aGF0IGNhbiBiZSBkZWNvbXBvc2VkIGludG8gdGhyZWUgb3J0aG9nb25hbCBjb21wb25lbnRzOiBiaWFzIChzeXN0ZW1hdGljIGVycm9yIGZyb20gbW9kZWwgYXNzdW1wdGlvbnMpLCB2YXJpYW5jZSAoc2Vuc2l0aXZpdHkgdG8gdGhlIHNwZWNpZmljIHRyYWluaW5nIHNldCBkcmF3biksIGFuZCBpcnJlZHVjaWJsZSBub2lzZSAoaW5oZXJlbnQgcmFuZG9tbmVzcyBpbiB0aGUgZGF0YS1nZW5lcmF0aW5nIHByb2Nlc3MpLiBVbmRlcnN0YW5kaW5nIHRoaXMgZGVjb21wb3NpdGlvbiBleHBsYWlucyB3aHkgc2ltcGxlIG1vZGVscyB1bmRlcmZpdCwgY29tcGxleCBtb2RlbHMgb3ZlcmZpdCwgYW5kIGhvdyByZWd1bGFyaXNhdGlvbiwgZW5zZW1ibGVzLCBhbmQgbGFyZ2VyIGRhdGFzZXRzIGhlbHAg4oCUIGVhY2ggdGFyZ2V0aW5nIGEgZGlmZmVyZW50IGNvbXBvbmVudC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZXJpdmluZyB0aGUgQmlhcy1WYXJpYW5jZSBEZWNvbXBvc2l0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMZXQgZih4KSBiZSB0aGUgdHJ1ZSBmdW5jdGlvbiwgxbcoeCkgdGhlIG1vZGVsIHByZWRpY3Rpb24gKGEgcmFuZG9tIHZhcmlhYmxlIG92ZXIgdHJhaW5pbmcgc2V0cyksIGFuZCDOtSB+IE4oMCzPg8KyKSBpcnJlZHVjaWJsZSBub2lzZS4gVGhlIGV4cGVjdGVkIHNxdWFyZWQgZXJyb3IgYXQgYSBwb2ludCB4IGRlY29tcG9zZXMgYXM6IEVbKHkg4oiSIMW3KcKyXSA9IEVbKGYoeCkgKyDOtSDiiJIgxbcpwrJdLiBBZGQgYW5kIHN1YnRyYWN0IEVbxbddOiA9IEVbKGYoeCkg4oiSIEVbxbddKcKyXSArIEVbKEVbxbddIOKIkiDFtynCsl0gKyDPg8KyID0gQmlhc8KyKMW3KSArIFZhcijFtykgKyDPg8KyLiBUaGUgY3Jvc3MgdGVybXMgdmFuaXNoIGJlY2F1c2UgzrUgaXMgaW5kZXBlbmRlbnQgb2YgxbcgYW5kIEVbzrVdPTAuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCaWFzID0gRVvFt10g4oiSIGYoeCkgaXMgdGhlIGF2ZXJhZ2UgZGlmZmVyZW5jZSBiZXR3ZWVuIG1vZGVsIHByZWRpY3Rpb25zIGFuZCB0aGUgdHJ1ZSBmdW5jdGlvbiDigJQgaXQgaXMgemVybyBmb3IgYSBtb2RlbCBmbGV4aWJsZSBlbm91Z2ggdG8gcmVwcmVzZW50IGYgZXhhY3RseS4gVmFyaWFuY2UgPSBFWyjFtyDiiJIgRVvFt10pwrJdIG1lYXN1cmVzIGhvdyBtdWNoIHRoZSBtb2RlbCBmbHVjdHVhdGVzIGFjcm9zcyBkaWZmZXJlbnQgdHJhaW5pbmcgc2V0cyBvZiB0aGUgc2FtZSBzaXplLiBBIGhpZ2gtY2FwYWNpdHkgbW9kZWwgKGRlZXAgdHJlZSwgaGlnaC1kZWdyZWUgcG9seW5vbWlhbCkgZml0cyBlYWNoIHRyYWluaW5nIHNldCBjbG9zZWx5OiBsb3cgYmlhcywgaGlnaCB2YXJpYW5jZS4gQSBzaW1wbGUgbW9kZWwgKGNvbnN0YW50LCBsaW5lYXIgd2l0aCBmZXcgZmVhdHVyZXMpOiBoaWdoIGJpYXMsIGxvdyB2YXJpYW5jZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTaW11bGF0aW5nIHRoZSBEZWNvbXBvc2l0aW9uIHZpYSBCb290c3RyYXAifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRvIGVtcGlyaWNhbGx5IGVzdGltYXRlIGJpYXMgYW5kIHZhcmlhbmNlLCByZXBlYXRlZGx5IGRyYXcgQiB0cmFpbmluZyBzZXRzIGZyb20gdGhlIHNhbWUgZGlzdHJpYnV0aW9uLCB0cmFpbiB0aGUgbW9kZWwgb24gZWFjaCwgYW5kIGV2YWx1YXRlIG9uIGEgZml4ZWQgdGVzdCBzZXQuIFRoZSBhdmVyYWdlIHByZWRpY3Rpb24gb3ZlciBCIG1vZGVscyBlc3RpbWF0ZXMgRVvFt107IHRoZSB2YXJpYW5jZSBvZiBwcmVkaWN0aW9ucyBlc3RpbWF0ZXMgVmFyKMW3KTsgdGhlIHNxdWFyZWQgZ2FwIGJldHdlZW4gdGhlIGF2ZXJhZ2UgcHJlZGljdGlvbiBhbmQgdGhlIHRydWUgZnVuY3Rpb24gZXN0aW1hdGVzIEJpYXPCsi4gVGhpcyBpcyBjb21wdXRhdGlvbmFsbHkgaW50ZW5zaXZlIGJ1dCBnaXZlcyBleGFjdCBlbXBpcmljYWwgZXN0aW1hdGVzIGZvciBhbnkgbW9kZWwgY2xhc3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnRyZWUgaW1wb3J0IERlY2lzaW9uVHJlZVJlZ3Jlc3NvclxuXG5kZWYgYmlhc192YXJpYW5jZV9kZWNvbXAobWF4X2RlcHRoLCBuX2Jvb3RzdHJhcHM9MjAwLCBuX3RyYWluPTYwLFxuICAgICAgICAgICAgICAgICAgICAgICAgICBuX3Rlc3Q9NDAwLCBub2lzZT0wLjUsIHNlZWQ9MCk6XG4gICAgcm5nID0gbnAucmFuZG9tLlJhbmRvbVN0YXRlKHNlZWQpXG4gICAgWF90ZXN0ID0gbnAubGluc3BhY2UoLTMsIDMsIG5fdGVzdCkucmVzaGFwZSgtMSwgMSlcbiAgICBmX3RydWUgPSBucC5zaW4oWF90ZXN0KS5yYXZlbCgpXG4gICAgcHJlZHMgPSBucC56ZXJvcygobl9ib290c3RyYXBzLCBuX3Rlc3QpKVxuICAgIGZvciBiIGluIHJhbmdlKG5fYm9vdHN0cmFwcyk6XG4gICAgICAgIFhfdHIgPSBybmcudW5pZm9ybSgtMywgMywgbl90cmFpbikucmVzaGFwZSgtMSwgMSlcbiAgICAgICAgeV90ciA9IG5wLnNpbihYX3RyKS5yYXZlbCgpICsgcm5nLnJhbmRuKG5fdHJhaW4pICogbm9pc2VcbiAgICAgICAgbW9kZWwgPSBEZWNpc2lvblRyZWVSZWdyZXNzb3IobWF4X2RlcHRoPW1heF9kZXB0aClcbiAgICAgICAgbW9kZWwuZml0KFhfdHIsIHlfdHIpXG4gICAgICAgIHByZWRzW2JdID0gbW9kZWwucHJlZGljdChYX3Rlc3QpXG4gICAgbWVhbl9wcmVkID0gcHJlZHMubWVhbihheGlzPTApXG4gICAgYmlhc19zcSAgPSBucC5tZWFuKChtZWFuX3ByZWQgLSBmX3RydWUpICoqIDIpXG4gICAgdmFyaWFuY2UgID0gbnAubWVhbihwcmVkcy52YXIoYXhpcz0wKSlcbiAgICBub2lzZV9zcSAgPSBub2lzZSAqKiAyXG4gICAgcmV0dXJuIGJpYXNfc3EsIHZhcmlhbmNlLCBub2lzZV9zcVxuXG5wcmludChmXHUwMDI3e1wiRGVwdGhcIjpcdTAwM2U2fSB7XCJCaWFzXjJcIjpcdTAwM2U4fSB7XCJWYXJcIjpcdTAwM2U4fSB7XCJOb2lzZVwiOlx1MDAzZTh9IHtcIlRvdGFsXCI6XHUwMDNlOH1cdTAwMjcpXG5mb3IgZGVwdGggaW4gWzEsIDIsIDQsIDgsIDE2XTpcbiAgICBiMiwgdiwgbiA9IGJpYXNfdmFyaWFuY2VfZGVjb21wKGRlcHRoKVxuICAgIHByaW50KGZcdTAwMjd7ZGVwdGg6XHUwMDNlNn0ge2IyOlx1MDAzZTguNGZ9IHt2Olx1MDAzZTguNGZ9IHtuOlx1MDAzZTguNGZ9IHtiMit2K246XHUwMDNlOC40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGVzdCBFcnJvciBDdXJ2ZSB2cyBNb2RlbCBDb21wbGV4aXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBcyBtb2RlbCBjb21wbGV4aXR5IGluY3JlYXNlcyAoZS5nLiwgcG9seW5vbWlhbCBkZWdyZWUsIHRyZWUgZGVwdGgsIG5ldHdvcmsgd2lkdGgpLCB0cmFpbmluZyBlcnJvciBtb25vdG9uaWNhbGx5IGRlY3JlYXNlcyB3aGlsZSB0ZXN0IGVycm9yIGZvbGxvd3MgYSBVLXNoYXBlOiBoaWdoICh1bmRlcmZpdHRpbmcpIGZvciBzaW1wbGUgbW9kZWxzLCBtaW5pbXVtIGF0IG9wdGltYWwgY29tcGxleGl0eSwgcmlzaW5nIGFnYWluIChvdmVyZml0dGluZykgZm9yIGNvbXBsZXggbW9kZWxzLiBUaGUgZ2FwIGJldHdlZW4gdHJhaW5pbmcgYW5kIHRlc3QgZXJyb3IgaXMgYXBwcm94aW1hdGVseSAyIMOXIFZhcmlhbmNlIC8gbiBmb3IgbWFueSBtb2RlbCBjbGFzc2VzLiBDcm9zcy12YWxpZGF0aW9uIGVzdGltYXRlcyB0aGUgdGVzdCBlcnJvciBjdXJ2ZSB3aXRob3V0IHJlcXVpcmluZyBhIGhvbGRvdXQgc2V0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5waXBlbGluZSBpbXBvcnQgUGlwZWxpbmVcbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBQb2x5bm9taWFsRmVhdHVyZXNcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IExpbmVhclJlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5tb2RlbF9zZWxlY3Rpb24gaW1wb3J0IGNyb3NzX3ZhbF9zY29yZVxuXG5ucC5yYW5kb20uc2VlZCgwKVxuWCA9IG5wLnJhbmRvbS51bmlmb3JtKC0zLCAzLCAxMjApLnJlc2hhcGUoLTEsIDEpXG55ID0gbnAuc2luKFgpLnJhdmVsKCkgKyAwLjQgKiBucC5yYW5kb20ucmFuZG4oMTIwKVxuXG5kZWdyZWVzID0gcmFuZ2UoMSwgMTYpXG50cmFpbl9lcnJzLCBjdl9lcnJzID0gW10sIFtdXG5mb3IgZCBpbiBkZWdyZWVzOlxuICAgIHBpcGUgPSBQaXBlbGluZShbXG4gICAgICAgIChcdTAwMjdwb2x5XHUwMDI3LCBQb2x5bm9taWFsRmVhdHVyZXMoZGVncmVlPWQsIGluY2x1ZGVfYmlhcz1GYWxzZSkpLFxuICAgICAgICAoXHUwMDI3bHJcdTAwMjcsICAgTGluZWFyUmVncmVzc2lvbigpKVxuICAgIF0pXG4gICAgY3Zfc2NvcmVzID0gY3Jvc3NfdmFsX3Njb3JlKFxuICAgICAgICBwaXBlLCBYLCB5LCBjdj01LCBzY29yaW5nPVx1MDAyN25lZ19tZWFuX3NxdWFyZWRfZXJyb3JcdTAwMjdcbiAgICApXG4gICAgcGlwZS5maXQoWCwgeSlcbiAgICB0cmFpbl9lcnJzLmFwcGVuZChucC5tZWFuKCh5IC0gcGlwZS5wcmVkaWN0KFgpKSoqMikpXG4gICAgY3ZfZXJycy5hcHBlbmQoLWN2X3Njb3Jlcy5tZWFuKCkpXG5cbmJlc3RfZCA9IGxpc3QoZGVncmVlcylbbnAuYXJnbWluKGN2X2VycnMpXVxucHJpbnQoZlx1MDAyN3tcIkRlZ1wiOlx1MDAzZTR9IHtcIlRyYWluIE1TRVwiOlx1MDAzZTEwfSB7XCJDViBNU0VcIjpcdTAwM2UxMH1cdTAwMjcpXG5mb3IgZCwgdHIsIGN2IGluIHppcChkZWdyZWVzLCB0cmFpbl9lcnJzLCBjdl9lcnJzKTpcbiAgICBtYXJrZXIgPSBcdTAwMjcgXHUwMDNjLS0gYmVzdFx1MDAyNyBpZiBkID09IGJlc3RfZCBlbHNlIFx1MDAyN1x1MDAyN1xuICAgIHByaW50KGZcdTAwMjd7ZDpcdTAwM2U0fSB7dHI6XHUwMDNlMTAuNGZ9IHtjdjpcdTAwM2UxMC40Zn17bWFya2VyfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEb3VibGUgRGVzY2VudCBQaGVub21lbm9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDbGFzc2ljYWwgc3RhdGlzdGljYWwgbGVhcm5pbmcgdGhlb3J5IHByZWRpY3RzIGEgVS1zaGFwZWQgYmlhcy12YXJpYW5jZSB0cmFkZW9mZi4gQnV0IG1vZGVybiBvdmVycGFyYW1ldGVyaXNlZCBtb2RlbHMgKGRlZXAgbmV0d29ya3MsIHJhbmRvbSBmZWF0dXJlcywga2VybmVsIG1hY2hpbmVzKSBleGhpYml0IGRvdWJsZSBkZXNjZW50OiB0ZXN0IGVycm9yIHJpc2VzIG5lYXIgdGhlIGludGVycG9sYXRpb24gdGhyZXNob2xkICh3aGVyZSBtb2RlbCBjYXBhY2l0eSDiiYggbikgYW5kIHRoZW4gZGVjcmVhc2VzIGFnYWluIGFzIGNhcGFjaXR5IGNvbnRpbnVlcyB0byBncm93LiBUaGUgbWluaW11bS1ub3JtIGludGVycG9sYXRpbmcgc29sdXRpb24gaW4gdGhlIG92ZXJwYXJhbWV0ZXJpc2VkIHJlZ2ltZSBpbXBsaWNpdGx5IHJlZ3VsYXJpc2VzLCBhY2hpZXZpbmcgbG93IHZhcmlhbmNlIGRlc3BpdGUgemVybyB0cmFpbmluZyBlcnJvci4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoeSBEb3VibGUgRGVzY2VudCBIYXBwZW5zIiwiY29udGVudCI6Ik5lYXIgdGhlIGludGVycG9sYXRpb24gdGhyZXNob2xkIHRoZSBtb2RlbCBiYXJlbHkgZml0cyB0aGUgZGF0YSDigJQgc21hbGwgcGVydHVyYmF0aW9ucyBjYXVzZSBsYXJnZSBjb2VmZmljaWVudCBzd2luZ3MgKGhpZ2ggdmFyaWFuY2UpLiBCZXlvbmQgdGhlIHRocmVzaG9sZCB0aGVyZSBhcmUgbWFueSBzb2x1dGlvbnMgdGhhdCBmaXQgcGVyZmVjdGx5OyBncmFkaWVudCBkZXNjZW50IG9yIHBzZXVkb2ludmVyc2Ugc2VsZWN0cyB0aGUgbWluaW11bS1ub3JtIG9uZSwgd2hpY2ggaXMgc21vb3RoIGFuZCBnZW5lcmFsaXNlcyB3ZWxsLiBUaGlzIGJyZWFrcyB0aGUgY2xhc3NpY2FsIFUtY3VydmUgYW5kIGNoYWxsZW5nZXMgdGhlIGJpYXMtdmFyaWFuY2UgZnJhbWluZyBmb3IgbW9kZXJuIG1vZGVscy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubl90cmFpbiA9IDUwXG5ybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoNDIpXG5YX2Z1bGwgPSBybmcucmFuZG4obl90cmFpbiwgMzAwKVxueV90cmFpbiA9IHJuZy5yYW5kbihuX3RyYWluKSAgICAgICAgICAjIHB1cmUgbm9pc2Ug4oCUIG5vIHRydWUgc2lnbmFsXG5YX3Rlc3QgID0gcm5nLnJhbmRuKDUwMCwgMzAwKVxueV90ZXN0ICA9IHJuZy5yYW5kbig1MDApXG5cbnBfdmFsdWVzID0gbGlzdChyYW5nZSg1LCAzMDAsIDUpKVxudGVzdF9tc2UgPSBbXVxuZm9yIHAgaW4gcF92YWx1ZXM6XG4gICAgWHRyID0gWF9mdWxsWzosIDpwXVxuICAgIFh0ZSA9IFhfdGVzdFs6LCA6cF1cbiAgICAjIE1pbmltdW0tbm9ybSAocHNldWRvaW52ZXJzZSkgc29sdXRpb25cbiAgICBjb2VmLCBfLCBfLCBfID0gbnAubGluYWxnLmxzdHNxKFh0ciwgeV90cmFpbiwgcmNvbmQ9Tm9uZSlcbiAgICBwcmVkID0gWHRlIEAgY29lZlxuICAgIHRlc3RfbXNlLmFwcGVuZChucC5tZWFuKCh5X3Rlc3QgLSBwcmVkKSoqMikpXG5cbnBlYWtfcCA9IHBfdmFsdWVzW2ludChucC5hcmdtYXgodGVzdF9tc2UpKV1cbnByaW50KGZcdTAwMjdJbnRlcnBvbGF0aW9uIHRocmVzaG9sZCBuID0ge25fdHJhaW59XHUwMDI3KVxucHJpbnQoZlx1MDAyN1BlYWsgdGVzdCBNU0UgYXQgcCA9IHtwZWFrX3B9OiB7bWF4KHRlc3RfbXNlKTouMmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1Rlc3QgTVNFIGF0IHA9NTogICB7dGVzdF9tc2VbMF06LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdUZXN0IE1TRSBhdCBwPTI5NToge3Rlc3RfbXNlWy0xXTouNGZ9XHUwMDI3KVxucHJpbnQoXHUwMDI3TVNFIHJpc2VzIG5lYXIgbj1wLCB0aGVuIGZhbGxzIGFnYWluIGFzIHAgXHUwMDNlXHUwMDNlIG4gKGRvdWJsZSBkZXNjZW50KS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVndWxhcmlzYXRpb24gYW5kIEVuc2VtYmxlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVndWxhcmlzYXRpb24gKEwxLCBMMiwgZHJvcG91dCwgZWFybHkgc3RvcHBpbmcpIGFkZHMgYmlhcyB0byByZWR1Y2UgdmFyaWFuY2Ug4oCUIHRyYWRpbmcgYSBzbGlnaHRseSB3cm9uZyBhbnN3ZXIgZm9yIGEgbXVjaCBtb3JlIHN0YWJsZSBvbmUuIEJhZ2dpbmcgKEJvb3RzdHJhcCBBR0dyZWdhdGluZykgYXZlcmFnZXMgcHJlZGljdGlvbnMgb3ZlciBCIG1vZGVscyB0cmFpbmVkIG9uIGJvb3RzdHJhcCBzYW1wbGVzLCByZWR1Y2luZyB2YXJpYW5jZSBieSB+MS9CIHdpdGhvdXQgaW5jcmVhc2luZyBiaWFzLiBCb29zdGluZyBmaXRzIG1vZGVscyBzZXF1ZW50aWFsbHkgb24gcmVzaWR1YWxzLCByZWR1Y2luZyBiaWFzIGF0IHRoZSBjb3N0IG9mIHNvbWUgdmFyaWFuY2UuIFJhbmRvbSBmb3Jlc3RzIGNvbWJpbmUgYmFnZ2luZyB3aXRoIGZlYXR1cmUgcmFuZG9taXNhdGlvbiBmb3IgYWRkaXRpb25hbCB2YXJpYW5jZSByZWR1Y3Rpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLnRyZWUgaW1wb3J0IERlY2lzaW9uVHJlZVJlZ3Jlc3NvclxuXG5ybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoMClcbm5fdHJhaW4sIG5fdGVzdCA9IDYwLCAzMDBcbm5fYmFncywgbl9ib290c3RyYXBzID0gNTAsIDEwMFxuWF90ZXN0ID0gbnAubGluc3BhY2UoLTMsIDMsIG5fdGVzdCkucmVzaGFwZSgtMSwgMSlcbmZfdHJ1ZSA9IG5wLnNpbihYX3Rlc3QpLnJhdmVsKClcbm5vaXNlID0gMC41XG5cbnNpbmdsZV9wcmVkcyA9IG5wLnplcm9zKChuX2Jvb3RzdHJhcHMsIG5fdGVzdCkpXG5iYWdfcHJlZHMgICAgPSBucC56ZXJvcygobl9ib290c3RyYXBzLCBuX3Rlc3QpKVxuXG5mb3IgYiBpbiByYW5nZShuX2Jvb3RzdHJhcHMpOlxuICAgIFhfdHIgPSBybmcudW5pZm9ybSgtMywgMywgbl90cmFpbikucmVzaGFwZSgtMSwgMSlcbiAgICB5X3RyID0gbnAuc2luKFhfdHIpLnJhdmVsKCkgKyBybmcucmFuZG4obl90cmFpbikgKiBub2lzZVxuICAgIHNpbmdsZV9wcmVkc1tiXSA9IERlY2lzaW9uVHJlZVJlZ3Jlc3NvcigpLmZpdChYX3RyLCB5X3RyKS5wcmVkaWN0KFhfdGVzdClcbiAgICBiYWdfcHJlZCA9IG5wLnplcm9zKG5fdGVzdClcbiAgICBmb3IgXyBpbiByYW5nZShuX2JhZ3MpOlxuICAgICAgICBpZHggPSBybmcucmFuZGludCgwLCBuX3RyYWluLCBuX3RyYWluKVxuICAgICAgICBiYWdfcHJlZCArPSBEZWNpc2lvblRyZWVSZWdyZXNzb3IoKS5maXQoWF90cltpZHhdLCB5X3RyW2lkeF0pLnByZWRpY3QoWF90ZXN0KVxuICAgIGJhZ19wcmVkc1tiXSA9IGJhZ19wcmVkIC8gbl9iYWdzXG5cbmZvciBuYW1lLCBwcmVkcyBpbiBbKFx1MDAyN1NpbmdsZSB0cmVlXHUwMDI3LCBzaW5nbGVfcHJlZHMpLCAoXHUwMDI3QmFnZ2luZ1x1MDAyNywgYmFnX3ByZWRzKV06XG4gICAgdiA9IG5wLm1lYW4ocHJlZHMudmFyKGF4aXM9MCkpXG4gICAgYjIgPSBucC5tZWFuKChwcmVkcy5tZWFuKGF4aXM9MCkgLSBmX3RydWUpKioyKVxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2UxMn06IEJpYXNeMj17YjI6LjRmfSAgVmFyPXt2Oi40Zn0gIFRvdGFs4omIe2IyK3Yrbm9pc2UqKjI6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNb2RlbCBDbGFzcyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiQmlhcyIsIlZhcmlhbmNlIiwiVHlwaWNhbCBGaXgiXSwicm93cyI6W1siTG9naXN0aWMgcmVncmVzc2lvbiAobGluZWFyIGJvdW5kYXJ5KSIsIkhpZ2ggaWYgdHJ1ZSBib3VuZGFyeSBpcyBub25saW5lYXIiLCJMb3cg4oCUIGZldyBwYXJhbWV0ZXJzIiwiQWRkIHBvbHlub21pYWwgZmVhdHVyZXMgb3Igc3dpdGNoIG1vZGVsIl0sWyJTaGFsbG93IGRlY2lzaW9uIHRyZWUgKGRlcHRoIDHigJMyKSIsIkhpZ2gg4oCUIGNhbiBvbmx5IHNwbGl0IG9uY2UiLCJMb3ciLCJJbmNyZWFzZSBkZXB0aCBvciB1c2UgYm9vc3RpbmciXSxbIkRlZXAgZGVjaXNpb24gdHJlZSAodW5wcnVuZWQpIiwiTG93IOKAlCBmaXRzIGNvbXBsZXggc2hhcGVzIiwiSGlnaCDigJQgc2Vuc2l0aXZlIHRvIGRhdGEiLCJQcnVuZSwgbGltaXQgZGVwdGgsIG9yIHVzZSBiYWdnaW5nIl0sWyJSYW5kb20gZm9yZXN0IiwiTG93LW1vZGVyYXRlIiwiTG93IOKAlCBiYWdnaW5nIHJlZHVjZXMgdmFyaWFuY2UiLCJUdW5lIG5fZXN0aW1hdG9ycyBhbmQgbWF4X2ZlYXR1cmVzIl0sWyJEZWVwIG5ldXJhbCBuZXR3b3JrIChubyByZWd1bGFyaXNhdGlvbikiLCJMb3ciLCJWZXJ5IGhpZ2giLCJEcm9wb3V0LCB3ZWlnaHQgZGVjYXksIGVhcmx5IHN0b3BwaW5nIl0sWyJLZXJuZWwgU1ZNIChSQkYsIHNtYWxsIM6zKSIsIkhpZ2gg4oCUIHNtb290aCBkZWNpc2lvbiBib3VuZGFyeSIsIkxvdyIsIkluY3JlYXNlIM6zIG9yIHVzZSBwb2x5bm9taWFsIGtlcm5lbCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUHJhY3RpY2FsIEltcGxpY2F0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVG8gZGlhZ25vc2Ugd2hldGhlciB5b3VyIG1vZGVsIGhhcyBhIGJpYXMgb3IgdmFyaWFuY2UgcHJvYmxlbTogcGxvdCBsZWFybmluZyBjdXJ2ZXMgKHRyYWluaW5nIGFuZCB2YWxpZGF0aW9uIGVycm9yIHZzIG4pLiBIaWdoIGJpYXM6IGJvdGggY3VydmVzIHBsYXRlYXUgaGlnaCBhbmQgY2xvc2UgdG9nZXRoZXIg4oCUIGNvbGxlY3QgbW9yZSBmZWF0dXJlcyBvciB1c2UgYSBtb3JlIGNvbXBsZXggbW9kZWwuIEhpZ2ggdmFyaWFuY2U6IGxhcmdlIGdhcCBiZXR3ZWVuIHRyYWluaW5nIGFuZCB2YWxpZGF0aW9uIGN1cnZlcyDigJQgY29sbGVjdCBtb3JlIGRhdGEsIHJlZ3VsYXJpc2UsIG9yIHJlZHVjZSBtb2RlbCBjb21wbGV4aXR5LiBSZWR1Y2luZyBkYXRhc2V0IG5vaXNlIChiZXR0ZXIgbGFiZWxzLCBmZWF0dXJlIGVuZ2luZWVyaW5nKSBkaXJlY3RseSByZWR1Y2VzIHRoZSBpcnJlZHVjaWJsZSBlcnJvciBmbG9vci4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkhpZ2ggYmlhcyBzaWduYWw6IHRyYWluaW5nIGVycm9yIOKJiCB2YWxpZGF0aW9uIGVycm9yLCBib3RoIHVuYWNjZXB0YWJseSBoaWdoLiIsIkhpZ2ggdmFyaWFuY2Ugc2lnbmFsOiB0cmFpbmluZyBlcnJvciDiiaogdmFsaWRhdGlvbiBlcnJvciAobGFyZ2UgZ2FwKS4iLCJCYWdnaW5nIHJlZHVjZXMgdmFyaWFuY2Ugd2l0aG91dCBjaGFuZ2luZyBiaWFzIOKAlCBnb29kIGZvciBoaWdoLXZhcmlhbmNlIG1vZGVscyBsaWtlIGRlZXAgdHJlZXMuIiwiQm9vc3RpbmcgcmVkdWNlcyBiaWFzIGJ5IHNlcXVlbnRpYWxseSBjb3JyZWN0aW5nIGVycm9ycyDigJQgZ29vZCBmb3IgaGlnaC1iaWFzIHdlYWsgbGVhcm5lcnMuIiwiUmVndWxhcmlzYXRpb24gKEwxL0wyLCBkcm9wb3V0KSBzaGlmdHMgdGhlIGJpYXMtdmFyaWFuY2UgYmFsYW5jZSB0b3dhcmQgbW9yZSBiaWFzLCBsZXNzIHZhcmlhbmNlLiIsIk1vcmUgdHJhaW5pbmcgZGF0YSBoZWxwcyBoaWdoLXZhcmlhbmNlIG1vZGVscyBtb3N0OyBpdCBkb2VzIG5vdCBoZWxwIGhpZ2gtYmlhcyBtb2RlbHMgc2lnbmlmaWNhbnRseS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Bias-Variance Tradeoff

Every supervised learning model makes an error that can be decomposed into three orthogonal components: bias (systematic error from model assumptions), variance (sensitivity to the specific training set drawn), and irreducible noise (inherent randomness in the data-generating process). Understanding this decomposition explains why simple models underfit, complex models overfit, and how regularisation, ensembles, and larger datasets help — each targeting a different component.

## Deriving the Bias-Variance Decomposition

Let f(x) be the true function, ŷ(x) the model prediction (a random variable over training sets), and ε ~ N(0,σ²) irreducible noise. The expected squared error at a point x decomposes as: E[(y − ŷ)²] = E[(f(x) + ε − ŷ)²]. Add and subtract E[ŷ]: = E[(f(x) − E[ŷ])²] + E[(E[ŷ] − ŷ)²] + σ² = Bias²(ŷ) + Var(ŷ) + σ². The cross terms vanish because ε is independent of ŷ and E[ε]=0.

Bias = E[ŷ] − f(x) is the average difference between model predictions and the true function — it is zero for a model flexible enough to represent f exactly. Variance = E[(ŷ − E[ŷ])²] measures how much the model fluctuates across different training sets of the same size. A high-capacity model (deep tree, high-degree polynomial) fits each training set closely: low bias, high variance. A simple model (constant, linear with few features): high bias, low variance.

## Simulating the Decomposition via Bootstrap

To empirically estimate bias and variance, repeatedly draw B training sets from the same distribution, train the model on each, and evaluate on a fixed test set. The average prediction over B models estimates E[ŷ]; the variance of predictions estimates Var(ŷ); the squared gap between the average prediction and the true function estimates Bias². This is computationally intensive but gives exact empirical estimates for any model class.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

def bias_variance_decomp(max_depth, n_bootstraps=200, n_train=60,
                          n_test=400, noise=0.5, seed=0):
    rng = np.random.RandomState(seed)
    X_test = np.linspace(-3, 3, n_test).reshape(-1, 1)
    f_true = np.sin(X_test).ravel()
    preds = np.zeros((n_bootstraps, n_test))
    for b in range(n_bootstraps):
        X_tr = rng.uniform(-3, 3, n_train).reshape(-1, 1)
        y_tr = np.sin(X_tr).ravel() + rng.randn(n_train) * noise
        model = DecisionTreeRegressor(max_depth=max_depth)
        model.fit(X_tr, y_tr)
        preds[b] = model.predict(X_test)
    mean_pred = preds.mean(axis=0)
    bias_sq  = np.mean((mean_pred - f_true) ** 2)
    variance  = np.mean(preds.var(axis=0))
    noise_sq  = noise ** 2
    return bias_sq, variance, noise_sq

print(f'{"Depth":>6} {"Bias^2":>8} {"Var":>8} {"Noise":>8} {"Total":>8}')
for depth in [1, 2, 4, 8, 16]:
    b2, v, n = bias_variance_decomp(depth)
    print(f'{depth:>6} {b2:>8.4f} {v:>8.4f} {n:>8.4f} {b2+v+n:>8.4f}')
```

## Test Error Curve vs Model Complexity

As model complexity increases (e.g., polynomial degree, tree depth, network width), training error monotonically decreases while test error follows a U-shape: high (underfitting) for simple models, minimum at optimal complexity, rising again (overfitting) for complex models. The gap between training and test error is approximately 2 × Variance / n for many model classes. Cross-validation estimates the test error curve without requiring a holdout set.

```python
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

np.random.seed(0)
X = np.random.uniform(-3, 3, 120).reshape(-1, 1)
y = np.sin(X).ravel() + 0.4 * np.random.randn(120)

degrees = range(1, 16)
train_errs, cv_errs = [], []
for d in degrees:
    pipe = Pipeline([
        ('poly', PolynomialFeatures(degree=d, include_bias=False)),
        ('lr',   LinearRegression())
    ])
    cv_scores = cross_val_score(
        pipe, X, y, cv=5, scoring='neg_mean_squared_error'
    )
    pipe.fit(X, y)
    train_errs.append(np.mean((y - pipe.predict(X))**2))
    cv_errs.append(-cv_scores.mean())

best_d = list(degrees)[np.argmin(cv_errs)]
print(f'{"Deg":>4} {"Train MSE":>10} {"CV MSE":>10}')
for d, tr, cv in zip(degrees, train_errs, cv_errs):
    marker = ' <-- best' if d == best_d else ''
    print(f'{d:>4} {tr:>10.4f} {cv:>10.4f}{marker}')
```

## Double Descent Phenomenon

Classical statistical learning theory predicts a U-shaped bias-variance tradeoff. But modern overparameterised models (deep networks, random features, kernel machines) exhibit double descent: test error rises near the interpolation threshold (where model capacity ≈ n) and then decreases again as capacity continues to grow. The minimum-norm interpolating solution in the overparameterised regime implicitly regularises, achieving low variance despite zero training error.

> **Why Double Descent Happens**: Near the interpolation threshold the model barely fits the data — small perturbations cause large coefficient swings (high variance). Beyond the threshold there are many solutions that fit perfectly; gradient descent or pseudoinverse selects the minimum-norm one, which is smooth and generalises well. This breaks the classical U-curve and challenges the bias-variance framing for modern models.

```python
import numpy as np

np.random.seed(42)
n_train = 50
rng = np.random.RandomState(42)
X_full = rng.randn(n_train, 300)
y_train = rng.randn(n_train)          # pure noise — no true signal
X_test  = rng.randn(500, 300)
y_test  = rng.randn(500)

p_values = list(range(5, 300, 5))
test_mse = []
for p in p_values:
    Xtr = X_full[:, :p]
    Xte = X_test[:, :p]
    # Minimum-norm (pseudoinverse) solution
    coef, _, _, _ = np.linalg.lstsq(Xtr, y_train, rcond=None)
    pred = Xte @ coef
    test_mse.append(np.mean((y_test - pred)**2))

peak_p = p_values[int(np.argmax(test_mse))]
print(f'Interpolation threshold n = {n_train}')
print(f'Peak test MSE at p = {peak_p}: {max(test_mse):.2f}')
print(f'Test MSE at p=5:   {test_mse[0]:.4f}')
print(f'Test MSE at p=295: {test_mse[-1]:.4f}')
print('MSE rises near n=p, then falls again as p >> n (double descent).')
```

## Regularisation and Ensembles

Regularisation (L1, L2, dropout, early stopping) adds bias to reduce variance — trading a slightly wrong answer for a much more stable one. Bagging (Bootstrap AGGregating) averages predictions over B models trained on bootstrap samples, reducing variance by ~1/B without increasing bias. Boosting fits models sequentially on residuals, reducing bias at the cost of some variance. Random forests combine bagging with feature randomisation for additional variance reduction.

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

rng = np.random.RandomState(0)
n_train, n_test = 60, 300
n_bags, n_bootstraps = 50, 100
X_test = np.linspace(-3, 3, n_test).reshape(-1, 1)
f_true = np.sin(X_test).ravel()
noise = 0.5

single_preds = np.zeros((n_bootstraps, n_test))
bag_preds    = np.zeros((n_bootstraps, n_test))

for b in range(n_bootstraps):
    X_tr = rng.uniform(-3, 3, n_train).reshape(-1, 1)
    y_tr = np.sin(X_tr).ravel() + rng.randn(n_train) * noise
    single_preds[b] = DecisionTreeRegressor().fit(X_tr, y_tr).predict(X_test)
    bag_pred = np.zeros(n_test)
    for _ in range(n_bags):
        idx = rng.randint(0, n_train, n_train)
        bag_pred += DecisionTreeRegressor().fit(X_tr[idx], y_tr[idx]).predict(X_test)
    bag_preds[b] = bag_pred / n_bags

for name, preds in [('Single tree', single_preds), ('Bagging', bag_preds)]:
    v = np.mean(preds.var(axis=0))
    b2 = np.mean((preds.mean(axis=0) - f_true)**2)
    print(f'{name:>12}: Bias^2={b2:.4f}  Var={v:.4f}  Total≈{b2+v+noise**2:.4f}')
```

## Model Class Comparison

| Model | Bias | Variance | Typical Fix |
| --- | --- | --- | --- |
| Logistic regression (linear boundary) | High if true boundary is nonlinear | Low — few parameters | Add polynomial features or switch model |
| Shallow decision tree (depth 1–2) | High — can only split once | Low | Increase depth or use boosting |
| Deep decision tree (unpruned) | Low — fits complex shapes | High — sensitive to data | Prune, limit depth, or use bagging |
| Random forest | Low-moderate | Low — bagging reduces variance | Tune n_estimators and max_features |
| Deep neural network (no regularisation) | Low | Very high | Dropout, weight decay, early stopping |
| Kernel SVM (RBF, small γ) | High — smooth decision boundary | Low | Increase γ or use polynomial kernel |

## Practical Implications

To diagnose whether your model has a bias or variance problem: plot learning curves (training and validation error vs n). High bias: both curves plateau high and close together — collect more features or use a more complex model. High variance: large gap between training and validation curves — collect more data, regularise, or reduce model complexity. Reducing dataset noise (better labels, feature engineering) directly reduces the irreducible error floor.

- High bias signal: training error ≈ validation error, both unacceptably high.
- High variance signal: training error ≪ validation error (large gap).
- Bagging reduces variance without changing bias — good for high-variance models like deep trees.
- Boosting reduces bias by sequentially correcting errors — good for high-bias weak learners.
- Regularisation (L1/L2, dropout) shifts the bias-variance balance toward more bias, less variance.
- More training data helps high-variance models most; it does not help high-bias models significantly.

---

