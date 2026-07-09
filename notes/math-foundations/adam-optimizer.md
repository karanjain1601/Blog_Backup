---
title: "Adam — Adaptive Learning Rates and Bias Correction"
slug: "adam-optimizer"
description: "Rigorous derivation of Adam combining RMSProp and momentum, bias correction analysis, convergence issues in convex case, AMSGrad fix, and practical guidance on hyperparameter selection."
tags: ["optimization", "math", "foundations"]
topic: "math-foundations"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiQWRhbSAoQWRhcHRpdmUgTW9tZW50IEVzdGltYXRpb24pIGNvbWJpbmVzIG1vbWVudHVtIHdpdGggUk1TUHJvcDogaXQgbWFpbnRhaW5zIGJvdGggYSBmaXJzdCBtb21lbnQgKGV4cG9uZW50aWFsIG1vdmluZyBhdmVyYWdlIG9mIGdyYWRpZW50cykgYW5kIGEgc2Vjb25kIG1vbWVudCAoRU1BIG9mIHNxdWFyZWQgZ3JhZGllbnRzKS4gVGhpcyBnaXZlcyBlYWNoIHBhcmFtZXRlciBpdHMgb3duIGFkYXB0aXZlIGxlYXJuaW5nIHJhdGUsIGludmVyc2VseSBwcm9wb3J0aW9uYWwgdG8gdGhlIHNxdWFyZSByb290IG9mIGl0cyBncmFkaWVudCB2YXJpYW5jZS4gQWRhcHRpdmUgcmF0ZXMgYXJlIGVzcGVjaWFsbHkgdmFsdWFibGUgZm9yIE5MUDogZW1iZWRkaW5nIHRhYmxlcyByZWNlaXZlIHNwYXJzZSB1cGRhdGVzIOKAlCBtb3N0IGVtYmVkZGluZ3MgYXJlIHVudG91Y2hlZCBpbiBhbnkgZ2l2ZW4gYmF0Y2guIEFkYW0gYW1wbGlmaWVzIExSIGZvciByYXJlbHktdXBkYXRlZCBwYXJhbWV0ZXJzIGFuZCBkYW1wZW5zIGl0IGZvciBmcmVxdWVudGx5LXVwZGF0ZWQgb25lcy4gVGhlc2UgcHJvcGVydGllcyBleHBsYWluIHdoeSBBZGFtIGRvbWluYXRlcyBkZWVwIGxlYXJuaW5nIGZvciBsYW5ndWFnZSwgc3BlZWNoLCBhbmQgbXVsdGltb2RhbCBtb2RlbHMuIn0sIHsidHlwZSI6ICJoZWFkaW5nIiwgImxldmVsIjogMiwgImNvbnRlbnQiOiAiQ29yZSBBbGdvcml0aG06IEZpcnN0IGFuZCBTZWNvbmQgTW9tZW50cyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZpcnN0IG1vbWVudDogbV90ID0gYmV0YTEqbV97dC0xfSArICgxLWJldGExKSpnX3QuIFNlY29uZCBtb21lbnQ6IHZfdCA9IGJldGEyKnZfe3QtMX0gKyAoMS1iZXRhMikqZ190XjIgKHVuY2VudGVyZWQgdmFyaWFuY2UpLiBCaWFzIGNvcnJlY3Rpb246IG1faGF0X3QgPSBtX3QvKDEtYmV0YTFedCksIHZfaGF0X3QgPSB2X3QvKDEtYmV0YTJedCkuIFVwZGF0ZTogdGhldGFfdCA9IHRoZXRhX3t0LTF9IC0gYWxwaGEgKiBtX2hhdF90IC8gKHNxcnQodl9oYXRfdCkgKyBlcHMpLiBCaWFzIGNvcnJlY3Rpb24gaXMgY3JpdGljYWw6IG1vbWVudHMgaW5pdGlhbGl6ZWQgYXQgemVybywgc28gZWFybHkgZXN0aW1hdGVzIGFyZSBiaWFzZWQgdG93YXJkIHplcm8g4oCUIHdpdGhvdXQgY29ycmVjdGlvbiwgZWZmZWN0aXZlIExSIGlzIGZhciBzbWFsbGVyIHRoYW4gYWxwaGEgaW4gdGhlIGZpcnN0IGh1bmRyZWRzIG9mIHN0ZXBzLiBEZWZhdWx0czogYmV0YTE9MC45LCBiZXRhMj0wLjk5OSwgZXBzPTFlLTgsIGFscGhhPTFlLTMuIFRoZSBzZWNvbmQgbW9tZW50IHdhcm1zIHVwIG1vcmUgc2xvd2x5IHRoYW4gdGhlIGZpcnN0OiB3aXRoIGJldGEyPTAuOTk5LCBpdCB0YWtlcyB+MTAwMCBzdGVwcyB0byBiZSByZWxpYWJsZS4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBhZGFtX3N0ZXAoZywgbSwgdiwgdCwgbHI9MWUtMywgYjE9MC45LCBiMj0wLjk5OSwgZXBzPTFlLTgpOlxuICAgIG0gPSBiMSAqIG0gKyAoMSAtIGIxKSAqIGdcbiAgICB2ID0gYjIgKiB2ICsgKDEgLSBiMikgKiBnICoqIDJcbiAgICAjIGJpYXMtY29ycmVjdGVkIGVzdGltYXRlc1xuICAgIG1faGF0ID0gbSAvICgxIC0gYjEgKiogdClcbiAgICB2X2hhdCA9IHYgLyAoMSAtIGIyICoqIHQpXG4gICAgdXBkYXRlID0gbHIgKiBtX2hhdCAvIChucC5zcXJ0KHZfaGF0KSArIGVwcylcbiAgICByZXR1cm4gdXBkYXRlLCBtLCB2XG5cbmRlZiBhZGFtX25vX2NvcnJlY3Rpb24oZywgbSwgdiwgbHI9MWUtMywgYjE9MC45LCBiMj0wLjk5OSwgZXBzPTFlLTgpOlxuICAgIG0gPSBiMSAqIG0gKyAoMSAtIGIxKSAqIGdcbiAgICB2ID0gYjIgKiB2ICsgKDEgLSBiMikgKiBnICoqIDJcbiAgICByZXR1cm4gbHIgKiBtIC8gKG5wLnNxcnQodikgKyBlcHMpLCBtLCB2XG5cbiMgU2hvdyBiaWFzIGVmZmVjdCBhdCBlYXJseSBzdGVwcyAodHJ1ZSBncmFkaWVudCA9IDEuMClcbmcgPSBucC5hcnJheShbMS4wXSlcbm0gPSB2ID0gbnAuemVyb3MoMSlcbnByaW50KFwic3RlcCB8IGNvcnJlY3RlZF91cGRhdGUgfCB1bmNvcnJlY3RlZF91cGRhdGVcIilcbmZvciB0IGluIHJhbmdlKDEsIDYpOlxuICAgIHVfY29yciwgbSwgdiA9IGFkYW1fc3RlcChnLCBtLCB2LCB0KVxuICAgIG0yID0gdjIgPSBucC56ZXJvcygxKVxuICAgIGZvciB0dCBpbiByYW5nZSgxLCB0ICsgMSk6XG4gICAgICAgIHVfdW5jLCBtMiwgdjIgPSBhZGFtX25vX2NvcnJlY3Rpb24oZywgbTIsIHYyKVxuICAgIHByaW50KGZcIiAge3R9ICB8ICAgIHt1X2NvcnJbMF06LjZmfSAgICB8ICAgIHt1X3VuY1swXTouNmZ9XCIpXG4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJXaHkgQWRhcHRpdmUgUmF0ZXMgSGVscDogU3BhcnNlIEdyYWRpZW50cyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkZvciBOTFAgdGFza3Mgd2l0aCBlbWJlZGRpbmcgdGFibGVzOiBtb3N0IGVtYmVkZGluZ3MgYXJlIG5vdCBhY3RpdmF0ZWQgaW4gYW55IGdpdmVuIGJhdGNoLCBwcm9kdWNpbmcgc3BhcnNlIGdyYWRpZW50cy4gVmFuaWxsYSBTR0QgYXBwbGllcyB0aGUgc2FtZSBMUiB0byBhbGwgcGFyYW1ldGVycyByZWdhcmRsZXNzIG9mIHVwZGF0ZSBmcmVxdWVuY3kuIEFkYW0ncyAxL3NxcnQodl9oYXQpIHNjYWxlcyBkb3duIExSIGZvciBmcmVxdWVudGx5LXVwZGF0ZWQgcGFyYW1ldGVycyAobGFyZ2Ugdl9oYXRfdCBuZWFyIEVbZ14yXSkgYW5kIHNjYWxlcyB1cCBmb3IgcmFyZWx5LXVwZGF0ZWQgcGFyYW1ldGVycyAoc21hbGwgdl9oYXRfdCkuIFRoaXMgaXMgd2h5IEFkYW0gaXMgc3RhbmRhcmQgZm9yIE5MUCB3aGlsZSBTR0QgaXMgY29tcGV0aXRpdmUgZm9yIHZpc2lvbi4gVGhlIGVwc2lsb24gdmFsdWUgbWF0dGVyczogcHJldmVudHMgZGl2aXNpb24gYnkgemVybyBmb3IgemVyby1ncmFkaWVudCBwYXJhbWV0ZXJzLCBidXQgZXBzIHRvbyBsYXJnZSAoZS5nLiwgMWUtMykgbWFrZXMgdGhlIGRlbm9taW5hdG9yIGRvbWluYXRlZCBieSBlcHMsIGNhdXNpbmcgQWRhbSB0byBiZWhhdmUgbmVhcmx5IGxpa2UgU0dEIHdpdGggdW5pZm9ybSBzdGVwIHNpemVzIOKAlCBkZWZlYXRpbmcgdGhlIGFkYXB0aXZlIHB1cnBvc2UuIn0sIHsidHlwZSI6ICJjb2RlIiwgImxhbmd1YWdlIjogInB5dGhvbiIsICJjb250ZW50IjogImltcG9ydCBudW1weSBhcyBucFxuXG5ucC5yYW5kb20uc2VlZCg0MilcbiMgU3BhcnNlIGdyYWRpZW50IHByb2JsZW06IDEwMDAgcGFyYW1zLCBvbmx5IDUgYWN0aXZlIHBlciBzdGVwXG5uX3BhcmFtcyA9IDEwMDBcbm5fYWN0aXZlID0gNVxubl9zdGVwcyA9IDUwMFxubHIgPSAxZS0yXG5cbiMgR3JvdW5kIHRydXRoOiBhbGwgcGFyYW1zID0gMS4wXG50aGV0YV9hZGFtID0gbnAuemVyb3Mobl9wYXJhbXMpXG50aGV0YV9zZ2QgID0gbnAuemVyb3Mobl9wYXJhbXMpXG5tID0gbnAuemVyb3Mobl9wYXJhbXMpXG52ID0gbnAuemVyb3Mobl9wYXJhbXMpXG5cbmxvc3Nlc19hZGFtLCBsb3NzZXNfc2dkID0gW10sIFtdXG5mb3IgdCBpbiByYW5nZSgxLCBuX3N0ZXBzICsgMSk6XG4gICAgIyBzcGFyc2UgZ3JhZGllbnQ6IHJhbmRvbSBzdWJzZXQgYWN0aXZhdGVkXG4gICAgaWR4ID0gbnAucmFuZG9tLmNob2ljZShuX3BhcmFtcywgbl9hY3RpdmUsIHJlcGxhY2U9RmFsc2UpXG4gICAgZyA9IG5wLnplcm9zKG5fcGFyYW1zKVxuICAgIGdbaWR4XSA9IHRoZXRhX2FkYW1baWR4XSAtIDEuMCAgIyBncmFkaWVudCBvZiAodGhldGEtMSleMlxuXG4gICAgbSA9IDAuOSAqIG0gKyAwLjEgKiBnXG4gICAgdiA9IDAuOTk5ICogdiArIDAuMDAxICogZyAqKiAyXG4gICAgbV9oYXQgPSBtIC8gKDEgLSAwLjkgKiogdClcbiAgICB2X2hhdCA9IHYgLyAoMSAtIDAuOTk5ICoqIHQpXG4gICAgdGhldGFfYWRhbSAtPSBsciAqIG1faGF0IC8gKG5wLnNxcnQodl9oYXQpICsgMWUtOClcblxuICAgIGdfc2dkID0gbnAuemVyb3Mobl9wYXJhbXMpXG4gICAgZ19zZ2RbaWR4XSA9IHRoZXRhX3NnZFtpZHhdIC0gMS4wXG4gICAgdGhldGFfc2dkIC09IGxyICogZ19zZ2RcblxuICAgIGxvc3Nlc19hZGFtLmFwcGVuZChucC5tZWFuKCh0aGV0YV9hZGFtIC0gMSkgKiogMikpXG4gICAgbG9zc2VzX3NnZC5hcHBlbmQobnAubWVhbigodGhldGFfc2dkIC0gMSkgKiogMikpXG5cbnByaW50KGZcIkZpbmFsIE1TRSDigJQgQWRhbToge2xvc3Nlc19hZGFtWy0xXTouNmZ9LCBTR0Q6IHtsb3NzZXNfc2dkWy0xXTouNmZ9XCIpXG5wcmludChmXCJBZGFtIGNvbnZlcmdlcyBmYXN0ZXIgb24gc3BhcnNlIHByb2JsZW1zIGJ5IHtsb3NzZXNfc2dkWy0xXS9sb3NzZXNfYWRhbVstMV06LjFmfXhcIilcbiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIkJpYXMgQ29ycmVjdGlvbiBBbmFseXNpcyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIldpdGhvdXQgYmlhcyBjb3JyZWN0aW9uIGF0IHQ9MTogbV8xID0gKDEtYmV0YTEpKmdfMSwgaS5lLiwgb25seSAxMCUgb2YgZ3JhZGllbnQgbWFnbml0dWRlIGZvciBiZXRhMT0wLjkuIFRoZSB1cGRhdGUgd291bGQgYmUgd2lsZGx5IHVuZGVyc2NhbGVkIGluIGVhcmx5IHN0ZXBzLiBCaWFzIGNvcnJlY3Rpb24gcmVjb3ZlcnMgdGhlIHRydWUgZXN0aW1hdGU6IG1faGF0XzEgPSBtXzEvKDEtYmV0YTFeMSkgPSBnXzEuIEF0IHQ9MTA6IDEtYmV0YTFeMTAgfiAwLjY1MSwgc28gY29ycmVjdGlvbiBpcyBzdGlsbCBzaWduaWZpY2FudCAofjM1JSB1bmRlcmVzdGltYXRlIHdpdGhvdXQgaXQpLiBBdCB0PTEwMDogY29ycmVjdGlvbiBpcyBuZWdsaWdpYmxlLiBUaGUgc2Vjb25kIG1vbWVudCBpcyBtdWNoIHNsb3dlciB0byB3YXJtIHVwOiBiZXRhMj0wLjk5OSBtZWFucyAxLWJldGEyXjEwMCA9IDAuMDk1LCBzbyB2X2hhdCBpcyBvbmx5IDkuNSUgYWNjdXJhdGUgYWZ0ZXIgMTAwIHN0ZXBzIOKAlCBtYWtpbmcgdGhlIGVmZmVjdGl2ZSBMUiBtdWNoIGxhcmdlciB0aGFuIGludGVuZGVkLiBUaGlzIG1vdGl2YXRlcyBMUiB3YXJtdXA6IGRlbGF5aW5nIHRoZSBmdWxsIExSIHVudGlsIHZfaGF0IGlzIHJlbGlhYmxlLCB0eXBpY2FsbHkgYWZ0ZXIgMTAwMCsgc3RlcHMgd2l0aCBiZXRhMj0wLjk5OS4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJOb24tQ29udmVyZ2VuY2UgaW4gQ29udmV4IENhc2UgYW5kIEFNU0dyYWQifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJSZWRkaSBldCBhbC4gKDIwMTgpIHByb3ZlZCBBZGFtIGNhbiBmYWlsIHRvIGNvbnZlcmdlIGV2ZW4gb24gc2ltcGxlIGNvbnZleCBwcm9ibGVtcy4gVGhlIGNvdW50ZXJleGFtcGxlOiBhIDFEIHByb2JsZW0gd2hlcmUgdGhlIG9wdGltYWwgc29sdXRpb24gcmVxdWlyZXMgYWNjdW11bGF0ZWQga25vd2xlZGdlIGZyb20gcmFyZSBsYXJnZSBncmFkaWVudHMuIEFkYW0ncyBkZWNheWluZyB2X2hhdCBmb3JnZXRzIHRoZXNlIGxhcmdlIGdyYWRpZW50cyBvdmVyIHRpbWUsIGFuZCB0aGUgZWZmZWN0aXZlIExSIGdyb3dzIHdoZW4gaXQgc2hvdWxkIHN0YXkgc21hbGwuIFRoZSBmaXg6IEFNU0dyYWQgbWFpbnRhaW5zIHZfaGF0X21heCA9IG1heCh2X2hhdF9tYXgsIHZfaGF0X3QpIOKAlCBhIG5ldmVyLWRlY3JlYXNpbmcgZGVub21pbmF0b3Ig4oCUIGVuc3VyaW5nIGVmZmVjdGl2ZSBzdGVwIHNpemUgaXMgbm9uLWluY3JlYXNpbmcuIFRoaXMgZ3VhcmFudGVlcyBjb252ZXJnZW5jZS4gSW4gcHJhY3RpY2UsIEFNU0dyYWQgcGVyZm9ybXMgc2ltaWxhcmx5IHRvIEFkYW0gb24gcmVhbCB0YXNrczsgdGhlIGNvdW50ZXJleGFtcGxlIHJlcXVpcmVzIGFkdmVyc2FyaWFsbHkgY2hvc2VuIHNlcXVlbmNlcy4gTmV2ZXJ0aGVsZXNzLCBBTVNHcmFkIGlzIHRoZSB0aGVvcmV0aWNhbGx5LXNhZmUgY2hvaWNlIGFuZCBhdmFpbGFibGUgaW4gUHlUb3JjaCB2aWEgYW1zZ3JhZD1UcnVlLiJ9LCB7InR5cGUiOiAiY29kZSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAiY29udGVudCI6ICJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGFtc2dyYWRfc3RlcChnLCBtLCB2LCB2X21heCwgdCwgbHI9MWUtMywgYjE9MC45LCBiMj0wLjk5OSwgZXBzPTFlLTgpOlxuICAgIG0gPSBiMSAqIG0gKyAoMSAtIGIxKSAqIGdcbiAgICB2ID0gYjIgKiB2ICsgKDEgLSBiMikgKiBnICoqIDJcbiAgICBtX2hhdCA9IG0gLyAoMSAtIGIxICoqIHQpXG4gICAgdl9oYXQgPSB2IC8gKDEgLSBiMiAqKiB0KVxuICAgIHZfbWF4ID0gbnAubWF4aW11bSh2X21heCwgdl9oYXQpICAjIG5ldmVyLWRlY3JlYXNpbmcgZGVub21pbmF0b3JcbiAgICB1cGRhdGUgPSBsciAqIG1faGF0IC8gKG5wLnNxcnQodl9tYXgpICsgZXBzKVxuICAgIHJldHVybiB1cGRhdGUsIG0sIHYsIHZfbWF4XG5cbiMgUmVkZGktc3R5bGUgcHJvYmxlbTogZ3JhZGllbnQgYWx0ZXJuYXRlcyBiZXR3ZWVuIGxhcmdlIHJhcmUgYW5kIHNtYWxsIGZyZXF1ZW50XG5ucC5yYW5kb20uc2VlZCgwKVxubl9zdGVwcyA9IDIwMDBcbnRoZXRhX2FkYW0gPSBucC56ZXJvcygxKVxudGhldGFfYW1zICA9IG5wLnplcm9zKDEpXG5tX2EgPSB2X2EgPSBtX3MgPSB2X3MgPSBucC56ZXJvcygxKVxudl9tYXggPSBucC56ZXJvcygxKVxuXG5mb3IgdCBpbiByYW5nZSgxLCBuX3N0ZXBzICsgMSk6XG4gICAgIyByYXJlIGxhcmdlIGdyYWRpZW50IChldmVyeSAxMDAgc3RlcHMpIGVsc2Ugc21hbGxcbiAgICBnID0gbnAuYXJyYXkoWzEwLjBdKSBpZiB0ICUgMTAxID09IDAgZWxzZSBucC5hcnJheShbLTAuMV0pXG5cbiAgICBtX2EgPSAwLjkgKiBtX2EgKyAwLjEgKiBnXG4gICAgdl9hID0gMC45OTkgKiB2X2EgKyAwLjAwMSAqIGcgKiogMlxuICAgIG1faGF0ID0gbV9hIC8gKDEgLSAwLjkgKiogdClcbiAgICB2X2hhdCA9IHZfYSAvICgxIC0gMC45OTkgKiogdClcbiAgICB0aGV0YV9hZGFtIC09IDFlLTMgKiBtX2hhdCAvIChucC5zcXJ0KHZfaGF0KSArIDFlLTgpXG5cbiAgICB1cGQsIG1fcywgdl9zLCB2X21heCA9IGFtc2dyYWRfc3RlcChnLCBtX3MsIHZfcywgdl9tYXgsIHQpXG4gICAgdGhldGFfYW1zIC09IHVwZFxuXG5wcmludChmXCJBZGFtIGZpbmFsIHRoZXRhOiAgICB7dGhldGFfYWRhbVswXTouNGZ9XCIpXG5wcmludChmXCJBTVNHcmFkIGZpbmFsIHRoZXRhOiB7dGhldGFfYW1zWzBdOi40Zn1cIilcbiJ9LCB7InR5cGUiOiAiaGVhZGluZyIsICJsZXZlbCI6IDIsICJjb250ZW50IjogIk1MIENvbm5lY3Rpb25zOiBUcmFuc2Zvcm1lciBUcmFpbmluZyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIkFkYW0gaXMgdGhlIGRlIGZhY3RvIG9wdGltaXplciBmb3IgdHJhbnNmb3JtZXIgdHJhaW5pbmcuIEF0dGVudGlvbiBsYXllcnMgaGF2ZSBncmFkaWVudCBtYWduaXR1ZGVzIHRoYXQgdmFyeSBkcmFtYXRpY2FsbHkgYWNyb3NzIGhlYWRzIGFuZCBwb3NpdGlvbnM7IGVtYmVkZGluZyBsYXllcnMgcmVjZWl2ZSBzcGFyc2UgdXBkYXRlcy4gQm90aCBjb25kaXRpb25zIGZhdm9yIGFkYXB0aXZlIHJhdGVzLiBUeXBpY2FsIHRyYW5zZm9ybWVyIGh5cGVycGFyYW1ldGVyczogYmV0YTE9MC45LCBiZXRhMj0wLjk5OSwgZXBzPTFlLTgsIExSIHdhcm11cCBmb3IgfjQlIG9mIHRyYWluaW5nLCB0aGVuIGNvc2luZSBkZWNheS4gR1BULTMgdXNlZCBMUj02ZS01IHdpdGggYmF0Y2ggc2l6ZSAzLjJNIHRva2Vucy4gVGhlIGVwc2lsb24gdmFsdWUgbWF0dGVycyBtb3JlIHRoYW4gY29tbW9ubHkgYWNrbm93bGVkZ2VkOiBlcHM9MWUtOCBpcyBzdGFuZGFyZCBidXQgZXBzPTFlLTYgY2FuIGltcHJvdmUgc3RhYmlsaXR5IGZvciBwb29ybHktc2NhbGVkIGxvc3Nlcy4gU29tZSBMTE0gdHJhaW5pbmcgdXNlcyBiZXRhMj0wLjk1IHRvIHJlZHVjZSB0aGUgZWZmZWN0aXZlIGF2ZXJhZ2luZyB3aW5kb3cgYW5kIHJlc3BvbmQgZmFzdGVyIHRvIGdyYWRpZW50IGNoYW5nZXMgZHVyaW5nIGRpc3RyaWJ1dGlvbiBzaGlmdCBlYXJseSBpbiB0cmFpbmluZy4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJJbXBsZW1lbnRhdGlvbiBQaXRmYWxscyJ9LCB7InR5cGUiOiAidGV4dCIsICJjb250ZW50IjogIlBpdGZhbGwgMTogZm9yZ2V0dGluZyBiaWFzIGNvcnJlY3Rpb24g4oCUIHRyYWluaW5nIGFwcGVhcnMgc2xvdyBpbiB0aGUgZmlyc3QgMTAwLTUwMCBzdGVwcyBiZWNhdXNlIHRoZSBlZmZlY3RpdmUgTFIgaXMgbXVjaCBsb3dlciB0aGFuIHNldC4gUGl0ZmFsbCAyOiBlcHNpbG9uIHRvbyBsYXJnZSDigJQgaWYgZXBzPTAuMSwgdGhlIGRlbm9taW5hdG9yIHNxcnQodl9oYXQpK2VwcyBhcHByb3hpbWF0ZXMgZXBzIGZvciBzbWFsbCBncmFkaWVudHMsIGdpdmluZyBuZWFybHkgdW5pZm9ybSBzdGVwIHNpemVzIGFuZCBkZWZlYXRpbmcgYWRhcHRhdGlvbi4gUGl0ZmFsbCAzOiB3ZWlnaHQgZGVjYXkgaW4gc3RhbmRhcmQgQWRhbSBpcyBub3QgZXF1aXZhbGVudCB0byBMMiByZWd1bGFyaXphdGlvbiDigJQgdXNlIEFkYW1XIGluc3RlYWQuIFBpdGZhbGwgNDogaW1wbGVtZW50YXRpb24gZGlmZmVyZW5jZXMg4oCUIFB5VG9yY2ggYXBwbGllcyBlcHMgaW5zaWRlIHRoZSBkZW5vbWluYXRvciBhcyAxLyhzcXJ0KHZfaGF0KStlcHMpOyBzb21lIFRlbnNvckZsb3cgdmVyc2lvbnMgYXBwbHkgaXQgZGlmZmVyZW50bHkuIEFsd2F5cyB2ZXJpZnkgYmVoYXZpb3IgbWF0Y2hlcyBleHBlY3RhdGlvbiBieSBjaGVja2luZyB0aGUgZWZmZWN0aXZlIExSIG1hZ25pdHVkZSBlYXJseSBpbiB0cmFpbmluZy4ifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJQcmFjdGljYWwgR3VpZGFuY2UifSwgeyJ0eXBlIjogInRleHQiLCAiY29udGVudCI6ICJEZWZhdWx0IEFkYW0gcmVjaXBlOiBMUj0xZS0zIChmaW5lLXR1bmluZzogMWUtNCB0byA1ZS01KSwgYmV0YTE9MC45LCBiZXRhMj0wLjk5OSwgZXBzPTFlLTguIEZvciB0cmFuc2Zvcm1lcnM6IHVzZSBBZGFtVyAobm90IEFkYW0pIHdpdGggd2VpZ2h0IGRlY2F5IDAuMDEtMC4xLiBNb25pdG9yIHRoZSBzZWNvbmQgbW9tZW50IHZfaGF0X3QgYWNyb3NzIGxheWVycyDigJQgaWYgdl9oYXRfdCBpcyB2ZXJ5IHNtYWxsIGZvciBzb21lIGxheWVycywgZXBzIGRvbWluYXRlcyBhbmQgdGhvc2UgbGF5ZXJzIGdldCBlcXVhbCBMUiB0byBvdGhlcnMsIGRlZmVhdGluZyBhZGFwdGl2ZSBwdXJwb3NlLiBUcmFjayBlZmZlY3RpdmUgTFIgPSBhbHBoYS9zcXJ0KHZfaGF0X3QpIHBlciBsYXllci4gRm9yIHNwYXJzZSBOTFAgbW9kZWxzLCBjb25zaWRlciBpbmNyZWFzaW5nIGJldGEyIHRvIDAuOTk5OSBmb3IgbW9yZSBzdGFibGUgc2Vjb25kLW1vbWVudCBlc3RpbWF0ZXMsIGNvbWJpbmVkIHdpdGggbG9uZ2VyIHdhcm11cC4ifSwgeyJ0eXBlIjogImNvZGUiLCAibGFuZ3VhZ2UiOiAicHl0aG9uIiwgImNvbnRlbnQiOiAiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuIyBTaW11bGF0ZSB0cmFuc2Zvcm1lci1saWtlIHRyYWluaW5nIHdpdGggTFIgbW9uaXRvcmluZ1xudG9yY2gubWFudWFsX3NlZWQoNDIpXG5tb2RlbCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uTGluZWFyKDEyOCwgMjU2KSwgbm4uUmVMVSgpLFxuICAgIG5uLkxpbmVhcigyNTYsIDI1NiksIG5uLlJlTFUoKSxcbiAgICBubi5MaW5lYXIoMjU2LCAxMClcbilcbm9wdGltaXplciA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0zLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYmV0YXM9KDAuOSwgMC45OTkpLCBlcHM9MWUtOClcblxueCA9IHRvcmNoLnJhbmRuKDMyLCAxMjgpXG55ID0gdG9yY2gucmFuZGludCgwLCAxMCwgKDMyLCkpXG5jcml0ZXJpb24gPSBubi5Dcm9zc0VudHJvcHlMb3NzKClcblxuZm9yIHN0ZXAgaW4gcmFuZ2UoNTApOlxuICAgIG9wdGltaXplci56ZXJvX2dyYWQoKVxuICAgIGxvc3MgPSBjcml0ZXJpb24obW9kZWwoeCksIHkpXG4gICAgbG9zcy5iYWNrd2FyZCgpXG4gICAgb3B0aW1pemVyLnN0ZXAoKVxuXG4jIEluc3BlY3QgZWZmZWN0aXZlIExSID0gbHIgLyBzcXJ0KHZfaGF0KSBwZXIgcGFyYW1ldGVyIGdyb3VwXG5wcmludChcIkVmZmVjdGl2ZSBMUiBwZXIgbGF5ZXIgKGZpcnN0IHBhcmFtIHRlbnNvcik6XCIpXG5mb3IgaSwgcGcgaW4gZW51bWVyYXRlKG9wdGltaXplci5wYXJhbV9ncm91cHMpOlxuICAgIGZvciBwIGluIHBnWydwYXJhbXMnXTpcbiAgICAgICAgc3RhdGUgPSBvcHRpbWl6ZXIuc3RhdGVbcF1cbiAgICAgICAgaWYgbGVuKHN0YXRlKSA+IDAgYW5kIHAuZ3JhZCBpcyBub3QgTm9uZTpcbiAgICAgICAgICAgIGV4cF9hdmdfc3EgPSBzdGF0ZVsnZXhwX2F2Z19zcSddXG4gICAgICAgICAgICBzdGVwX2NvdW50ID0gc3RhdGVbJ3N0ZXAnXVxuICAgICAgICAgICAgYmMgPSAxIC0gMC45OTkgKiogc3RlcF9jb3VudC5pdGVtKClcbiAgICAgICAgICAgIHZfaGF0ID0gZXhwX2F2Z19zcSAvIGJjXG4gICAgICAgICAgICBlZmZfbHIgPSBwZ1snbHInXSAvICh2X2hhdC5zcXJ0KCkgKyAxZS04KVxuICAgICAgICAgICAgcHJpbnQoZlwiICBzaGFwZT17dHVwbGUocC5zaGFwZSl9ICBlZmZfbHIgbWVhbj17ZWZmX2xyLm1lYW4oKTouMmV9ICBzdGQ9e2VmZl9sci5zdGQoKTouMmV9XCIpXG4gICAgICAgICAgICBicmVha1xuIn0sIHsidHlwZSI6ICJjYWxsb3V0IiwgInRpdGxlIjogIlVzZSBBZGFtVyBOb3QgQWRhbSBmb3IgUmVndWxhcml6ZWQgVHJhaW5pbmciLCAiY29udGVudCI6ICJTdGFuZGFyZCBBZGFtIHdpdGggd2VpZ2h0X2RlY2F5IGFkZHMgbGFtYmRhKnRoZXRhIHRvIHRoZSBncmFkaWVudCBiZWZvcmUgdGhlIGFkYXB0aXZlIHVwZGF0ZS4gVGhlIGVmZmVjdGl2ZSBkZWNheSBiZWNvbWVzIGxhbWJkYSphbHBoYS8oc3FydCh2X2hhdCkrZXBzKSDigJQgdmFyeWluZyBwZXIgcGFyYW1ldGVyLiBQYXJhbWV0ZXJzIHdpdGggbGFyZ2UgZ3JhZGllbnQgaGlzdG9yeSAobGFyZ2UgdikgZ2V0IHdlYWtlciByZWd1bGFyaXphdGlvbi4gQWRhbVcgZGVjb3VwbGVzIHdlaWdodCBkZWNheTogYXBwbHkgdGhldGEgPC0gdGhldGEqKDEtbGFtYmRhKmFscGhhKSBkaXJlY3RseSwgYmVmb3JlIHRoZSBhZGFwdGl2ZSBncmFkaWVudCBzdGVwLiBUaGlzIGdpdmVzIHVuaWZvcm0gc2hyaW5rYWdlIHJlZ2FyZGxlc3Mgb2YgZ3JhZGllbnQgaGlzdG9yeS4gQWx3YXlzIHVzZSBBZGFtVyBmb3IgcmVndWxhcml6ZWQgdHJhaW5pbmcuIFRoZSBkaWZmZXJlbmNlIGlzIHNpZ25pZmljYW50IGZvciBsYXJnZSB0cmFuc2Zvcm1lciBtb2RlbHMgd2hlcmUgZ3JhZGllbnQgbWFnbml0dWRlcyB2YXJ5IGJ5IG9yZGVycyBvZiBtYWduaXR1ZGUgYWNyb3NzIGxheWVycy4ifSwgeyJ0eXBlIjogInRhYmxlIiwgImhlYWRlcnMiOiBbIkh5cGVycGFyYW1ldGVyIiwgIkRlZmF1bHQiLCAiRWZmZWN0IG9mIEluY3JlYXNpbmciLCAiRWZmZWN0IG9mIERlY3JlYXNpbmciXSwgInJvd3MiOiBbWyJhbHBoYSAobGVhcm5pbmcgcmF0ZSkiLCAiMWUtMyIsICJGYXN0ZXIgYnV0IGxlc3Mgc3RhYmxlIiwgIlNsb3dlciBjb252ZXJnZW5jZSJdLCBbImJldGExIChtb21lbnR1bSkiLCAiMC45IiwgIk1vcmUgbW9tZW50dW0sIHNtb290aGVyIHVwZGF0ZXMiLCAiTGVzcyBtb21lbnR1bSwgbm9pc2llciB1cGRhdGVzIl0sIFsiYmV0YTIgKHNlY29uZCBtb21lbnQpIiwgIjAuOTk5IiwgIlNsb3dlciBhZGFwdGF0aW9uLCBtb3JlIHN0YWJsZSB2X2hhdCIsICJGYXN0ZXIgYWRhcHRhdGlvbiwgbm9pc2llciB2X2hhdCJdLCBbImVwcyAoZXBzaWxvbikiLCAiMWUtOCIsICJNb3JlIHVuaWZvcm0gTFIgKGxlc3MgYWRhcHRpdmUpIiwgIk1vcmUgYWRhcHRpdmUsIHBvdGVudGlhbCBudW1lcmljYWwgaXNzdWVzIl0sIFsid2VpZ2h0X2RlY2F5IiwgIjAgKEFkYW0pIC8gMC4wMS0wLjEgKEFkYW1XKSIsICJTdHJvbmdlciByZWd1bGFyaXphdGlvbiIsICJMZXNzIHJlZ3VsYXJpemF0aW9uIl1dfSwgeyJ0eXBlIjogImRpdmlkZXIifSwgeyJ0eXBlIjogImhlYWRpbmciLCAibGV2ZWwiOiAyLCAiY29udGVudCI6ICJLZXkgVGFrZWF3YXlzIn0sIHsidHlwZSI6ICJsaXN0IiwgIml0ZW1zIjogWyJBZGFtID0gbW9tZW50dW0gKGZpcnN0IG1vbWVudCkgKyBSTVNQcm9wIChzZWNvbmQgbW9tZW50KSwgd2l0aCBiaWFzIGNvcnJlY3Rpb24gZm9yIGJvdGguIiwgIkJpYXMgY29ycmVjdGlvbiBpcyBlc3NlbnRpYWw6IHdpdGhvdXQgaXQsIGVhcmx5IHVwZGF0ZXMgYXJlIG1hc3NpdmVseSB1bmRlcnNjYWxlZCAoMTAlIG9mIGludGVuZGVkIExSIGF0IHQ9MSB3aXRoIGJldGExPTAuOSkuIiwgIkFkYXB0aXZlIHJhdGVzIGhlbHAgbW9zdCBmb3Igc3BhcnNlIGdyYWRpZW50cyAoTkxQIGVtYmVkZGluZ3MpOyBmb3IgZGVuc2UgdmlzaW9uIHRhc2tzLCBTR0QgaXMgb2Z0ZW4gY29tcGV0aXRpdmUuIiwgIkFkYW0gY2FuIGZhaWwgdG8gY29udmVyZ2Ugb24gY29udmV4IHByb2JsZW1zIChSZWRkaSAyMDE4KTsgQU1TR3JhZCBmaXhlcyB0aGlzIHdpdGggYSBub24tZGVjcmVhc2luZyBkZW5vbWluYXRvci4iLCAiVXNlIEFkYW1XLCBub3QgQWRhbSwgd2hlbmV2ZXIgd2VpZ2h0IGRlY2F5IGlzIG5lZWRlZCDigJQgc3RhbmRhcmQgQWRhbSdzIEwyIGlzIGNvcnJ1cHRlZCBieSBhZGFwdGl2ZSByYXRlcy4iLCAiTW9uaXRvciBlZmZlY3RpdmUgTFIgPSBhbHBoYS9zcXJ0KHZfaGF0KSBwZXIgbGF5ZXI7IGlmIGVwcyBkb21pbmF0ZXMgKHZfaGF0IDw8IGVwc14yKSwgYWRhcHRhdGlvbiBpcyBsb3N0LiIsICJCZXRhMj0wLjk5OSByZXF1aXJlcyB+MTAwMCBzdGVwcyB0byB3YXJtIHVwOyBjb21iaW5lIHdpdGggTFIgd2FybXVwIHRvIGF2b2lkIGVhcmx5IGluc3RhYmlsaXR5IGZyb20gdW5yZWxpYWJsZSB2X2hhdC4iXX1d"
---

