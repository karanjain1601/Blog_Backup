---
title: "Receptive Field — Theoretical vs Effective, Depth and Dilation"
slug: "receptive-field-cnn"
description: "Compute theoretical receptive fields layer by layer, understand why the effective RF is Gaussian-shaped, and compare RF expansion strategies across architectures."
tags: ["deep-learning", "cnns"]
topic: "deep-learning"
status: "published"
updated: "2026-07-10"
blocks_json: "W3sidHlwZSI6InRleHQiLCJjb250ZW50IjoiVGhlIHJlY2VwdGl2ZSBmaWVsZCAoUkYpIG9mIGEgbmV1cm9uIGluIGEgQ05OIGlzIHRoZSByZWdpb24gb2YgdGhlIGlucHV0IGltYWdlIHRoYXQgY2FuIGluZmx1ZW5jZSBpdHMgYWN0aXZhdGlvbi4gUkYgc2l6ZSBkZXRlcm1pbmVzIHdoYXQgdGhlIG5ldHdvcmsgY2FuIFx1MDAyN3NlZVx1MDAyNyDigJQgdG9vIHNtYWxsIGFuZCBpdCBtaXNzZXMgZ2xvYmFsIGNvbnRleHQgbmVlZGVkIGZvciBvYmplY3QgcmVjb2duaXRpb247IHRvbyBsYXJnZSBhbmQgaXQgcHJvY2Vzc2VzIGlycmVsZXZhbnQgYmFja2dyb3VuZC4gVW5kZXJzdGFuZGluZyBob3cgUkYgZ3Jvd3Mgd2l0aCBkZXB0aCwgc3RyaWRlLCBkaWxhdGlvbiwgYW5kIGtlcm5lbCBzaXplIGxldHMgYXJjaGl0ZWN0cyBtYWtlIGRlbGliZXJhdGUgZGVzaWduIGRlY2lzaW9ucyByYXRoZXIgdGhhbiB0cmVhdGluZyB0aGUgUkYgYXMgYW4gYWZ0ZXJ0aG91Z2h0LiBBIGtleSBpbnNpZ2h0IGZyb20gTHVvIGV0IGFsLiAoMjAxNyk6IHRoZSBlZmZlY3RpdmUgUkYg4oCUIHRoZSByZWdpb24gdGhhdCBhY3R1YWxseSBpbmZsdWVuY2VzIHRoZSBvdXRwdXQgaW4gcHJvcG9ydGlvbiB0byBncmFkaWVudCBtYWduaXR1ZGUg4oCUIGlzIG11Y2ggc21hbGxlciBhbmQgR2F1c3NpYW4tc2hhcGVkLCBub3QgdGhlIGZ1bGwgdGhlb3JldGljYWwgc3F1YXJlLiJ9LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IlRoZW9yZXRpY2FsIFJlY2VwdGl2ZSBGaWVsZCBGb3JtdWxhIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJGb3IgYSBuZXR3b3JrIHdpdGggTCBsYXllcnMsIHRoZSB0aGVvcmV0aWNhbCBSRiBjYW4gYmUgY29tcHV0ZWQgcmVjdXJzaXZlbHkuIExldCBSRuKCgCA9IDEgKHNpbmdsZSBpbnB1dCBwaXhlbCkuIEFmdGVyIGxheWVyIGwgd2l0aCBrZXJuZWwgc2l6ZSBr4oKXIGFuZCBzdHJpZGUgc+KClzogUkZfbCA9IFJGX3tsLTF9ICsgKGvigpcgLSAxKSDCtyDOoOG1ouKCjOKCgcuh4oG7wrkgc+G1oi4gRXF1aXZhbGVudGx5LCBSRl9sID0gUkZfe2wtMX0gKyAoa+KClyAtIDEpIMK3IGp1bXBfe2wtMX0sIHdoZXJlIGp1bXBfe2wtMX0gPSDOoOG1olx1MDAzY2wgc+G1oiBpcyB0aGUgc3RyaWRlIGFjY3VtdWxhdGVkIHVwIHRvIGxheWVyIGwtMS4gRm9yIG4gc3RhY2tlZCAzw5czIGNvbnZzIHdpdGggc3RyaWRlIDE6IFJGID0gMm4rMS4gRm9yIG4gc3RhY2tlZCAzw5czIGNvbnZzIHdpdGggc3RyaWRlIDI6IFJGIGdyb3dzIGV4cG9uZW50aWFsbHkuIFBvb2xpbmcgbGF5ZXJzIGNvdW50IGFzIGNvbnZvbHV0aW9ucyB3aXRoIHN0cmlkZSBlcXVhbCB0byB0aGUgcG9vbCBzaXplLiBBIDHDlzEgY29udiBkb2VzIG5vdCBpbmNyZWFzZSB0aGUgUkYuIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImRlZiBjb21wdXRlX3JmKGxheWVycyk6XG4gICAgXCJcIlwiXG4gICAgQ29tcHV0ZSB0aGVvcmV0aWNhbCByZWNlcHRpdmUgZmllbGQgbGF5ZXItYnktbGF5ZXIuXG4gICAgbGF5ZXJzOiBsaXN0IG9mIGRpY3RzIHdpdGgga2V5cyBcdTAwMjduYW1lXHUwMDI3LCBcdTAwMjdrZXJuZWxcdTAwMjcsIFx1MDAyN3N0cmlkZVx1MDAyNywgXHUwMDI3ZGlsYXRpb25cdTAwMjcuXG4gICAgUmV0dXJucyBsaXN0IG9mIChuYW1lLCByZiwganVtcCwgZGlsYXRpb25fZWZmX2tlcm5lbCkuXG4gICAgXCJcIlwiXG4gICAgcmYsIGp1bXAgPSAxLCAxXG4gICAgcmVzdWx0cyA9IFtdXG4gICAgZm9yIGwgaW4gbGF5ZXJzOlxuICAgICAgICBrID0gbC5nZXQoXHUwMDI3a2VybmVsXHUwMDI3LCAxKVxuICAgICAgICBzID0gbC5nZXQoXHUwMDI3c3RyaWRlXHUwMDI3LCAxKVxuICAgICAgICBkID0gbC5nZXQoXHUwMDI3ZGlsYXRpb25cdTAwMjcsIDEpXG4gICAgICAgIGVmZl9rID0gKGsgLSAxKSAqIGQgKyAxICAjIGVmZmVjdGl2ZSBrZXJuZWwgc2l6ZSB3aXRoIGRpbGF0aW9uXG4gICAgICAgIHJmID0gcmYgKyAoZWZmX2sgLSAxKSAqIGp1bXBcbiAgICAgICAganVtcCA9IGp1bXAgKiBzXG4gICAgICAgIHJlc3VsdHMuYXBwZW5kKChsW1x1MDAyN25hbWVcdTAwMjddLCByZiwganVtcCkpXG4gICAgcmV0dXJuIHJlc3VsdHNcblxuIyBWR0ctc3R5bGU6IGZpdmUgYmxvY2tzIG9mIDN4MyBjb252cyArIG1heC1wb29sXG52Z2dfbGF5ZXJzID0gW1xuICAgICpbe1x1MDAyN25hbWVcdTAwMjc6IGZcdTAwMjdibG9jazFfY29udntpfVx1MDAyNywgXHUwMDI3a2VybmVsXHUwMDI3OiAzLCBcdTAwMjdzdHJpZGVcdTAwMjc6IDF9IGZvciBpIGluIHJhbmdlKDEsMyldLFxuICAgIHtcdTAwMjduYW1lXHUwMDI3OiBcdTAwMjdwb29sMVx1MDAyNywgXHUwMDI3a2VybmVsXHUwMDI3OiAyLCBcdTAwMjdzdHJpZGVcdTAwMjc6IDJ9LFxuICAgICpbe1x1MDAyN25hbWVcdTAwMjc6IGZcdTAwMjdibG9jazJfY29udntpfVx1MDAyNywgXHUwMDI3a2VybmVsXHUwMDI3OiAzLCBcdTAwMjdzdHJpZGVcdTAwMjc6IDF9IGZvciBpIGluIHJhbmdlKDEsMyldLFxuICAgIHtcdTAwMjduYW1lXHUwMDI3OiBcdTAwMjdwb29sMlx1MDAyNywgXHUwMDI3a2VybmVsXHUwMDI3OiAyLCBcdTAwMjdzdHJpZGVcdTAwMjc6IDJ9LFxuICAgICpbe1x1MDAyN25hbWVcdTAwMjc6IGZcdTAwMjdibG9jazNfY29udntpfVx1MDAyNywgXHUwMDI3a2VybmVsXHUwMDI3OiAzLCBcdTAwMjdzdHJpZGVcdTAwMjc6IDF9IGZvciBpIGluIHJhbmdlKDEsMyldLFxuICAgIHtcdTAwMjduYW1lXHUwMDI3OiBcdTAwMjdwb29sM1x1MDAyNywgXHUwMDI3a2VybmVsXHUwMDI3OiAyLCBcdTAwMjdzdHJpZGVcdTAwMjc6IDJ9LFxuXVxucHJpbnQoZlx1MDAyN3tcdTAwMjdMYXllclx1MDAyNzpcdTAwM2MxOH0ge1x1MDAyN1RoZW9yLiBSRlx1MDAyNzpcdTAwM2UxMH0ge1x1MDAyN0p1bXBcdTAwMjc6XHUwMDNlNn1cdTAwMjcpXG5mb3IgbmFtZSwgcmYsIGp1bXAgaW4gY29tcHV0ZV9yZih2Z2dfbGF5ZXJzKTpcbiAgICBwcmludChmXHUwMDI3e25hbWU6XHUwMDNjMTh9IHtyZjpcdTAwM2UxMH0ge2p1bXA6XHUwMDNlNn1cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiRWZmZWN0aXZlIFJlY2VwdGl2ZSBGaWVsZCJ9LHsidHlwZSI6InRleHQiLCJjb250ZW50IjoiTHVvIGV0IGFsLiAoMjAxNykgc2hvd2VkIHRoYXQgdGhlIGVmZmVjdGl2ZSBSRiDigJQgbWVhc3VyZWQgYXMgdGhlIGdyYWRpZW50IG9mIHRoZSBjZW50cmUgb3V0cHV0IHVuaXQgd2l0aCByZXNwZWN0IHRvIGFsbCBpbnB1dCBwaXhlbHMg4oCUIGlzIGFwcHJveGltYXRlbHkgR2F1c3NpYW4sIG5vdCB1bmlmb3JtIG92ZXIgdGhlIHRoZW9yZXRpY2FsIFJGIHNxdWFyZS4gQ2VudHJhbCBwaXhlbHMgY29udHJpYnV0ZSBleHBvbmVudGlhbGx5IG1vcmUgdGhhbiBwZXJpcGhlcmFsIG9uZXMgZHVlIHRvIHRoZSBtdWx0aXBsaWNhdGl2ZSBwYXRoLWNvdW50IGVmZmVjdDogYSBwaXhlbCBhdCB0aGUgY2VudHJlIG9mIHRoZSBSRiBwYXNzZXMgdGhyb3VnaCBtb3JlIG92ZXJsYXBwaW5nIGtlcm5lbCB3aW5kb3dzIHRoYW4gb25lIGF0IHRoZSBlZGdlLiBUaGUgZWZmZWN0aXZlIFJGIHR5cGljYWxseSBzcGFucyBhYm91dCDiiJoodGhlb3JldGljYWwgUkYpIGluIHByYWN0aWNlLiBUaGlzIG1lYW5zIGEgUmVzTmV0LTUwIHdpdGggYSB0aGVvcmV0aWNhbCBSRiBvZiA0ODPDlzQ4MyBvbiBJbWFnZU5ldCBoYXMgYW4gZWZmZWN0aXZlIFJGIG9mIHJvdWdobHkgMTAww5cxMDAuIEluY3JlYXNpbmcgZGVwdGggYmV5b25kIGEgY2VydGFpbiBwb2ludCBnaXZlcyBkaW1pbmlzaGluZyByZXR1cm5zIG9uIGVmZmVjdGl2ZSBjb250ZXh0LiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2hcbmltcG9ydCB0b3JjaC5ubiBhcyBublxuaW1wb3J0IG51bXB5IGFzIG5wXG5cbmRlZiBlc3RpbWF0ZV9lZmZlY3RpdmVfcmYobW9kZWwsIGlucHV0X3NpemU9KDEsIDMsIDIyNCwgMjI0KSk6XG4gICAgXCJcIlwiR3JhZGllbnQtYmFzZWQgZWZmZWN0aXZlIHJlY2VwdGl2ZSBmaWVsZCBlc3RpbWF0aW9uLlwiXCJcIlxuICAgIHggPSB0b3JjaC56ZXJvcyhpbnB1dF9zaXplLCByZXF1aXJlc19ncmFkPVRydWUpXG4gICAgIyBGb3J3YXJkIHBhc3NcbiAgICBvdXQgPSBtb2RlbCh4KVxuICAgICMgR3JhZGllbnQgb2YgY2VudHJlIG91dHB1dCB3LnIudC4gaW5wdXRcbiAgICBjZW50cmUgPSBvdXRbMCwgMCwgb3V0LnNoYXBlWzJdLy8yLCBvdXQuc2hhcGVbM10vLzJdXG4gICAgY2VudHJlLmJhY2t3YXJkKClcbiAgICBncmFkID0geC5ncmFkWzBdLmFicygpLm1lYW4oZGltPTApLmRldGFjaCgpLm51bXB5KCkgICMgKEgsIFcpXG4gICAgIyBOb3JtYWxpc2VcbiAgICBncmFkID0gZ3JhZCAvIGdyYWQubWF4KClcbiAgICAjIEVzdGltYXRlIGVmZmVjdGl2ZSBSRiBhcyByZWdpb24gd2l0aCBncmFkIFx1MDAzZSB0aHJlc2hvbGRcbiAgICB0aHJlc2hvbGQgPSAwLjFcbiAgICBtYXNrID0gKGdyYWQgXHUwMDNlIHRocmVzaG9sZClcbiAgICByb3dzID0gbnAuYW55KG1hc2ssIGF4aXM9MSlcbiAgICBjb2xzID0gbnAuYW55KG1hc2ssIGF4aXM9MClcbiAgICBoX2VmZiA9IHJvd3Muc3VtKClcbiAgICB3X2VmZiA9IGNvbHMuc3VtKClcbiAgICByZXR1cm4gZ3JhZCwgaF9lZmYsIHdfZWZmXG5cbiMgVXNlIGEgc21hbGwgY3VzdG9tIG5ldHdvcmsgZm9yIGRlbW9uc3RyYXRpb25cbm5ldCA9IG5uLlNlcXVlbnRpYWwoXG4gICAgbm4uQ29udjJkKDMsIDMyLCAzLCBwYWRkaW5nPTEpLCBubi5SZUxVKCksXG4gICAgbm4uQ29udjJkKDMyLCAzMiwgMywgcGFkZGluZz0xKSwgbm4uUmVMVSgpLFxuICAgIG5uLkNvbnYyZCgzMiwgMzIsIDMsIHBhZGRpbmc9MSksIG5uLlJlTFUoKSxcbiAgICBubi5Db252MmQoMzIsIDEsIDMsIHBhZGRpbmc9MSksXG4pXG5ncmFkLCBoX2VmZiwgd19lZmYgPSBlc3RpbWF0ZV9lZmZlY3RpdmVfcmYobmV0LCAoMSwgMywgMzIsIDMyKSlcbnRoZW9yX3JmID0gMiAqIDQgKyAxICAjIDQgbGF5ZXJzIG9mIGs9Mywgcz0xXG5wcmludChmXHUwMDI3VGhlb3JldGljYWwgUkY6IHt0aGVvcl9yZn14e3RoZW9yX3JmfVx1MDAyNylcbnByaW50KGZcdTAwMjdFZmZlY3RpdmUgUkYgKGdyYWRcdTAwM2UwLjEpOiB7aF9lZmZ9eHt3X2VmZn1cdTAwMjcpXG5wcmludChmXHUwMDI3R3JhZGllbnQgaXMgR2F1c3NpYW4tc2hhcGVkLCBub3QgdW5pZm9ybSByZWN0YW5ndWxhci5cdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUkYgR3Jvd3RoIHdpdGggRGlsYXRpb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpbGF0ZWQgY29udm9sdXRpb25zIGV4cGFuZCB0aGUgUkYgd2l0aG91dCBpbmNyZWFzaW5nIHBhcmFtZXRlcnMgb3IgcmVkdWNpbmcgc3BhdGlhbCByZXNvbHV0aW9uLiBBIDPDlzMgY29udiB3aXRoIGRpbGF0aW9uIGQgaGFzIGVmZmVjdGl2ZSBrZXJuZWwgc2l6ZSAoMy0xKcK3ZCsxLiBTdGFja2luZyB0aHJlZSAzw5czIGRpbGF0ZWQgY29udnMgd2l0aCByYXRlcyBkPVsxLDIsNF06IFJGIGNvbnRyaWJ1dGlvbnMgYXJlIDMsIDUsIDkgKGVmZmVjdGl2ZSBrZXJuZWwgc2l6ZXMpLiBXaXRoIHN0cmlkZT0xLCB0aGUgdG90YWwgUkYgPSAxICsgKDMtMSkgKyAoNS0xKcK3MSArICg5LTEpwrcxID0gMTUgdnMgNyBmb3Igc3RhbmRhcmQgKHRocmVlIGQ9MSBjb252cykuIFdhdmVOZXQgdXNlZCBleHBvbmVudGlhbGx5IGdyb3dpbmcgZGlsYXRpb24gWzEsMiw0LC4uLiw1MTJdIGluIGVhY2ggYmxvY2ssIGFjaGlldmluZyBhbiBSRiBvZiAxMDI0IHNhbXBsZXMgYXQgMTZrSHogPSA2NG1zIGNvbnRleHQuIERlZXBMYWJWMyB1c2VzIGRpbGF0aW9ucyBbNiwxMiwxOF0gaW4gQVNQUCBmb3IgbXVsdGktc2NhbGUgY29udGV4dCBpbiBzZWdtZW50YXRpb24uIn0seyJ0eXBlIjoiY29kZSIsImxhbmd1YWdlIjoicHl0aG9uIiwiY29udGVudCI6ImltcG9ydCB0b3JjaFxuaW1wb3J0IHRvcmNoLm5uIGFzIG5uXG5cbmRlZiByZl93aXRoX2RpbGF0aW9uKGRpbGF0aW9ucywgaz0zKTpcbiAgICBcIlwiXCJDb21wYXJlIFJGIGZvciBzdGFja2VkIGRpbGF0ZWQgM3gzIGNvbnZzIHZzIHN0YW5kYXJkLlwiXCJcIlxuICAgIHJmX3N0ZCA9IDEgKyBsZW4oZGlsYXRpb25zKSAqIChrIC0gMSkgICMgYWxsIGRpbGF0aW9uPTFcbiAgICByZl9kaWwgPSAxXG4gICAgZm9yIGQgaW4gZGlsYXRpb25zOlxuICAgICAgICBlZmZfayA9IChrIC0gMSkgKiBkICsgMVxuICAgICAgICByZl9kaWwgKz0gZWZmX2sgLSAxXG4gICAgcmV0dXJuIHJmX3N0ZCwgcmZfZGlsXG5cbnByaW50KGZcdTAwMjd7XHUwMDI3RGlsYXRpb25zXHUwMDI3Olx1MDAzYzMwfSB7XHUwMDI3U3RkIFJGXHUwMDI3Olx1MDAzZTh9IHtcdTAwMjdEaWxhdGVkIFJGXHUwMDI3Olx1MDAzZTEyfSB7XHUwMDI3R2Fpblx1MDAyNzpcdTAwM2U4fVx1MDAyNylcbmZvciBkaWxhdGlvbnMgaW4gW1xuICAgIFsxLCAxLCAxXSxcbiAgICBbMSwgMiwgNF0sXG4gICAgWzEsIDIsIDQsIDhdLFxuICAgIFsxLCAyLCA0LCA4LCAxNl0sXG4gICAgWzEsIDIsIDQsIDgsIDE2LCAzMl0sXG4gICAgWzYsIDEyLCAxOF0sICAgICAgICAgIyBEZWVwTGFiIEFTUFBcbiAgICBbMSwgMiwgNV0sICAgICAgICAgICAjIEh5YnJpZCBkaWxhdGVkIGNvbnYgKEhEQylcbl06XG4gICAgc3RkLCBkaWwgPSByZl93aXRoX2RpbGF0aW9uKGRpbGF0aW9ucylcbiAgICBwcmludChmXHUwMDI3e3N0cihkaWxhdGlvbnMpOlx1MDAzYzMwfSB7c3RkOlx1MDAzZTh9IHtkaWw6XHUwMDNlMTJ9IHtkaWwvc3RkOlx1MDAzZTcuMWZ9eFx1MDAyNylcblxucHJpbnQoXHUwMDI3XFxuRGlsYXRpb24gbXVsdGlwbGllcyBSRiB3aXRoIG5vIGV4dHJhIHBhcmFtZXRlcnMuXHUwMDI3KVxucHJpbnQoXHUwMDI3SERDIFsxLDIsNV06IGF2b2lkcyBncmlkZGluZyBhcnRpZmFjdCAoYWxsIHBvc2l0aW9ucyBjb3ZlcmVkKS5cdTAwMjcpIn0seyJ0eXBlIjoiY2FsbG91dCIsInZhcmlhbnQiOiJpbmZvIiwidGl0bGUiOiJUcmFuc2Zvcm1lciBHbG9iYWwgUkYgZnJvbSBMYXllciAxIiwiY29udGVudCI6IlZpc2lvbiBUcmFuc2Zvcm1lcnMgKFZpVCkgZGl2aWRlIHRoZSBpbWFnZSBpbnRvIHBhdGNoZXMgYW5kIGFwcGx5IHNlbGYtYXR0ZW50aW9uIGFjcm9zcyBhbGwgcGF0Y2ggdG9rZW5zLiBFdmVyeSB0b2tlbiBhdHRlbmRzIHRvIGV2ZXJ5IG90aGVyIHRva2VuIGZyb20gdGhlIHZlcnkgZmlyc3QgbGF5ZXIg4oCUIHRoZSByZWNlcHRpdmUgZmllbGQgaXMgZ2xvYmFsIGltbWVkaWF0ZWx5LiBDTk5zIGJ1aWxkIHVwIHRoZWlyIFJGIGluY3JlbWVudGFsbHkgdGhyb3VnaCBkZXB0aC4gVGhpcyBpcyB3aHkgVmlUcyBleGNlbCBhdCB0YXNrcyByZXF1aXJpbmcgbG9uZy1yYW5nZSBkZXBlbmRlbmNpZXMgKGUuZy4sIGRldGVjdGluZyByZWxhdGlvbnNoaXBzIGJldHdlZW4gZGlzdGFudCBpbWFnZSByZWdpb25zKSwgd2hpbGUgQ05OcyB3aXRoIGxvY2FsIGluZHVjdGl2ZSBiaWFzIG9mdGVuIG5lZWQgZmV3ZXIgZGF0YSB0byBjb252ZXJnZSBvbiBzcGF0aWFsbHkgbG9jYWwgdGFza3MuIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiQXJjaGl0ZWN0dXJlIFJGIENvbXBhcmlzb24ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRpZmZlcmVudCBhcmNoaXRlY3R1cmVzIGFjaGlldmUgbGFyZ2UgUkZzIHRocm91Z2ggZGlmZmVyZW50IHN0cmF0ZWdpZXMuIFZHRy0xNiB1c2VzIDEzIGNvbnYgbGF5ZXJzIG9mIDPDlzMgd2l0aCBwZXJpb2RpYyAyw5cyIG1heC1wb29saW5nLCByZWFjaGluZyBhIHRoZW9yZXRpY2FsIFJGIG9mIDIxMsOXMjEyIG9uIHRoZSBmaW5hbCBjb252IGxheWVyLiBSZXNOZXQtNTAgdXNlcyBib3R0bGVuZWNrIGJsb2NrcyB3aXRoIDHDlzEsIDPDlzMsIDHDlzEgY29udnMgYW5kIHN0cmlkZS0yIGZvciBkb3duc2FtcGxpbmcuIFRoZSAxw5cxIGNvbnZzIGRvIG5vdCBncm93IHRoZSBSRi4gRGVlcExhYiBhZGRzIGRpbGF0ZWQgY29udnMgdG8gUmVzTmV0XHUwMDI3cyBsYXRlciBzdGFnZXMgdG8gcHJldmVudCBzaHJpbmtpbmcgdGhlIFJGIHdoaWxlIHJlbW92aW5nIHN0cmlkZXMuIFZpVCBwYXRjaGVzICgxNsOXMTYpIGdpdmUgYSBmaXhlZCBwYXRjaC1sZXZlbCBSRiBvZiAxNiBpbml0aWFsbHksIHRoZW4gZ2xvYmFsIHRocm91Z2ggYXR0ZW50aW9uLiJ9LHsidHlwZSI6ImNvZGUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImNvbnRlbnQiOiJpbXBvcnQgdG9yY2h2aXNpb24ubW9kZWxzIGFzIG1vZGVsc1xuaW1wb3J0IHRvcmNoXG5cbmRlZiByZXNuZXQ1MF9yZigpOlxuICAgIFwiXCJcIkNvbXB1dGUgdGhlb3JldGljYWwgUkYgdGhyb3VnaCBSZXNOZXQtNTAgdXAgdG8gbGF5ZXI0LlwiXCJcIlxuICAgIGxheWVycyA9IFtcbiAgICAgICAge1x1MDAyN25hbWVcdTAwMjc6IFx1MDAyN2NvbnYxIDd4NyBzMlx1MDAyNywgIFx1MDAyN2tlcm5lbFx1MDAyNzogNywgXHUwMDI3c3RyaWRlXHUwMDI3OiAyfSxcbiAgICAgICAge1x1MDAyN25hbWVcdTAwMjc6IFx1MDAyN21heHBvb2wgM3gzIHMyXHUwMDI3LFx1MDAyN2tlcm5lbFx1MDAyNzogMywgXHUwMDI3c3RyaWRlXHUwMDI3OiAyfSxcbiAgICAgICAgIyBsYXllcjE6IDMgYm90dGxlbmVjayBibG9ja3MsIGVhY2ggaGFzIDF4MSwgM3gzLCAxeDFcbiAgICAgICAgKlt7XHUwMDI3bmFtZVx1MDAyNzogZlx1MDAyN2wxLntpfS57bn1cdTAwMjcsIFx1MDAyN2tlcm5lbFx1MDAyNzogaywgXHUwMDI3c3RyaWRlXHUwMDI3OiAxfVxuICAgICAgICAgIGZvciBpIGluIHJhbmdlKDMpIGZvciBrLCBuIGluIFsoMSxcdTAwMjdwdzFcdTAwMjcpLCgzLFx1MDAyN2NvbnZcdTAwMjcpLCgxLFx1MDAyN3B3Mlx1MDAyNyldXSxcbiAgICAgICAgIyBsYXllcjI6IHN0cmlkZS0yIG9uIGZpcnN0IGJsb2NrXHUwMDI3cyAzeDNcbiAgICAgICAge1x1MDAyN25hbWVcdTAwMjc6IFx1MDAyN2wyLjAucHcxXHUwMDI3LCBcdTAwMjdrZXJuZWxcdTAwMjc6IDEsIFx1MDAyN3N0cmlkZVx1MDAyNzogMX0sXG4gICAgICAgIHtcdTAwMjduYW1lXHUwMDI3OiBcdTAwMjdsMi4wLmNvbnZcdTAwMjcsIFx1MDAyN2tlcm5lbFx1MDAyNzogMywgXHUwMDI3c3RyaWRlXHUwMDI3OiAyfSxcbiAgICAgICAge1x1MDAyN25hbWVcdTAwMjc6IFx1MDAyN2wyLjAucHcyXHUwMDI3LCBcdTAwMjdrZXJuZWxcdTAwMjc6IDEsIFx1MDAyN3N0cmlkZVx1MDAyNzogMX0sXG4gICAgICAgICpbe1x1MDAyN25hbWVcdTAwMjc6IGZcdTAwMjdsMi57aX0ue259XHUwMDI3LCBcdTAwMjdrZXJuZWxcdTAwMjc6IGssIFx1MDAyN3N0cmlkZVx1MDAyNzogMX1cbiAgICAgICAgICBmb3IgaSBpbiByYW5nZSgxLDQpIGZvciBrLCBuIGluIFsoMSxcdTAwMjdwdzFcdTAwMjcpLCgzLFx1MDAyN2NvbnZcdTAwMjcpLCgxLFx1MDAyN3B3Mlx1MDAyNyldXSxcbiAgICBdXG4gICAgcmYsIGp1bXAgPSAxLCAxXG4gICAgZm9yIGwgaW4gbGF5ZXJzOlxuICAgICAgICBrLCBzID0gbFtcdTAwMjdrZXJuZWxcdTAwMjddLCBsW1x1MDAyN3N0cmlkZVx1MDAyN11cbiAgICAgICAgcmYgPSByZiArIChrIC0gMSkgKiBqdW1wXG4gICAgICAgIGp1bXAgKj0gc1xuICAgIHJldHVybiByZiwganVtcFxuXG5yZiwganVtcCA9IHJlc25ldDUwX3JmKClcbnByaW50KGZcdTAwMjdSZXNOZXQtNTAgdGhlb3JldGljYWwgUkYgYWZ0ZXIgbGF5ZXIyOiB7cmZ9eHtyZn1cdTAwMjcpXG5wcmludChmXHUwMDI3VG90YWwgc3RyaWRlIChqdW1wKToge2p1bXB9XHUwMDI3KVxucHJpbnQoXHUwMDI3UmVzTmV0LTUwIGZ1bGwgdGhlb3JldGljYWwgUkYgYXQgb3V0cHV0OiB+NDgzeDQ4M1x1MDAyNylcbnByaW50KFx1MDAyN0VmZmVjdGl2ZSBSRiB0eXBpY2FsbHkgfjEwMHgxMDAgKEdhdXNzaWFuIGNlbnRyZS13ZWlnaHRlZClcdTAwMjcpIn0seyJ0eXBlIjoiaGVhZGluZyIsImxldmVsIjoyLCJjb250ZW50IjoiUkYgRGVzaWduIEd1aWRlbGluZXMifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IlByYWN0aWNhbCBSRiBkZXNpZ24gZm9sbG93cyBhIGZldyBndWlkaW5nIHByaW5jaXBsZXMuIEZvciBpbWFnZSBjbGFzc2lmaWNhdGlvbiwgdGhlIFJGIHNob3VsZCBjb3ZlciBtb3N0IG9mIHRoZSBpbnB1dCBieSB0aGUgZmluYWwgY29udiBsYXllciDigJQgYSAyMjTDlzIyNCBpbWFnZSBuZWVkcyBhbiBSRiBvZiBhdCBsZWFzdCAxMDDigJMxNTAgZWZmZWN0aXZlIHBpeGVscy4gRm9yIG9iamVjdCBkZXRlY3Rpb24sIHRoZSBSRiBzaG91bGQgbWF0Y2ggdGhlIG9iamVjdCBzY2FsZSBhdCBlYWNoIGRldGVjdGlvbiBoZWFkIOKAlCBGUE4gKEZlYXR1cmUgUHlyYW1pZCBOZXR3b3JrKSB1c2VzIG11bHRpcGxlIHNjYWxlcyBleHBsaWNpdGx5LiBGb3Igc2VnbWVudGF0aW9uIHdpdGhvdXQgZG93bnNhbXBsaW5nIChlLmcuLCBtZWRpY2FsIGltYWdlcyksIGRpbGF0ZWQgY29udiBpcyBwcmVmZXJyZWQgdG8gbWFpbnRhaW4gcmVzb2x1dGlvbiB3aGlsZSBleHBhbmRpbmcgUkYuIEZvciBhdWRpbyAoZS5nLiwgV2F2ZU5ldCksIGV4cG9uZW50aWFsbHkgZ3Jvd2luZyBkaWxhdGlvbiBnaXZlcyBsb2dhcml0aG1pYyBSRiBncm93dGgg4oCUIGVmZmljaWVudCBmb3IgbG9uZy1yYW5nZSB0ZW1wb3JhbCBkZXBlbmRlbmNpZXMuIn0seyJ0eXBlIjoidGFibGUiLCJoZWFkZXJzIjpbIlJGIEdyb3d0aCBTdHJhdGVneSIsIlJGIFBlciBMYXllciIsIkV4dHJhIFBhcmFtcyIsIkV4dHJhIEZMT1BzIiwiU3BhdGlhbCBSZXNvbHV0aW9uIiwiVXNlIENhc2UiXSwicm93cyI6W1siU3RhY2sgM8OXMyAocz0xKSIsIisyIHBlciBsYXllciAobGluZWFyKSIsIk5vbmUiLCJOb25lIiwiUHJlc2VydmVkIiwiRGVwdGgtZmlyc3QsIGNoZWFwIGxvY2FsIGdyb3d0aCJdLFsiRGlsYXRpb24gZCIsIisoMmQpIHBlciBsYXllciIsIk5vbmUiLCJOb25lIiwiUHJlc2VydmVkIiwiU2VnbWVudGF0aW9uLCBhdWRpbyAoRGVlcExhYiwgV2F2ZU5ldCkiXSxbIlN0cmlkZSAyIC8gUG9vbCIsIsOXMiBtdWx0aXBsaWVyIiwiTm9uZSIsIk5vbmUiLCJIYWx2ZWQiLCJDbGFzc2lmaWNhdGlvbiwgZGV0ZWN0aW9uIGJhY2tib25lIl0sWyJMYXJnZXIga2VybmVsIGsiLCIray0xIHBlciBsYXllciIsIsOXKGsvMynCsiIsIsOXKGsvMynCsiIsIlByZXNlcnZlZCIsIlJhcmU7IHR3byAzw5czIHByZWZlcnJlZCBvdmVyIG9uZSA1w5c1Il0sWyJHbG9iYWwgYXR0ZW50aW9uIiwiRnVsbCBpbWFnZSAoMSBsYXllcikiLCJPKG7CsikgUUtWIiwiTyhuwrLCt2QpIiwiUHJlc2VydmVkIiwiVmlULCBTQVNBLCBub24tbG9jYWwgbmV0d29ya3MiXV19LHsidHlwZSI6ImhlYWRpbmciLCJsZXZlbCI6MiwiY29udGVudCI6IkVmZmVjdGl2ZSBSRiBhbmQgRmVhdHVyZSBJbXBvcnRhbmNlIn0seyJ0eXBlIjoidGV4dCIsImNvbnRlbnQiOiJCZWNhdXNlIHRoZSBlZmZlY3RpdmUgUkYgaXMgR2F1c3NpYW4tc2hhcGVkIGFuZCBtdWNoIHNtYWxsZXIgdGhhbiB0aGUgdGhlb3JldGljYWwgUkYsIGFyY2hpdGVjdHVyYWwgY2hvaWNlcyB0aGF0IHNlZW0gdG8gcHJvdmlkZSBzdWZmaWNpZW50IGNvbnRleHQgbWF5IG5vdCBpbiBwcmFjdGljZS4gQXR0ZW50aW9uIG1lY2hhbmlzbXMgKENCQU0sIFNFIGJsb2NrcywgVHJhbnNmb3JtZXIgbGF5ZXJzKSBjb21wbGVtZW50IENOTnMgYnkgcHJvdmlkaW5nIGEgYnlwYXNzIHJvdXRlIGZvciBsb25nLXJhbmdlIGRlcGVuZGVuY3kgbW9kZWxsaW5nIHRoYXQgdGhlIEdhdXNzaWFuLXNoYXBlZCBFUkYgc3VwcHJlc3Nlcy4gQ2xhc3MgQWN0aXZhdGlvbiBNYXBwaW5nIChDQU0pIGFuZCBHcmFkLUNBTSBleHBsb2l0IHRoZSBzcGF0aWFsIFJGIHN0cnVjdHVyZSB0byB2aXN1YWxpc2Ugd2hpY2ggaW5wdXQgcmVnaW9ucyBkcml2ZSBhIGNsYXNzaWZpY2F0aW9uIGRlY2lzaW9uLCBzZXJ2aW5nIGFzIGEgZGlhZ25vc3RpYyB0b29sIGZvciBjaGVja2luZyB3aGV0aGVyIHRoZSBuZXR3b3JrXHUwMDI3cyBhdHRlbmRlZCByZWdpb25zIG1hdGNoIGh1bWFuIGludHVpdGlvbi4ifSx7InR5cGUiOiJ0ZXh0IiwiY29udGVudCI6IkRlZm9ybWFibGUgY29udm9sdXRpb25zIChEYWkgZXQgYWwuIDIwMTcpIGxlYXJuIHNwYXRpYWwgb2Zmc2V0cyBmb3IgZWFjaCBrZXJuZWwgc2FtcGxpbmcgbG9jYXRpb24gc28gdGhlIFJGIGFkYXB0cyBkeW5hbWljYWxseSB0byBvYmplY3Qgc2hhcGUgcmF0aGVyIHRoYW4gcmVtYWluaW5nIGEgZml4ZWQgZ3JpZC4gVGhpcyBpbXByb3ZlcyBkZXRlY3Rpb24gb2Ygb2JqZWN0cyB3aXRoIGlycmVndWxhciBzaGFwZXMgYW5kIGxhcmdlIGFzcGVjdCByYXRpb3MuIERlZm9ybWFibGUgREVUUiB1c2VzIGRlZm9ybWFibGUgYXR0ZW50aW9uIGZvciBtdWx0aS1zY2FsZSBmZWF0dXJlIGFnZ3JlZ2F0aW9uIHdpdGggYWRhcHRpdmUgUkYuIERpbGF0ZWQgUmVzaWR1YWwgTmV0d29ya3MgKERSTikgcmVtb3ZlIHN0cmlkZXMgaW4gUmVzTmV0XHUwMDI3cyBsYXN0IHR3byBzdGFnZXMgYW5kIGNvbXBlbnNhdGUgd2l0aCBpbmNyZWFzaW5nIGRpbGF0aW9uIHJhdGVzIHRvIG1haW50YWluIHRoZSBmdWxsIHRoZW9yZXRpY2FsIFJGIGF0IGhpZ2hlciBzcGF0aWFsIHJlc29sdXRpb24uIn0seyJ0eXBlIjoibGlzdCIsIm9yZGVyZWQiOmZhbHNlLCJpdGVtcyI6WyJHcmFkLUNBTSB1c2VzIHRoZSBncmFkaWVudCBvZiBjbGFzcyBzY29yZSB3LnIudC4gdGhlIGxhc3QgY29udiBmZWF0dXJlIG1hcCBmb3IgY2xhc3Mtc3BlY2lmaWMgc2FsaWVuY3kgbWFwcy4iLCJMb2NhbCBBdHRlbnRpb24gKFNBU0EpIHJlc3RyaWN0cyBzZWxmLWF0dGVudGlvbiB0byBhIGxvY2FsIHdpbmRvdyDigJQgZXhwbGljaXQgUkYgY29udHJvbCB3aXRoIE8obsK3d8KyKSBjb3N0LiIsInRvcmNoLmZ4IGNhbiB0cmFjZSBhIG1vZGVsIGdyYXBoIGFuZCBjb21wdXRlIHRoZW9yZXRpY2FsIFJGIGJ5IHRyYWNraW5nIHRlbnNvciBzaGFwZXMgbGF5ZXIgYnkgbGF5ZXIuIiwiUkYgbWlzbWF0Y2g6IGlmIGFuIG9iamVjdCBpcyBsYXJnZXIgdGhhbiB0aGUgbmV0d29ya1x1MDAyN3MgRVJGLCBhY2N1cmFjeSBjb2xsYXBzZXMg4oCUIGEgY29tbW9uIGZhaWx1cmUgbW9kZSBvbiBoaWdoLXJlcyBpbnB1dHMuIl19LHsidHlwZSI6ImRpdmlkZXIifV0="
---
# Receptive Field — Theoretical vs Effective, Depth and Dilation

