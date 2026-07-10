---
title: "Transformer Scaling Laws — Chinchilla and Compute-Optimal Training"
slug: "transformer-scaling-laws"
description: "Power-law relationships between model size, dataset size, and loss; Kaplan vs Chinchilla optimal training recipes; estimating FLOPs; and implications for training budget allocation."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmV1cmFsIGxhbmd1YWdlIG1vZGVsIHBlcmZvcm1hbmNlIGZvbGxvd3MgcmVtYXJrYWJseSBzbW9vdGggcG93ZXIgbGF3cyBpbiBtb2RlbCBzaXplLCBkYXRhc2V0IHNpemUsIGFuZCBjb21wdXRlIGJ1ZGdldC4gVGhlc2Ugc2NhbGluZyBsYXdzIOKAlCBmaXJzdCBjaGFyYWN0ZXJpemVkIHN5c3RlbWF0aWNhbGx5IGJ5IEthcGxhbiBldCBhbC4gKDIwMjApIGFuZCB0aGVuIGNvcnJlY3RlZCBieSBIb2ZmbWFubiBldCBhbC4gKDIwMjIsIENoaW5jaGlsbGEpIOKAlCBwcm92aWRlIGEgcHJpbmNpcGxlZCBmcmFtZXdvcmsgZm9yIGRlY2lkaW5nIGhvdyBsYXJnZSB0byBtYWtlIGEgbW9kZWwgYW5kIGhvdyBtYW55IHRva2VucyB0byB0cmFpbiBvbiBmb3IgYSBnaXZlbiBjb21wdXRlIGJ1ZGdldC4gVW5kZXJzdGFuZGluZyB0aGVzZSByZWxhdGlvbnNoaXBzIGhhcyByZXNoYXBlZCBob3cgb3JnYW5pemF0aW9ucyBhbGxvY2F0ZSB0cmFpbmluZyByZXNvdXJjZXMgYW5kIGhhcyBkcml2ZW4gdGhlIHNoaWZ0IHRvd2FyZCB0cmFpbmluZyBzbWFsbGVyIG1vZGVscyBvbiBtb3JlIGRhdGEuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2FwbGFuIGV0IGFsLiBQb3dlciBMYXdzICgyMDIwKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiS2FwbGFuIGV0IGFsLiBmb3VuZCB0aGF0IGxhbmd1YWdlIG1vZGVsIGxvc3MgZm9sbG93cyBwb3dlciBsYXdzIGluIGlzb2xhdGlvbjogTChOKSDiiJ0gTl57Lc6xX059IHdpdGggzrFfTiDiiYggMC4wNzYgKHBhcmFtZXRlcnMpLCBMKEQpIOKInSBEXnstzrFfRH0gd2l0aCDOsV9EIOKJiCAwLjA5NSAodG9rZW5zKSwgYW5kIEwoQykg4oidIENeey3OsV9DfSAoY29tcHV0ZSkuIEtleSBmaW5kaW5nOiBmb3IgYSBmaXhlZCBjb21wdXRlIGJ1ZGdldCwgbW9zdCBidWRnZXQgc2hvdWxkIGdvIHRvIG1vZGVsIHNpemUgKE4pLCB3aXRoIHJlbGF0aXZlbHkgZmV3IHRyYWluaW5nIHRva2VucyDigJQgbW9kZWxzIHdlcmUgc2lnbmlmaWNhbnRseSB1bmRlcnRyYWluZWQuIFRoaXMgbGVkIHRvIEdQVC0zICgxNzVCKSBiZWluZyB0cmFpbmVkIG9uIG9ubHkgfjMwMEIgdG9rZW5zLCBhIHJhdGlvIG9mIH4xLjcgdG9rZW5zIHBlciBwYXJhbWV0ZXIsIHdlbGwgYmVsb3cgd2hhdCBDaGluY2hpbGxhIGxhdGVyIGlkZW50aWZpZWQgYXMgb3B0aW1hbC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNjaXB5Lm9wdGltaXplIGltcG9ydCBjdXJ2ZV9maXRcbmltcG9ydCB3YXJuaW5nc1xud2FybmluZ3MuZmlsdGVyd2FybmluZ3MoXHUwMDI3aWdub3JlXHUwMDI3KVxuXG5kZWYgcG93ZXJfbGF3KHgsIGEsIGFscGhhKTpcbiAgICBcIlwiXCJMID0gYSAqIHheKC1hbHBoYSlcIlwiXCJcbiAgICByZXR1cm4gYSAqIHggKiogKC1hbHBoYSlcblxuIyBTaW11bGF0ZSBsb3NzIG1lYXN1cmVtZW50cyBhY3Jvc3MgbW9kZWwgc2l6ZXMgKGlsbHVzdHJhdGl2ZSlcbm5wLnJhbmRvbS5zZWVkKDQyKVxuTl92YWx1ZXMgPSBucC5hcnJheShbMWU3LCAzZTcsIDFlOCwgM2U4LCAxZTksIDNlOSwgMWUxMF0pXG4jIFRydWUgcmVsYXRpb25zaGlwOiBMKE4pIH4gMi4wICogTl57LTAuMDc2fSArIG5vaXNlXG50cnVlX2FscGhhLCB0cnVlX2EgPSAwLjA3NiwgMi4wXG5ub2lzZSA9IG5wLnJhbmRvbS5ub3JtYWwoMCwgMC4wMDUsIGxlbihOX3ZhbHVlcykpXG5MX3ZhbHVlcyA9IHRydWVfYSAqIE5fdmFsdWVzICoqICgtdHJ1ZV9hbHBoYSkgKyBub2lzZVxuXG4jIEZpdCBwb3dlciBsYXdcbnBvcHQsIF8gPSBjdXJ2ZV9maXQocG93ZXJfbGF3LCBOX3ZhbHVlcywgTF92YWx1ZXMsIHAwPVsyLjAsIDAuMDhdKVxuYV9maXQsIGFscGhhX2ZpdCA9IHBvcHRcbnByaW50KGZcdTAwMjdGaXR0ZWQgYSA9IHthX2ZpdDouNGZ9LCBhbHBoYV9OID0ge2FscGhhX2ZpdDouNGZ9ICh0cnVlID0ge3RydWVfYWxwaGF9KVx1MDAyNylcbnByaW50KClcbnByaW50KGZcdTAwMjd7XHUwMDI3UGFyYW1zXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3VHJ1ZSBMb3NzXHUwMDI3Olx1MDAzZTEwfSB7XHUwMDI3UHJlZCBMb3NzXHUwMDI3Olx1MDAzZTEwfVx1MDAyNylcbmZvciBOLCBMIGluIHppcChOX3ZhbHVlcywgTF92YWx1ZXMpOlxuICAgIHByZWQgPSBwb3dlcl9sYXcoTiwgYV9maXQsIGFscGhhX2ZpdClcbiAgICBwcmludChmXHUwMDI3e046XHUwMDNlMTIuMWV9IHtMOlx1MDAzZTEwLjRmfSB7cHJlZDpcdTAwM2UxMC40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ2hpbmNoaWxsYTogQ29tcHV0ZS1PcHRpbWFsIFRyYWluaW5nICgyMDIyKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiSG9mZm1hbm4gZXQgYWwuICgyMDIyKSByYW4gYSByaWdvcm91cyBhYmxhdGlvbjogdHJhaW4gbWFueSBtb2RlbHMgb2YgZGlmZmVyZW50IHNpemVzIG9uIGRpZmZlcmVudCB0b2tlbiBjb3VudHMsIGFsbCBhdCB0aGUgc2FtZSBjb21wdXRlIGJ1ZGdldC4gRmluZGluZzogdGhlIGNvbXB1dGUtb3B0aW1hbCBtb2RlbCBzaXplIHNjYWxlcyBhcyBOX29wdCDiiJ0gQ157MC41fSBhbmQgdGhlIG9wdGltYWwgdG9rZW4gY291bnQgc2NhbGVzIGFzIERfb3B0IOKInSBDXnswLjV9IOKAlCBib3RoIHNob3VsZCBzY2FsZSBlcXVhbGx5IHdpdGggY29tcHV0ZS4gVGhlIHJhdGlvIGlzIGFwcHJveGltYXRlbHkgMjAgdG9rZW5zIHBlciBwYXJhbWV0ZXIgZm9yIGNvbXB1dGUtb3B0aW1hbCB0cmFpbmluZy4gVGhpcyBzaG93ZWQgdGhhdCBHUFQtMyAoMTc1QiBvbiAzMDBCIHRva2VucyDiiYggMS43IHRvay9wYXJhbSkgd2FzIHNldmVyZWx5IHVuZGVydHJhaW5lZC4gVGhlIDcwQiBDaGluY2hpbGxhIG1vZGVsIHRyYWluZWQgb24gMS40VCB0b2tlbnMgKDIwIHRvay9wYXJhbSkgb3V0cGVyZm9ybWVkIDI4MEIgR29waGVyIGF0IHRoZSBzYW1lIHRyYWluaW5nIGNvbXB1dGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgY2hpbmNoaWxsYV9vcHRpbWFsKGNvbXB1dGVfYnVkZ2V0X2Zsb3BzLCB0b2tlbnNfcGVyX3BhcmFtPTIwLjApOlxuICAgIFwiXCJcIlxuICAgIEdpdmVuIGEgY29tcHV0ZSBidWRnZXQgQyAoRkxPUHMpLCByZXR1cm4gb3B0aW1hbCBOIGFuZCBELlxuICAgIEFwcHJveGltYXRpb246IEMgPSA2Kk4qRCA9XHUwMDNlIE5fb3B0ID0gc3FydChDIC8gKDYgKiB0b2tlbnNfcGVyX3BhcmFtKSlcbiAgICBcIlwiXCJcbiAgICBOX29wdCA9IG5wLnNxcnQoY29tcHV0ZV9idWRnZXRfZmxvcHMgLyAoNi4wICogdG9rZW5zX3Blcl9wYXJhbSkpXG4gICAgRF9vcHQgPSB0b2tlbnNfcGVyX3BhcmFtICogTl9vcHRcbiAgICByZXR1cm4gaW50KE5fb3B0KSwgaW50KERfb3B0KVxuXG4jIENvbXB1dGUgYnVkZ2V0cyBpbiBGTE9QcyAoYXBwcm94aW1hdGUgZm9yIHdlbGwta25vd24gbW9kZWxzKVxubW9kZWxzID0ge1xuICAgIFx1MDAyN0dQVC0zICgxNzVCKVx1MDAyNzogICgxNzVlOSwgIDMwMGU5LCAgIDYgKiAxNzVlOSAqIDMwMGU5KSxcbiAgICBcdTAwMjdHb3BoZXIgKDI4MEIpXHUwMDI3OiAoMjgwZTksICAzMDBlOSwgICA2ICogMjgwZTkgKiAzMDBlOSksXG4gICAgXHUwMDI3Q2hpbmNoaWxsYVx1MDAyNzogICAgKDcwZTksICAgMS40ZTEyLCAgNiAqIDcwZTkgICogMS40ZTEyKSxcbiAgICBcdTAwMjdMTGFNQS0xICg2NUIpXHUwMDI3OiAoNjVlOSwgICAxLjRlMTIsICA2ICogNjVlOSAgKiAxLjRlMTIpLFxufVxuXG5wcmludChmXHUwMDI3e1x1MDAyN01vZGVsXHUwMDI3Olx1MDAzYzIwfSB7XHUwMDI3QWN0dWFsIE5cdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdBY3R1YWwgRFx1MDAyNzpcdTAwM2UxMn0ge1x1MDAyN0NoaW5jaGlsbGEgTl9vcHRcdTAwMjc6XHUwMDNlMTZ9IHtcdTAwMjdDaGluY2hpbGxhIERfb3B0XHUwMDI3Olx1MDAzZTE2fVx1MDAyNylcbmZvciBuYW1lLCAoTiwgRCwgQykgaW4gbW9kZWxzLml0ZW1zKCk6XG4gICAgbl9vcHQsIGRfb3B0ID0gY2hpbmNoaWxsYV9vcHRpbWFsKEMpXG4gICAgcmF0aW8gPSBEIC8gTlxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2MyMH0ge04vMWU5Olx1MDAzZTEwLjBmfUIge0QvMWU5Olx1MDAzZTEwLjBmfUIge25fb3B0LzFlOTpcdTAwM2UxNC4wZn1CIHtkX29wdC8xZTk6XHUwMDNlMTQuMGZ9QiAgKGFjdHVhbCB7cmF0aW86LjBmfSB0b2svcGFyYW0pXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVzdGltYXRpbmcgVHJhaW5pbmcgQ29tcHV0ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJ1bGUgb2YgdGh1bWIgZm9yIHRyYW5zZm9ybWVyIHRyYWluaW5nIEZMT1BzIGlzIEMg4omIIDZORCwgd2hlcmUgTiBpcyB0aGUgbnVtYmVyIG9mIG5vbi1lbWJlZGRpbmcgcGFyYW1ldGVycyBhbmQgRCBpcyB0aGUgbnVtYmVyIG9mIHRyYWluaW5nIHRva2Vucy4gVGhlIGZhY3RvciA2IGFjY291bnRzIGZvcjogMiBmb3IgdGhlIGZvcndhcmQgcGFzcyAob25lIG11bHRpcGx5LWFkZCA9IDIgRkxPUHMgcGVyIHdlaWdodCksIGFuZCA0IGZvciB0aGUgYmFja3dhcmQgcGFzcyAod2hpY2ggcmVxdWlyZXMgc3RvcmluZyBhY3RpdmF0aW9ucyBhbmQgY29tcHV0aW5nIGdyYWRpZW50cyBmb3IgYm90aCB3ZWlnaHRzIGFuZCBpbnB1dHMsIHJvdWdobHkgMsOXIHRoZSBmb3J3YXJkIHBhc3MgRkxPUHMpLiBUaGlzIGVzdGltYXRlIGlzIGFjY3VyYXRlIHRvIHdpdGhpbiB+MTAlIGZvciBzdGFuZGFyZCB0cmFuc2Zvcm1lciBhcmNoaXRlY3R1cmVzIGFuZCBpZ25vcmVzIGF0dGVudGlvblx1MDAyN3MgTyhUwrIpIGNvc3QgKG9mdGVuIHNtYWxsZXIgdGhhbiBGRk4gZm9yIHR5cGljYWwgc2VxdWVuY2UgbGVuZ3RocykuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgZXN0aW1hdGVfdHJhbnNmb3JtZXJfcGFyYW1zKHZvY2FiX3NpemUsIGRfbW9kZWwsIG5fbGF5ZXJzLCBuX2hlYWRzLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZmZuX211bHQ9NCwgaW5jbHVkZV9lbWJlZGRpbmdzPVRydWUpOlxuICAgIFwiXCJcIkVzdGltYXRlIG5vbi1lbWJlZGRpbmcgdHJhbnNmb3JtZXIgcGFyYW1ldGVycy5cIlwiXCJcbiAgICAjIEF0dGVudGlvbjogUSwgSywgViBwcm9qZWN0aW9ucyArIG91dHB1dCBwcm9qZWN0aW9uXG4gICAgYXR0bl9wYXJhbXMgPSA0ICogZF9tb2RlbCAqIGRfbW9kZWwgICMgcGVyIGxheWVyXG4gICAgIyBGRk46IHR3byBsaW5lYXIgbGF5ZXJzIHdpdGggZXhwYW5zaW9uIGZhY3RvciBmZm5fbXVsdFxuICAgIGZmbl9wYXJhbXMgPSAyICogZF9tb2RlbCAqIGRfbW9kZWwgKiBmZm5fbXVsdCAgIyBwZXIgbGF5ZXJcbiAgICAjIExheWVyTm9ybTogMiAqIGRfbW9kZWwgcGVyIG5vcm0sIDIgbm9ybXMgcGVyIGJsb2NrICsgMSBmaW5hbFxuICAgIGxuX3BhcmFtcyA9ICgyICogbl9sYXllcnMgKyAxKSAqIDIgKiBkX21vZGVsXG4gICAgbm9uX2VtYiA9IG5fbGF5ZXJzICogKGF0dG5fcGFyYW1zICsgZmZuX3BhcmFtcykgKyBsbl9wYXJhbXNcbiAgICBlbWIgPSB2b2NhYl9zaXplICogZF9tb2RlbCAgIyB0b2tlbiBlbWJlZGRpbmcgKHRpZWQgd2l0aCBvdXRwdXQpXG4gICAgcmV0dXJuIG5vbl9lbWIsIG5vbl9lbWIgKyBlbWIgaWYgaW5jbHVkZV9lbWJlZGRpbmdzIGVsc2Ugbm9uX2VtYlxuXG5jb25maWdzID0gW1xuICAgIChcdTAwMjdHUFQtMiBzbWFsbFx1MDAyNywgIDUwMjU3LCA3NjgsICAgMTIsIDEyKSxcbiAgICAoXHUwMDI3R1BULTIgWExcdTAwMjcsICAgICA1MDI1NywgMTYwMCwgIDQ4LCAyNSksXG4gICAgKFx1MDAyN0dQVC0zXHUwMDI3LCAgICAgICAgNTAyNTcsIDEyMjg4LCA5NiwgOTYpLFxuXVxucHJpbnQoZlx1MDAyN3tcdTAwMjdNb2RlbFx1MDAyNzpcdTAwM2MxNX0ge1x1MDAyN05vbi1lbWIgTlx1MDAyNzpcdTAwM2UxMn0ge1x1MDAyN1RvdGFsIE5cdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdDIEAgMzAwQiB0b2tcdTAwMjc6XHUwMDNlMTV9IHtcdTAwMjdDIEAgMS40VCB0b2tcdTAwMjc6XHUwMDNlMTV9XHUwMDI3KVxuZm9yIG5hbWUsIFYsIGQsIEwsIEggaW4gY29uZmlnczpcbiAgICBub25fZW1iLCB0b3RhbCA9IGVzdGltYXRlX3RyYW5zZm9ybWVyX3BhcmFtcyhWLCBkLCBMLCBIKVxuICAgIGNfMzAwYiA9IDYgKiBub25fZW1iICogMzAwZTlcbiAgICBjXzE0dCAgPSA2ICogbm9uX2VtYiAqIDEuNGUxMlxuICAgIHByaW50KGZcdTAwMjd7bmFtZTpcdTAwM2MxNX0ge25vbl9lbWIvMWU5Olx1MDAzZTEwLjJmfUIge3RvdGFsLzFlOTpcdTAwM2UxMC4yZn1CIHtjXzMwMGI6LjJlfSB7Y18xNHQ6LjJlfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsaW5nIExhdyBFeHRyYXBvbGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBIGtleSBwcmFjdGljYWwgdXNlIG9mIHNjYWxpbmcgbGF3cyBpcyBwcmVkaWN0aW5nIHRoZSBwZXJmb3JtYW5jZSBvZiBhIGxhcmdlIG1vZGVsIGJ5IHJ1bm5pbmcgY2hlYXAgc21hbGwtbW9kZWwgZXhwZXJpbWVudHMuIElmIGxvc3MgZm9sbG93cyBMKE4pID0gYU5eey3OsX0sIHlvdSBjYW4gZml0IM6xIGFuZCBhIGZyb20gc2V2ZXJhbCBzbWFsbCBydW5zICgxTeKAkzFCIHBhcmFtZXRlcnMpIGFuZCBleHRyYXBvbGF0ZSB0byAxMEIrLiBSZWxpYWJpbGl0eSBpbXByb3ZlcyB3aGVuIGV4cGVyaW1lbnRzIGFyZSBydW4gYXQgdGhlIHNhbWUgdG9rZW4tdG8tcGFyYW1ldGVyIHJhdGlvIGFzIHRoZSB0YXJnZXQgcnVuLiBUaGUgSXNvRkxPUCBtZXRob2Qg4oCUIHJ1biBtdWx0aXBsZSBtb2RlbHMgYXQgdGhlIHNhbWUgY29tcHV0ZSBidWRnZXQgd2l0aCB2YXJ5aW5nIHNpemVzIOKAlCBpcyBtb3JlIGFjY3VyYXRlIGJlY2F1c2UgaXQgZGlyZWN0bHkgZml0cyB0aGUgQ2hpbmNoaWxsYSB0d28tdmFyaWFibGUgY3VydmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCBudW1weSBhcyBucFxuZnJvbSBzY2lweS5vcHRpbWl6ZSBpbXBvcnQgY3VydmVfZml0XG5cbm5wLnJhbmRvbS5zZWVkKDcpXG5cbiMgU21hbGwgbW9kZWwgZXhwZXJpbWVudHMgKHNpbXVsYXRlZClcbk5fc21hbGwgPSBucC5hcnJheShbMWU2LCAzZTYsIDFlNywgM2U3LCAxZTgsIDNlOF0pXG5hbHBoYV90cnVlLCBhX3RydWUsIExfaXJyZWQgPSAwLjA3NiwgNDA2LjQsIDEuNjlcbiMgQ2hpbmNoaWxsYS1zdHlsZTogTChOKSA9IChOX2MgLyBOKV5hbHBoYSArIExfaXJyZWRcbk5fYyA9IDguOGUxM1xuTF9zbWFsbCA9IChOX2MgLyBOX3NtYWxsKSAqKiBhbHBoYV90cnVlICsgTF9pcnJlZFxuTF9ub2lzeSA9IExfc21hbGwgKyBucC5yYW5kb20ubm9ybWFsKDAsIDAuMDEsIGxlbihOX3NtYWxsKSlcblxuZGVmIGxvc3NfbW9kZWwoTiwgTDAsIE5fYywgYWxwaGEpOlxuICAgIHJldHVybiBMMCArIChOX2MgLyBOKSAqKiBhbHBoYVxuXG5wb3B0LCBfID0gY3VydmVfZml0KGxvc3NfbW9kZWwsIE5fc21hbGwsIExfbm9pc3ksXG4gICAgICAgICAgICAgICAgICAgIHAwPVsxLjcsIDhlMTMsIDAuMDc2XSwgbWF4ZmV2PTEwMDAwKVxuTDBfZml0LCBOY19maXQsIGFscGhhX2ZpdCA9IHBvcHRcblxuIyBFeHRyYXBvbGF0ZSB0byBsYXJnZSBtb2RlbHNcbk5fdGFyZ2V0cyA9IFsxZTksIDFlMTAsIDFlMTEsIDFlMTJdXG5wcmludChmXHUwMDI3Rml0dGVkOiBMMD17TDBfZml0Oi40Zn0sIE5fYz17TmNfZml0Oi4yZX0sIGFscGhhPXthbHBoYV9maXQ6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdcXG57XHUwMDI3VGFyZ2V0IE5cdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdQcmVkIExvc3NcdTAwMjc6XHUwMDNlMTB9IHtcdTAwMjdUcnVlIExvc3NcdTAwMjc6XHUwMDNlMTB9XHUwMDI3KVxuZm9yIE4gaW4gTl90YXJnZXRzOlxuICAgIHByZWQgPSBsb3NzX21vZGVsKE4sIEwwX2ZpdCwgTmNfZml0LCBhbHBoYV9maXQpXG4gICAgdHJ1ZSA9IGxvc3NfbW9kZWwoTiwgTF9pcnJlZCwgTl9jLCBhbHBoYV90cnVlKVxuICAgIHByaW50KGZcdTAwMjd7TjpcdTAwM2UxMi4wZX0ge3ByZWQ6XHUwMDNlMTAuNGZ9IHt0cnVlOlx1MDAzZTEwLjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLYXBsYW4gdnMgQ2hpbmNoaWxsYSBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkFzcGVjdCIsIkthcGxhbiBldCBhbC4gMjAyMCIsIkNoaW5jaGlsbGEgMjAyMiJdLCJyb3dzIjpbWyJPcHRpbWFsIE4gZ2l2ZW4gQyIsIk4g4oidIENeMC43MyDigJQgc2NhbGUgbW9kZWwgZmFzdCIsIk4g4oidIENeMC41IOKAlCBzY2FsZSBtb2RlbCBhbmQgZGF0YSBlcXVhbGx5Il0sWyJPcHRpbWFsIHRvay9wYXJhbSByYXRpbyIsIn4xLjcgdG9rZW5zIHBlciBwYXJhbWV0ZXIiLCJ+MjAgdG9rZW5zIHBlciBwYXJhbWV0ZXIiXSxbIlRyYWluaW5nIGR1cmF0aW9uIiwiU2hvcnQgdHJhaW5pbmcsIGxhcmdlIG1vZGVsIiwiTG9uZ2VyIHRyYWluaW5nLCBzbWFsbGVyIG1vZGVsIl0sWyJLZXkgcHJlZGljdGlvbiIsIkdQVC0zIHN0eWxlIHNjYWxpbmcgaXMgZWZmaWNpZW50IiwiR1BULTMgd2FzIHNldmVyZWx5IHVuZGVydHJhaW5lZCJdLFsiVmFsaWRhdGVkIGJ5IiwiR1BULTMgdHJhaW5pbmcgcnVucyIsIlRyYWluaW5nIENoaW5jaGlsbGEtNzBCIFx1MDAzZSBHb3BoZXItMjgwQiJdLFsiSW1wbGljYXRpb24gZm9yIGluZmVyZW5jZSIsIk5vdCBjb25zaWRlcmVkIOKAlCBmb2N1cyBvbiBwcmV0cmFpbmluZyIsIlNtYWxsZXIgbW9kZWwgPSBmYXN0ZXIsIGNoZWFwZXIgaW5mZXJlbmNlIl1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJJbXBsaWNhdGlvbnMgZm9yIE1vZGVsIFRyYWluaW5nIERlY2lzaW9ucyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ2hpbmNoaWxsYSBvcHRpbWFsIHRyYWluaW5nIG1heGltaXplcyBwZXJwbGV4aXR5IGF0IGEgZml4ZWQgY29tcHV0ZSBidWRnZXQgZHVyaW5nIHRyYWluaW5nLiBCdXQgaW5mZXJlbmNlIGNvc3Qgb2Z0ZW4gbWF0dGVycyBtb3JlIHRoYW4gdHJhaW5pbmcgY29zdCBpbiBwcm9kdWN0aW9uIOKAlCBhIDdCIG1vZGVsIHJ1bnMgb24gYSBzaW5nbGUgR1BVIHdoaWxlIDcwQiByZXF1aXJlcyBtdWx0aS1HUFUuIExMYU1BLTEgZXhwbGljaXRseSBhZG9wdGVkIGFuIGluZmVyZW5jZS1vcHRpbWFsIHN0cmF0ZWd5OiB0cmFpbiA2NUIgYW5kIDdCIG1vZGVscyBvbiAxVC0xLjRUIHRva2VucyAoZXhjZWVkaW5nIENoaW5jaGlsbGEgb3B0aW1hbCBmb3IgdGhlc2Ugc2l6ZXMpLCBhY2NlcHRpbmcgc2xpZ2h0bHkgaGlnaGVyIHRyYWluaW5nIGNvbXB1dGUgaW4gZXhjaGFuZ2UgZm9yIGJldHRlciBpbmZlcmVuY2UgcXVhbGl0eSBwZXIgcGFyYW1ldGVyLiBMTGFNQS0yICgyVCB0b2tlbnMpIGFuZCBzdWJzZXF1ZW50IG1vZGVscyBwdXNoZWQgdGhpcyBmdXJ0aGVyLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50Ijoid2FybmluZyIsInRpdGxlIjoiU2NhbGluZyBMYXdzIEFyZSBOb3QgVW5pdmVyc2FsIiwiY29udGVudCI6IlB1Ymxpc2hlZCBzY2FsaW5nIGxhd3MgYXJlIGZpdCB0byBzcGVjaWZpYyBhcmNoaXRlY3R1cmUgZmFtaWxpZXMsIHRva2VuaXplcnMsIGFuZCBkYXRhIGRpc3RyaWJ1dGlvbnMuIEV4cG9uZW50cyB2YXJ5IGFjcm9zcyBzdHVkaWVzICjOsV9OIHJhbmdlcyBmcm9tIDAuMDUgdG8gMC4xMiBpbiBkaWZmZXJlbnQgcGFwZXJzKS4gQXJjaGl0ZWN0dXJhbCBjaGFuZ2VzIChNb0UsIHN0YXRlLXNwYWNlIG1vZGVscywgYmV0dGVyIGRhdGEgY3VyYXRpb24pIHNoaWZ0IHRoZSBjdXJ2ZXMuIEFsd2F5cyBydW4geW91ciBvd24gc21hbGwtc2NhbGUgaXNvRkxPUCBleHBlcmltZW50cyB3aGVuIG1ha2luZyB0cmFpbmluZyBkZWNpc2lvbnMgZm9yIGEgbmV3IGFyY2hpdGVjdHVyZSBvciBkYXRhIG1peHR1cmUuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJDb21wdXRlIGJ1ZGdldCBDIOKJiCA2TkQgaXMgdGhlIHN0YW5kYXJkIGVzdGltYXRlOyBtb3JlIHByZWNpc2UgZm9ybXVsYXMgYWNjb3VudCBmb3IgYXR0ZW50aW9uIGFuZCBlbWJlZGRpbmcgRkxPUHMuIiwiQ2hpbmNoaWxsYSByYXRpbzogMjAgdG9rL3BhcmFtIGlzIG9wdGltYWwgZm9yIG1pbmltaXppbmcgbG9zcyBhdCBmaXhlZCBwcmV0cmFpbmluZyBjb21wdXRlLiIsIkluZmVyZW5jZS1vcHRpbWFsIG1vZGVscyB0cmFkZSBleHRyYSB0cmFpbmluZyBjb21wdXRlIGZvciBzbWFsbGVyLCBmYXN0ZXItYXQtaW5mZXJlbmNlIG1vZGVscy4iLCJEYXRhIHF1YWxpdHkgbWF0dGVyczogQ2hpbmNoaWxsYSBhbmQgTExhTUEgc2hvdyB0aGF0IGhpZ2gtcXVhbGl0eSBkYXRhIGlzIHdvcnRoIG1vcmUgdGhhbiByYXcgdG9rZW4gY291bnRzLiIsIkVtZXJnZW50IGFiaWxpdGllcyBhcHBlYXIgZGlzY29udGludW91c2x5IGF0IHNjYWxlIGFuZCBhcmUgbm90IHByZWRpY3RlZCBieSBzbW9vdGggcG93ZXItbGF3IGV4dHJhcG9sYXRpb24uIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkxMYU1BIGFuZCBJbmZlcmVuY2UtT3B0aW1hbCBNb2RlbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxMYU1BXHUwMDI3cyB0cmFpbmluZyBwaGlsb3NvcGh5IG9wZXJhdGlvbmFsaXplZCB0aGUgaW5mZXJlbmNlLW9wdGltYWwgaW5zaWdodDogcmF0aGVyIHRoYW4gdHJhaW5pbmcgdGhlIGxhcmdlc3QgY29tcHV0ZS1vcHRpbWFsIG1vZGVsIGZvciBhIHNpbmdsZSBydW4sIHRyYWluIHNtYWxsZXIgbW9kZWxzIGZvciBmYXIgbG9uZ2VyIG9uIGhpZ2hlci1xdWFsaXR5IGRhdGEuIExMYU1BLTEtN0Igd2FzIHRyYWluZWQgb24gMVQgdG9rZW5zIChDaGluY2hpbGxhLW9wdGltYWwgZm9yIH41MEIsIHNvIG92ZXJ0cmFpbmVkIGJ5IDIww5cpLCB5aWVsZGluZyBhIG1vZGVsIHRoYXQgbWF0Y2hlcyBvciBleGNlZWRzIEdQVC0zLTE3NUIgb24gbWFueSBiZW5jaG1hcmtzIHdoaWxlIGJlaW5nIDI1w5cgc21hbGxlci4gTExhTUEtMiBwdXNoZWQgdG8gMlQgdG9rZW5zOyBMTGFNQS0zIHRvIDE1VCB0b2tlbnMg4oCUIGZhciBwYXN0IENoaW5jaGlsbGEgb3B0aW1hbCBmb3IgdGhlaXIgc2l6ZXMuIFRoZSBjb21tdW5pdHkgaGFzIGFkb3B0ZWQgdGhpcyBwYXR0ZXJuOiB0cmFpbiA3QuKAkzcwQiBtb2RlbHMgb24gMeKAkzE1VCB0b2tlbnMsIGFjY2VwdGluZyBoaWdoZXIgcHJldHJhaW5pbmcgY29zdCBmb3IgZHJhbWF0aWMgaW5mZXJlbmNlIHNhdmluZ3MuIn0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Transformer Scaling Laws — Chinchilla and Compute-Optimal Training

