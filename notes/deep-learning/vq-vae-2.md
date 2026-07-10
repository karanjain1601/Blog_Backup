---
title: "VQ-VAE-2 — Hierarchical Discrete Latents for High-Resolution Generation"
slug: "vq-vae-2"
description: "VQ-VAE-2 extends vector-quantized autoencoders to 256x256 generation via two hierarchical codebook levels: an 8x8 top level capturing global structure and a 32x32 bottom level capturing local details, with bottom encoding conditioned on top codes and a two-stage PixelSnail prior for high-fidelity class-conditional generation."
tags: ["deep-learning", "generative-models"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVlEtVkFFLTIgKFJhemF2aSBldCBhbC4gMjAxOSkgZXh0ZW5kcyB0aGUgb3JpZ2luYWwgVlEtVkFFIHRvIGhpZ2gtcmVzb2x1dGlvbiBpbWFnZSBzeW50aGVzaXMgYnkgaW50cm9kdWNpbmcgYSBoaWVyYXJjaHkgb2YgZGlzY3JldGUgbGF0ZW50IGNvZGVzLiBBIHNpbmdsZSBjb2RlYm9vayBhdCBvbmUgcmVzb2x1dGlvbiBjYW5ub3Qgc2ltdWx0YW5lb3VzbHkgY2FwdHVyZSBib3RoIGdsb2JhbCBpbWFnZSBzdHJ1Y3R1cmUgKG9iamVjdCBsYXlvdXQsIGNvbG91ciBwYWxldHRlKSBhbmQgbG9jYWwgZmluZSBkZXRhaWxzICh0ZXh0dXJlcywgZWRnZXMpLiBUd28gbGV2ZWxzIHNvbHZlIHRoaXM6IGEgdG9wIGxldmVsIGF0IDh4OCBlbmNvZGVzIGNvYXJzZSBnbG9iYWwgaW5mb3JtYXRpb24sIGFuZCBhIGJvdHRvbSBsZXZlbCBhdCAzMngzMiBlbmNvZGVzIGxvY2FsIGRldGFpbCBjb25kaXRpb25lZCBvbiB0aGUgYWxyZWFkeS1xdWFudGl6ZWQgdG9wIHJlcHJlc2VudGF0aW9uLiBUaGUgcmVzdWx0IGlzIDI1NngyNTYgY2xhc3MtY29uZGl0aW9uYWwgZ2VuZXJhdGlvbiBhdCBGSUQgfjIuNSBvbiBJbWFnZU5ldCDigJQgY29tcGV0aXRpdmUgd2l0aCBCaWdHQU4gYXQgdGhlIHRpbWUg4oCUIHVzaW5nIGEgdHdvLXN0YWdlIGRpc2NyZXRlIGF1dG9yZWdyZXNzaXZlIHByaW9yLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkludHJvZHVjdGlvbjogSGllcmFyY2hpY2FsIE1vdGl2YXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBvcmlnaW5hbCBWUS1WQUUgdXNlZCBhIHNpbmdsZS1sZXZlbCBjb2RlYm9vayBhbmQgd2FzIGxpbWl0ZWQgdG8gMzJ4MzIgb3IgNjR4NjQgZ2VuZXJhdGlvbi4gU2NhbGluZyB0byAyNTZ4MjU2IHdpdGggb25lIGNvZGVib29rIGZvcmNlcyBhIHRyYWRlb2ZmOiBhIGxhcmdlIHNwYXRpYWwgZ3JpZCBwcmVzZXJ2ZXMgbG9jYWwgZGV0YWlsIGJ1dCB0aGUgY29kZWJvb2sgbXVzdCBzcGFuIHRoZSBlbnRpcmUgc3BhY2Ugb2YgaW1hZ2UgcGF0Y2hlczsgYSBzbWFsbCBncmlkIGxvc2VzIHNwYXRpYWwgcmVzb2x1dGlvbi4gSGllcmFyY2hpY2FsIHJlcHJlc2VudGF0aW9uIHNvbHZlcyB0aGlzIGJ5IGZhY3RvcmlzaW5nIGltYWdlIGluZm9ybWF0aW9uIGFjcm9zcyBsZXZlbHMuIFRoZSB0b3AgbGV2ZWwgbmVlZCBvbmx5IGRlc2NyaWJlIHNjZW5lLWxldmVsIHN0cnVjdHVyZSDigJQgd2hpY2ggcmVnaW9ucyBjb250YWluIGZvcmVncm91bmQgb2JqZWN0cywgYXBwcm94aW1hdGUgY29sb3VyIGRpc3RyaWJ1dGlvbiwgZG9taW5hbnQgc2hhcGVzIOKAlCB3aGlsZSB0aGUgYm90dG9tIGxldmVsIGZpbGxzIGluIGxvY2FsIHRleHR1cmUgY29uZGl0aW9uZWQgb24gdGhhdCBnbG9iYWwgY29udGV4dC4gVGhpcyBtaXJyb3JzIGhvdyBodW1hbnMgcGVyY2VpdmUgaW1hZ2VzOiBnbG9iYWwgc2NlbmUgdW5kZXJzdGFuZGluZyBwcmVjZWRlcyBsb2NhbCBkZXRhaWwuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVHdvLUxldmVsIEFyY2hpdGVjdHVyZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIFZRLVZBRS0yIGVuY29kZXItZGVjb2RlciBwYWlyIGhhcyB0d28gcXVhbnRpemF0aW9uIHN0YWdlcyB3aXRoIHNlcGFyYXRlIGNvZGVib29rcy4gVGhlIGJvdHRvbSBlbmNvZGVyIG1hcHMgMjU2eDI1NiBpbWFnZXMgdG8gMzJ4MzIgZmVhdHVyZSBtYXBzIGNhcHR1cmluZyBsb2NhbCBkZXRhaWwuIFRoZSB0b3AgZW5jb2RlciBmdXJ0aGVyIGNvbXByZXNzZXMgMzJ4MzIgZmVhdHVyZXMgdG8gOHg4LCBjYXB0dXJpbmcgZ2xvYmFsIHN0cnVjdHVyZS4gRWFjaCBsZXZlbCBoYXMgaXRzIG93biBjb2RlYm9vayAodHlwaWNhbGx5IDUxMiBlbnRyaWVzIGVhY2gsIGVtYmVkZGluZyBkaW1lbnNpb24gNjQpLiBEdXJpbmcgZW5jb2RpbmcsIHRvcCBmZWF0dXJlcyBhcmUgcXVhbnRpemVkIGZpcnN0OyB0aGUgcXVhbnRpemVkIHRvcCBjb2RlcyBhcmUgdGhlbiB1cHNhbXBsZWQgYW5kIGNvbmNhdGVuYXRlZCB0byB0aGUgYm90dG9tIGZlYXR1cmVzIGJlZm9yZSBib3R0b20gcXVhbnRpemF0aW9uLCBzbyB0aGUgYm90dG9tIGNvZGVib29rIG9ubHkgbmVlZHMgdG8gcmVwcmVzZW50IHJlc2lkdWFsIGxvY2FsIGluZm9ybWF0aW9uIG5vdCBhbHJlYWR5IGV4cGxhaW5lZCBieSB0aGUgdG9wLiBUaGUgZGVjb2RlciByZXZlcnNlcyB0aGlzIHByb2Nlc3MgdG9wLWRvd24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIFZlY3RvclF1YW50aXplKG5uLk1vZHVsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNvZGVib29rX3NpemU9NTEyLCBlbWJlZF9kaW09NjQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5jb2RlYm9vayA9IG5uLkVtYmVkZGluZyhjb2RlYm9va19zaXplLCBlbWJlZF9kaW0pXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB6KTpcbiAgICAgICAgQiwgQywgSCwgVyA9IHouc2hhcGVcbiAgICAgICAgel9mbGF0ID0gei5wZXJtdXRlKDAsIDIsIDMsIDEpLnJlc2hhcGUoLTEsIEMpXG4gICAgICAgIGRpc3QgPSAoel9mbGF0LnVuc3F1ZWV6ZSgxKSAtIHNlbGYuY29kZWJvb2sud2VpZ2h0LnVuc3F1ZWV6ZSgwKSkucG93KDIpLnN1bSgtMSlcbiAgICAgICAgaW5kaWNlcyA9IGRpc3QuYXJnbWluKGRpbT0xKVxuICAgICAgICB6X3EgPSBzZWxmLmNvZGVib29rKGluZGljZXMpLnJlc2hhcGUoQiwgSCwgVywgQykucGVybXV0ZSgwLCAzLCAxLCAyKVxuICAgICAgICB6X3EgPSB6ICsgKHpfcSAtIHopLmRldGFjaCgpICAgIyBzdHJhaWdodC10aHJvdWdoIGVzdGltYXRvclxuICAgICAgICByZXR1cm4gel9xLCBpbmRpY2VzLnJlc2hhcGUoQiwgSCwgVylcblxuY2xhc3MgSGllcmFyY2hpY2FsVlFWQUUobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2g9MywgaGlkZGVuPTEyOCwgY29kZWJvb2tfc2l6ZT01MTIsIGVtYmVkX2RpbT02NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLmJvdHRvbV9lbmMgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoLCBoaWRkZW4sIDQsIDIsIDEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQoaGlkZGVuLCBoaWRkZW4sIDQsIDIsIDEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQoaGlkZGVuLCBoaWRkZW4sIDQsIDIsIDEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5Db252MmQoaGlkZGVuLCBlbWJlZF9kaW0sIDEpICAgICAgICAjIDI1Ni1cdTAwM2UzMiAoMyBzdHJpZGVzIG9mIDIpXG4gICAgICAgIClcbiAgICAgICAgc2VsZi50b3BfZW5jID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChlbWJlZF9kaW0sIGhpZGRlbiwgNCwgMiwgMSksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChoaWRkZW4sIGhpZGRlbiwgNCwgMiwgMSksIG5uLlJlTFUoKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChoaWRkZW4sIGVtYmVkX2RpbSwgMSkgICAgICAgICMgMzItXHUwMDNlOCAoMiBzdHJpZGVzIG9mIDIpXG4gICAgICAgIClcbiAgICAgICAgc2VsZi52cV90b3AgICAgPSBWZWN0b3JRdWFudGl6ZShjb2RlYm9va19zaXplLCBlbWJlZF9kaW0pXG4gICAgICAgIHNlbGYudnFfYm90dG9tID0gVmVjdG9yUXVhbnRpemUoY29kZWJvb2tfc2l6ZSwgZW1iZWRfZGltKVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxubW9kZWwgPSBIaWVyYXJjaGljYWxWUVZBRSgpXG54ID0gdG9yY2gucmFuZG4oMiwgMywgMjU2LCAyNTYpXG5iX2ZlYXQgPSBtb2RlbC5ib3R0b21fZW5jKHgpICAgICAgICAjICgyLCA2NCwgMzIsIDMyKVxudF9mZWF0ID0gbW9kZWwudG9wX2VuYyhiX2ZlYXQpICAgICAgIyAoMiwgNjQsICA4LCAgOClcbnRfcSwgdF9pZHggPSBtb2RlbC52cV90b3AodF9mZWF0KVxucHJpbnQoZlx1MDAyN1RvcCBxdWFudGl6ZWQ6IHt0X3Euc2hhcGV9LCBpbmRpY2VzOiB7dF9pZHguc2hhcGV9XHUwMDI3KSAgIyAoMiw2NCw4LDgpLCAoMiw4LDgpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiVG9wLUxldmVsIEVuY29kaW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgdG9wIGVuY29kZXIgdGFrZXMgdGhlIDMyeDMyIGJvdHRvbSBmZWF0dXJlIG1hcCBhcyBpbnB1dCBhbmQgYXBwbGllcyB0d28gZnVydGhlciBzdHJpZGUtMiBjb252b2x1dGlvbnMgdG8gcmVhY2ggOHg4LiBUaGlzIDh4OCB0b3AgcmVwcmVzZW50YXRpb24gaXMgcXVhbnRpemVkIGFnYWluc3QgdGhlIHRvcCBjb2RlYm9vayB1c2luZyBuZWFyZXN0LW5laWdoYm9yIGxvb2t1cCBpbiBlbWJlZGRpbmcgc3BhY2UgKDUxMiBlbnRyaWVzKS4gVGhlIHJlc3VsdCBpcyA2NCBkaXNjcmV0ZSB0b2tlbnMgcGVyIGltYWdlIOKAlCBlbm91Z2ggdG8gcmVwcmVzZW50IGNvYXJzZSBzZW1hbnRpYyBsYXlvdXQgd2l0aG91dCByZWR1bmRhbmN5LiBCZWNhdXNlIHRoZSB0b3AgY29kZWJvb2sgaXMgc21hbGwgKDh4OCA9IDY0IHRva2VucyksIFBpeGVsU25haWwgY2FuIG1vZGVsIGl0cyBwcmlvciBhdXRvcmVncmVzc2l2ZWx5IGluIHJlYXNvbmFibGUgdGltZTogYSA2NC10b2tlbiBzZXF1ZW5jZSBpcyB0cmFjdGFibGUgZm9yIGEgY29udm9sdXRpb25hbCBhdXRvcmVncmVzc2l2ZSBtb2RlbCB3aXRoIG1hc2tpbmcuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQm90dG9tLUxldmVsIENvbmRpdGlvbmluZyJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIGtleSBpbm5vdmF0aW9uIGluIFZRLVZBRS0yIGlzIHRoYXQgYm90dG9tIHF1YW50aXphdGlvbiBpcyBjb25kaXRpb25lZCBvbiB0aGUgdG9wIGNvZGVzLiBBZnRlciBjb21wdXRpbmcgdGhlIHRvcCBxdWFudGl6ZWQgY29kZXMgdF9xIGF0IDh4OCwgdGhleSBhcmUgdXBzYW1wbGVkICh2aWEgbmVhcmVzdC1uZWlnaGJvciBpbnRlcnBvbGF0aW9uKSB0byAzMngzMiBhbmQgY29uY2F0ZW5hdGVkIGNoYW5uZWwtd2lzZSB3aXRoIHRoZSByYXcgYm90dG9tIGVuY29kZXIgZmVhdHVyZXMuIEEgbGVhcm5lZCBwcm9qZWN0aW9uIHRoZW4gbWFwcyB0aGUgY29tYmluZWQgcmVwcmVzZW50YXRpb24gdG8gdGhlIGVtYmVkZGluZyBzcGFjZSBiZWZvcmUgYm90dG9tIFZRIGxvb2t1cC4gVGhpcyBtZWFucyB0aGUgYm90dG9tIGNvZGVib29rIG9ubHkgbmVlZHMgdG8gZW5jb2RlIHJlc2lkdWFsIGxvY2FsIGluZm9ybWF0aW9uIG5vdCBhbHJlYWR5IGNhcHR1cmVkIGJ5IHRoZSB0b3AgbGV2ZWwg4oCUIGEgbXVjaCBlYXNpZXIgdGFzayB0aGFuIGVuY29kaW5nIGV2ZXJ5dGhpbmcgZnJvbSBzY3JhdGNoLiBUaGUgYm90dG9tIGNvZGVzIGNhcnJ5IGxvY2FsIHRleHR1cmVzLCBlZGdlIG9yaWVudGF0aW9ucywgYW5kIGZpbmUgY29sb3VyIHZhcmlhdGlvbnMuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5cbmNsYXNzIEJvdHRvbUNvbmRpdGlvbmVkRW5jb2Rlcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkVuY29kZXMgYm90dG9tIGZlYXR1cmVzIGNvbmRpdGlvbmVkIG9uIHVwc2FtcGxlZCB0b3AgcXVhbnRpemVkIGNvZGVzLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBlbWJlZF9kaW09NjQsIGhpZGRlbj0xMjgpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5jb25kaXRpb25fcHJvaiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoZW1iZWRfZGltICogMiwgaGlkZGVuLCAzLCAxLCAxKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uQ29udjJkKGhpZGRlbiwgZW1iZWRfZGltLCAxKVxuICAgICAgICApXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCBib3R0b21fZmVhdCwgdG9wX3EpOlxuICAgICAgICAjIFVwc2FtcGxlIDh4OCB0b3AgY29kZXMgdG8gbWF0Y2ggMzJ4MzIgYm90dG9tIHJlc29sdXRpb25cbiAgICAgICAgdG9wX3VwID0gRi5pbnRlcnBvbGF0ZSh0b3BfcSwgc2l6ZT1ib3R0b21fZmVhdC5zaGFwZVstMjpdLCBtb2RlPVx1MDAyN25lYXJlc3RcdTAwMjcpXG4gICAgICAgIGNvbWJpbmVkID0gdG9yY2guY2F0KFtib3R0b21fZmVhdCwgdG9wX3VwXSwgZGltPTEpICAjIChCLCAyKkMsIDMyLCAzMilcbiAgICAgICAgcmV0dXJuIHNlbGYuY29uZGl0aW9uX3Byb2ooY29tYmluZWQpICAgICAgICAgICAgICAgICMgKEIsIEMsICAgMzIsIDMyKVxuXG50b3JjaC5tYW51YWxfc2VlZCgwKVxuZW5jICAgPSBCb3R0b21Db25kaXRpb25lZEVuY29kZXIoZW1iZWRfZGltPTY0LCBoaWRkZW49MTI4KVxuYl9yYXcgPSB0b3JjaC5yYW5kbigyLCA2NCwgMzIsIDMyKSAgIyByYXcgYm90dG9tIGVuY29kZXIgb3V0cHV0XG50X3EgICA9IHRvcmNoLnJhbmRuKDIsIDY0LCAgOCwgIDgpICAjIHF1YW50aXplZCB0b3AgY29kZXNcbmNvbmRpdGlvbmVkID0gZW5jKGJfcmF3LCB0X3EpICAgICAgICMgKDIsIDY0LCAzMiwgMzIpXG5wcmludChmXHUwMDI3Qm90dG9tIHJhdzogICAgICAge2JfcmF3LnNoYXBlfVx1MDAyNylcbnByaW50KGZcdTAwMjdUb3AgdXBzYW1wbGVkIHRvOiB7Ri5pbnRlcnBvbGF0ZSh0X3EsIHNpemU9KDMyLDMyKSkuc2hhcGV9XHUwMDI3KVxucHJpbnQoZlx1MDAyN0NvbmRpdGlvbmVkIGZlYXQ6IHtjb25kaXRpb25lZC5zaGFwZX1cdTAwMjcpICAjIHJlYWR5IGZvciBWUSBsb29rdXAifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJEZWNvZGVyIFBhdGgifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlRoZSBWUS1WQUUtMiBkZWNvZGVyIHJlY29uc3RydWN0cyBpbWFnZXMgdG9wLWRvd24uIFRoZSA4eDggdG9wIHF1YW50aXplZCBjb2RlcyBhcmUgZmlyc3QgZGVjb2RlZCBieSBhIHNtYWxsIG5ldHdvcmsgdGhhdCB1cHNhbXBsZXMgdGhlbSB0byAzMngzMiBmZWF0dXJlIG1hcHMuIFRoZXNlIGRlY29kZWQgdG9wIGZlYXR1cmVzIGFyZSB0aGVuIGNvbmNhdGVuYXRlZCB3aXRoIHRoZSAzMngzMiBib3R0b20gcXVhbnRpemVkIGNvZGVzLCBhbmQgYSBmaW5hbCBkZWNvZGVyIG5ldHdvcmsgdXBzYW1wbGVzIHRoZSBjb21iaW5lZCByZXByZXNlbnRhdGlvbiBmcm9tIDMyeDMyIGJhY2sgdG8gMjU2eDI1NiBSR0IuIFRoZSB0b3AtZGVjb2RlZCBmZWF0dXJlcyBwcm92aWRlIGdsb2JhbCBzdHJ1Y3R1cmUgZ3VpZGFuY2U7IHRoZSBib3R0b20gY29kZXMgaW5qZWN0IGxvY2FsIGRldGFpbC4gVGhpcyB0d28tcGF0aCBtZXJnZSBhbGxvd3MgdGhlIGRlY29kZXIgdG8gYmVuZWZpdCBmcm9tIGJvdGggbGV2ZWxzIG9mIGFic3RyYWN0aW9uIHNpbXVsdGFuZW91c2x5LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBUb3BEb3duRGVjb2Rlcihubi5Nb2R1bGUpOlxuICAgIFwiXCJcIkRlY29kZXM6IHRvcCBjb2RlcyAoOHg4KSAtXHUwMDNlIHVwc2FtcGxlIC1cdTAwM2UgbWVyZ2Ugd2l0aCBib3R0b20gY29kZXMgKDMyeDMyKSAtXHUwMDNlIGltYWdlLlwiXCJcIlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBlbWJlZF9kaW09NjQsIGhpZGRlbj0xMjgsIG91dF9jaD0zKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXygpXG4gICAgICAgIHNlbGYudG9wX2RlYyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoZW1iZWRfZGltLCBoaWRkZW4sIDMsIDEsIDEpLCBubi5SZUxVKCksXG4gICAgICAgICAgICBubi5VcHNhbXBsZShzY2FsZV9mYWN0b3I9NCwgbW9kZT1cdTAwMjduZWFyZXN0XHUwMDI3KSwgICMgOHg4ICAtXHUwMDNlIDMyeDMyXG4gICAgICAgICAgICBubi5Db252MmQoaGlkZGVuLCBlbWJlZF9kaW0sIDMsIDEsIDEpLCBubi5SZUxVKClcbiAgICAgICAgKVxuICAgICAgICBzZWxmLmZpbmFsX2RlYyA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoZW1iZWRfZGltICogMiwgaGlkZGVuLCAzLCAxLCAxKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uVXBzYW1wbGUoc2NhbGVfZmFjdG9yPTQsIG1vZGU9XHUwMDI3bmVhcmVzdFx1MDAyNyksICAjIDMyeDMyIC1cdTAwM2UgMTI4eDEyOFxuICAgICAgICAgICAgbm4uQ29udjJkKGhpZGRlbiwgaGlkZGVuLCAzLCAxLCAxKSwgbm4uUmVMVSgpLFxuICAgICAgICAgICAgbm4uVXBzYW1wbGUoc2NhbGVfZmFjdG9yPTIsIG1vZGU9XHUwMDI3bmVhcmVzdFx1MDAyNyksICAjIDEyOHgxMjggLVx1MDAzZSAyNTZ4MjU2XG4gICAgICAgICAgICBubi5Db252MmQoaGlkZGVuLCBvdXRfY2gsIDMsIDEsIDEpLCBubi5UYW5oKClcbiAgICAgICAgKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgdG9wX3EsIGJvdHRvbV9xKTpcbiAgICAgICAgdG9wX2RlY29kZWQgPSBzZWxmLnRvcF9kZWModG9wX3EpICAgICAgICAgICAgICAgICAgICAgICMgKEIsIEMsIDMyLCAzMilcbiAgICAgICAgY29tYmluZWQgICAgPSB0b3JjaC5jYXQoW3RvcF9kZWNvZGVkLCBib3R0b21fcV0sIGRpbT0xKSAjIChCLCAyQywgMzIsIDMyKVxuICAgICAgICByZXR1cm4gc2VsZi5maW5hbF9kZWMoY29tYmluZWQpICAgICAgICAgICAgICAgICAgICAgICAgIyAoQiwgMywgMjU2LCAyNTYpXG5cbnRvcmNoLm1hbnVhbF9zZWVkKDApXG5kZWNvZGVyICA9IFRvcERvd25EZWNvZGVyKClcbnRvcF9xICAgID0gdG9yY2gucmFuZG4oMiwgNjQsICA4LCAgOClcbmJvdHRvbV9xID0gdG9yY2gucmFuZG4oMiwgNjQsIDMyLCAzMilcbnJlY29uICAgID0gZGVjb2Rlcih0b3BfcSwgYm90dG9tX3EpXG5wcmludChmXHUwMDI3VG9wIGNvZGVzOiAgIHt0b3BfcS5zaGFwZX1cdTAwMjcpICAgICAjICgyLCA2NCwgOCwgOClcbnByaW50KGZcdTAwMjdCb3R0b20gY29kZXM6e2JvdHRvbV9xLnNoYXBlfVx1MDAyNykgICMgKDIsIDY0LCAzMiwgMzIpXG5wcmludChmXHUwMDI3UmVjb25zdHJ1Y3Rpb246IHtyZWNvbi5zaGFwZX1cdTAwMjcpICAjICgyLCAzLCAyNTYsIDI1NikifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJUd28tU3RhZ2UgUHJpb3IgTW9kZWxzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJHZW5lcmF0aW9uIHdpdGggVlEtVkFFLTIgcmVxdWlyZXMgc2FtcGxpbmcgZGlzY3JldGUgY29kZXMgYW5kIGRlY29kaW5nIHRoZW0g4oCUIHRoZSBWUS1WQUUgaXRzZWxmIHByb3ZpZGVzIG5vIGdlbmVyYXRpdmUgcHJpb3IuIFZRLVZBRS0yIHVzZXMgUGl4ZWxTbmFpbCwgYSBjb252b2x1dGlvbmFsIGF1dG9yZWdyZXNzaXZlIG1vZGVsIHdpdGggYXR0ZW50aW9uLCBhcyBhIHByaW9yIGF0IGVhY2ggbGV2ZWwuIFN0YWdlIDE6IGEgUGl4ZWxTbmFpbCB0b3AgcHJpb3IgbW9kZWxzIHAoel90b3AgfCBjbGFzcykgYXV0b3JlZ3Jlc3NpdmVseSBvdmVyIHRoZSA4eDggPSA2NCB0b3AgdG9rZW5zLiBTdGFnZSAyOiBhIGNvbmRpdGlvbmVkIFBpeGVsU25haWwgYm90dG9tIHByaW9yIG1vZGVscyBwKHpfYm90dG9tIHwgel90b3AsIGNsYXNzKSBhdXRvcmVncmVzc2l2ZWx5IG92ZXIgdGhlIDEwMjQgYm90dG9tIHRva2VucyBhdCAzMngzMiwgY29uZGl0aW9uZWQgb24gdGhlIGZ1bGx5IHNhbXBsZWQgdG9wIGNvZGVzLiBPbmNlIGJvdGggY29kZSBtYXBzIGFyZSBzYW1wbGVkLCB0aGUgVlEtVkFFLTIgZGVjb2RlciBwcm9kdWNlcyB0aGUgZmluYWwgMjU2eDI1NiBpbWFnZS4gVGhlIHR3by1zdGFnZSBhcHByb2FjaCBhbGxvd3MgdGhlIHRvcCBwcmlvciB0byBlc3RhYmxpc2ggZ2xvYmFsIGNvaGVyZW5jZSBiZWZvcmUgdGhlIGJvdHRvbSBwcmlvciBmaWxscyBpbiBsb2NhbCBkZXRhaWxzLiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVG9wIHByaW9yOiBQaXhlbFNuYWlsIG92ZXIgOHg4PTY0IGRpc2NyZXRlIHRva2VuczsgcmVjZXB0aXZlIGZpZWxkIGNvdmVycyB0aGUgZnVsbCA4eDggZ3JpZCB2aWEgZ2xvYmFsIHNlbGYtYXR0ZW50aW9uLiIsIkJvdHRvbSBwcmlvcjogY29uZGl0aW9uZWQgUGl4ZWxTbmFpbCBvdmVyIDMyeDMyPTEwMjQgdG9rZW5zOyB0b3AgY29kZXMgYXJlIGVtYmVkZGVkIGFuZCB1c2VkIGFzIGNvbnRleHQgdmlhIGNyb3NzLWF0dGVudGlvbi4iLCJTYW1wbGluZyBvcmRlcjogc2FtcGxlIGFsbCA2NCB0b3AgdG9rZW5zIGZpcnN0IChyb3ctbWFqb3IgYXV0b3JlZ3Jlc3NpdmUpLCB0aGVuIHNhbXBsZSBhbGwgMTAyNCBib3R0b20gdG9rZW5zIGNvbmRpdGlvbmVkIG9uIHNhbXBsZWQgdG9wLiIsIkNsYXNzIGNvbmRpdGlvbmluZzogY2xhc3MgbGFiZWwgZW1iZWRkaW5nIGlzIGFkZGVkIHRvIGJvdGggdG9wIGFuZCBib3R0b20gUGl4ZWxTbmFpbCBpbnB1dHMsIGVuYWJsaW5nIGNsYXNzLWNvbmRpdGlvbmFsIGdlbmVyYXRpb24uIiwiRklEIH4yLjUgb24gY2xhc3MtY29uZGl0aW9uYWwgSW1hZ2VOZXQgMjU2eDI1NiwgY29tcGV0aXRpdmUgd2l0aCBCaWdHQU4gd2hpbGUgdXNpbmcgYSBmdW5kYW1lbnRhbGx5IGRpZmZlcmVudCAobm9uLWFkdmVyc2FyaWFsKSB0cmFpbmluZyBvYmplY3RpdmUuIl19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlZRR0FOIGFuZCBCZXlvbmQifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlZRR0FOIChFc3NlciBldCBhbC4gMjAyMSkgdXBncmFkZXMgdGhlIFZRLVZBRSByZWNvbnN0cnVjdGlvbiBxdWFsaXR5IGJ5IGFkZGluZyBhIFBhdGNoR0FOIGFkdmVyc2FyaWFsIGRpc2NyaW1pbmF0b3IgYW5kIGEgVkdHIHBlcmNlcHR1YWwgbG9zcyB0byB0aGUgc3RhbmRhcmQgY29tbWl0bWVudCArIHJlY29uc3RydWN0aW9uIG9iamVjdGl2ZS4gVGhlIGRpc2NyaW1pbmF0b3IgcHVzaGVzIHRoZSBkZWNvZGVyIHRvIHByb2R1Y2UgcGVyY2VwdHVhbGx5IHNoYXJwIG91dHB1dHMgcmF0aGVyIHRoYW4gYmx1cnJ5IE1TRS1vcHRpbWFsIHJlY29uc3RydWN0aW9ucy4gQ3JpdGljYWxseSwgVlFHQU4gYWxzbyByZXBsYWNlcyBQaXhlbFNuYWlsIHdpdGggYSBHUFQtc3R5bGUgVHJhbnNmb3JtZXIgYXMgdGhlIHByaW9yIOKAlCB0aGUgZGlzY3JldGUgdG9rZW5zIHByb2R1Y2VkIGJ5IHRoZSBWUUdBTiBlbmNvZGVyIGJlY29tZSBhIHNlcXVlbmNlIG1vZGVsZWQgYnkgYSBjYXVzYWwgVHJhbnNmb3JtZXIsIGVuYWJsaW5nIG11Y2ggbG9uZ2VyLXJhbmdlIGRlcGVuZGVuY2llcy4gREFMTC1FIHYxIHVzZWQgZXhhY3RseSB0aGlzIGFyY2hpdGVjdHVyZTogYSBWUUdBTiB0b2tlbml6ZXIgKDI1NiBpbWFnZSB0b2tlbnMgYXQgMzJ4MzIgZnJvbSBhIDI1NngyNTYgaW1hZ2UpIHBhaXJlZCB3aXRoIGEgR1BULXN0eWxlIFRyYW5zZm9ybWVyIGNvbmRpdGlvbmVkIG9uIHRleHQgdG9rZW5zLiBNb2Rlcm4gc3lzdGVtcyBleHRlbmQgZnVydGhlcjogTUFHVklULXYyIHVzZXMgaW1wcm92ZWQgbG9va3VwLWZyZWUgcXVhbnRpemF0aW9uIGFuZCBhbiBMTE0tc3R5bGUgbWFza2VkIHByaW9yLCB3aGlsZSBMbGFtYUdlbiBhcHBsaWVzIExMYU1BLXN0eWxlIGF1dG9yZWdyZXNzaXZlIFRyYW5zZm9ybWVycyB0byBWUSBpbWFnZSB0b2tlbnMgd2l0aCBjb21wZXRpdGl2ZSBGSUQuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5pbXBvcnQgdG9yY2gubm4uZnVuY3Rpb25hbCBhcyBGXG5mcm9tIHRvcmNodmlzaW9uLm1vZGVscyBpbXBvcnQgdmdnMTZcblxuY2xhc3MgUGF0Y2hHQU5EaXNjcmltaW5hdG9yKG5uLk1vZHVsZSk6XG4gICAgXCJcIlwiNzB4NzAgUGF0Y2hHQU46IGNsYXNzaWZpZXMgb3ZlcmxhcHBpbmcgaW1hZ2UgcGF0Y2hlcyBhcyByZWFsL2Zha2UuXCJcIlwiXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoPTMsIG5kZj02NCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2gsICAgIG5kZiwgICA0LCAyLCAxKSwgbm4uTGVha3lSZUxVKDAuMiwgVHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQobmRmLCAgIG5kZioyLCA0LCAyLCAxLCBiaWFzPUZhbHNlKSwgbm4uQmF0Y2hOb3JtMmQobmRmKjIpLCBubi5MZWFreVJlTFUoMC4yLCBUcnVlKSxcbiAgICAgICAgICAgIG5uLkNvbnYyZChuZGYqMiwgbmRmKjQsIDQsIDIsIDEsIGJpYXM9RmFsc2UpLCBubi5CYXRjaE5vcm0yZChuZGYqNCksIG5uLkxlYWt5UmVMVSgwLjIsIFRydWUpLFxuICAgICAgICAgICAgbm4uQ29udjJkKG5kZio0LCBuZGYqOCwgNCwgMSwgMSwgYmlhcz1GYWxzZSksIG5uLkJhdGNoTm9ybTJkKG5kZio4KSwgbm4uTGVha3lSZUxVKDAuMiwgVHJ1ZSksXG4gICAgICAgICAgICBubi5Db252MmQobmRmKjgsIDEsIDQsIDEsIDEpICAjIHBhdGNoLWxldmVsIGxvZ2l0c1xuICAgICAgICApXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHJldHVybiBzZWxmLm5ldCh4KVxuXG5kZWYgcGVyY2VwdHVhbF9sb3NzKHZnZ19mZWF0cywgcmVjb24sIHRhcmdldCwgbGF5ZXJzPSgzLCA4LCAxNSkpOlxuICAgIGxvc3MsIHgsIHkgPSAwLjAsIHJlY29uLCB0YXJnZXRcbiAgICBmb3IgaSwgbGF5ZXIgaW4gZW51bWVyYXRlKHZnZ19mZWF0cyk6XG4gICAgICAgIHgsIHkgPSBsYXllcih4KSwgbGF5ZXIoeSlcbiAgICAgICAgaWYgaSBpbiBsYXllcnM6XG4gICAgICAgICAgICBsb3NzID0gbG9zcyArIEYubXNlX2xvc3MoeCwgeSlcbiAgICByZXR1cm4gbG9zc1xuXG5kZWYgdnFnYW5fbG9zcyhyZWNvbiwgdGFyZ2V0LCBkaXNjLCB2Z2dfZmVhdHMsIGNiX2xvc3MsIGxhbV9kPTAuOCwgbGFtX3A9MS4wKTpcbiAgICByZWMgICA9IEYubDFfbG9zcyhyZWNvbiwgdGFyZ2V0KVxuICAgIHBlcmMgID0gcGVyY2VwdHVhbF9sb3NzKHZnZ19mZWF0cywgcmVjb24uZGV0YWNoKCksIHRhcmdldC5kZXRhY2goKSlcbiAgICBmYWtlICA9IGRpc2MocmVjb24pXG4gICAgYWR2ICAgPSBGLmJpbmFyeV9jcm9zc19lbnRyb3B5X3dpdGhfbG9naXRzKGZha2UsIHRvcmNoLm9uZXNfbGlrZShmYWtlKSlcbiAgICByZXR1cm4gcmVjICsgbGFtX3AgKiBwZXJjICsgbGFtX2QgKiBhZHYgKyBjYl9sb3NzXG5cbmRpc2MgPSBQYXRjaEdBTkRpc2NyaW1pbmF0b3IoKVxudmdnICA9IHZnZzE2KHdlaWdodHM9Tm9uZSlcbnJlY29uLCB0YXJnZXQgPSB0b3JjaC5yYW5kbigyLCAzLCAyNTYsIDI1NiksIHRvcmNoLnJhbmRuKDIsIDMsIDI1NiwgMjU2KVxubG9zcyA9IHZxZ2FuX2xvc3MocmVjb24sIHRhcmdldCwgZGlzYywgdmdnLmZlYXR1cmVzLCBjYl9sb3NzPXRvcmNoLnRlbnNvcigwLjA1KSlcbnByaW50KGZcdTAwMjdWUUdBTiB0b3RhbCBsb3NzOiB7bG9zcy5pdGVtKCk6LjRmfVx1MDAyNylcbnByaW50KFx1MDAyN0wxICsgVkdHIHBlcmNlcHR1YWwgKyBQYXRjaEdBTiBhZHZlcnNhcmlhbCArIGNvZGVib29rIGNvbW1pdG1lbnRcdTAwMjcpIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIk1vZGVsIiwiTGV2ZWxzIiwiUHJpb3IiLCJSZXNvbHV0aW9uIiwiRklEIChJbWFnZU5ldCAyNTYpIiwiVG9rZW5zIC8gSW1hZ2UiXSwicm93cyI6W1siVlEtVkFFIiwiMSIsIlBpeGVsQ05OIiwiMzJ4MzIgbmF0aXZlICh1cHNhbXBsZWQpIiwifjY3ICgzMngzMikiLCIzMngzMiA9IDEwMjQiXSxbIlZRLVZBRS0yIiwiMiAoOHg4ICsgMzJ4MzIpIiwiUGl4ZWxTbmFpbCAodHdvLXN0YWdlKSIsIjI1NngyNTYiLCJ+Mi41IChjbGFzcy1jb25kKSIsIjY0IHRvcCArIDEwMjQgYm90dG9tIl0sWyJWUUdBTiIsIjEiLCJHUFQgVHJhbnNmb3JtZXIiLCIyNTZ4MjU2IiwifjcuOSAodW5jb25kaXRpb25hbCkiLCIxNngxNiA9IDI1NiJdLFsiREFMTC1FIHYxIiwiMSAoVlFHQU4gdG9rZW5zKSIsIkdQVC0zIHN0eWxlIFRyYW5zZm9ybWVyICh0ZXh0LWNvbmQpIiwiMjU2eDI1NiIsIn4xNy45ICh6ZXJvLXNob3QpIiwiMzJ4MzIgPSAxMDI0Il0sWyJNQUdWSVQtdjIiLCIxIChsb29rdXAtZnJlZSBWUSkiLCJNYXNrR0lUIC8gTExNIG1hc2tlZCBwcmlvciIsIjI1NngyNTYiLCJ+MS43OCAoY2xhc3MtY29uZCkiLCIxNngxNiA9IDI1NiJdXX0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJ0aXAiLCJ0aXRsZSI6IlRyYWluaW5nIE9yZGVyIE1hdHRlcnMiLCJjb250ZW50IjoiVHJhaW4gdGhlIFZRLVZBRSByZWNvbnN0cnVjdGlvbiBtb2RlbCBjb21wbGV0ZWx5IGJlZm9yZSB0cmFpbmluZyB0aGUgUGl4ZWxTbmFpbCBwcmlvcnMg4oCUIHRoZSBwcmlvciBxdWFsaXR5IGRlcGVuZHMgb24gc3RhYmxlLCB3ZWxsLXV0aWxpemVkIGNvZGVib29rcy4gSWYgeW91IHRyYWluIHRoZSBwcmlvciBvbiBhIHN0aWxsLWV2b2x2aW5nIGNvZGVib29rLCB0aGUgdG9rZW4gZGlzdHJpYnV0aW9uIHNoaWZ0cyB1bmRlciB0aGUgcHJpb3IgYW5kIHlvdSBtdXN0IHJldHJhaW4gZnJvbSBzY3JhdGNoLiBNb25pdG9yIGNvZGVib29rIHV0aWxpemF0aW9uIChmcmFjdGlvbiBvZiBhY3RpdmUgY29kZXMpIGR1cmluZyBWUS1WQUUgdHJhaW5pbmc7IHV0aWxpemF0aW9uIGJlbG93IDUwJSBzaWduYWxzIGNvZGVib29rIGNvbGxhcHNlIGFuZCByZXF1aXJlcyBhIHJlc2V0IG9yIEVNQSB1cGRhdGVzIGJlZm9yZSBwcm9jZWVkaW5nIHRvIHByaW9yIHRyYWluaW5nLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlByYWN0aWNhbCBHdWlkYW5jZSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiVlEtVkFFLTIgdHJhaW5pbmcgaGFzIHNldmVyYWwgZmFpbHVyZSBtb2RlcyB0byB3YXRjaCBmb3IuIENvZGVib29rIGNvbGxhcHNlIOKAlCB3aGVyZSBtb3N0IGNvZGVzIGFyZSBuZXZlciBzZWxlY3RlZCDigJQgaXMgdGhlIG1vc3QgY29tbW9uIGlzc3VlLiBJdCBvY2N1cnMgd2hlbiB0aGUgZW5jb2RlciB2YXJpYW5jZSBpcyBtdWNoIHNtYWxsZXIgdGhhbiB0aGUgY29kZWJvb2sgc3ByZWFkLCBjYXVzaW5nIHRoZSBzYW1lIHNtYWxsIHN1YnNldCBvZiBjb2RlcyB0byB3aW4gZXZlcnkgbmVhcmVzdC1uZWlnaGJvciBsb29rdXAuIFJlbWVkaWVzIGluY2x1ZGUgZXhwb25lbnRpYWwgbW92aW5nIGF2ZXJhZ2UgKEVNQSkgY29kZWJvb2sgdXBkYXRlcyAoaW5zdGVhZCBvZiBncmFkaWVudC1iYXNlZCksIGNvZGVib29rIHJlc2V0IChyZWluaXRpYWxpemUgZGVhZCBjb2RlcyB0byByYW5kb20gZW5jb2RlciBvdXRwdXRzKSwgYW5kIHJlZHVjaW5nIHRoZSBjb21taXRtZW50IGxvc3Mgd2VpZ2h0LiBUaGUgc3RyYWlnaHQtdGhyb3VnaCBlc3RpbWF0b3IgZ3JhZGllbnQgb25seSBhcHByb3hpbWF0ZXMgdGhlIHRydWUgZ3JhZGllbnQ7IHJlcGFyYW1ldGVyaXphdGlvbi1mcmVlIHF1YW50aXphdGlvbiBtZXRob2RzIChNQUdWSVQtdjJcdTAwMjdzIGxvb2t1cC1mcmVlIHF1YW50aXphdGlvbikgYXZvaWQgdGhpcyBhcHByb3hpbWF0aW9uIGVudGlyZWx5LiJ9LHsidHlwZSI6Imxpc3QiLCJvcmRlcmVkIjpmYWxzZSwiaXRlbXMiOlsiVXNlIEVNQSBjb2RlYm9vayB1cGRhdGVzOiBlX2kgXHUwMDNjLSBkZWNheSAqIGVfaSArICgxLWRlY2F5KSAqIG1lYW4oYXNzaWduZWQgeikgZ2l2ZXMgc21vb3RoZXIgdXRpbGl6YXRpb24gdGhhbiBncmFkaWVudC1iYXNlZCBjb21taXRtZW50IGxvc3MuIiwiTW9uaXRvciBjb2RlYm9vayBwZXJwbGV4aXR5IHBlciBsZXZlbDogaGVhbHRoeSB1dGlsaXphdGlvbiB0YXJnZXRzIH43MC04MCUgb2YgY29kZXMgYWN0aXZlOyBjb2xsYXBzZSBzaG93cyBwZXJwbGV4aXR5IFx1MDAzYyAxMCBvdXQgb2YgNTEyLiIsIkJvdHRvbSBwcmlvciBpcyB0aGUgYm90dGxlbmVjazogMTAyNCB0b2tlbnMgYXV0b3JlZ3Jlc3NpdmVseSByZXF1aXJlcyBPKDEwMjReMikgYXR0ZW50aW9uOyB1c2UgbG9jYWwvZGlsYXRlZCBhdHRlbnRpb24gb3IgVHJhbnNmb3JtZXJzIHdpdGggbGluZWFyIGNvbXBsZXhpdHkuIiwiU2VwYXJhdGUgbGVhcm5pbmcgcmF0ZXM6IFZRLVZBRSBlbmNvZGVyL2RlY29kZXIgYmVuZWZpdCBmcm9tIDFlLTQ7IFBpeGVsU25haWwgcHJpb3JzIHRyYWluIHN0YWJseSBhdCAzZS00IHdpdGggZ3JhZGllbnQgY2xpcHBpbmcgYXQgMS4wLiIsIkZvciBWUUdBTjogYXBwbHkgYWRhcHRpdmUgZGlzY3JpbWluYXRvciB3ZWlnaHRpbmcg4oCUIHNjYWxlIHRoZSBhZHZlcnNhcmlhbCBsb3NzIGJ5IHx8Z3JhZF9sYXN0X2RlYyhMX3JlYyl8fCAvIHx8Z3JhZF9sYXN0X2RlYyhMX2Fkdil8fCwgcHJldmVudGluZyB0aGUgR0FOIHRlcm0gZnJvbSBkb21pbmF0aW5nIGVhcmx5IHRyYWluaW5nLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJLZXkgVGFrZWF3YXlzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJWUS1WQUUtMiBkZW1vbnN0cmF0ZXMgdGhhdCBoaWVyYXJjaGljYWwgZGlzY3JldGUgcmVwcmVzZW50YXRpb25zIGNhbiBtYXRjaCBvciBleGNlZWQgY29udGludW91cyBsYXRlbnQgbW9kZWxzIGF0IGhpZ2ggcmVzb2x1dGlvbiB3aXRob3V0IGFkdmVyc2FyaWFsIHRyYWluaW5nIGluIHRoZSByZWNvbnN0cnVjdGlvbiBzdGFnZS4gVGhlIHNlcGFyYXRpb24gb2YgZ2xvYmFsIHN0cnVjdHVyZSAodG9wIGxldmVsLCA4eDgpIGZyb20gbG9jYWwgZGV0YWlsIChib3R0b20gbGV2ZWwsIDMyeDMyKSDigJQgd2l0aCBib3R0b20gZW5jb2RpbmcgY29uZGl0aW9uZWQgb24gdG9wIGNvZGVzIOKAlCBpcyB0aGUgYXJjaGl0ZWN0dXJhbCBpbnNpZ2h0IHRoYXQgbWFrZXMgMjU2eDI1NiBnZW5lcmF0aW9uIGZlYXNpYmxlLiBUaGUgdHdvLXN0YWdlIHByaW9yIHRyYWluaW5nICh0b3AgUGl4ZWxTbmFpbCBmaXJzdCwgdGhlbiBjb25kaXRpb25lZCBib3R0b20gUGl4ZWxTbmFpbCkgaXMgdGhlIGdlbmVyYXRpdmUgbWVjaGFuaXNtLiBTdWJzZXF1ZW50IHdvcmsgKFZRR0FOLCBEQUxMLUUgdjEsIE1BR1ZJVC12MiwgTGxhbWFHZW4pIGFsbCBmb2xsb3cgdGhlIHNhbWUgcGFyYWRpZ20gb2YgZGlzY3JldGUgaW1hZ2UgdG9rZW5pemF0aW9uIGZvbGxvd2VkIGJ5IGEgcG93ZXJmdWwgc2VxdWVuY2UgcHJpb3IsIHdpdGggaW1wcm92ZW1lbnRzIGluIHRva2VuaXplciBxdWFsaXR5IChwZXJjZXB0dWFsIGxvc3MsIGFkdmVyc2FyaWFsIHRyYWluaW5nLCBsb29rdXAtZnJlZSBxdWFudGl6YXRpb24pIGFuZCBwcmlvciBleHByZXNzaXZlbmVzcyAoVHJhbnNmb3JtZXJzIG92ZXIgUGl4ZWxDTk5zKS4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIlR3byBjb2RlYm9vayBsZXZlbHMgd2l0aCBjb25kaXRpb25pbmc6IGJvdHRvbSBxdWFudGl6YXRpb24gY29uZGl0aW9uZWQgb24gdG9wIGNvZGVzIG1lYW5zIGVhY2ggbGV2ZWwgaGFzIGEgd2VsbC1kZWZpbmVkLCBub24tb3ZlcmxhcHBpbmcgcm9sZS4iLCJTdHJhaWdodC10aHJvdWdoIGVzdGltYXRvciBtYWtlcyBkaXNjcmV0ZSBxdWFudGl6YXRpb24gZW5kLXRvLWVuZCBkaWZmZXJlbnRpYWJsZSBieSBwYXNzaW5nIGdyYWRpZW50cyB0aHJvdWdoIHRoZSBhcmdtaW4gYXMgaWYgaXQgd2VyZSBpZGVudGl0eS4iLCJUd28tc3RhZ2UgYXV0b3JlZ3Jlc3NpdmUgcHJpb3I6IHNhbXBsZSB0b3AgOHg4IHRva2VucyBmaXJzdCAoZ2xvYmFsKSwgdGhlbiBib3R0b20gMzJ4MzIgdG9rZW5zIGNvbmRpdGlvbmVkIG9uIHRvcCAobG9jYWwgZGV0YWlsKS4iLCJWUUdBTiB1cGdyYWRlOiByZXBsYWNpbmcgTVNFL2NvbW1pdG1lbnQgbG9zcyB3aXRoIHBlcmNlcHR1YWwgKyBhZHZlcnNhcmlhbCBsb3NzIGRyYW1hdGljYWxseSBzaGFycGVucyByZWNvbnN0cnVjdGlvbiBxdWFsaXR5IHdpdGggbm8gY2hhbmdlIHRvIHRoZSBkaXNjcmV0ZSBib3R0bGVuZWNrLiIsIk1vZGVybiB0cmFqZWN0b3J5OiBWUS1WQUUtMiAtXHUwMDNlIFZRR0FOIC1cdTAwM2UgREFMTC1FIHYxIC1cdTAwM2UgTUFHVklULXYyIC8gTGxhbWFHZW47IGFsbCBzaGFyZSBkaXNjcmV0ZSB0b2tlbml6YXRpb24gKyBzZXF1ZW5jZSBwcmlvciwgZGlmZmVyaW5nIGluIHRva2VuaXplciBxdWFsaXR5IGFuZCBwcmlvciBhcmNoaXRlY3R1cmUuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# VQ-VAE-2 — Hierarchical Discrete Latents for High-Resolution Generation

VQ-VAE-2 (Razavi et al. 2019) extends the original VQ-VAE to high-resolution image synthesis by introducing a hierarchy of discrete latent codes. A single codebook at one resolution cannot simultaneously capture both global image structure (object layout, colour palette) and local fine details (textures, edges). Two levels solve this: a top level at 8x8 encodes coarse global information, and a bottom level at 32x32 encodes local detail conditioned on the already-quantized top representation. The result is 256x256 class-conditional generation at FID ~2.5 on ImageNet — competitive with BigGAN at the time — using a two-stage discrete autoregressive prior.

## Introduction: Hierarchical Motivation

The original VQ-VAE used a single-level codebook and was limited to 32x32 or 64x64 generation. Scaling to 256x256 with one codebook forces a tradeoff: a large spatial grid preserves local detail but the codebook must span the entire space of image patches; a small grid loses spatial resolution. Hierarchical representation solves this by factorising image information across levels. The top level need only describe scene-level structure — which regions contain foreground objects, approximate colour distribution, dominant shapes — while the bottom level fills in local texture conditioned on that global context. This mirrors how humans perceive images: global scene understanding precedes local detail.

## Two-Level Architecture

The VQ-VAE-2 encoder-decoder pair has two quantization stages with separate codebooks. The bottom encoder maps 256x256 images to 32x32 feature maps capturing local detail. The top encoder further compresses 32x32 features to 8x8, capturing global structure. Each level has its own codebook (typically 512 entries each, embedding dimension 64). During encoding, top features are quantized first; the quantized top codes are then upsampled and concatenated to the bottom features before bottom quantization, so the bottom codebook only needs to represent residual local information not already explained by the top. The decoder reverses this process top-down.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class VectorQuantize(nn.Module):
    def __init__(self, codebook_size=512, embed_dim=64):
        super().__init__()
        self.codebook = nn.Embedding(codebook_size, embed_dim)

    def forward(self, z):
        B, C, H, W = z.shape
        z_flat = z.permute(0, 2, 3, 1).reshape(-1, C)
        dist = (z_flat.unsqueeze(1) - self.codebook.weight.unsqueeze(0)).pow(2).sum(-1)
        indices = dist.argmin(dim=1)
        z_q = self.codebook(indices).reshape(B, H, W, C).permute(0, 3, 1, 2)
        z_q = z + (z_q - z).detach()   # straight-through estimator
        return z_q, indices.reshape(B, H, W)

class HierarchicalVQVAE(nn.Module):
    def __init__(self, in_ch=3, hidden=128, codebook_size=512, embed_dim=64):
        super().__init__()
        self.bottom_enc = nn.Sequential(
            nn.Conv2d(in_ch, hidden, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(hidden, hidden, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(hidden, hidden, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(hidden, embed_dim, 1)        # 256->32 (3 strides of 2)
        )
        self.top_enc = nn.Sequential(
            nn.Conv2d(embed_dim, hidden, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(hidden, hidden, 4, 2, 1), nn.ReLU(),
            nn.Conv2d(hidden, embed_dim, 1)        # 32->8 (2 strides of 2)
        )
        self.vq_top    = VectorQuantize(codebook_size, embed_dim)
        self.vq_bottom = VectorQuantize(codebook_size, embed_dim)

torch.manual_seed(0)
model = HierarchicalVQVAE()
x = torch.randn(2, 3, 256, 256)
b_feat = model.bottom_enc(x)        # (2, 64, 32, 32)
t_feat = model.top_enc(b_feat)      # (2, 64,  8,  8)
t_q, t_idx = model.vq_top(t_feat)
print(f'Top quantized: {t_q.shape}, indices: {t_idx.shape}')  # (2,64,8,8), (2,8,8)
```

## Top-Level Encoding

The top encoder takes the 32x32 bottom feature map as input and applies two further stride-2 convolutions to reach 8x8. This 8x8 top representation is quantized against the top codebook using nearest-neighbor lookup in embedding space (512 entries). The result is 64 discrete tokens per image — enough to represent coarse semantic layout without redundancy. Because the top codebook is small (8x8 = 64 tokens), PixelSnail can model its prior autoregressively in reasonable time: a 64-token sequence is tractable for a convolutional autoregressive model with masking.

## Bottom-Level Conditioning

The key innovation in VQ-VAE-2 is that bottom quantization is conditioned on the top codes. After computing the top quantized codes t_q at 8x8, they are upsampled (via nearest-neighbor interpolation) to 32x32 and concatenated channel-wise with the raw bottom encoder features. A learned projection then maps the combined representation to the embedding space before bottom VQ lookup. This means the bottom codebook only needs to encode residual local information not already captured by the top level — a much easier task than encoding everything from scratch. The bottom codes carry local textures, edge orientations, and fine colour variations.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class BottomConditionedEncoder(nn.Module):
    """Encodes bottom features conditioned on upsampled top quantized codes."""
    def __init__(self, embed_dim=64, hidden=128):
        super().__init__()
        self.condition_proj = nn.Sequential(
            nn.Conv2d(embed_dim * 2, hidden, 3, 1, 1), nn.ReLU(),
            nn.Conv2d(hidden, embed_dim, 1)
        )

    def forward(self, bottom_feat, top_q):
        # Upsample 8x8 top codes to match 32x32 bottom resolution
        top_up = F.interpolate(top_q, size=bottom_feat.shape[-2:], mode='nearest')
        combined = torch.cat([bottom_feat, top_up], dim=1)  # (B, 2*C, 32, 32)
        return self.condition_proj(combined)                # (B, C,   32, 32)

torch.manual_seed(0)
enc   = BottomConditionedEncoder(embed_dim=64, hidden=128)
b_raw = torch.randn(2, 64, 32, 32)  # raw bottom encoder output
t_q   = torch.randn(2, 64,  8,  8)  # quantized top codes
conditioned = enc(b_raw, t_q)       # (2, 64, 32, 32)
print(f'Bottom raw:       {b_raw.shape}')
print(f'Top upsampled to: {F.interpolate(t_q, size=(32,32)).shape}')
print(f'Conditioned feat: {conditioned.shape}')  # ready for VQ lookup
```

## Decoder Path

The VQ-VAE-2 decoder reconstructs images top-down. The 8x8 top quantized codes are first decoded by a small network that upsamples them to 32x32 feature maps. These decoded top features are then concatenated with the 32x32 bottom quantized codes, and a final decoder network upsamples the combined representation from 32x32 back to 256x256 RGB. The top-decoded features provide global structure guidance; the bottom codes inject local detail. This two-path merge allows the decoder to benefit from both levels of abstraction simultaneously.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TopDownDecoder(nn.Module):
    """Decodes: top codes (8x8) -> upsample -> merge with bottom codes (32x32) -> image."""
    def __init__(self, embed_dim=64, hidden=128, out_ch=3):
        super().__init__()
        self.top_dec = nn.Sequential(
            nn.Conv2d(embed_dim, hidden, 3, 1, 1), nn.ReLU(),
            nn.Upsample(scale_factor=4, mode='nearest'),  # 8x8  -> 32x32
            nn.Conv2d(hidden, embed_dim, 3, 1, 1), nn.ReLU()
        )
        self.final_dec = nn.Sequential(
            nn.Conv2d(embed_dim * 2, hidden, 3, 1, 1), nn.ReLU(),
            nn.Upsample(scale_factor=4, mode='nearest'),  # 32x32 -> 128x128
            nn.Conv2d(hidden, hidden, 3, 1, 1), nn.ReLU(),
            nn.Upsample(scale_factor=2, mode='nearest'),  # 128x128 -> 256x256
            nn.Conv2d(hidden, out_ch, 3, 1, 1), nn.Tanh()
        )

    def forward(self, top_q, bottom_q):
        top_decoded = self.top_dec(top_q)                      # (B, C, 32, 32)
        combined    = torch.cat([top_decoded, bottom_q], dim=1) # (B, 2C, 32, 32)
        return self.final_dec(combined)                        # (B, 3, 256, 256)

torch.manual_seed(0)
decoder  = TopDownDecoder()
top_q    = torch.randn(2, 64,  8,  8)
bottom_q = torch.randn(2, 64, 32, 32)
recon    = decoder(top_q, bottom_q)
print(f'Top codes:   {top_q.shape}')     # (2, 64, 8, 8)
print(f'Bottom codes:{bottom_q.shape}')  # (2, 64, 32, 32)
print(f'Reconstruction: {recon.shape}')  # (2, 3, 256, 256)
```

## Two-Stage Prior Models

Generation with VQ-VAE-2 requires sampling discrete codes and decoding them — the VQ-VAE itself provides no generative prior. VQ-VAE-2 uses PixelSnail, a convolutional autoregressive model with attention, as a prior at each level. Stage 1: a PixelSnail top prior models p(z_top | class) autoregressively over the 8x8 = 64 top tokens. Stage 2: a conditioned PixelSnail bottom prior models p(z_bottom | z_top, class) autoregressively over the 1024 bottom tokens at 32x32, conditioned on the fully sampled top codes. Once both code maps are sampled, the VQ-VAE-2 decoder produces the final 256x256 image. The two-stage approach allows the top prior to establish global coherence before the bottom prior fills in local details.

- Top prior: PixelSnail over 8x8=64 discrete tokens; receptive field covers the full 8x8 grid via global self-attention.
- Bottom prior: conditioned PixelSnail over 32x32=1024 tokens; top codes are embedded and used as context via cross-attention.
- Sampling order: sample all 64 top tokens first (row-major autoregressive), then sample all 1024 bottom tokens conditioned on sampled top.
- Class conditioning: class label embedding is added to both top and bottom PixelSnail inputs, enabling class-conditional generation.
- FID ~2.5 on class-conditional ImageNet 256x256, competitive with BigGAN while using a fundamentally different (non-adversarial) training objective.

## VQGAN and Beyond

VQGAN (Esser et al. 2021) upgrades the VQ-VAE reconstruction quality by adding a PatchGAN adversarial discriminator and a VGG perceptual loss to the standard commitment + reconstruction objective. The discriminator pushes the decoder to produce perceptually sharp outputs rather than blurry MSE-optimal reconstructions. Critically, VQGAN also replaces PixelSnail with a GPT-style Transformer as the prior — the discrete tokens produced by the VQGAN encoder become a sequence modeled by a causal Transformer, enabling much longer-range dependencies. DALL-E v1 used exactly this architecture: a VQGAN tokenizer (256 image tokens at 32x32 from a 256x256 image) paired with a GPT-style Transformer conditioned on text tokens. Modern systems extend further: MAGVIT-v2 uses improved lookup-free quantization and an LLM-style masked prior, while LlamaGen applies LLaMA-style autoregressive Transformers to VQ image tokens with competitive FID.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import vgg16

class PatchGANDiscriminator(nn.Module):
    """70x70 PatchGAN: classifies overlapping image patches as real/fake."""
    def __init__(self, in_ch=3, ndf=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(in_ch,    ndf,   4, 2, 1), nn.LeakyReLU(0.2, True),
            nn.Conv2d(ndf,   ndf*2, 4, 2, 1, bias=False), nn.BatchNorm2d(ndf*2), nn.LeakyReLU(0.2, True),
            nn.Conv2d(ndf*2, ndf*4, 4, 2, 1, bias=False), nn.BatchNorm2d(ndf*4), nn.LeakyReLU(0.2, True),
            nn.Conv2d(ndf*4, ndf*8, 4, 1, 1, bias=False), nn.BatchNorm2d(ndf*8), nn.LeakyReLU(0.2, True),
            nn.Conv2d(ndf*8, 1, 4, 1, 1)  # patch-level logits
        )
    def forward(self, x):
        return self.net(x)

def perceptual_loss(vgg_feats, recon, target, layers=(3, 8, 15)):
    loss, x, y = 0.0, recon, target
    for i, layer in enumerate(vgg_feats):
        x, y = layer(x), layer(y)
        if i in layers:
            loss = loss + F.mse_loss(x, y)
    return loss

def vqgan_loss(recon, target, disc, vgg_feats, cb_loss, lam_d=0.8, lam_p=1.0):
    rec   = F.l1_loss(recon, target)
    perc  = perceptual_loss(vgg_feats, recon.detach(), target.detach())
    fake  = disc(recon)
    adv   = F.binary_cross_entropy_with_logits(fake, torch.ones_like(fake))
    return rec + lam_p * perc + lam_d * adv + cb_loss

disc = PatchGANDiscriminator()
vgg  = vgg16(weights=None)
recon, target = torch.randn(2, 3, 256, 256), torch.randn(2, 3, 256, 256)
loss = vqgan_loss(recon, target, disc, vgg.features, cb_loss=torch.tensor(0.05))
print(f'VQGAN total loss: {loss.item():.4f}')
print('L1 + VGG perceptual + PatchGAN adversarial + codebook commitment')
```

| Model | Levels | Prior | Resolution | FID (ImageNet 256) | Tokens / Image |
| --- | --- | --- | --- | --- | --- |
| VQ-VAE | 1 | PixelCNN | 32x32 native (upsampled) | ~67 (32x32) | 32x32 = 1024 |
| VQ-VAE-2 | 2 (8x8 + 32x32) | PixelSnail (two-stage) | 256x256 | ~2.5 (class-cond) | 64 top + 1024 bottom |
| VQGAN | 1 | GPT Transformer | 256x256 | ~7.9 (unconditional) | 16x16 = 256 |
| DALL-E v1 | 1 (VQGAN tokens) | GPT-3 style Transformer (text-cond) | 256x256 | ~17.9 (zero-shot) | 32x32 = 1024 |
| MAGVIT-v2 | 1 (lookup-free VQ) | MaskGIT / LLM masked prior | 256x256 | ~1.78 (class-cond) | 16x16 = 256 |

> **Training Order Matters**: Train the VQ-VAE reconstruction model completely before training the PixelSnail priors — the prior quality depends on stable, well-utilized codebooks. If you train the prior on a still-evolving codebook, the token distribution shifts under the prior and you must retrain from scratch. Monitor codebook utilization (fraction of active codes) during VQ-VAE training; utilization below 50% signals codebook collapse and requires a reset or EMA updates before proceeding to prior training.

## Practical Guidance

VQ-VAE-2 training has several failure modes to watch for. Codebook collapse — where most codes are never selected — is the most common issue. It occurs when the encoder variance is much smaller than the codebook spread, causing the same small subset of codes to win every nearest-neighbor lookup. Remedies include exponential moving average (EMA) codebook updates (instead of gradient-based), codebook reset (reinitialize dead codes to random encoder outputs), and reducing the commitment loss weight. The straight-through estimator gradient only approximates the true gradient; reparameterization-free quantization methods (MAGVIT-v2's lookup-free quantization) avoid this approximation entirely.

- Use EMA codebook updates: e_i <- decay * e_i + (1-decay) * mean(assigned z) gives smoother utilization than gradient-based commitment loss.
- Monitor codebook perplexity per level: healthy utilization targets ~70-80% of codes active; collapse shows perplexity < 10 out of 512.
- Bottom prior is the bottleneck: 1024 tokens autoregressively requires O(1024^2) attention; use local/dilated attention or Transformers with linear complexity.
- Separate learning rates: VQ-VAE encoder/decoder benefit from 1e-4; PixelSnail priors train stably at 3e-4 with gradient clipping at 1.0.
- For VQGAN: apply adaptive discriminator weighting — scale the adversarial loss by ||grad_last_dec(L_rec)|| / ||grad_last_dec(L_adv)||, preventing the GAN term from dominating early training.

## Key Takeaways

VQ-VAE-2 demonstrates that hierarchical discrete representations can match or exceed continuous latent models at high resolution without adversarial training in the reconstruction stage. The separation of global structure (top level, 8x8) from local detail (bottom level, 32x32) — with bottom encoding conditioned on top codes — is the architectural insight that makes 256x256 generation feasible. The two-stage prior training (top PixelSnail first, then conditioned bottom PixelSnail) is the generative mechanism. Subsequent work (VQGAN, DALL-E v1, MAGVIT-v2, LlamaGen) all follow the same paradigm of discrete image tokenization followed by a powerful sequence prior, with improvements in tokenizer quality (perceptual loss, adversarial training, lookup-free quantization) and prior expressiveness (Transformers over PixelCNNs).

- Two codebook levels with conditioning: bottom quantization conditioned on top codes means each level has a well-defined, non-overlapping role.
- Straight-through estimator makes discrete quantization end-to-end differentiable by passing gradients through the argmin as if it were identity.
- Two-stage autoregressive prior: sample top 8x8 tokens first (global), then bottom 32x32 tokens conditioned on top (local detail).
- VQGAN upgrade: replacing MSE/commitment loss with perceptual + adversarial loss dramatically sharpens reconstruction quality with no change to the discrete bottleneck.
- Modern trajectory: VQ-VAE-2 -> VQGAN -> DALL-E v1 -> MAGVIT-v2 / LlamaGen; all share discrete tokenization + sequence prior, differing in tokenizer quality and prior architecture.

---

