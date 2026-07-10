---
title: "ResNet — Residual Connections and Bottleneck Blocks"
slug: "resnet-residual-networks"
description: "ResNet (He et al., 2015) introduces skip connections y=F(x)+x that let very deep networks learn residual functions instead of unreferenced mappings, solving the degradation problem and enabling networks of 50–1000+ layers. Bottleneck blocks and pre-activation variants extend the core idea."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGRlZ3JhZGF0aW9uIHByb2JsZW0g4oCUIHdoZXJlIGFkZGluZyBtb3JlIGxheWVycyB0byBhbiBhbHJlYWR5IGRlZXAgbmV0d29yayBpbmNyZWFzZXMgdHJhaW5pbmcgZXJyb3IsIG5vdCBqdXN0IHRlc3QgZXJyb3Ig4oCUIHN1Z2dlc3RzIHRoYXQgZGVlcGVyIHBsYWluIG5ldHdvcmtzIGFyZSBoYXJkZXIgdG8gb3B0aW1pc2UsIG5vdCB0aGF0IHRoZXkgb3ZlcmZpdC4gSGUgZXQgYWwuICgyMDE1KSBoeXBvdGhlc2lzZWQgdGhhdCBsZWFybmluZyB0aGUgaWRlbnRpdHkgbWFwcGluZyB0aHJvdWdoIG11bHRpcGxlIG5vbmxpbmVhciBsYXllcnMgaXMgZGlmZmljdWx0LiBUaGVpciBzb2x1dGlvbjogYWRkIGFuIGV4cGxpY2l0IHNob3J0Y3V0IHkgPSBGKHgsIFcpICsgeCBzbyB0aGUgbmV0d29yayBvbmx5IG5lZWRzIHRvIGxlYXJuIHRoZSByZXNpZHVhbCBGKHgpIOKJiCAwIHdoZW4gdGhlIGlkZW50aXR5IGlzIG9wdGltYWwuIFRoaXMgc2ltcGxlIGNoYW5nZSBlbmFibGVkIG5ldHdvcmtzIG9mIDE1MiBsYXllcnMgdG8gb3V0cGVyZm9ybSBhbGwgcHJpb3IgYXJjaGl0ZWN0dXJlcyB3aGlsZSBiZWluZyBlYXNpZXIgdG8gb3B0aW1pc2UuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVGhlIERlZ3JhZGF0aW9uIFByb2JsZW0gaW4gRGVlcCBOZXR3b3JrcyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSA1Ni1sYXllciBwbGFpbiBuZXR3b3JrIGhhcyBoaWdoZXIgdHJhaW5pbmcgZXJyb3IgdGhhbiBhIDIwLWxheWVyIG5ldHdvcmsgb24gQ0lGQVItMTAg4oCUIGNvdW50ZXJpbnR1aXRpdmVseSB3b3JzZSBkZXNwaXRlIGhhdmluZyBzdHJpY3RseSBtb3JlIGNhcGFjaXR5LiBUaGUgNTYtbGF5ZXIgbmV0d29yayBjb3VsZCwgaW4gcHJpbmNpcGxlLCBsZWFybiB0aGUgc2FtZSBmdW5jdGlvbiBhcyB0aGUgMjAtbGF5ZXIgbmV0d29yayBieSBzZXR0aW5nIGV4dHJhIGxheWVycyB0byBpZGVudGl0eSAoRih4KSA9IHgpLiBCdXQgaW4gcHJhY3RpY2UsIHJhbmRvbSBpbml0aWFsaXNhdGlvbiBhbmQgU0dEIGNhbm5vdCBmaW5kIHRoaXMgc29sdXRpb24gZWZmaWNpZW50bHkuIFRoZSBvcHRpbWlzYXRpb24gbGFuZHNjYXBlIG9mIGRlZXAgbmV0d29ya3Mgd2l0aG91dCBza2lwIGNvbm5lY3Rpb25zIGhhcyBtYW55IGxvY2FsIG1pbmltYSBhbmQgdmFuaXNoaW5nIGdyYWRpZW50cyBtYWtlIGl0IGhhcmQgdG8gdXBkYXRlIGVhcmx5IGxheWVycy4gQmF0Y2ggbm9ybWFsaXNhdGlvbiBoZWxwcyBidXQgZG9lcyBub3QgZnVsbHkgc29sdmUgdGhlIHByb2JsZW0gYXQgNTYrIGxheWVycy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJSZXNpZHVhbCBMZWFybmluZzogeSA9IEYoeCkgKyB4In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgcmVzaWR1YWwgZm9ybXVsYXRpb24geSA9IEYoeCwgVykgKyB4IGhhcyB0d28gY29tcG9uZW50czogRih4LCBXKSBpcyB0aGUgcmVzaWR1YWwgdG8gYmUgbGVhcm5lZCAoYSBzdGFjayBvZiBjb252LUJOLVJlTFUgbGF5ZXJzKSwgYW5kIHggaXMgdGhlIGlkZW50aXR5IHNob3J0Y3V0LiBXaGVuIHRoZSBvcHRpbWFsIG1hcHBpbmcgaXMgdGhlIGlkZW50aXR5LCB0aGUgbmV0d29yayBvbmx5IG5lZWRzIHRvIHB1c2ggRih4KSDihpIgMCwgd2hpY2ggaXMgZWFzeSDigJQgd2VpZ2h0cyBuZWFyIHplcm8gaXMgdGhlIG5hdHVyYWwgaW5pdGlhbGlzYXRpb24uIEdyYWRpZW50IGZsb3cgYW5hbHlzaXMgcmV2ZWFscyB3aHkgdGhpcyB3b3Jrczog4oiCTC/iiIJ4ID0g4oiCTC/iiIJ5IMK3ICjiiIJGL+KIgnggKyBJKS4gVGhlIGlkZW50aXR5IHRlcm0gSSBlbnN1cmVzIGdyYWRpZW50cyBhbHdheXMgZmxvdyBiYWNrd2FyZCB3aXRob3V0IHZhbmlzaGluZywgcmVnYXJkbGVzcyBvZiB0aGUgbGVhcm5lZCBGLiBXaGVuIGlucHV0IGFuZCBvdXRwdXQgZGltZW5zaW9ucyBkaWZmZXIgKGR1ZSB0byBzdHJpZGUgb3IgY2hhbm5lbCBjaGFuZ2UpLCBhIHByb2plY3Rpb24gc2hvcnRjdXQgdXNlcyBhIDHDlzEgY29udiB0byBtYXRjaCBkaW1lbnNpb25zLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBCYXNpY0Jsb2NrKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3UmVzTmV0IGJhc2ljIGJsb2NrOiB0d28gM3gzIGNvbnZzICsgaWRlbnRpdHkvcHJvamVjdGlvbiBzaG9ydGN1dC5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBleHBhbnNpb24gPSAxXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBvdXRfY2gsIHN0cmlkZT0xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuY29udjEgPSBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMywgc3RyaWRlPXN0cmlkZSwgcGFkZGluZz0xLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmJuMSAgID0gbm4uQmF0Y2hOb3JtMmQob3V0X2NoKVxuICAgICAgICBzZWxmLmNvbnYyID0gbm4uQ29udjJkKG91dF9jaCwgb3V0X2NoLCAzLCBwYWRkaW5nPTEsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuYm4yICAgPSBubi5CYXRjaE5vcm0yZChvdXRfY2gpXG4gICAgICAgIHNlbGYucmVsdSAgPSBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcbiAgICAgICAgc2VsZi5zaG9ydGN1dCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMSwgc3RyaWRlPXN0cmlkZSwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0yZChvdXRfY2gpKSBpZiAoc3RyaWRlICE9IDEgb3IgaW5fY2ggIT0gb3V0X2NoKSBlbHNlIG5uLklkZW50aXR5KClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5yZWx1KHNlbGYuYm4yKHNlbGYuY29udjIoc2VsZi5yZWx1KHNlbGYuYm4xKHNlbGYuY29udjEoeCkpKSkpICsgc2VsZi5zaG9ydGN1dCh4KSlcblxuY2xhc3MgQm90dGxlbmVjayhubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN1Jlc05ldCBib3R0bGVuZWNrOiAxeDEgcmVkdWNlIC1cdTAwM2UgM3gzIC1cdTAwM2UgMXgxIGV4cGFuZCArIHNob3J0Y3V0Llx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGV4cGFuc2lvbiA9IDRcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2gsIG1pZF9jaCwgc3RyaWRlPTEpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgb3V0X2NoID0gbWlkX2NoICogc2VsZi5leHBhbnNpb25cbiAgICAgICAgc2VsZi5jb252MSA9IG5uLkNvbnYyZChpbl9jaCwgbWlkX2NoLCAxLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmJuMSAgID0gbm4uQmF0Y2hOb3JtMmQobWlkX2NoKVxuICAgICAgICBzZWxmLmNvbnYyID0gbm4uQ29udjJkKG1pZF9jaCwgbWlkX2NoLCAzLCBzdHJpZGU9c3RyaWRlLCBwYWRkaW5nPTEsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuYm4yICAgPSBubi5CYXRjaE5vcm0yZChtaWRfY2gpXG4gICAgICAgIHNlbGYuY29udjMgPSBubi5Db252MmQobWlkX2NoLCBvdXRfY2gsIDEsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYuYm4zICAgPSBubi5CYXRjaE5vcm0yZChvdXRfY2gpXG4gICAgICAgIHNlbGYucmVsdSAgPSBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcbiAgICAgICAgc2VsZi5zaG9ydGN1dCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMSwgc3RyaWRlPXN0cmlkZSwgYmlhcz1GYWxzZSksXG4gICAgICAgICAgICBubi5CYXRjaE5vcm0yZChvdXRfY2gpKSBpZiAoaW5fY2ggIT0gb3V0X2NoIG9yIHN0cmlkZSAhPSAxKSBlbHNlIG5uLklkZW50aXR5KClcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBvdXQgPSBzZWxmLnJlbHUoc2VsZi5ibjEoc2VsZi5jb252MSh4KSkpXG4gICAgICAgIG91dCA9IHNlbGYucmVsdShzZWxmLmJuMihzZWxmLmNvbnYyKG91dCkpKVxuICAgICAgICByZXR1cm4gc2VsZi5yZWx1KHNlbGYuYm4zKHNlbGYuY29udjMob3V0KSkgKyBzZWxmLnNob3J0Y3V0KHgpKVxuXG5mb3IgQiwgYXJncyBpbiBbKEJhc2ljQmxvY2ssICg2NCwgNjQpKSwgKEJvdHRsZW5lY2ssICg2NCwgNjQpKV06XG4gICAgbSA9IEIoKmFyZ3MpXG4gICAgcCA9IHN1bSh4Lm51bWVsKCkgZm9yIHggaW4gbS5wYXJhbWV0ZXJzKCkpXG4gICAgcHJpbnQoXHUwMDI3e306IHs6LH0gcGFyYW1zXHUwMDI3LmZvcm1hdChCLl9fbmFtZV9fLCBwKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQcmUtQWN0aXZhdGlvbiBSZXNOZXQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkhlIGV0IGFsLiAoMjAxNikgcmV2aXNpdGVkIHRoZSByZXNpZHVhbCBibG9jayBhbmQgZm91bmQgdGhhdCBtb3ZpbmcgQmF0Y2hOb3JtIGFuZCBSZUxVIGJlZm9yZSB0aGUgY29udm9sdXRpb25zIChwcmUtYWN0aXZhdGlvbikgaW1wcm92ZXMgZ3JhZGllbnQgZmxvdyBhbmQgcmVndWxhcmlzYXRpb24uIFRoZSBwcmUtYWN0aXZhdGlvbiBvcmRlcmluZyBpcyBCTiDihpIgUmVMVSDihpIgQ29udiDihpIgQk4g4oaSIFJlTFUg4oaSIENvbnYsIGFuZCB0aGUgc2hvcnRjdXQgY2FycmllcyB0aGUgcmF3IChwcmUtYWN0aXZhdGlvbikgaW5wdXQuIFRoaXMgZW5zdXJlcyB0aGUgc2hvcnRjdXQgcGF0aCBpcyBhbHdheXMgYSBjbGVhbiBpZGVudGl0eSB3aXRoIG5vIGFjdGl2YXRpb25zIGFwcGxpZWQsIGFsbG93aW5nIGdyYWRpZW50IHRvIGZsb3cgdGhyb3VnaCB0aGUgc2tpcCBwYXRoIHdpdGhvdXQgYW55IHRyYW5zZm9ybWF0aW9uLiBFeHBlcmltZW50YWxseSwgcHJlLWFjdGl2YXRpb24gUmVzTmV0LTEwMDEgYWNoaWV2ZXMgNC42MiUgZXJyb3Igb24gQ0lGQVItMTAgdnMgNy42MSUgZm9yIHRoZSBvcmlnaW5hbCBSZXNOZXQtMTIwMi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgUG9zdEFjdGl2QmxvY2sobm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdPcmlnaW5hbCBSZXNOZXQ6IENvbnYtXHUwMDNlQk4tXHUwMDNlUmVMVS1cdTAwM2VDb252LVx1MDAzZUJOLCB0aGVuIGFkZCBzaG9ydGN1dCwgdGhlbiBSZUxVLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjaCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnNlcSA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoY2gsIGNoLCAzLCBwYWRkaW5nPTEsIGJpYXM9RmFsc2UpLCBubi5CYXRjaE5vcm0yZChjaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChjaCwgY2gsIDMsIHBhZGRpbmc9MSwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTJkKGNoKSlcbiAgICAgICAgc2VsZi5yZWx1ID0gbm4uUmVMVShpbnBsYWNlPVRydWUpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6IHJldHVybiBzZWxmLnJlbHUoc2VsZi5zZXEoeCkgKyB4KVxuXG5jbGFzcyBQcmVBY3RpdkJsb2NrKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3UHJlLWFjdGl2YXRpb24gUmVzTmV0IChIZSAyMDE2KTogQk4tXHUwMDNlUmVMVS1cdTAwM2VDb252LVx1MDAzZUJOLVx1MDAzZVJlTFUtXHUwMDNlQ29udiwgdGhlbiBhZGQgc2hvcnRjdXQuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNoKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYuc2VxID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKGNoKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLCBubi5Db252MmQoY2gsIGNoLCAzLCBwYWRkaW5nPTEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQoY2gpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksIG5uLkNvbnYyZChjaCwgY2gsIDMsIHBhZGRpbmc9MSwgYmlhcz1GYWxzZSkpXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6IHJldHVybiBzZWxmLnNlcSh4KSArIHhcblxuZGVmIGdyYWRfbm9ybShibG9jaywgeCk6XG4gICAgeCA9IHguY2xvbmUoKS5kZXRhY2goKS5yZXF1aXJlc19ncmFkXyhUcnVlKVxuICAgIGJsb2NrKHgpLnN1bSgpLmJhY2t3YXJkKClcbiAgICByZXR1cm4geC5ncmFkLm5vcm0oKS5pdGVtKClcblxudG9yY2gubWFudWFsX3NlZWQoMClcbnggPSB0b3JjaC5yYW5kbig0LCA2NCwgMjgsIDI4KVxucG9zdDEwID0gbm4uU2VxdWVudGlhbCgqW1Bvc3RBY3RpdkJsb2NrKDY0KSBmb3IgXyBpbiByYW5nZSgxMCldKVxucHJlMTAgID0gbm4uU2VxdWVudGlhbCgqW1ByZUFjdGl2QmxvY2soNjQpICBmb3IgXyBpbiByYW5nZSgxMCldKVxucHJpbnQoXHUwMDI3MTAtYmxvY2sgcG9zdC1hY3RpdmF0aW9uIGdyYWQgbm9ybTogezouNGZ9XHUwMDI3LmZvcm1hdChncmFkX25vcm0ocG9zdDEwLCB4KSkpXG5wcmludChcdTAwMjcxMC1ibG9jayBwcmUtYWN0aXZhdGlvbiAgZ3JhZCBub3JtOiB7Oi40Zn1cdTAwMjcuZm9ybWF0KGdyYWRfbm9ybShwcmUxMCwgeCkpKVxucHJpbnQoXHUwMDI3UHJlLWFjdGl2YXRpb24gbWFpbnRhaW5zIGdyYWRpZW50IG1hZ25pdHVkZSB0aHJvdWdoIGRlZXAgc3RhY2tzLlx1MDAyNykifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6ImluZm8iLCJ0aXRsZSI6IlRoZSBJZGVudGl0eSBTaG9ydGN1dCBJcyB0aGUgS2V5IEluc2lnaHQiLCJjb250ZW50IjoiVGhlIHNraXAgY29ubmVjdGlvbiB5ID0gRih4KSArIHggaXMgY29tcHV0YXRpb25hbGx5IGZyZWUgKGp1c3QgYWRkaXRpb24pIHlldCBmdW5kYW1lbnRhbGx5IGNoYW5nZXMgb3B0aW1pc2F0aW9uLiBWZWl0IGV0IGFsLiAoMjAxNikgc2hvd2VkIHRoYXQgYSBSZXNOZXQgd2l0aCBuIGJsb2NrcyBpbXBsaWNpdGx5IGVuc2VtYmxlcyAyXm4gcGF0aHMgb2YgdmFyeWluZyBkZXB0aHMg4oCUIG1vc3QgZ3JhZGllbnQgZmxvd3MgdGhyb3VnaCB0aGUgc2hvcnRlciBwYXRocyBkdXJpbmcgZWFybHkgdHJhaW5pbmcsIGdyYWR1YWxseSBlbmdhZ2luZyBkZWVwZXIgcGF0aHMgYXMgdGhlIG5ldHdvcmsgY29udmVyZ2VzLiBUaGlzIGVuc2VtYmxlIHZpZXcgZXhwbGFpbnMgd2h5IHJlc2lkdWFsIG5ldHdvcmtzIGFyZSBtdWNoIG1vcmUgcm9idXN0IHRvIHJlbW92aW5nIGluZGl2aWR1YWwgbGF5ZXJzIHRoYW4gcGxhaW4gbmV0d29ya3MsIHdoZXJlIGxheWVyIHJlbW92YWwgY29tcGxldGVseSBkaXNydXB0cyBpbmZvcm1hdGlvbiBmbG93LiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlc05ldC01MCBmcm9tIFNjcmF0Y2gifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlJlc05ldC01MCB1c2VzIGJvdHRsZW5lY2sgYmxvY2tzIGV4Y2x1c2l2ZWx5OiBlYWNoIGJsb2NrIGhhcyBhIDHDlzEgY29udiByZWR1Y2luZyBjaGFubmVscyBieSA0w5csIGEgM8OXMyBjb252IGF0IHRoZSByZWR1Y2VkIHNpemUsIGFuZCBhIDHDlzEgY29udiBleHBhbmRpbmcgYmFjayB0byA0w5cgdGhlIG1pZCBjaGFubmVscy4gVGhlIGFyY2hpdGVjdHVyZTogc3RlbSAoN8OXNyBjb252ICsgbWF4IHBvb2wpLCB0aGVuIGZvdXIgc3RhZ2VzIHdpdGggKDMsIDQsIDYsIDMpIGJvdHRsZW5lY2sgYmxvY2tzIGFuZCBjaGFubmVsIGNvdW50cyAoNjQsIDEyOCwgMjU2LCA1MTIpIOKAlCB0aGUgYWN0dWFsIG91dHB1dCBjaGFubmVscyBhcmUgNMOXIHRoZXNlIHZhbHVlcyAoMjU2LCA1MTIsIDEwMjQsIDIwNDgpLiBHbG9iYWwgYXZlcmFnZSBwb29saW5nIHJlcGxhY2VzIHRoZSBsYXJnZSBGQyBsYXllcnMgb2YgQWxleE5ldC9WR0csIGdpdmluZyBvbmx5IDIwNDjihpIxMDAwIGF0IHRoZSBoZWFkLiBUb3RhbDogMjVNIHBhcmFtZXRlcnMg4oCUIHZzIDEzOE0gZm9yIFZHRy0xNiBhdCBiZXR0ZXIgYWNjdXJhY3kuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIEJvdHRsZW5lY2sobm4uTW9kdWxlKTpcbiAgICBleHBhbnNpb24gPSA0XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBtaWRfY2gsIHN0cmlkZT0xKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIG91dF9jaCA9IG1pZF9jaCAqIHNlbGYuZXhwYW5zaW9uXG4gICAgICAgIHNlbGYuYm9keSA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2gsIG1pZF9jaCwgMSwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTJkKG1pZF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChtaWRfY2gsIG1pZF9jaCwgMywgc3RyaWRlPXN0cmlkZSwgcGFkZGluZz0xLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG1pZF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChtaWRfY2gsIG91dF9jaCwgMSwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTJkKG91dF9jaCkpXG4gICAgICAgIHNlbGYuc2hvcnRjdXQgPSAobm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAxLCBzdHJpZGU9c3RyaWRlLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQob3V0X2NoKSlcbiAgICAgICAgICAgIGlmIGluX2NoICE9IG91dF9jaCBvciBzdHJpZGUgIT0gMSBlbHNlIG5uLklkZW50aXR5KCkpXG4gICAgICAgIHNlbGYucmVsdSA9IG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiByZXR1cm4gc2VsZi5yZWx1KHNlbGYuYm9keSh4KSArIHNlbGYuc2hvcnRjdXQoeCkpXG5cbmRlZiBtYWtlX2xheWVyKGluX2NoLCBtaWRfY2gsIG5fYmxvY2tzLCBzdHJpZGU9MSk6XG4gICAgbGF5ZXJzID0gW0JvdHRsZW5lY2soaW5fY2gsIG1pZF9jaCwgc3RyaWRlKV1cbiAgICBvdXRfY2ggPSBtaWRfY2ggKiA0XG4gICAgZm9yIF8gaW4gcmFuZ2UoMSwgbl9ibG9ja3MpOlxuICAgICAgICBsYXllcnMuYXBwZW5kKEJvdHRsZW5lY2sob3V0X2NoLCBtaWRfY2gpKVxuICAgIHJldHVybiBubi5TZXF1ZW50aWFsKCpsYXllcnMpXG5cbmNsYXNzIFJlc05ldDUwKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG51bV9jbGFzc2VzPTEwMDApOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5zdGVtICAgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKDMsIDY0LCA3LCBzdHJpZGU9MiwgcGFkZGluZz0zLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKDY0KSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLCBubi5NYXhQb29sMmQoMywgc3RyaWRlPTIsIHBhZGRpbmc9MSkpXG4gICAgICAgIHNlbGYubGF5ZXIxID0gbWFrZV9sYXllcig2NCwgICA2NCwgIDMpXG4gICAgICAgIHNlbGYubGF5ZXIyID0gbWFrZV9sYXllcigyNTYsICAxMjgsIDQsIHN0cmlkZT0yKVxuICAgICAgICBzZWxmLmxheWVyMyA9IG1ha2VfbGF5ZXIoNTEyLCAgMjU2LCA2LCBzdHJpZGU9MilcbiAgICAgICAgc2VsZi5sYXllcjQgPSBtYWtlX2xheWVyKDEwMjQsIDUxMiwgMywgc3RyaWRlPTIpXG4gICAgICAgIHNlbGYuaGVhZCAgID0gbm4uU2VxdWVudGlhbChubi5BZGFwdGl2ZUF2Z1Bvb2wyZCgxKSwgbm4uRmxhdHRlbigpLCBubi5MaW5lYXIoMjA0OCwgbnVtX2NsYXNzZXMpKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5oZWFkKHNlbGYubGF5ZXI0KHNlbGYubGF5ZXIzKHNlbGYubGF5ZXIyKHNlbGYubGF5ZXIxKHNlbGYuc3RlbSh4KSkpKSkpXG5cbm1vZGVsID0gUmVzTmV0NTAoKVxueCA9IHRvcmNoLnJhbmRuKDIsIDMsIDIyNCwgMjI0KVxucGFyYW1zID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBtb2RlbC5wYXJhbWV0ZXJzKCkpIC8gMWU2XG5wcmludChcdTAwMjdSZXNOZXQtNTAgb3V0cHV0OiB7fSAgcGFyYW1zOiB7Oi4xZn1NXHUwMDI3LmZvcm1hdChtb2RlbCh4KS5zaGFwZSwgcGFyYW1zKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJXaWR0aCB2cyBEZXB0aDogV2lkZVJlc05ldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiWmFnb3J1eWtvIFx1MDAyNiBLb21vZGFraXMgKDIwMTYpIHNob3dlZCB0aGF0IHdpZGVuaW5nIHJlc2lkdWFsIG5ldHdvcmtzIOKAlCBpbmNyZWFzaW5nIGNoYW5uZWxzIGJ5IGEgd2lkZW5pbmcgZmFjdG9yIGsg4oCUIGNhbiBvdXRwZXJmb3JtIGRlcHRoIGluY3JlYXNlcyB3aGlsZSBiZWluZyBtb3JlIGNvbXB1dGF0aW9uYWxseSBlZmZpY2llbnQuIFdSTi0yOC0xMCAoMjggbGF5ZXJzLCBrPTEwKSBhY2hpZXZlcyAzLjg5JSBlcnJvciBvbiBDSUZBUi0xMCwgYmV0dGVyIHRoYW4gUmVzTmV0LTEwMDEuIFdpZGUgbmV0d29ya3MgYmVuZWZpdCBtb3JlIGZyb20gcGFyYWxsZWxpc20gb24gbW9kZXJuIEdQVXMgdGhhbiBkZWVwLWJ1dC10aGluIG5ldHdvcmtzIHdob3NlIHNlcXVlbnRpYWwgYm90dGxlbmVja3MgYXJlIGhhcmQgdG8gcGFyYWxsZWxpc2UuIFRoZSB0cmFkZS1vZmY6IFdpZGVSZXNOZXQgaGFzIG1vcmUgcGFyYW1ldGVycyBmb3IgYSBnaXZlbiBkZXB0aCBidXQgZmV3ZXIgdHJhaW5pbmcgc3RlcHMgdG8gY29udmVyZ2VuY2UuIERyb3BvdXQgaW4gd2lkZSBibG9ja3MgYWN0cyBhcyBlZmZlY3RpdmUgcmVndWxhcmlzYXRpb24gd2hlbiBjaGFubmVscyBhcmUgbGFyZ2UuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIFdpZGVCbG9jayhubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN1dpZGUgUmVzTmV0IGJsb2NrOiBwcmUtYWN0aXZhdGlvbiArIGRyb3BvdXQgZm9yIHJlZ3VsYXJpc2F0aW9uLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgb3V0X2NoLCBzdHJpZGU9MSwgZHJvcG91dD0wLjMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5ibjEgID0gbm4uQmF0Y2hOb3JtMmQoaW5fY2gpXG4gICAgICAgIHNlbGYuY29udjEgPSBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMywgc3RyaWRlPXN0cmlkZSwgcGFkZGluZz0xLCBiaWFzPUZhbHNlKVxuICAgICAgICBzZWxmLmRyb3AgID0gbm4uRHJvcG91dChkcm9wb3V0KVxuICAgICAgICBzZWxmLmJuMiAgID0gbm4uQmF0Y2hOb3JtMmQob3V0X2NoKVxuICAgICAgICBzZWxmLmNvbnYyID0gbm4uQ29udjJkKG91dF9jaCwgb3V0X2NoLCAzLCBwYWRkaW5nPTEsIGJpYXM9RmFsc2UpXG4gICAgICAgIHNlbGYucmVsdSAgPSBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcbiAgICAgICAgc2VsZi5zaG9ydGN1dCA9IChubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMSwgc3RyaWRlPXN0cmlkZSwgYmlhcz1GYWxzZSlcbiAgICAgICAgICAgICAgICAgICAgICAgICBpZiBpbl9jaCAhPSBvdXRfY2ggb3Igc3RyaWRlICE9IDEgZWxzZSBubi5JZGVudGl0eSgpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIG91dCA9IHNlbGYuY29udjEoc2VsZi5yZWx1KHNlbGYuYm4xKHgpKSlcbiAgICAgICAgb3V0ID0gc2VsZi5jb252MihzZWxmLmRyb3Aoc2VsZi5yZWx1KHNlbGYuYm4yKG91dCkpKSlcbiAgICAgICAgcmV0dXJuIG91dCArIHNlbGYuc2hvcnRjdXQoeClcblxuZGVmIHdybihkZXB0aD0xNiwgaz0xMCwgbnVtX2NsYXNzZXM9MTApOlxuICAgIHJldHVybiBubi5TZXF1ZW50aWFsKFxuICAgICAgICBubi5Db252MmQoMywgMTYsIDMsIHBhZGRpbmc9MSwgYmlhcz1GYWxzZSksXG4gICAgICAgIFdpZGVCbG9jaygxNiwgMTYqayksIFdpZGVCbG9jaygxNiprLCAzMiprLCBzdHJpZGU9MiksIFdpZGVCbG9jaygzMiprLCA2NCprLCBzdHJpZGU9MiksXG4gICAgICAgIG5uLkJhdGNoTm9ybTJkKDY0KmspLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgIG5uLkFkYXB0aXZlQXZnUG9vbDJkKDEpLCBubi5GbGF0dGVuKCksIG5uLkxpbmVhcig2NCprLCBudW1fY2xhc3NlcykpXG5cbnByaW50KFx1MDAyN3s6XHUwMDNjMTJ9IHs6XHUwMDNlMTB9IHs6XHUwMDNlMTR9XHUwMDI3LmZvcm1hdChcdTAwMjdNb2RlbFx1MDAyNywgXHUwMDI3UGFyYW1zXHUwMDI3LCBcdTAwMjdHRkxPUHMgKGVzdClcdTAwMjcpKVxuZm9yIGsgaW4gWzEsIDQsIDgsIDEwXTpcbiAgICBtID0gd3JuKGs9aylcbiAgICBwID0gc3VtKHgubnVtZWwoKSBmb3IgeCBpbiBtLnBhcmFtZXRlcnMoKSkgLyAxZTZcbiAgICBwcmludChcdTAwMjdXUk4tMTYtezpcdTAwM2M0fSB7Olx1MDAzZTkuMmZ9TVx1MDAyNy5mb3JtYXQoaywgcCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiV2h5IFNraXAgQ29ubmVjdGlvbnMgV29yayJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTXVsdGlwbGUgdGhlb3JldGljYWwgcGVyc3BlY3RpdmVzIGV4cGxhaW4gdGhlIGVmZmVjdGl2ZW5lc3Mgb2YgcmVzaWR1YWwgY29ubmVjdGlvbnMuIFRoZSBlbnNlbWJsZSB2aWV3IChWZWl0IGV0IGFsLikgc2hvd3MgdGhhdCBhIFJlc05ldCB3aXRoIG4gYmxvY2tzIGltcGxpY2l0bHkgcmVwcmVzZW50cyBhIDJebi1wYXRoIGVuc2VtYmxlLCB3aGVyZSBncmFkaWVudHMgcHJpbWFyaWx5IGZsb3cgdGhyb3VnaCBzaG9ydGVyIHBhdGhzIGVhcmx5IGluIHRyYWluaW5nLiBUaGUgdW5yb2xsZWQgaXRlcmF0aXZlIGVzdGltYXRpb24gdmlldyBpbnRlcnByZXRzIGVhY2ggcmVzaWR1YWwgYmxvY2sgYXMgb25lIHJlZmluZW1lbnQgc3RlcCBpbiBhbiBpdGVyYXRpdmUgZXN0aW1hdGlvbiBvZiB0aGUgdGFyZ2V0IHJlcHJlc2VudGF0aW9uLiBJbmZvcm1hdGlvbi10aGVvcmV0aWMgYW5hbHlzaXMgc2hvd3MgdGhhdCBza2lwIGNvbm5lY3Rpb25zIHByb3ZpZGUgYW4gaW5mb3JtYXRpb24gc3VwZXJoaWdod2F5IHRoYXQgcHJldmVudHMgYm90dGxlbmVja3MgaW4gZWFybHkgbGF5ZXJzLiBFbXBpcmljYWxseSwgcmVzaWR1YWwgbmV0d29ya3Mgd2l0aCByZW1vdmVkIGludGVybWVkaWF0ZSBsYXllcnMgZGVncmFkZSBncmFjZWZ1bGx5LCB3aGlsZSBwbGFpbiBuZXR3b3JrcyBmYWlsIGNhdGFzdHJvcGhpY2FsbHkgd2hlbiBsYXllcnMgYXJlIHJlbW92ZWQuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHcmFkaWVudCBmbG93OiBza2lwIGNvbm5lY3Rpb24gY29udHJpYnV0ZXMgK0kgdG8gdGhlIEphY29iaWFuLCBlbnN1cmluZyBub24tdmFuaXNoaW5nIGdyYWRpZW50cyBhdCBhbGwgZGVwdGhzLiIsIkVuc2VtYmxlIGVmZmVjdDogMl5uIGltcGxpY2l0IHBhdGhzIG9mIHZhcnlpbmcgZGVwdGhzIOKAlCBzaG9ydGVyIHBhdGhzIGRvbWluYXRlIGVhcmx5IHRyYWluaW5nLCBsb25nZXIgcGF0aHMgcmVmaW5lIGxhdGVyLiIsIklkZW50aXR5IGluaXRpYWxpc2F0aW9uOiBhdCBpbml0aWFsaXNhdGlvbiBGKHgpIOKJiCAwIChzbWFsbCB3ZWlnaHRzKSwgc28gdGhlIGJsb2NrIGlzIGFwcHJveGltYXRlbHkgaWRlbnRpdHkg4oCUIGEgc2Vuc2libGUgc3RhcnRpbmcgcG9pbnQuIiwiU2hhdHRlcmVkIGdyYWRpZW50cyAoQmFsZHV6emkgZXQgYWwuKTogcGxhaW4gbmV0d29ya3MgaGF2ZSBuZWFyLXplcm8gZ3JhZGllbnQgY29ycmVsYXRpb24gYmV0d2VlbiBhZGphY2VudCBsYXllcnM7IHJlc2lkdWFscyBwcmVzZXJ2ZSBpdC4iLCJMb3NzIGxhbmRzY2FwZSAoTGkgZXQgYWwuKTogc2tpcCBjb25uZWN0aW9ucyBjcmVhdGUgc21vb3RoZXIgbG9zcyBsYW5kc2NhcGVzIHdpdGggZmV3ZXIgbG9jYWwgbWluaW1hIGFuZCBzaGFycGVyIGdsb2JhbCBtaW5pbWEuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlc05ldCBWYXJpYW50cyBDb21wYXJpc29uIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiQmxvY2tzIiwiUGFyYW1zIiwiR0ZMT1BzIiwiVG9wLTEgQWNjIiwiS2V5IFZhcmlhbnQiXSwicm93cyI6W1siUmVzTmV0LTE4IiwiOCBiYXNpYyIsIjExTSIsIjEuOCIsIjY5LjglIiwiQmFzZWxpbmUsIHVzZWQgYXMgbGlnaHR3ZWlnaHQgYmFja2JvbmUiXSxbIlJlc05ldC0zNCIsIjE2IGJhc2ljIiwiMjFNIiwiMy43IiwiNzMuMyUiLCJMYXJnZXIgYmFzaWMtYmxvY2sgbmV0d29yayJdLFsiUmVzTmV0LTUwIiwiMTYgYm90dGxlbmVjayIsIjI1TSIsIjQuMSIsIjc2LjElIiwiU3RhbmRhcmQgYm90dGxlbmVjayBkZXNpZ24iXSxbIlJlc05ldC0xMDEiLCIzMyBib3R0bGVuZWNrIiwiNDRNIiwiNy45IiwiNzcuNCUiLCJEZWVwZXIgYmFja2JvbmUgZm9yIHNlZ21lbnRhdGlvbiJdLFsiUmVzTmV0LTE1MiIsIjUwIGJvdHRsZW5lY2siLCI2ME0iLCIxMS42IiwiNzguMyUiLCJJTFNWUkMgMjAxNSB3aW5uZXIiXSxbIldpZGVSZXNOZXQtMjgtMTAiLCIxMiB3aWRlIGJhc2ljIiwiMzZNIiwiNS4yIiwiOTUuOCUgQ0lGQVIiLCJXaWRlciwgc2hhbGxvd2VyLCBkcm9wb3V0Il0sWyJSZXNOZVh0LTUwICgzMsOXNGQpIiwiMTYgZ3JvdXBlZCBib3R0bGVuZWNrIiwiMjVNIiwiNC4zIiwiNzcuOCUiLCJHcm91cGVkIGNvbnZvbHV0aW9ucywgbXVsdGktYnJhbmNoIl1dfSx7InR5cGUiOiJkaXZpZGVyIn1d"
---
# ResNet — Residual Connections and Bottleneck Blocks

