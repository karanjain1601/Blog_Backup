---
title: "Bayesian Linear Regression"
slug: "bayesian-linear-regression"
description: "Derive the analytical posterior over weights, compute predictive distributions with uncertainty that grows away from training data, implement evidence maximisation for hyperparameter selection, and compare with frequentist ridge regression."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmF5ZXNpYW4gbGluZWFyIHJlZ3Jlc3Npb24gdHJlYXRzIHRoZSB3ZWlnaHQgdmVjdG9yIHcgYXMgYSByYW5kb20gdmFyaWFibGUgYW5kIGNvbXB1dGVzIGEgZnVsbCBwb3N0ZXJpb3IgZGlzdHJpYnV0aW9uIG92ZXIgdyBnaXZlbiB0aGUgZGF0YSwgcmF0aGVyIHRoYW4gYSBzaW5nbGUgcG9pbnQgZXN0aW1hdGUuIFRoaXMgZ2l2ZXMgcHJlZGljdGlvbnMgd2l0aCBwcmluY2lwbGVkIHVuY2VydGFpbnR5IHF1YW50aWZpY2F0aW9uOiB0aGUgcHJlZGljdGl2ZSBkaXN0cmlidXRpb24gaXMgYSBHYXVzc2lhbiB3aG9zZSB2YXJpYW5jZSByZWZsZWN0cyBib3RoIGFsZWF0b3JpYyBub2lzZSAoaXJyZWR1Y2libGUgZGF0YSBub2lzZSkgYW5kIGVwaXN0ZW1pYyB1bmNlcnRhaW50eSAodW5jZXJ0YWludHkgYWJvdXQgdGhlIHdlaWdodHMpLiBVbmxpa2UgZnJlcXVlbnRpc3QgY29uZmlkZW5jZSBpbnRlcnZhbHMgKHdoaWNoIHJlcXVpcmUgYXN5bXB0b3RpYyBhcHByb3hpbWF0aW9ucyksIEJheWVzaWFuIHVuY2VydGFpbnR5IGlzIGV4YWN0IHVuZGVyIHRoZSBHYXVzc2lhbiBwcmlvci1saWtlbGlob29kIG1vZGVsIGFuZCBncm93cyBuYXR1cmFsbHkgaW4gcmVnaW9ucyBmYXIgZnJvbSB0aGUgdHJhaW5pbmcgZGF0YS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmlvciwgTGlrZWxpaG9vZCwgYW5kIFBvc3RlcmlvciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2V0dXA6IEdhdXNzaWFuIHByaW9yIHAodykgPSBOKDAsIM6x4oG7wrlJKSB3aXRoIHByZWNpc2lvbiDOsSAoaW52ZXJzZSB2YXJpYW5jZSkuIEdhdXNzaWFuIGxpa2VsaWhvb2QgcCh5fFgsdykgPSBOKFh3LCDOsuKBu8K5SSkgd2l0aCBub2lzZSBwcmVjaXNpb24gzrIuIEJ5IEJheWVzXHUwMDI3IHRoZW9yZW06IHAod3xYLHkpIOKInSBwKHl8WCx3KcK3cCh3KSA9IE4ozrxfTiwgzqNfTikgd2hlcmUgzqNfTiA9ICjOsUkgKyDOsljhtYBYKeKBu8K5IGFuZCDOvF9OID0gzrLOo19OIFjhtYB5LiBUaGlzIGlzIGEgR2F1c3NpYW4gcG9zdGVyaW9yIOKAlCB0aGUgY29uanVnYXRlIHByb3BlcnR5IG9mIEdhdXNzaWFuIHByaW9ycyB3aXRoIEdhdXNzaWFuIGxpa2VsaWhvb2RzIGdpdmVzIGFuIGFuYWx5dGljYWxseSB0cmFjdGFibGUgcG9zdGVyaW9yLiBBcyBu4oaS4oieLCB0aGUgcG9zdGVyaW9yIGNvbmNlbnRyYXRlcyBvbiB0aGUgTUxFIGFuZCB0aGUgcHJpb3IgYmVjb21lcyBpcnJlbGV2YW50LiBUaGUgTUFQIGVzdGltYXRlIChwb3N0ZXJpb3IgbW9kZSkgaXMgaWRlbnRpY2FsIHRvIHRoZSByaWRnZSByZWdyZXNzaW9uIHNvbHV0aW9uIHdpdGggzrsgPSDOsS/Osi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxuXG5kZWYgYmF5ZXNpYW5fbHJfcG9zdGVyaW9yKFgsIHksIGFscGhhPTEuMCwgYmV0YT0yNS4wKTpcbiAgICBcIlwiXCJHYXVzc2lhbiBwb3N0ZXJpb3IgZm9yIEJheWVzaWFuIGxpbmVhciByZWdyZXNzaW9uLlxuICAgIFByaW9yOiB3IH4gTigwLCBhbHBoYV57LTF9IEkpXG4gICAgTGlrZWxpaG9vZDogeSB8IFgsdyB+IE4oWHcsIGJldGFeey0xfSBJKVxuICAgIFJldHVybnM6IG11X04gKHBvc3RlcmlvciBtZWFuKSwgU2lnbWFfTiAocG9zdGVyaW9yIGNvdmFyaWFuY2UpXG4gICAgXCJcIlwiXG4gICAgcCA9IFguc2hhcGVbMV1cbiAgICBTaWdtYV9OX2ludiA9IGFscGhhICogbnAuZXllKHApICsgYmV0YSAqIFguVCBAIFhcbiAgICBTaWdtYV9OID0gbnAubGluYWxnLmludihTaWdtYV9OX2ludilcbiAgICBtdV9OID0gYmV0YSAqIFNpZ21hX04gQCBYLlQgQCB5XG4gICAgcmV0dXJuIG11X04sIFNpZ21hX05cblxudHJ1ZV93ID0gbnAuYXJyYXkoWzEuNSwgLTAuOF0pXG5uID0gMzBcblggPSBucC5jb2x1bW5fc3RhY2soW25wLm9uZXMobiksIG5wLnJhbmRvbS51bmlmb3JtKC0zLCAzLCBuKV0pXG55ID0gWCBAIHRydWVfdyArIDAuMiAqIG5wLnJhbmRvbS5yYW5kbihuKVxuXG5hbHBoYSwgYmV0YSA9IDIuMCwgMjUuMFxubXVfTiwgU2lnbWFfTiA9IGJheWVzaWFuX2xyX3Bvc3RlcmlvcihYLCB5LCBhbHBoYSwgYmV0YSlcblxucHJpbnQoZlx1MDAyN1RydWUgd2VpZ2h0czogICB7dHJ1ZV93fVx1MDAyNylcbnByaW50KGZcdTAwMjdQb3N0ZXJpb3IgbWVhbjoge211X04ucm91bmQoNCl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1Bvc3RlcmlvciBzdGQ6ICB7bnAuc3FydChucC5kaWFnKFNpZ21hX04pKS5yb3VuZCg0KX1cdTAwMjcpXG5yaWRnZV9tYXAgPSBucC5saW5hbGcuc29sdmUoYWxwaGEvYmV0YSAqIG5wLmV5ZSgyKSArIFguVCBAIFgsIFguVCBAIHkpXG5wcmludChmXHUwMDI3UmlkZ2UgTUFQOiAgICAgIHtyaWRnZV9tYXAucm91bmQoNCl9ICAoc2hvdWxkIGVxdWFsIHBvc3RlcmlvciBtZWFuKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmVkaWN0aXZlIERpc3RyaWJ1dGlvbiB3aXRoIEVwaXN0ZW1pYyBVbmNlcnRhaW50eSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiR2l2ZW4gYSBuZXcgcG9pbnQgeCosIHRoZSBwcmVkaWN0aXZlIGRpc3RyaWJ1dGlvbiBpbnRlZ3JhdGVzIG91dCB0aGUgd2VpZ2h0IHVuY2VydGFpbnR5OiBwKHkqfHgqLCBYLCB5KSA9IOKIqyBwKHkqfHgqLHcpIHAod3xYLHkpIGR3ID0gTijOvF9O4bWAeCosIM+DwrIqKHgqKSkgd2hlcmUgz4PCsiooeCopID0gzrLigbvCuSArIHgq4bWAzqNfTiB4Ki4gVGhlIGZpcnN0IHRlcm0gzrLigbvCuSBpcyBpcnJlZHVjaWJsZSBhbGVhdG9yaWMgbm9pc2UuIFRoZSBzZWNvbmQgdGVybSB4KuG1gM6jX054KiBpcyBlcGlzdGVtaWMgdW5jZXJ0YWludHkg4oCUIGl0IGdyb3dzIGFzIHgqIG1vdmVzIGF3YXkgZnJvbSB0aGUgdHJhaW5pbmcgZGF0YSwgZ2l2aW5nIG5hdHVyYWxseSB3aWRlciBjb25maWRlbmNlIGJhbmRzIGluIGV4dHJhcG9sYXRpb24gcmVnaW9ucy4gVGhpcyBhdXRvbWF0aWMgdW5jZXJ0YWludHkgZ3Jvd3RoIGlzIHRoZSBrZXkgYWR2YW50YWdlIG92ZXIgZnJlcXVlbnRpc3QgcHJlZGljdGlvbiBpbnRlcnZhbHMsIHdoaWNoIHJlcXVpcmUgbGFyZ2UtbiBhcHByb3hpbWF0aW9ucyBhbmQgZG8gbm90IGF1dG9tYXRpY2FsbHkgZ3JvdyBpbiBkYXRhLXNwYXJzZSByZWdpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxubnAucmFuZG9tLnNlZWQoNDIpXG50cnVlX3cgPSBucC5hcnJheShbMC41LCAxLjJdKVxubiA9IDIwXG5YX3RyYWluXzFkID0gbnAucmFuZG9tLnVuaWZvcm0oLTIsIDIsIG4pXG5YX3RyYWluID0gbnAuY29sdW1uX3N0YWNrKFtucC5vbmVzKG4pLCBYX3RyYWluXzFkXSlcbnlfdHJhaW4gPSBYX3RyYWluIEAgdHJ1ZV93ICsgMC4zICogbnAucmFuZG9tLnJhbmRuKG4pXG5cbmFscGhhLCBiZXRhID0gMS4wLCAxMS4wXG5TaWdtYV9OX2ludiA9IGFscGhhICogbnAuZXllKDIpICsgYmV0YSAqIFhfdHJhaW4uVCBAIFhfdHJhaW5cblNpZ21hX04gPSBucC5saW5hbGcuaW52KFNpZ21hX05faW52KVxubXVfTiA9IGJldGEgKiBTaWdtYV9OIEAgWF90cmFpbi5UIEAgeV90cmFpblxuXG54X3Rlc3RfMWQgPSBucC5saW5zcGFjZSgtNSwgNSwgMjAwKSAgIyBpbmNsdWRlcyBleHRyYXBvbGF0aW9uIHJlZ2lvbnNcblhfdGVzdCA9IG5wLmNvbHVtbl9zdGFjayhbbnAub25lcygyMDApLCB4X3Rlc3RfMWRdKVxuXG55X3ByZWRfbWVhbiA9IFhfdGVzdCBAIG11X05cbnlfcHJlZF92YXIgID0gMS4wL2JldGEgKyBucC5hcnJheShbeCBAIFNpZ21hX04gQCB4IGZvciB4IGluIFhfdGVzdF0pXG55X3ByZWRfc3RkICA9IG5wLnNxcnQoeV9wcmVkX3ZhcilcblxucHJpbnQoXHUwMDI3UHJlZGljdGl2ZSB1bmNlcnRhaW50eSBncm93cyBpbiBleHRyYXBvbGF0aW9uIHJlZ2lvbjpcdTAwMjcpXG5mb3IgeF92YWwsIG11X3ZhbCwgc3RkX3ZhbCBpbiB6aXAoeF90ZXN0XzFkWzo6NDBdLCB5X3ByZWRfbWVhbls6OjQwXSwgeV9wcmVkX3N0ZFs6OjQwXSk6XG4gICAgcHJpbnQoZlx1MDAyNyAgeCo9e3hfdmFsOlx1MDAzZTYuMmZ9OiBwcmVkPXttdV92YWw6LjNmfSArLy0gezEuOTYqc3RkX3ZhbDouM2Z9ICg5NSUgQ0kpXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlcXVlbnRpYWwgQmF5ZXNpYW4gVXBkYXRpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik9uZSBlbGVnYW50IHByb3BlcnR5IG9mIEJheWVzaWFuIHJlZ3Jlc3Npb24gaXMgc2VxdWVudGlhbCB1cGRhdGluZzogdGhlIHBvc3RlcmlvciBhZnRlciBzZWVpbmcgbiBvYnNlcnZhdGlvbnMgc2VydmVzIGFzIHRoZSBwcmlvciBmb3Igb2JzZXJ2YXRpb24gbisxLiBTdGFydGluZyB3aXRoIHAodykgPSBOKG1fMCwgU18wKSwgYWZ0ZXIgb2JzZXJ2aW5nICh4X24sIHlfbikgdGhlIHBvc3RlcmlvciBpcyBOKG1fbiwgU19uKSB3aGVyZSBTX27igbvCuSA9IFNfe24tMX3igbvCuSArIM6yeF9ueOKCmeG1gCBhbmQgbV9uID0gU19uKFNfe24tMX3igbvCuW1fe24tMX0gKyDOsnlfbnhfbikuIFRoaXMgaXMgZXhhY3Qgb25saW5lIGxlYXJuaW5nIOKAlCBubyBuZWVkIHRvIHN0b3JlIHBhc3QgZGF0YSwgbm8gYXBwcm94aW1hdGlvbi4gVGhlIHBvc3RlcmlvciBwcmVjaXNpb24gKGludmVyc2UgY292YXJpYW5jZSkgZ3Jvd3Mgd2l0aCBlYWNoIG9ic2VydmF0aW9uLCBhbmQgdGhlIHVuY2VydGFpbnR5IGRlY3JlYXNlcyBtb25vdG9uaWNhbGx5LiBUaGlzIG1ha2VzIEJheWVzaWFuIHJlZ3Jlc3Npb24gbmF0dXJhbGx5IHN1aXRlZCBmb3IgcmVhbC10aW1lIHN5c3RlbXMgd2hlcmUgZGF0YSBhcnJpdmVzIHNlcXVlbnRpYWxseS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxudHJ1ZV93ID0gbnAuYXJyYXkoWzEuMCwgLTAuNSwgMC44XSlcbmJldGEsIGFscGhhLCBwX2RpbSA9IDkuMCwgMS4wLCAzXG5cbm0gPSBucC56ZXJvcyhwX2RpbSlcblNfaW52ID0gYWxwaGEgKiBucC5leWUocF9kaW0pXG5TID0gbnAubGluYWxnLmludihTX2ludilcblxuZm9yIG4gaW4gcmFuZ2UoMSwgMTAxKTpcbiAgICB4X24gPSBucC5yYW5kb20ucmFuZG4ocF9kaW0pXG4gICAgeV9uID0geF9uIEAgdHJ1ZV93ICsgbnAucmFuZG9tLnJhbmRuKCkgLyBucC5zcXJ0KGJldGEpXG4gICAgIyBSYW5rLTEgQmF5ZXNpYW4gdXBkYXRlXG4gICAgU19pbnZfbmV3ID0gU19pbnYgKyBiZXRhICogbnAub3V0ZXIoeF9uLCB4X24pXG4gICAgU19uZXcgPSBucC5saW5hbGcuaW52KFNfaW52X25ldylcbiAgICBtX25ldyA9IFNfbmV3IEAgKFNfaW52IEAgbSArIGJldGEgKiB5X24gKiB4X24pXG4gICAgU19pbnYsIFMsIG0gPSBTX2ludl9uZXcsIFNfbmV3LCBtX25ld1xuICAgIGlmIG4gaW4gWzEsIDUsIDEwLCAyNSwgNTAsIDEwMF06XG4gICAgICAgIHN0ZF93ID0gbnAuc3FydChucC5kaWFnKFMpKVxuICAgICAgICBwcmludChmXHUwMDI3bj17bjpcdTAwM2UzfTogbWVhbj17bS5yb3VuZCgzKX0sIHN0ZD17c3RkX3cucm91bmQoMyl9XHUwMDI3KVxuXG5wcmludChmXHUwMDI3VHJ1ZSB3OiB7dHJ1ZV93fVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFdmlkZW5jZSBNYXhpbWlzYXRpb24gZm9yIEh5cGVycGFyYW1ldGVyIFNlbGVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG1hcmdpbmFsIGxpa2VsaWhvb2QgKGV2aWRlbmNlKSBwKHl8WCwgzrEsIM6yKSA9IOKIqyBwKHl8WCx3KSBwKHd8zrEpIGR3IGludGVncmF0ZXMgb3V0IHRoZSB3ZWlnaHRzLCBnaXZpbmcgYSBtZWFzdXJlIG9mIGhvdyB3ZWxsIHRoZSBtb2RlbCAoYXQgZ2l2ZW4gzrEsIM6yKSBleHBsYWlucyB0aGUgZGF0YS4gTWF4aW1pc2luZyB0aGUgZXZpZGVuY2Ugb3ZlciDOsSBhbmQgzrIgKGNhbGxlZCBUeXBlLUlJIE1MIG9yIGVtcGlyaWNhbCBCYXllcykgc2VsZWN0cyBoeXBlcnBhcmFtZXRlcnMgd2l0aG91dCBjcm9zcy12YWxpZGF0aW9uIOKAlCB1c2luZyBhbGwgdHJhaW5pbmcgZGF0YS4gVGhlIGV2aWRlbmNlIGZhdm91cnMgbW9kZWxzIHRoYXQgYXJlIGNvbXBsZXggZW5vdWdoIHRvIGZpdCB0aGUgZGF0YSBidXQgbm90IHNvIGNvbXBsZXggdGhhdCB0aGV5IHNwcmVhZCBwcmlvciBtYXNzIG92ZXIgdG9vIG1hbnkgaXJyZWxldmFudCByZWdpb25zIChPY2NhbVx1MDAyN3MgUmF6b3IpLiBUaGlzIGlzIHRoZSBwcmluY2lwbGVkIGFsdGVybmF0aXZlIHRvIGhlbGQtb3V0IHZhbGlkYXRpb24gZm9yIGh5cGVycGFyYW1ldGVyIHNlbGVjdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5Lm9wdGltaXplIGltcG9ydCBtaW5pbWl6ZV9zY2FsYXJcblxubnAucmFuZG9tLnNlZWQoMClcbnRydWVfdyA9IG5wLmFycmF5KFsyLjAsIC0xLjBdKVxubiA9IDUwXG5YID0gbnAuY29sdW1uX3N0YWNrKFtucC5vbmVzKG4pLCBucC5yYW5kb20udW5pZm9ybSgtMywgMywgbildKVxueSA9IFggQCB0cnVlX3cgKyAwLjUgKiBucC5yYW5kb20ucmFuZG4obilcblxuZGVmIG5lZ19sb2dfZXZpZGVuY2UobG9nX2FscGhhLCBYLCB5LCBiZXRhPTQuMCk6XG4gICAgYWxwaGEgPSBucC5leHAobG9nX2FscGhhKVxuICAgIHAgPSBYLnNoYXBlWzFdXG4gICAgQSA9IGFscGhhICogbnAuZXllKHApICsgYmV0YSAqIFguVCBAIFhcbiAgICBBX2ludiA9IG5wLmxpbmFsZy5pbnYoQSlcbiAgICBtdV9OID0gYmV0YSAqIEFfaW52IEAgWC5UIEAgeVxuICAgIF8sIGxvZ2RldF9BID0gbnAubGluYWxnLnNsb2dkZXQoQSlcbiAgICByZXNpZCA9IHkgLSBYIEAgbXVfTlxuICAgIGxvZ19ldiA9ICgwLjUgKiBwICogbnAubG9nKGFscGhhKVxuICAgICAgICAgICAgICArIDAuNSAqIG4gKiBucC5sb2coYmV0YSlcbiAgICAgICAgICAgICAgLSAwLjUgKiBiZXRhICogcmVzaWQgQCByZXNpZFxuICAgICAgICAgICAgICAtIDAuNSAqIGFscGhhICogbXVfTiBAIG11X05cbiAgICAgICAgICAgICAgLSAwLjUgKiBsb2dkZXRfQVxuICAgICAgICAgICAgICAtIDAuNSAqIG4gKiBucC5sb2coMipucC5waSkpXG4gICAgcmV0dXJuIC1sb2dfZXZcblxuYmV0YV9maXhlZCA9IDQuMFxucmVzdWx0ID0gbWluaW1pemVfc2NhbGFyKG5lZ19sb2dfZXZpZGVuY2UsIGJvdW5kcz0oLTUsIDUpLCBtZXRob2Q9XHUwMDI3Ym91bmRlZFx1MDAyNyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgYXJncz0oWCwgeSwgYmV0YV9maXhlZCkpXG5vcHRfYWxwaGEgPSBucC5leHAocmVzdWx0LngpXG5wcmludChmXHUwMDI3RXZpZGVuY2Utb3B0aW1hbCBhbHBoYSA9IHtvcHRfYWxwaGE6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdFcXVpdmFsZW50IHJpZGdlIGxhbWJkYSA9IGFscGhhL2JldGEgPSB7b3B0X2FscGhhL2JldGFfZml4ZWQ6LjRmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiTUFQID0gUmlkZ2UsIEJ1dCBQb3N0ZXJpb3IgR2l2ZXMgTW9yZSIsImNvbnRlbnQiOiJUaGUgcG9zdGVyaW9yIG1vZGUgKE1BUCkgb2YgQmF5ZXNpYW4gbGluZWFyIHJlZ3Jlc3Npb24gd2l0aCBHYXVzc2lhbiBwcmlvciBpcyBpZGVudGljYWwgdG8gdGhlIHJpZGdlIHJlZ3Jlc3Npb24gc29sdXRpb24gd2l0aCDOuyA9IM6xL86yLiBIb3dldmVyLCByaWRnZSBnaXZlcyBvbmx5IGEgcG9pbnQgZXN0aW1hdGUsIHdoaWxlIEJheWVzaWFuIHJlZ3Jlc3Npb24gZ2l2ZXMgdGhlIGZ1bGwgcG9zdGVyaW9yIGRpc3RyaWJ1dGlvbi4gVGhlIHBvc3RlcmlvciBlbmFibGVzOiAoMSkgdW5jZXJ0YWludHkgcXVhbnRpZmljYXRpb24gb24gcHJlZGljdGlvbnM7ICgyKSBzZXF1ZW50aWFsIHVwZGF0aW5nIHdpdGhvdXQgc3RvcmluZyBwYXN0IGRhdGE7ICgzKSBldmlkZW5jZSBtYXhpbWlzYXRpb24gZm9yIGh5cGVycGFyYW1ldGVyIHNlbGVjdGlvbiB3aXRob3V0IGNyb3NzLXZhbGlkYXRpb24uIEFsbCB0aHJlZSBhcmUgdW5hdmFpbGFibGUgZnJvbSByaWRnZSByZWdyZXNzaW9uIGFsb25lLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbm5lY3Rpb24gdG8gR2F1c3NpYW4gUHJvY2Vzc2VzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXllc2lhbiBsaW5lYXIgcmVncmVzc2lvbiB3aXRoIGEgZmVhdHVyZSBtYXAgz4YoeCkgKGJhc2lzIGZ1bmN0aW9uczogcG9seW5vbWlhbHMsIFJCRnMsIGV0Yy4pIGdpdmVzIEJheWVzaWFuIHBvbHlub21pYWwva2VybmVsIHJlZ3Jlc3Npb24uIEluIHRoZSBsaW1pdCBvZiBpbmZpbml0ZSBiYXNpcyBmdW5jdGlvbnMsIHRoZSBwcmlvciBvdmVyIGZ1bmN0aW9ucyBpbmR1Y2VkIGJ5IHcgfiBOKDAsIM6x4oG7wrlJKSBiZWNvbWVzIGEgR2F1c3NpYW4gUHJvY2VzcyBwcmlvciBwKGYpID0gR1AoMCwgayh4LHhcdTAwMjcpKSB3aGVyZSBrKHgseFx1MDAyNykgPSDOseKBu8K5z4YoeCnhtYDPhih4XHUwMDI3KSBpcyB0aGUga2VybmVsLiBUaGlzIGNvbm5lY3Rpb24gc2hvd3MgdGhhdCBHYXVzc2lhbiBQcm9jZXNzZXMgYXJlIHRoZSBub25wYXJhbWV0cmljIGxpbWl0IG9mIEJheWVzaWFuIGxpbmVhciByZWdyZXNzaW9uIOKAlCB0aGV5IGV4dGVuZCB0aGUgY2xvc2VkLWZvcm0gcG9zdGVyaW9yIGFuZCBwcmVkaWN0aXZlIGRpc3RyaWJ1dGlvbiB0byBhbnkga2VybmVsIGZ1bmN0aW9uLCBwcm92aWRpbmcgdGhlIHNhbWUgdW5jZXJ0YWludHkgcXVhbnRpZmljYXRpb24gd2l0aG91dCBmaXhpbmcgYSBmaW5pdGUgYmFzaXMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlByb3BlcnR5IiwiRnJlcXVlbnRpc3QgUmlkZ2UiLCJCYXllc2lhbiBMaW5lYXIgUmVncmVzc2lvbiJdLCJyb3dzIjpbWyJPdXRwdXQiLCJTaW5nbGUgcG9pbnQgZXN0aW1hdGUgzrjMgiIsIkZ1bGwgcG9zdGVyaW9yIGRpc3RyaWJ1dGlvbiBOKM68X04sIM6jX04pIl0sWyJVbmNlcnRhaW50eSIsIkJvb3RzdHJhcCBvciBhc3ltcHRvdGljIENJIiwiRXhhY3QgcG9zdGVyaW9yOyBncm93cyBpbiBleHRyYXBvbGF0aW9uIHJlZ2lvbnMiXSxbIkh5cGVycGFyYW1ldGVyIHNlbGVjdGlvbiIsIkNyb3NzLXZhbGlkYXRpb24gKG5lZWRzIGhlbGQtb3V0IGRhdGEpIiwiRXZpZGVuY2UgbWF4aW1pc2F0aW9uICh1c2VzIGFsbCB0cmFpbmluZyBkYXRhKSJdLFsiQ29tcHV0YXRpb24iLCJPKHDCsykgbWF0cml4IHNvbHZlIiwiTyhwwrMpIG1hdHJpeCBpbnZlcnNpb24g4oCUIHNhbWUgY29zdCJdLFsiU2VxdWVudGlhbCB1cGRhdGUiLCJSZWZpdCBmcm9tIHNjcmF0Y2giLCJFeGFjdCBPKHDCsikgcmFuay0xIHVwZGF0ZSBwZXIgc2FtcGxlIl0sWyJQcmVkaWN0aW9uIiwixbcgPSDOvF9O4bWAeCoiLCJwKHkqfHgqKSA9IE4ozrxfTuG1gHgqLCDOsuKBu8K5ICsgeCrhtYDOo19OeCopIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkdhdXNzaWFuIHByaW9ycyBvdmVyIHcgY29ycmVzcG9uZCB0byBMMiAoUmlkZ2UpIHJlZ3VsYXJpc2F0aW9uIOKAlCB0aGUgTUFQIHNvbHV0aW9uIGlzIGlkZW50aWNhbC4iLCJVc2UgZXZpZGVuY2UgbWF4aW1pc2F0aW9uIChUeXBlLUlJIE1MKSB0byBzZWxlY3QgYWxwaGEgYW5kIGJldGEgd2l0aG91dCBjcm9zcy12YWxpZGF0aW9uLiIsIlNlcXVlbnRpYWwgdXBkYXRpbmcgZW5hYmxlcyBleGFjdCBvbmxpbmUgbGVhcm5pbmcg4oCUIGlkZWFsIGZvciBzdHJlYW1pbmcgcmVncmVzc2lvbiB0YXNrcy4iLCJQcmVkaWN0aXZlIHVuY2VydGFpbnR5IGdyb3dzIGluIGV4dHJhcG9sYXRpb24gcmVnaW9ucyDigJQgYWx3YXlzIHBsb3QgdGhlIHVuY2VydGFpbnR5IGJhbmRzLiIsIkZvciBub25saW5lYXIgcmVncmVzc2lvbiwgZXh0ZW5kIHRvIEdhdXNzaWFuIFByb2Nlc3NlcyAodGhlIGluZmluaXRlLWJhc2lzIGxpbWl0KS4iLCJGb3Igbm9uLUdhdXNzaWFuIGxpa2VsaWhvb2RzIChjbGFzc2lmaWNhdGlvbiksIHVzZSBMYXBsYWNlIGFwcHJveGltYXRpb24gb3IgdmFyaWF0aW9uYWwgaW5mZXJlbmNlIGZvciB0aGUgcG9zdGVyaW9yLiJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IkFsZWF0b3JpYyB2cyBFcGlzdGVtaWMgVW5jZXJ0YWludHkiLCJjb250ZW50IjoiVGhlIHByZWRpY3RpdmUgdmFyaWFuY2UgZGVjb21wb3NlcyBhcyBzaWdtYV4yKih4KikgPSBiZXRhXnstMX0gKyB4Kl5UIFNpZ21hX04geCouIFRoZSBmaXJzdCB0ZXJtIGJldGFeey0xfSBpcyBhbGVhdG9yaWMgdW5jZXJ0YWludHkg4oCUIGlycmVkdWNpYmxlIG5vaXNlIGluaGVyZW50IHRvIHRoZSBkYXRhIGdlbmVyYXRpbmcgcHJvY2Vzcy4gVGhlIHNlY29uZCB0ZXJtIHgqXlQgU2lnbWFfTiB4KiBpcyBlcGlzdGVtaWMgdW5jZXJ0YWludHkg4oCUIHVuY2VydGFpbnR5IGFib3V0IHRoZSBtb2RlbCB3ZWlnaHRzIGR1ZSB0byBsaW1pdGVkIGRhdGEuIEVwaXN0ZW1pYyB1bmNlcnRhaW50eSBzaHJpbmtzIHRvd2FyZCB6ZXJvIGFzIG4gZ3Jvd3MgYW5kIGFzIHgqIG1vdmVzIGludG8gZGF0YS1kZW5zZSByZWdpb25zLiBUaGlzIGRlY29tcG9zaXRpb24gaXMgbm90IGRpcmVjdGx5IGF2YWlsYWJsZSBmcm9tIGZyZXF1ZW50aXN0IG1ldGhvZHMgYW5kIGlzIGEga2V5IGFkdmFudGFnZSBvZiB0aGUgQmF5ZXNpYW4gZnJhbWV3b3JrIGZvciBzYWZldHktY3JpdGljYWwgYXBwbGljYXRpb25zLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGV2aWRlbmNlIChtYXJnaW5hbCBsaWtlbGlob29kKSBoYXMgYW4gT2NjYW0gZmFjdG9yIGludGVycHJldGF0aW9uLiBBIG1vZGVsIHdpdGggZGlmZnVzZSBwcmlvciAoc21hbGwgYWxwaGEpIGNhbiBmaXQgbWFueSBwb3NzaWJsZSBkYXRhc2V0cywgYnV0IG1vc3QgZG9uXHUwMDI3dCBsb29rIGxpa2UgeSDigJQgc28gdGhlIGV2aWRlbmNlIGlzIHNwcmVhZCB0aGluLiBBIG1vZGVsIHdpdGggY29uY2VudHJhdGVkIHByaW9yIChsYXJnZSBhbHBoYSwgd2VpZ2h0cyBuZWFyIHplcm8pIGZpdHMgZmV3ZXIgZGF0YXNldHMsIGJ1dCB3aGVuIGl0IGZpdHMgeSB3ZWxsIHRoZSBldmlkZW5jZSBpcyBoaWdoLiBUaGlzIGF1dG9tYXRpYyBjb21wbGV4aXR5IHBlbmFsaXNhdGlvbiBtZWFucyBldmlkZW5jZSBtYXhpbWlzYXRpb24gYXZvaWRzIG92ZXJmaXR0aW5nIGh5cGVycGFyYW1ldGVycyBldmVuIHdpdGhvdXQgaGVsZC1vdXQgZGF0YSDigJQgaXQgaW1wbGVtZW50cyBPY2NhbVx1MDAyN3MgUmF6b3IgZm9ybWFsbHkuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXllc2lhbiBsaW5lYXIgcmVncmVzc2lvbiB3aXRoIHBvbHlub21pYWwgYmFzaXMgZnVuY3Rpb25zIHBoaSh4KSA9IFsxLCB4LCB4XjIsIC4uLiwgeF5NXV5UIGdpdmVzIEJheWVzaWFuIHBvbHlub21pYWwgcmVncmVzc2lvbi4gVGhlIHByaW9yIHcgfiBOKDAsIGFscGhhXnstMX1JKSBjb21iaW5lZCB3aXRoIHBvbHlub21pYWwgZmVhdHVyZXMgaW5kdWNlcyBhIHByaW9yIG92ZXIgcG9seW5vbWlhbCBmdW5jdGlvbnMuIEV2aWRlbmNlIG1heGltaXNhdGlvbiBvdmVyIGFscGhhIGFuZCBNIHNlbGVjdHMgdGhlIG9wdGltYWwgcG9seW5vbWlhbCBkZWdyZWUgd2l0aG91dCBjcm9zcy12YWxpZGF0aW9uLiBJbiB0aGUgbGltaXQgb2YgaW5maW5pdGUgYmFzaXMgZnVuY3Rpb25zICh1c2luZyBhIGtlcm5lbCBmdW5jdGlvbiksIEJheWVzaWFuIGxpbmVhciByZWdyZXNzaW9uIGJlY29tZXMgYSBHYXVzc2lhbiBQcm9jZXNzIOKAlCB0aGUgbm9ucGFyYW1ldHJpYyBleHRlbnNpb24gdGhhdCBwcm92aWRlcyB0aGUgc2FtZSBjbG9zZWQtZm9ybSBwb3N0ZXJpb3IgYW5kIHByZWRpY3RpdmUgZGlzdHJpYnV0aW9uIGZvciBhbnkga2VybmVsLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Bayesian Linear Regression

