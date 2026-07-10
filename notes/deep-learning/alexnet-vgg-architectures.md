---
title: "AlexNet and VGG — Early Deep CNN Architectures"
slug: "alexnet-vgg-architectures"
description: "AlexNet (2012) proved deep CNNs with ReLU, dropout, and GPU training can win ImageNet; VGG (2014) showed that uniform 3×3 convolutions stacked deeply outperform large-kernel shallow networks. Both remain foundational feature extractors."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiQmVmb3JlIDIwMTIgdGhlIGRvbWluYW50IGNvbXB1dGVyIHZpc2lvbiBhcHByb2FjaCB3YXMgaGFuZC1jcmFmdGVkIGZlYXR1cmVzIChTSUZULCBIT0cpIGNvbWJpbmVkIHdpdGggc2hhbGxvdyBjbGFzc2lmaWVycy4gQWxleE5ldCAoS3JpemhldnNreSwgU3V0c2tldmVyLCBIaW50b24sIDIwMTIpIHNoYXR0ZXJlZCB0aGlzIHBhcmFkaWdtIGJ5IHdpbm5pbmcgSW1hZ2VOZXQgTFNWUkMgd2l0aCBhIDEwLjktcG9pbnQgdG9wLTUgZXJyb3IgaW1wcm92ZW1lbnQgb3ZlciB0aGUgcnVubmVyLXVwLiBJdCBkZW1vbnN0cmF0ZWQgdGhhdCBkZWVwIENOTnMgdHJhaW5lZCBvbiBHUFVzIHdpdGggbGFyZ2UgZGF0YXNldHMgY291bGQgbGVhcm4gZmFyIG1vcmUgcG93ZXJmdWwgcmVwcmVzZW50YXRpb25zIHRoYW4gYW55IGhhbmQtZW5naW5lZXJlZCBhbHRlcm5hdGl2ZS4gVkdHIChTaW1vbnlhbiBcdTAwMjYgWmlzc2VybWFuLCAyMDE0KSB0aGVuIHNob3dlZCB0aGF0IGFyY2hpdGVjdHVyYWwgc2ltcGxpY2l0eSDigJQgc3RhY2tpbmcgbWFueSAzw5czIGNvbnZvbHV0aW9ucyDigJQgY291bGQgcHVzaCBhY2N1cmFjeSBmdXJ0aGVyIHdoaWxlIHByb3ZpZGluZyBjbGVhbiwgcmV1c2FibGUgZmVhdHVyZSBleHRyYWN0b3JzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFsZXhOZXQgQXJjaGl0ZWN0dXJlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGV4TmV0IGNvbnNpc3RzIG9mIGZpdmUgY29udm9sdXRpb25hbCBsYXllcnMgZm9sbG93ZWQgYnkgdGhyZWUgZnVsbHktY29ubmVjdGVkIGxheWVycy4gVGhlIGZpcnN0IGNvbnYgbGF5ZXIgdXNlcyA5NiAxMcOXMTEgZmlsdGVycyB3aXRoIHN0cmlkZSA0IChsYXJnZSBzdHJpZGUgdG8gcXVpY2tseSByZWR1Y2UgdGhlIDIyNMOXMjI0IGlucHV0KS4gU3Vic2VxdWVudCBjb252IGxheWVycyB1c2UgM8OXMyBhbmQgNcOXNSBrZXJuZWxzLiBNYXggcG9vbGluZyBmb2xsb3dzIGxheWVycyAxLCAyLCBhbmQgNSB0byByZWR1Y2Ugc3BhdGlhbCBkaW1lbnNpb25zLiBMb2NhbCBSZXNwb25zZSBOb3JtYWxpc2F0aW9uIChMUk4pIOKAlCBhIG5vdy1kZXByZWNhdGVkIGxheWVyIHRoYXQgbm9ybWFsaXNlcyBhY3Jvc3MgYWRqYWNlbnQgZmVhdHVyZSBtYXBzIOKAlCBmb2xsb3dzIGxheWVycyAxIGFuZCAyLiBUaGUgdGhyZWUgRkMgbGF5ZXJzICg0MDk2IOKGkiA0MDk2IOKGkiAxMDAwKSBkb21pbmF0ZSB0aGUgcGFyYW1ldGVyIGNvdW50IGF0IDU4TSBvZiB0aGUgdG90YWwgNjBNIHBhcmFtZXRlcnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIEFsZXhOZXQobm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdBbGV4TmV0IChLcml6aGV2c2t5IGV0IGFsLiwgMjAxMikg4oCUIDUgY29udiArIDMgRkMgbGF5ZXJzLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBudW1fY2xhc3Nlcz0xMDAwLCBkcm9wb3V0PTAuNSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmZlYXR1cmVzID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZCgzLCA5NiwgMTEsIHN0cmlkZT00LCBwYWRkaW5nPTIpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Mb2NhbFJlc3BvbnNlTm9ybSg1LCBhbHBoYT0xZS00LCBiZXRhPTAuNzUsIGs9Mi4wKSxcbiAgICAgICAgICAgIG5uLk1heFBvb2wyZCgzLCBzdHJpZGU9MiksXG4gICAgICAgICAgICBubi5Db252MmQoOTYsIDI1NiwgNSwgcGFkZGluZz0yKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uTG9jYWxSZXNwb25zZU5vcm0oNSwgYWxwaGE9MWUtNCwgYmV0YT0wLjc1LCBrPTIuMCksXG4gICAgICAgICAgICBubi5NYXhQb29sMmQoMywgc3RyaWRlPTIpLFxuICAgICAgICAgICAgbm4uQ29udjJkKDI1NiwgMzg0LCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQoMzg0LCAzODQsIDMsIHBhZGRpbmc9MSksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZCgzODQsIDI1NiwgMywgcGFkZGluZz0xKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uTWF4UG9vbDJkKDMsIHN0cmlkZT0yKSlcbiAgICAgICAgc2VsZi5jbGFzc2lmaWVyID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkRyb3BvdXQoZHJvcG91dCksIG5uLkxpbmVhcigyNTYgKiA2ICogNiwgNDA5NiksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSxcbiAgICAgICAgICAgIG5uLkRyb3BvdXQoZHJvcG91dCksIG5uLkxpbmVhcig0MDk2LCA0MDk2KSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDQwOTYsIG51bV9jbGFzc2VzKSlcblxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICByZXR1cm4gc2VsZi5jbGFzc2lmaWVyKHNlbGYuZmVhdHVyZXMoeCkuZmxhdHRlbigxKSlcblxubW9kZWwgPSBBbGV4TmV0KClcbnggPSB0b3JjaC5yYW5kbigyLCAzLCAyMjQsIDIyNClcbnBhcmFtcyA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpKSAvIDFlNlxucHJpbnQoXHUwMDI3QWxleE5ldCBvdXRwdXQ6IHt9XHUwMDI3LmZvcm1hdChtb2RlbCh4KS5zaGFwZSkpXG5wcmludChcdTAwMjdQYXJhbWV0ZXJzOiB7Oi4xZn1NICg1OE0gaW4gRkMgbGF5ZXJzIGFsb25lKVx1MDAyNy5mb3JtYXQocGFyYW1zKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUcmFpbmluZyBJbm5vdmF0aW9ucyBpbiBBbGV4TmV0In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJBbGV4TmV0IGludHJvZHVjZWQgc2V2ZXJhbCB0cmFpbmluZyB0ZWNobmlxdWVzIHRoYXQgYmVjYW1lIHN0YW5kYXJkOiBSZUxVIGFjdGl2YXRpb25zIChpbnN0ZWFkIG9mIHRhbmggb3Igc2lnbW9pZCkgdHJhaW4gNsOXIGZhc3RlciBiZWNhdXNlIHRoZXkgZG8gbm90IHN1ZmZlciBmcm9tIHRoZSB2YW5pc2hpbmcgZ3JhZGllbnQgaW4gdGhlIHNhdHVyYXRpb24gcmVnaW9uOyBkcm9wb3V0IChwPTAuNSkgaW4gdGhlIHR3byBGQyBsYXllcnMgcmVkdWNlcyBjby1hZGFwdGF0aW9uIG9mIG5ldXJvbnMgYW5kIGhhbHZlcyB0ZXN0IGVycm9yIHJlbGF0aXZlIHRvIG5vIHJlZ3VsYXJpc2F0aW9uOyBkYXRhIGF1Z21lbnRhdGlvbiAocmFuZG9tIDIyNMOXMjI0IGNyb3BzIGFuZCBob3Jpem9udGFsIGZsaXBzIGZyb20gMjU2w5cyNTYgaW1hZ2VzLCBQQ0EgY29sb3VyIGppdHRlcikgZWZmZWN0aXZlbHkgcXVpbnR1cGxlcyB0aGUgdHJhaW5pbmcgc2V0LiBUcmFpbmluZyBvbiB0d28gR1RYIDU4MCBHUFVzIGZvciBzaXggZGF5cyB3YXMgZXNzZW50aWFsIOKAlCB0aGUgbW9kZWwgc3BsaXQgYWNyb3NzIEdQVXMsIHdpdGggY3Jvc3MtR1BVIGNvbW11bmljYXRpb24gb25seSBhdCBzcGVjaWZpYyBsYXllcnMuIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJSZUxVOiBmKHgpPW1heCgwLHgpIOKAlCBubyBzYXR1cmF0aW9uIGZvciB4XHUwMDNlMCwgZ3JhZGllbnQgYWx3YXlzIDEgb3IgMCwgdHJhaW5zIH42eCBmYXN0ZXIgdGhhbiBzaWdtb2lkL3RhbmguIiwiRHJvcG91dCAocD0wLjUpOiBhcHBsaWVkIHRvIEZDNiBhbmQgRkM3LCBmb3JjZXMgbmV1cm9ucyB0byBsZWFybiByZWR1bmRhbnQgcmVwcmVzZW50YXRpb25zLCBhY3RzIGFzIGltcGxpY2l0IGVuc2VtYmxlIG9mIDJebiBuZXR3b3Jrcy4iLCJMUk46IGxhdGVyYWwgaW5oaWJpdGlvbiBhY3Jvc3MgYWRqYWNlbnQgZmVhdHVyZSBtYXBzIOKAlCBub3JtYWxpc2VzIHJlc3BvbnNlIHJlbGF0aXZlIHRvIG5laWdoYm91cnMsIG1pbWljcyBiaW9sb2dpY2FsIGxhdGVyYWwgaW5oaWJpdGlvbi4gRHJvcHBlZCBpbiBsYXRlciBhcmNoaXRlY3R1cmVzLiIsIkRhdGEgYXVnbWVudGF0aW9uOiAyMjTDlzIyNCBjcm9wcyBmcm9tIHBhZGRlZCAyNTbDlzI1NiwgaG9yaXpvbnRhbCBmbGlwcywgUENBIGNvbG91ciBqaXR0ZXIg4oCUIGNyaXRpY2FsIGZvciBwcmV2ZW50aW5nIG92ZXJmaXR0aW5nIHdpdGggNjBNIHBhcmFtZXRlcnMuIiwiR1BVIHRyYWluaW5nOiBzcGxpdCBhcmNoaXRlY3R1cmUgYWNyb3NzIDIgR1BVcywgY3Jvc3MtR1BVIGNvbW11bmljYXRpb24gb25seSBhdCBsYXllcnMgMyBhbmQgRkMgbGF5ZXJzLiIsIldlaWdodCBpbml0aWFsaXNhdGlvbjogR2F1c3NpYW4oMCwgMC4wMSkgZm9yIHdlaWdodHMsIGNvbnN0YW50IDAgb3IgMSBmb3IgYmlhc2VzIChsYXllci1kZXBlbmRlbnQpLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJWR0c6IERlcHRoIFRocm91Z2ggU21hbGwgS2VybmVscyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVkdHIChTaW1vbnlhbiBcdTAwMjYgWmlzc2VybWFuLCAyMDE0KSBtYWtlcyBvbmUgZGVzaWduIGNob2ljZSBhbmQgcHVyc3VlcyBpdCByZWxlbnRsZXNzbHk6IHVzZSBvbmx5IDPDlzMgY29udm9sdXRpb25zIHdpdGggc3RyaWRlIDEgYW5kIHBhZGRpbmcgMS4gVHdvIHN0YWNrZWQgM8OXMyBjb252cyBoYXZlIHRoZSBzYW1lIHJlY2VwdGl2ZSBmaWVsZCBhcyBvbmUgNcOXNSBjb252IGJ1dCB1c2UgMsOXKDPDlzPDl0PCsikgPSAxOEPCsiBwYXJhbWV0ZXJzIGluc3RlYWQgb2YgMjVDwrIuIFRocmVlIHN0YWNrZWQgM8OXMyBjb252cyBtYXRjaCBhIDfDlzcgY29udjogMjdDwrIgdnMgNDlDwrIgcGFyYW1zIOKAlCBhIDQ0JSBzYXZpbmcg4oCUIHBsdXMgdHdvIGV4dHJhIFJlTFUgbm9ubGluZWFyaXRpZXMgd2hpY2ggaW5jcmVhc2UgZXhwcmVzc2l2ZW5lc3MuIFZHRyBpcyBvcmdhbmlzZWQgaW50byBmaXZlIGJsb2NrcyB3aXRoIHByb2dyZXNzaXZlbHkgZG91YmxpbmcgY2hhbm5lbHMgKDY0LCAxMjgsIDI1NiwgNTEyLCA1MTIpLCBlYWNoIGVuZGluZyB3aXRoIGEgMsOXMiBtYXggcG9vbC4gVkdHMTYgaGFzIDE2IHdlaWdodCBsYXllcnM7IFZHRzE5IGhhcyAxOS4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmZyb20gdHlwaW5nIGltcG9ydCBMaXN0XG5cbmRlZiB2Z2dfYmxvY2soaW5fY2g6IGludCwgb3V0X2NoOiBpbnQsIG5fY29udnM6IGludCkgLVx1MDAzZSBubi5TZXF1ZW50aWFsOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN1ZHRyBibG9jazogbl9jb252cyB4IChDb252IDN4MyArIEJOICsgUmVMVSksIHRoZW4gTWF4UG9vbCAyeDIuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgbGF5ZXJzOiBMaXN0W25uLk1vZHVsZV0gPSBbXVxuICAgIGZvciBfIGluIHJhbmdlKG5fY29udnMpOlxuICAgICAgICBsYXllcnMgKz0gW25uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAzLCBwYWRkaW5nPTEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG91dF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKV1cbiAgICAgICAgaW5fY2ggPSBvdXRfY2hcbiAgICBsYXllcnMuYXBwZW5kKG5uLk1heFBvb2wyZCgyLCBzdHJpZGU9MikpXG4gICAgcmV0dXJuIG5uLlNlcXVlbnRpYWwoKmxheWVycylcblxuY2xhc3MgVkdHMTYobm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdWR0ctMTYgd2l0aCBiYXRjaCBub3JtYWxpc2F0aW9uIChTaW1vbnlhbiBcdTAwMjYgWmlzc2VybWFuLCAyMDE0KS5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbnVtX2NsYXNzZXM9MTAwMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmZlYXR1cmVzID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIHZnZ19ibG9jaygzLCA2NCwgMiksICAgICMgMjI0IC1cdTAwM2UgMTEyXG4gICAgICAgICAgICB2Z2dfYmxvY2soNjQsIDEyOCwgMiksICAjIDExMiAtXHUwMDNlIDU2XG4gICAgICAgICAgICB2Z2dfYmxvY2soMTI4LCAyNTYsIDMpLCAjIDU2ICAtXHUwMDNlIDI4XG4gICAgICAgICAgICB2Z2dfYmxvY2soMjU2LCA1MTIsIDMpLCAjIDI4ICAtXHUwMDNlIDE0XG4gICAgICAgICAgICB2Z2dfYmxvY2soNTEyLCA1MTIsIDMpKSAjIDE0ICAtXHUwMDNlIDdcbiAgICAgICAgc2VsZi5oZWFkID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkZsYXR0ZW4oKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcig1MTIgKiA3ICogNywgNDA5NiksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSwgbm4uRHJvcG91dCgwLjUpLFxuICAgICAgICAgICAgbm4uTGluZWFyKDQwOTYsIDQwOTYpLCAgICAgICAgbm4uUmVMVShpbnBsYWNlPVRydWUpLCBubi5Ecm9wb3V0KDAuNSksXG4gICAgICAgICAgICBubi5MaW5lYXIoNDA5NiwgbnVtX2NsYXNzZXMpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6IHJldHVybiBzZWxmLmhlYWQoc2VsZi5mZWF0dXJlcyh4KSlcblxubW9kZWwgPSBWR0cxNigpXG54ID0gdG9yY2gucmFuZG4oMSwgMywgMjI0LCAyMjQpXG5wYXJhbXMgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSkgLyAxZTZcbnByaW50KFx1MDAyN1ZHRy0xNiBvdXRwdXQ6IHt9XHUwMDI3LmZvcm1hdChtb2RlbCh4KS5zaGFwZSkpXG5wcmludChcdTAwMjdQYXJhbWV0ZXJzOiB7Oi4xZn1NXHUwMDI3LmZvcm1hdChwYXJhbXMpKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlJlY2VwdGl2ZSBGaWVsZCBhbmQgUGFyYW1ldGVyIEFuYWx5c2lzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgZWZmZWN0aXZlIHJlY2VwdGl2ZSBmaWVsZCBvZiBzdGFja2VkIDPDlzMgY29udnMgZ3Jvd3MgbGluZWFybHk6IG9uZSAzw5czIGdpdmVzIFJGPTM7IHR3byBnaXZlIFJGPTUgKG1hdGNoaW5nIG9uZSA1w5c1KTsgdGhyZWUgZ2l2ZSBSRj03IChtYXRjaGluZyBvbmUgN8OXNykuIFRoZSBwYXJhbWV0ZXIgc2F2aW5ncyBhcmUgc2lnbmlmaWNhbnQ6IHR3byAzw5czIGNvbnZzIG9uIEMgY2hhbm5lbHMgY29zdCAyw5c5Q8KyID0gMThDwrIgcGFyYW1ldGVycyB3aGlsZSBhIHNpbmdsZSA1w5c1IGNvc3RzIDI1Q8KyICgyOCUgbW9yZSkuIFRocmVlIDPDlzMgY29udnMgY29zdCAyN0PCsiB2ZXJzdXMgNDlDwrIgZm9yIGEgN8OXNyAoNDQlIG1vcmUpLiBBZGRpdGlvbmFsbHksIGVhY2ggZXh0cmEgY29udiBsYXllciBhZGRzIGEgUmVMVSBub25saW5lYXJpdHksIHdoaWNoIGluY3JlYXNlcyB0aGUgZnVuY3Rpb24gY2xhc3NcdTAwMjdzIGV4cHJlc3NpdmVuZXNzIHdpdGhvdXQgZXh0cmEgc3BhdGlhbCBvdmVyaGVhZC4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuZGVmIGNvdW50X3BhcmFtcyhtb2RlbCk6XG4gICAgcmV0dXJuIHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZClcblxuZGVmIHJmX29mX3N0YWNrZWRfM3gzKG4pOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN0VmZmVjdGl2ZSByZWNlcHRpdmUgZmllbGQgb2YgbiBzdGFja2VkIDN4MyBjb252cy5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICByZXR1cm4gMSArIDIgKiBuXG5cbiMgUGFyYW1ldGVyIGNvbXBhcmlzb246IHN0YWNrZWQgM3gzIHZzIGVxdWl2YWxlbnQgbGFyZ2Uga2VybmVsXG5DID0gMjU2XG5jb25maWdzID0gW1xuICAgIChcdTAwMjdvbmUgNXg1XHUwMDI3LCBubi5Db252MmQoQywgQywgNSwgcGFkZGluZz0yKSksXG4gICAgKFx1MDAyN3R3byAzeDNcdTAwMjcsIG5uLlNlcXVlbnRpYWwobm4uQ29udjJkKEMsIEMsIDMsIHBhZGRpbmc9MSksIG5uLkNvbnYyZChDLCBDLCAzLCBwYWRkaW5nPTEpKSksXG4gICAgKFx1MDAyN29uZSA3eDdcdTAwMjcsIG5uLkNvbnYyZChDLCBDLCA3LCBwYWRkaW5nPTMpKSxcbiAgICAoXHUwMDI3dGhyZWUgM3gzXHUwMDI3LCBubi5TZXF1ZW50aWFsKFxuICAgICAgICBubi5Db252MmQoQywgQywgMywgcGFkZGluZz0xKSwgbm4uQ29udjJkKEMsIEMsIDMsIHBhZGRpbmc9MSksXG4gICAgICAgIG5uLkNvbnYyZChDLCBDLCAzLCBwYWRkaW5nPTEpKSlcbl1cbnByaW50KFx1MDAyN3s6XHUwMDNjMTR9IHs6XHUwMDNlMTJ9IHs6XHUwMDNlOH0gezpcdTAwM2UxMn1cdTAwMjcuZm9ybWF0KFx1MDAyN0NvbmZpZ1x1MDAyNywgXHUwMDI3UGFyYW1zXHUwMDI3LCBcdTAwMjdSRlx1MDAyNywgXHUwMDI3U2F2aW5nc1x1MDAyNykpXG5yZWY1ID0gY291bnRfcGFyYW1zKGNvbmZpZ3NbMF1bMV0pXG5yZWY3ID0gY291bnRfcGFyYW1zKGNvbmZpZ3NbMl1bMV0pXG5mb3IgbmFtZSwgbW9kdWxlIGluIGNvbmZpZ3M6XG4gICAgcCA9IGNvdW50X3BhcmFtcyhtb2R1bGUpXG4gICAgcmYgPSByZl9vZl9zdGFja2VkXzN4MygyIGlmIFx1MDAyNzN4M1x1MDAyNyBpbiBuYW1lIGFuZCBcdTAwMjd0d29cdTAwMjcgaW4gbmFtZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgZWxzZSAzIGlmIFx1MDAyN3RocmVlXHUwMDI3IGluIG5hbWUgZWxzZSAxKVxuICAgIHJlZiA9IHJlZjUgaWYgXHUwMDI3NXg1XHUwMDI3IGluIG5hbWUgb3IgXHUwMDI3dHdvXHUwMDI3IGluIG5hbWUgZWxzZSByZWY3XG4gICAgc2F2ZSA9IFx1MDAyNy0tLVx1MDAyNyBpZiBuYW1lIGluIChcdTAwMjdvbmUgNXg1XHUwMDI3LCBcdTAwMjdvbmUgN3g3XHUwMDI3KSBlbHNlIFx1MDAyNy17Oi4wZn0lXHUwMDI3LmZvcm1hdCgxMDAqKDEgLSBwL3JlZikpXG4gICAgcHJpbnQoXHUwMDI3ezpcdTAwM2MxNH0gezpcdTAwM2UxMix9IHs6XHUwMDNlOH0gezpcdTAwM2UxMn1cdTAwMjcuZm9ybWF0KG5hbWUsIHAsIHJmLCBzYXZlKSkifSx7InR5cGUiOiJjYWxsb3V0IiwidmFyaWFudCI6Indhcm5pbmciLCJ0aXRsZSI6IlZHR1x1MDAyN3MgRkMgTGF5ZXIgQm90dGxlbmVjayIsImNvbnRlbnQiOiJWR0cxNiBoYXMgMTM4TSBwYXJhbWV0ZXJzIOKAlCBidXQgMTIzTSAoODklKSBsaXZlIGluIHRoZSB0aHJlZSBGQyBsYXllcnMgKDUxMsOXN8OXN+KGkjQwOTYsIDQwOTbihpI0MDk2LCA0MDk24oaSMTAwMCkuIFRoZSBjb252IGxheWVycyB0aGF0IGRvIGFsbCB0aGUgc3BhdGlhbCBmZWF0dXJlIGV4dHJhY3Rpb24gYWNjb3VudCBmb3Igb25seSAxNU0gcGFyYW1ldGVycy4gTW9kZXJuIGFyY2hpdGVjdHVyZXMgcmVwbGFjZSBGQyBsYXllcnMgd2l0aCBnbG9iYWwgYXZlcmFnZSBwb29saW5nIChHQVApLCBlbGltaW5hdGluZyB0aGlzIGJvdHRsZW5lY2s6IFJlc05ldC01MCBoYXMgb25seSAyNU0gcGFyYW1ldGVycyBhbmQgR29vZ0xlTmV0IGhhcyA1TSDigJQgYm90aCBtb3JlIGFjY3VyYXRlIHRoYW4gVkdHLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZHRyBhcyBGZWF0dXJlIEV4dHJhY3RvciJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRGVzcGl0ZSBiZWluZyBzdXJwYXNzZWQgb24gSW1hZ2VOZXQgYWNjdXJhY3ksIFZHR1x1MDAyN3MgZmVhdHVyZSByZXByZXNlbnRhdGlvbnMgcmVtYWluIHBvd2VyZnVsIGZvciB0cmFuc2ZlciBsZWFybmluZywgcGVyY2VwdHVhbCBsb3NzIGluIHN0eWxlIHRyYW5zZmVyIChHYXR5cyBldCBhbC4sIDIwMTUpLCBhbmQgYXMgYSBiYWNrYm9uZSBmb3IgZG93bnN0cmVhbSB0YXNrcy4gVGhlIHVuaWZvcm0gM8OXMyBjb252IHN0cnVjdHVyZSBtYWtlcyBpdCBlYXN5IHRvIGV4dHJhY3QgZmVhdHVyZXMgYXQgYW55IGRlcHRoLiBDb21tb24gZXh0cmFjdGlvbiBwb2ludHM6IHJlbHUzXzMgKDI1NiBjaGFubmVscywgMjjDlzI4IGZvciAyMjTDlzIyNCBpbnB1dCkgZm9yIHRleHR1cmUtcmljaCBmZWF0dXJlczsgcmVsdTRfMyAoNTEyIGNoYW5uZWxzLCAxNMOXMTQpIGZvciBzZW1hbnRpYyBvYmplY3QgZmVhdHVyZXM7IHJlbHU1XzMgKDUxMiBjaGFubmVscywgN8OXNykgZm9yIHRoZSBtb3N0IGFic3RyYWN0IGZlYXR1cmVzLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0b3JjaHZpc2lvbiBpbXBvcnQgbW9kZWxzXG5cbmNsYXNzIFZHR0ZlYXR1cmVFeHRyYWN0b3Iobm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdWR0ctMTYgcHJldHJhaW5lZCBiYWNrYm9uZSB3aXRoIGEgbGlnaHR3ZWlnaHQgY2xhc3NpZmljYXRpb24gaGVhZC5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbnVtX2NsYXNzZXM9MTAsIGZlYXR1cmVfbGF5ZXI9MzAsIGZyZWV6ZT1UcnVlKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHZnZyA9IG1vZGVscy52Z2cxNl9ibih3ZWlnaHRzPW1vZGVscy5WR0cxNl9CTl9XZWlnaHRzLklNQUdFTkVUMUtfVjEpXG4gICAgICAgIHNlbGYuYmFja2JvbmUgPSBubi5TZXF1ZW50aWFsKCpsaXN0KHZnZy5mZWF0dXJlcy5jaGlsZHJlbigpKVs6ZmVhdHVyZV9sYXllcl0pXG4gICAgICAgIGlmIGZyZWV6ZTpcbiAgICAgICAgICAgIGZvciBwYXJhbSBpbiBzZWxmLmJhY2tib25lLnBhcmFtZXRlcnMoKTpcbiAgICAgICAgICAgICAgICBwYXJhbS5yZXF1aXJlc19ncmFkID0gRmFsc2VcbiAgICAgICAgc2VsZi5oZWFkID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkFkYXB0aXZlQXZnUG9vbDJkKCg0LCA0KSksIG5uLkZsYXR0ZW4oKSxcbiAgICAgICAgICAgIG5uLkxpbmVhcig1MTIgKiAxNiwgNTEyKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpLFxuICAgICAgICAgICAgbm4uRHJvcG91dCgwLjUpLCBubi5MaW5lYXIoNTEyLCBudW1fY2xhc3NlcykpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgcmV0dXJuIHNlbGYuaGVhZChzZWxmLmJhY2tib25lKHgpKVxuXG5tb2RlbCA9IFZHR0ZlYXR1cmVFeHRyYWN0b3IobnVtX2NsYXNzZXM9MTAsIGZyZWV6ZT1UcnVlKVxudG90YWwgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIG1vZGVsLnBhcmFtZXRlcnMoKSlcbnRyYWluYWJsZSA9IHN1bShwLm51bWVsKCkgZm9yIHAgaW4gbW9kZWwucGFyYW1ldGVycygpIGlmIHAucmVxdWlyZXNfZ3JhZClcbnggPSB0b3JjaC5yYW5kbig0LCAzLCAyMjQsIDIyNClcbm91dCA9IG1vZGVsKHgpXG5wcmludChcdTAwMjdPdXRwdXQ6IHt9XHUwMDI3LmZvcm1hdChvdXQuc2hhcGUpKVxucHJpbnQoXHUwMDI3VHJhaW5hYmxlOiB7Oix9IC8gVG90YWw6IHs6LH0gKHs6LjFmfSUpXHUwMDI3LmZvcm1hdChcbiAgICB0cmFpbmFibGUsIHRvdGFsLCAxMDAgKiB0cmFpbmFibGUgLyB0b3RhbCkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTGltaXRhdGlvbnMgYW5kIHRoZSBQYXRoIHRvIFJlc05ldCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQm90aCBBbGV4TmV0IGFuZCBWR0cgc3VmZmVyIGZyb20gdmFuaXNoaW5nIGdyYWRpZW50cyB3aGVuIGRlcHRoIGluY3JlYXNlcyBiZXlvbmQgfjIwIGxheWVycy4gU2ltcGx5IHN0YWNraW5nIG1vcmUgbGF5ZXJzIGRlZ3JhZGVzIHRyYWluaW5nIGFjY3VyYWN5IOKAlCBub3QgdGVzdCBhY2N1cmFjeSwgaW5kaWNhdGluZyBhbiBvcHRpbWlzYXRpb24gcHJvYmxlbSByYXRoZXIgdGhhbiBvdmVyZml0dGluZy4gVkdHMTkgYWxyZWFkeSBzaG93cyBkaW1pbmlzaGluZyByZXR1cm5zIG92ZXIgVkdHMTYuIFRoaXMgZGVncmFkYXRpb24gcHJvYmxlbSBsZWQgSGUgZXQgYWwuIHRvIGh5cG90aGVzaXNlIHRoYXQgbGVhcm5pbmcgaWRlbnRpdHkgbWFwcGluZ3MgaXMgaGFyZCwgYW5kIHRvIGludHJvZHVjZSBleHBsaWNpdCBzaG9ydGN1dCBjb25uZWN0aW9ucyAocmVzaWR1YWxzKSBpbiBSZXNOZXQgKDIwMTUpLiBSZXNOZXQtMTUyIG91dHBlcmZvcm1zIFZHRzE2IHdpdGggMjVNIHZzIDEzOE0gcGFyYW1ldGVycyBhbmQgZW5hYmxlcyBuZXR3b3JrcyBodW5kcmVkcyBvZiBsYXllcnMgZGVlcC4gTFJOICh1c2VkIGluIEFsZXhOZXQpIHdhcyBzaG93biB0byBwcm92aWRlIG5lZ2xpZ2libGUgYmVuZWZpdCBieSBWR0cgYW5kIHdhcyBkcm9wcGVkLiBCYXRjaCBub3JtYWxpc2F0aW9uIChJb2ZmZSBcdTAwMjYgU3plZ2VkeSwgMjAxNSkgc3VwZXJzZWRlZCBpdCBhcyB0aGUgc3RhbmRhcmQgbm9ybWFsaXNhdGlvbiB0ZWNobmlxdWUuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXJjaGl0ZWN0dXJlIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTW9kZWwiLCJZZWFyIiwiRGVwdGgiLCJQYXJhbXMiLCJHRkxPUHMiLCJLZXkgSW5ub3ZhdGlvbiIsIlRvcC01IEVycm9yIl0sInJvd3MiOltbIkFsZXhOZXQiLCIyMDEyIiwiOCIsIjYwTSIsIjAuNyIsIlJlTFUgKyBkcm9wb3V0ICsgR1BVIiwiMTUuMyUiXSxbIlZHRy0xNiIsIjIwMTQiLCIxNiIsIjEzOE0iLCIxNS41IiwiVW5pZm9ybSAzw5czIGNvbnYgc3RhY2tpbmciLCI3LjMlIl0sWyJWR0ctMTkiLCIyMDE0IiwiMTkiLCIxNDRNIiwiMTkuNiIsIkRlZXBlciB1bmlmb3JtIDPDlzMgc3RhY2tzIiwiNy4xJSJdLFsiR29vZ0xlTmV0IiwiMjAxNCIsIjIyIiwiNU0iLCIxLjUiLCJJbmNlcHRpb24gcGFyYWxsZWwgYnJhbmNoZXMiLCI2LjclIl0sWyJSZXNOZXQtNTAiLCIyMDE1IiwiNTAiLCIyNU0iLCI0LjEiLCJSZXNpZHVhbCBza2lwIGNvbm5lY3Rpb25zIiwiNS4zJSJdXX0seyJ0eXBlIjoiZGl2aWRlciJ9XQ=="
---
# AlexNet and VGG — Early Deep CNN Architectures

