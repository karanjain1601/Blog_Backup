---
title: "Attention Sinks and StreamingLLM"
slug: "attention-sinks"
description: "The discovery that LLMs attend heavily to initial tokens regardless of content (attention sinks) and how retaining these sink tokens in the KV cache enables infinite-length streaming inference."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXR0ZW50aW9uIHNpbmtzIChYaWFvIGV0IGFsLiwgMjAyMykgYXJlIGEgc3RydWN0dXJhbCBwcm9wZXJ0eSBvZiBhdXRvcmVncmVzc2l2ZSBsYW5ndWFnZSBtb2RlbHM6IHJlZ2FyZGxlc3Mgb2YgZG9jdW1lbnQgY29udGVudCwgdGhlIGluaXRpYWwgdG9rZW5zIGluIGFueSBzZXF1ZW5jZSDigJQgcG9zaXRpb25zIDAgdGhyb3VnaCAzIG9yIHNvIOKAlCBhY2N1bXVsYXRlIGRpc3Byb3BvcnRpb25hdGVseSBoaWdoIGF0dGVudGlvbiBzY29yZXMgYWNyb3NzIHZpcnR1YWxseSBhbGwgaGVhZHMgYW5kIGFsbCBsYXllcnMuIFRoaXMgaXMgbm90IGEgc2VtYW50aWMgc2lnbmFsOyB0aGUgaW5pdGlhbCB0b2tlbnMgYXJlIG5vdCBwYXJ0aWN1bGFybHkgaW5mb3JtYXRpdmUuIFJhdGhlciwgc29mdG1heCBmb3JjZXMgYXR0ZW50aW9uIHdlaWdodHMgdG8gc3VtIHRvIDEuMCwgYW5kIHdoZW4gbm8gdG9rZW4gaW4gdGhlIGNvbnRleHQgaXMgaGlnaGx5IHJlbGV2YW50LCB0aGUgbW9kZWwgXHUwMDI3ZHVtcHNcdTAwMjcgZXhjZXNzIGF0dGVudGlvbiBtYXNzIG9udG8gdGhlIGZpcnN0IGZldyB0b2tlbnMgYXMgYSBzYWZlIHNpbmsuIFRoZSBkaXNjb3ZlcnkgaGFzIGEgY3JpdGljYWwgcHJhY3RpY2FsIGltcGxpY2F0aW9uOiBuYWl2ZSBLViBjYWNoZSBldmljdGlvbiBzdHJhdGVnaWVzIHRoYXQgZHJvcCBpbml0aWFsIHRva2VucyBjYXVzZSBpbW1lZGlhdGUgcGVycGxleGl0eSBjb2xsYXBzZSBkdXJpbmcgc3RyZWFtaW5nIGluZmVyZW5jZSwgd2hpbGUgcmV0YWluaW5nIHRoZXNlIHNpbmsgdG9rZW5zIHBsdXMgYSBzbGlkaW5nIHdpbmRvdyBvZiByZWNlbnQgdG9rZW5zIGVuYWJsZXMgYXJiaXRyYXJpbHkgbG9uZyBnZW5lcmF0aW9uIHdpdGggc3RhYmxlIHF1YWxpdHkuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT3ZlcnZpZXcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IldoZW4gZ2VuZXJhdGluZyB0ZXh0IGF1dG9yZWdyZXNzaXZlbHksIHRoZSBLViBjYWNoZSBncm93cyBsaW5lYXJseSB3aXRoIHNlcXVlbmNlIGxlbmd0aCwgZXZlbnR1YWxseSBleGhhdXN0aW5nIEdQVSBtZW1vcnkuIFRoZSBuYWl2ZSBzb2x1dGlvbiDigJQgZXZpY3QgdGhlIG9sZGVzdCBLViBlbnRyaWVzIHRvIG1haW50YWluIGEgZml4ZWQgY2FjaGUgc2l6ZSDigJQgZmFpbHMgY2F0YXN0cm9waGljYWxseSBhZnRlciBhIGZldyB0aG91c2FuZCB0b2tlbnMgYmVjYXVzZSBpdCBldmljdHMgdGhlIHNpbmsgdG9rZW5zIHRoYXQgZXZlcnkgYXR0ZW50aW9uIGhlYWQgcmVsaWVzIG9uIGZvciBpdHMgbm9ybWFsaXphdGlvbiBhbmNob3IuIFRoZSBTdHJlYW1pbmdMTE0gcGFwZXIgKFhpYW8gZXQgYWwuLCAyMDIzKSBwcm9wb3NlcyBhIHNpbXBsZSBmaXg6IGFsd2F5cyByZXRhaW4gdGhlIGZpcnN0IDQgdG9rZW5zICh0aGUgc2luayB0b2tlbnMpIGluIHRoZSBLViBjYWNoZSwgYW5kIHVzZSBhIHNsaWRpbmcgd2luZG93IG9mIHJlY2VudCB0b2tlbnMgZm9yIHRoZSByZW1haW5kZXIuIFdpdGggdGhpcyBhcmNoaXRlY3R1cmUsIGEgbW9kZWwgY2FuIGdlbmVyYXRlIHNlcXVlbmNlcyBvZiBhcmJpdHJhcnkgbGVuZ3RoIHdoaWxlIG1haW50YWluaW5nIGNvbnN0YW50IG1lbW9yeSB1c2FnZSBhbmQgc3RhYmxlIHBlcnBsZXhpdHkgdGhyb3VnaG91dCDigJQgdHJhbnNmb3JtaW5nIGFueSBwcmV0cmFpbmVkIExMTSBpbnRvIGEgc3RyZWFtaW5nIG1vZGVsIHdpdGhvdXQgcmV0cmFpbmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUaGUgQXR0ZW50aW9uIFNpbmsgUGhlbm9tZW5vbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGF0dGVudGlvbiBzaW5rIHBoZW5vbWVub24gd2FzIGZpcnN0IGlkZW50aWZpZWQgYnkgYW5hbHl6aW5nIGF0dGVudGlvbiB3ZWlnaHQgbWF0cmljZXMgb2YgTGxhbWEtMi03QiwgRmFsY29uLTdCLCBhbmQgR1BULTIgb24gZG9jdW1lbnRzIG9mIDFL4oCTNEsgdG9rZW5zLiBJbiBldmVyeSBoZWFkIG9mIGV2ZXJ5IGxheWVyLCB0aGUgYXR0ZW50aW9uIHdlaWdodCBmb3IgcG9zaXRpb24gMCBpcyBiZXR3ZWVuIDEwIGFuZCAxMDAgdGltZXMgbGFyZ2VyIHRoYW4gZm9yIGFueSBvdGhlciBwb3NpdGlvbiBiZXlvbmQgcG9zaXRpb24gNC4gVGhpcyBwYXR0ZXJuIGhvbGRzIHJlZ2FyZGxlc3Mgb2Ygd2hhdCB0b2tlbiBhcHBlYXJzIGF0IHBvc2l0aW9uIDAg4oCUIGV2ZW4gaWYgcG9zaXRpb24gMCBpcyBhIHB1bmN0dWF0aW9uIG1hcmsgb3Igc3BlY2lhbCB0b2tlbi4gVGhlIHNvZnRtYXggYXR0ZW50aW9uIGZvcm11bGF0aW9uIGZvcmNlcyB3ZWlnaHRzIHRvIHN1bSB0byAxLjAuIFdoZW4gbm8gdG9rZW4gaXMgc2VtYW50aWNhbGx5IGhpZ2hseSByZWxldmFudCB0byB0aGUgY3VycmVudCBxdWVyeSwgdGhlIG1vZGVsIGNhbm5vdCBwcm9kdWNlIGEgemVyby1hdHRlbnRpb24gb3V0cHV0IOKAlCBpdCBtdXN0IGFsbG9jYXRlIHRoZSBwcm9iYWJpbGl0eSBtYXNzIHNvbWV3aGVyZS4gVGhlIGluaXRpYWwgdG9rZW5zIHNlcnZlIGFzIHRoaXMgYWxsb2NhdGlvbiB0YXJnZXQsIGEgbWF0aGVtYXRpY2FsbHkgbmVjZXNzYXJ5IGNvbnNlcXVlbmNlIG9mIHNvZnRtYXggbm9ybWFsaXphdGlvbiBvdmVyIGEgZGlzY3JldGUgdG9rZW4gc2V0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdFxuZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXIsIEF1dG9Nb2RlbEZvckNhdXNhbExNXG5cbmRlZiB2aXN1YWxpemVfYXR0ZW50aW9uX3NpbmtzKG1vZGVsX25hbWU6IHN0ciA9IFx1MDAyN21ldGEtbGxhbWEvTGxhbWEtMi03Yi1oZlx1MDAyNyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0ZXh0X2xlbmd0aDogaW50ID0gNTEyLCBsYXllcl9pZHg6IGludCA9IDE2KTpcbiAgICAjIEV4dHJhY3QgYXR0ZW50aW9uIHdlaWdodHMgYW5kIHNob3cgc2luayBjb25jZW50cmF0aW9uIG9uIHBvc2l0aW9ucyAwLTNcbiAgICB0b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgIG1vZGVsID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKG1vZGVsX25hbWUsIHRvcmNoX2R0eXBlPXRvcmNoLmZsb2F0MTYsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dF9hdHRlbnRpb25zPVRydWUsIGRldmljZV9tYXA9XHUwMDI3YXV0b1x1MDAyNylcbiAgICBzYW1wbGUgPSBcdTAwMjdTY2llbnRpc3RzIGhhdmUgbG9uZyBkZWJhdGVkIHdoZXRoZXIgY29uc2Npb3VzbmVzcyBhcmlzZXMgZnJvbSBcdTAwMjcgKiAyMFxuICAgIGlkcyA9IHRva2VuaXplcihzYW1wbGUsIHJldHVybl90ZW5zb3JzPVx1MDAyN3B0XHUwMDI3LCBtYXhfbGVuZ3RoPXRleHRfbGVuZ3RoLFxuICAgICAgICAgICAgICAgICAgICB0cnVuY2F0aW9uPVRydWUpLmlucHV0X2lkcy5jdWRhKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgb3V0ID0gbW9kZWwoaWRzLCBvdXRwdXRfYXR0ZW50aW9ucz1UcnVlKVxuICAgICMgQXR0ZW50aW9uIHNoYXBlOiAoYmF0Y2gsIG5faGVhZHMsIHNlcSwgc2VxKSDigJQgdGFrZSBsYXN0IHRva2VuXHUwMDI3cyBhdHRlbnRpb24gcm93XG4gICAgYXR0biA9IG91dC5hdHRlbnRpb25zW2xheWVyX2lkeF1bMCwgOiwgLTEsIDpdLmZsb2F0KCkuY3B1KCkubnVtcHkoKSAgIyAobl9oZWFkcywgc2VxKVxuICAgIG1lYW5fYnlfcG9zID0gYXR0bi5tZWFuKGF4aXM9MCkgICMgYXZlcmFnZSBvdmVyIGFsbCBoZWFkc1xuICAgIHNpbmtfbWFzcyA9IG1lYW5fYnlfcG9zWzo0XS5zdW0oKVxuICAgIHJlc3RfbWFzcyA9IG1lYW5fYnlfcG9zWzQ6XS5zdW0oKVxuICAgIHByaW50KGZcdTAwMjdMYXllciB7bGF5ZXJfaWR4fTogYXR0ZW50aW9uIG1hc3Mgb24gcG9zaXRpb25zIDAtMzoge3NpbmtfbWFzczouM2Z9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdMYXllciB7bGF5ZXJfaWR4fTogYXR0ZW50aW9uIG1hc3Mgb24gcG9zaXRpb25zIDQrOiAge3Jlc3RfbWFzczouM2Z9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjdTaW5rIGNvbmNlbnRyYXRpb24gcmF0aW86IHtzaW5rX21hc3MgLyAocmVzdF9tYXNzICsgMWUtOSk6LjFmfXhcdTAwMjcpXG4gICAgdG9wX3BvcyA9IG5wLmFyZ3NvcnQobWVhbl9ieV9wb3MpWzo6LTFdWzo1XVxuICAgIHByaW50KGZcdTAwMjdUb3AtNSBhdHRlbmRlZCBwb3NpdGlvbnM6IHt0b3BfcG9zLnRvbGlzdCgpfVx1MDAyNylcbiAgICByZXR1cm4gbWVhbl9ieV9wb3MifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaHkgSW5pdGlhbCBUb2tlbnMgQ2FwdHVyZSBBdHRlbnRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBzb2Z0bWF4IGZ1bmN0aW9uIG1hcHMgYXJiaXRyYXJ5IHJlYWwtdmFsdWVkIGF0dGVudGlvbiBsb2dpdHMgdG8gYSBwcm9iYWJpbGl0eSBkaXN0cmlidXRpb24gc3VtbWluZyB0byAxLjAuIFdoZW4gdGhlIG1vZGVsIHByb2Nlc3NlcyBhIHF1ZXJ5IGZvciB3aGljaCBubyBrZXkgaW4gdGhlIGNvbnRleHQgaXMgaGlnaGx5IHJlbGV2YW50IChsb3cgZG90LXByb2R1Y3Qgc2ltaWxhcml0eSBhY3Jvc3MgYWxsIHBvc2l0aW9ucyksIHNvZnRtYXggc3RpbGwgcHJvZHVjZXMgYSB2YWxpZCBkaXN0cmlidXRpb24uIFJhdGhlciB0aGFuIHByb2R1Y2luZyBhIG5lYXItdW5pZm9ybSBkaXN0cmlidXRpb24g4oCUIHdoaWNoIHdvdWxkIGluamVjdCBub2lzZSBhY3Jvc3MgYWxsIHBvc2l0aW9ucyDigJQgdGhlIG1vZGVsIGxlYXJucyB0byBjb25jZW50cmF0ZSBtYXNzIG9uIHNwZWNpZmljIFx1MDAyN3NpbmtcdTAwMjcgcG9zaXRpb25zIHRoYXQgYXJlIGFsd2F5cyBhdHRlbmRlZCB0byByZWdhcmRsZXNzIG9mIGNvbnRlbnQuIFRoZSBpbml0aWFsIHBvc2l0aW9ucyBhcmUgaWRlYWwgc2lua3MgZm9yIHR3byByZWFzb25zOiAoMSkgdGhleSBhcmUgYWx3YXlzIHByZXNlbnQgaW4gdGhlIGNhdXNhbCBhdHRlbnRpb24gd2luZG93IChldmVyeSB0b2tlbiBjYW4gc2VlIHBvc2l0aW9uIDApLCBhbmQgKDIpIGVhcmx5IGluIHRyYWluaW5nLCB0aGUgbW9kZWwgbGVhcm5zIHRoaXMgYXMgYSByZWd1bGFyaXphdGlvbiBzdHJhdGVneSBiZWZvcmUgZGV2ZWxvcGluZyBtb3JlIG51YW5jZWQgcG9zaXRpb24tc3BlY2lmaWMgYXR0ZW50aW9uIHBhdHRlcm5zLiBUaGUgcmVzdWx0IGlzIHRoYXQgZXZlcnkgbGF5ZXIgaGFzIGltcGxpY2l0IHNpbmsgYmVoYXZpb3IsIGFuZCByZW1vdmluZyBzaW5rIHRva2VucyBmcm9tIHRoZSBLViBjYWNoZSBpbnN0YW50bHkgZGVzdHJveXMgdGhpcyBub3JtYWxpemF0aW9uIG1lY2hhbmlzbS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplciwgQXV0b01vZGVsRm9yQ2F1c2FsTE1cbmZyb20gZGF0YWNsYXNzZXMgaW1wb3J0IGRhdGFjbGFzc1xuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3QsIFR1cGxlXG5cbkBkYXRhY2xhc3NcbmNsYXNzIEtWQ2FjaGU6XG4gICAga2V5czogdG9yY2guVGVuc29yICAgICMgKGxheWVycywgaGVhZHMsIHNlcSwgaGVhZF9kaW0pXG4gICAgdmFsdWVzOiB0b3JjaC5UZW5zb3JcblxuZGVmIGV2aWN0X29sZGVzdChjYWNoZTogS1ZDYWNoZSwgbWF4X3NpemU6IGludCkgLVx1MDAzZSBLVkNhY2hlOlxuICAgICMgRHJvcCBvbGRlc3QgKGxlZnRtb3N0KSBLViBlbnRyaWVzIGJleW9uZCBtYXhfc2l6ZVxuICAgIGlmIGNhY2hlLmtleXMuc2hhcGVbMl0gXHUwMDNlIG1heF9zaXplOlxuICAgICAgICBjYWNoZS5rZXlzICAgPSBjYWNoZS5rZXlzWzosIDosIC1tYXhfc2l6ZTosIDpdXG4gICAgICAgIGNhY2hlLnZhbHVlcyA9IGNhY2hlLnZhbHVlc1s6LCA6LCAtbWF4X3NpemU6LCA6XVxuICAgIHJldHVybiBjYWNoZVxuXG5kZWYgZXZpY3RfYnlfYXR0ZW50aW9uKGNhY2hlOiBLVkNhY2hlLCBhdHRuX3Njb3JlczogdG9yY2guVGVuc29yLFxuICAgICAgICAgICAgICAgICAgICAgICBtYXhfc2l6ZTogaW50KSAtXHUwMDNlIEtWQ2FjaGU6XG4gICAgIyBLZWVwIHRvcC1rIGVudHJpZXMgYnkgbWVhbiBhdHRlbnRpb24gc2NvcmUgYWNyb3NzIGhlYWRzIGFuZCBsYXllcnNcbiAgICBpZiBjYWNoZS5rZXlzLnNoYXBlWzJdIFx1MDAzZSBtYXhfc2l6ZTpcbiAgICAgICAgbWVhbl9hdHRuID0gYXR0bl9zY29yZXMubWVhbihkaW09KDAsIDEpKSAgIyAoc2VxLClcbiAgICAgICAgdG9wa19pZHggPSBtZWFuX2F0dG4udG9wayhtYXhfc2l6ZSkuaW5kaWNlcy5zb3J0KCkudmFsdWVzXG4gICAgICAgIGNhY2hlLmtleXMgICA9IGNhY2hlLmtleXNbOiwgOiwgdG9wa19pZHgsIDpdXG4gICAgICAgIGNhY2hlLnZhbHVlcyA9IGNhY2hlLnZhbHVlc1s6LCA6LCB0b3BrX2lkeCwgOl1cbiAgICByZXR1cm4gY2FjaGVcblxuZGVmIHNpbmtfcGx1c193aW5kb3coY2FjaGU6IEtWQ2FjaGUsIG1heF9zaXplOiBpbnQsIG5fc2luazogaW50ID0gNCkgLVx1MDAzZSBLVkNhY2hlOlxuICAgICMgQWx3YXlzIGtlZXAgZmlyc3Qgbl9zaW5rIHRva2VucyArIHJvbGxpbmcgd2luZG93IG9mIHJlbWFpbmluZyBidWRnZXRcbiAgICB3aW5kb3cgPSBtYXhfc2l6ZSAtIG5fc2lua1xuICAgIGlmIGNhY2hlLmtleXMuc2hhcGVbMl0gXHUwMDNlIG1heF9zaXplOlxuICAgICAgICBzaW5rX2sgPSBjYWNoZS5rZXlzWzosIDosIDpuX3NpbmssIDpdXG4gICAgICAgIHNpbmtfdiA9IGNhY2hlLnZhbHVlc1s6LCA6LCA6bl9zaW5rLCA6XVxuICAgICAgICB3aW5fayAgPSBjYWNoZS5rZXlzWzosIDosIC13aW5kb3c6LCA6XVxuICAgICAgICB3aW5fdiAgPSBjYWNoZS52YWx1ZXNbOiwgOiwgLXdpbmRvdzosIDpdXG4gICAgICAgIGNhY2hlLmtleXMgICA9IHRvcmNoLmNhdChbc2lua19rLCB3aW5fa10sIGRpbT0yKVxuICAgICAgICBjYWNoZS52YWx1ZXMgPSB0b3JjaC5jYXQoW3Npbmtfdiwgd2luX3ZdLCBkaW09MilcbiAgICByZXR1cm4gY2FjaGVcblxucHJpbnQoXHUwMDI3VGhyZWUgZXZpY3Rpb24gcG9saWNpZXM6IG9sZGVzdCwgYnlfYXR0ZW50aW9uLCBzaW5rK3dpbmRvd1x1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLViBDYWNoZSBFdmljdGlvbiBGYWlsdXJlIE1vZGVzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJOYWl2ZSBLViBjYWNoZSBldmljdGlvbiBzdHJhdGVnaWVzIGZhaWwgaW4gY2hhcmFjdGVyaXN0aWMgd2F5cy4gRXZpY3RpbmcgdGhlIG9sZGVzdCB0b2tlbnMgKGEgcXVldWUvRklGTyBwb2xpY3kpIHdvcmtzIHVudGlsIHRoZSBzaW5rIHRva2VucyBhZ2Ugb3V0IG9mIHRoZSBjYWNoZSwgYXQgd2hpY2ggcG9pbnQgcGVycGxleGl0eSBqdW1wcyBzaGFycGx5IOKAlCB0eXBpY2FsbHkgZnJvbSB+OCB0byBcdTAwM2UxMDAgaW4gYSBzaW5nbGUgZ2VuZXJhdGlvbiBzdGVwLiBFdmljdGluZyBieSBsb3dlc3QgYXR0ZW50aW9uIHNjb3JlIG1pZ2h0IHNlZW0gc21hcnRlciAoa2VlcCB3aGF0IHRoZSBtb2RlbCBhdHRlbmRzIHRvKSwgYnV0IHRoaXMgY3JlYXRlcyBhIHBvc2l0aXZlIGZlZWRiYWNrIGxvb3A6IG9uY2UgYSB1c2VmdWwgdG9rZW4gaXMgZXZpY3RlZCwgaXQgY2FuIG5vIGxvbmdlciByZWNlaXZlIGF0dGVudGlvbiwgc28gaXQgd291bGQgaGF2ZSBiZWVuIGV2aWN0ZWQgZXZlbiBpZiByZXRhaW5lZC4gQm90aCBzdHJhdGVnaWVzIHVsdGltYXRlbHkgZmFpbCBhdCBzZXF1ZW5jZXMgbG9uZ2VyIHRoYW4gdGhlIGNhY2hlIHNpemUuIE9ubHkgdGhlIHNpbmsrc2xpZGluZyB3aW5kb3cgc3RyYXRlZ3kgcHJvZHVjZXMgc3RhYmxlIHBlcnBsZXhpdHkgYWNyb3NzIGFyYml0cmFyeSBsZW5ndGhzLCBiZWNhdXNlIGl0IGd1YXJhbnRlZXMgdGhhdCB0aGUgYXR0ZW50aW9uIG5vcm1hbGl6YXRpb24gYW5jaG9ycyBhcmUgYWx3YXlzIGF2YWlsYWJsZSBpbiB0aGUgS1YgY2FjaGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b1Rva2VuaXplciwgQXV0b01vZGVsRm9yQ2F1c2FsTE1cblxuY2xhc3MgU2lua0NhY2hlOlxuICAgICMgTWluaW1hbCBTdHJlYW1pbmdMTE0gS1YgY2FjaGU6IHJldGFpbiBuX3NpbmsgaW5pdGlhbCB0b2tlbnMgKyByb2xsaW5nIHdpbmRvd1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuX3Npbms6IGludCA9IDQsIHdpbmRvd19zaXplOiBpbnQgPSA1MTIpOlxuICAgICAgICBzZWxmLm5fc2luayA9IG5fc2lua1xuICAgICAgICBzZWxmLndpbmRvd19zaXplID0gd2luZG93X3NpemVcbiAgICAgICAgc2VsZi5zaW5rX2tleXM6ICAgbGlzdCA9IFtdXG4gICAgICAgIHNlbGYuc2lua192YWx1ZXM6IGxpc3QgPSBbXVxuICAgICAgICBzZWxmLndpbl9rZXlzOiAgICBsaXN0ID0gW11cbiAgICAgICAgc2VsZi53aW5fdmFsdWVzOiAgbGlzdCA9IFtdXG4gICAgICAgIHNlbGYudG90YWxfdG9rZW5zID0gMFxuXG4gICAgZGVmIGFkZChzZWxmLCBrZXk6IHRvcmNoLlRlbnNvciwgdmFsdWU6IHRvcmNoLlRlbnNvcikgLVx1MDAzZSBOb25lOlxuICAgICAgICAjIGtleS92YWx1ZSBzaGFwZTogKGJhdGNoLCBoZWFkcywgMSwgaGVhZF9kaW0pXG4gICAgICAgIGlmIHNlbGYudG90YWxfdG9rZW5zIFx1MDAzYyBzZWxmLm5fc2luazpcbiAgICAgICAgICAgIHNlbGYuc2lua19rZXlzLmFwcGVuZChrZXkpXG4gICAgICAgICAgICBzZWxmLnNpbmtfdmFsdWVzLmFwcGVuZCh2YWx1ZSlcbiAgICAgICAgZWxzZTpcbiAgICAgICAgICAgIHNlbGYud2luX2tleXMuYXBwZW5kKGtleSlcbiAgICAgICAgICAgIHNlbGYud2luX3ZhbHVlcy5hcHBlbmQodmFsdWUpXG4gICAgICAgICAgICBpZiBsZW4oc2VsZi53aW5fa2V5cykgXHUwMDNlIHNlbGYud2luZG93X3NpemU6XG4gICAgICAgICAgICAgICAgc2VsZi53aW5fa2V5cy5wb3AoMClcbiAgICAgICAgICAgICAgICBzZWxmLndpbl92YWx1ZXMucG9wKDApXG4gICAgICAgIHNlbGYudG90YWxfdG9rZW5zICs9IDFcblxuICAgIGRlZiBnZXQoc2VsZikgLVx1MDAzZSB0dXBsZTpcbiAgICAgICAgYWxsX2sgPSB0b3JjaC5jYXQoc2VsZi5zaW5rX2tleXMgKyBzZWxmLndpbl9rZXlzLCBkaW09MilcbiAgICAgICAgYWxsX3YgPSB0b3JjaC5jYXQoc2VsZi5zaW5rX3ZhbHVlcyArIHNlbGYud2luX3ZhbHVlcywgZGltPTIpXG4gICAgICAgIHJldHVybiBhbGxfaywgYWxsX3ZcblxucHJpbnQoZlx1MDAyN1NpbmtDYWNoZTogNCBzaW5rIHRva2VucyArIDUxMi10b2tlbiBzbGlkaW5nIHdpbmRvdyA9IDUxNiB0b3RhbCBLViBlbnRyaWVzXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNpbmsgVG9rZW5zICsgUm9sbGluZyBXaW5kb3cifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBTdHJlYW1pbmdMTE0gS1YgY2FjaGUgYXJjaGl0ZWN0dXJlIGhhcyB0d28gY29tcG9uZW50czogYSBmaXhlZCBzaW5rIHJlZ2lvbiBjb250YWluaW5nIHRoZSBmaXJzdCBuX3NpbmsgdG9rZW5zICh0eXBpY2FsbHkgbl9zaW5rPTQpLCBhbmQgYSBzbGlkaW5nIHdpbmRvdyBjb250YWluaW5nIHRoZSBtb3N0IHJlY2VudCB3aW5kb3dfc2l6ZSB0b2tlbnMuIFRoZSB0b3RhbCBjYWNoZSBzaXplIGlzIHRoZXJlZm9yZSBuX3NpbmsgKyB3aW5kb3dfc2l6ZSDigJQgY29uc3RhbnQgcmVnYXJkbGVzcyBvZiBzZXF1ZW5jZSBsZW5ndGguIFdoZW4gYSBuZXcgdG9rZW4gaXMgZ2VuZXJhdGVkLCBpdHMgS1YgcGFpciBpcyBhcHBlbmRlZCB0byB0aGUgd2luZG93OyBpZiB0aGUgd2luZG93IGlzIGZ1bGwsIHRoZSBvbGRlc3Qgd2luZG93IGVudHJ5IGlzIGV2aWN0ZWQuIFRoZSBzaW5rIGVudHJpZXMgYXJlIG5ldmVyIGV2aWN0ZWQuIFdpdGggdGhpcyBzY2hlbWUsIHRoZSBtb2RlbCBhbHdheXMgaGFzIGFjY2VzcyB0byB0aGUgaW5pdGlhbCB0b2tlbnMgdGhhdCBzZXJ2ZSBhcyBhdHRlbnRpb24gbm9ybWFsaXphdGlvbiBhbmNob3JzLCBwbHVzIHRoZSBtb3N0IHJlY2VudCBjb250ZXh0IGZvciBsb2NhbCBjb2hlcmVuY2UuIFRoZSBhcHByb2FjaCBlbmFibGVzIGdlbmVyYXRpb24gb2Ygc2VxdWVuY2VzIG9mIGFyYml0cmFyeSBsZW5ndGgg4oCUIHRoZSBwYXBlciBkZW1vbnN0cmF0ZXMgc3RhYmxlIHBlcnBsZXhpdHkgYXQgNCBtaWxsaW9uIHRva2VucyDigJQgd2l0aCBjb25zdGFudCBtZW1vcnkgdXNhZ2UgYW5kIG5vIGFyY2hpdGVjdHVyYWwgY2hhbmdlcyB0byB0aGUgYXR0ZW50aW9uIG1lY2hhbmlzbS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgbnVtcHkgYXMgbnBcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvVG9rZW5pemVyLCBBdXRvTW9kZWxGb3JDYXVzYWxMTVxuXG5kZWYgZGV0ZWN0X3NpbmtfdG9rZW5zKG1vZGVsX25hbWU6IHN0ciwgc2FtcGxlX3RleHQ6IHN0ciwgbl9sYXllcnM6IGludCA9IDMyKTpcbiAgICAjIE1lYXN1cmUgbWVhbiBhdHRlbnRpb24gc2NvcmUgcGVyIHBvc2l0aW9uLCBhdmVyYWdlZCBvdmVyIGhlYWRzIGFuZCBsYXllcnNcbiAgICB0b2tlbml6ZXIgPSBBdXRvVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lKVxuICAgIG1vZGVsID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKFxuICAgICAgICBtb2RlbF9uYW1lLCB0b3JjaF9kdHlwZT10b3JjaC5mbG9hdDE2LFxuICAgICAgICBvdXRwdXRfYXR0ZW50aW9ucz1UcnVlLCBkZXZpY2VfbWFwPVx1MDAyN2F1dG9cdTAwMjdcbiAgICApXG4gICAgaWRzID0gdG9rZW5pemVyKHNhbXBsZV90ZXh0LCByZXR1cm5fdGVuc29ycz1cdTAwMjdwdFx1MDAyNywgbWF4X2xlbmd0aD0yNTYsXG4gICAgICAgICAgICAgICAgICAgIHRydW5jYXRpb249VHJ1ZSkuaW5wdXRfaWRzLmN1ZGEoKVxuICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgICAgICBvdXQgPSBtb2RlbChpZHMsIG91dHB1dF9hdHRlbnRpb25zPVRydWUpXG4gICAgIyBBdmVyYWdlIGF0dGVudGlvbiByZWNlaXZlZCBieSBlYWNoIHBvc2l0aW9uIGFjcm9zcyBhbGwgaGVhZHMgYW5kIGxheWVyc1xuICAgIGF0dG5fcmVjZWl2ZWQgPSB0b3JjaC56ZXJvcyhpZHMuc2hhcGVbMV0pXG4gICAgZm9yIGxheWVyX2F0dG4gaW4gb3V0LmF0dGVudGlvbnNbOm5fbGF5ZXJzXTpcbiAgICAgICAgIyBsYXllcl9hdHRuOiAoYmF0Y2gsIGhlYWRzLCB0Z3QsIHNyYylcbiAgICAgICAgYXR0bl9yZWNlaXZlZCArPSBsYXllcl9hdHRuWzBdLm1lYW4oZGltPSgwLCAxKSkuY3B1KCkuZmxvYXQoKVxuICAgIGF0dG5fcmVjZWl2ZWQgLz0gbl9sYXllcnNcbiAgICBwcmludChcdTAwMjdQb3NpdGlvbiB8IE1lYW4gYXR0ZW50aW9uIHJlY2VpdmVkXHUwMDI3KVxuICAgIGZvciBwb3MgaW4gcmFuZ2UobWluKDgsIGlkcy5zaGFwZVsxXSkpOlxuICAgICAgICBiYXIgPSBcdTAwMjcjXHUwMDI3ICogaW50KGF0dG5fcmVjZWl2ZWRbcG9zXS5pdGVtKCkgKiAyMDApXG4gICAgICAgIHByaW50KGZcdTAwMjcgIHBvcyB7cG9zOjNkfToge2F0dG5fcmVjZWl2ZWRbcG9zXTouNGZ9ICB7YmFyfVx1MDAyNylcbiAgICByZXR1cm4gYXR0bl9yZWNlaXZlZCJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJLViBFdmljdGlvbiBQb2xpY3kiLCJDYWNoZSBTaXplICh0b2tlbnMpIiwiUFBMIGF0IDEwSyB0b2tlbnMiLCJQUEwgYXQgMTAwSyB0b2tlbnMiLCJHZW5lcmF0aW9uIFNwZWVkIl0sInJvd3MiOltbIkZ1bGwgY2FjaGUgKG5vIGV2aWN0aW9uKSIsIkdyb3dzIHRvIE9PTSBhdCB+OEsiLCI4LjEgKG5vcm1hbCkiLCJPT00iLCJEZWdyYWRlcyBhcyBPKG5eMikiXSxbIkV2aWN0IG9sZGVzdCAoRklGTykiLCI1MTIgKGZpeGVkKSIsIjguMSAobm9ybWFsKSIsIjEwMi40IChjb2xsYXBzZSkiLCJDb25zdGFudCJdLFsiRXZpY3QgYnkgYXR0ZW50aW9uIHNjb3JlIiwiNTEyIChmaXhlZCkiLCI4LjMgKHNsaWdodCBkcm9wKSIsIjg5LjcgKGNvbGxhcHNlKSIsIkNvbnN0YW50Il0sWyJTaW5rICg0KSArIHNsaWRpbmcgd2luZG93ICg1MDgpIiwiNTEyIChmaXhlZCkiLCI4LjEgKHN0YWJsZSkiLCI4LjIgKHN0YWJsZSkiLCJDb25zdGFudCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RyZWFtaW5nTExNIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RyZWFtaW5nTExNIG1vZGlmaWVzIGluZmVyZW5jZSDigJQgbm90IGFyY2hpdGVjdHVyZS4gVGhlIGJhc2UgdHJhbnNmb3JtZXIgd2VpZ2h0cyBhcmUgdW5jaGFuZ2VkLiBUaGUgb25seSBtb2RpZmljYXRpb24gaXMgdGhlIEtWIGNhY2hlIG1hbmFnZW1lbnQ6IGluc3RlYWQgb2YgYSBzdGFuZGFyZCBncm93aW5nIGxpc3Qgb3IgYSBGSUZPIHF1ZXVlLCBhIFNpbmtDYWNoZSBvYmplY3QgaW50ZXJjZXB0cyBlYWNoIG5ldyBLViBwYWlyIGFuZCByb3V0ZXMgaXQgdG8gZWl0aGVyIHRoZSBzaW5rIHJlZ2lvbiBvciB0aGUgd2luZG93LiBBdCBhdHRlbnRpb24gY29tcHV0YXRpb24gdGltZSwgdGhlIG1vZGVsIGF0dGVuZHMgb3ZlciBhbGwgc2luayBlbnRyaWVzIHBsdXMgYWxsIHdpbmRvdyBlbnRyaWVzLCBjb25jYXRlbmF0ZWQgaW4gdGhlaXIgb3JpZ2luYWwgb3JkZXIuIFBvc2l0aW9uIElEcyBhcmUgcmUtaW5kZXhlZCBhdCBlYWNoIHN0ZXAgdG8gYmUgY29uc2lzdGVudCB3aXRoIHRoZSBhdHRlbmRlZCBzZXF1ZW5jZSDigJQgdGhlIHNpbmsgcG9zaXRpb25zIHJldGFpbiB0aGVpciBvcmlnaW5hbCBJRHMgKDAgdGhyb3VnaCBuX3NpbmstMSksIGFuZCB3aW5kb3cgcG9zaXRpb25zIGFyZSByZW51bWJlcmVkIHJlbGF0aXZlIHRvIHRoZWlyIGN1cnJlbnQgcG9zaXRpb24gaW4gdGhlIHdpbmRvdy4gVGhpcyByZS1pbmRleGluZyBlbnN1cmVzIFJvUEUgZW1iZWRkaW5ncyByZW1haW4gY29oZXJlbnQgd2l0aCB0aGUgYWN0dWFsIGF0dGVuZGVkIHNlcXVlbmNlLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiQXR0ZW50aW9uIFNpbmtzIENvc3QgUmVhbCBDYXBhY2l0eSIsImNvbnRlbnQiOiJBdHRlbnRpb24gc2lua3MgbWVhbiB0aGF0IG1vZGVscyBzZWNyZXRseSBcdTAwMjd1c2UgdXBcdTAwMjcgYXR0ZW50aW9uIGNhcGFjaXR5IG9uIGluaXRpYWwgdG9rZW5zIGV2ZW4gd2hlbiB0aG9zZSB0b2tlbnMgYXJlIGlycmVsZXZhbnQg4oCUIGFkZGluZyBhIGRlZGljYXRlZCBzaW5rIHRva2VuIChlLmcuLCBhIHNwZWNpYWwgXHUwMDNjc2lua1x1MDAzZSBwcmVmaXgpIGF0IHRyYWluaW5nIHRpbWUgZWxpbWluYXRlcyB0aGlzIHdhc3RlIGFuZCBpbXByb3ZlcyByZXRyaWV2YWwuIFdpdGhvdXQgYSBkZWRpY2F0ZWQgc2luaywgdGhlIG1vZGVsIHJlcHVycG9zZXMgYSByZWFsIGNvbnRlbnQgdG9rZW4gYXMgdGhlIHNpbmssIGNvcnJ1cHRpbmcgaXRzIHNlbWFudGljIHJlcHJlc2VudGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkluZmluaXRlIFRleHQgR2VuZXJhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RyZWFtaW5nTExNIGVuYWJsZXMgZ2VudWluZWx5IGluZmluaXRlLWxlbmd0aCB0ZXh0IGdlbmVyYXRpb24gZnJvbSBhIHByZXRyYWluZWQgTExNIHdpdGhvdXQgYW55IG1vZGlmaWNhdGlvbiB0byB0aGUgd2VpZ2h0cy4gVGhlIHByYWN0aWNhbCB1c2UgY2FzZXMgaW5jbHVkZTogcmVhbC10aW1lIHRyYW5zY3JpcHRpb24gYW5kIHN1bW1hcml6YXRpb24gb2YgbWVldGluZyBhdWRpbywgc3RyZWFtaW5nIGRvY3VtZW50IGNvbXBsZXRpb24gZm9yIHZlcnkgbG9uZyB0ZWNobmljYWwgcmVwb3J0cywgYWx3YXlzLW9uIGNoYXQgYXNzaXN0YW50cyB0aGF0IG1haW50YWluIGEgcm9sbGluZyBjb252ZXJzYXRpb24gd2luZG93LCBhbmQgc3RyZWFtaW5nIGNvZGUgZ2VuZXJhdGlvbiBmb3IgZW50aXJlIGNvZGViYXNlcy4gVGhlIG1lbW9yeSB1c2FnZSBpcyBib3VuZGVkIGJ5IG5fc2luayArIHdpbmRvd19zaXplIEtWIGVudHJpZXMgcmVnYXJkbGVzcyBvZiBob3cgbG9uZyBnZW5lcmF0aW9uIGNvbnRpbnVlcy4gVGhlIHBhcGVyIHJlcG9ydHMgc3RhYmxlIHBlcnBsZXhpdHkgYXQgNCBtaWxsaW9uIGdlbmVyYXRlZCB0b2tlbnMgd2l0aCBhIHdpbmRvdyBvZiAyMDQ4IGFuZCA0IHNpbmsgdG9rZW5zLiBTcGVlZCBtYXRjaGVzIHN0YW5kYXJkIGluZmVyZW5jZTogc2luY2UgY2FjaGUgc2l6ZSBpcyBjb25zdGFudCwgYXR0ZW50aW9uIGNvbXB1dGF0aW9uIHBlciB0b2tlbiBpcyBPKHdpbmRvd19zaXplKSByYXRoZXIgdGhhbiBPKG4pLCBlbGltaW5hdGluZyB0aGUgcXVhZHJhdGljIGNvc3Qgb2YgZnVsbC1jb250ZXh0IGdlbmVyYXRpb24uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJTaW5rIHRva2VuIGNvdW50OiBuX3Npbms9NCBpcyBzdWZmaWNpZW50OyBpbmNyZWFzaW5nIHRvIDggcHJvdmlkZXMgbWFyZ2luYWwgaW1wcm92ZW1lbnQgYXQgbWlub3IgY2FjaGUgY29zdC4iLCJXaW5kb3cgc2l6ZTogNTEyLTIwNDggaXMgdHlwaWNhbDsgbGFyZ2VyIHdpbmRvd3MgaW1wcm92ZSBjb2hlcmVuY2UgYXQgaGlnaGVyIG1lbW9yeSBjb3N0LiIsIlRvdGFsIGNhY2hlIHNpemUgPSBuX3NpbmsgKyB3aW5kb3dfc2l6ZSDigJQgY29uc3RhbnQgdGhyb3VnaG91dCBnZW5lcmF0aW9uIHJlZ2FyZGxlc3Mgb2Ygc2VxdWVuY2UgbGVuZ3RoLiIsIlBvc2l0aW9uIHJlLWluZGV4aW5nOiBzaW5rIHRva2VucyBrZWVwIG9yaWdpbmFsIElEczsgd2luZG93IHRva2VucyBhcmUgcmVudW1iZXJlZCB0byBtYWludGFpbiBSb1BFIGNvbnNpc3RlbmN5LiIsIlN0cmVhbWluZ0xMTSB3b3JrcyBvdXQtb2YtdGhlLWJveCB3aXRoIGFueSBSb1BFIG9yIEFMaUJpIG1vZGVsIHdpdGhvdXQgd2VpZ2h0IG1vZGlmaWNhdGlvbi4iLCJGb3IgR1BULTIgYW5kIEJFUlQtZmFtaWx5IG1vZGVscyAoYWJzb2x1dGUgcG9zaXRpb24gZW1iZWRkaW5ncyksIFN0cmVhbWluZ0xMTSByZXF1aXJlcyBhcmNoaXRlY3R1cmFsIGFkanVzdG1lbnRzLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBdHRlbnRpb24gc2lua3MgcmV2ZWFsIGEgc3RydWN0dXJhbCBwcm9wZXJ0eSBvZiBzb2Z0bWF4IGF0dGVudGlvbiB0aGF0IGhhcyBpbXBvcnRhbnQgaW1wbGljYXRpb25zIGZvciBib3RoIGVmZmljaWVuY3kgYW5kIGludGVycHJldGFiaWxpdHkuIFRoZSBwaGVub21lbm9uIGV4cGxhaW5zIHdoeSBzaW1wbGUgS1YgY2FjaGUgZXZpY3Rpb24gZmFpbHM6IGl0IGlzIG5vdCBtZW1vcnkgbGltaXRhdGlvbnMgdGhhdCBicmVhayBnZW5lcmF0aW9uIGJ1dCB0aGUgbG9zcyBvZiB0aGUgbm9ybWFsaXphdGlvbiBhbmNob3IgdGhhdCBldmVyeSBhdHRlbnRpb24gaGVhZCBpbXBsaWNpdGx5IHJlbGllcyBvbi4gVGhlIFN0cmVhbWluZ0xMTSBzb2x1dGlvbiBpcyBlbGVnYW50IOKAlCByZXRhaW4gNCB0b2tlbnMsIHNsaWRlIHRoZSByZXN0IOKAlCBhbmQgcmVxdWlyZXMgbm8gcmV0cmFpbmluZywgbm8gYXJjaGl0ZWN0dXJhbCBjaGFuZ2VzLCBhbmQgbmVnbGlnaWJsZSBpbXBsZW1lbnRhdGlvbiBjb21wbGV4aXR5LiBGb3IgYXBwbGljYXRpb25zIHJlcXVpcmluZyB0cnVseSBsb25nIG9yIHVuYm91bmRlZCBnZW5lcmF0aW9uLCBTdHJlYW1pbmdMTE0gaXMgY3VycmVudGx5IHRoZSBtb3N0IHByYWN0aWNhbCBhcHByb2FjaCBmb3IgcHJldHJhaW5lZCBtb2RlbHMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJBdHRlbnRpb24gc2lua3M6IHBvc2l0aW9ucyAwLTMgcmVjZWl2ZSAxMC0xMDB4IG1vcmUgbWVhbiBhdHRlbnRpb24gdGhhbiBhbnkgb3RoZXIgcG9zaXRpb24gaW4gdGhlIHNlcXVlbmNlLiIsIkV2aWN0aW5nIHNpbmsgdG9rZW5zIGZyb20gdGhlIEtWIGNhY2hlIGNhdXNlcyBpbW1lZGlhdGUgcGVycGxleGl0eSBjb2xsYXBzZSBmcm9tIH44IHRvIFx1MDAzZTEwMC4iLCJTdHJlYW1pbmdMTE0gZml4OiBhbHdheXMgcmV0YWluIHRoZSBmaXJzdCBuX3Npbms9NCBLViBlbnRyaWVzIHBsdXMgYSBzbGlkaW5nIHdpbmRvdyBvZiByZWNlbnQgZW50cmllcy4iLCJNZW1vcnkgaXMgY29uc3RhbnQ6IChuX3NpbmsgKyB3aW5kb3dfc2l6ZSkgS1YgcGFpcnMgcmVnYXJkbGVzcyBvZiB0b3RhbCBnZW5lcmF0aW9uIGxlbmd0aC4iLCJJbmZlcmVuY2Ugc3BlZWQgaXMgTyh3aW5kb3dfc2l6ZSkgcGVyIHRva2VuLCBlbGltaW5hdGluZyB0aGUgcXVhZHJhdGljIGNvc3Qgb2YgZnVsbC1jb250ZXh0IGdlbmVyYXRpb24uIiwiV29ya3Mgd2l0aCBhbnkgcHJldHJhaW5lZCBSb1BFIG1vZGVsIHdpdGhvdXQgcmV0cmFpbmluZyDigJQgcHVyZSBpbmZlcmVuY2UtdGltZSBtb2RpZmljYXRpb24uIiwiRm9yIHRyYWluaW5nLXRpbWUgZml4OiBhZGQgYSBkZWRpY2F0ZWQgXHUwMDNjc2lua1x1MDAzZSBwcmVmaXggdG9rZW4gc28gdGhlIG1vZGVsIGRvZXMgbm90IHJlcHVycG9zZSBjb250ZW50IHRva2Vucy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Attention Sinks and StreamingLLM

