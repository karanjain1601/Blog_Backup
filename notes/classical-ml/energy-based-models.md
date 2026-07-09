---
title: "Energy-Based Models — Boltzmann Distribution and MCMC"
slug: "energy-based-models"
description: "Understand energy-based models for anomaly detection: the Boltzmann distribution p(x)=exp(−E_θ(x))/Z, contrastive divergence training, Langevin dynamics MCMC for the negative phase, and score matching as an MCMC-free alternative to avoid the intractable partition function."
tags: ["anomaly-detection", "density-estimation", "classical-ml"]
topic: "classical-ml"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW5lcmd5LWJhc2VkIG1vZGVscyAoRUJNcykgZGVmaW5lIGEgcHJvYmFiaWxpdHkgZGlzdHJpYnV0aW9uIHZpYSBhbiBlbmVyZ3kgZnVuY3Rpb246IHBfzrgoeCkgPSBleHAo4oiSRV/OuCh4KSkgLyBaKM64KSB3aGVyZSBaKM64KSA9IOKIqyBleHAo4oiSRV/OuCh4KSkgZHggaXMgdGhlIHBhcnRpdGlvbiBmdW5jdGlvbi4gVGhlIGVuZXJneSBFX864IGlzIHBhcmFtZXRlcmlzZWQgYnkgYSBuZXVyYWwgbmV0d29yayBhbmQgY2FuIHRha2UgYW55IHZhbHVlIOKAlCBubyBhcmNoaXRlY3R1cmFsIGNvbnN0cmFpbnRzIGxpa2UgaW52ZXJ0aWJpbGl0eSBhcmUgcmVxdWlyZWQuIFRoZSBrZXkgY2hhbGxlbmdlIGlzIHRoYXQgWiBpcyBnZW5lcmFsbHkgaW50cmFjdGFibGUsIGNvbXBsaWNhdGluZyBib3RoIHRyYWluaW5nIGFuZCBub3JtYWxpc2VkLXByb2JhYmlsaXR5IGNvbXB1dGF0aW9uLiBGb3IgYW5vbWFseSBkZXRlY3Rpb24gdGhpcyBpcyBub3QgYSBmdW5kYW1lbnRhbCBiYXJyaWVyOiBsb3cgZW5lcmd5IOKGlCBub3JtYWwsIGhpZ2ggZW5lcmd5IOKGlCBhbm9tYWx5LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVuZXJneSBGdW5jdGlvbnMgYW5kIHRoZSBCb2x0em1hbm4gRGlzdHJpYnV0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQm9sdHptYW5uIGRpc3RyaWJ1dGlvbiBhc3NpZ25zIGhpZ2ggcHJvYmFiaWxpdHkgdG8gcmVnaW9ucyBvZiBsb3cgZW5lcmd5IGFuZCBsb3cgcHJvYmFiaWxpdHkgdG8gaGlnaC1lbmVyZ3kgcmVnaW9ucy4gRHVyaW5nIHRyYWluaW5nIHdlIHdhbnQgdGhlIG1vZGVsIHRvIGFzc2lnbiBsb3cgZW5lcmd5IHRvIHRyYWluaW5nIGRhdGEgKHBvc2l0aXZlIHBoYXNlKSBhbmQgaGlnaCBlbmVyZ3kgdG8gb3RoZXIgcmVnaW9ucyAobmVnYXRpdmUgcGhhc2UpLiBUaGUgbG9nLWxpa2VsaWhvb2QgZ3JhZGllbnQgaXM6IOKIgi/iiILOuCBsb2cgcF/OuCh4KSA9IOKIkuKIgkVfzrgoeCkv4oiCzrggKyBFX3twX864fVviiIJFX864L+KIgs64XS4gVGhlIGZpcnN0IHRlcm0gcHVzaGVzIGRvd24gZW5lcmd5IGF0IG9ic2VydmVkIGRhdGE7IHRoZSBzZWNvbmQgdGVybSAodGhlIG5lZ2F0aXZlIHBoYXNlKSBwdXNoZXMgZW5lcmd5IHVwIGF0IHNhbXBsZXMgZnJvbSB0aGUgY3VycmVudCBtb2RlbCDigJQgcmVxdWlyaW5nIE1DTUMgc2FtcGxpbmcuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJVbm5vcm1hbGlzZWQgZGVuc2l0eTogcF/OuCh4KSDiiJ0gZXhwKOKIkkVfzrgoeCkpIOKAlCBvbmx5IHRoZSBlbmVyZ3kgZnVuY3Rpb24gbmVlZHMgdG8gYmUgbGVhcm5lZC4iLCJQYXJ0aXRpb24gZnVuY3Rpb24gWijOuCkgPSDiiKtleHAo4oiSRV/OuClkeCDigJQgaW50cmFjdGFibGUgaW4gZ2VuZXJhbDsgbWFrZXMgTUxFIGdyYWRpZW50IGhhcmQgdG8gY29tcHV0ZS4iLCJOZWdhdGl2ZSBwaGFzZTogRV97cF/OuH1b4oiCRS/iiILOuF0g4oCUIGV4cGVjdGF0aW9uIHVuZGVyIHRoZSBtb2RlbDsgYXBwcm94aW1hdGVkIGJ5IE1DTUMgc2FtcGxlcy4iLCJDb250cmFzdGl2ZSBkaXZlcmdlbmNlOiBhcHByb3hpbWF0ZSBuZWdhdGl2ZSBwaGFzZSB1c2luZyBzaG9ydCBNQ01DIGNoYWlucyBpbml0aWFsaXNlZCBhdCB0cmFpbmluZyBkYXRhLiIsIlNjb3JlIG1hdGNoaW5nOiBzaWRlc3RlcCBaIGJ5IG1hdGNoaW5nIHNjb3JlIGZ1bmN0aW9ucyDiiIdfeCBsb2cgcCDigJQgYXZvaWRzIE1DTUMgZW50aXJlbHkuIl19LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmNsYXNzIEVuZXJneU5ldChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBkX2luKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkxpbmVhcihkX2luLCA2NCksIG5uLlNpTFUoKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcig2NCwgNjQpLCBubi5TaUxVKCksXG4gICAgICAgICAgICBubi5MaW5lYXIoNjQsIDEpKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5uZXQoeCkuc3F1ZWV6ZSgtMSkgICMgc2NhbGFyIGVuZXJneSBwZXIgc2FtcGxlXG5cbmRlZiBjb250cmFzdGl2ZV9kaXZlcmdlbmNlX3N0ZXAoZWJtLCB4X3Bvcywgb3B0LCBuX3N0ZXBzPTEwLCBzdGVwX3NpemU9MC4wMSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3T25lIENELWsgdHJhaW5pbmcgc3RlcDogcG9zaXRpdmUgcGhhc2UgbWludXMgbmVnYXRpdmUgcGhhc2UuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZWJtLnRyYWluKClcbiAgICAjIE5lZ2F0aXZlIHBoYXNlOiBydW4gc2hvcnQgTGFuZ2V2aW4gY2hhaW4gZnJvbSBwb3NpdGl2ZSBzYW1wbGVzXG4gICAgeF9uZWcgPSB4X3Bvcy5kZXRhY2goKS5jbG9uZSgpLnJlcXVpcmVzX2dyYWRfKFRydWUpXG4gICAgZm9yIF8gaW4gcmFuZ2Uobl9zdGVwcyk6XG4gICAgICAgIGVfbmVnID0gZWJtKHhfbmVnKVxuICAgICAgICBncmFkID0gdG9yY2guYXV0b2dyYWQuZ3JhZChlX25lZy5zdW0oKSwgeF9uZWcpWzBdXG4gICAgICAgIHhfbmVnID0gKHhfbmVnIC0gc3RlcF9zaXplICogZ3JhZCArXG4gICAgICAgICAgICAgICAgICgyICogc3RlcF9zaXplKSAqKiAwLjUgKiB0b3JjaC5yYW5kbl9saWtlKHhfbmVnKSkuZGV0YWNoKClcbiAgICAgICAgeF9uZWcucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICB4X25lZyA9IHhfbmVnLmRldGFjaCgpXG4gICAgb3B0Lnplcm9fZ3JhZCgpXG4gICAgbG9zcyA9IGVibSh4X3BvcykubWVhbigpIC0gZWJtKHhfbmVnKS5tZWFuKCkgICMgbWluIEUocG9zKSwgbWF4IEUobmVnKVxuICAgIGxvc3MuYmFja3dhcmQoKTsgb3B0LnN0ZXAoKVxuICAgIHJldHVybiBsb3NzLml0ZW0oKVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuWF90ciA9IHRvcmNoLnRlbnNvcihucC5yYW5kb20ucmFuZG4oNjAwLCA0KSwgZHR5cGU9dG9yY2guZmxvYXQzMilcbmVibSA9IEVuZXJneU5ldChkX2luPTQpXG5vcHQgPSB0b3JjaC5vcHRpbS5BZGFtKGVibS5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5mb3IgZXAgaW4gcmFuZ2UoMjApOlxuICAgIGxvc3NfdmFsID0gY29udHJhc3RpdmVfZGl2ZXJnZW5jZV9zdGVwKGVibSwgWF90ciwgb3B0KVxuICAgIGlmIChlcCsxKSAlIDUgPT0gMDpcbiAgICAgICAgcHJpbnQoZlx1MDAyN0Vwb2NoIHtlcCsxOjJkfSB8IENEIGxvc3M6IHtsb3NzX3ZhbDouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIHZpYSBDb250cmFzdGl2ZSBEaXZlcmdlbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDb250cmFzdGl2ZSBEaXZlcmdlbmNlIChDRC1rKSBhcHByb3hpbWF0ZXMgdGhlIG5lZ2F0aXZlIHBoYXNlIHdpdGggayBzdGVwcyBvZiBNQ01DIHN0YXJ0aW5nIGZyb20gdHJhaW5pbmcgZGF0YS4gQ0QtMSAoYSBzaW5nbGUgc3RlcCkgaXMgdGhlIG1vc3QgY29tbW9uIOKAlCBjaGVhcCBidXQgYmlhc2VkLiBQZXJzaXN0ZW50IENEIChQQ0QpIG1haW50YWlucyBhIHBlcnNpc3RlbnQgY2hhaW4gb2YgZmFudGFzeSBwYXJ0aWNsZXMgYWNyb3NzIGJhdGNoZXMsIHdoaWNoIGNvbnZlcmdlcyB0byB0cnVlIG1vZGVsIHNhbXBsZXMgYXMgdHJhaW5pbmcgcHJvZ3Jlc3NlcyBidXQgcmVxdWlyZXMgc3RvcmluZyBhbmQgdXBkYXRpbmcgdGhlIGNoYWluLiBDRC1rIGdyYWRpZW50IHF1YWxpdHkgaW5jcmVhc2VzIHdpdGggayBidXQgc28gZG9lcyBjb21wdXRhdGlvbmFsIGNvc3QuIEZvciBhbm9tYWx5IGRldGVjdGlvbiwgZXhhY3Qgbm9ybWFsaXNhdGlvbiBpcyBub3QgbmVlZGVkIOKAlCByZWxhdGl2ZSBlbmVyZ3kgdmFsdWVzIHN1ZmZpY2UgZm9yIHJhbmtpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGFuZ2V2aW4gRHluYW1pY3MgZm9yIE1DTUMgU2FtcGxpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkxhbmdldmluIGR5bmFtaWNzIHNhbXBsZXMgZnJvbSBwX864KHgpIOKInSBleHAo4oiSRV/OuCh4KSkgYnkgc2ltdWxhdGluZyB0aGUgU0RFOiB44oKc4oKK4oKBID0geOKCnCDiiJIgKM63LzIp4oiHX3ggRV/OuCh44oKcKSArIOKIms63wrfOtSB3aGVyZSDOtX5OKDAsSSkuIFRoZSBncmFkaWVudCB0ZXJtIHB1bGxzIHBhcnRpY2xlcyB0b3dhcmQgbG93LWVuZXJneSByZWdpb25zOyB0aGUgbm9pc2UgdGVybSBlbnN1cmVzIGV4cGxvcmF0aW9uLiBXaXRoIHN0ZXAgc2l6ZSDOt+KGkjAgYW5kIGVub3VnaCBzdGVwcywgc2FtcGxlcyBjb252ZXJnZSB0byBwX864LiBJbiBwcmFjdGljZSwgYSBmaW5pdGUgzrcgaW50cm9kdWNlcyBhIGRpc2NyZXRpc2F0aW9uIGJpYXMgY29ycmVjdGVkIGJ5IGEgTWV0cm9wb2xpcy1IYXN0aW5ncyBhY2NlcHQvcmVqZWN0IHN0ZXAgKE1BTEEpLiBMYW5nZXZpbiBkeW5hbWljcyBpcyB0aGUgc3RhbmRhcmQgbmVnYXRpdmUtcGhhc2Ugc2FtcGxlciBmb3IgZGVlcCBFQk1zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuXG5kZWYgbGFuZ2V2aW5fc2FtcGxlKGVibSwgbl9zYW1wbGVzLCBkLCBuX3N0ZXBzPTEwMCwgc3RlcF9zaXplPTAuMDEsIG5vaXNlX3NjYWxlPTEuMCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3U2FtcGxlIGZyb20gRUJNIHZpYSBMYW5nZXZpbiBNQ01DLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGVibS5ldmFsKClcbiAgICB4ID0gdG9yY2gucmFuZG4obl9zYW1wbGVzLCBkKSAqIG5vaXNlX3NjYWxlXG4gICAgeC5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgIGZvciBpIGluIHJhbmdlKG5fc3RlcHMpOlxuICAgICAgICBlbmVyZ3kgPSBlYm0oeClcbiAgICAgICAgZ3JhZCA9IHRvcmNoLmF1dG9ncmFkLmdyYWQoZW5lcmd5LnN1bSgpLCB4KVswXVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIHggPSB4IC0gMC41ICogc3RlcF9zaXplICogZ3JhZCArIChzdGVwX3NpemUgKiogMC41KSAqIHRvcmNoLnJhbmRuX2xpa2UoeClcbiAgICAgICAgeCA9IHguZGV0YWNoKCkucmVxdWlyZXNfZ3JhZF8oVHJ1ZSlcbiAgICAgICAgaWYgKGkgKyAxKSAlIDI1ID09IDA6XG4gICAgICAgICAgICBlX21lYW4gPSBlYm0oeC5kZXRhY2goKSkubWVhbigpLml0ZW0oKVxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyNyAgU3RlcCB7aSsxOjRkfSB8IG1lYW4gZW5lcmd5OiB7ZV9tZWFuOi40Zn1cdTAwMjcpXG4gICAgcmV0dXJuIHguZGV0YWNoKClcblxucHJpbnQoXHUwMDI3TGFuZ2V2aW4gc2FtcGxpbmcgZnJvbSB0cmFpbmVkIEVCTSAoNEQpOlx1MDAyNylcbnNhbXBsZXMgPSBsYW5nZXZpbl9zYW1wbGUoZWJtLCBuX3NhbXBsZXM9NTAsIGQ9NCwgbl9zdGVwcz0xMDApXG5wcmludChmXHUwMDI3U2FtcGxlIG1lYW46ICB7c2FtcGxlcy5tZWFuKGRpbT0wKS5udW1weSgpLnJvdW5kKDMpfVx1MDAyNylcbnByaW50KGZcdTAwMjdTYW1wbGUgc3RkOiAgIHtzYW1wbGVzLnN0ZChkaW09MCkubnVtcHkoKS5yb3VuZCgzKX1cdTAwMjcpXG5wcmludChmXHUwMDI3RW5lcmd5IG1lYW46ICB7ZWJtKHNhbXBsZXMpLm1lYW4oKS5pdGVtKCk6LjRmfVx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFQk0gQW5vbWFseSBEZXRlY3Rpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkJlY2F1c2UgcF/OuCh4KSDiiJ0gZXhwKOKIkkVfzrgoeCkpLCB0aGUgZW5lcmd5IEVfzrgoeCkgaXMgYSBkaXJlY3QgKHVubm9ybWFsaXNlZCkgYW5vbWFseSBzY29yZTogbG93IGVuZXJneSA9IGhpZ2ggcHJvYmFiaWxpdHkgPSBub3JtYWw7IGhpZ2ggZW5lcmd5ID0gbG93IHByb2JhYmlsaXR5ID0gYW5vbWFseS4gVGhpcyBhdm9pZHMgdGhlIG5lZWQgdG8gY29tcHV0ZSBaLiBUaGUgdGhyZXNob2xkIGlzIHNldCBmcm9tIHRoZSBkaXN0cmlidXRpb24gb2YgZW5lcmdpZXMgb24gbm9ybWFsIHRyYWluaW5nIGRhdGEuIEVCTSBhbm9tYWx5IGRldGVjdGlvbiBpcyByb2J1c3QgdG8gdGhlIGNob2ljZSBvZiBhcmNoaXRlY3R1cmUgYXMgbG9uZyBhcyBFX864IGlzIGZsZXhpYmxlIGVub3VnaCB0byBtb2RlbCB0aGUgbm9ybWFsIG1hbmlmb2xkIOKAlCBhbnkgbmV1cmFsIG5ldHdvcmsgc3VmZmljZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5mcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZVxuXG5ucC5yYW5kb20uc2VlZCg1KVxudG9yY2gubWFudWFsX3NlZWQoNSlcblhfdHJhaW4gPSB0b3JjaC50ZW5zb3IobnAucmFuZG9tLnJhbmRuKDUwMCwgNCksIGR0eXBlPXRvcmNoLmZsb2F0MzIpXG5lYm0yID0gRW5lcmd5TmV0KGRfaW49NClcbm9wdDIgPSB0b3JjaC5vcHRpbS5BZGFtKGVibTIucGFyYW1ldGVycygpLCBscj01ZS00KVxuZm9yIF8gaW4gcmFuZ2UoNTApOlxuICAgIGNvbnRyYXN0aXZlX2RpdmVyZ2VuY2Vfc3RlcChlYm0yLCBYX3RyYWluLCBvcHQyLCBuX3N0ZXBzPTUpXG5cbiMgQW5vbWFseSBkZXRlY3Rpb24gZXZhbHVhdGlvblxuWF9uX3RlID0gdG9yY2gudGVuc29yKG5wLnJhbmRvbS5yYW5kbigxMDAsIDQpLCBkdHlwZT10b3JjaC5mbG9hdDMyKVxuWF9hX3RlID0gdG9yY2gudGVuc29yKG5wLnJhbmRvbS5yYW5kbigyNSwgNCkqMC4yICsgMywgZHR5cGU9dG9yY2guZmxvYXQzMilcblhfYWxsID0gdG9yY2guY2F0KFtYX25fdGUsIFhfYV90ZV0pXG55ID0gbnAuYXJyYXkoWzBdKjEwMCArIFsxXSoyNSlcblxuZWJtMi5ldmFsKClcbndpdGggdG9yY2gubm9fZ3JhZCgpOlxuICAgIGVuZXJneV9zY29yZXMgPSBlYm0yKFhfYWxsKS5udW1weSgpXG5cbnRociA9IG5wLnBlcmNlbnRpbGUoZW5lcmd5X3Njb3Jlc1s6MTAwXSwgOTUpXG5kZXRlY3RlZCA9IChlbmVyZ3lfc2NvcmVzWzEwMDpdIFx1MDAzZSB0aHIpLnN1bSgpXG5hdXJvYyA9IHJvY19hdWNfc2NvcmUoeSwgZW5lcmd5X3Njb3JlcylcbnByaW50KGZcdTAwMjdBVVJPQyAoZW5lcmd5IHNjb3JlKTogICB7YXVyb2M6LjRmfVx1MDAyNylcbnByaW50KGZcdTAwMjdUaHJlc2hvbGQgKDk1dGggcGN0KTogICB7dGhyOi40Zn1cdTAwMjcpXG5wcmludChmXHUwMDI3QW5vbWFsaWVzIGRldGVjdGVkOiAgICAge2RldGVjdGVkfS97bGVuKFhfYV90ZSl9XHUwMDI3KVxucHJpbnQoZlx1MDAyN05vcm1hbCBlbmVyZ3kgbWVhbjogICAgIHtlbmVyZ3lfc2NvcmVzWzoxMDBdLm1lYW4oKTouNGZ9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0Fub21hbHkgZW5lcmd5IG1lYW46ICAgIHtlbmVyZ3lfc2NvcmVzWzEwMDpdLm1lYW4oKTouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiRUJNIHZzIE5vcm1hbGl6aW5nIEZsb3dzIGZvciBBbm9tYWx5IERldGVjdGlvbiIsImNvbnRlbnQiOiJFQk1zIHJlcXVpcmUgb25seSBmb3J3YXJkIHBhc3NlcyB0aHJvdWdoIEVfzrggYXQgaW5mZXJlbmNlIOKAlCBmYXN0IGFuZCBhcmNoaXRlY3R1cmFsbHkgZmxleGlibGUuIEZsb3dzIHJlcXVpcmUgYW4gaW52ZXJ0aWJsZSBhcmNoaXRlY3R1cmUgYW5kIGNhbiBjb21wdXRlIGV4YWN0IGxvZyBwKHgpLiBFQk1zIGFyZSBoYXJkZXIgdG8gdHJhaW4gKE1DTUMgbmVnYXRpdmUgcGhhc2UpIGJ1dCBjYW4gdXNlIGFyYml0cmFyeSBhcmNoaXRlY3R1cmVzIGluY2x1ZGluZyByZXNpZHVhbCBuZXR3b3JrcyB3aXRoIGJhdGNoIG5vcm0uIEZvciBhbm9tYWx5IGRldGVjdGlvbiB3aGVyZSBvbmx5IGEgcmFua2luZyAobm90IGFic29sdXRlIHByb2JhYmlsaXR5KSBpcyBuZWVkZWQsIEVCTSBlbmVyZ3kgc2NvcmVzIGFyZSBvZnRlbiBzdWZmaWNpZW50LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNjb3JlIE1hdGNoaW5nIOKAlCBBdm9pZGluZyB0aGUgUGFydGl0aW9uIEZ1bmN0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJIeXbDpHJpbmVuXHUwMDI3cyBzY29yZSBtYXRjaGluZyBzaWRlc3RlcHMgWiBlbnRpcmVseSBieSBtYXRjaGluZyB0aGUgc2NvcmUgZnVuY3Rpb24g4oiHX3ggbG9nIHBfzrgoeCkgPSDiiJLiiIdfeCBFX864KHgpIHRvIHRoZSBkYXRhIHNjb3JlLiBUaGUgb2JqZWN0aXZlIGlzOiBKKM64KSA9IEVfZGF0YVvigJbiiIdfeCBsb2cgcF/OuCh4KeKAlsKyIC8gMiArIHRyKOKIh194wrIgbG9nIHBfzrgoeCkpXS4gVGhlIGZpcnN0IHRlcm0gaXMgc21hbGwgd2hlbiBtb2RlbCBhbmQgZGF0YSBzY29yZXMgYWdyZWU7IHRoZSBzZWNvbmQgdGVybSAodHJhY2Ugb2YgdGhlIEhlc3NpYW4pIHJlZ3VsYXJpc2VzLiBEZW5vaXNpbmcgc2NvcmUgbWF0Y2hpbmcgKERTTSkgc2ltcGxpZmllcyBjb21wdXRhdGlvbiBieSBtYXRjaGluZyBzY29yZXMgb2Ygbm9pc3kgZGF0YTogSl9EU00gPSBFX3t4LM61fVvigJbiiIdfeCBsb2cgcF/OuCh4K8+DzrUpICsgzrUvz4PigJbCsl0uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBkZW5vaXNpbmdfc2NvcmVfbWF0Y2hpbmdfbG9zcyhlYm0sIHhfY2xlYW4sIHNpZ21hPTAuMSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3RFNNIGxvc3M6IG1hdGNoIGVuZXJneSBncmFkaWVudCB0byBub2lzZSBkaXJlY3Rpb24uXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgbm9pc2UgPSB0b3JjaC5yYW5kbl9saWtlKHhfY2xlYW4pICogc2lnbWFcbiAgICB4X25vaXN5ID0geF9jbGVhbiArIG5vaXNlXG4gICAgeF9ub2lzeS5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgIGVuZXJneSA9IGVibSh4X25vaXN5KVxuICAgIHNjb3JlX21vZGVsID0gLXRvcmNoLmF1dG9ncmFkLmdyYWQoZW5lcmd5LnN1bSgpLCB4X25vaXN5LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyZWF0ZV9ncmFwaD1UcnVlKVswXVxuICAgIHRhcmdldF9zY29yZSA9IC1ub2lzZSAvIChzaWdtYSAqKiAyKVxuICAgIGxvc3MgPSAwLjUgKiAoKHNjb3JlX21vZGVsIC0gdGFyZ2V0X3Njb3JlKSAqKiAyKS5zdW0oZGltPS0xKS5tZWFuKClcbiAgICByZXR1cm4gbG9zc1xuXG50b3JjaC5tYW51YWxfc2VlZCgzKVxuWF9zbSA9IHRvcmNoLnRlbnNvcihucC5yYW5kb20ucmFuZG4oNDAwLCA0KSwgZHR5cGU9dG9yY2guZmxvYXQzMilcbmVibV9zbSA9IEVuZXJneU5ldChkX2luPTQpXG5vcHRfc20gPSB0b3JjaC5vcHRpbS5BZGFtKGVibV9zbS5wYXJhbWV0ZXJzKCksIGxyPTFlLTMpXG5mb3IgZXAgaW4gcmFuZ2UoMzApOlxuICAgIGxvc3MgPSBkZW5vaXNpbmdfc2NvcmVfbWF0Y2hpbmdfbG9zcyhlYm1fc20sIFhfc20sIHNpZ21hPTAuMilcbiAgICBvcHRfc20uemVyb19ncmFkKClcbiAgICBsb3NzLmJhY2t3YXJkKCk7IG9wdF9zbS5zdGVwKClcbiAgICBpZiAoZXAgKyAxKSAlIDEwID09IDA6XG4gICAgICAgIHByaW50KGZcdTAwMjdFcG9jaCB7ZXArMToyZH0gfCBEU00gbG9zczoge2xvc3MuaXRlbSgpOi42Zn1cdTAwMjcpXG5wcmludChcdTAwMjdTY29yZSBtYXRjaGluZyBhdm9pZHMgTUNNQyDigJQgbm8gbmVnYXRpdmUgcGhhc2Ugc2FtcGxpbmcgcmVxdWlyZWQuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVCTSBUcmFpbmluZyBNZXRob2RzIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiVHJhaW5pbmcgTWV0aG9kIiwiTUNNQyBOZWVkZWQiLCJHcmFkaWVudCBRdWFsaXR5IiwiVHJhaW5pbmcgQ29zdCIsIlBhcnRpdGlvbiBGdW5jdGlvbiIsIlByYWN0aWNhbCBVc2UiXSwicm93cyI6W1siQ29udHJhc3RpdmUgRGl2ZXJnZW5jZSAoQ0QtMSkiLCJZZXMgKDEgc3RlcCkiLCJCaWFzZWQgYnV0IGZhc3QiLCJMb3ciLCJJZ25vcmVkIiwiTW9zdCBjb21tb24gYmFzZWxpbmUiXSxbIlBlcnNpc3RlbnQgQ0QgKFBDRCkiLCJZZXMgKHBlcnNpc3RlbnQgY2hhaW4pIiwiQmV0dGVyIOKAlCBjaGFpbiBtaXhlcyIsIk1lZGl1bSIsIklnbm9yZWQiLCJCZXR0ZXIgcXVhbGl0eSB0aGFuIENEIl0sWyJMYW5nZXZpbiBNQ01DIChmdWxsKSIsIlllcyAoMTAwKyBzdGVwcykiLCJHb29kIOKAlCBuZWFyIHRydWUgbW9kZWwiLCJIaWdoIiwiSWdub3JlZCIsIlNsb3cgYnV0IGFjY3VyYXRlIl0sWyJTY29yZSBNYXRjaGluZyIsIk5vIiwiVW5iaWFzZWQgKGV4YWN0KSIsIk1lZGl1bSDigJQgSGVzc2lhbiB0cmFjZSIsIkVsaW1pbmF0ZWQiLCJGb3Igc21vb3RoIGVuZXJnaWVzIl0sWyJOb2lzZSBDb250cmFzdGl2ZSBFc3RpbWF0aW9uIChOQ0UpIiwiTm8iLCJVbmJpYXNlZCIsIk1lZGl1bSIsIkVzdGltYXRlZCB2aWEgbm9pc2UiLCJXaGVuIFogZXN0aW1hdGUgbmVlZGVkIl1dfSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkVCTSBpbmZlcmVuY2UgaXMganVzdCBvbmUgZm9yd2FyZCBwYXNzIHRocm91Z2ggRV/OuCDigJQgbm8gcGFydGl0aW9uIGZ1bmN0aW9uIG5lZWRlZCBhdCB0ZXN0IHRpbWUuIiwiVXNlIERTTSB3aGVuIHRyYWluaW5nIGRhdGEgaXMgY2xlYW4gYW5kIHlvdSB3YW50IHRvIGF2b2lkIE1DTUMgZW50aXJlbHk7IGdyYWRpZW50IGNvbXB1dGF0aW9uIGlzIHRoZSBvbmx5IGNvc3QuIiwiVXNlIFBDRCB3aGVuIGdlbmVyYXRpb24gcXVhbGl0eSBhbHNvIG1hdHRlcnMg4oCUIHBlcnNpc3RlbnQgY2hhaW5zIHByb2R1Y2UgYmV0dGVyIHNhbXBsZXMgdGhhbiBDRC0xLiIsIkVuZXJneSBzY29yZXMgYXJlIHVubm9ybWFsaXNlZDsgZm9yIGFub21hbHkgdGhyZXNob2xkaW5nIGZpdCBhIEdhdXNzaWFuIHRvIHRyYWluaW5nIGVuZXJnaWVzIGFuZCBmbGFnIHBvaW50cyBcdTAwM2UgzrwgKyAzz4MuIiwiSkVNIChHcmF0aHdvaGwgZXQgYWwuLCAyMDIwKSBjb21iaW5lcyBjbGFzc2lmaWVyIGFuZCBFQk06IGxvZ2l0cyBkZWZpbmUgZW5lcmd5LCBlbmFibGluZyBqb2ludCBnZW5lcmF0aW9uIGFuZCBjbGFzc2lmaWNhdGlvbi4iXX0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYW5vbWFseSBkZXRlY3Rpb24sIGNvbnRyYXN0aXZlIGRpdmVyZ2VuY2Ugb3IgZGVub2lzaW5nIHNjb3JlIG1hdGNoaW5nIGFyZSB0aGUgbW9zdCBwcmFjdGljYWwgdHJhaW5pbmcgY2hvaWNlcy4gRFNNIGF2b2lkcyBNQ01DIGVudGlyZWx5IGFuZCBvZnRlbiB0cmFpbnMgZmFzdGVyLiBQQ0QgZ2l2ZXMgYmV0dGVyIGVuZXJneSBsYW5kc2NhcGVzIHdoZW4gZ2VuZXJhdGlvbiBxdWFsaXR5IGFsc28gbWF0dGVycy4gSW4gYWxsIGNhc2VzLCB0aGUgaW5mZXJlbmNlIGFub21hbHkgc2NvcmUgaXMganVzdCB0aGUgZm9yd2FyZCBwYXNzIHRocm91Z2ggRV/OuCDigJQgZmFzdCBhbmQgc2ltcGxlLiJ9LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Energy-Based Models — Boltzmann Distribution and MCMC

