---
title: "RLAIF — AI Feedback for Scalable Supervision Without Human Annotators"
slug: "rlaif"
description: "RLAIF (Lee et al., 2023, Google) replaces human preference annotators with a strong teacher LLM to generate preference labels for reward model training, enabling scalable RLHF-equivalent alignment at a fraction of the annotation cost, with debiasing techniques to correct position and verbosity biases in AI judges."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUkxBSUYgKFJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBBSSBGZWVkYmFjaywgTGVlIGV0IGFsLiAyMDIzLCBHb29nbGUpIHJlcGxhY2VzIHRoZSBodW1hbiBwcmVmZXJlbmNlIGxhYmVsZXJzIGluIHN0YW5kYXJkIFJMSEYgd2l0aCBhIHN0cm9uZyB0ZWFjaGVyIExMTSDigJQgc3VjaCBhcyBHUFQtNCwgQ2xhdWRlIDMgT3B1cywgb3IgR2VtaW5pIFVsdHJhIOKAlCB0byBnZW5lcmF0ZSBwcmVmZXJlbmNlIGxhYmVscyBhdCBzY2FsZS4gVGhlIHBpcGVsaW5lIG1pcnJvcnMgUkxIRiBleGFjdGx5OiBzYW1wbGUgdHdvIHJlc3BvbnNlcyBmcm9tIHRoZSBwb2xpY3ksIHByb21wdCB0aGUgdGVhY2hlciB0byBqdWRnZSB3aGljaCBpcyBwcmVmZXJyZWQgYW5kIHdoeSwgdXNlIHRob3NlIEFJIGxhYmVscyB0byB0cmFpbiBhIHJld2FyZCBtb2RlbCAoUk0pLCBhbmQgcnVuIFBQTyB3aXRoIHRoZSBSTS4gTGVlIGV0IGFsLiBmb3VuZCB0aGF0IFJMQUlGLXRyYWluZWQgbW9kZWxzIGFjaGlldmUgY29tcGFyYWJsZSBwZXJmb3JtYW5jZSB0byBodW1hbiBSTEhGIG1vZGVscyBvbiBzdW1tYXJpc2F0aW9uIGJlbmNobWFya3Mgd2hpbGUgcmVkdWNpbmcgYW5ub3RhdGlvbiBjb3N0IGJ5IG9yZGVycyBvZiBtYWduaXR1ZGUuIFRoZSBrZXkgcmVxdWlyZW1lbnQgaXMgdGhhdCB0aGUgdGVhY2hlciBtb2RlbCBiZSBzdWJzdGFudGlhbGx5IGJldHRlciB0aGFuIHRoZSBwb2xpY3kgYmVpbmcgdHJhaW5lZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSTEFJRiBQaXBlbGluZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFJMQUlGIHBpcGVsaW5lIGhhcyBmaXZlIHN0YWdlczogKDEpIENvbGxlY3QgcHJvbXB0cyBmcm9tIGEgZGF0YXNldCBvciB1c2VyIGxvZ3MuICgyKSBTYW1wbGUgdHdvIGNhbmRpZGF0ZSByZXNwb25zZXMgeeKCgSBhbmQgeeKCgiBmcm9tIHRoZSBjdXJyZW50IHBvbGljeSBmb3IgZWFjaCBwcm9tcHQuICgzKSBTdWJtaXQgdGhlIHByb21wdCBhbmQgYm90aCByZXNwb25zZXMgdG8gdGhlIHRlYWNoZXIgTExNIHdpdGggYSBzdHJ1Y3R1cmVkIGV2YWx1YXRpb24gcHJvbXB0IGFza2luZyBmb3IgYSBwcmVmZXJlbmNlIGp1ZGdtZW50IGFuZCByZWFzb25pbmcuICg0KSBDb2xsZWN0IHRoZSB0ZWFjaGVyXHUwMDI3cyBsYWJlbCAocHJlZmVycmVkIHJlc3BvbnNlKSBhbmQgdXNlIGl0IGFzIGEgdHJhaW5pbmcgc2lnbmFsIHRvIGZpbmUtdHVuZSB0aGUgcmV3YXJkIG1vZGVsIHZpYSBCcmFkbGV5LVRlcnJ5IGxvc3MuICg1KSBSdW4gUFBPIHdpdGggdGhlIHRyYWluZWQgUk0gdG8gdXBkYXRlIHRoZSBwb2xpY3kuIFRoZSB0ZWFjaGVyIG1vZGVsIGlzIGNhbGxlZCBvbmx5IGR1cmluZyBSTSB0cmFpbmluZywgbm90IGR1cmluZyBQUE87IHRoaXMga2VlcHMgaW5mZXJlbmNlIGNvc3RzIGJvdW5kZWQgZXZlbiBhcyB0aGUgcG9saWN5IGltcHJvdmVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZWZlcmVuY2UgTGFiZWxpbmcgd2l0aCBUZWFjaGVyIExMTSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHRlYWNoZXIgTExNIGlzIHByb21wdGVkIHdpdGggdGhlIG9yaWdpbmFsIHVzZXIgcXVlcnkgYW5kIGJvdGggY2FuZGlkYXRlIHJlc3BvbnNlcywgdGhlbiBhc2tlZCB0byBwcm92aWRlIGEgcHJlZmVyZW5jZSBqdWRnbWVudCB3aXRoIGNoYWluLW9mLXRob3VnaHQgcmVhc29uaW5nLiBUaGUgcmVhc29uaW5nIHN0ZXAgaXMgaW1wb3J0YW50OiBpdCBmb3JjZXMgdGhlIGp1ZGdlIHRvIGFydGljdWxhdGUgd2h5IG9uZSByZXNwb25zZSBpcyBiZXR0ZXIsIHJlZHVjaW5nIG5vaXNlIGFuZCBlbmFibGluZyBwb3N0LWhvYyBhbmFseXNpcyBvZiB0aGUgbGFiZWxpbmcgY3JpdGVyaWEuIFRoZSB0ZWFjaGVyXHUwMDI3cyByZXNwb25zZSBpcyBwYXJzZWQgdG8gZXh0cmFjdCBhIGJpbmFyeSBwcmVmZXJlbmNlIGxhYmVsIChBIG9yIEIpIHdoaWNoIGJlY29tZXMgdGhlIFJNIHRyYWluaW5nIHRhcmdldC4gVGVtcGVyYXR1cmUgMCAoZ3JlZWR5IGRlY29kaW5nKSBvciBsb3cgdGVtcGVyYXR1cmUgKDAuMSkgaXMgdXNlZCBmb3IgcmVwcm9kdWNpYmlsaXR5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgb3BlbmFpXG5pbXBvcnQganNvblxuZnJvbSB0eXBpbmcgaW1wb3J0IFR1cGxlLCBPcHRpb25hbFxuXG5kZWYgcmxhaWZfcHJlZmVyZW5jZV9sYWJlbChcbiAgICBwcm9tcHQ6IHN0cixcbiAgICByZXNwb25zZV9hOiBzdHIsXG4gICAgcmVzcG9uc2VfYjogc3RyLFxuICAgIHRlYWNoZXJfbW9kZWw6IHN0ciA9IFx1MDAyN2dwdC00b1x1MDAyNyxcbiAgICBjcml0ZXJpYTogc3RyID0gXHUwMDI3aGVscGZ1bCwgaGFybWxlc3MsIGFuZCBob25lc3RcdTAwMjcsXG4pIC1cdTAwM2UgVHVwbGVbc3RyLCBzdHIsIGZsb2F0XTpcbiAgICBcIlwiXCJcbiAgICBSTEFJRjogcXVlcnkgdGVhY2hlciBMTE0gZm9yIHByZWZlcmVuY2UgbGFiZWwgYmV0d2VlbiB0d28gcmVzcG9uc2VzLlxuICAgIFJldHVybnMgKHByZWZlcnJlZDogXHUwMDI3QVx1MDAyN3xcdTAwMjdCXHUwMDI3LCByZWFzb25pbmc6IHN0ciwgY29uZmlkZW5jZTogZmxvYXQpLlxuICAgIFwiXCJcIlxuICAgIGNsaWVudCA9IG9wZW5haS5PcGVuQUkoKVxuICAgIHN5c3RlbV9tc2cgPSAoXG4gICAgICAgIFx1MDAyN1lvdSBhcmUgYW4gZXhwZXJ0IGV2YWx1YXRvciBmb3IgQUkgYXNzaXN0YW50IHJlc3BvbnNlcy4gXHUwMDI3XG4gICAgICAgIFx1MDAyN0dpdmVuIGEgdXNlciBxdWVyeSBhbmQgdHdvIGNhbmRpZGF0ZSByZXNwb25zZXMsIHNlbGVjdCB0aGUgYmV0dGVyIG9uZS4gXHUwMDI3XG4gICAgICAgIFx1MDAyN1Jlc3BvbmQgd2l0aCB2YWxpZCBKU09OIG9ubHkuXHUwMDI3XG4gICAgKVxuICAgIHVzZXJfbXNnID0gKFxuICAgICAgICBmXHUwMDI3RXZhbHVhdGUgd2hpY2ggcmVzcG9uc2UgaXMgbW9yZSB7Y3JpdGVyaWF9Llxcblxcblx1MDAyN1xuICAgICAgICBmXHUwMDI3VXNlciBxdWVyeToge3Byb21wdH1cXG5cXG5cdTAwMjdcbiAgICAgICAgZlx1MDAyN1Jlc3BvbnNlIEE6XFxue3Jlc3BvbnNlX2F9XFxuXFxuXHUwMDI3XG4gICAgICAgIGZcdTAwMjdSZXNwb25zZSBCOlxcbntyZXNwb25zZV9ifVxcblxcblx1MDAyN1xuICAgICAgICBmXHUwMDI3UmVzcG9uZCB3aXRoIEpTT046IHt7XHUwMDI3XG4gICAgICAgIGZcdTAwMjdcInByZWZlcnJlZFwiOiBcIkFcIiBvciBcIkJcIiwgXHUwMDI3XG4gICAgICAgIGZcdTAwMjdcInJlYXNvbmluZ1wiOiBcImJyaWVmIGV4cGxhbmF0aW9uXCIsIFx1MDAyN1xuICAgICAgICBmXHUwMDI3XCJjb25maWRlbmNlXCI6IDAuMCB0byAxLjB9fVx1MDAyN1xuICAgIClcbiAgICByZXNwID0gY2xpZW50LmNoYXQuY29tcGxldGlvbnMuY3JlYXRlKFxuICAgICAgICBtb2RlbD10ZWFjaGVyX21vZGVsLFxuICAgICAgICBtZXNzYWdlcz1bXG4gICAgICAgICAgICB7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3c3lzdGVtXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBzeXN0ZW1fbXNnfSxcbiAgICAgICAgICAgIHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCAgIFx1MDAyN2NvbnRlbnRcdTAwMjc6IHVzZXJfbXNnfSxcbiAgICAgICAgXSxcbiAgICAgICAgdGVtcGVyYXR1cmU9MC4wLFxuICAgICAgICByZXNwb25zZV9mb3JtYXQ9e1x1MDAyN3R5cGVcdTAwMjc6IFx1MDAyN2pzb25fb2JqZWN0XHUwMDI3fSxcbiAgICApLmNob2ljZXNbMF0ubWVzc2FnZS5jb250ZW50XG4gICAgcGFyc2VkID0ganNvbi5sb2FkcyhyZXNwKVxuICAgIHJldHVybiBwYXJzZWRbXHUwMDI3cHJlZmVycmVkXHUwMDI3XSwgcGFyc2VkW1x1MDAyN3JlYXNvbmluZ1x1MDAyN10sIHBhcnNlZC5nZXQoXHUwMDI3Y29uZmlkZW5jZVx1MDAyNywgMS4wKVxuXG4jIEV4YW1wbGUgdXNhZ2VcbnJlc3VsdCA9IHJsYWlmX3ByZWZlcmVuY2VfbGFiZWwoXG4gICAgcHJvbXB0PVx1MDAyN0V4cGxhaW4gd2hhdCBhIHRyYW5zZm9ybWVyIGlzLlx1MDAyNyxcbiAgICByZXNwb25zZV9hPVx1MDAyN0l0IGlzIGEgdHlwZSBvZiBuZXVyYWwgbmV0d29yayB1c2luZyBhdHRlbnRpb24gbWVjaGFuaXNtcy5cdTAwMjcsXG4gICAgcmVzcG9uc2VfYj1cdTAwMjdBIHRyYW5zZm9ybWVyIGlzIGEgbWFjaGluZSBsZWFybmluZyBtb2RlbCBhcmNoaXRlY3R1cmUgaW50cm9kdWNlZCBpbiBcdTAwMjdcbiAgICAgICAgICAgICAgIFx1MDAyN1wiQXR0ZW50aW9uIGlzIEFsbCBZb3UgTmVlZFwiIChWYXN3YW5pIGV0IGFsLiAyMDE3KS5cdTAwMjcsXG4gICAgdGVhY2hlcl9tb2RlbD1cdTAwMjdncHQtNG8tbWluaVx1MDAyNyxcbilcbnByaW50KGZcdTAwMjdQcmVmZXJyZWQ6IHtyZXN1bHRbMF19LCBDb25maWRlbmNlOiB7cmVzdWx0WzJdOi4yZn1cdTAwMjcpXG5wcmludChmXHUwMDI3UmVhc29uaW5nOiB7cmVzdWx0WzFdfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQb3NpdGlvbiBCaWFzIERlYmlhc2luZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQUkganVkZ2VzIGV4aGliaXQgc3lzdGVtYXRpYyBwb3NpdGlvbiBiaWFzOiB0aGV5IHRlbmQgdG8gcHJlZmVyIHdoaWNoZXZlciByZXNwb25zZSBhcHBlYXJzIGZpcnN0IChBKSByZWdhcmRsZXNzIG9mIHF1YWxpdHkuIFZlcmJvc2l0eSBiaWFzIGlzIGVxdWFsbHkgY29tbW9uOiBsb25nZXIgcmVzcG9uc2VzIGFyZSByYXRlZCBoaWdoZXIgZXZlbiB3aGVuIHRoZSBzaG9ydGVyIHJlc3BvbnNlIGlzIG1vcmUgYWNjdXJhdGUgYW5kIGNvbmNpc2UuIFRoZXNlIGJpYXNlcywgaWYgdW5jb3JyZWN0ZWQsIHdpbGwgdHJhaW4gdGhlIHJld2FyZCBtb2RlbCB0byBwcmVmZXIgbG9uZywgZmlyc3QtcG9zaXRpb25lZCByZXNwb25zZXMgYW5kIGNvbnNlcXVlbnRseSB0cmFpbiB0aGUgcG9saWN5IHRvIGdlbmVyYXRlIHZlcmJvc2Ugb3V0cHV0LiBUaGUgc3RhbmRhcmQgZGViaWFzaW5nIHRlY2huaXF1ZSBpcyB0byBxdWVyeSB0aGUganVkZ2UgdHdpY2Ug4oCUIG9uY2Ugd2l0aCBvcmRlciAoQSwgQikgYW5kIG9uY2Ugd2l0aCBvcmRlciAoQiwgQSkg4oCUIGFuZCBhdmVyYWdlIG9yIHRha2UgdGhlIG1ham9yaXR5IHZvdGUgb2YgdGhlIHR3byBqdWRnbWVudHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBvcGVuYWlcbmltcG9ydCBqc29uXG5mcm9tIHR5cGluZyBpbXBvcnQgVHVwbGVcblxuZGVmIGRlYmlhc2VkX3ByZWZlcmVuY2VfbGFiZWwoXG4gICAgcHJvbXB0OiBzdHIsXG4gICAgcmVzcG9uc2VfMTogc3RyLFxuICAgIHJlc3BvbnNlXzI6IHN0cixcbiAgICBqdWRnZV9tb2RlbDogc3RyID0gXHUwMDI3Z3B0LTRvLW1pbmlcdTAwMjcsXG4pIC1cdTAwM2UgVHVwbGVbc3RyLCBmbG9hdF06XG4gICAgXCJcIlwiXG4gICAgUG9zaXRpb24tYmlhcyBkZWJpYXNpbmc6IHF1ZXJ5IGp1ZGdlIHdpdGggYm90aCBvcmRlcmluZ3MgYW5kIGF2ZXJhZ2UuXG4gICAgUmV0dXJucyAocHJlZmVycmVkOiBcdTAwMjcxXHUwMDI3fFx1MDAyNzJcdTAwMjd8XHUwMDI3dGllXHUwMDI3LCBhZ3JlZW1lbnQ6IGZsb2F0KS5cbiAgICBcIlwiXCJcbiAgICBjbGllbnQgPSBvcGVuYWkuT3BlbkFJKClcblxuICAgIGRlZiBqdWRnZV9wYWlyKGZpcnN0OiBzdHIsIHNlY29uZDogc3RyLCBsYWJlbF9maXJzdDogc3RyLCBsYWJlbF9zZWNvbmQ6IHN0cikgLVx1MDAzZSBzdHI6XG4gICAgICAgIG1zZyA9IChcbiAgICAgICAgICAgIGZcdTAwMjdRdWVyeToge3Byb21wdH1cXG5cXG5cdTAwMjdcbiAgICAgICAgICAgIGZcdTAwMjdSZXNwb25zZSB7bGFiZWxfZmlyc3R9OlxcbntmaXJzdH1cXG5cXG5cdTAwMjdcbiAgICAgICAgICAgIGZcdTAwMjdSZXNwb25zZSB7bGFiZWxfc2Vjb25kfTpcXG57c2Vjb25kfVxcblxcblx1MDAyN1xuICAgICAgICAgICAgZlx1MDAyN1doaWNoIGlzIGJldHRlcj8gUmVzcG9uZCB3aXRoIEpTT046IHt7XCJwcmVmZXJyZWRcIjogXCJ7bGFiZWxfZmlyc3R9XCIgb3IgXCJ7bGFiZWxfc2Vjb25kfVwifX1cdTAwMjdcbiAgICAgICAgKVxuICAgICAgICByZXNwID0gY2xpZW50LmNoYXQuY29tcGxldGlvbnMuY3JlYXRlKFxuICAgICAgICAgICAgbW9kZWw9anVkZ2VfbW9kZWwsXG4gICAgICAgICAgICBtZXNzYWdlcz1be1x1MDAyN3JvbGVcdTAwMjc6IFx1MDAyN3VzZXJcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IG1zZ31dLFxuICAgICAgICAgICAgdGVtcGVyYXR1cmU9MC4wLFxuICAgICAgICAgICAgcmVzcG9uc2VfZm9ybWF0PXtcdTAwMjd0eXBlXHUwMDI3OiBcdTAwMjdqc29uX29iamVjdFx1MDAyN30sXG4gICAgICAgICkuY2hvaWNlc1swXS5tZXNzYWdlLmNvbnRlbnRcbiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocmVzcClbXHUwMDI3cHJlZmVycmVkXHUwMDI3XVxuXG4gICAgIyBGb3J3YXJkIG9yZGVyOiAocmVzcG9uc2VfMSBhcyBBLCByZXNwb25zZV8yIGFzIEIpXG4gICAgbGFiZWxfZm9yd2FyZCA9IGp1ZGdlX3BhaXIocmVzcG9uc2VfMSwgcmVzcG9uc2VfMiwgXHUwMDI3QVx1MDAyNywgXHUwMDI3Qlx1MDAyNylcbiAgICBwcmVmZXJzXzFfZm9yd2FyZCA9IGxhYmVsX2ZvcndhcmQgPT0gXHUwMDI3QVx1MDAyN1xuXG4gICAgIyBSZXZlcnNlZCBvcmRlcjogKHJlc3BvbnNlXzIgYXMgQSwgcmVzcG9uc2VfMSBhcyBCKVxuICAgIGxhYmVsX3JldmVyc2UgPSBqdWRnZV9wYWlyKHJlc3BvbnNlXzIsIHJlc3BvbnNlXzEsIFx1MDAyN0FcdTAwMjcsIFx1MDAyN0JcdTAwMjcpXG4gICAgcHJlZmVyc18xX3JldmVyc2UgPSBsYWJlbF9yZXZlcnNlID09IFx1MDAyN0JcdTAwMjcgICMgXHUwMDI3Qlx1MDAyNyBtZWFucyByZXNwb25zZV8xIHByZWZlcnJlZFxuXG4gICAgIyBBZ2dyZWdhdGVcbiAgICBpZiBwcmVmZXJzXzFfZm9yd2FyZCBhbmQgcHJlZmVyc18xX3JldmVyc2U6XG4gICAgICAgIHJldHVybiBcdTAwMjcxXHUwMDI3LCAxLjAgICMgYm90aCBvcmRlcmluZ3MgcHJlZmVyIHJlc3BvbnNlXzFcbiAgICBlbGlmIG5vdCBwcmVmZXJzXzFfZm9yd2FyZCBhbmQgbm90IHByZWZlcnNfMV9yZXZlcnNlOlxuICAgICAgICByZXR1cm4gXHUwMDI3Mlx1MDAyNywgMS4wICAjIGJvdGggb3JkZXJpbmdzIHByZWZlciByZXNwb25zZV8yXG4gICAgZWxzZTpcbiAgICAgICAgcmV0dXJuIFx1MDAyN3RpZVx1MDAyNywgMC41ICAjIGRpc2FncmVlbWVudCDigJQgcG9zaXRpb24gYmlhcyBkZXRlY3RlZFxuXG5wcmVmZXJyZWQsIGNvbmZpZGVuY2UgPSBcdTAwMjcxXHUwMDI3LCAxLjAgICMgc2ltdWxhdGVkIHJlc3VsdFxucHJpbnQoZlx1MDAyN0RlYmlhc2VkIHByZWZlcmVuY2U6IHJlc3BvbnNlIHtwcmVmZXJyZWR9IChjb25maWRlbmNlPXtjb25maWRlbmNlOi4yZn0pXHUwMDI3KVxucHJpbnQoXHUwMDI3VGllIGluZGljYXRlcyBwb3NpdGlvbiBiaWFzIOKAlCBkaXNjYXJkIG9yIHVzZSBhcyBlcXVhbCBwYWlyIGluIFJNIHRyYWluaW5nXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFJIEp1ZGdlIFF1YWxpdHkgRXZhbHVhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVmb3JlIGRlcGxveWluZyBhbiBBSSBqdWRnZSBmb3IgUkxBSUYsIGl0cyBxdWFsaXR5IHNob3VsZCBiZSB2YWxpZGF0ZWQgYWdhaW5zdCBhIGNhbGlicmF0aW9uIHNldCBvZiBodW1hbi1sYWJlbGVkIHByZWZlcmVuY2UgcGFpcnMuIEludGVyLWFubm90YXRvciBhZ3JlZW1lbnQgKENvaGVuXHUwMDI3cyDOuiBvciBLcmlwcGVuZG9yZmZcdTAwMjdzIM6xKSBiZXR3ZWVuIHRoZSBBSSBqdWRnZSBhbmQgaHVtYW4gYW5ub3RhdG9ycyBxdWFudGlmaWVzIGhvdyBjbG9zZWx5IHRoZSBBSSBqdWRnZSB0cmFja3MgaHVtYW4gcHJlZmVyZW5jZXMuIEFuIEFJIGp1ZGdlIHdpdGggzrogXHUwMDNjIDAuNCBzaG91bGQgbm90IGJlIHVzZWQg4oCUIGl0cyBsYWJlbHMgaW50cm9kdWNlIHRvbyBtdWNoIG5vaXNlLiBBZGRpdGlvbmFsbHksIGNvbXB1dGUgcGVyLWNhdGVnb3J5IGFncmVlbWVudCB0byBpZGVudGlmeSBkb21haW5zIHdoZXJlIHRoZSBBSSBqdWRnZSBzeXN0ZW1hdGljYWxseSBkaXNhZ3JlZXMgd2l0aCBodW1hbnMgKGUuZy4sIGN1bHR1cmFsIG51YW5jZSwgaHVtb3VyLCB0ZWNobmljYWwgYWNjdXJhY3kgaW4gbmljaGUgZmllbGRzKS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgY29oZW5fa2FwcGFfc2NvcmUsIGNsYXNzaWZpY2F0aW9uX3JlcG9ydFxuXG5kZWYgZXZhbHVhdGVfYWlfanVkZ2UoXG4gICAgaHVtYW5fbGFiZWxzOiBsaXN0LFxuICAgIGFpX2xhYmVsczogbGlzdCxcbiAgICBjYXRlZ29yeV9sYWJlbHM6IGxpc3QgPSBOb25lLFxuKSAtXHUwMDNlIGRpY3Q6XG4gICAgXCJcIlwiXG4gICAgRXZhbHVhdGUgQUkganVkZ2UgcXVhbGl0eSB2cyBodW1hbiBsYWJlbHMgb24gYSBjYWxpYnJhdGlvbiBzZXQuXG4gICAgTGFiZWxzIHNob3VsZCBiZSAwIChwcmVmZXIgQSkgb3IgMSAocHJlZmVyIEIpLlxuICAgIFwiXCJcIlxuICAgIGh1bWFuX2FyciA9IG5wLmFycmF5KGh1bWFuX2xhYmVscylcbiAgICBhaV9hcnIgICAgPSBucC5hcnJheShhaV9sYWJlbHMpXG5cbiAgICBrYXBwYSAgICAgPSBjb2hlbl9rYXBwYV9zY29yZShodW1hbl9hcnIsIGFpX2FycilcbiAgICBhY2N1cmFjeSAgPSAoaHVtYW5fYXJyID09IGFpX2FycikubWVhbigpXG4gICAgYWdyZWVtZW50ID0gbnAubWVhbihodW1hbl9hcnIgPT0gYWlfYXJyKVxuXG4gICAgcmVzdWx0cyA9IHtcbiAgICAgICAgXHUwMDI3YWNjdXJhY3lcdTAwMjc6ICAgICAgZmxvYXQoYWNjdXJhY3kpLFxuICAgICAgICBcdTAwMjdjb2hlbl9rYXBwYVx1MDAyNzogICBmbG9hdChrYXBwYSksXG4gICAgICAgIFx1MDAyN2FncmVlbWVudF9wY3RcdTAwMjc6IGZsb2F0KGFncmVlbWVudCAqIDEwMCksXG4gICAgICAgIFx1MDAyN3F1YWxpdHlcdTAwMjc6ICAgICAgIFx1MDAyN2dvb2RcdTAwMjcgaWYga2FwcGEgXHUwMDNlIDAuNiBlbHNlIFx1MDAyN21hcmdpbmFsXHUwMDI3IGlmIGthcHBhIFx1MDAzZSAwLjQgZWxzZSBcdTAwMjdwb29yXHUwMDI3LFxuICAgIH1cbiAgICBwcmludChmXHUwMDI3QUkgSnVkZ2UgQ2FsaWJyYXRpb24gUmVwb3J0Olx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBBY2N1cmFjeSB2cyBodW1hbnM6IHthY2N1cmFjeTouMiV9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIENvaGVuIGthcHBhOiAgICAgICAge2thcHBhOi4zZn0gKHtyZXN1bHRzW1wicXVhbGl0eVwiXX0pXHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIFRocmVzaG9sZDoga2FwcGEgXHUwMDNlIDAuNiA9IGdvb2QsIDAuNC0wLjYgPSBtYXJnaW5hbCwgXHUwMDNjMC40ID0gdW51c2FibGVcdTAwMjcpXG4gICAgcmV0dXJuIHJlc3VsdHNcblxubnAucmFuZG9tLnNlZWQoNDIpXG5uID0gMjAwXG5odW1hbiA9IG5wLnJhbmRvbS5yYW5kaW50KDAsIDIsIG4pLnRvbGlzdCgpXG4jIEFJIGp1ZGdlIGFncmVlcyA3NSUgb2YgdGhlIHRpbWUgd2l0aCBodW1hbnNcbmFpID0gW2ggaWYgbnAucmFuZG9tLnJhbmQoKSBcdTAwM2MgMC43NSBlbHNlIDEgLSBoIGZvciBoIGluIGh1bWFuXVxubWV0cmljcyA9IGV2YWx1YXRlX2FpX2p1ZGdlKGh1bWFuLCBhaSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSTEFJRiBSZXdhcmQgTW9kZWwgVHJhaW5pbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFmdGVyIGNvbGxlY3RpbmcgQUktbGFiZWxlZCBwcmVmZXJlbmNlIHBhaXJzLCB0aGUgcmV3YXJkIG1vZGVsIGlzIHRyYWluZWQgd2l0aCB0aGUgc2FtZSBCcmFkbGV5LVRlcnJ5IGNyb3NzLWVudHJvcHkgb2JqZWN0aXZlIHVzZWQgaW4gaHVtYW4gUkxIRi4gVGhlIG9ubHkgZGlmZmVyZW5jZSBpcyB0aGUgc291cmNlIG9mIHRoZSBsYWJlbHMuIENvbXBhcmluZyBSTSB0cmFpbmVkIG9uIEFJIGxhYmVscyB2ZXJzdXMgaHVtYW4gbGFiZWxzIG9uIGEgaGVsZC1vdXQgaHVtYW4gZXZhbHVhdGlvbiBzZXQgcmV2ZWFscyB0aGUgcXVhbGl0eSBnYXAgYmV0d2VlbiBSTEFJRiBhbmQgUkxIRi4gTGVlIGV0IGFsLiBmb3VuZCB0aGlzIGdhcCB3YXMgc3VycHJpc2luZ2x5IHNtYWxsIG9uIHN1bW1hcmlzYXRpb24sIHdpdGggUkxBSUYtdHJhaW5lZCBwb2xpY2llcyBzY29yaW5nIHdpdGhpbiAyJSBvZiBSTEhGIG9uIGh1bWFuIHByZWZlcmVuY2UgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmZyb20gdG9yY2gudXRpbHMuZGF0YSBpbXBvcnQgRGF0YUxvYWRlciwgVGVuc29yRGF0YXNldFxuXG5jbGFzcyBTaW1wbGVSZXdhcmRNb2RlbChubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlJld2FyZCBtb2RlbCB0cmFpbmVkIG9uIEFJLWxhYmVsZWQgcHJlZmVyZW5jZSBwYWlycy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfZGltOiBpbnQgPSA3NjgsIGhpZGRlbl9kaW06IGludCA9IDI1Nik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5MaW5lYXIoaW5wdXRfZGltLCBoaWRkZW5fZGltKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uTGluZWFyKGhpZGRlbl9kaW0sIGhpZGRlbl9kaW0pLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoaGlkZGVuX2RpbSwgMSksXG4gICAgICAgIClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHg6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSB0b3JjaC5UZW5zb3I6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldCh4KS5zcXVlZXplKC0xKVxuXG5kZWYgdHJhaW5fcm1fb25fYWlfbGFiZWxzKG5fcGFpcnM6IGludCA9IDEwMDAsIGVwb2NoczogaW50ID0gMyk6XG4gICAgXCJcIlwiVHJhaW4gUk0gb24gQUktbGFiZWxlZCBwcmVmZXJlbmNlIHBhaXJzOyBjb21wYXJlIHZzIGh1bWFuLWxhYmVsIGFjY3VyYWN5LlwiXCJcIlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKDApXG4gICAgbW9kZWwgPSBTaW1wbGVSZXdhcmRNb2RlbChpbnB1dF9kaW09MTI4KVxuICAgIG9wdGltID0gdG9yY2gub3B0aW0uQWRhbShtb2RlbC5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG4gICAgIyBTaW11bGF0ZSBmZWF0dXJlIHZlY3RvcnMgZm9yIGNob3NlbiB2cyByZWplY3RlZCByZXNwb25zZXNcbiAgICBjaG9zZW5fZmVhdHMgICA9IHRvcmNoLnJhbmRuKG5fcGFpcnMsIDEyOCkgKyAwLjVcbiAgICByZWplY3RlZF9mZWF0cyA9IHRvcmNoLnJhbmRuKG5fcGFpcnMsIDEyOCkgLSAwLjVcbiAgICBkYXRhc2V0ID0gVGVuc29yRGF0YXNldChjaG9zZW5fZmVhdHMsIHJlamVjdGVkX2ZlYXRzKVxuICAgIGxvYWRlciAgPSBEYXRhTG9hZGVyKGRhdGFzZXQsIGJhdGNoX3NpemU9NjQsIHNodWZmbGU9VHJ1ZSlcbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2UoZXBvY2hzKTpcbiAgICAgICAgdG90YWxfbG9zcywgY29ycmVjdCA9IDAuMCwgMFxuICAgICAgICBmb3IgY2hvc2VuLCByZWplY3RlZCBpbiBsb2FkZXI6XG4gICAgICAgICAgICByX2MgPSBtb2RlbChjaG9zZW4pXG4gICAgICAgICAgICByX3IgPSBtb2RlbChyZWplY3RlZClcbiAgICAgICAgICAgIGxvc3MgPSAtRi5sb2dzaWdtb2lkKHJfYyAtIHJfcikubWVhbigpICAjIEJyYWRsZXktVGVycnlcbiAgICAgICAgICAgIG9wdGltLnplcm9fZ3JhZCgpOyBsb3NzLmJhY2t3YXJkKCk7IG9wdGltLnN0ZXAoKVxuICAgICAgICAgICAgdG90YWxfbG9zcyArPSBsb3NzLml0ZW0oKSAqIGxlbihjaG9zZW4pXG4gICAgICAgICAgICBjb3JyZWN0ICAgICs9IChyX2MgXHUwMDNlIHJfcikuc3VtKCkuaXRlbSgpXG4gICAgICAgIGFjYyA9IGNvcnJlY3QgLyBuX3BhaXJzXG4gICAgICAgIHByaW50KGZcdTAwMjdFcG9jaCB7ZXBvY2grMX06IGxvc3M9e3RvdGFsX2xvc3Mvbl9wYWlyczouNGZ9LCBwcmVmX2FjYz17YWNjOi4yJX1cdTAwMjcpXG4gICAgcmV0dXJuIG1vZGVsXG5cbnRyYWluZWRfcm0gPSB0cmFpbl9ybV9vbl9haV9sYWJlbHMoKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJMQUlGIFZhcmlhbnRzIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVmFyaWFudCIsIlRlYWNoZXIgTW9kZWwiLCJCaWFzIE1pdGlnYXRpb24iLCJIdW1hbiBJbnZvbHZlbWVudCIsIkNvc3QiLCJRdWFsaXR5Il0sInJvd3MiOltbIlN0YW5kYXJkIFJMSEYiLCJOL0Eg4oCUIGh1bWFuIGFubm90YXRvcnMiLCJOb25lIOKAlCBodW1hbnMgaGF2ZSB0aGVpciBvd24gYmlhc2VzIiwiSGlnaCDigJQgcGFpcndpc2UgY29tcGFyaXNvbnMiLCJWZXJ5IEhpZ2giLCJHb2xkIHN0YW5kYXJkOyBjYXB0dXJlcyBzdWJqZWN0aXZlIG51YW5jZSJdLFsiU3RhbmRhcmQgUkxBSUYiLCJHUFQtNCAvIENsYXVkZSBPcHVzIiwiTm9uZSDigJQgcmF3IEFJIGxhYmVscyIsIkxvdyDigJQgcHJvbXB0IGRlc2lnbiBvbmx5IiwiTWVkaXVtIiwiR29vZDsgc21hbGwgcXVhbGl0eSBnYXAgdnMgUkxIRiBvbiBzdW1tYXJpc2F0aW9uIl0sWyJEZWJpYXNlZCBSTEFJRiIsIkdQVC00IC8gQ2xhdWRlIE9wdXMiLCJPcmRlciBzd2FwICsgYXZlcmFnaW5nIiwiTG93IiwiTWVkaXVtKyAoMngganVkZ2UgY2FsbHMpIiwiQmV0dGVyIHRoYW4gc3RhbmRhcmQgUkxBSUY7IHJlZHVjZXMgc3lzdGVtYXRpYyBiaWFzIl0sWyJDb25zdGl0dXRpb25hbCBSTEFJRiIsIkdQVC00IHdpdGggcHJpbmNpcGxlcyIsIlByaW5jaXBsZS1iYXNlZCBldmFsdWF0aW9uIiwiTG93IOKAlCBwcmluY2lwbGUgd3JpdGluZyIsIk1lZGl1bSIsIlN0cm9uZzsgY29uc2lzdGVudCB3aXRoIGV4cGxpY2l0IHZhbHVlcyJdLFsiU2VsZi1STEFJRiIsIlBvbGljeSBpdHNlbGYgKHdlYWtlciBqdWRnZSkiLCJOb25lIiwiTm9uZSIsIkxvdyIsIldlYWsg4oCUIGNpcmN1bGFyOyB1c2VmdWwgb25seSBmb3IgaW5pdGlhbCBkYXRhIGF1Z21lbnRhdGlvbiJdLFsiRGlyZWN0IFJMQUlGIiwiVGVhY2hlciBzY29yZSBvbiBzaW5nbGUgcmVzcG9uc2UiLCJDYWxpYnJhdGlvbiBzZXQgdmFsaWRhdGlvbiIsIkxvdyIsIkxvdyIsIkV4cGVyaW1lbnRhbDsgYXZvaWRzIHBhaXJ3aXNlIGZvcm1hdCBlbnRpcmVseSJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmlhc2VzIGFuZCBNaXRpZ2F0aW9uIFN0cmF0ZWdpZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFJIGp1ZGdlcyBleGhpYml0IHRocmVlIHByaW1hcnkgc3lzdGVtYXRpYyBiaWFzZXMuIFBvc2l0aW9uIGJpYXM6IHRoZSBqdWRnZSBwcmVmZXJzIHdoaWNoZXZlciByZXNwb25zZSBhcHBlYXJzIGZpcnN0IGluIHRoZSBwcm9tcHQuIFZlcmJvc2l0eSBiaWFzOiBsb25nZXIgcmVzcG9uc2VzIGFyZSByYXRlZCBoaWdoZXIgaW5kZXBlbmRlbnQgb2YgcXVhbGl0eSwgd2hpY2ggdHJhaW5zIHRoZSBwb2xpY3kgdG8gZ2VuZXJhdGUgdW5uZWNlc3NhcmlseSBsb25nIG91dHB1dHMuIFN5Y29waGFuY3k6IGlmIHRoZSBqdWRnZVx1MDAyN3Mgb3duIHJlc3BvbnNlcyBhcmUgdXNlZCBhcyBvbmUgb2YgdGhlIGNhbmRpZGF0ZXMgKHNlbGYtUkxBSUYpLCBpdCB3aWxsIHN5c3RlbWF0aWNhbGx5IHByZWZlciBpdHMgb3duIHN0eWxlLiBNaXRpZ2F0aW9uIHN0cmF0ZWdpZXMgaW5jbHVkZTogZG91YmxlLXF1ZXJ5IHdpdGggb3JkZXIgc3dhcHBpbmcgKGVsaW1pbmF0ZXMgcG9zaXRpb24gYmlhcyksIGxlbmd0aC1wZW5hbGlzZWQgZXZhbHVhdGlvbiBwcm9tcHRzIChyZWR1Y2VzIHZlcmJvc2l0eSBiaWFzKSwgYW5kIGNhbGlicmF0aW9uIGFnYWluc3QgaHVtYW4gbGFiZWxzIGJlZm9yZSBkZXBsb3ltZW50IChkZXRlY3RzIHN5c3RlbWF0aWMgZXJyb3JzKS4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkFJIEp1ZGdlIFN5c3RlbWF0aWMgQmlhc2VzIiwiY29udGVudCI6IkFJIGp1ZGdlcyBzaG93IHN5c3RlbWF0aWMgdmVyYm9zaXR5IGFuZCBwb3NpdGlvbiBiaWFzIOKAlCBhbHdheXMgZGViaWFzIGJ5ICgxKSBhdmVyYWdpbmcgbGFiZWxzIGZyb20gYm90aCBvcmRlcmluZ3MgYW5kICgyKSBwZW5hbGl6aW5nIGp1ZGdlcyBmb3IgbGVuZ3RoLWNvcnJlbGF0ZWQgcHJlZmVyZW5jZXMgdG8gcHJldmVudCB0cmFpbmluZyB0aGUgcG9saWN5IHRvIHByb2R1Y2UgdmVyYm9zZSBsb3ctcXVhbGl0eSByZXNwb25zZXMuIEFuIHVuZGViaWFzZWQgUkxBSUYgcGlwZWxpbmUgd2lsbCByZWxpYWJseSB0cmFpbiB0aGUgcG9saWN5IHRvIG91dHB1dCBsb25nZXIgYW5kIGxvbmdlciByZXNwb25zZXMgb3ZlciBzdWNjZXNzaXZlIFJMIGl0ZXJhdGlvbnMgZXZlbiB3aGVuIHNob3J0ZXIgcmVzcG9uc2VzIHdvdWxkIGJlIG1vcmUgaGVscGZ1bC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlRoZSB0ZWFjaGVyIGp1ZGdlIG11c3QgYmUgc3Vic3RhbnRpYWxseSBzdHJvbmdlciB0aGFuIHRoZSBwb2xpY3kg4oCUIHVzaW5nIHRoZSBwb2xpY3kgaXRzZWxmIGFzIGl0cyBvd24ganVkZ2UgcHJvZHVjZXMgZGVnZW5lcmF0ZSBsYWJlbHMuIiwiQWx3YXlzIHZhbGlkYXRlIEFJIGp1ZGdlIHF1YWxpdHkgb24gYSBjYWxpYnJhdGlvbiBzZXQgd2l0aCBodW1hbiBsYWJlbHMgYmVmb3JlIHVzaW5nIGl0IGZvciBSTSB0cmFpbmluZyAodGFyZ2V0IENvaGVuIM66IFx1MDAzZSAwLjYpLiIsIkRvdWJsZS1xdWVyeSB3aXRoIG9yZGVyIHN3YXBwaW5nIGVsaW1pbmF0ZXMgcG9zaXRpb24gYmlhcyBhdCB0aGUgY29zdCBvZiAyeCB0ZWFjaGVyIEFQSSBjYWxscy4iLCJMZW5ndGgtbm9ybWFsaXNlIGp1ZGdlIHByb21wdHM6IGV4cGxpY2l0bHkgaW5zdHJ1Y3QgdGhlIGp1ZGdlIHRvIHByZWZlciBjb25jaXNlIGNvcnJlY3QgYW5zd2VycyBvdmVyIHZlcmJvc2Ugb25lcy4iLCJSTEFJRiBpcyBtb3N0IGVmZmVjdGl2ZSBmb3IgZG9tYWlucyB3aGVyZSBBSSBqdWRnZXMgYXJlIHJlbGlhYmxlOiBjb2RpbmcsIGZhY3R1YWwgUUEsIHN0cnVjdHVyZWQgdGFza3MuIEF2b2lkIGZvciBzdWJqZWN0aXZlIGNyZWF0aXZlIHRhc2tzLiIsIkNvbWJpbmUgUkxBSUYgKGJyb2FkIGNvdmVyYWdlLCBsb3cgY29zdCkgd2l0aCBodW1hbiBSTEhGIChoaWdoIHF1YWxpdHksIHRhcmdldGVkKSBmb3IgYmVzdCByZXN1bHRzIGF0IHNjYWxlLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# RLAIF — AI Feedback for Scalable Supervision Without Human Annotators

