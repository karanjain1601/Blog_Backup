---
title: "Special Tokens — BOS, EOS, PAD, Instruction Formats, and Chat Templates"
slug: "special-tokens-llm"
description: "Special tokens are structural vocabulary entries that control sequence boundaries, padding, and instruction formatting. Covers BOS/EOS/PAD roles, instruction format tokens across LLaMA-3/Mistral/ChatML/Alpaca/Gemma, apply_chat_template usage, stop token configuration, and left- vs right-padding strategies."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BlY2lhbCB0b2tlbnMgYXJlIHZvY2FidWxhcnkgZW50cmllcyB3aXRoIHN0cnVjdHVyYWwgcmF0aGVyIHRoYW4gc2VtYW50aWMgcm9sZXMuIFVubGlrZSByZWd1bGFyIHN1YndvcmQgdG9rZW5zIHRoYXQgcmVwcmVzZW50IHRleHQgZnJhZ21lbnRzLCBzcGVjaWFsIHRva2VucyBzaWduYWwgc2VxdWVuY2UgYm91bmRhcmllcywgc2VwYXJhdGUgY29udmVyc2F0aW9uIHR1cm5zLCBpbmRpY2F0ZSBwYWRkaW5nIHBvc2l0aW9ucywgYW5kIHRyaWdnZXIgc3BlY2lmaWMgbW9kZWwgYmVoYXZpb3JzLiBFdmVyeSBtYWpvciBsYW5ndWFnZSBtb2RlbCBmYW1pbHkgZGVmaW5lcyBhIGRpc3RpbmN0IHNldCBvZiBzcGVjaWFsIHRva2VucyBhbmQgYW4gaW5zdHJ1Y3Rpb24gZm9ybWF0IHRoYXQgdGhlIG1vZGVsIGhhcyBiZWVuIHRyYWluZWQgdG8gcmVjb2duaXNlLiBNaXNtYXRjaGluZyB0aGVzZSB0b2tlbnMgYXQgaW5mZXJlbmNlIHRpbWUg4oCUIHVzaW5nIHRoZSB3cm9uZyBjaGF0IHRlbXBsYXRlLCB3cm9uZyBCT1MgdG9rZW4sIG9yIHdyb25nIHN0b3AgY29uZGl0aW9uIOKAlCBjYXVzZXMgc2V2ZXJlIHF1YWxpdHkgZGVncmFkYXRpb24gZXZlbiB3aGVuIHRoZSBzZW1hbnRpYyBjb250ZW50IG9mIHRoZSBwcm9tcHQgaXMgY29ycmVjdC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJCT1MsIEVPUywgUEFEIOKAlCBDb3JlIFN0cnVjdHVyYWwgVG9rZW5zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCT1MgKGJlZ2lubmluZyBvZiBzZXF1ZW5jZSkgaXMgcHJlcGVuZGVkIHRvIGV2ZXJ5IGlucHV0IHNlcXVlbmNlIGFuZCBzaWduYWxzIHRvIHRoZSBtb2RlbCB3aGVyZSB0ZXh0IGJlZ2lucy4gRU9TIChlbmQgb2Ygc2VxdWVuY2UpIHNpZ25hbHMgdGhlIG1vZGVsIHRvIHN0b3AgZ2VuZXJhdGluZzsgaXQgaXMgYWxzbyB0aGUgdG9rZW4gdGhlIG1vZGVsIGlzIHRyYWluZWQgdG8gcHJlZGljdCBhdCB0aGUgZW5kIG9mIGl0cyBvdXRwdXQuIFdpdGhvdXQgYSBwcm9wZXJseSByZWNvZ25pc2VkIEVPUyB0b2tlbiBpbiB0aGUgc3RvcHBpbmcgY3JpdGVyaWEsIGRlY29kZXItb25seSBtb2RlbHMgY29udGludWUgZ2VuZXJhdGluZyBwYXN0IHRoZSBpbnRlbmRlZCBvdXRwdXQgdW50aWwgdGhleSBoaXQgdGhlIGNvbnRleHQgbGltaXQuIFBBRCBmaWxscyBzaG9ydGVyIHNlcXVlbmNlcyBpbiBhIGJhdGNoIHRvIG1hdGNoIHRoZSBtYXhpbXVtIHNlcXVlbmNlIGxlbmd0aDsgUEFEIHRva2VucyBhcmUgbWFza2VkIGluIHRoZSBhdHRlbnRpb24gY29tcHV0YXRpb24gc28gdGhleSBkbyBub3QgaW5mbHVlbmNlIGxvc3Mgb3IgbG9naXRzLiBTRVAgc2VwYXJhdGVzIHNlZ21lbnRzIGluIGVuY29kZXIgbW9kZWxzIGxpa2UgQkVSVDsgQ0xTIGlzIHByZXBlbmRlZCBhcyB0aGUgY2xhc3NpZmljYXRpb24gdG9rZW4gd2hvc2UgZmluYWwtbGF5ZXIgcmVwcmVzZW50YXRpb24gaXMgdXNlZCBmb3Igc2VxdWVuY2UtbGV2ZWwgdGFza3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSW5zdHJ1Y3Rpb24gRm9ybWF0IFRva2VucyBieSBNb2RlbCBGYW1pbHkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxMYU1BLTMgdXNlcyBcdTAwM2N8YmVnaW5fb2ZfdGV4dHxcdTAwM2UgYXMgQk9TLCBcdTAwM2N8ZW90X2lkfFx1MDAzZSB0byBtYXJrIGVuZC1vZi10dXJuLCBcdTAwM2N8c3RhcnRfaGVhZGVyX2lkfFx1MDAzZSBhbmQgXHUwMDNjfGVuZF9oZWFkZXJfaWR8XHUwMDNlIHRvIGRlbGltaXQgcm9sZSBoZWFkZXJzIChzeXN0ZW0sIHVzZXIsIGFzc2lzdGFudCksIGFuZCBcdTAwM2N8ZW5kX29mX3RleHR8XHUwMDNlIGFzIEVPUy4gQ2hhdE1MICh1c2VkIGJ5IEdQVC00IGFuZCBtYW55IG9wZW4gbW9kZWxzKSB1c2VzIFx1MDAzY3xpbV9zdGFydHxcdTAwM2Vyb2xlXFxuLi4uY29udGVudC4uLlx1MDAzY3xpbV9lbmR8XHUwMDNlIGZvciBlYWNoIHR1cm4uIE1pc3RyYWwvTWl4dHJhbCB1c2VzIFx1MDAzY3NcdTAwM2UgYXMgQk9TLCBbSU5TVF0gYW5kIFsvSU5TVF0gdG8gZGVsaW1pdCB1c2VyIHR1cm5zLCBhbmQgXHUwMDNjL3NcdTAwM2UgYXMgRU9TIHdpdGggbm8gZXhwbGljaXQgc3lzdGVtIHRva2VuIOKAlCBzeXN0ZW0gcHJvbXB0cyBhcmUgcHJlcGVuZGVkIHRvIHRoZSBmaXJzdCB1c2VyIG1lc3NhZ2UuIEFscGFjYSBmb3JtYXQgdXNlcyBodW1hbi1yZWFkYWJsZSBkZWxpbWl0ZXJzOiAjIyMgSW5zdHJ1Y3Rpb246XFxuLi4uXFxuIyMjIFJlc3BvbnNlOlxcbiB3aXRoIGdlbmVyYXRpb24gc3RvcHBpbmcgb24gdGhlIG5leHQgIyMjIG1hcmtlci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbnNwZWN0aW5nIFNwZWNpYWwgVG9rZW5zIEFjcm9zcyBNb2RlbCBGYW1pbGllcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG5kZWYgaW5zcGVjdF9zcGVjaWFsX3Rva2Vucyhtb2RlbF9uYW1lKTpcbiAgICB0b2sgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lLCB0cnVzdF9yZW1vdGVfY29kZT1UcnVlKVxuICAgIHByaW50KGZcdTAwMjdcXG49PT0ge21vZGVsX25hbWV9ID09PVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBib3NfdG9rZW46ICAgICAgIHtyZXByKHRvay5ib3NfdG9rZW4pfSAoaWQ9e3Rvay5ib3NfdG9rZW5faWR9KVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBlb3NfdG9rZW46ICAgICAgIHtyZXByKHRvay5lb3NfdG9rZW4pfSAoaWQ9e3Rvay5lb3NfdG9rZW5faWR9KVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBwYWRfdG9rZW46ICAgICAgIHtyZXByKHRvay5wYWRfdG9rZW4pfSAoaWQ9e3Rvay5wYWRfdG9rZW5faWR9KVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICB1bmtfdG9rZW46ICAgICAgIHtyZXByKHRvay51bmtfdG9rZW4pfSAoaWQ9e3Rvay51bmtfdG9rZW5faWR9KVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBzZXBfdG9rZW46ICAgICAgIHtyZXByKHRvay5zZXBfdG9rZW4pfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBhbGxfc3BlY2lhbF90b2tlbnMgKHtsZW4odG9rLmFsbF9zcGVjaWFsX3Rva2Vucyl9IHRvdGFsKTpcdTAwMjcpXG4gICAgZm9yIHN0IGluIHRvay5hbGxfc3BlY2lhbF90b2tlbnNbOjEwXTpcbiAgICAgICAgc2lkID0gdG9rLmNvbnZlcnRfdG9rZW5zX3RvX2lkcyhzdClcbiAgICAgICAgcHJpbnQoZlx1MDAyNyAgICB7cmVwcihzdCk6XHUwMDNjNDB9IGlkPXtzaWR9XHUwMDI3KVxuICAgIGlmIGhhc2F0dHIodG9rLCBcdTAwMjdjaGF0X3RlbXBsYXRlXHUwMDI3KSBhbmQgdG9rLmNoYXRfdGVtcGxhdGU6XG4gICAgICAgIHByZXZpZXcgPSB0b2suY2hhdF90ZW1wbGF0ZVs6ODBdLnJlcGxhY2UoXHUwMDI3XFxuXHUwMDI3LCBcdTAwMjcgXHUwMDI3KVxuICAgICAgICBwcmludChmXHUwMDI3ICBjaGF0X3RlbXBsYXRlOiB7cHJldmlld30uLi5cdTAwMjcpXG5cbm1vZGVscyA9IFtcbiAgICBcdTAwMjdtZXRhLWxsYW1hL01ldGEtTGxhbWEtMy04Qi1JbnN0cnVjdFx1MDAyNyxcbiAgICBcdTAwMjdtaXN0cmFsYWkvTWlzdHJhbC03Qi1JbnN0cnVjdC12MC4yXHUwMDI3LFxuICAgIFx1MDAyN2dvb2dsZS9nZW1tYS03Yi1pdFx1MDAyNyxcbl1cbmZvciBtb2RlbCBpbiBtb2RlbHM6XG4gICAgdHJ5OlxuICAgICAgICBpbnNwZWN0X3NwZWNpYWxfdG9rZW5zKG1vZGVsKVxuICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZTpcbiAgICAgICAgcHJpbnQoZlx1MDAyN3ttb2RlbH06IHtlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDaGF0IFRlbXBsYXRlIEFwcGxpY2F0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIdWdnaW5nRmFjZSB0b2tlbml6ZXJzIGV4cG9zZSBhcHBseV9jaGF0X3RlbXBsYXRlKCksIHdoaWNoIGZvcm1hdHMgYSBsaXN0IG9mIHJvbGUtY29udGVudCBkaWN0aW9uYXJpZXMgaW50byB0aGUgbW9kZWwtc3BlY2lmaWMgaW5zdHJ1Y3Rpb24gZm9ybWF0LiBUaGUgdGVtcGxhdGUgaXMgc3RvcmVkIGluIHRoZSB0b2tlbml6ZXJcdTAwMjdzIHRva2VuaXplcl9jb25maWcuanNvbiBhcyBhIEppbmphMiB0ZW1wbGF0ZSBzdHJpbmcuIENhbGxpbmcgYXBwbHlfY2hhdF90ZW1wbGF0ZSgpIHdpdGggYWRkX2dlbmVyYXRpb25fcHJvbXB0PVRydWUgYXBwZW5kcyB0aGUgYXNzaXN0YW50IGhlYWRlciB0b2tlbiwgcHJpbWluZyB0aGUgbW9kZWwgZm9yIHJlc3BvbnNlIGdlbmVyYXRpb24uIFVzaW5nIHRoaXMgbWV0aG9kIGd1YXJhbnRlZXMgY29ycmVjdCBmb3JtYXR0aW5nIHJlZ2FyZGxlc3Mgb2YgbW9kZWwgZmFtaWx5IOKAlCB0aGUgc2FtZSBQeXRob24gY29kZSB3b3JrcyBmb3IgTExhTUEtMywgTWlzdHJhbCwgYW5kIEdlbW1hIGJ5IHN3aXRjaGluZyBvbmx5IHRoZSBtb2RlbCBuYW1lLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG5kZWYgZm9ybWF0X2NvbnZlcnNhdGlvbihtb2RlbF9uYW1lLCBzeXN0ZW1fbXNnLCB1c2VyX21zZywgYXNzaXN0YW50X21zZz1Ob25lKTpcbiAgICB0b2sgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgIG1lc3NhZ2VzID0gW11cbiAgICBpZiBzeXN0ZW1fbXNnOlxuICAgICAgICBtZXNzYWdlcy5hcHBlbmQoe1x1MDAyN3JvbGVcdTAwMjc6IFx1MDAyN3N5c3RlbVx1MDAyNywgXHUwMDI3Y29udGVudFx1MDAyNzogc3lzdGVtX21zZ30pXG4gICAgbWVzc2FnZXMuYXBwZW5kKHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjd1c2VyXHUwMDI3LCBcdTAwMjdjb250ZW50XHUwMDI3OiB1c2VyX21zZ30pXG4gICAgaWYgYXNzaXN0YW50X21zZzpcbiAgICAgICAgbWVzc2FnZXMuYXBwZW5kKHtcdTAwMjdyb2xlXHUwMDI3OiBcdTAwMjdhc3Npc3RhbnRcdTAwMjcsIFx1MDAyN2NvbnRlbnRcdTAwMjc6IGFzc2lzdGFudF9tc2d9KVxuICAgIGZvcm1hdHRlZCA9IHRvay5hcHBseV9jaGF0X3RlbXBsYXRlKFxuICAgICAgICBtZXNzYWdlcyxcbiAgICAgICAgdG9rZW5pemU9RmFsc2UsXG4gICAgICAgIGFkZF9nZW5lcmF0aW9uX3Byb21wdD0oYXNzaXN0YW50X21zZyBpcyBOb25lKSxcbiAgICApXG4gICAgdG9rZW5faWRzID0gdG9rLmFwcGx5X2NoYXRfdGVtcGxhdGUoXG4gICAgICAgIG1lc3NhZ2VzLFxuICAgICAgICB0b2tlbml6ZT1UcnVlLFxuICAgICAgICBhZGRfZ2VuZXJhdGlvbl9wcm9tcHQ9KGFzc2lzdGFudF9tc2cgaXMgTm9uZSksXG4gICAgICAgIHJldHVybl90ZW5zb3JzPVx1MDAyN3B0XHUwMDI3LFxuICAgIClcbiAgICByZXR1cm4gZm9ybWF0dGVkLCB0b2tlbl9pZHNcblxuc3lzdGVtID0gXHUwMDI3WW91IGFyZSBhIGhlbHBmdWwgYXNzaXN0YW50IHNwZWNpYWxpc2luZyBpbiBtYWNoaW5lIGxlYXJuaW5nLlx1MDAyN1xudXNlciA9IFx1MDAyN0V4cGxhaW4gdGhlIGRpZmZlcmVuY2UgYmV0d2VlbiBCUEUgYW5kIFdvcmRQaWVjZSB0b2tlbml6YXRpb24uXHUwMDI3XG5tb2RlbHMgPSBbXHUwMDI3bWV0YS1sbGFtYS9NZXRhLUxsYW1hLTMtOEItSW5zdHJ1Y3RcdTAwMjcsIFx1MDAyN21pc3RyYWxhaS9NaXN0cmFsLTdCLUluc3RydWN0LXYwLjJcdTAwMjddXG5mb3IgbW9kZWwgaW4gbW9kZWxzOlxuICAgIHRyeTpcbiAgICAgICAgdGV4dCwgaWRzID0gZm9ybWF0X2NvbnZlcnNhdGlvbihtb2RlbCwgc3lzdGVtLCB1c2VyKVxuICAgICAgICBwcmludChmXHUwMDI3e21vZGVsfTpcdTAwMjcpXG4gICAgICAgIHByaW50KGZcdTAwMjcgIFRva2VuIGNvdW50OiB7aWRzLnNoYXBlWy0xXX1cdTAwMjcpXG4gICAgICAgIHByaW50KGZcdTAwMjcgIEZpcnN0IDIwMCBjaGFyczoge3RleHRbOjIwMF19XHUwMDI3KVxuICAgICAgICBwcmludCgpXG4gICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOlxuICAgICAgICBwcmludChmXHUwMDI3e21vZGVsfToge2V9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdlbmVyYXRpb24gU3RvcCBUb2tlbiBDb25maWd1cmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb3JyZWN0IHN0b3AgdG9rZW4gY29uZmlndXJhdGlvbiBpcyBlc3NlbnRpYWwgZm9yIGluZmVyZW5jZS4gVGhlIG1vZGVsXHUwMDI3cyBnZW5lcmF0ZSgpIG1ldGhvZCBhY2NlcHRzIGVvc190b2tlbl9pZCBhcyBhIHNpbmdsZSB0b2tlbiBpZCBvciBhIGxpc3Qgb2YgaWRzOyBnZW5lcmF0aW9uIGhhbHRzIHdoZW4gYW55IG9mIHRoZXNlIGlkcyBpcyBwcm9kdWNlZC4gRm9yIG1vZGVscyB3aXRoIG11bHRpcGxlIHN0b3AgdG9rZW5zIChMTGFNQS0zIGhhcyBib3RoIFx1MDAzY3xlb3RfaWR8XHUwMDNlIGFuZCBcdTAwM2N8ZW5kX29mX3RleHR8XHUwMDNlKSwgYWxsIHZhbGlkIHN0b3AgaWRzIG11c3QgYmUgaW5jbHVkZWQgb3IgdGhlIG1vZGVsIHdpbGwgY29udGludWUgZ2VuZXJhdGluZyBwYXN0IHRoZSBpbnRlbmRlZCB0dXJuIGJvdW5kYXJ5LiBUaGUgc3RvcHBpbmdfY3JpdGVyaWEgYXJndW1lbnQgYWNjZXB0cyBjdXN0b20gU3RvcHBpbmdDcml0ZXJpYSBzdWJjbGFzc2VzIGZvciBwYXR0ZXJuLWJhc2VkIHN0b3BwaW5nLCB1c2VmdWwgd2hlbiBzdG9wIHNlcXVlbmNlcyBzcGFuIG11bHRpcGxlIHRva2Vucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplciwgQXV0b01vZGVsRm9yQ2F1c2FsTE0sIFN0b3BwaW5nQ3JpdGVyaWEsIFN0b3BwaW5nQ3JpdGVyaWFMaXN0XG5cbmNsYXNzIE11bHRpVG9rZW5TdG9wQ3JpdGVyaWEoU3RvcHBpbmdDcml0ZXJpYSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHN0b3BfdG9rZW5faWRzKTpcbiAgICAgICAgc2VsZi5zdG9wX2lkcyA9IHNldChzdG9wX3Rva2VuX2lkcylcblxuICAgIGRlZiBfX2NhbGxfXyhzZWxmLCBpbnB1dF9pZHMsIHNjb3JlcywgKiprd2FyZ3MpOlxuICAgICAgICBsYXN0X3Rva2VuID0gaW5wdXRfaWRzWzAsIC0xXS5pdGVtKClcbiAgICAgICAgcmV0dXJuIGxhc3RfdG9rZW4gaW4gc2VsZi5zdG9wX2lkc1xuXG5kZWYgY29uZmlndXJlX2dlbmVyYXRpb24obW9kZWxfbmFtZSwgcHJvbXB0KTpcbiAgICB0b2sgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgICMgQ29sbGVjdCBhbGwgdmFsaWQgc3RvcCB0b2tlbiBpZHMgZm9yIHRoaXMgbW9kZWxcbiAgICBzdG9wX2lkcyA9IFtdXG4gICAgZm9yIHNwZWNpYWwgaW4gW3Rvay5lb3NfdG9rZW4sIFx1MDAyN1x1MDAzY3xlb3RfaWR8XHUwMDNlXHUwMDI3LCBcdTAwMjdcdTAwM2N8ZW5kX29mX3RleHR8XHUwMDNlXHUwMDI3LCBcdTAwMjdcdTAwM2Mvc1x1MDAzZVx1MDAyNywgXHUwMDI3XHUwMDNjfGltX2VuZHxcdTAwM2VcdTAwMjddOlxuICAgICAgICBpZiBzcGVjaWFsIGFuZCBzcGVjaWFsIGluIHRvay5nZXRfdm9jYWIoKTpcbiAgICAgICAgICAgIHN0b3BfaWRzLmFwcGVuZCh0b2suY29udmVydF90b2tlbnNfdG9faWRzKHNwZWNpYWwpKVxuICAgIHN0b3BfY3JpdGVyaWEgPSBTdG9wcGluZ0NyaXRlcmlhTGlzdChbTXVsdGlUb2tlblN0b3BDcml0ZXJpYShzdG9wX2lkcyldKVxuICAgIHByaW50KGZcdTAwMjd7bW9kZWxfbmFtZX06XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIFN0b3AgdG9rZW4gaWRzOiB7c3RvcF9pZHN9XHUwMDI3KVxuICAgIHN0b3BfdG9rZW5zID0gW3Rvay5jb252ZXJ0X2lkc190b190b2tlbnMoc2lkKSBmb3Igc2lkIGluIHN0b3BfaWRzXVxuICAgIHByaW50KGZcdTAwMjcgIFN0b3AgdG9rZW5zOiAgICB7c3RvcF90b2tlbnN9XHUwMDI3KVxuICAgIHJldHVybiBzdG9wX2NyaXRlcmlhXG5cbmZvciBtb2RlbCBpbiBbXHUwMDI3bWV0YS1sbGFtYS9NZXRhLUxsYW1hLTMtOEJcdTAwMjcsIFx1MDAyN21pc3RyYWxhaS9NaXN0cmFsLTdCLXYwLjFcdTAwMjddOlxuICAgIHRyeTpcbiAgICAgICAgY29uZmlndXJlX2dlbmVyYXRpb24obW9kZWwsIFx1MDAyN3Rlc3RcdTAwMjcpXG4gICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOlxuICAgICAgICBwcmludChmXHUwMDI3e21vZGVsfToge2V9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBhZGRpbmcgU3RyYXRlZ3kgZm9yIEJhdGNoZWQgSW5mZXJlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZWNvZGVyLW9ubHkgbW9kZWxzIChHUFQsIExMYU1BLCBNaXN0cmFsKSB1c2UgbGVmdC1wYWRkaW5nIGZvciBiYXRjaGVkIGdlbmVyYXRpb246IFBBRCB0b2tlbnMgYXJlIHByZXBlbmRlZCBzbyB0aGF0IGFsbCBzZXF1ZW5jZXMgaW4gYSBiYXRjaCBlbmQgYXQgdGhlIHNhbWUgcG9zaXRpb24sIGFsbG93aW5nIHRoZSBtb2RlbFx1MDAyN3MgYXV0b3JlZ3Jlc3NpdmUgZ2VuZXJhdGlvbiB0byBiZWdpbiBhdCBpZGVudGljYWwgcG9zaXRpb25zIGFjcm9zcyBiYXRjaCBlbGVtZW50cy4gUmlnaHQtcGFkZGluZyBpcyB1c2VkIGZvciBlbmNvZGVyIHRyYWluaW5nIChCRVJULCBSb0JFUlRhKSBhbmQgZm9yIGNvbXB1dGluZyBsb3NzIG9uIHZhcmlhYmxlLWxlbmd0aCBzZXF1ZW5jZXM6IHBhZGRpbmcgaXMgYXBwZW5kZWQgYW5kIG1hc2tlZCB2aWEgYXR0ZW50aW9uX21hc2suIFVzaW5nIHJpZ2h0LXBhZGRpbmcgd2l0aCBhIGRlY29kZXItb25seSBtb2RlbCBkdXJpbmcgZ2VuZXJhdGlvbiBjYXVzZXMgaW5jb3JyZWN0IG91dHB1dCBiZWNhdXNlIHRoZSBtb2RlbCBzZWVzIFBBRCB0b2tlbnMgYmV0d2VlbiB0aGUgcHJvbXB0IGVuZCBhbmQgdGhlIGZpcnN0IGdlbmVyYXRlZCB0b2tlbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplclxuXG5kZWYgZGVtb25zdHJhdGVfcGFkZGluZyhtb2RlbF9uYW1lLCBwcm9tcHRzKTpcbiAgICB0b2sgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgIGlmIHRvay5wYWRfdG9rZW4gaXMgTm9uZTpcbiAgICAgICAgdG9rLnBhZF90b2tlbiA9IHRvay5lb3NfdG9rZW5cblxuICAgICMgTGVmdC1wYWRkaW5nOiBjb3JyZWN0IGZvciBkZWNvZGVyLW9ubHkgZ2VuZXJhdGlvblxuICAgIHRvay5wYWRkaW5nX3NpZGUgPSBcdTAwMjdsZWZ0XHUwMDI3XG4gICAgbGVmdF9iYXRjaCA9IHRvayhwcm9tcHRzLCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNywgcGFkZGluZz1UcnVlLCB0cnVuY2F0aW9uPVRydWUpXG4gICAgcHJpbnQoZlx1MDAyN0xlZnQtcGFkZGluZyAoZGVjb2RlciBnZW5lcmF0aW9uKTpcdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyNyAgaW5wdXRfaWRzIHNoYXBlOiAgICAgIHtsZWZ0X2JhdGNoLmlucHV0X2lkcy5zaGFwZX1cdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyNyAgYXR0ZW50aW9uX21hc2sgc2hhcGU6IHtsZWZ0X2JhdGNoLmF0dGVudGlvbl9tYXNrLnNoYXBlfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBGaXJzdCBzZXF1ZW5jZSBpZHM6ICAge2xlZnRfYmF0Y2guaW5wdXRfaWRzWzBdLnRvbGlzdCgpfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3ICBGaXJzdCBzZXEgbWFzazogICAgICAge2xlZnRfYmF0Y2guYXR0ZW50aW9uX21hc2tbMF0udG9saXN0KCl9XHUwMDI3KVxuXG4gICAgIyBSaWdodC1wYWRkaW5nOiBjb3JyZWN0IGZvciBlbmNvZGVyIHRyYWluaW5nXG4gICAgdG9rLnBhZGRpbmdfc2lkZSA9IFx1MDAyN3JpZ2h0XHUwMDI3XG4gICAgcmlnaHRfYmF0Y2ggPSB0b2socHJvbXB0cywgcmV0dXJuX3RlbnNvcnM9XHUwMDI3cHRcdTAwMjcsIHBhZGRpbmc9VHJ1ZSwgdHJ1bmNhdGlvbj1UcnVlKVxuICAgIHByaW50KGZcdTAwMjdSaWdodC1wYWRkaW5nIChlbmNvZGVyIHRyYWluaW5nKTpcdTAwMjcpXG4gICAgcHJpbnQoZlx1MDAyNyAgRmlyc3Qgc2VxdWVuY2UgaWRzOiAgIHtyaWdodF9iYXRjaC5pbnB1dF9pZHNbMF0udG9saXN0KCl9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjcgIEZpcnN0IHNlcSBtYXNrOiAgICAgICB7cmlnaHRfYmF0Y2guYXR0ZW50aW9uX21hc2tbMF0udG9saXN0KCl9XHUwMDI3KVxuXG5zaG9ydF9wcm9tcHRzID0gW1x1MDAyN0hpXHUwMDI3LCBcdTAwMjdFeHBsYWluIEJQRSB0b2tlbml6YXRpb24gaW4gZGV0YWlsIHBsZWFzZS5cdTAwMjddXG5kZW1vbnN0cmF0ZV9wYWRkaW5nKFx1MDAyN2dwdDJcdTAwMjcsIHNob3J0X3Byb21wdHMpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3BlY2lhbCBUb2tlbiBGb3JtYXRzIGJ5IE1vZGVsIEZhbWlseSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNb2RlbCBGYW1pbHkiLCJCT1MgVG9rZW4iLCJUdXJuIERlbGltaXRlciIsIkVPUyBUb2tlbiIsIlN5c3RlbSBSb2xlIEZvcm1hdCJdLCJyb3dzIjpbWyJMTGFNQS0zIiwiXHUwMDNjfGJlZ2luX29mX3RleHR8XHUwMDNlIiwiXHUwMDNjfGVvdF9pZHxcdTAwM2UgKyBcdTAwM2N8c3RhcnRfaGVhZGVyX2lkfFx1MDAzZXJvbGVcdTAwM2N8ZW5kX2hlYWRlcl9pZHxcdTAwM2UiLCJcdTAwM2N8ZW5kX29mX3RleHR8XHUwMDNlIiwiXHUwMDNjfHN0YXJ0X2hlYWRlcl9pZHxcdTAwM2VzeXN0ZW1cdTAwM2N8ZW5kX2hlYWRlcl9pZHxcdTAwM2VcXG57Y29udGVudH1cdTAwM2N8ZW90X2lkfFx1MDAzZSJdLFsiTWlzdHJhbC9NaXh0cmFsIiwiXHUwMDNjc1x1MDAzZSIsIltJTlNUXSAvIFsvSU5TVF0iLCJcdTAwM2Mvc1x1MDAzZSIsIk5vIHN5c3RlbSB0YWcg4oCUIHByZXBlbmQgdG8gZmlyc3QgdXNlciBtZXNzYWdlIGluc2lkZSBbSU5TVF0iXSxbIkNoYXRNTCAoR1BULTQpIiwiXHUwMDNjfGltX3N0YXJ0fFx1MDAzZSIsIlx1MDAzY3xpbV9lbmR8XHUwMDNlXFxuXHUwMDNjfGltX3N0YXJ0fFx1MDAzZXJvbGVcXG4iLCJcdTAwM2N8ZW5kb2Z0ZXh0fFx1MDAzZSIsIlx1MDAzY3xpbV9zdGFydHxcdTAwM2VzeXN0ZW1cXG57Y29udGVudH1cdTAwM2N8aW1fZW5kfFx1MDAzZSJdLFsiQWxwYWNhIiwiTm9uZSIsIiMjIyBJbnN0cnVjdGlvbjpcXG4gLyAjIyMgUmVzcG9uc2U6XFxuIiwiU3RvcCBvbiBuZXh0ICMjIyAocGF0dGVybi1iYXNlZCkiLCIjIyMgU3lzdGVtIFByb21wdDpcXG57Y29udGVudH1cXG5cXG4iXSxbIkdlbW1hIiwiXHUwMDNjYm9zXHUwMDNlIiwiXHUwMDNjc3RhcnRfb2ZfdHVyblx1MDAzZXJvbGVcXG4gLyBcdTAwM2NlbmRfb2ZfdHVyblx1MDAzZVxcbiIsIlx1MDAzY2Vvc1x1MDAzZSIsIlx1MDAzY3N0YXJ0X29mX3R1cm5cdTAwM2V1c2VyXFxue3N5c3RlbSt1c2VyfVx1MDAzY2VuZF9vZl90dXJuXHUwMDNlIl1dfSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN5c3RlbSBwcm9tcHRzIGVuY29kZSB0aGUgbW9kZWxcdTAwMjdzIHBlcnNvbmEsIGNvbnN0cmFpbnRzLCBhbmQgdGFzayBjb250ZXh0LiBJbiBMTGFNQS0zIHRoZXkgYXJlIHBsYWNlZCBpbiBhIGRlZGljYXRlZCBzeXN0ZW0gaGVhZGVyIGJlZm9yZSB0aGUgZmlyc3QgdXNlciB0dXJuLiBJbiBNaXN0cmFsIHRoZXkgYXJlIGNvbmNhdGVuYXRlZCB0byB0aGUgZmlyc3QgdXNlciBtZXNzYWdlIGluc2lkZSBbSU5TVF0gYnJhY2tldHMuIEluIEdlbW1hLCB0aGVyZSBpcyBubyBzZXBhcmF0ZSBzeXN0ZW0gcm9sZTsgc3lzdGVtIGNvbnRleHQgaXMgcHJlcGVuZGVkIHRvIHRoZSB1c2VyIGNvbnRlbnQgaW4gdGhlIGZpcnN0IHR1cm4uIFRoZXNlIGRpZmZlcmVuY2VzIG1lYW4gdGhhdCBhIHN5c3RlbSBwcm9tcHQgd29ya2luZyBjb3JyZWN0bHkgd2l0aCBvbmUgbW9kZWwgZmFtaWx5IG1heSBwcm9kdWNlIGRpZmZlcmVudCBiZWhhdmlvciBvbiBhbm90aGVyIGV2ZW4gaWYgdGhlIHdvcmRzIGFyZSBpZGVudGljYWwg4oCUIHRoZSBtb2RlbCBoYXMgbGVhcm5lZCB0byByZXNwb25kIHRvIGl0cyBzcGVjaWZpYyBzdHJ1Y3R1cmFsIGRlbGltaXRlcnMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJXcm9uZyBDaGF0IFRlbXBsYXRlIENhdXNlcyBJbmNvaGVyZW50IE91dHB1dHMiLCJjb250ZW50IjoiVXNpbmcgdGhlIHdyb25nIGNoYXQgdGVtcGxhdGUgZm9yIGEgbW9kZWwgY2F1c2VzIGRyYW1hdGljIHF1YWxpdHkgZGVncmFkYXRpb24g4oCUIG1vZGVscyBhcmUgdHJhaW5lZCB0byByZWNvZ25pc2Ugc3BlY2lmaWMgZGVsaW1pdGVyIHRva2VucyBhcm91bmQgZWFjaCB0dXJuLCBhbmQgbWlzbWF0Y2hlZCB0ZW1wbGF0ZXMgcHJvZHVjZSBpbmNvaGVyZW50IG91dHB1dHMgZXZlbiB3aXRoIGNvcnJlY3QgY29udGVudC4gQWx3YXlzIHVzZSBhcHBseV9jaGF0X3RlbXBsYXRlKCkgZnJvbSB0aGUgbW9kZWxcdTAwMjdzIG93biB0b2tlbml6ZXIgcmF0aGVyIHRoYW4gaGFuZC1jb25zdHJ1Y3RpbmcgcHJvbXB0IHN0cmluZ3MuIElmIHRoZSB0b2tlbml6ZXIgbGFja3MgYSBjaGF0X3RlbXBsYXRlIGZpZWxkIChvbGRlciBtb2RlbHMpLCBjaGVjayB0aGUgbW9kZWwgY2FyZCBmb3IgdGhlIGV4YWN0IGZvcm1hdCB1c2VkIGR1cmluZyBpbnN0cnVjdGlvbiB0dW5pbmcuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJBbHdheXMgdXNlIGFwcGx5X2NoYXRfdGVtcGxhdGUoKSDigJQgbmV2ZXIgaGFuZC1jb25zdHJ1Y3QgaW5zdHJ1Y3Rpb24gcHJvbXB0cyBmb3IgaW5zdHJ1Y3Rpb24tdHVuZWQgbW9kZWxzLiIsIlNldCBlb3NfdG9rZW5faWQgdG8gQUxMIHZhbGlkIHN0b3AgdG9rZW4gaWRzIGZvciB0aGUgbW9kZWwgZmFtaWx5IHRvIHByZXZlbnQgcnVuYXdheSBnZW5lcmF0aW9uLiIsIlVzZSBsZWZ0LXBhZGRpbmcgZm9yIGRlY29kZXItb25seSBnZW5lcmF0aW9uIGJhdGNoZXM7IHVzZSByaWdodC1wYWRkaW5nIGZvciBlbmNvZGVyIHRyYWluaW5nLiIsIlBBRCB0b2tlbiBtdXN0IGJlIHNldCBmb3IgbW9kZWxzIHRoYXQgbGFjayBvbmUgKEdQVC0yKTogc2V0IHBhZF90b2tlbiA9IGVvc190b2tlbiBhbmQgbWFzayBpdCBpbiBhdHRlbnRpb25fbWFzay4iLCJMTGFNQS0zIGhhcyB0d28gc3RvcCB0b2tlbnM6IFx1MDAzY3xlb3RfaWR8XHUwMDNlIGVuZHMgYSB0dXJuLCBcdTAwM2N8ZW5kX29mX3RleHR8XHUwMDNlIGVuZHMgdGhlIGRvY3VtZW50IOKAlCBib3RoIG11c3QgYmUgaW4gc3RvcCBpZHMuIiwiVG9vbCBjYWxsIHRva2VucyBpbiBmdW5jdGlvbi1jYWxsaW5nIG1vZGVscyAoZS5nLiwgXHUwMDNjdG9vbF9jYWxsXHUwMDNlLCBcdTAwM2N8cHl0aG9uX3RhZ3xcdTAwM2UpIGFyZSBhZGRpdGlvbmFsIHNwZWNpYWwgdG9rZW5zIHRvIHJlZ2lzdGVyLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Special Tokens — BOS, EOS, PAD, Instruction Formats, and Chat Templates

