---
title: "MAE: Masked Autoencoders for Visual Pretraining"
slug: "mae-masked-image-modeling"
description: "Masked Autoencoders use a high masking ratio (75%) to pretrain ViT — encoder processes visible patches only, lightweight decoder reconstructs masked pixels, producing strong transfer features."
tags: ["computer-vision"]
topic: "computer-vision"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6Ik92ZXJ2aWV3In0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNYXNrZWQgQXV0b2VuY29kZXJzIChNQUUpIGFkYXB0IHRoZSBtYXNrZWQgbGFuZ3VhZ2UgbW9kZWxpbmcgcGFyYWRpZ20gKEJFUlQpIHRvIHZpc2lvbi4gQSByYW5kb20gNzUlIG9mIGltYWdlIHBhdGNoZXMgYXJlIG1hc2tlZDsgdGhlIGVuY29kZXIgcHJvY2Vzc2VzIG9ubHkgdGhlIHZpc2libGUgMjUlLCBhbmQgYSBsaWdodHdlaWdodCBkZWNvZGVyIHJlY29uc3RydWN0cyB0aGUgb3JpZ2luYWwgcGl4ZWwgdmFsdWVzIGZvciBhbGwgbWFza2VkIHBhdGNoZXMuIFRoaXMgYXN5bW1ldHJpYyBkZXNpZ24gbWFrZXMgcHJldHJhaW5pbmcgZWZmaWNpZW50IGFuZCBmb3JjZXMgdGhlIGVuY29kZXIgdG8gbGVhcm4gaG9saXN0aWMgc2NlbmUgdW5kZXJzdGFuZGluZy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6Ik1BRSBhY2hpZXZlcyA4Ny44JSB0b3AtMSBhY2N1cmFjeSBvbiBJbWFnZU5ldCB3aXRoIFZpVC1IIGFmdGVyIGZpbmUtdHVuaW5nIOKAlCBtYXRjaGluZyBvciBleGNlZWRpbmcgc3VwZXJ2aXNlZCBwcmV0cmFpbmluZy4gVW5saWtlIGNvbnRyYXN0aXZlIG1ldGhvZHMsIE1BRSByZXF1aXJlcyBubyBuZWdhdGl2ZSBwYWlycywgbm8gbW9tZW50dW0gZW5jb2RlciwgYW5kIG5vIHNwZWNpYWxpemVkIGF1Z21lbnRhdGlvbnMuIFRoZSByZWNvbnN0cnVjdGlvbiB0YXJnZXQgaXMgcmF3IG5vcm1hbGl6ZWQgcGl4ZWwgdmFsdWVzLCBrZWVwaW5nIHRoZSBpbXBsZW1lbnRhdGlvbiBzaW1wbGUgd2hpbGUgcHJvZHVjaW5nIHN0cm9uZyByZXByZXNlbnRhdGlvbnMuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXN5bW1ldHJpYyBFbmNvZGVyLURlY29kZXIifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBlbmNvZGVyIGlzIGEgc3RhbmRhcmQgVmlUIGFwcGxpZWQgb25seSB0byB2aXNpYmxlICh1bm1hc2tlZCkgcGF0Y2hlcy4gVGhpcyBtZWFucyB0aGUgZW5jb2RlciBwcm9jZXNzZXMganVzdCAyNSUgb2YgdGhlIHRvdGFsIHBhdGNoZXMsIHJlZHVjaW5nIGNvbXB1dGF0aW9uIGJ5IH40w5cuIE1hc2sgdG9rZW5zIGFyZSBuZXZlciBpbnRyb2R1Y2VkIGluIHRoZSBlbmNvZGVyLCBwcmV2ZW50aW5nIHRoZSBtb2RlbCBmcm9tIGV4cGxvaXRpbmcgdGhlaXIgcG9zaXRpb25hbCBpbmZvcm1hdGlvbi4gT25seSBpbiB0aGUgbGlnaHR3ZWlnaHQgZGVjb2RlciBhcmUgbWFzayB0b2tlbnMgYWRkZWQgYmFjaywgYWxvbmcgd2l0aCBwb3NpdGlvbmFsIGVtYmVkZGluZ3MsIHRvIHJlY29uc3RydWN0IHRoZSBmdWxsIGltYWdlLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcblxuZGVmIHJhbmRvbV9tYXNraW5nKHgsIG1hc2tfcmF0aW89MC43NSk6XG4gICAgIyB4OiBbQiwgTiwgRF0gcGF0Y2ggZW1iZWRkaW5nc1xuICAgIEIsIE4sIEQgPSB4LnNoYXBlXG4gICAgbnVtX2tlZXAgPSBpbnQoTiAqICgxIC0gbWFza19yYXRpbykpXG4gICAgbm9pc2UgPSB0b3JjaC5yYW5kKEIsIE4sIGRldmljZT14LmRldmljZSlcbiAgICBpZHNfc2h1ZmZsZSA9IHRvcmNoLmFyZ3NvcnQobm9pc2UsIGRpbT0xKVxuICAgIGlkc19yZXN0b3JlID0gdG9yY2guYXJnc29ydChpZHNfc2h1ZmZsZSwgZGltPTEpXG4gICAgaWRzX2tlZXAgPSBpZHNfc2h1ZmZsZVs6LCA6bnVtX2tlZXBdXG4gICAgeF9tYXNrZWQgPSB0b3JjaC5nYXRoZXIoeCwgMSwgaWRzX2tlZXAudW5zcXVlZXplKC0xKS5leHBhbmQoLTEsIC0xLCBEKSlcbiAgICBtYXNrID0gdG9yY2gub25lcyhCLCBOLCBkZXZpY2U9eC5kZXZpY2UpXG4gICAgbWFza1s6LCA6bnVtX2tlZXBdID0gMFxuICAgIG1hc2sgPSB0b3JjaC5nYXRoZXIobWFzaywgMSwgaWRzX3Jlc3RvcmUpXG4gICAgcmV0dXJuIHhfbWFza2VkLCBtYXNrLCBpZHNfcmVzdG9yZSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkhpZ2ggTWFza2luZyBSYXRpbyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIDc1JSBtYXNraW5nIHJhdGlvIGlzIGEgZGVsaWJlcmF0ZSBkZXNpZ24gY2hvaWNlLCBub3QganVzdCBhIGh5cGVycGFyYW1ldGVyLiBBdCBsb3cgcmF0aW9zIChlLmcuLCAxNSUgYXMgaW4gQkVSVCksIG5laWdoYm9yaW5nIHZpc2libGUgcGF0Y2hlcyBsZWFrIGVub3VnaCBpbmZvcm1hdGlvbiB0byByZWNvbnN0cnVjdCBtYXNrZWQgcGF0Y2hlcyB0aHJvdWdoIGxvY2FsIGludGVycG9sYXRpb24uIEF0IDc1JSwgdGhlIHRhc2sgcmVxdWlyZXMgdW5kZXJzdGFuZGluZyBnbG9iYWwgc3RydWN0dXJlLCBvYmplY3Qgc2VtYW50aWNzLCBhbmQgc3BhdGlhbCByZWxhdGlvbnNoaXBzIOKAlCBmb3JjaW5nIHRoZSBlbmNvZGVyIHRvIGJ1aWxkIHJpY2gsIGhvbGlzdGljIHJlcHJlc2VudGF0aW9ucy4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cblxuY2xhc3MgTUFFRW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB2aXRfYmFja2JvbmUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi52aXQgPSB2aXRfYmFja2JvbmVcbiAgICAgICAgc2VsZi5wYXRjaF9lbWJlZCA9IHZpdF9iYWNrYm9uZS5wYXRjaF9lbWJlZFxuICAgICAgICBzZWxmLmNsc190b2tlbiA9IHZpdF9iYWNrYm9uZS5jbHNfdG9rZW5cbiAgICAgICAgc2VsZi5wb3NfZW1iZWQgPSB2aXRfYmFja2JvbmUucG9zX2VtYmVkXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBpZHNfa2VlcCk6XG4gICAgICAgICMgZW1iZWQgcGF0Y2hlcywgbm8gbWFzayB0b2tlbnMgaW4gZW5jb2RlclxuICAgICAgICB4ID0gc2VsZi5wYXRjaF9lbWJlZCh4KSAgIyBbQiwgTiwgRF1cbiAgICAgICAgeCA9IHggKyBzZWxmLnBvc19lbWJlZFs6LCAxOiwgOl0gICMgYWRkIHBvc2l0aW9uYWwgZW1iZWRkaW5nc1xuICAgICAgICAjIHNlbGVjdCBvbmx5IHZpc2libGUgcGF0Y2hlc1xuICAgICAgICBCLCBOLCBEID0geC5zaGFwZVxuICAgICAgICB4ID0gdG9yY2guZ2F0aGVyKHgsIDEsIGlkc19rZWVwLnVuc3F1ZWV6ZSgtMSkuZXhwYW5kKC0xLCAtMSwgRCkpXG4gICAgICAgIGNscyA9IHNlbGYuY2xzX3Rva2VuICsgc2VsZi5wb3NfZW1iZWRbOiwgOjEsIDpdXG4gICAgICAgIHggPSB0b3JjaC5jYXQoW2Nscy5leHBhbmQoQiwgLTEsIC0xKSwgeF0sIGRpbT0xKVxuICAgICAgICB4ID0gc2VsZi52aXQuYmxvY2tzKHgpXG4gICAgICAgIHJldHVybiBzZWxmLnZpdC5ub3JtKHgpIn0seyJ0eXBlIjoiY2FsbG91dCIsImNhbGxvdXRfdHlwZSI6ImluZm8iLCJjb250ZW50IjoiTUFFXHUwMDI3cyBoaWdoIG1hc2tpbmcgcmF0aW8gKDc1JSkgaXMgY3JpdGljYWwg4oCUIGxvdyByYXRpb3MgbWFrZSB0aGUgdGFzayB0b28gZWFzeSAobmVpZ2hib3JzIHByb3ZpZGUgc2lnbmFsKS4gNzUlIGZvcmNlcyB0aGUgbW9kZWwgdG8gbGVhcm4gaG9saXN0aWMgc2VtYW50aWMgdW5kZXJzdGFuZGluZyByYXRoZXIgdGhhbiBsb2NhbCBpbnRlcnBvbGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByZXRyYWluaW5nIE9iamVjdGl2ZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlY29uc3RydWN0aW9uIHRhcmdldCBpcyB0aGUgbm9ybWFsaXplZCBwaXhlbCB2YWx1ZXMgd2l0aGluIGVhY2ggbWFza2VkIHBhdGNoLiBQZXItcGF0Y2ggbWVhbiBhbmQgdmFyaWFuY2UgYXJlIGNvbXB1dGVkIGFuZCB1c2VkIHRvIG5vcm1hbGl6ZSB0aGUgdGFyZ2V0LCBwcmV2ZW50aW5nIHRoZSBtb2RlbCBmcm9tIGZvY3VzaW5nIG9uIGxvdy1mcmVxdWVuY3kgY29sb3Igc3RhdGlzdGljcyByYXRoZXIgdGhhbiBzdHJ1Y3R1cmUuIFRoZSBsb3NzIGlzIE1TRSBjb21wdXRlZCBvbmx5IG9uIG1hc2tlZCBwYXRjaGVzIOKAlCB2aXNpYmxlIHBhdGNoZXMgYXJlIG5vdCBwZW5hbGl6ZWQsIGZvY3VzaW5nIG9wdGltaXphdGlvbiBlbnRpcmVseSBvbiB3aGF0IHdhcyBoaWRkZW4uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmNsYXNzIE1BRURlY29kZXIobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZW5jb2Rlcl9kaW09NzY4LCBkZWNvZGVyX2RpbT01MTIsXG4gICAgICAgICAgICAgICAgIG5fYmxvY2tzPTgsIHBhdGNoX3NpemU9MTYsIG5fY2hhbm5lbHM9Myk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnByb2ogPSBubi5MaW5lYXIoZW5jb2Rlcl9kaW0sIGRlY29kZXJfZGltKVxuICAgICAgICBzZWxmLm1hc2tfdG9rZW4gPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3MoMSwgMSwgZGVjb2Rlcl9kaW0pKVxuICAgICAgICBzZWxmLmJsb2NrcyA9IG5uLlNlcXVlbnRpYWwoKltubi5UcmFuc2Zvcm1lckVuY29kZXJMYXllcihcbiAgICAgICAgICAgIGRfbW9kZWw9ZGVjb2Rlcl9kaW0sIG5oZWFkPTE2LCBiYXRjaF9maXJzdD1UcnVlKVxuICAgICAgICAgICAgZm9yIF8gaW4gcmFuZ2Uobl9ibG9ja3MpXSlcbiAgICAgICAgc2VsZi5wcmVkID0gbm4uTGluZWFyKGRlY29kZXJfZGltLCBwYXRjaF9zaXplICogcGF0Y2hfc2l6ZSAqIG5fY2hhbm5lbHMpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4LCBpZHNfcmVzdG9yZSk6XG4gICAgICAgIHggPSBzZWxmLnByb2ooeCkgICMgcHJvamVjdCBlbmNvZGVyIHRva2Vuc1xuICAgICAgICBCLCBudW1fdmlzX3BsdXNfY2xzLCBEID0geC5zaGFwZVxuICAgICAgICBudW1fcGF0Y2hlcyA9IGlkc19yZXN0b3JlLnNoYXBlWzFdXG4gICAgICAgIG1hc2tfdG9rZW5zID0gc2VsZi5tYXNrX3Rva2VuLmV4cGFuZChCLCBudW1fcGF0Y2hlcyAtIChudW1fdmlzX3BsdXNfY2xzIC0gMSksIEQpXG4gICAgICAgIHhfID0gdG9yY2guY2F0KFt4WzosIDE6LCA6XSwgbWFza190b2tlbnNdLCBkaW09MSlcbiAgICAgICAgeF8gPSB0b3JjaC5nYXRoZXIoeF8sIDEsIGlkc19yZXN0b3JlLnVuc3F1ZWV6ZSgtMSkuZXhwYW5kKC0xLCAtMSwgRCkpXG4gICAgICAgIHggPSB0b3JjaC5jYXQoW3hbOiwgOjEsIDpdLCB4X10sIGRpbT0xKVxuICAgICAgICB4ID0gc2VsZi5ibG9ja3MoeClcbiAgICAgICAgcmV0dXJuIHNlbGYucHJlZCh4WzosIDE6LCA6XSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJNQUUgdnMgQ29udHJhc3RpdmUgTWV0aG9kcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuZnJvbSB0aW1tLm1vZGVscy52aXNpb25fdHJhbnNmb3JtZXIgaW1wb3J0IFZpc2lvblRyYW5zZm9ybWVyXG5cbmRlZiBidWlsZF9tYWVfZmluZXR1bmluZ19tb2RlbChlbmNvZGVyLCBudW1fY2xhc3Nlcz0xMDAwKTpcbiAgICAjIGRpc2NhcmQgZGVjb2RlcjsgYXR0YWNoIGNsYXNzaWZpY2F0aW9uIGhlYWQgdG8gZW5jb2RlclxuICAgIGNsYXNzIE1BRUZpbmVUdW5lcihubi5Nb2R1bGUpOlxuICAgICAgICBkZWYgX19pbml0X18oc2VsZiwgZW5jLCBuX2Nscyk6XG4gICAgICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgICAgIHNlbGYuZW5jb2RlciA9IGVuY1xuICAgICAgICAgICAgZGltID0gZW5jLmVtYmVkX2RpbVxuICAgICAgICAgICAgc2VsZi5oZWFkID0gbm4uTGluZWFyKGRpbSwgbl9jbHMpXG4gICAgICAgICAgICBubi5pbml0LnRydW5jX25vcm1hbF8oc2VsZi5oZWFkLndlaWdodCwgc3RkPTAuMDEpXG4gICAgICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOlxuICAgICAgICAgICAgIyB1c2UgQ0xTIHRva2VuIGZvciBjbGFzc2lmaWNhdGlvblxuICAgICAgICAgICAgeCA9IHNlbGYuZW5jb2Rlcih4KVs6LCAwXVxuICAgICAgICAgICAgcmV0dXJuIHNlbGYuaGVhZCh4KVxuICAgIHJldHVybiBNQUVGaW5lVHVuZXIoZW5jb2RlciwgbnVtX2NsYXNzZXMpIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNQUUgYW5kIGNvbnRyYXN0aXZlIG1ldGhvZHMgKERJTk8sIENMSVAsIFNpbUNMUikgbGVhcm4gY29tcGxlbWVudGFyeSByZXByZXNlbnRhdGlvbnMuIENvbnRyYXN0aXZlIG1ldGhvZHMgcHJvZHVjZSBmZWF0dXJlcyB0aGF0IGV4Y2VsIGF0IGxpbmVhciBwcm9iaW5nIGFuZCBrLU5OIHRhc2tzIGJlY2F1c2UgdGhlIGNvbnRyYXN0aXZlIG9iamVjdGl2ZSBkaXJlY3RseSBzdHJ1Y3R1cmVzIHRoZSBlbWJlZGRpbmcgc3BhY2UgZm9yIHNpbWlsYXJpdHkgY29tcGFyaXNvbnMuIE1BRSBmZWF0dXJlcyBvZnRlbiByZXF1aXJlIGZpbmUtdHVuaW5nIHRvIHJlYWNoIHBlYWsgcGVyZm9ybWFuY2UgYnV0IHRoZW4gc3VycGFzcyBjb250cmFzdGl2ZSBiYXNlbGluZXMgb24gdGFza3MgbGlrZSBkZXRlY3Rpb24gYW5kIHNlZ21lbnRhdGlvbi4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiTG9zcyIsIk1hc2tpbmciLCJMaW5lYXIgQWNjICglKSIsIkZpbmUtdHVuZSBBY2MgKCUpIiwiVGhyb3VnaHB1dCJdLCJyb3dzIjpbWyJNQUUtQiIsIk1TRSAocGl4ZWxzKSIsIjc1JSIsIjY4LjAiLCI4My42IiwiRmFzdCJdLFsiTUFFLUwiLCJNU0UgKHBpeGVscykiLCI3NSUiLCI3Ni4wIiwiODUuOSIsIk1lZGl1bSJdLFsiTUFFLUgiLCJNU0UgKHBpeGVscykiLCI3NSUiLCI3Ny4yIiwiODcuOCIsIlNsb3ciXSxbIkJFaVQiLCJDcm9zcy1lbnRyb3B5ICh0b2tlbnMpIiwiNDAlIiwiNTYuNyIsIjgzLjIiLCJNZWRpdW0iXSxbIlNpbU1JTSIsIk1TRSAocGl4ZWxzKSIsIjYwJSIsIjY1LjciLCI4My44IiwiTWVkaXVtIl0sWyJESU5PLUIiLCJDcm9zcy1lbnRyb3B5IiwiTm9uZSIsIjgwLjEiLCI4Mi44IiwiRmFzdCJdXX0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiS2V5IFRha2Vhd2F5cyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTUFFIGRlbW9uc3RyYXRlcyB0aGF0IGdlbmVyYXRpdmUgcHJldHJhaW5pbmcg4oCUIHJlY29uc3RydWN0aW5nIG1hc2tlZCBpbnB1dCDigJQgaXMgYSBwb3dlcmZ1bCBhbmQgc2NhbGFibGUgc2VsZi1zdXBlcnZpc2VkIGxlYXJuaW5nIHBhcmFkaWdtIGZvciB2aXNpb24uIFRoZSBhc3ltbWV0cmljIGVuY29kZXItZGVjb2RlciBkZXNpZ24gc2ltdWx0YW5lb3VzbHkgaW1wcm92ZXMgY29tcHV0ZSBlZmZpY2llbmN5IGFuZCByZXByZXNlbnRhdGlvbiBxdWFsaXR5LiBNQUUgc2NhbGVzIGdyYWNlZnVsbHk6IFZpVC1IIHdpdGggTUFFIHByZXRyYWluaW5nIG1hdGNoZXMgb3IgZXhjZWVkcyBhbGwgcHJpb3Igc2VsZi1zdXBlcnZpc2VkIG1ldGhvZHMgb24gc3RhbmRhcmQgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByYWN0aWNhbCBhZHZhbnRhZ2VzIG92ZXIgY29udHJhc3RpdmUgbWV0aG9kczogbm8gbmVlZCBmb3IgbmVnYXRpdmUgcGFpcnMgb3IgbGFyZ2UgYmF0Y2hlcywgbm8gc3BlY2lhbGl6ZWQgYXVnbWVudGF0aW9uIHBpcGVsaW5lcyAocmFuZG9tIGNyb3AgKyBob3Jpem9udGFsIGZsaXAgc3VmZmljZSksIG5vIG1vbWVudHVtIGVuY29kZXIsIGFuZCBsb3dlciBtZW1vcnkgdXNhZ2UgZHVyaW5nIHByZXRyYWluaW5nLiBUaGUgcmVjb25zdHJ1Y3Rpb24gb2JqZWN0aXZlIGlzIGludmFyaWFudCB0byB0aGUgbnVtYmVyIG9mIGNhdGVnb3JpZXMsIG1ha2luZyBNQUUgbmF0dXJhbGx5IHN1aXRhYmxlIGZvciBkb21haW4tc3BlY2lmaWMgcHJldHJhaW5pbmcgb3V0c2lkZSBJbWFnZU5ldC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRvd25zdHJlYW0gdXNhZ2U6IGRpc2NhcmQgdGhlIGRlY29kZXIgYWZ0ZXIgcHJldHJhaW5pbmcgYW5kIGZpbmUtdHVuZSBvbmx5IHRoZSBlbmNvZGVyIHdpdGggYSB0YXNrIGhlYWQuIEZvciBkZXRlY3Rpb24gKFZpVERldCksIE1BRS1wcmV0cmFpbmVkIFZpVC1IIGFjaGlldmVzIDYxLjMgQVAgb24gQ09DTy4gRm9yIHNlZ21lbnRhdGlvbiAoVVBlck5ldCksIGl0IGFjaGlldmVzIDUzLjYgbUlvVSBvbiBBREUyMGsuIFRoZXNlIHJlc3VsdHMgZXN0YWJsaXNoIE1BRSBhcyB0aGUgZGUgZmFjdG8gcHJldHJhaW5pbmcgbWV0aG9kIGZvciBsYXJnZSBWaVQgbW9kZWxzIGluIGRlbnNlIHByZWRpY3Rpb24gdGFza3MuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJFeHRlbnNpb25zIGFuZCB2YXJpYW50czogVmlkZW9NQUUgYXBwbGllcyB0aGUgc2FtZSBwYXJhZGlnbSB0byB2aWRlbyB3aXRoIHR1YmUgbWFza2luZzsgQXVkaW8tTUFFIHRvIHNwZWN0cm9ncmFtczsgUG9pbnQtTUFFIHRvIDNEIHBvaW50IGNsb3Vkcy4gaUJPVCBjb21iaW5lcyBNQUUtc3R5bGUgcGF0Y2ggdG9rZW4gcHJlZGljdGlvbiB3aXRoIERJTk9cdTAwMjdzIGdsb2JhbCBDTFMgZGlzdGlsbGF0aW9uIGZvciBhIGh5YnJpZCBvYmplY3RpdmUgdGhhdCBhY2hpZXZlcyBzdHJvbmcgcGVyZm9ybWFuY2Ugb24gYm90aCBsaW5lYXIgcHJvYmluZyBhbmQgZmluZS10dW5pbmcgYmVuY2htYXJrcyB3aXRob3V0IHNhY3JpZmljaW5nIGVpdGhlciBzdHJlbmd0aC4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkNvbW1vbiBpbXBsZW1lbnRhdGlvbiBwaXRmYWxsczogbm90IG5vcm1hbGl6aW5nIHBpeGVsIHRhcmdldHMgcGVyLXBhdGNoIChtb2RlbCBsZWFybnMgY29sb3Igc3RhdGlzdGljcyBpbnN0ZWFkIG9mIHN0cnVjdHVyZSksIHVzaW5nIHRvbyBzbWFsbCBhIGRlY29kZXIgKDQgYmxvY2tzLCAyNTYtZGltKSwgaW5jbHVkaW5nIG1hc2sgdG9rZW5zIGluIHRoZSBlbmNvZGVyIChsZWFrcyBwb3NpdGlvbmFsIGluZm9ybWF0aW9uIGFib3V0IG1hc2tlZCBsb2NhdGlvbnMpLCBhbmQgdXNpbmcgY29zaW5lIHNpbWlsYXJpdHkgbG9zcyBpbnN0ZWFkIG9mIE1TRSAobGVzcyBzdGFibGUsIG5vIGNsZWFyIGJlbmVmaXQpLiBVc2UgdGhlIGV4YWN0IGRlY29kZXIgYXJjaGl0ZWN0dXJlIGZyb20gdGhlIG9yaWdpbmFsIHBhcGVyIGFzIGEgc3RhcnRpbmcgcG9pbnQuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJTY2FsaW5nIGJlaGF2aW9yOiBNQUUgc2hvd3Mgc3Ryb25nIHNjYWxpbmcgd2l0aCBib3RoIG1vZGVsIHNpemUgYW5kIHByZXRyYWluaW5nIGR1cmF0aW9uLiBWaVQtSCBwcmV0cmFpbmVkIGZvciAxNjAwIGVwb2NocyBjb25zaXN0ZW50bHkgb3V0cGVyZm9ybXMgc2hvcnRlciBzY2hlZHVsZXMuIFVubGlrZSBzdXBlcnZpc2VkIHRyYWluaW5nLCB0aGVyZSBpcyBubyBjbGVhciBzaWduIG9mIG92ZXJmaXR0aW5nIHdpdGggbG9uZ2VyIHByZXRyYWluaW5nIG9uIEltYWdlTmV0LTFrIOKAlCBNQUUgYmVuZWZpdHMgZnJvbSB0aGUgaW5jcmVhc2VkIG51bWJlciBvZiBtYXNrZWQgcGF0Y2ggcmVjb25zdHJ1Y3Rpb24gcHJvYmxlbXMgc2VlbiBkdXJpbmcgdHJhaW5pbmcuIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJSZWNvbW1lbmRlZCBjb25maWd1cmF0aW9uIGZvciBwcmFjdGl0aW9uZXJzOiBWaVQtTC8xNiB3aXRoIE1BRSBwcmV0cmFpbmluZyBmb3IgNDAwIGVwb2NocyBvbiBhIGRvbWFpbi1zcGVjaWZpYyBkYXRhc2V0IHByb3ZpZGVzIHN0cm9uZyBpbml0aWFsaXphdGlvbiBmb3IgZmluZS10dW5pbmcgb24gZG93bnN0cmVhbSB0YXNrcy4gVGhlIG9yaWdpbmFsIEZBSVIgaW1wbGVtZW50YXRpb24gKGdpdGh1Yi5jb20vZmFjZWJvb2tyZXNlYXJjaC9tYWUpIGlzIGNsZWFuIGFuZCB3ZWxsLWRvY3VtZW50ZWQuIEh1Z2dpbmdGYWNlIFRyYW5zZm9ybWVycyBpbmNsdWRlcyBWaVRNQUVNb2RlbCB3aXRoIHByZXRyYWluZWQgd2VpZ2h0cyBmb3IgYm90aCBWaVQtQiBhbmQgVmlULUwgdmFyaWFudHMuIn1d"
---
# MAE: Masked Autoencoders for Visual Pretraining