Before 2012 the dominant computer vision approach was hand-crafted features (SIFT, HOG) combined with shallow classifiers. AlexNet (Krizhevsky, Sutskever, Hinton, 2012) shattered this paradigm by winning ImageNet LSVRC with a 10.9-point top-5 error improvement over the runner-up. It demonstrated that deep CNNs trained on GPUs with large datasets could learn far more powerful representations than any hand-engineered alternative. VGG (Simonyan & Zisserman, 2014) then showed that architectural simplicity — stacking many 3×3 convolutions — could push accuracy further while providing clean, reusable feature extractors.

## AlexNet Architecture

AlexNet consists of five convolutional layers followed by three fully-connected layers. The first conv layer uses 96 11×11 filters with stride 4 (large stride to quickly reduce the 224×224 input). Subsequent conv layers use 3×3 and 5×5 kernels. Max pooling follows layers 1, 2, and 5 to reduce spatial dimensions. Local Response Normalisation (LRN) — a now-deprecated layer that normalises across adjacent feature maps — follows layers 1 and 2. The three FC layers (4096 → 4096 → 1000) dominate the parameter count at 58M of the total 60M parameters.

```python
import torch
import torch.nn as nn

class AlexNet(nn.Module):
    '''AlexNet (Krizhevsky et al., 2012) — 5 conv + 3 FC layers.'''
    def __init__(self, num_classes=1000, dropout=0.5):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 96, 11, stride=4, padding=2), nn.ReLU(inplace=True),
            nn.LocalResponseNorm(5, alpha=1e-4, beta=0.75, k=2.0),
            nn.MaxPool2d(3, stride=2),
            nn.Conv2d(96, 256, 5, padding=2), nn.ReLU(inplace=True),
            nn.LocalResponseNorm(5, alpha=1e-4, beta=0.75, k=2.0),
            nn.MaxPool2d(3, stride=2),
            nn.Conv2d(256, 384, 3, padding=1), nn.ReLU(inplace=True),
            nn.Conv2d(384, 384, 3, padding=1), nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, 3, padding=1), nn.ReLU(inplace=True),
            nn.MaxPool2d(3, stride=2))
        self.classifier = nn.Sequential(
            nn.Dropout(dropout), nn.Linear(256 * 6 * 6, 4096), nn.ReLU(inplace=True),
            nn.Dropout(dropout), nn.Linear(4096, 4096), nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes))

    def forward(self, x):
        return self.classifier(self.features(x).flatten(1))

model = AlexNet()
x = torch.randn(2, 3, 224, 224)
params = sum(p.numel() for p in model.parameters()) / 1e6
print('AlexNet output: {}'.format(model(x).shape))
print('Parameters: {:.1f}M (58M in FC layers alone)'.format(params))
```

