---
title: "Forward Pass — Linear Layers, Activations, and Loss"
slug: "forward-pass-neural-network"
description: "Trace the forward pass step by step: linear transformation z=Wx+b, activation a=σ(z), batched matrix form, shape tracking, composition of transformations, cross-entropy and MSE loss, and the computational graph as foundation for autograd."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGZvcndhcmQgcGFzcyBpcyB0aGUgY29tcHV0YXRpb24gdGhhdCB0cmFuc2Zvcm1zIHJhdyBpbnB1dCBpbnRvIGEgcHJlZGljdGlvbi4gRXZlcnkgbGF5ZXIgYXBwbGllcyBhIGxpbmVhciB0cmFuc2Zvcm1hdGlvbiBmb2xsb3dlZCBieSBhIG5vbi1saW5lYXIgYWN0aXZhdGlvbjsgc3RhY2tpbmcgdGhlc2UgbGF5ZXJzIGFsbG93cyB0aGUgbmV0d29yayB0byBhcHByb3hpbWF0ZSBhcmJpdHJhcmlseSBjb21wbGV4IGZ1bmN0aW9ucy4gVW5kZXJzdGFuZGluZyB0aGUgbWVjaGFuaWNzIOKAlCBzaGFwZSB0cmFja2luZywgdmVjdG9yaXNlZCBiYXRjaCBjb21wdXRhdGlvbiwgYW5kIHRoZSBjYWNoZWQgaW50ZXJtZWRpYXRlIHZhbHVlcyDigJQgaXMgcHJlcmVxdWlzaXRlIGZvciBpbXBsZW1lbnRpbmcgYmFja3Byb3BhZ2F0aW9uIGNvcnJlY3RseS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMaW5lYXIgTGF5ZXI6IHogPSBXeCArIGIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc2luZ2xlIGxpbmVhciAoZnVsbHktY29ubmVjdGVkKSBsYXllciBjb21wdXRlcyB6ID0gV3ggKyBiIHdoZXJlIFcg4oiIIOKEnV57ZF9vdXQgw5cgZF9pbn0sIHgg4oiIIOKEnV57ZF9pbn0sIGIg4oiIIOKEnV57ZF9vdXR9LiBGb3IgYSBtaW5pLWJhdGNoIG9mIG0gc2FtcGxlcywgaW5wdXRzIGFyZSBzdGFja2VkIHJvdy13aXNlOiBYIOKIiCDihJ1ee20gw5cgZF9pbn0uIFRoZSBiYXRjaGVkIGZvcm0gaXMgWiA9IFhX4bWAICsgYiB3aGVyZSB0aGUgYmlhcyBiIGJyb2FkY2FzdHMgYWNyb3NzIHRoZSBiYXRjaCBkaW1lbnNpb24sIGdpdmluZyBaIOKIiCDihJ1ee20gw5cgZF9vdXR9LiBTaGFwZSB0cmFja2luZyBpcyBjcml0aWNhbCDigJQgYSBkaW1lbnNpb24gbWlzbWF0Y2ggc2lsZW50bHkgY29ycnVwdHMgY29tcHV0YXRpb25zIHJhdGhlciB0aGFuIHJhaXNpbmcgYW4gZXJyb3IgaW4gc29tZSBmcmFtZXdvcmtzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFjdGl2YXRpb24gRnVuY3Rpb25zIGFuZCBOb24tbGluZWFyaXR5In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJXaXRob3V0IG5vbi1saW5lYXIgYWN0aXZhdGlvbnMsIHN0YWNraW5nIGxpbmVhciBsYXllcnMgY29sbGFwc2VzIHRvIGEgc2luZ2xlIGxpbmVhciBtYXA6IFfigoIoV+KCgXggKyBi4oKBKSArIGLigoIgPSAoV+KCglfigoEpeCArIChX4oKCYuKCgSArIGLigoIpLiBUaGUgbmV0d29yayBjYW5ub3QgcmVwcmVzZW50IFhPUiwgbGV0IGFsb25lIHZpc2lvbiBvciBsYW5ndWFnZSB0YXNrcy4gQW4gYWN0aXZhdGlvbiBhID0gz4MoeikgYXBwbGllZCBlbGVtZW50LXdpc2UgYnJlYWtzIGxpbmVhcml0eS4gQ29tbW9uIGNob2ljZXM6IFJlTFUgYSA9IG1heCgwLCB6KSwgc2lnbW9pZCBhID0gMS8oMStl4oG74ba7KSwgR0VMVSwgYW5kIFNpTFUuIFRoZSBhY3RpdmF0aW9uIGlzIGFwcGxpZWQgYWZ0ZXIgZXZlcnkgbGluZWFyIGxheWVyIGV4Y2VwdCDigJQgdHlwaWNhbGx5IOKAlCB0aGUgZmluYWwgb3V0cHV0IGxheWVyLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbXBvc2l0aW9uIGFuZCB0aGUgQ29tcHV0YXRpb25hbCBHcmFwaCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSB0d28tbGF5ZXIgTUxQIGZvcndhcmQgcGFzczogeuKCgSA9IFhX4oKB4bWAICsgYuKCgSwgYeKCgSA9IFJlTFUoeuKCgSksIHrigoIgPSBh4oKBV+KCguG1gCArIGLigoIsIMW3ID0gc29mdG1heCh64oKCKS4gRWFjaCBpbnRlcm1lZGlhdGUgdmFsdWUgaXMgYSBub2RlIGluIHRoZSBjb21wdXRhdGlvbmFsIGdyYXBoLiBEdXJpbmcgdGhlIGZvcndhcmQgcGFzcyB0aGVzZSB2YWx1ZXMgYXJlIGNhY2hlZCAoeuKCgSwgYeKCgSwgeuKCgikgYmVjYXVzZSB0aGUgYmFja3dhcmQgcGFzcyBuZWVkcyB0aGVtIHRvIGNvbXB1dGUgZ3JhZGllbnRzLiBBdXRvZ3JhZCBlbmdpbmVzIGxpa2UgUHlUb3JjaCBidWlsZCB0aGlzIGdyYXBoIGR5bmFtaWNhbGx5IGFzIG9wZXJhdGlvbnMgZXhlY3V0ZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiByZWx1KHopOlxuICAgIHJldHVybiBucC5tYXhpbXVtKDAsIHopXG5cbmRlZiBzb2Z0bWF4KHopOlxuICAgIHpfc2hpZnRlZCA9IHogLSB6Lm1heChheGlzPTEsIGtlZXBkaW1zPVRydWUpICAjIG51bWVyaWNhbCBzdGFiaWxpdHlcbiAgICBleHBfeiA9IG5wLmV4cCh6X3NoaWZ0ZWQpXG4gICAgcmV0dXJuIGV4cF96IC8gZXhwX3ouc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSlcblxuZGVmIG1scF9mb3J3YXJkKFgsIFcxLCBiMSwgVzIsIGIyKTpcbiAgICBcIlwiXCJUd28tbGF5ZXIgTUxQIGZvcndhcmQgcGFzczsgcmV0dXJucyBwcmVkaWN0aW9uIGFuZCBjYWNoZWQgaW50ZXJtZWRpYXRlcy5cIlwiXCJcbiAgICB6MSA9IFggQCBXMS5UICsgYjEgICAgICAgICAgIyAobSwgZF9oaWRkZW4pXG4gICAgYTEgPSByZWx1KHoxKSAgICAgICAgICAgICAgICMgKG0sIGRfaGlkZGVuKVxuICAgIHoyID0gYTEgQCBXMi5UICsgYjIgICAgICAgICAjIChtLCBkX291dClcbiAgICB5X2hhdCA9IHNvZnRtYXgoejIpICAgICAgICAgIyAobSwgZF9vdXQpXG4gICAgY2FjaGUgPSB7XHUwMDI3WFx1MDAyNzogWCwgXHUwMDI3ejFcdTAwMjc6IHoxLCBcdTAwMjdhMVx1MDAyNzogYTEsIFx1MDAyN3oyXHUwMDI3OiB6Mn1cbiAgICByZXR1cm4geV9oYXQsIGNhY2hlXG5cbm5wLnJhbmRvbS5zZWVkKDQyKVxubSwgZF9pbiwgZF9oLCBkX291dCA9IDgsIDE2LCAzMiwgNFxuWCAgPSBucC5yYW5kb20ucmFuZG4obSwgZF9pbilcblcxID0gbnAucmFuZG9tLnJhbmRuKGRfaCwgZF9pbikgKiBucC5zcXJ0KDIuMCAvIGRfaW4pICAjIEhlIGluaXRcbmIxID0gbnAuemVyb3MoZF9oKVxuVzIgPSBucC5yYW5kb20ucmFuZG4oZF9vdXQsIGRfaCkgKiBucC5zcXJ0KDIuMCAvIGRfaClcbmIyID0gbnAuemVyb3MoZF9vdXQpXG5cbnlfaGF0LCBjYWNoZSA9IG1scF9mb3J3YXJkKFgsIFcxLCBiMSwgVzIsIGIyKVxucHJpbnQoXHUwMDI3SW5wdXQgIHNoYXBlOlx1MDAyNywgWC5zaGFwZSlcbnByaW50KFx1MDAyN3oxICAgICBzaGFwZTpcdTAwMjcsIGNhY2hlW1x1MDAyN3oxXHUwMDI3XS5zaGFwZSlcbnByaW50KFx1MDAyN2ExICAgICBzaGFwZTpcdTAwMjcsIGNhY2hlW1x1MDAyN2ExXHUwMDI3XS5zaGFwZSlcbnByaW50KFx1MDAyN091dHB1dCBzaGFwZTpcdTAwMjcsIHlfaGF0LnNoYXBlKVxucHJpbnQoXHUwMDI3Um93IHN1bXMgKHNob3VsZCBiZSAxKTpcdTAwMjcsIHlfaGF0LnN1bShheGlzPTEpLnJvdW5kKDYpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlB5VG9yY2ggRm9yd2FyZCBQYXNzIHdpdGggU2hhcGUgVHJhY2luZyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBUd29MYXllck1MUChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX2luLCBkX2hpZGRlbiwgZF9vdXQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5mYzEgPSBubi5MaW5lYXIoZF9pbiwgZF9oaWRkZW4pXG4gICAgICAgIHNlbGYuYWN0ID0gbm4uUmVMVSgpXG4gICAgICAgIHNlbGYuZmMyID0gbm4uTGluZWFyKGRfaGlkZGVuLCBkX291dClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBwcmludChmXHUwMDI3ICBpbnB1dCAgOiB7dHVwbGUoeC5zaGFwZSl9XHUwMDI3KVxuICAgICAgICB6MSA9IHNlbGYuZmMxKHgpXG4gICAgICAgIHByaW50KGZcdTAwMjcgIGFmdGVyIGZjMSA6IHt0dXBsZSh6MS5zaGFwZSl9XHUwMDI3KVxuICAgICAgICBhMSA9IHNlbGYuYWN0KHoxKVxuICAgICAgICBwcmludChmXHUwMDI3ICBhZnRlciBSZUxVOiB7dHVwbGUoYTEuc2hhcGUpfVx1MDAyNylcbiAgICAgICAgejIgPSBzZWxmLmZjMihhMSlcbiAgICAgICAgcHJpbnQoZlx1MDAyNyAgb3V0cHV0ICAgIDoge3R1cGxlKHoyLnNoYXBlKX1cdTAwMjcpXG4gICAgICAgIHJldHVybiB6MlxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubSwgZF9pbiwgZF9oLCBkX291dCA9IDgsIDE2LCAzMiwgNFxubW9kZWwgPSBUd29MYXllck1MUChkX2luLCBkX2gsIGRfb3V0KVxuWCA9IHRvcmNoLnJhbmRuKG0sIGRfaW4pXG5wcmludChcdTAwMjdGb3J3YXJkIHBhc3Mgc2hhcGUgdHJhY2U6XHUwMDI3KVxubG9naXRzID0gbW9kZWwoWClcbnByaW50KFx1MDAyN1xcblBhcmFtZXRlciBjb3VudDpcdTAwMjcpXG5mb3IgbmFtZSwgcCBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCk6XG4gICAgcHJpbnQoZlx1MDAyNyAge25hbWV9OiB7dHVwbGUocC5zaGFwZSl9ICBudW1lbD17cC5udW1lbCgpfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb3NzIEZ1bmN0aW9uczogQ3Jvc3MtRW50cm9weSBhbmQgTVNFIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgbG9zcyBxdWFudGlmaWVzIGhvdyB3cm9uZyB0aGUgcHJlZGljdGlvbiBpcy4gRm9yIGNsYXNzaWZpY2F0aW9uLCBjYXRlZ29yaWNhbCBjcm9zcy1lbnRyb3B5IGlzIEwgPSAtKDEvbSkgzqPhtaIgzqPigpYgeeG1ouKCliBsb2coxbfhtaLigpYpIHdoZXJlIHkgaXMgb25lLWhvdC4gV2hlbiB0aGUgdGFyZ2V0IGlzIGEgY2xhc3MgaW5kZXggKG5vdCBvbmUtaG90KSwgdGhpcyBzaW1wbGlmaWVzIHRvIEwgPSAtKDEvbSkgzqPhtaIgbG9nKMW34bWiLGPhtaIpIOKAlCBvbmx5IHRoZSBsb2ctcHJvYmFiaWxpdHkgb2YgdGhlIGNvcnJlY3QgY2xhc3MgbWF0dGVycy4gRm9yIHJlZ3Jlc3Npb24sIE1TRSBpcyBMID0gKDEvbSkgzqPhtaIgKHnhtaIgLSDFt+G1oinCsi4gVGhlIHJhdyBsb2dpdHMgeiBjYW4gYmUgcGFzc2VkIGRpcmVjdGx5IHRvIGEgbnVtZXJpY2FsbHkgc3RhYmxlIGNyb3NzLWVudHJvcHkgaW1wbGVtZW50YXRpb24gaW5zdGVhZCBvZiBmaXJzdCBjb21wdXRpbmcgc29mdG1heCB0aGVuIGxvZy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IG51bXB5IGFzIG5wXG5pbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG4jIC0tLSBTY3JhdGNoIGltcGxlbWVudGF0aW9uIC0tLVxuZGVmIGNyb3NzX2VudHJvcHlfc2NyYXRjaChsb2dpdHMsIHlfdHJ1ZSk6XG4gICAgXCJcIlwibG9naXRzOiAobSwgQykgcmF3IHNjb3JlczsgeV90cnVlOiAobSwpIGludGVnZXIgY2xhc3MgaW5kaWNlcy5cIlwiXCJcbiAgICBtID0gbG9naXRzLnNoYXBlWzBdXG4gICAgIyBOdW1lcmljYWxseSBzdGFibGU6IHN1YnRyYWN0IG1heCBiZWZvcmUgZXhwXG4gICAgc2hpZnRlZCA9IGxvZ2l0cyAtIGxvZ2l0cy5tYXgoYXhpcz0xLCBrZWVwZGltcz1UcnVlKVxuICAgIGxvZ19wcm9icyA9IHNoaWZ0ZWQgLSBucC5sb2cobnAuZXhwKHNoaWZ0ZWQpLnN1bShheGlzPTEsIGtlZXBkaW1zPVRydWUpKVxuICAgIHJldHVybiAtbG9nX3Byb2JzW25wLmFyYW5nZShtKSwgeV90cnVlXS5tZWFuKClcblxubnAucmFuZG9tLnNlZWQoMClcbm0sIEMgPSAxNiwgNVxubG9naXRzX25wID0gbnAucmFuZG9tLnJhbmRuKG0sIEMpXG55X3RydWVfbnAgPSBucC5yYW5kb20ucmFuZGludCgwLCBDLCBtKVxuXG5sb3NzX3NjcmF0Y2ggPSBjcm9zc19lbnRyb3B5X3NjcmF0Y2gobG9naXRzX25wLCB5X3RydWVfbnApXG5cbiMgLS0tIFB5VG9yY2ggYnVpbHQtaW4gKGNvbWJpbmVzIExvZ1NvZnRtYXggKyBOTExMb3NzKSAtLS1cbmxvZ2l0c190ID0gdG9yY2gudGVuc29yKGxvZ2l0c19ucCwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnlfdHJ1ZV90ID0gdG9yY2gudGVuc29yKHlfdHJ1ZV9ucCwgZHR5cGU9dG9yY2gubG9uZylcbmxvc3NfdG9yY2ggPSBubi5Dcm9zc0VudHJvcHlMb3NzKCkobG9naXRzX3QsIHlfdHJ1ZV90KS5pdGVtKClcblxucHJpbnQoZlx1MDAyN1NjcmF0Y2ggQ0UgbG9zczoge2xvc3Nfc2NyYXRjaDouNmZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN1B5VG9yY2ggQ0UgbG9zczoge2xvc3NfdG9yY2g6LjZmfVx1MDAyNylcbnByaW50KGZcdTAwMjdEaWZmZXJlbmNlICAgICA6IHthYnMobG9zc19zY3JhdGNoIC0gbG9zc190b3JjaCk6LjJlfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6Ik51bWVyaWNhbCBTdGFiaWxpdHkgaW4gQ3Jvc3MtRW50cm9weSIsImNvbnRlbnQiOiJOZXZlciBjb21wdXRlIHNvZnRtYXggZmlyc3QgYW5kIHRoZW4gdGFrZSBsb2c6IGxvZyhzb2Z0bWF4KHopKSBzdWZmZXJzIGZyb20gdW5kZXJmbG93IHdoZW4geiBjb250YWlucyBsYXJnZSBuZWdhdGl2ZSB2YWx1ZXMuIEFsd2F5cyB1c2UgdGhlIGxvZy1zdW0tZXhwIHRyaWNrOiBsb2cgzqMgZXhwKHrigpYpID0gbWF4KHopICsgbG9nIM6jIGV4cCh64oKWIC0gbWF4KHopKS4gUHlUb3JjaFx1MDAyN3Mgbm4uQ3Jvc3NFbnRyb3B5TG9zcyBhcHBsaWVzIHRoaXMgYXV0b21hdGljYWxseSDigJQgcGFzcyByYXcgbG9naXRzLCBub3Qgc29mdG1heCBwcm9iYWJpbGl0aWVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZvcndhcmQgUGFzcyBQcm9maWxpbmcifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0aW1lXG5cbmNsYXNzIFByb2ZpbGVkTUxQKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGRpbXMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgbGF5ZXJzID0gW11cbiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKGRpbXMpIC0gMSk6XG4gICAgICAgICAgICBsYXllcnMuYXBwZW5kKG5uLkxpbmVhcihkaW1zW2ldLCBkaW1zW2krMV0pKVxuICAgICAgICAgICAgaWYgaSBcdTAwM2MgbGVuKGRpbXMpIC0gMjpcbiAgICAgICAgICAgICAgICBsYXllcnMuYXBwZW5kKG5uLlJlTFUoKSlcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKCpsYXllcnMpXG4gICAgICAgIHNlbGYudGltaW5ncyA9IHt9XG4gICAgICAgIHNlbGYuaG9va19oYW5kbGVzID0gW11cblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeClcblxuZGVmIHByb2ZpbGVfbGF5ZXJzKG1vZGVsLCB4LCBuX3J1bnM9NTApOlxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciBuYW1lLCBtb2R1bGUgaW4gbW9kZWwubmFtZWRfbW9kdWxlcygpOlxuICAgICAgICBpZiBpc2luc3RhbmNlKG1vZHVsZSwgKG5uLkxpbmVhciwgbm4uUmVMVSkpOlxuICAgICAgICAgICAgdGltZXMgPSBbXVxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9ydW5zKTpcbiAgICAgICAgICAgICAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgICAgICAgICAgeCA9IG1vZHVsZSh4KVxuICAgICAgICAgICAgICAgIHRpbWVzLmFwcGVuZCgodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAqIDFlNilcbiAgICAgICAgICAgIHJlc3VsdHMuYXBwZW5kKChuYW1lIG9yIHR5cGUobW9kdWxlKS5fX25hbWVfXywgeC5zaGFwZSwgZmxvYXQobnAubWVhbih0aW1lcykpKSlcbiAgICAgICAgICAgIGJyZWFrICAjIGRlbW86IHByb2ZpbGUgZmlyc3QgbGF5ZXIgb25seVxuICAgIHJldHVybiByZXN1bHRzXG5cbmltcG9ydCBudW1weSBhcyBucFxudG9yY2gubWFudWFsX3NlZWQoMClcbm0gPSA1MTJcbm1vZGVsID0gUHJvZmlsZWRNTFAoWzc4NCwgNTEyLCAyNTYsIDEyOCwgMTBdKVxueCA9IHRvcmNoLnJhbmRuKG0sIDc4NClcblxudF90b3RhbCA9IHRpbWUucGVyZl9jb3VudGVyKClcbmZvciBfIGluIHJhbmdlKDEwMCk6XG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIG91dCA9IG1vZGVsKHgpXG5lbGFwc2VkID0gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0X3RvdGFsKSAqIDEwICAjIG1zIHBlciBmb3J3YXJkXG5wcmludChmXHUwMDI3QmF0Y2ggc2l6ZSB7bX0sIDEwMCBydW5zOiB7ZWxhcHNlZDouMmZ9IG1zL2ZvcndhcmRcdTAwMjcpXG5wcmludChmXHUwMDI3T3V0cHV0IHNoYXBlOiB7dHVwbGUob3V0LnNoYXBlKX1cdTAwMjcpXG5mb3IgbmFtZSwgcCBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCk6XG4gICAgbWIgPSBwLm51bWVsKCkgKiA0IC8gMTAyNCoqMlxuICAgIHByaW50KGZcdTAwMjcgIHtuYW1lfToge3R1cGxlKHAuc2hhcGUpfSDigJQge21iOi40Zn0gTUJcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29tbW9uIExvc3MgRnVuY3Rpb25zIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkxvc3MiLCJUYXNrIiwiT3V0cHV0IFJhbmdlIiwiR3JhZGllbnQiLCJXaGVuIHRvIFVzZSJdLCJyb3dzIjpbWyJNU0UiLCJSZWdyZXNzaW9uIiwiKC3iiJ4sICviiJ4pIiwiMijFty15KS9tIOKAlCBsaW5lYXIsIGxhcmdlIGZvciBiaWcgZXJyb3JzIiwiQ2xlYW4gdGFyZ2V0cywgR2F1c3NpYW4gbm9pc2UgYXNzdW1wdGlvbiJdLFsiQ3Jvc3MtRW50cm9weSIsIk11bHRpLWNsYXNzIGNsYXNzaWZpY2F0aW9uIiwiKDAsICviiJ4pIiwixbcteSAoc29mdG1heCtDRSBjb21iaW5lZCkg4oCUIGNsZWFuIGFuZCBib3VuZGVkIiwiRGVmYXVsdCBmb3IgY2xhc3NpZmljYXRpb24gd2l0aCBjbGFzcyBpbmRpY2VzIl0sWyJCaW5hcnkgQ0UiLCJCaW5hcnkgLyBtdWx0aS1sYWJlbCIsIigwLCAr4oieKSIsIsW3LXkgcGVyIGxvZ2l0IOKAlCBzZXBhcmFibGUiLCJFYWNoIG91dHB1dCBpcyBpbmRlcGVuZGVudCBiaW5hcnkgZGVjaXNpb24iXSxbIkZvY2FsIExvc3MiLCJJbWJhbGFuY2VkIGNsYXNzaWZpY2F0aW9uIiwiKDAsICviiJ4pIiwiRG93bi13ZWlnaHRzIGVhc3kgZXhhbXBsZXMgdmlhICgxLXApXs6zIGZhY3RvciIsIk9iamVjdCBkZXRlY3Rpb24sIGV4dHJlbWUgY2xhc3MgaW1iYWxhbmNlIl0sWyJDb250cmFzdGl2ZS9UcmlwbGV0IiwiTWV0cmljIGxlYXJuaW5nIiwiKDAsICviiJ4pIiwiUHVzaGVzIHNhbWUtY2xhc3MgZW1iZWRkaW5ncyB0b2dldGhlciwgZGlmZmVyZW50IGFwYXJ0IiwiRmFjZSByZWNvZ25pdGlvbiwgZmV3LXNob3QgbGVhcm5pbmcsIHJldHJpZXZhbCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IE5vbi1MaW5lYXIgQWN0aXZhdGlvbnMgQXJlIEVzc2VudGlhbCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBuZXR3b3JrIHdpdGggTCBsaW5lYXIgbGF5ZXJzIGFuZCBubyBhY3RpdmF0aW9ucyBpcyBlcXVpdmFsZW50IHRvIGEgc2luZ2xlIGxpbmVhciBsYXllcjogdGhlIGNvbXBvc2l0aW9uIG9mIGxpbmVhciBtYXBzIGlzIGxpbmVhci4gTm8gbWF0dGVyIGhvdyBtYW55IGxheWVycyBhcmUgc3RhY2tlZCwgdGhlIGh5cG90aGVzaXMgY2xhc3MgcmVtYWlucyB7eCDihqYgQXggKyBiIHwgQSDiiIgg4oSdXntkX291dCDDlyBkX2lufX0uIEFkZGluZyBhIHNpbmdsZSBub24tbGluZWFyIGFjdGl2YXRpb24gYWxyZWFkeSBtYWtlcyB0aGUgbmV0d29yayBhIHVuaXZlcnNhbCBmdW5jdGlvbiBhcHByb3hpbWF0b3IgKGJ5IHRoZSB1bml2ZXJzYWwgYXBwcm94aW1hdGlvbiB0aGVvcmVtKTogZ2l2ZW4gc3VmZmljaWVudCBoaWRkZW4gdW5pdHMsIGEgb25lLWhpZGRlbi1sYXllciBuZXR3b3JrIHdpdGggc2lnbW9pZCBhY3RpdmF0aW9ucyBjYW4gYXBwcm94aW1hdGUgYW55IGNvbnRpbnVvdXMgZnVuY3Rpb24gb24gYSBjb21wYWN0IGRvbWFpbiB0byBhcmJpdHJhcnkgcHJlY2lzaW9uLiBJbiBwcmFjdGljZSwgZGVwdGggaXMgbW9yZSBwYXJhbWV0ZXItZWZmaWNpZW50IHRoYW4gd2lkdGggZm9yIGxlYXJuaW5nIGhpZXJhcmNoaWNhbCByZXByZXNlbnRhdGlvbnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJMaW5lYXJpdHkgY29sbGFwc2U6IFfigoIoV+KCgXgrYuKCgSkrYuKCgiA9IFfigoN4K2LigoMg4oCUIGRlcHRoIGFkZHMgbm90aGluZyB3aXRob3V0IGFjdGl2YXRpb24uIiwiVW5pdmVyc2FsIGFwcHJveGltYXRpb246IG9uZSBoaWRkZW4gbGF5ZXIgKyBzaWdtb2lkIGlzIGEgdW5pdmVyc2FsIGFwcHJveGltYXRvciAod2lkdGgg4oaRIGFzIM61IOKGkykuIiwiRGVwdGggZWZmaWNpZW5jeTogZGVlcCBuZXR3b3JrcyByZXByZXNlbnQgZXhwb25lbnRpYWxseSBtb3JlIGZ1bmN0aW9ucyB0aGFuIHNoYWxsb3cgb25lcyBvZiBlcXVhbCB3aWR0aC4iLCJTcGFyc2UgYWN0aXZhdGlvbnM6IFJlTFUgb3V0cHV0cyBleGFjdGx5IHplcm8gZm9yIGhhbGYgb2YgaW5wdXRzIG9uIGF2ZXJhZ2Ug4oCUIGNvbXB1dGF0aW9uYWxseSBlZmZpY2llbnQuIiwiR3JhZGllbnQgZmxvdzogYWN0aXZhdGlvbiBjaG9pY2UgZGV0ZXJtaW5lcyB3aGV0aGVyIGdyYWRpZW50cyB2YW5pc2ggKHNpZ21vaWQgZGVlcCkgb3IgZmxvdyBmcmVlbHkgKFJlTFUpLiJdfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# Forward Pass — Linear Layers, Activations, and Loss