## Overview

Masked Autoencoders (MAE) adapt the masked language modeling paradigm (BERT) to vision. A random 75% of image patches are masked; the encoder processes only the visible 25%, and a lightweight decoder reconstructs the original pixel values for all masked patches. This asymmetric design makes pretraining efficient and forces the encoder to learn holistic scene understanding.

MAE achieves 87.8% top-1 accuracy on ImageNet with ViT-H after fine-tuning — matching or exceeding supervised pretraining. Unlike contrastive methods, MAE requires no negative pairs, no momentum encoder, and no specialized augmentations. The reconstruction target is raw normalized pixel values, keeping the implementation simple while producing strong representations.

## Asymmetric Encoder-Decoder

The encoder is a standard ViT applied only to visible (unmasked) patches. This means the encoder processes just 25% of the total patches, reducing computation by ~4×. Mask tokens are never introduced in the encoder, preventing the model from exploiting their positional information. Only in the lightweight decoder are mask tokens added back, along with positional embeddings, to reconstruct the full image.

```python
import torch

def random_masking(x, mask_ratio=0.75):
    # x: [B, N, D] patch embeddings
    B, N, D = x.shape
    num_keep = int(N * (1 - mask_ratio))
    noise = torch.rand(B, N, device=x.device)
    ids_shuffle = torch.argsort(noise, dim=1)
    ids_restore = torch.argsort(ids_shuffle, dim=1)
    ids_keep = ids_shuffle[:, :num_keep]
    x_masked = torch.gather(x, 1, ids_keep.unsqueeze(-1).expand(-1, -1, D))
    mask = torch.ones(B, N, device=x.device)
    mask[:, :num_keep] = 0
    mask = torch.gather(mask, 1, ids_restore)
    return x_masked, mask, ids_restore
```