Neural language model performance follows remarkably smooth power laws in model size, dataset size, and compute budget. These scaling laws — first characterized systematically by Kaplan et al. (2020) and then corrected by Hoffmann et al. (2022, Chinchilla) — provide a principled framework for deciding how large to make a model and how many tokens to train on for a given compute budget. Understanding these relationships has reshaped how organizations allocate training resources and has driven the shift toward training smaller models on more data.

## Kaplan et al. Power Laws (2020)

Kaplan et al. found that language model loss follows power laws in isolation: L(N) ∝ N^{-α_N} with α_N ≈ 0.076 (parameters), L(D) ∝ D^{-α_D} with α_D ≈ 0.095 (tokens), and L(C) ∝ C^{-α_C} (compute). Key finding: for a fixed compute budget, most budget should go to model size (N), with relatively few training tokens — models were significantly undertrained. This led to GPT-3 (175B) being trained on only ~300B tokens, a ratio of ~1.7 tokens per parameter, well below what Chinchilla later identified as optimal.

```python
import numpy as np
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

def power_law(x, a, alpha):
    """L = a * x^(-alpha)"""
    return a * x ** (-alpha)

# Simulate loss measurements across model sizes (illustrative)
np.random.seed(42)
N_values = np.array([1e7, 3e7, 1e8, 3e8, 1e9, 3e9, 1e10])
# True relationship: L(N) ~ 2.0 * N^{-0.076} + noise
true_alpha, true_a = 0.076, 2.0
noise = np.random.normal(0, 0.005, len(N_values))
L_values = true_a * N_values ** (-true_alpha) + noise

# Fit power law
popt, _ = curve_fit(power_law, N_values, L_values, p0=[2.0, 0.08])
a_fit, alpha_fit = popt
print(f'Fitted a = {a_fit:.4f}, alpha_N = {alpha_fit:.4f} (true = {true_alpha})')
print()
print(f'{'Params':>12} {'True Loss':>10} {'Pred Loss':>10}')
for N, L in zip(N_values, L_values):
    pred = power_law(N, a_fit, alpha_fit)
    print(f'{N:>12.1e} {L:>10.4f} {pred:>10.4f}')
```

