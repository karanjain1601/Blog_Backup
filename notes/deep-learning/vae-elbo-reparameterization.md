---
title: "VAE — ELBO Derivation and Reparameterization Trick"
slug: "vae-elbo-reparameterization"
description: "A rigorous derivation of the VAE objective from first principles: how the intractable marginal log p(x) is lower-bounded by the ELBO, why the reparameterization trick enables gradients through stochastic nodes, and how posterior collapse arises and is fixed with cyclical KL annealing."
tags: ["deep-learning", "generative-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVmFyaWF0aW9uYWwgQXV0b2VuY29kZXJzIChLaW5nbWEgXHUwMDI2IFdlbGxpbmcgMjAxMykgYXJlIGxhdGVudCB2YXJpYWJsZSBtb2RlbHMgdGhhdCBqb2ludGx5IGxlYXJuIHRvIGNvbXByZXNzIGRhdGEgaW50byBhIGNvbnRpbnVvdXMgbGF0ZW50IHNwYWNlIGFuZCBnZW5lcmF0ZSBkYXRhIGZyb20gdGhhdCBzcGFjZS4gVGhlIGdlbmVyYXRpdmUgbW9kZWwgaXMgcCh4LHopID0gcCh4fHopcCh6KSB3aGVyZSBwKHopID0gTigwLEkpIGlzIHRoZSBwcmlvciBhbmQgcF/OuCh4fHopIGlzIGEgbGVhcm5lZCBkZWNvZGVyLiBUaGUgaW5mZXJlbmNlIG1vZGVsIHFfz4Yoenx4KSBhcHByb3hpbWF0ZXMgdGhlIGludHJhY3RhYmxlIHBvc3RlcmlvciBwKHp8eCkuIFRyYWluaW5nIG1heGltaXplcyBhIGxvd2VyIGJvdW5kIG9uIGxvZyBwKHgpIGNhbGxlZCB0aGUgRUxCTywgZGVyaXZlZCBieSBpbnRyb2R1Y2luZyBxIGFuZCBhcHBseWluZyBKZW5zZW5cdTAwMjdzIGluZXF1YWxpdHkuIFRoZSByZXBhcmFtZXRlcml6YXRpb24gdHJpY2sgY29udmVydHMgdGhlIHN0b2NoYXN0aWMgc2FtcGxpbmcgc3RlcCBpbnRvIGEgZGlmZmVyZW50aWFibGUgb3BlcmF0aW9uLCBhbGxvd2luZyBncmFkaWVudC1iYXNlZCBvcHRpbWl6YXRpb24gb2YgYm90aCB0aGUgZW5jb2RlciDPhiBhbmQgZGVjb2RlciDOuCBzaW11bHRhbmVvdXNseS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFTEJPIERlcml2YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlN0YXJ0aW5nIGZyb20gbG9nIHAoeCkgYW5kIGludHJvZHVjaW5nIHFfz4Yoenx4KSB2aWEgaW1wb3J0YW5jZSB3ZWlnaHRpbmc6IGxvZyBwKHgpID0gbG9nIOKIqyBwKHh8eilwKHopIGR6ID0gbG9nIEVfe3Ffz4Z9W3AoeHx6KXAoeikvcV/Phih6fHgpXSDiiaUgRV97cV/Phn1bbG9nIHAoeHx6KV0gKyBFX3txX8+GfVtsb2cgcCh6KS9xX8+GKHp8eCldID0gRV97cV/Phn1bbG9nIHAoeHx6KV0gLSBLTChxX8+GKHp8eCkgfHwgcCh6KSkuIFRoZSBnYXAgYmV0d2VlbiBsb2cgcCh4KSBhbmQgdGhlIEVMQk8gaXMgS0wocV/Phih6fHgpIHx8IHAoenx4KSkg4omlIDAsIHNvIEVMQk8g4omkIGxvZyBwKHgpLiBNYXhpbWl6aW5nIHRoZSBFTEJPIHNpbXVsdGFuZW91c2x5IG1heGltaXplcyBhIGxvd2VyIGJvdW5kIG9uIHRoZSBtYXJnaW5hbCBsaWtlbGlob29kIGFuZCBtaW5pbWl6ZXMgdGhlIEtMIGRpdmVyZ2VuY2UgYmV0d2VlbiB0aGUgdmFyaWF0aW9uYWwgcG9zdGVyaW9yIGFuZCB0aGUgdHJ1ZSBwb3N0ZXJpb3IuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUmVwYXJhbWV0ZXJpemF0aW9uIFRyaWNrIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgRUxCTyByZXF1aXJlcyBjb21wdXRpbmcgZ3JhZGllbnRzIHRocm91Z2ggRV97cV/Phn1bbG9nIHAoeHx6KV0sIGJ1dCB6IH4gcV/Phih6fHgpID0gTijOvF/Phih4KSwgz4Nfz4bCsih4KSkgaXMgYSBzdG9jaGFzdGljIG5vZGUg4oCUIG5haXZlbHksIGdyYWRpZW50cyBjYW5ub3QgZmxvdyB0aHJvdWdoIHRoZSBzYW1wbGluZyBvcGVyYXRpb24uIFRoZSByZXBhcmFtZXRlcml6YXRpb24gdHJpY2sgZmFjdG9ycyB6ID0gzrxfz4YoeCkgKyDPg1/Phih4KSDiipkgzrUgd2hlcmUgzrUgfiBOKDAsSSkuIE5vdyB6IGlzIGEgZGV0ZXJtaW5pc3RpYyBmdW5jdGlvbiBvZiB0aGUgcGFyYW1ldGVycyDOvF/Phiwgz4Nfz4YgYW5kIHRoZSBhdXhpbGlhcnkgbm9pc2UgzrUuIEdyYWRpZW50cyBvZiB0aGUgbG9zcyB3aXRoIHJlc3BlY3QgdG8gz4YgZmxvdyB0aHJvdWdoIHogPSDOvCArIM+DwrfOtSBjbGVhbmx5IHZpYSBiYWNrcHJvcGFnYXRpb24uIFRoZSBlbmNvZGVyIG91dHB1dHMgzrwgKG1lYW4pIGFuZCBsb2cgz4PCsiAobG9nIHZhcmlhbmNlKSBmb3IgbnVtZXJpY2FsIHN0YWJpbGl0eSwgYW5kIM+DID0gZXhwKDAuNSDCtyBsb2cgz4PCsikuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFMb2FkZXJcbmZyb20gdG9yY2h2aXNpb24gaW1wb3J0IGRhdGFzZXRzLCB0cmFuc2Zvcm1zXG5cbmNsYXNzIFZBRUVuY29kZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5wdXRfZGltPTc4NCwgaGlkZGVuX2RpbT01MTIsIGxhdGVudF9kaW09MjApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5mYzEgPSBubi5MaW5lYXIoaW5wdXRfZGltLCBoaWRkZW5fZGltKVxuICAgICAgICBzZWxmLmZjX211ICA9IG5uLkxpbmVhcihoaWRkZW5fZGltLCBsYXRlbnRfZGltKVxuICAgICAgICBzZWxmLmZjX2xvZ3ZhciA9IG5uLkxpbmVhcihoaWRkZW5fZGltLCBsYXRlbnRfZGltKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGggPSBGLnJlbHUoc2VsZi5mYzEoeC52aWV3KHguc2l6ZSgwKSwgLTEpKSlcbiAgICAgICAgcmV0dXJuIHNlbGYuZmNfbXUoaCksIHNlbGYuZmNfbG9ndmFyKGgpXG5cbmNsYXNzIFZBRURlY29kZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbGF0ZW50X2RpbT0yMCwgaGlkZGVuX2RpbT01MTIsIG91dHB1dF9kaW09Nzg0KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZmMxID0gbm4uTGluZWFyKGxhdGVudF9kaW0sIGhpZGRlbl9kaW0pXG4gICAgICAgIHNlbGYuZmMyID0gbm4uTGluZWFyKGhpZGRlbl9kaW0sIG91dHB1dF9kaW0pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB6KTpcbiAgICAgICAgaCA9IEYucmVsdShzZWxmLmZjMSh6KSlcbiAgICAgICAgcmV0dXJuIHRvcmNoLnNpZ21vaWQoc2VsZi5mYzIoaCkpXG5cbmNsYXNzIFZBRShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBsYXRlbnRfZGltPTIwKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IFZBRUVuY29kZXIobGF0ZW50X2RpbT1sYXRlbnRfZGltKVxuICAgICAgICBzZWxmLmRlY29kZXIgPSBWQUVEZWNvZGVyKGxhdGVudF9kaW09bGF0ZW50X2RpbSlcblxuICAgIGRlZiByZXBhcmFtZXRlcml6ZShzZWxmLCBtdSwgbG9ndmFyKTpcbiAgICAgICAgXCJcIlwieiA9IG11ICsgc3RkICogZXBzOyBlcHMgfiBOKDAsIEkpIOKAlCBkaWZmZXJlbnRpYWJsZSBzYW1wbGluZy5cIlwiXCJcbiAgICAgICAgc3RkID0gdG9yY2guZXhwKDAuNSAqIGxvZ3ZhcilcbiAgICAgICAgZXBzID0gdG9yY2gucmFuZG5fbGlrZShzdGQpXG4gICAgICAgIHJldHVybiBtdSArIHN0ZCAqIGVwc1xuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG11LCBsb2d2YXIgPSBzZWxmLmVuY29kZXIoeClcbiAgICAgICAgeiA9IHNlbGYucmVwYXJhbWV0ZXJpemUobXUsIGxvZ3ZhcilcbiAgICAgICAgcmVjb24gPSBzZWxmLmRlY29kZXIoeilcbiAgICAgICAgcmV0dXJuIHJlY29uLCBtdSwgbG9ndmFyXG5cbm1vZGVsID0gVkFFKGxhdGVudF9kaW09MilcbnggPSB0b3JjaC5yYW5kbig4LCAxLCAyOCwgMjgpXG5yZWNvbiwgbXUsIGxvZ3ZhciA9IG1vZGVsKHgpXG5wcmludChmXHUwMDI3RW5jb2RlciBtdToge211LnNoYXBlfSwgbG9ndmFyOiB7bG9ndmFyLnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdEZWNvZGVyIHJlY29uOiB7cmVjb24uc2hhcGV9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVMQk8gTG9zcyDigJQgUmVjb25zdHJ1Y3Rpb24gYW5kIEtMIFRlcm1zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgRUxCTyBoYXMgdHdvIHRlcm1zLiBUaGUgcmVjb25zdHJ1Y3Rpb24gdGVybSBFX3txX8+GfVtsb2cgcF/OuCh4fHopXSBtZWFzdXJlcyBob3cgd2VsbCB0aGUgZGVjb2RlciByZWNvdmVycyB4IGZyb20gei4gRm9yIGEgQmVybm91bGxpIGRlY29kZXIgKGJpbmFyeSBpbWFnZXMpLCB0aGlzIGlzIGJpbmFyeSBjcm9zcy1lbnRyb3B5OyBmb3IgYSBHYXVzc2lhbiBkZWNvZGVyLCBpdCBpcyBtZWFuIHNxdWFyZWQgZXJyb3IuIFRoZSBLTCB0ZXJtIC1LTChxX8+GKHp8eCkgfHwgcCh6KSkgcmVndWxhcml6ZXMgdGhlIHBvc3RlcmlvciB0b3dhcmQgdGhlIHByaW9yIE4oMCxJKS4gRm9yIGRpYWdvbmFsIEdhdXNzaWFuIGVuY29kZXIgYW5kIHN0YW5kYXJkIEdhdXNzaWFuIHByaW9yLCB0aGUgS0wgaGFzIGEgY2xvc2VkIGZvcm06IEtMID0gLcK9IM6j4rG8ICgxICsgbG9nIM+D4rG8wrIgLSDOvOKxvMKyIC0gz4PisbzCsikuIFRoZSBjbG9zZWQgZm9ybSBhdm9pZHMgTW9udGUgQ2FybG8gZXN0aW1hdGlvbiBvZiB0aGUgS0wsIHJlZHVjaW5nIGdyYWRpZW50IHZhcmlhbmNlIGFuZCBtYWtpbmcgdHJhaW5pbmcgbW9yZSBzdGFibGUuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgdmFlX2xvc3MocmVjb24sIHgsIG11LCBsb2d2YXIsIGJldGE9MS4wKTpcbiAgICBcIlwiXCJcbiAgICBFTEJPIGxvc3MgPSByZWNvbnN0cnVjdGlvbl9sb3NzICsgYmV0YSAqIEtMX2RpdmVyZ2VuY2UuXG4gICAgcmVjb246IChCLCA3ODQpIHNpZ21vaWQgb3V0cHV0cy5cbiAgICB4OiAgICAgKEIsIDEsIDI4LCAyOCkgaW5wdXQgaW1hZ2VzIGluIFswLCAxXS5cbiAgICBtdSwgbG9ndmFyOiAoQiwgbGF0ZW50X2RpbSkgZW5jb2RlciBvdXRwdXRzLlxuICAgIEtMIGNsb3NlZCBmb3JtOiAtMC41ICogc3VtKDEgKyBsb2d2YXIgLSBtdV4yIC0gZXhwKGxvZ3ZhcikpLlxuICAgIFwiXCJcIlxuICAgIHhfZmxhdCA9IHgudmlldyh4LnNpemUoMCksIC0xKVxuICAgICMgQmVybm91bGxpIHJlY29uc3RydWN0aW9uOiBiaW5hcnkgY3Jvc3MtZW50cm9weSBzdW1tZWQgb3ZlciBwaXhlbHNcbiAgICByZWNvbl9sb3NzID0gRi5iaW5hcnlfY3Jvc3NfZW50cm9weShyZWNvbiwgeF9mbGF0LCByZWR1Y3Rpb249XHUwMDI3c3VtXHUwMDI3KSAvIHguc2l6ZSgwKVxuICAgICMgS0wgZGl2ZXJnZW5jZTogYW5hbHl0aWNhbCBmb3IgcT1OKG11LCBkaWFnKHNpZ21hXjIpKSBhbmQgcD1OKDAsSSlcbiAgICBrbCA9IC0wLjUgKiB0b3JjaC5zdW0oMSArIGxvZ3ZhciAtIG11LnBvdygyKSAtIGxvZ3Zhci5leHAoKSwgZGltPTEpXG4gICAga2xfbG9zcyA9IGtsLm1lYW4oKVxuICAgIHRvdGFsID0gcmVjb25fbG9zcyArIGJldGEgKiBrbF9sb3NzXG4gICAgcmV0dXJuIHRvdGFsLCByZWNvbl9sb3NzLml0ZW0oKSwga2xfbG9zcy5pdGVtKClcblxuIyBTYW5pdHkgY2hlY2sgYXQgaW5pdDogS0wgb2YgTigwLEkpIHZzIE4oMCxJKSBzaG91bGQgYmUgMFxubXVfemVybyAgICA9IHRvcmNoLnplcm9zKDE2LCAyMClcbmxvZ3Zhcl96ZXJvID0gdG9yY2guemVyb3MoMTYsIDIwKVxucmVjb25fZHVtbXkgPSB0b3JjaC5yYW5kKDE2LCA3ODQpXG54X2R1bW15ID0gdG9yY2gucmFuZCgxNiwgMSwgMjgsIDI4KVxudG90YWwsIHJlY29uX2wsIGtsX2wgPSB2YWVfbG9zcyhyZWNvbl9kdW1teSwgeF9kdW1teSwgbXVfemVybywgbG9ndmFyX3plcm8pXG5wcmludChmXHUwMDI3QXQgaW5pdCAobXU9MCwgbG9ndmFyPTApOiBLTD17a2xfbDouNGZ9IChleHBlY3RlZCB+MC4wKVx1MDAyNylcbnByaW50KGZcdTAwMjdUb3RhbCBFTEJPIGxvc3M6IHt0b3RhbDouNGZ9ICB8IFJlY29uOiB7cmVjb25fbDouNGZ9ICB8IEtMOiB7a2xfbDouNGZ9XHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkdhdXNzaWFuIHZzIEJlcm5vdWxsaSBEZWNvZGVyIENob2ljZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRlY29kZXIgb3V0cHV0IGRpc3RyaWJ1dGlvbiBkZXRlcm1pbmVzIHRoZSBmb3JtIG9mIHRoZSByZWNvbnN0cnVjdGlvbiB0ZXJtLiBBIEJlcm5vdWxsaSBkZWNvZGVyIChzaWdtb2lkIG91dHB1dCwgQkNFIGxvc3MpIGlzIHN0YW5kYXJkIGZvciBiaW5hcml6ZWQgTU5JU1Q6IGVhY2ggcGl4ZWwgaXMgdHJlYXRlZCBhcyBhbiBpbmRlcGVuZGVudCBCZXJub3VsbGkgdmFyaWFibGUuIEEgR2F1c3NpYW4gZGVjb2RlciAobGluZWFyIG91dHB1dCwgTVNFIGxvc3MpIGlzIG1vcmUgYXBwcm9wcmlhdGUgZm9yIGNvbnRpbnVvdXMgaW1hZ2VzOyB0aGUgcmVjb25zdHJ1Y3Rpb24gdGVybSBiZWNvbWVzIEVfe3F9Wy18fHggLSDOvF/OuCh6KXx8wrIvKDLPg8KyKV0sIHdoZXJlIHRoZSBkZWNvZGVyIHZhcmlhbmNlIM+DwrIgY2FuIGJlIGZpeGVkIGF0IDEgKGVxdWl2YWxlbnQgdG8gTVNFKSBvciBsZWFybmVkLiBBIGxlYXJuZWQgz4PCsiBhbGxvd3MgdGhlIG1vZGVsIHRvIGFkYXB0IGl0cyByZWNvbnN0cnVjdGlvbiBjb25maWRlbmNlIHBlciByZWdpb24uIEZvciBuYXR1cmFsIGltYWdlcywgYSBMYXBsYWNlIGRlY29kZXIgKE1BRSBsb3NzLCBtb3JlIHJvYnVzdCB0byBvdXRsaWVycykgb3IgYSBkaXNjcmV0aXplZCBsb2dpc3RpYyBtaXh0dXJlIChQaXhlbENOTisrIHN0eWxlKSBjYW4gaW1wcm92ZSBzYW1wbGUgc2hhcnBuZXNzIG92ZXIgcGxhaW4gR2F1c3NpYW4gZGVjb2RlcnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJCZXJub3VsbGkgZGVjb2Rlcjogc2lnbW9pZCBvdXRwdXQgKyBCQ0UgbG9zcyDigJQgc3RhbmRhcmQgZm9yIGJpbmFyaXplZCBNTklTVCwgYXNzdW1lcyBpbmRlcGVuZGVudCBwaXhlbHMuIiwiR2F1c3NpYW4gZGVjb2RlcjogbGluZWFyIG91dHB1dCArIE1TRSDigJQgYXBwcm9wcmlhdGUgZm9yIGNvbnRpbnVvdXMgaW1hZ2VzOyBlcXVpdmFsZW50IHRvIG1heGltaXppbmcgTih4OyDOvF/OuCh6KSwgSSkuIiwiRGlzY3JldGl6ZWQgbG9naXN0aWMgZGVjb2RlcjogbW9yZSBleHByZXNzaXZlIG91dHB1dCwgdXNlZCBpbiBQaXhlbENOTisrIGFuZCBWUS1WQUUgdG8gaW1wcm92ZSBzaGFycG5lc3MuIiwiRml4ZWQgZGVjb2RlciB2YXJpYW5jZSDPg8KyPTEgc2ltcGxpZmllcyB0cmFpbmluZzsgbGVhcm5lZCDPg8KyIGhlbHBzIHRoZSBtb2RlbCB3ZWlnaHQgcmVjb25zdHJ1Y3Rpb24gY29uZmlkZW5jZS4iLCJUaGUgY2hvaWNlIG9mIGRlY29kZXIgZGlzdHJpYnV0aW9uIGNoYW5nZXMgdGhlIHNjYWxlIG9mIHRoZSByZWNvbnN0cnVjdGlvbiB0ZXJtIHJlbGF0aXZlIHRvIEtMIOKAlCBhZmZlY3RzIGVmZmVjdGl2ZSDOsi4iXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVmlzdWFsaXppbmcgdGhlIDJEIExhdGVudCBTcGFjZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSAyLWRpbWVuc2lvbmFsIGxhdGVudCBzcGFjZSBhbGxvd3MgZGlyZWN0IHZpc3VhbGl6YXRpb24gb2YgdGhlIGxlYXJuZWQgcmVwcmVzZW50YXRpb24uIEFmdGVyIHRyYWluaW5nLCBlbmNvZGluZyB0aGUgTU5JU1QgdGVzdCBzZXQgYW5kIHBsb3R0aW5nIHRoZSAozrzigoEsIM684oKCKSB2YWx1ZXMgY29sb3JlZCBieSBkaWdpdCBjbGFzcyByZXZlYWxzIGNsdXN0ZXIgc3RydWN0dXJlLiBUcmF2ZXJzaW5nIHRoZSBsYXRlbnQgc3BhY2UgYnkgZGVjb2RpbmcgcG9pbnRzIG9uIGEgZ3JpZCBzaG93cyBzbW9vdGggaW50ZXJwb2xhdGlvbiBiZXR3ZWVuIGRpZ2l0IHN0eWxlcy4gVGhpcyBjb25maXJtcyB0aGF0IHRoZSBWQUUgaGFzIG9yZ2FuaXplZCB0aGUgbGF0ZW50IHNwYWNlIHNlbWFudGljYWxseSBhbmQgdGhhdCB0aGUgZGVjb2RlciBjYW4gZ2VuZXJhdGUgY29oZXJlbnQgaW1hZ2VzIGZyb20gYW55IHBvaW50IGluIHRoZSBjb250aW51b3VzIHByaW9yLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCBudW1weSBhcyBucFxuaW1wb3J0IG1hdHBsb3RsaWJcbm1hdHBsb3RsaWIudXNlKFx1MDAyN0FnZ1x1MDAyNylcbmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHRcbmZyb20gdG9yY2h2aXNpb24gaW1wb3J0IGRhdGFzZXRzLCB0cmFuc2Zvcm1zXG5cbmRlZiB2aXN1YWxpemVfbGF0ZW50X3NwYWNlKG1vZGVsLCBkZXZpY2U9XHUwMDI3Y3B1XHUwMDI3LCBuX3NhbXBsZXM9MjAwMCk6XG4gICAgXCJcIlwiUGxvdCAyRCBsYXRlbnQgc3BhY2Ugb2YgVkFFIHRyYWluZWQgb24gTU5JU1QsIGNvbG9yZWQgYnkgZGlnaXQgY2xhc3MuXCJcIlwiXG4gICAgbW9kZWwuZXZhbCgpXG4gICAgdHJhbnNmb3JtID0gdHJhbnNmb3Jtcy5Db21wb3NlKFt0cmFuc2Zvcm1zLlRvVGVuc29yKCldKVxuICAgIGRhdGFzZXQgPSBkYXRhc2V0cy5NTklTVChyb290PVx1MDAyNy90bXAvbW5pc3RcdTAwMjcsIHRyYWluPUZhbHNlLCBkb3dubG9hZD1UcnVlLCB0cmFuc2Zvcm09dHJhbnNmb3JtKVxuICAgIGxvYWRlciA9IHRvcmNoLnV0aWxzLmRhdGEuRGF0YUxvYWRlcihkYXRhc2V0LCBiYXRjaF9zaXplPTI1Niwgc2h1ZmZsZT1GYWxzZSlcbiAgICB6cywgbGFiZWxzID0gW10sIFtdXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGZvciB4LCB5IGluIGxvYWRlcjpcbiAgICAgICAgICAgIG11LCBfID0gbW9kZWwuZW5jb2Rlcih4LnRvKGRldmljZSkpXG4gICAgICAgICAgICB6cy5hcHBlbmQobXUuY3B1KCkubnVtcHkoKSlcbiAgICAgICAgICAgIGxhYmVscy5hcHBlbmQoeS5udW1weSgpKVxuICAgICAgICAgICAgaWYgc3VtKGxlbihsKSBmb3IgbCBpbiBsYWJlbHMpIFx1MDAzZT0gbl9zYW1wbGVzOlxuICAgICAgICAgICAgICAgIGJyZWFrXG4gICAgenMgPSBucC5jb25jYXRlbmF0ZSh6cylbOm5fc2FtcGxlc11cbiAgICBsYWJlbHMgPSBucC5jb25jYXRlbmF0ZShsYWJlbHMpWzpuX3NhbXBsZXNdXG4gICAgZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSg3LCA2KSlcbiAgICBzY2F0dGVyID0gYXguc2NhdHRlcih6c1s6LCAwXSwgenNbOiwgMV0sIGM9bGFiZWxzLCBjbWFwPVx1MDAyN3RhYjEwXHUwMDI3LCBhbHBoYT0wLjYsIHM9NilcbiAgICBwbHQuY29sb3JiYXIoc2NhdHRlciwgYXg9YXgsIGxhYmVsPVx1MDAyN0RpZ2l0IGNsYXNzXHUwMDI3KVxuICAgIGF4LnNldF94bGFiZWwoXHUwMDI3euKCgVx1MDAyNyk7IGF4LnNldF95bGFiZWwoXHUwMDI3euKCglx1MDAyNyk7IGF4LnNldF90aXRsZShcdTAwMjdWQUUgMkQgTGF0ZW50IFNwYWNlIOKAlCBNTklTVFx1MDAyNylcbiAgICBwbHQudGlnaHRfbGF5b3V0KCk7IHBsdC5zYXZlZmlnKFx1MDAyNy90bXAvdmFlX2xhdGVudC5wbmdcdTAwMjcsIGRwaT0xMjApXG4gICAgcHJpbnQoXHUwMDI3U2F2ZWQgbGF0ZW50IHNwYWNlIHBsb3QgdG8gL3RtcC92YWVfbGF0ZW50LnBuZ1x1MDAyNylcbiAgICByZXR1cm4genMsIGxhYmVsc1xuXG5mcm9tIHRvcmNoIGltcG9ydCBublxuY2xhc3MgTWluaW1hbFZBRShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW5jb2RlciA9IG5uLlNlcXVlbnRpYWwobm4uRmxhdHRlbigpLCBubi5MaW5lYXIoNzg0LDI1NiksIG5uLlJlTFUoKSlcbiAgICAgICAgc2VsZi5mY19tdSA9IG5uLkxpbmVhcigyNTYsIDIpXG4gICAgICAgIHNlbGYuZmNfbG9ndmFyID0gbm4uTGluZWFyKDI1NiwgMilcbiAgICAgICAgc2VsZi5kZWNvZGVyID0gbm4uU2VxdWVudGlhbChubi5MaW5lYXIoMiwyNTYpLCBubi5SZUxVKCksIG5uLkxpbmVhcigyNTYsNzg0KSwgbm4uU2lnbW9pZCgpKVxuICAgIGRlZiByZXBhcmFtZXRlcml6ZShzZWxmLCBtdSwgbG9ndmFyKTpcbiAgICAgICAgcmV0dXJuIG11ICsgdG9yY2guZXhwKDAuNSAqIGxvZ3ZhcikgKiB0b3JjaC5yYW5kbl9saWtlKG11KVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBoID0gc2VsZi5lbmNvZGVyKHgpXG4gICAgICAgIG11LCBsb2d2YXIgPSBzZWxmLmZjX211KGgpLCBzZWxmLmZjX2xvZ3ZhcihoKVxuICAgICAgICByZXR1cm4gc2VsZi5kZWNvZGVyKHNlbGYucmVwYXJhbWV0ZXJpemUobXUsIGxvZ3ZhcikpLCBtdSwgbG9ndmFyXG5wcmludChcdTAwMjcyRCBWQUUgcmVhZHkgZm9yIHZpc3VhbGl6YXRpb25cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUG9zdGVyaW9yIENvbGxhcHNlIGFuZCBDeWNsaWNhbCBLTCBBbm5lYWxpbmcifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBvc3RlcmlvciBjb2xsYXBzZSBvY2N1cnMgd2hlbiB0aGUgZGVjb2RlciBiZWNvbWVzIHNvIHBvd2VyZnVsIHRoYXQgaXQgaWdub3JlcyB0aGUgbGF0ZW50IGNvZGUgeiBlbnRpcmVseS4gVGhlIGVuY29kZXIgb3V0cHV0cyBxX8+GKHp8eCkg4omIIHAoeikgPSBOKDAsSSkgZm9yIGFsbCB4LCBkcml2aW5nIEtMIOKGkiAwIHdoaWxlIHRoZSByZWNvbnN0cnVjdGlvbiBsb3NzIHN0YWduYXRlcy4gVGhpcyBpcyBlc3BlY2lhbGx5IGNvbW1vbiB3aXRoIGF1dG9yZWdyZXNzaXZlIGRlY29kZXJzIChSTk4sIFRyYW5zZm9ybWVyKSB0aGF0IGNhbiBtb2RlbCBwKHgpIHdpdGhvdXQgei4gVGhlIGZyZWUgYml0cyBoZXVyaXN0aWMgc2V0cyBhIG1pbmltdW0gS0wgcGVyIGRpbWVuc2lvbiDOuyAodHlwaWNhbGx5IDLigJM0IGJpdHMpLCBhbmQgzrItVkFFIGluY3JlYXNlcyB0aGUgS0wgd2VpZ2h0LiBDeWNsaWNhbCBLTCBhbm5lYWxpbmcgKEZ1IGV0IGFsLiAyMDE5KSBzY2hlZHVsZXMgdGhlIEtMIHdlaWdodCBhcyBhIHNhd3Rvb3RoIHRoYXQgcmlzZXMgZnJvbSAwIHRvIDEgbXVsdGlwbGUgdGltZXMgcGVyIHRyYWluaW5nIHJ1biwgcGVyaW9kaWNhbGx5IHJlc2V0dGluZyB0aGUgZW5jb2RlciB0byBleHBsb3JlIGRpZmZlcmVudCBsYXRlbnQgdXNlcyBiZWZvcmUgdGhlIGRlY29kZXIgYWRhcHRzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBjeWNsaWNhbF9rbF93ZWlnaHQoc3RlcCwgbl9jeWNsZXM9NCwgcmF0aW89MC41LCBtYXhfc3RlcHM9MTAwMDApOlxuICAgIFwiXCJcIlNhd3Rvb3RoIEtMIHdlaWdodCBzY2hlZHVsZTogcmlzZSBmcm9tIDAgdG8gMSBuX2N5Y2xlcyB0aW1lcyBvdmVyIHRyYWluaW5nLlwiXCJcIlxuICAgIGN5Y2xlX2xlbiA9IG1heF9zdGVwcyAvLyBuX2N5Y2xlc1xuICAgIGN5Y2xlX3BvcyA9IHN0ZXAgJSBjeWNsZV9sZW5cbiAgICByYW1wX2VuZCAgPSBpbnQoY3ljbGVfbGVuICogcmF0aW8pXG4gICAgaWYgY3ljbGVfcG9zIFx1MDAzYyByYW1wX2VuZDpcbiAgICAgICAgcmV0dXJuIGN5Y2xlX3BvcyAvIHJhbXBfZW5kXG4gICAgcmV0dXJuIDEuMFxuXG5kZWYgZnJlZV9iaXRzX2tsKGtsX3Blcl9kaW0sIGxhbWJkYV9mYj0zLjApOlxuICAgIFwiXCJcIkZyZWUgYml0czogY2xhbXAgcGVyLWRpbWVuc2lvbiBLTCBiZWxvdyBsYW1iZGFfZmIgdG8gcHJldmVudCBjb2xsYXBzZS5cIlwiXCJcbiAgICByZXR1cm4gdG9yY2guY2xhbXAoa2xfcGVyX2RpbSwgbWluPWxhbWJkYV9mYikuc3VtKGRpbT0tMSkubWVhbigpXG5cbmRlZiBkZXRlY3RfcG9zdGVyaW9yX2NvbGxhcHNlKG11LCBsb2d2YXIsIHRocmVzaG9sZD0wLjA1KTpcbiAgICBcIlwiXCJGbGFnIGxhdGVudCBkaW1zIHdoZXJlIEtMIGNvbnRyaWJ1dGlvbiBpcyBiZWxvdyB0aHJlc2hvbGQgKGNvbGxhcHNlZCkuXCJcIlwiXG4gICAga2xfcGVyX2RpbSA9IC0wLjUgKiAoMSArIGxvZ3ZhciAtIG11LnBvdygyKSAtIGxvZ3Zhci5leHAoKSlcbiAgICBhdmdfa2wgPSBrbF9wZXJfZGltLm1lYW4oZGltPTApXG4gICAgY29sbGFwc2VkID0gKGF2Z19rbCBcdTAwM2MgdGhyZXNob2xkKS5zdW0oKS5pdGVtKClcbiAgICBhY3RpdmUgICAgPSAoYXZnX2tsIFx1MDAzZT0gdGhyZXNob2xkKS5zdW0oKS5pdGVtKClcbiAgICByZXR1cm4gYXZnX2tsLCBjb2xsYXBzZWQsIGFjdGl2ZVxuXG4jIFNpbXVsYXRlIGNvbGxhcHNlIHNjZW5hcmlvXG50b3JjaC5tYW51YWxfc2VlZCg0Milcbm11X2NvbGxhcHNlZCAgICA9IHRvcmNoLnJhbmRuKDY0LCAyMCkgKiAwLjAxXG5sb2d2YXJfY29sbGFwc2VkID0gdG9yY2guemVyb3MoNjQsIDIwKVxuYXZnX2tsLCBuX2NvbGxhcHNlZCwgbl9hY3RpdmUgPSBkZXRlY3RfcG9zdGVyaW9yX2NvbGxhcHNlKG11X2NvbGxhcHNlZCwgbG9ndmFyX2NvbGxhcHNlZClcbnByaW50KGZcdTAwMjdQb3N0ZXJpb3IgY29sbGFwc2U6IHtuX2NvbGxhcHNlZH0vMjAgZGltcyBjb2xsYXBzZWQsIHtuX2FjdGl2ZX0gYWN0aXZlXHUwMDI3KVxuZm9yIHN0ZXAgaW4gWzAsIDUwMCwgMTAwMCwgMjUwMCwgMzAwMF06XG4gICAgdyA9IGN5Y2xpY2FsX2tsX3dlaWdodChzdGVwLCBuX2N5Y2xlcz00LCBtYXhfc3RlcHM9NDAwMClcbiAgICBwcmludChmXHUwMDI3ICBTdGVwIHtzdGVwOjRkfTogY3ljbGljYWwgS0wgd2VpZ2h0ID0ge3c6LjNmfVx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IlBvc3RlcmlvciBDb2xsYXBzZSBXYXJuaW5nIiwiY29udGVudCI6IklmIHRoZSBLTCB0ZXJtIGRyb3BzIHRvIG5lYXIgemVybyBhZnRlciB0aGUgZmlyc3QgZmV3IGh1bmRyZWQgc3RlcHMgYW5kIHJlY29uc3RydWN0aW9uIGxvc3MgcGxhdGVhdXMsIHRoZSBkZWNvZGVyIGlzIGlnbm9yaW5nIHRoZSBsYXRlbnQgc3BhY2UuIERpYWdub3NlIGJ5IG1vbml0b3JpbmcgcGVyLWRpbWVuc2lvbiBLTDsgYW55IGRpbWVuc2lvbiBiZWxvdyAwLjEgbmF0cyBpcyBlZmZlY3RpdmVseSBjb2xsYXBzZWQuIEltbWVkaWF0ZSBmaXhlczogcmVkdWNlIGRlY29kZXIgY2FwYWNpdHksIGFkZCBmcmVlIGJpdHMgKM67PTLigJM0KSwgb3Igc3dpdGNoIHRvIGN5Y2xpY2FsIEtMIGFubmVhbGluZy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiRUxCTyBUZXJtIiwiTWF0aGVtYXRpY2FsIEZvcm0iLCJSb2xlIiwiQ29sbGFwc2UgRml4IiwizrItVkFFIEFkanVzdG1lbnQiXSwicm93cyI6W1siUmVjb25zdHJ1Y3Rpb24iLCJFX3txfVtsb2cgcF/OuCh4fHopXSIsIk1lYXN1cmVzIGhvdyB3ZWxsIGRlY29kZXIgcmVjb3ZlcnMgeCIsIlJlZHVjZSBkZWNvZGVyIGNhcGFjaXR5IiwiVW5jaGFuZ2VkICjOsiBvbmx5IHNjYWxlcyBLTCkiXSxbIktMIERpdmVyZ2VuY2UiLCItS0wocV/Phih6fHgpIHx8IHAoeikpIiwiUmVndWxhcml6ZXMgcG9zdGVyaW9yIHRvd2FyZCBwcmlvciBOKDAsSSkiLCJGcmVlIGJpdHM6IGNsYW1wIEtMIOKJpSDOuyBwZXIgZGltIiwiU2NhbGVkIGJ5IM6yOiDOssK3S0wgdGVybSJdLFsiRUxCTyBHYXAiLCJLTChxX8+GKHp8eCkgfHwgcCh6fHgpKSIsIlRpZ2h0bmVzcyBvZiBib3VuZCAodW5vYnNlcnZhYmxlKSIsIkJldHRlciBxIGNhcGFjaXR5IG5hcnJvd3MgZ2FwIiwiTGFyZ2VyIM6yIHdpZGVucyBnYXAgaW50ZW50aW9uYWxseSJdLFsizrJcdTAwM2UxIFByZXNzdXJlIiwiVHJhZGVzIHJlY29uIGZvciBkaXNlbnRhbmdsZW1lbnQiLCJFbmNvdXJhZ2VzIGluZGVwZW5kZW50IGxhdGVudCBkaW1zIiwiQ3ljbGljYWwgYW5uZWFsaW5nOiDOsiByaXNlcyAw4oaSMSByZXBlYXRlZGx5IiwiQ29yZSBtZWNoYW5pc20gb2YgzrItVkFFIl0sWyJGcmVlIEJpdHMgzrsiLCJtYXgoS0xfZCwgzrspIHBlciBkaW1lbnNpb24iLCJFbnN1cmVzIGVhY2ggZGltIGVuY29kZXMg4omlzrsgbmF0cyIsIlByZXZlbnRzIEtM4oaSMCBjb2xsYXBzZSIsIkNvbWJpbmVkIHdpdGggzrIgZm9yIGJlc3QgcmVzdWx0cyJdXX0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUaGUgcmVwYXJhbWV0ZXJpemF0aW9uIHRyaWNrIHdvcmtzIGJlY2F1c2UgeiA9IM68ICsgz4PCt861IHNlcGFyYXRlcyB0aGUgcmFuZG9tbmVzcyAozrUpIGZyb20gdGhlIHBhcmFtZXRlcnMgKM68LCDPgyksIGVuYWJsaW5nIGJhY2twcm9wIHRocm91Z2ggei4iLCJGb3IgZGlhZ29uYWwgR2F1c3NpYW4gcSBhbmQgc3RhbmRhcmQgR2F1c3NpYW4gcCwgdGhlIEtMIGhhcyB0aGUgY2xvc2VkIGZvcm06IC3CvSDOoygxICsgbG9nIM+DwrIgLSDOvMKyIC0gz4PCsikuIiwiQmVybm91bGxpIGRlY29kZXIgdXNlcyBCQ0UgbG9zczsgR2F1c3NpYW4gZGVjb2RlciB1c2VzIE1TRSBsb3NzIOKAlCB0aGUgY2hvaWNlIGNoYW5nZXMgdGhlIHNjYWxlIG9mIHRoZSByZWNvbnN0cnVjdGlvbiB0ZXJtLiIsIlBvc3RlcmlvciBjb2xsYXBzZSBpcyBtb3N0IGNvbW1vbiB3aXRoIGF1dG9yZWdyZXNzaXZlIGRlY29kZXJzIChMU1RNLCBUcmFuc2Zvcm1lcikgdGhhdCBhcmUgZXhwcmVzc2l2ZSBlbm91Z2ggdG8gbW9kZWwgcCh4KSB3aXRob3V0IHouIiwiQ3ljbGljYWwgYW5uZWFsaW5nIG91dHBlcmZvcm1zIG1vbm90b25pYyBhbm5lYWxpbmcgYmVjYXVzZSBlYWNoIGN5Y2xlIHJlc2V0cyB0aGUgZW5jb2RlciB0byBleHBsb3JlIG5ldyBsYXRlbnQgdXNlcy4iXX0seyJ0eXBlIjoiZGl2aWRlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFZBRSBmcmFtZXdvcmsgcHJvdmlkZXMgYSBwcmluY2lwbGVkIHByb2JhYmlsaXN0aWMgZ2VuZXJhdGl2ZSBtb2RlbCB3aXRoIGEgdHJhY3RhYmxlIHRyYWluaW5nIG9iamVjdGl2ZS4gVW5kZXJzdGFuZGluZyB0aGUgRUxCTyBkZXJpdmF0aW9uIGNsYXJpZmllcyB3aHkgdGhlIHJlY29uc3RydWN0aW9uLUtMIHRyYWRlb2ZmIGV4aXN0cyBhbmQgd2hhdCBlYWNoIHRlcm0gb3B0aW1pemVzLiBUaGUgcmVwYXJhbWV0ZXJpemF0aW9uIHRyaWNrIGlzIHRoZSBjb3JlIHRlY2huaWNhbCBpbnNpZ2h0IGVuYWJsaW5nIGVuZC10by1lbmQgZ3JhZGllbnQgZmxvdy4gUG9zdGVyaW9yIGNvbGxhcHNlIHJlbWFpbnMgdGhlIG1haW4gZmFpbHVyZSBtb2RlIHRvIG1vbml0b3IgaW4gcHJhY3RpY2UsIHdpdGggY3ljbGljYWwgYW5uZWFsaW5nIGFuZCBmcmVlIGJpdHMgYXMgdGhlIG1vc3QgcmVsaWFibGUgcmVtZWRpZXMuIn1d"
---
# VAE — ELBO Derivation and Reparameterization Trick

Variational Autoencoders (Kingma & Welling 2013) are latent variable models that jointly learn to compress data into a continuous latent space and generate data from that space. The generative model is p(x,z) = p(x|z)p(z) where p(z) = N(0,I) is the prior and p_θ(x|z) is a learned decoder. The inference model q_φ(z|x) approximates the intractable posterior p(z|x). Training maximizes a lower bound on log p(x) called the ELBO, derived by introducing q and applying Jensen's inequality. The reparameterization trick converts the stochastic sampling step into a differentiable operation, allowing gradient-based optimization of both the encoder φ and decoder θ simultaneously.

## ELBO Derivation

Starting from log p(x) and introducing q_φ(z|x) via importance weighting: log p(x) = log ∫ p(x|z)p(z) dz = log E_{q_φ}[p(x|z)p(z)/q_φ(z|x)] ≥ E_{q_φ}[log p(x|z)] + E_{q_φ}[log p(z)/q_φ(z|x)] = E_{q_φ}[log p(x|z)] - KL(q_φ(z|x) || p(z)). The gap between log p(x) and the ELBO is KL(q_φ(z|x) || p(z|x)) ≥ 0, so ELBO ≤ log p(x). Maximizing the ELBO simultaneously maximizes a lower bound on the marginal likelihood and minimizes the KL divergence between the variational posterior and the true posterior.

## Reparameterization Trick

The ELBO requires computing gradients through E_{q_φ}[log p(x|z)], but z ~ q_φ(z|x) = N(μ_φ(x), σ_φ²(x)) is a stochastic node — naively, gradients cannot flow through the sampling operation. The reparameterization trick factors z = μ_φ(x) + σ_φ(x) ⊙ ε where ε ~ N(0,I). Now z is a deterministic function of the parameters μ_φ, σ_φ and the auxiliary noise ε. Gradients of the loss with respect to φ flow through z = μ + σ·ε cleanly via backpropagation. The encoder outputs μ (mean) and log σ² (log variance) for numerical stability, and σ = exp(0.5 · log σ²).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class VAEEncoder(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=512, latent_dim=20):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc_mu  = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

    def forward(self, x):
        h = F.relu(self.fc1(x.view(x.size(0), -1)))
        return self.fc_mu(h), self.fc_logvar(h)

class VAEDecoder(nn.Module):
    def __init__(self, latent_dim=20, hidden_dim=512, output_dim=784):
        super().__init__()
        self.fc1 = nn.Linear(latent_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, z):
        h = F.relu(self.fc1(z))
        return torch.sigmoid(self.fc2(h))

class VAE(nn.Module):
    def __init__(self, latent_dim=20):
        super().__init__()
        self.encoder = VAEEncoder(latent_dim=latent_dim)
        self.decoder = VAEDecoder(latent_dim=latent_dim)

    def reparameterize(self, mu, logvar):
        """z = mu + std * eps; eps ~ N(0, I) — differentiable sampling."""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + std * eps

    def forward(self, x):
        mu, logvar = self.encoder(x)
        z = self.reparameterize(mu, logvar)
        recon = self.decoder(z)
        return recon, mu, logvar

model = VAE(latent_dim=2)
x = torch.randn(8, 1, 28, 28)
recon, mu, logvar = model(x)
print(f'Encoder mu: {mu.shape}, logvar: {logvar.shape}')
print(f'Decoder recon: {recon.shape}')
```

## ELBO Loss — Reconstruction and KL Terms

The ELBO has two terms. The reconstruction term E_{q_φ}[log p_θ(x|z)] measures how well the decoder recovers x from z. For a Bernoulli decoder (binary images), this is binary cross-entropy; for a Gaussian decoder, it is mean squared error. The KL term -KL(q_φ(z|x) || p(z)) regularizes the posterior toward the prior N(0,I). For diagonal Gaussian encoder and standard Gaussian prior, the KL has a closed form: KL = -½ Σⱼ (1 + log σⱼ² - μⱼ² - σⱼ²). The closed form avoids Monte Carlo estimation of the KL, reducing gradient variance and making training more stable.

```python
import torch
import torch.nn.functional as F

def vae_loss(recon, x, mu, logvar, beta=1.0):
    """
    ELBO loss = reconstruction_loss + beta * KL_divergence.
    recon: (B, 784) sigmoid outputs.
    x:     (B, 1, 28, 28) input images in [0, 1].
    mu, logvar: (B, latent_dim) encoder outputs.
    KL closed form: -0.5 * sum(1 + logvar - mu^2 - exp(logvar)).
    """
    x_flat = x.view(x.size(0), -1)
    # Bernoulli reconstruction: binary cross-entropy summed over pixels
    recon_loss = F.binary_cross_entropy(recon, x_flat, reduction='sum') / x.size(0)
    # KL divergence: analytical for q=N(mu, diag(sigma^2)) and p=N(0,I)
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=1)
    kl_loss = kl.mean()
    total = recon_loss + beta * kl_loss
    return total, recon_loss.item(), kl_loss.item()