# Adam — Adaptive Learning Rates and Bias Correction

Adam (Adaptive Moment Estimation) combines momentum with RMSProp: it maintains both a first moment (exponential moving average of gradients) and a second moment (EMA of squared gradients). This gives each parameter its own adaptive learning rate, inversely proportional to the square root of its gradient variance. Adaptive rates are especially valuable for NLP: embedding tables receive sparse updates — most embeddings are untouched in any given batch. Adam amplifies LR for rarely-updated parameters and dampens it for frequently-updated ones. These properties explain why Adam dominates deep learning for language, speech, and multimodal models.

## Core Algorithm: First and Second Moments

First moment: m_t = beta1*m_{t-1} + (1-beta1)*g_t. Second moment: v_t = beta2*v_{t-1} + (1-beta2)*g_t^2 (uncentered variance). Bias correction: m_hat_t = m_t/(1-beta1^t), v_hat_t = v_t/(1-beta2^t). Update: theta_t = theta_{t-1} - alpha * m_hat_t / (sqrt(v_hat_t) + eps). Bias correction is critical: moments initialized at zero, so early estimates are biased toward zero — without correction, effective LR is far smaller than alpha in the first hundreds of steps. Defaults: beta1=0.9, beta2=0.999, eps=1e-8, alpha=1e-3. The second moment warms up more slowly than the first: with beta2=0.999, it takes ~1000 steps to be reliable.