## Chinchilla: Compute-Optimal Training (2022)

Hoffmann et al. (2022) ran a rigorous ablation: train many models of different sizes on different token counts, all at the same compute budget. Finding: the compute-optimal model size scales as N_opt ∝ C^{0.5} and the optimal token count scales as D_opt ∝ C^{0.5} — both should scale equally with compute. The ratio is approximately 20 tokens per parameter for compute-optimal training. This showed that GPT-3 (175B on 300B tokens ≈ 1.7 tok/param) was severely undertrained. The 70B Chinchilla model trained on 1.4T tokens (20 tok/param) outperformed 280B Gopher at the same training compute.

```python
import numpy as np

def chinchilla_optimal(compute_budget_flops, tokens_per_param=20.0):
    """
    Given a compute budget C (FLOPs), return optimal N and D.
    Approximation: C = 6*N*D => N_opt = sqrt(C / (6 * tokens_per_param))
    """
    N_opt = np.sqrt(compute_budget_flops / (6.0 * tokens_per_param))
    D_opt = tokens_per_param * N_opt
    return int(N_opt), int(D_opt)

# Compute budgets in FLOPs (approximate for well-known models)
models = {
    'GPT-3 (175B)':  (175e9,  300e9,   6 * 175e9 * 300e9),
    'Gopher (280B)': (280e9,  300e9,   6 * 280e9 * 300e9),
    'Chinchilla':    (70e9,   1.4e12,  6 * 70e9  * 1.4e12),
    'LLaMA-1 (65B)': (65e9,   1.4e12,  6 * 65e9  * 1.4e12),
}

print(f'{'Model':<20} {'Actual N':>12} {'Actual D':>12} {'Chinchilla N_opt':>16} {'Chinchilla D_opt':>16}')
for name, (N, D, C) in models.items():
    n_opt, d_opt = chinchilla_optimal(C)
    ratio = D / N
    print(f'{name:<20} {N/1e9:>10.0f}B {D/1e9:>10.0f}B {n_opt/1e9:>14.0f}B {d_opt/1e9:>14.0f}B  (actual {ratio:.0f} tok/param)')
```