## Training Innovations in AlexNet

AlexNet introduced several training techniques that became standard: ReLU activations (instead of tanh or sigmoid) train 6× faster because they do not suffer from the vanishing gradient in the saturation region; dropout (p=0.5) in the two FC layers reduces co-adaptation of neurons and halves test error relative to no regularisation; data augmentation (random 224×224 crops and horizontal flips from 256×256 images, PCA colour jitter) effectively quintuples the training set. Training on two GTX 580 GPUs for six days was essential — the model split across GPUs, with cross-GPU communication only at specific layers.

- ReLU: f(x)=max(0,x) — no saturation for x>0, gradient always 1 or 0, trains ~6x faster than sigmoid/tanh.
- Dropout (p=0.5): applied to FC6 and FC7, forces neurons to learn redundant representations, acts as implicit ensemble of 2^n networks.
- LRN: lateral inhibition across adjacent feature maps — normalises response relative to neighbours, mimics biological lateral inhibition. Dropped in later architectures.
- Data augmentation: 224×224 crops from padded 256×256, horizontal flips, PCA colour jitter — critical for preventing overfitting with 60M parameters.
- GPU training: split architecture across 2 GPUs, cross-GPU communication only at layers 3 and FC layers.
- Weight initialisation: Gaussian(0, 0.01) for weights, constant 0 or 1 for biases (layer-dependent).