Attention sinks (Xiao et al., 2023) are a structural property of autoregressive language models: regardless of document content, the initial tokens in any sequence — positions 0 through 3 or so — accumulate disproportionately high attention scores across virtually all heads and all layers. This is not a semantic signal; the initial tokens are not particularly informative. Rather, softmax forces attention weights to sum to 1.0, and when no token in the context is highly relevant, the model 'dumps' excess attention mass onto the first few tokens as a safe sink. The discovery has a critical practical implication: naive KV cache eviction strategies that drop initial tokens cause immediate perplexity collapse during streaming inference, while retaining these sink tokens plus a sliding window of recent tokens enables arbitrarily long generation with stable quality.

## Overview

When generating text autoregressively, the KV cache grows linearly with sequence length, eventually exhausting GPU memory. The naive solution — evict the oldest KV entries to maintain a fixed cache size — fails catastrophically after a few thousand tokens because it evicts the sink tokens that every attention head relies on for its normalization anchor. The StreamingLLM paper (Xiao et al., 2023) proposes a simple fix: always retain the first 4 tokens (the sink tokens) in the KV cache, and use a sliding window of recent tokens for the remainder. With this architecture, a model can generate sequences of arbitrary length while maintaining constant memory usage and stable perplexity throughout — transforming any pretrained LLM into a streaming model without retraining.