## Estimating Training Compute

The rule of thumb for transformer training FLOPs is C ≈ 6ND, where N is the number of non-embedding parameters and D is the number of training tokens. The factor 6 accounts for: 2 for the forward pass (one multiply-add = 2 FLOPs per weight), and 4 for the backward pass (which requires storing activations and computing gradients for both weights and inputs, roughly 2× the forward pass FLOPs). This estimate is accurate to within ~10% for standard transformer architectures and ignores attention's O(T²) cost (often smaller than FFN for typical sequence lengths).

```python
import numpy as np

def estimate_transformer_params(vocab_size, d_model, n_layers, n_heads,
                                 ffn_mult=4, include_embeddings=True):
    """Estimate non-embedding transformer parameters."""
    # Attention: Q, K, V projections + output projection
    attn_params = 4 * d_model * d_model  # per layer
    # FFN: two linear layers with expansion factor ffn_mult
    ffn_params = 2 * d_model * d_model * ffn_mult  # per layer
    # LayerNorm: 2 * d_model per norm, 2 norms per block + 1 final
    ln_params = (2 * n_layers + 1) * 2 * d_model
    non_emb = n_layers * (attn_params + ffn_params) + ln_params
    emb = vocab_size * d_model  # token embedding (tied with output)
    return non_emb, non_emb + emb if include_embeddings else non_emb

configs = [
    ('GPT-2 small',  50257, 768,   12, 12),
    ('GPT-2 XL',     50257, 1600,  48, 25),
    ('GPT-3',        50257, 12288, 96, 96),
]
print(f'{'Model':<15} {'Non-emb N':>12} {'Total N':>12} {'C @ 300B tok':>15} {'C @ 1.4T tok':>15}')
for name, V, d, L, H in configs:
    non_emb, total = estimate_transformer_params(V, d, L, H)
    c_300b = 6 * non_emb * 300e9
    c_14t  = 6 * non_emb * 1.4e12
    print(f'{name:<15} {non_emb/1e9:>10.2f}B {total/1e9:>10.2f}B {c_300b:.2e} {c_14t:.2e}')
```

