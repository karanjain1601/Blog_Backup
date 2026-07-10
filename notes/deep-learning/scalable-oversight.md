---
title: "Scalable Oversight — Debate, Amplification, and Recursive Reward Modeling"
slug: "scalable-oversight"
description: "A technical examination of scalable oversight methods including AI debate, iterated amplification, recursive reward modeling, process supervision, and self-critique pipelines for extending effective human supervision to AI systems that exceed human performance on specific tasks."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2NhbGFibGUgb3ZlcnNpZ2h0IGFkZHJlc3NlcyBhIGNvcmUgYWxpZ25tZW50IGNoYWxsZW5nZTogYXMgQUkgc3lzdGVtcyBiZWNvbWUgbW9yZSBjYXBhYmxlLCBodW1hbiBldmFsdWF0b3JzIGluY3JlYXNpbmdseSBjYW5ub3QgcmVsaWFibHkganVkZ2Ugd2hldGhlciBhIG1vZGVsXHUwMDI3cyBvdXRwdXQgaXMgY29ycmVjdCBvciBzYWZlLiBBIGh1bWFuIGNhbm5vdCB2ZXJpZnkgYSBwcm9vZiBvZiBhIGNvbXBsZXggdGhlb3JlbSwgYXVkaXQgYSBsb25nIGNvZGViYXNlIGZvciBzdWJ0bGUgYnVncywgb3IgZXZhbHVhdGUgd2hldGhlciBhIHN0cmF0ZWdpYyBwbGFuIGlzIHRydWx5IG9wdGltYWwuIFNjYWxhYmxlIG92ZXJzaWdodCBtZXRob2RzIGFpbSB0byBtYWtlIGh1bWFuIHN1cGVydmlzaW9uIGVmZmVjdGl2ZSBldmVuIGZvciB0YXNrcyB3aGVyZSBodW1hbnMgY2Fubm90IGRpcmVjdGx5IGFzc2VzcyBxdWFsaXR5IOKAlCBlc3NlbnRpYWxseSBhbXBsaWZ5aW5nIGh1bWFuIGp1ZGdtZW50IHRvIHdvcmsgYXQgc3VwZXJodW1hbiBjYXBhYmlsaXR5IGxldmVscy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgT3ZlcnNpZ2h0IFByb2JsZW0gYXQgU2NhbGUifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkN1cnJlbnQgUkxIRiByZWxpZXMgb24gaHVtYW4gbGFiZWxlcnMgcHJvdmlkaW5nIGRpcmVjdCBwcmVmZXJlbmNlIGp1ZGdtZW50cy4gVGhpcyB3b3JrcyB3aGVuIGh1bWFucyBjYW4gZXZhbHVhdGUgb3V0cHV0cyDigJQgd3JpdGluZyBxdWFsaXR5LCBmYWN0dWFsIGFjY3VyYWN5LCBjb2RlIGNvcnJlY3RuZXNzIGZvciBzaW1wbGUgcHJvZ3JhbXMuIEJ1dCBpdCBicmVha3MgZG93biB3aGVuIHRoZSB0YXNrIHJlcXVpcmVzIGV4cGVydGlzZSB0aGUgZXZhbHVhdG9yIGxhY2tzLiBBIFBoRC1sZXZlbCBBSSBtaWdodCBwcm9kdWNlIHJlc2VhcmNoLXF1YWxpdHkgYXJndW1lbnRzIHRoYXQgbm9uLWV4cGVydCBsYWJlbGVycyBjYW5ub3QgcHJvcGVybHkgZXZhbHVhdGUuIFNjYWxhYmxlIG92ZXJzaWdodCBzZWVrcyB0byBtYWludGFpbiB0aGUgY29ycmVjdG5lc3Mgc2lnbmFsIGV2ZW4gYXMgQUkgY2FwYWJpbGl0aWVzIGdyb3cgYmV5b25kIGh1bWFuIGV4cGVydC1sZXZlbCwgdXNpbmcgdGhlIEFJXHUwMDI3cyBvd24gY2FwYWJpbGl0aWVzIHRvIGF1Z21lbnQgdGhlIG92ZXJzaWdodCBwcm9jZXNzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFJIERlYmF0ZSDigJQgQXJndW1lbnRhdGlvbiBhcyBhbiBPdmVyc2lnaHQgU2lnbmFsIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBSSBkZWJhdGUgKElydmluZyBldCBhbC4gMjAxOCkgcHJvcG9zZXMgdXNpbmcgdHdvIEFJIGFnZW50cyBhcmd1aW5nIG9wcG9zaXRlIHNpZGVzIG9mIGEgcXVlc3Rpb24gc28gdGhhdCBhIGh1bWFuIGp1ZGdlIGNhbiBpZGVudGlmeSB0aGUgdHJ1dGggYnkgZXZhbHVhdGluZyBhcmd1bWVudHMgcmF0aGVyIHRoYW4gdGhlIG9iamVjdC1sZXZlbCB0YXNrLiBUaGUga2V5IGluc2lnaHQgaXMgdGhhdCBodW1hbnMgYXJlIG9mdGVuIGJldHRlciBhdCBldmFsdWF0aW5nIGFyZ3VtZW50cyB0aGFuIGF0IGdlbmVyYXRpbmcgdGhlbS4gRm9yIGRlYmF0ZSB0byBiZSByZWxpYWJsZSwgdGhlIEFJIG11c3Qgbm90IGJlIGFibGUgdG8gY29uc3RydWN0IGNvbXBlbGxpbmctc291bmRpbmcgYnV0IGZhbHNlIGFyZ3VtZW50cyDigJQgdGhlIGhvbmVzdCBhZ2VudCBzaG91bGQgaGF2ZSBhIHdpbm5pbmcgc3RyYXRlZ3kgaWYgdHJ1dGggaXMgdmVyaWZpYWJsZS4gRGViYXRlIGxpdGVyYXR1cmUgc2hvd3MgdGhhdCBqdWRnZXMgY29ycmVjdGx5IGlkZW50aWZ5IHRoZSBob25lc3QgZGViYXRlciBtb3JlIG9mdGVuIHRoYW4gY2hhbmNlIGV2ZW4gb24gaGFyZCBxdWVzdGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBhbnRocm9waWNcbmZyb20gZGF0YWNsYXNzZXMgaW1wb3J0IGRhdGFjbGFzc1xuZnJvbSB0eXBpbmcgaW1wb3J0IE9wdGlvbmFsXG5cbkBkYXRhY2xhc3NcbmNsYXNzIERlYmF0ZVJvdW5kOlxuICAgIGNsYWltOiBzdHJcbiAgICBhcmdfZm9yOiBzdHJcbiAgICBhcmdfYWdhaW5zdDogc3RyXG4gICAgdmVyZGljdDogT3B0aW9uYWxbc3RyXSA9IE5vbmVcblxuZGVmIGdlbmVyYXRlX2FyZ3VtZW50KGNsaWVudCwgY2xhaW0sIHBvc2l0aW9uKTpcbiAgICAjIEdlbmVyYXRlIGEgcGVyc3Vhc2l2ZSBhcmd1bWVudCBmb3IgdGhlIGdpdmVuIHBvc2l0aW9uXG4gICAgcHJvbXB0ID0gXHUwMDI3Q2xhaW06IFx1MDAyNyArIGNsYWltICsgXHUwMDI3LiBQb3NpdGlvbjogXHUwMDI3ICsgcG9zaXRpb24gKyBcdTAwMjcuIFdyaXRlIGEgMy1zZW50ZW5jZSBhcmd1bWVudC5cdTAwMjdcbiAgICByZXNwID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShcbiAgICAgICAgbW9kZWw9XHUwMDI3Y2xhdWRlLTMtNS1oYWlrdS0yMDI0MTAyMlx1MDAyNyxcbiAgICAgICAgbWF4X3Rva2Vucz0yNTYsXG4gICAgICAgIG1lc3NhZ2VzPVt7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3dXNlclx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogcHJvbXB0fV1cbiAgICApXG4gICAgcmV0dXJuIHJlc3AuY29udGVudFswXS50ZXh0XG5cbmRlZiBydW5fZGViYXRlKGNsYWltKTpcbiAgICAjIFR3byBhZ2VudHMgYXJndWUgb3Bwb3NpbmcgcG9zaXRpb25zOyBodW1hbiBqdWRnZSBldmFsdWF0ZXMgYXJndW1lbnRzXG4gICAgY2xpZW50ID0gYW50aHJvcGljLkFudGhyb3BpYygpXG4gICAgYXJnX2ZvciA9IGdlbmVyYXRlX2FyZ3VtZW50KGNsaWVudCwgY2xhaW0sIFx1MDAyN0ZPUiDigJQgc3VwcG9ydCB0aGUgY2xhaW0gd2l0aCBldmlkZW5jZVx1MDAyNylcbiAgICBhcmdfYWdhaW5zdCA9IGdlbmVyYXRlX2FyZ3VtZW50KGNsaWVudCwgY2xhaW0sIFx1MDAyN0FHQUlOU1Qg4oCUIG9wcG9zZSB3aXRoIGNvdW50ZXItZXZpZGVuY2VcdTAwMjcpXG4gICAganVkZ2VfcHJvbXB0ID0gKFx1MDAyN0NsYWltOiBcdTAwMjcgKyBjbGFpbSArIFx1MDAyNy4gRk9SOiBcdTAwMjcgKyBhcmdfZm9yWzoxMjBdICtcbiAgICAgICAgICAgICAgICAgICAgXHUwMDI3LiBBR0FJTlNUOiBcdTAwMjcgKyBhcmdfYWdhaW5zdFs6MTIwXSArXG4gICAgICAgICAgICAgICAgICAgIFx1MDAyNy4gV2hpY2ggYXJndW1lbnQgaXMgbW9yZSBsb2dpY2FsbHkgY29tcGVsbGluZz8gUmVwbHk6IEZPUiBvciBBR0FJTlNULlx1MDAyNylcbiAgICB2ZXJkaWN0ID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShcbiAgICAgICAgbW9kZWw9XHUwMDI3Y2xhdWRlLTMtNS1oYWlrdS0yMDI0MTAyMlx1MDAyNyxcbiAgICAgICAgbWF4X3Rva2Vucz04MCxcbiAgICAgICAgbWVzc2FnZXM9W3tcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBqdWRnZV9wcm9tcHR9XVxuICAgIClcbiAgICByZXR1cm4gRGViYXRlUm91bmQoY2xhaW09Y2xhaW0sIGFyZ19mb3I9YXJnX2ZvciwgYXJnX2FnYWluc3Q9YXJnX2FnYWluc3QsXG4gICAgICAgICAgICAgICAgICAgICAgIHZlcmRpY3Q9dmVyZGljdC5jb250ZW50WzBdLnRleHQpXG5cbnJlc3VsdCA9IHJ1bl9kZWJhdGUoXHUwMDI3TExNcyBleGhpYml0IGdlbnVpbmUgcmVhc29uaW5nIGJleW9uZCBwYXR0ZXJuIG1hdGNoaW5nLlx1MDAyNylcbnByaW50KFx1MDAyN1ZlcmRpY3Q6XHUwMDI3LCByZXN1bHQudmVyZGljdClcbnByaW50KFx1MDAyN0RlYmF0ZTogaHVtYW5zIGp1ZGdlIGFyZ3VtZW50cyB0aGV5IGNvdWxkIG5vdCBpbmRlcGVuZGVudGx5IGdlbmVyYXRlXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ikl0ZXJhdGVkIEFtcGxpZmljYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikl0ZXJhdGVkIGFtcGxpZmljYXRpb24gKENocmlzdGlhbm8gZXQgYWwuIDIwMTgpIHJlY3Vyc2l2ZWx5IGRlY29tcG9zZXMgaGFyZCB0YXNrcyBpbnRvIGVhc2llciBzdWJwcm9ibGVtcyBhIGh1bWFuIGNhbiBzdXBlcnZpc2UgZGlyZWN0bHkuIEEgaHVtYW4gd2l0aCBhY2Nlc3MgdG8gYW4gQUkgYXNzaXN0YW50IChIQ0gg4oCUIEh1bWFuIHdpdGggYWNjZXNzIHRvIENvcGllcyBvZiB0aGVtc2VsdmVzIGluIGEgSGllcmFyY2h5KSBjYW4gYW5zd2VyIGhhcmRlciBxdWVzdGlvbnMgdGhhbiB0aGV5IGNvdWxkIGFsb25lIGJ5IGRlY29tcG9zaW5nIHRoZW0gYW5kIGRlbGVnYXRpbmcgc3VicHJvYmxlbXMuIFRoZSBBSSBpcyB0cmFpbmVkIHRvIGltaXRhdGUgdGhlIEhDSCwgYW5kIGF0IGVhY2ggY2FwYWJpbGl0eSBsZXZlbCB0aGUgQUkgaGVscHMgdGhlIGh1bWFuIGFuc3dlciBxdWVzdGlvbnMgYXQgdGhlIG5leHQgbGV2ZWwuIFRoZSBwcm9jZXNzIGJvb3RzdHJhcHMgaW5jcmVtZW50YWxseSwgbmV2ZXIgcmVxdWlyaW5nIGh1bWFucyB0byBldmFsdWF0ZSB0YXNrcyB0aGV5IGNhbm5vdCBhc3Nlc3MuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBhbnRocm9waWNcbmZyb20gZGF0YWNsYXNzZXMgaW1wb3J0IGRhdGFjbGFzcywgZmllbGRcbmZyb20gdHlwaW5nIGltcG9ydCBPcHRpb25hbFxuXG5AZGF0YWNsYXNzXG5jbGFzcyBEZWNvbXBvc2l0aW9uTm9kZTpcbiAgICBxdWVzdGlvbjogc3RyXG4gICAgYW5zd2VyOiBPcHRpb25hbFtzdHJdID0gTm9uZVxuICAgIHN1YnF1ZXN0aW9uczogbGlzdCA9IGZpZWxkKGRlZmF1bHRfZmFjdG9yeT1saXN0KVxuXG5kZWYgZGVjb21wb3NlX2FuZF9hbnN3ZXIoY2xpZW50LCBxdWVzdGlvbiwgZGVwdGg9MCwgbWF4X2RlcHRoPTIpOlxuICAgICMgUmVjdXJzaXZlbHkgZGVjb21wb3NlIHF1ZXN0aW9uIGludG8gc2ltcGxlciBzdWJxdWVzdGlvbnNcbiAgICBub2RlID0gRGVjb21wb3NpdGlvbk5vZGUocXVlc3Rpb249cXVlc3Rpb24pXG4gICAgaWYgZGVwdGggXHUwMDNlPSBtYXhfZGVwdGg6XG4gICAgICAgIHJlc3AgPSBjbGllbnQubWVzc2FnZXMuY3JlYXRlKFxuICAgICAgICAgICAgbW9kZWw9XHUwMDI3Y2xhdWRlLTMtNS1oYWlrdS0yMDI0MTAyMlx1MDAyNyxcbiAgICAgICAgICAgIG1heF90b2tlbnM9MjAwLFxuICAgICAgICAgICAgbWVzc2FnZXM9W3tcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiBcdTAwMjdBbnN3ZXIgY29uY2lzZWx5OiBcdTAwMjcgKyBxdWVzdGlvbn1dXG4gICAgICAgIClcbiAgICAgICAgbm9kZS5hbnN3ZXIgPSByZXNwLmNvbnRlbnRbMF0udGV4dFxuICAgICAgICByZXR1cm4gbm9kZVxuICAgIGRlY29tcF9wcm9tcHQgPSBcdTAwMjdCcmVhayBpbnRvIDItMyBzaW1wbGVyIHN1YnF1ZXN0aW9uczogXHUwMDI3ICsgcXVlc3Rpb24gKyBcdTAwMjcuIFJldHVybiBvbmUgc3VicXVlc3Rpb24gcGVyIGxpbmUuXHUwMDI3XG4gICAgZGVjb21wID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShcbiAgICAgICAgbW9kZWw9XHUwMDI3Y2xhdWRlLTMtNS1oYWlrdS0yMDI0MTAyMlx1MDAyNyxcbiAgICAgICAgbWF4X3Rva2Vucz0yMDAsXG4gICAgICAgIG1lc3NhZ2VzPVt7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3dXNlclx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogZGVjb21wX3Byb21wdH1dXG4gICAgKVxuICAgIHN1YnFzID0gW3Euc3RyaXAoKSBmb3IgcSBpbiBkZWNvbXAuY29udGVudFswXS50ZXh0LnN0cmlwKCkuc3BsaXQoXHUwMDI3XFxuXHUwMDI3KSBpZiBxLnN0cmlwKCldWzozXVxuICAgIGZvciBzcSBpbiBzdWJxczpcbiAgICAgICAgbm9kZS5zdWJxdWVzdGlvbnMuYXBwZW5kKGRlY29tcG9zZV9hbmRfYW5zd2VyKGNsaWVudCwgc3EsIGRlcHRoICsgMSwgbWF4X2RlcHRoKSlcbiAgICBzdWJfYW5zd2VycyA9IFtzcS5hbnN3ZXIgZm9yIHNxIGluIG5vZGUuc3VicXVlc3Rpb25zIGlmIHNxLmFuc3dlcl1cbiAgICBhZ2dfcHJvbXB0ID0gXHUwMDI3UXVlc3Rpb246IFx1MDAyNyArIHF1ZXN0aW9uICsgXHUwMDI3LiBTdWJhbnN3ZXJzOiBcdTAwMjcgKyBzdHIoc3ViX2Fuc3dlcnMpICsgXHUwMDI3LiBTeW50aGVzaXplIGEgZmluYWwgYW5zd2VyLlx1MDAyN1xuICAgIGFnZyA9IGNsaWVudC5tZXNzYWdlcy5jcmVhdGUoXG4gICAgICAgIG1vZGVsPVx1MDAyN2NsYXVkZS0zLTUtaGFpa3UtMjAyNDEwMjJcdTAwMjcsXG4gICAgICAgIG1heF90b2tlbnM9MzAwLFxuICAgICAgICBtZXNzYWdlcz1be1x1MDAyN3JvbGVcdTAwMjc6IFx1MDAyN3VzZXJcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IGFnZ19wcm9tcHR9XVxuICAgIClcbiAgICBub2RlLmFuc3dlciA9IGFnZy5jb250ZW50WzBdLnRleHRcbiAgICByZXR1cm4gbm9kZVxuXG5jbGllbnQgPSBhbnRocm9waWMuQW50aHJvcGljKClcbnRyZWUgPSBkZWNvbXBvc2VfYW5kX2Fuc3dlcihjbGllbnQsIFx1MDAyN1doYXQgYXJlIHRoZSBlY29ub21pYyBpbXBhY3RzIG9mIHdpZGVzcHJlYWQgQUkgYWRvcHRpb24/XHUwMDI3LCBtYXhfZGVwdGg9MSlcbnByaW50KFx1MDAyN1Jvb3QgYW5zd2VyOlx1MDAyNywgdHJlZS5hbnN3ZXJbOjEwMF0gKyBcdTAwMjcuLi5cdTAwMjcpXG5wcmludChcdTAwMjdTdWJxdWVzdGlvbnM6XHUwMDI3LCBbc3EucXVlc3Rpb24gZm9yIHNxIGluIHRyZWUuc3VicXVlc3Rpb25zXSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZWN1cnNpdmUgUmV3YXJkIE1vZGVsaW5nIGFuZCBQcm9jZXNzIFN1cGVydmlzaW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZWN1cnNpdmUgcmV3YXJkIG1vZGVsaW5nIChSUk0pIHRyYWlucyBhIHJld2FyZCBtb2RlbCBhdCBlYWNoIGNhcGFiaWxpdHkgbGV2ZWwgYW5kIHVzZXMgaXQgdG8gc3VwZXJ2aXNlIHRyYWluaW5nIGF0IHRoZSBuZXh0IGxldmVsLiBQcm9jZXNzIHJld2FyZCBtb2RlbHMgKFBSTXMpIHJld2FyZCBlYWNoIGludGVybWVkaWF0ZSByZWFzb25pbmcgc3RlcCByYXRoZXIgdGhhbiBvbmx5IHRoZSBmaW5hbCBhbnN3ZXIg4oCUIHRoaXMgcHJvdmlkZXMgbXVjaCBkZW5zZXIgdHJhaW5pbmcgc2lnbmFsIGFuZCBlbmFibGVzIGNhdGNoaW5nIGVycm9ycyBtaWQtY2hhaW4gYmVmb3JlIHRoZXkgcHJvcGFnYXRlLiBPcGVuQUlcdTAwMjdzIExldFx1MDAyN3MgVmVyaWZ5IFN0ZXAgYnkgU3RlcCAoTGlnaHRtYW4gZXQgYWwuIDIwMjMpIGRlbW9uc3RyYXRlZCB0aGF0IFBSTXMgdHJhaW5lZCBvbiBodW1hbiBzdGVwLWxldmVsIGFubm90YXRpb25zIHNpZ25pZmljYW50bHkgb3V0cGVyZm9ybSBvdXRjb21lIHJld2FyZCBtb2RlbHMgb24gTUFUSC4gUFJNcyBhcmUgbm93IHRoZSBtb3N0IHByYWN0aWNhbGx5IGRlcGxveWVkIGZvcm0gb2Ygc2NhbGFibGUgb3ZlcnNpZ2h0LCB1c2VkIGluIG8xL28zLXN0eWxlIHJlYXNvbmluZyBtb2RlbHMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBhbnRocm9waWNcbmZyb20gdHlwaW5nIGltcG9ydCBMaXRlcmFsXG5cbmRlZiBhbm5vdGF0ZV9yZWFzb25pbmdfc3RlcHMoY2xpZW50LCBwcm9ibGVtLCBzb2x1dGlvbik6XG4gICAgIyBBc2sgdGhlIG1vZGVsIHRvIGxhYmVsIGVhY2ggcmVhc29uaW5nIHN0ZXAgYXMgY29ycmVjdCBvciBpbmNvcnJlY3RcbiAgICBzdGVwcyA9IFtzLnN0cmlwKCkgZm9yIHMgaW4gc29sdXRpb24uc3RyaXAoKS5zcGxpdChcdTAwMjdcXG5cdTAwMjcpIGlmIHMuc3RyaXAoKV1cbiAgICBhbm5vdGF0ZWQgPSBbXVxuICAgIGZvciBpLCBzdGVwIGluIGVudW1lcmF0ZShzdGVwcyk6XG4gICAgICAgIHByaW9yX3N0ZXBzID0gXHUwMDI3XFxuXHUwMDI3LmpvaW4oc3RlcHNbOmldKVxuICAgICAgICBwcm9tcHQgPSAoXHUwMDI3TWF0aCBwcm9ibGVtOiBcdTAwMjcgKyBwcm9ibGVtICsgXHUwMDI3XFxuXHUwMDI3ICtcbiAgICAgICAgICAgICAgICAgIFx1MDAyN1JlYXNvbmluZyBzbyBmYXI6XFxuXHUwMDI3ICsgcHJpb3Jfc3RlcHMgKyBcdTAwMjdcXG5cdTAwMjcgK1xuICAgICAgICAgICAgICAgICAgXHUwMDI3TmV4dCBzdGVwOiBcdTAwMjcgKyBzdGVwICsgXHUwMDI3XFxuXHUwMDI3ICtcbiAgICAgICAgICAgICAgICAgIFx1MDAyN0lzIHRoaXMgc3RlcCBjb3JyZWN0PyBSZXBseTogQ09SUkVDVCBvciBJTkNPUlJFQ1Qgd2l0aCBhIG9uZS1zZW50ZW5jZSByZWFzb24uXHUwMDI3KVxuICAgICAgICByZXNwID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShcbiAgICAgICAgICAgIG1vZGVsPVx1MDAyN2NsYXVkZS0zLTUtaGFpa3UtMjAyNDEwMjJcdTAwMjcsXG4gICAgICAgICAgICBtYXhfdG9rZW5zPTEyMCxcbiAgICAgICAgICAgIG1lc3NhZ2VzPVt7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3dXNlclx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogcHJvbXB0fV1cbiAgICAgICAgKVxuICAgICAgICBsYWJlbF90ZXh0ID0gcmVzcC5jb250ZW50WzBdLnRleHQuc3RyaXAoKVxuICAgICAgICBsYWJlbCA9IFx1MDAyN2NvcnJlY3RcdTAwMjcgaWYgbGFiZWxfdGV4dC51cHBlcigpLnN0YXJ0c3dpdGgoXHUwMDI3Q09SUkVDVFx1MDAyNykgZWxzZSBcdTAwMjdpbmNvcnJlY3RcdTAwMjdcbiAgICAgICAgYW5ub3RhdGVkLmFwcGVuZCh7XHUwMDI3c3RlcFx1MDAyNzogc3RlcCwgXHUwMDI3bGFiZWxcdTAwMjc6IGxhYmVsLCBcdTAwMjdyZWFzb25cdTAwMjc6IGxhYmVsX3RleHR9KVxuICAgIHJldHVybiBhbm5vdGF0ZWRcblxuY2xpZW50ID0gYW50aHJvcGljLkFudGhyb3BpYygpXG5wcm9ibGVtID0gXHUwMDI3U29sdmU6IDN4ICsgNyA9IDIyXHUwMDI3XG5zb2x1dGlvbiA9IFx1MDAyN1N1YnRyYWN0IDcgZnJvbSBib3RoIHNpZGVzOiAzeCA9IDE1XFxuRGl2aWRlIGJvdGggc2lkZXMgYnkgMzogeCA9IDVcXG5DaGVjazogMyg1KSArIDcgPSAyMi5cdTAwMjdcbmFubm90YXRpb25zID0gYW5ub3RhdGVfcmVhc29uaW5nX3N0ZXBzKGNsaWVudCwgcHJvYmxlbSwgc29sdXRpb24pXG5mb3IgYW5uIGluIGFubm90YXRpb25zOlxuICAgIHByaW50KGZcIlt7YW5uW1x1MDAyN2xhYmVsXHUwMDI3XS51cHBlcigpfV0ge2FubltcdTAwMjdzdGVwXHUwMDI3XVs6NjBdfVwiKVxucHJpbnQoXHUwMDI3UFJNIGRhdGFzZXQ6XHUwMDI3LCBsZW4oYW5ub3RhdGlvbnMpLCBcdTAwMjdzdGVwIGFubm90YXRpb25zIGNvbGxlY3RlZFx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTZWxmLUNyaXRpcXVlIGFzIE92ZXJzaWdodCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU2VsZi1jcml0aXF1ZSBwaXBlbGluZXMgYXNrIHRoZSBtb2RlbCB0byBmaW5kIGZsYXdzIGluIGl0cyBvd24gYW5zd2VyIGFuZCB1c2UgY3JpdGlxdWUgcXVhbGl0eSBhcyBhbiBvdmVyc2lnaHQgc2lnbmFsLiBDb25zdGl0dXRpb25hbCBBSSAoQW50aHJvcGljIDIwMjIpIHVzZXMgYSBsaXN0IG9mIHByaW5jaXBsZXMgdG8gZ3VpZGUgc2VsZi1jcml0aXF1ZSBhbmQgcmV2aXNpb24sIGVuYWJsaW5nIHNjYWxhYmxlIG92ZXJzaWdodCB3aXRoIG1pbmltYWwgaHVtYW4gbGFiZWxzLiBUaGUgY3JpdGlxdWUgc3RlcCBzdXJmYWNlcyBwb3RlbnRpYWwgZXJyb3JzIGZvciBodW1hbiByZXZpZXcsIGFsbG93aW5nIGh1bWFucyB0byBmb2N1cyB0aGVpciBsaW1pdGVkIGF0dGVudGlvbiBvbiBmbGFnZ2VkIG91dHB1dHMgcmF0aGVyIHRoYW4gcmV2aWV3aW5nIGV2ZXJ5dGhpbmcuIFNlbGYtY3JpdGlxdWUgYWxzbyBlbmFibGVzIGl0ZXJhdGl2ZSByZWZpbmVtZW50IOKAlCBnZW5lcmF0ZSwgY3JpdGlxdWUsIHJldmlzZSDigJQgYXMgYW4gYXV0b21hdGVkIHNlbGYtaW1wcm92ZW1lbnQgbG9vcC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IGFudGhyb3BpY1xuZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzXG5cbkBkYXRhY2xhc3NcbmNsYXNzIENyaXRpcXVlZFJlc3BvbnNlOlxuICAgIHF1ZXN0aW9uOiBzdHJcbiAgICBpbml0aWFsX2Fuc3dlcjogc3RyXG4gICAgY3JpdGlxdWU6IHN0clxuICAgIGhhc19lcnJvcnM6IGJvb2xcbiAgICByZXZpc2VkX2Fuc3dlcjogc3RyXG5cbmRlZiBzZWxmX2NyaXRpcXVlX3BpcGVsaW5lKGNsaWVudCwgcXVlc3Rpb24pOlxuICAgICMgU3RlcCAxOiBnZW5lcmF0ZSBpbml0aWFsIGFuc3dlclxuICAgIGFuc3dlcl9yZXNwID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShcbiAgICAgICAgbW9kZWw9XHUwMDI3Y2xhdWRlLTMtNS1oYWlrdS0yMDI0MTAyMlx1MDAyNyxcbiAgICAgICAgbWF4X3Rva2Vucz00MDAsXG4gICAgICAgIG1lc3NhZ2VzPVt7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3dXNlclx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogcXVlc3Rpb259XVxuICAgIClcbiAgICBpbml0aWFsID0gYW5zd2VyX3Jlc3AuY29udGVudFswXS50ZXh0XG4gICAgIyBTdGVwIDI6IGFzayBtb2RlbCB0byBjcml0aXF1ZSBpdHMgb3duIGFuc3dlclxuICAgIGNyaXRpcXVlX3Jlc3AgPSBjbGllbnQubWVzc2FnZXMuY3JlYXRlKFxuICAgICAgICBtb2RlbD1cdTAwMjdjbGF1ZGUtMy01LWhhaWt1LTIwMjQxMDIyXHUwMDI3LFxuICAgICAgICBtYXhfdG9rZW5zPTMwMCxcbiAgICAgICAgbWVzc2FnZXM9W3tcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiAoXHUwMDI3UXVlc3Rpb246IFx1MDAyNyArIHF1ZXN0aW9uICsgXHUwMDI3XFxuQW5zd2VyOiBcdTAwMjcgKyBpbml0aWFsICtcbiAgICAgICAgICAgICAgICAgICBcdTAwMjdcXG5Dcml0aXF1ZSB0aGlzIGFuc3dlci4gTGlzdCBhbnkgZmFjdHVhbCBlcnJvcnMsIGxvZ2ljYWwgZmxhd3MsIG9yIGtleSBvbWlzc2lvbnMuIFx1MDAyNyArXG4gICAgICAgICAgICAgICAgICAgXHUwMDI3U3RhcnQgd2l0aCBFUlJPUiBpZiBlcnJvcnMgZm91bmQsIGVsc2UgTE9PS1MgR09PRC5cdTAwMjcpfV1cbiAgICApXG4gICAgY3JpdGlxdWUgPSBjcml0aXF1ZV9yZXNwLmNvbnRlbnRbMF0udGV4dFxuICAgIGhhc19lcnJvcnMgPSBjcml0aXF1ZS51cHBlcigpLnN0YXJ0c3dpdGgoXHUwMDI3RVJST1JcdTAwMjcpXG4gICAgIyBTdGVwIDM6IHJldmlzZSBvbmx5IGlmIGVycm9ycyB3ZXJlIGZsYWdnZWRcbiAgICByZXZpc2VkID0gaW5pdGlhbFxuICAgIGlmIGhhc19lcnJvcnM6XG4gICAgICAgIHJldmlzZV9yZXNwID0gY2xpZW50Lm1lc3NhZ2VzLmNyZWF0ZShcbiAgICAgICAgICAgIG1vZGVsPVx1MDAyN2NsYXVkZS0zLTUtaGFpa3UtMjAyNDEwMjJcdTAwMjcsXG4gICAgICAgICAgICBtYXhfdG9rZW5zPTQwMCxcbiAgICAgICAgICAgIG1lc3NhZ2VzPVt7XHUwMDI3cm9sZVx1MDAyNzogXHUwMDI3dXNlclx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogKFx1MDAyN1F1ZXN0aW9uOiBcdTAwMjcgKyBxdWVzdGlvbiArXG4gICAgICAgICAgICAgICAgICAgICAgIFx1MDAyN1xcbk9yaWdpbmFsOiBcdTAwMjcgKyBpbml0aWFsICsgXHUwMDI3XFxuQ3JpdGlxdWU6IFx1MDAyNyArIGNyaXRpcXVlICtcbiAgICAgICAgICAgICAgICAgICAgICAgXHUwMDI3XFxuUHJvdmlkZSBhIGNvcnJlY3RlZCBhbnN3ZXIuXHUwMDI3KX1dXG4gICAgICAgIClcbiAgICAgICAgcmV2aXNlZCA9IHJldmlzZV9yZXNwLmNvbnRlbnRbMF0udGV4dFxuICAgIHJldHVybiBDcml0aXF1ZWRSZXNwb25zZShxdWVzdGlvbiwgaW5pdGlhbCwgY3JpdGlxdWUsIGhhc19lcnJvcnMsIHJldmlzZWQpXG5cbmNsaWVudCA9IGFudGhyb3BpYy5BbnRocm9waWMoKVxucmVzdWx0ID0gc2VsZl9jcml0aXF1ZV9waXBlbGluZShjbGllbnQsIFx1MDAyN1doYXQgaXMgdGhlIGNhcGl0YWwgb2YgQXVzdHJhbGlhIGFuZCBpdHMgYXBwcm94aW1hdGUgcG9wdWxhdGlvbj9cdTAwMjcpXG5wcmludChcdTAwMjdFcnJvcnMgZm91bmQ6XHUwMDI3LCByZXN1bHQuaGFzX2Vycm9ycylcbnByaW50KFx1MDAyN0NyaXRpcXVlIHByZXZpZXc6XHUwMDI3LCByZXN1bHQuY3JpdGlxdWVbOjEwMF0gKyBcdTAwMjcuLi5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tcGFyaW5nIFNjYWxhYmxlIE92ZXJzaWdodCBBcHByb2FjaGVzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFwcHJvYWNoIiwiQ29yZSBBc3N1bXB0aW9uIiwiSHVtYW4gSW52b2x2ZW1lbnQiLCJTY2FsYWJpbGl0eSBMaW1pdCIsIkN1cnJlbnQgU3RhdHVzIl0sInJvd3MiOltbIkFJIERlYmF0ZSIsIkh1bWFucyBqdWRnZSBhcmd1bWVudHMgYmV0dGVyIHRoYW4gZ2VuZXJhdGluZyB0aGVtOyBob25lc3QgYWdlbnQgd2lucyIsIkp1ZGdlIGRlYmF0ZXMiLCJSZXF1aXJlcyBob25lc3QgZGViYXRlcnM7IGRlY2VwdGl2ZSBBSSBjYW4gZXhwbG9pdCIsIlJlc2VhcmNoIOKAlCBubyBsYXJnZS1zY2FsZSBkZXBsb3ltZW50Il0sWyJBbXBsaWZpY2F0aW9uIChIQ0gpIiwiSGFyZCB0YXNrcyBkZWNvbXBvc2UgaW50byBzdXBlcnZpc2VkIHN1YnRhc2tzIHJlY3Vyc2l2ZWx5IiwiU3VwZXJ2aXNlIGxlYWYgc3VicHJvYmxlbXMiLCJEZWNvbXBvc2l0aW9uIG11c3QgdGVybWluYXRlIGF0IGh1bWFuLWV2YWx1YWJsZSBsZXZlbCIsIlJlc2VhcmNoIOKAlCBjb25jZXB0dWFsIGZyYW1ld29yayJdLFsiUmVjdXJzaXZlIFJld2FyZCBNb2RlbGluZyIsIlJNIGF0IGxldmVsIE4gc3VwZXJ2aXNlcyB0cmFpbmluZyBhdCBsZXZlbCBOKzEiLCJMYWJlbCBSTSB0cmFpbmluZyBkYXRhIGF0IGVhY2ggbGV2ZWwiLCJSTSBtaXNzcGVjaWZpY2F0aW9uIGNvbXBvdW5kcyBhY3Jvc3MgbGV2ZWxzIiwiRWFybHkgcmVzZWFyY2gg4oCUIHVzZWQgaW4gQW50aHJvcGljIFJMSEYiXSxbIlByb2Nlc3MgU3VwZXJ2aXNpb24gKFBSTSkiLCJTdGVwLWxldmVsIGNvcnJlY3RuZXNzIGlzIGV2YWx1YWJsZSBldmVuIHdoZW4gZmluYWwgYW5zd2VyIGlzIG5vdCIsIkFubm90YXRlIGludGVybWVkaWF0ZSByZWFzb25pbmcgc3RlcHMiLCJFeHBlbnNpdmUgc3RlcC1sZXZlbCBhbm5vdGF0aW9uOyBhbWJpZ3VvdXMgc3RlcHMiLCJEZXBsb3llZCDigJQgdXNlZCBpbiBvMS9vMyByZWFzb25pbmcgbW9kZWxzIl0sWyJTZWxmLUNyaXRpcXVlIChDQUkpIiwiTW9kZWwgY3JpdGlxdWVzIGFyZSBpbmZvcm1hdGl2ZSBzaWduYWxzOyBwcmluY2lwbGVzIGd1aWRlIGNvcnJlY3Rpb24iLCJEZWZpbmUgY3JpdGlxdWUgcHJpbmNpcGxlczsgc3BvdC1jaGVjayIsIk1vZGVsIG1heSBub3QgY2F0Y2ggaXRzIG93biBzeXN0ZW1hdGljIGVycm9ycyIsIkRlcGxveWVkIOKAlCBDb25zdGl0dXRpb25hbCBBSSBpbiBwcm9kdWN0aW9uIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW1pdGF0aW9ucyBhbmQgUmVzZWFyY2ggRnJvbnRpZXJzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGwgc2NhbGFibGUgb3ZlcnNpZ2h0IG1ldGhvZHMgc2hhcmUgYSBjb21tb24gbGltaXRhdGlvbjogdGhleSBhc3N1bWUgdGhlIEFJIGNhbm5vdCBzeXN0ZW1hdGljYWxseSBkZWNlaXZlIHRoZSBvdmVyc2lnaHQgbWVjaGFuaXNtLiBEZWJhdGUgcmVxdWlyZXMgaG9uZXN0IGFnZW50cyB3aXRoIHdpbm5pbmcgc3RyYXRlZ2llczsgYW1wbGlmaWNhdGlvbiByZXF1aXJlcyBkZWNvbXBvc2l0aW9ucyB0aGF0IGRvblx1MDAyN3QgaGlkZSBlcnJvcnM7IHNlbGYtY3JpdGlxdWUgcmVxdWlyZXMgbW9kZWxzIHRoYXQgY2FuIGFjdHVhbGx5IGRldGVjdCB0aGVpciBvd24gbWlzdGFrZXMuIEFzIEFJIHN5c3RlbXMgYmVjb21lIG1vcmUgY2FwYWJsZSwgdGhleSBtYXkgbGVhcm4gdG8gZ2FtZSB0aGVzZSBvdmVyc2lnaHQgbWVjaGFuaXNtcyDigJQgcHJvZHVjaW5nIGNvbXBlbGxpbmcgZGViYXRlIGFyZ3VtZW50cyBmb3IgZmFsc2UgcG9zaXRpb25zLCBmaW5kaW5nIGRlY29tcG9zaXRpb25zIHRoYXQgb2JzY3VyZSBlcnJvcnMsIG9yIHByb2R1Y2luZyBjcml0aXF1ZXMgdGhhdCBzZWVtIHRob3JvdWdoIGJ1dCBtaXNzIHJlYWwgcHJvYmxlbXMuIEFkdmVyc2FyaWFsIHJvYnVzdG5lc3Mgb2Ygb3ZlcnNpZ2h0IG1lY2hhbmlzbXMgaXMgYW4gb3BlbiByZXNlYXJjaCBwcm9ibGVtLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRGViYXRlIGFzc3VtZXMgdHJ1dGggaXMgdmVyaWZpYWJsZSBvbmNlIGFyZ3VlZCDigJQgZmFpbHMgZm9yIHRhc2tzIHdpdGggbm8gZ3JvdW5kIHRydXRoIChlLmcuLCBldGhpY2FsIGp1ZGdtZW50LCBzdWJqZWN0aXZlIHF1YWxpdHkpLiIsIkFtcGxpZmljYXRpb24gYm90dGxlbmVja3MgYXQgdGhlIGxvd2VzdC1sZXZlbCBzdWJ0YXNrOiBpZiBhbnkgbGVhZiBzdWJ0YXNrIGV4Y2VlZHMgaHVtYW4gYWJpbGl0eSwgdGhlIG92ZXJzaWdodCBjaGFpbiBicmVha3MuIiwiUmVjdXJzaXZlIHJld2FyZCBtb2RlbGluZyBjb21wb3VuZHMgUk0gZXJyb3JzIOKAlCBlYWNoIGxldmVsXHUwMDI3cyBSTSBpbmhlcml0cyBpbmFjY3VyYWNpZXMgZnJvbSB0aGUgcHJldmlvdXMgbGV2ZWwuIiwiUHJvY2VzcyBzdXBlcnZpc2lvbiBhbm5vdGF0aW9uIGlzIGV4cGVuc2l2ZTogTGlnaHRtYW4gZXQgYWwuIGNvbGxlY3RlZCA4MDBLIHN0ZXAtbGV2ZWwgbGFiZWxzIGZvciB0aGUgTUFUSCBkYXRhc2V0LiIsIlNlbGYtY3JpdGlxdWUgZmFpbHMgd2hlbiB0aGUgbW9kZWwgaGFzIHN5c3RlbWF0aWMgYmxpbmQgc3BvdHMg4oCUIGlmIHRoZSBtb2RlbCBhbHdheXMgZ2VuZXJhdGVzIHRoZSBzYW1lIHR5cGUgb2YgZXJyb3IsIGl0IGNhbm5vdCBzZWxmLWRldGVjdCBpdC4iXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJTY2FsYWJsZSBPdmVyc2lnaHQgaW4gUHJvZHVjdGlvbiIsImNvbnRlbnQiOiJTY2FsYWJsZSBvdmVyc2lnaHQgbWV0aG9kcyBhcmUgcHJpbWFyaWx5IHJlc2VhcmNoIGRpcmVjdGlvbnMg4oCUIGN1cnJlbnQgcHJvZHVjdGlvbiBSTEhGIHN0aWxsIHJlbGllcyBvbiBkaXJlY3QgaHVtYW4gcHJlZmVyZW5jZSBsYWJlbHMuIFByb2Nlc3MgcmV3YXJkIG1vZGVscyAoUFJNcykgYXJlIHRoZSBtb3N0IHByYWN0aWNhbGx5IGRlcGxveWVkIGZvcm0gb2Ygc2NhbGFibGUgb3ZlcnNpZ2h0LCB1c2VkIGluIG8xL28zLXN0eWxlIHJlYXNvbmluZyBtb2RlbHMgdG8gdmVyaWZ5IGVhY2ggcmVhc29uaW5nIHN0ZXAgYW5kIHNlbGVjdCBjaGFpbnMgd2l0aCBjb25zaXN0ZW50bHkgY29ycmVjdCBpbnRlcm1lZGlhdGUgc3RlcHMuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Scalable Oversight — Debate, Amplification, and Recursive Reward Modeling

