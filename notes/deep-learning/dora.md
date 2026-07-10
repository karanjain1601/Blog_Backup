---
title: "DoRA — Weight-Decomposed LoRA with Magnitude and Direction Adaptation"
slug: "dora"
description: "In-depth guide to DoRA (Liu et al., 2024): decompose pretrained weights W0 = m·(V/‖V‖), separately adapt magnitude m with a learned scalar and direction V with LoRA, yielding consistent 1-3% improvements over same-rank LoRA across commonsense reasoning benchmarks."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiRG9SQSAoV2VpZ2h0LURlY29tcG9zZWQgTG93LVJhbmsgQWRhcHRhdGlvbiwgTGl1IGV0IGFsLiAyMDI0KSBpZGVudGlmaWVzIGEgc3RydWN0dXJhbCBsaW1pdGF0aW9uIG9mIExvUkE6IExvUkEgYWRhcHRzIG9ubHkgdGhlIGNvbHVtbiBzcGFjZSAoZGlyZWN0aW9uKSBvZiB3ZWlnaHQgdXBkYXRlcywgd2l0aCBubyBleHBsaWNpdCBjb250cm9sIG92ZXIgbWFnbml0dWRlIGNoYW5nZXMuIERvUkEgZGVjb21wb3NlcyBlYWNoIHByZXRyYWluZWQgd2VpZ2h0IG1hdHJpeCBX4oKAID0gbcK3KFYv4oCWVuKAlikgaW50byBhIG1hZ25pdHVkZSB2ZWN0b3IgbSDiiIgg4oSdXihvdXRfZmVhdHVyZXMpIGFuZCBhIGRpcmVjdGlvbiBtYXRyaXggVi/igJZW4oCWICh1bml0IG5vcm0pLiBJdCB0aGVuIGxlYXJucyDOlG0gKG1hZ25pdHVkZSBjaGFuZ2UpIGRpcmVjdGx5IGFzIGEgc2NhbGFyIHZlY3RvciBhbmQgzpRWIChkaXJlY3Rpb24gY2hhbmdlKSB2aWEgYSBzdGFuZGFyZCBMb1JBIGJyYW5jaCDigJQgc2VwYXJhdGVseSBvcHRpbWl6aW5nIGJvdGggY29tcG9uZW50cyBmb3IgYmV0dGVyIGFwcHJveGltYXRpb24gb2YgZnVsbCBmaW5lLXR1bmluZy4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJMb1JBXHUwMDI3cyBTdHJ1Y3R1cmFsIExpbWl0YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkFuYWx5c2lzIG9mIGZ1bGwgZmluZS10dW5pbmcgdXBkYXRlcyBzaG93cyB0aGF0IHByZXRyYWluZWQgTExNIHdlaWdodHMgdW5kZXJnbyBib3RoIG1hZ25pdHVkZSBhbmQgZGlyZWN0aW9uIGNoYW5nZXM6IHNvbWUgbmV1cm9ucyBzY2FsZSB1cCAobWFnbml0dWRlIGluY3JlYXNlcykgd2hpbGUgcGl2b3RpbmcgaW4gd2VpZ2h0IHNwYWNlIChkaXJlY3Rpb24gY2hhbmdlcykuIExvUkEgaW5qZWN0cyDOlFcgPSAozrEvcilCQSB3aGljaCBpcyBhIHJhbmstciBtYXRyaXgg4oCUIGl0IGNoYW5nZXMgdGhlIGVmZmVjdGl2ZSBjb2x1bW4gc3BhY2UgYnV0IGNhbm5vdCBpbmRlcGVuZGVudGx5IGNvbnRyb2wgcm93IG1hZ25pdHVkZXMuIEluIHByYWN0aWNlLCBMb1JBIGltcGxpY2l0bHkgY2hhbmdlcyBtYWduaXR1ZGVzIGFzIGEgc2lkZSBlZmZlY3Qgb2YgdGhlIGRpcmVjdGlvbiB1cGRhdGUsIGJ1dCB0aGlzIGNvdXBsaW5nIG1ha2VzIG9wdGltaXphdGlvbiBoYXJkZXIuIERvUkEgZGVjb3VwbGVzIHRoZW06IHRoZSBtYWduaXR1ZGUgdmVjdG9yIGlzIHRyYWluZWQgaW5kZXBlbmRlbnRseSBmcm9tIHRoZSBkaXJlY3Rpb24gTG9SQSBicmFuY2guIn0seyJ0eXBlIjoibWF0aCIsImNvbnRlbnQiOiJXXzAgPSBtIFxcY2RvdCBcXGZyYWN7Vn17XFx8VlxcfH0sXFxxdWFkIFdfe1xcdGV4dHtEb1JBfX0gPSAobSArIFxcRGVsdGEgbSkgXFxjZG90IFxcZnJhY3tWICsgXFxEZWx0YSBWX3tcXHRleHR7TG9SQX19fXtcXHxWICsgXFxEZWx0YSBWX3tcXHRleHR7TG9SQX19XFx8fSIsImRpc3BsYXkiOnRydWV9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRvUkEg4oCUIFdlaWdodCBEZWNvbXBvc2l0aW9uIGFuZCBTZXBhcmF0ZSBBZGFwdGF0aW9uIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEb1JBIGluaXRpYWxpemF0aW9uOiBnaXZlbiBwcmV0cmFpbmVkIFfigoAg4oiIIOKEnV4oZMOXayksIGNvbXB1dGUgdGhlIHJvdy13aXNlIEwyIG5vcm1zIG0gPSDigJZX4oKA4oCWX3JvdyDiiIgg4oSdXmQgYW5kIHRoZSB1bml0LWRpcmVjdGlvbiBtYXRyaXggViA9IFfigoAgLyBtLiBUaGUgbWFnbml0dWRlIHZlY3RvciBtIGlzIHN0b3JlZCBhcyBhIGxlYXJuYWJsZSBwYXJhbWV0ZXIgKGluaXRpYWxpemVkIHRvIHRoZSBhY3R1YWwgcm93IG5vcm1zIG9mIFfigoApLiBUaGUgZGlyZWN0aW9uIFYgaXMgc3RvcmVkIGFzIGEgYnVmZmVyIChub24tbGVhcm5hYmxlIGJhc2UpIGFuZCBhZGFwdGVkIHZpYSBhIHN0YW5kYXJkIExvUkEgYnJhbmNoIM6UViA9ICjOsS9yKUJBLiBBdCBlYWNoIGZvcndhcmQgcGFzczogY29tcHV0ZSBhZGFwdGVkIGRpcmVjdGlvbiBWICsgzpRWLCBub3JtYWxpemUgaXQgdG8gdW5pdCB2ZWN0b3JzLCB0aGVuIHNjYWxlIGJ5IG0gKyDOlG0gd2hlcmUgzpRtIGlzIGFsc28gbGVhcm5lZC4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIk1hZ25pdHVkZSBtIOKIiCBSXmQ6IGxlYXJuYWJsZSB2ZWN0b3IsIGluaXRpYWxpemVkIHRvIHJvdy13aXNlIEwyIG5vcm1zIG9mIFcwIOKAlCBjb250cm9scyBcdTAwMjdob3cgbXVjaFx1MDAyNyBlYWNoIG91dHB1dCBuZXVyb24gYWN0aXZhdGVzIiwiRGlyZWN0aW9uIFYvfHxWfHw6IHVuaXQtbm9ybSB3ZWlnaHQgbWF0cml4LCBhZGFwdGVkIHZpYSBMb1JBIGJyYW5jaCAoYWxwaGEvcikqQkBBIOKAlCBjb250cm9scyBcdTAwMjd3aGljaCBmZWF0dXJlc1x1MDAyNyB0aGUgbmV1cm9uIGRldGVjdHMiLCJMb1JBIGJyYW5jaDogc2FtZSBBLCBCIG1hdHJpY2VzIGFzIHN0YW5kYXJkIExvUkE7IHVwZGF0ZWQgdGhyb3VnaCBncmFkaWVudCBkZXNjZW50IHdpdGggdGhlIHNhbWUgcmFuayBoeXBlcnBhcmFtZXRlciIsIkV4dHJhIHBhcmFtZXRlcnM6IG9ubHkgZCBtYWduaXR1ZGUgc2NhbGFycyBwZXIgd2VpZ2h0IG1hdHJpeCAoNzY4IGZvciA3QiBMTGFNQSBRLXByb2opIOKAlCBjb21wbGV0ZWx5IG5lZ2xpZ2libGUgb3ZlcmhlYWQiLCJIdWdnaW5nRmFjZSBQRUZUIHN1cHBvcnQ6IGVuYWJsZWQgYnkgdXNlX2RvcmE9VHJ1ZSBpbiBMb3JhQ29uZmlnIOKAlCBubyBhcmNoaXRlY3R1cmFsIGNoYW5nZXMgbmVlZGVkIGJleW9uZCB0aGUgZmxhZyJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEb1JBIExheWVyIOKAlCBJbXBsZW1lbnRhdGlvbiBmcm9tIFNjcmF0Y2gifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCBtYXRoXG5cbmNsYXNzIERvUkFMYXllcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkRvUkE6IFcgPSBtYWduaXR1ZGUgKiBub3JtYWxpemUoZGlyZWN0aW9uICsgTG9SQV9kZWx0YSkuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2ZlYXQ6IGludCwgb3V0X2ZlYXQ6IGludCxcbiAgICAgICAgICAgICAgICAgcmFuazogaW50ID0gNCwgYWxwaGE6IGZsb2F0ID0gMTYuMCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnNjYWxpbmcgPSBhbHBoYSAvIHJhbmtcbiAgICAgICAgVzAgPSB0b3JjaC5yYW5kbihvdXRfZmVhdCwgaW5fZmVhdCkgKiAwLjAyXG4gICAgICAgIHJvd19ub3JtcyA9IFcwLm5vcm0oZGltPTEsIGtlZXBkaW09VHJ1ZSkuY2xhbXAobWluPTFlLTgpXG4gICAgICAgICMgTGVhcm5hYmxlIG1hZ25pdHVkZTogaW5pdGlhbGl6ZWQgdG8gcm93LXdpc2UgTDIgbm9ybXMgb2YgVzBcbiAgICAgICAgc2VsZi5tYWduaXR1ZGUgPSBubi5QYXJhbWV0ZXIocm93X25vcm1zLnNxdWVlemUoMSkpICAjIFtvdXRfZmVhdF1cbiAgICAgICAgIyBGcm96ZW4gdW5pdC1kaXJlY3Rpb24gbWF0cml4IChub24tbGVhcm5hYmxlIGJhc2UpXG4gICAgICAgIHNlbGYucmVnaXN0ZXJfYnVmZmVyKFwiZGlyZWN0aW9uXCIsIChXMCAvIHJvd19ub3JtcykuaGFsZigpKVxuICAgICAgICAjIExvUkEgbWF0cmljZXMgZm9yIGRpcmVjdGlvbiBhZGFwdGF0aW9uOiBBIH4gTigwLHNpZ21hKSwgQiA9IDBcbiAgICAgICAgc2VsZi5sb3JhX0EgPSBubi5QYXJhbWV0ZXIodG9yY2guZW1wdHkocmFuaywgaW5fZmVhdCkpXG4gICAgICAgIHNlbGYubG9yYV9CID0gbm4uUGFyYW1ldGVyKHRvcmNoLnplcm9zKG91dF9mZWF0LCByYW5rKSlcbiAgICAgICAgbm4uaW5pdC5rYWltaW5nX3VuaWZvcm1fKHNlbGYubG9yYV9BLCBhPW1hdGguc3FydCg1KSlcbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICAjIFBlcnR1cmIgdGhlIGRpcmVjdGlvbiB3aXRoIHRoZSBMb1JBIGJyYW5jaFxuICAgICAgICBkaXJfZGVsdGEgPSBzZWxmLnNjYWxpbmcgKiAoc2VsZi5sb3JhX0IgQCBzZWxmLmxvcmFfQSlcbiAgICAgICAgYWRhcHRlZF9kaXIgPSBzZWxmLmRpcmVjdGlvbi5mbG9hdCgpICsgZGlyX2RlbHRhXG4gICAgICAgICMgUmUtbm9ybWFsaXplIGVhY2ggcm93IHRvIHVuaXQgdmVjdG9yXG4gICAgICAgIHVuaXRfZGlyID0gYWRhcHRlZF9kaXIgLyBhZGFwdGVkX2Rpci5ub3JtKGRpbT0xLCBrZWVwZGltPVRydWUpLmNsYW1wKDFlLTgpXG4gICAgICAgICMgUmVjb25zdHJ1Y3Qgd2VpZ2h0OiBtYWduaXR1ZGUgKiB1bml0X2RpcmVjdGlvblxuICAgICAgICBXID0gc2VsZi5tYWduaXR1ZGUudW5zcXVlZXplKDEpICogdW5pdF9kaXJcbiAgICAgICAgcmV0dXJuIHggQCBXLlRcblxubGF5ZXIgPSBEb1JBTGF5ZXIoaW5fZmVhdD03NjgsIG91dF9mZWF0PTc2OCwgcmFuaz04LCBhbHBoYT0xNilcbnggPSB0b3JjaC5yYW5kbigyLCAxMCwgNzY4KVxucHJpbnQoZlwiT3V0cHV0IHNoYXBlOiB7bGF5ZXIoeCkuc2hhcGV9XCIpXG50cmFpbmFibGUgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIGxheWVyLnBhcmFtZXRlcnMoKSlcbnByaW50KGZcIlRyYWluYWJsZSBwYXJhbXM6IHt0cmFpbmFibGU6LH1cIikgICMgNzY4IG1hZ25pdHVkZSArIDEyMjg4IExvUkEgPSAxMzA1NiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIG5vcm1hbGl6YXRpb24gc3RlcCAodW5pdF9kaXIgPSBhZGFwdGVkX2RpciAvIG5vcm0pIGVuc3VyZXMgdGhhdCBncmFkaWVudCB1cGRhdGVzIHRvIGxvcmFfQSBhbmQgbG9yYV9CIGFmZmVjdCBvbmx5IHRoZSBkaXJlY3Rpb24gb2YgdGhlIHdlaWdodCwgbm90IGl0cyBtYWduaXR1ZGUg4oCUIGJlY2F1c2UgbWFnbml0dWRlIGNoYW5nZXMgYXJlIHNlcGFyYXRlbHkgaGFuZGxlZCBieSB0aGUgc2VsZi5tYWduaXR1ZGUgcGFyYW1ldGVyLiBUaGlzIGRlY291cGxpbmcgaXMgdGhlIGNvcmUgb2YgRG9SQVx1MDAyN3MgaW1wcm92ZW1lbnQgb3ZlciBMb1JBOiB0aGUgb3B0aW1pemVyIGNhbiBpbmRlcGVuZGVudGx5IHR1bmUgaG93IGxhcmdlIGVhY2ggbmV1cm9uXHUwMDI3cyByZXNwb25zZSBpcyB2ZXJzdXMgd2hpY2ggZmVhdHVyZXMgaXQgcmVzcG9uZHMgdG8uIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWFnbml0dWRlIHZzIERpcmVjdGlvbiBBbmFseXNpcyJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuZGVmIGFuYWx5emVfd2VpZ2h0X3VwZGF0ZShXX2Jhc2U6IHRvcmNoLlRlbnNvcixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgV19hZGFwdGVkOiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJEZWNvbXBvc2Ugd2VpZ2h0IHVwZGF0ZSBpbnRvIG1hZ25pdHVkZSB2cyBkaXJlY3Rpb24gY29tcG9uZW50cy5cIlwiXCJcbiAgICAjIFJvdy13aXNlIEwyIG1hZ25pdHVkZSBmb3IgZWFjaCBvdXRwdXQgbmV1cm9uXG4gICAgbWFnX2Jhc2UgPSBXX2Jhc2Uubm9ybShkaW09MSkgICAgICAgICAgICAgIyBbb3V0X2ZlYXR1cmVzXVxuICAgIG1hZ19hZGFwdGVkID0gV19hZGFwdGVkLm5vcm0oZGltPTEpXG4gICAgIyBSZWxhdGl2ZSBtYWduaXR1ZGUgY2hhbmdlOiB8ZGVsdGFfbXwgLyBtX2Jhc2VcbiAgICByZWxfbWFnID0gKChtYWdfYWRhcHRlZCAtIG1hZ19iYXNlKSAvIG1hZ19iYXNlLmNsYW1wKDFlLTgpKS5hYnMoKS5tZWFuKCkuaXRlbSgpXG5cbiAgICAjIFJvdy13aXNlIGRpcmVjdGlvbjogbm9ybWFsaXplIHRvIHVuaXQgdmVjdG9yc1xuICAgIGRpcl9iYXNlID0gRi5ub3JtYWxpemUoV19iYXNlLCBkaW09MSlcbiAgICBkaXJfYWRhcHRlZCA9IEYubm9ybWFsaXplKFdfYWRhcHRlZCwgZGltPTEpXG4gICAgIyBEaXJlY3Rpb24gY2hhbmdlOiAxIC0gY29zaW5lX3NpbSAoMD1pZGVudGljYWwsIDE9b3J0aG9nb25hbClcbiAgICBjb3Nfc2ltID0gKGRpcl9iYXNlICogZGlyX2FkYXB0ZWQpLnN1bShkaW09MSkuY2xhbXAoLTEsIDEpXG4gICAgZGlyX2NoYW5nZSA9ICgxIC0gY29zX3NpbSkubWVhbigpLml0ZW0oKVxuICAgIHJldHVybiB7XCJtYWdfY2hhbmdlXCI6IHJlbF9tYWcsIFwiZGlyX2NoYW5nZVwiOiBkaXJfY2hhbmdlfVxuXG5XMCA9IHRvcmNoLnJhbmRuKDc2OCwgNzY4KSAqIDAuMDJcbiMgU2ltdWxhdGUgTG9SQTogcmFuay1yIGFkZGl0aXZlIHBlcnR1cmJhdGlvbiAoZGlyZWN0aW9uIGNoYW5nZSwgaW1wbGljaXQgbWFnbml0dWRlIHNoaWZ0KVxuciA9IDhcbkJfbWF0ID0gdG9yY2gucmFuZG4oNzY4LCByKSAqIDAuMDAxXG5BX21hdCA9IHRvcmNoLnJhbmRuKHIsIDc2OCkgKiAwLjAwMVxuV19sb3JhID0gVzAgKyBCX21hdCBAIEFfbWF0XG4jIFNpbXVsYXRlIERvUkE6IGV4cGxpY2l0IG1hZ25pdHVkZSBzaGlmdCArIExvUkEgZGlyZWN0aW9uIGNoYW5nZVxuV19kb3JhID0gVzAgKiAoMSArIDAuMDUgKiB0b3JjaC5yYW5kbig3NjgsIDEpKSAgIyBleHBsaWNpdCBtYWduaXR1ZGUgYWRhcHRhdGlvblxuV19kb3JhID0gV19kb3JhICsgMC4wMDA1ICogdG9yY2gucmFuZG4oNzY4LCA3NjgpICAjIExvUkEgZGlyZWN0aW9uIGNoYW5nZVxuXG5sb3JhX3N0YXRzID0gYW5hbHl6ZV93ZWlnaHRfdXBkYXRlKFcwLCBXX2xvcmEpXG5kb3JhX3N0YXRzID0gYW5hbHl6ZV93ZWlnaHRfdXBkYXRlKFcwLCBXX2RvcmEpXG5wcmludChmXCJMb1JBIC1cdTAwM2UgbWFnOiB7bG9yYV9zdGF0c1tcdTAwMjdtYWdfY2hhbmdlXHUwMDI3XTouNWZ9LCBkaXI6IHtsb3JhX3N0YXRzW1x1MDAyN2Rpcl9jaGFuZ2VcdTAwMjddOi41Zn1cIilcbnByaW50KGZcIkRvUkEgLVx1MDAzZSBtYWc6IHtkb3JhX3N0YXRzW1x1MDAyN21hZ19jaGFuZ2VcdTAwMjddOi41Zn0sIGRpcjoge2RvcmFfc3RhdHNbXHUwMDI3ZGlyX2NoYW5nZVx1MDAyN106LjVmfVwiKVxucHJpbnQoXCJEb1JBIGNvbnRyb2xzIG1hZ25pdHVkZSBleHBsaWNpdGx5OyBMb1JBIGNoYW5nZXMgaXQgb25seSBhcyBhIHNpZGUgZWZmZWN0LlwiKSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGFuYWx5c2lzIHJldmVhbHMgdGhhdCBMb1JBIHVwZGF0ZXMgcHJvZHVjZSBzaW1pbGFyIG1hZ25pdHVkZSBhbmQgZGlyZWN0aW9uIGNoYW5nZXMgKHRpZ2h0bHkgY291cGxlZCksIHdoaWxlIERvUkEgYWxsb3dzIGluZGVwZW5kZW50IGNvbnRyb2wg4oCUIHRoZSBtYWduaXR1ZGUgdmVjdG9yIGNhbiBjaGFuZ2Ugc2lnbmlmaWNhbnRseSB3aGlsZSB0aGUgZGlyZWN0aW9uIGNoYW5nZXMgb25seSBzbGlnaHRseSwgb3IgdmljZSB2ZXJzYS4gVGhpcyBtYXRjaGVzIHRoZSBwYXR0ZXJuIG9ic2VydmVkIGluIGZ1bGwgZmluZS10dW5pbmcgd2hlcmUgZGlmZmVyZW50IGxheWVycyB1bmRlcmdvIGRpZmZlcmVudCBtYWduaXR1ZGVzIG9mIG1hZ25pdHVkZSB2cyBkaXJlY3Rpb24gY2hhbmdlIGRlcGVuZGluZyBvbiB0aGUgdGFzay4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEb1JBIHdpdGggSHVnZ2luZ0ZhY2UgUEVGVCJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplciwgVHJhaW5pbmdBcmd1bWVudHNcbmZyb20gcGVmdCBpbXBvcnQgTG9yYUNvbmZpZywgZ2V0X3BlZnRfbW9kZWwsIFRhc2tUeXBlXG5mcm9tIHRybCBpbXBvcnQgU0ZUVHJhaW5lclxuZnJvbSBkYXRhc2V0cyBpbXBvcnQgbG9hZF9kYXRhc2V0XG5cbm1vZGVsID0gQXV0b01vZGVsRm9yQ2F1c2FsTE0uZnJvbV9wcmV0cmFpbmVkKFxuICAgIFwibWV0YS1sbGFtYS9MbGFtYS0yLTdiLWhmXCIsXG4gICAgdG9yY2hfZHR5cGU9dG9yY2guYmZsb2F0MTYsXG4gICAgZGV2aWNlX21hcD1cImF1dG9cIixcbilcbnRva2VuaXplciA9IEF1dG9Ub2tlbml6ZXIuZnJvbV9wcmV0cmFpbmVkKFwibWV0YS1sbGFtYS9MbGFtYS0yLTdiLWhmXCIpXG50b2tlbml6ZXIucGFkX3Rva2VuID0gdG9rZW5pemVyLmVvc190b2tlblxuXG4jIERvUkE6IGlkZW50aWNhbCB0byBMb3JhQ29uZmlnIGJ1dCB3aXRoIHVzZV9kb3JhPVRydWVcbmRvcmFfY29uZmlnID0gTG9yYUNvbmZpZyhcbiAgICB0YXNrX3R5cGU9VGFza1R5cGUuQ0FVU0FMX0xNLFxuICAgIHI9MTYsIGxvcmFfYWxwaGE9MzIsXG4gICAgdGFyZ2V0X21vZHVsZXM9W1wicV9wcm9qXCIsIFwidl9wcm9qXCIsIFwia19wcm9qXCIsIFwib19wcm9qXCJdLFxuICAgIGxvcmFfZHJvcG91dD0wLjA1LCBiaWFzPVwibm9uZVwiLFxuICAgIHVzZV9kb3JhPVRydWUsICAgIyBFbmFibGUgd2VpZ2h0IGRlY29tcG9zaXRpb24gaW50byBtYWduaXR1ZGUgKyBkaXJlY3Rpb25cbilcblxucGVmdF9tb2RlbCA9IGdldF9wZWZ0X21vZGVsKG1vZGVsLCBkb3JhX2NvbmZpZylcbnBlZnRfbW9kZWwucHJpbnRfdHJhaW5hYmxlX3BhcmFtZXRlcnMoKSAgIyB+NjdNIExvUkEgKyB+MTNLIG1hZ25pdHVkZSBzY2FsYXJzXG5kYXRhc2V0ID0gbG9hZF9kYXRhc2V0KFwidGF0c3UtbGFiL2FscGFjYVwiLCBzcGxpdD1cInRyYWluWzo1MDAwXVwiKVxuYXJncyA9IFRyYWluaW5nQXJndW1lbnRzKFxuICAgIG91dHB1dF9kaXI9XCIuL2RvcmEtbGxhbWEyLTdiXCIsIHBlcl9kZXZpY2VfdHJhaW5fYmF0Y2hfc2l6ZT00LFxuICAgIGdyYWRpZW50X2FjY3VtdWxhdGlvbl9zdGVwcz00LCBudW1fdHJhaW5fZXBvY2hzPTMsXG4gICAgbGVhcm5pbmdfcmF0ZT0yZS00LCBiZjE2PVRydWUsIGxvZ2dpbmdfc3RlcHM9MTAsXG4pXG50cmFpbmVyID0gU0ZUVHJhaW5lcihtb2RlbD1wZWZ0X21vZGVsLCBhcmdzPWFyZ3MsXG4gICAgICAgICAgICAgICAgICAgICB0cmFpbl9kYXRhc2V0PWRhdGFzZXQsIHRva2VuaXplcj10b2tlbml6ZXIpXG50cmFpbmVyLnRyYWluKClcbnBlZnRfbW9kZWwuc2F2ZV9wcmV0cmFpbmVkKFwiLi9kb3JhLWFkYXB0ZXJcIikifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvbmx5IGRpZmZlcmVuY2UgZnJvbSBzdGFuZGFyZCBMb1JBIHRyYWluaW5nIGluIFBFRlQgaXMgdGhlIHVzZV9kb3JhPVRydWUgZmxhZy4gVGhlIG1hZ25pdHVkZSB2ZWN0b3JzIGFyZSBzdG9yZWQgYXMgYWRkaXRpb25hbCBwYXJhbWV0ZXJzIGluIHRoZSBhZGFwdGVyIGNoZWNrcG9pbnQg4oCUIGZvciBhIDdCIG1vZGVsIHRhcmdldGluZyBRLCBLLCBWLCBPIGFjcm9zcyAzMiBsYXllcnMsIHRoaXMgYWRkcyBvbmx5IDQgw5cgMzIgw5cgNDA5NiA9IDUyNCwyODggZXh0cmEgZmxvYXQzMiB2YWx1ZXMgKH4yTUIpIOKAlCBjb21wbGV0ZWx5IG5lZ2xpZ2libGUgY29tcGFyZWQgdG8gdGhlIDEwME1CKyBMb1JBIGFkYXB0ZXIgd2VpZ2h0cy4gVHJhaW5pbmcgdGltZSBpcyBuZWFybHkgaWRlbnRpY2FsIHRvIExvUkEgYmVjYXVzZSB0aGUgbWFnbml0dWRlIHVwZGF0ZSBpcyBqdXN0IGEgdmVjdG9yIGFkZGl0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkRvUkEgdnMgTG9SQSBCZW5jaG1hcmsifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5mcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQXV0b01vZGVsRm9yQ2F1c2FsTE1cbmZyb20gcGVmdCBpbXBvcnQgTG9yYUNvbmZpZywgZ2V0X3BlZnRfbW9kZWwsIFRhc2tUeXBlXG5mcm9tIGxtX2V2YWwgaW1wb3J0IGV2YWx1YXRvclxuZnJvbSBsbV9ldmFsLm1vZGVscy5odWdnaW5nZmFjZSBpbXBvcnQgSEZMTVxuXG5kZWYgcnVuX3BlZnRfZXZhbChtb2RlbF9uYW1lOiBzdHIsIHVzZV9kb3JhOiBib29sLCByYW5rOiBpbnQgPSAxNikgLVx1MDAzZSBkaWN0OlxuICAgIFwiXCJcIkV2YWx1YXRlIExvUkEgdnMgRG9SQSBhdCBlcXVhbCByYW5rIG9uIGNvbW1vbnNlbnNlIHJlYXNvbmluZyB0YXNrcy5cIlwiXCJcbiAgICBtb2RlbCA9IEF1dG9Nb2RlbEZvckNhdXNhbExNLmZyb21fcHJldHJhaW5lZChcbiAgICAgICAgbW9kZWxfbmFtZSwgdG9yY2hfZHR5cGU9dG9yY2guYmZsb2F0MTYsIGRldmljZV9tYXA9XCJhdXRvXCJcbiAgICApXG4gICAgY29uZmlnID0gTG9yYUNvbmZpZyhcbiAgICAgICAgdGFza190eXBlPVRhc2tUeXBlLkNBVVNBTF9MTSwgcj1yYW5rLCBsb3JhX2FscGhhPXJhbmsgKiAyLFxuICAgICAgICB0YXJnZXRfbW9kdWxlcz1bXCJxX3Byb2pcIiwgXCJ2X3Byb2pcIiwgXCJrX3Byb2pcIiwgXCJvX3Byb2pcIl0sXG4gICAgICAgIGxvcmFfZHJvcG91dD0wLjA1LCB1c2VfZG9yYT11c2VfZG9yYSxcbiAgICApXG4gICAgcGVmdF9tb2RlbCA9IGdldF9wZWZ0X21vZGVsKG1vZGVsLCBjb25maWcpXG4gICAgdHJhaW5hYmxlID0gc3VtKHAubnVtZWwoKSBmb3IgcCBpbiBwZWZ0X21vZGVsLnBhcmFtZXRlcnMoKSBpZiBwLnJlcXVpcmVzX2dyYWQpXG4gICAgIyBFdmFsdWF0ZSB1c2luZyBsbS1ldmFsdWF0aW9uLWhhcm5lc3NcbiAgICBsbSA9IEhGTE0ocHJldHJhaW5lZD1wZWZ0X21vZGVsKVxuICAgIHJlc3VsdHMgPSBldmFsdWF0b3Iuc2ltcGxlX2V2YWx1YXRlKGxtLCB0YXNrcz1bXCJoZWxsYXN3YWdcIiwgXCJhcmNfZWFzeVwiXSlcbiAgICBocyA9IHJlc3VsdHNbXCJyZXN1bHRzXCJdW1wiaGVsbGFzd2FnXCJdW1wiYWNjX25vcm0sbm9uZVwiXVxuICAgIGFyYyA9IHJlc3VsdHNbXCJyZXN1bHRzXCJdW1wiYXJjX2Vhc3lcIl1bXCJhY2Msbm9uZVwiXVxuICAgIG1ldGhvZCA9IFwiRG9SQVwiIGlmIHVzZV9kb3JhIGVsc2UgXCJMb1JBXCJcbiAgICBwcmludChmXCJ7bWV0aG9kfSByPXtyYW5rfTogcGFyYW1zPXt0cmFpbmFibGU6LH0sIEhlbGxhU3dhZz17aHM6LjNmfSwgQVJDLUVhc3k9e2FyYzouM2Z9XCIpXG4gICAgcmV0dXJuIHtcIm1ldGhvZFwiOiBtZXRob2QsIFwidHJhaW5hYmxlXCI6IHRyYWluYWJsZSwgXCJoZWxsYXN3YWdcIjogaHMsIFwiYXJjX2Vhc3lcIjogYXJjfVxuXG5mb3IgdXNlX2RvcmEgaW4gW0ZhbHNlLCBUcnVlXTpcbiAgICBydW5fcGVmdF9ldmFsKFwibWV0YS1sbGFtYS9MbGFtYS0yLTdiLWhmXCIsIHVzZV9kb3JhPXVzZV9kb3JhLCByYW5rPTE2KSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRW1waXJpY2FsIHJlc3VsdHMgZnJvbSBMaXUgZXQgYWwuICgyMDI0KTogYXQgZXF1YWwgcmFuayAocj0xNiksIERvUkEgY29uc2lzdGVudGx5IG91dHBlcmZvcm1zIExvUkEgYnkgMS0zJSBvbiBjb21tb25zZW5zZSByZWFzb25pbmcgYmVuY2htYXJrcyAoSGVsbGFTd2FnLCBBUkMsIEJvb2xRLCBXaW5vR3JhbmRlKS4gVGhlIGdhcCBpcyBsYXJnZXIgZm9yIHRhc2tzIHJlcXVpcmluZyBudWFuY2VkIGZhY3R1YWwgcmVjYWxsIGFuZCBzbWFsbGVyIGZvciB0YXNrcyB3aGVyZSBzaW1wbGUgaW5zdHJ1Y3Rpb24gZm9sbG93aW5nIHN1ZmZpY2VzLiBEb1JBIG1hdGNoZXMgZnVsbCBmaW5lLXR1bmluZyBxdWFsaXR5IGF0IGxvd2VyIHJhbmtzIHRoYW4gTG9SQSwgbWFraW5nIHI9MTYgRG9SQSByb3VnaGx5IGVxdWl2YWxlbnQgdG8gcj0zMiBMb1JBIG9uIG1vc3QgYmVuY2htYXJrcy4ifSx7InR5cGUiOiJ0YWJsZSIsImhlYWRlcnMiOlsiTWV0aG9kIiwiVHJhaW5hYmxlIFBhcmFtcyIsIkFkYXB0cyBNYWduaXR1ZGUiLCJBZGFwdHMgRGlyZWN0aW9uIiwiRXh0cmEgUGFyYW1ldGVycyIsIlBlcmZvcm1hbmNlIHZzIEZ1bGwgRlQiXSwicm93cyI6W1siRnVsbCBGaW5lLVR1bmluZyIsIjEwMCUiLCJZZXMg4oCUIGV4cGxpY2l0IiwiWWVzIOKAlCBleHBsaWNpdCIsIk5vbmUiLCJCYXNlbGluZSJdLFsiTG9SQSIsIn4wLjUtMiUiLCJJbXBsaWNpdGx5IChzaWRlIGVmZmVjdCkiLCJZZXMg4oCUIHByaW1hcnkgYWRhcHRhdGlvbiIsIk5vbmUiLCI5NS05OSUiXSxbIkRvUkEiLCJ+MC41LTIlICsgdGlueSIsIlllcyDigJQgZXhwbGljaXQgzpRtIHZlY3RvciIsIlllcyDigJQgdmlhIExvUkEgYnJhbmNoIiwiZCBzY2FsYXJzL2xheWVyICh+Mk1CIHRvdGFsKSIsIjk3LTk5LjUlIl0sWyJRTG9SQSAoTG9SQSBvbiA0LWJpdCkiLCJ+MC41LTIlIiwiSW1wbGljaXRseSIsIlllcyIsIk5vbmUiLCI5NS05OCUiXSxbIlFEb1JBIChEb1JBIG9uIDQtYml0KSIsIn4wLjUtMiUgKyB0aW55IiwiWWVzIOKAlCBleHBsaWNpdCIsIlllcyDigJQgdmlhIExvUkEgYnJhbmNoIiwiZCBzY2FsYXJzL2xheWVyIiwiOTYtOTguNSUiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IldoZW4gdG8gVXNlIERvUkEgb3ZlciBMb1JBIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEb1JBIGlzIG1vc3QgYmVuZWZpY2lhbCB3aGVuOiAoMSkgdGhlIHRhcmdldCB0YXNrIHJlcXVpcmVzIHNpZ25pZmljYW50IHNoaWZ0IGZyb20gcHJldHJhaW5lZCBiZWhhdmlvciAoY29tbW9uc2Vuc2UgcmVhc29uaW5nLCBjb21wbGV4IGluc3RydWN0aW9uIGZvbGxvd2luZyksIHdoZXJlIHRoZSBwcmV0cmFpbmVkIHdlaWdodCBtYWduaXR1ZGVzIGFuZCBkaXJlY3Rpb25zIGJvdGggbmVlZCB0byBjaGFuZ2Ugc3Vic3RhbnRpYWxseTsgKDIpIHlvdSBhcmUgY29uc3RyYWluZWQgdG8gYSBsb3cgcmFuayBidWRnZXQgKHI9NCB0byByPTE2KSBhbmQgbmVlZCBtYXhpbXVtIHF1YWxpdHkgcGVyIHRyYWluYWJsZSBwYXJhbWV0ZXI7ICgzKSB5b3UgYXJlIGZpbmUtdHVuaW5nIGZyb20gYSBzdHJvbmcgcHJldHJhaW5lZCBjaGVja3BvaW50IHdoZXJlIHRoZSBwcmV0cmFpbmVkIG1hZ25pdHVkZXMgY2FycnkgbWVhbmluZ2Z1bCBpbmZvcm1hdGlvbiB3b3J0aCBwcmVzZXJ2aW5nIGFuZCBhZGFwdGluZyBzZXBhcmF0ZWx5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIERvUkEgd2hlbiBMb1JBIHVuZGVycGVyZm9ybXM6IGlmIHI9MzIgTG9SQSBzdGlsbCBsYWdzIGJlaGluZCBmdWxsIGZpbmUtdHVuaW5nIGJ5IG1vcmUgdGhhbiAzJSwgdHJ5IERvUkEgYXQgcj0xNiIsIkRvUkEgaXMgbmVhcmx5IGZyZWU6IHRoZSBleHRyYSBtYWduaXR1ZGUgcGFyYW1ldGVycyBhZGQgfjJNQiBwZXIgN0IgbW9kZWwg4oCUIGNoZWNrcG9pbnQgc2l6ZSBhbmQgdHJhaW5pbmcgdGltZSBhcmUgdmlydHVhbGx5IHVuY2hhbmdlZCIsIkNvbWJpbmUgRG9SQSB3aXRoIFFMb1JBOiBzZXQgdXNlX2RvcmE9VHJ1ZSBhbG9uZ3NpZGUgQml0c0FuZEJ5dGVzQ29uZmlnIGZvciBtYXhpbXVtIG1lbW9yeSBlZmZpY2llbmN5ICsgcXVhbGl0eSIsIkF2b2lkIERvUkEgZm9yIHNpbXBsZSBzdHlsZSB0cmFuc2ZlciBvciBkb21haW4gYWRhcHRhdGlvbiB0YXNrcyB3aGVyZSBMb1JBIGFscmVhZHkgbWF0Y2hlcyBmdWxsIGZpbmUtdHVuaW5nIGF0IHI9OCIsIkRvUkEgYW5kIExvUkErIChhc3ltbWV0cmljIGxlYXJuaW5nIHJhdGVzIGZvciBBIHZzIEIpIGFyZSBvcnRob2dvbmFsIGltcHJvdmVtZW50cyBhbmQgY2FuIGJlIGNvbWJpbmVkIiwiQmVuY2htYXJrIGJlZm9yZSBjb21taXR0aW5nOiBydW4gYSBxdWljayByPTE2IExvUkEgdnMgcj0xNiBEb1JBIGNvbXBhcmlzb24gb24gYSB2YWxpZGF0aW9uIHNldCDigJQgaWYgZ2FwIGlzIGxlc3MgdGhhbiAwLjUlLCBzdGljayB3aXRoIExvUkEiXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJEb1JBXHUwMDI3cyBLZXkgSW5zaWdodCIsImNvbnRlbnQiOiJEb1JBXHUwMDI3cyBrZXkgaW5zaWdodCBpcyB0aGF0IHByZXRyYWluZWQgd2VpZ2h0cyB1bmRlcmdvIGRpZmZlcmVudCBtYWduaXR1ZGUgdnMgZGlyZWN0aW9uIGNoYW5nZXMgZHVyaW5nIGZpbmUtdHVuaW5nIOKAlCBMb1JBIG9ubHkgYWRhcHRzIGRpcmVjdGlvbiAodmlhIGNvbHVtbiBzcGFjZSBvZiBCQSksIHdoaWxlIERvUkEgZXhwbGljaXRseSBtb2RlbHMgYm90aCwgYmV0dGVyIGFwcHJveGltYXRpbmcgZnVsbCBmaW5lLXR1bmluZ1x1MDAyN3MgdXBkYXRlIHBhdHRlcm4uIFRoZSBtYWduaXR1ZGUgdmVjdG9yIG0gYWRkcyBvbmx5IGQ9NDA5NiBleHRyYSBmbG9hdDMyIHZhbHVlcyBwZXIgdGFyZ2V0IHdlaWdodCBtYXRyaXggaW4gYSA3QiBtb2RlbCDigJQgYSBjb21wbGV0ZWx5IG5lZ2xpZ2libGUgY29zdCAofjJNQiB0b3RhbCkgZm9yIGEgY29uc2lzdGVudCAxLTMlIGJlbmNobWFyayBpbXByb3ZlbWVudCBvdmVyIHNhbWUtcmFuayBMb1JBLiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiRG9SQSByZXByZXNlbnRzIHRoZSBjdXJyZW50IHN0YXRlLW9mLXRoZS1hcnQgZm9yIHNpbmdsZS1hZGFwdGVyIFBFRlQgbWV0aG9kcywgY29uc2lzdGVudGx5IG91dHBlcmZvcm1pbmcgTG9SQSBvbiBjb21tb25zZW5zZSByZWFzb25pbmcsIGluc3RydWN0aW9uIGZvbGxvd2luZywgYW5kIG11bHRpLXRhc2sgYmVuY2htYXJrcyB3aXRoIG5lZ2xpZ2libGUgYWRkaXRpb25hbCBjb3N0LiBJdHMgY29tcGF0aWJpbGl0eSB3aXRoIFFMb1JBICh1c2VfZG9yYT1UcnVlICsgQml0c0FuZEJ5dGVzQ29uZmlnKSBhbmQgbmF0aXZlIEh1Z2dpbmdGYWNlIFBFRlQgc3VwcG9ydCBtYWtlcyBpdCBhIGRyb3AtaW4gcmVwbGFjZW1lbnQgZm9yIExvUkEgaW4gbW9zdCB0cmFpbmluZyBzY3JpcHRzLiBGb3IgbmV3IGZpbmUtdHVuaW5nIHByb2plY3RzIHRhcmdldGluZyBxdWFsaXR5LWNyaXRpY2FsIHRhc2tzLCBEb1JBIGlzIHRoZSByZWNvbW1lbmRlZCBkZWZhdWx0IG92ZXIgdmFuaWxsYSBMb1JBLiJ9XQ=="
---
# DoRA — Weight-Decomposed LoRA with Magnitude and Direction Adaptation

