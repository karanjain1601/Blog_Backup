---
title: "Regularisation — L1, L2, and ElasticNet"
slug: "regularization-l1-l2-elasticnet"
description: "Understand Ridge (L2), LASSO (L1), and ElasticNet regularisation from geometric, optimisation, and Bayesian perspectives — including why L1 produces exact zeros while L2 does not, and when ElasticNet is preferred."
tags: ["supervised-learning", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmVndWxhcmlzYXRpb24gbW9kaWZpZXMgdGhlIGxvc3MgZnVuY3Rpb24gdG8gcGVuYWxpc2UgbW9kZWwgY29tcGxleGl0eSwgdHJhZGluZyBoaWdoZXIgYmlhcyBmb3IgbG93ZXIgdmFyaWFuY2UuIFRoZSB0d28gbW9zdCBjb21tb24gcGVuYWx0aWVzIGluIGxpbmVhciBtb2RlbHMgYXJlIEwyIChSaWRnZSkgYW5kIEwxIChMQVNTTyksIGVhY2ggd2l0aCBkaXN0aW5jdCBnZW9tZXRyaWMsIG9wdGltaXNhdGlvbiwgYW5kIEJheWVzaWFuIGludGVycHJldGF0aW9ucy4gRWxhc3RpY05ldCBjb21iaW5lcyB0aGVtIHRvIGdldCB0aGUgYmVuZWZpdHMgb2YgYm90aC4gQ2hvb3NpbmcgdGhlIHJpZ2h0IHBlbmFsdHkgZGVwZW5kcyBvbiB0aGUgc3RydWN0dXJlIG9mIHRoZSBwcm9ibGVtOiBzcGFyc2l0eSBpbiB0aGUgdHJ1ZSBtb2RlbCwgcHJlc2VuY2Ugb2YgY29ycmVsYXRlZCBwcmVkaWN0b3JzLCBhbmQgd2hldGhlciBpbnRlcnByZXRhYmlsaXR5IHJlcXVpcmVzIGV4cGxpY2l0IGZlYXR1cmUgc2VsZWN0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkwyIFJlZ3VsYXJpc2F0aW9uIOKAlCBSaWRnZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUmlkZ2UgcmVncmVzc2lvbiBtaW5pbWlzZXMg4oCWeSDiiJIgWM644oCWwrIgKyDOu+KAls644oCWwrIuIFRoZSB1bmlxdWUgY2xvc2VkLWZvcm0gc29sdXRpb24gzrjMgl9yaWRnZSA9IChY4bWAWCArIM67SSnigbvCuVjhtYB5IHNocmlua3MgYWxsIGNvZWZmaWNpZW50cyBwcm9wb3J0aW9uYWxseSB0b3dhcmQgemVyby4gUmlkZ2UgY2FuIGJlIHdyaXR0ZW4gYXMgYSBjb25zdHJhaW5lZCBwcm9ibGVtOiBtaW5pbWlzZSDigJZ5IOKIkiBYzrjigJbCsiBzdWJqZWN0IHRvIOKAls644oCWwrIg4omkIHQgKHRoZSBMMiBiYWxsIOKAlCBhIHNwaGVyZSBpbiDihJ3htZYpLiBUaGUgU1ZEIG9mIFggPSBVzqNW4bWAIGdpdmVzIM64zIJfcmlkZ2UgPSBWKM6jwrIgKyDOu0kp4oG7wrnOo1XhtYB5IOKAlCBzbWFsbCBzaW5ndWxhciB2YWx1ZXMgYXJlIHNocnVuayBtb3N0IGFnZ3Jlc3NpdmVseS4gQmF5ZXNpYW4gaW50ZXJwcmV0YXRpb246IM64IH4gTigwLCDPg8KyL867IMK3IEkpIOKGkiBNQVAgPSBSaWRnZSBzb2x1dGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMMSBSZWd1bGFyaXNhdGlvbiDigJQgTEFTU08ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxBU1NPIChMZWFzdCBBYnNvbHV0ZSBTaHJpbmthZ2UgYW5kIFNlbGVjdGlvbiBPcGVyYXRvcikgbWluaW1pc2VzIOKAlnkg4oiSIFjOuOKAlsKyICsgzrvigJbOuOKAluKCgS4gVGhlIEwxIHBlbmFsdHkg4oCWzrjigJbigoEgPSDOo3zOuOKxvHwgaXMgbm90IGRpZmZlcmVudGlhYmxlIGF0IHplcm8sIHNvIHRoZXJlIGlzIG5vIGNsb3NlZCBmb3JtIChleGNlcHQgZm9yIHRoZSBvcnRob2dvbmFsIGRlc2lnbiBjYXNlKS4gVGhlIGtleSBnZW9tZXRyaWMgcHJvcGVydHk6IHRoZSBMMSBiYWxsIGlzIGEgZGlhbW9uZCAocG9seXRvcGUpIHdpdGggY29ybmVycyBvbiB0aGUgY29vcmRpbmF0ZSBheGVzLiBUaGUgY29uc3RyYWluZWQgb3B0aW11bSB0eXBpY2FsbHkgbGFuZHMgb24gYSBjb3JuZXIsIHNldHRpbmcgc29tZSBjb2VmZmljaWVudHMgZXhhY3RseSB0byB6ZXJvIOKAlCBwcm9kdWNpbmcgc3BhcnNlIHNvbHV0aW9ucy4gRm9yIG9ydGhvZ29uYWwgWCwgdGhlIExBU1NPIHNvbHV0aW9uIGlzIHNvZnQtdGhyZXNob2xkaW5nOiDOuMyCX0xBU1NPLGogPSBzaWduKM64zIJfT0xTLGopIMK3IG1heCh8zrjMgl9PTFMsanwg4oiSIM67LzIsIDApLiBCYXllc2lhbiBpbnRlcnByZXRhdGlvbjogzrggfiBMYXBsYWNlKDAsIDEvzrspIOKGkiBNQVAgPSBMQVNTTyBzb2x1dGlvbi4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6InRpcCIsInRpdGxlIjoiV2hlbiB0byBDaG9vc2UgTDEgdnMgTDIiLCJjb250ZW50IjoiVXNlIEwxIChMQVNTTykgd2hlbiB5b3UgZXhwZWN0IHRoZSB0cnVlIG1vZGVsIHRvIGJlIHNwYXJzZSDigJQgb25seSBhIGZldyBmZWF0dXJlcyBtYXR0ZXIuIFVzZSBMMiAoUmlkZ2UpIHdoZW4gbW9zdCBmZWF0dXJlcyBjb250cmlidXRlIGFuZCB5b3Ugd2FudCBzdGFiaWxpdHkgdW5kZXIgbXVsdGljb2xsaW5lYXJpdHkuIFVzZSBFbGFzdGljTmV0IHdoZW4gZmVhdHVyZXMgYXJlIGhpZ2hseSBjb3JyZWxhdGVkIGFuZCB5b3Ugd2FudCBncm91cGluZyB3aXRoIHNvbWUgc3BhcnNpdHkuIEFzIGEgZGVmYXVsdCBzdGFydGluZyBwb2ludCwgdHJ5IFJpZGdlIGZpcnN0OyBzd2l0Y2ggdG8gTEFTU08gb3IgRWxhc3RpY05ldCBpZiBmZWF0dXJlIHNlbGVjdGlvbiBpcyBuZWVkZWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWxhc3RpY05ldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWxhc3RpY05ldCBjb21iaW5lcyBMMSBhbmQgTDIgcGVuYWx0aWVzOiBtaW5pbWlzZSDigJZ5IOKIkiBYzrjigJbCsiArIM67W86x4oCWzrjigJbigoEgKyAoMeKIks6xKeKAls644oCWwrJdLiBUaGUgbWl4aW5nIHBhcmFtZXRlciDOsSDiiIggWzAsMV0gY29udHJvbHMgdGhlIGJhbGFuY2U6IM6xPTEgZ2l2ZXMgTEFTU08sIM6xPTAgZ2l2ZXMgUmlkZ2UuIEVsYXN0aWNOZXQgaGFuZGxlcyB0aGUgdHdvIG1haW4gd2Vha25lc3NlcyBvZiBMQVNTTzogKDEpIHdoZW4gcCBcdTAwM2UgbiwgTEFTU08gc2VsZWN0cyBhdCBtb3N0IG4gdmFyaWFibGVzOyBFbGFzdGljTmV0IGNhbiBzZWxlY3QgbW9yZTsgKDIpIHdoZW4gcHJlZGljdG9ycyBhcmUgaGlnaGx5IGNvcnJlbGF0ZWQsIExBU1NPIGFyYml0cmFyaWx5IHBpY2tzIG9uZTsgRWxhc3RpY05ldCB0ZW5kcyB0byBzZWxlY3QgZ3JvdXBzIG9mIGNvcnJlbGF0ZWQgcHJlZGljdG9ycyB0b2dldGhlci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHZW9tZXRyaWMgSW50ZXJwcmV0YXRpb24g4oCUIFdoeSBMMSBTcGFyc2lmaWVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY29uc3RyYWluZWQgZm9ybSBvZiByZWd1bGFyaXNhdGlvbiByZXZlYWxzIHRoZSBnZW9tZXRyeS4gVGhlIHVuY29uc3RyYWluZWQgT0xTIG1pbmltdW0gaXMgYXQgzrjMgl9PTFMuIFdpdGggYW4gTDIgY29uc3RyYWludCwgdGhlIGZlYXNpYmxlIHJlZ2lvbiBpcyBhIHNwaGVyZSDigJQgdGhlIE9MUyBtaW5pbXVtIGlzIHB1bGxlZCBzbW9vdGhseSBvbnRvIHRoZSBzcGhlcmUgYm91bmRhcnksIGFsbW9zdCBuZXZlciBhdCBhIGNvb3JkaW5hdGUgYXhpcy4gV2l0aCBhbiBMMSBjb25zdHJhaW50LCB0aGUgZmVhc2libGUgcmVnaW9uIGlzIGEgZGlhbW9uZCBwb2x5dG9wZSDigJQgaXRzIGNvcm5lcnMgYXJlIG9uIHRoZSBjb29yZGluYXRlIGF4ZXMuIFRoZSBmaXJzdCBjb250YWN0IGJldHdlZW4gdGhlIGVsbGlwdGljYWwgT0xTIGNvbnRvdXJzIGFuZCB0aGUgTDEgYmFsbCBpcyBtb3N0IGxpa2VseSBhdCBhIGNvcm5lciwgc2V0dGluZyBvbmUgb3IgbW9yZSBjb2VmZmljaWVudHMgZXhhY3RseSB0byB6ZXJvLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlLCBMYXNzbywgRWxhc3RpY05ldFxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX3JlZ3Jlc3Npb25cbmZyb20gc2tsZWFybi5wcmVwcm9jZXNzaW5nIGltcG9ydCBTdGFuZGFyZFNjYWxlclxuXG5ucC5yYW5kb20uc2VlZCg0MilcblgsIHkgPSBtYWtlX3JlZ3Jlc3Npb24obl9zYW1wbGVzPTE1MCwgbl9mZWF0dXJlcz0yMCwgbl9pbmZvcm1hdGl2ZT01LFxuICAgICAgICAgICAgICAgICAgICAgICAgbm9pc2U9MTAuMCwgcmFuZG9tX3N0YXRlPTQyKVxuc2NhbGVyID0gU3RhbmRhcmRTY2FsZXIoKVxuWF9zID0gc2NhbGVyLmZpdF90cmFuc2Zvcm0oWClcblxubGFtID0gMS4wXG5yaWRnZSA9IFJpZGdlKGFscGhhPWxhbSkuZml0KFhfcywgeSlcbmxhc3NvID0gTGFzc28oYWxwaGE9bGFtLCBtYXhfaXRlcj0xMDAwMCkuZml0KFhfcywgeSlcbmVuZXQgID0gRWxhc3RpY05ldChhbHBoYT1sYW0sIGwxX3JhdGlvPTAuNSwgbWF4X2l0ZXI9MTAwMDApLmZpdChYX3MsIHkpXG5cbnByaW50KGZcdTAwMjdSaWRnZTogeyhucC5hYnMocmlkZ2UuY29lZl8pIFx1MDAzYyAxZS02KS5zdW0oKX0gZXhhY3QgemVyb3Mgb3V0IG9mIDIwXHUwMDI3KVxucHJpbnQoZlx1MDAyN0xBU1NPOiB7KG5wLmFicyhsYXNzby5jb2VmXykgXHUwMDNjIDFlLTYpLnN1bSgpfSBleGFjdCB6ZXJvcyBvdXQgb2YgMjBcdTAwMjcpXG5wcmludChmXHUwMDI3RWxOZXQ6IHsobnAuYWJzKGVuZXQuY29lZl8pICBcdTAwM2MgMWUtNikuc3VtKCl9IGV4YWN0IHplcm9zIG91dCBvZiAyMFx1MDAyNylcblxucHJpbnQoZlx1MDAyN1xcblJpZGdlIGNvZWYgbm9ybToge25wLmxpbmFsZy5ub3JtKHJpZGdlLmNvZWZfKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0xBU1NPIGNvZWYgbm9ybToge25wLmxpbmFsZy5ub3JtKGxhc3NvLmNvZWZfKTouM2Z9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0VsTmV0ICBjb2VmIG5vcm06IHtucC5saW5hbGcubm9ybShlbmV0LmNvZWZfKTouM2Z9XHUwMDI3KVxuXG4jIFZlcmlmeTogTEFTU08gemVyb3MgbWF0Y2ggbG93LWluZm9ybWF0aW9uIGZlYXR1cmVzXG5wcmludChmXHUwMDI3XFxuTEFTU08gbm9uemVybyBpbmRpY2VzOiB7bnAud2hlcmUobnAuYWJzKGxhc3NvLmNvZWZfKSBcdTAwM2UgMWUtNilbMF0udG9saXN0KCl9XHUwMDI3KSJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gc2tsZWFybi5saW5lYXJfbW9kZWwgaW1wb3J0IFJpZGdlQ1YsIExhc3NvQ1ZcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9yZWdyZXNzaW9uXG5mcm9tIHNrbGVhcm4ucHJlcHJvY2Vzc2luZyBpbXBvcnQgU3RhbmRhcmRTY2FsZXJcblxuIyBSaWRnZSB1c2VzIFNWRCBzaHJpbmthZ2U6IHRoZXRhX3JpZGdlID0gViBkaWFnKHNeMi8oc14yK2xhbSkpIGRpYWcoMS9zKSBVXlQgeVxubnAucmFuZG9tLnNlZWQoNDIpXG5YLCB5ID0gbWFrZV9yZWdyZXNzaW9uKG5fc2FtcGxlcz0yMDAsIG5fZmVhdHVyZXM9MTUsIG5faW5mb3JtYXRpdmU9NSxcbiAgICAgICAgICAgICAgICAgICAgICAgIG5vaXNlPTEwLjAsIHJhbmRvbV9zdGF0ZT00MilcblhfcyA9IFN0YW5kYXJkU2NhbGVyKCkuZml0X3RyYW5zZm9ybShYKVxuXG5VLCBzLCBWdCA9IG5wLmxpbmFsZy5zdmQoWF9zLCBmdWxsX21hdHJpY2VzPUZhbHNlKVxucHJpbnQoXHUwMDI3U2luZ3VsYXIgdmFsdWVzIG9mIFhfczpcdTAwMjcsIG5wLnJvdW5kKHMsIDIpKVxucHJpbnQoXHUwMDI3UmlkZ2Ugc2hyaW5rYWdlIGZhY3RvcnMgc14yLyhzXjIrbGFtKTpcdTAwMjcpXG5mb3IgbGFtIGluIFswLjEsIDEuMCwgMTAuMCwgMTAwLjBdOlxuICAgIGZhY3RvcnMgPSBzKioyIC8gKHMqKjIgKyBsYW0pXG4gICAgcHJpbnQoZlx1MDAyNyAgbGFtYmRhPXtsYW06XHUwMDNlNi4xZn06IG1pbj17ZmFjdG9ycy5taW4oKTouM2Z9LCBtYXg9e2ZhY3RvcnMubWF4KCk6LjNmfVx1MDAyNylcblxuIyBTb2Z0LXRocmVzaG9sZGluZyBjbG9zZWQgZm9ybSBmb3Igb3J0aG9nb25hbCBkZXNpZ25cbnJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZSg5OSlcblhfb3J0aCwgXyA9IG5wLmxpbmFsZy5xcihybmcucmFuZG4oMjAwLCA4KSlcblhfb3J0aCAqPSBucC5zcXJ0KDIwMClcbnRydWVfY29lZiA9IG5wLmFycmF5KFszLjAsIDAuMCwgMi4wLCAwLjAsIC0xLjUsIDAuMCwgMC4wLCAwLjhdKVxueV9vcnRoID0gWF9vcnRoIEAgdHJ1ZV9jb2VmICsgMC4zICogcm5nLnJhbmRuKDIwMClcbnRoZXRhX29sc19vcnRoID0gKFhfb3J0aC5UIEAgeV9vcnRoKSAvIDIwMC4wXG5sYW1fc3QgPSAwLjVcbnRoZXRhX2xhc3NvX29ydGggPSBucC5zaWduKHRoZXRhX29sc19vcnRoKSAqIG5wLm1heGltdW0obnAuYWJzKHRoZXRhX29sc19vcnRoKSAtIGxhbV9zdCwgMC4wKVxucHJpbnQoZlx1MDAyN1xcbk9ydGhvZ29uYWwgTEFTU08gKGxhbT17bGFtX3N0fSk6IHtucC5yb3VuZCh0aGV0YV9sYXNzb19vcnRoLCAzKX1cdTAwMjcpXG5wcmludChmXHUwMDI3VHJ1ZSBjb2VmczogICAgICAgICAgICAgICAgICAgICAgIHt0cnVlX2NvZWZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJheWVzaWFuIEludGVycHJldGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCb3RoIFJpZGdlIGFuZCBMQVNTTyBoYXZlIGVsZWdhbnQgQmF5ZXNpYW4gaW50ZXJwcmV0YXRpb25zLiBBc3N1bWluZyB5fFgszrggfiBOKFjOuCwgz4PCskkpLCB0aGUgTUFQIGVzdGltYXRlIHVuZGVyIGEgcHJpb3IgzrggfiBOKDAsIM+EwrJJKSBnaXZlcyB0aGUgUmlkZ2Ugc29sdXRpb24gd2l0aCDOuyA9IM+DwrIvz4TCsi4gVGhlIE1BUCBlc3RpbWF0ZSB1bmRlciDOuCB+IExhcGxhY2UoMCwgYsK3SSkgZ2l2ZXMgdGhlIExBU1NPIHNvbHV0aW9uIHdpdGggzrsgPSDPg8KyLygyYikuIFRoZSBMYXBsYWNlIHByaW9yIGhhcyBoZWF2aWVyIHRhaWxzIHRoYW4gR2F1c3NpYW4gYW5kIGEgc2hhcnBlciBwZWFrIGF0IHplcm8g4oCUIGl0IFx1MDAyN2JlbGlldmVzXHUwMDI3IGNvZWZmaWNpZW50cyBhcmUgZWl0aGVyIHplcm8gb3IgbGFyZ2UsIHdoaWNoIHByb21vdGVzIHNwYXJzaXR5LiBUaGUgcG9zdGVyaW9yIG1lYW4gdW5kZXIgTGFwbGFjZSBwcmlvciBpcyBub3QgdGhlIExBU1NPIHNvbHV0aW9uIChvbmx5IE1BUCBpcykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBza2xlYXJuLmxpbmVhcl9tb2RlbCBpbXBvcnQgUmlkZ2UsIExhc3NvXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfcmVncmVzc2lvblxuZnJvbSBza2xlYXJuLnByZXByb2Nlc3NpbmcgaW1wb3J0IFN0YW5kYXJkU2NhbGVyXG5cbiMgU2ltdWxhdGUgY29ycmVsYXRlZCBmZWF0dXJlcyB0byBzaG93IEVsYXN0aWNOZXQgZ3JvdXBpbmdcbm5wLnJhbmRvbS5zZWVkKDcpXG5uID0gMjAwXG5aID0gbnAucmFuZG9tLnJhbmRuKG4sIDMpICAgIyBsYXRlbnQgZmFjdG9yc1xuWF9jb3JyID0gbnAuY29sdW1uX3N0YWNrKFtcbiAgICBaWzosIDBdICsgMC4xICogbnAucmFuZG9tLnJhbmRuKG4pLFxuICAgIFpbOiwgMF0gKyAwLjEgKiBucC5yYW5kb20ucmFuZG4obiksICAgIyBoaWdobHkgY29ycmVsYXRlZCB3aXRoIGNvbCAwXG4gICAgWls6LCAwXSArIDAuMSAqIG5wLnJhbmRvbS5yYW5kbihuKSwgICAjIGhpZ2hseSBjb3JyZWxhdGVkIHdpdGggY29sIDBcbiAgICBaWzosIDFdICsgMC4xICogbnAucmFuZG9tLnJhbmRuKG4pLFxuICAgIFpbOiwgMl0gKyAwLjEgKiBucC5yYW5kb20ucmFuZG4obiksXG5dKVxueV9jb3JyID0gMipaWzosIDBdICsgMS41KlpbOiwgMV0gLSBaWzosIDJdICsgMC4zKm5wLnJhbmRvbS5yYW5kbihuKVxuXG5mcm9tIHNrbGVhcm4ubGluZWFyX21vZGVsIGltcG9ydCBFbGFzdGljTmV0XG5mb3IgbmFtZSwgbW9kZWwgaW4gWyhcdTAwMjdSaWRnZSAgIFx1MDAyNywgUmlkZ2UoYWxwaGE9MS4wKSksXG4gICAgICAgICAgICAgICAgICAgICAoXHUwMDI3TEFTU08gICBcdTAwMjcsIExhc3NvKGFscGhhPTAuNSwgbWF4X2l0ZXI9MTAwMDApKSxcbiAgICAgICAgICAgICAgICAgICAgIChcdTAwMjdFbGFzdGljTmV0XHUwMDI3LCBFbGFzdGljTmV0KGFscGhhPTAuNSwgbDFfcmF0aW89MC41LCBtYXhfaXRlcj0xMDAwMCkpXTpcbiAgICBtb2RlbC5maXQoWF9jb3JyLCB5X2NvcnIpXG4gICAgcHJpbnQoZlx1MDAyN3tuYW1lfTogY29lZnMgPSB7bnAucm91bmQobW9kZWwuY29lZl8sIDMpfVx1MDAyNykifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbiMgQmF5ZXNpYW4gc2FtcGxpbmc6IEdhdXNzaWFuIHByaW9yIC1cdTAwM2UgUmlkZ2Ugc2hyaW5rYWdlXG4jIExhcGxhY2UgcHJpb3IgLVx1MDAzZSBMQVNTTy1saWtlIHNwYXJzZSBzaHJpbmthZ2VcbnJuZyA9IG5wLnJhbmRvbS5SYW5kb21TdGF0ZSgwKVxubl9zYW1wbGVzID0gNTAwMFxuXG4jIEdhdXNzaWFuIHByaW9yIHNhbXBsZXNcbmdhdXNzaWFuX3NhbXBsZXMgPSBybmcubm9ybWFsKGxvYz0wLCBzY2FsZT0xLjAsIHNpemU9bl9zYW1wbGVzKVxuIyBMYXBsYWNlIHByaW9yIHNhbXBsZXNcbmxhcGxhY2Vfc2FtcGxlcyA9IHJuZy5sYXBsYWNlKGxvYz0wLCBzY2FsZT0xLjAsIHNpemU9bl9zYW1wbGVzKVxuXG50aHJlc2hvbGRzID0gWzAuNSwgMS4wLCAxLjUsIDIuMF1cbnByaW50KFx1MDAyN0ZyYWN0aW9uIG9mIHxzYW1wbGV8IFx1MDAzYyB0aHJlc2hvbGQgKHNwYXJzaXR5IHByb3h5KTpcdTAwMjcpXG5wcmludChmXHUwMDI3e1wiUHJpb3JcIjpcdTAwM2UxMn0gXHUwMDI3LCBlbmQ9XHUwMDI3XHUwMDI3KVxuZm9yIHQgaW4gdGhyZXNob2xkczpcbiAgICBwcmludChmXHUwMDI3ICB8eHxcdTAwM2N7dH1cdTAwMjcsIGVuZD1cdTAwMjdcdTAwMjcpXG5wcmludCgpXG5mb3IgbmFtZSwgc2FtcGxlcyBpbiBbKFx1MDAyN0dhdXNzaWFuXHUwMDI3LCBnYXVzc2lhbl9zYW1wbGVzKSwgKFx1MDAyN0xhcGxhY2VcdTAwMjcsIGxhcGxhY2Vfc2FtcGxlcyldOlxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2UxMn0gXHUwMDI3LCBlbmQ9XHUwMDI3XHUwMDI3KVxuICAgIGZvciB0IGluIHRocmVzaG9sZHM6XG4gICAgICAgIGZyYWMgPSBucC5tZWFuKG5wLmFicyhzYW1wbGVzKSBcdTAwM2MgdClcbiAgICAgICAgcHJpbnQoZlx1MDAyNyAge2ZyYWM6LjNmfSAgXHUwMDI3LCBlbmQ9XHUwMDI3XHUwMDI3KVxuICAgIHByaW50KClcbnByaW50KFx1MDAyN1xcbkxhcGxhY2UgY29uY2VudHJhdGVzIG1vcmUgbWFzcyBuZWFyIHplcm8gLVx1MDAzZSBzcGFyc2l0eS1pbmR1Y2luZyBwcmlvci5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaXNvbiBUYWJsZSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJQcm9wZXJ0eSIsIkwyIFJpZGdlIiwiTDEgTEFTU08iLCJFbGFzdGljTmV0Il0sInJvd3MiOltbIlBlbmFsdHkgdGVybSIsIs674oCWzrjigJbCsiIsIs674oCWzrjigJbigoEiLCLOu1vOseKAls644oCW4oKBICsgKDHiiJLOsSnigJbOuOKAlsKyXSJdLFsiQ2xvc2VkIGZvcm0iLCJZZXMg4oCUIChY4bWAWCvOu0kp4oG7wrlY4bWAeSIsIk5vIOKAlCBub24tc21vb3RoIGF0IDAiLCJObyDigJQgbm9uLXNtb290aCJdLFsiRXhhY3Qgc3BhcnNpdHkiLCJObyAoc2hyaW5rcyDiiaAgMCkiLCJZZXMiLCJZZXMgKHBhcnRpYWwpIl0sWyJDb3JyZWxhdGVkIGZlYXR1cmVzIiwiS2VlcHMgYWxsLCBzaHJpbmtzIGVxdWFsbHkiLCJQaWNrcyBvbmUgYXJiaXRyYXJpbHkiLCJUZW5kcyB0byBzZWxlY3QgZ3JvdXBzIl0sWyJNYXggbm9uLXplcm9zIChwXHUwMDNlbikiLCJwIiwi4omkIG4iLCJcdTAwM2UgbiBwb3NzaWJsZSJdLFsiQmF5ZXNpYW4gcHJpb3IiLCJHYXVzc2lhbiBOKDAsIM+DwrIvzrspIiwiTGFwbGFjZSgwLCAxL867KSIsIkNvbWJpbmF0aW9uIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmFjdGljYWwgR3VpZGVsaW5lcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSW4gcHJhY3RpY2UsIGFsd2F5cyBzdGFuZGFyZGlzZSBmZWF0dXJlcyBiZWZvcmUgYXBwbHlpbmcgYW55IHJlZ3VsYXJpc2F0aW9uIOKAlCB0aGUgcGVuYWx0eSB0cmVhdHMgYWxsIGNvZWZmaWNpZW50cyBlcXVhbGx5LCBzbyB1bi1zdGFuZGFyZGlzZWQgZmVhdHVyZXMgd2l0aCBsYXJnZSBtYWduaXR1ZGVzIGFyZSB1bmZhaXJseSBwZW5hbGlzZWQuIFVzZSBjcm9zcy12YWxpZGF0aW9uIHRvIHNlbGVjdCDOuyAoYW5kIM6xIGZvciBFbGFzdGljTmV0KS4gc2tsZWFyblx1MDAyN3MgUmlkZ2VDViwgTGFzc29DViwgYW5kIEVsYXN0aWNOZXRDViBjb21wdXRlIGVmZmljaWVudCBjcm9zcy12YWxpZGF0ZWQgcGF0aHMuIEFzIGEgc3RhcnRpbmcgaGV1cmlzdGljOiBpZiBpbnRlcnByZXRhYmlsaXR5IGFuZCBmZWF0dXJlIHNlbGVjdGlvbiBtYXR0ZXIsIHByZWZlciBMQVNTTzsgaWYgbW9zdCBmZWF0dXJlcyBhcmUgcmVsZXZhbnQgYW5kIHN0YWJpbGl0eSBpcyBwYXJhbW91bnQsIHByZWZlciBSaWRnZTsgaWYgZmVhdHVyZXMgYXJlIGNvcnJlbGF0ZWQsIHVzZSBFbGFzdGljTmV0LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQWx3YXlzIHN0YW5kYXJkaXNlICh6ZXJvIG1lYW4sIHVuaXQgdmFyaWFuY2UpIGZlYXR1cmVzIGJlZm9yZSBhcHBseWluZyBMMSBvciBMMiBwZW5hbHRpZXMuIiwiVXNlIFJpZGdlQ1YsIExhc3NvQ1YsIEVsYXN0aWNOZXRDViBmb3IgZWZmaWNpZW50IGNyb3NzLXZhbGlkYXRlZCDOuyBzZWxlY3Rpb24uIiwiTEFTU08gbWF5IG5vdCBjb252ZXJnZSBmb3IgdmVyeSBsYXJnZSBwIOKAlCBpbmNyZWFzZSBtYXhfaXRlciBhbmQgdXNlIHRoZSBcdTAwMjdzYWdhXHUwMDI3IHNvbHZlci4iLCJGb3IgZmVhdHVyZSBzZWxlY3Rpb24sIGV4YW1pbmUgdGhlIExBU1NPIHBhdGg6IGZlYXR1cmVzIGVudGVyaW5nIGVhcmx5IChzbWFsbCDOuykgYXJlIG1vcmUgaW1wb3J0YW50LiIsIkVsYXN0aWNOZXQgd2l0aCBsMV9yYXRpbz0wLjUgaXMgYSBnb29kIGRlZmF1bHQgd2hlbiB5b3UgZXhwZWN0IHNvbWUgY29ycmVsYXRlZCBncm91cHMuIiwiRm9yIHAgXHUwMDNlXHUwMDNlIG4gKGdlbm9taWNzLCB0ZXh0KSwgcHJlZmVyIEVsYXN0aWNOZXQgb3ZlciBwdXJlIExBU1NPIHRvIGF2b2lkIHRoZSBuLXZhcmlhYmxlIGxpbWl0LiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Regularisation — L1, L2, and ElasticNet

Regularisation modifies the loss function to penalise model complexity, trading higher bias for lower variance. The two most common penalties in linear models are L2 (Ridge) and L1 (LASSO), each with distinct geometric, optimisation, and Bayesian interpretations. ElasticNet combines them to get the benefits of both. Choosing the right penalty depends on the structure of the problem: sparsity in the true model, presence of correlated predictors, and whether interpretability requires explicit feature selection.

## L2 Regularisation — Ridge

Ridge regression minimises ‖y − Xθ‖² + λ‖θ‖². The unique closed-form solution θ̂_ridge = (XᵀX + λI)⁻¹Xᵀy shrinks all coefficients proportionally toward zero. Ridge can be written as a constrained problem: minimise ‖y − Xθ‖² subject to ‖θ‖² ≤ t (the L2 ball — a sphere in ℝᵖ). The SVD of X = UΣVᵀ gives θ̂_ridge = V(Σ² + λI)⁻¹ΣUᵀy — small singular values are shrunk most aggressively. Bayesian interpretation: θ ~ N(0, σ²/λ · I) → MAP = Ridge solution.

## L1 Regularisation — LASSO

LASSO (Least Absolute Shrinkage and Selection Operator) minimises ‖y − Xθ‖² + λ‖θ‖₁. The L1 penalty ‖θ‖₁ = Σ|θⱼ| is not differentiable at zero, so there is no closed form (except for the orthogonal design case). The key geometric property: the L1 ball is a diamond (polytope) with corners on the coordinate axes. The constrained optimum typically lands on a corner, setting some coefficients exactly to zero — producing sparse solutions. For orthogonal X, the LASSO solution is soft-thresholding: θ̂_LASSO,j = sign(θ̂_OLS,j) · max(|θ̂_OLS,j| − λ/2, 0). Bayesian interpretation: θ ~ Laplace(0, 1/λ) → MAP = LASSO solution.

> **When to Choose L1 vs L2**: Use L1 (LASSO) when you expect the true model to be sparse — only a few features matter. Use L2 (Ridge) when most features contribute and you want stability under multicollinearity. Use ElasticNet when features are highly correlated and you want grouping with some sparsity. As a default starting point, try Ridge first; switch to LASSO or ElasticNet if feature selection is needed.

## ElasticNet

ElasticNet combines L1 and L2 penalties: minimise ‖y − Xθ‖² + λ[α‖θ‖₁ + (1−α)‖θ‖²]. The mixing parameter α ∈ [0,1] controls the balance: α=1 gives LASSO, α=0 gives Ridge. ElasticNet handles the two main weaknesses of LASSO: (1) when p > n, LASSO selects at most n variables; ElasticNet can select more; (2) when predictors are highly correlated, LASSO arbitrarily picks one; ElasticNet tends to select groups of correlated predictors together.

## Geometric Interpretation — Why L1 Sparsifies

The constrained form of regularisation reveals the geometry. The unconstrained OLS minimum is at θ̂_OLS. With an L2 constraint, the feasible region is a sphere — the OLS minimum is pulled smoothly onto the sphere boundary, almost never at a coordinate axis. With an L1 constraint, the feasible region is a diamond polytope — its corners are on the coordinate axes. The first contact between the elliptical OLS contours and the L1 ball is most likely at a corner, setting one or more coefficients exactly to zero.

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X, y = make_regression(n_samples=150, n_features=20, n_informative=5,
                        noise=10.0, random_state=42)
scaler = StandardScaler()
X_s = scaler.fit_transform(X)

lam = 1.0
ridge = Ridge(alpha=lam).fit(X_s, y)
lasso = Lasso(alpha=lam, max_iter=10000).fit(X_s, y)
enet  = ElasticNet(alpha=lam, l1_ratio=0.5, max_iter=10000).fit(X_s, y)

print(f'Ridge: {(np.abs(ridge.coef_) < 1e-6).sum()} exact zeros out of 20')
print(f'LASSO: {(np.abs(lasso.coef_) < 1e-6).sum()} exact zeros out of 20')
print(f'ElNet: {(np.abs(enet.coef_)  < 1e-6).sum()} exact zeros out of 20')

print(f'\nRidge coef norm: {np.linalg.norm(ridge.coef_):.3f}')
print(f'LASSO coef norm: {np.linalg.norm(lasso.coef_):.3f}')
print(f'ElNet  coef norm: {np.linalg.norm(enet.coef_):.3f}')

# Verify: LASSO zeros match low-information features
print(f'\nLASSO nonzero indices: {np.where(np.abs(lasso.coef_) > 1e-6)[0].tolist()}')
```

```python
import numpy as np
from sklearn.linear_model import RidgeCV, LassoCV
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

# Ridge uses SVD shrinkage: theta_ridge = V diag(s^2/(s^2+lam)) diag(1/s) U^T y
np.random.seed(42)
X, y = make_regression(n_samples=200, n_features=15, n_informative=5,
                        noise=10.0, random_state=42)
X_s = StandardScaler().fit_transform(X)

U, s, Vt = np.linalg.svd(X_s, full_matrices=False)
print('Singular values of X_s:', np.round(s, 2))
print('Ridge shrinkage factors s^2/(s^2+lam):')
for lam in [0.1, 1.0, 10.0, 100.0]:
    factors = s**2 / (s**2 + lam)
    print(f'  lambda={lam:>6.1f}: min={factors.min():.3f}, max={factors.max():.3f}')

# Soft-thresholding closed form for orthogonal design
rng = np.random.RandomState(99)
X_orth, _ = np.linalg.qr(rng.randn(200, 8))
X_orth *= np.sqrt(200)
true_coef = np.array([3.0, 0.0, 2.0, 0.0, -1.5, 0.0, 0.0, 0.8])
y_orth = X_orth @ true_coef + 0.3 * rng.randn(200)
theta_ols_orth = (X_orth.T @ y_orth) / 200.0
lam_st = 0.5
theta_lasso_orth = np.sign(theta_ols_orth) * np.maximum(np.abs(theta_ols_orth) - lam_st, 0.0)
print(f'\nOrthogonal LASSO (lam={lam_st}): {np.round(theta_lasso_orth, 3)}')
print(f'True coefs:                       {true_coef}')
```

## Bayesian Interpretation

Both Ridge and LASSO have elegant Bayesian interpretations. Assuming y|X,θ ~ N(Xθ, σ²I), the MAP estimate under a prior θ ~ N(0, τ²I) gives the Ridge solution with λ = σ²/τ². The MAP estimate under θ ~ Laplace(0, b·I) gives the LASSO solution with λ = σ²/(2b). The Laplace prior has heavier tails than Gaussian and a sharper peak at zero — it 'believes' coefficients are either zero or large, which promotes sparsity. The posterior mean under Laplace prior is not the LASSO solution (only MAP is).

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

# Simulate correlated features to show ElasticNet grouping
np.random.seed(7)
n = 200
Z = np.random.randn(n, 3)   # latent factors
X_corr = np.column_stack([
    Z[:, 0] + 0.1 * np.random.randn(n),
    Z[:, 0] + 0.1 * np.random.randn(n),   # highly correlated with col 0
    Z[:, 0] + 0.1 * np.random.randn(n),   # highly correlated with col 0
    Z[:, 1] + 0.1 * np.random.randn(n),
    Z[:, 2] + 0.1 * np.random.randn(n),
])
y_corr = 2*Z[:, 0] + 1.5*Z[:, 1] - Z[:, 2] + 0.3*np.random.randn(n)

from sklearn.linear_model import ElasticNet
for name, model in [('Ridge   ', Ridge(alpha=1.0)),
                     ('LASSO   ', Lasso(alpha=0.5, max_iter=10000)),
                     ('ElasticNet', ElasticNet(alpha=0.5, l1_ratio=0.5, max_iter=10000))]:
    model.fit(X_corr, y_corr)
    print(f'{name}: coefs = {np.round(model.coef_, 3)}')
```

```python
import numpy as np

# Bayesian sampling: Gaussian prior -> Ridge shrinkage
# Laplace prior -> LASSO-like sparse shrinkage
rng = np.random.RandomState(0)
n_samples = 5000

# Gaussian prior samples
gaussian_samples = rng.normal(loc=0, scale=1.0, size=n_samples)
# Laplace prior samples
laplace_samples = rng.laplace(loc=0, scale=1.0, size=n_samples)

thresholds = [0.5, 1.0, 1.5, 2.0]
print('Fraction of |sample| < threshold (sparsity proxy):')
print(f'{"Prior":>12} ', end='')
for t in thresholds:
    print(f'  |x|<{t}', end='')
print()
for name, samples in [('Gaussian', gaussian_samples), ('Laplace', laplace_samples)]:
    print(f'{name:>12} ', end='')
    for t in thresholds:
        frac = np.mean(np.abs(samples) < t)
        print(f'  {frac:.3f}  ', end='')
    print()
print('\nLaplace concentrates more mass near zero -> sparsity-inducing prior.')
```

## Comparison Table

| Property | L2 Ridge | L1 LASSO | ElasticNet |
| --- | --- | --- | --- |
| Penalty term | λ‖θ‖² | λ‖θ‖₁ | λ[α‖θ‖₁ + (1−α)‖θ‖²] |
| Closed form | Yes — (XᵀX+λI)⁻¹Xᵀy | No — non-smooth at 0 | No — non-smooth |
| Exact sparsity | No (shrinks ≠ 0) | Yes | Yes (partial) |
| Correlated features | Keeps all, shrinks equally | Picks one arbitrarily | Tends to select groups |
| Max non-zeros (p>n) | p | ≤ n | > n possible |
| Bayesian prior | Gaussian N(0, σ²/λ) | Laplace(0, 1/λ) | Combination |

## Practical Guidelines

In practice, always standardise features before applying any regularisation — the penalty treats all coefficients equally, so un-standardised features with large magnitudes are unfairly penalised. Use cross-validation to select λ (and α for ElasticNet). sklearn's RidgeCV, LassoCV, and ElasticNetCV compute efficient cross-validated paths. As a starting heuristic: if interpretability and feature selection matter, prefer LASSO; if most features are relevant and stability is paramount, prefer Ridge; if features are correlated, use ElasticNet.

- Always standardise (zero mean, unit variance) features before applying L1 or L2 penalties.
- Use RidgeCV, LassoCV, ElasticNetCV for efficient cross-validated λ selection.
- LASSO may not converge for very large p — increase max_iter and use the 'saga' solver.
- For feature selection, examine the LASSO path: features entering early (small λ) are more important.
- ElasticNet with l1_ratio=0.5 is a good default when you expect some correlated groups.
- For p >> n (genomics, text), prefer ElasticNet over pure LASSO to avoid the n-variable limit.

---

