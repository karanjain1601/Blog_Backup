---
title: "DeepLabV3+: Atrous Spatial Pyramid Pooling"
slug: "deeplabv3-aspp"
description: "DeepLab's ASPP captures multi-scale context using dilated convolutions at rates [6,12,18] — encoder-decoder design, Xception backbone, and performance on Pascal VOC and Cityscapes."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZWVwTGFiVjMrIChDaGVuIGV0IGFsLiwgMjAxOCkgY29tYmluZXMgYXRyb3VzIHNwYXRpYWwgcHlyYW1pZCBwb29saW5nIGZvciBtdWx0aS1zY2FsZSBjb250ZXh0IHdpdGggYW4gZW5jb2Rlci1kZWNvZGVyIHN0cnVjdHVyZSBmb3Igc2hhcnAgYm91bmRhcmllcy4gSXQgYWNoaWV2ZXMgODkuMCUgbUlvVSBvbiBQYXNjYWwgVk9DIDIwMTIgYW5kIDgyLjElIG9uIENpdHlzY2FwZXMg4oCUIGFtb25nIHRoZSBzdHJvbmdlc3QgQ05OLWJhc2VkIHJlc3VsdHMgYmVmb3JlIFZpc2lvbiBUcmFuc2Zvcm1lcnMuIFRoZSBrZXkgaW5zaWdodCBpcyB0aGF0IG9iamVjdHMgYXBwZWFyIGF0IHZhc3RseSBkaWZmZXJlbnQgc2NhbGVzLCBhbmQgYSBzaW5nbGUgcmVjZXB0aXZlIGZpZWxkIGNhbm5vdCBjYXB0dXJlIGFsbCBvZiB0aGVtIHNpbXVsdGFuZW91c2x5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIERlZXBMYWIgbGluZWFnZSBwcm9ncmVzc2VkIGZyb20gQ1JGIHBvc3QtcHJvY2Vzc2luZyAodjEpIHRvIEFTUFAgKHYyKSwgbXVsdGktc2NhbGUgQVNQUCB3aXRob3V0IENSRiAodjMpLCBhbmQgZmluYWxseSB0aGUgZW5jb2Rlci1kZWNvZGVyIGZ1c2lvbiBvZiB2MysuIEVhY2ggdmVyc2lvbiBpbXByb3ZlZCBtSW9VIGJ5IGFkZHJlc3NpbmcgYSBzcGVjaWZpYyBsaW1pdGF0aW9uOiBzY2FsZSB2YXJpYXRpb24gKEFTUFApLCBzcGF0aWFsIHByZWNpc2lvbiAoZGVjb2RlciksIGFuZCBiYWNrYm9uZSBjaG9pY2UgKFhjZXB0aW9uIHdpdGggZGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbnMgZm9yIGVmZmljaWVuY3kpLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF0cm91cyBTcGF0aWFsIFB5cmFtaWQgUG9vbGluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQVNQUCBhcHBsaWVzIHBhcmFsbGVsIGRpbGF0ZWQgY29udm9sdXRpb25zIGF0IG11bHRpcGxlIHJhdGVzIHRvIHRoZSBzYW1lIGZlYXR1cmUgbWFwLCB0aGVuIGNvbmNhdGVuYXRlcyB0aGVpciBvdXRwdXRzLiBSYXRlIDYgY2FwdHVyZXMgbWVkaXVtLXJhbmdlIGNvbnRleHQ7IHJhdGUgMTIgY2FwdHVyZXMgYnJvYWRlciBwYXR0ZXJuczsgcmF0ZSAxOCBjYXB0dXJlcyB2ZXJ5IGxhcmdlIG9iamVjdHMuIEEgZ2xvYmFsIGF2ZXJhZ2UgcG9vbGluZyBicmFuY2ggYWRkcyBpbWFnZS1sZXZlbCBjb250ZXh0LiBBbGwgYnJhbmNoZXMgYXJlIHByb2plY3RlZCB0byAyNTYgY2hhbm5lbHMgYW5kIGNvbmNhdGVuYXRlZCwgZ2l2aW5nIHRoZSBjbGFzc2lmaWVyIGEgcmljaCwgbXVsdGktc2NhbGUgZmVhdHVyZSByZXByZXNlbnRhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgQVNQUChubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaD0yMDQ4LCBvdXRfY2g9MjU2LCByYXRlcz0oNiwgMTIsIDE4KSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmJyYW5jaGVzID0gbm4uTW9kdWxlTGlzdChbXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMSksICAjIHJhdGU9MSAoMXgxKVxuICAgICAgICAgICAgKltubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMywgcGFkZGluZz1yLCBkaWxhdGlvbj1yKSBmb3IgciBpbiByYXRlc11cbiAgICAgICAgXSlcbiAgICAgICAgc2VsZi5nYXAgPSBubi5BZGFwdGl2ZUF2Z1Bvb2wyZCgxKSAgIyBnbG9iYWwgYXZnIHBvb2wgYnJhbmNoXG4gICAgICAgIHNlbGYuZ2FwX3Byb2ogPSBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMSlcbiAgICAgICAgc2VsZi5wcm9qID0gbm4uQ29udjJkKG91dF9jaCAqIChsZW4ocmF0ZXMpICsgMiksIG91dF9jaCwgMSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICBoLCB3ID0geC5zaGFwZVsyOl1cbiAgICAgICAgZmVhdHMgPSBbYih4KSBmb3IgYiBpbiBzZWxmLmJyYW5jaGVzXVxuICAgICAgICBnYXAgPSBGLmludGVycG9sYXRlKHNlbGYuZ2FwX3Byb2ooc2VsZi5nYXAoeCkpLCBzaXplPShoLHcpLCBtb2RlPVx1MDAyN2JpbGluZWFyXHUwMDI3LCBhbGlnbl9jb3JuZXJzPUZhbHNlKVxuICAgICAgICByZXR1cm4gc2VsZi5wcm9qKHRvcmNoLmNhdChmZWF0cyArIFtnYXBdLCBkaW09MSkpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgQVNQUCBtb2R1bGUgaXMgdGhlIGNvcmUgZGlmZmVyZW50aWF0b3Igb2YgdGhlIERlZXBMYWIgZmFtaWx5LiBCeSBhZ2dyZWdhdGluZyBjb250ZXh0IGF0IHJhdGVzIFs2LDEyLDE4XSwgaXQgZWZmZWN0aXZlbHkgbG9va3MgYXQgdGhlIGZlYXR1cmUgbWFwIHRocm91Z2ggd2luZG93cyBvZiBkaWZmZXJlbnQgc2l6ZXMgc2ltdWx0YW5lb3VzbHkuIFRoaXMgaXMgZXNwZWNpYWxseSBpbXBvcnRhbnQgZm9yIENpdHlzY2FwZXMgdXJiYW4gc2NlbmVzLCB3aGVyZSBzbWFsbCB0cmFmZmljIHNpZ25zIGFuZCBsYXJnZSBidWlsZGluZ3MgbXVzdCBib3RoIGJlIHNlZ21lbnRlZCBhY2N1cmF0ZWx5IGluIHRoZSBzYW1lIGZvcndhcmQgcGFzcy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZWVwTGFiVjMrIEVuY29kZXItRGVjb2RlciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVjMrIGFkZHMgYSBsaWdodHdlaWdodCBkZWNvZGVyIG9uIHRvcCBvZiB0aGUgQVNQUCBlbmNvZGVyLiBMb3ctbGV2ZWwgZmVhdHVyZXMgZnJvbSBhbiBlYXJseSBiYWNrYm9uZSBsYXllciAoMS80IHJlc29sdXRpb24pIGFyZSBwcm9qZWN0ZWQgdG8gNDggY2hhbm5lbHMsIGNvbmNhdGVuYXRlZCB3aXRoIHRoZSA0w5cgdXBzYW1wbGVkIEFTUFAgb3V0cHV0LCB0aGVuIHJlZmluZWQgd2l0aCB0d28gM8OXMyBjb252b2x1dGlvbnMgYmVmb3JlIGEgZmluYWwgNMOXIHVwc2FtcGxlIHRvIGlucHV0IHJlc29sdXRpb24uIFRoaXMgc2ltcGxlIGRlY29kZXIgcmVjb3ZlcnMgc2hhcnAgb2JqZWN0IGJvdW5kYXJpZXMgYXQgbG93IGFkZGl0aW9uYWwgY29tcHV0ZSBjb3N0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBEZWVwTGFiVjNQbHVzRGVjb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBsb3dfbGV2ZWxfY2g9MjU2LCBhc3BwX291dF9jaD0yNTYsIG51bV9jbGFzc2VzPTIxKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYubG93X2xldmVsX3Byb2ogPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGxvd19sZXZlbF9jaCwgNDgsIDEpLCBubi5CYXRjaE5vcm0yZCg0OCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuICAgICAgICApXG4gICAgICAgIHNlbGYuZnVzZSA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoYXNwcF9vdXRfY2ggKyA0OCwgMjU2LCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQoMjU2LCAyNTYsIDMsIHBhZGRpbmc9MSksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZCgyNTYsIG51bV9jbGFzc2VzLCAxKVxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBhc3BwX291dCwgbG93X2xldmVsX2ZlYXQsIGlucHV0X3NpemUpOlxuICAgICAgICBsb3cgPSBzZWxmLmxvd19sZXZlbF9wcm9qKGxvd19sZXZlbF9mZWF0KVxuICAgICAgICB4ID0gRi5pbnRlcnBvbGF0ZShhc3BwX291dCwgc2l6ZT1sb3cuc2hhcGVbMjpdLCBtb2RlPVx1MDAyN2JpbGluZWFyXHUwMDI3LCBhbGlnbl9jb3JuZXJzPUZhbHNlKVxuICAgICAgICB4ID0gc2VsZi5mdXNlKHRvcmNoLmNhdChbeCwgbG93XSwgZGltPTEpKVxuICAgICAgICByZXR1cm4gRi5pbnRlcnBvbGF0ZSh4LCBzaXplPWlucHV0X3NpemUsIG1vZGU9XHUwMDI3YmlsaW5lYXJcdTAwMjcsIGFsaWduX2Nvcm5lcnM9RmFsc2UpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgY2hvaWNlIG9mIGxvdy1sZXZlbCBmZWF0dXJlIGxheWVyIG1hdHRlcnMuIEluIFJlc05ldC1iYXNlZCBEZWVwTGFiVjMrLCBmZWF0dXJlcyBhZnRlciB0aGUgZmlyc3QgcmVzaWR1YWwgYmxvY2sgKHN0cmlkZSA0LCAyNTYgY2hhbm5lbHMpIGFyZSB1c2VkLiBGb3IgWGNlcHRpb24sIGZlYXR1cmVzIGFmdGVyIHRoZSBlbnRyeSBmbG93IGJsb2NrIGFyZSBwcmVmZXJyZWQuIFByb2plY3RpbmcgdGhlc2UgdG8ganVzdCA0OCBjaGFubmVscyBwcmV2ZW50cyB0aGVtIGZyb20gZG9taW5hdGluZyB0aGUgQVNQUCBvdXRwdXQgZHVyaW5nIGNvbmNhdGVuYXRpb24sIGJhbGFuY2luZyBzZW1hbnRpYyBkZXB0aCB3aXRoIHNwYXRpYWwgZGV0YWlsLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlhjZXB0aW9uIEJhY2tib25lIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZWVwTGFiVjMrIGFkb3B0cyBhIG1vZGlmaWVkIFhjZXB0aW9uIGFzIGl0cyBkZWZhdWx0IGJhY2tib25lLCByZXBsYWNpbmcgVkdHIGFuZCBSZXNOZXQuIFhjZXB0aW9uIHVzZXMgZGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbnMgdGhyb3VnaG91dCDigJQgc3BsaXR0aW5nIGEgc3RhbmRhcmQgY29udiBpbnRvIGEgcGVyLWNoYW5uZWwgZGVwdGh3aXNlIGNvbnYgYW5kIGEgcG9pbnR3aXNlIDHDlzEgY29udiDigJQgd2hpY2ggcmVkdWNlcyBwYXJhbWV0ZXJzIGFuZCBGTE9QcyB3aGlsZSBtYWludGFpbmluZyBhY2N1cmFjeS4gVGhlIG1vZGlmaWVkIGJhY2tib25lIGFkZHMgbWlkZGxlIGZsb3cgcmVwZXRpdGlvbnMgKDE2IGluc3RlYWQgb2YgOCkgYW5kIHVzZXMgZGlsYXRlZCBkZXB0aHdpc2Ugc2VwYXJhYmxlIGNvbnZvbHV0aW9ucyBpbiB0aGUgZXhpdCBmbG93LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgRGVwdGh3aXNlU2VwYXJhYmxlQ29udihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbl9jaCwgb3V0X2NoLCBzdHJpZGU9MSwgZGlsYXRpb249MSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmRlcHRod2lzZSA9IG5uLkNvbnYyZChcbiAgICAgICAgICAgIGluX2NoLCBpbl9jaCwgMywgc3RyaWRlPXN0cmlkZSxcbiAgICAgICAgICAgIHBhZGRpbmc9ZGlsYXRpb24sIGRpbGF0aW9uPWRpbGF0aW9uLCBncm91cHM9aW5fY2hcbiAgICAgICAgKVxuICAgICAgICBzZWxmLnBvaW50d2lzZSA9IG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAxKVxuICAgICAgICBzZWxmLmJuID0gbm4uQmF0Y2hOb3JtMmQob3V0X2NoKVxuICAgICAgICBzZWxmLnJlbHUgPSBubi5SZUxVKGlucGxhY2U9VHJ1ZSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5yZWx1KHNlbGYuYm4oc2VsZi5wb2ludHdpc2Uoc2VsZi5kZXB0aHdpc2UoeCkpKSkifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBYY2VwdGlvbiBiYWNrYm9uZSBpbiBEZWVwTGFiVjMrIGlzIHByZXRyYWluZWQgb24gSW1hZ2VOZXQgYW5kIGZpbmUtdHVuZWQgZW5kLXRvLWVuZC4gRm9yIHJlc291cmNlLWNvbnN0cmFpbmVkIGRlcGxveW1lbnRzLCBNb2JpbGVOZXRWMiBvciBFZmZpY2llbnROZXQtTGl0ZSBhcmUgY29tbW9uIHN1YnN0aXR1dGVzLiBNb2JpbGVOZXRWMi1iYWNrZWQgRGVlcExhYlYzKyBydW5zIGF0IHJlYWwtdGltZSBzcGVlZHMgb24gbW9iaWxlIGRldmljZXMsIG1ha2luZyBpdCB0aGUgYmFzaXMgb2YgR29vZ2xlXHUwMDI3cyBvbi1kZXZpY2Ugc2VnbWVudGF0aW9uIEFQSXMgdXNlZCBpbiB2aWRlbyBjb25mZXJlbmNpbmcgYmFja2dyb3VuZCBibHVyIGZlYXR1cmVzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRyYWluaW5nIG9uIENpdHlzY2FwZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNpdHlzY2FwZXMgY29udGFpbnMgNTAwMCBmaW5lbHkgYW5ub3RhdGVkIHVyYmFuIGRyaXZpbmcgaW1hZ2VzIGFjcm9zcyAxOSBjbGFzc2VzLiBUcmFpbmluZyBEZWVwTGFiVjMrIHJlcXVpcmVzIGxhcmdlIGNyb3Agc2l6ZXMgKDc2OcOXNzY5KSwgb3V0cHV0X3N0cmlkZT0xNiwgYW5kIGEgcG9seSBsZWFybmluZyByYXRlIHNjaGVkdWxlLiBUaGUgbW9kZWwgaXMgdHlwaWNhbGx5IGZpcnN0IHByZXRyYWluZWQgb24gQ09DTyBvciBQYXNjYWwgVk9DLCB0aGVuIGZpbmUtdHVuZWQgb24gQ2l0eXNjYXBlcy4gTXVsdGktc2NhbGUgaW5mZXJlbmNlIChjcm9wcyBhdCAwLjXDlywgMS4ww5csIDEuNzXDlykgYW5kIGhvcml6b250YWwgZmxpcHBpbmcgYXQgdGVzdCB0aW1lIGJvb3N0IG1Jb1UgYnkgMeKAkzIlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgbnVtcHkgYXMgbnBcblxuZGVmIGNvbXB1dGVfbWlvdShwcmVkLCB0YXJnZXQsIG51bV9jbGFzc2VzPTE5LCBpZ25vcmVfaW5kZXg9MjU1KTpcbiAgICBpb3VzID0gW11cbiAgICBmb3IgY2xzIGluIHJhbmdlKG51bV9jbGFzc2VzKTpcbiAgICAgICAgbWFzayA9IHRhcmdldCAhPSBpZ25vcmVfaW5kZXhcbiAgICAgICAgcCA9IChwcmVkID09IGNscykgXHUwMDI2IG1hc2tcbiAgICAgICAgdCA9ICh0YXJnZXQgPT0gY2xzKSBcdTAwMjYgbWFza1xuICAgICAgICBpbnRlciA9IChwIFx1MDAyNiB0KS5zdW0oKVxuICAgICAgICB1bmlvbiA9IChwIHwgdCkuc3VtKClcbiAgICAgICAgaWYgdW5pb24gPT0gMDpcbiAgICAgICAgICAgIGNvbnRpbnVlICAjIGNsYXNzIG5vdCBwcmVzZW50IGluIHRoaXMgaW1hZ2VcbiAgICAgICAgaW91cy5hcHBlbmQoaW50ZXIgLyB1bmlvbilcbiAgICByZXR1cm4gbnAubWVhbihpb3VzKVxuXG4jIFVzYWdlOiBhdmVyYWdlIGNvbXB1dGVfbWlvdSBvdmVyIGFsbCB2YWwgaW1hZ2VzIGZvciBmaW5hbCBtSW9VIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbiMgb3V0cHV0X3N0cmlkZT0xNjogc3RhbmRhcmQgc3RyaWRlcywgc2F2ZXMgbWVtb3J5XG4jIG91dHB1dF9zdHJpZGU9ODogcmVtb3ZlIHN0cmlkZSBpbiBsYXllcjMgYW5kIGxheWVyNCwgY29tcGVuc2F0ZSB3aXRoIGRpbGF0aW9uXG5kZWYgc2V0X291dHB1dF9zdHJpZGUocmVzbmV0LCBvdXRwdXRfc3RyaWRlPTE2KTpcbiAgICBpZiBvdXRwdXRfc3RyaWRlID09IDE2OlxuICAgICAgICAjIGxheWVyNDogc3RyaWRlPTEsIGRpbGF0aW9uPTJcbiAgICAgICAgcmVzbmV0LmxheWVyNFswXS5jb252Mi5zdHJpZGUgPSAoMSwgMSlcbiAgICAgICAgcmVzbmV0LmxheWVyNFswXS5jb252Mi5kaWxhdGlvbiA9ICgyLCAyKVxuICAgICAgICByZXNuZXQubGF5ZXI0WzBdLmNvbnYyLnBhZGRpbmcgPSAoMiwgMilcbiAgICBlbGlmIG91dHB1dF9zdHJpZGUgPT0gODpcbiAgICAgICAgIyBsYXllcjM6IHN0cmlkZT0xLCBkaWxhdGlvbj0yOyBsYXllcjQ6IHN0cmlkZT0xLCBkaWxhdGlvbj00XG4gICAgICAgIHBhc3MgICMgYXBwbHkgYW5hbG9nb3VzbHkgdG8gbGF5ZXIzIGFuZCBsYXllcjRcbiAgICByZXR1cm4gcmVzbmV0In0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIkRlZXBMYWIgdmVyc2lvbiIsIkFTUFAgcmF0ZXMiLCJCYWNrYm9uZSIsIlZPQyBtSW9VIiwiQ2l0eXNjYXBlcyBtSW9VIl0sInJvd3MiOltbInYxIiwiTm9uZSAoc2luZ2xlIHNjYWxlKSIsIlZHRy0xNiIsIjY3LjYiLCLigJQiXSxbInYyIiwiWzYsIDEyLCAxOCwgMjRdIiwiUmVzTmV0LTEwMSIsIjc5LjciLCI3MC40Il0sWyJ2MyIsIls2LCAxMiwgMThdIiwiUmVzTmV0LTEwMSIsIjg1LjciLCI4MS4zIl0sWyJ2MysgKFhjZXB0aW9uKSIsIls2LCAxMiwgMThdIiwiWGNlcHRpb24tNjUiLCI4OS4wIiwiODIuMSJdLFsidjMrIChSZXNOZXQtMTAxKSIsIls2LCAxMiwgMThdIiwiUmVzTmV0LTEwMSIsIjg3LjgiLCI4MC45Il1dfSx7InR5cGUiOiJjYWxsb3V0IiwiY2FsbG91dF90eXBlIjoid2FybmluZyIsImNvbnRlbnQiOiJEZWVwTGFiVjMrIGF0IG91dHB1dF9zdHJpZGU9OCBnaXZlcyB+MSUgYmV0dGVyIG1Jb1UgdGhhbiBvdXRwdXRfc3RyaWRlPTE2IGJ1dCB1c2VzIDR4IG1vcmUgR1BVIG1lbW9yeSBmb3IgdGhlIHNhbWUgaW5wdXQg4oCUIHVzZSBvdXRwdXRfc3RyaWRlPTE2IHVubGVzcyB5b3UgaGF2ZSBhYnVuZGFudCBWUkFNLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IktleSBUYWtlYXdheXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZXBMYWJWMysgYWNoaWV2ZXMgaXRzIHN0cm9uZyBwZXJmb3JtYW5jZSB0aHJvdWdoIHRocmVlIGNvbXBsZW1lbnRhcnkgaWRlYXM6IGRpbGF0ZWQgY29udm9sdXRpb25zIHRvIG1haW50YWluIHNwYXRpYWwgcmVzb2x1dGlvbiwgQVNQUCB0byBhZ2dyZWdhdGUgbXVsdGktc2NhbGUgY29udGV4dCwgYW5kIGEgbGlnaHR3ZWlnaHQgZGVjb2RlciB0byByZWNvdmVyIHNoYXJwIGJvdW5kYXJpZXMuIFRoZXNlIGlkZWFzIGFyZSBpbmRpdmlkdWFsbHkgdXNlZnVsIGFuZCBhcmUgd2lkZWx5IGFkb3B0ZWQgaW4gb3RoZXIgYXJjaGl0ZWN0dXJlcy4gVGhlIFhjZXB0aW9uIGJhY2tib25lIHdpdGggZGVwdGh3aXNlIHNlcGFyYWJsZSBjb252b2x1dGlvbnMgbWFrZXMgdGhlIG1vZGVsIGVmZmljaWVudCB3aXRob3V0IHNhY3JpZmljaW5nIGFjY3VyYWN5LiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRm9yIG5ldyBwcm9qZWN0cywgdG9yY2h2aXNpb24gcHJvdmlkZXMgZGVlcGxhYnYzX3Jlc25ldDEwMSBhbmQgZGVlcGxhYnYzX21vYmlsZW5ldF92M19sYXJnZSB3aXRoIHByZXRyYWluZWQgd2VpZ2h0cy4gVGhlIG1vYmlsZSB2YXJpYW50IHJ1bnMgYXQgaW50ZXJhY3RpdmUgc3BlZWRzIG9uIENQVS4gRm9yIG1heGltdW0gYWNjdXJhY3kgb24gQ2l0eXNjYXBlcyBvciBWT0MsIHVzZSB0aGUgWGNlcHRpb24gYmFja2JvbmUgd2l0aCBvdXRwdXRfc3RyaWRlPTE2LCBBU1BQIHJhdGVzIFs2LDEyLDE4XSwgYW5kIHRlc3QtdGltZSBhdWdtZW50YXRpb24uIEZpbmUtdHVuZSBmcm9tIENPQ08tcHJldHJhaW5lZCB3ZWlnaHRzIHJhdGhlciB0aGFuIHRyYWluaW5nIGZyb20gc2NyYXRjaCB0byBzYXZlIGNvbXB1dGUuIn1d"
---
# DeepLabV3+: Atrous Spatial Pyramid Pooling