## Scaling Law Extrapolation

A key practical use of scaling laws is predicting the performance of a large model by running cheap small-model experiments. If loss follows L(N) = aN^{-α}, you can fit α and a from several small runs (1M–1B parameters) and extrapolate to 10B+. Reliability improves when experiments are run at the same token-to-parameter ratio as the target run. The IsoFLOP method — run multiple models at the same compute budget with varying sizes — is more accurate because it directly fits the Chinchilla two-variable curve.

```python
import numpy as np
from scipy.optimize import curve_fit

np.random.seed(7)

# Small model experiments (simulated)
N_small = np.array([1e6, 3e6, 1e7, 3e7, 1e8, 3e8])
alpha_true, a_true, L_irred = 0.076, 406.4, 1.69
# Chinchilla-style: L(N) = (N_c / N)^alpha + L_irred
N_c = 8.8e13
L_small = (N_c / N_small) ** alpha_true + L_irred
L_noisy = L_small + np.random.normal(0, 0.01, len(N_small))

def loss_model(N, L0, N_c, alpha):
    return L0 + (N_c / N) ** alpha

popt, _ = curve_fit(loss_model, N_small, L_noisy,
                    p0=[1.7, 8e13, 0.076], maxfev=10000)
L0_fit, Nc_fit, alpha_fit = popt

# Extrapolate to large models
N_targets = [1e9, 1e10, 1e11, 1e12]
print(f'Fitted: L0={L0_fit:.4f}, N_c={Nc_fit:.2e}, alpha={alpha_fit:.4f}')
print(f'\n{'Target N':>12} {'Pred Loss':>10} {'True Loss':>10}')
for N in N_targets:
    pred = loss_model(N, L0_fit, Nc_fit, alpha_fit)
    true = loss_model(N, L_irred, N_c, alpha_true)
    print(f'{N:>12.0e} {pred:>10.4f} {true:>10.4f}')
```