# Sanity check at init: KL of N(0,I) vs N(0,I) should be 0
mu_zero    = torch.zeros(16, 20)
logvar_zero = torch.zeros(16, 20)
recon_dummy = torch.rand(16, 784)
x_dummy = torch.rand(16, 1, 28, 28)
total, recon_l, kl_l = vae_loss(recon_dummy, x_dummy, mu_zero, logvar_zero)
print(f'At init (mu=0, logvar=0): KL={kl_l:.4f} (expected ~0.0)')
print(f'Total ELBO loss: {total:.4f}  | Recon: {recon_l:.4f}  | KL: {kl_l:.4f}')
```

## Gaussian vs Bernoulli Decoder Choice

The decoder output distribution determines the form of the reconstruction term. A Bernoulli decoder (sigmoid output, BCE loss) is standard for binarized MNIST: each pixel is treated as an independent Bernoulli variable. A Gaussian decoder (linear output, MSE loss) is more appropriate for continuous images; the reconstruction term becomes E_{q}[-||x - μ_θ(z)||²/(2σ²)], where the decoder variance σ² can be fixed at 1 (equivalent to MSE) or learned. A learned σ² allows the model to adapt its reconstruction confidence per region. For natural images, a Laplace decoder (MAE loss, more robust to outliers) or a discretized logistic mixture (PixelCNN++ style) can improve sample sharpness over plain Gaussian decoders.

- Bernoulli decoder: sigmoid output + BCE loss — standard for binarized MNIST, assumes independent pixels.
- Gaussian decoder: linear output + MSE — appropriate for continuous images; equivalent to maximizing N(x; μ_θ(z), I).
- Discretized logistic decoder: more expressive output, used in PixelCNN++ and VQ-VAE to improve sharpness.
- Fixed decoder variance σ²=1 simplifies training; learned σ² helps the model weight reconstruction confidence.
- The choice of decoder distribution changes the scale of the reconstruction term relative to KL — affects effective β.

## Visualizing the 2D Latent Space

A 2-dimensional latent space allows direct visualization of the learned representation. After training, encoding the MNIST test set and plotting the (μ₁, μ₂) values colored by digit class reveals cluster structure. Traversing the latent space by decoding points on a grid shows smooth interpolation between digit styles. This confirms that the VAE has organized the latent space semantically and that the decoder can generate coherent images from any point in the continuous prior.

```python
import torch
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

