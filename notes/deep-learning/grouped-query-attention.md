---
title: "Grouped Query Attention (GQA) — Interpolating MHA and MQA"
slug: "grouped-query-attention"
description: "Implement GQA from scratch, convert MHA checkpoints to GQA by mean-pooling K/V heads, build a GQA inference KV cache, and benchmark MHA vs GQA vs MQA on quality and memory."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiR3JvdXBlZCBRdWVyeSBBdHRlbnRpb24gKEdRQSksIGludHJvZHVjZWQgYnkgQWluc2xpZSBldCBhbC4gKDIwMjMpLCBnZW5lcmFsaXNlcyBib3RoIE11bHRpLUhlYWQgQXR0ZW50aW9uIChNSEEpIGFuZCBNdWx0aS1RdWVyeSBBdHRlbnRpb24gKE1RQSkgYnkgZGl2aWRpbmcgdGhlIGggcXVlcnkgaGVhZHMgaW50byBHIGdyb3Vwcy4gRWFjaCBncm91cCBzaGFyZXMgYSBzaW5nbGUgSyBhbmQgViBwcm9qZWN0aW9uLCBzbyB0aGUgbW9kZWwga2VlcHMgaCBxdWVyeSBoZWFkcyBidXQgb25seSBHIEtWIGhlYWRzLiBXaGVuIEcgPSBoIGV2ZXJ5IGhlYWQgaGFzIGl0cyBvd24gSyBhbmQgViDigJQgaWRlbnRpY2FsIHRvIE1IQS4gV2hlbiBHID0gMSBhbGwgaGVhZHMgc2hhcmUgb25lIEsgYW5kIFYg4oCUIGlkZW50aWNhbCB0byBNUUEuIFRoZSBLViBjYWNoZSBhdCBpbmZlcmVuY2UgaXMgcHJvcG9ydGlvbmFsIHRvIEcgcmF0aGVyIHRoYW4gaCwgZ2l2aW5nIGFuIGgvR8OXIG1lbW9yeSByZWR1Y3Rpb24gd2hpbGUgbWFpbnRhaW5pbmcgcXVhbGl0eSBjbG9zZSB0byBNSEEuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU3RhbmRhcmQgTUhBIGFuZCB0aGUgS1YgQ2FjaGUgQm90dGxlbmVjayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQXQgaW5mZXJlbmNlIHRoZSB0cmFuc2Zvcm1lciBLViBjYWNoZSBzdG9yZXMgcGFzdCBrZXlzIGFuZCB2YWx1ZXMgZm9yIGV2ZXJ5IGxheWVyIHRvIGF2b2lkIHJlY29tcHV0YXRpb24uIEZvciBNSEEgd2l0aCBoIGhlYWRzIGFuZCBoZWFkIGRpbWVuc2lvbiBkX2hlYWQgdGhlIGNhY2hlIHBlciBsYXllciBpcyAyIMOXIGggw5cgZF9oZWFkIMOXIEwgZWxlbWVudHMuIEZvciBMTGFNQSAyIDcwQiAoaD02NCwgZF9oZWFkPTEyOCwgTD00MDk2LCBmbG9hdDE2KSB0aGlzIGlzIH42NCBNQiBwZXIgbGF5ZXIsIH41IEdCIGFjcm9zcyA4MCBsYXllcnMg4oCUIGp1c3QgZm9yIEtWLiBNUUEgKEc9MSkgcmVkdWNlcyB0aGlzIGjDlyBidXQgZGVncmFkZXMgb3V0cHV0IHF1YWxpdHkgYnkgMeKAkzMlIG9uIGxvbmctZG9jdW1lbnQgdGFza3MuIEdRQSB3aXRoIEc9OCBhY2hpZXZlcyBhIDTigJM4w5cgS1YgcmVkdWN0aW9uIHdpdGggbmVnbGlnaWJsZSBxdWFsaXR5IGxvc3MsIG1ha2luZyBsb25nLWNvbnRleHQgaW5mZXJlbmNlIHByYWN0aWNhbCBvbiBjb21tb2RpdHkgR1BVIG1lbW9yeS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHUUE6IEdyb3VwaW5nIFF1ZXJ5IEhlYWRzIGFuZCBTaGFyaW5nIEssIFYifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkluIEdRQSB0aGUgaCBxdWVyeSBoZWFkcyBhcmUgcGFydGl0aW9uZWQgaW50byBHIGdyb3VwcyBvZiBzaXplIGgvRy4gRWFjaCBncm91cCB1c2VzIG9uZSBzaGFyZWQgSyBwcm9qZWN0aW9uIGFuZCBvbmUgc2hhcmVkIFYgcHJvamVjdGlvbi4gV19RIHJlbWFpbnMgKGggw5cgZF9oZWFkKSDDlyBkX21vZGVsLCBidXQgV19LIGFuZCBXX1Ygc2hyaW5rIHRvIChHIMOXIGRfaGVhZCkgw5cgZF9tb2RlbC4gRHVyaW5nIHRoZSBmb3J3YXJkIHBhc3MgSyBhbmQgViBhcmUgZXhwYW5kZWQgZnJvbSBHIHRvIGggYnkgcmVwZWF0aW5nIGVhY2ggZ3JvdXBcdTAwMjdzIHJlcHJlc2VudGF0aW9uIGgvRyB0aW1lcyDigJQgYSBjaGVhcCBtZW1vcnkgb3BlcmF0aW9uIHdpdGggbm8gZXh0cmEgbGVhcm5hYmxlIHBhcmFtZXRlcnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuXG5jbGFzcyBHcm91cGVkUXVlcnlBdHRlbnRpb24obm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbCwgbnVtX2hlYWRzLCBudW1fa3ZfZ3JvdXBzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGFzc2VydCBudW1faGVhZHMgJSBudW1fa3ZfZ3JvdXBzID09IDBcbiAgICAgICAgc2VsZi5oID0gbnVtX2hlYWRzXG4gICAgICAgIHNlbGYuRyA9IG51bV9rdl9ncm91cHNcbiAgICAgICAgc2VsZi5xcGcgPSBudW1faGVhZHMgLy8gbnVtX2t2X2dyb3VwcyAgIyBxdWVyaWVzIHBlciBncm91cFxuICAgICAgICBzZWxmLmRfaGVhZCA9IGRfbW9kZWwgLy8gbnVtX2hlYWRzXG4gICAgICAgIHNlbGYuV19xID0gbm4uTGluZWFyKGRfbW9kZWwsIG51bV9oZWFkcyAqIHNlbGYuZF9oZWFkLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLldfayA9IG5uLkxpbmVhcihkX21vZGVsLCBudW1fa3ZfZ3JvdXBzICogc2VsZi5kX2hlYWQsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuV192ID0gbm4uTGluZWFyKGRfbW9kZWwsIG51bV9rdl9ncm91cHMgKiBzZWxmLmRfaGVhZCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5XX28gPSBubi5MaW5lYXIobnVtX2hlYWRzICogc2VsZi5kX2hlYWQsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgQiwgTCwgXyA9IHguc2hhcGVcbiAgICAgICAgUSA9IHNlbGYuV19xKHgpLnZpZXcoQiwgTCwgc2VsZi5oLCBzZWxmLmRfaGVhZCkudHJhbnNwb3NlKDEsIDIpXG4gICAgICAgIEsgPSBzZWxmLldfayh4KS52aWV3KEIsIEwsIHNlbGYuRywgc2VsZi5kX2hlYWQpLnRyYW5zcG9zZSgxLCAyKVxuICAgICAgICBWID0gc2VsZi5XX3YoeCkudmlldyhCLCBMLCBzZWxmLkcsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgSyA9IEsucmVwZWF0X2ludGVybGVhdmUoc2VsZi5xcGcsIGRpbT0xKSAgIyBleHBhbmQgRyAtXHUwMDNlIGhcbiAgICAgICAgViA9IFYucmVwZWF0X2ludGVybGVhdmUoc2VsZi5xcGcsIGRpbT0xKVxuICAgICAgICBhdHRuID0gRi5zb2Z0bWF4KFEgQCBLLnRyYW5zcG9zZSgtMiwgLTEpIC8gbWF0aC5zcXJ0KHNlbGYuZF9oZWFkKSwgZGltPS0xKVxuICAgICAgICBvdXQgPSAoYXR0biBAIFYpLnRyYW5zcG9zZSgxLCAyKS5yZXNoYXBlKEIsIEwsIC0xKVxuICAgICAgICByZXR1cm4gc2VsZi5XX28ob3V0KVxuXG5mb3IgRyBpbiBbMSwgMiwgNCwgOF06ICAjIEc9MTogTVFBLCBHPTg6IE1IQSAoaD04KVxuICAgIG0gPSBHcm91cGVkUXVlcnlBdHRlbnRpb24oZF9tb2RlbD0yNTYsIG51bV9oZWFkcz04LCBudW1fa3ZfZ3JvdXBzPUcpXG4gICAgeCA9IHRvcmNoLnJhbmRuKDIsIDE2LCAyNTYpXG4gICAgb3V0ID0gbSh4KVxuICAgIGt2ID0gc3VtKHAubnVtZWwoKSBmb3IgbiwgcCBpbiBtLm5hbWVkX3BhcmFtZXRlcnMoKSBpZiBcdTAwMjdfa1x1MDAyNyBpbiBuIG9yIFx1MDAyN192XHUwMDI3IGluIG4pXG4gICAgcHJpbnQoZlx1MDAyN0c9e0d9OiBvdXQ9e291dC5zaGFwZX0sIEtWIHBhcmFtcz17a3Z9LCBLViBjYWNoZSByYXRpbz17OC8vR314IHZzIE1IQVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb252ZXJ0aW5nIE1IQSB0byBHUUEgYnkgTWVhbi1Qb29saW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJMTGFNQSAyIDM0QiBhbmQgNzBCIHdlcmUgb3JpZ2luYWxseSB0cmFpbmVkIGFzIE1IQSBtb2RlbHMgYW5kIHRoZW4gY29udmVydGVkIHRvIEdRQSBiZWZvcmUgcmVsZWFzZS4gVGhlIGNvbnZlcnNpb246IHJlc2hhcGUgdGhlIEsgd2VpZ2h0IGZyb20gKGggw5cgZF9oZWFkLCBkX21vZGVsKSBpbnRvIChHLCBoL0csIGRfaGVhZCwgZF9tb2RlbCksIG1lYW4tcG9vbCBhY3Jvc3MgdGhlIGgvRyBoZWFkcyB3aXRoaW4gZWFjaCBncm91cCwgeWllbGRpbmcgKEcsIGRfaGVhZCwgZF9tb2RlbCkuIFRoaXMgbWluaW11bS1kaXN0b3J0aW9uIGFwcHJveGltYXRpb24gaXMgZm9sbG93ZWQgYnkgYSBicmllZiBmaW5lLXR1bmluZyBwaGFzZS4gQWluc2xpZSBldCBhbC4gc2hvd2VkIHRoYXQgdXB0cmFpbmVkIEdRQSBtYXRjaGVzIHNjcmF0Y2gtdHJhaW5lZCBHUUEgcXVhbGl0eSBhZnRlciBzdWZmaWNpZW50IGZpbmUtdHVuaW5nIHN0ZXBzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIG1oYV90b19ncWEoV19rLCBXX3YsIG51bV9oZWFkcywgbnVtX2t2X2dyb3VwcywgZF9oZWFkKTpcbiAgICBcIlwiXCJDb252ZXJ0IE1IQSBLLFYgd2VpZ2h0IG1hdHJpY2VzIHRvIEdRQSBieSBtZWFuLXBvb2xpbmcgd2l0aGluIGdyb3Vwcy5cbiAgICBXX2sgc2hhcGU6IChudW1faGVhZHMgKiBkX2hlYWQsIGRfbW9kZWwpXG4gICAgUmV0dXJuczogICAobnVtX2t2X2dyb3VwcyAqIGRfaGVhZCwgZF9tb2RlbClcbiAgICBcIlwiXCJcbiAgICBxcGcgPSBudW1faGVhZHMgLy8gbnVtX2t2X2dyb3Vwc1xuICAgIGRfbW9kZWwgPSBXX2suc2hhcGVbMV1cbiAgICBXayA9IFdfay52aWV3KG51bV9rdl9ncm91cHMsIHFwZywgZF9oZWFkLCBkX21vZGVsKS5tZWFuKGRpbT0xKVxuICAgIFd2ID0gV192LnZpZXcobnVtX2t2X2dyb3VwcywgcXBnLCBkX2hlYWQsIGRfbW9kZWwpLm1lYW4oZGltPTEpXG4gICAgcmV0dXJuIFdrLnJlc2hhcGUobnVtX2t2X2dyb3VwcyAqIGRfaGVhZCwgZF9tb2RlbCksIFd2LnJlc2hhcGUobnVtX2t2X2dyb3VwcyAqIGRfaGVhZCwgZF9tb2RlbClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbmgsIEcsIGRfaGVhZCwgZF9tb2RlbCA9IDgsIDIsIDMyLCAyNTZcbldrX21oYSA9IHRvcmNoLnJhbmRuKGggKiBkX2hlYWQsIGRfbW9kZWwpXG5Xdl9taGEgPSB0b3JjaC5yYW5kbihoICogZF9oZWFkLCBkX21vZGVsKVxuV2tfZ3FhLCBXdl9ncWEgPSBtaGFfdG9fZ3FhKFdrX21oYSwgV3ZfbWhhLCBoLCBHLCBkX2hlYWQpXG5wcmludChmXHUwMDI3TUhBIFdfSzoge1drX21oYS5zaGFwZX0gIC1cdTAwM2UgR1FBIFdfSzoge1drX2dxYS5zaGFwZX1cdTAwMjcpXG5wcmludChmXHUwMDI3TUhBIEtWIHBhcmFtczoge1drX21oYS5udW1lbCgpKjJ9ICAtXHUwMDNlIEdRQToge1drX2dxYS5udW1lbCgpKjJ9ICAoe2gvL0d9eCByZWR1Y3Rpb24pXHUwMDI3KVxucHJpbnQoZlx1MDAyN0xMYU1BIDIgNzBCOiBoPTY0LCBHPTggLVx1MDAzZSA4eCBLViByZWR1Y3Rpb24gdmlhIHRoaXMgbWVhbi1wb29sICsgZmluZS10dW5lLlx1MDAyNylcbnByaW50KFx1MDAyN0Nvc2luZSBzaW0gb2YgZmlyc3QgZ3JvdXAgKG9yaWdpbmFsIHZzIHBvb2xlZCk6XHUwMDI3KVxub3JpZ19ncm91cDAgPSBXa19taGEudmlldyhHLCBoLy9HLCBkX2hlYWQsIGRfbW9kZWwpWzBdLm1lYW4oMCkgICMgZXhwZWN0ZWQgcG9vbGVkXG5wcmludChmXHUwMDI3ICB7dG9yY2gubm4uZnVuY3Rpb25hbC5jb3NpbmVfc2ltaWxhcml0eShvcmlnX2dyb3VwMC5mbGF0dGVuKCksIFdrX2dxYVs6ZF9oZWFkXS5mbGF0dGVuKCksIGRpbT0wKS5pdGVtKCk6LjZmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHUUEgS1YgQ2FjaGUgYXQgSW5mZXJlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgS1YgY2FjaGUgc3RvcmVzIEcgw5cgZF9oZWFkIMOXIDIgdmFsdWVzIHBlciB0b2tlbiBwZXIgbGF5ZXIgKHZzIGggw5cgZF9oZWFkIMOXIDIgZm9yIE1IQSkuIEF0IGVhY2ggZ2VuZXJhdGlvbiBzdGVwOiBwcm9qZWN0IFEgdG8gaCBoZWFkcywgcHJvamVjdCBLIGFuZCBWIHRvIEcgZ3JvdXBzLCBhcHBlbmQgbmV3IEssViBzbGljZXMgdG8gdGhlIGNhY2hlLCBleHBhbmQgdGhlIGZ1bGwgY2FjaGUgZnJvbSBHIHRvIGggdmlhIHJlcGVhdF9pbnRlcmxlYXZlLCB0aGVuIGNvbXB1dGUgYXR0ZW50aW9uIG92ZXIgdGhlIGNhY2hlZCBzZXF1ZW5jZS4gVGhlIGNhY2hlIGdyb3d0aCBwZXIgdG9rZW4gaXMgRy9oIG9mIE1IQSDigJQgZm9yIEc9OCwgaD02NCwgdGhhdCBpcyA4w5cgbGVzcyBtZW1vcnkgYWxsb2NhdGVkIHBlciBuZXcgdG9rZW4uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuY2xhc3MgR1FBS1ZDYWNoZTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbWF4X2xlbiwgRywgZF9oZWFkKTpcbiAgICAgICAgc2VsZi5HLCBzZWxmLmQsIHNlbGYudCA9IEcsIGRfaGVhZCwgMFxuICAgICAgICBzZWxmLksgPSB0b3JjaC56ZXJvcygxLCBHLCBtYXhfbGVuLCBkX2hlYWQpXG4gICAgICAgIHNlbGYuViA9IHRvcmNoLnplcm9zKDEsIEcsIG1heF9sZW4sIGRfaGVhZClcblxuICAgIGRlZiBzdGVwKHNlbGYsIHEsIGssIHYpOlxuICAgICAgICBcIlwiXCJxOiAoMSxoLDEsZCkgIGsvdjogKDEsRywxLGQpLiBSZXR1cm5zICgxLGgsMSxkKS5cIlwiXCJcbiAgICAgICAgc2VsZi5LWzosIDosIHNlbGYudDpzZWxmLnQrMV0gPSBrXG4gICAgICAgIHNlbGYuVls6LCA6LCBzZWxmLnQ6c2VsZi50KzFdID0gdlxuICAgICAgICBzZWxmLnQgKz0gMVxuICAgICAgICBLYyA9IHNlbGYuS1s6LCA6LCA6c2VsZi50XSAgIyAoMSxHLHQsZClcbiAgICAgICAgVmMgPSBzZWxmLlZbOiwgOiwgOnNlbGYudF1cbiAgICAgICAgaCA9IHEuc2hhcGVbMV1cbiAgICAgICAgS2MgPSBLYy5yZXBlYXRfaW50ZXJsZWF2ZShoIC8vIHNlbGYuRywgZGltPTEpXG4gICAgICAgIFZjID0gVmMucmVwZWF0X2ludGVybGVhdmUoaCAvLyBzZWxmLkcsIGRpbT0xKVxuICAgICAgICBzY29yZXMgPSBxIEAgS2MudHJhbnNwb3NlKC0yLCAtMSkgLyBtYXRoLnNxcnQoc2VsZi5kKVxuICAgICAgICByZXR1cm4gRi5zb2Z0bWF4KHNjb3JlcywgZGltPS0xKSBAIFZjXG5cbmgsIEcsIGQsIG1heF9sZW4gPSA4LCAyLCAzMiwgMTI4XG5jYWNoZSA9IEdRQUtWQ2FjaGUobWF4X2xlbiwgRywgZClcbmZvciBfIGluIHJhbmdlKDIwKTpcbiAgICBvdXQgPSBjYWNoZS5zdGVwKHRvcmNoLnJhbmRuKDEsaCwxLGQpLCB0b3JjaC5yYW5kbigxLEcsMSxkKSwgdG9yY2gucmFuZG4oMSxHLDEsZCkpXG5wcmludChmXHUwMDI3QWZ0ZXIge2NhY2hlLnR9IHN0ZXBzOiBjYWNoZSBLID0ge2NhY2hlLktbOiw6LDpjYWNoZS50XS5zaGFwZX1cdTAwMjcpXG5mb3IgZywgbGFiZWwgaW4gWyhoLFx1MDAyN01IQVx1MDAyNyksIChHLFx1MDAyN0dRQVx1MDAyNyldOlxuICAgIGtiID0gZyAqIGQgKiBtYXhfbGVuICogMiAqIDIgLyAxMDI0ICAjIEsrViwgZmxvYXQxNlxuICAgIHByaW50KGZcdTAwMjd7bGFiZWx9IChHPXtnfSk6IHtrYjouMWZ9IEtCL2xheWVyICByYXRpbz17aC8vZ314XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJlbmNobWFyazogTUhBIHZzIEdRQSB2cyBNUUEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSB0aHJvdWdocHV0IGJlbmVmaXQgb2YgR1FBIGF0IGluZmVyZW5jZSBpcyBkb21pbmF0ZWQgYnkgS1YgY2FjaGUgc2l6ZS4gV2hlbiB0aGUgY2FjaGUgZml0cyBpbiBIQk0gcmF0aGVyIHRoYW4gRFJBTSwgZ2VuZXJhdGlvbiBjYW4gYmUgMuKAkzTDlyBmYXN0ZXIgZHVlIHRvIHJlZHVjZWQgbWVtb3J5IGJhbmR3aWR0aCBwcmVzc3VyZS4gRHVyaW5nIHRyYWluaW5nLCBzbWFsbGVyIFdfSyBhbmQgV19WIG1hdHJpY2VzIHJlZHVjZSB0aGUgS1YgcHJvamVjdGlvbiBGTE9QcyBieSBHL2gsIGJ1dCB0aGlzIGlzIHVzdWFsbHkgYSBzbWFsbCBmcmFjdGlvbiBvZiB0b3RhbCBjb21wdXRlLiBUaGUgcXVhbGl0eSBnYXAgYmV0d2VlbiBNSEEgYW5kIEdRQSAoRz04KSBpcyBcdTAwM2MwLjUgcGVycGxleGl0eSBwb2ludHMgb24gbGFuZ3VhZ2UgbW9kZWxsaW5nIGJlbmNobWFya3M7IE1RQSAoRz0xKSBzaG93cyAx4oCTMyUgZGVncmFkYXRpb24gb24gbG9uZy1kb2N1bWVudCBRQS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgbWF0aFxuaW1wb3J0IHRpbWVcblxuZGVmIGdxYV9hdHRuKFEsIEssIFYsIEcpOlxuICAgIFwiXCJcIlE6IChCLGgsTCxkKSwgSy9WOiAoQixHLEwsZCkuIFJldHVybnMgKEIsaCxMLGQpLlwiXCJcIlxuICAgIGggPSBRLnNoYXBlWzFdXG4gICAgSyA9IEsucmVwZWF0X2ludGVybGVhdmUoaCAvLyBHLCBkaW09MSlcbiAgICBWID0gVi5yZXBlYXRfaW50ZXJsZWF2ZShoIC8vIEcsIGRpbT0xKVxuICAgIHJldHVybiBGLnNvZnRtYXgoUSBAIEsudHJhbnNwb3NlKC0yLC0xKSAvIG1hdGguc3FydChRLnNoYXBlWy0xXSksIGRpbT0tMSkgQCBWXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5CLCBMLCBoLCBkID0gMiwgMjU2LCA4LCA2NFxucHJpbnQoZlwie1x1MDAyN01ldGhvZFx1MDAyNzpcdTAwM2U4fSB7XHUwMDI3R1x1MDAyNzpcdTAwM2U0fSB7XHUwMDI3S1YgY2FjaGUgS0JcdTAwMjc6XHUwMDNlMTN9IHtcdTAwMjdtcy9md2RcdTAwMjc6XHUwMDNlOX0ge1x1MDAyN0tWIHJhdGlvXHUwMDI3Olx1MDAzZTEwfVwiKVxuZm9yIEcgaW4gW2gsIDQsIDIsIDFdOlxuICAgIFEgPSB0b3JjaC5yYW5kbihCLCBoLCBMLCBkKVxuICAgIEsgPSB0b3JjaC5yYW5kbihCLCBHLCBMLCBkKVxuICAgIFYgPSB0b3JjaC5yYW5kbihCLCBHLCBMLCBkKVxuICAgIHJ1bnMgPSAzMFxuICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGZvciBfIGluIHJhbmdlKHJ1bnMpOlxuICAgICAgICBfID0gZ3FhX2F0dG4oUSwgSywgViwgRylcbiAgICBtcyA9ICh0aW1lLnBlcmZfY291bnRlcigpIC0gdDApIC8gcnVucyAqIDEwMDBcbiAgICBrdl9rYiA9IEcgKiBkICogTCAqIDIgKiAyIC8gMTAyNCAgIyBLK1YsIGZsb2F0MTZcbiAgICBsYWJlbCA9IFx1MDAyN01IQVx1MDAyNyBpZiBHID09IGggZWxzZSAoXHUwMDI3TVFBXHUwMDI3IGlmIEcgPT0gMSBlbHNlIGZcdTAwMjdHUUEte0d9XHUwMDI3KVxuICAgIHByaW50KGZcdTAwMjd7bGFiZWw6XHUwMDNlOH0ge0c6XHUwMDNlNH0ge2t2X2tiOlx1MDAzZTEzLjFmfSB7bXM6XHUwMDNlOS4yZn0ge2gvL0c6XHUwMDNlOX14XHUwMDI3KSJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJHIHZhbHVlIiwiS1YgaGVhZHMiLCJRdWFsaXR5IHZzIE1IQSIsIktWIGNhY2hlIHJhdGlvIiwiVXNlZCBpbiBMTE1zIiwiTUhBIGNvbnZlcnNpb24iXSwicm93cyI6W1siTUhBIiwiRyA9IGgiLCJoIChhbGwgdW5pcXVlKSIsIkJhc2VsaW5lIChiZXN0KSIsIjHDlyAobGFyZ2VzdCkiLCJHUFQtMiwgQkVSVCwgZWFybHkgTExhTUEiLCJOL0EiXSxbIk1RQSIsIkcgPSAxIiwiMSAoYWxsIHNoYXJlZCkiLCLiiJIx4oCTMyUgb24gbG9uZy1kb2MgUUEiLCJow5cgc21hbGxlciIsIlBhTE0sIEZhbGNvbi03QiIsIk1lYW4tcG9vbCBhbGwgaCBoZWFkcyB0byAxIl0sWyJHUUEiLCIxIFx1MDAzYyBHIFx1MDAzYyBoIiwiRyAoZ3JvdXBlZCkiLCLiiYhNSEEgd2l0aCBHIOKJpSA0IiwiaC9Hw5cgc21hbGxlciIsIkxMYU1BIDIvMywgTWlzdHJhbCwgR2VtbWEsIFF3ZW4iLCJNZWFuLXBvb2wgaC9HIGhlYWRzIHBlciBncm91cCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUXVhbGl0eSBhbmQgRWZmaWNpZW5jeSBUcmFkZS1vZmZzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBaW5zbGllIGV0IGFsLiBiZW5jaG1hcmtlZCBHUUEgb24gVDUtTGFyZ2UgYW5kIFQ1LVhYTC4gV2l0aCBHID0gaC84LCBHUUEgbWF0Y2hlcyBNSEEgcGVycGxleGl0eSBvbiBsYW5ndWFnZSBtb2RlbGxpbmcgYW5kIHN0YXlzIHdpdGhpbiAwLjUlIG9uIHN1bW1hcmlzYXRpb24uIFRoZSBLViBjYWNoZSBpcyBoL0fDlyBzbWFsbGVyOiBmb3IgTExhTUEgNzBCIChoPTY0LCBHPTgpLCB0aGF0IGlzIGFuIDjDlyByZWR1Y3Rpb24uIEJhdGNoIHRocm91Z2hwdXQgYXQgbG9uZy1jb250ZXh0IGluZmVyZW5jZSBpbmNyZWFzZXMgMuKAkzPDlyBiZWNhdXNlIHRoZSBzbWFsbGVyIGNhY2hlIGxldHMgbW9yZSBzZXF1ZW5jZXMgZml0IGluIEdQVSBtZW1vcnkgc2ltdWx0YW5lb3VzbHksIHJhaXNpbmcgYmF0Y2ggc2l6ZSBhbmQgR1BVIHV0aWxpc2F0aW9uLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiR1FBIERlc2lnbiBSdWxlIiwiY29udGVudCI6IlNldCBHIHNvIHRoYXQgaC9HIGlzIGEgcG93ZXIgb2YgMiBhbmQgRyBkaXZpZGVzIGggZXZlbmx5LiBMTGFNQSAyLzMgdXNlIEc9OCBmb3IgbGFyZ2UgbW9kZWxzIChoPTY0IGZvciA3MEIg4oaSIDggS1YgaGVhZHMpLiBNaXN0cmFsIDdCIHVzZXMgRz04IHdpdGggaD0zMiDihpIgNCBLViBoZWFkcy4gU21hbGxlciBtb2RlbHMgbWF5IHVzZSBHPTQgb3IgRz0yLiBNUUEgKEc9MSkgaXMgb25seSByZWNvbW1lbmRlZCB3aGVuIG1lbW9yeSBpcyBzZXZlcmVseSBjb25zdHJhaW5lZCBhbmQgcXVhbGl0eSBkZWdyYWRhdGlvbiBpcyBhY2NlcHRhYmxlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1vZGVscyBhbmQgQ29uZmlndXJhdGlvbnMgVXNpbmcgR1FBIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHUUEgaGFzIGJlY29tZSB0aGUgZGUgZmFjdG8gc3RhbmRhcmQgZm9yIGxhcmdlIHRyYW5zZm9ybWVyIG1vZGVscyBzaW5jZSAyMDIzLiBMTGFNQSAyIGludHJvZHVjZWQgaXQgZm9yIDM0QiBhbmQgNzBCIHZhcmlhbnRzICg3QiBhbmQgMTNCIHJldGFpbmVkIE1IQSkuIExMYU1BIDMgdXNlcyBHUUEgYWNyb3NzIGFsbCBzaXplcyBpbmNsdWRpbmcgOEIuIE1pc3RyYWwgN0IsIE1peHRyYWwgTW9FLCBHZW1tYSwgR2VtbWEgMiwgYW5kIFF3ZW4yIGFsbCBhZG9wdCBHUUEuIFRoZSBjb25zaXN0ZW50IGFkb3B0aW9uIGRlbW9uc3RyYXRlcyB0aGF0IEc9OCBpcyBhIHdlbGwtdmFsaWRhdGVkIGNvbmZpZ3VyYXRpb24gYmFsYW5jaW5nIHF1YWxpdHkgYW5kIGluZmVyZW5jZSBlZmZpY2llbmN5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiTExhTUEgMjogaD0zMiwgRz04IGZvciAzNEI7IGg9NjQsIEc9OCBmb3IgNzBCIOKAlCBjb252ZXJ0ZWQgZnJvbSBNSEEgdmlhIG1lYW4tcG9vbCArIGZpbmUtdHVuZS4iLCJMTGFNQSAzOiBhbGwgc2l6ZXMgdXNlIEdRQSDigJQgOEI6IGg9MzIsIEc9ODsgNzBCOiBoPTY0LCBHPTguIiwiTWlzdHJhbCA3QjogaD0zMiwgRz04IOKGkiA0IEtWIGhlYWRzOyBjb21iaW5lZCB3aXRoIHNsaWRpbmcgd2luZG93IGF0dGVudGlvbi4iLCJHZW1tYSAyOiBHPTEgKE1RQSkgZm9yIDJCOyBHPTQgZm9yIDlCIGFuZCAyN0IgdmFyaWFudHMuIiwiUXdlbjI6IEdRQSBhY3Jvc3MgYWxsIHNpemVzOyA3MkIgdXNlcyBoPTY0LCBHPTguIiwiRmFsY29uIDQwQis6IHVzZXMgTVFBIChHPTEpOyBlYXJsaWVyIEZhbGNvbiBtb2RlbHMgdXNlZCBmdWxsIE1IQS4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Grouped Query Attention (GQA) — Interpolating MHA and MQA