Energy-based models (EBMs) define a probability distribution via an energy function: p_θ(x) = exp(−E_θ(x)) / Z(θ) where Z(θ) = ∫ exp(−E_θ(x)) dx is the partition function. The energy E_θ is parameterised by a neural network and can take any value — no architectural constraints like invertibility are required. The key challenge is that Z is generally intractable, complicating both training and normalised-probability computation. For anomaly detection this is not a fundamental barrier: low energy ↔ normal, high energy ↔ anomaly.

## Energy Functions and the Boltzmann Distribution

The Boltzmann distribution assigns high probability to regions of low energy and low probability to high-energy regions. During training we want the model to assign low energy to training data (positive phase) and high energy to other regions (negative phase). The log-likelihood gradient is: ∂/∂θ log p_θ(x) = −∂E_θ(x)/∂θ + E_{p_θ}[∂E_θ/∂θ]. The first term pushes down energy at observed data; the second term (the negative phase) pushes energy up at samples from the current model — requiring MCMC sampling.

- Unnormalised density: p_θ(x) ∝ exp(−E_θ(x)) — only the energy function needs to be learned.
- Partition function Z(θ) = ∫exp(−E_θ)dx — intractable in general; makes MLE gradient hard to compute.
- Negative phase: E_{p_θ}[∂E/∂θ] — expectation under the model; approximated by MCMC samples.
- Contrastive divergence: approximate negative phase using short MCMC chains initialised at training data.
- Score matching: sidestep Z by matching score functions ∇_x log p — avoids MCMC entirely.

