---
title: "Bayesian Optimization — Surrogate Models and the BO Loop"
slug: "bayesian-optimization"
description: "Sequential model-based optimization of expensive black-box functions using a GP surrogate and acquisition functions."
tags: ["bayesian-optimization", "gaussian-processes", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWFueSByZWFsLXdvcmxkIG9wdGltaXphdGlvbiBwcm9ibGVtcyDigJQgdHVuaW5nIG5ldXJhbC1uZXR3b3JrIGh5cGVycGFyYW1ldGVycywgZGVzaWduaW5nIG5ldyBkcnVnIG1vbGVjdWxlcywgZmluZGluZyBvcHRpbWFsIGFsbG95IGNvbXBvc2l0aW9ucyDigJQgc2hhcmUgb25lIGJydXRhbCBjb25zdHJhaW50OiBldmVyeSBmdW5jdGlvbiBldmFsdWF0aW9uIGlzIGV4cGVuc2l2ZS4gQSBzaW5nbGUgdHJhaW5pbmcgcnVuIGNhbiB0YWtlIGhvdXJzOyBhIGxhYiBzeW50aGVzaXMgY2FuIGNvc3QgdGhvdXNhbmRzIG9mIGRvbGxhcnMuIEdyaWQgc2VhcmNoIGFuZCByYW5kb20gc2VhcmNoIHdhc3RlIHRob3NlIGV2YWx1YXRpb25zIGJ5IGlnbm9yaW5nIGV2ZXJ5dGhpbmcgbGVhcm5lZCBzbyBmYXIuIEJheWVzaWFuIE9wdGltaXphdGlvbiAoQk8pIGlzIGEgcHJpbmNpcGxlZCwgc2FtcGxlLWVmZmljaWVudCBhbHRlcm5hdGl2ZSB0aGF0IGJ1aWxkcyBhIHByb2JhYmlsaXN0aWMgbW9kZWwgb2YgdGhlIG9iamVjdGl2ZSBhbmQgdXNlcyBpdCB0byBkZWNpZGUgKndoZXJlIHRvIGxvb2sgbmV4dCouIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIEJheWVzaWFuIE9wdGltaXphdGlvbiBMb29wIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCTyBpcyBhIHNlcXVlbnRpYWwgZGVjaXNpb24tbWFraW5nIGFsZ29yaXRobS4gQXQgZWFjaCBpdGVyYXRpb24gaXQgcGVyZm9ybXMgZm91ciBzdGVwczogKDEpIGZpdCBhIHN1cnJvZ2F0ZSBtb2RlbCB0byBhbGwgb2JzZXJ2YXRpb25zIGNvbGxlY3RlZCBzbyBmYXIsICgyKSBtYXhpbWl6ZSBhbiBhY3F1aXNpdGlvbiBmdW5jdGlvbiBvdmVyIHRoZSBzdXJyb2dhdGUgdG8gY2hvb3NlIHRoZSBuZXh0IGNhbmRpZGF0ZSBwb2ludCwgKDMpIGV2YWx1YXRlIHRoZSBleHBlbnNpdmUgb2JqZWN0aXZlIGF0IHRoYXQgcG9pbnQsIGFuZCAoNCkgYWRkIHRoZSBuZXcgb2JzZXJ2YXRpb24gdG8gdGhlIGRhdGFzZXQgYW5kIHJlcGVhdC4gQWZ0ZXIgYSBidWRnZXQgb2YgZXZhbHVhdGlvbnMgaXMgZXhoYXVzdGVkLCB0aGUgYmVzdCBvYnNlcnZlZCBwb2ludCBpcyByZXR1cm5lZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6dHJ1ZSwiaXRlbXMiOlsiRml0IHN1cnJvZ2F0ZSBwKGYgfCBEKSB0byBjdXJyZW50IG9ic2VydmF0aW9ucyBEID0geyh44bWiLCB54bWiKX0iLCJNYXhpbWl6ZSBhY3F1aXNpdGlvbiDOsSh4OyBEKSB0byBzZWxlY3QgbmV4dCBxdWVyeSB44oKZ4oKR4oKT4oKcIiwiRXZhbHVhdGUgdGhlIHRydWUgb2JqZWN0aXZlOiB54oKZ4oKR4oKT4oKcID0gZih44oKZ4oKR4oKT4oKcKSArIM61IiwiVXBkYXRlIGRhdGFzZXQgRCDihpAgRCDiiKogeyh44oKZ4oKR4oKT4oKcLCB54oKZ4oKR4oKT4oKcKX0gYW5kIGdvIHRvIHN0ZXAgMSJdfSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldoeSBOb3QgSnVzdCBPcHRpbWl6ZSB0aGUgU3Vycm9nYXRlIERpcmVjdGx5PyIsImNvbnRlbnQiOiJUaGUgc3Vycm9nYXRlIGlzIGNoZWFwIHRvIGV2YWx1YXRlLCBzbyB3ZSBjYW4gb3B0aW1pemUgaXQgd2l0aCBhbnkgZ3JhZGllbnQtYmFzZWQgb3IgZXZvbHV0aW9uYXJ5IG1ldGhvZC4gVGhlIGFjcXVpc2l0aW9uIGZ1bmN0aW9uIGlzIGFsc28gY2hlYXAgYW5kIGVuY29kZXMgd2hlcmUgdG8gcXVlcnkgbmV4dCBnaXZlbiB1bmNlcnRhaW50eSDigJQgdGhlIHRydWUgb2JqZWN0aXZlIGYgaXMgb25seSBjYWxsZWQgb25jZSBwZXIgQk8gaXRlcmF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdhdXNzaWFuIFByb2Nlc3NlcyBhcyB0aGUgSWRlYWwgU3Vycm9nYXRlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIEdhdXNzaWFuIFByb2Nlc3MgKEdQKSBpcyBhIGRpc3RyaWJ1dGlvbiBvdmVyIGZ1bmN0aW9ucy4gR2l2ZW4gdHJhaW5pbmcgZGF0YSwgdGhlIEdQIHBvc3RlcmlvciBwcm92aWRlcyBhIG1lYW4gcHJlZGljdGlvbiDOvCh4KSBhbmQgYSBjYWxpYnJhdGVkIHVuY2VydGFpbnR5IGVzdGltYXRlIM+DKHgpIGF0IGV2ZXJ5IGlucHV0LiBUaGlzIGlzIGV4YWN0bHkgd2hhdCBhIGdvb2Qgc3Vycm9nYXRlIG5lZWRzOiBub3QganVzdCBhIHByZWRpY3Rpb24sIGJ1dCBhbiBob25lc3QgYXNzZXNzbWVudCBvZiBob3cgY29uZmlkZW50IGl0IGlzLiBUaGUgR1AgaXMgbm9uLXBhcmFtZXRyaWMg4oCUIGl0cyBlZmZlY3RpdmUgY29tcGxleGl0eSBncm93cyB3aXRoIGRhdGEg4oCUIGFuZCBpdHMgcHJlZGljdGlvbnMgYXJlIGFuYWx5dGljYWxseSB0cmFjdGFibGUgdW5kZXIgR2F1c3NpYW4gbm9pc2UuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgR1AgaXMgZnVsbHkgc3BlY2lmaWVkIGJ5IGEgbWVhbiBmdW5jdGlvbiBtKHgpIChvZnRlbiBzZXQgdG8gemVybykgYW5kIGEgY292YXJpYW5jZSBrZXJuZWwgayh4LCB44oCyKS4gVGhlIE1hdMOpcm4tNS8yIGtlcm5lbCBpcyB0aGUgZGVmYXVsdCBjaG9pY2UgaW4gbW9zdCBCTyBsaWJyYXJpZXMgYmVjYXVzZSBpdCBwcm9kdWNlcyBmdW5jdGlvbnMgdGhhdCBhcmUgdHdpY2UgZGlmZmVyZW50aWFibGUg4oCUIHNtb290aGVyIHRoYW4gYSByb3VnaCBwcm9jZXNzIGJ1dCByb3VnaGVyIHRoYW4gaW5maW5pdGVseSBkaWZmZXJlbnRpYWJsZSBSQkYsIHdoaWNoIGlzIG9mdGVuIHRvbyBvcHRpbWlzdGljLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFjcXVpc2l0aW9uIEZ1bmN0aW9ucyDigJQgRXhwbG9pdGF0aW9uIHZzIEV4cGxvcmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgYWNxdWlzaXRpb24gZnVuY3Rpb24gzrEoeCkgY29udmVydHMgdGhlIEdQIHBvc3RlcmlvciBpbnRvIGEgdXRpbGl0eSBzY29yZSBmb3IgZWFjaCBjYW5kaWRhdGUgcG9pbnQuIEl0IG11c3QgYmFsYW5jZSAqZXhwbG9pdGF0aW9uKiAocXVlcnlpbmcgbmVhciB0aGUgY3VycmVudCBiZXN0KSBhbmQgKmV4cGxvcmF0aW9uKiAocXVlcnlpbmcgaW4gdW5jZXJ0YWluIHJlZ2lvbnMpLiBUaGUgdGhyZWUgbW9zdCB3aWRlbHkgdXNlZCBhY3F1aXNpdGlvbiBmdW5jdGlvbnMgYXJlIFVwcGVyIENvbmZpZGVuY2UgQm91bmQgKFVDQiksIFByb2JhYmlsaXR5IG9mIEltcHJvdmVtZW50IChQSSksIGFuZCBFeHBlY3RlZCBJbXByb3ZlbWVudCAoRUkpLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVUNCOiDOsSh4KSA9IM68KHgpICsgzrLCt8+DKHgpIOKAlCBleHBsaWNpdCBleHBsb3JhdGlvbiBwYXJhbWV0ZXIgzrIiLCJQSTogzrEoeCkgPSBQKGYoeCkgXHUwMDNlIGYqICsgzr4pIOKAlCBwcm9iYWJpbGl0eSBvZiBiZWF0aW5nIGN1cnJlbnQgYmVzdCBieSBtYXJnaW4gzr4iLCJFSTogzrEoeCkgPSBFW21heCgwLCBmKHgpIOKIkiBmKildIOKAlCBleHBlY3RlZCBnYWluIG92ZXIgY3VycmVudCBiZXN0IGYqIiwiRUkgaXMgdGhlIGRlZmF1bHQgcmVjb21tZW5kYXRpb246IG5vIHR1bmluZyByZXF1aXJlZCwgbmF0dXJhbGx5IGJhbGFuY2VzIGJvdGggb2JqZWN0aXZlcyJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2RlIDEg4oCUIEJPIGZyb20gU2NyYXRjaCB3aXRoIEdQIFN1cnJvZ2F0ZSBhbmQgRUkifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5LnN0YXRzIGltcG9ydCBub3JtXG5mcm9tIHNjaXB5Lm9wdGltaXplIGltcG9ydCBtaW5pbWl6ZVxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuXG4jIOKUgOKUgCBUcnVlIG9iamVjdGl2ZSAoZXhwZW5zaXZlIGJsYWNrLWJveCwgMUQgZm9yIGlsbHVzdHJhdGlvbikg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAXG5kZWYgb2JqZWN0aXZlKHgpOlxuICAgIHJldHVybiAtKG5wLnNpbigzICogeCkgKyB4ICogMC4xKSAgIyBtaW5pbWl6YXRpb24gdGFyZ2V0XG5cbiMg4pSA4pSAIEdQIGtlcm5lbDogUkJGIHdpdGggbGVuZ3RoLXNjYWxlIGwgYW5kIHNpZ25hbCB2YXJpYW5jZSDPg8KyIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgFxuZGVmIHJiZl9rZXJuZWwoWDEsIFgyLCBsPTEuMCwgc2lnbWFfZj0xLjApOlxuICAgIHNxZGlzdCA9IG5wLnN1bShYMSoqMiwgMSkucmVzaGFwZSgtMSwgMSkgKyBucC5zdW0oWDIqKjIsIDEpIC0gMiAqIFgxIEAgWDIuVFxuICAgIHJldHVybiBzaWdtYV9mKioyICogbnAuZXhwKC0wLjUgLyBsKioyICogc3FkaXN0KVxuXG4jIOKUgOKUgCBHUCBwb3N0ZXJpb3Ig4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAXG5kZWYgZ3BfcG9zdGVyaW9yKFhfdHJhaW4sIHlfdHJhaW4sIFhfdGVzdCwgbD0xLjAsIHNpZ21hX2Y9MS4wLCBzaWdtYV9uPTFlLTgpOlxuICAgIEsgPSByYmZfa2VybmVsKFhfdHJhaW4sIFhfdHJhaW4sIGwsIHNpZ21hX2YpICsgc2lnbWFfbioqMiAqIG5wLmV5ZShsZW4oWF90cmFpbikpXG4gICAgS19zID0gcmJmX2tlcm5lbChYX3RyYWluLCBYX3Rlc3QsIGwsIHNpZ21hX2YpXG4gICAgS19zcyA9IHJiZl9rZXJuZWwoWF90ZXN0LCBYX3Rlc3QsIGwsIHNpZ21hX2YpXG4gICAgS19pbnYgPSBucC5saW5hbGcuaW52KEspXG4gICAgbXUgPSBLX3MuVCBAIEtfaW52IEAgeV90cmFpblxuICAgIGNvdiA9IEtfc3MgLSBLX3MuVCBAIEtfaW52IEAgS19zXG4gICAgcmV0dXJuIG11LCBucC5zcXJ0KG5wLmRpYWcoY292KS5jbGlwKDApKVxuXG4jIOKUgOKUgCBFeHBlY3RlZCBJbXByb3ZlbWVudCDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIBcbmRlZiBleHBlY3RlZF9pbXByb3ZlbWVudChYX3Rlc3QsIFhfdHJhaW4sIHlfdHJhaW4sIHhpPTAuMDEpOlxuICAgIG11LCBzaWdtYSA9IGdwX3Bvc3RlcmlvcihYX3RyYWluLCB5X3RyYWluLCBYX3Rlc3QpXG4gICAgZl9iZXN0ID0gbnAubWluKHlfdHJhaW4pXG4gICAgWiA9IChmX2Jlc3QgLSBtdSAtIHhpKSAvIChzaWdtYSArIDFlLTkpXG4gICAgcmV0dXJuIChmX2Jlc3QgLSBtdSAtIHhpKSAqIG5vcm0uY2RmKFopICsgc2lnbWEgKiBub3JtLnBkZihaKVxuXG4jIOKUgOKUgCBCTyBsb29wIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgFxubnAucmFuZG9tLnNlZWQoNDIpXG5YX2luaXQgPSBucC5yYW5kb20udW5pZm9ybSgwLCA1LCBzaXplPSgzLCAxKSlcbnlfaW5pdCA9IG9iamVjdGl2ZShYX2luaXQpLnJhdmVsKClcblxuWF9vYnMsIHlfb2JzID0gWF9pbml0LmNvcHkoKSwgeV9pbml0LmNvcHkoKVxuZm9yIGl0ZXJhdGlvbiBpbiByYW5nZSgxMCk6XG4gICAgIyBNYXhpbWl6ZSBFSSB2aWEgbXVsdGktc3RhcnQgTC1CRkdTLUJcbiAgICBiZXN0X3gsIGJlc3RfZWkgPSBOb25lLCAtbnAuaW5mXG4gICAgZm9yIHgwIGluIG5wLnJhbmRvbS51bmlmb3JtKDAsIDUsICgyMCwgMSkpOlxuICAgICAgICByZXMgPSBtaW5pbWl6ZShsYW1iZGEgeDogLWV4cGVjdGVkX2ltcHJvdmVtZW50KHgucmVzaGFwZSgxLC0xKSwgWF9vYnMsIHlfb2JzKSxcbiAgICAgICAgICAgICAgICAgICAgICAgeDAsIGJvdW5kcz1bKDAsIDUpXSwgbWV0aG9kPVx1MDAyN0wtQkZHUy1CXHUwMDI3KVxuICAgICAgICBpZiAtcmVzLmZ1biBcdTAwM2UgYmVzdF9laTpcbiAgICAgICAgICAgIGJlc3RfZWksIGJlc3RfeCA9IC1yZXMuZnVuLCByZXMueFxuICAgIFhfb2JzID0gbnAudnN0YWNrKFtYX29icywgYmVzdF94LnJlc2hhcGUoMSwgLTEpXSlcbiAgICB5X29icyA9IG5wLmFwcGVuZCh5X29icywgb2JqZWN0aXZlKGJlc3RfeCkpXG4gICAgcHJpbnQoZlwiSXRlciB7aXRlcmF0aW9uKzE6MmR9IHwgbmV4dF94PXtiZXN0X3hbMF06LjNmfSB8IGJlc3RfZj17eV9vYnMubWluKCk6LjRmfVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMiDigJQgQm9Ub3JjaCBvbiB0aGUgMkQgQnJhbmluIEZ1bmN0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuZnJvbSBib3RvcmNoLm1vZGVscyBpbXBvcnQgU2luZ2xlVGFza0dQXG5mcm9tIGJvdG9yY2guZml0IGltcG9ydCBmaXRfZ3B5dG9yY2hfbWxsXG5mcm9tIGJvdG9yY2guYWNxdWlzaXRpb24gaW1wb3J0IEV4cGVjdGVkSW1wcm92ZW1lbnRcbmZyb20gYm90b3JjaC5vcHRpbSBpbXBvcnQgb3B0aW1pemVfYWNxZlxuZnJvbSBncHl0b3JjaC5tbGxzIGltcG9ydCBFeGFjdE1hcmdpbmFsTG9nTGlrZWxpaG9vZFxuZnJvbSBib3RvcmNoLnRlc3RfZnVuY3Rpb25zIGltcG9ydCBCcmFuaW5cblxuIyDilIDilIAgU2V0dXAg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuYnJhbmluID0gQnJhbmluKG5lZ2F0ZT1UcnVlKSAgICMgbmVnYXRlIOKGkiBtYXhpbWl6YXRpb24gcHJvYmxlbVxuYm91bmRzID0gdG9yY2gudGVuc29yKFtbMC4wLCAwLjBdLCBbMS4wLCAxLjBdXSkgICMgbm9ybWFsaXplZCB1bml0IHNxdWFyZVxuXG5kZWYgZXZhbHVhdGUoWCk6XG4gICAgXCJcIlwiRXZhbHVhdGUgQnJhbmluIG9uIGEgYmF0Y2ggb2YgcG9pbnRzLCByZXR1cm5zIChOLDEpIHRlbnNvci5cIlwiXCJcbiAgICByZXR1cm4gYnJhbmluKFgpLnVuc3F1ZWV6ZSgtMSlcblxuIyDilIDilIAgSW5pdGlhbCBkZXNpZ24g4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAXG50cmFpbl9YID0gdG9yY2gucmFuZCg1LCAyKVxudHJhaW5fWSA9IGV2YWx1YXRlKHRyYWluX1gpXG5cbiMg4pSA4pSAIEJPIGxvb3Ag4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAXG5mb3IgaSBpbiByYW5nZSgxNSk6XG4gICAgIyBGaXQgR1BcbiAgICBtb2RlbCA9IFNpbmdsZVRhc2tHUCh0cmFpbl9YLCB0cmFpbl9ZKVxuICAgIG1sbCA9IEV4YWN0TWFyZ2luYWxMb2dMaWtlbGlob29kKG1vZGVsLmxpa2VsaWhvb2QsIG1vZGVsKVxuICAgIGZpdF9ncHl0b3JjaF9tbGwobWxsKVxuXG4gICAgIyBPcHRpbWl6ZSBFSVxuICAgIGJlc3RfZiA9IHRyYWluX1kubWF4KClcbiAgICBFSSA9IEV4cGVjdGVkSW1wcm92ZW1lbnQobW9kZWw9bW9kZWwsIGJlc3RfZj1iZXN0X2YpXG4gICAgY2FuZGlkYXRlLCBhY3FfdmFsdWUgPSBvcHRpbWl6ZV9hY3FmKFxuICAgICAgICBFSSwgYm91bmRzPWJvdW5kcywgcT0xLCBudW1fcmVzdGFydHM9MTAsIHJhd19zYW1wbGVzPTEyOFxuICAgIClcblxuICAgICMgRXZhbHVhdGUgYW5kIGFwcGVuZFxuICAgIG5ld195ID0gZXZhbHVhdGUoY2FuZGlkYXRlKVxuICAgIHRyYWluX1ggPSB0b3JjaC5jYXQoW3RyYWluX1gsIGNhbmRpZGF0ZV0pXG4gICAgdHJhaW5fWSA9IHRvcmNoLmNhdChbdHJhaW5fWSwgbmV3X3ldKVxuICAgIHByaW50KGZcIkl0ZXIge2krMToyZH0gfCBjYW5kaWRhdGU9e2NhbmRpZGF0ZS5zcXVlZXplKCkudG9saXN0KCl9IFwiXG4gICAgICAgICAgZlwifCBiZXN0PXt0cmFpbl9ZLm1heCgpLml0ZW0oKTouNGZ9XCIpXG5cbnByaW50KGZcIlxcbkZpbmFsIGJlc3QgdmFsdWU6IHt0cmFpbl9ZLm1heCgpLml0ZW0oKTouNGZ9IChCcmFuaW4gb3B0aW11bSDiiYggLTAuMzk3KVwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgMyDigJQgVmlzdWFsaXppbmcgdGhlIEJPIExvb3AgSXRlcmF0aW9uIGJ5IEl0ZXJhdGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IG5vcm1cbmZyb20gc2NpcHkub3B0aW1pemUgaW1wb3J0IG1pbmltaXplXG5cbmRlZiByYmZfa2VybmVsKFgxLCBYMiwgbD0xLjAsIHNmPTEuMCk6XG4gICAgZCA9IG5wLnN1bSgoWDFbOiwgTm9uZV0gLSBYMltOb25lLCA6XSkqKjIsIGF4aXM9LTEpXG4gICAgcmV0dXJuIHNmKioyICogbnAuZXhwKC0wLjUgKiBkIC8gbCoqMilcblxuZGVmIGdwX3ByZWRpY3QoWHRyLCB5dHIsIFh0ZSwgbm9pc2U9MWUtNik6XG4gICAgSyA9IHJiZl9rZXJuZWwoWHRyLCBYdHIpICsgbm9pc2UgKiBucC5leWUobGVuKFh0cikpXG4gICAgS3MgPSByYmZfa2VybmVsKFh0ciwgWHRlKVxuICAgIEtzc19kaWFnID0gbnAub25lcyhsZW4oWHRlKSlcbiAgICBhbHBoYSA9IG5wLmxpbmFsZy5zb2x2ZShLLCB5dHIpXG4gICAgbXUgPSBLcy5UIEAgYWxwaGFcbiAgICB2ID0gbnAubGluYWxnLnNvbHZlKEssIEtzKVxuICAgIHNpZ21hID0gbnAuc3FydCgoS3NzX2RpYWcgLSAoS3MgKiB2KS5zdW0oMCkpLmNsaXAoMCkpXG4gICAgcmV0dXJuIG11LCBzaWdtYVxuXG5kZWYgZWkoWHRlLCBYdHIsIHl0ciwgeGk9MC4wKTpcbiAgICBtdSwgc2lnbWEgPSBncF9wcmVkaWN0KFh0ciwgeXRyLCBYdGUpXG4gICAgaW1wID0geXRyLm1pbigpIC0gbXUgLSB4aVxuICAgIFogPSBpbXAgLyAoc2lnbWEgKyAxZS05KVxuICAgIHJldHVybiBpbXAgKiBub3JtLmNkZihaKSArIHNpZ21hICogbm9ybS5wZGYoWilcblxuZiA9IGxhbWJkYSB4OiBucC5zaW4oNSp4KSAqICgxIC0gbnAudGFuaCh4KioyKSkgICMgMS1EIHRveSBvYmplY3RpdmVcbnhfZ3JpZCA9IG5wLmxpbnNwYWNlKC0yLCAyLCAzMDApXG5ucC5yYW5kb20uc2VlZCg3KVxuWG9icyA9IG5wLmFycmF5KFstMS41LCAwLjAsIDEuNV0pXG55b2JzID0gZihYb2JzKVxuXG5maWcsIGF4ZXMgPSBwbHQuc3VicGxvdHMoMiwgMywgZmlnc2l6ZT0oMTQsIDcpKVxuZm9yIGF4X3JvdywgYXggaW4gemlwKGF4ZXMuVCwgYXhlcy5UKTpcbiAgICBwYXNzICAjIGxheW91dCBwbGFjZWhvbGRlclxuXG5mb3IgaXQgaW4gcmFuZ2UoNik6XG4gICAgYXggPSBheGVzLmZsYXRbaXRdXG4gICAgbXUsIHNpZ21hID0gZ3BfcHJlZGljdChYb2JzLCB5b2JzLCB4X2dyaWQpXG4gICAgYWNxID0gZWkoeF9ncmlkLCBYb2JzLCB5b2JzKVxuICAgIGF4LmZpbGxfYmV0d2Vlbih4X2dyaWQsIG11LTIqc2lnbWEsIG11KzIqc2lnbWEsIGFscGhhPTAuMiwgbGFiZWw9XHUwMDI3wrEyz4NcdTAwMjcpXG4gICAgYXgucGxvdCh4X2dyaWQsIG11LCBsYWJlbD1cdTAwMjdHUCBtZWFuXHUwMDI3KVxuICAgIGF4LnBsb3QoeF9ncmlkLCBmKHhfZ3JpZCksIFx1MDAyN2stLVx1MDAyNywgYWxwaGE9MC40LCBsYWJlbD1cdTAwMjd0cnVlIGZcdTAwMjcpXG4gICAgYXguc2NhdHRlcihYb2JzLCB5b2JzLCB6b3JkZXI9NSwgY29sb3I9XHUwMDI3cmVkXHUwMDI3LCBsYWJlbD1cdTAwMjdvYnNcdTAwMjcpXG4gICAgYXgyID0gYXgudHdpbngoKVxuICAgIGF4Mi5wbG90KHhfZ3JpZCwgYWNxLCBjb2xvcj1cdTAwMjdncmVlblx1MDAyNywgYWxwaGE9MC42LCBsdz0xKVxuICAgIGF4Mi5zZXRfeWxhYmVsKFx1MDAyN0VJXHUwMDI3LCBjb2xvcj1cdTAwMjdncmVlblx1MDAyNywgZm9udHNpemU9OClcbiAgICBheC5zZXRfdGl0bGUoZlx1MDAyN0l0ZXJhdGlvbiB7aXQrMX1cdTAwMjcpXG4gICAgIyBTZWxlY3QgbmV4dCBwb2ludFxuICAgIG5leHRfeCA9IHhfZ3JpZFtucC5hcmdtYXgoYWNxKV1cbiAgICBYb2JzID0gbnAuYXBwZW5kKFhvYnMsIG5leHRfeClcbiAgICB5b2JzID0gbnAuYXBwZW5kKHlvYnMsIGYobmV4dF94KSlcblxucGx0LnRpZ2h0X2xheW91dCgpXG5wbHQuc2F2ZWZpZyhcdTAwMjdib19sb29wX3Zpc3VhbGl6YXRpb24ucG5nXHUwMDI3LCBkcGk9MTIwKVxucGx0LnNob3coKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvZGUgNCDigJQgQmF0Y2ggQk8gd2l0aCBxLUVJIChNb250ZSBDYXJsbyBBcHByb3hpbWF0aW9uKSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gYm90b3JjaC5tb2RlbHMgaW1wb3J0IFNpbmdsZVRhc2tHUFxuZnJvbSBib3RvcmNoLmZpdCBpbXBvcnQgZml0X2dweXRvcmNoX21sbFxuZnJvbSBib3RvcmNoLmFjcXVpc2l0aW9uLm1vbnRlX2NhcmxvIGltcG9ydCBxRXhwZWN0ZWRJbXByb3ZlbWVudFxuZnJvbSBib3RvcmNoLnNhbXBsaW5nLm5vcm1hbCBpbXBvcnQgU29ib2xRTUNOb3JtYWxTYW1wbGVyXG5mcm9tIGJvdG9yY2gub3B0aW0gaW1wb3J0IG9wdGltaXplX2FjcWZcbmZyb20gZ3B5dG9yY2gubWxscyBpbXBvcnQgRXhhY3RNYXJnaW5hbExvZ0xpa2VsaWhvb2RcbmZyb20gYm90b3JjaC50ZXN0X2Z1bmN0aW9ucyBpbXBvcnQgQnJhbmluXG5cbiMg4pSA4pSAIENvbmZpZyDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIBcbkJBVENIX1NJWkUgPSA0ICAgICAgICAgICMgZXZhbHVhdGUgNCBwb2ludHMgaW4gcGFyYWxsZWwgZWFjaCByb3VuZFxuTl9JTklUID0gNlxuTl9ST1VORFMgPSA4XG5NQ19TQU1QTEVTID0gMjU2ICAgICAgICAjIE1vbnRlIENhcmxvIHNhbXBsZXMgZm9yIHEtRUkgYXBwcm94aW1hdGlvblxuYm91bmRzID0gdG9yY2gudGVuc29yKFtbMC4wLCAwLjBdLCBbMS4wLCAxLjBdXSlcbmYgPSBCcmFuaW4obmVnYXRlPVRydWUpXG5cbmRlZiBldmFsX2JhdGNoKFgpOlxuICAgIHJldHVybiBmKFgpLnVuc3F1ZWV6ZSgtMSlcblxudG9yY2gubWFudWFsX3NlZWQoMSlcbnRyYWluX1ggPSB0b3JjaC5yYW5kKE5fSU5JVCwgMilcbnRyYWluX1kgPSBldmFsX2JhdGNoKHRyYWluX1gpXG5cbmZvciBybmQgaW4gcmFuZ2UoTl9ST1VORFMpOlxuICAgIG1vZGVsID0gU2luZ2xlVGFza0dQKHRyYWluX1gsIHRyYWluX1kpXG4gICAgbWxsID0gRXhhY3RNYXJnaW5hbExvZ0xpa2VsaWhvb2QobW9kZWwubGlrZWxpaG9vZCwgbW9kZWwpXG4gICAgZml0X2dweXRvcmNoX21sbChtbGwpXG5cbiAgICBzYW1wbGVyID0gU29ib2xRTUNOb3JtYWxTYW1wbGVyKHNhbXBsZV9zaGFwZT10b3JjaC5TaXplKFtNQ19TQU1QTEVTXSkpXG4gICAgcUVJID0gcUV4cGVjdGVkSW1wcm92ZW1lbnQoXG4gICAgICAgIG1vZGVsPW1vZGVsLCBiZXN0X2Y9dHJhaW5fWS5tYXgoKSwgc2FtcGxlcj1zYW1wbGVyXG4gICAgKVxuXG4gICAgIyBKb2ludCBvcHRpbWl6YXRpb24gb2YgcSBjYW5kaWRhdGVzIHNpbXVsdGFuZW91c2x5XG4gICAgY2FuZGlkYXRlcywgYWNxX3ZhbCA9IG9wdGltaXplX2FjcWYoXG4gICAgICAgIHFFSSwgYm91bmRzPWJvdW5kcywgcT1CQVRDSF9TSVpFLFxuICAgICAgICBudW1fcmVzdGFydHM9OCwgcmF3X3NhbXBsZXM9MjU2XG4gICAgKVxuXG4gICAgbmV3X1kgPSBldmFsX2JhdGNoKGNhbmRpZGF0ZXMpXG4gICAgdHJhaW5fWCA9IHRvcmNoLmNhdChbdHJhaW5fWCwgY2FuZGlkYXRlc10pXG4gICAgdHJhaW5fWSA9IHRvcmNoLmNhdChbdHJhaW5fWSwgbmV3X1ldKVxuICAgIHByaW50KGZcIlJvdW5kIHtybmQrMToyZH0gfCBiYXRjaF9zaXplPXtCQVRDSF9TSVpFfSB8IFwiXG4gICAgICAgICAgZlwiYmVzdD17dHJhaW5fWS5tYXgoKS5pdGVtKCk6LjRmfSB8IFwiXG4gICAgICAgICAgZlwidG90YWxfZXZhbHM9e2xlbih0cmFpbl9YKX1cIilcblxucHJpbnQoZlwiXFxuT3B0aW1hbCBmb3VuZDoge3RyYWluX1kubWF4KCkuaXRlbSgpOi40Zn1cIikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb252ZXJnZW5jZSBhbmQgTm8tUmVncmV0IEd1YXJhbnRlZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJPIHdpdGggR1AtVUNCIHNhdGlzZmllcyBhIG5vLXJlZ3JldCBndWFyYW50ZWU6IHRoZSBjdW11bGF0aXZlIHJlZ3JldCBS4oKZID0gzqPhtaIoZiog4oiSIGYoeOG1oikpIGdyb3dzIHN1YmxpbmVhcmx5LCBtZWFuaW5nIHRoZSBhdmVyYWdlIHJlZ3JldCBS4oKZL24g4oaSIDAgYXMgbiDihpIg4oieLiBUaGlzIGhvbGRzIHVuZGVyIG1pbGQgYXNzdW1wdGlvbnMgb24gdGhlIGtlcm5lbCAoYm91bmRlZCBSS0hTIG5vcm0pLiBJbiBwcmFjdGljZSB0aGlzIG1lYW5zIEJPIHdpbGwgZXZlbnR1YWxseSBmaW5kIGEgbmVhci1vcHRpbWFsIHBvaW50IGdpdmVuIGVub3VnaCBldmFsdWF0aW9ucywgZXZlbiB0aG91Z2ggdGhlIGJsYWNrLWJveCBpcyBuZXZlciBkaWZmZXJlbnRpYXRlZC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBrZXkgcXVhbnRpdHkgY29udHJvbGxpbmcgY29udmVyZ2VuY2UgcmF0ZSBpcyB0aGUgKm1heGltdW0gaW5mb3JtYXRpb24gZ2FpbiogzrPigpkg4oCUIGhvdyBtdWNoIGluZm9ybWF0aW9uIG4gcXVlcmllcyBjYW4gcHJvdmlkZSBhYm91dCB0aGUgR1AgZnVuY3Rpb24uIEZvciBjb21tb24ga2VybmVsczogzrPigpkgPSBPKGxvZ8KybikgZm9yIFJCRiwgTyhuXihkLygyzr0rZCkpKSBmb3IgTWF0w6lybi3OvS4gU21vb3RoZXIgZnVuY3Rpb25zIChsYXJnZSDOvSkgaGF2ZSBzbWFsbGVyIM6z4oKZIGFuZCB0aGVyZWZvcmUgZmFzdGVyIGNvbnZlcmdlbmNlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBhcmlzb24gb2YgQmxhY2stQm94IE9wdGltaXphdGlvbiBNZXRob2RzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIkV2YWx1YXRpb25zIHRvIE9wdGltdW0iLCJQYXJhbGxlbGl6YWJsZSIsIkhhbmRsZXMgTm9pc2UiLCJEaW0gTGltaXQiXSwicm93cyI6W1siQmF5ZXNpYW4gT3B0aW1pemF0aW9uIiwiTG93ICgxMOKAkzIwMCkiLCJZZXMgKGJhdGNoIEJPIC8gcS1FSSkiLCJZZXMgKEdQIG5vaXNlIG1vZGVsKSIsImQg4omkIDIwIHByYWN0aWNhbCJdLFsiUmFuZG9tIFNlYXJjaCIsIkhpZ2ggKGh1bmRyZWRz4oCTdGhvdXNhbmRzKSIsIlllcyAoZW1iYXJyYXNzaW5nbHkpIiwiWWVzIChpbXBsaWNpdCBhdmVyYWdlKSIsIk5vIGhhcmQgbGltaXQiXSxbIkdyaWQgU2VhcmNoIiwiVmVyeSBIaWdoIChleHBvbmVudGlhbCBpbiBkKSIsIlllcyAoZW1iYXJyYXNzaW5nbHkpIiwiUGFydGlhbCAocmVwZWF0IGV2YWxzKSIsImQg4omkIDQgcHJhY3RpY2FsIl0sWyJUUEUgKE9wdHVuYSkiLCJNb2RlcmF0ZSAoNTDigJM1MDApIiwiWWVzIChhc3luYyB3b3JrZXJzKSIsIlllcyAoS0RFIG9uIGdvb2QvYmFkKSIsImQg4omkIDEwMCsiXSxbIkh5cGVyYmFuZCIsIk1vZGVyYXRlIChyZXNvdXJjZS1hd2FyZSkiLCJZZXMgKG11bHRpLWZpZGVsaXR5KSIsIlBhcnRpYWwgKGVhcmx5IHN0b3BzKSIsIk5vIGhhcmQgbGltaXQiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNjYWxhYmlsaXR5IGFuZCBMaW1pdGF0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgR1AtYmFzZWQgQk8gaGFzIHR3byBmdW5kYW1lbnRhbCBzY2FsYWJpbGl0eSBib3R0bGVuZWNrcy4gRmlyc3QsIEdQIGluZmVyZW5jZSBpcyBPKG7CsykgaW4gdGhlIG51bWJlciBvZiBvYnNlcnZhdGlvbnMgZHVlIHRvIHRoZSBtYXRyaXggaW52ZXJzaW9uIOKAlCBtYW5hZ2VhYmxlIGZvciBuIFx1MDAzYyAyMDAwIGJ1dCBzbG93IGJleW9uZCB0aGF0LiBTcGFyc2UgR1AgYXBwcm94aW1hdGlvbnMgKGluZHVjaW5nIHBvaW50cywgU1ZHUCkgZXh0ZW5kIEJPIHRvIGxhcmdlciBidWRnZXRzLiBTZWNvbmQsIHRoZSBjdXJzZSBvZiBkaW1lbnNpb25hbGl0eTogdGhlIHN1cnJvZ2F0ZSBiZWNvbWVzIGluY3JlYXNpbmdseSBkaWZmaWN1bHQgdG8gZml0IGFuZCB0aGUgYWNxdWlzaXRpb24gc3VyZmFjZSBpbmNyZWFzaW5nbHkgbXVsdGltb2RhbCBhcyBkIGdyb3dzLiBFbXBpcmljYWxseSBCTyBkZWdyYWRlcyBub3RpY2VhYmx5IGJleW9uZCBkIOKJiCAyMC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkhpZ2gtZGltZW5zaW9uYWwgQk8gYWx0ZXJuYXRpdmVzOiBSRU1CTyAocmFuZG9tIGVtYmVkZGluZyksIEFMRUJPLCBUdVJCTyAodHJ1c3QgcmVnaW9ucyksIE1BQ0UiLCJMYXJnZSBuOiBzcGFyc2UgR1AgKFNWR1ApLCByYW5kb20gZm9yZXN0cyBhcyBzdXJyb2dhdGUgKFNNQUMpLCBuZXVyYWwgbmV0d29yayBzdXJyb2dhdGVzIChETkdPLCBCT0hBTUlBTk4pIiwiTXVsdGktZmlkZWxpdHkgQk86IGNvbWJpbmUgY2hlYXAgYXBwcm94aW1hdGlvbnMgKGUuZy4sIGZld2VyIHRyYWluaW5nIGVwb2Nocykgd2l0aCBmdWxsIGV2YWx1YXRpb25zIiwiTXVsdGktb2JqZWN0aXZlIEJPOiBQYXJldG8gZnJvbnRpZXIgb3B0aW1pemF0aW9uIHdpdGggRUhWSSAoRXhwZWN0ZWQgSHlwZXJ2b2x1bWUgSW1wcm92ZW1lbnQpIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiR1AgQXNzdW1wdGlvbiBNaXNtYXRjaCIsImNvbnRlbnQiOiJCTyB3aXRoIGEgR1Agc3Vycm9nYXRlIGFzc3VtZXMgdGhlIG9iamVjdGl2ZSBpcyBhIHNtb290aCwgc3RhdGlvbmFyeSBmdW5jdGlvbi4gSGlnaGx5IGRpc2NvbnRpbnVvdXMgbGFuZHNjYXBlcywgZnVuY3Rpb25zIHdpdGggZGlzY3JldGUgdmFyaWFibGVzLCBvciBub24tc3RhdGlvbmFyeSByZXNwb25zZXMgdmlvbGF0ZSB0aGVzZSBhc3N1bXB0aW9ucy4gSW4gc3VjaCBjYXNlcyBUUEUsIFNNQUMgKHJhbmRvbS1mb3Jlc3Qgc3Vycm9nYXRlKSwgb3IgQ01BLUVTIG1heSBvdXRwZXJmb3JtIEdQLUJPLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFwcGxpY2F0aW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmF5ZXNpYW4gT3B0aW1pemF0aW9uIGhhcyBiZWNvbWUgdGhlIHN0YW5kYXJkIG1ldGhvZCB3aGVuZXZlciBlYWNoIGZ1bmN0aW9uIGV2YWx1YXRpb24gaXMgZXhwZW5zaXZlIGFuZCB0aGUgYnVkZ2V0IGlzIHNtYWxsIChcdTAwM2MgYSBmZXcgaHVuZHJlZCBldmFsdWF0aW9ucykuIEl0cyBtb3N0IHByb21pbmVudCBhcHBsaWNhdGlvbiBpcyBoeXBlcnBhcmFtZXRlciBvcHRpbWl6YXRpb24gKEhQTykgZm9yIG1hY2hpbmUgbGVhcm5pbmcgbW9kZWxzIOKAlCBsaWJyYXJpZXMgbGlrZSBBeCwgT3B0dW5hICh3aXRoIEdQIHNhbXBsZXIpLCBhbmQgU01BQzMgYWxsIGltcGxlbWVudCBCTy4gQmV5b25kIE1MLCBCTyBpcyB1c2VkIGluIGRydWcgZGlzY292ZXJ5IHRvIHByb3Bvc2UgbmV3IG1vbGVjdWxhciBjYW5kaWRhdGVzLCBpbiBtYXRlcmlhbHMgc2NpZW5jZSB0byBvcHRpbWl6ZSBhbGxveSBvciBjYXRhbHlzdCBwcm9wZXJ0aWVzLCBpbiByb2JvdGljcyBmb3IgcG9saWN5IHNlYXJjaCwgYW5kIGluIGVuZ2luZWVyaW5nIGRlc2lnbiBmb3IgYWVyb2R5bmFtaWMgc2hhcGUgb3B0aW1pemF0aW9uLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiSHlwZXJwYXJhbWV0ZXIgb3B0aW1pemF0aW9uIChIUE8pOiBsZWFybmluZyByYXRlLCBhcmNoaXRlY3R1cmUgc2VhcmNoLCByZWd1bGFyaXphdGlvbiIsIkRydWcgZGlzY292ZXJ5OiBtb2xlY3VsYXIgcHJvcGVydHkgb3B0aW1pemF0aW9uIG92ZXIgY2hlbWljYWwgc3BhY2UiLCJNYXRlcmlhbHMgZGVzaWduOiBhbGxveSBjb21wb3NpdGlvbiwgY2F0YWx5c3Qgc3VyZmFjZSBhcmVhLCBiYXR0ZXJ5IGVsZWN0cm9kZSBnZW9tZXRyeSIsIkEvQiB0ZXN0aW5nOiBtdWx0aS1hcm1lZCBiYW5kaXQgdmFyaWFudHMgb2YgQk8gZm9yIGNvbnZlcnNpb24gb3B0aW1pemF0aW9uIiwiUm9ib3RpY3M6IHNpbS10by1yZWFsIHRyYW5zZmVyLCBjb250cm9sbGVyIGdhaW4gdHVuaW5nIl19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJQcmFjdGljYWwgU3RhcnRpbmcgUG9pbnQiLCJjb250ZW50IjoiRm9yIEhQTyBpbiBQeXRob24sIHN0YXJ0IHdpdGggQXggKE1ldGEsIHdyYXBzIEJvVG9yY2gpIG9yIE9wdHVuYSB3aXRoIHRoZSBHUFNhbXBsZXIuIEJvdGggaGFuZGxlIGludGVnZXIvY2F0ZWdvcmljYWwgdmFyaWFibGVzLCBjb25zdHJhaW50cywgYW5kIHBhcmFsbGVsaXNtIG91dCBvZiB0aGUgYm94LiBVc2UgQm9Ub3JjaCBkaXJlY3RseSBvbmx5IHdoZW4geW91IG5lZWQgY3VzdG9tIGFjcXVpc2l0aW9uIGZ1bmN0aW9ucyBvciBtdWx0aS1vYmplY3RpdmUgQk8uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCYXllc2lhbiBPcHRpbWl6YXRpb24gc2l0cyBhdCB0aGUgaW50ZXJzZWN0aW9uIG9mIHByb2JhYmlsaXN0aWMgbW9kZWxpbmcsIGRlY2lzaW9uIHRoZW9yeSwgYW5kIG51bWVyaWNhbCBvcHRpbWl6YXRpb24uIEl0cyBwb3dlciBjb21lcyBmcm9tIHRyZWF0aW5nIG9wdGltaXphdGlvbiBhcyBhIHN0YXRpc3RpY2FsIGluZmVyZW5jZSBwcm9ibGVtOiBtYWludGFpbiB1bmNlcnRhaW50eSBhYm91dCB0aGUgb2JqZWN0aXZlLCBhY3QgdG8gcmVkdWNlIGl0IHN0cmF0ZWdpY2FsbHksIGFuZCBleHBsb2l0IHN0cnVjdHVyZSBhcyBpdCBiZWNvbWVzIGFwcGFyZW50LiBGb3IgYW55IHByb2JsZW0gd2hlcmUgZWFjaCBldmFsdWF0aW9uIGNvc3RzIHJlYWwgcmVzb3VyY2VzLCBCTyBzaG91bGQgYmUgdGhlIGZpcnN0IGFsZ29yaXRobSB5b3UgcmVhY2ggZm9yLiJ9XQ=="
---
# Bayesian Optimization — Surrogate Models and the BO Loop

Many real-world optimization problems — tuning neural-network hyperparameters, designing new drug molecules, finding optimal alloy compositions — share one brutal constraint: every function evaluation is expensive. A single training run can take hours; a lab synthesis can cost thousands of dollars. Grid search and random search waste those evaluations by ignoring everything learned so far. Bayesian Optimization (BO) is a principled, sample-efficient alternative that builds a probabilistic model of the objective and uses it to decide *where to look next*.

## The Bayesian Optimization Loop

BO is a sequential decision-making algorithm. At each iteration it performs four steps: (1) fit a surrogate model to all observations collected so far, (2) maximize an acquisition function over the surrogate to choose the next candidate point, (3) evaluate the expensive objective at that point, and (4) add the new observation to the dataset and repeat. After a budget of evaluations is exhausted, the best observed point is returned.

1. Fit surrogate p(f | D) to current observations D = {(xᵢ, yᵢ)}
2. Maximize acquisition α(x; D) to select next query xₙₑₓₜ
3. Evaluate the true objective: yₙₑₓₜ = f(xₙₑₓₜ) + ε
4. Update dataset D ← D ∪ {(xₙₑₓₜ, yₙₑₓₜ)} and go to step 1

> **Why Not Just Optimize the Surrogate Directly?**: The surrogate is cheap to evaluate, so we can optimize it with any gradient-based or evolutionary method. The acquisition function is also cheap and encodes where to query next given uncertainty — the true objective f is only called once per BO iteration.

## Gaussian Processes as the Ideal Surrogate

A Gaussian Process (GP) is a distribution over functions. Given training data, the GP posterior provides a mean prediction μ(x) and a calibrated uncertainty estimate σ(x) at every input. This is exactly what a good surrogate needs: not just a prediction, but an honest assessment of how confident it is. The GP is non-parametric — its effective complexity grows with data — and its predictions are analytically tractable under Gaussian noise.

The GP is fully specified by a mean function m(x) (often set to zero) and a covariance kernel k(x, x′). The Matérn-5/2 kernel is the default choice in most BO libraries because it produces functions that are twice differentiable — smoother than a rough process but rougher than infinitely differentiable RBF, which is often too optimistic.

## Acquisition Functions — Exploitation vs Exploration

The acquisition function α(x) converts the GP posterior into a utility score for each candidate point. It must balance *exploitation* (querying near the current best) and *exploration* (querying in uncertain regions). The three most widely used acquisition functions are Upper Confidence Bound (UCB), Probability of Improvement (PI), and Expected Improvement (EI).

- UCB: α(x) = μ(x) + β·σ(x) — explicit exploration parameter β
- PI: α(x) = P(f(x) > f* + ξ) — probability of beating current best by margin ξ
- EI: α(x) = E[max(0, f(x) − f*)] — expected gain over current best f*
- EI is the default recommendation: no tuning required, naturally balances both objectives

## Code 1 — BO from Scratch with GP Surrogate and EI

```python
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# ── True objective (expensive black-box, 1D for illustration) ──────────────
def objective(x):
    return -(np.sin(3 * x) + x * 0.1)  # minimization target

# ── GP kernel: RBF with length-scale l and signal variance σ² ─────────────
def rbf_kernel(X1, X2, l=1.0, sigma_f=1.0):
    sqdist = np.sum(X1**2, 1).reshape(-1, 1) + np.sum(X2**2, 1) - 2 * X1 @ X2.T
    return sigma_f**2 * np.exp(-0.5 / l**2 * sqdist)

# ── GP posterior ──────────────────────────────────────────────────────────
def gp_posterior(X_train, y_train, X_test, l=1.0, sigma_f=1.0, sigma_n=1e-8):
    K = rbf_kernel(X_train, X_train, l, sigma_f) + sigma_n**2 * np.eye(len(X_train))
    K_s = rbf_kernel(X_train, X_test, l, sigma_f)
    K_ss = rbf_kernel(X_test, X_test, l, sigma_f)
    K_inv = np.linalg.inv(K)
    mu = K_s.T @ K_inv @ y_train
    cov = K_ss - K_s.T @ K_inv @ K_s
    return mu, np.sqrt(np.diag(cov).clip(0))

# ── Expected Improvement ──────────────────────────────────────────────────
def expected_improvement(X_test, X_train, y_train, xi=0.01):
    mu, sigma = gp_posterior(X_train, y_train, X_test)
    f_best = np.min(y_train)
    Z = (f_best - mu - xi) / (sigma + 1e-9)
    return (f_best - mu - xi) * norm.cdf(Z) + sigma * norm.pdf(Z)

# ── BO loop ───────────────────────────────────────────────────────────────
np.random.seed(42)
X_init = np.random.uniform(0, 5, size=(3, 1))
y_init = objective(X_init).ravel()

X_obs, y_obs = X_init.copy(), y_init.copy()
for iteration in range(10):
    # Maximize EI via multi-start L-BFGS-B
    best_x, best_ei = None, -np.inf
    for x0 in np.random.uniform(0, 5, (20, 1)):
        res = minimize(lambda x: -expected_improvement(x.reshape(1,-1), X_obs, y_obs),
                       x0, bounds=[(0, 5)], method='L-BFGS-B')
        if -res.fun > best_ei:
            best_ei, best_x = -res.fun, res.x
    X_obs = np.vstack([X_obs, best_x.reshape(1, -1)])
    y_obs = np.append(y_obs, objective(best_x))
    print(f"Iter {iteration+1:2d} | next_x={best_x[0]:.3f} | best_f={y_obs.min():.4f}")
```

## Code 2 — BoTorch on the 2D Branin Function

```python
import torch
from botorch.models import SingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.acquisition import ExpectedImprovement
from botorch.optim import optimize_acqf
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.test_functions import Branin

# ── Setup ─────────────────────────────────────────────────────────────────
torch.manual_seed(0)
branin = Branin(negate=True)   # negate → maximization problem
bounds = torch.tensor([[0.0, 0.0], [1.0, 1.0]])  # normalized unit square

def evaluate(X):
    """Evaluate Branin on a batch of points, returns (N,1) tensor."""
    return branin(X).unsqueeze(-1)

# ── Initial design ────────────────────────────────────────────────────────
train_X = torch.rand(5, 2)
train_Y = evaluate(train_X)

# ── BO loop ───────────────────────────────────────────────────────────────
for i in range(15):
    # Fit GP
    model = SingleTaskGP(train_X, train_Y)
    mll = ExactMarginalLogLikelihood(model.likelihood, model)
    fit_gpytorch_mll(mll)

    # Optimize EI
    best_f = train_Y.max()
    EI = ExpectedImprovement(model=model, best_f=best_f)
    candidate, acq_value = optimize_acqf(
        EI, bounds=bounds, q=1, num_restarts=10, raw_samples=128
    )

    # Evaluate and append
    new_y = evaluate(candidate)
    train_X = torch.cat([train_X, candidate])
    train_Y = torch.cat([train_Y, new_y])
    print(f"Iter {i+1:2d} | candidate={candidate.squeeze().tolist()} "
          f"| best={train_Y.max().item():.4f}")

print(f"\nFinal best value: {train_Y.max().item():.4f} (Branin optimum ≈ -0.397)")
```

## Code 3 — Visualizing the BO Loop Iteration by Iteration

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import minimize

def rbf_kernel(X1, X2, l=1.0, sf=1.0):
    d = np.sum((X1[:, None] - X2[None, :])**2, axis=-1)
    return sf**2 * np.exp(-0.5 * d / l**2)

def gp_predict(Xtr, ytr, Xte, noise=1e-6):
    K = rbf_kernel(Xtr, Xtr) + noise * np.eye(len(Xtr))
    Ks = rbf_kernel(Xtr, Xte)
    Kss_diag = np.ones(len(Xte))
    alpha = np.linalg.solve(K, ytr)
    mu = Ks.T @ alpha
    v = np.linalg.solve(K, Ks)
    sigma = np.sqrt((Kss_diag - (Ks * v).sum(0)).clip(0))
    return mu, sigma

def ei(Xte, Xtr, ytr, xi=0.0):
    mu, sigma = gp_predict(Xtr, ytr, Xte)
    imp = ytr.min() - mu - xi
    Z = imp / (sigma + 1e-9)
    return imp * norm.cdf(Z) + sigma * norm.pdf(Z)

f = lambda x: np.sin(5*x) * (1 - np.tanh(x**2))  # 1-D toy objective
x_grid = np.linspace(-2, 2, 300)
np.random.seed(7)
Xobs = np.array([-1.5, 0.0, 1.5])
yobs = f(Xobs)

fig, axes = plt.subplots(2, 3, figsize=(14, 7))
for ax_row, ax in zip(axes.T, axes.T):
    pass  # layout placeholder

for it in range(6):
    ax = axes.flat[it]
    mu, sigma = gp_predict(Xobs, yobs, x_grid)
    acq = ei(x_grid, Xobs, yobs)
    ax.fill_between(x_grid, mu-2*sigma, mu+2*sigma, alpha=0.2, label='±2σ')
    ax.plot(x_grid, mu, label='GP mean')
    ax.plot(x_grid, f(x_grid), 'k--', alpha=0.4, label='true f')
    ax.scatter(Xobs, yobs, zorder=5, color='red', label='obs')
    ax2 = ax.twinx()
    ax2.plot(x_grid, acq, color='green', alpha=0.6, lw=1)
    ax2.set_ylabel('EI', color='green', fontsize=8)
    ax.set_title(f'Iteration {it+1}')
    # Select next point
    next_x = x_grid[np.argmax(acq)]
    Xobs = np.append(Xobs, next_x)
    yobs = np.append(yobs, f(next_x))

plt.tight_layout()
plt.savefig('bo_loop_visualization.png', dpi=120)
plt.show()
```

## Code 4 — Batch BO with q-EI (Monte Carlo Approximation)

```python
import torch
from botorch.models import SingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.acquisition.monte_carlo import qExpectedImprovement
from botorch.sampling.normal import SobolQMCNormalSampler
from botorch.optim import optimize_acqf
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.test_functions import Branin

# ── Config ────────────────────────────────────────────────────────────────
BATCH_SIZE = 4          # evaluate 4 points in parallel each round
N_INIT = 6
N_ROUNDS = 8
MC_SAMPLES = 256        # Monte Carlo samples for q-EI approximation
bounds = torch.tensor([[0.0, 0.0], [1.0, 1.0]])
f = Branin(negate=True)

def eval_batch(X):
    return f(X).unsqueeze(-1)

torch.manual_seed(1)
train_X = torch.rand(N_INIT, 2)
train_Y = eval_batch(train_X)

for rnd in range(N_ROUNDS):
    model = SingleTaskGP(train_X, train_Y)
    mll = ExactMarginalLogLikelihood(model.likelihood, model)
    fit_gpytorch_mll(mll)

    sampler = SobolQMCNormalSampler(sample_shape=torch.Size([MC_SAMPLES]))
    qEI = qExpectedImprovement(
        model=model, best_f=train_Y.max(), sampler=sampler
    )

    # Joint optimization of q candidates simultaneously
    candidates, acq_val = optimize_acqf(
        qEI, bounds=bounds, q=BATCH_SIZE,
        num_restarts=8, raw_samples=256
    )

    new_Y = eval_batch(candidates)
    train_X = torch.cat([train_X, candidates])
    train_Y = torch.cat([train_Y, new_Y])
    print(f"Round {rnd+1:2d} | batch_size={BATCH_SIZE} | "
          f"best={train_Y.max().item():.4f} | "
          f"total_evals={len(train_X)}")

print(f"\nOptimal found: {train_Y.max().item():.4f}")
```

## Convergence and No-Regret Guarantees

BO with GP-UCB satisfies a no-regret guarantee: the cumulative regret Rₙ = Σᵢ(f* − f(xᵢ)) grows sublinearly, meaning the average regret Rₙ/n → 0 as n → ∞. This holds under mild assumptions on the kernel (bounded RKHS norm). In practice this means BO will eventually find a near-optimal point given enough evaluations, even though the black-box is never differentiated.

The key quantity controlling convergence rate is the *maximum information gain* γₙ — how much information n queries can provide about the GP function. For common kernels: γₙ = O(log²n) for RBF, O(n^(d/(2ν+d))) for Matérn-ν. Smoother functions (large ν) have smaller γₙ and therefore faster convergence.

## Comparison of Black-Box Optimization Methods

| Method | Evaluations to Optimum | Parallelizable | Handles Noise | Dim Limit |
| --- | --- | --- | --- | --- |
| Bayesian Optimization | Low (10–200) | Yes (batch BO / q-EI) | Yes (GP noise model) | d ≤ 20 practical |
| Random Search | High (hundreds–thousands) | Yes (embarrassingly) | Yes (implicit average) | No hard limit |
| Grid Search | Very High (exponential in d) | Yes (embarrassingly) | Partial (repeat evals) | d ≤ 4 practical |
| TPE (Optuna) | Moderate (50–500) | Yes (async workers) | Yes (KDE on good/bad) | d ≤ 100+ |
| Hyperband | Moderate (resource-aware) | Yes (multi-fidelity) | Partial (early stops) | No hard limit |

## Scalability and Limitations

Standard GP-based BO has two fundamental scalability bottlenecks. First, GP inference is O(n³) in the number of observations due to the matrix inversion — manageable for n < 2000 but slow beyond that. Sparse GP approximations (inducing points, SVGP) extend BO to larger budgets. Second, the curse of dimensionality: the surrogate becomes increasingly difficult to fit and the acquisition surface increasingly multimodal as d grows. Empirically BO degrades noticeably beyond d ≈ 20.

- High-dimensional BO alternatives: REMBO (random embedding), ALEBO, TuRBO (trust regions), MACE
- Large n: sparse GP (SVGP), random forests as surrogate (SMAC), neural network surrogates (DNGO, BOHAMIANN)
- Multi-fidelity BO: combine cheap approximations (e.g., fewer training epochs) with full evaluations
- Multi-objective BO: Pareto frontier optimization with EHVI (Expected Hypervolume Improvement)

> **GP Assumption Mismatch**: BO with a GP surrogate assumes the objective is a smooth, stationary function. Highly discontinuous landscapes, functions with discrete variables, or non-stationary responses violate these assumptions. In such cases TPE, SMAC (random-forest surrogate), or CMA-ES may outperform GP-BO.

## Applications

Bayesian Optimization has become the standard method whenever each function evaluation is expensive and the budget is small (< a few hundred evaluations). Its most prominent application is hyperparameter optimization (HPO) for machine learning models — libraries like Ax, Optuna (with GP sampler), and SMAC3 all implement BO. Beyond ML, BO is used in drug discovery to propose new molecular candidates, in materials science to optimize alloy or catalyst properties, in robotics for policy search, and in engineering design for aerodynamic shape optimization.

- Hyperparameter optimization (HPO): learning rate, architecture search, regularization
- Drug discovery: molecular property optimization over chemical space
- Materials design: alloy composition, catalyst surface area, battery electrode geometry
- A/B testing: multi-armed bandit variants of BO for conversion optimization
- Robotics: sim-to-real transfer, controller gain tuning

> **Practical Starting Point**: For HPO in Python, start with Ax (Meta, wraps BoTorch) or Optuna with the GPSampler. Both handle integer/categorical variables, constraints, and parallelism out of the box. Use BoTorch directly only when you need custom acquisition functions or multi-objective BO.

Bayesian Optimization sits at the intersection of probabilistic modeling, decision theory, and numerical optimization. Its power comes from treating optimization as a statistical inference problem: maintain uncertainty about the objective, act to reduce it strategically, and exploit structure as it becomes apparent. For any problem where each evaluation costs real resources, BO should be the first algorithm you reach for.