Grouped Query Attention (GQA), introduced by Ainslie et al. (2023), generalises both Multi-Head Attention (MHA) and Multi-Query Attention (MQA) by dividing the h query heads into G groups. Each group shares a single K and V projection, so the model keeps h query heads but only G KV heads. When G = h every head has its own K and V — identical to MHA. When G = 1 all heads share one K and V — identical to MQA. The KV cache at inference is proportional to G rather than h, giving an h/G× memory reduction while maintaining quality close to MHA.

## Standard MHA and the KV Cache Bottleneck

At inference the transformer KV cache stores past keys and values for every layer to avoid recomputation. For MHA with h heads and head dimension d_head the cache per layer is 2 × h × d_head × L elements. For LLaMA 2 70B (h=64, d_head=128, L=4096, float16) this is ~64 MB per layer, ~5 GB across 80 layers — just for KV. MQA (G=1) reduces this h× but degrades output quality by 1–3% on long-document tasks. GQA with G=8 achieves a 4–8× KV reduction with negligible quality loss, making long-context inference practical on commodity GPU memory.

## GQA: Grouping Query Heads and Sharing K, V

In GQA the h query heads are partitioned into G groups of size h/G. Each group uses one shared K projection and one shared V projection. W_Q remains (h × d_head) × d_model, but W_K and W_V shrink to (G × d_head) × d_model. During the forward pass K and V are expanded from G to h by repeating each group's representation h/G times — a cheap memory operation with no extra learnable parameters.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class GroupedQueryAttention(nn.Module):
    def __init__(self, d_model, num_heads, num_kv_groups):
        super().__init__()
        assert num_heads % num_kv_groups == 0
        self.h = num_heads
        self.G = num_kv_groups
        self.qpg = num_heads // num_kv_groups  # queries per group
        self.d_head = d_model // num_heads
        self.W_q = nn.Linear(d_model, num_heads * self.d_head, bias=False)
        self.W_k = nn.Linear(d_model, num_kv_groups * self.d_head, bias=False)
        self.W_v = nn.Linear(d_model, num_kv_groups * self.d_head, bias=False)
        self.W_o = nn.Linear(num_heads * self.d_head, d_model, bias=False)

    def forward(self, x):
        B, L, _ = x.shape
        Q = self.W_q(x).view(B, L, self.h, self.d_head).transpose(1, 2)
        K = self.W_k(x).view(B, L, self.G, self.d_head).transpose(1, 2)
        V = self.W_v(x).view(B, L, self.G, self.d_head).transpose(1, 2)
        K = K.repeat_interleave(self.qpg, dim=1)  # expand G -> h
        V = V.repeat_interleave(self.qpg, dim=1)
        attn = F.softmax(Q @ K.transpose(-2, -1) / math.sqrt(self.d_head), dim=-1)
        out = (attn @ V).transpose(1, 2).reshape(B, L, -1)
        return self.W_o(out)