The forward pass is the computation that transforms raw input into a prediction. Every layer applies a linear transformation followed by a non-linear activation; stacking these layers allows the network to approximate arbitrarily complex functions. Understanding the mechanics — shape tracking, vectorised batch computation, and the cached intermediate values — is prerequisite for implementing backpropagation correctly.

## Linear Layer: z = Wx + b

A single linear (fully-connected) layer computes z = Wx + b where W ∈ ℝ^{d_out × d_in}, x ∈ ℝ^{d_in}, b ∈ ℝ^{d_out}. For a mini-batch of m samples, inputs are stacked row-wise: X ∈ ℝ^{m × d_in}. The batched form is Z = XWᵀ + b where the bias b broadcasts across the batch dimension, giving Z ∈ ℝ^{m × d_out}. Shape tracking is critical — a dimension mismatch silently corrupts computations rather than raising an error in some frameworks.

## Activation Functions and Non-linearity

Without non-linear activations, stacking linear layers collapses to a single linear map: W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂). The network cannot represent XOR, let alone vision or language tasks. An activation a = σ(z) applied element-wise breaks linearity. Common choices: ReLU a = max(0, z), sigmoid a = 1/(1+e⁻ᶻ), GELU, and SiLU. The activation is applied after every linear layer except — typically — the final output layer.