Scalable oversight addresses a core alignment challenge: as AI systems become more capable, human evaluators increasingly cannot reliably judge whether a model's output is correct or safe. A human cannot verify a proof of a complex theorem, audit a long codebase for subtle bugs, or evaluate whether a strategic plan is truly optimal. Scalable oversight methods aim to make human supervision effective even for tasks where humans cannot directly assess quality — essentially amplifying human judgment to work at superhuman capability levels.

## The Oversight Problem at Scale

Current RLHF relies on human labelers providing direct preference judgments. This works when humans can evaluate outputs — writing quality, factual accuracy, code correctness for simple programs. But it breaks down when the task requires expertise the evaluator lacks. A PhD-level AI might produce research-quality arguments that non-expert labelers cannot properly evaluate. Scalable oversight seeks to maintain the correctness signal even as AI capabilities grow beyond human expert-level, using the AI's own capabilities to augment the oversight process.

## AI Debate — Argumentation as an Oversight Signal

AI debate (Irving et al. 2018) proposes using two AI agents arguing opposite sides of a question so that a human judge can identify the truth by evaluating arguments rather than the object-level task. The key insight is that humans are often better at evaluating arguments than at generating them. For debate to be reliable, the AI must not be able to construct compelling-sounding but false arguments — the honest agent should have a winning strategy if truth is verifiable. Debate literature shows that judges correctly identify the honest debater more often than chance even on hard questions.