```python
import numpy as np

def adam_step(g, m, v, t, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    # bias-corrected estimates
    m_hat = m / (1 - b1 ** t)
    v_hat = v / (1 - b2 ** t)
    update = lr * m_hat / (np.sqrt(v_hat) + eps)
    return update, m, v

def adam_no_correction(g, m, v, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    return lr * m / (np.sqrt(v) + eps), m, v

# Show bias effect at early steps (true gradient = 1.0)
g = np.array([1.0])
m = v = np.zeros(1)
print("step | corrected_update | uncorrected_update")
for t in range(1, 6):
    u_corr, m, v = adam_step(g, m, v, t)
    m2 = v2 = np.zeros(1)
    for tt in range(1, t + 1):
        u_unc, m2, v2 = adam_no_correction(g, m2, v2)
    print(f"  {t}  |    {u_corr[0]:.6f}    |    {u_unc[0]:.6f}")

```

## Why Adaptive Rates Help: Sparse Gradients

For NLP tasks with embedding tables: most embeddings are not activated in any given batch, producing sparse gradients. Vanilla SGD applies the same LR to all parameters regardless of update frequency. Adam's 1/sqrt(v_hat) scales down LR for frequently-updated parameters (large v_hat_t near E[g^2]) and scales up for rarely-updated parameters (small v_hat_t). This is why Adam is standard for NLP while SGD is competitive for vision. The epsilon value matters: prevents division by zero for zero-gradient parameters, but eps too large (e.g., 1e-3) makes the denominator dominated by eps, causing Adam to behave nearly like SGD with uniform step sizes — defeating the adaptive purpose.