## Composition and the Computational Graph

A two-layer MLP forward pass: z₁ = XW₁ᵀ + b₁, a₁ = ReLU(z₁), z₂ = a₁W₂ᵀ + b₂, ŷ = softmax(z₂). Each intermediate value is a node in the computational graph. During the forward pass these values are cached (z₁, a₁, z₂) because the backward pass needs them to compute gradients. Autograd engines like PyTorch build this graph dynamically as operations execute.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

def softmax(z):
    z_shifted = z - z.max(axis=1, keepdims=True)  # numerical stability
    exp_z = np.exp(z_shifted)
    return exp_z / exp_z.sum(axis=1, keepdims=True)

def mlp_forward(X, W1, b1, W2, b2):
    """Two-layer MLP forward pass; returns prediction and cached intermediates."""
    z1 = X @ W1.T + b1          # (m, d_hidden)
    a1 = relu(z1)               # (m, d_hidden)
    z2 = a1 @ W2.T + b2         # (m, d_out)
    y_hat = softmax(z2)         # (m, d_out)
    cache = {'X': X, 'z1': z1, 'a1': a1, 'z2': z2}
    return y_hat, cache

np.random.seed(42)
m, d_in, d_h, d_out = 8, 16, 32, 4
X  = np.random.randn(m, d_in)
W1 = np.random.randn(d_h, d_in) * np.sqrt(2.0 / d_in)  # He init
b1 = np.zeros(d_h)
W2 = np.random.randn(d_out, d_h) * np.sqrt(2.0 / d_h)
b2 = np.zeros(d_out)