## Overview

DeepLabV3+ (Chen et al., 2018) combines atrous spatial pyramid pooling for multi-scale context with an encoder-decoder structure for sharp boundaries. It achieves 89.0% mIoU on Pascal VOC 2012 and 82.1% on Cityscapes — among the strongest CNN-based results before Vision Transformers. The key insight is that objects appear at vastly different scales, and a single receptive field cannot capture all of them simultaneously.

The DeepLab lineage progressed from CRF post-processing (v1) to ASPP (v2), multi-scale ASPP without CRF (v3), and finally the encoder-decoder fusion of v3+. Each version improved mIoU by addressing a specific limitation: scale variation (ASPP), spatial precision (decoder), and backbone choice (Xception with depthwise separable convolutions for efficiency).

## Atrous Spatial Pyramid Pooling

ASPP applies parallel dilated convolutions at multiple rates to the same feature map, then concatenates their outputs. Rate 6 captures medium-range context; rate 12 captures broader patterns; rate 18 captures very large objects. A global average pooling branch adds image-level context. All branches are projected to 256 channels and concatenated, giving the classifier a rich, multi-scale feature representation.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ASPP(nn.Module):
    def __init__(self, in_ch=2048, out_ch=256, rates=(6, 12, 18)):
        super().__init__()
        self.branches = nn.ModuleList([
            nn.Conv2d(in_ch, out_ch, 1),  # rate=1 (1x1)
            *[nn.Conv2d(in_ch, out_ch, 3, padding=r, dilation=r) for r in rates]
        ])
        self.gap = nn.AdaptiveAvgPool2d(1)  # global avg pool branch
        self.gap_proj = nn.Conv2d(in_ch, out_ch, 1)
        self.proj = nn.Conv2d(out_ch * (len(rates) + 2), out_ch, 1)

    def forward(self, x):
        h, w = x.shape[2:]
        feats = [b(x) for b in self.branches]
        gap = F.interpolate(self.gap_proj(self.gap(x)), size=(h,w), mode='bilinear', align_corners=False)
        return self.proj(torch.cat(feats + [gap], dim=1))