## The Attention Sink Phenomenon

The attention sink phenomenon was first identified by analyzing attention weight matrices of Llama-2-7B, Falcon-7B, and GPT-2 on documents of 1K–4K tokens. In every head of every layer, the attention weight for position 0 is between 10 and 100 times larger than for any other position beyond position 4. This pattern holds regardless of what token appears at position 0 — even if position 0 is a punctuation mark or special token. The softmax attention formulation forces weights to sum to 1.0. When no token is semantically highly relevant to the current query, the model cannot produce a zero-attention output — it must allocate the probability mass somewhere. The initial tokens serve as this allocation target, a mathematically necessary consequence of softmax normalization over a discrete token set.

```python
import torch
import numpy as np
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForCausalLM

def visualize_attention_sinks(model_name: str = 'meta-llama/Llama-2-7b-hf',
                               text_length: int = 512, layer_idx: int = 16):
    # Extract attention weights and show sink concentration on positions 0-3
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16,
                                                  output_attentions=True, device_map='auto')
    sample = 'Scientists have long debated whether consciousness arises from ' * 20
    ids = tokenizer(sample, return_tensors='pt', max_length=text_length,
                    truncation=True).input_ids.cuda()
    with torch.no_grad():
        out = model(ids, output_attentions=True)
    # Attention shape: (batch, n_heads, seq, seq) — take last token's attention row
    attn = out.attentions[layer_idx][0, :, -1, :].float().cpu().numpy()  # (n_heads, seq)
    mean_by_pos = attn.mean(axis=0)  # average over all heads
    sink_mass = mean_by_pos[:4].sum()
    rest_mass = mean_by_pos[4:].sum()
    print(f'Layer {layer_idx}: attention mass on positions 0-3: {sink_mass:.3f}')
    print(f'Layer {layer_idx}: attention mass on positions 4+:  {rest_mass:.3f}')
    print(f'Sink concentration ratio: {sink_mass / (rest_mass + 1e-9):.1f}x')
    top_pos = np.argsort(mean_by_pos)[::-1][:5]
    print(f'Top-5 attended positions: {top_pos.tolist()}')
    return mean_by_pos
```