y_hat, cache = mlp_forward(X, W1, b1, W2, b2)
print('Input  shape:', X.shape)
print('z1     shape:', cache['z1'].shape)
print('a1     shape:', cache['a1'].shape)
print('Output shape:', y_hat.shape)
print('Row sums (should be 1):', y_hat.sum(axis=1).round(6))
```

## PyTorch Forward Pass with Shape Tracing

```python
import torch
import torch.nn as nn

class TwoLayerMLP(nn.Module):
    def __init__(self, d_in, d_hidden, d_out):
        super().__init__()
        self.fc1 = nn.Linear(d_in, d_hidden)
        self.act = nn.ReLU()
        self.fc2 = nn.Linear(d_hidden, d_out)

    def forward(self, x):
        print(f'  input  : {tuple(x.shape)}')
        z1 = self.fc1(x)
        print(f'  after fc1 : {tuple(z1.shape)}')
        a1 = self.act(z1)
        print(f'  after ReLU: {tuple(a1.shape)}')
        z2 = self.fc2(a1)
        print(f'  output    : {tuple(z2.shape)}')
        return z2

torch.manual_seed(0)
m, d_in, d_h, d_out = 8, 16, 32, 4
model = TwoLayerMLP(d_in, d_h, d_out)
X = torch.randn(m, d_in)
print('Forward pass shape trace:')
logits = model(X)
print('\nParameter count:')
for name, p in model.named_parameters():
    print(f'  {name}: {tuple(p.shape)}  numel={p.numel()}')