```

The ASPP module is the core differentiator of the DeepLab family. By aggregating context at rates [6,12,18], it effectively looks at the feature map through windows of different sizes simultaneously. This is especially important for Cityscapes urban scenes, where small traffic signs and large buildings must both be segmented accurately in the same forward pass.

## DeepLabV3+ Encoder-Decoder

V3+ adds a lightweight decoder on top of the ASPP encoder. Low-level features from an early backbone layer (1/4 resolution) are projected to 48 channels, concatenated with the 4× upsampled ASPP output, then refined with two 3×3 convolutions before a final 4× upsample to input resolution. This simple decoder recovers sharp object boundaries at low additional compute cost.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DeepLabV3PlusDecoder(nn.Module):
    def __init__(self, low_level_ch=256, aspp_out_ch=256, num_classes=21):
        super().__init__()
        self.low_level_proj = nn.Sequential(
            nn.Conv2d(low_level_ch, 48, 1), nn.BatchNorm2d(48), nn.ReLU(inplace=True)
        )
        self.fuse = nn.Sequential(
            nn.Conv2d(aspp_out_ch + 48, 256, 3, padding=1), nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, 3, padding=1), nn.ReLU(inplace=True),
            nn.Conv2d(256, num_classes, 1)
        )

    def forward(self, aspp_out, low_level_feat, input_size):
        low = self.low_level_proj(low_level_feat)
        x = F.interpolate(aspp_out, size=low.shape[2:], mode='bilinear', align_corners=False)
        x = self.fuse(torch.cat([x, low], dim=1))
        return F.interpolate(x, size=input_size, mode='bilinear', align_corners=False)
```