DoRA (Weight-Decomposed Low-Rank Adaptation, Liu et al. 2024) identifies a structural limitation of LoRA: LoRA adapts only the column space (direction) of weight updates, with no explicit control over magnitude changes. DoRA decomposes each pretrained weight matrix W₀ = m·(V/‖V‖) into a magnitude vector m ∈ ℝ^(out_features) and a direction matrix V/‖V‖ (unit norm). It then learns Δm (magnitude change) directly as a scalar vector and ΔV (direction change) via a standard LoRA branch — separately optimizing both components for better approximation of full fine-tuning.

## LoRA's Structural Limitation

Analysis of full fine-tuning updates shows that pretrained LLM weights undergo both magnitude and direction changes: some neurons scale up (magnitude increases) while pivoting in weight space (direction changes). LoRA injects ΔW = (α/r)BA which is a rank-r matrix — it changes the effective column space but cannot independently control row magnitudes. In practice, LoRA implicitly changes magnitudes as a side effect of the direction update, but this coupling makes optimization harder. DoRA decouples them: the magnitude vector is trained independently from the direction LoRA branch.

$$W_0 = m \cdot \frac{V}{\|V\|},\quad W_{\text{DoRA}} = (m + \Delta m) \cdot \frac{V + \Delta V_{\text{LoRA}}}{\|V + \Delta V_{\text{LoRA}}\|}$$