## Why Initial Tokens Capture Attention

The softmax function maps arbitrary real-valued attention logits to a probability distribution summing to 1.0. When the model processes a query for which no key in the context is highly relevant (low dot-product similarity across all positions), softmax still produces a valid distribution. Rather than producing a near-uniform distribution — which would inject noise across all positions — the model learns to concentrate mass on specific 'sink' positions that are always attended to regardless of content. The initial positions are ideal sinks for two reasons: (1) they are always present in the causal attention window (every token can see position 0), and (2) early in training, the model learns this as a regularization strategy before developing more nuanced position-specific attention patterns. The result is that every layer has implicit sink behavior, and removing sink tokens from the KV cache instantly destroys this normalization mechanism.

```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class KVCache:
    keys: torch.Tensor    # (layers, heads, seq, head_dim)
    values: torch.Tensor

def evict_oldest(cache: KVCache, max_size: int) -> KVCache:
    # Drop oldest (leftmost) KV entries beyond max_size
    if cache.keys.shape[2] > max_size:
        cache.keys   = cache.keys[:, :, -max_size:, :]
        cache.values = cache.values[:, :, -max_size:, :]
    return cache

def evict_by_attention(cache: KVCache, attn_scores: torch.Tensor,
                       max_size: int) -> KVCache:
    # Keep top-k entries by mean attention score across heads and layers
    if cache.keys.shape[2] > max_size:
        mean_attn = attn_scores.mean(dim=(0, 1))  # (seq,)
        topk_idx = mean_attn.topk(max_size).indices.sort().values
        cache.keys   = cache.keys[:, :, topk_idx, :]
        cache.values = cache.values[:, :, topk_idx, :]
    return cache

def sink_plus_window(cache: KVCache, max_size: int, n_sink: int = 4) -> KVCache:
    # Always keep first n_sink tokens + rolling window of remaining budget
    window = max_size - n_sink
    if cache.keys.shape[2] > max_size:
        sink_k = cache.keys[:, :, :n_sink, :]
        sink_v = cache.values[:, :, :n_sink, :]
        win_k  = cache.keys[:, :, -window:, :]
        win_v  = cache.values[:, :, -window:, :]
        cache.keys   = torch.cat([sink_k, win_k], dim=2)
        cache.values = torch.cat([sink_v, win_v], dim=2)
    return cache

print('Three eviction policies: oldest, by_attention, sink+window')
```