for G in [1, 2, 4, 8]:  # G=1: MQA, G=8: MHA (h=8)
    m = GroupedQueryAttention(d_model=256, num_heads=8, num_kv_groups=G)
    x = torch.randn(2, 16, 256)
    out = m(x)
    kv = sum(p.numel() for n, p in m.named_parameters() if '_k' in n or '_v' in n)
    print(f'G={G}: out={out.shape}, KV params={kv}, KV cache ratio={8//G}x vs MHA')
```

## Converting MHA to GQA by Mean-Pooling

LLaMA 2 34B and 70B were originally trained as MHA models and then converted to GQA before release. The conversion: reshape the K weight from (h × d_head, d_model) into (G, h/G, d_head, d_model), mean-pool across the h/G heads within each group, yielding (G, d_head, d_model). This minimum-distortion approximation is followed by a brief fine-tuning phase. Ainslie et al. showed that uptrained GQA matches scratch-trained GQA quality after sufficient fine-tuning steps.

```python
import torch

def mha_to_gqa(W_k, W_v, num_heads, num_kv_groups, d_head):
    """Convert MHA K,V weight matrices to GQA by mean-pooling within groups.
    W_k shape: (num_heads * d_head, d_model)
    Returns:   (num_kv_groups * d_head, d_model)
    """
    qpg = num_heads // num_kv_groups
    d_model = W_k.shape[1]
    Wk = W_k.view(num_kv_groups, qpg, d_head, d_model).mean(dim=1)
    Wv = W_v.view(num_kv_groups, qpg, d_head, d_model).mean(dim=1)
    return Wk.reshape(num_kv_groups * d_head, d_model), Wv.reshape(num_kv_groups * d_head, d_model)