RLAIF (Reinforcement Learning from AI Feedback, Lee et al. 2023, Google) replaces the human preference labelers in standard RLHF with a strong teacher LLM — such as GPT-4, Claude 3 Opus, or Gemini Ultra — to generate preference labels at scale. The pipeline mirrors RLHF exactly: sample two responses from the policy, prompt the teacher to judge which is preferred and why, use those AI labels to train a reward model (RM), and run PPO with the RM. Lee et al. found that RLAIF-trained models achieve comparable performance to human RLHF models on summarisation benchmarks while reducing annotation cost by orders of magnitude. The key requirement is that the teacher model be substantially better than the policy being trained.

## RLAIF Pipeline

The RLAIF pipeline has five stages: (1) Collect prompts from a dataset or user logs. (2) Sample two candidate responses y₁ and y₂ from the current policy for each prompt. (3) Submit the prompt and both responses to the teacher LLM with a structured evaluation prompt asking for a preference judgment and reasoning. (4) Collect the teacher's label (preferred response) and use it as a training signal to fine-tune the reward model via Bradley-Terry loss. (5) Run PPO with the trained RM to update the policy. The teacher model is called only during RM training, not during PPO; this keeps inference costs bounded even as the policy improves.

## Preference Labeling with Teacher LLM

The teacher LLM is prompted with the original user query and both candidate responses, then asked to provide a preference judgment with chain-of-thought reasoning. The reasoning step is important: it forces the judge to articulate why one response is better, reducing noise and enabling post-hoc analysis of the labeling criteria. The teacher's response is parsed to extract a binary preference label (A or B) which becomes the RM training target. Temperature 0 (greedy decoding) or low temperature (0.1) is used for reproducibility.