```python
import anthropic
from dataclasses import dataclass
from typing import Optional

@dataclass
class DebateRound:
    claim: str
    arg_for: str
    arg_against: str
    verdict: Optional[str] = None

def generate_argument(client, claim, position):
    # Generate a persuasive argument for the given position
    prompt = 'Claim: ' + claim + '. Position: ' + position + '. Write a 3-sentence argument.'
    resp = client.messages.create(
        model='claude-3-5-haiku-20241022',
        max_tokens=256,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return resp.content[0].text

def run_debate(claim):
    # Two agents argue opposing positions; human judge evaluates arguments
    client = anthropic.Anthropic()
    arg_for = generate_argument(client, claim, 'FOR — support the claim with evidence')
    arg_against = generate_argument(client, claim, 'AGAINST — oppose with counter-evidence')
    judge_prompt = ('Claim: ' + claim + '. FOR: ' + arg_for[:120] +
                    '. AGAINST: ' + arg_against[:120] +
                    '. Which argument is more logically compelling? Reply: FOR or AGAINST.')
    verdict = client.messages.create(
        model='claude-3-5-haiku-20241022',
        max_tokens=80,
        messages=[{'role': 'user', 'content': judge_prompt}]
    )
    return DebateRound(claim=claim, arg_for=arg_for, arg_against=arg_against,
                       verdict=verdict.content[0].text)

result = run_debate('LLMs exhibit genuine reasoning beyond pattern matching.')
print('Verdict:', result.verdict)
print('Debate: humans judge arguments they could not independently generate')
```