Special tokens are vocabulary entries with structural rather than semantic roles. Unlike regular subword tokens that represent text fragments, special tokens signal sequence boundaries, separate conversation turns, indicate padding positions, and trigger specific model behaviors. Every major language model family defines a distinct set of special tokens and an instruction format that the model has been trained to recognise. Mismatching these tokens at inference time — using the wrong chat template, wrong BOS token, or wrong stop condition — causes severe quality degradation even when the semantic content of the prompt is correct.

## BOS, EOS, PAD — Core Structural Tokens

BOS (beginning of sequence) is prepended to every input sequence and signals to the model where text begins. EOS (end of sequence) signals the model to stop generating; it is also the token the model is trained to predict at the end of its output. Without a properly recognised EOS token in the stopping criteria, decoder-only models continue generating past the intended output until they hit the context limit. PAD fills shorter sequences in a batch to match the maximum sequence length; PAD tokens are masked in the attention computation so they do not influence loss or logits. SEP separates segments in encoder models like BERT; CLS is prepended as the classification token whose final-layer representation is used for sequence-level tasks.

## Instruction Format Tokens by Model Family

LLaMA-3 uses <|begin_of_text|> as BOS, <|eot_id|> to mark end-of-turn, <|start_header_id|> and <|end_header_id|> to delimit role headers (system, user, assistant), and <|end_of_text|> as EOS. ChatML (used by GPT-4 and many open models) uses <|im_start|>role\n...content...<|im_end|> for each turn. Mistral/Mixtral uses <s> as BOS, [INST] and [/INST] to delimit user turns, and </s> as EOS with no explicit system token — system prompts are prepended to the first user message. Alpaca format uses human-readable delimiters: ### Instruction:\n...\n### Response:\n with generation stopping on the next ### marker.