def visualize_latent_space(model, device='cpu', n_samples=2000):
    """Plot 2D latent space of VAE trained on MNIST, colored by digit class."""
    model.eval()
    transform = transforms.Compose([transforms.ToTensor()])
    dataset = datasets.MNIST(root='/tmp/mnist', train=False, download=True, transform=transform)
    loader = torch.utils.data.DataLoader(dataset, batch_size=256, shuffle=False)
    zs, labels = [], []
    with torch.no_grad():
        for x, y in loader:
            mu, _ = model.encoder(x.to(device))
            zs.append(mu.cpu().numpy())
            labels.append(y.numpy())
            if sum(len(l) for l in labels) >= n_samples:
                break
    zs = np.concatenate(zs)[:n_samples]
    labels = np.concatenate(labels)[:n_samples]
    fig, ax = plt.subplots(figsize=(7, 6))
    scatter = ax.scatter(zs[:, 0], zs[:, 1], c=labels, cmap='tab10', alpha=0.6, s=6)
    plt.colorbar(scatter, ax=ax, label='Digit class')
    ax.set_xlabel('z₁'); ax.set_ylabel('z₂'); ax.set_title('VAE 2D Latent Space — MNIST')
    plt.tight_layout(); plt.savefig('/tmp/vae_latent.png', dpi=120)
    print('Saved latent space plot to /tmp/vae_latent.png')
    return zs, labels