## Iterated Amplification

Iterated amplification (Christiano et al. 2018) recursively decomposes hard tasks into easier subproblems a human can supervise directly. A human with access to an AI assistant (HCH — Human with access to Copies of themselves in a Hierarchy) can answer harder questions than they could alone by decomposing them and delegating subproblems. The AI is trained to imitate the HCH, and at each capability level the AI helps the human answer questions at the next level. The process bootstraps incrementally, never requiring humans to evaluate tasks they cannot assess.

```python
import anthropic
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DecompositionNode:
    question: str
    answer: Optional[str] = None
    subquestions: list = field(default_factory=list)

def decompose_and_answer(client, question, depth=0, max_depth=2):
    # Recursively decompose question into simpler subquestions
    node = DecompositionNode(question=question)
    if depth >= max_depth:
        resp = client.messages.create(
            model='claude-3-5-haiku-20241022',
            max_tokens=200,
            messages=[{'role': 'user', 'content': 'Answer concisely: ' + question}]
        )
        node.answer = resp.content[0].text
        return node
    decomp_prompt = 'Break into 2-3 simpler subquestions: ' + question + '. Return one subquestion per line.'
    decomp = client.messages.create(
        model='claude-3-5-haiku-20241022',
        max_tokens=200,
        messages=[{'role': 'user', 'content': decomp_prompt}]
    )
    subqs = [q.strip() for q in decomp.content[0].text.strip().split('\n') if q.strip()][:3]
    for sq in subqs:
        node.subquestions.append(decompose_and_answer(client, sq, depth + 1, max_depth))
    sub_answers = [sq.answer for sq in node.subquestions if sq.answer]
    agg_prompt = 'Question: ' + question + '. Subanswers: ' + str(sub_answers) + '. Synthesize a final answer.'
    agg = client.messages.create(
        model='claude-3-5-haiku-20241022',
        max_tokens=300,
        messages=[{'role': 'user', 'content': agg_prompt}]
    )
    node.answer = agg.content[0].text
    return node

client = anthropic.Anthropic()
tree = decompose_and_answer(client, 'What are the economic impacts of widespread AI adoption?', max_depth=1)
print('Root answer:', tree.answer[:100] + '...')
print('Subquestions:', [sq.question for sq in tree.subquestions])
```