## High Masking Ratio

The 75% masking ratio is a deliberate design choice, not just a hyperparameter. At low ratios (e.g., 15% as in BERT), neighboring visible patches leak enough information to reconstruct masked patches through local interpolation. At 75%, the task requires understanding global structure, object semantics, and spatial relationships — forcing the encoder to build rich, holistic representations.

```python
import torch
import torch.nn as nn

class MAEEncoder(nn.Module):
    def __init__(self, vit_backbone):
        super().__init__()
        self.vit = vit_backbone
        self.patch_embed = vit_backbone.patch_embed
        self.cls_token = vit_backbone.cls_token
        self.pos_embed = vit_backbone.pos_embed

    def forward(self, x, ids_keep):
        # embed patches, no mask tokens in encoder
        x = self.patch_embed(x)  # [B, N, D]
        x = x + self.pos_embed[:, 1:, :]  # add positional embeddings
        # select only visible patches
        B, N, D = x.shape
        x = torch.gather(x, 1, ids_keep.unsqueeze(-1).expand(-1, -1, D))
        cls = self.cls_token + self.pos_embed[:, :1, :]
        x = torch.cat([cls.expand(B, -1, -1), x], dim=1)
        x = self.vit.blocks(x)
        return self.vit.norm(x)
```

> ****: MAE's high masking ratio (75%) is critical — low ratios make the task too easy (neighbors provide signal). 75% forces the model to learn holistic semantic understanding rather than local interpolation.

