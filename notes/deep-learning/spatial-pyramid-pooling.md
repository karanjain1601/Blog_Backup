---
title: "Spatial Pyramid Pooling (SPP) — Multi-Scale Feature Aggregation"
slug: "spatial-pyramid-pooling"
description: "SPP-Net pools at multiple grid sizes to produce fixed-size feature vectors from any input resolution; ASPP applies atrous convolutions at multiple dilation rates for semantic segmentation; PSPNet, SPPF, and PANet extend the idea to detection and scene parsing."
tags: ["deep-learning", "cnns", "architectures"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiU3BhdGlhbCBQeXJhbWlkIFBvb2xpbmcgKFNQUCkgc29sdmVzIGEgZnVuZGFtZW50YWwgbWlzbWF0Y2ggYmV0d2VlbiBjb252b2x1dGlvbmFsIGZlYXR1cmUgbWFwcyBvZiBhcmJpdHJhcnkgc3BhdGlhbCBzaXplIGFuZCBkb3duc3RyZWFtIGxheWVycyB0aGF0IHJlcXVpcmUgYSBmaXhlZC1sZW5ndGggaW5wdXQuIEJ5IHBvb2xpbmcgYXQgbXVsdGlwbGUgcHlyYW1pZCBsZXZlbHMg4oCUIDHDlzEsIDLDlzIsIGFuZCA0w5c0IGdyaWRzIOKAlCBhbmQgY29uY2F0ZW5hdGluZyB0aGUgcmVzdWx0cywgU1BQIHByb2R1Y2VzIGEgZml4ZWQtc2l6ZSBkZXNjcmlwdG9yIHJlZ2FyZGxlc3Mgb2YgaW5wdXQgaW1hZ2UgcmVzb2x1dGlvbi4gVGhpcyBzaW5nbGUgaWRlYSBzcGF3bmVkIGFuIGVudGlyZSBmYW1pbHkgb2YgbXVsdGktc2NhbGUgcG9vbGluZyBhcmNoaXRlY3R1cmVzIHNwYW5uaW5nIGltYWdlIGNsYXNzaWZpY2F0aW9uLCBvYmplY3QgZGV0ZWN0aW9uLCBhbmQgc2VtYW50aWMgc2VnbWVudGF0aW9uLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkZpeGVkLVNpemUgRmVhdHVyZSBWZWN0b3JzIGZyb20gVmFyaWFibGUtU2l6ZSBJbnB1dHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkEgc3RhbmRhcmQgQ05OIHJlcXVpcmVzIGEgZml4ZWQgaW5wdXQgc2l6ZSBiZWNhdXNlIGZ1bGx5LWNvbm5lY3RlZCBsYXllcnMgZXhwZWN0IGEgZml4ZWQgbnVtYmVyIG9mIGlucHV0cy4gVGhlIHNwYXRpYWwgZmVhdHVyZSBtYXAgZnJvbSBhIGNvbnYgbGF5ZXIgaGFzIHNoYXBlIEPDl0jDl1cgd2hlcmUgSCBhbmQgVyBkZXBlbmQgb24gaW5wdXQgZGltZW5zaW9ucy4gU1BQIHJlc29sdmVzIHRoaXMgYnkgYXBwbHlpbmcgYWRhcHRpdmUgcG9vbGluZyBhdCBsIHB5cmFtaWQgbGV2ZWxzIHdpdGggZ3JpZCBzaXplcyBz4oKBLCBz4oKCLCAuLi4sIHPigpcuIEVhY2ggbGV2ZWwgcG9vbHMgdGhlIEMtY2hhbm5lbCBtYXAgaW50byBDw5dz4bWiw5dz4bWiLCB3aGljaCBpcyB0aGVuIGZsYXR0ZW5lZC4gT3V0cHV0cyBhcmUgY29uY2F0ZW5hdGVkIHRvIGZvcm0gYSBmaXhlZCB2ZWN0b3Igb2YgbGVuZ3RoIEMgw5cgzqMoc+G1osKyKS4gRm9yIHBvb2wgc2l6ZXMgezEsIDIsIDR9IGFuZCBDPTUxMiwgb3V0cHV0IGlzIGFsd2F5cyA1MTLDlygxKzQrMTYpPTEwLDc1MiByZWdhcmRsZXNzIG9mIHdoZXRoZXIgaW5wdXQgaXMgMjI0w5cyMjQgb3IgNjQww5c0ODAuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiU1BQLU5ldDogQ29tcHV0aW5nIEZlYXR1cmVzIE9uY2UgZm9yIEFsbCBQcm9wb3NhbHMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlItQ05OIChHaXJzaGljayBldCBhbC4sIDIwMTQpIHJ1bnMgYSBmb3J3YXJkIHBhc3MgdGhyb3VnaCB0aGUgZnVsbCBDTk4gZm9yIGVhY2ggcmVnaW9uIHByb3Bvc2FsIGluZGVwZW5kZW50bHkg4oCUIHR5cGljYWxseSAyLDAwMCBwcm9wb3NhbHMgcGVyIGltYWdlLCBlYWNoIHJlc2l6ZWQgdG8gYSBmaXhlZCAyMjfDlzIyNyBjcm9wLiBTUFAtTmV0IChIZSBldCBhbC4sIDIwMTUpIGVsaW1pbmF0ZXMgdGhpcyByZWR1bmRhbmN5OiBpdCBydW5zIHRoZSBjb252b2x1dGlvbmFsIGxheWVycyBvbmNlIG9uIHRoZSBlbnRpcmUgaW1hZ2UgdG8gcHJvZHVjZSBhIHNoYXJlZCBmZWF0dXJlIG1hcCwgdGhlbiBhcHBsaWVzIFNQUCB0byBlYWNoIHByb3Bvc2FsXHUwMDI3cyByZWdpb24gd2l0aGluIHRoYXQgZmVhdHVyZSBtYXAuIFNpbmNlIHByb3Bvc2FscyBvdmVybGFwIGhlYXZpbHksIHNoYXJlZCBjb21wdXRhdGlvbiB5aWVsZHMgYSAyNOKAkzEwMsOXIHNwZWVkdXAuIFRoaXMgaW5zaWdodCDigJQgY29tcHV0ZSBvbmNlLCBwb29sIHBlciByZWdpb24g4oCUIGRpcmVjdGx5IGluc3BpcmVkIFJvSSBQb29saW5nIGluIEZhc3QgUi1DTk4gYW5kIFJvSSBBbGlnbiBpbiBNYXNrIFItQ05OLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBTUFBNb2R1bGUobm4uTW9kdWxlKTpcbiAgICBcdTAwMjdcdTAwMjdcdTAwMjdTcGF0aWFsIFB5cmFtaWQgUG9vbGluZzogcG9vbHMgYXQgbXVsdGlwbGUgZ3JpZCBzaXplcywgY29uY2F0ZW5hdGVzLlx1MDAyN1x1MDAyN1x1MDAyN1xuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwb29sX3NpemVzPSgxLCAyLCA0KSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBzZWxmLnBvb2xfc2l6ZXMgPSBwb29sX3NpemVzXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgYiwgYywgaCwgdyA9IHguc2hhcGVcbiAgICAgICAgcG9vbGVkID0gW11cbiAgICAgICAgZm9yIHNpemUgaW4gc2VsZi5wb29sX3NpemVzOlxuICAgICAgICAgICAgb3V0ID0gRi5hZGFwdGl2ZV9hdmdfcG9vbDJkKHgsIG91dHB1dF9zaXplPShzaXplLCBzaXplKSlcbiAgICAgICAgICAgIHBvb2xlZC5hcHBlbmQob3V0LnZpZXcoYiwgLTEpKSAgIyBmbGF0dGVuIGVhY2ggc2NhbGVcbiAgICAgICAgcmV0dXJuIHRvcmNoLmNhdChwb29sZWQsIGRpbT0xKVxuXG4gICAgZGVmIG91dHB1dF9kaW0oc2VsZiwgaW5fY2hhbm5lbHMpOlxuICAgICAgICByZXR1cm4gaW5fY2hhbm5lbHMgKiBzdW0ocyAqIHMgZm9yIHMgaW4gc2VsZi5wb29sX3NpemVzKVxuXG4jIEFueSBpbnB1dCBzcGF0aWFsIHNpemUgd29ya3Mg4oCUIG5vIGNyb3BwaW5nIG9yIHdhcnBpbmcgbmVlZGVkXG5tb2RlbCA9IFNQUE1vZHVsZShwb29sX3NpemVzPSgxLCAyLCA0KSlcbmZvciBoLCB3IGluIFsoNywgNyksICgxNCwgMTApLCAoMjAsIDE1KV06XG4gICAgeCA9IHRvcmNoLnJhbmRuKDIsIDUxMiwgaCwgdylcbiAgICBvdXQgPSBtb2RlbCh4KVxuICAgIHByaW50KFx1MDAyN0lucHV0IHt9eHt9IC1cdTAwM2UgU1BQIG91dHB1dCBkaW06IHt9XHUwMDI3LmZvcm1hdChoLCB3LCBvdXQuc2hhcGVbMV0pKVxucHJpbnQoXHUwMDI3Rml4ZWQgb3V0cHV0IGRpbSA9IDUxMiooMSs0KzE2KSA9IHs6LH1cdTAwMjcuZm9ybWF0KG1vZGVsLm91dHB1dF9kaW0oNTEyKSkpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQVNQUDogQXRyb3VzIFNwYXRpYWwgUHlyYW1pZCBQb29saW5nIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJEZWVwTGFiIChDaGVuIGV0IGFsLikgcmVwbGFjZXMgc3RhbmRhcmQgbWF4IHBvb2xpbmcgd2l0aCBhdHJvdXMgKGRpbGF0ZWQpIGNvbnZvbHV0aW9ucyB0byBjYXB0dXJlIG11bHRpLXNjYWxlIGNvbnRleHQgd2l0aG91dCByZWR1Y2luZyBmZWF0dXJlIG1hcCByZXNvbHV0aW9uLiBBU1BQIGFwcGxpZXMgcGFyYWxsZWwgM8OXMyBkaWxhdGVkIGNvbnZvbHV0aW9ucyB3aXRoIHJhdGVzIHIg4oiIIHs2LCAxMiwgMTh9LCBwbHVzIGEgMcOXMSBjb252IGFuZCBnbG9iYWwgYXZlcmFnZSBwb29saW5nLCBhbGwgb3BlcmF0aW5nIG9uIHRoZSBzYW1lIGhpZ2gtcmVzb2x1dGlvbiBmZWF0dXJlIG1hcC4gV2l0aCBkaWxhdGlvbiByYXRlIHIsIGEgM8OXMyBrZXJuZWwgY292ZXJzIGFuIGVmZmVjdGl2ZSByZWNlcHRpdmUgZmllbGQgb2YgKHLDlzIrMSnCsiB3aGlsZSBtYWludGFpbmluZyBmdWxsIHNwYXRpYWwgcmVzb2x1dGlvbi4gQ29uY2F0ZW5hdGluZyBhbGwgYnJhbmNoZXMgYW5kIHByb2plY3Rpbmcgd2l0aCBhIDHDlzEgY29udiBnaXZlcyBhIHJpY2ggbXVsdGktc2NhbGUgcmVwcmVzZW50YXRpb24gZm9yIHBlci1waXhlbCBjbGFzc2lmaWNhdGlvbi4ifSx7InR5cGUiOiJjb2RlIiwibGFuZ3VhZ2UiOiJweXRob24iLCJjb250ZW50IjoiaW1wb3J0IHRvcmNoXG5pbXBvcnQgdG9yY2gubm4gYXMgbm5cbmltcG9ydCB0b3JjaC5ubi5mdW5jdGlvbmFsIGFzIEZcblxuY2xhc3MgQVNQUENvbnYobm4uTW9kdWxlKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2gsIG91dF9jaCwgZGlsYXRpb24pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5ibG9jayA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2gsIG91dF9jaCwgMywgcGFkZGluZz1kaWxhdGlvbiwgZGlsYXRpb249ZGlsYXRpb24sIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQob3V0X2NoKSwgbm4uUmVMVShpbnBsYWNlPVRydWUpKVxuICAgIGRlZiBmb3J3YXJkKHNlbGYsIHgpOiByZXR1cm4gc2VsZi5ibG9jayh4KVxuXG5jbGFzcyBBU1BQTW9kdWxlKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3QXRyb3VzIFNwYXRpYWwgUHlyYW1pZCBQb29saW5nIGZyb20gRGVlcExhYi12My5cdTAwMjdcdTAwMjdcdTAwMjdcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaW5fY2g9MjA0OCwgb3V0X2NoPTI1NiwgcmF0ZXM9KDYsIDEyLCAxOCkpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKClcbiAgICAgICAgc2VsZi5jb252MXgxID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG91dF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSlcbiAgICAgICAgc2VsZi5hdHJvdXMgPSBubi5Nb2R1bGVMaXN0KFtBU1BQQ29udihpbl9jaCwgb3V0X2NoLCByKSBmb3IgciBpbiByYXRlc10pXG4gICAgICAgIHNlbGYuZ2xvYmFsX3Bvb2wgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQWRhcHRpdmVBdmdQb29sMmQoMSksIG5uLkNvbnYyZChpbl9jaCwgb3V0X2NoLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG91dF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSlcbiAgICAgICAgbl9icmFuY2hlcyA9IDIgKyBsZW4ocmF0ZXMpXG4gICAgICAgIHNlbGYucHJvaiA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQob3V0X2NoICogbl9icmFuY2hlcywgb3V0X2NoLCAxLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG91dF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKSwgbm4uRHJvcG91dCgwLjUpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIGgsIHcgPSB4LnNoYXBlWy0yOl1cbiAgICAgICAgYnJhbmNoZXMgPSBbc2VsZi5jb252MXgxKHgpXSArIFthKHgpIGZvciBhIGluIHNlbGYuYXRyb3VzXVxuICAgICAgICBncCA9IEYuaW50ZXJwb2xhdGUoc2VsZi5nbG9iYWxfcG9vbCh4KSwgKGgsIHcpLCBtb2RlPVx1MDAyN2JpbGluZWFyXHUwMDI3LCBhbGlnbl9jb3JuZXJzPUZhbHNlKVxuICAgICAgICByZXR1cm4gc2VsZi5wcm9qKHRvcmNoLmNhdChicmFuY2hlcyArIFtncF0sIGRpbT0xKSlcblxuYXNwcCA9IEFTUFBNb2R1bGUoKVxueCA9IHRvcmNoLnJhbmRuKDIsIDIwNDgsIDMyLCAzMilcbnByaW50KFx1MDAyN0FTUFAgaW5wdXQ6IHt9IC1cdTAwM2Ugb3V0cHV0OiB7fVx1MDAyNy5mb3JtYXQoeC5zaGFwZSwgYXNwcCh4KS5zaGFwZSkpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJDaG9vc2luZyBEaWxhdGlvbiBSYXRlcyIsImNvbnRlbnQiOiJBU1BQIHJhdGVzIHs2LCAxMiwgMTh9IGFyZSBjYWxpYnJhdGVkIGZvciBvdXRwdXQgc3RyaWRlIDE2IChmZWF0dXJlIG1hcCBpcyAxLzE2IG9mIGlucHV0KS4gRWZmZWN0aXZlIHJlY2VwdGl2ZSBmaWVsZHMgYmVjb21lIDEzw5cxMywgMjXDlzI1LCBhbmQgMzfDlzM3LiBGb3Igb3V0cHV0IHN0cmlkZSA4LCByYXRlcyB7MTIsIDI0LCAzNn0gbWFpbnRhaW4gZXF1aXZhbGVudCBjb3ZlcmFnZS4gVmVyeSBsYXJnZSByYXRlcyBvbiBzbWFsbCBmZWF0dXJlIG1hcHMgY2F1c2UgZ3JpZGRpbmcgYXJ0aWZhY3RzIOKAlCB0aGUgZGlsYXRlZCBrZXJuZWwgc2FtcGxlcyBtb3N0bHkgYmFja2dyb3VuZCDigJQgd2hpY2ggaXMgd2h5IGEgZ2xvYmFsIHBvb2xpbmcgYnJhbmNoIGlzIGFsd2F5cyBpbmNsdWRlZCB0byBjYXB0dXJlIGltYWdlLWxldmVsIGNvbnRleHQuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUFNQTmV0OiBQeXJhbWlkIFBvb2xpbmcgTW9kdWxlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJQeXJhbWlkIFNjZW5lIFBhcnNpbmcgTmV0d29yayAoWmhhbyBldCBhbC4sIDIwMTcpIGFwcGxpZXMgZ2xvYmFsIGNvbnRleHQgdmlhIHBvb2xpbmcgYXQgZm91ciBzdWItcmVnaW9uIHNpemVzOiAxw5cxIChnbG9iYWwgYXZlcmFnZSksIDLDlzIsIDPDlzMsIGFuZCA2w5c2LiBFYWNoIHBvb2xlZCByZXByZXNlbnRhdGlvbiBwYXNzZXMgdGhyb3VnaCBhIDHDlzEgY29udiByZWR1Y2luZyBjaGFubmVscyB0byBpbl9jaCAvLyA0LCB0aGVuIGlzIHVwc2FtcGxlZCBiYWNrIHRvIHRoZSBvcmlnaW5hbCBmZWF0dXJlIG1hcCBzaXplIHZpYSBiaWxpbmVhciBpbnRlcnBvbGF0aW9uLiBDb25jYXRlbmF0aW5nIHRoZXNlIGZvdXIgY29udGV4dCBkZXNjcmlwdG9ycyB3aXRoIHRoZSBvcmlnaW5hbCBmZWF0dXJlIG1hcCBhbmQgYXBwbHlpbmcgYSBmaW5hbCBib3R0bGVuZWNrIGNvbnYgcHJvZHVjZXMgdGhlIG91dHB1dCBmb3IgcGl4ZWwtd2lzZSBjbGFzc2lmaWNhdGlvbi4gUFNQTmV0IHdvbiB0aGUgSW1hZ2VOZXQgU2NlbmUgUGFyc2luZyBDaGFsbGVuZ2UgMjAxNiB3aXRoIG1Jb1UgODUuNCUgb24gQURFMjBLLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IHRvcmNoLm5uLmZ1bmN0aW9uYWwgYXMgRlxuXG5jbGFzcyBQeXJhbWlkUG9vbGluZ01vZHVsZShubi5Nb2R1bGUpOlxuICAgIFx1MDAyN1x1MDAyN1x1MDAyN1BTUE5ldCBQeXJhbWlkIFBvb2xpbmcgTW9kdWxlIChaaGFvIGV0IGFsLiwgMjAxNykuXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBwb29sX3NpemVzPSgxLCAyLCAzLCA2KSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBtaWRfY2ggPSBpbl9jaCAvLyBsZW4ocG9vbF9zaXplcylcbiAgICAgICAgc2VsZi5zdGFnZXMgPSBubi5Nb2R1bGVMaXN0KFtcbiAgICAgICAgICAgIG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICAgICAgbm4uQWRhcHRpdmVBdmdQb29sMmQocyksXG4gICAgICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoLCBtaWRfY2gsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKG1pZF9jaCksIG5uLlJlTFUoaW5wbGFjZT1UcnVlKVxuICAgICAgICAgICAgKSBmb3IgcyBpbiBwb29sX3NpemVzXG4gICAgICAgIF0pXG4gICAgICAgIHNlbGYuYm90dGxlbmVjayA9IG5uLlNlcXVlbnRpYWwoXG4gICAgICAgICAgICBubi5Db252MmQoaW5fY2ggKyBtaWRfY2ggKiBsZW4ocG9vbF9zaXplcyksIGluX2NoIC8vIDIsIDMsXG4gICAgICAgICAgICAgICAgICAgICAgcGFkZGluZz0xLCBiaWFzPUZhbHNlKSxcbiAgICAgICAgICAgIG5uLkJhdGNoTm9ybTJkKGluX2NoIC8vIDIpLCBubi5SZUxVKGlucGxhY2U9VHJ1ZSkpXG5cbiAgICBkZWYgZm9yd2FyZChzZWxmLCB4KTpcbiAgICAgICAgaCwgdyA9IHguc2hhcGVbLTI6XVxuICAgICAgICBvdXQgPSBbeF1cbiAgICAgICAgZm9yIHN0YWdlIGluIHNlbGYuc3RhZ2VzOlxuICAgICAgICAgICAgcG9vbGVkID0gc3RhZ2UoeClcbiAgICAgICAgICAgIG91dC5hcHBlbmQoRi5pbnRlcnBvbGF0ZShwb29sZWQsIChoLCB3KSwgbW9kZT1cdTAwMjdiaWxpbmVhclx1MDAyNywgYWxpZ25fY29ybmVycz1GYWxzZSkpXG4gICAgICAgIHJldHVybiBzZWxmLmJvdHRsZW5lY2sodG9yY2guY2F0KG91dCwgZGltPTEpKVxuXG5wcG0gPSBQeXJhbWlkUG9vbGluZ01vZHVsZShpbl9jaD0yMDQ4KVxueCA9IHRvcmNoLnJhbmRuKDIsIDIwNDgsIDYwLCA2MClcbm91dCA9IHBwbSh4KVxucHJpbnQoXHUwMDI3UFBNIHt9IC1cdTAwM2Uge31cdTAwMjcuZm9ybWF0KHguc2hhcGUsIG91dC5zaGFwZSkpXG5wcmludChcdTAwMjdPdXRwdXQgY2hhbm5lbHM6IHt9IChpbl9jaCAvLyAyKVx1MDAyNy5mb3JtYXQob3V0LnNoYXBlWzFdKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJTUFBGOiBTZXF1ZW50aWFsIE1heCBQb29saW5nIGluIFlPTE92NSJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiU1BQRiAoU3BhdGlhbCBQeXJhbWlkIFBvb2xpbmcg4oCUIEZhc3QpIHJlcGxhY2VzIHBhcmFsbGVsIG11bHRpLXNjYWxlIG1heCBwb29scyB3aXRoIHRocmVlIHNlcXVlbnRpYWwgNcOXNSBtYXggcG9vbHMuIEEgc2luZ2xlIDXDlzUgcG9vbCBjb3ZlcnMgYSA1w5c1IHJlZ2lvbjsgdHdvIHNlcXVlbnRpYWwgNcOXNSBwb29scyBjb3ZlciA5w5c5OyB0aHJlZSBjb3ZlciAxM8OXMTMuIFRoaXMgbWF0Y2hlcyB0aGUgcmVjZXB0aXZlIGZpZWxkcyBvZiBwYXJhbGxlbCA1w5c1LCA5w5c5LCBhbmQgMTPDlzEzIHBvb2xzIGJ1dCBydW5zIGZhc3RlciBiZWNhdXNlIHNlcXVlbnRpYWwgcG9vbHMgc2hhcmUgY29tcHV0YXRpb24uIFlPTE92NSBpbnNlcnRzIFNQUEYgYXQgdGhlIGVuZCBvZiBpdHMgYmFja2JvbmUgKGFmdGVyIENTUCBsYXllcnMpIHRvIGFnZ3JlZ2F0ZSBnbG9iYWwgY29udGV4dCBiZWZvcmUgdGhlIFBBTmV0IG5lY2suIEEgY2hhbm5lbC1oYWx2aW5nIDHDlzEgY29udiBwcmVjZWRlcyB0aGUgcG9vbHMgYW5kIGEgMcOXMSBjb252IHByb2plY3RzIHRoZSBjb25jYXRlbmF0ZWQgNC13YXkgb3V0cHV0LCBrZWVwaW5nIGxhdGVuY3kgbG93LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuXG5jbGFzcyBTUFBGKG5uLk1vZHVsZSk6XG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3U1BQRjogU3BhdGlhbCBQeXJhbWlkIFBvb2xpbmcgLSBGYXN0IChZT0xPdjUpLlxuICAgIFRocmVlIHNlcXVlbnRpYWwgNXg1IG1heCBwb29scyBnaXZlIGVmZmVjdGl2ZSBSRnMgb2YgNXg1LCA5eDksIDEzeDEzLlxuICAgIEZhc3RlciB0aGFuIHBhcmFsbGVsIFNQUCBkdWUgdG8gc2hhcmVkIGludGVybWVkaWF0ZSBjb21wdXRhdGlvbnMuXG4gICAgXHUwMDI3XHUwMDI3XHUwMDI3XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGluX2NoLCBvdXRfY2gsIGs9NSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuICAgICAgICBtaWRfY2ggPSBpbl9jaCAvLyAyXG4gICAgICAgIHNlbGYuY29udjEgPSBubi5TZXF1ZW50aWFsKFxuICAgICAgICAgICAgbm4uQ29udjJkKGluX2NoLCBtaWRfY2gsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQobWlkX2NoKSwgbm4uU2lMVSgpKVxuICAgICAgICBzZWxmLnBvb2wgPSBubi5NYXhQb29sMmQoaywgc3RyaWRlPTEsIHBhZGRpbmc9ayAvLyAyKVxuICAgICAgICBzZWxmLmNvbnYyID0gbm4uU2VxdWVudGlhbChcbiAgICAgICAgICAgIG5uLkNvbnYyZChtaWRfY2ggKiA0LCBvdXRfY2gsIDEsIGJpYXM9RmFsc2UpLFxuICAgICAgICAgICAgbm4uQmF0Y2hOb3JtMmQob3V0X2NoKSwgbm4uU2lMVSgpKVxuXG4gICAgZGVmIGZvcndhcmQoc2VsZiwgeCk6XG4gICAgICAgIHggPSBzZWxmLmNvbnYxKHgpXG4gICAgICAgIHAxID0gc2VsZi5wb29sKHgpXG4gICAgICAgIHAyID0gc2VsZi5wb29sKHAxKVxuICAgICAgICBwMyA9IHNlbGYucG9vbChwMilcbiAgICAgICAgcmV0dXJuIHNlbGYuY29udjIodG9yY2guY2F0KFt4LCBwMSwgcDIsIHAzXSwgZGltPTEpKVxuXG5zcHBmID0gU1BQRihpbl9jaD01MTIsIG91dF9jaD01MTIpXG54ID0gdG9yY2gucmFuZG4oMSwgNTEyLCAyMCwgMjApXG5vdXQgPSBzcHBmKHgpXG5wYXJhbXMgPSBzdW0ocC5udW1lbCgpIGZvciBwIGluIHNwcGYucGFyYW1ldGVycygpKVxucHJpbnQoXHUwMDI3U1BQRiB7fSAtXHUwMDNlIHt9XHUwMDI3LmZvcm1hdCh4LnNoYXBlLCBvdXQuc2hhcGUpKVxucHJpbnQoXHUwMDI3UGFyYW1ldGVyczogezosfVx1MDAyNy5mb3JtYXQocGFyYW1zKSkifSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJQQU5ldCBhbmQgTXVsdGktU2NhbGUgRmVhdHVyZSBBZ2dyZWdhdGlvbiJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiUGF0aCBBZ2dyZWdhdGlvbiBOZXR3b3JrIChQQU5ldCwgTGl1IGV0IGFsLiAyMDE4KSBleHRlbmRzIEZQTiBieSBhZGRpbmcgYSBib3R0b20tdXAgcGF0aCBhdWdtZW50YXRpb24gYWZ0ZXIgdGhlIHN0YW5kYXJkIHRvcC1kb3duIEZQTiBwYXRod2F5LiBGUE4gcHJvcGFnYXRlcyBzdHJvbmcgc2VtYW50aWMgZmVhdHVyZXMgZnJvbSBsb3ctcmVzb2x1dGlvbiBsYXllcnMgdXB3YXJkIHRvIGhpZ2gtcmVzb2x1dGlvbiBsYXllcnMuIFBBTmV0IGFkZHMgYSBzaG9ydGN1dCBmcm9tIHRoZSBsb3ctbGV2ZWwgZmVhdHVyZXMgYmFjayB1cCB0aHJvdWdoIHRoZSBoaWVyYXJjaHksIHNvIGhpZ2gtcmVzb2x1dGlvbiBzcGF0aWFsIGRldGFpbCAoZWRnZXMsIHRleHR1cmVzKSBmbG93cyB1cHdhcmQgaW50byBoaWdoLWxldmVsIHNlbWFudGljIHJlcHJlc2VudGF0aW9ucy4gVGhpcyBiaWRpcmVjdGlvbmFsIGZsb3cg4oCUIHRvcC1kb3duIHNlbWFudGljcyArIGJvdHRvbS11cCBzcGF0aWFsIGRldGFpbCDigJQgaW1wcm92ZXMgaW5zdGFuY2Ugc2VnbWVudGF0aW9uIGFuZCBkZXRlY3Rpb24gYWNyb3NzIHNjYWxlcy4gWU9MT3Y1LCBZT0xPdjgsIGFuZCBQUC1ZT0xPIGFsbCBhZG9wdCBQQU5ldC1zdHlsZSBuZWNrcy4ifSx7InR5cGUiOiJsaXN0Iiwib3JkZXJlZCI6ZmFsc2UsIml0ZW1zIjpbIkZQTiB0b3AtZG93biBwYXRoOiBDNSAobG93LXJlcywgaGlnaC1zZW1hbnRpYykg4oaSIEM0IOKGkiBDMyAoaGlnaC1yZXMpIHZpYSB1cHNhbXBsaW5nIGFuZCBsYXRlcmFsIGNvbm5lY3Rpb25zLiIsIlBBTmV0IGJvdHRvbS11cCBwYXRoOiBQMyAoaGlnaC1yZXMpIOKGkiBQNCDihpIgUDUgKGxvdy1yZXMpIHZpYSBzdHJpZGUtMiBkb3duc2FtcGxpbmcgYW5kIGxhdGVyYWwgY29ubmVjdGlvbnMuIiwiRWFjaCBmZWF0dXJlIG1hcCBub3cgc2VlcyBib3RoIHRvcC1kb3duIGNvbnRleHQgKGxvbmcgcGF0aCkgYW5kIGJvdHRvbS11cCBzcGF0aWFsIGRldGFpbCAoc2hvcnQgcGF0aCkuIiwiQWRhcHRpdmUgRmVhdHVyZSBQb29saW5nOiBSb0kgZmVhdHVyZXMgYXJlIHBvb2xlZCBmcm9tIGFsbCBweXJhbWlkIGxldmVscyBhbmQgZnVzZWQsIGVuc3VyaW5nIHByb3Bvc2FscyBzZWUgY29udGV4dCBhdCBldmVyeSBzY2FsZS4iLCJTUFBGIGlzIHR5cGljYWxseSBwbGFjZWQgYXQgdGhlIGJhY2tib25lIG91dHB1dCBiZWZvcmUgdGhlIFBBTmV0IG5lY2sgdG8gcHJvdmlkZSBnbG9iYWwgcmVjZXB0aXZlIGZpZWxkIGNvdmVyYWdlLiJdfSx7InR5cGUiOiJoZWFkaW5nIiwibGV2ZWwiOjIsImNvbnRlbnQiOiJDb21wYXJpbmcgU1BQIFZhcmlhbnRzIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJUaGUgU1BQIGZhbWlseSBzcGFucyBwb29saW5nIHN0cmF0ZWdpZXMgb3B0aW1pc2VkIGZvciBkaWZmZXJlbnQgdGFza3MuIENsYXNzaWZpY2F0aW9uIG5ldHdvcmtzIG5lZWQgZml4ZWQtc2l6ZSBkZXNjcmlwdG9yczsgc2VnbWVudGF0aW9uIG1vZGVscyBuZWVkIGZ1bGwtcmVzb2x1dGlvbiBvdXRwdXRzIHdpdGggbXVsdGktc2NhbGUgY29udGV4dDsgZGV0ZWN0aW9uIGJhY2tib25lcyBuZWVkIHNwZWVkIHdpdGggZ2xvYmFsIHJlY2VwdGl2ZSBmaWVsZDsgbXVsdGktc2NhbGUgbmVja3MgbmVlZCBiaWRpcmVjdGlvbmFsIGluZm9ybWF0aW9uIGZsb3cgYWNyb3NzIHB5cmFtaWQgbGV2ZWxzLiJ9LHsidHlwZSI6InRhYmxlIiwiaGVhZGVycyI6WyJWYXJpYW50IiwiU2NhbGVzIC8gUmF0ZXMiLCJQb29saW5nIE9wIiwiVGFzayIsIkxhdGVuY3kiLCJLZXkgQmVuZWZpdCJdLCJyb3dzIjpbWyJTUFAgKEhlIDIwMTUpIiwiezHDlzEsIDLDlzIsIDTDlzR9IiwiQWRhcHRpdmUgbWF4IHBvb2wiLCJDbGFzc2lmaWNhdGlvbiwgRGV0ZWN0aW9uIiwiTWVkaXVtIiwiRml4ZWQgb3V0cHV0IGZyb20gYW55IGlucHV0IHNpemUiXSxbIkFTUFAgKERlZXBMYWIpIiwiRGlsYXRpb24gezYsIDEyLCAxOH0iLCJEaWxhdGVkIDPDlzMgY29udiIsIlNlbWFudGljIHNlZ21lbnRhdGlvbiIsIkhpZ2giLCJGdWxsLXJlc29sdXRpb24gbXVsdGktc2NhbGUgY29udGV4dCJdLFsiUFNQTmV0IFBQTSIsInsxLCAyLCAzLCA2fSBncmlkIiwiQXZnIHBvb2wgKyB1cHNhbXBsZSIsIlNlbWFudGljIHNlZ21lbnRhdGlvbiIsIk1lZGl1bSIsIkdsb2JhbCBzY2VuZSBjb250ZXh0IHBvb2xpbmciXSxbIlNQUEYgKFlPTE92NSkiLCI1w5c1IHNlcXVlbnRpYWwgw5cgMyIsIlNlcXVlbnRpYWwgbWF4IHBvb2wiLCJPYmplY3QgZGV0ZWN0aW9uIiwiTG93IiwiRmFzdCBtdWx0aS1zY2FsZSBSRiBleHBhbnNpb24iXSxbIlBBTmV0IiwiRlBOICsgYm90dG9tLXVwIiwiU3RyaWRlLTIgY29udiArIGxhdGVyYWwiLCJEZXRlY3Rpb24sIFNlZ21lbnRhdGlvbiIsIk1lZGl1bSIsIkJpZGlyZWN0aW9uYWwgc2VtYW50aWMgKyBzcGF0aWFsIGZsb3ciXV19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Spatial Pyramid Pooling (SPP) — Multi-Scale Feature Aggregation

Spatial Pyramid Pooling (SPP) solves a fundamental mismatch between convolutional feature maps of arbitrary spatial size and downstream layers that require a fixed-length input. By pooling at multiple pyramid levels — 1×1, 2×2, and 4×4 grids — and concatenating the results, SPP produces a fixed-size descriptor regardless of input image resolution. This single idea spawned an entire family of multi-scale pooling architectures spanning image classification, object detection, and semantic segmentation.

## Fixed-Size Feature Vectors from Variable-Size Inputs

A standard CNN requires a fixed input size because fully-connected layers expect a fixed number of inputs. The spatial feature map from a conv layer has shape C×H×W where H and W depend on input dimensions. SPP resolves this by applying adaptive pooling at l pyramid levels with grid sizes s₁, s₂, ..., sₗ. Each level pools the C-channel map into C×sᵢ×sᵢ, which is then flattened. Outputs are concatenated to form a fixed vector of length C × Σ(sᵢ²). For pool sizes {1, 2, 4} and C=512, output is always 512×(1+4+16)=10,752 regardless of whether input is 224×224 or 640×480.

## SPP-Net: Computing Features Once for All Proposals

R-CNN (Girshick et al., 2014) runs a forward pass through the full CNN for each region proposal independently — typically 2,000 proposals per image, each resized to a fixed 227×227 crop. SPP-Net (He et al., 2015) eliminates this redundancy: it runs the convolutional layers once on the entire image to produce a shared feature map, then applies SPP to each proposal's region within that feature map. Since proposals overlap heavily, shared computation yields a 24–102× speedup. This insight — compute once, pool per region — directly inspired RoI Pooling in Fast R-CNN and RoI Align in Mask R-CNN.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SPPModule(nn.Module):
    '''Spatial Pyramid Pooling: pools at multiple grid sizes, concatenates.'''
    def __init__(self, pool_sizes=(1, 2, 4)):
        super().__init__()
        self.pool_sizes = pool_sizes

    def forward(self, x):
        b, c, h, w = x.shape
        pooled = []
        for size in self.pool_sizes:
            out = F.adaptive_avg_pool2d(x, output_size=(size, size))
            pooled.append(out.view(b, -1))  # flatten each scale
        return torch.cat(pooled, dim=1)

    def output_dim(self, in_channels):
        return in_channels * sum(s * s for s in self.pool_sizes)

# Any input spatial size works — no cropping or warping needed
model = SPPModule(pool_sizes=(1, 2, 4))
for h, w in [(7, 7), (14, 10), (20, 15)]:
    x = torch.randn(2, 512, h, w)
    out = model(x)
    print('Input {}x{} -> SPP output dim: {}'.format(h, w, out.shape[1]))
print('Fixed output dim = 512*(1+4+16) = {:,}'.format(model.output_dim(512)))
```

## ASPP: Atrous Spatial Pyramid Pooling

DeepLab (Chen et al.) replaces standard max pooling with atrous (dilated) convolutions to capture multi-scale context without reducing feature map resolution. ASPP applies parallel 3×3 dilated convolutions with rates r ∈ {6, 12, 18}, plus a 1×1 conv and global average pooling, all operating on the same high-resolution feature map. With dilation rate r, a 3×3 kernel covers an effective receptive field of (r×2+1)² while maintaining full spatial resolution. Concatenating all branches and projecting with a 1×1 conv gives a rich multi-scale representation for per-pixel classification.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ASPPConv(nn.Module):
    def __init__(self, in_ch, out_ch, dilation):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=dilation, dilation=dilation, bias=False),
            nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True))
    def forward(self, x): return self.block(x)

class ASPPModule(nn.Module):
    '''Atrous Spatial Pyramid Pooling from DeepLab-v3.'''
    def __init__(self, in_ch=2048, out_ch=256, rates=(6, 12, 18)):
        super().__init__()
        self.conv1x1 = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 1, bias=False),
            nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True))
        self.atrous = nn.ModuleList([ASPPConv(in_ch, out_ch, r) for r in rates])
        self.global_pool = nn.Sequential(
            nn.AdaptiveAvgPool2d(1), nn.Conv2d(in_ch, out_ch, 1, bias=False),
            nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True))
        n_branches = 2 + len(rates)
        self.proj = nn.Sequential(
            nn.Conv2d(out_ch * n_branches, out_ch, 1, bias=False),
            nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True), nn.Dropout(0.5))

    def forward(self, x):
        h, w = x.shape[-2:]
        branches = [self.conv1x1(x)] + [a(x) for a in self.atrous]
        gp = F.interpolate(self.global_pool(x), (h, w), mode='bilinear', align_corners=False)
        return self.proj(torch.cat(branches + [gp], dim=1))

aspp = ASPPModule()
x = torch.randn(2, 2048, 32, 32)
print('ASPP input: {} -> output: {}'.format(x.shape, aspp(x).shape))
```

> **Choosing Dilation Rates**: ASPP rates {6, 12, 18} are calibrated for output stride 16 (feature map is 1/16 of input). Effective receptive fields become 13×13, 25×25, and 37×37. For output stride 8, rates {12, 24, 36} maintain equivalent coverage. Very large rates on small feature maps cause gridding artifacts — the dilated kernel samples mostly background — which is why a global pooling branch is always included to capture image-level context.

## PSPNet: Pyramid Pooling Module

Pyramid Scene Parsing Network (Zhao et al., 2017) applies global context via pooling at four sub-region sizes: 1×1 (global average), 2×2, 3×3, and 6×6. Each pooled representation passes through a 1×1 conv reducing channels to in_ch // 4, then is upsampled back to the original feature map size via bilinear interpolation. Concatenating these four context descriptors with the original feature map and applying a final bottleneck conv produces the output for pixel-wise classification. PSPNet won the ImageNet Scene Parsing Challenge 2016 with mIoU 85.4% on ADE20K.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class PyramidPoolingModule(nn.Module):
    '''PSPNet Pyramid Pooling Module (Zhao et al., 2017).'''
    def __init__(self, in_ch, pool_sizes=(1, 2, 3, 6)):
        super().__init__()
        mid_ch = in_ch // len(pool_sizes)
        self.stages = nn.ModuleList([
            nn.Sequential(
                nn.AdaptiveAvgPool2d(s),
                nn.Conv2d(in_ch, mid_ch, 1, bias=False),
                nn.BatchNorm2d(mid_ch), nn.ReLU(inplace=True)
            ) for s in pool_sizes
        ])
        self.bottleneck = nn.Sequential(
            nn.Conv2d(in_ch + mid_ch * len(pool_sizes), in_ch // 2, 3,
                      padding=1, bias=False),
            nn.BatchNorm2d(in_ch // 2), nn.ReLU(inplace=True))

    def forward(self, x):
        h, w = x.shape[-2:]
        out = [x]
        for stage in self.stages:
            pooled = stage(x)
            out.append(F.interpolate(pooled, (h, w), mode='bilinear', align_corners=False))
        return self.bottleneck(torch.cat(out, dim=1))

ppm = PyramidPoolingModule(in_ch=2048)
x = torch.randn(2, 2048, 60, 60)
out = ppm(x)
print('PPM {} -> {}'.format(x.shape, out.shape))
print('Output channels: {} (in_ch // 2)'.format(out.shape[1]))
```

## SPPF: Sequential Max Pooling in YOLOv5

SPPF (Spatial Pyramid Pooling — Fast) replaces parallel multi-scale max pools with three sequential 5×5 max pools. A single 5×5 pool covers a 5×5 region; two sequential 5×5 pools cover 9×9; three cover 13×13. This matches the receptive fields of parallel 5×5, 9×9, and 13×13 pools but runs faster because sequential pools share computation. YOLOv5 inserts SPPF at the end of its backbone (after CSP layers) to aggregate global context before the PANet neck. A channel-halving 1×1 conv precedes the pools and a 1×1 conv projects the concatenated 4-way output, keeping latency low.

```python
import torch
import torch.nn as nn

class SPPF(nn.Module):
    '''SPPF: Spatial Pyramid Pooling - Fast (YOLOv5).
    Three sequential 5x5 max pools give effective RFs of 5x5, 9x9, 13x13.
    Faster than parallel SPP due to shared intermediate computations.
    '''
    def __init__(self, in_ch, out_ch, k=5):
        super().__init__()
        mid_ch = in_ch // 2
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_ch, mid_ch, 1, bias=False),
            nn.BatchNorm2d(mid_ch), nn.SiLU())
        self.pool = nn.MaxPool2d(k, stride=1, padding=k // 2)
        self.conv2 = nn.Sequential(
            nn.Conv2d(mid_ch * 4, out_ch, 1, bias=False),
            nn.BatchNorm2d(out_ch), nn.SiLU())

    def forward(self, x):
        x = self.conv1(x)
        p1 = self.pool(x)
        p2 = self.pool(p1)
        p3 = self.pool(p2)
        return self.conv2(torch.cat([x, p1, p2, p3], dim=1))

sppf = SPPF(in_ch=512, out_ch=512)
x = torch.randn(1, 512, 20, 20)
out = sppf(x)
params = sum(p.numel() for p in sppf.parameters())
print('SPPF {} -> {}'.format(x.shape, out.shape))
print('Parameters: {:,}'.format(params))
```

## PANet and Multi-Scale Feature Aggregation

Path Aggregation Network (PANet, Liu et al. 2018) extends FPN by adding a bottom-up path augmentation after the standard top-down FPN pathway. FPN propagates strong semantic features from low-resolution layers upward to high-resolution layers. PANet adds a shortcut from the low-level features back up through the hierarchy, so high-resolution spatial detail (edges, textures) flows upward into high-level semantic representations. This bidirectional flow — top-down semantics + bottom-up spatial detail — improves instance segmentation and detection across scales. YOLOv5, YOLOv8, and PP-YOLO all adopt PANet-style necks.

- FPN top-down path: C5 (low-res, high-semantic) → C4 → C3 (high-res) via upsampling and lateral connections.
- PANet bottom-up path: P3 (high-res) → P4 → P5 (low-res) via stride-2 downsampling and lateral connections.
- Each feature map now sees both top-down context (long path) and bottom-up spatial detail (short path).
- Adaptive Feature Pooling: RoI features are pooled from all pyramid levels and fused, ensuring proposals see context at every scale.
- SPPF is typically placed at the backbone output before the PANet neck to provide global receptive field coverage.

## Comparing SPP Variants

The SPP family spans pooling strategies optimised for different tasks. Classification networks need fixed-size descriptors; segmentation models need full-resolution outputs with multi-scale context; detection backbones need speed with global receptive field; multi-scale necks need bidirectional information flow across pyramid levels.

| Variant | Scales / Rates | Pooling Op | Task | Latency | Key Benefit |
| --- | --- | --- | --- | --- | --- |
| SPP (He 2015) | {1×1, 2×2, 4×4} | Adaptive max pool | Classification, Detection | Medium | Fixed output from any input size |
| ASPP (DeepLab) | Dilation {6, 12, 18} | Dilated 3×3 conv | Semantic segmentation | High | Full-resolution multi-scale context |
| PSPNet PPM | {1, 2, 3, 6} grid | Avg pool + upsample | Semantic segmentation | Medium | Global scene context pooling |
| SPPF (YOLOv5) | 5×5 sequential × 3 | Sequential max pool | Object detection | Low | Fast multi-scale RF expansion |
| PANet | FPN + bottom-up | Stride-2 conv + lateral | Detection, Segmentation | Medium | Bidirectional semantic + spatial flow |

---