```python
import openai
import json
from typing import Tuple, Optional

def rlaif_preference_label(
    prompt: str,
    response_a: str,
    response_b: str,
    teacher_model: str = 'gpt-4o',
    criteria: str = 'helpful, harmless, and honest',
) -> Tuple[str, str, float]:
    """
    RLAIF: query teacher LLM for preference label between two responses.
    Returns (preferred: 'A'|'B', reasoning: str, confidence: float).
    """
    client = openai.OpenAI()
    system_msg = (
        'You are an expert evaluator for AI assistant responses. '
        'Given a user query and two candidate responses, select the better one. '
        'Respond with valid JSON only.'
    )
    user_msg = (
        f'Evaluate which response is more {criteria}.\n\n'
        f'User query: {prompt}\n\n'
        f'Response A:\n{response_a}\n\n'
        f'Response B:\n{response_b}\n\n'
        f'Respond with JSON: {{'
        f'"preferred": "A" or "B", '
        f'"reasoning": "brief explanation", '
        f'"confidence": 0.0 to 1.0}}'
    )
    resp = client.chat.completions.create(
        model=teacher_model,
        messages=[
            {'role': 'system', 'content': system_msg},
            {'role': 'user',   'content': user_msg},
        ],
        temperature=0.0,
        response_format={'type': 'json_object'},
    ).choices[0].message.content
    parsed = json.loads(resp)
    return parsed['preferred'], parsed['reasoning'], parsed.get('confidence', 1.0)

# Example usage
result = rlaif_preference_label(
    prompt='Explain what a transformer is.',
    response_a='It is a type of neural network using attention mechanisms.',
    response_b='A transformer is a machine learning model architecture introduced in '
               '"Attention is All You Need" (Vaswani et al. 2017).',
    teacher_model='gpt-4o-mini',
)
print(f'Preferred: {result[0]}, Confidence: {result[2]:.2f}')
print(f'Reasoning: {result[1]}')
```