## Pretraining Objective

The reconstruction target is the normalized pixel values within each masked patch. Per-patch mean and variance are computed and used to normalize the target, preventing the model from focusing on low-frequency color statistics rather than structure. The loss is MSE computed only on masked patches — visible patches are not penalized, focusing optimization entirely on what was hidden.

```python
import torch
import torch.nn as nn

class MAEDecoder(nn.Module):
    def __init__(self, encoder_dim=768, decoder_dim=512,
                 n_blocks=8, patch_size=16, n_channels=3):
        super().__init__()
        self.proj = nn.Linear(encoder_dim, decoder_dim)
        self.mask_token = nn.Parameter(torch.zeros(1, 1, decoder_dim))
        self.blocks = nn.Sequential(*[nn.TransformerEncoderLayer(
            d_model=decoder_dim, nhead=16, batch_first=True)
            for _ in range(n_blocks)])
        self.pred = nn.Linear(decoder_dim, patch_size * patch_size * n_channels)

    def forward(self, x, ids_restore):
        x = self.proj(x)  # project encoder tokens
        B, num_vis_plus_cls, D = x.shape
        num_patches = ids_restore.shape[1]
        mask_tokens = self.mask_token.expand(B, num_patches - (num_vis_plus_cls - 1), D)
        x_ = torch.cat([x[:, 1:, :], mask_tokens], dim=1)
        x_ = torch.gather(x_, 1, ids_restore.unsqueeze(-1).expand(-1, -1, D))
        x = torch.cat([x[:, :1, :], x_], dim=1)
        x = self.blocks(x)
        return self.pred(x[:, 1:, :])
```

