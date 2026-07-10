---
title: "Recurrent Computation — Hidden State and Weight Sharing"
slug: "recurrent-computation"
description: "Derive the RNN recurrence equation, explore weight sharing across time, understand many-to-one/many-to-many architectures, implement stateful inference for long sequences, and compare RNN vs Transformer training speed."
tags: ["deep-learning", "rnns", "sequence-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBSZWN1cnJlbnQgTmV1cmFsIE5ldHdvcmsgKFJOTikgcHJvY2Vzc2VzIHNlcXVlbmNlcyBieSBtYWludGFpbmluZyBhIGhpZGRlbiBzdGF0ZSBo4oKcIHRoYXQgc3VtbWFyaXNlcyBhbGwgaW5mb3JtYXRpb24gc2VlbiB1cCB0byB0aW1lIHQuIEF0IGVhY2ggc3RlcCB0aGUgc2FtZSB3ZWlnaHQgbWF0cmljZXMgYXJlIGFwcGxpZWQ6IGjigpwgPSB0YW5oKFfigpXigpN44oKcICsgV+KCleKClWjigpzigovigoEgKyBiKSwgeeKCnCA9IFfigpJo4oKcLiBUaGlzIHdlaWdodCBzaGFyaW5nIGFjcm9zcyB0aW1lIGlzIHRoZSBkZWZpbmluZyBwcm9wZXJ0eSBvZiBSTk5zIOKAlCB1bmxpa2UgYSBmZWVkZm9yd2FyZCBuZXR3b3JrIHdpdGggc2VwYXJhdGUgcGFyYW1ldGVycyBwZXIgcG9zaXRpb24sIHRoZSBSTk4gdXNlcyBpZGVudGljYWwgV+KCleKClSBhdCBldmVyeSBzdGVwLCBnaXZpbmcgaXQgTyhIwrIpIHJlY3VycmVudCBwYXJhbWV0ZXJzIHJlZ2FyZGxlc3Mgb2Ygc2VxdWVuY2UgbGVuZ3RoIFQuIFRoZSBzYW1lIG1lY2hhbmlzbSB0aGF0IGVuYWJsZXMgdmFyaWFibGUtbGVuZ3RoIHByb2Nlc3NpbmcgYWxzbyBpbnRyb2R1Y2VzIHRoZSB2YW5pc2hpbmcgZ3JhZGllbnQgcHJvYmxlbSBhbmQgcHJldmVudHMgcGFyYWxsZWxpc2F0aW9uIG92ZXIgdGhlIHRpbWUgYXhpcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgUk5OIFJlY3VycmVuY2UgRXF1YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBjb3JlIHJlY3VycmVuY2UgaOKCnCA9IHRhbmgoV+KCleKCk3jigpwgKyBX4oKV4oKVaOKCnOKCi+KCgSArIGIpIGNvbXBvc2VzIHRocmVlIG9wZXJhdGlvbnM6IGEgbGluZWFyIHByb2plY3Rpb24gb2YgdGhlIGlucHV0IHjigpwg4oiIIOKEneG0tSB2aWEgV+KCleKCkyDiiIgg4oSd4bS0y6PhtLUsIGEgbGluZWFyIHByb2plY3Rpb24gb2YgdGhlIHByZXZpb3VzIGhpZGRlbiBzdGF0ZSBo4oKc4oKL4oKBIOKIiCDihJ3htLQgdmlhIFfigpXigpUg4oiIIOKEneG0tMuj4bS0LCBhbmQgYSB0YW5oIG5vbmxpbmVhcml0eSB0aGF0IHNxdWFzaGVzIHRoZSByZXN1bHQgdG8gKC0xLCAxKS4gVGhlIG91dHB1dCB54oKcID0gV+KCkmjigpwgaXMgYSBsaW5lYXIgcmVhZG91dCBmcm9tIHRoZSBoaWRkZW4gc3RhdGUgdmlhIFfigpIg4oiIIOKEneG0vMuj4bS0LiBUb3RhbCBwYXJhbWV0ZXJzOiBIw5dJIChX4oKV4oKTKSArIEjDl0ggKFfigpXigpUpICsgSMOXTyAoV+KCkikgKyBIIChiaWFzKS4gQ29tcHV0YXRpb25hbCBjb3N0IHBlciBzdGVwIGlzIE8oSMKyKSBmb3IgdGhlIFfigpXigpVo4oKc4oKL4oKBIHByb2R1Y3QsIGdpdmluZyBPKFTCt0jCsikgdG90YWwgZm9yIGEgc2VxdWVuY2Ugb2YgbGVuZ3RoIFQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2VpZ2h0IFNoYXJpbmcgQWNyb3NzIFRpbWUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldlaWdodCBzaGFyaW5nIG1lYW5zIHRoZSBzYW1lIFfigpXigpUgaXMgbXVsdGlwbGllZCBhdCBldmVyeSB0aW1lIHN0ZXAuIFRoaXMgaXMgYW5hbG9nb3VzIHRvIGEgY29udm9sdXRpb25hbCBmaWx0ZXIgYmVpbmcgYXBwbGllZCBhdCBldmVyeSBzcGF0aWFsIHBvc2l0aW9uIOKAlCBpdCBhbGxvd3MgdGhlIG1vZGVsIHRvIGdlbmVyYWxpc2UgdGVtcG9yYWwgcGF0dGVybnMgcmVnYXJkbGVzcyBvZiB3aGVuIHRoZXkgb2NjdXIuIFRoZW9yZXRpY2FsbHksIFJOTnMgd2l0aCBzdWZmaWNpZW50IGhpZGRlbiBzaXplIGFyZSBUdXJpbmcgY29tcGxldGU6IHRoZXkgY2FuIHNpbXVsYXRlIGFueSBjb21wdXRhYmxlIGZ1bmN0aW9uIG9uIHNlcXVlbmNlcy4gUHJhY3RpY2FsbHksIGxlYXJuaW5nIGxvbmctcmFuZ2UgZGVwZW5kZW5jaWVzIGlzIGxpbWl0ZWQgYnkgdGhlIHZhbmlzaGluZyBncmFkaWVudCBwcm9ibGVtLiBUaGUgaGlkZGVuIHN0YXRlIGjigpwgbXVzdCBjb21wcmVzcyB0aGUgZW50aXJlIGhpc3RvcnkgaW50byBIIG51bWJlcnMsIGNyZWF0aW5nIGFuIGluZm9ybWF0aW9uIGJvdHRsZW5lY2sgZm9yIHZlcnkgbG9uZyBzZXF1ZW5jZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5jbGFzcyBWYW5pbGxhUk5OOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbnB1dF9zaXplLCBoaWRkZW5fc2l6ZSwgb3V0cHV0X3NpemUpOlxuICAgICAgICBzY2FsZSA9IDAuMDFcbiAgICAgICAgc2VsZi5XeGggPSBucC5yYW5kb20ucmFuZG4oaGlkZGVuX3NpemUsIGlucHV0X3NpemUpICogc2NhbGVcbiAgICAgICAgc2VsZi5XaGggPSBucC5yYW5kb20ucmFuZG4oaGlkZGVuX3NpemUsIGhpZGRlbl9zaXplKSAqIHNjYWxlXG4gICAgICAgIHNlbGYuV2h5ID0gbnAucmFuZG9tLnJhbmRuKG91dHB1dF9zaXplLCBoaWRkZW5fc2l6ZSkgKiBzY2FsZVxuICAgICAgICBzZWxmLmJoICA9IG5wLnplcm9zKChoaWRkZW5fc2l6ZSwgMSkpXG4gICAgICAgIHNlbGYuYnkgID0gbnAuemVyb3MoKG91dHB1dF9zaXplLCAxKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGlucHV0cywgaF9wcmV2KTpcbiAgICAgICAgc2VsZi5ocyA9IHstMTogaF9wcmV2fVxuICAgICAgICBzZWxmLnlzID0ge31cbiAgICAgICAgZm9yIHQsIHggaW4gZW51bWVyYXRlKGlucHV0cyk6XG4gICAgICAgICAgICBzZWxmLmhzW3RdID0gbnAudGFuaChcbiAgICAgICAgICAgICAgICBzZWxmLld4aCBAIHggKyBzZWxmLldoaCBAIHNlbGYuaHNbdCAtIDFdICsgc2VsZi5iaFxuICAgICAgICAgICAgKVxuICAgICAgICAgICAgc2VsZi55c1t0XSA9IHNlbGYuV2h5IEAgc2VsZi5oc1t0XSArIHNlbGYuYnlcbiAgICAgICAgcmV0dXJuIHNlbGYueXMsIHNlbGYuaHNcblxubnAucmFuZG9tLnNlZWQoNDIpXG5ULCBJLCBILCBPID0gNSwgNCwgOCwgM1xucm5uID0gVmFuaWxsYVJOTihJLCBILCBPKVxuaW5wdXRzID0gW25wLnJhbmRvbS5yYW5kbihJLCAxKSBmb3IgXyBpbiByYW5nZShUKV1cbmgwID0gbnAuemVyb3MoKEgsIDEpKVxueXMsIGhzID0gcm5uLmZvcndhcmQoaW5wdXRzLCBoMClcbnByaW50KGZcdTAwMjdTZXF1ZW5jZSBsZW5ndGggVD17VH0sIGhpZGRlbiBzaXplIEg9e0h9XHUwMDI3KVxuZm9yIHQgaW4gcmFuZ2UoVCk6XG4gICAgcHJpbnQoZlx1MDAyNyAgdD17dH06IGggc2hhcGU9e2hzW3RdLnNoYXBlfSwgeSBzaGFwZT17eXNbdF0uc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN2hfVCBub3JtID0ge25wLmxpbmFsZy5ub3JtKGhzW1QtMV0pOi40Zn1cdTAwMjcpXG5wcmludChcdTAwMjdTYW1lIFdoaCBhcHBsaWVkIGF0IGV2ZXJ5IHN0ZXAgLS0gd2VpZ2h0IHNoYXJpbmcgYWNyb3NzIHRpbWUuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlB5VG9yY2ggbm4uUk5OIOKAlCBNYW55LXRvLU9uZSBhbmQgTWFueS10by1NYW55In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQeVRvcmNoXHUwMDI3cyBubi5STk4gd3JhcHMgdGhlIHJlY3VycmVuY2UgaW4gYW4gb3B0aW1pc2VkIENVREEga2VybmVsLiBUaGUgb3V0cHV0IHRlbnNvciBjb250YWlucyBoaWRkZW4gc3RhdGVzIGF0IGFsbCBUIHN0ZXBzOyBoX24gaXMgdGhlIGZpbmFsIGhpZGRlbiBzdGF0ZS4gRm9yIG1hbnktdG8tb25lIHRhc2tzIChjbGFzc2lmaWNhdGlvbiksIHVzZSBoX24gZGlyZWN0bHkuIEZvciBtYW55LXRvLW1hbnkgKHRhZ2dpbmcsIHRyYW5zbGF0aW9uKSwgdXNlIHRoZSBmdWxsIG91dHB1dCBzZXF1ZW5jZS4gT25lLXRvLW1hbnkgKGdlbmVyYXRpb24pIHJlcGVhdHMgYSBzZWVkIGlucHV0IGZvciBUIHN0ZXBzLiBCaWRpcmVjdGlvbmFsIFJOTnMgcnVuIG9uZSBmb3J3YXJkIGFuZCBvbmUgYmFja3dhcmQgcGFzcywgY29uY2F0ZW5hdGluZyBoaWRkZW4gc3RhdGVzIOKAlCBkb3VibGluZyB0aGUgcGFyYW1ldGVyIGNvdW50IGFuZCBvdXRwdXQgZGltZW5zaW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcblQsIEIsIEksIEggPSAxMCwgNCwgOCwgMTYgICMgc2VxX2xlbiwgYmF0Y2gsIGlucHV0X2RpbSwgaGlkZGVuX2RpbVxuXG5ybm4gPSBubi5STk4oaW5wdXRfc2l6ZT1JLCBoaWRkZW5fc2l6ZT1ILCBiYXRjaF9maXJzdD1UcnVlKVxueCA9IHRvcmNoLnJhbmRuKEIsIFQsIEkpXG5cbiMgTWFueS10by1tYW55OiB1c2UgYWxsIHRpbWUtc3RlcCBvdXRwdXRzXG5vdXQsIGhfbiA9IHJubih4KVxucHJpbnQoZlx1MDAyN01hbnktdG8tbWFueTogb3V0LnNoYXBlPXtvdXQuc2hhcGV9LCBoX24uc2hhcGU9e2hfbi5zaGFwZX1cdTAwMjcpXG5cbiMgTWFueS10by1vbmU6IGxhc3QgaGlkZGVuIHN0YXRlIG9ubHlcbmxhc3RfaGlkZGVuID0gaF9uLnNxdWVlemUoMCkgICMgKEIsIEgpXG5wcmludChmXHUwMDI3TWFueS10by1vbmU6IGxhc3RfaGlkZGVuLnNoYXBlPXtsYXN0X2hpZGRlbi5zaGFwZX1cdTAwMjcpXG5cbiMgT25lLXRvLW1hbnk6IHJlcGVhdCBzaW5nbGUgaW5wdXQgZm9yIFQgc3RlcHNcbnNpbmdsZV9pbnB1dCA9IHRvcmNoLnJhbmRuKEIsIDEsIEkpLnJlcGVhdCgxLCBULCAxKVxub3V0X290bSwgXyA9IHJubihzaW5nbGVfaW5wdXQpXG5wcmludChmXHUwMDI3T25lLXRvLW1hbnk6IG91dC5zaGFwZT17b3V0X290bS5zaGFwZX1cdTAwMjcpXG5cbiMgQmlkaXJlY3Rpb25hbCBSTk5cbnJubl9iaSA9IG5uLlJOTihpbnB1dF9zaXplPUksIGhpZGRlbl9zaXplPUgsIGJhdGNoX2ZpcnN0PVRydWUsIGJpZGlyZWN0aW9uYWw9VHJ1ZSlcbm91dF9iaSwgaF9iaSA9IHJubl9iaSh4KVxucHJpbnQoZlx1MDAyN0JpZGlyZWN0aW9uYWw6IG91dC5zaGFwZT17b3V0X2JpLnNoYXBlfSwgaF9uLnNoYXBlPXtoX2JpLnNoYXBlfVx1MDAyNylcblxudG90YWxfcGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBybm4ucGFyYW1ldGVycygpKVxucHJpbnQoZlx1MDAyN1VuaWRpcmVjdGlvbmFsIFJOTiBwYXJhbXM6IHt0b3RhbF9wYXJhbXN9XHUwMDI3KVxucHJpbnQoZlx1MDAyNyAgV3hoOiB7SX14e0h9PXtJKkh9LCBXaGg6IHtIfXh7SH09e0gqSH0sIGJoOiB7SH1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RhdGVmdWwgSW5mZXJlbmNlIGZvciBMb25nIFNlcXVlbmNlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIHNlcXVlbmNlcyBsb25nZXIgdGhhbiB0aGUgdHJhaW5pbmcgY29udGV4dCAoZS5nLiwgc3RyZWFtaW5nIGF1ZGlvIG9yIHZlcnkgbG9uZyBkb2N1bWVudHMpLCB0aGUgaGlkZGVuIHN0YXRlIG11c3QgYmUgY2FycmllZCBiZXR3ZWVuIGJhdGNoZXMuIFRoZSBrZXkgaXMgdG8gcGFzcyBoX3N0YXRlIGZyb20gdGhlIHByZXZpb3VzIGNodW5rIGFzIHRoZSBpbml0aWFsIHN0YXRlIGZvciB0aGUgbmV4dCBjaHVuay4gR3JhZGllbnRzIGFyZSBub3QgdHJhY2tlZCBhY3Jvc3MgY2h1bmtzIGR1cmluZyBpbmZlcmVuY2UuIER1cmluZyB0cmFpbmluZywgdGhlIGhpZGRlbiBzdGF0ZSBpcyBkZXRhY2hlZCAoaC5kZXRhY2goKSkgdG8gc3RvcCBncmFkaWVudCBmbG93IGludG8gZWFybGllciBjaHVua3Mg4oCUIHRoaXMgaXMgdGhlIHRydW5jYXRlZCBCUFRUIHBhdHRlcm4uIENhcnJ5aW5nIHN0YXRlIGFsbG93cyB0aGUgbW9kZWwgdG8gdXNlIGluZm9ybWF0aW9uIGZyb20gdGhlIGVudGlyZSBzZXF1ZW5jZSBoaXN0b3J5IGF0IGluZmVyZW5jZSB0aW1lLCBldmVuIGlmIGdyYWRpZW50cyBvbmx5IGZsb3cgd2l0aGluIGNodW5rcyBhdCB0cmFpbmluZyB0aW1lLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuSSwgSCwgTywgQiA9IDgsIDMyLCA0LCAyXG5UT1RBTF9MRU4gPSA1MDBcbkNIVU5LX1NJWkUgPSA1MFxuXG5ybm4gPSBubi5STk4oaW5wdXRfc2l6ZT1JLCBoaWRkZW5fc2l6ZT1ILCBiYXRjaF9maXJzdD1UcnVlKVxuZmMgID0gbm4uTGluZWFyKEgsIE8pXG5ybm4uZXZhbCgpOyBmYy5ldmFsKClcblxubG9uZ19zZXEgPSB0b3JjaC5yYW5kbihCLCBUT1RBTF9MRU4sIEkpXG5oX3N0YXRlICA9IHRvcmNoLnplcm9zKDEsIEIsIEgpICAjIChudW1fbGF5ZXJzLCBiYXRjaCwgaGlkZGVuKVxuXG5vdXRwdXRzID0gW11cbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIGZvciBzdGFydCBpbiByYW5nZSgwLCBUT1RBTF9MRU4sIENIVU5LX1NJWkUpOlxuICAgICAgICBjaHVuayA9IGxvbmdfc2VxWzosIHN0YXJ0OnN0YXJ0ICsgQ0hVTktfU0laRSwgOl1cbiAgICAgICAgb3V0LCBoX3N0YXRlID0gcm5uKGNodW5rLCBoX3N0YXRlKVxuICAgICAgICAjIGhfc3RhdGUgY2FycmllcyB0byBuZXh0IGNodW5rIOKAlCBzdGF0ZWZ1bCBpbmZlcmVuY2VcbiAgICAgICAgbG9naXRzID0gZmMob3V0KVxuICAgICAgICBvdXRwdXRzLmFwcGVuZChsb2dpdHMpXG5cbmFsbF9vdXQgPSB0b3JjaC5jYXQob3V0cHV0cywgZGltPTEpXG5wcmludChmXHUwMDI3SW5wdXQgbGVuZ3RoOiB7VE9UQUxfTEVOfSwgY2h1bmsgc2l6ZToge0NIVU5LX1NJWkV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN051bWJlciBvZiBjaHVua3M6IHtUT1RBTF9MRU4gLy8gQ0hVTktfU0laRX1cdTAwMjcpXG5wcmludChmXHUwMDI3RmluYWwgb3V0cHV0IHNoYXBlOiB7YWxsX291dC5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3RmluYWwgaGlkZGVuIHN0YXRlIG5vcm06IHtoX3N0YXRlLm5vcm0oKS5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN0hpZGRlbiBzdGF0ZSBjYXJyaWVkIGFjcm9zcyBjaHVua3MgLS0gZnVsbC1zZXF1ZW5jZSBjb250ZXh0IGF0IGluZmVyZW5jZS5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUk5OIEFyY2hpdGVjdHVyZXMifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiQXJjaGl0ZWN0dXJlIiwiVXNlIENhc2UiLCJIaWRkZW4gU3RhdGUgSGFuZGxpbmciLCJCYXRjaCBQcm9jZXNzaW5nIiwiRXhhbXBsZSBUYXNrIl0sInJvd3MiOltbIk1hbnktdG8tbWFueSAoYWxpZ25lZCkiLCJPdXRwdXQgYXQgZXZlcnkgaW5wdXQgc3RlcCIsImhfdCB1c2VkIGF0IGVhY2ggdCIsIlBhZCB0byBtYXggbGVuZ3RoOyBtYXNrIG91dHB1dCBsb3NzIiwiUE9TIHRhZ2dpbmcsIE5FUiwgZnJhbWUtbGV2ZWwgcHJlZGljdGlvbiJdLFsiTWFueS10by1vbmUiLCJTaW5nbGUgb3V0cHV0IGZvciB3aG9sZSBzZXF1ZW5jZSIsIk9ubHkgZmluYWwgaF9UIHVzZWQiLCJQYWQgKyBwYWNrIHNlcXVlbmNlcyBmb3IgZWZmaWNpZW5jeSIsIlNlbnRpbWVudCBhbmFseXNpcywgc2VxdWVuY2UgY2xhc3NpZmljYXRpb24iXSxbIk9uZS10by1tYW55IiwiR2VuZXJhdGUgc2VxdWVuY2UgZnJvbSBzaW5nbGUgaW5wdXQiLCJEZWNvZGVkIHN0ZXAtYnktc3RlcCBmcm9tIGhfMCIsIlJlcGxpY2F0ZSBpbnB1dCBmb3IgVCBzdGVwcyIsIkltYWdlIGNhcHRpb25pbmcsIG11c2ljIGdlbmVyYXRpb24iXSxbIkVuY29kZXItZGVjb2RlciIsIk1hcCBzZXF1ZW5jZSB0byBzZXF1ZW5jZSBvZiBkaWZmZXJlbnQgbGVuZ3RoIiwiRW5jb2RlciBoX1QgaW5pdGlhbGlzZXMgZGVjb2RlciIsIkZpeGVkLWxlbmd0aCBib3R0bGVuZWNrOyBhdHRlbnRpb24gbmVlZGVkIGZvciBsb25nIHNlcXMiLCJNYWNoaW5lIHRyYW5zbGF0aW9uLCBzdW1tYXJpemF0aW9uIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTZXF1ZW50aWFsIENvbXB1dGF0aW9uIGFuZCBHUFUgTGltaXRhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSByZWN1cnJlbmNlIGjigpwgPSBmKGjigpzigovigoEsIHjigpwpIGNyZWF0ZXMgYSBzdHJpY3Qgc2VxdWVudGlhbCBkZXBlbmRlbmN5OiBzdGVwIHQgY2Fubm90IGJlZ2luIHVudGlsIHN0ZXAgdC0xIGlzIGNvbXBsZXRlLiBUaGlzIHByZXZlbnRzIHBhcmFsbGVsaXNhdGlvbiBvdmVyIHRoZSB0aW1lIGF4aXMuIE9uIGEgR1BVIHdpdGggdGhvdXNhbmRzIG9mIGNvcmVzLCBvbmx5IHRoZSBtYXRyaXggbXVsdGlwbGljYXRpb25zIFfigpXigpN44oKcIGFuZCBX4oKV4oKVaOKCnOKCi+KCgSBhdCBlYWNoIHNpbmdsZSBzdGVwIGFyZSBwYXJhbGxlbGlzYWJsZSDigJQgYnV0IHRoZXNlIGFyZSBzbWFsbCBjb21wYXJlZCB0byB3aGF0IGEgVHJhbnNmb3JtZXIgY2FuIHBhcmFsbGVsaXNlIChhbGwgVCBwb3NpdGlvbnMgc2ltdWx0YW5lb3VzbHkpLiBGb3IgVD01MTIgYW5kIEg9NTEyLCBhbiBSTk4gcmVxdWlyZXMgNTEyIHNlcXVlbnRpYWwgbWF0cml4IG11bHRpcGxpY2F0aW9ucyBvZiBzaXplIDUxMsOXNTEyLCB3aGlsZSBhIFRyYW5zZm9ybWVyIGNvbXB1dGVzIGFsbCBhdHRlbnRpb24gaW4gYSBzaW5nbGUgYmF0Y2hlZCBvcGVyYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdGltZVxuXG50b3JjaC5tYW51YWxfc2VlZCg0MilcbmRldmljZSA9IHRvcmNoLmRldmljZShcdTAwMjdjdWRhXHUwMDI3IGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcdTAwMjdjcHVcdTAwMjcpXG5CLCBULCBJLCBIID0gMTYsIDY0LCAzMiwgNjRcblxucm5uID0gbm4uUk5OKGlucHV0X3NpemU9SSwgaGlkZGVuX3NpemU9SCwgYmF0Y2hfZmlyc3Q9VHJ1ZSkudG8oZGV2aWNlKVxudGZfbGF5ZXIgPSBubi5UcmFuc2Zvcm1lckVuY29kZXJMYXllcihcbiAgICBkX21vZGVsPUksIG5oZWFkPTQsIGRpbV9mZWVkZm9yd2FyZD0xMjgsIGJhdGNoX2ZpcnN0PVRydWVcbikudG8oZGV2aWNlKVxuXG54ID0gdG9yY2gucmFuZG4oQiwgVCwgSSwgZGV2aWNlPWRldmljZSlcbm5faXRlcnMgPSA1MFxuXG4jIFJOTjogc2VxdWVudGlhbCBvdmVyIFQgc3RlcHNcbnN0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuZm9yIF8gaW4gcmFuZ2Uobl9pdGVycyk6XG4gICAgb3V0X3JubiwgXyA9IHJubih4KVxuICAgIG91dF9ybm4uc3VtKCkuYmFja3dhcmQoKVxucm5uX21zID0gKHRpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydCkgLyBuX2l0ZXJzICogMTAwMFxuXG4jIFRyYW5zZm9ybWVyOiBwYXJhbGxlbCBvdmVyIGFsbCBUIHBvc2l0aW9uc1xuc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG5mb3IgXyBpbiByYW5nZShuX2l0ZXJzKTpcbiAgICBvdXRfdGYgPSB0Zl9sYXllcih4KVxuICAgIG91dF90Zi5zdW0oKS5iYWNrd2FyZCgpXG50Zl9tcyA9ICh0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnQpIC8gbl9pdGVycyAqIDEwMDBcblxucHJpbnQoZlx1MDAyN0RldmljZToge2RldmljZX0sIFQ9e1R9LCBCPXtCfVx1MDAyNylcbnByaW50KGZcdTAwMjdSTk4gYXZnIGZ3ZCtid2Q6ICAgICAgICAge3Jubl9tczouMmZ9IG1zXHUwMDI3KVxucHJpbnQoZlx1MDAyN1RyYW5zZm9ybWVyIGF2ZyBmd2QrYndkOiB7dGZfbXM6LjJmfSBtc1x1MDAyNylcbnByaW50KFx1MDAyN1JOTiBpcyBzZXF1ZW50aWFsIG92ZXIgVDsgVHJhbnNmb3JtZXIgcGFyYWxsZWxpc2VzIGFsbCBUIHBvc2l0aW9ucy5cdTAwMjcpXG5wcmludChcdTAwMjdHUFUgdXRpbGlzYXRpb24gaXMgbXVjaCBsb3dlciBmb3IgUk5OIC0tIFQgc3RlcHMgbXVzdCBiZSBzZXJpYWwuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXB1dGF0aW9uYWwgQ29zdCBhbmQgQ29tcGxleGl0eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRvbWluYW50IGNvc3QgcGVyIFJOTiBzdGVwIGlzIHRoZSBX4oKV4oKVaOKCnOKCi+KCgSBwcm9kdWN0OiBPKEjCsikgRkxPUHMuIE92ZXIgVCBzdGVwcywgdG90YWwgY29zdCBpcyBPKFTCt0jCsikgZm9yIHRoZSByZWN1cnJlbnQgcGFydCwgcGx1cyBPKFTCt0jCt0kpIGZvciBpbnB1dCBwcm9qZWN0aW9ucy4gTWVtb3J5IHNjYWxlcyBhcyBPKFTCt0gpIHRvIHN0b3JlIGFsbCBoaWRkZW4gc3RhdGVzIGZvciBiYWNrcHJvcGFnYXRpb24uIEluIGNvbnRyYXN0LCBUcmFuc2Zvcm1lcnMgdXNlIE8oVMKywrdEKSBhdHRlbnRpb24gKHF1YWRyYXRpYyBpbiBzZXF1ZW5jZSBsZW5ndGgpIGJ1dCBPKETCsikgcGVyIHRva2VuIGZvciBmZWVkLWZvcndhcmQgbGF5ZXJzLiBGb3Igc2hvcnQgc2VxdWVuY2VzIChUXHUwMDNjMjAwKSwgUk5OcyBjYW4gYmUgY29tcGV0aXRpdmU7IGZvciBUXHUwMDNlMTAwMCwgdGhlIFRyYW5zZm9ybWVyXHUwMDI3cyBwYXJhbGxlbGlzbSBhZHZhbnRhZ2UgZG9taW5hdGVzIG9uIG1vZGVybiBoYXJkd2FyZSBkZXNwaXRlIGl0cyBxdWFkcmF0aWMgYXR0ZW50aW9uIGNvc3QuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJTZXF1ZW50aWFsIENvbXB1dGF0aW9uIEJvdHRsZW5lY2siLCJjb250ZW50IjoiVGhlIFJOTlx1MDAyN3MgcmVjdXJyZW5jZSBwcmV2ZW50cyBHUFUgcGFyYWxsZWxpc2F0aW9uIG92ZXIgdGltZS4gRm9yIEg9NTEyLCBUPTI1NiwgYSBzaW5nbGUgZm9yd2FyZCBwYXNzIHJlcXVpcmVzIDI1NiBzZXF1ZW50aWFsIG1hdHJpeCBtdWx0aXBsaWNhdGlvbnMuIFRoaXMgaXMgd2h5IFJOTnMgdHJhaW4gMTDigJM1MHggc2xvd2VyIHRoYW4gVHJhbnNmb3JtZXJzIG9uIHRoZSBzYW1lIHNlcXVlbmNlIGxlbmd0aCB1c2luZyBtb2Rlcm4gR1BVcy4gVHJhbnNmb3JtZXJzIHRyYWRlIE8oVMKyKSBhdHRlbnRpb24gbWVtb3J5IGZvciBPKDEvVCkgc2VxdWVudGlhbCBzdGVwcyDigJQgYSB3b3J0aHdoaWxlIHRyYWRlIGZvciBUIHVwIHRvIHNldmVyYWwgdGhvdXNhbmQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFRyYW5zZm9ybWVycyBSZXBsYWNlZCBSTk5zIGZvciBMb25nIFNlcXVlbmNlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVHJhbnNmb3JtZXJzIChWYXN3YW5pIGV0IGFsLiAyMDE3KSBzb2x2ZSB0d28gZnVuZGFtZW50YWwgUk5OIGxpbWl0YXRpb25zOiAoMSkgc2VxdWVudGlhbCBjb21wdXRhdGlvbiBieSB1c2luZyBzZWxmLWF0dGVudGlvbiB0aGF0IGNvbm5lY3RzIGFsbCBwb3NpdGlvbnMgaW4gTygxKSBzZXF1ZW50aWFsIHN0ZXBzLCBhbmQgKDIpIHRoZSB2YW5pc2hpbmcgZ3JhZGllbnQgcHJvYmxlbSBieSBwcm92aWRpbmcgZGlyZWN0IGdyYWRpZW50IHBhdGhzIGZyb20gZXZlcnkgb3V0cHV0IHBvc2l0aW9uIHRvIGV2ZXJ5IGlucHV0IHBvc2l0aW9uLiBSTk5zIHJlbWFpbiByZWxldmFudCBmb3Igc3RyZWFtaW5nIGluZmVyZW5jZSAoY29uc3RhbnQgbWVtb3J5LCBubyBzZXF1ZW5jZS1sZW5ndGggbGltaXQpLCBlZGdlIGRlcGxveW1lbnQgKHNtYWxsIHBhcmFtZXRlciBjb3VudCksIGFuZCB0YXNrcyB3aGVyZSBjYXVzYWxpdHkgaXMgcmVxdWlyZWQgd2l0aG91dCBmdXR1cmUgY29udGV4dC4gSG93ZXZlciwgZm9yIHByZS10cmFpbmluZyBvbiBsb25nIHRleHQsIGF1ZGlvLCBvciB2aWRlbywgVHJhbnNmb3JtZXJzIChvciB0aGVpciBsaW5lYXItYXR0ZW50aW9uIHZhcmlhbnRzKSBhcmUgdGhlIGRvbWluYW50IGFyY2hpdGVjdHVyZS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlJOTiBzdHJlbmd0aDogTyhIKSBtZW1vcnkgYXQgaW5mZXJlbmNlIOKAlCBubyBLViBjYWNoZSBuZWVkZWQ7IGlkZWFsIGZvciBzdHJlYW1pbmcgYW5kIGVtYmVkZGVkIHN5c3RlbXMuIiwiUk5OIHdlYWtuZXNzOiBPKFQpIHNlcXVlbnRpYWwgc3RlcHMgcHJldmVudCBHUFUgcGFyYWxsZWxpc207IHZhbmlzaGluZyBncmFkaWVudHMgbGltaXQgZWZmZWN0aXZlIG1lbW9yeSB0byB+MTAwIHN0ZXBzLiIsIlRyYW5zZm9ybWVyIHN0cmVuZ3RoOiBPKDEpIHNlcXVlbnRpYWwgc3RlcHM7IGRpcmVjdCBncmFkaWVudCBwYXRoczsgc2NhbGVzIHdpdGggZGF0YSBhbmQgY29tcHV0ZS4iLCJUcmFuc2Zvcm1lciB3ZWFrbmVzczogTyhUwrIpIGF0dGVudGlvbiBtZW1vcnk7IGZpeGVkIGNvbnRleHQgd2luZG93OyBubyBuYXRpdmUgc3RyZWFtaW5nLiIsIkxTVE0vR1JVIG1pdGlnYXRlIHZhbmlzaGluZyBncmFkaWVudHMgd2l0aCBnYXRpbmcgYnV0IHByZXNlcnZlIHNlcXVlbnRpYWwgY29tcHV0YXRpb24gYm90dGxlbmVjay4iLCJNYW1iYS9TNC9saW5lYXIgUk5OcyBhaW0gdG8gcmVjb3ZlciBwYXJhbGxlbGlzYWJsZSB0cmFpbmluZyB3aGlsZSByZXRhaW5pbmcgUk5OLXN0eWxlIGluZmVyZW5jZSBlZmZpY2llbmN5LiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Recurrent Computation — Hidden State and Weight Sharing

A Recurrent Neural Network (RNN) processes sequences by maintaining a hidden state hₜ that summarises all information seen up to time t. At each step the same weight matrices are applied: hₜ = tanh(Wₕₓxₜ + Wₕₕhₜ₋₁ + b), yₜ = Wₒhₜ. This weight sharing across time is the defining property of RNNs — unlike a feedforward network with separate parameters per position, the RNN uses identical Wₕₕ at every step, giving it O(H²) recurrent parameters regardless of sequence length T. The same mechanism that enables variable-length processing also introduces the vanishing gradient problem and prevents parallelisation over the time axis.

## The RNN Recurrence Equation

The core recurrence hₜ = tanh(Wₕₓxₜ + Wₕₕhₜ₋₁ + b) composes three operations: a linear projection of the input xₜ ∈ ℝᴵ via Wₕₓ ∈ ℝᴴˣᴵ, a linear projection of the previous hidden state hₜ₋₁ ∈ ℝᴴ via Wₕₕ ∈ ℝᴴˣᴴ, and a tanh nonlinearity that squashes the result to (-1, 1). The output yₜ = Wₒhₜ is a linear readout from the hidden state via Wₒ ∈ ℝᴼˣᴴ. Total parameters: H×I (Wₕₓ) + H×H (Wₕₕ) + H×O (Wₒ) + H (bias). Computational cost per step is O(H²) for the Wₕₕhₜ₋₁ product, giving O(T·H²) total for a sequence of length T.

## Weight Sharing Across Time

Weight sharing means the same Wₕₕ is multiplied at every time step. This is analogous to a convolutional filter being applied at every spatial position — it allows the model to generalise temporal patterns regardless of when they occur. Theoretically, RNNs with sufficient hidden size are Turing complete: they can simulate any computable function on sequences. Practically, learning long-range dependencies is limited by the vanishing gradient problem. The hidden state hₜ must compress the entire history into H numbers, creating an information bottleneck for very long sequences.

```python
import numpy as np

class VanillaRNN:
    def __init__(self, input_size, hidden_size, output_size):
        scale = 0.01
        self.Wxh = np.random.randn(hidden_size, input_size) * scale
        self.Whh = np.random.randn(hidden_size, hidden_size) * scale
        self.Why = np.random.randn(output_size, hidden_size) * scale
        self.bh  = np.zeros((hidden_size, 1))
        self.by  = np.zeros((output_size, 1))

    def forward(self, inputs, h_prev):
        self.hs = {-1: h_prev}
        self.ys = {}
        for t, x in enumerate(inputs):
            self.hs[t] = np.tanh(
                self.Wxh @ x + self.Whh @ self.hs[t - 1] + self.bh
            )
            self.ys[t] = self.Why @ self.hs[t] + self.by
        return self.ys, self.hs

np.random.seed(42)
T, I, H, O = 5, 4, 8, 3
rnn = VanillaRNN(I, H, O)
inputs = [np.random.randn(I, 1) for _ in range(T)]
h0 = np.zeros((H, 1))
ys, hs = rnn.forward(inputs, h0)
print(f'Sequence length T={T}, hidden size H={H}')
for t in range(T):
    print(f'  t={t}: h shape={hs[t].shape}, y shape={ys[t].shape}')
print(f'h_T norm = {np.linalg.norm(hs[T-1]):.4f}')
print('Same Whh applied at every step -- weight sharing across time.')
```

## PyTorch nn.RNN — Many-to-One and Many-to-Many

PyTorch's nn.RNN wraps the recurrence in an optimised CUDA kernel. The output tensor contains hidden states at all T steps; h_n is the final hidden state. For many-to-one tasks (classification), use h_n directly. For many-to-many (tagging, translation), use the full output sequence. One-to-many (generation) repeats a seed input for T steps. Bidirectional RNNs run one forward and one backward pass, concatenating hidden states — doubling the parameter count and output dimension.

```python
import torch
import torch.nn as nn

torch.manual_seed(42)
T, B, I, H = 10, 4, 8, 16  # seq_len, batch, input_dim, hidden_dim

rnn = nn.RNN(input_size=I, hidden_size=H, batch_first=True)
x = torch.randn(B, T, I)

# Many-to-many: use all time-step outputs
out, h_n = rnn(x)
print(f'Many-to-many: out.shape={out.shape}, h_n.shape={h_n.shape}')

# Many-to-one: last hidden state only
last_hidden = h_n.squeeze(0)  # (B, H)
print(f'Many-to-one: last_hidden.shape={last_hidden.shape}')

# One-to-many: repeat single input for T steps
single_input = torch.randn(B, 1, I).repeat(1, T, 1)
out_otm, _ = rnn(single_input)
print(f'One-to-many: out.shape={out_otm.shape}')

# Bidirectional RNN
rnn_bi = nn.RNN(input_size=I, hidden_size=H, batch_first=True, bidirectional=True)
out_bi, h_bi = rnn_bi(x)
print(f'Bidirectional: out.shape={out_bi.shape}, h_n.shape={h_bi.shape}')

total_params = sum(p.numel() for p in rnn.parameters())
print(f'Unidirectional RNN params: {total_params}')
print(f'  Wxh: {I}x{H}={I*H}, Whh: {H}x{H}={H*H}, bh: {H}')
```

## Stateful Inference for Long Sequences

For sequences longer than the training context (e.g., streaming audio or very long documents), the hidden state must be carried between batches. The key is to pass h_state from the previous chunk as the initial state for the next chunk. Gradients are not tracked across chunks during inference. During training, the hidden state is detached (h.detach()) to stop gradient flow into earlier chunks — this is the truncated BPTT pattern. Carrying state allows the model to use information from the entire sequence history at inference time, even if gradients only flow within chunks at training time.

```python
import torch
import torch.nn as nn

torch.manual_seed(0)
I, H, O, B = 8, 32, 4, 2
TOTAL_LEN = 500
CHUNK_SIZE = 50

rnn = nn.RNN(input_size=I, hidden_size=H, batch_first=True)
fc  = nn.Linear(H, O)
rnn.eval(); fc.eval()

long_seq = torch.randn(B, TOTAL_LEN, I)
h_state  = torch.zeros(1, B, H)  # (num_layers, batch, hidden)

outputs = []
with torch.no_grad():
    for start in range(0, TOTAL_LEN, CHUNK_SIZE):
        chunk = long_seq[:, start:start + CHUNK_SIZE, :]
        out, h_state = rnn(chunk, h_state)
        # h_state carries to next chunk — stateful inference
        logits = fc(out)
        outputs.append(logits)

all_out = torch.cat(outputs, dim=1)
print(f'Input length: {TOTAL_LEN}, chunk size: {CHUNK_SIZE}')
print(f'Number of chunks: {TOTAL_LEN // CHUNK_SIZE}')
print(f'Final output shape: {all_out.shape}')
print(f'Final hidden state norm: {h_state.norm().item():.4f}')
print('Hidden state carried across chunks -- full-sequence context at inference.')
```

## RNN Architectures

| Architecture | Use Case | Hidden State Handling | Batch Processing | Example Task |
| --- | --- | --- | --- | --- |
| Many-to-many (aligned) | Output at every input step | h_t used at each t | Pad to max length; mask output loss | POS tagging, NER, frame-level prediction |
| Many-to-one | Single output for whole sequence | Only final h_T used | Pad + pack sequences for efficiency | Sentiment analysis, sequence classification |
| One-to-many | Generate sequence from single input | Decoded step-by-step from h_0 | Replicate input for T steps | Image captioning, music generation |
| Encoder-decoder | Map sequence to sequence of different length | Encoder h_T initialises decoder | Fixed-length bottleneck; attention needed for long seqs | Machine translation, summarization |

## Sequential Computation and GPU Limitations

The recurrence hₜ = f(hₜ₋₁, xₜ) creates a strict sequential dependency: step t cannot begin until step t-1 is complete. This prevents parallelisation over the time axis. On a GPU with thousands of cores, only the matrix multiplications Wₕₓxₜ and Wₕₕhₜ₋₁ at each single step are parallelisable — but these are small compared to what a Transformer can parallelise (all T positions simultaneously). For T=512 and H=512, an RNN requires 512 sequential matrix multiplications of size 512×512, while a Transformer computes all attention in a single batched operation.

```python
import torch
import torch.nn as nn
import time

torch.manual_seed(42)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
B, T, I, H = 16, 64, 32, 64

rnn = nn.RNN(input_size=I, hidden_size=H, batch_first=True).to(device)
tf_layer = nn.TransformerEncoderLayer(
    d_model=I, nhead=4, dim_feedforward=128, batch_first=True
).to(device)

x = torch.randn(B, T, I, device=device)
n_iters = 50

# RNN: sequential over T steps
start = time.perf_counter()
for _ in range(n_iters):
    out_rnn, _ = rnn(x)
    out_rnn.sum().backward()
rnn_ms = (time.perf_counter() - start) / n_iters * 1000

# Transformer: parallel over all T positions
start = time.perf_counter()
for _ in range(n_iters):
    out_tf = tf_layer(x)
    out_tf.sum().backward()
tf_ms = (time.perf_counter() - start) / n_iters * 1000

print(f'Device: {device}, T={T}, B={B}')
print(f'RNN avg fwd+bwd:         {rnn_ms:.2f} ms')
print(f'Transformer avg fwd+bwd: {tf_ms:.2f} ms')
print('RNN is sequential over T; Transformer parallelises all T positions.')
print('GPU utilisation is much lower for RNN -- T steps must be serial.')
```

## Computational Cost and Complexity

The dominant cost per RNN step is the Wₕₕhₜ₋₁ product: O(H²) FLOPs. Over T steps, total cost is O(T·H²) for the recurrent part, plus O(T·H·I) for input projections. Memory scales as O(T·H) to store all hidden states for backpropagation. In contrast, Transformers use O(T²·D) attention (quadratic in sequence length) but O(D²) per token for feed-forward layers. For short sequences (T<200), RNNs can be competitive; for T>1000, the Transformer's parallelism advantage dominates on modern hardware despite its quadratic attention cost.

> **Sequential Computation Bottleneck**: The RNN's recurrence prevents GPU parallelisation over time. For H=512, T=256, a single forward pass requires 256 sequential matrix multiplications. This is why RNNs train 10–50x slower than Transformers on the same sequence length using modern GPUs. Transformers trade O(T²) attention memory for O(1/T) sequential steps — a worthwhile trade for T up to several thousand.

## Why Transformers Replaced RNNs for Long Sequences

Transformers (Vaswani et al. 2017) solve two fundamental RNN limitations: (1) sequential computation by using self-attention that connects all positions in O(1) sequential steps, and (2) the vanishing gradient problem by providing direct gradient paths from every output position to every input position. RNNs remain relevant for streaming inference (constant memory, no sequence-length limit), edge deployment (small parameter count), and tasks where causality is required without future context. However, for pre-training on long text, audio, or video, Transformers (or their linear-attention variants) are the dominant architecture.

- RNN strength: O(H) memory at inference — no KV cache needed; ideal for streaming and embedded systems.
- RNN weakness: O(T) sequential steps prevent GPU parallelism; vanishing gradients limit effective memory to ~100 steps.
- Transformer strength: O(1) sequential steps; direct gradient paths; scales with data and compute.
- Transformer weakness: O(T²) attention memory; fixed context window; no native streaming.
- LSTM/GRU mitigate vanishing gradients with gating but preserve sequential computation bottleneck.
- Mamba/S4/linear RNNs aim to recover parallelisable training while retaining RNN-style inference efficiency.

---