Bayesian linear regression treats the weight vector w as a random variable and computes a full posterior distribution over w given the data, rather than a single point estimate. This gives predictions with principled uncertainty quantification: the predictive distribution is a Gaussian whose variance reflects both aleatoric noise (irreducible data noise) and epistemic uncertainty (uncertainty about the weights). Unlike frequentist confidence intervals (which require asymptotic approximations), Bayesian uncertainty is exact under the Gaussian prior-likelihood model and grows naturally in regions far from the training data.

## Prior, Likelihood, and Posterior

Setup: Gaussian prior p(w) = N(0, α⁻¹I) with precision α (inverse variance). Gaussian likelihood p(y|X,w) = N(Xw, β⁻¹I) with noise precision β. By Bayes' theorem: p(w|X,y) ∝ p(y|X,w)·p(w) = N(μ_N, Σ_N) where Σ_N = (αI + βXᵀX)⁻¹ and μ_N = βΣ_N Xᵀy. This is a Gaussian posterior — the conjugate property of Gaussian priors with Gaussian likelihoods gives an analytically tractable posterior. As n→∞, the posterior concentrates on the MLE and the prior becomes irrelevant. The MAP estimate (posterior mode) is identical to the ridge regression solution with λ = α/β.

```python
import numpy as np

np.random.seed(42)

def bayesian_lr_posterior(X, y, alpha=1.0, beta=25.0):
    """Gaussian posterior for Bayesian linear regression.
    Prior: w ~ N(0, alpha^{-1} I)
    Likelihood: y | X,w ~ N(Xw, beta^{-1} I)
    Returns: mu_N (posterior mean), Sigma_N (posterior covariance)
    """
    p = X.shape[1]
    Sigma_N_inv = alpha * np.eye(p) + beta * X.T @ X
    Sigma_N = np.linalg.inv(Sigma_N_inv)
    mu_N = beta * Sigma_N @ X.T @ y
    return mu_N, Sigma_N

true_w = np.array([1.5, -0.8])
n = 30
X = np.column_stack([np.ones(n), np.random.uniform(-3, 3, n)])
y = X @ true_w + 0.2 * np.random.randn(n)

alpha, beta = 2.0, 25.0
mu_N, Sigma_N = bayesian_lr_posterior(X, y, alpha, beta)

print(f'True weights:   {true_w}')
print(f'Posterior mean: {mu_N.round(4)}')
print(f'Posterior std:  {np.sqrt(np.diag(Sigma_N)).round(4)}')
ridge_map = np.linalg.solve(alpha/beta * np.eye(2) + X.T @ X, X.T @ y)
print(f'Ridge MAP:      {ridge_map.round(4)}  (should equal posterior mean)')
```