```python
import numpy as np

np.random.seed(42)
# Sparse gradient problem: 1000 params, only 5 active per step
n_params = 1000
n_active = 5
n_steps = 500
lr = 1e-2

# Ground truth: all params = 1.0
theta_adam = np.zeros(n_params)
theta_sgd  = np.zeros(n_params)
m = np.zeros(n_params)
v = np.zeros(n_params)

losses_adam, losses_sgd = [], []
for t in range(1, n_steps + 1):
    # sparse gradient: random subset activated
    idx = np.random.choice(n_params, n_active, replace=False)
    g = np.zeros(n_params)
    g[idx] = theta_adam[idx] - 1.0  # gradient of (theta-1)^2

    m = 0.9 * m + 0.1 * g
    v = 0.999 * v + 0.001 * g ** 2
    m_hat = m / (1 - 0.9 ** t)
    v_hat = v / (1 - 0.999 ** t)
    theta_adam -= lr * m_hat / (np.sqrt(v_hat) + 1e-8)

    g_sgd = np.zeros(n_params)
    g_sgd[idx] = theta_sgd[idx] - 1.0
    theta_sgd -= lr * g_sgd

    losses_adam.append(np.mean((theta_adam - 1) ** 2))
    losses_sgd.append(np.mean((theta_sgd - 1) ** 2))

print(f"Final MSE — Adam: {losses_adam[-1]:.6f}, SGD: {losses_sgd[-1]:.6f}")
print(f"Adam converges faster on sparse problems by {losses_sgd[-1]/losses_adam[-1]:.1f}x")

```