## Inspecting Special Tokens Across Model Families

```python
from transformers import AutoTokenizer

def inspect_special_tokens(model_name):
    tok = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    print(f'\n=== {model_name} ===')
    print(f'  bos_token:       {repr(tok.bos_token)} (id={tok.bos_token_id})')
    print(f'  eos_token:       {repr(tok.eos_token)} (id={tok.eos_token_id})')
    print(f'  pad_token:       {repr(tok.pad_token)} (id={tok.pad_token_id})')
    print(f'  unk_token:       {repr(tok.unk_token)} (id={tok.unk_token_id})')
    print(f'  sep_token:       {repr(tok.sep_token)}')
    print(f'  all_special_tokens ({len(tok.all_special_tokens)} total):')
    for st in tok.all_special_tokens[:10]:
        sid = tok.convert_tokens_to_ids(st)
        print(f'    {repr(st):<40} id={sid}')
    if hasattr(tok, 'chat_template') and tok.chat_template:
        preview = tok.chat_template[:80].replace('\n', ' ')
        print(f'  chat_template: {preview}...')

models = [
    'meta-llama/Meta-Llama-3-8B-Instruct',
    'mistralai/Mistral-7B-Instruct-v0.2',
    'google/gemma-7b-it',
]
for model in models:
    try:
        inspect_special_tokens(model)
    except Exception as e:
        print(f'{model}: {e}')
```