The choice of low-level feature layer matters. In ResNet-based DeepLabV3+, features after the first residual block (stride 4, 256 channels) are used. For Xception, features after the entry flow block are preferred. Projecting these to just 48 channels prevents them from dominating the ASPP output during concatenation, balancing semantic depth with spatial detail.

## Xception Backbone

DeepLabV3+ adopts a modified Xception as its default backbone, replacing VGG and ResNet. Xception uses depthwise separable convolutions throughout — splitting a standard conv into a per-channel depthwise conv and a pointwise 1×1 conv — which reduces parameters and FLOPs while maintaining accuracy. The modified backbone adds middle flow repetitions (16 instead of 8) and uses dilated depthwise separable convolutions in the exit flow.

```python
import torch.nn as nn

class DepthwiseSeparableConv(nn.Module):
    def __init__(self, in_ch, out_ch, stride=1, dilation=1):
        super().__init__()
        self.depthwise = nn.Conv2d(
            in_ch, in_ch, 3, stride=stride,
            padding=dilation, dilation=dilation, groups=in_ch
        )
        self.pointwise = nn.Conv2d(in_ch, out_ch, 1)
        self.bn = nn.BatchNorm2d(out_ch)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        return self.relu(self.bn(self.pointwise(self.depthwise(x))))
```