## Predictive Distribution with Epistemic Uncertainty

Given a new point x*, the predictive distribution integrates out the weight uncertainty: p(y*|x*, X, y) = ∫ p(y*|x*,w) p(w|X,y) dw = N(μ_Nᵀx*, σ²*(x*)) where σ²*(x*) = β⁻¹ + x*ᵀΣ_N x*. The first term β⁻¹ is irreducible aleatoric noise. The second term x*ᵀΣ_Nx* is epistemic uncertainty — it grows as x* moves away from the training data, giving naturally wider confidence bands in extrapolation regions. This automatic uncertainty growth is the key advantage over frequentist prediction intervals, which require large-n approximations and do not automatically grow in data-sparse regions.

```python
import numpy as np

np.random.seed(42)
true_w = np.array([0.5, 1.2])
n = 20
X_train_1d = np.random.uniform(-2, 2, n)
X_train = np.column_stack([np.ones(n), X_train_1d])
y_train = X_train @ true_w + 0.3 * np.random.randn(n)

alpha, beta = 1.0, 11.0
Sigma_N_inv = alpha * np.eye(2) + beta * X_train.T @ X_train
Sigma_N = np.linalg.inv(Sigma_N_inv)
mu_N = beta * Sigma_N @ X_train.T @ y_train

x_test_1d = np.linspace(-5, 5, 200)  # includes extrapolation regions
X_test = np.column_stack([np.ones(200), x_test_1d])

y_pred_mean = X_test @ mu_N
y_pred_var  = 1.0/beta + np.array([x @ Sigma_N @ x for x in X_test])
y_pred_std  = np.sqrt(y_pred_var)

print('Predictive uncertainty grows in extrapolation region:')
for x_val, mu_val, std_val in zip(x_test_1d[::40], y_pred_mean[::40], y_pred_std[::40]):
    print(f'  x*={x_val:>6.2f}: pred={mu_val:.3f} +/- {1.96*std_val:.3f} (95% CI)')
```