## KV Cache Eviction Failure Modes

Naive KV cache eviction strategies fail in characteristic ways. Evicting the oldest tokens (a queue/FIFO policy) works until the sink tokens age out of the cache, at which point perplexity jumps sharply — typically from ~8 to >100 in a single generation step. Evicting by lowest attention score might seem smarter (keep what the model attends to), but this creates a positive feedback loop: once a useful token is evicted, it can no longer receive attention, so it would have been evicted even if retained. Both strategies ultimately fail at sequences longer than the cache size. Only the sink+sliding window strategy produces stable perplexity across arbitrary lengths, because it guarantees that the attention normalization anchors are always available in the KV cache.

```python
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLM

class SinkCache:
    # Minimal StreamingLLM KV cache: retain n_sink initial tokens + rolling window
    def __init__(self, n_sink: int = 4, window_size: int = 512):
        self.n_sink = n_sink
        self.window_size = window_size
        self.sink_keys:   list = []
        self.sink_values: list = []
        self.win_keys:    list = []
        self.win_values:  list = []
        self.total_tokens = 0

    def add(self, key: torch.Tensor, value: torch.Tensor) -> None:
        # key/value shape: (batch, heads, 1, head_dim)
        if self.total_tokens < self.n_sink:
            self.sink_keys.append(key)
            self.sink_values.append(value)
        else:
            self.win_keys.append(key)
            self.win_values.append(value)
            if len(self.win_keys) > self.window_size:
                self.win_keys.pop(0)
                self.win_values.pop(0)
        self.total_tokens += 1

    def get(self) -> tuple:
        all_k = torch.cat(self.sink_keys + self.win_keys, dim=2)
        all_v = torch.cat(self.sink_values + self.win_values, dim=2)
        return all_k, all_v

print(f'SinkCache: 4 sink tokens + 512-token sliding window = 516 total KV entries')
```