```python
import torch
import torch.nn as nn
import numpy as np

class EnergyNet(nn.Module):
    def __init__(self, d_in):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_in, 64), nn.SiLU(),
            nn.Linear(64, 64), nn.SiLU(),
            nn.Linear(64, 1))
    def forward(self, x):
        return self.net(x).squeeze(-1)  # scalar energy per sample

def contrastive_divergence_step(ebm, x_pos, opt, n_steps=10, step_size=0.01):
    '''One CD-k training step: positive phase minus negative phase.'''
    ebm.train()
    # Negative phase: run short Langevin chain from positive samples
    x_neg = x_pos.detach().clone().requires_grad_(True)
    for _ in range(n_steps):
        e_neg = ebm(x_neg)
        grad = torch.autograd.grad(e_neg.sum(), x_neg)[0]
        x_neg = (x_neg - step_size * grad +
                 (2 * step_size) ** 0.5 * torch.randn_like(x_neg)).detach()
        x_neg.requires_grad_(True)
    x_neg = x_neg.detach()
    opt.zero_grad()
    loss = ebm(x_pos).mean() - ebm(x_neg).mean()  # min E(pos), max E(neg)
    loss.backward(); opt.step()
    return loss.item()

torch.manual_seed(0)
X_tr = torch.tensor(np.random.randn(600, 4), dtype=torch.float32)
ebm = EnergyNet(d_in=4)
opt = torch.optim.Adam(ebm.parameters(), lr=1e-3)
for ep in range(20):
    loss_val = contrastive_divergence_step(ebm, X_tr, opt)
    if (ep+1) % 5 == 0:
        print(f'Epoch {ep+1:2d} | CD loss: {loss_val:.4f}')
```