## VGG: Depth Through Small Kernels

VGG (Simonyan & Zisserman, 2014) makes one design choice and pursues it relentlessly: use only 3×3 convolutions with stride 1 and padding 1. Two stacked 3×3 convs have the same receptive field as one 5×5 conv but use 2×(3×3×C²) = 18C² parameters instead of 25C². Three stacked 3×3 convs match a 7×7 conv: 27C² vs 49C² params — a 44% saving — plus two extra ReLU nonlinearities which increase expressiveness. VGG is organised into five blocks with progressively doubling channels (64, 128, 256, 512, 512), each ending with a 2×2 max pool. VGG16 has 16 weight layers; VGG19 has 19.

```python
import torch
import torch.nn as nn
from typing import List

def vgg_block(in_ch: int, out_ch: int, n_convs: int) -> nn.Sequential:
    '''VGG block: n_convs x (Conv 3x3 + BN + ReLU), then MaxPool 2x2.'''
    layers: List[nn.Module] = []
    for _ in range(n_convs):
        layers += [nn.Conv2d(in_ch, out_ch, 3, padding=1, bias=False),
                   nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True)]
        in_ch = out_ch
    layers.append(nn.MaxPool2d(2, stride=2))
    return nn.Sequential(*layers)

class VGG16(nn.Module):
    '''VGG-16 with batch normalisation (Simonyan & Zisserman, 2014).'''
    def __init__(self, num_classes=1000):
        super().__init__()
        self.features = nn.Sequential(
            vgg_block(3, 64, 2),    # 224 -> 112
            vgg_block(64, 128, 2),  # 112 -> 56
            vgg_block(128, 256, 3), # 56  -> 28
            vgg_block(256, 512, 3), # 28  -> 14
            vgg_block(512, 512, 3)) # 14  -> 7
        self.head = nn.Sequential(
            nn.Flatten(),
            nn.Linear(512 * 7 * 7, 4096), nn.ReLU(inplace=True), nn.Dropout(0.5),
            nn.Linear(4096, 4096),        nn.ReLU(inplace=True), nn.Dropout(0.5),
            nn.Linear(4096, num_classes))

    def forward(self, x): return self.head(self.features(x))

model = VGG16()
x = torch.randn(1, 3, 224, 224)
params = sum(p.numel() for p in model.parameters()) / 1e6
print('VGG-16 output: {}'.format(model(x).shape))
print('Parameters: {:.1f}M'.format(params))
```