## Bias Correction Analysis

Without bias correction at t=1: m_1 = (1-beta1)*g_1, i.e., only 10% of gradient magnitude for beta1=0.9. The update would be wildly underscaled in early steps. Bias correction recovers the true estimate: m_hat_1 = m_1/(1-beta1^1) = g_1. At t=10: 1-beta1^10 ~ 0.651, so correction is still significant (~35% underestimate without it). At t=100: correction is negligible. The second moment is much slower to warm up: beta2=0.999 means 1-beta2^100 = 0.095, so v_hat is only 9.5% accurate after 100 steps — making the effective LR much larger than intended. This motivates LR warmup: delaying the full LR until v_hat is reliable, typically after 1000+ steps with beta2=0.999.

## Non-Convergence in Convex Case and AMSGrad

Reddi et al. (2018) proved Adam can fail to converge even on simple convex problems. The counterexample: a 1D problem where the optimal solution requires accumulated knowledge from rare large gradients. Adam's decaying v_hat forgets these large gradients over time, and the effective LR grows when it should stay small. The fix: AMSGrad maintains v_hat_max = max(v_hat_max, v_hat_t) — a never-decreasing denominator — ensuring effective step size is non-increasing. This guarantees convergence. In practice, AMSGrad performs similarly to Adam on real tasks; the counterexample requires adversarially chosen sequences. Nevertheless, AMSGrad is the theoretically-safe choice and available in PyTorch via amsgrad=True.