## Recursive Reward Modeling and Process Supervision

Recursive reward modeling (RRM) trains a reward model at each capability level and uses it to supervise training at the next level. Process reward models (PRMs) reward each intermediate reasoning step rather than only the final answer — this provides much denser training signal and enables catching errors mid-chain before they propagate. OpenAI's Let's Verify Step by Step (Lightman et al. 2023) demonstrated that PRMs trained on human step-level annotations significantly outperform outcome reward models on MATH. PRMs are now the most practically deployed form of scalable oversight, used in o1/o3-style reasoning models.

```python
import anthropic
from typing import Literal

def annotate_reasoning_steps(client, problem, solution):
    # Ask the model to label each reasoning step as correct or incorrect
    steps = [s.strip() for s in solution.strip().split('\n') if s.strip()]
    annotated = []
    for i, step in enumerate(steps):
        prior_steps = '\n'.join(steps[:i])
        prompt = ('Math problem: ' + problem + '\n' +
                  'Reasoning so far:\n' + prior_steps + '\n' +
                  'Next step: ' + step + '\n' +
                  'Is this step correct? Reply: CORRECT or INCORRECT with a one-sentence reason.')
        resp = client.messages.create(
            model='claude-3-5-haiku-20241022',
            max_tokens=120,
            messages=[{'role': 'user', 'content': prompt}]
        )
        label_text = resp.content[0].text.strip()
        label = 'correct' if label_text.upper().startswith('CORRECT') else 'incorrect'
        annotated.append({'step': step, 'label': label, 'reason': label_text})
    return annotated

client = anthropic.Anthropic()
problem = 'Solve: 3x + 7 = 22'
solution = 'Subtract 7 from both sides: 3x = 15\nDivide both sides by 3: x = 5\nCheck: 3(5) + 7 = 22.'
annotations = annotate_reasoning_steps(client, problem, solution)
for ann in annotations:
    print(f"[{ann['label'].upper()}] {ann['step'][:60]}")
print('PRM dataset:', len(annotations), 'step annotations collected')
```