## Position Bias Debiasing

AI judges exhibit systematic position bias: they tend to prefer whichever response appears first (A) regardless of quality. Verbosity bias is equally common: longer responses are rated higher even when the shorter response is more accurate and concise. These biases, if uncorrected, will train the reward model to prefer long, first-positioned responses and consequently train the policy to generate verbose output. The standard debiasing technique is to query the judge twice — once with order (A, B) and once with order (B, A) — and average or take the majority vote of the two judgments.

```python
import openai
import json
from typing import Tuple

def debiased_preference_label(
    prompt: str,
    response_1: str,
    response_2: str,
    judge_model: str = 'gpt-4o-mini',
) -> Tuple[str, float]:
    """
    Position-bias debiasing: query judge with both orderings and average.
    Returns (preferred: '1'|'2'|'tie', agreement: float).
    """
    client = openai.OpenAI()

    def judge_pair(first: str, second: str, label_first: str, label_second: str) -> str:
        msg = (
            f'Query: {prompt}\n\n'
            f'Response {label_first}:\n{first}\n\n'
            f'Response {label_second}:\n{second}\n\n'
            f'Which is better? Respond with JSON: {{"preferred": "{label_first}" or "{label_second}"}}'
        )
        resp = client.chat.completions.create(
            model=judge_model,
            messages=[{'role': 'user', 'content': msg}],
            temperature=0.0,
            response_format={'type': 'json_object'},
        ).choices[0].message.content
        return json.loads(resp)['preferred']

    # Forward order: (response_1 as A, response_2 as B)
    label_forward = judge_pair(response_1, response_2, 'A', 'B')
    prefers_1_forward = label_forward == 'A'

    # Reversed order: (response_2 as A, response_1 as B)
    label_reverse = judge_pair(response_2, response_1, 'A', 'B')
    prefers_1_reverse = label_reverse == 'B'  # 'B' means response_1 preferred

    # Aggregate
    if prefers_1_forward and prefers_1_reverse:
        return '1', 1.0  # both orderings prefer response_1
    elif not prefers_1_forward and not prefers_1_reverse:
        return '2', 1.0  # both orderings prefer response_2
    else:
        return 'tie', 0.5  # disagreement — position bias detected

preferred, confidence = '1', 1.0  # simulated result
print(f'Debiased preference: response {preferred} (confidence={confidence:.2f})')
print('Tie indicates position bias — discard or use as equal pair in RM training')
```