## DoRA — Weight Decomposition and Separate Adaptation

DoRA initialization: given pretrained W₀ ∈ ℝ^(d×k), compute the row-wise L2 norms m = ‖W₀‖_row ∈ ℝ^d and the unit-direction matrix V = W₀ / m. The magnitude vector m is stored as a learnable parameter (initialized to the actual row norms of W₀). The direction V is stored as a buffer (non-learnable base) and adapted via a standard LoRA branch ΔV = (α/r)BA. At each forward pass: compute adapted direction V + ΔV, normalize it to unit vectors, then scale by m + Δm where Δm is also learned.

- Magnitude m ∈ R^d: learnable vector, initialized to row-wise L2 norms of W0 — controls 'how much' each output neuron activates
- Direction V/||V||: unit-norm weight matrix, adapted via LoRA branch (alpha/r)*B@A — controls 'which features' the neuron detects
- LoRA branch: same A, B matrices as standard LoRA; updated through gradient descent with the same rank hyperparameter
- Extra parameters: only d magnitude scalars per weight matrix (768 for 7B LLaMA Q-proj) — completely negligible overhead
- HuggingFace PEFT support: enabled by use_dora=True in LoraConfig — no architectural changes needed beyond the flag

## DoRA Layer — Implementation from Scratch

```python
import torch
import torch.nn as nn
import math

class DoRALayer(nn.Module):
    """DoRA: W = magnitude * normalize(direction + LoRA_delta)."""
    def __init__(self, in_feat: int, out_feat: int,
                 rank: int = 4, alpha: float = 16.0):
        super().__init__()
        self.scaling = alpha / rank
        W0 = torch.randn(out_feat, in_feat) * 0.02
        row_norms = W0.norm(dim=1, keepdim=True).clamp(min=1e-8)
        # Learnable magnitude: initialized to row-wise L2 norms of W0
        self.magnitude = nn.Parameter(row_norms.squeeze(1))  # [out_feat]
        # Frozen unit-direction matrix (non-learnable base)
        self.register_buffer("direction", (W0 / row_norms).half())
        # LoRA matrices for direction adaptation: A ~ N(0,sigma), B = 0
        self.lora_A = nn.Parameter(torch.empty(rank, in_feat))
        self.lora_B = nn.Parameter(torch.zeros(out_feat, rank))
        nn.init.kaiming_uniform_(self.lora_A, a=math.sqrt(5))
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Perturb the direction with the LoRA branch
        dir_delta = self.scaling * (self.lora_B @ self.lora_A)
        adapted_dir = self.direction.float() + dir_delta
        # Re-normalize each row to unit vector
        unit_dir = adapted_dir / adapted_dir.norm(dim=1, keepdim=True).clamp(1e-8)
        # Reconstruct weight: magnitude * unit_direction
        W = self.magnitude.unsqueeze(1) * unit_dir
        return x @ W.T

layer = DoRALayer(in_feat=768, out_feat=768, rank=8, alpha=16)
x = torch.randn(2, 10, 768)
print(f"Output shape: {layer(x).shape}")
trainable = sum(p.numel() for p in layer.parameters())
print(f"Trainable params: {trainable:,}")  # 768 magnitude + 12288 LoRA = 13056
```