## Chat Template Application

HuggingFace tokenizers expose apply_chat_template(), which formats a list of role-content dictionaries into the model-specific instruction format. The template is stored in the tokenizer's tokenizer_config.json as a Jinja2 template string. Calling apply_chat_template() with add_generation_prompt=True appends the assistant header token, priming the model for response generation. Using this method guarantees correct formatting regardless of model family — the same Python code works for LLaMA-3, Mistral, and Gemma by switching only the model name.

```python
from transformers import AutoTokenizer

def format_conversation(model_name, system_msg, user_msg, assistant_msg=None):
    tok = AutoTokenizer.from_pretrained(model_name)
    messages = []
    if system_msg:
        messages.append({'role': 'system', 'content': system_msg})
    messages.append({'role': 'user', 'content': user_msg})
    if assistant_msg:
        messages.append({'role': 'assistant', 'content': assistant_msg})
    formatted = tok.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=(assistant_msg is None),
    )
    token_ids = tok.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=(assistant_msg is None),
        return_tensors='pt',
    )
    return formatted, token_ids

system = 'You are a helpful assistant specialising in machine learning.'
user = 'Explain the difference between BPE and WordPiece tokenization.'
models = ['meta-llama/Meta-Llama-3-8B-Instruct', 'mistralai/Mistral-7B-Instruct-v0.2']
for model in models:
    try:
        text, ids = format_conversation(model, system, user)
        print(f'{model}:')
        print(f'  Token count: {ids.shape[-1]}')
        print(f'  First 200 chars: {text[:200]}')
        print()
    except Exception as e:
        print(f'{model}: {e}')
```