## Receptive Field and Parameter Analysis

The effective receptive field of stacked 3×3 convs grows linearly: one 3×3 gives RF=3; two give RF=5 (matching one 5×5); three give RF=7 (matching one 7×7). The parameter savings are significant: two 3×3 convs on C channels cost 2×9C² = 18C² parameters while a single 5×5 costs 25C² (28% more). Three 3×3 convs cost 27C² versus 49C² for a 7×7 (44% more). Additionally, each extra conv layer adds a ReLU nonlinearity, which increases the function class's expressiveness without extra spatial overhead.

```python
import torch
import torch.nn as nn

def count_params(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def rf_of_stacked_3x3(n):
    '''Effective receptive field of n stacked 3x3 convs.'''
    return 1 + 2 * n

# Parameter comparison: stacked 3x3 vs equivalent large kernel
C = 256
configs = [
    ('one 5x5', nn.Conv2d(C, C, 5, padding=2)),
    ('two 3x3', nn.Sequential(nn.Conv2d(C, C, 3, padding=1), nn.Conv2d(C, C, 3, padding=1))),
    ('one 7x7', nn.Conv2d(C, C, 7, padding=3)),
    ('three 3x3', nn.Sequential(
        nn.Conv2d(C, C, 3, padding=1), nn.Conv2d(C, C, 3, padding=1),
        nn.Conv2d(C, C, 3, padding=1)))
]
print('{:<14} {:>12} {:>8} {:>12}'.format('Config', 'Params', 'RF', 'Savings'))
ref5 = count_params(configs[0][1])
ref7 = count_params(configs[2][1])
for name, module in configs:
    p = count_params(module)
    rf = rf_of_stacked_3x3(2 if '3x3' in name and 'two' in name
                           else 3 if 'three' in name else 1)
    ref = ref5 if '5x5' in name or 'two' in name else ref7
    save = '---' if name in ('one 5x5', 'one 7x7') else '-{:.0f}%'.format(100*(1 - p/ref))
    print('{:<14} {:>12,} {:>8} {:>12}'.format(name, p, rf, save))
```