## Sink Tokens + Rolling Window

The StreamingLLM KV cache architecture has two components: a fixed sink region containing the first n_sink tokens (typically n_sink=4), and a sliding window containing the most recent window_size tokens. The total cache size is therefore n_sink + window_size — constant regardless of sequence length. When a new token is generated, its KV pair is appended to the window; if the window is full, the oldest window entry is evicted. The sink entries are never evicted. With this scheme, the model always has access to the initial tokens that serve as attention normalization anchors, plus the most recent context for local coherence. The approach enables generation of sequences of arbitrary length — the paper demonstrates stable perplexity at 4 million tokens — with constant memory usage and no architectural changes to the attention mechanism.

```python
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM

def detect_sink_tokens(model_name: str, sample_text: str, n_layers: int = 32):
    # Measure mean attention score per position, averaged over heads and layers
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16,
        output_attentions=True, device_map='auto'
    )
    ids = tokenizer(sample_text, return_tensors='pt', max_length=256,
                    truncation=True).input_ids.cuda()
    with torch.no_grad():
        out = model(ids, output_attentions=True)
    # Average attention received by each position across all heads and layers
    attn_received = torch.zeros(ids.shape[1])
    for layer_attn in out.attentions[:n_layers]:
        # layer_attn: (batch, heads, tgt, src)
        attn_received += layer_attn[0].mean(dim=(0, 1)).cpu().float()
    attn_received /= n_layers
    print('Position | Mean attention received')
    for pos in range(min(8, ids.shape[1])):
        bar = '#' * int(attn_received[pos].item() * 200)
        print(f'  pos {pos:3d}: {attn_received[pos]:.4f}  {bar}')
    return attn_received
```