```

## Loss Functions: Cross-Entropy and MSE

The loss quantifies how wrong the prediction is. For classification, categorical cross-entropy is L = -(1/m) Σᵢ Σₖ yᵢₖ log(ŷᵢₖ) where y is one-hot. When the target is a class index (not one-hot), this simplifies to L = -(1/m) Σᵢ log(ŷᵢ,cᵢ) — only the log-probability of the correct class matters. For regression, MSE is L = (1/m) Σᵢ (yᵢ - ŷᵢ)². The raw logits z can be passed directly to a numerically stable cross-entropy implementation instead of first computing softmax then log.

```python
import numpy as np
import torch
import torch.nn as nn

# --- Scratch implementation ---
def cross_entropy_scratch(logits, y_true):
    """logits: (m, C) raw scores; y_true: (m,) integer class indices."""
    m = logits.shape[0]
    # Numerically stable: subtract max before exp
    shifted = logits - logits.max(axis=1, keepdims=True)
    log_probs = shifted - np.log(np.exp(shifted).sum(axis=1, keepdims=True))
    return -log_probs[np.arange(m), y_true].mean()

np.random.seed(0)
m, C = 16, 5
logits_np = np.random.randn(m, C)
y_true_np = np.random.randint(0, C, m)

loss_scratch = cross_entropy_scratch(logits_np, y_true_np)