> **VGG's FC Layer Bottleneck**: VGG16 has 138M parameters — but 123M (89%) live in the three FC layers (512×7×7→4096, 4096→4096, 4096→1000). The conv layers that do all the spatial feature extraction account for only 15M parameters. Modern architectures replace FC layers with global average pooling (GAP), eliminating this bottleneck: ResNet-50 has only 25M parameters and GoogLeNet has 5M — both more accurate than VGG.

## VGG as Feature Extractor

Despite being surpassed on ImageNet accuracy, VGG's feature representations remain powerful for transfer learning, perceptual loss in style transfer (Gatys et al., 2015), and as a backbone for downstream tasks. The uniform 3×3 conv structure makes it easy to extract features at any depth. Common extraction points: relu3_3 (256 channels, 28×28 for 224×224 input) for texture-rich features; relu4_3 (512 channels, 14×14) for semantic object features; relu5_3 (512 channels, 7×7) for the most abstract features.

```python
import torch
import torch.nn as nn
from torchvision import models

class VGGFeatureExtractor(nn.Module):
    '''VGG-16 pretrained backbone with a lightweight classification head.'''
    def __init__(self, num_classes=10, feature_layer=30, freeze=True):
        super().__init__()
        vgg = models.vgg16_bn(weights=models.VGG16_BN_Weights.IMAGENET1K_V1)
        self.backbone = nn.Sequential(*list(vgg.features.children())[:feature_layer])
        if freeze:
            for param in self.backbone.parameters():
                param.requires_grad = False
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d((4, 4)), nn.Flatten(),
            nn.Linear(512 * 16, 512), nn.ReLU(inplace=True),
            nn.Dropout(0.5), nn.Linear(512, num_classes))

    def forward(self, x):
        return self.head(self.backbone(x))

model = VGGFeatureExtractor(num_classes=10, freeze=True)
total = sum(p.numel() for p in model.parameters())
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
x = torch.randn(4, 3, 224, 224)
out = model(x)
print('Output: {}'.format(out.shape))
print('Trainable: {:,} / Total: {:,} ({:.1f}%)'.format(
    trainable, total, 100 * trainable / total))
```