The receptive field (RF) of a neuron in a CNN is the region of the input image that can influence its activation. RF size determines what the network can 'see' — too small and it misses global context needed for object recognition; too large and it processes irrelevant background. Understanding how RF grows with depth, stride, dilation, and kernel size lets architects make deliberate design decisions rather than treating the RF as an afterthought. A key insight from Luo et al. (2017): the effective RF — the region that actually influences the output in proportion to gradient magnitude — is much smaller and Gaussian-shaped, not the full theoretical square.

## Theoretical Receptive Field Formula

For a network with L layers, the theoretical RF can be computed recursively. Let RF₀ = 1 (single input pixel). After layer l with kernel size kₗ and stride sₗ: RF_l = RF_{l-1} + (kₗ - 1) · Πᵢ₌₁ˡ⁻¹ sᵢ. Equivalently, RF_l = RF_{l-1} + (kₗ - 1) · jump_{l-1}, where jump_{l-1} = Πᵢ<l sᵢ is the stride accumulated up to layer l-1. For n stacked 3×3 convs with stride 1: RF = 2n+1. For n stacked 3×3 convs with stride 2: RF grows exponentially. Pooling layers count as convolutions with stride equal to the pool size. A 1×1 conv does not increase the RF.

```python
def compute_rf(layers):
    """
    Compute theoretical receptive field layer-by-layer.
    layers: list of dicts with keys 'name', 'kernel', 'stride', 'dilation'.
    Returns list of (name, rf, jump, dilation_eff_kernel).
    """
    rf, jump = 1, 1
    results = []
    for l in layers:
        k = l.get('kernel', 1)
        s = l.get('stride', 1)
        d = l.get('dilation', 1)
        eff_k = (k - 1) * d + 1  # effective kernel size with dilation
        rf = rf + (eff_k - 1) * jump
        jump = jump * s
        results.append((l['name'], rf, jump))
    return results

# VGG-style: five blocks of 3x3 convs + max-pool
vgg_layers = [
    *[{'name': f'block1_conv{i}', 'kernel': 3, 'stride': 1} for i in range(1,3)],
    {'name': 'pool1', 'kernel': 2, 'stride': 2},
    *[{'name': f'block2_conv{i}', 'kernel': 3, 'stride': 1} for i in range(1,3)],
    {'name': 'pool2', 'kernel': 2, 'stride': 2},
    *[{'name': f'block3_conv{i}', 'kernel': 3, 'stride': 1} for i in range(1,3)],
    {'name': 'pool3', 'kernel': 2, 'stride': 2},
]
print(f'{'Layer':<18} {'Theor. RF':>10} {'Jump':>6}')
for name, rf, jump in compute_rf(vgg_layers):
    print(f'{name:<18} {rf:>10} {jump:>6}')
```