| KV Eviction Policy | Cache Size (tokens) | PPL at 10K tokens | PPL at 100K tokens | Generation Speed |
| --- | --- | --- | --- | --- |
| Full cache (no eviction) | Grows to OOM at ~8K | 8.1 (normal) | OOM | Degrades as O(n^2) |
| Evict oldest (FIFO) | 512 (fixed) | 8.1 (normal) | 102.4 (collapse) | Constant |
| Evict by attention score | 512 (fixed) | 8.3 (slight drop) | 89.7 (collapse) | Constant |
| Sink (4) + sliding window (508) | 512 (fixed) | 8.1 (stable) | 8.2 (stable) | Constant |

## StreamingLLM Architecture

StreamingLLM modifies inference — not architecture. The base transformer weights are unchanged. The only modification is the KV cache management: instead of a standard growing list or a FIFO queue, a SinkCache object intercepts each new KV pair and routes it to either the sink region or the window. At attention computation time, the model attends over all sink entries plus all window entries, concatenated in their original order. Position IDs are re-indexed at each step to be consistent with the attended sequence — the sink positions retain their original IDs (0 through n_sink-1), and window positions are renumbered relative to their current position in the window. This re-indexing ensures RoPE embeddings remain coherent with the actual attended sequence.

> **Attention Sinks Cost Real Capacity**: Attention sinks mean that models secretly 'use up' attention capacity on initial tokens even when those tokens are irrelevant — adding a dedicated sink token (e.g., a special <sink> prefix) at training time eliminates this waste and improves retrieval. Without a dedicated sink, the model repurposes a real content token as the sink, corrupting its semantic representation.