The degradation problem — where adding more layers to an already deep network increases training error, not just test error — suggests that deeper plain networks are harder to optimise, not that they overfit. He et al. (2015) hypothesised that learning the identity mapping through multiple nonlinear layers is difficult. Their solution: add an explicit shortcut y = F(x, W) + x so the network only needs to learn the residual F(x) ≈ 0 when the identity is optimal. This simple change enabled networks of 152 layers to outperform all prior architectures while being easier to optimise.

## The Degradation Problem in Deep Networks

A 56-layer plain network has higher training error than a 20-layer network on CIFAR-10 — counterintuitively worse despite having strictly more capacity. The 56-layer network could, in principle, learn the same function as the 20-layer network by setting extra layers to identity (F(x) = x). But in practice, random initialisation and SGD cannot find this solution efficiently. The optimisation landscape of deep networks without skip connections has many local minima and vanishing gradients make it hard to update early layers. Batch normalisation helps but does not fully solve the problem at 56+ layers.

## Residual Learning: y = F(x) + x

The residual formulation y = F(x, W) + x has two components: F(x, W) is the residual to be learned (a stack of conv-BN-ReLU layers), and x is the identity shortcut. When the optimal mapping is the identity, the network only needs to push F(x) → 0, which is easy — weights near zero is the natural initialisation. Gradient flow analysis reveals why this works: ∂L/∂x = ∂L/∂y · (∂F/∂x + I). The identity term I ensures gradients always flow backward without vanishing, regardless of the learned F. When input and output dimensions differ (due to stride or channel change), a projection shortcut uses a 1×1 conv to match dimensions.