## Effective Receptive Field

Luo et al. (2017) showed that the effective RF — measured as the gradient of the centre output unit with respect to all input pixels — is approximately Gaussian, not uniform over the theoretical RF square. Central pixels contribute exponentially more than peripheral ones due to the multiplicative path-count effect: a pixel at the centre of the RF passes through more overlapping kernel windows than one at the edge. The effective RF typically spans about √(theoretical RF) in practice. This means a ResNet-50 with a theoretical RF of 483×483 on ImageNet has an effective RF of roughly 100×100. Increasing depth beyond a certain point gives diminishing returns on effective context.

```python
import torch
import torch.nn as nn
import numpy as np

def estimate_effective_rf(model, input_size=(1, 3, 224, 224)):
    """Gradient-based effective receptive field estimation."""
    x = torch.zeros(input_size, requires_grad=True)
    # Forward pass
    out = model(x)
    # Gradient of centre output w.r.t. input
    centre = out[0, 0, out.shape[2]//2, out.shape[3]//2]
    centre.backward()
    grad = x.grad[0].abs().mean(dim=0).detach().numpy()  # (H, W)
    # Normalise
    grad = grad / grad.max()
    # Estimate effective RF as region with grad > threshold
    threshold = 0.1
    mask = (grad > threshold)
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    h_eff = rows.sum()
    w_eff = cols.sum()
    return grad, h_eff, w_eff

# Use a small custom network for demonstration
net = nn.Sequential(
    nn.Conv2d(3, 32, 3, padding=1), nn.ReLU(),
    nn.Conv2d(32, 32, 3, padding=1), nn.ReLU(),
    nn.Conv2d(32, 32, 3, padding=1), nn.ReLU(),
    nn.Conv2d(32, 1, 3, padding=1),
)
grad, h_eff, w_eff = estimate_effective_rf(net, (1, 3, 32, 32))
theor_rf = 2 * 4 + 1  # 4 layers of k=3, s=1
print(f'Theoretical RF: {theor_rf}x{theor_rf}')
print(f'Effective RF (grad>0.1): {h_eff}x{w_eff}')
print(f'Gradient is Gaussian-shaped, not uniform rectangular.')
```