## Infinite Text Generation

StreamingLLM enables genuinely infinite-length text generation from a pretrained LLM without any modification to the weights. The practical use cases include: real-time transcription and summarization of meeting audio, streaming document completion for very long technical reports, always-on chat assistants that maintain a rolling conversation window, and streaming code generation for entire codebases. The memory usage is bounded by n_sink + window_size KV entries regardless of how long generation continues. The paper reports stable perplexity at 4 million generated tokens with a window of 2048 and 4 sink tokens. Speed matches standard inference: since cache size is constant, attention computation per token is O(window_size) rather than O(n), eliminating the quadratic cost of full-context generation.

- Sink token count: n_sink=4 is sufficient; increasing to 8 provides marginal improvement at minor cache cost.
- Window size: 512-2048 is typical; larger windows improve coherence at higher memory cost.
- Total cache size = n_sink + window_size — constant throughout generation regardless of sequence length.
- Position re-indexing: sink tokens keep original IDs; window tokens are renumbered to maintain RoPE consistency.
- StreamingLLM works out-of-the-box with any RoPE or ALiBi model without weight modification.
- For GPT-2 and BERT-family models (absolute position embeddings), StreamingLLM requires architectural adjustments.

## Key Takeaways

Attention sinks reveal a structural property of softmax attention that has important implications for both efficiency and interpretability. The phenomenon explains why simple KV cache eviction fails: it is not memory limitations that break generation but the loss of the normalization anchor that every attention head implicitly relies on. The StreamingLLM solution is elegant — retain 4 tokens, slide the rest — and requires no retraining, no architectural changes, and negligible implementation complexity. For applications requiring truly long or unbounded generation, StreamingLLM is currently the most practical approach for pretrained models.

- Attention sinks: positions 0-3 receive 10-100x more mean attention than any other position in the sequence.
- Evicting sink tokens from the KV cache causes immediate perplexity collapse from ~8 to >100.
- StreamingLLM fix: always retain the first n_sink=4 KV entries plus a sliding window of recent entries.
- Memory is constant: (n_sink + window_size) KV pairs regardless of total generation length.
- Inference speed is O(window_size) per token, eliminating the quadratic cost of full-context generation.
- Works with any pretrained RoPE model without retraining — pure inference-time modification.
- For training-time fix: add a dedicated <sink> prefix token so the model does not repurpose content tokens.

---