## Self-Critique as Oversight

Self-critique pipelines ask the model to find flaws in its own answer and use critique quality as an oversight signal. Constitutional AI (Anthropic 2022) uses a list of principles to guide self-critique and revision, enabling scalable oversight with minimal human labels. The critique step surfaces potential errors for human review, allowing humans to focus their limited attention on flagged outputs rather than reviewing everything. Self-critique also enables iterative refinement — generate, critique, revise — as an automated self-improvement loop.

```python
import anthropic
from dataclasses import dataclass

@dataclass
class CritiquedResponse:
    question: str
    initial_answer: str
    critique: str
    has_errors: bool
    revised_answer: str

def self_critique_pipeline(client, question):
    # Step 1: generate initial answer
    answer_resp = client.messages.create(
        model='claude-3-5-haiku-20241022',
        max_tokens=400,
        messages=[{'role': 'user', 'content': question}]
    )
    initial = answer_resp.content[0].text
    # Step 2: ask model to critique its own answer
    critique_resp = client.messages.create(
        model='claude-3-5-haiku-20241022',
        max_tokens=300,
        messages=[{'role': 'user', 'content': ('Question: ' + question + '\nAnswer: ' + initial +
                   '\nCritique this answer. List any factual errors, logical flaws, or key omissions. ' +
                   'Start with ERROR if errors found, else LOOKS GOOD.')}]
    )
    critique = critique_resp.content[0].text
    has_errors = critique.upper().startswith('ERROR')
    # Step 3: revise only if errors were flagged
    revised = initial
    if has_errors:
        revise_resp = client.messages.create(
            model='claude-3-5-haiku-20241022',
            max_tokens=400,
            messages=[{'role': 'user', 'content': ('Question: ' + question +
                       '\nOriginal: ' + initial + '\nCritique: ' + critique +
                       '\nProvide a corrected answer.')}]
        )
        revised = revise_resp.content[0].text
    return CritiquedResponse(question, initial, critique, has_errors, revised)

client = anthropic.Anthropic()
result = self_critique_pipeline(client, 'What is the capital of Australia and its approximate population?')
print('Errors found:', result.has_errors)
print('Critique preview:', result.critique[:100] + '...')
```