## Training via Contrastive Divergence

Contrastive Divergence (CD-k) approximates the negative phase with k steps of MCMC starting from training data. CD-1 (a single step) is the most common — cheap but biased. Persistent CD (PCD) maintains a persistent chain of fantasy particles across batches, which converges to true model samples as training progresses but requires storing and updating the chain. CD-k gradient quality increases with k but so does computational cost. For anomaly detection, exact normalisation is not needed — relative energy values suffice for ranking.

## Langevin Dynamics for MCMC Sampling

Langevin dynamics samples from p_θ(x) ∝ exp(−E_θ(x)) by simulating the SDE: xₜ₊₁ = xₜ − (η/2)∇_x E_θ(xₜ) + √η·ε where ε~N(0,I). The gradient term pulls particles toward low-energy regions; the noise term ensures exploration. With step size η→0 and enough steps, samples converge to p_θ. In practice, a finite η introduces a discretisation bias corrected by a Metropolis-Hastings accept/reject step (MALA). Langevin dynamics is the standard negative-phase sampler for deep EBMs.

```python
import torch
import numpy as np

def langevin_sample(ebm, n_samples, d, n_steps=100, step_size=0.01, noise_scale=1.0):
    '''Sample from EBM via Langevin MCMC.'''
    ebm.eval()
    x = torch.randn(n_samples, d) * noise_scale
    x.requires_grad_(True)
    for i in range(n_steps):
        energy = ebm(x)
        grad = torch.autograd.grad(energy.sum(), x)[0]
        with torch.no_grad():
            x = x - 0.5 * step_size * grad + (step_size ** 0.5) * torch.randn_like(x)
        x = x.detach().requires_grad_(True)
        if (i + 1) % 25 == 0:
            e_mean = ebm(x.detach()).mean().item()
            print(f'  Step {i+1:4d} | mean energy: {e_mean:.4f}')
    return x.detach()

print('Langevin sampling from trained EBM (4D):')
samples = langevin_sample(ebm, n_samples=50, d=4, n_steps=100)
print(f'Sample mean:  {samples.mean(dim=0).numpy().round(3)}')
print(f'Sample std:   {samples.std(dim=0).numpy().round(3)}')
print(f'Energy mean:  {ebm(samples).mean().item():.4f}')
```

