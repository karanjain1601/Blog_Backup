---
title: "NAS — Differentiable Architecture Search and Efficiency Proxies"
slug: "nas-neural-architecture-search"
description: "Neural architecture search from RL-based controllers to DARTS bi-level optimization. Covers the search space definition, differentiable relaxation, efficiency-aware objectives (FLOPs, latency), and one-shot supernet methods with weight sharing."
tags: ["deep-learning", "model-compression", "pruning", "quantization"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiTmV1cmFsIGFyY2hpdGVjdHVyZSBzZWFyY2ggKE5BUykgYXV0b21hdGVzIHRoZSBkZXNpZ24gb2YgbmV1cmFsIG5ldHdvcmsgYXJjaGl0ZWN0dXJlcyBieSBmb3JtdWxhdGluZyBhcmNoaXRlY3R1cmUgc2VsZWN0aW9uIGFzIGFuIG9wdGltaXphdGlvbiBwcm9ibGVtLiBFYXJseSBOQVMgbWV0aG9kcyB1c2VkIHJlaW5mb3JjZW1lbnQgbGVhcm5pbmcgdG8gdHJhaW4gYSBjb250cm9sbGVyIHRoYXQgcHJvcG9zZXMgYXJjaGl0ZWN0dXJlcywgZXZhbHVhdGVkIGVhY2ggb24gYSBwcm94eSB0YXNrLCBhbmQgdXBkYXRlZCB0aGUgY29udHJvbGxlciBiYXNlZCBvbiB0aGUgdmFsaWRhdGlvbiBhY2N1cmFjeS4gVGhpcyByZXF1aXJlZCB0aG91c2FuZHMgb2YgR1BVLWhvdXJzIGFuZCBodW5kcmVkcyBvZiBHUFUgbWFjaGluZXMuIE1vZGVybiBOQVMgbWV0aG9kcyDigJQgREFSVFMsIG9uZS1zaG90IHN1cGVybmV0cywgYW5kIGVmZmljaWVuY3ktYXdhcmUgc2VhcmNoIOKAlCBoYXZlIHJlZHVjZWQgdGhlIGNvc3QgdG8gYSBzaW5nbGUgR1BVLWRheSBvciBsZXNzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNlYXJjaCBTcGFjZSBEZWZpbml0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgc2VhcmNoIHNwYWNlIGRldGVybWluZXMgd2hpY2ggYXJjaGl0ZWN0dXJlcyBjYW4gYmUgZm91bmQuIEEgdHlwaWNhbCBjZWxsLWJhc2VkIHNlYXJjaCBzcGFjZSBkZWZpbmVzIGEgY29tcHV0YXRpb25hbCBjZWxsIChhIHNtYWxsIGdyYXBoIG9mIG9wZXJhdGlvbnMpIGFuZCBzdGFja3MgTiBjZWxscyB0byBmb3JtIHRoZSBmdWxsIG5ldHdvcmsuIEF0IGVhY2ggZWRnZSBpbiB0aGUgY2VsbCwgdGhlIG9wZXJhdGlvbiBpcyBjaG9zZW4gZnJvbSBhIGNhbmRpZGF0ZSBzZXQ6IDPDlzMgY29udiwgNcOXNSBjb252LCAzw5czIGRpbGF0ZWQgY29udiwgM8OXMyBtYXggcG9vbCwgc2tpcCBjb25uZWN0aW9uLCB6ZXJvLiBXaXRoIDcgY2FuZGlkYXRlIG9wcyBhbmQgMTQgZWRnZXMgaW4gYSBjZWxsLCB0aGUgc2VhcmNoIHNwYWNlIGhhcyA3XjE0IOKJiCAxMF4xMiBwb3NzaWJsZSBjZWxscy4gUkwtTkFTIHNhbXBsZXMgZGlyZWN0bHkgZnJvbSB0aGlzIHNwYWNlOyBEQVJUUyByZWxheGVzIGl0IHRvIGEgY29udGludW91cyBtaXh0dXJlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRBUlRTIOKAlCBEaWZmZXJlbnRpYWJsZSBNaXhlZCBPcGVyYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRBUlRTIChMaXUgZXQgYWwuIDIwMTkpIHJlbGF4ZXMgdGhlIGRpc2NyZXRlIG9wZXJhdGlvbiBzZWxlY3Rpb24gdG8gYSBjb250aW51b3VzIG1peHR1cmU6IGZvciBlYWNoIGVkZ2UsIHRoZSBvdXRwdXQgaXMgYSB3ZWlnaHRlZCBzdW0gb2YgYWxsIGNhbmRpZGF0ZSBvcGVyYXRpb25zOiDFjSh4KSA9IM6jX2kgZXhwKM6xX2kpIC8gzqNfaiBleHAozrFfaikgwrcgb19pKHgpLiBUaGUgYXJjaGl0ZWN0dXJlIHBhcmFtZXRlcnMgzrEgKG9uZSBwZXIgb3BlcmF0aW9uIHBlciBlZGdlKSBhcmUgbGVhcm5lZCBqb2ludGx5IHdpdGggdGhlIHdlaWdodCBwYXJhbWV0ZXJzIHcgYnkgZ3JhZGllbnQgZGVzY2VudC4gQWZ0ZXIgc2VhcmNoLCB0aGUgYXJjaGl0ZWN0dXJlIGlzIGRpc2NyZXRpemVkIGJ5IHNlbGVjdGluZyB0aGUgaGlnaGVzdC3OsSBvcGVyYXRpb24gb24gZWFjaCBlZGdlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBNaXhlZE9wKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiREFSVFMgbWl4ZWQgb3BlcmF0aW9uOiB3ZWlnaHRlZCBzb2Z0bWF4IG1peHR1cmUgb2YgY2FuZGlkYXRlIG9wcy5cIlwiXCJcblxuICAgIENBTkRJREFURVMgPSB7XG4gICAgICAgIFx1MDAyN3NraXBcdTAwMjc6IGxhbWJkYSBDOiBubi5JZGVudGl0eSgpLFxuICAgICAgICBcdTAwMjdjb252M3gzXHUwMDI3OiBsYW1iZGEgQzogbm4uU2VxdWVudGlhbChubi5Db252MmQoQywgQywgMywgcGFkZGluZz0xLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQoQykpLFxuICAgICAgICBcdTAwMjdjb252NXg1XHUwMDI3OiBsYW1iZGEgQzogbm4uU2VxdWVudGlhbChubi5Db252MmQoQywgQywgNSwgcGFkZGluZz0yLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQoQykpLFxuICAgICAgICBcdTAwMjdtYXhwb29sXHUwMDI3OiBsYW1iZGEgQzogbm4uTWF4UG9vbDJkKDMsIHN0cmlkZT0xLCBwYWRkaW5nPTEpLFxuICAgICAgICBcdTAwMjdhdmdwb29sXHUwMDI3OiBsYW1iZGEgQzogbm4uQXZnUG9vbDJkKDMsIHN0cmlkZT0xLCBwYWRkaW5nPTEpLFxuICAgIH1cblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBDOiBpbnQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5vcHMgPSBubi5Nb2R1bGVMaXN0KFtmbihDKSBmb3IgZm4gaW4gc2VsZi5DQU5ESURBVEVTLnZhbHVlcygpXSlcbiAgICAgICAgc2VsZi5vcF9uYW1lcyA9IGxpc3Qoc2VsZi5DQU5ESURBVEVTLmtleXMoKSlcbiAgICAgICAgIyBBcmNoaXRlY3R1cmUgd2VpZ2h0cyAozrEpIOKAlCBub3QgaW4gbW9kZWwucGFyYW1ldGVycygpLCB0cmFpbmVkIHNlcGFyYXRlbHlcbiAgICAgICAgc2VsZi5hcmNoX3dlaWdodHMgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3MobGVuKHNlbGYub3BzKSkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICB3ZWlnaHRzID0gRi5zb2Z0bWF4KHNlbGYuYXJjaF93ZWlnaHRzLCBkaW09MClcbiAgICAgICAgcmV0dXJuIHN1bSh3ICogb3AoeCkgZm9yIHcsIG9wIGluIHppcCh3ZWlnaHRzLCBzZWxmLm9wcykpXG5cbiAgICBkZWYgZGlzY3JldGl6ZShzZWxmKSAtXHUwMDNlIHN0cjpcbiAgICAgICAgXCJcIlwiUmV0dXJuIHRoZSBuYW1lIG9mIHRoZSBvcGVyYXRpb24gd2l0aCBoaWdoZXN0IGFyY2ggd2VpZ2h0LlwiXCJcIlxuICAgICAgICBiZXN0ID0gc2VsZi5hcmNoX3dlaWdodHMuYXJnbWF4KCkuaXRlbSgpXG4gICAgICAgIHJldHVybiBzZWxmLm9wX25hbWVzW2Jlc3RdXG5cbiMgRGVtb1xuQyA9IDE2XG5taXhlZCA9IE1peGVkT3AoQylcbnggPSB0b3JjaC5yYW5kbigyLCBDLCA4LCA4KVxub3V0ID0gbWl4ZWQoeClcbnByaW50KGZcdTAwMjdPdXRwdXQgc2hhcGU6IHtvdXQuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0FyY2ggd2VpZ2h0cyAoc29mdG1heCk6IHtGLnNvZnRtYXgobWl4ZWQuYXJjaF93ZWlnaHRzLCBkaW09MCkuZGV0YWNoKCkucm91bmQoZGVjaW1hbHM9MykudG9saXN0KCl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0Rpc2NyZXRpemVkIG9wZXJhdGlvbjoge21peGVkLmRpc2NyZXRpemUoKX1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiREFSVFMgQmktTGV2ZWwgT3B0aW1pemF0aW9uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gub3B0aW0gYXMgb3B0aW1cblxuZGVmIGRhcnRzX3RyYWluX3N0ZXAobW9kZWwsIGFyY2hfcGFyYW1zLCB0cmFpbl9iYXRjaCwgdmFsX2JhdGNoLCBjcml0ZXJpb24sXG4gICAgICAgICAgICAgICAgICAgICB3X29wdGltaXplciwgYXJjaF9vcHRpbWl6ZXIsIGlubmVyX3N0ZXBzPTEpOlxuICAgIFwiXCJcIlxuICAgIERBUlRTIGFsdGVybmF0aW5nIG9wdGltaXphdGlvbjpcbiAgICAxLiBVcGRhdGUgYXJjaGl0ZWN0dXJlIHBhcmFtcyBhbHBoYSBvbiB2YWxpZGF0aW9uIGxvc3MuXG4gICAgMi4gVXBkYXRlIHdlaWdodCBwYXJhbXMgdyBvbiB0cmFpbmluZyBsb3NzLlxuICAgIFwiXCJcIlxuICAgIFhfdHJhaW4sIHlfdHJhaW4gPSB0cmFpbl9iYXRjaFxuICAgIFhfdmFsLCB5X3ZhbCA9IHZhbF9iYXRjaFxuXG4gICAgIyBTdGVwIDE6IFVwZGF0ZSBhcmNoaXRlY3R1cmUgcGFyYW1ldGVycyBvbiB2YWxpZGF0aW9uIHNldFxuICAgIGFyY2hfb3B0aW1pemVyLnplcm9fZ3JhZCgpXG4gICAgdmFsX2xvc3MgPSBjcml0ZXJpb24obW9kZWwoWF92YWwpLCB5X3ZhbClcbiAgICB2YWxfbG9zcy5iYWNrd2FyZCgpXG4gICAgYXJjaF9vcHRpbWl6ZXIuc3RlcCgpXG5cbiAgICAjIFN0ZXAgMjogVXBkYXRlIHdlaWdodCBwYXJhbWV0ZXJzIG9uIHRyYWluaW5nIHNldFxuICAgIGZvciBfIGluIHJhbmdlKGlubmVyX3N0ZXBzKTpcbiAgICAgICAgd19vcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgdHJhaW5fbG9zcyA9IGNyaXRlcmlvbihtb2RlbChYX3RyYWluKSwgeV90cmFpbilcbiAgICAgICAgdHJhaW5fbG9zcy5iYWNrd2FyZCgpXG4gICAgICAgIHdfb3B0aW1pemVyLnN0ZXAoKVxuXG4gICAgcmV0dXJuIHRyYWluX2xvc3MuaXRlbSgpLCB2YWxfbG9zcy5pdGVtKClcblxuIyBTZXBhcmF0ZSB3ZWlnaHQgYW5kIGFyY2ggcGFyYW1ldGVycyBmb3IgZHVhbCBvcHRpbWl6ZXJzXG4jIChhcmNoX3BhcmFtcyBoYXZlIHJlcXVpcmVzX2dyYWQ9VHJ1ZSBhbmQgYXJlIHBhc3NlZCB0byBhcmNoX29wdGltaXplcilcbnByaW50KFx1MDAyN0RBUlRTIGJpLWxldmVsOiBhcmNoIG9wdGltaXplciAtXHUwMDNlIHZhbCBsb3NzOyB3ZWlnaHQgb3B0aW1pemVyIC1cdTAwM2UgdHJhaW4gbG9zc1x1MDAyNylcbnByaW50KFx1MDAyN0FmdGVyIHNlYXJjaDogZGlzY3JldGl6ZSBieSBhcmdtYXgoYXJjaF93ZWlnaHRzKSBwZXIgZWRnZS5cdTAwMjcpXG5wcmludChcdTAwMjdSZS10cmFpbiBkaXNjcmV0aXplZCBhcmNoaXRlY3R1cmUgZnJvbSBzY3JhdGNoIGZvciBmYWlyIGNvbXBhcmlzb24uXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmljaWVuY3ktQXdhcmUgTkFTIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBY2N1cmFjeSBhbG9uZSBpcyBpbnN1ZmZpY2llbnQgZm9yIG1vYmlsZSBhbmQgZWRnZSBkZXBsb3ltZW50LiBFZmZpY2llbmN5LWF3YXJlIE5BUyBhZGRzIGEgaGFyZHdhcmUgY29zdCB0ZXJtIHRvIHRoZSBvYmplY3RpdmU6IExfdG90YWwgPSBMX0NFKHksIMW3KSArIM67IMK3IGxvZyhsYXRlbmN5KM6xKSkuIFRoZSBsYXRlbmN5IGlzIGVzdGltYXRlZCBmcm9tIGEgbG9va3VwIHRhYmxlIChvcCDDlyByZXNvbHV0aW9uIMOXIGhhcmR3YXJlKSByYXRoZXIgdGhhbiBtZWFzdXJlZCBhdCBldmVyeSBzdGVwLiBGQk5ldCBhbmQgUHJveHlsZXNzTkFTIHVzZSB0aGlzIGFwcHJvYWNoLiBUaGUgzrsgaHlwZXJwYXJhbWV0ZXIgY29udHJvbHMgdGhlIGFjY3VyYWN5LWxhdGVuY3kgdHJhZGUtb2ZmOyBzd2VlcGluZyDOuyBwcm9kdWNlcyBhIFBhcmV0byBmcm9udGllciBvZiBhcmNoaXRlY3R1cmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG4jIExhdGVuY3kgbG9va3VwIHRhYmxlOiBvcCAtXHUwMDNlIChtcyBvbiBtb2JpbGUgQ1BVLCBtcyBvbiBzZXJ2ZXIgR1BVKVxuTEFURU5DWV9UQUJMRSA9IHtcbiAgICBcdTAwMjdza2lwXHUwMDI3OiAgICAoMC4wNSwgMC4wMSksXG4gICAgXHUwMDI3Y29udjN4M1x1MDAyNzogKDEuMjAsIDAuMTUpLFxuICAgIFx1MDAyN2NvbnY1eDVcdTAwMjc6ICgyLjgwLCAwLjMwKSxcbiAgICBcdTAwMjdtYXhwb29sXHUwMDI3OiAoMC4zMCwgMC4wNCksXG4gICAgXHUwMDI3YXZncG9vbFx1MDAyNzogKDAuMjUsIDAuMDQpLFxufVxuXG5kZWYgZGlmZmVyZW50aWFibGVfbGF0ZW5jeShhcmNoX3dlaWdodHM6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG9wX25hbWVzOiBsaXN0LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdGFyZ2V0OiBzdHIgPSBcdTAwMjdtb2JpbGVcdTAwMjcpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgIFwiXCJcIlxuICAgIEV4cGVjdGVkIGxhdGVuY3kgYXMgYSBkaWZmZXJlbnRpYWJsZSBmdW5jdGlvbiBvZiBhcmNoIHdlaWdodHMuXG4gICAgdGFyZ2V0OiBcdTAwMjdtb2JpbGVcdTAwMjcgKGluZGV4IDApIG9yIFx1MDAyN3NlcnZlclx1MDAyNyAoaW5kZXggMSlcbiAgICBcIlwiXCJcbiAgICBpZHggPSAwIGlmIHRhcmdldCA9PSBcdTAwMjdtb2JpbGVcdTAwMjcgZWxzZSAxXG4gICAgbGF0X3RlbnNvciA9IHRvcmNoLnRlbnNvcihcbiAgICAgICAgW0xBVEVOQ1lfVEFCTEVbbmFtZV1baWR4XSBmb3IgbmFtZSBpbiBvcF9uYW1lc10sXG4gICAgICAgIGR0eXBlPXRvcmNoLmZsb2F0MzJcbiAgICApXG4gICAgcHJvYnMgPSB0b3JjaC5zb2Z0bWF4KGFyY2hfd2VpZ2h0cywgZGltPTApXG4gICAgcmV0dXJuIChwcm9icyAqIGxhdF90ZW5zb3IpLnN1bSgpICAjIGV4cGVjdGVkIGxhdGVuY3lcblxuZGVmIGVmZmljaWVuY3lfYXdhcmVfbG9zcyh0YXNrX2xvc3MsIGFyY2hfd2VpZ2h0cywgb3BfbmFtZXMsIGxhbT0wLjEsIHRhcmdldD1cdTAwMjdtb2JpbGVcdTAwMjcpOlxuICAgIGxhdCA9IGRpZmZlcmVudGlhYmxlX2xhdGVuY3koYXJjaF93ZWlnaHRzLCBvcF9uYW1lcywgdGFyZ2V0KVxuICAgIHJldHVybiB0YXNrX2xvc3MgKyBsYW0gKiB0b3JjaC5sb2cobGF0ICsgMWUtNilcblxuIyBEZW1vXG5hcmNoX3cgPSB0b3JjaC5yYW5kbig1LCByZXF1aXJlc19ncmFkPVRydWUpXG5vcF9uYW1lcyA9IGxpc3QoTEFURU5DWV9UQUJMRS5rZXlzKCkpXG50YXNrX2xvc3MgPSB0b3JjaC50ZW5zb3IoMS41KVxudG90YWxfbG9zcyA9IGVmZmljaWVuY3lfYXdhcmVfbG9zcyh0YXNrX2xvc3MsIGFyY2hfdywgb3BfbmFtZXMsIGxhbT0wLjEpXG50b3RhbF9sb3NzLmJhY2t3YXJkKClcbnByaW50KGZcdTAwMjdUb3RhbCBsb3NzOiB7dG90YWxfbG9zcy5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdhcmNoX3cgZ3JhZDoge2FyY2hfdy5ncmFkLnJvdW5kKGRlY2ltYWxzPTQpLnRvbGlzdCgpfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPbmUtU2hvdCBTdXBlcm5ldCB3aXRoIFdlaWdodCBTaGFyaW5nIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgcmFuZG9tXG5cbmNsYXNzIFN1cGVybmV0KG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiT25lLXNob3Qgc3VwZXJuZXQ6IGFsbCBzdWJuZXRzIHNoYXJlIHRoZSBzYW1lIHdlaWdodHMuXCJcIlwiXG5cbiAgICBPUFMgPSBbXHUwMDI3c2tpcFx1MDAyNywgXHUwMDI3Y29udjNcdTAwMjcsIFx1MDAyN2NvbnY1XHUwMDI3LCBcdTAwMjdwb29sXHUwMDI3XVxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5fbGF5ZXJzOiBpbnQgPSA0LCBDOiBpbnQgPSAzMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5fbGF5ZXJzID0gbl9sYXllcnNcbiAgICAgICAgc2VsZi5sYXllcnMgPSBubi5Nb2R1bGVMaXN0KFtcbiAgICAgICAgICAgIG5uLk1vZHVsZURpY3Qoe1xuICAgICAgICAgICAgICAgIFx1MDAyN3NraXBcdTAwMjc6ICBubi5JZGVudGl0eSgpLFxuICAgICAgICAgICAgICAgIFx1MDAyN2NvbnYzXHUwMDI3OiBubi5TZXF1ZW50aWFsKG5uLkNvbnYyZChDLCBDLCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKCkpLFxuICAgICAgICAgICAgICAgIFx1MDAyN2NvbnY1XHUwMDI3OiBubi5TZXF1ZW50aWFsKG5uLkNvbnYyZChDLCBDLCA1LCBwYWRkaW5nPTIpLCBubi5SZUxVKCkpLFxuICAgICAgICAgICAgICAgIFx1MDAyN3Bvb2xcdTAwMjc6ICBubi5BdmdQb29sMmQoMywgc3RyaWRlPTEsIHBhZGRpbmc9MSksXG4gICAgICAgICAgICB9KVxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9sYXllcnMpXG4gICAgICAgIF0pXG4gICAgICAgIHNlbGYuY2xhc3NpZmllciA9IG5uLkFkYXB0aXZlQXZnUG9vbDJkKDEpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IsIHN1Ym5ldDogbGlzdCA9IE5vbmUpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICBcIlwiXCJzdWJuZXQ6IGxpc3Qgb2Ygb3AgbmFtZXMgcGVyIGxheWVyLiBJZiBOb25lLCBzYW1wbGUgcmFuZG9tbHkuXCJcIlwiXG4gICAgICAgIGlmIHN1Ym5ldCBpcyBOb25lOlxuICAgICAgICAgICAgc3VibmV0ID0gW3JhbmRvbS5jaG9pY2Uoc2VsZi5PUFMpIGZvciBfIGluIHJhbmdlKHNlbGYubl9sYXllcnMpXVxuICAgICAgICBmb3Igb3BfY2hvaWNlLCBsYXllcl9vcHMgaW4gemlwKHN1Ym5ldCwgc2VsZi5sYXllcnMpOlxuICAgICAgICAgICAgeCA9IGxheWVyX29wc1tvcF9jaG9pY2VdKHgpXG4gICAgICAgIHJldHVybiBzZWxmLmNsYXNzaWZpZXIoeCkuc3F1ZWV6ZSgtMSkuc3F1ZWV6ZSgtMSlcblxuIyBUcmFpbiBzdXBlcm5ldCB3aXRoIHJhbmRvbSBzdWJuZXQgc2FtcGxpbmdcbnN1cGVybmV0ID0gU3VwZXJuZXQobl9sYXllcnM9NCwgQz0zMilcbnggPSB0b3JjaC5yYW5kbig0LCAzMiwgOCwgOClcbiMgRWFjaCBmb3J3YXJkIHVzZXMgYSBkaWZmZXJlbnQgcmFuZG9tIHN1Ym5ldCAtXHUwMDNlIGFsbCBvcCB3ZWlnaHRzIGdldCB0cmFpbmVkXG5mb3Igc3RlcCBpbiByYW5nZSgzKTpcbiAgICBzdWJuZXQgPSBbcmFuZG9tLmNob2ljZShTdXBlcm5ldC5PUFMpIGZvciBfIGluIHJhbmdlKDQpXVxuICAgIG91dCA9IHN1cGVybmV0KHgsIHN1Ym5ldClcbiAgICBwcmludChmXHUwMDI3U3RlcCB7c3RlcCsxfSBzdWJuZXQ9e3N1Ym5ldH0gIG91dC5zaGFwZT17b3V0LnNoYXBlfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IldlaWdodCBDb3VwbGluZyBpbiBPbmUtU2hvdCBOQVMiLCJjb250ZW50IjoiSW4gYSBvbmUtc2hvdCBzdXBlcm5ldCwgYWxsIHN1Ym5ldHMgc2hhcmUgd2VpZ2h0cy4gVGhpcyBjYXVzZXMgd2VpZ2h0IGNvdXBsaW5nOiB0aGUgb3B0aW1hbCB3ZWlnaHRzIGZvciB0aGUgY29udjMgc3VibmV0IGFyZSBub3QgdGhlIHNhbWUgYXMgdGhlIG9wdGltYWwgd2VpZ2h0cyB3aGVuIGNvbnYzIGNvZXhpc3RzIHdpdGggY29udjUuIFRoaXMgY291cGxpbmcgbWVhbnMgdGhlIHN1cGVybmV0IHJhbmtpbmcgb2Ygc3VibmV0cyBkb2VzIG5vdCBwZXJmZWN0bHkgY29ycmVsYXRlIHdpdGggdGhlaXIgc3RhbmRhbG9uZSBhY2N1cmFjeSBhZnRlciByZXRyYWluaW5nLiBPbmNlLWZvci1BbGwgKE9GQSkgYWRkcmVzc2VzIHRoaXMgd2l0aCBwcm9ncmVzc2l2ZSBzaHJpbmtpbmcgYW5kIGluLXBsYWNlIGRpc3RpbGxhdGlvbi4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJOQVMgTWV0aG9kIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiR1BVLURheXMgKFNlYXJjaCkiLCJTZWFyY2ggVHlwZSIsIlRvcC0xIEltYWdlTmV0IiwiRkxPUCBFZmZpY2llbmN5IiwiVGFyZ2V0IEhhcmR3YXJlIl0sInJvd3MiOltbIlJMLU5BUyAoWm9waCAyMDE3KSIsIn4xODAwIEdQVS1kYXlzIiwiRGlzY3JldGUgc2FtcGxpbmcgdmlhIFJMIGNvbnRyb2xsZXIiLCI3NC4wJSIsIk5vdCBvcHRpbWl6ZWQiLCJHZW5lcmljIl0sWyJEQVJUUyAoMjAxOSkiLCJ+NCBHUFUtZGF5cyIsIkNvbnRpbnVvdXMgcmVsYXhhdGlvbiwgZ3JhZGllbnQiLCI3My4zJSIsIk5vdCBvcHRpbWl6ZWQiLCJHZW5lcmljIl0sWyJGQk5ldCAoMjAxOSkiLCJ+OSBHUFUtZGF5cyIsIkd1bWJlbC1zb2Z0bWF4ICsgbGF0ZW5jeSB0YWJsZSIsIjc0LjklIiwiTW9iaWxlICg1ME0gRkxPUHMpIiwiTW9iaWxlIENQVSJdLFsiT25lLXNob3QgKFNOQVMpIiwifjEuNSBHUFUtZGF5cyIsIldlaWdodCBzaGFyaW5nICsgc3RvY2hhc3RpYyBzYW1wbGluZyIsIjcyLjclIiwiTW9kZXJhdGUiLCJHZW5lcmljIl0sWyJFZmZpY2llbnROZXQgKG1hbnVhbCtOQVMpIiwifk4vQSAoY29tcG91bmQpIiwiR3JpZCBzZWFyY2ggb3ZlciBkZXB0aC93aWR0aC9yZXMiLCI4NC40JSIsIkV4Y2VsbGVudCBQYXJldG8iLCJBbGwgaGFyZHdhcmUiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRBUlRTIFBpdGZhbGxzIGFuZCBGaXhlcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiREFSVFMgaGFzIGtub3duIGZhaWx1cmUgbW9kZXMuIFRoZSBiaS1sZXZlbCBvcHRpbWl6YXRpb24gaXMgb25seSBhbiBhcHByb3hpbWF0aW9uOiB0aGUgaW5uZXIgb3B0aW1pemF0aW9uICh3ZWlnaHQgdXBkYXRlKSBpcyBub3QgdGFrZW4gdG8gY29udmVyZ2VuY2UsIHNvIHRoZSBhcmNoaXRlY3R1cmUgZ3JhZGllbnQgaXMgYmlhc2VkLiBUaGlzIGNhbiBjYXVzZSB0aGUgc2VhcmNoIHRvIG92ZXItc2VsZWN0IHNraXAgY29ubmVjdGlvbnMgKHplcm8tcGFyYW1ldGVyLCBsb3ctbG9zcyBvcGVyYXRpb25zKSwgY29sbGFwc2luZyB0aGUgYXJjaGl0ZWN0dXJlIHRvIGEgbmVhci1pZGVudGl0eSBtYXBwaW5nLiBGaXhlcyBpbmNsdWRlIERBUlRTKyAocmVndWxhcml6ZSBza2lwIGNvdW50KSwgR0RBUyAoR3VtYmVsLXNvZnRtYXggd2l0aCB0ZW1wZXJhdHVyZSBhbm5lYWxpbmcpLCBhbmQgU05BUyAoc3RvY2hhc3RpYyBOQVMgd2l0aCBLTCBkaXZlcmdlbmNlIGNvbnN0cmFpbnRzKS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgcHJhY3RpY2FsIERBUlRTIHRyYWluaW5nIHNjaGVkdWxlOiBzZWFyY2ggZm9yIDUwIGVwb2NocyB3aXRoIGFyY2hpdGVjdHVyZSBMUiAzZS00IGFuZCB3ZWlnaHQgTFIgM2UtNDsga2VlcCBhIHN0cmljdCA1MC81MCB0cmFpbi92YWwgc3BsaXQgc28gYXJjaGl0ZWN0dXJlIGdyYWRpZW50cyBhcmUgbm90IGNvbXB1dGVkIG9uIHRyYWluaW5nIGRhdGE7IGFmdGVyIHNlYXJjaCwgZGlzY3JldGl6ZSBhbmQgcmUtdHJhaW4gdGhlIGRpc2NvdmVyZWQgYXJjaGl0ZWN0dXJlIGZyb20gc2NyYXRjaCBmb3IgNjAwIGVwb2Nocy4gVGhlIHJlLXRyYWluaW5nIHN0ZXAgaXMgaW1wb3J0YW50IOKAlCBhY2N1cmFjeSBtZWFzdXJlZCBvbiB0aGUgbWl4ZWQgb3BlcmF0aW9uIHN1cGVybmV0IGlzIG5vdCByZXByZXNlbnRhdGl2ZSBvZiB0aGUgZGlzY3JldGl6ZWQgYXJjaGl0ZWN0dXJlLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU2tpcCBjb25uZWN0aW9uIGNvbGxhcHNlOiBEQVJUUyB0ZW5kcyB0byBzZWxlY3Qgc2tpcCBjb25uZWN0aW9ucyDigJQgZm9yY2UgYXQgbW9zdCAyIHNraXBzIHBlciBjZWxsLiIsIkJpLWxldmVsIGFwcHJveGltYXRpb24gYmlhczogdXNlIGZpcnN0LW9yZGVyIERBUlRTIChpZ25vcmUgc2Vjb25kLW9yZGVyIEhlc3NpYW4pIGZvciBzdGFiaWxpdHkgYXQgc2xpZ2h0IGFjY3VyYWN5IGNvc3QuIiwiRGlzY3JldGl6ZSB0aGVuIHJldHJhaW46IHRoZSBzdXBlcm5ldCBhY2N1cmFjeSBpcyBub3QgdGhlIGZpbmFsIG1vZGVsIGFjY3VyYWN5IOKAlCBhbHdheXMgcmV0cmFpbiBmcm9tIHNjcmF0Y2guIiwiUHJveHkgdGFzazogc2VhcmNoIG9uIGEgc21hbGwgcHJveHkgKENJRkFSLTEwKSB0aGVuIHRyYW5zZmVyIGFyY2hpdGVjdHVyZSB0byB0aGUgdGFyZ2V0IGRhdGFzZXQuIiwiRWFybHkgc3RvcHBpbmcgb2YgYXJjaCBzZWFyY2g6IG92ZXItc2VhcmNoaW5nIGRlZ3JhZGVzIHRoZSBhcmNoaXRlY3R1cmUg4oCUIDUwIGVwb2NocyBpcyB1c3VhbGx5IGVub3VnaC4iLCJPbmUtc2hvdCB2cyBEQVJUUzogb25lLXNob3QgYXZvaWRzIGJpLWxldmVsIGVudGlyZWx5IGJ5IHRyYWluaW5nIGEgc3VwZXJuZXQgYW5kIHNhbXBsaW5nIHN1Ym5ldHMuIl19LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRWZmaWNpZW5jeSBwcm94aWVzIGJleW9uZCBsYXRlbmN5IHRhYmxlcyBpbmNsdWRlIEZMT1BzLCBudW1iZXIgb2YgcGFyYW1ldGVycywgYW5kIGVuZXJneSBjb25zdW1wdGlvbi4gRkxPUHMgaXMgaGFyZHdhcmUtYWdub3N0aWMgYnV0IGRvZXMgbm90IGFjY291bnQgZm9yIG1lbW9yeSBiYW5kd2lkdGgg4oCUIGEgZGVwdGh3aXNlIGNvbnYgaGFzIGZhciBmZXdlciBGTE9QcyB0aGFuIGEgc3RhbmRhcmQgY29udiBidXQgaXMgbWVtb3J5LWJhbmR3aWR0aC1ib3VuZCBvbiBHUFUuIExhdGVuY3kgbG9va3VwIHRhYmxlcyBtZWFzdXJlZCBvbiB0aGUgYWN0dWFsIHRhcmdldCBkZXZpY2UgYXJlIG1vcmUgYWNjdXJhdGUgcHJveGllcywgZXNwZWNpYWxseSBmb3IgbW9iaWxlIENQVSB2cyBHUFUgdnMgRFNQLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiRkxPUHM6IGVhc3kgdG8gY29tcHV0ZSBhbmFseXRpY2FsbHkgYnV0IHBvb3IgcHJlZGljdG9yIG9mIEdQVSBsYXRlbmN5IChtZW1vcnktYm91bmQgb3BlcmF0aW9ucyBhcmUgcGVuYWxpc2VkIHVuZmFpcmx5KS4iLCJMYXRlbmN5IExVVDogbWVhc3VyZSBlYWNoIChvcCwgcmVzb2x1dGlvbiwgY2hhbm5lbCkgY29tYmluYXRpb24gb24gdGFyZ2V0IGRldmljZTsgZmFzdCB0byBxdWVyeSBkdXJpbmcgc2VhcmNoLiIsIkVuZXJneTogY3JpdGljYWwgZm9yIGJhdHRlcnktcG93ZXJlZCBkZXZpY2VzOyBjb3JyZWxhdGVzIHdpdGggbWVtb3J5IGFjY2VzcyBjb3VudCBtb3JlIHRoYW4gRkxPUHMuIiwiTW9kZWwgc2l6ZSAoTUIpOiBpbXBvcnRhbnQgZm9yIG92ZXItdGhlLWFpciB1cGRhdGUgYW5kIG9uLWRldmljZSBzdG9yYWdlLCBub3QgZm9yIGluZmVyZW5jZSBzcGVlZC4iLCJIYXJkd2FyZS1hd2FyZSBOQVM6IFByb3h5bGVzc05BUywgRkJOZXQsIE1OQVNOZXQg4oCUIGFsbCB1c2UgaGFyZHdhcmUtc3BlY2lmaWMgbGF0ZW5jeSBtb2RlbHMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# NAS — Differentiable Architecture Search and Efficiency Proxies

Neural architecture search (NAS) automates the design of neural network architectures by formulating architecture selection as an optimization problem. Early NAS methods used reinforcement learning to train a controller that proposes architectures, evaluated each on a proxy task, and updated the controller based on the validation accuracy. This required thousands of GPU-hours and hundreds of GPU machines. Modern NAS methods — DARTS, one-shot supernets, and efficiency-aware search — have reduced the cost to a single GPU-day or less.

## Search Space Definition

The search space determines which architectures can be found. A typical cell-based search space defines a computational cell (a small graph of operations) and stacks N cells to form the full network. At each edge in the cell, the operation is chosen from a candidate set: 3×3 conv, 5×5 conv, 3×3 dilated conv, 3×3 max pool, skip connection, zero. With 7 candidate ops and 14 edges in a cell, the search space has 7^14 ≈ 10^12 possible cells. RL-NAS samples directly from this space; DARTS relaxes it to a continuous mixture.

## DARTS — Differentiable Mixed Operation

DARTS (Liu et al. 2019) relaxes the discrete operation selection to a continuous mixture: for each edge, the output is a weighted sum of all candidate operations: ō(x) = Σ_i exp(α_i) / Σ_j exp(α_j) · o_i(x). The architecture parameters α (one per operation per edge) are learned jointly with the weight parameters w by gradient descent. After search, the architecture is discretized by selecting the highest-α operation on each edge.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MixedOp(nn.Module):
    """DARTS mixed operation: weighted softmax mixture of candidate ops."""

    CANDIDATES = {
        'skip': lambda C: nn.Identity(),
        'conv3x3': lambda C: nn.Sequential(nn.Conv2d(C, C, 3, padding=1, bias=False), nn.BatchNorm2d(C)),
        'conv5x5': lambda C: nn.Sequential(nn.Conv2d(C, C, 5, padding=2, bias=False), nn.BatchNorm2d(C)),
        'maxpool': lambda C: nn.MaxPool2d(3, stride=1, padding=1),
        'avgpool': lambda C: nn.AvgPool2d(3, stride=1, padding=1),
    }

    def __init__(self, C: int):
        super().__init__()
        self.ops = nn.ModuleList([fn(C) for fn in self.CANDIDATES.values()])
        self.op_names = list(self.CANDIDATES.keys())
        # Architecture weights (α) — not in model.parameters(), trained separately
        self.arch_weights = nn.Parameter(torch.zeros(len(self.ops)))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        weights = F.softmax(self.arch_weights, dim=0)
        return sum(w * op(x) for w, op in zip(weights, self.ops))

    def discretize(self) -> str:
        """Return the name of the operation with highest arch weight."""
        best = self.arch_weights.argmax().item()
        return self.op_names[best]

# Demo
C = 16
mixed = MixedOp(C)
x = torch.randn(2, C, 8, 8)
out = mixed(x)
print(f'Output shape: {out.shape}')
print(f'Arch weights (softmax): {F.softmax(mixed.arch_weights, dim=0).detach().round(decimals=3).tolist()}')
print(f'Discretized operation: {mixed.discretize()}')
```

## DARTS Bi-Level Optimization

```python
import torch
import torch.nn as nn
import torch.optim as optim

def darts_train_step(model, arch_params, train_batch, val_batch, criterion,
                     w_optimizer, arch_optimizer, inner_steps=1):
    """
    DARTS alternating optimization:
    1. Update architecture params alpha on validation loss.
    2. Update weight params w on training loss.
    """
    X_train, y_train = train_batch
    X_val, y_val = val_batch

    # Step 1: Update architecture parameters on validation set
    arch_optimizer.zero_grad()
    val_loss = criterion(model(X_val), y_val)
    val_loss.backward()
    arch_optimizer.step()

    # Step 2: Update weight parameters on training set
    for _ in range(inner_steps):
        w_optimizer.zero_grad()
        train_loss = criterion(model(X_train), y_train)
        train_loss.backward()
        w_optimizer.step()

    return train_loss.item(), val_loss.item()

# Separate weight and arch parameters for dual optimizers
# (arch_params have requires_grad=True and are passed to arch_optimizer)
print('DARTS bi-level: arch optimizer -> val loss; weight optimizer -> train loss')
print('After search: discretize by argmax(arch_weights) per edge.')
print('Re-train discretized architecture from scratch for fair comparison.')
```

## Efficiency-Aware NAS

Accuracy alone is insufficient for mobile and edge deployment. Efficiency-aware NAS adds a hardware cost term to the objective: L_total = L_CE(y, ŷ) + λ · log(latency(α)). The latency is estimated from a lookup table (op × resolution × hardware) rather than measured at every step. FBNet and ProxylessNAS use this approach. The λ hyperparameter controls the accuracy-latency trade-off; sweeping λ produces a Pareto frontier of architectures.

```python
import torch
import torch.nn as nn

# Latency lookup table: op -> (ms on mobile CPU, ms on server GPU)
LATENCY_TABLE = {
    'skip':    (0.05, 0.01),
    'conv3x3': (1.20, 0.15),
    'conv5x5': (2.80, 0.30),
    'maxpool': (0.30, 0.04),
    'avgpool': (0.25, 0.04),
}

def differentiable_latency(arch_weights: torch.Tensor,
                           op_names: list,
                           target: str = 'mobile') -> torch.Tensor:
    """
    Expected latency as a differentiable function of arch weights.
    target: 'mobile' (index 0) or 'server' (index 1)
    """
    idx = 0 if target == 'mobile' else 1
    lat_tensor = torch.tensor(
        [LATENCY_TABLE[name][idx] for name in op_names],
        dtype=torch.float32
    )
    probs = torch.softmax(arch_weights, dim=0)
    return (probs * lat_tensor).sum()  # expected latency

def efficiency_aware_loss(task_loss, arch_weights, op_names, lam=0.1, target='mobile'):
    lat = differentiable_latency(arch_weights, op_names, target)
    return task_loss + lam * torch.log(lat + 1e-6)

# Demo
arch_w = torch.randn(5, requires_grad=True)
op_names = list(LATENCY_TABLE.keys())
task_loss = torch.tensor(1.5)
total_loss = efficiency_aware_loss(task_loss, arch_w, op_names, lam=0.1)
total_loss.backward()
print(f'Total loss: {total_loss.item():.4f}')
print(f'arch_w grad: {arch_w.grad.round(decimals=4).tolist()}')
```

## One-Shot Supernet with Weight Sharing

```python
import torch
import torch.nn as nn
import random

class Supernet(nn.Module):
    """One-shot supernet: all subnets share the same weights."""

    OPS = ['skip', 'conv3', 'conv5', 'pool']

    def __init__(self, n_layers: int = 4, C: int = 32):
        super().__init__()
        self.n_layers = n_layers
        self.layers = nn.ModuleList([
            nn.ModuleDict({
                'skip':  nn.Identity(),
                'conv3': nn.Sequential(nn.Conv2d(C, C, 3, padding=1), nn.ReLU()),
                'conv5': nn.Sequential(nn.Conv2d(C, C, 5, padding=2), nn.ReLU()),
                'pool':  nn.AvgPool2d(3, stride=1, padding=1),
            })
            for _ in range(n_layers)
        ])
        self.classifier = nn.AdaptiveAvgPool2d(1)

    def forward(self, x: torch.Tensor, subnet: list = None) -> torch.Tensor:
        """subnet: list of op names per layer. If None, sample randomly."""
        if subnet is None:
            subnet = [random.choice(self.OPS) for _ in range(self.n_layers)]
        for op_choice, layer_ops in zip(subnet, self.layers):
            x = layer_ops[op_choice](x)
        return self.classifier(x).squeeze(-1).squeeze(-1)

# Train supernet with random subnet sampling
supernet = Supernet(n_layers=4, C=32)
x = torch.randn(4, 32, 8, 8)
# Each forward uses a different random subnet -> all op weights get trained
for step in range(3):
    subnet = [random.choice(Supernet.OPS) for _ in range(4)]
    out = supernet(x, subnet)
    print(f'Step {step+1} subnet={subnet}  out.shape={out.shape}')
```

> **Weight Coupling in One-Shot NAS**: In a one-shot supernet, all subnets share weights. This causes weight coupling: the optimal weights for the conv3 subnet are not the same as the optimal weights when conv3 coexists with conv5. This coupling means the supernet ranking of subnets does not perfectly correlate with their standalone accuracy after retraining. Once-for-All (OFA) addresses this with progressive shrinking and in-place distillation.

## NAS Method Comparison

| Method | GPU-Days (Search) | Search Type | Top-1 ImageNet | FLOP Efficiency | Target Hardware |
| --- | --- | --- | --- | --- | --- |
| RL-NAS (Zoph 2017) | ~1800 GPU-days | Discrete sampling via RL controller | 74.0% | Not optimized | Generic |
| DARTS (2019) | ~4 GPU-days | Continuous relaxation, gradient | 73.3% | Not optimized | Generic |
| FBNet (2019) | ~9 GPU-days | Gumbel-softmax + latency table | 74.9% | Mobile (50M FLOPs) | Mobile CPU |
| One-shot (SNAS) | ~1.5 GPU-days | Weight sharing + stochastic sampling | 72.7% | Moderate | Generic |
| EfficientNet (manual+NAS) | ~N/A (compound) | Grid search over depth/width/res | 84.4% | Excellent Pareto | All hardware |

## DARTS Pitfalls and Fixes

DARTS has known failure modes. The bi-level optimization is only an approximation: the inner optimization (weight update) is not taken to convergence, so the architecture gradient is biased. This can cause the search to over-select skip connections (zero-parameter, low-loss operations), collapsing the architecture to a near-identity mapping. Fixes include DARTS+ (regularize skip count), GDAS (Gumbel-softmax with temperature annealing), and SNAS (stochastic NAS with KL divergence constraints).

A practical DARTS training schedule: search for 50 epochs with architecture LR 3e-4 and weight LR 3e-4; keep a strict 50/50 train/val split so architecture gradients are not computed on training data; after search, discretize and re-train the discovered architecture from scratch for 600 epochs. The re-training step is important — accuracy measured on the mixed operation supernet is not representative of the discretized architecture.

- Skip connection collapse: DARTS tends to select skip connections — force at most 2 skips per cell.
- Bi-level approximation bias: use first-order DARTS (ignore second-order Hessian) for stability at slight accuracy cost.
- Discretize then retrain: the supernet accuracy is not the final model accuracy — always retrain from scratch.
- Proxy task: search on a small proxy (CIFAR-10) then transfer architecture to the target dataset.
- Early stopping of arch search: over-searching degrades the architecture — 50 epochs is usually enough.
- One-shot vs DARTS: one-shot avoids bi-level entirely by training a supernet and sampling subnets.

Efficiency proxies beyond latency tables include FLOPs, number of parameters, and energy consumption. FLOPs is hardware-agnostic but does not account for memory bandwidth — a depthwise conv has far fewer FLOPs than a standard conv but is memory-bandwidth-bound on GPU. Latency lookup tables measured on the actual target device are more accurate proxies, especially for mobile CPU vs GPU vs DSP.

- FLOPs: easy to compute analytically but poor predictor of GPU latency (memory-bound operations are penalised unfairly).
- Latency LUT: measure each (op, resolution, channel) combination on target device; fast to query during search.
- Energy: critical for battery-powered devices; correlates with memory access count more than FLOPs.
- Model size (MB): important for over-the-air update and on-device storage, not for inference speed.
- Hardware-aware NAS: ProxylessNAS, FBNet, MNASNet — all use hardware-specific latency models.

---

