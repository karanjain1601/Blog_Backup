---
title: "VQ-VAE — Vector Quantization and Discrete Latent Spaces"
slug: "vq-vae"
description: "A deep dive into VQ-VAE: how vector quantization replaces continuous latents with discrete codebook lookups, enabling two-stage generation with autoregressive priors and powering VQGAN, DALL-E, and FSQ."
tags: ["deep-learning", "generative-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkludHJvZHVjdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVlEtVkFFICh2YW4gZGVuIE9vcmQgZXQgYWwuLCAyMDE3KSByZXBsYWNlcyB0aGUgY29udGludW91cyBHYXVzc2lhbiBsYXRlbnQgb2YgYSBzdGFuZGFyZCBWQUUgd2l0aCBhICoqZGlzY3JldGUgY29kZWJvb2sqKiBvZiBLIGxlYXJuZWQgZW1iZWRkaW5nIHZlY3RvcnMgRSA9IHtl4oKBLCDigKYsIGVfS30g4oiIIOKEnV5ELiBJbnN0ZWFkIG9mIHNhbXBsaW5nIGZyb20gYSBkaXN0cmlidXRpb24sIHRoZSBlbmNvZGVyIG91dHB1dCB6X2UoeCkgaXMgc25hcHBlZCB0byBpdHMgbmVhcmVzdCBjb2RlYm9vayBlbnRyeSwgcHJvZHVjaW5nIGEgc3RydWN0dXJlZCBzeW1ib2xpYyByZXByZXNlbnRhdGlvbi4gVGhpcyBzaWRlc3RlcHMgcG9zdGVyaW9yIGNvbGxhcHNlICh0aGUgZW5jb2RlciBpZ25vcmluZyB0aGUgbGF0ZW50KSBhbmQgdGhlIGJsdXJyaW5nIGNhdXNlZCBieSBhdmVyYWdpbmcgb3ZlciBjb250aW51b3VzIHVuY2VydGFpbnR5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGNvcmUgZGVzaWduIHBoaWxvc29waHkgaXMgdG8gZGVjb3VwbGUgcmVwcmVzZW50YXRpb24gZnJvbSBnZW5lcmF0aW9uLiBWUS1WQUUgbGVhcm5zIGEgY29tcGFjdCBkaXNjcmV0ZSBjb2RlIHBlciBpbnB1dDsgYSBzZXBhcmF0ZSBhdXRvcmVncmVzc2l2ZSBtb2RlbCAoUGl4ZWxDTk4sIFRyYW5zZm9ybWVyKSB0aGVuIGxlYXJucyBhIHByaW9yIG92ZXIgdGhvc2UgY29kZXMuIFRoaXMgdHdvLXN0YWdlIGFwcHJvYWNoIHVuZGVycGlucyBEQUxMLUUsIFZRR0FOLCBBdWRpb0xNLCBhbmQgTXVzaWNMTS4gVGhlIGRpc2NyZXRlIGJvdHRsZW5lY2sgZm9yY2VzIHRoZSBtb2RlbCB0byBjb21taXQgdG8gbWVhbmluZ2Z1bCwgcmV1c2FibGUgc3ltYm9saWMgdW5pdHMgcmF0aGVyIHRoYW4gc21lYXJpbmcgaW5mb3JtYXRpb24gYWNyb3NzIGEgY29udGludW91cyBtYW5pZm9sZC4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWZWN0b3IgUXVhbnRpemF0aW9uIE1hdGhlbWF0aWNzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZW5jb2RlciBtYXBzIGlucHV0IHggdG8gYSBjb250aW51b3VzIGZlYXR1cmUgbWFwIHpfZSh4KSDiiIgg4oSdXkQuIFF1YW50aXphdGlvbiBtYXBzIGVhY2ggc3BhdGlhbCBwb3NpdGlvbiB0byB0aGUgbmVhcmVzdCBjb2RlYm9vayB2ZWN0b3I6IHpfcSA9IGVfayB3aGVyZSBrID0gYXJnbWlu4oCWel9lIOKIkiBlX2nigJbCsi4gVGhlIHRvdGFsIFZRLVZBRSBsb3NzIGNvbWJpbmVzIHRocmVlIHRlcm1zOiByZWNvbnN0cnVjdGlvbiAocGl4ZWwtbGV2ZWwgTVNFIGJldHdlZW4gaW5wdXQgYW5kIGRlY29kZXIgb3V0cHV0KSwgY29kZWJvb2sgbG9zcyAobW92ZXMgY29kZWJvb2sgZW50cmllcyB0b3dhcmQgZW5jb2RlciBvdXRwdXRzIHVzaW5nIHN0b3AtZ3JhZGllbnQgb24gel9lKSwgYW5kIGNvbW1pdG1lbnQgbG9zcyAocHVzaGVzIHRoZSBlbmNvZGVyIHRvd2FyZCB0aGUgY2hvc2VuIGNvZGUgdXNpbmcgc3RvcC1ncmFkaWVudCBvbiB6X3EpLiBUaGUgc3RvcC1ncmFkaWVudCBzZygpIHBhc3NlcyB2YWx1ZXMgZm9yd2FyZCBidXQgYmxvY2tzIGFsbCBncmFkaWVudHMgYmFja3dhcmQuIn0seyJ0eXBlIjoibWF0aCIsImRpc3BsYXkiOnRydWUsImNvbnRlbnQiOiJcXFxcbWF0aGNhbHtMfSA9IFxcXFx8eCAtIFxcXFxoYXR7eH1cXFxcfF4yICsgXFxcXHxcXFxcbWF0aHJte3NnfSh6X2UpIC0gel9xXFxcXHxeMiArIFxcXFxiZXRhXFxcXCxcXFxcfHpfZSAtIFxcXFxtYXRocm17c2d9KHpfcSlcXFxcfF4yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY29tbWl0bWVudCB3ZWlnaHQgzrIg4omIIDAuMjUgY29udHJvbHMgaG93IHN0cm9uZ2x5IHRoZSBlbmNvZGVyIGlzIHB1c2hlZCB0byBzdGF5IG5lYXIgaXRzIGNob3NlbiBjb2RlYm9vayBlbnRyeS4gV2l0aG91dCBpdCwgdGhlIGVuY29kZXIgY2FuIGRyaWZ0IGJldHdlZW4gbXVsdGlwbGUgZW50cmllcyBkdXJpbmcgdHJhaW5pbmcsIHByb2R1Y2luZyB1bnN0YWJsZSBjb2RlIGFzc2lnbm1lbnRzIGFuZCBzbG93IGNvbnZlcmdlbmNlLiBUaGUgY29kZWJvb2sgYW5kIGNvbW1pdG1lbnQgbG9zc2VzIGFyZSBjb21wbGVtZW50YXJ5OiBjb2RlYm9vayBsb3NzIG1vdmVzIHRoZSBkaWN0aW9uYXJ5OyBjb21taXRtZW50IGxvc3MgYW5jaG9ycyB0aGUgZW5jb2Rlci4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTdHJhaWdodC1UaHJvdWdoIEdyYWRpZW50IEVzdGltYXRvciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGFyZ21pbiBvcGVyYXRpb24gaGFzIHplcm8gZGVyaXZhdGl2ZSBhbG1vc3QgZXZlcnl3aGVyZSBhbmQgaXMgdW5kZWZpbmVkIGF0IHRoZSBib3VuZGFyaWVzIGJldHdlZW4gVm9yb25vaSBjZWxscy4gSXQgY2Fubm90IGJlIGRpZmZlcmVudGlhdGVkIHRocm91Z2ggZGlyZWN0bHksIHNvIGdyYWRpZW50cyBmcm9tIHRoZSBkZWNvZGVyIGNhbm5vdCByZWFjaCB0aGUgZW5jb2Rlci4gVGhlIHN0cmFpZ2h0LXRocm91Z2ggZXN0aW1hdG9yIChCZW5naW8gZXQgYWwuLCAyMDEzKSByZXNvbHZlcyB0aGlzIGJ5IHNpbXBseSBjb3B5aW5nIGdyYWRpZW50cyBmcm9tIHRoZSBkZWNvZGVyIGlucHV0IHpfcSBiYWNrIHRvIHRoZSBlbmNvZGVyIG91dHB1dCB6X2UsIGJ5cGFzc2luZyB0aGUgbm9uLWRpZmZlcmVudGlhYmxlIHF1YW50aXphdGlvbi4gSW4gY29kZSB0aGlzIGlzIG9uZSBsaW5lOiB6X3Ffc3QgPSB6X2UgKyAoel9xIC0gel9lKS5kZXRhY2goKS4gVGhlIC5kZXRhY2goKSBtYWtlcyAoel9xIC0gel9lKSBhIGNvbnN0YW50IGluIHRoZSBiYWNrd2FyZCBwYXNzLCBzbyBhbGwgZ3JhZGllbnQgZmxvd3MgdGhyb3VnaCB6X2Ugb25seSwgYXMgaWYgel9xIGFuZCB6X2Ugd2VyZSBpZGVudGljYWwuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFZlY3RvclF1YW50aXplcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBudW1fZW1iZWRkaW5ncywgZW1iZWRkaW5nX2RpbSwgY29tbWl0bWVudF9jb3N0PTAuMjUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5lbWJlZGRpbmdfZGltID0gZW1iZWRkaW5nX2RpbVxuICAgICAgICBzZWxmLm51bV9lbWJlZGRpbmdzID0gbnVtX2VtYmVkZGluZ3NcbiAgICAgICAgc2VsZi5jb21taXRtZW50X2Nvc3QgPSBjb21taXRtZW50X2Nvc3RcbiAgICAgICAgc2VsZi5lbWJlZGRpbmdzID0gbm4uRW1iZWRkaW5nKG51bV9lbWJlZGRpbmdzLCBlbWJlZGRpbmdfZGltKVxuICAgICAgICBubi5pbml0LnVuaWZvcm1fKHNlbGYuZW1iZWRkaW5ncy53ZWlnaHQsIC0xL251bV9lbWJlZGRpbmdzLCAxL251bV9lbWJlZGRpbmdzKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgel9lKTpcbiAgICAgICAgIyB6X2U6IChCLCBELCBILCBXKSAtXHUwMDNlIGZsYXR0ZW4gc3BhdGlhbCBkaW1zIHRvIChCKkgqVywgRClcbiAgICAgICAgel9lX2ZsYXQgPSB6X2UucGVybXV0ZSgwLCAyLCAzLCAxKS5yZXNoYXBlKC0xLCBzZWxmLmVtYmVkZGluZ19kaW0pXG4gICAgICAgICMgU3F1YXJlZCBMMiBkaXN0YW5jZXMgdmlhIGV4cGFuc2lvbjogfHxhLWJ8fF4yID0gfHxhfHxeMiAtIDJhKmJeVCArIHx8Ynx8XjJcbiAgICAgICAgZGlzdGFuY2VzID0gKHpfZV9mbGF0LnBvdygyKS5zdW0oMSwga2VlcGRpbT1UcnVlKVxuICAgICAgICAgICAgICAgICAgICAgLSAyICogel9lX2ZsYXQgQCBzZWxmLmVtYmVkZGluZ3Mud2VpZ2h0LlRcbiAgICAgICAgICAgICAgICAgICAgICsgc2VsZi5lbWJlZGRpbmdzLndlaWdodC5wb3coMikuc3VtKDEpKVxuICAgICAgICBpbmRpY2VzID0gZGlzdGFuY2VzLmFyZ21pbihkaW09MSkgICAgICAgICAgICMgbmVhcmVzdCBjb2RlYm9vayBlbnRyeVxuICAgICAgICB6X3FfZmxhdCA9IHNlbGYuZW1iZWRkaW5ncyhpbmRpY2VzKVxuICAgICAgICB6X3EgPSB6X3FfZmxhdC5yZXNoYXBlKHpfZS5zaGFwZVswXSwgel9lLnNoYXBlWzJdLCB6X2Uuc2hhcGVbM10sIC0xKS5wZXJtdXRlKDAsIDMsIDEsIDIpXG4gICAgICAgIGNvZGVib29rX2xvc3MgPSBGLm1zZV9sb3NzKHpfcSwgel9lLmRldGFjaCgpKSAgICAgIyBtb3ZlIGNvZGVzIHRvd2FyZCBlbmNvZGVyXG4gICAgICAgIGNvbW1pdG1lbnRfbG9zcyA9IEYubXNlX2xvc3Moel9lLCB6X3EuZGV0YWNoKCkpICAgIyBtb3ZlIGVuY29kZXIgdG93YXJkIGNvZGVzXG4gICAgICAgIGxvc3MgPSBjb2RlYm9va19sb3NzICsgc2VsZi5jb21taXRtZW50X2Nvc3QgKiBjb21taXRtZW50X2xvc3NcbiAgICAgICAgel9xX3N0ID0gel9lICsgKHpfcSAtIHpfZSkuZGV0YWNoKCkgICAgICAgIyBzdHJhaWdodC10aHJvdWdoIGVzdGltYXRvclxuICAgICAgICByZXR1cm4gel9xX3N0LCBsb3NzLCBpbmRpY2VzIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29kZWJvb2sgTGVhcm5pbmcgd2l0aCBFTUEifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ikluc3RlYWQgb2YgZ3JhZGllbnQgZGVzY2VudCBvbiB0aGUgY29kZWJvb2sgbG9zcywgdGhlIFZRLVZBRSBwYXBlciByZWNvbW1lbmRzIGV4cG9uZW50aWFsIG1vdmluZyBhdmVyYWdlIChFTUEpIHVwZGF0ZXMgYXMgYSBtb3JlIHN0YWJsZSBhbHRlcm5hdGl2ZS4gRm9yIGVhY2ggY29kZWJvb2sgZW50cnkgZV9pLCBtYWludGFpbiBhIHJ1bm5pbmcgY291bnQgbl9pIG9mIGFzc2lnbm1lbnRzIGFuZCBhIHJ1bm5pbmcgZW1iZWRkaW5nIHN1bSBtX2kuIEFmdGVyIGVhY2ggYmF0Y2gsIHVwZGF0ZSB3aXRoIGRlY2F5IM6zIOKJiCAwLjk5OiBuX2kg4oaQIM6zbl9pICsgKDHiiJLOsynCt2NvdW50KGkpLCBhbmQgbV9pIOKGkCDOs21faSArICgx4oiSzrMpwrdzdW0oel9lIGFzc2lnbmVkIHRvIGkpLCB0aGVuIHNldCBlX2kgPSBtX2kgLyBuX2kuIFRoaXMgaXMgb25saW5lIGstbWVhbnMuIEl0IGF2b2lkcyB0aGUgaW50ZXJhY3Rpb24gYmV0d2VlbiBjb2RlYm9vayBncmFkaWVudCB1cGRhdGVzIGFuZCB0aGUgZW5jb2RlciBncmFkaWVudCwgbGVhZGluZyB0byBmYXN0ZXIgY29udmVyZ2VuY2UgYW5kIGZld2VyIGRlYWQgY29kZXMgaW4gcHJhY3RpY2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFZlY3RvclF1YW50aXplckVNQShubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBudW1fZW1iZWRkaW5ncywgZW1iZWRkaW5nX2RpbSwgZGVjYXk9MC45OSwgY29tbWl0bWVudF9jb3N0PTAuMjUsIGVwcz0xZS01KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuZW1iZWRkaW5nX2RpbSA9IGVtYmVkZGluZ19kaW1cbiAgICAgICAgc2VsZi5udW1fZW1iZWRkaW5ncyA9IG51bV9lbWJlZGRpbmdzXG4gICAgICAgIHNlbGYuY29tbWl0bWVudF9jb3N0ID0gY29tbWl0bWVudF9jb3N0XG4gICAgICAgIHNlbGYuZGVjYXkgPSBkZWNheVxuICAgICAgICBzZWxmLmVwcyA9IGVwc1xuICAgICAgICBlbWJlZGRpbmcgPSB0b3JjaC5yYW5kbihudW1fZW1iZWRkaW5ncywgZW1iZWRkaW5nX2RpbSlcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3ZW1iZWRkaW5nc1x1MDAyNywgZW1iZWRkaW5nKVxuICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1ZmZlcihcdTAwMjdjbHVzdGVyX3NpemVcdTAwMjcsIHRvcmNoLnplcm9zKG51bV9lbWJlZGRpbmdzKSlcbiAgICAgICAgc2VsZi5yZWdpc3Rlcl9idWZmZXIoXHUwMDI3ZW1iZWRfYXZnXHUwMDI3LCBlbWJlZGRpbmcuY2xvbmUoKSlcblxuICAgIGRlZiB1cGRhdGVfZW1hKHNlbGYsIHpfZV9mbGF0LCBpbmRpY2VzKTpcbiAgICAgICAgIyBPbmUtaG90IGVuY29kZSBjb2RlIGFzc2lnbm1lbnRzOiBzaGFwZSAoTiwgSylcbiAgICAgICAgb25lX2hvdCA9IHRvcmNoLnplcm9zKGluZGljZXMuc2hhcGVbMF0sIHNlbGYubnVtX2VtYmVkZGluZ3MsIGRldmljZT16X2VfZmxhdC5kZXZpY2UpXG4gICAgICAgIG9uZV9ob3Quc2NhdHRlcl8oMSwgaW5kaWNlcy51bnNxdWVlemUoMSksIDEpXG4gICAgICAgICMgRU1BIHVwZGF0ZSBmb3IgY2x1c3RlciBzaXplcyBhbmQgZW1iZWRkaW5nIHJ1bm5pbmcgc3Vtc1xuICAgICAgICBzZWxmLmNsdXN0ZXJfc2l6ZS5tdWxfKHNlbGYuZGVjYXkpLmFkZF8oKDEgLSBzZWxmLmRlY2F5KSAqIG9uZV9ob3Quc3VtKDApKVxuICAgICAgICBlbWJlZF9zdW0gPSBvbmVfaG90LlQgQCB6X2VfZmxhdFxuICAgICAgICBzZWxmLmVtYmVkX2F2Zy5tdWxfKHNlbGYuZGVjYXkpLmFkZF8oKDEgLSBzZWxmLmRlY2F5KSAqIGVtYmVkX3N1bSlcbiAgICAgICAgIyBMYXBsYWNlIHNtb290aGluZyBhdm9pZHMgZGl2aXNpb24gYnkgemVybyBmb3IgZW1wdHkgY2x1c3RlcnNcbiAgICAgICAgbiA9IHNlbGYuY2x1c3Rlcl9zaXplLnN1bSgpXG4gICAgICAgIHNtb290aGVkID0gKHNlbGYuY2x1c3Rlcl9zaXplICsgc2VsZi5lcHMpIC8gKG4gKyBzZWxmLm51bV9lbWJlZGRpbmdzICogc2VsZi5lcHMpICogblxuICAgICAgICBzZWxmLmVtYmVkZGluZ3MgPSBzZWxmLmVtYmVkX2F2ZyAvIHNtb290aGVkLnVuc3F1ZWV6ZSgxKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRlYWQgQ29kZSBQcm9ibGVtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbiBwcmFjdGljZSwgbWFueSBjb2RlYm9vayBlbnRyaWVzIHJlY2VpdmUgemVybyBhc3NpZ25tZW50cyB0aHJvdWdob3V0IHRyYWluaW5nIOKAlCB0aGV5IGFyZSBuZXZlciB0aGUgbmVhcmVzdCBuZWlnaGJvdXIgZm9yIGFueSBlbmNvZGVyIG91dHB1dC4gVGhlc2UgKipkZWFkIGNvZGVzKiogd2FzdGUgY29kZWJvb2sgY2FwYWNpdHkgYW5kIHJlZHVjZSB0aGUgZWZmZWN0aXZlIG51bWJlciBvZiBkaXN0aW5jdCByZXByZXNlbnRhdGlvbnMuIENvbW1vbiBzeW1wdG9tczogY29kZWJvb2sgdXRpbGlzYXRpb24gYmVsb3cgNTAlIGFuZCByZWNvbnN0cnVjdGlvbiBxdWFsaXR5IHBsYXRlYXVpbmcgZWFybHkuIERlYWQgY29kZXMgYXJpc2UgYmVjYXVzZSBvbmNlIGEgY29kZSBmYWxscyBiZWhpbmQgaXRzIG5laWdoYm91cnMgZHVlIHRvIHJhbmRvbSBpbml0aWFsaXNhdGlvbiwgaXQgZ2V0cyBubyBncmFkaWVudCBzaWduYWwgb3IgRU1BIHVwZGF0ZSBhbmQgY2FuIG5ldmVyIHJlY292ZXIgb24gaXRzIG93bi4ifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkJhdGNoIFNpemUgV2FybmluZyIsImNvbnRlbnQiOiJFTUEgY29kZWJvb2sgdXBkYXRlcyByZXF1aXJlIGxhcmdlIGJhdGNoIHNpemUgKOKJpTI1NikgdG8gZ2V0IGVub3VnaCBjb2RlIGFzc2lnbm1lbnRzIHBlciBzdGVwIOKAlCBzbWFsbCBiYXRjaGVzIGxlYWQgdG8gZGVhZCBjb2RlIGNvbGxhcHNlLiBXaXRoIGJhdGNoIHNpemUgMzIsIG1vc3QgY29kZXMgcmVjZWl2ZSB6ZXJvIGFzc2lnbm1lbnRzIGluIGFueSBzaW5nbGUgc3RlcCwgY2F1c2luZyB0aGUgRU1BIGNsdXN0ZXIgc2l6ZXMgdG8gZGVjYXkgdG93YXJkIHplcm8gd2l0aG91dCByZWNvdmVyeS4gVXNlIGdyYWRpZW50IGFjY3VtdWxhdGlvbiBvciBpbmNyZWFzZSBiYXRjaCBzaXplIGJlZm9yZSByZWx5aW5nIG9uIEVNQSBjb2RlYm9vayB1cGRhdGVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuY2xhc3MgRGVhZENvZGVNb25pdG9yOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBudW1fZW1iZWRkaW5ncywgdGhyZXNob2xkPTEuMCwgcmVzdGFydF9ldmVyeT01MCk6XG4gICAgICAgIHNlbGYubnVtX2VtYmVkZGluZ3MgPSBudW1fZW1iZWRkaW5nc1xuICAgICAgICBzZWxmLnRocmVzaG9sZCA9IHRocmVzaG9sZCAgICAgICMgY29kZXMgdXNlZCBmZXdlciB0aW1lcyB0aGFuIHRoaXMgYXJlIGRlYWRcbiAgICAgICAgc2VsZi5yZXN0YXJ0X2V2ZXJ5ID0gcmVzdGFydF9ldmVyeSAgIyBjaGVjayBpbnRlcnZhbCBpbiB0cmFpbmluZyBzdGVwc1xuICAgICAgICBzZWxmLnVzYWdlX2NvdW50ID0gdG9yY2guemVyb3MobnVtX2VtYmVkZGluZ3MpXG4gICAgICAgIHNlbGYuc3RlcCA9IDBcblxuICAgIGRlZiB1cGRhdGUoc2VsZiwgaW5kaWNlcyk6XG4gICAgICAgICMgQWNjdW11bGF0ZSBwZXItY29kZSB1c2FnZSBjb3VudHMgZnJvbSB0aGlzIGJhdGNoXG4gICAgICAgIGNvdW50cyA9IHRvcmNoLnplcm9zKHNlbGYubnVtX2VtYmVkZGluZ3MpXG4gICAgICAgIGNvdW50cy5zY2F0dGVyX2FkZF8oMCwgaW5kaWNlcy5mbGF0dGVuKCkuY3B1KCksIHRvcmNoLm9uZXMoaW5kaWNlcy5udW1lbCgpKSlcbiAgICAgICAgc2VsZi51c2FnZV9jb3VudCArPSBjb3VudHNcbiAgICAgICAgc2VsZi5zdGVwICs9IDFcblxuICAgIGRlZiByZXN0YXJ0X2RlYWRfY29kZXMoc2VsZiwgZW1iZWRkaW5ncywgel9lX2ZsYXQpOlxuICAgICAgICAjIE9ubHkgY2hlY2sgYXQgcmVzdGFydF9ldmVyeSBpbnRlcnZhbHMgdG8gcmVkdWNlIG92ZXJoZWFkXG4gICAgICAgIGlmIHNlbGYuc3RlcCAlIHNlbGYucmVzdGFydF9ldmVyeSAhPSAwOlxuICAgICAgICAgICAgcmV0dXJuIDBcbiAgICAgICAgZGVhZF9tYXNrID0gc2VsZi51c2FnZV9jb3VudCBcdTAwM2Mgc2VsZi50aHJlc2hvbGRcbiAgICAgICAgbnVtX2RlYWQgPSBpbnQoZGVhZF9tYXNrLnN1bSgpLml0ZW0oKSlcbiAgICAgICAgaWYgbnVtX2RlYWQgPT0gMDpcbiAgICAgICAgICAgIHNlbGYudXNhZ2VfY291bnQuemVyb18oKVxuICAgICAgICAgICAgcmV0dXJuIDBcbiAgICAgICAgIyBSZWluaXRpYWxpemUgZGVhZCBjb2RlcyB3aXRoIHJhbmRvbSBlbmNvZGVyIG91dHB1dHMgZnJvbSBjdXJyZW50IGJhdGNoXG4gICAgICAgIHBlcm0gPSB0b3JjaC5yYW5kcGVybSh6X2VfZmxhdC5zaGFwZVswXSlbOm51bV9kZWFkXVxuICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICAgICAgICAgIGVtYmVkZGluZ3MuZGF0YVtkZWFkX21hc2tdID0gel9lX2ZsYXRbcGVybV0uZGV0YWNoKClcbiAgICAgICAgc2VsZi51c2FnZV9jb3VudC56ZXJvXygpXG4gICAgICAgIHByaW50KGZcdTAwMjdSZXN0YXJ0ZWQge251bV9kZWFkfSBkZWFkIGNvZGVzIGF0IHN0ZXAge3NlbGYuc3RlcH1cdTAwMjcpXG4gICAgICAgIHJldHVybiBudW1fZGVhZCJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlR3by1TdGFnZSBHZW5lcmF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWUS1WQUUgaXMgb25seSBhbiBhdXRvZW5jb2RlciDigJQgaXQgY2Fubm90IGdlbmVyYXRlIG5vdmVsIHNhbXBsZXMgb24gaXRzIG93bi4gU3RhZ2UgMiB0cmFpbnMgYW4gYXV0b3JlZ3Jlc3NpdmUgbW9kZWwgdG8gbW9kZWwgdGhlIGRpc3RyaWJ1dGlvbiBvZiBkaXNjcmV0ZSBjb2RlIHNlcXVlbmNlcyBwcm9kdWNlZCBieSB0aGUgZW5jb2RlciBvbiB0aGUgdHJhaW5pbmcgc2V0LiBBdCBpbmZlcmVuY2UsIHNhbXBsZSBhIGNvbXBsZXRlIGNvZGUgc2VxdWVuY2UgZnJvbSB0aGUgcHJpb3IsIHRoZW4gcGFzcyBpdCB0aHJvdWdoIHRoZSBWUS1WQUUgZGVjb2RlciB0byBwcm9kdWNlIGFuIGltYWdlLiBUaGUgc2VwYXJhdGlvbiBpcyBhcmNoaXRlY3R1cmFsbHkgcG93ZXJmdWw6IHRoZSBWUS1WQUUgc29sdmVzIHRoZSBoYXJkIHBlcmNlcHR1YWwgcmVjb25zdHJ1Y3Rpb24gcHJvYmxlbSBhdCB0aGUgcGl4ZWwgbGV2ZWw7IHRoZSBwcmlvciBvbmx5IG5lZWRzIHRvIG1vZGVsIGEgc2hvcnQgc2VxdWVuY2Ugb2YgZGlzY3JldGUgdG9rZW5zIHJlcHJlc2VudGluZyBoaWdoLWxldmVsIHN0cnVjdHVyZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRvcmNoLmRpc3RyaWJ1dGlvbnMgaW1wb3J0IENhdGVnb3JpY2FsXG5cbmNsYXNzIFZRVkFFR2VuZXJhdG9yOlxuICAgICMgVHdvLXN0YWdlOiAoMSkgdHJhaW4gVlEtVkFFLCAoMikgdHJhaW4gYXV0b3JlZ3Jlc3NpdmUgcHJpb3Igb24gZGlzY3JldGUgY29kZXNcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZW5jb2RlciwgcXVhbnRpemVyLCBkZWNvZGVyLCBwcmlvcik6XG4gICAgICAgIHNlbGYuZW5jb2RlciA9IGVuY29kZXJcbiAgICAgICAgc2VsZi5xdWFudGl6ZXIgPSBxdWFudGl6ZXJcbiAgICAgICAgc2VsZi5kZWNvZGVyID0gZGVjb2RlclxuICAgICAgICBzZWxmLnByaW9yID0gcHJpb3IgICMgUGl4ZWxDTk4gb3IgVHJhbnNmb3JtZXIgdHJhaW5lZCBvbiBjb2RlIHNlcXVlbmNlc1xuXG4gICAgQHRvcmNoLm5vX2dyYWQoKVxuICAgIGRlZiBlbmNvZGVfdG9fY29kZXMoc2VsZiwgeCk6XG4gICAgICAgICMgU3RhZ2UgMSBvdXRwdXQ6IGRpc2NyZXRlIGluZGV4IGZvciBlYWNoIHNwYXRpYWwgcG9zaXRpb25cbiAgICAgICAgel9lID0gc2VsZi5lbmNvZGVyKHgpXG4gICAgICAgIF8sIF8sIGluZGljZXMgPSBzZWxmLnF1YW50aXplcih6X2UpXG4gICAgICAgIHJldHVybiBpbmRpY2VzICAjIHNoYXBlOiAoQiwgSCpXKVxuXG4gICAgQHRvcmNoLm5vX2dyYWQoKVxuICAgIGRlZiBnZW5lcmF0ZShzZWxmLCBiYXRjaF9zaXplLCBjb2RlX3NoYXBlPSgxNiwgMTYpLCBkZXZpY2U9XHUwMDI3Y3VkYVx1MDAyNywgdGVtcGVyYXR1cmU9MS4wKTpcbiAgICAgICAgIyBTdGFnZSAyOiBhdXRvcmVncmVzc2l2ZWx5IHNhbXBsZSBjb2RlIGluZGljZXMgdGhlbiBkZWNvZGUgdG8gaW1hZ2VcbiAgICAgICAgSCwgVyA9IGNvZGVfc2hhcGVcbiAgICAgICAgY29kZXMgPSB0b3JjaC56ZXJvcyhiYXRjaF9zaXplLCBIICogVywgZHR5cGU9dG9yY2gubG9uZywgZGV2aWNlPWRldmljZSlcbiAgICAgICAgZm9yIHBvcyBpbiByYW5nZShIICogVyk6XG4gICAgICAgICAgICBsb2dpdHMgPSBzZWxmLnByaW9yKGNvZGVzKVs6LCBwb3MsIDpdICAjIChCLCBudW1fZW1iZWRkaW5ncylcbiAgICAgICAgICAgIHByb2JzID0gdG9yY2guc29mdG1heChsb2dpdHMgLyB0ZW1wZXJhdHVyZSwgZGltPS0xKVxuICAgICAgICAgICAgY29kZXNbOiwgcG9zXSA9IENhdGVnb3JpY2FsKHByb2JzKS5zYW1wbGUoKVxuICAgICAgICAjIExvb2sgdXAgcXVhbnRpemVkIHZlY3RvcnMgYW5kIGRlY29kZSB0byBpbWFnZSBzcGFjZVxuICAgICAgICB6X3EgPSBzZWxmLnF1YW50aXplci5lbWJlZGRpbmdzW2NvZGVzXSAgIyAoQiwgSCpXLCBEKVxuICAgICAgICB6X3EgPSB6X3EucmVzaGFwZShiYXRjaF9zaXplLCBILCBXLCAtMSkucGVybXV0ZSgwLCAzLCAxLCAyKSAgIyAoQiwgRCwgSCwgVylcbiAgICAgICAgcmV0dXJuIHNlbGYuZGVjb2Rlcih6X3EpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVlFHQU4gYW5kIEV4dGVuc2lvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZRR0FOIChFc3NlciBldCBhbC4sIDIwMjEpIGF1Z21lbnRzIFZRLVZBRSB3aXRoIHR3byBhZGRpdGlvbmFsIGxvc3NlczogYSAqKnBlcmNlcHR1YWwgbG9zcyoqIChWR0cgZmVhdHVyZS1zcGFjZSBMMiBtYXRjaGluZyB0aGF0IHBlbmFsaXNlcyBoaWdoLWxldmVsIGRpc2NyZXBhbmNpZXMpIGFuZCBhICoqcGF0Y2ggYWR2ZXJzYXJpYWwgbG9zcyoqIGZyb20gYSBQYXRjaEdBTiBkaXNjcmltaW5hdG9yIHRoYXQgcGVuYWxpc2VzIGxvY2FsbHkgdW5yZWFsaXN0aWMgdGV4dHVyZXMuIFRvZ2V0aGVyIHRoZXNlIHByb2R1Y2UgZmFyIHNoYXJwZXIgcmVjb25zdHJ1Y3Rpb25zIHRoYW4gcGl4ZWwtbGV2ZWwgTVNFIGFsb25lLiBWUUdBTiBjb2RlcyBmZWQgdG8gYSBHUFQtc3R5bGUgVHJhbnNmb3JtZXIgcHJpb3IgZm9ybWVkIHRoZSBiYWNrYm9uZSBvZiBEQUxMLUUuIFRoZSBzYW1lIGVuY29kZXItZGVjb2RlciBkZXNpZ24gdW5kZXJwaW5zIFN0YWJsZSBEaWZmdXNpb27igJlzIGxhdGVudCBzcGFjZSAod2l0aCBhIEtMLXJlZ3VsYXJpc2VkIGNvbnRpbnVvdXMgdmFyaWFudCBmb3IgdGhlIGZpbmFsIG1vZGVsKS4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IioqRlNRIChGaW5pdGUgU2NhbGFyIFF1YW50aXphdGlvbiwgTWVudHplciBldCBhbC4sIDIwMjMpKiogb2ZmZXJzIGEgc2ltcGxlciwgY29sbGFwc2UtZnJlZSBhbHRlcm5hdGl2ZTogaW5kZXBlbmRlbnRseSBxdWFudGl6ZSBlYWNoIGxhdGVudCBkaW1lbnNpb24gdG8gYSBzbWFsbCBzZXQgb2YgaW50ZWdlcnMgKGUuZy4sIHstMiwgLTEsIDAsIDEsIDJ9KSB2aWEgYm91bmRlZCByb3VuZGluZy4gV2l0aCBEIGRpbWVuc2lvbnMgYXQgTCBsZXZlbHMgZWFjaCwgdGhlIGVmZmVjdGl2ZSBjb2RlYm9vayBzaXplIGlzIExeRC4gRlNRIGVsaW1pbmF0ZXMgZGVhZCBjb2RlIGNvbGxhcHNlIGVudGlyZWx5IChldmVyeSBsYXR0aWNlIHBvaW50IGlzIHJlYWNoYWJsZSksIHJlcXVpcmVzIG5vIGNvZGVib29rIGxvc3MsIEVNQSB1cGRhdGVzLCBvciBjb21taXRtZW50IGxvc3MsIGFuZCBtYXRjaGVzIFZRLVZBRSBhbmQgVlFHQU4gcXVhbGl0eSBvbiBzdGFuZGFyZCBiZW5jaG1hcmtzIHdpdGggZHJhbWF0aWNhbGx5IHNpbXBsZXIgaW1wbGVtZW50YXRpb24uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiTGF0ZW50IFR5cGUiLCJDb2xsYXBzZSBSaXNrIiwiUHJpb3IgTW9kZWwiLCJHZW5lcmF0aW9uIFF1YWxpdHkiLCJLZXkgQXBwbGljYXRpb24iXSwicm93cyI6W1siVkFFIiwiQ29udGludW91cyBHYXVzc2lhbiIsIlBvc3RlcmlvciBjb2xsYXBzZSIsIkZsb3cgLyBEaWZmdXNpb24iLCJCbHVycnkgKE1TRSkiLCJSZXByZXNlbnRhdGlvbiBsZWFybmluZyJdLFsiVlEtVkFFIiwiRGlzY3JldGUgY29kZWJvb2siLCJEZWFkIGNvZGVzIiwiUGl4ZWxDTk4gLyBUcmFuc2Zvcm1lciIsIlNoYXJwLCBjb21wcmVzc2VkIiwiQXVkaW8gYW5kIGltYWdlIGNvbXByZXNzaW9uIl0sWyJWUUdBTiIsIkRpc2NyZXRlIGNvZGVib29rICsgcGVyY2VwdHVhbCIsIkRlYWQgY29kZXMgKG1hbmFnZWQpIiwiR1BULXN0eWxlIFRyYW5zZm9ybWVyIiwiSGlnaCBmaWRlbGl0eSIsIkhpZ2gtcmVzIGltYWdlIGdlbmVyYXRpb24iXSxbIkZTUSIsIkRpc2NyZXRlIHNjYWxhciBncmlkIiwiTm9uZSAoZGV0ZXJtaW5pc3RpYykiLCJUcmFuc2Zvcm1lciIsIkNvbXBhcmFibGUgdG8gVlEtVkFFIiwiU2ltcGxlciBkcm9wLWluIHJlcGxhY2VtZW50Il1dfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJWUS1WQUUgcmVwbGFjZXMgY29udGludW91cyBsYXRlbnRzIHdpdGggZGlzY3JldGUgY29kZWJvb2sgbG9va3VwcywgZW5hYmxpbmcgY2xlYW4gc3ltYm9saWMgcmVwcmVzZW50YXRpb25zIHdpdGhvdXQgcG9zdGVyaW9yIGNvbGxhcHNlIG9yIGJsdXJyaW5nLiIsIlRoZSBzdHJhaWdodC10aHJvdWdoIGVzdGltYXRvciAoel9xX3N0ID0gel9lICsgKHpfcSAtIHpfZSkuZGV0YWNoKCkpIGlzIHRoZSBzaW5nbGUgbGluZSB0aGF0IGVuYWJsZXMgZW5kLXRvLWVuZCBiYWNrcHJvcGFnYXRpb24gdGhyb3VnaCB0aGUgbm9uLWRpZmZlcmVudGlhYmxlIGFyZ21pbi4iLCJFTUEgY29kZWJvb2sgdXBkYXRlcyAoZXF1aXZhbGVudCB0byBvbmxpbmUgay1tZWFucykgYXJlIG1vcmUgc3RhYmxlIHRoYW4gZ3JhZGllbnQgZGVzY2VudCBvbiB0aGUgY29kZWJvb2sgbG9zcyBhbmQgYXJlIHRoZSByZWNvbW1lbmRlZCBhcHByb2FjaCBpbiBwcmFjdGljZS4iLCJEZWFkIGNvZGUgY29sbGFwc2UgaXMgdGhlIG1haW4gZmFpbHVyZSBtb2RlOiBtb25pdG9yIHBlci1jb2RlIHV0aWxpc2F0aW9uIGFuZCB1c2UgcmFuZG9tIHJlc3RhcnQgdG8gcmVpbml0aWFsaXNlIHVudXNlZCBlbnRyaWVzIGZyb20gY3VycmVudCBlbmNvZGVyIG91dHB1dHMuIiwiVHdvLXN0YWdlIGdlbmVyYXRpb24gY2xlYW5seSBzZXBhcmF0ZXMgY29tcHJlc3Npb24gZnJvbSBzeW50aGVzaXM6IFZRLVZBRSBoYW5kbGVzIHBpeGVsLWxldmVsIGZpZGVsaXR5OyB0aGUgYXV0b3JlZ3Jlc3NpdmUgcHJpb3IgaGFuZGxlcyBoaWdoLWxldmVsIGNvbXBvc2l0aW9uYWwgc3RydWN0dXJlLiIsIlZRR0FOIGFkZHMgcGVyY2VwdHVhbCBhbmQgYWR2ZXJzYXJpYWwgbG9zc2VzIGZvciBzaWduaWZpY2FudGx5IHNoYXJwZXIgcmVjb25zdHJ1Y3Rpb25zIGFuZCBwb3dlcnMgREFMTC1FIGFuZCBsYXRlbnQgZGlmZnVzaW9uIG1vZGVscy4iLCJGU1Egb2ZmZXJzIGEgY29sbGFwc2UtZnJlZSBkcm9wLWluIGFsdGVybmF0aXZlIGJ5IHF1YW50aXppbmcgZWFjaCBsYXRlbnQgZGltZW5zaW9uIGluZGVwZW5kZW50bHkgdG8gc2NhbGFyIGludGVnZXIgbGV2ZWxzLCBlbGltaW5hdGluZyBhbGwgY29kZWJvb2sgY29tcGxleGl0eS4iXX1d"
---
# VQ-VAE — Vector Quantization and Discrete Latent Spaces

## Introduction

VQ-VAE (van den Oord et al., 2017) replaces the continuous Gaussian latent of a standard VAE with a **discrete codebook** of K learned embedding vectors E = {e₁, …, e_K} ∈ ℝ^D. Instead of sampling from a distribution, the encoder output z_e(x) is snapped to its nearest codebook entry, producing a structured symbolic representation. This sidesteps posterior collapse (the encoder ignoring the latent) and the blurring caused by averaging over continuous uncertainty.

The core design philosophy is to decouple representation from generation. VQ-VAE learns a compact discrete code per input; a separate autoregressive model (PixelCNN, Transformer) then learns a prior over those codes. This two-stage approach underpins DALL-E, VQGAN, AudioLM, and MusicLM. The discrete bottleneck forces the model to commit to meaningful, reusable symbolic units rather than smearing information across a continuous manifold.

## Vector Quantization Mathematics

The encoder maps input x to a continuous feature map z_e(x) ∈ ℝ^D. Quantization maps each spatial position to the nearest codebook vector: z_q = e_k where k = argmin‖z_e − e_i‖². The total VQ-VAE loss combines three terms: reconstruction (pixel-level MSE between input and decoder output), codebook loss (moves codebook entries toward encoder outputs using stop-gradient on z_e), and commitment loss (pushes the encoder toward the chosen code using stop-gradient on z_q). The stop-gradient sg() passes values forward but blocks all gradients backward.

$$\\mathcal{L} = \\|x - \\hat{x}\\|^2 + \\|\\mathrm{sg}(z_e) - z_q\\|^2 + \\beta\\,\\|z_e - \\mathrm{sg}(z_q)\\|^2$$

The commitment weight β ≈ 0.25 controls how strongly the encoder is pushed to stay near its chosen codebook entry. Without it, the encoder can drift between multiple entries during training, producing unstable code assignments and slow convergence. The codebook and commitment losses are complementary: codebook loss moves the dictionary; commitment loss anchors the encoder.

## Straight-Through Gradient Estimator

The argmin operation has zero derivative almost everywhere and is undefined at the boundaries between Voronoi cells. It cannot be differentiated through directly, so gradients from the decoder cannot reach the encoder. The straight-through estimator (Bengio et al., 2013) resolves this by simply copying gradients from the decoder input z_q back to the encoder output z_e, bypassing the non-differentiable quantization. In code this is one line: z_q_st = z_e + (z_q - z_e).detach(). The .detach() makes (z_q - z_e) a constant in the backward pass, so all gradient flows through z_e only, as if z_q and z_e were identical.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class VectorQuantizer(nn.Module):
    def __init__(self, num_embeddings, embedding_dim, commitment_cost=0.25):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_embeddings = num_embeddings
        self.commitment_cost = commitment_cost
        self.embeddings = nn.Embedding(num_embeddings, embedding_dim)
        nn.init.uniform_(self.embeddings.weight, -1/num_embeddings, 1/num_embeddings)

    def forward(self, z_e):
        # z_e: (B, D, H, W) -> flatten spatial dims to (B*H*W, D)
        z_e_flat = z_e.permute(0, 2, 3, 1).reshape(-1, self.embedding_dim)
        # Squared L2 distances via expansion: ||a-b||^2 = ||a||^2 - 2a*b^T + ||b||^2
        distances = (z_e_flat.pow(2).sum(1, keepdim=True)
                     - 2 * z_e_flat @ self.embeddings.weight.T
                     + self.embeddings.weight.pow(2).sum(1))
        indices = distances.argmin(dim=1)           # nearest codebook entry
        z_q_flat = self.embeddings(indices)
        z_q = z_q_flat.reshape(z_e.shape[0], z_e.shape[2], z_e.shape[3], -1).permute(0, 3, 1, 2)
        codebook_loss = F.mse_loss(z_q, z_e.detach())     # move codes toward encoder
        commitment_loss = F.mse_loss(z_e, z_q.detach())   # move encoder toward codes
        loss = codebook_loss + self.commitment_cost * commitment_loss
        z_q_st = z_e + (z_q - z_e).detach()       # straight-through estimator
        return z_q_st, loss, indices
```

## Codebook Learning with EMA

Instead of gradient descent on the codebook loss, the VQ-VAE paper recommends exponential moving average (EMA) updates as a more stable alternative. For each codebook entry e_i, maintain a running count n_i of assignments and a running embedding sum m_i. After each batch, update with decay γ ≈ 0.99: n_i ← γn_i + (1−γ)·count(i), and m_i ← γm_i + (1−γ)·sum(z_e assigned to i), then set e_i = m_i / n_i. This is online k-means. It avoids the interaction between codebook gradient updates and the encoder gradient, leading to faster convergence and fewer dead codes in practice.

```python
import torch
import torch.nn as nn

class VectorQuantizerEMA(nn.Module):
    def __init__(self, num_embeddings, embedding_dim, decay=0.99, commitment_cost=0.25, eps=1e-5):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_embeddings = num_embeddings
        self.commitment_cost = commitment_cost
        self.decay = decay
        self.eps = eps
        embedding = torch.randn(num_embeddings, embedding_dim)
        self.register_buffer('embeddings', embedding)
        self.register_buffer('cluster_size', torch.zeros(num_embeddings))
        self.register_buffer('embed_avg', embedding.clone())

    def update_ema(self, z_e_flat, indices):
        # One-hot encode code assignments: shape (N, K)
        one_hot = torch.zeros(indices.shape[0], self.num_embeddings, device=z_e_flat.device)
        one_hot.scatter_(1, indices.unsqueeze(1), 1)
        # EMA update for cluster sizes and embedding running sums
        self.cluster_size.mul_(self.decay).add_((1 - self.decay) * one_hot.sum(0))
        embed_sum = one_hot.T @ z_e_flat
        self.embed_avg.mul_(self.decay).add_((1 - self.decay) * embed_sum)
        # Laplace smoothing avoids division by zero for empty clusters
        n = self.cluster_size.sum()
        smoothed = (self.cluster_size + self.eps) / (n + self.num_embeddings * self.eps) * n
        self.embeddings = self.embed_avg / smoothed.unsqueeze(1)
```

## Dead Code Problem

In practice, many codebook entries receive zero assignments throughout training — they are never the nearest neighbour for any encoder output. These **dead codes** waste codebook capacity and reduce the effective number of distinct representations. Common symptoms: codebook utilisation below 50% and reconstruction quality plateauing early. Dead codes arise because once a code falls behind its neighbours due to random initialisation, it gets no gradient signal or EMA update and can never recover on its own.

> **Batch Size Warning**: EMA codebook updates require large batch size (≥256) to get enough code assignments per step — small batches lead to dead code collapse. With batch size 32, most codes receive zero assignments in any single step, causing the EMA cluster sizes to decay toward zero without recovery. Use gradient accumulation or increase batch size before relying on EMA codebook updates.

```python
import torch

class DeadCodeMonitor:
    def __init__(self, num_embeddings, threshold=1.0, restart_every=50):
        self.num_embeddings = num_embeddings
        self.threshold = threshold      # codes used fewer times than this are dead
        self.restart_every = restart_every  # check interval in training steps
        self.usage_count = torch.zeros(num_embeddings)
        self.step = 0

    def update(self, indices):
        # Accumulate per-code usage counts from this batch
        counts = torch.zeros(self.num_embeddings)
        counts.scatter_add_(0, indices.flatten().cpu(), torch.ones(indices.numel()))
        self.usage_count += counts
        self.step += 1

    def restart_dead_codes(self, embeddings, z_e_flat):
        # Only check at restart_every intervals to reduce overhead
        if self.step % self.restart_every != 0:
            return 0
        dead_mask = self.usage_count < self.threshold
        num_dead = int(dead_mask.sum().item())
        if num_dead == 0:
            self.usage_count.zero_()
            return 0
        # Reinitialize dead codes with random encoder outputs from current batch
        perm = torch.randperm(z_e_flat.shape[0])[:num_dead]
        with torch.no_grad():
            embeddings.data[dead_mask] = z_e_flat[perm].detach()
        self.usage_count.zero_()
        print(f'Restarted {num_dead} dead codes at step {self.step}')
        return num_dead
```

## Two-Stage Generation

VQ-VAE is only an autoencoder — it cannot generate novel samples on its own. Stage 2 trains an autoregressive model to model the distribution of discrete code sequences produced by the encoder on the training set. At inference, sample a complete code sequence from the prior, then pass it through the VQ-VAE decoder to produce an image. The separation is architecturally powerful: the VQ-VAE solves the hard perceptual reconstruction problem at the pixel level; the prior only needs to model a short sequence of discrete tokens representing high-level structure.

```python
import torch
from torch.distributions import Categorical

class VQVAEGenerator:
    # Two-stage: (1) train VQ-VAE, (2) train autoregressive prior on discrete codes
    def __init__(self, encoder, quantizer, decoder, prior):
        self.encoder = encoder
        self.quantizer = quantizer
        self.decoder = decoder
        self.prior = prior  # PixelCNN or Transformer trained on code sequences

    @torch.no_grad()
    def encode_to_codes(self, x):
        # Stage 1 output: discrete index for each spatial position
        z_e = self.encoder(x)
        _, _, indices = self.quantizer(z_e)
        return indices  # shape: (B, H*W)

    @torch.no_grad()
    def generate(self, batch_size, code_shape=(16, 16), device='cuda', temperature=1.0):
        # Stage 2: autoregressively sample code indices then decode to image
        H, W = code_shape
        codes = torch.zeros(batch_size, H * W, dtype=torch.long, device=device)
        for pos in range(H * W):
            logits = self.prior(codes)[:, pos, :]  # (B, num_embeddings)
            probs = torch.softmax(logits / temperature, dim=-1)
            codes[:, pos] = Categorical(probs).sample()
        # Look up quantized vectors and decode to image space
        z_q = self.quantizer.embeddings[codes]  # (B, H*W, D)
        z_q = z_q.reshape(batch_size, H, W, -1).permute(0, 3, 1, 2)  # (B, D, H, W)
        return self.decoder(z_q)
```

## VQGAN and Extensions

VQGAN (Esser et al., 2021) augments VQ-VAE with two additional losses: a **perceptual loss** (VGG feature-space L2 matching that penalises high-level discrepancies) and a **patch adversarial loss** from a PatchGAN discriminator that penalises locally unrealistic textures. Together these produce far sharper reconstructions than pixel-level MSE alone. VQGAN codes fed to a GPT-style Transformer prior formed the backbone of DALL-E. The same encoder-decoder design underpins Stable Diffusion’s latent space (with a KL-regularised continuous variant for the final model).

**FSQ (Finite Scalar Quantization, Mentzer et al., 2023)** offers a simpler, collapse-free alternative: independently quantize each latent dimension to a small set of integers (e.g., {-2, -1, 0, 1, 2}) via bounded rounding. With D dimensions at L levels each, the effective codebook size is L^D. FSQ eliminates dead code collapse entirely (every lattice point is reachable), requires no codebook loss, EMA updates, or commitment loss, and matches VQ-VAE and VQGAN quality on standard benchmarks with dramatically simpler implementation.

| Model | Latent Type | Collapse Risk | Prior Model | Generation Quality | Key Application |
| --- | --- | --- | --- | --- | --- |
| VAE | Continuous Gaussian | Posterior collapse | Flow / Diffusion | Blurry (MSE) | Representation learning |
| VQ-VAE | Discrete codebook | Dead codes | PixelCNN / Transformer | Sharp, compressed | Audio and image compression |
| VQGAN | Discrete codebook + perceptual | Dead codes (managed) | GPT-style Transformer | High fidelity | High-res image generation |
| FSQ | Discrete scalar grid | None (deterministic) | Transformer | Comparable to VQ-VAE | Simpler drop-in replacement |

## Key Takeaways

- VQ-VAE replaces continuous latents with discrete codebook lookups, enabling clean symbolic representations without posterior collapse or blurring.
- The straight-through estimator (z_q_st = z_e + (z_q - z_e).detach()) is the single line that enables end-to-end backpropagation through the non-differentiable argmin.
- EMA codebook updates (equivalent to online k-means) are more stable than gradient descent on the codebook loss and are the recommended approach in practice.
- Dead code collapse is the main failure mode: monitor per-code utilisation and use random restart to reinitialise unused entries from current encoder outputs.
- Two-stage generation cleanly separates compression from synthesis: VQ-VAE handles pixel-level fidelity; the autoregressive prior handles high-level compositional structure.
- VQGAN adds perceptual and adversarial losses for significantly sharper reconstructions and powers DALL-E and latent diffusion models.
- FSQ offers a collapse-free drop-in alternative by quantizing each latent dimension independently to scalar integer levels, eliminating all codebook complexity.

