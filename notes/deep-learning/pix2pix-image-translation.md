---
title: "Pix2Pix — Paired Image-to-Image Translation"
slug: "pix2pix-image-translation"
description: "Pix2Pix (Isola et al. 2017) learns image-to-image translation from paired data using a U-Net generator with skip connections, a PatchGAN discriminator that classifies 70x70 overlapping patches, and a combined GAN + L1 objective that enforces both local realism and global consistency."
tags: ["deep-learning", "generative-models", "gans", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGl4MlBpeCAoSXNvbGEgZXQgYWwuIDIwMTcpIGZyYW1lcyBpbWFnZSB0cmFuc2xhdGlvbiBhcyBhIGNvbmRpdGlvbmFsIEdBTiBwcm9ibGVtOiBnaXZlbiBhIHBhaXJlZCBkYXRhc2V0IG9mIChpbnB1dCBpbWFnZSBBLCB0YXJnZXQgaW1hZ2UgQiksIHRyYWluIGEgZ2VuZXJhdG9yIEcgdG8gbWFwIEEg4oaSIEIgc3VjaCB0aGF0IHRoZSBvdXRwdXQgaXMgaW5kaXN0aW5ndWlzaGFibGUgZnJvbSByZWFsIEIgaW1hZ2VzLiBBcHBsaWNhdGlvbnMgaW5jbHVkZSBlZGdlc+KGknBob3RvcywgbWFwc+KGknNhdGVsbGl0ZSBpbWFnZXJ5LCBzZW1hbnRpYyBsYWJlbHPihpJwaG90b3JlYWxpc3RpYyBpbWFnZXMsIGFuZCBkYXnihpJuaWdodCBjb252ZXJzaW9uLiBQYWlyZWQgdHJhaW5pbmcgZGF0YSBpcyB0aGUgY2VudHJhbCByZXF1aXJlbWVudCDigJQgYW5kIGxpbWl0YXRpb24g4oCUIG9mIFBpeDJQaXg7IHdoZW4gcGFpcnMgYXJlIHVuYXZhaWxhYmxlLCBDeWNsZUdBTiBpcyB1c2VkIGluc3RlYWQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiY0dBTiBGb3JtdWxhdGlvbiB3aXRoIEwxIFJlY29uc3RydWN0aW9uIExvc3MifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBQaXgyUGl4IG9iamVjdGl2ZSBpcyBMID0gTF9jR0FOKEcsRCkgKyDOu8K3TF9MMShHKS4gVGhlIGNHQU4gdGVybSBMX2NHQU4gZW5jb3VyYWdlcyBHIHRvIHByb2R1Y2UgcmVhbGlzdGljLWxvb2tpbmcgb3V0cHV0cyB0aGF0IGZvb2wgRC4gVGhlIEwxIHRlcm0gTF9MMSA9IEVb4oCWeSAtIEcoeCnigJbigoFdIHBlbmFsaXNlcyBkZXZpYXRpb24gZnJvbSB0aGUgZ3JvdW5kLXRydXRoIHRhcmdldCBhbmQgZm9yY2VzIGdsb2JhbCBjb25zaXN0ZW5jeS4gTDEgaXMgcHJlZmVycmVkIG92ZXIgTDIgYmVjYXVzZSBMMiB0ZW5kcyB0byBwcm9kdWNlIGJsdXJyeSBvdXRwdXRzIChpdCBtaW5pbWlzZXMgZXhwZWN0ZWQgc3F1YXJlZCBlcnJvciwgd2hpY2ggZW5jb3VyYWdlcyBhdmVyYWdpbmcgb3ZlciBtb2RlcykuIM67PTEwMCBpcyB0aGUgc3RhbmRhcmQgc2V0dGluZyDigJQgc3Ryb25nIGVub3VnaCB0byBwcmV2ZW50IEcgZnJvbSBpZ25vcmluZyB0aGUgaW5wdXQgY29udGVudC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIHVuZXRfZG93bihpbl9jaCwgb3V0X2NoLCBub3JtPVRydWUpOlxuICAgIGxheWVycyA9IFtubi5Db252MmQoaW5fY2gsIG91dF9jaCwgNCwgMiwgMSwgYmlhcz1ub3Qgbm9ybSldXG4gICAgaWYgbm9ybTogbGF5ZXJzLmFwcGVuZChubi5JbnN0YW5jZU5vcm0yZChvdXRfY2gpKVxuICAgIGxheWVycy5hcHBlbmQobm4uTGVha3lSZUxVKDAuMiwgVHJ1ZSkpXG4gICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwoKmxheWVycylcblxuZGVmIHVuZXRfdXAoaW5fY2gsIG91dF9jaCwgZHJvcG91dD1GYWxzZSk6XG4gICAgbGF5ZXJzID0gW25uLkNvbnZUcmFuc3Bvc2UyZChpbl9jaCwgb3V0X2NoLCA0LCAyLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgICAgbm4uSW5zdGFuY2VOb3JtMmQob3V0X2NoKSwgbm4uUmVMVShUcnVlKV1cbiAgICBpZiBkcm9wb3V0OiBsYXllcnMuYXBwZW5kKG5uLkRyb3BvdXQoMC41KSlcbiAgICByZXR1cm4gbm4uU2VxdWVudGlhbCgqbGF5ZXJzKVxuXG5jbGFzcyBQaXgyUGl4R2VuZXJhdG9yKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3VS1OZXQgZ2VuZXJhdG9yIHdpdGggc2tpcCBjb25uZWN0aW9ucyBmb3IgUGl4MlBpeC5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2g9Mywgb3V0X2NoPTMsIG5nZj0zMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmUxID0gdW5ldF9kb3duKGluX2NoLCBuZ2YsIG5vcm09RmFsc2UpXG4gICAgICAgIHNlbGYuZTIgPSB1bmV0X2Rvd24obmdmLCAgIG5nZioyKVxuICAgICAgICBzZWxmLmUzID0gdW5ldF9kb3duKG5nZioyLCBuZ2YqNClcbiAgICAgICAgc2VsZi5lNCA9IHVuZXRfZG93bihuZ2YqNCwgbmdmKjgpXG4gICAgICAgIHNlbGYuZDEgPSB1bmV0X3VwKG5nZio4LCAgIG5nZio0LCBkcm9wb3V0PVRydWUpXG4gICAgICAgIHNlbGYuZDIgPSB1bmV0X3VwKG5nZio0KjIsIG5nZioyKVxuICAgICAgICBzZWxmLmQzID0gdW5ldF91cChuZ2YqMioyLCBuZ2YpXG4gICAgICAgIHNlbGYuZDQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKG5nZioyLCBvdXRfY2gsIDQsIDIsIDEpLCBubi5UYW5oKCkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgZTE9c2VsZi5lMSh4KTsgZTI9c2VsZi5lMihlMSk7IGUzPXNlbGYuZTMoZTIpOyBlND1zZWxmLmU0KGUzKVxuICAgICAgICBkPXNlbGYuZDEoZTQpOyBkPXNlbGYuZDIodG9yY2guY2F0KFtkLGUzXSwxKSlcbiAgICAgICAgZD1zZWxmLmQzKHRvcmNoLmNhdChbZCxlMl0sMSkpXG4gICAgICAgIHJldHVybiBzZWxmLmQ0KHRvcmNoLmNhdChbZCxlMV0sMSkpXG5cbkc9UGl4MlBpeEdlbmVyYXRvcigpXG5wcmludChcdTAwMjdHZW5lcmF0b3Igb3V0cHV0Olx1MDAyNywgRyh0b3JjaC5yYW5kbigxLDMsNjQsNjQpKS5zaGFwZSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQYXRjaEdBTiBEaXNjcmltaW5hdG9yIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJJbnN0ZWFkIG9mIGNsYXNzaWZ5aW5nIHRoZSBlbnRpcmUgaW1hZ2UgYXMgcmVhbCBvciBmYWtlLCB0aGUgUGF0Y2hHQU4gZGlzY3JpbWluYXRvciBjbGFzc2lmaWVzIG92ZXJsYXBwaW5nIDcww5c3MCBwYXRjaGVzLiBUaGUgb3V0cHV0IGlzIGEgc3BhdGlhbCBtYXAgd2hlcmUgZWFjaCB2YWx1ZSBpcyB0aGUgcmVhbC9mYWtlIHNjb3JlIGZvciB0aGUgY29ycmVzcG9uZGluZyBwYXRjaC4gVGhpcyBkZXNpZ24gaGFzIHRocmVlIGFkdmFudGFnZXM6ICgxKSBpdCBmb2N1c2VzIERcdTAwMjdzIGNhcGFjaXR5IG9uIGxvY2FsIHRleHR1cmUgYW5kIGhpZ2gtZnJlcXVlbmN5IGRldGFpbHMgd2hlcmUgR0FOIHRyYWluaW5nIGlzIG1vc3QgdXNlZnVsOyAoMikgaXQgaGFzIGZld2VyIHBhcmFtZXRlcnMgdGhhbiBhIGZ1bGwtaW1hZ2UgRDsgYW5kICgzKSBpdCBjYW4gYmUgYXBwbGllZCB0byBpbWFnZXMgb2YgYW55IHJlc29sdXRpb24g4oCUIGp1c3QgcnVuIHRoZSBjb252b2x1dGlvbmFsIEQgYWNyb3NzIHRoZSBmdWxsIGltYWdlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5kZWYgZF9ibG9jayhpbl9jaCwgb3V0X2NoLCBzdHJpZGU9Miwgbm9ybT1UcnVlKTpcbiAgICBsYXllcnMgPSBbbm4uQ29udjJkKGluX2NoLCBvdXRfY2gsIDQsIHN0cmlkZSwgMSwgYmlhcz1ub3Qgbm9ybSldXG4gICAgaWYgbm9ybTogbGF5ZXJzLmFwcGVuZChubi5JbnN0YW5jZU5vcm0yZChvdXRfY2gpKVxuICAgIGxheWVycy5hcHBlbmQobm4uTGVha3lSZUxVKDAuMiwgVHJ1ZSkpXG4gICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwoKmxheWVycylcblxuY2xhc3MgUGF0Y2hHQU5EaXNjcmltaW5hdG9yKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3NzB4NzAgUGF0Y2hHQU46IGVhY2ggb3V0cHV0IHBpeGVsIHNjb3JlcyBvbmUgb3ZlcmxhcHBpbmcgcGF0Y2guXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoPTYsIG5kZj0zMik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICAjIElucHV0OiBjb25jYXQocmVhbF9BLCByZWFsX0Igb3IgZmFrZV9CKSAtXHUwMDNlIDYgY2hhbm5lbHNcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgZF9ibG9jayhpbl9jaCwgbmRmLCAgICBub3JtPUZhbHNlKSwgICMgNjQtXHUwMDNlMzJcbiAgICAgICAgICAgIGRfYmxvY2sobmRmLCAgIG5kZioyKSwgICAgICAgICAgICAgICAjIDMyLVx1MDAzZTE2XG4gICAgICAgICAgICBkX2Jsb2NrKG5kZioyLCBuZGYqNCksICAgICAgICAgICAgICAgIyAxNi1cdTAwM2U4XG4gICAgICAgICAgICBkX2Jsb2NrKG5kZio0LCBuZGYqOCwgc3RyaWRlPTEpLCAgICAgIyA4LVx1MDAzZThcbiAgICAgICAgICAgIG5uLkNvbnYyZChuZGYqOCwgMSwgNCwgMSwgMSkpICAgICAgICAjIHBhdGNoIGxvZ2l0c1xuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCwgeSk6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldCh0b3JjaC5jYXQoW3gsIHldLCAxKSkgICAjIGNvbmRpdGlvbiBvbiBpbnB1dFxuXG5EID0gUGF0Y2hHQU5EaXNjcmltaW5hdG9yKClcbnggPSB0b3JjaC5yYW5kbigyLCAzLCA2NCwgNjQpXG55ID0gdG9yY2gucmFuZG4oMiwgMywgNjQsIDY0KVxub3V0ID0gRCh4LCB5KVxucHJpbnQoXHUwMDI3UGF0Y2hHQU4gb3V0cHV0IHNoYXBlOlx1MDAyNywgb3V0LnNoYXBlKSAgIyBzcGF0aWFsIHBhdGNoIG1hcCJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkNvbWJpbmVkIEdBTiBhbmQgTDEgTG9zcyBUcmFpbmluZyBTdGVwIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUcmFpbmluZyBhbHRlcm5hdGVzIGJldHdlZW4gdXBkYXRpbmcgRCBhbmQgRy4gRCBpcyB1cGRhdGVkIHRvIG1heGltaXNlIGxvZyBEKHgseSkgKyBsb2coMeKIkkQoeCxHKHgpKSkuIEcgaXMgdXBkYXRlZCB0byBtaW5pbWlzZSB0aGUgYWR2ZXJzYXJpYWwgbG9zcyBsb2coMeKIkkQoeCxHKHgpKSkgcGx1cyDOu8K3TDEoRyh4KSx5KS4gSW4gcHJhY3RpY2UsIEcgbWluaW1pc2VzIOKIkmxvZyBEKHgsRyh4KSkgKG5vbi1zYXR1cmF0aW5nIHZhcmlhbnQpIGZvciBzdHJvbmdlciBncmFkaWVudHMgZWFybHkgaW4gdHJhaW5pbmcuIFRoZSBMMSBjb2VmZmljaWVudCDOuz0xMDAgbWVhbnMgdGhlIGdlbmVyYXRvciBwcmltYXJpbHkgb3B0aW1pc2VzIHJlY29uc3RydWN0aW9uIGZpZGVsaXR5LCB1c2luZyB0aGUgYWR2ZXJzYXJpYWwgc2lnbmFsIHRvIHNoYXJwZW4gdGV4dHVyZXMgdGhhdCBMMSB3b3VsZCBvdGhlcndpc2UgYmx1ci4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIHBpeDJwaXhfc3RlcChHLCBELCByZWFsX0EsIHJlYWxfQiwgbGFtPTEwMC4wKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdDb21wdXRlIEcgYW5kIEQgbG9zc2VzIGZvciBvbmUgdHJhaW5pbmcgc3RlcC5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBiY2UgPSBubi5CQ0VXaXRoTG9naXRzTG9zcygpXG4gICAgbDEgID0gbm4uTDFMb3NzKClcbiAgICBmYWtlX0IgPSBHKHJlYWxfQSlcbiAgICAjIC0tIERpc2NyaW1pbmF0b3IgLS1cbiAgICByZWFsX291dCA9IEQocmVhbF9BLCByZWFsX0IpXG4gICAgZmFrZV9vdXQgPSBEKHJlYWxfQSwgZmFrZV9CLmRldGFjaCgpKVxuICAgIGxvc3NfRCAgID0gMC41ICogKGJjZShyZWFsX291dCwgdG9yY2gub25lc19saWtlKHJlYWxfb3V0KSkgK1xuICAgICAgICAgICAgICAgICAgICAgIGJjZShmYWtlX291dCwgdG9yY2guemVyb3NfbGlrZShmYWtlX291dCkpKVxuICAgICMgLS0gR2VuZXJhdG9yIC0tXG4gICAgZmFrZV9vdXRfZyAgPSBEKHJlYWxfQSwgZmFrZV9CKVxuICAgIGxvc3NfR19hZHYgID0gYmNlKGZha2Vfb3V0X2csIHRvcmNoLm9uZXNfbGlrZShmYWtlX291dF9nKSlcbiAgICBsb3NzX0dfbDEgICA9IGwxKGZha2VfQiwgcmVhbF9CKSAqIGxhbVxuICAgIGxvc3NfRyAgICAgID0gbG9zc19HX2FkdiArIGxvc3NfR19sMVxuICAgIHJldHVybiBsb3NzX0QsIGxvc3NfRywgbG9zc19HX2Fkdi5pdGVtKCksIGxvc3NfR19sMS5pdGVtKClcblxuRyA9IFBpeDJQaXhHZW5lcmF0b3IoKTsgRCA9IFBhdGNoR0FORGlzY3JpbWluYXRvcigpXG5yQSA9IHRvcmNoLnJhbmRuKDIsIDMsIDY0LCA2NCk7IHJCID0gdG9yY2gucmFuZG4oMiwgMywgNjQsIDY0KVxubGQsIGxnLCBhZHYsIGwxdiA9IHBpeDJwaXhfc3RlcChHLCBELCByQSwgckIpXG5wcmludChcdTAwMjdsb3NzX0Q9ezouM2Z9ICBsb3NzX0dfYWR2PXs6LjNmfSAgbG9zc19HX0wxPXs6LjNmfVx1MDAyNy5mb3JtYXQoXG4gICAgICBsZC5pdGVtKCksIGFkdiwgbDF2KSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTa2lwIENvbm5lY3Rpb25zIGluIHRoZSBVLU5ldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFUtTmV0IGFyY2hpdGVjdHVyZSB1c2VzIGVuY29kZXItZGVjb2RlciBza2lwIGNvbm5lY3Rpb25zOiBhY3RpdmF0aW9ucyBmcm9tIGVuY29kZXIgbGF5ZXIgaSBhcmUgY29uY2F0ZW5hdGVkIHRvIHRoZSBjb3JyZXNwb25kaW5nIGRlY29kZXIgbGF5ZXIgbuKIkmkuIFRoaXMgcHJlc2VydmVzIGZpbmUtZ3JhaW5lZCBzcGF0aWFsIGRldGFpbCAodGV4dHVyZXMsIGVkZ2VzLCBwcmVjaXNlIGdlb21ldHJ5KSB0aGF0IHdvdWxkIG90aGVyd2lzZSBiZSBsb3N0IHRocm91Z2ggdGhlIGJvdHRsZW5lY2suIFdpdGhvdXQgc2tpcCBjb25uZWN0aW9ucywgdGhlIGdlbmVyYXRvciBtdXN0IHJlLXN5bnRoZXNpc2UgYWxsIHNwYXRpYWwgc3RydWN0dXJlIGZyb20gdGhlIGNvbXByZXNzZWQgYm90dGxlbmVjayByZXByZXNlbnRhdGlvbiDigJQgYSBoYXJkZXIgdGFzayB0aGF0IHJlc3VsdHMgaW4gYmx1cnJpZXIgb3V0cHV0cy4gU2tpcCBjb25uZWN0aW9ucyBhbGxvdyB0aGUgZGVjb2RlciB0byBmb2N1cyBvbiBoaWdoLWxldmVsIHN0eWxlIGFuZCBjb250ZW50IHJhdGhlciB0aGFuIHJlY29uc3RydWN0aW5nIGxvdy1sZXZlbCBzdHJ1Y3R1cmUgZnJvbSBzY3JhdGNoLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU2tpcCBmcm9tIGUxIHRvIGQ0OiBwcmVzZXJ2ZXMgZmluZXN0IHNwYXRpYWwgZGV0YWlsIChlZGdlcywgdGV4dHVyZXMpIiwiU2tpcCBmcm9tIGUyIHRvIGQzOiBwcmVzZXJ2ZXMgbWlkLXNjYWxlIHN0cnVjdHVyZSIsIlNraXAgZnJvbSBlMyB0byBkMjogcHJlc2VydmVzIGNvYXJzZSBsYXlvdXQiLCJCb3R0bGVuZWNrIChlNCk6IGZvcmNlcyBnbG9iYWwgY29udGV4dCBjb21wcmVzc2lvbiDigJQgdGhlIG9ubHkgcGF0aCBmb3IgaG9saXN0aWMgcmVhc29uaW5nIiwiRHJvcG91dCBvbiBkZWNvZGVyIChkMSk6IGFkZHMgc3RvY2hhc3RpY2l0eSwgYWN0cyBhcyByZWd1bGFyaXNhdGlvbiBkdXJpbmcgdHJhaW5pbmciLCJJbnN0YW5jZSBub3JtIChub3QgYmF0Y2ggbm9ybSk6IHBlci1pbWFnZSBub3JtYWxpc2F0aW9uIGF2b2lkcyBjcm9zcy1pbWFnZSBjb250YW1pbmF0aW9uIGluIHBhaXJlZCB0cmFpbmluZyJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJFdmFsdWF0aW9uOiBQU05SIGFuZCBTU0lNIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQYWlyZWQgaW1hZ2UgdHJhbnNsYXRpb24gZW5hYmxlcyBwaXhlbC1sZXZlbCBtZXRyaWNzIGFnYWluc3QgZ3JvdW5kIHRydXRoLiBQU05SIChQZWFrIFNpZ25hbC10by1Ob2lzZSBSYXRpbykgbWVhc3VyZXMgTVNFIGluIGRCOiBQU05SID0gMjDCt2xvZ+KCgeKCgChNQVgpIOKIkiAxMMK3bG9n4oKB4oKAKE1TRSkuIEhpZ2hlciBpcyBiZXR0ZXI7IHR5cGljYWwgdmFsdWVzIGZvciBnb29kIHRyYW5zbGF0aW9uOiAyNeKAkzM1IGRCLiBTU0lNIChTdHJ1Y3R1cmFsIFNpbWlsYXJpdHkgSW5kZXgpIG1lYXN1cmVzIGx1bWluYW5jZSwgY29udHJhc3QsIGFuZCBzdHJ1Y3R1cmUgc2ltaWxhcml0eSBpbiBb4oiSMSwxXS4gSGlnaGVyIGlzIGJldHRlcjsgU1NJTSBcdTAwM2UgMC45IGlzIGNvbnNpZGVyZWQgaGlnaCBxdWFsaXR5LiBQZXJjZXB0dWFsIG1ldHJpY3MgKExQSVBTKSBhbmQgRklEIGFyZSBhbHNvIHVzZWQgd2hlbiBncm91bmQgdHJ1dGggcGFpcnMgYXJlIGF2YWlsYWJsZS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmRlZiBwc25yKHByZWQsIHRhcmdldCwgbWF4X3ZhbD0xLjApOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN1BlYWsgU2lnbmFsLXRvLU5vaXNlIFJhdGlvIGluIGRCIChoaWdoZXIgaXMgYmV0dGVyKS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBtc2UgPSBGLm1zZV9sb3NzKHByZWQsIHRhcmdldClcbiAgICBpZiBtc2UgPT0gMDpcbiAgICAgICAgcmV0dXJuIGZsb2F0KFx1MDAyN2luZlx1MDAyNylcbiAgICByZXR1cm4gMjAuMCAqIHRvcmNoLmxvZzEwKHRvcmNoLnRlbnNvcihtYXhfdmFsKSkgLSAxMC4wICogdG9yY2gubG9nMTAobXNlKVxuXG5kZWYgc3NpbV8xY2gocHJlZCwgdGFyZ2V0LCBDMT0wLjAxKioyLCBDMj0wLjAzKioyKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdTaW5nbGUtY2hhbm5lbCBTU0lNIGFwcHJveGltYXRpb24gKHNpbXBsaWZpZWQpLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIG11X3AsIG11X3QgPSBwcmVkLm1lYW4oKSwgdGFyZ2V0Lm1lYW4oKVxuICAgIHZhcl9wID0gcHJlZC52YXIoKTsgdmFyX3QgPSB0YXJnZXQudmFyKClcbiAgICBjb3YgICA9ICgocHJlZCAtIG11X3ApICogKHRhcmdldCAtIG11X3QpKS5tZWFuKClcbiAgICBudW0gPSAoMiptdV9wKm11X3QgKyBDMSkgKiAoMipjb3YgKyBDMilcbiAgICBkZW4gPSAobXVfcCoqMiArIG11X3QqKjIgKyBDMSkgKiAodmFyX3AgKyB2YXJfdCArIEMyKVxuICAgIHJldHVybiAobnVtIC8gZGVuKS5pdGVtKClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbkcgPSBQaXgyUGl4R2VuZXJhdG9yKClcbnJlYWxfQSA9IHRvcmNoLnJhbmRuKDEsIDMsIDY0LCA2NClcbnJlYWxfQiA9IHRvcmNoLnRhbmgocmVhbF9BICsgMC4zKSAgIyBzaW11bGF0ZSBwYWlyZWQgdGFyZ2V0XG53aXRoIHRvcmNoLm5vX2dyYWQoKTpcbiAgICBmYWtlX0IgPSBHKHJlYWxfQSlcbnByaW50KFx1MDAyN1BTTlI6IHs6LjJmfSBkQlx1MDAyNy5mb3JtYXQocHNucihmYWtlX0IsIHJlYWxfQikuaXRlbSgpKSlcbnByaW50KFx1MDAyN1NTSU06IHs6LjRmfVx1MDAyNy5mb3JtYXQoc3NpbV8xY2goZmFrZV9CLCByZWFsX0IpKSkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IkwxIExvc3MgQmx1cnM7IEdBTiBTaGFycGVucyIsImNvbnRlbnQiOiJMMSBsb3NzIGFsb25lIHByb2R1Y2VzIGJsdXJyeSBvdXRwdXRzIGJlY2F1c2UgaXQgbWluaW1pc2VzIGV4cGVjdGVkIGFic29sdXRlIGVycm9yIOKAlCBhdmVyYWdpbmcgYWNyb3NzIGFtYmlndW91cyB0ZXh0dXJlIG1vZGVzLiBUaGUgR0FOIGxvc3Mgc2hhcnBlbnMgdGhlIG91dHB1dCBieSBwZW5hbGlzaW5nIGJsdXJyaW5lc3MgYXMgYSB0ZWxsLXRhbGUgc2lnbiBvZiBmYWtlbmVzcy4gVGhlIGtleSBpbnNpZ2h0IG9mIFBpeDJQaXggaXMgdGhhdCBMMSBoYW5kbGVzIGdsb2JhbCBzdHJ1Y3R1cmUgKHNoYXBlLCBsYXlvdXQpIHdoaWxlIHRoZSBhZHZlcnNhcmlhbCBsb3NzIGhhbmRsZXMgbG9jYWwgdGV4dHVyZSAoc2hhcnBuZXNzLCBncmFpbikuIFNldHRpbmcgbGFtYmRhIHRvbyBsb3cgbGV0cyBHQU4gZG9taW5hdGUgYW5kIHByb2R1Y2VzIGFydGVmYWN0czsgdG9vIGhpZ2ggYW5kIHRoZSBvdXRwdXQgYmx1cnMgdG93YXJkIHRoZSBMMSBtaW5pbXVtLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFwcGxpY2F0aW9ucyBhbmQgTGltaXRhdGlvbnMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlBpeDJQaXggaGFzIGJlZW4gYXBwbGllZCB0byBlZGdlc+KGknBob3RvcyAodXNpbmcgSEVEIGVkZ2UgZGV0ZWN0b3IpLCBhcmNoaXRlY3R1cmFsIGxhYmVsc+KGkmZhY2FkZXMsIGFlcmlhbCBtYXBz4oaSc2F0ZWxsaXRlIGltYWdlcnksIGRheeKGkm5pZ2h0LCBCV+KGkmNvbG91ciwgYW5kIG1lZGljYWwgaW1hZ2UgbW9kYWxpdHkgdHJhbnNsYXRpb24gKE1SSeKGkkNUKS4gVGhlIGNlbnRyYWwgbGltaXRhdGlvbiBpcyB0aGUgcmVxdWlyZW1lbnQgZm9yIGFsaWduZWQgcGFpcmVkIGRhdGEg4oCUIGNvbGxlY3Rpbmcgc3VjaCBwYWlycyBpcyBleHBlbnNpdmUgYW5kIHNvbWV0aW1lcyBpbXBvc3NpYmxlIChlLmcuLCBwaG90b+KGlHBhaW50aW5nKS4gQ3ljbGVHQU4gYWRkcmVzc2VzIHVucGFpcmVkIHNldHRpbmdzLiBTUEFERS9HYXVHQU4gZXh0ZW5kcyBQaXgyUGl4IHdpdGggc3BhdGlhbGx5LWFkYXB0aXZlIG5vcm1hbGlzYXRpb24gZm9yIHNlbWFudGljIGltYWdlIHN5bnRoZXNpcyB3aXRoIGJldHRlciBxdWFsaXR5IG9uIHNlZ21lbnRhdGlvbiBtYXBzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlBpeDJQaXggdnMgUmVsYXRlZCBNZXRob2RzIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlBhaXJlZCBEYXRhIiwiR2VuZXJhdG9yIiwiRGlzY3JpbWluYXRvciIsIktleSBMb3NzIiwiQmVzdCBBcHBsaWNhdGlvbiJdLCJyb3dzIjpbWyJQaXgyUGl4IiwiUmVxdWlyZWQiLCJVLU5ldCArIHNraXAiLCJQYXRjaEdBTiA3MMOXNzAiLCJHQU4gKyBMMSIsIkVkZ2Vz4oaScGhvdG8sIG1hcOKGknNhdGVsbGl0ZSJdLFsiQ3ljbGVHQU4iLCJOb3QgcmVxdWlyZWQiLCJSZXNOZXQgKyBJTiIsIlBhdGNoR0FOIiwiR0FOICsgY3ljbGUgKyBpZGVudGl0eSIsIlN0eWxlIHRyYW5zZmVyLCBkb21haW4gYWRhcHRhdGlvbiJdLFsiU1BBREUgLyBHYXVHQU4iLCJTZWdtZW50YXRpb24gbWFwIiwiU1BBREUgUmVzTmV0IiwiTXVsdGktc2NhbGUgUGF0Y2hHQU4iLCJHQU4gKyBmZWF0dXJlIG1hdGNoICsgVkdHIiwiU2VtYW50aWPihpJwaG90b3JlYWxpc3RpYyBzeW50aGVzaXMiXSxbIkJpY3ljbGVHQU4iLCJSZXF1aXJlZCIsIlUtTmV0IiwiUGF0Y2hHQU4iLCJHQU4gKyBMMSArIEtMIiwiTXVsdGktbW9kYWwgZGl2ZXJzZSB0cmFuc2xhdGlvbiJdXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# Pix2Pix — Paired Image-to-Image Translation

Pix2Pix (Isola et al. 2017) frames image translation as a conditional GAN problem: given a paired dataset of (input image A, target image B), train a generator G to map A → B such that the output is indistinguishable from real B images. Applications include edges→photos, maps→satellite imagery, semantic labels→photorealistic images, and day→night conversion. Paired training data is the central requirement — and limitation — of Pix2Pix; when pairs are unavailable, CycleGAN is used instead.

## cGAN Formulation with L1 Reconstruction Loss

The Pix2Pix objective is L = L_cGAN(G,D) + λ·L_L1(G). The cGAN term L_cGAN encourages G to produce realistic-looking outputs that fool D. The L1 term L_L1 = E[‖y - G(x)‖₁] penalises deviation from the ground-truth target and forces global consistency. L1 is preferred over L2 because L2 tends to produce blurry outputs (it minimises expected squared error, which encourages averaging over modes). λ=100 is the standard setting — strong enough to prevent G from ignoring the input content.

```python
import torch
import torch.nn as nn

def unet_down(in_ch, out_ch, norm=True):
    layers = [nn.Conv2d(in_ch, out_ch, 4, 2, 1, bias=not norm)]
    if norm: layers.append(nn.InstanceNorm2d(out_ch))
    layers.append(nn.LeakyReLU(0.2, True))
    return nn.Sequential(*layers)

def unet_up(in_ch, out_ch, dropout=False):
    layers = [nn.ConvTranspose2d(in_ch, out_ch, 4, 2, 1, bias=False),
              nn.InstanceNorm2d(out_ch), nn.ReLU(True)]
    if dropout: layers.append(nn.Dropout(0.5))
    return nn.Sequential(*layers)

class Pix2PixGenerator(nn.Module):
    '''U-Net generator with skip connections for Pix2Pix.'''
    def __init__(self, in_ch=3, out_ch=3, ngf=32):
        super().__init__()
        self.e1 = unet_down(in_ch, ngf, norm=False)
        self.e2 = unet_down(ngf,   ngf*2)
        self.e3 = unet_down(ngf*2, ngf*4)
        self.e4 = unet_down(ngf*4, ngf*8)
        self.d1 = unet_up(ngf*8,   ngf*4, dropout=True)
        self.d2 = unet_up(ngf*4*2, ngf*2)
        self.d3 = unet_up(ngf*2*2, ngf)
        self.d4 = nn.Sequential(
            nn.ConvTranspose2d(ngf*2, out_ch, 4, 2, 1), nn.Tanh())

    def forward(self, x):
        e1=self.e1(x); e2=self.e2(e1); e3=self.e3(e2); e4=self.e4(e3)
        d=self.d1(e4); d=self.d2(torch.cat([d,e3],1))
        d=self.d3(torch.cat([d,e2],1))
        return self.d4(torch.cat([d,e1],1))

G=Pix2PixGenerator()
print('Generator output:', G(torch.randn(1,3,64,64)).shape)
```

## PatchGAN Discriminator

Instead of classifying the entire image as real or fake, the PatchGAN discriminator classifies overlapping 70×70 patches. The output is a spatial map where each value is the real/fake score for the corresponding patch. This design has three advantages: (1) it focuses D's capacity on local texture and high-frequency details where GAN training is most useful; (2) it has fewer parameters than a full-image D; and (3) it can be applied to images of any resolution — just run the convolutional D across the full image.

```python
import torch
import torch.nn as nn

def d_block(in_ch, out_ch, stride=2, norm=True):
    layers = [nn.Conv2d(in_ch, out_ch, 4, stride, 1, bias=not norm)]
    if norm: layers.append(nn.InstanceNorm2d(out_ch))
    layers.append(nn.LeakyReLU(0.2, True))
    return nn.Sequential(*layers)

class PatchGANDiscriminator(nn.Module):
    '''70x70 PatchGAN: each output pixel scores one overlapping patch.'''
    def __init__(self, in_ch=6, ndf=32):
        super().__init__()
        # Input: concat(real_A, real_B or fake_B) -> 6 channels
        self.net = nn.Sequential(
            d_block(in_ch, ndf,    norm=False),  # 64->32
            d_block(ndf,   ndf*2),               # 32->16
            d_block(ndf*2, ndf*4),               # 16->8
            d_block(ndf*4, ndf*8, stride=1),     # 8->8
            nn.Conv2d(ndf*8, 1, 4, 1, 1))        # patch logits

    def forward(self, x, y):
        return self.net(torch.cat([x, y], 1))   # condition on input

D = PatchGANDiscriminator()
x = torch.randn(2, 3, 64, 64)
y = torch.randn(2, 3, 64, 64)
out = D(x, y)
print('PatchGAN output shape:', out.shape)  # spatial patch map
```

## Combined GAN and L1 Loss Training Step

Training alternates between updating D and G. D is updated to maximise log D(x,y) + log(1−D(x,G(x))). G is updated to minimise the adversarial loss log(1−D(x,G(x))) plus λ·L1(G(x),y). In practice, G minimises −log D(x,G(x)) (non-saturating variant) for stronger gradients early in training. The L1 coefficient λ=100 means the generator primarily optimises reconstruction fidelity, using the adversarial signal to sharpen textures that L1 would otherwise blur.

```python
import torch
import torch.nn as nn

def pix2pix_step(G, D, real_A, real_B, lam=100.0):
    '''Compute G and D losses for one training step.'''
    bce = nn.BCEWithLogitsLoss()
    l1  = nn.L1Loss()
    fake_B = G(real_A)
    # -- Discriminator --
    real_out = D(real_A, real_B)
    fake_out = D(real_A, fake_B.detach())
    loss_D   = 0.5 * (bce(real_out, torch.ones_like(real_out)) +
                      bce(fake_out, torch.zeros_like(fake_out)))
    # -- Generator --
    fake_out_g  = D(real_A, fake_B)
    loss_G_adv  = bce(fake_out_g, torch.ones_like(fake_out_g))
    loss_G_l1   = l1(fake_B, real_B) * lam
    loss_G      = loss_G_adv + loss_G_l1
    return loss_D, loss_G, loss_G_adv.item(), loss_G_l1.item()

G = Pix2PixGenerator(); D = PatchGANDiscriminator()
rA = torch.randn(2, 3, 64, 64); rB = torch.randn(2, 3, 64, 64)
ld, lg, adv, l1v = pix2pix_step(G, D, rA, rB)
print('loss_D={:.3f}  loss_G_adv={:.3f}  loss_G_L1={:.3f}'.format(
      ld.item(), adv, l1v))
```

## Skip Connections in the U-Net

The U-Net architecture uses encoder-decoder skip connections: activations from encoder layer i are concatenated to the corresponding decoder layer n−i. This preserves fine-grained spatial detail (textures, edges, precise geometry) that would otherwise be lost through the bottleneck. Without skip connections, the generator must re-synthesise all spatial structure from the compressed bottleneck representation — a harder task that results in blurrier outputs. Skip connections allow the decoder to focus on high-level style and content rather than reconstructing low-level structure from scratch.

- Skip from e1 to d4: preserves finest spatial detail (edges, textures)
- Skip from e2 to d3: preserves mid-scale structure
- Skip from e3 to d2: preserves coarse layout
- Bottleneck (e4): forces global context compression — the only path for holistic reasoning
- Dropout on decoder (d1): adds stochasticity, acts as regularisation during training
- Instance norm (not batch norm): per-image normalisation avoids cross-image contamination in paired training

## Evaluation: PSNR and SSIM

Paired image translation enables pixel-level metrics against ground truth. PSNR (Peak Signal-to-Noise Ratio) measures MSE in dB: PSNR = 20·log₁₀(MAX) − 10·log₁₀(MSE). Higher is better; typical values for good translation: 25–35 dB. SSIM (Structural Similarity Index) measures luminance, contrast, and structure similarity in [−1,1]. Higher is better; SSIM > 0.9 is considered high quality. Perceptual metrics (LPIPS) and FID are also used when ground truth pairs are available.

```python
import torch
import torch.nn.functional as F

def psnr(pred, target, max_val=1.0):
    '''Peak Signal-to-Noise Ratio in dB (higher is better).'''
    mse = F.mse_loss(pred, target)
    if mse == 0:
        return float('inf')
    return 20.0 * torch.log10(torch.tensor(max_val)) - 10.0 * torch.log10(mse)

def ssim_1ch(pred, target, C1=0.01**2, C2=0.03**2):
    '''Single-channel SSIM approximation (simplified).'''
    mu_p, mu_t = pred.mean(), target.mean()
    var_p = pred.var(); var_t = target.var()
    cov   = ((pred - mu_p) * (target - mu_t)).mean()
    num = (2*mu_p*mu_t + C1) * (2*cov + C2)
    den = (mu_p**2 + mu_t**2 + C1) * (var_p + var_t + C2)
    return (num / den).item()

torch.manual_seed(0)
G = Pix2PixGenerator()
real_A = torch.randn(1, 3, 64, 64)
real_B = torch.tanh(real_A + 0.3)  # simulate paired target
with torch.no_grad():
    fake_B = G(real_A)
print('PSNR: {:.2f} dB'.format(psnr(fake_B, real_B).item()))
print('SSIM: {:.4f}'.format(ssim_1ch(fake_B, real_B)))
```

> **L1 Loss Blurs; GAN Sharpens**: L1 loss alone produces blurry outputs because it minimises expected absolute error — averaging across ambiguous texture modes. The GAN loss sharpens the output by penalising blurriness as a tell-tale sign of fakeness. The key insight of Pix2Pix is that L1 handles global structure (shape, layout) while the adversarial loss handles local texture (sharpness, grain). Setting lambda too low lets GAN dominate and produces artefacts; too high and the output blurs toward the L1 minimum.

## Applications and Limitations

Pix2Pix has been applied to edges→photos (using HED edge detector), architectural labels→facades, aerial maps→satellite imagery, day→night, BW→colour, and medical image modality translation (MRI→CT). The central limitation is the requirement for aligned paired data — collecting such pairs is expensive and sometimes impossible (e.g., photo↔painting). CycleGAN addresses unpaired settings. SPADE/GauGAN extends Pix2Pix with spatially-adaptive normalisation for semantic image synthesis with better quality on segmentation maps.

## Pix2Pix vs Related Methods

| Method | Paired Data | Generator | Discriminator | Key Loss | Best Application |
| --- | --- | --- | --- | --- | --- |
| Pix2Pix | Required | U-Net + skip | PatchGAN 70×70 | GAN + L1 | Edges→photo, map→satellite |
| CycleGAN | Not required | ResNet + IN | PatchGAN | GAN + cycle + identity | Style transfer, domain adaptation |
| SPADE / GauGAN | Segmentation map | SPADE ResNet | Multi-scale PatchGAN | GAN + feature match + VGG | Semantic→photorealistic synthesis |
| BicycleGAN | Required | U-Net | PatchGAN | GAN + L1 + KL | Multi-modal diverse translation |

---