torch.manual_seed(0)
h, G, d_head, d_model = 8, 2, 32, 256
Wk_mha = torch.randn(h * d_head, d_model)
Wv_mha = torch.randn(h * d_head, d_model)
Wk_gqa, Wv_gqa = mha_to_gqa(Wk_mha, Wv_mha, h, G, d_head)
print(f'MHA W_K: {Wk_mha.shape}  -> GQA W_K: {Wk_gqa.shape}')
print(f'MHA KV params: {Wk_mha.numel()*2}  -> GQA: {Wk_gqa.numel()*2}  ({h//G}x reduction)')
print(f'LLaMA 2 70B: h=64, G=8 -> 8x KV reduction via this mean-pool + fine-tune.')
print('Cosine sim of first group (original vs pooled):')
orig_group0 = Wk_mha.view(G, h//G, d_head, d_model)[0].mean(0)  # expected pooled
print(f'  {torch.nn.functional.cosine_similarity(orig_group0.flatten(), Wk_gqa[:d_head].flatten(), dim=0).item():.6f}')
```

## GQA KV Cache at Inference

The KV cache stores G × d_head × 2 values per token per layer (vs h × d_head × 2 for MHA). At each generation step: project Q to h heads, project K and V to G groups, append new K,V slices to the cache, expand the full cache from G to h via repeat_interleave, then compute attention over the cached sequence. The cache growth per token is G/h of MHA — for G=8, h=64, that is 8× less memory allocated per new token.

```python
import torch
import torch.nn.functional as F
import math

class GQAKVCache:
    def __init__(self, max_len, G, d_head):
        self.G, self.d, self.t = G, d_head, 0
        self.K = torch.zeros(1, G, max_len, d_head)
        self.V = torch.zeros(1, G, max_len, d_head)

    def step(self, q, k, v):
        """q: (1,h,1,d)  k/v: (1,G,1,d). Returns (1,h,1,d)."""
        self.K[:, :, self.t:self.t+1] = k
        self.V[:, :, self.t:self.t+1] = v
        self.t += 1
        Kc = self.K[:, :, :self.t]  # (1,G,t,d)
        Vc = self.V[:, :, :self.t]
        h = q.shape[1]
        Kc = Kc.repeat_interleave(h // self.G, dim=1)
        Vc = Vc.repeat_interleave(h // self.G, dim=1)
        scores = q @ Kc.transpose(-2, -1) / math.sqrt(self.d)
        return F.softmax(scores, dim=-1) @ Vc

h, G, d, max_len = 8, 2, 32, 128
cache = GQAKVCache(max_len, G, d)
for _ in range(20):
    out = cache.step(torch.randn(1,h,1,d), torch.randn(1,G,1,d), torch.randn(1,G,1,d))
print(f'After {cache.t} steps: cache K = {cache.K[:,:,:cache.t].shape}')
for g, label in [(h,'MHA'), (G,'GQA')]:
    kb = g * d * max_len * 2 * 2 / 1024  # K+V, float16
    print(f'{label} (G={g}): {kb:.1f} KB/layer  ratio={h//g}x')
```

## Benchmark: MHA vs GQA vs MQA

The throughput benefit of GQA at inference is dominated by KV cache size. When the cache fits in HBM rather than DRAM, generation can be 2–4× faster due to reduced memory bandwidth pressure. During training, smaller W_K and W_V matrices reduce the KV projection FLOPs by G/h, but this is usually a small fraction of total compute. The quality gap between MHA and GQA (G=8) is <0.5 perplexity points on language modelling benchmarks; MQA (G=1) shows 1–3% degradation on long-document QA.

```python
import torch
import torch.nn.functional as F
import math
import time

def gqa_attn(Q, K, V, G):
    """Q: (B,h,L,d), K/V: (B,G,L,d). Returns (B,h,L,d)."""
    h = Q.shape[1]
    K = K.repeat_interleave(h // G, dim=1)
    V = V.repeat_interleave(h // G, dim=1)
    return F.softmax(Q @ K.transpose(-2,-1) / math.sqrt(Q.shape[-1]), dim=-1) @ V

torch.manual_seed(0)
B, L, h, d = 2, 256, 8, 64
print(f"{'Method':>8} {'G':>4} {'KV cache KB':>13} {'ms/fwd':>9} {'KV ratio':>10}")
for G in [h, 4, 2, 1]:
    Q = torch.randn(B, h, L, d)
    K = torch.randn(B, G, L, d)
    V = torch.randn(B, G, L, d)
    runs = 30
    t0 = time.perf_counter()
    for _ in range(runs):
        _ = gqa_attn(Q, K, V, G)
    ms = (time.perf_counter() - t0) / runs * 1000
    kv_kb = G * d * L * 2 * 2 / 1024  # K+V, float16
    label = 'MHA' if G == h else ('MQA' if G == 1 else f'GQA-{G}')
    print(f'{label:>8} {G:>4} {kv_kb:>13.1f} {ms:>9.2f} {h//G:>9}x')
```

| Method | G value | KV heads | Quality vs MHA | KV cache ratio | Used in LLMs | MHA conversion |
| --- | --- | --- | --- | --- | --- | --- |
| MHA | G = h | h (all unique) | Baseline (best) | 1× (largest) | GPT-2, BERT, early LLaMA | N/A |
| MQA | G = 1 | 1 (all shared) | −1–3% on long-doc QA | h× smaller | PaLM, Falcon-7B | Mean-pool all h heads to 1 |
| GQA | 1 < G < h | G (grouped) | ≈MHA with G ≥ 4 | h/G× smaller | LLaMA 2/3, Mistral, Gemma, Qwen | Mean-pool h/G heads per group |

## Quality and Efficiency Trade-offs

Ainslie et al. benchmarked GQA on T5-Large and T5-XXL. With G = h/8, GQA matches MHA perplexity on language modelling and stays within 0.5% on summarisation. The KV cache is h/G× smaller: for LLaMA 70B (h=64, G=8), that is an 8× reduction. Batch throughput at long-context inference increases 2–3× because the smaller cache lets more sequences fit in GPU memory simultaneously, raising batch size and GPU utilisation.

> **GQA Design Rule**: Set G so that h/G is a power of 2 and G divides h evenly. LLaMA 2/3 use G=8 for large models (h=64 for 70B → 8 KV heads). Mistral 7B uses G=8 with h=32 → 4 KV heads. Smaller models may use G=4 or G=2. MQA (G=1) is only recommended when memory is severely constrained and quality degradation is acceptable.

## Models and Configurations Using GQA

GQA has become the de facto standard for large transformer models since 2023. LLaMA 2 introduced it for 34B and 70B variants (7B and 13B retained MHA). LLaMA 3 uses GQA across all sizes including 8B. Mistral 7B, Mixtral MoE, Gemma, Gemma 2, and Qwen2 all adopt GQA. The consistent adoption demonstrates that G=8 is a well-validated configuration balancing quality and inference efficiency.

- LLaMA 2: h=32, G=8 for 34B; h=64, G=8 for 70B — converted from MHA via mean-pool + fine-tune.
- LLaMA 3: all sizes use GQA — 8B: h=32, G=8; 70B: h=64, G=8.
- Mistral 7B: h=32, G=8 → 4 KV heads; combined with sliding window attention.
- Gemma 2: G=1 (MQA) for 2B; G=4 for 9B and 27B variants.
- Qwen2: GQA across all sizes; 72B uses h=64, G=8.
- Falcon 40B+: uses MQA (G=1); earlier Falcon models used full MHA.

---