## Generation Stop Token Configuration

Correct stop token configuration is essential for inference. The model's generate() method accepts eos_token_id as a single token id or a list of ids; generation halts when any of these ids is produced. For models with multiple stop tokens (LLaMA-3 has both <|eot_id|> and <|end_of_text|>), all valid stop ids must be included or the model will continue generating past the intended turn boundary. The stopping_criteria argument accepts custom StoppingCriteria subclasses for pattern-based stopping, useful when stop sequences span multiple tokens.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria, StoppingCriteriaList

class MultiTokenStopCriteria(StoppingCriteria):
    def __init__(self, stop_token_ids):
        self.stop_ids = set(stop_token_ids)

    def __call__(self, input_ids, scores, **kwargs):
        last_token = input_ids[0, -1].item()
        return last_token in self.stop_ids

def configure_generation(model_name, prompt):
    tok = AutoTokenizer.from_pretrained(model_name)
    # Collect all valid stop token ids for this model
    stop_ids = []
    for special in [tok.eos_token, '<|eot_id|>', '<|end_of_text|>', '</s>', '<|im_end|>']:
        if special and special in tok.get_vocab():
            stop_ids.append(tok.convert_tokens_to_ids(special))
    stop_criteria = StoppingCriteriaList([MultiTokenStopCriteria(stop_ids)])
    print(f'{model_name}:')
    print(f'  Stop token ids: {stop_ids}')
    stop_tokens = [tok.convert_ids_to_tokens(sid) for sid in stop_ids]
    print(f'  Stop tokens:    {stop_tokens}')
    return stop_criteria