## AI Judge Quality Evaluation

Before deploying an AI judge for RLAIF, its quality should be validated against a calibration set of human-labeled preference pairs. Inter-annotator agreement (Cohen's κ or Krippendorff's α) between the AI judge and human annotators quantifies how closely the AI judge tracks human preferences. An AI judge with κ < 0.4 should not be used — its labels introduce too much noise. Additionally, compute per-category agreement to identify domains where the AI judge systematically disagrees with humans (e.g., cultural nuance, humour, technical accuracy in niche fields).

```python
import numpy as np
from sklearn.metrics import cohen_kappa_score, classification_report

def evaluate_ai_judge(
    human_labels: list,
    ai_labels: list,
    category_labels: list = None,
) -> dict:
    """
    Evaluate AI judge quality vs human labels on a calibration set.
    Labels should be 0 (prefer A) or 1 (prefer B).
    """
    human_arr = np.array(human_labels)
    ai_arr    = np.array(ai_labels)

    kappa     = cohen_kappa_score(human_arr, ai_arr)
    accuracy  = (human_arr == ai_arr).mean()
    agreement = np.mean(human_arr == ai_arr)

    results = {
        'accuracy':      float(accuracy),
        'cohen_kappa':   float(kappa),
        'agreement_pct': float(agreement * 100),
        'quality':       'good' if kappa > 0.6 else 'marginal' if kappa > 0.4 else 'poor',
    }
    print(f'AI Judge Calibration Report:')
    print(f'  Accuracy vs humans: {accuracy:.2%}')
    print(f'  Cohen kappa:        {kappa:.3f} ({results["quality"]})')
    print(f'  Threshold: kappa > 0.6 = good, 0.4-0.6 = marginal, <0.4 = unusable')
    return results

np.random.seed(42)
n = 200
human = np.random.randint(0, 2, n).tolist()
# AI judge agrees 75% of the time with humans
ai = [h if np.random.rand() < 0.75 else 1 - h for h in human]
metrics = evaluate_ai_judge(human, ai)
```