## EBM Anomaly Detection

Because p_θ(x) ∝ exp(−E_θ(x)), the energy E_θ(x) is a direct (unnormalised) anomaly score: low energy = high probability = normal; high energy = low probability = anomaly. This avoids the need to compute Z. The threshold is set from the distribution of energies on normal training data. EBM anomaly detection is robust to the choice of architecture as long as E_θ is flexible enough to model the normal manifold — any neural network suffices.

```python
import torch
import numpy as np
from sklearn.metrics import roc_auc_score

np.random.seed(5)
torch.manual_seed(5)
X_train = torch.tensor(np.random.randn(500, 4), dtype=torch.float32)
ebm2 = EnergyNet(d_in=4)
opt2 = torch.optim.Adam(ebm2.parameters(), lr=5e-4)
for _ in range(50):
    contrastive_divergence_step(ebm2, X_train, opt2, n_steps=5)

# Anomaly detection evaluation
X_n_te = torch.tensor(np.random.randn(100, 4), dtype=torch.float32)
X_a_te = torch.tensor(np.random.randn(25, 4)*0.2 + 3, dtype=torch.float32)
X_all = torch.cat([X_n_te, X_a_te])
y = np.array([0]*100 + [1]*25)

ebm2.eval()
with torch.no_grad():
    energy_scores = ebm2(X_all).numpy()

thr = np.percentile(energy_scores[:100], 95)
detected = (energy_scores[100:] > thr).sum()
auroc = roc_auc_score(y, energy_scores)
print(f'AUROC (energy score):   {auroc:.4f}')
print(f'Threshold (95th pct):   {thr:.4f}')
print(f'Anomalies detected:     {detected}/{len(X_a_te)}')
print(f'Normal energy mean:     {energy_scores[:100].mean():.4f}')
print(f'Anomaly energy mean:    {energy_scores[100:].mean():.4f}')
```