```python
import numpy as np

def amsgrad_step(g, m, v, v_max, t, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    m_hat = m / (1 - b1 ** t)
    v_hat = v / (1 - b2 ** t)
    v_max = np.maximum(v_max, v_hat)  # never-decreasing denominator
    update = lr * m_hat / (np.sqrt(v_max) + eps)
    return update, m, v, v_max

# Reddi-style problem: gradient alternates between large rare and small frequent
np.random.seed(0)
n_steps = 2000
theta_adam = np.zeros(1)
theta_ams  = np.zeros(1)
m_a = v_a = m_s = v_s = np.zeros(1)
v_max = np.zeros(1)

for t in range(1, n_steps + 1):
    # rare large gradient (every 100 steps) else small
    g = np.array([10.0]) if t % 101 == 0 else np.array([-0.1])

    m_a = 0.9 * m_a + 0.1 * g
    v_a = 0.999 * v_a + 0.001 * g ** 2
    m_hat = m_a / (1 - 0.9 ** t)
    v_hat = v_a / (1 - 0.999 ** t)
    theta_adam -= 1e-3 * m_hat / (np.sqrt(v_hat) + 1e-8)

    upd, m_s, v_s, v_max = amsgrad_step(g, m_s, v_s, v_max, t)
    theta_ams -= upd

print(f"Adam final theta:    {theta_adam[0]:.4f}")
print(f"AMSGrad final theta: {theta_ams[0]:.4f}")

```