## RF Growth with Dilation

Dilated convolutions expand the RF without increasing parameters or reducing spatial resolution. A 3×3 conv with dilation d has effective kernel size (3-1)·d+1. Stacking three 3×3 dilated convs with rates d=[1,2,4]: RF contributions are 3, 5, 9 (effective kernel sizes). With stride=1, the total RF = 1 + (3-1) + (5-1)·1 + (9-1)·1 = 15 vs 7 for standard (three d=1 convs). WaveNet used exponentially growing dilation [1,2,4,...,512] in each block, achieving an RF of 1024 samples at 16kHz = 64ms context. DeepLabV3 uses dilations [6,12,18] in ASPP for multi-scale context in segmentation.

```python
import torch
import torch.nn as nn

def rf_with_dilation(dilations, k=3):
    """Compare RF for stacked dilated 3x3 convs vs standard."""
    rf_std = 1 + len(dilations) * (k - 1)  # all dilation=1
    rf_dil = 1
    for d in dilations:
        eff_k = (k - 1) * d + 1
        rf_dil += eff_k - 1
    return rf_std, rf_dil

print(f'{'Dilations':<30} {'Std RF':>8} {'Dilated RF':>12} {'Gain':>8}')
for dilations in [
    [1, 1, 1],
    [1, 2, 4],
    [1, 2, 4, 8],
    [1, 2, 4, 8, 16],
    [1, 2, 4, 8, 16, 32],
    [6, 12, 18],         # DeepLab ASPP
    [1, 2, 5],           # Hybrid dilated conv (HDC)
]:
    std, dil = rf_with_dilation(dilations)
    print(f'{str(dilations):<30} {std:>8} {dil:>12} {dil/std:>7.1f}x')

print('\nDilation multiplies RF with no extra parameters.')
print('HDC [1,2,5]: avoids gridding artifact (all positions covered).')
```

