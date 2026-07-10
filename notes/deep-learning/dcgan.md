---
title: "DCGAN — Deep Convolutional GAN Architecture Guidelines"
slug: "dcgan"
description: "DCGAN (Radford 2015) architecture guidelines for stable GAN training: strided convolutions, BatchNorm placement, LeakyReLU in D, ReLU+tanh in G, no FC layers, Adam with beta1=0.5, plus spectral normalization and latent space arithmetic."
tags: ["deep-learning", "generative-models", "gans"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRENHQU4gKFJhZGZvcmQgZXQgYWwuLCAyMDE1KSBpbnRyb2R1Y2VkIGEgc2V0IG9mIGFyY2hpdGVjdHVyYWwgZ3VpZGVsaW5lcyB0aGF0IG1hZGUgY29udm9sdXRpb25hbCBHQU5zIHJlbGlhYmx5IHRyYWluYWJsZSBmb3IgdGhlIGZpcnN0IHRpbWUuIFByaW9yIHRvIERDR0FOLCBHQU4gdHJhaW5pbmcgd2FzIGhpZ2hseSBzZW5zaXRpdmUgdG8gYXJjaGl0ZWN0dXJlIGNob2ljZXMsIGFuZCBjb252b2x1dGlvbmFsIGFyY2hpdGVjdHVyZXMgZnJlcXVlbnRseSBmYWlsZWQgdG8gY29udmVyZ2UuIFRoZSBEQ0dBTiBndWlkZWxpbmVzIOKAlCBzdHJpZGVkIGNvbnZvbHV0aW9ucywgY2FyZWZ1bCBCYXRjaE5vcm0gcGxhY2VtZW50LCBzcGVjaWZpYyBhY3RpdmF0aW9uIGZ1bmN0aW9ucywgYW5kIG5vIGZ1bGx5LWNvbm5lY3RlZCBsYXllcnMg4oCUIGJlY2FtZSB0aGUgZGUgZmFjdG8gc3RhcnRpbmcgcG9pbnQgZm9yIG5lYXJseSBhbGwgc3Vic2VxdWVudCBHQU4gcmVzZWFyY2guIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXJjaGl0ZWN0dXJlIE92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEQ0dBTlx1MDAyN3MgZml2ZSBndWlkZWxpbmVzIGFyZTogKDEpIHJlcGxhY2UgcG9vbGluZyB3aXRoIHN0cmlkZWQgY29udm9sdXRpb25zIGluIEQgYW5kIHRyYW5zcG9zZWQgY29udm9sdXRpb25zIGluIEc7ICgyKSB1c2UgQmF0Y2hOb3JtIGluIGJvdGggRyBhbmQgRCwgZXhjZXB0IGF0IHRoZSBHIG91dHB1dCBsYXllciBhbmQgRCBpbnB1dCBsYXllcjsgKDMpIHVzZSBSZUxVIGFjdGl2YXRpb25zIGluIEcgKGFsbCBsYXllcnMpIGFuZCB0YW5oIGF0IHRoZSBHIG91dHB1dDsgKDQpIHVzZSBMZWFreVJlTFUoMC4yKSBpbiBEIChhbGwgbGF5ZXJzKTsgKDUpIHJlbW92ZSBmdWxseS1jb25uZWN0ZWQgbGF5ZXJzIOKAlCBjb25uZWN0IHRoZSBsYXRlbnQgdmVjdG9yIHogZGlyZWN0bHkgdG8gdGhlIGZpcnN0IGNvbnZvbHV0aW9uYWwgbGF5ZXIgb2YgRyB2aWEgcmVzaGFwZSwgYW5kIGZsYXR0ZW4gdG8gYSBzaW5nbGUgbG9naXQgaW4gRC4gVGhlc2UgZml2ZSBydWxlcyB0b2dldGhlciBjcmVhdGUgYSBzdGFibGUgdHJhaW5pbmcgc2V0dXAgYWNyb3NzIGEgd2lkZSByYW5nZSBvZiBkYXRhc2V0cy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJHZW5lcmF0b3IgQXJjaGl0ZWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZ2VuZXJhdG9yIG1hcHMgYSAxMDAtZGltZW5zaW9uYWwgbGF0ZW50IHZlY3RvciB6IHRvIGEgNjR4NjQgUkdCIGltYWdlIHRocm91Z2ggYSBzZXJpZXMgb2YgdHJhbnNwb3NlZCBjb252b2x1dGlvbiAoZnJhY3Rpb25hbGx5LXN0cmlkZWQgY29udm9sdXRpb24pIGxheWVyczogeigxMDApIOKGkiByZXNoYXBlIHRvIDF4MXgxMDI0IOKGkiA0eDR4NTEyIOKGkiA4eDh4MjU2IOKGkiAxNngxNngxMjgg4oaSIDMyeDMyeDY0IOKGkiA2NHg2NHgzLiBFYWNoIGludGVybWVkaWF0ZSBsYXllciB1c2VzIEJhdGNoTm9ybSBhbmQgUmVMVS4gVGhlIGZpbmFsIGxheWVyIHVzZXMgdGFuaCAob3V0cHV0IGluIFstMSwxXSkgd2l0aCBubyBCYXRjaE5vcm0g4oCUIGFkZGluZyBCTiBhdCB0aGUgb3V0cHV0IGxheWVyIGNhdXNlcyBvc2NpbGxhdGlvbiBiZWNhdXNlIGl0IG1vZGlmaWVzIHRoZSBleGFjdCBwaXhlbCB2YWx1ZSBkaXN0cmlidXRpb24gdGhhdCB0aGUgZGlzY3JpbWluYXRvciB0cmFpbnMgb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIERDR0FOR2VuZXJhdG9yKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3eiAoMTAwLWQgbGF0ZW50KSAtXHUwMDNlIHRyYW5zcG9zZWQtY29udiBzdGFjayAtXHUwMDNlIDY0eDY0IFJHQiB2aWEgdGFuaC5cbiAgICBHdWlkZWxpbmVzOiB0cmFuc3Bvc2VkIGNvbnYgKG5vIHBvb2xpbmcpLCBCTiBvbiBhbGwgbGF5ZXJzIGV4Y2VwdCBvdXRwdXQsIFJlTFUuXG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGxhdGVudF9kaW09MTAwLCBuZ2Y9NjQsIG5jPTMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5uZXQgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgIyB6IC1cdTAwM2UgNHg0IGZlYXR1cmUgbWFwIChuZ2YqMTYgPSAxMDI0IGNoYW5uZWxzIHdpdGggbmdmPTY0KVxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKGxhdGVudF9kaW0sIG5nZiAqIDE2LCA0LCAxLCAwLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG5nZiAqIDE2KSwgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgICMgNHg0IC1cdTAwM2UgOHg4XG4gICAgICAgICAgICBubi5Db252VHJhbnNwb3NlMmQobmdmICogMTYsIG5nZiAqIDgsIDQsIDIsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQobmdmICogOCksIG5uLlJlTFUoVHJ1ZSksXG4gICAgICAgICAgICAjIDh4OCAtXHUwMDNlIDE2eDE2XG4gICAgICAgICAgICBubi5Db252VHJhbnNwb3NlMmQobmdmICogOCwgbmdmICogNCwgNCwgMiwgMSwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0yZChuZ2YgKiA0KSwgbm4uUmVMVShUcnVlKSxcbiAgICAgICAgICAgICMgMTZ4MTYgLVx1MDAzZSAzMngzMlxuICAgICAgICAgICAgbm4uQ29udlRyYW5zcG9zZTJkKG5nZiAqIDQsIG5nZiAqIDIsIDQsIDIsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQobmdmICogMiksIG5uLlJlTFUoVHJ1ZSksXG4gICAgICAgICAgICAjIDMyeDMyIC1cdTAwM2UgNjR4NjQsIE5PIEJOIGF0IG91dHB1dCBsYXllciwgdGFuaCBhY3RpdmF0aW9uXG4gICAgICAgICAgICBubi5Db252VHJhbnNwb3NlMmQobmdmICogMiwgbmMsIDQsIDIsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uVGFuaCgpXG4gICAgICAgIClcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB6KTpcbiAgICAgICAgcmV0dXJuIHNlbGYubmV0KHoudmlldyh6LnNpemUoMCksIHouc2l6ZSgxKSwgMSwgMSkpXG5cbmcgPSBEQ0dBTkdlbmVyYXRvcigpXG56ID0gdG9yY2gucmFuZG4oNCwgMTAwKVxucHJpbnQoXHUwMDI3R2VuZXJhdG9yIG91dHB1dDpcdTAwMjcsIGcoeikuc2hhcGUpICAgIyB0b3JjaC5TaXplKFs0LCAzLCA2NCwgNjRdKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRpc2NyaW1pbmF0b3IgQXJjaGl0ZWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZGlzY3JpbWluYXRvciBpcyBhIG1pcnJvciBvZiB0aGUgZ2VuZXJhdG9yIHVzaW5nIHN0cmlkZWQgY29udm9sdXRpb25zIGluc3RlYWQgb2YgdHJhbnNwb3NlZCBjb252b2x1dGlvbnM6IDY0eDY0eDMg4oaSIDMyeDMyeDY0IOKGkiAxNngxNngxMjgg4oaSIDh4OHgyNTYg4oaSIDR4NHg1MTIg4oaSIDF4MXgxIOKGkiBzaWdtb2lkLiBUaGUgZmlyc3QgbGF5ZXIgaGFzIG5vIEJhdGNoTm9ybSAodGhlIGlucHV0IGxheWVyXHUwMDI3cyBzdGF0aXN0aWNzIHNob3VsZCBub3QgYmUgbm9ybWFsaXNlZCDigJQgdGhlIGRpc2NyaW1pbmF0b3IgbmVlZHMgdG8gY29tcGFyZSByYXcgcGl4ZWwgZGlzdHJpYnV0aW9ucykuIEFsbCBpbnRlcm1lZGlhdGUgbGF5ZXJzIHVzZSBCYXRjaE5vcm0gYW5kIExlYWt5UmVMVSgwLjIpLiBUaGUgZmluYWwgY29udiBsYXllciByZWR1Y2VzIHRvIGEgc2luZ2xlIGxvZ2l0IGZvbGxvd2VkIGJ5IHNpZ21vaWQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIERDR0FORGlzY3JpbWluYXRvcihubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyNzY0eDY0IFJHQiAtXHUwMDNlIHJlYWwvZmFrZSBwcm9iYWJpbGl0eSB2aWEgc3RyaWRlZCBjb252b2x1dGlvbnMuXG4gICAgR3VpZGVsaW5lczogc3RyaWRlZCBjb252IChubyBwb29saW5nKSwgQk4gZXhjZXB0IGF0IGlucHV0LCBMZWFreVJlTFUoMC4yKS5cbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbmRmPTY0LCBuYz0zKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgICMgTk8gQk4gYXQgaW5wdXQgbGF5ZXIg4oCUIGRpc2NyaW1pbmF0b3IgbXVzdCBzZWUgcmF3IHBpeGVsIHN0YXRpc3RpY3NcbiAgICAgICAgICAgIG5uLkNvbnYyZChuYywgbmRmLCA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgICAgICAgICAgICMgNjQtXHUwMDNlMzJcbiAgICAgICAgICAgIG5uLkxlYWt5UmVMVSgwLjIsIGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQobmRmLCBuZGYgKiAyLCA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgICAgICAjIDMyLVx1MDAzZTE2XG4gICAgICAgICAgICBubi5CYXRjaE5vcm0yZChuZGYgKiAyKSwgbm4uTGVha3lSZUxVKDAuMiwgaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChuZGYgKiAyLCBuZGYgKiA0LCA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgICMgMTYtXHUwMDNlOFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQobmRmICogNCksIG5uLkxlYWt5UmVMVSgwLjIsIGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQobmRmICogNCwgbmRmICogOCwgNCwgMiwgMSwgYmlhcz1GYWxzZSksICAjIDgtXHUwMDNlNFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQobmRmICogOCksIG5uLkxlYWt5UmVMVSgwLjIsIGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQobmRmICogOCwgMSwgNCwgMSwgMCwgYmlhcz1GYWxzZSksICAgICAgICAjIDQtXHUwMDNlMXgxXG4gICAgICAgICAgICBubi5TaWdtb2lkKClcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGltZyk6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldChpbWcpLnZpZXcoLTEsIDEpXG5cbmQgPSBEQ0dBTkRpc2NyaW1pbmF0b3IoKVxueCA9IHRvcmNoLnJhbmRuKDQsIDMsIDY0LCA2NClcbnByaW50KFx1MDAyN0Rpc2NyaW1pbmF0b3Igb3V0cHV0Olx1MDAyNywgZCh4KS5zaGFwZSkgICAjIHRvcmNoLlNpemUoWzQsIDFdKVxucHJpbnQoXHUwMDI3U2FtcGxlIHByb2JzOlx1MDAyNywgZCh4KS5kZXRhY2goKS5udW1weSgpLmZsYXR0ZW4oKS5yb3VuZCgzKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZXNpZ24gQ2hvaWNlcyBhbmQgUmF0aW9uYWxlIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRlc2lnbiBDaG9pY2UiLCJPbGQgQXBwcm9hY2giLCJEQ0dBTiBBcHByb2FjaCIsIldoeSBJdCBNYXR0ZXJzIl0sInJvd3MiOltbIkRvd25zYW1wbGluZyBpbiBEIiwiTWF4IHBvb2xpbmciLCJTdHJpZGVkIGNvbnYgKHN0cmlkZT0yKSIsIkxlYXJuYWJsZSBkb3duc2FtcGxpbmc7IHBvb2xpbmcgZGlzY2FyZHMgc3BhdGlhbCBpbmZvcm1hdGlvbiB0aGUgZGlzY3JpbWluYXRvciBuZWVkcyJdLFsiVXBzYW1wbGluZyBpbiBHIiwiTmVhcmVzdC1uZWlnaGJvdXIgKyBjb252IiwiVHJhbnNwb3NlZCBjb252IChmcmFjdGlvbmFsbHktc3RyaWRlZCkiLCJMZWFybmFibGUgdXBzYW1wbGluZyBhdm9pZHMgY2hlY2tlcmJvYXJkIGFydGlmYWN0cyBmcm9tIGZpeGVkIGludGVycG9sYXRpb24iXSxbIkJOIGluIEciLCJOb25lIG9yIGV2ZXJ5d2hlcmUiLCJBbGwgbGF5ZXJzIGV4Y2VwdCBvdXRwdXQgKHRhbmgpIiwiQk4gc3RhYmlsaXNlcyB0cmFpbmluZzsgZXhjbHVkaW5nIG91dHB1dCBsYXllciBwcmV2ZW50cyBub3JtYWxpc2luZyB0aGUgcGl4ZWwgZGlzdHJpYnV0aW9uIEcgaXMgb3B0aW1pc2luZyJdLFsiQk4gaW4gRCIsIk5vbmUgb3IgZXZlcnl3aGVyZSIsIkFsbCBsYXllcnMgZXhjZXB0IGlucHV0IiwiQk4gaW4gRCBoZWxwcyBncmFkaWVudCBmbG93OyBleGNsdWRpbmcgaW5wdXQgcHJldmVudHMgbm9ybWFsaXNpbmcgdGhlIHJhdyBwaXhlbCBzdGF0aXN0aWNzIEQgbXVzdCBkaXNjcmltaW5hdGUiXSxbIkFjdGl2YXRpb25zIGluIEciLCJSZUxVIGV2ZXJ5d2hlcmUgd2l0aCBzaWdtb2lkIG91dHB1dCIsIlJlTFUgKGhpZGRlbiksIHRhbmggKG91dHB1dCkiLCJUYW5oIGJvdW5kcyBvdXRwdXQgdG8gWy0xLDFdIG1hdGNoaW5nIG5vcm1hbGlzZWQgZGF0YTsgUmVMVSBoaWRkZW4gbGF5ZXJzIGxlYXJuIHNwYXJzZSBmZWF0dXJlcyJdLFsiQWN0aXZhdGlvbnMgaW4gRCIsIlJlTFUgZXZlcnl3aGVyZSIsIkxlYWt5UmVMVSgwLjIpIGV2ZXJ5d2hlcmUiLCJMZWFreSBzbG9wZSBwcmV2ZW50cyBkeWluZyBSZUxVOyBkaXNjcmltaW5hdG9yIG5lZWRzIHRvIGZsb3cgZ3JhZGllbnRzIGZvciBhbGwgaW5wdXQgdmFsdWVzIl0sWyJGdWxseS1jb25uZWN0ZWQgbGF5ZXJzIiwiRGVuc2UgbGF5ZXJzIGJldHdlZW4gY29udiBhbmQgb3V0cHV0IiwiUmVtb3ZlZCBlbnRpcmVseSIsIkZDIGxheWVycyBhZGQgcGFyYW1ldGVycyB0aGF0IG92ZXJmaXQgYW5kIGRlc3RhYmlsaXNlOyBkaXJlY3Qgc3BhdGlhbCBmbGF0dGVuaW5nIGlzIHN1ZmZpY2llbnQiXV19LHsidHlwZSI6ImNhbGxvdXQiLCJ2YXJpYW50IjoidGlwIiwidGl0bGUiOiJCTiBQbGFjZW1lbnQgUnVsZSIsImNvbnRlbnQiOiJUaGUgQmF0Y2hOb3JtIHJ1bGUgaW4gRENHQU4gaXM6IHVzZSBCTiBldmVyeXdoZXJlIGV4Y2VwdCAoMSkgdGhlIEcgb3V0cHV0IGxheWVyIOKAlCB0YW5oIG91dHB1dCBzaG91bGQgbm90IGJlIGJhdGNoLW5vcm1hbGlzZWQsIGFzIHRoaXMgd291bGQgZGVzdHJveSB0aGUgcGl4ZWwtbGV2ZWwgc2lnbmFsIEcgaXMgb3B0aW1pc2luZyDigJQgYW5kICgyKSB0aGUgRCBpbnB1dCBsYXllciDigJQgdGhlIGRpc2NyaW1pbmF0b3IgbXVzdCBjb21wYXJlIHJhdyBwaXhlbCBkaXN0cmlidXRpb25zIGZyb20gcmVhbCBhbmQgZmFrZSBpbWFnZXMgd2l0aG91dCBub3JtYWxpc2F0aW9uIHRoYXQgd291bGQgZXJhc2UgdGhlIHN0YXRpc3RpY3MgaXQgaXMgdHJ5aW5nIHRvIGRpc3Rpbmd1aXNoLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIENvbmZpZ3VyYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBEQ0dBTiBwYXBlciB0cmFpbnMgd2l0aCBBZGFtIG9wdGltaXNlciwgbGVhcm5pbmcgcmF0ZSAwLjAwMDIsIGFuZCBiZXRhMT0wLjUgKG5vdCB0aGUgZGVmYXVsdCAwLjkpLiBUaGUgcmVkdWNlZCBiZXRhMSBpcyBjcml0aWNhbCDigJQgc3RhbmRhcmQgQWRhbSBhY2N1bXVsYXRlcyBncmFkaWVudCBtb21lbnR1bSB0aGF0IGNhdXNlcyBvc2NpbGxhdGlvbiBpbiBhZHZlcnNhcmlhbCB0cmFpbmluZy4gQmF0Y2ggc2l6ZSAxMjggaXMgc3RhbmRhcmQuIEltYWdlcyBhcmUgbm9ybWFsaXNlZCB0byBbLTEsMV0gdG8gbWF0Y2ggdGhlIGdlbmVyYXRvclx1MDAyN3MgdGFuaCBvdXRwdXQuIFdlaWdodHMgYXJlIGluaXRpYWxpc2VkIGZyb20gYSB6ZXJvLW1lYW4gR2F1c3NpYW4gd2l0aCBzdGQ9MC4wMiwgd2hpY2ggcHJldmVudHMgdGhlIGRpc2NyaW1pbmF0b3IgZnJvbSBkb21pbmF0aW5nIGVhcmx5IGluIHRyYWluaW5nLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiT3B0aW1pc2VyOiBBZGFtIHdpdGggbHI9MC4wMDAyLCBiZXRhMT0wLjUsIGJldGEyPTAuOTk5IGZvciBib3RoIEcgYW5kIEQiLCJCYXRjaCBzaXplOiAxMjggKGxhcmdlciBiYXRjaGVzIHN0YWJpbGlzZSBCTiBzdGF0aXN0aWNzKSIsIkltYWdlIG5vcm1hbGlzYXRpb246IG1lYW49MC41LCBzdGQ9MC41IHBlciBjaGFubmVsIHRvIG1hcCBbMCwxXSBpbWFnZXMgdG8gWy0xLDFdIiwiV2VpZ2h0IGluaXQ6IE5vcm1hbCgwLCAwLjAyKSDigJQgdGhlIHNtYWxsIHN0ZCBwcmV2ZW50cyBlYXJseSB0cmFpbmluZyBpbnN0YWJpbGl0eSIsIkxhdGVudCBkaW06IDEwMCAodW5pZm9ybSBvciBHYXVzc2lhbiBwcmlvciwgYm90aCB3b3JrKSIsIlRyYWluaW5nIHJhdGlvOiBrPTEgKG9uZSBEIHN0ZXAgcGVyIEcgc3RlcCkg4oCUIHN1ZmZpY2llbnQgZm9yIERDR0FOXHUwMDI3cyBzdGFibGUgYXJjaGl0ZWN0dXJlIiwiTm8gbGVhcm5pbmcgcmF0ZSBzY2hlZHVsaW5nIOKAlCBEQ0dBTiB0cmFpbnMgc3RhYmx5IGF0IGNvbnN0YW50IGxyPTAuMDAwMiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMYXRlbnQgU3BhY2UgQXJpdGhtZXRpYyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSBrZXkgZmluZGluZyBvZiBEQ0dBTiBpcyB0aGF0IHRoZSBsYXRlbnQgc3BhY2UgaGFzIG1lYW5pbmdmdWwgc3RydWN0dXJlLiBBcml0aG1ldGljIGluIHogc3BhY2UgdHJhbnNmZXJzIHRvIHNlbWFudGljIGltYWdlIGF0dHJpYnV0ZXM6IHpfc21pbGluZ19tYW4gLSB6X25ldXRyYWxfbWFuICsgel9uZXV0cmFsX3dvbWFuIOKJiCB6X3NtaWxpbmdfd29tYW4uIEludGVycG9sYXRpb24gYmV0d2VlbiB0d28geiB2ZWN0b3JzIHByb2R1Y2VzIHNtb290aCB2aXN1YWwgdHJhbnNpdGlvbnMgcmF0aGVyIHRoYW4gZGlzY29udGludW91cyBqdW1wcywgZGVtb25zdHJhdGluZyB0aGF0IEcgbGVhcm5zIGEgc21vb3RoLCBjb250aW51b3VzIG1hcHBpbmcuIFRoaXMgc3RydWN0dXJlIGVtZXJnZXMgZnJvbSB0cmFpbmluZyBhbG9uZSDigJQgbm8gZXhwbGljaXQgZGlzZW50YW5nbGVtZW50IG9iamVjdGl2ZSBpcyBuZWVkZWQgaW4gRENHQU4uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBlbmNvZGVfaW1hZ2VzKGVuY29kZXIsIGltYWdlcywgbl9zYW1wbGVzPTUwKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdFbmNvZGUgaW1hZ2VzIHRvIGEgbWVhbiBsYXRlbnQgdmVjdG9yIChyZXF1aXJlcyBhIHByZS10cmFpbmVkIGVuY29kZXIpLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGVuY29kZXIuZXZhbCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGlmIGltYWdlcy5kaW0oKSA9PSAzOlxuICAgICAgICAgICAgaW1hZ2VzID0gaW1hZ2VzLnVuc3F1ZWV6ZSgwKS5leHBhbmQobl9zYW1wbGVzLCAtMSwgLTEsIC0xKVxuICAgICAgICBsYXRlbnRzID0gZW5jb2RlcihpbWFnZXMpXG4gICAgICAgIGlmIGlzaW5zdGFuY2UobGF0ZW50cywgdHVwbGUpOlxuICAgICAgICAgICAgbGF0ZW50cyA9IGxhdGVudHNbMF0gICAjIFZBRSBlbmNvZGVyIHJldHVybnMgKG11LCBsb2d2YXIpXG4gICAgcmV0dXJuIGxhdGVudHMubWVhbihkaW09MClcblxuZGVmIGxhdGVudF9hcml0aG1ldGljKGdlbmVyYXRvciwgZW5jb2RlciwgaW1nX2EsIGltZ19iLCBpbWdfYywgbl9pbnRlcnA9OCk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3VmVjdG9yIGFyaXRobWV0aWMgaW4gbGF0ZW50IHNwYWNlOiByZXN1bHQgPSB6X2EgLSB6X2IgKyB6X2MuXG4gICAgQ2xhc3NpYzogc21pbGluZ19tYW4gLSBuZXV0cmFsX21hbiArIG5ldXRyYWxfd29tYW4g4omIIHNtaWxpbmdfd29tYW4uXG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgel9hID0gZW5jb2RlX2ltYWdlcyhlbmNvZGVyLCBpbWdfYSlcbiAgICB6X2IgPSBlbmNvZGVfaW1hZ2VzKGVuY29kZXIsIGltZ19iKVxuICAgIHpfYyA9IGVuY29kZV9pbWFnZXMoZW5jb2RlciwgaW1nX2MpXG4gICAgel9yZXN1bHQgPSB6X2EgLSB6X2IgKyB6X2NcbiAgICBnZW5lcmF0b3IuZXZhbCgpXG4gICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6XG4gICAgICAgIGltZ19yZXN1bHQgPSBnZW5lcmF0b3Ioel9yZXN1bHQudW5zcXVlZXplKDApKVxuICAgICAgICAjIEludGVycG9sYXRlIGZyb20gel9jIHRvIHpfcmVzdWx0XG4gICAgICAgIGFscGhhcyA9IHRvcmNoLmxpbnNwYWNlKDAuMCwgMS4wLCBuX2ludGVycClcbiAgICAgICAgaW50ZXJwX2ltZ3MgPSBbXG4gICAgICAgICAgICBnZW5lcmF0b3IoKCgxIC0gYSkgKiB6X2MgKyBhICogel9yZXN1bHQpLnVuc3F1ZWV6ZSgwKSlcbiAgICAgICAgICAgIGZvciBhIGluIGFscGhhc1xuICAgICAgICBdXG4gICAgcHJpbnQoZlx1MDAyN0xhdGVudCBkaW06IHt6X2Euc2hhcGVbMF19ICB8ICBSZXN1bHQgc2hhcGU6IHtpbWdfcmVzdWx0LnNoYXBlfVx1MDAyNylcbiAgICBwcmludChmXHUwMDI3SW50ZXJwb2xhdGlvbjoge25faW50ZXJwfSBzdGVwcyBmcm9tIHpfYyB0byB6X2FyaXRobWV0aWNfcmVzdWx0XHUwMDI3KVxuICAgIHJldHVybiBpbWdfcmVzdWx0LCBpbnRlcnBfaW1ncyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlNwZWN0cmFsIE5vcm1hbGl6YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlNwZWN0cmFsIG5vcm1hbGl6YXRpb24gKE1peWF0byBldCBhbC4sIDIwMTgpIGltcHJvdmVzIHVwb24gRENHQU5cdTAwMjdzIEJhdGNoTm9ybSBieSBub3JtYWxpc2luZyBlYWNoIHdlaWdodCBtYXRyaXggYnkgaXRzIGxhcmdlc3Qgc2luZ3VsYXIgdmFsdWUgc2lnbWFfbWF4KFcpLCBlbmZvcmNpbmcgYSBwZXItbGF5ZXIgMS1MaXBzY2hpdHogY29uc3RyYWludC4gVW5saWtlIFdHQU4gd2VpZ2h0IGNsaXBwaW5nICh3aGljaCBjbGlwcyBhbGwgd2VpZ2h0cyB1bmlmb3JtbHkpIG9yIEJhdGNoTm9ybSAod2hpY2ggbm9ybWFsaXNlcyBhY3RpdmF0aW9ucyBhbmQgdGh1cyBkZXBlbmRzIG9uIGJhdGNoIHNpemUpLCBzcGVjdHJhbCBub3JtIGNvbnN0cmFpbnMgdGhlIHdlaWdodCBtYXRyaXggZGlyZWN0bHkgYW5kIGlzIGluZGVwZW5kZW50IG9mIGJhdGNoIHN0YXRpc3RpY3MuIEl0IHdvcmtzIHdlbGwgd2l0aCBhbnkgYmF0Y2ggc2l6ZSBpbmNsdWRpbmcgYmF0Y2ggc2l6ZSAxLCBtYWtpbmcgaXQgc3VpdGFibGUgZm9yIGluc3RhbmNlLWNvbmRpdGlvbmVkIGdlbmVyYXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5mcm9tIHRvcmNoLm5uLnV0aWxzIGltcG9ydCBzcGVjdHJhbF9ub3JtXG5cbmNsYXNzIFNwZWN0cmFsTm9ybURpc2NyaW1pbmF0b3Iobm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdEaXNjcmltaW5hdG9yIHdpdGggU3BlY3RyYWwgTm9ybWFsaXphdGlvbiAoTWl5YXRvIGV0IGFsLiAyMDE4KS5cbiAgICBTTiBkaXZpZGVzIHdlaWdodHMgYnkgc2lnbWFfbWF4KFcpIGFmdGVyIGVhY2ggc3RlcCB2aWEgcG93ZXIgaXRlcmF0aW9uLFxuICAgIGVuZm9yY2luZyAxLUxpcHNjaGl0eiBjb25zdHJhaW50IGluZGVwZW5kZW50bHkgb2YgYmF0Y2ggc2l6ZS5cbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbmRmPTY0LCBuYz0zKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubmV0ID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIHNwZWN0cmFsX25vcm0obm4uQ29udjJkKG5jLCBuZGYsIDQsIDIsIDEpKSxcbiAgICAgICAgICAgIG5uLkxlYWt5UmVMVSgwLjIsIGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBzcGVjdHJhbF9ub3JtKG5uLkNvbnYyZChuZGYsIG5kZiAqIDIsIDQsIDIsIDEpKSxcbiAgICAgICAgICAgIG5uLkxlYWt5UmVMVSgwLjIsIGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBzcGVjdHJhbF9ub3JtKG5uLkNvbnYyZChuZGYgKiAyLCBuZGYgKiA0LCA0LCAyLCAxKSksXG4gICAgICAgICAgICBubi5MZWFreVJlTFUoMC4yLCBpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgc3BlY3RyYWxfbm9ybShubi5Db252MmQobmRmICogNCwgbmRmICogOCwgNCwgMiwgMSkpLFxuICAgICAgICAgICAgbm4uTGVha3lSZUxVKDAuMiwgaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIHNwZWN0cmFsX25vcm0obm4uQ29udjJkKG5kZiAqIDgsIDEsIDQsIDEsIDApKSxcbiAgICAgICAgKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIGltZyk6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldChpbWcpLnZpZXcoLTEsIDEpXG5cbmRlZiBpbnNwZWN0X3NwZWN0cmFsX25vcm1zKG1vZGVsKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdWZXJpZnkgdGhhdCBzcGVjdHJhbCBub3JtIGNvbnN0cmFpbnMgc2lnbWFfbWF4IHRvIGFwcHJveGltYXRlbHkgMS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBmb3IgbmFtZSwgbSBpbiBtb2RlbC5uYW1lZF9tb2R1bGVzKCk6XG4gICAgICAgIGlmIGhhc2F0dHIobSwgXHUwMDI3d2VpZ2h0X29yaWdcdTAwMjcpOlxuICAgICAgICAgICAgVyA9IG0ud2VpZ2h0X29yaWcuZGF0YS52aWV3KG0ud2VpZ2h0X29yaWcuc2l6ZSgwKSwgLTEpXG4gICAgICAgICAgICBzaWdtYSA9IHRvcmNoLmxpbmFsZy5zdmR2YWxzKFcpLm1heCgpLml0ZW0oKVxuICAgICAgICAgICAgcHJpbnQoZlx1MDAyN3tuYW1lfTogc2lnbWFfbWF4ID0ge3NpZ21hOi40Zn0gIChzaG91bGQgYmUgY2xvc2UgdG8gMS4wKVx1MDAyNylcblxuZF9zbiA9IFNwZWN0cmFsTm9ybURpc2NyaW1pbmF0b3IoKVxuaW5zcGVjdF9zcGVjdHJhbF9ub3JtcyhkX3NuKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRDR0FOXHUwMDI3cyBndWlkZWxpbmVzIHJlbWFpbiByZWxldmFudCBiZWNhdXNlIHRoZXkgZW5jb2RlIGhhcmQtd29uIGVtcGlyaWNhbCBrbm93bGVkZ2UgYWJvdXQgc3RhYmxlIGFkdmVyc2FyaWFsIHRyYWluaW5nLiBUaGUgc3RyaWRlZC90cmFuc3Bvc2VkIGNvbnYgcGF0dGVybiwgY2FyZWZ1bCBCTiBwbGFjZW1lbnQsIExlYWt5UmVMVSBpbiBELCBhbmQgQWRhbSB3aXRoIGJldGExPTAuNSBjb2xsZWN0aXZlbHkgYWRkcmVzcyB0aGUgbW9zdCBjb21tb24gZmFpbHVyZSBtb2RlcyBvZiBlYXJseSBjb252b2x1dGlvbmFsIEdBTnMuIE1vZGVybiBhcmNoaXRlY3R1cmVzIChXR0FOLUdQLCBTdHlsZUdBTikgZXh0ZW5kIHRoZXNlIGZvdW5kYXRpb25zIGJ1dCByYXJlbHkgZGlzY2FyZCB0aGVtIG91dHJpZ2h0LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiU3RyaWRlZCBjb252b2x1dGlvbnMgKG5vdCBwb29saW5nKSBhbGxvdyB0aGUgZGlzY3JpbWluYXRvciB0byBsZWFybiBpdHMgb3duIGRvd25zYW1wbGluZyDigJQgY3JpdGljYWwgZm9yIGNhcHR1cmluZyBkaXN0cmlidXRpb24gc3RhdGlzdGljcyBhdCBtdWx0aXBsZSBzY2FsZXMiLCJCYXRjaE5vcm0gcGxhY2VtZW50IHJ1bGVzIChubyBCTiBhdCBHIG91dHB1dCwgbm8gQk4gYXQgRCBpbnB1dCkgcHJldmVudCB0aGUgbmV0d29yayBmcm9tIG5vcm1hbGlzaW5nIGV4YWN0bHkgdGhlIHNpZ25hbHMgaXQgbmVlZHMgdG8gcHJlc2VydmUiLCJMZWFreVJlTFUoMC4yKSBpbiBEIGVuc3VyZXMgZ3JhZGllbnQgZmxvdyBmb3IgYWxsIGlucHV0IHZhbHVlcywgd2hpbGUgUmVMVSBpbiBHIGVuY291cmFnZXMgc3BhcnNlLCBzdHJ1Y3R1cmVkIHJlcHJlc2VudGF0aW9ucyIsIkFkYW0gd2l0aCBiZXRhMT0wLjUgaXMgZXNzZW50aWFsIOKAlCBkZWZhdWx0IGJldGExPTAuOSBhY2N1bXVsYXRlcyBzdGFsZSBncmFkaWVudCBtb21lbnR1bSB0aGF0IGNhdXNlcyBvc2NpbGxhdGlvbiIsIkxhdGVudCBzcGFjZSBhcml0aG1ldGljIHdvcmtzIGJlY2F1c2UgRENHQU4gbGVhcm5zIGEgc21vb3RoIGdlbmVyYXRpdmUgbWFuaWZvbGQg4oCUIGEgcHJvcGVydHkgdGhhdCBjYXJyaWVzIGZvcndhcmQgdG8gYWxsIHN1YnNlcXVlbnQgR0FOIGFyY2hpdGVjdHVyZXMiXX1d"
---
# DCGAN — Deep Convolutional GAN Architecture Guidelines

DCGAN (Radford et al., 2015) introduced a set of architectural guidelines that made convolutional GANs reliably trainable for the first time. Prior to DCGAN, GAN training was highly sensitive to architecture choices, and convolutional architectures frequently failed to converge. The DCGAN guidelines — strided convolutions, careful BatchNorm placement, specific activation functions, and no fully-connected layers — became the de facto starting point for nearly all subsequent GAN research.

## Architecture Overview

DCGAN's five guidelines are: (1) replace pooling with strided convolutions in D and transposed convolutions in G; (2) use BatchNorm in both G and D, except at the G output layer and D input layer; (3) use ReLU activations in G (all layers) and tanh at the G output; (4) use LeakyReLU(0.2) in D (all layers); (5) remove fully-connected layers — connect the latent vector z directly to the first convolutional layer of G via reshape, and flatten to a single logit in D. These five rules together create a stable training setup across a wide range of datasets.

## Generator Architecture

The generator maps a 100-dimensional latent vector z to a 64x64 RGB image through a series of transposed convolution (fractionally-strided convolution) layers: z(100) → reshape to 1x1x1024 → 4x4x512 → 8x8x256 → 16x16x128 → 32x32x64 → 64x64x3. Each intermediate layer uses BatchNorm and ReLU. The final layer uses tanh (output in [-1,1]) with no BatchNorm — adding BN at the output layer causes oscillation because it modifies the exact pixel value distribution that the discriminator trains on.

```python
import torch
import torch.nn as nn

class DCGANGenerator(nn.Module):
    '''z (100-d latent) -> transposed-conv stack -> 64x64 RGB via tanh.
    Guidelines: transposed conv (no pooling), BN on all layers except output, ReLU.
    '''
    def __init__(self, latent_dim=100, ngf=64, nc=3):
        super().__init__()
        self.net = nn.Sequential(
            # z -> 4x4 feature map (ngf*16 = 1024 channels with ngf=64)
            nn.ConvTranspose2d(latent_dim, ngf * 16, 4, 1, 0, bias=False),
            nn.BatchNorm2d(ngf * 16), nn.ReLU(True),
            # 4x4 -> 8x8
            nn.ConvTranspose2d(ngf * 16, ngf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 8), nn.ReLU(True),
            # 8x8 -> 16x16
            nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 4), nn.ReLU(True),
            # 16x16 -> 32x32
            nn.ConvTranspose2d(ngf * 4, ngf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2), nn.ReLU(True),
            # 32x32 -> 64x64, NO BN at output layer, tanh activation
            nn.ConvTranspose2d(ngf * 2, nc, 4, 2, 1, bias=False),
            nn.Tanh()
        )
    def forward(self, z):
        return self.net(z.view(z.size(0), z.size(1), 1, 1))

g = DCGANGenerator()
z = torch.randn(4, 100)
print('Generator output:', g(z).shape)   # torch.Size([4, 3, 64, 64])
```

## Discriminator Architecture

The discriminator is a mirror of the generator using strided convolutions instead of transposed convolutions: 64x64x3 → 32x32x64 → 16x16x128 → 8x8x256 → 4x4x512 → 1x1x1 → sigmoid. The first layer has no BatchNorm (the input layer's statistics should not be normalised — the discriminator needs to compare raw pixel distributions). All intermediate layers use BatchNorm and LeakyReLU(0.2). The final conv layer reduces to a single logit followed by sigmoid.

```python
import torch
import torch.nn as nn

class DCGANDiscriminator(nn.Module):
    '''64x64 RGB -> real/fake probability via strided convolutions.
    Guidelines: strided conv (no pooling), BN except at input, LeakyReLU(0.2).
    '''
    def __init__(self, ndf=64, nc=3):
        super().__init__()
        self.net = nn.Sequential(
            # NO BN at input layer — discriminator must see raw pixel statistics
            nn.Conv2d(nc, ndf, 4, 2, 1, bias=False),           # 64->32
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),      # 32->16
            nn.BatchNorm2d(ndf * 2), nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),  # 16->8
            nn.BatchNorm2d(ndf * 4), nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),  # 8->4
            nn.BatchNorm2d(ndf * 8), nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),        # 4->1x1
            nn.Sigmoid()
        )
    def forward(self, img):
        return self.net(img).view(-1, 1)

d = DCGANDiscriminator()
x = torch.randn(4, 3, 64, 64)
print('Discriminator output:', d(x).shape)   # torch.Size([4, 1])
print('Sample probs:', d(x).detach().numpy().flatten().round(3))
```

## Design Choices and Rationale

| Design Choice | Old Approach | DCGAN Approach | Why It Matters |
| --- | --- | --- | --- |
| Downsampling in D | Max pooling | Strided conv (stride=2) | Learnable downsampling; pooling discards spatial information the discriminator needs |
| Upsampling in G | Nearest-neighbour + conv | Transposed conv (fractionally-strided) | Learnable upsampling avoids checkerboard artifacts from fixed interpolation |
| BN in G | None or everywhere | All layers except output (tanh) | BN stabilises training; excluding output layer prevents normalising the pixel distribution G is optimising |
| BN in D | None or everywhere | All layers except input | BN in D helps gradient flow; excluding input prevents normalising the raw pixel statistics D must discriminate |
| Activations in G | ReLU everywhere with sigmoid output | ReLU (hidden), tanh (output) | Tanh bounds output to [-1,1] matching normalised data; ReLU hidden layers learn sparse features |
| Activations in D | ReLU everywhere | LeakyReLU(0.2) everywhere | Leaky slope prevents dying ReLU; discriminator needs to flow gradients for all input values |
| Fully-connected layers | Dense layers between conv and output | Removed entirely | FC layers add parameters that overfit and destabilise; direct spatial flattening is sufficient |

> **BN Placement Rule**: The BatchNorm rule in DCGAN is: use BN everywhere except (1) the G output layer — tanh output should not be batch-normalised, as this would destroy the pixel-level signal G is optimising — and (2) the D input layer — the discriminator must compare raw pixel distributions from real and fake images without normalisation that would erase the statistics it is trying to distinguish.

## Training Configuration

The DCGAN paper trains with Adam optimiser, learning rate 0.0002, and beta1=0.5 (not the default 0.9). The reduced beta1 is critical — standard Adam accumulates gradient momentum that causes oscillation in adversarial training. Batch size 128 is standard. Images are normalised to [-1,1] to match the generator's tanh output. Weights are initialised from a zero-mean Gaussian with std=0.02, which prevents the discriminator from dominating early in training.

- Optimiser: Adam with lr=0.0002, beta1=0.5, beta2=0.999 for both G and D
- Batch size: 128 (larger batches stabilise BN statistics)
- Image normalisation: mean=0.5, std=0.5 per channel to map [0,1] images to [-1,1]
- Weight init: Normal(0, 0.02) — the small std prevents early training instability
- Latent dim: 100 (uniform or Gaussian prior, both work)
- Training ratio: k=1 (one D step per G step) — sufficient for DCGAN's stable architecture
- No learning rate scheduling — DCGAN trains stably at constant lr=0.0002

## Latent Space Arithmetic

A key finding of DCGAN is that the latent space has meaningful structure. Arithmetic in z space transfers to semantic image attributes: z_smiling_man - z_neutral_man + z_neutral_woman ≈ z_smiling_woman. Interpolation between two z vectors produces smooth visual transitions rather than discontinuous jumps, demonstrating that G learns a smooth, continuous mapping. This structure emerges from training alone — no explicit disentanglement objective is needed in DCGAN.

```python
import torch
import numpy as np

def encode_images(encoder, images, n_samples=50):
    '''Encode images to a mean latent vector (requires a pre-trained encoder).'''
    encoder.eval()
    with torch.no_grad():
        if images.dim() == 3:
            images = images.unsqueeze(0).expand(n_samples, -1, -1, -1)
        latents = encoder(images)
        if isinstance(latents, tuple):
            latents = latents[0]   # VAE encoder returns (mu, logvar)
    return latents.mean(dim=0)

def latent_arithmetic(generator, encoder, img_a, img_b, img_c, n_interp=8):
    '''Vector arithmetic in latent space: result = z_a - z_b + z_c.
    Classic: smiling_man - neutral_man + neutral_woman ≈ smiling_woman.
    '''
    z_a = encode_images(encoder, img_a)
    z_b = encode_images(encoder, img_b)
    z_c = encode_images(encoder, img_c)
    z_result = z_a - z_b + z_c
    generator.eval()
    with torch.no_grad():
        img_result = generator(z_result.unsqueeze(0))
        # Interpolate from z_c to z_result
        alphas = torch.linspace(0.0, 1.0, n_interp)
        interp_imgs = [
            generator(((1 - a) * z_c + a * z_result).unsqueeze(0))
            for a in alphas
        ]
    print(f'Latent dim: {z_a.shape[0]}  |  Result shape: {img_result.shape}')
    print(f'Interpolation: {n_interp} steps from z_c to z_arithmetic_result')
    return img_result, interp_imgs
```

## Spectral Normalization

Spectral normalization (Miyato et al., 2018) improves upon DCGAN's BatchNorm by normalising each weight matrix by its largest singular value sigma_max(W), enforcing a per-layer 1-Lipschitz constraint. Unlike WGAN weight clipping (which clips all weights uniformly) or BatchNorm (which normalises activations and thus depends on batch size), spectral norm constrains the weight matrix directly and is independent of batch statistics. It works well with any batch size including batch size 1, making it suitable for instance-conditioned generation.

```python
import torch
import torch.nn as nn
from torch.nn.utils import spectral_norm

class SpectralNormDiscriminator(nn.Module):
    '''Discriminator with Spectral Normalization (Miyato et al. 2018).
    SN divides weights by sigma_max(W) after each step via power iteration,
    enforcing 1-Lipschitz constraint independently of batch size.
    '''
    def __init__(self, ndf=64, nc=3):
        super().__init__()
        self.net = nn.Sequential(
            spectral_norm(nn.Conv2d(nc, ndf, 4, 2, 1)),
            nn.LeakyReLU(0.2, inplace=True),
            spectral_norm(nn.Conv2d(ndf, ndf * 2, 4, 2, 1)),
            nn.LeakyReLU(0.2, inplace=True),
            spectral_norm(nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1)),
            nn.LeakyReLU(0.2, inplace=True),
            spectral_norm(nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1)),
            nn.LeakyReLU(0.2, inplace=True),
            spectral_norm(nn.Conv2d(ndf * 8, 1, 4, 1, 0)),
        )
    def forward(self, img):
        return self.net(img).view(-1, 1)

def inspect_spectral_norms(model):
    '''Verify that spectral norm constrains sigma_max to approximately 1.'''
    for name, m in model.named_modules():
        if hasattr(m, 'weight_orig'):
            W = m.weight_orig.data.view(m.weight_orig.size(0), -1)
            sigma = torch.linalg.svdvals(W).max().item()
            print(f'{name}: sigma_max = {sigma:.4f}  (should be close to 1.0)')

d_sn = SpectralNormDiscriminator()
inspect_spectral_norms(d_sn)
```

## Key Takeaways

DCGAN's guidelines remain relevant because they encode hard-won empirical knowledge about stable adversarial training. The strided/transposed conv pattern, careful BN placement, LeakyReLU in D, and Adam with beta1=0.5 collectively address the most common failure modes of early convolutional GANs. Modern architectures (WGAN-GP, StyleGAN) extend these foundations but rarely discard them outright.

- Strided convolutions (not pooling) allow the discriminator to learn its own downsampling — critical for capturing distribution statistics at multiple scales
- BatchNorm placement rules (no BN at G output, no BN at D input) prevent the network from normalising exactly the signals it needs to preserve
- LeakyReLU(0.2) in D ensures gradient flow for all input values, while ReLU in G encourages sparse, structured representations
- Adam with beta1=0.5 is essential — default beta1=0.9 accumulates stale gradient momentum that causes oscillation
- Latent space arithmetic works because DCGAN learns a smooth generative manifold — a property that carries forward to all subsequent GAN architectures