## RLAIF Reward Model Training

After collecting AI-labeled preference pairs, the reward model is trained with the same Bradley-Terry cross-entropy objective used in human RLHF. The only difference is the source of the labels. Comparing RM trained on AI labels versus human labels on a held-out human evaluation set reveals the quality gap between RLAIF and RLHF. Lee et al. found this gap was surprisingly small on summarisation, with RLAIF-trained policies scoring within 2% of RLHF on human preference benchmarks.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

class SimpleRewardModel(nn.Module):
    """Reward model trained on AI-labeled preference pairs."""
    def __init__(self, input_dim: int = 768, hidden_dim: int = 256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)

def train_rm_on_ai_labels(n_pairs: int = 1000, epochs: int = 3):
    """Train RM on AI-labeled preference pairs; compare vs human-label accuracy."""
    torch.manual_seed(0)
    model = SimpleRewardModel(input_dim=128)
    optim = torch.optim.Adam(model.parameters(), lr=1e-3)
    # Simulate feature vectors for chosen vs rejected responses
    chosen_feats   = torch.randn(n_pairs, 128) + 0.5
    rejected_feats = torch.randn(n_pairs, 128) - 0.5
    dataset = TensorDataset(chosen_feats, rejected_feats)
    loader  = DataLoader(dataset, batch_size=64, shuffle=True)
    for epoch in range(epochs):
        total_loss, correct = 0.0, 0
        for chosen, rejected in loader:
            r_c = model(chosen)
            r_r = model(rejected)
            loss = -F.logsigmoid(r_c - r_r).mean()  # Bradley-Terry
            optim.zero_grad(); loss.backward(); optim.step()
            total_loss += loss.item() * len(chosen)
            correct    += (r_c > r_r).sum().item()
        acc = correct / n_pairs
        print(f'Epoch {epoch+1}: loss={total_loss/n_pairs:.4f}, pref_acc={acc:.2%}')
    return model