The Xception backbone in DeepLabV3+ is pretrained on ImageNet and fine-tuned end-to-end. For resource-constrained deployments, MobileNetV2 or EfficientNet-Lite are common substitutes. MobileNetV2-backed DeepLabV3+ runs at real-time speeds on mobile devices, making it the basis of Google's on-device segmentation APIs used in video conferencing background blur features.

## Training on Cityscapes

Cityscapes contains 5000 finely annotated urban driving images across 19 classes. Training DeepLabV3+ requires large crop sizes (769×769), output_stride=16, and a poly learning rate schedule. The model is typically first pretrained on COCO or Pascal VOC, then fine-tuned on Cityscapes. Multi-scale inference (crops at 0.5×, 1.0×, 1.75×) and horizontal flipping at test time boost mIoU by 1–2%.

```python
import numpy as np

def compute_miou(pred, target, num_classes=19, ignore_index=255):
    ious = []
    for cls in range(num_classes):
        mask = target != ignore_index
        p = (pred == cls) & mask
        t = (target == cls) & mask
        inter = (p & t).sum()
        union = (p | t).sum()
        if union == 0:
            continue  # class not present in this image
        ious.append(inter / union)
    return np.mean(ious)

# Usage: average compute_miou over all val images for final mIoU
```

```python
import torch
import torch.nn as nn

# output_stride=16: standard strides, saves memory
# output_stride=8: remove stride in layer3 and layer4, compensate with dilation
def set_output_stride(resnet, output_stride=16):
    if output_stride == 16:
        # layer4: stride=1, dilation=2
        resnet.layer4[0].conv2.stride = (1, 1)
        resnet.layer4[0].conv2.dilation = (2, 2)
        resnet.layer4[0].conv2.padding = (2, 2)
    elif output_stride == 8:
        # layer3: stride=1, dilation=2; layer4: stride=1, dilation=4
        pass  # apply analogously to layer3 and layer4
    return resnet
```