from torch import nn
class MinimalVAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Flatten(), nn.Linear(784,256), nn.ReLU())
        self.fc_mu = nn.Linear(256, 2)
        self.fc_logvar = nn.Linear(256, 2)
        self.decoder = nn.Sequential(nn.Linear(2,256), nn.ReLU(), nn.Linear(256,784), nn.Sigmoid())
    def reparameterize(self, mu, logvar):
        return mu + torch.exp(0.5 * logvar) * torch.randn_like(mu)
    def forward(self, x):
        h = self.encoder(x)
        mu, logvar = self.fc_mu(h), self.fc_logvar(h)
        return self.decoder(self.reparameterize(mu, logvar)), mu, logvar
print('2D VAE ready for visualization')
```

## Posterior Collapse and Cyclical KL Annealing

Posterior collapse occurs when the decoder becomes so powerful that it ignores the latent code z entirely. The encoder outputs q_φ(z|x) ≈ p(z) = N(0,I) for all x, driving KL → 0 while the reconstruction loss stagnates. This is especially common with autoregressive decoders (RNN, Transformer) that can model p(x) without z. The free bits heuristic sets a minimum KL per dimension λ (typically 2–4 bits), and β-VAE increases the KL weight. Cyclical KL annealing (Fu et al. 2019) schedules the KL weight as a sawtooth that rises from 0 to 1 multiple times per training run, periodically resetting the encoder to explore different latent uses before the decoder adapts.

```python
import torch
import torch.nn as nn
import numpy as np