```python
import torch
import torch.nn as nn

class BasicBlock(nn.Module):
    '''ResNet basic block: two 3x3 convs + identity/projection shortcut.'''
    expansion = 1
    def __init__(self, in_ch, out_ch, stride=1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_ch, out_ch, 3, stride=stride, padding=1, bias=False)
        self.bn1   = nn.BatchNorm2d(out_ch)
        self.conv2 = nn.Conv2d(out_ch, out_ch, 3, padding=1, bias=False)
        self.bn2   = nn.BatchNorm2d(out_ch)
        self.relu  = nn.ReLU(inplace=True)
        self.shortcut = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 1, stride=stride, bias=False),
            nn.BatchNorm2d(out_ch)) if (stride != 1 or in_ch != out_ch) else nn.Identity()

    def forward(self, x):
        return self.relu(self.bn2(self.conv2(self.relu(self.bn1(self.conv1(x))))) + self.shortcut(x))

class Bottleneck(nn.Module):
    '''ResNet bottleneck: 1x1 reduce -> 3x3 -> 1x1 expand + shortcut.'''
    expansion = 4
    def __init__(self, in_ch, mid_ch, stride=1):
        super().__init__()
        out_ch = mid_ch * self.expansion
        self.conv1 = nn.Conv2d(in_ch, mid_ch, 1, bias=False)
        self.bn1   = nn.BatchNorm2d(mid_ch)
        self.conv2 = nn.Conv2d(mid_ch, mid_ch, 3, stride=stride, padding=1, bias=False)
        self.bn2   = nn.BatchNorm2d(mid_ch)
        self.conv3 = nn.Conv2d(mid_ch, out_ch, 1, bias=False)
        self.bn3   = nn.BatchNorm2d(out_ch)
        self.relu  = nn.ReLU(inplace=True)
        self.shortcut = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 1, stride=stride, bias=False),
            nn.BatchNorm2d(out_ch)) if (in_ch != out_ch or stride != 1) else nn.Identity()

    def forward(self, x):
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.relu(self.bn2(self.conv2(out)))
        return self.relu(self.bn3(self.conv3(out)) + self.shortcut(x))

for B, args in [(BasicBlock, (64, 64)), (Bottleneck, (64, 64))]:
    m = B(*args)
    p = sum(x.numel() for x in m.parameters())
    print('{}: {:,} params'.format(B.__name__, p))
```