The normalization step (unit_dir = adapted_dir / norm) ensures that gradient updates to lora_A and lora_B affect only the direction of the weight, not its magnitude — because magnitude changes are separately handled by the self.magnitude parameter. This decoupling is the core of DoRA's improvement over LoRA: the optimizer can independently tune how large each neuron's response is versus which features it responds to.

## Magnitude vs Direction Analysis

```python
import torch
import torch.nn.functional as F

def analyze_weight_update(W_base: torch.Tensor,
                          W_adapted: torch.Tensor) -> dict:
    """Decompose weight update into magnitude vs direction components."""
    # Row-wise L2 magnitude for each output neuron
    mag_base = W_base.norm(dim=1)             # [out_features]
    mag_adapted = W_adapted.norm(dim=1)
    # Relative magnitude change: |delta_m| / m_base
    rel_mag = ((mag_adapted - mag_base) / mag_base.clamp(1e-8)).abs().mean().item()

    # Row-wise direction: normalize to unit vectors
    dir_base = F.normalize(W_base, dim=1)
    dir_adapted = F.normalize(W_adapted, dim=1)
    # Direction change: 1 - cosine_sim (0=identical, 1=orthogonal)
    cos_sim = (dir_base * dir_adapted).sum(dim=1).clamp(-1, 1)
    dir_change = (1 - cos_sim).mean().item()
    return {"mag_change": rel_mag, "dir_change": dir_change}

W0 = torch.randn(768, 768) * 0.02
# Simulate LoRA: rank-r additive perturbation (direction change, implicit magnitude shift)
r = 8
B_mat = torch.randn(768, r) * 0.001
A_mat = torch.randn(r, 768) * 0.001
W_lora = W0 + B_mat @ A_mat
# Simulate DoRA: explicit magnitude shift + LoRA direction change
W_dora = W0 * (1 + 0.05 * torch.randn(768, 1))  # explicit magnitude adaptation
W_dora = W_dora + 0.0005 * torch.randn(768, 768)  # LoRA direction change

lora_stats = analyze_weight_update(W0, W_lora)
dora_stats = analyze_weight_update(W0, W_dora)
print(f"LoRA -> mag: {lora_stats['mag_change']:.5f}, dir: {lora_stats['dir_change']:.5f}")
print(f"DoRA -> mag: {dora_stats['mag_change']:.5f}, dir: {dora_stats['dir_change']:.5f}")
print("DoRA controls magnitude explicitly; LoRA changes it only as a side effect.")
```