# --- PyTorch built-in (combines LogSoftmax + NLLLoss) ---
logits_t = torch.tensor(logits_np, dtype=torch.float32)
y_true_t = torch.tensor(y_true_np, dtype=torch.long)
loss_torch = nn.CrossEntropyLoss()(logits_t, y_true_t).item()

print(f'Scratch CE loss: {loss_scratch:.6f}')
print(f'PyTorch CE loss: {loss_torch:.6f}')
print(f'Difference     : {abs(loss_scratch - loss_torch):.2e}')
```

> **Numerical Stability in Cross-Entropy**: Never compute softmax first and then take log: log(softmax(z)) suffers from underflow when z contains large negative values. Always use the log-sum-exp trick: log Σ exp(zₖ) = max(z) + log Σ exp(zₖ - max(z)). PyTorch's nn.CrossEntropyLoss applies this automatically — pass raw logits, not softmax probabilities.

## Forward Pass Profiling

```python
import torch
import torch.nn as nn
import time

class ProfiledMLP(nn.Module):
    def __init__(self, dims):
        super().__init__()
        layers = []
        for i in range(len(dims) - 1):
            layers.append(nn.Linear(dims[i], dims[i+1]))
            if i < len(dims) - 2:
                layers.append(nn.ReLU())
        self.net = nn.Sequential(*layers)
        self.timings = {}
        self.hook_handles = []

    def forward(self, x):
        return self.net(x)