| DeepLab version | ASPP rates | Backbone | VOC mIoU | Cityscapes mIoU |
| --- | --- | --- | --- | --- |
| v1 | None (single scale) | VGG-16 | 67.6 | — |
| v2 | [6, 12, 18, 24] | ResNet-101 | 79.7 | 70.4 |
| v3 | [6, 12, 18] | ResNet-101 | 85.7 | 81.3 |
| v3+ (Xception) | [6, 12, 18] | Xception-65 | 89.0 | 82.1 |
| v3+ (ResNet-101) | [6, 12, 18] | ResNet-101 | 87.8 | 80.9 |

> ****: DeepLabV3+ at output_stride=8 gives ~1% better mIoU than output_stride=16 but uses 4x more GPU memory for the same input — use output_stride=16 unless you have abundant VRAM.

## Key Takeaways

DeepLabV3+ achieves its strong performance through three complementary ideas: dilated convolutions to maintain spatial resolution, ASPP to aggregate multi-scale context, and a lightweight decoder to recover sharp boundaries. These ideas are individually useful and are widely adopted in other architectures. The Xception backbone with depthwise separable convolutions makes the model efficient without sacrificing accuracy.

For new projects, torchvision provides deeplabv3_resnet101 and deeplabv3_mobilenet_v3_large with pretrained weights. The mobile variant runs at interactive speeds on CPU. For maximum accuracy on Cityscapes or VOC, use the Xception backbone with output_stride=16, ASPP rates [6,12,18], and test-time augmentation. Fine-tune from COCO-pretrained weights rather than training from scratch to save compute.