The analysis reveals that LoRA updates produce similar magnitude and direction changes (tightly coupled), while DoRA allows independent control — the magnitude vector can change significantly while the direction changes only slightly, or vice versa. This matches the pattern observed in full fine-tuning where different layers undergo different magnitudes of magnitude vs direction change depending on the task.

## DoRA with HuggingFace PEFT

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model, TaskType
from trl import SFTTrainer
from datasets import load_dataset

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer.pad_token = tokenizer.eos_token

# DoRA: identical to LoraConfig but with use_dora=True
dora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16, lora_alpha=32,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05, bias="none",
    use_dora=True,   # Enable weight decomposition into magnitude + direction
)

peft_model = get_peft_model(model, dora_config)
peft_model.print_trainable_parameters()  # ~67M LoRA + ~13K magnitude scalars
dataset = load_dataset("tatsu-lab/alpaca", split="train[:5000]")
args = TrainingArguments(
    output_dir="./dora-llama2-7b", per_device_train_batch_size=4,
    gradient_accumulation_steps=4, num_train_epochs=3,
    learning_rate=2e-4, bf16=True, logging_steps=10,
)
trainer = SFTTrainer(model=peft_model, args=args,
                     train_dataset=dataset, tokenizer=tokenizer)
trainer.train()
peft_model.save_pretrained("./dora-adapter")
```

The only difference from standard LoRA training in PEFT is the use_dora=True flag. The magnitude vectors are stored as additional parameters in the adapter checkpoint — for a 7B model targeting Q, K, V, O across 32 layers, this adds only 4 × 32 × 4096 = 524,288 extra float32 values (~2MB) — completely negligible compared to the 100MB+ LoRA adapter weights. Training time is nearly identical to LoRA because the magnitude update is just a vector addition.

## DoRA vs LoRA Benchmark

```python
import torch
from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model, TaskType
from lm_eval import evaluator
from lm_eval.models.huggingface import HFLM