## ML Connections: Transformer Training

Adam is the de facto optimizer for transformer training. Attention layers have gradient magnitudes that vary dramatically across heads and positions; embedding layers receive sparse updates. Both conditions favor adaptive rates. Typical transformer hyperparameters: beta1=0.9, beta2=0.999, eps=1e-8, LR warmup for ~4% of training, then cosine decay. GPT-3 used LR=6e-5 with batch size 3.2M tokens. The epsilon value matters more than commonly acknowledged: eps=1e-8 is standard but eps=1e-6 can improve stability for poorly-scaled losses. Some LLM training uses beta2=0.95 to reduce the effective averaging window and respond faster to gradient changes during distribution shift early in training.

## Implementation Pitfalls

Pitfall 1: forgetting bias correction — training appears slow in the first 100-500 steps because the effective LR is much lower than set. Pitfall 2: epsilon too large — if eps=0.1, the denominator sqrt(v_hat)+eps approximates eps for small gradients, giving nearly uniform step sizes and defeating adaptation. Pitfall 3: weight decay in standard Adam is not equivalent to L2 regularization — use AdamW instead. Pitfall 4: implementation differences — PyTorch applies eps inside the denominator as 1/(sqrt(v_hat)+eps); some TensorFlow versions apply it differently. Always verify behavior matches expectation by checking the effective LR magnitude early in training.