## Pre-Activation ResNet

He et al. (2016) revisited the residual block and found that moving BatchNorm and ReLU before the convolutions (pre-activation) improves gradient flow and regularisation. The pre-activation ordering is BN → ReLU → Conv → BN → ReLU → Conv, and the shortcut carries the raw (pre-activation) input. This ensures the shortcut path is always a clean identity with no activations applied, allowing gradient to flow through the skip path without any transformation. Experimentally, pre-activation ResNet-1001 achieves 4.62% error on CIFAR-10 vs 7.61% for the original ResNet-1202.

```python
import torch
import torch.nn as nn

class PostActivBlock(nn.Module):
    '''Original ResNet: Conv->BN->ReLU->Conv->BN, then add shortcut, then ReLU.'''
    def __init__(self, ch):
        super().__init__()
        self.seq = nn.Sequential(
            nn.Conv2d(ch, ch, 3, padding=1, bias=False), nn.BatchNorm2d(ch), nn.ReLU(inplace=True),
            nn.Conv2d(ch, ch, 3, padding=1, bias=False), nn.BatchNorm2d(ch))
        self.relu = nn.ReLU(inplace=True)
    def forward(self, x): return self.relu(self.seq(x) + x)

class PreActivBlock(nn.Module):
    '''Pre-activation ResNet (He 2016): BN->ReLU->Conv->BN->ReLU->Conv, then add shortcut.'''
    def __init__(self, ch):
        super().__init__()
        self.seq = nn.Sequential(
            nn.BatchNorm2d(ch), nn.ReLU(inplace=True), nn.Conv2d(ch, ch, 3, padding=1, bias=False),
            nn.BatchNorm2d(ch), nn.ReLU(inplace=True), nn.Conv2d(ch, ch, 3, padding=1, bias=False))
    def forward(self, x): return self.seq(x) + x

def grad_norm(block, x):
    x = x.clone().detach().requires_grad_(True)
    block(x).sum().backward()
    return x.grad.norm().item()

torch.manual_seed(0)
x = torch.randn(4, 64, 28, 28)
post10 = nn.Sequential(*[PostActivBlock(64) for _ in range(10)])
pre10  = nn.Sequential(*[PreActivBlock(64)  for _ in range(10)])
print('10-block post-activation grad norm: {:.4f}'.format(grad_norm(post10, x)))
print('10-block pre-activation  grad norm: {:.4f}'.format(grad_norm(pre10, x)))
print('Pre-activation maintains gradient magnitude through deep stacks.')
```