> **Transformer Global RF from Layer 1**: Vision Transformers (ViT) divide the image into patches and apply self-attention across all patch tokens. Every token attends to every other token from the very first layer — the receptive field is global immediately. CNNs build up their RF incrementally through depth. This is why ViTs excel at tasks requiring long-range dependencies (e.g., detecting relationships between distant image regions), while CNNs with local inductive bias often need fewer data to converge on spatially local tasks.

## Architecture RF Comparison

Different architectures achieve large RFs through different strategies. VGG-16 uses 13 conv layers of 3×3 with periodic 2×2 max-pooling, reaching a theoretical RF of 212×212 on the final conv layer. ResNet-50 uses bottleneck blocks with 1×1, 3×3, 1×1 convs and stride-2 for downsampling. The 1×1 convs do not grow the RF. DeepLab adds dilated convs to ResNet's later stages to prevent shrinking the RF while removing strides. ViT patches (16×16) give a fixed patch-level RF of 16 initially, then global through attention.

```python
import torchvision.models as models
import torch

def resnet50_rf():
    """Compute theoretical RF through ResNet-50 up to layer4."""
    layers = [
        {'name': 'conv1 7x7 s2',  'kernel': 7, 'stride': 2},
        {'name': 'maxpool 3x3 s2','kernel': 3, 'stride': 2},
        # layer1: 3 bottleneck blocks, each has 1x1, 3x3, 1x1
        *[{'name': f'l1.{i}.{n}', 'kernel': k, 'stride': 1}
          for i in range(3) for k, n in [(1,'pw1'),(3,'conv'),(1,'pw2')]],
        # layer2: stride-2 on first block's 3x3
        {'name': 'l2.0.pw1', 'kernel': 1, 'stride': 1},
        {'name': 'l2.0.conv', 'kernel': 3, 'stride': 2},
        {'name': 'l2.0.pw2', 'kernel': 1, 'stride': 1},
        *[{'name': f'l2.{i}.{n}', 'kernel': k, 'stride': 1}
          for i in range(1,4) for k, n in [(1,'pw1'),(3,'conv'),(1,'pw2')]],
    ]
    rf, jump = 1, 1
    for l in layers:
        k, s = l['kernel'], l['stride']
        rf = rf + (k - 1) * jump
        jump *= s
    return rf, jump

rf, jump = resnet50_rf()
print(f'ResNet-50 theoretical RF after layer2: {rf}x{rf}')
print(f'Total stride (jump): {jump}')
print('ResNet-50 full theoretical RF at output: ~483x483')
print('Effective RF typically ~100x100 (Gaussian centre-weighted)')
```

