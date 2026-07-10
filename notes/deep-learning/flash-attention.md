---
title: "Flash Attention 1/2/3 — IO-Aware Attention Algorithm"
slug: "flash-attention"
description: "How FlashAttention eliminates O(N²) memory by tiling attention in SRAM, online softmax normalization, backward pass recomputation, and benchmarks vs standard attention."
tags: ["deep-learning", "transformers", "attention-efficiency"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgYXR0ZW50aW9uIHJlcXVpcmVzIG1hdGVyaWFsaXppbmcgdGhlIGZ1bGwgTsOXTiBhdHRlbnRpb24gbWF0cml4IGluIEdQVSBIQk0gKGhpZ2gtYmFuZHdpZHRoIG1lbW9yeSksIGNvbnN1bWluZyBPKE7CsikgbWVtb3J5LiBGb3IgYSBzZXF1ZW5jZSBvZiBsZW5ndGggODE5MiB3aXRoIDMyIGhlYWRzIGluIGZsb2F0MTYsIHRoaXMgaXMgODE5MsKyIMOXIDMyIMOXIDIgYnl0ZXMg4omIIDMyIEdCIOKAlCBleGNlZWRpbmcgdHlwaWNhbCBHUFUgbWVtb3J5IGJ1ZGdldHMuIEZsYXNoQXR0ZW50aW9uIChEYW8gZXQgYWwuIDIwMjIpIHJlZm9ybXVsYXRlcyBhdHRlbnRpb24gYXMgYW4gSU8tYXdhcmUgYWxnb3JpdGhtOiBjb21wdXRlIGF0dGVudGlvbiBpbiB0aWxlcyB0aGF0IGZpdCBlbnRpcmVseSBpbiBTUkFNIChvbi1jaGlwIGNhY2hlKSwgYXZvaWRpbmcgdGhlIHJvdW5kdHJpcCB0byBIQk0uIFRoZSByZXN1bHQgaXMgaWRlbnRpY2FsIHRvIHN0YW5kYXJkIGF0dGVudGlvbiBtYXRoZW1hdGljYWxseSwgYnV0IHVzZXMgTyhOKSBtZW1vcnkgYW5kIHJ1bnMgMuKAkzTDlyBmYXN0ZXIgb24gQTEwMCBHUFVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN0YW5kYXJkIEF0dGVudGlvbjogTyhOwrIpIE1lbW9yeSBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTdGFuZGFyZCBzY2FsZWQgZG90LXByb2R1Y3QgYXR0ZW50aW9uIGNvbXB1dGVzOiBTID0gUUteVC/iiJpkIChOw5dOKSwgUCA9IHNvZnRtYXgoUykgKE7Dl04pLCBPID0gUFYgKE7Dl2QpLiBUaGUgYm90dGxlbmVjayBpcyBzdG9yaW5nIFMgYW5kIFAgaW4gSEJNLiBFYWNoIEhCTSByZWFkL3dyaXRlIGNvc3RzIH4xMOKAkzIwIG5zOyBTUkFNIGFjY2VzcyBjb3N0cyB+MSBucy4gQSBzaW5nbGUgYXR0ZW50aW9uIGNvbXB1dGF0aW9uIGZvciBOPTgxOTIsIGQ9NjQgcmVxdWlyZXMgd3JpdGluZyA4MTkywrIgZmxvYXQxNiB2YWx1ZXMgPSAxMjggTUIgdG8gSEJNLiBBY3Jvc3MgbWFueSBsYXllcnMgYW5kIGJhdGNoIHNpemVzIHRoaXMgZG9taW5hdGVzIHRyYWluaW5nIHRpbWUg4oCUIHRoZSBHUFVcdTAwMjdzIHRlbnNvciBjb3JlcyBhcmUgaWRsZSB3YWl0aW5nIGZvciBtZW1vcnkgdHJhbnNmZXJzLiBUaGUga2V5IGluc2lnaHQgb2YgRmxhc2hBdHRlbnRpb246IHRoZSBtZW1vcnkgYm90dGxlbmVjaywgbm90IEZMT1AgY291bnQsIGxpbWl0cyBhdHRlbnRpb24gc3BlZWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuZGVmIHN0YW5kYXJkX2F0dGVudGlvbihRLCBLLCBWLCBjYXVzYWw9RmFsc2UpOlxuICAgIFwiXCJcIk5haXZlIGF0dGVudGlvbiB0aGF0IG1hdGVyaWFsaXplcyB0aGUgZnVsbCBOIHggTiBtYXRyaXggaW4gbWVtb3J5LlwiXCJcIlxuICAgIHNjYWxlID0gbWF0aC5zcXJ0KFEuc2hhcGVbLTFdKVxuICAgIFMgPSB0b3JjaC5tYXRtdWwoUSwgSy50cmFuc3Bvc2UoLTIsIC0xKSkgLyBzY2FsZSAgIyAoQiwgSCwgTiwgTikgLS0gTyhOXjIpIG1lbW9yeVxuICAgIGlmIGNhdXNhbDpcbiAgICAgICAgTiA9IFEuc2hhcGVbLTJdXG4gICAgICAgIG1hc2sgPSB0b3JjaC50cmlsKHRvcmNoLm9uZXMoTiwgTiwgZGV2aWNlPVEuZGV2aWNlKSkuYm9vbCgpXG4gICAgICAgIFMgPSBTLm1hc2tlZF9maWxsKH5tYXNrLCBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSlcbiAgICBQID0gRi5zb2Z0bWF4KFMsIGRpbT0tMSkgICMgc3RpbGwgTyhOXjIpIGluIG1lbW9yeVxuICAgIHJldHVybiB0b3JjaC5tYXRtdWwoUCwgVikgICMgKEIsIEgsIE4sIGRfaGVhZClcblxuZGVmIGZsYXNoX2F0dGVudGlvbl9yZWZlcmVuY2UoUSwgSywgViwgYmxvY2tfc2l6ZT02NCk6XG4gICAgXCJcIlwiXG4gICAgU2ltcGxpZmllZCBibG9jay13aXNlIGF0dGVudGlvbiBmb3IgY2xhcml0eSAobm90IHRoZSByZWFsIENVREEga2VybmVsKS5cbiAgICBDb21wdXRlcyB0aGUgc2FtZSByZXN1bHQgYXMgc3RhbmRhcmQgYXR0ZW50aW9uIHVzaW5nIHRpbGVkIHNvZnRtYXguXG4gICAgXCJcIlwiXG4gICAgQiwgSCwgTiwgZCA9IFEuc2hhcGVcbiAgICBPID0gdG9yY2guemVyb3NfbGlrZShRKVxuICAgIEwgPSB0b3JjaC56ZXJvcyhCLCBILCBOLCBkZXZpY2U9US5kZXZpY2UpICAgIyBsb2ctc3VtLWV4cCBydW5uaW5nIHN0YXRlXG4gICAgbSA9IHRvcmNoLmZ1bGwoKEIsIEgsIE4pLCBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSwgZGV2aWNlPVEuZGV2aWNlKSAgIyBydW5uaW5nIG1heFxuICAgIHNjYWxlID0gZCAqKiAtMC41XG4gICAgZm9yIGogaW4gcmFuZ2UoMCwgTiwgYmxvY2tfc2l6ZSk6XG4gICAgICAgIEtqID0gS1s6LCA6LCBqOmorYmxvY2tfc2l6ZSwgOl1cbiAgICAgICAgVmogPSBWWzosIDosIGo6aitibG9ja19zaXplLCA6XVxuICAgICAgICBTX2Jsb2NrID0gKFEgQCBLai50cmFuc3Bvc2UoLTIsIC0xKSkgKiBzY2FsZSAgIyAoQiwgSCwgTiwgYmxvY2tfc2l6ZSlcbiAgICAgICAgbV9uZXcgPSB0b3JjaC5tYXhpbXVtKG0sIFNfYmxvY2subWF4KGRpbT0tMSkudmFsdWVzKVxuICAgICAgICBleHBfYmxvY2sgPSB0b3JjaC5leHAoU19ibG9jayAtIG1fbmV3LnVuc3F1ZWV6ZSgtMSkpXG4gICAgICAgIEwgPSB0b3JjaC5leHAobSAtIG1fbmV3KSAqIEwgKyBleHBfYmxvY2suc3VtKGRpbT0tMSlcbiAgICAgICAgTyA9IHRvcmNoLmV4cChtIC0gbV9uZXcpLnVuc3F1ZWV6ZSgtMSkgKiBPICsgZXhwX2Jsb2NrIEAgVmpcbiAgICAgICAgbSA9IG1fbmV3XG4gICAgcmV0dXJuIE8gLyBMLnVuc3F1ZWV6ZSgtMSkgICMgbm9ybWFsaXplXG5cbkIsIEgsIE4sIGQgPSAxLCAxLCA2NCwgMzJcblEgPSB0b3JjaC5yYW5kbihCLCBILCBOLCBkKVxuSyA9IHRvcmNoLnJhbmRuKEIsIEgsIE4sIGQpXG5WID0gdG9yY2gucmFuZG4oQiwgSCwgTiwgZClcbm91dF9zdGQgPSBzdGFuZGFyZF9hdHRlbnRpb24oUSwgSywgVilcbm91dF9mbGFzaCA9IGZsYXNoX2F0dGVudGlvbl9yZWZlcmVuY2UoUSwgSywgViwgYmxvY2tfc2l6ZT0xNilcbnByaW50KGZcdTAwMjdNYXggZGlmZjogeyhvdXRfc3RkIC0gb3V0X2ZsYXNoKS5hYnMoKS5tYXgoKS5pdGVtKCk6LjJlfVx1MDAyNykgICMgbmVhciAwIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiT25saW5lIFNvZnRtYXg6IEluY3JlbWVudGFsIE5vcm1hbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YW5kYXJkIHNvZnRtYXggb3ZlciBhIHJvdyByZXF1aXJlcyB0d28gcGFzc2VzOiBvbmUgdG8gZmluZCB0aGUgbWF4aW11bSAoZm9yIG51bWVyaWNhbCBzdGFiaWxpdHkpIGFuZCBvbmUgdG8gY29tcHV0ZSBleHAgYW5kIHN1bS4gV2hlbiBwcm9jZXNzaW5nIGF0dGVudGlvbiBpbiB0aWxlcywgdGhlIGZ1bGwgcm93IGlzIG5ldmVyIGF2YWlsYWJsZSBhdCBvbmNlLiBPbmxpbmUgc29mdG1heCBtYWludGFpbnMgYSBydW5uaW5nIG1heGltdW0gbSBhbmQgYSBydW5uaW5nIHN1bSBMOiBmb3IgZWFjaCBuZXcgdGlsZSBvZiBzY29yZXMsIHVwZGF0ZSBtX25ldyA9IG1heChtLCBtYXgobmV3X3RpbGUpKSwgdGhlbiByZXNjYWxlIHRoZSBydW5uaW5nIHN1bSBhbmQgYWNjdW11bGF0b3I6IExfbmV3ID0gZXhwKG0g4oiSIG1fbmV3KSDDlyBMICsgzqNleHAocyDiiJIgbV9uZXcpLCBPX25ldyA9IGV4cChtIOKIkiBtX25ldykgw5cgTyArIGV4cChzIOKIkiBtX25ldykgw5cgVi4gVGhpcyBwcm9kdWNlcyBpZGVudGljYWwgb3V0cHV0IHRvIHR3by1wYXNzIHNvZnRtYXggd2hpbGUgbmV2ZXIgbWF0ZXJpYWxpemluZyB0aGUgZnVsbCBOw5dOIG1hdHJpeC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5cbmRlZiBvbmxpbmVfc29mdG1heF9kZW1vKHNjb3Jlc19saXN0KTpcbiAgICBcIlwiXCJcbiAgICBEZW1vbnN0cmF0ZSBvbmxpbmUgc29mdG1heCBmb3IgYSAxRCBzZXF1ZW5jZSBvZiBzY29yZSBjaHVua3MuXG4gICAgRXF1aXZhbGVudCB0byBzb2Z0bWF4KHRvcmNoLmNhdChzY29yZXNfbGlzdCkpIGJ1dCBjb21wdXRlZCBpbmNyZW1lbnRhbGx5LlxuICAgIFwiXCJcIlxuICAgIG0gPSBmbG9hdChcdTAwMjctaW5mXHUwMDI3KSAgIyBydW5uaW5nIG1heFxuICAgIGQgPSAwLjAgICAgICAgICAgICAjIHJ1bm5pbmcgZGVub21pbmF0b3IgKHN1bSBvZiBleHApXG4gICAgbnVtZXJhdG9ycyA9IFtdICAgICMgc3RvcmUgKGNodW5rLCBjb3JyZWN0aW9uX2ZhY3RvcikgcGFpcnNcblxuICAgIGZvciBjaHVuayBpbiBzY29yZXNfbGlzdDpcbiAgICAgICAgbV9jaHVuayA9IGNodW5rLm1heCgpLml0ZW0oKVxuICAgICAgICBpZiBtX2NodW5rIFx1MDAzZSBtOlxuICAgICAgICAgICAgIyBSZXNjYWxlIHByZXZpb3VzIGRlbm9taW5hdG9yIGFuZCBudW1lcmF0b3JzXG4gICAgICAgICAgICBjb3JyZWN0aW9uID0gdG9yY2guZXhwKHRvcmNoLnRlbnNvcihtIC0gbV9jaHVuaykpXG4gICAgICAgICAgICBkID0gZCAqIGNvcnJlY3Rpb24uaXRlbSgpXG4gICAgICAgICAgICBudW1lcmF0b3JzID0gWyhuICogY29ycmVjdGlvbiwgYykgZm9yIG4sIGMgaW4gbnVtZXJhdG9yc11cbiAgICAgICAgICAgIG0gPSBtX2NodW5rXG4gICAgICAgIGV4cF9jaHVuayA9IHRvcmNoLmV4cChjaHVuayAtIG0pXG4gICAgICAgIGQgKz0gZXhwX2NodW5rLnN1bSgpLml0ZW0oKVxuICAgICAgICBudW1lcmF0b3JzLmFwcGVuZCgoZXhwX2NodW5rLCAxLjApKVxuXG4gICAgIyBOb3JtYWxpemUgYWxsIGNodW5rc1xuICAgIHJlc3VsdCA9IHRvcmNoLmNhdChbbiAvIGQgZm9yIG4sIF8gaW4gbnVtZXJhdG9yc10pXG4gICAgcmV0dXJuIHJlc3VsdFxuXG4jIFZlcmlmeSBhZ2FpbnN0IHN0YW5kYXJkIHNvZnRtYXhcbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5mdWxsX3Njb3JlcyA9IHRvcmNoLnJhbmRuKDMyKVxuY2h1bmtzID0gZnVsbF9zY29yZXMuc3BsaXQoOClcbm9ubGluZV9yZXN1bHQgPSBvbmxpbmVfc29mdG1heF9kZW1vKGxpc3QoY2h1bmtzKSlcbnN0YW5kYXJkX3Jlc3VsdCA9IHRvcmNoLnNvZnRtYXgoZnVsbF9zY29yZXMsIGRpbT0wKVxucHJpbnQoZlx1MDAyN01heCBlcnJvcjogeyhvbmxpbmVfcmVzdWx0IC0gc3RhbmRhcmRfcmVzdWx0KS5hYnMoKS5tYXgoKS5pdGVtKCk6LjJlfVx1MDAyNylcbnByaW50KGZcdTAwMjdTdW06IHtvbmxpbmVfcmVzdWx0LnN1bSgpLml0ZW0oKTouNmZ9IChzaG91bGQgYmUgMS4wKVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJVc2luZyBGbGFzaCBBdHRlbnRpb24gaW4gUHlUb3JjaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUHlUb3JjaCAyLjArIGV4cG9zZXMgRmxhc2hBdHRlbnRpb24gdGhyb3VnaCB0b3JjaC5ubi5mdW5jdGlvbmFsLnNjYWxlZF9kb3RfcHJvZHVjdF9hdHRlbnRpb24uIFdoZW4gaW5wdXRzIGFyZSBvbiBDVURBIGluIGZsb2F0MTYgb3IgYmZsb2F0MTYgYW5kIG5vIGN1c3RvbSBtYXNrIGlzIHJlcXVpcmVkLCBQeVRvcmNoIGF1dG9tYXRpY2FsbHkgZGlzcGF0Y2hlcyB0byB0aGUgRmxhc2hBdHRlbnRpb24ga2VybmVsLiBGb3IgY2F1c2FsIChhdXRvcmVncmVzc2l2ZSkgYXR0ZW50aW9uLCBwYXNzIGlzX2NhdXNhbD1UcnVlLiBUaGUgQVBJIGlzIGEgZHJvcC1pbiByZXBsYWNlbWVudCBmb3IgdGhlIG5haXZlIGltcGxlbWVudGF0aW9uLiBUcmFuc2Zvcm1lcnMgbGlicmFyeSB1c2VzIHRoaXMgaW50ZXJuYWxseSB3aGVuIHVzZV9mbGFzaF9hdHRlbnRpb25fMj1UcnVlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuaW1wb3J0IG1hdGhcblxuY2xhc3MgRmxhc2hNSEEobm4uTW9kdWxlKTpcbiAgICBcIlwiXCJNdWx0aS1IZWFkIEF0dGVudGlvbiB1c2luZyBQeVRvcmNoXHUwMDI3cyBidWlsdC1pbiBGbGFzaEF0dGVudGlvbi5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZF9tb2RlbD01MTIsIG5faGVhZHM9OCwgZHJvcG91dD0wLjApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uX2hlYWRzID0gbl9oZWFkc1xuICAgICAgICBzZWxmLmRfaGVhZCA9IGRfbW9kZWwgLy8gbl9oZWFkc1xuICAgICAgICBzZWxmLnFrdiA9IG5uLkxpbmVhcihkX21vZGVsLCAzICogZF9tb2RlbCwgYmlhcz1GYWxzZSlcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uTGluZWFyKGRfbW9kZWwsIGRfbW9kZWwsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuZHJvcG91dCA9IGRyb3BvdXRcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgsIGlzX2NhdXNhbD1GYWxzZSk6XG4gICAgICAgIEIsIFQsIEMgPSB4LnNoYXBlXG4gICAgICAgIHEsIGssIHYgPSBzZWxmLnFrdih4KS5zcGxpdChDLCBkaW09LTEpXG4gICAgICAgIGRlZiByZXNoYXBlKHQpOlxuICAgICAgICAgICAgcmV0dXJuIHQudmlldyhCLCBULCBzZWxmLm5faGVhZHMsIHNlbGYuZF9oZWFkKS50cmFuc3Bvc2UoMSwgMilcbiAgICAgICAgcSwgaywgdiA9IHJlc2hhcGUocSksIHJlc2hhcGUoayksIHJlc2hhcGUodilcbiAgICAgICAgIyBEaXNwYXRjaCB0byBGbGFzaEF0dGVudGlvbiB3aGVuIG9uIENVREEgd2l0aCBmbG9hdDE2L2JmbG9hdDE2XG4gICAgICAgIG91dCA9IEYuc2NhbGVkX2RvdF9wcm9kdWN0X2F0dGVudGlvbihcbiAgICAgICAgICAgIHEsIGssIHYsXG4gICAgICAgICAgICBhdHRuX21hc2s9Tm9uZSxcbiAgICAgICAgICAgIGRyb3BvdXRfcD1zZWxmLmRyb3BvdXQgaWYgc2VsZi50cmFpbmluZyBlbHNlIDAuMCxcbiAgICAgICAgICAgIGlzX2NhdXNhbD1pc19jYXVzYWxcbiAgICAgICAgKVxuICAgICAgICByZXR1cm4gc2VsZi5wcm9qKG91dC50cmFuc3Bvc2UoMSwgMikuY29udGlndW91cygpLnZpZXcoQiwgVCwgQykpXG5cbm1oYSA9IEZsYXNoTUhBKGRfbW9kZWw9NTEyLCBuX2hlYWRzPTgpXG54ID0gdG9yY2gucmFuZG4oNCwgMTI4LCA1MTIpXG5vdXQgPSBtaGEoeCwgaXNfY2F1c2FsPVRydWUpXG5wcmludChmXHUwMDI3T3V0cHV0OiB7b3V0LnNoYXBlfVx1MDAyNykgICMgKDQsIDEyOCwgNTEyKVxucHJpbnQoZlx1MDAyN1VzZXMgZmxhc2ggYXR0ZW50aW9uIHdoZW4gb24gQ1VEQSB3aXRoIGZsb2F0MTZcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQmVuY2htYXJraW5nIFN0YW5kYXJkIHZzIEZsYXNoIEF0dGVudGlvbiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmltcG9ydCB0aW1lXG5pbXBvcnQgbWF0aFxuXG5kZWYgdGltZV9hdHRlbnRpb24oZm4sIFEsIEssIFYsIG5fd2FybXVwPTUsIG5fcnVucz0yMCk6XG4gICAgZm9yIF8gaW4gcmFuZ2Uobl93YXJtdXApOlxuICAgICAgICBmbihRLCBLLCBWKVxuICAgIGlmIFEuaXNfY3VkYTogdG9yY2guY3VkYS5zeW5jaHJvbml6ZSgpXG4gICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl9ydW5zKTpcbiAgICAgICAgZm4oUSwgSywgVilcbiAgICBpZiBRLmlzX2N1ZGE6IHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuICAgIHJldHVybiAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAvIG5fcnVucyAqIDEwMDAgICMgbXNcblxuZGVmIG5haXZlX2F0dG4oUSwgSywgVik6XG4gICAgc2NhbGUgPSBtYXRoLnNxcnQoUS5zaGFwZVstMV0pXG4gICAgcmV0dXJuIEYuc29mdG1heChRIEAgSy50cmFuc3Bvc2UoLTIsIC0xKSAvIHNjYWxlLCBkaW09LTEpIEAgVlxuXG5kZWYgZmxhc2hfYXR0bihRLCBLLCBWKTpcbiAgICByZXR1cm4gRi5zY2FsZWRfZG90X3Byb2R1Y3RfYXR0ZW50aW9uKFEsIEssIFYsIGlzX2NhdXNhbD1UcnVlKVxuXG5kZXZpY2UgPSBcdTAwMjdjdWRhXHUwMDI3IGlmIHRvcmNoLmN1ZGEuaXNfYXZhaWxhYmxlKCkgZWxzZSBcdTAwMjdjcHVcdTAwMjdcbnByaW50KGZcdTAwMjdEZXZpY2U6IHtkZXZpY2V9XHUwMDI3KVxuc2VxX2xlbnMgPSBbNTEyLCAxMDI0LCAyMDQ4LCA0MDk2XVxucHJpbnQoZlx1MDAyN3tcdTAwMjdTZXFMZW5cdTAwMjc6XHUwMDNlOH0ge1x1MDAyN05haXZlIChtcylcdTAwMjc6XHUwMDNlMTJ9IHtcdTAwMjdGbGFzaCAobXMpXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3TmFpdmUgTUJcdTAwMjc6XHUwMDNlMTB9IHtcdTAwMjdTcGVlZHVwXHUwMDI3Olx1MDAzZTh9XHUwMDI3KVxuZm9yIE4gaW4gc2VxX2xlbnM6XG4gICAgQiwgSCwgZCA9IDEsIDE2LCA2NFxuICAgIFEgPSB0b3JjaC5yYW5kbihCLCBILCBOLCBkLCBkZXZpY2U9ZGV2aWNlLCBkdHlwZT10b3JjaC5mbG9hdDE2KVxuICAgIEsgPSB0b3JjaC5yYW5kbihCLCBILCBOLCBkLCBkZXZpY2U9ZGV2aWNlLCBkdHlwZT10b3JjaC5mbG9hdDE2KVxuICAgIFYgPSB0b3JjaC5yYW5kbihCLCBILCBOLCBkLCBkZXZpY2U9ZGV2aWNlLCBkdHlwZT10b3JjaC5mbG9hdDE2KVxuICAgIG5haXZlX21iID0gQiAqIEggKiBOICogTiAqIDIgLyAxZTYgICMgZmxvYXQxNiBieXRlc1xuICAgIHRyeTpcbiAgICAgICAgdF9uYWl2ZSA9IHRpbWVfYXR0ZW50aW9uKG5haXZlX2F0dG4sIFEsIEssIFYpXG4gICAgICAgIHRfZmxhc2ggPSB0aW1lX2F0dGVudGlvbihmbGFzaF9hdHRuLCBRLCBLLCBWKVxuICAgICAgICBzcGVlZHVwID0gdF9uYWl2ZSAvIHRfZmxhc2hcbiAgICAgICAgcHJpbnQoZlx1MDAyN3tOOlx1MDAzZTh9IHt0X25haXZlOlx1MDAzZTEyLjJmfSB7dF9mbGFzaDpcdTAwM2UxMi4yZn0ge25haXZlX21iOlx1MDAzZTEwLjFmfSB7c3BlZWR1cDpcdTAwM2U4LjJmfXhcdTAwMjcpXG4gICAgZXhjZXB0IFJ1bnRpbWVFcnJvciBhcyBlOlxuICAgICAgICBwcmludChmXHUwMDI3e046XHUwMDNlOH0gT09NIGZvciBuYWl2ZTsgZmxhc2ggc3RpbGwgd29ya3NcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRmxhc2hBdHRlbnRpb24gVmVyc2lvbnMgYW5kIEhhcmR3YXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGbGFzaEF0dGVudGlvbi0xIChEYW8gZXQgYWwuIDIwMjIpIGFjaGlldmVkIDLigJM0w5cgc3BlZWR1cCBvbiBBMTAwIGJ5IHJlZHVjaW5nIEhCTSByZWFkcy93cml0ZXMuIFRoZSBiYWNrd2FyZCBwYXNzIHJlY29tcHV0ZXMgYXR0ZW50aW9uIHdlaWdodHMgZnJvbSBRLEssViBpbnN0ZWFkIG9mIHN0b3JpbmcgdGhlIE8oTsKyKSBhdHRlbnRpb24gbWF0cml4IOKAlCB0cmFkaW5nIGNvbXB1dGUgZm9yIG1lbW9yeS4gRmxhc2hBdHRlbnRpb24tMiAoRGFvIDIwMjMpIHJlZHVjZWQgbm9uLW1hdG11bCBGTE9QcyBhbmQgaW1wcm92ZWQgdGhyZWFkIGJsb2NrIHBhcnRpdGlvbmluZywgcmVhY2hpbmcgfjcyJSBvZiBBMTAwIHBlYWsgdXRpbGl6YXRpb24gKHVwIGZyb20gfjI1JSBmb3IgdjEpLiBGbGFzaEF0dGVudGlvbi0zIChTaGFoIGV0IGFsLiAyMDI0KSB0YXJnZXRzIEgxMDA6IHVzZXMgYXN5bmNocm9ub3VzIFRlbnNvciBDb3JlIHBpcGVsaW5lcyBhbmQgdGhlIEgxMDAgVE1BIGluc3RydWN0aW9uIHRvIG92ZXJsYXAgZGF0YSBtb3ZlbWVudCB3aXRoIGNvbXB1dGF0aW9uLCByZWFjaGluZyB+NzUlIG9mIEgxMDBcdTAwMjdzIDk4OSBURkxPUFMuIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IldoZW4gRmxhc2hBdHRlbnRpb24gQ2Fubm90IEJlIFVzZWQiLCJjb250ZW50IjoiUHlUb3JjaFx1MDAyN3MgU0RQQSBkaXNwYXRjaGVzIHRvIEZsYXNoQXR0ZW50aW9uIG9ubHkgd2hlbjogKDEpIGlucHV0IGlzIG9uIENVREEsICgyKSBkdHlwZSBpcyBmbG9hdDE2IG9yIGJmbG9hdDE2LCAoMykgbm8gY3VzdG9tIGF0dGVudGlvbiBtYXNrIGlzIHByb3ZpZGVkIChvbmx5IGlzX2NhdXNhbD1UcnVlIGlzIHN1cHBvcnRlZCBuYXRpdmVseSkuIEZvciBhcmJpdHJhcnkgc3BhcnNlIG1hc2tzLCBjdXN0b20gcG9zaXRpb24gYmlhc2VzIChBTGlCaSwgVDUgcmVsYXRpdmUgYmlhcyksIG9yIGNyb3NzLWF0dGVudGlvbiB3aXRoIGRpZmZlcmVudCBRIGFuZCBLL1YgbGVuZ3Rocywgc3RhbmRhcmQgYXR0ZW50aW9uIG1heSBiZSByZXF1aXJlZCB1bmxlc3MgeW91IHVzZSB0aGUgeGZvcm1lcnMgb3IgZmxhc2gtYXR0biBwYWNrYWdlIGRpcmVjdGx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlN1bW1hcnk6IFN0YW5kYXJkIHZzIEZsYXNoQXR0ZW50aW9uIFZlcnNpb25zIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkF0dHJpYnV0ZSIsIlN0YW5kYXJkIiwiRmxhc2hBdHRlbnRpb24tMSIsIkZsYXNoQXR0ZW50aW9uLTIiLCJGbGFzaEF0dGVudGlvbi0zIl0sInJvd3MiOltbIk1lbW9yeSBjb21wbGV4aXR5IiwiTyhOwrIpIiwiTyhOKSIsIk8oTikiLCJPKE4pIl0sWyJIQk0gcmVhZHMvd3JpdGVzIiwiTyhOwrIpIiwiTyhOIMOXIGQpIiwiTyhOIMOXIGQpIiwiTyhOIMOXIGQpIl0sWyJQZWFrIFRGTE9QUyAoQTEwMCkiLCJ+MTDigJMxNSIsIn42MOKAkzcwIiwifjcyIiwiTi9BIChIMTAwIHRhcmdldCkiXSxbIlBlYWsgVEZMT1BTIChIMTAwKSIsIn4yNSIsIn4xMzAiLCJ+MjAwIiwifjc0MCAoNzUlIHV0aWxpemF0aW9uKSJdLFsiQ2F1c2FsIG1hc2tpbmciLCJGdWxsIG1hc2sgaW4gSEJNIiwiU2tpcCBsb3dlci10cmkgYmxvY2tzIiwiRmV3ZXIgbm9uLW1hdG11bCBvcHMiLCJTYW1lICsgYXN5bmMgcGlwZWxpbmUiXSxbIk1heCBzZXEgbGVuZ3RoIiwifjRLIChtZW1vcnkgYm91bmQpIiwifjY0SyAoY29tcHV0ZSBib3VuZCkiLCJ+MTI4SyIsIn4yNTZLKyJdLFsiQmFja2VuZCIsImN1QkxBUyArIGN1c3RvbSIsIkN1c3RvbSBDVURBIGtlcm5lbCIsIkN1c3RvbSBDVURBIGtlcm5lbCIsIkgxMDAgYXN5bmMgV0dNTUEiXV19LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiQmFja3dhcmQgcGFzczogRmxhc2hBdHRlbnRpb24gcmVjb21wdXRlcyBhdHRlbnRpb24gZnJvbSBRLEssViByYXRoZXIgdGhhbiBzdG9yaW5nIHRoZSBOw5dOIGF0dGVudGlvbiBtYXRyaXgg4oCUIE8oTikgbWVtb3J5IGZvciBiYWNrd2FyZC4iLCJDYXVzYWwgbWFza2luZzogRmxhc2hBdHRlbnRpb24gc2tpcHMgbG93ZXItdHJpYW5ndWxhciBibG9ja3MgZW50aXJlbHkgKHRoZXkgY29udHJpYnV0ZSB6ZXJvIGFmdGVyIOKIkmluZiBtYXNraW5nKSwgaGFsdmluZyBjb21wdXRhdGlvbiBmb3IgY2F1c2FsIG1vZGVscy4iLCJQeVRvcmNoIGludGVncmF0aW9uOiB0b3JjaC5ubi5mdW5jdGlvbmFsLnNjYWxlZF9kb3RfcHJvZHVjdF9hdHRlbnRpb24gYXV0by1zZWxlY3RzIEZsYXNoQXR0ZW50aW9uIGtlcm5lbCB3aGVuIGNvbmRpdGlvbnMgYXJlIG1ldC4iLCJ4Zm9ybWVycyBhbmQgZmxhc2gtYXR0biBwYWNrYWdlcyBleHBvc2UgbG93ZXItbGV2ZWwgQVBJcyBmb3IgY3VzdG9tIG1hc2tzIGFuZCB2YXJpYWJsZS1sZW5ndGggc2VxdWVuY2VzLiIsIkFsbCBtb2Rlcm4gTExNcyAoTExhTUEsIE1pc3RyYWwsIEdQVC00LCBHZW1pbmkpIHVzZSBGbGFzaEF0dGVudGlvbiBhcyBhIHRyYWluaW5nIGFuZCBpbmZlcmVuY2UgcmVxdWlyZW1lbnQuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkJhY2t3YXJkIFBhc3M6IEFjdGl2YXRpb24gUmVjb21wdXRhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3RhbmRhcmQgYXR0ZW50aW9uIHN0b3JlcyB0aGUgTsOXTiBhdHRlbnRpb24gd2VpZ2h0IG1hdHJpeCBQIGR1cmluZyB0aGUgZm9yd2FyZCBwYXNzIHNvIHRoZSBiYWNrd2FyZCBwYXNzIGNhbiBjb21wdXRlIGdyYWRpZW50cyBkTC9kUSA9IGRPIMK3IFBeVCBhbmQgZEwvZEsgPSBRXlQgwrcgZFAgd2l0aG91dCByZWNvbXB1dGluZyBhdHRlbnRpb24uIEZsYXNoQXR0ZW50aW9uLTEgYXZvaWRzIHN0b3JpbmcgUCBieSByZWNvbXB1dGluZyBpdCBkdXJpbmcgdGhlIGJhY2t3YXJkIHBhc3MgZnJvbSB0aGUgc2F2ZWQgUSwgSywgViB0ZW5zb3JzLiBUaGlzIHRyYWRlcyBhbiBleHRyYSBmb3J3YXJkLXBhc3MgY29tcHV0ZSAofjMzJSBvdmVyaGVhZCkgZm9yIGFuIE7CsuKGkk8oTikgcmVkdWN0aW9uIGluIG1lbW9yeS4gVGhlIGJhY2t3YXJkIHBhc3MgdmlzaXRzIGVhY2ggdGlsZSBvZiBRLEssViB0d2ljZSAob25jZSBmb3J3YXJkLCBvbmNlIHJlY29tcHV0ZWQgZm9yIGdyYWRpZW50cyksIHNvIHRoZSB0b3RhbCBiYWNrd2FyZCBwYXNzIGNvc3QgaXMgfjLDlyB0aGUgZm9yd2FyZCBwYXNzLCBzYW1lIGFzIHN0YW5kYXJkIGJhY2twcm9wLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRmxhc2hBdHRlbnRpb24gaXMgbm93IGEgcHJlcmVxdWlzaXRlIGZvciB0cmFpbmluZyBhbnkgc2VyaW91cyBsb25nLWNvbnRleHQgbW9kZWwuIFdpdGhvdXQgaXQsIGEgNDA5Ni10b2tlbiBzZXF1ZW5jZSB3aXRoIDMyIGhlYWRzIGluIGZsb2F0MTYgcmVxdWlyZXMgNDA5NsKyIMOXIDMyIMOXIDIgYnl0ZXMgPSAxIEdCIGp1c3QgZm9yIGF0dGVudGlvbiBtYXRyaWNlcyBwZXIgbGF5ZXIg4oCUIGluZmVhc2libGUgZm9yIG11bHRpLWxheWVyIG1vZGVscy4gV2l0aCBGbGFzaEF0dGVudGlvbiB0aGUgbWVtb3J5IGlzIE8oTiDDlyBkKSDiiYggNDA5NiDDlyAxMjggw5cgMiBieXRlcyA9IDEgTUIgcGVyIGxheWVyLiBUaGlzIDEwMDDDlyByZWR1Y3Rpb24gaW4gYXR0ZW50aW9uIG1lbW9yeSBpcyB3aGF0IG1hZGUgdHJhaW5pbmcgTExhTUEtMiAoNDA5NiBjb250ZXh0KSwgTWlzdHJhbCAoODE5MiksIGFuZCBMbGFtYS0zICgxMzEwNzIpIGZlYXNpYmxlIG9uIHN0YW5kYXJkIEdQVSBjbHVzdGVycy4ifSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Flash Attention 1/2/3 — IO-Aware Attention Algorithm

Standard attention requires materializing the full N×N attention matrix in GPU HBM (high-bandwidth memory), consuming O(N²) memory. For a sequence of length 8192 with 32 heads in float16, this is 8192² × 32 × 2 bytes ≈ 32 GB — exceeding typical GPU memory budgets. FlashAttention (Dao et al. 2022) reformulates attention as an IO-aware algorithm: compute attention in tiles that fit entirely in SRAM (on-chip cache), avoiding the roundtrip to HBM. The result is identical to standard attention mathematically, but uses O(N) memory and runs 2–4× faster on A100 GPUs.

## Standard Attention: O(N²) Memory Problem

Standard scaled dot-product attention computes: S = QK^T/√d (N×N), P = softmax(S) (N×N), O = PV (N×d). The bottleneck is storing S and P in HBM. Each HBM read/write costs ~10–20 ns; SRAM access costs ~1 ns. A single attention computation for N=8192, d=64 requires writing 8192² float16 values = 128 MB to HBM. Across many layers and batch sizes this dominates training time — the GPU's tensor cores are idle waiting for memory transfers. The key insight of FlashAttention: the memory bottleneck, not FLOP count, limits attention speed.

```python
import torch
import torch.nn.functional as F
import math

def standard_attention(Q, K, V, causal=False):
    """Naive attention that materializes the full N x N matrix in memory."""
    scale = math.sqrt(Q.shape[-1])
    S = torch.matmul(Q, K.transpose(-2, -1)) / scale  # (B, H, N, N) -- O(N^2) memory
    if causal:
        N = Q.shape[-2]
        mask = torch.tril(torch.ones(N, N, device=Q.device)).bool()
        S = S.masked_fill(~mask, float('-inf'))
    P = F.softmax(S, dim=-1)  # still O(N^2) in memory
    return torch.matmul(P, V)  # (B, H, N, d_head)

def flash_attention_reference(Q, K, V, block_size=64):
    """
    Simplified block-wise attention for clarity (not the real CUDA kernel).
    Computes the same result as standard attention using tiled softmax.
    """
    B, H, N, d = Q.shape
    O = torch.zeros_like(Q)
    L = torch.zeros(B, H, N, device=Q.device)   # log-sum-exp running state
    m = torch.full((B, H, N), float('-inf'), device=Q.device)  # running max
    scale = d ** -0.5
    for j in range(0, N, block_size):
        Kj = K[:, :, j:j+block_size, :]
        Vj = V[:, :, j:j+block_size, :]
        S_block = (Q @ Kj.transpose(-2, -1)) * scale  # (B, H, N, block_size)
        m_new = torch.maximum(m, S_block.max(dim=-1).values)
        exp_block = torch.exp(S_block - m_new.unsqueeze(-1))
        L = torch.exp(m - m_new) * L + exp_block.sum(dim=-1)
        O = torch.exp(m - m_new).unsqueeze(-1) * O + exp_block @ Vj
        m = m_new
    return O / L.unsqueeze(-1)  # normalize

B, H, N, d = 1, 1, 64, 32
Q = torch.randn(B, H, N, d)
K = torch.randn(B, H, N, d)
V = torch.randn(B, H, N, d)
out_std = standard_attention(Q, K, V)
out_flash = flash_attention_reference(Q, K, V, block_size=16)
print(f'Max diff: {(out_std - out_flash).abs().max().item():.2e}')  # near 0
```

## Online Softmax: Incremental Normalization

Standard softmax over a row requires two passes: one to find the maximum (for numerical stability) and one to compute exp and sum. When processing attention in tiles, the full row is never available at once. Online softmax maintains a running maximum m and a running sum L: for each new tile of scores, update m_new = max(m, max(new_tile)), then rescale the running sum and accumulator: L_new = exp(m − m_new) × L + Σexp(s − m_new), O_new = exp(m − m_new) × O + exp(s − m_new) × V. This produces identical output to two-pass softmax while never materializing the full N×N matrix.

```python
import torch

def online_softmax_demo(scores_list):
    """
    Demonstrate online softmax for a 1D sequence of score chunks.
    Equivalent to softmax(torch.cat(scores_list)) but computed incrementally.
    """
    m = float('-inf')  # running max
    d = 0.0            # running denominator (sum of exp)
    numerators = []    # store (chunk, correction_factor) pairs

    for chunk in scores_list:
        m_chunk = chunk.max().item()
        if m_chunk > m:
            # Rescale previous denominator and numerators
            correction = torch.exp(torch.tensor(m - m_chunk))
            d = d * correction.item()
            numerators = [(n * correction, c) for n, c in numerators]
            m = m_chunk
        exp_chunk = torch.exp(chunk - m)
        d += exp_chunk.sum().item()
        numerators.append((exp_chunk, 1.0))

    # Normalize all chunks
    result = torch.cat([n / d for n, _ in numerators])
    return result

# Verify against standard softmax
torch.manual_seed(0)
full_scores = torch.randn(32)
chunks = full_scores.split(8)
online_result = online_softmax_demo(list(chunks))
standard_result = torch.softmax(full_scores, dim=0)
print(f'Max error: {(online_result - standard_result).abs().max().item():.2e}')
print(f'Sum: {online_result.sum().item():.6f} (should be 1.0)')
```

## Using Flash Attention in PyTorch

PyTorch 2.0+ exposes FlashAttention through torch.nn.functional.scaled_dot_product_attention. When inputs are on CUDA in float16 or bfloat16 and no custom mask is required, PyTorch automatically dispatches to the FlashAttention kernel. For causal (autoregressive) attention, pass is_causal=True. The API is a drop-in replacement for the naive implementation. Transformers library uses this internally when use_flash_attention_2=True.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class FlashMHA(nn.Module):
    """Multi-Head Attention using PyTorch's built-in FlashAttention."""
    def __init__(self, d_model=512, n_heads=8, dropout=0.0):
        super().__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.dropout = dropout

    def forward(self, x, is_causal=False):
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=-1)
        def reshape(t):
            return t.view(B, T, self.n_heads, self.d_head).transpose(1, 2)
        q, k, v = reshape(q), reshape(k), reshape(v)
        # Dispatch to FlashAttention when on CUDA with float16/bfloat16
        out = F.scaled_dot_product_attention(
            q, k, v,
            attn_mask=None,
            dropout_p=self.dropout if self.training else 0.0,
            is_causal=is_causal
        )
        return self.proj(out.transpose(1, 2).contiguous().view(B, T, C))