> **The Identity Shortcut Is the Key Insight**: The skip connection y = F(x) + x is computationally free (just addition) yet fundamentally changes optimisation. Veit et al. (2016) showed that a ResNet with n blocks implicitly ensembles 2^n paths of varying depths — most gradient flows through the shorter paths during early training, gradually engaging deeper paths as the network converges. This ensemble view explains why residual networks are much more robust to removing individual layers than plain networks, where layer removal completely disrupts information flow.

## ResNet-50 from Scratch

ResNet-50 uses bottleneck blocks exclusively: each block has a 1×1 conv reducing channels by 4×, a 3×3 conv at the reduced size, and a 1×1 conv expanding back to 4× the mid channels. The architecture: stem (7×7 conv + max pool), then four stages with (3, 4, 6, 3) bottleneck blocks and channel counts (64, 128, 256, 512) — the actual output channels are 4× these values (256, 512, 1024, 2048). Global average pooling replaces the large FC layers of AlexNet/VGG, giving only 2048→1000 at the head. Total: 25M parameters — vs 138M for VGG-16 at better accuracy.

```python
import torch
import torch.nn as nn

class Bottleneck(nn.Module):
    expansion = 4
    def __init__(self, in_ch, mid_ch, stride=1):
        super().__init__()
        out_ch = mid_ch * self.expansion
        self.body = nn.Sequential(
            nn.Conv2d(in_ch, mid_ch, 1, bias=False), nn.BatchNorm2d(mid_ch), nn.ReLU(inplace=True),
            nn.Conv2d(mid_ch, mid_ch, 3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(mid_ch), nn.ReLU(inplace=True),
            nn.Conv2d(mid_ch, out_ch, 1, bias=False), nn.BatchNorm2d(out_ch))
        self.shortcut = (nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 1, stride=stride, bias=False), nn.BatchNorm2d(out_ch))
            if in_ch != out_ch or stride != 1 else nn.Identity())
        self.relu = nn.ReLU(inplace=True)
    def forward(self, x): return self.relu(self.body(x) + self.shortcut(x))

def make_layer(in_ch, mid_ch, n_blocks, stride=1):
    layers = [Bottleneck(in_ch, mid_ch, stride)]
    out_ch = mid_ch * 4
    for _ in range(1, n_blocks):
        layers.append(Bottleneck(out_ch, mid_ch))
    return nn.Sequential(*layers)

class ResNet50(nn.Module):
    def __init__(self, num_classes=1000):
        super().__init__()
        self.stem   = nn.Sequential(
            nn.Conv2d(3, 64, 7, stride=2, padding=3, bias=False),
            nn.BatchNorm2d(64), nn.ReLU(inplace=True), nn.MaxPool2d(3, stride=2, padding=1))
        self.layer1 = make_layer(64,   64,  3)
        self.layer2 = make_layer(256,  128, 4, stride=2)
        self.layer3 = make_layer(512,  256, 6, stride=2)
        self.layer4 = make_layer(1024, 512, 3, stride=2)
        self.head   = nn.Sequential(nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(2048, num_classes))
    def forward(self, x):
        return self.head(self.layer4(self.layer3(self.layer2(self.layer1(self.stem(x))))))

model = ResNet50()
x = torch.randn(2, 3, 224, 224)
params = sum(p.numel() for p in model.parameters()) / 1e6
print('ResNet-50 output: {}  params: {:.1f}M'.format(model(x).shape, params))
```