## Sequential Bayesian Updating

One elegant property of Bayesian regression is sequential updating: the posterior after seeing n observations serves as the prior for observation n+1. Starting with p(w) = N(m_0, S_0), after observing (x_n, y_n) the posterior is N(m_n, S_n) where S_n⁻¹ = S_{n-1}⁻¹ + βx_nxₙᵀ and m_n = S_n(S_{n-1}⁻¹m_{n-1} + βy_nx_n). This is exact online learning — no need to store past data, no approximation. The posterior precision (inverse covariance) grows with each observation, and the uncertainty decreases monotonically. This makes Bayesian regression naturally suited for real-time systems where data arrives sequentially.

```python
import numpy as np

np.random.seed(42)
true_w = np.array([1.0, -0.5, 0.8])
beta, alpha, p_dim = 9.0, 1.0, 3

m = np.zeros(p_dim)
S_inv = alpha * np.eye(p_dim)
S = np.linalg.inv(S_inv)

for n in range(1, 101):
    x_n = np.random.randn(p_dim)
    y_n = x_n @ true_w + np.random.randn() / np.sqrt(beta)
    # Rank-1 Bayesian update
    S_inv_new = S_inv + beta * np.outer(x_n, x_n)
    S_new = np.linalg.inv(S_inv_new)
    m_new = S_new @ (S_inv @ m + beta * y_n * x_n)
    S_inv, S, m = S_inv_new, S_new, m_new
    if n in [1, 5, 10, 25, 50, 100]:
        std_w = np.sqrt(np.diag(S))
        print(f'n={n:>3}: mean={m.round(3)}, std={std_w.round(3)}')

print(f'True w: {true_w}')
```