for model in ['meta-llama/Meta-Llama-3-8B', 'mistralai/Mistral-7B-v0.1']:
    try:
        configure_generation(model, 'test')
    except Exception as e:
        print(f'{model}: {e}')
```

## Padding Strategy for Batched Inference

Decoder-only models (GPT, LLaMA, Mistral) use left-padding for batched generation: PAD tokens are prepended so that all sequences in a batch end at the same position, allowing the model's autoregressive generation to begin at identical positions across batch elements. Right-padding is used for encoder training (BERT, RoBERTa) and for computing loss on variable-length sequences: padding is appended and masked via attention_mask. Using right-padding with a decoder-only model during generation causes incorrect output because the model sees PAD tokens between the prompt end and the first generated token.

```python
import torch
from transformers import AutoTokenizer

def demonstrate_padding(model_name, prompts):
    tok = AutoTokenizer.from_pretrained(model_name)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token

    # Left-padding: correct for decoder-only generation
    tok.padding_side = 'left'
    left_batch = tok(prompts, return_tensors='pt', padding=True, truncation=True)
    print(f'Left-padding (decoder generation):')
    print(f'  input_ids shape:      {left_batch.input_ids.shape}')
    print(f'  attention_mask shape: {left_batch.attention_mask.shape}')
    print(f'  First sequence ids:   {left_batch.input_ids[0].tolist()}')
    print(f'  First seq mask:       {left_batch.attention_mask[0].tolist()}')

    # Right-padding: correct for encoder training
    tok.padding_side = 'right'
    right_batch = tok(prompts, return_tensors='pt', padding=True, truncation=True)
    print(f'Right-padding (encoder training):')
    print(f'  First sequence ids:   {right_batch.input_ids[0].tolist()}')
    print(f'  First seq mask:       {right_batch.attention_mask[0].tolist()}')