def profile_layers(model, x, n_runs=50):
    results = []
    for name, module in model.named_modules():
        if isinstance(module, (nn.Linear, nn.ReLU)):
            times = []
            for _ in range(n_runs):
                t0 = time.perf_counter()
                with torch.no_grad():
                    x = module(x)
                times.append((time.perf_counter() - t0) * 1e6)
            results.append((name or type(module).__name__, x.shape, float(np.mean(times))))
            break  # demo: profile first layer only
    return results

import numpy as np
torch.manual_seed(0)
m = 512
model = ProfiledMLP([784, 512, 256, 128, 10])
x = torch.randn(m, 784)

t_total = time.perf_counter()
for _ in range(100):
    with torch.no_grad():
        out = model(x)
elapsed = (time.perf_counter() - t_total) * 10  # ms per forward
print(f'Batch size {m}, 100 runs: {elapsed:.2f} ms/forward')
print(f'Output shape: {tuple(out.shape)}')
for name, p in model.named_parameters():
    mb = p.numel() * 4 / 1024**2
    print(f'  {name}: {tuple(p.shape)} — {mb:.4f} MB')
```

## Common Loss Functions

| Loss | Task | Output Range | Gradient | When to Use |
| --- | --- | --- | --- | --- |
| MSE | Regression | (-∞, +∞) | 2(ŷ-y)/m — linear, large for big errors | Clean targets, Gaussian noise assumption |
| Cross-Entropy | Multi-class classification | (0, +∞) | ŷ-y (softmax+CE combined) — clean and bounded | Default for classification with class indices |
| Binary CE | Binary / multi-label | (0, +∞) | ŷ-y per logit — separable | Each output is independent binary decision |
| Focal Loss | Imbalanced classification | (0, +∞) | Down-weights easy examples via (1-p)^γ factor | Object detection, extreme class imbalance |
| Contrastive/Triplet | Metric learning | (0, +∞) | Pushes same-class embeddings together, different apart | Face recognition, few-shot learning, retrieval |

## Why Non-Linear Activations Are Essential

A network with L linear layers and no activations is equivalent to a single linear layer: the composition of linear maps is linear. No matter how many layers are stacked, the hypothesis class remains {x ↦ Ax + b | A ∈ ℝ^{d_out × d_in}}. Adding a single non-linear activation already makes the network a universal function approximator (by the universal approximation theorem): given sufficient hidden units, a one-hidden-layer network with sigmoid activations can approximate any continuous function on a compact domain to arbitrary precision. In practice, depth is more parameter-efficient than width for learning hierarchical representations.

- Linearity collapse: W₂(W₁x+b₁)+b₂ = W₃x+b₃ — depth adds nothing without activation.
- Universal approximation: one hidden layer + sigmoid is a universal approximator (width ↑ as ε ↓).
- Depth efficiency: deep networks represent exponentially more functions than shallow ones of equal width.
- Sparse activations: ReLU outputs exactly zero for half of inputs on average — computationally efficient.
- Gradient flow: activation choice determines whether gradients vanish (sigmoid deep) or flow freely (ReLU).

---