def cyclical_kl_weight(step, n_cycles=4, ratio=0.5, max_steps=10000):
    """Sawtooth KL weight schedule: rise from 0 to 1 n_cycles times over training."""
    cycle_len = max_steps // n_cycles
    cycle_pos = step % cycle_len
    ramp_end  = int(cycle_len * ratio)
    if cycle_pos < ramp_end:
        return cycle_pos / ramp_end
    return 1.0

def free_bits_kl(kl_per_dim, lambda_fb=3.0):
    """Free bits: clamp per-dimension KL below lambda_fb to prevent collapse."""
    return torch.clamp(kl_per_dim, min=lambda_fb).sum(dim=-1).mean()

def detect_posterior_collapse(mu, logvar, threshold=0.05):
    """Flag latent dims where KL contribution is below threshold (collapsed)."""
    kl_per_dim = -0.5 * (1 + logvar - mu.pow(2) - logvar.exp())
    avg_kl = kl_per_dim.mean(dim=0)
    collapsed = (avg_kl < threshold).sum().item()
    active    = (avg_kl >= threshold).sum().item()
    return avg_kl, collapsed, active

# Simulate collapse scenario
torch.manual_seed(42)
mu_collapsed    = torch.randn(64, 20) * 0.01
logvar_collapsed = torch.zeros(64, 20)
avg_kl, n_collapsed, n_active = detect_posterior_collapse(mu_collapsed, logvar_collapsed)
print(f'Posterior collapse: {n_collapsed}/20 dims collapsed, {n_active} active')
for step in [0, 500, 1000, 2500, 3000]:
    w = cyclical_kl_weight(step, n_cycles=4, max_steps=4000)
    print(f'  Step {step:4d}: cyclical KL weight = {w:.3f}')