short_prompts = ['Hi', 'Explain BPE tokenization in detail please.']
demonstrate_padding('gpt2', short_prompts)
```

## Special Token Formats by Model Family

| Model Family | BOS Token | Turn Delimiter | EOS Token | System Role Format |
| --- | --- | --- | --- | --- |
| LLaMA-3 | <|begin_of_text|> | <|eot_id|> + <|start_header_id|>role<|end_header_id|> | <|end_of_text|> | <|start_header_id|>system<|end_header_id|>\n{content}<|eot_id|> |
| Mistral/Mixtral | <s> | [INST] / [/INST] | </s> | No system tag — prepend to first user message inside [INST] |
| ChatML (GPT-4) | <|im_start|> | <|im_end|>\n<|im_start|>role\n | <|endoftext|> | <|im_start|>system\n{content}<|im_end|> |
| Alpaca | None | ### Instruction:\n / ### Response:\n | Stop on next ### (pattern-based) | ### System Prompt:\n{content}\n\n |
| Gemma | <bos> | <start_of_turn>role\n / <end_of_turn>\n | <eos> | <start_of_turn>user\n{system+user}<end_of_turn> |

System prompts encode the model's persona, constraints, and task context. In LLaMA-3 they are placed in a dedicated system header before the first user turn. In Mistral they are concatenated to the first user message inside [INST] brackets. In Gemma, there is no separate system role; system context is prepended to the user content in the first turn. These differences mean that a system prompt working correctly with one model family may produce different behavior on another even if the words are identical — the model has learned to respond to its specific structural delimiters.

> **Wrong Chat Template Causes Incoherent Outputs**: Using the wrong chat template for a model causes dramatic quality degradation — models are trained to recognise specific delimiter tokens around each turn, and mismatched templates produce incoherent outputs even with correct content. Always use apply_chat_template() from the model's own tokenizer rather than hand-constructing prompt strings. If the tokenizer lacks a chat_template field (older models), check the model card for the exact format used during instruction tuning.

- Always use apply_chat_template() — never hand-construct instruction prompts for instruction-tuned models.
- Set eos_token_id to ALL valid stop token ids for the model family to prevent runaway generation.
- Use left-padding for decoder-only generation batches; use right-padding for encoder training.
- PAD token must be set for models that lack one (GPT-2): set pad_token = eos_token and mask it in attention_mask.
- LLaMA-3 has two stop tokens: <|eot_id|> ends a turn, <|end_of_text|> ends the document — both must be in stop ids.
- Tool call tokens in function-calling models (e.g., <tool_call>, <|python_tag|>) are additional special tokens to register.

---