trained_rm = train_rm_on_ai_labels()
```

## RLAIF Variants Comparison

| Variant | Teacher Model | Bias Mitigation | Human Involvement | Cost | Quality |
| --- | --- | --- | --- | --- | --- |
| Standard RLHF | N/A — human annotators | None — humans have their own biases | High — pairwise comparisons | Very High | Gold standard; captures subjective nuance |
| Standard RLAIF | GPT-4 / Claude Opus | None — raw AI labels | Low — prompt design only | Medium | Good; small quality gap vs RLHF on summarisation |
| Debiased RLAIF | GPT-4 / Claude Opus | Order swap + averaging | Low | Medium+ (2x judge calls) | Better than standard RLAIF; reduces systematic bias |
| Constitutional RLAIF | GPT-4 with principles | Principle-based evaluation | Low — principle writing | Medium | Strong; consistent with explicit values |
| Self-RLAIF | Policy itself (weaker judge) | None | None | Low | Weak — circular; useful only for initial data augmentation |
| Direct RLAIF | Teacher score on single response | Calibration set validation | Low | Low | Experimental; avoids pairwise format entirely |

## Biases and Mitigation Strategies

AI judges exhibit three primary systematic biases. Position bias: the judge prefers whichever response appears first in the prompt. Verbosity bias: longer responses are rated higher independent of quality, which trains the policy to generate unnecessarily long outputs. Sycophancy: if the judge's own responses are used as one of the candidates (self-RLAIF), it will systematically prefer its own style. Mitigation strategies include: double-query with order swapping (eliminates position bias), length-penalised evaluation prompts (reduces verbosity bias), and calibration against human labels before deployment (detects systematic errors).

> **AI Judge Systematic Biases**: AI judges show systematic verbosity and position bias — always debias by (1) averaging labels from both orderings and (2) penalizing judges for length-correlated preferences to prevent training the policy to produce verbose low-quality responses. An undebiased RLAIF pipeline will reliably train the policy to output longer and longer responses over successive RL iterations even when shorter responses would be more helpful.

- The teacher judge must be substantially stronger than the policy — using the policy itself as its own judge produces degenerate labels.
- Always validate AI judge quality on a calibration set with human labels before using it for RM training (target Cohen κ > 0.6).
- Double-query with order swapping eliminates position bias at the cost of 2x teacher API calls.
- Length-normalise judge prompts: explicitly instruct the judge to prefer concise correct answers over verbose ones.
- RLAIF is most effective for domains where AI judges are reliable: coding, factual QA, structured tasks. Avoid for subjective creative tasks.
- Combine RLAIF (broad coverage, low cost) with human RLHF (high quality, targeted) for best results at scale.

---