## Comparing Scalable Oversight Approaches

| Approach | Core Assumption | Human Involvement | Scalability Limit | Current Status |
| --- | --- | --- | --- | --- |
| AI Debate | Humans judge arguments better than generating them; honest agent wins | Judge debates | Requires honest debaters; deceptive AI can exploit | Research — no large-scale deployment |
| Amplification (HCH) | Hard tasks decompose into supervised subtasks recursively | Supervise leaf subproblems | Decomposition must terminate at human-evaluable level | Research — conceptual framework |
| Recursive Reward Modeling | RM at level N supervises training at level N+1 | Label RM training data at each level | RM misspecification compounds across levels | Early research — used in Anthropic RLHF |
| Process Supervision (PRM) | Step-level correctness is evaluable even when final answer is not | Annotate intermediate reasoning steps | Expensive step-level annotation; ambiguous steps | Deployed — used in o1/o3 reasoning models |
| Self-Critique (CAI) | Model critiques are informative signals; principles guide correction | Define critique principles; spot-check | Model may not catch its own systematic errors | Deployed — Constitutional AI in production |

## Limitations and Research Frontiers

All scalable oversight methods share a common limitation: they assume the AI cannot systematically deceive the oversight mechanism. Debate requires honest agents with winning strategies; amplification requires decompositions that don't hide errors; self-critique requires models that can actually detect their own mistakes. As AI systems become more capable, they may learn to game these oversight mechanisms — producing compelling debate arguments for false positions, finding decompositions that obscure errors, or producing critiques that seem thorough but miss real problems. Adversarial robustness of oversight mechanisms is an open research problem.

- Debate assumes truth is verifiable once argued — fails for tasks with no ground truth (e.g., ethical judgment, subjective quality).
- Amplification bottlenecks at the lowest-level subtask: if any leaf subtask exceeds human ability, the oversight chain breaks.
- Recursive reward modeling compounds RM errors — each level's RM inherits inaccuracies from the previous level.
- Process supervision annotation is expensive: Lightman et al. collected 800K step-level labels for the MATH dataset.
- Self-critique fails when the model has systematic blind spots — if the model always generates the same type of error, it cannot self-detect it.

> **Scalable Oversight in Production**: Scalable oversight methods are primarily research directions — current production RLHF still relies on direct human preference labels. Process reward models (PRMs) are the most practically deployed form of scalable oversight, used in o1/o3-style reasoning models to verify each reasoning step and select chains with consistently correct intermediate steps.

---