> **EBM vs Normalizing Flows for Anomaly Detection**: EBMs require only forward passes through E_θ at inference — fast and architecturally flexible. Flows require an invertible architecture and can compute exact log p(x). EBMs are harder to train (MCMC negative phase) but can use arbitrary architectures including residual networks with batch norm. For anomaly detection where only a ranking (not absolute probability) is needed, EBM energy scores are often sufficient.

## Score Matching — Avoiding the Partition Function

Hyvärinen's score matching sidesteps Z entirely by matching the score function ∇_x log p_θ(x) = −∇_x E_θ(x) to the data score. The objective is: J(θ) = E_data[‖∇_x log p_θ(x)‖² / 2 + tr(∇_x² log p_θ(x))]. The first term is small when model and data scores agree; the second term (trace of the Hessian) regularises. Denoising score matching (DSM) simplifies computation by matching scores of noisy data: J_DSM = E_{x,ε}[‖∇_x log p_θ(x+σε) + ε/σ‖²].

```python
import torch
import numpy as np

def denoising_score_matching_loss(ebm, x_clean, sigma=0.1):
    '''DSM loss: match energy gradient to noise direction.'''
    noise = torch.randn_like(x_clean) * sigma
    x_noisy = x_clean + noise
    x_noisy.requires_grad_(True)
    energy = ebm(x_noisy)
    score_model = -torch.autograd.grad(energy.sum(), x_noisy,
                                        create_graph=True)[0]
    target_score = -noise / (sigma ** 2)
    loss = 0.5 * ((score_model - target_score) ** 2).sum(dim=-1).mean()
    return loss

torch.manual_seed(3)
X_sm = torch.tensor(np.random.randn(400, 4), dtype=torch.float32)
ebm_sm = EnergyNet(d_in=4)
opt_sm = torch.optim.Adam(ebm_sm.parameters(), lr=1e-3)
for ep in range(30):
    loss = denoising_score_matching_loss(ebm_sm, X_sm, sigma=0.2)
    opt_sm.zero_grad()
    loss.backward(); opt_sm.step()
    if (ep + 1) % 10 == 0:
        print(f'Epoch {ep+1:2d} | DSM loss: {loss.item():.6f}')
print('Score matching avoids MCMC — no negative phase sampling required.')
```

