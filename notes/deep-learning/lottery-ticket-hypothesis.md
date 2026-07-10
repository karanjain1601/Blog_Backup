---
title: "Lottery Ticket Hypothesis — Winning Tickets and IMP"
slug: "lottery-ticket-hypothesis"
description: "Implement Iterative Magnitude Pruning from scratch, validate the lottery ticket hypothesis by comparing winning tickets vs random sparse masks, detect early-bird tickets, and transfer tickets across datasets."
tags: ["deep-learning", "neural-networks"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIExvdHRlcnkgVGlja2V0IEh5cG90aGVzaXMgKEZyYW5rbGUgXHUwMDI2IENhcmxpbiAyMDE5KSBzdGF0ZXM6IGEgcmFuZG9tbHkgaW5pdGlhbGl6ZWQgZGVuc2UgbmV1cmFsIG5ldHdvcmsgY29udGFpbnMgYSBzcGFyc2Ugc3VibmV0d29yayDigJQgYSB3aW5uaW5nIHRpY2tldCDigJQgdGhhdCwgd2hlbiB0cmFpbmVkIGluIGlzb2xhdGlvbiBmcm9tIGl0cyBvcmlnaW5hbCBpbml0aWFsaXphdGlvbiwgY2FuIG1hdGNoIHRoZSBmdWxsIG5ldHdvcmtcdTAwMjdzIHRlc3QgYWNjdXJhY3kgd2l0aGluIHRoZSBzYW1lIHRyYWluaW5nIGJ1ZGdldC4gRmluZGluZyB3aW5uaW5nIHRpY2tldHMgcmVxdWlyZXMgSXRlcmF0aXZlIE1hZ25pdHVkZSBQcnVuaW5nIChJTVApIHdpdGggdGhlIGNyaXRpY2FsIHN0ZXAgb2YgcmV3aW5kaW5nIHRvIHRoZSBvcmlnaW5hbCBpbml0aWFsaXphdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoaXMgaXMgcmVtYXJrYWJsZTogdGhlIGZ1bGwgbmV0d29ya1x1MDAyN3MgZXhwcmVzc2l2aXR5IGlzIG5vdCBuZWNlc3NhcnkgZm9yIGdvb2QgZ2VuZXJhbGl6YXRpb24uIFRoZSBoeXBvdGhlc2lzIHJlZnJhbWVzIHBydW5pbmcgZnJvbSBwb3N0LXRyYWluaW5nIGNvbXByZXNzaW9uIHRvIHByZS10cmFpbmluZyBhcmNoaXRlY3R1cmUgc2VhcmNoLiBUaGUgd2lubmluZyB0aWNrZXQgaXMgbm90IHRoZSBwcnVuZWQgbmV0d29yayBhZnRlciB0cmFpbmluZyDigJQgaXQgaXMgdGhlIHNwYXJzZSBzdWJuZXR3b3JrIHRoYXQsIHdoZW4gaW5pdGlhbGl6ZWQgdG8gaXRzIG9yaWdpbmFsIHZhbHVlcyBhbmQgdHJhaW5lZCBmcm9tIHNjcmF0Y2ggKGJ1dCB3aXRoIHRoZSBtYXNrKSwgYWNoaWV2ZXMgdGhlIHNhbWUgYWNjdXJhY3kuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiSXRlcmF0aXZlIE1hZ25pdHVkZSBQcnVuaW5nIChJTVApIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJTVAgY29uc2lzdHMgb2YgZm91ciBzdGVwcyByZXBlYXRlZCBrIHRpbWVzOiAoMSkgVHJhaW4gdGhlIGZ1bGwgbmV0d29yayB0byBjb252ZXJnZW5jZSBmcm9tIGluaXRpYWxpemF0aW9uIM644oKALiAoMikgUHJ1bmUgcCUgb2YgcmVtYWluaW5nIHdlaWdodHMgZ2xvYmFsbHkgYnkgbWFnbml0dWRlLiAoMykgUmVzZXQgcmVtYWluaW5nIHdlaWdodHMgdG8gzrjigoAg4oCUIHRoZSByZXdpbmQgc3RlcC4gKDQpIFJlcGVhdCB3aXRoIHRoZSBwcnVuZWQsIHJld291bmQgbmV0d29yay4gRWFjaCByb3VuZCBwcnVuZXMgcCUgb2YgcmVtYWluaW5nIHdlaWdodHMsIHNvIGFmdGVyIGsgcm91bmRzIHRoZSBzcGFyc2l0eSBpcyAx4oiSKDHiiJJwKV5rLiBQcnVuaW5nIDIwJSBwZXIgcm91bmQgZm9yIDEwIHJvdW5kcyBhY2hpZXZlcyB+ODklIHNwYXJzaXR5LiBUaGUgbWFzayBkZWZpbmVzIHRoZSB3aW5uaW5nIHRpY2tldCBzdHJ1Y3R1cmUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5pbXBvcnQgY29weVxuXG5jbGFzcyBJTVA6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG1vZGVsKTpcbiAgICAgICAgc2VsZi5tb2RlbCA9IG1vZGVsXG4gICAgICAgIHNlbGYudGhldGEwID0gY29weS5kZWVwY29weShtb2RlbC5zdGF0ZV9kaWN0KCkpXG4gICAgICAgIHNlbGYubWFza3MgPSB7bjogdG9yY2gub25lc19saWtlKHApXG4gICAgICAgICAgICAgICAgICAgICAgZm9yIG4sIHAgaW4gbW9kZWwubmFtZWRfcGFyYW1ldGVycygpIGlmIFx1MDAyN3dlaWdodFx1MDAyNyBpbiBufVxuXG4gICAgZGVmIHRyYWluX3N0ZXAoc2VsZiwgeCwgeSwgb3B0aW1pemVyLCBjcml0ZXJpb24pOlxuICAgICAgICBvcHRpbWl6ZXIuemVyb19ncmFkKClcbiAgICAgICAgbG9zcyA9IGNyaXRlcmlvbihzZWxmLm1vZGVsKHgpLCB5KVxuICAgICAgICBsb3NzLmJhY2t3YXJkKClcbiAgICAgICAgZm9yIG4sIHAgaW4gc2VsZi5tb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCk6XG4gICAgICAgICAgICBpZiBuIGluIHNlbGYubWFza3MgYW5kIHAuZ3JhZCBpcyBub3QgTm9uZTpcbiAgICAgICAgICAgICAgICBwLmdyYWQuZGF0YS5tdWxfKHNlbGYubWFza3Nbbl0pXG4gICAgICAgIG9wdGltaXplci5zdGVwKClcbiAgICAgICAgcmV0dXJuIGxvc3MuaXRlbSgpXG5cbiAgICBkZWYgcHJ1bmUoc2VsZiwgcHJ1bmVfcmF0ZT0wLjIpOlxuICAgICAgICBhbGxfdyA9IHRvcmNoLmNhdChbcC5hYnMoKS5mbGF0dGVuKCkgZm9yIG4sIHAgaW4gc2VsZi5tb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKClcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIG4gaW4gc2VsZi5tYXNrc10pXG4gICAgICAgIHRocmVzaCA9IHRvcmNoLnF1YW50aWxlKGFsbF93LCBwcnVuZV9yYXRlKVxuICAgICAgICBmb3IgbiwgcCBpbiBzZWxmLm1vZGVsLm5hbWVkX3BhcmFtZXRlcnMoKTpcbiAgICAgICAgICAgIGlmIG4gaW4gc2VsZi5tYXNrczpcbiAgICAgICAgICAgICAgICBzZWxmLm1hc2tzW25dID0gKHAuZGF0YS5hYnMoKSBcdTAwM2UgdGhyZXNoKS5mbG9hdCgpXG5cbiAgICBkZWYgcmV3aW5kKHNlbGYpOlxuICAgICAgICBzZWxmLm1vZGVsLmxvYWRfc3RhdGVfZGljdChjb3B5LmRlZXBjb3B5KHNlbGYudGhldGEwKSlcbiAgICAgICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgICAgICBmb3IgbiwgcCBpbiBzZWxmLm1vZGVsLm5hbWVkX3BhcmFtZXRlcnMoKTpcbiAgICAgICAgICAgICAgICBpZiBuIGluIHNlbGYubWFza3M6IHAuZGF0YS5tdWxfKHNlbGYubWFza3Nbbl0pXG5cbiAgICBkZWYgc3BhcnNpdHkoc2VsZik6XG4gICAgICAgIHRvdGFsID0gc3VtKG0ubnVtZWwoKSBmb3IgbSBpbiBzZWxmLm1hc2tzLnZhbHVlcygpKVxuICAgICAgICBhY3RpdmUgPSBzdW0obS5zdW0oKS5pdGVtKCkgZm9yIG0gaW4gc2VsZi5tYXNrcy52YWx1ZXMoKSlcbiAgICAgICAgcmV0dXJuIDEuMCAtIGFjdGl2ZSAvIHRvdGFsXG5cbnByaW50KFx1MDAyN0lNUDogdHJhaW5fc3RlcCwgcHJ1bmUsIHJld2luZCwgc3BhcnNpdHkgcmVhZHkuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ildpbm5pbmcgVGlja2V0IHZzIFJhbmRvbSBTcGFyc2UgTWFzayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHdpbm5pbmcgdGlja2V0IHByb3BlcnR5IGRlcGVuZHMgb24gYm90aCB0aGUgbWFzayBzdHJ1Y3R1cmUgQU5EIHRoZSBzcGVjaWZpYyBpbml0aWFsaXphdGlvbiDOuOKCgC4gVG8gdmVyaWZ5OiBjb21wYXJlIChBKSB3aW5uaW5nIHRpY2tldCDigJQgSU1QIG1hc2sgKyByZXdpbmQgdG8gzrjigoAsIChCKSByYW5kb20gc3BhcnNlIG1hc2sg4oCUIHNhbWUgc3BhcnNpdHkgYnV0IHJhbmRvbWx5IGNob3NlbiBjb25uZWN0aW9ucywgYWxzbyBpbml0aWFsaXplZCBmcm9tIM644oKALiBJZiB0aGUgaHlwb3RoZXNpcyBob2xkcywgKEEpIHNpZ25pZmljYW50bHkgb3V0cGVyZm9ybXMgKEIpIGF0IHRoZSBzYW1lIHNwYXJzaXR5IGxldmVsLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IGNvcHlcbmZyb20gc2tsZWFybi5kYXRhc2V0cyBpbXBvcnQgbWFrZV9jbGFzc2lmaWNhdGlvblxuXG5kZWYgc2ltcGxlX25ldChzZWVkPTApOlxuICAgIHRvcmNoLm1hbnVhbF9zZWVkKHNlZWQpXG4gICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDIwLDY0KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoNjQsNjQpLCBubi5SZUxVKCksIG5uLkxpbmVhcig2NCwyKSlcblxuZGVmIHRyYWluX2V2YWwobW9kZWwsIFhfdHIsIHlfdHIsIFhfdGUsIHlfdGUsIG1hc2s9Tm9uZSwgbl9lcG9jaHM9ODApOlxuICAgIG9wdCA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0zKVxuICAgIGZvciBfIGluIHJhbmdlKG5fZXBvY2hzKTpcbiAgICAgICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgICAgIGxvc3MgPSBubi5Dcm9zc0VudHJvcHlMb3NzKCkobW9kZWwoWF90ciksIHlfdHIpXG4gICAgICAgIGxvc3MuYmFja3dhcmQoKVxuICAgICAgICBpZiBtYXNrOlxuICAgICAgICAgICAgZm9yIG4sIHAgaW4gbW9kZWwubmFtZWRfcGFyYW1ldGVycygpOlxuICAgICAgICAgICAgICAgIGlmIG4gaW4gbWFzayBhbmQgcC5ncmFkIGlzIG5vdCBOb25lOiBwLmdyYWQuZGF0YS5tdWxfKG1hc2tbbl0pXG4gICAgICAgIG9wdC5zdGVwKClcbiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgcmV0dXJuIChtb2RlbChYX3RlKS5hcmdtYXgoMSkgPT0geV90ZSkuZmxvYXQoKS5tZWFuKCkuaXRlbSgpXG5cblhfbnAsIHlfbnAgPSBtYWtlX2NsYXNzaWZpY2F0aW9uKDgwMCwgMjAsIG5fY2xhc3Nlcz0yLCByYW5kb21fc3RhdGU9MClcblggPSB0b3JjaC50ZW5zb3IoWF9ucCwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnkgPSB0b3JjaC50ZW5zb3IoeV9ucCwgZHR5cGU9dG9yY2gubG9uZylcblhfdHIsIHlfdHIsIFhfdGUsIHlfdGUgPSBYWzo2MDBdLCB5Wzo2MDBdLCBYWzYwMDpdLCB5WzYwMDpdXG5cbmZ1bGwgPSBzaW1wbGVfbmV0KDApXG5hY2NfZnVsbCA9IHRyYWluX2V2YWwoZnVsbCwgWF90ciwgeV90ciwgWF90ZSwgeV90ZSlcbnByaW50KGZcdTAwMjdGdWxsIG5ldHdvcms6IHthY2NfZnVsbDouNGZ9XHUwMDI3KVxuXG53dF9tYXNrID0ge246IChwLmFicygpIFx1MDAzZSBwLmFicygpLnF1YW50aWxlKDAuNSkpLmZsb2F0KCkgZm9yIG4sIHAgaW4gZnVsbC5uYW1lZF9wYXJhbWV0ZXJzKCkgaWYgXHUwMDI3d2VpZ2h0XHUwMDI3IGluIG59XG53dCA9IHNpbXBsZV9uZXQoMClcbmZvciBuLCBwIGluIHd0Lm5hbWVkX3BhcmFtZXRlcnMoKTpcbiAgICBpZiBuIGluIHd0X21hc2s6IHAuZGF0YS5tdWxfKHd0X21hc2tbbl0pXG5wcmludChmXHUwMDI3V2lubmluZyB0aWNrZXQgKDUwJSBzcGFyc2UpOiB7dHJhaW5fZXZhbCh3dCwgWF90ciwgeV90ciwgWF90ZSwgeV90ZSwgd3RfbWFzayk6LjRmfVx1MDAyNylcblxucmFuZF9tYXNrID0ge246ICh0b3JjaC5yYW5kX2xpa2UocCkgXHUwMDNlIDAuNSkuZmxvYXQoKSBmb3IgbiwgcCBpbiBmdWxsLm5hbWVkX3BhcmFtZXRlcnMoKSBpZiBcdTAwMjd3ZWlnaHRcdTAwMjcgaW4gbn1cbnJhbmQgPSBzaW1wbGVfbmV0KDApXG5mb3IgbiwgcCBpbiByYW5kLm5hbWVkX3BhcmFtZXRlcnMoKTpcbiAgICBpZiBuIGluIHJhbmRfbWFzazogcC5kYXRhLm11bF8ocmFuZF9tYXNrW25dKVxucHJpbnQoZlx1MDAyN1JhbmRvbSBzcGFyc2UgICg1MCUgc3BhcnNlKToge3RyYWluX2V2YWwocmFuZCwgWF90ciwgeV90ciwgWF90ZSwgeV90ZSwgcmFuZF9tYXNrKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVhcmx5IEJpcmQgVGlja2V0cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiWW91IGV0IGFsLiAoMjAyMCkgc2hvd2VkIHdpbm5pbmcgdGlja2V0IG1hc2tzIHN0YWJpbGl6ZSB2ZXJ5IGVhcmx5IGluIHRyYWluaW5nIOKAlCB3aXRoaW4gdGhlIGZpcnN0IDXigJMxMCUgb2YgdG90YWwgZXBvY2hzLiBUaGUgZWFybHkgYmlyZCB0aWNrZXQgaXMgZGV0ZWN0ZWQgdmlhIHRoZSBIYW1taW5nIGRpc3RhbmNlIGJldHdlZW4gY29uc2VjdXRpdmUgZXBvY2ggbWFza3M6IHdoZW4gdGhlIG1hc2sgY2hhbmdlIHJhdGUgZHJvcHMgYmVsb3cgzrUg4omIIDAuMDIsIHRoZSB0aWNrZXQgaGFzIGNyeXN0YWxsaXplZC4gVGhpcyByZWR1Y2VzIHRoZSBjb3N0IG9mIElNUCBieSA04oCTN8OXIHNpbmNlIHlvdSBjYW4gaWRlbnRpZnkgdGhlIG1hc2sgc3RydWN0dXJlIHdpdGhvdXQgdHJhaW5pbmcgdG8gZnVsbCBjb252ZXJnZW5jZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGRldGVjdF9lYXJseV9iaXJkKG1vZGVsLCBYLCB5LCBuX2Vwb2Nocz02MCwgcHJ1bmVfcmF0ZT0wLjUpOlxuICAgIG9wdCA9IHRvcmNoLm9wdGltLkFkYW0obW9kZWwucGFyYW1ldGVycygpLCBscj0xZS0zKVxuICAgIHByZXZfbWFzayA9IE5vbmVcbiAgICBlYXJseV9lcG9jaCA9IE5vbmVcbiAgICBmb3IgZXBvY2ggaW4gcmFuZ2Uobl9lcG9jaHMpOlxuICAgICAgICBubi5Dcm9zc0VudHJvcHlMb3NzKCkobW9kZWwoWCksIHkpLmJhY2t3YXJkKClcbiAgICAgICAgb3B0LnN0ZXAoKTsgb3B0Lnplcm9fZ3JhZCgpXG4gICAgICAgIGFsbF93ID0gdG9yY2guY2F0KFtwLmFicygpLmZsYXR0ZW4oKSBmb3IgbiwgcCBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCkgaWYgXHUwMDI3d2VpZ2h0XHUwMDI3IGluIG5dKVxuICAgICAgICB0aHJlc2ggPSB0b3JjaC5xdWFudGlsZShhbGxfdywgcHJ1bmVfcmF0ZSlcbiAgICAgICAgY3VyX21hc2sgPSB0b3JjaC5jYXQoWyhwLmFicygpIFx1MDAzZSB0aHJlc2gpLmZsb2F0KCkuZmxhdHRlbigpXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmb3IgbiwgcCBpbiBtb2RlbC5uYW1lZF9wYXJhbWV0ZXJzKCkgaWYgXHUwMDI3d2VpZ2h0XHUwMDI3IGluIG5dKVxuICAgICAgICBpZiBwcmV2X21hc2sgaXMgbm90IE5vbmU6XG4gICAgICAgICAgICBjaGFuZ2UgPSAoY3VyX21hc2sgIT0gcHJldl9tYXNrKS5mbG9hdCgpLm1lYW4oKS5pdGVtKClcbiAgICAgICAgICAgIGlmIGNoYW5nZSBcdTAwM2MgMC4wMiBhbmQgZWFybHlfZXBvY2ggaXMgTm9uZTpcbiAgICAgICAgICAgICAgICBlYXJseV9lcG9jaCA9IGVwb2NoXG4gICAgICAgICAgICBpZiBlcG9jaCAlIDEwID09IDA6XG4gICAgICAgICAgICAgICAgcHJpbnQoZlx1MDAyN0Vwb2NoIHtlcG9jaDozZH06IG1hc2sgY2hhbmdlID0ge2NoYW5nZTouNGZ9XHUwMDI3KVxuICAgICAgICBwcmV2X21hc2sgPSBjdXJfbWFza1xuICAgIHByaW50KGZcdTAwMjdFYXJseSBiaXJkIGF0IGVwb2NoOiB7ZWFybHlfZXBvY2h9XHUwMDI3KVxuICAgIHJldHVybiBlYXJseV9lcG9jaFxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuZnJvbSBza2xlYXJuLmRhdGFzZXRzIGltcG9ydCBtYWtlX2NsYXNzaWZpY2F0aW9uXG5YX25wLCB5X25wID0gbWFrZV9jbGFzc2lmaWNhdGlvbig2MDAsIDIwLCByYW5kb21fc3RhdGU9MClcblggPSB0b3JjaC50ZW5zb3IoWF9ucCwgZHR5cGU9dG9yY2guZmxvYXQzMilcbnkgPSB0b3JjaC50ZW5zb3IoeV9ucCwgZHR5cGU9dG9yY2gubG9uZylcbm1vZGVsID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMjAsNjQpLCBubi5SZUxVKCksIG5uLkxpbmVhcig2NCwzMiksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDMyLDIpKVxuZGV0ZWN0X2Vhcmx5X2JpcmQobW9kZWwsIFgsIHkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTG90dGVyeSBUaWNrZXQgVHJhbnNmZXIgQWNyb3NzIFRhc2tzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNb3Jjb3MgZXQgYWwuICgyMDE5KSBzaG93ZWQgdGlja2V0cyBmb3VuZCBvbiBhIHNvdXJjZSB0YXNrIG9mdGVuIHRyYW5zZmVyIHRvIHJlbGF0ZWQgdGFyZ2V0IHRhc2tzLiBUaWNrZXRzIGZyb20gbGFyZ2VyIGRhdGFzZXRzIGFyZSBtb3JlIHRyYW5zZmVyYWJsZSDigJQgY29ubmVjdGluZyB0byB0aGUgcHJlLXRyYWluaW5nIHBhcmFkaWdtLiBBIHRpY2tldCBmb3VuZCBkdXJpbmcgcHJlLXRyYWluaW5nIG1heSBhbHJlYWR5IGJlIGEgZ29vZCB0aWNrZXQgZm9yIGRvd25zdHJlYW0gdGFza3MsIGVuYWJsaW5nIGVmZmljaWVudCBzcGFyc2UgZmluZS10dW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHNrbGVhcm4uZGF0YXNldHMgaW1wb3J0IG1ha2VfY2xhc3NpZmljYXRpb25cblxuZGVmIGdldF9kYXRhKG5fY2xhc3Nlcywgc2VlZCk6XG4gICAgWCwgeSA9IG1ha2VfY2xhc3NpZmljYXRpb24oODAwLCAzMCwgbl9jbGFzc2VzPW5fY2xhc3Nlcywgbl9pbmZvcm1hdGl2ZT0xNSwgcmFuZG9tX3N0YXRlPXNlZWQpXG4gICAgWCA9IHRvcmNoLnRlbnNvcihYLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuICAgIHkgPSB0b3JjaC50ZW5zb3IoeSwgZHR5cGU9dG9yY2gubG9uZylcbiAgICByZXR1cm4gWFs6NjAwXSwgeVs6NjAwXSwgWFs2MDA6XSwgeVs2MDA6XVxuXG5kZWYgZ2V0X21hc2soWF90ciwgeV90ciwgbl9jbHMsIHBydW5lX3JhdGU9MC43LCBlcG9jaHM9ODAsIHNlZWQ9MCk6XG4gICAgdG9yY2gubWFudWFsX3NlZWQoc2VlZClcbiAgICBtb2RlbCA9IG5uLlNlcXVlbnRpYWwobm4uTGluZWFyKDMwLDEyOCksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDEyOCw2NCksIG5uLlJlTFUoKSwgbm4uTGluZWFyKDY0LG5fY2xzKSlcbiAgICBvcHQgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsLnBhcmFtZXRlcnMoKSwgbHI9MWUtMylcbiAgICBmb3IgXyBpbiByYW5nZShlcG9jaHMpOlxuICAgICAgICBubi5Dcm9zc0VudHJvcHlMb3NzKCkobW9kZWwoWF90ciksIHlfdHIpLmJhY2t3YXJkKCk7IG9wdC5zdGVwKCk7IG9wdC56ZXJvX2dyYWQoKVxuICAgIGFsbF93ID0gdG9yY2guY2F0KFtwLmFicygpLmZsYXR0ZW4oKSBmb3IgbixwIGluIG1vZGVsLm5hbWVkX3BhcmFtZXRlcnMoKSBpZiBcdTAwMjd3ZWlnaHRcdTAwMjcgaW4gbl0pXG4gICAgdGhyZXNoID0gdG9yY2gucXVhbnRpbGUoYWxsX3csIHBydW5lX3JhdGUpXG4gICAgcmV0dXJuIHtuOiAocC5hYnMoKSBcdTAwM2UgdGhyZXNoKS5mbG9hdCgpIGZvciBuLHAgaW4gbW9kZWwubmFtZWRfcGFyYW1ldGVycygpIGlmIFx1MDAyN3dlaWdodFx1MDAyNyBpbiBufVxuXG5YX3RyMSwgeV90cjEsIF8sIF8gPSBnZXRfZGF0YSgzLCAwKVxuWF90cjIsIHlfdHIyLCBYX3RlMiwgeV90ZTIgPSBnZXRfZGF0YSg0LCA5OSlcbm1hc2sgPSBnZXRfbWFzayhYX3RyMSwgeV90cjEsIG5fY2xzPTMpXG5zcGFyc2l0eSA9IDEgLSBzdW0oKG1cdTAwM2UwKS5zdW0oKS5pdGVtKCkgZm9yIG0gaW4gbWFzay52YWx1ZXMoKSkgLyBzdW0obS5udW1lbCgpIGZvciBtIGluIG1hc2sudmFsdWVzKCkpXG5wcmludChmXHUwMDI3VGFzay0xIHRpY2tldCBzcGFyc2l0eToge3NwYXJzaXR5Oi4xJX1cdTAwMjcpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDQyKVxubW9kZWwyID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMzAsMTI4KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoMTI4LDY0KSwgbm4uUmVMVSgpLCBubi5MaW5lYXIoNjQsNCkpXG5mb3IgbiwgcCBpbiBtb2RlbDIubmFtZWRfcGFyYW1ldGVycygpOlxuICAgIGlmIG4gaW4gbWFzazogcC5kYXRhLm11bF8obWFza1tuXSlcbm9wdDIgPSB0b3JjaC5vcHRpbS5BZGFtKG1vZGVsMi5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5mb3IgXyBpbiByYW5nZSg4MCk6XG4gICAgbm4uQ3Jvc3NFbnRyb3B5TG9zcygpKG1vZGVsMihYX3RyMiksIHlfdHIyKS5iYWNrd2FyZCgpOyBvcHQyLnN0ZXAoKTsgb3B0Mi56ZXJvX2dyYWQoKVxud2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgYWNjID0gKG1vZGVsMihYX3RlMikuYXJnbWF4KDEpID09IHlfdGUyKS5mbG9hdCgpLm1lYW4oKS5pdGVtKClcbnByaW50KGZcdTAwMjdUYXNrLTIgYWNjdXJhY3kgd2l0aCB0YXNrLTEgdGlja2V0OiB7YWNjOi40Zn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29ubmVjdGlvbiB0byBOQVMgYW5kIFN0cm9uZyBMb3R0ZXJ5IFRpY2tldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHN0cm9uZyBsb3R0ZXJ5IHRpY2tldCBoeXBvdGhlc2lzIChaaG91IGV0IGFsLiAyMDE5KSBzaG93cyB0aGF0IHJhbmRvbSB3ZWlnaHRzIHdpdGggdGhlIHJpZ2h0IGJpbmFyeSBtYXNrIGFscmVhZHkgcGVyZm9ybSB3ZWxsIOKAlCBldmVuIHdpdGhvdXQgb3B0aW1pemluZyBmcm9tIM644oKALiBUaGlzIG1lYW5zIHRoZSBtYXNrIHN0cnVjdHVyZSBpcyB0aGUgcHJpbWFyeSBzb3VyY2Ugb2YgaW5kdWN0aXZlIGJpYXMuIFRoaXMgY29ubmVjdHMgdG8gTmV1cmFsIEFyY2hpdGVjdHVyZSBTZWFyY2ggKE5BUyk6IGZpbmRpbmcgdGhlIHdpbm5pbmcgdGlja2V0IHN0cnVjdHVyZSBpcyBlcXVpdmFsZW50IHRvIGEgYmluYXJ5IE5BUyBwcm9ibGVtLiBPbmUtc2hvdCBOQVMgbWV0aG9kcyAoREFSVFMsIFNNQVNIKSB0cmFpbiBhIHN1cGVybmV0d29yayBhbmQgZXh0cmFjdCB0aGUgYmVzdCBzdWJuZXR3b3JrIOKAlCBjb25jZXB0dWFsbHkgaWRlbnRpY2FsIHRvIElNUC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxhdGVyIHdvcmsgc2hvd2VkIHRoYXQgcmV3aW5kaW5nIHRvIGFuIGVhcmx5IChidXQgbm90IGluaXRpYWwpIGNoZWNrcG9pbnQg4oCUIGFmdGVyIGEgZmV3IGh1bmRyZWQgc3RlcHMgb2Ygd2FybXVwIOKAlCB3b3JrcyBldmVuIGZvciBsYXJnZS1zY2FsZSBtb2RlbHMgd2hlcmUgc3RlcC16ZXJvIHJld2luZCBmYWlscy4gVGhpcyB3YXJtIHJld2luZCB2YXJpYW50IGlzIG5lY2Vzc2FyeSBmb3IgUmVzTmV0cyBhbmQgVHJhbnNmb3JtZXJzIGF0IEltYWdlTmV0IHNjYWxlLiBUaGUgZWZmZWN0aXZlIHJld2luZCBwb2ludCBpcyBhIGh5cGVycGFyYW1ldGVyIHR1bmVkIGJhc2VkIG9uIG1vZGVsIHNpemUgYW5kIGRhdGFzZXQgY29tcGxleGl0eS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcnVuaW5nIE1ldGhvZHMgQ29tcGFyaXNvbiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiUmV3aW5kIGlzIEVzc2VudGlhbCIsImNvbnRlbnQiOiJUaGUgY3JpdGljYWwgZmluZGluZyBvZiBGcmFua2xlIFx1MDAyNiBDYXJsaW4gaXMgdGhhdCB0cmFpbmluZyB0aGUgc3BhcnNlIHN1Ym5ldHdvcmsgZnJvbSBhIG5ldyByYW5kb20gaW5pdGlhbGl6YXRpb24gZmFpbHMgdG8gbWF0Y2ggdGhlIGZ1bGwgbmV0d29yay4gVGhlIHdpbm5pbmcgdGlja2V0IHByb3BlcnR5IHJlcXVpcmVzIGJvdGggdGhlIG1hc2sgc3RydWN0dXJlIEFORCB0aGUgb3JpZ2luYWwgaW5pdGlhbGl6YXRpb24gzrjigoAuIFJlc2V0dGluZyB0byDOuOKCgCBpcyBub24tbmVnb3RpYWJsZSDigJQgaXQgZGlzdGluZ3Vpc2hlcyBJTVAgZnJvbSBvcmRpbmFyeSBwcnVuaW5nLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJNZXRob2QiLCJXaW5uaW5nIHRpY2tldCIsIlJld2luZCB0byDOuOKCgCIsIkFjY3VyYWN5IHJlY292ZXJ5IiwiR1BVIHNwZWVkdXAiXSwicm93cyI6W1siSU1QIC8gTG90dGVyeSB0aWNrZXQiLCJZZXMiLCJZZXMg4oCUIGVzc2VudGlhbCIsIkZ1bGwgbWF0Y2ggYXQgNjDigJM5MCUgc3BhcnNpdHkiLCJOZWVkcyBzcGFyc2Uga2VybmVsczsgbGltaXRlZCBvbiBjdXJyZW50IEdQVXMiXSxbIk9uZS1zaG90IG1hZ25pdHVkZSIsIlBhcnRpYWwiLCJObyDigJQgcHJ1bmUgYWZ0ZXIgdHJhaW5pbmcgb25jZSIsIkdvb2QgYXQgNTAlLCBkZWdyYWRlcyBwYXN0IDgwJSIsIkRpcmVjdCBpZiBzcGFyc2Ugb3BzIGF2YWlsYWJsZSJdLFsiTW92ZW1lbnQgcHJ1bmluZyIsIlBhcnRpYWwiLCJObyIsIkJldHRlciB0aGFuIG1hZ25pdHVkZSBmb3IgZmluZS10dW5pbmciLCJMaW1pdGVkIOKAlCB1bnN0cnVjdHVyZWQgc3BhcnNpdHkiXSxbIlN0cnVjdHVyZWQgKGNoYW5uZWwpIHBydW5pbmciLCJObyIsIk5vIiwiUmVjb3ZlcmFibGUgd2l0aCByZXRyYWluaW5nIGF0IDUwJSIsIkRpcmVjdCAy4oCTNMOXIG9uIHN0YW5kYXJkIGhhcmR3YXJlIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIldpbm5pbmcgdGlja2V0cyBhdCA5MCUgc3BhcnNpdHkgb24gTU5JU1QsIDYw4oCTNzAlIG9uIENJRkFSLTEwIG1hdGNoIHRoZSBmdWxsIG5ldHdvcmsuIiwiVGhlIHJld2luZCBzdGVwIChyZXNldHRpbmcgdG8gzrjigoApIGlzIHdoYXQgZGlzdGluZ3Vpc2hlcyBJTVAgZnJvbSBvcmRpbmFyeSBwcnVuaW5nLiIsIkVhcmx5IGJpcmQgdGlja2V0cyByZWR1Y2UgSU1QIGNvc3QgYnkgNOKAkzfDlyBieSBkZXRlY3RpbmcgbWFzayBzdGFiaWxpdHkgd2l0aGluIDXigJMxMCUgb2YgdHJhaW5pbmcuIiwiU3Ryb25nIGxvdHRlcnkgdGlja2V0OiBldmVuIHJhbmRvbSB3ZWlnaHRzIHdpdGggdGhlIHJpZ2h0IGJpbmFyeSBtYXNrIHBlcmZvcm0gd2VsbCAoc3RydWN0dXJlIFx1MDAzZSB2YWx1ZXMpLiIsIlRyYW5zZmVyIHRpY2tldHM6IG1hc2tzIGZyb20gbGFyZ2UgZGF0YXNldHMgdHJhbnNmZXIgdG8gc21hbGxlciB0YXNrcywgZW5hYmxpbmcgZWZmaWNpZW50IHNwYXJzZSBmaW5lLXR1bmluZy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Lottery Ticket Hypothesis — Winning Tickets and IMP

The Lottery Ticket Hypothesis (Frankle & Carlin 2019) states: a randomly initialized dense neural network contains a sparse subnetwork — a winning ticket — that, when trained in isolation from its original initialization, can match the full network's test accuracy within the same training budget. Finding winning tickets requires Iterative Magnitude Pruning (IMP) with the critical step of rewinding to the original initialization.

This is remarkable: the full network's expressivity is not necessary for good generalization. The hypothesis reframes pruning from post-training compression to pre-training architecture search. The winning ticket is not the pruned network after training — it is the sparse subnetwork that, when initialized to its original values and trained from scratch (but with the mask), achieves the same accuracy.

## Iterative Magnitude Pruning (IMP)

IMP consists of four steps repeated k times: (1) Train the full network to convergence from initialization θ₀. (2) Prune p% of remaining weights globally by magnitude. (3) Reset remaining weights to θ₀ — the rewind step. (4) Repeat with the pruned, rewound network. Each round prunes p% of remaining weights, so after k rounds the sparsity is 1−(1−p)^k. Pruning 20% per round for 10 rounds achieves ~89% sparsity. The mask defines the winning ticket structure.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import copy

class IMP:
    def __init__(self, model):
        self.model = model
        self.theta0 = copy.deepcopy(model.state_dict())
        self.masks = {n: torch.ones_like(p)
                      for n, p in model.named_parameters() if 'weight' in n}

    def train_step(self, x, y, optimizer, criterion):
        optimizer.zero_grad()
        loss = criterion(self.model(x), y)
        loss.backward()
        for n, p in self.model.named_parameters():
            if n in self.masks and p.grad is not None:
                p.grad.data.mul_(self.masks[n])
        optimizer.step()
        return loss.item()

    def prune(self, prune_rate=0.2):
        all_w = torch.cat([p.abs().flatten() for n, p in self.model.named_parameters()
                           if n in self.masks])
        thresh = torch.quantile(all_w, prune_rate)
        for n, p in self.model.named_parameters():
            if n in self.masks:
                self.masks[n] = (p.data.abs() > thresh).float()

    def rewind(self):
        self.model.load_state_dict(copy.deepcopy(self.theta0))
        with torch.no_grad():
            for n, p in self.model.named_parameters():
                if n in self.masks: p.data.mul_(self.masks[n])

    def sparsity(self):
        total = sum(m.numel() for m in self.masks.values())
        active = sum(m.sum().item() for m in self.masks.values())
        return 1.0 - active / total

print('IMP: train_step, prune, rewind, sparsity ready.')
```

## Winning Ticket vs Random Sparse Mask

The winning ticket property depends on both the mask structure AND the specific initialization θ₀. To verify: compare (A) winning ticket — IMP mask + rewind to θ₀, (B) random sparse mask — same sparsity but randomly chosen connections, also initialized from θ₀. If the hypothesis holds, (A) significantly outperforms (B) at the same sparsity level.

```python
import torch
import torch.nn as nn
import copy
from sklearn.datasets import make_classification

def simple_net(seed=0):
    torch.manual_seed(seed)
    return nn.Sequential(nn.Linear(20,64), nn.ReLU(), nn.Linear(64,64), nn.ReLU(), nn.Linear(64,2))

def train_eval(model, X_tr, y_tr, X_te, y_te, mask=None, n_epochs=80):
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    for _ in range(n_epochs):
        opt.zero_grad()
        loss = nn.CrossEntropyLoss()(model(X_tr), y_tr)
        loss.backward()
        if mask:
            for n, p in model.named_parameters():
                if n in mask and p.grad is not None: p.grad.data.mul_(mask[n])
        opt.step()
    with torch.no_grad():
        return (model(X_te).argmax(1) == y_te).float().mean().item()

X_np, y_np = make_classification(800, 20, n_classes=2, random_state=0)
X = torch.tensor(X_np, dtype=torch.float32)
y = torch.tensor(y_np, dtype=torch.long)
X_tr, y_tr, X_te, y_te = X[:600], y[:600], X[600:], y[600:]

full = simple_net(0)
acc_full = train_eval(full, X_tr, y_tr, X_te, y_te)
print(f'Full network: {acc_full:.4f}')

wt_mask = {n: (p.abs() > p.abs().quantile(0.5)).float() for n, p in full.named_parameters() if 'weight' in n}
wt = simple_net(0)
for n, p in wt.named_parameters():
    if n in wt_mask: p.data.mul_(wt_mask[n])
print(f'Winning ticket (50% sparse): {train_eval(wt, X_tr, y_tr, X_te, y_te, wt_mask):.4f}')

rand_mask = {n: (torch.rand_like(p) > 0.5).float() for n, p in full.named_parameters() if 'weight' in n}
rand = simple_net(0)
for n, p in rand.named_parameters():
    if n in rand_mask: p.data.mul_(rand_mask[n])
print(f'Random sparse  (50% sparse): {train_eval(rand, X_tr, y_tr, X_te, y_te, rand_mask):.4f}')
```

## Early Bird Tickets

You et al. (2020) showed winning ticket masks stabilize very early in training — within the first 5–10% of total epochs. The early bird ticket is detected via the Hamming distance between consecutive epoch masks: when the mask change rate drops below ε ≈ 0.02, the ticket has crystallized. This reduces the cost of IMP by 4–7× since you can identify the mask structure without training to full convergence.

```python
import torch
import torch.nn as nn

def detect_early_bird(model, X, y, n_epochs=60, prune_rate=0.5):
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    prev_mask = None
    early_epoch = None
    for epoch in range(n_epochs):
        nn.CrossEntropyLoss()(model(X), y).backward()
        opt.step(); opt.zero_grad()
        all_w = torch.cat([p.abs().flatten() for n, p in model.named_parameters() if 'weight' in n])
        thresh = torch.quantile(all_w, prune_rate)
        cur_mask = torch.cat([(p.abs() > thresh).float().flatten()
                              for n, p in model.named_parameters() if 'weight' in n])
        if prev_mask is not None:
            change = (cur_mask != prev_mask).float().mean().item()
            if change < 0.02 and early_epoch is None:
                early_epoch = epoch
            if epoch % 10 == 0:
                print(f'Epoch {epoch:3d}: mask change = {change:.4f}')
        prev_mask = cur_mask
    print(f'Early bird at epoch: {early_epoch}')
    return early_epoch

torch.manual_seed(0)
from sklearn.datasets import make_classification
X_np, y_np = make_classification(600, 20, random_state=0)
X = torch.tensor(X_np, dtype=torch.float32)
y = torch.tensor(y_np, dtype=torch.long)
model = nn.Sequential(nn.Linear(20,64), nn.ReLU(), nn.Linear(64,32), nn.ReLU(), nn.Linear(32,2))
detect_early_bird(model, X, y)
```

## Lottery Ticket Transfer Across Tasks

Morcos et al. (2019) showed tickets found on a source task often transfer to related target tasks. Tickets from larger datasets are more transferable — connecting to the pre-training paradigm. A ticket found during pre-training may already be a good ticket for downstream tasks, enabling efficient sparse fine-tuning.

```python
import torch
import torch.nn as nn
from sklearn.datasets import make_classification

def get_data(n_classes, seed):
    X, y = make_classification(800, 30, n_classes=n_classes, n_informative=15, random_state=seed)
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.long)
    return X[:600], y[:600], X[600:], y[600:]