## Evidence Maximisation for Hyperparameter Selection

The marginal likelihood (evidence) p(y|X, α, β) = ∫ p(y|X,w) p(w|α) dw integrates out the weights, giving a measure of how well the model (at given α, β) explains the data. Maximising the evidence over α and β (called Type-II ML or empirical Bayes) selects hyperparameters without cross-validation — using all training data. The evidence favours models that are complex enough to fit the data but not so complex that they spread prior mass over too many irrelevant regions (Occam's Razor). This is the principled alternative to held-out validation for hyperparameter selection.

```python
import numpy as np
from scipy.optimize import minimize_scalar

np.random.seed(0)
true_w = np.array([2.0, -1.0])
n = 50
X = np.column_stack([np.ones(n), np.random.uniform(-3, 3, n)])
y = X @ true_w + 0.5 * np.random.randn(n)

def neg_log_evidence(log_alpha, X, y, beta=4.0):
    alpha = np.exp(log_alpha)
    p = X.shape[1]
    A = alpha * np.eye(p) + beta * X.T @ X
    A_inv = np.linalg.inv(A)
    mu_N = beta * A_inv @ X.T @ y
    _, logdet_A = np.linalg.slogdet(A)
    resid = y - X @ mu_N
    log_ev = (0.5 * p * np.log(alpha)
              + 0.5 * n * np.log(beta)
              - 0.5 * beta * resid @ resid
              - 0.5 * alpha * mu_N @ mu_N
              - 0.5 * logdet_A
              - 0.5 * n * np.log(2*np.pi))
    return -log_ev

beta_fixed = 4.0
result = minimize_scalar(neg_log_evidence, bounds=(-5, 5), method='bounded',
                          args=(X, y, beta_fixed))
opt_alpha = np.exp(result.x)
print(f'Evidence-optimal alpha = {opt_alpha:.4f}')
print(f'Equivalent ridge lambda = alpha/beta = {opt_alpha/beta_fixed:.4f}')
```

> **MAP = Ridge, But Posterior Gives More**: The posterior mode (MAP) of Bayesian linear regression with Gaussian prior is identical to the ridge regression solution with λ = α/β. However, ridge gives only a point estimate, while Bayesian regression gives the full posterior distribution. The posterior enables: (1) uncertainty quantification on predictions; (2) sequential updating without storing past data; (3) evidence maximisation for hyperparameter selection without cross-validation. All three are unavailable from ridge regression alone.

## Connection to Gaussian Processes

Bayesian linear regression with a feature map φ(x) (basis functions: polynomials, RBFs, etc.) gives Bayesian polynomial/kernel regression. In the limit of infinite basis functions, the prior over functions induced by w ~ N(0, α⁻¹I) becomes a Gaussian Process prior p(f) = GP(0, k(x,x')) where k(x,x') = α⁻¹φ(x)ᵀφ(x') is the kernel. This connection shows that Gaussian Processes are the nonparametric limit of Bayesian linear regression — they extend the closed-form posterior and predictive distribution to any kernel function, providing the same uncertainty quantification without fixing a finite basis.

| Property | Frequentist Ridge | Bayesian Linear Regression |
| --- | --- | --- |
| Output | Single point estimate θ̂ | Full posterior distribution N(μ_N, Σ_N) |
| Uncertainty | Bootstrap or asymptotic CI | Exact posterior; grows in extrapolation regions |
| Hyperparameter selection | Cross-validation (needs held-out data) | Evidence maximisation (uses all training data) |
| Computation | O(p³) matrix solve | O(p³) matrix inversion — same cost |
| Sequential update | Refit from scratch | Exact O(p²) rank-1 update per sample |
| Prediction | ŷ = μ_Nᵀx* | p(y*|x*) = N(μ_Nᵀx*, β⁻¹ + x*ᵀΣ_Nx*) |

- Gaussian priors over w correspond to L2 (Ridge) regularisation — the MAP solution is identical.
- Use evidence maximisation (Type-II ML) to select alpha and beta without cross-validation.
- Sequential updating enables exact online learning — ideal for streaming regression tasks.
- Predictive uncertainty grows in extrapolation regions — always plot the uncertainty bands.
- For nonlinear regression, extend to Gaussian Processes (the infinite-basis limit).
- For non-Gaussian likelihoods (classification), use Laplace approximation or variational inference for the posterior.

> **Aleatoric vs Epistemic Uncertainty**: The predictive variance decomposes as sigma^2*(x*) = beta^{-1} + x*^T Sigma_N x*. The first term beta^{-1} is aleatoric uncertainty — irreducible noise inherent to the data generating process. The second term x*^T Sigma_N x* is epistemic uncertainty — uncertainty about the model weights due to limited data. Epistemic uncertainty shrinks toward zero as n grows and as x* moves into data-dense regions. This decomposition is not directly available from frequentist methods and is a key advantage of the Bayesian framework for safety-critical applications.

The evidence (marginal likelihood) has an Occam factor interpretation. A model with diffuse prior (small alpha) can fit many possible datasets, but most don't look like y — so the evidence is spread thin. A model with concentrated prior (large alpha, weights near zero) fits fewer datasets, but when it fits y well the evidence is high. This automatic complexity penalisation means evidence maximisation avoids overfitting hyperparameters even without held-out data — it implements Occam's Razor formally.

Bayesian linear regression with polynomial basis functions phi(x) = [1, x, x^2, ..., x^M]^T gives Bayesian polynomial regression. The prior w ~ N(0, alpha^{-1}I) combined with polynomial features induces a prior over polynomial functions. Evidence maximisation over alpha and M selects the optimal polynomial degree without cross-validation. In the limit of infinite basis functions (using a kernel function), Bayesian linear regression becomes a Gaussian Process — the nonparametric extension that provides the same closed-form posterior and predictive distribution for any kernel.

---