## MAE vs Contrastive Methods

```python
import torch
import torch.nn as nn
from timm.models.vision_transformer import VisionTransformer

def build_mae_finetuning_model(encoder, num_classes=1000):
    # discard decoder; attach classification head to encoder
    class MAEFineTuner(nn.Module):
        def __init__(self, enc, n_cls):
            super().__init__()
            self.encoder = enc
            dim = enc.embed_dim
            self.head = nn.Linear(dim, n_cls)
            nn.init.trunc_normal_(self.head.weight, std=0.01)
        def forward(self, x):
            # use CLS token for classification
            x = self.encoder(x)[:, 0]
            return self.head(x)
    return MAEFineTuner(encoder, num_classes)
```

MAE and contrastive methods (DINO, CLIP, SimCLR) learn complementary representations. Contrastive methods produce features that excel at linear probing and k-NN tasks because the contrastive objective directly structures the embedding space for similarity comparisons. MAE features often require fine-tuning to reach peak performance but then surpass contrastive baselines on tasks like detection and segmentation.

| Method | Loss | Masking | Linear Acc (%) | Fine-tune Acc (%) | Throughput |
| --- | --- | --- | --- | --- | --- |
| MAE-B | MSE (pixels) | 75% | 68.0 | 83.6 | Fast |
| MAE-L | MSE (pixels) | 75% | 76.0 | 85.9 | Medium |
| MAE-H | MSE (pixels) | 75% | 77.2 | 87.8 | Slow |
| BEiT | Cross-entropy (tokens) | 40% | 56.7 | 83.2 | Medium |
| SimMIM | MSE (pixels) | 60% | 65.7 | 83.8 | Medium |
| DINO-B | Cross-entropy | None | 80.1 | 82.8 | Fast |