mha = FlashMHA(d_model=512, n_heads=8)
x = torch.randn(4, 128, 512)
out = mha(x, is_causal=True)
print(f'Output: {out.shape}')  # (4, 128, 512)
print(f'Uses flash attention when on CUDA with float16')
```

## Benchmarking Standard vs Flash Attention

```python
import torch
import torch.nn.functional as F
import time
import math

def time_attention(fn, Q, K, V, n_warmup=5, n_runs=20):
    for _ in range(n_warmup):
        fn(Q, K, V)
    if Q.is_cuda: torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(n_runs):
        fn(Q, K, V)
    if Q.is_cuda: torch.cuda.synchronize()
    return (time.perf_counter() - t0) / n_runs * 1000  # ms

def naive_attn(Q, K, V):
    scale = math.sqrt(Q.shape[-1])
    return F.softmax(Q @ K.transpose(-2, -1) / scale, dim=-1) @ V

def flash_attn(Q, K, V):
    return F.scaled_dot_product_attention(Q, K, V, is_causal=True)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Device: {device}')
seq_lens = [512, 1024, 2048, 4096]
print(f'{'SeqLen':>8} {'Naive (ms)':>12} {'Flash (ms)':>12} {'Naive MB':>10} {'Speedup':>8}')
for N in seq_lens:
    B, H, d = 1, 16, 64
    Q = torch.randn(B, H, N, d, device=device, dtype=torch.float16)
    K = torch.randn(B, H, N, d, device=device, dtype=torch.float16)
    V = torch.randn(B, H, N, d, device=device, dtype=torch.float16)
    naive_mb = B * H * N * N * 2 / 1e6  # float16 bytes
    try:
        t_naive = time_attention(naive_attn, Q, K, V)
        t_flash = time_attention(flash_attn, Q, K, V)
        speedup = t_naive / t_flash
        print(f'{N:>8} {t_naive:>12.2f} {t_flash:>12.2f} {naive_mb:>10.1f} {speedup:>8.2f}x')
    except RuntimeError as e:
        print(f'{N:>8} OOM for naive; flash still works')
