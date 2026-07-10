---
title: "CycleGAN — Unpaired Image Translation via Cycle Consistency"
slug: "cyclegan-unpaired-translation"
description: "CycleGAN (Zhu et al. 2017) learns image-to-image translation without paired training data using two generators G:X->Y and F:Y->X with cycle consistency F(G(x))~x enforced by an L1 loss, enabling horse-to-zebra, photo-to-painting, and other domain transfers."
tags: ["deep-learning", "generative-models", "gans", "normalizing-flows"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ3ljbGVHQU4gKFpodSBldCBhbC4gMjAxNykgc29sdmVzIHRoZSBmdW5kYW1lbnRhbCBsaW1pdGF0aW9uIG9mIFBpeDJQaXg6IHRoZSBuZWVkIGZvciBhbGlnbmVkIHBhaXJlZCBpbWFnZXMuIEluc3RlYWQsIEN5Y2xlR0FOIGxlYXJucyBmcm9tIHR3byB1bnJlbGF0ZWQgY29sbGVjdGlvbnMgb2YgaW1hZ2VzIOKAlCBkb21haW4gWCAoZS5nLiwgcGhvdG9zIG9mIGhvcnNlcykgYW5kIGRvbWFpbiBZIChlLmcuLCBwaG90b3Mgb2YgemVicmFzKSDigJQgd2l0aCBubyBjb3JyZXNwb25kZW5jZSBiZXR3ZWVuIHRoZW0uIFRoZSBrZXkgaW5zaWdodCBpcyB0aGUgY3ljbGUgY29uc2lzdGVuY3kgY29uc3RyYWludDogYSByb3VuZC10cmlwIHRyYW5zbGF0aW9uIFjihpJZ4oaSWCBzaG91bGQgcmVjb3ZlciB0aGUgb3JpZ2luYWwgaW1hZ2UuIFRoaXMgY29uc3RyYWludCBpcyBwb3dlcmZ1bCBlbm91Z2ggdG8gcHJldmVudCBHIGZyb20gbWFwcGluZyBldmVyeXRoaW5nIHRvIGEgc2luZ2xlIG1vZGUgYW5kIGVuc3VyZXMgc2VtYW50aWNhbGx5IG1lYW5pbmdmdWwgdHJhbnNsYXRpb25zIGVtZXJnZSBmcm9tIHVucGFpcmVkIGRhdGEuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHdvIEdlbmVyYXRvcnMgYW5kIFR3byBEaXNjcmltaW5hdG9ycyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQ3ljbGVHQU4gdXNlcyB0d28gZ2VuZXJhdG9yczogRzogWOKGklkgdHJhbnNsYXRlcyBYLWRvbWFpbiBpbWFnZXMgdG8gbG9vayBsaWtlIFktZG9tYWluLCBhbmQgRjogWeKGklggdHJhbnNsYXRlcyBZLWRvbWFpbiBpbWFnZXMgdG8gbG9vayBsaWtlIFgtZG9tYWluLiBUd28gY29ycmVzcG9uZGluZyBkaXNjcmltaW5hdG9ycyBEX1ggYW5kIERfWSBjbGFzc2lmeSB3aGV0aGVyIGFuIGltYWdlIGJlbG9uZ3MgdG8gZG9tYWluIFggb3IgWSByZXNwZWN0aXZlbHkuIEcgYW5kIEYgYXJlIFJlc05ldC1iYXNlZCB3aXRoIGluc3RhbmNlIG5vcm1hbGlzYXRpb247IERfWCBhbmQgRF9ZIHVzZSBQYXRjaEdBTi4gVGhlIG1vZGVsIGhhcyByb3VnaGx5IDExTSBwYXJhbWV0ZXJzIHBlciBnZW5lcmF0b3IgYW5kIDIuN00gcGVyIGRpc2NyaW1pbmF0b3IuIEluc3RhbmNlIG5vcm1hbGlzYXRpb24gKHBlci1pbWFnZSwgbm90IHBlci1iYXRjaCkgd2FzIGZvdW5kIGNyaXRpY2FsIGZvciBzdGFibGUgdW5wYWlyZWQgdHJhbnNsYXRpb24gdHJhaW5pbmcuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFJlc0Jsb2NrKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNoKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLlJlZmxlY3Rpb25QYWQyZCgxKSwgbm4uQ29udjJkKGNoLCBjaCwgMywgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5JbnN0YW5jZU5vcm0yZChjaCksIG5uLlJlTFUoVHJ1ZSksXG4gICAgICAgICAgICBubi5SZWZsZWN0aW9uUGFkMmQoMSksIG5uLkNvbnYyZChjaCwgY2gsIDMsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uSW5zdGFuY2VOb3JtMmQoY2gpKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiByZXR1cm4geCArIHNlbGYubmV0KHgpXG5cbmNsYXNzIEN5Y2xlR2VuZXJhdG9yKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoPTMsIG5nZj0zMiwgbl9yZXM9NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBtb2RlbCA9IFtubi5SZWZsZWN0aW9uUGFkMmQoMyksIG5uLkNvbnYyZChpbl9jaCwgbmdmLCA3LCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgICAgICAgbm4uSW5zdGFuY2VOb3JtMmQobmdmKSwgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgICAgICAgbm4uQ29udjJkKG5nZiwgbmdmKjIsIDMsIDIsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgICAgICBubi5JbnN0YW5jZU5vcm0yZChuZ2YqMiksIG5uLlJlTFUoVHJ1ZSldXG4gICAgICAgIG1vZGVsICs9IFtSZXNCbG9jayhuZ2YqMikgZm9yIF8gaW4gcmFuZ2Uobl9yZXMpXVxuICAgICAgICBtb2RlbCArPSBbbm4uQ29udlRyYW5zcG9zZTJkKG5nZioyLCBuZ2YsIDMsIDIsIDEsIG91dHB1dF9wYWRkaW5nPTEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgICAgICAgbm4uSW5zdGFuY2VOb3JtMmQobmdmKSwgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgICAgICAgIG5uLlJlZmxlY3Rpb25QYWQyZCgzKSwgbm4uQ29udjJkKG5nZiwgaW5fY2gsIDcpLCBubi5UYW5oKCldXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbCgqbW9kZWwpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6IHJldHVybiBzZWxmLm5ldCh4KVxuXG5HX1hZID0gQ3ljbGVHZW5lcmF0b3IoKVxueCA9IHRvcmNoLnJhbmRuKDEsIDMsIDY0LCA2NClcbnByaW50KFx1MDAyN0N5Y2xlR0FOIEcgb3V0cHV0Olx1MDAyNywgR19YWSh4KS5zaGFwZSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDeWNsZSBDb25zaXN0ZW5jeSBMb3NzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY3ljbGUgY29uc2lzdGVuY3kgbG9zcyBlbmZvcmNlcyB0aGF0IHJvdW5kLXRyaXAgdHJhbnNsYXRpb25zIHJlY29uc3RydWN0IHRoZSBvcmlnaW5hbDogRihHKHgpKSDiiYggeCAoZm9yd2FyZCBjeWNsZSkgYW5kIEcoRih5KSkg4omIIHkgKGJhY2t3YXJkIGN5Y2xlKS4gVGhlIGxvc3MgdXNlcyBMMSBub3JtOiBMX2N5YyA9IM67wrcoRVvigJZGKEcoeCkp4oiSeOKAluKCgV0gKyBFW+KAlkcoRih5KSniiJJ54oCW4oKBXSkuIFdpdGhvdXQgdGhpcyBjb25zdHJhaW50LCB0aGUgbmV0d29ya3MgbGVhcm4gYSBtYXBwaW5nIHRoYXQgc2F0aXNmaWVzIHRoZSBHQU4gb2JqZWN0aXZlIGJ1dCBpcyBvdGhlcndpc2UgdW5jb25zdHJhaW5lZCDigJQgdHlwaWNhbGx5IGRlZ2VuZXJhdGluZyB0byBtb2RlIGNvbGxhcHNlIHdoZXJlIEcgbWFwcyBhbGwgeCB0byB0aGUgc2FtZSB5LiBUaGUgY3ljbGUgbG9zcyBpcyB3aGF0IGdpdmVzIEN5Y2xlR0FOIGl0cyByZW1hcmthYmxlIGFiaWxpdHkgdG8gbGVhcm4gbWVhbmluZ2Z1bCBzZW1hbnRpYyBjb3JyZXNwb25kZW5jZXMgKGhvcnNlIGJvZHkg4oaSIHplYnJhIGJvZHksIG5vdCBqdXN0IGF2ZXJhZ2UgemVicmEgdGV4dHVyZSkuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBjeWNsZV9jb25zaXN0ZW5jeV9sb3NzKEdfWFksIEdfWVgsIHJlYWxfWCwgcmVhbF9ZLCBsYW09MTAuMCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3TF9jeWMgPSBsYW0gKiAofHxGKEcoeCkpLXh8fF8xICsgfHxHKEYoeSkpLXl8fF8xKS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBsMSA9IG5uLkwxTG9zcygpXG4gICAgZmFrZV9ZID0gR19YWShyZWFsX1gpICAgICAgICAgICAgIyBYIC1cdTAwM2UgWVxuICAgIHJlY19YICA9IEdfWVgoZmFrZV9ZKSAgICAgICAgICAgICMgWSAtXHUwMDNlIFggIChyZWNvbnN0cnVjdClcbiAgICBmYWtlX1ggPSBHX1lYKHJlYWxfWSkgICAgICAgICAgICAjIFkgLVx1MDAzZSBYXG4gICAgcmVjX1kgID0gR19YWShmYWtlX1gpICAgICAgICAgICAgIyBYIC1cdTAwM2UgWSAgKHJlY29uc3RydWN0KVxuICAgIGxvc3NfZndkID0gbDEocmVjX1gsIHJlYWxfWCkgICAgICMgZm9yd2FyZCBjeWNsZVxuICAgIGxvc3NfYndkID0gbDEocmVjX1ksIHJlYWxfWSkgICAgICMgYmFja3dhcmQgY3ljbGVcbiAgICBsb3NzID0gbGFtICogKGxvc3NfZndkICsgbG9zc19id2QpXG4gICAgcmV0dXJuIGxvc3MsIGxvc3NfZndkLml0ZW0oKSwgbG9zc19id2QuaXRlbSgpXG5cbkdfWFkgPSBDeWNsZUdlbmVyYXRvcigpOyBHX1lYID0gQ3ljbGVHZW5lcmF0b3IoKVxucnggPSB0b3JjaC5yYW5kbigxLCAzLCA2NCwgNjQpXG5yeSA9IHRvcmNoLnJhbmRuKDEsIDMsIDY0LCA2NClcbmxvc3MsIGZ3ZCwgYndkID0gY3ljbGVfY29uc2lzdGVuY3lfbG9zcyhHX1hZLCBHX1lYLCByeCwgcnkpXG5wcmludChcdTAwMjdDeWNsZSBsb3NzOiB7Oi40Zn0gIGZ3ZDogezouNGZ9ICBid2Q6IHs6LjRmfVx1MDAyNy5mb3JtYXQoXG4gICAgICBsb3NzLml0ZW0oKSwgZndkLCBid2QpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IklkZW50aXR5IExvc3MgZm9yIENvbG9yIFByZXNlcnZhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGlkZW50aXR5IGxvc3MgYWRkcyB0aGUgY29uc3RyYWludCB0aGF0IEcgc2hvdWxkIGFjdCBhcyB0aGUgaWRlbnRpdHkgd2hlbiBnaXZlbiBhbiBpbWFnZSBhbHJlYWR5IGluIGl0cyB0YXJnZXQgZG9tYWluOiBHKHkpIOKJiCB5IGFuZCBGKHgpIOKJiCB4LiBMX2lkID0gzrtfaWTCtyhFW+KAlkcoeSniiJJ54oCW4oKBXSArIEVb4oCWRih4KeKIknjigJbigoFdKS4gVHlwaWNhbGx5IM67X2lkID0gMC41wrfOu19jeWMuIFdpdGhvdXQgdGhlIGlkZW50aXR5IGxvc3MsIEcgbWF5IGZyZWVseSBzaGlmdCB0aGUgY29sb3VyIHBhbGV0dGUgb2YgaW1hZ2VzIHRoYXQgZG9uXHUwMDI3dCBuZWVkIHRyYW5zbGF0aW9uIOKAlCBmb3IgZXhhbXBsZSwgRyB0cmFpbmVkIGZvciBwaG90b+KGkk1vbmV0IG1pZ2h0IGFkZCBhIHdhcm0gb3JhbmdlIHRvbmUgdG8gcGhvdG9zIHRoYXQgYWxyZWFkeSBsb29rIHBhaW50ZXJseS4gVGhlIGlkZW50aXR5IGxvc3MgcHJldmVudHMgdGhpcyB1bndhbnRlZCBjb2xvdXIgc2hpZnQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiBpZGVudGl0eV9sb3NzKEdfWFksIEdfWVgsIHJlYWxfWCwgcmVhbF9ZLCBsYW1faWQ9NS4wKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdQZW5hbGlzZSBHX1hZKHkpICE9IHkgYW5kIEdfWVgoeCkgIT0geC5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBsMSAgID0gbm4uTDFMb3NzKClcbiAgICBpZF9ZID0gR19YWShyZWFsX1kpICAgIyBHIHNob3VsZCBiZSBpZGVudGl0eSBvbiBZLWRvbWFpbiBpbnB1dFxuICAgIGlkX1ggPSBHX1lYKHJlYWxfWCkgICAjIEYgc2hvdWxkIGJlIGlkZW50aXR5IG9uIFgtZG9tYWluIGlucHV0XG4gICAgbG9zcyA9IGxhbV9pZCAqIChsMShpZF9ZLCByZWFsX1kpICsgbDEoaWRfWCwgcmVhbF9YKSlcbiAgICByZXR1cm4gbG9zc1xuXG5HX1hZID0gQ3ljbGVHZW5lcmF0b3IoKTsgR19ZWCA9IEN5Y2xlR2VuZXJhdG9yKClcbnJ4ID0gdG9yY2gucmFuZG4oMSwgMywgNjQsIDY0KTsgcnkgPSB0b3JjaC5yYW5kbigxLCAzLCA2NCwgNjQpXG5sb3NzX2lkID0gaWRlbnRpdHlfbG9zcyhHX1hZLCBHX1lYLCByeCwgcnkpXG5wcmludChcdTAwMjdJZGVudGl0eSBsb3NzOlx1MDAyNywgcm91bmQobG9zc19pZC5pdGVtKCksIDQpKVxucHJpbnQoXHUwMDI3V2l0aG91dCBpZGVudGl0eSBsb3NzLCBHIG1heSBzaGlmdCBvdmVyYWxsIGNvbG9yIGh1ZSBvZiBpbnB1dCBpbWFnZXMuXHUwMDI3KSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZ1bGwgT2JqZWN0aXZlIGFuZCBUcmFpbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGZ1bGwgQ3ljbGVHQU4gb2JqZWN0aXZlIGlzIEwgPSBMX0dBTihHLERfWSxYLFkpICsgTF9HQU4oRixEX1gsWSxYKSArIM67wrdMX2N5YyhHLEYpICsgzrtfaWTCt0xfaWQoRyxGKS4gVHJhaW5pbmcgYWx0ZXJuYXRlczogdXBkYXRlIERfWCBhbmQgRF9ZIHVzaW5nIHRoZSBMU0dBTiAobGVhc3Qtc3F1YXJlcykgb2JqZWN0aXZlIChtb3JlIHN0YWJsZSB0aGFuIEJDRSksIHRoZW4gdXBkYXRlIEcgYW5kIEYgam9pbnRseSB1c2luZyB0aGUgZnVsbCBsb3NzIHdpdGggY3ljbGUgYW5kIGlkZW50aXR5IHRlcm1zLiBBIHJlcGxheSBidWZmZXIgb2YgNTAgcHJldmlvdXNseSBnZW5lcmF0ZWQgaW1hZ2VzIGlzIHVzZWQgd2hlbiB1cGRhdGluZyBEIHRvIHByZXZlbnQgb3NjaWxsYXRpb25zLiBMZWFybmluZyByYXRlIDAuMDAwMiB3aXRoIEFkYW07IGxpbmVhciBkZWNheSBhZnRlciAxMDAgZXBvY2hzLiJ9LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoiaW5mbyIsInRpdGxlIjoiV2hhdCBDeWNsZUdBTiBDYW5ub3QgRG8iLCJjb250ZW50IjoiQ3ljbGUgY29uc2lzdGVuY3kgZW5mb3JjZXMgdGhhdCB0aGUgb3ZlcmFsbCBpbWFnZSBzdHJ1Y3R1cmUgaXMgcHJlc2VydmVkIGJ1dCBkb2VzIG5vdCBjb25zdHJhaW4gbG9jYWwgZ2VvbWV0cnkuIEN5Y2xlR0FOIGNhbm5vdCByZWxpYWJseSBjaGFuZ2Ugb2JqZWN0IGNvdW50LCBzaXplLCBvciBzaGFwZSDigJQgaXQgY2FuIGNoYW5nZSB0ZXh0dXJlIGFuZCBjb2xvdXIgKGhvcnNlIHN0cmlwZXMpIGJ1dCBub3QgcmVtb2RlbCB0aGUgYm9keSBzaGFwZSBvciBhZGQvcmVtb3ZlIG9iamVjdHMuIFRhc2tzIHJlcXVpcmluZyBzdHJ1Y3R1cmFsIGNoYW5nZSAoY2F04oaSZG9nLCBsYW5kc2NhcGXihpJwb3J0cmFpdCkgcmVxdWlyZSBhZGRpdGlvbmFsIGNvbnN0cmFpbnRzIG9yIGEgZGlmZmVyZW50IGZvcm11bGF0aW9uIHN1Y2ggYXMgR2VvR0FOIG9yIGdlb21ldHJ5LWF3YXJlIHRyYW5zbGF0aW9uIG1ldGhvZHMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQ29udHJhc3RpdmUgVW5wYWlyZWQgVHJhbnNsYXRpb24gKENVVCkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNVVCAoUGFyayBldCBhbC4gMjAyMCkgYWNoaWV2ZXMgdW5wYWlyZWQgdHJhbnNsYXRpb24gd2l0aG91dCBhIHJldmVyc2UgZ2VuZXJhdG9yIEYgb3IgY3ljbGUgY29uc2lzdGVuY3kuIEluc3RlYWQsIGl0IHVzZXMgcGF0Y2gtd2lzZSBjb250cmFzdGl2ZSBsb3NzIChQYXRjaE5DRSk6IGZvciBlYWNoIHBhdGNoIGxvY2F0aW9uLCB0aGUgY29ycmVzcG9uZGluZyBwYXRjaCBpbiB0aGUgZ2VuZXJhdGVkIGltYWdlIHNob3VsZCBiZSBjbG9zZXIgdG8gdGhlIHJlYWwgc291cmNlIHBhdGNoIHRoYW4gdG8gcGF0Y2hlcyBhdCBvdGhlciBsb2NhdGlvbnMuIFRoaXMgcHJlc2VydmVzIGNvbnRlbnQgd2l0aG91dCByZXF1aXJpbmcgRihHKHgpKeKJiHguIENVVCB1c2VzIG9ubHkgb25lIGdlbmVyYXRvciBhbmQgb25lIGRpc2NyaW1pbmF0b3Ig4oCUIGhhbGYgdGhlIHBhcmFtZXRlcnMgb2YgQ3ljbGVHQU4g4oCUIGFuZCBpcyByb3VnaGx5IDLDlyBmYXN0ZXIgdG8gdHJhaW4uIEl0IGFjaGlldmVzIGNvbXBhcmFibGUgb3IgYmV0dGVyIEZJRCBvbiBob3JzZeKGlHplYnJhIGFuZCBvdGhlciBiZW5jaG1hcmtzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5kZWYgcGF0Y2hfbmNlX2xvc3MoZmVhdF9xLCBmZWF0X2ssIHRhdT0wLjA3KTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdQYXRjaE5DRTogcXVlcnkgKGdlbmVyYXRlZCkgdnMga2V5IChzb3VyY2UpIHBhdGNoIGZlYXR1cmVzLlxuICAgIFBvc2l0aXZlIHBhaXI6IHNhbWUgc3BhdGlhbCBsb2NhdGlvbi4gTmVnYXRpdmVzOiBvdGhlciBsb2NhdGlvbnMuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZmVhdF9xID0gRi5ub3JtYWxpemUoZmVhdF9xLCBkaW09MSkgICMgKE4sIEMpXG4gICAgZmVhdF9rID0gRi5ub3JtYWxpemUoZmVhdF9rLCBkaW09MSkgICMgKE4sIEMpXG4gICAgbG9naXRzID0gdG9yY2gubW0oZmVhdF9xLCBmZWF0X2sudCgpKSAvIHRhdSAgIyAoTiwgTilcbiAgICBsYWJlbHMgPSB0b3JjaC5hcmFuZ2UobG9naXRzLnNpemUoMCksIGRldmljZT1sb2dpdHMuZGV2aWNlKVxuICAgIHJldHVybiBGLmNyb3NzX2VudHJvcHkobG9naXRzLCBsYWJlbHMpXG5cbiMgQ29tcGFyaXNvbjogbWVtb3J5IGFuZCBwYXJhbWV0ZXIgY291bnRcbmRlZiBtb2RlbF9zdGF0cyhuYW1lLCBuX3BhcmFtcyk6XG4gICAgcHJpbnQoXHUwMDI3e306IHs6LH0gcGFyYW1zICAoezouMWZ9TSlcdTAwMjcuZm9ybWF0KG5hbWUsIG5fcGFyYW1zLCBuX3BhcmFtcy8xZTYpKVxuXG5OLCBDID0gMjU2LCAyNTZcbmZlYXRfcSA9IHRvcmNoLnJhbmRuKE4sIEMpXG5mZWF0X2sgPSB0b3JjaC5yYW5kbihOLCBDKVxubmNlID0gcGF0Y2hfbmNlX2xvc3MoZmVhdF9xLCBmZWF0X2spXG5wcmludChcdTAwMjdQYXRjaE5DRSBsb3NzOlx1MDAyNywgcm91bmQobmNlLml0ZW0oKSwgNCkpXG5wcmludChcdTAwMjdDVVQ6IDEgZ2VuZXJhdG9yICsgUGF0Y2hOQ0UgLS0gbm8gRiwgbm8gY3ljbGUsIH4yeCBmYXN0ZXIgdGhhbiBDeWNsZUdBTlx1MDAyNykifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJBcHBsaWNhdGlvbnMgYW5kIEtub3duIExpbWl0YXRpb25zIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJDeWNsZUdBTiBoYXMgYmVlbiBhcHBsaWVkIHRvIGhvcnNl4oaUemVicmEgKHRleHR1cmUgY2hhbmdlKSwgYXBwbGXihpRvcmFuZ2UgKHRleHR1cmUgKyBjb2xvdXIpLCBwaG90b+KGlE1vbmV0IHBhaW50aW5nLCBwaG90b+KGlFZhbiBHb2doLCBhZXJpYWzihpJtYXAsIHN1bW1lcuKGkndpbnRlciwgYW5kIG1lZGljYWwgaW1hZ2Ugc3ludGhlc2lzIChDVOKGkk1SSSkuIExpbWl0YXRpb25zOiBjYW5ub3QgY2hhbmdlIGdlb21ldHJ5IG9yIGNvdW50OyByZXF1aXJlcyBkb21haW4gZ2FwIHRvIGJlIG1haW5seSB0ZXh0dXJlL2NvbG91cjsgY2FuIGhhbGx1Y2luYXRlIHNwdXJpb3VzIHBhdHRlcm5zIHdoZW4gc291cmNlIGFuZCB0YXJnZXQgZG9tYWlucyBoYXZlIHZlcnkgZGlmZmVyZW50IHNlbWFudGljczsgdHJhaW5pbmcgY2FuIGJlIHVuc3RhYmxlIGFuZCBzZW5zaXRpdmUgdG8gzrsgdmFsdWVzLiBDVVQgYW5kIHJlY2VudCBkaWZmdXNpb24tYmFzZWQgbWV0aG9kcyBhZGRyZXNzIHNldmVyYWwgb2YgdGhlc2UgbGltaXRhdGlvbnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJIb3JzZeKGknplYnJhOiB0ZXh0dXJlIGNoYW5nZSB3b3JrcyB3ZWxsIChzdHJpcGVzIGFkZGVkIG5hdHVyYWxseSkiLCJBcHBsZeKGkm9yYW5nZTogY29sb3VyICsgdGV4dHVyZSBjaGFuZ2UsIHNoYXBlIHByZXNlcnZlZCIsIlBob3Rv4oaSTW9uZXQ6IGFydGlzdGljIHN0eWxlIHRyYW5zZmVycmVkLCBzdHJ1Y3R1cmUgcHJlc2VydmVkIiwiUGhvdG/ihpJWYW4gR29naDogbW9yZSBhZ2dyZXNzaXZlIHN0eWxlLCBvY2Nhc2lvbmFsIGdlb21ldHJ5IGRpc3RvcnRpb24iLCJDYXTihpJkb2c6IG9mdGVuIGZhaWxzIGR1ZSB0byBnZW9tZXRyaWMgZGlmZmVyZW5jZXMg4oCUIGJleW9uZCBDeWNsZUdBTlx1MDAyN3Mgc2NvcGUiLCJNZWRpY2FsIENU4oaSTVJJOiBjcm9zcy1tb2RhbGl0eSBzeW50aGVzaXMgZm9yIGRhdGEgYXVnbWVudGF0aW9uIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik1ldGhvZCBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1ldGhvZCIsIlBhaXJlZCBEYXRhIiwiR2VuZXJhdG9ycyIsIkRpc2NyaW1pbmF0b3JzIiwiQ3ljbGUgTG9zcyIsIlRyYWluaW5nIFNwZWVkIiwiRklEIFF1YWxpdHkiXSwicm93cyI6W1siUGl4MlBpeCIsIlJlcXVpcmVkIiwiMSIsIjEgUGF0Y2hHQU4iLCJObyIsIkZhc3QiLCJCZXN0ICh3aXRoIHBhaXJzKSJdLFsiQ3ljbGVHQU4iLCJOb3QgcmVxdWlyZWQiLCIyIChHIGFuZCBGKSIsIjIgUGF0Y2hHQU4iLCJZZXMgKM67PTEwKSIsIk1vZGVyYXRlIiwiR29vZCJdLFsiVU5JVCIsIk5vdCByZXF1aXJlZCIsIjIgVkFFLUdBTiIsIjIiLCJObyAoc2hhcmVkIGxhdGVudCkiLCJTbG93IiwiQ29tcGFyYWJsZSJdLFsiQ1VUIiwiTm90IHJlcXVpcmVkIiwiMSBvbmx5IiwiMSBQYXRjaEdBTiIsIk5vIChQYXRjaE5DRSkiLCJ+MnggZmFzdGVyIiwiQ29tcGFyYWJsZS9iZXR0ZXIiXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# CycleGAN — Unpaired Image Translation via Cycle Consistency

CycleGAN (Zhu et al. 2017) solves the fundamental limitation of Pix2Pix: the need for aligned paired images. Instead, CycleGAN learns from two unrelated collections of images — domain X (e.g., photos of horses) and domain Y (e.g., photos of zebras) — with no correspondence between them. The key insight is the cycle consistency constraint: a round-trip translation X→Y→X should recover the original image. This constraint is powerful enough to prevent G from mapping everything to a single mode and ensures semantically meaningful translations emerge from unpaired data.

## Two Generators and Two Discriminators

CycleGAN uses two generators: G: X→Y translates X-domain images to look like Y-domain, and F: Y→X translates Y-domain images to look like X-domain. Two corresponding discriminators D_X and D_Y classify whether an image belongs to domain X or Y respectively. G and F are ResNet-based with instance normalisation; D_X and D_Y use PatchGAN. The model has roughly 11M parameters per generator and 2.7M per discriminator. Instance normalisation (per-image, not per-batch) was found critical for stable unpaired translation training.

```python
import torch
import torch.nn as nn

class ResBlock(nn.Module):
    def __init__(self, ch):
        super().__init__()
        self.net = nn.Sequential(
            nn.ReflectionPad2d(1), nn.Conv2d(ch, ch, 3, bias=False),
            nn.InstanceNorm2d(ch), nn.ReLU(True),
            nn.ReflectionPad2d(1), nn.Conv2d(ch, ch, 3, bias=False),
            nn.InstanceNorm2d(ch))
    def forward(self, x): return x + self.net(x)

class CycleGenerator(nn.Module):
    def __init__(self, in_ch=3, ngf=32, n_res=4):
        super().__init__()
        model = [nn.ReflectionPad2d(3), nn.Conv2d(in_ch, ngf, 7, bias=False),
                 nn.InstanceNorm2d(ngf), nn.ReLU(True),
                 nn.Conv2d(ngf, ngf*2, 3, 2, 1, bias=False),
                 nn.InstanceNorm2d(ngf*2), nn.ReLU(True)]
        model += [ResBlock(ngf*2) for _ in range(n_res)]
        model += [nn.ConvTranspose2d(ngf*2, ngf, 3, 2, 1, output_padding=1, bias=False),
                  nn.InstanceNorm2d(ngf), nn.ReLU(True),
                  nn.ReflectionPad2d(3), nn.Conv2d(ngf, in_ch, 7), nn.Tanh()]
        self.net = nn.Sequential(*model)
    def forward(self, x): return self.net(x)

G_XY = CycleGenerator()
x = torch.randn(1, 3, 64, 64)
print('CycleGAN G output:', G_XY(x).shape)
```

## Cycle Consistency Loss

The cycle consistency loss enforces that round-trip translations reconstruct the original: F(G(x)) ≈ x (forward cycle) and G(F(y)) ≈ y (backward cycle). The loss uses L1 norm: L_cyc = λ·(E[‖F(G(x))−x‖₁] + E[‖G(F(y))−y‖₁]). Without this constraint, the networks learn a mapping that satisfies the GAN objective but is otherwise unconstrained — typically degenerating to mode collapse where G maps all x to the same y. The cycle loss is what gives CycleGAN its remarkable ability to learn meaningful semantic correspondences (horse body → zebra body, not just average zebra texture).

```python
import torch
import torch.nn as nn

def cycle_consistency_loss(G_XY, G_YX, real_X, real_Y, lam=10.0):
    '''L_cyc = lam * (||F(G(x))-x||_1 + ||G(F(y))-y||_1).'''
    l1 = nn.L1Loss()
    fake_Y = G_XY(real_X)            # X -> Y
    rec_X  = G_YX(fake_Y)            # Y -> X  (reconstruct)
    fake_X = G_YX(real_Y)            # Y -> X
    rec_Y  = G_XY(fake_X)            # X -> Y  (reconstruct)
    loss_fwd = l1(rec_X, real_X)     # forward cycle
    loss_bwd = l1(rec_Y, real_Y)     # backward cycle
    loss = lam * (loss_fwd + loss_bwd)
    return loss, loss_fwd.item(), loss_bwd.item()

G_XY = CycleGenerator(); G_YX = CycleGenerator()
rx = torch.randn(1, 3, 64, 64)
ry = torch.randn(1, 3, 64, 64)
loss, fwd, bwd = cycle_consistency_loss(G_XY, G_YX, rx, ry)
print('Cycle loss: {:.4f}  fwd: {:.4f}  bwd: {:.4f}'.format(
      loss.item(), fwd, bwd))
```

## Identity Loss for Color Preservation

The identity loss adds the constraint that G should act as the identity when given an image already in its target domain: G(y) ≈ y and F(x) ≈ x. L_id = λ_id·(E[‖G(y)−y‖₁] + E[‖F(x)−x‖₁]). Typically λ_id = 0.5·λ_cyc. Without the identity loss, G may freely shift the colour palette of images that don't need translation — for example, G trained for photo→Monet might add a warm orange tone to photos that already look painterly. The identity loss prevents this unwanted colour shift.

```python
import torch
import torch.nn as nn

def identity_loss(G_XY, G_YX, real_X, real_Y, lam_id=5.0):
    '''Penalise G_XY(y) != y and G_YX(x) != x.'''
    l1   = nn.L1Loss()
    id_Y = G_XY(real_Y)   # G should be identity on Y-domain input
    id_X = G_YX(real_X)   # F should be identity on X-domain input
    loss = lam_id * (l1(id_Y, real_Y) + l1(id_X, real_X))
    return loss

G_XY = CycleGenerator(); G_YX = CycleGenerator()
rx = torch.randn(1, 3, 64, 64); ry = torch.randn(1, 3, 64, 64)
loss_id = identity_loss(G_XY, G_YX, rx, ry)
print('Identity loss:', round(loss_id.item(), 4))
print('Without identity loss, G may shift overall color hue of input images.')
```

## Full Objective and Training

The full CycleGAN objective is L = L_GAN(G,D_Y,X,Y) + L_GAN(F,D_X,Y,X) + λ·L_cyc(G,F) + λ_id·L_id(G,F). Training alternates: update D_X and D_Y using the LSGAN (least-squares) objective (more stable than BCE), then update G and F jointly using the full loss with cycle and identity terms. A replay buffer of 50 previously generated images is used when updating D to prevent oscillations. Learning rate 0.0002 with Adam; linear decay after 100 epochs.

> **What CycleGAN Cannot Do**: Cycle consistency enforces that the overall image structure is preserved but does not constrain local geometry. CycleGAN cannot reliably change object count, size, or shape — it can change texture and colour (horse stripes) but not remodel the body shape or add/remove objects. Tasks requiring structural change (cat→dog, landscape→portrait) require additional constraints or a different formulation such as GeoGAN or geometry-aware translation methods.

## Contrastive Unpaired Translation (CUT)

CUT (Park et al. 2020) achieves unpaired translation without a reverse generator F or cycle consistency. Instead, it uses patch-wise contrastive loss (PatchNCE): for each patch location, the corresponding patch in the generated image should be closer to the real source patch than to patches at other locations. This preserves content without requiring F(G(x))≈x. CUT uses only one generator and one discriminator — half the parameters of CycleGAN — and is roughly 2× faster to train. It achieves comparable or better FID on horse↔zebra and other benchmarks.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def patch_nce_loss(feat_q, feat_k, tau=0.07):
    '''PatchNCE: query (generated) vs key (source) patch features.
    Positive pair: same spatial location. Negatives: other locations.'''
    feat_q = F.normalize(feat_q, dim=1)  # (N, C)
    feat_k = F.normalize(feat_k, dim=1)  # (N, C)
    logits = torch.mm(feat_q, feat_k.t()) / tau  # (N, N)
    labels = torch.arange(logits.size(0), device=logits.device)
    return F.cross_entropy(logits, labels)

# Comparison: memory and parameter count
def model_stats(name, n_params):
    print('{}: {:,} params  ({:.1f}M)'.format(name, n_params, n_params/1e6))

N, C = 256, 256
feat_q = torch.randn(N, C)
feat_k = torch.randn(N, C)
nce = patch_nce_loss(feat_q, feat_k)
print('PatchNCE loss:', round(nce.item(), 4))
print('CUT: 1 generator + PatchNCE -- no F, no cycle, ~2x faster than CycleGAN')
```

## Applications and Known Limitations

CycleGAN has been applied to horse↔zebra (texture change), apple↔orange (texture + colour), photo↔Monet painting, photo↔Van Gogh, aerial→map, summer→winter, and medical image synthesis (CT→MRI). Limitations: cannot change geometry or count; requires domain gap to be mainly texture/colour; can hallucinate spurious patterns when source and target domains have very different semantics; training can be unstable and sensitive to λ values. CUT and recent diffusion-based methods address several of these limitations.

- Horse→zebra: texture change works well (stripes added naturally)
- Apple→orange: colour + texture change, shape preserved
- Photo→Monet: artistic style transferred, structure preserved
- Photo→Van Gogh: more aggressive style, occasional geometry distortion
- Cat→dog: often fails due to geometric differences — beyond CycleGAN's scope
- Medical CT→MRI: cross-modality synthesis for data augmentation

## Method Comparison

| Method | Paired Data | Generators | Discriminators | Cycle Loss | Training Speed | FID Quality |
| --- | --- | --- | --- | --- | --- | --- |
| Pix2Pix | Required | 1 | 1 PatchGAN | No | Fast | Best (with pairs) |
| CycleGAN | Not required | 2 (G and F) | 2 PatchGAN | Yes (λ=10) | Moderate | Good |
| UNIT | Not required | 2 VAE-GAN | 2 | No (shared latent) | Slow | Comparable |
| CUT | Not required | 1 only | 1 PatchGAN | No (PatchNCE) | ~2x faster | Comparable/better |

---