def run_peft_eval(model_name: str, use_dora: bool, rank: int = 16) -> dict:
    """Evaluate LoRA vs DoRA at equal rank on commonsense reasoning tasks."""
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, device_map="auto"
    )
    config = LoraConfig(
        task_type=TaskType.CAUSAL_LM, r=rank, lora_alpha=rank * 2,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        lora_dropout=0.05, use_dora=use_dora,
    )
    peft_model = get_peft_model(model, config)
    trainable = sum(p.numel() for p in peft_model.parameters() if p.requires_grad)
    # Evaluate using lm-evaluation-harness
    lm = HFLM(pretrained=peft_model)
    results = evaluator.simple_evaluate(lm, tasks=["hellaswag", "arc_easy"])
    hs = results["results"]["hellaswag"]["acc_norm,none"]
    arc = results["results"]["arc_easy"]["acc,none"]
    method = "DoRA" if use_dora else "LoRA"
    print(f"{method} r={rank}: params={trainable:,}, HellaSwag={hs:.3f}, ARC-Easy={arc:.3f}")
    return {"method": method, "trainable": trainable, "hellaswag": hs, "arc_easy": arc}

for use_dora in [False, True]:
    run_peft_eval("meta-llama/Llama-2-7b-hf", use_dora=use_dora, rank=16)