def get_mask(X_tr, y_tr, n_cls, prune_rate=0.7, epochs=80, seed=0):
    torch.manual_seed(seed)
    model = nn.Sequential(nn.Linear(30,128), nn.ReLU(), nn.Linear(128,64), nn.ReLU(), nn.Linear(64,n_cls))
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    for _ in range(epochs):
        nn.CrossEntropyLoss()(model(X_tr), y_tr).backward(); opt.step(); opt.zero_grad()
    all_w = torch.cat([p.abs().flatten() for n,p in model.named_parameters() if 'weight' in n])
    thresh = torch.quantile(all_w, prune_rate)
    return {n: (p.abs() > thresh).float() for n,p in model.named_parameters() if 'weight' in n}

X_tr1, y_tr1, _, _ = get_data(3, 0)
X_tr2, y_tr2, X_te2, y_te2 = get_data(4, 99)
mask = get_mask(X_tr1, y_tr1, n_cls=3)
sparsity = 1 - sum((m>0).sum().item() for m in mask.values()) / sum(m.numel() for m in mask.values())
print(f'Task-1 ticket sparsity: {sparsity:.1%}')

torch.manual_seed(42)
model2 = nn.Sequential(nn.Linear(30,128), nn.ReLU(), nn.Linear(128,64), nn.ReLU(), nn.Linear(64,4))
for n, p in model2.named_parameters():
    if n in mask: p.data.mul_(mask[n])