```

> **Posterior Collapse Warning**: If the KL term drops to near zero after the first few hundred steps and reconstruction loss plateaus, the decoder is ignoring the latent space. Diagnose by monitoring per-dimension KL; any dimension below 0.1 nats is effectively collapsed. Immediate fixes: reduce decoder capacity, add free bits (λ=2–4), or switch to cyclical KL annealing.

| ELBO Term | Mathematical Form | Role | Collapse Fix | β-VAE Adjustment |
| --- | --- | --- | --- | --- |
| Reconstruction | E_{q}[log p_θ(x|z)] | Measures how well decoder recovers x | Reduce decoder capacity | Unchanged (β only scales KL) |
| KL Divergence | -KL(q_φ(z|x) || p(z)) | Regularizes posterior toward prior N(0,I) | Free bits: clamp KL ≥ λ per dim | Scaled by β: β·KL term |
| ELBO Gap | KL(q_φ(z|x) || p(z|x)) | Tightness of bound (unobservable) | Better q capacity narrows gap | Larger β widens gap intentionally |
| β>1 Pressure | Trades recon for disentanglement | Encourages independent latent dims | Cyclical annealing: β rises 0→1 repeatedly | Core mechanism of β-VAE |
| Free Bits λ | max(KL_d, λ) per dimension | Ensures each dim encodes ≥λ nats | Prevents KL→0 collapse | Combined with β for best results |

- The reparameterization trick works because z = μ + σ·ε separates the randomness (ε) from the parameters (μ, σ), enabling backprop through z.
- For diagonal Gaussian q and standard Gaussian p, the KL has the closed form: -½ Σ(1 + log σ² - μ² - σ²).
- Bernoulli decoder uses BCE loss; Gaussian decoder uses MSE loss — the choice changes the scale of the reconstruction term.
- Posterior collapse is most common with autoregressive decoders (LSTM, Transformer) that are expressive enough to model p(x) without z.
- Cyclical annealing outperforms monotonic annealing because each cycle resets the encoder to explore new latent uses.

---

The VAE framework provides a principled probabilistic generative model with a tractable training objective. Understanding the ELBO derivation clarifies why the reconstruction-KL tradeoff exists and what each term optimizes. The reparameterization trick is the core technical insight enabling end-to-end gradient flow. Posterior collapse remains the main failure mode to monitor in practice, with cyclical annealing and free bits as the most reliable remedies.