## Width vs Depth: WideResNet

Zagoruyko & Komodakis (2016) showed that widening residual networks — increasing channels by a widening factor k — can outperform depth increases while being more computationally efficient. WRN-28-10 (28 layers, k=10) achieves 3.89% error on CIFAR-10, better than ResNet-1001. Wide networks benefit more from parallelism on modern GPUs than deep-but-thin networks whose sequential bottlenecks are hard to parallelise. The trade-off: WideResNet has more parameters for a given depth but fewer training steps to convergence. Dropout in wide blocks acts as effective regularisation when channels are large.

```python
import torch
import torch.nn as nn

class WideBlock(nn.Module):
    '''Wide ResNet block: pre-activation + dropout for regularisation.'''
    def __init__(self, in_ch, out_ch, stride=1, dropout=0.3):
        super().__init__()
        self.bn1  = nn.BatchNorm2d(in_ch)
        self.conv1 = nn.Conv2d(in_ch, out_ch, 3, stride=stride, padding=1, bias=False)
        self.drop  = nn.Dropout(dropout)
        self.bn2   = nn.BatchNorm2d(out_ch)
        self.conv2 = nn.Conv2d(out_ch, out_ch, 3, padding=1, bias=False)
        self.relu  = nn.ReLU(inplace=True)
        self.shortcut = (nn.Conv2d(in_ch, out_ch, 1, stride=stride, bias=False)
                         if in_ch != out_ch or stride != 1 else nn.Identity())

    def forward(self, x):
        out = self.conv1(self.relu(self.bn1(x)))
        out = self.conv2(self.drop(self.relu(self.bn2(out))))
        return out + self.shortcut(x)

def wrn(depth=16, k=10, num_classes=10):
    return nn.Sequential(
        nn.Conv2d(3, 16, 3, padding=1, bias=False),
        WideBlock(16, 16*k), WideBlock(16*k, 32*k, stride=2), WideBlock(32*k, 64*k, stride=2),
        nn.BatchNorm2d(64*k), nn.ReLU(inplace=True),
        nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(64*k, num_classes))

print('{:<12} {:>10} {:>14}'.format('Model', 'Params', 'GFLOPs (est)'))
for k in [1, 4, 8, 10]:
    m = wrn(k=k)
    p = sum(x.numel() for x in m.parameters()) / 1e6
    print('WRN-16-{:<4} {:>9.2f}M'.format(k, p))
```