```

## FlashAttention Versions and Hardware

FlashAttention-1 (Dao et al. 2022) achieved 2–4× speedup on A100 by reducing HBM reads/writes. The backward pass recomputes attention weights from Q,K,V instead of storing the O(N²) attention matrix — trading compute for memory. FlashAttention-2 (Dao 2023) reduced non-matmul FLOPs and improved thread block partitioning, reaching ~72% of A100 peak utilization (up from ~25% for v1). FlashAttention-3 (Shah et al. 2024) targets H100: uses asynchronous Tensor Core pipelines and the H100 TMA instruction to overlap data movement with computation, reaching ~75% of H100's 989 TFLOPS.

> **When FlashAttention Cannot Be Used**: PyTorch's SDPA dispatches to FlashAttention only when: (1) input is on CUDA, (2) dtype is float16 or bfloat16, (3) no custom attention mask is provided (only is_causal=True is supported natively). For arbitrary sparse masks, custom position biases (ALiBi, T5 relative bias), or cross-attention with different Q and K/V lengths, standard attention may be required unless you use the xformers or flash-attn package directly.

## Summary: Standard vs FlashAttention Versions

| Attribute | Standard | FlashAttention-1 | FlashAttention-2 | FlashAttention-3 |
| --- | --- | --- | --- | --- |
| Memory complexity | O(N²) | O(N) | O(N) | O(N) |
| HBM reads/writes | O(N²) | O(N × d) | O(N × d) | O(N × d) |
| Peak TFLOPS (A100) | ~10–15 | ~60–70 | ~72 | N/A (H100 target) |
| Peak TFLOPS (H100) | ~25 | ~130 | ~200 | ~740 (75% utilization) |
| Causal masking | Full mask in HBM | Skip lower-tri blocks | Fewer non-matmul ops | Same + async pipeline |
| Max seq length | ~4K (memory bound) | ~64K (compute bound) | ~128K | ~256K+ |
| Backend | cuBLAS + custom | Custom CUDA kernel | Custom CUDA kernel | H100 async WGMMA |

- Backward pass: FlashAttention recomputes attention from Q,K,V rather than storing the N×N attention matrix — O(N) memory for backward.
- Causal masking: FlashAttention skips lower-triangular blocks entirely (they contribute zero after −inf masking), halving computation for causal models.
- PyTorch integration: torch.nn.functional.scaled_dot_product_attention auto-selects FlashAttention kernel when conditions are met.
- xformers and flash-attn packages expose lower-level APIs for custom masks and variable-length sequences.
- All modern LLMs (LLaMA, Mistral, GPT-4, Gemini) use FlashAttention as a training and inference requirement.

## Backward Pass: Activation Recomputation

Standard attention stores the N×N attention weight matrix P during the forward pass so the backward pass can compute gradients dL/dQ = dO · P^T and dL/dK = Q^T · dP without recomputing attention. FlashAttention-1 avoids storing P by recomputing it during the backward pass from the saved Q, K, V tensors. This trades an extra forward-pass compute (~33% overhead) for an N²→O(N) reduction in memory. The backward pass visits each tile of Q,K,V twice (once forward, once recomputed for gradients), so the total backward pass cost is ~2× the forward pass, same as standard backprop.

FlashAttention is now a prerequisite for training any serious long-context model. Without it, a 4096-token sequence with 32 heads in float16 requires 4096² × 32 × 2 bytes = 1 GB just for attention matrices per layer — infeasible for multi-layer models. With FlashAttention the memory is O(N × d) ≈ 4096 × 128 × 2 bytes = 1 MB per layer. This 1000× reduction in attention memory is what made training LLaMA-2 (4096 context), Mistral (8192), and Llama-3 (131072) feasible on standard GPU clusters.

---