## Practical Guidance

Default Adam recipe: LR=1e-3 (fine-tuning: 1e-4 to 5e-5), beta1=0.9, beta2=0.999, eps=1e-8. For transformers: use AdamW (not Adam) with weight decay 0.01-0.1. Monitor the second moment v_hat_t across layers — if v_hat_t is very small for some layers, eps dominates and those layers get equal LR to others, defeating adaptive purpose. Track effective LR = alpha/sqrt(v_hat_t) per layer. For sparse NLP models, consider increasing beta2 to 0.9999 for more stable second-moment estimates, combined with longer warmup.

```python
import torch
import torch.nn as nn

# Simulate transformer-like training with LR monitoring
torch.manual_seed(42)
model = nn.Sequential(
    nn.Linear(128, 256), nn.ReLU(),
    nn.Linear(256, 256), nn.ReLU(),
    nn.Linear(256, 10)
)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3,
                              betas=(0.9, 0.999), eps=1e-8)

x = torch.randn(32, 128)
y = torch.randint(0, 10, (32,))
criterion = nn.CrossEntropyLoss()

for step in range(50):
    optimizer.zero_grad()
    loss = criterion(model(x), y)
    loss.backward()
    optimizer.step()

# Inspect effective LR = lr / sqrt(v_hat) per parameter group
print("Effective LR per layer (first param tensor):")
for i, pg in enumerate(optimizer.param_groups):
    for p in pg['params']:
        state = optimizer.state[p]
        if len(state) > 0 and p.grad is not None:
            exp_avg_sq = state['exp_avg_sq']
            step_count = state['step']
            bc = 1 - 0.999 ** step_count.item()
            v_hat = exp_avg_sq / bc
            eff_lr = pg['lr'] / (v_hat.sqrt() + 1e-8)
            print(f"  shape={tuple(p.shape)}  eff_lr mean={eff_lr.mean():.2e}  std={eff_lr.std():.2e}")
            break

```

> **Use AdamW Not Adam for Regularized Training**: Standard Adam with weight_decay adds lambda*theta to the gradient before the adaptive update. The effective decay becomes lambda*alpha/(sqrt(v_hat)+eps) — varying per parameter. Parameters with large gradient history (large v) get weaker regularization. AdamW decouples weight decay: apply theta <- theta*(1-lambda*alpha) directly, before the adaptive gradient step. This gives uniform shrinkage regardless of gradient history. Always use AdamW for regularized training. The difference is significant for large transformer models where gradient magnitudes vary by orders of magnitude across layers.

| Hyperparameter | Default | Effect of Increasing | Effect of Decreasing |
|---|---|---|---|
| alpha (learning rate) | 1e-3 | Faster but less stable | Slower convergence |
| beta1 (momentum) | 0.9 | More momentum, smoother updates | Less momentum, noisier updates |
| beta2 (second moment) | 0.999 | Slower adaptation, more stable v_hat | Faster adaptation, noisier v_hat |
| eps (epsilon) | 1e-8 | More uniform LR (less adaptive) | More adaptive, potential numerical issues |
| weight_decay | 0 (Adam) / 0.01-0.1 (AdamW) | Stronger regularization | Less regularization |

---

## Key Takeaways

- Adam = momentum (first moment) + RMSProp (second moment), with bias correction for both.
- Bias correction is essential: without it, early updates are massively underscaled (10% of intended LR at t=1 with beta1=0.9).
- Adaptive rates help most for sparse gradients (NLP embeddings); for dense vision tasks, SGD is often competitive.
- Adam can fail to converge on convex problems (Reddi 2018); AMSGrad fixes this with a non-decreasing denominator.
- Use AdamW, not Adam, whenever weight decay is needed — standard Adam's L2 is corrupted by adaptive rates.
- Monitor effective LR = alpha/sqrt(v_hat) per layer; if eps dominates (v_hat << eps^2), adaptation is lost.
- Beta2=0.999 requires ~1000 steps to warm up; combine with LR warmup to avoid early instability from unreliable v_hat.