## EBM Training Methods Comparison

| Training Method | MCMC Needed | Gradient Quality | Training Cost | Partition Function | Practical Use |
| --- | --- | --- | --- | --- | --- |
| Contrastive Divergence (CD-1) | Yes (1 step) | Biased but fast | Low | Ignored | Most common baseline |
| Persistent CD (PCD) | Yes (persistent chain) | Better — chain mixes | Medium | Ignored | Better quality than CD |
| Langevin MCMC (full) | Yes (100+ steps) | Good — near true model | High | Ignored | Slow but accurate |
| Score Matching | No | Unbiased (exact) | Medium — Hessian trace | Eliminated | For smooth energies |
| Noise Contrastive Estimation (NCE) | No | Unbiased | Medium | Estimated via noise | When Z estimate needed |

- EBM inference is just one forward pass through E_θ — no partition function needed at test time.
- Use DSM when training data is clean and you want to avoid MCMC entirely; gradient computation is the only cost.
- Use PCD when generation quality also matters — persistent chains produce better samples than CD-1.
- Energy scores are unnormalised; for anomaly thresholding fit a Gaussian to training energies and flag points > μ + 3σ.
- JEM (Grathwohl et al., 2020) combines classifier and EBM: logits define energy, enabling joint generation and classification.

For anomaly detection, contrastive divergence or denoising score matching are the most practical training choices. DSM avoids MCMC entirely and often trains faster. PCD gives better energy landscapes when generation quality also matters. In all cases, the inference anomaly score is just the forward pass through E_θ — fast and simple.

---