## Kaplan vs Chinchilla Comparison

| Aspect | Kaplan et al. 2020 | Chinchilla 2022 |
| --- | --- | --- |
| Optimal N given C | N ∝ C^0.73 — scale model fast | N ∝ C^0.5 — scale model and data equally |
| Optimal tok/param ratio | ~1.7 tokens per parameter | ~20 tokens per parameter |
| Training duration | Short training, large model | Longer training, smaller model |
| Key prediction | GPT-3 style scaling is efficient | GPT-3 was severely undertrained |
| Validated by | GPT-3 training runs | Training Chinchilla-70B > Gopher-280B |
| Implication for inference | Not considered — focus on pretraining | Smaller model = faster, cheaper inference |

## Implications for Model Training Decisions

Chinchilla optimal training maximizes perplexity at a fixed compute budget during training. But inference cost often matters more than training cost in production — a 7B model runs on a single GPU while 70B requires multi-GPU. LLaMA-1 explicitly adopted an inference-optimal strategy: train 65B and 7B models on 1T-1.4T tokens (exceeding Chinchilla optimal for these sizes), accepting slightly higher training compute in exchange for better inference quality per parameter. LLaMA-2 (2T tokens) and subsequent models pushed this further.

> **Scaling Laws Are Not Universal**: Published scaling laws are fit to specific architecture families, tokenizers, and data distributions. Exponents vary across studies (α_N ranges from 0.05 to 0.12 in different papers). Architectural changes (MoE, state-space models, better data curation) shift the curves. Always run your own small-scale isoFLOP experiments when making training decisions for a new architecture or data mixture.

- Compute budget C ≈ 6ND is the standard estimate; more precise formulas account for attention and embedding FLOPs.
- Chinchilla ratio: 20 tok/param is optimal for minimizing loss at fixed pretraining compute.
- Inference-optimal models trade extra training compute for smaller, faster-at-inference models.
- Data quality matters: Chinchilla and LLaMA show that high-quality data is worth more than raw token counts.
- Emergent abilities appear discontinuously at scale and are not predicted by smooth power-law extrapolation.

## LLaMA and Inference-Optimal Models

LLaMA's training philosophy operationalized the inference-optimal insight: rather than training the largest compute-optimal model for a single run, train smaller models for far longer on higher-quality data. LLaMA-1-7B was trained on 1T tokens (Chinchilla-optimal for ~50B, so overtrained by 20×), yielding a model that matches or exceeds GPT-3-175B on many benchmarks while being 25× smaller. LLaMA-2 pushed to 2T tokens; LLaMA-3 to 15T tokens — far past Chinchilla optimal for their sizes. The community has adopted this pattern: train 7B–70B models on 1–15T tokens, accepting higher pretraining cost for dramatic inference savings.

---

