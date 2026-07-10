---
title: "Tensor Parallelism for LLM Inference"
slug: "tensor-parallelism-inference"
description: "Splitting individual weight matrices across multiple GPUs along row or column dimensions to serve models too large for a single GPU while maintaining low latency."
tags: ["deep-learning", "llm"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGVuc29yIHBhcmFsbGVsaXNtIChUUCkgc2hhcmRzIGluZGl2aWR1YWwgd2VpZ2h0IG1hdHJpY2VzIGFjcm9zcyBtdWx0aXBsZSBHUFVzLCBhbGxvd2luZyBlYWNoIEdQVSB0byBob2xkIG9ubHkgYSBmcmFjdGlvbiBvZiB0aGUgcGFyYW1ldGVycyB3aGlsZSBjb2xsZWN0aXZlbHkgY29tcHV0aW5nIHRoZSBmdWxsIGZvcndhcmQgcGFzcy4gVW5saWtlIHBpcGVsaW5lIHBhcmFsbGVsaXNtICh3aGljaCBzcGxpdHMgdGhlIG1vZGVsIGxheWVyLWJ5LWxheWVyIGFjcm9zcyBHUFVzIHdpdGggc2VxdWVudGlhbCBleGVjdXRpb24pIG9yIGRhdGEgcGFyYWxsZWxpc20gKHdoaWNoIHJlcGxpY2F0ZXMgdGhlIG1vZGVsIGFuZCBzcGxpdHMgdGhlIGJhdGNoKSwgdGVuc29yIHBhcmFsbGVsaXNtIHNwbGl0cyB0aGUgY29tcHV0YXRpb24gd2l0aGluIGVhY2ggbGF5ZXIgYW5kIHJlcXVpcmVzIHN5bmNocm9uaXphdGlvbiB3aXRoaW4gZXZlcnkgdHJhbnNmb3JtZXIgYmxvY2suIE1lZ2F0cm9uLUxNIChTaG9leWJpIGV0IGFsLiwgMjAxOSkgaW50cm9kdWNlZCB0aGUgY2Fub25pY2FsIGNvbHVtbi10aGVuLXJvdyBwYXJhbGxlbGlzbSBwYXR0ZXJuIGZvciB0cmFuc2Zvcm1lciBmZWVkLWZvcndhcmQgYW5kIGF0dGVudGlvbiBsYXllcnMgdGhhdCBpcyBub3cgaW1wbGVtZW50ZWQgYnkgdmlydHVhbGx5IGV2ZXJ5IHByb2R1Y3Rpb24gTExNIGluZmVyZW5jZSBmcmFtZXdvcmsgaW5jbHVkaW5nIHZMTE0sIFRHSSwgYW5kIFRlbnNvclJULUxMTS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJPdmVydmlldyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQSA3MEIgcGFyYW1ldGVyIExMTSBpbiBmbG9hdDE2IHJlcXVpcmVzIDE0MCBHQiBvZiBHUFUgbWVtb3J5IOKAlCBmYXIgZXhjZWVkaW5nIGEgc2luZ2xlIEExMDAgKDgwIEdCKSBvciBIMTAwICg4MCBHQikuIFRlbnNvciBwYXJhbGxlbGlzbSBhY3Jvc3MgTiBHUFVzIHJlZHVjZXMgcGVyLUdQVSBtZW1vcnkgdG8gcm91Z2hseSAxNDAvTiBHQiBmb3IgbW9kZWwgd2VpZ2h0cywgcGx1cyB0aGUgcGVyLUdQVSBLViBjYWNoZSBhbmQgYWN0aXZhdGlvbiBtZW1vcnkuIFdpdGggVFA9MiBhY3Jvc3MgdHdvIEgxMDBzLCB0aGUgNzBCIG1vZGVsIGZpdHMgY29tZm9ydGFibHkgd2l0aCByb29tIGZvciBsb25nLWNvbnRleHQgS1YgY2FjaGVzLiBUaGUgY29zdCBvZiBUUCBpcyBhbGwtcmVkdWNlIGNvbW11bmljYXRpb246IGFmdGVyIGVhY2ggY29sdW1uLXBhcmFsbGVsIG9yIHJvdy1wYXJhbGxlbCBsYXllciwgR1BVcyBtdXN0IHN5bmNocm9uaXplIHBhcnRpYWwgcmVzdWx0cy4gT24gTlZMaW5rLWNvbm5lY3RlZCBHUFVzIChlLmcuLCBBMTAwIE5WTGluayB3aXRoIDYwMCBHQi9zIGJpZGlyZWN0aW9uYWwgYmFuZHdpZHRoKSwgYWxsLXJlZHVjZSBmb3IgdHlwaWNhbCBhY3RpdmF0aW9uIHNpemVzIHRha2VzIHVuZGVyIDAuMSBtcyBhbmQgaXMgbmVnbGlnaWJsZSByZWxhdGl2ZSB0byBjb21wdXRlIHRpbWUuIE9uIFBDSWUtY29ubmVjdGVkIEdQVXMgKDE2IEdCL3MgYmlkaXJlY3Rpb25hbCksIHRoZSBzYW1lIGFsbC1yZWR1Y2UgY2FuIHRha2UgNeKAkzIwIG1zIOKAlCBwb3RlbnRpYWxseSBkb21pbmF0aW5nIHRoZSBwZXItbGF5ZXIgY29tcHV0ZSB0aW1lIGF0IGJhdGNoIHNpemUgMS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb2x1bW4gYW5kIFJvdyBQYXJhbGxlbGlzbSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTWVnYXRyb24tTE1cdTAwMjdzIHRlbnNvciBwYXJhbGxlbGlzbSB1c2VzIHR3byBjb21wbGVtZW50YXJ5IHBhcnRpdGlvbmluZyBzdHJhdGVnaWVzIGZvciBsaW5lYXIgbGF5ZXJzIFkgPSBYVyArIGIuIEluIGNvbHVtbiBwYXJhbGxlbGlzbSwgdGhlIHdlaWdodCBtYXRyaXggVyDiiIgg4oSdXihpbiDDlyBvdXQpIGlzIHNwbGl0IGFsb25nIHRoZSBvdXRwdXQgKGNvbHVtbikgZGltZW5zaW9uOiBXID0gW1dfMSB8IFdfMiB8IC4uLiB8IFdfTl0gd2hlcmUgZWFjaCBXX2kg4oiIIOKEnV4oaW4gw5cgb3V0L04pIGxpdmVzIG9uIEdQVSBpLiBFYWNoIEdQVSBjb21wdXRlcyBZX2kgPSBYIFdfaSAoYSBwYXJ0aWFsIG91dHB1dCksIHRoZW4gYW4gYWxsLWdhdGhlciBhY3Jvc3MgR1BVcyBhc3NlbWJsZXMgdGhlIGZ1bGwgWS4gSW4gcm93IHBhcmFsbGVsaXNtLCB0aGUgaW5wdXQgWCBpcyBzcGxpdCBhbG9uZyB0aGUgZmVhdHVyZSBkaW1lbnNpb246IGVhY2ggR1BVIGkgcmVjZWl2ZXMgWF9pIChhIGZyYWN0aW9uIG9mIHRoZSBpbnB1dCkgYW5kIGNvbXB1dGVzIHBhcnRpYWwgWV9pID0gWF9pIFcuIEFuIGFsbC1yZWR1Y2Ugc3VtIGNvbWJpbmVzIHRoZSBwYXJ0aWFsIG91dHB1dHMgaW50byB0aGUgZmluYWwgWSwgd2hpY2ggaXMgaWRlbnRpY2FsIG9uIGFsbCBHUFVzIGFmdGVyIHJlZHVjdGlvbi4gVGhlIGtleSBpbnNpZ2h0IG9mIE1lZ2F0cm9uXHUwMDI3cyBkZXNpZ24gaXMgdG8gY2hhaW4gY29sdW1uLXBhcmFsbGVsIOKGkiBhY3RpdmF0aW9uIOKGkiByb3ctcGFyYWxsZWwgd2l0aG91dCBhbiBpbnRlcm1lZGlhdGUgYWxsLWdhdGhlcjogdGhlIGNvbHVtbi1wYXJhbGxlbCBvdXRwdXQgWV9pIGZlZWRzIGRpcmVjdGx5IGludG8gcm93LXBhcmFsbGVsIGFzIHRoZSBzaGFyZGVkIGlucHV0IFhfaSwgcmVxdWlyaW5nIG9ubHkgb25lIGFsbC1yZWR1Y2UgYXQgdGhlIGVuZCBvZiB0aGUgdHdvLWxheWVyIGJsb2NrLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLmRpc3RyaWJ1dGVkIGFzIGRpc3RcbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcbmZyb20gdHlwaW5nIGltcG9ydCBPcHRpb25hbFxuXG5jbGFzcyBDb2x1bW5QYXJhbGxlbExpbmVhcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlNwbGl0IHdlaWdodCBXIGFsb25nIG91dHB1dCBkaW07IGVhY2ggR1BVIGhvbGRzIG91dC9OIGNvbHVtbnM7IGFsbC1nYXRoZXIgcmVzdWx0cy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fZmVhdHVyZXM6IGludCwgb3V0X2ZlYXR1cmVzOiBpbnQsIHdvcmxkX3NpemU6IGludCwgYmlhczogYm9vbCA9IFRydWUpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgYXNzZXJ0IG91dF9mZWF0dXJlcyAlIHdvcmxkX3NpemUgPT0gMCwgXCJvdXRfZmVhdHVyZXMgbXVzdCBiZSBkaXZpc2libGUgYnkgd29ybGRfc2l6ZVwiXG4gICAgICAgIHNlbGYub3V0X3Blcl9yYW5rID0gb3V0X2ZlYXR1cmVzIC8vIHdvcmxkX3NpemVcbiAgICAgICAgc2VsZi53b3JsZF9zaXplID0gd29ybGRfc2l6ZVxuICAgICAgICAjIEVhY2ggR1BVIHN0b3JlcyBhIChvdXQvTiwgaW4pIHdlaWdodCBzbGljZVxuICAgICAgICBzZWxmLndlaWdodCA9IG5uLlBhcmFtZXRlcih0b3JjaC5lbXB0eShzZWxmLm91dF9wZXJfcmFuaywgaW5fZmVhdHVyZXMpKVxuICAgICAgICBzZWxmLmJpYXMgPSBubi5QYXJhbWV0ZXIodG9yY2guemVyb3Moc2VsZi5vdXRfcGVyX3JhbmspKSBpZiBiaWFzIGVsc2UgTm9uZVxuICAgICAgICBubi5pbml0LmthaW1pbmdfdW5pZm9ybV8oc2VsZi53ZWlnaHQsIGE9NSAqKiAwLjUpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4OiB0b3JjaC5UZW5zb3IpIC1cdTAwM2UgdG9yY2guVGVuc29yOlxuICAgICAgICAjIExvY2FsIG1hdG11bDogKGJhdGNoLCBpbikgQCAoaW4sIG91dC9OKS5UIC1cdTAwM2UgKGJhdGNoLCBvdXQvTilcbiAgICAgICAgb3V0ID0gRi5saW5lYXIoeCwgc2VsZi53ZWlnaHQsIHNlbGYuYmlhcylcbiAgICAgICAgIyBBbGwtZ2F0aGVyOiBjb25jYXRlbmF0ZSBwYXJ0aWFsIG91dHB1dHMgZnJvbSBhbGwgcmFua3MgLVx1MDAzZSAoYmF0Y2gsIG91dClcbiAgICAgICAgZ2F0aGVyZWQgPSBbdG9yY2guemVyb3NfbGlrZShvdXQpIGZvciBfIGluIHJhbmdlKHNlbGYud29ybGRfc2l6ZSldXG4gICAgICAgIGRpc3QuYWxsX2dhdGhlcihnYXRoZXJlZCwgb3V0KVxuICAgICAgICByZXR1cm4gdG9yY2guY2F0KGdhdGhlcmVkLCBkaW09LTEpXG5cbmRlZiB2ZXJpZnlfY29sdW1uX3BhcmFsbGVsKHJhbms6IGludCwgd29ybGRfc2l6ZTogaW50LCBpbl9mOiBpbnQgPSAyNTYsIG91dF9mOiBpbnQgPSA1MTIpOlxuICAgIFwiXCJcIlZlcmlmeSBDb2x1bW5QYXJhbGxlbExpbmVhciBtYXRjaGVzIHNpbmdsZS1HUFUgcmVmZXJlbmNlLlwiXCJcIlxuICAgIGZ1bGxfVyA9IHRvcmNoLnJhbmRuKG91dF9mLCBpbl9mKS5jdWRhKCkgICMgcmVmZXJlbmNlIHdlaWdodFxuICAgIHggPSB0b3JjaC5yYW5kbig0LCBpbl9mKS5jdWRhKCkgICAgICAgICAgICMgc2hhcmVkIGlucHV0IChpZGVudGljYWwgb24gYWxsIEdQVXMpXG4gICAgcmVmID0gRi5saW5lYXIoeCwgZnVsbF9XKSAgICAgICAgICAgICAgICAgIyBzaW5nbGUtR1BVIHJlZmVyZW5jZVxuICAgIGxheWVyID0gQ29sdW1uUGFyYWxsZWxMaW5lYXIoaW5fZiwgb3V0X2YsIHdvcmxkX3NpemUsIGJpYXM9RmFsc2UpLmN1ZGEoKVxuICAgICMgRWFjaCByYW5rIGdldHMgaXRzIHNsaWNlIG9mIHRoZSBmdWxsIHdlaWdodFxuICAgIHNsaWNlX3NpemUgPSBvdXRfZiAvLyB3b3JsZF9zaXplXG4gICAgbGF5ZXIud2VpZ2h0LmRhdGEuY29weV8oZnVsbF9XW3JhbmsgKiBzbGljZV9zaXplOihyYW5rICsgMSkgKiBzbGljZV9zaXplXSlcbiAgICBvdXQgPSBsYXllcih4KVxuICAgIHByaW50KGZcIlJhbmsge3Jhbmt9OiBtYXhfZGlmZj17KChvdXQgLSByZWYpLmFicygpLm1heCgpKTouNmZ9XCIpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiTWVnYXRyb24tTE0gU3R5bGUgU3BsaXR0aW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJNZWdhdHJvbi1MTVx1MDAyN3Mga2V5IGNvbnRyaWJ1dGlvbiBpcyBpZGVudGlmeWluZyB0aGUgZXhhY3QgcGxhY2VtZW50IG9mIGNvbHVtbi1wYXJhbGxlbCBhbmQgcm93LXBhcmFsbGVsIGxheWVycyBpbiBhIHRyYW5zZm9ybWVyIGJsb2NrIHRoYXQgbWluaW1pemVzIHRoZSBudW1iZXIgb2YgYWxsLXJlZHVjZSBvcGVyYXRpb25zLiBGb3IgdGhlIE1MUCBzdWItYmxvY2sgKHR3byBsaW5lYXIgbGF5ZXJzOiBXMSBhbmQgVzIpLCBjb2x1bW4gcGFyYWxsZWxpc20gaXMgYXBwbGllZCB0byBXMSAoc3BsaXR0aW5nIHRoZSBvdXRwdXQvaGlkZGVuIGRpbWVuc2lvbikgYW5kIHJvdyBwYXJhbGxlbGlzbSB0byBXMiAoc3BsaXR0aW5nIHRoZSBpbnB1dC9oaWRkZW4gZGltZW5zaW9uKS4gVGhpcyBtZWFucyBXMVx1MDAyN3MgcGFydGlhbCBvdXRwdXRzIFkxX2kgPSBYIFcxX2kgYXJlIGFscmVhZHkgc3BsaXQgYWxvbmcgdGhlIGNvcnJlY3QgZGltZW5zaW9uIHRvIHNlcnZlIGFzIHRoZSByb3ctcGFyYWxsZWwgaW5wdXQgdG8gVzIsIHNvIG5vIGludGVybWVkaWF0ZSBhbGwtZ2F0aGVyIGlzIG5lZWRlZCBiZXR3ZWVuIFcxIGFuZCBXMi4gT25seSBvbmUgYWxsLXJlZHVjZSBpcyBuZWVkZWQgYXQgdGhlIG91dHB1dCBvZiBXMiBwZXIgTUxQIGJsb2NrLiBGb3IgdGhlIGF0dGVudGlvbiBzdWItYmxvY2ssIHRoZSBRLCBLLCBWIHByb2plY3Rpb25zIGFyZSBjb2x1bW4tcGFyYWxsZWwgKHNwbGl0IGFsb25nIHRoZSBoZWFkIGRpbWVuc2lvbiwgZWZmZWN0aXZlbHkgc2hhcmRpbmcgYXR0ZW50aW9uIGhlYWRzIGFjcm9zcyBHUFVzKSwgYW5kIHRoZSBvdXRwdXQgcHJvamVjdGlvbiBpcyByb3ctcGFyYWxsZWwuIE9uZSBhbGwtcmVkdWNlIGlzIG5lZWRlZCBwZXIgYXR0ZW50aW9uIGJsb2NrLiBUaGUgdG90YWwgc3luY2hyb25pemF0aW9uIGNvc3QgZm9yIGEgdHJhbnNmb3JtZXIgbGF5ZXIgaXMgdGhlcmVmb3JlIDIgYWxsLXJlZHVjZXM6IG9uZSBhZnRlciBhdHRlbnRpb24sIG9uZSBhZnRlciBNTFAuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2guZGlzdHJpYnV0ZWQgYXMgZGlzdFxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBSb3dQYXJhbGxlbExpbmVhcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIlNwbGl0IGlucHV0IFggYWxvbmcgZmVhdHVyZSBkaW07IGVhY2ggR1BVIGNvbXB1dGVzIHBhcnRpYWwgWFc7IGFsbC1yZWR1Y2Ugc3Vtcy5cIlwiXCJcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fZmVhdHVyZXM6IGludCwgb3V0X2ZlYXR1cmVzOiBpbnQsIHdvcmxkX3NpemU6IGludCwgcmFuazogaW50KTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIGFzc2VydCBpbl9mZWF0dXJlcyAlIHdvcmxkX3NpemUgPT0gMFxuICAgICAgICBzZWxmLmluX3Blcl9yYW5rID0gaW5fZmVhdHVyZXMgLy8gd29ybGRfc2l6ZVxuICAgICAgICBzZWxmLnJhbmsgPSByYW5rXG4gICAgICAgIHNlbGYud29ybGRfc2l6ZSA9IHdvcmxkX3NpemVcbiAgICAgICAgIyBFYWNoIEdQVSBzdG9yZXMgYSBjb2x1bW4gc2xpY2Ugb2YgVzogKG91dF9mZWF0dXJlcywgaW4vTilcbiAgICAgICAgc2VsZi53ZWlnaHQgPSBubi5QYXJhbWV0ZXIodG9yY2guZW1wdHkob3V0X2ZlYXR1cmVzLCBzZWxmLmluX3Blcl9yYW5rKSlcbiAgICAgICAgbm4uaW5pdC5rYWltaW5nX3VuaWZvcm1fKHNlbGYud2VpZ2h0LCBhPTUgKiogMC41KVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeF9sb2NhbDogdG9yY2guVGVuc29yKSAtXHUwMDNlIHRvcmNoLlRlbnNvcjpcbiAgICAgICAgXCJcIlwieF9sb2NhbCBpcyBhbHJlYWR5IHRoZSByYW5rLWxvY2FsIHNoYXJkOiAoYmF0Y2gsIGluL04pLlwiXCJcIlxuICAgICAgICBwYXJ0aWFsID0gRi5saW5lYXIoeF9sb2NhbCwgc2VsZi53ZWlnaHQpICAjIChiYXRjaCwgb3V0X2ZlYXR1cmVzKVxuICAgICAgICBkaXN0LmFsbF9yZWR1Y2UocGFydGlhbCwgb3A9ZGlzdC5SZWR1Y2VPcC5TVU0pICAjIHN1bSBhY3Jvc3MgYWxsIEdQVXNcbiAgICAgICAgcmV0dXJuIHBhcnRpYWwgICMgcmVzdWx0IGlzIGlkZW50aWNhbCBvbiBhbGwgcmFua3NcblxuIyBQYXR0ZXJuIGd1aWRlOiB3aGVuIHRvIHVzZSBjb2x1bW4gdnMgcm93IHBhcmFsbGVsXG5wcmludChcIk1lZ2F0cm9uIFRQIHBhdHRlcm4gZm9yIE1MUCBibG9jazpcIilcbnByaW50KFwiICBMYXllciAxIChXMSk6IENvbHVtblBhcmFsbGVsICDigJQgc3BsaXQgb3V0cHV0IGRpbSwgbm8gc3luYyBuZWVkZWRcIilcbnByaW50KFwiICBBY3RpdmF0aW9uOiAgIExvY2FsIEdFTFUvU2lMVSDigJQgbm8gY29tbXVuaWNhdGlvblwiKVxucHJpbnQoXCIgIExheWVyIDIgKFcyKTogUm93UGFyYWxsZWwgICAgIOKAlCBzcGxpdCBpbnB1dCBkaW0sIDEgYWxsLXJlZHVjZSBhdCBvdXRwdXRcIilcbnByaW50KFwiXCIpXG5wcmludChcIk1lZ2F0cm9uIFRQIHBhdHRlcm4gZm9yIEF0dGVudGlvbiBibG9jazpcIilcbnByaW50KFwiICBRLCBLLCBWIHByb2o6IENvbHVtblBhcmFsbGVsICDigJQgc2hhcmQgYWxvbmcgaGVhZCBkaW1lbnNpb25cIilcbnByaW50KFwiICBBdHRlbnRpb246ICAgIExvY2FsIHBlci1yYW5rICDigJQgZWFjaCByYW5rIGhhbmRsZXMgaXRzIGhlYWQgc2xpY2VcIilcbnByaW50KFwiICBPdXQgcHJvajogICAgIFJvd1BhcmFsbGVsICAgICDigJQgMSBhbGwtcmVkdWNlIGF0IG91dHB1dFwiKVxucHJpbnQoXCJcIilcbnByaW50KFwiVG90YWw6IDIgYWxsLXJlZHVjZXMgcGVyIHRyYW5zZm9ybWVyIGxheWVyIHJlZ2FyZGxlc3Mgb2YgVFAgZGVncmVlLlwiKSJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkF0dGVudGlvbiBIZWFkIFNoYXJkaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgbXVsdGktaGVhZCBhdHRlbnRpb24gKE1IQSkgd2l0aCBIIGhlYWRzIGFuZCBoZWFkIGRpbWVuc2lvbiBkX2ssIHRlbnNvciBwYXJhbGxlbGlzbSBvdmVyIE4gR1BVcyBhc3NpZ25zIEgvTiBoZWFkcyB0byBlYWNoIEdQVS4gRWFjaCBHUFUgY29tcHV0ZXMgZnVsbCBzZWxmLWF0dGVudGlvbiBmb3IgaXRzIHN1YnNldCBvZiBoZWFkcyB1c2luZyB0aGUgZnVsbCBpbnB1dCBzZXF1ZW5jZSDigJQgUSwgSywgViBwcm9qZWN0aW9ucyBhcmUgY29sdW1uLXBhcmFsbGVsIChlYWNoIEdQVSBnZW5lcmF0ZXMgUV9pLCBLX2ksIFZfaSBmb3IgaXRzIGhlYWRzKSwgYXR0ZW50aW9uIHNjb3JlcyBhcmUgY29tcHV0ZWQgbG9jYWxseSwgYW5kIHRoZSBvdXRwdXQgcHJvamVjdGlvbiBpcyByb3ctcGFyYWxsZWwuIFRoaXMgaGVhZC1sZXZlbCBzaGFyZGluZyByZXF1aXJlcyB0aGF0IEggaXMgZGl2aXNpYmxlIGJ5IE46IGZvciBhIDMyLWhlYWQgbW9kZWwgd2l0aCBUUD00LCBlYWNoIEdQVSBoYW5kbGVzIDggaGVhZHMuIEZvciBncm91cGVkLXF1ZXJ5IGF0dGVudGlvbiAoR1FBKSBvciBtdWx0aS1xdWVyeSBhdHRlbnRpb24gKE1RQSksIHdoaWNoIGhhdmUgZmV3ZXIgS1YgaGVhZHMgdGhhbiBxdWVyeSBoZWFkcywgdGhlIEtWIGhlYWRzIG11c3QgYWxzbyBiZSBkaXZpc2libGUgYnkgTi4gTW9kZWxzIHdpdGggdmVyeSBmZXcgS1YgaGVhZHMgKGUuZy4sIDggS1YgaGVhZHMgaW4gTExhTUEtMy03MEIpIGxpbWl0IHByYWN0aWNhbCBUUCBkZWdyZWUgdG8gODsgZ29pbmcgdG8gVFA9MTYgd2l0aCBmZXdlciB0aGFuIDE2IEtWIGhlYWRzIGlzIG5vdCBwb3NzaWJsZSB3aXRob3V0IHJlcGxpY2F0aW5nIEtWIGhlYWRzLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkFsbC1SZWR1Y2UgQ29tbXVuaWNhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiQWxsLXJlZHVjZSBpcyBhIGNvbGxlY3RpdmUgb3BlcmF0aW9uIHRoYXQgc3VtcyAob3IgdGFrZXMgbWF4L21pbiBvZikgdGVuc29ycyBmcm9tIGFsbCBwYXJ0aWNpcGF0aW5nIHJhbmtzIGFuZCBkaXN0cmlidXRlcyB0aGUgcmVzdWx0IHRvIGV2ZXJ5IHJhbmsuIE5DQ0wgKE5WSURJQSBDb2xsZWN0aXZlIENvbW11bmljYXRpb25zIExpYnJhcnkpIGltcGxlbWVudHMgYWxsLXJlZHVjZSB1c2luZyBhIHJpbmcgYWxnb3JpdGhtOiBlYWNoIEdQVSBzZW5kcyBhbmQgcmVjZWl2ZXMgZGF0YSBpbiBhIHJpbmcgdG9wb2xvZ3ksIHJlcXVpcmluZyAyICogKE4tMSkvTiBkYXRhIHBhc3Nlcy4gRm9yIE5WTGluay1jb25uZWN0ZWQgR1BVcyAoQTEwMC9IMTAwIHdpdGggNjAwIEdCL3MgYmlkaXJlY3Rpb25hbCBOVkxpbmsgYmFuZHdpZHRoKSwgYSAxTUIgYWxsLXJlZHVjZSBjb21wbGV0ZXMgaW4gdW5kZXIgMTAgbWljcm9zZWNvbmRzLiBGb3IgUENJZS1jb25uZWN0ZWQgR1BVcyAodHlwaWNhbGx5IDE24oCTMzIgR0IvcyBQQ0llIDQuMCBiYW5kd2lkdGgpLCB0aGUgc2FtZSAxTUIgYWxsLXJlZHVjZSB0YWtlcyAyMDDigJM1MDAgbWljcm9zZWNvbmRzIOKAlCBzbG93ZXIgYnkgYSBmYWN0b3Igb2YgMjDigJM1MC4gQWN0aXZhdGlvbiB0ZW5zb3JzIGluIGEgNzBCIG1vZGVsIGZvcndhcmQgcGFzcyBhcmUgdHlwaWNhbGx5IDAuNeKAkzQgTUIgcGVyIGFsbC1yZWR1Y2UgY2FsbCwgbWFraW5nIE5WTGluayBlc3NlbnRpYWxseSBmcmVlIHdoaWxlIFBDSWUgYWxsLXJlZHVjZXMgZG9taW5hdGUgaW5mZXJlbmNlIGxhdGVuY3kgYXQgc21hbGwgYmF0Y2ggc2l6ZXMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRpbWVcbmZyb20gdmxsbSBpbXBvcnQgTExNLCBTYW1wbGluZ1BhcmFtc1xuXG5kZWYgYmVuY2htYXJrX3RlbnNvcl9wYXJhbGxlbF92bGxtKFxuICAgIG1vZGVsX25hbWU6IHN0ciA9IFwibWV0YS1sbGFtYS9MbGFtYS0yLTcwYi1oZlwiLFxuICAgIHRwX3NpemVzOiBsaXN0ID0gWzIsIDRdXG4pIC1cdTAwM2UgZGljdDpcbiAgICBcIlwiXCJNZWFzdXJlIHZMTE0gdGhyb3VnaHB1dCBhdCBkaWZmZXJlbnQgdGVuc29yLXBhcmFsbGVsIGRlZ3JlZXMuXCJcIlwiXG4gICAgcHJvbXB0cyA9IFtcIkV4cGxhaW4gdGhlIHRoZW9yeSBvZiBnZW5lcmFsIHJlbGF0aXZpdHkgZnJvbSBmaXJzdCBwcmluY2lwbGVzLlwiXSAqIDMyXG4gICAgcGFyYW1zID0gU2FtcGxpbmdQYXJhbXModGVtcGVyYXR1cmU9MC4wLCBtYXhfdG9rZW5zPTI1NilcbiAgICByZXN1bHRzID0ge31cbiAgICBmb3IgdHAgaW4gdHBfc2l6ZXM6XG4gICAgICAgIGlmIHRvcmNoLmN1ZGEuZGV2aWNlX2NvdW50KCkgXHUwMDNjIHRwOlxuICAgICAgICAgICAgcHJpbnQoZlwiU2tpcHBpbmcgVFA9e3RwfTogb25seSB7dG9yY2guY3VkYS5kZXZpY2VfY291bnQoKX0gR1BVKHMpIGF2YWlsYWJsZVwiKVxuICAgICAgICAgICAgY29udGludWVcbiAgICAgICAgbGxtID0gTExNKG1vZGVsPW1vZGVsX25hbWUsIHRlbnNvcl9wYXJhbGxlbF9zaXplPXRwLFxuICAgICAgICAgICAgICAgICAgZHR5cGU9XCJmbG9hdDE2XCIsIGdwdV9tZW1vcnlfdXRpbGl6YXRpb249MC44NSlcbiAgICAgICAgIyBDb25maXJtIG1lbW9yeSBkaXN0cmlidXRpb24gYWNyb3NzIEdQVXNcbiAgICAgICAgZm9yIGkgaW4gcmFuZ2UodHApOlxuICAgICAgICAgICAgbWVtX2diID0gdG9yY2guY3VkYS5tZW1vcnlfYWxsb2NhdGVkKGkpIC8gMWU5XG4gICAgICAgICAgICBwcmludChmXCIgIFRQPXt0cH0gfCBHUFUge2l9OiB7bWVtX2diOi4xZn0gR0IgYWxsb2NhdGVkXCIpXG4gICAgICAgIHQwID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgICAgICBvdXRwdXRzID0gbGxtLmdlbmVyYXRlKHByb21wdHMsIHBhcmFtcylcbiAgICAgICAgZWxhcHNlZCA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MFxuICAgICAgICB0b2tlbnNfb3V0ID0gc3VtKGxlbihvLm91dHB1dHNbMF0udG9rZW5faWRzKSBmb3IgbyBpbiBvdXRwdXRzKVxuICAgICAgICB0cHV0ID0gdG9rZW5zX291dCAvIGVsYXBzZWRcbiAgICAgICAgbGF0ZW5jeV9tcyA9IGVsYXBzZWQgLyBsZW4ocHJvbXB0cykgKiAxMDAwXG4gICAgICAgIHJlc3VsdHNbdHBdID0ge1widGhyb3VnaHB1dF90cHNcIjogdHB1dCwgXCJsYXRlbmN5X21zXCI6IGxhdGVuY3lfbXN9XG4gICAgICAgIHByaW50KGZcIlRQPXt0cH06IHt0cHV0Oi4wZn0gdG9rL3MgIHtsYXRlbmN5X21zOi4wZn0gbXMvcmVxXCIpXG4gICAgICAgIGRlbCBsbG1cbiAgICByZXR1cm4gcmVzdWx0cyJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6InZMTE0gVGVuc29yIFBhcmFsbGVsaXNtIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJ2TExNIGltcGxlbWVudHMgdGVuc29yIHBhcmFsbGVsaXNtIHVzaW5nIFB5VG9yY2hcdTAwMjdzIGRpc3RyaWJ1dGVkIGJhY2tlbmQgKHR5cGljYWxseSBOQ0NMKSBhbmQgZXhwb3NlcyBpdCB2aWEgYSBzaW5nbGUgY29uZmlndXJhdGlvbiBwYXJhbWV0ZXI6IHRlbnNvcl9wYXJhbGxlbF9zaXplLiBJbnRlcm5hbGx5LCB2TExNIHVzZXMgTWVnYXRyb24tc3R5bGUgY29sdW1uLXRoZW4tcm93IHNwbGl0dGluZyBmb3IgTUxQIGxheWVycyBhbmQgaGVhZCBzaGFyZGluZyBmb3IgYXR0ZW50aW9uLiBUaGUgbW9kZWwgd2VpZ2h0cyBhcmUgbG9hZGVkIG9uY2UgYnkgcmFuayAwIGFuZCBicm9hZGNhc3QgdG8gb3RoZXIgcmFua3MgZHVyaW5nIGluaXRpYWxpemF0aW9uLiB2TExNXHUwMDI3cyBQYWdlZEF0dGVudGlvbiBLViBjYWNoZSBpcyBhbHNvIHNoYXJkZWQ6IGVhY2ggR1BVIHN0b3JlcyB0aGUgS1YgY2FjaGUgb25seSBmb3IgdGhlIGF0dGVudGlvbiBoZWFkcyBpdCBvd25zLiBGb3IgYSA3MEIgbW9kZWwgb24gNCBIMTAwcywgZWFjaCBHUFUgaG9sZHMgfjE3LjVCIHBhcmFtZXRlcnMgd29ydGggb2Ygd2VpZ2h0cyBhbmQgMjUlIG9mIHRoZSBLViBjYWNoZSBwYWdlcy4gVGhpcyBjb21iaW5lZCB3ZWlnaHQgKyBLViBzaGFyZGluZyBpcyB3aGF0IG1ha2VzIHZMTE0gbWVtb3J5LWVmZmljaWVudCBhdCBoaWdoIFRQIGRlZ3JlZXMuIFRoZSBhc3luY19lbmdpbmUgbW9kZSAoZGVmYXVsdCBmb3IgcHJvZHVjdGlvbikgb3ZlcmxhcHMgY29tbXVuaWNhdGlvbiB3aXRoIGNvbXB1dGF0aW9uIHVzaW5nIENVREEgc3RyZWFtcywgZnVydGhlciBoaWRpbmcgYWxsLXJlZHVjZSBsYXRlbmN5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5kaXN0cmlidXRlZCBhcyBkaXN0XG5pbXBvcnQgdGltZVxuZnJvbSB0eXBpbmcgaW1wb3J0IExpc3QsIERpY3RcblxuZGVmIHByb2ZpbGVfYWxscmVkdWNlX2xhdGVuY3koXG4gICAgdGVuc29yX3NpemVzX21iOiBMaXN0W2Zsb2F0XSA9IFsxLCAxMCwgNTAsIDEwMCwgNTAwLCAxMDAwXSxcbiAgICBuX3dhcm11cDogaW50ID0gNSxcbiAgICBuX2JlbmNoOiBpbnQgPSAyMFxuKSAtXHUwMDNlIERpY3RbZmxvYXQsIGRpY3RdOlxuICAgIFwiXCJcIkJlbmNobWFyayBOQ0NMIGFsbC1yZWR1Y2UgbGF0ZW5jeSBmb3IgdGVuc29ycyByYW5naW5nIDFNQiB0byAxR0IuXCJcIlwiXG4gICAgYXNzZXJ0IGRpc3QuaXNfaW5pdGlhbGl6ZWQoKSwgXCJDYWxsIGRpc3QuaW5pdF9wcm9jZXNzX2dyb3VwKFx1MDAyN25jY2xcdTAwMjcpIGZpcnN0LlwiXG4gICAgcmVzdWx0cyA9IHt9XG4gICAgZm9yIHNpemVfbWIgaW4gdGVuc29yX3NpemVzX21iOlxuICAgICAgICBuX2VsZW1lbnRzID0gaW50KHNpemVfbWIgKiAxZTYgLyA0KSAgIyBmbG9hdDMyOiA0IGJ5dGVzL2VsZW1lbnRcbiAgICAgICAgdGVuc29yID0gdG9yY2gucmFuZChuX2VsZW1lbnRzLCBkZXZpY2U9XCJjdWRhXCIpXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fd2FybXVwKTpcbiAgICAgICAgICAgIGRpc3QuYWxsX3JlZHVjZSh0ZW5zb3IsIG9wPWRpc3QuUmVkdWNlT3AuU1VNKVxuICAgICAgICB0b3JjaC5jdWRhLnN5bmNocm9uaXplKClcbiAgICAgICAgdDAgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgICAgIGZvciBfIGluIHJhbmdlKG5fYmVuY2gpOlxuICAgICAgICAgICAgZGlzdC5hbGxfcmVkdWNlKHRlbnNvciwgb3A9ZGlzdC5SZWR1Y2VPcC5TVU0pXG4gICAgICAgIHRvcmNoLmN1ZGEuc3luY2hyb25pemUoKVxuICAgICAgICBsYXRfbXMgPSAodGltZS5wZXJmX2NvdW50ZXIoKSAtIHQwKSAvIG5fYmVuY2ggKiAxMDAwXG4gICAgICAgICMgRWZmZWN0aXZlIGJhbmR3aWR0aDogcmluZyBhbGwtcmVkdWNlIHNlbmRzIDIqKE4tMSkvTiAqIGRhdGFcbiAgICAgICAgd29ybGQgPSBkaXN0LmdldF93b3JsZF9zaXplKClcbiAgICAgICAgZWZmZWN0aXZlX2J5dGVzID0gMiAqICh3b3JsZCAtIDEpIC8gd29ybGQgKiBzaXplX21iICogMWU2XG4gICAgICAgIGJ3X2dicHMgPSAoZWZmZWN0aXZlX2J5dGVzIC8gMWU5KSAvIChsYXRfbXMgLyAxMDAwKVxuICAgICAgICByZXN1bHRzW3NpemVfbWJdID0ge1wibGF0ZW5jeV9tc1wiOiBsYXRfbXMsIFwiYmFuZHdpZHRoX2dicHNcIjogYndfZ2Jwc31cbiAgICAgICAgcHJpbnQoZlwie3NpemVfbWI6Ni4wZn0gTUIgIHwgIHtsYXRfbXM6LjNmfSBtcyAgfCAge2J3X2dicHM6LjFmfSBHQi9zXCIpXG4gICAgcmV0dXJuIHJlc3VsdHMifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTY2FsaW5nIEVmZmljaWVuY3kifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRlbnNvciBwYXJhbGxlbGlzbSBzY2FsaW5nIGVmZmljaWVuY3kg4oCUIHRoZSBmcmFjdGlvbiBvZiBpZGVhbCBsaW5lYXIgc3BlZWR1cCBhY2hpZXZlZCBhcyBUUCBkZWdyZWUgaW5jcmVhc2VzIOKAlCBkZWdyYWRlcyBhcyBOIGdyb3dzIGJlY2F1c2UgYWxsLXJlZHVjZSBvdmVyaGVhZCBncm93cyB3aXRoIE4gd2hpbGUgcGVyLUdQVSBjb21wdXRlIHNocmlua3MuIEZvciBOVkxpbmsgc3lzdGVtcywgZWZmaWNpZW5jeSByZW1haW5zIGFib3ZlIDkwJSB0aHJvdWdoIFRQPTggZm9yIDcwQiBtb2RlbHMgYmVjYXVzZSBhbGwtcmVkdWNlIGlzIGZhc3QgcmVsYXRpdmUgdG8gY29tcHV0ZS4gQmV5b25kIFRQPTgsIGNvbXB1dGUgYmVjb21lcyB0b28gc21hbGwgcGVyIEdQVSBhbmQgYWxsLXJlZHVjZSBvdmVyaGVhZCBiZWdpbnMgdG8gZG9taW5hdGUgZXZlbiBvbiBOVkxpbmsuIEZvciBQQ0llIHN5c3RlbXMsIGVmZmljaWVuY3kgZGVncmFkZXMgcmFwaWRseTogVFA9NCBvbiBQQ0llIG1heSB5aWVsZCBvbmx5IDIuMOKAkzIuNXggc3BlZWR1cCBpbnN0ZWFkIG9mIHRoZSB0aGVvcmV0aWNhbCA0eCwgd2l0aCBhbGwtcmVkdWNlIGNvbnN1bWluZyAzMOKAkzUwJSBvZiBlYWNoIGZvcndhcmQgcGFzcyB0aW1lLiBUaGlzIGlzIHdoeSBOVklESUEgREdYIHN5c3RlbXMgcGFpciBoaWdoLWJhbmR3aWR0aCBOVkxpbmsgd2l0aGluIGEgbm9kZSB3aXRoIHNsb3dlciBJbmZpbmlCYW5kIGJldHdlZW4gbm9kZXM6IHRlbnNvciBwYXJhbGxlbGlzbSBzaG91bGQgc3RheSB3aXRoaW4gTlZMaW5rLWNvbm5lY3RlZCBHUFVzLCB3aGlsZSBwaXBlbGluZSBvciBkYXRhIHBhcmFsbGVsaXNtIHNwYW5zIG5vZGVzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJUUCBEZWdyZWUiLCJMYXRlbmN5IChtcy90b2tlbikiLCJUaHJvdWdocHV0ICh0b2svcykiLCJHUFUgTWVtb3J5IHBlciBHUFUiLCJBbGwtUmVkdWNlIENvc3QgKE5WTGluaykiXSwicm93cyI6W1siVFA9MSAoc2luZ2xlIEdQVSkiLCI0MOKAkzYwIG1zIiwiMTjigJMyNSB0b2svcyIsIjE0MCBHQiAoT09NIGZvciA3MEIpIiwiTi9BIl0sWyJUUD0yIiwiMjLigJMzMiBtcyIsIjMw4oCTNDUgdG9rL3MiLCI3MCBHQiIsIn4wLjA1IG1zIChuZWdsaWdpYmxlKSJdLFsiVFA9NCIsIjEz4oCTMTggbXMiLCI1NeKAkzc1IHRvay9zIiwiMzUgR0IiLCJ+MC4wOCBtcyAobmVnbGlnaWJsZSkiXSxbIlRQPTgiLCI54oCTMTMgbXMiLCI3NeKAkzEwMCB0b2svcyIsIjE4IEdCIiwifjAuMTIgbXMgKHN0aWxsIHNtYWxsKSJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ3YXJuaW5nIiwidGl0bGUiOiJOVkxpbmsgUmVxdWlyZWQgZm9yIFRQIFx1MDAzZSAyIiwiY29udGVudCI6IlRlbnNvciBwYXJhbGxlbGlzbSByZXF1aXJlcyBhbiBhbGwtcmVkdWNlIGFmdGVyIGV2ZXJ5IHRyYW5zZm9ybWVyIGxheWVyIOKAlCBvbiBQQ0llLWNvbm5lY3RlZCBHUFVzIHRoaXMgYmVjb21lcyB0aGUgYm90dGxlbmVjayBhdCBiYXRjaCBzaXplIDEuIFBDSWUgYmFuZHdpZHRoIG9mIDE24oCTMzIgR0IvcyBtZWFucyBhIDUwMCBNQiBhY3RpdmF0aW9uIGFsbC1yZWR1Y2UgdGFrZXMgMTXigJMzMCBtcywgY29tcGFyYWJsZSB0byBvciBleGNlZWRpbmcgdGhlIGNvbXB1dGUgdGltZS4gVXNlIE5WTGluayBvciBhdm9pZCBUUFx1MDAzZTIgd2l0aG91dCBoaWdoLWJhbmR3aWR0aCBpbnRlcmNvbm5lY3RzOyBwcmVmZXIgcGlwZWxpbmUgcGFyYWxsZWxpc20gZm9yIFBDSWUgbXVsdGktR1BVIGluZmVyZW5jZS4ifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJUZW5zb3IgcGFyYWxsZWxpc20gc2hhcmRzIHdlaWdodCBtYXRyaWNlcyB3aXRoaW4gZWFjaCBsYXllciBhY3Jvc3MgR1BVcywgZW5hYmxpbmcgbW9kZWxzIGxhcmdlciB0aGFuIGEgc2luZ2xlIEdQVVx1MDAyN3MgbWVtb3J5IHRvIGJlIHNlcnZlZCB3aGlsZSBtYWludGFpbmluZyBsb3cgbGF0ZW5jeS4iLCJNZWdhdHJvbi1MTVx1MDAyN3MgY29sdW1uLXRoZW4tcm93IHBhdHRlcm4gbWluaW1pemVzIHN5bmNocm9uaXphdGlvbjogb25seSAyIGFsbC1yZWR1Y2VzIHBlciB0cmFuc2Zvcm1lciBsYXllciByZWdhcmRsZXNzIG9mIFRQIGRlZ3JlZS4iLCJGb3IgTUhBIGxheWVycywgVFAgZGVncmVlIE4gbXVzdCBkaXZpZGUgdGhlIG51bWJlciBvZiBLViBoZWFkcyDigJQgR1FBIG1vZGVscyB3aXRoIDggS1YgaGVhZHMgY2Fubm90IGV4Y2VlZCBUUD04LiIsIk5WTGluayBiYW5kd2lkdGggKDYwMCBHQi9zIG9uIEgxMDApIG1ha2VzIGFsbC1yZWR1Y2UgY29zdCBuZWdsaWdpYmxlIHRocm91Z2ggVFA9ODsgUENJZSBiYW5kd2lkdGggKDMyIEdCL3MpIG1ha2VzIFRQXHUwMDNlMiBpbmVmZmljaWVudCBmb3IgbGF0ZW5jeS1zZW5zaXRpdmUgd29ya2xvYWRzLiIsInZMTE0gZXhwb3NlcyBUUCB2aWEgdGVuc29yX3BhcmFsbGVsX3NpemU7IGJvdGggd2VpZ2h0cyBhbmQgUGFnZWRBdHRlbnRpb24gS1YgY2FjaGUgcGFnZXMgYXJlIHNoYXJkZWQgYWNyb3NzIEdQVXMgYXV0b21hdGljYWxseS4iLCJGb3IgYSA3MEIgbW9kZWwgb24gNHggSDEwMCAoTlZMaW5rKSwgZXhwZWN0IDMuMOKAkzMuNXggdGhyb3VnaHB1dCBpbXByb3ZlbWVudCB2cyAyeCBIMTAwLCBhbmQgNuKAkzh4IHZzIHNpbmdsZSBBMTAwIChPT00pLiIsIlByZWZlciBwaXBlbGluZSBwYXJhbGxlbGlzbSBmb3IgUENJZSBtdWx0aS1ub2RlIHNldHVwcyBhbmQgdGVuc29yIHBhcmFsbGVsaXNtIGZvciBOVkxpbmsgaW50cmEtbm9kZSBHUFUgY2x1c3RlcnMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Tensor Parallelism for LLM Inference

Tensor parallelism (TP) shards individual weight matrices across multiple GPUs, allowing each GPU to hold only a fraction of the parameters while collectively computing the full forward pass. Unlike pipeline parallelism (which splits the model layer-by-layer across GPUs with sequential execution) or data parallelism (which replicates the model and splits the batch), tensor parallelism splits the computation within each layer and requires synchronization within every transformer block. Megatron-LM (Shoeybi et al., 2019) introduced the canonical column-then-row parallelism pattern for transformer feed-forward and attention layers that is now implemented by virtually every production LLM inference framework including vLLM, TGI, and TensorRT-LLM.

## Overview

A 70B parameter LLM in float16 requires 140 GB of GPU memory — far exceeding a single A100 (80 GB) or H100 (80 GB). Tensor parallelism across N GPUs reduces per-GPU memory to roughly 140/N GB for model weights, plus the per-GPU KV cache and activation memory. With TP=2 across two H100s, the 70B model fits comfortably with room for long-context KV caches. The cost of TP is all-reduce communication: after each column-parallel or row-parallel layer, GPUs must synchronize partial results. On NVLink-connected GPUs (e.g., A100 NVLink with 600 GB/s bidirectional bandwidth), all-reduce for typical activation sizes takes under 0.1 ms and is negligible relative to compute time. On PCIe-connected GPUs (16 GB/s bidirectional), the same all-reduce can take 5–20 ms — potentially dominating the per-layer compute time at batch size 1.

## Column and Row Parallelism

Megatron-LM's tensor parallelism uses two complementary partitioning strategies for linear layers Y = XW + b. In column parallelism, the weight matrix W ∈ ℝ^(in × out) is split along the output (column) dimension: W = [W_1 | W_2 | ... | W_N] where each W_i ∈ ℝ^(in × out/N) lives on GPU i. Each GPU computes Y_i = X W_i (a partial output), then an all-gather across GPUs assembles the full Y. In row parallelism, the input X is split along the feature dimension: each GPU i receives X_i (a fraction of the input) and computes partial Y_i = X_i W. An all-reduce sum combines the partial outputs into the final Y, which is identical on all GPUs after reduction. The key insight of Megatron's design is to chain column-parallel → activation → row-parallel without an intermediate all-gather: the column-parallel output Y_i feeds directly into row-parallel as the sharded input X_i, requiring only one all-reduce at the end of the two-layer block.

```python
import torch
import torch.nn as nn
import torch.distributed as dist
import torch.nn.functional as F
from typing import Optional

class ColumnParallelLinear(nn.Module):
    """Split weight W along output dim; each GPU holds out/N columns; all-gather results."""
    def __init__(self, in_features: int, out_features: int, world_size: int, bias: bool = True):
        super().__init__()
        assert out_features % world_size == 0, "out_features must be divisible by world_size"
        self.out_per_rank = out_features // world_size
        self.world_size = world_size
        # Each GPU stores a (out/N, in) weight slice
        self.weight = nn.Parameter(torch.empty(self.out_per_rank, in_features))
        self.bias = nn.Parameter(torch.zeros(self.out_per_rank)) if bias else None
        nn.init.kaiming_uniform_(self.weight, a=5 ** 0.5)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Local matmul: (batch, in) @ (in, out/N).T -> (batch, out/N)
        out = F.linear(x, self.weight, self.bias)
        # All-gather: concatenate partial outputs from all ranks -> (batch, out)
        gathered = [torch.zeros_like(out) for _ in range(self.world_size)]
        dist.all_gather(gathered, out)
        return torch.cat(gathered, dim=-1)

def verify_column_parallel(rank: int, world_size: int, in_f: int = 256, out_f: int = 512):
    """Verify ColumnParallelLinear matches single-GPU reference."""
    full_W = torch.randn(out_f, in_f).cuda()  # reference weight
    x = torch.randn(4, in_f).cuda()           # shared input (identical on all GPUs)
    ref = F.linear(x, full_W)                 # single-GPU reference
    layer = ColumnParallelLinear(in_f, out_f, world_size, bias=False).cuda()
    # Each rank gets its slice of the full weight
    slice_size = out_f // world_size
    layer.weight.data.copy_(full_W[rank * slice_size:(rank + 1) * slice_size])
    out = layer(x)
    print(f"Rank {rank}: max_diff={((out - ref).abs().max()):.6f}")
```

## Megatron-LM Style Splitting

Megatron-LM's key contribution is identifying the exact placement of column-parallel and row-parallel layers in a transformer block that minimizes the number of all-reduce operations. For the MLP sub-block (two linear layers: W1 and W2), column parallelism is applied to W1 (splitting the output/hidden dimension) and row parallelism to W2 (splitting the input/hidden dimension). This means W1's partial outputs Y1_i = X W1_i are already split along the correct dimension to serve as the row-parallel input to W2, so no intermediate all-gather is needed between W1 and W2. Only one all-reduce is needed at the output of W2 per MLP block. For the attention sub-block, the Q, K, V projections are column-parallel (split along the head dimension, effectively sharding attention heads across GPUs), and the output projection is row-parallel. One all-reduce is needed per attention block. The total synchronization cost for a transformer layer is therefore 2 all-reduces: one after attention, one after MLP.

```python
import torch
import torch.nn as nn
import torch.distributed as dist
import torch.nn.functional as F

class RowParallelLinear(nn.Module):
    """Split input X along feature dim; each GPU computes partial XW; all-reduce sums."""
    def __init__(self, in_features: int, out_features: int, world_size: int, rank: int):
        super().__init__()
        assert in_features % world_size == 0
        self.in_per_rank = in_features // world_size
        self.rank = rank
        self.world_size = world_size
        # Each GPU stores a column slice of W: (out_features, in/N)
        self.weight = nn.Parameter(torch.empty(out_features, self.in_per_rank))
        nn.init.kaiming_uniform_(self.weight, a=5 ** 0.5)

    def forward(self, x_local: torch.Tensor) -> torch.Tensor:
        """x_local is already the rank-local shard: (batch, in/N)."""
        partial = F.linear(x_local, self.weight)  # (batch, out_features)
        dist.all_reduce(partial, op=dist.ReduceOp.SUM)  # sum across all GPUs
        return partial  # result is identical on all ranks

# Pattern guide: when to use column vs row parallel
print("Megatron TP pattern for MLP block:")
print("  Layer 1 (W1): ColumnParallel  — split output dim, no sync needed")
print("  Activation:   Local GELU/SiLU — no communication")
print("  Layer 2 (W2): RowParallel     — split input dim, 1 all-reduce at output")
print("")
print("Megatron TP pattern for Attention block:")
print("  Q, K, V proj: ColumnParallel  — shard along head dimension")
print("  Attention:    Local per-rank  — each rank handles its head slice")
print("  Out proj:     RowParallel     — 1 all-reduce at output")
print("")
print("Total: 2 all-reduces per transformer layer regardless of TP degree.")
```

## Attention Head Sharding

For multi-head attention (MHA) with H heads and head dimension d_k, tensor parallelism over N GPUs assigns H/N heads to each GPU. Each GPU computes full self-attention for its subset of heads using the full input sequence — Q, K, V projections are column-parallel (each GPU generates Q_i, K_i, V_i for its heads), attention scores are computed locally, and the output projection is row-parallel. This head-level sharding requires that H is divisible by N: for a 32-head model with TP=4, each GPU handles 8 heads. For grouped-query attention (GQA) or multi-query attention (MQA), which have fewer KV heads than query heads, the KV heads must also be divisible by N. Models with very few KV heads (e.g., 8 KV heads in LLaMA-3-70B) limit practical TP degree to 8; going to TP=16 with fewer than 16 KV heads is not possible without replicating KV heads.

## All-Reduce Communication

All-reduce is a collective operation that sums (or takes max/min of) tensors from all participating ranks and distributes the result to every rank. NCCL (NVIDIA Collective Communications Library) implements all-reduce using a ring algorithm: each GPU sends and receives data in a ring topology, requiring 2 * (N-1)/N data passes. For NVLink-connected GPUs (A100/H100 with 600 GB/s bidirectional NVLink bandwidth), a 1MB all-reduce completes in under 10 microseconds. For PCIe-connected GPUs (typically 16–32 GB/s PCIe 4.0 bandwidth), the same 1MB all-reduce takes 200–500 microseconds — slower by a factor of 20–50. Activation tensors in a 70B model forward pass are typically 0.5–4 MB per all-reduce call, making NVLink essentially free while PCIe all-reduces dominate inference latency at small batch sizes.

```python
import torch
import time
from vllm import LLM, SamplingParams

def benchmark_tensor_parallel_vllm(
    model_name: str = "meta-llama/Llama-2-70b-hf",
    tp_sizes: list = [2, 4]
) -> dict:
    """Measure vLLM throughput at different tensor-parallel degrees."""
    prompts = ["Explain the theory of general relativity from first principles."] * 32
    params = SamplingParams(temperature=0.0, max_tokens=256)
    results = {}
    for tp in tp_sizes:
        if torch.cuda.device_count() < tp:
            print(f"Skipping TP={tp}: only {torch.cuda.device_count()} GPU(s) available")
            continue
        llm = LLM(model=model_name, tensor_parallel_size=tp,
                  dtype="float16", gpu_memory_utilization=0.85)
        # Confirm memory distribution across GPUs
        for i in range(tp):
            mem_gb = torch.cuda.memory_allocated(i) / 1e9
            print(f"  TP={tp} | GPU {i}: {mem_gb:.1f} GB allocated")
        t0 = time.perf_counter()
        outputs = llm.generate(prompts, params)
        elapsed = time.perf_counter() - t0
        tokens_out = sum(len(o.outputs[0].token_ids) for o in outputs)
        tput = tokens_out / elapsed
        latency_ms = elapsed / len(prompts) * 1000
        results[tp] = {"throughput_tps": tput, "latency_ms": latency_ms}
        print(f"TP={tp}: {tput:.0f} tok/s  {latency_ms:.0f} ms/req")
        del llm
    return results
```

## vLLM Tensor Parallelism

vLLM implements tensor parallelism using PyTorch's distributed backend (typically NCCL) and exposes it via a single configuration parameter: tensor_parallel_size. Internally, vLLM uses Megatron-style column-then-row splitting for MLP layers and head sharding for attention. The model weights are loaded once by rank 0 and broadcast to other ranks during initialization. vLLM's PagedAttention KV cache is also sharded: each GPU stores the KV cache only for the attention heads it owns. For a 70B model on 4 H100s, each GPU holds ~17.5B parameters worth of weights and 25% of the KV cache pages. This combined weight + KV sharding is what makes vLLM memory-efficient at high TP degrees. The async_engine mode (default for production) overlaps communication with computation using CUDA streams, further hiding all-reduce latency.

```python
import torch
import torch.distributed as dist
import time
from typing import List, Dict

def profile_allreduce_latency(
    tensor_sizes_mb: List[float] = [1, 10, 50, 100, 500, 1000],
    n_warmup: int = 5,
    n_bench: int = 20
) -> Dict[float, dict]:
    """Benchmark NCCL all-reduce latency for tensors ranging 1MB to 1GB."""
    assert dist.is_initialized(), "Call dist.init_process_group('nccl') first."
    results = {}
    for size_mb in tensor_sizes_mb:
        n_elements = int(size_mb * 1e6 / 4)  # float32: 4 bytes/element
        tensor = torch.rand(n_elements, device="cuda")
        for _ in range(n_warmup):
            dist.all_reduce(tensor, op=dist.ReduceOp.SUM)
        torch.cuda.synchronize()
        t0 = time.perf_counter()
        for _ in range(n_bench):
            dist.all_reduce(tensor, op=dist.ReduceOp.SUM)
        torch.cuda.synchronize()
        lat_ms = (time.perf_counter() - t0) / n_bench * 1000
        # Effective bandwidth: ring all-reduce sends 2*(N-1)/N * data
        world = dist.get_world_size()
        effective_bytes = 2 * (world - 1) / world * size_mb * 1e6
        bw_gbps = (effective_bytes / 1e9) / (lat_ms / 1000)
        results[size_mb] = {"latency_ms": lat_ms, "bandwidth_gbps": bw_gbps}
        print(f"{size_mb:6.0f} MB  |  {lat_ms:.3f} ms  |  {bw_gbps:.1f} GB/s")
    return results
```

## Scaling Efficiency

Tensor parallelism scaling efficiency — the fraction of ideal linear speedup achieved as TP degree increases — degrades as N grows because all-reduce overhead grows with N while per-GPU compute shrinks. For NVLink systems, efficiency remains above 90% through TP=8 for 70B models because all-reduce is fast relative to compute. Beyond TP=8, compute becomes too small per GPU and all-reduce overhead begins to dominate even on NVLink. For PCIe systems, efficiency degrades rapidly: TP=4 on PCIe may yield only 2.0–2.5x speedup instead of the theoretical 4x, with all-reduce consuming 30–50% of each forward pass time. This is why NVIDIA DGX systems pair high-bandwidth NVLink within a node with slower InfiniBand between nodes: tensor parallelism should stay within NVLink-connected GPUs, while pipeline or data parallelism spans nodes.

| TP Degree | Latency (ms/token) | Throughput (tok/s) | GPU Memory per GPU | All-Reduce Cost (NVLink) |
| --- | --- | --- | --- | --- |
| TP=1 (single GPU) | 40–60 ms | 18–25 tok/s | 140 GB (OOM for 70B) | N/A |
| TP=2 | 22–32 ms | 30–45 tok/s | 70 GB | ~0.05 ms (negligible) |
| TP=4 | 13–18 ms | 55–75 tok/s | 35 GB | ~0.08 ms (negligible) |
| TP=8 | 9–13 ms | 75–100 tok/s | 18 GB | ~0.12 ms (still small) |

> **NVLink Required for TP > 2**: Tensor parallelism requires an all-reduce after every transformer layer — on PCIe-connected GPUs this becomes the bottleneck at batch size 1. PCIe bandwidth of 16–32 GB/s means a 500 MB activation all-reduce takes 15–30 ms, comparable to or exceeding the compute time. Use NVLink or avoid TP>2 without high-bandwidth interconnects; prefer pipeline parallelism for PCIe multi-GPU inference.

## Key Takeaways

- Tensor parallelism shards weight matrices within each layer across GPUs, enabling models larger than a single GPU's memory to be served while maintaining low latency.
- Megatron-LM's column-then-row pattern minimizes synchronization: only 2 all-reduces per transformer layer regardless of TP degree.
- For MHA layers, TP degree N must divide the number of KV heads — GQA models with 8 KV heads cannot exceed TP=8.
- NVLink bandwidth (600 GB/s on H100) makes all-reduce cost negligible through TP=8; PCIe bandwidth (32 GB/s) makes TP>2 inefficient for latency-sensitive workloads.
- vLLM exposes TP via tensor_parallel_size; both weights and PagedAttention KV cache pages are sharded across GPUs automatically.
- For a 70B model on 4x H100 (NVLink), expect 3.0–3.5x throughput improvement vs 2x H100, and 6–8x vs single A100 (OOM).
- Prefer pipeline parallelism for PCIe multi-node setups and tensor parallelism for NVLink intra-node GPU clusters.

---