## Limitations and the Path to ResNet

Both AlexNet and VGG suffer from vanishing gradients when depth increases beyond ~20 layers. Simply stacking more layers degrades training accuracy — not test accuracy, indicating an optimisation problem rather than overfitting. VGG19 already shows diminishing returns over VGG16. This degradation problem led He et al. to hypothesise that learning identity mappings is hard, and to introduce explicit shortcut connections (residuals) in ResNet (2015). ResNet-152 outperforms VGG16 with 25M vs 138M parameters and enables networks hundreds of layers deep. LRN (used in AlexNet) was shown to provide negligible benefit by VGG and was dropped. Batch normalisation (Ioffe & Szegedy, 2015) superseded it as the standard normalisation technique.

## Architecture Comparison

| Model | Year | Depth | Params | GFLOPs | Key Innovation | Top-5 Error |
| --- | --- | --- | --- | --- | --- | --- |
| AlexNet | 2012 | 8 | 60M | 0.7 | ReLU + dropout + GPU | 15.3% |
| VGG-16 | 2014 | 16 | 138M | 15.5 | Uniform 3×3 conv stacking | 7.3% |
| VGG-19 | 2014 | 19 | 144M | 19.6 | Deeper uniform 3×3 stacks | 7.1% |
| GoogLeNet | 2014 | 22 | 5M | 1.5 | Inception parallel branches | 6.7% |
| ResNet-50 | 2015 | 50 | 25M | 4.1 | Residual skip connections | 5.3% |

---