## RF Design Guidelines

Practical RF design follows a few guiding principles. For image classification, the RF should cover most of the input by the final conv layer — a 224×224 image needs an RF of at least 100–150 effective pixels. For object detection, the RF should match the object scale at each detection head — FPN (Feature Pyramid Network) uses multiple scales explicitly. For segmentation without downsampling (e.g., medical images), dilated conv is preferred to maintain resolution while expanding RF. For audio (e.g., WaveNet), exponentially growing dilation gives logarithmic RF growth — efficient for long-range temporal dependencies.

| RF Growth Strategy | RF Per Layer | Extra Params | Extra FLOPs | Spatial Resolution | Use Case |
| --- | --- | --- | --- | --- | --- |
| Stack 3×3 (s=1) | +2 per layer (linear) | None | None | Preserved | Depth-first, cheap local growth |
| Dilation d | +(2d) per layer | None | None | Preserved | Segmentation, audio (DeepLab, WaveNet) |
| Stride 2 / Pool | ×2 multiplier | None | None | Halved | Classification, detection backbone |
| Larger kernel k | +k-1 per layer | ×(k/3)² | ×(k/3)² | Preserved | Rare; two 3×3 preferred over one 5×5 |
| Global attention | Full image (1 layer) | O(n²) QKV | O(n²·d) | Preserved | ViT, SASA, non-local networks |