opt2 = torch.optim.Adam(model2.parameters(), lr=1e-3)
for _ in range(80):
    nn.CrossEntropyLoss()(model2(X_tr2), y_tr2).backward(); opt2.step(); opt2.zero_grad()
with torch.no_grad():
    acc = (model2(X_te2).argmax(1) == y_te2).float().mean().item()
print(f'Task-2 accuracy with task-1 ticket: {acc:.4f}')
```

## Connection to NAS and Strong Lottery Ticket

The strong lottery ticket hypothesis (Zhou et al. 2019) shows that random weights with the right binary mask already perform well — even without optimizing from θ₀. This means the mask structure is the primary source of inductive bias. This connects to Neural Architecture Search (NAS): finding the winning ticket structure is equivalent to a binary NAS problem. One-shot NAS methods (DARTS, SMASH) train a supernetwork and extract the best subnetwork — conceptually identical to IMP.

Later work showed that rewinding to an early (but not initial) checkpoint — after a few hundred steps of warmup — works even for large-scale models where step-zero rewind fails. This warm rewind variant is necessary for ResNets and Transformers at ImageNet scale. The effective rewind point is a hyperparameter tuned based on model size and dataset complexity.

## Pruning Methods Comparison

> **Rewind is Essential**: The critical finding of Frankle & Carlin is that training the sparse subnetwork from a new random initialization fails to match the full network. The winning ticket property requires both the mask structure AND the original initialization θ₀. Resetting to θ₀ is non-negotiable — it distinguishes IMP from ordinary pruning.

| Method | Winning ticket | Rewind to θ₀ | Accuracy recovery | GPU speedup |
| --- | --- | --- | --- | --- |
| IMP / Lottery ticket | Yes | Yes — essential | Full match at 60–90% sparsity | Needs sparse kernels; limited on current GPUs |
| One-shot magnitude | Partial | No — prune after training once | Good at 50%, degrades past 80% | Direct if sparse ops available |
| Movement pruning | Partial | No | Better than magnitude for fine-tuning | Limited — unstructured sparsity |
| Structured (channel) pruning | No | No | Recoverable with retraining at 50% | Direct 2–4× on standard hardware |

- Winning tickets at 90% sparsity on MNIST, 60–70% on CIFAR-10 match the full network.
- The rewind step (resetting to θ₀) is what distinguishes IMP from ordinary pruning.
- Early bird tickets reduce IMP cost by 4–7× by detecting mask stability within 5–10% of training.
- Strong lottery ticket: even random weights with the right binary mask perform well (structure > values).
- Transfer tickets: masks from large datasets transfer to smaller tasks, enabling efficient sparse fine-tuning.

---