## Why Skip Connections Work

Multiple theoretical perspectives explain the effectiveness of residual connections. The ensemble view (Veit et al.) shows that a ResNet with n blocks implicitly represents a 2^n-path ensemble, where gradients primarily flow through shorter paths early in training. The unrolled iterative estimation view interprets each residual block as one refinement step in an iterative estimation of the target representation. Information-theoretic analysis shows that skip connections provide an information superhighway that prevents bottlenecks in early layers. Empirically, residual networks with removed intermediate layers degrade gracefully, while plain networks fail catastrophically when layers are removed.

- Gradient flow: skip connection contributes +I to the Jacobian, ensuring non-vanishing gradients at all depths.
- Ensemble effect: 2^n implicit paths of varying depths — shorter paths dominate early training, longer paths refine later.
- Identity initialisation: at initialisation F(x) ≈ 0 (small weights), so the block is approximately identity — a sensible starting point.
- Shattered gradients (Balduzzi et al.): plain networks have near-zero gradient correlation between adjacent layers; residuals preserve it.
- Loss landscape (Li et al.): skip connections create smoother loss landscapes with fewer local minima and sharper global minima.

## ResNet Variants Comparison

| Model | Blocks | Params | GFLOPs | Top-1 Acc | Key Variant |
| --- | --- | --- | --- | --- | --- |
| ResNet-18 | 8 basic | 11M | 1.8 | 69.8% | Baseline, used as lightweight backbone |
| ResNet-34 | 16 basic | 21M | 3.7 | 73.3% | Larger basic-block network |
| ResNet-50 | 16 bottleneck | 25M | 4.1 | 76.1% | Standard bottleneck design |
| ResNet-101 | 33 bottleneck | 44M | 7.9 | 77.4% | Deeper backbone for segmentation |
| ResNet-152 | 50 bottleneck | 60M | 11.6 | 78.3% | ILSVRC 2015 winner |
| WideResNet-28-10 | 12 wide basic | 36M | 5.2 | 95.8% CIFAR | Wider, shallower, dropout |
| ResNeXt-50 (32×4d) | 16 grouped bottleneck | 25M | 4.3 | 77.8% | Grouped convolutions, multi-branch |

---