## Key Takeaways

MAE demonstrates that generative pretraining — reconstructing masked input — is a powerful and scalable self-supervised learning paradigm for vision. The asymmetric encoder-decoder design simultaneously improves compute efficiency and representation quality. MAE scales gracefully: ViT-H with MAE pretraining matches or exceeds all prior self-supervised methods on standard benchmarks.

Practical advantages over contrastive methods: no need for negative pairs or large batches, no specialized augmentation pipelines (random crop + horizontal flip suffice), no momentum encoder, and lower memory usage during pretraining. The reconstruction objective is invariant to the number of categories, making MAE naturally suitable for domain-specific pretraining outside ImageNet.

Downstream usage: discard the decoder after pretraining and fine-tune only the encoder with a task head. For detection (ViTDet), MAE-pretrained ViT-H achieves 61.3 AP on COCO. For segmentation (UPerNet), it achieves 53.6 mIoU on ADE20k. These results establish MAE as the de facto pretraining method for large ViT models in dense prediction tasks.

Extensions and variants: VideoMAE applies the same paradigm to video with tube masking; Audio-MAE to spectrograms; Point-MAE to 3D point clouds. iBOT combines MAE-style patch token prediction with DINO's global CLS distillation for a hybrid objective that achieves strong performance on both linear probing and fine-tuning benchmarks without sacrificing either strength.

Common implementation pitfalls: not normalizing pixel targets per-patch (model learns color statistics instead of structure), using too small a decoder (4 blocks, 256-dim), including mask tokens in the encoder (leaks positional information about masked locations), and using cosine similarity loss instead of MSE (less stable, no clear benefit). Use the exact decoder architecture from the original paper as a starting point.

Scaling behavior: MAE shows strong scaling with both model size and pretraining duration. ViT-H pretrained for 1600 epochs consistently outperforms shorter schedules. Unlike supervised training, there is no clear sign of overfitting with longer pretraining on ImageNet-1k — MAE benefits from the increased number of masked patch reconstruction problems seen during training.

Recommended configuration for practitioners: ViT-L/16 with MAE pretraining for 400 epochs on a domain-specific dataset provides strong initialization for fine-tuning on downstream tasks. The original FAIR implementation (github.com/facebookresearch/mae) is clean and well-documented. HuggingFace Transformers includes ViTMAEModel with pretrained weights for both ViT-B and ViT-L variants.