## Effective RF and Feature Importance

Because the effective RF is Gaussian-shaped and much smaller than the theoretical RF, architectural choices that seem to provide sufficient context may not in practice. Attention mechanisms (CBAM, SE blocks, Transformer layers) complement CNNs by providing a bypass route for long-range dependency modelling that the Gaussian-shaped ERF suppresses. Class Activation Mapping (CAM) and Grad-CAM exploit the spatial RF structure to visualise which input regions drive a classification decision, serving as a diagnostic tool for checking whether the network's attended regions match human intuition.

Deformable convolutions (Dai et al. 2017) learn spatial offsets for each kernel sampling location so the RF adapts dynamically to object shape rather than remaining a fixed grid. This improves detection of objects with irregular shapes and large aspect ratios. Deformable DETR uses deformable attention for multi-scale feature aggregation with adaptive RF. Dilated Residual Networks (DRN) remove strides in ResNet's last two stages and compensate with increasing dilation rates to maintain the full theoretical RF at higher spatial resolution.

- Grad-CAM uses the gradient of class score w.r.t. the last conv feature map for class-specific saliency maps.
- Local Attention (SASA) restricts self-attention to a local window — explicit RF control with O(n·w²) cost.
- torch.fx can trace a model graph and compute theoretical RF by tracking tensor shapes layer by layer.
- RF mismatch: if an object is larger than the network's ERF, accuracy collapses — a common failure mode on high-res inputs.

---