```

Empirical results from Liu et al. (2024): at equal rank (r=16), DoRA consistently outperforms LoRA by 1-3% on commonsense reasoning benchmarks (HellaSwag, ARC, BoolQ, WinoGrande). The gap is larger for tasks requiring nuanced factual recall and smaller for tasks where simple instruction following suffices. DoRA matches full fine-tuning quality at lower ranks than LoRA, making r=16 DoRA roughly equivalent to r=32 LoRA on most benchmarks.

| Method | Trainable Params | Adapts Magnitude | Adapts Direction | Extra Parameters | Performance vs Full FT |
| --- | --- | --- | --- | --- | --- |
| Full Fine-Tuning | 100% | Yes — explicit | Yes — explicit | None | Baseline |
| LoRA | ~0.5-2% | Implicitly (side effect) | Yes — primary adaptation | None | 95-99% |
| DoRA | ~0.5-2% + tiny | Yes — explicit Δm vector | Yes — via LoRA branch | d scalars/layer (~2MB total) | 97-99.5% |
| QLoRA (LoRA on 4-bit) | ~0.5-2% | Implicitly | Yes | None | 95-98% |
| QDoRA (DoRA on 4-bit) | ~0.5-2% + tiny | Yes — explicit | Yes — via LoRA branch | d scalars/layer | 96-98.5% |

## When to Use DoRA over LoRA

DoRA is most beneficial when: (1) the target task requires significant shift from pretrained behavior (commonsense reasoning, complex instruction following), where the pretrained weight magnitudes and directions both need to change substantially; (2) you are constrained to a low rank budget (r=4 to r=16) and need maximum quality per trainable parameter; (3) you are fine-tuning from a strong pretrained checkpoint where the pretrained magnitudes carry meaningful information worth preserving and adapting separately.

- Use DoRA when LoRA underperforms: if r=32 LoRA still lags behind full fine-tuning by more than 3%, try DoRA at r=16
- DoRA is nearly free: the extra magnitude parameters add ~2MB per 7B model — checkpoint size and training time are virtually unchanged
- Combine DoRA with QLoRA: set use_dora=True alongside BitsAndBytesConfig for maximum memory efficiency + quality
- Avoid DoRA for simple style transfer or domain adaptation tasks where LoRA already matches full fine-tuning at r=8
- DoRA and LoRA+ (asymmetric learning rates for A vs B) are orthogonal improvements and can be combined
- Benchmark before committing: run a quick r=16 LoRA vs r=16 DoRA comparison on a validation set — if gap is less than 0.5%, stick with LoRA

> **DoRA's Key Insight**: DoRA's key insight is that pretrained weights undergo different magnitude vs direction changes during fine-tuning — LoRA only adapts direction (via column space of BA), while DoRA explicitly models both, better approximating full fine-tuning's update pattern. The magnitude vector m adds only d=4096 extra float32 values per target weight matrix in a 7B model — a completely negligible cost (~2MB total) for a consistent 1-3% benchmark improvement over same-rank LoRA.

DoRA represents the current state-of-the-art for single-adapter PEFT methods, consistently outperforming LoRA on commonsense reasoning, instruction following, and multi-task benchmarks with negligible additional cost. Its compatibility with QLoRA (use_dora=True + BitsAndBytesConfig) and native HuggingFace PEFT support makes it a drop-in replacement for LoRA in most training scripts. For new fine-tuning projects targeting quality-critical tasks, DoRA is the recommended default over vanilla LoRA.

